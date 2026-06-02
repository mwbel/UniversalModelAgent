Given the vector field $\mathbf { F } ( \mathbf { x } )$ defined above, the differential equation

$$
\frac { d \mathbf { x } } { d \sigma } = \mathbf { F } ( \mathbf { x } )
$$

has a unique solution for each initial condition, because the vector field is smooth. If a nominal solution $\mathbf { x } ^ { * }$ has been found, let us select the initial condition $\mathbf { x } ( 0 ) = \mathbf { x } ^ { * }$ , that is $\sigma = 0$ corresponds to the nominal solution, and let us denote with $\mathbf { x } ( \sigma )$ the unique solution with such initial value. In the linear approximation, the solution $\mathbf { x } ( \sigma )$ is one tip of the major axis of the confidence ellipsoid $Z _ { L } ( \sigma )$ . Without approximations $\mathbf { x } ( \sigma )$ is indeed curved and can be computed by numerical integration of the differential equation.

This approach could be used to define a special curve in the initial conditions space. However, such a definition may not be a constructive one, because of two problems. First, the definition cannot be used unless the nominal solution $\mathbf { x } ^ { * }$ is known. Second, there is a numerical instability in the algorithm to compute it. As an intuitive analogy, for weakly determined orbits the graph of the target function is like a very steep valley with an almost flat river bed at the bottom. The river valley is steeper than any canyon you can find on Earth; so steep that a very small deviation from the stream line sends you up the valley slopes by a great deal. This problem cannot be efficiently solved by brute force, that is by increasing the order or decreasing the step-size in the numerical integration of the differential equation. The only way is to slide down the steepest slopes until the river bed is reached again, which is the intuitive analog of the definition below.

# Constrained differential corrections

Where the vector field $\mathbf { v } _ { 1 } ( \mathbf { x } )$ is defined, the orthogonal hyperplane $H ( \mathbf { x } )$ i s

$$
H ( \mathbf { x } ) = \{ \mathbf { y } \mid ( \mathbf { y } - \mathbf { x } ) \cdot \mathbf { v } _ { 1 } ( \mathbf { x } ) = 0 \} .
$$

Given an initial guess $\mathbf { x }$ , it is possible to compute one step of the differential corrections constrained to $H ( \mathbf { x } )$ by defining the $5 \times m$ matrix $B _ { \mathbf { h } } ( \mathbf { x } )$ with the partial derivatives of the residuals with respect to the coordinates of the vector $\mathbf { h }$ of $H ( \mathbf { x } )$ . Then the constrained normal equation is defined by the constrained normal matrix $C _ { \mathbf { h } }$ , which gives the restriction of the linear map associated to $C$ to the hyperplane $H ( \mathbf { x } )$ , and by the right-hand side $D _ { \mathbf { h } }$ , which is the projection of the vector $D$ along the hyperplane:

$$
C _ { \bf h } = B _ { \bf h } ^ { T } B _ { \bf h } , ~ D _ { \bf h } = - B _ { \bf h } ^ { T } \pmb { \xi } , ~ C _ { \bf h } \Delta \bf h = D _ { h }
$$

with solution

$$
\Delta { \bf h } = \Gamma _ { \bf h } D _ { \bf h } , \Gamma _ { \bf h } = C _ { \bf h } ^ { - 1 }
$$

where the constrained covariance matrix $\Gamma _ { \mathbf { h } }$ is not the restriction of the covariance matrix $\Gamma$ to the hyperplane (see Section 5.4). The computation of $C _ { \mathbf { h } }$ , $D _ { \mathbf { h } }$ can be performed by means of a rotation to a basis with $\mathbf { v } _ { 1 } ( \mathbf { x } )$ as the first vector; then $C _ { \mathbf { h } }$ is obtained by removing the first row and the first column of $C$ , $D _ { \mathbf { h } }$ by removing the first coordinate from $D$ .

The constrained differential corrections process gives the corrected $\mathbf { x } ^ { \prime } =$ $\mathbf { x } + \Delta \mathbf { x }$ where $\Delta \mathbf { x }$ coincides with $\Delta H$ along $H ( \mathbf { x } )$ and has zero component along $\mathbf { v } _ { 1 } ( \mathbf { x } )$ . Then the weak direction $\mathbf { v } _ { 1 } ( \mathbf { x } ^ { \prime } )$ and the hyperplane $H ( \mathbf { x } ^ { \prime } )$ are recomputed, and the next correction is constrained to $H ( \mathbf { x } ^ { \prime } )$ . This procedure is iterated until convergence.2 At the convergence value $\bar { \bf x }$ , $D _ { \mathbf { h } } ( \overline { { \mathbf { x } } } ) = \mathbf { 0 }$ , that is the right-hand side $D ( { \overline { { \mathbf { x } } } } )$ of the unconstrained normal equation is parallel to the weak direction $\mathbf { v } _ { 1 } ( \overline { { \mathbf { x } } } )$ . This equation is equivalent to the following property: the restriction of the target function to the hyperplane $H ( { \overline { { \mathbf { x } } } } )$ has a stationary point in $\overline { { \mathbf { x } } }$ . The constrained corrections correspond to the intuitive idea of “falling down to the river”.

Thus we can define the line of variations (LOV) as the set

$$
\{ \mathbf { x } \mid D ( \mathbf { x } ) = s \mathbf { v } _ { 1 } ( \mathbf { x } ) { \mathrm { ~ f o r ~ s o m e ~ } } s \in \mathbb { R } \} ,
$$

where the gradient of the target function is in the weak direction; if there is a nominal solution $\mathbf { x } ^ { * }$ with $D ( \mathbf { x } ^ { * } ) = 0$ , it also belongs to the LOV. However, the LOV is defined independently of the existence of a local minimum of the target function. The definition by eq. (10.3) does not give the same curve as that resulting from the solutions of eq. (10.2), unless the problem is linear. For a discussion of different possible definitions of LOV, see (Milani et al. 2005c, Appendix A).

# Parameterizing and sampling the LOV

The equation $D ( \mathbf { x } ) = s \mathbf { v } _ { 1 } ( \mathbf { x } )$ corresponds to five scalar equations in six unknowns, thus it has generically a smooth one-parameter set of solutions, i.e., a differentiable curve. However, we have an analytical expression neither for the points of this curve nor for its parameterization (e.g., by the arc length).

An algorithm to compute the LOV by continuation from one of its points $\mathbf { x }$ is the following. The vector field $\mathbf { F } ( \mathbf { x } )$ , deduced from the weak direction vector field $\mathbf { v } _ { 1 } ( \mathbf { x } )$ , is orthogonal to $H ( \mathbf { x } )$ . A step in the direction of $\mathbf { F } ( \mathbf { x } )$ , such as an Euler step of the solution of the differential equation $d \mathbf { x } / d \sigma = \mathbf { F } ( \mathbf { x } )$ , that is $\mathbf { x } ^ { \prime } = \mathbf { x } + \delta \sigma \mathbf { F } ( \mathbf { x } )$ , does not provide another point on the LOV, unless the LOV itself is a straight line; this does not depend on the method employed to find a numerical solution of the differential equations (we normally use a second-order implicit Runge–Kutta–Gauss). However, $\mathbf { x } ^ { \prime }$ will be close to another point $\mathbf { x } ^ { \prime \prime }$ on the LOV, which can be obtained by applying the constrained differential corrections algorithm, starting from $\mathbf { x } ^ { \prime }$ and iterating until convergence, as shown in Figure 10.1.

![](images/7356c60426347e5f0ad2e166c751c6eb553cd20473c30af78c2a50bf72a5026c.jpg)  
Fig. 10.1. The procedure to obtain multiple solutions; only two steps are shown pro jected onto the $( a , e )$ plane. Top: starting from $\mathbf { x } ^ { * }$ (circle), the LOV solutions are obtained by propagation of eq. (10.2) followed by constrained differential corrections (each iteration is a cross); they converge to the “river” (continuous line), whose points have been computed by the same procedure with a much smaller step. Bottom: the RMS of the residuals is large at the starting point of each constrained differential corrections procedure, and rapidly converges towards the much smaller values obtained along the “river” line (circles). Reprinted from (Milani 1999) with permission from Elsevier.

If the LOV parameter of the starting point $\mathbf { x }$ is $\sigma _ { 0 }$ , we can set $\mathbf { x } ^ { \prime \prime } =$ $\mathbf { x } ( \sigma _ { 0 } + \delta \sigma )$ , which is an approximation (the value $\sigma _ { 0 } + \delta \sigma$ actually pertains to $\mathbf { x } ^ { \prime }$ ). As an alternative, if we already know the nominal solution $\mathbf { x } ^ { * }$ and the local minimum value of the target function $Q ( \mathbf { x } ^ { * } )$ , we can compute the $\chi$ parameter as a function of the value of the target function at $\mathbf { x } ^ { \prime \prime }$ by $\chi = \sqrt { m \cdot [ Q ( { \bf x } ^ { \prime \prime } ) - Q ( { \bf x } ^ { * } ) ] }$ . In the linear regime, the two definitions are related by $\sigma = \pm \chi$ , but this is by no means the case in strongly nonlinear conditions. Thus we can adopt the definition $\sigma _ { Q } = \pm \chi$ , where the sign is taken to be the same as that of $\sigma$ , for an alternative parameterization of the LOV. If we assume that the probability density at the initial conditions $\mathbf { x }$ is an exponentially decreasing function of $\chi$ , as in the Gaussian distributions of Chapter 3, then it is logical to terminate the sampling of the LOV at some value of $\chi$ , that is, to use the intersection of the LOV with the nonlinear confidence region $Z ( b )$ , where $b$ is the maximum $\chi$ value.

This algorithm to compute the LOV can be used when a nominal solution $\mathbf { x } ^ { * }$ is known and when it is unknown, even non-existent. If $\mathbf { x } ^ { * }$ is known, then we can set $\mathbf { x } ^ { * } = \mathbf { x } ( 0 )$ as the origin of the parameterization and proceed by using either $\sigma$ or $\sigma _ { Q }$ as parameters for the other points computed with the alternating sequence of numerical integration steps and constrained differential corrections. Else, when a nominal solution is not available, we must first reach some point on the LOV by constrained differential corrections starting from some initial condition (a preliminary orbit). Once on the LOV, we can begin moving along it as was done from the nominal solution. In such cases, we set the LOV origin ${ \bf x } ( 0 )$ to whatever point $\overline { { \mathbf { x } } }$ of the LOV we have found first. Then we compute the other points as above and use the parameterization $\sigma$ with arbitrary origin. The parameterization $\sigma _ { Q }$ cannot be computed point by point: it can be derived a posteriori.

# 10.2 Applications of the constrained solutions

There are two classes of applications. First, a single LOV solution can be used as intermediary for further orbit determination (or for identification). This may stabilize the procedure of orbit determination and/or identification, allowing us to increase its efficiency. Second, multiple solutions sampling the LOV can be computed in the attempt of representing all the possible orbits within some confidence region. For example, $2 p + 1$ LOV solutions $\mathbf { x } _ { k }$ can be computed, with $- p \leq k \leq p$ , with $\mathbf { x } _ { 0 }$ the nominal solution if available, and with a fixed step $\Delta \sigma$ in the $\sigma$ LOV parameter between two consecutive ones. Possibly the most important application of confidence region sampling along the LOV is impact monitoring, discussed in Chapter 12.

# Orbit determination

A procedure for computing an orbit from the astrometric data, by the methods of this and the previous chapter, consists of the following steps, depending upon the quality control parameter $\Sigma$ to be selected:

(i) if no orbit is already available, compute a preliminary orbit $\mathbf { x }$ with either the Gauss method or with the methods of Chapter 8;   
(ii) compute constrained differential corrections by using $\mathbf { x }$ as first guess;   
(iii) if constrained differential corrections converge to a LOV solution $\bar { \bf x }$ (with RMS of the residuals $\leq w \Sigma$ , for some margin $w > 1$ ), then attempt differential corrections by using $\overline { { \mathbf { x } } }$ as first guess;   
(iv) if the full differential corrections converge to a nominal solution $\mathbf { x } ^ { * }$ (with RMS of the residuals $\leq \Sigma$ ) then adopt this as orbit, with uncertainty described by its covariance;   
(v) if the full differential corrections fail, then adopt $\overline { { \mathbf { x } } }$ as orbit if it has RMS $\leq \Sigma$ ;3   
(vi) if the constrained differential corrections fail to converge, attempt full differential corrections with the preliminary orbit $\mathbf { x }$ as first guess.

After obtaining a least squares orbit, be it a nominal or just a LOV solution, we can apply the continuation algorithm of the previous section for multiple LOV solutions. By this procedure, it is possible to obtain a significantly larger number of orbits, which can be the starting point for the applications which follow; this increase results from

LOV solutions in case nominal solutions are not available;   
nominal solutions computed starting from LOV orbits, when the iterations starting from the preliminary orbits diverge;   
multiple LOV solutions computed from the nominal ones;   
multiple LOV solutions computed from one of them, without a nominal.

# Multiple ephemerides and recovery

Sampling along the LOV is a very useful tool when the predictions have a large uncertainty and are extremely nonlinear. This happens when the confidence region is very large, either at the initial epoch (because of very limited observational data) or at some subsequent time, after the propagation has stretched the confidence region preferentially in the along-track direction, as it is already clear from the model problem of Section 5.6.

A typical use of multiple solutions is to compute observation predictions, that is ephemerides. For each observation epoch $t$ , we can compute the $2 p + 1$ points $\mathbf { y } _ { k } = F ( \mathbf { x } _ { k } ( t ) )$ on the celestial sphere, and plot the line joining these points, as in Figure 10.2. This method (Milani 1999) is comparable to that of the semilinear confidence boundary when the orbit determination at an epoch near the observations is quasi-linear, but can work even for orbits which are very poorly determined at all times. This method has been found useful to search for precoveries in plate archives (Boattini et al. 2001).

![](images/109d231f7d68ad2299cb43ebcfafdf1233c60dbb5d854d7507dbb37ed436fc31.jpg)  
Fig. 10.2. Multiple solutions for the asteroid 1992 BU give multiple ephemerides 31 years before, when 4161 PLS was discovered. The actual observation of 4161 PLS is marked with a cross. Reprinted from Milani (1999) with permission from Elsevier.

# Multiple orbit identification

Identifications could be achieved by comparing multiple solutions for two asteroids, observed during short and widely separated arcs. As an example, in Figure 10.3 we show the already mentioned case of $4 1 6 1 ~ \mathrm { P L S } = 1 9 9 2$ BU studied in this way. The two curves, plotted in the $( a , e )$ plane (the inclination and node are typically better determined), are the multiple solutions computed for both single opposition orbits (the gaps correspond to the nominal). The two lines cross in only one point; we select, among the multiple solutions computed, the two which are closest to this intersection point. From them by the linear identification formula (7.1) we compute the first guess for the least squares fit to all the observations of both arcs; the differential corrections converge to an orbit, shown with a cross.

A better method computes orbit identification penalties from (7.2) for each couple of multiple solutions, finds the minimum of the $( 2 p + 1 ) ^ { 2 }$ penalties, for a given couple of objects, and proposes the couple as identification if this minimum is below some control value. An effective method requires us to reduce the computational complexity for $N$ objects below $\mathcal { O } ( N ^ { 2 } ( 2 p + 1 ) ^ { 2 } )$ .

![](images/a065e6c5bd3b6b0430e43947ef4b1a9bad5f2e64e12c2d897cdd6b7d9642b28b.jpg)  
Fig. 10.3. Multiple solutions (up to $\sigma = 3$ ) for the asteroids 4161 PLS and 1992 BU: the projections of the LOV on the $( a , e )$ plane have a single intersection point which is close to the least squares fit (with the observations of both arcs). These two asteroids could have been identified by this method, although they were actually identified with a different procedure (Sansaturio et al. 1996). Reprinted from Milani (1999) with permission from Elsevier.

Milani et al. (2005c, Section 5) discuss the systematic application of this class of methods to a large data set of asteroid orbits, with considerable success ( $\simeq 1 5 0 0$ confirmed identifications found in a single run).

# Recursive attribution

In the linkage problem, after computing the preliminary orbits, e.g., with the methods of Section 8.5 and/or those of Section 8.6, the next step is to compute, starting from the preliminary orbits, least squares solutions. However, in most cases the observational data available are very limited even after the identification, e.g., just enough to compute two attributables. Thus constrained differential corrections are necessary as the first step, and in most cases the LOV solutions are the only ones achievable.

Figure 10.4 summarizes a hypothetical procedure of linkage for the Centaur (31824) Elatus: it was discovered in October 1999, given the designation 1999 UG $5$ , and then followed up until a good orbit could be computed, allowing us to attribute to it prediscovery observations from October 1998. The test consists in linking the data from the discovery night with the precovery data one year earlier, with the methods of Section 8.5. The figure shows the admissible region computed from the October 1999 attributable and the

![](images/761aa3e2595678e8bdd7249d3f7e50a7ae4974462d1b63e477d6adbba837cb15.jpg)  
Fig. 10.4. (31824) For $1 9 9 9 \ \mathrm { U G } _ { 5 }$ , linkage of the four discovery observations with one night of data one year earlier. The continuous lines join the nodes with identification penalty $K ^ { i } \ < \ 5 ^ { 2 }$ : none of them belongs to the first connected component of the admissible region, the one closer to the Earth. The nominal least squares solution, marked “best”, is a hyperbolic orbit: it is not close to the true solution, which is marked with a crossed square near the node number 10. The LOV has been approximated by a straight line best fitting all the LOV points obtained in this way. Reprinted from Milani et al. (2005a) with permission from Elsevier.

Delaunay triangulation to create a swarm of virtual asteroids, with the same conventions as Figure 8.5. The nodes for which the attribution penalty is below some control have been used to compute preliminary orbits, in turn used as a first guess of constrained differential corrections: the points in the $( \rho , \dot { \rho } )$ plane corresponding to the LOV solutions fit well to a straight line. The LOV also contains a nominal solution, which is hyperbolic: it has been computed by using Cartesian coordinates; it would not exist in Keplerian/equinoctial elements. Then the LOV solutions have been used to attribute another one-night arc from September 14, 1999, and this provides a three-night full least squares solution, marked with a crossed square in the figure, which is very close to the line fitting the LOV, not close to the two-night nominal solution.

The above example is extreme, with a very long time span between the first two attributables. Thus it is a strong confirmation of the feasibility of recursive attribution, by which the data from single nights, providing attributables, are added one by one. The procedure starts from linkage, which in fact, with the virtual asteroids method, is also an attribution.

# Qualitative analysis

The sampling along the LOV is also useful to understand the situation whenever the orbit determination is extremely nonlinear. The problem of nonlinearity in orbit determination is too complex to be discussed in full generality here. We shall show the use of the LOV sampling as a tool to understand the geometry of the nonlinear confidence region in a single case study, in which there are multiple local minima of the target function.

The asteroid 1998 XB was discovered in December 1998, at an elongation $\simeq 9 3 ^ { \circ }$ from the Sun. The first orbit published by the Minor Planet Center, with observation time span $\Delta t \simeq 1 0$ days, had $a = 1 . 0 2 1$ AU. In the following days the orbit was repeatedly revised by the MPC, with semimajor axis gradually decreasing to 0.989 AU for $\Delta t \simeq 1 3$ days. Then, with observations extending $\Delta t$ to 16 days, the semimajor axis jumped to 0.906 AU.

![](images/c38a558b130fc8b19ce794db536fba2a4432a97cf9d12fc595f3ed0f63a30a09.jpg)  
Fig. 10.5. The RMS of the residuals (in arcsec), for different observation data sets, as a function of the LOV parameter $\sigma$ ; $\sigma = 0$ has been fixed at one of the nominal solutions found for nine days. The lines are marked with plus signs (arc time span of nine days), crosses (10 days), stars (11 days), boxes (13 days), full boxes (14 days) and circles (16 days). Reprinted from Milani et al. (2005c) with permission from Astronomy and Astrophysics.

To understand this behavior we compute the LOV for different data sets, corresponding to $\Delta t = 9 , 1 0 , 1 1 , 1 3 , 1 4 , 1 6$ days. Figure 10.5 shows a double minimum of the residuals RMS on the LOV; the secondary minimum moves in the direction of lower $a$ as the data increase, but not as far as the location of the other minimum. The secondary minimum disappears with 16 days of data, then the differential corrections lead to the other solution.

As discussed in Chapter 9, the classical preliminary orbit methods can have two distinct solutions, especially when the elongation is below $1 1 6 . 5 ^ { \circ }$ . When applied with three observations selected in the shorter time spans, it can provide preliminary orbits close to both the primary and the secondary minimum. As an example, with data over 10 days we can compute with the Gauss method a preliminary orbit with $a = 0 . 9 0 0$ , and from this a full least squares solution, which is a minimum of the target function, with $a = 0 . 9 0 1$ and $\mathrm { R M S } = 0 . 4 7$ arcsec. There is also an alternative preliminary solution with $a = 1 . 0 4 6$ , and from this we can compute another nominal solution, which is a local minimum, with $a = 1 . 0 3 2$ and $\mathrm { R M S } = 0 . 5 8$ arcsec.

Indeed, if there were only three observations, both preliminary orbit solutions would correspond to very low RMS of residuals (not zero, because of planetary perturbations); the two local minima of the target function would be roughly at the same level. As the amount of data increases, the RMS increases for both the nominal solutions, but for one more than for the other. The existence of two local minima implies that there needs to be a saddle point, where the Hessian matrix of second derivatives has some negative eigenvalue, somewhere in the $\mathbf { x }$ space of orbital elements.4 However, the LOVs for which the RMS is plotted in Figure 10.5 join two local minima without necessarily passing from the saddle, and even if they did, the LOV computation algorithm does not provide a way to find this out. Indeed, the normal matrices $C ( \mathbf { x } )$ used in the computation of the multiple solutions have eigenvalues $\geq 0$ ; only the normal matrix of Newton’s method, $C _ { n e w }$ of eq. (5.3), can have negative eigenvalues. Saddle points actually exist in asteroid orbit determination, but to find them it is necessary to use at least some approximation for the second partial derivatives of the residuals, and a more sophisticated optimization method (Sansaturio et al. 1996).

