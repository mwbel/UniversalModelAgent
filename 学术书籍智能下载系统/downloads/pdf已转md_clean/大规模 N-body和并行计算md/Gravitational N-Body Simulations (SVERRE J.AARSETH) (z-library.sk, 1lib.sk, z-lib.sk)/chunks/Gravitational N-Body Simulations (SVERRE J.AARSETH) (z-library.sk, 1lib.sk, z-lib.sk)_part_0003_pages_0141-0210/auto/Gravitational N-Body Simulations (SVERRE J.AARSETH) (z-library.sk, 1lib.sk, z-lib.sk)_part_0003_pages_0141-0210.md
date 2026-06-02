Next we turn to the more general case of King [1966] models with varying central density contrast. The basic models are characterized by isotropic velocities, subject to a local truncation at the escape velocity. However, the King–Michie [1963] models include a velocity anisotropy and are more appropriate for realistic cluster simulations. The distribution function can be written in the convenient form [Binney $\&$ Tremaine, 1987]

$$
f ( E , { \bf J } ) = \frac { \rho _ { 1 } } { ( 2 \pi \sigma ^ { 2 } ) ^ { 3 / 2 } } \exp \left( - \frac { J ^ { 2 } } { 2 r _ { a } ^ { 2 } \sigma ^ { 2 } } \right) \left[ \exp \left( - \frac { E } { \sigma ^ { 2 } } \right) - 1 \right] ,
$$

where $\mathbf { J }$ here is the specific angular momentum, $r _ { \mathrm { a } }$ is the anisotropy radius and $\rho _ { 1 }$ is the normalization of the density obtained by integrating over velocities with dispersion $\sigma$ . Hence in the limit $r _ { \mathrm { a } } \to \infty$ this expression reduces to the standard King model. Moreover, from the separable form, it can be seen that at large distances orbits of high angular momentum are deficient, thereby giving rise to velocity anisotropy for isolated systems. More than 30 years ago, preferentially eccentric orbits were also observed outside the half-mass radius of the Pleiades [Jones, 1970].

Until recently, anisotropic velocity distributions have been little used in simulations although detailed models with rotation for the orbit–averaged Fokker–Planck method have been presented [Einsel & Spurzem, 1999]. An early study employed King–Michie models to analyse 111 radial velocities in the globular cluster M3 [Gunn & Griffin, 1979]. Evidence for velocity anisotropy and mass segregation was obtained by a consistent iteration technique. A more general formulation introduced the additional factor $\exp ( - \gamma J _ { z } )$ in (8.10) to describe solid-body rotation in the core [Lupton $\&$ Gunn, 1987]. In this treatment, $E , J ^ { 2 }$ and $J _ { z }$ are assumed to be integrals of the motion but, because of the non-spherical potential, $J ^ { 2 }$ is only an approximate integral. This work also contains various procedures for constructing initial conditions.

More detailed algorithms for generating King–Michie models are now available [Spurzem & Einsel, private communication, 2002]. These procedures are based on generalized two-integral models with rotation that yield density distributions $\rho ( r )$ or $\rho ( r , z )$ of a continuous system by Runge–Kutta integration. A Monte Carlo rejection technique is then used to create the desired $N$ -body realization. The first simulations of axisymmetric $N$ -body models based on this approach have been reported [Boily, 2000; Boily & Spurzem, 2000].

A sequence of isotropic models can be constructed for different concentration parameters, $W _ { 0 } = | \Phi _ { 0 } | / \sigma _ { 0 } ^ { 2 }$ , where $\Phi _ { 0 }$ is the central potential and $\sigma _ { 0 }$ the corresponding velocity dispersion. Typical values range from $W _ { 0 } = 3$ for extended systems to $W _ { 0 } = 9$ for highly concentrated systems with small core radii. The King-type models are more dynamically relevant than the Plummer model which has a relatively large core when used with a tidal cutoff. Detailed algorithms for the generation of initial conditions including tidal truncation are available [Heggie & Ramamani, 1995] and will therefore not be repeated here. These models are approximately self-consistent, with the Galaxy represented by either a point mass or an extended disc potential which are suitable for globular cluster and open cluster simulations, respectively (to be described below). A number of investigations have employed the tidally truncated multi-mass King models which are convenient for systematic studies [cf. Aarseth & Heggie, 1998; Portegies Zwart et al., 1999, 2001; Hurley et al., 2001a].

# 8.3 Primordial binaries

Already the earliest $N$ -body simulations of point-mass interactions with $N \leq 2 5$ [von Hoerner, 1960, 1963; van Albada, 1968] demonstrated that binaries are an important feature of self-gravitating systems. Later studies confirmed that this process is also effective for systems with $N = 5 0 0$ [Aarseth, 1972a]. At this time, few binaries were known in open clusters and essentially none in globulars. Although this situation was consistent with theoretical expectations of small formation rates, some early $N$ -body and Monte Carlo simulations included the effect of primordial binaries [Aarseth, 1975, 1980; Spitzer & Mathieu, 1980]. In spite of detection difficulties [Trimble, 1980], evidence in favour of a significant distribution accumulated [Mathieu, 1983; van Leeuwen, 1983; Pryor et al., 1989], and close binaries are now observed by the Hubble Space Telescope (HST) at the very centres of globulars∗ [Grindlay, 1996]. These observational developments gave rise to more systematic explorations of this fascinating subject [McMillan, Hut & Makino, 1990, 1991; Heggie & Aarseth, 1992).

After these historical remarks we turn to the problem at hand, namely the initialization of primordial binaries. This procedure will be illustrated by choosing a flat distribution in $\log ( a )$ , where $a$ is the semi-major axis [Kroupa, 1995a]. Such a distribution is consistent with the classical result for low-mass stars in the solar neighbourhood [Duquennoy & Mayor, 1991]. Let us assume that the minimum and maximum periods have been specified, either on astrophysical or dynamical grounds. Next we must address the delicate question of the mass ratio. There is currently much uncertainty about this aspect even if we limit our attention to open star clusters. For the present purpose it suffices to combine component masses obtained separately from an unbiased IMF, although the possibility of some correlation for massive binaries may be justified observationally [Eggleton, private communication, 1997].

The following algorithmic steps are now carried out for an initial population of $N _ { \mathrm { b } }$ primordial binaries. This explicit notation is equivalent to the conventional definition of the binary fraction, $f _ { \mathrm { b } } = N _ { \mathrm { b } } / ( N _ { \mathrm { b } } + N _ { \mathrm { s } } )$ , with $N _ { \mathrm { s } }$ being the number of single stars, and is actually used by the codes. Accordingly, we define a provisional particle number, $N = N _ { \mathrm { s } } + N _ { \mathrm { b } }$ , which is specified as an input parameter. After generating the $2 N _ { \mathrm { b } }$ component masses independently, we form the sum of pair-wise masses in decreasing order and record the individual values separately. If $N _ { \mathrm { s } } ~ > ~ 0$ , the single bodies are also generated from the IMF and ordered sequentially, such that the most massive single body is at location $2 N _ { \mathrm { b } } + 1$ . From the initial coordinates and velocities of these $N _ { \mathrm { b } } + N _ { \mathrm { s } }$ objects we now perform the scaling in the usual way, which produces a system with total energy $E _ { 0 } = - 0 . 2 5$ (modified slightly by any external potential) satisfying the desired virial ratio. Because of the sampling involved in generating the IMF by (8.4), the maximum binary mass usually only exceeds the heaviest single mass by a modest factor for $f _ { \mathrm { b } } \simeq 0 . 5$ , even though the average binary mass is twice that of the singles. Hence a relatively large membership is needed in order for the upper mass limit to be approached.

At this stage, the component masses are introduced by splitting the relevant centre-of-mass (c.m.) body according to the initialization. Let us define the range $\psi$ (say $\psi = 1 0 0 0$ ) in semi-major axis, starting from an upper limit $a _ { 0 }$ . Here $a _ { 0 }$ is an input parameter, already scaled by the length unit, $R _ { \mathrm { V } }$ . The semi-major axis for pair index $i$ is chosen by

$$
a _ { i } = a _ { 0 } / 1 0 ^ { \beta } ,
$$

with $\beta = X _ { i } \log \psi$ and $X _ { i }$ a normalized random number. Corresponding eccentricities are assigned from a thermal distribution [Jeans, 1929] by $e _ { i } = Y _ { i } ^ { 2 }$ , with $Y _ { i }$ another random number, or given a constant value, as required. Using classical expressions [Brouwer & Clemence, 1961, p. 35], we form two-body elements by randomizing the perihelion, node and inclination angles appropriately for each binary. For computational convenience, the initial separation is taken as the apocentre, $R _ { i } = a _ { i } ( 1 { + } e _ { i } )$ . Combining the c.m. coordinates, $\mathbf { r } _ { \mathrm { c m } }$ , with the relative separation, ${ \bf R } _ { i } = { \bf r } _ { 2 i - 1 } - { \bf r } _ { 2 i }$ , we obtain the global coordinates

$$
\begin{array} { r } { \mathbf { r } _ { 2 i - 1 } = \mathbf { r } _ { \mathrm { c m } } + m _ { 2 i } \mathbf { R } _ { i } / ( m _ { 2 i - 1 } + m _ { 2 i } ) , \quad \quad } \\ { \mathbf { r } _ { 2 i } = \mathbf { r } _ { \mathrm { c m } } - m _ { 2 i - 1 } \mathbf { R } _ { i } / ( m _ { 2 i - 1 } + m _ { 2 i } ) , \quad \quad } \end{array}
$$

and similarly for the velocities. Upon completion of the binary initialization, the total particle number is assigned the final value $N = N _ { \mathrm { s } } + 2 N _ { \mathrm { b } }$ .

Procedures for so-called ‘eigenevolution’ [Kroupa, 1995b] have also been included as an alternative to the above. The basic idea is to modify the two-body elements for small pericentre distances, $R _ { \mathrm { p } }$ , due to pre-mainsequence evolution when stellar radii are larger. Although this scheme should be considered experimental, the essential steps are given below. First the period is assigned from a distribution with specified minimum period, $P _ { \mathrm { m i n } }$ [cf. eq. 11b of Kroupa, 1995b], whereas the eccentricity is again sampled from a thermal distribution. Given the period and mass, the pericentre distance is derived via the semi-major axis. A pre-mainsequence radius of $5 ( m / M _ { \odot } ) ^ { 1 / 2 }$ is used to reflect the earlier contraction stage. Using tidal circularization theory [Mardling & Aarseth, 2001], we obtain the modified eccentricity ${ \tilde { e } } _ { i }$ during a characteristic time interval of $1 0 ^ { 5 } \mathrm { y r }$ . Angular momentum conservation then yields the new semi-major axis by $a _ { i } = R _ { \mathrm { p } } / ( 1 - \tilde { e } _ { i } )$ . Finally, any case of overlapping enlarged radii is defined as collision and rejected. Depending on the minimum period, only a small fraction of the binaries are affected, with typically a dozen circularized orbits for $P _ { \mathrm { m i n } } = 5 \mathrm { d }$ and $N _ { \mathrm { b } } = 2 0 0 0$ .

One useful feature of the data structure is that the primordial binary components have neighbouring labels, $\mathcal { N } _ { i } , \mathcal { N } _ { j }$ , referred to as ‘names’ in the codes, which are helpful for distinguishing original and exchanged binaries. In this connection, we remark that in subsequent data analysis the definition of a primordial binary does not necessarily imply that $| { \mathcal N } _ { i } - { \mathcal N } _ { j } | = 1$ , since exchanged descendants still possess a certain binding energy and should therefore also be considered as primordial. On the other hand, new binaries form from single stars even if some of these may originally have been members of disrupted primordials. We now have a cluster of $N _ { \mathrm { b } }$ binaries with total internal binding energy

$$
\begin{array} { r } { E _ { \mathrm { b } } = - \frac { 1 } { 2 } \displaystyle \sum _ { i = 1 } ^ { N _ { \mathrm { b } } } m _ { 2 i - 1 } m _ { 2 i } / a _ { i } . } \end{array}
$$

Finally, any binary satisfying the close encounter condition $R _ { i } < R _ { \mathrm { c l } }$ is initialized as a KS solution before the calculation starts. This explicit initialization provides a convenient dataset for subsequent comparison.

Given the preponderance of binaries and even multiple systems in a variety of clusters, it is natural to extend the algorithm outlined above to include hierarchical configurations. We concentrate on the case of primordial triples which can be readily generalized to higher-order systems. The basic idea is to split the mass of the primary into an inner binary, with suitably chosen two-body parameters. Using the outer pericentre and eccentricity, we test the stability (to be defined in the next chapter) before accepting the new initial conditions, otherwise a new inner semi-major axis is generated. Since the first sequential binaries are selected for this procedure, the combined mass will also tend to be slightly larger than for the standard binaries, but other mass distributions may be chosen if desired. As in the case of primordial binaries, the total particle number is increased accordingly. Moreover, the outer components are placed sequentially at $j > 2 N _ { \mathrm { b } }$ after all the inner binaries have been assigned. This arrangement therefore results in a well-defined data structure that facilitates KS initialization and membership identification. A popular alternative data structure is discussed in Appendix F.

# 8.4 Open clusters and clouds

A cluster orbiting in the Galaxy is subject to an external tidal force that affects the motions in the outer parts and, indeed, often determines the spatial extent. We consider in turn three different perturbing components, i.e. circular motion near the Galactic plane, an irregular force due to passing interstellar clouds and a constant external potential. A discussion of the latter is left for subsequent sections.

We begin with the simple case of a circular orbit in the solar neighbourhood and adopt a right-handed coordinate system whose origin rotates about the Galaxy with constant angular velocity, $\Omega _ { z }$ , and the $x$ -axis pointing away from the centre. Since typical cluster radii are small compared with the size of the Galaxy, it is sufficient to expand the perturbing potential to first order. The well-known equations of motion for the coordinates $x _ { i } , y _ { i } , z _ { i }$ take the form [Aarseth, 1967; Hayli, 1967]

$$
\begin{array} { r l } & { \ddot { x } _ { i } = F _ { x } + 4 A ( A - B ) x _ { i } + 2 \Omega _ { z } \dot { y } _ { i } , } \\ & { \ddot { y } _ { i } = F _ { y } - 2 \Omega _ { z } \dot { x } _ { i } , } \\ & { \ddot { z } _ { i } = F _ { z } + \displaystyle \frac { \partial K _ { z } } { \partial z } z _ { i } . } \end{array}
$$

The first terms represent the sum over all the internal interactions, $A$ and $B$ are Oort’s constants of Galactic rotation and $\partial K _ { z } / \partial z$ is the local force gradient normal to the plane of symmetry.

The equations (8.14) induce a tidal torque since $K _ { z }$ is directed towards the plane of symmetry, leading to flattening as well as velocity anisotropy. Taking $\dot { \mathbf { r } } _ { i } \cdot \ddot { \mathbf { r } } _ { i }$ and summing over the masses, we readily obtain the Jacobi energy integral

$$
E _ { \mathrm { J } } = T + U - 2 A ( A - B ) \sum m _ { i } x _ { i } ^ { 2 } - \frac { 1 } { 2 } \frac { \partial K _ { z } } { \partial z } \sum m _ { i } z _ { i } ^ { 2 } ,
$$

since the Coriolis terms cancel. An equivalent constant of motion also applies to individual stars in the absence of encounters and significant mass motions or mass loss.

The concept of tidal radius [von Hoerner, 1957; King, 1962] has played an important role towards the understanding of cluster dynamics. For a star at rest on the $x$ -axis, the central attraction of the cluster is balanced

by the tidal force at a distance

$$
R _ { \mathrm { t } } = \left[ { \frac { G M } { 4 A ( A - B ) } } \right] ^ { 1 / 3 } ,
$$

where all quantities are now expressed in physical units. According to classical perceptions, the energy per unit mass for a star to escape from an idealized cluster model is given by [Wielen, 1972]

$$
\begin{array} { r } { C _ { \mathrm { c r i t } } = - \frac { 3 } { 2 } [ 4 G ^ { 2 } M ^ { 2 } A ( A - B ) ] ^ { 1 / 3 } . } \end{array}
$$

Although this energy limit is less stringent compared with an isolated system, a star satisfying this condition may still take a long time to reach one of the Lagrange points, $L _ { 1 }$ or $L _ { 2 }$ , and some excess is usually required to ensure escape. We shall see later that there exist some orbits that return to the cluster after moving well outside the tidal radius [Ross, Mennim $\&$ Heggie, 1997].

The tidal parameters are scaled to $N$ -body units in the following way. First we choose the Oort’s constants $A = 1 4 . 4$ , $B = - 1 2 . 0 \mathrm { k m s ^ { - 1 } k p c ^ { - 1 } }$ [Binney & Tremaine, 1987]. After converting $A$ and $B$ to $\mathrm { c m s ^ { - 1 } p c ^ { - 1 } }$ and comparing dimensions, star cluster units of solar mass and pc are introduced into the $x$ -component of the tidal coefficient by the scaling

$$
\tilde { T } _ { 1 } = 4 \tilde { A } ( \tilde { A } - \tilde { B } ) \beta ,
$$

with $\beta = L ^ { * } / G M _ { \odot }$ and $L ^ { * }$ in pc. Hence the final scaling to the appropriate length unit and total mass gives

$$
T _ { 1 } = \tilde { T } _ { 1 } ( R _ { \mathrm { V } } ^ { 3 } / N M _ { \mathrm { S } } ) ,
$$

where $\tilde { T } _ { 1 } \simeq 0 . 3 5 3 7$ .

For the $z$ -component, denoted by ${ \tilde { T } } _ { 3 }$ , we have according to the theory of stellar dynamics [Oort, 1965]

$$
T _ { 3 } ^ { * } = - 4 \pi G \rho _ { 0 } - 2 ( A - B ) ( A + B ) ,
$$

where $\rho _ { 0 } = 0 . 1 1 M _ { \odot } \mathrm { p c ^ { - 3 } }$ is the local density [Kuijken $\&$ Gilmore, 1989]. Converting to the above units and transforming to $\tilde { \cal T } _ { 3 }$ as above, we obtain

$$
T _ { 3 } = \tilde { T } _ { 3 } ( R _ { \mathrm { V } } ^ { 3 } / N M _ { \mathrm { S } } ) ,
$$

with $\bar { T } _ { 3 } \simeq - 1 . 4 1 1 8$ . Note that the vertical force gradient is a factor of 4 greater than the $x$ -component for the assumed Galactic model.

The final conversion concerns the angular velocity, given by $\Omega _ { z } = A - B$ . Let us define

$$
\tilde { T } _ { 4 } = 2 ( \tilde { A } - \tilde { B } ) \beta ^ { 1 / 2 }
$$

as twice the actual value for computational convenience, with $\tilde { T } _ { 4 } \simeq 0 . 8 0 5 2$ . Accordingly, the final scaled value becomes

$$
T _ { 4 } = \tilde { T } _ { 4 } ( R _ { \mathrm { V } } ^ { 3 } / N M _ { \mathrm { S } } ) ^ { 1 / 2 } .
$$

The corresponding Galactic rotation period is readily obtained using (7.5). For completeness, the scaled tidal radius takes the form

$$
r _ { \mathrm { t } } = ( { { \tilde { M } } } / { T _ { 1 } } ) ^ { 1 / 3 } ,
$$

with $\tilde { M }$ denoting the total mass in $N$ -body units.† We remark that one may study tidal effects for circular orbits at different locations in the Galaxy by using appropriate differential rotation constants and vertical force gradients derived from models and/or observation. Moreover, since the coefficient $T _ { 3 }$ is approximately constant for $z \le 0 . 5 \mathrm { k p c }$ , the present treatment is also valid for open clusters at moderate heights above the Galactic plane, i.e. tidal shocks are not important here.

As far as the AC integration scheme is concerned, the additional force terms in (8.14) must be assigned to the appropriate component of (3.1). Since the tidal contributions arising from $T _ { 1 }$ and $T _ { 3 }$ change smoothly with position, it is natural to combine them with the regular force. However, the Coriolis terms vary with the velocity and are therefore added to the neighbour force. Note that expressions for the corresponding derivatives are readily obtained for Hermite integration.

The perturbation by interstellar clouds may also be modelled by $N$ - body simulations [Bouvier & Janin, 1970; Terlevich, 1983, 1987]. Consider a spherical region of size $R _ { \mathrm { b } }$ surrounding an open cluster and containing a number of individual clouds. These clouds exert an irregular tidal force on the cluster members. By ignoring the contributions from clouds outside the boundary, it is shown below that only the external fluctuating force component is neglected. The perturbing effect of each cloud, represented as a polytrope of index 5 (or Plummer model), is included in the equations of motion and provides a regular force

$$
\mathbf { F } _ { c } = - G M _ { \mathrm { c } } \left[ \frac { \mathbf { r } _ { i } - \mathbf { r } _ { \mathrm { c } } } { ( | \mathbf { r } _ { i } - \mathbf { r } _ { \mathrm { c } } | ^ { 2 } + \epsilon _ { \mathrm { c } } ^ { 2 } ) ^ { 3 / 2 } } - \frac { \mathbf { r } _ { i } - \mathbf { r } _ { \mathrm { d } } } { R _ { \mathrm { b } } ^ { 3 } } \right] .
$$

Here $M _ { \mathrm { c } } , \mathbf { r } _ { \mathrm { c } } , \epsilon _ { \mathrm { c } }$ is the cloud mass, vectorial position and softening length, and $\mathbf r _ { \mathrm { d } }$ is the density (or symmetry) centre of the cluster. The repulsive force is added to cancel a spurious net inward attraction that would otherwise reduce the escape rate; i.e. the local fast-moving clouds contribute an average density distribution and resulting retardation at large distances. Again this treatment is suitable for implementation in the Hermite codes since taking the time derivative of (8.25) is straightforward.

The clouds are integrated in the rotating frame, with the cluster attraction omitted from their equations of motion (8.14). When the boundary is crossed, a new cloud is introduced at random position angles with isotropic velocities [cf. Terlevich, 1987]. The resulting small force discontinuity is alleviated by employing a mass smoothing function near $R _ { \mathrm { b } }$ . Although the actual force from a given cloud may be large, the differential effect is relatively small due to the high velocity dispersion. Even so, the regular time-steps are reduced by a significant factor because the higher derivatives are affected by the cloud velocities and masses.

The employment of a relatively small boundary radius can be justified by the following considerations. Let us write the equation of motion in an inertial coordinate system as

$$
\ddot { \mathbf { r } } _ { i } = \mathbf { F } _ { i } + \mathbf { A } _ { \mathrm { o u t } } + \mathbf { A } _ { \mathrm { i n } } ,
$$

where $\mathbf { A } _ { \mathrm { o u t } }$ and $\mathbf { A } _ { \mathrm { i n } }$ represent all additional accelerations outside and inside the cloud boundary, respectively, and the first term is due to the cluster members. We now assume that $\mathbf { A } _ { \mathrm { o u t } } = \mathbf { A } _ { \mathrm { o u t } }$ ; i.e. we neglect irregular effects outside the boundary. Adding and subtracting $\bar { \mathbf { A } } _ { \mathrm { i n } }$ then results in

$$
\ddot { \mathbf { r } } _ { i } = \mathbf { F } _ { i } + \bar { \mathbf { A } } + \mathbf { A } _ { \mathrm { i n } } - \bar { \mathbf { A } } _ { \mathrm { i n } } ,
$$

which is readily converted to rotating coordinates. The combined term $\mathbf { A } _ { \mathrm { i n } } - \mathbf { A } _ { \mathrm { i n } }$ refers to the clouds and $\mathbf { A }$ is the usual total galactic tidal acceleration. Hence this exercise also provides the justification for subtracting the average cloud force in the basic equation (8.25).

The effect of interstellar clouds on the internal dynamics of star clusters was examined in a classical paper by Spitzer [1958], who based his conclusions of reduced life-times on somewhat higher cloud densities and masses than employed in the numerical simulations. From the impulse approximation, the energy change of the cluster due to a cloud with impact parameter $p > r _ { h }$ , relative velocity $V$ and mass $M _ { 2 }$ is given by

$$
\Delta E = \frac { 4 G ^ { 2 } M _ { 2 } ^ { 2 } M \bar { r ^ { 2 } } } { 3 b ^ { 4 } V ^ { 2 } } ,
$$

where $r ^ { 2 }$ is the mean square radius of the cluster members with mass $M$ and $b$ the impact parameter. This compares with $\Delta E = G ^ { 2 } M ^ { 3 } / 3 V ^ { 2 } a ^ { 2 }$ for the case of a head-on encounter between two equal-mass Plummer models with scale factor $a$ [Binney & Tremaine, 1987].

An independent derivation, based on the so-called ‘extended impulse approximation’, gave rise to a convergent expression for close encounters between two Plummer spheres [Theuns, 1992b]. Here the magnitude of the velocity change in the orbital plane, $\Delta v \simeq 2 M _ { 2 } / a ^ { 2 } v$ , replaces the singular expression $\Delta v \simeq 2 M _ { 2 } / b ^ { 2 } v$ , in agreement with the head-on encounter result. It was also pointed out that the relative energy gain from the cluster heating does not scale in a simple manner with the parameters defining the encounter.

