bars. A least-square solution gave a power-law for the probability of binary formation as

$$
P _ { \mathrm { b i n } } \simeq 4 X ^ { - 2 } .
$$

This numerical solution is consistent with the asymptotically largest contribution obtained by a theoretical derivation§ [cf. Aarseth & Heggie, 1976]. Based on this result, it was shown that the binary formation rate per crossing time is independent of $N$ and that essentially all such binaries are soft. The present work provided quantitative answers to a classical problem and the numerical results guided the theoretical derivation, demonstrating the usefulness of the experimental approach.

The case of equal masses continued to attract attention. With greater coverage of parameter space, improved comparison with analytical approximations becomes feasible. One such ambitious undertaking [Hut & Bahcall, 1983] studied over $1 0 ^ { 6 }$ scattering experiments without making assumptions about dependence on orientation, phase angle or impact parameter. The results yielded cross sections for ionization, exchange and resonance scattering as functions of intruder velocity. The total cross section for an event $Z$ can be obtained from the numerical results by

$$
\sigma _ { Z } ( v ) = F n _ { Z } ( v ) / n _ { \mathrm { t o t } } ( v ) ,
$$

where $n _ { \mathrm { t o t } }$ is the total number of initial conditions for which event $Z$ can occur, $n z$ is the number of actual events and $F$ is a factor that includes gravitational focusing.

Although the humble RK4 integrator was used, careful analysis justified the acceptance of relatively large energy errors. The essential point is that the total error of a cross section can be determined in Monte Carlo sampling, taking into account all the sources of uncertainty. Of the nine independent initial parameters that are required for a complete mapping of phase space, the masses and eccentricity were assigned fixed values, whereas the four angular variables were randomized. The impact parameter was sampled uniformly in $\rho ^ { 2 }$ up to a maximum given by

$$
\rho _ { \mathrm { m a x } } ( v ) = ( C / v + D ) a ,
$$

with $C$ and $D$ appropriate constants, reflecting the effect of gravitational focusing. Finally, the intruder velocity was scaled according to (18.2) and chosen in a specified range.

Additional experiments were later made for high intruder velocity [Hut, 1983]. Further analysis of the numerical results combined with analytical approximations yielded an accurate description over a complete range of parameters [Hut, 1983, 1993]. Thus differential cross sections were derived for binary–single star scattering at high intruder velocity, together with total cross sections for ionization and exchange which were shown to be independent of binary eccentricity. These results for equal masses agree with analytical calculations [Heggie, 1975]. The water-shed effect for equal masses and a thermal binary eccentricity distribution was redetermined, yielding $\alpha _ { \mathrm { c } } \simeq 0 . 4 8$ [Hut, 1993], in fair agreement with earlier values [Fullerton & Hills, 1982] based on zero impact parameter. Comprehensive fitting formulae for exchange reactions of arbitrary mass ratios have also been obtained [Heggie, Hut & McMillan, 1996]. The semi-analytical fitting functions are accurate to $2 5 \%$ for most mass ratios. In order to facilitate exploration of the three-body problem further, an automated scattering package has been developed and the software is freely available. $^ \mathparagraph$

Special three-body scattering experiments are sometimes motivated by astrophysical considerations. One investigation examined configurations where the intruding star is more massive by a factor of 2, which is relevant to globular cluster cores [Sigurdsson $\&$ Phinney, 1993]. These simulations again employed the RK4 integrator. Analysis of $1 \times 1 0 ^ { 5 }$ experiments showed that for moderately hard binaries, exchange is the dominant process. Moreover, exchange of a heavy field star actually increases the cross section in future encounters since the binary tends to widen while becoming more strongly bound. It was also found that resonances contribute significantly to physical collisions.

To conclude this brief review of some salient three-body scattering experiments, it is evident that this beautiful problem still contains a wealth of fascinating complexity which is waiting to be unravelled.

# 18.4 Binary–binary interactions

The addition of a fourth body increases the number of variables considerably. Thus with two initial binaries, we have four more angles, as well as a second mass ratio, semi-major axis and eccentricity. Hence it is not surprising that so few studies have been made in four-body scattering. Moreover, this problem is also harder numerically and some kind of regularization method is beneficial.

The first modest outcomes of binary–binary encounters already showed some features of interest [Th¨uring, 1958]. The impact of two equal circular binaries was integrated by hand, with the number of differential equations reduced by half due to symmetry. The choice of initial conditions led to escape, with the binaries considerably more strongly bound and having reversed orbital spins. After examination of the c.m. velocity gain, the modern concept of a hyper-elastic encounter was defined. Because of the analogy with binary–binary scattering, we also mention that further electronic calculations of impacting four-body systems by the Adams– Moulton method were performed subsequently [Th¨uring, 1968]. This work introduced the additional concepts of elasticity, interaction energy, as well as hard and soft configurations, which are still topical.

The early 1980s saw a pioneering investigation which was not repeated for a long time [Mikkola, 1983, 1984a,b,c], as is often the case with a hard mountaineering ascent. Some 3000 experiments were performed in the first study, which was restricted to equal masses and semi-major axes. The impact parameters were randomized to give an equal number of impacts on equal areas up to a limiting value, i.e. $\psi ( \rho ) = 2 \rho / \rho _ { \mathrm { m a x } } ^ { 2 }$ . This sample proved sufficient for obtaining meaningful results of fly-by interactions as a function of the impact energy. Four types of final motions were delineated for purposes of data analysis:

Two binaries in a hyperbolic relative orbit One escaper and a hierarchical triple system • One binary and two escapers • Total disruption into four single stars

If none of these categories were confirmed, the configuration was classified as undecided and the integration continued. The majority of outcomes were of the first type, with the third type well represented. This dataset also provided early evidence of hierarchical triple formation (type two), especially at low impact energy, although stability was not checked.

A further 1800 cases of strong interactions with smaller values of the maximum impact parameters were also investigated. Such interactions are of particular interest and may lead to quite complex behaviour. Thus one star may be ejected in a bound orbit and return after the escape of a second ejected star. The problem is then reduced to the three-body case. Alternatively, the softest binary may become more weakly bound and return for a strong interaction with the escape of only one component. In both these processes the remaining triple can be very wide. Analysis of these configurations based on two values of the critical outer pericentre ratio for an approximate criterion [cf. Harrington, 1972] yielded a high proportion of stable systems, with about $2 0 \%$ at modest impact energies. The question of exchange with two binaries surviving was also addressed. Thus at the smallest impact energy, the probability of exchange was about

$5 0 \%$ . Finally, the distribution of energies in the case of two escapers was given. More general initial conditions were studied later [Mikkola, 1984b,c] and a start was made on the important extension to unequal masses [Mikkola, 1985b, 1988]. The provisional result $P \propto ( m _ { i } m _ { j } ) ^ { 3 }$ was obtained for the probability of the remaining binary masses in both three- and four-body systems.

A special integration method was devised in order to deal with the different configurations discussed above [Mikkola, 1983]. At the beginning of this work, a fourth-order polynomial method for direct integration was used together with the two-body regularization method of section 4.5 [Burdet, 1967; Heggie, 1973]. However, persistent configurations consisting of a close binary and two eccentric elliptical orbits proved too expensive. A code combining three different solution methods was therefore developed. Long-lived hierarchies were treated as perturbed Keplerian orbits using the classical variation of parameters method, and more than one relative motion could be studied at the same time. Direct integration was employed for non-hierarchical systems not benefiting from regularization. Finally, the global regularization method [Heggie, 1974] was modified to a more convenient form for practical use [Mikkola, 1985a]. This three-part implementation was quite efficient and contained sophisticated decisionmaking. As a unifying thread, all the relevant equations of motion were advanced by the powerful Bulirsch–Stoer [1966] method.

For completeness, we record another contemporary binary–binary scattering experiment [Hoffer, 1983]. A time-smoothing technique [Heggie, 1972a] was used, combined with the c.m. approximation for a hard binary and the equations were integrated by the RK4 method. Because of numerical problems, this study was unable to deal with hard binary interactions and the results are therefore of limited validity. However, the importance of physical collisions in such encounters was highlighted. Over the subsequent years, there have been very few four-body scattering experiments. A preliminary study of scattering cross sections [Hut, 1992] for equal masses emphasized the frequent occurrence of hierarchical triple formation. A distinction was made between systems preserving one of the inner binaries and those undergoing exchange. Given the relatively small effort so far in this fundamental problem, the time is ripe for a renewed attack.

A thorough comparison of regularization methods for binary–single star and binary–binary scattering was very informative [Alexander, 1986]. All the current multiple regularization schemes were examined [Aarseth $\&$ Zare, 1974; Zare, 1974; Heggie, 1974], together with different choices for the time transformation. Although the initial conditions of the main comparisons were based on symmetrical configurations starting from rest, some results were also presented for more general scattering experiments which gave rise to hierarchical triples.∗∗

A number of careful tests were made for three-body and four-body systems, including time reversal, and the Poincar´e control term was also included [Baumgarte & Stiefel, 1974]. From the general form (5.66) of the equations of motion, we have the relation [cf. Alexander, 1986]

$$
\frac { d } { d \tau } \left[ \frac { 1 } { 2 } ( H - E _ { 0 } ) ^ { 2 } \right] = - ( H - E _ { 0 } ) ^ { 2 } \frac { 1 } { g } \frac { d g } { d \tau } .
$$

Hence stabilization of the integral $H - E _ { 0 } = 0$ is achieved when $g$ increases along the solution path. This condition is satisfied for the time transformation $g = 1 / L$ if the Lagrangian is decreasing; i.e. after pericentre passage. It may therefore be beneficial to reverse the sign of each control term when $g$ is decreasing. This device was already used without regularization [Zare & Szebehely, 1975]. However, care must be taken near critical situations with regularization since the regularity is lost.

After testing several alternative time transformations, as well as the standard forms, the inverse Lagrangian was favoured on grounds of accuracy and efficiency. Somewhat surprisingly, the wheel-spoke regularization [Zare, 1974] appeared to give smaller residual errors than the global method for $N = 4$ . However, it should be noted that only one type of initial conditions were examined, in which close triple encounters may have been less important. Based on these results, we would therefore expect the subsequent chain regularization method [Mikkola & Aarseth, 1993] to be competitive for binary–binary scattering. As described earlier, it has already proved itself in $N$ -body simulations with primordial binaries.

A special code for analysing scattering experiments was also developed [Alexander, 1986]. By analogy with (18.2), the critical velocity in the four-body case is defined as

$$
V _ { \mathrm { c } } ^ { 2 } = { \frac { m _ { 1 } + m _ { 2 } + m _ { 3 } + m _ { 4 } } { ( m _ { 1 } + m _ { 2 } ) ( m _ { 3 } + m _ { 4 } ) } } \left[ { \frac { m _ { 1 } m _ { 2 } } { a _ { 1 } } } + { \frac { m _ { 3 } m _ { 4 } } { a _ { 2 } } } \right] .
$$

This quantity can then be used to define the dimensionless hardness parameter, $x = ( V _ { \mathrm { f } } / V _ { \mathrm { c } } ) ^ { 2 }$ . Comparison of a three-body scattering experiment with hardness $x = 1 0 ^ { 4 }$ showed agreement in the final values of $a$ and $e$ for the different methods. However, in the case $N \ = \ 4$ and $x = 1 0 ^ { 2 }$ , the identity of the second escaper was not the same; consequently the final binary elements did not agree. There were many temporary ejections and exchanges and the assumption of unperturbed two-body motion also introduced further uncertainty. The code was subsequently used for binary–binary scattering experiments [Leonard & Linnell, 1992] in connection with the collision hypothesis for blue stragglers.

Further binary–binary scattering experiments were made using astrophysical parameters, including realistic stellar radii, for modelling collisions [Leonard, 1995]. Thus a cluster potential with rms escape velocity $3 . 5 \mathrm { k m s ^ { - 1 } }$ was assumed for reference. The binaries were generated with masses $2 { - } 2 0 M _ { \odot }$ and uniformly distributed periods 1–100 d for a total of 2000 experiments. A considerable fraction of O-type stars formed by collisions were ejected with sufficiently high velocities ( $> 3 0 \mathrm { k m s ^ { - 1 } } )$ to be associated with runaway stars. It was also emphasized that it is difficult to distinguish between runaway stars originating by dynamical slingshot ejection and the supernova mass-loss mechanism in binaries.

The globular cluster M4 contains a unique triple system where one of the inner binary components is a pulsar. A model based on exchange was proposed to account for the existence of the old pulsar inside a soft outer binary inferred from observations [Rasio, McMillan & Hut, 1995]. In this scenario, it was assumed that the inner binary ( $a _ { \mathrm { i n } } = 0 . 8$ au) only suffered a small perturbation during a close binary–binary encounter, consistent with the small eccentricity, $e _ { \mathrm { i n } } = 0 . 0 2 5$ . Accordingly, a three-body scattering experiment was performed using the ST ARLAB package, with the exchange probability estimated after excluding a minimum impact parameter of $3 a _ { \mathrm { i n } }$ obtained from separate calculations. Even so, the maximum probability of triple formation was found to be about $5 0 \%$ in the most favourable case of a pre-encounter binary with semi-major axis 12 au which would typically form a wide outer binary, $a _ { \mathrm { o u t } } \simeq 1 0 0$ au.

Strong binary–binary interactions in star cluster simulations often lead to physical collisions with the possible formation of exotic objects [cf. Mardling & Aarseth, 2001]. An extensive series of such scattering experiments was undertaken with a view to clarifying this question [Bacon, Sigurdsson & Davies, 1996]. The selection of initial conditions followed earlier three-body studies [Hut & Bahcall, 1983]. A set of experiments was defined by fixed semi-major axes, masses and a range of intruder velocities, the other elements being sampled by Monte Carlo techniques. A total of $1 0 ^ { 5 }$ experiments were performed, divided into 25 sets. Both the RK4 integrator and chain regularization were used. However, the secular drift in total energy became unacceptable with the former when the semi-major axes ratio exceeded 2.

The following five usual types of outcome were examined: fly-by, exchange, breakup, stable triple and unresolved experiment. The latter reached a maximum of 5% in the case of equal semi-major axes, with $2 \%$ being typical. Surprisingly, the fraction of exchange cases was quite small and reached at most 4%. A somewhat higher proportion of exchange for equal masses, likewise with two surviving binaries, was seen in an earlier experiment for a small sample [Mikkola, 1983]. Stable triples were defined according to the simplified Harrington [1972] criterion,

$$
R _ { \mathrm { p } } ^ { \mathrm { c r i t } } = 3 \left( 1 + e _ { \mathrm { i n } } \right) a _ { \mathrm { i n } } ,
$$

which does not include the masses (cf. (15.13) and (15.15) for improved expressions). Moreover, in view of (9.14), the numerical factor increases by 2.0 for a characteristic outer eccentricity of 0.9 instead of zero. Bearing in mind that many systems exceed the stability ratio by modest amounts, the adopted definition is somewhat optimistic.

A primary motivation for the above work was to estimate the rate of tidal encounters and physical collisions from binary–binary interactions in globular clusters. This requires the determination of the minimum periastron distance, $r _ { \mathrm { m i n } }$ , which is about three times the radius of a mainsequence star for significant tidal effects [Press $\&$ Teukolsky, 1977]. The derived cumulative cross section may be compared with a power-law fit

$$
\tilde { \sigma } ( \operatorname* { m i n } _ { j \neq i } \{ r _ { i j } \} \leq r _ { \operatorname* { m i n } } ) = \sigma _ { 0 } \left( \frac { r _ { \operatorname* { m i n } } } { a _ { 1 2 } } \right) ^ { \nu } ,
$$

where $a _ { \mathrm { 1 2 } }$ is taken to be the geometric mean of the semi-major axes. The resulting graphs are conveniently approximated by piece-wise fitting for two values of the exponent, $\nu$ . With this approximation, the number of tidal interactions or physical collisions may be estimated from typical cluster core densities and binary properties. In the latter case, these estimates range from a few to about 500 for core densities in the range $1 0 ^ { 2 } { - } 1 0 ^ { 6 } \mathrm { p c } ^ { - 3 }$ and binary fractions $f _ { \mathrm { b } } ~ \simeq ~ 0 . 1$ . Note that such estimates are highly uncertain since eccentricity-induced processes in hierarchical systems cannot easily be taken into account [Mardling & Aarseth, 2001].

Recently an under-estimate of the smallest two-body distances was noted which affects the lower end of the cumulative cross section [Rasio, private communication, 2001]. Thus, in the calculations, $r _ { \mathrm { m i n } }$ was simply taken as the minimum distance, specified at the end of each integration step. It is a property of regularization methods that the time-steps may be large during close encounters, provided the perturbation is small. Below we give a general algorithm for determining the pericentre distance which is also appropriate for three-body and chain regularization [Mikkola, private communication, 1990].

In this general-purpose algorithm, $\mathbf { U } ^ { \prime }$ represents the actual derivative used in the equations of motion, together with the corresponding $t ^ { \prime }$ , and the relevant two-body terms are identified. A well-defined result for the eccentricity is obtained since the division by $R$ at step 4 cancels; hence the pericentre distance $Q _ { \mathrm { p } }$ is regular. The same algorithm also applies to standard KS regularization. Note that this formulation is based on osculating solutions of the two-body problem and should therefore only be used for small relative perturbations.

Algorithm 18.1. Pericentre determination.   

<table><tr><td>1</td><td> Form the square of the KS cross product, C = |U × U&#x27;|2</td></tr><tr><td>2</td><td> Set physical transformation factor, D = (2R/t&#x27;)²/(m1 + m2)</td></tr><tr><td>3</td><td>Construct the semi-latus rectum by p = CD</td></tr><tr><td>4</td><td>Obtain the inverse semi-major axis, a-1 = (2 - D|U&#x27;/2)/R</td></tr><tr><td>5</td><td>Derive the eccentricity from e = (1 - p/a)1/2</td></tr><tr><td>6</td><td> Evaluate non-singular pericentre distance, Qp = p/(1+ e)</td></tr></table>

Finally, we mention another approach where multiple regularization methods are used to investigate scattering outcomes in more detail. Thus Monte Carlo simulations of star clusters containing primordial binaries can be considered as a series of scattering experiments in parallel. First results of an implementation using unperturbed three-body [Aarseth $\&$ Zare, 1974] and Heggie [1974] four-body regularization have already been obtained [Giersz & Spurzem, 2003]. Hopefully, the more general method of perturbed chain regularization can also be included in this treatment. Hence the Monte Carlo method allows all the usual processes discussed earlier to be examined in considerable detail.

# 18.5 Chaos and stability

Given the complexity of the three-body problem, it is perhaps surprising that the case of 1D did not receive much attention in the early days. A series of papers [Mikkola & Hietarinta, 1989, 1990, 1991] describes complicated behaviour of chaotic type. In this section, we first consider a few investigations that emphasize such features and also provide applications of the three-body and chain regularization methods. The 1D formulation has already been elucidated earlier, with the Hamiltonian for equal masses given by (5.14).

Two final states of solutions are possible in 1D problems. Break-up is defined as a binary with energy ratio $E _ { \mathrm { b } } / E > 1$ , together with the third particle outside $1 0 0 a$ . The ratio $z = E / E _ { \mathrm { b } }$ is a convenient parameter for displaying results since it is confined to the interval [0,1]. It turns out that the life-time of the interplay phase divides the interactions into two well-defined regions in both directions of time. In so-called ‘zero interplay time’, a close triple encounter occurs only once early on and the outcome is a continuous function of the initial conditions. For longer interplay times, the orbits depend sensitively on the initial conditions and hence are chaotic. There is also a small region of infinite interplay time of quasiperiodic motions in the neighbourhood of the well-known Schubart [1956] periodic orbit.

A second similar investigation was made for positive energies. The characteristic types of final motions are either a binary and a single particle or complete ionization. Properties of the orbits are summarized in 2D maps of initial values and the transition from negative to positive energy is illustrated. For completeness, we mention the third paper which is mainly concerned with a survey of the periodic orbit for a grid of masses. The numerical solutions are used extensively to map the regions of stability and compare the results with linear stability analysis. Remarkably, linearly stable orbits transformed to 3D survived over at least several thousand periods when integrated directly by the method of section 5.2.

Recently an analogous study was made of the symmetrical four-body problem in 1D [Sweatman, 2002a]. Application of chain regularization yields a simple Hamiltonian of the type (5.14) with four well-behaved equations of motion. Again the motion can be divided into two main categories, where scattering orbits are characterized by systems starting and finishing as subsystems of binaries and single particles, whereas for bound orbits all the four bodies are confined. Moreover, scattering orbits are subdivided into fast and chaotic types, in which all bodies come together either once or a number of times, respectively. A subregion was chosen to illustrate the chaotic behaviour in greater detail and the elements of a Schubart-type periodic orbit were determined by iteration.

Returning to 2D, the effect of chaos was seen in an investigation which applied perturbed velocities to the initial conditions of the Pythagorean Problem [Aarseth et al., 1994a]. A novel feature in these experiments was to ascertain reproducibility by including time reversal after escape and to measure the final rms errors in position and velocity, $\sigma _ { x }$ and $\sigma _ { v }$ . An initial tolerance of $1 0 ^ { - 1 3 }$ was used with the T RI P LE code. Each experiment was repeated with 100 times reduced tolerance if the errors were not acceptable; i.e. max $\{ \sigma _ { x } , \sigma _ { v } \} < 1 \times 1 0 ^ { - 3 }$ . This procedure, which allows a determination of successful experiments, may be considered a template for accuracy studies, although such stringent criteria are not recommended for scattering experiments.

The final escape process in the vicinity of the standard Pythagorean configuration has also been examined [Aarseth et al., 1994b]. Based on 831 examples, the angle, $\Psi$ , between the velocity vector of the escaper and the line bisecting the binary components favoured $\Psi > 4 5 ^ { \circ }$ by a ratio of 2:1. The significance of this conclusion has been criticized [Umehara $\&$ Tanikawa, 2000]. The latter work introduced the velocity vector product

$$
\Phi _ { j k } = v _ { j } v _ { k } \sin \left( \lvert \theta _ { j } \rvert - \lvert \theta _ { k } \rvert \right) ,
$$

![](images/d616b2d6ba8c4acabf2ebd78e0e04d088d0a06fff79aa084cefccc9cba0bbb50.jpg)  
Fig. 18.1. Chaotic behaviour of outer apocentre distance. Time is measured in crossing times of the triple system.

where $\theta _ { i }$ is the angle spanned by $\mathbf { r } _ { j k }$ and $\mathbf { v } _ { i }$ . On the other hand, the corresponding radial velocity is given by

$$
U _ { j k } = v _ { k } \ \mathrm { c o s } \ \theta _ { k } - v _ { j } \ : c o s \theta _ { j } .
$$

Although the second condition of positive radial velocity agrees with the region for positive $\Phi _ { i j }$ and equal masses, the two tests are not equivalent for $v _ { j } \gg v _ { k }$ ; consequently the former does not always apply.

Actual cluster simulations deal with a wide variety of hierarchical configurations where chaos often plays an important role. It is therefore not surprising that some systems are close to the stability boundary as defined by (9.14). However, the temptation to accept a long-lived subsystem as stable even if this condition is not met must be resisted, albeit at some cost. Here we give an example that illustrates this point, taken from a realistic star cluster simulation ( $N _ { \mathrm { s } } = 8 0 0$ , $N _ { \mathrm { b } } = 2 0 0$ ). This episode began with a compact binary–binary interaction in which one of the components acquired escape energy during the first approach. The outer pericentre distance of the new triple was marginally (i.e. 3%) inside the stability value after due allowance for the inclination effect in which $\psi \simeq 1 3 0 ^ { \mathrm { o } }$ . This necessitated a lengthy integration by chain regularization until the outer small mass was eventually ejected.

Data from the initial four-body configuration was extracted and used by the stand-alone chain code for further examination with slightly smaller tolerance and the same outcome was reproduced on a comparable timescale in the absence of external perturbations. Figure 18.1 shows the apocentre distance of the outer body, evaluated near each turning point, over a time interval of about 2800 crossing times with some 500 excursions. After an irregular build-up to larger distances, the reverse process gave rise to considerable shrinkage, followed by another stage of successive energy gains, whereupon ejection took place. Although the time interval is too long to guarantee accurate solutions, the characteristic chaotic behaviour is nevertheless instructive.

The results of scattering experiments may also be used to illustrate the chaotic nature of gravitational interactions instead of obtaining cross sections. As we have seen above for the 1D case, this approach is generally based on producing phase-space maps which reveal chaotic structure. One such study [Boyd & McMillan, 1993] adopted standard selection of initial conditions for three-body scattering and used the TRIPLE code. The emphasis was on displaying maps of the entire region over which resonance can occur. Regions where simple ejection, fly-by or exchange take place are separated by so-called ‘rivers of resonance scattering’. Enlargements of such a region reveal intricate nested patterns of alternating smooth and irregular bands on decreasing scales. The existence of such subdivided bands is a hallmark of fractal structure. Moreover, in the case of equal masses, the structure within these regions is due to the existence of a constant probability of escape from the interaction region at each close approach.

In order to study long-lived systems, a novel use was made of the total kinetic energy which contains information about the internal dynamics. Thus the case of a hierarchical configuration with non-zero outer eccentricity shows this quantity varying on two time-scales. For equal masses, the two frequencies, $\omega _ { 1 }$ , $\omega _ { 2 }$ , may be recognized by transforming the sum of the two Keplerian energies into a relation of the form