# 10.3 Selection of a metric

The eigenvalues $\lambda _ { j }$ of the normal matrix $C$ are not invariant under a coordinate change. Thus a different weak direction and a different LOV would be obtained by using some other coordinates $\mathbf { y } = \mathbf { y } ( \mathbf { x } )$ . This is true even when the coordinate change is linear $\mathbf { y } = S \mathbf { \Psi } \mathbf { x }$ : the normal matrix is transformed as $C _ { \bf y } = \left[ S ^ { - 1 } \right] ^ { T } ~ C _ { \bf x } ~ S ^ { - 1 }$ and the eigenvalues are the same if $S ^ { - 1 } = S ^ { T }$ , that is if the change of coordinates is isometric. Otherwise, the eigenvalues in the y space are not the same, and the eigenvectors are not the image by $S$ of the eigenvectors in the $\mathbf { x }$ space. Thus the weak direction and the LOV in the y space do not correspond by $S ^ { - 1 }$ to the weak direction and the LOV in the $\mathbf { x }$ space. A special case is scaling, a transformation changing the units along each axis, represented by a diagonal matrix $S$ (see Section 6.4).

# Coordinates to express initial conditions

A non-exhaustive list of coordinates used in orbit determination is:

Cartesian heliocentric coordinates (position, velocity);   
• cometary elements $( q , e , I , \Omega , \omega , t _ { p }$ , with $t _ { p }$ the time of perihelion passage);   
Keplerian elements $( a , e , I , \Omega , \omega , \ell$ , with $\ell$ the mean anomaly);   
equinoctial elements $( a , h = e \sin ( \varpi )$ , $k = e \cos ( \varpi )$ , $p = \tan ( I / 2 ) \sin ( \Omega )$ , $q = \tan ( I / 2 ) \cos ( \Omega )$ , $\lambda = \ell + \varpi$ , with $\varpi = \Omega + \omega$ );   
attributable elements $( \alpha , \delta , \dot { \alpha } , \dot { \delta } , \rho , \dot { \rho } )$ .

If the coordinate change is nonlinear, as it is for transformations between any two of the five types of orbital elements listed above, the covariance is transformed by the standard formula (5.5) with the Jacobian matrix

$$
{ \mathbf { y } } = \Phi ( { \mathbf { x } } ) , S ( { \mathbf { x } } ) = \frac { \partial \Phi } { \partial { \mathbf { x } } } ( { \mathbf { x } } ) , \Gamma _ { \mathbf { y } } = S ( { \mathbf { x } } ) \Gamma _ { \mathbf { x } } S ( { \mathbf { x } } ) ^ { T }
$$

and the constrained differential correction $\Delta \mathbf { y }$ can be computed accordingly.

If the computations are actually performed in the $\mathbf { x }$ coordinates, once the constrained differential correction $\Delta \mathbf { y }$ has been computed, we need to pull it back to the coordinates $\mathbf { x }$ . If $\Delta \mathbf { y }$ is small, as is typically the case when taking modest steps along the LOV, this can be done linearly:

$$
\mathbf { x } ^ { \prime } = \mathbf { x } + \left[ \frac { \partial \Phi } { \partial \mathbf { x } } ( \mathbf { x } ) \right] ^ { - 1 } \Delta \mathbf { y } .
$$

When the constrained differential corrections are large, as is likely to be when the initial point is not near the LOV, the corrections $\Delta \mathbf { y }$ must be pulled back to $\mathbf { x }$ nonlinearly, that is $\mathbf { x } ^ { \prime } = \Phi ^ { - 1 } ( \mathbf { y } + \Delta \mathbf { y } )$ .

Table 10.1 shows possible scalings for the five coordinate systems above, as proposed by Milani et al. (2005c). Cartesian position coordinates are measured in astronomical units (AU), but they are scaled as relative changes. Angle variables are measured in radians, but they are scaled in revolutions. Velocities in Cartesian coordinates are expressed in AU/day and are scaled as relative changes; angular velocities are scaled by the Earth mean motion $\boldsymbol { n } _ { \oplus }$ . The range rate is scaled by $\boldsymbol { n } _ { \oplus }$ to get a parameter with the dimension of a length, thus commensurable to the range.

Table 10.1. Units and LOV scalings for different elements. $r$ and $v$ are the heliocentric distance and velocity. $\textstyle n _ { \oplus } \simeq k$ is the Earth mean motion in rad/day; $Z = 2 \pi q ^ { 3 / 2 } n _ { \oplus } ^ { - 1 } ( 1 - e ) ^ { - 1 / 2 }$ is a characteristic time for an orbit with large $e$ .   

<table><tr><td>Cartesian Units Scaling</td><td>x AU r</td><td>y AU r</td><td>Z AU r</td><td>Ux AU/d</td><td>Uy AU/d</td><td>Uz AU/d</td></tr><tr><td>Cometary</td><td>q</td><td>e</td><td>I</td><td>U Ω</td><td>U W</td><td>U</td></tr><tr><td>Units</td><td>AU</td><td>一</td><td>rad</td><td>rad</td><td>rad</td><td>t</td></tr><tr><td>Scaling</td><td>q</td><td>1</td><td>T</td><td>2π</td><td>2π</td><td>Z</td></tr><tr><td>Keplerian</td><td>a</td><td>e</td><td>I</td><td>Ω</td><td>W</td><td>l</td></tr><tr><td>Units</td><td>AU</td><td>1</td><td>rad</td><td>rad</td><td>rad</td><td>rad</td></tr><tr><td>Scaling</td><td>a</td><td>1</td><td>T</td><td>2π</td><td>2π</td><td>2π</td></tr><tr><td>Equinoctial</td><td></td><td>h</td><td></td><td></td><td></td><td></td></tr><tr><td>Units</td><td>a AU</td><td>1</td><td>k</td><td>p</td><td>q</td><td>入 rad</td></tr><tr><td>Scaling</td><td>a</td><td>1</td><td>1 1</td><td>1 1</td><td>1 1</td><td>2π</td></tr><tr><td>Attributable</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Units</td><td>α</td><td>8 rad</td><td>a</td><td>8</td><td>p AU</td><td>L</td></tr><tr><td> Scaling</td><td>rad 2π</td><td>T</td><td>rad/d n</td><td>rad/d n</td><td>1</td><td>AU/d n</td></tr></table>

# Comparison of different LOVs

With the list of coordinates in Table 10.1, each with and without scaling, we can select 10 different LOVs. The question is to select the most effective for a specific usage. This question is complex, but we can state two rules of thumb. If the arc drawn on the celestial sphere by the apparent asteroid position is small, e.g., $\leq 1 ^ { \circ }$ , the orbit determination is less nonlinear in the coordinate systems representing instantaneous initial conditions, such as the Cartesian and the attributable elements. In the latter the angular variables $\alpha , \delta , \dot { \alpha } , \dot { \delta }$ are well determined while $\rho , { \dot { \rho } }$ are very poorly determined.

On the contrary, orbital elements solving exactly the two-body problem perform better in orbit determination whenever the observed arc is comparatively wide, e.g., tens of degrees. The cometary elements avoid the discontinuity at the $e = 1$ boundary, the equinoctial ones avoid the coordinate singularity for $e = 0$ and for $I = 0$ . The Keplerian elements are strongly nonlinear, because of nearby coordinate singularities for $e \simeq 0$ , $e \simeq 1$ and $I \simeq 0$ , thus they are not always suitable for orbit determination. Equinoctial elements modified by replacing $a$ with $n$ are especially suitable for orbit identification (see Section 7.4).

Figure 10.6 shows a comparison of the LOVs computed with different coordinate systems, without and with the scaling defined in Table 10.1, in the case of asteroid 2004 FU $^ 4$ , observed only over a time span of $\simeq 3$ days, with an arc of only $\simeq 1 ^ { \circ }$ . The data are projected on the $( \rho , \dot { \rho } )$ plane, with $\dot { \rho }$ scaled by $n _ { \oplus }$ . For each coordinate system we show both the LOV, sampled with 41 VAs in the interval $- 1 \leq \sigma _ { Q } \leq 1$ , and the second LOV, defined as the LOV but with the second largest eigenvalue $\lambda _ { 2 }$ of the normal matrix and the corresponding eigenvector $\mathbf { v } _ { 2 }$ . The dependence of the LOV on the coordinates is very strong in this case. Note that the LOV of the Cartesian and attributable coordinates is closer to the second LOV, rather than to the first LOV, of the equinoctial coordinates. In such cases, with a very short observed arc, the confidence region has a two-dimensional spine, and the selection of a LOV in the corresponding plane is quite arbitrary. For example, in scaled Cartesian coordinates, the ratio of the two largest semiaxes of the confidence ellipsoid is $\simeq 2 . 4$ . Then the best strategy to sample the confidence region would be either to use a number of LOVs, like in the figures, or to use a fully two-dimensional sampling, as in Section 8.2.

![](images/c3a4547c537fd20b375301e373d9c97492c2594f5bf5b4379bd1b2b22fb32ca0.jpg)  
Fig. 10.6. For the asteroid $2 0 0 4 ~ \mathrm { F U _ { 4 } }$ the computation of the LOV, by using only the first 17 observations, in different coordinates, without scaling on the left, with scaling on the right; the label denotes the coordinate system used and whether the line represents either the ordinary LOV or the second LOV. The Cartesian and attributable LOVs are indistinguishable on this plot and so only the attributable LOV is depicted. Reprinted from Milani et al. (2005c) with permission from Astronomy and Astrophysics.

![](images/ba52b7266074861a2f725d05f85b0f41cdad5b325d8c6b3b048b7864bf93c0c0.jpg)  
Fig. 10.7. For the asteroid $2 0 0 2 ~ \mathrm { N T _ { 7 } }$ the computation of the LOV, by using only the first 113 observations, in different coordinates, without scaling on the left, with scaling on the right. The Cartesian and attributable LOVs are indistinguishable. Reprinted from Milani et al. (2005c) with permission from Astronomy and Astrophysics.

Figure 10.7 shows the comparison of the LOVs in the case of asteroid 2002 NT $7$ when the available observations spanned 15 days, forming an arc almost $9 ^ { \circ }$ wide. In this case the ratio of the two largest semiaxes (in scaled Cartesian) is $\simeq 7 . 3$ and the LOVs computed with different coordinates are very close. As the confidence region becomes smaller, but also narrower, the long axis becomes less dependent upon the metric. Note that the attributable and the Cartesian coordinates have LOVs quite close in all cases. This can be understood knowing that the $( \rho , \dot { \rho } )$ plane of the attributable coordinates corresponds exactly to a plane in Cartesian coordinates.

# Uncertainty of curvature

Given the explicit formulae (9.2) and (9.3) we can compute the covariance matrix of the quantities $( \kappa , \dot { \eta } )$ by propagation of the covariance matrix of the angles and derivatives with the matrix of partial derivatives for $\kappa , ~ \dot { \eta }$ with respect to the 6-vector $V = ( \alpha , \delta , \dot { \alpha } , \dot { \delta } , \ddot { \alpha } , \ddot { \delta } )$

$$
\Gamma _ { ( \kappa , \dot { \eta } ) } = \frac { \partial ( \kappa , \dot { \eta } ) } { \partial V } \Gamma _ { V } \left[ \frac { \partial ( \kappa , \dot { \eta } ) } { \partial V } \right] ^ { T } .
$$

The covariance matrix $1 _ { V } ^ { \prime }$ for the angles and their first and second derivatives is obtained by the procedure of least squares in a fit to the individual observations as a quadratic function of time. The partials of $\kappa$ and $\dot { \eta }$ are given in (Milani et al. 2008, Section 5.1): we list just the last four of these partials, the $2 \times 2$ matrix $\partial ( \kappa , \dot { \eta } ) / \partial ( \ddot { \alpha } , \ddot { \delta } )$ , because they contribute to the principal part of the covariance of $( \kappa , \dot { \eta } )$ for short arcs, as shown below.

$$
\frac { \partial \kappa } { \partial \ddot { \alpha } } = - \frac { \dot { \delta } \cos \delta } { \eta ^ { 3 } } ; \frac { \partial \kappa } { \partial \ddot { \delta } } = \frac { \dot { \alpha } \cos \delta } { \eta ^ { 3 } } ; \frac { \partial \dot { \eta } } { \partial \ddot { \alpha } } = \frac { \dot { \alpha } \cos ^ { 2 } \delta } { \eta } ; \frac { \partial \dot { \eta } } { \partial \ddot { \delta } } = \frac { \dot { \delta } } { \eta } .
$$

We use a full computation of the covariance matrix to assess the significance of curvature with the formula

$$
\chi ^ { 2 } = \left[ \begin{array} { l } { \kappa } \\ { \dot { \eta } } \end{array} \right] ^ { T } \Gamma _ { ( \kappa , \dot { \eta } ) } ^ { - 1 } \left[ \begin{array} { l } { \kappa } \\ { \dot { \eta } } \end{array} \right]
$$

and we assume that the curvature is significant if $\chi ^ { 2 } > \chi _ { m i n } ^ { 2 }$

# The infinite distance limit

Low values of $\mathcal { C }$ , see eq. (9.30), can occur in two ways: near the zero circle and for large values of both $\rho$ and $r$ . The size of the deviations from a great circle will depend upon the length of the observed arc (both in time $\Delta t$ and in arc length $\sim \eta \Delta t$ ). Thus for short observed arcs it may be the case that the curvature is not significant, and the preliminary orbit algorithms will yield orbits which may fail as starting guesses for differential corrections.

We will now focus on the case of distant objects. We would like to estimate the magnitude of the uncertainty in the computed orbit with respect to the small parameters $\nu , \tau , b$ where $\nu$ is the astrometric accuracy of the individual observations (in radians) and $\tau = n _ { \oplus } \Delta t$ , $b = q _ { \oplus } / \rho$ are small for short observed arcs and for distant objects, respectively. Note that the proper motion $\eta$ for $b  0$ has principal part $\textstyle n _ { \oplus } b$ – the effect of the motion of the Earth. The uncertainty in the angles $( \alpha , \delta )$ and their derivatives can be estimated as follows (Crawford et al. 1930, page 68):

$$
\begin{array} { r c l } { { \mathrm { R M S } ( \alpha ) \simeq \mathrm { R M S } ( \delta ) } } & { { = } } & { { { \mathcal O } ( \nu ) , } } \\ { { \mathrm { R M S } ( \dot { \alpha } ) \simeq \mathrm { R M S } ( \dot { \delta } ) } } & { { = } } & { { { \mathcal O } ( \nu \tau ^ { - 1 } ) , } } \\ { { \mathrm { R M S } ( \ddot { \alpha } ) \simeq \mathrm { R M S } ( \ddot { \delta } ) } } & { { = } } & { { { \mathcal O } ( \nu \tau ^ { - 2 } ) . } } \end{array}
$$

The uncertainty of the curvature components $( \kappa , \dot { \eta } )$ should be estimated by the propagation formula (10.4) but it can be shown that the uncertainty of $( \alpha , \delta , \dot { \alpha } , \dot { \delta } )$ contributes with higher order terms. Thus we use the estimates based upon the partials in (10.5)

$$
\frac { \partial ( \kappa , \dot { \eta } ) } { \partial ( \ddot { \alpha } , \ddot { \delta } ) } = \left[ \begin{array} { c c } { { \mathcal O ( b ^ { - 2 } ) n _ { \oplus } ^ { - 2 } } } & { { \mathcal O ( b ^ { - 2 } ) n _ { \oplus } ^ { - 2 } } } \\ { { \mathcal O ( 1 ) } } & { { \mathcal O ( 1 ) } } \end{array} \right]
$$

and obtain

$$
\Gamma _ { ( \kappa , \dot { \eta } ) } = \nu \left[ \begin{array} { c c } { \mathcal { O } ( b ^ { - 4 } \tau ^ { - 2 } ) } & { \mathcal { O } ( b ^ { - 2 } \tau ^ { - 2 } ) n _ { \oplus } ^ { 2 } } \\ { \mathcal { O } ( b ^ { - 2 } \tau ^ { - 2 } ) n _ { \oplus } ^ { 2 } } & { \mathcal { O } ( \tau ^ { - 2 } ) n _ { \oplus } ^ { 4 } } \end{array} \right] .
$$

To propagate the covariance to the variables $( \rho , \dot { \rho } )$ we use the implicit equation connecting $c$ and $\rho$ obtained by eliminating $r$ from (9.4) and (9.30):

$$
F ( \mathcal { C } , \rho ) = \mathcal { C } ~ \frac { \rho } { q } ~ + \frac { q ^ { 3 } } { ( q ^ { 2 } + \rho ^ { 2 } + 2 q \rho \cos \varepsilon ) ^ { 3 / 2 } } ~ - 1 + \Lambda _ { n } = 0 .
$$

For $b \to 0$ we have $\displaystyle { \mathcal { C } \ b ^ { - 1 } \to 1 - \Lambda _ { n } }$ ; thus $c \to 0$ and is of the same order as $b$ . Although $c$ depends upon all the variables $( \alpha , \delta , \dot { \alpha } , \dot { \delta } , \ddot { \alpha } , \ddot { \delta } )$ , by the approximation with the Laplace method (see Section 9.4) $c \simeq c$ . $C$ is given by eq. (9.27); it contains $\kappa \eta ^ { 2 }$ and has an uncertainty mostly depending upon the uncertainty of $\kappa$ and, ultimately, upon the difficulty in estimating the second derivatives of the angles. Thus we can use the derivatives of the implicit function $\rho ( \kappa )$ ; assuming $\cos \varepsilon , \eta , { \hat { \mathbf { n } } }$ to be constant and keeping only the term of lowest order in $q / \rho$ , we find

$$
\frac { \partial \rho } { \partial \kappa } = - \frac { \eta ^ { 2 } q ^ { 4 } } { \mu \hat { \mathbf { q } } _ { \oplus } \cdot \hat { \mathbf { n } } } \frac { \rho } { q _ { \oplus } C } + \mathcal { O } \left( \frac { q ^ { 3 } } { \rho ^ { 3 } } \right) = q _ { \oplus } \mathcal { O } ( 1 ) .
$$

In the same way from (9.28) we deduce $\dot { \eta } = n _ { \oplus } ^ { 2 } \mathcal { O } ( b )$ and obtain the estimates

$$
\frac { \partial \dot { \rho } } { \partial \kappa } = n _ { \oplus } q _ { \oplus } \mathcal { O } ( 1 ) , \frac { \partial \dot { \rho } } { \partial \dot { \eta } } = \frac { q _ { \oplus } } { n _ { \oplus } } \mathcal { O } ( b ^ { - 2 } ) .
$$

For the covariance matrix,

$$
\Gamma _ { ( \rho , \dot { \rho } ) } = \frac { \partial ( \rho , \dot { \rho } ) } { \partial ( \kappa , \dot { \eta } ) } \Gamma _ { ( \kappa , \dot { \eta } ) } \left[ \frac { \partial ( \rho , \dot { \rho } ) } { \partial ( \kappa , \dot { \eta } ) } \right] ^ { T } ,
$$

we compute the main terms of highest order in $b ^ { - 1 } , \tau ^ { - 1 }$ as

$$
\Gamma _ { ( \rho , \dot { \rho } ) } = \nu \ b ^ { - 3 } \ \tau ^ { - 2 } \ \left[ \begin{array} { c c } { q _ { \oplus } ^ { 2 } \ \mathcal { O } ( 1 ) } & { q _ { \oplus } ^ { 2 } \ n _ { \oplus } \ \mathcal { O } ( 1 ) } \\ { q _ { \oplus } ^ { 2 } n _ { \oplus } \mathcal { O } ( 1 ) } & { q _ { \oplus } ^ { 2 } \ n _ { \oplus } ^ { 2 } \ \mathcal { O } ( 1 ) } \end{array} \right] .
$$

In conclusion, if $( \rho , \dot { \rho } )$ are measured in the appropriate units (AU for $\rho$ and $n _ { \oplus }$ AU for $\dot { \rho }$ ) their uncertainties are of the same order: this confirms the scaling of Table 10.1. In the scaled $( \rho , \dot { \rho } )$ plane the weak direction, thus the LOV, can be in any direction, as can be seen from Figures 8.5 and 10.4.

# 10.4 Surface of variations

When the confidence region is not elongated in one direction much more than in the others, as in the example of Figure 10.6, whatever LOV we select may not be representative of the entire confidence region. If we use for a short arc of observations the attributable elements $( A , \rho , { \dot { \rho } } )$ , where $A$ is the attributable, the confidence region is a “thin” shell surrounding a subset of the admissible region (see Section 8.4). We define as surface of variations the set $S$ of the points where the target function has a local minimum with respect to changes of $A$ , for each fixed $( \rho , \dot { \rho } )$ , with minimum RMS of the residuals below some control $\Sigma$ . $S$ is, generically, a two-dimensional manifold. Under the conditions assumed in this chapter, that is when there is little information beyond $A$ , $S$ is parameterized by $( A ( \rho , { \dot { \rho } } ) , \rho , { \dot { \rho } } )$ , defined on a subset $B$ of the $( \rho , \dot { \rho } )$ plane; $B$ is an open set, not necessarily connected. Then the surface $S$ can be computed point by point: for each $( \rho _ { 0 } , \dot { \rho } _ { 0 } )$ we can correct only $A$ , i.e., perform “doubly constrained” differential corrections, with normal equation