Numerical simulations [Aguilar & White, 1985] show good agreement with theory for $b \geq 5 \operatorname* { m a x } \left\{ r _ { \mathrm { h } } , \epsilon _ { \mathrm { c } } \right\}$ . The heating is a small effect and the actual energy change will be less because the cluster size is usually smaller than typical impact parameters. Finally, we remark that, given the field star density, there may be several hundred such stars inside the tidal radius. Their disrupting effect on open clusters is likely to be small due to the high velocity dispersion but a quantitative investigation is lacking.

# 8.5 Eccentric planar orbits

Let us now turn to modelling general motions of bound subsystems in a galactic environment. Some examples are globular clusters and dwarf spheroidal galaxies, both of which have received considerable attention [Grillmair, 1998; Oh, Lin & Aarseth, 1995]. We begin by deriving equations of motion suitable for the divided difference formulation which are easier to implement and restrict the treatment to motion in the plane. The next section deals with the case of 3D motion, using a formulation that is also suitable for Hermite integration.

Consider a system of self-gravitating particles orbiting the Galaxy at a distance $R _ { 0 }$ . We define right-handed coordinates centred on the cluster, with the $x$ -axis pointing towards the Galactic centre. The acceleration in the inertial reference frame of a local test particle at ${ \bf r } = { \bf r } _ { \mathrm { R } }$ is given by

$$
\ddot { \mathbf { r } } _ { \mathrm { I } } = \ddot { \mathbf { r } } _ { \mathrm { R } } + 2 \boldsymbol { \Omega } \times \dot { \mathbf { r } } _ { \mathrm { R } } + \boldsymbol { \Omega } \times ( \boldsymbol { \Omega } \times \mathbf { r } _ { \mathrm { R } } ) + \dot { \boldsymbol { \Omega } } \times \mathbf { r } _ { \mathrm { R } } ,
$$

where $\Omega$ is the instantaneous angular velocity and $\mathbf { r } _ { \mathrm { R } }$ refers to rotating coordinates. This equation contains the well-known Coriolis terms as well as the centrifugal and Euler terms.

First we discuss the case of a point-mass potential. In the inertial frame, the equation of motion for a cluster member is

$$
{ \ddot { \bf r } } _ { \mathrm { I } } = \Sigma - { \frac { M _ { \mathrm { g } } } { R ^ { 3 } } } { \bf R } + { \frac { M _ { \mathrm { g } } } { R _ { 0 } ^ { 3 } } } { \bf R } _ { 0 } ,
$$

with $\pmb { \Sigma }$ the internal attraction and the last two terms representing the tidal acceleration due to the mass $M _ { \mathrm { g } }$ located at ${ \bf R } = { \bf R _ { 0 } } + { \bf r }$ .

In the following we consider motion in the $x$ – $y$ plane with angular velocity $\Omega _ { z }$ . The position and angular velocity of the Galactic centre are

then given in terms of the unit vectors $\hat { \mathbf x } , \hat { \mathbf y } , \hat { \mathbf z }$ such that

$$
\begin{array} { r l } & { { \bf R } _ { 0 } = - R _ { 0 } \hat { \bf x } , } \\ & { \quad \Omega = ( { \bf R } _ { 0 } \times \dot { \bf R } _ { 0 } ) / R _ { 0 } ^ { 2 } = \Omega _ { z } \hat { \bf z } . } \end{array}
$$

This allows the centrifugal term to be expressed as

$$
\boldsymbol { \Omega } \times ( \boldsymbol { \Omega } \times \mathbf { r } ) = - \Omega _ { z } ^ { 2 } \dot { x } \hat { \mathbf { x } } - \Omega _ { z } ^ { 2 } \dot { y } \hat { \mathbf { y } } .
$$

Similarly, the angular momentum per unit mass is

$$
{ \bf J } = { \bf R } _ { 0 } \times \dot { \bf R } _ { 0 } = R _ { 0 } ^ { 2 } \Omega _ { z } \hat { \bf z } = J _ { z } \hat { \bf z } .
$$

Differentiation of (8.31) combined with the above relation results in

$$
\dot { \boldsymbol \Omega } = - \frac { 2 \dot { R } _ { 0 } ( \mathbf { R } _ { 0 } \times \dot { \mathbf { R } } _ { 0 } ) } { R _ { 0 } ^ { 3 } } = - \frac { 2 \dot { R } _ { 0 } \Omega _ { z } } { R _ { 0 } } \hat { \mathbf { z } } .
$$

Substituting for $\Omega _ { z }$ from (8.33) gives rise to the Euler term

$$
\dot { \boldsymbol \Omega } \times \mathbf { r } = - \frac { 2 \dot { R } _ { 0 } J _ { z } } { R _ { 0 } ^ { 3 } } ( x \hat { \mathbf y } - y \hat { \mathbf x } ) .
$$

The equation of motion in rotating coordinates can now be written down by inverting (8.29) and making use of (8.30) and the definition of $\mathbf { R } _ { 0 }$ . This yields the explicit expressions