$$
( 1 / 2 ) ^ { 1 / 3 } \omega _ { \mathrm { b } } ^ { 2 / 3 } + 2 ( 1 / 2 ) ^ { 1 / 3 } \omega _ { 3 } ^ { 2 / 3 } = \mathrm { c o n s t } .
$$

These frequencies can be determined accurately and the result shows a smooth variation as binding energy is transferred between the inner and outer orbit. However, there are times when the system cannot be decomposed into two separable orbits. The departures from the conservation law can be used to identify epochs when interesting non-hierarchical interactions or transitions are taking place.

The question of practical unpredictability has been addressed by examining the phase-space structure of chaotic three-body scattering [Mikkola, 1994]. The complexity of the problem was reduced by choosing initial values along curves in phase space and analysing the final binary properties. Numerical investigations with the $T R I P L E$ code showed that phase space is divided into separate zones, isolated by hyper-surfaces of parabolic disruption. Thus there are regular regions characterized by short interplay times, whereas chaotic behaviour is usually associated with long interplay times and ejections without escape. Since the discontinuous singular surfaces are very dense, a small numerical error can move the trajectory across a surface, making the outcome different and hence unpredictable. This behaviour is connected with an earlier idea that escape times are discontinuous [Szebehely, 1972].

Although the Pythagorean configurations undoubtedly display chaotic behaviour, certain regular patterns may be seen from movies. Thus in the original system with masses 3, 4 and 5, there are nearly 30 independent two-body encounters, and yet the two lightest bodies are never the closest pair until the final triple approach. There does not appear to be any fundamental reason for this curious avoidance, since other similar initial conditions produce mutual encounters between all the bodies, albeit with some tendency for the heaviest mass to control the motion.

As we have seen from many examples, numerical integrations of three mass-points readily produce chaotic orbits. However, stable few-body systems have received remarkably little attention in spite of some interesting theoretical developments. Given a hierarchical configuration, the question of stability poses a big challenge. This is particularly relevant for the treatment of weakly perturbed systems in cluster simulations, as discussed in previous chapters (cf. sections 9.5 and 15.7).

The observational search for stable hierarchies has yielded a few examples where the elements may change on relatively short time-scales. We highlight the triple system HD 109648 which reveals evidence for precession of the nodes and apsidal advance, as well as eccentricity variation over an 8-yr base line [Jha et al., 2000]. Given a period ratio of 22:1 and outer period $1 2 0 \mathrm { d }$ , this triple should be stable, with a modulation timescale $T _ { \mathrm { K o z a i } } \simeq 1 5 \mathrm { y r }$ for small outer eccentricity (cf. (15.17)). Since the inner period is only $^ \mathrm { 5 d }$ , the orbit is expected to have been circularized, yet $e _ { \mathrm { i n } } ~ \simeq ~ 0 . 0 1 1$ . This small but non-zero value appears to change in a cyclical way consistent with either a small inclination and/or strong tidal force. Direct integrations using the $T R I P L E$ code have also been made, based on the derived elements. In particular, a small relative inclination of $\psi \geq 5 ^ { \circ }$ obtained from geometrical and observational constraints was used. The results of the inner eccentricity modulations over a decade were found to be consistent with the observed variation.

In general, binaries with periods below some cutoff value that depends on stellar type are expected to be circularized [Mermilliod & Mayor, 1992; Verbunt & Phinney, 1995]. It is therefore interesting to note some evidence of significant deviation from circular motion that supports the data presented above. Thus two cluster binaries with periods of 2.4 and 4.4 d in the Hyades and M67, respectively, have eccentricities 0.057 and 0.027 [Mazeh, 1990]; moreover, a $4 . 3 \mathrm { d }$ halo binary has $e \ : = \ : 0 . 0 3 1$ . Although the circularization time is much less than the age in each case, there is additional evidence for the presence of a third companion. Once again, the relatively small eccentricities may provide a clue to the strength of the tidal dissipation which tends to have a stabilizing effect. The question of long-term stability of hierarchical stellar systems may therefore also depend on astrophysical processes such as mass transfer and tidal friction [Eggleton, Kiseleva & Hut, 1998].

![](images/74b863d1287e83158673ce53ccaa698f820a1ef6241ffa1344daf38370ed9cb3.jpg)  
Fig. 18.2. Quasi-periodic three-body system

On rare occasions even general three-body systems may exhibit regular motions. Remarkably, a sample of 5000 experiments in 2D yielded two kinds of regular orbits which were numerically stable over long times [Anosova et al., 1984]. The first was of a chain type where a central body approached the other two successively on opposite sides without the latter getting close, while in the second case all bodies made close pair-wise encounters. Figure 18.2 illustrates the orbits in the former example until the rotating pattern has precessed by about $4 5 ^ { \mathrm { { \circ } } }$ . In the absence of close triple encounters, the solution is quite accurate and displays the same pattern for much longer times.

The serendipitous discovery above shows that phase space contains hidden secrets. Another example was recently revealed by the existence proof for a periodic 2D orbit where three equal masses describe a figure eight solution [Chenciner & Montgomery, 2000]. Accurate numerical methods for finding such orbits based on minimization formulations have also been presented [Sim´o, 2001]. A variety of so-called ‘choreographic solutions’ have in fact been obtained for a range of particle numbers, including some cases without any symmetry.††

Finally, in this connection, we mention a practical algorithm for recognizing figure eight orbits with zero angular momentum [Heggie, 2000]. This scheme is based on identifying possible collinear configurations occurring in the sequence 123123123 . . ., or its reverse, where each digit denotes the middle body. Although the figure eight orbit appears special, it can be reproduced by scattering experiments in which a fourth incoming body produces two binaries, whereupon time reversal yields the desired result. Nevertheless, this new outcome of binary–binary scattering only has a low probability of occurring and hence the corresponding stability test in chain regularization is not needed.

The grand challenge of understanding the three-body problem has attracted much attention by celebrated mathematicians over the last few centuries, yet many mysteries remain. A new formalism has recently been developed from first principles for studying the energy and angular momentum exchange in hierarchical triples and scattering experiments [Mardling, 2001, 2003a,b], allowing a study of configurations with arbitrary initial conditions. The different scattering processes include fly-by, ionization, resonant capture and exchange. Moreover, stability boundaries for hierarchical systems can be determined for arbitrary masses and orbital elements and, in addition, the evolution of unstable triples may be obtained. A description of unstable behaviour is particularly useful for long-lived systems with large outer eccentricity that occur in star cluster simulations.

By analogy with the modes of oscillation of a rotating star that may be excited due to a close binary companion [Lai, 1997], the formalism introduces the concept of the modes of oscillation of a binary. The inner orbit is regarded as a pair of circular rings of material that spin in the same plane as the actual (inner) orbit. In a frame rotating with the spin frequency (i.e. the orbital frequency), the rings are stationary when the orbit is circular, but oscillate radially and azimuthally for an eccentric orbit. A related device was introduced by Gauss for the case of two planets orbiting the Sun. In this picture, the mass of the inner planet is smeared out along its orbit to form a single ring, such that the density is highest at apastron and lowest at periastron. The outer planet then responds to this static (non-oscillating) distribution of matter. This formulation predicts successfully secular evolution features such as the rate of apsidal motion of the outer orbit [Murray & Dermott, 1999].

The new formulation differs in two distinct ways from that of Gauss. First, a binary of arbitrary mass ratio is regarded as a pair of rings, and the third body responds to a radially varying distribution of matter, much like in the binary–tides problem where the second star responds to the moments of the mass distribution of the first. The other difference is that the rings interact dynamically with the outer orbit so that its normal modes of oscillation, given in terms of the mean anomaly, are excited by the outer body. Hence the rings oscillate as they exchange energy and angular momentum with the outer orbit, at all times remaining circular.

While Gauss’s formulation involves averaging over the inner orbit to predict secular evolution, the new formalism involves averaging over the inner orbit to predict dynamical evolution. In effect, the averaging procedure isolates the dynamically important frequencies.

Dynamically active triple processes generally involve significant exchange of energy and angular momentum between the inner and outer orbits in contrast to, for example, stable (non-resonant) hierarchical triples in which the semi-major axis remains secularly constant, although the eccentricity may evolve secularly through angular momentum exchange. It is this aspect that the new formalism captures, an aspect particularly important for studying stability. Previous studies of stability have generally focused on the concept of Hill stability. A system is Hill stable if no close approaches of any pair of bodies is possible [Szebehely & Zare, 1977; Gladman, 1993]. In fact this is no guarantee of stability; it is possible for the outer eccentricity effectively to random-walk its way past unity without there ever being a close encounter. This introduces the more general concept of Lagrange stability: a system is Lagrange stable if in addition it remains bound for all time. This is very much associated with the question of whether or not significant energy can be transferred between the orbits, and this in turn is associated with the existence of internal resonances.

The interactions between non-linear oscillators and their chaotic behaviour have been studied extensively as mathematical dynamical systems [Chirikov, 1979 and references therein]. A particularly useful concept for predicting the onset of chaotic behavior is that of resonance overlap [Chirikov, 1979]. In the context of the three-body problem, this was first applied by Wisdom [1980] to the restricted problem, and it is this concept that is employed in the new formalism to study stability in the general three-body problem. Here, the dominant mode excited in the inner binary by the outer body is determined and it is then treated as an oscillator interacting with a Kepler orbit (the outer orbit). If the outer orbit is eccentric, the frequencies associated with it are the orbital frequency and all integer multiples of this. Hence there is the possibility of resonance between the inner orbit and any one of these frequencies, and if any of these resonances ‘overlap’, unstable behaviour ensues.

The energy pumped into or out of the ‘oscillator’ (the dominant mode) by the outer orbit represents the dynamical activity, both in unstable bound triples and unbound scattering events. Including this energy in the description allows one to study the general problem, and it is this aspect that is absent from other descriptions of stability and scattering.

Given such an analytical description of stability and scattering, it becomes possible to devise convenient fitting formulae for use in $N$ -body simulations. These procedures are currently being formulated.

Questions concerning the stability of the Solar System have dominated the field of celestial mechanics since the days of Newton and Laplace. We consider briefly some developments involving numerical studies that are connected with chaotic motion. For a comprehensive review, see Lecar et al. [2001]. In the early days of direct $N$ -body simulations, the asteroids presented a popular subject for applications [cf. Lecar & Franklin, 1973] and the results focused the attention on chaos. Although general planetary integrations are still unable to provide observationally correct solutions for time intervals of even 100 Myr because of the short Lyapunov times, much can be learnt about the long-term behaviour.

In view of the importance of the symplectic mapping method [Wisdom & Holman, 1991] for numerical studies, it is reassuring to note general agreement with conventional integrations for the outer planets over nearly $^ 1$ Gyr. The latter results were obtained using the special-purpose Digital Orrery computer [Sussman & Wisdom, 1988] which pointed the way to later hardware developments. In a new approach, 50 000 terms of the averaged secular equations were integrated by a 12th-order Adams method over 15 Gyr after comparison with direct solutions [Laskar, 1994]. The motion of the outer planets is always very regular, whereas Mercury is more susceptible to developing chaotic orbits. A number of successive solutions were adopted for the Earth, which maximized the eccentricity of Mercury and eventually large values were reached, indicating possible escape. Subsequently, it was found that the spacing of the inner planets show evidence of chaotic wanderings [Laskar, 1997]. However, these wanderings are limited by the so-called ‘angular momentum deficit’ (AMD) which contains the contributions from non-circular and non-planar motion. A simplified model of planetary accretion also made use of the AMD conservation to constrain the evolution following collisions [Laskar, 2000]. The final distribution of semi-major axes obeyed a square root relation reminiscent of the Titus–Bode rule which was also reproduced for the $\upsilon$ Andromedae system. Meanwhile, an application of the Wisdom–Holman method to asteroid orbits, with simultaneous solutions of the variational equations, yielded longer Lyapunov times in the main asteroid belt which may account for the apparent longevity [Mikkola $\&$ Innanen, 1995].

A new long-term study of planetary orbits [Ito & Tanikawa, 2002] can be seen as a culmination of the modern approach which seeks to answer the ultimate challenge in our field. $\ddag \ddag$ Based on dedicated computations lasting several years, all the nine planets were integrated over time-spans of $\pm 4 \times 1 0 ^ { 9 }$ yr using the Wisdom–Holman [1991] method [see also Mikkola $\&$ Saha, 2003]. The main outcome of this heroic effort is that the Solar System appears to be quite stable on this time-scale and no close encounters were recorded. However, the eccentricity of Mercury tends to show large amplitude variations which may indicate the onset of chaotic motion on a somewhat longer time-scale. Since the orbital motion of the outer planets is quite regular and the total AMD is conserved, the AMD of the inner four planets is expected to be approximately constant. The $z$ -component of the normalized AMD is defined by

$$
C _ { z } = \sum _ { j = 1 } ^ { 4 } \frac { m _ { j } M _ { \odot } } { m _ { j } + M _ { \odot } } [ G ( M _ { \odot } + m _ { j } ) a _ { j } ] ^ { 1 / 2 } [ 1 - ( 1 - e _ { j } ^ { 2 } ) ^ { 1 / 2 } \cos \psi _ { j } ] .
$$

The deviations from zero are relatively small, with Mercury again showing the largest effect. The authors concluded that the main reason for the long-term stability is that the terrestrial planets have larger separations measured in terms of their mutual Hill radii as compensation for the shorter orbital periods. Hence the stronger perturbations by the outer planets are less effective in inducing chaotic features in the inner Solar System. These results also indicate that much can be learnt by studying the behaviour of the Jovian planets in isolation.

So far, this book has been exclusively concerned with topics restricted to dynamics, with emphasis on the relevant integration methods. However, it is interesting to note that such methods have found applications in other fields. One problem studied is the semi-classical quantization of the quadratic Zeeman effect in the hydrogen atom [Krantzman, Milligan & Farrelly, 1992]. KS regularization was used effectively to avoid singularities associated with the classical separatrix. Moreover, this problem is an important example of a non-integrable Hamiltonian that is chaotic in the classical limit. Another investigation of classical electron motion of two-electron atoms [Richter, Tanner & Wintgen, 1992] employed the three-body regularization of section 5.2 to calculate stability properties of periodic orbits with two degrees of freedom. These systems display an amazingly rich structure and a variety of different types of motion. In particular, the behaviour for zero angular momentum where the orbits degenerate to collinear motion exhibit Poincar´e maps analogous to the properties of the 1D systems discussed above [cf. Mikkola & Hietarinta, 1989]. Hence, in conclusion, the general theme of chaos and stability connects Newtonian dynamics with the atomic world.

# Appendix A Global regularization algorithms

A collection of the relevant formulae for Heggie’s global regularization method is given, based on the reformulation of Mikkola [1985a]. In the second section, we summarize procedures for including external perturbations for the case $N = 3$ .

# A.1 Transformations and equations of motion

We begin with the algorithm for constructing the initial values, then derive the equations of motion and finally write expressions for obtaining the physical variables. In the following we use the Lagrangian time transformation, with $g = 1 / ( T + U )$ and assume the centre-of-mass frame.

Let the coordinates and velocities be given by $\mathbf { r } _ { i } , \dot { \mathbf { r } } _ { i }$ . Define the index $k = ( i - 1 ) N - i ( i + 1 ) / 2 + j$ for $1 \leq i < j \leq N$ by adding one to $k$ when incrementing $i$ and $j$ . At the same time form the quantities

$$
\begin{array} { l } { { \bf q } _ { k } = { \bf r } _ { i } - { \bf r } _ { j } , } \\ { \quad \mathbf p _ { k } = ( m _ { i } \dot { \bf r } _ { i } - m _ { j } \dot { \bf r } _ { j } ) / N , } \\ { M _ { k } = m _ { i } m _ { j } , } \\ { a _ { i k } = 1 , \quad a _ { j k } = - 1 , } \end{array}
$$

and take the other components of $a _ { i j }$ as zero. Hence there are a total of $N ( N - 1 ) / 2$ terms $\mathbf q _ { k }$ , $\mathbf { p } _ { k }$ . We define $\mathbf { q } _ { k } = ( X , Y , Z ) ^ { \mathrm { { T } } }$ and write the standard KS transformation for $X \geq 0$ as

$$
\begin{array} { r l } & { \mathbf { Q } _ { 1 } = [ \frac { 1 } { 2 } ( q _ { k } + X ) ] ^ { 1 / 2 } , } \\ & { \mathbf { Q } _ { 2 } = \frac { 1 } { 2 } Y / Q _ { 1 } , } \\ & { \mathbf { Q } _ { 3 } = \frac { 1 } { 2 } Z / Q _ { 1 } , } \\ & { \mathbf { Q } _ { 4 } = 0 , } \end{array}
$$

otherwise we choose

$$
\begin{array} { r l } & { \mathbf { Q } _ { 2 } = [ \frac { 1 } { 2 } ( q _ { k } - X ) ] ^ { 1 / 2 } , } \\ & { \mathbf { Q } _ { 1 } = \frac { 1 } { 2 } Y / Q _ { 2 } , } \\ & { \mathbf { Q } _ { 3 } = 0 , } \\ & { \mathbf { Q } _ { 4 } = \frac { 1 } { 2 } Z / Q _ { 2 } . } \end{array}
$$

The corresponding regularized momenta are then related to the relative physical momenta, $\mathbf { p } _ { k }$ , by

$$
\mathbf { P } _ { k } = 2 \mathcal { L } _ { k } ^ { \mathrm { T } } \mathbf { p } _ { k } ,
$$

where the superscript T denotes the transpose. At this stage we also calculate $K = N ( N - 1 ) / 2$ elements of the matrix $z _ { u v }$ from

$$
T _ { u v } = { \textstyle \frac { 1 } { 2 } } \sum _ { e = 1 } ^ { N } a _ { e u } a _ { e v } / m _ { e } . ~ ( u = 1 , \ldots , K ) ~ ( v = 1 , \ldots , K )
$$

Given the KS variables $\mathbf { Q } _ { k }$ , $\mathbf { P } _ { k }$ , the respective derivatives are evaluated by the following sequential steps

$$
\begin{array} { r l } & { \mathrm { P r } - \gamma _ { \mathrm { e } } ^ { \mathrm { i } } \phi _ { \mathrm { e } } ^ { \mathrm { i } } , } \\ & { \mathrm { A } _ { \phi } - \sum _ { j } ^ { \prime } \mathrm { R } _ { 2 } \mathrm { R } _ { 3 } , } \\ & { \hat { \lambda } _ { z } - \sum _ { j } ^ { \prime } \mathrm { R } _ { 3 } , } \\ & { \hat { \lambda } _ { z } - \mathrm { i } _ { x } ^ { \prime } \mathrm { R } _ { 3 } , } \\ & { \hat { \lambda } _ { z } - \sum _ { j } ^ { \prime } \mathrm { R } _ { 3 } , } \\ & { \hat { \lambda } _ { x } ^ { \prime } - \sum _ { k \ne j } ^ { \prime } \mathrm { R } _ { 3 } , } \\ & { \hat { \lambda } _ { y } ^ { \prime } - \sum _ { j } ^ { \prime } \mathrm { R } _ { 3 } \mathrm { i } _ { y } ^ { \prime } , } \\ & { \hat { \lambda } _ { z } - \sum _ { j } ^ { \prime } \mathrm { R } _ { 3 } / Q _ { z } ^ { \dag } , } \\ & { \hat { \lambda } _ { z } ^ { \prime } - \sum _ { j } ^ { \prime } \mathrm { R } _ { 3 } / Q _ { z } ^ { \dag } , } \\ & { \hat { \lambda } _ { z } ^ { \prime } - ( \lambda _ { x } \lambda _ { x } \lambda _ { y } - \lambda _ { z } ) / 2 } \\ & { \hat { \lambda } _ { z } ^ { \prime } - ( \lambda _ { y } \lambda _ { x } ^ { \prime } \lambda _ { z } - \lambda _ { z } \lambda _ { z } ) / 2 } \\ & { \hat { \lambda } _ { z } ^ { \prime } - ( \lambda _ { x } ^ { \prime } \lambda _ { y } ^ { \prime } \lambda _ { z } - \lambda _ { z } \lambda _ { z } ) / 2 } \\ & { \hat { \lambda } _ { z } ^ { \prime } - ( \lambda _ { x } ^ { \prime } \lambda _ { y } ^ { \prime } \lambda _ { z } - \lambda _ { z } ^ { \prime } \lambda _ { z } ) / 2 } \\ & { \hat { \lambda } _ { z } ^ { \prime } - \sum _ { j } ^ { \prime } \mathrm { R } _ { z } ^ { \prime } / Q _ { z } ^ { \dag } , } \\ &  \hat { \lambda } _ { z } ^ { \prime } - \sum _ { j } ^ { \prime } \mathrm { R } _ { z } ^ { \prime } / Q _ { z } ^  \ d \end{array}
$$

Here the equation for $T _ { \mathbf { Q } _ { k } }$ contains the transpose Levi-Civita matrix with argument $\mathbf { P } _ { k }$ . Defining partial derivatives with subscripts, we write the equations of motion

$$
\begin{array} { r l } & { \mathbf { Q } _ { k } ^ { \prime } = G _ { \mathrm { T } } T _ { \mathbf { P } _ { k } } , } \\ & { \mathbf { P } _ { k } ^ { \prime } = - G _ { \mathrm { T } } T _ { \mathbf { Q } _ { k } } - G _ { \mathrm { U } } U _ { \mathbf { Q } _ { k } } , } \\ & { \quad t ^ { \prime } = 1 / L . } \end{array}
$$

With $k = k ( i , j )$ as before, the transformations to physical variables take the form

$$
\begin{array} { l } { { \displaystyle { \bf q } _ { i j } = { \bf q } _ { k } = \mathcal { L } _ { k } { \bf Q } _ { k } } , } \\ { { \displaystyle { \bf p } _ { i j } = { \bf p } _ { k } = \frac { 1 } { 2 } \mathcal { L } _ { k } { \bf P } _ { k } / Q _ { k } ^ { 2 } } , } \\ { { \displaystyle { \bf r } _ { i } = \frac { 1 } { M } \sum _ { j = i + 1 } ^ { N } m _ { j } { \bf q } _ { i j } - \frac { 1 } { M } \sum _ { j = 1 } ^ { i - 1 } m _ { j } { \bf q } _ { j i } } , } \\ { { \displaystyle \dot { \bf r } _ { i } = \frac { 1 } { m _ { i } } \sum _ { j = i + 1 } ^ { N } { \bf p } _ { i j } - \frac { 1 } { m _ { i } } \sum _ { j = 1 } ^ { i - 1 } { \bf p } _ { j i } } , } \end{array}
$$

with $M$ the total mass. In order to obtain accurate solutions, a high-order integrator such as the Bulirsch–Stoer method [1966] is recommended. As is usual in canonical theory, the differential equations to be solved are of first order.

# A.2 External perturbations

Some of the steps for including external effects in the three-body problem are outlined below. Analogous derivations for the general case $N > 3$ are given elsewhere [cf. Heggie, 1988]. Only the potential energy interaction term requires differentiation if we also introduce an equation for the energy itself. The former can be expressed in the form

$$
\mathcal { R } = - \sum _ { i = 1 } ^ { 3 } \sum _ { j = 4 } ^ { N } \frac { m _ { i } m _ { j } } { \vert \mathbf { r } _ { i } - \mathbf { r } _ { j } \vert } .
$$

By analogy with (5.30), we now obtain the desired perturbation term by partial differentiation

$$
{ \frac { \partial { \mathcal { R } } } { \partial \mathbf { Q } _ { k } } } = \sum _ { i = 1 } ^ { 3 } { \frac { \partial { \mathcal { R } } } { \partial \mathbf { r } _ { i } } } { \frac { \partial \mathbf { r } _ { i } } { \partial \mathbf { q } _ { k } } } { \frac { \partial \mathbf { q } _ { k } } { \partial \mathbf { Q } _ { k } } } .
$$

Explicit differentiation yields the perturbing force

$$
\partial { \mathcal R } / \partial { \bf r } _ { i } = - m _ { i } { \bf F } _ { i } ,
$$

where $\mathbf { F } _ { i }$ has the usual meaning. Alternatively, we can obtain the perturbation directly in the form $\partial \mathcal { R } / \partial \mathbf { q } _ { k }$ . Its evaluation is facilitated by employing the cyclic notation defined in section 5.5,

$$
{ \bf r } _ { 1 } = ( m _ { 2 } { \bf q } _ { 3 } - m _ { 3 } { \bf q } _ { 2 } ) / M + { \bf r } _ { 0 } , \qquad ( * )
$$

where $\mathbf { r } _ { 0 }$ denotes the local centre of mass and the asterisk indicates two more equations by cyclic interchange of indices. Consequently, the expressions for $\partial \mathbf { r } _ { i } / \partial \mathbf { q } _ { k }$ reduce to mass ratios. Lastly, we have

$$
\partial { \bf q } _ { k } / \partial { \bf Q } _ { k } = 2 \mathcal { L } _ { k } ^ { \mathrm { T } } ,
$$

and by combining terms we recover the full derivative expression (A.10). By analogy with the perturbed equation of motion given by (5.29), this is substituted into the differentiated form of (5.56).

