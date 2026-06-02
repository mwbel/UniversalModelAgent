Turn from initial- and final-value data to the action integral that is determined by(l) these data and (2) the principle that the action be an extremum,

$$
I = I _ { \mathrm { e x t r e m u m } } = S .
$$

The action depends on the variables on the final hypersurface,according to the formula

Problem in assuring completeness and consistency of initial data

$$
S = S ( \varSigma , B )
$$

in electrodynamics, but according to the formula

$$
S = S ( ^ { ( 3 ) } \mathcal { Y } )
$$

in geometrodynamics. In each case, there are three numbers per spacepoint in the argument of the functional (one in $\pmb { \Sigma }$ ; two in a divergence-free magnetic field; three in $( 3 ) \textcircled { 8 }$

This mixing of the one many-fingered time and the two dynamic variables in a 3-geometry makes it harder in general relativity than in Maxwell theory to know when one has in hand appropriate initial value data. Give $\pmb { \Sigma }$ and give $\mathcal { B }$ and $\dot { \mathcal { B } }$ on $\pmb { \Sigma }$ : that was enough for electrodynamics. For geometrodynamics, to give the six $g _ { i j } ( x , y , z )$ and the six $\dot { g } _ { i j } ( x , y , z )$ is not necessarily enough. For example, let the time parameter $t$ be a fake, so that $d t$ , instead of leading forward from a given hypersurface $\pmb { \Sigma }$ to a new hypersurface $\pm \mathbf { \nabla } d \Sigma$ , merely recoordinatizes the present hypersurface:

$$
\begin{array} { c } { { x ^ { i } \longrightarrow x ^ { i } - \xi ^ { i } d t , \qquad \longrightarrow } } \\ { { g _ { i j } \longrightarrow g _ { i j } + ( \xi _ { i \mid j } + \xi _ { j \mid i } ) d t . } } \end{array}
$$

A first inspection may make one think that one has adequate data in the six $g _ { i j }$ and the six

$$
\dot { g } _ { i j } = \xi _ { i \vert j } + \xi _ { j \vert i } ,
$$

but in the end one sees that one has not both faces of the thin sandwich,as required, but only one. Thus one must reject, as improperly posed data in the generic problem of dynamics,any set of six $\dot { g } _ { i j }$ that let themselves be expressed in the form (21.131) [Belasco and Ohanian (1969)].

The “thin sandwich conjecture"

Similar diffculties occur when the two faces of the thin sandwich, instead of coinciding everywhere, coincide in a limited region,be it three-dimensional, twodimensional, or even one-dimensional ("crossover of one face from being earlier than the other to being later"). Thus it is enough to have (21.131) obtaining even on only a curved line in $\boldsymbol { \Sigma }$ to reject the six $g _ { i j }$ as inappropriate initial-value data.

That one can impose conditions on the $g _ { i j }$ and $\dot { g } _ { i j }$ which will guarantee existence and uniqueness of the solution $N ( x , y , z )$ ， $N _ { \mathfrak { i } } ( x , y , z )$ of the initial-value equations (21.126)and (21.127) is known as the“thin-sandwich conjecture,”a topic on which there has been much work by many investigators,but so far no decisive theorem.

To presuppose existence and uniqueness is to make the first step in giving mathematical content to Mach's principle that the distribution of massenergy throughout space determines inertia (821.12).

# \$21.10. THE TIME-SYMMETRIC AND TIME-ANTISYMMETRIC INITIAL-VALUE PROBLEMS

Turn from the general initial-value problem to two special initial-value problems that lend themselves to detailed treatment, one known as the time-symmetric initial-value problem,the other as the time-antisymmetric problem.

A 4-geometry is said to be time-symmetric when there exists a spacelike hypersurface $\pmb { \Sigma }$ at all points of which the extrinsic curvature vanishes.In this case the three initial value equations (21.127) are automatically satisfied,and the fourth reduces to a simple requirement on the three-dimensional scalar curvature invariant,

$$
R = 1 6 \pi \rho .
$$

Still further simplifications result when one limits attention to empty space. Simplest of all is the case of spherical symmetry in which (21.132) yields at once the full Schwarzschild geometry at the moment of time symmetry (two asymptotically flat spaces connected by a throat),as developed in exercise 21.20.

Consider a 3-geometry with metric

$$
d s _ { 1 } ^ { 2 } = g _ { ( 1 ) i k } d x ^ { i } d x ^ { k } .
$$

Call it a“base metric.” Consider another 3-geometry with metric

$$
d s _ { 2 } ^ { 2 } = \psi ^ { 4 } ( x ^ { i } ) d s _ { 1 } ^ { 2 } .
$$

Angles are identical in the two geometries. On this account they are said to be conformally equivalent. The scalar curvature invariants of the two 3-geometries are related by the formula [Eisenhart (1926)]

$$
{ \cal R } _ { 2 } = - 8 { \psi } ^ { - 5 } { \bf { \nabla } } { \bf { \overline { { { \psi } } } } } _ { 1 } ^ { 2 } \psi + { \psi } ^ { - 4 } { \cal R } _ { 1 } ,
$$

where

$$
\pmb { \nabla } _ { 1 } ^ { 2 } \psi = \psi _ { \mid i } ^ { \mid i } = g _ { 1 } ^ { \enspace - 1 / 2 } ( \partial / \partial x ^ { i } ) [ g _ { 1 } ^ { \enspace 1 / 2 } g ^ { i k } ( \partial \psi / \partial x ^ { k } ) ]
$$

Demand that the scalar curvature invariant $R _ { 2 }$ vanish,and arrive [Brill (1959)] at the “wave equation”

$$
\pmb { \nabla } _ { 1 } 2 \psi - ( R _ { 1 } / 8 ) \psi = 0
$$

for the conformal correction factor $\psi$ . Brill takes the base metric to have the form suggested by Bondi,

$$
d s _ { 1 } ^ { ~ 2 } = e ^ { 2 4 q _ { 1 } ( \rho , z ) } ( d z ^ { 2 } + d \rho ^ { 2 } ) + \rho ^ { 2 } d \phi ^ { 2 } ,
$$

and takes the conformal correction factor $\psi$ also to possess axial symmetry. In the application:

$q _ { 1 } ( \pmb { \rho } , z )$ measures the“distribution of gravitational wave amplitude,”assumed for simplicity.to vanish outside $r = ( \rho ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 } = a .$   
$\pmb { A }$ measures the “amplitude of the distribution of gravitational wave amplitude";   
$\psi ( \rho , z )$ is the conformal correction factor, which varies with position at large distances as $1 + ( m / 2 r )$ . The quantity $m ( \mathrm { c m } )$ is uniquely determined by the condition that the geometry be asymtotically flat. It measures the mass-energy of the distribution of gravitational radiation.

Wave amplitude determines mass-energy: $m = m ( A )$

The mass m of the gravitational radiation is proportional to $A ^ { 2 }$ for small values of the amplitude A. It is inversely proportional to the reduced wavelength $\lambda =$ (effective wavelength/ $^ { \prime } 2 \pi $ )that measures the scale of rapid variations in the gravitational wave amplitude $q _ { 1 } ( \pmb { \rho } , z )$ in the“active zone.”Thus the metric is dominated by wiggles, proportional in amplitude to $\pmb { A }$ ,in the active zone,and at larger distances dominated by something close to a Schwarzschild $( 1 + 2 m / r )$ factor in the metric.When the amplitude $\pmb { A }$ is increased,a critical value is attained, $A = A _ { \mathrm { c r i t } } ,$ at which $m$ goes to infinity and the geometry curves up into closure("universe closed by its own content of gravitational-wave energy"). Further analysis and examples will be found in Wheeler (1964a), pp.399-451, also in Wheeler (1964c).

Brill has carried out a similar analysis [Brill (l961)] for the vacuum case of what he calls time-antisymmetric initial-value conditions,sketched below as amended by York(1973).(l） The initial slice is maximal,T $\mathbf { \nabla } \cdot \kappa = 0 _ { : - } ( 2 )$ This slice is conformally flat,

$$
g _ { i j } = \psi ^ { 4 } \delta _ { i j } .
$$

(3) Work in the“base space" with metric $\delta _ { i j }$ and afterwards transform to the geometry (21.139). Three of the initial-value equations become

$$
K _ { \mathrm { b a s e , } j } ^ { i j } = 0 .
$$

To solve these equations, (l） take any localized trace-free symmetric tensor $B _ { k m }$ ； (2） solve the flat-space Laplace equation $\nabla ^ { 2 } A = ( 3 / 2 ) \partial ^ { 2 } B _ { k m } / \partial x ^ { k } \partial x ^ { m }$ for $\pmb { A }$ ； (3） define the six potentials $A _ { k m } = B _ { k m } + \frac { 1 } { 3 } A \ \delta _ { k m }$ and (4） calculate

$$
K _ { \mathrm { b a s e } } ^ { i j } = [ i k \ell ] [ j m n ] \partial ^ { 2 } A _ { k m } / \partial x ^ { \ell } \partial x ^ { n } ,
$$

that automaticallysatisfy (21.140)and give $\mathrm { T r } \kappa _ { \mathrm { b a s e } } = 0$ . Then $K ^ { i j } = \psi ^ { - 1 0 } K _ { \mathrm { b a s e } } ^ { i j } a l s o$ automatically satisfies these conditions,but now in the curved geometry (21.139). The final initial-value equation becomes a quasilinear elliptic equation, in the flat base space, for the conformal factor $\psi ,$

$$
8 \nabla _ { \mathrm { b a s e } } ^ { 2 } \psi + \psi ^ { - 7 } \sum _ { i , j } ( K _ { \mathrm { b a s e } i j } ) ^ { 2 } = 0 .
$$

The asymptotic form of $\psi$ reveals that the mass of the wave is positive.

In addition to the time-symmetric and time-antisymmetric cases, there are at least two further cases where the initial-value problem possess special simplicity. One is the case of a geometry endowed with a symmetry,as,for example,for the Friedmann universe of Chapter 27 or the mixmaster universe of Chapter 30 or cylindrical gravitational waves in the treatment of Kuchar (l97la). One starts with a spacelike slice on which the $g _ { i j }$ and $\pi ^ { i j }$ have a special symmetry, and makes allfuture spacelike slices in a way that preserves this symmetry. The geometry on any one of these simultaneities, though almost entirely governed by these symmetry considerations, still typically demands some countable number of parameters for its complete determination, such as the radius of the Friedmann universe, or the three principal radii of curvature of the mixmaster universe. These parameters and the momenta conjugate to them define a miniphase space. In this miniphase space, the dynamics runs its course as for any other problem of classcal dynamics [see,for example,Box 30.1 and Misner (1969) for the mixmaster universe; Kuchar (197la) and (l972) for waves endowed with cylindrical symmetry;and Gowdy (1973) for waves with spherical symmetry]. Even the evidence for the existence of many-fingered time, most characteristic feature of general relativity,is suppressed as the price for never having to give attention to any spacelike slice that departs from the prescribed symmetry.

Exercise 21.16. POOR MAN'S WAY TO DO COSMOLOGY Consider a spacetime with the metric

EXERCISES

$$
d s ^ { 2 } = \ - d t ^ { 2 } + \ a ^ { 2 } ( t ) [ d \chi ^ { 2 } + \sin ^ { 2 } \chi ( d \theta ^ { 2 } + \sin ^ { 2 } \theta \ d \phi ^ { 2 } ) ] ,
$$

corresponding to a 3-geometry- with the form of a sphere of radius $a ( t )$ changing with time. Show that the tensor of extrinsic curvature as expressed in a local Euclidean frame of reference is

$$
\pmb { K } = - \pmb { a } ^ { - 1 } ( d \pmb { a } / d t ) \pmb { \eta } ,
$$

where $\pmb { \eta }$ is the unit tensor. Show that the initial value equation (21.77) reduces to

$$
( 6 / a ^ { 2 } ) ( d a / d t ) ^ { 2 } + ( 6 / a ^ { 2 } ) = 1 6 \pi \rho ( a )
$$

[for the value of the second term on the left, see exercise l4.3 and Boxes l4.2 and 14.5], and explain why it is appropriate to write the term on the right as $6 a _ { 0 } / a ^ { 3 }$ for a“dust-filled model universe.” More generally,given any equation of state, $p = p ( \boldsymbol { \rho } )$ , explain how one can find $\rho = \rho ( a )$ from

$$
d ( \rho a ^ { 3 } ) = - p d ( a ^ { 3 } ) ;
$$

and how one can thus forecast the history of expansion and recontraction, $a = a ( t )$

# Exercise 21.17. THIN-SANDWICH VARIATIONAL PRINCIPLE FOR THE SCALAR POTENTIAL IN ELECTRODYNAMICS

(a) Choose the unknown $U ^ { m }$ in the expression

$$
\frac { 1 } { 8 \pi } g ^ { m n } \frac { \hat { c } \phi } { \hat { c } . { \bf x } ^ { m } } \frac { \hat { c } \phi } { \hat { c } . { \bf x } ^ { n } } + U ^ { m } \frac { \hat { c } \phi } { \hat { c } x ^ { n } }
$$

in such a way that this expression, multiplied by the volume element $g ^ { 1 / 2 } d ^ { 3 } x$ ,and integrated over the simultaneity $\pmb { \Sigma }$ , is extremized by a $\phi .$ ,and only by a $\phi$ 、that satisfies the initial-value equation (21.108) of electrodynamics.

(b) Show that the resulting variational principle,instead of having to be invented “out of the blue,”is none other than what follows directly from the action principle build on the Lagrangian density (21.l00) of electrodynamics (independent variation of $\phi$ and the three $A _ { i }$ everywhere between the two faces of a sandwich to extremize $\boldsymbol { I }$ ,subject only to the prior specification of the $A _ { i }$ on the two faces of the sandwich,in the limit where the thickness of the sandwich goes to zero).

# ExerciSe 21.18. THIN-SANDWICH VARIATIONAL PRINCIPLE FOR THE LAPSE AND SHIFT FUNCTIONS IN GEOMETRODYNAMICS

(a)Extremize the action integral

$$
\begin{array} { l } { { I _ { 3 } = \displaystyle \int \left\{ [ R - ( \mathrm { T r } K ) ^ { 2 } + \mathrm { T r } K ^ { 2 } - 2 T _ { n n } ^ { * } ] N \right. } } \\ { { \left. - 2 T _ { n } ^ { * k } N _ { k } \right\} g ^ { 1 / 2 } d ^ { 3 } x } } \end{array}
$$

with respect to the lapse and shift functions,and show that one arrives in this way at the four initial-value equations of geometrodynamics. It is understood that one has given the six $g _ { i j }$ and the six $\partial g _ { i j } / \partial t$ on the simultaneity where the analysis is being done. The extrinsic curvature is considered to be expressed as in (21.67) in terms of these quantities and the lapse and shift. The energy density and energy fow are referred to a unit normal vector $\pmb { n }$ and three arbitrary coordinate basis vectors ${ \pmb e } _ { i }$ within the simultaneity,as earlier in this chapter,and the asterisk is an abbreviation for an omitted factor of ${ \tt 8 \pi }$

(b) Derive this variational principle from the ADM variational principle by going to the limit of an infinitesimally thin sandwich [see derivation in Wheeler (1964)].

# Exercise 21.19. CONDENSED THIN-SANDWICH VARIATIONAL PRINCIPLE

(a）Extremize the action $I _ { 3 }$ of the preceding exercise with respect to the lapse function $N .$ (b) What is the relation between the result and the principle that $^ { 6 6 } 3$ -geometry is a carrier of information about time"? (c) By elimination of $N _ { \ast }$ ,arrive at a“condensed thin-sandwich variational principle”in which the only quantities to be varied are the three shift functions $N _ { i }$

# Exercise 21.20. POOR MAN'S WAY TO SCHWARZSCHILD GEOMETRY

On curved empty space evolving deterministically in time, impose the conditions (l） that it possess a moment of time-symmetry, a spacelike hypersurface, the extrinsic curvature of which,withespectenelopingspaceti,isvererezerond2)thattisscelike hypersurface be endowed with spherical symmetry. Write the metric of the 3-geometry in the form

$$
d s ^ { 2 } = \psi ^ { 4 } ( \overline { { { r } } } ) ( d \overline { { { r } } } ^ { 2 } + \overline { { { r } } } ^ { 2 } d \theta ^ { 2 } + \overline { { { r } } } ^ { 2 } \sin ^ { 2 } \theta d \phi ^ { 2 } ) .
$$

From the initial-value equation (21.127),show that the conformal factor $\psi$ up to a multiplicative factor must have the form $\psi = ( 1 + m / 2 \overline { { r } } )$ .Show that the proper circumference $2 \pi \overline { n } \ell ^ { 2 } ( \overline { r } )$ assumes a minimum value at a certain value of $\widetilde { \pmb { r } } ,$ thus defining the throat of the 3-geometry. Show that the 3-geometry is mirror-symmetric with respect to reflection in this throat in the sense that the metric is unchanged in form under the substitution $r ^ { \prime } = m ^ { 2 } / 4 \overline { { r } } .$ Find the transformation from the conformal coordinate $\widetilde { \pmb { r } }$ to the Schwarzschild coordinate $\boldsymbol { r } .$

# \$21.11. YORK'S "HANDLES" TO SPECIFY A 4-GEOMETRY

On a simultaneity-or on the simultaneity-of extremal proper volume, give the conformal part of the 3-geometry and give the two inequivalent components of the dynamically conjugate momentum in order (l） to have freely specifiable, but also complete,initial-value data and thus (2) to determine completely the whole generic four-dimensional spacetime manifold.This in brief is York's extension (1971,1972b) to the generic case of what Brill did for special cases (see the preceding section). York and Brill acknowledge earlier considerations of Lichnerowicz (1944)and Bruhat (1962 and earlier papers cited there on conformal geometry and the initial-value problem). But why conformal geometry,and why pick such a special spacelike hypersurface on which to give the four dynamic data per spacepoint?

Few solutions of Maxwell's equations are simpler than an infinite plane monochromatic wave in Minkowski's fat spacetime,and few look more complex when examined on a spacelike slice cut through that spacetime in an arbitrary way,with local wiggles and waves,larger-scale lumps and bumps,and still larger-scale general curvatures. No one who wants to explore electrodynamics in its evolution with many-fingered time can avoid these complexities；and no one will accept these complexities of many-fingered time who wants to see the degrees of freedom of the electromagnetic field in and by themselves exhibited in their neatest form.He will pick the simplest kind of timelike slice he can find. On that simultaneity, there are two and only two field coordinates, and two and only two feld momenta per spacepoint. Similarly in geometrodynamics.

When one wants to untangle the degrees of freedom of the geometry, as distinct from analyzing the dynamics of the geometry, one therefore retreats from the three items of information per-spacepoint that are contained in a 3-geometry [or in any other way of analyzing the geometrodynamics,as especially seen in the “extrinsic time” formulation of Kuchar (1971b and 1972)] and following York (l） picks the simultaneity to have maximal proper volume and (2) on this simultaneity specifies the two “coordinate degrees of freedom per spacepoint’ that are contained in the conformal part of the 3-geometry.

The degrees of freedom of the geometry in brief

An element of proper volume $g ^ { 1 / 2 } d ^ { 3 } x$ on the spacelike hypersurface $\pmb { \Sigma }$ undergoes, in the next unit interval of proper time as measured normal to the hypersurface, a fractional increase of proper volume [see Figure 21.3 and equations 21.59 and 21.66] given by

# Pick hypersurface of extremal proper volume

$$
- \mathrm { T r } { \pmb { K } } = - \frac 1 2 g ^ { - 1 / 2 } \mathrm { T r } { \pmb { \pi } } .
$$

For the volume to be extremal this quantity must vanish at every point of $\pmb { \Sigma }$ This condition is satisfed in a Friedmann universe (Chapter 27) and in a Taub universe (Chapter 3O) at that value of the natural time-coordinate $t$ at which the universe switches over from expansion to recontraction. It is remarkable that the same condition on the choice of simultaneity, $\pmb { \Sigma }$ ,lets itself be formulated in the same natural way,

$$
\mathrm { T r } { \cal K } = 0 ~ \mathrm { o r ~ T r } \pi = 0 ,
$$

for a closed universe altogether deprived of any symmetry whatsoever. Alternatively, one can deal with a spacetime that is topologically the product of an open 3-space by the real line (time). Then it is natural to think of specifying the location in it of a bounding spacelike 2-geometry $s$ with the topology of a 2-sphere. Then one has many ways to fil in the interior of $s$ with a spacelike 3-geometry $\pmb { \Sigma }$ ; but of all these $\pmb { \Sigma }$ 's,only the one that is extremal,or only the ones that are extremal,satisfy (21.144).

Who is going to specify this 2-geometry with the topology of a 2-sphere? The choice of that 2-geometry is not a matter of indifference. In a given 4-geometry, distinct choices for the bounding 2-geometry willordinarily give distinct results for the extremizing 3-geometry,and therefore different choices for the “initial-value simultaneity,” $\pmb { \Sigma }$ . No consideration immediately thrusts itself forward that would give preference to one choice of 2-geometry over another. However, no such infinity of options presents itself when one limits attention to a closed 3-geometry. Therefore it will give concreteness to the following analysis to consider it applied to a closed universe, even though the analysis surely lets itself be made well-defined in an open region by appropriate specification of boundary values on the closed 2-geometry that bounds that open region. In brief, by limiting attention to a closed 3-geometry, one lets the obvious condition of closure take the place of boundary conditions that are not obvious.

York's analysis remains simple when his extrinsic time

$$
\tau = \frac { 2 } { 3 } g ^ { - 1 / 2 } \operatorname { T r } \pmb { \eta } = \frac { 4 } { 3 } \operatorname { T r } \pmb { K }
$$

has any constant value on the hypersurface, not only the value $\tau = 0$ appropriate for the hypersurface of extremal proper volume.

On the simultaneity $\pmb { \Sigma }$ specified by the condition of constant extrinsic time, $\tau =$ constant, begin by giving the conformal 3-geometry,

$$
< = ^ { ( 3 ) } < = \left( \begin{array} { l } { { \mathrm { t h e ~ e q u i v a l e n c e ~ c l a s s ~ o f ~ a l l ~ t h o s e ~ p o s i t i v e ~ d e f i n i t e } } } \\ { { \mathrm { R i e m a n n i a n ~ t h r e e - d i m e n s i o n a l ~ m e t r i c s ~ t h a t ~ a r e } } } \\ { { \mathrm { e q u i v a l e n t ~ t o ~ e a c h ~ o t h e r ~ u n d e r ~ ( 1 ) ~ d i f f e o m o r p h i s m } } } \\ { { \mathrm { ( s m o o t h ~ s l i d i n g ~ o f ~ t h e ~ p o i n t s ~ o v e r ~ t h e ~ m a i n i f o l d ~ t o ) } } } \\ { { \mathrm { n e w ~ l o c a t i o n s ~ o r ~ ( 2 ) ~ c h a n g e s ~ o f ~ s c a l e ~ t h a t ~ v a r y } } } \\ { { \mathrm { s m o o t h y ~ f r o m ~ p o i n t ~ t o ~ p o i n t , ~ l e a s i n g ~ f i x e d ~ a l l } } } \\ { { \mathrm { l o c a l ~ a n g l e s ~ ( r a t i o s ~ o f ~ l o c a l ~ d i s t a n c e s ) , ~ b u t } } } \\ { { \mathrm { c h a n g i n g ~ l o c a l ~ d i s t a n c e s ~ t h e r w s ~ o r ~ ( 3 ) ~ b o t h } } } \end{array} \right)
$$

The conformal 3-geometry is a geometric object that lends itself to definition and interpretation quite apart from the specific choice of coordinate system and even without need to use any coordinates at all. The conformal 3-geometry (on the hypersurface $\pmb { \Sigma }$ where T= constant） may be regarded much as one regards the magnetic feld in electromagnetism. The case of conformally flat 3-geometry,

$$
d s ^ { 2 } = \psi ^ { 4 } ( x , y , z ) d s _ { \mathrm { b a s e } } ^ { 2 }
$$

(with $g _ { i j b a s e } = \delta _ { i j }$ , is analogous to those initial-value situations in electromagnetism where the magnetic feld is everywhere zero (the time-antisymmetric initial-value problemof Bril);utnow weconsider thecaseofgenral $d s _ { \mathrm { b a s e } } ^ { 2 }$

The six metric coefficients $g _ { i j }$ of the conformal 3-geometry, subject to being changed by change of the three coordinates $x ^ { i }$ ,and undetermined at any one point up to a common position-dependent multiplicative factor,carry $6 - 3 - 1 = 2$ pieces of information per spacepoint. In this respect, they are like the components of the divergenceless magnetic field $\boldsymbol { \mathcal { B } }$ The corresponding field momentum $\pi _ { E M } ^ { i } \propto \delta ^ { i }$ (Box 21.1, page 496) has its divergence specified by the charge density,and so also carries

two pieces of information (in addition to the prescribed information about the density of charge) per spacepoint. （

The comparison is a little faulty between the components of $\boldsymbol { \mathcal { B } }$ and the metric coefficients. They are more like potentials than like components of the physically relevant field.

The appropriate measure of the “field” in geometrodynamics is the curvature tensor; but how can one possibly define a curvature tensor for a geometry that is asrudimentary as a conformal 3-geometry? York (l97l) has raised and answered this question. The Weyl conformal-curvature tensor [equation (l3.50) and exercise 13.13] is independent [in the proper $\textstyle { { \binom { 2 } { 2 } } }$ representation], in spaces of higher dimensionality,of the position-dependent factor $\psi ^ { \pm }$ with which one multiplies the metric coeffcients,but vanishes identically in three-dimensional space (exercise 21.21). One arrives at a non-zero conformally invariant measure of the curvature only when one goes to one higher derivative (exercise 21.22). In this way,one comes to York's curvature ${ \widetilde { \beta } } ^ { a \delta }$ ,here called $Y ^ { a b }$ , a tensor density with these properties:

York's curvature tensor

$$
\begin{array} { c } { { Y ^ { a b } = Y ^ { b a } ( \mathrm { s y m m e t r i c } ) ; } } \\ { { { } } } \\ { { Y _ { a } ^ { a } = 0 ( \mathrm { t r a c e l e s s } ) ; } } \\ { { { } } } \\ { { Y ^ { a b } { } _ { | b } = 0 ( \mathrm { t r a n s v e r s e } ) ; } } \end{array}
$$

$Y ^ { a b }$ invariant with respect to position-dependent changes in the conformal scale factor;

$Y ^ { a b } = 0$ when and only when the 3-geometry is conformally fat

$Y ^ { a b }$ provides what York calls the pure spin-two representation of the 3-geometry intrinsic to $\pmb { \Sigma }$ .It is the analog of the field $\mathcal { B }$ of electrodynamics on the spacelike initial-value simultaneity.It directly carries physical information about the conformal 3-geometry.

In addition to the conformal geometry $^ { ( 3 ) } <$ ,specified by the“potentials” $g _ { i j } / g ^ { 1 / 3 }$ ， and measured -by the “field components” $\gamma ^ { i j }$ ，one must also specify on $\pmb { \Sigma }$ the corresponding conjugate momenta:

$$
\widetilde { \pi } ^ { a b } = \widetilde { \pi } ^ { a b } ( \mathrm { s y m m e t r i c } ) ; \widetilde { \pi } _ { a } ^ { a } = 0 ( \mathrm { t r a c e l e s s } ) ;
$$

$\widetilde { \overline { { { \tau } } } } ^ { a \delta } { } _ { \mathfrak { i } \mathfrak { b } } = 0$ (transverse)incase thereisnofowofnergy in space;otherwise

$$
\widetilde { \pi } \sp { a b } \sb { | b } = 8 \pi ( { \mathrm { d e n s i t y ~ o f ~ f i o w ~ o f ~ e n e r g y } } ) \sp a ;
$$

two pieces of information (in addition to the prescribed information about the flow of energy) per spacepoint.

It might appear to be essential to specify with respect to which of the 3-geometries, distinguished from one another by different values of the conformal factor one calculates the covariant derivatives of tensor densities of weight $5 / 3$ (see $\ S 2 1 . 2 )$ in (21.148)and (21.149). However, York has shown that the conditions (21.149) do not in any way depend on the value of the conformal factor $\psi ^ { \pm }$

These equations (21.149) for what York calls the “momentum density of weight $5 / 3$ ”

$$
{ \widetilde { \pi } } ^ { a b } = g ^ { 1 / 3 } \biggl ( \pi ^ { a b } - { \frac { 1 } { 3 } } g ^ { a b } \mathrm { T r } \pi \biggr ) ,
$$

are linear,and therefore lend themselves to analysis by standard methods. It is a great help in this enterprise that York (l973a,b) has provided a “conformally invariant orthogonal decomposition of symmetric tensors on Riemannian manifolds” that allows one to generate solutions of these requirements ("transverse traceless,”“conformal Killing,” and “trace” parts,respectively, measure deformation of conformal part of geometry,mere recoordinatization, and change of scale). It is a further assistance,as York notes,that one has the same $\widetilde { \tau } ^ { a b }$ for an entire conformal equivalence class of metrics; that is, for a given

$$
\tilde { g } _ { a b } = g ^ { - 1 / 3 } g _ { a b } ,
$$

no matter how different the $g _ { a b }$ and $\psi$ themselves may be.

The conformal 3-geometry and the “momentum density of weight $5 / 3 "$ once picked,the remaining initial-value equation (21.116） then becomes the “scale” equation,

$$
8 { \pmb \nabla } ^ { 2 } \psi - { \ O ^ { ( 3 ) } } R \psi + M \psi ^ { - 7 } + Q \psi ^ { - 3 } - \frac { 3 } { 8 } \tau ^ { 2 } \psi ^ { 5 } = 0 ,
$$

for the determination of the conformal factor $\psi$ Here ${ \pmb { \nabla } } ^ { 2 }$ stands for the Laplacian

$$
\nabla ^ { 2 } \psi \equiv g ^ { - 1 / 2 } ( \partial / \partial x ^ { a } ) g ^ { 1 / 2 } g ^ { a b } ( \partial \psi / \partial x ^ { b } ) .
$$

It, like $^ { ( 3 ) } R , M ,$ and $Q$ ,refers to the base space. It is interesting that

$$
\nabla ^ { 2 } - \frac { 1 } { 8 } { } ^ { ( 3 ) } R
$$

is a conformally invariant wave operator, whereas ${ \pmb { \nabla } } ^ { 2 }$ itself is not. The quantity $M$ in York's analysis is an abbreviation for

$$
M \equiv g ^ { - 5 / 3 } g _ { a c } g _ { b d } \widetilde { \overline { { { \pi } } } } { } ^ { a b } \widetilde { \overline { { { \pi } } } } { } ^ { c d } ,
$$

and

$$
Q \equiv 1 6 \pi \rho _ { \mathrm { b a s e } } ( = 1 6 \pi \psi ^ { 8 } \rho = 1 6 \pi \psi ^ { 8 } \rho _ { \mathrm { i n f i n a l 3 - g e o m e t r y } } ) .
$$

One seeks a solution $\psi$ that is continuous over the closed manifold and everywhere real and positive.When does such a solution $\psi$ of the elliptic equation (21.152) exist? When is it unique? Always (when $M > 0$ and $\tau \neq 0$ ),is the result of O'Murchadha and York (1973); see also earlier investigations of Choquet-Bruhat (l972). Some of the physical considerations that come into this kind of problem have been discussed by Wheeler (1964a,pp.370-381).

# \$21.12. MACH'S PRINCIPLE AND THE ORIGIN OF INERTIA

In my opinion the general theory of relativity can only solve this problem [of inertia] satisfactorily ifit regardsthe world as spatially self-enclosed.

ALBERT EINSTEIN(1934),p.52.

On June 25,1913,two years before he had discovered the geometrodynamic law that bears his name, Einstein (1913b) wrote to Ernst Mach (Figure 21.5) to express his appreciation for the inspiration that he had derived for his endeavors from Mach's ideas.In his great book,The Science of Mechanics,Mach [(l9l2), Chapter 2, section 6] had reasoned that it could not make sense to speak of the acceleration of a mass relative to absolute space.Anyone trying to clear physics of mystical ideas would do better,he reasoned, to speak of acceleration relative to the distant stars. But how can a star at a distance of $1 0 ^ { 9 }$ light-years contribute to inertia in the here and the now? To make a long story short, one can say at once that Einstein's theory (l) identifies gravitation as the mechanism by which matter there infuences inertia here;(2) says that this coupling takes place on a spacelike hypersurface [in what one,without a closer examination,might mistakenly think to be a violation of the principle of causality; see Fermi(l932) for a discussion and clarification of the similar apparent paradox in electrodynamics； see also Einstein (1934),p. 84:“Moreover I believed that I could show on general considerations a law of gravitation invariant in relation to any transformation of coordinates whatever was inconsistent with the principle of causation. These were errors of thought which cost me two years of excessively hard work,until I finally recognized them as such at the end of 1915"]; (3) supplies in the initial-value equations of geometrodynamics a mathematical tool to describe this coupling; (4) demands closure of the geometry in space [one conjectures; see Wheeler (1959,1964c) and Honl (l962)],as a boundary condition on the initial-value equations if they are to yield a well-determined [and,we know now, a uniquel 4-geometry; and (5) identifies the collection of local Lorentz frames near any point in this resulting spacetime as what one means quantitatively by speaking of inertia at that point. This is how one ends up with inertia here determined by density and flow of mass-energy there.

No violation of causality. despite appearances

There are many scores of papers in the literature on Mach's principle, including many-even one by Lenin (English translation,l927)-one could call anti-Mach-ian; and many of them make interesting points [see especially the delightful dialog by Weyl (1924a) on “inertia and the cosmos,”and the article (1957) and book (1961) of Sciama]. However, most of them were written before one had anything like the understanding of the initial-value problem that one possesses today. Therefore no (continued on page 546)

An enormous literature

4.25. 13

Tth remen Xu Rullcyt:

![](images/26ab03acd4b355449e778035c1f7d3ba6ce56404457e7e2a16087b9da9356cd0.jpg)  
Figure 21.5. Einstein's appreciation of Mach,writen to Ernst Mach June 25,1913,while Einstein was working hard atarriving at the final November l915 formulationof standard general relativity.Regarding confirmation at a forthcoming eclipse:“If so,then your happy investigations on the foundations of mechanics,Planck's unjustified criticism notwithstanding,willreceive brilliant confrmation.For it necessarily turns out that inertia originates in a kind of interaction between bodies.quite in the sense of your considerations on Newton's pail experiment. The first consequence is on p. 6 of my paper. The following additional points emerge:(1) If one accelerates a heavy shellof matter S. then a mass enclosed by that shell experiences an accelerative force.(2) If one rotates the shell relative to the fixed stars about an axis going through its center,a Coriolis force arises in the interior of the shell; that is,the plane of a Foucault pendulum is dragged around (with a practically unmeasurably small angular velocity).”Following the death of Mach,Einstein (l916a）wrote a tribute to the man and his work.Reprinted with the kind permission of the estate of Albert Einstein, Helen Dukas and Otto Nathan,executors.

hku ja， afelren Hu guuk Mntersuihungm aibn du gunidlayu lin Mulum.k-Dlnch's.mguechr. pitgtu Kutk ju.hot-mi glinywa sestitiyry.Oemy daes'du Liyhuit  unu tix Wehuelmivhmmg n Hirpu hum gy uhn Sinu -Vneuch.

1) Bemhlemmiyt e wu tnir Puyelrhel yx ufiht uach der Thesria etm t -

![](images/2dc9fd12fe698d2cf07fcb50b35791108343556cba85017ea3ee57c79b290063.jpg)

Mingeloysmur Kirpu Lui tieeilha.   
\~guude .Kraft   
21Rter su tllnl Y hm eiu clureh lru. Miteyumkt geluuu Ala   
(ulatrr r Yyutm du Eetru(rut   
iyetuu)，u eltlt r   
  
klu"gierhudryktt)y "lo ei uu 'eue yrrut Trud   
Hhu. da mtul m hiuu,   
ru! Jte Kth Dlahe m   
zhm imn hirli \~mgnuh!   
futyt uoclulua mu. Mit grisern Hrhuchluug guur   
Llue hnylicl Lkr ugelmu it.生te\~. Js duwh iIlve huyke i   
thmy huB

attempt will be made to summarize or analyze the literature, which would demand a book in itself. Moreover, Mach's principle as presented here is more sharply formulated than Einstein ever put it in the literature [except for his considerations arguing that the universe must.be closed; see Einstein's book (l950),Pp. 107-108]; and Mach would surely have disowned it,for he could never bring himself to accept general (or even special) relativity.Nevertheless,it is a fact that Mach's principlethat mater there governs inertia here--and Riemann's idea--that the geometry of space responds to physics and participates in physics-were the two great currents of thought which Einstein,by means of his powerful equivalence principle,brought together into the present-day geometric description of gravitation and motion.

"Specify everyhere thedistribution andfowofmas-energy and thereby determine the inertial properties of every test particle everywhere and at all times". Spelled out, this prescription demands (l) a way of speaking about “everywhere": a spacelike hypersurface $\pmb { \Sigma }$ .Let one insist-in conformity with Einstein-(2) that it be a closed 3-geometry, and for convenience, not out of necesity, (3) that $\boldsymbol { \tau }$ be independent of position on $\pmb { \Sigma }$ . (4) Specify this 3-geometry to the extent of giving the conformal metric; without the specification of at least this much 3-geometry, there would be no evident way to say “where” the mas-energy is to be located. (5） Give density $\rho _ { \tt b a s e }$ as a function of position in this conformal 3-geometry. (6) Recognize that giving the mass-energy only of fields other than gravity is an inadequate way to specify the distribution of mas-energy throughout space. Formalistically,to be sure, the gravitational felds does not and cannot make any contribution to the source term that stands on the righthand side of Einstein's field equation. However, the analysis of gravitational waves (Chapters 18 and 35) shows that perturbations in the geometry ofscale small compared to the scale of observation have to be regarded as carrying an effective content of mass-energy. Moreover, one has in a geon [Wheeler(1955); Brilland Hartle (1964); for more on gravitational-wave energy, see $\ S 3 5 . 1 4 ]$ an object built out of gravitational waves (or electromagnetic waves, or neutrinos,or any combination of the three) that holds itself together for a time that is long in·comparison to the characteristic period of vibration of the waves.It looks from a distance like any other mass,even though nowhere in its interior can one put a finger and say “here is mass.” Therefore it, like any other mass,must have “its infuence on inertia.”But to specify this mass,one must give enough information to characterize completely the gravitational waves on the simultaneity $\pmb { \Sigma }$ . For this,it is not enough merely to have given the two “wave-coordinates” per spacepoint that one possesses in $^ { ( 3 ) } <$ . One must give in addition (7) the two “wave-momenta" per spacepoint that appear in York's “momentum density ofweight $5 / 3 , \ " \approx \mathbf { a } \mathbf { b }$ ; and at the same time,as an inextricable part of this operation, one must (8) specify the density of flow of field energy. (9) Solve for the conformal factor $\psi .$ (10)Then one has complete initial-value data that satisfy the initial-value equations of general relativity. (ll） These data now known, the remaining, dynamic, components of the field equation determine the 4-geometry into the past and the future.(l2) In this way,the inertial properties of every test particle are determined everywhere and at all times,giving concrete realization to Mach's principle.

Much must still be done to spell out the physics behind these equations and to see this physics in action. Some significant progress had already been made in this direction before the present stage in one's understanding of the initial-value equations.Especially interesting are results of Thirring (1918)and (1921) and of Thiring and Lense (1918),discussed by Einstein (195O) in the third edition of his book, The Meaning of Relativity.

Consider a bit of solid ground near the geographic pole, and a support erected there,and from it hanging a pendulum. Though the sky is cloudy, the observer watches the track of the Foucault pendulum as it slowly turns through. $3 6 0 ^ { \circ }$ . Then the sky clears and, miracle of miracles, the pendulum is found to be swinging all the time on an arc fixed relative to the far-away stars.If“mass there governs inertia here,” as envisaged by Mach, how can this be?

The Foucault pendulum

Enlarge the question. By the democratic principle that equal masses are created equal, the mass of the earth must come into the bookkeeping of the Foucault pendulum. Its plane of rotation must be dragged around with a slight angular velocity, $\omega _ { \tt d r a g } ,$ relative to the so-called “fixed stars.” How much is $\omega _ { \mathrm { d r a g } } ?$ And how much would $\omega _ { \tt d r a g }$ be if the pendulum were surrounded by a rapidly spinning spherical shell of mass $M$ and radius $R _ { \mathrm { s h e l l } } ,$ turning at angular velocity $\omega _ { \mathrm { s h e l l } } ?$

Einstein's theory says that inertia is a manifestation of the geometry of spacetime. It also says that geometry is affected by the presence of mater to an extent proportional to the factor $G / c ^ { 2 } = 0 . 7 4 2 \times 1 0 ^ { - 2 8 } \mathrm { c m / g }$ Simple dimensional considerations leave no room except to say that the rate of drag is proportional to a expression of the form

The dragging of the inertial frame

$$
\omega _ { \mathrm { d r a g } } = k \frac { G } { c ^ { 2 } } \frac { m _ { \mathrm { s h e l l , c o n v } } } { R _ { \mathrm { s h e l l } } } \omega _ { \mathrm { s h e l l } } = k \frac { m _ { \mathrm { s h e l l } } } { R _ { \mathrm { s h e l l } } } \omega _ { \mathrm { s h e l l } } .
$$

Here $k$ is a numerical factor to be found only by detailed calculation. Lense and Thirring [(l918) and (l92l)], starting with a flat background spacetime manifold, calculated in the weak-field approximation of Chapter 18 the effect of the moving current of mass on the metric. Expressed in polar coordinates,the metric acquires a non-zero coefficient $g _ { \phi t }$ .Inserted into the equation of geodesic motion, this offdiagonal metric coefficient gives rise to a precession. This precession (defined here about an axis parallel to the axis of rotation, not about the local vertical) is given by an expression of the form (21.155),where the precession factor $k$ has the value

$$
k = 4 / 3 .
$$

There is a close parallelism between the magnetic component of the Maxwell field and the precession component of the Einstein field. In neither field does a source at rest produce the new kind of effect when acting on a test particle that is also at rest. One designs a circular current of charge to produce a magnetic feld; and a test charge,in order to respond to this magnetic field,must also be in motion. Similarly here: no pendulum vibration means no pendulum precession. Moreover, the direction of the precession depends on where the pendulum is,relative to the rotating shell of mass. The precession factor $k$ has the following values:

$k = 4 / 3$ for pendulum anywhere inside rotating shell of mass;

$k = 4 / 3$ for pendulum at North or South pole; $k = - 2 / 3$ for pendulum just outside the rotating shell at its equator.

This position-dependence of the drag, $\omega _ { \tt d r a g } ,$ makes still more apparent the analogy with magnetism,where the field of a rotating charged sphere points North at the center of the sphere,and North at both poles,but South at the equator.

Whether the Foucault pendulum is located in imagination at the center of the earth or in actuality at the North pole,the order of magnitude of the expected drag is

$$
\begin{array} { c l c r } { \omega _ { \mathrm { d r a g } } \sim \displaystyle \frac { m _ { \mathrm { e a r t h } } } { R _ { \mathrm { e a r t h } } } \omega _ { \mathrm { e a r t h } } \sim \frac { 0 . 4 4 \mathrm { c m } } { 6 \times 1 0 ^ { 8 } \mathrm { c m } } \frac { \mathrm { l } \mathrm { r a d i a n } } { 1 3 7 0 0 \mathrm { s e c } } } \\ { \sim 5 \times 1 0 ^ { - 1 4 } \mathrm { r a d / s e c } , } \end{array}
$$

too small to allow detection, let alone actual measurement, by any device so far built--but perhaps measurable by gyroscopes now under construction $( \ S 4 0 . 7 )$ .By contrast, near a rapidly spinning neutron star or near a black hole endowed with substantial angular momentum, the calculated drag effect is not merely detectable; it is even important (see Chapter 33 on the physics of a rotating black hole).

The distant stars must influence the natural plane of vibration of the Foucault pendulum as the nearby rotating shell of matter does,provided that the stars are not so far away ( $r \sim$ radius of universe) that the curvature of space begins to introduce substantial corrections into the calculation of Thirring and Lense.In other words,no reason is apparent why all masses should not be treated on the same footing,so that (21.158) more appropriately,if also somewhat symbolically,reads

$$
\omega _ { \mathrm { p l a n e o f } } \sim \frac { m _ { \mathrm { s h e l l } } } { R _ { \mathrm { s h e l l } } } \omega _ { \mathrm { s h e l l } } + \sum _ { \mathrm { f a r - a w a y } } \frac { m _ { \mathrm { * } _ { \mathrm { s t a r } } } , } { r _ { \mathrm { * } _ { \mathrm { s t a r } } } , } \omega _ { \mathrm { * } _ { \mathrm { s t a r } } } , .
$$

Moreover, when there is no nearby shell of matter,or when it has negligible effects, the plane of vibration of the pendulum,if experience is any guide, cannot turn with respect to the frame defined by the far-away “stars.” In this event $\omega _ { \mathtt { F o u c a u l t } }$ must be identical with $\omega _ { \tt s t a r s }$ or the“sum for inertia,”

$$
\sum _ { \mathrm { f a r - a w } \mathrm { a y } } \frac { m _ { \mathrm { * } } } { r _ { \mathrm { * } \mathrm { s t a r } ^ { \mathrm { s } } } } { \sim } \frac { m _ { \mathrm { u n i v e r s e } } } { r _ { \mathrm { u n i v e r s e } } } ,
$$

must be of the order of unity.Just such a relation of approximate identity between the mass content of the universe and its radius at the phase of maximum expansion is a characteristic feature of the Friedman model and other simple models of a closed universe (Chapters 27 and 30). In this respect, Einstein's theory of Mach's principle exhibits a satisfying degree of self-consistency.

At phases of the dynamics of the universe other than the stage of maximum expansion, $r _ { \mathrm { u n i v e r s e } }$ can become arbitrarily small compared to $m _ { \mathrm { u n i v e r s e } }$ . Then the ratio (21.160) can depart by powers of ten from unity. Regardless of this circumstance, one has no option but to understand that the effective value of the “sum for inertia” is still unity after all corrections have been made for the dynamics of contraction or expansion,for retardation, etc. Only so can $\omega _ { \mathbf { F o u c a u l t } }$ retain its inescap-able identity with $\omega _ { \tt f a r }$ away starg-Fortunately,one does not have to pursue the theology of the“sum for inertia”to the uttermost of these sophistications to have a proper account of inertia. Mach's idea that mass there determines inertia here has its complete mathematical account in Einstein's geometrodynamic law,as already speled out.For-the first strong-field analysis of the dragging of the inertial reference system in the context of relativistic cosmology, see Brill and Cohen (1966) and Cohen and Brill (1967)； see also $\ S 3 3 . 4$ for dragging by a rotating black hole.

Still another clarification is required of what Mach's principle means and how it is used.The inertial properties of a test particle are perfectly well-determined when that particle is moving in ideal Minkowski space.“Point out, please,” the anti-Machian critic says,“the masses that are responsible for this inertia.”In answer,recall that Einstein's theory includes not only the geometrodynamic law, but also, in Einstein's view,the boundary condition that the universe be closed.Thus the section of spacetime that is flat is to be viewed, not as infinite,but as part of a closed universe. (For a two-dimensional analog,fill a rubber balloon with water and set it on a glass tabletop and look at it from underneath). The part of the universe that is curved acquires its curvature by reason of its actual content of mass-energy or--if animated only by gravitational waves-by reason of its effective content of mass-energy. This mass-energy,real or effective,is to be viewed as responsible for the inertial properties of the test particle that at first sight looked all alone in the universe.

It in no way changes the qualitative character of the result to turn attention to a model universe where the region of Minkowski flatness,and all the other linear dimensions of the universe, have been augmented tenfold("ten times larger balloon; ten times larger face"). The curvature and density of the curved part of the model universe are down by a factor of 10o, the volume is up by a factor of 1,000,the mass is up by a factor of 1O;but the ratio of mass to radius, or the“sum for inertia” (the poor man's substitute for a complete initial-value calculation) is unchanged.

Einstein acknowledged a debt of parentage for his theory to Mach's principle (Figure 21.5). It is therefore only justice that Mach's principle should in return today owe its elucidation to Einstein's theory.

Minkowski geometry as limit of a closed 3-geometry

# Exercise 21.21. WHY THE WEYL CONFORMAL CURVATURE TENSOR VANISHES

# EXERCISES

How many independent components does the Riemann curvature tensor have in threedimensional space? How many does the Ricci curvature tensor have? Show that the two tensors are related by the formula

$$
\begin{array} { c } { { R ^ { d } { } _ { a b c } = \delta _ { b } ^ { d } R _ { a c } - \delta _ { c } ^ { d } R _ { a b } + g _ { a c } R ^ { d } { } _ { b } - g _ { a b } R _ { c } ^ { d } } } \\ { { { } } } \\ { { + \displaystyle { \frac { 1 } { 2 } R ( \delta _ { c } ^ { d } g _ { a b } - \delta _ { b } ^ { d } g _ { a c } ) } } } \end{array}
$$

with no need of any Weyl conformal-curvature tensor to specify (as in higher dimensions) the further details of the Riemann tensor. Show that the Weyl tensor, from an $\pmb { n }$ -dimensional modification of equation (l3.50) as in exercise l3.l3,vanishes for $n = 2$

# Exercise 21.22. YORK'S CURVATURE

[York (197l)]. (a) Define the tensor [Eisenhart (1926)]

$$
R _ { a b c } = R _ { a b \mid c } - R _ { a c \mid b } + { \frac { 1 } { 4 } } ( g _ { a e } R _ { \mid b } - g _ { \pi b } R _ { 1 \bar { c } } ) .
$$

(b) Show that a 3-geometry is conformall flat when and only when $R _ { a b c } = 0$

(c) Show that the following identities hold and reduce to five the number of independent components of $R _ { a b c }$ ：

$$
\begin{array} { c } { { R ^ { a } { } _ { a c } = g ^ { a b } R _ { b a c } = 0 ; } } \\ { { { } } } \\ { { R _ { a b c } + R _ { a c b } = 0 ; } } \\ { { { } } } \\ { { R _ { a b c } + R _ { c a b } + R _ { b c a } = 0 . } } \end{array}
$$

(d) Show that Yorks’ curvature

$$
\begin{array} { c } { { Y ^ { a b } = g ^ { 1 / 3 } [ a e f ] \left( R _ { t } ^ { \ b } - \frac 1 4 \delta _ { t } ^ { \ b } R \right) _ { | e } } } \\ { { { } } } \\ { { { } = - \frac 1 2 g ^ { 1 / 3 } [ a e f ] g ^ { b m } R _ { m e f } } } \end{array}
$$

is conformally invariant and has the properties listed in equations (21.148).

# Exercise 21.23. PULLING THE POYNTING FLUX VECTOR “OUT OF THE AIR"

From the condition that the Hamilton-Jacobi functional $S ( g _ { i j } , A _ { m } )$ (extremal of the action integral) for the combined Einstein and Maxwellfields,ostensibly dependent on the six metric coefficients $g _ { i j } ( x , y , z )$ and the three potentials $A _ { m } ( x , y , z )$ , shall actually depend only on the 3-geometry of the spacelike hypersurface and the distribution of magnetic field strength on this hypersurface,show that the geometrodynamic field momentum $\pi ^ { i j } = \delta S / \delta g _ { i j }$ satisfies a condition of the form

$$
\pi ^ { i j } { } _ { | j } = c [ i m n ] \mathcal { E } _ { m } \mathcal { B } _ { n } ,
$$

and evaluate the coefficient $\pmb { c }$ in this equation [Wheeler(l968b)). Hint: Note that the transformation

$$
x ^ { i } \longrightarrow x ^ { i } - \xi ^ { i } , g _ { i j } \longrightarrow g _ { i j } + \xi _ { i \mid j } + \xi _ { j \mid i }
$$

in no way changes the 3-geometry itself, and therefore the corresponding induced change in $s$ ，

$$
\delta S = \int \biggl [ \frac { \delta S } { \delta g _ { i j } } \delta g _ { i j } + \frac { \delta S } { \delta A _ { m } } \delta A _ { m } \biggr ] d ^ { 3 } x
$$

must vanish identically for arbitrary choice of the $\xi ^ { i } ( x , y , z )$ ，which measure the equivalent of the sliding of a ruled transparent rubber sheet over an automobile fender.

# Exercise 21.24. THE EXTREMAL ACTION ASSOCIATED WITH THE HILBERT ACTION PRINCIPLE DEPENDS ON CONFORMAL 3-GEOMETRY AND EXTRINSIC TIME [K. Kuchar (1972) and J. York (1972)]

Show that the data demanded by the Hilbert action principle $\delta \int ^ { ( 4 ) } R ( - { } ^ { ( 4 ) } g ) ^ { 1 / 2 } d ^ { 4 } x = 0$ on each of the two bounding spacelike hypersurfaces consist of (l) the conformal 3-geometry $^ { ( 3 ) } <$ of the hypersurface plus (2)the extrinsic time variable defined by

$$
\tau = \frac { 2 } { 3 } g ^ { - 1 / 2 } \operatorname { T r } \pmb { \pi } = \frac { 4 } { 3 } \operatorname { T r } \pmb { K } ,
$$

conveniently represented by the pictogram $\approx$ ，measured by one number per spacepoint, and independent of the conformai factor in the metric of the 3-geometry.This done, explain in a few words why in this formulation of geometrodynamics the Hamilton-Jacobi function $\hbar$ times the phase of the wave function in the semiclassical or JWKB approximation) is appropriately expressed in the form

$$
S = S ( ^ { ( 3 ) } < , \breve { \varkappa } ) .
$$

# \$21.13. JUNCTION CONDITIONS

The intrinsic and extrinsic curvatures of a hypersurface, which played such fundamental roles in the initial-value formalism,are also powerful tools in the analysis of “junction conditions.”

Recall the junction conditions of electrodynamics: across any surface (e.g.， a capacitor plate), the tangential part of the electric feld, $\pmb { { \cal E } } _ { | | } ,$ and the normal part of the magnetic field, $\pmb { B } _ { \perp }$ ，must be continuous; thus,

Junction conditions for electrodynamics

$$
\begin{array} { r l } & { [ E _ { | | } ] \equiv ( \mathrm { d i s c o n t i n u i t y ~ i n ~ } E _ { | | } ) } \\ & { ~ \equiv ( E _ { | | } \mathrm { ~ o n ~ } ^ { \omega _ { \mathrm { + } } } + ^ { , \prime } \mathrm { ~ s i d e ~ o f ~ s u r f a c e } ) - ( E _ { | | } \mathrm { ~ o n ~ } ^ { \omega _ { \mathrm { - } } } - ^ { , \prime } \mathrm { ~ s i d e ~ o f ~ } } \\ & { ~ \mathrm { s u r f a c e } ) } \\ & { ~ \equiv E _ { | | } ^ { + } - E _ { | | } ^ { - } = 0 , } \\ & { [ B _ { \perp } ] \equiv B _ { \perp } ^ { + } - B _ { \perp } ^ { - } = 0 ; } \end{array}
$$

while the“jump” in the parts $\pmb { E } _ { \bot }$ and $\pmb { { \cal B } } _ { | | }$ must be related to the charge density (charge per unit area) $\pmb { \sigma }$ ,the current density (current per unit area) $j ,$ and the unit normal to the surface $\pmb { n }$ by the formulas

$$
\begin{array} { c } { { [ E _ { \perp } ] = E _ { \perp } ^ { + } - E _ { \perp } ^ { - } = 4 \pi \sigma n , } } \\ { { { } } } \\ { { [ B _ { | | } ] = B _ { | | } ^ { + } - B _ { | | } ^ { - } = 4 \pi j \times n . } } \end{array}
$$

Recall also that one derives these junction conditions by integrating Maxwell's equations over a “pill box” that is centered on the surface.

Similar junction conditions,derivable in a similar manner,apply to the gravitational field (spacetime curvature),and to the stress-energy that generates it.\* Focus

![](images/c21f9e38ac294c33fc8cb79dab8c029b713af112c10ca04046de8f65b17cea33.jpg)  
Figure 21.6. Gaussian normal coordinates in the neighborhood of a 3-surface $\pmb { \Sigma }$ The metric in Gaussian normal coordinates has the form

$$
d s ^ { 2 } = ( { \pmb { n } } \cdot { \pmb { n } } ) ^ { - 1 } d n ^ { 2 } + g _ { i j } d x ^ { i } d x ^ { j }
$$

with ${ \pmb n } = \partial / \partial n$ ， $( { \pmb n } \cdot { \pmb n } ) = - 1$ if the surface is spacelike,and $( \pmb { n } \cdot \pmb { n } ) = 1$ if it is timelike.(See exercise 27.2.) The extrinsic curvature of the surfaces $\pmb { n } =$ constant is $K _ { i j } = - \textstyle { \frac { 1 } { 2 } } \hat { \sigma } g _ { i j } / \hat { \sigma } n$ ,and the Einstein field equations writen in $" 3 + 1 "$ form are (21.162).

Einstein equation in $3 + 1$ ： form

attention on a specific three-dimensional slice through spacetime-the 3-surface $\pmb { \Sigma }$ on Figure 21.6. Let the surface be either spacelike [unit normal $\pmb { n }$ timelike; $( \pmb { n } \cdot \pmb { n } ) = - 1 ]$ or timelike [n spacelike; $( \pmb { n } \cdot \pmb { n } ) = + 1 ]$ . The null case will be discussed later.As an aid in deriving junction conditions, introduce Gaussian normal coordinates in the neighborhood of $\pmb { \Sigma }$ [see the paragraph preceeding equation (21.82)]. In terms of the intrinsic and extrinsic curvatures of $\pmb { \Sigma }$ and of neighboring 3-surfaces $n =$ constant, the Einstein tensor and Einstein field equation have components

$$
\begin{array} { l } { { G ^ { n } { } _ { n } = \displaystyle - \frac { 1 } { 2 } { } ^ { ( 3 ) } R + \frac { 1 } { 2 } ( n \cdot n ) ^ { - 1 } \{ ( \mathrm { T r } K ) ^ { 2 } - \mathrm { T r } ( K ^ { 2 } ) \} = 8 \pi T ^ { n } { } _ { n } , } } \\ { { \displaystyle G ^ { n } { } _ { i } = - ( n \cdot n ) ^ { - 1 } \{ K _ { i } ^ { m } | _ { m } - ( \mathrm { T r } K ) _ { | i } \} = 8 \pi T ^ { n } { } _ { i } , } } \\ { { G ^ { i } { } _ { j } = { } ^ { ( 3 ) } G ^ { i } { } _ { j } + ( n \cdot n ) ^ { - 1 } \{ ( K ^ { i } { } _ { j } - \delta ^ { i } { } _ { j } \mathrm { T r } K ) _ { , n } } } \\ { { \displaystyle ~ - ( \mathrm { T r } K ) K _ { j } ^ { i } + \frac { 1 } { 2 } \delta ^ { i } { } _ { j } ( \mathrm { T r } K ) ^ { 2 } + \frac { 1 } { 2 } \delta ^ { i } { } _ { j } \mathrm { T r } ( K ^ { 2 } ) \} = 8 \pi T ^ { i } { } _ { j } . } } \end{array}
$$

Surface stress-energy tensor

[See equations (21.77), (21.81), (21.76),and (21.82).]

Suppose that the stress-energy tensor $T ^ { \alpha } { } _ { \beta }$ contains a “delta-function singularity” at $\pmb { \Sigma }$ i.e.,suppose that $\pmb { \Sigma }$ is the“world tube”of a two-dimensional surface with finite 4-momentum per unit area (analog of surface charge and surface current in electrodynamics). Then define the surface stress-energy tensor on $\pmb { \Sigma }$ to be the integral of $T ^ { \alpha } { } _ { \beta }$ with respect to proper distance $( n )$ ，measured perpendicularly through $\pmb { \Sigma }$ ：

$$
{ S ^ { \alpha } } _ { \beta } = \underset { \varepsilon  0 } { \mathrm { L i m } } \biggl [ \int _ { - \varepsilon } ^ { + \varepsilon } T _ { \beta } ^ { \alpha } d n \biggr ] .
$$

To discover the efect of this surface layer on the spacetime geometry, perform a "pil-box integration”of the Einstein field equation (21.162)

$$
\operatorname * { L i m } _ { \varepsilon \to 0 } \left[ \int _ { - \varepsilon } ^ { + \varepsilon } G ^ { \alpha } { } _ { \beta } d n \right] = 8 \pi S ^ { \alpha } { } _ { \beta } .
$$

Derivation of junction conditions

Examine the integral of $G ^ { \alpha } { } _ { \beta }$ If the 3-metric $g _ { i j }$ were to contain a delta function or a discontinuity at $\pmb { \Sigma }$ then $\pmb { \Sigma }$ would not have any well-defined 3-geometry-a physically inadmissble situation, even in the presence of surface layers. Absence of delta functions, $\delta ( { \pmb n } )$ ,in $g _ { i j }$ means absence of delta functions in $^ { ( 3 ) } R$ ； absence of discontinuities in $g _ { i j }$ means absence of delta functions in $K _ { i j } = - { \textstyle \frac { 1 } { 2 } } g _ { i j , n }$ Thus, equations (21.162) when integrated say

$$
\begin{array} { c } { { { \stackrel { . } { \int } } G _ { ~ n } ^ { n } d \stackrel { . } { n } = 0 = 8 \pi S _ { ~ n } ^ { n } , } } \\ { { { \stackrel { . } { \int } } G _ { ~ i } ^ { n } d n = 0 = 8 \pi S _ { ~ i } ^ { n } , } } \\ { { { \stackrel { . } { \int } } G _ { ~ j } ^ { i } \cdot d n = ( n \cdot n ) ( \gamma _ { ~ j } ^ { i } - \delta _ { ~ j } ^ { i } \mathrm { T r } \gamma ) = 8 \pi S _ { ~ j } ^ { i } , } } \end{array}
$$

where $\gamma _ { \ j } ^ { \ i }$ is the “jump” in the components of the extrinsic curvature

$$
\begin{array} { r l } & { \gamma \equiv [ K ] \equiv ( K \circ \mathfrak { n } \ ^ { \ast } n = + \varepsilon \ \mathrm { s i d e } ^ { \prime } \ \mathrm { o f } \ \mathcal { L } ) - ( K \circ \mathfrak { n } \ ^ { \ast } n = - \varepsilon \ \mathrm { s i d e } ^ { \prime } \ \mathrm { o f } \ \mathcal { L } ) } \\ & { \quad \equiv K ^ { + } - K ^ { - } . } \end{array}
$$

In the absence of a delta-function surface layer, the above junction conditions say,simply, that $\pmb { \gamma } \equiv [ \pmb { K } ] = 0$ . In words: if one examines how $\pmb { \Sigma }$ is embedded in the spacetime above its “upper"face,and how it is embedded in the spacetime below its “lower” face, one must discover identical embeddings--i.e., identical extrinsic curvatures K. Of course, the intrinsic curvature of $\pmb { \Sigma }$ must also be the same, whether viewed from above or below. More briefly:

$$
\mathrm { a b s e n c e ~ o f ~ s u r f a c e ~ l a y e r s ) } \overrightarrow { \longleftarrow } ( \mathrm { ^ * c o n t i n u i t y ^ { \prime \prime } ~ o f ~ } g _ { i j } \mathrm { ~ a n d ~ } K _ { i j } ) .
$$

Junction conditions in absence of surface layers

If a surface layer is present, then $\pmb { \Sigma }$ must be the world tube of a two-dimensional layer of mater, and the normal to $\pmb { \Sigma }$ must be spacelike, $( \pmb { n } \cdot \pmb { n } ) = + 1$ . The junction conditions (21.165a,b) then have the simple physical meaning

$$
\begin{array} { r } { \pmb { S } ( n , . . . ) = 0 \pm \operatorname* { m a x } _ { \mathbf { \lambda } } \left( \begin{array} { l } { \mathrm { t h e ~ m o m e n t u m ~ f l o w ~ i s ~ e n t i r e l y ~ i n ~ } E ; \mathrm { , } } \\ { \mathrm { i . e . , ~ n o ~ m o m e n t u m ~ a s s o c i a t e d ~ w i t h ~ t h e } } \\ { \mathrm { s u r f a c e ~ l a y e r ~ f l o w s ~ o u t ~ o f ~ } E ; \mathrm { i . e . , ~ } E } \\ { \mathrm { i s ~ t h e ~ w o r l d ~ t u b e ~ o f ~ t h e ~ s u r f a c e ~ l a y e r } } \end{array} \right) , } \end{array}
$$

which tells one nothing new. The junction condition (21.165c) says that the surface stress-energy generates a discontinuity in the extrinsic curvature (different embedding in spacetime “above” $\pmb { \Sigma }$ than “below” $\pmb { \Sigma }$ ), given by

$$
\gamma ^ { i } { } _ { j } - \delta ^ { i } { } _ { j } \operatorname { T r } \gamma = 8 \pi S ^ { i } { } _ { j } .
$$

Of course, the intrinsic geometry of $\pmb { \Sigma }$ must be the same as seen from above and below, $g _ { i j }$ continuous across $\pmb { \Sigma }$ (21.169)

Junction conditions for a surface layer

In analyzing surface layers, one uses not only the junction conditions (21.168a) to (21.169), but also the four-dimensional Einstein field equation applied on each side of the surface $\pmb { \Sigma }$ separately,and also an equation of motion for the surface stressenergy.The equation of motion is derived by examining the jump in the field equation $G _ { \ i } ^ { n } = 8 \pi T _ { \ i } ^ { n }$ (equation 21.162b)； thus $[ G ^ { n } { } _ { i } ] = 8 \pi [ T ^ { n } { } _ { i } ]$ says

$$
( { \gamma _ { i } } ^ { m } - { \delta _ { i } } ^ { m } \operatorname { T r } \gamma ) _ { | m } = - 8 \pi [ { T ^ { n } } _ { \mathrm { i } } ] ;
$$

and when reexpressed in terms of $S _ { i } ^ { { m } }$ by means of the junction condition (21.168b), it says

Equation of motion for a surface layer

$$
{ \cal S } ^ { i m } { } _ { | m } + [ T ^ { i n } ] = 0 .
$$

[For intuition into this equation of motion, see Exercises 21.25 and 21.26. For applications of the “surface-layer formalism”see exercise 21.27；also Israel (1966). Kuchar (1968), Papapetrou and Hamoui (1968).]

Gravitational-wave shock fronts

When one turns attention to junction conditions across a null surface $\pmb { \Sigma }$ ,one finds results rather different from those in the spacelike and timelike cases.A“pill-box” integration of the field equations reveals that even in vacuum the extrinsic curvature may be discontinuous.A discontinuity in $K _ { i j }$ across a null surface, without any stress-energy to produce it, is the geometric manifestation of a gravitational-wave shock front (analog of a shock-front in hydrodynamics). For quantitative details see, e.g.,Pirani (1957),Papapetrou and Treder (1959,1962), Treder (1962),and especially Choquet-Bruhat (1968b).

That a discontinuity in the curvature tensor can propagate with the speed of light is a reminder that all gravitational effects, like all electromagnetic effects, obey a causal law. The initial-value data on a spacelike initial-value hypersurface uniquely determine the resulting spacetime geometry [see the work of Cartan, Stellmacher, Lichnerowicz,and Bruhat (also under the names Foures-Bruhat and Choquet-Bruhat) and others cited and summarized in the article of Bruhat (l962)] but determine it in a way consistent with causality. Thus a change in these data throughout a limited region of the initial value 3-geometry makes itself felt on a slightly later hypersurface solely in a region that is also limited,and only a little larger than the original region.

When one turns from classical dynamics to quantum dynamics, one sees new reason to focus attention on a spacelike initial-value hypersurface: the observables at different points on such a hypersurface commute with one another; i.e., are in principle simultaneously observable.

Not every four-dimensional manifold admits a global singularity-free spacelike hypersurface. Those manifolds that do admit such a hypersurface have more to do with physics,it is possible to believe, than those that do not.

Even in a manifold that does admit a spacelike hypersurface, attention has been given sometimes, in the context of classical theory, to initial-value data on a hypersurface that is not spacelike but “characteristic,” in the sense that it accomodates null geodesics [see,for example,Sachs (l964) and references cited there].It is typical in such situations that one can predict the future but not the past, or predict the past but not the future.

Children of.light and children of darkness is the vision of physics that emerges from this chapter,as from other branches of physics.The children of light are the differential equations that predict the future from the present. The children of darkness are the factors that fix these initial conditions.

# Exercise 21.25. EQUATION OF MOTION FOR A SURFACE LAYER

# EXERCISES

(a) Let $\pmb { u }$ be the“mean 4-velocity”of the matter in a surface layer-so defined that an Observer moving with 4-velocity $\pmb { u }$ sees zero energy flux. Let $\pmb { \sigma }$ be the total mass-energy per unit proper surface area,as measured by such a“comoving observer.”Show that the surface stress-energy tensor can be expressed in the form

$$
\pmb { S } = \sigma \pmb { u } \otimes \pmb { u } + \pmb { t } , \mathrm { w h e r e } \ ( \pmb { t } \cdot \pmb { u } ) = 0 ,
$$

and where $\pmb { t }$ is a symmetric stress tensor.

(b) Show that the component along $\pmb { u }$ of the equation of motion (21.170) is

$$
d \sigma / d \tau = - \sigma u ^ { j } { } _ { | j } + u _ { j } t ^ { j k } { } _ { | k } + u _ { j } [ T ^ { j n } ] ,
$$

where $d / d \tau = \pmb { \mathscr { u } }$ Give a physical interpretation for each term.

(c)Let $a _ { j }$ be that part of the 4-acceleration of the comoving observer which lies in the surface layer $\pmb { \Sigma }$ .By projecting the equation of motion (21.170) perpendicular to ${ \pmb u }$ ，show that

$$
\sigma a _ { j } = - P _ { j a } \{ t ^ { a b } { } _ { | b } + [ T ^ { a n } ] \} ,
$$

where $P _ { j a }$ is the projection operator

$$
P _ { j a } = g _ { j a } + u _ { j } u _ { a } .
$$

Give a physical interpretation for each term of equation (21.182).

# Exercise 21.26. THIN SHELLS OF DUST

For a thin shell of dust surrounded by vacuum $( [ T ^ { j n } ] = 0$ ， $\pmb { t } = 0$ ，derive the following equations

$$
d \sigma / d \tau = - { \sigma } { u ^ { b } } _ { | b } ,
$$

$$
{ \pmb a } ^ { + } + { \pmb a } ^ { - } = 0 ,
$$

$$
a ^ { + } - a ^ { - } = ( 4 \pi \sigma ) n
$$

$$
\pmb { \gamma } = 8 \pi \sigma \bigg ( \pmb { u } \otimes \pmb { u } + \frac { 1 } { 2 } \pmb { g } \bigg ) .
$$

Here $\pmb { \hat { e } } ^ { + }$ and $\pmb { a } ^ { - }$ are the 4-accelerations as measured by accelerometers that are fastened onto the outer and inner sides of the shell,and $\pmb { \mathscr { g } }$ is the $^ 3$ -metric of the shell. Show that the first of these equations is the law of “conservation of rest mass.”

# Exercise 21.27. SPHERICAL SHELL OF DUST

Apply the formalism of exercise 21.25 to a collapsing spherical shell of dust [Israel (1967b)]. For the metric inside and outside the shell.take the flat-spacetime and vacuum Schwarzschild expressions (Chapter 23),

$$
d s ^ { 2 } = { } - \left( 1 - { \frac { 2 M } { r } } \right) d t ^ { 2 } + { \frac { d r ^ { 2 } } { 1 - 2 M / r } } + r ^ { 2 } ( d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } ) \ \mathrm { o u t s i d e } .
$$

Let the“radius” of the shell,as a function of proper time measured on the shell, be

$$
R \equiv { \frac { 1 } { 2 \pi } } \times ( { \mathrm { p r o p e r ~ c i r c u m f e r e n c e ~ o f ~ s h e l l } } ) = R ( \tau ) .
$$

Show that the shell's mass density varies with time as

$$
\sigma ( \tau ) = \mu / 4 \pi R ^ { 2 } ( \tau ) , ~ \mu = \mathrm { c o n s t a n t } = { } ^ { \cdot \circ } \mathrm { t o t a l ~ r e s t ~ m a s s ^ { \circ } ; }
$$

and derive and solve the equation of motion

$$
M = \mu \left\{ 1 + \left( { \frac { d R } { d \tau } } \right) ^ { 2 } \right\} ^ { 1 / 2 } - { \frac { \mu } { 2 R } } .
$$

CHAPTER 22

# THERMODYNAMICS,HYDRODYNAMICS, ELECTRODYNAMICS，GEOMETRIC OPTICS,AND KINETIC THEORY

# \$22.1. THE WHY OF THIS CHAPTER

Astrophysical applications of gravitation theory are the focus of the rest of this book, except for Chapters 41-44. Each application-stars,star clusters,cosmology,collapse, black holes,gravitational waves,solar-system experiments-can be pursued by itself at an elementary level,-without reference to the material in this chapter. But deep understanding of the applications requires a prior grasp of thermodynamics, hydrodynamics, electrodynamics,geometric optics,and kinetic theory,all in the context of curved spacetime. Hence, most Track-2 readers will want to probe these subjects at this point.

This chapter is entirely Track 2. No earlier Track-2 material is needed as preparation for it. but Chapter 5 (stress-energy tensor) will be helpful.

$\$ 22.5$ (geometric optics) is needed as preparation for Chapter 34 (singularities and global methods). The rest of the chapter is not needed as preparation for any later chapter;but it will be extremely helpful in most applications of gravitation theory (Chapters 23-40).

# \$22.2. THERMODYNAMICS IN CURVED SPACETIME\*

Consider, for concreteness and simplicity,the equilibrium thermodynamics of a perfect fluid with fixed chemical composition ("simple perfect fuid")-for example, the gaseous interior of a collapsing supermassive star. The thermodynamic state of a fluid element, as it passes through an event ${ \mathcal { P } } _ { 0 }$ ,can be characterized by various thermodynamic potentials, such as $n , \ \rho , \ p , \ T , \ s , \ \mu$ ，The numerical value of each potential at $\mathcal { P } _ { 0 }$ is measured in the proper reference frame $( \ S 1 3 . 6 )$ of an observer who moves with the fluid element-i..,in the fluid element's“rest frame.” Despite

Thermodynamic potentials are defined in rest frame of fluid

this use of rest frame to measure the potentials. the potentials are frame-independent functions (scalar fields). At the chosen event $\boldsymbol { \mathfrak { P } } _ { 0 }$ ,a given potential (e.g., n) has a unique value $n ( \mathfrak { s } \mathfrak { P } _ { 0 } )$ ：so $\pmb { n }$ is a perfectly good frame-independent function.

The values of $n , \rho , p , T , s , \mu$ measure the following quantities in the rest frame of the fluid element:

# Definitions of thermodynamic potentials

$\pmb { n }$ ，baryon number density: i.e., number of baryons per unit three-dimensional volume of rest frame, with antibaryons (if any) counted negatively.   
$\pmb { \rho }$ ，density of total mass-energy; i.e., total mass-energy (including rest mass, thermal energy,compressional energy,etc.) contained in a unit three-dimensional volume of the rest frame.   
$\boldsymbol { p }$ ，isotropic pressure in rest frame.   
$T ,$ temperature in rest frame.   
$s$ ， entropy per baryon in rest frame. (The entropy per unit volume is ns.)   
$\mu$ ,chemical potential of baryons in rest frame [see equation (22.8) below].

Definition of “simple fluid'

The chemical composition of the fluid (number density of hydrogen molecules, number density of hydrogen atoms, number density of free protons and electrons, number density of photons,number density of $^ { 2 3 8 } \mathrm { U }$ nuclei, number density of $\pmb { A }$ hyperons ..)is assumed to be fixed uniquely by two thermodynamic variables-e.g, by the total number density of baryons $\pmb { n }$ and the entropy per baryon s. In this sense the fluid is a“simple fuid.” Simple fluids occur whenever the chemical abundances are“frozen” (reaction rates too slow to be important on the time scales of interest; for example, in a supermassive star except during explosive burning and except at temperatures high enough for $e ^ { - } - e ^ { + }$ pair production).Simple fluids also occur in the opposite extreme of complete chemical equilibrium (reaction rates fast enough to maintain equilibrium despite changing density and entropy; for example, in neutron stars,where high pressures speed up all reactions). When one examines nuclear burning in a nonconvecting star, or explosive nuclear burning,or pair production and neutrino energy losses at high temperatures, one must usually treat the fluid as “multicomponent.” Then one introduces a number density $n _ { J }$ and a chemical potential $\mu _ { J }$ for each chemical species with abundance not fixed by $\pmb { n }$ and s.For further details see, e.g., Zel'dovich and Novikov (1971).

The most fundamental law of thermodynamics-even more fundamental than the “first”and “second” laws-is baryon conservation.Consider a fluid element whose moving wals are attached to the fluid so that no baryons flow in or out.As the fluid element moves through spacetime,deforming along the way,its volume $V$ changes. But the number of baryons in it must remain fixed,so

$$
\frac { d } { d \tau } \left( n V \right) = 0 .
$$

The changes in volume are produced by the flow of neighboring bits of fluid away from or toward each other-explicitly (exercise 22.1)

$$
d V / d \tau = ( \nabla \cdot \pmb { u } ) V ,
$$

where $\pmb { \mu } = \pmb { d } / d \tau$ is the 4-velocity of the fluid. Consequently, baryon conservation [equation (22.1)] can be reexpressed as

$$
0 = \frac { d n } { d \tau } + \frac { n } { V } \frac { d V } { d \tau } = \nabla _ { u } n + n ( \nabla \cdot u ) = u \cdot \nabla n + n ( \nabla \cdot u ) = \nabla \cdot ( n u ) ;
$$

i.e.,

$$
\begin{array} { r } { \pmb { \nabla } \cdot \pmb { s } = 0 , } \end{array}
$$

(see $\ S 5 . 4$ and exercise 5.3.) Moreover,this abstract geometric version of the law must be just as valid in curved spacetime as in flat (equivalence principle).

Note the analogy with the law of charge conservation, $\pmb { \nabla } \cdot \pmb { J } = 0$ ,in electrodynamics (exercise 3.16) and with the local law of energy-momentum conservation, $\pmb { \bigtriangledown } \cdot \pmb { \cal T } = 0$ $\mathfrak { S } \mathfrak { S } \mathfrak { S } . 9$ and 16.2). In a very deep sense,the forms of these three laws are dictated by the theorem of Gauss (S5.9,and Boxes 5.3,5.4).

The second law of thermodynamics states that, in flat spacetime or in curved, entropy can be generated but not destroyed. Apply this law to a fluid element of volume $V$ containing a fixed number of baryons $N .$ The entropy it contains is

Second law of thermodynamics

$$
S = N s = n s V .
$$

Entropy may flow in and out across the faces of the fuid element ("heat flow” between neighboring fluid elements); but for simplicity assume it does not; or if it does,assume that it flows too slowly to have any significance for the problem at hand. Then the entropy in the fluid element can only increase:

$$
d ( n s V ) / d \tau \geq 0
$$

i.e. [combine with equation (2.1)]

$$
d s / d \tau \geq 0 \ ( \mathrm { n o \ e n t r o p y \ e x c h a n g e } ) .
$$

Shock waves and heat flow

So long as the fluid element remains in thermodynamic equilibrium, its entropy will actually be conserved $[ ^ { 6 6 } = "$ in equation (22.5)]; but at a shock wave,where equilibrium is momentarily broken, the entropy will increase (conversion of "relative kinetic energy”of neighboring fluid elements into heat). [For discussions of heat flow in special and general relativity, see Exercise 22.7.For discussion of shock waves, see Taub (1948),de Hoffman and Teller (1950), Israel (1960),May and White (1967), Zel'dovich and Rayzer (1967),Lichnerowicz (1967,1971),and Thorne (1973a).]

The first law of thermodynamics, in the proper reference frame of a fuid element, is identical to the first law in flat spacetime ("principle of equivalence"); and in flat spacetime the first law is merely the law of energy conservation:

First law of thermodynamics

$$
d { \binom { \mathrm { e n e r g y ~ i n ~ a ~ v o l u m e ~ e l e m e n t ~ c o n t a i n i n g } } { \mathrm { a ~ f u x e d ~ n u m b e r } , ~ \mathcal { A } , ~ \mathrm { o f ~ b a r y o n s } } } = - p d ( \mathrm { v o l u m e } ) ~ + ~ T d ( \mathrm { e n t r o p y } ) ;
$$

$$
d ( \rho A / n ) = - p d ( A / n ) + T d ( A s ) ;
$$

i.e.,

$$
d \rho = \frac { \rho + p } { n } d n + n T d s .
$$

Query: what kind of a $" d "$ appears here? For a simple fluid, the values of two potentials, e.g., $\pmb { n }$ and $\pmb { S }$ ,fix all the others uniquely; so any change in $\rho$ must be determined uniquely by the changes in $\pmb { n }$ and ${ \pmb S } .$ . It matters not whether the changes are measured along the world line of a given fluid element, or in some other direction. Thus, the $" d "$ in the frst law can'be interpreted as an exterior derivative

$$
{ \pmb d } \rho = \frac { \rho + p } { n } { \pmb d } n + n T { \pmb d } s ;
$$

and the changes along a given direction in the fuid (along a given tangent vector $\pmb { \nu }$ ）can be written

$$
\begin{array} { c l } { \displaystyle \pmb { \nabla } _ { \pmb { v } } \rho \equiv \langle \pmb { d } \rho , \pmb { v } \rangle = \frac { \rho + p } { n } \langle \pmb { d } n , \pmb { v } \rangle + n T \langle \pmb { d } s , \pmb { v } \rangle } \\ { \displaystyle = \frac { \rho + p } { n } \pmb { \nabla } _ { \pmb { v } } n + n T \pmb { \nabla } _ { \pmb { v } } s . } \end{array}
$$

Pressure and temperature calculated from $\rho ( n , s )$

Equation (22.6) lends itself to interpretation in two opposite senses: as a way to deduce the density of mass-energy of the medium from information about pressure (as a function of $\pmb { n }$ and $s \mathrm { \ i }$ )and temperature (as a function of $\pmb { n }$ and s); and conversely, as a way to deduce the two functions $p ( n , s )$ and $T ( n , s )$ from the one function $\rho ( n , s )$ It is natural to look at the second approach first; who does not like a strategy that makes an intellectual profit? Regarding $\pmb { \rho }$ as a known (or calculable) function of $\pmb { n }$ and $s$ ,one deduces from (22.6)

$$
\begin{array} { c } { \displaystyle \frac { \rho + p } { n } = \left( \frac { \hat { \sigma } \rho } { \hat { \sigma } n } \right) _ { s } , } \\ { \displaystyle n T = \left( \frac { \hat { \sigma } \rho } { \hat { \sigma } s } \right) _ { n } , } \end{array}
$$

and thence pressure and temperature individually,

$$
\begin{array} { c } { { p ( n , s ) = n \left( \frac { \hat { \sigma } \rho } { \hat { \sigma } n } \right) _ { s } - \rho , } } \\ { { { } } } \\ { { T ( n , s ) = \displaystyle \frac { 1 } { n } \left( \frac { \hat { \sigma } \rho } { \hat { \sigma } s } \right) _ { n } } } \end{array}
$$

("two equations of state from one"). The analysis simplifies stil further when the fluid,already assumed to be everywhere of the same composition,is also everywhere endowed with the same entropy per baryon, s,and is in a state of adiabatic flow (no shocks or heat conduction). Then the density $\rho = \rho ( n , s )$ reduces to a function of one variable out of which one derives everything $( \pmb \rho , p , \mu )$ needed for the hydrodynamics and the gravitation physics of the system (next chapter). Other choices of the “primary thermodynamic potential” are appropriate under other circumstances (see Box 22.1).

If differentiation leads from $\rho ( n , s )$ to $p ( n , s )$ and $T ( n , s )$ ,it does not follow that one can take any two functions $p ( n , s )$ and $T ( n , s )$ and proceed “backwards" (by integration） to the“primary function”, $\rho ( n , s )$ . To be compatible with the first law of thermodynamics (22.6),the two functions must satisfy the consistency requirement ["Maxwell relation”; equality of second partial derivatives of $\pmb { \rho } ]$

$$
( \hat { \sigma } p / \hat { \sigma } s ) _ { n } = n ^ { 2 } ( \hat { \sigma } T / \hat { \sigma } n ) _ { s } .
$$

# Box 22.1 PRINCIPAL ALTERNATIVES FOR "PRIMARY THERMODYNAMIC POTENTIAL" TO DESCRIBE A FLUID

Primary thermodynamic potential and quantities on which it is most appropriately envisaged to depend

“Secondary” thermodynamic quantities obtained by differentiation of primary with or without use of

Conditions under which convenient, appropriate,and relevant

$$
d \bigg ( \frac { \rho } { n } \bigg ) + p d \bigg ( \frac { 1 } { n } \bigg ) - T d s = 0
$$

"Density"; total amount of masenergy (rest $^ +$ thermal $+ \cdot \cdot \cdot )$ per unit volume

$$
\rho = \rho ( n , s )
$$

$$
{ \begin{array} { l } { p ( n , s ) \equiv n { \Big ( } { \frac { \partial \rho } { \partial n } } { \Big ) } _ { s } - \rho } \\ { T ( n , s ) = { \frac { 1 } { n } } { \Big ( } { \frac { \partial \rho } { \partial s } } { \Big ) } _ { n } } \\ { \mu ( n , s ) = { \frac { p + \rho } { n } } = { \Big ( } { \frac { \partial \rho } { \partial n } } { \Big ) } _ { s } } \end{array} }
$$

Conditions of adiabatic flow (no shocks or heat conduction),so'that $\pmb { \mathscr { s } }$ stays constant along streamline

"Physical free energy"

$$
a ( n , T ) = { \frac { \rho } { n } } - T s
$$

$$
\begin{array} { l } { { \displaystyle p ( n , T ) = n ^ { 2 } \bigg ( \frac { \partial a } { \partial n } \bigg ) _ { T } } } \\ { { \displaystyle s ( n , T ) = - \bigg ( \frac { \partial a } { \partial T } \bigg ) _ { n } } } \\ { { \displaystyle \rho ( n , T ) = - n T ^ { 2 } \bigg [ \frac { \partial ( a / T ) } { \partial T } \bigg ] _ { n } } } \end{array}
$$

Know or can calculate a (or the “sum over states”of statistical mechanics) for conditions of specified volume per baryon and temperature "Chemical free energy”

$$
f ( p , T ) = { \frac { \rho + p } { n } } - T s
$$

Relevant for determining equilibrium when pressure and temperature are specified

“Chemical potential"("energy to inject”expressed on a“per baryon" basis)

$$
\mu ( p , s ) = { \frac { p + \rho } { n } } 
$$

$$
\rho ( p , s ) = { \frac { \mu } { ( \partial \mu / \hat { \sigma } p ) _ { s } } } - p
$$

When injection energy $\{ =$ Fermi energy for an ideal Fermi gas,relativistic or not; see exercise 22.3j is the center of attention

Chemical potential equals "injection energy"at fixed entropy per baryon and total volume

The chemical potential $\mu$ is also a unique function of $\pmb { n }$ and s. It is defined as follows. (l) Take a sample of the simple fluid in a fixed thermodynamic state (fixed $\pmb { n }$ and $s ^ { \cdot }$ ).(2)Take, separately,a much smaller sample of the same fluid, containing $\delta A$ baryons in the same thermodynamic state as the large sample (same $\pmb { n }$ and s). (3) Inject the smaller sample into the larger one, holding the volume of the large sample fixed during the injection process. (4) The total mass-energy injected,

$$
\delta M _ { \mathrm { i n j e c t e d } } = \rho \times ( \mathrm { v o l u m e ~ o f ~ i n j e c t e d ~ f l u i d } ) = \rho ( \delta A / n ) ,
$$

plus the work required to perform the injection

$$
\begin{array} { r } { \delta W _ { \mathrm { i n j e c t i o n } } = \Big ( \mathrm { w o r k ~ d o n e ~ \mathsf { a g a i n s t } ~ p r e s s u r e ~ o f ~ l a r g e ~ s a m p l e } \Big ) } \\ { \mathsf { \ t i o ~ o p e n ~ \mathsf { u p ~ s p a c e ~ i n ~ i t ~ f o r ~ t h e ~ i n j e c t e d ~ f l u i d } } } \\ { = p ( \mathrm { v o l u m e ~ o f ~ i n j e c t e d ~ f l u i d } ) = p ( \delta A / n ) , \qquad } \end{array}
$$

is equal to $\mu \delta A$ ：

$$
\mu \delta A = \delta M _ { \mathrm { i n j e c t e d } } + \delta W _ { \mathrm { i n j e c t i o n } } = \frac { \rho + p } { n } \delta A .
$$

Stated more briefly:“

$$
\begin{array} { r l } & { \mu = \left( \begin{array} { l } { \mathrm { t o t a l ~ m a s s - e n e r g y ~ r e q u i r e d , ~ p e r ~ b a r y o n , ~ t o ~ \hat { \mu } ^ { * } c r e a t e ' s ~ a n d } } \\ { \mathrm { i n j e c t ~ a ~ s m a l l ~ a d d i t i o n a l ~ a m o u n t ~ o f ~ f u i d ~ i n i d ~ i n t o ~ a ~ g i v e n } } \\ { \mathrm { s a m p l e , ~ w i t h o u t ~ c h a n g i n g ~ \hat { \mu } s ~ o r ~ v o l u m e ~ o f ~ t h e ~ s a m p l e } } \end{array} \right) } \\ & { \quad = \frac { \rho + p } { n } = \left( \frac { \hat { \sigma } \rho } { \hat { \sigma } n } \right) _ { s } . } \\ & { \qquad \quad \begin{array} { r } { \mathrm { L } _ { [ b y ~ f i r s t ~ l a w ~ o f ~ t h e r m o d y n a m i c s ~ ( 2 2 . 6 ) ] } } \end{array} } \end{array}
$$

All the above laws and equations of thermodynamics are the same in curved spacetime as in flat spacetime; and the same in (relativistic) flat spacetime as in classical nonrelativistic thermodynamics-except for the inclusion of rest mass, together with all other forms of mass-energy,in $\pmb { \rho }$ and $\mu$ .The reason is simple: the laws are all formulated as scalar equations linking thermodynamic variables that one measures in the rest frame of the fluid.

# $\$ 22.3$ . HYDRODYNAMICS IN CURVED SPACETIME\*

Laws of hydrodynamics for simple fluid without heat flow or viscosity:

A simple perfect fluid flows through spacetime.It might be the Earth's atmosphere circulating in the Earth's gravitational field. It might be the gaseous interior of the Sun at rest in its own gravitational feld. It might be interstellar gas accreting onto a black hole.But whatever and wherever the fluid may be, its motion will be governed by the curved-spacetime laws of thermodynamics $( \ S 2 2 . 2 )$ plus the local

(1） Origins of laws

law of energy-momentum conservation, ${ \pmb { \nabla } } \cdot { \pmb { \vec { r } } } = 0$ .The chief objective of this section is to reduce the equation $\pmb { \bigtriangledown } \cdot \pmb { \cal T } = 0$ to usable form. The reduction will be performed in the text using abstract notation; the reader is encouraged to repeat the reduction using index notation.

The stress-energy tensor for a perfect fluid,in curved spacetime as in flat (equivalence principle!), is

$$
\pmb { \tau } = ( \rho + p ) \pmb { \mu } \otimes \pmb { \mu } + p \pmb { g } .
$$

(See $\ S 5 . 5 . )$ Its divergence is readily calculated using the chain rule; using the “com-patibility relation between $\pmb { \mathscr { g } }$ and $\because \pmb { \nabla } \pmb { g } = 0$ ； using the identity $( { \pmb { \nabla } } p ) \cdot { \pmb { g } } = { \pmb { \nabla } } p$ (which one readily verifies in index notation); and using

$$
\begin{array} { r l r } {  { 0 = \nabla \cdot \pmb { T } = [ \nabla ( \rho + p ) \cdot \pmb { u } ] \pmb { u } + [ ( \rho + p ) \nabla \cdot \pmb { u } ] \pmb { u } + [ ( \rho + p ) \pmb { u } ] \cdot \pmb { \nabla } \pmb { u } + ( \pmb { \nabla } p ) \cdot \pmb { g } } } \\ & { \overset { \mathrm { . } } { \mathrm { L } } _ { [ \mathrm { d i v e r g e n c e ~ o n ~ f i r s t ~ s l o t } ] } } \\ & { = [ \pmb { \nabla } _ { \pmb { u } } \rho + \pmb { \nabla } _ { \pmb { u } } p + ( \rho + p ) \pmb { \nabla } \cdot \pmb { u } ] \pmb { u } + ( \rho + p ) \pmb { \nabla } _ { \pmb { u } } \pmb { u } + \pmb { \nabla } p . } & { ( 2 2 . 1 6 \pmb { \nabla } \pmb { u } ) } \end{array}
$$

The component of this equation along the 4-velocity is especially simple (recall that $\begin{array} { r } { \pmb { u } \cdot \pmb { \nabla _ { u } } \pmb { u } = \frac { 1 } { 2 } \pmb { \nabla _ { u } } \pmb { u } ^ { 2 } = 0 } \end{array}$ because $\pmb { u } ^ { 2 } \equiv - 1$ ）：

$$
\begin{array} { r l } & { 0 = u \cdot ( \pmb { \nabla } \cdot \pmb { T } ) = - [ \pmb { \nabla } _ { u } \rho + \pmb { \nabla } _ { u } p + ( \rho + p ) \pmb { \nabla } \cdot \pmb { u } ] + \pmb { \nabla } _ { u } p } \\ & { \quad = - \pmb { \nabla } _ { u } \rho - ( \rho + p ) \pmb { \nabla } \cdot \pmb { u } . } \end{array}
$$

Combine this with the equation of baryon conservation (22.3); the result is

$$
- \quad - \qquad { \frac { d \rho } { d \tau } } = { \frac { ( \rho + p ) } { n } } { \frac { d n } { d \tau } } .
$$

(2) Local energy   
conservation:adiabaticity of   
flow

Notice that this is identical to the first law of thermodynamics (22.6) applied along a fow line, plus the assumption that the entropy per baryon is conserved along a flow line

$$
d s / d \tau = 0 .
$$

There is no reason for surprise at this result.To insist on thermodynamic equilibrium and to demand that the entropy remain constant is to require zero exchange of heat between one element of the fluid and another. But the stress-energy tensor (22.9) recognizes that heat exchange is absent. Any heat exchange would show up as an energy flux term in $\pmb { \tau } ( \mathbf { E x } . 2 2 . 7 )$ ； but no such term is present. Consequently, when one studies local energy conservation by evaluating ${ \pmb u } \cdot \hat { ( } \dot { \pmb { v } } \cdot \pmb { r } ) = 0$ ,the stress-energy tensor reports that no heat flow is occurring--i.e. that $d s / d \tau = 0$

Three components of ${ \pmb { \bigtriangledown } } \cdot { \pmb { \cal T } } = 0$ remain: the components orthogonal to the fluid's 4-velocity. One can pluck them out of ${ \pmb { \bigtriangledown } } \cdot { \pmb { \cal T } } = 0$ ,leaving behind the component along $\pmb { u }$ ,by use of the “projection tensor”

$$
{ \pmb { P } } \equiv { \pmb { g } } + { \pmb { u } } \otimes { \pmb { u } } .
$$

# A.Ten Quantities Characterize the Fluid

Thermodynamic potentials all measured in rest frame

$_ { n }$ ,baryon number density   
$\pmb { \rho }$ ,density of total mass-energy   
$\boldsymbol { p }$ pressure   
$T ,$ temperature   
$s ,$ ,entropy per baryon   
$\mu$ ,chemical potential per baryon

Four components of the fuid 4-velocity

# B. Ten Equations Govern the Fluid's Motion

Two equations of state

$$
p = p ( n , s ) , \quad \quad T = T ( n , s )
$$

subject to the compatibility constraint ("Maxwell relation,”which follows from first law of thermodynamics)

$$
( \hat { \sigma } p / \hat { \sigma } s ) _ { n } = n ^ { 2 } ( \hat { \sigma } T / \hat { \sigma } n ) _ { s } .
$$

First law of thermodynamics

$$
{ \pmb d } \rho = \frac { \rho + p } { n } { \pmb d } n + n T { \pmb d } s ,
$$

which can be integrated to give $\rho ( n , s )$

Equation for chemical potential

$$
\begin{array} { r } { \mu = ( \rho + p ) / n , } \end{array}
$$

which can be combined with $\rho ( n , s )$ and $p ( n , s )$ to give $\mu ( n , s )$

Law of baryon conseruation

$$
d n / d \tau \equiv \pmb { \nabla } _ { \pmb { u } } n = - n \ \pmb { \nabla } \cdot \pmb { u } .
$$

Conservation of energy along flow lines, which (assuming no energy exchange between adjacent fluid elements) means “adiabatic flow”

[Shock waves are not treated in this book; see Taub (l948),de Hoffman and Teller (1950), Israel (1960), May and White (1967), Zel'dovich and Rayzer(l967)； Lichnerowicz (1967,1971); and Thorne (1973a).]

Euler equations

$$
\left( \rho + p \right) \nabla _ { u } u = - ( { \pmb g } + { \pmb u } \otimes { \pmb u } ) \cdot \nabla p ,
$$

which determine the flow lines to which $\pmb { u }$ is tangent.

Normalization of 4-velocity

$$
{ \pmb u } \cdot { \pmb u } = - 1 .
$$

(See exercise 22.4.) Contracting $\pmb { P }$ with $\pmb { \bigtriangledown } \cdot \pmb { \cal T } = 0$ [equation (22.10)] gives

(3) Euler equation

$$
\left( \rho + p \right) \nabla _ { u } u = - P \cdot \left( \nabla p \right) \equiv - [ \nabla p + ( \nabla _ { u } p ) u ] .
$$

This is the “Euler equation”of relativistic hydrodynamics.It has precisely the same form as the corresponding flat-spacetime Euler equation:

$$
{ \begin{array} { r l } & { { \left( \begin{array} { l } { { \mathrm { i n e r t i a l ~ m a s s } } } \\ { { \mathrm { p e r ~ u n i t ~ v o l u m e } } } \\ { [ { \mathrm { e x e r c i s e ~ } } 5 . 4 ] } \end{array} \right) } \times { \left( \begin{array} { l } { 4 { \mathrm { - a c c e l e r a t i o n } } } \\ { { \mathrm { o f ~ f l u i d } } } \end{array} \right) } = - { \left( \begin{array} { l } { { \mathrm { p r e s s u r e ~ g r a d i e n t } } } \\ { { \mathrm { i n ~ t h e ~ } } 3 { \mathrm { - s u r f a c e } } } \\ { { \mathrm { o r t h o g o n a l ~ t o ~ } } 4 { \mathrm { - v e l o c i t y } } } \end{array} \right) } . } \end{array} }
$$

The pressure gradient, not “gravity,” is responsible for all deviation of fow lines from geodesics.

Box 22.2 reorganizes and summarizes the above laws of thermodynamics and hydrodynamics.

# Exercise 22.1. DIVERGENCE OF FLOW LINES PRODUCES VOLUME CHANGES

Derive the equation $d V / d \tau = ( \pmb { \nabla } \cdot \pmb { u } ) V$ [equation (22.2)] for the rate of change of volume of a fluid element. [Hint: Pick an event $\varphi _ { \mathfrak { d } } ^ { }$ and calculate in a local Lorentz frame at $\scriptstyle { \mathcal { P } } _ { 0 }$ which momentarily moves with the fluid ("rest frame at ${ \vec { \pmb { \mathscr { P } } } } _ { 0 } ^ { \pmb { \mathscr { P } } } .$ .] [Solution: At events near $\pmb { \mathcal { P } _ { 0 } }$ the fluid has a very small ordinary velocity $v ^ { j } = d x ^ { j } / d t$ .Consequently a cube of fluid at ${ \pmb \mathcal { P } } _ { \bf 0 }$ with edges $\Delta x = \Delta y = \Delta z = L$ changes its edges,after time $\delta t .$ ,by the amounts

$$
\begin{array} { r l } & { \delta ( \varDelta x ) = [ ( d x / d t ) \delta t ] _ { \mathrm { a t } ^ { * } \mathrm { t r o n t f a c e } ^ { * } } - [ ( d x / d t ) \delta t ] _ { \mathrm { a t } ^ { * } \mathrm { b a c k } \mathrm { t a c e } ^ { * } } } \\ & { \qquad = ( \partial v ^ { x } / \partial x ) L \delta t , } \\ & { \delta ( \varDelta y ) = ( \partial v ^ { y } / \partial y ) L \delta t , } \\ & { \delta ( \varDelta z ) = ( \partial v ^ { z } / \partial z ) L \delta t . } \end{array}
$$

The corresponding change in volume is

$$
\delta ( \varDelta x \varDelta y \varDelta z ) = ( \partial v ^ { j } / \partial x ^ { j } ) L ^ { 3 } \delta t ;
$$

so the rate of change of volume is

$$
\partial V / \partial t = V ( \partial v ^ { j } / \partial x ^ { j } ) .
$$

But in the local Lorentz rest frame at and near ${ \pmb \mathcal { S } } _ { \bf 0 }$ (where $x ^ { \alpha } = 0$ ），the metric coefficientsare $g _ { \mu \nu } = \eta _ { \mu \nu } + 0 ( | x ^ { \alpha } | ^ { 2 } ) ~$ ,and the ordinary velocity is $v ^ { j } = 0 ( | x ^ { \alpha } | )$ ； so

$$
\begin{array} { c } { { u ^ { 0 } = \displaystyle \frac { d t } { d \tau } = \displaystyle \frac { d t } { ( - g _ { \mu \nu } d x ^ { \mu } d x ^ { \nu } ) ^ { 1 / 2 } } = \mathrm { 1 } + 0 ( | x ^ { \alpha } | ^ { 2 } ) , } } \\ { { u ^ { j } = \displaystyle \frac { d x ^ { j } } { d \tau } = v ^ { j } + 0 ( | x ^ { \alpha } | ^ { 3 } ) . } } \end{array}
$$

Thus, the derivatives $\partial V / \partial t$ and $V ( \partial v ^ { j } / \partial x ^ { j } )$ at $\scriptstyle { \mathcal { P } } _ { 0 }$ are

$$
\begin{array} { r l } & { \partial V / \partial t = u ^ { \alpha } \partial V / \partial x ^ { \alpha } = u ^ { \alpha } V _ { , \alpha } = d V / d \tau } \\ & { \qquad = V ( \partial v ^ { j } / \partial x ^ { j } ) = V ( \partial u ^ { \alpha } / \partial x ^ { \alpha } ) = V { u ^ { \alpha } } _ { ; \alpha } = V ( \pmb { \nabla } \pmb { \cdot } \pmb { u } ) . } \end{array}
$$

[Note that by working in flat spacetime, one could have inferred more easily that $\partial V / \partial t =$ $d V / d \tau$ and $\partial v ^ { j } / \partial x ^ { j } = \mathbf { \nabla \mathbf { \nabla } \cdot } \pmb { u }$ ；one would then have concluded $d V / d \tau = ( \pmb { \nabla } \cdot \pmb { u } ) V$ and one could have invoked the equivalence principle to move this law into curved spacetime.]

# Exercise 22.2. EQUATION OF CONTINUITY

Show that in the nonrelativistic limit in flat spacetime the equation of baryon conservation (22.3) becomes the “equation of continuity”

$$
\frac { \partial n } { \partial t } + \frac { \partial } { \partial x ^ { j } } ( n v ^ { j } ) = 0 .
$$

# Exercise 22.3. CHEMICAL POTENTIAL FOR IDEAL FERMI GAS

Show that the chemical potential of an ideal Fermi gas, nonrelativistic or relativistic,is (at zero temperature) equal to the Fermi energy (energy of highest occupied momentum state) of that gas.

# Exercise 22.4. PROJECTION TENSORS

Show that contraction of a tangent vector $\pmb { B }$ with the “projection tensor” $\pmb { P } \equiv \pmb { g } + \pmb { u } \otimes \pmb { u }$ projects $\pmb { B }$ into the 3-surface orthogonal to the 4-velocity vector $\pmb { u }$ [Hint: perform the calculation in an orthonormal frame with $\pmb { e } _ { \hat { \imath } } = \pmb { \mu }$ and write $\pmb { { \cal B } } = { \cal B } ^ { \alpha } \pmb { e } _ { \alpha }$ ：then show that ${ \pmb P } \cdot { \pmb B } = B ^ { \dagger } { \pmb e } _ { \hat { \jmath } } . ]$ If $\pmb { n }$ is a unit spacelike vector, show that ${ \pmb { P } } \equiv { \pmb { g } } - { \pmb { n } } \otimes { \pmb { i } }$ n is the corresponding projection operator. Note: There is no unique concept of “the projection orthogonal to a null vector."Why? [Hint: draw pictures in flat spacetime suppressing one spatial dimension.]

# ExerciSe 22.5. PRESSURE GRADIENT IN STATIONARY GRAVITATIONAL FIELD

A perfect fuid is at rest (flow lines have $x ^ { j } =$ constant） in a stationary gravitational field (metric coefficients are independent of $x ^ { 0 }$ ). Show that the pressure gradient required to “support the fluid against gravity” (i.e., to make its flow lines be $x ^ { j } =$ constant instead of geodesics) is

$$
\frac { \partial p } { \partial x ^ { 0 } } = 0 , \frac { \partial p } { \partial x ^ { j } } = - ( \rho + p ) \frac { \partial \ln \sqrt { - g _ { 0 0 } } } { \partial x ^ { j } } .
$$

Evaluate this pressure gradient in the Newtonian limit, using the coordinate system and metric coeficients of equation (18.15c).

# Exercise 22.6. EXPANSION，ROTATION，AND SHEAR

Let a field of fluid 4-velocities ${ \pmb u } ( { \pmb \mathcal { G } } )$ be given.

(a) Show that $\yen 4$ can be decomposed in the following manner:

$$
u _ { \alpha ; \beta } = \omega _ { \alpha \beta } + \sigma _ { \alpha \beta } + \frac { 1 } { 3 } \theta P _ { \alpha \beta } - a _ { \alpha } u _ { \beta } ,
$$

where a is the ${ \pmb { 4 } } .$ acceleration of the fluid

$$
a _ { \alpha } \equiv u _ { \alpha ; \beta } u ^ { \beta } ,
$$

$\pmb \theta$ is the “expansion”of the fuid world lines

$$
\begin{array} { r } { \pmb { \theta } \equiv \pmb { \nabla } { \cdot } \pmb { u } = \pmb { u } ^ { \alpha } { } _ { ; \alpha } , } \end{array}
$$

$P _ { \alpha \beta }$ is the projection tensor

$$
P _ { \alpha \beta } \equiv g _ { \alpha \beta } + u _ { \alpha } u _ { \beta } ,
$$

$\sigma _ { \alpha \beta }$ is the shear tensor of the fluid

$$
\sigma _ { \alpha \beta } \equiv \frac { 1 } { 2 } ( u _ { \alpha ; \mu } { P ^ { \mu } } _ { \beta } + u _ { \beta ; \mu } { P ^ { \mu } } _ { \alpha } ) - \frac { 1 } { 3 } \theta P _ { \alpha \beta } ,
$$

and $\omega _ { \alpha \beta }$ is the rotation 2-form of the fuid

$$
\omega _ { \alpha \beta } \equiv \frac { 1 } { 2 } ( u _ { \alpha ; \mu } { P ^ { \mu } } _ { \beta } - u _ { \beta ; \mu } { P ^ { \mu } } _ { \alpha } ) .
$$

(b) Each of the component parts of this decomposition has a simple physical interpretation in the local rest frames of the fluid.The interpretation of the 4-acceleration $\pmb { a }$ in terms of accelerometer readings should be familiar. Exercise 22.l showed that the expansion $\pmb { \theta } = \pmb { \nabla } \cdot \pmb { u }$ describes the rate of increase of the volume of a fuid element,

$$
\theta = ( 1 / V ) ( d V / d \tau ) .
$$

Exercise 22.4 explored the meaning and use of the projection tensor $\pmb { P } .$ Verify that in a local Lorentz frame $\dot { ( } g _ { \hat { \alpha } \beta } = \eta _ { \alpha \beta } , \Gamma ^ { \hat { \alpha } } { } _ { \beta \hat { \gamma } } \stackrel { \smile } { = } 0 )$ momentarily moving with the fluid $\dot { ( u ^ { \alpha } } = \delta ^ { \alpha } { } _ { 0 } )$ ， $\sigma _ { \hat { \alpha } \beta }$ and $\omega _ { \hat { \alpha } \hat { \beta } }$ reduce to the classical (nonrelativistic) shear and rotation of the fluid.[See, e.g, $\ S 8 2 . 4$ and 2.5of Ellis (197l） for both classical and relativistic descriptions of shear and rotation.]

# Exercise 22.7. HYDRODYNAMICS WITH VISCOSITY AND HEAT FLOW.\*

(a)In $\ S 1 S$ of Landau and Lifshitz (l959),one finds an analysis of viscous stresses for'a classical (nonrelativistic) fluid.By carrying that analysis over directly to the local Lorentz rest frame of a relativistic fluid, and by then generalizing to frame-independent language, show that the contribution of viscosity to the stress-energy tensor is

$$
\begin{array} { r } { \pmb { T } ^ { \mathrm { ( v i s c ) } } = - 2 \eta \pmb { \sigma } - \zeta \pmb { \theta } \pmb { P } , } \end{array}
$$

where $\eta \geq 0$ is the“coefficientofdynamic viscosity"; $\zeta \geq 0$ is the“coefficient ofbulk viscosity";   
and $\sigma , \theta , P$ are the shear, expansion,and projection tensor of the fluid.

(b) An idealized description of heat flow in a fluid introduces the heat-flux 4-vector q with components in the local rest-frame of the fluid,

$$
q _ { \cdot } ^ { \widehat { \boldsymbol { \mathfrak { \mathfrak { \varphi } } } } } = 0 , \qquad q ^ { \widehat { \boldsymbol { \mathfrak { \mathfrak { j } } } } } = \left( \operatorname * { e n e r g y } _ { \mathrm { s u r f a c e \ p e r \ u n i t \ t i m e \ c r o s s i n g \ u n i t } } \right) .
$$

By generalizing from the fluid rest frame to frame-independent language,show that the contribution of heat flux to the stress-energy tensor is

$$
\pmb { T } ^ { ( \mathrm { b e a t } ) } = \pmb { u } \otimes \pmb { q } + \pmb { q } \otimes \pmb { u } .
$$

Thereby conclude that, in this idealized picture,the stress-energy tensor for a viscous fluid with heat conduction is

$$
T ^ { \alpha \beta } = \rho u ^ { \alpha } u ^ { \beta } + ( p - \xi \theta ) { \cal P } ^ { \alpha \beta } - 2 \eta \sigma ^ { \alpha \beta } + q ^ { \alpha } u ^ { \beta } + u ^ { \alpha } q ^ { \beta } .
$$

(c) Define the entropy 4-vector $\pmb { s }$ by

$$
{ \pmb s } \equiv n s { \pmb u } + { \pmb q } / T .
$$

By calculations in the local rest-frame of the fluid, show that

$$
\begin{array} { r l } & { { \pmb \nabla } \cdot { \pmb s } = \left( \mathrm { \mathop { r a t e ~ o f ~ i n c r e a s e ~ o f ~ e n t r o p y } } \right) - \left( \mathrm { r a t e ~ a t ~ w h i c h ~ h e a t ~ a n d ~ f u i d } \right. } \\ & { \left. \qquad \mathrm { ( c a r r y ~ e n t r o ~ a ~ u n i t ~ v o l u m e ) } \right. } \\ & { \qquad = \left( \mathrm { r a t e ~ a t ~ w h i c h ~ e n t r o p y ~ i s ~ b e i n g } \right) . } \\ & { \qquad \left. ( 2 \mathrm { e n e r a t e d ~ i n ~ a ~ u n i t ~ v o l u m e } \right. } \end{array}
$$

Thereby arrive at the following form of the second law of thermodynamics:

$$
{ \pmb { \nabla } } \cdot { \pmb { s } } \geq 0 .
$$

(d) Calculate the law of local energy conservation, $\pmb { \mu } \cdot \pmb { \nabla } \pmb { \cdot } \pmb { \tau } = 0$ ,for a viscous fluid with heat flow. Combine with the first law of thermodynamics and with the law of baryon conservation to obtain

$$
T \Psi \cdot s = \xi \theta ^ { 2 } + 2 \eta \sigma _ { \alpha \beta } \sigma ^ { \alpha \beta } - q ^ { \alpha } ( T _ { , \alpha } / T + a _ { \alpha } ) .
$$

Interpret each term of this equation as a contribution to entropy generation (example: $2 \eta \sigma _ { \alpha \beta } \sigma ^ { \alpha \beta }$ describes entropy generation by viscous heating). [Note: The term $q ^ { \alpha } a _ { \alpha }$ is relativistic in origin.It is associated with the inertia of the flowing heat.]

(e) When one takes account of the inertia of the flowing heat, one obtains the following generalization of the classical law of heat conduction:

$$
q ^ { \alpha } = - \kappa P ^ { \alpha \beta } ( T _ { , \beta } + T a _ { \beta } )
$$

(Eckart 1940). Here $\kappa$ is the coefficient of thermal conductivity. Use this equation to show that,for a fuid at rest in a-stationary gravitational field (Exercise 22.5),

$$
q _ { 0 } = 0 , \qquad q _ { j } = - \frac { \kappa } { \sqrt { - g _ { 0 0 } } } ( T \sqrt { - g _ { 0 0 } } ) _ { , j } .
$$

[Thus,thermal equilibrium corresponds not to constant temperature,but to the redshifted temperature distribution ${ \cal T } \sqrt { - g _ { 0 0 } } =$ constant; Tolman (1934a), p.313.] Also,use the idealized law of heat conduction (22.16i) to reexpress the rate of entropy generation as

$$
\begin{array} { r l } & { T \mathbf { \nabla } \cdot \mathbf { s } = \xi \theta ^ { 2 } + 2 \eta \sigma _ { \alpha \beta } \sigma ^ { \alpha \beta } + ( \kappa / T ) P ^ { \alpha \beta } ( T _ { , \alpha } + T a _ { \alpha } ) ( T _ { , \beta } + T a _ { \beta } ) } \\ & { \quad \quad \geq 0 . } \end{array}
$$

[For further details about heat flow and for discussions of the limitations of the above idealized description,see e.g., $\ S 4 . 1 8$ of Ehlers (1971)； also Marle (1969),Anderson (1970), Stewart (197l),and papers cited therein.]

Electric and magnetic fields

# \$22.4. ELECTRODYNAMICS IN CURVED SPACETIME

In a local Lorentz frame in the presence of gravity, an observer can measure the electric and magnetic fields $\pmb { \cal E }$ and $\pmb { B }$ using the usual Lorentz force law for charged particles. As in special relativity, he can regard $\pmb { \cal E }$ and $\pmb { B }$ as components of an electromagnetic field tensor,

$$
F ^ { \hat { 0 } \hat { \dagger } } = - F ^ { \hat { j } \hat { 0 } } = E ^ { \hat { j } } , \qquad F ^ { \hat { j } \hat { k } } = \epsilon ^ { \hat { j } \hat { k } \hat { l } } B ^ { \hat { l } } ; \cdots
$$

he can regard the charge and current densities as components of a 4-vector $J ^ { \hat { \alpha } }$ and he can write Maxwell's equations and the Lorentz force equation in the special relativistic form,

$$
F ^ { \hat { \alpha } \hat { \beta } } { } _ { , \hat { \beta } } = 4 \pi J ^ { \hat { \alpha } } , \qquad F _ { \hat { \alpha } \hat { \beta } , \hat { \gamma } } + F _ { \hat { \beta } \hat { \gamma } , \hat { \alpha } } + F _ { \hat { \gamma } \hat { \alpha } , \hat { \beta } } = 0 ,
$$

$$
m a ^ { \hat { \alpha } } \doteq F ^ { \hat { \alpha } \hat { \beta } } q u _ { \hat { \beta } } \qquad \left( { m = { \mathrm { m a s s ~ o f ~ p a r t i c l e } } , q = { \mathrm { c h a r g e } } , \atop { u ^ { \hat { \alpha } } = 4 \mathrm { - v e l o c i t y } , a ^ { \hat { \alpha } } = 4 \mathrm { - a c c e l e r a t i o n } } } \right) .
$$

Maxwell equations and Lorentz force law

In any other frame these equations will have the same form, but with commas replaced by semicolons

$$
\begin{array} { c } { { F ^ { \alpha \beta } { } _ { ; \beta } = 4 \pi J ^ { \alpha } , } } \\ { { { } } } \\ { { F _ { \alpha \beta ; \gamma } + F _ { \beta \gamma ; \alpha } + F _ { \gamma \alpha ; \beta } = 0 , } } \\ { { { } } } \\ { { m a ^ { \alpha } = F ^ { \alpha \beta } q \dot { u } _ { \beta } . } } \end{array}
$$

These are the basic equations of electrodynamics in the presence of gravity. From them follws everything else. For example,as in special relativity, so also here (exercise 22.9), they imply the equation of charge conservation

$$
J ^ { \alpha } { } _ { ; \alpha } = 0 ;
$$

and for an electromagnetic field interacting with charged matter (exercise 22.10) they imply vanishing divergence for the sum of the stress-energy tensors

$$
( T ^ { ( \mathrm { E M } ) \alpha \beta } + T ^ { ( \mathrm { M A T T E R } ) \alpha \beta } ) _ { ; \beta } = 0 .
$$

Local conservation of energy-momentum

As in special relativity, so also here, one can introduce a vector potential $A ^ { \mu }$ Replacing commas by semicolons in the usual special-relativistic expression for $F ^ { \mu \nu }$ in terms of $A ^ { \mu }$ ，one obtains

Vector potential

$$
F _ { \mu \nu } = A _ { \nu ; \mu } - A _ { \mu ; \nu } .
$$

If allis well, this equation should guarantee (as in special relativity) that the Maxwell equations (22.17b) are satisfied.Indeed, it does,as one sees in exercise 22.8.To derive the wave equation that governs the vector potential, insert expression (22.l9a) into the remaining Maxwell equations (22.17a), obtaining

$$
- { A ^ { \alpha ; \beta } } _ { \beta } + { A ^ { \beta ; \alpha } } _ { \beta } = 4 \pi J ^ { \alpha } ;
$$

then commute covariant derivatives in the first term using the identity (l6.6c), to obtain

$$
- { A ^ { \alpha ; \mu } } _ { \mu } + { A ^ { \mu } } _ { ; \mu } { } ^ { ; \alpha } + { R ^ { \alpha } } _ { \mu } A ^ { \mu } = 4 \pi J ^ { \alpha } .
$$

Finally, adopting the standard approach of special relativity, impose the Lorentz gauge condition

$$
{ A ^ { \mu } } _ { ; \mu } = 0 ,
$$

Lorentz gauge condition

thereby bringing the wave equation (2.19b) into the form

$$
( { \cal { A } } _ { d R } { \cal { A } } ) ^ { \alpha } \equiv - { \cal { A } } ^ { \alpha ; \beta } { } _ { \beta } + R ^ { \alpha } { } _ { \beta } { \cal { A } } ^ { \beta } = 4 \pi J ^ { \alpha } .
$$

Wave equation for vector potential

The “de Rham vector wave operator” A which appears here is, apart from sign, a generalized d'Alambertian for vectors in curved spacetime.Mathematically it is more powerful han $- A ^ { \alpha ; \beta } { } _ { ; \beta }$ andthananyotheroperatorthatreducesto(minus) the d'Alambertian in special relativity.[For a discussion, see de Rham (1955).]

Although the electrodynamic equations (22.17a)-(22.19b) are all obtained from special relativity by the comma-goes-to-semicolon rule, the wave equation (22.19d) for the vector potential is not ("curvature coupling"; see Box l6.1). Nevertheless, .when spacetime is flat (so $R ^ { \alpha } { } _ { \beta } = 0 \rangle$ ,(22.19d) does reduce to the usual wave equation of special relativity.

# Exercise 22.8. THE VECTOR POTENTIAL FOR ELECTRODYNAMICS

Show that in any coordinate frame the connection coefficients cancel out of both equations (22.19a) and (22.17b),so they can be written

$$
F _ { \alpha \beta , \gamma } + F _ { \beta \gamma , \alpha } + F _ { \gamma \alpha , \beta } = 0 .
$$

$$
F _ { \mu \nu } = A _ { \nu , \mu } - A _ { \mu , \nu } ,
$$

# EXERCISES

(ln the language of differential forms these equations are ${ \pmb F } = \pmb { d A }$ ， $\begin{array} { r } { \pmb { d } \pmb { F } = 0 . } \end{array}$ ）Then use this form of the equations to show that equation (2.19a) implies equation (22.17b), as asserted in the text.

# ExerciSe 22.9. CHARGE CONSERVATION·IN THE PRESENCE OF GRAVITY

Show that Maxwel's equations (22.17a,b) imply the equation of charge conservation (22.18a) when gravity is present, just as they do in special relativity theory.[Hints: Use the antisymmetry of $F ^ { \alpha \beta }$ ； and beware of the noncommutation of the covariant derivatives, which must be handled using equations (16.6). Alternatively,show that in coordinate frames,equation (22.17a) can be written as

$$
\frac { 1 } { \sqrt { | g | } } \frac { \partial } { \partial x ^ { \beta } } ( \sqrt { | g | } F ^ { \alpha \beta } ) = 4 \pi J ^ { \alpha }
$$

and (22.18a) as

$$
{ J ^ { \alpha } } _ { ; \alpha } \equiv \frac { 1 } { \sqrt { | g | } } \frac { \partial } { \partial x ^ { \alpha } } \left( \sqrt { | g | } J ^ { \alpha } \right) = 0 ,
$$

and carry out the demonstration in a coordinate frame.]

# ExerCise 22.1O. INTERACTING ELECTROMAGNETIC FIELDAND CHARGED MATTER

As in special relativity， so also in the presence of gravity (equivalence principle"),the stress-energy tensor for an electromagnetic field is

$$
T ^ { \mathrm { ( E M ) } } { } _ { \alpha \beta } = \frac { 1 } { 4 \pi } \bigg ( F _ { \alpha \mu } F _ { \beta } { } ^ { \mu } - \frac { 1 } { 4 } F _ { \mu \nu } F ^ { \mu \nu } g _ { \alpha \beta } \bigg ) .
$$

Use Maxwell's equations (22.17a,b) in the presence of gravity to show that

$$
T ^ { ( \mathrm { E M } ) \alpha \beta } { } _ { ; \beta } = - F ^ { \alpha \beta } J _ { \beta } .
$$

But $F ^ { \alpha \beta } J _ { \beta }$ is just the Lorentz 4-force per unit volume with which the electromagnetic field acts on the charged mater [see the Lorentz force equation (22.l7c)； also equation (5.43)}; i.e.,it is T(MATTER)aβ. ;B Consequently,the above equation can be rewritten in the form (22.18b) cited in the text.

# \$22.5. GEOMETRIC OPTICS IN CURVED SPACETIME\*

Radio waves from the quasar 3C279 pass near the sun and get deflected by its gravitational field. Light rays emitted by newborn galaxies long ago and far away propagate through the cosmologically curved spacetime of the universe,and get focused (and redshifted) producing curvature-enlarged (but dim) images of the galaxies on the Earth's sky.

These and most other instances of the propagation of light and radio waves are subject to the laws of geometric optics. This section derives those laws, in curved spacetime, from Maxwell's equations.

The fundamental laws of geometric optics are: (1) light rays are null geodesics; (2) the polarization vector is perpendicular to the rays and is parallel-propagated along the rays; and (3) the amplitude is governed by an adiabatic invariant which, in quantum language, states that the number of photons is conserved.

The conditions under which these laws hold are defined by conditions on three lengths: (l) the typical reduced wavelength of the waves,

$$
\lambda \equiv \frac { \lambda } { 2 \pi } = \binom { \mathrm { { * c l a s s i c a l ~ d i s t a n c e ~ o f ~ c l o s e s t ~ a p p r o a c h ~ f o r } } } { a \ p h o t o n \ w i t h \ o n e \ u n i t \ o f \ a n g u l a r \ m o m e n t u m ^ { \prime } } \Big ) ,
$$

as measured in a typical local Lorentz frame (e.g., a frame at rest relative to nearby galaxies)； (2) the typical length $\mathcal { L }$ over which the amplitude, polarization,and wavelength of the waves vary, e.g., the radius of curvature of a wave front, or the length of a wave packet produced by a sudden outburst in a quasar; (3) the typical radius of curvature $\mathcal { R }$ of the spacetime through which the waves propagate,

$$
\mathcal { R } \equiv \left| \operatorname * { t y p i c a l \ c o m p o n e n t \ o f } \ R i e m a n n \mathrm { \ a s \ m e a s u r e d } \right| ^ { - 1 / 2 } .
$$

Overview of geometric optics

Conditions for validity of geometric optics

Geometric optics is valid whenever the reduced wavelength is very short compared to each of the other scales present,

$$
\lambda \ll \mathcal { L } \mathrm { a n d } \lambda \ll \mathcal { R } ,
$$

so that the waves can be regarded locally as plane waves propagating through spacetime of negligible curvature.

Mathematically one exploits the geometric-optics assumption, $\lambda \ll \mathcal { L }$ and $\lambda \ll \mathcal { R }$ ， as follows. Focus attention on waves that are highly monochromatic over regions $\lesssim \mathcal { L } .$ .(More complex spectra can be analyzed by superposition, i.e.,by Fourier analysis.)Split the vector potential of electromagnetic theory into a rapidly changing, real phase,

The "'two-length-scale" expansion underlying geometric optics

$$
\theta \sim ( \mathrm { d i s t a n c e } \ p r o p a g a t e d ) / \lambda ,
$$

and a slowly changing,complex amplitude(i.e. one with real and imaginary parts),

$$
\pmb { A } = \mathrm { R e a l ~ p a r t ~ o f } \{ \mathrm { a m p l i t u d e } \times e ^ { i \theta } \} \equiv \Re \{ \mathrm { a m p l i t u d e } \times e ^ { i \theta } \} .
$$

Imagine holding fixed the scale of the amplitude variation, $\mathcal { E }$ ,and the scale of the spacetime curvature, $\mathscr { R }$ ,while making the reduced wavelength, $\pmb { \lambda }$ ,shorter and shorter. The phase will get larger and larger $( \theta \propto 1 / \lambda )$ at any fixed event in spacetime, but the amplitude as a function oflocation in spacetime can remain virtually unchanged,

This circumstance allows one to expand the amplitude in powers of :\*

$$
\begin{array} { l } { { \mathrm { \bf ~ \Gamma ~ \ a m p u u u c = } \atop { \mathrm { \bf ~ \Gamma ~ } } } } \\ { { \mathrm { \bf ~ \Gamma ~ \ i n d e p e n d e n t { \bf \Gamma } } } } \\ { { \mathrm { \bf ~ \Gamma ~ \ o f ~ } \lambda } } \end{array} \nonumber
$$

The vector potential in geometric optics

[Actually, the expansion proceeds in powers of the dimensionless number

$$
\lambda / ( \mathrm { m i n i m u m ~ o f } \ \mathcal { L } \ \mathrm { ~ a n d ~ } \ \mathcal { R } ) \equiv \lambda / L .
$$

Applied mathematicians call this a “two-length-scale expansion”；see,e.g., Cole (1968). The basic short-wavelength approximation here has a long history; see,e.g., Liouville (1837), Rayleigh (1912). Following a suggestion of Debye, it was applied to Max well's equations by Sommerfeld and Runge (l911). It is familiar as the WKB approximation in quantum mechanics,and has many other applications as indicated by the bibliography in Keller,Lewis,and Seckler (1956). The contribution of higher order terms is considered by Kline (l954) and Lewis (l958). See especially the book of Froman and Froman (1965).]

It is useful to introduce a parameter ε that keeps track of how rapidly various terms approach zero (or infinity) as $\pmb { \lambda } / L$ approaches zero:

$$
A _ { \mu } = \mathfrak { R } \{ ( a _ { \mu } + \varepsilon b _ { \mu } + \varepsilon ^ { 2 } c _ { \mu } + \cdot \cdot \cdot ) e ^ { { \mathrm { i } } \theta / { \varepsilon } } \} .
$$

Any term with a factor $\varepsilon ^ { n }$ in front of it varies as $( { \pmb { \chi } } / L ) ^ { n }$ in the limit of very small wavelengths $[ \theta \propto ( \pmb { \lambda } / L ) ^ { - 1 }$ ； $c _ { \mu } \propto ( \dot { x } / L ) ^ { 2 }$ ; etc.].By convention,ε is a dummy expan-sion parameter with eventual value unity; so it can be dropped from the calculations when it ceases to be useful. And by convention, all “post-geometric-optics correc-tions" are put into the amplitude terms b, c,...； none are put into $\pmb \theta$

Note that,while the phase $\pmb \theta$ is a real function of position in spacetime, the amplitude and hence the vectors $\pmb { a }$ ,b, c,...are complex. For example, to describe monochromatic waves with righthand circular polarization,propagating in the $_ { z }$ direction, one could set $\theta = \omega ( z - t )$ and $a = \dot { 1 / \sqrt { 2 } } a ( { \pmb e } _ { x } + \dot { i \pmb e } _ { y } )$ with $\pmb { a }$ real; so‘

$$
A = \Re \left\{ { \frac { 1 } { \sqrt { 2 } } } a ( e _ { x } + i e _ { y } ) e ^ { i \omega ( z - t ) } \right\} = { \frac { 1 } { \sqrt { 2 } } } a \{ \cos \left[ \omega ( z - t ) \right] e _ { x } - \sin \left[ \omega ( z - t ) \right] e _ { y } \}
$$

The assumed form (22.25) for the vector potential is the mathematical foundation of geometric optics. All the key equations of geometric optics result from inserting this vector potential into the source-free wave equation $\pmb { \mathscr { A } } = 0$ [equation (22.19d)] and into the Lorentz gauge condition $\pmb { \nabla } \cdot \pmb { A } = 0$ [equation (22.19c)]. The resulting equations (derived below) take their simplest form only when expressed in terms of the following:

Basic concepts of geometric optics:

"polarization vector,” ${ \pmb f } \equiv { \pmb a } / a =$ "unit complex vector along a".

(Here ā is the complex conjugate of $\pmb { a }$ ) Light rays are defined to be the curves $\mathcal { P } ( \lambda )$ normal to surfaces of constant phase $\pmb \theta$ Since $\pmb { k } \equiv \pmb { \nabla } \theta$ is the normal to these surfaces, the differential equation for a light ray is

(4) light rays

$$
{ \frac { d x ^ { \mu } } { d \lambda } } = k ^ { \mu } ( x ) = g ^ { \mu \nu } ( x ) \theta _ { , \nu } ( x ) .
$$

Box 22.3,appropriate for study at this point, shows the polarization vector, wave vector, surfaces of constant phase,and light rays for a propagating wave; the scalar amplitude, not shown there, merely tells the length of the vector amplitude a.Insight into the complex polarization vector, if not familiar from electrodynamics,can be developed later in Exercise 22.12.

So much for the foundations. Now for the calculations. First insert the geometricoptics vector potential (22.25) into the Lorentz gauge condition:

Derivation of laws of geometric optics

$$
0 = { A ^ { \mu } } _ { ; \mu } = \Re \left\{ \left[ { \frac { i } { \varepsilon } } k _ { \mu } ( a ^ { \mu } + \varepsilon b ^ { \mu } + \cdot \cdot \cdot ) + ( a ^ { \mu } + \varepsilon b ^ { \mu } + \cdot \cdot \cdot ) _ { ; \mu } \right] e ^ { \mathrm { i } \theta / \varepsilon } \right\} .
$$

The leading term (order $1 / \varepsilon$ says

$$
{ \bf { k \cdot a } } = 0 ~ ( a m p l i t u d e ~ i s ~ p e r p e n d i c u l a r ~ t o ~ w a v e ~ v e c t o r ) ;
$$

or, equivalently

$$
{ \pmb k } \cdot { \pmb f } = 0 ~ ( p o l a r i z a t i o n ~ i s ~ p e r p e n d i c u l a r ~ t o ~ w a v e ~ v e c t o r ) .
$$

The post-geometric-optics breakdown in this orthogonality condition is governed by the higher-order terms $[ 0 ( 1 ) , \ 0 ( \varepsilon ) , \ 0 ( \varepsilon ^ { 2 } ) , \ldots ]$ in the gauge condition (22.27)；for example, the O(l) terms say

$$
\pmb { k } \cdot \pmb { b } = i \pmb { \nabla } \cdot \pmb { a } .
$$

Next insert the vector potential (22.25) into the source-free wave equation (22.19d):

$$
\begin{array} { r l } & { 0 = ( { \cal A } _ { d R } { \cal A } ) ^ { \alpha } = - { \cal A } ^ { \alpha ; \beta } { } _ { \beta } + { \cal R } ^ { \alpha } { } _ { \beta } { \cal A } ^ { \beta } } \\ { } & { ~ = \Re \left\{ \left[ \frac { 1 } { \varepsilon ^ { 2 } } k ^ { \beta } k _ { \beta } ( a ^ { \alpha } + \varepsilon b ^ { \alpha } + \varepsilon ^ { 2 } c ^ { \alpha } + \cdot \cdot \cdot ) - 2 \frac { i } { \varepsilon } k ^ { \beta } ( a ^ { \alpha } + \varepsilon b ^ { \alpha } + \cdot \cdot \cdot ) _ { ; \beta } \right. \right. } \\ { } & { \qquad \left. \left. - \frac { i } { \varepsilon } k ^ { \beta } { } _ { ; \beta } ( a ^ { \alpha } + \varepsilon b ^ { \alpha } + \cdot \cdot \cdot ) - ( a ^ { \alpha } + \cdot \cdot \cdot ) ^ { ; \beta } { } _ { \beta } + { \cal R } ^ { \alpha } { } _ { \beta } ( a ^ { \beta } + \cdot \cdot \cdot ) \right] e ^ { \mathrm { i } \theta / \varepsilon } \right\} . } \end{array}
$$

Collect terms of order $1 / \varepsilon ^ { 2 }$ and $1 / \varepsilon$ (terms of order higher than $1 / \varepsilon$ govern postgeometric-optics corrections):

(continued on page 576)

![](images/794db3806a7d0feda19d06b47ed12076f074c8ff9d8ddec1a0960382f721f4dd.jpg)  
Box 22.3 GEOMETRY OF AN ELECTROMAGNETIC WAVE TRAIN   
one wavelength, $2 \pi \lambda$ ， as seen in local Lorentz frame

direction of propagation as seen in local Lorentz frame

The drawing shows surfaces of constant phase, $\theta =$ constant, emerging through the “surface of simultaneity", $t = 0$ , of a local Lorentz frame. The surfaces shown are alternately “crests” $( \theta = 1 7 6 4 \pi$ ， $\theta = 1 7 6 6 \pi , \ldots .$ and“troughs” $( \theta = 1 7 6 5 \pi _ { ; }$ $\theta =$ $1 7 6 7 \pi , \ldots )$ of the wave train. These surfaces make up a 1-form, $\widetilde { \pmb { k } } = \pmb { d } \pmb { \theta }$ The "corresponding vector” $\pmb { k } = \pmb { \nabla } \theta$ is the “wave vector." The wave vector is null, $\pmb { k } \cdot \pmb { k } = 0$ ,according to Maxwell's equations [equation (22.30). Therefore it lies in a surface of constant phase:

$$
{ \binom { \mathrm { n u m b e r ~ o f ~ s u r f a c e s } } { \mathrm { p i e r c e d ~ b y ~ } k } } = \langle d \theta , k \rangle = \langle \widetilde { k } , k \rangle = { k \cdot k } = 0 .
$$

But not only does it lie in a surface of constant phase; it is also perpendicular to that surface! Any vector $\pmb { \nu }$ in that surface must satisfy $\pmb { k } \cdot \pmb { v } = \langle \widetilde { \pmb { k } } , \pmb { v } \rangle \doteq \langle \pmb { d } \theta , \pmb { v } \rangle = 0$ because it pierces no surfaces.

Geometric optics assumes that the reduced wavelength $\pmb { \lambda }$ ,as measured in a typical local Lorentz frame, is small compared to the scale $\mathcal { L }$ of inhomogeneities in the wave train and small compared to the radius of curvature of spacetime, $\mathcal { R }$ Thus, over regions much larger than $\pmb { \lambda }$ but smaller than $\mathcal { L }$ or $\mathcal { R }$ , the waves are plane-fronted and monochromatic,and there exist Lorentz reference frames (Riemann normal coordinates). In one of these “extended" local Lorentz frames, the phase must be

$$
\theta = k _ { \alpha } x ^ { \alpha } + \mathrm { c o n s t a n t } ;
$$

no other expression will yield ${ \overline { { \mathbf { \nabla } } } } \pmb { \nabla } \theta = \pmb { k } .$ . The corresponding vector potential [equation (22.25)] will be

$$
{ \cal A } ^ { \mu } = \Re \left\{ a ^ { \mu } \exp [ i ( k \cdot x - k ^ { 0 } t ) ] \right\} + ( { } ^ { \mathrm { * * } } \mathrm { p o s t . } \mathrm { g e o m e t r i c \mathrm { - } o p t i c s ~ c o r r e c t i o n s " } ) ;
$$

hence,

$$
\begin{array} { c } { k ^ { 0 } = 2 \pi / ( \mathrm { p e r i o d ~ o f ~ w a v e } ) = 2 \pi \nu = \omega \equiv ( \mathrm { a n g u l a r ~ f r e q } } \\ { \left| k \right| = 2 \pi / ( \mathrm { w a v e l e n g t h ~ o f ~ w a v e } ) = 1 / \lambda = \omega , } \end{array}
$$

At each event in spacetime there is a wave vector; and these wave vectors, tacked end-on-end, form a family of curves-the “light rays”or simply “rays”-whose tangent vector is $\pmb { k }$ .The rays,like their tangent vector,lie both in and perpendicular to the surfaces of constant phase.

The affine parameter $\lambda$ of a ray (not to be confused with wavelength $= 2 \pi \lambda$ satisfies $\pmb { k } = \bar { d } / d \lambda$ ; therefore it is given by

$$
\lambda = t / k ^ { 0 } + \mathrm { c o n s t a n t } = t / \omega + \mathrm { c o n s t a n t } ,
$$

where $t$ is proper time along the ray as measured, not by the ray itself (its proper time is zero!), but by the local Lorentz observer who sees angular frequency $\omega .$ Thus, while $\pmb { \omega }$ is a frame-dependent quantity and $t$ is also a frame-dependent quantity, their quotient $t / \omega$ when measured along the ray (not off the ray) is the frame-independent affine parameter. For a particle it is possible and natural to identify the affine parameter $\lambda$ with proper time $\tau$ .For a light ray this identification is unnatural and impossible. The lapse of proper time along the ray is identically zero. The springing up of $\lambda$ to take the place of the vanished $\pmb { \tau }$ gives one a tool to do what one might not have suspected to be possible. Given a light ray shot out at event $\boldsymbol { \mathcal { Q } }$ and passing through event $\mathcal { B }$ , one can give a third event $\mathcal { C }$ along the same null world line that is twice as“far” from $\boldsymbol { \mathcal { Q } }$ as $\mathcal { B }$ is “far,” in a new sense of“far” that has nothing whatever directly to do with proper time (zero!), but is defined by equal increments of the affine parameter $( \lambda _ { \mathfrak { c } } - \lambda _ { \mathfrak { r } } = \lambda _ { \mathfrak { s } } - \lambda _ { \mathfrak { c } } )$ .The “affine parameter” has a meaning for any null geodesic analyzed even in isolation. In this respect, it is to be distinguished from the so-called “luminosity distance”which is sometimes introduced in dealing with the propagation of radiation through curved spacetime, and which is defined by the spreading apart of two or more light rays coming from a common source.

Maxwell's equations as explored in the text [equation (22.28')] guarantee that the complex polarization vector $\pmb { \mathscr { f } }$ is perpendicular to the wave vector $\pmb { k }$ and that, therefore, it lies in a surface of constant phase (see drawing). Intuition into the polarization vector is developed in exercise 22.12.

$$
\scriptstyle 0 \left( { \frac { 1 } { \varepsilon ^ { 2 } } } \right) :
$$

$$
k ^ { \beta } k _ { \beta } a ^ { \alpha } = 0
$$

$\implies \boldsymbol { k } \cdot \boldsymbol { k } = 0$ (wave vector is null);

$$
\scriptstyle 0 \left( { \frac { 1 } { \varepsilon } } \right) ;
$$

$$
\begin{array} { r l } & { \frac { 1 } { \varepsilon } \bigg ) : \qquad \underbrace { k ^ { \beta } k _ { \beta } b ^ { \alpha } - 2 i \Big ( k ^ { \beta } a ^ { \alpha } { } _ { ; \beta } + \frac { 1 } { 2 } k ^ { \beta } { } _ { ; \beta } a ^ { \alpha } \Big ) } _ { \dot { \mathbb { L } } \left[ = \ 0 \right] } = 0 } \\ & { \implies \Psi _ { k } a = - \frac { 1 } { 2 } ( \pmb { \nabla } \cdot \pmb { k } ) a \ ( p r o p a g a t i o n \ e q u a t i o n \ f o r \ v e c t o r \ a m p l i t u d e ) . } \end{array}
$$

These equations (22.30,22.31） together with equation (22.28) are the basis from which all subsequent results will follow. As a first consequence,one can obtain the geodesic law from equation (22.30). Form the gradient of $\pmb { k } \cdot \pmb { k } = 0$ ，

$$
0 = ( k ^ { \beta } k _ { \beta } ) _ { ; \alpha } = 2 k ^ { \beta } k _ { \beta ; \alpha } ,
$$

and use the fact that $k _ { \beta } \equiv \theta _ { , \beta }$ is the gradient of a scalar to interchange indices, $\theta _ { ; \beta \alpha } = \theta _ { ; \alpha \beta }$ 0r

$$
0 = k ^ { \beta } k _ { \beta ; \alpha } = k ^ { \beta } k _ { \alpha ; \beta } .
$$

The main laws of geometric optics:

The result is

$$
\Psi _ { k } k = 0 ~ ( p r o p a g a t i o n ~ e q u a t i o n ~ f o r ~ w a v e ~ v e c t o r ) .
$$

(1） Light rays are null geodesics

Notice that this is the geodesic equation! Combined with equation (22.30),it is the statement, derived from Maxwel's equations in curved spacetime, that light rays are null geodesics, the first main result of geometric optics.

Turn now from the propagation vector $\pmb { k } = \pmb { \nabla } \theta$ to the wave amplitude $a = a f ,$ and obtain separate equations for the magnitude $^ { a }$ and polarization f. Use equation (22.31) to compute

$$
\begin{array} { l } { { 2 a \widehat { \circ } _ { \pmb { \partial } _ { k } a } = 2 a \pmb { \nabla } _ { k } a = \pmb { \nabla } _ { k } a ^ { 2 } = \pmb { \nabla } _ { k } ( a \cdot \overrightarrow { a } ) = \overline { { a } } \cdot \pmb { \nabla } _ { k } a + a \cdot \pmb { \nabla } _ { k } \overrightarrow { a } } } \\ { { \mathrm { } } } \\ { { \mathrm { } = - \displaystyle \frac { 1 } { 2 } ( \pmb { \nabla } \cdot \pmb { k } ) ( \overline { { a } } \cdot \pmb { a } + a \cdot \overrightarrow { a } ) = - a ^ { 2 } \pmb { \nabla } \cdot \pmb { k } ; } } \end{array}
$$

so

$$
\hat { v } _ { k } a = - \frac { 1 } { 2 } ( \pmb { \nabla } \cdot \pmb { k } ) a ( p r o p a g a t i o n ~ e q u a t i o n ~ f o r ~ s c a l a r ~ a m p l i t u d e ) ,
$$

Next write $\bullet = a \bullet$ in equation (22.31) to obtain

$$
0 = \boldsymbol { \nabla } _ { k } ( a t ) + \frac { 1 } { 2 } \left( \boldsymbol { \nabla } \cdot \boldsymbol { k } \right) a t = a \boldsymbol { \nabla } _ { k } t + \frac { 1 } { t } \left[ \boldsymbol { \nabla } _ { k } a + \frac { 1 } { 2 } \left( \boldsymbol { \nabla } \cdot \boldsymbol { k } \right) a \right] = a \boldsymbol { \nabla } _ { k } t
$$

$$
\pmb { \nabla } _ { k } \pmb { f } = 0 \ ( p r o p a g a t i o n \ e q u a t i o n \ f o r \ p o l a r i z a t i o n \ v e c t o r ) .
$$

This together with equation (22.28), constitutes the second main result of geometric optics,that the polarization vector is perpendicular to the rays and is parallel-propagated along the rays. It is now possible to see that these results,derived from equations (22.30) and (22.31) are consistent with the gauge condition (22.28). The vectors $\pmb { k }$ and $\pmb { \mathscr { f } } ,$ specifed at one point, are fixed along the entire ray by their propagation equations. But because both propagation equations are parallel-transport laws,the conditions $\pmb { k } \cdot \pmb { k } = 0$ ， ${ \pmb f } \cdot { \pmb { \bar { f } } } = 1$ ,and $\pmb { k } \cdot \pmb { f } = 0$ , once imposed on the vectors at one point, willbe satisfied along the entire ray.

The equation (22.33) for the scalar amplitude can be reformulated as a conservation law. Since $\partial _ { \pmb { k } } \equiv ( \pmb { k } \cdot \pmb { \nabla } )$ ,one rewrites the equation as $( \pmb { k } \cdot \pmb { \nabla } ) a ^ { 2 } + a ^ { 2 } \pmb { \nabla } \cdot \pmb { k } = 0$ ， or

(2)polarization vector is perpendicular to ray and is parallel propagated along ray

$$
\pmb { \nabla } \cdot ( a ^ { 2 } \pmb { k } ) = 0 .
$$

(3) conservation of \`photon number"

Consequently the vector $a ^ { 2 } \pmb { k }$ is a “conserved current,” and the integral $\displaystyle \int a ^ { 2 } k ^ { \mu } d ^ { 3 } { \textstyle \sum _ { \mu } }$ has a fixed, unchanging value for each 3-volume cutting a given tube formed of light rays. (The tube must be so formed of rays that an integral of $a ^ { 2 } k$ over the walls of the tube will give zero.) What is conserved? To remain purely classical, one could say it is the “number of light rays” and call $a ^ { 2 } k ^ { 0 }$ the“density of light rays” on an $x ^ { 0 } =$ constant hypersurface. But the proper correspondence and more concrete physical interpretation make one prefer to call equation (22.35) the law of conservation of photon number. It is the third main result of geometric optics.Photon number, of course, is not always conserved; it is an adiabatic invariant, a quantity that is not changed by influences (e.g., spacetime curvature, ${ \sim } 1 / \mathcal { R } ^ { 2 } )$ which change slowly $( { \mathcal { R } } \gg { \mathcal { X } } )$ compared to the photon frequency.

Box 22.4 summarizes the above equations of geometric optics,along with others derived in the exercises,

Exercise 22.11. ELECTROMAGNETIC FIELD AND STRESS ENERG Derive the equations given in part $\mathbf { D }$ of Box 22.4 for $\pmb { F } , \pmb { E } , \pmb { B }$ and $\pmb { \tau } .$

# Exercise 22.12. POLARIZATION

At an event ${ \mathfrak { P } } _ { 0 }$ through which geometric-optics waves are passing, introduce a local Lorentz frame with $\bar { \cdot }$ -axis along the direction of propagation. Then $\pmb { k } = \omega ( \pmb { e } _ { 0 } + \pmb { e } _ { z } )$ . Since the polarization vector is orthogonal to $\pmb { k }$ 、itis $\pmb { f } = f ^ { 0 } ( \pmb { e } _ { 0 } + \pmb { e } _ { z } ) + f ^ { 1 } \pmb { e } _ { z } + f ^ { 2 } \pmb { e } _ { y }$ and since $\dot { \pmb { f } } \cdot \pmb { \bar { f } } = 1$ it has $| f ^ { 1 } | ^ { 2 } + | f ^ { 2 } | ^ { 2 } = 1$

(a） Show that the component $f ^ { 0 }$ of the polarization vector has no influence on the electric and magnetic fields measured in the given frame;i.e., show that one can add a multiple of $\pmb { k }$ to $\pmb { \mathscr { f } }$ without affecting any physical measurements.

(continued on page 581)

# Box 22.4 GEOMETRIC OPTICS IN CURVED SPACETIME (Summary of Results Derived in Text and Exercises)

# A. Geometric Optics Assumption

Electromagnetic waves propagating in a source-free region of spacetime are locally plane-fronted and monochromatic (reduced wavelength $\lambda \ll$ scale $\mathcal { E }$ over which amplitude,wavelength, or polarization vary; and $\lambda \ll \Re =$ mean radius of curvature of spacetime).

# B. Rays, Phase,and Wave Vector (see Box 22.3)

Everything (amplitude, polarization, energy, etc.） is transported along rays; and the quantities on one ray do not influence the quantities on any other ray.

The rays are null geodesics of curved spacetime, with tangent vectors ("wave vectors")k:

$$
\pmb { \nabla } _ { \pmb { k } } \pmb { k } = 0 .
$$

The rays both lie in and are perpendicular to surfaces of constant phase, $\theta =$ const.;and their tangent vectors are the gradient of $\pmb \theta$ ：

$$
\pmb { k } = \pmb { \nabla } \pmb { \theta } .
$$

In a local Lorentz frame, $k ^ { 0 }$ is the“angular frequency" and $k ^ { 0 } / 2 \pi$ is the ordinary frequency of the waves, and

$$
{ \pmb n } = { \pmb k } / k ^ { 0 }
$$

is a unit 3-vector pointing along their direction of propagation.

# C. Amplitude and Polarization Vector

The waves are characterized by a real amplitude $_ { a }$ and a complex polarization vector $\pmb { \mathscr { f } }$ of unit length, $\pmb { \mathscr { f } } \cdot \bar { \pmb { f } } = 1$ .(Of the fundamental quantities $\theta , \kappa , a , \tilde { \prime } ,$ all are real except f. See exercise 22.12 for deeper understanding of $\pmb { \mathscr { f } } .$ ）

The polarization vector is everywhere orthogonal to the rays, $\pmb { k } \cdot \pmb { f } = 0$ ； and is parallel-transported along them, $\pmb { \nabla } _ { \pmb { k } } \pmb { f } = 0$

The propagation law for the amplitude is

$$
\partial _ { \pmb { k } } a = - \frac { 1 } { 2 } ( \pmb { \nabla } \cdot \pmb { k } ) a .
$$

This propagation law is equivalent to a law of conseruation of photons (classically: of rays)； $a ^ { 2 } k$ is the"“conserved current” satisfying $\pmb { \nabla } \pmb { \cdot } ( a ^ { 2 } \pmb { k } ) = 0$ ；and $( 8 \pi \hbar ) ^ { - 1 } \int a ^ { 2 } k ^ { 0 } \sqrt { | g | } d ^ { 3 } x$ is the number of photons (rays) in the 3-volume of integration on any $x ^ { 0 } =$ constant hypersurface,and is constant as this volume is carried along the rays.

The propagation law holds separately on each hypersurface of constant phase. There it can be interpreted as conservation of a $a ^ { 2 } { \mathcal { Q } }$ where $\boldsymbol { \mathscr { a } }$ is a two-dimensional cross-sectional area of a pulse of photons or rays. See exercise 22.13.

# D. Vector Potential, Electromagnetic Field, and Stress-Energy-Momentum

At any event the vector potential in Lorentz gauge is

$$
A = \Re \{ a e ^ { \mathsf { i } \theta } \pmb { \mathscr { f } } \} ,
$$

where R denotes the real part.

The electromagnetic field tensor is orthogonal to the rays, $\pmb { F } \cdot \pmb { k } = 0$ , and is given by

$$
{ \pmb F } = \Re \{ i a e ^ { i \theta } { \pmb k } \wedge { \pmb f } \} , \quad \_
$$

The corresponding electric and magnetic felds in any local Lorentz frame are

$$
\begin{array} { c } { { E = \Re \{ i a k ^ { 0 } e ^ { \mathrm { { i } } \theta } ( \mathrm { p r o j e c t i o n \ o f \ } f \mathrm { \ p e r p e n d i c u l a r \ t o \ } k ) \} , } } \\ { { B = n \times E , \mathrm { w h e r e \ } n \equiv k / k ^ { 0 } . } } \end{array}
$$

The stress-energy tensor, averaged over a wavelength, is

$$
\dot { \pmb { \tau } } = ( 1 \bar { / } 8 \bar { \pmb { \pi } } ) a ^ { 2 } \pmb { k } \otimes \pmb { k } ,
$$

corresponding to an energy density in a local Lorentz frame of

$$
T ^ { 0 0 } = ( 1 / 8 \pi ) ( a k ^ { 0 } ) ^ { 2 }
$$

and an energy flux of

$$
T ^ { 0 j } = T ^ { 0 0 } n ^ { j } , \ldots \ldots \ -
$$

that-cnergy flows along the rays (in ${ \pmb n } = { \pmb k } / k ^ { 0 }$ direction) with the speed of :ht. This is identical with the stress-energy tensor that would be produced by beam of photons with 4-momenta $\pmb { p } = \hbar \pmb { k }$

Conservation of energy-momentum $\begin{array} { r }  \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \mathbf { \nabla } \nabla \mathbf { \nabla } \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \mathbf { \nabla } \nabla \nabla \mathbf { } \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \mathbf { } \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \nabla \mathbf \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla \nabla  \end{array}$ follows from the ray conservation law $\pmb { \nabla } \pmb { \cdot } ( a ^ { 2 } \pmb { k } ) = 0$ and the geodesic law $\pmb { \nabla } _ { \pmb { k } } \pmb { k } \equiv ( \pmb { k } \cdot \pmb { \nabla } ) \pmb { k } = 0$ ：

$$
8 \pi \ \Psi \cdot T = \Psi \cdot ( a ^ { 2 } \pmb { k } \otimes \pmb { k } ) = [ \pmb { \nabla } \cdot ( a ^ { 2 } \pmb { k } ) ] \pmb { k } + a ^ { 2 } ( \pmb { k } \cdot \pmb { \nabla } ) \pmb { k } = 0 .
$$

The adiabatic(geometric optics) invariant“ray number" $a ^ { 2 } k ^ { 0 }$ or"photon number" $( 8 \pi \hbar ) ^ { - 1 } a ^ { 2 } k ^ { 0 }$ in a unit volume is proportional to the energy, $( 8 \pi ) ^ { - 1 } a ^ { 2 } ( k ^ { 0 } ) ^ { 2 }$ ， divided by the frequency, $k ^ { 0 }$ --corresponding exactly to the harmonic oscillator adiabatic invariant $E / \omega$ [Einstein (19i2),Ehrenfest (19l6),Landau and Lifshitz (1960)].

# E. Photon Reinterpretation of Geometric Optics

The laws of geometric optics can be reinterpreted as follows. This reinterpretation becomes a foundation of the standard quantum theory of the electromagnetic field (see,e.g.,Chapters 1 and I3 of Baym (l969)]; and the classical limit of that quantum theory is standard Maxwell electrodynamics.

Photons are particles of zero rest mass that move along nul geodesics of spacetime (the null rays).

The 4-momentum of a photon is related to the tangent vector of the nul ray (wave vector) by $\pmb { p } = \hbar \pmb { k }$ .A renormalization of the afine parameter,

$$
( \mathrm { n e w ~ p a r a m e t e r } ) = ( 1 / \hbar ) \times ( \mathrm { o l d ~ p a r a m e t e r } ) ,
$$

makes $\pmb { \rho }$ the tangent vector to the ray.

Each photon possesses a polarization vector, $\pmb { \mathscr { f } } ,$ which is orthogonal to its 4-momentum ( $\mathbf { \nabla } \cdot \mathbf { \vec { r } } = 0 ,$ ,and which it parallel-transports along its geodesic world line $( \pmb { \nabla _ { p } } \pmb { f } = 0 )$ .

A swarm of photons, all with nearly the same 4-momentum $\pmb { p }$ and polarization vector $\pmb { \mathscr { f } }$ (as compared by parallel transport), make up a classical electromagnetic wave.The scalar amplitude $^ { a }$ of the wave is determined by equating the stress-energy tensor of the wave-

$$
\pmb { \tau } = \frac { 1 } { 8 \pi } a ^ { 2 } \pmb { k } \otimes \pmb { k } = \frac { 1 } { 8 \pi } \bigg ( \frac { a } { \hbar } \bigg ) ^ { 2 } \pmb { p } \otimes \pmb { p }
$$

to the stress-energy tensor of a swarm of photons with number-flux vector S,

$$
{ \pmb { \tau } } = { \pmb { \rho } } \otimes { \pmb { s } }
$$

[see equation (5.18). The result:

$$
{ \pmb S } = \frac { 1 } { 8 \pi } \bigg ( \frac { a } { \hbar } \bigg ) ^ { 2 } { \pmb \rho } = \frac { 1 } { 8 \pi \hbar } a ^ { 2 } { \pmb k }
$$

or, in any local Lorentz frame,

$$
a = ( 8 \pi \hbar ^ { 2 } S ^ { 0 } / p ^ { 0 } ) ^ { 1 / 2 } = ( 8 \pi ) ^ { 1 / 2 } \hbar \left( { \frac { \mathrm { n u m b e r ~ d e n s i t y ~ o f ~ p h o t o n s } } { \mathrm { e n e r g y ~ o f ~ o n e ~ p h o t o n } } } \right) ^ { 1 / 2 } .
$$

(b) Show that the following polarization vectors correspond to the types of polarization listed:

(c) Show that the type of polarization (linear; circular; elliptical with given eccentricity of ellipse) is the same as viewed in any local Lorentz frame at any event along a given ray. [Hint:Use pictures and abstract calculations rather than Lorentz transformations and component calculations.]

# Exercise 22.13. THE AREA OF A BUNDLE OF RAYS

Write equation (22.31) in a coordinate system in which one of the coordinates is chosen to be $\scriptstyle x ^ { 0 } = \theta$ ,the phase (a retarded time coordinate).

(a) Show that $g ^ { 0 0 } = 0$ and that no derivatives $\partial / \partial \pmb \theta$ appear in equation (22.33); so propagation of a can be described within a single $\theta =$ constant hypersurface.

(b) Perform the following construction (see Figure 22.1). Pick a ray $\mathcal { C } _ { 0 }$ along which $\pmb { a }$ is to be propagated.Pick a bundle of rays,with two-dimensional cross section,that (i） all lie in the same constant-phase surface as $\mathcal { C } _ { 0 } ,$ and (ii） surround $\mathcal { C } _ { 0 }$ (The surface is three-di-("conseruation of photon fux").(3) $\boldsymbol { \mathcal { Q } }$ obeys the “propagation equation" (22.36).

![](images/2fef0e6d2c7950b0bf76f342d3bd9d4e56d6b73bb27477f142c7a10fb25410fb.jpg)  
Figure 22.1. Geometric optics fora bundle of rays with two-dimensional cross section,all lying in a surface of constant phase, $\theta = \mathsf { c o n s t }$ ，Sketch (a) shows the bundle, surrounding a central ray $c _ { \mathbf { 0 } } ^ { \prime } .$ in a spacetime diagram with one spatial dimension suppressed.Sketch (b) shows the bundle as viewed on a slice of simultaneity in a local Lorentz frame at the event $\mathcal { P } _ { \mathbf { 0 } }$ Slicing the bundle turns each ray into a“photon”；so the bundle becomes a two-dimensional surface filled with photons.The area $\boldsymbol { \mathcal { Q } }$ of this photon-filled surface obeys the following laws (see exercises 22.13 and 22.14):(l) $\boldsymbol { \mathcal { Q } }$ is independent of the choice of Lorentz frame;it depends only on location $\vartheta _ { \mathbf { 0 } }$ along the ray $\scriptstyle { \mathcal { C } } _ { 0 }$ .(2）The amplitude $^ { a }$ of the waves satisfies

mensional,soany bundle filing it hasa two-dimensional cross section.)At any event $\mathcal { P } _ { 0 } .$ in any local Lorentz frame there,on a “slice of simultaneity” $x ^ { 0 } =$ constant, measure the cross-sectional area $\pmb { \mathcal { a } }$ of the bundle.(Note: the area being measured is perpendicular to $\pmb { k }$ in the three-dimensional Euclidean sense; it can be thought of as the region occupied momentarily by a group of photons propagating along,side by side,in the $\pmb { k }$ direction.） Show that the area $\pmb { \mathcal { a } }$ is the same, at a given event $\boldsymbol { \mathfrak { P } } _ { 0 } ,$ regardless of what Lorentz frame is used to measure it; but the area changes from point to point along the ray $\mathcal { C } _ { 0 }$ as a result of the rays' divergence away from each other or convergence toward each other:

$$
\begin{array} { r } { \hat { v } _ { \pmb { k } } \pmb { \mathcal { a } } = ( \pmb { \nabla } \pmb { \cdot } \pmb { k } ) \pmb { \mathcal { a } } . } \end{array}
$$

Then show that $\scriptstyle { \mathcal { a } } a ^ { 2 }$ is a constant everywhere along the ray $\mathcal { E } _ { 0 }$ ("conservation of photon flux"). [Hints: (i) Any vector $\pmb { \xi }$ connecting adjacent rays in the bundle is perpendicular to $\pmb { k }$ ，because $\pmb { \xi }$ lies in a surface of constant $\pmb \theta$ and $\pmb { k } \cdot \pmb { \xi } \overset { \cdot } { = } \langle \widetilde { \pmb { k } } , \pmb { \xi } \rangle = \langle \pmb { d } \theta , \pmb { \xi } \rangle \overset { \cdot } { = } \overset$ (change in $\pmb \theta$ along $\xi ) = 0$ .(ii） Consider,for simplicity,a bundle with rectangular cross section as seen in a specific local Lorentz frame at a specific event $\mathcal { P } _ { 0 }$ [edge vectors $\pmb { v }$ and $\boldsymbol { \mathsf { w } }$ with ${ \pmb v } \cdot { \pmb w } = 0$ (edges perpendicular） and $\pmb { v } \cdot \pmb { e } _ { 0 } = \pmb { w } \cdot \pmb { e } _ { 0 } = 0$ (edges in surface of constant time） and $\pmb { v } \cdot \pmb { k } = \pmb { w } \cdot \pmb { k } = 0$ (since edge vectors connect adjacent rays of the bundle)]. Show pictorially that in any other Lorentz frame at $\mathcal { P } _ { 0 }$ ,the edge vectors are ${ \pmb v } ^ { \prime } = { \pmb v } + \alpha { \pmb k }$ and $w ^ { \prime } = w + \beta k$ for some $\pmb { \alpha }$ and $\beta$ .Conclude that in all Lorentz frames at $\mathcal { P } _ { 0 }$ the cross section has identical shape and identical area,and is spatially perpendicular to the direction of propagation $( \pmb { k } \cdot \pmb { v } = \pmb { k } \cdot \pmb { w } = 0 )$ .(iii) By a calculation in a local Lorentz frame show that $\partial _ { \pmb { k } } \pmb { \mathcal { a } } = ( \pmb { \nabla } \pmb { \cdot } \pmb { k } ) \pmb { \mathcal { a } }$ (iv) Conclude from $\hat { \partial } _ { \pmb { k } } a = - \frac { 1 } { 2 } ( \pmb { \nabla } \cdot \pmb { k } ) a$ that $\hat { v } _ { \star } ( \mathcal { a } a ^ { 2 } ) = 0 . ]$

# Exercise 22.14. FOCUSING THEOREM

The cross-sectional area $\boldsymbol { \mathscr { a } }$ of a bundle of rays all lying in the same surface of constant phase changes along the central ray of the bundle at the rate (22.36) (see Figure 22.1).

(a) Derive the following equation (“focusing equation") for the second derivative of $\pmb { \mathcal { Q } } ^ { 1 / 2 }$

$$
\frac { d ^ { 2 } \mathcal { Q } ^ { 1 / 2 } } { d \lambda ^ { 2 } } = - \bigg ( | \sigma | ^ { 2 } + \frac { 1 } { 2 } R _ { \alpha \beta } k ^ { \alpha } k ^ { \beta } \bigg ) \mathcal { Q } ^ { 1 / 2 } ,
$$

where $\lambda$ is affine parameter along the central ray $( \pmb { \mathscr { k } } = d / d \lambda )$ ,and the“magnitude of the shear of the rays”, $| \pmb { \sigma } |$ ,is defined by the equation

$$
\vert \sigma \vert ^ { 2 } \equiv { \frac { 1 } { 2 } } k _ { \alpha ; \beta } k ^ { \alpha ; \beta } - { \frac { 1 } { 4 } } ( k ^ { \mu } { } _ { ; \mu } ) ^ { 2 } .
$$

[Hint: This is a vigorous exercise in index manipulations. The key equations needed in the manipulations are $\mathcal { a } _ { , \alpha } k ^ { \alpha } = ( k ^ { \alpha } { } _ { ; \alpha } ) \mathcal { a }$ [equation (22.36)}; $k ^ { \alpha } { } _ { ; \beta } k ^ { \beta } = 0$ [geodesic equation (22.32) for rays]; $k _ { \alpha ; \beta } = k _ { \beta ; \alpha }$ [which follows from $k _ { \alpha } \equiv \theta _ { , \alpha } ] ;$ and the rule (16.6c) for interchanging covariant derivatives of a vector.]

(b) Show that, in a local Lorentz frame where $\pmb { k } = \omega ( \pmb { e } _ { t } + \pmb { e } _ { z } )$ at the origin,

$$
| \sigma | ^ { 2 } = \frac { 1 } { 4 } ( k _ { x , x } - k _ { y , y } ) ^ { 2 } + ( k _ { x , y } ) ^ { 2 } .
$$

Thus, $| \pmb { \sigma } | ^ { 2 }$ is nonnegative, which justifies the use of the absolute value sign.

(c) Discussion: The quantity $| \pmb { \sigma } |$ is called the shear of the bundle of rays because it measures the extent to which neighboring rays are sliding past each other [see,e.g., Sachs(1964)]. Hence,the focusing equation (22.37） says that shear focuses a bundle of rays (makes $d ^ { 2 } { \cal { Q } } ^ { 1 / 2 } / d \lambda ^ { 2 } < 0 )$ ; and spacetime curvature also focuses it if $R _ { \alpha \beta } k ^ { \alpha } k ^ { \beta } > 0$ ,but defocuses it if $R _ { \alpha \beta } k ^ { \alpha } k ^ { \beta } < 0$ .(When a bundle of toothpicks,originally circular in crosssection,is squeezed into an elliptic cross section, it is sheared.)

(d) Assume that the energy density $T _ { \hat { 0 } \hat { 0 } } .$ , as measured by any observer anywhere in spacetime,is nonnegative. By combining the focusing equation (22.37） with the Einstein field equation, conclude that

$$
\frac { d ^ { 2 } { d ^ { 1 / 2 } } } { d \lambda ^ { 2 } } \leq 0 \left( \begin{array} { l } { \mathrm { f o r ~ a n y ~ b u n d l e ~ o f ~ r a y s , ~ a l l ~ i n ~ t h e ~ s a m e } } \\ { \mathrm { s u r f a c e ~ o f ~ c o n s t a n t ~ p h a s e , ~ a n y w h e r e ~ i n } } \\ { \mathrm { s p a c e t i m e } } \end{array} \right)
$$

(focusing theorem). This theorem plays a crucial role in black-hole physics (S34.5)and in the theory of singularities (S34.6).

# \$22.6. KINETIC THEORY IN CURVED SPACETIME\*

The stars in a galaxy wander through spacetime, each on its own geodesic world line, each helping to produce the spacetime curvature felt by allthe others. Photons, left over from the hot phases of the big bang,bathe the Earth, bringing with themselves data on the homogeneity and isotropy of the universe. Theoretical analyses of these and many other problems are unmanageable, if they attempt to keep track of the motion of every single star or photon. But a statistical description gives accurate results and is powerful. Moreover,for most problems in astrophysics and cosmology, the simplest of statistical descriptions-one ignoring collisions-is adequate. Usually collisions are unimportant for the large-scale behavior of a system (e.g:; a galaxy), or they are so important that a fuid description is possible (e.g., in a stellar interior).

Consider,then, a swarm of particles (stars,or photons,or black holes,or ...) that move through spacetime on geodesic world lines, without colliding. Assume, for simplicity,that the particles all have the same rest mass. Then all information of a statistical nature about the particles can be incorporated into a single function, the “distribution function” or “number density in phase space", $\mathfrak { X }$

Define $\mathfrak { X }$ in terms of measurements made by a specific local Lorentz observer at a specific event $\mathcal { P } _ { 0 }$ in curved spacetime. Give the observer a box with 3-volume $\mathcal { V } _ { \pmb { \varepsilon } }$ (and with imaginary walls). Ask the observer to count how many particles, $N ,$ are inside the box and have local-Lorentz momentum components $p ^ { j }$ in the range

Volume in phase space for a group of identical particles

$$
P ^ { j } - \frac { 1 } { 2 } { \cal { \cal { A } } } p ^ { j } < p ^ { j } < P ^ { j } + \frac { 1 } { 2 } { \cal { \cal { A } } } p ^ { j } .
$$

(He can ignore the particle energies $p ^ { 0 }$ ； since all particles have the Same rest mass $m$ energy

$$
p ^ { 0 } = ( m ^ { 2 } + p ^ { 2 } ) ^ { 1 / 2 }
$$

is fixed uniquely by momentum.) The volume in momentum space occupied by the $N$ particles is $\mathcal { V } _ { p } = \varDelta p ^ { \boldsymbol { \tau } } \varDelta p ^ { \boldsymbol { \nu } } \varDelta p ^ { \boldsymbol { z } }$ ； and the volume in phase space is

$$
\begin{array} { r } { \mathcal { V } \equiv \mathcal { V } _ { \texttt { r } } \mathcal { T } _ { p } . } \end{array}
$$

Lorentz invariance of volume in phase space

Other observers at $\mathcal { P } _ { 0 }$ ,moving relative to the first, will disagree on how much spatial volume $\mathcal { V } _ { \pmb { z } }$ and how much momentum volume $\mathcal { T } _ { p }$ these same $N$ particles occupy:

$\mathcal { V } _ { \pmb { \varepsilon } }$ and $\mathcal { V } _ { p }$ depend on the choice of Lorentz frame.

However, all observers will agree on the value of the product $\mathcal { V } \equiv \mathcal { T } _ { \textit { \texttt { z } } } \mathcal { T } _ { \textit { p } }$ ("volume in phase space"):

The phase-space volume $\cdot \boldsymbol { \mathcal { V } }$ occupied by a given set of $N$ identical particles at a given event in spacetime is independent of the local Lorentz frame in which it is measured.

(See Box 22.5 for proof.) Moreover, as the same $N$ particles move through spacetime along their geodesic world lines (and through momentum space),the volume $\mathcal { V }$ they span in phase space remains constant:

Liouville's theorem (conservation of volume in phase space)

The $\mathcal { V }$ occupied by a given swarm of $N$ particles is independent of location along the world line of the swarm ("Liouville's theorem in curved spacetime").

(See Box 22.6 for proof.)

Number density in phase space (distribution function)

More convenient for applications than the volume $\mathcal { V }$ in phase space occupied by a given set of $N$ particles is the“number density in phase space”("distribution function") in the neighborhood of one of these particles:

$$
{ \mathcal { X } } \equiv N / { \mathcal { V } } .
$$

On what does this number density depend? It depends on the location in spacetime, ${ \mathcal P }$ ,at which the measurements are made.It also depends on the 4-momentum $\pmb { \rho }$ of the particle in whose neighborhood the measurements are made.But because the particles all have the same rest mass, $\pmb { \rho }$ cannot take on any and every value in the tangent space at $\mathcal { P }$ Rather, $\pmb { \rho }$ is confined to the “forward mass hyperboloid" at $\mathcal { P }$ ：

Thus,

$$
\mathcal { X } = \mathcal { X } \left[ \left( \begin{array} { l } { \mathrm { l o c a t i o n } , \mathcal { P } , } \\ { \mathrm { i n ~ s p a c e t i m e } } \end{array} \right) , \left( \begin{array} { l } { 4 \mathrm { - m o m e n t u m } p , \mathrm { w h i c h ~ m u s t ~ l i e } } \\ { \mathrm { o n ~ t h e ~ f o r w a r d ~ m a s s ~ h y p e r b o l o i d } } \\ { \mathrm { o f ~ t h e ~ t a n g e n t ~ s p a c e ~ a t } \mathcal { P } } \end{array} \right) \right] .
$$

Pick some one particle in the swarm,with geodesic world line $\mathcal { P } ( \lambda ) \left[ \lambda = \right.$ (affine parameter) $=$ (proper time, if particle has finite rest mass)], and with 4-momentum

Box 22.5 VOLUME IN PHASE SPACE

# A. For Swarm of Identical Particles with Nonzero Rest Mass

Pick an event $\mathcal { P } _ { 0 }$ ，through which passes a particle named“John”with a 4-momentum named $" \mathbf { \nabla } _ { \mathbf { \vec { P } } } \mathbf { \vec { \nu } } ^ { \mathbf { \vec { \nu } } }$ . In John's local Lorentz rest frame at $\mathcal { P } _ { 0 }$ ("barred frame", ${ \overline { { \mathcal { S } } } } ^ { \cdot }$ ), select a small 3-volume, $\mathcal { V } _ { z } \equiv \varDelta \bar { x } \varDelta \bar { y }$ $\pmb { \varDelta \overline { { z } } } ,$ ,containing him.Also select a small $^ { \mathfrak { s } \mathfrak { s } }$ -volume in momentum space," $\mathcal { V } _ { \bar { p } } \equiv \varDelta p ^ { \bar { x } } \varDelta p ^ { \bar { y } } \varDelta p ^ { \bar { z } }$ centered on John's momentum, which is $\dot { P } ^ { \tilde { \tau } } = P ^ { \tilde { \tau } } =$ $P ^ { \overline { { z } } } = 0 .$ Focus attention on all particles whose world lines pass through $\mathcal { V } _ { \overline { { \pmb { \varepsilon } } } }$ and which have momenta $p ^ { \dagger }$ in the range $\mathcal { V } _ { \overline { { p } } }$ surrounding $P ^ { \dagger } = 0$

![](images/1a6267e2448e4a177e830a178da5511d058f2d248d7e30dd31d665dc36690358.jpg)

Examine this bundle in another local Lorentz frame("unbarred frame",S) at ${ \mathcal { P } } _ { 0 } ,$ which moves with speed $\beta$ relative to the rest frame. Orient axes so the relative motion of the frames is in the $_ x$ and $\bar { x }$ directions. Then the space volume $\mathcal { T } _ { \pi }$ occupied in the new frame has $\varDelta y = \varDelta \bar { y }$ ， $\varDelta z = \varDelta \overline { { z } }$ (no effect of motion on transverse directions),and $\varDelta x = ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 } \varDelta \overline { { x } }$ (Lorentz contraction in longitudinal direction). Hence $\mathcal { V } _ { \varepsilon } = ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 } \mathcal { V } _ { \frac { - } { \varepsilon } }$ ("transformation law for space volumes")or, equivalently [since $P ^ { 0 } = m / ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 } ]$

$$
P ^ { 0 } \mathcal { V } _ { \overline { { x } } } = m \mathcal { V } _ { \overline { { x } } } = \binom { \mathrm { c o n s t a n t , ~ i n d e p e n d e n t } } { \mathrm { o f ~ L o r e n t z ~ f r a m e } } .
$$

![](images/512f5fa5c76c9762f1cb5517057e25852ef1ad98a41fdaf98e8fac3aa51cf36c.jpg)

A momentum-space diagram, analogous to the spacetime diagram, depicts the momentum spread for_particles in the bundle,and shows that $\varDelta p ^ { \pm } =$ $\Delta p ^ { \overline { { \tau } } } / ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 }$ .The Lorentz transformation from $\overline { { \boldsymbol { s } } }$ to $s$ leaves transverse components of momenta unaffected; so $\varDelta p ^ { y } = \varDelta p ^ { \widetilde { y } }$ ， $A p ^ { z } = 4 p ^ { \bar { z } }$ Hence $\mathcal { V } _ { p } = \mathcal { V } _ { \bar { p } } / ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 }$ ("transformation law for momentum volumes"); or, equivalently

$$
{ \frac { { \mathcal { V } } _ { p } } { P ^ { 0 } } } = { \frac { { \mathcal { V } } _ { \bar { p } } } { m } } = { \binom { { \mathrm { c o n s t a n t , ~ i n d e p e n d e n t } } } { { \mathrm { o f ~ L o r e n t z ~ f r a m e } } } } .
$$

Although the spatial 3-volumes $\mathcal { V } _ { \pmb { \varepsilon } }$ and $\mathcal { V } _ { \overline { { \pmb { \mathscr { x } } } } }$ differ from one frame to another,and the momentum 3-volumes $\mathcal { V } _ { p }$ and $\mathcal { V } _ { \overline { { p } } }$ differ, the volume in six-dimensional phase space is Lorentz-invariant:

$$
\mathcal { V } \equiv \mathcal { V } _ { \overline { { x } } } \mathcal { V } _ { \overline { { p } } } = \mathcal { V } _ { x } \mathcal { V } _ { p } .
$$

It is a frame-independent, geometric object!

# B. For Swarm of ldentical Particles with Zero Rest Mass

Examine a sequence of systems,each with particles of smaller rest mass and of higher velocity relative to a laboratory.For every bundle of particles in each system, $P ^ { \mathrm { { i } } } \mathcal { V } _ { \pi } , \mathcal { V } _ { p } / P ^ { \mathrm { { i } } }$ ,and $\mathcal { V } _ { \pmb { \mathscr { x } } } \mathcal { V } _ { \pmb { \mathscr { p } } }$ are Lorentzinvariant.Hence,in the limit as $m \longrightarrow 0$ ，as $\beta \longrightarrow 1$ ,and as $P ^ { 0 } = m / ( 1 - \beta ^ { 2 } ) ^ { 1 / 2 } \longrightarrow$ finite value (particles of zero rest mass moving with speed of light), $P ^ { 0 } \mathcal { V } _ { \pmb { x } }$ and $\mathcal { V } _ { p } / P ^ { 0 }$ and $\mathcal { V } _ { \pmb { \mathscr { s } } } \mathcal { V } _ { \pmb { \mathscr { p } } }$ are still Lorentz-invariant, geometric quantities.

Examine a very small bundle of identical particles that move through curved spacetime on neighboring geodesics. Measure the bundle's volume in phase space, $\mathcal { V }$ $( \mathcal { V } = \mathcal { V } _ { z } \mathcal { V } _ { , p }$ in any local Lorentz frame), as a function of affine parameter $\lambda$ along the central geodesic of the bundle. The following calculation shows that

$$
d \mathcal { V } / d \lambda = 0 \qquad \binom { \mathrm { { ' } L i o u v i l l e ~ t h e o r e m ~ i n } } { \mathrm { { c u r v e d ~ s p a c e t i m e } ^ { , 9 } } } .
$$

Proof for particles of finite rest mass: Examine particle motion during time interval $\delta \tau$ ,using local Lorentz rest frame of central particle. All velocities are small in this frame, so

$$
p ^ { \tilde { j } } = m d x ^ { \tilde { j } } / d \overline { { t } } .
$$

Hence (see pictures) the spreads in momentum and position conserve $\varDelta \overline { { x } } \varDelta \bar { p ^ { \bar { x } } }$ ,4y $\varDelta p ^ { \tilde { \nu } }$ ,and $\Delta \overline { { z } } \Delta p ^ { \overline { { z } } }$ ； i.e.,

$$
. \frac { d \mathcal { V } } { d \tau } = \frac { \delta ( \varDelta \overline { { x } } \varDelta \overline { { y } } \varDelta \overline { { z } } \varDelta p ^ { \overline { { x } } } \varDelta p ^ { \overline { { y } } } \varDelta p ^ { \overline { { z } } } ) } { \delta \overline { { t } } } = 0 .
$$

But $\tau = a \lambda + b$ for some arbitrary constants $^ { a }$ and$^ { b }$ ； so $, d \mathcal { V } / d \lambda = 0$

Prooffor particles of zero rest mass. Examine particle motion in local Lorentz frame where central particle has ${ \pmb P } = P ^ { 0 } ( { \pmb e } _ { 0 } + { \pmb e } _ { \tau } )$ . In this frame, all particleshave $p ^ { y } \ll p ^ { 0 }$ ， $p ^ { z } \ll p ^ { 0 }$ ， $p ^ { \pm } = p ^ { 0 } + $ ${ \cal O } ( [ p ^ { y } ] ^ { 2 } / P ^ { 0 } ) \approx P ^ { 0 }$ Since $p ^ { \alpha } = d x ^ { \alpha } / d \lambda$ for appropriate normalization of afine parameters (see Box 22.4), one can write $d x ^ { j } / d t = \dot { p } ^ { j } / p ^ { 0 }$ ； i.e.,

$$
\begin{array} { c } { { \frac { d x } { d t } = 1 + O ( [ p ^ { \nu } / P ^ { 0 } ] ^ { 2 } + [ p ^ { z } / P ^ { 0 } ] ^ { 2 } ) } } \\ { { \approx 1 , } } \end{array}
$$

![](images/884e9419cc77941f8155021cab5073bc93bfe44472fc57991034ff91e48e71ee.jpg)

![](images/42fa825272a340bcf23b97f3f5727ca234763e0c2edf5e36bd50b3547fa0caf6.jpg)

Each particle moves with speed $d \widetilde { x } / \widetilde { d t }$ proportional to height in diagram

$$
d \widetilde { x } / { \widetilde { d t } } = p ^ { \overline { { z } } } / m ,
$$

and conserves its momentum, $d p ^ { \overline { { x } } } / \widetilde { d t } = 0$ .Hence the region occupied by particles deforms,but maintains its area. Same is true for $( y - p ^ { \pmb { \nu } } )$ and $( z - p ^ { z } )$

$$
\frac { d y } { d t } = \frac { p ^ { y } } { P ^ { 0 } } , \frac { d z } { d t } = \frac { p ^ { z } } { P ^ { 0 } } .
$$

![](images/7e4a963adeb73de072722b71556546c84a0a32602dda75ddbd9538c2a36e1deb.jpg)  
Each particle("photon") moves with $d x / d t = 1$ and $d p ^ { z } / d t = 0$ in the local Lorentz frame.Area and shape of occupied region are preserved.

Hence (see pictures) $\boldsymbol { \varDelta } \boldsymbol { x } \boldsymbol { \varDelta } p ^ { \boldsymbol { \varepsilon } }$ 4y $\varDelta p ^ { y }$ and $\varDelta z \varDelta p ^ { z }$ are all conserved; and

$$
\frac { d \mathcal { V } } { d t } = \frac { \delta ( \varDelta x \varDelta y \varDelta z \varDelta p ^ { x } \varDelta p ^ { y } \varDelta p ^ { z } ) } { \delta t } = 0 .
$$

But $t$ and the affine parameter $\lambda$ of central particle are related by $t = \bar { P } ^ { 0 } \lambda$ [cf. equation (16.4); thus

$$
d \mathcal { V } / d \lambda = 0 .
$$

![](images/43649d62e44cc30d6f3c2234bbae11b6a0b346e81388012e85300e6e5cf57e3b.jpg)

Particle("photon") speedsare proportional to height in diagram

$$
\begin{array} { r } { d y / d t = p ^ { y } / P ^ { 0 } , } \end{array}
$$

and $d p ^ { y } / d t = 0$ Hence,occupied region deforms but maintains its area. Same is true of z-p.

${ \pmb \rho } ( \lambda )$ .Examine the density in phase space in this particle's neighborhood at each point along its world line:

$$
\begin{array} { r } { \mathcal { X } = \mathcal { X } [ \mathcal { P } ( \lambda ) , \pmb { p } ( \lambda ) ] . } \end{array}
$$

Calculate ${ \mathcal { R } } ( \lambda )$ as follows: (l) Pick an initial event ${ \mathcal { P } } ( 0 )$ on the world line,and a phase-space volume $\mathcal { V }$ containing the particle. (2) Cover with red paint all the particles contained in $\mathcal { V }$ at ${ \mathcal { P } } ( 0 )$ .(3) Watch the red particles move through spacetime alongside the initial particle. (4) As they move,the phase-space region they occupy changes shape extensively; but its volume $\mathcal { V }$ remains fixed (Liouville's theorem). Moreover, no particles can enter or leave that phase-space region (once in, always in; once out, always out; boundaries of phase-space region are attached to and move with the particles). (5) Hence,at any $\lambda$ along the initial particle's world line,the particle is in a phase-space region of unchanged volume $\mathcal { V }$ ,unchanged number of particles $N ,$ and unchanged ratio $\mathcal { X } = N / \mathcal { V }$ ：

$$
{ \frac { d { \mathcal { D } } \zeta [ { \mathcal { P } } ( \lambda ) , \pmb { \rho } ( \lambda ) ] } { d \lambda } } = 0 .
$$

Collisionless Boltzmann equation (kinetic equation)

This equation for the conservation of $\mathfrak { N }$ along a particle's trajectory in phase space is called the“collisionless Boltzmann equation,”or the “kinetic equation.”

Photons provide an important application of the Boltzmann equation. But when discussing photons one usually does not think in terms of the number density in phase space. Rather,one speaks of the“specific intensity" $I _ { \nu }$ of radiation at a given frequency $\nu$ ,flowing in a given direction. $\pmb { n }$ ,as measured in a specified local Lorentz frame:

$$
I _ { \nu } \equiv \frac { d ( \mathrm { e n e r g y } ) } { d ( \mathrm { t i m e } ) d ( \mathrm { a r e a } ) d ( \mathrm { f r e q u e n c y } ) d ( \mathrm { s o l i d a n g l e } ) } .
$$

Distribution function for photons expressed in terms of specific intensity, $\prime _ { \nu }$

(See Figure 22.2). A simple calculation in the local Lorentz frame reveals that

$$
{ \mathcal D } = h ^ { - 4 } ( I _ { \nu } / \nu ^ { 3 } ) ,
$$

Invariance and conservation of $I _ { \nu } / \nu ^ { 3 }$

where $\pmb { h }$ is Planck's constant (see Figure 22.2).Thus,if two different observers at the same or different events in spacetime look at the same photon (and neighboring photons) as it passes them,they will see different frequencies $\nu$ ("doppler shift," “cosmological red shift,”“gravitational redshift"),and different specific intensities $I _ { \nu }$ ; but they will obtain identical values for the ratio $I _ { \nu } / \nu ^ { 3 }$ .Thus $I _ { \nu } / \nu ^ { 3 }$ like $\mathfrak { N }$ ,is invariant from observer to observer and from event to event along a given photon's world line.

# EXERCISES

# Exercise 22.15. INVERSE SQUARE LAW FOR FLUX

The specific flux of radiation entering a telescope from a given source is defined by

$$
F _ { \nu } = \int I _ { \nu } d \Omega ,
$$

where integration is over the total solid angle (assumed $\lessleqslant 4 \pi$ ）subtended by the source on the observer's sky. Use the Boltzmann equation (conservation of $I _ { \nu } / \nu ^ { 3 } )$ to show that $F _ { \nu } \propto$ (distance from source)-² for observers who are all at rest relative to each other in flat spacetime.

# Exercise 22.16. BRIGHTNESS OF THE SUN

Does the surface of the sun look any brighter to an astronaut standing on Mercury than to a student standing on Earth?

# Exercise 22.17. BLACK BODY RADIATION

An“optically thick” source of black-body radiation (e.g.,the surface of a star,or the hot matter filling the universe shortly after the big bang) emits photons isotropically with a specific intensity,as seen by an observer at rest near the source,given (Planck radiation law） by

$$
I _ { \nu } = { \frac { 2 h \nu ^ { 3 } } { e ^ { h \nu / k T } - 1 } } .
$$

Here $T$ is the temperature of the source. Show that any observer, in any local Lorentz frame, anywhere in the universe,who examines this radiation as it flows past him,will also see a black-body spectrum. Show,further, that if he calculates a temperature by measuring the specific intensity $I _ { \nu }$ at any one frequency,and if he calculates a temperature from the shape of the spectrum, those temperatures will agree.(Radiation remains black body rather than being“diluted”into“grey-body.") Finally,show that the temperature he measures is redshifted by precisely the same factor as the frequency of any given photon is redshifted,

$$
\frac { T _ { \mathrm { { o b s e r v e d } } } } { T _ { \mathrm { { e m i t t e d } } } } = \left( \frac { \nu _ { \mathrm { { o b s e r v e d } } } } { \nu _ { \mathrm { { e m i t t e d } } } } \right) \mathrm { { f o r } \ a \ g i v e n \ p h o t o n . }
$$

[Note that the redshifts can be “Doppler”in origin,“cosmological”inorigin,“gravitational" in origin,or some inseparable mixture.Allthat matters is the fact that the parallel-transport law for a photon's 4-momentum, $\pmb { \nabla _ { p } p } = 0$ ，guarantees that the redshift $\nu _ { \mathrm { o b s e r v e d } } / \nu _ { \mathrm { e m i t t e d } }$ is independent of frequency emitted.]

![](images/ce0c45bd2f9f5b3a484167ee3dbcd930d30091b212bcf03496a671d0e56e5b26.jpg)  
3-momentum volume,with direction of momentum vectors reversed for ease of visualization (telescope as an emitter,not a receiver!)

Figure 22.2.   
Number density in phase space for photons,interpreted in terms of the specific intensity $I _ { \nu }$ An astronomer has a telescope with filter that admits only photons ariving from within a smallsolid angle $\pmb { \varDelta \pmb { \varOmega } }$ about the $z$ -direction,and having energies between $p ^ { \mathbf { 0 } }$ and $p ^ { 0 } + 4 p ^ { 0 }$ .The collecting area, $\pmb { \mathcal { q } }$ ,of his telescope lies in the $\pmb { x }$ ， $_ { y }$ -plane (perpendicular to the incoming photon beam).Let $\pmb { \delta N }$ be the number of photons that cross the area $\boldsymbol { \mathcal { Q } }$ in a time interval δt.[All energies,areas,times,and lengths are measured in the orthonormal frame ("proper reference frame; $\ S 1 3 . 6 )$ ，which the astronomer Fermi-Walker transports with himself along his (possibly accelerated） world line-or,equivalently,in a local Lorentz frame momentarily at rest with respect to the astronomer.] The $\delta N$ photons, just before the time interval $\delta t$ begins,lie in the cylinder of area $\boldsymbol { \mathcal { q } }$ and height $\delta z = \delta t$ shown above.Their spatial 3-volume is thus $\begin{array} { r } { \mathcal { V } _ { \pmb { z } } = \mathcal { Q } \delta t . } \end{array}$ Their momentum 3-volume is $\mathcal { V } _ { p } = ( p ^ { 0 } ) ^ { 2 } \varDelta p ^ { 0 } \varDelta \varOmega$ (see drawing). Hence,their number density in phase space is

$$
\begin{array} { r } { \mathcal { X } = \frac { \delta N } { \mathcal { T } _ { \mathfrak { r } } \mathcal { T } _ { \mathfrak { p } } } = \frac { \delta N } { \mathcal { T } \delta t ( \mathfrak { p } ^ { 0 } ) ^ { 2 } ( \varDelta \mathfrak { p } ^ { 0 } ) \varDelta \varOmega } = \frac { \delta N } { \mathit { h } ^ { 3 } \mathcal { Q } \delta t \nu ^ { 2 } \varDelta \nu \varDelta \varOmega } } \end{array}
$$

where ${ \pmb \nu }$ is the photon frequency measured by the telescope $( p ^ { 0 } = h \nu _ { \mathrm { \scriptscriptstyle { \perp } } }$ .

The specific intensity of the photons, $I _ { \nu }$ (a standard concept in astronomy),is the energy per unit area per unit time per unit frequency per unit solid angle crossng a surface perpendicular to the beam: i.e.,

$$
I _ { \nu } = \frac { h \nu ~ \delta N } { \textit { a } \delta \iota ~ \varDelta \nu ~ \varDelta \Omega } .
$$

Direct comparison reveals $\mathcal { X } = h ^ { - 4 } ( I _ { \nu } / \nu ^ { 3 } )$

Thus,conservation of $\boldsymbol { \mathcal { R } }$ alonga photon's world line implies conservation of $I _ { \nu } / \nu ^ { 3 }$ .This conservation lawfinds important applications in cosmology (e.g.,Box 29.2andEx.29.5)and in thegravitational lens effect (Refsdal 1964);see also exercises 22.15-22.17.

# Exercise 22.18. STRESS-ENERGY TENSOR

(a) Show that the stress-energy tensor for a swarm of identical particles at an event $\boldsymbol { \mathscr { s } } _ { 0 }$ can be written as an integral over the mass hyperboloid of the momentum space at $\mathcal { P } _ { \mathbf { 0 } }$ ：

$$
{ \pmb \tau } = \int ( \Im \pmb { \tau } { \pmb \rho } \otimes { \pmb p } ) ( d ^ { * } \pmb { \gamma } _ { \pmb { p } } / p ^ { 0 } ) ,
$$

(Notice from Box 22.5 that $d \mathcal { V } _ { p } / p ^ { 0 }$ is a Lorentz-invariant volume element for any segment of the mass hyperboloid.)

(b) Verify that the Boltzmann equation, $d \mathcal { D } / d \lambda = 0$ ,implies $\pmb { \nabla } \cdot \pmb { r } = 0$ for any swarm of identical particles.[Hint: Calculate $\mathbf { \nabla } \cdot \mathbf { \vec { r } }$ in a local Lorentz frame,using the above expression for $\pmb { \tau } ,$ and using the geodesic equation in the form $D p ^ { \mu } / d \lambda = 0 . ]$

ExerciSe 22.19. KINETIC THEORY FOR NONIDENTICAL PARTICLES

For a swarm of particles with a wide distribution of rest masses, define

$$
\mathcal { R } = \frac { \dot { \mathrm { ~ \it ~ \_ ~ } } \Delta N } { \dot { \mathcal { r } } _ { \ast } \mathcal { T } _ { \ast } \Delta m } ,
$$

where $\mathcal { V } _ { \pmb { z } }$ and $\mathcal { T } _ { p }$ are spatial and momentum 3-volumes, and $\pmb { \mathscr { A } N }$ is the number of particles in the region $\mathcal { T } _ { \texttt { z } } \mathcal { V } _ { p }$ with rest masses between $m - 4 m / 2$ and $m + \Delta m / 2$ . Show the following.

（a） $\because \gamma _ { p } \lrcorner \lrcorner m$ is independent of Lorentz frame and independent of location on the world tube of a bundle of particles.

(b) $\mathfrak { X }$ can be regarded as a function of location $\mathcal { P }$ in spacetime and 4-momentum $\pmb { \rho }$ inside the future light cone of the tangent space at $\mathcal { P }$ ：

$$
{ \mathcal { X } } = { \mathcal { X } } ( { \mathcal { P } } , { \pmb { p } } ) .
$$

(c） $\mathfrak { X }$ satisfies the collsionless Boltzmann equation (kinetic equation)

$$
{ \frac { d { \mathcal { H } } [ { \mathcal { P } } ( \lambda ) , p ( \lambda ) ] } { d \lambda } } = 0 \qquad { \mathrm { a l o n g ~ g e o d e s i c ~ t r a j e c t o r y ~ o f ~ a n y ~ p a r t i c l e . } }
$$

(d) $\mathfrak { X }$ can be rewritten in a local Lorentz frame as

$$
\mathcal { X } = \frac { A N } { [ ( p ^ { 0 } / m ) ~ 4 x ~ 4 y ~ 4 z ] [ 4 p ^ { 0 } ~ 4 p ^ { x } ~ 4 p ^ { y } ~ \varDelta p _ { . } ^ { z } ] } .
$$

(e) The stress-energy tensor at an event $\mathcal { P }$ can be written as an integral over the interior of the future light cone of momentum space

$$
T ^ { \mu \nu } = \int ( \mathcal { R } p ^ { \mu } p ^ { \nu } ) m ^ { - 1 } d p ^ { 0 } d p ^ { 1 } d p ^ { 2 } d p ^ { 3 }
$$

in a local Lorentz frame (Track-1 notation for integral; see Box 5.3);

$$
\begin{array} { l } { { \pmb { \tau } = \displaystyle \int ( \mathscr { X } { \pmb p } \otimes { \pmb p } ) m ^ { - 1 * } 1 \qquad \mathrm { i n ~ f r a m e - i n d e p e n d e n t ~ n o t a } } } \\ { { \qquad = \displaystyle \int ( \mathscr { X } { \pmb p } \otimes { \pmb p } ) m ^ { - 1 } d p ^ { 0 } \wedge d p ^ { 1 } \wedge d p ^ { 2 } \wedge d p ^ { 3 } } } \end{array}
$$

in a local Lorentz frame (Track-2 notation; see Box 5.4).

PART V

# RELATIVISTIC STARS

Wherein the reader,armed with the magic potions and powers of Geometrodynamics,conquers the stars.

CHAPTER 23

# S23.1. PROLOG

Preview of the rest of this book

Beautiful though gravitation theory may be,it is a sterile subject until it touches thereal physical world. Only the hard reality of experiments and of astronomical observations can bring gravitation theory to life. And only by building theoretical models of stars (Part V),of the universe (Part VI), of stellar collapse and black holes (Part VII), of gravitational waves and their sources (Part VII),and of gravitational experiments (Part IX),can one understand clearly the contacts between gravitation theory and reality.

The model-building in this book will follow the tradition of theoretical physics. Each Part (stars,universe,collapse,...） will begin with the most oversimplified model conceivable,and will subsequently add only those additional touches of realism necessary to make contact with the least complex of actual physical systems. The result will be a tested intellectual framework, ready to support and organize the additional complexities demanded by greater realism. Greater realism will not be attempted in this book.But the reader seeking it could start in no better place than the two-volume treatise on Relativistic Astrophysics by Zel'dovich and Novikov (1971,1974).

Begin,now,with models for relativistic stars.As a major simplification,insist (initially) that all stars studied be static. Thereby exclude not only exploding and pulsating stars,but even quiescent ones with stationary rotational motions. From the static assumption, plus a demand that the star be made of “perfect fluid" (no shear stresses allowed!), plus Einstein's field equations, it probably follows that the star is spherically symmetric. However,nobody has yet given a proof.[For proofs under more restricted assumptions,see Avez (l964) and Kunzle (l971).] In the absence of a proof,assume the result: insist that all stars studied be spherical as well as static.

Static stars must be spherical

# S23.2. COORDINATES AND METRIC FOR A STATIC. SPHERICAL SYSTEM

Metric for any static, spherical system:

To deduce the gravitational field for a static spherical star-or for any other static. spherical system--begin with the metric of special relativity (no gravity) in the spherically symmetric form

$$
d s ^ { 2 } = - d t ^ { 2 } + d r ^ { 2 } + r ^ { 2 } d \varOmega ^ { 2 } ,
$$

where

$$
d \Omega ^ { 2 } = d \theta ^ { 2 } + \mathrm { s i n } ^ { 2 } \theta d \phi ^ { 2 } .
$$

(1）generalized from flat spacetime

Try to modify this metric to allow for curvature due to the gravitational influence of the star,while preserving spherical symmetry. The simplest and most obvious guess is to allow those metric components that are already non-zero in equation (23.1) to assume different values:

$$
d s ^ { 2 } = - e ^ { 2 \phi } d t ^ { 2 } + e ^ { 2 A } d r ^ { 2 } + R ^ { 2 } d \Omega ^ { 2 } ,
$$

where $\Phi , \ A ,$ and $R$ are functions of $\pmb { r }$ only.(The static assumption demands $\partial g _ { \mu \nu } / \partial t = 0 .$ To verify that this guess is good,use it in constructing stellar models, and check that the resulting models have the same generality (same set of quantities freely specifiable) as in Newtonian theory and as expected from general physical considerations. An apparently more general metric

$$
d s ^ { 2 } = { } - a ^ { 2 } d t ^ { 2 } - 2 a b d r d t + c ^ { 2 } d r ^ { 2 } + R ^ { 2 } d \Omega ^ { 2 }
$$

actually is not more general in any physical sense. One can perform a coordinate transformation to a new time coordinate $t ^ { \prime }$ defined by

$$
e ^ { \phi } d t ^ { \prime } = a d t + b d r .
$$

By inserting this in equation (23.4),and by defining $e ^ { 2 A } \equiv b ^ { 2 } + c ^ { 2 }$ ,one obtains the postulated line element (23.3), apart from a prime on the t.\*

The necessity to allow for arbitrary coordinates in general relativity may appear burdensome when one is formulating the theory; but it gives an added flexibility, something one should always try to turn to one's advantage when formulating and solving problems. The $g _ { r t } = 0$ simplification (called a coordinate condition) in equation (23.3) results from an advantageous choice of the $t$ coordinate. The $r$ coordinate, however, is also at one's disposal (as long as one chooses it in a way that respects spherical symmetry; thus not $r ^ { \prime } = r + \cos \theta$ ).One can turn this freedom to advantage by introducing a new coordinate $r ^ { \prime } ( r )$ defined by

$$
r ^ { \prime } = R ( r ) .
$$

With this choice of the radial coordinate, and with the primes dropped, equation (23.3） reduces to

$$
d s ^ { 2 } = { } - e ^ { 2 \phi } d t ^ { 2 } + e ^ { 2 A } d r ^ { 2 } + r ^ { 2 } d \Omega ^ { 2 } ,
$$

a line element with just two unknown functions, $\pmb { \phi } ( \pmb { r } )$ and $\boldsymbol { A } ( \boldsymbol { r } )$ .This coordinate system and metric have been used in most theoretical models for relativistic stars since the pioneering work of Schwarzschild (l916b),Tolman (1939),and Oppenheimer and Volkoff (1939). These particular coordinates are sometimes called “curvature coordinates”and sometimes “Schwarzschild coordinates.”The central idea of these coordinates, in a nutshell, is (Schwarzschild $\pmb { r }$ -coordinate) $=$ (proper circumference)/ $n \pi$

For a more rigorous proof that in any static spherical system Schwarzschild coordinates can be introduced, bringing the metric into the simple form (23.7), see Box 23.3 at the end of this chapter.

(3) derived more rigorously

# Exercise 23.1. ISOTROPIC COORDINATES AND NEWTONIAN LIMIT

# EXERCISE

An alternative set of coordinates sometimes used for static,spherical systems is the “isotropic coordinate system” $( t , \widetilde { r } , \theta , \phi )$ . The metric in isotropic coordinates has the form

$$
d s ^ { 2 } = - e ^ { 2 \phi } d t ^ { 2 } + e ^ { 2 \mu } [ d \overline { { { r } } } ^ { 2 } + \overline { { { r } } } ^ { 2 } d \Omega ^ { 2 } ] ,
$$

with $\pmb { \phi }$ and $\mu$ being functions of $\widetilde { \pmb { r } } .$

(a)Exhibit the coordinate transformation connecting the Schwarzschild coordinates (23.7) to the isotropic coordinates (23.8).

(b) From equation (l6.2a) [or equivalently (18.15c)],show that, in the Newtonian limit, the metric coefficient $\pmb { \phi }$ of the isotropic line element becomes the Newtonian potential;and $\mu$ becomes equal to $- \tilde { \phi }$ 、By combining with part (a),discover that $\Lambda = r d \tilde { \phi } / d r$ in the Newtonian limit.

# $\$ 23.3$ .PHYSICAL INTERPRETATION OF SCHWARZSCHILD COORDINATES

In general relativity, because the use of arbitrary coordinates is permitted,the physical significance of statements about tensor or vector components and other quantities is not always obvious.There are, however, some situations where the interpretation is almost as straightforward as in special relativity. The most obvious example is the center point of a local inertial coordinate system,where the principle of equivalence allows one to treat all local quantities (quantities not involving spacetime curvature） exactly as in special relativity. Schwarzschild coordinates for a spherical system turn out to be a second example.

One's first reaction when meeting a new metric should be to examine it,not in order to learn about the gravitational field,for which the curvature tensor is more

The form of any metric can reveal the nature of the coordinates being used

directly informative, but to learn about the coordinates. (Are they,for instance, locally inertial at some point?)

Geometric significance of the Schwarzschild coordinates:

(1) $\theta , \phi$ are angles on sphere

The names given to the coordinates have no intrinsic significance.A coordinate transformation $t ^ { \prime } = \theta , r ^ { \prime } = \phi , \theta ^ { \prime } = r , \phi ^ { \prime } = t$ is perfectly permissible,and has no influence on the physics or the mathematics of a relativistic problem. The only thing it affects is easy communication between the investigator who adopts it and his colleagues. Thus the names $t r \theta \phi$ for the Schwarzschild coordinates (23.7） provide a mnemonic device pointing out the geometric content of the coordinates.\* In particular,the names $\theta , \phi$ are justified by the fact that on each two-dimensional surface of constant $r$ and $t$ ，the distance between two nearby events is given by $d s ^ { 2 } = r ^ { 2 } d \varOmega ^ { 2 }$ ,as befits standard $\theta , \phi$ coordinates on a sphere of radius $\boldsymbol { r } ,$ The area of this two-dimensional sphere is clearly

$$
A = \int ( r d \theta ) ( r \sin \theta d \phi ) = 4 \pi r ^ { 2 } ;
$$

(2)r measures surface area of sphere

hence,the metric (23.7) tels how to measure the $r$ coordinate that it employs. One can merely measure (in proper length units) the area $\pmb { A }$ of the sphere, composed of all points rotationally equivalent to the point $\mathcal { P }$ for which the value $r ( \mathcal { P } )$ is desired; and one can then calculate

$$
r ( \mathcal { P } ) = \binom { \mathrm { p r o p e r ~ a r e a ~ o f ~ s p h e r e } } { \mathrm { t h r o u g h ~ p o i n t } ~ \mathcal { P } } 4 \pi \bigg ) ^ { 1 / 2 } .
$$

(3) t has 3 special geometric properties

The Schwarzschild coordinates have been picked for convenience,and not for the ease with which one could build a coordinate-measuring machine. This makes it more difficult to design a machine to measure $t$ than machines to measure $r , \theta , \phi$

The geometric properties of $t$ on which a measuring device can be based are: (l） the time-independent distances $( \partial g _ { \alpha \beta } / \partial t = 0 )$ ）between world lines of constant $r , \theta , \phi ^ { \prime }$ （2）the orthogonality $( g _ { t \tau } = g _ { t \theta } = g _ { t \phi } = 0 )$ of these world lines to the $t =$ constant hypersurfaces；and (3)a labeling of these hypersurfaces by Minkowski (special relativistic) coordinate time at spatial infinity,where spacetime becomes flat. This labeling produces a constraint

$$
\bar { \pmb { \phi } } ( \infty ) = 0
$$

(4) description of a "machine" to measure t

in the metric (23.7).[Mathematically,this constraint is imposed by a simple rescaling transformation $t ^ { \prime } = e ^ { \phi ( \infty ) } t$ ,and by then dropping the prime.]

One“machine” design which constructs (mentally) such a t coordinate, and in the process measures it, is the following. Observers using radar sets arrange to move along the coordinate lines $r , \theta , \phi = \mathrm { c o n s t }$ They do this by adjusting their velocities until each finds that the radar echos from his neighbors,or from“benchmark” reference points in the asymptotically flat space, require the same round-trip time at each repetition. Equivalently, each returning echo must show zero doppler shift;

it must return with the same frequency at which it was sent out. Next a master clock is set up near spatial infinity (far from the star). It is constructed to measure proper time-which, for it, is Minkowski time “at infinity”-and to emit a standard one-Hertz signal. Each observer adjusts the rate of his“coordinate clock”to beat in time with the signals he receives from the master clock.To set the zero of his“coordinate clock,”now that its rate is correct, he synchronizes with the master clock, taking account of the coordinate time At required for radar signals to travel from the master to him.[To compute the transit time, he assumes that for radar signals (treflection - $t _ { \mathrm { e m i s s i o n } } ) = ( t _ { \mathrm { r e t u r n } } - t _ { \mathrm { r e f l e c t i o n } } ) = \varDelta t _ { \mathrm { : } }$ ,so that the echo is obtained by time-inversion about the reflection event. This time-reversal invariance distinguishes the time $t$ in the metric (23.7) from the more general $t$ coordinates allowed by equation (23.4).] Each observer moving along a coordinate line $( r , \theta , \phi =$ const.) now has a clock that measures coordinate time $t$ in his neighborhood.

The above discussion identifies the Schwarzschild coordinates of equation (23.7) by their intrinsic geometric properties. Not only are $r$ and $t$ radial and time variables, respectively (in that $\partial / \partial r$ and $\partial / \partial t$ are spacelike and timelike, respectively, and are orthogonal also to the spheres defined by rotational symmetry), but they have particular properties $\scriptstyle \left[ 4 \pi r ^ { 2 } \right. =$ surface area; $\partial g _ { \mu \nu } / \partial t = 0$ ； $\partial / \partial r \cdot \partial / \partial t = g _ { r t } = 0$ $\partial / \partial t \cdot \partial / \partial t = g _ { t t } = - 1$ at $r = \infty ]$ that distinguish them from other possible coordinate choices $[ r ^ { \prime } = f ( r )$ ， $t ^ { \prime } = t + F ( r ) \}$ . No claim is made that these are the only coordinates that might reasonably be called $r$ and $t$ ；for an alternative choice ("isotropic coordinates"),see exercise 23.1. However,they provide a choice that is reasonable,unambiguous,useful,and often used.

Other coordinates are possible，but Schwarzschild are particularly simple

# \$23.4. DESCRIPTION OF THE MATTER INSIDE A STAR

To high precision, the matter inside any star is a perfect fluid. (Shear stresses are negligible, and energy transport is negligible on a“hydrodynamic time scale.") Thus, it is reasonable in model building to describe the matter by perfect-fluid parameters:

$$
\begin{array} { r l } & { \rho = \rho ( r ) = \mathrm { d e n s i t y ~ o f ~ m a s s - e n e r g y ~ i n ~ r e s t - f r a m e ~ o f ~ f l u i d } ; } \\ & { p = p ( r ) = \mathrm { i s o t r o p i c ~ p r e s s u r e ~ i n ~ r e s t - f r a m e ~ o f ~ f l u i d } ; } \\ & { n = n ( r ) = \mathrm { n u , b e r ~ d e n s i t y ~ o f ~ b a r y o n s ~ i n ~ r e s t - f r a m e ~ o f ~ f l u i d } ; } \end{array}
$$

$u ^ { \mu } = u ^ { \mu } ( r ) = 4$ -velocity of fluid;

$$
T ^ { \mu \nu } = ( \rho + p ) u ^ { \mu } u ^ { \nu } + p g ^ { \mu \nu } = { \mathrm { s t r e s s - e n e r g y ~ t e n s o r ~ o f ~ f l u i d } } .
$$

(For Track-1 discussion,see Box 5.1; for greater Track-2 detail, see $\ S 8 2 2 . 2$ and 22.3.) In order that the star be static, each element of fluid must remain always at rest in the static coordinate system; i.e., each element must move along a world line of constant $r , \theta , \phi$ ； i.e., each element must have 4-velocity components

$$
u ^ { \tau } = d r / d \tau = 0 , \quad \quad u ^ { \theta } = d \theta / d \tau = 0 , \quad \quad u ^ { \phi } = d \phi / d \tau = 0 .
$$

Material inside star to be idealized as perfect fluid

Parameters describing perfect fluid:

(1) $\rho , p , n$

The normalization of 4-velocity,

$$
- 1 = \pmb { u } \cdot \pmb { u } = g _ { \mu \nu } u ^ { \mu } u ^ { \nu } = g _ { t t } u ^ { t } u ^ { t } = - e ^ { 2 \phi } u ^ { t } u ^ { t } ,
$$

then determines $u ^ { t }$

$$
u ^ { t } = d t / d \tau = e ^ { - \phi } , ~ \pmb { \upsilon } = e ^ { - \phi } \partial / \partial t ;
$$

and this, together with the general form (23.12) of the stress-energy tensor and the form (23.7) of the metric, determines $T ^ { \mu \nu }$ ：

$$
\begin{array} { c c c } { { T ^ { 0 0 } = \rho e ^ { - 2 \phi } , } } & { { T ^ { r r } = p e ^ { - 2 A } , } } & { { T ^ { \theta \theta } = p r ^ { - 2 } , } } \\ { { } } & { { } } & { { T ^ { \alpha \beta } = 0 \mathrm { i f } \alpha \not = \beta . } } \end{array} \quad T ^ { \phi \phi } = p r ^ { - 2 } \sin ^ { - 2 } \theta ,
$$

Although these components of the stress-energy tensor in Schwarzschild coordinates are useful for calculations, the normalization factors $e ^ { - 2 \phi } , e ^ { - 2 A } , r ^ { - 2 } , r ^ { - 2 } \sin ^ { - 2 } \theta$ make them inconvenient for physical interpretations. More convenient are components on orthonormal tetrads carried by the fluid elements ("proper reference frames"; see $\ S 1 3 . 6 )$ ：

Proper reference frame of fluid

$$
\pmb { e } _ { \hat { \imath } } \equiv \frac { d } { d \tau } = \frac { 1 } { e ^ { \phi } } \frac { \partial } { \partial t } , \pmb { e } _ { \hat { \imath } } = \frac { 1 } { e ^ { A } } \frac { \partial } { \partial r } , \pmb { e } _ { \hat { \imath } } = \frac { 1 } { r } \frac { \partial } { \partial \theta } , \pmb { e } _ { \hat { \imath } } = \frac { 1 } { r \sin \theta } \frac { \partial } { \partial \phi } ;
$$

$$
\begin{array} { r } { \omega ^ { \hat { t } } = e ^ { \phi } d t , \qquad \omega ^ { \hat { r } } = e ^ { A } d r , \qquad \omega ^ { \hat { \theta } } = r d \theta , \qquad \omega ^ { \hat { \phi } } = r \sin \theta d \phi ; } \end{array}
$$

Components of $\pmb { u }$ and $\pmb { \tau }$ in proper reference frame

$$
\begin{array} { l l l } { { \pmb { u } = \pmb { e } _ { \hat { t } } ; } } & { { ~ \pmb { u } ^ { \hat { t } } = 1 , } } & { { ~ \pmb { u } ^ { \hat { \tau } } = u ^ { \hat { \theta } } = u ^ { \hat { \phi } } = 0 ; } } \end{array}
$$

$$
T _ { \hat { t } \hat { t } } \equiv T _ { \hat { 0 } \hat { 0 } } = \rho , \qquad T _ { \hat { r } \hat { r } } = T _ { \hat { \theta } \hat { \theta } } = T _ { \hat { \phi } \hat { \phi } } = p , \qquad T _ { \hat { \alpha } \hat { \beta } } = 0 \mathrm { ~ i f ~ } \alpha \neq \beta .
$$

See exercise 23.2 below.

The structure of a star--i.e., the set of functions ${ \Phi ( \boldsymbol { r } ) } , \ A ( \boldsymbol { r } ) , \ \rho ( \boldsymbol { r } ) , \ p ( \boldsymbol { r } ) , \ n ( \boldsymbol { r } )$ -is determined in part by the Einstein field equations, $G ^ { \mu \nu } = 8 \pi T ^ { \mu \nu }$ ,and in part by the law of local conservation of energy-momentum in the fluid, $T ^ { \mu \nu } { } _ { ; \nu } = 0$ .However, these are not sufficient to fix the structure uniquely. Also necessary is the functional dependence of pressure $p$ and density $\pmb { \rho }$ on number density of baryons $\pmb { n }$ ：

$$
p = p ( n ) , \qquad \rho = \rho ( n ) .
$$

Equation of state: (1)in general

Normally one cannot deduce $p$ and $\pmb { \rho }$ from a knowledge solely of $\pmb { n }$ . One must know, in addition, the temperature $T$ or the entropy per baryon $\pmb { s }$ ；then the laws of thermodynamics plus equations of state will determine all remaining thermodynamic variables:

$$
p = p ( n , s ) , \rho = \rho ( n , s ) , . . . . .
$$

(2) idealized to "one-parameter form" $p = p ( n ) , \rho = \rho ( n )$ ，

(See $\ S 2 2 . 2$ and $\mathbf { B o x } 2 2 . 1$ for full Track-2 discussions.) To pass from the given thermodynamic knowledge, $p ( n , s )$ and $\rho ( n , s )$ ,to the desired knowledge, $p ( n )$ and $\rho ( n )$ ,one needs information about the star's thermal properties,and especially about the way in which energy-generation plus heat flow have conspired to distribute the entropy, $s = s ( n )$ ：

$$
p ( n ) = p [ n , s ( n ) ] , \qquad \rho ( n ) = \rho [ n , s ( n ) ] .
$$

There exist three important applications of the theory of relativistic stars: neutron stars,white dwarfs,and supermassive stars (stars with $M \gtrsim 1 0 ^ { 3 } M _ { \odot }$ ，which may exist according to theory, but the existence of which has never yet been confirmed by observation). In all three cases, happily, the passage from $\begin{array} { r } { p = p ( n , s ) , \rho ( n , s ) , } \end{array}$ to $p = p ( n )$ ， $\rho = \rho ( n )$ ，is trivial.

Justification for idealized equation of state:

Consider first a neutron star. Though hot by ordinary standards,a neutron star is so cold by any nuclear-matter scale of temperatures that essentially all its thermal degrees of freedom are frozen out ("degenerate gas";“quantum fluid"). It is not important that a detailed treatment of the substance of a neutron star is beyond the capability of present theory (allowance for the interaction between baryon and baryon; production at sufficiently high pressures of hyperons and mesons). The simple fact is that one is dealing with matter at densities comparable to the density of matter in an atomic nucleus $( 2 \times 1 0 ^ { 1 4 } \mathrm { g } / \mathrm { c m } ^ { 3 } )$ and higher. Everything one knows about nuclear matter [see,for example, Bohr and Mottelson (1969)] tells one that it is degenerate, and that one can estimate in order of magnitude its degeneracy temperature by treating it as though it were an ideal Fermi neutron gas. (In a normal atomic nucleus,a little more than 5O per cent of all baryons are neutrons, the rest are protons; in a neutron star, as many as 99 per cent are neutrons.) When approximating the neutron-star matter as an ideal Fermi neutron gas,one considers the neutrons to occupy free-particle quantum states, with two particles of opposite spin in each occupied state, and a sharp drop from lOo per cent occupancy of quantum states to empty states when the particle energy rises to the level of the“Fermi energy” [for more on such an ideal Fermi gas, see Kittel, Section 19 (l958); or at an introductory level, see Sears, Section l6-5 (1953)]. In matter at nuclear density, the Fermi energy is of the order

(1) in neutron stars

$$
E _ { \mathrm { F e r m i } } \sim 3 0 ~ \mathrm { M e V ~ o r } ~ 3 \times 1 0 ^ { 1 1 } \mathrm { K } ;
$$

and at higher density the temperature required to unfreeze the degeneracy is even greater. In other words, for matter at and above nuclear densities, already at zero temperature the kinetic energy of the particles (governed by the Pauli exclusion principle and by their Fermi energy) is a primary source of pressure. Nuclear forces make a large correction to this pressure, but for $T \lesssim 3 0 ~ \mathrm { M e V } = 3 \times 1 0 ^ { 1 1 } \mathrm { K } .$ energies of thermal agitation do not.

A star, in collapsing from a normal state to a neutron-star state (see Chapter 24), emits a huge flux of neutrinos at temperatures $\gtrsim 1 0 ^ { 1 0 } \mathrm { K }$ ，and thereby cools to $T \ll 3 \times 1 0 ^ { 1 1 } \mathrm { K }$ within a few seconds after formation. Consequently, in all neutron stars older than a few seconds one can neglect thermal contributions to the pressure and density; i.e.,one can set

$$
p ( n , s ) = p ( n , s = 0 ) = p ( n ) , \qquad \rho ( n , s ) = \rho ( n , s = 0 ) = \rho ( n ) .
$$

A white dwarf is similar, except that here electrons rather than neutrons are the (2) in white dwarfs source of Fermi gas pressure and degeneracy. Typical white-dwarf temperatures satisfy

$$
k T \leqslant E _ { \mathrm { F e r m i e l e c t r o n s } } ;
$$

the Fermi kinetic energy (Pauli exclusion principle),and not random $k T$ energy, is primarily responsible for the pressure and energy density; and one can set

$$
p ( n , s ) = p ( n , s = 0 ) = p ( n ) , \qquad \varrho ( n , s ) = \rho ( n , s = 0 ) = \rho ( n ) .
$$

(3) in supermassive stars

In a supermassive star (see Chapter 24), the situation is quite different. There temperature and entropy are almost the whole story,so far as pressure and energy density are concerned. However, convection keeps the star stirred up and produces a uniform entropy distribution

so one can write

$$
\begin{array} { r l } & { p ( n , s ) = p _ { s } ( n ) , \qquad \quad \rho ( n , s ) = \rho _ { s } ( n ) . } \\ & { \qquad \quad  \begin{array} { l } { \mathrm { f u n c t i o n s ~ d e p e n d i n g ~ o n } } \\ { \mathrm { u n i f o r m ~ e n t r o p y ~ p e r ~ b a r y o n } , } \\ { s , \mathrm { i n ~ t h e ~ s t a r } } \end{array}  } \end{array}  ^ { \mathrm { ~ \tiny ~ \cdot ~ } }
$$

In all three cases-neutron stars,white dwarfs,supermassive stars-one regards the relations $p ( n )$ and ${ \pmb \rho } ( n )$ as “equations of state";and having specified them, one can calculate the star's structure without further reference to its thermal properties.

# EXERCISE

# Exercise 23.2. PROPER REFERENCE FRAMES OF FLUID ELEMENTS

(a) Verify that equations (23.15a,b)define an orthonormal tetrad and its dual basis of1-forms,   
at each event in spacetime. (b) Verify that the components of the fluid 4-velocity relative to these tetrads are given   
by equations (23.15c). Why do these components guarantee that the tetrads form“proper   
reference frames” for the fluid elements? (c) Verify equations (23.15d) for the components of the stress-energy tensor.

# $\$ 23.5$ .EQUATIONS OF STRUCTURE

Five equations needed to determine 5 stellar-structure functions: $\pmb { \phi }$ A $p$ p.n

The structure of a relativistic star is determined by five functions of radius $r$ the metric functions $\varPhi ( r ) , A ( r )$ ，the pressure $p ( r ) .$ ，the density of mass-energy $\rho ( r )$ and the number density of baryons, $n ( r )$ 、Hence,to determine the structure uniquely, one needs five equations of structure, plus boundary conditions. Two equations of structure, the equations of state $p ( n )$ and $\rho ( n )$ ,are already in hand.The remaining three must be the essential content of the Einstein field equations and of the law of local energy-momentum conservation, $T ^ { \mu \nu } { } _ { ; \nu } = 0$

One knows that the law of local energy-momentum conservation for the fluid follows as an identity from the Einstein field equations.Without loss of information, one can therefore impose all ten field equations and ignore local energy-momentum conservation. But that is an inefficient way to proceed. Almost always the equations $T ^ { \mu \nu } { } _ { ; \nu } = 0$ can be reduced to usable form more easily than can the field equations. Hence, the most efficient procedure is to: (l) evaluate the four equations $T ^ { \mu \nu } { } _ { ; \nu } = 0$ (2) evaluate enough field equations (six) to obtain a complete set $( 6 + 4 = 1 0 )$ ； and (3） evaluate the remaining four field equations as checks of the results of (1) and (2).

The Track-2 reader has learned (S22.3) that the equations $T ^ { \mu \nu } { } _ { ; \nu } = 0$ for a perfect fluid take on an especially simple form when projected (l) on the 4-velocity ${ \pmb u }$ of the fluid itself,and (2) orthogonal to u. Projection along u $( u _ { \mu } { T ^ { \mu \nu } } _ { ; \nu } = 0 )$ gives the local law of energy conservation (22.1la),

The most efficient procedure for solving Einstein equations

$$
\frac { d \rho } { d \tau } = - ( \rho + p ) \pmb { \nabla } \cdot \pmb { u } = \frac { \rho + p } { n } \frac { d n } { d \tau } ,
$$

where $\pmb { \upsilon } = d / d \tau$ ;i.e., $\tau$ is proper time along the world line of any chosen element of the fluid.For a static star, or for any other static system, both sides of this equation must vanish identically (no fluid element ever sees any change in its own density).

Projection of $T ^ { \mu \nu } { } _ { ; \nu } = 0$ orthogonal to $\pmb { u }$ gives the reasonable equation

Equation of hydrostatic equilibrium derived

$$
{ \begin{array} { r l } & { { \mathrm { ( i n e r t i a l ~ m a s s } } } \\ & { { \mathrm { \backslash p e r ~ u n i t ~ v o l u m e } } } \end{array} } ) \cdot { \mathrm { ( 4 - a c c e l e r a t i o n ) } } = \ - ( { \begin{array} { l } { { \mathrm { p r e s s u r e ~ g r a d i e n t , ~ p r o j e c t e d } } } \\ { { \mathrm { p e r p e n d i c u l a r ~ t o ~ } } u } \end{array} } )
$$

i.e.,

$$
( \rho + p ) \pmb { \nabla } _ { \pmb { u } } \pmb { u } = - [ \pmb { \nabla } p + ( \pmb { \nabla } _ { \pmb { u } } p ) \pmb { u } ] .
$$

[see equation (22.13)]. When applied to a static star, this equation tells how much pressure gradient is needed to prevent a fluid element from falling. Only the radial component of this equation has content, since the pressure depends only on $r$ The radial component in.the Schwarzschild coordinate system says [see the line element (23.7) and the 4-velocity components (23.13)],

$$
\begin{array} { c } { { ( \rho + p ) u _ { r ; \nu } u ^ { \nu } = - ( \rho + p ) { \cal T } ^ { \alpha } { } _ { r \nu } u _ { \alpha } u ^ { \nu } = - ( \rho + p ) { \cal T } ^ { 0 } { } _ { r 0 } u _ { 0 } u ^ { 0 } } } \\ { { = ( \rho + p ) \varPhi _ { , r } = - p { } _ { , r } . } } \end{array}
$$

(Track-l readers can derive this from scratch at the end of the section, exercise 23.3.) In the Newtonian limit,Φ becomes the Newtonian potential (since goo = -e2+ = -1 - 2Φ), and the pressure becomes much smaller than the mass-energy density; consequently equation (23.17) becomes

$$
\rho \tilde { \phi } _ { , \tau } = - p _ { , \tau } .
$$

This is the Newtonian version of the equation describing the balance between gravitational force and pressure gradient.

The pressure gradient that prevents a fluid element from falling appears in Einstein's theory as the source of an acceleration. This acceleration, by keeping the fluid element at a fixed $r$ value, causes it to depart from geodesic motion (from “fiducial world line"; from motion of free fall into the center of the star). Newtonian

Comparison of Newton and Einstein views of hydrostatic equilibrium

theory,on the other hand,views as the fducial world line the one that stays at a fixed $r$ value. It regards the “gravitational force” as trying (without success, because balanced by the pressure gradient) to pull a particle from a fixed- $\cdot r$ world line onto a geodesic world line. In the two theories the magnitudes of the acceleration, whether “actually taking place” (Einstein theory） or “trying to take place”(Newtonian theory),are the same to lowest order (but opposite in direction); so it is no surprise that (23.17) and (23.17N) differ only in detail.

Turn next to the Einstein field equation. Here,as is often the case, the components of the field equation in the fuid's orthonormal frame [equations (23.15a,b)] are simpler than the components in the coordinate basis. One already knows the stressenergy tensor $T _ { \hat { \alpha } \hat { \beta } }$ in the orthonormal frame [equation (23.15d)]; and Track-2 readers have already calculated the Einstein tensor $G _ { \hat { \alpha } \hat { \beta } }$ (exercise 14.13; Track-1 readers will face the task at the end of this section, exercise 23.4). All that remains is to equate $G _ { \hat { \alpha } \hat { \beta } }$ t0 $8 \pi T _ { \hat { \alpha } \hat { \beta } }$ . Examine first the O0 component of the field equations:

$$
\begin{array} { r l } & { G _ { \hat { 0 } \hat { 0 } } = r ^ { - 2 } - r ^ { - 2 } e ^ { - 2 A } - r ^ { - 1 } ( d / d r ) ( e ^ { - 2 A } ) } \\ & { \qquad = r ^ { - 2 } ( d / d r ) [ r ( 1 - e ^ { - 2 A } ) ] = 8 \pi T _ { \hat { 0 } \hat { 0 } } = 8 \pi \rho . } \end{array}
$$

This equation becomes easy to solve as soon as one notices that it is a differential equation linear in the quantity $e ^ { - 2 A }$ ； a bit of tidying up then focuses attention on the quantity $r ( 1 - e ^ { - 2 A } )$ . Give this quantity the name $2 m ( r )$ (so far only a name!); thus,

$$
2 m \equiv r ( 1 - e ^ { - 2 A } ) ; ~ e ^ { 2 A } = ( 1 - 2 m / r ) ^ { - 1 } .
$$

In this notation the O0 component of the Einstein tensor becomes

$$
G _ { \hat { 0 } \hat { 0 } } = \frac { 2 } { r ^ { 2 } } \frac { d m ( r ) } { d r } = 8 \pi \rho .
$$

Integrate and find

$$
m ( r ) = \int _ { 0 } ^ { r } 4 \pi r ^ { 2 } \rho d r + m ( 0 ) .
$$

For the constant of integration $m ( 0 )$ ,a zero value means a space geometry smooth at the origin (physically acceptable); a non-zero value means a geometry with a singularity at the origin (physically unacceptable: no local Lorentz frame at $r = 0$ ：

$$
\begin{array} { r l r } { d s ^ { 2 } = [ 1 - 2 m ( 0 ) / r ] ^ { - 1 } d r ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) } \\ { } & { } & { \approx - [ r / 2 m ( 0 ) ] d r ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) ~ \mathrm { a t } r \approx 0 \mathrm { i f } m ( 0 ) \ne 0 ; } \\ { } & { } & { d s ^ { 2 } = [ 1 - ( 8 \pi / 3 ) \rho _ { c } r ^ { 2 } ] ^ { - 1 } d r ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) } \\ { } & { } & { \approx d r ^ { 2 } + r ^ { 2 } ( d \theta ^ { 2 } + \sin ^ { 2 } \theta d \phi ^ { 2 } ) ~ \mathrm { a t } r \approx 0 \mathrm { i f } m ( 0 ) = 0 . } \end{array}
$$

The quantity $m ( r )$ ，defined by equation (23.18) and calculated from equation (23.19) with $m ( 0 ) = 0$ ,is a relativistic analog of the“mass-energy inside radius $r$ ” Box 23.1 spells out the analogy in detail.

# Box 23.1 MASS-ENERGY INSIDE RADIUS r

The total mass-energy $M$ of an isolated star is well-defined (Chapter l9). But not well-defined,in general, is the distribution of that mass-energy from point to point inside the star and in its gravitational field (no unique “gravitational stress-energy tensor"). This was the crucial message of $\ S 2 0 . 4$ (Track 2).

The message is true-in general.But for the case of a spherical star-and only for that case-the message loses its bite. Spherical symmetry allows one to select a distribution of the total mass-energy that is physically reasonable.In Schwarzschild coordinates, it is defined by

$$
{ } ^ { \mathrm { * } } \mathrm { t o t a l ~ m a s s - e n e r g y ~ i n s i d e ~ r a d i u s ~ } r ^ { \prime } \equiv m ( r ) = \int _ { 0 } ^ { r } 4 \pi r ^ { 2 } \rho ~ d r .
$$

The fully convincing argument for this definition is found only by considering a generalization of it to time-dependent spherically symmetric stars (pulsating, collapsing,or exploding stars; see Chapters 26 and 32,and especially exercise 32.7). For them one finds that the mass-energy m associated with a given ball of matter (fixed baryon number) can change in time only to the extent that locally measurable energy fluxes can be detected at the boundary of the ball.[Such energy fluxes could be the power expended by pressure forces against the moving boundary surface, or heat fluxes,or radiation (photon or neutrino) fluxes.But since spherically symmetric gravitational waves do not exist (Chapters 35 and 36), neither physical intuition nor Einstein's equations require that problems oflocalizing gravitational-wave energy be faced.] Thus the energy m is localized, not by a mathematical convention, but by the circumstance that transfer of energy (with this definition of $m$ ）is detectable by local measurements.[For the mathematical details of $m ( r , t )$ in the time-dependent case,see Misner and Sharp (1964), Misner (l965),and exercise 32.7.]

In addition to the critical “local energy flux” property of $m ( r )$ described above, there are three further properties that verify its identification as mass-energy. They are:(l） Everywhere outside the star

$$
m ( r ) = M \equiv { \binom { \mathrm { t o t a l ~ m a s s - e n e r g y ~ o f ~ s t a r ~ a s ~ m e a s u r e d ~ f r o m } } { \mathrm { K e p l e r ' s ~ t h i r d ~ l a w ~ f o r ~ d i s t a n t ~ p l a n e t s } } } ;
$$

see $\ S 2 3 . 6$ for proof. (2) For a Newtonian star, where “mass inside radius $r ^ { , , }$ has a unique meaning, $m ( r )$ is that mass.(3) For a relativistic star, $m ( r )$ splits nicely into “rest mass-energy" $m _ { 0 } ( r )$ plus “internal energy” $U ( r )$ plus “gravitational potential energy” $\varOmega ( r )$

To recognize and appreciate the split

$$
m ( r ) = m _ { 0 } ( r ) + U ( r ) + \varOmega ( r ) ,
$$

proceed as follows. First split the total density of mass-energy, $\pmb { \rho }$ , into a part $\mu _ { 0 } n$ due to rest mass--where $\mu _ { 0 }$ is the average rest mass of the baryonic species pres-