$$
\begin{array} { r l r } & { \ddot { x } = \Sigma _ { x } + \displaystyle \frac { M _ { \mathrm { g } } } { R _ { 0 } ^ { 3 } } \left[ R _ { 0 } - \left( R _ { 0 } + x \right) \left( \frac { R _ { 0 } } { R } \right) ^ { 3 } \right] - \displaystyle \frac { 2 \dot { R } _ { 0 } J _ { z } } { R _ { 0 } ^ { 3 } } y + \Omega _ { z } ^ { 2 } x + 2 \Omega _ { z } \dot { y } , } & \\ & { \ddot { y } = \Sigma _ { y } - \displaystyle \frac { M _ { \mathrm { g } } } { R ^ { 3 } } y + \frac { 2 \dot { R } _ { 0 } J _ { z } } { R _ { 0 } ^ { 3 } } x + \Omega _ { z } ^ { 2 } y - 2 \Omega _ { z } \dot { x } , } & \\ & { \ddot { z } = \Sigma _ { z } - \displaystyle \frac { M _ { \mathrm { g } } } { R ^ { 3 } } z . } & { \qquad ( 8 } \end{array}
$$

If $r \ll R$ , which is frequently the case, the evaluation of the tidal force terms may be speeded up by expanding $( R _ { 0 } / R ) ^ { - 3 }$ to first order. Taking account of the vectorial relation $R ^ { 2 } = R _ { 0 } ^ { 2 } + 2 { \bf R } _ { 0 } \cdot { \bf r } + r ^ { 2 }$ , we have

$$
R ^ { - 3 } = R _ { 0 } ^ { - 3 } \left[ 1 - \frac { 3 { \bf R } _ { 0 } \cdot { \bf r } } { R _ { 0 } ^ { 2 } } + { \cal O } ( \frac { r ^ { 2 } } { R _ { 0 } ^ { 2 } } ) \right] ,
$$

which can be used to simplify the equations of motion above. The full equations were used to study the tidal evolution of globular clusters in eccentric orbits and also the tidal disruption of dwarf spheroidal galaxies

[Oh, Lin & Aarseth, 1992, 1995]. As can be readily verified, these equations reduce to the form (8.14) with reversed sign of $\ddot { x }$ for circular motion if the point-mass nature of the model is taken into account.

The energy of the cluster centre associated with the rotating frame is

$$
\begin{array} { r } { E = \frac 1 2 \dot { \bf R } _ { 0 } ^ { 2 } + \frac 1 2 J _ { z } ^ { 2 } / R _ { 0 } ^ { 2 } - M _ { \mathrm { g } } / R _ { 0 } . } \end{array}
$$

Since this quantity is conserved, we derive the equation of motion by differentiation. Cancelling $\dot { \bf R } _ { 0 }$ from the common scalar products yields

$$
\ddot { \bf R } _ { 0 } = \left( - \frac { M _ { \mathrm { g } } } { R _ { 0 } ^ { 3 } } + \frac { J _ { z } ^ { 2 } } { R _ { 0 } ^ { 4 } } \right) { \bf R } _ { 0 } .
$$

The case of a logarithmic potential, $\Phi = V _ { 0 } ^ { 2 } \ln ( R / a _ { 0 } )$ represents another useful galaxy model that has many applications. Since the kinematical terms are the same as before, we need consider only the equation of motion in the inertial frame. The alternative form of (8.30) is then

$$
\ddot { \mathbf { r } } _ { \mathrm { I } } = \boldsymbol { \Sigma } - \frac { V _ { 0 } ^ { 2 } } { R ^ { 2 } } \mathbf { R } + \frac { V _ { 0 } ^ { 2 } } { R _ { 0 } ^ { 2 } } \mathbf { R } _ { 0 } .
$$

Hence the factors $M _ { \mathrm { g } } / R _ { 0 } ^ { 3 }$ , $M _ { g } / R ^ { 3 }$ , and $( R / R _ { 0 } ) ^ { 3 }$ in (8.36) are replaced by $V _ { 0 } ^ { 2 } / R _ { 0 } ^ { 2 }$ , $V _ { 0 } ^ { 2 } / R ^ { 2 }$ and $( R / R _ { 0 } ) ^ { 2 }$ , respectively. The corresponding energy per unit mass for the cluster centre is now given by

$$
\begin{array} { r } { E = \frac 1 2 \dot { \bf R } _ { 0 } ^ { 2 } + \frac 1 2 J _ { z } ^ { 2 } / R _ { 0 } ^ { 2 } + V _ { 0 } ^ { 2 } \ln ( R _ { 0 } / a _ { 0 } ) + C , } \end{array}
$$

where $V _ { 0 }$ and $a _ { 0 }$ denote velocity and radius scales and $C$ is a constant. From $\dot { E } = 0$ and the procedure above we obtain the equation of motion

$$
\ddot { \bf R } _ { 0 } = \left( - \frac { V _ { 0 } ^ { 2 } } { R _ { 0 } ^ { 2 } } + \frac { J _ { z } ^ { 2 } } { R _ { 0 } ^ { 4 } } \right) { \bf R } _ { 0 } .
$$

All these equations are in exact form and therefore suitable for general use. Moreover, the additional equations for the cluster centre itself, (8.39) or (8.42), are simple and can be integrated to high accuracy. Since the third derivative of $\mathbf { R } _ { 0 }$ involves only the velocity $\dot { \bf R } _ { 0 }$ additionally, the Hermite scheme would be appropriate. Hence the values of $\Omega _ { z }$ and ${ \dot { R } _ { 0 } } = \mathbf { R } _ { 0 } \cdot \dot { \mathbf { R } } _ { 0 } / R _ { 0 }$ which appear in the equations of motion can be updated frequently. Finally, note that these formulations are suitable only for the divided difference method (i.e. NBODY 5) since the force derivatives needed for Hermite integration are rather cumbersome.

# 8.6 Motion in 3D

The case of 3D globular cluster orbits requires special care with a Hermite method. Thus, in order for such a scheme to work, we need to obtain explicit force derivatives of all the terms. For this purpose we have a choice of two strategies, both of which exploit the computational advantage of a local reference system when the internal dimensions are small compared with the size of the orbit. By generalizing the procedure of section 8.5 to 3D, the number of terms in the equation of motion is larger and their form less amenable to differentiation. In the alternative and preferable formulation, we take a non-rotating, but accelerating, coordinate system also with the origin at the cluster centre, with axes having fixed directions in space.

The construction of realistic galactic potentials requires a significant disc component as well as a halo. Hence we consider a superposition of different characteristic contributions, with each part having a 3D representation. Let us first introduce a spherical potential due to a point-mass $M _ { \mathrm { g } }$ , adapted for Hermite integration. After linearizing the tidal terms in (8.30) using (8.37), the equation of motion in non-rotating coordinates for a mass-point at $\mathbf { r }$ takes the form

$$
\ddot { \mathbf { r } } = \pmb { \Sigma } - \frac { M _ { \mathrm { g } } } { R _ { 0 } ^ { 3 } } \left( \mathbf { r } - \frac { 3 \mathbf { r } \cdot \mathbf { R } _ { 0 } } { R _ { 0 } ^ { 2 } } \mathbf { R } _ { 0 } \right) .
$$

By differentiation the corresponding force derivative becomes

$$
\begin{array} { l } { { \displaystyle \frac { d ^ { 3 } { \bf r } } { d t ^ { 3 } } = \dot { \Sigma } - \frac { M _ { \mathrm { g } } } { R _ { 0 } ^ { 3 } } \left( \dot { \bf r } - \frac { 3 \dot { \bf r } \cdot { \bf R } _ { 0 } } { R _ { 0 } ^ { 2 } } { \bf R } _ { 0 } - \frac { 3 { \bf r } \cdot \dot { \bf R } _ { 0 } } { R _ { 0 } ^ { 2 } } { \bf R } _ { 0 } - \frac { 3 { \bf R } _ { 0 } \cdot \dot { \bf R } _ { 0 } } { R _ { 0 } ^ { 2 } } { \bf r } \right) } } \\ { { \displaystyle ~ + \frac { 3 M _ { \mathrm { g } } } { R _ { 0 } ^ { 5 } } \left[ \dot { \bf R } _ { 0 } - \frac { 5 ( { \bf R } _ { 0 } \cdot \dot { \bf R } _ { 0 } ) } { R _ { 0 } ^ { 2 } } { \bf R } _ { 0 } \right] ( { \bf r } \cdot { \bf R } _ { 0 } ) . } } \end{array}
$$

In the absence of encounters, (8.43) yields a conserved Jacobi integral,

$$
\begin{array} { r } { E _ { J } = \frac { 1 } { 2 } \dot { \mathbf { r } } ^ { 2 } - \boldsymbol { \Omega } \cdot ( \mathbf { r } \times \dot { \mathbf { r } } ) + \frac { 1 } { 2 } \Omega ^ { 2 } r ^ { 2 } - \frac { 3 } { 2 } \Omega ^ { 2 } \left( \frac { \mathbf { r } \cdot \mathbf { R } _ { 0 } } { R _ { 0 } } \right) ^ { 2 } + \boldsymbol { \Phi } _ { \mathrm { c } } , } \end{array}
$$

with the angular velocity $\Omega ^ { 2 } = M _ { \mathrm { g } } / R ^ { 3 }$ and $\Phi _ { \mathrm { c } }$ the cluster potential at $r$ [Heggie, 2001].

From the definition of the total energy or virial theorem, the external tidal field contribution is given by

$$
W = { \frac { M _ { \mathrm { g } } } { 2 R _ { 0 } ^ { 3 } } } \sum _ { i } m _ { i } \left( r ^ { 2 } - 3 { \frac { ( \mathbf { r } \cdot \mathbf { R } _ { 0 } ) ^ { 2 } } { R _ { 0 } ^ { 2 } } } \right) .
$$

For the special case of circular cluster motion, the Jacobi energy in the rotating frame given by (8.15) is conserved. This quantity can also be expressed in the non-rotating frame as

$$
E = T + U + W - \Omega \cdot \mathbf { J } ,
$$

where $\mathbf { J }$ is the standard angular momentum. For some purposes, it may be desirable to construct initial conditions without rotation in a rotating frame. This is achieved by adding the quantity

$$
\Delta \dot { \mathbf { r } } = - \frac { 1 } { R _ { 0 } ^ { 2 } } \left[ ( \mathbf { r } \cdot \dot { \mathbf { R } } _ { 0 } ) \mathbf { R } _ { 0 } - ( \mathbf { r } \cdot \mathbf { R } _ { 0 } ) \dot { \mathbf { R } } _ { 0 } \right]
$$

to the velocity of each star. Finally, the integration of the cluster centre can be carried out according to the prescription of the previous section. As before, the equation of motion (8.39) can be integrated accurately using explicit derivatives of higher order.

At this stage we introduce a disc potential which breaks the spherical symmetry. Given the requirement of an analytical force derivative, the choice is somewhat limited. In the following we derive the relevant expressions for the Miyamoto–Nagai [1975] potential that in cylindrical coordinates $R , z$ takes the form

$$
\Phi = - \frac { M _ { \mathrm { d } } } { \{ R ^ { 2 } + [ a + ( b ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 } ] ^ { 2 } \} ^ { 1 / 2 } } .
$$

This expression can represent the full range, from infinitely thin discs to a spherical system by the choice of the coefficients $a , b$ . Taking the gradient gives rise to the radial and vertical force components

$$
\begin{array} { l } { \mathbf { F } _ { R } = - \displaystyle \frac { M _ { \mathrm { d } } } { A ^ { 3 } } \mathbf { R } , } \\ { F _ { z } = - \displaystyle \frac { M _ { \mathrm { d } } z [ a + ( b ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 } ] } { A ^ { 3 } ( b ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 } } , } \\ { \mathbf { R } = \mathbf { R } _ { 0 } + x \hat { \mathbf { x } } + y \hat { \mathbf { y } } } \\ { A = \{ R ^ { 2 } + [ a + ( b ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 } ] ^ { 2 } \} ^ { 1 / 2 } . } \end{array}
$$

with

and

Differentiation with respect to time and collection of terms yield

$$
\begin{array} { l } { { \displaystyle { { \dot { \bf F } } } _ { R } = - \frac { M _ { \mathrm { d } } } { A ^ { 3 } } \left\{ { { \dot { \bf R } } } - \frac { 3 } { A ^ { 2 } } \left[ R { \dot { R } } + \frac { a + ( b ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 } } { ( b ^ { 2 } + z ^ { 2 } ) } z { \dot { z } } \right] { \bf R } \right\} , } } \\ { { \displaystyle { { \dot { F } } _ { z } } = - \frac { 3 M _ { \mathrm { d } } [ a + ( b ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 } ] z } { A ^ { 5 } ( b ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 } } \left[ R { \dot { R } } + \frac { a + ( b ^ { 2 } + z ^ { 2 } ) ^ { 1 / 2 } } { ( b ^ { 2 } + z ^ { 2 } ) } z { \dot { z } } \right] } } \\ { { \displaystyle ~ - \frac { M _ { d } [ a b ^ { 2 } + ( b ^ { 2 } + z ^ { 2 } ) ^ { 3 / 2 } ] } { A ^ { 3 } ( b ^ { 2 } + z ^ { 2 } ) ^ { 3 / 2 } \dot { z } } . } } \end{array}
$$

The disc potential contains expressions which do not appear amenable to linearization, although analytical derivation by special software is feasible. Alternatively, we may obtain the smoothly varying differential effect by subtracting the corresponding values for the cluster centre. Note that the latter evaluations are in any case performed at frequent intervals for the purpose of integrating the cluster centre. In view of the many common factors in these expressions, the numerical effort may be considered acceptable even if carried out on the GRAPE-6 host. If necessary, several such components may be superimposed, albeit at extra cost.

As the final part of a realistic galaxy model, we include the logarithmic potential discussed earlier. An expansion to second order gives

$$
\Phi = V _ { 0 } ^ { 2 } \left[ \ln \left( \frac { R _ { 0 } } { a _ { 0 } } \right) + \frac { { \bf R } _ { 0 } \cdot { \bf r } } { R _ { 0 } ^ { 2 } } + \frac { 1 } { 2 } \left( \frac { r ^ { 2 } } { R _ { 0 } ^ { 2 } } - \frac { 2 ( { \bf r } \cdot { \bf R } _ { 0 } ) ^ { 2 } } { R _ { 0 } ^ { 4 } } \right) \right] .
$$

In the inertial frame, the corresponding linearized tidal force and first derivative are given by

$$
\begin{array} { r l } & { { \displaystyle { \bf F } _ { \mathrm { L } } = - \frac { V _ { 0 } ^ { 2 } } { R _ { 0 } ^ { 2 } } \left( { \bf r } - \frac { 2 { \bf R } _ { 0 } \cdot { \bf r } } { R _ { 0 } ^ { 2 } } { \bf R } _ { 0 } \right) } \ , } \\ & { { \displaystyle { { \dot { \bf F } } _ { \mathrm { L } } } = - \frac { V _ { 0 } ^ { 2 } } { R _ { 0 } ^ { 2 } } \left( { \dot { \bf r } } - \frac { 2 { \bf R } _ { 0 } \cdot { \bf r } } { R _ { 0 } ^ { 2 } } { \dot { \bf R } } _ { 0 } \right) + \frac { 2 V _ { 0 } ^ { 2 } } { R _ { 0 } ^ { 4 } } ( { \dot { \bf R } } _ { 0 } \cdot { \bf r } + { \bf R } _ { 0 } \cdot { \dot { \bf r } } ) { \bf R } _ { 0 } } } \\ & { ~ + \frac { 2 V _ { 0 } ^ { 2 } } { R _ { 0 } ^ { 4 } } \left( { \bf r } - \frac { 4 { \bf R } _ { 0 } \cdot { \bf r } } { R _ { 0 } ^ { 2 } } { \bf R } _ { 0 } \right) \left( { \bf R } _ { 0 } \cdot { \dot { \bf R } } _ { 0 } \right) . } \end{array}
$$

Hence the total force is the sum of the contributions (8.43), (8.50) and (8.54), bearing in mind the use of cylindrical coordinates for the disc component. Alternatively, the halo potential may be included by direct evaluation as for the disc above, with acceptable loss of precision.‡

# 8.7 Standard polynomials

The last task before beginning the calculation is usually to initialize force polynomials and time-steps. These procedures are essentially identical in the divided difference and Hermite formulations, and we therefore concentrate on the latter in connection with the AC neighbour scheme (i.e. the code NBODY 6). Note that the case of initializing a single force polynomial has already been described in chapter 2, where all the necessary expressions are given.

Only two main input parameters are needed to create the desired polynomials. This stage begins by forming neighbour lists for all the particles. For Plummer or King–Michie models, the basic neighbour radius $S _ { 0 }$ is modified by the central distance according to $R _ { \mathrm { s } } ^ { 2 } = S _ { 0 } ^ { 2 } ( 1 + r _ { i } ^ { 2 } )$ in order to yield an acceptable membership at different radii. This relation compensates for the density profile but should not be used if subsystems are present. In any case, the radius $R _ { \mathrm { s } }$ is increased if there are no neighbours and reduced if the membership exceeds a prescribed value, $n _ { \mathrm { m a x } }$ (which should be a bit smaller than $L _ { \mathrm { m a x } }$ for technical reasons).

Having determined sequential neighbour lists, $L _ { j , i }$ , with the membership $n _ { i } = L _ { 1 , i }$ , we now evaluate the force and its derivative by explicit summation over all particles. If the summation index is identified in the neighbour list, the corresponding contributions are added to the irregular components $\mathbf { F } _ { \mathrm { I } }$ , ${ \bf D } _ { \mathrm { I } } ^ { 1 }$ ; otherwise they are included in the regular terms. After all the particles have been considered, any external contributions are added to the respective components as discussed above. Lastly, the total force and first derivative for each particle are formed by

$$
\begin{array} { r c l } { { } } & { { } } & { { { \bf F } = { \bf F } _ { \mathrm { I } } + { \bf F } _ { \mathrm { R } } , } } \\ { { } } & { { } } & { { \dot { \bf F } = { \bf D } _ { \mathrm { I } } ^ { 1 } + { \bf D } _ { \mathrm { R } } ^ { 1 } , } } \end{array}
$$

where the index $i$ has been suppressed and $\mathbf { D }$ now denotes a derivative.

Another full $N$ summation is performed in order to obtain the second and third force derivatives. This boot-strapping procedure requires all $\mathbf { F }$ and $\dot { \mathbf { F } }$ to be known, as can be seen from the basic derivation in chapter 2. Again the neighbour list is used to distinguish the irregular and regular components, ${ \bf D } _ { \mathrm { I } } ^ { 2 }$ , $\mathbf { D } _ { \mathrm { I } } ^ { 3 }$ and ${ \bf D } _ { \mathrm { R } } ^ { 2 }$ , ${ \bf D } _ { \mathrm { R } } ^ { 3 }$ . Since distant particles do not contribute significantly to the regular derivatives, their effect may be neglected outside some distance (say $5 R _ { \mathrm { s } }$ ). Higher derivatives of any external forces are added consistently according to type, using boot-strapping.

It now remains for new irregular and regular time-steps, $\Delta t _ { i }$ , $\Delta T _ { i }$ , to be assigned from the definition (2.13), using the block-step rule, (2.25), if relevant. At the same time, the primary coordinates and velocity, $\mathbf { x } _ { \mathrm { 0 } }$ , $\mathbf { v } _ { 0 }$ , are initialized and the factorials $\begin{array} { l } { \displaystyle { \frac { 1 } { 2 } } } \end{array}$ and $\textstyle { \frac { 1 } { 6 } }$ are absorbed in $\mathbf { F }$ and $\dot { \mathbf { F } }$ for computational convenience. Finally, the quantity $t _ { \mathrm { n e x t } } = t _ { i } + \Delta t _ { i }$ is introduced for decision-making in the Hermite scheme.

We note that, strictly speaking, the evaluation of the two higher force derivatives can be omitted in the Hermite AC formulation, as is done in NBODY 4, the only significant draw-back being the need to construct new time-steps from lower derivatives. In the latter case, we employ the conservative expression

$$
\begin{array} { r } { \Delta t = \frac { 1 } { 2 } \eta \operatorname* { m i n } \left\{ | \mathbf { F } | / | \dot { \mathbf { F } } | , t _ { \mathrm { c r } } | \right\} , } \end{array}
$$

with $t _ { \mathrm { c r } }$ the initial crossing time. However, the extra cost for the standard versions is very small, both initially and at subsequent initializations, and consistency with the difference formulation is retained. The initialization of the latter method contains one essential step more, i.e. conversion of all force derivatives to divided differences according to the formulae of section 2.2. On the other hand, the corresponding time-steps are not truncated to commensurate values.

# 8.8 Regularized polynomials

The case of primordial binaries discussed above also requires special attention initially. Thus it is elegant and numerically more accurate to begin a KS solution at $t = 0$ , instead of delaying by up to half a period when the selection would otherwise be made. Since the primordial binary components are already ordered pair-wise, the regularized quantities can be initialized for each pair in turn satisfying the usual close encounter condition $r _ { i j } < R _ { \mathrm { c l } }$ without the time-step test; otherwise direct integration will be used. We shall now concentrate on a given pair with index $i$ .

Initialization of regularized polynomials is also required at subsequent times as a result of close encounters. The following treatment combines both cases if it is assumed that the two selected particles, $m , m , m _ { l }$ , have already been placed in adjacent locations with pair index $i$ and all arrays are updated, such that the situation is similar to the above.

Standard force polynomials are first formed for each component following the procedure outlined in the previous section. In a general situation, neighbour lists contain single particles as well as the c.m. locations corresponding to the KS components. For the irregular contributions the summation is over both components of other perturbed binaries, whereas the point-mass approximation can normally be used for most of the regular interactions. The two individual quantities $\mathbf { F } _ { 2 i - 1 }$ and $\mathbf { F } _ { 2 i }$ are combined to give the new c.m. force by

$$
{ \bf F } _ { \mathrm { c m } } = \left( m _ { 2 i - 1 } { \bf F } _ { 2 i - 1 } + m _ { 2 i } { \bf F } _ { 2 i } \right) / ( m _ { 2 i - 1 } + m _ { 2 i } ) ,
$$

and likewise for the derivative, $\dot { F } _ { \mathrm { c m } }$ . However, the more expensive second and third derivative are obtained by one summation, using the binary c.m. which is sufficient for the present purpose. The last part of the c.m. initialization proceeds as described in the previous section.

Next it is the turn of the KS polynomials to be constructed. The basic variables $\mathbf { U }$ , $\mathbf { U } ^ { \prime }$ , $R$ , $h$ are initialized in the standard way of section 4.4, whereupon the perturber list is formed from the existing neighbour list if available (i.e. NBODY 5 and NBODY 6). A direct selection is carried out if $N$ is small, whereas for $N B O D Y 4$ the HARP and GRAPE provide the desired list of candidates. Perturbers $m _ { j }$ are then selected according to the tidal approximation by

$$
r _ { i j } < \left[ \frac { 2 m _ { j } } { ( m _ { k } + m _ { l } ) \gamma _ { \mathrm { m i n } } } \right] ^ { 1 / 3 } R .
$$

A more efficient criterion, $r _ { i j } ^ { 2 } > f ( m ) \lambda ^ { 2 } R ^ { 2 }$ with $f ( m ) = 2 m _ { 1 } / m _ { N + i }$ involving the maximum mass, $m _ { 1 }$ , is first used to exclude more distant particles. Recall that $\lambda = \gamma _ { \mathrm { m i n } } ^ { - 1 / 3 }$ is a subsidiary c.m. distance parameter.

It is sometimes the case in the AC method that the neighbour list is not sufficiently large to ensure that enough perturbers can be selected when using the apocentre condition $\lambda a _ { i } ( 1 + e _ { i } ) \ < \ R _ { \mathrm { s } }$ .§ However, this is not usually a problem for large $N$ or hard binaries.

Considerable care is involved in forming the highest derivatives of the KS force polynomials, especially in Hermite formulations that employ additional differentiation (cf. section 4.6). The essential procedure consists of the following steps summarized in Algorithm 8.1.

Algorithm 8.1. Initialization of KS polynomials.   

<table><tr><td>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15</td><td>Predict rj,rj for all the perturbers to order Fj Obtain P and P by summation over all perturbers Add any external effects on the relative motion R, R Introduce regularized derivative by P&#x27;= RP Define relative perturbation γ = |P|R²/(m2i-1 + m2i) Scale P and P&#x27; by the slow-down factor if κ &gt;1 Construct Q= LTP and the expression for Fu Form Fy, t(2), t(3), h&#x27;, h(2) by explicit differentiatin Include Q= LTP and Q&#x27; in Fy,h(2), h(3), t(4) Save f2 RQ， = 1(RQ)&#x27;, ho = h for corrector Derive two of the terms in Q(2) = (CTP)&quot; using L(U&quot;) ,F(3),h(4),t(5) t(6) by boot-strapping Evaluate F(2), Improve F (2) F (3） h(3), h(4) to order Q(2) IT Set regularized time-step △r,including perturbation Generate Stumpff coefficients c3, C4, C5, c4(4z), ℃5(4z) Find △t from △τ to order t(6) with c4(4z),c5(4z)</td></tr></table>

This condensed algorithm is almost self-explanatory. Note that the derivatives F(2 ) and F(3) are required for high-order prediction in the Stumpff formulation, with the short-hand notation $\mathbf { F } _ { \mathrm { U } } = \mathbf { U } ^ { \prime \prime }$ . As for the slow-down factor $\kappa$ , the procedure differs slightly from that in chain regularization and will be discussed subsequently. In any case, the nominal value $\kappa = 1$ is assigned for most perturbed initializations. We recall that the perturbing force is obtained from the expression $\mathbf { P } = \mathbf { F } _ { k } - \mathbf { F } _ { l }$ and $\mathbf { Q } = { \mathcal { L } } ^ { \mathrm { T } } \mathbf { P }$ as defined in section 4.7. Being of a tidal nature, this has the advantage that only relatively nearby members (specified in terms of $\gamma _ { \mathrm { m i n } }$ ) need to be selected. For the regularized time-step we still use the original criterion [Aarseth, 1972b]

$$
\Delta \tau = \eta _ { U } \left( \frac { 1 } { 2 \left| h \right| } \right) ^ { 1 / 2 } \frac { 1 } { ( 1 + 1 0 0 0 \gamma ) ^ { 1 / 3 } } ,
$$

where $\eta _ { U }$ is an input parameter. Hence this gives $2 \pi / \eta _ { U }$ steps per unperturbed orbit, which is reduced by a factor of 10 for $\gamma \simeq 1$ . In the case of nearly parabolic orbits, the factor $1 / 2 | h |$ is replaced by $R / ( m _ { k } + m _ { l } )$ which has the property of yielding a small relative change in the variables. If desired, an additional condition to ensure convergence of the Taylor series solution may be obtained by considering the predicted change of the orbital energy,

$$
\Delta h = h ^ { \prime } \Delta \tilde { \tau } + { \textstyle \frac { 1 } { 2 } } h ^ { \prime \prime } \Delta \tilde { \tau } ^ { 2 } ,
$$

and specifying some tolerance for the relative change (e.g. $0 . 0 0 1 | h |$ but taking care near zero). The smallest of the two values given by (8.59) and (8.60) may then be chosen for the regularized step. At present the second algorithm is only used for initializations, whereas subsequent values of $\Delta \tau$ are restricted to an increase by a factor of 1.2.

The theory of the Stumpff coefficients is given in section 4.7 [cf. Mikkola $\&$ Aarseth, 1998]. Suffice it to note that $\tilde { c } _ { 4 } ( 4 z )$ , $\tilde { c } _ { 5 } ( 4 z )$ with argument $4 z = - 2 h \Delta \tau ^ { 2 }$ are used to modify the last two terms in the Taylor series for the physical time interval, while the first three coefficients appear in the predictor and corrector. In comparing this method with the basic Hermite formulation, it can be seen that the Stumpff coefficients have values close to unity for properly chosen time-steps, $\Delta \tau$ .

The algorithm above is also relevant for the standard Hermite KS method. Thus only steps 10 and 15 are not needed in this treatment, although the refinement of steps 13 and 16 (to order $t ^ { ( 6 ) }$ ) was not implemented for some time. A comparison of the two methods (without energy stabilization) can be found elsewhere [Mikkola & Aarseth 1998], together with the original derivation. In this connection we remark that in order to compensate for a larger recommended value of $\eta _ { U }$ for the Stumpff method (i.e. 0.2 vs 0.1), a slightly steeper perturbation dependence in (8.59) may be beneficial.

We conclude by remarking that even the earlier KS difference formulation [cf. Aarseth, 1985a] has many similarities with the procedures above. Thus the number of equations to be integrated are actually less but on balance the Hermite schemes are preferable, with the Stumpff method being the most efficient at the cost of some extra programming efforts. However, the original difference method may be useful for problems where it is impractical to calculate the time derivative of the perturbing force.

# 9 Decision-making

# 9.1 Introduction

$N$ -body simulations involve a large number of decisions and the situation becomes even more complex when astrophysical processes are added. The guiding principle of efficient code design must be to provide a framework for decision-making that is sufficiently flexible to deal with a variety of special conditions at the appropriate time. Since the direct approach is based on a star-by-star treatment at frequent intervals, this prerequisite is usually satisfied. However, we need to ensure that the relevant tests are not performed unnecessarily. The development of suitable criteria for changing the integration method or identifying procedures to be carried out does in fact require a deep understanding of the interplay between many different modes of interactions. Hence building up the network for decision-making is a boot-strapping operation needing much patience and experience. The aim of a good scheme should be that this part of the calculation represents only a small proportion of the total effort.

This chapter discusses several distinct types of decisions necessary for a smooth performance. First we deal with the important task of selecting the next particle, or block of particles, to be advanced in time. The challenge is to devise an optimized strategy in order to reduce the overheads. Another aspect concerns close encounters, either between single particles or where one or more subsystems already consist of binaries. Such interactions may be studied by multiple regularization or procedures for hierarchical systems in the case of stable configurations. Once selected for special treatment, these systems may need to be terminated either due to external perturbations or internal evolution. The escape process is a characteristic feature of star cluster evolution and it is desirable to remove distant members in order to concentrate on the bound system. Other algorithms discussed below are concerned with mass loss from evolving stars as well as physical collisions. A well-tried scheme for error checking by relying on energy conservation is also described. Finally, it is worth emphasizing that all the above procedures are completely automatic. Ideally a large-scale simulation should proceed from start to finish without any external intervention.

# 9.2 Scheduling

The procedure of determining the next particle(s) for consideration is known as scheduling, which is a queueing problem. Although many solutions to this logistical challenge exist, it is often better to develop special procedures by exploiting certain features. In the following we distinguish between small and large $N$ -values. The basic problem can be formulated as follows. Given a wide distribution of $N$ time-steps, $\Delta t _ { j }$ , and the corresponding times, $t _ { j }$ , of the last force evaluation, the next particle to be advanced is selected by

$$
i = \operatorname* { m i n } _ { j } \left\{ t _ { j } + \Delta t _ { j } \right\} ,
$$

such that $t = t _ { i } + \Delta t _ { i }$ defines the new time. Moreover, in the case of quantized time-steps, a number of particles may satisfy this condition.

Let us begin by outlining a simple scheme as follows. Construct a list $L$ containing all particles satisfying $t _ { j } + \Delta t _ { j } < t _ { \mathrm { L } }$ . Initially $t _ { \mathrm { L } } = \Delta t _ { \mathrm { L } }$ , where $\Delta t _ { \mathrm { L } }$ is a suitably small time interval that is modified to stabilize the list membership on $N ^ { 1 / 2 }$ at each updating of $t _ { \mathrm { L } }$ and $L$ . A redetermination of the list is made as soon as $t > t _ { \mathrm { L } }$ , followed by another search over all the members. The next particle to be advanced is then determined using (9.1) for the list $L$ .

A more sophisticated algorithm based on the above was developed for the code NBODY 2 [Aarseth, 2001b]. The list is now ordered by sequential sorting such that the next particle due to be advanced is simply given by the next member. A complication arises for repeated small steps in the interval $\Delta t _ { \mathrm { L } }$ . In order to ensure that the global time increases monotonically, we employ an insert procedure which maintains the sequential ordering. Thus the index of a particle satisfying $t + \Delta t _ { i } < t _ { \mathrm { L } }$ , evaluated at the end of the cycle, is inserted at the appropriate sequential location. The interval $\Delta t _ { \mathrm { L } }$ is stabilized on a membership chosen as a compromise between the cost of sorting the quantities $t _ { j } + \Delta t _ { j }$ and inserting a small number of particles in the sequential list. Thus a target membership of $2 N ^ { 1 / 2 }$ is chosen initially but the value is modified according to the number of inserts. In spite of this complication, comparison with the so-called ‘heap-sort algorithm’ advocated by Press [1986] favoured the present algorithm above $N \simeq 1 0 0$ , although the cost of both procedures is $\propto N \ln N$ .

With Hermite integration, the block-step structure presents a new feature because a number of particles from several levels are usually advanced together. This situation is handled in the following way. Given the array $\{ \tilde { t } _ { j } \equiv t _ { j } + \Delta t _ { j } \}$ and the smallest value, $t _ { \mathrm { m i n } }$ , the particles in the next block are those for which $\{ \tilde { t } _ { j } \} = t _ { \operatorname* { m i n } }$ . A list of members is maintained for the corresponding interval $\Delta t _ { \mathrm { L } }$ , with the membership stabilized on the square root of the effective population, $( N - N _ { \mathrm { p } } ) ^ { 1 / 2 }$ , where $N _ { \mathrm { p } }$ is the number of KS pairs. Unless there are changes in the particle sequence, this simply requires the next value of $t _ { \mathrm { m i n } }$ to be determined during the integration cycle itself. Hence the subsequent block-step is defined by $\operatorname* { m i n } \left\{ \tilde { t } _ { j } \right\} - t$ , where $t$ is the current time. A full $N$ search is also carried out a second time after each non-standard termination or initialization of special configurations, such as multiple regularizations, since this may have resulted in smaller time-steps prescribed at the current block time. Profiling tests show that this scheme is efficient at least up to $N \simeq 1 0 ^ { 5 }$ ; i.e. the overheads arising from (9.1) only account for at most $1 . 5 \%$ of total CPU.

Modern star cluster simulations often deal with a large number of primordial binaries [McMillan, Hut & Makino, 1990; Heggie & Aarseth, 1992]. If two-body regularization is used, it is necessary to have a separate scheduling algorithm because the corresponding physical time-steps are not quantized.∗ In a typical situation the majority of KS solutions are unperturbed, with look-up times of many periods which may still be small. Two different algorithms have been tried for determining the next KS solution to be advanced. An earlier version consisted of the following three-level approach. We begin by constructing a list of members for all KS pairs satisfying $t _ { i } + \Delta t _ { i } < t _ { \mathrm { b } }$ , where the epoch, $t _ { \mathrm { b } }$ , is updated by an interval, $\Delta t _ { \mathrm { b } }$ , stabilized on a membership of $N _ { \mathrm { p } } / 4$ . At each new block-step, another list is formed by selecting those pairs for which $t _ { j } + \Delta t _ { j } \leq t _ { \mathrm { b l o c k } }$ , where $t _ { \mathrm { b l o c k } }$ defines the block boundary time for direct integration. This second list is then examined before each new KS step to determine the smallest look-up time. The first list is also initialized when there is a change in the sequence, but this occurs much less frequently than the renewals after the interval $\Delta t _ { \mathrm { b } }$ .

For relatively large values of $N _ { \mathrm { p } }$ , the sorting algorithm described above is a better alternative. Again the principle of sequential selection is maintained by the insert procedure. The sorted list is stabilized on a membership of 2N 1/2p as a compromise between renewals and list size. The conditions for reconstructing the full time-step list are the same as above, namely at the end of the interval $\Delta t _ { \mathrm { L } }$ or after each change in the particle sequence. Most of the latter changes occur at the end of a block-step and are much less frequent (by a factor of about $1 0 ^ { 4 }$ ) in large simulations. Since the relevant pointer is advanced by one at the beginning of each block-step, the current value must also be reduced by one on exit. Although the number of inserts may be comparable to the total number of KS steps due to some small values of $\Delta t _ { i }$ , the insert procedure is speeded up with an appropriate initial guess based on the remaining interval. Profiling of the relative costs shows that the second algorithm for KS selection is significantly faster for large memberships and this procedure has in fact been implemented in the Hermite codes.

Finally, for completeness, we also mention the independent and efficient block-step algorithm of McMillan [1986] that was employed in the tree code described in section 6.3 [cf. McMillan & Aarseth, 1993].

# 9.3 Close two-body encounters

The question of when to regularize a close encounter is based on considerations of numerical accuracy as well as computational efficiency. However, given that the number of such method changes is relatively small in a typical calculation, the decision-making must be aimed at gaining accuracy. In fact, introduction of the relative motion does not alter the cost per step significantly on conventional computers. Now only one particle is advanced by direct integration, albeit with some force summations over both components, whereas the cost of the regularized solution depends on the perturber number together with initialization and termination. Hence in the limit of few perturbers, the cost of integrating a binary essentially reduces to that of a single particle.† Since hyperbolic two-body encounters are relatively infrequent compared with the various types of bound interactions, the main consideration is to define dominant two-body motion. The benefit of switching to KS regularization is two-fold: accuracy is gained while reducing the number of steps per orbit.

Let us describe an encounter between two stars of mass $m _ { k }$ , $m _ { l }$ in terms of the deflection angle [Chandrasekhar, 1942]

$$
\cos { \delta } = \left[ 1 + \frac { R ^ { 2 } V _ { 0 } ^ { 4 } } { G ^ { 2 } ( m _ { k } + m _ { l } ) ^ { 2 } } \right] ^ { - 1 / 2 } ,
$$

where $R$ is the impact parameter and $V _ { 0 }$ is the pre-encounter relative velocity. We now define a close encounter by a total deflection $2 \delta = \pi / 2$ and replace $V _ { 0 }$ by the approximate rms velocity from the virial theorem, $( G N \bar { m } / 2 r _ { \mathrm { h } } ) ^ { 1 / 2 }$ . For equal masses, the close encounter distance is given by

$R _ { \mathrm { c l } } = 4 r _ { \mathrm { h } } / N$ (cf. (1.9)). However, we are dealing with centrally concentrated clusters so it is more prudent to use the density-related expression

$$
R _ { \mathrm { c l } } = 4 r _ { \mathrm { h } } / [ N ( \rho _ { \mathrm { d } } / \rho _ { \mathrm { h } } ) ^ { 1 / 3 } ] ,
$$

where $\rho _ { \mathrm { d } } / \rho _ { \mathrm { h } }$ is the central density contrast (to be discussed in chapter 15). With both integration schemes, the corresponding time-scale for a typical parabolic encounter is found empirically to be

$$
\Delta t _ { \mathrm { c l } } \simeq 0 . 0 4 ( \eta _ { I } / 0 . 0 2 ) ^ { 1 / 2 } ( R _ { \mathrm { c l } } ^ { 3 } / \bar { m } ) ^ { 1 / 2 } ,
$$

where $m$ is the mean mass (i.e. $1 / N$ in $N$ -body units).

Having defined dynamically relevant parameters for close two-body encounters, we now turn to the actual implementation. If a particle $k$ satisfies the condition $\Delta t _ { k } < \Delta t _ { \mathrm { c l } }$ , a search is made for other nearby particles. For large $N$ , this procedure uses either the neighbour list (NBODY 5, NBODY 6) or an existing list containing short steps (NBODY 4); otherwise all particles need to be considered. Every particle inside a distance $2 R _ { \mathrm { c l } }$ is recorded $^ \ddagger$ and the closest single particle is denoted by index $l$ . The pair $k , l$ is tentatively accepted for regularization, provided the minimum distance condition $R < { R _ { \mathrm { c l } } }$ is satisfied and, in the case of other close particles $j$ , the two-body force is dominant which requires

$$
( m _ { k } + m _ { l } ) / R ^ { 2 } > ( m _ { l } + m _ { j } ) / | { \bf r } _ { l } - { \bf r } _ { j } | ^ { 2 } .
$$

This condition excludes the possibility of particle $l$ being close to another regularized pair. It is also prudent to accept approaching particles only (i.e. $\dot { R } < 0$ ). Moreover, nearly circular orbits may be included by extending the radial velocity test to angles slightly less than $9 0 ^ { \circ }$ , using

$$
\mathbf { R } \cdot ( { \dot { \mathbf { r } } } _ { k } - { \dot { \mathbf { r } } } _ { l } ) < 0 . 0 2 [ R ( m _ { k } + m _ { l } ) ] ^ { 1 / 2 } .
$$

This modification is especially useful in the difference formulation since the velocity $\dot { \mathbf { r } } _ { l }$ is not predicted, in which case a factor 0.1 is used instead. Note that, with Hermite integration, synchronization of time-steps is required but the steps tend to be identical because a relative criterion is employed. If necessary, we achieve synchronization by halving the value of $\Delta t _ { k }$ , but only if $t _ { 0 , l } + \Delta t _ { l } < t + \Delta t _ { k }$ .

If massive binaries with low eccentricity are present, the time-step condition (9.4) may be too conservative for a close encounter search. Such binaries are often quite energetic and may contribute noticeably to systematic errors. A separate search procedure allowing somewhat wider criteria has therefore been included, i.e. $\Delta t _ { k } < 4 \Delta t _ { \mathrm { c l } }$ and $m _ { k } > 2 \bar { m }$ . The closest single particle is then identified from either the neighbour list (NBODY 6) or a list of short time-steps $\left( G R A P E \right)$ . Provided we have $E _ { \mathrm { b } } < \epsilon _ { \mathrm { h a r d } }$ , $e < 0 . 5$ and the estimated nearest neighbour perturbation is relatively small, the binary components are chosen for KS regularization. This procedure can be very beneficial for systems with significant mass dispersion.

Following acceptance of the regularization conditions, the initialization proceeds as described in section 8.8. The next question relating to decision-making is concerned with the possible termination of a regularization. We distinguish between hard and soft binaries, as well as hyperbolic fly-by’s, since these cases require different considerations. The latter are simplest and for them the termination conditions $R > R _ { 0 }$ , $\dot { R } > 0$ may be employed, where $R _ { 0 }$ is the initial separation (taken as $2 a$ for hard binaries). An additional criterion based on the perturbation is also used to prolong the integration in case $R _ { 0 } < R _ { \mathrm { c l } }$ (see below).

Soft binaries require more care since high eccentricities are often involved. Hence termination during the outward motion with $R > R _ { \mathrm { c l } }$ might be followed by a new initialization after the apocentre passage even if the maximum perturbation is modest. Hence if such a binary is in a lowdensity region this switching might occur repeatedly unless some precaution is taken. Instead we introduce a secondary perturbation parameter, $\gamma _ { \mathrm { m a x } }$ , (usually 0.01) and employ the termination conditions

$$
R > R _ { 0 } , \gamma > \gamma _ { \mathrm { m a x } } ,
$$

otherwise $\lambda R > R _ { \mathrm { s } }$ is used for the AC scheme.

Hard binaries often experience strong perturbations without suffering exchange. Thus if $\gamma > 0 . 2$ (say) a search for the dominant perturber is made based on the vectorial force. Termination with subsequent selection of the new component is only carried out if the negative radial velocity condition is also satisfied. In the rare case of no such test being successful before $\gamma = 0 . 5$ is reached, a direct comparison of dominant force terms among the perturbers usually results in a new companion being identified, whereupon termination is activated.§

Termination in the Hermite scheme has been modified slightly to fit in with the existing block-steps. Thus, except for collisions, it is advantageous to switch over to direct integration at the end of the current block-step instead of the need to create a smaller new step. Even if the termination conditions are satisfied, the regularized solution is extended until the corresponding physical time-step exceeds the remaining interval,

$$
\Delta t _ { 2 i - 1 } > t _ { \mathrm { b l o c k } } - t ,
$$

where $i$ is the pair index. The final solution is then predicted at the time $t _ { \mathrm { b l o c k } }$ by iteration of the regularized time (discussed in chapter 11). This novel procedure works well because the block-steps are usually small compared with the time-scale for significant changes in two-body configurations; i.e. the very nature of a strong perturbation implies a small value of the associated centre-of-mass (c.m.) step.

In conclusion, the identification of dominant two-body motion for KS regularization and its termination is essentially carried out with only two parameters, the close encounter time-step, $\Delta t _ { \mathrm { c l } }$ , and individual dimensionless perturbation, $\gamma _ { i }$ .

# 9.4 Multiple encounters

Compact subsystems where binaries are involved in strong interactions with single particles or other binaries may be treated by several types of multiple regularization described previously. Since many aspects of decision-making are similar, we concentrate on the more versatile chain regularization method. Let us first consider the case of a single particle of mass $m _ { j }$ approaching a hard binary with component masses $m _ { k }$ and $m _ { l }$ , semi-major axis $a$ and eccentricity $e$ . A convenient time to check for chain regularization is at each binary apocentre passage, provided $\Delta t _ { \mathrm { c m } } < \Delta t _ { \mathrm { c l } }$ . Thus a small value of the c.m. time-step ensures a strong interaction. The following conditions for the intruder need to be satisfied before the configuration can be selected for treatment. In addition to a negative radial velocity, we employ the condition of a compact subsystem,

$$
\left| \mathbf { r } _ { \mathrm { c m } } - \mathbf { r } _ { j } \right| < \operatorname* { m a x } \left\{ 3 R _ { \mathrm { g r a v } } , R _ { \mathrm { c l } } \right\} .
$$

Here $R _ { \mathrm { g r a v } }$ is the characteristic gravitational radius defined by

$$
R _ { \mathrm { g r a v } } = ( m _ { k } m _ { l } + m _ { \mathrm { c m } } m _ { j } ) / | E _ { \mathrm { b } } + E _ { \mathrm { o u t } } | ,
$$

with $E _ { \mathrm { b } }$ , $E _ { \mathrm { o u t } }$ the binding energies of the inner and outer relative motion. If the subsystem is not well bound (i.e. $E _ { \mathrm { o u t } } \gg 0$ ), we employ the expression $R _ { \mathrm { g r a v } } = { \textstyle \frac { 1 } { 2 } } ( R + | \mathbf { r } _ { \mathrm { c m } } - \mathbf { r } _ { j } | )$ instead for decision-making purposes, with $R$ the binary separation. In order to ensure a strong interaction, the condition for a small pericentre distance is also imposed by

$$
a _ { \mathrm { o u t } } ( 1 - e _ { \mathrm { o u t } } ) < | a | ( 1 + e ) ,
$$

where $a _ { \mathrm { o u t } }$ is the semi-major axis of the intruder with respect to the binary c.m. and $e _ { \mathrm { o u t } }$ is the corresponding eccentricity. Moreover, a factor 2 may be included on the right-hand side for small apocentre distances (e.g. $a _ { \mathrm { o u t } } ( 1 + e _ { \mathrm { o u t } } ) < 0 . 0 1 R _ { \mathrm { c l } } ,$ ), and even a factor 2.5 might be tried for large outer eccentricities¶ (e.g. $e _ { \mathrm { o u t } } > 0 . 9$ ).

The condition (9.9) ensures that the transition from a perturbed KS system is not made until the interaction can be said to be strong, and chain regularization becomes a more appropriate solution method. For a parabolic intruder orbit and equal masses, $R _ { \mathrm { g r a v } } = 6 a$ and the perturbation at this distance would only be a few per cent, whereas the remaining time until maximum interaction barely exceeds one orbital period. However, it is more efficient to initiate the chain regularization with the existing KS pair, otherwise another dominant solution may be initialized before the next check. Because orbital phase is a random element here, the desirable change from a binary KS solution to chain regularization is usually achieved with the present criteria, but a small fraction of new hyperbolic KS motions do occur. Hence if a second approaching KS binary is terminated prematurely, both components are in fact subject to a distance test and may be selected, instead of the fourth particle being treated as a strong perturber.

Chain regularization may also be initiated with four members if two hard binaries approach each other closely. In this case the second binary is treated analogously with the single particle above and its internal energy added to $E _ { \mathrm { b } }$ for use by (9.10). We generalize (9.11) by enlarging the apocentre cross section such that the semi-major axes are added. Once accepted for treatment, both KS solutions are terminated in the usual way. A discussion of aspects pertaining to the actual integration will be presented in another chapter.

A more general chain selection scheme has been added in order to prevent the intruder approaching too closely before being identified, as might be the case between two apocentre passages. Thus if the perturbation is significant (say $\gamma > 0 . 2$ ), the configuration is examined more carefully. Before deciding on termination of the KS solution, we consider the suitability for chain regularization. The actual decision for acceptance is then made using the standard conditions (9.9) and (9.11).

Decision-making for termination is much more involved than in KS regularization. A search for escape candidates is performed after each integration step if $\begin{array} { r } { \sum _ { k } R _ { k } > 3 R _ { \mathrm { g r a v } } } \end{array}$ . Since this procedure requires velocity information, the basic variables are obtained after every integration step. The distances $R _ { k }$ are ordered and the index of the largest one with mass $m _ { \mathrm { e s c } }$ is noted. First we express the relevant distance and radial velocity in the local c.m. frame. Multiplication by the factor $M _ { \mathrm { s u b } } / ( M _ { \mathrm { s u b } } - m _ { \mathrm { e s c } } )$ , with $M _ { \mathrm { s u b } }$ the subsystem mass, then yields the corresponding distance $d$ and radial velocity $\dot { d }$ with respect to the remaining system, which for a chain membership $N _ { \mathrm { c h } } = 3$ would be the binary c.m. This gives rise to the approximate two-body equation

$$
\begin{array} { r } { E _ { \mathrm d } = \frac { 1 } { 2 } \dot { d } ^ { 2 } - M _ { \mathrm { s u b } } / d . } \end{array}
$$

The simplest case is a single particle being ejected from a three-body system with hyperbolic motion (i.e. $\dot { d } > 0$ , $E _ { \mathrm { d } } ~ > ~ 0 $ ). Such a particle is a candidate for escape provided $d \mathrm { ~ > ~ } 3 R _ { \mathrm { { g r a v } } }$ [cf. Standish, 1971]. In addition, we employ a subsidiary distance condition which may continue the solution for small external perturbations up to a somewhat larger distance. If $E _ { \mathrm { d } } < 0$ , termination also occurs for an extended orbit with $d > 2 R _ { \mathrm { c l } }$ , provided certain conditions are met. In practice it is beneficial to delay KS initialization for small pericentre separations. For this purpose the semi-major axis of the inner two-body motion is evaluated by inverting the expression $E _ { \mathrm { b } } = - m _ { k } m _ { l } / 2 a$ in (9.10). Combining with (9.12) we write $E _ { \mathrm { o u t } } = \mu _ { \mathrm { o u t } } E _ { \mathrm { d } }$ , where $\mu _ { \mathrm { o u t } } = m _ { \mathrm { e s c } } m _ { \mathrm { c m } } / M _ { \mathrm { s u b } }$ and $m _ { j } = m _ { \mathrm { e s c } }$ is the outer mass. Re-arranging terms, we finally obtain

$$
a = \frac { R _ { \mathrm { g r a v } } } { 2 + 2 \frac { m _ { j } } { \mu } ( 1 + \frac { R _ { \mathrm { g r a v } } } { M _ { \mathrm { s u b } } } E _ { \mathrm { d } } ) } ,
$$

with $\mu = m _ { k } m _ { l } / m _ { \mathrm { { c m } } }$ . Consequently, we delay starting a new two-body solution for any value of (9.12) in the pericentre region $R \ < \ a$ . The most distant single particle is treated similarly if $N _ { \mathrm { c h } } > 3$ , except for the semi-major axis condition above. Now the remaining subsystem is retained, whereupon initialization takes place as described previously and the ejected particle is prepared for direct integration in the usual way.

Configurations with $N _ { \mathrm { c h } } > 3$ may also contain two particles escaping together, rather than just one. Provisional close components are identified by examining the smallest particle separation at either end of the chain. Again the procedure above is used, with (9.12) describing the relative motion of the combined c.m. Such particle pairs may be initialized as one KS solution if the separation is suitably small. The alternative case of $E _ { \mathrm { d } } < 0$ and an extended orbit is also considered. Thus $N _ { \mathrm { c h } } = 4$ and the potential binary exerting a small perturbation on the two other particles may result in termination with two separate KS solutions. Furthermore, two KS solutions may be initialized if the two smallest distances are well separated; e.g. $R _ { 1 } + R _ { 3 } < R _ { 2 } / 5$ , where $R _ { 2 }$ is the middle distance.

Change of membership by the addition of an intruder, followed by escape of another body may lead to long-lived systems that become timeconsuming when treated by chain regularization. At the simplest level, stable triples form during strong binary–binary interactions and may persist over long intervals even in the presence of external perturbations. The possibility of more complex structures also needs to be considered. Thus the case $N _ { \mathrm { c h } } = 4$ with an inner or outer binary of small size can be reduced to a hierarchical triple and likewise a five-body subsystem may be simplified. In the event of approximate stability being satisfied, the chain treatment is replaced by the appropriate combination of KS and direct solutions. Although semi-stable systems of higher orders are relatively rare during chain regularization, it is desirable to include such terminations in the decision-making. Fortunately, the available two-body separations together with the value of $N _ { \mathrm { c h } }$ can be used to distinguish the different cases (cf. section 11.7).

Finally, we note that procedures exist for initiation of unperturbed treatments of three-body regularization [Aarseth & Zare, 1974] as well as four-body chain regularization [Mikkola & Aarseth, 1990]. The unperturbed global four-body regularization [Heggie, 1974; Mikkola, 1985a] was also used for some time [cf. Aarseth, 1985a] until replaced by the chain method for $N = 4$ . Although the selection criteria are essentially similar to those above, the relevant procedures will be discussed later in connection with initialization and termination.

# 9.5 Hierarchical configurations

The formation and persistence of hierarchical systems poses difficult technical problems for $N$ -body simulations. Such configurations are known to exist in the Galactic field, and it is therefore not surprising that they should appear in cluster models containing a significant binary population. The technical problem arises because the inner binary in a triple invariably has a short period that needs to be integrated as a perturbed KS solution over long time intervals, and likewise the outer orbit by the direct method. It has been known for a long time [cf. Harrington, 1972] that most observed triples appear to be quite stable as indicated by their age. According to perturbation theory, the inner semi-major axis does not exhibit any secular effects for sufficiently large ratios of the outer pericentre to the inner apocentre distance and this feature can be exploited in numerical integrations.

A number of systematic studies of triple systems have been made in order to determine the boundaries of stable configurations. Most of these investigations [cf. Harrington, 1975; Eggleton & Kiseleva, 1995] have specifically addressed the problem of comparable masses. However, only a restricted set of initial conditions can be explored because of the large parameter space; i.e. usually both the inner and outer orbits are taken to be circular. The importance of stable hierarchies in cluster simulations has been recognized for some time and such criteria were used extensively [cf. Aarseth, 1985a] until replaced by a more general expression.

A new approach, based on the binary–tides problem [Mardling, 1995], inspired a semi-analytical stability criterion that holds for a wide range of outer mass ratios and arbitrary outer eccentricities [Mardling $\&$ Aarseth, 1999]. The limiting outer pericentre distance, $R _ { \mathrm { p } } ^ { \mathrm { c r i t } }$ , is expressed in terms of the inner semi-major axis, $a _ { \mathrm { i n } }$ , by the relation

$$
R _ { \mathrm { p } } ^ { \mathrm { c r i t } } = C \left[ ( 1 + q _ { \mathrm { o u t } } ) \frac { ( 1 + e _ { \mathrm { o u t } } ) } { ( 1 - e _ { \mathrm { o u t } } ) ^ { 1 / 2 } } \right] ^ { 2 / 5 } a _ { \mathrm { i n } } ,
$$

where $q _ { \mathrm { o u t } } = m _ { 3 } / ( m _ { 1 } + m _ { 2 } )$ is the outer mass ratio, $e _ { \mathrm { o u t } }$ is the corresponding eccentricity and $C \simeq 2 . 8$ is determined empirically. This criterion applies to coplanar prograde orbits, which are the most unstable, and ignores a weak dependence on the inner eccentricity and mass ratio $m _ { 1 } / m _ { 2 }$ .  Since inclined systems tend to be more stable, we adopt an heuristic linear correction factor of up to $3 0 \%$ , in qualitative agreement with early work [Harrington, 1972] and recent unpublished experiments.

The criterion (9.14) ensures stability against escape of the outermost body. However, the alternative outcome of exchange with one of the inner components also needs to be considered. The latter case is treated by the semi-analytical criterion [Zare, 1976, 1977]

$$
( { \bf J } ^ { 2 } E ) _ { \mathrm { c r i t } } = - { \frac { G ^ { 2 } f ^ { 2 } ( \rho ) g ( \rho ) } { 2 ( m _ { 1 } + m _ { 2 } + m _ { 3 } ) } } ,
$$

where $\mathbf { J }$ is the total angular momentum, with $f ( \rho )$ and $g ( \rho )$ algebraic functions of the masses which can be solved by iteration. If $\mathbf { J } ^ { 2 } E < ( \mathbf { J } ^ { 2 } E ) _ { \mathrm { c r i t } }$ (with $E < 0$ ), no exchange can occur and the inner binary retains its identity. However, this criterion is only sufficient; hence exchange is not inevitable if the criterion is violated, but if it does occur, escape follows. Application of the expression (9.15) shows that for planar prograde motion, the escape boundary lies above the exchange limit for $q _ { \mathrm { o u t } } < 5$ [cf. Mardling $\&$ Aarseth, 2001], and this is mostly satisfied in star cluster simulations.

We now define a triple that satisfies the outer pericentre condition $a _ { \mathrm { o u t } } ( 1 - e _ { \mathrm { o u t } } ) > R _ { \mathrm { p } } ^ { \mathrm { c r i t } }$ to be stable, in the sense that $a _ { \mathrm { i n } }$ will be assumed constant in spite of small short-term fluctuations. Such a system is then converted to a KS solution, where the combined mass $m _ { 1 } + m _ { 2 }$ plays the role of the inner component. Notwithstanding some current terminology, $* *$ we refer to this procedure as a merger but emphasize that it is only a temporary approximation and the two components are re-activated at the end. Quadruples and higher-order systems may also be treated in an analogous way by modifying the relation (9.14) appropriately, with a correction factor $f = 1 + 0 . 1 a _ { 2 } / a _ { \mathrm { i n } }$ for the smallest binary of size $a _ { 2 }$ .

The actual identification of a stable hierarchy is again carried out at the apocentre phase, provided $\Delta t _ { \mathrm { c m } } ~ < ~ \Delta t _ { \mathrm { c l } }$ . This may appear to be rather conservative but the additional condition $E _ { \mathrm { o u t } } ~ < ~ \frac { 1 } { 4 } \epsilon _ { \mathrm { h a r d } }$ is employed, mainly because a long life-time is still possible. Hence it follows that the time-step for the c.m. will be quite small for such configurations. We also note that even an unperturbed binary may be found inside a stable hierarchy. If we ignore the cube root of the mass ratio, this condition arises when we have

$$
a _ { \mathrm { o u t } } ( 1 - e _ { \mathrm { o u t } } ) > \lambda a _ { \mathrm { i n } } ( 1 + e _ { \mathrm { i n } } ) ,
$$

where λ = γ−1/3min . Hence a stability search is also performed during the check for unperturbed two-body motion, provided the time-step is below $\Delta t _ { \mathrm { c l } }$ . As an alternative to the more careful standard procedure, a fast evaluation of the stability parameter and inclination is carried out first if $\Delta t _ { \mathrm { c m } } < 4 \Delta t _ { \mathrm { c l } }$ , with existing information of the closest perturber. For a typical hard outer orbit, (9.16) allows for a large range of inner binary sizes and hence stable configurations of higher order are possible.

Occasionally, long-lived hierarchies occur that do not satisfy the stability criterion (9.14), even after the inclination effect has been included. A fraction of such systems exhibit relatively large outer eccentricity. In the case of high outer eccentricity and in analogy with tides in binaries, the amount of energy exchanged during a pericentre passage of the outer body is proportional to $( a _ { \mathrm { i n } } / R _ { \mathrm { p } } ) ^ { 6 }$ . Hence the small energy exchange at each passage owing to a small ratio would take a long time for the random walk process to reach $e _ { \mathrm { o u t } } \ > \ 1$ . In order to include such systems for a shorter interval, we introduce the experimental concept of practical stability (not yet included in $N B O D Y 6$ ). Accordingly, if $e _ { \mathrm { o u t } } > 0 . 9 9$ , we assign the number of outer periods by [cf. Aarseth $\&$ Mardling, 2001]

$$
n _ { \mathrm { o u t } } = 1 + 1 0 e _ { \mathrm { o u t } } / ( 1 - e _ { \mathrm { o u t } } ) ,
$$

where the corresponding time interval is used for termination.

Termination of hierarchies is somewhat similar to the case of hard binaries treated by KS in one respect. Based on the predicted apocentre perturbation, $\gamma _ { \mathrm { a p o } } \simeq \gamma [ a ( 1 + e ) / R ] ^ { 3 }$ , termination occurs if $\gamma _ { \mathrm { a p o } } > 0 . 2 5$ together with $R > a$ . The stability condition (9.14) must be checked regularly. This is done conveniently at each apocentre. Thus we compare the unperturbed expression $a _ { \mathrm { o u t } } ( 1 - e _ { \mathrm { o u t } } )$ , slightly modified by the empirical factor $1 - 2 \gamma$ , with $R _ { \mathrm { p } } ^ { \mathrm { c r i t } }$ which is now represented by $R _ { 0 }$ . The simple convention of associating each c.m. particle with a negative identification label, or name, (to be discussed later) allows the variable $R _ { 0 }$ to be used for a second purpose. Recall that it is also used as termination distance for regularized soft binaries. Finally, the inner components are again reinitialized as a KS binary in the usual way, whereas the outer component is treated as a single particle or another KS solution, as required.

# 9.6 Escapers

Star clusters evolve by losing members to the galactic field. It therefore makes sense to remove distant cluster members and concentrate on the bound system. Although the classical tidal radius might be expected to be a good choice for the cluster boundary, simulations show that a significant population is present further out [cf. Terlevich, 1987]. Likewise, stars above the escape energy may linger for a long time when the orbits are calculated in a fixed potential [Fukushige & Heggie, 2000]. Theoretical considerations also suggest that some orbits may reach quite large distances and still return to the cluster [Ross, Mennim & Heggie, 1997]. However, such orbits appear to be of a special type and only a small fraction of escapers in the present models exhibit this behaviour when their motion is investigated. The old criterion of using twice the tidal radius for escaper removal has therefore been retained [Aarseth, 1973], in conformity with other studies [Portegies Zwart et al., 2001].

As is well known [cf. Hayli, 1970; Wielen, 1972], the zero velocity boundary for the symmetrical Lagrange points, $L _ { 1 }$ and $L _ { 2 }$ , is highly flattened in the presence of a galactic field. Likewise, if a particle has a small excess energy, $E _ { i } > C _ { \mathrm { c r i t } }$ (cf. (8.17)), it can only escape in the vicinity of the Lagrange points. Consequently, most particles satisfying the energy escape criterion will experience random reflections inside the zero velocity boundary before finding the energy-dependent exit window. Hence kinetic energy in the $z$ -direction is converted to $x$ - or $y$ -motion, and vice versa, by the agency of the core as well as the non-symmetrical tidal torque. This behaviour is analogous to the absence of a third integral for eccentric orbits in certain galactic potentials [Aarseth, 1966b]. For completeness, we mention an extensive analysis of the escape process performed recently [Heggie, 2001].

The central distance of each single and c.m. particle, $i$ , is examined at regular intervals. For open clusters we employ the escape criterion

$$
\left| \mathbf { r } _ { i } - \mathbf { r } _ { d } \right| > 2 r _ { \mathrm { t } } ,
$$

where $\mathbf { r } _ { d }$ defines the density centre (to be discussed later) and $r _ { \mathrm { t } }$ is the scaled tidal radius given by (8.24). At the same time, the energy per unit mass, $E _ { i }$ , is obtained; this includes any external tidal field. Hence escapers from isolated systems may also be treated in a similar way, provided $E _ { i } > 0$ and a nominal value (say $1 0 r _ { \mathrm { h } }$ ) has been assigned to $r _ { \mathrm { t } }$ . In any case, the quantity $m _ { i } E _ { i }$ is needed in order to correct the total energy, permitting conservation to be maintained.

A given particle is removed from the data structure by compressing all arrays with members $j \geq i$ and reducing $N$ by one. Additionally, all relevant lists must be updated consistently, as well as the total mass and tidal radius. Since the distance between an escaper and other particles is usually fairly large, no force corrections are needed to account for the slight discontinuity. However, care is taken if a neighbouring single particle is present that does not satisfy the escape condition, when a delay may be imposed depending on the perturbing force.

In the case $i > N$ which defines a KS solution, we proceed as follows. First the c.m. particle is removed, using the procedure above. The corresponding KS components $m , m ,$ of pair $i - N$ are also removed after noting the binding energy $E _ { \mathrm { b } } = \mu _ { k l } h$ , with $\mu _ { k l }$ the reduced mass. Again the latter quantity is subtracted from the total energy and all the list arrays are modified consistently. From time to time even hierarchical systems escape. The treatment is similar to that for binaries, except that additional quantities relating to the inner binary must also be removed. Detailed procedures for escaper removal are discussed in Appendix C.

# 9.7 Mass loss and tidal interactions

A realistic simulation of stellar systems needs to consider various processes connected with the finite size of stars as well as their change of mass with time. The modelling of synthetic stellar evolution is based on fast look-up algorithms for the radius, luminosity and type as a function of the initial mass and age [Eggleton, Tout & Fitchett, 1989; Tout et al., 1997; Hurley, Pols & Tout, 2000]. Here we are mainly concerned with decision-making aspects for instantaneous mass loss due to stellar winds or supernovae explosions and processes related to tidal interactions.

Each star is assigned an evolutionary time-scale, $t _ { \mathrm { e v } }$ , when the relevant parameters are updated according to some prescription. As well as using the current mass, this scheme requires the initial mass, $m _ { 0 }$ , as a variable for several purposes. Suitably small time intervals are used for advancing $t _ { \mathrm { e v } }$ which produces fairly smooth changes in the basic quantities. In the Hermite scheme, all individual values of $t _ { \mathrm { e v } }$ are examined at small quantized intervals of 100–200 yr coinciding with the end of an integration cycle, or block-step. Each star is also characterized by a stellar type, $k ^ { * }$ , in order to distinguish different evolutionary states in the Hertzsprung– Russell (HR) diagram, which facilitates decision-making. For many years a basic scheme was used [cf. Tout et al., 1997] but this has now been replaced by a more general representation [Hurley, Pols & Tout, 2000] comprising some 16 types, ranging from low-mass main-sequence stars to neutron stars and black holes.

The introduction of evolutionary time-scales and types for c.m. particles as well provides greater flexibility of program control. Thus the former specifies the appropriate time for the next mass transfer episode in circularized binaries, whereas the latter is used to define the binary type.

Subsequent to a standard initial state ( $k ^ { * } = 0$ ), binaries may undergo chaotic energy exchange ( $k ^ { * } = - 1$ ) or tidal circularization ( $k ^ { * } = - 2$ ) until the orbit is circular ( $k ^ { * } = 1 0$ ), followed by Roche-lobe mass transfer ( $k ^ { * } = 1 1$ , etc.), of which there may be several distinct phases.

The process of tidal circularization has been described in detail elsewhere [cf. Mardling & Aarseth, 2001], together with chaotic motion, and some relevant algorithms will be given in a subsequent section. As far as decision-making is concerned, the orbital elements $a , e$ are updated in a smooth manner either at each pericentre passage of a perturbed binary or, more usually, at the time of rechecking unperturbed motion. Hence, in general, the computational effort here is relatively insignificant, although the recent inclusion of stellar spin ( $N B O D Y 4$ only) requires integration of some extra equations. Since the regularized coordinates for standard unperturbed binaries by convention specify the first point past apocentre, we need an algorithm for transforming the elements to pericentre. The phase angle is first advanced by half a physical period (i.e. $\pi / 2$ ). Using general transformation expressions [Stiefel $\&$ Scheifele, 1971], we take $\theta = \pi / 2$ and obtain the regularized coordinates and velocity

$$
\begin{array} { r } { \mathbf { U } = \mathbf { U } _ { 0 } \cos \theta + \mathbf { U } ^ { \prime } \sin \theta / \nu , } \\ { \mathbf { U } ^ { \prime } = \mathbf { U } _ { 0 } ^ { \prime } \cos \theta - \mathbf { U } _ { 0 } \sin \theta \nu , } \end{array}
$$

where $\nu = | { \textstyle \frac { 1 } { 2 } } h | ^ { 1 / 2 } .$ . Finally, if necessary, transformation to exact pericentre employs the analytical solution after solving Kepler’s equation. However, an actual integration is performed if the motion is perturbed. Further algorithms are given in Appendix D.4.

An interval of circular motion usually precedes the Roche stage which is triggered by the increase of stellar radii. Since this type of mass transfer is essentially continuous, we need to discretize it in order to fit in with the integration scheme. The process is initiated when one of the stars fills its Roche lobe, with the effective radius [Eggleton, 1983]

$$
r _ { \mathrm { R } } \simeq 0 . 4 9 q ^ { 2 / 3 } / [ 0 . 6 q ^ { 2 / 3 } + \ln ( 1 + q ^ { 1 / 3 } ) ] a ,
$$

where $q = m _ { k } / m _ { l }$ is the mass ratio, $m _ { k }$ being the primary. From the known mass transfer rate [cf. Tout et al., 1997], we limit the amount transferred to a small fraction (say $0 . 5 \%$ ) of the primary mass. The mass transfer activity is halted temporarily when the corresponding time exceeds the next c.m. force calculation time, whereupon there is a quiescent or coasting stage until $t _ { \mathrm { e v } }$ is exceeded again. During this process it is important to make sure that the look-up times of the individual components stay ahead of the c.m. value; otherwise mass loss without any transfer would occur. Once an active stage is completed, the relevant type indices and evolution times are updated. More details can be found in section 11.10.

Close binaries consisting of low-mass or degenerate stars are subject to magnetic and gravitational wave braking [cf. Tout et al., 1997]. Now the time-scale might be several Gyr, with correspondingly longer intervals between each orbital modification in the absence of mass loss. For convenience, the angular momentum losses due to magnetic braking and gravitational radiation at small separations $( < 1 0 R _ { \odot }$ ) are combined to yield the final semi-major axis by angular momentum conservation. Finally, the KS variables are scaled at constant eccentricity, followed by standard initialization in the case of perturbed motion (cf. (11.44)).

The actual procedures concerned with mass loss will be described later but it may be instructive here to consider how a supernova event is handled. Let us suppose that a massive component of a hard binary undergoes a sudden transition to a neutron star. According to consensus, such an object will generate a velocity kick because the rapid mass ejection is not symmetrical. Here we mention the main steps for implementing this effect, assuming that the kick occurs at an arbitrary phase (cf. section 15.5). After assigning a random phase shift $\theta$ in $[ 0 , \pi ]$ , equation (9.19) is employed to generate new regularized variables. This is followed by termination of the KS solution, together with corrections of the neighbour forces and total energy resulting from the mass loss. Even if the modified two-body motion is hyperbolic, a new KS regularization is initialized for consistency, subject to the condition $R < { R _ { \mathrm { c l } } }$ .

# 9.8 Physical collisions

The interaction of close binaries undergoing mass transfer frequently leads to the stage known as common-envelope evolution [Paczynski, 1976]. A significant fraction of these events results in coalescence of the two stars, accompanied by mass loss and should not be considered as collisions. For practical purposes it is useful to distinguish between hyperbolic encounters and nearly circular motion leading to the common-envelope stage, even though the former may occasionally produce the same outcome.†† Other types of collision also occur (i.e. induced inner eccentricity) and the possible formation of exotic objects is of particular interest.

The simplest case of collision is between two single stars in a hyperbolic regularized orbit. Although some giant stars are present, estimates indicate that such collisions are quite rare. Thus in a typical open cluster with $N \simeq 1 0 ^ { 4 }$ members, we have $R _ { \odot } / R _ { \odot } \simeq 5 \times 1 0 ^ { 4 }$ . We assume a provisional collision criterion $\ddag \ddag$ of the type obtained by smoothed particle hydrodynamics or SPH [e.g. Kochanek, 1992],

$$
R _ { \mathrm { c o l l } } = 1 . 7 \left( \frac { m _ { 1 } + m _ { 2 } } { 2 m _ { 1 } } \right) ^ { 1 / 3 } r _ { 1 } ^ { * } ,
$$

where $r _ { 1 } ^ { \ast }$ is the largest stellar radius. Although the decision-making for coalescence is quite different, the actual KS treatment is based on the same principles and need not be commented on specifically here. For clarity, we summarize the main steps of the collision procedure in Algorithm 9.1.

Algorithm 9.1. Physical collision in KS regularization.   

<table><tr><td>1</td><td>Identify the turning point by t&quot;t&quot; &lt;O, R&lt;a</td></tr><tr><td>2</td><td>Determine the pericentre distance,Rp Compare Rp with the collision distance, Rcoll</td></tr><tr><td>3</td><td></td></tr><tr><td>4</td><td>Predict back to the exact pericentre</td></tr><tr><td>5</td><td>Terminate the KS solution in the standard way</td></tr><tr><td>6</td><td>Form the new c.m. particle with rcm,rcm</td></tr><tr><td>7</td><td>Implement stellar evolution for mcm = mk + m</td></tr><tr><td>8</td><td>Replace body m by a massless particle</td></tr><tr><td>9</td><td>Perform mass-loss corrections of potential energy</td></tr><tr><td>10</td><td>Update lists to new single body, mcm</td></tr><tr><td>11</td><td>Obtain improved force polynomials for neighbours</td></tr><tr><td>12</td><td>Initialize force polynomials for mcm</td></tr><tr><td></td><td>Correct the total energy, Ecoll by μklh</td></tr><tr><td>13</td><td></td></tr></table>

The first point past pericentre is identified by comparing the sign of the old and new radial velocity, $t ^ { \prime \prime } = R ^ { \prime }$ , for $R < a$ . This algorithm is also used for determining the apocentre of binaries which requires the alternative condition $R > a$ . In order to have a regular expression for the distance of closest approach, we introduce the semi-latus rectum

$$
p = 4 ( \mathbf { U } \times \mathbf { U } ^ { \prime } ) ^ { 2 } / m _ { \mathrm { b } } ,
$$

with $m _ { \mathrm { b } } = m _ { k } + m _ { l }$ for brevity. Since $e ^ { 2 } = 1 - p / a$ and we have the energy relation $1 / a = ( 2 - 4 { \bf U } ^ { \prime } \cdot { \bf U } ^ { \prime } / m _ { \mathrm { b } } ) / R$ , this finally gives

$$
R _ { \mathrm { p } } = p / ( 1 + e ) .
$$

Note that the determination of the eccentricity and semi-major axis from the physical variables of a collision solution is prone to errors and may in fact lead to non-physical values, whereas $p$ contains numerically the factor

$R$ which compensates for the division. If the collision condition is satisfied, the actual pericentre is obtained by backwards integration together with a final iteration using the procedure described below. Having replaced two particles by one composite body, we create a so-called ‘ghost particle’ with zero mass and large distance so that it will be removed as a massless escaper. One possibility not mentioned in the collision algorithm is that step 12 may be replaced by initializing a KS solution of $m _ { \mathrm { { c m } } }$ with respect to another close single particle.

The case of collision inside a compact subsystem is much more frequent and quite complicated to deal with. Some of these events are of the common-envelope type which occur if at least one of the components has a dense core and an extended envelope, but technically the treatment is the same (cf. section 12.9). We now consider a situation with more than three chain members since the case $N _ { \mathrm { c h } } = 3$ leads to immediate termination after some simple procedures, followed by a new KS solution.

The first prerequisite is to have a decision-making algorithm for determining a possible collision. One way to identify the pericentre passage of two bodies in a system of arbitrary membership is to note when the quantity $1 / \textstyle \sum _ { j _ { - } } R _ { j } ^ { 2 }$ starts to decrease after successive increases. If $\operatorname* { m i n } \left\{ R _ { j } \right\} < 8$ max {r∗k, r∗l } at the same time, the smallest pericentre distance is determined after the first subsequent function evaluation. In chain regularization, the procedure for obtaining the osculating pericentre distance, $R _ { \mathrm { p } }$ , from (9.23) is given by Algorithm 18.1. The essential steps involved in achieving the objective of identifying tidal interaction or collision candidates are elucidated by Algorithm 9.2.

Algorithm 9.2. Pericentre determination in chain regularization.   

<table><tr><td>1 2 3</td><td>Determine the smallest pericentre distance, Rp Check distance criterion Rp &lt; 4 max {r*, r*} Form KS radial velocity from R&#x27; = 2Qk : QRk/t&#x27; Evaluate a using non-singular energy expression Obtain pericentre time, tp,by Kepler&#x27;s equation Convert to chain step △T = (tp/a-R&#x27;/mb)Rk/t&#x27;</td></tr></table>

Here $r _ { k } ^ { \ast } , r _ { l } ^ { \ast }$ denote the stellar radii and $m , m ,$ are the masses at each end of the smallest chain separation, $R _ { k }$ . Again the pericentre distance is obtained by (9.22) and (9.23), with $\mathbf { Q } _ { k }$ substituted for $\mathbf { U }$ . However, each velocity $\mathbf { Q } _ { k } ^ { \prime }$ needs to be modified by the factor $R _ { k } / t ^ { \prime }$ (with $t ^ { \prime } = 1 / L$ here) in order to convert from chain to KS derivatives. Formally the slowdown factor $\kappa$ should be included but $\kappa = 1$ is imposed here because of possible convergence problems in the solution of Kepler’s equation for high eccentricity. Note the extra factor 2 used to initiate the search which is based on osculating elements.

Evaluation of the semi-major axis from the physical variables at small pericentres suffers from numerical uncertainty. Instead we obtain the twobody energy from the regular expression

$$
E _ { \mathrm { b } } = E _ { \mathrm { c h } } - \mathcal { V } ,
$$

where $E _ { \mathrm { c h } }$ is the energy of the subsystem and $\nu$ represents the nondominant chain and non-chained contributions. From this the semi-major axis is obtained by $a = - { \textstyle \frac { 1 } { 2 } } m _ { k } m _ { l } / E _ { \mathrm { b } }$ . We remark that collisions represent near-singular conditions and care should therefore be exercised to work in terms of well-defined variables.

An analytical estimate for the pericentre time can be obtained by neglecting the perturbation of any nearby members, whereupon convergence is attained by iteration. The desired expression is derived by the following algorithm [Mikkola, private communication, 1999]. First we establish the unperturbed two-body relation

$$
d R ^ { \prime } / d t = d ( { \bf R } \cdot \dot { \bf R } ) / d t = m _ { \mathrm { b } } / R - m _ { \mathrm { b } } / a ,
$$

where $\dot { \mathbf { R } } ^ { 2 }$ has been replaced by $2 m _ { \mathrm { b } } / R - m _ { \mathrm { b } } / a$ . From the definition (4.4) a straightforward integration gives

$$
R ^ { \prime } - R _ { 0 } ^ { \prime } = m _ { \mathrm { b } } \tau - m _ { \mathrm { b } } t / a .
$$

Setting $R ^ { \prime } = 0$ at the pericentre, we obtain the regularized interva $^ { \ S \ S }$

$$
\Delta \tau = t _ { \mathrm { p } } / a - R _ { 0 } ^ { \prime } / m _ { \mathrm { b } } .
$$

The pericentre time, $t _ { \mathrm { p } }$ ( $< 0$ if $R ^ { \prime } < 0$ ) is obtained from Kepler’s equation,

$$
t _ { \mathrm { p } } = [ \theta - t _ { 0 } ^ { \prime \prime } / ( m _ { \mathrm { b } } a ) ^ { 1 / 2 } ] t _ { \mathrm { K } } / 2 \pi ,
$$

where $t _ { \mathrm { K } }$ is the period. Finally, if relevant, the KS interval (9.27) is converted to chain regularization time units by the scaling factor $R _ { k } / t ^ { \prime }$ . Note that $R _ { k } = Q _ { k }$ to high accuracy after reaching a small radial velocity. This is usually achieved in three iterations which cost the same as full integration steps. Since $a$ is obtained by means of the non-singular expression (9.24), the eccentricity is also well determined by $e = 1 - Q _ { k } / a$ .

Let us now suppose that the collision condition $R _ { \mathrm { p } } < R _ { \mathrm { c o l l } }$ is satisfied. A few of the procedures are the same as for hyperbolic collision but all are listed by Algorithm 9.3 for completeness.

Algorithm 9.3. Implementation of chain collision.   

<table><tr><td>1</td><td>Transform to rj,rj for all chain members</td></tr><tr><td>2 3</td><td>Evaluate the two-body energy from Eb = Ech -V Form coordinates and velocity of the c.m.particle</td></tr><tr><td>4</td><td>Implement stellar evolution for mcm = mk + ml</td></tr><tr><td></td><td>Create a massless particle at location of ml</td></tr><tr><td>5</td><td></td></tr><tr><td>6</td><td>Add the tidal energy correction △Φ to Ecoll</td></tr><tr><td></td><td>Prescribe new force polynomials for the neighbours</td></tr><tr><td>8</td><td>Compress the membership list {Ij} to remove j = l</td></tr><tr><td>9</td><td>Update the total energy by Eb to ensure conservation</td></tr><tr><td>10</td><td>Re-initialize the chain with reduced membership,Nch</td></tr></table>

The energy $E _ { \mathrm { b } }$ (a local quantity) is again obtained by (9.24). In order to maintain energy conservation, the change in potential energy in going from two particles to one is added to the quantity $E _ { \mathrm { c o l l } }$ which forms part of the total energy (defined in the next section). This differential effect, arising from the nearest neighbours, is also included for two-body collisions, where it tends to be quite small. From the negative sign convention, it can be seen that the addition of $\Delta \Phi = \Phi _ { 1 } - \Phi _ { 2 }$ preserves the value of the total energy, ${ \boldsymbol { E } } = { \boldsymbol { T } } + \Phi$ , with $\Phi _ { 1 }$ due to the interaction between the two colliding bodies and the other chain members, and $\Phi _ { 2 }$ arising from the c.m. approximation. Since the chain membership $\{ I _ { j } \}$ is contained in a sequential list, the massless particle is removed by compressing the array. This allows for re-initialization of the chain regularization directly, unless only two particles are left which implies termination.

In conclusion, we have seen how the membership of a chain regularization may be increased or also decreased by either escape or collision. General algorithms for changing the membership will be outlined in a subsequent section. Although such procedures illustrate the practical usefulness of the chain method, it should be emphasized that the technical treatment requires some complicated programming. However, the advantages of describing near-singular interactions in terms of well-defined variables are tangible.

# 9.9 Automatic error checks

The star cluster codes, which form the basis for discussion, contain a number of dissipative processes as well as discontinuous dynamical events. In this chapter, we have discussed mass loss, tidal circularization, collisions, escape and the temporary creation of stable hierarchies. Since each event or process is corrected for, it becomes possible to maintain an energy-conserving scheme, and its use as a check of the calculation is included as an option.

The change in total energy is monitored at regular time intervals and is considered to represent the global error, although the main source may well be connected with the integration of some difficult interaction. We compare the relative error, $q _ { \mathrm { E } } = | \Delta E / E |$ , with the specified tolerance, $Q _ { \mathrm { E } }$ , and have implemented the following scheme. If $0 . 2 Q _ { \mathrm { E } } < q _ { \mathrm { E } } < Q _ { \mathrm { E } }$ , the calculation is continued normally. On the other hand, if the error is larger there are two courses of action. Thus $Q _ { \mathrm { E } } < q _ { \mathrm { E } } < 5 Q _ { \mathrm { E } }$ results in a reduction of the time-step parameters $\eta$ or $\eta _ { I }$ and $\eta _ { R }$ by a factor $( q _ { \mathrm { E } } / Q _ { \mathrm { E } } ) ^ { 1 / 2 }$ . However, errors exceeding $5 Q _ { \mathrm { E } }$ are not acceptable and a restart is made from the last save of the common variables, together with a factor of 2 reduction of $\eta$ or $\eta _ { I } , \eta _ { R }$ . A further restart is allowed for, but such cases are usually connected with technical problems which may require attention. Finally, if $q _ { \mathrm { E } } < 0 . 2 Q _ { \mathrm { E } }$ , the time-step parameters are increased by a small amount unless already at their initial values which should not be exceeded.

Hence by adopting the old procedure of saving all common variables for acceptable solutions [Aarseth, 1966a], we have a practical scheme for controlling the progress of a simulation that can therefore be left to itself on a dedicated machine for long periods of time. Detailed investigations are carried out if the calculation is halted because the error limit has been exceeded. This requires the results to be reproducible, which is usually the case with workstation versions. However, time-sharing on special-purpose HARP or GRAPE computers may sometimes cause problems in this respect, due to small variations in the time ration and reloading of the data which affects the scheduling.

The present data structure allows the total energy to be obtained by adding different contributions which are evaluated separately. Thus the total energy is defined by a sum of ten terms as

$$
E = T + U + E _ { \mathrm { t i d e } } + E _ { \mathrm { b i n } } + E _ { \mathrm { m e r g e } } + E _ { \mathrm { c o l l } } + E _ { \mathrm { m d o t } } + E _ { \mathrm { c d o t } } + E _ { \mathrm { c h } } + E _ { \mathrm { s u b } } .
$$

The various quantities are listed in Table 9.1, together with brief definitions. Note that here $T$ and $U$ do not include any internal contributions from binaries or multiple subsystems. This definition arises naturally from the way in which the different classes of objects are integrated. For convenience, we have introduced some new definitions which correspond more closely to code usage, hence $E _ { \mathrm { t i d e } } = W$ . The collision energy, $E _ { \mathrm { c o l l } }$ , contains the tidal (or differential) energy corrections associated with the c.m. approximation when combining two particles. $\ P \ P$ Moreover, note that the energy budget contains two terms for multiple regularization. Thus $E _ { \mathrm { s u b } }$ remains constant and the original value is subtracted from the total energy at the end of an unperturbed multiple regularization, whereas the internal chain energy, $E _ { \mathrm { c h } }$ , changes with time and cannot be treated in the same way if we want (9.29) to be conserved during the interaction.

Table 9.1. Components of the energy budget.   

<table><tr><td>T</td><td>Kinetic energy of single bodies and c.m. particles</td></tr><tr><td>U</td><td>Potential energy of single and c.m. bodies</td></tr><tr><td>Etide</td><td>Tidal energy due to external perturbations</td></tr><tr><td>Ebin</td><td>Binding energy in regularized pairs,∑i μkthi</td></tr><tr><td>Emerge</td><td>Total internal energy of hierarchical systems</td></tr><tr><td>Ecoll</td><td>Sum of binding energies released in collisions</td></tr><tr><td>Emdot</td><td>Energy change from mass loss and Roche mass transfer</td></tr><tr><td>Ecdot</td><td>Neutron star kicks and common-envelope evolution</td></tr><tr><td>Ech</td><td>Total energy of any existing chain subsystem</td></tr><tr><td>Esub</td><td>Energy in unperturbed triple and quadruple subsystems</td></tr></table>

Some further comments on the entries in the table are in order. The expression for the potential energy contains the interaction between each KS pair and other pairs, as well as with single particles. For consistency, the energy of each perturbed KS solution is predicted to highest order before being accumulated in $E _ { \mathrm { b i n } }$ . As regards hierarchies, contributions from changes in the data structure are also included in the form of differential corrections, both at initialization and termination. Thus we need to take account of the changing nature of the equations of motion, since the resulting c.m. approximation affects the force on nearby particles. Various safety procedures are therefore employed to check the external perturbation on a hierarchical configuration before it is accepted for treatment (cf. Algorithm 11.3).

On conventional computers, the change in potential energy due to mass loss from single stars or binaries is obtained by explicit summation over all members. A separate quantity, $E _ { \mathrm { c d o t } }$ , accumulates the kinetic energy contained in the velocity kick when neutron stars are formed. By analogy with the other entries here, one could also introduce a quantity, $E _ { \mathrm { e s c } }$ , for the energy carried away by escaping members but, for historical reasons, the relevant correction is subtracted directly. However, information about the different escape processes is kept separately for further analysis.

A different strategy for mass-loss correction is possible when using GRAPE. Thus in addition to $\mathbf { F }$ and $\dot { \mathbf { F } }$ , the potential $\Phi$ is also evaluated by the hardware. For most cases, i.e. significant time-steps and small mass loss, the value at a subsequent time, $t \leq t _ { 0 } + \Delta t$ , is obtained from

$$
\Phi ( t ) = \Phi ( t _ { 0 } ) - { \dot { \mathbf { r } } } _ { 0 } \cdot \mathbf { F } .
$$

Moreover, any external tidal contributions contained in $\mathbf { F }$ are subtracted to give the net effect.

Given the general energy expression (9.29) for star cluster simulations, the question of the relative energy error usually quoted in the literature requires special consideration. We first remark that $| E |$ itself may be very large initially when studying primordial binaries. Moreover, the ejection of dynamically formed binaries or fast escapers may result in large changes of opposite sign. Consequently, we adopt a conservative definition of the relative error, based on the energy binding the cluster (discussed later),

$$
\alpha = \Delta E / ( T + U + E _ { \mathrm { t i d e } } ) .
$$

Again $T$ and $U$ represent the contributions from $N - N _ { \mathrm { p } }$ single objects, except that the pair-wise potential energies are evaluated more carefully. As a result of mass loss and other dissipative processes, the absolute value of the denominator tends to decrease with time and may in fact become quite small compared with the initial value. However, the energy exchanged, or liberated, in strong interactions may still be large in systems containing significant amounts of so-called ‘fossil fuel’. Moreover, the formation of hierarchies also absorbs some of the available interaction energy. Consequently, the accumulated quantity $\sum \Delta E$ for all the energy check intervals provides an alternative measure of the energy error, and in particular any systematic effects are readily evident.

The acceptable error tolerance is a matter of taste and depends on the type of problem being investigated. For general star cluster simulations, a typical value $\alpha \simeq 1 0 ^ { - 5 }$ per crossing time can usually be achieved using standard time-step parameters. However, it is desirable to aim for even smaller values above $N \simeq 1 0 ^ { 4 }$ in order to ensure an adequate description of energy generation in the core [Heggie, 1988], particularly because of the longer time-scale required. We defer a general discussion of numerical errors to section 13.2.

To increase the practical usefulness and obtain physically meaningful results, a variety of consistency warnings are included. Termination occurs if any of these are sufficiently serious, i.e. so-called ‘danger signals’. This may occur on inappropriate input data or some rare condition that has not been catered for. However, many warnings are only intended for information and their occurrence does not degrade the results.

# 10 Neighbour schemes

# 10.1 Introduction

Direct $N$ -body simulations on conventional computers benefit greatly from the use of the Ahmad–Cohen [1973] or AC neighbour scheme. Algorithms for both the divided difference method and Hermite formulation will therefore be discussed in the following sections. We also consider the implementation of the code $N B O D Y 6 ^ { + + }$ on a popular type of parallel computer [Spurzem, Baumgardt & Ibold, 2003], since it seems that the future of large- $N$ calculations is evolving in this direction at least for those who do not use the special-purpose HARP or GRAPE machines described previously. The important problem of massive black hole binaries in galactic nuclei is very challenging and appears amenable to direct integration using parallel architecture and neighbour schemes. A direct solution method is described [Milosavljevi´c & Merritt, 2001]. This treats the massive components by two-body regularization, whereas the formation process itself is studied by a tree code. Some of the drawbacks of this method inspired a new formulation where the massive binary is considered as part of a compact subsystem which is advanced by a time-transformed leapfrog method [Mikkola & Aarseth, 2002]. Over the years, the quest for larger particle numbers has also encouraged the construction of partially collisional methods. An early attempt to introduce multipole expansion for the outer cluster regions [Aarseth, 1967] was eventually combined with the code NBODY 5 and will be considered here since it still forms a viable alternative. Finally, we outline two other hybrid formulations [Quinlan $\&$ Hernquist, 1997; Hemsendorf, Sigurdsson & Spurzem, 2002] that combine the self-consistent field method [Hernquist & Ostriker, 1992] with direct integration as well as two-body regularization.

# 10.2 Basic Ahmad–Cohen method

Having described the theory and initialization procedures for the AC scheme in previous chapters, we now concentrate on some practical algorithms for efficient use. It will be assumed in the following that pointmass calculations are intended since a detailed description of the NBODY 2 code already exists [Aarseth, 2001b]; otherwise any reference to regularized binary components and centre-of-mass (c.m.) particles can simply be ignored.

In order to focus on the specific tasks, Algorithm 10.1 summarizes the main steps of the integration cycle for the divided difference scheme, together with some procedures for two-body regularization.

Algorithm 10.1. Integration cycle for the $A C$ scheme.   

<table><tr><td>1 Select the next particle,i,and define the time by t = ti +△ti 2 Make a new sorted time-step list,L,if t &gt; tL and adjust △tL 3 Advance any regularized solutions up to the current time 4 Decide regular force prediction [case (1)] or summation [case (2)] 5 Search for close encounter if △ti &lt; △tcl and △ti decreasing 6 Predict neighbour coordinates [case (1)] or all particles [case (2)] 7 Combine polynomials for particle i and predict r,r to order F(3) Obtain the irregular force Fold and update the times tk 8 9 Form new irregular differences and include the term D4 10 Initialize any new KS regularization and go back to step 1 11 to give Ft,F(1); R 12 Evaluate new forces, Frew, and form new neighbour list 13 Repeat step 12 if ni = O and ri &lt; 1Orh; reduce list if ni &gt; nmax 14 Adjust the neighbour sphere Rs and update the times Tk</td></tr></table>

A regular force calculation is decided on by comparing $t + \Delta t _ { i }$ with $T _ { 0 } + \Delta T _ { i }$ . If the former exceeds the latter, the regular step is shortened to end at the present time, $t$ . Note that we are comparing the next estimated irregular force time with the regular force time. Both the irregular and regular force summations extend over the individual components in case of regularized pairs, unless the c.m. approximation applies. The second regular derivative required at general output times is obtained from a differentiation of (2.1) at $t \neq T _ { 0 }$ which yields an extra term in ${ \bf D } _ { \mathrm { R } } ^ { 3 }$ ,

$$
{ \bf F } _ { \mathrm { R } } ^ { ( 2 ) } = { \bf D } _ { \mathrm { R } } ^ { 3 } [ ( t _ { 0 } - T _ { 0 } ) + ( t _ { 0 } - T _ { 1 } ) + ( t _ { 0 } - T _ { 2 } ) ] + { \bf D } _ { \mathrm { R } } ^ { 2 } .
$$

Likewise for step 11, the regular force and its first derivative are evaluated to highest order (i.e. ${ \bf D } _ { \mathrm { R } } ^ { 3 }$ ) at an intermediate time before the contributions are added to the respective irregular parts. Since a general time is involved, the regular derivative is obtained by the extrapolation

$$
\begin{array} { r } { { \bf F } _ { \mathrm { R } } ^ { ( 1 ) } = { \bf D } _ { \mathrm { R } } ^ { 3 } ( t _ { 0 } ^ { \prime } t _ { 1 } ^ { \prime } + t _ { 0 } ^ { \prime } t _ { 2 } ^ { \prime } + t _ { 1 } ^ { \prime } t _ { 2 } ^ { \prime } ) + { \bf D } _ { \mathrm { R } } ^ { 2 } ( t _ { 0 } ^ { \prime } + t _ { 1 } ^ { \prime } ) + { \bf D } _ { \mathrm { R } } ^ { 1 } , } \end{array}
$$

where $t _ { k } ^ { \prime } = t _ { 0 } - t _ { k }$ and $t _ { 0 } = t$ . Substituting $t _ { k } = { \cal T } _ { k } ^ { \mathrm { ~ ~ } }$ , $( k = 0 , 1 , 2$ ) for the regular times then yields the desired value which is added to the irregular force derivative given by

$$
{ \bf F } _ { \mathrm { I } } ^ { ( 1 ) } = ( { \bf D } _ { \mathrm { I } } ^ { 3 } t _ { 2 } ^ { \prime } + { \bf D } _ { \mathrm { I } } ^ { 2 } ) t _ { 1 } ^ { \prime } + { \bf D } _ { \mathrm { I } } ^ { 1 } .
$$

In the case of a successful close encounter search ( $i \leq N$ ), both particles are predicted to order $\mathbf { F } ^ { ( 3 ) }$ before applying the corrector for particle $i$ . The integration cycle is then terminated and the KS initialization procedure begins (cf. section 8.8). Since the time-steps are not synchronized, the neighbour coordinates are predicted before the c.m. force polynomials are formed.

The new total force evaluation (step 12) follows an irregular step which includes the fourth-order corrector. Some care is required in order to avoid spurious contributions to the regular force differences. Thus in the case of no change of neighbours, the old and new irregular force should be numerically identical to yield the actual first difference (3.5). This is achieved by using the predicted coordinates at step 12 instead of the corrected values, and likewise when evaluating derivative corrections.

Appropriate measures are taken in case there are no neighbours. Alternatively, if $n _ { i } \ge { n _ { \mathrm { m a x } } }$ , the neighbour sphere radius is reduced by a factor 0.9 and, for particles outside the new boundary, identical contributions are subtracted from the irregular force and added to the regular force. A procedure that adds approaching particles in an outer shell to the neighbour field is beneficial on conventional computers. We also need to make sure that enough neighbours are retained for uneven distributions which invariably occur. In some situations (i.e. for increased accuracy with binaries or shorter CPU time), it may be desirable for the average neighbour number to exceed a specified fraction of the maximum value. An optional procedure is therefore included which increases the predicted membership (3.3) by a suitable factor if $\bar { n } < \frac { 1 } { 2 } n _ { \operatorname* { m a x } }$ .

The case $i > N$ requires special attention because the neighbour list is used to select the perturbers and the membership may not be sufficient. If $\tilde { R } _ { \mathrm { s } } > R _ { \mathrm { s } }$ , with $\bar { R } _ { \mathrm { s } } = - 1 0 0 m _ { i } / h _ { i - N }$ , the neighbour radius is stabilized on $0 . 9 n _ { \mathrm { m a x } }$ by (3.4). Here $\tilde { R } _ { \mathrm { s } }$ denotes the maximum perturber distance for equal-mass particles, according to (8.58). Hence for long-lived binaries an attempt is made to increase the neighbour sphere if it is too small for the perturber range $\lambda a ( 1 + e )$ , with $\lambda \simeq 1 0 0$ . This problem only tends to occur for relatively small $N$ , since the inter-particle distance scales as $N ^ { - 1 / 3 }$ and $R _ { \mathrm { c l } } \propto N ^ { - 1 }$ . However, systems containing massive binary components require additional consideration because the two-body separation may be fairly large. One simple expedient is to redefine the termination distance by setting $R _ { 0 } = 2 a$ for hard energies ( $E _ { \mathrm { b } } < \epsilon _ { \mathrm { h a r d } }$ ), provided the neighbour radius is sufficiently large (i.e. $a ( 1 + e ) < 0 . 0 2 R _ { \mathrm { s } }$ ).

Because of frequent coordinate predictions, it is convenient to include the c.m. particles in the neighbour list instead of the components, whereupon the latter can be obtained by KS transformations if desired. Hence at every termination the relevant c.m. body needs to be replaced by the two components in their sequential location. Several such list expansions may occur within one regular time-step and some allowance for extra members must therefore be made when allocating the maximum size. Conversely, it may happen that only one component of a future KS solution is included in the neighbour list and regularization occurs before the next update. To circumvent this problem we initialize all the prediction variables to zero such that the current coordinates are used in the force evaluation. Only a small error is incurred here since the separation is comparable to $R _ { \mathrm { s } }$ . The corresponding c.m. particle will then be selected at the next regular step. In the case when primordial binaries are initialized, a recent procedure ensures that both the components are selected together as neighbours, which avoids the difficulty above.

When the force on a single particle is considered, the contribution from any neighbouring c.m. particle is evaluated in the point-mass approximation provided $r _ { i j } > \lambda R$ , where $R$ is the current two-body separation. In the alternative case, a coordinate transformation is performed and the summation is over both components. However, if the same particle is also a member of the corresponding perturber list by virtue of its larger mass (cf. (8.58)), its effect on the internal motion will be included. This apparent inconsistency can be justified if we note that the orbital energy change, $\dot { h } = \dot { \mathbf { R } } \cdot \mathbf { P }$ , cancels to first order when a weak perturbation (here $\gamma \simeq \gamma _ { \mathrm { m i n } }$ ) is integrated over one period. Hence use of the c.m. approximation according to a distance test avoids additional complications in the evaluation of $\mathbf { F } _ { \mathrm { I } }$ and ${ \bf { F } } _ { \mathrm { { R } } }$ , which must use the same expression.

A more serious problem with the divided difference formulation is due to large derivative corrections which are difficult to avoid without additional algorithms. Thus one can to a certain extent anticipate some problems by, for instance, selecting a particle undergoing a close non-regularized encounter with an existing neighbour; otherwise large high-order force derivatives may appear. Note that the selection of two such particles instead of one still gives rise to some high derivatives, but the dipole terms cancel. Likewise, a previous neighbour with small time-step is retained out to a distance $2 R _ { \mathrm { s } }$ in order to minimize the derivative corrections $\mathbf { F } ^ { ( 2 ) } \propto r ^ { - 4 } )$ . Alternatively, such a particle may belong to a soft binary of high eccentricity which becomes regularized at some stage.