The last term of the Hamiltonian (5.56) represents the total energy which is no longer constant. Accordingly, we can obtain its changing value by direct integration rather than by explicit evaluation. Employing the known equations of motion for $\dot { \mathbf { q } } _ { i }$ and $\dot { \mathbf { p } } _ { i }$ , we derive the simplified result [Heggie, 1974]

$$
\dot { E } = - \sum _ { i = 1 } ^ { 3 } \dot { \bf q } _ { i } ^ { \mathrm { T } } { \partial \mathcal { R } } / { \partial \bf q } _ { i } .
$$

Finally, we convert to regularized derivatives by introducing primes and employ the standard KS relation $\mathbf { q } _ { k } = \mathcal { L } _ { k } \mathbf { Q } _ { k }$ which, together with (4.21), simplifies to

$$
E ^ { \prime } = - 2 \sum _ { i = 1 } ^ { 3 } \mathcal { L } _ { k } \mathbf { Q } _ { k } ^ { \prime } \partial \mathcal { R } / \partial \mathbf { q } _ { i } .
$$

In conclusion, it may be remarked that the additional effort of using the global three-body method, compared with the Aarseth–Zare regularization, might be relatively modest when perturbations are included, since the similar terms $\partial \mathcal { R } / \partial \mathbf { q } _ { i }$ could well dominate the cost. It appears that the perturbed case has not been attempted in any $N$ -body simulation so far. Hence an implementation would provide a good programming exercise. However, an application to general $N$ -body systems would still require considerable decision-making. Its introduction would therefore depend on whether several simultaneous chain regularizations are developed.

# Appendix B Chain algorithms

Below we provide a practical collection of the necessary expressions for chain regularization, based closely on the improved notation [Mikkola $\&$ Aarseth, 1993].

# B.1 Transformations and switching

In the following we refer to the actual indices of the physical variables instead of those assigned while relabelling the particles. This notation facilitates the construction of a computer code. We first describe transformation to regularized variables and assume that the initial chain structure has been determined, as described in section 5.4.

Let the location of a particle with mass $m _ { j }$ be denoted by an index $I _ { j }$ , such that the actual index (or name) is also $I _ { j }$ . The c.m. and chain variables for $N$ members are then defined by

$$
\begin{array} { r l } { \mathbf { r } _ { 0 } = \displaystyle \sum _ { j = 1 } ^ { N } m _ { j } \mathbf { r } _ { j } / M , } & { } \\ { \dot { \mathbf { r } } _ { 0 } = \displaystyle \sum _ { j = 1 } ^ { N } m _ { j } \dot { \mathbf { r } } _ { j } / M , } & { } \\ { \dot { \mathbf { p } } _ { j } = m _ { j } \dot { \mathbf { r } } _ { j } / M , } & { } \\ { \dot { \mathbf { p } } _ { j } = m _ { j } ( \dot { \mathbf { r } } _ { j } - \dot { \mathbf { r } } _ { 0 } ) , \quad } & { ( j = 1 , \dots , N ) } \\ { \mathbf { W } _ { \mathbf { \Phi } } = \mathbf { - p } _ { \mathbf { 1 } } , } & { } \\ { \mathbf { W } _ { \mathbf { \Phi } } = \mathbf { W } _ { k = 1 } - \mathbf { p } _ { k } , \qquad ( k = 2 , \dots , N - 2 ) } \\ { \mathbf { W } _ { \mathbf { \Phi } \mathbf { - 1 } } = \mathbf { - p } _ { N } , } & { } \\ { \mathbf { R } _ { k } = \mathbf { r } _ { k + 1 } - \mathbf { r } _ { k } . } & { } \end{array}
$$

Note the explicit absence of the term $\mathbf { p } _ { N - 1 }$ from the chain momenta. This is connected with the c.m. condition since $\mathbf { W } _ { N - 1 }$ consists of the negative

sum of the first $N - 1$ physical momenta. Hence for $N \ = \ 3$ we have $\mathbf { W } _ { 2 } = - ( \mathbf { p _ { 1 } } + \mathbf { p _ { 2 } } )$ , whereas the two momenta are treated symmetrically in the equivalent formulation of section 5.2.

We define $\mathbf { R } _ { k } = ( X , Y , Z ) ^ { \mathrm { T } }$ , whereupon the standard KS transformation for $X \geq 0$ can be written as

$$
\begin{array} { r l } & { { \bf Q } _ { 1 } = [ \frac { 1 } { 2 } ( R + X ) ] ^ { 1 / 2 } , } \\ & { { \bf Q } _ { 2 } = \frac { 1 } { 2 } Y / Q _ { 1 } , } \\ & { { \bf Q } _ { 3 } = \frac { 1 } { 2 } Z / Q _ { 1 } , } \\ & { { \bf Q } _ { 4 } = 0 , } \end{array}
$$

otherwise we choose well-determined values by

$$
\begin{array} { r l } & { \mathbf { Q } _ { 2 } = [ \frac { 1 } { 2 } ( R - X ) ] ^ { 1 / 2 } , } \\ & { \mathbf { Q } _ { 1 } = \frac { 1 } { 2 } Y / Q _ { 2 } , } \\ & { \mathbf { Q } _ { 3 } = 0 , } \\ & { \mathbf { Q } _ { 4 } = \frac { 1 } { 2 } Z / Q _ { 2 } . } \end{array}
$$

The corresponding momenta are obtained by

$$
{ \bf P } _ { k } = 2 \mathcal { L } _ { k } ^ { \mathrm { T } } { \bf W } _ { k } . \qquad \quad ( k = 1 , \ldots , N - 1 )
$$

The transformation from $\mathbf { Q } , \mathbf { P }$ to $\mathbf { r } , \dot { \mathbf { r } }$ begins by the inverse KS mapping of chain vectors and associated momenta,

$$
\begin{array} { r l } & { \mathbf { R } _ { k } = \mathcal { L } _ { k } \mathbf { Q } _ { k } , } \\ & { \mathbf { W } _ { k } = \frac { 1 } { 2 } \mathcal { L } _ { k } \mathbf { P } _ { k } / Q _ { k } ^ { 2 } , } \\ & { \mathbf { p } _ { 1 } = - \mathbf { W } _ { 1 } , } \\ & { \mathbf { p } _ { k } = \mathbf { W } _ { k - 1 } - \mathbf { W } _ { k } , } \\ & { \mathbf { p } _ { N } = \mathbf { W } _ { N - 1 } , } \\ & { \dot { \mathbf { r } } _ { I _ { j } } = \mathbf { p } _ { j } / m _ { j } + \dot { \mathbf { r } } _ { 0 } . \qquad ( j = 1 , \dots , N ) } \end{array}
$$

To obtain the coordinates $\mathbf { r } _ { j }$ we first form coordinates ${ \bf q } _ { j }$ in a system where $\mathbf q _ { 1 } = 0$ , which are then converted to the physical coordinates. This gives rise to the expressions

$$
\begin{array} { l } { { \displaystyle { \bf q } _ { 1 } = 0 , } } \\ { { \displaystyle { \bf q } _ { j + 1 } = { \bf q } _ { j } + { \bf R } _ { j } , \qquad ( j = 1 , \ldots , N - 1 ) } } \\ { { \displaystyle { \bf q } _ { 0 } = \sum _ { j = 1 } ^ { N } m _ { j } { \bf q } _ { j } / M , } } \\ { { \displaystyle { \bf r } _ { I _ { j } } = { \bf q } _ { j } - { \bf q } _ { 0 } + { \bf r } _ { 0 } . \qquad ( j = 1 , \ldots , N ) } } \end{array}
$$

Switching becomes desirable when one of the non-chained distances would connect a dominant particle interaction. For each value of the index $\mu = 1 , \ldots , N - 1$ , we find the indices s enables us to write $k _ { 0 }$ and $k _ { 1 }$ such that $I _ { k _ { 0 } } ^ { \mathrm { o l d } } = I _ { \mu } ^ { \mathrm { n e w } }$ and $I _ { k _ { 1 } } ^ { \mathrm { o l d } } = I _ { \mu + 1 } ^ { \mathrm { n e w } }$

$$
{ \displaystyle { \bf R } _ { \mu } ^ { \mathrm { n e w } } = \sum _ { \nu = 1 } ^ { N - 1 } B _ { \mu \nu } { \bf R } _ { \nu } ^ { \mathrm { o l d } } } ,
$$

where $B _ { \mu \nu } = 1$ if ( $k _ { 1 } > \nu$ and $k _ { 0 } \le \nu$ ) and $B _ { \mu \nu } = - 1$ if ( $k _ { 1 } \leq \nu$ and $k _ { 0 } > \nu$ ), otherwise $B _ { \mu \nu } = 0$ .

To transform the chain momenta, we first obtain the physical momenta from the old chain by

$$
\begin{array} { r l } & { \mathbf { p } _ { I _ { 1 } ^ { \mathrm { o l d } } } = - \mathbf { W } _ { 1 } , } \\ & { \mathbf { p } _ { I _ { k } ^ { \mathrm { o l d } } } = \mathbf { W } _ { k - 1 } - \mathbf { W } _ { k } , } \\ & { \mathbf { p } _ { I _ { N } ^ { \mathrm { o l d } } } = \mathbf { W } _ { N - 1 } , } \end{array} \qquad \begin{array} { r l } & { ( k = 2 , \ldots , N - 1 ) } \\ & { ( k = 2 , \ldots , N - 1 ) } \end{array}
$$

and evaluate the new chain momenta with the same notation by

$$
\begin{array} { r l } & { \mathbf { W } _ { 1 } = - \mathbf { p } _ { I _ { 1 } ^ { \mathrm { n e w } } } , } \\ & { \mathbf { W } _ { k } = \mathbf { W } _ { k - 1 } - \mathbf { p } _ { I _ { k } ^ { \mathrm { n e w } } } , \qquad ( k = 2 , \ldots , N - 2 ) } \\ & { \mathbf { W } _ { N - 1 } = \mathbf { p } _ { I _ { N } ^ { \mathrm { n e w } } } . } \end{array}
$$

Now the procedure follows the established path of performing the KS transformations given above, whereupon the integration is continued.

# B.2 Evaluation of derivatives

Let us define the matrix $\mathit { T } _ { i j }$ and the mass products $M _ { k }$ , $M _ { i j }$ by

$$
\begin{array} { r c l } { { } } & { { } } & { { T _ { k k } = \frac { 1 } { 2 } ( 1 / m _ { k } + 1 / m _ { k + 1 } ) , } } \\ { { } } & { { } } & { { T _ { k k + 1 } = - 1 / m _ { k } , } } \\ { { } } & { { } } & { { M _ { k } = m _ { k } m _ { k + 1 } , } } \\ { { } } & { { } } & { { M _ { i j } = m _ { i } m _ { j } . } } \end{array}
$$

Further auxiliary variables are introduced by

$$
\begin{array} { l l } { { { \bf W } _ { k } = \frac { 1 } { 2 } { \mathcal L } _ { k } { \bf P } _ { k } / Q _ { k } ^ { 2 } , } } \\ { { { \bf A } _ { k } = \displaystyle \sum _ { i } \frac { 1 } { 2 } ( T _ { k i } + T _ { i k } ) { \bf W } _ { i } , \quad \quad } } & { { ( | i - k | \le 1 ) \quad \quad ( 1 \le i \le N - 1 ) } } \\ { { D _ { k } = { \bf A } _ { k } \cdot { \bf W } _ { k } , \quad } } & { { } } \\ { { T = \displaystyle \sum { D _ { k } } , \quad } } & { { ( 1 \le k \le N - 1 ) } } \end{array}
$$

$$
\begin{array} { r l } { { { \bf R } _ { i j } = { \bf q } _ { j } - { \bf q } _ { i } = \displaystyle \sum _ { k ^ { \prime } } { \bf R } _ { k ^ { \prime } } , } } & { { \qquad ( i \le k ^ { \prime } \le j - 1 ) } } \\ { { { \boldsymbol U } _ { n c } = \displaystyle \sum _ { k = 1 } M _ { i j } / R _ { i j } , } } & { { \qquad ( 1 \le i \le j - 2 ) } } \\ { { { \boldsymbol U } = \displaystyle \sum _ { k = 1 } ^ { N - 1 } M _ { k } / R _ { k } + U _ { n c } , } } & { { } } \\ { { { \boldsymbol g } = 1 / ( T + U ) . } } & { { } } \end{array}
$$

When calculating the vectors ${ \bf R } _ { i j }$ above, the difference form is generally more efficient, but the summation form should be used if there are only two terms in the sum; this avoids some round-off problems. We express partial derivatives with subscripts and obtain

$$
\begin{array}{c} \begin{array} { c l } { { } } & { { T _ { \mathbf { P } _ { k } } = \mathcal { L } _ { k } ^ { \mathrm { T } } \mathbf { A } _ { k } / Q _ { k } ^ { 2 } , } } \\ { { } } & { { \begin{array} { l } { { \mathbf { A } _ { k } ^ { * } = \left( A _ { 1 } , A _ { 2 } , A _ { 3 } , - A _ { 4 } \right) _ { k } ^ { \mathrm { T } } , } } \\ { { T _ { \mathbf { Q } _ { k } } = \left[ \mathcal { L } ( \mathbf { P } _ { k } ) ^ { \mathrm { T } } { \mathbf { A } _ { k } ^ { * } } - 4 D _ { k } \mathbf { Q } _ { k } \right] / Q _ { k } ^ { 2 } , } } \end{array} } } \\ { { } } & { { U _ { n c \mathbf { R } _ { k } } = - \sum M _ { i j } \mathbf { R } _ { i j } / R _ { i j } ^ { 3 } , \qquad ( i \leq k \leq j - 1 ) } } \\ { { } } & { { U _ { n c \mathbf { Q } _ { k } } = 2 \mathcal { L } _ { k } ^ { \mathrm { T } } U _ { n c \mathbf { R } _ { k } } , } } \\ { { } } & { { U _ { \mathbf { Q } _ { k } } = - 2 M _ { k } \mathbf { Q } _ { k } / Q _ { k } ^ { 4 } + U _ { n c \mathbf { Q } _ { k } } . } } \end{array}  \end{array}
$$

Here the third equation (B.12) contains the transpose Levi-Civita matrix with argument $\mathbf { P } _ { k }$ .

If perturbations are present, the physical coordinates (and velocities if needed) are evaluated according to the transformation formulae given above, whereupon the external acceleration, $\mathbf { F } _ { j }$ , acting on each particle can be calculated. Since these quantities appear as tidal terms, we first define the c.m. acceleration by

$$
{ \bf F } _ { 0 } = \sum _ { j = 1 } ^ { N } m _ { j } { \bf F } _ { j } / M .
$$

Given the perturbative contributions

$$
\begin{array} { r l } & { \quad \delta \dot { \mathbf { p } } _ { j } = m _ { j } ( \mathbf { F } _ { j } - \mathbf { F } _ { 0 } ) , \qquad ( j = 1 , \dots , N ) } \\ & { \delta \dot { \mathbf { W } } _ { 1 } = - \delta \dot { \mathbf { p } } _ { 1 } , } \\ & { \delta \dot { \mathbf { W } } _ { k } = \delta \dot { \mathbf { W } } _ { k - 1 } - \delta \dot { \mathbf { p } } _ { k } , \qquad ( k = 2 , \dots , N - 2 ) } \\ & { \delta \dot { \mathbf { W } } _ { N - 1 } = \delta \mathbf { p } _ { N } , } \\ & { \delta \mathbf { P } _ { k } ^ { \prime } = 2 g \mathcal { L } _ { k } ^ { \mathrm { T } } \delta \dot { \mathbf { W } } _ { k } , } \end{array}
$$

the equations of motion for the KS variables are obtained by

$$
H = T - U ,
$$

$$
\begin{array} { r l } & { \Gamma = g ( H - E _ { 0 } ) , } \\ & { \Gamma _ { \mathrm { T } } = ( 1 - \Gamma ) g , } \\ & { \Gamma _ { \mathrm { U } } = - ( 1 + \Gamma ) g , } \\ & { \Gamma _ { \mathbf { P } _ { k } } = \Gamma _ { \mathrm { T } } T _ { \mathbf { P } _ { k } } , } \\ & { \Gamma _ { \mathbf { Q } _ { k } } = \Gamma _ { \mathrm { T } } T _ { \mathbf { Q } _ { k } } + \Gamma _ { \mathrm { U } } U _ { \mathbf { Q } _ { k } } , } \\ & { \mathbf { P } _ { k } ^ { \prime } = - \Gamma _ { \mathbf { Q } _ { k } } + \delta \mathbf { P } _ { k } ^ { \prime } , } \\ & { \mathbf { Q } _ { k } ^ { \prime } = \Gamma _ { \mathbf { P } _ { k } } . } \end{array}
$$

The c.m. coordinates and velocities may be advanced by standard integration according to

$$
\begin{array} { r } { d { \bf v } _ { 0 } / d \tau = g { \bf F } _ { 0 } , } \\ { d { \bf r } _ { 0 } / d \tau = g { \bf v } _ { 0 } , } \end{array}
$$

or in the more usual way taking derivatives with respect to the physical time, $t$ , by omitting $g$ .

Finally, we need the rates of change for the internal energy and time. The former may be derived in analogy with the two-body energy equation (4.38) and also with the expression (5.37) of the Aarseth–Zare [1974] three-body regularization. Hence with the last equation (B.14), the desired equations take the form

$$
\begin{array} { r c l } { { } } & { { } } & { { E ^ { \prime } = 2 \displaystyle \sum _ { k = 1 } ^ { N - 1 } \mathbf { Q } _ { k } ^ { \prime \mathrm { T } } { \mathcal L } _ { k } ^ { \mathrm { T } } \delta \dot { \mathbf { W } } _ { k } , } } \\ { { } } & { { } } & { { t ^ { \prime } = g . } } \end{array}
$$

We remark that because tidal effects enter the energy equation, relatively few perturbers may need to be considered. Still, the perturbed treatment can be quite time-consuming when employing a high-order integrator and only compact subsystems are therefore suitable for special study since external effects are included out to a distance $\simeq \lambda R _ { \mathrm { g r a v } }$ .

# B.3 Errata

It has been pointed out [Orlov, private communication, 1998] that the original chain paper [Mikkola & Aarseth, 1990] contains some errors in the explicit expressions for the regularized derivatives, whereas the Hamiltonian itself is correct. The corrections are as follows: (i) the terms $\mathbf { B } _ { 1 } \cdot \mathbf { B } _ { 2 }$ in (45) and $\mathbf { B } _ { 3 } \cdot \mathbf { B } _ { 2 }$ in (47) should be interchanged; (ii) a factor of 2 is missing from the term $R _ { 1 } R _ { 2 } R _ { 3 }$ in (45), (46) and (47). This formulation has mostly been superseded by the 1993 version but the corresponding code is free from these errors.

# Appendix C Higher-order systems

# C.1 Introduction

We describe some relevant algorithms for initializing and terminating higher-order systems which are selected for the merger treatment discussed in chapter 11. Such configurations may consist of a single particle or binary in bound orbit around an existing triple or quadruple, or be composed of two stable triples. There are some significant differences from the standard case, the main one being that the KS solution of the binary is not terminated at the initialization. In other words, the complexity of the structure is increased, and the whole process is reminiscent of molecular chemistry. However, once formed as a KS solution, the new hierarchy needs to be restored to its original constituents at the termination which is usually triggered by large perturbations or mass loss. Special procedures are also required for removing all the relevant components of escaping hierarchies, and here we include merged triples and quadruples since the treatment is similar to that for higher-order systems.

# C.2 Initialization

Consider an existing hierarchy of arbitrary multiplicity and mass, $m _ { i }$ , which is to be merged with the mass-point $m _ { j }$ , representing any object in the form of a single particle or even another hierarchy. Again we adopt the convention of denoting the component masses of a KS pair by $m _ { k }$ and $m _ { l }$ , respectively. Some of the essential steps are listed in Algorithm C.1.

Nearly all of these steps also appear in the standard case and therefore do not require comment. We note one important difference here, in that there is no termination of the KS solution. Hence the new c.m. particle occupies the same position in the general tables as the original primary, assuming there has been no switching. Moreover, the merger table contains four locations for saving component masses, in case the outer member also represents a KS solution which may be standard or hierarchical. On the other hand, there is only one array entry containing KS quantities for each merger. Hence any secondary KS solution needs to be defined as a ghost pair, with zero component masses and perturber membership, as well as a large value of $t _ { 0 }$ . In order to distinguish between different levels of a hierarchy, we use the convention that the c.m. particle is assigned a name $\mathcal { N } _ { \mathrm { c m } }$ which is effectively $- 2 N _ { 0 }$ smaller than the previous one. Thus the initial particle number, $N _ { 0 }$ , is used as a fixed reference number, such that the corresponding names of single particles can at most reach this value. This simple device allows an arbitrary number of hierarchical levels referring to the same system as it increases in complexity.

Algorithm C.1. Initialization of higher-order system.   

<table><tr><td>1</td><td>Ensure that the primary binary is a hierarchy</td></tr><tr><td>2</td><td>Save the component masses and neighbour or perturber list</td></tr><tr><td>3</td><td>Copy the basic KS elements of the primary binary</td></tr><tr><td>4</td><td>Obtain potential energy of primary components and neighbours</td></tr><tr><td>5</td><td>Retain current values R,R of the primary components</td></tr><tr><td>6</td><td>Evaluate tidal correction for primary mass mi and neighbours</td></tr><tr><td>7</td><td>Set initial conditions for the c.m.body by mcm = mi + mj</td></tr><tr><td>8</td><td>Form basic KS quantities for the new outer binary mi and mj</td></tr><tr><td>9</td><td>Define initial conditions for ghost KS if required [case j &gt; N]</td></tr><tr><td>10</td><td>Create ghost particle ml = O with large values of ro,r and to</td></tr><tr><td>11</td><td>Remove the ghost from all neighbour or perturber lists</td></tr><tr><td>12</td><td>Initialize the c.m.and KS polynomials for the binary</td></tr><tr><td>13</td><td>Record the ghost name for identification at termination</td></tr><tr><td>14</td><td>Specify negative c.m. name for the decision-making</td></tr><tr><td>15</td><td>Update Emerge by the old binding energy and tidal correction</td></tr></table>

# C.3 Termination

At some stage, the higher-order hierarchy discussed above may cease to satisfy one of the stability conditions, whether it be increased outer eccentricity or large perturbation. Algorithm C.2 lists the steps involved in restoring the present configuration to its original state.

Again most of the listed steps are similar to the standard case. Note that the existing c.m. location (but not its value) is also used for the new inner binary, which is initialized in the standard way. The corresponding KS solution is also initialized after forming the appropriate perturber list. One new feature is the re-evaluation of the stability parameter (9.14), together with the basic inclination modification. This is achieved by obtaining the inner semi-major axis with the specified merger index and the outer twobody elements in the standard way, whereas the inclination is determined from the saved relative coordinates and velocities together with those of the c.m. and outer component. Finally, regarding step 18, care is needed to retain any inner members of hierarchies that would otherwise appear to be associated with escapers; i.e. those for which the saved c.m. name equals $2 n N _ { 0 } + \mathcal { N } _ { \mathrm { c m } }$ , where $n = 0 , 1 , 2 , \ldots$ denotes the possible levels and $ { \mathcal { N } } _ { \mathrm { c m } } < 0$ represents the actual c.m. name.

Algorithm C.2. Termination of higher-order system.   

<table><tr><td>1 2 3 4 5 6 8 9 10 11</td><td>Locate the current index in the merger table Save the neighbour or perturber list for corrections Predict the c.m.motion to highest order Define mass, coordinates and velocity for the new c.m. Add the old outer component to the perturber list Obtain the potential energy of inner binary and neighbours Identify the location, j, of the corresponding ghost particle Set initial conditions for ghost and new inner c.m. Restore the basic quantities of the primary components Copy the saved KS variables from the merger table Form new force polynomials for the old outer component 12 Initialize the c.m.polynomials and corresponding KS 13 Find the merger index for the next hierarchical level 14 Re-evaluate the stability parameter, Rput, including inclination 15 Update the original name of the hierarchy by adding 2No 16 Perform perturbed initialization of any outer binary [case j &gt; N] Subtract new binding energy and add tidal correction to Emerge 17 18 Compress the merger table, including any escaped hierarchies</td></tr></table>

# C.4 Escape of hierarchies

It is not uncommon for hierarchical systems to acquire escape velocity and be ejected from the cluster. This requires special treatment of the data structure since removal of only the active binary itself would leave single ghost particles and even massless binaries as cluster members. Hierarchies of any order are identified by a negative c.m. name, and it is therefore natural to discuss such systems together.

Let us first consider the case of a stable triple that satisfies the standard escape criterion for the associated c.m. particle, i. After the active KS binary elements and c.m. variables have been updated in the usual way, we determine the merger index using the c.m. name. The total energy, $E$ , and merger energy, $E _ { \mathrm { m e r g e } }$ , are updated by subtracting the inner binding energy, $\mu _ { \mathrm { k l } } h$ , where the latter quantities are obtained from the merger table. This enables the global index of the corresponding ghost particle to be identified by comparing it with the saved ghost name, whereupon the large value of the $x$ -coordinate is reduced to facilitate escape removal. Accordingly, this should be a single particle with zero mass which can be removed in the usual way together with reducing $N$ and $N _ { \mathrm { t o t } }$ . Again all the relevant lists must be updated, but only to the extent of reducing any larger indices since the ghost particle itself should not be a member.

