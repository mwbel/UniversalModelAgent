# TheoryofOrbit Determination

Andrea Milani and Giovanni Gronchi

![](images/75182ae6443c4a14db09d3bf3e80f532edb4c362e6c91a7159e80189c2bf4bcd.jpg)

Determining orbits of natural and artificial celestial bodies is an essential step in the exploration and understanding of the Solar System. However, recent progress in the quality and quantity of data from astronomical observations and spacecraft-tracking has generated orbit determination problems which cannot be handled by classical algorithms. This book presents new algorithms capable of handling the millions of bodies which could be observed by next-generation surveys, and which can fully exploit tracking data with state-of-the-art levels of accuracy.

After a general mathematical background and summary of classical algorithms, the new algorithms are introduced using the latest mathematical tools and results, to which the authors have personally contributed. Case studies based on actual astronomical surveys and space missions are provided, with applications of these new methods. Intended for graduate students and researchers in applied mathematics, physics, astronomy, and aerospace engineering, this book is also of interest to non-professional astronomers.

andrea milani is Full Professor of Mathematical Physics in the Department of Mathematics, University of Pisa. His areas of research include the $N .$ -body problem, the stability of the Solar System, asteroid dynamics and families, satellite geodesy, planetary exploration, orbit determination, and asteroid impact risk.

giovanni f. gronchi is a Researcher of Mathematical Physics in the Department of Mathematics, University of Pisa. His research is on Solar System body dynamics, perturbation theory, orbit determination, singularities, and periodic orbits of the $N .$ -body problem.

COVER ILLUSTRATION: The orbits of eight potentially hazardous asteroids (PHA); they have a minimum intersection distance with the orbit of the Earth of less than 0.05 astronomical units. Together with many more smaller objects, they form a swarm surrounding the orbit of our planet (represented, not to scale, in green, orbit in yellow), are observable with either telescopes or radar, and provide a good example of an orbit determination problem. The objects in this figure are the brightest PHA, with diameters larger than $2 ~ \mathrm { k m }$ ; thus an impact with the Earth would result in a global catastrophe. There has been interesting recent progress in the theory of orbit determination, to which the authors of this book have contributed. New algorithms have been developed to exclude the possibility that any of these objects have the possibility of impacting the Earth, at least in the next 100 years. The same result also applies to somewhat smaller PHA, but the impact of either a much smaller known asteroid or an asteroid still to be discovered is still possible; thus the orbit determination work must go on. The orbit diagram is superimposed on an actual image of the sky (courtesy of G. Rhemann, Astrostudio, Vienna) which includes a Solar System body: a comet discovered in 2008 by A. Boattini, showing its coma.

# THEORY OF ORBIT DETERMINATION

ANDREA MILANI AND

GIOVANNI F. GRONCHI Department of Mathematics, University of Pisa

CAMBRIDGE UNIVERSITY PRESS   
Cambridge, New York, Melbourne, Madrid, Cape Town, Singapore,   
São Paulo, Delhi, Dubai, Tokyo

Cambridge University Press The Edinburgh Building, Cambridge CB2 8RU, UK

Published in the United States of America by Cambridge University Press, New York www.cambridge.org Information on this title: www.cambridge.org/9780521873895 $©$ A. Milani and G. Gronchi 2010

This publication is in copyright. Subject to statutory exception and to the provision of relevant collective licensing agreements, no reproduction of any part may take place without the written permission of Cambridge University Press.

First published in print format 2009

ISBN-13 978-0-511-65827-3 eBook (NetLibrary)

ISBN-13 978-0-521-87389-5 Hardback

Cambridge University Press has no responsibility for the persistence or accuracy of urls for external or third-party internet websites referred to in this publication, and does not guarantee that any content on such websites is, or will remain, accurate or appropriate.

# Part I Problem Statement and Requirements 1

# 1 THE PROBLEM OF ORBIT DETERMINATION

1.1 Orbits and observations The minimum principle 35   
1.3 Two interpretations 6   
1.4 Classification of the problem 7   
1.5 How to read this book 13

# 2 DYNAMICAL SYSTEMS 15

2.1 The equation of motion 15   
2.2 Solutions of the equation 16   
2.3 The variational equation 18   
2.4 Lyapounov exponents 20   
2.5 Model problem dynamics 21

# 3 ERROR MODELS 23

3.1 Continuous random variables 2327   
3.2 Gaussian random variables   
3.3 Expected values and transformations 30

# 4 THE N–BODY PROBLEM 33

4.1 Equation of motion and integrals 33   
4.2 Coordinate changes 36   
4.3 Barycentric and heliocentric coordinates   
4.4 Jacobian coordinates   
4.5 Small parameter perturbation   
4.6 Solar System dynamical models 54

# Contents

Part II Basic Theory 57

5 LEAST SQUARES 59

5.1 Linear least squares 59   
5.2 Nonlinear least squares 62   
5.3 Weighting of the residuals 66   
5.4 Confidence ellipsoids 68   
5.5 Propagation of covariance 7274   
5.6 Model problem   
5.7 Probabilistic interpretation 77   
5.8 Gaussian error models and outlier rejection 80

# 6 RANK DEFICIENCY 87

6.1 Complete rank deficiency 87   
6.2 Exact symmetries 91   
6.3 Approximate rank deficiency and symmetries 93   
6.4 Scaling and approximate rank deficiency 96   
6.5 Planetary systems: extrasolar planets 98   
6.6 Planetary systems: the Solar System 104

# Part III Population Orbit Determination 111

# THE IDENTIFICATION PROBLEM 113

7.1 Classification of the problem 113   
7.2 Linear orbit identification 116   
7.3 Semilinear orbit identification 120   
7.4 Nonlinear orbit identification 124   
7.5 Recovery and precovery 130   
7.6 Attribution 133

# 8 LINKAGE

# 137

8.1 Admissible region 137   
8.2 Sampling of the admissible region 144   
8.3 Attributable orbital elements 148   
8.4 Predictions from an attributable 152   
8.5 Linkage by sampling the admissible region 156   
8.6 Linkage by the two-body integrals 158   
8.7 The space debris problem 163

# 9 METHODS BY LAPLACE AND GAUSS 171

9.1 Attributables and curvature 171   
9.2 The method of Laplace 174   
9.3 The method of Gauss 175

Contents vii

9.4 Topocentric Gauss–Laplace methods 177   
9.5 Number of solutions 183   
9.6 Charlier theory 185   
9.7 Generalization of the Charlier theory 188

# WEAKLY DETERMINED ORBITS 197

10.1 The line of variations 197   
10.2 Applications of the constrained solutions 202   
10.3 Selection of a metric 208   
10.4 Surface of variations 214   
10.5 The definition of discovery 215

# 11 SURVEYS 219

11.1 Operational constraints of Solar System surveys 219   
11.2 Identification and orbit determination procedure 221   
11.3 Controlling the computational complexity 223   
11.4 Identification management 226   
11.5 Tests for accuracy 232   
11.6 Recovery of low confidence detections 235

# 12 IMPACT MONITORING 237

12.1 Target planes 239   
12.2 Minimum orbital intersection distance 242   
12.3 Virtual asteroids 248   
12.4 Target plane trails 251   
12.5 Reliability and completion of impact monitoring 256   
12.6 The current monitoring systems 258

# Part IV Collaborative Orbit Determination

# 13 THE GRAVITY OF A PLANET 261

13.1 The gravity field 261   
13.2 Spherical harmonics 266   
13.3 The Hilbert space of the harmonic functions 276   
13.4 The gravity field along the orbit 280   
13.5 Frequency analysis, ground track, and resonance 284

# 14 NON-GRAVITATIONAL PERTURBATIONS

14.1 Direct radiation pressure 288   
14.2 Thermal emission 294   
14.3 Indirect radiation pressure 299   
14.4 Drag 302   
14.5 Active spacecraft effects 303

Contents

14.6 Case study: asteroid orbiter 306

15 MULTI-ARC STRATEGY 311

15.1 Local–global decomposition 311   
15.2 Case study: satellite laser ranging 314   
15.3 Perturbation model 315   
15.4 Local geodesy 317   
15.5 Symmetries and rank deficiencies 319

# 16 SATELLITE GRAVIMETRY 323

16.1 On-board instrumentation 324   
16.2 Accelerometer missions 331   
16.3 Gradiometer missions 333   
16.4 Resonant decomposition 338   
16.5 Polar gaps 339   
16.6 Satellite-to-satellite tracking 345

# 17 ORBITERS AROUND OTHER PLANETS 349

17.1 Science goals for an orbiter around Mercury 349   
17.2 Interplanetary tracking 351   
17.3 The gravimetry experiment 356   
17.4 The rotation experiment 360   
17.5 The relativity experiment 364   
17.6 Global data processing 367   
References 371   
Index 379

# PREFACE

This book is a tool for our own teaching and an opportunity to rethink and reorganize the results of our own research. However, I think such a book can be useful to others, for two main reasons. First, spaceflight is no longer the privilege of the few superpowers, but is becoming available to many nations and agencies. Orbit determination is an essential knowhow, both in the planning phase of mission analysis and in the operations of space missions. Thus its mathematical tools need to become widely available.

Second, the knowledge and skill used in orbit determination, for both natural and artificial celestial bodies, was available only among a restricted group of specialists. The prevailing attitude was a proprietary one: the knowledge and the software were protected by formal copyright and/or by secrecy, although protecting in this way the pure mathematical theory is, in the long run, impossible. This attitude might have been justified under the conditions of the world of 30–40 years ago, in the critical phases of the competition to achieve space firsts. Now it is time to teach and disseminate this knowledge, allowing the formation of a wider group of specialists.

I know that many of the rules of thumb and practical advice contained in this book will be rated as well known, even obvious, by the few experts, but this is not the point. Even well-known results may need to be presented in a rational, rigorous, and didactically effective new way, together with the outcome of recent innovative research. On the other hand, this book does not have the intent of providing a comprehensive review of all that has been done in this field, because the size would become impractical. This book is about making widely available the outcome of the research done by my group over many years, and includes methods for which there are rigorous mathematical arguments and which have been fully tested by us first hand, and found to be effective. In the last $\simeq 1 5$ years there has been enormous progress in this field, and several other research groups have given important contributions: we are in no way claiming that their methods would not work, we are just giving a list of methods which we know to work.

The above arguments may not be enough for the approval of all the people in this field, but I do think that to state the mathematical foundations and rules of orbit determination, thus removing a vague flavor of craftmanship, can also benefit the already existing specialists. The orbit determination expert, in the very competitive environment in which space missions and large astronomical projects are selected today, is too often under pressure to endorse claims of wonderful results to be achieved with very limited means. By ignoring the rules of good practice it is possible to claim illusory precision and/or completeness for the solution, including the orbits and other parameters which can be operationally, technologically, and scientifically relevant. Maybe being able to cite a textbook stating clearly what is appropriate and what is illusory can help in relieving this improper pressure.

This book is based on the experience accumulated in $\simeq 3 0$ years of research with my coworkers of the former Space Mechanics Group (now Celestial Mechanics Group) at the Department of Mathematics, University of Pisa. Thus it contains, besides the formal mathematical theory and the teaching examples, a number of “case studies” based upon actual research projects. They are about space missions and about natural objects: one of the goals is to stress the common mathematics used in satellite geodesy and in dynamical astronomy, and at the same time to present clearly the main differences.