$$
C _ { A } \Delta A = D _ { A } , C _ { A } = B _ { A } ^ { T } B _ { A } , D _ { A } = - B _ { A } ^ { T } \xi , B _ { A } = \partial \pmb { \xi } / \partial A .
$$

If these corrections converge to a point of minimum $A ( \rho _ { 0 } , \dot { \rho } _ { 0 } )$ , and if the RMS of the residuals at this minimum is $< \Sigma$ , the point $( A ( \rho _ { 0 } , \dot { \rho } _ { 0 } ) , \rho _ { 0 } , \dot { \rho } _ { 0 } )$ belongs to the surface of variations, and $( \rho _ { 0 } , \dot { \rho } _ { 0 } )$ belongs to $B$ .

Since the attributable elements are well defined also for hyperbolic orbits, $B$ does not need to be a subset of the admissible region ${ \mathcal { D } } ( A )$ . Indeed Figures 8.5 and 10.4 clearly show that $B$ pokes out of the admissible region; in the latter case it is clear that the LOV would extend much further, if it was continued from the LOV points found by recursive attribution. Thus the choice depends upon the purpose: if we are aiming at sampling as much as possible the confidence region, even the hyperbolic orbits, a sampling of $B$ is more useful than a sampling of ${ \mathcal { D } } ( A )$ . On the contrary, if the goal is to discover the largest number of real objects, we can take into account that the number density of objects being discovered with $e \gg 1$ is very small (possibly zero, since none is known) and use a sampling of $\mathcal { D } ( A ) \cap B$ , which can be obtained by discarding the nodes of a triangulation of ${ \mathcal { D } } ( A )$ for which the doubly constrained differential corrections give a residual RMS too high.

Thus to compute the surface of variations it is not required to compute the admissible region: we can start from a set of points sampling the $( \rho , \dot { \rho } )$ plane in any convenient way, e.g., a rectangular grid.5 This and closely related methods are widely in use, e.g., (Chesley 2005, Tommei 2005). Another class of methods selects sample points in a two-dimensional space at random: this could be done in the space $( \rho , \dot { \rho } )$ , but also in the space $\left( \rho _ { 1 } , \rho _ { 2 } \right)$ of the distances at two epochs $t _ { 1 } , t _ { 2 }$ ; then the sample orbits could be selected according to some criteria, like discarding the hyperbolic ones but also preferentially exploring some portion of the phase space (Virtanen et al. 2001).

# 10.5 The definition of discovery

The quality of the least squares orbits improves as new observations, extending the observed arc time span, are added. The problem is how to find an algorithm to classify the observed arcs in quality classes with some predictive value on the information content of the orbit. This is connected with the definition of discovery: how many observations are enough to consider that a new Solar System object has been discovered? An obvious requirement would be to have enough information to be able to decide the nature of the object, e.g., to discriminate between a near-Earth asteroid (NEA), a main belt asteroid (MBA), a Jupiter trojan, a trans-neptunian object (TNO), a long periodic comet, and so on. In the definition of discovery there are a number of legal and science policy aspects, which are interesting, but not to be discussed here: we shall only give the mathematical background which should be used to build one such definition on rigorous grounds.

In modern surveys, the observations of Solar System objects are singled out among star images as moving objects: a number $m$ of digital images of the same portion of the sky is taken within a short interval, on the same night,6 and they are “digitally blinked”, that is, computer programs remove the images stationary with respect to the stellar reference frame and assemble the transients into groups which could belong to a single moving object. One such group is called a tracklet, containing astrometric observations assembled without computing an orbit, by either a linear fit or a quadratic one with upper limits on the curvature (Kubica et al. 2007). Since $m \geq 2$ , from a tracklet it is always possible to compute an attributable, but in most cases there is little, if any, curvature information.

We would like to capture in a definition an observed arc that does not allow us to compute a useful least squares orbit. Unfortunately such a definition would not be a clear-cut and operational one: the orbits computed from a given observational data set depend upon the algorithms used. For example, the complex procedure presented in Section 10.2 often succeeds in computing some orbit from a very limited data set, but then it is often a LOV orbit, or anyway with a very badly conditioned covariance matrix.

To provide a definition which is computable in all cases and is independent of the methods used in the orbit determination, we define as too short arc (TSA) an observed arc with no significant curvature, measured by eq. (10.6). The main problems with such a definition are two: the choice of the control value $\chi _ { m i n } ^ { 2 }$ , and the fact that some observed arcs may contain enough information for a significant third derivative of the angles with respect to time. If the latter is the case, the residuals of a quadratic fit have a characteristic Z shape (Milani et al. 2007, Figure 1), which is significant if the standard deviation of the (normalized) residuals is larger than some ${ \mathrm { R M S } } _ { m i n }$ . Such definitions depend upon the error model used, see Section 5.8; the covariance matrix used in (10.6) contains the weights, and the RMS of the residuals after a quadratic fit needs to be the normalized one.

Because tracklets are typically formed with observations within the same night, most of them are also TSA. In some cases an observed arc may already be the result of the identification of $\geq 2$ tracklets, and still be a TSA; this is often the case for TNO.

We call an arc of type $N$ an observed arc which can be split into exactly $N$ disjoint TSA, in such a way that each couple of TSA consecutive in time, if joined, would show a significant curvature. To obtain in all cases a unique value for the arc type it is necessary to specify the method by which observed arcs with significant curvature are to be split. A recursive procedure to compute the arc type is as follows: if the arc has significant curvature and/or a significant Z shape, it is split into two arcs by selecting the largest time gap between two observations. If the two subarcs have no significant curvature and no significant Z shape, the arc type is 2. Otherwise, the same procedure is applied to the two subarcs, and the arc type is the sum of the arc types of the subarcs. The recursion terminates because the number of observations in the subarcs decreases, and a subarc with $< 3$ observations can have neither curvature nor Z shape.

This definition, with predictive value on the orbit quality for all orbital classes of objects, should replace the currently used definition of M-nighter, an arc with observations belonging to $M$ distinct nights. For TNOs, two nights of observations in most cases form an arc of type 1. For NEAs discovered near the Earth a single night of observations often is an arc of type $\geq 2$ , then an orbit with moderate uncertainty can be computed for a one-nighter.

# Test of possible definitions

Milani et al. (2007) discusses the outcome of large-scale tests of possible definitions of discovery based on the arc type. We have used all the public asteroid astrometry available in March 2006: 9.2 million observations, including 185 296 observed arcs with time span $< ~ 1 9 0$ days (single opposition). The values $\chi _ { m i n } ^ { 2 } = 9$ and $\mathrm { R M S } _ { m i n } = 4$ were used.7 The error model for weighting the astrometry was based on (Carpino et al. 2003). A summary of the results is presented graphically in Figure 10.8. Going from type 2 to type 3 there is a sharp improvement in the quality of the orbit, allowing us in almost all cases to discriminate between MBA and NEA. As shown by Milani et al. (2007, Table IV), the arc type 3 does not correspond to three-nighters, in particular for MBA three non-consecutive nights are required.

A formal decision on the definition of discovery is not just mathematics; however, the above results suggest the mathematical properties which should be required from a data set to form a discovery. A discovery of a Solar System object should include an arc of type $N$ with $N \geq 3$ . Moreover, the information supplied should contain a unique least squares orbit (full, with six free parameters), fitting the data with residuals compatible with the current error model. The data should also contain enough photometric information to fit an absolute magnitude, constraining the size of the object.

![](images/42528791c092b9b6fd03bb44bbd800e5cf576cca46fe581b95d1cc9436ba81c1.jpg)  
Fig. 10.8. Distribution of the RMS of the perihelion $( \log _ { 1 0 } \mathrm { R M S } ( q )$ in AU) for observed arcs of different types. Top: type 1 (left), type 2 (right). Bottom: type 3 (left), type 4 (right). Reproduced with permission of Springer from Milani et al. (2007).

The object also needs to be new, not yet discovered according to the same definition, but this becomes complicated, both from the legal and the mathematical point of view, if the same discovery contains data from different observatories. Even the definition of arc type needs to be changed in case two tracklets, from different observatories, are overlapping in time, to take into account the topocentric corrections in a smooth way. One way is to split the arc by tracklets, not by observations. Anyway it is necessary to use information on the time when the data have been made public.

# 11 SURVEYS

This chapter is devoted to population orbit determination, that is not just computing the orbit for a single object, but compiling a catalog of orbits given a large number of observations. A survey is a project aiming at collecting observations of the largest and most representative sample of objects possible. We deal here only with the case in which the target population belongs to the Solar System; of course an astronomical survey may target simultaneously extrasolar populations. We deal with Earth satellites in Section 8.7. This chapter is based on our papers (Milani et al. 2005a, Milani et al. 2008, Milani et al. 2006) and ongoing research, in particular that in preparation for Pan-STARRS, a nextgeneration survey.

# 11.1 Operational constraints of Solar System surveys

The following three arguments should be taken into account in the definition of an identification/orbit determination procedure for a modern sky survey.

First, Moore’s law tells us that the number of elements in an electronic chip grows exponentially with time; the doubling time has been around 18 months for more than 30 years. There is no indication that this trend might slow down; although in the last few years it has no longer been possible to increase the clock frequency, the increase in the complexity of the chips is now used to produce “multicore” CPUs. Assuming the multicores are used in an efficient parallelization procedure, the practical performance of computers continues to increase by a factor of 4 every three years. The CCD cameras used to produce astronomical images have also increased their number of pixels according to Moore’s law,1 thus the capability of surveys to produce astrometric data is also growing exponentially with time. To exploit this technology is more cost effective than increasing the telescope size.

Second, the surveys have interest in decreasing the signal-to-noise (S/N) ratio at which the observations are considered, because state-of-the-art CCDs have less noise and because a gain in the acceptable S/N gives an increase in the limiting magnitude (at which objects can be considered detected) without an increase in the telescope diameter. Then some false observations are unavoidably accepted. The problem is that the false data may propagate through the orbit determination procedure and degrade the results.2

Third, the surveys have interest in scheduling their observations to get a minimum number of observations for each Solar System object to be discovered. This is due to the preference given to multidisciplinary surveys, trying to obtain results for very different astronomical, astrophysical, and cosmological investigations with the same telescope and even the same images. To obtain orbits for Solar System objects there is a requirement of multiple observations at constrained time intervals. This can generate a conflict of interest between the Solar System subtask and the requirement of other investigations to be conducted simultaneously. This implies the need for a more aggressive orbit determination, using less data for each object.

These three considerations lead to choices, in the design of a survey, which cannot be reversed just because we would like orbit determination to be easier. Thus we must not neglect the following implications.

First, it is essential to keep under control the computational complexity of the procedure used for identification and orbit determination; if the number of objects which could be discovered is $N$ and the number of observations is $M$ , the algorithms need to use a number of operations of order smaller than quadratic, e.g. $\mathcal { O } ( N \log N )$ , $\mathcal { O } ( N \log M )$ , or $\mathcal { O } ( M \log M )$ . Any algorithm with a quadratic complexity $\mathcal { O } ( N ^ { 2 } )$ , $\mathcal { O } ( M ^ { 2 } )$ , or $\mathcal { O } ( N M )$ becomes impossible to use when $N \simeq 1 0 ^ { 7 }$ and $M \simeq 1 0 ^ { 9 }$ (including false), as it is planned for the surveys starting at the time this book is being written: 3 nanoseconds used in an $N \times M$ loop correspond to about a year of CPU time. It is important to be aware that we cannot brush away this constraint by waiting for more powerful computers of the next generation, because the next generation surveys will produce more data with more or less the same increase in performance: a quadratic algorithm would become more and more inadequate as time goes by. Note that traditional procedures, e.g., computing Gauss preliminary orbits with all triples of observations from different nights, an $\mathcal { O } ( M ^ { 3 } )$ algorithm, was adequate when it was invented, but cannot be used for the current surveys.

Second, there is the problem of accuracy, that is the fraction of the proposed identifications and orbits which are true. To keep the fraction of false under control without decreasing the efficiency, that is the fraction of the objects actually appearing in the images which can be declared discovered, is the most difficult task of population orbit determination. Individual detections presumed to be moving objects could be false (noise, statistical flukes, variable stars, etc.), each tracklet formed with them could be false (containing false detections and/or assembling detections from two different objects), and the identifications proposed among the tracklets can also be false (containing false tracklets and/or assembling tracklets from different objects). The false detections increase sharply with lower S/N, the false tracklets and false identifications grow quadratically (either $\mathcal { O } ( M ^ { 2 } )$ or $\mathcal { O } ( N ^ { 2 } )$ , depending upon the methods used). To avoid this cascade of false conclusions, it is essential to use a very tight quality control on the final orbit; typically we use a statistical quality control on the residuals of the least squares fit. However, if the number of false tracks produced by the first stages of the procedure is $\mathcal { O } ( N ^ { 2 } )$ , this would be the complexity of the overall procedure.

Third, the orbit determination methods have to attempt to provide an orbit with much less data than the traditional ones, e.g., observations in only two nights, observations in two short arcs separated by more than one orbital period, and some observations at a low S/N mixed with more reliable ones. Some of the algorithms proposed in the previous chapters can be used for this. Of course this increases the difficulty of the verification procedure and of the statistical quality control to avoid false conclusions.

# 11.2 Identification and orbit determination procedure

The processing begins with the astrometric data,3 containing the detections presumed to belong to moving objects above a given S/N threshold $s$ . They include false detections, but $s$ has to be chosen such that the false are not too many, e.g., the true/false ratio could be of the order of 1.

# From detections to tracklets

The first step is to assemble each group of detections which could belong to one and the same moving object into a tracklet. Without an orbit, this can be done just by using spatial proximity between detections at different times. For two detection tracklets the number of possible tracklets is $\mathcal { O } ( M ^ { 2 } )$ , the most likely belonging to moving objects need to be selected by a smaller complexity algorithm, e.g. $\mathcal { O } ( M \log M )$ , as in (Kubica et al. 2007). The control values used to select the tracklets are the proper motion $\eta$ and, if there are three detections, the curvature components $\kappa \eta ^ { 2 } , \dot { \eta }$ introduced in Chapter 9. Interesting objects passing close, mostly near-Earth asteroids, can have rather long and curved tracklets, thus the controls must be loose. Hence it is unavoidable to have a significant fraction of false tracklets. As we will see in Section 11.4, this does not result in a cascade of false identifications.

# From tracklets to tracks

The second step is to assemble tracklets into tracks, or proposed identifications. A track is a list of tracklets which could belong to one and the same Solar System object. There are at least two different methods to select the tracks. First, the recursive attribution methods, described in Chapter 8 and Section 10.2. Second, the binary tree methods, described by Kubica et al. (2007). A possible third method uses the integrals of the Kepler problem, see Section 8.6, but this has not been fully tested yet, while the two previous methods have been shown to be very efficient in simulation tests. There are also other methods such as (Granvik et al. 2005).

The main difference is that binary trees are sophisticated algorithms to control the computational complexity, which remains $\mathcal { O } ( M \log M )$ even to align triples, quadruples, and so on, of tracklets, but the controls used to select the tracks are just polynomial inequalities. No orbit is computed, although the controls with quadratic polynomials can be done in such a way to exploit the relationship between the distance $\rho$ and $\eta ^ { 2 } \kappa$ to exclude only objects nearer than those at the tiny object boundary (see Section 8.1).

On the contrary, in the recursive attribution methods the smooth function with which the data are compared is always the path on the celestial sphere computed by means of an orbit, maybe just a hypothetical one.

In this book we have discussed in detail the recursive attribution methods; for the binary tree methods we suggest reading (Kubica et al. 2007). In practice, the two classes of methods can be effectively used together in a multistage procedure, see (Milani et al. 2008, Section 6).

# From tracks to identifications

The process to confirm a track and generate from it a confirmed identification can be conceptually decomposed into four steps:

(i) Compute a preliminary orbit, by using some information from the observations of all the tracklets, e.g., either by selecting one observation in each tracklet, or by using the attributable of each tracklet.   
(ii) Use the preliminary orbit as first guess for a differential corrections procedure, which might contain several steps as in Section 10.2.   
(iii) If the differential corrections converge, apply a statistical quality control to the final residuals. If the values of the quality control parameters are satisfactory, the track is accepted as identification.   
(iv) Apply identification management and tracklet management to the global set of identifications and tracklets obtained, to remove duplications, contradictions, and incomplete identifications; see Section 11.4.

Only at the end of such a process is it possible to claim to have identified the real Solar System objects which have been observed. Those with a welldetermined orbit could then be tested for the requirements of a definition of discovery (Section 10.5). Even after this rigorous procedure, a small fraction of false discoveries may remain, and special care needs to be taken to remove them from the results, thanks to the successive accumulation of data.

# 11.3 Controlling the computational complexity

There are two problems to be solved to find an appropriate algorithm for identification and orbit determination from the data of a large survey. First, the tracks have to be found with a fast algorithm, e.g., with a computational complexity $\mathcal { O } ( M \log M )$ , and a very high efficiency, that is only a small fraction of objects actually observed can be lost (a typical goal could be an efficiency 0.95–0.99). Second, the accuracy of the tracks has to be controlled; if the true tracks were just a fraction $\mathcal { O } ( 1 / N )$ of the proposed ones, the tracks to be tested would be $\mathcal { O } ( N ^ { 2 } )$ and the computational cost would be dominated by the confirmation procedure, mostly step (ii).

At first sight, these two requirements appear contradictory. The solution is to devise a somewhat more complex procedure, in which both efficiency and accuracy are achieved by successive steps, in such a way that the composite computational complexity of the pipeline is controlled. We will present here two possible solutions, which should not be considered alternative, but rather to be used together for best performance.

# Binary tree method

If the binary tree method is used as the first step, to generate a list of tracks, a high efficiency can be achieved in finding the true tracks corresponding to Solar System objects observed over at least three different nights. The main problem is that they are mixed with many false tracks. Kubica et al. (2007) and Milani et al. (2008) describe full-scale simulations of a large survey with accuracies below 0.01 for the proposed tracks: this could lead to a large computational overhead in the confirmation procedure.

A solution is to use step (i) of the confirmation procedure, the preliminary orbit computation, as a filter to reduce the number of tracks to be submitted to differential corrections (which are much more computationally intensive). Since the binary tree method works with tracklets from three or more nights, the preliminary orbit method should be Gauss. A track can be refused on the basis of the preliminary orbit computation in two cases. The first one occurs when the hypothesis (9.36) is contradicted: if the values of $\gamma = \gamma _ { 2 } , C = C _ { 2 } , \epsilon$ obtained from the three observations selected among the $\geq 3$ tracklets are such that there is no solution of the intersection problem of Section 9.7, 4 then the track should be false.

The second case of track rejection is when some preliminary two-body orbit can be obtained, but when the residuals of the observations from all tracklets are computed, they have a RMS value too large. The control value for this kind of track rejection has to be selected with care. The preliminary orbit is a two-body orbit, and even that is obtained with some truncation to some order in $\Delta t$ , thus the accuracy cannot be the same as requested for a least squares solution with a full $N$ -body model; e.g., in (Milani et al. 2008) values around 10 arcsec have been shown to be a good choice.

By combining both tests, it is possible to reduce the number of proposed tracks by an order of magnitude, thus the computational overhead of differential corrections, needed as the following step, becomes acceptable. Moreover, the procedure to confirm tracks is parallelizable by tracks, that is the proposed tracks may be split among a number of processors/cores.5

# Recursive attribution method

Another procedure to compose tracks is recursive attribution, that is a $( j + 1 )$ -track is formed by attribution to an orbit computed for a $j$ -track, see Section 10.2. For $j = 1$ the procedure starts from virtual asteroids obtained by sampling the admissible region, as discussed in Sections 8.2 and 8.3. The main problem is how to avoid performing complex computations inside an $\mathcal { O } ( M N )$ loop (the number of tracklets is $\mathcal { O } ( M )$ and the number of orbits is $\mathcal { O } ( N ) )$ . From each tracklet an attributable is computed: however, each attributable $A _ { i }$ has its own mean time $t _ { i }$ . If we were to compute the predicted attributable at times $t _ { i }$ from each orbit $E _ { k }$ , the double loop with respect to $i , k$ would contain a computationally expensive orbit propagation.

This problem can be solved by selecting a fixed time step, e.g., one day, and a discrete set of times, e.g., local midnight near where the telescopes are located. Each orbit is propagated to the local midnight of the $N _ { n i g }$ nights in which there are observations to be attributed. Thus the number of orbit propagations is still $\mathcal O ( N )$ . Each attributable is propagated from time $t _ { i }$ to the local midnight $t _ { 0 }$ by some simple formula, such as a linear extrapolation:

$$
\alpha ( t _ { 0 } ) = \alpha ( t _ { i } ) + \dot { \alpha } ( t _ { i } ) ( t _ { 0 } - t _ { i } ) , \delta ( t _ { 0 } ) = \delta ( t _ { i } ) + \dot { \delta } ( t _ { i } ) ( t _ { 0 } - t _ { i } ) .
$$

If this approximation is too poor, it is possible to propagate to the time of each individual digital image (in modern asteroid surveys, a large number of objects is detected in each frame).

The extrapolated values $( \alpha ( t _ { 0 } ) , \delta ( t _ { 0 } ) )$ can be compared with the predictions for the same epoch from the orbit. This comparison is in a twodimensional space, and the selection of the candidates for attribution can be done by using some simple two-dimensional metric $K _ { 2 }$ , e.g., by using either the confidence ellipse or the two-dimensional identification penalty. The prediction needs to be in a linear regime to do this with simple computations. The test $K _ { 2 } < K _ { 2 m a x }$ can be used as a first filtering stage, with a very limited number of operations to be repeated $\mathcal { O } ( N M )$ times.