An escaping quadruple is distinguished by the second or outer component being a c.m. particle; hence we have $\mathcal { N } _ { 2 p } > N _ { 0 }$ , where the pair index is given by $p = i - N$ . First the KS index of the ghost binary is determined by comparing the relevant names with $\mathcal { N } _ { 2 p }$ , since the second component is in fact another binary c.m. The ghost pair index, $q$ (say), then specifies the corresponding ghost c.m. particle as $i _ { q } = N + q$ , which must also be removed. The index of the latter is obtained by comparing the relevant names with the corresponding one for $i _ { q }$ . Again the updating procedure above is carried out, whereby the present KS and corresponding c.m. variables are updated. At this stage we correct the energies $E$ and $E _ { \mathrm { m e r g e } }$ by subtracting the original ghost contribution since the masses and specific binding energy are known if due allowance is made for table updating (i.e. $q > p$ ). At the next sequential search, an activated value of $i _ { q }$ is used to identify the necessary ghost binary by employing the specified name. Removal of the corresponding components can now be performed in the usual way, provided the large $x$ -coordinate of the ghost c.m. has been re-assigned an intermediate value which ensures escape.

It is also possible to envisage higher-order systems escaping. Although this is extremely rare, examples of ejected quintuplets have been noted for realistic populations. The above escape algorithm has been generalized to include one more hierarchical level where the outermost component may be a single particle or another binary. Note that the energy correction procedure now needs to account for the interaction between the two inner levels, as well as that of the outer level. Consequently, a successful update should reduce $E _ { \mathrm { m e r g e } }$ to the value given by any remaining hierarchies (apart from small tidal corrections) and remove all the relevant ghost members. For this purpose we introduce a notation where the innermost binary is said to be ‘hierarchical’ and any other binary (excluding the current KS pair) is denoted as a ‘quadruple’, although such a usage is only intended to be descriptive. Accordingly, an escaping quintuplet of the type $[ [ B , S ] , B ]$ will be dissected into four different configurations, where the outermost ghost binary is called a quadruple.

# Appendix D Practical algorithms

In the following we give some useful algorithms to assist in the construction of codes or explain more fully the present implementations.

# D.1 Maxwellian distribution

A Maxwellian velocity distribution is often used for generating initial conditions. This is specifically needed for the kick velocities, as described in section 15.5. We adopt an elegant method due to H´enon [Heggie, private communication, 1997]. It is based on a pair-wise procedure as follows. First select two random numbers, $X _ { 1 } , X _ { 2 }$ , and form the quantities

$$
\begin{array} { l } { { S = \sigma [ - 2 \ln ( 1 - X _ { 1 } ) ] , } } \\ { { \theta = 2 \pi X _ { 2 } , } } \end{array}
$$

where $\sigma$ is the velocity dispersion in 1D. The two corresponding velocity components are then given by $v _ { x } = S \cos \theta$ and $v _ { y } = S \sin \theta$ . For a 3D distribution we perform the same procedure a second time and choose $v _ { z } = S \cos { \theta }$ .

# D.2 Ghost particles

The general problem of recovering the actual mass, coordinates and velocity of a ghost particle is fairly simple for a triple system. However, quadruples also occur and the procedure is now more involved. Consequently, the general case is presented here, where only the first part is relevant for triples. Thus a quadruple system is defined by ${ \mathcal N } _ { j } > { \mathcal N } _ { 0 }$ for ghost particle $j$ . Algorithm D.1 is needed if we are considering a c.m. particle with index $i > N$ , mass $m _ { i } > 0$ , name $\mathcal { N } _ { i } < 0$ and wish to obtain global quantities for any ghost components. The two mass components of the active KS solution are denoted by $m , m , m _ { l }$ as usual.

Algorithm D.1. Identification of ghost particles.   

<table><tr><td>1</td><td> Locate the index p in the merger table using Nmerge = Ni</td></tr><tr><td>2</td><td>Determine the global index j of the ghost by Nj = Nghost</td></tr><tr><td></td><td>Copy component masses from m1,m2 of the merger table</td></tr><tr><td></td><td>Form r,r for binary components from mk and old R1,R1</td></tr><tr><td></td><td>Obtain the c.m. index, q, from Nq = Nj [case Nj &gt; No]</td></tr><tr><td></td><td>Get the component masses from mg,m4 of merger index p</td></tr><tr><td></td><td>Transform U,U&#x27; of any ghost binary pair q-N to R2,R2</td></tr><tr><td>8</td><td>Derive global r,r for components using ml and R2,R2</td></tr></table>

The merger table holds the array $\{ m _ { j } \}$ for saving the masses of the first and any second binary components. However, only the relative quantities ${ \bf R } _ { 1 } , \dot { \bf R } _ { 1 }$ and corresponding KS elements, including $h$ , of the inner binary are recorded in the table since any second binary is preserved as a ghost. In addition, the table contains the names of the original c.m. as well as the ghost. Parts of this algorithm are required for at least six different purposes in the codes NBODY 4 and $N B O D Y 6$ .

# D.3 KS procedures for averaging

A variety of tasks need to be carried out during the averaging of hierarchical systems. Let us concentrate on those aspects that are connected with KS regularization. Given the appropriate merger index, the current values of the relative coordinates and velocity, $\mathbf { R } , \mathbf { V }$ , are obtained by KS transformations, whereupon the Runge–Lenz and angular momentum vectors are constructed.

Following evaluation of $e _ { \mathrm { m a x } }$ and other quantities, together with timestep selection, the next integration interval is carried out and new values of $\mathbf { R } , \mathbf { V }$ are determined from the orbital elements. Transformation to the corresponding KS variables now takes place (cf. (4.32) and (4.36)) and the physical values are recorded. The binding energy, $h$ , is also an important quantity and is evaluated via the semi-major axis in terms of the specific angular momentum $\mathbf { j }$ , binary mass $m _ { \mathrm { b } }$ and eccentricity,

$$
a = | \mathbf { j } | ^ { 2 } / m _ { \mathrm { b } } ( 1 - | \mathbf { e } | ^ { 2 } ) .
$$

Finally, any change in energy given by $\mu ( h - h _ { 0 } )$ is added to the merger energy, $E _ { \mathrm { m e r g e } }$ , and subtracted from $E _ { \mathrm { c o l l } }$ . Although there is no net change in the total energy budget, the corrected quantities will now be consistent at termination.

# D.4 Determination of pericentre or apocentre

We now describe procedures for specifying KS variables at the pericentre or apocentre position. This is needed for several purposes, such as during tidal interactions or collisions. Thus unperturbed binaries are defined at the first point past apocentre, whereas the energy change in tidal interactions are implemented at pericentre. To facilitate decision-making, the two-body separation is compared with the semi-major axis and the sign of the radial velocity, $t ^ { \prime \prime } = R ^ { \prime }$ , defines approach or recession.

By combining two algorithms, we can obtain any desired transformation. Thus the case of increasing the orbital phase by an angle $\theta$ yields the new values [Stiefel $\&$ Scheifele, 1971]

$$
\begin{array} { r } { \mathbf { U } = \mathbf { U } _ { 0 } \cos \theta + \mathbf { U } _ { 0 } ^ { \prime } \sin \theta / \nu , } \\ { \mathbf { U } ^ { \prime } = \mathbf { U } _ { 0 } ^ { \prime } \cos \theta - \mathbf { U } _ { 0 } \sin \theta \nu , } \end{array}
$$

where $\nu = ( \textstyle { \frac { 1 } { 2 } } | h | ) ^ { 1 / 2 }$ is the regularized orbital frequency. This procedure assumes unperturbed motion and is used frequently for reflection by an angle $\theta = \pi / 2$ which corresponds to half a physical period.

In order to consider an arbitrary orbital phase, a second algorithm is needed which should include integration for perturbed motion. We distinguish between near-collision, elliptic or hyperbolic cases and evaluate the pericentre time from an expansion or the two forms of Kepler’s equation, respectively [Mikkola, private communication, 1991]. If the orbit is perturbed and $R > a$ , we first perform a reflection by $\pi / 2$ , followed by integration back to the pericentre. Treating this as a provisional solution, improved values are determined by the inverted relations

$$
\begin{array} { r l } & { \mathbf { U } = \tilde { \mathbf { U } } x _ { \mathrm { c } } - \tilde { \mathbf { U } } ^ { \prime } y _ { \mathrm { s } } , } \\ & { \mathbf { U } ^ { \prime } = \tilde { \mathbf { U } } ^ { \prime } x _ { \mathrm { c } } + \frac { 1 } { 4 } \tilde { \mathbf { U } } y _ { \mathrm { s } } m _ { \mathrm { b } } / a , } \end{array}
$$

since $\mathbf { U } ^ { \prime \prime } = - m _ { \mathrm { b } } \mathbf { U } / 4 a$ . If $R < a$ , we adopt $\begin{array} { r } { x _ { \mathrm { c } } = [ \frac { 1 } { 2 } + \frac { 1 } { 2 } ( 1 - R / a ) / e ] ^ { 1 / 2 } } \end{array}$ and $y _ { \mathrm { s } } = t ^ { \prime \prime } / e m _ { \mathrm { b } } x _ { \mathrm { c } }$ . The latter expressions are derived from $\cos ( \theta / 2 )$ and $\sin ( \theta / 2 )$ by inverting (D.3), with $R = a ( 1 - e \cos \theta )$ , Kepler’s equation and $\theta$ half the eccentric anomaly. However, these coefficients are not well behaved near the apocentre since $x _ { \mathrm { c } } \  \ 0$ and alternative expressions should then be used [Mikkola, private communication, 1997]. From the relation $\xi ^ { 2 } + \psi ^ { 2 } / a = e ^ { 2 }$ , with $\xi = 1 - R / a$ and $\psi = t ^ { \prime \prime } / m _ { \mathrm { b } } ^ { 1 / 2 }$ , we have $\xi / e = - ( 1 - \psi ^ { 2 } / a e ^ { 2 } ) ^ { 1 / 2 }$ if $\xi < 0$ . After some manipulation we obtain

$$
\begin{array} { l } { { x _ { \mathrm { c } } = \displaystyle \frac { \psi } { e a ^ { 1 / 2 } ( 2 - 2 \xi / e ) ^ { 1 / 2 } } , } } \\ { { y _ { \mathrm { s } } = [ \displaystyle \frac { a } { m _ { \mathrm { b } } } ( 2 - 2 \xi / e ) ] ^ { 1 / 2 } , } } \end{array}
$$

where $- y _ { \mathrm { s } }$ should be chosen if $\psi < 0$ .

# D.5 Partial unperturbed reflection

Highly eccentric orbits treated by KS regularization are characterized by small perturbations in the inner part. Hence it might be of interest to assume unperturbed motion and perform a partial reflection, provided the relative perturbation is sufficiently small. Accordingly, we give an algorithm for achieving this task.∗

Algorithm D.2. Partial two-body reflection.   

<table><tr><td>1 2 3</td><td>Determine osculating elements α and e Specify the total reflection time, tref,by Kepler&#x27;s equation Convert to regularized time units,δT 4 Skip reflection near pericentre if δτ&lt;4△T 5 Predict c.m.and obtain coordinates of the components 6 Generate reflected solutions of U and U&#x27; by (D.4)</td></tr></table>

Using $\xi$ and $\psi$ from the previous section, the total reflection time is obtained from Kepler’s equation, which gives

$$
t _ { \mathrm { r e f } } = 2 ( a ^ { 3 } / m _ { \mathrm { b } } ) ^ { 1 / 2 } ( \theta - | \psi | / m _ { \mathrm { b } } ^ { 1 / 2 } ) ,
$$

where $\theta$ is the eccentric anomaly in $[ 0 , \pi ]$ . The corresponding regularized time interval is obtained from the differential expression [Baumgarte $\&$ Stiefel, 1974]

$$
\delta \tau = - ( 2 h t _ { \mathrm { r e f } } - \Delta t ^ { \prime \prime } ) / m _ { \mathrm { b } } ,
$$

with $\Delta t ^ { \prime \prime } = t _ { 1 } ^ { \prime \prime } - t _ { 0 } ^ { \prime \prime } = - 2 t _ { 0 } ^ { \prime \prime }$ by symmetry (cf. (9.27)). Here we adopt simplified coefficients for the transformations (D.4), with $x _ { \mathrm { c } } = \xi / e$ and $y _ { \mathrm { s } } = 2 \psi / e m _ { \mathrm { b } } ^ { 1 / 2 }$ . Thus the full eccentric anomaly is used (instead of half) because of the time derivative $t ^ { \prime } = { \bf U } \cdot { \bf U }$ , and the squaring implies doubling of angles. Since unperturbed motion is defined, the new KS polynomials will be initialized at the next updating time, $t + t _ { \mathrm { r e f } }$ . Finally, the c.m. velocity is modified to compensate for the small tidal energy change, with the correction factor

$$
C = ( 1 + 2 \Delta \Phi / m _ { \mathrm { b } } v _ { \mathrm { c m } } ^ { 2 } ) ^ { 1 / 2 } ,
$$

which facilitates formal energy conservation (cf. Algorithm 12.1).

# Appendix E KS procedures with GRAPE

When using HARP or GRAPE, force calculations involving a perturbed c.m. body require modification because the summation is performed over all interactions in the point-mass approximation. Thus in order to obtain the correct c.m. force given by (8.57), we need to perform certain corrections, and the same principle applies to a single particle in the neighbourhood of a c.m. body or composite particle. A description of the relevant procedures is contained in the sections below.

HARP holds the quantities ${ \bf r } _ { 0 } , \dot { \bf r } _ { 0 } , { \bf F } _ { 0 } , \dot { \bf F } _ { 0 } , t _ { 0 }$ (GRAPE has also $\ddot { \mathbf { F } }$ ) for all single particles and c.m. bodies, and all current values of $\mathbf { r } , \dot { \mathbf { r } }$ are predicted by the hardware at each block-step before the force is evaluated. To facilitate decision-making, a list of perturbed KS solutions is maintained and updated at the end of a KS cycle if the status has changed. Coordinates and velocities of all the KS components are predicted on the host during a block-step but some are done at no cost while HARP is busy.

# E.1 Single particles

The force on a single particle, $i$ , exerted by a nearby c.m. body of mass $m _ { \mathrm { b } } = m _ { k } + m _ { l }$ is obtained by vector summation over both components. Thus if the c.m. approximation is not satisfied, the force is modified by

$$
\tilde { \mathbf { F } } _ { i } = \mathbf { F } _ { i } + \frac { m _ { \mathrm { b } } ( \mathbf { r } _ { i } - \mathbf { r } _ { \mathrm { c m } } ) } { | \mathbf { r } _ { i } - \mathbf { r } _ { \mathrm { c m } } | ^ { 3 } } - \frac { m _ { k } ( \mathbf { r } _ { i } - \mathbf { r } _ { k } ) } { | \mathbf { r } _ { i } - \mathbf { r } _ { k } | ^ { 3 } } - \frac { m _ { l } ( \mathbf { r } _ { i } - \mathbf { r } _ { l } ) } { | \mathbf { r } _ { i } - \mathbf { r } _ { l } | ^ { 3 } } ,
$$

otherwise no correction is made. A similar procedure is carried out for $\dot { \mathbf { F } } _ { i }$ and any other perturbed c.m. bodies are treated in an analogous way.

Likewise, a differential force correction is made on the rare occasions when chain regularization is used. The same principle as used above applies with respect to the chain perturber list or the chain c.m. itself, which is distinguished by zero name.

# E.2 Regularized KS pairs

The force on a c.m. particle is given by (8.57), except that the c.m. approximation is used when appropriate. Thus in the case of unperturbed two-body motion, the correction procedure is the same as for a single particle. Since $i > N$ here, the sequential perturber lists of active KS solutions are searched backwards.

The case of perturbed two-body motion is more complicated but the principle is the same. Each member, $j$ , of the perturber list is considered in turn. If $j \leq N$ and $r _ { \mathrm { i j } } < \lambda R$ , the HARP contribution to the force and its derivative is first subtracted. This is followed by prediction of coordinates and velocity∗ before the individual interaction terms are evaluated.

In the case $j > N$ , we need to check two c.m. approximations and obtain the appropriate force terms if required. For example, a binary may have small size such that the c.m. approximation with respect to another binary is satisfied but the reverse may not be true. When all the perturbers have been considered, the new component forces and first derivatives are combined vectorially according to (8.57) and its derivative.

The above procedure is less cumbersome than an earlier formulation based on creating a mask and sending zero masses of relevant perturbers and active KS solutions to HARP before the force evaluation. This was followed by addition of the remaining contributions on the host. Finally, the proper perturber masses were restored on HARP. With some effort, an arbitrary number of active KS solutions were treated together at the same time. This scheme was used successfully by NBODY 4 for some years until the present procedure was implemented (end of 1998).

Unfortunately, the gain in efficiency of the new scheme is made at the expense of accuracy. Thus the numerically inelegant practice of subtracting previously added terms also suffers from the fact that the precision on HARP is different from the host [Makino et al., 1997]. This is a design feature to optimize the performance and especially the first derivative is less accurate. However, the force errors are still sufficiently small to be of no practical significance in most cases. A test calculation with $N = 5 0 0 0$ showed typical relative force errors of $1 \times 1 0 ^ { - 7 }$ when compared with evaluation on the host, whereas the corresponding errors in the force derivatives were about $4 \times 1 0 ^ { - 6 }$ . Similar errors are also present when using GRAPE-6 for a static configuration. Note, however, that predictions to order $\ddot { \mathbf { F } }$ are only performed on the hardware in the latter case. Small additional errors are therefore introduced when making corrections during actual calculations. To compensate, explicit force summation is performed on the host if the first derivative is very large during polynomial initialization.

# Appendix F Alternative simulation method

Realistic $N$ -body simulations of star cluster evolution require a substantial programming effort. Since it takes time to develop suitable software, published descriptions tend to lag behind or be non-existent. However, one large team effort has reached a degree of development that merits detailed comments, especially since many results have been described in this book. In the following we highlight some aspects relating to the integration method as well as the treatment of stellar evolution, based on one available source of information [Portegies Zwart et al., 2001].

# F.1 $N$ -body treatment

The kira integrator∗ advances the particle motions according to the standard Hermite method [Makino, 1991a] using hierarchical (or quantized) time-steps [McMillan, 1986]. An efficient scheme was realized with the construction of the high-precision GRAPE computers which calculate the force and force derivative and also include predictions on the hardware.

One special feature here is the use of hierarchical Jacobi coordinates which is reminiscent of an earlier binary tree formulation [Jernigan & Porter, 1989]. This representation is equivalent to the data structure used in KS and chain regularization. Increased numerical accuracy is achieved by evaluating nearby contributions on the host, whereas the traditional brute force way involves the subtraction of two larger distances. On the other hand, binaries and multiple close encounters are not studied by regularization methods which also employ local coordinates. Hence direct integration of binaries requires significantly shorter time-steps in order to maintain adequate accuracy even for circular orbits. In compensation, direct integration offers advantages of simplicity.

As in the KS formulation, unperturbed binaries are treated in the c.m. approximation, whereas weak perturbations are included by a slowdown procedure (cf. section 5.8). Large numerical terms are avoided at small pericentre distances by the adoption of partial unperturbed motion (cf. (D.5)). On the other hand, long-lived stable hierarchies are only defined by means of the perturbations. Although the kira scheme exploits the GRAPE facility to full advantage, the lack of regular solutions for studying strong interactions may be a cause for concern. This situation is exemplified by the so-called ‘terrible triples’ which must be integrated over many inner orbits with small time-steps when the stability condition is not satisfied. $^ \dagger$ So far simulations of clusters containing primordial binaries have been discussed for $N _ { \mathrm { s } } = 1 \mathrm { K }$ single stars and $5 0 \%$ binaries.

# F.2 Stellar evolution

Single star and binary evolution are handled by the SeBa module, which is also part of $S T A R L A B$ . The treatment of single stars is currently based on standard fitting functions for solar metallicities [cf. Eggleton et al., 1989; Tout et al., 1997]. Further prescriptions for the core mass and mass loss by stellar winds have been added [Portegies Zwart & Verbunt, 1996]. A randomized velocity kick [Hartman, 1997] is assigned when stars in the initial range $8 – 2 5 M _ { \odot }$ become neutron stars. An upper limit of $1 0 0 M _ { \odot }$ is assumed for the IMF, with the heaviest stars losing mass rapidly before becoming Wolf–Rayet stars, which eventually form black holes.

An extensive network of processes must be considered when binaries are included [Portegies Zwart, 1996]. The look-up interval is $1 \%$ of the typical evolution time for each stage in the HR diagram, with further reductions during Roche-lobe mass transfer. Sequential circularization without synchronizing spin effects is implemented if $5 r _ { 1 } ^ { * } > a ( 1 - e )$ , with $r _ { 1 } ^ { \ast }$ the largest stellar radius (cf. (11.34)).‡ The angular momentum loss associated with stellar winds is also modelled, as is gravitational radiation for compact stars in short-period orbits. Unstable mass transfer is implemented in the standard way, including prescriptions for the spiral-in process when the envelope is ejected [Webbink, 1984]. Again, stable mass transfer is treated on different time-scales, where the details depend on the period and evolutionary state of the components.

Collisions are implemented when the stellar radii overlap, with coalescence due to mass transfer or common-envelope phases, followed by system mass loss. Finally, the scheme for assigning collision products includes a full range of astrophysically interesting objects.

# Appendix G Table of symbols

# G.1 Introduction

In this table we present a list of the most commonly used symbols. Depending on the context, some of these quantities may be in physical or $N$ -body units but this should not cause confusion since relevant scaling factors are provided. Inevitably some symbols are not unique, but adopting the traditional notation for clarity has been given precedence. In any case, such multiplicity does not usually occur within the same section. A few duplicated definitions are listed in footnotes to the table.

Table G.1. Frequently used symbols.   

<table><tr><td>a</td><td>Semi-major axis</td></tr><tr><td>ahard</td><td>Hard binary semi-major axis</td></tr><tr><td>D</td><td>Divided difference</td></tr><tr><td>e</td><td>Binary eccentricity</td></tr><tr><td>E</td><td>Energy</td></tr><tr><td>Eb</td><td>Binary energy</td></tr><tr><td>Ech</td><td>Energy of chain members</td></tr><tr><td>Esub</td><td>Subsystem energy</td></tr><tr><td>fb</td><td>Binary fraction</td></tr><tr><td>F</td><td>Force per unit mass</td></tr><tr><td>F(k)</td><td>Force derivative (also F)</td></tr><tr><td>F1</td><td>Irregular force</td></tr><tr><td>FR</td><td>Regular force</td></tr><tr><td>G</td><td>Gravitational constant</td></tr><tr><td>h</td><td>Two-body energy per unit mass</td></tr></table>

Table G.1. (cont.) Frequently used symbols.   

<table><tr><td>H</td><td>Hamiltonian function</td></tr><tr><td>J</td><td>Angular momentum</td></tr><tr><td>K</td><td>Kilo byte unit,1024</td></tr><tr><td>L</td><td>Neighbour list*</td></tr><tr><td>L</td><td>Levi-Civita matrix</td></tr><tr><td>mb</td><td>Binary mass</td></tr><tr><td>mi</td><td>Particle mass</td></tr><tr><td>mk</td><td>Mass of first binary component</td></tr><tr><td>ml</td><td>Mass of second binary component</td></tr><tr><td>M</td><td>Total cluster mass</td></tr><tr><td>Ms</td><td>Mean stellar mass (M)</td></tr><tr><td>nmax</td><td>Maximum neighbour number</td></tr><tr><td>N</td><td>Particle number</td></tr><tr><td>Nb Nc</td><td>Number of binaries</td></tr><tr><td></td><td>Particle number in the core</td></tr><tr><td>Np</td><td>Number of regularized pairs</td></tr><tr><td>Ns Ni</td><td>Number of single stars</td></tr><tr><td>P</td><td>Particle name</td></tr><tr><td></td><td>Physical perturbation</td></tr><tr><td>Pk</td><td>Regularized momenta</td></tr><tr><td>Qk</td><td>Regularized coordinates</td></tr><tr><td>Qvir</td><td>Virial theorem ratio</td></tr><tr><td>rc</td><td>Core radius (cluster or stellar)</td></tr><tr><td>rd</td><td>Density centre</td></tr><tr><td>rh</td><td>Half-mass radius</td></tr><tr><td>ri</td><td>Global coordinates</td></tr><tr><td>r</td><td>Stellar radius</td></tr><tr><td>rt</td><td>Tidal radius</td></tr><tr><td>R</td><td>Two-body separation</td></tr><tr><td>R</td><td>Initial two-body separation</td></tr><tr><td>Rcl</td><td>Close encounter distance</td></tr><tr><td>Rgrav</td><td>Gravitational radius</td></tr><tr><td>Rp</td><td>Pericentre distance</td></tr><tr><td>Rs</td><td>Neighbour sphere radius</td></tr><tr><td>Rv</td><td>Virial cluster radius (pc)</td></tr><tr><td>t</td><td>Time in N-body units</td></tr><tr><td>tblock</td><td>Block boundary time</td></tr><tr><td>tcr</td><td>Crossing time</td></tr></table>

Table G.1. (cont.) Frequently used symbols.   