Even if the optional treatment to minimize high derivatives is activated, the regular force polynomial may sometimes reveal non-convergent behaviour. Thus the rare case of the second difference being abnormally large compared with the first regular force difference is best handled by neglecting the corrector ${ \bf D } _ { \mathrm { R } } ^ { 4 }$ altogether; i.e. if $| { \bf D } _ { \mathrm { R } } ^ { 2 } | ( T _ { 0 } - T _ { 1 } ) > | { \bf D } _ { \mathrm { R } } ^ { 1 } |$ . This behaviour may be due to force derivative corrections for a particle near the boundary that is repeatedly included and excluded when the neighbour radius is modified according to (3.4).

Finally, we consider a special algorithm to alleviate possible problems connected with high velocities. Superfast particles are often ejected from a cluster following strong interactions inside compact subsystems of three or more members, or may be due to a neutron star velocity kick. Unless some precaution is exercised, such a particle may penetrate deeply into the neighbour sphere before the next regular force update, and hence produce an unacceptable change in the irregular force. An optional procedure has therefore been added to create a list of high-velocity particles for possible inclusion in the neighbour field already at a distance of $2 R _ { \mathrm { s } }$ , provided the impact parameter is less than $R _ { \mathrm { s } }$ . A high-velocity particle is defined by $v _ { j } ^ { 2 } > 8 v _ { \infty } ^ { 2 }$ together with $\Delta t _ { j } > \Delta t _ { \mathrm { c l } }$ , where $v _ { \infty }$ is the estimated central escape velocity of twice the current rms value. In practice, the limiting square velocity is derived from the expression $1 6 | h _ { \mathrm { h a r d } } |$ (cf. (4.1)). The condition $\Delta T _ { j } > 2 0 \Delta t _ { \mathrm { c l } }$ for the regular step ensures that only genuinely freely moving particles are selected. In addition, we may also employ the subsidiary condition $| \mathbf { F } _ { i } | ^ { 2 } \ < \ 4 N$ which excludes an ongoing close encounter. Members of the high-velocity list are checked and removed at frequent intervals if $r _ { j } > 3 r _ { \mathrm { h } }$ or if the velocity has decreased below the specified limit.