This loop can be replaced by a faster one with computational complexity $\mathcal { O } ( N \log M ) + \mathcal { O } ( M \log M )$ ; we can sort the $( \alpha _ { i } ( t _ { 0 } ) , \delta _ { i } ( t _ { 0 } ) )$ coordinates for each night by the value of the right ascension. The sorting has complexity $\mathcal { O } ( M \log M )$ and can be performed with classical algorithms (Knuth 1998). Then for each of the $N$ orbits we search the sorted list to find the attributable with the $\alpha _ { i }$ nearest to the prediction and compare only those with neighboring $\alpha$ . This can be done by the binary search method, with complexity $\mathcal { O } ( N \log M )$ . This algorithm is simpler and less efficient than the binary tree, and other multidimensional sorting methods such as (Granvik et al. 2005), but it is good enough to reduce the computational complexity. Moreover, the procedure for attribution is parallelizable by orbits, that is the orbits may be split among a number of processors/cores.

The orbit-attributable couples passing the first filter are submitted to a second one, containing an orbit propagation to the exact time $t _ { i }$ , a prediction of an attributable at time $t _ { i }$ (with covariance) resulting into a fourdimensional vector of residuals (O-C), and the computation of the penalty $K _ { 4 }$ , see Section 8.4. If $K _ { 4 } ~ < ~ K _ { 4 m a x }$ , then the couple is proposed as an attribution.

Confirmation of a proposed attribution, the third filtering stage, is done by selecting a preliminary orbit as in Section 8.5.6 This is used as first guess for differential corrections. If convergence is achieved, and the quality control of the residuals is satisfactory, the attribution is accepted, which is not the same as saying that the identification is true, see the next section.

# 11.4 Identification management

The procedure of identification management has the purpose of compiling a catalog of identifications, each with its orbit(s) and auxiliary information (covariance, residuals, quality control metrics), removing all kinds of duplications and contradictions.

Duplications may arise because the same identification may be obtained through different sequences, e.g., $( ( A , B ) , C )$ and $( ( A , C ) , B )$ , where $A , B , C$ are tracklets and the symbol $( \cdot , \cdot )$ denotes an identification. There are different kinds of contradiction: the most severe is of the form $( ( A , B ) , C )$ and $( ( A , D ) , E )$ , i.e., two discordant identifications with a tracklet in common.

Both duplications and contradictions can be removed with a procedure of identification normalization, with an arbitrary list of identifications as input and as output a normalized list with only independent identifications, that is each observation belongs to only one of them.

The key issue is that normalization is a global procedure, which needs to be applied to all the identifications available, or at least to all those formed with a set of observations which may refer to the same objects. For example, if the survey covers, in a given lunation, a region near the opposition and one near quadrature (the so-called sweet spots, specially suited for detection of near-Earth asteroids), then we can apply the normalization procedure to the identifications formed with opposition data and, separately, to those with quadrature data, because they can be assumed to be independent.

# Normalization procedure

We define the following relationships between two identifications: let $L i s t ( i d _ { 1 } )$ , $L i s t ( i d _ { 2 } )$ be the lists of tracklets belonging to the identifications $i d _ { 1 } , i d _ { 2 }$

$$
\begin{array} { r l } & { \bullet \ i n c l u d e d ( i d _ { 1 } , i d _ { 2 } ) \Longleftrightarrow L i s t ( i d _ { 1 } ) \subsetneq L i s t ( i d _ { 2 } ) } \\ & { \bullet \ c o n t a i n s ( i d _ { 1 } , i d _ { 2 } ) \Longleftrightarrow L i s t ( i d _ { 2 } ) \subsetneq L i s t ( i d _ { 1 } ) } \\ & { \bullet \ i n d e p e n d e n t ( i d _ { 1 } , i d _ { 2 } ) \Longleftrightarrow L i s t ( i d _ { 1 } ) \cap L i s t ( i d _ { 2 } ) = \emptyset } \end{array}
$$

$$
{ \begin{array} { l } { { s a m e ( i d _ { 1 } , i d _ { 2 } ) \Longleftrightarrow L i s t ( i d _ { 1 } ) = L i s t ( i d _ { 2 } ) } } \\ { { d i s c o r d a n t ( i d _ { 1 } , i d _ { 2 } ) = L i s t ( i d _ { 1 } ) \cap L i s t ( i d _ { 2 } ) \neq \emptyset , L i s t ( i d _ { 1 } ) , L i s t ( i d _ { 2 } ) . } } \end{array} }
$$

These five properties are mutually exclusive and they cover all possible cases. The goal of normalization is to select a subset with only independent identifications. Among non-independent identifications, the procedure needs to select those with more information and more likely to be true.

Our normalization procedure is defined as follows. The input list of identifications is sorted according to an ordering relationship called better. The definition we currently use is based upon the number nt of tracklets in the identification, and upon the RMS $\sigma$ of the least squares fit residuals (if the identification has alternative orbit solutions, the lowest RMS value has to be used). An identification is better if it includes more tracklets or, for the same number of tracklets, if the residuals have a smaller RMS:

Then the sorted list is scanned from the top: the “best” identification is inserted in the normalized list. We proceed as follows: For the following identifications $i d _ { k }$ in the input list:

if for each $i d _ { j }$ in the normalized list independent $( i d _ { k } , i d _ { j } )$ , then $i d _ { k }$ is inserted in the normalized list;   
if there is a normalized $i d _ { j }$ such that included $\ l _ { l } ( i d _ { k } , i d _ { j } )$ , then $i d _ { k }$ is dropped; if there is a normalized $i d _ { j }$ such that $s a m e ( i d _ { k } , i d _ { j } )$ , then the solutions of $i d _ { k }$ are added to those of $i d _ { j }$ , and duplicate solutions (consistent within the uncertainty given by the covariance matrices) are removed.

Note that $c o n t a i n s ( i d _ { k } , i d _ { j } )$ cannot occur: it would imply $b e t t e r ( i d _ { k } , i d _ { j } )$ , while $i d _ { j }$ comes from higher up in the sorted list.

The steps defined above are enough to remove from the normalized list all duplications and cases of included identifications: e.g., if $( ( A , B ) , C )$ i s in the input list, both $( A , B )$ and $( ( A , C ) , B )$ are removed, without losing track of possible double solutions with the same set of observations.

# Discordant identifications

The critical step is how to handle a couple of discordant identifications. There are three appropriate choices: to keep in the normalized list only one if it is much better than the other, to discard both, or to try to “merge” them into a single identification.

The choice of the much better ordering relationship is critical. It should indicate that an identification is significantly more likely to be true than the other, as measured from the quality control metrics. To “merge” two identifications requires fitting an orbit to all the observations belonging to both, then to apply quality control to the resulting residuals. If neither of these two cases applies, the only way to complete the normalization, removing all discordancies, is to discard both. In doing this, as the simulations discussed below show, we often sacrifice one true identification to remove a false one, that is we privilege accuracy with respect to efficiency. 7

In the tests we have done so far, we use a definition of much better based only on the two parameters $n t$ and $\sigma$ :

with a control $\delta _ { \sigma } > 0$ (we have used $\delta _ { \sigma } = 0 . 2 5$ ). It would be possible to use some of the other quality control parameters described in Section 11.5.

# An example

To explain better the logic of the normalization procedure, let us use a simple example. Let us assume that $A , B , C , D , E , F$ are tracklets, and that the output of the identification procedure is

$$
\begin{array} { r l r } { { 2 } ~ i d s } & { \textnormal { 3 } i d s } & { \textnormal { 4 } i d s } \\ { ( A , B ) , } & { ( ( A , B ) , C ) , } & { ( ( ( A , B ) , C ) , D ) , } \\ { ( F , C ) , } & { ( ( E , F ) , C ) , } \\ { ( E , F ) . } & { } & \end{array}
$$

Let us assume the identification list, sorted by better, is

$$
\begin{array} { l l } { { ( ( ( A , B ) , C ) , D ) } } & { { } } \\ { { ( ( A , B ) , C ) } } & { { i n c l u d e d \mathrm { i n \ ( 1 ) } } } \\ { { ( ( E , F ) , C ) } } & { { d i s c o r d a n t \mathrm { w i t h \ ( 1 ) } \mathrm { w h i c h \ i s \ m u c h \ b e t t e r } } } \\ { { ( A , B ) } } & { { i n c l u d e d \mathrm { i n \ ( 1 ) } } } \\ { { ( F , C ) } } & { { d i s c o r d a n t \mathrm { w i t h \ ( 1 ) } \mathrm { w h i c h \ i s \ m u c h \ b e t t e r } } } \\ { { ( E , F ) } } & { { i n d e p e n d e n t \mathrm { f r o m \ ( 1 ) } . } } \end{array}
$$

Then the normalized list is

$$
( ( ( A , B ) , C ) , D ) , \qquad ( E , F ) .
$$

This example can also be used to show that the normalization must be done globally, on all the identifications in the same set of data, not by adding sequentially the tracklets and the identifications when they are available. Let us suppose the tracklet $D$ has not been observed yet, and the normalization is started using as list of identifications the one above without (1). Then (2) and (3) are discordant: if none of the two is much better, both of them have to be discarded; the same may occur with (5) and (6), and the normalized list may be just $( A , B )$ . If $D$ is added later, maybe $( ( A , B ) , D )$ is found, but the much better identification (1) is not available and the object corresponding to $( E , F )$ is lost.

# Controlling the computational complexity

The normalization procedure as outlined above does work, and gives an important contribution to increase the accuracy as discussed in Section 11.5. However, if $N$ is the number of objects being discovered, the computational complexity of the normalization procedure as described is $\mathcal { O } ( N ^ { 2 } )$ . Thus for $N$ large enough, the computational load of the normalization could exceed the load for obtaining the identifications.

An algorithm for normalization of complexity $\mathcal { O } ( N \log N )$ is as follows. Whenever an identification $i d _ { j }$ is added to the normalized list, all the tracklets in $L i s t ( i d _ { j } )$ are endowed with a pointer to $i d _ { j }$ . Then, when another identification $i d _ { k }$ from the original list is analyzed, we can assemble all the pointers to normalized identifications of the tracklets in $L i s t ( i d _ { k } )$ ; they define the subset of the normalized identifications $i d _ { r }$ for which independent $\left( i d _ { k } , i d _ { r } \right)$ is false. This list is used in the normalization procedure as outlined above. The procedure for assembling the pointers has complexity $\mathcal { O } ( N \log N )$ i f binary search of the tracklets is used to access the pointers.

With this method, the computational load of the identification management becomes negligible, with respect to that for finding and confirming the identifications. The only caveat is that for large $N$ a large random access memory (RAM) is needed to run the procedure globally, because of the long input list of identifications (possibly with duplications) and of the large set of pointers. If this results in using virtual memory, i.e., much slower access to disk, the performance could be severely impaired.8

# Merging discordant identifications

We need to consider the possibility, in the case $d i s c o r d a n t ( i d _ { k } , i d _ { j } )$ , of merging identifications, that is to look for an orbit which can fit all the observations belonging to the tracklets of $L i s t ( i d _ { j } ) \cup L i s t ( i d _ { k } )$ , with residuals passing the quality control. The track, hence the list of observations, is given; however, in the list of observations it is necessary to remove the duplications and check for contradictions (see under tracklet management).

The first guess orbit for differential corrections could be selected among the already known ones, an orbit of $i d _ { j }$ being preferred to that of $i d _ { k }$ because $b e t t e r ( i d _ { j } , i d _ { k } )$ . Then differential corrections need to be applied: if they converge and the residuals pass the quality control, then the new identification $i d _ { m }$ with $L i s t ( i d _ { m } ) = L i s t ( i d _ { j } ) \cup L i s t ( i d _ { k } )$ replaces $i d _ { j }$ in the normalized list and $i d _ { k }$ is dropped.

This algorithm has been shown by many tests to be very effective in assembling much larger identifications (with more tracklets) from smaller ones, but it may introduce serious problems in the overall procedure. First, the average computational complexity of the merging algorithm is hard to compute, but it is possible to generate fictitious examples showing that the worst case complexity could be terrible.9 Second, the insertion of $i d _ { m }$ in place of $i d _ { j }$ destroys the work already done in the normalization procedure, in that $i d _ { m }$ may well be discordant, e.g., merging $( A , B )$ with $( A , C )$ may result in discordancy with $( C , D )$ , which might have been already inserted into the supposedly normalized list. A solution to both problems is to use recursive attribution for as many steps as required to get to the identifications with $M$ tracklets, where $M$ is such that objects observed with more than $M$ tracklets are exceptional cases, occurring for a small fraction of the population. For example, if there is just one tracklet per night for each object in the great majority of the cases, $M$ could be the number of observing nights. Then identification merging allows us to find the best orbit even for the few “overobserved” objects. To obtain the normalized list, it is enough to run the normalization procedure twice, the first with merging, the second without.

# Orbit identification

Once the normalized list of identifications for a given time span (e.g., a lunation) has been formed, it should be compared with those built previously. Since each identification has some fitting orbit, this problem could be solved with the methods of orbit identification of Chapter 7.

The tracklets observed in one lunation can also be attributed to the orbits computed for another lunation (be it the previous or the next): in this approach, the combination between the two sets of results is just a continuation of the recursive attribution procedure of Section 11.3, to be followed by identification management (for all the identifications obtained with the data of both lunations). When the gap in time between the two observation time spans, in which the same objects might appear, is short, the attribution is a more efficient method. If the gap in time is long, and the orbits obtained are well determined (e.g., arc type $\geq 3$ , see Section 10.5), the orbit identification algorithms are very efficient. There is one difficult case, when an object has not been observed enough for a well-determined orbit, e.g., just two nights, and then may have been re-observed after a long time (years). There is currently no general solution for this case, but several methods are being tested, see Sections 7.4 and 8.6, and also (Granvik and Muinonen 2008).

# Tracklet management

The composition of tracklets can have two problems. First, there can be incomplete tracklets, not including all the detections of an object in the same night: if $a , b , c , d$ are detections of the same object, there could be tracklets $( ( a , b ) , c )$ and $( ( b , c ) , d )$ . Second, there can be false tracklets, including false detections and/or detections of different objects. Thus there can also be discordant tracklets, with some (but not all) detections in common.

The problems with incomplete tracklets may result from uneven performance of the scheduler, the method used to select the sequence of telescope pointings to collect observations. Optimal scheduling belongs to the class of discrete optimization problems, known to be of non-polynomial complexity; this in practice means the perfect scheduler cannot be available. Uneven spacing between observations of the same area may result in several tracklets of the same object in one night, increasing the complexity of the identification procedure without increasing, in most cases, the quality of the orbits. The orderings used in the identification management, better and much better, may need to be redefined to compensate for this. Too long spacing between detections may result in failure to assemble some of them into tracklets.

One advantage of the identification management procedure is that a significant fraction of the problems with the tracklets can be solved a posteriori, after finding the identification. If two tracklets belong to the same identification, it does not matter if there are common detections, provided the duplicates are removed from the list of observations of the identification. $1 0$ If there are two discordant tracklets, of which one is identified and the other is not, we can assume that the latter is false and discard it; this procedure is called tracklet management.

An important output of the identification management is the list of leftover tracklets. It is obtained by removing from the input list the tracklets belonging to confirmed identifications and those discordant with the identified ones. This allows us to build a list of unidentified tracklets which is shorter and also contains fewer false tracklets.

To control the computational complexity of the method that finds the tracklets discordant with the identified ones, a list of discordant tracklets needs to be prepared with an $\mathcal { O } ( M \log M )$ algorithm (where $M$ is the total number of detections); this is possible by sorting the detections. After identification management this list is scanned, searching for identified tracklets.

# 11.5 Tests for accuracy

The best way to measure the efficiency and accuracy of an orbit determination method applied to a large survey is to run a full-scale simulation. Then we have a ground truth, that is a list of synthetic objects used in data simulation and their assumed orbits, with which the output of the procedure can be directly compared. While processing real data we have no way of knowing how many other identifications may be possible, and false identifications can be long lasting. The performance of the algorithms is strongly dependent upon the number density of detections; the future surveys are designed to achieve a much larger number density of detections than those of the currently available data. The results of these simulations depend upon so many assumptions, many of them implicit, that it is very hard to predict the performance of a future survey. The point is to show that the main limitation to the performance of the next-generation surveys, as far as Solar System objects concerned, is not due to the orbit determination task.

The main purpose of large-scale orbit determination simulation is to measure the accuracy of the procedure. However, efficiency and accuracy are not independent. The quality control parameters may be selected to favor efficiency, sacrificing accuracy. The identification management methods may be effective in removing false identifications, because they are discordant with one another, but in this way a true identification is often sacrificed to remove a false one, decreasing efficiency. Simulations are needed to test different sequences of algorithms, options, and control values to achieve the best possible compromise between efficiency and accuracy.

# Quality control metrics

Accuracy can be increased with a statistical quality control based upon more than just one parameter, trying to capture information not only on the noise component (measured by the RMS) but also on systematic signals left in the residuals. For the full-scale simulations of Milani et al. (2008) we have used the following 10 metrics (control values in square brackets):

normalized RMS of astrometric residuals (the assumed RMS of the observation errors was 0.1 arcsec) [1.0]; RMS of photometric residuals in magnitudes [0.5]; bias of the residuals in RA and in DEC [1.5]; first derivatives of the residuals in RA and DEC [1.5];   
second derivatives of the residuals in RA and DEC [1.5];   
$\bullet$ third derivatives of the residuals in RA and DEC [1.5].

To compute the bias and derivatives of the residuals we fit them to a polynomial of degree 3 and divide the coefficients by their standard deviation as obtained from the covariance matrix of the fit.11

There is a problem in comparing values of the above parameters with fixed control values, because the statistically expected values depend upon the number $m$ of (scalar) observations and the number $n$ of fit parameters, which could be 6, 5, and even 4 (see Section 10.4). One standard way to take this into account is to normalize the control parameters dividing by the factor $\sqrt { m / ( m - n ) }$ before comparing to a fixed control, independent of $m , n$ .

# Simulation results

As an example we give the output of the simulation of Milani et al. (2008), a full density simulation of a next-generation survey over an entire lunation, with limiting magnitude 24 and a large Solar System model (with 11 million objects). This simulation did not include false detections.

In a first iteration, the binary tree algorithm was used to form tracks, which were submitted to differential corrections. Then the resulting list of identifications was normalized. Table 11.1 summarizes the accuracy results, showing that identification management is necessary to reduce the false identifications to the desired very low level, while before normalization there were far too many. It also shows that the false tracklets are very seldom included in identifications. The identification management was also effective in removing false tracklets, e.g., at opposition the leftover tracklets were reduced in number by a fraction 0.743, among them the false tracklets were reduced by a fraction 0.794.

Table 11.1. Accuracy results, before (columns 2–4) and after (columns 5–7) normalization. For each case, the number of false identifications passing quality control, fraction of false, and number of true identifications with false tracklets.   

<table><tr><td rowspan="2">Region</td><td colspan="3">All Identifications</td><td colspan="3">Normalized</td></tr><tr><td>False</td><td>Fraction</td><td>F.Tr.</td><td>False</td><td>Fraction</td><td>F.Tr.</td></tr><tr><td>Opposition</td><td>7093</td><td>0.043</td><td>4</td><td>80</td><td>0.0005</td><td>1</td></tr><tr><td>Sweet spots</td><td>1869</td><td>0.013</td><td>10</td><td>29</td><td>0.0002</td><td>0</td></tr></table>

Table 11.2. Overall and NEA-only identifications. Column 2: number of objects observed on three nights. Column 3: efficiency before normalization. Column 4: efficiency after normalization. Column 5: fraction lost in the first iteration and recovered in a second iteration. Column 6: combined efficiency from both iterations. Column 7: fraction of false identifications after both iterations.   

<table><tr><td></td><td>Total</td><td>Eff.</td><td>Eff. No.</td><td>Recovered</td><td>Eff.tot.</td><td>False Id.</td></tr><tr><td rowspan="2">Opposition NEAs</td><td>161146</td><td>0.973</td><td>0.959</td><td>0.754</td><td>0.990</td><td>0.0006</td></tr><tr><td>353</td><td>0.904</td><td>0.904</td><td>0.853</td><td>0.971</td><td></td></tr><tr><td rowspan="2">Sweet spots NEAs</td><td>144903</td><td>0.980</td><td>0.974</td><td>0.750</td><td>0.994</td><td>0.0002</td></tr><tr><td>271</td><td>0.801</td><td>0.801</td><td>0.852</td><td>0.971</td><td></td></tr></table>

A second iteration based on the recursive attribution algorithm was applied to the list of leftover tracklets, followed by normalization. Table 11.2 shows that the overall efficiency was already high in the first iteration, although the efficiency for the near-Earth asteroids was less so, especially at the sweet spots. Most of the objects observed over three nights and lost by the first iteration were recovered by the second one, especially among NEAs. The recursive attribution method also provided orbits for a fraction $> 0 . 8$ of the objects observed over two nights; these lower quality orbits may be used to be identified with similar orbits from the previous/next lunation, and also for recovery of low confidence detections, see the next section.

In conclusion, the algorithms described in Chapters 8, 9 and 10 and assembled in an identification procedure are adequate for the next-generation sky surveys, even with $N \simeq 3 0 0 0 0 0$ objects discovered in each lunation.12

# 11.6 Recovery of low confidence detections

