and inverting (6.33), we obtain the caustic condition in the form

$$
\operatorname { d e t } \left| \frac { \partial \mathbf { q } } { \partial \mathbf { p } } \right| = \operatorname * { d e t } \left| \frac { \partial ^ { 2 } S } { \partial \mathbf { p } \partial \mathbf { p } } \right| = 0 .
$$

The map $\pmb { \mathrm { p } }  \pmb { \mathrm { q } }$ is given by the gradient of the function $S ( \mathbf { \mathfrak { p } } )$ according to (6.37).The classification of the locally generic forms of the simplest singularities (6.38) of gradient maps is the content of Thom's theorem, the cornerstone of catastrophe theory, presented in, for example, Poston and Stewart (1978). Generic singularities are those whose form remains invariant with respect to small alterations of the function $S ( \mathfrak { p } )$ The classification depends only on the dimension of configuration space. The simplest case is that of one freedom,for which the only structurally stable caustic is the fold,that is,the turning point already met in several examples. Folds also appear in higher-dimensional configuration spaces; this is the case of the fold lines in fig. 6.6c.The dimension of the locus of fold points is always one less than that of the configuration space; for example, folds will form two-dimensional surfaces in the case of a three-freedom system. For this reason folds are said to have codimension 1.

![](images/d18a33dc6b987ef607faf4cd37f1494a29cb8ae6cf9766965c4a38e88dda43b3.jpg)  
Fig.6.12. Cusp points are the generic projection of the meeting of smooth folds in the phase space.

Caustic lines can join at a cusp point (fig. 6.12). Cusps are the only other generic caustic in the plane. Since their dimension is two less than the configuration space, they are of codimension 2. Hence, they appear along lines in a three-dimensional space.So far we have not met any cusp point, but these can easily be obtained by rotating the torus offig. 6.6c by a group of symplectic transformations.The result is the same as the projection of a rotated tyre tube depicted in fig. 6.13.The numbers in the figure specify the multiplicity of $S ( \mathbf { q } )$ in each region.

Thom's theorem also furnishes the normal form to which we can reduce the action function $s ( \mathbf { \boldsymbol { p } } )$ by a canonical transformation near the generic caustic. The most elegant presentation in the context of Hamiltonian dynamics is that of Arnold (1978,app.12), who has considerably extended the classification of caustics.The idea is to use the mixed action function $S ( p _ { 1 } , \ldots , p _ { l } , q _ { l + 1 } , \ldots , q _ { L } ) ;$ ，which can be considered to be the Legendre transform of $S ( \mathbf { q } )$ with respect to $l$ variables,or the transform of $S ( \mathbf { \{ q \} } )$ with respect to $L - l$ variables. The transformation $\pmb { \mathrm { p } }  \pmb { \mathrm { q } }$ is given implicitly by

$$
q _ { i } = { \partial S } / { \partial p _ { i } } , \qquad p _ { j } = { \partial S } / { \partial q _ { j } }
$$

with $1 \leq i \leq l$ and $l < j \leq L$

A nonsingular region has the normal form

$$
A _ { 1 } { : } S = \sum _ { i } p _ { i } ^ { 2 } { : }
$$

![](images/0183b79a0665428e03ac6fe7666af3a2e50b874535bcbe5f2c36fc21986da35f.jpg)  
Fig.6.13.Cusps appear in the shadows of a semitransparent tyre tube as it is rotated froma horizontal toa vertical position.The numbersinthe figure indicate the multiplicity of the projection in each region.

that is, the Lagrangian manifold can be linearized in the absence of a caustic. For $L = 1$ ,the only generic singularity is the fold with the normal form

$$
\begin{array} { r } { A _ { 2 } { : } S = \pm p _ { 1 } ^ { 3 } . \qquad } \end{array}
$$

For $L > 1$ we obtain the normal form for the fold line $( L = 2 )$ ，the fold surface $( L = 3 )$ and so on, simply by adding $L - 1$ terms of the normal form $A _ { 1 }$ to $A _ { 2 }$ . This procedure for constructing the normal form for singularities in higher-dimensional spaces by adding $A _ { 1 }$ is also valid for the singularities that follow. For $L = 2$ the other generic caustic is the cusp, the normal form of which is

$$
A _ { 3 } ; S = \pm p _ { 1 } ^ { 4 } + q _ { 2 } p _ { 1 } ^ { 2 } .
$$

For $L = 3$ we have two new generic codimension-3 caustics:

$$
\begin{array} { c } { { A _ { 4 } { : } S = \pm p _ { 1 } ^ { 5 } + q _ { 3 } p _ { 1 } ^ { 3 } + q _ { 2 } p _ { 1 } ^ { 2 } , } } \\ { { } } \\ { { D _ { 4 } ^ { \pm } { : } S = \pm p _ { 1 } ^ { 2 } p _ { 2 } \pm p _ { 2 } ^ { 3 } + q _ { 3 } p _ { 2 } ^ { 2 } . } } \end{array}
$$

For $L = 4$ there is also

$$
\begin{array} { c } { { A _ { 5 } { : } S = \pm p _ { 1 } ^ { 6 } + q _ { 4 } p _ { 1 } ^ { 4 } + q _ { 3 } p _ { 1 } ^ { 3 } + q _ { 2 } p _ { 1 } ^ { 2 } , } } \\ { { } } \\ { { D _ { 5 } { : } S = \pm p _ { 1 } ^ { 2 } q _ { 2 } \pm p _ { 2 } ^ { 4 } + q _ { 4 } p _ { 2 } ^ { 3 } + q _ { 3 } p _ { 2 } ^ { 2 } , } } \end{array}
$$

and finally, for $L = 5$

$$
\begin{array} { r l } & { A _ { 6 } { : } S = \pm { p } _ { 1 } ^ { 7 } + q _ { 5 } { p } _ { 1 } ^ { 5 } + \cdots + q _ { 2 } { p } _ { 1 } ^ { 2 } , } \\ & { D _ { 6 } { : } S = \pm { p } _ { 1 } ^ { 2 } p _ { 2 } \pm { p } _ { 2 } ^ { 5 } + q _ { 5 } p _ { 2 } ^ { 4 } + q _ { 4 } p _ { 2 } ^ { 3 } + q _ { 3 } p _ { 2 } ^ { 2 } , } \\ & { E _ { 6 } { : } S = \pm { p } _ { 1 } ^ { 3 } \pm { p } _ { 2 } ^ { 4 } + q _ { 5 } p _ { 1 } q _ { 2 } ^ { 2 } + q _ { 4 } p _ { 1 } p _ { 2 } + q _ { 3 } p _ { 2 } ^ { 2 } . } \end{array}
$$

Arnold(1975)also studied the generic caustics for $L > 5$ ,but they cannot all be reduced to a discrete set.

The catastrophes $D _ { 4 } ^ { \pm }$ (6.44) are known as the umbilics. If both the first terms have the same sign, we have the hyperbolic umbilic $D _ { 4 } ^ { + }$ ; otherwise, the normal form represents the elliptic umbilic.

# Exercises

1. Show that the transformation

$$
p _ { 1 } = 2 ^ { - 2 / 3 } 3 ^ { 1 / 2 } ( { \mathfrak { p } } _ { 1 } - { \mathfrak { p } } _ { 2 } ) , \qquad p _ { 2 } = 2 ^ { - 2 / 3 } ( { \mathfrak { p } } _ { 1 } + { \mathfrak { p } } _ { 2 } )
$$

reduces the normal form for $D _ { 4 } ^ { + }$ to

$$
\pm { \mathfrak { p } } _ { 1 } ^ { 3 } \pm { \mathfrak { p } } _ { 2 } ^ { 3 } + 2 ^ { - 4 / 3 } q _ { 3 } ( { \mathfrak { p } } _ { 1 } + { \mathfrak { p } } _ { 2 } ) ^ { 2 } .
$$

Find the transformation ${ \mathfrak { q } } \to { \mathfrak { q } }$ that makes $( { \pmb { \mathsf { p } } } , { \pmb { \mathsf { q } } } ) \to ( { \pmb { \mathsf { p } } } , { \pmb { \mathsf { q } } } )$ a canonical transformation.