<table><tr><td>tev</td><td>Stellar evolution time</td></tr><tr><td>trh</td><td>Half-mass relaxation time</td></tr><tr><td>T</td><td>Total kinetic energy</td></tr><tr><td>T*</td><td>Time scaling factor (Myr)</td></tr><tr><td>U</td><td>Potential energy</td></tr><tr><td>U</td><td>Regularized coordinates (also u)</td></tr><tr><td>U&#x27;</td><td>Regularized velocities (also u&#x27;)</td></tr><tr><td>Vi</td><td>Global velocities</td></tr><tr><td>V</td><td>Virial energy</td></tr><tr><td>V*</td><td>Velocity scaling factor (km s-1)</td></tr><tr><td>W</td><td>Tidal energy</td></tr><tr><td>α</td><td>IMF power-law exponent†</td></tr><tr><td>Y</td><td>Relative two-body perturbationt</td></tr><tr><td>/min</td><td>Limit for unperturbed motion</td></tr><tr><td>T</td><td>Regularized Hamiltonian</td></tr><tr><td>△tcl</td><td>Close encounter time-step</td></tr><tr><td>△ti</td><td>Individual time-step</td></tr><tr><td>△T</td><td>Regularized time-step</td></tr><tr><td>E</td><td>Softening parameter</td></tr><tr><td>Ehard</td><td>Hard binary energy</td></tr><tr><td>n</td><td>Standard time-step parameter</td></tr><tr><td>nu</td><td>KS time-step parameter</td></tr><tr><td>0</td><td>Eccentric anomaly$</td></tr><tr><td>K</td><td>Slow-down factor</td></tr><tr><td>入</td><td>C.m.approximation factor</td></tr><tr><td>μ</td><td>Reduced mass of binary</td></tr><tr><td>p</td><td>Spatial density</td></tr><tr><td>0</td><td>Velocity dispersion</td></tr><tr><td>T</td><td>Regularized time</td></tr><tr><td>Φ</td><td>Potential or potential energy</td></tr><tr><td>?</td><td>Inclination angle</td></tr><tr><td>w</td><td>General purpose angle</td></tr><tr><td>Ω</td><td>Angular velocityl</td></tr></table>

† Also relative energy error ‡ Also in Coloumb logarithm § Also opening angle $^ \mathparagraph$ Also energy in Stumpff method

# Appendix H Hermite integration method

Here we give the FORTRAN listing of standard Hermite integration for a test particle. The accuracy is controlled by the tolerance denoted $E T A$ . Results are given at times scaled by the initial period.

\* H E R M I T   
\* \*\*\*\*\*\*\*\*\*\*\*   
\*   
\* Standard Hermite integration.   
\*   
\* IMPLICIT REAL $^ { * 8 }$ (A-H,O-Z) REAL $^ { * 8 }$ X(3),XDOT(3),F(3),FDOT(3),FI(3),FD(3),D2(3) DATA TIME,NSTEPS /0.0,0/   
\* READ $( 5 , * )$ ETA, DELTAT, TCRIT READ $( 5 , * )$ (X(K), $\mathtt { K } { = } 1$ ,3), (XDOT(K), $\mathtt { K } { = } 1$ ,3) TNEXT $=$ DELTAT $\mathrm { R I } 2 ~ = ~ \mathrm { X } ( 1 ) * * 2 { \mathbf { \Omega } } + { \mathrm {  ~ X ( } 2 ) } * * 2 { \mathbf { \Omega } } + { \mathrm {  ~ X ( } 3 ) } * * 2$ $\mathtt { R I } \ = \ \mathtt { S Q R T } ( \mathtt { R I } 2 )$ $\mathrm { V I } 2 ~ = ~ \mathrm { X D O T } \left( 1 \right) * * 2 ~ + ~ \mathrm { X D O T } \left( 2 \right) * * 2 ~ + ~ \mathrm { X D O T } \left( 3 \right) * * 2$ $\mathtt { S E M I O } ~ = ~ 2 . 0 / \mathtt { R I } ~ - ~ \mathtt { V I } 2$ $\mathtt { S E M I O } \ = \ \mathtt { 1 . 0 / S E M I O }$ RDOT $ = \mathrm {  ~ X ( 1 ) * X D O T ( 1 ) ~ } + \mathrm {  ~ X ( 2 ) * X D O T ( 2 ) ~ } + \mathrm {  ~ X ( 3 ) * X D O T ( }$ (3) ECC0 $=$ SQRT((1.0 - RI/SEMI0) $* * 2$ $^ +$ RDOT\*\*2/SEMI0) $\mathrm { T W O P I } \ = \ 8 . 0 { * } \mathrm { A T A N } ( 1 . 0 \mathrm { D } 0 )$ $0 \tt N E 3 \ = \ 1 . 0 / 3 . 0 \tt D 0$ $0 \tt N E 1 2 \ = \ 1 . 0 / 1 2 . 0 D 0$ P = TWOPI\*SEMI0\*SQRT(SEMI0) DELTAT $=$ DELTAT $\mathrm { * P }$

TNEXT $=$ DELTAT TCRIT $\mathbf { \Sigma } = \mathbf { \Sigma } _ { \mathrm { T C R I T * P } }$

\* \*

Evaluate the initial force and first derivative. $\mathrm { R I N 3 } \ = \ 1 . 0 / ( \mathrm { R I 2 * S Q R T } ( )$ RI2)) RDOT $ = \ 3 . 0 * ( \mathrm { X } ( 1 ) * \mathrm { X D O T } ( 1 ) \ + \ \mathrm { X } ( 2 ) * \mathrm { X D O T } ( 2 ) + $ $\&$ X(3)\*XDOT(3))/RI2 DO 5 $\mathtt { K } \ = \ 1 , 3$ $\begin{array} { l } { \displaystyle { \sf F ( \bar { \bf K } ) } = - \bar { \bf X } \left( { \bf K } \right) * \mathrm { R I N } 3 } \end{array}$ $\mathrm { F D O T ( K ) \ = \ - ( X D O T ( K ) \ - \ \mathbb { R } D O T \ast X ( K ) \ ) \ast \mathbb { R } I N 3 }$ 5 CONTINUE

Choose initial time-step by force criterion. $\mathrm { F F } ~ = ~ \mathrm { S Q R T } \left( \mathrm { F } \left( 1 \right) * * 2 ~ + ~ \mathrm { F } \left( 2 \right) * * 2 ~ + ~ \mathrm { F } \left( 3 \right) * * 2 \right)$ STEP $=$ SQRT(ETA\*RI/FF)

Predict coordinates and velocity to order FDOT. 10 DT $\mathrm { ~ : ~ } = \mathrm { ~ } \mathsf { { s } }$ TEP $\mathtt { D T 2 } ~ = ~ 0 . 5 { * \mathtt { D T } }$ $\mathrm { D T } 3 \ = \ \mathrm { O N E 3 * D T }$ DO 20 $\mathrm { ~ K ~ } = \mathrm { ~ 1 ~ } ,$ 3 $\begin{array} { r } { \mathrm { X ( K ) ~ \ = ~ \ ( \ ( \ F D O T ( K ) * D T 3 ~ + ~ F ( K ) ) * D T 2 ~ + ~ \ x D O T ( K ) ) * D T ~ + } } \end{array}$ & X(K) $\mathrm { { X D O T } ( K ) \ = \ ( F D O T ( K ) * D T 2 \ + \ F ( K ) ) * D T \ + \ X D O T ( K ) }$ 20 CONTINUE

\*

Obtain force and first derivative at end of step. $\mathrm { R I } 2 ~ = ~ \mathrm { X } ( 1 ) * * 2 { \mathbf { \Omega } } + { \mathrm {  ~ X ( } 2 ) } * * 2 { \mathbf { \Omega } } + { \mathrm {  ~ X ( } 3 ) } * * 2$ $\mathrm { R I N 3 } ~ = ~ 1 . 0 / \left( \mathrm { R I } 2 { * \mathrm { S Q R T } \left( \mathrm { R I } 2 \right) } \right)$ ) R $\mathrm { \Delta \Psi ^ { \prime } D O T ~ = ~ 3 . 0 * ( X ( 1 ) * X D O T ( 1 ) ~ + ~ X ( 2 ) * X D O T ( 2 ) ~ + ~ }$ & X(3)\*XDOT(3))/RI2 DO 30 $\textsc { \det k } = \textsc { 1 } , 3$ $\begin{array} { r } { \mathrm { \sf { F I } } \left( \mathrm {  ~ \cal { K } } \right) \ = \ - \mathrm {  { ~ \cal { K } } } \left( \mathrm {  { ~ \cal { K } } } \right) * \mathrm { \sf { R I N } } 3 } \end{array}$ FD(K) $=$ -(XDOT(K) - RDOT\*X(K))\*RIN3 30 CONTINUE

\* $^ *$

Set corrector time factors and advance the time. $\mathsf { D T S Q } \ = \ \mathsf { D T } \ast \ast 2$ $\mathsf { D T 2 } \ = \ \mathsf { 2 } . 0 / \mathsf { D T S Q }$ $\mathrm { D T 6 } ~ = ~ 6 . 0 / \left( \mathrm { D T * D T S Q } \right)$ $\mathtt { D T 1 3 } \ = \ \mathtt { O N E 3 * D T }$ $\mathrm { D T S Q 1 2 } ~ = ~ \mathrm { O N E 1 } 2 { * \mathrm { D T S Q } }$ TIME $=$ TIME $^ +$ DT

\*

Include the Hermite corrector and update F & FDO DO $^ { 4 0 \mathrm { ~ K ~ } = \mathrm { ~ 1 ~ } , }$ 3 $\begin{array} { r } { \mathrm { D } \mathrm { F } \ = \ \mathrm { F } \left( \mathrm { K } \right) \ - \ \mathrm { F } \mathrm { I } \left( \mathrm { K } \right) } \end{array}$ $\mathrm { \bf S U M } = \mathrm { \bf \mathbb { F } D } 0 \mathrm { \bf T } \left( \mathrm { \bf K } \right) + \mathrm { \bf \nabla F D } \left( \mathrm { \bf K } \right)$ $\mathtt { A T 3 } \ = \ 2 . 0 { * } \mathrm { D F } \ + \ \mathtt { S U M } { * } \mathrm { D T }$ $\mathsf { B T 2 } \ = \ - 3 . 0 { * } \mathrm { D F }$ - (SUM $^ +$ FDOT(K)) $\ast \mathrm { D T }$ $\mathrm { X ( K ) ~ \ = ~ \ X ( K ) ~ \ + ~ \ ( 0 . 6 * A T 3 ~ + ~ B T 2 ) * D T S Q 1 2 }$ $\mathrm { { X D O T } ( K ) \ = \ \mathrm { { X D O T } ( K ) \ + \ ( 0 . 7 5 * A T 3 \ + \ B T 2 ) * D T 1 3 } }$ ${ \sf F } \left( { \sf K } \right) \ = \ { \sf F I } \left( { \sf K } \right)$ $\mathtt { F D O T } ( \mathtt { K } ) \ = \ \mathtt { F D } ( \mathtt { K } )$ $\mathrm { D 2 ( K ) \ = \ \mathrm { B T 2 * D T 2 \ + \ D T * A T 3 * D T 6 } }$

40 CONTINUE