In conclusion, we see that regularization is beneficial in placing a lower limit on existing time-steps and also assists in suppressing high-frequency force fluctuations that have no significant secular effects. Hence the combination of the AC neighbour scheme with regularization has proved itself, although a considerable programming effort has been invested towards the achievement of this goal.

# 10.3 Hermite implementation

The Hermite version of the AC scheme (HACS) gives rise to the code NBODY 6 and has many features in common with the standard formulation discussed above. On the whole, the block-step structure allows for a simpler treatment and the main differences are sufficiently distinct to warrant a separate section. The special scheduling has been described in section 9.2 and we therefore move on, assuming that a list of particles due for updating is given.

Since there are usually a number of particles, $N _ { \mathrm { b l o c k } }$ , to be advanced at the same time, we employ a different prediction strategy. Thus for small block memberships (say $N _ { \mathrm { b l o c k } } \leq 1 0$ for $N \simeq 1 0 0 0$ ) and no regular force update, the neighbour lists are combined by an efficient sorting procedure for prediction; otherwise the coordinates and velocities of all particles are predicted for simplicity.∗ Unless already done, any c.m. particles are predicted next, followed by iteration of the regularized time for prediction of $\mathbf { U }$ , $\mathbf { U } ^ { \prime }$ and KS transformations to obtain the state vector of the components. Most of the procedures concerning the irregular and regular force polynomials are now essentially similar to the previous case, including the use of predicted coordinates and velocities for step 12 of Algorithm 10.1. However, high-order derivative corrections are simplified and the corrector is of different form (cf. (2.23)), containing less terms.