2. Show that the folds of a separable system meet each other along the $\mathfrak { q } _ { 3 } = 0$ (i.e., $q _ { 3 } = 0 \mathrm { . }$ ） section of the hyperbolic umbilic.

The double fold lines of a separable system do not meet at a cusp point, the only other generic singularity for a two-dimensional system. According to exercise 2 above, this meeting takes place in a section of a higher singularity. Thom's theorem thus leads us to expect that a small deformation of the torus will ‘almost always' unfold this singularity into generic caustics. These are obtained by taking sections of $D _ { 4 } ^ { + }$ with $q _ { 3 }$ small but finite; that is,we consider $q _ { 3 }$ not to be a coordinate in a higher-dimensional phase space but a parameter measuring the ‘departure from separability'. The result of the unfolding is shown in fig.6.14. The deformation of a separable torus in two dimensions may therefore have caustics resembling that of the torus with circular symmetry in fig. 6.13c.This is not the only possibility,however, since catastrophe theory provides only local results. Ozorio de Almeida and Hannay (1982) present transformations that bring separable tori into each of the configurations in fig. 6.15.

How sure can we be that a perturbation of-the torus is generic - that is, capable of unfolding the projection of the torus? There will obviously be no unfolding if the perturbed Hamiltonian is still separable. What about an invariant torus of a general $\pmb { \mathrm { p } } ^ { 2 } / 2 m + V ( \pmb { \mathrm { q } } )$ type of Hamiltonian?Even in this case,it was shown by Ozorio de Almeida and Hannay(1982) that there is no unfolding of the $D _ { 4 } ^ { + }$ corners because of the symmetry in the momenta. The unfoldings in fig.6.15 are all realized by breaking this symmetry. The central problem in utilizing Thom's theorem or other arguments based on genericity or structural stability is to know whether the perturbation is really generic or special, owing to a possibly hidden symmetry.

![](images/cdff28fe6e02abb3beaf8293e0ede8c1f08e074e46f825b533db5356b0c14fdb.jpg)  
Fig.6.14. The double fold lines of the hyperbolic umbilic are unfolded so that there are regions with zero,two or four pre-images on the torus.

![](images/e31e3c63e3f2cdc2975f1b2f1a406bddcc4e377d40ecbb319e4412f20b7f6b92.jpg)  
Fig. 6.15.Possible global unfoldings for a separable torus.

The original concept of caustic is that of an envelope of a family of trajectories. In our case the family is the projection onto configuration space of the orbits that wind around an invariant torus.When the orbits pass smoothly from one torus branch to another, their projections touch a caustic. The simplest example of a caustic is that of a hose sprinkling parallel jets of water (fig.6.16). The caustic is the horizontal line of maximum height attained by the water.It corresponds to a singularity in the density of orbits.If the orbits are identified with the light rays of optics, the resulting high intensity of light leads to ‘burning'-hence the name. Berry and Upstill(198O) provide a clear presentation of caustics and catastrophe theory in an intuitive optical context.

In an integrable system where the frequencies do not have a constant ratio,almost all tori have open orbits that are dense.It follows that we can take a single orbit as ‘the family' and obtain the caustic as the envelope of successive windings of this orbit. Furthermore, the integrability of the system can be ascertained if almost all orbits have caustic envelopes.As an example we first consider the circular billiard in fig. 6.17a. We know this to be an integrable system, because the force is central. Any orbit has a point of closest approach to the centre,at which it is tangent to an inscribed circle - the caustic.It is much harder to show directly that the elliptic billiard is an integrable system. However,in this case it is also true that any orbit has as envelope an inscribed curve,in this case a confocal ellipse (fig. 6.17b).

![](images/5647fd4cdca665f4618080aadb76f725a9e72adc2838d1dc6d6062590ee232b6.jpg)  
Fig. 6.16. One-dimensional water sprinkler. The horizontal line of highest ascent is an envelope of orbits,i.e., a caustic.

![](images/257c28d000111c094565a907f7beab60fe676c805db8e1870ccbdd8088c0857c.jpg)  
Fig. 6.17.(a) An orbit in a circular billiard has an inscribed circular envelope. The equality of the angles of incidence and reflection with respect to the radius leads to the conservation of angular momentum. (b) An orbit in an elliptic billiard also has an envelope -a confocal ellipse.The equality of the angles of incidence and reflection with respect to the lines to the foci at O and ${ \boldsymbol { 0 } } ^ { \prime }$ leads to the conservation of the product of angular momenta about O and ${ \mathfrak { V } }$

# Exercise

Show that the product $J _ { 0 } J _ { 0 ^ { \prime } }$ of the angular momenta about the foci O and $0 ^ { \prime }$ is conserved for the circular billiard.(Hint: The angles between the tangent to an ellipse, at a given point,and the two lines joining it to the foci are equal.)1

# 6.4 Perturbations and averaging

The introduction to the theory of integrable systems presented in the preceding sections will serve as the basis for the traditional treatment of the semiclassical limit of quantum mechanics in chapter 7.The very particular restrictions on integrable systems prevent them from being structurally stable.Thus,in spite of the great number of solved integrable problems in classical mechanics, one should not expect that a general perturbation will lead to a new integrable system. Yet it is still very worthwhile to base the understanding of nearly integrable systems on the unperturbed system. In section 6.5 we shall discuss the fundamental question of the survival of invariant tori subject to perturbations, the subject of the KAM theorem. We start with the discussion of approximate methods- that is,low-order perturbation theory and the averaging principle -which provide good quantitative results for limited time intervals.

It is convenient to study the flow of a perturbed system with the actionangle variables of the integrable system. The equations of motion for a quasi-integrable system have the form

$$
\begin{array} { l } { { \displaystyle { \dot { \phi } } = \pmb { \omega } _ { 0 } ( { \bf I } ) + \varepsilon { \bf f } ( { \bf I } , \phi ) , } } \\ { ~ } \\ { { \displaystyle { \dot { \bf I } } = \varepsilon { \bf g } ( { \bf I } , \phi ) } . } \end{array}
$$

If the Hamiltonian has the form

$$
H ( \mathbf { I } ) = H _ { 0 } ( \mathbf { I } ) + \varepsilon H _ { 1 } ( \mathbf { I } , \phi ) ,
$$

then

$$
{ \bf f } = \partial { \cal H } _ { 1 } / \partial { \bf I } \quad \quad \mathrm { a n d } \quad \quad { \bf g } = - \partial { \cal H } _ { 1 } / \partial \phi .
$$

Consider‘disconnecting the perturbation’ so that all the orbits are restricted to the invariant tori of $H _ { 0 }$ . We can then evaluate the time average of $\mathbf { g } ( \mathbf { I } , \pmb { \phi } ( t ) )$ . Almost all tori will have rationally independent frequencies, so the equivalence of time and configuration averages is valid:

$$
{ \bar { \bf g } } ( { \bf I } ) \equiv { \frac { 1 } { T } } \operatorname* { l i m } _ { T \to \infty } \int _ { 0 } ^ { T } { \bf g } ( { \bf I } , \phi ( t ) ) d t = ( 2 \pi ) ^ { - L } \int _ { 0 } ^ { 2 \pi } \cdots \int _ { 0 } ^ { 2 \pi } { \bf g } ( { \bf I } , \phi ) d \phi .
$$

In other words,the residue of the periodic force,

$$
\tilde { \mathbf { g } } ( \mathbf { I } , \boldsymbol { \phi } ) \equiv \mathbf { g } ( \mathbf { I } , \boldsymbol { \phi } ) - \bar { \mathbf { g } } ( \mathbf { I } ) ,
$$

has zero time average for periods $T$ much larger than the characteristic periods $2 \pi \omega _ { 0 } ^ { - 1 }$ of the integrable system. This suggests that, if we now reconnect the perturbation so that the system moves according to(6.5O), the effect of the force $\tilde { \bf g }$ will be small, provided that the‘inertia' $\varepsilon ^ { - 1 }$ of the system is large and the unperturbed periods are small. The system is already receiving a contrary force before it has had time to respond to the original force. This argument leads to the approximation of (6.50) by the averaged system

$$
\dot { \mathbf { I } ^ { \prime } } = \varepsilon \bar { \mathbf { g } } ( \mathbf { I } ^ { \prime } ) .
$$

This conjecture is confirmed for the following simple example presented by Arnold (1978, sec. 52):

$$
\dot { \phi } = \omega \neq 0 , \qquad \dot { I } = \varepsilon g ( \phi ) .
$$

The solution is

$$
\begin{array} { l } { { I ( t ) - I ( 0 ) = \displaystyle \int _ { 0 } ^ { t } \varepsilon g ( \phi _ { 0 } + \omega t ) d t = \displaystyle \int _ { 0 } ^ { t } \varepsilon \bar { g } d t + \frac { \varepsilon } { \omega } \int _ { \phi _ { 0 } } ^ { \phi _ { 0 } + t / \omega } \tilde { g } ( \phi ) d \phi } } \\ { { \quad \quad = \varepsilon \bar { g } t + \displaystyle \frac { \varepsilon } { \omega } h \biggl ( \displaystyle \frac { t } { \omega } \biggr ) , } } \end{array}
$$

where $h ( \phi )$ is a periodic function and therefore bounded. Thus, if $I ^ { \prime } ( t )$ is the motion of the averaged system, we have

$$
| I ( t ) - I ^ { \prime } ( t ) | < C \varepsilon ,
$$

where $C = \| h \| \omega ^ { - 1 }$ .The validity of the averaging principle for $L$ -freedom systems, subject to a perturbation depending on a single angle under quite general conditions, is also proved by Arnold (1978, sec.52); that is,

$$
| I ( t ) - I ^ { \prime } ( t ) | < C \varepsilon \qquad \mathrm { f o r } \qquad 0 \leq t \leq \varepsilon ^ { - 1 } .
$$

The averaging principle must be applied with care if the system has more than one freedom and the perturbation also depends on more than one angle.The problem resides in the tori with rationally dependent frequencies: An unperturbed periodic orbit will not average out a perturbation that depends on more than a single angle. If the frequency ratio $\omega _ { 1 } / \omega _ { 2 }$ is a low-order rational, the unperturbed periodic orbit will sample only an atypical part of ${ \bf g } ( \phi _ { 1 } , \phi _ { 2 } )$ ,and even the open orbits of neighboring tori will take a long time to sweep through allthe angles. We cannot apply the full averaging principle in such a region. Still it is possible to make a partial average along the direction of the unperturbed periodic orbit, the fast variable,while keeping the slow variables transverse to the motion generated by $H _ { 0 }$

A superior alternative to averaging away oscillatory terms of a Hamiltonian perturbation is to eliminate them by means of canonical transformations. We have already met a particular form of this procedure in chapter 4.There the unperturbed integrable Hamiltonian was quadratic, so that in the neighbourhood of the origin we could treat the higher-order angle-dependent terms in the Taylor expansion as the perturbation.We will now study the general perturbed Hamiltonian (6.51),following the presentation of Lichtenberg and Lieberman (1983).

The function $H _ { 1 }$ is multiply periodic in the angles $\pmb { \phi } ,$ ，so it can be developed in the Fourier series

$$
H _ { 1 } ( \mathbf { I } , \phi ) = \sum _ { \mathbf { m } } H _ { \mathrm { 1 m } } ( \mathbf { I } ) \exp ( i \mathbf { m } \cdot \phi ) .
$$

The Hamiltonian is then subject to a transformation $( { \bf I } , \phi ) \to ( { \bf I ^ { \prime } } , \phi ^ { \prime } ) .$ generated implicitly by

$$
S ( \mathbf { I } ^ { \prime } , \pmb { \phi } ) = \mathbf { I } ^ { \prime } \cdot \pmb { \phi } + \varepsilon S _ { 1 } ( \mathbf { I } ^ { \prime } , \pmb { \phi } ) ,
$$

where

$$
S _ { 1 } ( \mathbf { I } ^ { \prime } , \phi ) = \sum _ { \mathbf { m } } S _ { 1 \mathbf { m } } ( \mathbf { I } ^ { \prime } ) \exp ( i \mathbf { m } \cdot \phi ) .
$$

Differentiating,

$$
\begin{array} { r } { \mathbf { I } = \mathbf { I ^ { \prime } } + \varepsilon \partial S _ { 1 } ( \mathbf { I ^ { \prime } } , \pmb { \phi } ) / \partial \pmb { \phi } , } \\ { \mathbf { \phi } \ll \pmb { \phi } - \pmb { \phi } + \varepsilon \partial S _ { 1 } ( \mathbf { I ^ { \prime } } , \pmb { \phi } ) / \partial \mathbf { I ^ { \prime } } , } \end{array}
$$

we obtain the explicit transformation in the form

$$
\begin{array} { c } { { { \bf I } = { \bf I ^ { \prime } } + \varepsilon \partial S _ { 1 } ( { \bf I ^ { \prime } } , \phi ^ { \prime } ) / \partial \phi + O ( \varepsilon ^ { 2 } ) , } } \\ { { \phi = \phi ^ { \prime } - \varepsilon \partial S _ { 1 } ( { \bf I ^ { \prime } } , \phi ^ { \prime } ) / \partial { \bf I ^ { \prime } } + O ( \varepsilon ^ { 2 } ) . } } \end{array}
$$

The Hamiltonian is invariant with respect to this transformation, so

$$
H ^ { \prime } ( \mathbf { I } ^ { \prime } , \phi ^ { \prime } ) = H _ { 0 } ( \mathbf { I } ^ { \prime } ) + \varepsilon H _ { 1 } ( \mathbf { I } ^ { \prime } , \phi ^ { \prime } ) + \varepsilon \frac { \partial H _ { 0 } } { \partial \mathbf { I } ^ { \prime } } \cdot \frac { \partial S _ { 1 } } { \partial \phi ^ { \prime } } + O ( \varepsilon ^ { 2 } ) .
$$

We can now specify the function $S _ { 1 }$ so as to cancel the angular dependence of the linear part of $H ^ { \prime }$ .In this way the new Hamiltonian becomes integrable up to $O ( \varepsilon ^ { 2 } )$ 、The required condition is

$$
{ \pmb \omega } \cdot \frac { \partial S _ { 1 } } { \partial { \pmb \phi } ^ { \prime } } = - \sum _ { { \bf m } \neq 0 } H _ { \bf 1 m } ( { \bf I ^ { \prime } } ) \exp ( i { \bf m } \cdot { \pmb \phi } ^ { \prime } ) ,
$$

which yields

$$
S _ { 1 } ( \mathbf { I } ^ { \prime } , \phi ) = i \sum _ { m \neq 0 } \frac { H _ { \mathrm { 1 m } } ( \mathbf { I } ^ { \prime } ) } { \mathbf { m } \cdot \boldsymbol { \omega } } \exp ( i \mathbf { m } \cdot \phi ) .
$$

Once again we have to face the problem of small denominators. Generally the frequencies vary continuously among the tori, so the resonant tori, for which

$$
\mathbf { m } \cdot { \pmb { \omega } } ( { \bf { I } } ) = 0 ,
$$

are dense in phase space. We can study the first-order effect of the perturbation in the neighbourhood of a given resonant torus by adopting its periodic orbits as coordinates.In the case of two freedoms, the resonant torus will have frequencies

$$
\omega _ { 1 } / \omega _ { 2 } = s / r .
$$

If we choose one of the angular coordinates to be

$$
\phi = \phi _ { 1 } - s \phi _ { 2 } / r ,
$$

then $\dot { \phi } = 0$ on the unperturbed torus. We need a full canonical transformation $( I _ { 1 } , I _ { 2 } , \phi _ { 1 } , \phi _ { 2 } )  ( J , I , \theta , \phi )$ incorporating (6.67). This is implicitly defined by the generating function

$$
F = ( \phi _ { 1 } - s \phi _ { 2 } / r ) I + ( \phi _ { 2 } / r ) J ,
$$

so that the rest of the transformation becomes

$$
\theta = \phi _ { 2 } / r , \qquad I = I _ { 1 } , \qquad J = r I _ { 2 } + s I _ { 1 } .
$$

# Exercise

Find the irreducible circuits $\theta = 0$ and $\phi = 0$ on the torus and show that the respective symplectic areas are $2 \pi J$ and $2 \pi I$

This exercise identifies the variables $( J , \theta )$ with the periodic orbit variables introduced in section 2.5.In the present integrable case,each orbit belongs to a family with two parameters- the energy and the angle $\phi$ ·

$$
H = H _ { 0 } ( J , I ) + \varepsilon H _ { 1 } ( J , I , \theta , \phi ) ,
$$

where

$$
H _ { 1 } = \sum _ { k , m } H _ { k , m } ( J , I ) \exp \big \{ i [ k \phi + ( k s + m r ) \theta ] \big \} .
$$

Though we cannot average over both angles, this is a reasonable approximation for the fast variable $\theta$ The result is

$$
\begin{array} { r } { \overline { { H } } = H _ { 0 } ( J , I ) + \varepsilon \overline { { H } } _ { 1 } ( J , I , \phi ) , } \end{array}
$$

where

$$
\bar { H } _ { 1 } = \sum _ { n = 0 } ^ { \infty } H _ { - n r , n s } ( J , I ) \exp ( - i n r \phi ) .
$$

By abandoning the attempt to eliminate all the angular dependence of the Hamiltonian, we thus obtain an improved approximation. The Hamiltonian $\bar { H }$ is integrable, since $J$ is an independent constant of the motion.

# Exercise

Derive the approximation (6.72) of the Hamiltonian (6.70) through perturbation theory and show that the generating function for the corresponding canonical transformation has no smal denominators.Note that the identity of the two approximate Hamiltonians does not imply that the motion is the same.

If $\boldsymbol { \overline { { H } } } _ { 1 }$ is an analytic function (in a complex strip $| \operatorname { I m } \phi | < \rho )$ ,then the coefficients in the Fourier series (6.73) decay exponentially. The simplest case is the one in which the only nonzero terms have $| n | \leq 1 .$ For smallε we can then make an approximate Taylor expansion about the unperturbed periodic torus with actions $( I _ { 0 } , J _ { 0 } )$ ,to obtain

$$
\begin{array} { r } { \bar { H } = H _ { 0 } ( I _ { 0 } , J _ { 0 } ) + \varepsilon H _ { 0 , 0 } ( I _ { 0 } , J _ { 0 } ) + a ( \Delta I ) ^ { 2 } + \varepsilon b \cos ( r \phi ) . } \end{array}
$$

This approximation is known as a Chirikov resonance (see Chirikov,1979). We immediately recognize the pendulum Hamiltonian in the variables $( \Delta I , \phi )$ studied in section 4.4. There are $r$ families of islands, corresponding to a single family of island tori.These are centred by a single stable periodic orbit,and they are separated from the enveloping tori by the separatrices that emanate from the unique unstable periodic orbit. The inclusion of further terms in the series (6.73) merely distorts the pendulum tori if all the higher-order terms are small. In contrast, the inclusion of $\theta$ dependent terms will generally lead to homoclinic intersections of the separatrices and hence to the existence of chaotic orbits. The appearance of pairs of stable and unstable periodic orbits at a resonance of a perturbed integrable system can be proved by topological arguments. This is the content of the Poincaré-Birkhoff theorem,the proof of which is sketched by Berry (1978).

Ofcourse, we can apply the above theory again to the resonant island tori as in Lichtenberg and Lieberman (1983). These tori willbreak up into new islands and so on in an infinite hierarchy. The complexity of this picture leads to doubts that there is any truth in it. Do any tori survive the perturbation? This is the subject of the following section.

# 6.5 Discussion of the KAM theorem

A first approximation to the perturbed Hamiltonian (6.51) in the neighbourhood of a perturbed torus is given by(6.72)and(6.73).The appearance of unstable fixed points leads to motion that is radically different from that generated by the original Hamiltonian. Further perturbation from this resonant approximation still alters important features of the motion, but it gcnerally cannot bring back even distortions of the unperturbed tori usually destroyed in the resonant region. This is because the unstable periodic orbits willshow up as hyperbolic fixed points in a Poincaré section. These points with their separatrices are incompatible with the unperturbed lorus family. Nonetheless,unstable fixed points are structurally stable within a one-parameter family of maps,as was shown in section 2.5.

Taking into account allthe resonances up to a given order [defined as the biggest integer $| r |$ or $| s |$ in (6.66)], we obtain a picture such as fig. 6.18. The exponential decay of the coefficients $H _ { k , m }$ in (6.71)implies that the size of the resonance - that is the area between the separatrices - proportional to εb in (6.74)decreases exponentially with the order of the resonance.We can thus obtain a first approximation to the flow as a whole by extending fig. 6.18 to all orders of resonance, while omitting those higher-order resonances that overlap and hence are ‘swallowed up’ by lower-order resonances. The resonant tori are densely distributed in the unperturbed system. Can tori survive the perturbation in the midst of all the resonances?

![](images/03abf41239b2f7bf2ef7f7a9c6ddebb84b1cec5f19ec46f6850fe9ae9aa2c6b3.jpg)  
Fig. 6.18. Generally each region surrounding an unperturbed periodic torus wil develop a resonance, but the resonant region becomes very narrow for those tori with very long periodic orbits.

In the case of two freedoms, the Poincaré map for an unperturbed torus can be reduced to a translation on a circle.In chapter 5 we found that perturbations of this simple motion can still be reduced to it, provided that the rotation number is ‘sufficiently irrational'.In the present context the rotation number can be identified with the frequency ratio,which varies continuously among the tori. Resonant tori correspond to circle maps whose rotation numbers are rational. Therefore, the basic theorem in section 5.4 proves directly that, if a torus ‘sufciently far' from resonance survives a perturbation, its Poincaré map can be reduced to a translation; that is, its flow will be quasi-periodic, just as in the integrable system.

The demonstration that tori do actually survive is much more intricate than the theory of the circle map.I will sketch only briefly the proof of Arnold(1963). The first step is to show the convergence of the Fourier series for the generating function (6.58) of the canonical transformation $( I , \phi )$ $ ( \mathbf { I } ^ { \prime } , \pmb { \phi } ^ { \prime } )$ ,corresponding to first-order perturbation theory.To this end we assume that $H _ { 1 } ( \mathbf { I } , \phi )$ is analytic, with $\| H _ { 1 } \| < \varepsilon$ in a strip $| \operatorname { I m } \phi | < \rho$ (as with the circle map) and in a domain $G$ of $I$ .Convergence is proved in a reduced strip $| \operatorname { I m } \phi ^ { \prime } | < \rho - \delta$ and in a subdomain of $\pmb { G }$ .This includes all the tori with actions $\mathbf { I ^ { \prime } }$ and frequencies

$$
\pmb { \omega } ^ { \prime } = \hat { o } \pmb { H } ^ { \prime } / \hat { o } \pmb { \mathrm { I } } ^ { \prime }
$$

satisfying the Diophantine condition

$$
| \mathbf { \pmb { \omega } } ^ { \prime } \mathbf { \cdot } \mathbf { k } | \geq c | \mathbf { k } | ^ { - \nu } .
$$

The constants $c$ and $\nu$ depend only on ε and not on the integer vector $\mathbf { k }$

The result of this transformation is that the original Hamiltonian is reduced to the form

$$
H ^ { \prime } ( \mathbf { I } ^ { \prime } , \pmb { \phi } ^ { \prime } ) = H _ { 0 } ^ { \prime } ( \mathbf { I } ^ { \prime } ) + \varepsilon ^ { 2 } H _ { 2 } ^ { \prime } ( \mathbf { I } ^ { \prime } , \pmb { \phi } ^ { \prime } )
$$

along the tori satisfying (6.76). By applying Kolmogorov's method,as presented in section 5.4, it can now be shown that successive canonical transformations cancel the $\pmb { \phi }$ -dependent term while preserving a residual analyticity strip for the Hamiltonian.In this way the KAM theorem proves that the majority of the volume of phase space is occupied by invariant tori as $\varepsilon \to 0$ .Moser's demonstration of the survival of invariant curves in areapreserving maps relaxes the condition of analyticity on $H$ (Moser, 1962). On the other hand,Arnold's proof applies to perturbations of integrable systems with any number of freedoms.

The tori in the KAM theorem are specified by their frequencies (6.75)and (6.76). Therefore, the validity of the theorem depends on the nondegeneracy of the map $\mathbf { I } \to { \pmb { \omega } }$ ; that is, we must add the condition that

$$
\mathrm { d e t } | \hat { \sigma } ^ { 2 } H / \hat { \sigma } \mathbf { I } ^ { 2 } | \neq 0 .
$$

The KAM theorem can bc adapted to integrable systems that are perturbed by a time-periodic Hamiltonian, since this can always be transformed into an autonomous system in an expanded phase space (see section 2.5). An important corollary for a forced system with one freedom is that linearly stable equilibria are truly stable, even after the perturbation. The reason is that near the equilibrium the Hamiltonian can be approximated by the truncated Birkhoff normal form,as in section 4.4.The remainder can be considered to be a perturbation that vanishes as the equilibrium is approached. The KAM theorem thus guarantees the existence of invariant curves surrounding the equilibrium. The orbits within are continuous and cannot intersect the curves. Since invariant tori exist arbitrarily close to the equilibrium, the motion in its neighbourhood is stable.

The motion for an autonomous system with two freedoms is restricted to three-dimensional energy surfaces. The KAM theorem guarantees the survival of small two-dimensional Birkhoff tori with the same energy as that of a point oflinearly stable equilibrium.The equilibrium is inside any one of these tori on the energy shell.Thus,other orbits will remain within, even if they are not actually on a torus.The motion near a linearly stable periodic orbit of an autonomous two-freedom system is also stable, by a similar argument.

# Exercise

Explain why we must invoke the Birkhof normal form, rather than apply the KAM theorem directly to the integrable linearized system, by considering the whole nonlinear part as a perturbation.

The stability will be lost only when the last enveloping torus is destroyed. Presumably this torus is characterized by the frequency ratio most difficult to approximate by rationals. This conjecture has been computationally verified by Greene (1979) for the ‘standard map'.This large perturbation regime is not accessible to the KAM techniques -hence, the great interest in the adaptation by Escande (1985) of‘renormalization group' techniques to the study of the survival of tori subject to large perturbations.

A relatively recent discovery of great importance by Aubry (1978) and Percival (1979) is that of nonchaotic, nonperiodic orbits resulting from the destruction of nonresonant tori by large perturbations. General existence proofs are given by Katok (1982), Mather (1982) and Aubrey and Le Daeron (1983). This orbit maintains the same rotation number as on the torus before destruction, but it does not fill a torus densely. There are gaps,creating a structure described as a product of a torus with a Cantor set.These so-called cantori hinder the diffusion of chaotic orbits,as studied by Mackay,Meiss and Percival(1984). Immediately beyond the destruction of a torus, holes of the cantorus are exponentially small entailing exponentially slow diffusion through the gaps.

The situation for systems with three freedoms resembles that of the motion near cantori, even for arbitrarily small perturbations. The reason is that a three-dimensional torus does not separate the five-dimensional energy surface.It can be circumvented, just as a line in three-dimensional space.The Poincaré map for an integrable system will consist of linear translations along two-dimensional tori by angles $( 2 \pi \mu _ { 1 } , 2 \pi \mu _ { 2 } )$ All the tori with rotation numbers satisfying

$$
m _ { 1 } \mu _ { 1 } + m _ { 2 } \mu _ { 2 } = k
$$

are resonant. The KAM theorem-guarantees the survival of only sufficiently nonresonant tori. These are the ones that are not caught in Arnold's net, partially sketched in fig. 6.19. Each band in the net corresponds to one of the resonance conditions (6.79). They become exponentially narrow as the order of the resonance becomes large. Instead of an infinite number of separated chaotic regions,as with two freedoms, we have a single chaotic region that penetrates everywhere. Since the bands communicate, an orbit started inside the chaotic region of one particular band will be able to wander around and explore all the other bands. The net is dense on the square,so the orbit will be able to go everywhere.This is known as Arnold diffusion. The diffusion will be exponentially slow as $\varepsilon \to 0$ ,because of the exponential narrowness of the higher-order bands. This subject is extensively reviewed by Lichtenberg and Lieberman (1983).

![](images/984449914e0ccf5555b55bce698fd9249f8943318db3701bfad0012b7b3f93d0.jpg)  
Fig.6.19. The resonance condition establishes straight lines in the plane of rotation numbers $( \mu _ { 1 } , \mu _ { 2 } )$ for the unpcrturbed system. The resonant region for cach of these is thus a band. These are multiply connected in Arnold's net.

The proof in section 6.1 that the invariant tori of an integrable system are Lagrangian cannot be generalized to the survivors of a KAM perturbation. Nonetheless, this important property also holds for any invariant surface contained in an energy shell. This is a consequence of the same argument that led to the Poincaré-Cartan theorem in section 2.4.The full action

$$
\oint [ \mathbf { p } \cdot d \mathbf { q } - H d t ] = 0
$$

for any reducible closed circuit on the surface formed by a one-parameter family of trajectories in extended phase space.If all the orbits have the same energy, the loop can be projected into phase space, yielding

$$
\oint \mathbf { p } \cdot d \mathbf { q } = 0 .
$$

Thus, the invariant tori of a KAM system have caustics, just as do those of an integrable system. Moreover, their local features should have the generic properties allowed by catastrophe theory, unless there are special symmetries involved. Since all the invariant KAM tori have dense orbits, we can in principle determine whether an orbit belongs to a torus by simply graphing it in configuration space and watching out for envelopes. Figure 6.20 shows orbits computed by Ramaswamy and Marcus (1981)for a one-parameter family of quasi-integrable two-freedom Hamiltonians of the $\mathbf { p } ^ { 2 } + V ( \mathbf { q } )$ type.The first six graphs indicate the existence of a torus.Note the nongeneric meeting of the folds at the umbilic corners, due to the symmetry in p.The penultimate orbit is compatible with a thin island torus, since each thin ribbon shows afold.The last graph indicates chaotic motion constrained by surviving tori: There are bounds to the motion,but clearly some orbits turn before reaching this ‘outermost envelope'.The corresponding Poincaré sections are shown in fig. 6.1.

In a quasi-integrable system, we can be sure that an envelope for the successive windings of a trajectory is the signature of a torus. However, a more general system may have invariant surfaces with diferent topology. An example is provided by the ‘pseudointegrable' systems studied by Richens and Berry (1981), which appear among polygon billiards. Among these,a two-dimensional invariant surface may be a $g$ -handled sphere with $g > 1 ( g$ is called the genus of the surface). Ozorio de Almeida and Hannay (1982) present a rule for identifying $g$ from the caustics of a two-dimensional invariant surface: The tangent to a smooth closed line swings through a multiple of $2 \pi$ (it may self-intersect). If the closed line has cusps, however, it may swing through half-turns; that is,we consider the direction of the tangent line as that of a car traveling along a fold line, which backs away when it meets a cusp point. Then, if all the caustic lines are traversed the “same”way - that is, with the double layer of the fold always on the right (or always on the left)-the total number of rotations of the tangent line is $g - 1$ . For a torus with umbilic corners,because of symmetry, the rule must be applied to the unfolded projection,as in fig. 6.15.

We have now completed the outline of classical dynamics. Many subjects omited or merely touched upon are thoroughly discussed by Lichtenberg and Lieberman (1983), who also provide extensive references. My emphasis has been mainly on periodic orbits. In contrast to a dissipative system, where periodic orbits may be attractors, there is zero probability of the system being on a periodic orbit. However,we have seen many systems where periodic orbits are at least approximately dense.This is the case of integrable systems, simply because commensurable frequency ratios are dense among the real numbers. Perturbing these systems we generally destroy all the periodic tori. Yet isolated periodic orbits remain, half of which are stable.Around these we find nonresonant island tori, the periodic tori giving way to isolated periodic orbits and so on, in an ever finer selfsimilar structure. The complement of this figure is organized around the unstable periodic orbits,also present in the resonant region. Their separa-(rices generally have homoclinic or heteroclinic intersections-points of accumulation for infinite families of periodic orbits. Increasing the perturbation may bring about the destruction of most island tori and the period-doubling bifurcation cascades of the stable fixed points.The result is (he population of most of phase space by a multitude of unstable periodic orbits,as in the cat map, where they are proved to be dense.

The hypothesis that periodic orbits are dense means that all orbits can be well approximated by periodic orbits for arbitrarily long times. One of the guiding principles for research in this field since Poincaré has thus been the parallel studies of the local motion near periodic orbits and of their organization in phase space. The latter program is certainly at a much more incipient stage. All the same, it will be shown in chapter 9 that the same principle is also a valuable guide to the study of the semiclassical limit of quantum mechanics,our concern from here on.

![](images/ec21b7e23e81b4f3804d5c96af61c6237b0a2b8b4c37fd171edd1c4f8f732dc6.jpg)

![](images/ae08483e070268bbbcd03f83f0e946bbdde1a0d9134a62f2aeedb3c4c0fc211f.jpg)

# Part II

# Quantum dynamics

# Torus quantization

In principle allthe classical Hamiltonian systems studied in the first part of this book are only approximations to the systems of quantum mechanics. There are no unique rules for ascribing a quantum Hamiltonian to a known classical system. However, the inverse problem is perfectly well defined: Consider a quantum Hamiltonian $\hat { H } = H ( \hat { p } , \hat { q } ) ;$ ，a function of the position operators $\hat { \bf q } \equiv ( \hat { q } _ { 1 } , \dots , \hat { q } _ { L } )$ and the momentum operators $\hat { \bf p } \equiv ( \hat { p } _ { 1 } , \dots , \hat { p } _ { L } ) =$ $- \mathrm { i } \hbar \partial / \partial \mathbf { q } .$ ，where $\hbar$ is Planck's constant; then the corresponding classical Hamiltonian is simply ${ \check { H } } ( \mathbf { p } , \mathbf { q } )$ .Much more is understood about the classical motion than about the corresponding quantum system.In the semiclassical limit $\hbar  0$ (i.e., where the ratio of $\hbar$ to other relevant parameters of the motion is small), we can apply our understanding of classical dynamics to the study of wave functions, energy levels and other quantum mechanical entities.The behaviour that emerges must be distinguished from the strict classical limit, $\hbar = 0$ ,because of the nonanalyticity of quantum mechanics at $\hbar = 0$

The next three chapters are dedicated to the study of autonomous Hamiltonian systems. This chapter presents mainly the traditional semiclassical theory of the quantization of Lagrangian surfaces, which goes back to the work of Dirac,Van Vleck,Einstein,Brillouin, Keller and Maslov.The stationary states correspond to the invariant tori of classically integrable systems.This identification becomes even tighter in the Wigner-Weyl phase space representation,which is also discussed. The time cvolution of an open Lagrangian surface corresponds to a nonstationary state,with which we start our study. A particularly important example is Ihc semiclassical propagator, to be used as a tool for the study of nonintegrable systems in chapter 9.

# 7.1 Semiclassical wave functions

The Schrodinger equation determines the evolution of the wave function $\langle \mathbf { q } | \psi ( t ) \rangle$ generated by the Hamiltonian $H ( \pmb { \hat { \rho } } , \pmb { \ q } )$ in the coordinate

representation,

$$
i \hbar { \frac { \hat { \partial } } { \partial t } } \langle \mathbf { { q } } | \psi ( t ) \rangle = H ( { \hat { \mathbf { p } } } , \mathbf { { q } } ) \langle \mathbf { { q } } | \psi ( t ) \rangle ,
$$

where $\hat { \bf p } = - i \hbar \partial / \partial { \bf q }$ . The simplest case is that of a free particle,for which

$$
H ( \hat { \mathbf { p } } , \mathbf { q } ) = \hat { \mathbf { p } } ^ { 2 } / 2 m .
$$

The solutions are then plane waves

$$
\langle \mathbf { q } | \psi _ { \mathfrak { p } } ( t ) \rangle = \exp \{ \mathrm { i } \hbar ^ { - 1 } ( \mathbf { p } \cdot \mathbf { q } - E t ) \} ,
$$

where $E = \mathfrak { p } ^ { 2 } / 2 m$ is the particle energy. The plane wave (7.3) is the eigenfunction of the momentum operator,

$$
\hat { \mathbf { p } } \langle \mathbf { q } | \psi _ { \mathsf { p } } ( t ) \rangle = \mathbf { p } \langle \mathbf { q } | \psi _ { \mathsf { p } } ( t ) \rangle ,
$$

and its wavelength $\lambda = 2 \pi \hbar / | { \bf p } |  0$ as $\hbar  0$ for fixed $\pmb { \mathrm { p } }$

Let us consider now a general classical Hamiltonian $H ( \pmb { \mathsf { p } } , \pmb { \mathsf { q } } )$ in the neighbourhood of the coordinate ${ \mathfrak { q } } = { \mathfrak { q } } _ { 0 }$ . The error in approximating the Hamiltonian by $H ( \mathfrak { p } , \mathfrak { q } _ { 0 } )$ becomes arbitrarily smalas this neighbourhood is reduced. However,it still contains many wavelengths of the corresponding plane wave solutions of the Schrodinger equation in the limit of $\hbar  0$ .One way of obtaining the semiclassical limit of a general wave function is thus to subdivide the Hamiltonian in $J$ steps, centred on coordinates ${ \mathfrak { q } } _ { j }$ ,where $H$ $\mathbf { \mu } = H ( \mathbf { p } , \mathbf { q } _ { j } )$ . The solutions of the corresponding Schrodinger equation will be plane waves having $\mathbf { p } = \mathbf { p } _ { j }$ ,such that $H ( \boldsymbol { \mathbf { p } } _ { j } , \boldsymbol { \mathbf { q } } _ { j } ) = E$ , a constant. The problem is reduced in this way to matching the amplitude and phase of the plane waves at the common boundaries. This procedure is feasible and useful for one-dimensional problems, as reviewed by Berry and Mount (1972).

In general it is simpler to note that in the limit $J \to \infty$ we obtain a wave function whose exponent is no longer linear in $\mathbf { q }$ and that the amplitude is now a function of ${ \pmb q }$ .We therefore introduce the trial solution

$$
\langle \mathbf { q } | \psi ( t ) \rangle = A ( \mathbf { q } , t ) \exp [ i \hbar ^ { - 1 } \sigma ( \mathbf { q } , t ) ]
$$

into the Schrodinger equation (7.1), as in Dirac (1930). The resulting equation is

$$
i \hbar \frac { \partial A } { \partial t } - A \frac { \partial \sigma } { \partial t } = \exp ( - i \hbar ^ { - 1 } \sigma ) H ( \hat { \bf p } , { \bf q } ) \exp ( i \hbar ^ { - 1 } \sigma ) A .
$$

The right side divided by $\pmb { A }$ is the coordinate representation of the operator

$$
\exp [ - i \hbar ^ { - 1 } \sigma ( \hat { \bf { q } } , t ) ] H ( \hat { \bf { p } } , \hat { \bf { q } } ) \exp [ i \hbar ^ { - 1 } \sigma ( \hat { \bf { q } } , t ) ] = H ( \hat { \bf { p } } + \hat { \sigma } \sigma / \hat { \sigma } \hat { \bf { q } } , \hat { \bf { q } } ) .
$$

This is obtained by noting that exp $[ - i \hbar ^ { - 1 } \sigma ( \hat { \bf q } , t ) ]$ is a unitary operator for which

$$
\exp [ - i \hbar ^ { - 1 } \sigma ( { \bf { q } } , t ) ] { \hat { \bf p } } \exp [ i \hbar ^ { - 1 } \sigma ( { \hat { \bf { q } } } , t ) ] = { \hat { \bf p } } + { \hat { \sigma } } \sigma / { \hat { \sigma } } { \bf q }
$$

and that algebraic relations are preserved by unitary transformations. Thus, the Schrodinger equation takes on the exact form

$$
i \hbar { \frac { \partial A } { \partial t } } - A { \frac { \partial \sigma } { \partial t } } = H { \biggl ( } { \hat { \mathbf { p } } } + { \frac { \partial \sigma } { \partial \mathbf { q } } } , \mathbf { q } { \biggr ) } A .
$$

If we now neglect all the terms containing $\hbar$ , as a first approximation, there results

$$
H \left( \frac { \partial \sigma } { \partial \mathbf { q } } , \mathbf { q } \right) + \frac { \partial \sigma } { \partial t } = 0 .
$$

This is immediately recognised as the Hamilton-Jacobi equation of classical mechanics (Arnold, 1978;Goldstein,1980). Given any initial condition $\sigma ( \mathbf q , t _ { 0 } ) = S ( \dot { \mathbf q } )$ ，we obtain the solution as the action

$$
\begin{array} { c } { { \displaystyle \sigma ( { \bf q } , t ) = S ( { \bf q } _ { 0 } ) + \int _ { { \bf q } _ { 0 } , t _ { 0 } } ^ { { \bf q } , t } { \cal L } ( { \bf q } , \dot { \bf q } , t ) d t } } \\ { { \displaystyle = S ( { \bf q } _ { 0 } ) + \int _ { { \bf q } _ { 0 } , t } ^ { { \bf q } , t } \left\{ { \bf p } \cdot \dot { \bf q } - H \right\} d t } , } \end{array}
$$

where $L ( \mathbf { q } , { \dot { \mathbf { q } } } , t )$ is the Lagrangian of the system and the integration is carried out along the classical trajectories of $( \ P , t )$ space. The evolution of the surface

$$
\mathbf { p } ( \mathbf { q } , t ) = \hat { \alpha } \sigma / \hat { \alpha } \mathbf { q }
$$

in phase space corresponds to the semiclassical evolution of $\langle \mathbf { q } | \psi ( t ) \rangle$ . This surface is Lagrangian at any time, that is,

$$
\oint \mathbf { p } \cdot d \mathbf { q } = 0
$$

for any reducible closed loop contained in it.

We seek stationary solutions analogous to the plane waves (7.3). Then p(q) will be independent of $t$ and so

$$
\partial \sigma / \partial t = - { \cal H } ( { \bf p } , { \bf q } ) = - E ,
$$

I constant, that is,

$$
\pmb { \sigma } = S ( \mathbf { q } ) - E ( t - t _ { 0 } ) .
$$

The function $S ( \mathbf { q } )$ satisfies the equation

$$
H ( \partial S / \partial { \bf q } , { \bf q } ) = E ,
$$

also called the (stationary) Hamilton-Jacobi equation.In the simple case of the free particle with the Hamiltonian (7.2)and one freedom, the solution is

$$
S = \pm \int _ { q _ { 0 } } ^ { q } ( 2 m E ) ^ { 1 / 2 } d q = \pm ( 2 m E ) ^ { 1 / 2 } ( q - q _ { 0 } ) ,
$$

so the semiclassical solution is then exact.

We can consider the passage from(7.10)to(7.16)to be another instance of the reduction of the Hamiltonian by one freedom, due to the conservation of energy,as in section 2.5.This interpretation is made explicit by bringing forth the implicit function

$$
\frac { \partial S } { \partial q _ { 1 } } = - K \biggl ( \frac { \partial S } { \partial { \bf Q } } , { \bf Q } ; q _ { 1 } \biggr ) ,
$$

where $\mathbf { Q }$ are the remaining $L - 1$ coordinates, and interpreting $K$ as the reduced Hamiltonian and $- \ q _ { 1 }$ as the‘time'. This has the same form as (7.10), so any function ${ \cal S } _ { 0 } ( { \bf Q } _ { 0 } )$ will give rise to a solution $s ( \mathbf { Q } ; q _ { 1 } ) .$ generated by the trajectories of the reduced Hamiltonian according to (7.11). The problem is that, in contrast to time, the coordinate $q _ { 1 }$ will generally wind back over itself, if $H ( \mathfrak { p } , \mathfrak { q } ) = E$ is a compact surface. If we attempt to extend the local solution obtained from an arbitrary ${ \cal S } _ { 0 } ( { \bf Q } _ { 0 } ) .$ ， the‘returning solution' $S ( \mathbf { Q } ; q _ { 1 } )$ will not usually match smoothly back onto ${ \cal S } _ { 0 } ( { \bf Q } )$

The search for global solutions to (7.16) in the end falls back on the problem of the existence of invariant Lagrangian surfaces for a given Hamiltonian.As we saw in chapter 6, these surfaces foliate'the entire phase space of an integrable system. They are guaranteed to exist in quasi-integrable systems, yet they are completely absent from ergodic systems and from the chaotic regions of quasi-integrable systems. In the absence of invariant surfaces, the stationary wave function cannot have the simple form (7.5). Its general features are still a substantially open problem.

We shall now determine the amplitude $A$ of the wave function. Van Vleck (1928) derived it from the next term of an $\hbar ^ { n }$ expansion of equation (7.9). However,he also obtained it from a simple argument based on the uncertainty principle, which we here adopt.Let us consider the Lagrangian surface p(q as being part of a family.The standard case is that of a family of tori (which need not be invariant) $\mathfrak { p } ( \mathfrak { q } , \mathbf { I } )$ ,so we shall use the corresponding notation. We can then consider that the function $\pmb { \sigma } ( \ P , \mathbf { I } , t )$ [or $S ( \mathfrak { q } , \mathbf { I } ) ]$ generates a canonical transformation, defined by

$$
\partial \sigma / \partial { \bf q } = { \bf p } , \qquad \partial \sigma / \partial { \bf I } = \pmb { \phi } .
$$

In the semiclassical limit, we can take I and $\pmb { \phi }$ to correspond to quantum variables $\hat { \bf I }$ and $\hat { \pmb { \phi } }$ ，with commutators

$$
[ \hat { I } _ { i } , \hat { I } _ { j } ] = [ \hat { \phi } _ { i } , \hat { \phi } _ { j } ] = 0 , \qquad [ \hat { \phi } _ { i } , \hat { I } _ { j } ] = i \hbar .
$$

But $\mathbf { I }$ is a constant of the motion-it is known exactly. So in the $\pmb { \phi }$ representation the wave function $\langle \phi | \psi _ { \mathrm { I } } \rangle$ must have a constant amplitude. From the conservation of probability under a change of variables,

$$
| \langle \mathbf { q } | \psi _ { \mathbf { I } } \rangle | ^ { 2 } d \pmb { \phi } = | \langle \mathbf { q } | \psi _ { \mathbf { I } } ( t ) \rangle | ^ { 2 } d \mathbf { q } ,
$$

we thus obtain

$$
A ^ { 2 } = | \psi _ { \mathrm { I } } ( \boldsymbol { \mathbf { q } } ) | ^ { 2 } \propto \left| \operatorname* { d e t } \frac { \partial \phi } { \partial \boldsymbol { \mathbf { q } } } \right| = \left| \operatorname* { d e t } \frac { \partial ^ { 2 } \sigma } { \partial \boldsymbol { \mathbf { q } } \partial \boldsymbol { \mathbf { I } } } \right| .
$$

The semiclassical wavé functions corresponding to a family of Lagrangian surfaces with actions $\sigma ( \boldsymbol { \mathfrak { q } } , \mathbf { I } , t )$ therefore have the form

$$
\langle \mathbf { q } | \psi _ { I } ( t ) \rangle = c \left| \operatorname* { d e t } { \frac { \partial ^ { 2 } \sigma } { \partial \mathbf { q } \partial \mathbf { I } } } \right| ^ { 1 / 2 } \exp { \big \{ } i \hbar ^ { - 1 } \sigma ( \mathbf { q } , \mathbf { I } , t ) { \big \} } .
$$

# 7.2 Wave functions for invariant tori

Tori are invariant Lagrangian surfaces, but we found in chapter 6 that they are specified by a multivalued action ${ \cal S } _ { j } ( { \bf { q } } )$ .None of the layers is invariant on its own, though each of the actions $S _ { j } ( { \mathfrak { q } } )$ satisfies the stationary Hamilton-Jacobi equation (7.16). Therefore, the corresponding solution of the timeindependent Schrodinger equation is given by the superposition principle as

$$
 \mathbf { q }  \psi _ { \mathbf { I } }  = c \sum _ { j }  \operatorname* { d e t } \frac { \partial ^ { 2 } S _ { j } } { \partial \mathbf { q } \partial \mathbf { I } }  ^ { 1 / 2 } \exp \big \{ i \hbar ^ { - 1 } S _ { j } ( \mathbf { q } , \mathbf { I } ) + i \alpha _ { j } \big \} .
$$

The common real factor $c$ arises from the fact that the probability (7.21)is constant for each of the ranges of angles $\pmb { \phi }$ ,corresponding to each of the layers of the torus.The problem with this semiclassical wave function is that it diverges at the boundaries of the torus layers. By resolving this difficulty, we shall also determine the constant phases αj.

To start with, consider the simple one-freedom Hamiltonian of the form $H = p ^ { 2 } / 2 m + V ( q )$ The torus (the invariant closed curve) is a symmetric function of $p$ .The actions for both layers have the form

$$
S _ { \pm } ( q , I ) = \pm \int _ { q _ { 0 } } ^ { q } d q \{ 2 m [ E ( I ) - V ( q ) ] \} ^ { 1 / 2 } .
$$

Use of the chain rule and the fact that $d E / d I$ ，obtained from (6.20),is constant with the same value along both layers takes (7.24) into the form

$$
\begin{array} { l } { { \displaystyle { \langle q | \psi _ { I } \rangle = c \bigg | \frac { d E } { d I } \frac { 1 } { 2 } \big \{ 2 m [ E - V ( q ) ] \big \} ^ { - 1 / 2 } \bigg | ^ { 1 / 2 } \big \{ \exp \big ( i \hbar ^ { - 1 } S _ { + } + i \alpha _ { + } \big ) } } } \\ { { \displaystyle ~ + \exp \big ( i \hbar ^ { - 1 } S _ { - } + i \alpha _ { - } \big ) \big \} . } } \end{array}
$$

At the turning point $E = V ( q )$ ,the wave function diverges, though it has a finite integral. This wave function is identical with the Wentzel-Kramers-Brillouin approximation (see, e.g., Berry and Mount, 1972).

For a general torus wave function, the squared amplitude is given by

$$
\operatorname* { d e t } { \frac { \partial ^ { 2 } S } { \partial \mathbf { q } \partial \mathbf { I } } } { \mathit { \Gamma } } = \operatorname* { d e t } { \frac { \partial \phi } { \partial \mathbf { q } } } = \operatorname* { d e t } { \frac { \partial \phi } { \partial \mathbf { p } } } \operatorname* { d e t } { \frac { \partial \mathbf { p } } { \partial \mathbf { q } } } .
$$

At a caustic of the torus,the last determinant in(7.27) blows up,as discussed in section 6.3. This is a defect of the semiclassical wave function, but it is important to note again that the probability integral remains finite and the peak in the density reflects a real though finite increase in the probability amplitude near the caustic.

One way around this singularity of the wave function is to use the momentum representation. The semiclassical wave function is then

$$
\langle \pmb { \mathrm { p } } | \psi _ { \mathbf { I } } \rangle = c \sum _ { j } \left| \operatorname* { d e t } \frac { \partial ^ { 2 } S _ { j } ( \pmb { \mathrm { p } } ) } { \partial \pmb { \mathrm { p } } \partial \mathbf { I } } \right| ^ { 1 / 2 } \exp \big \{ - i \hbar ^ { - 1 } S _ { j } ( \pmb { \mathrm { p } } , \mathbf { I } ) + i \beta _ { j } \big \} ,
$$

where the action

$$
S _ { j } ( \mathbf { p } ) = \int _ { \mathbf { p } _ { 0 } } ^ { \mathbf { p } } \mathbf { q } _ { j } ( \mathbf { p } ) \cdot d \mathbf { p }
$$

is the Legendre transform of $S _ { j } ( { \bf q } )$ ,as in section 6.3.

# Exercise

Derive (7.28) directly as the stationary semiclassical approximation to the solution of the equation

$$
H ( \mathbf { p } , i \hbar \partial / \partial \mathbf { p } ) \langle \mathbf { p } | \psi \rangle = i \hbar \partial / \langle \mathbf { p } | \psi \rangle / \partial t
$$

using the trial solution

$$
\dot { } _ { - } \bf { j } | \psi ( t ) \rangle = { \cal A } \exp \{ i \hbar ^ { - 1 } [ - S ( { \bf p } ) - E t ] \} .
$$

We found in section 6.3 that ${ \bf q } ( { \bf p } )$ is also multivalued for an invariant torus and that the different layers join up exactly at the locus of |det $\partial ^ { 2 } S _ { j } / \partial \mathbf { p } \partial \mathbf { I } | = \infty$ . But these p caustics never coincide with the $\pmb q$ caustics. In the regions free of any kind of caustic, both representations should be equivalent.

They are, of course, related by the Fourier transform

$$
\langle \mathbf { q } | \psi \rangle = ( 2 \pi \hbar ) ^ { - L / 2 } \int d \mathbf { p } \langle \mathbf { p } | \psi \rangle \exp ( i \hbar ^ { - 1 } \mathbf { p } \cdot \mathbf { q } ) .
$$

Introducing(7.28) into (7.30), we obtain a sum of integrals. Each integrand has a classical amplitude |det $\partial ^ { 2 } S _ { j } / \partial \mathbf { p } \partial \mathbf { I } | ^ { 1 / 2 }$ ,independent of $\hbar$ ,multiplied by an oscillatory term. Any region of $\pmb { \mathrm { p } }$ with high-frequency oscillations will give a small contribution to the integral. This is dominated by the neighbourhoods of

$$
( \partial / \partial { \bf p } ) [ - S _ { j } ( { \bf p } , { \bf I } ) + i \hbar \beta _ { j } + { \bf p ^ { * } q } ] = - { \bf q } _ { j } ( { \bf p } ) + { \bf q } = 0 .
$$

Since the frequencies of oscillation are proportional to $\hbar ^ { - 1 }$ ，we can approximate each integral by the contributions of small neighbourhoods of the stationary points in the limit $\hbar  0$ According to (7.31) these are exactly the points on the torus ${ \pmb \ p } _ { j } ( { \pmb \ q } )$ that project down onto the point ${ \pmb q }$ The simplest case occurs when allthe stationary points are separated from one another by many wavelengths; precisely the case in which allcaustics are far away. Then the action in the neighbourhood of each stationary point can be approximated by

$$
S _ { j } ( \mathbf { p } , \mathbf { I } ) \simeq S _ { j } ( \mathbf { p } _ { j } , \mathbf { I } ) + \frac 1 2 ( \mathbf { p } - \mathbf { p } _ { j } ) \frac { \partial ^ { 2 } S _ { j } } { \partial \mathbf { p } ^ { 2 } } ( \mathbf { p } - \mathbf { p } _ { j } ) .
$$

The substitution of(7.32)for the exponent in the integrals (7.30) constitutes a good approximation in the dominant regions,while for the rest of the domain of integration the approximate integrals will also be highly oscillatory.

# Exercises

1. Show that

$$
\int _ { - \infty } ^ { \infty } d p \exp \bigg ( \frac { i \hbar ^ { - 1 } a p ^ { 2 } } { 2 } \bigg ) = \bigg ( \frac { 2 \pi \hbar } { a } \bigg ) ^ { 1 / 2 } \exp \bigg ( \frac { \mathrm { i } \pi \gamma _ { a } } { 4 } \bigg ) ,
$$

where $\gamma _ { a } \equiv a / | a |$ is the sign of $^ { a }$

2. A symmetric $L \times L$ matrix can be diagonalized byan orthogonal

transformation with unit Jacobian determinant. Hence, show that

$$
\int _ { - \infty } ^ { + \infty } d \mathbf { p } \exp \left\{ i ( 2 \hbar ) ^ { - 1 } \mathbf { p } \mathcal { A } \mathbf { p } \right\} = \left( \frac { ( 2 \pi \hbar ) ^ { L } } { | \det \mathcal { A } | } \right) ^ { 1 / 2 } \exp \left( \frac { i \pi \gamma _ { \mathcal { A } } } { 4 } \right) ,
$$

where $\gamma _ { \mathcal { A } }$ is the signature of $\mathcal { A }$ ,that is,the number of positive minus the number of negative eigenvalues of this matrix.

The stationary-phase approximation consists of the substitution of the phase $\hbar ^ { - 1 } S _ { j }$ by its quadratic approximation (7.31),while the relatively slowly varying amplitude is kept constant. Using (7.34), we obtain

$$
\begin{array} { l } { { ( 2 \pi \hbar ) ^ { - L / 2 } \displaystyle \int d { \bf p } \bigg | \operatorname* { d e t } \frac { { \partial ^ { 2 } S _ { j } } } { { \partial { \bf { p } } \partial \mathbf { I } } } \bigg | ^ { 1 / 2 } \exp \big \{ - i \hbar ^ { - 1 } [ { \bf { p } } \cdot { \bf { q } } - S _ { j } ( { \bf { p } } , { \bf { I } } ) ] + i \beta _ { j } \big \} } } \\ { { \displaystyle \qquad = \bigg | \operatorname* { d e t } \frac { { \partial ^ { 2 } S _ { j } } } { { \partial { \bf { p } } \partial \mathbf { I } } } \bigg | ^ { 1 / 2 } \bigg | \operatorname* { d e t } \frac { { \partial ^ { 2 } S _ { j } } } { { \partial { \bf { p } } ^ { 2 } } } \bigg | ^ { - 1 / 2 } \exp \big \{ i \hbar ^ { - 1 } [ { \bf { p } } _ { j } ( { \bf { q } } ) \cdot { \bf { q } } - S _ { j } ( { \bf { p } } _ { j } ( { \bf { q } } ) , { \bf { I } } ) ] + i \alpha _ { j } \big \} . } } \end{array}
$$

This expression is simplified by means of the identification

$$
\mathbf { p } _ { j } ( \mathbf { q } ) { \bf { \cdot q } } - S _ { j } ( \mathbf { p } _ { j } ( \mathbf { q } ) , \mathbf { I } ) = S _ { j } ( \mathbf { q } ) ,
$$

the Legendre transform. For the amplitude we have

$$
\left| \operatorname* { d e t } { \frac { \hat { \sigma } \mathbf { q } } { \partial \mathbf { I } } } \operatorname* { d e t } ^ { - 1 } { \frac { \hat { \sigma } \mathbf { q } } { \hat { \sigma } \mathbf { p } } } \right| ^ { 1 / 2 } = \left| \operatorname* { d e t } { \frac { \hat { \sigma } \mathbf { q } } { \partial \mathbf { I } } } \operatorname* { d e t } { \frac { \hat { \sigma } \mathbf { p } } { \hat { \sigma } \mathbf { q } } } \right| ^ { 1 / 2 } = \left| \operatorname* { d e t } { \frac { \hat { \sigma } \mathbf { p } } { \hat { \sigma } \mathbf { I } } } \right| ^ { 1 / 2 } = \left| \operatorname* { d e t } { \frac { { \hat { \sigma } } ^ { 2 } S _ { j } } { \hat { \sigma } \mathbf { q } \hat { \sigma } \mathbf { I } } } ( \mathbf { q } , \mathbf { I } ) \right| ^ { 1 / 2 } .
$$

The end result of taking the Fourier transform of $\langle \pmb { \mathrm { p } } | \psi _ { \mathbf { I } } \rangle$ in a region without caustics within the stationary-phase approximation is thus the semiclassical wave function $\langle \mathbf { q } | \psi _ { \mathrm { { I } } } \rangle$ . This consistency of the coordinate and the momentum representation, where both are nonsingular, allows us to define the semiclassical wave function $\langle \mathbf { q } | \psi _ { \mathrm { { I } } } \rangle$ near a caustic by the Fourier transform (7.3O). This manner of avoiding semiclassical singularities is known as Maslov's method. Its equivalent in optics was discovered by Keller (1958). Maslov's treatment (see Maslov and Fedorink, 1981) is considerably more abstract than this presentation,which follows Berry (1981a).

Two or more points ${ \pmb \ p } ( { \pmb q } )$ coalesce as one approaches a q caustic of the torus. The momenta of these points are defined by the stationary-phase condition (7.31). But the condition for the validity of the stationary-phase method is just that the stationary points be separated by many wavelengths, so this method cannot be applied close to a caustic. However, it is still true that the integral is dominated by the neighbourhoods of the points with stationary phase.

What we now need is an improvement of the too simple quadratic approximation to the action (7.32). This is readily supplied by the normal forms for the caustics presented in section 6.3. There exists a canonical transformation $( { \pmb { \mathsf { p } } } , { \pmb { \mathsf { q } } } ) \to ( { \pmb { \mathsf { p } } } , { \pmb { \mathsf { q } } } )$ ，such that $S ( { \mathfrak { p } } )$ is just one of the forms enumerated,depending on the local type of caustic. The wave function for $L = 1$ corresponding to the normal form of the action ${ \cal { S } } _ { A _ { j } }$ , (6.41), (6.42), (6.43),..., can be modelled by

$$
\langle q | \psi _ { A _ { j } } \rangle = \int _ { - \infty } ^ { \infty } d p \exp \big \{ i [ q p - S _ { A _ { j } } ( p ) ] \big \} ,
$$

known as a diffraction catastrophe integral. Analogous definitions hold for the other normal forms $D _ { j }$ ，and so on. For $L > 1$ we simply multiply $\langle q | \psi _ { A _ { j } } \rangle$ by

$$
\langle \mathbf { Q } | \dot { \psi } _ { A _ { 2 } } \rangle = \int _ { - \infty } ^ { \infty } d \mathbf { P } \exp \left\{ i ( \mathbf { Q } \cdot \mathbf { P } \mp \mathbf { P } ^ { 2 } ) \right\} ;
$$

that is,the other degrees of freedom will have normal coordinates where the action is just a Gaussian. Reduction to (7.39) thus amounts to performing a stationary-phase integration in the $\mathbf { P }$ variables‘transverse to the caustic'.

The simplest case is that of the fold $A _ { 3 }$ , for which $S _ { A _ { 3 } } ( p ) = - { p ^ { 3 } }$ . The stationary points $p ^ { \pm } ( q )$ meet at $p = 0$ (fig. 7.1). The catastrophe integral has the standard form

$$
\left. \mathbf { q } \right. \psi _ { A _ { 3 } } \rangle = \int _ { - \infty } ^ { \infty } { d p \exp \left\{ i ( p ^ { 3 } + q p ) \right\} } = 2 \pi 3 ^ { - 1 / 3 } A i ( 3 ^ { - 1 / 3 } q ) ,
$$

where $A i ( x )$ is the Airy function (Abramowitz and Stegun, 1964). Consider the family of curves for which the action is

$$
S ( p , I ) = - p ^ { 3 } / 3 + p I .
$$

The curves $q ( p , I ) = I - p ^ { 2 }$ are parabolas, so the parameter $\pmb { I }$ (not an action variable here) distinguishes each parabola by the point where it crosses the $q$ axis. The action measured from this point is

$$
S _ { \pm } ( q , I ) = \pm \int _ { I } ^ { q } \sqrt { I - q } d q = \mathfrak { f } ( I - q ) ^ { 3 / 2 } ,
$$

![](images/927f6fb0ccd67f987705544cc2e80e7050efb9b09630716be8410ce727b4aa17.jpg)  
Fig. 7.1.Normal form for the fold line $S _ { A _ { 3 } } ( p ) = - p ^ { 3 }$ . The stationary points $p ^ { \pm } ( q )$ meet at $p = 0$

and the corresponding wave function is

$$
\begin{array} { c } { { \displaystyle { \langle q | \psi _ { I } \rangle = c ( 2 \pi \hbar ) ^ { - 1 / 2 } \int _ { - \infty } ^ { \infty } d p \exp \{ i \hbar ^ { - 1 } \biggl [ \frac { p ^ { 3 } } { 3 } + ( q - I ) p ] \} } } } \\ { { = c ( 2 \pi \hbar ^ { - 1 / 3 } ) ^ { 1 / 2 } A i [ \hbar ^ { - 2 / 3 } ( q - I ) ] . } } \end{array}
$$

The maximum amplitude of $\langle q | \psi _ { I } \rangle$ does not fall exactly on the caustic $( q = I )$ ,as can be seen from the graph of the Airy function in fig. 7.2. However, this maximal point tends to the caustic as $\hbar  0$ .In this limit the amplitude diverges. The higher-order catastrophes diverge with higher fractional powers of $\hbar ^ { - 1 }$ .Thus,the torus caustics mark the semiclassical function in a characteristic way analysed by Berry,Hannay and Ozorio de Almeida (1983).We can compare (7.43) with its crude semiclassical approximation (7.24) by means of the asymptotic formula

$$
A i ( x ) \underset { x  \infty } { \longrightarrow } \pi ^ { - 1 / 2 } ( - x ) ^ { - 1 / 4 } \cos \big \{ \frac { 2 } { 3 } ( - x ) ^ { 3 / 2 } - \pi / 4 \big \} ,
$$

![](images/581bb3ad49acc6ab6fcd2a20ccbf2699d1cd093c9f6de87028f9483cfc36fec1.jpg)  
Fig. 7.2. Graph of the Airy function. The origin separates the region of exponential decay from the slowly decreasing oscillations.

given by Abramowitz and Stegun (1964,p. 448). Substituting this into (7.43) and using (7.42), we obtain

$$
\langle q | \psi _ { I } \rangle = c 2 ^ { 1 / 2 } \{ \exp [ i \hbar ^ { - 1 } S _ { + } ( q , I ) - i \pi / 4 ] + \exp [ i \hbar ^ { - 1 } S _ { - } ( q , I ) + i \pi / 4 ] \} .
$$

So we recover the semiclassical approximation, which is valid away from the caustic. As a bonus we have deduced that the phase change is $\pi / 2$ for crossing the fold from the branch $S _ { + }$ to $s _ { - }$ ; that is, we have determined the phases $\alpha _ { j }$ in (7.24).

The wave function (7.43) corresponds exactly to the momentum wave function $\exp { \{ i \hbar ^ { - 1 } [ ( p ^ { 3 } / 3 ) - p I ] \} }$ . Generally a semiclassical momentum wave function near a fold can be brought to this form by a canonical transformation of the phase space coordinates. But $S ( p , I )$ will usually have a more complicated dependence on $I _ { \mathrm { { ; } } }$ , so the amplitude of the wave function will not be constant,and it will also have to be multiplied by the Jacobian of the transformation. This considerably complicates the task of deriving a uniform approximation to $\langle q | \psi \rangle$ based on (7.40) or (7.38). The problem is to guarantee that each stationary point contributes with its correct amplitude. The general method presented by Berry(1976) provides excellent quantitative results.The qualitative features are analogous to our simple example.

# 7.3 The energy spectrum

We found in the previous section that the semiclassical wave function gains a phase of $\pi / 2$ as it pusses from a branch where $\partial \boldsymbol { q } _ { 1 } / \partial p _ { 1 } < 0$ to one where $\partial \boldsymbol { q } _ { 1 } / \partial p _ { 1 } > 0$ .The equation that determines a fold is just $d q _ { 1 } / d p _ { 1 } = 0$ for a one-freedom system, whereas if $L > 1$ , we usually have to transform to new coordinates $( p _ { 1 } , { \bf P } , q _ { 1 } , { \bf Q } )$ ，such that $\partial q _ { 1 } / \partial p _ { 1 } = 0$ is the fold equation. The Maslov index $\mu$ for a closed curve is the number of times that $\partial { \boldsymbol { q } _ { 1 } } / \partial { \boldsymbol { p } _ { 1 } }$ becomes positive minus the number of times that $\partial { \boldsymbol { q } _ { 1 } } / \partial { \boldsymbol { p } _ { 1 } }$ becomes negative, as we go once around the curve. The definition is the same for any number of freedoms. If $L > 1$ , then the curve is on a Lagrangian surface (manifold) and $\partial { \boldsymbol { q } _ { 1 } } / \partial { \boldsymbol { p } _ { 1 } }$ changes sign each time the curve crosses a fold, Arnold (1967) proved that the Maslov index is a topological invariant of a Lagrangian torus.

For an anticlockwise circuit along a closed curve on the $( p , q )$ plane, such as fig.7.3, the Maslov index is $\mu = 2$ ，so the wave function gains the total phase $\mu \pi / 2 = \pi$ on returning to the point $q _ { 0 }$ after a whole turn. Let us follow through the changes of the wave function step by step. If we define $s _ { + } ( q )$ such that $S _ { + } ( q _ { 0 } ) = 0 $ ,then the wave function for the upper branch is

$$
\langle q | \psi _ { + } \rangle = A _ { + } ( q ) \exp \left\{ i \hbar ^ { - 1 } S _ { + } ( q , I ) \right\}
$$

![](images/27811d241f600311021c29010ea94b1b7ffbc9ef2cfce7f446ad76dfd1608da6.jpg)  
Fig.7.3.The phase of the wave function, as we proceed clock wise, depends on the shaded area and on the phase gains of $\pi / 2$ as a caustic is traversed. Quantization is obtained by requiring self-consistency of the wave function.

within a constant phase. Beyond the fold at $q ^ { + }$ ， we have

$$
\langle q | \psi _ { - } \rangle = A _ { - } ( q ) \exp { \{ i \hbar ^ { - 1 } S _ { - } ( q , I ) + i \pi / 2 \} } ,
$$

where

$$
S _ { - } ( q , I ) = \int _ { q _ { 0 } } ^ { q ^ { + } } p _ { + } ( q ) d q + \int _ { q ^ { + } } ^ { q } p _ { - } ( q ) d q
$$

is the shaded area in fig.7.3. On passing the other fold at $q ^ { - }$ ,we obtain

$$
\langle q | \psi _ { + } ^ { \prime } \rangle = A _ { + } ( q ) \exp { \left\{ i \hbar ^ { - 1 } S _ { + } ^ { \prime } ( q , I ) + i \pi \right\} } ,
$$

where

$$
S _ { + } ^ { \prime } ( q , I ) = S _ { + } ( q , I ) + \oint p d q .
$$

The wave function cannot depend on the number of times we go around the closed curve. So the identity $\langle q | \psi _ { + } ^ { \prime } \rangle = \langle q | \psi _ { + } \rangle$ determines the semiclassical quantization condition

$$
\oint _ { } ^ { } p d q = 2 \pi \hbar ( n + { \textstyle \frac { 1 } { 2 } } ) .
$$

The presence of extra folds along the closed curve does not alter the Maslov index,because extra folds are created in pairs making opposite contributions to the index. The general condition (for $L = 1 \AA$ ）is therefore

$$
\oint p d q = 2 \pi \hbar { \Bigg ( } n + { \frac { \mu } { 4 } } { \Bigg ) } .
$$

For a nonlinear oscillator $\mu = 2$ ,whereas for a rotor $\mu = 0$ If $L > 0$ we can choose $L$ independent irreducible circuits $\gamma _ { l }$ in a way that they cross only folds, without touching any higher caustic.The self-consistency of the wave function after returning along any of these circuits entails the $L$ conditions for torus quantization:

$$
\int _ { \gamma _ { l } } \mathbf { p } \cdot d \mathbf { q } = 2 \pi I _ { l } = 2 \pi \hbar { \bigg ( } n _ { l } + { \frac { \mu _ { l } } { 4 } } { \bigg ) } .
$$

The quantization conditions go back to the old quantum theory. They are the result of work by Bohr, Sommerfeld,Einstein,Brillouin, Keller and Maslov.

The energy spectrum for an integrable system is given explicitly by the equations

$$
\begin{array} { r } { E _ { \mathfrak { n } } = H [ \hbar ( \mathfrak { n } + \pmb { \mu } / 4 ) ] ; } \end{array}
$$

that is, the eigenenergies correspond to level surfaces of the Hamiltonian,

![](images/2291fc0f3f2ca51aaf054b2b477f723b981f6302851082e3ac0bfb75d86ce905.jpg)  
Fig. 7.4. In a semiclassical regime the lattice of quantized tori becomes quite dense. The sequence of quantized tori of increasing energy will not then generally be close together.

which touch some point of the latice of quantized actions $\mathbf { I } = \hbar ( \mathbf { n } + \pmb { \mu } / 4 )$ Figure 7.4 shows the case of a nonlinear oscillator $\pmb { \mu } = ( 2 , 2 )$

# 7.4 The Weyl transform and the Wigner function

We shall be concerned mainly with the semiclassical limit of pure states. However, it should be noted that the torus quantization conditions imply that the average separation between energy levels tends to zero as $\hbar  0$ Hence,any imprecision in an energy measurement will prevent us from distinguishing the pure state of the system. In this case we must resort to a statistical description,by means of the density operator

$$
\hat { \rho } = \sum _ { n } a _ { n } | \psi _ { n } \rangle \langle \psi _ { n } | .
$$

In this formalism the probability of finding the system at the position $\pmb q$ is given by the diagonal elements of the density matrix $\langle { { \bf { q } } | \hat { \rho } | { \bf { q } } ^ { \prime } } \rangle$ ：

$$
\langle \mathbf { q } | { \hat { \rho } } | \mathbf { q } \rangle = \sum _ { n } a _ { n } | \langle \mathbf { q } | \psi _ { n } \rangle | ^ { 2 } .
$$

Integrating over ${ \mathfrak { q } } .$ ,we arrive at the interpretation of $a _ { n }$ as the probability that the pure state is $| \psi _ { n } \rangle$ .Thus,the density matrix for a pure state $| \psi _ { n } \rangle$ has $a _ { m } = \delta _ { n m } .$

The Weyl transform of any operator $\hat { A }$ is defined as

$$
{ \cal A } _ { w } ( { \bf p } , { \bf q } ) \equiv \int d { \bf y } \langle { \bf q } + { \bf y } / 2 | \hat { A } | { \bf q } - { \bf y } / 2 \rangle \exp ( - i \hbar ^ { - 1 } { \bf p } \cdot { \bf y } ) .
$$

In this way we associate a function in phase space to any operator $\hat { A }$ By inverting this Fourier transform we obtain a unique operator $\hat { A }$ specified by $A _ { w } ( \mathfrak { p } , \mathfrak { q } )$ .In some simple cases $A _ { \mathbf { w } } ( \mathbf { p } , \mathbf { q } )$ will equal the classical variable $A ( \mathbf { p } , \mathbf { q } )$

# Exercises

1. Show that if $\hat { A } = f ( \hat { \mathbf { { q } } } ) ;$ ，then $A _ { \mathrm { w } } ( \mathbf { p } , \mathbf { q } ) = f ( \mathbf { q } )$   
2. Show that if ${ \hat { A } } = f ( { \hat { \mathbf { p } } } ) .$ ，then $A _ { \mathrm { w } } ( \mathbf { p } , \mathbf { q } ) = f ( \mathbf { p } )$

It follows from these two results that the Weyl transform of a Hamiltonian $\hat { \pmb { p } } ^ { 2 } / 2 m + V ( \hat { \pmb { { q } } } )$ equals the corresponding classical Hamiltonian.

The Weyl transform of the density operator ${ \hat { \rho } } / ( 2 \pi \hbar ) ^ { L }$ ，

$$
W ( { \bf { p } } , { \bf { q } } ) \equiv ( 2 \pi \hbar ) ^ { - L } \int d { \bf { x } } \times \langle { \bf { q } } + { \bf { y } } / 2 | \hat { \rho } | { \bf { q } } - { \bf { y } } / 2 \rangle \exp ( - i \hbar ^ { - 1 } { \bf { p } } \cdot { \bf { y } } ) ,
$$

is known as the Wigner function (Wigner,1932). It furnishes a‘quasiprobability density' in phase space, in the sense that its projection,

$$
\int W ( \mathbf { p } , \mathbf { q } ) d \mathbf { p } = \langle \mathbf { q } \vert \hat { \rho } \vert \mathbf { q } \rangle ,
$$

is a true probability density, though $W ( \mathbf { p } , \mathbf { q } )$ may be negative in some regions. Integrating (7.59) over $\pmb q$ results in the normalization condition

$$
\int W ( { \mathfrak { p } } , { \mathfrak { q } } ) d { \mathfrak { p } } d { \mathfrak { q } } = 1 .
$$

A pair of simple examples,discussed by Ozorio de Almeida and Hannay (1982), increases our intuitive grasp of the Wigner function for pure states. The first considers a travelling wave in the interval $( - d / 2 , d / 2 )$ ，with pcriodic boundary conditions:

$$
\langle q \vert \psi \rangle = d ^ { - 1 / 2 } \exp ( i \hbar ^ { - 1 } p _ { 0 } q ) ,
$$

where $p _ { 0 } = 2 \pi n \hbar / d$ .Inserting the corresponding density matrix into (7.58),

we obtain

$$
W ( p , q ) = \frac { 1 } { \pi d } \frac { \sin \left[ d \hbar ^ { - 1 } ( p - p _ { 0 } ) \right] } { p - p _ { 0 } } \underset { \hbar \to 0 } { \longrightarrow } \frac { 1 } { d } \delta ( p - p _ { 0 } ) .
$$

The Wigner function is independent of $q$ 、In the semiclassical limit it ‘condenses' onto the classical Liouville probability density - a $\delta$ function on the horizontal line $\pmb { p } = \pmb { p _ { 0 } }$

Replacing the boundary condition by hard walls at $\pm d / 2$ leads to the wave function

$$
\langle q | \psi \rangle = ( 2 / d ) ^ { 1 / 2 } \cos ( \hbar ^ { - 1 } p _ { 0 } q ) .
$$

The corresponding Wigner function is

$$
W ( p , q ) = \frac 1 { 2 \pi d } \left\{ \frac { \sin \left[ d \hbar ^ { - 1 } ( p - p _ { 0 } ) \right] } { p - p _ { 0 } } + \frac { \sin \left[ d \hbar ^ { - 1 } ( p + p _ { 0 } ) \right] } { p + p _ { 0 } } \right.
$$

$$
+ \frac { 2 \cos ( 2 \hbar ^ { - 1 } p _ { 0 } q ) \sin ( d \hbar ^ { - 1 } p ) } { p } \Bigg \} .
$$

In the limit $\hbar  0$ the two first terms ‘condense' onto the classical manifold $p = \pm p _ { 0 }$ ,in the same way as for the travelling wave.But now there is also a nonclassical term.This interference term oscillates along the $q$ axis itself, and it is essential for the correct oscillating projection of $| \langle q | \psi \rangle | ^ { 2 }$ onto the $q$ axis:

$$
\int d p W ( p , q ) = d ^ { - 1 } [ 1 + \cos ( 2 \hbar ^ { - 1 } p _ { 0 } q ) ] = 2 d ^ { - 1 } \cos ^ { 2 } ( \hbar ^ { - 1 } p _ { 0 } q ) .
$$

The Wigner functions for both examples are depicted in fig.7.5.In the classical limit, the oscillations of $| \langle q | \psi \rangle | ^ { 2 }$ become infinitely rapid, so we can measure only its average $\overline { { | \langle q | \psi \rangle | ^ { 2 } } } = 1 / d$ ，By the same token, the interference term of the Wigner function can be considered to vanish as a consequence of its infinitely rapid positive and negative oscillations. The resulting Wigner function thus corresponds to the classical probability density.

An alternative representation of the Wigner function is

$$
W ( { \bf p } , { \bf q } ) = ( 2 \pi \hbar ) ^ { - L } \sum _ { n } a _ { n } \langle \psi _ { n } | \hat { W } | \psi _ { n } \rangle ,
$$

introducing the Weyl operator,

$$
\begin{array} { r l r } { \hat { W } = \displaystyle \int d { \bf y } | { \bf q } - { \bf y } / 2 \rangle \langle { \bf q } - { \bf y } / 2 | \exp ( - i \hbar ^ { - 1 } { \bf p } \cdot { \bf y } ) } & { } & \\ { = \displaystyle \int d { \bf y } | { \bf p } - { \bf y } / 2 \rangle \langle { \bf p } + { \bf y } / 2 | \exp ( + i \hbar ^ { - 1 } { \bf q } \cdot { \bf y } ) . } & { } & \end{array}
$$

![](images/3bf4cd969509f4637a80e98ba3ed98fe17ea9a66f5cf3663e5fe569ef17e8bc0.jpg)  
Fig.7.5.Wigner function for a box with periodic conditions (a) and with hard walls (b).

From the Heisenberg equation for the evolution of an operator, we then obtain the time evolution of the Wigner function as

$$
\frac { \partial W } { \partial t } { = } \frac { 1 } { i \hbar } \sum _ { n } a _ { n } \langle \psi _ { n } | ( \hat { W } \hat { H } - \hat { H } \hat { W } ) | \psi _ { n } \rangle ,
$$

where the states $| \psi _ { n } \rangle$ remain constant in time.

This equation takes on a particularly simple form in the case where $\hat { H }$ is a quadratic Hamiltonian, that is, for one degree of freedom:

$$
2 \hat { H } = H _ { q q } \hat { q } ^ { 2 } + H _ { p q } ( \hat { q } \hat { p } + \hat { p } \hat { q } ) + H _ { p p } \hat { p } ^ { 2 } .
$$

# Exercise

Use (7.67) to demonstrate the relations

$$
\begin{array} { l l } { { \hat { q } \hat { W } = \left( q + \frac { \hbar } { 2 i } \frac { \partial } { \partial p } \right) \hat { W } , } } & { { \hat { W } \hat { q } = \left( q - \frac { \hbar } { 2 i } \frac { \partial } { \partial p } \right) \hat { W } ; } } \\ { { \hat { p } \hat { W } = \left( p - \frac { \hbar } { 2 i } \frac { \partial } { \partial q } \right) \hat { W } , } } & { { \hat { W } \hat { p } = \left( p + \frac { \hbar } { 2 i } \frac { \partial } { \partial q } \right) \hat { W } . } } \end{array}
$$

Inserting these relations in (7.68), we obtain

$$
\begin{array} { c } { \displaystyle { \frac { \partial W } { \partial t } = \frac { 1 } { i \hbar } \sum _ { n } a _ { n } \langle \psi _ { n } | \biggl [ \displaystyle \frac { - \hbar } { i } H _ { q q } q \frac { \partial \hat { W } } { \partial p } + \frac { \hbar } { i } H _ { p q } \biggl ( - p \displaystyle \frac { \partial \hat { W } } { \partial p } + q \frac { \partial \hat { W } } { \partial q } \biggr ) } } \\ { \displaystyle { + \frac { \hbar } { i } H _ { p p } p \displaystyle \frac { \partial \hat { W } } { \partial q } \biggl ] | \psi _ { n } \rangle } } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle = ( H _ { q q } q + H _ { p q } p ) \frac { \partial W } { \partial p } - ( H _ { p q } q + H _ { p p } p ) \frac { \partial W } { \partial q } } } \\ { ~ } \\ { { \displaystyle = \frac { \partial H } { \partial q } \frac { \partial W } { \partial p } - \frac { \partial H } { \partial p } \frac { \partial W } { \partial q } = \{ H , W \} } . }  \end{array}
$$

Thus, the evolution of the Wigner function in this case is exactly the same as that of the classical Liouville distribution, since (7.71) is just the continuity equation for the ‘incompressible' flow in phase space. This result cannot be generalized for nonquadratic Hamiltonians. For instance,equation (7.7) establishes a quantum mechanical equivalence for nonlinear shear transformations in phase space. These do not alter the projections onto the $\pmb q$ axes of the Wigner function, though the latter is not itself invariant.

A classical quadratic Hamiltonian generates a linear vector field.As we found in section 1.2, the corresponding flow constitutes a group of symplectic (linear canonical) transformations. The Wigner function is therefore invariant with respect to the symplectic transformations. Since the Wigner function is a complete representation of the quantum state, we can obtain a new density matrix $\rho ( \mathfrak { q } , \mathfrak { q } ^ { \prime } )$ by taking the Weyl transform of $\rho ( \mathfrak { q } , \mathfrak { q } ^ { \prime } ) .$ ，then performing the symplectic transformation $( { \pmb { \mathsf { p } } } , { \pmb { \mathsf { q } } } ) \to ( { \pmb { \mathsf { p } } } , { \pmb { \mathsf { q } } } )$ and finally taking the inverse of the Weyl transform. Once a pure Wigner function has been derived, we obtain a new wave intensity $| \langle { \mathfrak { q } } | \psi \rangle | ^ { 2 }$ simply by projecting $W ( \pmb { \mathfrak { p } } , \pmb { \mathfrak { q } } )$ onto the $\pmb q$ axes. These can be chosen to lie on any Lagrangian plane.

# 7.5 Semiclassical Wigner functions

To obtain the semiclassical Wigner function for a pure state $| \psi _ { n } \rangle$ we construct the density matrix $\langle \mathbf { q } | \psi _ { n } \rangle \langle \psi _ { n } | \mathbf { q } ^ { \prime } \rangle$ with the semiclassical wave function(7.24) and insert it into (7.58). For one branch of the wave function corresponding to the torus I, we then have

$$
\begin{array} { c } { { W _ { \bf { r } } ( { \bf { p } } , { \bf { q } } ) = c ^ { 2 } ( 2 \pi \hbar ) ^ { - L } \displaystyle \int d { \bf { y } } \exp \left\{ { i \hbar ^ { - 1 } [ { \cal S } ( { \bf { q } } + { \bf { y } } / 2 , { \bf { I } } ) - { \cal S } ( { \bf { q } } - { \bf { y } } / 2 , { \bf { I } } ) - { \bf { p } } \cdot { \bf { y } } { \bf { J } } ] } \right\} } } \\ { { \times | \operatorname* { d e t } \displaystyle \frac { \partial ^ { 2 } { \cal S } } { \partial { \bf { q } } \partial { \bf { I } } } ( { \bf { q } } + { \bf { y } } / 2 , { \bf { I } } ) \operatorname* { d e t } \displaystyle \frac { \partial ^ { 2 } { \cal S } } { \partial { \bf { q } } \partial { \bf { I } } } ( { \bf { q } } - { \bf { y } } / 2 , { \bf { I } } ) | ^ { 1 / 2 } . } } \end{array}
$$

We expect that, in the classical limit, $W _ { \parallel }$ will be small unless ${ \mathfrak { p } } = { \mathfrak { p } } ( { \mathfrak { q } } ) =$ ${ \partial \mathbf { S } } / { \partial \mathbf { q } } .$ ，Given this momentum,the stationary-phase condition for the rapid oscillations of the exponential term is $\mathbf { y } = \mathbf { 0 } .$ ，So,following Berry (1977a), we gain a first (classical) approximation of the Wigner function by expanding the exponent to first order in $\mathbf { y }$ ，while taking $\mathbf { y } = 0$ in the amplitude:

$$
\begin{array} { l } { { \displaystyle W _ { \mathbf { I } } ( \mathbf { p } , { \bf q } ) = c ^ { 2 } ( 2 \pi \hbar ) ^ { - L } \vert \operatorname* { d e t } \partial \mathbf { p } / \partial { \bf I } \vert \int d { \mathbf { y } } \exp \big \{ i \hbar ^ { - 1 } [ { \bf p } ( { \bf q } , { \bf I } ) - { \bf p } ] \cdot { \bf y } \big \} } } \\ { { \displaystyle ~ = c ^ { 2 } \vert \operatorname* { d e t } \partial { \bf p } / \partial { \bf I } \vert \delta [ { \bf p } - { \bf p } ( { \bf q } , { \bf I } ) ] . } } \end{array}
$$

With the change of variable from $\pmb { \mathrm { p } }$ to I, we thus attin the symmetric form

$$
{ \cal W } _ { \mathrm { I } } ( { \bf p } , { \bf q } ) = ( 2 \pi ) ^ { - L } \delta ( { \bf I } ( { \bf p } , { \bf q } ) - { \bf I } ) ,
$$

normalized according to (7.60).

The classical limit of the pure-state Wigner function is a $\delta$ function over the corresponding torus. The amplitude of the $\delta$ function is constant in the conjugate variables $\pmb { \phi }$ ，which do not generally coincide with Euclidean lengths on the torus. Consider, for instance, the one-dimensional tori in figs.3.1a and b.The motion on the tori that nearly touch an unstable equilibrium is very slow in its vicinity. Most of the range of $0 \leq \phi < 2 \pi$ thus lies very close to this point. In consequence, the amplitude of the Wigner function is concentrated in the neighbourhood of the unstable equilibrium. In the case of a separable system with two freedoms,for which figs. 3.1a and b are sections,the equilibrium represents in fact an unstable periodic orbit. The Wigner function is concentrated near the periodic orbit, which is said lo scar it. Projecting the Wigner function,we obtain a scar on the wave intensity near the periodic orbit.This coincides with the caustic in the case of a projection onto the $q$ axis, but in the $p$ representation the scar is far rcmoved from any caustic. The wave function is then unusually concentrated near the unstable periodic orbit,even though its semiclassical quantization condition still depends on the action for the entire torus.

Given a mixed state (7.55), there will be a superposition of the $\delta$ functions for each of the quantized tori. But in the classical limit, the mean spacing between the quantized tori tends to zero. If the probability for the nth state has the limiting classical form

$$
a _ { \mathfrak { n } } = a [ ( \mathfrak { n } + \pmb { \alpha } / 4 ) \hbar ] ,
$$

then the Wigner function

$$
W ( \mathbf { p } , \mathbf { q } ) = \sum _ { \mathbf { \lambda } \mathbf { 0 } } a _ { \mathbf { \lambda } } \delta \biggl ( \mathbf { I } ( \mathbf { p } , q ) - \biggl ( \mathbf { n } + \frac { \alpha } { 4 } \biggr ) \hbar \biggr ) \underset { h \to 0 } { \longrightarrow } a [ \mathbf { I } ( \mathbf { p } , \mathbf { q } ) ] ,
$$

sincc we can approximate the sum by an integral over I.

Without presuming that the pure Wigner is appreciable only when close to the torus,we obtain its semiclassical approximation by means of the Ntationary-phase approximation. The phase in (7.72) willbe stationary for

any $\mathbf { y }$ satisfying

$$
\frac { \partial S } { \partial \mathbf { y } } \bigg ( \mathbf { q } + \frac { \mathbf { y } } { 2 } \bigg ) - \frac { \partial S } { \partial \mathbf { y } } \bigg ( \mathbf { q } - \frac { \mathbf { y } } { 2 } \bigg ) = \mathbf { p } \bigg ( \mathbf { q } - \frac { \mathbf { y } } { 2 } \bigg ) + \mathbf { p } \bigg ( \mathbf { q } - \frac { \mathbf { y } } { 2 } \bigg ) = 2 \mathbf { p } .
$$

These conditions define the end points of Berry chords, that is,the chords of the torus that have $( { \pmb { \mathsf { p } } } , { \pmb { \mathsf { q } } } )$ as their midpoint. Their geometry is discussed by Berry(1977a)and Ozorio de Almeida and Hannay(1982).Figure 7.6 shows a Berry chord for a one-dimensional torus.Given a solution $\mathbf { y _ { 0 } }$ of (7.77), the stationary phase

$$
\hbar ^ { - 1 } \Phi _ { 0 } = \hbar ^ { - 1 } [ S ( { \bf q } + { \bf y } _ { 0 } / 2 , { \bf I } ) - S ( { \bf q } - { \bf y } _ { 0 } / 2 , { \bf I } ) - { \bf p } \cdot { \bf y } _ { 0 } ]
$$

coincides precisely with the simplectic area (in units of $\hbar$ ）bounded by the chord and any path in the torus joining the end points. There is a pair of stationary points $\mathbf { y } _ { j }$ and $- \mathbf { y } _ { j }$ for the jth Berry chord,so the semiclassical

![](images/a06ea53c3d8007bab736adcde9c30d7656f48176c9e53d128628e52c01efe259.jpg)  
Fig.7.6. A Berry chord for a one-dimensional torus. The symplectic area between the chord and the torus determines the phase of the Wigner function.

Wigner function is

$$
W _ { \mathrm { I } } ( \mathbf { p } , \mathbf { q } ) = 2 ( \pi ( 2 \pi \hbar ) ^ { 1 / 2 } ) ^ { - L } \sum _ { j } V _ { j } ^ { - 1 / 2 } \cos \biggl ( \hbar ^ { - 1 } \Phi _ { j } - n _ { j } { \frac { \pi } { 4 } } \biggr ) .
$$

The reader willfind detailed specifications of the phase corrections $n _ { j } \pi / 4$ ， and the amplitudes $V _ { j } ^ { - 1 / 2 }$ in Berry (1977a) and Ozorio de Almeida and Hannay (1982). The important point is that $V _ { j } {  } 0$ as the evaluation point $( { \pmb { \mathsf { p } } } , { \pmb { \mathsf { q } } } )$ tends to the torus.Indeed, the torus belongs to a hypersurface of $2 L$ -1 dimensions,the Wigner caustic, where the semiclassical approximation to the Wigner function diverges. Inside the Wigner caustic the Wigner function oscillates rapidly according to (7.79),while it vanishes outside. These singularities of the semiclassical Wigner function are a shortcoming of the stationary-phase method used in its derivation. At least one Berry chord shrinks as the evaluation point approaches the torus; that is,a pair of stationary points coalesces.Berry (1977a) and Ozorio de Almeida (1983) derive improved uniform approximations (based on diffraction catastrophe integrals)，which remain finite on the Wigner caustic for $\hbar > 0$ The semiclassical equivalence of the Wigner representation with the semiclassical wave function of section 7.2 was obtained by Berry and Wright (1980) on the basis of remarkable projection identities.

The singularity of the semiclassical Wigner function at the Wigner caustic mimics a true peak of its amplitude. The difference between the torus and the rest of the Wigner caustic is that the phase remains constant on the entire torus, whereas it oscillates rapidly along the Wigner caustic as a whole.The classical limit (7.74) must therefore be understood in the same manner as the second example in the previous section -it does not involve the vanishing of the amplitude of the Wigner function, but the cancellation through arbitrarily rapid phase oscillations of the Wigner function, cverywhere except on the torus itself.

We derived the semiclassical Wigner function from the wave function corresponding to a single branch of the torus. However, the symplectic invariance of the Wigner function implies that the result is quite general. If a Berry chord does not fit into a given branch of the torus,we can find a coordinate transformation fitting it in a single branch,as in fig.7.7. The only chords for which this expedient is of no avail have both tips on branch boundaries for some representation: Their midpoints lie on the Wigner caustic. In any case, the symplectic invariance of (7.79) is evident, since $V _ { j }$ and $n _ { j }$ are canonically invariant. The transformation being linear, it takes a Berry chord into a new Berry chord with a corresponding midpoint. The symplectic area $\Phi$ is also preserved,because the transformation is canonical. Conversely, the noninvariance of the Wigner function with respect to general canonical transformations manifests itself clearly in the semiclassical limit: The Wigner function for the transformed torus depends on its new Berry chords and not on the curvilinear images of the old chords.

An interesting case is that of the transformation to the systems'own action-angle variables. In these coordinates a torus in the phase plane becomes a straight line,whereas the image of the Berry chord is now a curve.However, the semiclassical Wigner function in the action-angle variables is a discrete,evenly spaced set of $\delta$ functions in $I$ with the separation $\hbar / 2$ . In the semiclassical limit we can construct the Wigner function in any convenient canonical coordinates,even if there is no exact quantum mechanical unitary transformation corresponding to this change of representation.

It should be noted that the Wigner function represents a single state, so it cannot supply directly matrix elements between different states (i.e., transition probabilities, etc.). These are obtained from the Moyal matrix or crossed Wigner function introduced by Moyal (1949). The semiclassical limit of the Moyal matrix for classically integrable systems in the variables $( \pmb { \mathrm { p } } , \pmb { \mathrm { q } } )$ and $( \mathbf { I } , \pmb { \phi } )$ is discussed in Ozorio de Almeida (1984).

![](images/cb014523ab6c584a2cb261d24a6185e30f5cc5db5447a661513d0822c4a0dc97.jpg)  
Fig. 7.7. If the centre of a Berry chord does not lie on the Wigner caustic, we can find a symplectic transformation such that the chord lies in a single branch of the action function.

# 7.6 The semiclassical propagator

In the beginning of this chapter,we found that the propagation of nonstationary wave functions, corresponding to general Lagrangian surfaces that move under the action of the classical Hamiltonian, are not constrained like stationary states to the invariant tori of integrable systems. The time-dependent semiclassical wave functions are formally impervious to the nonintegrability of the system, though the details of their evolution are certainly sensitive to the classical dynamics,as shown by Berry and Balazs (1979). One of the methods for extracting information about stationary states of nonintegrable systems,to be discussed in chapter 9,is to consider the way the Hamiltonian propagates nonstationary states.

It is particularly convenient to define states related to the evolution operator

$$
{ \hat { U } } ( t ) = \exp ( - i \hbar ^ { - 1 } { \hat { H } } t ) .
$$

Its coordinate representation $\langle \pmb { \mathfrak { q } } | \hat { U } | \pmb { \mathfrak { q } } \rangle$ ,known as the propagator,can be identified as the wave function $\langle \bullet \vert \psi ( t ) \rangle$ that results from the propagation

![](images/8de267db379ebcaa79d33331161e5765f3d938feebe7e4595fc88c3fb72cefab.jpg)  
Fig.7.8. The propagator for $\mathbf { u }$ system with one freedom is associated with the time cvolution of a vertical $q =$ const. linc.

of $\langle \pmb { \mathfrak { q } } | \pmb { \mathfrak { q } } \rangle = \delta ( \pmb { \mathfrak { q } } - \pmb { \mathfrak { q } } )$ in the time $t .$ Classically this initial state corresponds to a uniform $\pmb { \mathrm { p } }$ distribution along the plane ${ \mathfrak { q } } = { \mathfrak { q } } .$ .This plane will evolve into the Lagrangian surface

$$
\pmb { \mathfrak { p } } = \frac { \partial \sigma } { \partial \pmb { \mathfrak { q } } } ( \pmb { \mathfrak { q } } , \pmb { \mathfrak { q } } , t ) ,
$$

where $\pmb { \sigma }$ is a solution of the Hamilton-Jacobi equation (7.1O). The configuration for a system with one freedom is sketched in fig. 7.8.

The semiclassical propagator has the standard form (7.23), except for the presence of caustics. Of course, the initial wave function $\langle \pmb { \mathfrak { q } } | \pmb { \mathfrak { q } } \rangle$ isa single degenerate caustic! So we resort to the Maslov method, since the $\pmb { \mathrm { p } }$ representation

$$
\langle \pmb { \cdot } | \hat { U } ( t ) | \pmb { \cdot } | | \ P \rangle = ( 2 \pi \hbar ) ^ { - 1 / 2 } \left| \operatorname* { d e t } \frac { \hat { \partial } ^ { 2 } \pmb { \sigma } } { \partial \pmb { \mathrm { p } } \hat { \partial } \pmb { \mathrm { q } } } \right| ^ { 1 / 2 } \exp \left\{ i \hbar ^ { - 1 } \pmb { \sigma } ( \pmb { \mathrm { p } } , \pmb { \mathrm { q } } , t ) \right\}
$$

is guaranteed to have no caustics for small enough $t$

# Exercise

Show that for small enough positive time the semiclassical propagator has the form

$$
\left. \pmb { \cdot } \pmb { \mathfrak { q } } | \hat { U } ( t ) | \mathbf { q } \right. = ( 2 \pi i \hbar ) ^ { - 1 / 2 } \left| \operatorname* { d e t } \frac { \hat { \partial } ^ { 2 } \pmb { \sigma } } { \partial \pmb { \mathfrak { q } } \partial \pmb { \mathfrak { q } } } \right| ^ { 1 / 2 } \exp \left\{ i \hbar ^ { - 1 } \pmb { \sigma } ( \pmb { \mathfrak { q } } , \mathbf { q } , t ) \right\}
$$

if $H = { \mathbf { { p } } ^ { 2 } } / { 2 m } + V ( \mathbf { q } ) .$

For $t < 0$ the unitary property of the evolution operator implies that

$$
\langle \mathbf { q } | { \hat { U } } ( - t ) | \mathbf { q } \rangle = \langle \mathbf { q } | { \hat { U } } ( t ) | \mathbf { q } \rangle ^ { * } .
$$

Even for simple motions where ${ \dot { \mathbf { q } } } = \mathbf { p }$ ,the evolving Lagrangian surface may eventually develop caustics.In this instance they are known as focal points or conjugate points to q-they are the loci beyond which the $\pmb q$ orbits emanating from the point $\pmb q$ touch again, as at the cusp in fig. 7.9. The Morse index $\pmb { \mu }$ for a $\pmb q$ orbit is the number of times that it crosses a caustic.Arnold (1967) established the connection between the Morse index and the Maslov index and hence the canonical invariance of the former. We know that the presence of caustics on a Lagrangian surface leads to phase jumps for the wave functions corresponding to each of its branches. Fortunately, the phase for the jth branch can be obtained from the Morse index $\mu _ { j }$ of the corresponding $\pmb q$ orbits.Except for the neighbourhood of caustics, the full semiclassical propagator is

![](images/e8c41682a98e3d96b3c1da221368a904e0e07156b035940d07a4721909967bb9.jpg)  
Fig.7.9.The Morse index of the orbit starting at $q _ { 0 }$ changes from Oto 1 as it enters the region within the cusp.

$$
\langle \mathbf { q } | \hat { U } ( t ) | \mathbf { q } \rangle = ( 2 \pi i \hbar ) ^ { - 1 / 2 } \sum _ { j } \left| \operatorname* { d e t } \frac { \hat { \sigma } ^ { 2 } \sigma _ { j } } { \hat { \sigma } \mathbf { q } \hat { \sigma } \mathbf { q } } \right| ^ { 1 / 2 } \exp \left\{ i \hbar ^ { - 1 } \sigma _ { j } ( \mathbf { q } , \mathbf { q } , t ) - i \mu _ { j } \frac { \pi } { 2 } \right\} .
$$

The derivation of the role of the Morse index in (7.85) is simplest in the Feynman path integral formalism used by Gutzwiller (1967)and by Bery and Mount (1972).

The propagator is the coordinate representation of the unitary evolution operator. The unitary transformation for a fixed $t$ corresponds classically lo the canonical transformation $( { \pmb { \mathrm { p } } } , { \pmb { \mathrm { q } } } )  ( { \pmb { \mathrm { p } } } , { \pmb { \mathrm { q } } } ) ,$ generated implicitly by $\sigma ( \boldsymbol { \mathfrak { q } } , \boldsymbol { \mathfrak { q } } , t )$ according to

$$
{ \bf p } = \frac { \partial \sigma } { \partial { \bf q } } \left( { \bf q } , { \bf q } , t \right) ; \qquad - { \bf p } = \frac { \partial \sigma } { \partial { \bf q } } \left( { \bf q } , { \bf q } , t \right) .
$$

Since the coordinate representation of the evolution operator depends only on the final canonical transformation, we can associate an approximately unitary operator $\hat { U }$ to a canonical transformation generated by any arbitrary function $\sigma ( \mathfrak { q } , \mathfrak { q } ) .$

If the transformation is symplectic, the vertical line ${ \mathfrak { q } } = { \mathfrak { q } }$ will be transformed into another straight line. So there will be no caustics, unless the straight line is vertical. The generating function must have the quadratic form

$$
\sigma ( { \mathfrak { q } } , q ) = ( \alpha / 2 ) { \mathfrak { q } } ^ { 2 } + \beta { \mathfrak { q } } q + ( \gamma / 2 ) q ^ { 2 } ,
$$

so that the amplitude in (7.83) is just $\beta ^ { 1 / 2 }$ . We can verify directly that the semiclassical propagator (7.83) then satisfies

$$
\begin{array} { l } { { \displaystyle { \int } d q ^ { \prime } \langle { \mathfrak { q } } | \hat { U } ^ { - 1 } | q ^ { \prime } \rangle \langle q ^ { \prime } | \hat { U } | { \mathfrak { q } } \rangle = \int d q ^ { \prime } \langle q ^ { \prime } | \hat { U } | { \mathfrak { q } } \rangle ^ { * } \langle q ^ { \prime } | \hat { U } | { \mathfrak { q } } \rangle } } \\ { { \displaystyle \quad = ( 2 \pi \hbar i ) ^ { - 1 } \exp \{ i \hbar ^ { - 1 } \gamma ( q ^ { 2 } - { \mathfrak { q } } ) ^ { 2 } / 2 \} \int d q ^ { \prime } \beta \exp \{ i \hbar ^ { - 1 } \beta ( q - { \mathfrak { q } } ) q ^ { \prime } \} } } \\ { { \displaystyle = \delta ( q - { \mathfrak { q } } ) . } } \end{array}
$$

Thus,the semiclassical form of the coordinate representation of the unitary operator corresponding to a symplectic transformation is exact.

8

# Quantization of ergodic systems

The remarkable self-consistency of the semiclassical theory of integrable systems prevents its natural generalization in the absence of invariant tori. The two ways we may attempt to tackle the problem are by studying the quantization of quasi-integrable systems or,at the other extreme, by plunging straight into ergodic systems.The first option has so far been confined to the quantization of the nearest integrable system that can be found. If the perturbations from integrability are sufficiently weak, this procedure can be justified by the analysis presented in section 9.4.

The present chapter starts with the investigation of the Berry-Voros hypothesis that the classical limit of the Wigner function for an ergodic system is uniform on the energy shell. This leads to some interesting consequences for the smoothed probability density and spatial correlation function.The classical limit of the Wigner function can be refined through multiple iterations of the pure-state condition.In section 8.2 it is shown (hat the torus Wigner function satisfies the pure-state condition,whereas the energy shell Wigner function is brought into a form that depends on individual orbits. A very important feature is that for an ergodic system we can identify the Wigner caustic with the energy shell itself-the scmiclassical Wigner function oscillates inside and decays outside the shell.

The‘Weyl rule’ for the mean density of eigenenergies,derived in scction 8.3, is insensitive to the integrable or chaotic nature of the classical motion. However,the fluctuations of the energy spectrum of some ergodic systems have been computationally verified to have an ‘ergodic property' - (heir correlation functions and averages coincide with those of an ensemble of random matrices.A brief introduction to random matrix theory is given in scction 8.4.

Finally,we return once again to linear maps on the torus. They can be quantized exactly,though at the cost of discretizing the phase space. It Iurns out that they break thc rulc that all classically ergodic systems have in crgodic cncrgy spectrum.

# 8.1 A Wigner function on the energy shell

The Wigner function corresponding to a quantized torus was shown in section 7.5 to condense onto the torus as a $\delta$ function in the classical limit.This result is intuitively satisfying: Almost all orbits of an integrable system wind uniformly around some torus. The classical probability density of finding the system anywhere on the torus is therefore uniform, and there is no possibility of finding it off the torus.

The situation for an ergodic system is analogous: Almost all orbits wind uniformly over the energy shell. The Berry-Voros hypothesis (Berry,1977b; Voros,1979) is that the Wigner function for the stationary state of an ergodic system is then approximately

$$
W _ { c } ( { \bf p } , { \bf q } ) = C \delta \{ E - H ( { \bf p } , { \bf q } ) \} ,
$$

where the normalization constant is

$$
C ^ { - 1 } = \int d { \bf p } d { \bf q } \delta \{ E - H ( { \bf p } , { \bf q } ) \} .
$$

For an integrable system we know that the correct semiclassical approximation (7.79)contains interference terms neglected in the classical approximation (7.74). For an ergodic system it is hard to go beyond (8.2), though a method to achieve this will be put forward in the next section.

Let us consider the projection $| \langle \pmb { \mathsf { q } } | \psi \rangle | _ { m } ^ { 2 }$ of the classical approximation of a Wigner function onto configuration space.In the case of a torus we have

$$
| \langle \mathbf { q } | \psi \rangle | _ { m } ^ { 2 } = \int d \mathbf { p } { \cal W } _ { c } ( \mathbf { p } , \mathbf { q } ) = ( 2 \pi ) ^ { - L } \sum _ { i } \left| \operatorname* { d e t } \frac { \partial \phi } { \partial \mathbf { q } } ( \mathbf { p } _ { i } ( \mathbf { q } ) , \mathbf { q } ) \right| ,
$$

where the $\pmb { \phi }$ are the angle variables on the torus. Comparing this with the square of (7.24), we find that the contribution of each layer of the torus is correct, though (8.3) ignores the interference between layers.These interference terms may be neglected as $\hbar  0$ ,but we also obtain this limit by averaging the semiclassical intensity over a small region $D ^ { L }$ ,large enough to contain many oscillations of the wave function:

$$
| \langle \mathbf { q } | \psi \rangle | _ { m } ^ { 2 } = D ^ { - L } \int _ { D / 2 } ^ { D / 2 } \cdots \int _ { D / 2 } ^ { D / 2 } d \mathbf { y } | \langle \mathbf { q } + \mathbf { y } | \psi \rangle | ^ { 2 } .
$$

By analogy we also interpret the projections of the energy shell Wigner function (8.2) as averages over the unknown semiclassical wave intensity. In the case of the Hamiltonian

$$
H ( \mathbf { p } , \mathbf { q } ) = p ^ { 2 } / 2 m + V ( \mathbf { q } ) ,
$$

the averaged intensity (8.4) will be

$$
\begin{array} { r } { | \langle { \bf q } | \psi \rangle | _ { m } ^ { 2 } = \displaystyle \frac { \int d p p ^ { L - 1 } \delta ( E - p ^ { 2 } / 2 m + V ( { \bf q } ) ) } { \int d { \bf q } d p p ^ { L - 1 } \delta ( E - p ^ { 2 } / 2 m + V ( { \bf q } ) ) } } \\ { = \displaystyle \frac { ( E - V ( { \bf q } ) ) ^ { L / 2 - 1 } \Theta ( E - V ( { \bf q } ) ) } { \int d { \bf q } ( E - V ( { \bf q } ) ) ^ { L / 2 - 1 } \Theta ( E - V ( { \bf q } ) ) } , } \end{array}
$$

where $\Theta ( x )$ is the unit step function. The classical probability density is nonzero only if $V ( \mathbf { q } ) < E$

Let us consider the boundary of this region. For $L = 1$ the averaged intensity is singular at the boundary point. This is just what we expectafter all, the system is integrable, so we are dealing with a caustic. For $L = 2$ the density is constant, so the classically allowed region terminates with a finite step of the intensity. For $L > 2$ the probability density goes smoothly to zero.This behaviour for $L \ge 2$ contrasts strongly with that of integrable systems. These boundaries are therefore named anticaustics by Berry (1977b).We have seen that the caustics of integrable systems do not correspond to true singularities of the wave intensity. However, as $\hbar  0$ we do obtain sharp ridges near the caustic. The Berry-Voros hypothesis predicts the absence of this important feature in the intensity of the states of ergodic systems.

The Wigner function contains more information than its projection. In particular we obtain the correlation function $C ( \mathbf { y } ; \mathbf { q } )$ by averaging the variable $\mathbf { q }$ in the density matrix $\langle \mathbf { q } + \mathbf { y } / 2 | \psi \rangle \langle \psi | \mathbf { q } - \mathbf { y } / 2 \rangle$ over a small region $D ^ { L }$ ，while keeping $\mathbf { y }$ fixed:

$$
\begin{array} { c } { { \displaystyle C ( { \bf y } ; { \bf q } ) = \frac { \{  { \bf q } + { \bf y } / 2 | \psi   \psi | { \bf q } - { \bf y } / 2  \} _ { m } } { |  { \bf q } | \psi  | _ { m } ^ { 2 } } } } \\ { { = \displaystyle |  q | \psi  | _ { m } ^ { - 2 } \int d { \bf p } W _ { c } ( { \bf p } , { \bf q } ) \exp ( i \hbar ^ { - 1 } { \bf p } \cdot { \bf y } ) . } } \end{array}
$$

For the one-dimensional wave function (7.63), the density matrix is

$$
\langle q + y / 2 | \psi \rangle \langle \psi | q - y / 2 \rangle = d ^ { - 1 } \bigl \{ \cos ( \hbar ^ { - 1 } p _ { 0 } y ) + \cos ( \hbar ^ { - 1 } 2 p _ { 0 } q ) \bigr \} .
$$

Averaging over $q$ in a region large enough for the second term to have many oscillations,we obtain

$$
C ( y ) = \cos ( \hbar ^ { - 1 } p _ { 0 } y ) ,
$$

which coincides with the result of inserting the classical Wigner function

$$
W _ { c } ( p , q ) = ( 2 d ) ^ { - 1 } [ \delta ( p - p _ { 0 } ) + \delta ( p + p _ { 0 } ) ]
$$

in (8.7).

For states corresponding to tori

$$
C ( \mathbf { y } ; \mathbf { q } ) = \left\{ \sum _ { j } \left| \operatorname* { d e t } \frac { \partial \phi } { \partial \mathbf { q } } \right| \right\} ^ { - 1 } \sum _ { i } \left| \operatorname* { d e t } \frac { \partial \phi } { \partial \mathbf { q } } \right| \exp \left\{ i \hbar ^ { - 1 } \mathbf { p } _ { j } ( \mathbf { q } ) \cdot \mathbf { y } \right\} ,
$$

a weighted average of plane de Broglie waves, with wave vectors ${ \bf p } _ { j } ( { \bf q } ) / \hbar$ The torus has a finite number of layers, so $C ( \mathbf { y } , \mathbf { q } )$ is necessarily anisotropic in y. The resulting interference fringes are illustrated in fig. 8.1 in the simple case of a two-dimensional torus with only two layers over the point ${ \pmb q } .$ .For an ergodic system there is a continuum of p's for each $\mathbf { q }$ In the case of the simple Hamiltonian (8.5) we obtain

$$
C ( \mathbf { y } ; \mathbf { q } ) = \left\{ \int d \Omega \right\} ^ { - 1 } \int d \Omega \exp { \left\{ i \hbar ^ { - 1 } \left[ 2 m ( E - V ( \mathbf { q } ) ) \right] ^ { 1 / 2 } \mathbf { y } \cdot \pmb { \Omega } \right\} } ,
$$

where $\pmb { \Omega }$ is the unit vector in the $\pmb { \mathrm { p } }$ direction and $d \pmb { \Omega }$ is the differential of the $L$ dimensional angle in $\pmb { \mathrm { p } }$ 、According to Berry (1977b) this can be integrated as

$$
C ( \mathbf { y } ; \mathbf { q } ) = \Gamma { \bigg ( } { \frac { N } { 2 } } { \bigg ) } { \frac { J _ { N / 2 - 1 } \left\{ \hbar ^ { - 1 } \lbrack 2 m ( E - V ( \mathbf { q } ) ) ] ^ { 1 / 2 } | \mathbf { y } | \right\} } { \left\{ \hbar ^ { - 1 } [ 2 m ( E - V ( \mathbf { q } ) ) ] ^ { 1 / 2 } | \mathbf { y } | \right\} } } ,
$$

where $\Gamma$ is the Euler gamma function and $J _ { y }$ is a Bessel function (both defined in Abramowitz and Stegun, 1964). Thus, the Berry-Voros approximation to the correlation function of an ergodic system is isotropic in y. This prediction is confirmed by the calculations of McDonald and Kaufman (1979) for the stadium. They also discovered that the eigenfunctions exhibit a random pattern for the nodal curves.

![](images/82ef009d03ea215f67f304a55196a1e9600b74bacdac4187f6faed0a45850548.jpg)  
Fig.8.1. The correlation function shows the interference fringes of a finite number of plane de Broglie waves.

# 8.2 The pure-state condition

The condition that the density operator $\hat { \rho }$ , given by (7.55),defines a pure state is simply that

$$
{ \hat { \rho } } ^ { 2 } = { \hat { \rho } } .
$$

Taking the Weyl transform of both sides, we obtain the following identity between Wigner functions,

$$
\int _ { - \infty } ^ { \infty } d { \bf x } _ { 1 } d { \bf x } _ { 2 } W ( { \bf x } _ { 1 } ) W ( { \bf x } _ { 2 } ) \cos ( \hbar ^ { - 1 } \Delta ) = \left( \frac { \pi \hbar } { 2 } \right) ^ { L } W ( { \bf x } ) ,
$$

![](images/4c5a609fc07bc1a49060778b2dbd9de65ebb4e36e16c4315a31715dbfc5ec521.jpg)  
Fig.8.2. The triangle△fits with two Berry chords to produce a third Berry chord m a stationary configuration.

where $\mathbf { x } = ( \pmb { \mathrm { p } } , \pmb { \mathrm { q } } )$ and $\Delta$ is twice the symplectic area of the parallelogram with sides ${ \bf x } _ { 1 } - { \bf x }$ and $\mathbf { x } _ { 2 } - \mathbf { x } ,$ ,that is,

$$
\boldsymbol { \Delta } ( \mathbf { x } , \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } ) = 2 \sum _ { l = 1 } ^ { L } \operatorname* { d e t } \left[ \begin{array} { l l } { p _ { 1 l } - p _ { l } } & { p _ { 2 l } - p _ { l } } \\ { q _ { 1 l } - q _ { l } } & { q _ { 2 l } - q _ { l } } \end{array} \right] .
$$

An alternative geometric interpretation of $\Delta$ is that of the symplectic area of the triangle that has $\mathbf { x } , \mathbf { x } _ { 1 }$ and $\mathbf { x } _ { 2 }$ as the midpoints of its sides.As we see in fig. 8.2, this fits in beautifully with the semiclassical Wigner function,defined in terms of Berry chords.Indeed, for the case drawn, the phases of $W ( \mathbf { x } _ { 1 } )$ and $W (  { \mathbf { x } } _ { 2 } )$ together with $\Delta$ equal the phase of the Wigner function $W ( \mathbf { x } )$ .Ozorio de Almeida (1983) showed that this is the configuration for the stationary-phase condition with respect to $\mathbf { x } _ { 1 }$ and $\mathbf { x } _ { 2 }$ in the integral (8.15). Thus, the semiclassical Wigner function satisfies the pure-state condition within the stationary-phase approximation.

The fact that condition (8.15) also holds for the amplitudes and phase corrections of the Wigner function (and that the results can be generalized to tori of any dimension) is just another example of the self-consistency of the semiclassical theory of integrable systems.The important question is whether we can use the pure-state condition to refine a crude approximation of the Wigner function.

Let us thus insert the classical approximation of the torus Wigner function into the integral in (8.15); there results a new approximation

![](images/051e102d51775d550147daf1f07c1806315102d47ed837e3a470c9a9a7a989e7.jpg)  
Fig. 8.3. Inserting classical Wigner functions in the pure-state condition, we obtain an approximation whose phase is that of a triangle tangent to the torus.

$$
W _ { 1 } ( { \bf x } ) = ( 2 \pi ^ { 3 } \hbar ) ^ { - L } \int _ { - \infty } ^ { \infty } d { \bf x } _ { 1 } d { \bf x } _ { 2 } \delta ( { \bf I } ( { \bf x } _ { 1 } ) - { \bf I } ) \delta ( { \bf I } ( { \bf x } _ { 2 } ) - { \bf I } ) \cos \big \{ \hbar ^ { - 1 } \Delta ( { \bf x } , { \bf x } _ { 1 } , { \bf x } _ { 2 } ) \big \} .
$$

For $L = 1$ ,it is easy to verify that the phase is stationary in the integral over the angle variables $\pmb { \phi } _ { 1 }$ and $\pmb { \phi } _ { 2 }$ when the triangle $\Delta$ is tangent to the torus at both points $\mathbf { x } _ { 1 }$ and $\mathbf { x } _ { 2 }$ . For example, if we fix the vector ${ \bf x } _ { 2 } - { \bf x }$ in fig.8.3, the area of the parallelogram defined by this vector together with $\mathbf { x } _ { 1 } - \mathbf { x }$ is stationary with respect to small displacements of $\mathbf { x } _ { 1 }$ along the torus.This result can also be generalized for $L > 1$ : The phase $\hbar ^ { - 1 } \Delta$ is stationary when two sides of the triangle belong to tangent planes of the torus at $\mathbf { x } _ { 1 }$ and $\mathbf { x } _ { 2 }$ . This can be seen by taking the tangent plane at $\mathbf { x } _ { 1 }$ to be the $\pmb { \mathrm { p } } = 0$ coordinate plane (permitted by the Lagrangian property of the torus). The condition that the side of $\Delta$ at $\mathbf { x } _ { 1 }$ is in the $\pmb { \mathrm { p } } = 0$ plane forces the projections of $( \mathbf { x } _ { 2 } - \mathbf { x } ) _ { l }$ onto the $L$ conjugate planes $( p _ { l } , q _ { l } )$ to be parallel to the $q _ { l }$ axis (fig. 8.4). None of the areas $A _ { l }$ will be altered by displacements of $\mathbf { x } _ { 1 }$ along the $\pmb { \mathrm { p } } = 0$ plane. So the phase is stationary with respect to $\mathbf { x } _ { 1 }$ if it lies on a tangent plane,the same condition holding for $\mathbf { x } _ { 2 }$ . Note that the $\scriptstyle L$ -dimensional tangent planes at $\mathbf { x } _ { 1 }$ and $\mathbf { x } _ { 2 }$ intersect at a single point in the $2 L$ -dimensional phase space.This is a vertex of $\Delta$ ， the phase of $W _ { 1 } ( \mathbf { x } ) ;$ ：that is,we obtain a clumsy imitation of the Berry chord construction. Thus,after a single iteration of the pure-state condition, we already have an approximation to the Wigner function that oscillates inside the torus, a part of the Wigner caustic.

![](images/8e279cb01299d9a0b40dcd928ef43d3778c66f20ef6f0482af0b99b267ae3a58.jpg)  
Fig.8.4. The stationary-phase condition is that (x2- x) be paralel to the tangent plane to the torus at $\bigstar _ { 1 }$ This can be taken as the $\pmb { \mathrm { p } } = \pmb { 0 }$ plane.

Successive iterations of the pure-state conditions bring further_refinements to the Wigner function. It is easily seen that the stationary-phase condition for $W _ { 2 } ( \mathbf { x } ) .$ ，obtained by inserting $W _ { 1 } (  { \mathbf { x } } _ { 1 } )$ and $W _ { 1 } (  { \mathbf { x } } _ { 2 } )$ in (8.15), is that the pentagon drawn in fig.8.5 has four sides tangent to the torus at their midpoints. Further iterations bring improved polygonal approximations to the Berry chord phase,which emerges in the limit of infinite iterations!

Let us now apply our method for refining approximations of the Wigner function to the Berry-Voros hypothesis.The first iteration of the pure-state condition is

$$
W _ { 1 } ( \mathbf { x } ) = \frac { c ^ { 2 } } { ( \pi \hbar / 2 ) ^ { L } } \int d \mathbf { x } _ { 1 } d \mathbf { x } _ { 2 } \delta ( H ( \mathbf { x } _ { 1 } ) - E ) \delta ( H ( \mathbf { x } _ { 2 } ) - E ) \cos ( \hbar ^ { - 1 } \Delta ) .
$$

We seek the condition for the area $\Delta$ to be stationary with respect to the $( 2 L - 1 )$ free variables in $\mathbf { x } _ { 1 }$ and $\mathbf { x } _ { 2 }$ . Again we choose the $( 2 L - 1 )$ dimensional plane tangent to the energy shell at $\mathbf { x } _ { 1 }$ as a coordinate plane with $p _ { 1 } = 0$ .If the projection of the vector ${ \bf x } _ { 2 } - { \bf x }$ onto the plane $\left( p _ { 1 } , q _ { 1 } \right)$ is parallel to the $q _ { 1 }$ axis as in fig.8.4, then the area $A _ { 1 }$ will be stationary with respect to displacements of $\mathbf { x } _ { 1 }$ .However,having the side of $\Delta$ at $\mathbf { x } _ { 1 }$ contained in the $p _ { 1 } = 0$ plane imposes no other restriction on $\mathbf { x } _ { 2 } - \mathbf { x } ,$ so the other areas $A _ { j }$ need not be stationary. The only way of guaranteeing that the full symplectic area $\Delta$ is stationary is for $\mathbf { x } _ { 2 } - \mathbf { x }$ to be parallel to the $q _ { 1 }$ axis itself. In a Euclidean space the situation would be hopeless, because this direction would not be uniquely defined on the tangent plane. In a symplectic space the $q _ { 1 }$ axis does have a unique direction, namely $\dot { \mathbf { x } } = \mathcal { J } \partial H / \partial \mathbf { x } .$ ，where $\mathcal { J }$ is given by (1.37). Thus, the phase of the Wigner function $W _ { 1 }$ is that of the triangle $\Delta _ { ; }$ ，where $\mathbf { x } _ { 1 }$ and $\mathbf { x } _ { 2 }$ are tangent to classical orbits of the ergodic system.

![](images/65a1dee91d49e50117248777218bc9fde8f9cb7d3c8074fc018b50ab4a546396.jpg)  
Fig. 8.5. The second iteration of the pure-state condition leads to an approximate Wigner function whose phase depends on the area of a tangent pentagon.

At the $W _ { 1 }$ level there is no restriction identifying the orbits at $\mathbf { x } _ { 1 }$ and $\mathbf { x } _ { 2 }$ .However, on approaching the limit of infinite iterations there arises a polygonal line with infinitesimal sides, each one being tangent to an orbit. In the limit $W _ { \infty }$ we obtain a Berry chord on the shell with both edges touching the same orbit. The corresponding phase is the symplectic area (in units of $\hbar$ ) bounded by the orbit and the chord.Note that,in this case, we canot choose any path between the chord tips, since the energy shell is a not a Lagrangian surface.

Far from the energy shell the semiclassical Wigner function will be very complicated. Near the shell we can approximate its $( 2 L - 2 )$ -parameter family of orbits by plane curves.Each point within and near the shell lies on a two-dimensional plane containing a single orbit. In each plane we obtain a semiclassical Wigner function whose structure is identical to the one for a single freedom (simultaneously integrable and ergodic!). The cnergy shell is the Wigner caustic-a fold. Beyond it the Wigner function decays,whereas inside there are multiple-phase oscillations of a complex nature yet to be analysed. The ergodic Wigner function has some relation to that for an integrable system with $L \ge 2$ 、However, the Wigner caustic of the latter is a mere geometric construction based on the invariant torus, whereas in the former case the Wigner caustic is the energy shell itself.

It is hard to calculate the amplitudes and phase corrections of the semiclassical Wigner function directly from the iterations of the pure-state condition. The important and surprising point is that,from the refinements of the energy shell Wigner function， there emerges a semiclassical dependence on individual orbits,for all the complexity of their structure. In chapter 9 we shall use a formalism based on the propagator,which tukes the orbits into account from the start,and thus derive some important results in an easier way than iterating the pure-state condition.

# 8.3 The mean level density

The energy spectrum of integrable systems was derived in section 7.3 from a detailed consideration of the semiclassical wave functions.It is now important to try to obtain information about the spectrum, without relying on the (unknown) characteristics of the eigenstates of unintegrable systems. We shall deal with the density of states

$$
d ( E ) = \sum _ { j = 1 } ^ { \infty } \delta ( E - E _ { j } ) = { \mathrm { T r } } \delta ( E - { \hat { H } } )
$$

and its integral

$$
N ( E ) = \sum _ { j = 1 } ^ { \infty } \Theta ( E - E _ { j } ) = \operatorname { T r } \Theta ( E - \widehat { H } ) ,
$$

the cumulative density or mode number.

Turning once again to the formalism of Weyl and Wigner, we note that inverting the Fourier transform (7.57) and integrating over ${ \mathfrak { q } } .$ ，we obtain

$$
\mathrm { T r } \hat { A } = ( 2 \pi \hbar ) ^ { - L } \int d { \bf p } d { \bf q } A _ { w } ( { \bf p } , { \bf q } ) .
$$

We found in section 7.4 that in some simple cases the Weyl transform of an operator coincides with its classical limit. According to the correspondence principle this equivalence holds in the semiclassical limit (also verified directly using semiclassical Wigner functions by Ozorio de Almeida,1984). So following Berry (1983), we substitute (8.21) for the right side of(8.20) with $[ \Theta ( E - \hat { H } ) ] _ { w } \simeq \Theta ( E - H ( { \bf p } , { \bf q } ) )$ , which results in the Weyl rule:

$$
\bar { N } ( E ) = ( 2 \pi \hbar ) ^ { - L } \int d { \bf p } d { \bf q } \Theta ( E - H ( { \bf p } , { \bf q } ) ) .
$$

The surprising feature of this formula is its complete generality. No distinction is made as to the dynamical nature of the system,whether integrable,ergodic or otherwise. The approximate number of states with energy smaller than $E$ is determined by the volume within the corresponding energy shell, measured in units of $( 2 \pi \hbar ) ^ { L }$

This continuous density can only be an approximation of the steps in the mode number (8.20). That it represents an averaged density becomes clear from the consideration of integrable systems.For these the mode number,derived in section 7.3,is precisely

$$
\begin{array} { r } { N ( E ) = \underset { \mathbf { \eta } \mathbf { \eta } } { \sum } \Theta ( E - H ( \mathbf { I } _ { \mathbf { \eta } } ) ) , } \end{array}
$$

where the $\mathbf { I _ { \overline { { n } } } }$ are the actions of the quantized invariant tori. These form a regular lattice in the action variables, so as a first approximation we can take

$$
\bar { N } ( E ) = \hbar ^ { - L } \int d \mathbf { I } \Theta ( E - H ( \mathbf { I } ) ) .
$$

Since the Hamiltonian is independent of the angle variables,this integral can be rewritten as

$$
\bar { N } ( E ) = \hbar ^ { - L } \int d \mathbf { I } \frac { d \pmb { \theta } } { ( 2 \pi ) ^ { L } } \Theta ( E - H ( \mathbf { I } ) ) .
$$

The canonical transformation $( \mathbf { I } , \pmb { \theta } )  ( \mathbf { p } , \pmb { \ q } )$ preserves volume; therefore, the mean level density (8.25) can be identified with the Weyl rule.

The verification of the Weyl rule for nonintegrable systems is possible only through ‘computational experiments’with simple systems.The most popular systems are quantum billiards, that is, the quantization of the two-dimensional classical billiards presented in section 3.5.Within the boundaries,the Schrodinger equation reduces to the Helmholtz equation, so the problem is simply to ascertain the vibrational spectra of drums with different shapes. The boundary conditions on the square in Sinai's billiard shown in fig. 3.12 are periodic. Berry (1981b) calculated the energy spectrum of Sinai's billiard for five values of the parameter $\pmb R$ ，the ratio of the radius of the circle to the side of the square. The results appear in fig. 8.6.It should be noted that the system is integrable for $R = 0$ ,whereas in all other cases it is ergodic with positive entropy.

For a particle with unit massin a billiard,the Weyl rule takes the simple form

$$
\begin{array} { r } { \vec { N } ( E ) \simeq A E / ( 2 \pi \hbar ^ { 2 } ) , } \end{array}
$$

where $A$ is the available area of the billiard. Unfortunately, the discontinuity of the potential, which helps the computation of eigenvalues, hinders the agreement of the Weyl rule with the averaged mode number. Even so,Baltes and Hilf(1978) provide corrections to the Weyl rule, which also take into account the perimeter $\gamma$ of the billiard, its curvature,its connectivity and the contribution of the vertices:

$$
\overline { { N } } ( E ) = \frac { A E } { ( 2 \pi \hbar ) ^ { 2 } } - \frac { \gamma E ^ { 1 / 2 } } { 2 ^ { 3 / 2 } \pi \hbar } + K ,
$$

the latter contributions all being included in $\pmb { K }$ ,a constant in energy.This is the equation of the dashed curves in fig. 8.6, which correctly interpolate the steps in the cumulative density of states. The Weyl rule (8.26) is presented as an unbroken straight line in each graph.

![](images/c374414980de68f8175de32a0ca86e619cf1cb3131e1b97575a6273ec74710a5.jpg)  
Fig.8.6. The mode number for Sinai's biliard, calculated for five values of the parameter R.(Courtesy of M.V. Berry.)

Even though it is necessary to add corrections to the Weyl rule in the case of billiards, the important fact is that we have a simple theory that predicts the correct mean level density. It is insensitive to the nature of the classical motion (also in the case of billiards), so that it is only more subtle properties of the spectrum- the fluctuations of the density about its mean - that may distinguish the dynamical nature of the corresponding classical motion.In the following section we shall briefly study the theory of random matrices and examine the evidence that they furnish correct predictions of the statistics of fluctuations for the spectra of classical chaotic systems. Chapter 9 provides the dynamical explanation of some of these results,based on the quantization of periodic orbits.

# 8.4 Random matrices

In the semiclassical limit the mean level density $\bar { d } ( E )$ increases with $\hbar ^ { - L }$ For small $\hbar$ all the physically significant properties of the spectrum may depend only on $\overline { { d } } ( E )$ and on some averages over the fluctuations

$$
\widetilde { d } ( E ) = d ( E ) - \overline { { d } } ( E )
$$

of the spectrum. These averages can then be defined locally for an energy range $\delta E \propto \hbar ^ { - 1 }$ ,containing $\delta { \cal N } \propto \hbar ^ { - ( L - 1 ) }$ .In other words,the semiclassical limit permits us to subject the spectrum to a statistical treatment even in an energy range that is classically small.

This section presents techniques for calculating statistical properties of spectra from those ensembles of random matrices that share only the same symmetry properties.An ergodic spectrum is defined by the property that its individual averages coincide with averages over the ensemble.Thus,a Hamiltonian matrix $\mathcal { H }$ with an ergodic spectrum can be substituted by a random matrix whose $K \times K$ elements are random variables.The method is familiar from its use in statistical mechanics,though the statistical natures of both theories differ.As Balian (1968) notes:

In statistical mechanics, some information is missing because the system is too complicated to be observed; the purpose is to make predictions in spite of this luck of knowledge. In the theory of random matrices,it happens that the Hamiltonian matrix $\pmb { \mathcal { H } }$ of the system is exactly known, but it is too complicated lo be diagonalized practically. One deliberately discards some available informalion,assuming that the detailed form of $\pmb { \mathcal { H } }$ is irrelevant for the studied property, in order to satisfy a simplified (but statistical) mathematical treatment.

The presentation in this chapter is based on the review of Bohigas and Giannoni (1984) and on Balian (1968). The introductory review in Porter (1965)is an important background reference.That book contains the main papers on the subject up to 1965.

The main problem is that of determining the class of matrices to be admitted in the ensemble for a particular Hamiltonian and to define an appropriate measure for the ensemble. We know that Hamiltonians can always be represented by Hermitian matrices. If there exists an exact constant of the motion (such as angular momentum), the matrix can be separated into blocks.In this case the ensemble averages will refer to a single block.Underlying space-time symmetries impose restrictions on the ensemble.In the absence of spin,the matrix can be chosen to be real and symmetric, provided that the Hamiltonian is invariant with respect to time inversion. Otherwise (e.g.,in the presence of a magnetic field), we must allow complex Hermitian matrices in the ensemble.

The measure $d { \mathcal { H } }$ in the space of matrices can be introduced in a natural way by the postulation of the metric,

$$
d s ^ { 2 } = \operatorname { T r } \delta { \mathcal { H } } \delta { \mathcal { H } } ^ { \dagger }
$$

where $\mathcal { H } ^ { \dagger }$ is the Hermitian conjugate of $\mathcal { H }$ .Hence,the ‘distance’between two neighbouring matrices $\mathcal { H }$ and $\mathcal { H } + \delta \mathcal { H }$ can be written as the function of its elements,

$$
d s ^ { 2 } = \sum _ { 1 \leq k \leq K } ( \delta H _ { k k } ) ^ { 2 } + 2 \sum _ { 1 \leq j \leq k \leq K } ( \delta H _ { j k } ) ^ { 2 } ,
$$

in the case of real symmetric matrices,whereas for complex Hermitian matrices $\mathcal { H } = \mathcal { H } ^ { \prime } + i \mathcal { H } ^ { \prime \prime }$ ,we have

$$
d s ^ { 2 } = \sum _ { 1 \leq k \leq K } ( \delta H _ { k k } ^ { \prime } ) ^ { 2 } + 2 \sum _ { 1 \leq j \leq k \leq K } [ ( \delta H _ { j k } ^ { \prime } ) ^ { 2 } + ( \delta H _ { j k } ^ { \prime \prime } ) ^ { 2 } ] .
$$

The introduction of a metric among $N$ variables $\mathbf { x }$ , in the form

$$
d s ^ { 2 } = \sum _ { \mu , v } ^ { N } g _ { \mu v } \delta x _ { \mu } \delta x _ { v }
$$

implies the definition of the basic measure

$$
d V { = } ( \operatorname * { d e t } g _ { \mu v } ) ^ { 1 / 2 } \prod _ { \mu = 1 } ^ { N } d x _ { \mu } .
$$

Therefore,the natural measure for the ensemble ofreal symmetric matrices is

$$
d \mathcal { H } = 2 ^ { K ( K - 1 ) / 4 } \prod _ { 1 \leq k \leq K } d H _ { k k } \prod _ { 1 \leq j \leq k \leq K } d H _ { j k } ,
$$

and the measure in the space of complex Hermitian matrices has the form

$$
d \mathcal { H } = 2 ^ { K ( K - 1 ) / 2 } \prod _ { 1 \leq k \leq K } d H _ { k k } ^ { \prime } \prod _ { 1 \leq j \leq k \leq K } d H _ { j k } ^ { \prime } d H _ { j k } ^ { \prime \prime } .
$$

Any transformation for which the metric is invariant also preserves the measure $d { \mathcal { H } }$ 、The probability differential $P ( { \mathcal { H } } ) d { \mathcal { H } }$ is also preserved; therefore,probability densities $P ( { \mathcal { H } } )$ are invariant with respect to real orthogonal transformations if $\mathcal { H }$ is real and symmetric, whereas for complex Hermitian matrices $P ( { \mathcal { H } } )$ will be invariant with respect to general unitary transformations. As a token of these invariance properties, we obtain the invariance of the entropy,

$$
h \{ P ( \mathcal { H } ) \} \equiv - \int d \mathcal { H } P ( \mathcal { H } ) \log P ( \mathcal { H } ) ,
$$

generalizing the definition (3.27) of entropy for a discrete probability distribution. The second and final postulate in the theory of random matrices is that $P ( { \mathcal { H } } )$ must be chosen so as to maximize the entropy. This is exactly the procedure in statistical mechanics -we presume the same probability for all accessible states; that is,in the absence of information, we choose the distribution with the maximum entropy.

Let us assume the knowledge of some average properties of the matrix $\mathcal { H }$ ：

$$
\langle f _ { i } \rangle \equiv \int d \mathcal { H } P ( \mathcal { H } ) f _ { i } ( \mathcal { H } ) = C _ { i } .
$$

The distribution with maximum entropy with respect to any variation $\delta P ( { \mathcal { H } } ) .$ ， subject to the constraints (8.37), satisfies the equation

$$
\int d \mathcal { H } \delta P ( \mathcal { H } ) \left\{ \log P ( \mathcal { H } ) - \sum _ { i } \lambda _ { i } f _ { i } ( \mathcal { H } ) \right\} = 0 ,
$$

since the integral over $\delta P ( { \mathcal { H } } )$ vanishes. Thus, the probability density is simply

$$
P ( \mathcal { H } ) = \exp { \biggl [ \sum _ { i } \lambda _ { i } f _ { i } ( \mathcal { H } ) \biggr ] } ,
$$

und we determine the Lagrange multipliers $\lambda _ { i }$ by inserting (8.39) back into (8.37).

One way to guarantee that the eigenvalues ofa finite matrix are bounded is to specify the norm

$$
\langle \operatorname { T r } \mathcal { H } \mathcal { H } ^ { \dagger } \rangle = \langle E _ { 1 } ^ { 2 } + E _ { 2 } ^ { 2 } + \cdots \rangle = C _ { 2 } .
$$

(ombining this with the‘normalization constraint' $( \langle 1 \rangle = 1 )$ , we obtain

the probability density

$$
P ( \mathcal { H } ) { = } \exp ( \lambda _ { 0 } + \lambda _ { 1 } \operatorname { T r } \mathcal { H } \mathcal { H } ^ { \dagger } )
$$

the Gaussian orthogonal ensemble (GOE) or the Gaussian unitary ensemble (GUE), depending on the symmetry properties of the matrix $\mathcal { H }$

In the semiclassical limit we have to deal with an infinite matrix, with a mean level density that is known a priori, instead of a finite matrix with a finite norm.Thus, in this case we have a continuum of constraints

$$
\langle d ( E ) \rangle = \langle \operatorname { T r } \delta ( E \mathbf { 1 } - \mathcal { H } ) \rangle = \sum _ { j } \delta ( E - E _ { j } ) = \overline { { d } } ( E ) ,
$$

parametrized by the energy $E$ .The resulting probability density for the Weyl-Balian ensemble is

$$
\begin{array} { r } { P ( \mathcal { H } ) = \exp \Bigg \{ \int d E \lambda ( E ) \operatorname { T r } \delta ( E \mathbf { 1 } - \mathcal { H } ) \Bigg \} = \exp \{ \operatorname { T r } \lambda ( \mathcal { H } ) \} , } \end{array}
$$

or

$$
P ( { \mathcal { H } } ) = \operatorname* { d e t } \mu ( { \mathcal { H } } ) ,
$$

where

$$
\mu ( E ) \equiv \exp \left\{ \lambda ( E ) \right\} .
$$

The probability densities (8.41) and (8.43) depend only on the eigenvalues of $\mathcal { H }$ .However,we need to know the measure $d \mathcal { H }$ in terms of the eigenvectors and eigenvalues of $\mathcal { H }$ before we can derive the combined probability density for the eigenvalues on their own.Let $\mathbf { E }$ be the eigenvalues of $\mathcal { H }$ and $\pmb { \alpha }$ the parameters that specify the directions of its eigenvectors.The measure is then shown by Porter (1965) to have the form

$$
d \mathcal { H } = \prod _ { i < j } | E _ { i } - E _ { j } | ^ { \beta } d \mathbf { E } d \pmb { \alpha } ,
$$

where $\beta = 1$ for real matrices and $\beta = 2$ if they are complex. Integrating over all the directions of the eigenvectors,we thus obtain the combined eigenvalue probability densities as

$$
P ( \mathbf { E } ) = C \prod _ { i < j } | E _ { i } - E _ { j } | ^ { \beta } \exp \big \{ - ( 4 \sigma ^ { 2 } ) ^ { - 1 } \sum _ { k } E _ { k } ^ { 2 } \big \}
$$

for the Gaussian ensembles and

$$
P ( \mathbf { E } ) = \prod _ { i < j } | E _ { i } - E _ { j } | ^ { \beta } \exp \left\{ \sum _ { k } \lambda ( E _ { k } ) \right\}
$$

for the Weyl-Balian ensemble.

In principle we can determine the function $\lambda ( E )$ by integrating (8.48)

over $K - 1$ variables and equating the result to $\overline { { d } } ( E )$ .A simpler alternative is to use the approximate method of Wigner (1957): For $P ( \mathbf { E } )$ we substitute $P [ f ( E ) ]$ ，where $f ( E ) d E$ is the number of eigenvalues in the interval $d E$ The allowed distributions $f ( E )$ should be a set of $K$ Dirac $\delta$ functions, but in the limit where $K \to \infty$ we can approximate $f ( E )$ by a smooth function. The assumption is that $f = \overline { { d } }$ is the distribution that maximizes

$$
\log P [ f ] \simeq \int d E f ( E ) \lambda ( E ) + ( \beta / 2 ) \int d E d E ^ { \prime } f ( E ) f ( E ^ { \prime } ) \log | E - E ^ { \prime } | .
$$

[This neglects correlations in the second term of (8.47), which, it is hoped, are of short range.] Differentiating with respect to $f _ { \mathrm { { ; } } }$ we obtain explicitly

$$
\lambda ( E ) \simeq - ( \beta / 2 ) \int d E ^ { \prime } \overline { { d } } ( E ^ { \prime } ) \log | E - E ^ { \prime } | .
$$

# Exercise

Verify that this expression for $\lambda$ makes $P ( \mathbf { E } )$ invariant with respect to changes in the energy scale.

In the case of the Gaussian ensembles, we have no a priori knowledge of $\langle d ( E ) \rangle$ . Wigner's method can now be applied to (8.47), resulting in the integral equation

$$
- ( 4 \sigma ^ { 2 } ) ^ { - 1 } E ^ { 2 } + \beta \int d E ^ { \prime } \langle d ( E ^ { \prime } ) \rangle \log | E - E ^ { \prime } | = \mathrm { c o n s t } ,
$$

with the solution

$$
\langle d ( E ) \rangle = \left\{ \begin{array} { l l } { ( 2 \pi \sigma ^ { 2 } ) ^ { - 1 } ( 4 N \sigma ^ { 2 } - E ^ { 2 } ) ^ { 1 / 2 } , \quad } & { | E | \leq 2 N ^ { 1 / 2 } \sigma } \\ { 0 , \quad } & { | E | \geq 2 N ^ { 1 / 2 } \sigma . } \end{array} \right.
$$

This expression for the mean level density coincides with the exact result for the Gaussian ensembles,obtained by direct integration. This fact reinforces our confidence as to the value of the approximation (8.50) for the Weyl-Balian density.

The semicircular form of the density of states for the Gaussian ensembles usually bears no relation to the true Weyl density. Even so,both distributions show level repulsion - $P ( { \bf E } ) \to 0$ as two levels approach each other. The similarity between the Weyl-Balian and the Gaussian distributions permits us to fit the latter to the former in a small energy range $d E \propto \hbar$ ， which is sufficient to obtain statistical properties of an individual semiclassical spectrum. The Gaussan distributions have two free parameters - the width $\pmb { \sigma }$ and the mean $\overbar { E }$ ,taken as zero in (8.47). Thus,choosing

$$
\begin{array} { r } { \bar { E } = E - 2 \lambda / \lambda ^ { \prime } ( E ) , \qquad \sigma ^ { 2 } = - \lambda / ( \lambda ^ { \prime } ) ^ { 2 } , } \end{array}
$$

where $\lambda ^ { \prime } = d \lambda / d E$ we fit

$$
\lambda ( E ) = - ( 4 \sigma ^ { 2 } ) ^ { - 1 } ( E - \overline { { E } } ) ^ { 2 }
$$

up to the first order in the Taylor expansion about any point inside $\delta E$ The only condition is that $\lambda ( E ) < 0$ ，which implies that $\bar { d } ( E )$ should not have any very narrow peak.But this event can always be avoided with a change in energy scale, since the Weyl-Balian distribution with $\lambda ( E )$ given by (8.50) is scale invariant.

The great advantage of fitting the Gaussian distributions to the correct distributions for an ergodic semiclassical spectrum is that many important statistical properties of the former are known exactly. This is the case of the two-level correlation function

$$
Y _ { 2 } ( E _ { 1 } , E _ { 2 } ) \equiv - \frac { P ( E _ { 1 } , E _ { 2 } ) - P ( E _ { 1 } ) P ( E _ { 2 } ) } { P ( E _ { 1 } ) P ( E _ { 2 } ) }
$$

and of higher correlation functions (see Bohigas and Giannoni, 1984, for references). In the case of the Gaussian orthogonal ensemble, $\beta = 1$ ，we obtain the limits

$$
\begin{array} { r l } & { Y _ { 2 } ( r ) \underset { r  0 } { \longrightarrow } 1 - \frac { 1 } { 6 } \pi ^ { 2 } r + \frac { 1 } { 6 0 } \pi ^ { 4 } r ^ { 3 } + \cdots , } \\ & { Y _ { 2 } ( r ) \underset { r  \infty } { \longrightarrow } ( \pi r ) ^ { - 2 } - ( 1 + ( \cos \pi r ) ^ { 2 } ) ( \pi r ) ^ { - 4 } + \cdots , } \\ & { \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad r = | \dot { E _ { 2 } } - E _ { 1 } | \bar { d } } \end{array}
$$

where

in a region in which $\bar { d } ( E ) = K P ( : E )$ can be considered constant. The distribution for the nearest-neighbour spacings has the form

$$
P ( r ) = ( \dot { \beta \pi } ^ { 2 } / 6 ) r ^ { \beta } + \cdots .
$$

We are now in a position to ascertain whether classically ergodic systems have spectra that are also ergodic. The computational evidence that this is indeed the case has become substantial. For example,Bohigas,Giannoni and Schmit (1984) obtained the histogram for $P ( r )$ in fig. 8.7 from the analysis of 74O levels of Sinai's billiard.Similar calculations for the stadium as well as other statistics of the spectrum are also well fitted by the GOE. At the start of this section we restricted this analysis to systems without any special symmetries; therefore, fig. 8.7 deals with the spectrum for only one-eighth of Sinai's billiard (the desymmetrized billiard).

![](images/48350ff54236b0a5f50068f6aef14cf8bd61433fea01fc7c4024bf085423cbdb.jpg)  
Fig.8.7. Histogram of the nearest-neighbour spacings in the spectrum of Sinai's billiard.Dashed curve, Poisson distribution； solid curve, GOE; stepped curve, Sinai's billiard. (Courtesy of O.Bohigas,M.J.Giannoni and C. Schmit.)

![](images/1b5d8513bbf1cd193a96ada531933eeed7de177f0541cc68079b65636728f1db.jpg)  
Fig.8.8. Nearest-neighbour spacing for the quarter-circle billiard.Dashed curve, Poisson distribution; solid curve, GOE; stepped curve,quarter of a circle.(Courtesy of O.Bohigas,M.J. Giannoni and C. Schmit.)

As a comparison, fig. 8.8 presents the nearest-neighbour spacing of an integrable billiard -the quarter of a circle.There is no correlation between the way that different regions of the energy shell $H ( \mathbf { I } ) = E$ sweep through the‘dense' lattice of quantized tori in fig. 7.4. The fluctuations of the spectrum can thus be approximately modelled by the Poisson distribution.' There is no level repulsion in this case.

# 8.5 Quantization of the cat map

Consideration of the discrete Poincaré map is always helpful in the study of continuous classical systems.However, there is no obvious way to quantize maps directly.The best available option is to consider the classical map as the stroboscopic map of a time-periodic Hamiltonian system and then deal with the period operator $\hat { U } _ { \tau }$ ,that is, the evolution operator for the period $\boldsymbol { \tau }$ of the Hamiltonian. This operator is unitary rather than Hermitian, but we can also investigate its eigenvalues and eigenfunctions. In particular we can verify whether its spectrum is ergodic,which in this instance means having the same fluctuation statistics as the circular ensemble of Dyson (1962) with properties similar to those of the Gaussian ensembles.The quantum map that has been most intensively studied is the ‘standard map':

$$
\begin{array} { l } { { p ^ { \prime } = q - K \sin q , } } \\ { { q ^ { \prime } = q + p ^ { \prime } , } } \end{array}
$$

obtained from the periodic Hamiltonian,

$$
H ( p , q , t ) = \frac { p ^ { 2 } } { 2 } + \frac { K } { 2 \pi } \cos q \sum _ { n } \delta ( t - 2 n \pi ) ,
$$

known as the kicked rotor,by Casati, Chirikov,Ford and Izrailev (1979).

Unfortunately the rigorous mathematical basis for quantum timeperiodic systems is less developed than that for time-independent Hamiltonians. Indeed, one of the ways of obtaining such results, known as Howland's method (Howland,198o), consists precisely of the elimination of time by expanding the phase space by two extra dimensions - just the reverse procedure of taking the Poincaré section!

An especially simple map to quantize is Arnold's cat map, presented in section 1.4 and used thereafter as a paradigm of classically chaotic motion. It has several unusual characteristics,but it is worthwhile to review briefly the results of Hannay and Berry (198O).In the case of the rotor (8.61), the variable $q$ is an angle with period $2 \pi$ (the phase space is a cylinder),so the conjugate variable- the angular momentum-is discretized.In the cat map, with $( p , q ) = ( \theta _ { 2 } , \theta _ { 1 } )$ in section 1.4, the momentum is also periodic (the phase space is a torus); therefore, the coordinates $q$ are also discrete. The $\pmb { p }$ and $q$ wave functions for this system are necessarily ‘combs'of equally spaced $\delta$ functions modulated by a (complex) periodic amplitude. The coordinate representation is

$$
\langle q | \psi \rangle = \sum _ { k = - \infty } ^ { \infty } \sum _ { n = 1 } ^ { N } a _ { n } \delta \Bigg ( q - \bigg ( \frac { n } { N } + k \bigg ) 2 \pi \Bigg ) ,
$$

with the Fourier transform

$$
\left. p | \psi \right. = \left( 2 \pi \hbar \right) ^ { - 1 / 2 } \sum _ { k = - \infty } ^ { \infty } \sum _ { n = 1 } ^ { N } a _ { n } \exp \left\{ i \hbar ^ { - 1 } 2 \pi { \left( \frac { n } { N } + k \right) } p \right\} .
$$

The periodicity of the momentum must then be

$$
\Delta p = N \hbar ,
$$

so that the area of the torus is quantized as

$$
\Delta p \Delta q = 2 \pi \hbar N .
$$

In other words,the choice $\Delta q = \Delta p = 2 \pi$ determines

$$
\hbar = 2 \pi / N ,
$$

where $N$ is the number of 'teeth' in one period of the wave function ‘comb. The semiclassical limit $\hbar  0$ here corresponds to $N \to \infty$ .Use of the Poisson identity,

$$
\sum _ { j = - \infty } ^ { \infty } \delta ( t - j ) = \sum _ { k = - \infty } ^ { \infty } \exp ( i 2 \pi k t ) ,
$$

leads to

$$
\left. p | \psi \right. = \sum _ { j = - \infty } ^ { \infty } \left\{ \sum _ { n = 1 } ^ { N } N ^ { - 1 / 2 } a _ { n } \exp ( i n p ) \right\} \delta \Biggl ( p - \frac { 2 \pi j } { N } \Biggr ) ,
$$

that is, a $\delta$ comb with $N$ teeth in each period.

So far we have studied only the kinematics of the cat map.Its dynamics ire based on the propagator corresponding to a linear canonical transformation, studied in section 7.6. The generating function

$$
S ( q , \mathfrak { q } ) = ( \alpha \mathfrak { q } ^ { 2 } + 2 \beta \mathfrak { q } q + \gamma q ^ { 2 } ) / 2
$$

defines the exact quantum propagator

$$
\langle \mathfrak { q } | \hat { U } | \mathfrak { q } \rangle = ( - i \beta / 2 \pi \hbar ) ^ { 1 / 2 } \exp \left\{ i \hbar ^ { - 1 } S ( \mathfrak { q } , \mathfrak { q } ) \right\} .
$$

The classical map has the form

$$
{ \Bigg [ } { \mathfrak { p } } { \Bigg ] } = { \Bigg [ } { a \atop b } { \begin{array} { l } { d } \\ { e } \end{array} } { \Bigg ] } { \Bigg [ } { \begin{array} { l } { p } \\ { q } \\ { - { \frac { 1 } { \beta } } } \end{array} } { \frac { \beta ^ { 2 } - \alpha \gamma } { \beta } } { \Bigg ] } { \Bigg [ } { \begin{array} { l } { p } \\ { q } \end{array} } { \Bigg ] } .
$$

Therefore, the propagator can be written as

$$
\left. \mathfrak { q } \right. \hat { U } | q \rangle = \frac { 1 } { 2 \pi } \bigg ( \frac { i N } { b } \bigg ) ^ { 1 / 2 } \exp { \bigg \{ \frac { i N } { 4 \pi b } ( a \mathfrak { q } ^ { 2 } - 2 \mathfrak { q } q + c q ^ { 2 } ) \bigg \} } ,
$$

where the constants $N , a , b , c$ are all integers.

In order to build up the torus propagator we now have to combine all the contributions of equivalent points $q + 2 \pi m$ to the amplitude at $\mathfrak { q }$ (fig.8.9). The contributions of all equivalent points to the propagator at $\mathfrak { q }$ will be out of phase and therefore cancel if $\mathfrak { q }$ is not on the $\delta$ comb. Conversely points on the $\delta$ comb may receive all contributions in phase. The analysis becomes very simple in the special case where $b = 1$ . Then

$$
\begin{array} { l } { { \displaystyle \zeta { \mathfrak { q } } | \hat { U } | q \rangle _ { \mathrm { t o r u s } } = \displaystyle \frac { 1 } { 2 \pi } ( i N ) ^ { 1 / 2 } \sum _ { m } \exp \left\{ \frac { i N } { 4 \pi } [ a { \mathfrak { q } } ^ { 2 } - 2 { \mathfrak { q } } ( q + 2 \pi m ) + c ( q + 2 \pi m ) ^ { 2 } ] \right\} } } \\ { { \displaystyle \qquad = \frac { 1 } { 2 \pi } ( i N ) ^ { 1 / 2 } \exp \left\{ \frac { i N } { 4 \pi } ( a { \mathfrak { q } } ^ { 2 } - 2 { \mathfrak { q } } q + c q ^ { 2 } ) \right\} } } \\ { { \displaystyle \qquad \times \sum _ { m } \exp \left\{ i \pi [ N c m ^ { 2 } + 2 ( c Q - \mathfrak { Q } ) m ] \right\} } , \qquad { \scriptstyle ( 8 \cdot 7 \qquad Z ) \geq 0 } } \end{array}
$$

![](images/2f1b2187092fe54ecd91ad3a481088d02da7a666509c6bd256bb4341c7dc03cf.jpg)  
Fig.8.9. Periodicity of the torus demands that the contribution of equivalent points $q + 2 \pi m$ be included in the propagator.