Determine next step from $\textbf { F } \&$ F2DOT in Taylor series. $\mathrm { F F } ~ = ~ \mathrm { S Q R T } \left( \mathrm { F } \left( 1 \right) * * 2 ~ + ~ \mathrm { F } \left( 2 \right) * * 2 ~ + ~ \mathrm { F } \left( 3 \right) * * 2 \right)$ $\mathrm { F F } 2 ~ = ~ \mathrm { S Q R T } \left( \mathrm { D } 2 \left( 1 \right) * * 2 ~ + ~ \mathrm { D } 2 \left( 2 \right) * * 2 ~ + ~ \mathrm { D } 2 \left( 3 \right) * * 2 ~ \right.$ STEP $=$ SQRT(ETA\*FF/FF2)

Increase step counter and check output time. NSTE ${ \mathsf { P S } } ~ = ~ { \tt N S T E P S } ~ + ~$ 1 IF (TIME.LT.TNEXT) GO TO 10

Print errors in semi-major axis & eccentricity. $\mathrm { R I } 2 ~ = ~ \mathrm { X } ( 1 ) * * 2 { \mathbf { \Omega } } + { \mathrm {  ~ X ( } 2 ) } * * 2 { \mathbf { \Omega } } + { \mathrm {  ~ X ( } 3 ) } * * 2$ $\mathtt { R I } \ = \ \mathtt { S Q R T } ( \mathtt { R I } 2 )$ $\mathrm { V I } 2 ~ = ~ \mathrm { X D O T } \left( 1 \right) * * 2 ~ + ~ \mathrm { X D O T } \left( 2 \right) * * 2 ~ + ~ \mathrm { X D O T } \left( 3 \right) * * 2$ SEMI $=$ 2.0/RI - VI2 SEMI $\mathit { \Theta } = \mathit { \Theta } 1 . 0 / \mathtt { S E M I }$ $\mathrm { R D O T } ~ = ~ \mathrm { X } ( \mathrm { 1 } ) * \mathrm { X D O T } ( \mathrm { 1 } ) ~ + ~ \mathrm { X } ( \mathrm { 2 } ) * \mathrm { X D O T } ( \mathrm { 2 } ) ~ + ~ \mathrm { X } ( \mathrm { 3 } ) * \mathrm { X D O T } ( \mathrm { 3 } ) * \mathrm { X } ( \mathrm { 2 } )$ (3) ECC $=$ SQRT((1.0 - RI/SEMI) $* * 2$ $^ +$ RDOT\*\*2/SEMI) DA $=$ (SEMI - SEMI0)/SEMI0 $\mathrm { D E } \ = \ \mathrm { E C C } 0 \ - \ \mathrm { E C } ($ C WRITE (6,50) TIME/P, NSTEPS, ECC, DA, DE 50 FORMAT (’ $\mathrm { T / P } \ = \mathrm { \mathrm { \Omega } }$ ,F8.1,’ # $\ r = \ r ^ { \prime }$ ,I7,’ $\boldsymbol { \mathrm { ~ E ~ } } = \boldsymbol { \ O }$ ,F8.4, & ， DA/A $=$ ’,1P,E9.1,’ DE $\mathbf { \lambda } = \mathbf { \dot { \varepsilon } }$ ,E9.1) TNEXT $=$ TNEXT $^ +$ DELTAT IF (TIME.LT.TCRIT) GO TO 10

# References

arseth, S. J. [1963a], Dynamics of Galaxies, Ph.D. Thesis (University of Cambridge).   
[1963b], ‘Dynamical evolution of clusters of galaxies, I’, Mon. Not. R. Astron. Soc. 126, 223–55.   
[1966a], ‘Dynamical evolution of clusters of galaxies, II’, Mon. Not. R. Astron. Soc. 132, 35–65.   
[1966b], ‘Third integral of motion for high-velocity stars’, Nature, 212, 57–8.   
[1967], ‘On a collisionless method in stellar dynamics, I’, Bull. Astron. 2, 47– 57.   
[1968], ‘Dynamical evolution of simulated $N$ -body systems’, Bull. Astron. 3, 105–25.   
[1969], ‘Dynamical evolution of clusters of galaxies, III’, Mon. Not. R. Astron. Soc. 144, 537–48.   
[1970], ‘Perturbation treatment of close binaries in the $N$ -body problem’, Astron. Astrophys. 9, 64–9.   
[1972a], ‘Binary evolution in stellar systems’, in Gravitational $N$ -Body Problem, ed. M. Lecar (Reidel, Dordrecht), 88–98.   
[1972b], ‘Direct integration methods of the $N$ -body problem’, in Gravitational $N$ -Body Problem, ed. M. Lecar (Reidel, Dordrecht), 373–87.   
[1973], ‘Computer simulations of star cluster dynamics’, Vistas Astron. 15, 13–37.   
[1974], ‘Dynamical evolution of simulated star clusters’, Astron. Astrophys. 35, 237–50.   
[1975], ‘ $N$ -body simulations’, in Dynamics of Stellar Systems, ed. A. Hayli (Reidel, Dordrecht), 57–9.   
[1976], ‘A note on stabilization in three-body regularization’, in Long-Time Predictions in Dynamics, ed. V. Szebehely & B. D. Tapley (Reidel, Dordrecht), 173–7.   
[1980], ‘Dynamics of initial binaries in open clusters’, in Star Clusters, ed. J. E. Hesser (Reidel, Dordrecht), 325–6. J. Press, Orlando), 377–418. [1985b], ‘Direct $N$ -body calculations’, in Dynamics of Star Clusters, ed. J. Goodman & P. Hut (Reidel, Dordrecht), 251–8. [1988a], ‘Integration methods for small $N$ -body systems’, in The Few Body Problem, ed. M. J. Valtonen (Reidel, Dordrecht), 287–307. [1988b], ‘Dynamics of molecular clouds’, Bol. Acad. Nac. Cienc. Cordoba 58, 201–8. [1994], ‘Direct methods for $N$ -body simulations’, in Lecture Notes in Physics, ed. G. Contopoulos, N. K. Spyrou, & L. Vlahos (Springer-Verlag, New York), 433, 277–312. [1996a], ‘Star cluster simulations on HARP’, in Dynamical Evolution of Star Clusters, ed. P. Hut & J. Makino (Kluwer, Dordrecht), 161–70. [1996b], ‘ $N$ -body simulations of open clusters with binary evolution’, in The Origins, Evolution, and Destinies of Binary Stars in Clusters, ed. E. F. Milone & J.-C. Mermilliod (ASP, San Francisco), 90, 423–30. [1999a], ‘From NBODY1 to NBODY6: the growth of an industry’, Publ. Astron. Soc. Pacific 111, 1333–46. [1999b], ‘Star cluster simulations: the state of the art’, in Impact of Modern Dynamics in Astronomy, ed. J. Henrard & S. Ferraz-Mello (Kluwer, Dordrecht), 127–37. [2001a], ‘The formation of hierarchical systems’, in Dynamics of Star Clusters and the Milky Way, ed. S. Deiters, B. Fuchs, A. Just, R. Spurzem & R. Wielen (ASP, San Francisco), 228, 111–16. [2001b], ‘NBODY2: a direct $N$ -body integration code’, New Astron. 6, 277–91. [2001c], ‘Regularization methods for the $N$ -body problem’, in The Restless Universe, ed. B. A. Steves & A. J. Maciejewski (Institute of Physics, Bristol), 93–108. [2003a], ‘Regularization tools for binary interactions’, in Astrophysical Supercomputing using Particle Simulations, ed. J. Makino & P. Hut (ASP, San Francisco), 295–304, astro-ph/0110148. [2003b], ‘Black hole binary dynamics’, in Fred Hoyle’s Universe, ed. G. Burbidge, J. V. Narlikar & N. C. Wickramasinghe, astro-ph/0210116, Astrophys. Sp. Sci. 285.   
Aarseth, S. J. & Fall, S. M. [1980], ‘Cosmological $N$ -body simulations of galaxy merging’, Astrophys. J. 236, 43–57.   
Aarseth, S. J. & Heggie, D.C. [1976], ‘The probability of binary formation by three-body encounters’, Astron. Astrophys. 53, 259–65. [1993], ‘Core collapse for $N = 6 0 0 0$ ’, in The Globular Cluster–Galaxy Connection, ed. G. H. Smith & J. P. Brodie (ASP, San Francisco), 48, 701–4. [1998], ‘Basic $N$ -body modelling of the evolution of globular clusters, I. Time scaling’, Mon. Not. R. Astron. Soc. 297, 794–806.   
Aarseth, S. J. & Hills, J. G. [1972], ‘The dynamical evolution of a stellar cluster with initial subclustering’, Astron. Astrophys. 21, 255–63.   
Aarseth, S. J. & Hoyle, F. [1964], ‘An assessment of the present state of the gravitational $N$ -body problem’, Astrophysica Norvegica 9, 313–21.   
Aarseth, S. J. & Inagaki, S. [1986], ‘Vectorization of $N$ -body codes’, in The Use of Supercomputers in Stellar Dynamics, ed. P. Hut & S. McMillan (Springer-Verlag, New York), 203–5.   
Aarseth, S. J. & Lecar, M. [1975], ‘Computer simulations of stellar systems’, Ann. Rev. Astron. Astrophys. 13, 1–21. [1984], ‘The formation of the terrestrial planets from lunar sized planetesimals’, in Planetary Rings, ed. A. Brahic (Cepadues, Toulouse), 661–74.   
Aarseth, S. & Mardling, R. [1997], ‘Neutron star binaries in open clusters’, in Pulsars: Problems and Progress, ed. S. Johnston, M.A. Walker & M. Bailes (ASP, San Francisco), 105, 541–2. [2001], ‘The formation and evolution of multiple star systems’, in Evolution of Binary and Multiple Star Systems; A Meeting in Celebration of Peter Eggleton’s 60th Birthday, ed. P. Podsiadlowski, S. Rappaport, A. R. King, F. D’Antona & L. Burderi (ASP, San Francisco), 229, 77–88.   
Aarseth, S. J. & Saslaw, W. C. [1972], ‘Virial mass determinations of bound and unstable groups of galaxies’, Astrophys. J. 172, 17–35. [1982], ‘Formation of voids in the galaxy distribution’, Astrophys. J. 258, L7– L10.   
Aarseth, S. J. & Wolf, N. J. [1972], ’Depletion of low-mass stars in clusters’, Astrophys. Lett. 12, 159–64.   
Aarseth, S. J. & Zare, K. [1974], ‘A regularization of the three-body problem’, Celes. Mech. 10, 185–205.   
Aarseth, S. J., Gott, J. R. & Turner, E. L. [1979], ‘ $N$ -body simulations of galaxy clustering, I. Initial conditions and galaxy collapse times’, Astrophys. J. 228, 664–83.   
Aarseth, S. J., H´enon, M. & Wielen, R. [1974], ‘A comparison of numerical methods for the study of star cluster dynamics’, Astron. Astrophys. 37, 183–7.   
Aarseth, S. J., Lin, D. N. C. & Palmer, P. L. [1993], ‘Evolution of planetesimals, II. Numerical simulations’, Astrophys. J. 403, 351–76.   
Aarseth, S. J., Lin, D. N. C. & Papaloizou, J. C. B. [1988], ‘On the collapse and violent relaxation of protoglobular clusters’, Astrophys. J. 324, 288–310.   
Aarseth, S. J., Anosova, J. P., Orlov, V. V. & Szebehely, V. G. [1994a], ‘Global chaoticity in the Pythagorean three-body problem’, Celes. Mech. Dyn. Ast. 58, 1–16. [1994b], ‘Close triple approaches and escape in the three-body problem’, Celes. Mech. Dyn. Ast. 60, 131–7.   
Adams, F. C. & Laughlin, G. [2001], ‘Constraints on the birth aggregate of the Solar System’, Icarus 150, 151–62.   
Agekian, T. A. & Anosova, J. P. [1968a], ‘Investigation of the dynamics of triple systems by the method of statistical tests, II’, Astrophys. 4, 11–16. [1968b], ‘Evolution of binary systems in the galactic field’, Astrophys. 4, 196–8. [1968c], ‘A study of the dynamics of triple systems by means of statistical sampling’, Soviet Astron. 11, 1006–14. [1971], ‘Probability of binary-system formation through triple encounters’, Soviet Astron. 15, 411–14.   
Aguilar, L. A. & White, S. D. M. [1985], ’Tidal interactions between spherical galaxies’, Astrophys. J. 295, 374–87.   
Ahmad, A. & Cohen, L. [1973], ‘A numerical integration scheme for the $N$ -body gravitational problem’, J. Comput. Phys. 12, 389–402. [1974], ‘Integration of the $N$ -body gravitational problem by separation of the force into a near and a far component’, in Lecture Notes in Mathematics, ed. D. G. Bettis (Springer-Verlag, New York), 362, 313–6.   
Aitken, R. G. [1914], ‘Measures of double stars’, Publ. Lick Obs. 12, 35–6.   
Aksnes, K. & Standish, E. M. [1969], ‘A numerical test of the relaxation time’, Astrophys. J. 158, 519–27.   
Alexander, M. E. [1986], ‘Simulation of binary–single star and binary–binary scattering’, J. Comput. Phys. 64, 195–219.   
Allen, C. & Poveda, A. [1972], ‘On the reproducibility of run-away stars formed in collapsing clusters’, in Gravitational N -Body Problem, ed. M. Lecar (Reidel, Dordrecht), 114–23.   
Ambartsumian, V. A. [1938], Ann. Leningrad State Univ., No. 22, 19. [1985], ‘On the dynamics of open clusters’, in Dynamics of Star Clusters, ed. J. Goodman & P. Hut (Reidel, Dordrecht), 521–4.   
Anosova, J. P. [1986], ‘Dynamical evolution of triple systems’, Astrophys. Sp. Sci. 124, 217–41. [1991], ‘Strong triple interactions in the general three-body problem’, Celes. Mech. Dyn. Ast. 51, 1–15.   
Anosova, J. P., Bertov, D. I. & Orlov, V. V. [1984], ‘Influence of rotation on the evolution of triple systems’, Astrophys. 20, 177–84.   
Anosova, J. P., Orlov, V. V. & Aarseth, S. J. [1994], ‘Initial conditions and dynamics of triple systems’, Celes. Mech. Dyn. Ast. 60, 365–72.   
Arabadjis, J. S. & Richstone, D. O. [1996], ‘The evolution of dense rotating $N$ -body systems’, Bull. Am. Astron. Soc. 28, 1310.   
Bacon, D., Sigurdsson, S. & Davies, M. B. [1996], ‘Close approach during hard binary–binary scattering’, Mon. Not. R. Astron. Soc. 281, 830–46.   
Bailey, V. C. & Davies, M. B. [1999], ‘Red giant collisions in the Galactic Centre’, Mon. Not. R. Astron. Soc. 308, 257–70.   
Bailyn, C. D. [1987], Ph.D. Thesis (Yale University). [1995], ‘Blue stragglers and other stellar anomalies: implications for the dynamics of globular clusters’, Ann. Rev. Astron. Astrophys. 33, 133– 62.   
Barnes, J. [1984], ‘ $N$ -body studies of compact groups of galaxies dominated by dark matter’, Mon. Not. R. Astron. Soc. 208, 873–85.   
Barnes, J. & Hut, P. [1986], ‘A hierarchical $O ( N \log N )$ force-calculation algorithm’, Nature 324, 446–9.   
Baumgardt, H. [2001], ‘Scaling of $N$ -body calculations’, Mon. Not. R. Astron. Soc. 325, 1323–31. [2002], ‘Lifetimes of star clusters and dynamical relaxation’, in Dynamics of Star Clusters and the Milky Way, ed. S. Deiters, B. Fuchs, A. Just, R. Spurzem & R. Wielen (ASP, San Francisco), 228, 125–30.   
Baumgardt, H. & Makino, J. [2003] ‘Dynamical evolution of star clusters in tidal fields’, Mon. Not. R. Astron. Soc. 340, 227–46.   
Baumgardt, H., Hut, P. & Heggie, D.C. [2002], ‘Long-term evolution of isolated $N$ -body systems’, Mon. Not. R. Astron. Soc. 336, 1069–81.   
Baumgardt, H., Hut, P., Makino, J., McMillan, S. & Portegies Zwart, S. [2003], ‘On the central structure of M15’, Astrophys. J. 582, L21–L24.   
Baumgarte, J. [1973], ‘Numerical stabilization of all laws of conservation in the many body problem’, Celes. Mech. 8, 223–8.   
Baumgarte, J. & Stiefel, E. L. [1974], ‘Examples of transformations improving the numerical accuracy of the integration of differential equations’, in Lecture Notes in Mathematics, ed. D. G. Bettis (Springer-Verlag, New York), 362, 207–36.   
Beaug´e, C. & Aarseth, S. J. [1990], ‘ $N$ -body simulations of planetary formation’, Mon. Not. R. Astron. Soc. 245, 30–9.   
Benz, W. & Hills, J. G. [1992], ‘Three-dimensional hydrodynamical simulations of colliding stars, III. Collisions and tidal captures of unequal-mass mainsequence stars’, Astrophys. J. 389, 546–57.   
Bettis, D. G. & Szebehely, V. [1972], ‘Treatment of close approaches in the numerical integration of the gravitational problem of $N$ bodies’, in Gravitational $N$ -Body Problem, ed. M. Lecar (Reidel, Dordrecht), 388–405.   
Bettwieser, E. & Sugimoto, D. [1984], ‘Post-collapse evolution and gravothermal oscillations of globular clusters’, Mon. Not. R. Astron. Soc. 208, 493–509.   
Binney, J. & Tremaine, S. [1987], Galactic Dynamics (Princeton University Press).   
Blaes, O., Lee, M. H. & Socrates, A. [2002], ‘The Kozai mechanism and the evolution of binary supermassive black holes’, Astrophys. J. 578, 775–86.   
Boily, C. M. [2000], ‘The impact of rotation on cluster dynamics’, in Massive Stellar Clusters, ed. A. Lan¸con & C. M. Boily (ASP, San Francisco), 211, 190–6.   
Boily, C. M. & Spurzem, R. [2000], ‘ $N$ -body modelling of rotating star clusters’, in The Galactic Halo, ed. A. Noels et al. (Liege, Belgium), 607–12.   
Bolte, M. [1992], ‘CCD photometry in the globular cluster NGC 288, I. Blue stragglers and main-sequence binary stars’, Astrophys. J. Suppl. 82, 145–65.   
Bolte, M., Hesser, J. E. & Stetson, P. B. [1993], ‘Canada–France–Hawaii telescope observations of globular cluster cores: blue straggler stars in M3’, Astrophys. J. 408, L89–L92.   
Bonnell, I. A. & Davies, M. B. [1998], ‘Mass segregation in young stellar clusters’, Mon. Not. R. Astron. Soc. 295, 691–8.   
Bonnell, I. A., Smith, K. W., Davies, M. B. & Horne, K. [2001], ‘Planetary dynamics in stellar clusters’, Mon. Not. R. Astron. Soc. 322, 859–65.   
Bouvier, P. & Janin, G. [1970], ‘Disruption of star clusters through passing interstellar clouds investigated by numerical experiments’, Astron. Astrophys. 9, 461–5.   
Boyd, P. T. & McMillan, S. L. W. [1993], ‘Chaotic scattering in the gravitational three-body problem’, Chaos 3, 507–23.   
Brehm, M., Bader, R., Heller, H. & Ebner, R. [2000], ‘Pseudovectorization, SMP and message passing on the Hitachi SR8000-F1’, in Lecture Notes in Computer Science, ed. A. Bode et al. (Springer-Verlag, New York), 1900, 1351–62.   
Brouwer, D. & Clemence, G. M. [1961], Methods of Celestial Mechanics, (Academic Press, New York).   
Bulirsch, R. & Stoer, J. [1966], ‘Numerical treatment of ordinary differential equations by extrapolation methods’, Num. Math. 8, 1–13.   
Burdet, C. A. [1967], ‘Regularization of the two-body problem’, Z. Angew. Math. Phys. 18, 434–8. [1968], ‘Theory of Kepler motion: the general perturbed two body problem’, Z. Angew. Math. Phys. 19, 345–68.   
Burrau, C. [1913], ‘Numerische Berechnung eines Spezialfalles des Dreik¨orper-Problems’, Astron. Nach. 195, 113–18.   
Casertano, S. & Hut, P. [1985], ‘Core radius and density measurements in $N$ -body experiments: connections with theoretical and observational definitions’, Astrophys. J. 298, 80–94.   
Cazenave, A., Lago, B. & Dominh, K. [1982], ‘Numerical experiment applicable to the latest stage of planet growth’, Icarus 51, 133–48.   
Chambers, J. E. [1999], ‘A hybrid symplectic integrator that permits close encounters between massive bodies’, Mon. Not. R. Astron. Soc. 304, 793–9.   
Chambers, J. E. & Wetherill, G. W. [1998], ‘Making the terrestrial planets: $N$ -body integrations of planetary embryos in three dimensions’, Icarus 136, 304–27.   
Chandrasekhar, S. [1942], Principles of Stellar Dynamics (Dover, New York).   
Chenciner, A. & Montgomery, R. [2000], ‘A remarkable periodic solution of the three-body problem in the case of equal masses’, Ann. Math. 152, 881– 901.   
Chernoff, D. & Weinberg, M. [1990], ‘Evolution of globular clusters in the Galaxy’, Astrophys. J. 351, 121–56.   
Chirikov, B. V. [1979], ‘A universal instability of many-dimensional oscillator systems’, Phys. Rep. 52, 263–379.   
Cohn, H. [1979], ‘Numerical integration of the Fokker–Planck equation and the evolution of star clusters’, Astrophys. J. 234, 1036–53. [1980], ‘Late core collapse in star clusters and the gravothermal instability’, Astrophys. J. 242, 765–71.   
Cohn, H., Hut, P. & Wise, M. [1989], ‘Gravothermal oscillations after core collapse in globular cluster evolution’, Astrophys. J. 342, 814–22.   
Cool, A., Piotto, G. & King, I. [1996], ‘The main sequence and a white dwarf sequence in the globular cluster NGC 6397’, Astrophys. J. 468, 655–62.   
Couchman, H. M. P. [1991], ‘Mesh-refined P3M: a fast adaptive $N$ -body algorithm’, Astrophys. J. 368, L23–L26.   
Cox, L. P. & Lewis, J. S. [1980], ‘Numerical simulation of the final stages of terrestrial planet formation’, Icarus 44, 706–21.   
Daisaka, H. & Makino, J. [2003], ‘The formation process and dynamics of the Uranian elliptical rings’, Astrophys. J. , submitted.   
Daisaka, H., Tanaka, H. & Ida, S. [2001], ‘Viscosity in a dense planetary ring with self-gravitating particles’, Icarus 154, 296–312.   
Danby, J. M. A. [1992], Fundamentals of Celestial Mechanics (Willmann–Bell, Richmond).   
Davies, M. B. [2001], ‘Stellar collisions in the Galactic centre’, in Dynamics of Star Clusters and the Milky Way, ed. S. Deiters, B. Fuchs, A. Just, R. Spurzem & R. Wielen (ASP, San Francisco), 228, 147–52.   
Davies, M. B., Benz, W. & Hills, J. G. [1991], ‘Stellar encounters involving red giants in globular cluster cores’, Astrophys. J. 381, 449–61.   
Davies, M. B., Blackwell, R., Bailey, V. C. & Sigurdsson, S. [1998], ‘The destructive effects of binary encounters on red giants in the Galactic centre’, Mon. Not. R. Astron. Soc. 301, 745–53.   
de la Fuente Marcos, C. & de la Fuente Marcos, R. [1997], ‘Eccentric giant planets in open star clusters’, Astron. Astrophys. 326, L21–L24. [1999], ‘Runaway planets’, New Astron. 4, 21–32. [2001], ‘Reshaping the outskirts of planetary systems’, Astron. Astrophys. 371, 1097–206.   
de la Fuente Marcos, R. [1995], ‘The initial mass function and the dynamical evolution of open clusters, I. Conservative systems’, Astron. Astrophys. 301, 407–18. [1996a], ‘The initial mass function and the dynamical evolution of open clusters, II. With mass loss’, Astron. Astrophys. 308, 141–50. [1996b], ‘The initial mass function and the dynamical evolution of open clusters, III. With primordial binaries’, Astron. Astrophys. 314, 453–64. [1997], ‘The initial mass function and the dynamical evolution of open clusters, IV. Realistic systems’, Astron. Astrophys. 322, 764–77. [1998], ‘Searching for open cluster remnants’, Astron. Astrophys. 333, L27–L30.   
de la Fuente Marcos, R. & de la Fuente Marcos, C. [2000], ‘On the dynamical evolution of the brown dwarf population in open clusters’, Astrophys. Sp. Sci. 271, 127–44. [2002], ‘Dynamics of very rich open clusters’, Astrophys. Sp. Sci. 280, 381–404.   
de la Fuente Marcos, R., Aarseth, S. J., Kiseleva, L. G. & Eggleton, P. P. [1997], ‘Hierarchical systems in open clusters’, in Visual Double Stars: Formation, Dynamics and Evolutionary Tracks, ed. J. A. Docobo, A. Elipe & H. McAlister (Kluwer, Dordrecht), 165–78.   
Dehnen, W. [2001], ‘Towards optimal softening in three-dimensional $N$ -body codes, I. Minimizing the force error’, Mon. Not. R. Astron. Soc. 324, 273–91.   
Dejonghe, H. & Hut, P. [1986], ‘Round-off sensitivity in the $N$ -body problem’, in The Use of Supercomputers in Stellar Dynamics, ed. P. Hut & S. McMillan (Springer-Verlag, New York), 212–18.   
Dekel, A. & Aarseth, S. J. [1984], ‘The spatial correlation function of galaxies confronted with theoretical scenarios’, Astrophys. J. 283, 1–23.   
Dorband, E. N., Hemsendorf, M. & Merritt, D. [2003], ‘Systolic and hypersystolic algorithms for the gravitational $N$ -body problem with an application to Brownian motion’, astro-ph/0112092, J. Comput. Phys. 185, 484–511.   
Dubinski, J. [1996], ‘A parallel tree code’, New Astron. 1, 133–47.   
Duchˆene, G. [1999], ‘Binary fraction in low-mass star forming regions: a reexamination of the possible excesses and implications’, Astron. Astrophys. 341, 547-52.   
Duquennoy, A. & Mayor, M. [1991], ‘Multiplicity among solar-type stars in the solar neighbourhood, II. Distribution of the orbital elements in an unbiased sample’, Astron. Astrophys. 248, 485–524.   
Dyer, C. C. & Ip, P. S. S. [1993], ‘Softening in $N$ -body simulations of collisionless systems’, Astrophys. J. 409, 60–7.   
Ebisuzaki, T., Makino, J., Tsuru, T. G., Funato, Y., Portegies Zwart, S., Hut, P., McMillan, S., Matsushita, S., Matsumoto, H. & Kawabe, R. [2001], ‘Missing link found? The ”runaway” path to supermassive black holes’, Astrophys. J. 562, L19–L22.   
Efstathiou, G. P. & Eastwood, J. [1981], ‘On the clustering of particles in an expanding universe’, Mon. Not. R. Astron. Soc. 194, 503–25.   
Eggleton, P. P. [1983], ‘Approximations to the radii of Roche lobes’, Astrophys. J. 268, 368–9.   
Eggleton, P. & Kiseleva, L. [1995], ‘An empirical condition for stability of hierarchical triple systems’, Astrophys. J. 455, 640–5.   
Eggleton, P. P., Fitchett, M. J. & Tout, C. A. [1989], ‘The distribution of visual binaries with two bright components’, Astrophys. J. 347, 998–1011.   
Eggleton, P. P., Kiseleva, L. G. & Hut, P. [1998], ‘The equilibrium tide model for tidal friction’, Astrophys. J. 499, 853–70.   
Einsel, C. & Spurzem, R. [1999], ‘Dynamical evolution of rotating stellar systems, I. Pre-collapse, equal-mass system’, Mon. Not. R. Astron. Soc. 302, 81–95.   
Elson, R. A. W., Sigurdsson, S., Davies, M., Hurley, J. & Gilmore, G. [1998], ‘The binary star population of the young cluster NGC 1818 in the Large Magellanic Cloud’, Mon. Not. R. Astron. Soc. 300, 857–62.   
Farouki, R. T. & Salpeter, E. E. [1982], ‘Mass segregation, relaxation and the Coulomb logarithm in $N$ -body systems’, Astrophys. J. 253, 512–19.   
Fekel, F. C., Scarfe, C. D., Barlow, D. J., Hartkopf, W. I., Mason, B. & McAlister, H.A. [2002], ‘The quadruple system $\mu$ Orionis: threedimensional orbit and physical parameters’, Astron. J. 123, 1723–40.   
Fellhauer, M., Kroupa, P., Baumgardt, H., Bien, R., Boily, C. M., Spurzem, R. & Wassmer, N. [2000], ‘SUPERBOX – An efficient code for collisionless galactic dynamics’, New Astron. 5, 305–26.   
Fellhauer, M., Lin, D. N. C, Bolte, M., Aarseth, S. J. & Williams, K. A. [2003], ‘The white dwarf deficit in open clusters: dynamical processes’, Astrophys. J. Letters, in press.   
Ferraro, F. R., Sills, A., Rood, R. T., Paltrinieri, B. & Buonanno, R. [2003], ‘Blue straggler stars: a direct comparison of star counts and population ratios in six Galactic globular clusters’, Astrophys. J. 558, 464–77.   
Findlay, D. A. [1983], Cosmological $N$ -Body Simulations of Galaxy Clustering: Tidal Interactions and Merging, Ph.D. Thesis (University of Cambridge). extrasolar planetary systems containing two giant planets’, Icarus 150, 303–13.   
Ford, E. B., Kozinsky, B. & Rasio, F. A. [2000], ‘Secular evolution of hierarchical triple star systems’, Astrophys. J. 535, 385–401.   
Freitag, M. & Benz, W. [2001], ‘A new Monte Carlo code for star cluster simulations, I. Relaxation’, Astron. Astrophys. 375, 711–38. [2002], ‘A new Monte Carlo code for star cluster simulations, II. Central black hole and stellar collisions’, Astron. Astrophys. 394, 345–74.   
Fukushige, T. & Heggie, D.C. [1995], ‘Pre-collapse evolution of galactic globular clusters’, Mon. Not. R. Astron. Soc. 276, 206–18. [2000], ‘The time-scale of escape from star clusters’, Mon. Not. R. Astron. Soc. 318, 753–61.   
Fukushima, T. [1997], ‘Vector integration of dynamical motions by the Picard– Chebyshev method’, Astron. J. 113, 2325–8.   
Fullerton, L. W. & Hills, J. G. [1982], ‘Computer simulations of close encounters between binary and single stars: the effect of the impact velocity and the stellar masses’, Astron. J. 87, 175–83.   
Funato, Y., Hut, P., McMillan, S. & Makino, J. [1996], ‘Time-symmetrized Kustaanheimo–Stiefel regularization’, Astron. J. 112, 1697–708.   
Gerhard, O. E. [1981], ‘ $N$ -body simulations of disc-halo galaxies: isolated systems, tidal interactions and merging’, Mon. Not. R. Astron. Soc. 197, 179–208. [1982], Dynamical Effects of Galaxy Encounters, Ph.D. Thesis (University of Cambridge). [2000], ‘Dynamical masses, time-scales and evolution of star clusters’, in Massive Stellar Clusters, ed. A. Lan¸con & C. M. Boily (ASP, San Francisco), 211, 12–24.   
Giannone, G. & Molteni, D. [1985], ‘The role of initial binaries in cluster evolution: direct $N$ -body calculations’, Astron. Astrophys. 143, 321–6.   
Giersz, M. [1996], ‘Monte-Carlo simulations’, in Dynamical Evolution of Star Clusters, ed. P. Hut & J. Makino (Kluwer, Dordrecht), 101–10. [2001a], ‘Monte Carlo simulations of star clusters, II. Tidally limited, multimass systems with stellar evolution’, Mon. Not. R. Astron. Soc. 324, 218– 30. [2001b], ‘Monte Carlo simulations of star clusters’, in Dynamics of Star Clusters and the Milky Way, ed. S. Deiters, B. Fuchs, A. Just, R. Spurzem & R. Wielen (ASP, San Francisco), 228, 61–6.   
Giersz, M. & Heggie, D.C. [1994a], ‘Statistics of $N .$ -body simulations, I. Equal masses before core collapse’, Mon. Not. R. Astron. Soc. 268, 257–75. [1994b], ‘Statistics of $N$ -body simulations, II. Equal masses after core collapse’, Mon. Not. R. Astron. Soc. 270, 298–324. [1996], ‘Statistics of $N$ -body simulations, III. Unequal masses’, Mon. Not. R. Astron. Soc. 279, 1037–56. [1997], ‘Statistics of $N$ -body simulations, IV. Unequal masses with a tidal field’, Mon. Not. R. Astron. Soc. 286, 709–31.   
Giersz, M. & Spurzem, R. [1994], ‘Comparing direct $N$ -body integration with anisotropic gaseous models of star clusters’, Mon. Not. R. Astron. Soc. 269, 241–56. [2000], ‘A stochastic Monte Carlo approach to model real star cluster evolution, II. Self-consistent models and primordial binaries’, Mon. Not. R. Astron. Soc. 317, 581–606. [2003], ‘A stochastic Monte Carlo approach to model real star cluster evolution, III. Direct integrations of three- and four-body interactions’, Mon. Not. R. Astron. Soc. in press.   
Gladman, B. [1993], ‘Dynamics of systems of two close planets’, Icarus 106, 247–63.   
Gnedin, O. Y. & Ostriker, J. P. [1997], ‘Destruction of the galactic globular cluster system’, Astrophys. J. 474, 223–55.   
Goldreich, P. & Tremaine, S. D. [1978], ‘The velocity dispersion in Saturn’s rings’, Icarus 34, 227–39.   
Gonzalez, C. C. & Lecar, M. [1968], ‘Encounters and escapes’, Bull. Astron. 3, 209–11.   
Goodman, J. [1987], ’On gravothermal oscillations’, Astrophys. J. 313, 576– 95.   
Goodman, J., Heggie, D.C. & Hut, P. [1993], ‘On the exponential instability of $N$ -body systems’, Astrophys. J. 415, 715–33.   
Goodwin, S. P. [1997], ‘Residual gas expulsion from young globular clusters’, Mon. Not. R. Astron. Soc. 284, 785–802.   
Gott, J. R., Turner, E. L. & Aarseth, S. J. [1979], ‘ $N$ -body simulations of galaxy clustering, III. The covariance function’, Astrophys. J. 234, 13–26.   
Griffith, J. S. & North, R. D. [1974], ‘Escape or retention in the three-body problem’, Celes. Mech. 8, 473–9.   
Grillmair, C. J. [1998], ‘Probing the Galactic Halo with globular cluster tidal tails’, in Galactic Halos, ed. D. Zaritsky (ASP, San Francisco), 136, 45–52.   
Grindlay, J. E. [1996], ‘High resolution studies of compact binaries in globular clusters with HST and ROSAT’, in Dynamical Evolution of Star Clusters, ed. P. Hut & J. Makino (Kluwer, Dordrecht), 171–80.   
Guhathakurta, P., Webster, Z. T., Yanny, B., Schneider, D. P. & Bahcall, J. N. [1998], ‘Globular cluster photometry with the Hubble Space Telescope, VII. Color gradients and blue stragglers in the central region of M30’, Astron. J. 116, 1757–74.   
Gunn, J. E. & Griffin, R. F. [1979], ‘Dynamical studies of globular clusters based on photometric radial velocities of individual stars, I. M3’, Astron. J. 84, 752–73.   
Hansen, B. M. S. & Phinney, E. S. [1997], ‘The pulsar kick velocity distribution’, Mon. Not. R. Astron. Soc. 291, 569–77.   
Harrington, R. S. [1972], ‘Stability criteria for triple stars’, Celes. Mech. 6, 322–7. [1974], ‘The dynamical decay of unstable 4-body systems’, Celes. Mech. 9, 465–70. [1975], ‘Production of triple stars by the dynamical decay of small stellar systems’, Astron. J. 80, 1081–86. Astron. Astrophys. 322, 127–30.   
Hayli, A. [1967], ‘Le probl´eme des $N$ corps dans un champ ext´eriur. Application a l’´evolution dynamique des amas ouverts, I’, Bull. Astron. 2, 67–89. [1969], Contribution \`a l’Etude du Probl´eme Gravitationel des N Corps, Ph.D. Thesis (Paris University). [1970], ‘Numerical experiments on the escape from non-isolated clusters’, Astron. Astrophys. 7, 17–23. [1972], ‘Numerical experiments on the escape from non-isolated clusters and the formation of multiple stars’, in Gravitational N -Body Problem, ed. M. Lecar (Reidel, Dordrecht), 73–87. [1974], ‘The method of the doubly individual step for $N$ -body computations’, in Lecture Notes in Mathematics, ed. D. G. Bettis (Springer-Verlag, New York), 362, 304–12.   
Heggie, D. C. [1972a], ‘A multi-particle regularisation technique’, in Gravitational $N$ -Body Problem, ed. M. Lecar (Reidel, Dordrecht), 148–52. [1972b], Binary Evolution in Stellar Dynamics, Ph.D. Thesis (University of Cambridge). [1973], ‘Regularization using a time-transformation only’, in Recent Advances in Dynamical Astronomy, ed. B.D. Tapley & V. Szebehely (Reidel, Dordrecht), 34–7. [1974], ‘A global regularisation of the gravitational $N$ -body problem’, Celes. Mech. 10, 217–41. [1975], ‘Binary evolution in stellar dynamics’, Mon. Not. R. Astron. Soc. 173, 729–87. [1988], ‘The $N$ -body problem in stellar dynamics’, in Long-Term Dynamical Behaviour of Natural and Artificial $N$ -Body Systems, ed. A. E. Roy (Kluwer, Dordrecht), 329–47. [2000], ‘A new outcome of binary–binary scattering’, Mon. Not. R. Astron. Soc. 318, L61–L63. [2001], ‘Escape in Hill’s problem’, in The Restless Universe, ed. B. A. Steves & A. J. Maciejewski (Institute of Physics, Bristol), 109–28.   
Heggie, D. C. & Aarseth, S. J. [1992], ‘Dynamical effects of primordial binaries in star clusters, I. Equal masses’, Mon. Not. R. Astron. Soc. 257, 513– 36.   
Heggie, D. & Hut, P. [2003], The Gravitational Million-Body Problem (Cambridge University Press).   
Heggie, D. C. & Mathieu, R. D. [1986], ‘Standardised units and time scales’, in The Use of Supercomputers in Stellar Dynamics, ed. P. Hut & S. McMillan (Springer-Verlag, New York), 233–5.   
Heggie, D. C. & Ramamani, N. [1989], ‘Evolution of star clusters after core collapse’, Mon. Not. R. Astron. Soc. 237, 757–83. [1995], ‘Approximate self-consistent models for tidally truncated star clusters’, Mon. Not. R. Astron. Soc. 272, 317–22.   
Heggie, D. C., Hut, P. & McMillan, S. L. W. [1996], ‘Binary–single star scattering, VII. Hard binary exchange cross sections for arbitrary mass ratios: numerical results and semianalytical fits’, Astrophys. J. 467, 359–69. in an $N$ -body system’, Mon. Not. R. Astron. Soc. 271, 706–18.   
Heggie, D. C., Giersz, M., Spurzem, R. & Takahashi, K. [1998], ‘Dynamical simulations: methods and comparisons’, in Highlights of Astronomy, Vol. 11, ed. J. Andersen (Kluwer, Dordrecht), 591–6.   
Hemsendorf. M. & Merritt, D. [2002], ‘Instability of the gravitational $N$ -body problem in the large- $N$ limit’, Astrophys. J. 580, 606–9.   
Hemsendorf, M., Sigurdsson, S. & Spurzem, R. [2002], ‘Collisional dynamics around binary black holes in galactic centers’, Astrophys. J. 581, 1256– 70.   
H´enon, M. [1961], ‘Sur l’evolution dynamique des amas globulaires’, Ann. d’Astrophys. 24, 369–419. [1964], ‘L’evolution initial d’un amas spherique’, Ann. d’Astrophys. 27, 83–91. [1967], ‘Introduction’, Bull. Astron. 2, 45–6. [1968], ‘Collective motions in a spherical star cluster’, Bull. Astron. 3, 241– 63. [1969], ‘Rates of escape from isolated clusters with an arbitrary mass distribution’, Astron. Astrophys. 2, 151–61. [1972], ‘The Monte Carlo method’, in Gravitational $N$ -Body Problem, ed. M. Lecar (Reidel, Dordrecht), 406–22. [1975], ‘Two recent developments concerning the Monte Carlo Method’, in Dynamics of Stellar Systems, ed. A. Hayli (Reidel, Dordrecht), 133–49.   
Hernquist, L. [1987], ‘Performance characteristics of tree codes’, Astrophys. J. Suppl. 64, 715–34.   
Hernquist, L. & Ostriker, J. P. [1992], ‘A self-consistent field method for galactic dynamics’, Astrophys. J. 386, 375–97.   
Hills, J. G. [1970], ‘Dynamical relaxation of planetary systems and Bode’s Law’, Nature 225, 840–2. [1975], ‘Encounters between binary and single stars and their effect on the dynamical evolution of stellar systems’, Astron. J. 80, 809–25. [1983], ‘The effect of low-velocity, low-mass intruders on the dynamical evolution of a binary system’, Astron. J. 88, 1269–83. [1989], ‘Effect of intruder mass on collisions with hard binaries, I. Zero-impact parameters’, Astron. J. 97, 222–35. [1990], ‘Encounters between single and binary stars: the effect of intruder mass on the maximum impact velocity for which the mean change in binding energy is positive’, Astron. J. 99, 979–82. [1991], ‘Computer simulations of encounters between massive black holes and binaries’, Astron. J. 102, 704–75. [1992], ‘Effect of intruder mass on collisions with hard binaries, II. Dependence on impact parameter and computations of the interaction cross sections’, Astron. J. 103, 1955–69.   
Hills, J. G. & Day, C. A. [1976], ‘Stellar collisions in globular clusters’, Astrophys. Lett. 17, 87–93.   
Hills, J. G. & Fullerton, L. W. [1980], ‘Computer simulations of close encounters between single stars and hard binaries’, Astron. J. 85, 1281–91.   
Hoffer, J. B. [1983], ‘Computer simulations of gravitational encounters between pairs of binary star systems’, Astron. J. 88, 1420–34. eccentricity of the planet orbiting 16 Cygni B’, Nature 386, 254–6.   
Holmberg, E. [1941], ‘On the clustering tendencies among the nebulae, II. A study of encounters between laboratory models of stellar systems by a new integration procedure’, Astrophys. J. 94, 385–95.   
Hoogerwerf, R., de Bruijne, J. H. J. & de Zeeuw, P. T. [2000], ‘The origin of runaway stars’, Astrophys. J. 544, L133–L36. [2001], ‘On the origin of O and B-type stars with high velocities, II. Runaway stars and pulsars ejected from the nearby young stellar groups’, Astron. Astrophys. 365, 49–77.   
Hurley, J. R. [2000], Nuclear and Dynamical Evolution of Stellar Systems, Ph.D. Thesis (University of Cambridge).   
Hurley, J. R. & Shara, M. M. [2002], ‘Free-floating planets in stellar clusters: not so surprising’, Astrophys. J. 565, 1251–6. [2003], ‘White dwarf sequences in dense star clusters’, Astrophys. J. 589, 179–98.   
Hurley, J. R., Pols, O. R. & Tout, C. A. [2000], ‘Comprehensive analytical formulae for stellar evolution as a function of mass and metallicity’, Mon. Not. R. Astron. Soc. 315, 543–69.   
Hurley, J. R., Tout, C. A. & Pols, O. R. [2002], ‘Evolution of binary stars and the effect of tides on binary populations’, Mon. Not. R. Astron. Soc. 329, 897–928.   
Hurley, J. R., Tout, C. A., Aarseth, S. J. & Pols, O. R. [2001a], ‘Direct $N .$ -body modelling of stellar populations: blue stragglers in M67’, Mon. Not. R. Astron. Soc. 323, 630–50.   
Hurley, J. R., Aarseth, S. J., Tout, C. A., Gilmore, G. & Pols, O. R. [2001b], ‘On the road to realistic globular cluster models’, in Dynamics of Star Clusters and the Milky Way, ed. S. Deiters, B. Fuchs, A. Just, R. Spurzem & R. Wielen (ASP, San Francisco), 228, 452–4.   
Hut, P. [1981], ‘Tidal evolution in close binary systems’, Astron. Astrophys. 99, 126–40. [1983], ‘Binary–single star scattering, II. Analytic approximations for high velocity’, Astrophys. J. 268, 342–55. [1992], ‘New directions in globular cluster modeling’, in X-Ray Binaries and Recycled Pulsars, ed. E. P. J. van den Heuvel & S. A. Rappaport (Kluwer, Dordrecht), 317–48. [1993], ‘Binary–single star scattering, III. Numerical experiments for equalmass hard binaries’, Astrophys. J. 403, 256–70.   
Hut, P. & Bahcall, J. N. [1983], ‘Binary–single star scattering, I. Numerical experiments for equal masses’, Astrophys. J. 268, 319–41.   
Hut, P., Makino, J. & McMillan, S. [1995], ‘Building a better leapfrog’, Astrophys. J. 443, L93–L96.   
Hut, P., McMillan, S., Goodman, J., Mateo, M., Phinney, E. S., Pryor, C., Richer, H. B., Verbunt, F. & Weinberg, M. [1992], ‘Binaries in globular clusters’, Publ. Astron. Soc. Pacific 104, 981–1034.   
Hut, P., Shara, M. M., Aarseth, S. J., Klessen, R. S., Lombardi, J. C., Makino, J., McMillan, S., Pols, O. R., Teuben, P. J. & Webbink, R. F. [2003], ‘MODEST-1: integrating stellar evolution and stellar dynamics’, New. Astron. 8, 337–70. between planetesimals and a protoplanet, II. Dynamical friction’, Icarus 98, 28–37.   
Inagaki, S. [1986], ‘Post-collapse evolution of globular clusters with finite number of stars in the core’, Publ. Astron. Soc. Japan 38, 853–63.   
Inagaki, S. & Saslaw, W. C. [1985], ‘Equipartition in multicomponent gravitational systems’, Astrophys. J. 292, 339–47.   
Ito, T. & Tanikawa, K. [2002], ‘Long-term integrations and stability of planetary orbits in our Solar System’, Mon. Not. R. Astron. Soc. 336, 483– 500.   
Itoh, M., Inagaki, S. & Saslaw, W. C. [1988], ‘Gravitational clustering of galaxies: comparison between thermodynamic theory and $N$ -body simulations’, Astrophys. J. 331, 45–63. [1990], ‘Gravitational clustering of galaxies: comparison of thermodynamic theory and $N .$ -body simulations, II. The effects of different mass components’, Astrophys. J. 356, 315–31.   
Jeans, J. H. [1929], Astronomy and Cosmogony (Cambridge University Press).   
Jernigan, J. G. & Porter, D. H. [1989], ‘A tree code with logarithmic reduction of force terms, hierarchical regularization of all variables, and explicit accuracy controls’, Astrophys. J. Suppl. 71, 871–93.   
Jha, S., Torres, G., Stefanik, R. P., Latham, D. W. & Mazeh, T. [2000], ‘Studies of multiple stellar systems, III. Modulation of orbital elements in the triplelined system HD 109648’, Mon. Not. R. Astron. Soc. 317, 375–84.   
Johnson, J. A., Bolte, M., Stetson, P. B., Hesser, J. E. & Sommerville, R. S. [1999], ‘Hubble Space Telescope observations of the oldest star clusters in the Large Magellanic Cloud’, Astrophys. J. 527, 199–218.   
Johnstone, D. & Rucinski, S. M. [1991], ‘Statistical properties of planar zeroangular-momentum equal-mass triple systems’, Publ. Astron. Soc. Pacific 103, 359–67.   
Jones, B. F. [1970], ‘Internal motions in the Pleiades’, Astron. J. 75, 563–74.   
Joshi, K. J., Rasio, F. A. & Portegies Zwart, S. [2000], ‘Monte Carlo simulations of globular cluster evolution, I. Method and test calculations’, Astrophys. J. 540, 969–82.   
Kandrup, H. E. & Smith, H. [1991], ‘On the sensitivity of the $N$ -body problem to small changes in initial conditions’, Astrophys. J. 374, 255–65.   
Kim, S. S., Figer, D. F., Lee, H. M. & Morris, M. [2000], ‘ $N$ -body simulations of compact young clusters near the Galactic center’, Astrophys. J. 545, 301–8.   
Kim, E., Einsel, C., Lee, H. M., Spurzem, R. & Lee, M. G. [2002], ‘Dynamical evolution of rotating stellar systems, II. Post-collapse, equal-mass system’, Mon. Not. R. Astron. Soc. 334, 310–22.   
King, I. [1958], ‘The escape of stars from clusters, I. Calculation for a centrally concentrated model’, Astron. J. 63, 109–13. [1962], ‘The structure of star clusters, I. An empirical density law’, Astron. J. 67, 471–85. [1966], ‘The structure of star clusters, III. Some simple dynamical models’, Astron. J. 71, 64–75.   
Kiseleva, L. G. & Eggleton, P. P. [1999], ‘Tidal friction in triple systems: a means of producing close stellar and planetary orbits’, in The Dynamics of Small Bodies in the Solar System, ed. B. A. Steves & A. E. Roy (Kluwer, Dordrecht), 399–406.   
Kiseleva, L., Aarseth, S., Eggleton, P. & de la Fuente Marcos, R. [1996], ‘Formation and evolution of hierarchical triple systems in open clusters’, in The Origins, Evolution, and Destinies of Binary Stars in Clusters, ed. E. F. Milone & J.-C. Mermilliod (ASP, San Francisco), 433–5.   
Kiseleva, L. G., Colin, J., Dauphole, B. & Eggleton, P. [1998], ‘High-velocity stars from decay of small stellar systems’, Mon. Not. R. Astron. Soc. 301, 759–66.   
Kochanek, C. S. [1992], ‘The dynamical evolution of tidal capture binaries’, Astrophys. J. 385, 604–20.   
Kokubo, E. & Ida, S. [1995], ‘Orbital evolution of protoplanets embedded in a swarm of planetesimals’, Icarus 114, 247–57. [1996], ‘On runaway growth of planetesimals’, Icarus 123, 180–91. [1998], ‘Oligarchic growth of planetesimals’, Icarus 131, 171–8. [2000], ‘Formation of protoplanets from planetesimals in the solar nebula’, Icarus 143, 15–27.   
Kokubo, E., Yoshinaga, K. & Makino, J. [1998], ‘On a time-symmetric Hermite integrator for planetary $N$ -body simulation’, Mon. Not. R. Astron. Soc. 297, 1067–72.   
Kong, K. N. & Lee, H. M. [1995], ‘Effects of gravitational radiation on three-body interactions of 10 $M _ { \odot }$ black holes’, J. Kor. Phys. Soc. 28, S530–S35.   
Kozai, Y. [1962], ‘Secular perturbations of asteroids with high inclination and eccentricity’, Astron. J. 67, 591–8.   
Krantzman, K. D., Milligan, J. A. & Farrelly, D. [1992], ‘Semiclassical mechanics of the quadratic Zeeman effect’, Phys. Rev. A45, 3093–03.   
Kroupa, P. [1995a], ‘Inverse dynamical population synthesis and star formation’, Mon. Not. R. Astron. Soc. 277, 1491–506. [1995b], ‘The dynamical properties of stellar systems in the Galactic disc’, Mon. Not. R. Astron. Soc. 277, 1507–21. [1995c], ‘Star cluster evolution, dynamical age estimation and the kinematical signature of star formation’, Mon. Not. R. Astron. Soc. 277, 1522–40. [1998], ‘On the binary properties and the spatial and kinematical distribution of young stars’, Mon. Not. R. Astron. Soc. 298, 231–42. [2000], ‘Constraints on stellar-dynamical models of the Orion nebula cluster’, New Astron. 4, 615–24. [2001a], ‘On the variation of the initial mass function’, Mon. Not. R. Astron. Soc. 322, 231–46. [2001b], ‘The local stellar initial mass function’, in Dynamics of Star Clusters and the Milky Way, ed. S. Deiters, B. Fuchs, A. Just, R. Spurzem & R. Wielen (ASP, San Francisco), 228, 187–200.   
Kroupa, P., Aarseth, S. J. & Hurley, J. [2001], ‘The formation of a bound star cluster: from the Orion Nebula cluster to the Pleiades’, Mon. Not. R. Astron. Soc. 321, 699–712.   
Kroupa, P., Petr, M. G. & McCaughrean, M. J. [1999], ‘Binary stars in young clusters: models versus observations of the Trapezium Cluster’, New Astron. 4, 495–520.   
Kroupa, P., Tout, C. A. & Gilmore, G. [1993], ‘The distribution of low-mass stars in the Galactic disc’, Mon. Not. R. Astron. Soc. 262, 545–87.   
Kuberka, T., Kugel, A. M¨anner, R., Singpiel, H., Spurzem, R. & Klessen, R. [1999], ‘AHA-GRAPE: Adaptive Hydrodynamic Architechture – GRAvity PipE’, in Lecture Notes in Computer Science, ed. P. Lysaght, J. Irvine & R. Hartenstein (Springer-Verlag, New York), 1673, 417–24.   
Kudritzki, R. P. & Reimers, D. [1978], ‘On the absolute scale of mass-loss in red giants’, Astron. Astrophys. 70, 227–39.   
Kuijken, K. & Gilmore, G. [1989], ‘The mass distribution in the Galactic disc, III. The local volume mass density’, Mon. Not. R. Astron. Soc. 239, 651–64.   
Kumar, P. & Goodman, J. [1996], ‘Nonlinear damping of oscillations in tidalcapture binaries’, Astrophys. J. 466, 946–56.   
Kustaanheimo, P. & Stiefel, E. [1965], ‘Perturbation theory of Kepler motion based on spinor regularization’, J. Reine Angew. Math. 218, 204–19.   
Kwan, J. & Valdes, F. [1987], ‘The spatial and mass distributions of molecular clouds and spiral structure’, Astrophys. J. 315, 92–103.   
Lada, C. J., Margulis, M. & Dearborn, D. [1984], ‘The formation and early dynamical evolution of bound stellar systems’, Astrophys. J. 285, 141–52.   
Lai, D. [1997], ‘Dynamical tides in rotating binary stars’, Astrophys. J. 490, 847–62.   
Lang, K. R. [1992], Astrophysical Data: Planets and Stars (Springer-Verlag, Berlin).   
Larson, R. B. [1970], ‘A method for computing the evolution of star clusters’, Mon. Not. R. Astron. Soc. 147, 323–37.   
Laskar, J. [1994], ‘Large scale chaos in the Solar System’, Astron. Astrophys. 287, L9–L12. [1997], ‘Large scale chaos and the spacing of the inner planets’, Astron. Astrophys. 317, L75–L78. [2000], ‘On the spacing of planetary systems’, Phys. Rev. Lett. 84, 3240–3.   
Laughlin, G. & Adams, F. C. [1998], ‘The modification of planetary orbits in dense open clusters’, Astrophys. J. 508, L171–L74. [1999], ‘Stability and chaos in the $\upsilon$ Andromedae planetary system’, Astrophys. J. 526, 881–9.   
Laughlin, G. & Chambers, J. E. [2001], ‘Short-term dynamical interactions among extrasolar planets’, Astrophys. J. 551, L109–L13.   
Lecar, M. [1968], ‘A comparison of eleven numerical integrations of the same gravitational 25-body problem’, Bull. Astron. 3, 91–104.   
Lecar, M. & Aarseth, S. J. [1986], ‘A numerical simulation of the formation of the terrestrial planets’, Astrophys. J. 305, 564–79.   
Lecar, M. & Cohen, L. [1972], ‘Numerical experiments on Lynden-Bell’s statistics’, in Gravitational $N$ -Body Problem, ed. M. Lecar (Reidel, Dordrecht), 262–75. times in stellar dynamics’, in Gravitational $N$ -Body Problem, ed. M. Lecar (Reidel, Dordrecht), 131–5.   
Lecar, M. & Franklin, F. A. [1973], ‘On the original distribution of the asteroids, I’, Icarus 20, 422–36.   
Lecar, M., Loeser, R., & Cherniack, J. R. [1974], ‘Numerical integration of gravitational $N$ -body systems with the use of explicit Taylor series’, in Lecture Notes in Mathematics, ed. D. G. Bettis (Springer-Verlag, New York), 362, 451–70.   
Lecar, M., Franklin, F. A., Holman, M. J. & Murray, N. W. [2001], ‘Chaos in the Solar System’, Ann. Rev. Astron. Astrophys. 39, 581–631.   
Lee, H. M., Fahlman, G. B. & Richer, H. B. [1991], ‘Multicomponent models for the dynamic evolution of globular clusters’, Astrophys. J. 366, 455–63.   
Lee, M. H. [1993], $N$ -body evolution of dense clusters of compact stars’, Astrophys. J. 418, 147–62.   
Leinhardt, Z. M. & Richardson, D. C. [2002], $N$ -body simulations of planetesimal evolution: effect of varying impactor mass ratio’, Icarus 159, 306–13.   
Leinhardt, Z. M., Richardson, D. C. & Quinn, T. [2000], ‘Direct $N$ -body simulations of rubble pile collisions’, Icarus 146, 133–51.   
Lemaˆitre, G. [1955], ‘Regularization of the three-body problem’, Vistas Astron. 1, 207–15.   
Leonard, P. J. T. [1988], The Dynamics of Open Star Clusters, Ph.D. Thesis (University of Toronto). [1989], ‘Stellar collisions in globular clusters and the blue straggler problem’, Astron. J. 98, 217–26. [1991], ‘The maximum possible velocity of dynamically ejected runaway stars’, Astron. J. 101, 562–71. [1995], ‘Merged dynamically ejected OB runaway stars’, Mon. Not. R. Astron. Soc. 277, 1080–6. [1996], ‘The implications of the binary properties of the M67 blue stragglers’, Astrophys. J. 470, 521–7.   
Leonard, P. J. T. & Duncan, M. J. [1988], ‘Runaway stars from young star clusters containing initial binaries, I. Equal-mass, equal-energy binaries’, Astron. J. 96, 222–32. [1990], ‘Runaway stars from young star clusters containing initial binaries, II. A mass spectrum and a binary energy spectrum’, Astron. J. 99, 608–16.   
Leonard, P. J. T. & Linnell, A. P. [1992], ‘On the possibility of a collisional origin for the blue stragglers and contact binaries in the old open clusters M67 and NGC 188’, Astron. J. 103, 1928–44.   
Levi-Civita, T. [1920], ‘Sur la r´egularisation du probl\`eme des trois corps’, Acta Math. 42, 99–44.   
Levison, H. F. & Duncan, M. J. [1994], ‘The long-term dynamical behaviour of short-period comets’, Icarus 108, 18–36.   
Lissauer, J. J & Rivera, E. J. [2001], ‘Stability analysis of the planetary system orbiting $\upsilon$ Andromedae, II. Simulations using new Lick Observatory fits’, Astrophys. J. 554, 1141–50.   
Lombardi, J. C., Rasio, F. A. & Shapiro, S. L. [1996], ‘Collisions of main-sequence stars and the formation of blue stragglers in globular clusters’, Astrophys. J. 468, 797–818.   
Louis, P. D. & Spurzem, R. [1991], ‘Anisotropic gaseous models for the evolution of star clusters’, Mon. Not. R. Astron. Soc. 251, 408–26.   
Lupton, R. H. & Gunn, J. E. [1987], ‘Three-integral models of globular clusters’, Astron. J. 93, 1106–13.   
Lynden-Bell, D. [1967], ‘Statistical mechanics of violent relaxation in stellar systems’, Mon. Not. R. Astron. Soc. 136, 101–21.   
Lynden-Bell, D. & Eggleton, P. P. [1980], ‘On the consequences of the gravothermal catastrophe’, Mon. Not. R. Astron. Soc. 191, 483–98.   
Magorrian, J. & Tremaine, S. [1999], ‘Rates of tidal disruption of stars by massive central black holes’, Mon. Not. R. Astron. Soc. 309, 447–60.   
Makino, J. [1990], ‘Comparison of two different tree algorithms’, J. Comput. Phys. 88, 393–408. [1991a], ‘Optimal order and time-step criterion for Aarseth-type $N$ -body integrators’, Astrophys. J. 369, 200–12. [1991b], ‘A modified Aarseth code for GRAPE and vector processors’, Publ. Astron. Soc. Japan 43, 859–76. [1996a], ‘Gravothermal oscillations’, in Dynamical Evolution of Star Clusters, ed. P. Hut & J. Makino (Kluwer, Dordrecht), 151–60. [1996b], ‘Postcollapse evolution of globular clusters’, Astrophys. J. 471, 796– 803. [1997], ‘Merging of galaxies with central black holes, II. Evolution of the black hole binary and the structure of the core’, Astrophys. J. 478, 58– 65. [2002], ‘An efficient parallel algorithm for O( $N ^ { 2 }$ ) direct summation method and its variations on distributed-memory parallel machines’, New Astron. 7, 373–84. [2003], ‘The GRAPE project: current status and future outlook’, in Astrophysical Supercomputing Using Particle Simulations, ed. P. Hut & J. Makino (ASP, San Francisco), 13–24.   
Makino, J. & Aarseth, S. J. [1992], ‘On a Hermite integrator with Ahmad–Cohen scheme for gravitational many-body problems’, Publ. Astron. Soc. Japan 44, 141–51.   
Makino, J. & Ebisuzaki, T. [1996], ‘Merging of galaxies with central black holes, I. Hierarchical mergings of equal-mass galaxies’, Astrophys. J. 465, 527–33.   
Makino, J. & Fukushige, T. [2002], ‘A 11.55 Tflops simulation of black holes in a galactic center on GRAPE-6’, Gordon Bell Prize, in Proceedings IEE/ACM SC2002 Conference, (CD-ROM).   
Makino, J. & Hut, P. [1988], ‘Performance analysis of direct $N$ -body calculations’, Astrophys. J. Suppl. 68, 833–56. [1990], ‘Bottlenecks in simulations of dense stellar systems’, Astrophys. J. 365, 208–18.   
Makino, J. & Sugimoto, D. [1987], ‘Effect of suprathermal particles on gravothermal oscillation’, Publ. Astron. Soc. Japan 39, 589–603.   
Makino, J. & Taiji, M. [1998], Scientific Simulations with Special-Purpose Computers: The GRAPE systems (John Wiley & Sons, Chichester).   
Makino, J., Fukushige, T. & Namura, K. [2003], ‘GRAPE-6: the massivelyparallel special-purpose computer for astrophysical particle simulations’, Publ. Astron. Soc. Japan, submitted.   
Makino, J., Kokubo, E. & Taiji, M. [1993], ‘HARP: a special-purpose computer for $N$ -body problem’, Publ. Astron. Soc. Japan 45, 349–60.   
Makino, J., Tanekusa, J. & Sugimoto, D. [1986], ‘Gravothermal oscillation in gravitational many-body systems’, Publ. Astron. Soc. Japan 38, 865–77.   
Makino, J., Taiji, M., Ebisuzaki, T. & Sugimoto, D. [1997], ‘GRAPE-4: a massively parallel special-purpose computer for collisional $N$ -body simulations’, Astrophys. J. 480, 432–46.   
Mann, P. J. [1987], ‘Finite difference methods for the classical particle–particle gravitational $N$ -body problem’, Comp. Phys. Comm. 47, 213–28.   
Marchal, C., Yoshida, J. & Sun, Y.-S. [1984], ‘A test of escape valid even for very small mutual distances, I. The acceleration and the escape velocities of the third body’, Celes. Mech. 33, 193–207.   
Mardling, R. A. [1991], Chaos in Binary Star Systems, Ph.D. Thesis (Monash University).   
[1995a], ‘The role of chaos in the circularization of tidal capture binaries, I. The chaos boundary’, Astrophys. J. 450, 722–31.   
[1995b], ‘The role of chaos in the circularization of tidal capture binaries, II. Long-time evolution’, Astrophys. J. 450, 732–47. [1996a], ‘Tidal capture binaries in clusters: the chaos model for tidal evolution’, in The Origins, Evolution, and Destinies of Binary Stars in Clusters, ed. E. F. Milone & J.-C. Mermilliod (ASP, San Francisco), 399–408. [1996b], ‘Chaos and tidal capture’, in Evolutionary Processes in Binary Stars, ed. R. A. M. J. Wijers, M. B. Davies & C. A. Tout (Kluwer, Dordrecht), 81–99.   
[1996c], ‘Tidal capture in star clusters’, in Dynamical Evolution of Star Clusters, ed. P. Hut & J. Makino (Kluwer, Dordrecht), 273–82.   
[2001], ‘Stability in the general three-body problem’, in Evolution of Binary and Multiple Star Systems; A Meeting in Celebration of Peter Eggleton’s 60th Birthday, ed. P. Podsiadlowski, S. Rappaport, A. R. King, F. D’Antona & L. Burderi (ASP, San Francisco), 229, 101–16.   
[2003a], ‘A new formalism for studying three-body interactions’, in Astrophysical Supercomputing using Particle Simulations, ed. J. Makino & P. Hut (ASP, San Francisco), 123–30.   
[2003b], ’A new three-body formalism’, in preparation.   
Mardling, R. & Aarseth, S. [1999], ‘Dynamics and stability of three-body systems’, in The Dynamics of Small Bodies in the Solar System, ed. B. A. Steves & A. E. Roy (Kluwer, Dordrecht), 385–92. [2001], ‘Tidal interactions in star cluster simulations’, Mon. Not. R. Astron. Soc. 321, 398–420.   
Mardling, R. A. & Lin, D. N. C. [2002], ‘Calculating the tidal, spin, and dynamical evolution of extrasolar planetary systems’, Astrophys. J. 573, 829–44. [2003], ‘On the interaction between three planets and their host star Upsilon Andromedae’, Astrophys. J. , submitted.   
Mathieu, R. D. [1983], The Structure, Internal Kinematics and Dynamics of Open Star Clusters, Ph.D. Thesis (University of California, Berkeley).   
Mathieu, R. D., Latham, D. W. & Griffin, R. F. [1990], ‘Orbits of 22 spectroscopic binaries in the open cluster M67’, Astron. J. 100, 1859–81.   
Mazeh, T. [1990], ‘Eccentric orbits in samples of circularized binary systems: the fingerprint of a third star’, Astron. J. 99, 675–7.   
McCrea, W. H. [1964], ‘Extended main-sequence of some clusters’, Mon. Not. R. Astron. Soc. 128, 147–55.   
McMillan, S. L. W. [1986], ‘The vectorization of small- $N$ integrators’, in The Use of Supercomputers in Stellar Dynamics, ed. P. Hut & S. McMillan (Springer-Verlag, New York), 156–61.   
McMillan, S. L. W. & Aarseth, S. J. [1993], ‘An $O ( N \log N )$ integration scheme for collisional stellar systems’, Astrophys. J. 414, 200–12.   
McMillan, S. L. W. & Hut. P. [1994], ‘Star cluster evolution with primordial binaries, III. Effect of the galactic tidal field’, Astrophys. J. 427, 793– 807. [1996], ‘Binary–single-star scattering, VI. Automatic determination of interaction cross sections’, Astrophys. J. 467, 348–58.   
McMillan, S. L. W. & Lightman, A. P. [1984a], ‘A unified $N$ -body and statistical treatment of stellar dynamics, I. The hybrid code’, Astrophys. J. 283, 801–12. [1984b], ‘A unified $N$ -body and statistical treatment of stellar dynamics, II. Applications to globular cluster cores’, Astrophys. J. 283, 813–24.   
McMillan, S., Hut. P. & Makino, J. [1990], ‘Star cluster evolution with primordial binaries, I. A comparative study’, Astrophys. J. 362, 522–37. [1991], ‘Star cluster evolution with primordial binaries, II. Detailed analysis’, Astrophys. J. 372, 111–24.   
Mermilliod, J.-C. & Mayor, M. [1992], ‘Distribution of orbital elements for red giant spectroscopic binaries in open clusters’, in Binaries as Tracers of Stellar Formation, ed. A. Duquennoy & M. Mayor (Cambridge University Press), 183–201.   
Merritt, D. [1996], ‘Optimal smoothing for $N$ -body codes’, Astron. J. 111, 2462–4.   
Merritt, D. & Quinlan, G. D. [1998], ‘Dynamical evolution of elliptical galaxies with central singularities’, Astrophys. J. 498, 625–39.   
Meusinger, H., Scholz, R. D. & Irwin, M. J. [2001], ‘A proper motion search for stars escaping from a globular cluster with high velocity’, in Dynamics of Star Clusters and the Milky Way, ed. S. Deiters, B. Fuchs, A. Just, R. Spurzem & R. Wielen (ASP, San Francisco), 228, 520–2.   
Meylan, G. & Heggie, D. C. [1997], ‘Internal dynamics of globular clusters’, Astron. Astrophys. Rev. 8, 1–143.   
Michie, R. W. [1963], ‘On the distribution of high energy stars in spherical stellar systems’, Mon. Not. R. Astron. Soc. 125, 127–39.   
Mikkola, S. [1983], ‘Encounters of binaries, I. Equal energies’, Mon. Not. R. Astron. Soc. 203, 1107–21. [1984a], Dynamics of Interacting Binaries, Ph.D. Thesis (University of Turku). [1984b], ‘Encounters of binaries, II. Unequal energies’, Mon. Not. R. Astron. Soc. 207, 115–26. [1984c], ‘Encounters of binaries, III. Fly-bys’, Mon. Not. R. Astron. Soc. 208, 75–82. [1985a], ‘A practical and regular formulation of the $N$ -body equations’, Mon. Not. R. Astron. Soc. 215, 171–7. [1985b], ‘Numerical simulations of encounters of hard binaries’, in Dynamics of Star Clusters, ed. J. Goodman & P. Hut (Reidel, Dordrecht), 335–8. [1988], ‘On the effects of unequal masses in the statistics of three- and fourbody interactions’, in The Few Body Problem, ed. M. J. Valtonen (Reidel, Dordrecht), 261–4. [1994], ‘A numerical exploration of the phase-space structure of chaotic threebody scattering’, Mon. Not. R. Astron. Soc. 269, 127–36. [1997a], ‘Practical symplectic methods with time transformation for the fewbody problem’, Celes. Mech. Dyn. Ast. 67, 145–65. [1997b], ‘Numerical treatment of small stellar systems with binaries’, Celes. Mech. Dyn. Ast. 68, 87–104.   
Mikkola, S. and Aarseth, S. J. [1990], ‘A chain regularization method for the few-body problem’, Celes. Mech. Dyn. Ast. 47, 375–90. [1993], ‘An implementation of $N$ -body chain regularization’, Celes. Mech. Dyn. Ast. 57, 439–59. [1996], ‘A slow-down treatment for close binaries’, Celes. Mech. Dyn. Ast. 64, 197–208. [1998], ‘An efficient integration method for binaries in $N$ -body simulations’, New Astron. 3, 309–20. [2002], ‘A time-transformed leapfrog scheme’, Celes. Mech. Dyn. Ast. 84, 343– 54.   
Mikkola, S. & Hietarinta, J. [1989], ‘A numerical investigation of the onedimensional Newtonian three-body problem’, Celes. Mech. Dyn. Ast. 46, 1–18. [1990], ‘A numerical investigation of the one-dimensional Newtonian threebody problem, II. Positive energies’, Celes. Mech. Dyn. Ast. 47, 321– 31. [1991], ‘A numerical investigation of the one-dimensional Newtonian threebody problem, III. Mass dependence in the stability of motion’, Celes. Mech. Dyn. Ast. 51, 379–94.   
Mikkola, S. & Innanen, K. [1995], ‘Solar system chaos and the distribution of asteroid orbits’, Mon. Not. R. Astron. Soc. 277, 497–501.   
Mikkola, S. & Saha, P. [2003], Numerical Celestial Mechanics (Kluwer, Dordrecht), in preparation.   
Mikkola, S. & Tanikawa, K. [1999a], ‘Explicit symplectic algorithms for timetransformed Hamiltonians’, Celes. Mech. Dyn. Ast. 74, 287–95. [1999b], ‘Algorithmic regularization of the few-body problem’, Mon. Not. R. Astron. Soc. 310, 745–9.   
Miller, M. C. & Hamilton, D. C. [2002], ‘Four-body effects in globular cluster black hole coalescence’, Astrophys. J. 576, 894–8.   
Miller, R. H. [1964], ‘Irreversibility in small stellar dynamical systems’, Astrophys. J. 140, 250–6. [1974], ‘Numerical difficulties with the gravitational $N$ -body problem’, in Lecture Notes in Mathematics, ed. D. G. Bettis (Springer-Verlag, New York), 362, 260–75.   
Milosavljevi´c, M. & Merritt, D. [2001], ‘Formation of galactic nuclei’, Astrophys. J. 563, 34–62.   
Miyamoto, M. & Nagai, R. [1975], ‘Three-dimensional models for the distribution of mass in galaxies’, Publ. Astron. Soc. Japan 27, 533–43.   
Monaghan, J. J. [1976], ‘A statistical theory of the disruption of three-body systems, II. High angular momentum’, Mon. Not. R. Astron. Soc. 177, 583–94.   
Montgomery, K. A., Marschall, L. A. & Janes, K. A. [1993], ‘CCD photometry of the old open cluster M67’, Astron. J. 106, 181–219.   
Murray, C. D. & Dermott, S. F. [1999], Solar System Dynamics (Cambridge University Press).   
Nacozy, P. E. [1972], ‘The use of integrals in numerical integrations of the $N$ -body problem’, in Gravitational N-Body Problem, ed. M. Lecar (Reidel, Dordrecht), 153–64.   
Nakano, T. & Makino, J. [1999], ‘On the origin of density cusps in elliptical galaxies’, Astrophys. J. 510, 155–66.   
Nash, P. E. & Monaghan, J. J. [1978], ‘A statistical theory of the disruption of three-body systems, III. Three-dimensional motion’, Mon. Not. R. Astron. Soc. 184, 119–25.   
Oh, K. S., Lin, D. N. C. & Aarseth, S. J. [1992], ‘Tidal evolution of globular clusters, I. Method’, Astrophys. J. 386, 506–18. [1995], ‘On the tidal disruption of dwarf spheroidal galaxies around the Galaxy’, Astrophys. J. 442, 142–58.   
Oort, J. H. [1965], ‘Stellar dynamics’, in Galactic Structure, ed. A. Blaauw & M. Schmidt (University of Chicago Press), 455–511.   
Ostriker, J. P., Spitzer, L. & Chevalier, R. A. [1972], ‘On the evolution of globular clusters’, Astrophys. J. 176, L51–L56.   
Paczynski, B. [1976], ‘Common envelope binaries’, in Structure and Evolution of Close Binary Systems, ed. P. Eggleton, S. Mitton & J. Whelan, (Reidel, Dordrecht), 75–9.   
Palmer, P. L., Lin, D. N. C. & Aarseth, S. J. [1992], ‘Evolution of planetesimals, I. Dynamics: relaxation in a thin disk’, Astrophys. J. 403, 336–50.   
Palmer, P. L., Aarseth, S. J., Mikkola, S. & Hashida, Y. [1998], ‘High precision integration methods for orbit propagation’, J. Astronaut. Sci. 46, 329–42.   
Peters, C. F. [1968a], Treatment of Close Approaches in Stellar Dynamics, Ph.D. Thesis (Yale University). [1968b], ‘Numerical Regularization’, Bull. Astron. 3, 167–75.   
Peters, P. C. [1964], ‘Gravitational radiation and the motion of two point masses’, Phys. Rev. 136, B1224–32.   
Pfahl, E., Rappaport, S. & Podsiadlowski, P. [2002], ‘A comprehensive study of neutron star retention in globular clusters’, Astrophys. J. 573, 283–305.   
Pfahl, E., Rappaport, S., Podsiadlowski, P. & Spruit, H. [2002], ‘A new class of high-mass X-ray binaries: implications for core collapse and neutron star recoil’, Astrophys. J. 574, 364–76.   
Plummer, H. C. [1911], ‘On the problem of distribution in globular star clusters’, Mon. Not. R. Astron. Soc. 71, 460–70.   
Podsiadlowski, P. [1996], ‘The response of tidally heated stars’, Mon. Not. R. Astron. Soc. 279, 1104–10.   
Portegies Zwart, S. F. [1996], Interacting Stars, Ph.D. Thesis (University of Utrecht).   
Portegies Zwart, S. F. & McMillan, S. L. W. [2002], ‘The runaway growth of intermediate-mass black holes in dense star clusters’, Astrophys. J. 576, 899–907.   
Portegies Zwart, S. F. & Meinen, A. T. [1993], ‘Quick method for calculating energy dissipation in tidal interaction’, Astron. Astrophys. 280, 174–6.   
Portegies Zwart, S. F. & Verbunt, F. [1996], ‘Population synthesis of high-mass binaries’, Astron. Astrophys. 309, 179–96.   
Portegies Zwart, S. F., Hut, P., McMillan, S. L. W. & Verbunt, F. [1997], ‘Star cluster ecology, II. Binary evolution with single-star encounters’, Astron. Astrophys. 328, 143–57.   
Portegies Zwart, S. F., Hut, P., Makino, J. & McMillan, S. L. W. [1998], ‘On the dissolution of evolving star clusters’, Astron. Astrophys. 337, 363–71.   
Portegies Zwart, S. F., Makino, J., McMillan, S. L. W. & Hut, P. [1999], ‘Star cluster ecology, III. Runaway collisions in young compact star clusters’, Astron. Astrophys. 348, 117–26.   
Portegies Zwart, S. F., McMillan, S. L. W., Hut, P. & Makino, J. [2001], ‘Star cluster ecology, IV. Dissection of an open star cluster: photometry’, Mon. Not. R. Astron. Soc. 321, 199–226.   
Portegies Zwart, S. F., Makino, J., McMillan, S. L. W. & Hut, P. [2002], ‘The lives and deaths of star clusters near the Galactic center’, Astrophys. J. 565, 265–79.   
Poveda, A., Ruiz, J. & Allen, C. [1967], ‘Run-away stars as the result of the gravitational collapse of proto-stellar clusters’, Bol. Obs. Tonantzintla $y$ Tacubaya 28, 86–90.   
Press, W. H. [1986], ‘Techniques and tricks for $N$ -body computation’, in The Use of Supercomputers in Stellar Dynamics, ed. P. Hut & S. McMillan (Springer-Verlag, New York), 184–92.   
Press, W. H. & Spergel, D. N. [1988], ‘Choice of order and extrapolation method in Aarseth-type $N$ -body algorithms’, Astrophys. J. 325, 715–21.   
Press, W. H. & Teukolsky, S. [1977], ‘On the formation of close binaries by two-body tidal capture’, Astrophys. J. 213, 183–92.   
Preto, M. & Tremaine, S. [1999], ‘A class of symplectic integrators with adaptive time step for separable Hamiltonian systems’, Astron. J. 118, 2532– 41.   
Pryor, C., McClure, R. D., Hesser, J. E. & Fletcher, J. M. [1989], ‘The frequency of primordial binary stars’, in Dynamics of Dense Stellar Systems, ed. D. Merritt (Cambridge University Press), 175–81.   
Quinlan, G. D. & Hernquist, L. [1997], ‘The dynamical evolution of massive black hole binaries, II. Self-consistent $N$ -body integrations’, New Astron. 2, 533–54.   
Quinlan, G. D. & Tremaine, S. [1990], ‘Symmetric multistep methods for the numerical integration of planetary orbits’, Astron. J. 100, 1694–700. [1992], ‘On the reliability of gravitational $N$ -body integrations’, Mon. Not. R. Astron. Soc. 259, 505–18.   
Raboud, R. & Mermilliod, J.-C. [1998a], ‘Investigation of the Pleiades cluster, IV. The radial structure’, Astron. Astrophys. 329, 101–14. [1998b], ‘Evolution of mass segregation in open clusters: some observational evidences’, Astron. Astrophys. 333, 897–909.   
Rasio, F. A., McMillan, S. & Hut, P. [1995], ‘Binary–binary interactions and the formation of the PSR B1620–26 triple system in M4’, Astrophys. J. 438, L33–L36.   
Richardson, D. C. [1993a], Planetesimal Dynamics, Ph.D. Thesis (University of Cambridge). [1993b], ‘A new tree code method for simulation of planetesimal dynamics’, Mon. Not. R. Astron. Soc. 261, 396–414. [1994], ‘Tree code simulations of planetary rings’, Mon. Not. R. Astron. Soc. 269, 493–511. [1995], ‘A self-consistent numerical treatment of fractal aggregate dynamics’, Icarus 115, 320–35.   
Richardson, D. C., Asphaug. E. & Benner, L. [1995], ‘Comet Shoemaker–Levy 9: a ‘rubble pile’ model with dissipative collisions and gravitational perturbations’, Bull. Am. Astron. Soc. 27, 1114.   
Richardson, D. C., Bottke, W. F. & Love, S. G. [1998], ‘Tidal distortion and disruption of Earth-crossing asteroids’, Icarus 134, 47–76.   
Richardson, D. C., Quinn, T., Stadel, J. & Lake, G. [2000], ‘Direct large-scale $N$ -body simulations of planetesimal dynamics’, Icarus 143, 45–59.   
Richardson, D. C., Leinhardt, Z. M., Melosh, H. J., Bottke, W. F. & Asphaug, E. [2003], ‘Gravitational aggregates: evidence and evolution’, in Asteroids III, ed. W. F. Bottke et al. (University of Arizona Press), 501–15.   
Richter, K., Tanner, G. & Wintgen, D. [1993], ‘Classical mechanics of twoelectron atoms’, Phys. Rev. A48, 4182–96.   
Risken, H. [1984], The Fokker–Planck Equation (Springer-Verlag, Berlin).   
Rivera, E. J. & Lissauer, J. J. [2000], ‘Stability analysis of the planetary system orbiting $\upsilon$ Andromedae’, Astrophys. J. 530, 454–63.   
Roos, N. & Aarseth, S. J. [1982], ‘Evolution of rich clusters of galaxies’, Astron. Astrophys. 114, 41–52.   
Roos, N. & Norman, C. A. [1979], ‘Galaxy collisions and their influence on the dynamics and evolution of groups and clusters of galaxies’, Astron. Astrophys. 76, 75–85.   
Ross, D. J., Mennim, A. & Heggie, D. C. [1997], ‘Escape from a tidally limited star cluster’, Mon. Not. R. Astron. Soc. 284, 811–14.   
Rosseland, S. [1928], ‘On the time of relaxation of closed stellar systems’, Mon. Not. R. Astron. Soc. 88, 208–12.   
Roy, A. E. [1988], Orbital Motion (Adam Hilger, Bristol).   
Saar, S. H., Nordstr¨om, B. & Andersen, J. [1990], ‘Physical parameters for three chromospherically active binaries’, Astron. Astrophys. 235, 291–304.   
Safronov, V. S. [1969], Evolution of the Protoplanetary Cloud and Formation of the Earth and the Planets (Nauka, Moscow; NASA TT–F–667).   
Salo, H. [1992], ‘Gravitational wakes in Saturn’s rings’, Nature 359, 619–21.   
Salpeter, E. E. [1955], ‘The luminosity function and stellar evolution’, Astrophys. J. 121, 161–7.   
Sandage, A. R. [1953], ‘The color–magnitude diagram for the globular cluster M3’, Astron. J. 58, 61–75.   
Saslaw, W. C., Valtonen, M. & Aarseth, S. J. [1974], ‘The gravitational slingshot and the structure of extragalactic radio sources’, Astrophys. J. 190, 253–70.   
Scally, A. & Clarke, C. [2001], ‘Destruction of protoplanetary discs in the Orion Nebula Cluster’, Mon. Not. R. Astron. Soc. 325, 449–56.   
Schubart, J. [1956], ‘Numerische Aufsuchung periodischer L¨osungen im Dreik¨orperproblem’, Astron. Nach. 283, 17–22.   
Schwarzschild, M. [1958], Structure and Evolution of the Stars, (Princeton University Press).   
Shara, M. M. & Hurley, J. R. [2002], ‘Star clusters as type Ia supernova factories’, Astrophys. J. 571, 830–42.   
Shara, M. M., Hurley, J. R. & Mardling, R. A. [2003], ‘Planet migration and solar system survival in open cluster’, in preparation.   
Shara, M. M., Saffer, R. A. & Livio, M. [1997], ‘The first direct measurement of the mass of a blue straggler in the core of a globular cluster: BSS 19 in 47 Tucanae’, Astrophys. J. 489, L59–L62.   
Shara, M. M., Fall, S. M., Rich, R. M. & Zurek, D. [1998], ‘Hubble Space Telescope observations of NGC 121: first detection of blue stragglers in an extragalactic globular cluster’, Astrophys. J. 508, 570–5.   
Sigurdsson, S. & Phinney, E. S. [1993], ‘Binary–single star interactions in globular clusters’, Astrophys. J. 415, 631–51.   
Sills, A., Lombardi, J. C., Bailyn, C. D., Demarque, P., Rasio, F. A. & Shapiro, S. L. [1997], ‘Evolution of stellar collision products in globular clusters, I. Head-on collisions’, Astrophys. J. 487, 290–303.   
Sim´o, C. [2001], ‘Periodic orbits of the planar $N$ -body problem with equal masses and all bodies on the same path’, in The Restless Universe, ed. B. A. Steves & A. J. Maciejewski (Institute of Physics, Bristol), 265–84.   
Smith, H. [1974], ‘Integration errors and their effects on macroscopic properties of calculated $N$ -body systems’, in Lecture Notes in Mathematics, ed. D. G. Bettis (Springer-Verlag, New York), 362, 360–73. [1977], ‘The validity of statistical results from $N .$ -body calculations’, Astron. Astrophys. 61, 305–12.   
Smith, K. W. & Bonnell, I. A. [2001], ‘Free-floating planets in stellar clusters?’, Mon. Not. R. Astron. Soc. 322, L1–L4.   
Soffel, M. H. [1989], Relativity in Astrometry, Celestial Mechanics and Geodesy (Springer-Verlag, Berlin).   
Spitzer, L. [1940], ‘The stability of isolated clusters’, Mon. Not. R. Astron. Soc. 100, 396–413. [1958], ‘Disruption of galactic clusters’, Astrophys. J. 127, 17–27. [1969], ‘Equipartition and the formation of compact nuclei in spherical stellar systems’, Astrophys. J. 158, L139–L43. [1987], Dynamical Evolution of Globular Clusters (Princeton University Press).   
Spitzer, L. & Hart, M. H. [1971a], ‘Random gravitational encounters and the evolution of spherical systems, I. Method’, Astrophys. J. 164, 399–409. [1971b], ‘Random gravitational encounters and the evolution of spherical systems, II. Models’, Astrophys. J. 166, 483–511.   
Spitzer, L. & Mathieu, R. D. [1980], ‘Random gravitational encounters and the evolution of spherical systems, VIII. Clusters with an initial distribution of binaries’, Astrophys. J. 241, 618–36.   
Spitzer, L. & Shull, J. M. [1975a], ‘Random gravitational encounters and the evolution of spherical systems, VI. Plummer’s model’, Astrophys. J. 200, 339–42. [1975b], ‘Random gravitational encounters and the evolution of spherical systems, VII. Systems with several mass groups’, Astrophys. J. 201, 773–82.   
Spitzer, L. & Thuan, T. X. [1972], ‘Random gravitational encounters and the evolution of spherical systems, IV. Isolated systems of identical stars’, Astrophys. J. 175, 31–61.   
Springel, V., Yoshida, N. & White, S. D. M. [2001], ‘GADGET: a code for collisionless and gasdynamical cosmological simulations’, New Astron. 6, 79– 117.   
Spurzem, R. [1999], ‘Direct $N$ -body simulations’, J. Comp. Applied Maths. 109, 407–32.   
Spurzem, R. & Aarseth, S. J. [1996], ‘Direct collisional simulation of 10 000 particles past core collapse’, Mon. Not. R. Astron. Soc. 282, 19–39.   
Spurzem, R. & Giersz, M. [1996], ‘A stochastic Monte Carlo approach to modelling of real star cluster evolution, I. The model’, Mon. Not. R. Astron. Soc. 283, 805–10.   
Spurzem, R. & Takahashi, K. [1995], ‘Comparison between Fokker–Planck and gaseous models of star clusters in the multi-mass case revisited’, Mon. Not. R. Astron. Soc. 272, 772–84.   
Spurzem, R., Baumgardt, H. & Ibold, N. [2003], ‘A parallel implementation of an N-body integrator on general and special purpose computers’, Mon. Not. R. Astron. Soc., submitted, astro-ph/0103410.   
Spurzem, R., Makino, J., Fukushige, T., Lienhart, G., Kugel, A., M¨anner, R., Wetzstein, M., Burkert, A. & Naab, T. [2002], ‘Collisional stellar dynamics, gas dynamics and special purpose computing’, Fifth JSPS/CSE Symposium, Tokyo, in press, astro-ph/0204326.   
Stadel, J., Wadsley, J. & Richardson, D. C. [2002], ‘High performance computational astrophysics with pkdgrav’, in High Performance Computing Systems and Applications, ed. N.J. Dimopoulos & K. F. Lie (Kluwer, Boston), 501–23.   
Standish, E. M. [1968a], ‘The numerical integration of collapsing clusters’, Bull. Astron. 3, 135–45.