There is one especially tricky case of attribution, the one in which the data to be attributed are not yet organized into attributables, but are just individual observations. This may occur in very deep surveys, in which the number density of observations per unit area on the sky is extremely high, to the point that pairing them to form tracklets is not easy. If this procedure is pushed to low levels of signal-to-noise ratio, a large fraction of the supposed observations may in fact be spurious. The question is how far down we can push the minimum acceptable S/N to avoid a false identification catastrophe, that is a sharp drop of the accuracy beyond a critical number density.

As a basic form of the problem, let us suppose we have an orbit and two images, taken at two different times $t _ { 1 }$ and $t _ { 2 }$ ; on each image there are $M$ supposed observations, including the spurious ones. By computing from the orbit two predictions $( \alpha _ { i } , \delta _ { i } )$ for the times $t _ { i } , i = 1 , 2$ , we can compare them with the (supposed) observations in each image, computing a simple twodimensional metric $K _ { 2 }$ . This allows us to select by the values of $K _ { 2 }$ a subset of $M _ { i } \ll M$ observations from the frames at time $t _ { i } , i = 1 , 2$ .

If the numbers $M _ { i }$ are small, we can test each of the $M _ { 1 } \times M _ { 2 }$ pairs of observations by forming an attributable (with covariance) and comparing it, by the $K _ { 4 }$ metric, with the predicted attributable for time $t = ( t _ { 1 } + t _ { 2 } ) / 2$ . This procedure may fail if $| t _ { 2 } - t _ { 1 } |$ is too large, because the actual path of the object on the celestial sphere might have enough curvature, so that the tangent vector $( \dot { \alpha } ( \overline { { t } } ) , \dot { \delta } ( \overline { { t } } ) )$ is significantly different from the velocity of the straight line approximation.13 If $M _ { 1 } \times M _ { 2 }$ is too large, we may use the sorting method to find an algorithm of complexity $\mathcal { O } ( M _ { 1 } \ \log M _ { 2 } )$ .

The couples of observations giving a satisfactory value of $K _ { 4 }$ can be submitted to differential corrections, trying to fit the data used to compute the orbit and the two additional observations. The quality control metrics of the fit with the additional observations should not be significantly worse than those without them. When this is achieved, the two observations can be attributed even if there was no way to know a priori that they belonged to an object whatsoever (they could have been spurious).

The computational complexity of the procedure described above is difficult to control. The main reason is that the first filter, based upon the twodimensional metric $K _ { 2 }$ , must be applied searching frame by frame. The second filter with the four-dimensional metric $K _ { 4 }$ has to be applied searching by orbit, that is the detections selected by the first filter have to be sorted in an order different from that in which they have been computed. If all the data passing the first filter, let $Z$ be their number, can be kept in memory, then binary sorting with computational complexity $\mathcal { O } ( Z \log Z )$ can be used to sort by orbit. This results in an algorithm with considerable complexity.

# Recovery simulations

The performance of the above algorithms to recover low confidence detections and promote them to tracklets attributed to available orbits has not been fully tested yet; some simulations are available, but it is difficult to model realistically the occurrence of false detections, which do not really follow simple statistics, like Poisson. One such simulation, with uniform probability density, indicates that the accuracy problem is the main one.

Including false detections with overall number density $\mu = 1 0 ^ { 4 }$ per square degree, $\simeq 1 0 0$ times the number density of the real detections, accuracy in the attribution of a promoted low confidence tracklet in an additional night turns out to be 0.99 when the orbit is based on $\geq 3$ nights of observations and 0.96 for orbits with just two nights of data. At this level the results may be useful, especially for upgrading the weak two-night orbits to threenight orbits, generally well determined, thus possibly complying with some definition of discovery such as the one of Section 10.5.

If $\mu = 1 0 ^ { 5 }$ per square degree, $\simeq 1 0 0 0$ times the real detections, we obtain 0.90 for the accuracy, with $\geq 3$ nights of observations and 0.68 with just two nights of data. Such low reliability identifications cannot be used to claim discovery, especially those which would be most useful, i.e., the two-nighters promoted to three-nighters. They could provide candidate, or probabilistic, discoveries to be confirmed by targeted follow up.

A limitation to the number density cannot be avoided; if $\mu$ is the number density and $\Gamma _ { ( \alpha , \delta ) }$ is the covariance matrix of the predicted observations $\alpha , \delta$ , then the expected number of detections in the confidence ellipse $Z _ { L } ( \sigma )$ is ${ \cal F } = \mu \ \sigma ^ { 2 } \ \pi \sqrt { \operatorname * { d e t } \ \Gamma _ { ( \alpha , \delta ) } }$ , the number of tracklets formed with detections selected in a couple of frames is of the order of $F ^ { 2 }$ , and spurious tracklets with accuracy of the order of $1 / F$ in $\dot { \alpha }$ and $\dot { \delta }$ must often occur. The simulations indicate that the false identification catastrophe does not need to occur in the next-generation surveys, provided the required S/N is such that the number of false detections is not much larger than that of true detections.

# 12

# IMPACT MONITORING

When an asteroid or a comet has just been discovered, its orbit is weakly constrained by the available astrometric observations and it might be the case that an impact on the Earth in the near future (within the next 100 years) cannot be excluded. If additional observations are obtained, the uncertainty of the orbit decreases and the impact may become incompatible with the available information. Thus, if we are aware that an impact is possible, it is enough to spread this information to the astronomers to convince them to follow up the object. On the contrary if this piece of information is not available, or is made available when the asteroid has been lost, the impact risk will remain until the same asteroid is accidentally recovered. This might occur too late for any mitigation action.

This problem can be solved if all the asteroids/comets, immediately after being discovered and before they can be lost, are “scanned” for possible impacts in the near future. If impacts are possible, this information has to be broadcast to the astronomers. This is the goal of impact monitoring.

It is somewhat surprising that this was not really possible until late 1999, when the first impact monitoring system, the CLOMON software robot of the University of Pisa, became operational. For many years, even after the risk of impacts of asteroids and comets on our planet had been identified and its probability estimated, even while dedicated surveys were scanning the sky to discover as many near-Earth asteroids (NEA) and comets as possible, the algorithms to scan a given, known object for possible impacts were not effective enough. By using the linear theory of impact prediction (see Section 12.1) it was possible to identify impact possibilities with comparatively high probability, of the order of $1 0 ^ { - 3 } – 1 0 ^ { - 4 }$ . However, if the possible event was the impact of an asteroid with diameter exceeding 1 km, which would result in an explosion with a yield of more than $2 0 0 0 0$ megatons, even a probability of the order of $1 0 ^ { - 6 } – 1 0 ^ { - 7 }$ cannot be considered negligible, and to omit to follow up such a dangerous asteroid would be a serious mistake. On the contrary, unfounded announcements of possible impacts, such as for asteroid 1997 XF $1 1$ in March 1998, can undermine the credibility of the scientific community involved and thus make it more difficult to obtain the resources necessary in a serious case.

In 1999 we were able for the first time to issue a warning of a possible impact for asteroid 1999 AN $1 0$ (Milani et al. 1999). The impact probability for the year 2039 was $\simeq 1 0 ^ { - 9 }$ , so small that it would not need to be cause of concern for the public, but the mathematical problem had been solved.1 The new methods introduced for the 1999 AN $1 0$ case led to the impact monitoring system CLOMON later in the same year.

In 2002 the impact monitoring system CLOMON was replaced by the second generation CLOMON2 in Pisa (duplicated at the University of Valladolid) and by SENTRY at the NASA Jet Propulsion Laboratory. These two independent systems, whose output is carefully compared, now guarantee that the potentially dangerous objects are identified very early (within hours from the dissemination of the astrometric data) and followed up until the observations succeed in contradicting the possibility of an impact. During the time span over which these observations are obtained, the announcement that some asteroid has the possibility of impacting must be in full view of the public, and in practice it is posted on the web.2 This is essential to communicate the need of observations to the astronomers and also reassures the public that no information on impact risk is withheld.

In case the impact possibility remains for a long time, as it is currently the case for asteroids (99942) Apophis and (144898) 2004 VD $1 7$ , which have been on the risk pages of CLOMON2 and SENTRY for years, it is reasonable to begin planning for the mitigation actions which may become necessary if the later observations were to confirm, rather than contradict, the impact. Although the impact probability is small for these cases, we need to have a technologically feasible method to deflect such asteroids which can be used if necessary, see Section 14.6. Otherwise, the practical utility of the surveys and of the impact monitoring itself would be cast into doubt.

The purpose of this chapter is to outline the mathematical methods used in impact monitoring. It is based on (Milani and Valsecchi 1999, Milani et al. 1999, Milani et al. 2000b, Gronchi 2002, Gronchi 2005, Chesley et al.

2002, Valsecchi et al. 2003, Milani et al. 2005b, Gronchi and Tommei 2006, Gronchi et al. 2007).

# 12.1 Target planes

The geometry of the encounters with a planet can be described in terms of a target plane, a plane in 3-D space through the center of the target planet, e.g., the Earth, orthogonal to the direction of the relative velocity of the approaching small body. In this context, an impact can be described as an orbit containing a target plane point inside the planet cross-section.

There are two ways to define such a target plane. The simplest is the modified target plane (MTP) (Milani and Valsecchi 1999): it is obtained by considering the time $\bar { t }$ at which the small body orbit has a relative minimum of the distance from the planet center of mass (CoM). Let $\mathbf { d }$ and $\mathbf { v }$ be the planetocentric position and velocity vectors of the asteroid at the time $t$ : the distance being minimum, $\mathbf { d } \cdot \mathbf { v } = 0$ . The MTP is the plane containing 0 (the CoM) and normal to $\mathbf { v }$ . On this plane the point $\mathbf { d }$ represents the close approach trace on the MTP. A complete description of the close approach is obtained by assigning two coordinates on the MTP, two angles defining the orientation of the MTP, the size of the velocity $v = | \mathbf { v } |$ , and the time $\bar { t }$ . The cross-section of the planet on the MTP is a disk centered at 0 and with the radius $R$ of the planet; if the minimum distance $d = | \mathbf { d } |$ at time $t$ is less than $R$ there is an impact.3

The other definition, called in the literature either just the target plane (TP) or b-plane, uses the same vectors $\mathbf { d }$ and $\mathbf { v }$ describing the state at the closest approach time $\bar { t }$ to compute a planetocentric two-body approximation of the orbit. If, as it is generally the case, such a two-body orbit is hyperbolic, then the TP is the plane containing 0 and orthogonal to the incoming asymptote of the hyperbola, corresponding to the limit vector $\mathbf { u }$ for $t \to - \infty$ of the planetocentric velocity along the hyperbolic trajectory; the size $u = | \mathbf { u } |$ is the velocity “at infinity” as used in astrodynamics. The point $\mathbf { b }$ , representing the trace of the close approach, is the intersection of the asymptote with the TP; its size $b = | \mathbf { b } |$ is the impact parameter, larger than the minimum distance $d$ by a factor

$$
{ \frac { b } { d } } = { \sqrt { \frac { v ^ { 2 } d } { v ^ { 2 } d - 2 G M } } }
$$

where $G M$ is the gravitational constant multiplied by the planet mass. A complete description of the close approaching orbit is obtained by assigning two coordinates $\xi , \zeta$ on the TP, two angles $\theta , \phi$ defining the orientation of the TP, the size of the escape velocity $u = | \mathbf { u } |$ , and the time $\bar { t }$ (Greenberg et al. 1988). On the TP the impact cross-section is a disk of radius

$$
B = R \sqrt { 1 + 2 G M / R u ^ { 2 } }
$$

larger than the radius $R$ by a factor accounting for gravitational focusing.

The two planes are different, because the velocity $\mathbf { v }$ at the close approach is rotated by an angle $\gamma / 2$ around the axis of the planetocentric angular momentum. The angle $\gamma$ measures the total deflection from the incoming to the outgoing asymptote and can be computed by

$$
\sin ( \gamma / 2 ) = { \frac { G M } { v ^ { 2 } d - G M } } .
$$

The transformation of coordinates rotating and rescaling the MTP into the TP is not canonical, thus it is impossible to use the Hamiltonian formalism including coordinates on the TP (Tommei 2006a, Tommei 2006b). Moreover, the choice of the coordinates on the two planes can be done in different ways, and this has also to be accounted for in the transformation.

From an abstract point of view, it does not matter how we select a representative vector for a given close approach, provided it is a smooth function of the orbit initial conditions: thus a smooth coordinate transformation is acceptable. However, some coordinate systems are more equal than others, because the propagation of the uncertainty is easy in a linear approximation, by using the differential of the transformations, and a coordinate change with large higher order derivatives introduces strong limitations in the applicability of the linearization. Since gravitational focusing introduces a deformation more nonlinear where gravity is stronger, that is near collisions, there is advantage in using the TP with respect to the MTP.

# Linear predictions on target planes

For a given asteroid, and a set of orbital elements $\textbf { x } \in \ \mathbb { R } ^ { 6 }$ at epoch $t _ { 0 }$ there is a unique orbit, which can be accurately propagated for some time span.4 For each close approach to the Earth, occurring within this time span, there is at least one point $\mathbf { y } \in \mathbb { R } ^ { 2 }$ which is the trace of this orbit on the target plane. To avoid useless geometric complications, we consider as close approach only an encounter with a distance from the planet CoM not exceeding some value $d _ { m a x }$ ; practical values for $d _ { m a x }$ range between 0.05 and 0.2 astronomical units (AU), thus the target planes are replaced by disks with a finite radius.5

Let us suppose the orbit determination solves only for the initial conditions $\mathbf { x } \in \mathbb { R } ^ { 6 }$ of the asteroid at some epoch $t _ { 0 }$ , and the differential corrections converge to the nominal solution $\mathbf { x } ^ { * }$ , with normal and covariance matrices $C , \Gamma$ (see Chapter 5). As the nominal solution $\mathbf { x } ^ { * }$ is surrounded by a sixdimensional confidence region of acceptable solutions, the trace point $\mathbf { y } ^ { * } =$ $\mathbf { g } ( \mathbf { x } ^ { * } )$ determined by the propagated nominal orbit on the target plane of some encounter is surrounded by a two-dimensional confidence region.

To compute an approximation, we use the differential of the map $\mathbf { g } ( \mathbf { x } )$ providing the TP trace (Milani and Valsecchi 1999). The trace point is reached at the time $t _ { c } ( \mathbf { x } )$ of the target plane crossing for each orbit with initial conditions $\mathbf { x }$ in a neighborhood of $\mathbf { x } ^ { * }$ . By using Cartesian geocentric coordinates $\xi , \eta , \zeta$ such that $\eta = 0$ is the target plane, the equation $\eta ( t , { \bf x } ) = 0$ implicitly defines the crossing time $t _ { c } ( \mathbf { x } )$ as a differentiable function, thus $\xi ( t _ { c } ( { \bf x } ) , { \bf x } )$ and $\zeta ( t _ { c } ( { \bf x } ) , { \bf x } )$ are differentiable too. Using the differential $D \mathbf { g } ( \mathbf { x } ^ { * } ) = \partial ( \xi , \zeta ) ( \mathbf { x } ^ { * } ) / \partial \mathbf { x }$ we can compute the covariance and normal matrix of the $\mathbf { y }$ prediction by the linear covariance propagation formula

$$
\Gamma _ { \mathbf { y } } = D \mathbf { g } \Gamma _ { \mathbf { x } } ( D \mathbf { g } ) ^ { T } , \quad C _ { \mathbf { y } } = \Gamma _ { \mathbf { y } } ^ { - 1 }
$$

defining the confidence ellipse on the target plane

$$
( \mathbf { y } - \mathbf { y } ^ { * } ) ^ { T } C _ { \mathbf { y } } \ ( \mathbf { y } - \mathbf { y } ^ { * } ) \leq \sigma ^ { 2 }
$$

with the same confidence parameter $\sigma$ used for the confidence ellipsoids. This formalism is applicable because the trace function is differentiable, but this does not imply that the quadratic approximation (12.2) is an accurate description of the confidence region on the target plane. However, if it is adequate, the possibility of an impact can be studied by looking for intersections of the confidence ellipses with the impact cross-section. By using a Gaussian probabilistic formalism, from the normal probability density $N ( \mathbf { x } ^ { * } , \Gamma )$ we can define a probability density on the target plane. In the linear approximation corresponding to the differential $D \mathbf { g } ( \mathbf { x } ^ { * } )$ , $\mathbf { y }$ is Gaussian with density $N ( \mathbf { y } ^ { * } , \Gamma _ { \mathbf { y } } )$ . Then it is possible to estimate the impact probability by computing a probability integral on the impact cross-section.

The formalism above is well known for applications to the navigation of interplanetary spacecraft, a case in which the assumptions of small confidence regions and therefore the applicability of linearization are well founded, for the reasons given in Section 1.4. To estimate the probability of impact of asteroids is much more difficult, due to nonlinearity.

# 12.2 Minimum orbital intersection distance

A convenient reference system ${ \cal O } \xi \eta \zeta$ for the geocentric position on the TP is obtained by aligning the negative $\zeta$ axis with the projection of the heliocentric velocity $\mathbf { v } _ { \oplus }$ of the Earth, the positive $\eta$ axis with the geocentric asymptotic velocity $\mathbf { u }$ (i.e., normal to the TP), and the positive $\xi$ axis in such a way that the reference system is positively oriented. With this frame of reference the TP coordinates $( \xi , \zeta )$ indicate the cross-track and alongtrack miss distances, respectively. In other words, $\zeta$ is the distance by which the asteroid is early or late for the minimum possible distance encounter. The associated “miss time” of the target plane crossing ( $\eta = 0$ ) is $\Delta t = - \zeta / ( v _ { \oplus } \sin \theta )$ , where $\theta$ is the angle between $\mathbf { u }$ and $\mathbf { v } _ { \oplus }$ and $v _ { \oplus } = | \mathbf { v } _ { \oplus } |$ ; a positive $\zeta$ implies that the asteroid is “late” at the date with the Earth, $\zeta < 0$ means the asteroid is early.

On the $b$ -plane the $\xi$ coordinate is the minimum distance that can be obtained by varying the timing of the encounter. This distance is closely related to the orbit distance, known as the minimum orbital intersection distance (MOID) in the literature (Bowell and Muinonen 1994), that is the minimum separation between the two osculating Keplerian orbits of the asteroid and the Earth as curves in three-dimensional space, without regard to the phase on each of the two. Note that the approximation of the MOID with the $\xi$ coordinate is valid only in the linear approximation and can break down for distant encounters (e.g., beyond several lunar distances).

# Stationary points of the Keplerian distance function

Two confocal Keplerian orbits can get close at more than a pair of points, for example near both the mutual nodes, thus it is useful to compute all the local minima of the Keplerian distance function $d$ , the distance between two points on the two orbits, not only the absolute minimum. We compute these values as the stationary points of the function $d ^ { 2 }$ , squared to be smooth also in case of orbit crossing, when the distance can be zero.

There are several papers in the literature on the computation of the minimum points of $d$ , e.g. (Sitarski 1968, Hoots 1994). Recently some algebraic methods to compute all the stationary points of $d ^ { 2 }$ have been introduced, using Gr¨obner bases (Kholshevnikov and Vassiliev 1999) and resultant theory (Gronchi 2002, Gronchi 2005). They are both based on a polynomial formulation of the problem. The algebraic formulation of the problem allows us to search for all the solutions using the efficient methods of modern computational algebra and gives us a bound for the maximum number of stationary points, as discussed below.

# Mutual geometry of confocal Keplerian orbits

The stationary points of $d ^ { 2 }$ have been proven to be $\leq 1 6$ for the case of two ellipses and at most 12 if one orbit is circular, except for very particular cases with infinitely many stationary points (Gronchi 2002). From a large number of numerical experiments we have found cases with at most 12 stationary points of $d ^ { 2 }$ and at most four local MOID, that is local minima of $d ^ { 2 }$ .

The statistics of the stationary and minimum points of the squared distance function $d ^ { 2 }$ using the orbit of the Earth and those of the known NEAs shows that most mutual orbit configurations give two local minima and one maximum, among six stationary points: this is the most intuitive case, with a simple geometry. There are also several cases with only one local minimum. No real asteroid has been found so far with four minimum points.

When there is a crossing between the orbits (MOID $= 0$ ) and the mutual inclination is not zero the minimum point of $d$ corresponds to a mutual node. It is not always the case that at least one local minimum point of $d$ is close to a mutual node: there are examples of real NEAs with two minima, both far enough from the mutual nodes. Such cases arise from orbits with low mutual inclination.

# Uncertainty of the MOID

The role of the MOID in impact monitoring is to select, among the large number (thousands, even tens of thousands) of close approaches possible for a given asteroid, the ones which could be very close. If the TP coordinates have a small value of $\xi$ and a large value of $\zeta$ , then the encounter has not been close, but another orbit with different orbital phase might get in time to the date with the Earth at the local MOID point. If the value of $\zeta$ has a large enough uncertainty, such a phase change could be compatible with the available observations. In a linear approximation, applicable to very close encounters, the confidence ellipse has a major axis almost parallel to the $\zeta$ axis and a minor axis almost parallel to the $\xi$ axis, that is expressing the uncertainty of the local MOID value.

Let $( \mathbf { e } , v )$ be a set of orbital elements such that $\mathbf { e } = ( e _ { 1 } , \ldots , e _ { 5 } )$ describes the geometric configuration of the orbit and $v$ is a parameter along the trajectory, e.g., the true anomaly. The least squares solution gives us a nominal orbit $( \mathbf { e } ^ { * } , v ^ { * } )$ , together with its uncertainty represented by the $6 \times 6$ covariance matrix

$$
\Gamma _ { ( \mathbf { e } , v ) } = \left( \begin{array} { l l } { \Gamma _ { \mathbf { e e } } } & { \Gamma _ { \mathbf { e } v } } \\ { \Gamma _ { v \mathbf { e } } } & { \Gamma _ { v v } } \end{array} \right) ,
$$