The preparation of this book has been made possible by the collaboration of my younger colleague, Dr. Giovanni F. Gronchi. Besides classical material and original results by myself and Gronchi, this book contains the output of research done by the members of our group and by either regular or occasional external coworkers. Thus I would like to include a long, but still possibly incomplete, list of coworkers whose contributions have to be acknowledged: L. Anselmo, O. Arratia, S. Baccili, A. Boattini, C. Bonanno, M. Carpino, G. Catastini, L. Cattaneo, S.R. Chesley, S. Cical\`o, L. Denneau, L. Dimare, P. Farinella, D. Farnocchia, Z. Kneˇzevi´c, L. Iess, R. Jedicke, A. La Spina, M. de’ Michieli Vitturi, A.M. Nobili, A. Rossi, M.E. Sansaturio, G. Tommei, G.B. Valsecchi, D. Villani, D. Vokrouhlick´y.

This book is dedicated to two good friends and valuable coworkers: Paolo Farinella and Steve Chesley. They could have been among the authors of this book, but they both left in the year 2000, when the book project was immature. Steve went back to his home country, from where he can still advise me on these subjects. Paolo went where he can give me neither his essential scientific insight nor the warmth of his friendship. Thus I would like to thank both of them for what I learned with them and from them.

# Part I

# Problem Statement and Requirements

# 1

# THE PROBLEM OF ORBIT DETERMINATION

In this chapter we define the problem of orbit determination, by specifying its three basic mathematical elements: the dynamics, the observations and the error model. We state the minimum principle, the least squares principle as the main case, and attempt a classification of the types of orbit determination found in astronomy and astrodynamics. The last section contains suggestions on the reading sequence, to adapt this book to different needs.

# 1.1 Orbits and observations

The two essential elements of an orbit determination problem are orbits and observations. Orbits are solutions of an equation of motion:

$$
\frac { d \mathbf { y } } { d t } = \mathbf { f } \left( \mathbf { y } , t , \mu \right)
$$

which is an ordinary differential equation; $\mathbf { y } \in \mathbb { R } ^ { p }$ is the state vector, $\pmb { \mu } \in$ $\mathbb { R } ^ { p ^ { \prime } }$ are the dynamical parameters, such as the geopotential coefficients, $t \in \mathbb R$ is the time. In the asteroid case the equation of motion is the $N -$ -body problem, the asteroid orbit being perturbed by the gravitational attraction of the planets; for many comets and some exceptionally accurate orbits of asteroids the non-gravitational effects are also relevant. For an artificial satellite the equation of motion is the satellite problem, the orbit being mostly perturbed by the asymmetric part of the geopotential, but also by non-gravitational perturbations.

The initial conditions are the value of the state vector at an epoch $t _ { 0 }$ :

$$
\mathbf { y } ( t _ { 0 } ) = \mathbf { y _ { 0 } } \in \mathbb { R } ^ { p } .
$$

In the two simple cases cited above we have $p = 6$ , i.e., the vector of the initial condition is just formed by the position and velocity of the small

body in some inertial reference system. The orbits are specific solutions, for a given value of $\mathbf { y _ { 0 } }$ and $\pmb { \mu }$ , of the equation of motion (initial condition problem). All the orbits together form the general solution

$$
\mathbf { y } = \mathbf { y } ( t , \mathbf { y _ { 0 } } , \mu ) ,
$$

also known as integral flow when considered as a mapping from the initial conditions (and dynamical parameters) to the current state at time $t$ :

$$
\mathbf { y } ( t ) = \Phi _ { t _ { 0 } } ^ { t } ( \mathbf { y _ { 0 } } , \mu ) .
$$

For the second element we introduce an observation function

$$
R ( \mathbf { y } , t , \nu )
$$

depending on the current state, directly upon time, and also upon a number of kinematical parameters $\nu \in \mathbb { R } ^ { p ^ { \prime \prime } }$ . The function $R$ is assumed to be differentiable. The composition of the general solution with the observation function is the prediction function

$$
r ( t ) = R ( \mathbf { y } ( t ) , t , \nu )
$$

which is used to predict the outcome of a specific observation at some time $t _ { i }$ , with $i = 1 , \ldots , m$ . However, the observation result $r _ { i }$ is generically not equal to the prediction, the difference being the residual

$$
\xi _ { i } = r _ { i } - R ( \mathbf { y } ( t _ { i } ) , t _ { i } , \pmb { \nu } ) , \quad i = 1 , \ldots , m .
$$

The observation function can depend also upon the index $i$ , the most common case being the use of a two-dimensional observation function like (right ascension, declination) or (range, range-rate), in which case $R$ has two different analytical expressions, one for $i$ even, the other for $i$ odd. All the residuals can be assembled forming a vector in $\mathbb { R } ^ { m }$

$$
{ \pmb { \xi } } = ( \xi _ { i } ) _ { i = 1 , \dots , m }
$$

which is in principle a function of all the $p + p ^ { \prime } + p ^ { \prime \prime }$ variables $( \mathbf { y _ { 0 } } , \mu , \nu )$ .

The above equations define a fully deterministic model: each residual is a single valued function of the $p { + } p ^ { \prime } { + } p ^ { \prime \prime }$ parameters. This function is obtained from the observation function, for which we assume an explicit analytical expression, by using the general solution, which is not known as an analytical expression but is uniquely defined by the differential equations; both functions are assumed to be differentiable, see Chapter 2. These assumptions may not be the whole truth, as we shall see in Chapters 14 and 17, but we shall work with them for now.

The random element is introduced by the assumption that every observation contains an error. Even assuming we know with perfect accuracy all the true values $\left( \mathbf { y _ { 0 } } ^ { * } , \mu ^ { * } , \nu ^ { * } \right)$ of the parameters, that our model is perfectly complete (both for the equation of motion and for the observations), and that our explicit computations are perfectly accurate (they are computed in “exact arithmetic”, not with a realistic computer), nevertheless the residuals

$$
\xi _ { i } ^ { * } = r _ { i } - R ( \mathbf { y } ( \mathbf { y _ { 0 } } ^ { * } , t _ { i } , \mu ^ { * } ) , t _ { i } , \nu ^ { * } , i ) = \epsilon _ { i }
$$

would not be zero but random variables. The joint distribution of $\epsilon =$ $( \epsilon _ { i } ) _ { i = 1 , \dots , m }$ needs to be modeled, that is we need some assumptions, either in the form of a probability density function or as a set of inequalities, describing the observation errors we rate as acceptable. The probabilistic approach in most cases uses Gaussian distributions, discussed in Chapter 3.

# 1.2 The minimum principle

The basic tool of the classical theory of orbit determination (Gauss 1809) is the definition of a target function $\mathcal { Q } ( \xi )$ depending on the vector of residuals $\xi$ . The target function cannot be chosen arbitrarily, but needs to satisfy suitable conditions of regularity and convexity. We shall focus on the simplest case, in which $\mathcal { Q }$ is proportional to the sum of squares of all the residuals:

$$
\boldsymbol { \mathcal { Q } } ( \xi ) = \frac { 1 } { m } \xi ^ { T } \xi = \frac { 1 } { m } \sum _ { i = 1 } ^ { m } \xi _ { i } ^ { 2 } .
$$

A quadratic form of general type, provided it is non-negative, can be handled with exactly the same formalism (see Chapter 5) and often needs to be used in practical applications. Since each residual is a function of all the parameters,

$$
\xi _ { i } = \xi _ { i } ( \mathbf { y _ { 0 } } , \pmb { \mu } , \pmb { \nu } ) ,
$$

the target function is also a function of $( \mathbf { y _ { 0 } } , \pmb { \mu } , \pmb { \nu } )$ . The next step is to select the parameters to be fit to the data: let $\mathbf { x } \in \mathbb { R } ^ { N }$ be a subvector of $( \mathbf { y _ { 0 } } , \pmb { \mu } , \pmb { \nu } ) \in$ $\mathbb { R } ^ { p + p ^ { \prime } + p ^ { \prime \prime } }$ , that is $\mathbf { x } = ( x _ { i } ) , i = 1 , N$ , with each $x _ { i }$ either a component of the initial conditions, or a dynamical parameter, or a kinematical parameter. Then we consider the target function

$$
Q ( \mathbf { x } ) = \mathcal { Q } ( \pmb { \xi } ( \mathbf { x } ) )
$$

as a function of $\mathbf { x }$ only, leaving the vector of the consider parameters $\mathbf { k } \in \mathbb { R } ^ { p + p ^ { \prime } + p ^ { \prime \prime } - N }$ (all the parameters not included in $\mathbf { x }$ ) fixed at the assumed value.

The minimum principle selects as nominal solution the point $\mathbf { x } ^ { * } \in$ $\mathbb { R } ^ { N }$ where the target function $Q ( \mathbf { x } )$ has its minimum value $Q ^ { * }$ . The principle of least squares is the minimum principle with as target function the sum of squares ${ \mathcal Q } ( \pmb { \xi } ) = \pmb { \xi } ^ { T } \pmb { \xi } / m$ , or some other quadratic form.

# 1.3 Two interpretations

The minimum principle should not be understood as if the “real” solution needs to be the point of minimum $\mathbf { x } ^ { * }$ . Two interpretations can be used.

According to the optimization interpretation, $\mathbf { x } ^ { * }$ is the optimum point but values of the target function immediately above the minimum are also acceptable. The set of acceptable solutions can be described as the confidence region

$$
Z ( \sigma ) = \left\{ \mathbf { x } \in \mathbb { R } ^ { N } \left| Q ( \mathbf { x } ) \leq Q ^ { * } + { \frac { \sigma ^ { 2 } } { m } } \right. \right\}
$$

depending upon the confidence parameter $\sigma > 0$ . For least squares

$$
Z ( \sigma ) = \left\{ \mathbf { x } \in \mathbb { R } ^ { N } \left| \sum _ { i = 1 } ^ { N } \xi _ { i } ^ { 2 } \leq m Q ^ { * } + \sigma ^ { 2 } \right. \right\} .
$$

The intuitive meaning of the confidence region is clear: the solutions $\mathbf { x }$ in $Z ( \sigma )$ correspond to observation errors larger than those for $\mathbf { x } ^ { * }$ , but still compatible with the available information on the observation procedure. The choice of the value of $\sigma$ bounding the acceptable errors is not easy.

The alternative probabilistic interpretation describes the observation errors $\epsilon _ { i }$ as random variables with an assumed probability density, which should be the result of an error model, justified by a priori knowledge of the observation process and/or a posteriori statistical tests. The vector ${ \epsilon } = ( { \epsilon } _ { i } ) , i = 1 , m$ , is then a set of jointly distributed random variables (see Section 3.1), and also the joint probability density function needs to be known; in particular, independence of the errors for observations at different times cannot be assumed, but needs to be justified by statistical tests.

Then the probabilistic model of the observation errors can be mapped in a probabilistic model of the result of orbit determination, with a probability density for the random variables $\mathbf { x }$ which in principle exists and can be, at least under some hypotheses, explicitly computed. The probability that the true orbit coincides exactly with the nominal solution $\mathbf { x } ^ { * }$ is zero, although under reasonable hypotheses $\mathbf { x }$ could be both the mode (point of maximum of the probability density) and the expected value.

In other words, the optimization interpretation describes the possible solutions as a subset of the $\mathbf { x }$ space where the target function has an acceptable value, surrounding the nominal solution which is the minimum point. The probabilistic interpretation regards the solutions as a probability density cloud, surrounding the point of highest probability density. Both interpretations can be useful, having different advantages and limitations.

# 1.4 Classification of the problem

Orbit determination appears as a number of different problems, with different dynamical systems and observation techniques. One way to classify the dynamical systems is to decompose the right-hand side of the equation of motion into three parts:

$$
\frac { d \mathbf { y } } { d t } = \mathbf { f _ { 0 } } ( \mathbf { y } , t , \mu ) + \mathbf { f _ { 1 } } ( \mathbf { y } , t , \mu ) + \mathbf { f _ { 2 } } ( \mathbf { y } , t , \mu ) ;
$$

the unperturbed equation of motion has only the main term $\mathbf { f _ { 0 } }$ , with $| \mathbf { f _ { 0 } } | \gg$ $\left| \mathbf { f _ { 1 } } \right|$ . The main term may not contain unknown parameters, or very few. The perturbations are subdivided into the most relevant ones $\mathbf { f _ { 1 } }$ and the negligible ones $\mathbf { f _ { 2 } }$ . Negligible means not only that $| \mathbf { f _ { 1 } } | \gg | \mathbf { f _ { 2 } } |$ but also that the effects of the $\mathbf { f _ { 2 } }$ terms on the general solution are small (with respect to the observational accuracy), thus the equation of motion actually solved to compute the predictions contains only $\mathbf { f _ { 0 } } + \mathbf { f _ { 1 } }$ . The choice of the terms to be neglected in each specific case is therefore a delicate issue, discussed in Sections 4.6, 15.3, and 17.3.

Let us focus on the main term f . For a satellite of the Earth it is the monopole gravitational attraction of the Earth; for an object in heliocentric orbit it is the monopole attraction from the Sun, and so on. In most cases the unperturbed equation of motion is a two-body problem. Only in a few exceptional examples is there no dominant two-body term.

Thus we can classify orbit determination problems by the central body:

• Earth satellite orbits, for the Moon, artificial satellites, and space debris; • heliocentric orbits, including the planets, the smaller asteroids, comets, meteoroids, trans-neptunian objects, and artificial interplanetary probes; satellite orbits of other planets, for the natural satellites, planetary orbiters, binary asteroids, and asteroid/comet orbiter missions; the orbits around another star, for binary stars and extrasolar planets; the cases without a dominant central body, such as orbits near the Lagrangian equilibrium points, temporary satellite captures, very small interplanetary dust with motion dominated by radiation pressure.

The orbit determination problems may differ also in the observation method, in the number and timing of the data, and in their accuracy. The main difference is between the collaborative and the population orbit determination problems.

# Tracking

In collaborative orbit determination the object whose orbit has to be determined has a man-built device specifically intended to assist the observer. In this case the observation procedure is usually called tracking.

The most common case is tracking by radio waves: artificial satellites are normally equipped with a device called a transponder, which receives, amplifies, and retransmits the radio signal received from a ground station in a given frequency band.1 Then the range-rate, the time derivative of the distance between the spacecraft and the ground station, can be measured by the Doppler shift between the signal emitted from the ground station and the one received back. If the signal also contains, beside the carrier, an encoded signal and the transponder is regenerative, that is it can send back this encoded signal on top of the return carrier, then also the range, or distance from the ground station, can be measured. This is possible also at interplanetary distance, thus the spacecraft could be in heliocentric orbit but also orbiting around another planet, or around an asteroid/comet.

In the above example the spacecraft needs to consume energy in the transponder, thus it has to be active, with a power system and possibly with attitude control to suitably point some antenna. There are examples in which the spacecraft is totally passive, such as the Earth satellites specifically launched for satellite laser ranging: they are only equipped with a special class of mirror, the corner cubes, to return a light ray in the same direction it came from with minimal dispersion. The ground stations are equipped with lasers capable of powerful but short-duration pulses of monochromatic light: the time interval between the emission of each pulse and the return signal detection measures the distance to the satellite.

The above examples are about artificial celestial bodies, that is man-made spacecraft. However, a tracking device can be planted on a natural body: e.g., corner cubes have been placed on the Moon by American and Soviet missions in the 1970s, thus lunar laser ranging has been regularly performed for more than 30 years, and the orbit of our natural satellite is known with centimeter level accuracy, actually more accurately than the orbit of any artificial satellite, affected by non-gravitational perturbations. The Viking landers have been on the surface of Mars for more than five years with operational transponders, and this has allowed the computation of the orbit of Mars with an accuracy of a few tens of meters. The interplanetary space probes like Voyager can be used to constrain the orbit of the planets they encounter. Planetary orbiters like Cassini (now around Saturn) and the future BepiColombo (around Mercury) will provide very accurate orbit determination for these planets and for the natural satellites of Saturn, thanks to the very accurate transponders on these spacecraft. Thus the main difference is not between natural and artificial orbits.

The specific properties of the collaborative cases are three.

First, the body has some built in capability to respond to tracking; thus the number of observations, their distribution in time and their accuracy are planned in the design phase of the mission. A simulation of orbit determination is a compulsory phase of mission analysis, the study showing that some proposed space mission is feasible from the astrodynamics point of view. If the simulated orbit determination gives poor results, the required frequency and accuracy of the observations has to be improved. Thus the most difficult cases of divergent orbit determination should not occur in the collaborative case; even strong nonlinearity and chaos should not happen. However, if there is some failure, either hardware like an antenna failing to deploy, or software like a faulty on-board computer program, or planning like an orbit determination simulation providing illusory results, then a tracking case may show some problems of the non-collaborative case, including divergence, excessive nonlinearity, and chaos.

Second, the observation data contain information on which object is being tracked. In the simplest case, there is only one spacecraft answering in a given frequency band in a given direction (within a given solid angle). Frequency bands and orbit slots (e.g., in the geosynchronous belt) are allocated by international authorities to avoid confusion and interference between signals to and from the satellites. In other cases (e.g., satellite constellations, such as navigation satellites) the satellite encodes its identity in the signal sent back to the ground. Thus we can assume we always know to which spacecraft each batch of tracking data belongs. 2 In most cases it is possible to treat each spacecraft as a separate problem of orbit determination; the exceptions are the cases of satellite-to-satellite tracking, where the radio/laser beam travels between two (or more) satellites, in which case the orbits of the two (or more) have to be solved simultaneously.

Third, if the amount of observational data and their accuracy exceeds what is required for the determination of the orbit in the strictest sense, that is for fitting the initial conditions $\mathbf { y _ { 0 } }$ , the additional information can be used to fit other parameters, either dynamical or kinematical, and in fact this is often the case. This is the key idea of satellite geodesy, where the gravity field of the central planet (the Earth, the Moon, another planet, an asteroid) is determined from the tracking data, rather than from the inhomogeneous ground-based gravimetry. In satellite geodesy around the Earth also the position of the ground stations can be determined with an accuracy far superior to that possible with ground-based measurements.

# Catalogs

In the case of population orbit determination the observations are a scarce resource because the objects do not assist the observer. The total number of observations may not be small; actually it can be comparable to that of the tracking data points for a scientific space mission, e.g., tens of millions. The problem is that they refer to objects of a large population, and the average number of observations per object is small: e.g., $1 0 ^ { 7 }$ observations of a population of $1 0 ^ { 6 }$ objects (down to the minimum size observable).

The example most extensively discussed in this book is the orbit determination of the small bodies of the Solar System, including asteroids, comets, meteoroids and trans-neptunian objects. The number of objects needs to be qualified by a class of orbits and a minimum size: e.g., there are of the order of $1 0 ^ { 6 }$ main belt asteroids of size $\geq 1$ km in diameter (this is just an estimate, extrapolated from the orbits already determined). A survey consists of a number of telescopes scanning the sky and looking for objects with stellar appearance which move with respect to the approximately fixed stars; this is the origin of the name asteroid, as proposed by Herschel. When such a moving object is detected the amount of information is minimal, typically only astrometry, that is angular positions, and photometry, that is apparent magnitude. There is a signature neither to identify the object with the ones already discovered, nor to decide it is new.

As we will see in Chapter 8, orbit determination is typically not possible with the discovery data alone. Thus the orbit determination problem cannot be disentangled from the identification problem, that is to find the independent discoveries referring to the same physical object: only by joining the information, contained in such separate discoveries, we can gather enough data for a solution. The output of the identification/orbit determination procedure is a catalog containing the list of distinct objects discovered, their best fit orbits, an estimate of their uncertainty and the little physical information available, in most cases just the absolute magnitude, a measure of the intrinsic capability of the object to reflect sunlight.3

The above example refers to passive observations detecting photons of reflected sunlight. Active observations are used in planetary radar observations, where a powerful beam of microwaves is directed towards a celestial body such as a major planet, a natural planetary satellite, an asteroid, a comet. At the present state-of-the-art, given that the signal-to-noise ratio at distance $r$ is proportional to $1 / r ^ { 4 }$ , only the major inner planets, some very large satellites (e.g., Titan), and large asteroids can be observed by radar at interplanetary distances. Most of the targets therefore are near-Earth asteroids, which have the possibility of comparatively close approaches to the Earth.4 Radar observations are a complex subject, because the radar return signal contains photons reflected from different parts of the asteroid surface, each with a different range and range-rate with respect to the radar antenna. In fact, the radar astrometry data are normal points obtained from a large fit providing also information on the size, shape, radar reflectivity, and rotation state of the object. The information constraining the orbit can be synthesized into an equivalent observation of range and range-rate. The accuracy of radar astrometry is between two and three orders of magnitude better than conventional astrometry.

The above examples are about natural bodies, but a very similar problem is obtained by considering spacecraft whose operational life is over. They can be observed in a non-collaborative way, with exactly the same techniques as asteroids, that is by astrometry and by radar. In most cases, however, these observations do not allow us to discriminate one dead spacecraft from another (actually, some care needs to be used to identify among the observations the ones belonging to operational spacecraft). As the search for this space debris progresses towards smaller and smaller Earth-orbiting objects, the list of bodies increases by adding spent rocket stages, pieces of exploded satellites and rocket motors, screws, bolts, and small pieces released during stage separation and antenna deployment, as well as particles of fuel, of frozen cooling liquid, all kinds of trash. A current estimate places at about $3 5 0 0 0 0$ the number of orbiting debris above 1 cm of diameter. Thus the space debris problem is a population orbit determination problem, and surveys have to be set up to compile catalogs of all the particles above a given size. The analogy is striking because there is an impact monitoring problem: the objects larger than a few mm could seriously damage the International Space Station by colliding at a relative speed of several km/s.

Thus the specific properties of the population cases are three, and they are opposite to those of the collaborative case.

First, the number of observations is not under our control. A survey can be designed to obtain a very large number of observations, but unavoidably the larger the data set, the larger the set of distinct objects for which the orbit has to be determined. Thus the average number of observations per object is small, typically of the order of 10.

Second, the batches of observations which can be immediately assigned to a single object are not enough to compute an orbit, thus the identification problem needs to be solved before orbit determination is possible. On the other hand, an identification can be considered reliable only if an orbit can be consistently fit to all the data believed to be of the same physical object. Thus orbit determination and identification are just a single algorithm, necessarily complex.

Third, the dynamical and kinematical parameters are normally not determined. After the reliable identifications have been established, each orbit can be solved individually, fitting just $N = p = 6$ parameters. Additionally, a separate fit of the photometric data can provide the absolute magnitude. However, this has to be performed for millions of bodies.

# Planetary systems

There are a few examples of orbit determination which do not fit well into the binary classification collaborative/population. Interesting examples are the planetary systems. There are two main cases.

Our Solar System contains a small number $N _ { P }$ of planets.5 The equation of motion for the planets needs to take into account the perturbations from the other planets, relativistic corrections, the perturbations from the larger satellites (especially the Moon), and the larger asteroids. The masses of the major planets appear as dynamical parameters $\pmb { \mu }$ , together with the post-Newtonian parameters describing general relativity effects.

Thus the orbits of the planets have to be determined all at once, including that of the Earth. The list of parameters may include $p \ : = \ : 6 N _ { P }$ initial conditions, $p ^ { \prime } \geq N _ { P }$ dynamical, and a number of kinematical parameters. The observations include astrometry, planetary radar, occultations, planetary landers, and spacecraft data. This example will be discussed mostly in Chapter 6 because of the rank deficiency.

Planets (and very small companion stars) orbiting around another star can be detected by measuring the star’s radial velocity, that is the range-rate. Although the motion of the planet is much wider, the dim luminosity of the planet in most cases cannot be discriminated from the much brighter signal from the star. If we assume there is a single planet (or companion star), the dynamical system is a two-body problem and the orbit determination problem is simple, once the symmetries have been properly accounted for (see Chapter 6). These extrasolar planets can be considered as a population: indeed there is now a large data set of high-resolution radial velocity data. However, each planetary system can be solved on its own, without possibility of confusion among the data from different stars. If there are more planets around the same star the problem becomes more complex, but still not as much as the satellite geodesy and population orbit determination problems. Thus this problem is comparatively simple, but this does not mean it can be solved without care.

There is a separate theory for the orbit determination of binary stars, when both are observable from the Earth. We are not discussing this case in this book, but there are specialized textbooks such as (Aitken 1964).

There is also an intermediate case of orbit determination for artificial satellites, the constellation orbit determination, when a set of dozens of satellites on similar orbits is used in such a way that measurements have to be simultaneously taken from different constellation members, to exploit the higher accuracy of differences with respect to absolute measurements.6 Then the orbits of the navigation satellites have to be determined all at once.

# 1.5 How to read this book

This textbook is intended for people interested in the general mathematical framework of orbit determination and in at least one of the main classes of applications (tracking, populations, and planetary systems). We expect that a significant fraction of the readers will not wish to read all the details about applications very far from the ones they are working on. Thus we suggest three ways to select your customized path through this book.

If you are interested in satellite geodesy, mission analysis and operations of space missions, planetary exploration, and similar topics, you should check that you know the required material of Chapters 2 and 3, then read the basic theory of Chapters 5 and 6. You need the specific background on satellite orbits of Chapters 13 and 14. At this point you are ready for the satellite geodesy and planetary exploration case studies of Chapters 14, 15, 16 and 17.

If you are interested in asteroid/comet orbit determination, you should begin with Chapters 2 and 3 as in the other case, but you cannot skip Chapter 4 unless you already have a specific background in celestial mechanics. Then you should read the basic theory of Chapters 5 and 6. At this point you should be ready for the theory of simultaneous identification and orbit determination of Chapters 7–10. Chapter 11 contains a case study of an asteroid survey. Chapter 8 contains useful suggestions if you need comparable work for space debris. If you are interested in one of the most impressive applications of orbit determination, namely impact monitoring, which is a necessary tool to protect the Earth from collisions with asteroids, you may also read Chapter 12.

If you are only interested in planetary systems, the relevant examples are discussed in Chapter 6, thus you can read the first six chapters; some additional information is contained in Chapter 17.

If you are interested in all the possible applications of orbit determination, you can choose what you like, possibly using the subject index to identify where the definitions are given (on the pages with numbers in bold). We hope you will appreciate the effort done to present this subject in a unified way, based on our long and varied experience.

The appendices contain auxiliary material, which may be of significant help if you are undertaking the design and implementation of your own orbit determination software. Both for reasons of space in the book and to make the updates easier, the appendixes are not contained in this book but will be available online at the URL http://adams.dm.unipi.it/orbdetbook.

2

# DYNAMICAL SYSTEMS

This chapter contains some basic material on dynamical systems which is required for the following. We are giving no formal proofs, but just recall the statements of the main results to be used. Several textbooks on the subject are available, including (Hartmann 1964, Milani 2002a).

# 2.1 The equation of motion

We shall describe the motion by an ordinary differential equation of the form

$$
\frac { d \mathbf { y } } { d t } = \mathbf { f } \left( \mathbf { y } , t , \mu \right)
$$

where $\mathbf { f } : \mathbb { R } ^ { p + p ^ { \prime } + 1 } \longrightarrow \mathbb { R } ^ { p }$ is a function obeying some regularity requirements, the state vector $\mathbf { y } \in \mathbb { R } ^ { p }$ is the unknown, and $\pmb { \mu } \in \mathbb { R } ^ { p ^ { \prime } }$ are the dynamical parameters, that we may assume as constant ( $\mu = \mu _ { 0 }$ ). We are interested in the solutions of the initial value problem (the Cauchy problem)

$$
\frac { d { \bf y } } { d t } ( t ) = { \bf f } ( { \bf y } ( t ) , t , \mu ) , { \bf y } ( t _ { 0 } ) = { \bf y } _ { 0 } ;
$$

the general solution of (2.1) is a function of the time, the initial conditions, and the parameters

$$
\mathbf { y } ( t ) = \mathbf { y } ( t , t _ { 0 } , \mathbf { y } _ { 0 } , \pmb { \mu } ) .
$$

We can study the problem as an autonomous dynamical system, by introducing the variable $\mathbf { z }$ , the initial conditions $\mathbf { z } _ { 0 }$ , and the function $\mathbf { g }$

$$
\begin{array} { r } { { \bf z } = \left( \begin{array} { c } { { \bf y } } \\ { t - t _ { 0 } } \\ { \mu } \end{array} \right) ; \qquad { \bf z } _ { 0 } = { \bf z } ( t _ { 0 } ) = \left( \begin{array} { c } { { \bf y } _ { 0 } } \\ { 0 } \\ { \mu _ { 0 } } \end{array} \right) ; \qquad { \bf g } = \left( \begin{array} { c } { { \bf f } } \\ { 1 } \\ { { \bf 0 } } \end{array} \right) } \end{array}
$$

( $\mathbf { 0 }$ is the zero vector in $\mathbb { R } ^ { p ^ { \prime } }$ ): with these notations the problem becomes

$$
\frac { d { \bf z } } { d t } ( t ) = { \bf g } ( { \bf z } ( t ) ) , \mathrm {  ~ \bf ~ z } ( t _ { 0 } ) = { \bf z } _ { 0 } .
$$

The general solution of (2.2) is usually denoted with either $\Phi _ { t _ { 0 } } ^ { t } ( \mathbf { z } _ { 0 } )$ o r ${ \bf z } ( t , t _ { 0 } , { \bf z } _ { 0 } )$ , and it is called the integral flow. The map $\Phi _ { t _ { 0 } } ^ { t }$ depends on the two parameters $t _ { 0 } , t$ and, for each value of $t$ , it sends the initial conditions $\mathbf { z } _ { 0 }$ into ${ \bf z } ( t )$ , the value of the solution at time $t$ . The integral flow has the following semigroup property: for each $t _ { 0 } , t _ { 1 } , t _ { 2 } \in \mathbb { R }$

$$
\Phi _ { t _ { 1 } } ^ { t _ { 2 } } \circ \Phi _ { t _ { 0 } } ^ { t _ { 1 } } = \Phi _ { t _ { 0 } } ^ { t _ { 2 } } .
$$

As $\Phi _ { t _ { 0 } } ^ { t _ { 0 } }$ is the identity application, the integral flow $\Phi _ { t _ { 0 } } ^ { t }$ is invertible and its inverse is $\Phi _ { t } ^ { t _ { 0 } }$ . For autonomous differential equations like (2.2), we have time-shift invariance of the solutions:

$$
\begin{array} { r } { \Phi _ { t _ { 0 } } ^ { t } ( \mathbf { z } _ { 0 } ) = \Phi _ { 0 } ^ { t - t _ { 0 } } ( \mathbf { z } _ { 0 } ) = \mathbf { z } ( t - t _ { 0 } , 0 , \mathbf { z } _ { 0 } ) ; } \end{array}
$$

thus, given the initial time $t _ { 0 }$ , we can either consider $t - t _ { 0 }$ as time variable or we can assume that $t _ { 0 } = 0$ , and we can use the simplified notation $\Phi ^ { t } = \Phi _ { 0 } ^ { t }$ .

# Second-order equations

Sometimes the equation of motion is a second-order differential equation

$$
\frac { d ^ { 2 } { \bf x } } { d t ^ { 2 } } = { \bf h } ( { \bf x } , { \bf v } , \mu , t ) , ~ { \bf x } ( t _ { 0 } ) = { \bf x } _ { 0 } , ~ { \bf v } ( t _ { 0 } ) = { \bf v } _ { 0 }
$$

with ${ \bf v } = d { \bf x } / d t$ , as is the case when the orbits are computed in Cartesian coordinates. Then the problem can be reduced to (2.1) simply by setting $\mathbf { y } = ( \mathbf { x } , \mathbf { v } )$ , ${ \bf y } _ { 0 } = ( { \bf x } _ { 0 } , { \bf v } _ { 0 } )$ , and $\mathbf { f } ( \mathbf { y } ) = ( \mathbf { v } , \mathbf { h } )$ .

# 2.2 Solutions of the equation

We recall some basic results about existence, uniqueness, and regularity of the solutions of (2.2). A proof of these results can be found in several books on dynamical systems, e.g., (Hartmann 1964).

# Existence and uniqueness of the solutions

Let us consider an open set $\Omega \subseteq \mathbb { R } ^ { n }$ . A function $\mathbf { g } : \Omega \to \mathbb { R } ^ { n }$ is uniformly Lipschitz-continuous on $\Omega$ if there exists $L > 0$ such that

$$
| \mathbf { g } ( \mathbf { z } _ { 1 } ) - \mathbf { g } ( \mathbf { z } _ { 2 } ) | < L | \mathbf { z } _ { 1 } - \mathbf { z } _ { 2 } | \qquad \forall \mathbf { z } _ { 1 } , \mathbf { z } _ { 2 } \in \Omega .
$$

If $\mathbf { g }$ is uniformly Lipschitz-continuous, then for each ${ \mathbf z } _ { 0 } \in \Omega$ there exists a unique solution ${ \bf z } ( t )$ of (2.2) defined in an interval $( - \epsilon , \epsilon )$ with $\epsilon > 0$ depending on $\mathbf { z } _ { 0 }$ . If $\mathbf { g }$ is locally Lipschitz-continuous in $\Omega$ there exists locally a unique integral flow ${ \bf z } ( t , { \bf z } _ { 0 } )$ defined on an open set in $\mathbb { R } ^ { n + 1 }$ .

Note that if $\mathbf { g }$ is differentiable of class ${ \mathcal { C } } ^ { 1 }$ (with continuous partial derivatives) in a larger open set $\Omega _ { 1 }$ containing the compact $K$ and $\Omega \subset K$ , then it is also uniformly Lipschitz-continuous on $\Omega$ . In celestial mechanics the regularity of the equation of motion is guaranteed because the gravitational potential is a harmonic function (see Chapter 13). Only some non-gravitational perturbations may introduce regularity problems, see Section 14.3.

# Maximal solutions

A solution of (2.2) is maximal if it is defined in a maximal time interval, i.e., no solution with that initial data can be defined in a larger interval.

Let $\mathbf { z } _ { 0 } \in \Omega$ and ${ \bf z } = { \bf z } ( t )$ be a solution of (2.2) on an open interval $I \in \mathbb R$ containing 0. If the solution ${ \bf z } ( t )$ defined for $t \geq 0$ on a limited interval $[ 0 , t _ { 1 } )$ is contained in a compact set $K \subset \Omega$ then ${ \bf z } ( t )$ is not a maximal solution; similarly for $t \leq 0$ . The maximal solutions defined only in a limited interval must get out of any compact set in $\Omega$ .

# Lipschitz-continuity of the flow

The integral flow ${ \bf z } ( t , { \bf z } _ { 0 } )$ is Lipschitz-continuous as a function of the initial conditions $\mathbf { z } _ { 0 }$ ; this can be shown using the Gronwall lemma: let $y : I  \mathbb { R }$ be a non-negative function defined in an interval $I \subseteq \mathbb { R }$ ; if there are $\alpha , \beta > 0$ such that

$$
0 \leq y ( t ) \leq \beta + \alpha \int _ { 0 } ^ { t } y ( s ) d s , \quad { \mathrm { ~ t h e n ~ } } 0 \leq y ( t ) \leq \beta \exp ( \alpha t ) .
$$

An immediate consequence of the Gronwall lemma: if ${ \bf z } _ { 1 } ( t ) , { \bf z } _ { 2 } ( t )$ are solutions of (2.2), with different initial conditions ${ \bf z } _ { 1 } ( 0 ) , { \bf z } _ { 2 } ( 0 )$ , then assuming that $\mathbf { g }$ is uniformly Lipschitz-continuous we have

$$
| \mathbf { z } _ { 1 } ( t ) - \mathbf { z } _ { 2 } ( t ) | \leq | \mathbf { z } _ { 1 } ( 0 ) - \mathbf { z } _ { 2 } ( 0 ) | + L \int _ { 0 } ^ { t } | \mathbf { z } _ { 1 } ( s ) - \mathbf { z } _ { 2 } ( s ) | d s .
$$

Then by the Gronwall lemma

$$
| \mathbf { z } _ { 1 } ( t ) - \mathbf { z } _ { 2 } ( t ) | \leq | \mathbf { z } _ { 1 } ( 0 ) - \mathbf { z } _ { 2 } ( 0 ) | \exp { ( L t ) } ,
$$

i.e., the integral flow is Lipschitz-continuous with respect to the initial data.

# 2.3 The variational equation

Let us define the state transition matrix as the Jacobian matrix

$$
A ( t , { \mathbf { z } } _ { 0 } ) = \frac { \partial { \mathbf { z } } } { \partial { \mathbf { z } } _ { 0 } } ( t , { \mathbf { z } } _ { 0 } ) .
$$

If the integral flow ${ \bf z } ( t , { \bf z } _ { 0 } )$ is regular enough we can differentiate it twice, with respect to the time $t$ and the initial condition $\mathbf { z } _ { 0 }$ , and exchanging the order of the derivatives we obtain the same result:1

$$
\frac { \partial } { \partial t } \bigg [ \frac { \partial \mathbf { z } } { \partial \mathbf { z } _ { 0 } } ( t , \mathbf { z } _ { 0 } ) \bigg ] = \frac { \partial } { \partial \mathbf { z } _ { 0 } } \bigg [ \frac { \partial \mathbf { z } } { \partial t } ( t , \mathbf { z } _ { 0 } ) \bigg ] .
$$

Using (2.5) and the fact that ${ \bf z } ( t , { \bf z } _ { 0 } )$ is the solution of (2.2), we obtain the differential equation

$$
\frac { \partial } { \partial t } \bigg [ \frac { \partial \mathbf { z } } { \partial \mathbf { z } _ { 0 } } ( t , \mathbf { z } _ { 0 } ) \bigg ] = \frac { \partial \mathbf { g } } { \partial \mathbf { z } } \left( \mathbf { z } ( t , \mathbf { z } _ { 0 } ) \right) \frac { \partial \mathbf { z } } { \partial \mathbf { z } _ { 0 } } ( t , \mathbf { z } _ { 0 } ) .
$$

Equation (2.6) together with the initial condition ${ \partial { \bf z } } / { \partial { \bf z } _ { 0 } } = I$ at $( t , \mathbf { z } ) =$ $( 0 , { \bf z } _ { 0 } )$ , where $I$ is the identity matrix, give the Cauchy problem

$$
\left\{ \begin{array} { l c l } { \displaystyle \frac { \partial A } { \partial t } ( t , { \mathbf z } _ { 0 } ) } & { = } & { \displaystyle \frac { \partial { \mathbf g } } { \partial { \mathbf z } } \left( { \mathbf z } ( t , { \mathbf z } _ { 0 } ) \right) A ( t , { \mathbf z } _ { 0 } ) } \\ { A ( 0 , { \mathbf z } _ { 0 } ) } & { = } & { { \boldsymbol I } . } \end{array} \right.
$$

The linear differential equation in (2.7) is the variational equation. It can be interpreted as the linearized equation for the relative motion. Let ${ \bf z } ^ { ( 0 ) } ( t , { \bf z } _ { 0 } ) = { \bf z } ( t , { \bf z } _ { 0 } )$ be the general solution of (2.2) and let ${ \bf z } ^ { ( \epsilon ) } ( 0 , { \bf z } _ { 0 } ) =$ ${ \bf z } _ { 0 } + \epsilon { \bf v } _ { 0 }$ be the initial condition with the small perturbation $\epsilon { \bf v } _ { 0 }$ , where

$$
{ \bf z } ^ { ( \epsilon ) } ( t , { \bf z } _ { 0 } ) = { \bf z } \left( t , { \bf z } _ { 0 } + \epsilon { \bf v } _ { 0 } \right) .
$$

The Taylor expansion of $\mathbf { z } ^ { ( \epsilon ) }$ with respect to the small parameter $\epsilon$ gives

$$
\mathbf { z } ^ { ( \epsilon ) } ( t , \mathbf { z } _ { 0 } ) = \mathbf { z } ^ { ( 0 ) } ( t , \mathbf { z } _ { 0 } ) + \epsilon \mathbf { z } ^ { ( 1 ) } ( t , \mathbf { z } _ { 0 } ) + O ( \epsilon ^ { 2 } )
$$

where

$$
{ \bf z } ^ { ( 1 ) } ( t , { \bf z } _ { 0 } ) = \frac { \partial { \bf z } } { \partial { \bf z } _ { 0 } } ( t , { \bf z } _ { 0 } ) { \bf v } _ { 0 } .
$$

The Taylor expansion of $\mathbf { g } \left( \mathbf { z } ^ { ( \epsilon ) } \right)$ gives

$$
\mathbf { g } ( \mathbf { z } ^ { ( \epsilon ) } ) = \mathbf { g } ( \mathbf { z } ^ { ( 0 ) } + \epsilon \mathbf { z } ^ { ( 1 ) } + O ( \epsilon ^ { 2 } ) ) = \mathbf { g } ( \mathbf { z } ^ { ( 0 ) } ) + \epsilon \frac { \partial \mathbf { g } } { \partial \mathbf { z } } ( \mathbf { z } ^ { ( 0 ) } ) \mathbf { z } ^ { ( 1 ) } + O ( \epsilon ^ { 2 } ) .
$$

By equating the terms of order zero and one in $\partial \mathbf { z } ^ { ( \epsilon ) } / \partial t = \mathbf { g } \left( \mathbf { z } ^ { ( \epsilon ) } \right)$ and neglecting the higher order terms in $\epsilon$ we obtain

$$
\frac { \partial } { \partial t } ( \mathbf { z } ^ { ( \epsilon ) } - \mathbf { z } ^ { ( 0 ) } ) = \frac { \partial \mathbf { g } } { \partial \mathbf { z } } ( \mathbf { z } ^ { ( 0 ) } ) ( \mathbf { z } ^ { ( \epsilon ) } - \mathbf { z } ^ { ( 0 ) } )
$$

that is, the relative motion ${ \bf v } ( t , { \bf z } _ { 0 } ) = { \bf z } ^ { ( \epsilon ) } ( t , { \bf z } _ { 0 } ) - { \bf z } ^ { ( 0 ) } ( t , { \bf z } _ { 0 } )$ is the solution of the system

$$
\left\{ \begin{array} { l c l } { \displaystyle \frac { \partial { \bf v } } { \partial t } ( t , { \bf z } _ { 0 } ) } & { = } & { \displaystyle \frac { \partial { \bf g } } { \partial { \bf z } } ( { \bf z } ^ { ( 0 ) } ( t , { \bf z } _ { 0 } ) ) { \bf v } ( t , { \bf z } _ { 0 } ) } \\ { { \bf v } ( 0 , { \bf z } _ { 0 } ) } & { = } & { { \bf v } _ { 0 } } \end{array} \right.
$$

whose general solution is given by the variational equation (2.7).

# Variational equation with dynamical parameters

Let us write explicitly the variational equation for eq. (2.1). The state transition matrix is

$$
A ( t ) = { \frac { \partial \mathbf { z } } { \partial \mathbf { z } _ { 0 } } } = { \left[ \begin{array} { l l } { { \frac { \partial \mathbf { y } } { \partial \mathbf { y } _ { 0 } } } } & { { \frac { \partial \mathbf { y } } { \partial \mu } } } \\ { { \frac { \partial \pm \pmb { \mu } } { \partial \mathbf { y } _ { 0 } } } } & { { \frac { \partial \pmb { \mu } } { \partial \mu } } } \end{array} \right] } = { \left[ \begin{array} { l l } { { \frac { \partial \mathbf { y } } { \partial \mathbf { y } _ { 0 } } } } & { { \frac { \partial \mathbf { y } } { \partial \mu } } } \\ { \mathbf { 0 } } & { I } \end{array} \right] }
$$

where $\mathbf { 0 } , \mathbf { \xi } _ { I }$ are respectively the zero and the identity matrix, with dimensions suitable to their place in the matrix $A ( t )$ . Furthermore we have

$$
\frac { \partial \mathbf { g } } { \partial \mathbf { z } } = \left[ \begin{array} { c c } { \frac { \partial \mathbf { f } } { \partial \mathbf { y } } } & { \frac { \partial \mathbf { f } } { \partial \boldsymbol { \mu } } } \\ { \mathbf { 0 } } & { \mathbf { 0 } } \end{array} \right]
$$

so that the variational equation (2.7) gives the system

$$
{ \frac { \partial } { \partial t } } \left( { \frac { \partial \mathbf { y } } { \partial \mathbf { y } _ { 0 } } } \right) = { \frac { \partial \mathbf { f } } { \partial \mathbf { y } } } { \frac { \partial \mathbf { y } } { \partial \mathbf { y } _ { 0 } } } , ~ { \frac { \partial } { \partial t } } \left( { \frac { \partial \mathbf { y } } { \partial \mu } } \right) = { \frac { \partial \mathbf { f } } { \partial \mathbf { y } } } { \frac { \partial \mathbf { y } } { \partial \mu } } + { \frac { \partial \mathbf { f } } { \partial \mu } }
$$

with initial data

$$
{ \frac { \partial \mathbf { y } } { \partial \mathbf { y } _ { 0 } } } ( 0 ) = I , \quad { \frac { \partial \mathbf { y } } { \partial \pmb { \mu } } } ( 0 ) = \mathbf { 0 } .
$$

# Variational equation for second-order equations

If the equation of motion is of second order, like eq. (2.3), then we can decompose the state transition matrix as follows

$$
B = \frac { \partial \mathbf { x } } { \partial \mathbf { x } _ { 0 } } , \quad C = \frac { \partial \mathbf { x } } { \partial \mathbf { v } _ { 0 } } , \quad D = \frac { \partial \mathbf { x } } { \partial \pmb { \mu } } .
$$

We use here, and widely in this book, the dot notation $\dot { \mathbf { x } } = d \mathbf { x } / d t$ . Note that

$$
\dot { B } = \frac { \partial \mathbf { v } } { \partial \mathbf { x } _ { 0 } } , ~ \dot { C } = \frac { \partial \mathbf { v } } { \partial \mathbf { v } _ { 0 } } , ~ \dot { D } = \frac { \partial \mathbf { v } } { \partial \mu } .
$$

Then the variational equation is obtained by exchanging the derivatives: for $B$ and $C$ , with the double dot indicating second time derivatives,

$$
\begin{array}{c} \begin{array} { l } { \left\{ \begin{array} { l l } { \ddot { B } } & { = } \end{array} \frac { \partial { \bf h } } { \partial { \bf v } } \dot { B } + \frac { \partial { \bf h } } { \partial { \bf x } } B \right.} \\ { B ( t _ { 0 } ) } & { = } \end{array}   \\ { \left\{ \begin{array} { l l } { \ddot { C } } & { = } \end{array} \frac { \partial { \bf h } } { \partial { \bf v } } \dot { C } + \frac { \partial { \bf h } } { \partial { \bf x } } C } \\ { C ( t _ { 0 } ) } & { = \begin{array} { r } { { \bf 0 } , \dot { C } ( t _ { 0 } ) = I , } \end{array} \right. } \end{array}
$$

while for $D$ the linear equations are non-homogeneous

$$
\left\{ \begin{array} { l l l } { { \ddot { D } } } & { { = } } & { { \displaystyle \frac { \partial { \bf h } } { \partial { \bf v } } \dot { D } + \frac { \partial { \bf h } } { \partial { \bf x } } D + \frac { \partial { \bf h } } { \partial \mu } } } \\ { { D ( t _ { 0 } ) } } & { { = } } & { { \bf 0 } , { \dot { D } } ( t _ { 0 } ) = { \bf 0 } . } \end{array} \right.
$$

# Differentiability of the solutions

We state another regularity property of the integral flow. Let $\Omega \subseteq \mathbb { R } ^ { n }$ be an open set and $\mathbf { g } : \Omega \to \mathbb { R } ^ { n }$ a ${ \mathcal { C } } ^ { 1 }$ function. Then for each $\bar { \mathbf { z } } _ { 0 } \in \Omega$ there is an open set $W \subset \mathbb { R } \times \{ 2$ containing $( 0 , \bar { \bf z } _ { 0 } )$ such that the integral flow $\Phi ^ { t } ( \mathbf { z } _ { 0 } )$ restricted to $W$ is a $\mathcal { C } ^ { 1 }$ function in the variable $( t , { \bf z } _ { 0 } )$ . Furthermore the mixed derivatives $\partial ^ { 2 } \Phi ^ { t } ( { \bf z } _ { 0 } ) / \partial t \partial { \bf z } _ { 0 }$ exist and are continuous; in particular the procedure followed to obtain the variational equation (2.7) makes sense. The proof can be given using the variational equation itself and the Gronwall lemma. This result can also be extended to functions $\mathbf { g }$ of class $\mathcal { C } ^ { k }$ , getting solutions of class $\mathcal { C } ^ { k }$ in all the variables.

# 2.4 Lyapounov exponents

Given the solution ${ \bf z } ( t , { \bf z } _ { 0 } )$ of the Cauchy problem (2.2) let $\mathbf { v } ^ { t } ( \mathbf { z } _ { 0 } )$ be the solution of the variational equation (2.7). If the limit

$$
\operatorname* { l i m } _ { t \to + \infty } { \frac { 1 } { t } } \log { \frac { | \mathbf { v } ^ { t } ( \mathbf { z } _ { 0 } ) | } { | \mathbf { v } _ { 0 } | } }
$$

exists, we denote it by $\chi = \chi ( \mathbf { z } _ { 0 } , \mathbf { v } _ { 0 } )$ and we call it a Lyapounov exponent of the dynamical system. The inverse of the maximum positive Lyapounov exponent, if it exists, is the Lyapounov time over which two nearby orbits diverge, on average, by a factor exp(1).

Let us consider two different solutions ${ \bf z } _ { 1 } ( t ) , { \bf z } _ { 2 } ( t )$ of (2.2) obtained from different initial conditions ${ \bf z } _ { 1 } ( 0 ) , { \bf z } _ { 2 } ( 0 )$ . By the Gronwall lemma we have eq. (2.4):

$$
\Delta ( t ) = | \mathbf { z } _ { 1 } ( t ) - \mathbf { z } _ { 2 } ( t ) | \leq \Delta ( 0 ) \cdot \exp ( L t ) , \quad \mathrm { ~ s o ~ t h a t ~ } \quad \frac { 1 } { t } \log \frac { \Delta ( t ) } { \Delta ( 0 ) } \leq L .
$$

Passing to the limit as $\Delta ( 0 )  0$ and $t \to + \infty$ we obtain the inequality

$$
\chi ( \mathbf { z } _ { 0 } , \mathbf { v } _ { 0 } ) \leq L ,
$$

where $L$ is the Lipschitz constant of $\mathbf { g }$ . This inequality is sharp, as shown by the following example: the equation $d \mathbf { z } / d t = \lambda \mathbf { z }$ with initial condition ${ \bf z } ( 0 ) = { \bf z } _ { 0 }$ has solution $\mathbf { z } ( t ) = \exp ( \lambda t ) \mathbf { z } _ { 0 }$ and the difference $\Delta ( t )$ increases in size according to

$$
{ \frac { \Delta ( t ) } { \Delta ( 0 ) } } = { \frac { | { \bf z } _ { 1 } ( t ) - { \bf z } _ { 2 } ( t ) | } { | { \bf z } _ { 1 } ( 0 ) - { \bf z } _ { 2 } ( 0 ) | } } = \exp ( \lambda t ) , \quad \mathrm { ~ s o ~ t h a t ~ } \quad { \frac { 1 } { t } } \log { \frac { \Delta ( t ) } { \Delta ( 0 ) } } = \lambda ,
$$

that is, it has $\lambda$ as Lyapounov exponent.

# 2.5 Model problem dynamics

We shall consider the simple nonlinear problem

$$
\frac { d a } { d t } = 0 , \frac { d \lambda } { d t } = n ( a ) = \frac { k } { a ^ { 3 / 2 } }
$$

with initial conditions $a ( 0 ) = a _ { 0 } , \lambda ( 0 ) = \lambda _ { 0 }$ ; here $k > 0$ is the Gauss gravitational constant, that is $k ^ { 2 } = G m _ { \odot }$ . This problem is modeled on the planar two-body problem, with the nonlinear dependence of the mean motion upon the semimajor axis, in a zero eccentricity approximation; it is extensively used in Chapters 5, 6 and 7 as a model problem. The integral flow is a shift map

$$
a ( t , a _ { 0 } , \lambda _ { 0 } ) = a _ { 0 } , \lambda ( t , a _ { 0 } , \lambda _ { 0 } ) = \lambda _ { 0 } + n _ { 0 } t
$$

with $n _ { 0 } = n ( a _ { 0 } )$ , that is two initially nearby orbits diverge linearly with time; the Lyapounov exponents are all zero. The corresponding variational equation is as follows: the state transition matrix

$$
A ( t , a _ { 0 } , \lambda _ { 0 } ) = \frac { \partial ( a , \lambda ) } { \partial ( a _ { 0 } , \lambda _ { 0 } ) }
$$

is the solution of the Cauchy problem

$$
\frac { \partial A } { \partial t } = \left[ \begin{array} { c c } { 0 } & { 0 } \\ { - \frac { 3 } { 2 } \frac { n _ { 0 } } { a _ { 0 } } } & { 0 } \end{array} \right] ~ A , ~ A ( 0 ) = I .
$$

The integral flow of a linear Cauchy problem

$$
\frac { d \mathbf { z } } { d t } ( t ) = M \mathbf { z } ( t ) , \quad \mathbf { z } ( 0 ) = \mathbf { z } _ { 0 }
$$

where $M$ is an $n \times n$ matrix, is given by $\Phi ^ { t } ( { \bf z } _ { 0 } ) = \exp ( M t ) { \bf z } _ { 0 }$ where the matrix exponential is defined by

$$
\exp ( M t ) = \sum _ { i = 0 } ^ { \infty } \frac { M ^ { i } t ^ { i } } { i ! } .
$$

This series converges uniformly with respect to $t$ in every compact interval. For the case of eq. (2.15)

$$
A ( t , a _ { 0 } , \lambda _ { 0 } ) = \exp \left[ \begin{array} { c c } { { 0 } } & { { 0 } } \\ { { \displaystyle - \frac { 3 } { 2 } \frac { n _ { 0 } } { a _ { 0 } } t } } & { { 0 } } \end{array} \right] = \left[ \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { \displaystyle - \frac { 3 } { 2 } \frac { n _ { 0 } } { a _ { 0 } } t } } & { { 1 } } \end{array} \right] .
$$

The partial derivatives with respect to the dynamical parameter $k$

$$
B ( t , a _ { 0 } , \lambda _ { 0 } ) = \left[ \frac { \partial a ( t , a _ { 0 } , \lambda _ { 0 } ) } { \partial k } , \frac { \partial \lambda ( t , a _ { 0 } , \lambda _ { 0 } ) } { \partial k } \right] ^ { T }
$$

are the solution of the Cauchy problem

$$
\frac { \partial B } { \partial t } = \left[ \begin{array} { c c } { 0 } & { 0 } \\ { - \frac { 3 } { 2 } \frac { n _ { 0 } } { a _ { 0 } } } & { 0 } \end{array} \right] { \cal B } + \left[ \begin{array} { c } { 0 } \\ { \frac { 1 } { a _ { 0 } ^ { 3 / 2 } } } \end{array} \right] , \quad { \cal B } ( 0 ) = \left[ \begin{array} { c } { 0 } \\ { 0 } \end{array} \right]
$$

and can be written as

$$
{ \cal B } ( t , a _ { 0 } , \lambda _ { 0 } ) = \Big [ 0 , t / a _ { 0 } ^ { 3 / 2 } \Big ] ^ { T } .
$$

# ERROR MODELS

We outline the basic tools of probability theory needed in the following chapters, with special emphasis on the Gaussian, or normal, distributions, which have an essential connection with the least squares principle (see Section 5.7). We give very few proofs; the others can be found in many textbooks, e.g., (Jazwinski 1970, Mood et al. 1974).

# 3.1 Continuous random variables

A continuous random variable $X$ is defined by a probability density function, a real function ${ \mathsf p } _ { X } ( x ) \ge 0$ defined and continuous for all $x \in \mathbb { R }$ with the property

$$
\int _ { - \infty } ^ { + \infty } { \mathfrak { p } } _ { X } ( x ) d x = 1 .
$$

It follows that $X$ has also a distribution function ${ \mathsf { d } } _ { X } ( x )$ , defined for all $x \in \mathbb { R }$ and continuously differentiable:

$$
\mathsf { d } _ { X } ( x ) = \int _ { - \infty } ^ { x } \mathsf { p } _ { X } ( s ) d s , \quad \mathrm { s o ~ t h a t } \quad \mathsf { p } _ { X } ( x ) = \frac { d } { d x } \mathsf { d } _ { X } ( x ) ,
$$

by which we can compute a probability measure $\mathcal { P } _ { X }$ on $\mathbb { R }$ . The probability for $X$ to be inside an open interval $( a , b )$ is

$$
{ \mathcal { P } } _ { X } ( a < X < b ) = \mathbf { d } _ { X } ( b ) - \mathbf { d } _ { X } ( a ) = \int _ { a } ^ { b } { \mathsf { p } } _ { X } ( x ) d x .
$$

Note that ${ \mathcal { P } } _ { X } ( a \ < \ X \ < \ b ) \ = \ { \mathcal { P } } _ { X } ( a \ \leq \ X \ \leq \ b )$ , hence we have also a probability measure for the closed intervals $[ a , b ]$ . Because the probability density $\mathsf { p } _ { X } ( x )$ has a bounded integral, there is a large algebra of subsets $B$

of $\mathbb { R }$ such that the probability for $X$ to be inside can be computed by

$$
{ \mathcal { P } } _ { X } ( X \in B ) = \int _ { B } { \mathsf { p } } _ { X } ( x ) d x .
$$

Indeed, finite and countable infinite disjoint unions of open intervals are included, and the algebra is closed with respect to the complement; this is called the Borel $\sigma$ -algebra for $\mathbb { R }$ .1 The continuous random variables are not enough to describe all cases occurring in the applications, in particular in the measurement errors: there are also discrete distributions, and random variables $X$ can be defined as combinations of continuous and discrete ones, such that, for some $a$ , $\mathcal { P } _ { X } ( x = a ) > 0$ ; they cannot be represented by continuous distribution functions and have no probability density function. These do occur in the errors, e.g., whenever the data are digitized by hand the copyist mistakes are discrete. However, for a large data set this kind of mistake is not very important, and the use of continuous random variables as error models is justified when the largest errors, which are exceptional events and hard to model, are removed (see Section 5.8).

Given a continuous random variable $X$ , we use the following definitions:

$$
E ( X ) = \int _ { - \infty } ^ { + \infty } x \mathsf { p } _ { X } ( x ) d x \qquad { \mathrm { m e a n ~ ( o r ~ e x p e c t a t i o n ) , } }
$$

$$
\operatorname { V a r } ( X ) = \int _ { - \infty } ^ { + \infty } [ x - E ( X ) ] ^ { 2 } \mathfrak { p } _ { X } ( x ) d x \quad \mathbf { v }
$$

$$
K ( X ) = { \frac { \mu _ { 4 } ( X ) } { \operatorname { V a r } ( X ) ^ { 2 } } }
$$

# Jointly distributed random variables

Two continuous random variables $X , Y$ are jointly distributed if they are defined by a joint probability density function $\mathsf { p } _ { X , Y } ( x , y )$ which is con-

tinuous in the vector variable $( x , y ) \in \mathbb { R } ^ { 2 }$ and such that

$$
{ \mathsf p } _ { X , Y } ( x , y ) \ge 0 , ~ \int _ { \mathbb { R } ^ { 2 } } { \mathsf p } _ { X , Y } ( x , y ) ~ d x ~ d y = 1 .
$$

Following the same steps of the univariate case we can define a probability measure $\mathcal { P } _ { X , Y }$ : first we define

$$
{ \mathcal { P } } _ { X , Y } \left( { \begin{array} { l } { a < X < b } \\ { c < Y < d } \end{array} } \right) = \int _ { a } ^ { b } \ \int _ { c } ^ { d } { \mathsf { p } } _ { X , Y } ( x , y ) d x d y
$$

for the rectangles $( a , b ) \times ( c , d )$ , then we consider the subsets of $\mathbb { R } ^ { 2 }$ that are finite or countable infinite unions of rectangles, or the complement of them, i.e. the Borel $\sigma$ -algebra for $\mathbb { R } ^ { 2 }$ . If $\boldsymbol { D }$ is one of these subsets, we define2

$$
{ \mathcal { P } } _ { X , Y } ( D ) = \int _ { D } { \mathsf { p } } _ { X , Y } ( x , y ) d x d y .
$$

For the continuous random variables $X , Y$ we define the mean and the variance of $X$ :

$$
\begin{array} { r c l } { E ( X ) } & { = } & { \displaystyle \int _ { \mathbb { R } ^ { 2 } } x { \mathsf p } _ { X , Y } ( x , y ) d x d y , } \\ { \mathrm { V a r } ( X ) } & { = } & { \displaystyle \int _ { - \infty } ^ { + \infty } [ x - E ( X ) ] ^ { 2 } { \mathsf p } _ { X , Y } ( x , y ) d x d y , } \end{array}
$$

and similarly for $Y$ . Moreover we define the covariance of $X , Y$

$$
\begin{array} { r c l } { \operatorname { C o v } ( X , Y ) } & { = } & { \displaystyle \int _ { \mathbb { R } ^ { 2 } } [ x - E ( X ) ] [ y - E ( Y ) ] \mathsf { p } _ { X , Y } ( x , y ) d x d y } \\ & { = } & { \displaystyle E \left( [ X - E ( X ) ] [ Y - E ( Y ) ] \right) } \end{array}
$$

and the covariance matrix

$$
\Gamma = \left[ \begin{array} { c c } { { \mathrm { V a r } ( X ) } } & { { \mathrm { C o v } ( X , Y ) } } \\ { { \mathrm { C o v } ( X , Y ) } } & { { \mathrm { V a r } ( Y ) } } \end{array} \right] .
$$

The normal matrix is defined as $C = \Gamma ^ { - 1 }$ . The coefficient of correlation of $X$ and $Y$ is the ratio

$$
\operatorname { C o r r } ( X , Y ) = { \frac { \operatorname { C o v } ( X , Y ) } { { \sqrt { \operatorname { V a r } ( X ) } } { \sqrt { \operatorname { V a r } ( Y ) } } } }
$$

and we shall say that the two variables are uncorrelated if this coefficient is zero, correlated if it is not zero.

It is possible to generalize these definitions to $n$ jointly distributed continuous random variables $X _ { 1 } , \ldots , X _ { n }$ . They are defined by a joint probability

density function $\mathsf { p } _ { X _ { 1 } , X _ { 2 } , \ldots , X _ { n } } \left( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } \right)$ which is non-negative, continuous in all the variables, and has unit integral on $\mathbb { R } ^ { n }$ . The probability measure of a subset $D$ of $\mathbb { R } ^ { n }$ can be computed as the multiple integral

$$
{ \mathcal { P } } _ { X _ { 1 } , \ldots , X _ { n } } \left( \left( X _ { 1 } , X _ { 2 } , \ldots , X _ { n } \right) \in D \right) = \int _ { D } { \mathsf { p } } _ { X _ { 1 } , X _ { 2 } , \ldots , X _ { n } } d x _ { 1 } d x _ { 2 } \ldots d x _ { n }
$$

provided $D$ satisfies conditions like those of the two-dimensional case.

Given $n$ jointly distributed continuous random variables $X _ { j }$ , $j = 1 , n$ , the mean and the variance of each variable is

$$
\begin{array} { r c l } { E ( X _ { j } ) } & { = } & { \displaystyle \int _ { \mathbb R ^ { n } } x _ { j } \mathsf { p } _ { X _ { 1 } , \ldots , X _ { n } } \left( x _ { 1 } , \ldots , x _ { n } \right) d x _ { 1 } \ldots d x _ { n } , } \\ { \mathrm { V a r } ( X _ { j } ) } & { = } & { \displaystyle \int _ { \mathbb R ^ { n } } \left[ x _ { j } - E ( X _ { j } ) \right] ^ { 2 } \mathsf { p } _ { X _ { 1 } , \ldots , X _ { n } } \left( x _ { 1 } , \ldots , x _ { n } \right) d x _ { 1 } \ldots d x _ { n } , } \end{array}
$$

the covariance of $X _ { i } , X _ { j }$ is

$$
( X _ { i } , X _ { j } ) = \int _ { \mathbb { R } ^ { n } } [ x _ { i } - E ( X _ { i } ) ] [ x _ { j } - E ( X _ { j } ) ] \ { \mathsf { p } } _ { X _ { 1 } , \ldots , X _ { n } } ( x _ { 1 } , \ldots , x _ { n } ) d x _ { 1 } \ldots d x
$$

and the normal matrix $C$ is the inverse of the covariance matrix $\Gamma = ( \gamma _ { i j } ) _ { i , j }$ whose coefficients are $\gamma _ { i i } = \mathrm { V a r } ( X _ { i } )$ and $\gamma _ { i j } = \operatorname { C o v } ( X _ { i } , X _ { j } )$ for $i \neq j$ . The correlation coefficients can also be deduced from the covariance matrix

$$
\mathrm { C o r r } ( X _ { i } , X _ { j } ) = \frac { \gamma _ { i j } } { \sqrt { \gamma _ { i i } \gamma _ { j j } } } .
$$

# Independence, marginal and conditional probability

For two jointly distributed random variables $X , Y$ we define the marginal density functions

$$
{ \mathsf { p } } _ { X } ( x ) = \int _ { - \infty } ^ { + \infty } { \mathsf { p } } _ { X , Y } ( x , y ) d y , \quad { \mathsf { p } } _ { Y } ( y ) = \int _ { - \infty } ^ { + \infty } { \mathsf { p } } _ { X , Y } ( x , y ) d x ,
$$

which can be regarded as probability densities of one of the jointly distributed random variables, valid for each value of the other variable.

The jointly distributed $X , Y$ are independent random variables if

$$
{ \mathsf { p } } _ { X , Y } ( x , y ) = { \mathsf { p } } _ { X } ( x ) { \mathsf { p } } _ { Y } ( y ) .
$$

If $X$ , $Y$ are independent, $\operatorname { C o v } ( X , Y ) = 0$ . The converse is not always true.

Given $X , Y$ continuous random variables with probability density $\mathsf { p } _ { X , Y } ( x , y )$ the conditional density functions are

$$
p _ { X | Y } ( x ; y ) = \frac { \mathsf { p } _ { X , Y } ( x , y ) } { \mathsf { p } _ { Y } ( y ) } , ~ p _ { Y | X } ( y ; x ) = \frac { \mathsf { p } _ { X , Y } ( x , y ) } { \mathsf { p } _ { X } ( x ) } ,
$$

for $\mathsf { p } _ { Y } ( y ) > 0$ and $\mathsf { p } _ { X } ( x ) > 0$ , respectively, where we use “;” to stress the different role of the two variables. The independence of $X$ and $Y$ can be expressed in terms of conditional density functions as either $p _ { Y | X } ( y ; x ) =$ $\mathsf p _ { Y } ( y )$ or $p _ { X | Y } ( x ; y ) = \mathsf { p } _ { X } ( x )$ .

# 3.2 Gaussian random variables

There are continuous random variables that play an important role in the least squares principle: those with density function of the type

$$
{ \sf p } _ { X } ( x ) = N ( \mu , \sigma ^ { 2 } ) ( x ) = \frac { 1 } { \sqrt { 2 \pi } \sigma } \exp \left( - \frac { ( x - \mu ) ^ { 2 } } { 2 \sigma ^ { 2 } } \right) ,
$$

where $\mu = E ( X )$ and $\sigma = \mathrm { R M S } ( X )$ . Such variables are called Gaussian or normally distributed. The following relation is useful:

$$
\int _ { - \infty } ^ { + \infty } \exp \left( - \frac { x ^ { 2 } } { 2 \sigma ^ { 2 } } \right) ~ d x = \sqrt { 2 \pi } \sigma ;
$$

it can be computed from the integral over the plane $\mathbb { R } ^ { 2 }$ of the function $\exp \left( x ^ { 2 } + y ^ { 2 } \right)$ in polar coordinates. It can be easily checked that a Gaussian variable satisfies the property (3.1) of a probability density function.

# Rotational invariance

A geometric characterization of the Gaussian densities is as follows. If two jointly distributed continuous random variables $X , Y$ are independent, with equal marginal densities ${ \mathsf { p } } _ { X } ( x ) = { \mathsf { p } } _ { Y } ( x ) = f ( x )$ and the probability density function $\mathsf { p } _ { X , Y } ( x , y )$ is invariant under rotations, i.e., there exists a function $g : \mathbb { R } \to \mathbb { R }$ such that ${ \mathsf p } _ { X , Y } ( x , y ) = g ( x ^ { 2 } + y ^ { 2 } )$ , then they are Gaussian with zero mean:

$$
\mathsf { p } _ { X } ( x ) = N ( 0 , \sigma ^ { 2 } ) ( x ) .
$$

This can be shown as follows:

$$
g ( x ^ { 2 } + y ^ { 2 } ) = f ( x ) \ f ( y ) \Longrightarrow g ( x ^ { 2 } ) = f ( x ) \ f ( 0 )
$$

where $f ( 0 ) = k$ is constant. Thus $f ( x ) = g ( x ^ { 2 } ) / k = k h ( x ^ { 2 } )$ and by substituting in the formula above

$$
h ( x ^ { 2 } + y ^ { 2 } ) = h ( x ^ { 2 } ) \ h ( y ^ { 2 } ) \Longrightarrow \log h ( x ^ { 2 } ) + \log h ( y ^ { 2 } ) = \log h ( x ^ { 2 } + y ^ { 2 } ) ,
$$

thus $\log h ( z )$ is a linear function: $\log h ( x ^ { 2 } ) = s x ^ { 2 }$ and $f ( x ) = k \exp ( s x ^ { 2 } )$ . For $f$ to have a limited integral, $s$ must be negative, say $s = - 1 / 2 \sigma ^ { 2 }$ and

$$
{ \sf p } _ { X } ( x ) = f ( x ) = k \exp \left( - \frac { 1 } { 2 \sigma ^ { 2 } } \right) .
$$

Then the normalization property (3.1) implies $k = 1 / \sigma \sqrt { 2 \pi }$ . Hence the two-dimensional rotation invariant Gaussian is

$$
{ \mathsf { p } } _ { X , Y } ( x , y ) = N ( 0 , \sigma ^ { 2 } ) ( x ) N ( 0 , \sigma ^ { 2 } ) ( y ) = { \frac { 1 } { 2 \pi \sigma ^ { 2 } } } \exp \left( - { \frac { x ^ { 2 } + y ^ { 2 } } { 2 \sigma ^ { 2 } } } \right) .
$$

# Two-dimensional Gaussian variables

We take two independent jointly distributed Gaussian variables $X , Y$ with joint density function ${ \mathsf { p } } _ { X , Y } ( x , y ) = { \mathsf { p } } _ { X } ( x ) { \mathsf { p } } _ { Y } ( y )$ with zero mean and different standard deviations $\sigma _ { x } , \sigma _ { y }$ . In this case the covariance matrix is

$$
\Gamma = \left( \begin{array} { c c } { { \sigma _ { x } ^ { 2 } } } & { { 0 } } \\ { { 0 } } & { { \sigma _ { y } ^ { 2 } } } \end{array} \right) ,
$$

the normal matrix is $C = \Gamma ^ { - 1 }$ and the joint probability density is

$$
\begin{array} { r c l } { { \mathsf { p } _ { X , Y } ( x , y ) = N ( 0 , \Gamma ) ( x , y ) } } & { { = } } & { { \displaystyle \frac { \sqrt { \operatorname* { d e t } C } } { 2 \pi } \exp \left[ - \frac { 1 } { 2 } ( x , y ) C \left( \begin{array} { c } { { x } } \\ { { y } } \end{array} \right) \right] } } \\ { { } } & { { = } } & { { \displaystyle \frac { 1 } { 2 \pi \sigma _ { x } \sigma _ { y } } \exp \left[ - \frac { 1 } { 2 } \left( \frac { x ^ { 2 } } { \sigma _ { x } ^ { 2 } } + \frac { y ^ { 2 } } { \sigma _ { y } ^ { 2 } } \right) \right] . } } \end{array}
$$

More generally, let us consider two correlated Gaussian random variables $X , Y$ , with normal matrix $C$ and covariance matrix $\Gamma$ defined by

$$
C = \frac { 1 } { 1 - \rho ^ { 2 } } \left( \begin{array} { c c } { { 1 / \sigma _ { x } ^ { 2 } } } & { { - \rho / ( \sigma _ { x } \sigma _ { y } ) } } \\ { { - \rho / ( \sigma _ { x } \sigma _ { y } ) } } & { { 1 / \sigma _ { y } ^ { 2 } } } \end{array} \right) , \Gamma = \left( \begin{array} { c c } { { \sigma _ { x } ^ { 2 } } } & { { \rho \sigma _ { x } \sigma _ { y } } } \\ { { \rho \sigma _ { x } \sigma _ { y } } } & { { \sigma _ { y } ^ { 2 } } } \end{array} \right)
$$

where $\rho = \operatorname { C o r r } ( X , Y )$ . The marginal probability densities are the same as in the independent case:

$$
\mathsf { p } _ { X } ( x ) = N ( 0 , \sigma _ { x } ^ { 2 } ) ( x ) , ~ \mathsf { p } _ { Y } ( y ) = N ( 0 , \sigma _ { y } ^ { 2 } ) ( y ) ,
$$

but the joint probability density is different:

$$
\begin{array} { l l l } { \displaystyle { \mathit { \Sigma } _ { Y } ( x , y ) } } & { = } & { \displaystyle N ( 0 , \Gamma ) ( x , y ) } \\ & { = } & { \displaystyle \frac { 1 } { 2 \pi \sigma _ { x } \sigma _ { y } \sqrt { 1 - \rho ^ { 2 } } } \exp \left[ - \frac { 1 } { 2 ( 1 - \rho ^ { 2 } ) } \left( \frac { x ^ { 2 } } { \sigma _ { x } ^ { 2 } } - \frac { 2 \rho x y } { \sigma _ { x } \sigma _ { y } } + \frac { y ^ { 2 } } { \sigma _ { y } ^ { 2 } } \right) \right] } \end{array}
$$

The result is valid also for jointly distributed continuous random variables with non-zero mean: in this case the density function is

$$
\begin{array} { l l l } { { \sf p } _ { X , Y } ( x , y ) } & { { = } } & { { N ( { \bf m } , { \Gamma } ) ( x , y ) \mathrm { ~ } } } \\ { { \mathrm { } } } & { { = } } & { { \displaystyle \frac { \sqrt { \operatorname* { d e t } C } } { 2 \pi } \exp \left[ - \frac { 1 } { 2 } ( x - m _ { x } , y - m _ { y } ) C \left( \begin{array} { l } { { x - m _ { x } } } \\ { { y - m _ { y } } } \end{array} \right) \right] } } \end{array}
$$

where

$$
{ \bf m } = ( m _ { x } , m _ { y } ) = ( E ( X ) , E ( Y ) ) ;
$$

the marginal density functions of $X$ and $Y$ are normal

$$
\mathsf { p } _ { X } ( x ) = N ( m _ { x } , \sigma _ { x } ^ { 2 } ) , ~ \mathsf { p } _ { Y } ( y ) = N ( m _ { y } , \sigma _ { y } ^ { 2 } ) .
$$

Moreover, if $\operatorname { C o r r } ( X , Y ) = 0$ then both the normal and the covariance matrix are diagonal, and $X , Y$ are independent.

# Regression line

Given two jointly distributed Gaussian variables $X , Y$ , with probability density (3.6), the conditional probability density of $X$ given $Y$ is also Gaussian:

$$
p _ { X | Y } ( x ; y ) = N \left( m _ { x } + \rho \frac { \sigma _ { x } } { \sigma _ { y } } ( y - m _ { y } ) , \sigma _ { x } ^ { 2 } ( 1 - \rho ^ { 2 } ) \right) ( x ) .
$$

The above formula uses the regression line

$$
y = m _ { y } + \frac { \sigma _ { y } } { \sigma _ { x } } \rho ( x - m _ { x } ) ,
$$

giving the expected conditional value $\begin{array} { r } { E [ Y | X ] ( x ) = \int _ { \mathbb { R } } p _ { Y | X } ( y ; x ) } \end{array}$ dy. A similar formula gives the conditional probability density of $Y$ given $X$

$$
p _ { Y | X } ( y ; x ) = N \left( m _ { y } + \rho \frac { \sigma _ { y } } { \sigma _ { x } } ( x - m _ { x } ) , \sigma _ { y } ^ { 2 } ( 1 - \rho ^ { 2 } ) \right) ( y ) ,
$$

which uses the other regression line

$$
x = m _ { x } + \frac { \sigma _ { x } } { \sigma _ { y } } \rho ( y - m _ { y } ) .
$$

The regression lines are shown in Figure 5.1.

# Multidimensional Gaussian variables

Given $n$ jointly distributed random variables $X _ { 1 } , X _ { 2 } , \ldots , X _ { n }$ , we say that they are Gaussian, or normally distributed, if their joint density function is of the form

$$
{ \bf \sf { \sf { 3 } } } _ { X _ { 1 } , X _ { 2 } , \ldots , X _ { n } } \left( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } \right) = \frac { \sqrt { \operatorname* { d e t } C } } { ( 2 \pi ) ^ { n / 2 } } \exp \left[ - \frac { 1 } { 2 } ( { \bf x - m } ) ^ { T } C \left( { \bf x - m } \right) \right]
$$

where $\mathbf { m } = ( m _ { 1 } , \ldots , m _ { n } ) ^ { T }$ is the vector of the means and $C$ , the normal matrix, is symmetric and positive definite. The notation $N ( \mathbf { m } , \Gamma )$ is used for the above probability density function, where $\Gamma = C ^ { - 1 }$ . Again, if $C$ is

diagonal so is $\Gamma$ , and the $X _ { j }$ are all independent: for Gaussian variables, being independent and uncorrelated is equivalent.

For a multidimensional Gaussian, we need to generalize the result on marginal probability densities: let us consider the two vector random variables

$$
{ \bf X } = ( X _ { 1 } , \ldots , X _ { n } ) , \quad { \bf Y } = ( Y _ { 1 } , \ldots , Y _ { m } )
$$

jointly distributed, Gaussian with probability density

$$
\mathbf { p } _ { \mathbf { X } , \mathbf { Y } } ( \mathbf { x } , \mathbf { y } ) = N \left( ( \mathbf { m } _ { \mathbf { x } } ; \mathbf { m } _ { \mathbf { y } } ) , \Gamma _ { \mathbf { x } \mathbf { y } } \right) ,
$$

where $\mathbf { x } = ( x _ { 1 } , \ldots , x _ { n } )$ , $\mathbf { y } = ( y _ { 1 } , \dots y _ { m } )$ , $( \mathbf { m } _ { \mathbf { x } } ; \mathbf { m } _ { \mathbf { y } } )$ is the stacking of the two vectors, and the covariance matrix can be decomposed as

$$
\begin{array} { r } { \Gamma = \left[ \begin{array} { l l } { \Gamma _ { \mathbf { x } } } & { \Gamma _ { \mathbf { x } \mathbf { y } } } \\ { \Gamma _ { \mathbf { y } \mathbf { x } } } & { \Gamma _ { \mathbf { y } } } \end{array} \right] , \quad \Gamma _ { \mathbf { y } \mathbf { x } } = \Gamma _ { \mathbf { x } \mathbf { y } } ^ { T } , } \end{array}
$$

where $\Gamma _ { \mathbf { x } }$ is an $n \times n$ matrix, $\Gamma _ { \mathbf { y } }$ is $m \times m$ , and $\Gamma _ { \mathbf { x } \mathbf { y } }$ is $n \times m$ . Then the marginal probability densities are

$$
\mathsf { p } \mathbf { x } = N ( \mathbf { m } _ { \mathbf { x } } , \Gamma _ { \mathbf { x } } ) , \quad \mathsf { p } \mathbf { y } = N ( \mathbf { m } _ { \mathbf { y } } , \Gamma _ { \mathbf { y } } ) ,
$$

that is the marginal covariance matrix is the restriction, to the corresponding linear subspace, of the covariance matrix. For the conditional covariance matrix the following formula applies

$$
p _ { X | Y } ( x ; y ) = N ( \mathbf { m _ { x } } + \Gamma _ { \mathbf { x y } } \Gamma _ { \mathbf { y } } ^ { - 1 } ( \mathbf { y } - \mathbf { m _ { y } } ) , \Gamma _ { \mathbf { x } } - \Gamma _ { \mathbf { x y } } \Gamma _ { \mathbf { y } } ^ { - 1 } \Gamma _ { \mathbf { y x } } ) ,
$$

which can be described by the statement that the conditional normal matrix $C ^ { \bf x }$ is the restriction, to the corresponding linear subspace, of the normal matrix $C = \Gamma ^ { - 1 }$ . Similarly for $p _ { Y | X } ( y ; x )$ , see Section 5.4.

# 3.3 Expected values and transformations

Given a continuous random variable $X$ and a continuous real function $f ( x )$ , we can define the random variable $Y = F ( X )$ with probability measure

$$
{ \mathcal { P } } _ { Y } ( a < Y < b ) = { \mathcal { P } } _ { X } ( X : a < F ( X ) < b ) ~ .
$$

The question is whether $Y$ is a continuous random variable, i.e., whether a continuous probability density function $\mathsf p _ { Y } ( y )$ can be defined. Under the assumptions

(i) $y = f ( x )$ is bijective from $W = \{ x \in \mathbb { R } : { \mathsf { p } } _ { X } ( x ) > 0 \}$ to a set $D \subset \mathbb { R }$ ;   
(ii) $x = f ^ { - 1 } ( y )$ has in $\boldsymbol { D }$ continuous derivative, different from 0;

$Y = F ( X )$ is a continuous random variable with probability density

$$
{ \mathsf { p } } _ { Y } ( y ) = \left| { \frac { d f ^ { - 1 } ( y ) } { d y } } \right| { \mathsf { p } } _ { X } { \bigl ( } f ^ { - 1 } ( y ) { \bigr ) }
$$

inside $D$ and 0 outside.

This definition can be generalized to $n$ variables as follows. Given a set $\mathbf { X } = \left( X _ { 1 } , \ldots , X _ { n } \right)$ of jointly distributed continuous random variables with probability density function $p _ { \mathbf { X } } ( \mathbf { x } )$ , where $\mathbf { x } = ( x _ { 1 } , \ldots , x _ { n } )$ , and given a continuous function $\mathbf { f } \left( \mathbf { x } \right) = \mathbf { y }$ , with $\mathbf { y } = ( y _ { 1 } , \dots , y _ { n } )$ , let

$$
W = \{ \mathbf { x } \in \mathbb { R } ^ { n } \ \mathrm { s u c h \ t h a t \ p \mathbf { x } \left( \mathbf { x } \right) > 0 } \}
$$

and $D = \mathbf { f } ( W )$ , with $\mathbf { f } : W  D$ a bijective function. If $\mathbf { f } ^ { - 1 } \in \mathcal { C } ^ { 1 } ( D )$ with Jacobian $J$ different from zero, then

$$
\mathsf { p } _ { \mathbf { Y } } ( \mathbf { y } ) = | \operatorname* { d e t } J | \mathsf { p } _ { \mathbf { X } } ( \mathbf { f } ^ { - 1 } ( \mathbf { y } ) )
$$

inside $\boldsymbol { D }$ , $0$ outside, is the probability density that defines the continuous vector random variable $\mathbf { Y } = \mathbf { F } ( \mathbf { X } )$ .

# Linear transformations of Gaussians

Given a continuous random variable $\mathbf { X }$ , let $\mathbf { y } = \mathbf { f } ( \mathbf { x } ) = A \mathbf { x } + \mathbf { b }$ , with $A$ an $n \times n$ matrix, be an affine transformation in $\mathbb { R } ^ { n }$ . If $\mathbf { X }$ is Gaussian, with probability density $\mathsf { p } _ { \mathbf { X } } ( \mathbf { x } ) = N ( \mathbf { m } , \Gamma )$ , $\mathbf { m } \in \mathbb { R } ^ { n }$ and $\Gamma$ a symmetric positive definite $n \times n$ matrix, then $\mathbf { Y } = \mathbf { F } ( \mathbf { X } )$ also has a normal distribution, with probability density

$$
\mathsf { p } _ { \mathbf { Y } } ( \mathbf { y } ) = N \left( A \mathbf { m } + \mathbf { b } , A \Gamma A ^ { T } \right) ,
$$

that is, with expected value $\mathbf { f } ( \mathbf { m } )$ and covariance matrix $A \Gamma A ^ { T }$ . This is called the covariance propagation rule.

In this case the transformation is invertible: $\mathbf { x } \ = \ A ^ { - 1 } \left( \mathbf { y } \ - \ \mathbf { b } \right)$ with $\operatorname* { d e t } \partial \mathbf { x } / \partial \mathbf { y } = \operatorname* { d e t } ^ { - 1 } ( A )$ . Then eq. (3.8), by using $\mathbf { x } - \mathbf { m } = A ^ { - 1 } \left[ \mathbf { y } - \mathbf { f } ( \mathbf { m } ) \right]$ and $( A ^ { I ^ { \prime } } ) ^ { - 1 } C A ^ { - 1 } = ( A \Gamma A ^ { I ^ { \prime } } ) ^ { - 1 }$ , gives

$$
\begin{array} { l } { { \displaystyle { \bf { y } } ) \ = \ \frac { \sqrt { \operatorname* { d e t } C \left( \operatorname* { d e t } A \right) ^ { - 2 } } } { { \left( 2 \pi \right) } ^ { n / 2 } } \exp \left[ - \frac 1 2 [ { \bf { y } } - { \bf { f } } ( { \bf { m } } ) ] ^ { T } \left( A ^ { T } \right) ^ { - 1 } C A ^ { - 1 } \left[ { \bf { y } } - { \bf { f } } ( { \bf { m } } ) \right] \right]}  } \ ~  \\ { { \displaystyle = \ \frac { \sqrt { \operatorname* { d e t } ( A \Gamma A ^ { T } ) ^ { - 1 } } } { { \left( 2 \pi \right) } ^ { n / 2 } } \exp \left[ - \frac 1 2 [ { \bf { y } } - { \bf { f } } ( { \bf { m } } ) ] ^ { T } \left( A \Gamma A ^ { T } \right) ^ { - 1 } [ { \bf { y } } - { \bf { f } } ( { \bf { m } } ) ] \right] } \ ~ } \\ { = \ N \left( { \bf { f } } ( { \bf { m } } ) , A \Gamma A ^ { T } \right) . } \end{array}
$$

A generalization to transformations $\mathbf { y } = \mathbf { f } ( \mathbf { x } ) = B \left( \mathbf { x } + \mathbf { b } \right)$ of the Gaussian variable $\mathbf { X }$ with density $N ( \mathbf { m } , \Gamma )$ , where $B$ is an $m \times n$ matrix ( $m < n$ ) with maximal rank $m$ , can be obtained as follows. Let $\Pi = \lfloor I \vert \mathbf { 0 } \rfloor$ be the matrix of the projection onto the subspace of the first $m$ coordinates and let $A$ be an invertible $n \times n$ matrix with $B = \Pi A$ : we use relation (3.9) to compute the probability density $N ( A ( \mathbf { m } + \mathbf { b } ) , A \Gamma A ^ { \prime } )$ of the random variable defined by the invertible transformation ${ \bf z } = A ( { \bf x } + { \bf b } )$ , and then relation (3.6), about marginal densities, to obtain

$$
\mathsf { p } _ { \mathbf { Y } } ( \mathbf { y } ) = N \left( \Pi A ( \mathbf { m } + \mathbf { b } ) , \Pi A \Gamma A ^ { T } \Pi ^ { T } \right) = N \left( \mathbf { f } ( \mathbf { m } ) , B \Gamma B ^ { T } \right) .
$$

# Conditional probability density on a linear subspace

We need to generalize the formula for the conditional probability density of a Gaussian to an ambient space of arbitrary dimension $m$ and to an affine subset of arbitrary dimension $N < m$ ; this is used in Section 5.7.

Let $W$ be an $N$ -plane, image of $\mathbb { R } ^ { N }$ by a linear (non-homogeneous) map defined by the $m \times N$ matrix $B$ and the reference point $\xi ^ { * }$

$$
W = \{ \pmb { \xi } \in \mathbb { R } ^ { m } : \pmb { \xi } = B \mathbf { x } + \pmb { \xi } ^ { * } , \mathbf { x } \in \mathbb { R } ^ { N } \} ;
$$

moreover, we may assume that $\xi ^ { * }$ is a vector orthogonal to $W$ (otherwise the component parallel to $W$ can be subtracted). Let $\mathsf { p } \mathsf { \Xi } ( \pmb { \xi } ) = N ( 0 , I )$ b e a rotation-invariant Gaussian probability density; we need to compute the conditional probability density of the random variable $\Xi$ on $W$ .

We use a rotation matrix $R$ such that

$$
R \left( \pmb { \xi } - \pmb { \xi } ^ { * } \right) = \left[ \begin{array} { c } { \pmb { \xi } ^ { \prime } } \\ { \pmb { \xi } ^ { \prime \prime } } \end{array} \right] \Longrightarrow R ^ { T } \left[ \begin{array} { c } { \mathbf { 0 } } \\ { \pmb { \xi } ^ { \prime \prime } } \end{array} \right] + \pmb { \xi } ^ { * } \in W ,
$$

that is, $\pmb { \xi } ^ { \prime \prime } \in \mathbb { R } ^ { N }$ parameterizes $W$ . The probability density of $\Xi ^ { \prime \prime }$ is the conditional probability density of $R ( \Xi )$ given $\xi ^ { \prime } = R \xi ^ { * }$ , but the distribution $N ( \mathbf { 0 } , I )$ is rotation invariant, thus the probability density of $\Xi ^ { \prime \prime }$ can be computed from eq. (3.7) and $\Xi ^ { \prime \prime }$ is Gaussian with as normal matrix the restriction of the normal matrix of $\Xi$

$$
\mathsf { p } _ { \Xi ^ { \prime \prime } } = N ( \mathbf { 0 } , I )
$$

with $I$ the $N \times N$ identity matrix. Geometrically, the intersection of $( m - 1 )$ - spheres with $N$ -planes can only be $( N - 1 )$ -spheres, and these are the level surfaces of the probability density of $\Xi ^ { \prime \prime }$ .

# 4

# THE N–BODY PROBLEM

This chapter presents the basic theory of the gravitational $N$ -body problem, the coordinate systems used for both theoretical investigations and practical applications, and how to select the dynamical model for a Solar System orbit.

# 4.1 Equation of motion and integrals

By $( N { + } 1 )$ -body problem we mean the ordinary differential equation defining the motion of $N + 1$ point masses with positions $\mathbf { r } _ { j }$ , velocities $\dot { \mathbf { r } } _ { j }$ , and masses $m _ { j }$ , interacting only through the mutual gravitational attraction

$$
m _ { j } { \ddot { \mathbf { r } } } _ { j } = \sum _ { i \neq j } { \frac { G m _ { i } m _ { j } } { | \mathbf { r } _ { i } - \mathbf { r } _ { j } | ^ { 3 } } } ( \mathbf { r } _ { i } - \mathbf { r } _ { j } ) , \quad j = 0 , \ldots , N
$$

where the dots indicate time derivatives and $G$ is the universal gravitational constant; this is the equation of motion in Newtonian form. We need to express it in another form, more suitable both to discuss symmetries and integrals and to perform coordinate changes. The mutual gravitational forces admit a potential, thus we can define the potential energy

$$
V = - \sum _ { 0 \leq i < j \leq N } { \frac { G m _ { i } m _ { j } } { | \mathbf { r } _ { i } - \mathbf { r } _ { j } | } } ;
$$

we introduce the kinetic energy $T$ and the Lagrange function (or Lagrangian) $L$ :

$$
T = { \frac { 1 } { 2 } } \sum _ { i = 0 } ^ { N } m _ { i } \ \vert { \dot { \mathbf { r } } } _ { i } \vert ^ { 2 } , L = T - V .
$$

The Newton equation of motion is equivalent to the Lagrange equation

$$
{ \frac { d } { d t } } \left( { \frac { \partial L } { \partial { \dot { \mathbf { r } } } _ { j } } } \right) - { \frac { \partial L } { \partial \mathbf { r } _ { j } } } = \mathbf { 0 }
$$

with two important properties. The first one has to do with integrals of motion, the second is discussed in Section 4.2. A first integral of the Lagrange equation (4.3) is a function of all the positions and velocities

$$
I = I ( { \bf R } , { \dot { \bf R } } ) , \quad { \bf R } = ( { \bf r } _ { 0 } , { \bf r } _ { 1 } , \ldots , { \bf r } _ { N } ) , \quad { \dot { \bf R } } = ( { \dot { \bf r } } _ { 0 } , { \dot { \bf r } } _ { 1 } , \ldots , { \dot { \bf r } } _ { N } )
$$

such that the total time derivative along the solutions is identically zero:

$$
\frac { d I } { d t } = \frac { \partial I } { \partial { \bf R } } \dot { \bf R } + \frac { \partial I } { \partial \dot { \bf R } } \ddot { \bf R } = 0 ;
$$

thus the value of $I$ is constant along the orbits.

# Symmetries and integrals

A one-parameter group of symmetries of the Lagrange function $L$ is a diffeomorphism $F ^ { s }$ of the positions $\mathbf { R }$ depending (in a differentiable way) upon a parameter $s \in \mathbb R$ so that $F ^ { s } \circ F ^ { z } = F ^ { s + z }$ and the Lagrange function is invariant:

$$
L \left( F ^ { s } ( { \bf R } ) , \frac { d } { d t } F ^ { s } ( { \bf R } ) \right) = L \left( F ^ { s } ( { \bf R } ) , \frac { \partial F ^ { s } } { \partial { \bf R } } \dot { \bf R } \right) = L ( { \bf R } , \dot { \bf R } ) .
$$

$F ^ { 0 }$ is the identity transformation; we also assume the mixed derivatives $\partial ^ { 2 } F ^ { s } / \partial \mathbf { R } \partial s$ are continuous. A local one-parameter group of symmetries of the Lagrange function is defined by the same properties for $s$ in a neighborhood of $0$ . The main result we need is the Noether theorem, stating that if the Lagrange function $L$ admits a local one-parameter group of symmetries $F ^ { s }$ then

$$
I ( { \bf R } , \dot { \bf R } ) = \frac { \partial L } { \partial \dot { \bf R } } \cdot \left. \frac { \partial F ^ { s } ( { \bf R } ) } { \partial s } \right| _ { s = 0 }
$$

is a first integral of the Lagrange equation (4.3).

To apply this theorem to the $( N + 1 )$ -body problem we look for symmetries of the Lagrange function in (4.2), a function of the mutual distances $| \mathbf { r } _ { i } - \mathbf { r } _ { j } |$ and of the velocities $\left| { \dot { \mathbf { r } } } _ { j } \right|$ . Thus every isometry of the space of positions, preserving distances and independent of time, preserves the Lagrange function. The isometries of the Euclidean space $\mathbb { R } ^ { 3 }$ are the functions

$$
G ( \mathbf { x } ) = R \mathbf { x } + \mathbf { q } , { \frac { d G } { d t } } ( \mathbf { x } ) = R { \dot { \mathbf { x } } } ,
$$

where $R$ is an orthogonal matrix ( $R ^ { T } ~ R = I$ ) and $\mathbf { q }$ a constant vector, both independent of time. The symmetry group of three-dimensional space has

dimension 6 and is generated by six one-parameter subgroups.1 There are three one-parameter symmetry groups of translations ( $R = I$ ):

$$
F ^ { s } ( { \bf x } ) = { \bf x } + s \hat { \bf v } _ { h } , \quad \frac { \partial F ^ { s } ( { \bf x } ) } { \partial s } = \hat { \bf v } _ { h }
$$

where $\hat { \mathbf { v } } _ { h }$ is the unit vector along one coordinate axis, for $h = 1 , 2 , 3$ . If equal translations are applied to all bodies, then the integral of (4.4) is

$$
p _ { h } = \hat { \mathbf { v } } _ { h } \cdot \sum _ { j = 0 } ^ { N } m _ { j } \ \dot { \mathbf { r } } _ { j } ,
$$

the component along the axis $\hat { \mathbf { v } } _ { h }$ of the total linear momentum $\mathbf { p }$ . The latter is a vector integral, and the center of mass $\mathbf { b } _ { 0 }$ moves with constant velocity:

$$
0 = \frac { 1 } { M _ { 0 } } \sum _ { j = 0 } ^ { N } m _ { j } { \bf r } _ { j } ; M _ { 0 } = \sum _ { j = 0 } ^ { N } m _ { j } ( \mathrm { t o t a l m a s s } ) ; { \bf b } _ { 0 } ( t ) = \frac { t } { M _ { 0 } } { \bf p } + { \bf b } _ { 0 }
$$

In the above formula, ${ \bf b } _ { 0 } ( 0 )$ is a constant vector which can be obtained as a combination of positions and velocities, but with coefficients depending upon time: each of its components is a time-dependent first integral.

The other three one-parameter symmetry groups are groups of rotations ( $\mathbf q = \mathbf 0$ ). A three-dimensional $\mathbf { x }$ rotates by an angle of $s$ radians around an axis $\hat { \mathbf { v } } _ { h }$ ; the rotation is counterclockwise for $s > 0$ , as seen from the tip of vˆh,

$$
F ^ { s } ( { \bf { x } } ) = R _ { s \hat { \bf { v } } _ { h } } \ { \bf { x } } , \quad \left. \frac { \partial F ^ { s } ( { \bf { x } } ) } { \partial s } \right| _ { s = 0 } = \hat { \bf { v } } _ { h } \times { \bf { x } }
$$

and the integral of the Noether theorem

$$
c _ { h } = \sum _ { j = 0 } ^ { N } \left( { \hat { \mathbf { v } } } _ { h } \times \mathbf { r } _ { j } \right) \cdot m _ { j } { \dot { \mathbf { r } } } _ { j } = { \hat { \mathbf { v } } } _ { h } \cdot \sum _ { j = 0 } ^ { N } m _ { j } \left( \mathbf { r } _ { j } \times { \dot { \mathbf { r } } } _ { j } \right)
$$

is the component along $\hat { \mathbf { v } } _ { h }$ of the total angular momentum

$$
\mathbf { c } = \sum _ { j = 0 } ^ { N } m _ { j } ( \mathbf { r } _ { j } \times \dot { \mathbf { r } } _ { j } ) ,
$$

thus the motion preserves the angular momentum vector integral.

There is one additional integral, the total energy integral, which is not deduced from the Noether theorem.2 By computing the total time deriva-

tives

$$
{ \frac { d T } { d t } } = \sum _ { j = 0 } ^ { N } m _ { j } { \ddot { \mathbf { r } } } _ { j } \cdot { \dot { \mathbf { r } } } _ { j } , \quad { \frac { d V } { d t } } = \sum _ { j = 0 } ^ { N } { \frac { \partial V } { \partial \mathbf { r } _ { j } } } \cdot { \dot { \mathbf { r } } } _ { j }
$$

and by eq. (4.1) they are opposite, thus $E = T + V$ is a first integral.

There is one additional symmetry in the $( N + 1 )$ -body problem, which involves not only the coordinates but also the time and possibly the masses: the change of scale. It is also associated with a first integral, which is not independent of the previous ones. If the lengths are changed by a factor $\lambda$ , the times by a factor $\tau$ , the masses by a factor $\mu$ , then

$$
m _ { j } { \ddot { \mathbf { r } } } _ { j } \mapsto { \frac { \mu \lambda } { \tau ^ { 2 } } } m _ { j } { \ddot { \mathbf { r } } } _ { j } , \quad { \frac { \partial V } { \partial \mathbf { r } _ { j } } } \mapsto { \frac { \mu ^ { 2 } } { \lambda ^ { 2 } } } { \frac { \partial V } { \partial \mathbf { r } _ { j } } } ,
$$

and the equation of motion is satisfied by the scaled orbits if and only if

$$
\lambda ^ { 3 } = \mu \tau ^ { 2 } ,
$$

the dimensional version of Kepler’s third law. If $\tau = 1$ it is possible to scale the lengths compensating with a scaling of the masses $\lambda ^ { 3 } = \mu$ ; this may imply the impossibility of determining masses and lengths (see Section 6.2).

When a scaling with $\lambda ^ { 3 } = \mu \tau ^ { 2 }$ is applied, the energy integral is scaled

$$
T \mapsto { \frac { \mu \lambda ^ { 2 } } { \tau ^ { 2 } } } \ T , \quad V \mapsto { \frac { \mu ^ { 2 } } { \lambda } } \ V \Longrightarrow E \mapsto { \frac { \mu \lambda ^ { 2 } } { \tau ^ { 2 } } } \ E
$$

and the angular momentum vector integral scales as $\mathbf { c } \mapsto \mu \lambda ^ { 2 } / \tau \mathbf { c }$ , thus the combination $\textit { E c } ^ { 2 }$ , where $c = | \mathbf { c } |$ , scales as

$$
E \ c ^ { 2 } \mapsto { \frac { \mu \lambda ^ { 2 } } { \tau ^ { 2 } } } \ { \frac { \mu ^ { 2 } \lambda ^ { 4 } } { \tau ^ { 2 } } } E \ c ^ { 2 } = \mu ^ { 5 } \ E \ c ^ { 2 } ;
$$

thus $\textit { E c } ^ { 2 }$ is invariant if $\mu = 1$ , that is, if masses are not scaled.

A deep result obtained by the celestial mechanicians of the late nineteenth century states that for $N \geq 3$ there are no first integrals in the $( N + 1 )$ - body problem independent of the 10 classical ones of the linear and angular momentum and total energy (seven time independent and three time dependent).

# 4.2 Coordinate changes

The first integrals have to be exploited to reduce the dimensionality of the equation of motion, and this is for two reasons. First, the dimensions $3 N + 3$ of the configuration space, and $6 N + 6$ of the phase space (of the initial conditions), are too large to understand the properties of the solutions. Second, the symmetries associated with the integrals may result in degeneracy of the orbit determination problem, as discussed in Chapter 6; one of the possible remedies is to decrease the number of variables. Also for the above purpose, we need to know how the equation of motion transforms under a coordinate change: this is easier for the Lagrange equation.

Let $\mathbf { B } = ( \mathbf { b } _ { 0 } , \mathbf { b } _ { 1 } , \dots , \mathbf { b } _ { n } )$ be another set of coordinates for the positions of the $N + 1$ bodies, and $\mathbf { R } = \mathbf { R } ( \mathbf { B } )$ a coordinate change which is a diffeomorphism (with continuous second derivatives) of the $( 3 N + 3 )$ -dimensional space; we are thus assuming that the Jacobian matrix $A ( \mathbf { B } ) = \partial \mathbf { R } / \partial \mathbf { B }$ is invertible at each point $\mathbf { B }$ . The corresponding change in the velocities is

$$
\dot { \bf R } = \frac { \partial { \bf R } } { \partial { \bf B } } ( { \bf B } ) \dot { \bf B } = A ( { \bf B } ) \dot { \bf B } .
$$

Let ${ \cal L } ( { \bf R } , \dot { \bf R } )$ , $\mathcal { L } ( \mathbf { B } , \dot { \mathbf { B } } )$ be Lagrange functions corresponding by value:

$$
{ \mathcal { L } } ( \mathbf { B } , { \dot { \mathbf { B } } } ) = L \left( \mathbf { R } ( \mathbf { B } ) , { \dot { \mathbf { R } } } ( \mathbf { B } , { \dot { \mathbf { B } } } ) \right) = L \left( \mathbf { R } ( \mathbf { B } ) , A ( \mathbf { B } ) { \dot { \mathbf { B } } } \right) ;
$$

then the left-hand side of the Lagrange equation is transformed as follows:

$$
{ \frac { d } { d t } } \left( { \frac { \partial { \mathcal { L } } } { \partial { \dot { \mathbf { B } } } } } \right) - { \frac { \partial { \mathcal { L } } } { \partial \mathbf { B } } } = \left[ { \frac { d } { d t } } \left( { \frac { \partial L } { \partial { \dot { \mathbf { R } } } } } \right) - { \frac { \partial L } { \partial \mathbf { R } } } \right] A ( \mathbf { B } ) .
$$

The Lagrange equations in the two coordinate systems are equivalent

$$
\frac { d } { d t } \left( \frac { \partial \mathcal { L } } { \partial \dot { \mathbf { B } } } \right) - \frac { \partial \mathcal { L } } { \partial \mathbf { B } } = \mathbf { 0 } \Longleftrightarrow \frac { d } { d t } \left( \frac { \partial L } { \partial \dot { \mathbf { R } } } \right) - \frac { \partial L } { \partial \mathbf { R } } = \mathbf { 0 } ;
$$

solutions of one are transformed by $\mathbf { R } = \mathbf { R } ( \mathbf { B } )$ into solutions of the other.

# Reduction of the two-body problem

We shall start from the simplest case, the two-body problem, to get some ideas to be exploited in the general case. The Lagrange function is

$$
L = { \frac { 1 } { 2 } } m _ { 0 } | { \dot { \mathbf { r } } } _ { 0 } | ^ { 2 } + { \frac { 1 } { 2 } } m _ { 1 } | { \dot { \mathbf { r } } } _ { 1 } | ^ { 2 } + { \frac { G m _ { 0 } m _ { 1 } } { | \mathbf { r } _ { 0 } - \mathbf { r } _ { 1 } | } } .
$$

We can change coordinates by using, in place of $\mathbf { r } _ { 0 } , \mathbf { r } _ { 1 }$ , the coordinates of the center of mass and the relative position of $\mathbf { r } _ { 1 }$ with respect to $\mathbf { r } _ { 0 }$

$$
\mathbf { b } _ { 0 } = \mu _ { 1 } \ \mathbf { r } _ { 1 } + { \big ( } 1 - \mu _ { 1 } { \big ) } \mathbf { r } _ { 0 } , \quad \mu _ { 1 } = { \frac { m _ { 1 } } { m _ { 0 } + m _ { 1 } } } , \quad \mathbf { b } _ { 1 } = \mathbf { r } _ { 1 } - \mathbf { r } _ { 0 } .
$$

Then $V = \mathcal { V } ( b _ { 1 } ) = - G m _ { 0 } m _ { 1 } / b _ { 1 }$ , with $b _ { 1 } = | \mathbf { b } _ { 1 } |$ ; to write $T$ as a function of $\mathbf { b } _ { 0 } , \mathbf { b } _ { 1 }$ we express $\dot { \mathbf { r } } _ { 0 }$ and $\dot { \mathbf { r } } _ { 1 }$ as a function of $\dot { \mathbf { b } } _ { 0 } , \dot { \mathbf { b } } _ { 1 }$ and substitute in $T$ :

$$
2 T = m _ { 0 } { \dot { \mathbf { r } } } _ { 0 } ^ { 2 } + m _ { 1 } { \dot { \mathbf { r } } } _ { 1 } ^ { 2 } = \left( m _ { 0 } + m _ { 1 } \right) { \dot { \mathbf { b } } } _ { 0 } ^ { 2 } + { \frac { m _ { 0 } m _ { 1 } } { m _ { 0 } + m _ { 1 } } } { \dot { \mathbf { b } } } _ { 1 } ^ { 2 }
$$

the mixed terms canceling. The Lagrange function as a function of $\mathbf { b } _ { 0 } , \mathbf { b } _ { 1 }$ is

$$
L = { \frac { 1 } { 2 } } ~ M _ { 0 } ~ { \dot { \bf b } } _ { 0 } ^ { 2 } + { \frac { 1 } { 2 } } ~ M _ { 1 } ~ { \dot { \bf b } } _ { 1 } ^ { 2 } + { \frac { G M _ { 0 } ~ M _ { 1 } } { b _ { 1 } } }
$$

with $M _ { 0 } = m _ { 0 } + m _ { 1 }$ the total mass and $M _ { 1 }$ the reduced mass:

$$
M _ { 1 } = \frac { m _ { 0 } m _ { 1 } } { m _ { 0 } + m _ { 1 } } .
$$

Then the Lagrange function $L$ can be decomposed as the sum of two Lagrange functions $L = M _ { 0 } L _ { 0 } ( \dot { \bf b } _ { 0 } ) + M _ { 1 } L _ { 1 } ( { \bf b } _ { 1 } , \dot { \bf b } _ { 1 } )$ , one containing only $\mathbf { b } _ { 0 }$ , the other containing only $\mathbf { b } _ { 1 }$ , and the Lagrange equation decouples:

$$
M _ { 0 } \ddot { \mathbf { b } } _ { 0 } = 0 , M _ { 1 } \ddot { \mathbf { b } } _ { 1 } = - \frac { \partial \mathcal { V } ( \mathbf { b } _ { 1 } ) } { \partial \mathbf { b } _ { 1 } } .
$$

The first equation states that the center of mass moves with constant velocity along a straight line, the second equation is the Kepler problem, with a particle of mass $M _ { 1 }$ attracted by a fixed center of mass $M _ { 0 }$ .

By repeating the same computations done for $T$ , we find that also the angular momentum has a simple expression in the $\mathbf { B }$ coordinates:

$$
\mathbf { c } = m _ { 0 } \ \mathbf { r } _ { 0 } \times { \dot { \mathbf { r } } } _ { 0 } + m _ { 1 } \ \mathbf { r } _ { 1 } \times { \dot { \mathbf { r } } } _ { 1 } = M _ { 0 } \ \mathbf { b } _ { 0 } \times { \dot { \mathbf { b } } } _ { 0 } + M _ { 1 } \ \mathbf { b } _ { 1 } \times { \dot { \mathbf { b } } } _ { 1 } .
$$

When ${ \bf b } _ { 0 } ( t )$ from eq. (4.5) is substituted, the $\mathbf { b } _ { 0 }$ contribution is constant

$$
\mathbf { c } _ { 0 } = \mathbf { b } _ { 0 } \times { \dot { \mathbf { b } } } _ { 0 } = { \frac { 1 } { M _ { 0 } } } { \mathbf { b } } _ { 0 } ( 0 ) \times \mathbf { p } , \quad \mathbf { c } = M _ { 0 } \ \mathbf { c } _ { 0 } + M _ { 1 } \ \mathbf { c } _ { 1 }
$$

and the contribution from $\mathbf { b } _ { 1 }$ is $\mathbf { c } _ { 1 } = \mathbf { b } _ { 1 } \times \dot { \mathbf { b } } _ { 1 }$ , the angular momentum per unit (reduced) mass of $\mathbf { r } _ { 1 }$ with respect to the center $\mathbf { r } _ { 0 }$ , which is also a vector first integral. Thus $\mathbf { b } _ { 1 } , \dot { \mathbf { b } } _ { 1 }$ will lie for each $t$ in the orbital plane normal to $\mathbf { c } _ { 1 }$ .

# Solution of the two-body problem

The two-body problem has another vector integral, not occurring in the $N \geq 3$ -body problem: the Laplace–Lenz vector

$$
\mathbf { e } = { \frac { 1 } { G M _ { 0 } } } { \dot { \mathbf { b } } } _ { 1 } \times \mathbf { c } _ { 1 } - { \frac { 1 } { b _ { 1 } } } \mathbf { b } _ { 1 } .
$$

This can be shown by using a reference frame formed by three mutually orthogonal unit vectors, $\mathbf { v } _ { z } = \mathbf { c } _ { 1 } / c _ { 1 }$ ( $c _ { 1 } = | \mathbf { c } _ { 1 } |$ ), ${ \mathbf v } _ { r } = { \mathbf b } _ { 1 } / b _ { 1 }$ , and $\mathbf { v } _ { \theta }$ such that $\dot { \mathbf { b } } _ { 1 } \cdot \mathbf { v } _ { \theta } > 0$ . If $\theta$ is the angle between the vector $\mathbf { v } _ { r }$ and a fixed direction in the orbital plane, and $r = b _ { 1 }$ , we have

$$
{ \bf \Omega } _ { 1 } = r { \bf v } _ { r } \times \frac { d } { d t } ( r { \bf v } _ { r } ) = r { \bf v } _ { r } \times ( \dot { r } { \bf v } _ { r } + r \dot { \theta } { \bf v } _ { \theta } ) = r ^ { 2 } \dot { \theta } { \bf v } _ { r } \times { \bf v } _ { \theta } = r ^ { 2 } \dot { \theta } { \bf v } _ { z } ,
$$

$$
G M _ { 0 } { \mathbf e } = - r ^ { 2 } { \dot { r } } { \dot { \theta } } { \mathbf v } _ { \theta } + \left( r ^ { 3 } { \dot { \theta } } ^ { 2 } - G M _ { 0 } \right) { \mathbf v } _ { r } .
$$

Along the solutions we have

$$
\dot { \bf c } _ { 1 } = 0 , ~ 2 \dot { r } \dot { \theta } + r \dot { \theta } ^ { 2 } = 0 , ~ \ddot { r } = - { \frac { G M _ { 0 } } { r ^ { 2 } } } + { \frac { c _ { 1 } ^ { 2 } } { r ^ { 3 } } } ,
$$

so that

$$
G M _ { 0 } { \dot { \mathbf { e } } } = { \ddot { \mathbf { b } } } _ { 1 } \times \mathbf { c } _ { 1 } - G M _ { 0 } { \dot { \theta } } \ \mathbf { v } _ { \theta } = - G M _ { 0 } { \dot { \theta } } \ ( \mathbf { v } _ { r } \times \mathbf { v } _ { z } + \mathbf { v } _ { \theta } ) = \mathbf { 0 } .
$$

Thus $\mathbf { e }$ contains two integrals independent of $\mathbf { c } _ { 1 }$ (not three because $\mathbf { e } { \cdot } \mathbf { c } _ { 1 } = 0$ ). We define the true anomaly $\boldsymbol { v }$ as the angle between $\mathbf { e }$ and $\mathbf { v } _ { r }$ on the orbital plane, that is

$$
e \cos v = \mathbf e \cdot \mathbf v _ { r } = { \frac { r ^ { 3 } \dot { \theta } ^ { 2 } } { G M _ { 0 } } } - 1 = { \frac { c _ { 1 } ^ { 2 } } { G M _ { 0 } r } } - 1
$$

where $r ^ { 2 } { \dot { \theta } } = c _ { 1 }$ is the (scalar) angular momentum of $\mathbf { b } _ { 1 }$ and is constant. From this we find the familiar formula of a conic section

$$
r = { \frac { c _ { 1 } ^ { 2 } / G M _ { 0 } } { 1 + e \cos v } }
$$

and the interpretation of the two additional two-body integrals as eccentricity $e = | \mathbf { e } |$ and argument of pericenter $\omega$ , that is the angle of $\mathbf { e }$ with a fixed direction in the orbital plane, in such a way that $\theta = v + \omega$ . The eccentricity $e$ is an integral depending upon angular momentum and energy. The energy integral of the two-body problem in $\left( \mathbf { b } _ { 0 } , \mathbf { b } _ { 1 } \right)$ coordinates is

$$
E ( { \bf B } , { \dot { \bf B } } ) = M _ { 0 } ~ E _ { 0 } + M _ { 1 } ~ E _ { 1 } , ~ E _ { 0 } = { \frac { 1 } { 2 } } ~ | { \dot { \bf b } } _ { 0 } | ^ { 2 } , ~ E _ { 1 } = { \frac { 1 } { 2 } } ~ | { \dot { \bf b } } _ { 1 } | ^ { 2 } - { \frac { G ~ M _ { 0 } } { | { \bf b } _ { 1 } | } }
$$

and the eccentricity squared, computed from eq. (4.12), is

$$
e ^ { 2 } = \mathbf { e \cdot e } = { \frac { r ^ { 4 } { \dot { \theta } } ^ { 2 } { \dot { r } } ^ { 2 } + \left( r ^ { 3 } { \dot { \theta } } ^ { 2 } - G M _ { 0 } \right) ^ { 2 } } { G ^ { 2 } M _ { 0 } ^ { 2 } } } = 1 + { \frac { 2 E _ { 1 } c _ { 1 } ^ { 2 } } { G ^ { 2 } M _ { 0 } ^ { 2 } } } .
$$

If the energy of the relative motion $E _ { 1 }$ is negative, then $\textit { e } < 1$ and the trajectory of $\mathbf { b } _ { 1 }$ is an ellipse with semimajor axis

$$
a = \frac { q + Q } { 2 } = \frac { 1 } { 2 } \left[ \frac { c _ { 1 } ^ { 2 } / G M _ { 0 } } { 1 + e } + \frac { c _ { 1 } ^ { 2 } / G M _ { 0 } } { 1 - e } \right] = \frac { G M _ { 0 } } { - 2 E _ { 1 } } ,
$$

where $q , Q$ are the pericenter and apocenter distances, and the scalar angular momentum of the relative motion is $c _ { 1 } = \sqrt { G M _ { 0 } a ( 1 - e ^ { 2 } ) }$ . Formulae to express explicitly the solutions of the two-body problem are available in Appendix A.

# 4.3 Barycentric and heliocentric coordinates

The set of positions of the $N + 1$ bodies can be represented in different coordinates; we are interested in the linear coordinate changes of the form

$$
\mathbf { b } _ { j } = \sum _ { i = 0 } ^ { N } a _ { j i } \mathbf { r } _ { i } , A = ( a _ { j i } ) , i , j = 0 , N
$$

where the matrix $A$ is a function of the masses only. The purpose is to exploit the integrals of the center of mass to reduce the number of equations, generalizing the results of the two-body case. A natural choice is to use the center of mass as ${ \bf b } _ { 0 }$ , thus by (4.5) the first row of the matrix $A$ is

$$
a _ { 0 i } = \frac { m _ { i } } { M _ { 0 } } , \quad i = 0 , N .
$$

The choice of the other $\mathbf { b } _ { i } , i = 1 , N$ , is not as simple as in the two-body case. Different choices have different advantages, and can be used for different purposes. We shall review in this and in the next section the most common coordinate systems used for the $( N + 1 )$ -body problem.

# Barycentric coordinates

The barycentric coordinate system uses the fact that a reference system with a constant velocity translation with respect to an inertial system is also inertial. Thus a reference system with $\mathbf b _ { 0 } = \mathbf 0$ as origin and barycentric positions $\mathbf { b } _ { i } = \mathbf { r } _ { i } - \mathbf { b } _ { 0 }$ for $i = 1 , N$ is inertial, and the equation of motion is the same as eq. (4.1). The change to barycentric is not just a change of coordinates, but also a reduction of the dimension of the problem: we write three differential equations less. The barycentric coordinates of body 0 (e.g., the Sun) are not dynamical variables, but are deduced from the coordinates of the other bodies and $\mathbf { b } _ { 0 }$ , by eq. (4.5):

$$
\mathbf { s } = \mathbf { s } ( \mathbf { B } ) = \mathbf { r } _ { 0 } - \mathbf { b } _ { 0 } = - \sum _ { i = 1 } ^ { N } \frac { m _ { i } } { m _ { 0 } } \mathbf { b } _ { i } ,
$$

where the first term is assumed to be zero. The equation of motion is

$$
m _ { j } { \ddot { \bf b } } _ { j } = \sum _ { i \neq j , i = 1 } ^ { N } { \frac { G m _ { i } m _ { j } } { | { \bf b } _ { i } - { \bf b } _ { j } | ^ { 3 } } } ( { \bf b } _ { i } - { \bf b } _ { j } ) + { \frac { G m _ { 0 } m _ { j } } { | { \bf b } _ { j } - { \bf s } | ^ { 3 } } } ( { \bf s } - { \bf b } _ { j } ) \qquad j = 1 , \dots , N - 1 ,
$$

and can be written in conservative form

$$
m _ { j } { \ddot { \mathbf { b } } } _ { j } = - { \frac { \partial { \mathcal { V } } ( \mathbf { s } , \mathbf { b } _ { 1 } , \mathbf { b } _ { 2 } , \ldots , \mathbf { b } _ { n } ) } { \partial \mathbf { b } _ { j } } } , ~ j = 1 , N ,
$$

with the potential energy $\mathscr { V } ( \mathbf { B } ) = V ( \mathbf { R } ( \mathbf { B } ) )$ , where the partial derivatives of $\nu$ have to be computed before substituting $\begin{array} { r } { \mathbf s = \mathbf s ( \mathbf B ) } \end{array}$ . The integrals of energy and angular momentum have a less simple expression, including the contributions from $\dot { \bf s }$ .

Barycentric coordinates are efficient to be used for numerical integrations: only the $3 N$ equations (4.16) have to be integrated, and the only additional computation to be performed at each step is s according to (4.15). The computed orbit does not need to be used in barycentric coordinates: to change the output back to heliocentric coordinates is the normal procedure.

Barycentric coordinates need to be used when the inertial velocities are directly observable: this is the case when the radial velocity of some star is measured (either by radio astronomy, for pulsars, or by spectroscopy, for normal stars). This is used to detect the small velocity of the star as a result of the presence of a small companion, such as a planet, see Section 6.5. The measured radial velocity is the difference between s˙ of the star and $\dot { \bf b } _ { 3 }$ of the Earth; to use heliocentric coordinates for the Earth would result in a serious mistake.3 The barycentric coordinates also play a role in the general relativistic corrections to the Newton equation, see Section 6.6.

On the other hand, barycentric coordinates are seldom used in analytical developments and in theoretical discussions, because of the lack of symmetry of the equation and of the less simple expressions for the classical integrals.

# Heliocentric coordinates

A possible choice to represent the motion of planets and asteroids is the use of heliocentric coordinates. These follow the same idea used in the twobody case, eq. (4.9), namely use the motion of bodies $j = 1 , N$ relative to the one with index 0, usually the Sun. Since $m _ { 0 } \gg m _ { j } , ~ j = 1 , N$ , the Sun moves little, but this motion cannot be neglected in the differential equations. The positions are thus represented by the vectors $\mathbf b _ { i } = \mathbf r _ { i } - \mathbf r _ { 0 }$ and the equation of motion can be simply derived from eq. (4.1), taking into account the non-inertial frame, that is adding the apparent force exactly opposite to the acceleration of the Sun times the mass of the body:

$$
m _ { j } { \ddot { \mathbf { b } } } _ { j } = \sum _ { i \neq j , i = 0 } ^ { N } { \frac { G m _ { i } m _ { j } } { | \mathbf { r } _ { i } - \mathbf { r } _ { j } | ^ { 3 } } } ( \mathbf { r } _ { i } - \mathbf { r } _ { j } ) - m _ { j } { \ddot { \mathbf { r } } } _ { 0 } .
$$

$\boldsymbol { ^ 3 }$ It would lead to a pretended discovery of a companion with a period of one year!

The equation can be written in terms of the heliocentric vectors, since they contain only the differences $\mathbf b _ { i } - \mathbf b _ { j } = \mathbf r _ { i } - \mathbf r _ { j }$ and $\mathbf { b } _ { i } = \mathbf { r } _ { i } - \mathbf { r } _ { 0 }$

$$
m _ { j } { \ddot { \mathbf { b } } } _ { j } = - { \frac { G m _ { 0 } m _ { j } } { | \mathbf { b } _ { j } | ^ { 3 } } } \mathbf { b } _ { j } + \sum _ { i \neq j , i = 1 } ^ { N } { \frac { G m _ { i } m _ { j } } { | \mathbf { b } _ { i } - \mathbf { b } _ { j } | ^ { 3 } } } ( \mathbf { b } _ { i } - \mathbf { b } _ { j } ) - m _ { j } { \ddot { \mathbf { r } } } _ { 0 } .
$$

The value of the acceleration of the Sun, resulting from the gravitational attraction of all the planets, is obtained from eq. (4.1) for $j = 0$ ; by substituting into the equation and removing the common factor $m _ { j }$

$$
{ \ddot { \bf b } } _ { j } = - { \frac { G m _ { 0 } } { | { \bf b } _ { j } | ^ { 3 } } } { \bf b } _ { j } + \sum _ { i \neq j , i = 1 } ^ { N } { \frac { G m _ { i } } { | { \bf b } _ { i } - { \bf b } _ { j } | ^ { 3 } } } ( { \bf b } _ { i } - { \bf b } _ { j } ) - \sum _ { i = 1 } ^ { N } { \frac { G m _ { i } } { | { \bf b } _ { i } | ^ { 3 } } } { \bf b } _ { i } .
$$

The equations above allow us to compute a solution for each heliocentric vector $\mathbf { b } _ { i } , \ i = 1 , n$ , without the need to compute the position of the Sun in an inertial frame. Taking into account that in the acceleration of the Sun there is also a component due to the same planet

$$
\ddot { \mathbf { b } } _ { j } = - \frac { G \left( m _ { 0 } + m _ { j } \right) } { \vert \mathbf { b } _ { j } \vert ^ { 3 } } \mathbf { b } _ { j } + \sum _ { i \neq j , i = 1 } ^ { N } \frac { G m _ { i } } { \vert \mathbf { b } _ { i } - \mathbf { b } _ { j } \vert ^ { 3 } } \left( \mathbf { b } _ { i } - \mathbf { b } _ { j } \right) - \sum _ { i \neq j , i = 1 } ^ { N } \frac { G m _ { i } } { \vert \mathbf { b } _ { i } \vert ^ { 3 } } \mathbf { b } _ { i } .
$$

In this way the equation of motion is split into the two-body part, with the planet orbiting around a fixed center with mass $m _ { 0 } + m _ { j }$ (as in the reduction of a two-body problem with the Sun and the planet $j$ only), the direct perturbations by the attraction of the other planets, and the indirect perturbations, resulting from the other planets accelerating the Sun.

The heliocentric coordinates are a natural choice for Solar System orbits. The relative positions $\mathbf { r } _ { j } - \mathbf { r } _ { k } = \mathbf { b } _ { j } - \mathbf { b } _ { k }$ generate the only quantities observable inside our Solar System, e.g., the direction angles in optical astrometry and the range and range-rate in radar observations. The center of mass $\mathbf { b } _ { 0 }$ and the barycentric position $\mathbf { s }$ of the Sun are derived quantities containing the mass ratios $m _ { j } / m _ { 0 }$ . Thus, a catalog of asteroid orbital elements, computed from Cartesian coordinates in a barycentric system, would contain values dependent upon the planetary masses: every time the masses are corrected, the catalog should be revised. If the orbital elements are computed from heliocentric coordinates, there is no need for revision when the estimated values of the planetary masses change, with the exception of the asteroids having close approaches to a planet whose mass has been revised.

# 4.4 Jacobian coordinates

The Jacobian coordinates are obtained by selecting, among the linear coordinate changes of the form (4.13), the ones with the center of mass as first vector, thus fulfilling eq. (4.14), with the simplest equation of motion. This requires a matrix $A$ , thus a set of Jacobian vectors $\mathbf { b } _ { 0 } , \mathbf { b } _ { 1 } , \mathbf { b } _ { 2 } , \ldots , \mathbf { b } _ { N }$ , and a set of reduced masses $M _ { 0 } , M _ { 1 } , M _ { 2 } , \ldots , M _ { N }$ with the properties

[1] the first vector $\mathbf { b } _ { 0 }$ is the center of mass, $M _ { 0 }$ is the total mass; [2] the Lagrange equation in the $\mathbf { R }$ coordinates is transformed into the Lagrange equation in the Jacobian coordinates of the same form:

$$
m _ { i } { \ddot { \mathbf { r } } } _ { i } = - { \frac { \partial V } { \partial \mathbf { r } _ { i } } } \Longleftrightarrow M _ { i } { \ddot { \mathbf { b } } } _ { i } = - { \frac { \partial { \boldsymbol { \nu } } } { \partial \mathbf { b } _ { i } } }
$$

where $\mathcal { V } ( \mathbf { B } ) = V ( \mathbf { R } )$ is the potential energy in the Jacobian coordinates.

The conditions on $A$ resulting from [1] are given in (4.14), the ones resulting from [2] require that the kinetic energy remains in diagonal form:

$$
2 T = \sum _ { i = 0 } ^ { N } m _ { i } | \dot { \bf r } _ { i } | ^ { 2 } = \sum _ { j = 0 } ^ { N } M _ { j } | \dot { \bf b } _ { j } | ^ { 2 } ;
$$

then the Jacobian momentum is $M _ { j } \dot { \mathbf { b } } _ { j }$ and the equation is in the simple form required by [2]. By substituting eq. (4.13) in the above formula

$$
2 T = \sum _ { i , k = 0 } ^ { N } { \dot { \bf r } } _ { i } \cdot { \dot { \bf r } } _ { k } \sum _ { j = 0 } ^ { N } a _ { j i } M _ { j } a _ { j k } = \sum _ { i , k = 0 } ^ { N } { \dot { \bf r } } _ { i } \cdot { \dot { \bf r } } _ { k } m _ { i } \delta _ { i k }
$$

where $\delta _ { i k } = 1$ for $i = k$ , and $\delta _ { i k } = 0$ for $i \neq k$ . Thus the equations for $A$ are

$$
m _ { i } \delta _ { i k } = \sum _ { j = 0 } ^ { N } a _ { j i } M _ { j } a _ { j k } \qquad i , k = 0 , N .
$$

In matrix form, if $m , M$ are the diagonal matrices with the masses and the reduced masses, respectively, as coefficients

$$
m = \mathrm { d i a g } [ m _ { 0 } , m _ { 1 } , \ldots , m _ { N } ] , { \cal M } = \mathrm { d i a g } [ M _ { 0 } , M _ { 1 } , \ldots , M _ { N } ]
$$

then eq. (4.19) can be written with $A ^ { T }$ , the transposed matrix

$$
m = A ^ { T } M A .
$$

The Jacobian coordinates have another property, which is a consequence of [2]: the total angular momentum (4.6) has also a simple expression

$$
\mathbf { c } = \sum _ { i = 0 } ^ { N } \mathbf { r } _ { i } \times m _ { i } { \dot { \mathbf { r } } } _ { i } = \sum _ { j = 0 } ^ { N } \mathbf { b } _ { j } \times M _ { j } { \dot { \mathbf { b } } } _ { j } ,
$$

i.e., the total angular momentum of the $( N + 1 )$ -body system is the angular momentum of the free motion of the center of mass ${ \bf b } _ { 0 } \times M _ { 0 } \dot { { \bf b } } _ { 0 }$ plus the sum of the angular momentum of the two-body subsystems $\mathbf { b } _ { j } \times M _ { j } \dot { \mathbf { b } } _ { j }$ , $j = 1 , \ldots , N$ .

Equation (4.20) implies $\operatorname* { d e t } ( m ) = \operatorname* { d e t } ( M ) \operatorname* { d e t } ( A ) ^ { 2 }$ , where the determinants of $m , M$ are the product of all masses and the product of all reduced masses, respectively. Thus [1] and [2] allow rescaling of the masses; a change of orientation is also possible. To avoid this, two additional properties have to be added to the definition of Jacobian coordinates:

[3] the product of the masses is equal to the product of the reduced masses

$$
\prod _ { i = 0 } ^ { N } m _ { i } = \prod _ { j = 0 } ^ { N } M _ { j } ;
$$

[4] the linear transformation defined by $A$ preserves orientation: $\operatorname* { d e t } ( A ) > 0$ .

Properties [2], [3], and [4] imply $\operatorname* { d e t } ( A ) = + 1$ .

# Existence and conditional uniqueness of Jacobian coordinates

If the transformation (4.13) fulfills [1], [2], [3], and [4], it defines a system of Jacobian coordinates. Matrices $A$ with all these properties exist but they are not unique for a given $N$ and for the given set of masses $m _ { i }$ . To obtain a unique selection we proceed as follows.

Let $\mathbf { b } _ { 0 } ^ { N } , \ldots , \mathbf { b } _ { N } ^ { N }$ be a set of Jacobian vectors satisfying [1]–[4], with reduced masses $M _ { 0 } ^ { N } , \dots , M _ { N } ^ { N }$ . Let $m _ { N + 1 } , \mathbf { r } _ { N + 1 }$ be the mass and position of an additional body. Then there are unique Jacobian coordinates, satisfying [1]–[4], with $N$ unchanged Jacobian vectors and $N$ unchanged reduced masses

$$
{ \bf b } _ { j } ^ { N + 1 } = { \bf b } _ { j } ^ { N } , \quad M _ { j } ^ { N + 1 } = M _ { j } ^ { N } \qquad j = 1 , N .
$$

The new reduced masses are

$$
M _ { N + 1 } = \frac { m _ { N + 1 } M _ { 0 } ^ { N } } { M _ { 0 } ^ { N + 1 } } , M _ { 0 } ^ { N + 1 } = M _ { 0 } ^ { N } + m _ { N + 1 }
$$

and the new Jacobian vectors are

$$
\mathbf { b } _ { N + 1 } = \mathbf { r } _ { N + 1 } - \mathbf { b } _ { 0 } ^ { N } , \mathbf { b } _ { 0 } ^ { N + 1 } = \frac { 1 } { M _ { 0 } ^ { N + 1 } } \sum _ { j = 0 } ^ { N + 1 } m _ { j } \mathbf { r } _ { j } .
$$

This can be shown by comparing eqs. (4.19) and (4.21) for $N + 1$ and $N + 2$ bodies (Milani and Nobili 1983).

The solutions (4.23) and (4.22) can be described as follows. A Jacobian coordinate system is a way to decompose an $( N + 1 )$ -body system into free motion of the center of mass and $N$ two-body subsystems. To add a new body, the new Jacobian vector is the position of the new body $\mathbf { r } _ { N + 1 }$ relative to the center of mass ${ \bf b } _ { 0 } ^ { N }$ of the previous system, and the new reduced mass is the harmonic mean of the new mass $m _ {  { N } + 1 }$ and of the previous total mass $M _ { 0 } ^ { N }$ . This generalizes the reduction of the two-body problem (4.9), (4.10).

As for uniqueness, the reduction of the two-body problem to the central force problem gives the Jacobian coordinates for $N + 1 = 2$ bodies. However, if the list of bodies was $\{ \mathbf { r } _ { 1 } , \mathbf { r } _ { 0 } \}$ the Jacobian vector would be $\mathbf { b } _ { 1 } = \mathbf { r } _ { 0 } - \mathbf { r } _ { 1 }$ . For $N + 1 = 3$ the standard solution is to first couple $( m _ { 0 } , m _ { 1 } )$ , that is

$$
{ \bf b } _ { 1 } = { \bf r } _ { 1 } - { \bf r } _ { 0 } , M _ { 1 } = \frac { m _ { 0 } m _ { 1 } } { m _ { 0 } + m _ { 1 } }
$$

then use the vector $\mathbf { b } _ { 2 }$ relative to the center of mass of $( m _ { 0 } , m _ { 1 } )$ , that is

$$
{ \bf b } _ { 2 } = { \bf r } _ { 2 } - \frac { m _ { 0 } } { m _ { 0 } + m _ { 1 } } { \bf r } _ { 0 } - \frac { m _ { 1 } } { m _ { 0 } + m _ { 1 } } { \bf r } _ { 1 } , M _ { 2 } = \frac { m _ { 2 } \left( m _ { 0 } + m _ { 1 } \right) } { m _ { 0 } + m _ { 1 } + m _ { 2 } } .
$$

This solution is not unique: it is possible to form first the binary $( m _ { 2 } , m _ { 0 } )$ , that is $\mathbf { b } _ { 1 } = \mathbf { r } _ { 0 } - \mathbf { r } _ { 2 }$ and then join $\mathbf { r } _ { 1 }$ to the center of mass of $( m _ { 2 } , m _ { 0 } )$ . A third solution corresponds to the sequence of couplings $( ( m _ { 1 } , m _ { 2 } ) , m _ { 0 } )$ ; there are three more solutions violating [4].

The choice of a solution depends upon the sequence of coupling operations, which can be represented by a symbol like $( ( m _ { 0 } , m _ { 1 } ) , m _ { 2 } )$ for the standard three-body solution. At a purely formal level, each of the $( N + 1 )$ ! ways to order the $N + 1$ bodies results, by applying recursively the procedure above, in a set of Jacobian coordinates. When the relative size of the perturbation is computed, as in the next section, the solutions are found to be by no means equivalent. As an example, if $m _ { 0 }$ corresponds to the Sun, $m _ { 1 }$ to the Earth, $m _ { 2 }$ to the Moon, the best Jacobian system is the one with $( ( m _ { 1 } , m _ { 2 } ) , m _ { 0 } )$ , that is the center of mass of the Earth–Moon system is orbiting around the Sun, while the Moon is orbiting around the Earth–Moon center of mass.

![](images/21f5a7a6a4a6314c2063d281a2dbc753c795f162616f2f3c057b22505be2f910.jpg)  
Fig. 4.1. Three examples of hierarchies and of the corresponding Jacobian vectors. The planetary hierarchy and the double binary hierarchy are described in the text. The hierarchy in the lower part of the figure could be used to describe a planetary system around the star $\mathbf { r } _ { 0 }$ , with planets $\mathbf { r } _ { 2 } , \mathbf { r } _ { 3 } , \mathbf { r } _ { 5 }$ and $\mathbf { r } _ { 6 }$ ; planet $\mathbf { r } _ { 3 }$ has one satellite, planet $\mathbf { r } _ { 6 }$ has two satellites.

# Planetary and binary type hierarchies

The non-uniqueness of the Jacobian coordinates becomes more significant for $N + 1 = 4$ bodies. Let us assume some Jacobian coordinates have been selected for the first three bodies, e.g., according to the coupling order $( ( m _ { 0 } , m _ { 1 } ) , m _ { 2 } )$ . When a body $m _ { 4 } , { \bf r } _ { 4 }$ is added, there are two options. One is the recursive procedure of the previous subsection, that is $\mathbf { b } _ { 3 } = \mathbf { r } _ { 3 } - \mathbf { b } _ { 0 } ^ { 3 }$ . The other is to set $\mathbf { b } _ { 2 } = \mathbf { r } _ { 3 } - \mathbf { r } _ { 2 }$ and to replace $\mathbf { r } _ { 2 }$ with the center of mass of the binary $( m _ { 2 } , m _ { 3 } )$ , that is to use as ${ \bf b } _ { 3 }$ the vector joining the two centers of mass of the binary subsystems $( m _ { 0 } , m _ { 1 } )$ and $( m _ { 2 } , m _ { 3 } )$

$$
\mathbf { \dot { \mu } } _ { 1 } - \mathbf { r } _ { 0 } , \ \mathbf { b } _ { 2 } = \mathbf { r } _ { 3 } - \mathbf { r } _ { 2 } , \ \mathbf { b } _ { 3 } = \left[ \left( 1 - \mu _ { 2 } \right) \mathbf { r } _ { 2 } + \mu _ { 2 } \ \mathbf { r } _ { 3 } \right] - \left[ \left( 1 - \mu _ { 1 } \right) \mathbf { r } _ { 0 } + \mu _ { 1 } \ \mathbf { r } _ { 1 } \right]
$$

where $\mu _ { 2 } = m _ { 3 } / ( m _ { 2 } + m _ { 3 } )$ . Then the reduced mass $M _ { 2 }$ is the harmonic mean of the masses $m _ { 2 }$ and $m _ { 3 }$ , $M _ { 3 }$ is the harmonic mean of the masses $( m _ { 0 } + m _ { 1 } )$ and $( m _ { 2 } + m _ { 3 } )$ :

$$
M _ { 1 } = \frac { m _ { 0 } m _ { 1 } } { m _ { 0 } + m _ { 1 } } , M _ { 2 } = \frac { m _ { 2 } m _ { 3 } } { m _ { 2 } + m _ { 3 } } , M _ { 3 } = \frac { \left( m _ { 0 } + m _ { 1 } \right) \left( m _ { 2 } + m _ { 3 } \right) } { m _ { 0 } + m _ { 1 } + m _ { 2 } + m _ { 3 } } .
$$

The first option is called a planetary hierarchy and is represented by the coupling symbol $( ( m _ { 0 } , m _ { 1 } ) , m _ { 2 } ) , m _ { 3 } )$ ; the second is a double binary hierarchy and is represented by $( ( m _ { 0 } , m _ { 1 } ) , ( m _ { 2 } , m _ { 3 } ) )$ . Formally, both choices are equivalent, in that both provide a Jacobian coordinate system satisfying [1], [2], [3], and [4]. The planetary hierarchy suggests that all the “planets” of masses $m _ { 1 } , m _ { 2 } , m _ { 3 }$ orbit around the “star” of much larger mass $m _ { 0 }$ , at increasing distances $| \mathbf { r } _ { 1 } - \mathbf { r } _ { 0 } |$ , $| \mathbf { r } _ { 2 } - \mathbf { r } _ { 0 } |$ , and $| \mathbf { r } _ { 3 } - \mathbf { r } _ { 0 } |$ . The double binary hierarchy suggests that the “interior planet” $m _ { 1 }$ orbits around the “star” $m _ { 0 }$ at a smaller distance than the “exterior planet” $m _ { 2 }$ , the latter having a “satellite” $m _ { 3 }$ . To give rigorous meaning to this suggestion, we need to show that dynamical configurations, with different mass and distance ratios, are better represented in either one or the other hierarchy.

In general, given two subsystems with $N ^ { \prime }$ and $N ^ { \prime \prime }$ bodies, each with Jacobian coordinates, centers of mass ${ \bf { b } } _ { 0 } ^ { \prime }$ , ${ \bf { b } } _ { 0 } ^ { \prime \prime }$ and total masses $M _ { 0 } ^ { \prime }$ , $M _ { 0 } ^ { \prime \prime }$ , respectively, there is a Jacobian system for the joint system of $N ^ { \prime } { + } N ^ { \prime \prime }$ masses with a new Jacobian vector joining the two centers of mass, and a new reduced mass equal to the harmonic mean of the two total masses

$$
{ \bf b } _ { N ^ { \prime } + N ^ { \prime \prime } } = { \bf b } _ { 0 } ^ { \prime \prime } - { \bf b } _ { 0 } ^ { \prime } , ~ M _ { N ^ { \prime } + N ^ { \prime \prime } } = \frac { M _ { 0 } ^ { \prime } ~ M _ { 0 } ^ { \prime \prime } } { M _ { 0 } ^ { \prime } + M _ { 0 } ^ { \prime \prime } } ;
$$

${ \bf b } _ { 0 }$ is the center of mass of all bodies, and the other $( N ^ { \prime } - 1 ) + ( N ^ { \prime \prime } - 1 )$ vectors coincide with the previously defined ones. This is the only way to combine the two subsystems, preserving $N ^ { \prime } + N ^ { \prime \prime } - 2$ Jacobian vectors (not including the centers of mass of the subsystems). In this way we can build a Jacobian system for an arbitrary coupling symbol. For example, for the hierarchy shown in the lower portion of Figure 4.1 the coupling symbol is ( $( ( ( m _ { 0 } , m _ { 1 } ) , m _ { 2 } ) , ( m _ { 3 } , m _ { 4 } ) ) , m _ { 5 } ) , ( m _ { 6 } , m _ { 7 } ) )$ .

# 4.5 Small parameter perturbation

We would like to assess how relevant are the perturbations resulting from each additional body included in the dynamical model of a planetary system. The Jacobian coordinates provide a direct way to estimate the relative size of the perturbations, with the Roy–Walker parameters.

# The perturbing function

We shall discuss first a three-body case, in Jacobian coordinates, with standard hierarchy $( ( m _ { 0 } , m _ { 1 } ) , m _ { 2 } )$ . The Lagrange function is

$$
\mathcal { L } ( \mathbf { B } , \dot { \mathbf { B } } ) = \sum _ { i = 1 } ^ { 3 } \frac { 1 } { 2 } ~ M _ { i } | \dot { \mathbf { b } } _ { i } | ^ { 2 } + \frac { G m _ { 0 } m _ { 1 } } { | \mathbf { b } _ { 1 } | } + \frac { G m _ { 1 } m _ { 2 } } { | \mathbf { r } _ { 2 } - \mathbf { r } _ { 1 } | } + \frac { G m _ { 0 } m _ { 2 } } { | \mathbf { r } _ { 2 } - \mathbf { r } _ { 0 } | } ,
$$

with

$$
\mathbf { r } _ { 2 } - \mathbf { r } _ { 1 } = \mathbf { b } _ { 2 } - { \frac { m _ { 0 } } { m _ { 0 } + m _ { 1 } } } \mathbf { b } _ { 1 } , \quad \mathbf { r } _ { 2 } - \mathbf { r } _ { 0 } = \mathbf { b } _ { 2 } + { \frac { m _ { 1 } } { m _ { 0 } + m _ { 1 } } } \mathbf { b } _ { 1 } .
$$

Our goal is to express the Lagrange function as a sum of three “unperturbed” Lagrange functions and a perturbing function. Since the kinetic energy, in Jacobian coordinates, is already decomposed as needed, only the potential needs to be transformed. We use the sum of masses

$$
N _ { j } = \sum _ { i = 0 } ^ { j } m _ { i } , N _ { 1 } M _ { 1 } = m _ { 0 } m _ { 1 } , N _ { 2 } M _ { 2 } = M _ { 0 } M _ { 2 } = m _ { 2 } \left( m _ { 0 } + m _ { 2 } \right) .
$$

to form the three unperturbed Lagrange functions

$$
L _ { 0 } ( { \bf b } _ { 0 } , \dot { \bf b } _ { 0 } ) = \frac { 1 } { 2 } | \dot { \bf b } _ { 0 } | ^ { 2 } , L _ { i } ( { \bf b } _ { i } , \dot { \bf b } _ { i } ) = \frac { 1 } { 2 } | \dot { \bf b } _ { i } | ^ { 2 } + \frac { G N _ { i } } { | { \bf b } _ { i } | } , i = 1 , 2
$$

corresponding to the free motion of the center of mass and to the two-body motion of $\mathbf { b } _ { i }$ around an attracting center of mass $N _ { i }$ , for $i = 1 , 2$ . The perturbing function is simply what is left:

$$
\begin{array} { r l r } & { } & { \dot { \bf B } ) = M _ { 0 } ~ L _ { 0 } ( { \bf b } _ { 0 } , \dot { \bf b } _ { 0 } ) + M _ { 1 } ~ L _ { 1 } ( { \bf b } _ { 1 } , \dot { \bf b } _ { 1 } ) + M _ { 2 } ~ L _ { 2 } ( { \bf b } _ { 2 } , \dot { \bf b } _ { 2 } ) + R _ { 1 2 } ( { \bf b } _ { 1 } , { \bf b } _ { 2 } ) , } \\ & { } & \\ & { } & { R _ { 1 2 } ( { \bf b } _ { 1 } , { \bf b } _ { 2 } ) = m _ { 2 } G ~ N _ { 1 } ~ \left\{ \frac { \mu _ { 1 } } { \left| { \bf r } _ { 2 } - { \bf r } _ { 1 } \right| } + \frac { 1 - \mu _ { 1 } } { \left| { \bf r } _ { 2 } - { \bf r } _ { 0 } \right| } - \frac { 1 } { \left| { \bf b } _ { 2 } \right| } \right\} ~ ( 4 . 2 4 ) } \end{array}
$$

where $\mu _ { 1 } = m _ { 1 } / ( m _ { 0 } + m _ { 1 } )$ is the mass ratio of the $\mathbf { b } _ { 1 }$ binary. $R _ { 1 2 }$ has three terms, corresponding to the potential (the opposite of the gravitational potential energy) at the position $\mathbf { r } _ { 2 }$ of the mass $m _ { 0 }$ , of the mass $m _ { 1 }$ , and to the opposite of the potential of a mass $m _ { 0 } + m _ { 1 }$ placed in the center of mass of $( m _ { 0 } , m _ { 1 } )$ . This is because the hypothetical potential of a mass $m _ { 0 } + m _ { 1 }$ in the center of mass of the first binary has been used to form the unperturbed Lagrange function of the binary $( m _ { 0 } + m _ { 1 } , m _ { 2 } )$ . Thus the perturbing function is the gravitational potential of a mass distribution consisting of three masses, one of which is negative, with total mass zero.

# Expansions in spherical harmonics

We expand the perturbing function $R _ { 1 2 }$ in spherical harmonics. Three masses $m _ { 0 }$ , $m _ { 1 }$ , and $- ( m _ { 0 } + m _ { 1 } )$ , located at $\mathbf { r } _ { 0 }$ , $\mathbf { r } _ { 1 }$ and at the center of mass $\mathbf { b } _ { 0 } ^ { \mathrm { { l } } } = \mu _ { 1 } \mathbf { r } _ { 1 } + \left( 1 - \mu _ { 1 } \right) \mathbf { r } _ { 0 }$ form the mass distribution generating the perturbing function: since these three masses are aligned, the potential is axially symmetric and can be expressed by zonal spherical harmonics only (see Section 13.2). We are only interested in the first few terms in the harmonics expansion, and shall compute the harmonic coefficients directly.

Let the angle between ${ \bf b } _ { 1 }$ and $\mathbf { b } _ { 2 }$ be $\psi$ , and $\theta = \pi / 2 - \psi$ the latitude (with respect to an equatorial plane through ${ \bf b } _ { 0 } ^ { 1 }$ and perpendicular to the $\mathbf { b } _ { 1 }$ axis). We shall now compute the three distances appearing in the denominators in $\mathcal { R } _ { 1 2 } ( \mathbf { b } _ { 1 } , \mathbf { b } _ { 2 } )$ as functions of the lengths $b _ { 1 } = | \mathbf { b } _ { 1 } |$ and $b _ { 2 } = |  { \mathbf { b } } _ { 2 } |$ and of the angle $\theta$ . The distance between $m _ { 2 }$ and of $m _ { 1 }$ is

$$
\mathbf { r } _ { 2 } - \mathbf { r } _ { 1 } | ^ { 2 } = | \mathbf { b } _ { 2 } - ( 1 - \mu _ { 1 } ) \mathbf { b } _ { 1 } | ^ { 2 } = b _ { 2 } ^ { 2 } + ( 1 - \mu _ { 1 } ) ^ { 2 } b _ { 1 } ^ { 2 } - 2 ( 1 - \mu _ { 1 } ) b _ { 1 } b _ { 2 } { \mathrm { ~ s i n } }
$$

Then we shall express the power $^ { - 1 }$ of the distance by means of the unperturbed distance $b _ { 2 }$ and the ratio $\alpha _ { 1 } = b _ { 1 } / b _ { 2 }$ , with $\alpha _ { 1 } < 1$ (if not, the hierarchy should be changed):

$$
\frac { 1 } { \left| { \bf r } _ { 2 } - { \bf r } _ { 1 } \right| } = \frac { 1 } { b _ { 2 } } \left\{ 1 - 2 ( 1 - \mu _ { 1 } ) \alpha _ { 1 } \sin \theta + ( 1 - \mu _ { 1 } ) ^ { 2 } \alpha _ { 1 } ^ { 2 } \right\} ^ { - 1 / 2 }
$$

and by using the Taylor formula $( 1 + x ) ^ { - 1 / 2 } = 1 - 1 / 2 x + 3 / 8 x ^ { 2 } + O ( x ^ { 3 } )$ we obtain the expansion, with respect to the small parameter $\alpha _ { 1 }$ ,

$$
{ \frac { 1 } { - \left. \mathbf { r } _ { 1 } \right| } } = { \frac { 1 } { b _ { 2 } } } \ \left\{ 1 + ( 1 - \mu _ { 1 } ) \alpha _ { 1 } P _ { 1 } ( \sin \theta ) + ( 1 - \mu _ { 1 } ) ^ { 2 } \alpha _ { 1 } ^ { 2 } P _ { 2 } ( \sin \theta ) + O ( \alpha _ { 1 } ^ { 3 } ) \right.
$$

where we have used the first and the second Legendre polynomials (for a discussion of the Legendre functions, see Section 13.2)

$$
P _ { 1 } ( \sin \theta ) = \sin \theta , ~ P _ { 2 } ( \sin \theta ) = \frac { 3 } { 2 } ~ \sin ^ { 2 } \theta - \frac { 1 } { 2 } .
$$

The formula for the distance between the position of $m _ { 2 }$ and of $m _ { 0 }$ is

$$
| { \bf r } _ { 2 } - { \bf r } _ { 0 } | ^ { 2 } = | { \bf b } _ { 2 } + \mu _ { 1 } { \bf b } _ { 1 } | ^ { 2 } = b _ { 2 } ^ { 2 } + \mu _ { 1 } ^ { 2 } b _ { 1 } ^ { 2 } + 2 \mu _ { 1 } b _ { 1 } b _ { 2 } \sin \theta ,
$$

so that

$$
{ \frac { 1 } { | \mathbf { r } _ { 2 } - \mathbf { r } _ { 0 } | } } = { \frac { 1 } { b _ { 2 } } } \ \left\{ 1 - \mu _ { 1 } \alpha _ { 1 } P _ { 1 } ( \sin \theta ) + \mu _ { 1 } ^ { 2 } \alpha _ { 1 } ^ { 2 } P _ { 2 } ( \sin \theta ) + O ( \alpha _ { 1 } ^ { 3 } ) \right\} .
$$

The perturbing function $R _ { 1 2 }$ is a linear combination of the previous expressions minus $1 / b _ { 2 }$ , in which both the monopole term $1 / b _ { 2 }$ and the dipole term containing $P _ { 1 }$ cancel out, as it has to be expected when the expansion in spherical harmonics is centered at the center of mass

$$
{ \frac { 1 } { m _ { 2 } } } R _ { 1 2 } ( { \bf b } _ { 1 } , { \bf b } _ { 2 } ) = { \frac { G N _ { 1 } } { b _ { 2 } } } \mu _ { 1 } ( 1 - \mu _ { 1 } ) \left[ \alpha _ { 1 } ^ { 2 } P _ { 2 } ( \sin \theta ) + O ( \alpha _ { 1 } ^ { 3 } ) \right]
$$

where the remainder has been indicated taking into account that the $O ( \alpha _ { 1 } ^ { 3 } )$ term also contains the coefficient $\mu _ { 1 } \left( 1 - \mu _ { 1 } \right)$ ; this can be checked by computing of the degree 3 zonal harmonics.

# Perturbations in Jacobian coordinates

The effect of the perturbing function on each of the binaries can be measured as a change in the related two-body energy. The integral of energy

$$
E ( \mathbf { B } , { \dot { \mathbf { B } } } ) = M _ { 0 } \ E _ { 0 } + M _ { 1 } \ E _ { 1 } + M _ { 2 } \ E _ { 2 } - R _ { 1 2 }
$$

contains a linear combination of the two-body energies (per unit mass) of the subsystems

$$
E _ { 0 } = { \frac { 1 } { 2 } } | { \dot { \mathbf { b } } } _ { 0 } | ^ { 2 } , E _ { i } = T _ { i } + V _ { i } = { \frac { 1 } { 2 } } | { \dot { \mathbf { b } } } _ { i } | ^ { 2 } - { \frac { G N _ { i } } { | \mathbf { b } _ { i } | } } , i = 1 , 2 .
$$

The perturbing potential $R _ { 1 2 }$ has the relative effect $R _ { 1 2 } / ( M _ { 2 } E _ { 2 } )$ on the $\mathbf { b } _ { 2 }$ subsystem: this ratio can be approximated, for order of magnitude computations, assuming $V _ { 2 } = - G N _ { 2 } / b _ { 2 } \simeq 2 \ E _ { 2 }$ , which is exact for a circular orbit

$$
{ \frac { R _ { 1 2 } } { M _ { 2 } ~ E _ { 2 } } } \simeq { \frac { 2 R _ { 1 2 } } { M _ { 2 } ~ V _ { 2 } } } = - 2 \mu _ { 1 } \left( 1 - \mu _ { 1 } \right) ~ \left[ \alpha _ { 1 } ^ { 2 } ~ P _ { 2 } ( \sin \theta ) + { \cal O } ( \alpha _ { 1 } ^ { 3 } ) \right]
$$

and for $\alpha _ { 1 } \ll 1$ this leads to the approximate upper bound

$$
\left| \frac { R _ { 1 2 } } { M _ { 2 } E _ { 2 } } \right| \le 2 \epsilon _ { 1 2 } , ~ \epsilon _ { 1 2 } = \mu _ { 1 } \left( 1 - \mu _ { 1 } \right) \alpha _ { 1 } ^ { 2 } .
$$

The same argument applied to the $\mathbf { b } _ { 1 }$ subsystem is $V _ { 1 } = - G \ : N _ { 1 } / b _ { 1 } \simeq 2 \ : E _ { 1 }$ and gives

$$
\left| \frac { R _ { 1 2 } } { M _ { 1 } E _ { 1 } } \right| \le 2 \ : \frac { M _ { 2 } \ : N _ { 2 } \ : \mu _ { 1 } \left( 1 - \mu _ { 1 } \right) } { M _ { 1 } \ : N _ { 1 } } \ : \alpha _ { 1 } ^ { 3 } = 2 \ : \epsilon _ { 2 1 } , \epsilon _ { 2 1 } = \frac { \mu _ { 2 } } { 1 - \mu _ { 2 } } \ : \alpha _ { 1 } ^ { 3 } .
$$

Thus the size of the perturbing function, relative to the size of the unperturbed potential energy, is estimated by the Roy–Walker parameters $\epsilon _ { 1 2 }$ , $\epsilon _ { 2 1 }$ . Note they both contain mass ratios and the ratio $\alpha _ { 1 }$ of the Jacobian vector lengths: the exterior perturbation decreases like the cube of $\alpha _ { 1 }$ , the interior one like the square. The effect of such a perturbation on the semimajor axes $a _ { j }$ of the two orbits of ${ \bf b } _ { j }$ , $j = 1 , 2$ , assuming $\epsilon _ { i j }$ small, could be estimated by the simple rule $\Delta a _ { j } / a _ { j } = - \Delta E _ { j } / E _ { j }$ .

# The four-body case

A hierarchy can be understood just as a combinatorial structure, represented by either a symbol like $( ( m _ { 0 } , m _ { 1 } ) , ( m _ { 2 } , m _ { 3 } ) )$ or a graph like the one of Figure 4.1, top right. Not all graphs are suitable to represent a hierarchy: each vector ${ \bf b } _ { j }$ must have one and only one “superior” vector $\mathbf { b } _ { s ( j ) }$ , with the exception of the “top” vector with no superior: in the example above of the double binary hierarchy the vector ${ \bf b } _ { 3 }$ is at the top and is the superior for both $\mathbf { b } _ { 2 }$ and $\mathbf { b } _ { 1 }$ . Then for each Jacobian vector (not at the top) ${ \bf b } _ { j }$ we can define a length ratio $\alpha _ { j } = b _ { j } / b _ { s ( j ) }$ . A hierarchy becomes more than a combinatorial device if the superior vectors are also longer, that is, if the length ratios $\alpha _ { j }$ are small. Then we can estimate the relative size of the perturbing functions, describing the interaction of each two binaries, by using powers of the $\alpha _ { j }$ and mass ratios to form generalized Roy–Walker parameters.

For a double binary hierarchy, the potential energy is the sum of three two-body terms and a perturbing function with three terms

$$
\mathrm { ~  ~ \gamma ~ } = - \sum _ { 0 \le i < j \le 4 } \frac { G m _ { i } m _ { j } } { | { \bf r } _ { i } - { \bf r } _ { j } | } = M _ { 1 } V _ { 1 } + M _ { 2 } V _ { 2 } + M _ { 3 } V _ { 3 } - R _ { 1 3 } - R _ { 2 3 } - R _ { 1 2 }
$$

where the perturbing terms are (Milani and Nobili 1983)

$$
{ \begin{array} { r l r } { { 3 } } & { = } & { N _ { 2 } \ \mathcal { R } _ { 1 } ( \mathbf { b } _ { 2 3 } ) , \ \mathcal { R } _ { 1 } ( \mathbf { x } ) = G N _ { 1 } \left[ { \frac { \mu _ { 1 } } { | \mathbf { x } - \mathbf { r } _ { 1 } | } } + { \frac { 1 - \mu _ { 1 } } { | \mathbf { x } - \mathbf { r } _ { 0 } | } } - { \frac { 1 } { | \mathbf { x } - \mathbf { b } _ { 0 1 } | } } \right] } \\ & { } & \\ { { 3 } } & { = } & { N _ { 1 } \ \mathcal { R } _ { 2 } ( \mathbf { b } _ { 0 1 } ) , \ \mathcal { R } _ { 2 } ( \mathbf { x } ) = G N _ { 2 } \left[ { \frac { \mu _ { 2 } } { | \mathbf { x } - \mathbf { r } _ { 3 } | } } + { \frac { 1 - \mu _ { 3 } } { | \mathbf { x } - \mathbf { r } _ { 2 } | } } - { \frac { 1 } { | \mathbf { x } - \mathbf { b } _ { 2 3 } | } } \right] } \end{array} }
$$

for the perturbations between each of the two binaries with state vector $\mathbf { b } _ { 1 } , \mathbf { b } _ { 2 }$ and the “handle” with state vector ${ \bf b } _ { 3 }$ , and

$$
\begin{array} { r l r } { R _ { 1 2 } } & { = } & { N _ { 1 } \left\{ \mu _ { 1 } \mathcal { R } _ { 2 } ( \mathbf { r } _ { 1 } ) + \left( 1 - \mu _ { 1 } \right) \mathcal { R } _ { 2 } ( \mathbf { r } _ { 0 } ) - \mathcal { R } _ { 2 } ( \mathbf { b } _ { 0 1 } ) \right\} } \\ & { = } & { N _ { 2 } \left\{ \mu _ { 2 } \mathcal { R } _ { 1 } ( \mathbf { r } _ { 3 } ) + \left( 1 - \mu _ { 2 } \right) \mathcal { R } _ { 1 } ( \mathbf { r } _ { 2 } ) - \mathcal { R } _ { 1 } ( \mathbf { b } _ { 2 3 } ) \right\} } \end{array}
$$

for the perturbations between binaries, with ${ \bf b } _ { i k } = ( m _ { i } { \bf b } _ { i } + m _ { k } { \bf b } _ { k } ) / ( m _ { i } +$ $m _ { k }$ ) the centers of mass of the binaries for $( i , k ) = ( 0 , 1 )$ , $( 2 , 3 )$ . By using essentially the same formalism as in the three-body case, it is possible to estimate the ratio of the perturbing functions to the two-body potential energies: e.g., for the perturbations between ${ \bf b } _ { 3 }$ and $\mathbf { b } _ { 1 }$

$$
\begin{array} { r c l } { { \displaystyle \left| \frac { R _ { 1 3 } } { M _ { 1 } V _ { 1 } } \right| } } & { { = } } & { { \displaystyle \frac { G M _ { 1 } N _ { 1 } } { b _ { 1 } } ~ \left[ \mu _ { 1 } ( 1 - \mu _ { 1 } ) \alpha _ { 1 } ^ { 2 } ~ P _ { 2 } ( \sin \theta ) + O ( \alpha _ { 1 } ^ { 3 } ) \right] ~ \frac { b _ { 1 } } { G N _ { 1 } N _ { 2 } } } } \\ { { } } & { { = } } & { { \displaystyle \frac { N _ { 2 } \mu _ { 1 } ( 1 - \mu _ { 1 } ) } { N _ { 1 } } ~ \alpha _ { 1 } ^ { 3 } + O ( \alpha _ { 1 } ^ { 4 } ) = \epsilon _ { 3 1 } + O ( \alpha _ { 1 } ^ { 4 } ) , } } \\ { { \displaystyle \left| \frac { R _ { 3 1 } } { M _ { 3 } V _ { 3 } } \right| } } & { { = } } & { { \displaystyle \frac { G N _ { 1 } N _ { 2 } } { b _ { 3 } } ~ \left[ \mu _ { 1 } ( 1 - \mu _ { 1 } ) \alpha _ { 1 } ^ { 2 } ~ P _ { 2 } ( \sin \theta ) + O ( \alpha _ { 1 } ^ { 3 } ) \right] ~ \frac { b _ { 3 } } { G M _ { 3 } N _ { 3 } } } } \\ { { } } & { { = } } & { { \mu _ { 1 } \left( 1 - \mu _ { 1 } \right) \alpha _ { 1 } ^ { 2 } + O ( \alpha _ { 1 } ^ { 3 } ) = \epsilon _ { 1 3 } + O ( \alpha _ { 1 } ^ { 3 } ) } } \end{array}
$$

and the Roy–Walker parameters have the same expression as in the threebody case; the same occurs for $\epsilon _ { \mathrm { 3 2 } } , \epsilon _ { \mathrm { 2 3 } }$ .

The case of $\epsilon _ { \mathrm { 1 2 } }$ estimating the perturbations of the binary $\mathbf { b } _ { 1 }$ onto $\mathbf { b } _ { 2 }$ is more complicated. It can be shown (Milani and Nobili 1983) that the lowest order term in the expansion (in powers of $\alpha _ { 1 }$ , $\alpha _ { 2 }$ ) of the perturbing function $R _ { 1 2 }$ contains $\mu _ { 1 } \left( 1 - \mu _ { 1 } \right) \mu _ { 2 } \left( 1 - \mu _ { 2 } \right) \alpha _ { 1 } ^ { 2 } \alpha _ { 2 } ^ { 2 }$ . That is, $\epsilon _ { \mathrm { 1 2 } }$ is of the same order in the small parameters as the product $\epsilon _ { 1 3 } \ \epsilon _ { 2 3 }$ . Thus the mutual perturbation of the two binaries in a double binary hierarchy is negligible in many practical cases, such as the perturbations of the satellites of Jupiter on the orbits of the inner planets.

# Perturbations in heliocentric coordinates

To estimate the size of the perturbations to the two-body orbital elements in heliocentric coordinates we need to take into account separately the indirect perturbations resulting from the non-inertial origin in the Sun.

Let us consider the simplest case $N = 2$ and use the analogs of eq. (4.26) for the two-body energies of $\mathbf b _ { j } = \mathbf r _ { j } - \mathbf r _ { 0 }$ orbiting around the Sun

$$
E _ { j } = \frac { 1 } { 2 } | \dot { \mathbf { b } } _ { j } | ^ { 2 } - \frac { G \left( m _ { 0 } + m _ { j } \right) } { | \mathbf { b } _ { j } | } = - \frac { G \left( m _ { 0 } + m _ { j } \right) } { 2 a _ { j } } ,
$$

with $a _ { j }$ the semimajor axis of the osculating heliocentric orbit. In the equation of motion (4.17) $( j = 1 , 2 )$ the first term is two-body like, not affecting $E _ { j }$ ; the time derivative of the two-body energies is the power of the perturbing forces

$$
= \dot { E } _ { j } ^ { d i r } + \dot { E } _ { j } ^ { i n d } , \dot { E } _ { j } ^ { d i r } = G m _ { i } \frac { { \bf b } _ { i } - { \bf b } _ { j } } { | { \bf b } _ { i } - { \bf b } _ { j } | ^ { 3 } } \mathrm {  ~ \cdot ~ } \dot { \bf b } _ { j } , \dot { E } _ { j } ^ { i n d } = - G m _ { i } \frac { { \bf b } _ { i } } { | { \bf b } _ { i } | ^ { 3 } } \mathrm {  ~ \cdot ~ } \dot { \bf b }
$$

The indirect part can be estimated with a circular orbit approximation

$$
| { \bf b } _ { j } | \simeq a _ { j } , | \dot { \bf b } _ { j } | = n _ { j } a _ { j } , n _ { j } = \sqrt { G m _ { 0 } m _ { j } / a _ { j } ^ { 3 } }
$$

taking also into account that the main terms of this perturbation have the frequency $n _ { j } - n _ { i }$ , resulting in an approximate amplitude of oscillation in $E _ { j }$ with this frequency, due to the indirect part only

$$
| \Delta ^ { i n d } E _ { j } | \lesssim \frac { 1 } { | n _ { j } - n _ { i } | } \frac { G m _ { i } a _ { j } n _ { j } } { a _ { i } ^ { 2 } } .
$$

The oscillation amplitude of the heliocentric semimajor axis is estimated by

$$
\frac { | \Delta ^ { i n d } a _ { j } | } { a _ { j } } \simeq \frac { | \Delta ^ { i n d } E _ { j } | } { E _ { j } } = 2 \frac { m _ { i } } { ( m _ { 0 } + m _ { j } ) } \frac { n _ { j } } { | n _ { j } - n _ { i } | } \frac { a _ { j } ^ { 2 } } { a _ { i } ^ { 2 } } .
$$

For the indirect perturbation by an exterior planet $j = 1 , i = 2$ , $n _ { 1 } \gg n _ { 2 }$

and, assuming $m _ { 0 } \gg m _ { 1 } , m _ { 2 }$ ,

$$
\frac { | \Delta _ { 2 } ^ { i n d } a _ { 1 } | } { a _ { 1 } } \lesssim 2 \frac { m _ { 2 } } { m _ { 0 } } \frac { a _ { 1 } ^ { 2 } } { a _ { 2 } ^ { 2 } } .
$$

For the indirect perturbation of an interior planet $j = 2 , i = 1$

$$
\frac { | \Delta _ { 1 } ^ { i n d } a _ { 2 } | } { a _ { 2 } } \stackrel { < } { \sim } 2 \frac { m _ { 1 } } { m _ { 0 } } \frac { a _ { 2 } ^ { 2 } n _ { 2 } } { a _ { 1 } ^ { 2 } n _ { 1 } } \simeq 2 \frac { m _ { 1 } } { m _ { 0 } } \frac { \sqrt { a _ { 2 } } } { \sqrt { a _ { 1 } } } .
$$

For an upper bound to the direct perturbations we use the triangular inequality and the circular orbit approximation $| \mathbf { b } _ { i } - \mathbf { b } _ { j } | \geq | a _ { j } - a _ { i } |$

$$
\vert \Delta ^ { d i r } E _ { j } \vert \lesssim \frac { 1 } { \vert n _ { j } - n _ { i } \vert } ~ \frac { G m _ { i } } { \vert a _ { j } - a _ { i } \vert ^ { 2 } } ~ n _ { j } ~ a _ { j }
$$

and for the semimajor axis amplitude

$$
\frac { | \Delta ^ { d i r } a _ { j } | } { a _ { j } } \lesssim \frac { | \Delta ^ { d i r } E _ { j } | } { E _ { j } } = 2 \frac { m _ { i } } { ( m _ { 0 } + m _ { j } ) } \frac { n _ { j } } { | n _ { j } - n _ { i } | } \frac { a _ { j } ^ { 2 } } { | a _ { i } - a _ { j } | ^ { 2 } } .
$$

For the direct perturbation by an exterior planet $j = 1 , i = 2$

$$
\frac { | \Delta _ { 2 } ^ { d i r } a _ { 1 } | } { a _ { 1 } } \lesssim 2 \frac { m _ { 2 } } { m _ { 0 } } \frac { a _ { 1 } ^ { 2 } } { a _ { 2 } ^ { 2 } } ,
$$

that is the same estimate obtained for the indirect part. For the direct perturbation of an interior planet $j = 2 , i = 1$

$$
\frac { | \Delta _ { 1 } ^ { d i r } a _ { 2 } | } { a _ { 2 } } \lesssim 2 { \frac { m _ { 1 } } { m _ { 0 } } } { \frac { a _ { 2 } ^ { 2 } n _ { 2 } } { a _ { 2 } ^ { 2 } n _ { 1 } } } \simeq 2 { \frac { m _ { 1 } } { m _ { 0 } } } { \frac { { a _ { 1 } } ^ { 3 / 2 } } { a _ { 2 } ^ { 2 } ^ { 3 / 2 } } } ,
$$

which is qualitatively different from the estimate for the indirect part: for $a _ { 2 } / a _ { 1 } \to + \infty$ the direct perturbation of the interior planet $ 0$ , the indirect perturbation $ + \infty$ . The indirect perturbation of an interior planet may perturb the semimajor axis to arbitrarily large values, even to an apparent hyperbolic orbit. For growing $a _ { 2 }$ the attraction of the other bodies $ 0$ while the acceleration of the Sun due to $m _ { 1 } , \mathbf { b } _ { 1 }$ remains constant, until the indirect perturbation is larger than the attraction from the Sun.

For the perturbations from an exterior planet the estimates for the perturbations on the heliocentric semimajor axis contain the ratio $a _ { 1 } ^ { 2 } / a _ { 2 } ^ { 2 }$ , while the corresponding estimate computed in Jacobian coordinates would contain the Roy–Walker parameter $\epsilon _ { 2 1 }$ , proportional to $a _ { 1 } ^ { 3 } / a _ { 2 } ^ { 3 }$ . That is, for large $a _ { 2 } / a _ { 1 }$ the heliocentric perturbations are larger, but still $ 0$ for $a _ { 2 } / a _ { 1 } \to + \infty$ .

The conclusion from the discussion in this section and in Section 4.3 is that it may be necessary to use heliocentric coordinates to express planetary orbits with elements independent of the values of the mass ratios $m _ { j } / m _ { 0 }$ , but these elements could be sharply changing with time as a result of perturbations from interior planets. Jacobian coordinates could provide orbital elements more stable in time, but dependent upon the masses. Barycentric coordinates have an intermediate behavior, with perturbations larger than the Jacobian ones but without the divergence for $a _ { 2 } / a _ { 1 } \to + \infty$ of the heliocentric coordinates. Thus there is no choice optimal for all purposes: we need to use coordinate changes to exploit the best properties of each system.

# 4.6 Solar System dynamical models

The equation of motion for an $( N + 1 )$ -body system needs to be used as a dynamic model for the orbit determination of objects belonging to a planetary system, especially our own Solar System. Which terms have to be included in the equation of motion for a given orbit determination problem? This depends upon the orbits and upon the accuracy of the observations.

This section discusses the number of bodies to be included in the gravitational perturbation model and the non-gravitational perturbations. The effect of a non-spherical shape of the bodies is discussed in Chapter 13. The general relativistic perturbations are discussed in Section 6.6.

# How many bodies?

The first question about an $( N + 1 )$ -body model for the orbit of a given object is: how to choose $N$ ? Our Solar System contains the Sun, a number of major planets,4 the natural satellites of the planets, and a large population of minor bodies (asteroids, comets, trans-neptunian objects, Centaurs, even meteoroids). Of course we need to cut off at some level, and to use a consistent approximation we need to select some order of magnitude of the perturbations and to neglect the bodies resulting in lesser effects on the target body (or bodies) of the orbit determination.

The most efficient method to do this is to use the Jacobian coordinates and the Roy–Walker small parameters to estimate the perturbative effects. This does not imply that we have to use Jacobian coordinates as variables to be determined. The values of the $\epsilon _ { i j }$ parameters for perturbations by superior and inferior planets are given in Table II of (Walker et al. 1980); here we either reproduce or recompute some values.5

The conclusions to be drawn from Table 4.1, and from similar computations, of course depend upon the application. The accuracy required in the orbit computation has to be adequate for the accuracy of the observations. As an example, this table contains the parameters to be used to discuss the dynamical model for the orbit of the Earth, allowing the following conclusions: the perturbations from Ceres are more important than the ones from Pluto, the perturbations from Ganymede are negligible, and the problem of the orbit of the Moon is strongly coupled to the orbit of the Earth–Moon center of mass, thus it cannot be solved independently.

Table 4.1. Roy–Walker parameters for three-body subsystems of the Solar System.   

<table><tr><td>Subsystem</td><td>€12</td><td>E21</td></tr><tr><td>Sun-Mercury-Earth</td><td>2.5 ×10-8</td><td>1.7 ×10-7</td></tr><tr><td>Sun-Venus-Earth</td><td>1.3 × 10-6</td><td>1.1 × 10-6</td></tr><tr><td>Sun-Earth-Mars</td><td>1.3 × 10-6</td><td>9.2 ×10-8</td></tr><tr><td>Sun-Earth-Ceres</td><td>4.0 ×10-7</td><td>2.2 × 10-11</td></tr><tr><td>Sun-Earth-Jupiter</td><td>1.1 ×10-7</td><td>6.8 ×10-6</td></tr><tr><td>Sun-Earth-Saturn</td><td>3.3 ×10-8</td><td>3.3 ×10-7</td></tr><tr><td>Sun-Earth-Uranus</td><td>8.2 ×10-9</td><td>6.2 × 10-9</td></tr><tr><td>Sun-Earth-Neptune</td><td>3.3 ×10-9</td><td>1.9 ×10-9</td></tr><tr><td>Sun-Earth-Pluto</td><td>4.8×10-10</td><td>7.5 ×10-13</td></tr><tr><td>Earth-Moon-Sun Jupiter-Ganymede-Sun</td><td>7.9 ×10-8 1.5 × 10-10</td><td>5.7×10-3 2.7× 10-6</td></tr></table>

# Non-gravitational perturbations

Gravitation is the most penetrating interaction, in that it is coupled to the entire mass of a celestial body, without distinction between the near surface and the central portions. The other perturbations act essentially on the surface only. For example, electrostatic forces cannot be too important for macroscopic bodies even if they become highly charged, because charges tend to migrate towards the surface. Electromagnetic radiation interacts only with a comparatively thin layer near the surface, with thickness comparable to the wavelength. Drag is an interaction, due to electromagnetic forces, of external particles with the surface. Thus a small parameter appearing in all non-gravitational perturbations is the area-to-mass ratio

$$
\frac { A } { m } \simeq \frac { \pi R ^ { 2 } } { \frac { 4 \pi } { 3 } \rho R ^ { 3 } } = \frac { 3 } { 4 \rho R }
$$

where $A$ is the cross-sectional area, $\rho$ the average density, $R$ the radius of the perturbed body, and the approximate formula becomes exact for a spherical body. The simplest example is the direct radiation pressure force due to sunlight $F = ( \Phi / c ) A$ , where $\Phi$ is the radiation energy flow (per unit crosssection) at the given distance from the Sun $r _ { \odot }$ and $c$ is the speed of light. The ratio of radiation pressure force to gravitational attraction is

$$
\beta = \frac { \Phi A r _ { \odot } ^ { 2 } } { G m _ { \odot } m c }
$$

where $m _ { \odot } = m _ { \odot }$ is the Sun mass. The energy flow from the Sun, because of $E = m c ^ { 2 }$ , carries away mass from the Sun at a rate $\dot { m } _ { \odot } = 4 \pi r _ { \odot } ^ { 2 } \Phi / c ^ { 2 } \simeq$ ${ 7 } \times 1 0 ^ { - 1 4 } m _ { \odot } / \mathrm { y }$ , that is, the Sun decreases its mass due to shedding of photons with a characteristic time $^ 6$ $t _ { \odot } = m _ { \odot } / \dot { m } _ { \odot } \simeq 1 . 5 \times 1 0 ^ { 1 3 }$ y. Thus

$$
\beta \simeq \frac { A } { m } \frac { \dot { m } _ { \odot } } { m _ { \odot } } \frac { c } { 4 \pi G } .
$$

In CGS units, $c / 4 \pi G \simeq 3 \times 1 0 ^ { 1 6 }$ and $3 \times 1 0 ^ { 1 6 } ~ \mathrm { s } \simeq 1 0 ^ { 9 } ~ \mathrm { { J } }$ , thus

$$
\beta = { \frac { A } { m } } { \frac { 1 } { t _ { \odot } } } \simeq { \frac { A } { m } } { \frac { 1 } { 1 5 0 0 0 } } \qquad \mathrm { ( u n i t ~ o f ~ } t _ { \odot } \mathrm { ~ i n ~ b i l l i o n ~ y e a r s } \mathrm { ) . }
$$

Let us use this estimate to assess when radiation pressure can be a significant perturbation of a heliocentric orbit.

For a planet, e.g., Mercury, $\rho \simeq 5$ and $R \simeq 2 4 0 0 ~ \mathrm { k m }$ , $A / m \simeq 6 \times 1 0 ^ { - 1 0 }$ and $\beta \simeq 4 \times 1 0 ^ { - 1 4 }$ : radiation pressure is almost at the rounding off level.   
For a small asteroid with $\rho \simeq 1 . 5$ and $R \simeq 5 0 0 \mathrm { ~ m ~ }$ , $A / m \simeq 2 \times 1 0 ^ { - 5 }$ and $\beta \simeq 1 . 3 \times 1 0 ^ { - 9 }$ : radiation pressure is small, negligible for astrometric observations, but it cannot be neglected if very accurate observations (e.g., radar, tracking of an orbiter) are available.   
For a spacecraft, $A \simeq 5 ~ \mathrm { m } ^ { 2 }$ and $m \simeq 5 0 0 ~ \mathrm { k g }$ , $A / m \simeq 0 . 1$ and $\beta \simeq 7 \times 1 0 ^ { - 6 }$ is not negligible at all. Radiation pressure and other non-gravitational forces acting on spacecraft are discussed in Chapter 14.   
• For a dust particle of given density, e.g., $\rho = 2$ , there is a critical radius at which $\beta = 1$ : for spherical shape $A / m = 3 / 8 R$ and $\beta = 2 . 5 \times 1 0 ^ { - 5 } / R = 1$ implies $R = 0 . 2 5$ micron. For a particle of this size this is a simplistic model of the particle/wave interaction, but the order of magnitude is right, particles in the sub-micron range released from a Solar System orbit at low relative velocity are not bound to the Solar System: they are called $\beta$ -particles.

# Part II

Basic Theory