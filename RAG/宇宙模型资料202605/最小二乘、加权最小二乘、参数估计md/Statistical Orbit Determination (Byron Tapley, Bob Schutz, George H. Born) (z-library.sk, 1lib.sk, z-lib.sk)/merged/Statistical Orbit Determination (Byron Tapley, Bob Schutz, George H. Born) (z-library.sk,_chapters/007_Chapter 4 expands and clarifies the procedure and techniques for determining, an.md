Chapter 4 expands and clarifies the procedure and techniques for determining, and assessing the accuracy of, the estimate $\hat { \mathbf { x } } _ { k }$ . Further details are given on computational methods for determining $\hat { \mathbf { x } } _ { k }$ in Chapter 5.

# 1.3 BACKGROUND AND OVERVIEW

As noted in this introductory chapter, orbit determination methodology can be separated into two general classes, for example, classical (or deterministic) orbit determination and modern (or statistical based) orbit determination. In the classical approach, observational errors are not considered and the problem is reduced to making the necessary number of measurements to determine the orbit. There is an equivalence between the number of observations and the number of unknowns. The modern orbit determination problem recognizes the influence of observation errors and, to minimize the effects of the observational error, more observations are used than the number of parameters to be estimated. Modern orbit determination methodology dates back to the beginning of the 19th century, when Legendre (1806), in attempting to determine the orbits of the planets, recognized the importance of observational errors and proposed the least squares solution as a method for minimizing the effect of such errors. Gauss (1809) presented a probabilistic basis for the method of least squares, which was closely akin to the maximum likelihood method proposed by Fisher (1912). Gauss (1809) stated that he had used the method since 1795 and historians (Cajori, 1919) generally agree that Gauss originated the method. The notation of Gauss is still in use. Laplace (1812) added refinements to the computational approach and to the statistical foundations. Markov (1898), in his work on the mathematical foundations of probability theory, clarified many of the concepts associated with the method of least squares. Helmert (1900) extended the application to astronomy and geodesy. In the 20th century, Kolmogorov (1941) and Wiener (1949) linked the problem to modern systems theory and set the stage for the sequential filter formulation for processing tracking data. In 1959, Swerling gave the first conceptual approach to the sequential orbit determination problem. Kalman (1960) presented a mathematically rigorous approach for the sequential processing of observations of a linear dynamic system. In a later work, Kalman and Bucy (1961)

gave an approach for the extended Kalman filter, which is the sequential approach for the general nonlinear orbit determination problem. Following the publication of Kalman’s paper in 1960, there was an extensive series of publications related to this topic during the next three decades. Many of these investigations will be referenced in the subsequent chapters. A summary of the historical development of the least squares approach is given by Sorenson (1970).

The main thrust of this book will be aimed at developing computational data processing techniques for estimating the state of orbiting satellites. As noted in the previous discussion, the problem formulation will lead to a nonlinear relation between the observations and the epoch state of the satellite. Therefore, in modern system theory terms, we will be concerned with estimating the state of a nonlinear dynamic system, using observations of nonlinear functions of the system state, where the observations are corrupted by random and systematic observational errors. Although the main focus for the physical models will be the orbit determination problem, the problem will be cast in the state space notation defined by modern system theory. As such, the computational approaches presented in the treatment will be applicable to a wide range of problems, including missile guidance, attitude control, economic system analysis, chemical process control, and a wide variety of manufacturing processes. Once the defining equations from these processes have been reduced to the state space formulation, the computational techniques developed here will be applicable.

# 1.4 SUMMARY

Following the introduction of the basic concepts of nonlinear parameter estimation in Chapter 1, Chapter 2 provides a detailed discussion of the characteristics of the orbit for Earth-orbiting satellites. This is the primary dynamical system of interest in this treatment. Chapter 3 describes the various observations used in the Earth-orbiting satellite orbit determination problem. Chapter 4 describes the properties of the Weighted Least Squares and Minimum Variance Estimation algorithms as they are expressed in a batch estimation form and describes the transformation to the sequential estimation algorithm. The relation to the Kalman filter is noted. In Chapter 5, the computation algorithms for solving the linear system based on both the Cholesky Decomposition and the Orthogonal Transformation approach are presented. In addition, square root sequential estimation algorithms are given. Chapter 6 describes the error analysis approaches that evolve from the Consider covariance analysis. The algorithms developed here account for the effects of uncertainties on unestimated parameters that appear in either the dynamic or measurement equations.

As noted previously, a primary emphasis of this treatment will be devoted to developing computationally robust and efficient algorithms for processing the

observations of Earth-orbiting satellites.

# 1.5 REFERENCES

Cajori, F., A History of Mathematics, MacMillan Co., New York, 1919.

Fisher, R. A., “On an absolute criteria for fitting frequency curves,” Mess. Math., Vol. 41, pp. 155–160, 1912.

Gauss, K. F., Theoria Motus Corporum Coelestium, 1809 (Translated into English: Davis, C. H., Theory of the Motion of the Heavenly Bodies Moving about the Sun in Conic Sections, Dover, New York, 1963).

Helmert, F. R., “Zur Bestimmung kleiner Flachenst ¨ ucke des Geoids aus Lothab- ¨ weichungen mit Rucksicht auf Lothkr ¨ ummung”, Sitzungsberichte Preuss. ¨ Akad. Wiss., Berlin, Germany, 1900.

Kalman, R. E., “A New Approach to Linear Filtering and Prediction Theory,” J. Basic Eng., Vol. 82, Series E, No. 1, pp. 35–45, March 1960.

Kalman, R. E. and R. S. Bucy, “New Results in Linear Filtering and Prediction Theory,” J. Basic Eng., Vol. 83, Series D, No. 1, pp. 95–108, March 1961.

Kolmogorov, A. N., “Interpolation and Extrapolation of Stationary Random Sequences,” Bulletin of the Academy of Sciences of the USSR Math. Series, Vol. 5, pp. 3–14, 1941.

Laplace, P. S., Theorie Analytique de Probabilit ´ es´ , Paris, 1812 (The 1814 edition included an introduction, Essai Philosophique sur les Probabilites´ , which has been translated into English: Dale, A. I., Philosophical Essay on Probabilities, Springer-Verlag, New York, 1995).

Legendre, A. M., Nouvelles methodes pour la d ´ etermination des orbites des ´ cometes \` , Paris, 1806.

Markov, A. A., “The law of large numbers and the method of Least Squares,” (1898), Izbr. Trudi., Izd. Akod. Nauk, USSR, pp. 233–251, 1951.

Sorenson, H. W., “Least squares estimation: from Gauss to Kalman,” IEEE Spectrum, Vol. 7, No. 7, pp. 63–68, July 1970.

Swerling, P., “First order error propagation in a stagewise differential smoothing procedure for satellite observations,” J. Astronaut. Sci., Vol. 6, pp. 46–52, 1959.

Wiener, N., The Extrapolation, Interpolation and Smoothing of Stationary Time Series, John Wiley & Sons, Inc., New York, 1949.

# 1.6 EXERCISES

1. Write a computer program that computes $\rho ( t _ { i } )$ for a uniform gravity field ρ tusing Eq. (1.2.10). A set of initial conditions, $X _ { 0 }$ , $\dot { X } _ { 0 }$ , $Y _ { 0 }$ , $\dot { Y } _ { 0 }$ , $g$ , $X _ { s }$ , $Y _ { s }$ , and observations, $\rho$ X X Y Y g X, follow. With the exception of the station coordi-Y ρnates, the initial conditions have been perturbed so that they will not produce exactly the observations given. Use the Newton iteration scheme of Eq. (1.2.9) to recover the exact initial conditions for these quantities; that is, the values used to generate the observations. Assume that $X _ { s }$ and $Y _ { s }$ are known exactly. Hence, they are not solved for.

# Unitless Initial Conditions

$$
\begin{array} { c } { { X _ { 0 } = 1 . 5 } } \\ { { Y _ { 0 } = 1 0 . 0 } } \\ { { \dot { X } _ { 0 } = 2 . 2 } } \\ { { \dot { Y } _ { 0 } = 0 . 5 } } \\ { { g = 0 . 3 } } \\ { { X _ { s } = Y _ { s } = 1 . 0 } } \end{array}
$$

Answer

$$
\begin{array} { r } { X _ { 0 } = 1 . 0 } \\ { Y _ { 0 } = 8 . 0 } \\ { \dot { X } _ { 0 } = 2 . 0 } \\ { \dot { Y } _ { 0 } = 1 . 0 } \\ { g = 0 . 5 } \end{array}
$$

2. In addition to the five state variables of Exercise 1, could $X _ { s }$ and $Y _ { s }$ be solved for given seven independent observations of $\rho$ X Y? Why or why not? Hint: Notice the relationship between $X _ { 0 }$ and $X _ { s }$ ρand between $Y _ { 0 }$ and $Y _ { s }$ in Eq. (1.2.7) for $\rho _ { j }$ X X. See also Section 4.12 on observability.

# The Orbit Problem

# 2.1 HISTORICAL BACKGROUND

Johannes Kepler, based on a study of planetary position data acquired by Tycho Brahe, formulated three laws of planetary motion (Plummer, 1918):

1. The orbit of each planet is an ellipse with the Sun at one focus;   
2. The heliocentric radius vector of each planet sweeps over equal area in equal time;   
3. The square of the orbital period is proportional to the cube of the ellipse semimajor axis.

But it was Isaac Newton who established the mathematical foundation from which Kepler’s Laws can be derived. Newton’s insightful analysis of the work of Kepler led to the formulation of the basic concepts of mechanics and gravitation at an early stage in his career. Not until he was in his forties, however, did Newton publish these concepts in the Principia (1687), as described in the extensive biography by Westfall (1980) .

The Principia presented the Three Laws of Motion, quoted from p. 13 of Motte’s 1729 English translation of Newton’s Latin publication (with modern terminology in brackets):

Law I: Every body continues in its state of rest, or of uniform motion in a right line [straight line] unless it is compelled to change that state by forces impressed upon it.

Law II: The change of motion is proportional to the motive force impressed; and is made in the direction of the right line in which that force is impressed. $\mathbf { \dot { F } } = m \mathbf { a }$ , where $\mathbf { F }$ is force, $m$ is mass, and a is acceleration, which is equal to the time derivative of velocity, V.]

Law III: To every action there is always opposed an equal reaction: or, the mutual actions of two bodies upon each other are always equal, and directed to contrary parts.

Newton deduced the Law of Gravitation as well, which states: the mutual force of gravitational attraction between two point masses is

$$
F = { \frac { G M _ { 1 } M _ { 2 } } { d ^ { 2 } } }
$$

where $G$ is the Universal Constant of Gravitation and $d$ is the distance between the two point masses or particles, $M _ { 1 }$ and $M _ { 2 }$ .

The Laws of Newton contain some important concepts. The concept of a point mass is embodied in these laws, which presumes that the body has no physical dimensions and all its mass is concentrated at a point. The concept of an inertial reference frame is crucial to Newton’s Second Law; that is, the existence of a coordinate system that has zero acceleration. The concept of force $( \mathbf { F } )$ i s introduced as the cause of the acceleration experienced by a point mass, and the mass $( m )$ is the constant of proportionality implied by Newton’s statement of the Second Law. Finally, the concept of a uniformly changing time is fundamental to Newton’s Laws of Motion.

These laws are the foundation of the mathematical description of orbital dynamics. To this day, the laws enable a remarkably accurate description of the motion of both natural and arti cial bodies. The work of Albert Einstein [1905] provided even greater insight into this description and allowed the explanation of small discrepancies between observation and Newtonian dynamics.

The description of orbital dynamics in this book is Newtonian in nature. Inclusion of relativistic corrections is important for those applications that require high accuracy, and the relevant terms are described in this chapter.

Subtle differences in terminology exist in the literature concerning the distinction between reference frames and reference systems, for example. A careful and precise set of de nitions is discussed by Kovalevsky et al. (1989). For purposes of this book, the terminology reference frame will be used within a context that describes some speci c characteristic (e.g., inertial reference frame). The terminology coordinate system generally will apply to a set of axes that is used to describe the motion of a body. In some instances, reference frame and coordinate system are used interchangeably where there is no ambiguity.

In the following sections, the description of satellite motion is developed, beginning with the two-body gravitational model of satellite motion. The fundamental description from the problem of two bodies serves as a useful reference, but it is inadequate for the accurate representation of the actual satellite motion. The more complete and realistic representation will be developed from the twobody case. It is not the intent of the development in this chapter to provide an exhaustive treatise on orbital mechanics, since excellent books already exist (e.g., Szebehely and Mark, 1998; Vallado, 2001; Bond and Allman, 1996; Chobotov, 1996; Prussing and Conway, 1993; Danby, 1988; Roy, 1988; Battin, 1999; and Schaub and Junkins, 2003). The philosophy in this chapter is to provide the key steps in the development and its interpretation, especially within the context of the main purpose related to the determination of the orbit. With this philosophy, many details are left to you, although the preceding list of references provides most of the details.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0001_pages_0001-0070/auto/images/cdc4393127e0b1aba02629735a963310af074bcf713b3cfae45c7d1ef98c313d.jpg)  
Figure 2.2.1: The problem of two bodies: $M _ { 1 }$ and $M _ { 2 }$ are spheres of constant, uniform density. The position vectors of the spheres refer to their respective geometrical center, which also coincide with the center of mass of the sphere.

# 2.2 PROBLEM OF TWO BODIES: GENERALPROPERTIES

The classic problem of two bodies was solved by Newton, which is repeated in a modern form by all treatises on celestial mechanics. The classic treatment describes the motion of two point masses. However, human experience demonstrates that the Earth has physical dimensions, and a point mass Earth is a serious stretch of the imagination. Nevertheless, a spherical body with constant, uniform mass distribution can be shown to be gravitationally equivalent to a point mass. Thus, as a more realistic approximation to the physical characteristics of a planet, a spherical body will be used in the following development.

Consider the motion of two spheres of mass $M _ { 1 }$ and $M _ { 2 }$ , as illustrated in Fig. 2.2.1. No restrictions are placed on the magnitude of these masses, so for illustrative purposes, assume $M _ { 1 }$ represents the Earth and $M _ { 2 }$ represents a satellite, including the Moon. The coordinate system $( X , \ Y , \ Z )$ is inertial and nonrotating; that is, it has no acceleration, and there is no preferred orientation of the axes at this stage. The position vectors of the geometrical centers of the respective spheres are ${ \bf R } _ { 1 }$ and ${ \bf R } _ { 2 }$ . The position of $M _ { 2 }$ with respect to $M _ { 1 }$ is described by $\mathbf { r }$ . The equations of motion derived from Newton’s Laws of Motion and Law of Gravitation are

$$
\begin{array} { l c l } { { { \cal M } _ { 1 } { \ddot { \bf R } } _ { 1 } } } & { { = } } & { { \displaystyle \frac { G M _ { 1 } M _ { 2 } { \bf r } } { r ^ { 3 } } } } \\ { { { \cal M } _ { 2 } { \ddot { \bf R } } _ { 2 } } } & { { = } } & { { \displaystyle - \frac { G M _ { 1 } M _ { 2 } { \bf r } } { r ^ { 3 } } } } \end{array}
$$

where $\ddot { \bf R } _ { 1 } = d ^ { 2 } { \bf R } _ { 1 } / d t ^ { 2 }$ and $t$ represents time. It can readily be shown that the equations of relative motion are

$$
{ \ddot { \mathbf { r } } } = - { \frac { \mu \mathbf { r } } { r ^ { 3 } } }
$$

where $\mu = G ( M _ { 1 } + M _ { 2 } )$ . In the case of an arti ci al satellite of the Earth, let $M _ { 1 }$ represent the Earth and $M _ { 2 }$ the satellite. Since the Earth is so massive, even a large satellite like a fully loaded space station results in

$$
\mu = G ( M _ { 1 } + M _ { 2 } ) \cong G M _ { 1 }
$$

to very high accuracy (better than one part in $1 0 ^ { 1 5 }$ ).

The general characteristics of the motion follow from manipulation of Eqs. (2.2.1) and (2.2.2):

1. Motion of Two-Body Center of Mass. The de nition of the position of the center of mass of the two spheres, $\mathbf { R } _ { \mathrm { c m } }$ , is

$$
{ \bf R } _ { \mathrm { c m } } = \frac { M _ { 1 } { \bf R } _ { 1 } + M _ { 2 } { \bf R } _ { 2 } } { \left( M _ { 1 } + M _ { 2 } \right) } .
$$

By adding Eqs. (2.2.1) and (2.2.2) it follows that

$$
\ddot { \mathbf { R } } _ { \mathrm { c m } } = 0 \quad \mathrm { a n d } \quad \mathbf { R } _ { \mathrm { c m } } = \mathbf { C } _ { 1 } ( t - t _ { o } ) + \mathbf { C } _ { 2 }
$$

where $\mathbf { C } _ { 1 }$ and $\mathbf { C } _ { 2 }$ are constants of the motion. Equation (2.2.5) states that the center of mass of the two spheres moves in a straight line with constant velocity. Note that the straight line motion of the center of mass is de ned in an inertial coordinate system.

2. Angular Momentum. Taking the vector cross product of $\mathbf { r }$ with both sides of Eq. (2.2.3) gives

$$
\mathbf { r } \times { \ddot { \mathbf { r } } } = 0 \quad { \mathrm { o r } } \quad { \frac { d } { d t } } ( \mathbf { r } \times { \dot { \mathbf { r } } } ) = 0 .
$$

Defining $\textbf { h } = \textbf { r } \times \dot { \textbf { r } }$ , the angular momentum per unit mass (or specific angular momentum), it follows that $\mathbf { h }$ is a vector constant:

$$
\mathbf { h } = \mathbf { r } \times { \dot { \mathbf { r } } } = \mathbf { c o n s t a n t } .
$$

An important interpretation of $\textbf { h } =$ constant is that the orbital motion is planar, since $\mathbf { r }$ and $\dot { \mathbf { r } }$ must always be perpendicular to $\mathbf { h }$ . The plane of the motion is referred to as the orbit plane, which is a plane that is perpendicular to the angular momentum vector. Note that the angular momentum in Eq. (2.2.6) is defined for the motion of $M _ { 2 }$ with respect to $M _ { 1 }$ .

3. Energy. Taking the vector dot product of $\dot { \mathbf { r } }$ with Eq. (2.2.3), it can be shown that

$$
\xi = { \frac { { \dot { \mathbf { r } } } \cdot { \dot { \mathbf { r } } } } { 2 } } - { \frac { \mu } { r } } = \mathrm { c o n s t a n t }
$$

where $\xi$ is the scalar energy per unit mass (also known as specific energy or vis viva) and $\dot { \mathbf { r } }$ is the velocity of $M _ { 2 }$ with respect to $M _ { 1 }$ . Thus, the energy per unit mass is constant; that is, the sum of the kinetic and potential energies is constant. Note that this expression describes the energy in terms of the motion of $M _ { 2 }$ with respect to $M _ { 1 }$ .

In summary, there are ten constants of the motion: $\mathbf { C } _ { 1 }$ $\mathbf { \Sigma } _ { 1 , 1 , 2 , \mathbf { h } , \xi } ^ { \bullet }$ . The following general properties of the orbital motion can be stated:

a. The motion of $M _ { 2 }$ with respect to $M _ { 1 }$ takes place in a plane, the orbit plane, defined as the plane that is perpendicular to the constant angular momentum vector $( \mathbf { h } = \mathbf { r } \times { \dot { \mathbf { r } } } ,$ );   
b. The center of mass of the two bodies moves in a straight line with constant velocity with respect to an inertial coordinate system;   
c. The scalar energy per unit mass is constant, as given by Eq. (2.2.7).

# 2.2.1 MOTION IN THE PLANE

The previous section summarized some general characteristics of the twobody motion, but the differential equations of motion, Eq. (2.2.3), were not solved. The detailed characteristics of the orbital motion are still to be determined, as described in this section.

The previous section showed that the orbital motion of $M _ { 2 }$ with respect to $M _ { 1 }$ takes place in a plane perpendicular to the angular momentum vector. This fact of planar motion can be used to facilitate the solution of Eq. (2.2.3). The planar motion is illustrated in Fig. 2.2.2, described with respect to a nonrotating $( X , Y , Z )$ coordinate system. The $\hat { X }$ axis is shown at the intersection of the orbit plane and the $( X , Y )$ plane, where the intersection between the planes is referred to as the line of nodes. The angles $i$ and $\Omega$ are discussed in Section 2.2.2. The $\hat { Y }$ axis is perpendicular to $\hat { X }$ , but it lies in the orbit plane, whereas $\hat { Z }$ is coincident with $\mathbf { h }$ . Since the angular momentum vector, $\mathbf { h }$ , is constant, the orientation of the orbit plane in space does not change with time, and the $( \hat { X } , \hat { Y } , \hat { Z } )$ axes are, therefore, nonrotating. From the introduction of a unit vector, $\mathbf { u } _ { r }$ , defined by $\mathbf { r } = r \ \mathbf { u } _ { r }$ and the unit vector, $\mathbf { u } _ { \theta }$ , as illustrated in Fig. 2.2.3, it follows that Eq. (2.2.3) can be written in polar coordinates as

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0001_pages_0001-0070/auto/images/a67bf4ce0d81ec3e5e0fdc8a9b02d70601f4695f443760e9b2a726aefba01426.jpg)  
Figure 2.2.2: The orbit plane in space. Since the angular momentum is constant, the motion of $M _ { 2 }$ with repect to $M _ { 1 }$ takes place in a plane, known as the orbit plane. This plane is perpendicular to the angular momentum vector and the orientation is defined by the angles $i$ and $\Omega$ .

$$
\begin{array} { c c } { { \bf u } _ { r } \mathrm { c o m p o n e n t : } } & { { \ddot { r } - r \dot { \theta } ^ { 2 } = - \frac { \mu } { r ^ { 2 } } } } \\ { { \bf u } _ { \theta } \mathrm { c o m p o n e n t : } } & { { 2 \dot { r } \dot { \theta } + r \ddot { \theta } = 0 . } } \end{array}
$$

Two cases exist: $\dot { \theta } = 0$ and $\dot { \theta } \neq 0$ . The $\dot { \theta } = 0$ case is rectilinear motion, which is a special case of no interest in this discussion. For the orbital motion case, $\dot { \theta } \neq 0$ , and it can be shown from Eq. (2.2.9) that

$$
{ \frac { d } { d t } } ( r ^ { 2 } { \dot { \theta } } ) = 0 .
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0001_pages_0001-0070/auto/images/b8669705dbf7a6094502bcc4cf856c5e0202c6813938488f09020e8c54a84552.jpg)  
Figure 2.2.3: The planar motion described with polar coordinates.

Note that since ${ \dot { \mathbf { r } } } = { \dot { r } } \mathbf { u } _ { r } + r { \dot { \theta } } \mathbf { u } _ { \theta }$ , it follows from $\mathbf { h } = \mathbf { r } \times { \dot { \mathbf { r } } }$ that $\mathbf { h } = r ^ { 2 } { \dot { \theta } } { \mathbf { u } } _ { h }$ , where $\mathbf { u } _ { h }$ is the unit vector in the $\mathbf { h }$ direction. It is evident that $\textit { h } = r ^ { 2 } \Dot { \theta }$ is constant. Furthermore, a change in both the dependent and independent variables in Eq. (2.2.8)

$$
r \to 1 / u , \quad t \to \theta
$$

gives the differential equation of motion

$$
{ \frac { d ^ { 2 } u } { d \theta ^ { 2 } } } + u = { \frac { \mu } { h ^ { 2 } } }
$$

which has the solution

$$
u = \frac { \mu } { h ^ { 2 } } + A \cos ( \theta - \omega )
$$

where $A$ and $\omega$ are constants of integration.

From Eq. (2.2.7) for the energy, it can be shown that

$$
A = { \frac { \mu } { h ^ { 2 } } } e
$$

where

$$
e = \left[ 1 + 2 \frac { \xi h ^ { 2 } } { \mu ^ { 2 } } \right] ^ { \frac { 1 } { 2 } } ,
$$

a positive quantity.

Table 2.2.1: Classes of Orbital Motion   

<table><tr><td>Orbit Type</td><td>Eccentricity</td><td>Energy</td><td>Orbital Speed</td></tr><tr><td>Circle</td><td>e=0</td><td>=- 品</td><td>V=√u/r</td></tr><tr><td>Ellipse</td><td>e&lt;1</td><td>m&lt;0</td><td>√μ/r &lt;V&lt;√2μ/r</td></tr><tr><td>Parabola</td><td>e=1</td><td>m=0</td><td>V = √2μ/r</td></tr><tr><td>Hyperbola</td><td>e&gt;1</td><td>m&gt;0</td><td>V &gt;√2μ/r</td></tr></table>

It follows from Eq. (2.2.13) that

$$
r = \frac { h ^ { 2 } / \mu } { 1 + e \cos ( \theta - \omega ) } .
$$

It can be readily shown that

$$
\frac { d r } { d \theta } = \frac { \mu e \sin ( \theta - \omega ) } { h ^ { 2 } ( 1 + \cos ( \theta - \omega ) ) ^ { 2 } }
$$

from which it follows that

$$
\frac { d r } { d \theta } = 0
$$

when $\theta = \omega$ or $\theta - \omega = \pi$ . Furthermore, since

$$
\frac { d ^ { 2 } r } { d \theta ^ { 2 } } > 0
$$

at $\theta = \omega$ , it is evident that $r$ is a minimum. This location with minimum $r$ is referred to as the perifocus, or perigee in the case of a satellite of the Earth. As a consequence, the constant of integration $\omega$ is known as the argument of perigee.

Introducing the true anomaly, $f$ defined by $f = \theta - \omega$ , then the expression for $r$ becomes

$$
r = { \frac { p } { 1 + e \cos f } }
$$

where $p = h ^ { 2 } / \mu$

The form of Eq. (2.2.15) is identical to the geometrical equation for a conic section (for example, see Danby [1988]). The geometrical quantities $p$ and $e$ are the semilatus rectum and eccentricity of the conic section, respectively. As shown in the preceding equations, these geometrical parameters are determined by dynamical parameters $h , \xi$ , and $\mu$ .

The two-body orbit can be described as a conic section: circle, ellipse, parabola, or hyperbola. The specific conic section is determined by the eccentricity, e. Each conic section has a specific energy and velocity for a given $r$ , as shown in Table 2.2.1.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0001_pages_0001-0070/auto/images/34766eeedf52c00237142982948ba8dbc33f9852a0ef5e0917dbdc4442d091ea.jpg)  
Figure 2.2.4: Characteristics of the elliptic orbit. The circle has radius equal to $a$ and is used to illustrate the eccentric anomaly, $E$ . The dashed line is perpendicular to the major axis of the ellipse.

Only the conic sections with $e < 1$ are closed paths. The parabola and hyperbola are often referred to as escape trajectories.

Equation (2.2.15) describes the position of $M _ { 2 }$ with respect to $M _ { 1 }$ , where $M _ { 1 }$ is located at a focus of the conic section, and the position of $M _ { 2 }$ is described in terms of $r$ and $f$ . The ellipse conic section, as illustrated in Fig. 2.2.4, has two foci, where $M _ { 1 }$ is located at one focus and the other is an empty focus. The ellipse is defined by $p$ and $e$ , but other parameters are commonly used, such as semimajor axis $( a )$ and semiminor axis $( b )$ . Some useful geometrical relations are

$$
\begin{array} { r c l } { { p } } & { { = } } & { { a ( 1 - e ^ { 2 } ) } } \\ { { b } } & { { = } } & { { a \sqrt { 1 - e ^ { 2 } } . } } \end{array}
$$

Note that $p = r$ when $f = \pm \pi / 2$ .

The minimum distance between $M _ { 1 }$ and $M _ { 2 }$ is the perifocus (or perigee if $M _ { 1 }$ is the Earth), given by

$$
r _ { p } = a ( 1 - e )
$$

and the maximum distance, apfocus (or apogee for an Earth satellite) is

$$
r _ { a } = a ( 1 + e ) .
$$

Other relations between geometrical and dynamical parameters for the elliptical orbit can be shown to be

$$
\begin{array} { r } { h ^ { 2 } = \mu a ( 1 - e ^ { 2 } ) = \mu p } \\ { \xi = - \displaystyle \frac { \mu } { 2 a } . } \end{array}
$$

The $M _ { 2 }$ velocity, $\mathbf { V }$ , with respect to $M _ { 1 }$ can be written as

$$
{ \bf V } = \dot { r } { \bf u } _ { r } + r \dot { f } { \bf u } _ { \theta } .
$$

The magnitude of the $M _ { 2 }$ velocity (with respect to $M _ { 1 }$ ), or speed, is

$$
V = \sqrt { \mu ( 2 / r - 1 / a ) }
$$

and it can be shown that the radial component of the velocity, $\dot { r }$ , is

$$
\dot { r } = \frac { h e \sin f } { p }
$$

from which it is evident that the radial velocity is positive (away from $M _ { 1 }$ ) while traveling from perifocus to apfocus, and it is negative (toward $M _ { 1 }$ ) from apfocus to perifocus. Furthermore, from $h = r ^ { 2 } { \dot { f } }$ (since ${ \dot { f } } = { \dot { \theta } }$ ), the velocity component perpendicular to the position vector is

$$
r { \dot { f } } = { \frac { h } { r } } .
$$

As demonstrated by Vallado (2001), for example, the area (A) swept out by $r$ as a function of time is

$$
{ \frac { d A } { d t } } = { \frac { h } { 2 } }
$$

which is constant, thereby demonstrating Kepler’s Second Law. If this equation is integrated over one orbital period, $T$ , the time required for $M _ { 2 }$ to complete one revolution of $M _ { 1 }$ (for example, from perifocus and back to perifocus) is

$$
T = \frac { 2 \pi a ^ { 3 / 2 } } { \mu ^ { 1 / 2 } } .
$$

This equation verifies Kepler’s Third law.

From the conic section equation, Eq. (2.2.14), if the angle $f$ is known, the distance $r$ can be determined. However, for most applications, the time of a particular event is the known quantity, rather than the true anomaly, $f$ . A simple relation between time and true anomaly does not exist. The transformation between time and true anomaly uses an alternate angle, $E$ , the eccentric anomaly, and is expressed by Kepler’s Equation, which relates time and $E$ as

$$
E - e \sin E = n ( t - t _ { p } )
$$

where $n$ is the mean motion $( \sqrt { \mu / a ^ { 3 } } )$ , $t$ is time, and $t _ { p }$ is the time when $M _ { 2 }$ is located at perifocus. The time $t _ { p }$ is a constant of integration. Since Kepler’s Equation is a transcendental equation, its solution can be obtained by an iterative method, such as the Newton–Raphson method. If

$$
g = E - e \sin E - M ,
$$

where $M = n ( t - t _ { p } )$ , the mean anomaly, then the iterative solution gives

$$
E _ { k + 1 } = E _ { k } - \left( \frac { g } { g ^ { \prime } } \right) _ { k } ,
$$

where $k$ represents the iteration number and

$$
g ^ { \prime } = \frac { d g } { d E } = 1 - e \cos E .
$$

From known values of $a$ and $e$ and a specifie $\textrm { d } t$ , the preceding iterative method will provide the eccentric anomaly, $E$ . A typical value of $E$ to start the iteration is $E _ { 0 } = M$ . Some useful relations between the true anomaly and the eccentric anomaly are

$$
\begin{array} { c c } { { \sin f = \displaystyle \frac { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } \sin E } { 1 - e \cos E } \quad } } & { { \sin E = \displaystyle \frac { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } \sin f } { 1 + e \cos f } } } \\ { { \cos f = \displaystyle \frac { \cos E - e } { 1 - e \cos E } \quad } } & { { \cos E = \displaystyle \frac { e + \cos f } { 1 + e \cos f } } } \\ { { \tan \displaystyle \frac { f } { 2 } = \displaystyle \left( \frac { 1 + e } { 1 - e } \right) ^ { 1 / 2 } \tan \displaystyle \frac { E } { 2 } \quad } } & { { \tan \displaystyle \frac { E } { 2 } = \displaystyle \left( \frac { 1 - e } { 1 + e } \right) ^ { 1 / 2 } \tan \displaystyle \frac { f } { 2 } } } \end{array}
$$

$$
{ \begin{array} { r c l } { M } & { = } & { E - e \sin E { \mathrm { ( K e p l e r ' s ~ E q u a t i o n ) } } } \\ { { \frac { d f } { d E } } } & { = } & { { \frac { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } { 1 - e \cos E } } = { \frac { 1 + e \cos f } { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } } } \\ { { \frac { d M } { d E } } } & { = } & { 1 - e \cos E = { \frac { 1 - e ^ { 2 } } { 1 + e \cos f } } } \\ { { \frac { d M } { d f } } } & { = } & { { \frac { ( 1 - e \cos E ) ^ { 2 } } { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } } = { \frac { ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } { ( 1 + e \cos f ) ^ { 2 } } } . } \end{array} }
$$

It can be shown that

$$
r = a ( 1 - e \cos E )
$$

but in some cases it is useful to express $r$ as a function of time, or mean anomaly. This relation for elliptic orbits, however, involves an infinite series because of the

transcendental nature of Kepler’s Equation; namely,

$$
\frac { a } { r } = 1 + 2 \sum _ { m = 1 } ^ { \infty } \hat { J } _ { m } ( m e ) \cos m M
$$

where ${ \hat { J } } _ { m } $ is the Bessel Function of the first kind of order $m$ , with argument me (see Smart, 1961; Brouwer and Clemence, 1961). If the eccentricity is small, the following approximate equations may be useful:

$$
{ \begin{array} { r c l } { { \frac { a } { r } } } & { \simeq } & { 1 + e \cos M + \mathrm { h i g h e r ~ o r d e r ~ t e r m s } } \\ { } & { \simeq } & { \cos M + e ( \cos 2 M - 1 ) + \dots } \\ { } & { \sin f } & { \cong } & { \sin M + e \sin 2 M + \dots } \\ { f } & { \cong } & { M + 2 e \sin M + \dots } \\ { } & { \cos E } & { \cong } & { \cos M + { \frac { e } { 2 } } ( \cos 2 M - 1 ) + \dots } \\ { } & { \sin E } & { \cong } & { \sin M + { \frac { e } { 2 } } \sin 2 M + \dots } \\ { } & { \cong } & { M + e \sin M + \dots ~ . } \end{array} }
$$

# 2.2.2 MOTION IN SPACE

The preceding section has described the two-body orbital motion in the plane. The description of the complete three-dimensional motion requires two additional parameters. The angular momentum per unit mass, $\mathbf { h }$ , is

$$
\mathbf { h } = h _ { X } \mathbf { u } _ { X } + h _ { Y } \mathbf { u } _ { Y } + h _ { Z } \mathbf { u } _ { Z }
$$

where $\mathbf { u } _ { X } , \mathbf { u } _ { Y }$ , and $\mathbf { u } _ { Z }$ are unit vectors associated with the $( X , Y , Z )$ axes. Two angles, $i$ and $\Omega$ (see Fig. 2.2.2), can be used to describe the three-dimensional orientation of the orbit plane.

The orbital inclination, $i$ , is the angle between the $Z$ axis and $\mathbf { h }$ . This angle can be determined from

$$
\cos i = { \frac { h _ { Z } } { h } } ,
$$

where $0 \leq i \leq 1 8 0 ^ { \circ }$ and $h = | \mathbf { h } |$ . If the $( X , \ Y )$ axes are in the equator of the planet, then the orbit can be categorized by the inclination, as summarized in Table 2.2.2.

The orbit plane shown in Fig. 2.2.2 intersects the plane containing the $( X , Y )$ axes at the line of nodes. Since the motion is planar, the satellite will move through the line of nodes at the ascending node (AN) where it moves from $- Z$ to $+ Z$ . With the $( X , Y )$ axes in the equatorial plane, the satellite moves from the southern hemisphere to the northern hemisphere when it crosses the ascending node.

Table 2.2.2: Inclination Terminology   

<table><tr><td>i</td><td>Orbit Type</td></tr><tr><td>90°</td><td>Polar</td></tr><tr><td>0≤i&lt;90°</td><td>Posigrade</td></tr><tr><td>90°&lt;i≤180°</td><td>Retrograde</td></tr><tr><td>i=0°</td><td>Posigrade equatorial</td></tr><tr><td>i= 180°</td><td>Retrograde equatorial</td></tr></table>

Similarly, the point where the satellite crosses the line of nodes from $+ Z$ to $- Z$ is referred to as the descending node (DN). The angle, $\Omega$ , that defines the ascending node location is

$$
\begin{array} { l c l } { \sin \Omega } & { = } & { \displaystyle \frac { h _ { X } } { h _ { X Y } } } \\ { \cos \Omega } & { = } & { \displaystyle - \frac { h _ { Y } } { h _ { X Y } } } \end{array}
$$

where $h _ { X Y } = [ h _ { X } ^ { 2 } + h _ { Y } ^ { 2 } ] ^ { 1 / 2 }$ and $0 \leq \Omega \leq 3 6 0 ^ { \circ }$ . Note that both $\sin \Omega$ and $\cos \Omega$ are required to determine the quadrant of $\Omega$ . The specific terminology used for $\Omega$ depends on the $( X , \ Y , \ Z )$ coordinate system. The term right ascension of the ascending node is used in cases where $( X , \ Y , \ Z )$ is a celestial system, but longitude of the ascending node is used in the case of an Earth-fix ed coordinate system.

# 2.2.3 BASIC COORDINATE SYSTEMS

The $( X , Y , Z )$ coordinate system used in the preceding sections has no preferred orientation for the simple description of the two-body motion. Nevertheless, a specific, well-defined orientation of the $( X , \ Y , \ Z )$ axes is required in practice.

Consider the motion of the Earth about the Sun. Since the mass of the Sun is 328,000 times the mass of the Earth, it is quite natural to describe the motion of this system as the motion of the Earth relative to the Sun. But from the description of the two-body motion, there is no requirement that $M _ { 1 }$ be greater than $M _ { 2 }$ or vice versa. The two-body motion of the Earth-Sun system is illustrated in Fig. 2.2.5 from a geocentric point of view. The sphere representing the Earth includes a body-fix ed (Earth-fixed) coordinate system, with the $( x , y )$ axes in the equatorial plane and with the $x$ axis coincident with the intersection of the Greenwich meridian and the equator. The $z$ axis of the Earth-fix ed system coincides with the angular velocity vector of the Earth, $\omega _ { e }$ . The nonrotating $( X ^ { \prime } , Y ^ { \prime } )$ axes lie in the Earth’s equator, but there is no preferred direction for these axes, except the $Z ^ { \prime }$ axis coincides with the angular velocity of the Earth in this model. The Earth-Sun orbit plane intersects the equator at the line of nodes. The point where the Sun moves from the southern hemisphere into the northern hemisphere is the ascending node, denoted by AN in Fig. 2.2.5 from a geocentric viewpoint. Similarly, the descending node is identified by DN.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0001_pages_0001-0070/auto/images/32ff5e19abe63f22d299e174ad6ef53e327c7c8a7d4c9fa3392dcc5a9162818e.jpg)  
Figure 2.2.5: The Earth-Sun two-body motion. For convenience the motion can be described from the geocentric perspective to illustrate the relations between twobody parameters and astronomical conventions. The orbit plane defined by the angular momentum of the two-body system is the ecliptic, the ascending node is the vernal equinox, and the inclination is the obliquity of the ecliptic. The bodies are not drawn to scale since the diameter of the Sun is 100 times the diameter of the Earth. The $( \mathrm { X } ^ { \prime } , \mathrm { Y } ^ { \prime } )$ axes have no preferred orientation, but the $\mathbf { X }$ axis is chosen to coincide with the vernal equinox.

The description given in the preceding paragraph and illustrated in Fig. 2.2.5 contains the essential descriptions of a well-defined and consistent celestial coordinate system. Since the two celestial bodies are modeled as rigid spheres with constant density, the node locations are fix ed in space and the angular velocity vector, $\omega _ { e }$ , of the rotating Earth is constant in magnitude and direction.

Special terms are assigned to the orbit parameters illustrated in Fig. 2.2.5. The orbit plane of the Sun about the Earth (or the Earth about the Sun) is referred to as the ecliptic and the inclination is the obliquity of the ecliptic, usually denoted by $\epsilon \ : ( \simeq 2 3 . 5 ^ { \circ }$ ). The ascending node corresponds to the point known as the vernal equinox and the descending node is the autumnal equinox. The vernal equinox occurs about March 21 and the autumnal equinox occurs about September 21. The location of the Sun when it is $9 0 ^ { \circ }$ from the vernal equinox is the summer solstice and the location at $2 7 0 ^ { \circ }$ is the winter solstice, which occur about June 21 and December 21, respectively. It is somewhat prejudicial that these astronomical locations are identified with northern hemisphere seasons, since association with seasons is reversed in the southern hemisphere. Finally, the angle $\alpha _ { G }$ defines the orientation of the Earth-fix ed coordinate system $( x , y , z )$ with respect to the vernal equinox (i.e., the $x$ axis shown in Fig. 2.2.5). The angle $\alpha _ { G }$ is known as the Greenwich mean sidereal time (GMST), defined by $\alpha _ { G } = \omega _ { e } ( t - t _ { 0 } ) + \alpha _ { G 0 }$ . The period of Earth rotation with respect to a fix ed direction in space is about 86,164 sec $( 2 3 \mathrm { h r } 5 6 \mathrm { m i n } 4 \mathrm { s e c } )$ (i.e., $\omega _ { e } = 2 \pi / 8 6 1 6 4 ~ \mathrm { r a d / s e c } )$ .

With the $X$ axis directed toward the vernal equinox and with both the $z$ and $Z$ axes coincident with the angular velocity vector, $\omega _ { e }$ , it follows that the relations between the nonrotating $( X , Y , Z )$ axes and the Earth-fix ed, rotating $( x , y , z )$ axes as illustrated in Fig. 2.2.5 are

$$
\begin{array} { l c l } { x } & { = } & { X \cos \alpha _ { G } + Y \sin \alpha _ { G } } \\ { y } & { = } & { - X \sin \alpha _ { G } + Y \cos \alpha _ { G } } \\ { z } & { = } & { Z . } \end{array}
$$

For the two-body problem that has been described up to this point, the orientation of the ecliptic defined in a consistent manner with the two-body dynamics will be fix ed in space. Hence, the vernal equinox would be a fix ed direction in space and the obliquity of the ecliptic would also be fix ed. However, as described in Section 2.4, temporal variations exist in the location of the vernal equinox and in $\epsilon$ . With such variations, it is necessary to designate a specific epoch to be assigned to the equinox and obliquity. A commonly used reference is the mean equator and equinox of 2000.0 (the vernal equinox on January 1, 2000, 12 hrs). The system defined for this date is referred to as the J2000 system. In some applications, the M50 system is used, which is defined by the mean equator and equinox of

1950.0. The nonrotating J2000 or M50 systems are sometimes referred to as Earth-centered inertial (ECI) and the Earth-fix ed system $( x , y , z )$ is referred to as Earth-centered, Earth-fix ed (ECF or ECEF or ECF (Earth-centered, fix ed)). We will use the notation J2000 to refer to the system and J2000.0 to refer to the date.

# 2.2.4 ORBIT ELEMENTS AND POSITION/VELOCITY

Assume that an artificial satellite orbits a planet whose mass, $M _ { 1 }$ , is known (i.e., $\mu = G M _ { 1 }$ is known). Assume further that a technique and/or procedure has been utilized to determine the position and velocity of the satellite at a time, $t _ { 0 }$ , in a nonrotating coordinate system. The position and velocity at $t _ { 0 }$ are

$$
\begin{array} { r c l } { \mathbf { r } _ { 0 } } & { = } & { X _ { 0 } \mathbf { u } _ { X } + Y _ { 0 } \mathbf { u } _ { Y } + Z _ { 0 } \mathbf { u } _ { Z } } \\ { \mathbf { V } _ { 0 } } & { = } & { \dot { X } _ { 0 } \mathbf { u } _ { X } + \dot { Y } _ { 0 } \mathbf { u } _ { Y } + \dot { Z } _ { 0 } \mathbf { u } _ { Z } . } \end{array}
$$

The angular momentum, $\mathbf { h }$ , is

$$
\mathbf { h } = h _ { X } \mathbf { u } _ { X } + h _ { Y } \mathbf { u } _ { Y } + h _ { Z } \mathbf { u } _ { Z }
$$

where

$$
\begin{array} { r c l } { { h _ { X } } } & { { = } } & { { Y _ { 0 } \dot { Z } _ { 0 } - \dot { Y } _ { 0 } Z _ { 0 } } } \\ { { h _ { Y } } } & { { = } } & { { Z _ { 0 } \dot { X } _ { 0 } - \dot { Z } _ { 0 } X _ { 0 } } } \\ { { h _ { Z } } } & { { = } } & { { X _ { 0 } \dot { Y } _ { 0 } - \dot { X } _ { 0 } Y _ { 0 } . } } \end{array}
$$

Also,

$$
h ^ { 2 } = \mathbf { h } \cdot \mathbf { h } .
$$

It follows that the inclination $( i )$ and node location $( \Omega )$ can be determined from Eqs. (2.2.28), (2.2.29), (2.2.30), and (2.2.33).

The energy per unit mass can be determined from Eq. (2.2.7),

$$
\xi = \frac { V _ { 0 } ^ { 2 } } { 2 } - \frac { \mu } { r _ { 0 } }
$$

where

$$
V _ { 0 } ^ { 2 } = \mathbf { V } _ { 0 } \cdot \mathbf { V } _ { 0 }
$$

and

$$
r _ { 0 } = \left[ \mathbf { r } _ { 0 } \cdot \mathbf { r } _ { 0 } \right] ^ { 1 / 2 } .
$$

From $\xi$ , the semimajor axis is

$$
a = - \frac { \mu } { 2 \xi } .
$$

The eccentricity of the orbit is determined from Eq. (2.2.14),

$$
e = \left[ 1 + \frac { 2 \xi h ^ { 2 } } { \mu ^ { 2 } } \right] ^ { 1 / 2 } .
$$

The semilatus rectum is given by $p = h ^ { 2 } / \mu$ and the true anomaly is

$$
\begin{array} { l } { \displaystyle \cos f = \frac { 1 } { r _ { 0 } e } [ p - r _ { 0 } ] } \\ { \displaystyle \sin f = \frac { p } { h e } \frac { { \bf r } _ { 0 } \cdot \dot { \bf r _ { 0 } } } { r _ { 0 } } . } \end{array}
$$

The angle $( \omega + f )$ i s

$$
\cos ( \omega + f ) = \frac { X _ { 0 } } { r _ { 0 } } \cos \Omega + \frac { Y _ { 0 } } { r _ { 0 } } \sin \Omega
$$

$$
\sin ( \omega + f ) = \frac { Z _ { 0 } } { r _ { 0 } \sin i }
$$

where both cosine and sine expressions are required to properly determine the quadrant. The argument of perifocus, $\omega$ , can be determined from

$$
\omega = ( \omega + f ) - f .
$$

An alternate determination of the argument of perifocus can be obtained from the eccentricity vector, $\mathbf { e }$ , a vector directed toward perifocus with magnitude equal to the orbit eccentricity. The vector $\mathbf { e }$ is given by

$$
\mathbf { e } = \mathbf { V } _ { 0 } \times { \frac { \mathbf { h } } { \mu } } - { \frac { \mathbf { r } _ { 0 } } { r _ { 0 } } } = e _ { X } \mathbf { u } _ { X } + e _ { Y } \mathbf { u } _ { Y } + e _ { Z } \mathbf { u } _ { Z } .
$$

It can be shown that

$$
\cos \omega = \frac { e _ { X } \cos \Omega + e _ { Y } \sin \Omega } { e }
$$

$$
\sin \omega = \frac { - \cos i \sin \Omega e _ { X } + \cos i \cos \Omega e _ { Y } + \sin i e _ { Z } } { e } .
$$

The eccentric anomaly, $E _ { 0 }$ , can be obtained from

$$
\begin{array} { r } { \cos E _ { 0 } = \frac { r _ { 0 } } { a } \cos f + e } \\ { \sin E _ { 0 } = \frac { r _ { 0 } } { b } \sin f . } \end{array}
$$

Furthermore, the mean anomaly, $M _ { 0 }$ , is given by

$$
M _ { 0 } = E _ { 0 } - e \sin E _ { 0 }
$$

and the time of perifocus passage is

$$
t _ { p } = t _ { 0 } - { \frac { M _ { 0 } } { n } } .
$$

In summary, the position and velocity vectors at $t _ { 0 }$ completely describe the two-body orbit, since they can be converted to an independent set of six orbit elements:

$$
\begin{array} { r } { a } \\ { e } \\ { i } \\ { \Omega } \\ { \omega } \\ { t _ { p } \mathrm { o r } M _ { 0 } . } \end{array}
$$

In other words, the position and velocity completely determine the nature of the two-body orbit, assuming that $\mu$ is known. Similarly, if the orbit elements are given, there are corresponding position and velocity vectors at a specified time.

# Example 2.2.4.1

The ECI position and velocity of a Space Shuttle has been determined to be the following:

$$
{ \begin{array} { l c c c } { X } & { = } & { 5 4 9 2 0 0 0 . 3 4 } & { { \mathrm { m } } } \\ { Y } & { = } & { 3 9 8 4 0 0 1 . 4 0 } & { { \mathrm { m } } } \\ { Z } & { = } & { 2 9 5 5 . 8 1 } & { { \mathrm { m } } } \\ { { \dot { X } } } & { = } & { - 3 9 3 1 . 0 4 6 4 9 1 } & { { \mathrm { m / s e c } } } \\ { { \dot { Y } } } & { = } & { 5 4 9 8 . 6 7 6 9 2 1 } & { { \mathrm { m / s e c } } } \\ { { \dot { Z } } } & { = } & { 3 6 6 5 . 9 8 0 6 9 7 } & { { \mathrm { m / s e c } } } \end{array} }
$$

With $\mu = 3 . 9 8 6 0 0 4 4 \times 1 0 ^ { 1 4 } \mathrm { m ^ { 3 } / s ^ { 2 } }$ and the preceding equations, it follows that the corresponding orbit elements are

Also,

# Example 2.2.4.2

A two-line element (TLE) format is commonly used by NORAD and NASA. An example for NOAA 14 is

NOAA 14

1 23455U 94089A 97229.90474114 .00000115 00000-0 88111-4 0 1530   
2 23455 98.9964 181.3428 0010013 113.9737 246.2483 14.11685823135657

The interpretation of the TLE format is given in Table 2.2.3. Some components of the TLE pertain to the perturbing effects of additional forces, described in Section 2.3. Updated TLE sets can be found on the World Wide Web.

Convert the TLE for NOAA 14 into position and velocity at the epoch contained in the format. From the TLE set, the orbit elements on Day 229.90474114 of 1997 are

It follows that

# 2.2.5 POSITION/VELOCITY PREDICTION

With a specified set of orbit elements, the position and velocity at time $t$ can be determined by solving Kepler’s Equation for eccentric anomaly and determining true anomaly. From the orbit elements and the true anomaly at time $t$ , the position and velocity are

$$
\begin{array} { l c l } { { X } } & { { = } } & { { r \cos f Q _ { 1 1 } + r \sin f Q _ { 1 2 } } } \\ { { Y } } & { { = } } & { { r \cos f Q _ { 2 1 } + r \sin f Q _ { 2 2 } } } \\ { { Z } } & { { = } } & { { r \cos f Q _ { 3 1 } + r \sin f Q _ { 3 2 } } } \\ { { \dot { X } } } & { { = } } & { { \dot { X } ^ { \ast } Q _ { 1 1 } + \dot { Y } ^ { \ast } Q _ { 1 2 } } } \\ { { \dot { Y } } } & { { = } } & { { \dot { X } ^ { \ast } Q _ { 2 1 } + \dot { Y } ^ { \ast } Q _ { 2 2 } } } \\ { { \dot { Z } } } & { { = } } & { { \dot { X } ^ { \ast } Q _ { 3 1 } + \dot { Y } ^ { \ast } Q _ { 3 2 } } } \end{array}
$$

Table 2.2.3: NORAD/NASA TWO-LINE ELEMENTS (TLE)   

<table><tr><td rowspan=1 colspan=2>Line 1</td></tr><tr><td rowspan=1 colspan=1>Column</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>01-01</td><td rowspan=1 colspan=1>Line Number of Element Data</td></tr><tr><td rowspan=1 colspan=1>03-07</td><td rowspan=1 colspan=1>Satellite Number</td></tr><tr><td rowspan=1 colspan=1>10-11</td><td rowspan=1 colspan=1>International Designator (Last two digits of launch year)</td></tr><tr><td rowspan=1 colspan=1>12-14</td><td rowspan=1 colspan=1>International Designator (Launch number of the year)</td></tr><tr><td rowspan=1 colspan=1>15-17</td><td rowspan=1 colspan=1>International Designator (Component of launch)</td></tr><tr><td rowspan=1 colspan=1>19-20</td><td rowspan=1 colspan=1>Epoch Year (Last two digits of year)</td></tr><tr><td rowspan=1 colspan=1>21-32</td><td rowspan=1 colspan=1>Epoch (Day of year and fractional portion of the day)</td></tr><tr><td rowspan=1 colspan=1>34-43</td><td rowspan=1 colspan=1>First Time Derivative of the Mean Motion or Ballistic Coeffcient</td></tr><tr><td rowspan=1 colspan=1>45-52</td><td rowspan=1 colspan=1>Second Time Derivative of Mean Motion (decimal point assumed)</td></tr><tr><td rowspan=1 colspan=1>54-61</td><td rowspan=1 colspan=1>Drag term or radiation pressure coeffcient (decimal point assumed)</td></tr><tr><td rowspan=1 colspan=1>63-63</td><td rowspan=1 colspan=1>Ephemeris type</td></tr><tr><td rowspan=1 colspan=1>65-68</td><td rowspan=1 colspan=1>Element number</td></tr><tr><td rowspan=1 colspan=1>69-69</td><td rowspan=1 colspan=1>Check sum (Modulo 10)</td></tr><tr><td rowspan=1 colspan=2>Line 2</td></tr><tr><td rowspan=1 colspan=1>Column</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>01-01</td><td rowspan=1 colspan=1>Line Number of Element Data</td></tr><tr><td rowspan=1 colspan=1>03-07</td><td rowspan=1 colspan=1>Satellite Number</td></tr><tr><td rowspan=1 colspan=1>09-16</td><td rowspan=1 colspan=1>Inclination [Degrees]</td></tr><tr><td rowspan=1 colspan=1>18-25</td><td rowspan=1 colspan=1>Right Ascension of the Ascending Node [Degrees]</td></tr><tr><td rowspan=1 colspan=1>27-33</td><td rowspan=1 colspan=1>Eccentricity (decimal point assumed)</td></tr><tr><td rowspan=1 colspan=1>35-42</td><td rowspan=1 colspan=1>Argument of Perigee [Degrees]</td></tr><tr><td rowspan=1 colspan=1>44-51</td><td rowspan=1 colspan=1>Mean Anomaly [Degrees]</td></tr><tr><td rowspan=1 colspan=1>53-63</td><td rowspan=1 colspan=1>Mean Motion [Revs per day]</td></tr><tr><td rowspan=1 colspan=1>64-68</td><td rowspan=1 colspan=1>Revolution number at epoch [Revs]</td></tr><tr><td rowspan=1 colspan=1>69-69</td><td rowspan=1 colspan=1>Check Sum (Modulo 10)</td></tr></table>

where

$$
\begin{array} { r c l } { \dot { X } ^ { * } } & { = } & { V _ { \mathrm { r } } \cos f - V _ { \mathrm { r } } \sin f } \\ { \dot { Y } ^ { * } } & { = } & { V _ { \mathrm { r } } \sin f + V _ { \mathrm { t } } \cos f } \\ { V _ { \mathrm { r } } } & { = } & { \dot { r } - \frac { \hbar c } { 9 } \sin f } \\ { V _ { \mathrm { \theta } } } & { = } & { \frac { \hbar } { r } } \\ { Q _ { 1 1 } } & { = } & { \cos \omega \cos \Omega - \sin \omega \sin \Omega \cos i } \\ { Q _ { 2 1 } } & { = } & { - \sin \omega \cos \Omega - \cos \omega \sin \Omega \cos i } \\ { Q _ { 2 1 } } & { = } & { \cos \omega \sin \Omega + \sin \omega \cos \Omega \cos i } \\ { Q _ { 2 2 } } & { = } & { - \sin \omega \sin \Omega + \cos \omega \cos \Omega \cos i } \\ { Q _ { 3 1 } } & { = } & { \sin \omega \sin i } \\ { Q _ { 2 3 } } & { = } & { \cos \omega \cos \sin i . } \end{array}
$$

# Example 2.2.5

The position and velocity of the Space Shuttle at a later time can be determined from the state given in Example 2.2.4.1. For example, at 30 minutes after the epoch used in Example 2.2.4.1, the eccentric anomaly is $1 5 9 . 6 2 8 1 3 8 ^ { \circ }$ . It follows that the position and velocity at 30 minutes is

An example of an ephemeris of positions, or table of positions, for the interval $3 0 \mathrm { { m i n } }$ to $3 4 \mathrm { m i n }$ is

<table><tr><td>t (min)</td><td>X (m)</td><td>Y (m)</td><td>Z (m)</td></tr><tr><td>30</td><td>-5579681.52</td><td>2729244.60</td><td>2973901.72</td></tr><tr><td>32</td><td>-5999982.83</td><td>1951421.98</td><td>2765929.81</td></tr><tr><td>34</td><td>-6315097.41</td><td>1139386.52</td><td>2509466.97</td></tr></table>

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0001_pages_0001-0070/auto/images/fc0f4897c47db6de47254e55f2eb62724f69d62afe8c8cfee1bbd49c9bdd44f4.jpg)  
Figure 2.2.6: Shuttle ground track: the latitude-longitude ephemeris of Example 2.2.4.1. The latitude-longitude ephemeris is overlaid on a global map to illustrate the ground track of the satellite.

In some applications, the ephemeris is expressed in the body-fix ed coordinate system. The transformation is given by Eq. (2.2.31), in which

$$
\alpha _ { G } = \omega _ { e } ( t - t _ { 0 } ) + \alpha _ { G 0 } .
$$

Assuming $t _ { 0 } = 0$ and $\alpha _ { G 0 } = 0$ , it follows that the preceding ephemeris expressed in ECF coordinates is:

<table><tr><td>t (min)</td><td>x (m)</td><td>y(m)</td><td>z (m)</td></tr><tr><td>30</td><td>-5174477.07</td><td>3436045.54</td><td>2973901.72</td></tr><tr><td>32</td><td>-5668947.18</td><td>2769635.28</td><td>2765929.81</td></tr><tr><td>34</td><td>-6076481.79</td><td>2062771.41</td><td>2509466.97</td></tr></table>

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0001_pages_0001-0070/auto/images/5e026e00fddadc3c96caab525dbd0d02f009a1f8b71cdbce65a404cc5dbbf682.jpg)  
Figure 2.2.7: Definition of geocentric latitude $( \phi )$ and longitude $( \lambda )$ .

For other applications, these coordinates are further transformed into geocentric latitude $( \phi )$ and longitude $( \lambda )$ , illustrated in Fig. 2.2.7 and defined by

$$
\begin{array} { l c l } { x } & { = } & { r \cos \phi \cos \lambda } \\ { y } & { = } & { r \cos \phi \sin \lambda } \\ { z } & { = } & { r \sin \phi } \end{array}
$$

or

$$
\begin{array} { l l } { \sin \phi = \displaystyle \frac { z } { r } } & { - 9 0 ^ { \circ } \leq \phi \leq 9 0 ^ { \circ } } \\ { \cos \lambda = \displaystyle \frac { x } { r \cos \phi } } & \\ { \sin \lambda = \displaystyle \frac { y } { r \cos \phi } } & { 0 \leq \lambda \leq 3 6 0 ^ { \circ } . } \end{array}
$$

The altitude, $h$ , is obtained from $h = r - r _ { e }$ , where $r _ { e }$ is the Earth radius. The geocentric latitude, longitude, and height ephemeris derived from the preceding ECF ephemeris for the interval is:

<table><tr><td>t(min)</td><td>(deg)</td><td>入(deg)</td><td>h(m)</td></tr><tr><td>30</td><td>25.584</td><td>146.414</td><td>508495.95</td></tr><tr><td>32</td><td>23.672</td><td>153.962</td><td>510854.90</td></tr><tr><td>34</td><td>21.359</td><td>161.249</td><td>512151.92</td></tr></table>

Here, it has been assumed that the Earth is spherical with radius $6 3 7 8 1 3 7 \mathrm { m }$ . The latitude/longitude ephemeris can be plotted on a global or regional map to illustrate the path of the subsatellite point; that is, the point where the position vector of the satellite pierces the Earth’s surface. The subsatellite locus of points produces a ground track. The ephemeris generated by the position and velocity in Example 2.2.4.1 for two orbital revolutions is illustrated in Fig. 2.2.6.

It is evident from Fig. 2.2.6 that, although $\Omega$ is constant, the longitude of the point where the satellite crosses the equator in a northward direction is not constant. The change in the longitude of the ascending node is caused solely by the rotation of the Earth in the two-body problem, but other factors contribute as well to the actual motion, as described in Section 2.3.

# 2.2.6 STATE TRANSITION MATRIX AND ERROR PROPAGA-TION

The initial state for a particular problem, such as the example state vectors in the Section 2.2.4 examples, can be expected to be in error at some level. If the error in position, for example, is $\Delta \mathbf { r } ( t _ { 0 } )$ , this error will produce an error $\Delta \mathbf { r } ( t )$ at a later time $t$ , as well as an error in velocity, $\Delta \dot { \mathbf { r } } ( t )$ . The propagation of the error at $t _ { 0 }$ to an error at $t$ can be approximately expressed by

$$
[ \begin{array} { c } { \Delta X } \\ { \Delta Y } \\ { \Delta Z } \\ { \Delta \dot { X } } \\ { \Delta \dot { X } } \\ { \Delta \dot { Y } } \\ { \Delta \dot { X } } \\ { \Delta \dot { Z } } \end{array} ] = [ \begin{array} { c c c c c c c } { \frac { \partial X } { \partial X _ { 0 } } } & { \frac { \partial X } { \partial Y _ { 0 } } } & { \frac { \partial X } { \partial Z _ { 0 } } } & { \frac { \partial X } { \partial X _ { 0 } } } & { \frac { \partial X } { \partial Y _ { 0 } } } & { \frac { \partial X } { \partial Z _ { 0 } } } \\ { \frac { \partial Y } { \partial X _ { 0 } } } & { \frac { \partial Y } { \partial Y _ { 0 } } } & { \frac { \partial Y } { \partial Z _ { 0 } } } & { \frac { \partial Y } { \partial X _ { 0 } } } & { \frac { \partial Y } { \partial Y _ { 0 } } } & { \frac { \partial Y } { \partial Z _ { 0 } } } \\ { \frac { \partial Z } { \partial X _ { 0 } } } & { \frac { \partial Z } { \partial Y _ { 0 } } } & { \frac { \partial Z } { \partial Z _ { 0 } } } & { \frac { \partial Z } { \partial X _ { 0 } } } & { \frac { \partial Z } { \partial Y _ { 0 } } } & { \frac { \partial Z } { \partial Z _ { 0 } } } \\ { \frac { \partial \dot { X } } { \partial X _ { 0 } } } & { \frac { \partial \dot { X } } { \partial Y _ { 0 } } } & { \frac { \partial \dot { X } } { \partial Z _ { 0 } } } & { \frac { \partial \dot { X } } { \partial X _ { 0 } } } & { \frac { \partial \dot { X } } { \partial Y _ { 0 } } } & { \frac { \partial \dot { X } } { \partial Z _ { 0 } } } \\ { \frac { \partial \dot { Y } } { \partial X _ { 0 } } } & { \frac { \partial \dot { Y } } { \partial Y _ { 0 } } } & { \frac { \partial \dot { Y } } { \partial Z _ { 0 } } } & { \frac { \partial \dot { Y } } { \partial X _ { 0 } } } & { \frac { \partial \dot { Y } } { \partial Y _ { 0 } } } & { \frac { \partial \dot { Y } } { \partial Z _ { 0 } } } \\ { \frac { \partial \dot { Z } } { \partial X _ { 0 } } } & { \frac { \partial \dot { Z } } { \partial Y _ { 0 } } } &  \frac { \partial \dot { Z } }  \partial Z _  \end{array}
$$

where the matrix of partial derivatives is referred to as the state transition matrix, also known as the matrizant. Although they are complicated, expressions for the partial derivatives, such as $\frac { \partial X } { \partial X _ { 0 } }$ , can be formed for the problem of two bodies (e.g., Goodyear, 1965). A general approach to the generation of the state transition matrix is given in Chapter 4. The origin of Eq. (2.2.38) can readily be seen by noting that a differential change in $X$ at time $t$ is related to differential changes in position and velocity at $t _ { 0 }$ by

$$
\begin{array} { r } { d X = \cfrac { \partial X } { \partial X _ { 0 } } d X _ { 0 } + \cfrac { \partial X } { \partial Y _ { 0 } } d Y _ { 0 } + \cfrac { \partial X } { \partial Z _ { 0 } } d Z _ { 0 } + \cfrac { \partial X } { \partial \dot { X } _ { 0 } } d \dot { X } _ { 0 } } \\ { + \cfrac { \partial X } { \partial \dot { Y } _ { 0 } } d \dot { Y } _ { 0 } + \cfrac { \partial X } { \partial \dot { Z } _ { 0 } } d \dot { Z } _ { 0 } . } \end{array}
$$

For fini te changes, let $\Delta X$ replace $d X$ , $\Delta X _ { 0 }$ replace $d X _ { 0 }$ , and so on; then Eq.   
(2.2.38) becomes the equation produced by Eq. (2.2.39) for $\Delta X$ .

# Example 2.2.6.1

Assuming an initial error in Example 2.2.4.1 given by

$$
\begin{array} { r l } { \Delta X _ { 0 } = } & { { } ~ 1 \mathrm { m } } \\ { \Delta Y _ { 0 } = } & { { } ~ 2 \mathrm { m } } \\ { \Delta Z _ { 0 } = } & { { } ~ 3 \mathrm { m } } \\ { \Delta \dot { X } _ { 0 } = } & { { } ~ 0 } \\ { \Delta \dot { Y } _ { 0 } = } & { { } ~ 0 } \\ { \Delta \dot { Z } _ { 0 } = } & { { } ~ 0 , } \end{array}
$$

the Goodyear (1965) formulation of the state transition matrix can be used to map this error to $3 0 \mathrm { { m i n } }$ , which produces

$$
\begin{array} { r l } { \Delta X = } & { { } \quad 0 . 6 5 \mathrm { m } } \\ { \Delta Y = } & { { } \quad 1 3 . 7 7 \mathrm { m } } \\ { \Delta Z = } & { { } \quad 4 . 7 8 \mathrm { m } } \\ { \Delta \dot { X } = } & { { } \quad - 0 . 0 0 9 9 5 3 \mathrm { m } / \mathrm { s } } \\ { \Delta \dot { Y } = } & { { } \quad 0 . 0 1 1 4 2 1 \mathrm { m } / \mathrm { s } } \\ { \Delta \dot { Z } = } & { { } \quad 0 . 0 0 5 7 1 8 \mathrm { m } / \mathrm { s } } \end{array}
$$

Note that the error at $t _ { 0 }$ propagated to $3 0 \mathrm { { m i n } }$ can also be obtained by adding the above initial error to the state, which results in

$$
\begin{array} { r l r } { X } & { = } & { 5 4 9 2 0 0 1 . 3 4 \mathrm { m } } \\ { Y } & { = } & { 3 9 8 4 0 0 3 . 4 0 \mathrm { m } } \\ { Z } & { = } & { 2 9 5 8 . 8 1 \mathrm { m } } \end{array}
$$

and no change in velocity. Following the procedure in Section 2.2.5, the predicted state at 1800 sec is

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0001_pages_0001-0070/auto/images/3b03b614718a527e4050fcc84c6f6777e96e54ce625155141d39de78af68d3c8.jpg)  
Figure 2.2.8: The RTN system: Radial (R), Transverse (T), and Normal (N).

Differencing this state with the predicted state in Section 2.2.5 produces the same error components obtained with the state transition matrix mapping. Since the differences are small in comparison to the total position magnitudes, the differential displacements in Eq. (2.2.38) are accurately approximated by the actual displacements. This aspect is discussed in Chapter 4 within the context of linear approximations.

For most applications, use of the $( X Y Z )$ coordinates to express the error is less revealing than other coordinate systems. An alternate system is shown in Fig. 2.2.8, in which unit vectors are defined in the radial (R) direction, transverse (T) direction, and normal $( \mathrm { N } )$ direction, referred to as the RTN system. To avoid ambiguity, these directions are specified by unit vectors $\mathbf { u } _ { r } , \mathbf { u } _ { t }$ , and $\mathbf { u } _ { n }$ , which are defined by

$$
\begin{array} { r } { \mathbf { r } = r \mathbf { u } _ { r } } \\ { \mathbf { h } = h \mathbf { u } _ { n } } \end{array}
$$

and $\mathbf { u } _ { t }$ completes the right-handed, orthogonal system.

A commonly used terminology for the RTN directions is: $\mathbf { u } _ { t }$ may be referred to as the along-track direction and $\mathbf { u } _ { n }$ may be referred to as the cross-track direc-

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0001_pages_0001-0070/auto/images/62346d359fa6e105541bee0b296314d1fd65b43c4f4a3b2d1d3eba449da1428d.jpg)  
Figure 2.2.9: Orbit error evolution in RTN directions. A radial perturbation of 1 meter at $t = 0$ was applied to the state vector in Example 2.2.4.1. The plot illustrates the $1 { - } \mathrm { m }$ radially perturbed orbit minus the unperturbed orbit (Example 2.2.4.1).

tion. In some definitions, the along-track direction may refer to the direction of the velocity vector, which coincides with the $\mathbf { u } _ { t }$ direction at every point only on a circular orbit. The ECI to RTN transformation is given by Eq. (4.16.21).

# Example 2.2.6.2

To illustrate the nature of the orbit error, Fig. 2.2.9 shows the evolution of orbit error for two orbital revolutions resulting from a 1-meter error in the radial direction for the Shuttle described in Example 2.2.4.1. The 1-meter error in the radial component (increase in radial component) at the initial time produces the perturbed position of

$$
\begin{array} { r l r } { X = } & { { } } & { 5 4 9 2 0 0 1 . 1 4 9 4 5 \mathrm { m } } \\ { Y = } & { { } } & { 3 9 8 4 0 0 1 . 9 8 7 1 9 \mathrm { m } } \\ { Z = } & { { } } & { 2 9 5 5 . 8 1 0 4 4 \mathrm { m } } \end{array}
$$

and no change in velocity. Figure 2.2.9 shows the evolution of this 1-meter radial error in (RTN)-components, where the components are defined as the perturbed orbit position minus the reference orbit defined by the state vector in Example 2.2.4.1. With $\mathbf { u } _ { t }$ defined by the reference orbit, the position on the perturbed orbit is about $- 4 0 \mathrm { ~ m ~ } \mathbf { u } _ { t }$ at $1 1 , 0 0 0 ~ \mathrm { s e c }$ ; that is, it “trails” the reference orbit by about $4 0 \mathrm { m }$ at this time. Since there is no out-of-plane perturbation of either position or velocity, the normal component is zero. Two significant characteristics are evident in the radial and transverse components. The transverse component exhibits a somewhat linear growth with time, or secular change. Furthermore, the existence of a periodic variation coinciding with the orbit period is evident in the radial and transverse components. This periodic variation is usually identified as a once per revolution variation. A more complete discussion is given by El´Yasberg (1967).

Further consideration of Fig. 2.2.9 explains the sign and periodicity in this figure. The increase in $r$ with no change in initial velocity results in an increase in semimajor axis and an increase in orbital period. With the difference in orbital period, a satellite in the unperturbed orbit must move ahead of a satellite in the perturbed orbit. Since the transverse component is defined as perturbed minus unperturbed, the component will be negative. It appears linear because of the linear dependence in time exhibited by Kepler’s Equation. The explanation of the periodic variation in this characteristic results from the difference in semimajor axis and eccentricity of the two orbits, which produces terms that are dependent on eccentric anomaly.

# 2.3 PERTURBED MOTION

The description of motion given in Section 2.2 is idealized. It has been obtained by assuming that only gravitational forces exist between two bodies, both of which have been further idealized by assuming them to be spheres that are gravitationally equivalent to point masses. The idealizations enable an analytical solution to the equations of motion and the motion can be interpreted as a simple geometrical figure (circle, ellipse, parabola, hyperbola). Because of the simple geometrical interpretation of the orbit, the idealized problem of two bodies provides a starting point for the interpretation of more realistic representations of the orbital motion.

Newton was well aware of the complexities surrounding the equations of motion that better represent the real world. He considered the gravitational problem of three bodies representing the Earth, Moon, and Sun, but he reportedly told his friend, the Royal Astronomer Halley, that the motion of the Moon “ma de his head ache and kept him awake so often that he would think of it no more” (Moulton, p. 363, 1914). The lunar problem (or the three-body problem) has no general, closed-form solution analogous to the conic section solution for the problem of two bodies (except for equilibrium solutions), but there are various ways of forming approximate solutions. Approximate analytical solutions use the problem of two bodies as a reference solution and expressions can be derived for the deviation, or perturbation, resulting from additional forces. These additional forces, that is, forces in addition to the point mass gravitation between two bodies, are referred to as perturbing forces. The analytical techniques used to obtain the approximate solutions are known as general perturbations.

With the advent of increasingly powerful digital computers, techniques that provide a numerical solution to the perturbed equations of motion have received increased attention as well. In these techniques, the equations of perturbed motion, represented by a set of ordinary differential equations, are solved numerically with specified initial conditions. These techniques are known as special perturbations. The procedures applied to the numerical integration of the equations of motion are described in most books on numerical analysis, but references such as Press et al. (1986) and Shampine and Gordon (1975) are good sources of applied information.

In the following sections, the contributions of various perturbing forces are summarized. These forces are separated into two categories: gravitational and nongravitational. The influenc e of these perturbing forces on the orbit is described in these sections.

# 2.3.1 CLASSICAL EXAMPLE: LUNAR PROBLEM

In spite of the notorious difficulty in solving the equations that describe the motion of the Moon, the problem can readily be solved by numerical integration. The results of the integration are instructive in describing the nature of perturbed motion and, additionally, the results are applicable to a further discussion of astronomical coordinate systems.

Following the approach used in the derivation of the equations of motion of two spheres given in Section 2.2, the equations of motion for three bodies that attract each other in accordance with Newtonian gravity can be derived in a similar manner. Let $M _ { 1 }$ , $M _ { 2 }$ , and $M _ { 3 }$ represent the masses of three spheres, each with constant and uniform density. The equations of motion for each body can be expressed using an inertial coordinate system. But it is useful (and instructive) to describe the motion of two of the bodies with respect to the third body, say $M _ { 1 }$ . The resulting equations of motion for $M _ { 2 }$ and $M _ { 3 }$ are as follows, where the

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0001_pages_0001-0070/auto/images/00f0ea176bb7b469d32d038725b0196b0854439649d4ed9ee0400eb911d7dd06.jpg)  
Figure 2.3.1: Vector definition for three bodies.

vectors are illustrated in Fig. 2.3.1:

$$
\begin{array} { r c l } { \displaystyle \ddot { \mathbf { r } } } & { = } & { \displaystyle - \frac { \mu \mathbf { r } } { r ^ { 3 } } + G M _ { 3 } \left( \frac { \Delta } { \Delta ^ { 3 } } - \frac { \mathbf { r } _ { p } } { r _ { p } ^ { 3 } } \right) } \\ { \displaystyle \ddot { \mathbf { r } } _ { p } } & { = } & { \displaystyle - \frac { \mu ^ { \prime } \mathbf { r } _ { p } } { r _ { p } ^ { 3 } } - G M _ { 2 } \left( \frac { \mathbf { r } } { r ^ { 3 } } + \frac { \Delta } { \Delta ^ { 3 } } \right) } \end{array}
$$

where $\mu = G ( M _ { 1 } + M _ { 2 } )$ and $\mu ^ { \prime } = G ( M _ { 1 } + M _ { 3 } )$ .

Let the bodies represent the Earth, Moon, and Sun, so that $M _ { 1 }$ is the Earth’s mass, $M _ { 2 }$ is the mass of the Moon, and $M _ { 3 }$ represents the Sun. This description is known as the problem of three bodies in celestial mechanics. The vector $\mathbf { r }$ represents the position vector of the Moon with respect to the Earth, $\pmb { \Delta }$ is the position vector of the Sun with respect to the Moon, and $\mathbf { r } _ { p }$ is the position vector of the Sun with respect to the Earth. Examination of the gravitational parameters of the Earth, Moon, and Sun as given in Appendix D shows that the mass of the Sun is more than 300,000 times greater than the Earth and the mass of the Moon is 81 times smaller than the Earth. An accurate approximation can be made in Eq. (2.3.2) by ignoring both the term with $G M _ { 2 }$ and $M _ { 1 }$ in $\mu ^ { \prime }$ . With these approximations, the motion of the Sun about the Earth (or vice versa) is described by two-body dynamics. This approximation is known as the restricted problem of three bodies, described in more detail by Szebehely (1967).

Equations (2.3.1) and (2.3.2) can be integrated using a numerical method (e.g., see Shampine and Gordon, 1975) with specified initial conditions. Since the Sun is a dominant perturbation of the lunar motion, it is more appropriate to use a different orientation of the $( X , Y , Z )$ axes. In this orientation, the $Z$ axis is perpendicular to the ecliptic instead of the equator (as defined in Section 2.2.3), but the $X$ axis is still directed to the vernal equinox. If the initial conditions in Table 2.3.1 are adopted, along with the mass parameters from Appendix D, the numerical integration of the equations for the Moon will produce an ephemeris, a table of time, position, and velocity. If the position and velocity vectors at each time are converted into orbit elements, referred to as osculating elements, using the equations in Section 2.2.4, the lunar inclination is illustrated in Fig. 2.3.2. The variation in the lunar ascending node is shown in Fig. 2.3.3 with respect to the vernal equinox over a period of one year. It is clearly evident from these figures that the orbit elements are not constant, which is the result of the influence of the gravitational perturbation of the Sun on the two bodies: Earth and Moon.

Table 2.3.1: Ecliptic Position and Velocity of Sun and Moon on January 1, 2000, 12 Hours   

<table><tr><td colspan="3">MOON</td></tr><tr><td>X=</td><td>-291608 km</td><td>X= 0.643531 km/sec</td></tr><tr><td>Y=</td><td>-274979 km</td><td>Y= -0.730984 km/sec</td></tr><tr><td>Z=</td><td>36271 km</td><td>2= -0.011506 km/sec</td></tr><tr><td colspan="3">SUN</td></tr><tr><td>X=</td><td>26499000 km</td><td>X= 29.794 km/sec</td></tr><tr><td>Y=</td><td>Y= -144697300 km</td><td>5.469 km/sec</td></tr><tr><td>Z=</td><td>0 km Z=</td><td>0 km/sec</td></tr></table>

Figures 2.3.2 and 2.3.3 exhibit some important features of perturbed motion. The ascending node location in Fig. 2.3.3 exhibits a linear variation with time, referred to as a secular variation, as well as periodic variations. The inclination also shows periodic variations, but no apparent secular variation. Close examination of the periodic variations show the existence of approximately 180-day and 14-day periods, half the orbital period of the Sun about the Earth, and half the orbital period of the Moon, respectively. These periods appear in the plot for the node as well, but the 14-day periods are less evident. The secular node rate is negative, thus the change is referred to as a regression of the node, with a rate of about 19.4 degrees per year. The line of nodes of the Moon’s orbit completes one revolution in 18.6 years, a fundamental period in the lunar motion that has been known since antiquity. Although less evident, other periodicities exist in the orbit element variations, including 28 days and 365 days, but the amplitudes of these terms are smaller and their effects are less evident in Figs. 2.3.2 and 2.3.3.

This example illustrates the influence that a perturbing force may have. An orbit element may exhibit secular variations, but it will also show periodic variations. The orbit elements that exhibit secular variations depend on the nature of the perturbing force, as do the specific periods associated with the periodic variations. The periodic variations are often loosely categorized as short-period perturbations or long-period perturbations. Depending on the nature of the perturbing forces, other periodicities may exist that do not fit these two categories, so other categories may be introduced to accommodate them. Furthermore, the period of a perturbation is not a definit ive statement regarding how a perturbation should be categorized. For example, “short period” usually refers to perturbations in the frequency spectrum that are integer or near-integer multiples of the mean orbital angular rate. There are usually several specific frequencies that are categorized as short-period, but all are near the mean orbital angular rate.

# 2.3.2 VARIATION OF PARAMETERS

As illustrated in the previous section, the influence of a perturbing force on an orbit can be illustrated through time variations of the elements. The temporal variations illustrated for the Moon suggest the development of differential equations for the elements, analogous to the process known as variation of parameters in the solution of ordinary differential equations. The differential equations of motion for the perturbed satellite problem can be expressed as

$$
{ \ddot { \mathbf { r } } } = - { \frac { \mu \mathbf { r } } { r ^ { 3 } } } + \mathbf { f } ,
$$

where $\mathbf { r }$ is the position vector of the satellite center of mass expressed in an appropriate reference frame and $\mathbf { f }$ is the perturbing force. The perturbing force f , or more correctly, the force per unit mass since f has acceleration units, can be further resolved into components in the RTN system (see Section 2.2.6),

$$
\mathbf { f } = { \hat { R } } \mathbf { u } _ { r } + { \hat { T } } \mathbf { u } _ { t } + { \hat { N } } \mathbf { u } _ { n }
$$

where the unit vectors are defined by the RTN directions and $\hat { R } , \hat { T } , \hat { N }$ represent the force components. Note in Eq. (2.3.3) that if $\mathbf { f } = 0$ , the resulting motion is two-body. Thus, f perturbs the two-body motion.

It can be shown that the equations of motion given by Eq. (2.3.3) can be equivalently expressed by a set of differential equations that describes the time rate of change of the orbit elements (Appendix D). For example, the rates of change of the node and inclination are

$$
\frac { d \Omega } { d t } = \frac { r \sin ( \omega + f ) \hat { N } } { h \sin i }
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0001_pages_0001-0070/auto/images/b874e4de784ca82d5bce8918cd49cafdeeef5f3cf33948cd386ef3c3c53b9ed5.jpg)  
Figure 2.3.2: Time variation of the lunar inclination with respect to the ecliptic. Epoch: January 1, 2000, 12 hours.

$$
\frac { d i } { d t } = \frac { r \cos ( \omega + f ) { \hat { N } } } { h } .
$$

The solutions to the full set of equations give the six orbit elements as a function of time, from which position and velocity can be obtained from the equations in Section 2.2.4.

In some cases, the perturbing force, f , is derivable from a potential or disturbing function, $D$ . The equations for time variation of the orbit elements can be also expressed as a function of $D$ , as given in Appendix C. For example, the node and inclination are

$$
\begin{array} { r c l } { { \displaystyle \frac { d \Omega } { d t } } } & { { = } } & { { \displaystyle \frac { 1 } { h \sin i } \frac { \partial D } { \partial i } } } \\ { { \displaystyle \frac { d i } { d t } } } & { { = } } & { { \displaystyle \frac { 1 } { h \sin i } \left[ \cos i \frac { \partial D } { \partial \omega } - \frac { \partial D } { \partial \Omega } \right] . } } \end{array}
$$

The equations given by Eqs. (2.3.3), (2.3.5), and (2.3.6) are equivalent. That is, aside from errors introduced by the respective technique used to solve these equations, the solutions of the equations are identical for the same perturbing forces. Equation (2.3.6) is particularly useful in gaining insight into the nature of perturbed motion, whereas Eq. (2.3.3) is most often used for applications requiring high accuracy in the representation of f.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0001_pages_0001-0070/auto/images/2745a615caf879975fbd164112807f7f170357748b956f9277b93ec7bf313c18.jpg)  
Figure 2.3.3: Time variation of the lunar node measured in the ecliptic. Epoch: January 1, 2000, 12 hours.

The perturbing force f in Eq. (2.3.3) can be categorized into two types of forces: gravitational and nongravitational. In the following sections, various sources that contribute to f are described.

# 2.3.3 GRAVITATIONAL PERTURBATIONS: MASS DISTRIBUTION

Consider the gravitational attraction between two point masses, $M _ { 1 }$ and $M _ { 2 }$ , separated by a distance $r$ . The gravitational potential between these two bodies, $U$ , can be expressed as

$$
U = { \frac { G M _ { 1 } M _ { 2 } } { r } } .
$$

The gravitational force on $M _ { 2 }$ resulting from the interaction with $M _ { 1 }$ can be derived from the potential as the gradient of $U$ ; that is,

$$
\mathbf { F } = \boldsymbol { \nabla } U = - { \frac { G M _ { 1 } M _ { 2 } \mathbf { r } } { r ^ { 3 } } }
$$

where $\mathbf { r }$ is the position vector of $M _ { 2 }$ with respect to $M _ { 1 }$ given by

$$
\mathbf { r } = x \mathbf { u } _ { x } + y \mathbf { u } _ { y } + z \mathbf { u } _ { z }
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0001_pages_0001-0070/auto/images/7939f2a788285f2ed9c366d731c208facd4dcadc12d57cc82b33cc55b749acea.jpg)  
Figure 2.3.4: Definit ion of position vectors and differential mass for a body with arbitrary mass distribution.

and

$$
\nabla = \frac { \partial } { \partial x } { \mathbf u } _ { x } + \frac { \partial } { \partial y } { \mathbf u } _ { y } + \frac { \partial } { \partial z } { \mathbf u } _ { z } .
$$

If a body of total mass $M$ has an arbitrary distribution of mass, it can be modeled as the collection of a large number of point masses. The gravitational potential sensed by a point mass, $m ^ { \prime }$ , at an external location is

$$
U = m ^ { \prime } \int \int \int { \frac { G \gamma d x d y d z } { \rho } }
$$

where $\gamma$ is the mass density associated with an element of mass dm, dx dy $d z$ is the differential volume, and $\rho$ is the distance between the differential mass dm and the external mass $m ^ { \prime }$ (see Fig. 2.3.4). For convenience, the external mass is usually taken to be unity $( m ^ { \prime } = 1 \mathrm { ~ \AA ~ }$ ), and the integral expression is written in a more compact notation

$$
U = \int _ { M } { \frac { G d m } { \rho } }
$$

where the integral notation represents integration over the entire mass of the body. Equation (2.3.10) can be directly integrated for some bodies, such as a sphere of constant density $\gamma$ . This integration (see Danby, 1988) shows that the constant density sphere is gravitationally equivalent to a point mass.

The position vector of $m ^ { \prime }$ with respect to the coordinate system $( x , y , z )$ is $\mathbf { r }$ . The location of the origin, $O$ , and the orientation of $( x , y , z )$ is arbitrary; however, for convenience, the $( x , y , z )$ system is assumed to be body-fixed. Hence, the $( x , y , z )$ axes are fix ed in the body and rotate with it. For the Earth, as an example, the $( x , y )$ plane would coincide with the equator, with the $x$ axis also coinciding with the Greenwich meridian.

Equation (2.3.10) can be expanded into the infinite series

$$
U = \frac { G } { r } \int _ { M } \sum _ { \ell = 0 } ^ { \infty } \left( \frac { R } { r } \right) ^ { \ell } P _ { \ell } ( \cos S ) d m
$$

where $R$ is the distance between the origin $O$ and the differential mass $d m$ , and $P _ { \ell }$ is the Legendre polynomial of degree $\ell$ , with argument equal to the cosine of the angle between the two vectors, $\mathbf { R }$ and $\mathbf { r }$ . Using the decomposition formula (Heiskanen and Moritz, 1967, p. 33), the Legendre polynomial can be expanded into spherical harmonics and terms that are dependent on the mass distribution collected into coefficients to yield

$$
\begin{array} { r c l } { { U } } & { { = } } & { { \displaystyle { \frac { \mu } { r } } + U ^ { \prime } } } \\ { { U ^ { \prime } } } & { { = } } & { { \displaystyle - { \frac { \mu ^ { * } } { r } } \sum _ { \ell = 1 } ^ { \infty } \left( { \frac { a _ { e } } { r } } \right) ^ { \ell } P _ { \ell } ( \sin \phi ) J _ { \ell } } } \\ { { } } & { { } } & { { \displaystyle + { \frac { \mu ^ { * } } { r } } \sum _ { \ell = 1 } ^ { \infty } \sum _ { m = 1 } ^ { \ell } \left( { \frac { a _ { e } } { r } } \right) ^ { \ell } P _ { \ell m } ( \sin \phi ) [ C _ { \ell m } \cos m \lambda + S _ { \ell m } \sin m \lambda ] } } \end{array}
$$

where the coordinates of $m ^ { \prime }$ are now expressed with spherical coordinates $( r _ { \cdot }$ , $\phi , \lambda )$ . Scale factors involving a reference mass $( \mu ^ { * } = G M ^ { * } )$ ) and a reference distance $( a _ { e } )$ have been introduced to nondimensionalize the mass property coefficients , $C _ { \ell m }$ and $S _ { \ell m }$ . The decomposition formula has introduced Legendre’s Associated Functions, $P _ { \ell m }$ , of degree $\ell$ and order m. The spherical coordinate $\phi$ represents a geocentric latitude and $\lambda$ represents a longitude angle. The relations between the spherical coordinates and $( x , y , z )$ are given by Eq. (2.2.37).

The coeffici ents $J _ { \ell } , C _ { \ell m }$ , and $S _ { \ell m }$ are referred to as spherical harmonic coefficients , or Stokes coefficients , representing mass properties of the body. For example, $J _ { \ell }$ is given by

$$
J _ { \ell } = - \left( \frac { 1 } { M ^ { * } a _ { e } ^ { \ell } } \right) \int _ { M } R ^ { \ell } P _ { \ell } ( \sin \phi ^ { \prime } ) d m
$$

where $\phi ^ { \prime }$ is the geocentric latitude of the differential mass $d m$ , $M ^ { * }$ is usually taken to be the mass of the body, and $a _ { e }$ is its mean equatorial radius. The Legendre polynomial $P _ { \ell }$ equals $P _ { \ell , 0 }$ . The similar expressions for $C _ { \ell m }$ and $S _ { \ell m }$ are dependent on the longitude of the differential mass. Note that if the body is rigid and the $( x , y , z )$ system is fix ed in the body, then the $J _ { \ell }$ , $C _ { \ell m }$ , and $S _ { \ell m }$ coeffic ients will be constant. On the other hand, if $( x , y , z )$ is not body-fix ed or if temporal redistribution of mass takes place, the coefficients will be time-dependent.

The $J _ { \ell }$ coefficient s are referred to as zonal harmonics, which are related to $C _ { \ell m }$ by the relation $J _ { \ell } = - C _ { \ell , 0 }$ . The $C _ { \ell m }$ and $S _ { \ell m }$ terms are named according to the values of $\ell$ and $m$ . If $\ell \neq m$ , the $C _ { \ell m }$ and $S _ { \ell m }$ coefficients are referred to as tesseral harmonics and if $\ell = m$ , they are referred to as sectoral harmonics. The terminology is derived from the fact that the $J _ { \ell }$ terms are independent of longitude and the zeroes of $P _ { \ell }$ can be visualized as dividing the body into zones of latitude. Similarly, when $\ell = m$ , the coefficients divide the body into sectors defined by longitude. The number of sectors is determined by $m$ . Additional descriptions are given by Heiskanen and Moritz (1967).

An alternate formulation for the gravitational potential uses normalized Legendre functions and coefficients. The Legendre functions for high degree acquire large numerical values and the mass coefficients are very small. The normalization process results in a set of mass coefficients, usually identified as $\overline { { C } } _ { \ell m }$ and $\overline { { S } } _ { \ell m }$ , with the same order of magnitude over a wide range of $\ell$ and $m$ . For the Earth, a set of mass coefficients is given in Appendix D along with the relations between normalized coefficients and conventional coefficients. Note that if normalized coefficients are used, a normalized set of Legendre functions must be used also.

Recursive expressions for the generation of both conventional and normalized expressions are given by Lundberg and Schutz (1988). The recursive expression for the conventional Legendre polynomial, $P _ { \ell } ( \sin \phi )$ , is

$$
P _ { \ell } ( \sin \phi ) = \bigl [ ( 2 \ell - 1 ) \sin \phi P _ { \ell - 1 } ( \sin \phi ) - ( \ell - 1 ) P _ { \ell - 2 } ( \sin \phi ) \bigr ] / \ell
$$

where $P _ { 0 } ( \sin \phi ) = 1$ and $P _ { 1 } ( \sin \phi ) = \sin \phi$ . The recursions for the conventional Legendre Associated Functions are

$$
P _ { \ell , \ell } ( \sin \phi ) = ( 2 \ell - 1 ) \cos \phi P _ { \ell - 1 , \ell - 1 } ( \sin \phi )
$$

where $P _ { 1 , 1 } ( \sin \phi ) = \cos \phi$ . Furthermore, for $l \neq m$

$$
P _ { \ell , m } ( \sin \phi ) = \left[ ( 2 \ell - 1 ) \sin \phi P _ { \ell - 1 , m } ( \sin \phi ) - ( \ell + m - 1 ) P _ { \ell - 2 , m } \right] / ( \ell - m )
$$

where $P _ { i , j } = 0$ if $j > i$ . In addition, note the following recursions:

$$
\begin{array} { r c l } { { \sin m \lambda } } & { { = } } & { { 2 \cos \lambda \sin ( m - 1 ) \lambda - \sin ( m - 2 ) \lambda } } \\ { { \cos m \lambda } } & { { = } } & { { 2 \cos \lambda \cos ( m - 1 ) \lambda - \cos ( m - 2 ) \lambda . } } \end{array}
$$

It can be shown that the degree one terms $( J _ { 1 } , C _ { 1 , 1 }$ , and $S _ { 1 , 1 }$ ) are proportional to the distance that the origin $O$ is offset from the center of mass of the body. If the origin $O$ coincides with the center of mass, the degree one terms will be zero.

In the case of the Earth, the center of mass origin usually is referred to as the geocenter. Furthermore, it can be shown that the degree two terms are proportional to the moments and products of inertia of the body and their combinations:

$$
\begin{array} { c } { { J _ { 2 } = \displaystyle \frac { 2 C - B - A } { 2 M a _ { e } ^ { 2 } } } } \\ { { { } } } \\ { { C _ { 2 , 1 } = \displaystyle \frac { I _ { x z } } { M a _ { e } ^ { 2 } } { \quad } S _ { 2 , 1 } = \displaystyle \frac { I _ { y z } } { M a _ { e } ^ { 2 } } { } } } \\ { { { } } } \\ { { C _ { 2 , 2 } = \displaystyle \frac { B - A } { 4 M a _ { e } ^ { 2 } } { \quad } S _ { 2 , 2 } = \displaystyle \frac { I _ { x y } } { 2 M a _ { e } ^ { 2 } } } } \end{array}
$$

where $A$ and $B$ are equatorial moments of inertia $\scriptstyle \cdot$ and $y$ axes); $C$ is the polar moment of inertia $z$ axis); $I _ { x y } , I _ { x z }$ , and $I _ { y z }$ are the products of inertia; $M$ is the mass of the body; and $a _ { e }$ is the mean radius.

$\mathbf { F } ^ { * }$ , experienced by $m ^ { \prime }$ , can be expressed as

$$
\mathbf { F } ^ { * } = m ^ { \prime } \nabla U
$$

and the equations of motion for $m ^ { \prime }$ can be shown to be

$$
\ddot { \bf r } = \left( 1 + \frac { m ^ { \prime } } { M } \right) \nabla U .
$$

However, if $m ^ { \prime }$ represents an artific ial satellite of the Earth, $m ^ { \prime } / M$ is very small, and this equation becomes

$$
\ddot { \mathbf { r } } = \nabla U = - \frac { \mu \mathbf { r } } { r ^ { 3 } } + \mathbf { f } _ { N S }
$$

where $\mathbf { f } _ { N S }$ denotes the contribution from the nonspherical $U ^ { \prime }$ terms; that is, $\boldsymbol { \nabla } U ^ { \prime }$ . Integration of these equations, even with a numerical method, requires some careful consideration. The acceleration term, $\ddot { \mathbf { r } }$ , can be expressed in either a bodyfix ed, rotating system $( x , y , z )$ or a nonrotating system $( X , Y , Z )$ . However, the gravitational potential is expressed using spherical coordinates, presumed to be defined using a body-fix ed coordinate system so that the mass property coefficients are constant (at least for a rigid body). Thus,

$$
\pmb { \nabla } U = \frac { \partial U } { \partial r } \mathbf { u } _ { r } + \frac { 1 } { r } \frac { \partial U } { \partial \phi } \mathbf { u } _ { \phi } + \frac { 1 } { r \cos \phi } \frac { \partial U } { \partial \lambda } \mathbf { u } _ { \lambda } .
$$

Although Eq. (2.3.18) contains a singularity at the poles, which poses a problem for exactly polar orbits, alternate formulations exist that remove this singularity (e.g., Pines, 1973). If the body-fix ed system is chosen to represent $\mathbf { r }$ , then $\ddot { \mathbf { r } }$ will


<!-- chunk 0002: pages 71-140 -->
include the Coriolis, centripetal, tangential, and relative acceleration terms. Alternatively, expressing ¨r in the nonrotating expression is simpler. Since the gradient of $U$ given by Eq. (2.3.18) provides force components in spherical coordinates, a coordinate transformation matrix $T _ { r \phi \lambda } ^ { x y z }$ is required to rotate the $\left( \mathbf { u } _ { r } , \mathbf { u } _ { \phi } , \mathbf { u } _ { \lambda } \right)$ components of $\mathbf { f }$ into $( x , y , z )$ components, as follows:

$$
T _ { r \phi \lambda } ^ { x y z } = \left[ \begin{array} { c c c } { \cos \phi \cos \lambda } & { - \sin \phi \cos \lambda } & { - \sin \lambda } \\ { \cos \phi \sin \lambda } & { - \sin \phi \sin \lambda } & { \cos \lambda } \\ { \sin \phi } & { \cos \phi } & { 0 } \end{array} \right]
$$

where the latitude $\phi$ and longitude $\lambda$ are related to $( x , y , z )$ through Eq. (2.2.36). In addition, if $\ddot { \mathbf { r } }$ is expressed in the nonrotating system, then a further transformation, $T _ { x y z } ^ { X Y Z }$ , is needed between the rotating axes $( x , y , z )$ and the nonrotating axes $( X , Y , Z )$ . The details of this transformation are dependent on variations in both the magnitude and direction of the angular velocity vector of the rotating axes. For simplicity in this discussion, if the $( x , y , z )$ axes rotate about the $Z$ axis and the $z$ axis is coincident with the $Z$ axis, it follows that the transformation is

$$
T _ { x y z } ^ { X Y Z } = \left[ \begin{array} { c c c } { \cos \alpha } & { - \sin \alpha } & { 0 } \\ { \sin \alpha } & { \cos \alpha } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right]
$$

where $\alpha$ represents the angle of rotation.

If the $( x , y , z )$ axes are fix ed in the Earth, with the $x$ axis coinciding with the intersection between the Greenwich meridian and the equator and the $X$ axis coincides with the vernal equinox, the angle $\alpha$ corresponds to $\alpha _ { G }$ , described in Section 2.2.3. Thus, the contribution of the mass distribution of the central body to the perturbing force in Eq. (2.3.3) is expressed by

$$
{ \bf f } _ { N S } = T _ { x y z } ^ { X Y Z } T _ { r \phi \lambda } ^ { x y z } \nabla U ^ { \prime }
$$

assuming $\mathbf { r }$ is expressed in the nonrotating system $( X , Y , Z )$ in the equations of motion. Hence, Eq. (2.3.17) becomes

$$
\ddot { \mathbf { r } } = - \frac { \mu } { r ^ { 3 } } \mathbf { r } + T _ { x y z } ^ { X Y Z } \ : T _ { r \phi \lambda } ^ { x y z } \ : \nabla U ^ { \prime } .
$$

The alternate expression for the equations of motion use the rotating system to express $\mathbf { r }$ . In this case,

$$
\begin{array} { c c l } { \ddot { \mathbf { r } } _ { \mathrm { R e l } } } & { = } & { - \boldsymbol { \omega } _ { c } \times \left( \boldsymbol { \omega } _ { c } \times \mathbf { r } \right) - 2 \boldsymbol { \omega } _ { c } \times \dot { \mathbf { r } } _ { \mathrm { R e l } } - \dot { \boldsymbol { \omega } } _ { c } \times \mathbf { r } } \\ & & { - \displaystyle \frac { \mu \mathbf { r } } { r ^ { 3 } } + T _ { r \phi \lambda } ^ { x y z } \nabla U ^ { \prime } } \end{array}
$$

where $\omega _ { c }$ represents the angular velocity vector of $( x , y , z )$ with respect to $( X , Y$ , $Z$ ), the position vector $\mathbf { r }$ is expressed in terms of $( x , y , z )$ components, and “Rel” means that the time derivative does not include derivatives of the unit vectors.

If $\omega _ { c }$ is constant such that $\omega _ { c } = \omega _ { c } \mathbf { u } _ { z }$ , it can be shown that an energy-like integral exists, known as the Jacobi Integral:

$$
\frac { v ^ { 2 } } { 2 } - \frac { \omega _ { c } ^ { 2 } ( x ^ { 2 } + y ^ { 2 } ) } { 2 } - \frac { \mu } { r } - U ^ { \prime } = K
$$

where $K$ is the Jacobi Constant and $v$ is the speed of the satellite with respect to the rotating system $( x , y , z )$ . Another form of this integral is given by Bond and Allman (1996), which is suitable for the nonrotating formulation:

$$
\frac { V ^ { 2 } } { 2 } - { \omega _ { c } } \cdot { \bf h } - \frac { \mu } { r } - U ^ { \prime } = K
$$

where $V$ is the ECI speed, $\omega _ { c }$ and $\mathbf { h }$ are also expressed in the ECI coordinate system. The relation between ECI velocity $( \mathbf { V } _ { \mathbf { \Omega } }$ ) and ECF velocity $( \mathbf { v } )$ i s

$$
\mathbf { V } = \mathbf { v } + \omega _ { c } \times \mathbf { r }
$$

For the same $U ^ { \prime }$ and the same assumptions about reference frames, the various differential equations (Eqs. (2.3.22), (2.3.23)) and the equations in Appendix C for orbit elements give equivalent results. In practice, the solution method applied to the respective equations may produce a different error spectrum. The nonrotating coordinate system and the equations represented by Eq. (2.3.22) are widely used in precision orbit determination software.

# 2.3.4 GRAVITATIONAL PERTURBATIONS: OBLATENESS AND OTHER EFFECTS

Consider an ellipsoid of revolution with constant mass density. It is apparent that $C _ { \ell m }$ and $S _ { \ell m }$ will be zero for all nonzero $m$ because there is no longitudinal dependency of the mass distribution. Furthermore, it can readily be shown that because of symmetry with respect to the equator there will be no odd-degree zonal harmonics. Hence, the gravitational potential of such a body will be represented by only the even-degree zonal harmonics. Furthermore, for a body like the Earth, more than $9 5 \%$ of the gravitational force (other than $\mu / r ^ { 2 }$ ) will be derived from the degree-2 term, $J _ { 2 }$ .

Assuming that the entire gravitational potential for the ellipsoid of revolution can be represented by the $J _ { 2 }$ term, it follows from Eq. (2.3.12) that

$$
U ^ { \prime } = - \frac { \mu } { r } \left( \frac { a _ { e } } { r } \right) ^ { 2 } J _ { 2 } P _ { 2 } ( \sin \phi )
$$

Table 2.3.2: Node Motion as a Function of i $\left( J _ { 2 } > 0 \right)$ )   

<table><tr><td>Inclination</td><td>Ss</td><td>Terminology</td></tr><tr><td>Posigrade</td><td>Negative</td><td>Regression of Nodes</td></tr><tr><td>Retrograde</td><td>Positive</td><td>Progression of Nodes</td></tr><tr><td>Polar</td><td>Zero</td><td></td></tr></table>

where $\mu ^ { * } = \mu$ and $P _ { 2 } ( \sin \phi ) = ( 3 \sin ^ { 2 } \phi - 1 ) / 2$ .

Noting that $\sin \phi = \sin i \sin ( \omega + f )$ from spherical trigonometry, it can be shown that the gravitational potential can be expressed in terms of orbit elements with the help of the expansions in eccentricity given in Eq. (2.2.26). By ignoring terms of order $e$ and higher, it follows that

$$
\begin{array} { l l l } { { U ^ { \prime } } } & { { = } } & { { \displaystyle - \frac { \mu } { a } \left( \frac { a _ { e } } { a } \right) ^ { 2 } J _ { 2 } \{ 3 / 4 \sin ^ { 2 } i [ 1 - \cos ( 2 \omega + 2 M ) ] - 1 / 2 \} } } \\ { { } } & { { + } } & { { \mathrm { h i g h e r ~ o r d e r ~ t e r m s } . } } \end{array}
$$

To a first order approximation, the orbit elements have a small variation with time, except $M$ , which is dominated by $n t$ . If $U ^ { \prime }$ is separated into

$$
U ^ { \prime } = U _ { s } + U _ { p }
$$

where

$$
\begin{array} { l c l } { { U _ { s } } } & { { = } } & { { \displaystyle - \frac { G M } { a } \left( \frac { a _ { e } } { a } \right) ^ { 2 } J _ { 2 } ( 3 / 4 \sin ^ { 2 } i - 1 / 2 ) } } \\ { { } } & { { } } & { { } } \\ { { U _ { p } } } & { { = } } & { { \displaystyle \frac { G M } { a } \left( \frac { a _ { e } } { a } \right) ^ { 2 } J _ { 2 } \left( 3 / 4 \sin ^ { 2 } i \cos ( 2 \omega + 2 M ) \right) } } \end{array}
$$

it can be shown from Eq. (2.3.6) that

$$
\dot { \Omega } _ { s } \cong - \frac { 3 } { 2 } J _ { 2 } n \left( \frac { a _ { e } } { a } \right) ^ { 2 } \cos i
$$

if the disturbing function $D$ is taken to be $U _ { s }$ and terms with $e$ are ignored. For convenience the notation $\dot { \Omega } _ { s }$ has been introduced to identify the node rate caused by $U _ { s }$ . It can be further shown using $U _ { s }$ that $a , ~ e$ , and $i$ do not change with time. Hence, for a given set of $a , e$ , and $i$ , $\dot { \Omega } _ { s }$ will be constant, referred to as the secular node rate. Furthermore, it is evident that the sign of $\dot { \Omega } _ { s }$ is determined by the inclination. Specifically , if $J _ { 2 }$ is positive (oblate spheroid, such as Earth), then Table 2.3.2 summarizes the characteristics and terminology associated with various inclinations.

From $\dot { \Omega } _ { s } = \mathrm { c o n s t a n t }$ , it is evident that the ascending node location changes linearly with time at a constant rate, referred to as a secular perturbation. Similarly, the term $U _ { p }$ is responsible for periodic perturbations. It is evident from Eq. (2.3.30) that the magnitude of the node rate for a given inclination will increase as the altitude decreases.

An important application of the secular perturbation in the node is the solarsynchronous satellite. As the name implies, such a satellite is synchronized with the Sun, such that the line of nodes remains aligned with the Earth-Sun direction. This orbit design is adopted for various reasons; for example, lighting conditions on the Earth’s surfaces. For a solar-synchronous satellite $\dot { \Omega _ { s } } = \bar { 3 6 0 ^ { \circ } } / \bar { 3 6 5 } . 2 5$ days $\cong 1 ^ { \circ }$ /day. For a near-circular orbit with a semimajor axis of about $7 0 0 0 { \mathrm { k m } }$ , the inclination would be about $9 8 ^ { \circ }$ .

A more complete expression with no eccentricity truncation for the expansion of the potential as a function of orbit elements can be found in Kaula (1966). This expansion enables the following expressions for the secular rates of $\Omega , \omega$ , and $M$ to be readily obtained:

$$
\begin{array} { r c l } { { \dot { \Omega } _ { s } } } & { { = } } & { { \displaystyle - \frac { 3 } { 2 } J _ { 2 } \frac { n } { ( 1 - e ^ { 2 } ) ^ { 2 } } \left( \frac { a _ { e } } { a } \right) ^ { 2 } \cos i } } \\ { { \dot { \omega } _ { s } } } & { { = } } & { { \displaystyle \frac { 3 } { 4 } J _ { 2 } \frac { n } { ( 1 - e ^ { 2 } ) ^ { 2 } } \left( \frac { a _ { e } } { a } \right) ^ { 2 } ( 5 \cos ^ { 2 } i - 1 ) } } \\ { { \dot { M } _ { s } } } & { { = } } & { { \displaystyle \bar { n } + \frac { 3 } { 4 } J _ { 2 } \frac { n } { ( 1 - e ^ { 2 } ) ^ { 3 / 2 } } \left( \frac { a _ { e } } { a } \right) ^ { 2 } ( 3 \cos ^ { 2 } i - 1 ) . } } \end{array}
$$

The values of $a , e$ , and $i$ in these expressions represent the mean elements; that is, the elements with periodic variations averaged out. In Eq. (2.3.33), $\bar { n } \ =$ $\mu ^ { 1 / 2 } / \bar { a } ^ { 3 / 2 }$ , where $\bar { a }$ is the mean value. Table 2.3.3 provides the characteristics and motion expressed by $\dot { \omega } _ { s }$ . As shown in this table, two inclinations exist where $\dot { \omega } _ { s } = 0$ , referred to as the critical inclinations.

Considering only the effect of $U _ { s }$ , the following orbit elements exhibit linear variations with time: $\Omega , \omega , M$ . It can be shown that $a , e$ , and $i$ do not exhibit such change. As a consequence, a simple model of the perturbed motion is a secularly precessing ellipse (SPE). In this model, $a , e$ , and $i$ are constant, and $\Omega , \omega$ , and $M$ change linearly with time at the rates derived from $U _ { s }$ . With the SPE as a reference, the effect of $U _ { p }$ , Eq. (2.3.29), can be introduced to show that, to first order,

$$
a ( t ) = \overline { { a } } + 3 \bar { n } \bar { a } J _ { 2 } \left( \frac { a _ { e } } { \overline { { a } } } \right) ^ { 2 } \sin ^ { 2 } \overline { { i } } \frac { \cos ( 2 \omega + 2 M ) } { 2 \dot { \omega } _ { s } + 2 \dot { M } _ { s } }
$$

Table 2.3.3: Perigee Motion as a Function of Inclination $\left( J _ { 2 } > 0 \right)$ )   

<table><tr><td>Inclination i</td><td>Ws</td><td>Terminology</td></tr><tr><td>i&lt; 63.435°</td><td>Positive</td><td>Progression of perigee</td></tr><tr><td>i = 63.435°</td><td>Zero</td><td>Critical inclination</td></tr><tr><td>63.435°&lt;i&lt;116.656°</td><td>Negative</td><td>Regression of perigee</td></tr><tr><td>i= 116.565°</td><td>Zero</td><td>Critical inclination</td></tr><tr><td>i &gt; 116.565</td><td>Positive</td><td>Progression of perigee</td></tr></table>

where $( ^ { - } )$ denotes the mean value of the element. Recall that this expression is approximate since terms with order $e ^ { 1 }$ and higher powers, as well as $J _ { 2 } ^ { 2 }$ , have been ignored. If the eccentricity is small, this expression is a good approximation. It should also be noted that mean elements can be replaced by osculating elements, except in the computation of $\overline { { n } }$ in the first term of $\dot { M }$ , since terms of $J _ { 2 } ^ { 2 }$ are ignored. Note that $\overline { { n } } = \mu ^ { 1 / 2 } / \overline { { a } } ^ { 3 / 2 }$ . If $J _ { 2 } ^ { 2 }$ terms are ignored, $\bar { a }$ may be computed from Eq. (2.3.34) by using an osculating value for $a ( t )$ and in the second term for $\bar { a }$ .

The preceding discussion illustrates the concepts of general perturbations; that is, an analytical solution of Lagranges planetary equations. A well-known solution for all the orbit elements is given by Brouwer for the $J _ { 2 }$ problem (Appendix E). The equations in this appendix have truncated Brouwer’s solution so that terms of order $e J _ { 2 }$ are ignored.

The linear solution of Kaula (1966) is an example of a solution that enables categorization of the influence of all gravity coefficients on the orbit perturbation. As shown by Kaula, the general frequency of a perturbation is given by

$$
\dot { \psi } _ { l m p q } = ( l - 2 p ) \dot { \omega } _ { s } + ( l - 2 p + q ) \dot { M } _ { s } + m ( \dot { \Omega } _ { s } - \omega _ { e } )
$$

where $p$ is an index that ranges from 0 to $l , q$ is an index associated with a function that is dependent on the orbit eccentricity, and $\omega _ { e }$ is the rotation rate of the primary body. The orbit element change with time is dependent on eccentricity and inclination functions. The eccentricity-dependent function has a leading term that is dependent on $e ^ { | q | }$ ; thus, for small eccentricity orbits, $q$ is usually considered to range between $- 2$ and $+ 2$ . The characteristics of the orbit perturbations caused by individual degree and order terms in the gravity field are summarized in Table 2.3.4, where the categories are defined by the nature of $\dot { \psi } _ { l m p q }$ . Note that the period of the perturbation is $2 \pi / \dot { \psi } _ { l m p q }$ . An example of resonance is the geostationary satellite, where $\dot { M } = \omega _ { e }$ .

Table 2.3.4:   
Perturbation Categories and Sources   

<table><tr><td>Category</td><td>Source</td><td>Comments</td></tr><tr><td>Secular</td><td>Even-degree zonals</td><td>l-2p=0;l-2p+q=0;m=0</td></tr><tr><td>Long period</td><td>Odd-degree zonals</td><td>l-2p≠0;l-2p+q=0;m=0</td></tr><tr><td>Short period</td><td>All gravity coeffci ents</td><td>l-2p+q≠0</td></tr><tr><td>m-daily</td><td>Order m terms</td><td>l-2p=0;l-2p+q=0;m≠0</td></tr><tr><td>Resonance</td><td>Order m terms</td><td>(l-2p)u+(l-2p+q)M≌-m(Ω-ωe)</td></tr></table>

A special class of perturbed orbits, known as frozen orbits, have proven useful for some applications. For these orbits, even though the inclination is not critical, $J _ { 2 }$ and $J _ { 3 }$ interact to produce $\dot { \omega } _ { s } = 0$ (Cook, 1966; Born et al., 1987) and the mean perigee remains fixed at about $9 0 °$ or $2 7 0 ^ { \circ }$ in an average sense. Frozen orbits are useful in applications where it is desired that the mean altitude have small variations for a given latitude. They are required if it is necessary to have an exactly repeating ground track. Otherwise, the time to go between two latitudes will vary as the perigee rotates, and the ground tracks will not repeat.

The nodal period is the time required for a satellite to complete successive equatorial crossings, such as ascending node to ascending node. The nodal period, $P _ { n }$ , is

$$
P _ { n } = \frac { 2 \pi } { \dot { \omega } _ { s } + \dot { M } _ { s } }
$$

or

$$
P _ { n } = \frac { 2 \pi } { \bar { n } } \left[ 1 - 3 / 2 J _ { 2 } \left( \frac { a _ { e } } { \overline { { { a } } } } \right) ^ { 2 } \left( 4 \cos ^ { 2 } i - 1 \right) \right]
$$

which is obtained using Eqs. (2.3.31) and (2.3.32). Using osculating elements, the nodal period for a near-circular orbit is

$$
\begin{array} { l c l } { { P _ { n } } } & { { = } } & { { \displaystyle \frac { 2 \pi } { n } \bigg [ 1 - 3 / 4 ~ J _ { 2 } \left( \frac { a _ { e } } { a } \right) } } \\ { { } } & { { } } & { { \displaystyle \left\{ 1 + 5 \cos ^ { 2 } i - 6 \sin ^ { 2 } i \sin ^ { 2 } \left( \omega + M \right) \right\} \bigg ] . } } \end{array}
$$

Note that either mean or osculating elements can be used in any term that is multiplied by $J _ { 2 }$ , since the approximation used in the analytic theory is accurate only to order $J _ { 2 }$ . However, unless a mean value of semimajor axis is used in Eq. (2.3.37), an error of order $J _ { 2 }$ will be introduced in the lead term of the nodal period equation. Note also that Eq. (2.3.38) requires an osculating value for $a$ to compute $n$ .

Another useful concept in mission design is that of the nodal day, which is the time required for the Earth to make one revolution relative to the satellite’s line of nodes. It is given by

$$
D _ { n } = \frac { 2 \Pi } { \dot { \Omega } _ { s } + \omega _ { e } } .
$$

Hence, a nodal day will be greater than a siderial day for retrograde orbits and less than a siderial day for posigrade orbits.

# Example 2.3.1

For the Space Shuttle example, Example 2.2.4.1, use the state vector as initial conditions for the numerical integration of the equations of motion given by Eqs. (2.3.17) and (2.3.26). For the Earth, $J _ { 2 } = 0 . 0 0 1 0 8 2 6 3 6$ (the normalized value $C _ { 2 , 0 } = - 0 . 0 0 0 4 8 4 1 6 9 5 )$ . The position-velocity ephemeris, converted into orbit elements, produces the results shown in Fig. 2.3.5 for $a , e , i , \Omega$ , and $\omega$ for a one-day interval. Evaluation of Eq. (2.3.31) for $\dot { \Omega } _ { s }$ with the approximate mean orbit elements $( a = 6 8 2 7 \mathrm { k m }$ , $e = 0 . 0 0 8$ , $i = 2 8 . 4 5 5$ ) gives $- 6 . 9 1 ^ { \circ } / \mathrm { d a y }$ . The approximate slope of $\Omega$ in Fig. 2.3.5 is $- 6 . 9 3 ^ { \circ } / \mathrm { d a y }$ . Note that $a$ and $i$ exhibit no secular rate (as expected), only a dominant twice-per-revolution change, as suggested by Eq. (2.3.34) for semimajor axis. Note that $e$ exhibits no secular variation, although its periodic variations includes a combination of frequencies (see Appendix E).

# 2.3.5 GRAVITATIONAL PERTURBATIONS: THIRD-BODY EFFECTS

An artificial satellite of the Earth experiences the gravitational attraction of the Sun, the Moon, and to a lesser extent the planets and other bodies in the solar system. Equation (2.3.1), which was derived for the perturbed lunar motion based on the gravitational problem of three bodies, can be adapted to represent the gravitational effect of celestial bodies on the motion of a satellite. Since the description is based on the problem of three bodies, the perturbation is often referred to as the third-body effect, even when more than three bodies are considered. In some literature, the terminology $n$ -body effects may be used to accommodate the case when many perturbing bodies are included. With the third-body effects, it can be shown that the perturbing force contribution to the equations of motion, Eq. (2.3.3), is

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0002_pages_0071-0140/auto/images/5293a6e480e9127c6889632a7c519b62f8847a56860bad0948f657468a79da37.jpg)  
Figure 2.3.5: Orbit element variations produced by Earth oblateness, $J _ { 2 }$ . The mean anomaly is not shown since it is a straight line with a slope approximately equal to $n$ . The ascending node and the argument of perigee exhibit significant linear variation, whereas $a , ~ e$ , and $i$ do not. These results were obtained from numerical integration of the equations of motion.

$$
\mathbf { f } _ { 3 B } = \sum _ { j = 1 } ^ { n _ { p } } \mu _ { j } \left( \frac { \Delta _ { j } } { \Delta _ { j } ^ { 3 } } - \frac { \mathbf { r } _ { j } } { r _ { j } ^ { 3 } } \right)
$$

where $n _ { p }$ is the number of additional bodies, $j$ represents a specific body (Sun, Moon, or planet), $\mu _ { j } = G M _ { j }$ is the gravitational parameter of body $j , \Delta _ { j }$ is the position vector of $M _ { j }$ with respect to the satellite, and $\mathbf { r } _ { j }$ is the position vector of $M _ { j }$ with respect to the Earth (see Fig. 2.3.1). The first term $( \Delta _ { j } / \Delta _ { j } ^ { 3 } )$ of the thirdbody perturbation is known as the direct effect and the second term $( \mathbf { r } _ { j } / r _ { j } ^ { 3 } )$ is the indirect effect. The notation for the latter term arises from the observation that it is independent of the artificial satellite coordinates. Since Eq. (2.3.39) describes the satellite motion with respect to the Earth center of mass, which is a noninertial point, the indirect term accounts for the inertial acceleration of the geocenter.

The third-body terms in Eq. (2.3.39) are based on the assumption that the satellite, Earth, and perturbing body $( M _ { j } )$ are point masses (or spheres of constant density). In reality, the Moon and Sun should be represented by a gravitational potential, such as Eq. (2.3.12). The satellite equations of motion will be complicated by the inclusion of these terms, but the accuracy required for most applications does not warrant such modeling of the luni-solar gravitational fields. For some high-accuracy applications, the dominant contribution is the interaction of the third body with the Earth oblateness through the indirect term, sometimes referred to as the indirect oblateness.

The nature of the third-body perturbation is similar to the Earth oblateness effect; namely, the Sun and Moon produce a secular variation in the satellite node, argument of perigee, and mean anomaly. Expressing the third-body perturbation with a gravitational potential and following a treatment similar to the approach used in Section 2.3.4, it can be shown that the secular node rate for an Earth satellite is

$$
{ \dot { \Omega } } _ { \mathrm { s e c } } = { \frac { 3 } { 4 } } { \frac { \mu _ { j } } { a _ { j } ^ { 3 } } } { \frac { \cos i } { n } } \left( { \frac { 3 } { 2 } } \sin ^ { 2 } \epsilon - 1 \right)
$$

where the $5 ^ { \circ }$ inclination of the Moon’s orbit with respect to the ecliptic has been ignored, the subscript $j$ identifies the Moon or the Sun, and $\epsilon$ is the obliquity of the ecliptic.

It is evident from Eq. (2.3.40) that the third-body effect on the nodal motion increases as the altitude increases, since $n$ gets smaller with increasing semimajor axis. This characteristic is consistent with the expectation that the effect would increase as the satellite altitude approaches the source of the perturbation. Note the dependency of $\dot { \Omega } _ { \mathrm { s e c } }$ on $\cos i$ , which is similar to the $J _ { 2 }$ effect. Since the quantity in parentheses is negative, $\dot { \Omega } _ { \mathrm { s e c } }$ is retrograde for a posigrade orbit, for example.

In addition to the secular effect contributed by the Moon and Sun, significant periodic effects exist. The largest periodic effects have periods of 183 days and 14 days, caused by the Sun and Moon, respectively. The semiannual solar effects are greater than the lunar semimonthly effects. The coordinates of the Sun, Moon, and planets required for the third-body perturbation are available in numerical form (e.g., Standish et al., 1997). These coordinates are expressed in the J2000.0 system.

# 2.3.6 GRAVITATIONAL PERTURBATIONS: TEMPORAL CHANGES IN GRAVITY

If the mass distribution within a body is constant over time in an appropriate coordinate system that is fix ed in the body, the mass property coeffici ents, $C _ { l m }$ and $S _ { l m }$ , will be constant. Such is the case if the body is perfectly rigid. However, all celestial bodies deform at some level and this deformation redistributes mass so that the mass property coefficients vary with time. The ocean tides are well known and familiar mass-redistribution phenomena, but the solid Earth also responds to the same luni-solar gravitational forces that are responsible for the ocean tides. The previous formulation for the gravitational potential, Eq. (2.3.12), is valid even if the $C _ { l m }$ and $S _ { l m }$ coefficients are time dependent. The detailed formulation for the temporal changes in these coefficients produced by solid Earth and ocean tides is given by McCarthy (1996). Further discussion of the topic is given by Lambeck (1988).

The dominant tide effect appears in temporal changes of the degree two coefficients ; namely,

$$
\begin{array} { l r c l r c l } { { \Delta J _ { 2 } } } & { { = } } & { { - K _ { T } \ q _ { 2 , 0 } } } & { { } } & { { } } & { { } } & { { } } \\ { { \Delta C _ { 2 , 1 } } } & { { = } } & { { K _ { T } \ q _ { 2 , 1 } } } & { { \Delta S _ { 2 , 1 } } } & { { = } } & { { K _ { T } \ u _ { 2 , 1 } \nonumber } } \\ { { \Delta C _ { 2 , 2 } } } & { { = } } & { { K _ { T } \ q _ { 2 , 2 } } } & { { \Delta S _ { 2 , 2 } } } & { { = } } & { { K _ { T } \ u _ { 2 , 2 } } } \end{array}
$$

$$
K _ { T } = k _ { 2 } \frac { a _ { e } ^ { 3 } } { \mu } .
$$

Here, $k _ { 2 } =$ second-degree Love Number (dependent on elastic properties of the Earth, with an approximate value of 0.3), thus:

$$
\begin{array} { c c l } { { q _ { 2 , 0 } } } & { { = } } & { { \displaystyle \sum _ { j } C _ { T } P _ { 2 , 0 } ( \sin \phi _ { j } ) } } \\ { { } } & { { } } & { { } } \\ { { q _ { 2 , 1 } } } & { { = } } & { { \frac { 1 } { 3 } \displaystyle \sum _ { j } C _ { T } P _ { 2 , 1 } ( \sin \phi _ { j } ) \cos \lambda _ { j } } } \end{array}
$$

$$
\begin{array} { l c l } { { q _ { 2 , 2 } } } & { { = } } & { { \frac { 1 } { 1 2 } \displaystyle \sum _ { j } C _ { T } P _ { 2 , 2 } ( \sin \phi _ { j } ) \cos 2 \lambda _ { j } } } \\ { { } } & { { } } & { { } } \\ { { u _ { 2 , 1 } } } & { { = } } & { { \frac { 1 } { 3 } \displaystyle \sum _ { j } C _ { T } P _ { 2 , 1 } ( \sin \phi _ { j } ) \sin \lambda _ { j } } } \\ { { } } & { { } } & { { } } \\ { { u _ { 2 , 2 } } } & { { = } } & { { \frac { 1 } { 1 2 } \displaystyle \sum _ { j } C _ { T } P _ { 2 , 2 } ( \sin \phi _ { j } ) \sin 2 \lambda _ { j } } } \\ { { } } & { { } } & { { } } \\ { { C _ { T } } } & { { = } } & { { \frac { \mu _ { j } } { r _ { j } ^ { 3 } } } } \end{array}
$$

where

$j$ is determined by the Moon or Sun,

$r _ { j }$ is the distance from the geocenter to the center of mass of the Moon or Sun, and

$\phi _ { j } \lambda _ { j }$ are the geocentric latitude and longitude of the Moon and Sun, respectively.

The magnitude of $\Delta J _ { 2 }$ is about $1 0 ^ { - 8 }$ , compared to the $J _ { 2 }$ magnitude of $1 0 ^ { - 3 }$ . Care should be taken with applying $\Delta J _ { 2 }$ , since the average value produced by Eq. (2.3.41) is nonzero and this average may already be accommodated into $J _ { 2 }$ .

Other phenomena contribute to temporal changes in gravity. Among these are meteorologically driven redistributions of atmospheric mass as well as redistribution of solid Earth and ocean mass in response to changes in the magnitude and direction of the Earth’s angular velocity vector. The latter phenomena are referred to as pole tides.

# 2.3.7 GRAVITATIONAL PERTURBATIONS: GENERAL RELATIVITY

Although the preceding developments are well served by the foundations of Newtonian mechanics, some high-accuracy applications will require additional terms introduced by relativistic effects (Einstein, 1905; Huang et al. 1990; Ries et al., 1991). The dominant dynamical effect from general relativity is a small, but observable, advance in the argument of perigee (Ries et al., 1991). For example, a satellite such as BE-C $( a = 7 5 0 0 \mathrm { k m }$ , $e = 0 . 0 2 5$ , $i = 4 1 . 2 ^ { \circ }$ ) experiences an advance of 11 arcsec/yr in the location of perigee. The relativistic term that should be included in the equations of motion is

$$
{ \bf f } _ { g } = \frac { \mu } { c ^ { 2 } r ^ { 3 } } \left\{ \left[ 2 ( \beta + \gamma ) \frac { \mu } { r } - \gamma ( \dot { \bf r } \cdot \dot { \bf r } ) \right] { \bf r } + 2 ( 1 + \gamma ) ( { \bf r } \cdot \dot { \bf r } ) \dot { \bf r } \right\}
$$

where

$c$ is the speed of light,

$\mathbf { r } , \dot { \mathbf { r } }$ are the position and velocity vectors of the satellite in geocentric nonrotating coordinates,

$\beta , \gamma$ are parameters in the isotropic Parameterized Post-Newtonian metric, which are exactly equal to one in General Relativity.

As previously noted, the dominant effect of this contribution is a secular motion of perigee.

# 2.3.8 NONGRAVITATIONAL PERTURBATIONS: ATMOSPHERIC RESISTANCE

For a low-altitude Earth satellite, atmospheric drag can be a dominant perturbing force. The drag force is derived from aerodynamic considerations and the representation of the drag force on an orbiting vehicle is the same as an atmospheric fli ght vehicle:

$$
\mathbf { F } _ { \mathrm { D r a g } } = - 1 / 2 \rho C _ { D } A V _ { r } \mathbf { V } _ { r }
$$

where $\rho$ is the atmospheric density, $C _ { D }$ is the drag coefficient, ${ \mathbf V } _ { r }$ is the vehicle velocity relative to the atmosphere, $A$ is the satellite cross-sectional area and the minus sign denotes the direction opposite to ${ \mathbf V } _ { r }$ . When this force is included in the derivation of the equations of satellite motion with respect to the geocenter, the following perturbing force per unit mass results, which will be added to the other forces in Eq. (2.3.3):

$$
{ \bf f } _ { \mathrm { D r a g } } = - 1 / 2 \rho \left( \frac { C _ { D } A } { m } \right) V _ { r } { \bf V } _ { r }
$$

where the satellite mass, $m$ , now appears as a divisor in the drag term. A commonly used parameter in the drag term is $( C _ { D } A / m )$ , sometimes referred to as the ballistic coefficient . At low altitudes, such as those where the Space Shuttle operates $( \sim 3 5 0 \mathrm { k m } )$ ), the atmospheric density is about $1 0 ^ { - 1 1 }$ that of sea level density. Such low densities have mean molecular distances measured in meters. Nevertheless, atmospheric drag removes energy from the orbit and produces a secular decay in semimajor axis and eccentricity. This decay eventually brings the satellite into the higher density regions of the atmosphere, and it may be destroyed by the heating produced from atmospheric friction generated by the high orbital speeds. Some satellites have been designed to accommodate the high heat loads produced by atmospheric entry, such as Space Shuttle, but most satellites will not survive intact.

The drag term in Eq. (2.3.43) is dependent on several factors. Most notably, the atmospheric density exhibits an approximately exponential reduction with increasing altitude, $\rho = \rho _ { 0 } e ^ { - \beta ( h - h _ { 0 } ) }$ , where $\rho _ { 0 }$ is the density at a reference altitude $h _ { 0 }$ , $h$ is the altitude of interest, and $\beta$ is a scale parameter. But the specific density at any location will be influe nced by the day-night cycle and the location of the subsolar point, solar activity (e.g., solar storms), geomagnetic activity, and seasonal variations. A satellite at a constant altitude can experience an order of magnitude change in density over an orbital revolution. Acting over many orbital revolutions, the decay in semimajor axis will determine the lifetime of a satellite. A very low-altitude satellite with a high ballistic coefficient will have a short lifetime, perhaps a few weeks or a few months in duration. Prediction of satellite lifetime is a challenging problem, but it is made particularly difficul t by uncertainties in predicting atmospheric density and other factors. Various models of atmospheric density exist, such as those developed by Barlier, et al. (1978) and Jacchia (1977).

To account for the variations in drag produced by changes in atmospheric density, as well as the area-to-mass ratio $\left( A / m \right)$ , other parameterizations are introduced. These parameterizations may include piecewise constant values of $C _ { D }$ , which are defined over specific intervals of time, or more complex representations of $C _ { D }$ .

Some satellites have been designed to reduce the effects of atmospheric drag. Most notably, these are satellites where high-accuracy knowledge of the orbital position is required and it is desirable to minimize the influence of forces with significa nt uncertainty such as drag. The French Starlette satellite, launched in 1975, is spherical with a diameter of $1 4 ~ \mathrm { c m }$ , but it contains a core of depleted uranium to increase the mass. The area-to-mass ratio for Starlette is $0 . 0 0 1 \mathrm { ~ m } ^ { 2 } / \mathrm { k g }$ . By contrast, the Echo balloon satellite had an $\mathrm { A } / \mathrm { m }$ of about $1 0 \mathrm { m } ^ { 2 } / \mathrm { k g }$ . It is obvious that the balloon satellite will have a much shorter lifetime than Starlette at the same altitude.

If it is assumed that $V _ { r } = V$ , it can be shown (Danby, 1988) that

$$
\frac { d a } { d t } = - \left( \frac { C _ { D } A } { m } \right) \frac { \rho a ^ { 2 } } { \mu } V ^ { 3 } .
$$

Since $V _ { r }$ is almost entirely in the orbit plane, drag has only a very small out-ofplane force and, hence, there is no significant drag effect on the orbit node or

inclination. In addition to the secular change in semimajor axis, $e$ and $\omega$ also exhibit secular change because of drag.

# 2.3.9 NONGRAVITATIONAL PERTURBATIONS: RADIATION PRESSURE

For an Earth satellite, the Sun is the source for perturbations referred to as solar radiation pressure. This force results from the transfer of momentum through impact, reflection, absorption, and re-emission of photons. The Earth is an additional perturbation source, through both reflected solar radiation and emitted radiation, both of which exhibit considerable variation over an orbital revolution. The solar radiation pressure force contribution $( \mathbf { f } _ { S R P } )$ to Eq. (2.3.3) is given by

$$
\mathbf { f } _ { S R P } = - P \frac { \nu A } { m } C _ { R } \mathbf { u }
$$

where $P$ is the momentum flux from the Sun at the satellite location, $A$ is the cross-sectional area of the satellite normal to the Sun, $\mathbf { u }$ is the unit vector pointing from the satellite to the Sun, $C _ { R }$ is the reflec tivity coefficient with a value of approximately one, and $\nu$ is an eclipse factor such that $\nu = 0$ if the satellite is in the Earth’s shadow (umbra), $\nu = 1$ if the satellite is in sunlight, and $0 < \nu < 1$ if the satellite is in partial shadow or penumbra. The passage of the satellite from sunlight to shadow is not abrupt, but the interval of time spent in partial shadow will be very brief for near-Earth satellites. In the vicinity of Earth, $P$ is approximately $4 . 5 6 \times 1 0 ^ { - 6 }$ Newtons $/ \mathrm { m ^ { 2 } }$ .

The modeling of the Earth radiation components is commonly performed with spherical harmonics to represent latitudinal and longitudinal variations of Earth albedo and emissivity. This force can be expressed using Eq. (2.3.45), except the momentum flux parameter would account for the albedo and emissivity and u would be directed toward the Earth. It is known from observations that the simple model given by Eq. (2.3.45) is inadequate for applications with high accuracy requirements. Alternate models for GPS are described by Fliegel et al. (1992) and Beutler et al. (1994).

# 2.3.10 NONGRAVITATIONAL PERTURBATIONS: OTHER

Other nongravitational forces exist that may influence the orbit in complex ways. Aside from forces that involve the magnetic fiel d of the planet (e.g., if the satellite has a charge), there are other forces that have been studied because of their anomalous nature.

In addition to solar radiation pressure modeled by Eq. (2.3.45), heating of satellite components by the Sun and the Earth, as well as internal heat sources, will produce an unsymmetrical thermal distribution. Such a thermal imbalance will generate a thermal force, which may produce drag-like characteristics. The modeling of a spacecraft with more complex shapes, such as TOPEX/Poseidon and GPS, has required analysis by finite element methods for high-accuracy applications. A review of nongravitational force modeling is given by Ries et al. (1993). For purposes of this book, these forces will be covered by the term fOther in the satellite equations of motion.

Satellite-dependent models have been developed to represent some nongravitational components. The GPS satellites experience a force parallel to the solar panel rotation axis, referred to as the y-bias force, thought to result from solar panel misalignment and/or thermal force effects (Vigue, et al., 1994). index[aut]Schutz, B. E.

Additional forces exist, usually with short time duration, associated with mass expulsion from a spacecraft. The resulting force, or thrust, may be difficult to model because the time at which the expulsion occurred and magnitude of the event may be unknown.

For some applications, empirical forces are included in the equations of motion to accommodate forces of unknown origin or errors that result from mismodeling of forces. As described in this chapter, a typical error signature has a periodicity approximately equal to the orbit period; that is, a once per revolution characteristic. A convenient modeling takes the form of $A \cos n t + B \sin n t + C$ , where $n$ is the mean motion and $A$ , $B$ , $C$ are empirical parameters to be estimated in the orbit determination process. The empirical model may be applied to the radial, transverse, and/or normal components.

# 2.3.11 PERTURBED EQUATIONS OF MOTION: SUMMARY

Based on Eq. (2.3.3), the satellite equations of motion are

$$
{ \ddot { \mathbf { r } } } = - { \frac { \mu \mathbf { r } } { r ^ { 3 } } } + \mathbf { f }
$$

where $\mathbf { r }$ is the position vector of the satellite center of mass in an appropriate reference frame. The perturbing force f consists of the following

$$
\mathbf { f } = \mathbf { f } _ { N S } + \mathbf { f } _ { 3 B } + \mathbf { f } _ { g } + \mathbf { f } _ { \mathrm { D r a g } } + \mathbf { f } _ { \mathrm { S R P } } + \mathbf { f } _ { \mathrm { E R P } } + \mathbf { f } _ { \mathrm { O t h e r } }
$$

where

$\mathbf { f } _ { N S }$ is given by Eq. (2.3.21), including the tide contribution in Eq. (2.3.41),   
$\mathbf { f } _ { 3 B }$ is given by Eq. (2.3.39),   
$\mathbf { f } _ { g }$ represents the contributions of general relativity, Eq. (2.3.42),   
$\mathbf { f } _ { \mathrm { D r a g } }$ is given by Eq. (2.3.43),

fSRP is given by Eq. (2.3.45), fERP is Earth radiation pressure,

fOther represents other forces, such as thermal effects, magnetically induced forces, and so on.

The various contributions to the equations of motion must use a consistent coordinate system. If, for example, the acceleration ¨r is expressed in J2000, all individual components of f must be expressed in the same system. As a result, some of these components may require coordinate transformations similar to those given in Eq. (2.3.21) for the nonspherical mass distribution effects. Advanced aspects of the relevant transformation between, for example, Earth-fix ed and J2000 are discussed in the next section.

As noted previously, Eq. (2.3.46) can be solved with the use of a numerical method or through analytical approaches. Both introduce different levels of approximation. Various high-accuracy numerical programs have been developed in the community based on different numerical methods (single-step integrators, multistep integrators, etc.).

The advantage of speed offered by analytical techniques may be traded for force model accuracy (see Section 2.5). In these cases, a simplified geopotential consisting of a few zonal harmonics plus the effects of luni-solar gravity and drag may be used. NORAD, for example, has adopted such a general perturbation method, based on Brouwer’s Theory (see Appendix E).

# Example 2.3.11.1

The node rate of the GPS satellite known as PRN-5 was observed to have a dominant secular rate of $- 0 . 0 4 1 0 9 ~ \mathrm { d e g / d a y }$ during 1995 and 1996. We wish to determine the most significant factors that contribute to this rate. The following mean elements for the satellite also were observed:

$$
\begin{array} { l c l } { { a } } & { { = } } & { { 2 6 5 6 0 . 5 \mathrm { k m } } } \\ { { e } } & { { = } } & { { 0 . 0 0 1 5 } } \\ { { i } } & { { = } } & { { 5 4 . 5 \mathrm { d e g } . } } \end{array}
$$

The following contributions can readily be obtained:

$J _ { 2 }$ Eq. (2.3.31) −0.03927 deg/day Moon Eq. (2.3.40) −0.00097 Sun Eq. (2.3.40) −0.00045

Total −0.04069 deg/day

The difference between the observed value and this total is $0 . 0 0 0 4 ~ \mathrm { d e g / d a y }$ , or $1 \%$ , caused mainly by secular contributions from the other even-degree zonal harmonics and $J _ { 2 } ^ { 2 }$ .

# 2.4 COORDINATE SYSTEMS AND TIME:INTRODUCTION

Time and coordinate systems are an inherent component of the orbit determination problem. As described in Chapter 3, measurements of some aspect of a satellite’s position or motion must be indexed in time. The time index of the measurements must be related to the time used in the equations of motion, Eq. (2.3.46), but different time systems are used, all of which attempt to represent the concept of Newtonian time. The relation between the various time systems must be known.

Measurements collected by some instrumentation located on the Earth’s surface suggest the use of coordinate systems attached to the Earth at the location of the instrument. Such topocentric coordinate systems rotate since they are fix ed to the planet’s surface. On the other hand, the equations of motion use an inertial system. It is evident that transformation equations between the various coordinate systems are required.

The coordinate description given in Section 2.2.3, based on the problem of two bodies, assumed that the bodies were rigid spheres with constant density. In this model, the equinoxes remained fix ed in direction, and the angular velocity vectors of the rotating bodies maintain the same direction in space. The following sections relax these conditions and examine the effects resulting from more realistic models of the celestial bodies. The resulting transformations and relationships are essential in the modern orbit determination problem. More complete discussions of the characteristics of the rotation of the Earth are given by Lambeck (1980) and Moritz and Mueller (1987).

# 2.4.1 PRECESSION AND NUTATION

Consider the motion of a spherical Moon orbiting the nonspherical Earth. Based on the discussion in Section 2.3, the gradient of the gravitational potential given by Eq. (2.3.12), multiplied by the mass of the Moon, yields the gravitational force experienced by the Moon. By Newton’s Third Law, the Earth will experience an equal and opposite force; however, this force will not, in general, be directed through the center of mass of the Earth. As a consequence, the Earth will experience a gravitational torque, $\mathbf { T }$ , given by

$$
\mathbf { T } = - \mathbf { r } _ { p } \times M _ { P } \pmb { \nabla } _ { P } U ^ { \prime }
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0002_pages_0071-0140/auto/images/2195bbb3aefa6fd7f2879c7cc3aae991874debf49482f41746ac834c5412a069.jpg)  
Figure 2.4.1: Precession and nutation. The Sun and Moon interact with the oblateness of the Earth to produce a westward motion of the vernal equinox along the ecliptic $( \Psi )$ and oscillations of the obliquity of the ecliptic $( \epsilon )$ .

where $U ^ { \prime }$ is the Earth’s gravitational potential, $\nabla _ { P }$ is the gradient operator with respect to the coordinates of the Moon $( \mathbf { r } _ { p } )$ , and $M _ { P }$ is the mass of the Moon. The torque acting on the Earth produces changes in the inertial orientation of the Earth.

In the case of the Earth, both the Moon and the Sun are significant contributors to this gravitational torque. A dominant characteristic of the changes in inertial orientation is a conical motion of the Earth’s angular velocity vector in inertial space, referred to as precession. Superimposed on this conical motion are small oscillations, referred to as nutation.

Consider the two angles in Fig. 2.4.1, $\Psi$ and $\epsilon$ . The angle $\Psi$ is measured in the ecliptic from a fix ed direction in space, $X ^ { \ast }$ , to the instantaneous intersection of the Earth’s equator and the ecliptic. As discussed in Section 2.2.3, the intersection between the equator and the ecliptic where the Sun crosses the equator from the southern hemisphere into the northern hemisphere is the vernal equinox. For this discussion, the ecliptic is assumed to maintain a fix ed orientation in space, although this is not precisely the case because of gravitational perturbations from the planets. The angle $\epsilon$ represents the angle between the angular velocity vector and an axis $Z _ { e c }$ , which is perpendicular to the ecliptic. The gravitational interaction between the Earth’s mass distribution, predominantly represented by the oblateness term, $J _ { 2 }$ , and the Sun or Moon produces a change in $\Psi$ , which can be shown to be

$$
\dot { \Psi } = - { \frac { 3 } { 2 } } \left( { \frac { \mu J _ { 2 } a _ { e } ^ { 2 } } { C \omega _ { e } } } \right) { \frac { M _ { p } } { a _ { p } ^ { 3 } } } \cos \bar { \epsilon }
$$

where the subscript $p$ represents the Sun or the Moon, the parameters in the parentheses refer to Earth, $C$ is the polar moment of inertia of Earth, and $\bar { \epsilon }$ is the mean obliquity of the ecliptic. This motion, known as the precession of the equinoxes, has been known since antiquity. The combined effect of the Sun and the Moon produce $\dot { \Psi } = - 5 0$ arcsec/yr; that is, a westward motion of the vernal equinox amounting to $1 . 4 ^ { \circ }$ in a century. Thus, the conical motion of $\omega _ { e }$ about $Z _ { e c }$ requires about 26,000 years for one revolution.

The obliquity of the ecliptic, $\epsilon$ , is $\epsilon = \bar { \epsilon } + \Delta \epsilon$ , where $\bar { \epsilon }$ represents the mean value, approximately $2 3 . 5 ^ { \circ }$ . The nutations are represented by $\Delta \epsilon$ , which exhibits periodicities of about 14 days (half the lunar period, or semimonthly) and 183 days (half the solar period, or semiannual), plus other long period variations. The $5 ^ { \circ }$ inclination of the Moon’s orbit with respect to the ecliptic, $i _ { M }$ , produces a long period nutation given by:

$$
\Delta \epsilon = \frac { 3 } { 2 } \left( \frac { \mu J _ { 2 } a _ { e } ^ { 2 } } { C \omega _ { e } } \right) \frac { M _ { M } } { a _ { M } ^ { 3 } } \cos i _ { M } \sin i _ { M } \cos \epsilon \frac { \cos ( \Omega _ { M } - \Psi ) } { ( \dot { \Omega } _ { M } - \dot { \Psi } ) }
$$

where the subscript $M$ refers to the Moon, and the amplitude of the coefficient of $\cos ( \Omega _ { M } - \Psi )$ in Eq. (2.4.3) is about 9 arcsec with a period of 18.6 years. The 9 arcsec amplitude of this term is known as the constant of nutation. The amplitudes of the semimonthly and semiannual terms are smaller than the constant of nutation, but all are important for high-precision applications.

The precession/nutation series for a rigid body model of the Earth, including the ecliptic variations, were derived by Woolard (1953). Extensions that include the effects of nonrigidity have been developed. Nevertheless, small discrepancies between observation and theory exist, believed to be associated with geophysical effects in the Earth’s interior (Herring et al., 1991; Wahr, 1981). Such observational evidence will lead, in time, to the adoption of new series representing the precession and nutation. The current 1980 International Astronomical Union (IAU) series are available with the lunar, solar, and planetary ephemerides in an efficient numerical form based on results generated by the Jet Propulsion Laboratory (Standish et al., 1997).

As described in Section 2.2.3, the J2000.0 mean equator and equinox specifies a specific point on the celestial sphere on January 1, 2000, 12 hrs. The true of date (TOD) designation identifies the true equator and equinox at a specified date. The J2000.0 equinox is fix ed in space, but the location of the TOD equinox changes with time.

# 2.4.2 EARTH ROTATION AND TIME

In the simplified model of Earth rotation described in Section 2.2.3, the angular velocity vector, $\omega _ { e }$ , is fix ed in direction and magnitude. It has been known since the late 1800s that the direction of this vector does not remain fixed in direction with respect to an Earth-fix ed frame of reference (Seidelmann, 1992). The vector describes a conical counter-clockwise motion, making a complete revolution in about 430 days (known as the Chandler period), but exhibiting an annual variation as well. The combination of Chandler and annual periods results in a six-year variation. Over a decadal time scale, this polar motion is confined to a region around the $z$ axis with a diameter of less than 0.6 arcsec (or $1 8 . 5 \mathrm { ~ m ~ }$ at the Earth’s surface). The components of the angular velocity vector in the $( x , y )$ plane are usually expressed in terms of angular components $( x _ { p } , y _ { p } )$ using a left-handed coordinate system. The $x$ axis of this system is directed along the Greenwich meridian and the $y$ axis is directed toward $9 0 °$ west. These components $( x _ { p } , y _ { p } )$ provide the direction of $\omega _ { e }$ but they cannot be predicted accurately over long periods of time, so they are determined from modern observational techniques (see Chapter 3) and reported by the International Earth Rotation Service (IERS).

In addition to changes that take place in the direction of $\omega _ { e }$ , the magnitude of the vector changes with time. These changes in the magnitude are caused by transfer of angular momentum from atmospheric winds to the solid Earth and by tidal deformations that produce changes in the Earth’s moments of inertia. A change in the angular velocity vector produces a corresponding change in the length of day (LOD), the period required for a complete revolution of the Earth with respect to the stars (but not the Sun). This change in LOD usually is expressed with a parameter using units of time, a form of Universal Time known as $\Delta ( \mathrm { U T } 1 )$ . The variations in LOD, as well as $\Delta ( \mathrm { U T } 1 )$ , are difficult to predict so they are observed regularly and reported by the IERS. In cases that rely on the use of satellite observations, the quantities $x _ { p }$ , $y _ { p }$ , and LOD may be estimated simultanelously with the satellite state.

Although $\Delta ( \mathrm { U T } 1 )$ can, in principle, be estimated with polar motion and satellite state, the separation of $\Delta ( \mathrm { U T } 1 )$ from the orbit node, $\Omega$ , complicates such estimation. Although satellite observations from satellites such as GPS and Lageos have been used to determine both $\Delta ( \mathrm { U T } 1 )$ and $\Omega$ over time scales of a few days, it should be noted that errors in modeling $\Omega$ will be absorbed in the estimation of $\Delta ( \mathrm { U T } 1 )$ . Since modeling the satellite $\Omega$ over very long periods, such as semiannual and longer, is complicated by force model errors from, for example, radiation pressure, artificial satellite observations cannot provide reliable longterm estimates of $\Delta ( \mathrm { U T } 1 )$ .

Time is expressed in different ways. An event can uniquely be identified by the calendar date and time of day, expressed in local time or Universal Time (discussed in a later paragraph). For example, the epoch $J 2 0 O O . O$ is January 1, 2000, 12 hours. The event may be identified by the Julian Date (JD), which is measured from 4713 b.c., but the day begins at noon. The epoch J2000.0 is represented by JD2451545.0. However, January 1, 2000, 0 hours (midnight) is JD 2451544.5. A modified Julian date (MJD) is represented by the JD minus 2400000.5 and the Julian day number is the integral part of the Julian date. Another commonly used expression of time is the day of year (DOY), in which January 1, 2000, would be day 1 of 2000 and February 1, 2000, would be day 32. The general format for the system is DOY followed by hours, minutes, and seconds past midnight.

Time is the independent variable of the equations of motion, Eq. (2.3.46), and the ability to relate the time tag associated with some observation of an aspect of satellite motion to the independent variable is essential for the problem of orbit determination. Observations such as the distance from an instrument to a satellite are described in Chapter 3, but each observation will be time tagged using a reference clock at the tracking station.

A clock requires the repeated recurrence of an event with a known interval. Up until the early part of the twentieth century, the rotation of the Earth served as a clock, but this use was abandoned when evidence mounted that the rotation rate was not uniform. In the modern context, clocks are a particular application of devices that oscillate with specific frequencies. By counting the number of cycles completed over a specified time interval, the oscillator becomes a clock. For example, crystal oscillators abound in modern life (e.g., wristwatches, computers, etc.) The reference frequency of crystal oscillators will change with temperature, for example. Hence, the frequency will exhibit temporal characteristics, usually represented by an offset from “true” time, a drift term and perhaps higher order terms, including stochastic components.

Modern atomic frequency standards, also used as clocks, are classified as rubidium, cesium, and hydrogen maser, given in the order of increasing accuracy and cost. In the case of a cesium frequency standard, a tunable quartz oscillator is used to excite the cesium at the natural frequency of 9,192,631,770 Hz. This frequency is used to define the System International (SI) second. Cesium clocks exhibit high stability, losing about 1 second in 1.5 million years. Hydrogen maser clocks exhibit about an order of magnitude even higher stability.

Various time systems are in use. For Earth satellite applications, the Terrestrial

Table 2.4.1: Difference Between GPS-Time and UTCa   

<table><tr><td colspan="2">Date</td><td>(GPS-T) minus UTC</td></tr><tr><td>(00:00:01 UTC)</td><td></td><td>seconds</td></tr><tr><td>July July 1,</td><td>1, 1981</td><td>1</td></tr><tr><td>July 1,</td><td>1982</td><td>2</td></tr><tr><td>July</td><td>1983</td><td>3</td></tr><tr><td></td><td>1, 1985</td><td>4</td></tr><tr><td> January</td><td>1, 1988</td><td>5</td></tr><tr><td>January</td><td>1, 1990</td><td>6</td></tr><tr><td> January</td><td>1, 1991</td><td>7</td></tr><tr><td>July</td><td>1, 1992</td><td>8</td></tr><tr><td>July July</td><td>1, 1993</td><td>9</td></tr><tr><td></td><td>1, 1994</td><td>10</td></tr><tr><td> January</td><td>1, 1996</td><td>11</td></tr><tr><td>July</td><td>1, 1997</td><td>12</td></tr><tr><td>January</td><td>1, 1999</td><td>13</td></tr></table>

aDates shown are leap second adjustments.

Dynamical Time (TDT) is used as the independent variable in the equations of motion, although Barycentric Dynamical Time (TDB) is used for solar system applications. Both TDT and TDB were related to International Atomic Time (TAI) at a specified epoch. TAI is a time scale based on cesium atomic clocks operated by numerous international agencies. In principle, by averaging over numerous atomic clocks, stochastic variations can be diminished and TAI will be a close approximation of a uniform time scale. TDT has come to be known as Terrestrial Time (TT).

Universal Time is the measure of time that is the theoretical basis for all civil time-keeping. Aside from the previously defined $\Delta ( \mathrm { U T } 1 )$ , Coordinated Universal Time (UTC) is derived from TAI, where $\mathbf { U T 1 } = \mathbf { U T C } + \Delta ( \mathbf { U T 1 } )$ . UTC is maintained by the atomic clocks of various agencies, such as the National Institute of Standards and Time (NIST) and the U.S. Naval Observatory (USNO). The specific time systems are designated UTC(NIST) or UTC(USNO), for example. UTC(USNO) and TAI are based on the ensemble average of several cesium oscillators and hydrogen masers (about 30 cesium and 5–10 hydrogen masers in early 2000). The primary difference between UTC and TAI is the introduction of leap seconds to maintain synchronization between UTC and $\Delta ( \mathrm { U T } 1 )$ to within $\pm 0 . 9$ seconds.

The difference between TAI and TT is, by definition, a constant. The transformation is given by

$$
\mathrm { T T - T A I } = 3 2 . 1 8 4 \mathrm { s e c } .
$$

The transformation between TDB and $\mathrm { T T }$ is a purely periodic function of the position and velocity of the Earth, Moon, planets, and Sun, a relativistic effect. The largest term in this transformation is an annual term with an amplitude of 1.658 milliseconds.

With the introduction of the Global Positioning System (GPS), another time system was introduced. To avoid discontinuities that occur with UTC, GPS-Time (GPS-T) is related to atomic time (maintained by USNO), but the leap second adjustments applied to UTC are not introduced in GPS-T. One of the hydrogen maser clocks at the USNO is used to provide the physical realization of both UTC(USNO) and GPS-T, which is determined from the ensemble average. This clock is steered to UTC(USNO) and is referred to as the Master Clock (MC). The MC is used for both UTC(USNO) and GPS-T. The offsets between GPS-T and UTC are shown in Table 2.4.1. As of January 1, 1999, and until the next leap second, TAI-UTC $= 3 2$ seconds.

In GPS operations, time is measured by GPS-week and time within the week, measured from Sunday midnight. The GPS-week is an integer with the initial week assigned a value of zero, corresponding to January 6, 1980. Since 10 bits were allocated in the GPS broadcast message to the GPS-week, the week number is limited to 1023, which occurred the week of August 15, 1999. After reaching the value of 1023, the week “rolled over” to zero for the week of August 22. Although an ambiguity exists with the uniqueness of the GPS-week as the result of the rollover, resolution of this ambiguity is not a problem for most applications.

References containing more detailed information include Seidelmann (1992) and McCarthy (1996). The latter reference documents the definitions, algorithms, models and constants adopted by the IERS. The document on the “IERS Conventions” is updated every few years.

# 2.4.3 EARTH-FIXED AND TOPOCENTRIC SYSTEMS

Since the Earth is not a rigid body, the concept of an Earth-fix ed reference frame is not precisely defined. As previously noted, the Earth deforms in response to luni-solar gravity, which produces a redistribution of mass. The deformations associated with this redistribution, or tides, produce not only changes in gravity but changes in the coordinates of points on the Earth’s surface. In addition, the Earth’s crust consists of several moving tectonic plates. As a consequence, a relative motion exists between points on different plates. With these considerations, a true Earth-fix ed reference frame does not exist. The selected reference frame must be consistent with the description of the Earth’s rotational characteristics and deformation.

A Terrestrial Reference Frame (TRF) for precision orbit determination is “attached” to the Earth with an origin that is coincident with the center of mass. The $( x , y , z )$ axes are orthogonal and the $z$ axis of this coordinate system is approximately coincident with $\omega _ { e }$ , but it cannot remain coincident because of polar motion. The $x$ axis is usually chosen to be approximately coincident with the Greenwich meridian and the $y$ axis is mutually perpendicular. Specific realizations of the TRF include the IERS TRF, or $I T R F$ , and the TRF commonly used with many GPS applications, referred to as the WGS-84 (World Geodetic System) system. WGS-84 is closely aligned with the ITRF.

With the ITRF, for example, velocities of the observing sites are determined to account for plate motion, including local crustal deformations. To maintain a consistent TRF, these site velocities are determined within a process that defines the ITRF as well as the Earth rotation parameters. ITRF-97 (Boucher et al., 1999) provides the coordinates and velocities for stations participating in the International Space Geodetic Network. The IERS Conventions (McCarthy, 1996) are a useful source of information for the effects of tides on station coordinates.

As defined in Section 2.3.3, spherical coordinates are used to describe the planetary gravitational potential. These spherical coordinates are related to the $( x , y , z )$ coordinates by the following relations:

$$
\begin{array} { r c l } { x } & { = } & { r \cos \phi \cos \lambda } \\ { y } & { = } & { r \cos \phi \sin \lambda } \\ { z } & { = } & { r \sin \phi . } \end{array}
$$

Here the angle $\phi$ is the geocentric latitude, $\lambda$ is the longitude, and $r$ is the magnitude of the position vector, $\mathbf { r }$ . Since an ellipsoid of revolution is a better approximation to the physical topography of the Earth than a sphere, an alternate set of coordinates is used to describe positions on the surface of the ellipsoid, as illustrated in Fig. 2.4.2. This alternate set uses a geodetic latitude, $\phi ^ { \prime }$ , longitude, $\lambda$ , and height above the ellipsoid, $h$ . The relationships between these coordinates and $( x , y , z )$ are

$$
\begin{array} { r c l } { { x } } & { { = } } & { { { \left( N _ { h } + h \right) \cos \phi ^ { \prime } \cos \lambda } } } \\ { { y } } & { { = } } & { { { \left( N _ { h } + h \right) \cos \phi ^ { \prime } \sin \lambda } } } \end{array}
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0002_pages_0071-0140/auto/images/e016a2c5ca3d1d5db55ccef22cdd26223524d5e925dfafeab28aa33724949ce9.jpg)  
Figure 2.4.2: Geodetic coordinates. Coordinates on the surface of the Earth are usually defined in terms of geodetic latitude, $\phi ^ { \prime }$ , which differs from geocentric latitude, $\phi$ .

$$
\begin{array} { l l l } { z } & { = } & { \left( N _ { h } + h - { \tilde { e } } ^ { 2 } N _ { h } \right) \sin { \phi ^ { \prime } } } \end{array}
$$

where eccentricity of the elliptical cross-section of the ellipsoid is

$$
\begin{array} { c } { { \tilde { e } ^ { 2 } = \tilde { f } ( 2 - \tilde { f } ) , } } \\ { { { } } } \\ { { N _ { h } = \displaystyle \frac { R _ { e } } { ( 1 - \tilde { e } ^ { 2 } \sin ^ { 2 } \phi ^ { \prime } ) ^ { 1 / 2 } } } } \end{array}
$$

and $\tilde { f }$ represents the flattening parameter. The parameter $\tilde { f }$ is defined by

$$
\tilde { f } = \frac { R _ { e } - R _ { p } } { R _ { e } } ,
$$

where $R _ { e }$ is the equatorial radius of the ellipsoid, and $R _ { p }$ is its polar radius. Another useful equation for the ellipsoid is

$$
x ^ { 2 } + y ^ { 2 } + \left( { \frac { R _ { e } } { R _ { p } } } \right) ^ { 2 } z ^ { 2 } = R _ { e } ^ { 2 }
$$

where $( x , y , z )$ are coordinates of a point on the ellipsoid surface. Further geodetic details can be found in Torge (1980). This equation can be a useful constraint to determine the location, for example, of the point where a space-borne instrument boresight pierces the ellipsoid for a specified spacecraft orientation in the ECF.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0002_pages_0071-0140/auto/images/739a7da8f44be59da069f8433ea01419172f58d2324e1c094a5340652f584814.jpg)  
Figure 2.4.3: Topocentric coordinates. A useful description of satellite position can be made with topocentric coordinates. The origin is an observer’s position on the surface of the Earth and the topocentric coordinates are defined with $x _ { t }$ directed eastward, $y _ { t }$ northward, and $z _ { t }$ is radial.

For some applications, a coordinate system attached to a point on the surface of the Earth is useful in the description of satellite motion from a ground-based observer’s viewpoint. A topocentric coordinate system can be defined such that $z _ { t }$ is along the local vertical, $x _ { t }$ is eastward, and $y _ { t }$ is northward, as illustrated in Fig. 2.4.3. The position vector of a satellite, for example, in an Earth-fix ed system, $\mathbf { r }$ , can be expressed in the topocentric system as $\mathbf { r } _ { t }$ :

$$
{ \bf r } _ { t } = T _ { t } ( { \bf r } - { \bf r } _ { s } ) = T _ { t } \rho
$$

$$
T _ { t } = \left[ \begin{array} { c c c } { { - \sin \lambda } } & { { \cos \lambda } } & { { 0 } } \\ { { - \sin \phi \cos \lambda } } & { { - \sin \phi \sin \lambda } } & { { \cos \phi } } \\ { { \cos \phi \cos \lambda } } & { { \cos \phi \sin \lambda } } & { { \sin \phi } } \end{array} \right] .
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0002_pages_0071-0140/auto/images/901fd1e4d995be1be6bcaba359a50ae5643599ca393785dbcf10c5dfb8b04ca5.jpg)  
Figure 2.4.4: Azimuth and elevation. These angles are defined in a topocentric system with azimuth measured eastward from north and elevation measured above the plane tangent to the Earth at the observer’s location.

Where geocentric latitude has been used for simplicity, $\mathbf { r }$ and $\mathbf { r } _ { s }$ are the position vectors of the satellite, and the observer is expressed in the Earth-fix ed system. With the components of satellite position expressed in the topocentric system, $( x , y , z ) _ { t }$ , two commonly used angles can be introduced: azimuth (Az) and elevation (El). These angles are illustrated in Fig. 2.4.4 and can be determined from

$$
\begin{array} { r l r } & { \sin ( \mathrm { E l } ) = \displaystyle \frac { z _ { t } } { r _ { t } } \qquad } & { - 9 0 ^ { \circ } \leq \mathrm { E l } \leq 9 0 ^ { \circ } } \\ & { \sin ( \mathrm { A z } ) = \displaystyle \frac { x _ { t } } { r _ { x y } } } \\ & { \cos ( \mathrm { A z } ) = \displaystyle \frac { y _ { t } } { r _ { x y } } } \end{array}
$$

Where $( \mathbf { A } \mathbf { z } )$ is measured from North in an eastward direction, (El) is measured above (or below) the $( x , y ) _ { t }$ plane (that is, the local tangent plane), and $r _ { x y } =$ $[ x _ { t } ^ { 2 } + y _ { t } ^ { 2 } ] ^ { 1 / 2 }$ . Both sin (Az) and cos (Az) are needed to determine the correct quadrant.

# 2.4.4 TRANSFORMATION BETWEEN ECF AND ECI

If the equations of motion given by Eqs. (2.3.46) and (2.3.47) are expressed in an ECI system, such as the J2000 system, the gravitational force given by Eq. (2.3.18) must be transformed from the Earth-fix ed system used to describe the potential into the J2000 system. For the simplified case of simple ECF rotation about the body-fix ed $z$ axis, the necessary transformation was given in Eq. (2.3.20). In reality, with consideration given to precession, nutation, polar motion, and UT1, the transformation is considerably more complex. If T xyzXY Z represents the transformation matrix from J2000 coordinates to Earth-fix ed, then

$$
\left[ \begin{array} { l } { x } \\ { y } \\ { z } \end{array} \right] _ { E C F } = T _ { X Y Z } ^ { x y z } \left[ \begin{array} { l } { X } \\ { Y } \\ { Z } \end{array} \right] _ { E C I }
$$

where the vector components $( X , Y , Z ) _ { E C I }$ represent Earth-centered inertial coordinates (e.g., J2000) and $( x , y , z ) _ { E C F }$ represents the Earth-fix ed components (e.g., ITRF). The transformation matrix can be further decomposed into

$$
T _ { X Y Z } ^ { x y z } = W S ^ { \prime } N P
$$

where the specific components of these matrices and additional details are given in Appendix H. The general purpose of these matrices is

P: applies precession, from a specified epoch to the current time,   
N: applies nutation at the current time,   
$S ^ { \prime }$ : applies the rotation to account for true sidereal time,   
W: applies polar motion to align the $z$ axis (true pole) with the pole of the ECF system.

# 2.5 ORBIT ACCURACY

Different conditions and considerations must be applied to a discussion about orbit accuracy. The term orbit accuracy may refer to the accuracy of the solution of the equations of motion with specified parameters in the model of the forces acting on the satellite. In this case, little consideration is given to the accuracy of the parameters in the equations of motion. Instead the focus is simply on the accuracy of the technique used to solve the nonlinear ordinary differential equations given by Eqs. (2.3.46) and (2.3.47). If a general perturbation technique is used, the concern is usually with the small parameters, such as eccentricity, that are used to expand the forces and facilitate the solution. On the other hand, if a special perturbation technique is used, the concern will be with the step size of the numerical method chosen to solve the equations of motion. In either case, the solution technique is an approximation and will always introduce some error in the solution. To clarify this aspect, the terminology solution technique accuracy refers to the error introduced in the solution of the equations of motion by the solution technique, with no consideration given to the accuracy of the parameters in the equations. The solution technique accuracy can be controlled at different levels. For example, a numerical integration technique can be controlled by the step size and order of the technique.

Since the errors introduced by the solution technique can be controlled at some level, they are seldom the dominant error source. The parameters in the force models as well as the modeling of the forces are usually the most significant error sources. For example, all parameters in the force model have been determined by some means, usually as part of the orbit determination process. As a consequence, all parameters in the equations of motion contain some level of error. Such errors are crucial in the comparison of the solution to the equations of motion to physical measurements of some characteristics of the motion. In some cases, the error source may be embedded in the force modeling. In other words, the force model may be incorrect or incomplete. These errors will be described by the terminology force model accuracy.

In some cases, intentional mismodeling may be introduced to simplify the equations of motion. For example, the simple evaluation of the spherical harmonic terms in the gravitational force will require significantly greater computation time if the representation includes terms to degree and order 180 compared to degree and order 8. In this case, it may be acceptable to introduce a level of spherical harmonic truncation to reduce the computation time, though some error will be introduced into the solution by the omitted terms.

The most important consideration for the orbit accuracy is the specification of a requirement for the accuracy in each application. The requirement may be motivated by a wide variety of considerations, such as sensor accuracy, but the requirement will determine the selection of parameters for the solution technique, the accuracy of the force model parameters, the selection of force models, and the selection of a solution technique. The equations of motion are distinctly different if the orbit of a satellite must be known (and hence determined) with centimeter accuracy versus kilometer accuracy. Depending on these requirements, intentional model simplificat ions may be introduced. Identification of the accuracy to which the orbit must be determined is a vital aspect of the orbit determination problem.

# 2.6 REFERENCES

Barlier, F., C. Berger, J. Falin, G. Kockarts, and G. Thuiller, “A thermospheric model based on satellite drag data,” Annales de Geophysique ´ , Vol. 34, No. 1, pp. 9–24, 1978.

Battin, R., An Introduction to the Mathematics and Methods of Astrodynamics, American Institute of Aeronautics and Astronautics, Reston, VA, 1999.

Beutler, G., E. Brockmann, W. Gurtner, U. Hugentobler, L. Mervart, M. Rothacher, and A. Verdun, “Extended orbit modeling techniques at the CODE Processing Center of the International GPS Service for Geodynamics (IGS): theory and initial results,” Manuscripta Geodaetica, Vol. 19, No. 6, pp. 367–385, April 1994.

Bond, V., and M. Allman, Modern Astrodynamics, Princeton University Press, Princeton, NJ, 1996.

Born, G., J. Mitchell, and G. Hegler, “GEOSAT ERM – mission design,” J. Astronaut. Sci., Vol. 35, No. 2, pp. 119–134, April–June 1987.

Boucher, C., Z. Altamini, and P. Sillard, The International Terrestrial Reference Frame (ITRF97), IERS Technical Note 27, International Earth Rotation Service, Observatoire de Paris, May 1999.

Brouwer, D., “Solutions of the problem of artificial satellite theory without drag,” Astron. J., Vol. 64, No. 9, pp. 378–397, November 1959.

Brouwer, D., and G. Clemence, Methods of Celestial Mechanics, Academic Press, New York, 1961.

Chobotov, V. (ed.), Orbital Mechanics, American Institute of Aeronautics and Astronautics, Inc., Reston, VA, 1996.

Cook, G. E., “Perturba tions of near-circular orbits by the Earth’s gravitational potential,” Planetary and Space Science, Vol. 14, No. 5, pp. 433–444, May 1966.

Danby, J. M. A., Fundamentals of Celestial Mechanics, Willmann-Bell, Inc., Richmond, VA, 1988.

Einstein, A., “Zur Elektrodynamik bewegter Korper,” ¨ Annalen der Physik, Vol. 17, No. 10, pp. 891–921, 1905 (translated to English: Perrett, W., and G. Jeffery, The Principle of Relativity, Methuen and Co., 1923; republished by Dover, New York).

El´Yasberg, P. E., Introduction to the Theory of Flight of Artificial Earth Satellites, translated from Russian, Israel Program for Scientific Translations, 1967.

Fliegel, H., T. Gallini, and E. Swift, “Global Positioning System radiation force models for geodetic applications,” J. Geophys. Res., Vol. 97, No. B1, 559– 568, January 10, 1992.

Goodyear, W. H., “Complet ely general closed form solution for coordinates and partial derivatives of the two-body problem,” Astron. J., Vol. 70, No. 3, pp. 189–192, April 1965.

Heiskanen, W., and H. Moritz, Physical Geodesy, W. H. Freeman and Co., San Francisco, 1967.

Herring, T., B. Buffett, P. Mathews, and I. Shapiro, “Free nutations of the Earth: influence of inner core dynamics,” J. Geophys. Res., Vol. 96, No. B5, pp. 8259–8273, May 10, 1991.

Huang, C., J. C. Ries, B. Tapley, and M. Watkins, “Rel ativistic effects for near-Earth satellite orbit determination,” Celest. Mech., Vol. 48, No. 2, pp. 167– 185, 1990.

Jacchia, L., Thermospheric temperature, density and composition: new models, Special Report 375, Smithsonian Astrophysical Observatory, Cambridge, MA, 1977.

Kaula, W. M., Theory of Satellite Geodesy, Blaisdell Publishing Co., Waltham, 1966 (republished by Dover, New York, 2000).

Kovalevsky, J., I. Mueller, and B. Kolaczek (eds.), Reference Frames in Astronomy and Geophysics, Kluwer Academic Publishers, Dordrecht, 1989.

Lambeck, K., The Earth’s Variable Rotation, Cambridge University Press, Cambridge, 1980.

Lambeck, K., Geophysical Geodesy, Clarendon Press, Oxford, 1988.

Lundberg, J., and B. Schutz, “Recursion formulas of Legendre functions for use with nonsingular geopotential models,” J. Guid. Cont. Dyn., Vol. 11, No. 1, pp. 31–38, January–Februar y 1988.

McCarthy, D. (ed.), IERS Conventions (1996), IERS Technical Note 21, International Earth Rotation Service, Observatoire de Paris, July 1996.

Moritz, H., and I. Mueller, Earth Rotation: Theory and Observation, Ungar Publishing Company, New York, 1987.

Moulton, F. R., An Introduction to Celestial Mechanics, MacMillan Co., New York, 1914.

Newton, I., Philosophiae Naturalis Principia Mathematica, 1687 (translated into English: A. Motte, 1729; revised by F. Cajori, University of California Press, 1962).

Pines, S., “Uniform representation of the gravitational potential and its derivatives,” AIAA J., Vol. 11, No. 11, pp. 1508–1511, November 1973.

Plummer, H. C., An Introductory Treatise on Dynamical Astronomy, Cambridge University Press, 1918 (republished by Dover Publications, New York, 1966).

Pollard, H., Mathematical Introduction to Celestial Mechanics, Prentice-Hall, Englewood Cliffs, NJ, 1966.

Press, W., B. Flannery, S. Teukolsky, and W. Vetterling, Numerical Recipes, Cambridge University Press, Cambridge, 1986.

Prussing, J., and B. Conway, Orbit Mechanics, Oxford University Press, New York, 1993.

Ries, J. C., C. K. Shum, and B. Tapley, “Surf ace force modeling for precision orbit determination,” Geophysical Monograph Series, Vol. 73, A. Jones (ed.), American Geophysical Union, Washington, DC, 1993.

Ries, J. C., C. Huang, M. M. Watkins, and B. D. Tapley, “Orbit determination in the relativistic geocentric reference frame,” J. Astronaut. Sci., Vol. 39, No. 2, pp. 173–181, April–June 1991.

Roy, A. E., Orbital Motion, John Wiley & Sons Inc., New York, 1988.

Schaub, H., and J. Junkins, Analytical Mechanics of Space Systems, American Institute of Aeronautics and Astronautics, Reston, VA, 2003.

Seidelmann, P. K. (ed.), Explanatory Supplement to the Astronomical Almanac, University Science Books, Mill Valley, CA, 1992.

Shampine, L., and M. Gordon, Computer Solution of Ordinary Differential Equations, The Initial Value Problem, W. H. Freeman and Co., San Francisco, 1975.

Smart, W. M., Celestial Mechanics, John Wiley & Sons Inc., New York, 1961.

Standish, E. M., X. Newhall, J. Williams, and W. Folkner, JPL Planetary and Lunar Ephemerides (CD-ROM), Willmann-Bell, Inc., Richmond, VA, 1997.

Szebehely, V., Theory of Orbits, Academic Press, New York, 1967.   
Szebehely, V., and H. Mark, Adventures in Celestial Mechanics, John Wiley & Sons, Inc., New York, 1998.   
Torge, W., Geodesy, Walter de Gruyter, Berlin, 1980 (translated to English: Jekeli, C.).   
Vallado, D., Fundamentals of Astrodynamics and Applications, Space Technology Library, Microcosm Press, El Segundo, CA, 2001.   
Vigue, Y., B. Schutz, and P. Abusali, “Thermal force modeling for the Global Positioning System satellites using the finite element method,” J. Spacecr. Rockets, Vol. 31, No. 5, pp. 866–859, 1994.   
Wahr, J. M., “The forced nutations of an elliptical, rotating, elastic, and oceanless Earth,” Geophys. J. of Royal Astronom. Soc., 64, pp. 705–727, 1981.   
Westfall, R., Never at Rest: A Biography of Isaac Newton, Cambridge University Press, Cambridge, 1980.   
Woolard, E., Theory of the rotation of the Earth around its center of mass, Astronomical Papers—American Ephemeris and Nautical Almanac, Vol. XV, Part I, U.S. Naval Observatory, Washington, DC, 1953.

# 2.7 EXERCISES

1. By differentiating ${ \mathbf { r } } = r { \mathbf { u } } _ { r }$ , derive Eqs. (2.2.8) and (2.2.9). Recall that the derivative of a unit vector in a rotating frame is given by $\dot { \mathbf { u } } = \boldsymbol { \omega } \times \mathbf { u }$ , where $\omega$ is the angular velocity of the rotating frame. In this case, $\omega = { \dot { \theta } } \mathbf { u } _ { h }$ .

2. Determine the orbital period of the following satellites:

(a) Shuttle: $a = 6 , 7 7 8 \mathrm { k m }$ (b) Earth-observing platform (EOS/Terra): $a = 7 , 0 8 3 \mathrm { k m }$ (c) Geodetic satellite (Lageos): $a = 1 2 , 3 0 0 \mathrm { k m }$

3. Determine the semimajor axis from the period for the following:

(a) Geosynchronous $( T = 8 6 , 1 6 4 \mathrm { s e c }$ ) (b) GPS $( T = 8 6 , 1 6 4 / 2$ sec)

4. Given the following position and velocity of a satellite expressed in a nonrotating, geocentric coordinate system:

<table><tr><td></td><td>Position (m)</td><td>Velocity (m/sec)</td></tr><tr><td>X</td><td>7088580.789</td><td>-10.20544809</td></tr><tr><td>Y</td><td>-64.326</td><td>-522.85385193</td></tr><tr><td>Z</td><td>920.514</td><td>7482.07514112</td></tr></table>

Determine the six orbit elements (a, e, i, $\Omega , \omega , \mathbf { M } _ { 0 } ,$ ). Express the angles in degrees.

5. Given the position and velocity in Exercise 4 at $t = 0$ , predict the position and velocity of the satellite at $t = 3 , 0 0 0$ sec, assuming two-body motion. Determine the radial and horizontal components of velocity and the flight path angle at $t = 3 , 0 0 0$ sec. The flight path angle is the angle in the orbit plane between the normal to the position vector and the velocity vector.

6. Determine the latitude and longitude of the subsatellite point for $t = 3 , 0 0 0$ sec in Exercise 5 if $\alpha _ { G }$ at $t = 0$ is zero. Assume the $Z$ axis of the nonrotating system is coincident with the $z$ axis of the rotating system.

7. Determine the node rate and perigee rate due to $J _ { 2 }$ of the Earth for the following satellites:

<table><tr><td>Satellite</td><td>Altitude</td><td>Eccentricity</td><td>Inclination</td></tr><tr><td>Mir</td><td>400 km</td><td>0</td><td>51 deg</td></tr><tr><td>EOS/AM</td><td>705 km</td><td>0</td><td>98 deg</td></tr><tr><td>GPS</td><td>20,000 km</td><td>0</td><td>55 deg</td></tr><tr><td>Geosync</td><td>36,000 km</td><td>0.1</td><td>63 deg</td></tr></table>

(Assume semimajor axis is altitude $^ +$ mean radius of Earth.)

8. Determine the inclination required for a “solar -synchronous” satellite with an altitude of $6 0 0 { \mathrm { k m } }$ (add Earth radius to obtain semimajor axis) and zero eccentricity.

9. Determine the node rate caused by the Sun and Moon for the set of satellites in Exercise 7. Determine the individual luni-solar contributions and the combined effect.

10. In November, 1996, a payload known as Wakeshield (WSF-03) was deployed from Columbia on STS-80. This payload carried a GPS receiver. Using an on-board navigation method, the receiver measurements were processed into position in an Earth-centered, Earth-fix ed coordinate system. The GPS-determined positions for selected times follow.

<table><tr><td colspan="2">WSF-O3 Earth-fx ed Position Determined by GPS WGS-84 Positions in Meters November 24,1996</td><td rowspan="2">00:00:03.000000</td></tr><tr><td>GPS-T (hrs:min:sec)</td><td>00:00:0.000000</td></tr><tr><td>x</td><td>3325396.441</td><td>3309747.175</td></tr><tr><td>y</td><td>5472597.483</td><td>5485240.159</td></tr><tr><td>2</td><td>-2057129.050</td><td>-2048664.333</td></tr><tr><td></td><td></td><td></td></tr><tr><td colspan="3">November 25,1996</td></tr><tr><td>GPS-T (hrs:min:sec)</td><td>00:00:0.000000</td><td>00:00:03.000000</td></tr><tr><td>x</td><td>4389882.255</td><td>4402505.030</td></tr><tr><td>y</td><td>-4444406.953</td><td>-4428002.728</td></tr><tr><td>2</td><td>-2508462.520</td><td>-2515303.456</td></tr></table>

(a) Use these positions to demonstrate that the WSF-03 node location is not fixed in space and determine an approximate rate of node change (degrees/day) from these positions. Compare the node rate with the value predicted by Eq. (2.3.31). (Hint: Determine the node location in the first 3 sec and the last 3 sec. Also, recall that for two-body dynamics, the position vectors at two times will define the orbit plane.)

(b) Determine the inclination of WSF-03 during the first 3-sec interval and the last 3-sec interval. (Hint: Assume two-body dynamics applies during these respective 3-sec intervals.)

Comment: The position vectors determined by GPS in this case are influenced at the 100-meter level by Selective Ability, but the error does not significantly affect this problem.

11. Assuming an Earth satellite is influenced by $J _ { 2 }$ only, derive the equations of motion in nonrotating coordinates. Assume the nonrotating $Z$ axis coincides with the Earth-fix ed $z$ axis.

12. Using the result of Exercise 11, numerically integrate the equations of motion for one day with the following initial conditions for a high-alititude, GLONASS-like satellite:

a 25500.0 km e 0.0015 i 63 deg $\Omega$ −60 deg $\omega$ 0 deg ${ { \bf { M } } _ { 0 } }$ 0 deg

(a) During the integration, compute the Jacobi constant and the $Z$ component of the angular momentum. Are these quantities constant?   
(b) Plot the six orbit elements as a function of time.   
(c) Identify features that are similar to and different from Fig. 2.3.5 for the Shuttle.   
(d) Compare the node rate predicted by Eq. (2.3.31) with a value estimated from (b).   
(e) Compare the amplitude of the semimajor axis periodic term with Eq. (2.3.34).   
(f) Plot the ground track. Does the ground track repeat after one day?

13. Using Fig. 2.3.5, estimate the mean values of $a , e$ , and $i$ and the linear rates of node and perigee change. Compare the estimated node and perigee rates with the rates predicted by Eqs. (2.3.31) and (2.3.32).

14. For the orbit of the TOPEX/Poseidon, assume the ECF frame rotates with a constant rate $\omega _ { e }$ about the $z$ axis and the initial osculating elements are:

$$
\begin{array} { l l l } { { a } } & { { } } & { { 7 7 1 2 \mathrm { k m } } } \\ { { e } } & { { } } & { { 0 . 0 0 0 1 } } \\ { { i } } & { { } } & { { 6 3 . 4 ^ { \circ } } } \\ { { \Omega } } & { { } } & { { 1 3 5 ^ { \circ } } } \\ { { \omega } } & { { } } & { { 9 0 ^ { \circ } } } \\ { { M _ { 0 } } } & { { 0 } } & { { } } \end{array}
$$

(a) Use the $J _ { 2 }$ result of Exercise 11 to numerically integrate the equations of motion for one day.   
(b) Compare the numerical results with results from the analytical theory in Appendix E. Note that errors in the analytical theory are of the order $e J _ { 2 }$ and $J _ { 2 } ^ { 2 }$ .

15. Using the gravitational potential in Eq. (2.3.12), derive

$$
{ \frac { \partial U } { \partial r } } , \quad { \frac { \partial U } { \partial \phi } } , \quad \mathrm { a n d } \ { \frac { \partial U } { \partial \lambda } } .
$$

Derive a recursive relation for

$$
\frac { \partial P _ { \ell m } } { \partial \phi } .
$$

16. With the initial conditions from Exercise 12 or 14, derive the equations of motion in both the ECF and ECI with all gravity coefficient s through degree and order 3. Numerically integrate for 10 days both ECF (Eq. 2.3.22) and ECI (Eq. 2.3.23) and compute the Jacobi integral for both cases. Assume the Earth rotates with constant angular velocity (neglect polar motion, $\Delta$ (LOD), precession, and nutation). Assume the Greenwich meridian coincides with the vernal equinox at $t = 0$ .

(a) Assess the numerical integration accuracy from the Jacobi integral. (b) Compare the ECF and ECI position results by applying an appropriate transformation into a common coordinate system.

17. Determine the contributions from the Moon and the Sun to the precession of the equinoxes using Eq. 2.4.2. Compare the combined luni-solar rate with the observed rate of $- 5 0 . 2 5$ arcsec/yr. Note that the polar moment of inertia of the Earth is $8 . 1 2 \times 1 0 ^ { 4 4 } ~ \mathrm { g ~ c m ^ { 2 } }$ , the semimajor axis of the Moon’s orbit is $3 8 4 , 0 0 0 \ \mathrm { k m }$ , and for the Sun $a = 1 4 9 , 5 9 9 , 0 0 0 { \mathrm { k m } }$ $\sim 1$ Astronomical Unit).

18. Determine the secular change in semimajor axis (in m per day) for a balloonlike satellite $( A / m = 1 0 ~ \mathrm { m ^ { 2 } ~ k g ^ { - 1 } } ,$ ) at an altitude of $6 0 0 ~ \mathrm { k m }$ , with atmospheric density $\rho = 5 \times 1 0 ^ { - 1 3 } \mathrm { k g \ m ^ { - 3 } }$ . Compare the result to a geodetic satellite with $A / m = 0 . 0 0 1 { \mathrm { m } } ^ { 2 } { \mathrm { k g } } ^ { - 1 }$ . Assume $C _ { D } = 2$ for both cases.