which is the inverse of a normal matrix $C _ { ( \mathbf { e } , v ) }$ . The $5 \times 5$ submatrix $\Gamma _ { \mathbf { e e } }$ gives the marginal covariance of the five elements $\mathbf { e }$ , independently from the value of the sixth one $v$ , and $C ^ { \mathbf { e e } } = \Gamma _ { \mathbf { e e } } ^ { - 1 }$ is the marginal normal matrix.

# The minimal distance maps and their singularities

Let $( \mathbf { e } , v )$ be the orbital elements of the asteroid and $( \mathbf { e } _ { \oplus } , v _ { \oplus } )$ those of the Earth, supposedly known with negligible errors. For each configuration $\mathbf { e }$ we consider the minimum points $( v , v _ { \oplus } ) = { \mathbf v } _ { h } ( { \mathbf e } )$ of the Keplerian distance function (assuming $\mathbf { e } _ { \oplus }$ as fixed parameters) and we define the maps

$$
d _ { h } ( \mathbf { e } ) = d ( \mathbf { e } , \mathbf { v } _ { h } ( \mathbf { e } ) ) \mathrm { l o c a l ~ m i n i m a l ~ d i s t a n c e } ,
$$

$$
d _ { m i n } ( \mathbf { e } ) = \operatorname* { m i n } _ { h } d _ { h } ( \mathbf { e } ) \mathrm { o r b i t ~ d i s t a n c e ~ ( M O I D ) . }
$$

where $h$ is an index with a finite number of values.

![](images/57618278cdf70bdd6129b0118a0818c0b941fed66b7d7c3b9439da221769258c.jpg)  
Fig. 12.1. The singularities of the maps $d _ { h }$ and $d _ { m i n }$ can occur in three forms, as described in the text. Reproduced from Gronchi and Tommei (2006).

In Figure 12.1 we show the singularities of $d _ { h }$ and of $d _ { m i n }$ , which belong to three types. Left: $d _ { h }$ and $d _ { m i n }$ are not differentiable where they vanish. Center: in a neighborhood of an orbit configuration $\mathbf { e } ^ { * }$ , two local minima can exchange their role as absolute minimum; then $d _ { m i n }$ can lose its regularity even without vanishing. Right: when a bifurcation occurs the definition of the maps $d _ { h }$ may become ambiguous after the bifurcation point. Note that this ambiguity can occur only where the $2 \times 2$ Hessian matrix of $d ^ { 2 } ( \mathbf { e } , \mathbf { v } )$ is degenerate and does not occur for the $d _ { m i n }$ map.

# Computation of the uncertainty of $d _ { h }$ and $d _ { m i n }$

The errors in the orbit also affect the computation of the local minima of $d$ and it is important to estimate the size of this effect. Let us consider the orbit distance map $d _ { m i n }$ ; the same method can be applied to the minimal distance maps $d _ { h }$ . For a given $( { \mathbf e } ^ { * } , { \mathbf e } _ { \oplus } )$ , the nominal orbit configuration $\mathbf { e } ^ { * }$ being endowed with its covariance matrix $\Gamma _ { \mathbf { e } \mathbf { e } }$ , we can compute the covariance of $d _ { m i n } ( \mathbf { e } ^ { * } )$ by a linear propagation of the matrix $\Gamma _ { \mathbf { e } \mathbf { e } }$ :

$$
\Gamma _ { d _ { m i n } } ( \mathbf { e } ^ { * } ) = \left[ \frac { \partial d _ { m i n } } { \partial \mathbf { e } } ( \mathbf { e } ^ { * } ) \right] \Gamma _ { \mathbf { e } } ( \mathbf { e } ^ { * } ) \left[ \frac { \partial d _ { m i n } } { \partial \mathbf { e } } ( \mathbf { e } ^ { * } ) \right] ^ { T } .
$$

The possibility of crossings between the orbits produces a singularity in this computation because the partial derivatives $\partial d _ { m i n } / \partial \mathbf { e }$ do not exist at $\mathbf { e } ^ { * }$ when $d _ { m i n } ( \mathbf { e } ^ { * } ) = 0$ , e.g., when the two orbits in the configuration $( { \mathbf e } ^ { * } , { \mathbf e } _ { \oplus } )$ intersect each other. Moreover the uncertainty of a non-zero but small orbit distance may allow meaningless negative values of the distance. Note that we are interested in knowing the uncertainty just when the orbit distance can be small or vanishing, that is when a collision or a close approach is possible. Thus the classical covariance propagation formula to compute the uncertainty of the MOID is applicable only when it is not very useful.

# Regularization of the minimal distance maps

We introduce a regularization of the maps $d _ { h }$ , $d _ { m i n }$ , generalizing the approach by Wetherill (1967) and Bonanno (2000). Let us take into account the map $d _ { m i n }$ , the same method can also be applied to $d _ { h }$ . It is possible to make $d _ { m i n }$ locally analytic even where its value is zero, simply by changing its sign according to some properties of the orbit configuration.

The idea of the regularization can be illustrated by a simple example. Let us consider the positive function, defined on the whole plane, $f ( x , y ) =$ $\sqrt { x ^ { 2 } + y ^ { 2 } }$ and the function $\tilde { f }$ , defined on a smaller domain,

$$
\tilde { f } ( x , y ) = \left\{ \begin{array} { l l } { { - f ( x , y ) } } & { { \mathrm { ~ f o r ~ } x > 0 } } \\ { { f ( x , y ) } } & { { \mathrm { ~ f o r ~ } x < 0 . } } \end{array} \right.
$$

The directional derivative of $f$ in $( x , y ) = ( 0 , 0 )$ does not exist for every choice of the direction. The regularized function $\tilde { f }$ , extended by continuity to the origin $( 0 , 0 )$ , has all the directional derivatives in $( x , y ) = ( 0 , 0 )$ . How to extend such a method to the problem at hand is discussed below.

# Geometric definition of the regularization

Let $\tau _ { 1 }$ , $\tau _ { 2 }$ be the tangent vectors to the orbits at the minimum point and let $\Delta _ { m i n }$ be the vector joining the two tangency points ( $| \pmb { \Delta } _ { m i n } | = d _ { m i n }$ ). If $\tau _ { 1 }$ is not parallel to $\tau _ { 2 }$ we can define the non-zero vector $\tau _ { 3 } = \tau _ { 1 } \times \tau _ { 2 }$ . Due to the stationary points properties, if $\Delta _ { m i n } \neq 0$ , $\Delta _ { m i n }$ is parallel to $\mathbf { \tau _ { 3 } }$ . We define the regularized map $\tilde { d } _ { m i n }$ by setting $| \bar { d } _ { m i n } | = d _ { m i n }$ and choosing the sign $^ +$ for $\tilde { d } _ { m i n }$ if $\Delta _ { m i n }$ and $\mathbf { \tau _ { 3 } }$ have the same orientation, the sign $-$ otherwise. This sign is well defined, with the only exception of the cases in which $\tau _ { 1 }$ and $\mathbf { \sigma } _ { \mathbf { \lambda } ^ { T } 2 }$ are parallel. Then we extend the definition domain to most crossing orbits setting $\tilde { d } _ { m i n } = 0$ if $d _ { m i n } = 0$ . The orbit configurations with parallel tangent vectors to minimum points are also excluded from the definition domain even if they are not crossing points. The resulting map $\mathbf { e } \mapsto \bar { d } _ { m i n } ( \mathbf { e } )$ is locally analytic almost everywhere, without excluding a neighborhood of most orbit configurations $\mathbf { e }$ such that $d _ { m i n } ( \mathbf { e } ) = 0$ . In particular the partial derivatives can be computed as

![](images/12fcbc9c1dcbbd9e77f29036122ea772ad1e953f40271d756a6c8cbb7c5756f1.jpg)  
Fig. 12.2. Geometry of the regularization: the orientation of the two parallel vectors $\Delta _ { m i n }$ , $\mathbf { \hat { \mathbf { \eta } } } ^ { \ T } \mathbf { 3 }$ is the key to defining a regular map $\bar { d } _ { m i n }$ by simply changing the sign of $d _ { m i n }$ on selected configurations $\mathbf { e }$ . Reproduced from Gronchi and Tommei (2006).

$$
\frac { \partial \tilde { d } _ { m i n } } { \partial e _ { k } } ( { \bf e ^ { * } } ) = \left. \frac { \tau _ { 3 } ( { \bf e ^ { * } } ) } { | \tau _ { 3 } ( { \bf e ^ { * } } ) | } , \frac { \partial \Delta } { \partial E _ { k } } ( { \bf e ^ { * } } , { \bf v } _ { m i n } ( { \bf e ^ { * } } ) ) \right. \qquad k = 1 \ldots { 1 } \ldots 5
$$

where $\mathbf { v } _ { m i n } ( \mathbf { e } ^ { * } )$ is the absolute minimum point and $\Delta ( \mathbf { e } , \mathbf { v } )$ is the vector joining the points corresponding to $v$ and $v _ { \oplus }$ on the orbit of the asteroid and of the Earth respectively.

Thus it becomes possible to use for the smooth function $\bar { d } _ { m i n } ( \mathbf { e } )$ the standard covariance propagation formula, applicable only to differentiable functions, including the interesting low MOID cases. For each nominal orbit configuration $\mathbf { e } ^ { * }$ , with covariance matrix $\Gamma _ { \mathbf { e } \mathbf { e } }$ , we can compute the variance of $\bar { d } _ { m i n } ( { \bf e } ^ { * } )$ a s

$$
\Gamma _ { \tilde { d } _ { m i n } } ( \mathbf { e } ^ { * } ) = \left[ \frac { \partial \tilde { d } _ { m i n } } { \partial \mathbf { e } } ( \mathbf { e } ^ { * } ) \right] \Gamma _ { \mathbf { e } } ( \mathbf { e } ^ { * } ) \left[ \frac { \partial \tilde { d } _ { m i n } } { \partial \mathbf { e } } ( \mathbf { e } ^ { * } ) \right] ^ { T }
$$

by using the smooth partial derivatives of eq. (12.4).

The above statement needs to be taken with some caution. It is necessary to check that the singular case ( $\tau _ { 1 }$ parallel to $\boldsymbol { \tau _ { 2 } }$ ) does not occur at $\mathbf { e } ^ { * }$ and is not even within the confidence ellipsoid. We need to check the variance of the determinant of the Hessian matrix to look for possible bifurcations of the stationary points. Last but not least, the propagation of the covariance by the linear formula of eq. (12.5) may be mathematically consistent, but to assume $\bar { d } _ { m i n } ( \mathbf { e } )$ is a Gaussian random variable is a good approximation only provided the function $\tilde { d } _ { m i n }$ is quasi-linear, which does occur when the uncertainty on $\mathbf { e }$ is small, see (Gronchi et al. 2007).

# Potentially hazardous asteroids

Bowell and Muinonen (1994) define a potentially hazardous asteroid (PHA) as an asteroid having MOID $( = | \tilde { d } _ { m i n } | ) \leq 0 . 0 5$ AU and absolute magnitude $H \leq 2 2$ ; these are the most relevant objects for impact monitoring. However, this definition refers only to the nominal orbits and does not take into account the uncertainty. To be complete, we should consider all the virtual hazardous asteroids, that is asteroids that have a significant probability of being a PHA, taking into account the joint probability density function of the variables $( \tilde { d } _ { m i n } , H )$ . The use of the regularized minimal distances $\tilde { d } _ { h }$ is essential for this purpose; for small nominal values of $d _ { h }$ also negative values $> - 0 . 0 5$ have to be considered.

The probability that $\tilde { d } _ { h }$ belongs to $\left\lfloor - 0 . 0 5 \mathrm { A U } , 0 . 0 5 \mathrm { A U } \right\rfloor$ is

$$
\mathcal { P } \left( | \tilde { d } _ { h } | \leq 0 . 0 5 \mathrm { A U } \right) = \frac { 1 } { \sqrt { 2 \pi } } \int _ { z _ { 1 } } ^ { z _ { 2 } } \exp ( - z ^ { 2 } / 2 ) d z
$$

with

$$
z _ { i } = \frac { x _ { i } - \tilde { d } _ { h } ( { \bf e ^ { * } } ) } { \sigma _ { \tilde { d } _ { h } } ( { \bf e ^ { * } } ) } \qquad ( i = 1 , 2 )
$$

where $x _ { 1 } = - 0 . 0 5$ , $x _ { 2 } = + 0 . 0 5$ and $\sigma _ { \tilde { d } _ { h } } \left( \mathbf { e } ^ { * } \right)$ is the standard deviation of ${ \tilde { d } } _ { h }$ , defined by

$$
\sigma _ { \tilde { d } _ { h } } ( \mathbf { e } ^ { * } ) = \sqrt { \Gamma _ { \tilde { d } _ { h } ( \mathbf { e } ^ { * } ) } } .
$$

The variance $\Gamma _ { H H }$ of the absolute magnitude depends both on the photometry and astrometry, because it is computed from the apparent magnitudes by a formula involving the topocentric distance of the object. Given the variance $V _ { p h o t }$ of the photometry, assuming it is independent of the astrometry, we can decide if a celestial body is a virtual hazardous asteroid by looking at the $2 \times 2$ covariance matrix

$$
{ \bf \Pi } _ { \nu i n , H ) } ( \mathbf { e } ^ { * } ) = \frac { \partial ( \tilde { d } _ { m i n } , H ) ( \mathbf { e } ^ { * } ) } { \partial \mathbf { e } } \Gamma _ { \mathbf { e } } ( \mathbf { e } ^ { * } ) \left[ \frac { \partial ( \tilde { d } _ { m i n } , H ) ( \mathbf { e } ^ { * } ) } { \partial \mathbf { e } } \right] ^ { T } + \left( \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { V _ { p h o t } } \end{array} \right)
$$

computed at the nominal orbit configuration $\mathbf { e } ^ { * }$

# 12.3 Virtual asteroids

When an asteroid has been discovered only recently, or anyway has been observed only for a short time span, the orbit of the real object may belong to a large confidence region. Another way to describe our (lack of) knowledge is by using a swarm of virtual asteroids (VA), with slightly different orbits all compatible with the observations, that is belonging to the confidence region. The reality of the asteroid is shared among the virtual ones, in the sense that only one of them is real, but we do not know which one. Since the confidence region contains a continuum of orbits, each VA is in turn representative of a small region, i.e., its orbit is also uncertain, but to a much smaller degree. This smaller uncertainty enables us to use for each VA some local algorithms, which would not apply to the entire confidence region. Note that the nominal orbit is just one of the VAs, and is not extraordinary in this context.

The $N .$ -body problem not being integrable, there is no way to compute globally the totality of orbits of the confidence region; only a finite set of orbits can be numerically propagated. The reason for using a swarm of VAs is that they are a finite set of orbits, which can be propagated one by one, representing the totality of orbits compatible with the observations much better than the nominal solution alone. Moreover, by propagating together with the orbits the corresponding state transition matrices, we can use a linear approximation in a neighborhood of each VA: it is not easy to decide how many such points are needed to keep up with strong nonlinearities.

Thus the critical issue is how to sample the confidence region in an efficient way, that is with few orbits $_ 6$ but selected in such a way that they are as far as possible representative of the different possible orbits. There are two classes of sampling methods used in the selection of VA: the random, or Monte Carlo (MC) methods, and the geometric sampling methods, in which the sampling takes place on the intersection of a geometric object, a differentiable manifold, with the confidence region.

The MC methods directly use the probabilistic interpretation of the least squares principle. Since the orbit determination process yields a probabilistic distribution in the space of orbital elements, the distribution can be randomly sampled to obtain a set of equally probable VAs. They will be more dense near the nominal solution, where the probability density is maximum, and progressively less dense as the RMS of the residuals increases (Chodas and Yeomans 1996). This can be implemented in different ways, by using a random number generator to sample an assumed probability density either in the space of the elements $\mathbf { x }$ , or in the space of all residuals $\boldsymbol { \xi }$ , or in some appropriate combination of the two as in statistical ranging (Virtanen et al. 2001).

When the computational resources are not an issue and the probabilistic error models are reliable, the MC methods are more rigorous and complete, thus they are often used for checking the results once a case of possible impact has been identified. If by impact monitoring we mean checking all newly discovered, or anyway re-observed, asteroids for the possibility of a future impact, then computational complexity is the main concern and the MC methods are too slow, thus the geometric sampling methods have to be used. In this chapter we will concentrate on the one-dimensional sampling methods, in which the geometric object is a smooth line sampled by a regular sequence of intervals. More complex sampling methods, such as two-dimensional ones using a surface of variations, have been proposed (Tommei 2005) but are not yet being used in operational impact monitoring.

# The line of variations as geometric sampling

As discussed in Sections 5.6 and 7.3, some years after the epoch of initial conditions the confidence region becomes stretched in the along-track direction; for asteroids with low MOID, this effect is stronger because of the chaotic orbit, with a typical Lyapounov time of the order of the average time span between two close approaches to a major planet (Whipple 1995). Since the goal of impact monitoring is to find possible impacts with a long warning time (tens of years, longer than the Lyapounov time), the best way to sample the confidence region is by defining a curve which intuitively can be the “spine” of such an elongated confidence region.

The solution adopted by Milani et al. (1999) and used in the current impact monitoring systems is to use a sampling of the line of variations (LOV), see Section 10.1, as a set of virtual asteroids. The main advantage of this approach is that the set of VA has a geometric structure, that is they belong to a differentiable curve along which interpolation is possible. Thus the methods of impact monitoring are a version of manifold dynamics, in which a smoothly parameterized set of orbits is implicitly propagated.

The problem with the LOV is that it is not independent of the choice of coordinates in the space of initial conditions $\mathbf { x }$ (Section 10.3). Thus we have to choose the coordinate system which makes the LOV most representative of the set of orbits filling the confidence region, and this depends upon the purpose of the sampling. For impact monitoring we are interested in predictions for times much later than the initial conditions, then in most cases the important changes in the orbit elements are those in the semimajor axis, and the metric should be chosen accordingly.7

# The LOV trace on the target planes

Once the LOV sampling has been computed, we have a set of VAs $\mathbf { x } _ { i }$ for $1 \leq i \leq 2 k + 1$ ; let us assume the LOV points have been computed with a uniform spacing $h$ in the LOV parameter $\sigma$ , thus $\mathbf { x } _ { i }$ corresponds to the value $\sigma _ { i } = ( i - k - 1 ) \cdot h$ . By propagating each of the VA orbits for a given time span (80–100 years), we record for each VA all the close approaches to the Earth within the distance $d _ { m a x }$ . Each close approach is represented by at least one trace point $\mathbf { y } = ( \boldsymbol { \xi } , \boldsymbol { \zeta } )$ on the TP. Up to this point the procedure is the same, whatever the sampling method.

Since the LOV sampling is not just a set of points, we can exploit the facts that they sample a smooth line and the trace of the LOV on the TP is also a smooth line. Let us suppose that two consecutive VAs, $\mathbf { x } _ { i }$ and $\mathbf x _ { i + 1 }$ , have TP trace points $\mathbf { y } _ { i }$ and $\mathbf { y } _ { i + 1 }$ straddling the Earth impact cross-section, such that the trace point ${ \bf y } _ { i }$ is “early”, that is $\zeta _ { i } < 0$ , while $\mathbf { y } _ { i + 1 }$ is “late”, $\zeta _ { i + 1 } > 0$ . Then there is one point $\mathbf x _ { i + \delta }$ on the LOV (as a continuous curve) corresponding to the parameter $\sigma = ( i - k - 1 + \delta ) h$ , with $0 ~ < ~ \delta ~ < ~ 1$ , such that $\zeta _ { i + \delta } = 0$ ; this must occur provided the trace of the LOV segment between ${ \bf y } _ { i }$ and $\mathbf { y } _ { i + 1 }$ lies entirely within the distance $d _ { m a x }$ from the Earth CoM. This is the first instance of the principle of the simplest geometry we will further discuss in the next section: cases with strong nonlinearities, so that the function $\zeta ( \sigma )$ is not defined in the interval $[ \sigma _ { i } , \sigma _ { i + 1 } ]$ , are possible, but this is less frequent than the simple case in which the segment joining ${ \bf y } _ { i }$ to $\mathbf { y } _ { i + 1 }$ behaves like a straight line.

The point $\mathbf x _ { i + \delta }$ on the LOV, which was not among the original set of VAs, can be computed by using some iterative method such as regula falsi (see the next section). If the TP trace $\mathbf { y } _ { i + \delta }$ is inside the Earth impact cross-section, then around $\mathbf x _ { i + \delta }$ there is a virtual impactor (VI), that is a connected set of initial conditions leading to an impact (at about the same date). If the point $\mathbf { y } _ { i + \delta }$ is outside the impact cross-section, but the width $w$ of the confidence ellipse computed by linearizing at $\mathbf { y } _ { i + \delta }$ is large enough, there is an intersection between the confidence ellipse and the impact cross-section and there is anyway a VI, with initial conditions not belonging to the LOV.

By computing the probability density function with a suitable Gaussian approximation centered at $\mathbf x _ { i + \delta }$ it is possible to estimate the probability integral on the impact cross-section, that is the impact probability (IP) associated with the given VI. These computations are approximate, but when the IP is low they are better than the estimates done with MC type sampling; the MC estimates based upon the number of impacting VA suffer from the uncertainties of small number statistic, e.g., a MC sampling is likely not to provide any impacting VA if the number of VAs is less than 1/IP. On the contrary, the geometric sampling methods described here can detect VIs with IP of the order of $1 0 ^ { - 7 } – 1 0 ^ { - 8 }$ (and even less, as in the 1999 AN $_ { 1 0 }$ case) starting from a few thousands of VAs on the LOV. The issue of completion in the searches for VIs is more complex and needs to be discussed in the context of the geometric theory of the next section.