The irregular time-step is determined by the original criterion of chapter 2. Following an earlier suggestion [Makino & Aarseth, 1992], we modify the expression slightly to

$$
\Delta t _ { i } = \left[ \frac { \eta _ { I } ( | \mathbf { F } | | \mathbf { F } _ { \mathrm { I } } ^ { ( 2 ) } | + | \mathbf { F } _ { \mathrm { I } } ^ { ( 1 ) } | ^ { 2 } ) } { | \mathbf { F } _ { \mathrm { I } } ^ { ( 1 ) } | | \mathbf { F } _ { \mathrm { I } } ^ { ( 3 ) } | + | \mathbf { F } _ { \mathrm { I } } ^ { ( 2 ) } | ^ { 2 } } \right] ^ { 1 / 2 } .
$$

Thus the total force is used instead of the irregular force, in case the latter happens to be small. This leads to somewhat larger irregular steps since the error of the neighbour force is now a constant fraction of the total force. The same expression would also be beneficial in $N B O D Y 5$ .

The basic regular time-step takes the same form as (2.13), with the corresponding regular quantities substituted. However, there are situations where the value of $\Delta T _ { i }$ may be increased because the fractional change in the regular force is below the tolerance. We therefore evaluate the predicted change due to an increased trial value $\Delta \tilde { T } _ { i } = 2 \Delta T _ { i }$ from

$$
\begin{array} { r } { \Delta \mathbf { F } _ { \mathrm { R } } = [ ( \frac { 1 } { 6 } \mathbf { F } _ { \mathrm { R } } ^ { ( 3 ) } \Delta \tilde { T } _ { i } + \frac { 1 } { 2 } \mathbf { F } _ { \mathrm { R } } ^ { ( 2 ) } ) \Delta \tilde { T } _ { i } + \mathbf { F } _ { \mathrm { R } } ^ { ( 1 ) } ] \Delta \tilde { T } _ { i } . } \end{array}
$$

The trial value is chosen on a successful outcome of the convergence test

$$
| \Delta \mathbf { F } _ { \mathrm { R } } | < \eta _ { R } \operatorname* { m i n } \left\{ | \mathbf { F } _ { \mathrm { R } } | , | \mathbf { F } _ { \mathrm { I } } | \right\}
$$

for isolated systems, with a suitable modification of the first force term on the right-hand side for an external tidal field. The final values of $\Delta t _ { i }$ and $\Delta T _ { i }$ are chosen according to the block-step synchronization rules discussed in section 2.6. In order to satisfy decision-making requirements, the irregular time-step is not allowed to exceed the regular value.

In Hermite integration, the second and third force derivatives are obtained at the end of the time-step. Hence it is not necessary to perform the relatively expensive initialization of these quantities by explicit summation, provided a satisfactory time-step can be prescribed. For this purpose we have again adopted an expression of the type (8.56). This form is also used to initialize regular time-steps in NBODY 6.

Early use of the neighbour scheme was mainly confined to relatively homogeneous systems. However, systems that have experienced core collapse produce a wide range in density. Although the computational cost is dominated by the central region, the original limit on the predicted membership (cf. (3.3)) may be relaxed. Somewhat belatedly we now introduce a modified lower limit outside the half-mass radius,

$$
n _ { \mathrm { m i n } } = 0 . 2 n _ { \mathrm { m a x } } ( r _ { \mathrm { h } } / r ) .
$$

This condition leads to a gradually decreasing neighbour membership for particles moving into the far halo.

The case of zero neighbours requires special treatment. A similar algorithm exists for standard AC but here we need both the force and its derivative. Very distant particles, say $r _ { i } > 1 0 r _ { \mathrm { h } }$ , do not usually have any natural neighbours and are therefore allocated a nominal mass of $0 . 0 1 \bar { m }$ at the coordinate centre in order to facilitate the integration. The corresponding first derivative is evaluated explicitly and any optional external perturbations are added to give a well-defined irregular time-step which is usually fairly large. In order to reach the state of zero neighbour number, the radius $R _ { \mathrm { s } }$ is reduced gradually outside a specified central distance according to

$$
\tilde { R } _ { \mathrm { s } } = \operatorname* { m a x } \left\{ 0 . 7 5 R _ { \mathrm { s } } , 0 . 0 1 r _ { \mathrm { h } } \right\} ,
$$

which achieves the desired objective unless escaper removal occurs. Note that, in the standard scheme, this modification of the neighbour radius for distant particles may lead to some reduction of the time-steps because of the force derivative corrections.

The HACS scheme provides for a simplified treatment of high-order derivative corrections compared with the standard ACS. As has been discussed elsewhere [Makino & Aarseth, 1992], the high-order derivatives are not actually used for the integration of single particles. However, for some purposes (i.e. diagnostics) it may be useful to predict coordinates and velocities to highest order, and there is also the new feature of regularization to consider. On the other hand, all particles are synchronized at the longest time-step (typically 0.5), whereas output intervals are usually a few time units. Hence the derivative corrections are only performed if the relevant option is activated, except for the case $i > N$ and significant perturbation. The latter is useful in connection with regularization terminations which do occur at arbitrary times.

The higher force derivative corrections on a c.m. particle are not based on the mass-weighted contributions because the component values of $\mathbf { F }$ and $\dot { \mathbf { F } }$ required to construct $\mathbf { F } ^ { ( 2 ) }$ and $\mathbf { F } ^ { ( 3 ) }$ are not available. Consequently, use of the c.m. approximation is only consistent outside the perturber distance, $\lambda R$ , and, for this reason, it is desirable to ensure a sufficiently large neighbour radius or, failing that, place an upper limit on the size of the two-body separation, $R$ .

The Hermite integration cycle is essentially similar to Algorithm 10.1. One difference is that any new KS regularization is initialized at step 3, whereupon the cycle begins again since the sequential data structure may have changed. Moreover, following a successful close encounter search at step 8, the relevant particle indices are saved for the next cycle. The end of each irregular or regular corrector step is characterized by initializing the basic integration variables, $\mathbf { r } _ { 0 }$ , $\mathbf { v } _ { 0 }$ . In HACS, and also for parallel implementations, it is preferable to delay setting the final values of $\mathbf { r }$ , $\mathbf { v }$ until the end of the block-step, copied from $\mathbf { r } _ { 0 }$ , $\mathbf { v } _ { 0 }$ . In other words, the predicted values are used throughout the current cycle for consistency.

Since memory is no longer a concern, two different regular force derivatives are defined for convenience in HACS. Thus we distinguish between the regular force derivative based on the new neighbours and the derivative (3.9) with respect to the old neighbours. The former is only used to construct the prediction variables (3.6) and (3.7). Note that the latter, which preserves the sum of the derivative corrections at the end of a regular step, may not be updated to include the change of neighbours for single particles. Likewise, the irregular derivatives are treated analogously.

With the block-step scheme, the candidates for KS regularization need to be synchronized before initialization so that both components are advanced in the same block. The time-steps are usually equal but, if necessary, this is achieved by enforcing a step reduction for the particle being advanced. Unless other complications prevail, the new KS solution is initialized at the start of the next cycle by re-instating the previous value of the time. On the other hand, procedures for KS termination, new multiple regularizations or hierarchical mergers are activated at the end of the integration cycle. We note that the total number of such initialization procedures is very small compared with the number of block-steps (by a factor of about $1 0 ^ { 4 }$ ) so that coincidence conflicts are extremely rare and not harmful; i.e. this causes a possible delay by one small block-step.

Star cluster simulations often exhibit examples of superfast particles, especially if hard binaries are present. As in the code NBODY 5, this may result in an approaching particle moving well inside the neighbour sphere before it is identified at the next regular force calculation. The check for possible penetrations is done differently as follows. Since the ejection of a fast particle is usually associated with strong interactions involving KS or chain regularization, it is natural to initiate a special search at terminations that are defined by the control index in Table 7.2. Again the conditions for acceptance described previously are employed. Given a list of high-velocity particles, any contribution to the irregular force is considered together with other optional procedures when evaluating the total force.

A subsequent search for neighbour sphere intersections is made at moderately large commensurate intervals; i.e. $\Delta t _ { \mathrm { n b } } ~ = ~ 1 / 3 2$ (scaled by $( 1 0 0 0 / N ) ^ { 1 / 3 }$ for $N > 1 0 0 0$ ). This provides an opportunity for the regular time-step to be reduced. Hence we treat the case of close and distant neighbours separately. The search itself only considers particles $j$ with regular time-steps $\Delta T _ { j } \ \ge \ \Delta t _ { \mathrm { n b } }$ , because these are the most vulnerable. Provided the radial velocity is negative, we form the time until minimum approach by

$$
\Delta \tilde { t } _ { \mathrm { m i n } } = \operatorname* { m i n } \left\{ T _ { 0 } + \Delta T _ { j } - t , - \mathbf { D } \cdot \mathbf { V } / \mathbf { V } ^ { 2 } \right\} ,
$$

where $\mathbf { D }$ and $\mathbf { V }$ denote the relative distance and velocity. The minimum impact parameter can be estimated if we assume straight-line motion,

$$
D _ { \mathrm { m i n } } = \left| { \bf D } + { \bf V } \Delta \tilde { t } _ { \mathrm { m i n } } \right| .
$$

If the corresponding intruder force is significant, i.e.

$$
m _ { i } / D _ { \operatorname* { m i n } } ^ { 2 } > 0 . 1 | \mathbf { F } _ { j } | ,
$$

the regular time-step is reduced by a factor 2, subject to the synchronization condition $T _ { 0 } + \frac { 1 } { 2 } \Delta T _ { j } > t$ , and further reductions are performed if relevant. The above algorithm is also implemented in NBODY 4 for the time-step $\Delta t _ { i }$ .

A check for removal of high-velocity particles is carried out at intervals of $\Delta t _ { \mathrm { n b } }$ . Such particles are removed from the special list outside a central distance of $3 r _ { \mathrm { h } }$ and also if their velocity falls below the critical value, given by $v ^ { 2 } = 1 6 | h _ { \mathrm { h a r d } } |$ (cf. (4.1)). Moreover, the list is updated to take account of any changes in the particle sequence.

Comparison of the two versions of the AC scheme depends on the hardware even if we consider only workstations or laptops. In fact, on a RISCbased workstation, the total CPU time for the same number of steps of both types favoured HACS slightly for a test problem with $N = 1 0 0 0$ . Thus the extra effort to obtain $\dot { \mathbf { F } }$ with HACS is compensated by less predictions and a simpler corrector. The original investigation [cf. Makino $\&$ Aarseth, 1992] showed that nearly twice as many steps were needed by the latter method for the same accuracy when softening is used. However, recent laptop comparisons of $N B O D Y 5$ and NBODY 6 with $N \leq 1 0 0 0$ yield more comparable energy errors for standard parameters, the latter still being faster per step. The Hermite block-step version is also considerably easier to implement and exhibits greater numerical stability [cf. Makino, 1991a]. Finally, we emphasize that, although of fourth order, the general Hermite scheme has the attractive feature of being self-starting.

# 10.4 Parallel adaptations

As a first case study, we discuss the adaptation of the parallel code NBODY 6 to the CRAY T3E [Spurzem, Baumgardt & Ibold, 2003]. This development also aims to provide a portable code for LINUX cluster configurations by a comprehensive code-building algorithm which ideally should reduce to NBODY 6 for single CPUs. The implementation has necessitated several important changes, both as regards general strategy and exploitation of the different architecture. This code has therefore been given the new name NBODY 6++ to distinguish it from the original version. The main structural changes facilitate parallelization of three independent procedures as follows:

• Advance all KS solutions up to the end of the current block-step Evaluate new irregular forces and apply the corrector • Obtain regular forces, neighbour lists and perform corrections

The second and third stages have already been fully parallelized. Moreover, the prediction of neighbours has also been included in the second part. In order to ensure that the results do not depend on the order in which the particles in a given block are treated, the final corrector initialization $\mathbf { r } = \mathbf { r } _ { 0 } , \mathbf { v } = \mathbf { v } _ { 0 }$ for all the members is delayed until the end of the block-step, as is also done in $N B O D Y 6$ .

The parallelization of KS solutions presents a challenge for efficient use of multi-processor machines like the T3E. The non-linearity of the time transformation $d t = R d \tau$ does not by itself prevent such procedures because one can always define a set of approximate hierarchical levels. Consider a number of perturbed binaries that are due to be updated during the next block-step. Depending on their location in the cluster, some may have joint perturbers of single particles or even other binaries. It follows that a random assignment to different processors may cause problems of inconsistency in the latter case since predictions are involved. One possible way is to take account of the spatial distribution and construct a binary tree structure in order to facilitate the decision-making. An alternative solution method for the immediate future is to subdivide the block-step by factors of 2 into sufficiently small subintervals to prevent predictions outside the range of validity. All such members in one sub-block can then be distributed to different processors which would achieve a significant speed-up. By analogy with the parallel procedures for the irregular and regular integration steps, it can be anticipated that the number of simultaneous KS solutions will be large enough to justify this approach. Provisional experimentation along the latter lines has been carried out and appears to be promising [Spurzem, private communication, 2001].

In considering this problem, one should envisage studying a large population of primordial binaries (say $N _ { \mathrm { b } } \simeq 5 \times 1 0 ^ { 4 }$ ). Such a distribution would contain a significant number of unperturbed binaries, where integration of the corresponding c.m. motions proceeds as for single particles. This leaves the checking for perturbers that occurs on time-scales from one binary orbit up to the c.m. time-step, depending on the local density and velocity distribution. Fortunately, this procedure does not create any conflicts and all the necessary checks can be carried out in parallel, provided the operation is performed as an additional step. Alternatively, by making no distinction, the latter task may be carried out together with the advancement of KS solutions, since the numerical effort to check unperturbed motion is less.

Again the hierarchical time-step algorithm is employed for both the irregular and regular time-steps, which must be individually commensurate. Since the distribution of block-steps is quite wide, with less members at small values in realistic systems, there is some loss of efficiency and serial integration may in fact be preferable. As $N$ increases, so does the number of particles, $N _ { \mathrm { g r } }$ , due to be advanced at the same time. The theoretical prediction $N _ { \mathrm { g r } } \propto N ^ { 2 / 3 }$ [Makino $\&$ Hut, 1988] appears to be in reasonable agreement with present simulations of inhomogeneous systems. Hence for large $N$ , the average number of group members starts to exceed the number of available processors, $n _ { \mathrm { p r o c } }$ . The typical amount of communication after each block-step is $k N _ { \mathrm { g r } } / n _ { \mathrm { p r o c } }$ double-precision words, where $k = 1 9$ and $4 1 + n _ { \mathrm { m a x } }$ , respectively, for the irregular and regular force calculation. Consequently, it is beneficial to limit the maximum neighbour number as much as possible. Notwithstanding the theoretical prediction $n _ { \mathrm { p } } \simeq ( N / 1 . 8 ) ^ { 3 / 4 }$ [Makino & Hut, 1988], a constant value, $6 4 \le n _ { \mathrm { m a x } } \le 1 2 8$ , has been found satisfactory for a wide range of particle numbers. We may distinguish between the theoretical speed-up and actual performance. Thus when communication times are neglected, the efficiency does improve up to the maximum processor number. However, at present the computing time only scales linearly with $N$ up to about 512 processors (for $N = 1 0 ^ { 4 }$ ) owing to memory and communication limits.