# 12.4 Target plane trails

To understand the properties of the TP trace of the LOV we need to use the finite sample formed by the trace points $\mathbf { y } _ { i }$ as markers of a geometric structure. To do this, after computing all the close approaches to the Earth for all the VAs $\mathbf { x } _ { i }$ , we sort them by the time of the closest approach. The recorded close approaches cluster around a discrete set of encounter times, associated to passages of the Earth through the point corresponding to the (local) MOID while the asteroid is neither very late nor very early at its (local) MOID point. Each of these clusters of close approaches forms a shower, and a shower is represented as a set of trace points on the TP.

In some cases, corresponding to comparatively slow encounters, the situation can be somewhat more complicated, see (Milani et al. 2005b, Figure 6), but let us assume this decomposition of the set of close approaches into showers has been obtained. Next we decompose each shower into contiguous LOV segments; this is easily obtained by sorting the shower according to the index $i$ . A subset of a shower with contiguous indexes $i$ is a trail. In some cases a trail is a singleton, formed by just one of the selected VAs.

![](images/eaf6b3b367c3b19578b55989f103f94abe3cb9a6eea067b4d789d01a7f8cbcd5.jpg)  
Fig. 12.3. A single shower with five trails for the asteroid 1998 OX $^ 4$ in January 2046. The Earth is depicted by the “ $\oplus$ ”. The two diamonds that are connected by the dotted line actually correspond to a trail with collision, emphasizing that care must be taken when interpolating between solutions. Note the axes have different scales, thus the trails are very close to each other. These trails have been computed by using only the observations obtained in 1998; the asteroid was recovered in 2002 and the new observations have shown that there is no risk of impact. Reprinted from Milani et al. (2000b) with permission from Elsevier.

Figure 12.3 shows the trace on the TP for a shower containing five trails, including one singleton and a “pair” with just two TP points.

# The principle of the simplest geometry

We can conjecture that a trail with $h \leq i \leq k$ corresponds to a continuous set, a segment of the LOV, with a corresponding curve segment of TP trace points joining $\mathbf { y } _ { h }$ to $\mathbf { y } _ { k }$ . Because of the finite sampling, we cannot prove that this must be the case. This hypothesis could be verified by densifying the LOV sampling: if some of the new VAs miss the TP, that is do not have a close approach (within $d _ { m a x }$ ) around the same date, we cannot exploit the differentiable structure of the LOV. However, if such a TP segment of a differentiable curve exists, we can draw very important conclusions.

Let us take as an example the “doubleton” of Figure 12.3. To interpolate linearly between the two extremes ${ \bf y } _ { i }$ and $\mathbf { y } _ { i + 1 }$ (dotted line in the figure)

is obviously a very poor approximation; the trails with more TP points do suggest a significant curvature of the TP trace curves. We can use additional information: the map from the LOV to the TP is differentiable and we can compute the tangent vector $\mathbf { s } ( \sigma ) = d \mathbf { y } ( \sigma ) / d \sigma$ to the TP trace curve at the point $\mathbf { y } _ { i } = \mathbf { y } ( \sigma _ { i } )$ ; the length $s = | \mathbf { s } |$ is the stretching. Let $\mathbf { s } ( \sigma _ { i } ) = \mathbf { s } _ { i }$ ; if the angle between ${ \bf s } _ { i }$ and the vector to the origin $- \hat { \mathbf { y } } _ { i }$ is $< \pi / 2$ , then the closest approach distance is decreasing for increasing values of the LOV parameter $\sigma$ at the value $\sigma _ { i }$ corresponding to $\mathbf { x } _ { i }$ . The same computation can be done for $\mathbf x _ { i + 1 }$ , and if the angle between $\mathbf { s } _ { i + 1 }$ and $- \mathbf { y } _ { i + 1 }$ is $> \pi / 2$ the closest approach distance increases with $\sigma$ at the value $\sigma _ { i + 1 }$ . If the TP trace segment joining continuously ${ \bf y } _ { i }$ to $\mathbf { y } _ { i + 1 }$ exists, then there is for some value of $\sigma$ in the interval $( \sigma _ { i } , \sigma _ { i + 1 } )$ a local minimum of the closest approach distance.

In conclusion, if we make the assumption that the behavior of the TP curve is simple, more exactly as simple as it is compatible with the existing decomposition of the shower into trails, we expect to have at least one local minimum of the closest approach distance for each trail. This is why we adopt the principle of the simplest geometry, by which the curve segment does not exit the TP disk of radius $d _ { m a x }$ ; then there needs to be at least one minimum of the closest approach distance. We can define constructive algorithms for the determination of at least one minimum. Note that it is also an assumption that such a minimum is unique for each trail. In the case of the “doubleton” of Figure 12.3 the minimum is such that there is a VI, but this cannot be confirmed by using a linear approximation.

In fact, the shape of the TP trace curve between two given VAs can be much more complex than the simplest geometry, in which case the convergence of the minimum-finding algorithms and/or the uniqueness of the local minimum may fail. However, if the TP trace curve has extreme nonlinearities over a very short segment of the LOV, that implies the stretching is large and thus the IP is low. This is a robust qualitative argument, that is the VIs we can find by using this method have larger IP than those we can miss, but unfortunately we have not yet been able to transform it into a quantitative argument, that is into an estimate of the maximum IP of the missed VIs. Thus we do not yet have an analytical estimate of the maximum IP for which we can guarantee completion in the search for VIs.

# Returns to close approach

Another application of the principle of the simplest geometry can be appreciated from the trail with 5 TP points near the bottom of Figure 12.3. Also in this case the first and last TP point of the trail, $\mathbf { y } _ { i }$ and $\mathbf { y } _ { i + 4 }$ , correspond to decreasing and increasing closest approach distance, respectively. Thus, if the TP trace curve segment joins ${ \bf y } _ { i }$ and $\mathbf { y } _ { i + 4 }$ without exceeding the distance $d _ { m a x }$ , then it must have at least one point with minimum closest approach distance. However, the behavior of the TP trace curve cannot be approximated by a straight line and the map between the confidence region for the initial conditions $\mathbf { x }$ and the TP points $\mathbf { y }$ is strongly nonlinear, because there is a fold line where the differential of the map $\mathbf x \mapsto \mathbf y$ is degenerate (Milani et al. 2005b). The closest approach distance decreases to a minimum, then increases again, because the TP trace “turns back”.

A return is a trail with the additional condition that the VAs forming it have experienced another close approach between the times of the available observations and the times of the close approaches belonging to the trail. Among the returns there are those such that the intermediate close approach is to the same planet and has occurred near the same local MOID point of the close approaches belonging to the return (e.g., both near the ascending node for a high inclination orbit). That implies the Earth is near the same value of the mean anomaly in the intermediate and in the return encounter, i.e., the close approach occurs at about the same date in different years. Also the asteroid needs to be near the same anomaly to be close to the MOID point along its orbit. The time span $\Delta t$ between the two encounters needs to be close to an integer multiple of the Earth orbital period and to an integer multiple of the asteroid period, thus the two orbits must be nearly resonant. This is the motivation for the name resonant return (Milani et al. 1999).

We have developed an analytical theory, based upon the Opik formal- ¨ ism for planetary encounters, describing in a qualitative and approximately quantitative way the shape of the TP trace curves associated to returns, in particular for resonant returns (Valsecchi et al. 2003). This is possible because there is a comparatively simple analytical formula approximating the change in the asteroid semimajor axis resulting from the intermediate encounter, as a function of the coordinates $( u , \theta , \xi , \zeta )$ . Without going into long details, it is enough to point out that each intermediate encounter can generate as many as four “turning back points” in the TP trace curves of successive encounters. Non-resonant returns to the same planet (e.g., after a close approach near the other node) and even encounters with another planet can also generate reversals. Thus the behavior of the bottom trail of Figure 12.3 is by no means exceptional, rather generic, and the principle of the simplest geometry does not exclude it. We conclude that the algorithms to find local minima of the close approach distance for each trail must be able to cope with this case, thus they must not assume that the $\mathbf x \mapsto \mathbf y$ map is locally well approximated by a linear map.

# Algorithms for the minimum close approach distance

By assuming the principle of the simplest geometry, each value of the LOV parameter $\sigma$ belonging to a segment $( \sigma _ { j } , \sigma _ { k } )$ corresponds to a point of the TP trace differentiable curve $\mathbf { y } ( \sigma )$ joining the TP points $\mathbf { y } _ { j }$ and $\mathbf { y } _ { k }$ . For each of these values of $\sigma$ we can compute the squared distance to the center of the Earth on the TP, that is $b ^ { 2 } ( \sigma ) = \mathbf { y } ( \sigma ) \cdot \mathbf { y } ( \sigma )$ , and its derivative $f ( \sigma ) =$ $d b ^ { 2 } / d \sigma = 2 { \bf s } ( \sigma ) \cdot { \bf y } ( \sigma )$ with respect to the LOV parameter $\sigma$ . Then we can search the set of TP points $y _ { i }$ , $j \le i \le k$ , to find the couples of consecutive indexes $i , i + 1$ where the signs are discordant, $f ( \sigma _ { i } ) < 0$ and $f ( \sigma _ { i + 1 } ) > 0$ , then there is at least one value of $\sigma ^ { * } \in ( \sigma _ { i } , \sigma _ { i + 1 } )$ such that $f ( \sigma ^ { * } ) = 0$ . The algorithm of regula falsi provides an approximate value of $\sigma ^ { * }$ :

$$
\sigma ^ { * } \simeq \sigma _ { i } + \delta = \sigma _ { i } - \frac { f ( \sigma _ { i + 1 } ) - f ( \sigma _ { i } ) } { \sigma _ { i + 1 } - \sigma _ { i } } .
$$

A step of length $\delta$ is performed with the same formula $\mathbf { x } ^ { \prime } = \mathbf { x } _ { i } + \delta \sigma _ { 1 } \mathbf { v } _ { 1 }$ used for the original VA sampling, then constrained differential corrections are used to obtain a LOV point which is taken as $\mathbf x _ { i + \delta }$ . If the corresponding TP trace $\mathbf { y } _ { i + \delta }$ is not the minimum distance point along the LOV trace, that is $f ( \sigma _ { i } + \delta )$ is significantly $\neq 0$ , the procedure is iterated on the interval with extremes $\sigma _ { i } + \delta$ and either $\sigma _ { i }$ or $\sigma _ { i + 1 }$ , in such a way that the signs of $f$ at these extremes are discordant. At convergence we obtain a LOV point of (local) minimum of the close approach distance; if $f$ is defined in the whole interval $[ \sigma _ { i } , \sigma _ { i + 1 } ]$ , that is the TP trace is always within the disk of radius $d _ { m a x }$ , this regula falsi iteration has guaranteed convergence.

The difference with the procedure of the previous section is that no assumption needs to be done on the direction and curvature of the TP trace curve. Indeed, in resonant returns the TP trace curve may never cross the $\zeta = 0$ line, because it “turns back” before crossing it. Thus the minimum distance may be much larger than the local MOID, e.g., the two cases in Figure 12.3 of the “doubleton” and of the resonant return can be handled without problems. In other cases the curve may turn back after crossing the $\zeta = 0$ line, with a double minimum of the close approach distance. These different cases need to be handled with an adaptive algorithm, able to identify the simplest geometry of the TP trace curve compatible with the available sampling and to take the necessary action, that is selecting additional sampling points to be used as initial conditions for iterative procedures to reach multiple local minima. The case of a singleton TP trace $\mathbf { y } _ { j }$ has to be handled with a different iterative procedure, which is a modification of Newton method on the variable $\sigma$ with bounded increment (Milani et al. 2005b).

# 12.5 Reliability and completion of impact monitoring

Whenever one of the TP points $\mathbf { y } _ { 0 }$ of local minimum (in the close approach distance along the LOV) is within the Earth impact cross-section, we have a virtual impactor representative, that is an explicitly computed set of initial conditions $\mathbf { x } _ { 0 }$ compatible with the observations and leading to a collision at a given date. Whether the simpler algorithm, described in Section 12.3, or the more robust algorithm of Section 12.4 has been used does not matter: once found, the VI representative is a proof that the collision can occur, and the problem is how to associate an IP to the VI. Linearization at $\mathbf { y } _ { 0 }$ of some Gaussian probability density is the only algorithm available and efficient enough to be used in operational impact monitoring, although targeted investigations with denser VA sampling and/or localized Monte Carlo are possible and are used in difficult cases, when there is significant nonlinearity in a neighborhood of the VI representative.

A delicate case is when $\mathbf { y } _ { 0 }$ is outside the impact cross-section, but the TP confidence ellipse computed by linearizing at $\mathbf { x } _ { 0 }$ does contain collisions. In this case an explicit representative of the VI is not available; the linearization can be of questionable accuracy, especially when the second largest eigenvalue of $\Gamma _ { \mathbf { y } }$ is large, thus the width $w$ of the TP confidence ellipse is large. Both including and excluding these cases from the list of VIs can be a mistake.

For the CLOMON2 impact monitoring system we have developed a method to confirm possible VIs by an iterative procedure which has shown the capability to converge to a VI representative, in most cases in which such a VI exists. It is based on a modified Newton method, first proposed by Milani et al. (2000c). If $\mathbf { y } _ { 0 }$ is the point on the LOV TP trace with minimum distance from the Earth, corresponding to the initial condition $\mathbf { x } _ { 0 }$ , but $| \mathbf { y } _ { 0 } | > B$ , see equation (12.1), we select a point $\mathbf { y } _ { 1 } ^ { \prime }$ on the TP with $| \mathbf { y } _ { 1 } ^ { \prime } | = B$ , e.g., by moving radially. Then we find the point $\mathbf { x } _ { 1 }$ in the confidence region near $\mathbf { x } _ { 0 }$ with the minimum penalty among those projecting into $\mathbf { y } _ { 1 } ^ { \prime }$ on the TP, using the differential of the $\mathbf x \mapsto \mathbf y$ map at $\mathbf { x } _ { 0 }$ ; this is obtained by the same algorithm used in semilinear predictions (see Section 7.5). Then the TP trace $\mathbf g ( \mathbf x _ { 1 } ) = \mathbf y _ { 1 }$ is computed, and it is not $\mathbf { y } _ { 1 } ^ { \prime }$ because of the nonlinearity, but by iterating this procedure the convergence to a VI representative is possible. The difficult point is to define a criterion to terminate the above iterative procedure when convergence is not achieved. Such “divergence” should provide a good indication that the intersection of the linear confidence ellipse and the impact cross-section was a “spurious” VI, see (Milani et al. 2005b).

# Generic completion

How complete is the search for VIs? This is a difficult question to answer rigorously, but it can be useful to understand how efficient a system could be under idealized circumstances. Specifically, we can ask what is the highest impact probability of a VI which could possibly escape detection if the associated trail on the TP is fully linear; we also assume that the width is small with respect to the size of the Earth impact cross-section. This we call the generic completion level of the system.

To obtain this maximum IP, we assume the VI is a very narrow strip passing through the origin of the TP, with a length $2 B _ { \oplus } > 2 R _ { \oplus }$ , depending upon the gravitational focusing. If a sufficient number of VAs intersects the target plane disk of radius $d _ { m a x }$ , then the methods described in the previous subsection will reveal the VI. Otherwise, the VI will be missed in the scan.

The generic completion level is given by

$$
\mathrm { I P ^ { * } } = \frac { \delta p 2 B _ { \oplus } } { \Delta \mathrm { T P } }
$$

where $\delta p$ is the probability integral between TP trace points and $\Delta \mathrm { T P }$ is the maximal separation between TP trace points for which a VI detection is assured; $\Delta \mathrm { T P } \simeq s \Delta \sigma$ , where $s$ is the stretching and $\Delta \sigma$ is the separation of the consecutive VAs in terms of the LOV parameter $\sigma$ .

For CLOMON2, $d _ { m a x } = 0 . 2$ AU, and, under the linearity hypothesis, only one point on the TP is required to detect a VI. Thus the spacing of consecutive VAs on the target plane cannot be more than $0 . 4 \mathrm { ~ A U } \simeq 9 4 0 0 R _ { \oplus }$ . By sampling 2400 VAs over the interval $| \sigma | \le 3$ on the LOV, these points are separated by $\Delta \sigma = 0 . 0 0 2 5$ , and the maximum cumulative probability over one interval is $\delta p = \Delta \sigma / \sqrt { 2 \pi } \simeq 0 . 0 0 1$ (near the nominal, where the Gaussian probability density is $\simeq 1 / \sqrt { 2 \pi }$ ). From this we can compute the CLOMON2 generic completion,

$$
\mathrm { I P } ^ { * } \simeq \frac { 0 . 0 0 2 ~ B _ { \oplus } } { 9 4 0 0 ~ R _ { \oplus } } \simeq 2 . 1 \times 1 0 ^ { - 7 } \frac { B _ { \oplus } } { R _ { \oplus } } .
$$

Thus the generic completion level depends upon the amount of gravitational focusing, and can be higher for asteroids with a low velocity at infinity, $u$ . A somewhat smaller value applies to SENTRY, currently not handling singletons but using more VAs. VIs with IP well below IP $^ *$ can be found, and are indeed found very often, but their detection is probabilistic, depending upon some VA crossing by chance the TP disk.

# 12.6 The current monitoring systems

The impact monitoring software robots CLOMON2 and SENTRY have been operational since early 2002. They handle on average about 100 cases per year: each case begins with the impact monitoring, either by CLOMON2 or by SENTRY, finding at least one VI for either a newly discovered or a re-observed asteroid. In most cases, these results are immediately posted on the web. In the most serious cases $^ 8$ the two impact monitoring systems crosscheck their results before announcing the existence of a VI: this procedure takes typically just a few hours. Anyway, after the public announcement of a risk case, the astronomical community takes action by performing follow up observations until enough information is available to exclude the possibility of impacts in this century. In a fraction of cases, the asteroids have been lost while still having VIs; however, these are generally small asteroids ( $< 1 0 0$ m diameter), indicating that the telescopes available for this targeted follow up might not have been large enough. It is expected that this rate of VI cases will further increase when the next generation asteroid surveys will be operational and discover smaller asteroids.

One case has been a significant source of concern for the personnel of the monitoring systems: (99942) Apophis has been on the “risk pages” of CLOMON2 and SENTRY since December 2004, with a VI for 2029 with an estimated IP peaking at 1/37 and then declining as new and more accurate observations were received. Now the orbit is very well determined, also with radar observations: the 2029 approach will be very close (the asteroid will be visible to the human eye) but there is no possibility of impact for that year. The estimated IP for the VI resulting from the 2036 resonant return is low but it is difficult to contradict this impact possibility. This is because the current optical observations are not accurate enough to improve the orbit, and also because of the extreme sensitivity of the outcome in 2036 with respect to the exact conditions of the 2029 encounter, to the point that non-gravitational perturbations cannot be neglected. This case has for the first time raised the public issue of planning for mitigation action: knowing there is some risk does not solve the problem, if the risk is not contradicted by follow up observations. Thus a dedicated space mission, such as the one discussed in Section 14.6, might be needed.

# Part IV

# Collaborative Orbit Determination

# 13

# THE GRAVITY OF A PLANET

The equation of motion for a satellite is dominated by the gravity field of the central body, be it the Earth or another major planet. This chapter discusses the mathematical properties of the gravity field of an extended body, how to parameterize it, and how to represent it as a function of both Cartesian coordinates and orbital elements.

# 13.1 The gravity field

The equation of motion for artificial satellites has the monopole attraction of the planet as the main term; the main perturbation is the effect of the planet shape and internal mass distribution. Thus we need to discuss the gravity field of an extended body and the way to parameterize it. Expressive parameters are the coefficients of the spherical harmonic expansion, which can be included in the fit parameters for satellite gravimetry.

# Gravity of point masses

The gravity field of accelerations generated by a point mass with mass $M$ and located in $\mathbf { p } \in \mathbb { R } ^ { 3 }$ , computed at $\mathbf { x }$ , is

$$
{ \frac { d ^ { 2 } \mathbf { x } } { d t ^ { 2 } } } = \mathbf { v } ( \mathbf { x } ) = { \frac { G M } { | \mathbf { x } - \mathbf { p } | ^ { 3 } } } \left( \mathbf { p } - \mathbf { x } \right) = { \frac { G M } { r ^ { 3 } } } \left( \mathbf { p } - \mathbf { x } \right)
$$

where $r = \left| \mathbf { p } - \mathbf { x } \right|$ is the distance and $G$ is the universal gravitational constant, whose value depends only upon the system of units used; e.g., in the CGS system, $G = 6 . 6 7 2 6 \times 1 0 ^ { - 8 } \mathrm { c m ^ { 3 } / s ^ { 2 } g }$ . Note that in the orbit determination problem the constant $G$ always appears in the combination $\it G M$ and cannot be solved independently. The field $\mathbf { v } ( \mathbf { x } )$ is defined and smooth at every point $\mathbf { x } \neq \mathbf { p }$ ; it is a conservative vector field, that is rot ${ \bf v } =$

0 and it can be obtained from a gravitational potential

$$
U ( \mathbf { x } ) = G M / r , \mathbf { v } ( \mathbf { x } ) = \operatorname { g r a d } U ( \mathbf { x } )
$$

determined up to a constant, conventionally selected by imposing $\mathrm { l i m } _ { r \to + \infty }$ $U = 0$ . The vector field $\mathbf { v } ( \mathbf { x } )$ is divergence free: div $\mathbf { v } = \mathbf { \nabla } 0$ , thus by the divergence formula1 for every volume $W \subset \mathbb { R } ^ { 3 }$ , with as boundary the oriented surface $S$ , the flow of $\mathbf { v } ( \mathbf { x } )$ across $S$ (from the inside to the outside of $W$ ) can be computed as the volume integral of the divergence