The parallel algorithm considered above does not assign specific particles to any processor and every node contains an identical copy of the whole dataset. So-called ‘domain decomposition’ is employed in the recent cosmological tree code $G A D G E I ^ { \prime }$ [Springel, Yoshida & White, 2001] (and other such codes) which takes advantage of the slow mixing when using comoving coordinates. Accordingly, at the end of each block-step the new data must be broadcast to all the other processors. The net result is that maximum efficiency is achieved at some intermediate number of processors that depends on $N$ [cf. Spurzem et al., 2003]. Thus we have an example where further software development is desirable in order to exploit an existing hardware configuration that is potentially very powerful. Judging from the history of conventional computers and given the incentive, there is bound to be progress in this young subject.†

A separate version of $N B O D Y 6 ^ { + + }$ has been prepared for the HARP-3 special-purpose computer [Spurzem et al., 2003]. Such an attempt faces the problem that only the force calculations can be executed in parallel. Moreover, since the irregular force is now evaluated on the host, the regular force is obtained by subtraction after setting the neighbour masses to zero in a second full $N$ summation on HARP. In order to utilize many pipelines, the neighbour lists of all the particles due for regular force updates are first combined, with a subsequent modification of the affected individual components on the host. Hence the additional effort is less for relatively small neighbour numbers which in any case must be below the hardware limit. However, this somewhat laborious procedure suffers from numerical problems because of the different accuracy employed by HARP, which results in reduction of the regular time-steps produced by spurious force derivatives. In view of this exploratory investigation, we may anticipate that future hardware developments will take advantage of the potential gain from using a neighbour scheme.

# 10.5 Black hole binaries in galactic nuclei

The problem of formation and dynamical evolution of a black hole (BH) binary with massive components is of considerable topical interest. Several past efforts employed direct integration methods to elucidate the behaviour of such systems but applications to galactic nuclei pose severe limitations with regard to the particle number that can be studied. The formation is usually envisaged as the end product of two separate unequal galactic nuclei spiralling together by dynamical friction, but there are other scenarios. In view of the different numerical requirements for the early and late stages, it is natural to consider this problem in two parts and take advantage of direct integration where it matters most.

A recent investigation [Milosavljevi´c & Merritt, 2001] employed the parallel version of the GADGET code [Springel et al., 2001] to study the formation process. This code maintains individual and adaptive timesteps and maps the particles on to an octal tree structure. For initial conditions, two spherical stellar systems containing a central BH masspoint were placed in a moderately eccentric orbit with semi-major axis $a _ { \mathrm { G } } \simeq 4 r _ { \mathrm { h } }$ . The relatively small softening length used, $\epsilon = 0 . 0 0 1$ , was well below the BH hard binary separation, $a _ { \mathrm { h a r d } } = ( m _ { 1 } + m _ { 2 } ) / 8 \sigma ^ { 2 } \simeq 0 . 0 0 2 5$ . A mass ratio $m _ { 1 } / M = 0 . 0 1$ and total particle number $N = 2 5 6 \mathrm { K }$ was adopted. This model is close to current computational limits, although still well short of realistic requirements. Another important aspect here is the presence of a steep stellar density cusp, $\rho \propto r ^ { - 2 }$ , surrounding each BH, whereas previous studies tended to use shallower King models.

Following the early phase of dynamical friction acting between the two BHs together with their bound subsystems, the collisionless simulation was continued until $a \simeq \epsilon$ . However, new datasets were generated by random sampling of the whole population already at an earlier stage when $a \simeq 3 0 a _ { \mathrm { h a r d } }$ , with effective memberships up to $3 2 \mathrm { K }$ and enhanced masses. These reduced datasets were then integrated by $N B O D Y 6 ^ { + + }$ in order to ascertain the $N$ -dependence of the subsequent evolution. A nearly constant hardening rate, $d a ^ { - 1 } / d t$ , was observed, with a modest eccentricity increase during shrinkage by a factor of 20. Contrary to previous findings, the hardening rate appeared to be independent of $N$ ; this result was ascribed to a larger reservoir of central stars. It is also significant that a simulation with initial supermassive black holes inside steep density cusps produced nuclei with shallow cusps and $\rho \propto r ^ { - 1 }$ .

The presence of a supermassive binary poses several new technical challenges for the numerical treatment. Since the regularization scheme employed by NBODY 6 was developed for conventional star clusters containing a realistic IMF, it is essential to modify the strategy in order to prevent inefficient usage. One characteristic feature that requires fresh consideration is the occurrence of persistent orbits of short periods around one of the BHs. For sufficiently small length scales, the effect of gravitational radiation should be included and this may eventually induce coalescence. In any case, a few strongly bound orbits are of little dynamical significance here and such stellar companions can therefore be combined with their BH. Since the dominant binary is surrounded by a large number of stars in bound orbits, the standard criteria for chain regularization and even the KS regularization scheme require modification. In general, the code scales well with the number of processors for a moderate spread in time-steps. However, the scaling was poor when a few particles had small time-steps and so a switch was made to serial integration.

If the decay of the binary continues sufficiently far, energy loss by gravitational radiation will eventually play an important role. The time-scale for this stage to be reached depends on the Brownian motions generated by recoil effects due to slingshot interactions [Saslaw, Valtonen & Aarseth, 1974]. Since the amplitude of the binary wandering is much larger in an $N$ -body simulation than in a real galaxy, the question of the loss-cone replenishment cannot be settled by direct integration alone. However, the ejection of stars by the BH binary tends to lower the central density, permitting the binary an increased amplitude for further interactions. On the other hand, for some density profiles, BH binaries may essentially complete their evolution before gravitational radiation takes over.

The simulation of BH binary evolution is an exciting problem that demonstrates well the power of direct integration and holds great promise. Given the undoubted advantage of treating the BH binary as a perturbed system, it might be worthwhile trying the wheel-spoke regularization discussed in section 5.4. The two BH components would then be permanent members, with a small number of the most critical orbits considered for inclusion in the chain. Although this method has yet to be tried in a serious application, the development is based on the same principles as chain regularization. If it works, such a formulation would in fact lead to much simplification elsewhere because most of the other regularization procedures would become redundant. However, complications are also likely to arise due to the need for a generalized branching chain structure to be developed [cf. Mikkola & Aarseth, 1990]. Hence this idea remains a project for the future. Another promising avenue of dealing with this problem was opened up recently [Mikkola & Aarseth, 2002]. Because of similarities with chain regularization, algorithms for the associated new code NBODY 7 will be discussed in a subsequent chapter.

# 10.6 Hybrid formulations

Many stellar systems are characterized by a core–halo structure where the stars in low-density regions move in essentially collisionless orbits. Algorithms that include the star-by-star treatment in the inner regions and represent the outer parts in an approximate but consistent way can therefore still be considered to be collisional. Although the integration steps increase significantly with central distance in such systems, the force calculation for the inner particles can be speeded up on conventional machines by a fast evaluation of the distant interactions. This point was not considered in an analysis of computational cost [Makino & Hut, 1988].

The use of multipole expansion, discussed in section 3.4, can be formulated as a hybrid method while the collisional aspects are retained. In the following we describe a scheme for combining the direct force summation over particles in the inner regions with external contributions from an expansion in spherical shells [Aarseth, 1967]. The so-called ‘shell method’ was implemented during the early 1980s in a separate code, $N B O D Y S$ , based on NBODY 5 but was never used to obtain any published results. Some of the most relevant steps are displayed in Algorithm 10.2, which is an abbreviated form of Algorithm 10.1.

Algorithm 10.2. Integration cycle for the shell method.   

<table><tr><td>1</td><td>Divide the cluster into radial zones of equal membership</td></tr><tr><td>2</td><td>Evaluate all the moments at regular intervals,△tsh</td></tr><tr><td>3</td><td>Combine sum of external and internal moments for each shell</td></tr><tr><td>4</td><td>Select the next particle,i, to be treated (KS,single or c.m.)</td></tr><tr><td>5</td><td>Predict the coordinates of neighbours or all particles</td></tr><tr><td>6</td><td>Advance the solution for the irregular time-step,△ti</td></tr><tr><td>7</td><td>Repeat steps 4, 5 and 6 until t + △ti &gt; Ti +△Ti</td></tr><tr><td>8</td><td>Perform regular force summation and determine neighbour list</td></tr><tr><td>9</td><td>Add external and internal contributions from the shell force</td></tr><tr><td>10</td><td>Form new regular force differences and include the corrector</td></tr><tr><td>11</td><td>Update irregular and regular differences and set new time-steps</td></tr><tr><td>12</td><td>Return to step 2 (t ≥ tsh) or step 4 (t &lt;tsh)</td></tr></table>

The main idea is to divide the system into a relatively small number of zones (e.g. 7) of comparable size to twice the largest neighbour radii. Hence we extend the AC force expression to a sum of three terms by

$$
\mathbf { F } = \mathbf { F } _ { \mathrm { I } } + \mathbf { F } _ { \mathrm { R } } + \mathbf { F } _ { \mathrm { S } } ,
$$

where contributions from all non-overlapping shells are included in the smooth component, $\mathbf { F } _ { \mathrm { S } }$ . The moments are updated at times $t _ { \mathrm { s h } }$ with intervals $\Delta t _ { \mathrm { s h } } = 0 . 0 0 4 t _ { \mathrm { c r } }$ at a cost of $O ( N )$ . For each shell we then form separate sums of any internal and external terms of different order (cf. (3.24)), as well as a sequential list of the relevant particles. Accordingly, the main difference with the standard treatment of NBODY 5 is in the total force evaluation. Given a particle at radial position $\tilde { r } _ { i } = | \mathbf { r } _ { i } - \mathbf { r } _ { \mathrm { d } } |$ with respect to the density centre, $\mathbf { r } _ { \mathrm { d } }$ , and neighbour radius $R _ { \mathrm { s } }$ , the particles involved in the direct summation are those that fall inside shells in the distance range $[ \tilde { r } _ { i } - 2 R _ { \mathrm { s } } , \tilde { r } _ { i } + 2 R _ { \mathrm { s } } ]$ . After the determination of the corresponding shell indices, the new regular and irregular force are obtained by a sum over the respective list members. Contributions from the smooth component are then combined with the standard regular force.

The present treatment avoids the problem of boundary crossings if neighbour selection (including high-velocity stars) falls inside a distance of $2 R _ { \mathrm { s } }$ . Moreover, there is no need for interpolation within the associated shell as in the original formulation of section 3.4. We also note that for particles inside the innermost shell, which tend to have the smallest time-steps, only the external contributions are required. Hence the shell moment method appears to be an attractive alternative for allowing increased particle numbers.

Before returning to the problem of black hole binaries, we mention a simpler approach where the AC method for softened potentials was combined with the SCF code to model the dynamical evolution of elliptical galaxies containing a central singularity [Merritt & Quinlan, 1998]. Following the initial approach to equilibrium, a single massive body was introduced. The evolution of the central region was towards nearly spherical shape while the outer parts became axisymmetric, with the rate of change depending on the final BH mass ratio.

The behaviour of black hole binaries has been investigated by a hybrid method with some ingredients of a neighbour scheme. An attempt to cover more realistic mass ratios [Quinlan & Hernquist, 1997] combined the self-consistent field (SCF) method [Hernquist & Ostriker, 1992] with direct integration. Since the basic version of the SCF code employs one expansion centre, the existence of a relatively wide BH binary inside the same system was assumed at the outset. However, the lack of a consistent starting model has certain implications for the results [cf. Milosavljevi´c & Merritt, 2001]. Nevertheless, we summarize this work below as an interesting example of a hybrid method spanning three different techniques.

The dominant two-body motion was included in the point-mass form, whereas attractions from the other stars were added by direct summation using a softened potential. Moreover, the stellar contributions to each BH were split into two parts according to the AC scheme of $N B O D Y 2$ . Likewise, a softened potential was employed for the star–BH interactions, with the star–star attractions evaluated according to the SCF method. After some time, the BH binary components became close enough for their relative motion to be regularized. A KS treatment was used, based on the standard Hermite formulation of section 4.6 as implemented in the original version of NBODY 6. Special efforts were also made to circumvent problems connected with the large mass ratio. Thus stars within a distance of $5 0 a$ of the binary were included in the perturber list regardless of the size of their perturbation. The parameter $\gamma _ { \mathrm { m i n } }$ controlling unperturbed two-body motion was also reduced to $1 0 ^ { - 7 }$ .

Galaxy models with density cusps and some $1 0 ^ { 5 }$ particles with the masses decreasing towards the centre for improved resolution were selected for study. The softening was chosen as $\epsilon = m _ { 1 } / v _ { \epsilon } ^ { 2 }$ , where the softening velocity, $v _ { \epsilon }$ , was 2–3 times the BH orbital velocity for $a _ { \mathrm { B H } } = a _ { \mathrm { h a r d } }$ . The two BHs with masses $m _ { 1 } = m _ { 2 } = 0 . 0 1 M$ were initialized on nearly circular orbits at a distance $0 . 5 r _ { \mathrm { h } }$ and spiralled inwards to the centre in about six crossing times. From then on, regularization was employed and subsequent shrinkage by a factor of 12 beyond the hard binary limit (defined above) was observed. After a while, some stars were captured into bound orbits with small time-steps around the BHs and were absorbed by their massive component, subject to the condition $a < 2 \epsilon$ . In the event, the corresponding growth of the BH masses was at most $0 . 2 \%$ .

The basic integrator starts by generating the first three force derivatives which are not available for the coefficients of the potential expansion. In such situations it is adequate to begin with smaller time-steps and set the higher derivatives to zero, whereupon the next few time-steps can be increased gradually while the proper differences are formed. In this connection, we remark that although the Hermite method requires only the first derivative, it needs to be evaluated precisely for the corrector. It is also reassuring to note that the evolution of the hard binary was independent of the integrator used for the two-body motion, i.e. NBODY 1, NBODY 2 or NBODY 6. However, the accuracy parameters for direct integration need to be chosen conservatively in order for the well-known systematic errors to be acceptable. Although this study did not provide any definite model for the later stages of BH binary evolution and the initial conditions were somewhat unrealistic, it highlighted many essential aspects of a difficult problem and pointed the way forward.

An even more recent development combined the SCF method with the point-mass code $N B O D Y 6 ^ { + + }$ [Hemsendorf et al., 2002]. In order to use Hermite integration, the SCF code was upgraded to include evaluation of the force derivative. The initial application did not emphasize the importance of density cusps and used a Plummer model instead, with two massive components $m _ { \mathrm { B H } } = 0 . 0 1 M$ placed on the $x$ -axis at $\pm 0 . 6 4 r _ { \mathrm { h } }$ with small $y$ -velocity of opposite sign. In scaled units, the BH binary formed at $t \simeq 1 0$ and hardened linearly with time to $a _ { \mathrm { B H } } \simeq 2 \times 1 0 ^ { - 3 }$ . The full hybrid code used $6 4 \mathrm { K }$ and $1 2 8 \mathrm { K }$ particles, whereas comparison tests with the basic $N B O D Y 6 ^ { + + }$ were restricted to $N = 1 6 \mathrm { K }$ . This new implementation demonstrated that large- $N$ systems can be studied by direct means. However, some numerical difficulties were also reported, suggesting that this is a challenging problem that requires further attention.

# 11 Two-body algorithms

# 11.1 Introduction

A large number of algorithms are connected with regularization. Many of these concern the KS treatment which plays a key role in the $N$ -body simulation codes. In this chapter, we derive some expressions relating to the conversion of regularized time, followed by other considerations of a practical nature. A separate section provides essential details of the Stumpff KS method as employed in an $N$ -body code. This is followed by an algorithmic discussion of KS termination. Next we describe decision-making procedures for unperturbed two-body motion which speed up the calculation by a large factor. Another important feature with the same objective is the so-called ‘slow-down device’, where the principle of adiabatic invariance is exploited. The theory was given previously in connection with chain regularization and here we discuss the KS implementation. Special treatments of stable hierarchies also contribute significantly to enhanced efficiency while retaining the essential dynamics. Finally, the last sections deal with several processes relating to tidal interactions in close binaries that are connected through an evolutionary sequence. We discuss tidal circularization and two-body capture, as well as Roche-lobe mass transfer which all contribute to making star cluster modelling such an exciting and challenging project.

# 11.2 General KS considerations

We first discuss various general features that are applicable to all the KS methods and also include some aspects of the divided difference scheme, while the next section deals specifically with the Stumpff version.

In order to advance the whole $N$ -body system consistently, we need to integrate the equation of motion for the time (4.39). The conversion from

regularized time to physical time is most conveniently carried out by a Taylor series expansion to order $n$ ,

$$
\Delta t = \sum _ { k = 1 } ^ { n } \frac { 1 } { k ! } t _ { 0 } ^ { ( k ) } \Delta \tau ^ { k } .
$$

Provided $n \leq 6$ , all the necessary derivatives are already known in the high-order integration schemes, and hence the Hermite method applies directly. For the divided differences, $n = 5$ was chosen as sufficient. However, one more order, i.e. $\mathbf { U } ^ { ( 5 ) }$ , is available for (11.1) and has been implemented in the Hermite codes for increased accuracy when combined with the Stumpff functions. The high-order coefficients are formed by successive differentiation of (4.39), with the first two terms given by

$$
\begin{array} { r l } & { t _ { 0 } ^ { ( 2 ) } = 2 \mathbf { U } ^ { \prime } \cdot \mathbf { U } , } \\ & { t _ { 0 } ^ { ( 3 ) } = 2 \mathbf { U } ^ { \prime \prime } \cdot \mathbf { U } + 2 \mathbf { U } ^ { \prime } \cdot \mathbf { U } ^ { \prime } . } \end{array}
$$

Substitution of $\mathbf { U } ^ { \prime \prime }$ from (4.37) and $\mathbf { U } ^ { \prime } \cdot \mathbf { U } ^ { \prime }$ from (4.24) yields

$$
t _ { 0 } ^ { ( 3 ) } = 2 h R + m _ { \mathrm { b } } + R \mathbf { U } \cdot \mathcal { L } ^ { \mathrm { T } } \mathbf { F } .
$$

By definition $R ^ { \prime \prime } = t _ { 0 } ^ { ( 3 ) }$ t (3)0 ; hence this equation may also be used to obtain the integrated value of $R$ as a numerical check of the basic relation (4.29). Although of harmonic oscillator type, it is not clear whether its use would present any practical advantage. Thus $R$ is connected with $\mathbf { U }$ by a summation constraint and the regularized coordinates are already evaluated from linear equations of motion.

An inverse relation is required for interpolation within the interval $\Delta \tau$ in order to determine physical coordinates at a general time. This occurs when the force on other particles due to the KS pair is evaluated and the centre-of-mass (c.m.) approximation does not apply. Let $\delta t = t - t _ { 0 }$ denote the subinterval since the last KS treatment. We can either obtain a solution of (11.1) by iteration or from the inverse expansion

$$
\delta \tau = \sum _ { k = 1 } ^ { n } \frac { 1 } { k ! } \tau _ { 0 } ^ { ( k ) } \delta t ^ { k } ,
$$

in which $n = 3$ usually suffices. From the definition (4.39), $\dot { \tau } _ { 0 } = 1 / R$ and the next two terms are obtained by differentiation which gives

$$
\begin{array} { r c l } { { } } & { { } } & { { \tau _ { 0 } ^ { ( 2 ) } = - t _ { 0 } ^ { ( 2 ) } / R ^ { 3 } , } } \\ { { } } & { { } } & { { \tau _ { 0 } ^ { ( 3 ) } = ( 3 t _ { 0 } ^ { \prime \prime 2 } / R - t _ { 0 } ^ { ( 3 ) } ) / R ^ { 4 } . } } \end{array}
$$

The division by small values of $R$ is not harmful because it does not affect the integration of the relative motion. Moreover, the c.m. approximation is used if the distance ratio, $r _ { i j } / R$ , exceeds some prescribed value (i.e. the parameter $\lambda$ ). Thus the inversion (11.4) is usually called for when the solution of (4.42) is obtained after predicting a nearby c.m. particle in connection with force evaluations. Note that all the quantities on the right-hand side of (11.5) are known for each KS solution.

The prediction of the corresponding values of $\mathbf { U }$ (and $\mathbf { U } ^ { \prime }$ for Hermite) is carried out to highest order if required. Alternatively, if the distance ratio exceeds an appropriate value (e.g. 25), it is sufficient to expand the regularized interval to second order only. In this case, less accuracy is required and the coordinate prediction is performed to order $\mathbf { F } _ { \mathrm { U } }$ (and $\mathbf { U } ^ { \prime }$ to order $\mathbf { F } _ { \mathrm { U } } ^ { \prime }$ ).

Although the program structure for the two KS alternatives discussed here is formally similar, different prediction strategies were employed originally. Thus in the difference scheme it is natural to predict $\mathbf { U }$ and $\mathbf { U } ^ { \prime }$ to highest order before evaluating the perturbation and then apply the corrector to all the derivatives according to (2.3). Since the Hermite corrector takes a simpler form, with two terms added to the low-order prediction, it is convenient to treat these contributions separately and this is also in keeping with the spirit of the standard formulation. However, a more careful analysis [Funato et al., 1996; Mikkola & Aarseth, 1998] showed that it is advantageous to predict the regularized variables more accurately. The new procedure differs sufficiently from the basic approach to merit an outlined here.

We first perform a Taylor series prediction of the regularized coordinates and velocity to second or third order in the derivatives of $\mathbf { F } _ { U }$ , with the energy stabilization (4.43) included if the perturbation is suitably small (say $\gamma \simeq 0 . 0 1 \mathrm { - } 0 . 0 0 1 )$ . Using the transformed physical coordinates and velocity, the perturbation $( \mathbf { P } , \dot { \mathbf { P } } )$ is obtained in the usual way. After obtaining the relevant expressions for the corrector, we form the higher Taylor series derivatives where all the terms are evaluated at the beginning of the step. Note that the stabilization factor may be saved at the prediction stage since it must be combined with $\mathbf { F } _ { \mathrm { U } }$ again for the corrector.∗ This enables the complete solution for $\mathbf { U }$ and $\mathbf { U } ^ { \prime }$ to be written in nested form, instead of combining the predicted values with the corrector. According to the usual rationale of the Hermite formulation, the standard correction procedure may still be used for the energy integration, provided $h$ is predicted to order $h ^ { \prime \prime }$ only, otherwise the above scheme may readily be adopted. Recent experimentation shows that there is little gain in an extension to order F(3)U in the prediction (with energy stabilization), whereas the addition of one more order to the integration is beneficial in return for about 20 extra operations. When combined with the slow-down algorithm, the Hermite KS method is quite effective and deserves attention because of its simplicity.

Let us next consider some aspects connected with the external tidal field. In the standard case (cf. (8.14)), the Coriolis terms are omitted from the perturbation because the contributions to $h ^ { \prime }$ cancel identically, as can be seen by taking the scalar product $\dot { \mathbf { R } } { \cdot } \ddot { \mathbf { R } }$ which implies $\dot { \bf R } \cdot ( \Omega _ { \bf z } \times \dot { \bf R } ) = 0$ . However, the angular momentum would be affected to a small extent. The rate of change of the specific angular momentum is given by $\mathbf { R } \times { \ddot { \mathbf { R } } }$ . The contribution from the Coriolis force is then $- 2 \Omega _ { z } ( X \dot { X } + Y \dot { Y } )$ , with $X , Y$ the relative coordinates in the plane. For constant semi-major axis this averages to zero over an orbit. Hence we neglect the effect of the rotating coordinate system on the longitude of the periapse since the orientation is of a random nature when it comes to encounters with other particles.

According to the equations of motion (8.14), the linear tidal field gives rise to the contributions

$$
\dot { h } _ { \mathrm { t i d e } } = { \textstyle \frac { 1 } { 2 } } T _ { 1 } \frac { d } { d t } ( x _ { k } - x _ { l } ) ^ { 2 } + { \textstyle \frac { 1 } { 2 } } T _ { 3 } \frac { d } { d t } ( z _ { k } - z _ { l } ) ^ { 2 } ,
$$

where $\mathbf { R } = \mathbf { r } _ { k } - \mathbf { r } _ { l }$ . Assuming harmonic motion by $\mathbf { R } = \mathbf { A } \cos \omega t$ , we obtain $- A _ { j } ^ { 2 } \cos \omega t \sin \omega t$ from each term. Here $\omega = 2 \pi / t _ { \mathrm { K } }$ , with $t _ { \mathrm { K } }$ the period. Ignoring the different signs, we integrate the change over an orbit for each component $j$ which yields

$$
\Delta { h } _ { \mathrm { t i d e } } = A _ { j } ^ { 2 } T _ { j } \omega \int _ { 0 } ^ { t _ { \mathrm { K } } } \sin \omega t \cos \omega t d t = 0 .
$$

From the definition of the tidal radius (8.24), the relative galactic tidal perturbation in the $x$ -direction for equal masses is

$$
\begin{array} { r } { \gamma _ { \mathrm { t i d e } } \simeq \frac { 1 } { 2 } N ( R / r _ { \mathrm { t } } ) ^ { 3 } . } \end{array}
$$

This is negligible for most KS binaries in large clusters but is included at present for general validity in case large separations should occur. Thus in the approximation (8.58), the magnitude is equivalent to a perturber distance of about $( 2 / N ) ^ { 1 / 3 } r _ { \mathrm { t } }$ which is usually sufficiently large for unperturbed motion. Note that the assumption of constant period leading to $\Delta h _ { \mathrm { t i d e } } = 0$ does not apply in general; however, the effect of the perturbers will in any case dominate when the period is changing.

In the divided difference scheme we employ the standard expressions developed for direct integration, except that now we are dealing with the nine equations (4.37) and (4.38). Note that since the latter gives $h ^ { \prime }$ explicitly, we form the higher divided differences of this quantity. Again the respective polynomials are extended to fourth order and the corrector is included in the usual way. For this purpose a nominal reference time, $\tau _ { 0 }$ , is defined and updated by the step $\Delta \tau$ every time. However, the decision-making for advancing KS solutions is based on the corresponding expression $t _ { i } + \Delta t _ { i }$ , which is part of the scheduling, unlike in the standard Hermite case where all the physical time-steps are quantized and regularized solutions must be selected by a separate procedure.

Perturbers are determined from the general expression (8.58) for hard binaries, with the substitution $R = a ( 1 { + } e )$ to allow for possible initialization at smaller separations (e.g. after chain regularization or tidal dissipation). For soft binaries (i.e. $E _ { \mathrm { b } } > \epsilon _ { \mathrm { h a r d } }$ ), $R$ is replaced by max $\{ f _ { \epsilon } R _ { \mathrm { c l } } , R \}$ with $f _ { \epsilon } = 1 - \vert ( E _ { \mathrm { b } } - \epsilon _ { \mathrm { h a r d } } ) / \epsilon _ { \mathrm { h a r d } } \vert$ . This modification is intended to anticipate any significant expansion during the next orbit. At initialization, the actual apocentre distance is used, irrespective of energy, since the starting value of $R$ may be relatively small.

The perturber selection is formally carried out at the end of the step following the apocentre passage, defined by $t _ { 0 } ^ { \prime \prime } t ^ { \prime \prime } < 0$ and $R > a$ . However, the old perturbers may be retained if the next estimated apocentre time occurs before the corresponding c.m. update, i.e.

$$
t _ { \mathrm { K } } < t _ { 0 } + \Delta t _ { \mathrm { c m } } - t .
$$

Hence some unnecessary operations are saved for large values of $\Delta t _ { \mathrm { c m } } / t _ { \mathrm { K } }$ .

By analogy with the energy stabilization procedure in the difference formulation (cf. (4.43)), we have introduced rectification of the regularized elements at every apocentre subject to (11.9). This is achieved by the following algorithm. Given the correct value of $h$ obtained from integrating $h ^ { \prime }$ , we seek to modify $\mathbf { U } , \mathbf { U } ^ { \prime }$ by the coefficients $C _ { 1 } , C _ { 2 }$ such that $\tilde { h } = h$ , where $\tilde { h }$ is the explicit energy expression (4.24). Accordingly, we first write the energy relation in the form

$$
h = ( 2 { \bf U } ^ { \prime } { } ^ { 2 } C _ { 2 } ^ { 2 } - m _ { \mathrm { b } } ) / { \bf U } ^ { 2 } C _ { 1 } ^ { 2 } .
$$

By virtue of angular momentum conservation, $C _ { 1 } C _ { 2 } = 1$ , from which we obtain

$$
\begin{array} { r } { C _ { 2 } = \left\{ \frac { 1 } { 4 } m _ { \mathrm { b } } / \mathbf { U } ^ { \prime 2 } \pm [ \frac { 1 } { 2 } h R / \mathbf { U } ^ { \prime 2 } + ( \frac { 1 } { 4 } m _ { \mathrm { b } } / \mathbf { U } ^ { \prime 2 } ) ^ { 2 } ] ^ { 1 / 2 } \right\} ^ { 1 / 2 } . } \end{array}
$$

Here the square root sign is chosen according to the eccentric anomaly, with positive value if $\frac { 1 } { 4 } m _ { \mathrm { b } } / \mathbf { U } ^ { \prime 2 } < 1$ , or $R < a$ . The resulting modifications then yield the corrected values

$$
\begin{array} { r } { \tilde { \mathbf { U } } = C _ { 1 } \mathbf { U } , } \\ { \tilde { \mathbf { U } } ^ { \prime } = C _ { 2 } \mathbf { U } ^ { \prime } , } \end{array}
$$

which are used to initialize $R , \mathbf { U } _ { 0 }$ and $t _ { 0 } ^ { \prime \prime }$ . Since these adjustments are usually very small, there are no further complications. We note that the additional effort amounting to some 13 additions, 22 multiplications, two divisions and two square roots is insignificant compared with the cost of an entire orbit integration. For completeness, an alternative procedure is included for any rare case, which might be a circularized orbit, if the inner square root argument is negative. In that case we choose

$$
C _ { 1 } = m _ { \mathrm { b } } / ( - 8 h R \mathbf { U } ^ { \prime 2 } ) ^ { 1 / 2 } ,
$$

together with $C _ { 2 } = 1$ . This corresponds to $C _ { 1 } = 1$ for circular orbits or $C _ { 1 } = 1 / ( 1 - e ^ { 2 } ) ^ { 1 / 2 }$ at pericentre or apocentre.

Finally, if $\Delta t _ { \mathrm { c m } } < \Delta t _ { \mathrm { c l } }$ , a search is made for a possible chain regularization or hierarchical configuration at every apocentre consistent with (11.9) and also at the end of updates of unperturbed motion. The former check is in fact the last procedure of the KS integration cycle.

# 11.3 Stumpff Hermite version

Since the Stumpff version of KS regularization is now the method of choice, it is useful to concentrate on some aspects of implementation in a separate section. This method differs significantly in construction from the alternatives discussed in chapter 4, particularly when it comes to improving the solution by iteration.

Using the notation of section 4.7, we begin by writing the basic equations of motion at the start of an integration step in Hermite form as

$$
\begin{array} { r } { \mathbf { U } _ { 0 } ^ { ( 2 ) } = - \Omega _ { 0 } \mathbf { U } _ { 0 } + \mathbf { f } _ { 0 } ^ { ( 2 ) } , } \\ { \mathbf { U } _ { 0 } ^ { ( 3 ) } = - \Omega _ { 0 } \mathbf { U } _ { 0 } ^ { \prime } + \mathbf { f } _ { 0 } ^ { ( 3 ) } , } \end{array}
$$

where $\Omega = - \frac { 1 } { 2 } h$ and $\begin{array} { r } { \mathbf { f } _ { 0 } ^ { ( 2 ) } = \frac { 1 } { 2 } R \mathbf { Q } } \end{array}$ with ${ \bf Q } = \mathcal { L } ( { \bf U } ) { \bf P }$ as the perturbed force function, evaluated at the end of the previous corrector cycle. Likewise, the last term of the second equation (11.14) is obtained by comparing with the differentiated form of (4.69) and setting $\Omega = \Omega _ { 0 }$ ,

$$
\begin{array} { r } { { \bf f } _ { 0 } ^ { ( 3 ) } = \frac 1 2 R { \bf Q } ^ { \prime } + \frac 1 2 t _ { 0 } ^ { \prime \prime } { \bf Q } - \Omega _ { 0 } ^ { \prime } { \bf U } . } \end{array}
$$

The integration cycle begins by standard prediction of the coordinates and velocities of all perturbers and the c.m. particle. The prediction of $\mathbf { U }$ , $R$ and $\mathbf { U } ^ { \prime }$ is carried out to highest order which includes the pairwise Stumpff [1962] functions (4.59), $\tilde { c } _ { 4 } , \tilde { c } _ { 5 }$ and $\tilde { c } _ { 3 } , \tilde { c } _ { 4 }$ , respectively, as factors in the two derivatives $\mathbf { U } ^ { ( 4 ) }$ and $\mathbf { U } ^ { ( 5 ) }$ . After transformation to global coordinates and velocity, the perturbations $\mathbf { P } , \mathbf { P ^ { \prime } }$ are obtained in the usual way and the slow-down factor $\kappa$ (to be described later) is included if relevant.

The corrector cycle first evaluates the new perturbative functions

$$
\begin{array} { r l } & { \mathbf { f } ^ { ( 2 ) } = ( \Omega _ { 0 } - \Omega ) \mathbf { U } + \frac { 1 } { 2 } R \mathbf { Q } , } \\ & { \mathbf { f } ^ { ( 3 ) } = ( \Omega _ { 0 } - \Omega ) \mathbf { U } ^ { \prime } - \Omega ^ { \prime } \mathbf { U } + \frac { 1 } { 2 } R ^ { \prime } \mathbf { Q } + \frac { 1 } { 2 } R \mathbf { Q } ^ { \prime } . } \end{array}
$$

It can be seen that the first of these equations takes its form from (4.69), where the analogy with an Encke-type formulation is evident. This enables construction of the higher derivatives by the Hermite rule (2.20), which yields the expressions

$$
\begin{array} { r } { \mathbf { U } _ { 0 } ^ { ( 4 ) } = - \Omega _ { 0 } \mathbf { U } _ { 0 } ^ { ( 2 ) } + \mathbf { f } _ { 0 } ^ { ( 4 ) } , } \\ { \mathbf { U } _ { 0 } ^ { ( 5 ) } = - \Omega _ { 0 } \mathbf { U } _ { 0 } ^ { ( 3 ) } + \mathbf { f } _ { 0 } ^ { ( 5 ) } . } \end{array}
$$

Note that $\mathbf { Q } ^ { \prime }$ is obtained from $\mathbf { P } ^ { \prime } = R \dot { \mathbf { P } }$ together with $\mathcal { L } ( \mathbf { U } ^ { \prime } )$ . The provisional solution of the first equation (4.67) and its derivative, $\mathbf { U } ^ { \prime }$ , is improved by one full iteration of (11.16) and (11.17) without recalculating the perturbations. Hence the nested solution is evaluated twice to full order, including the pairwise Stumpff functions. As compensation for the extra effort of the iteration, high accuracy is achieved for a somewhat larger integration step.

According to the second equation (4.56), the energy integration

$$
\Omega ^ { \prime } = - \mathbf { U } ^ { \prime } \cdot \mathbf { Q }
$$

remains the same as for the standard Hermite case. Substitution for $\mathbf { U } ^ { ( 2 ) }$ gives rise to the second derivative

$$
\Omega ^ { ( 2 ) } = \Omega _ { 0 } { \bf U } \cdot { \bf Q } - { \bf f } ^ { ( 2 ) } \cdot { \bf Q } - { \bf U } ^ { \prime } \cdot { \bf Q } ^ { \prime } .
$$

The two Hermite corrector terms formed from $\Omega ^ { \prime }$ and $\Omega ^ { ( 2 ) }$ are added to the predicted value to yield an improved solution for $\Omega$ at the start of an iteration or at an endpoint.

The corrector cycle ends by saving all the derivatives ${ \bf U } ^ { ( n ) }$ , $n = 2 , 3 , 4 , 5$ , as well as the perturbative derivatives (11.16). For this purpose it is advantageous to employ the final values of $R$ and $R ^ { \prime }$ since the re-evaluation of (11.16) is fast and these expressions also enter $\mathbf { U } ^ { ( 2 ) }$ and $\mathbf { U } ^ { ( 3 ) }$ . Finally, it is beneficial to improve the penultimate derivatives by addition of the next order,

$$
\begin{array} { r } { \mathbf { U } ^ { ( 4 ) } = \mathbf { U } _ { 0 } ^ { ( 4 ) } + \mathbf { U } _ { 0 } ^ { ( 5 ) } \Delta \tau , } \\ { \Omega ^ { ( 3 ) } = \Omega _ { 0 } ^ { ( 3 ) } + \Omega _ { 0 } ^ { ( 4 ) } \Delta \tau . } \end{array}
$$

Unless the step $\Delta \tau$ is constant, new coefficients $\tilde { c } _ { n }$ must be re-evaluated every time. The summation to twelfth order does represent a modest extra cost, estimated as a few per cent of one KS step; however, the improvement in accuracy is substantial [cf. Mikkola $\&$ Aarseth, 1998]. The coefficients $\tilde { c } _ { n }$ for $n = 3 , 4 , 5$ are generated by recursion from $n = 1 2$ . The argument $_ { 4 z }$ then yields $\tilde { c } _ { 5 } ( 4 z )$ and $\tilde { c } _ { 6 } ( 4 z )$ by the same method; hence orders $n < 5$ need not be evaluated. $^ \dagger$ This task is most conveniently carried out just after the determination of the regularized step, (8.59), since the next physical time-step (11.1) must be modified by including the coefficients $\tilde { c } _ { 5 } ( 4 z )$ , $\tilde { c } _ { 6 } ( 4 z )$ in the last two terms (cf. (4.67)). At the same time, the reference energy $\Omega _ { 0 }$ must be updated and saved. Accordingly, this scheme requires 16 additional variables for each KS pair, including seven Stumpff functions, compared with the standard Hermite KS formulation.

Finally, we note some similarity of this scheme to the recalculation of the dominant term in the time-symmetric method [Kokubo, Yoshinaga $\&$ Makino, 1998], discussed in section 2.7. Thus, for small perturbations, the term $\scriptstyle { \frac { 1 } { 2 } } h \mathbf { U }$ and its derivative are analogous to the role of the dominant solar interaction. Moreover, the regularized step is also fairly constant if the perturbation is small. Note that a constant value of $\Delta \tau$ does not avoid a re-evaluation of the Stumpff functions because the argument $\Omega \Delta \tau ^ { 2 }$ would still be changing slightly.

# 11.4 KS termination

The actual termination of two-body regularization requires a number of special procedures to be carried out and is best described in a separate section. In the following we assume the Stumpff version, although many algorithms are fairly similar for the alternative formulations. The main steps are summarized in Algorithm 11.1.

Unless collision occurs, it is advantageous to advance the KS solution to the end of the block-step. In the case of large perturbations, this is achieved by delaying the termination procedure until the physical timestep is smaller than the remaining interval. Alternatively, one or more standard KS steps are carried out in situ if required. The residual interval $\delta \tau$ is then obtained by one Newton–Raphson iteration of (11.1) to third order, whereupon the final integration step is performed without any further complications. Since the Stumpff functions depend on $\delta \tau$ by (4.59), the coefficients also need to be recalculated. Consequently, the global time is now defined to be at the end of the block-step.

Any dominant perturbers are predicted to high order before the potential energy interaction between the components and all the perturbers is obtained. Following rectification of $\mathbf { U }$ and $\mathbf { U } ^ { \prime }$ to ensure consistency, the differential energy correction is obtained and added to the term $E _ { \mathrm { c o l l } }$ for conservation purposes.

Algorithm 11.1. Termination of KS regularization.   

<table><tr><td>1 2</td><td>Advance the KS solution for pair i until tblock - t2i-1 &lt; △t2i-1 Take the final step with δT obtained by third-order iteration Predict coordinates and velocity for any dominant perturber Evaluate potential energy of binary components and perturbers Rectify the orbit to yield U,U&#x27; consistent with the value of h Determine current coordinates and velocities of KS components Save basic KS variables in case of a stable hierarchical merger 8 Obtain improved coordinates and velocities of the components</td></tr></table>

If the terminating KS pair is not the last in the sequence (i.e. $\textit { i } <$ $N _ { \mathrm { p } }$ ), all the relevant common arrays are moved down to the first single particle locations, $2 N _ { \mathrm { p } } + 1$ , $2 N _ { \mathrm { p } } + 2$ , while the subsequent quantities are compressed, and likewise for the corresponding KS and c.m. arrays. It is also necessary to update all common array lists since global locations are referred to. This entails replacement of the c.m. by its components and reduction of any subsequent members, $j > N + i$ , by one. Although this is an $O ( N )$ procedure, only a few operations per particle are needed, and the overheads for the sequential data structure are less than the cost of polynomial initialization. $^ \ddag$ In any case, the number of KS terminations is usually quite modest. Finally, in addition to step 14, the force polynomial for any dominant perturber that triggers termination is also initialized in order to be consistent with the current configuration.

Time quantization in the Hermite scheme has certain implications for the time-steps relating to close two-body encounters. In the first place, KS solutions are inevitably initialized at small values of $\Delta t _ { i }$ , which usually means few block-step members. Consequently, both the irregular and regular steps for the associated c.m. body are severely restricted by the small block-step even if the natural step is large. The inefficiency on termination is less significant, since such procedures are performed at arbitrary block times, where at least the regular time-steps may be assigned more typical values. To compensate, most KS solutions are connected with binaries which tend to have long life-times and the initial c.m. steps also increase quickly if conditions are favourable. The question remains, however, whether improved strategies can be devised.

# 11.5 Unperturbed two-body motion

The perturber search for hard binaries frequently results in zero membership for the adopted criterion (8.58). This situation is inevitable, given the $N$ -dependence of the mean particle separation and the typical perturber distance $\lambda R _ { \mathrm { c l } }$ , particularly since many primordial binaries are superhard. If no perturbers are identified following a new search at apocentre, the two-body motion is defined to be unperturbed during the next orbit, with the time-step given by the period, $\Delta t = t _ { \mathrm { K } }$ . Consequently, only the centre of mass needs to be advanced, with the further simplification that the force evaluation is identical to that of a single particle.

The status of an unperturbed binary needs to be rechecked one period later. However, by a more careful analysis of the associated neighbour velocity field, it is possible to estimate the time for approaching particles to come within a certain distance and hence extend the interval of unperturbed motion. The main steps of this procedure are set out below.

From the corresponding list $\ S$ of c.m. neighbours, we determine the particle, $j$ , giving the maximum force as well as the smallest inverse travel time, $\beta _ { s } = \mathbf { r } _ { s } \cdot \dot { \mathbf { r } } _ { s } / r _ { s } ^ { 2 }$ for particle index $s$ . In the following all distances and velocities are expressed with respect to the c.m. Although there may not be any approaching particles, we still use this quantity which defines a radial velocity $\dot { r } _ { s } = r _ { s } | \beta _ { s } |$ . Let us introduce the perturber boundary for any particle mass $\tilde { m }$ by

$$
r _ { \gamma } = R [ 2 \tilde { m } / ( m _ { \mathrm { b } } \gamma _ { \mathrm { m i n } } ) ] ^ { 1 / 3 } ,
$$

with $m _ { \mathrm { b } }$ the mass of the binary. The time to reach this boundary with inward motion is then

$$
\Delta t _ { \mathrm { i n } } = ( r _ { s } - r _ { \gamma } ) / | \dot { r } _ { s } | ,
$$

with $m _ { s }$ substituted for $\tilde { m }$ in (11.21).

We now evaluate a second travel time for the same particle, based on the acceleration, by

$$
\Delta t _ { \mathrm { a } } = [ 2 \Delta t _ { \mathrm { i n } } | \dot { r } _ { s } | r _ { s } ^ { 2 } / ( m _ { \mathrm { b } } + m _ { s } ) ] ^ { 1 / 2 } .
$$

Similarly, if $j \neq s$ the dominant body, which may be near a turning point, would have a return time

$$
\Delta t _ { j } = [ 2 ( r _ { j } - r _ { \gamma } ) r _ { j } ^ { 2 } / ( m _ { \mathrm { b } } + m _ { j } ) ] ^ { 1 / 2 } ,
$$

with $m _ { j }$ substituted in (11.21). The next unperturbed time interval is then chosen by

$$
\Delta t _ { \gamma } = \operatorname* { m i n } \left\{ \Delta t _ { \mathrm { i n } } , \Delta t _ { \mathrm { a } } , \Delta t _ { j } \right\} .
$$

In case the background force dominates, it is also prudent to include the safety condition $\Delta t _ { \gamma } = \operatorname* { m i n } \left\{ \Delta t _ { \gamma } , 2 \Delta t _ { \mathrm { c m } } \right\}$ .

An additional check is performed if the final value of the time interval exceeds the period. Thus if we have $\Delta t _ { \gamma } < 2 \times 1 0 ^ { 9 } t _ { \mathrm { K } }$ , the number of unperturbed periods is chosen conservatively by

$$
\begin{array} { r } { K = 1 + \frac { 1 } { 2 } \Delta t _ { \gamma } / t _ { \mathrm { K } } . } \end{array}
$$

Finally, the corresponding time-step itself is taken to be

$$
\Delta t _ { k } = K \operatorname* { m i n } \left\{ t _ { \mathrm { K } } , \Delta t _ { \mathrm { c m } } \right\} ,
$$

where $k = 2 ( i - N ) - 1$ denotes the first KS index of the c.m. particle $i$ . The latter precaution is included if the period exceeds $\Delta t _ { \mathrm { c m } }$ . In the case of an extremely short period, with $K > 1 0 ^ { 9 }$ , it is sufficient to use the c.m. step itself.

Given the neighbour list, the above procedure is relatively inexpensive and may be speeded up further by restricting the initial search distance. The use of two time-scales provides for the possibility of a more distant perturber approaching first. If there is no such particle and the dominant body is also moving outwards, the above expressions are conservative. Hence the main purpose of the algorithm is to prevent the unperturbed condition from being violated during the next interval, which is chosen as large as possible subject to kinematical considerations.

If it turns out that $\Delta t _ { k } < t _ { \mathrm { K } }$ , a new perturber search is performed in the usual way. In the unlikely event that no perturber is selected, the motion is assumed to be unperturbed during the next period. Alternatively, an update of the physical coordinates and velocity takes place, followed by initialization of the KS polynomials using a slow-down factor $\kappa = 1$ .

For completeness, we remark that a counter accumulates the number of elapsed unperturbed orbits, given by

$$
\begin{array} { r } { n _ { \mathrm { K } } = ( t - t _ { 0 } ) / t _ { \mathrm { K } } , } \end{array}
$$

where $t _ { 0 }$ refers to the previous epoch. If this counter exceeds the integer limit $2 \times 1 0 ^ { 9 }$ , it is set to zero again and a second counter is advanced by one. This situation occurs quite frequently in large simulations and demonstrates the necessity of introducing unperturbed two-body motion. An algorithm for partial unperturbed motion, no longer used in the codes, is given by Appendix D.5.

# 11.6 Slow-down in KS

The theory of the adiabatic invariance for weakly perturbed binaries in chain regularization is given in chapter 5, together with the algorithm. The same principle can be used in KS regularization, where weak perturbations are a characteristic feature to be exploited. Since explicit information is available for the two-body elements, it is possible to change the strategy and only re-evaluate the slow-down factor at the apocentre. In the following we describe the implementation in the Stumpff KS formulation [Mikkola & Aarseth, 1998], but all the procedures have also been adopted in the older codes, NBODY 3 and $N B O D Y 5$ .

Given the basic equations of motion (4.37) and (4.38), the slow-down concept is introduced by scaling the perturbing force and its derivative according to

$$
\begin{array} { r } { \widetilde { { \mathbf P } } = \kappa { \mathbf P } , } \\ { \widetilde { { \mathbf P } } ^ { \prime } = \kappa { \mathbf P } ^ { \prime } , } \end{array}
$$

where the dimensionless factor $\kappa$ plays the same role as in chain regularization. In addition, (4.39) should be replaced by

$$
t ^ { \prime } = \kappa \mathbf { U } \cdot \mathbf { U } .
$$

Hence one regularized period now represents $\kappa$ actual periods, with the regularized time-step chosen as before. Now the required modifications are simple and only represent minor complications. However, in order to achieve an optimized scheme the determination of $\kappa$ provides a new challenge. This is desirable since a typical $N -$ -body simulation with primordial binaries usually involves large numbers of perturbed periods, with a significant proportion having small perturbations. It is these weakly perturbed binaries that can be studied advantageously with the slow-down procedure.

The value of $\kappa$ is most conveniently determined at an apocentre point, where the magnitude (but not necessarily the effect) of the perturbation tends to be largest. Not every apocentre passage needs be considered. Thus we only perform this check at the same time as the redetermination of new perturbers, defined as the time for which $\kappa t _ { \mathrm { K } } > t _ { \mathrm { c m } } + \Delta t _ { \mathrm { c m } } - t$ , where $t _ { \mathrm { K } }$ denotes the binary period and $t _ { \mathrm { c m } }$ is the time of the last c.m. integration endpoint.

In order to implement the slow-down procedure, we define $\kappa$ to be an integer and introduce a hierarchical slow-down vector $I _ { \mathrm { s l } } = 2 ^ { k - 1 }$ , where $k$ takes the values $1 , 2 , \ldots$ up to some maximum (say 10). Given the relative perturbation $\gamma$ , the steps for obtaining the new $\kappa$ from the old value $\kappa _ { 0 }$ are set out in Algorithm 11.2, originally given in Mikkola & Aarseth [1996].