$$
\int _ { S } \mathbf { v } \cdot \mathbf { n } d S = \int _ { W } \operatorname { d i v } \mathbf { v } ( \mathbf { x } ) d \mathbf { x }
$$

where $d \mathbf { x }$ is the volume element in $\mathbb { R } ^ { 3 }$ , $d S$ the element of surface on $S$ , and $\mathbf { I I }$ the unit vector normal to $S$ pointing to the exterior of $W$ . If the attracting point mass is not in $W$ the volume integral and the flow across $S$ are zero. If $\mathbf { p } \in W$ the divergence formula does not apply because of the singularity at $\mathbf x = \mathbf p$ . The flow of $\mathbf { v } ( \mathbf { x } )$ does not change under a deformation of the surface $S$ , if $\mathbf { p }$ remains inside; the flow can be computed by using the sphere $S ( r )$ of radius $r$ centered in $P$ , with normal vector $\mathbf { n } = ( \mathbf { x } - \mathbf { p } ) / r$ :

$$
\int _ { S ( r ) } - { \frac { G M } { r ^ { 3 } } } \left( \mathbf { x } - \mathbf { p } \right) \cdot \mathbf { n } d S = \int _ { S ( r ) } - { \frac { G M } { r ^ { 2 } } } d S = - 4 \pi r ^ { 2 } { \frac { G M } { r ^ { 2 } } } = - 4 \pi G
$$

A simple generalization is the $N$ -body gravity field: given a finite number of point masses $M _ { 1 } , M _ { 2 } , \ldots , M _ { n }$ located at $\mathbf { p } 1 , \mathbf { p } 2 , \ldots , \mathbf { p } _ { n }$ , by the superposition principle the gravity field and the potential are the sums

$$
\mathbf { v } ( \mathbf { x } ) = \sum _ { i = 1 } ^ { n } { \frac { G M _ { i } } { | \mathbf { x } - \mathbf { p } _ { i } | ^ { 3 } } } \left( \mathbf { p } _ { i } - \mathbf { x } \right) , U ( \mathbf { x } ) = \sum _ { i = 1 } ^ { n } { \frac { G M _ { i } } { | \mathbf { x } - \mathbf { p } _ { i } | } } .
$$

The flow across a surface $S$ is the sum of the flows, thus for every surface $S$ corresponding to the (oriented) boundary of some volume $W \subset \mathbb { R } ^ { 3 }$

$$
\int _ { S } \mathbf { v } \cdot \mathbf { n } d S = - 4 \pi G \sum _ { k } M _ { k }
$$

where the sum is extended to the point masses $\mathbf { p } _ { k } ~ \in ~ W$ , inside $S$ . To represent a solid body – a planet – as a swarm of point masses is possible, but this is neither physically intuitive nor computationally efficient.

# Mass and gravity of an extended body

To describe the gravity field of an extended body it is better to abandon the unphysical mathematical model of point masses and to use a continuous mass distribution, defined by a mass density function $\rho ( \mathbf { p } ) \geq 0$ which is positive only on a limited subset $W \subset \mathbb { R } ^ { 3 }$ , the support of the mass distribution. Then the total mass is given by the volume integral

$$
M = \int _ { W } \rho ( { \bf p } ) d { \bf p } ,
$$

well defined under some regularity conditions; e.g., the total mass is well defined if $S$ is a smooth surface and $\rho$ is continuous.2 The gravity field generated by the mass density $\rho$ is

$$
\mathbf { v } ( \mathbf { x } ) = \int _ { W } { \frac { G \rho ( \mathbf { p } ) } { | \mathbf { x } - \mathbf { p } | ^ { 3 } } } ( \mathbf { p } - \mathbf { x } ) \ d \mathbf { p }
$$

where the integral is over the points $\mathbf { p } \in W$ , with $\mathbf { x }$ fixed.

The extended body may well move, thus the mass density may also be time dependent, satisfying a mass conservation equation. If we use the Newtonian approximation, by which the gravity field acts instantaneously (with infinite propagation speed), the gravity field can be computed at each instant of time for every point $\mathbf { x } \in \mathbb { R } ^ { 3 }$ with the same formula.

Also the gravitational potential of an extended body can be defined by a volume integral:

$$
U ( \mathbf { x } ) = \int _ { W } { \frac { G \rho ( \mathbf { p } ) } { | \mathbf { x } - \mathbf { p } | } } d \mathbf { p } .
$$

By exchanging the operations of integral over $\mathbf { p }$ and differentiation with respect to the components of $\mathbf { x }$ , we can obtain eq. (13.2) by applying the gradient operator to the integral above.3

The conventional definition of the (Riemann) integral used in eq. (13.1) is obtained by partitioning the support $W$ by parallelograms $W _ { k }$ defined by intervals for each of the coordinates of $\mathbf { p }$ . The contribution for each $k$ to the sums approximating the integral is just the volume of $W _ { k }$ times the value of $\rho$ in some point $\mathbf { p } \in W _ { k }$ . This corresponds to the intuitive idea that the total mass of the extended body can be obtained by cutting it into small bricks and by estimating the density of each brick, e.g., by weighing it. However, this is certainly not an operational definition of the mass of a planet.

To obtain a more practical definition, we can use the divergence formula. By exchanging derivatives and integrals, also for an extended body div $\mathbf { v } ( \mathbf { x } ) = 0$ for all $\mathbf { x }$ outside $W$ , where there is no mass. Inside the body div $\mathbf { v } ( \mathbf { x } ) = - 4 \pi G \rho ( \mathbf { x } )$ ; the proof requires some non-trivial steps.

Let $S$ be an oriented surface, containing the planet, that is the set $W$ where $\rho ( \mathbf { p } ) > 0$ , inside. Then the mass of the planet can be measured by the flow of its gravity field across $S$

$$
M = \int _ { W } \rho ( \mathbf { x } ) d \mathbf { x } = - { \frac { 1 } { 4 \pi G } } \int _ { W } \operatorname { d i v } \mathbf { v } ( \mathbf { x } ) d \mathbf { x } = - { \frac { 1 } { 4 \pi G } } \int _ { S } \mathbf { v } \cdot \mathbf { n } d S .
$$

This formula suggests that the mass of the planet can be determined by scanning some closed surface, either at the physical surface of the planet or above it, with a gravimeter measuring the gravity field vector.

As an historical example, let us approximate a planet like our Earth by a sphere of radius $R _ { \oplus }$ , with the gravity field at the surface everywhere normal to the sphere and of constant size $| \mathbf { v } | = g$ ; we are also neglecting the apparent forces due to the rotation of the planet. In this approximation the mass

$$
M = - \frac { 1 } { 4 \pi G } \int \int _ { S } - g d S = \frac { 1 } { 4 \pi G } g 4 \pi R _ { \oplus } ^ { 2 } = \frac { g R _ { \oplus } ^ { 2 } } { G }
$$

can be estimated if $g$ and $G$ are known.4

# Harmonic functions

By combining the equations $\mathbf { v } ( \mathbf { x } ) = \mathrm { g r a d } \ U ( \mathbf { x } )$ and div $\mathbf { v } ( \mathbf { x } ) = - 4 \pi G \rho ( \mathbf { x } )$ we obtain the Poisson equation

$$
\operatorname { d i v } \left( \operatorname { g r a d } U ( \mathbf { x } ) \right) = - 4 \pi G \rho ( \mathbf { x } )
$$

for the points $\mathbf { x } \in W$ where there is source mass density, and the Laplace equation

$$
\mathrm { d i v } \left( \mathrm { g r a d } U ( \mathbf { x } ) \right) = 0
$$

for $\mathbf { x }$ outside $W$ , in empty space. The combined operator $\Delta U = \operatorname { d i v } \left( \operatorname { g r a d } U \right)$ can be expressed by means of the second partial derivatives of the potential

$$
\Delta { \mathrm { ~ } } U = \operatorname { d i v } { \mathrm { ~ ( g r a d ~ } } U { \mathrm { ) } } = { \frac { \partial ^ { 2 } U } { \partial { x _ { 1 } } ^ { 2 } } } + { \frac { \partial ^ { 2 } U } { \partial { x _ { 2 } } ^ { 2 } } } + { \frac { \partial ^ { 2 } U } { \partial { x _ { 3 } } ^ { 2 } } } .
$$

A function $U ( \mathbf { x } )$ fulfilling the Laplace equation $\Delta \ U = 0$ is a harmonic function: the gravitational potential generated by an extended body with support $W$ is harmonic in $\mathbb { R } ^ { 3 } \setminus W$ .

Harmonic functions have many important properties, including the following: they can have neither local maxima nor local minima (Evans 1998, Section 2.2). A function with continuous second derivatives and harmonic is smooth, that is it has continuous derivatives of whatever order. It is also analytic, that is with convergent Taylor series in a neighborhood of every point. This has an important implication in orbit determination, actually in all problems of celestial mechanics: the equation of motion and the corresponding general solution are always smooth, even analytic, for each body moving in empty space under the gravitational attraction of the other bodies. Only for non-gravitational perturbations might regularity problems occur (see Section 14.3).

# Spherical symmetry

The simplest case in which the solutions of the Laplace equation can be explicitly computed is when the gravitational potential has spherical symmetry around the origin in the $\mathbf { x }$ space, that is $U ( \mathbf { x } ) = R ( r )$ (where $r = | \mathbf { x } |$ and $R$ is a smooth function). Then the Laplace operator $\Delta$ can be easily computed from the partials

$$
\begin{array} { r c l } { { \displaystyle { \frac { \partial U } { \partial { x _ { j } } } } } } & { { = } } & { { \displaystyle { \frac { d R } { d r } \frac { \partial r } { \partial { x _ { j } } } = \frac { x _ { j } } { r } \frac { d R } { d r } } , } } \\ { { \displaystyle { \frac { \partial ^ { 2 } U } { \partial { x _ { j } } ^ { 2 } } } } } & { { = } } &  { \displaystyle { \frac { 1 } { r } \ \frac { d R } { d r } + \frac { x _ { j } ^ { 2 } } { r } \left( \frac { 1 } { r } \ { \frac { d ^ { 2 } R } { d r ^ { 2 } } } - \frac { 1 } { r ^ { 2 } } \ { \frac { d R } { d r } } \right) } } \end{array}
$$

and, by summing over $j = 1 , 3$ ,

$$
0 = \Delta U = 2 { \frac { 1 } { r } } { \frac { d R } { d r } } + { \frac { d ^ { 2 } R } { d r ^ { 2 } } } = { \frac { 1 } { r ^ { 2 } } } { \frac { d } { d r } } \left[ r ^ { 2 } { \frac { d R } { d r } } \right] ;
$$

we conclude that $r ^ { 2 } d R / d r = - k$ , with $k$ an arbitrary constant. This gives all the possible spherically symmetric harmonic functions as $\begin{array} { r } { R ( r ) = \frac { k } { r } + c o n s t } \end{array}$ . By selecting the additive constant to be $0$ , we find that the solution coincides with the gravitational potential of a point mass in $\mathbf { p } = \mathbf { 0 }$ with mass $M =$ $k / G$ .

This result has a very deep implication for all methods of gravimetry, including satellite geodesy. Let the mass density function be spherically symmetric, that is $\rho ( \mathbf { p } ) = \tilde { \rho } ( | \mathbf { p } | )$ for some function $\tilde { \rho }$ . The support $W$ has necessarily spherical symmetry, and we say that the planet is spherically symmetric. Then the gravitational potential $U$ is a spherically symmetric harmonic function in $\mathbb { R } ^ { 3 } \setminus W$ and there is a positive constant $M$ such that $U = G M / r$ outside $W$ . By the divergence formula it can be shown that

$M$ is indeed the mass as defined by eq. (13.1). Thus the gravity field of two spherically symmetric planets with equal mass are exactly the same, outside the support of both mass distributions; they are both the same as the potential of a point mass with the same $M$ .

This implies that there is no way to determine the internal mass distribution of a planet, that is the mass density $\rho ( \mathbf { p } )$ , by measuring the gravitational field either on or outside its surface. This limitation applies also to the methods of measurement using whatever consequence of the gravity field, including the orbits of satellites. Satellite gravimetry cannot solve for parameters describing the mass density function, unless such parameters are chosen in such a way that the “concentration” of the mass near the center depends upon the parameters to be measured by other means, e.g., by measuring the rotational properties of the planet (see Chapter 17).

# 13.2 Spherical harmonics

The example of spherically symmetric harmonic functions shows the advantage of using a system of coordinates adapted to the problem. To generalize this we use a coordinate system adapted to bodies with an approximate spherical shape, the spherical polar coordinates defined by

$$
x _ { 1 } = r \cos \theta \cos \lambda , \qquad x _ { 2 } = r \cos \theta \sin \lambda , \qquad x _ { 3 } = r \sin \theta ,
$$

that is, $r \ > \ 0$ is the distance from the selected center, $\theta$ the latitude $( - \pi / 2 \leq \theta \leq \pi / 2$ ), and $\lambda$ the longitude, an angle variable. On the Earth a reference system with the $x _ { 3 }$ axis along the rotation axis and the $( x _ { 1 } , x _ { 2 } )$ plane containing the equator is normally used.5 Thus the gravitational potential can be expressed in polar coordinates: $U ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) = \Phi ( r , \theta , \lambda )$ .

To compute the Laplace operator in spherical polar coordinates we use the chain rule

$$
\frac { \partial U } { \partial x _ { j } } = \frac { \partial \Phi } { \partial r } \frac { \partial r } { \partial x _ { j } } + \frac { \partial \Phi } { \partial \theta } \frac { \partial \theta } { \partial x _ { j } } + \frac { \partial \Phi } { \partial \lambda } \frac { \partial \lambda } { \partial x _ { j } } ,
$$

and the derivatives of the inverse coordinate change (13.4)

$$
{ \frac { \partial U } { \partial x _ { 1 } } } = { \frac { \partial \Phi } { \partial r } } \cos \theta \cos \lambda - { \frac { \partial \Phi } { \partial \theta } } { \frac { 1 } { r } } \sin \theta \cos \lambda - { \frac { \partial \Phi } { \partial \lambda } } { \frac { \sin \lambda } { r \cos \theta } } .
$$

The second partial derivatives can be obtained by iterating the same procedure on the first derivatives and by summing we obtain an expression for

$\Delta U$ containing only partial derivatives with respect to $r , \theta , \lambda$ :

$$
r ^ { 2 } \Delta U = \frac { \partial } { \partial r } \left( r ^ { 2 } \frac { \partial \Phi } { \partial r } \right) + \Delta _ { S } U ,
$$

where

$$
\Delta _ { S } U = \frac { 1 } { \cos \theta } \frac { \partial } { \partial \theta } \left( \cos \theta \frac { \partial \Phi } { \partial \theta } \right) + \frac { 1 } { \cos ^ { 2 } \theta } \frac { \partial ^ { 2 } \Phi } { \partial \lambda ^ { 2 } }
$$

is called the Laplace–Beltrami operator; it is independent of $r$ and can be applied to functions defined over a sphere $S ( r )$ with fixed $r$ , that is functions of $( \theta , \lambda )$ only.

# Zonal spherical harmonics

We will first search for solutions of the Laplace equation $\Delta U \ = \ 0$ with axial symmetry, that is $U ( x , y , z ) = \Phi ( r , \theta )$ (independent of $\lambda$ ). Then the Laplace operator in polar coordinates of (13.5) has the simpler expression

$$
\Delta U = { \frac { 1 } { r ^ { 2 } } } { \frac { \partial } { \partial r } } [ r ^ { 2 }  { \frac { \partial \Phi } { \partial r } } ] + { \frac { 1 } { r ^ { 2 } \cos \theta } } { \frac { \partial } { \partial \theta } } [ \cos \theta  { \frac { \partial \Phi } { \partial \theta } } ] = 0 .
$$

We proceed to solve the partial differential equation above by separation of variables, that is by looking for special solutions as the product of a function of $r$ and a function of $\theta$ : $U = \Phi ( r , \theta ) = R ( r ) F ( \theta )$ . Then

$$
\Delta U = { \frac { R F } { r ^ { 2 } } } \left\{ { \frac { 1 } { R } } { \frac { d } { d r } } \left[ r ^ { 2 } { \frac { d R } { d r } } \right] + { \frac { 1 } { F \cos \theta } } { \frac { d } { d \theta } } \left[ \cos \theta { \frac { d F } { d \theta } } \right] \right\} = 0 .
$$

The expression inside the bracket is the sum of a function of $r$ and a function of $\theta$ . If the above equation is satisfied on an open set in the $( r , \theta )$ space, these functions are both constant. Let this constant be $\ell \left( \ell + 1 \right)$ ; then

$$
{ \frac { d } { d r } } \left[ r ^ { 2 } { \frac { d R } { d r } } \right] = \ell ( \ell + 1 ) R , \quad { \frac { d } { d \theta } } \left[ \cos \theta { \frac { d F } { d \theta } } \right] = - \ell ( \ell + 1 ) F \cos \theta
$$

are two ordinary differential equations to be satisfied by the functions $R ( r )$ and $F ( \theta )$ . The first one has solutions of the form $R ( r ) = r ^ { \gamma } , \gamma \in \mathbb { R }$ ,

$$
{ \frac { d } { d r } } \left[ r ^ { 2 } \gamma r ^ { \gamma - 1 } \right] = \ell ( \ell + 1 ) r ^ { \gamma } \Longleftrightarrow \gamma ( \gamma + 1 ) r ^ { \gamma } = \ell ( \ell + 1 ) r ^ { \gamma }
$$

with two possible solutions for $\gamma$ : either $\gamma = \ell$ or $\gamma = - \ell - 1$ . By the standard existence and uniqueness theorem, the second-order ordinary differential equation for $R ( r )$ has solutions depending upon two arbitrary constants $A , B$ :

$$
R ( r ) = A r ^ { \ell } + \frac { B } { r ^ { \ell + 1 } } .
$$

To solve the equation for $F ( \theta )$ we change variable: $\mu = \sin \theta$ , $F ( \theta ) = f ( \mu )$

$$
\frac { 1 } { \cos \theta } { \frac { d } { d \theta } } \left[ \cos \theta { \frac { d F } { d \theta } } \right] = { \frac { d } { d \mu } } \left[ \cos ^ { 2 } \theta { \frac { d f } { d \mu } } \right] = { \frac { d } { d \mu } } \left[ \left( 1 - \mu ^ { 2 } \right) { \frac { d f } { d \mu } } \right] .
$$

Thus the function $f ( \mu )$ is a solution of a second-order linear equation, the Legendre equation:

$$
\left( 1 - \mu ^ { 2 } \right) \frac { d ^ { 2 } f } { d \mu ^ { 2 } } - 2 \mu \frac { d f } { d \mu } + \ell ( \ell + 1 ) f = 0 .
$$

The solutions of the Legendre equation are found by the method of undetermined coefficients, that is by representing $f ( \mu )$ as a power series

$$
f ( \mu ) = \sum _ { k = 0 } ^ { + \infty } a _ { k } \mu ^ { k } ,
$$

by substituting the series into (13.7) and by grouping terms according to their degree in $\mu$ :

$$
\begin{array} { r c l } { { \mathrm { } \mathrm { ~  ~ \Lambda ~ } ^ { \mathrm { ~ \tiny ~ + ~ \infty ~ } } } } & { { = } } &  { \displaystyle { \left( 1 - \mu ^ { 2 } \right) \sum _ { k = 2 } ^ { + \infty } a _ { k } \ : k ( k - 1 ) \ : \mu ^ { k - 2 } - 2 \mu \sum _ { k = 1 } ^ { + \infty } a _ { k } \ : k \ : \mu ^ { k - 1 } + \ell ( \ell + 1 ) \sum _ { k = 0 } ^ { + \infty } a _ { k } } } \\ { { \mathrm { } } } & { { = } } &  { \displaystyle { \sum _ { k = 0 } ^ { + \infty } \mu ^ { k } \left[ a _ { k + 2 } \left( k + 2 \right) \left( k + 1 \right) - a _ { k } \ : k ( k - 1 ) - 2 k a _ { k } + \ell ( \ell + 1 ) a _ { k } \right] } } \end{array}
$$

The Legendre equation needs to be satisfied identically, for whatever $\theta$ in $- \pi / 2 \le \theta \le \pi / 2$ , that is for $- 1 \leq \mu \leq 1$ , thus the coefficients of the power series above need to be all zero:

$$
a _ { k + 2 } \left( k + 2 \right) \left( k + 1 \right) - a _ { k } \left[ k ( k - 1 ) + 2 k - \ell ( \ell + 1 ) \right] = 0
$$

for every non-negative integer $k$ . This is a second-order recursion formula, allowing us to solve for the unknown $a _ { k + 2 }$ provided $a _ { k }$ is known

$$
a _ { k + 2 } = { \frac { k ( k + 1 ) - \ell ( \ell + 1 ) } { ( k + 2 ) ( k + 1 ) } } a _ { k } .
$$

This recursion formula gives zero for $k = \ell$ : this implies that we can find a solution with $f ( \mu )$ polynomial in $\mu = \sin \theta$ provided $\ell$ is a non-negative integer.6 If $\ell$ is even we set the initial conditions $a _ { 0 } \neq 0$ and $a _ { 1 } = 0$ , and we obtain $f ( \mu )$ , a polynomial with only even degree monomials. If $\ell$ is odd we use $a _ { 0 } = 0$ and $a _ { 1 } \neq 0$ , we obtain for $f ( \mu )$ an odd polynomial. For example,

$$
\ell = 0 \Longrightarrow f ( \mu ) = a _ { 0 }
$$