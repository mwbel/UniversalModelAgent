Selecting a value of the cycle slip number $k$ in this range implies selecting the coordinates $\mathbf { h } _ { 0 }$ for the preliminary orbit at epoch $t _ { 0 }$

$$
\begin{array} { l l l } { { n _ { k } } } & { { = } } & { { \displaystyle \frac { 2 \pi k + \Delta \lambda } { \Delta t } } } \\ { { \lambda _ { 0 k } } } & { { \equiv } } & { { n _ { k } ( t _ { 0 } - t _ { 1 } ) + \lambda _ { 1 } \ ( \mathrm { m o d } \ 2 \pi ) \equiv n _ { k } ( t _ { 0 } - t _ { 2 } ) + \lambda _ { 2 } \ ( \mathrm { m o d } \ 2 \pi ) . } } \end{array}
$$

This algorithm can be illustrated with our model problem, containing only the variables $\mathbf { h }$ . Figure 7.5 shows a case with five intersections of the confidence ellipses. By testing five different first guess orbits, corresponding to $k = 4 , 5 , 6 , 7 , 8$ , the differential corrections converge to five different solutions. The true solution corresponds to $k = 5$ and has a normalized residuals $\mathrm { R M S } \simeq 1 . 0 1 $ . Note that the linear algorithm, without cycle slip, would provide a $\mathbf { h } _ { 0 }$ close to the intersection with $n \simeq 1 . 2 1$ , corresponding to $k = 6$ ; from this, the differential corrections converge to a spurious solution with normalized $\mathrm { R M S } \simeq 0 . 9 1$ . This example shows that to choose among alternative solutions for the identification orbit is far from easy, especially when the data are of poor quality, as in this example.

# Constrained orbit identification

If the portion $\mathbf { h } _ { 0 }$ of the identification orbit has been selected already, then the other part $\mathbf { g } _ { 0 }$ should be selected in a consistent way. In the two-body approximation, the value of $\mathbf { g }$ is independent of time, thus $\mathbf { g } _ { i }$ are the predictions for epoch $t _ { 0 }$ from $t _ { i }$ , for $i = 1 , 2$ . The uncertainty of these predictions can be computed, given the fixed value of $\mathbf { h } = \mathbf { h } _ { 0 }$ , by the formula for the conditional case of Section 5.4: the nominal conditional value is

$$
{ \bf g } _ { 0 i } = { \bf g } _ { i } - C _ { \bf g g } ^ { - 1 } ( { \bf x } _ { i } ) C _ { \bf g h } ( { \bf x } _ { i } ) ( { \bf h } _ { 0 } - { \bf h } _ { i } ) \mathrm { f o r } i = 1 , 2
$$

and the normal matrices are the same $C _ { \mathbf { g g } } ( \mathbf { x } _ { i } )$ . The conditional identification penalty $K _ { C }$ contains three terms: one from forcing ${ \bf h } _ { 1 } ( t _ { 0 } )$ to $\mathbf { h } _ { 0 }$ , one from forcing ${ \bf h } _ { 2 } ( t _ { 0 } )$ to $\mathbf { h } _ { 0 }$ , the third by the compromise between ${ \bf g } _ { 0 1 }$ and ${ \bf g } _ { 0 2 }$ :

$$
\begin{array} { r c l } { K _ { C } } & { = } & { K _ { \mathbf { h } } ^ { 1 } + K _ { \mathbf { h } } ^ { 2 } + K _ { \mathbf { g } } } \\ { K _ { \mathbf { h } } ^ { 1 } } & { = } & { \left( \mathbf { h } _ { 0 } - \mathbf { h } _ { 1 } ( t _ { 0 } ) \right) \cdot C ^ { \mathbf { h h } } ( \mathbf { x } _ { 1 } ) \left( \mathbf { h } _ { 0 } - \mathbf { h } _ { 1 } ( t _ { 0 } ) \right) } \\ { K _ { \mathbf { h } } ^ { 2 } } & { = } & { \left( \mathbf { h } _ { 0 } - \mathbf { h } _ { 2 } ( t _ { 0 } ) \right) \cdot C ^ { \mathbf { h h } } ( \mathbf { x } _ { 2 } ) \left( \mathbf { h } _ { 0 } - \mathbf { h } _ { 2 } ( t _ { 0 } ) \right) } \\ { K _ { \mathbf { g } } } & { = } & { \left( \mathbf { g } _ { 0 2 } - \mathbf { g } _ { 0 1 } \right) \cdot C ^ { \mathbf { g } } \left( \mathbf { g } _ { 0 2 } - \mathbf { g } _ { 0 1 } \right) } \\ { C ^ { \mathbf { g } } } & { = } & { C _ { \mathbf { g g } } ( \mathbf { x } _ { 1 } ) - C _ { \mathbf { g g } } ( \mathbf { x } _ { 1 } ) \ \left[ C _ { \mathbf { g g } } ( \mathbf { x } _ { 1 } ) + C _ { \mathbf { g g } } ( \mathbf { x } _ { 2 } ) \right] ^ { - 1 } \ C _ { \mathbf { g g } } ( \mathbf { x } _ { 1 } ) } \end{array}
$$

and the point of minimum penalty is at

$$
{ \bf g } _ { 0 } = [ C _ { { \bf g } { \bf g } } ( { \bf x } _ { 1 } ) + C _ { { \bf g } { \bf g } } ( { \bf x } _ { 2 } ) ] ^ { - 1 } \left( C _ { { \bf g } { \bf g } } ( { \bf x } _ { 1 } ) { \bf g } _ { 0 1 } + C _ { { \bf g } { \bf g } } ( { \bf x } _ { 2 } ) { \bf g } _ { 0 2 } \right) .
$$

# 7.5 Recovery and precovery

The problem is how to describe the uncertainty of the position of the asteroid on the celestial sphere, taking into account the nonlinearity of the relationship between orbital elements at some epoch and the observations to be predicted at some other time.

# The confidence ellipse

Let a least squares orbit be available with initial conditions $\mathbf { x }$ at some epoch $t _ { 0 }$ , with normal and covariance matrices $C , \Gamma$ . At some later time $t _ { 1 }$ an observation is either performed or planned. An astrometric observation is a map $G$ from the elements space to the celestial sphere, parameterized by two coordinates (usually right ascension and declination) $\mathbf { y } = \left( \alpha , \delta \right)$ :

$$
\mathbf { y } ( t _ { 1 } ) = G ( \mathbf { x } ( t _ { 1 } ) ) , \quad G : W \longrightarrow \mathbb { R } ^ { 2 } , \quad W \subset \mathbb { R } ^ { 6 }
$$

with $W$ an open set.3 ${ \bf x } ( t _ { 1 } )$ is the state vector at time $t _ { 1 }$ , a function of the initial conditions $\mathbf { x } = \mathbf { x } ( t _ { 0 } )$ through the integral flow $\mathbf { x } ( t _ { 1 } ) = \Phi _ { t _ { 0 } } ^ { t _ { 1 } } ( \mathbf { x } ( t _ { 0 } ) )$ . The composition of the observation function with the integral flow

$$
\mathbf { y } = F ( \mathbf { x } ) = G \left( \Phi _ { t _ { 0 } } ^ { t _ { 1 } } ( \mathbf { x } ) \right) , \quad F : W \longrightarrow \mathbb { R } ^ { 2 }
$$

is the astrometric prediction function; its Jacobian matrix can be computed by means of the state transition matrix $D \Phi _ { t _ { 0 } } ^ { t _ { 1 } }$ , by $D F = D G D \Phi _ { t _ { 0 } } ^ { t _ { 1 } }$ .

The astrometric prediction function $F ^ { \prime }$ maps the orbital elements space onto the observation space, and the confidence region $\Delta Q \ \le \ \sigma ^ { 2 }$ into a confidence prediction region in the observation space. The linearized function $D F$ maps the displacement (from the least squares solution $\mathbf { x } ^ { * }$ ) in the orbital elements space $\Delta \mathbf { x } = \mathbf { x } - \mathbf { x } ^ { * }$ , into linearized deviations from the prediction $\mathbf { y } ^ { * } = F ( \mathbf { x } ^ { * } )$ :

$$
\Delta \mathbf { y } = \mathbf { y } - \mathbf { y } ^ { * } = D F ( \mathbf { x } ^ { * } ) \Delta \mathbf { x }
$$

and therefore maps the confidence ellipsoid $\Delta \mathbf { x } \cdot C \Delta \mathbf { x } \leq \sigma ^ { 2 }$ onto a confidence ellipse in the observation coordinate plane: $\Delta \mathbf { y } \cdot C _ { \mathbf { y } } \ \Delta \mathbf { y } \leq \sigma ^ { 2 }$ . The matrix $C _ { \mathbf { y } }$ is the normal matrix for the observations $\mathbf { y }$ (at a given time $t _ { 1 }$ ), and the inverse $\Gamma _ { \mathbf { y } } = C _ { \mathbf { y } } ^ { - 1 }$ is the corresponding covariance matrix. In the probabilistic interpretation, by using standard result from the theory of multivariate Gaussian distribution (see Section 3.3), the covariance matrix is transformed by $\Gamma _ { \mathbf { y } } = D F \Gamma D F ^ { \prime }$ , then the normal matrix is computed as $C _ { \mathbf { y } } = \Gamma _ { \mathbf { y } } ^ { - 1 }$ .

To obtain the same result within the optimization interpretation, and also to gain some geometrical insight, let us consider in the $\mathbf { x }$ space the rows of $D F$ , that is the gradients of the observable angles. If the two angular variables observed are independent4 the subspace spanned by the rows of $D F$ has dimension 2. Thus $\mathbf { x } \in \mathbb { R } ^ { 6 }$ can be decomposed into a component $\mathbf { g }$ in this subspace, and a component $\mathbf { h }$ in the four-dimensional orthogonal subspace. That is, there is a rotation matrix $R$ in $\mathbb { R } ^ { 6 }$ such that

$$
R \mathbf { x } = \left[ \begin{array} { c } { \mathbf { g } } \\ { \mathbf { h } } \end{array} \right] , \quad \mathbf { g } \in \mathbb { R } ^ { 2 } , \ \mathbf { h } \in \mathbb { R } ^ { 4 }
$$

and then the map $D F$ is an isomorphism between $\mathbf { g }$ and y:

$$
D F = A \circ \Pi _ { \mathbf { g } } \circ R
$$

where $\Pi _ { \mathbf { g } }$ is the $2 \times 6$ matrix of the projection on the two-dimensional subspace and $A$ is an invertible $2 \times 2$ matrix. The normal and covariance matrix can be transformed into the new coordinate system by $R , R ^ { I }$ ; then we can use the formulae of Section 5.4 and compute the marginal covariance for g:

$$
\Gamma _ { \mathbf { g } \mathbf { g } } ^ { - 1 } = C ^ { \mathbf { g } \mathbf { g } } = C _ { \mathbf { g } \mathbf { g } } - C _ { \mathbf { g } \mathbf { h } } ~ C _ { \mathbf { h } \mathbf { h } } ^ { - 1 } ~ C _ { \mathbf { h } \mathbf { g } } .
$$

Since $A$ is invertible, the same formulae for covariance propagation of Section 5.5 apply, that is

$$
\begin{array} { r } { C _ { \mathbf { y } } = \left( A ^ { - 1 } \right) ^ { T } \ C _ { \mathbf { g g } } \ A ^ { - 1 } , \quad \Gamma _ { \mathbf { y } } = A \ \Gamma _ { \mathbf { g g } } \ A ^ { T } } \end{array}
$$

and by combining all the transformations of the covariance with eq. (7.5)

$$
\Gamma _ { \mathbf { y } } = A \ \Pi _ { \mathbf { g } } \ R \Gamma \ R ^ { T } \ \Pi _ { \mathbf { g } } ^ { T } \ A ^ { T } = D F \Gamma \ D F ^ { T } ,
$$

that is, the same formula of the probabilistic interpretation.

This linear prediction formalism is used as a matter of routine in the collaborative case, and it has been proposed to use it systematically for asteroid astrometry. However, the astrometric prediction function $F$ is nonlinear, and there is no guarantee that the confidence ellipse is a good approximation of the confidence prediction region: this is indeed not the case when a poorly determined orbit is used to predict the observations at a time $t _ { 1 }$ very far from the last observation used in the orbit determination.

# Semilinear predictions

We would like to have an algorithm to compute an approximation of the fully nonlinear confidence prediction region which is a better approximation than the linear one, and nevertheless can be computed explicitly. The astrometric prediction function contains the integral flow, thus in realistic cases to compute it accurately we can only numerically propagate a finite number of orbits from time $t _ { 0 }$ to time $t _ { 1 }$ .

The geometric idea of the semilinear confidence boundary comes from the regression subspace of $\mathbf { h }$ given $\mathbf { g }$ , that is the dimension 2 linear subspace

$$
\mathbf { h } - \mathbf { h } ^ { * } = - C _ { \mathbf { h } \mathbf { h } } ^ { - 1 } C _ { \mathbf { h } \mathbf { g } } \left( \mathbf { g } - \mathbf { g } ^ { * } \right)
$$

where $\mathbf { h } ^ { * } , \mathbf { g } ^ { * }$ are the nominal values

$$
\left[ \begin{array} { l } { \mathbf { g } ^ { * } } \\ { \mathbf { h } ^ { * } } \end{array} \right] = R \mathbf { x } ^ { * } , \quad \mathbf { g } ^ { * } \in \mathbb { R } ^ { 2 } , \ \mathbf { h } ^ { * } \in \mathbb { R } ^ { 4 } .
$$

![](images/16fc058b55bb0e65dfa407d83522cd9dc6a292ba1c422bf125cf73809e813006.jpg)  
Fig. 7.6. Simulated recovery of the asteroid 4161 PLS, lost in September 1960, at the epoch of the discovery of the asteroid $1 9 9 2 ~ \mathrm { B U }$ , that is 31 year later. The recovery observation (cross) is well inside the semilinear confidence boundary corresponding to the $\sigma = 3$ level. Reprinted from (Milani 1999) with permission from Elsevier.

The values of $\mathbf { h }$ from the above formula have the property that, for a given $\mathbf { g }$ , thus for a given linearized prediction $\Delta \mathbf { y } = D F \Delta \mathbf { x }$ , the quadratic penalty $\Delta _ { \mathbf { h } } Q = \Delta \mathbf { x } ^ { T } ~ C ~ \Delta _ { \mathbf { x } } / m$ is minimum. In particular, the intersection of the regression subspace of $\mathbf { h }$ given $\mathbf { g }$ with the outer surface of the confidence ellipsoid $\Delta \mathbf { x } ^ { T } \ C \ \Delta \mathbf { x } = { \boldsymbol \sigma } ^ { 2 }$ is an ellipse $\gamma$ in the $\mathbf { x }$ space, which projects (by $\Pi _ { \mathbf { g } } \circ R$ ) onto the marginal confidence ellipse in the $\mathbf { g }$ space, thus also (by $D F$ ) onto the confidence ellipse in the y space.

We define the semilinear confidence boundary as the image, by the nonlinear astrometric prediction function $F$ , of the ellipse $\gamma$ defined above into the y space of astrometric observations. In practical cases, the semilinear boundary is very different from the linear ellipse when the size of both figures is large, e.g., several degrees. This happens when the orbit has been determined by using only a short observed arc and/or when the prediction is for a time remote from the observations. Figure 7.6 shows a rather extreme case of an asteroid lost after being observed only during a survey in 1960 and recovered 31 years later. In such a case the mean longitude at the prediction time has an enormous uncertainty, thus the semilinear boundary follows the curvature of the image of a long segment of the $\lambda$ coordinate axis in the space of equinoctial elements.

# 7.6 Attribution

In the attribution case the problem is how to define the observation space in which the comparison between prediction and available data has to be performed. We assume an orbit $\mathbf { x } _ { 1 }$ has been fit to the first set of $m _ { 1 }$ observations, with epoch time $t _ { 1 }$ , and the uncertainty is described by the covariance and normal matrices $\Gamma _ { 1 } , C _ { 1 }$ . The second arc includes $m _ { 2 }$ scalar observations.

It is possible to compute a prediction for each of the $m _ { 2 }$ observations, with its uncertainty, and to apply a test on the size of each of the normalized residuals, but this is inefficient for two reasons. First, the predictions for observations close in time are correlated, thus the marginal uncertainty of each one gives a less stringent control than performing a single test for all, with a full normal matrix for the vector prediction in $\mathbb { R } ^ { 2 m _ { 2 } }$ . Second, to compute an accurate prediction for a sequence of times requires us to propagate the orbit to each one of the (distinct) times $t _ { i }$ of the second arc. The number $m _ { 2 }$ can be comparatively large, and still we can have a too short arc to fit an orbit, when many observations are taken over a short time span.

Thus it is useful to synthesize the information contained in the second arc into a vector observation at a single time $t _ { 2 }$ : this is the attributable.

# Attributables

Let $( \rho , \alpha , \delta ) \in \mathbb { R } ^ { + } \times [ - \pi , \pi ) \times ( - \pi / 2 , \pi / 2 )$ be spherical coordinates for the topocentric position of a celestial body. The angular coordinates $( \alpha , \delta )$ are defined by a topocentric reference system that can be arbitrarily selected.

Usually, in the applications, $\alpha$ is the right ascension and $\delta$ the declination with respect to an equatorial reference system (e.g., J2000).

We shall call attributable a vector

$$
A = ( \alpha , \delta , \dot { \alpha } , \dot { \delta } ) \in [ - \pi , \pi ) \times ( - \pi / 2 , \pi / 2 ) \times \mathbb { R } ^ { 2 } ,
$$

representing the angular position and velocity of the body at a time $t$ in the selected reference frame. A natural operation is trying to attribute the data used for $A$ to an already existing orbit, hence the name.

A detection of a moving object today is done by comparing two or more images of the same field, taken at short intervals of time. Thus an attributable can be computed from a short arc of astrometric observations of a celestial body. Given the observed values $( t _ { i } , \alpha _ { i } , \delta _ { i } )$ for $i = 1 , m$ with $m \geq 2$ , we can compute an attributable with its uncertainty. We can fit both angular coordinates with linear functions of time, that is with the same fit of the model problem of Section 5.1. More precisely, let $t$ be the mean of the $t _ { i }$ and let the fit solution at time $t$ be $( \alpha , \dot { \alpha } , \delta , \dot { \delta } )$ ; this solution is obtained with the regression line formulae, together with the two $2 \times 2$ normal matrices $C _ { ( \alpha , \dot { \alpha } ) } , C _ { ( \delta , \dot { \delta } ) }$ and covariance matrices $\Gamma _ { ( \alpha , \dot { \alpha } ) } , \Gamma _ { ( \delta , \dot { \delta } ) } .$ The normal matrix $C _ { A }$ of $A$ is composed just by joining the two normal matrices, and is not singular provided the observations refer to $\geq 2$ distinct times; its inverse $\Gamma _ { A }$ is also composed by joining the two $2 \times 2$ covariance matrices.

On the other hand, if there are $m \geq 3$ observations and the time span is not too short, a more accurate estimate of the attributable $A$ is obtained by fitting both angular coordinates as a function of time with a quadratic model. Then the solution $( \alpha , \dot { \alpha } , \ddot { \alpha } , \delta , \dot { \delta } , \ddot { \delta } )$ is obtained with the standard formulae of the least squares problem, together with the two $3 \times 3$ covariance matrices $\Gamma _ { ( \alpha , \dot { \alpha } , \ddot { \alpha } ) } , \Gamma _ { ( \delta , \dot { \delta } , \ddot { \delta } ) }$ . The marginal covariance matrix $\Gamma _ { A }$ of $A$ , whatever the values of $( \ddot { \alpha } , \ddot { \delta } )$ , is obtained by extracting the relevant $4 \times 4$ submatrix, and the normal matrix is computed by $C _ { A } = \Gamma _ { A } ^ { - 1 }$ .

Note that the observations can be weighted. If there are only two observations with equal weight $1 / \sigma ^ { 2 }$ and difference in times $2 \Delta t$ , then the correlations $\mathrm { C o r r } ( \alpha , \dot { \alpha } ) , \mathrm { C o r r } ( \delta , \dot { \delta } )$ are zero and $C _ { A } , \Gamma _ { A }$ are diagonal:5 the standard deviation of both angles is $\sigma / \sqrt { 2 }$ and the standard deviation of the angular rates is $\scriptstyle { \sqrt { 2 } } \sigma / \Delta t$ .

# Prediction for an attributable

Predictions of an attributable $A ( t )$ are a straightforward generalization of the standard ephemerides $( \alpha ( t ) , \delta ( t ) )$ discussed in Section 7.5. Let us assume the prediction function $G$ maps an open set of the initial conditions space into a four-dimensional space, that is the vector of observables is

$$
\mathbf { y } ( { \bar { t } } ) = ( \alpha ( { \bar { t } } ) , \delta ( { \bar { t } } ) , { \dot { \alpha } } ( { \bar { t } } ) , { \dot { \delta } } ( { \bar { t } } ) ) = G \left( \mathbf { x } ( { \bar { t } } ) \right) .
$$

Given initial conditions $\mathbf { x }$ at time $t _ { 0 }$ with covariance $\Gamma$ , the prediction function $F = G \circ \Phi _ { t _ { 0 } }$ is also four-dimensional and its partial derivatives form the matrix $D F$ of dimension $4 \times 6$ : the covariance and normal matrix, by the same argument of Section 7.5, are the $4 \times 4$ matrices obtained from $\Gamma$ by

$$
\Gamma _ { \mathbf { y } } = ( D F ) \Gamma ( D F ) ^ { T } , \quad C _ { \mathbf { y } } = \Gamma _ { \mathbf { y } } ^ { - 1 } .
$$

The matrix $\Gamma _ { \mathbf { y } }$ can be used to assess the uncertainty of all the components of the attributable, e.g., the RMS uncertainty of the angles $( \alpha , \delta )$ (see Figure 8.4) as well as that of the angular rates $( { \dot { \alpha } } , { \dot { \delta } } )$ . The normal matrix $C _ { \mathbf { y } }$ can be used to define the metric used in the attribution algorithm.

# Attribution penalty

Let $\mathbf { x } _ { 1 }$ be the attributable, that is the four-dimensional vector representing the set of observations to be attributed, and $C _ { 1 }$ be the $4 \times 4$ normal matrix of the fit used to compute it. Let $\mathbf { x } _ { 2 }$ be the predicted attributable, computed from the known least squares orbit, and $\Gamma _ { 2 }$ be the covariance matrix of such a four-dimensional prediction, obtained by propagation of the covariance of the orbital elements (as discussed above). Then $C _ { 2 } = \Gamma _ { 2 } ^ { - 1 }$ is the corresponding normal matrix. With this new interpretation for the symbols $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , C _ { 1 } , C _ { 2 }$ , the algorithm for linear attribution uses the same formulae of Section 7.2 applied in the four-dimensional attributable space:

$$
\begin{array} { r c l } { { C _ { 0 } } } & { { = } } & { { C _ { 1 } + C _ { 2 } , ~ \Gamma _ { 0 } = C _ { 0 } ^ { - 1 } } } \\ { { { \cal K } _ { 4 } } } & { { = } } & { { \left( { \bf x } _ { 2 } - { \bf x } _ { 1 } \right) \cdot \left[ C _ { 1 } - C _ { 1 } \Gamma _ { 0 } C _ { 1 } \right] \left( { \bf x } _ { 2 } - { \bf x } _ { 1 } \right) } } \\ { { { \bf x } _ { 0 } } } & { { = } } & { { \Gamma _ { 0 } \left[ C _ { 1 } { \bf x } _ { 1 } + C _ { 2 } { \bf x } _ { 2 } \right] . } } \end{array}
$$

In particular, the attribution penalty $K _ { 4 } / m$ ( $m = 8$ , the number of scalar components of the two attributables) is computed and used as a control to filter out the orbit-attributable pairs which cannot belong to the same object (unless the observations are exceptionally poor). For the orbit-attributable couples with $K _ { 4 }$ below some control value, the next stages are to select a preliminary orbit and to perform differential corrections.

If, for an orbit-attributable couple, the orbit is good enough, it could be used as a preliminary orbit without modifications. That is, the orbit computed with the data of the first arc is used as a first guess for the differential correction iterations, fitting the observations of both arcs. In more difficult cases, e.g., when the orbit for the first arc has not been obtained by a least squares fit, but is itself a preliminary orbit, a better preliminary orbit can be estimated from the four-dimensional compromise attributable $\mathbf { x } _ { 0 }$ . This is discussed in Section 8.5.

# Attribution procedure

As in the case of orbit identification, a procedure to try to attribute a large number of attributables to a large orbit catalog needs to use a sequence of filters. We have experimented with the following filters:

(i) comparison of the two-dimensional prediction $( \alpha , \delta )$ from the orbit at the attributable time with the angles of the attributable;   
(ii) computation of the attribution penalty $K _ { 4 }$ from the attributable and the predicted attributable from the orbit;   
(iii) confirmation by differential corrections and quality control.

The choice of the controls for selection in each filter is very delicate, and needs to be based on experience since there is no analytic estimate available. The extensive tests of Milani et al. (2001a) have resulted in a large number (thousands) of identifications. Additional and even more extensive tests have been performed in the context of the simulation of future Solar System surveys, see (Milani et al. 2005a, Milani et al. 2008) and Chapters 8 and 11.

The case which has not been fully studied yet is the one in which two very different data sets are used, e.g., attributables from a current survey and a catalog of orbits from historic data. If the cataloged orbits are based on much longer observed arcs, possibly with lower accuracy observations, an ad hoc quality control procedure needs to be used, based on the increase of the quality control parameters as a result of the attribution rather than the absolute value of the controls.

LINKAGE

In Chapter 7 we explained how to compute an attributable

$$
A = ( \alpha , \delta , \dot { \alpha } , \dot { \delta } ) \in [ - \pi , \pi ) \times ( - \pi / 2 , \pi / 2 ) \times \mathbb { R } ^ { 2 }
$$

at a certain time $t$ , given $\geq 2$ observations of a celestial body. Throughout this chapter, we shall use only the information contained in the attributable to try to achieve identifications and therefore orbit determination. This chapter is based on (Milani et al. 2001a, Milani et al. 2004, Milani et al. 2005a, Tommei et al. 2007, Gronchi et al. 2008) and ongoing research.

# 8.1 Admissible region

Let $A$ be an attributable at time $t$ for a celestial body $\boldsymbol { B }$ (e.g., an asteroid). We denote by $\mathbf { r }$ and $\mathbf { q }$ the heliocentric position vectors of the body and the observer on the Earth at time $t$ . Let $r = \| \mathbf { r } \|$ , $q = \| \mathbf { q } \|$ be the Euclidean norms of these vectors. We also write $( \rho , \alpha , \delta ) \in \mathbb { R } ^ { + } \times [ - \pi , \pi ) \times ( - \pi / 2 , \pi / 2 )$ for the spherical coordinates of the topocentric position $\rho = \mathbf { r } - \mathbf { q }$ of the body, with $\rho = \| \rho \|$ . The information contained in the attributable $A$ leaves completely unknown the topocentric distance $\rho$ and the radial velocity $\dot { \rho }$ of $\boldsymbol { B }$ .1 The purpose of this section is to constrain the possible values of $\rho , { \dot { \rho } }$ with the hypothesis that the observed object is a Solar System body.

# Excluding interstellar orbits

We introduce the following notation: let

$$
\mathcal { E } _ { \odot } ( \rho , \dot { \rho } ) = \frac { 1 } { 2 } \| \dot { \mathbf { r } } ( \rho , \dot { \rho } ) \| ^ { 2 } - k ^ { 2 } \frac { 1 } { r ( \rho ) } ,
$$

1 The same quantities are called range and range-rate in the context of spacecraft tracking.

with $k = 0 . 0 1 7 2 0 2 0 9 8 9 5$ the Gauss constant, be the two-body energy of the heliocentric orbit of $\boldsymbol { B }$ , in the approximation neglecting the mass of $\boldsymbol { B }$ . Note that we are using 1 AU as the unit of length and 1 ephemeris day as the unit of time; we do not need to specify the unit of mass as $\mathcal { E } _ { \odot } ( \rho , \dot { \rho } )$ is the two-body energy per unit mass of $\boldsymbol { B }$ . We describe the region excluding interstellar orbits, that is satisfying the condition

$$
\mathcal { E } _ { \odot } ( \rho , \dot { \rho } ) \stackrel { } { \_ } 0 .
$$

In particular we shall show that this region can have either one or two connected components. The heliocentric position of $\boldsymbol { B }$ is given by

$$
\mathbf { r } = \mathbf { q } + \rho \hat { \pmb { \rho } } ,
$$

where $\hat { \rho }$ is the unit vector in the observation direction. Using the spherical coordinates $( \rho , \alpha , \delta )$ , the heliocentric velocity $\dot { \mathbf { r } }$ of $\boldsymbol { B }$ is

$$
\dot { \mathbf { r } } = \dot { \mathbf { q } } + \dot { \rho } \hat { \pmb { \rho } } + \rho \dot { \alpha } \hat { \pmb { \rho } } _ { \alpha } + \rho \dot { \delta } \hat { \pmb { \rho } } _ { \delta } ,
$$

where ${ \hat { \pmb { \rho } } } _ { \alpha } = \partial { \hat { \pmb { \rho } } } / \partial \alpha$ , $\hat { \rho } _ { \delta } = \partial \hat { \rho } / \partial \delta$ , and $\dot { \mathbf { q } }$ is the heliocentric velocity of the observer. In coordinates

$$
\begin{array} { r c l } { \hat { \pmb { \rho } } } & { = } & { ( \cos \alpha \cos \delta , \sin \alpha \cos \delta , \sin \delta ) , } \\ { \hat { \pmb { \rho } } _ { \alpha } } & { = } & { ( - \sin \alpha \cos \delta , \cos \alpha \cos \delta , 0 ) , } \\ { \hat { \pmb { \rho } } _ { \delta } } & { = } & { ( - \cos \alpha \sin \delta , - \sin \alpha \sin \delta , \cos \delta ) , } \end{array}
$$

$$
{ \hat { \pmb { \rho } } } \cdot { \hat { \pmb { \rho } } } _ { \alpha } = { \hat { \pmb { \rho } } } \cdot { \hat { \pmb { \rho } } } _ { \delta } = { \hat { \pmb { \rho } } } _ { \alpha } \cdot { \hat { \pmb { \rho } } } _ { \delta } = 0 , \quad \| { \hat { \pmb { \rho } } } \| = \| { \hat { \pmb { \rho } } } _ { \delta } \| = 1 , \quad \| { \hat { \pmb { \rho } } } _ { \alpha } \| = \cos { \delta } .
$$

Thus the squared norms of the heliocentric position and velocity are

$$
r ^ { 2 } ( \rho ) = \rho ^ { 2 } + 2 \rho \mathbf { q } \cdot \hat { \pmb { \rho } } + \| \mathbf { q } \| ^ { 2 } ,
$$

$$
\begin{array} { r l r } { \| \dot { \bf r } ( \rho , \dot { \rho } ) \| ^ { 2 } } & { = } & { \dot { \rho } ^ { 2 } + 2 \dot { \rho } \dot { \bf q } \cdot \hat { \rho } + \rho ^ { 2 } \left( \dot { \alpha } ^ { 2 } \cos ^ { 2 } \delta + \dot { \delta } ^ { 2 } \right) } \\ & { } & { + 2 \rho \left( \dot { \alpha } \dot { \bf q } \cdot \hat { \rho } _ { \alpha } + \dot { \delta } \dot { \bf q } \cdot \hat { \rho } _ { \delta } \right) + \| \dot { \bf q } \| ^ { 2 } . } \end{array}
$$

We shall use the coefficients2

$$
\begin{array} { l c l c l } { { c _ { 0 } } } & { { = } } & { { \| { \bf q } \| ^ { 2 } } } & { { \qquad } } & { { c _ { 3 } } } & { { = } } & { { 2 \dot { \alpha } \dot { \bf q } \cdot \hat { \rho } _ { \alpha } + 2 \dot { \delta } \dot { \bf q } \cdot \hat { \rho } _ { \delta } } } \\ { { c _ { 1 } } } & { { = } } & { { 2 \dot { \bf q } \cdot \hat { \rho } } } & { { \qquad } } & { { c _ { 4 } } } & { { = } } & { { \| \dot { \bf q } \| ^ { 2 } } } \\ { { c _ { 2 } } } & { { = } } & { { \dot { \alpha } ^ { 2 } \cos ^ { 2 } \delta + \dot { \delta } ^ { 2 } = \eta ^ { 2 } } } & { { \qquad } } & { { c _ { 5 } } } & { { = } } & { { 2 { \bf q } \cdot \hat { \rho } , } } \end{array}
$$

and the polynomial expressions

$$
\begin{array} { r c l } { { \| \dot { \mathbf { r } } ( \rho , \dot { \rho } ) \| ^ { 2 } } } & { { = } } & { { 2 T _ { \odot } ( \rho , \dot { \rho } ) = \dot { \rho } ^ { 2 } + c _ { 1 } \dot { \rho } + c _ { 2 } \rho ^ { 2 } + c _ { 3 } \rho + c _ { 4 } , } } \\ { { r ^ { 2 } = S ( \rho ) } } & { { = } } & { { \rho ^ { 2 } + c _ { 5 } \rho + c _ { 0 } , ~ W ( \rho ) = c _ { 2 } \rho ^ { 2 } + c _ { 3 } \rho + c _ { 4 } . } } \end{array}
$$

By substituting the last expressions in (8.2), condition (8.3) reads

$$
2 \mathcal { E } _ { \odot } ( \rho , \dot { \rho } ) = \dot { \rho } ^ { 2 } + c _ { 1 } \dot { \rho } + W ( \rho ) - 2 k ^ { 2 } / \sqrt { S ( \rho ) } \le 0 .
$$

To have real solutions for $\dot { \rho }$ , the discriminant of $\xi _ { \odot }$ , as a polynomial of degree $2$ in $\dot { \rho }$ , must be non-negative, i.e.,

$$
c _ { 1 } ^ { 2 } / 4 - W ( \rho ) + 2 k ^ { 2 } / \sqrt { S ( \rho ) } \geq 0 .
$$

Let us set $\gamma = c _ { 4 } - c _ { 1 } ^ { 2 } / 4$ (note that $\gamma \geq 0$ ), and define $P ( \rho ) = c _ { 2 } \rho ^ { 2 } + c _ { 3 } \rho + \gamma$ ; then condition (8.3) implies

$$
2 k ^ { 2 } / \sqrt { S ( \rho ) } \geq P ( \rho ) .
$$

The polynomial $P ( \rho )$ is non-negative for each $\rho$ : it is the opposite of the discriminant of $\mathcal { T } _ { \odot } ( \rho , \dot { \rho } )$ , regarded as a polynomial in the variable $\dot { \rho }$ . $\tau _ { \odot }$ is a kinetic energy and is non-negative, thus its discriminant is non-positive. Also $S ( \boldsymbol { \rho } )$ is non-negative, thus we can square both sides of (8.10) and obtain an inequality involving a polynomial of degree 6

$$
4 k ^ { 4 } \geq V ( \rho ) = P ^ { 2 } ( \rho ) S ( \rho ) = \sum _ { i = 0 } ^ { 6 } A _ { i } \rho ^ { i } ,
$$

with coefficients

$$
\begin{array} { l l l } { { 4 _ { 0 } } } & { { = } } & { { c _ { 0 } \gamma ^ { 2 } , \quad A _ { 1 } = c _ { 5 } \gamma ^ { 2 } + 2 c _ { 0 } c _ { 3 } \gamma , \quad A _ { 2 } = \gamma ^ { 2 } + 2 c _ { 3 } c _ { 5 } \gamma + c _ { 0 } ( c _ { 3 } ^ { 2 } + 2 c _ { 2 } c _ { 3 } \gamma , } } \\ { { 4 _ { 3 } } } & { { = } } & { { 2 c _ { 3 } \gamma + c _ { 5 } ( c _ { 3 } ^ { 2 } + 2 c _ { 2 } \gamma ) + 2 c _ { 0 } c _ { 2 } c _ { 3 } , } } \\ { { 4 _ { 4 } } } & { { = } } & { { c _ { 3 } ^ { 2 } + 2 c _ { 2 } \gamma + 2 c _ { 2 } c _ { 3 } c _ { 5 } + c _ { 0 } c _ { 2 } ^ { 2 } , \quad A _ { 5 } = c _ { 2 } ( 2 c _ { 3 } + c _ { 2 } c _ { 5 } ) , \quad A _ { 6 } = c _ { 2 } ^ { 2 } . } } \end{array}
$$

The most important property of the region defined by (8.3) is that it has at most two connected components. For a proof, see (Milani et al. 2004).

If the motion of the observer is approximated by a circular heliocentric orbit, it is possible to show that the region of Solar System orbits is connected when the direction of observation is at quadrature (orthogonal to the direction to the Sun). At opposition (direction of observation opposite to the Sun) there can be two connected regions only if the path of the body $\boldsymbol { B }$ on the celestial sphere is retrograde, as in the following example (see Figure 8.1): we have used the attributable $( \alpha , \delta , \dot { \alpha } , \dot { \delta } ) = ( 0 , 0 , - 0 . 0 9 , 0 . 0 1 )$ , with $\dot { \alpha } , \dot { \delta }$ in degrees per day (assuming the Earth is at $( x , y , z ) = ( 1 , 0 , 0 )$ in equatorial coordinates, lengths in AU). We have also plotted the level curves for small positive and negative values of $\xi _ { \odot }$ , showing the qualitative change.

![](images/22338009a20fe01914fc49cc7c89d5b10dfcdf795a9174bcdaef3cad1142a083.jpg)  
Fig. 8.1. An example with two connected components. On the left three level curves of $\varepsilon _ { \odot }$ , including the zero level curve, and $\dot { \varepsilon } _ { \oplus } = 0$ (dashed curve) in the plane $( \rho , \dot { \rho } )$ ; on the right the same plot in the plane $( \log _ { 1 0 } ( \rho ) , \dot { \rho } )$ . Reproduced with permission of Springer from Milani et al. (2004).

To know the number of components of the region defined by (8.3) we have to compute the roots of the degree six polynomial $V ( \rho ) - 4 k ^ { 4 }$ . There are fast and reliable algorithms in the numerical analysis literature providing the roots of a polynomial (as a complex vector), with rigorous upper bounds for the errors including rounding off. We use the algorithm by Bini (1997) and the corresponding public domain software. 3

# The inner boundary

A difficulty in the practical usage of the region defined by condition (8.3) as a tool for the identification problem is that it is not a compact set, that is, the observed object could be at an arbitrarily small distance from the observer. This makes it impossible to sample it with a finite number of points in such a way that the corresponding orbits are representative of the range of ephemeris uncertainty (see the discussion in Section 8.4). There are several ways to assign an inner boundary to the region where $\boldsymbol { B }$ could be, based on different practical considerations:

an inner boundary can be assigned requiring that $\boldsymbol { B }$ is not a satellite of the Earth, i.e., by imposing a condition on the geocentric energy $\mathcal { E } _ { \oplus } ( \rho , \dot { \rho } )$ ;

a minimal distance can be dictated by physical limitations, such as the Earth’s atmosphere or the Earth’s radius $R _ { \oplus }$ in the geocentric approximation;   
a minimal distance can be assigned by requiring that $\boldsymbol { B }$ is not too small, if photometric measurements are supplied together with the astrometry used to compute the attributable.

# Excluding satellites of the Earth

We look for a simple description of the region satisfying the condition $\mathcal { E } _ { \oplus } ( \rho , \dot { \rho } ) \geq 0$ . A simplifying approximation is obtained by assuming that the observations are geocentric: with $\mathbf { q } _ { \oplus }$ the heliocentric position of the Earth’s center, assuming $\mathbf { r } = \pmb { \rho } + \mathbf { q } _ { \oplus }$ , the geocentric energy is

$$
\displaystyle \mathcal { E } _ { \oplus } ( \rho , \dot { \rho } ) = \frac { 1 } { 2 } \| \dot { \pmb \rho } \| ^ { 2 } - k ^ { 2 } \mu _ { \oplus } \frac { 1 } { \rho } \geq 0 ,
$$

where $\mu _ { \oplus }$ is the ratio between the mass of the Earth and the mass of the Sun. By using $\| \dot { \pmb \rho } ( \rho , \dot { \rho } ) \| ^ { 2 } = \dot { \rho } ^ { 2 } + \rho ^ { 2 } \eta ^ { 2 }$ , where $\eta = \sqrt { \dot { \alpha } ^ { 2 } \cos ^ { 2 } \delta + \dot { \delta } ^ { 2 } }$ is the proper motion, (8.12) becomes

$$
\dot { \rho } ^ { 2 } + \rho ^ { 2 } \eta ^ { 2 } - 2 k ^ { 2 } \mu _ { \oplus } \frac { 1 } { \rho } \ge 0 ,
$$

that is

$$
\dot { \rho } ^ { 2 } \geq G ( \rho ) , \qquad \mathrm { w i t h } \quad G ( \rho ) = \frac { 2 k ^ { 2 } \mu _ { \oplus } } { \rho } - \eta ^ { 2 } \rho ^ { 2 } ,
$$

where $G ( \rho ) > 0$ for $0 < \rho < \rho _ { 0 } = \sqrt [ 3 ] { ( 2 k ^ { 2 } \mu _ { \oplus } ) / \eta ^ { 2 } }$

However, condition (8.12) is meaningful only inside the sphere of influence of the Earth, otherwise the dynamics of $\boldsymbol { B }$ is dominated by the Sun, not by the Earth. Thus we need to introduce the condition

$$
\rho \ge R _ { S I } = a _ { \oplus } \ \sqrt [ 3 ] { \mu _ { \oplus } / 3 }
$$

where $R _ { S I }$ is the radius of the sphere of influence, and $a _ { \oplus }$ is the semimajor axis of the Earth. To exclude the satellites of the Earth we have to assume that either (8.12) or (8.14) apply. If $\rho _ { 0 } \leq R _ { S I }$ the region of the satellites to be excluded is defined simply by eq. (8.13); this occurs for

$$
\rho _ { 0 } ^ { 3 } = 2 k ^ { 2 } \mu _ { \oplus } / \eta ^ { 2 } \le R _ { S I } ^ { 3 } = a _ { \oplus } ^ { 3 } \mu _ { \oplus } / 3
$$

thus, taking into account Kepler’s third law $a _ { \oplus } ^ { 3 } n _ { \oplus } ^ { 2 } \simeq k ^ { 2 }$ with $\boldsymbol { n } _ { \oplus }$ the mean motion of the Earth, we have $\rho _ { 0 } \leq R _ { S I }$ if and only if $\eta \geq \sqrt { 6 } \ : n _ { \oplus }$ . Otherwise, if $\rho _ { 0 } > R _ { S I }$ , the boundary of the region containing satellites of the Earth is formed by a segment of the straight line $\rho = R _ { S I }$ and the two arcs of the $\dot { \rho } ^ { 2 } = G ( \rho )$ curve with $0 < \rho < R _ { S I }$ , as in Figures 8.1 and 8.2.

![](images/8e1112e4dd62012c3a6f2e0ff030ad921470492d2ea964dfc20fe68d1ac594e4.jpg)  
Fig. 8.2. The qualitative features of the region of heliocentric orbits in the $( \rho , \dot { \rho } )$ plane: by combining conditions (8.3), (8.12), (8.14) and $\rho \ge R _ { \oplus }$ , we are left with the domain sketched. This figure refers to a case with only one connected component and the plot is in the plane $( \log _ { 1 0 } ( \rho ) , \dot { \rho } )$ .

# The shape of the inner boundary

To understand the shape of the boundary of the Earth satellites region we need to find possible intersections between the curves $ { \mathcal { E } _ { \oplus } } = 0$ and $\xi _ { \odot } = 0$ . However, if $\scriptstyle { \mathcal { E } } _ { \oplus }$ is computed in a geocentric approximation, these intersections are physically meaningful only if they occur for $R _ { \oplus } < \rho < R _ { S I }$ , that is, during a close approach to the Earth, but above its physical surface. In (Milani et al. 2004) we prove that for $R _ { \oplus } ~ \le ~ \rho ~ \le ~ R _ { S I }$ the condition $\mathcal { E } _ { \oplus } ( \rho , \dot { \rho } ) \stackrel { < } { = } 0$ implies $\mathcal { E } _ { \odot } ( \rho , \dot { \rho } ) \leq 0$ .

This result shows that the intersections of the two zero-energy curves occur only where they do not matter; it also implies that the region of Solar System orbits excluding the satellites of the Earth does not have more connected components than the region satisfying condition (8.3) only. This applies only for particular values of the mass, radius, and orbital elements of the planet on which the observer is located. It is a physical property of the Earth, not a general property of whatever planet. A larger planet, such as Jupiter, can have satellites whose velocity would lead to a hyperbolic orbit with respect to the Sun, if Jupiter was not controlling the orbit; the Earth cannot have satellites with this behavior.

# The tiny object boundary

An alternative method to assign a lower limit to the distance is to impose the condition that the object is not a “shooting star” (very small and very close

to the Earth). We assume that the size is controlled by setting a maximum for the absolute magnitude $H$

$$
H ( \rho ) \leq H _ { m a x } .
$$

If some value of the apparent magnitude is available, then the absolute magnitude $H$ can be computed from $h$ , the average of the measured apparent magnitudes, using the relation

$$
H = h - 5 \log _ { 1 0 } \rho - x ( \rho ) ,
$$

where the correction $x ( \rho )$ accounts for the distance from the Sun and the phase effect.4 For small $\rho$ (e.g., $\rho < 0 . 0 1$ AU) the correction $x ( \rho )$ has a negligible dependence upon $\rho$ because the distance from the Sun is $\simeq 1$ AU and the phase is close to the angle between $\hat { \rho }$ and the opposition direction. Thus we can approximate $x ( \rho )$ with a quantity $x _ { 0 }$ independent of $\rho$ . Also for larger values of $\rho$ this is an acceptable approximation. Moreover, we are using $\rho$ , the distance at the reference time $t$ , for all the epochs of the observations including photometry: this is a fair approximation unless the relative change of distance during the time span of the observed arc is relevant, which can happen only for very small distances. In this approximation, condition (8.15) becomes

$$
{ \cal I } _ { m a x } \geq H = h - 5 \log _ { 1 0 } \rho - x _ { 0 } \Longrightarrow \log _ { 1 0 } \rho \geq \frac { h - H _ { m a x } - x _ { 0 } } { 5 } \stackrel { d e f } { = } \log _ { 1 0 } \rho ,
$$

that is, given the apparent magnitude $h$ , we have a minimum distance $\rho _ { H } =$ $\rho ( H _ { m a x } )$ for the object to be of significant size. If we use $H _ { m a x } = 3 0$ (a few meters diameter) and $x _ { 0 } = 0$ then, for example

$$
h = 2 0 \Longrightarrow \rho \geq 0 . 0 1 \mathrm { ~ A U } , \quad h = 1 5 \Longrightarrow \rho \geq 0 . 0 0 1 \mathrm { ~ A U } .
$$

In any case, the absolute magnitude of the object is not a function of $\dot { \rho }$ and the region satisfying condition (8.15) is just a half-plane $\rho \ge \rho _ { H }$ . We call the tiny object boundary the straight line $\rho = \rho _ { H }$ .

Provided $\rho _ { H } \geq R _ { \oplus }$ (for $H _ { m a x } = 3 0$ this occurs for $h \geq 8 . 1$ ) it is possible to use the same arguments of the theorem on the intersection between the energy curves to show that condition (8.15) does not increase the number of connected components with respect to the region defined by excluding the satellites of the Earth. On the contrary it is quite possible that the geometry of the region becomes simpler. If $H _ { m a x } = 3 0$ and $h > 2 0$ the entire sphere of influence of the Earth is excluded by condition (8.15), thus condition (8.14) is implied by (8.15) and condition (8.12) becomes irrelevant.

# Definition of admissible region

We wish to determine a region which is a good approximation of the subset in the $\rho > 0$ half-plane where the object $\boldsymbol { B }$ we are searching for has to be located. Thus we adapt the definition to the goal of the population orbit determination at hand, e.g., it has to be different in a search for objects in heliocentric limited orbit (asteroids, comets, trans-neptunian objects), for objects passing very close to the Earth (meteoroids), and for objects in geocentric orbits (artificial satellites, space debris).

We give as an example a definition appropriate in a search for objects in heliocentric orbit with significant size, thus we can assume that $\rho ( H _ { m a x } ) >$ $R _ { S I }$ . Given an attributable $A$ and selecting a maximum absolute magnitude $H _ { m a x }$ , we define as the admissible region the set

$$
\mathcal { D } ( A ) = \{ ( \rho , \dot { \rho } ) : \rho \geq \rho _ { H } , \mathcal { E } _ { \odot } ( \rho , \dot { \rho } ) \leq 0 \} .
$$

This definition does not use any geocentric approximation, avoiding the problems discussed in Sections 8.7 and 9.4. For smaller objects the portions of the conditions (8.12) and (8.14) should be taken into account.

# 8.2 Sampling of the admissible region

The admissible region consists of at most two compact connected components. Its boundary has an outer part, given by arcs of the curve $\mathcal { E } _ { \odot } ( \rho , \dot { \rho } ) = 0$ , symmetric with respect to the line $\dot { \rho } = - c _ { 1 } / 2$ . The boundary also has an inner part consisting, in the simplest case, of a segment of the line $\rho = \rho ( H _ { m a x } )$ ; for smaller objects, with $\rho ( H _ { m a x } ) < R _ { S I }$ , the inner boundary has a more complicated shape like the one shown in Figure 8.2.

To sample the admissible region we start by sampling its boundary. We would like to select points that are equispaced on the boundary, that is, if the boundary is parameterized by its arc length $s$ , then the distance of each couple of consecutive points corresponds to a fixed increment of $s$ . To avoid the computation of the arc length parameter we use the following idea: we choose a large number of points, equispaced in one of the two coordinates, and then we use an elimination rule to be iterated until we are left with the desired number of points. It can be shown (Milani et al. 2004) that the remaining points are close to the ideal distribution, equispaced in arc length.

# Delaunay triangulations

Consider the polygonal domain $\tilde { \mathcal { D } }$ defined by connecting with edges the sample of boundary points of the admissible region $\mathcal { D }$ ; we shall define a method to triangulate $\tilde { \mathcal { D } }$ . A triangulation of $\tilde { \mathcal { D } }$ is a pair $( \Pi , \tau )$ , where $\Pi = \{ P { 1 , \dots } , P _ { N } \}$ is a set of points (the nodes) of the domain, and $\tau =$ $\{ T _ { 1 } , \dots , T _ { k } \}$ is a set of triangles with vertices in $\Pi$ such that:

(i) $\begin{array} { r } { \bigcup _ { i = 1 , k } T _ { i } = \tilde { \mathcal { D } } } \end{array}$ ;   
(ii) for each $i \neq j$ the set $T _ { i } \int \ d z | T _ { j }$ is either empty or a vertex or an edge of a triangle .

To each triangulation $( \Pi , \tau )$ we can associate the minimum angle, that is the minimum among the angles of all the triangles $T _ { i }$ . Among all possible triangulations of a convex domain a Delaunay triangulation is characterized by these properties (Bern and Eppstein 1992):

(i) it maximizes the minimum angle;   
(ii) it minimizes the maximum circumcircle;   
(iii) for each triangle $T _ { i }$ , the interior part of its circumcircle does not contain any nodes of the triangulation (Risler 1991).

These properties are all equivalent for convex domains.

If the domain is a convex quadrangle whose vertexes $\Pi$ are not on the same circle, then there exist two possible triangulations $( \Pi , \tau _ { 1 } ) , ( \Pi , \tau _ { 2 } )$ : by property (iii), only one of these is Delaunay (see Figure 8.3). In this case the Delaunay triangulation can be obtained from the other one by an edgeflipping technique, which consists of substituting the diagonal $P _ { 1 } P _ { 3 }$ (non-Delaunay edge) of the quadrangle, corresponding to the common edge, with the diagonal $P _ { 2 } P _ { 4 }$ (Delaunay edge). The edge-flipping also results in an increase of the minimum angle.

If, in addition to the set of points $\Pi$ , we give as input also some edges $P _ { i } P _ { j }$ , for example the boundary edges as we do for $\tilde { \mathcal { D } }$ , we refer to the corresponding triangulation containing the prescribed edges as a constrained triangulation.

The domain $\tilde { \mathcal { D } }$ is in general not convex; in this case we need to give as input the edges along the boundary. Then there still exists a constrained triangulation that maximizes the minimum angle (also minimizes the maximum circumcircles, i.e., (i), (ii) hold), called constrained Delaunay triangulation (Bern and Eppstein 1992), but property (iii) is not guaranteed. Figure 8.3 suggests how to transform any triangulation of $\tilde { \mathcal { D } }$ into a constrained Delaunay: for each triangle ${ \bf \Phi } ^ { T } i$ , we iterate a procedure over the adjacent triangles; if the common edge with an adjacent triangle is not Delaunay, we apply the edge-flipping technique. Repeating this procedure until all edges of the triangulation are Delaunay or edges of the boundary of $\tilde { \mathcal { D } }$ , at each step the minimum angle increases and at the end we obtain the triangulation that maximizes the minimum angle (Delaunay 1934).

![](images/029fcd89b40d075be05e7d701a74f6baea4811cbc28524fcc9adf2144050a6fc.jpg)  
Fig. 8.3. Possible triangulations of the quadrangle $P _ { 1 } P _ { 2 } P _ { 3 } P _ { 4 }$ : the one in (A) is a Delaunay triangulation. We mark in both cases the minimum angle and we draw the circumcircles corresponding to triangle $P _ { 2 } P _ { 3 } P _ { 4 }$ (left plot) and to triangle $P _ { 1 } P _ { 2 } P _ { 3 }$ (right plot). Reproduced with permission of Springer from Milani et al. (2004).

The procedure adopted to triangulate our domain uses as input the sampling of the boundary described above and the polygon formed by these boundary points. The first phase is to generate a constrained Delaunay triangulation $( \Pi _ { 0 } , \tau _ { 0 } )$ with these boundary points and boundary edges. Once the initial triangulation is obtained, we refine it by adding new points internal to the domain, keeping at each insertion the Delaunay property. At each step we add a point extending to the internal part of the domain the discrete density defined on the boundary points by the quantities $\begin{array} { r } { \rho ( P _ { j } ) = \operatorname* { m i n } _ { l \neq j } d ( P _ { l } - P _ { j } ) } \end{array}$ where $d$ is some distance.5 Let $G _ { i }$ be the barycenters of the triangles $T _ { i }$ ; we define the corresponding densities

$$
\tilde { \rho } ( G _ { i } ) = \frac { 1 } { 3 } \sum _ { m = 1 } ^ { 3 } \rho ( P _ { i _ { m } } )
$$

$P _ { i _ { m } } , m = 1 , 2 , 3$ , belongs to the same triangle $T _ { i }$ ) and we add as a new point the barycenter $G _ { \bar { k } }$ that maximizes the minimum distance (weighted with its density $\tilde { \rho } ( G _ { \bar { k } } )$ ) from the nodes of the triangulation. Then we eliminate the corresponding triangle $T _ { \bar { k } }$ and we add to $\tau$ the triangles obtained joining the edges of $\boldsymbol { \mathit { 1 } } _ { \bar { k } } ^ { \prime }$ with the new point (keeping at each triangle insertion the Delaunay optimal property by means of the edge-flipping technique). We

iterate this insertion procedure until

$$
\operatorname* { m a x } _ { G _ { i } } \left( \operatorname* { m i n } _ { j } \left\{ \frac { d ( G _ { i } , P _ { j } ) } { \tilde { \rho } ( G _ { i } ) } \right\} \right) > \sigma ,
$$

where $\sigma$ is a fixed small parameter. In (de’ Michieli Vitturi 2004) it is shown that the algorithm converges and the final number of triangles is $< \mu ( \partial \tilde { D } ) n _ { 0 } / \sqrt { 3 } \sigma$ , where $n _ { 0 }$ is the number of points on the boundary of length $\mu ( \partial \tilde { D } )$ .

When no new point needs to be added, either because some maximum number has been reached, or because the convergence criterion (8.18) is fulfilled, we apply to the triangulation obtained as above a mesh improvement technique, generalizing Laplacian smoothing (Winslow 1964, Field 1988). We move every internal point $P _ { j }$ of the triangulation to the center of mass (weighted with the density defined above) of the polygon formed by all its neighboring points (i.e., the ones connected to $P _ { j }$ by an edge), if it lies inside the polygon. This technique improves the quality of the triangulation, but it can produce a triangulation that is not Delaunay, so that we apply again the edge-flipping technique at the end of the smoothing algorithm. The final result is a triangulation optimal from the point of view of property (i), that is avoiding as much as possible “flattened” triangles.

The definition of Delaunay triangulation uses distances and angles, thus it depends on the metric selected for the space $( \rho , \dot { \rho } )$ , in fact its own definition is based on computations of distances and angles. In particular we can select a strictly increasing function $f ( \rho )$ and perform the triangulation of the admissible region with the metric $d s ^ { 2 } = d f ( \rho ) ^ { 2 } + d \dot { \rho } ^ { 2 }$ , i.e., we can work in the plane $( f ( \rho ) , \dot { \rho } )$ endowed with the Euclidean metric. In our work we have selected an adaptive metric, defined by the function

$$
f ( \rho ) = 1 - \exp \left( - \frac { \rho ^ { 2 } } { 2 s ^ { 2 } } \right) .
$$

Since $f ^ { \prime } ( \rho )$ is maximum at $\rho = s$ , by choosing the parameter $s$ we select which part of the admissible region should be more densely sampled. For example, we can use $s = \rho _ { m a x }$ , the largest root of the polynomial equation obtained by selecting the equal sign in (8.11); with this choice we enhance the portion of the space $( \rho , \dot { \rho } )$ farthest from the observer. If our purpose is to search for objects in a particular portion of the $( \rho , \dot { \rho } )$ space, then we can use a metric selected ad hoc. For example, to enhance the region near the Earth we can use either a smaller $s$ , or possibly $f ( \rho ) = \log _ { 1 0 } ( \rho )$ as in Figure 8.1.

# 8.3 Attributable orbital elements

Given a short arc of observations, after computing the attributable we are left with a totally undetermined point in the $( \rho , \dot { \rho } )$ plane. Following Section 8.1, we can assume that this point belongs to an admissible region of Solar System orbits, and we can sample this compact region by a finite Delaunay triangulation. Each node defines a virtual asteroid, that is a possible, but by no means determined, set of six quantities6

$$
X = [ \alpha , \delta , \dot { \alpha } , \dot { \delta } , \rho , \dot { \rho } ]
$$

which are topocentric spherical polar coordinates, in a different order. A set of six initial conditions uniquely determines the orbit of an asteroid, thus it is a set of orbital elements, belonging to a new type (different from the classical coordinates, such as Keplerian, equinoctial, cometary, Cartesian, etc.). We shall call such data a set of attributable orbital elements.

# Distance-dependent corrections

We need to refer a set of orbital elements to an epoch time $t _ { 0 }$ ; we can also obtain a value for the absolute magnitude $H$ if there are photometric measurements together with the astrometric ones. The values of these quantities are not equal to the mean observation time $t$ and the mean apparent magnitude $h$ computed with the attributable, but require distance dependent corrections. An observation at time $t$ of an asteroid needs to be corrected for aberration. The light spends a significant time $\delta t = \rho / c$ , with $c$ the speed of light, to reach the observer from $\boldsymbol { B }$ ; this means that the asteroid is observed at time $\bar { t }$ for its position at the time $\bar { t } - \delta t = t _ { 0 }$ , the epoch time of the orbital elements, which is a function of $\rho$ .

Equation (8.16) describing the relationship between apparent magnitude $h$ and the absolute magnitude $H$ has the form $\begin{array} { r } { H = h + Z ( \rho ) } \end{array}$ , thus also $H =$ $H ( \rho )$ . In conclusion, both $t _ { 0 }$ and $H$ change for different virtual asteroids with the same attributable.

Two approximations are used in the above definitions. The values of the angles $( \alpha , \delta )$ are corrected for aberration with an approximation to some order $7$ in $\delta t$ . A single $\delta t ( \rho )$ and a single $Z ( \rho )$ are used for all observations, while the value of $\rho$ is not constant in time: this approximation may fail if the distance changes significantly during the arc time span, that is if $\dot { \rho } \delta t$ is of the order of $\rho$ , in practice this can happen only for very small $\rho$ .

To convert from attributable elements to Cartesian ones we use eqs. (8.4), and (8.5), thus $( \mathbf { r } , { \dot { \mathbf { r } } } )$ are functions of $( \rho , \dot { \rho } )$ , of $\hat { \pmb \rho } = \hat { \pmb \rho } ( { \alpha } , { \delta } )$ , and other quantities depending upon the attributable. However, they also contain $\mathbf { q }$ and $\dot { \mathbf { q } }$ , which represent the position and velocity of the observer at time $t = t _ { 0 } + \delta t$ . The observer position is close to the geocenter position at the same time: $\mathbf { P } = \mathbf { q } - \mathbf { q } _ { \oplus }$ is small, $\left| \mathbf { P } \right| \simeq R _ { \oplus } \simeq 4 \times 1 0 ^ { - 5 } \left| \mathbf { q } _ { \oplus } \right|$ , but a significant contribution to the heliocentric velocity comes from the observer geocentric velocity, which has size $| { \bf P } | = \Omega _ { \oplus } R _ { \oplus } \cos \theta \simeq 0 . 5 \cos \theta ~ \mathrm { k m / s } \leq | { \dot { \bf q } } _ { \oplus } | / 6 0$ , where $\Omega _ { \oplus }$ is the angular velocity of the Earth’s rotation and $\theta$ is the latitude of the observer.

The problem is that the main frequency of the geocentric motion is $\Omega _ { \oplus }$ , more than two orders of magnitude faster than the mean motion of both the Earth and the asteroid. Thus the quadratic interpolation used to compute the attributable fails to represent correctly the motion of the observer (see Figure 9.1), unless the time span of the observations used for the attributable is much shorter than one day. In (Poincar´e 1906), to solve a similar problem (see Section 9.4), it is suggested to make a quadratic interpolation for the geocentric position vectors at the individual observations times to estimate $\mathbf P ( t )$ and $\dot { \mathbf { P } } ( \bar { t } )$ . These values must be used in eqs. (8.4) and (8.5) when the time span of the observations used to form the attributable is of the order of one day or more, and can improve the results even for shorter arcs.

# Structure of the confidence regions

The problem is how to represent the uncertainty of a set of attributable orbital elements, obtained from a given attributable. This case is quite different from the customary one, in which the uncertainty of a set of orbital elements is described by a positive definite $6 \times 6$ covariance matrix, computed in the differential corrections, by a fit to $\geq 3$ observations well separated in time and in direction, see Section 10.5.

Among the attributable orbital elements, the first four coordinates are the attributable $A$ , computed by a least squares fit, thus with a positive definite $4 \times 4$ covariance matrix $\Gamma _ { A }$ . The last two coordinates are the point $B =$ $( \rho , \dot { \rho } )$ , to be selected in the admissible region. To describe the uncertainty of the attributable orbital elements $X = [ A , B ]$ we need to translate into a mathematical formalism the intuitive statement that the attributable $A$ is measured, the point $B$ is just conjectured.

The inverse of the covariance matrix $\Gamma _ { A }$ , which is used in the least squares fit to compute $A$ , is the $4 \times 4$ conditional normal matrix $C _ { A }$ , appearing in a probabilistic interpretation in the Gaussian probability density for the variables $A$ assuming that $B$ has a given value, that is assuming the selected virtual asteroid. $C _ { A }$ can be built with the design matrix, giving the partials of the observations $( \alpha _ { i } , \delta _ { i } )$ with respect to the four coordinates of $A$ . Thus also $\Gamma _ { A }$ is the conditional covariance matrix $^ 8$ of the attributable. We can formally define the conditional covariance matrix for the attributable elements $X$ as the $6 \times 6$ symmetric matrix

$$
\Gamma _ { X } = \left[ \begin{array} { c c } { { \Gamma _ { A } } } & { { { \bf 0 } } } \\ { { { \bf 0 } } } & { { { \bf 0 } } } \end{array} \right] ,
$$

with 0 suitable matrices with null coefficients. $\Gamma _ { X }$ is obviously not positive definite: it has the $B$ subspace as kernel (null space). The $2 \times 2$ submatrix in the lower right-hand corner is $\Gamma _ { B } = \mathbf { 0 }$ because the value of $B$ has been assumed at some exact value, no uncertainty. The companion matrix

$$
C _ { X } = \left[ \begin{array} { c c } { C _ { A } } & { \mathbf { 0 } } \\ { \mathbf { 0 } } & { \mathbf { 0 } } \end{array} \right]
$$

is the conditional normal matrix in 6-space. $C _ { X }$ and $\Gamma _ { X }$ are not inverse of each other, but pseudo-inverse, that is $\Gamma _ { X }$ is indeed the matrix providing the least squares differential correction for $X$ when $B$ is constrained to a fixed value, see eq. (10.9).

A covariance matrix which is not positive definite, such as $\Gamma _ { X }$ , can be used in the same way (with some caution) as a conventional covariance matrix to compute the uncertainty of predictions, such as future observations. The covariance $\Gamma _ { X }$ can be propagated and/or transformed to a covariance matrix in some other coordinate system, e.g., Cartesian coordinates $Y$ . Then, given the Jacobian matrix $\partial Y / \partial X$ ,

$$
\Gamma _ { Y } = \frac { \partial Y } { \partial X } \Gamma _ { X } \frac { \partial Y } { \partial X } ^ { T }
$$

is also not positive definite, with a two-dimensional null space, containing the radial direction in both position and velocity. It is possible to propagate also the normal matrix, by using the inverse Jacobian matrix $\partial X / \partial Y$

$$
C _ { Y } = \frac { \partial { X ^ { T } } } { \partial { Y } } C _ { X } \frac { \partial { X } } { \partial { Y } } .
$$

$C _ { Y }$ also has a null space of dimension 2, $C _ { Y }$ and $\Gamma _ { Y }$ are pseudo-inverse.

In the formulae of this section we have used so far a rather standard notation; from now on we will face the following ambiguity: a normal matrix and a covariance matrix are functions of the values of the variables for which they are computed. The matrices resulting from the differential corrections process are the ones at convergence, e.g., if the vector $A$ has to be determined, and the nominal least squares solution is $A _ { 1 }$ , the normal matrix $C _ { A }$ must be computed by using the design matrix computed in $A _ { 1 }$ ; then the notation should stress this:

$$
C _ { A } \vert _ { A = A _ { 1 } } , ~ \Gamma _ { A } \vert _ { A = A _ { 1 } } .
$$

However, we shall also use the abbreviated version $C _ { A _ { 1 } } , \Gamma _ { A _ { 1 } }$ . A similar problem occurs for partial derivatives of a function $F ( A )$ : confusion is possible between the variable, with respect to which derivation is performed, and the value assumed by the corresponding argument. We shall use the short notation:

$$
\frac { \partial F } { \partial A } \bigg | _ { A _ { 1 } } = \frac { \partial F } { \partial A } \bigg | _ { A = A _ { 1 } } .
$$

# Quasi-product structure

As discussed in Section 8.1, for each value $A$ of the attributable we can define an admissible region ${ \mathcal { D } } ( A )$ in the plane of $B = \left( \rho , \dot { \rho } \right)$ , such that for $B \in { \mathcal { D } } ( A )$ the attributable orbital elements $X = \lfloor A , B \rfloor$ belong to a Solar System body. The set ${ \mathcal { D } } ( A )$ is compact with at most two connected components, and its boundary can be explicitly computed.

Even if we cannot determine the value of $B$ from the observations (no significant curvature information, see Section 9.1), we can assume that, if the exact value of the attributable is $A$ , the value of $B$ is contained in ${ \mathcal { D } } ( A )$ . The existence of an observable real body with $B$ outside ${ \mathcal { D } } ( A )$ is not impossible, but is either very unlikely (observable hyperbolic comets are rare) or outside the scope of this investigation (artificial satellites of the Earth do exist, but they have to be handled separately, see Section 8.7).

Thus the confidence region, describing the uncertainty of the attributable orbital elements $X = \lfloor A , B \rfloor$ , is defined by

$$
Z _ { X } ( \sigma ) = \left\{ [ A , B ] \left| ( A - A _ { 1 } ) ^ { T } C _ { A _ { 1 } } \left( A - A _ { 1 } \right) \le \sigma ^ { 2 } \mathrm { ~ a n d ~ } B \in \mathcal { D } ( A ) \right. \right\}
$$

where $\sigma > 0$ is a parameter, $A _ { 1 }$ is the nominal (least squares) value of the four attributable coordinates at time $\bar { t } _ { 1 }$ , and $C _ { A _ { 1 } }$ is the corresponding normal matrix. This set is not a Cartesian product, although in many cases it can be approximated by the product of a confidence ellipsoid in the space of $A$ times the admissible region computed with the nominal attributable $A _ { 1 }$ :

$$
Z _ { X } ^ { 1 } ( \sigma ) = \left\{ A \left| ( A - A _ { 1 } ) ^ { T } C _ { A _ { 1 } } \left( A - A _ { 1 } \right) \leq \sigma ^ { 2 } \right. \right\} \times \mathcal { D } ( A _ { 1 } ) .
$$

The quasi-product structure of eq. (8.21) and its approximation with the product of eq. (8.22) will play an important role in the following.

# Sampling the confidence region

The practical problem is how to sample the confidence region $Z _ { X } ( \sigma )$ with a finite number of virtual asteroids. Our approach is to use the nodes of a Delaunay triangulation of the admissible region $\mathcal { D } ( A _ { 1 } )$ , the points $\{ B _ { 1 } ^ { i } =$ $( \rho _ { i } , \dot { \rho } _ { i } ) \} _ { i = 1 , k }$ in $\mathcal { D } ( A _ { 1 } )$ ; then the orbits of the virtual asteroids are defined by the attributable orbital elements

$$
\{ X ^ { i } = [ A _ { 1 } , B _ { 1 } ^ { i } ] \} \ i = 1 , k
$$

with epoch times $t _ { 1 } ^ { \ i } = \bar { t } _ { 1 } - \rho _ { i } / c$ . The sampling is adequate for prediction if

(i) the sampling of $\mathcal { D } ( A _ { 1 } )$ by the nodes $\{ B _ { 1 } ^ { \imath } \}$ is dense enough;   
(ii) the uncertainty in the $A$ subspace is not too large, and anyway is appropriately accounted for by the covariance matrix $\Gamma _ { A _ { 1 } }$ ;   
(iii) ${ \mathcal { D } } ( A )$ is not too different from $\mathcal { D } ( A _ { 1 } )$ for values of $A$ far from the nominal, but still inside the confidence ellipsoid for $A$ .

All the above are hypotheses to be verified in concrete cases. Some parameters, such as the number of points in the Delaunay triangulation, can be adjusted to meet the requirements of condition (i). Condition (ii) refers to the reliability of the astrometric measurement error model (see Section 5.8); condition (iii) remains to be investigated.

# 8.4 Predictions from an attributable

We now discuss how to compute a prediction, starting from a set of virtual asteroids, that is from a set of attributable orbital elements with uncertainty

$$
X ^ { i } , t _ { 1 } ^ { i } , H ; \quad \Gamma _ { X ^ { i } }
$$

with $X ^ { i } ~ = ~ [ A _ { 1 } , B _ { 1 } ^ { i } ]$ , obtained as described in the previous section. The process of prediction consists of two steps. The first is the orbit propagation $\Phi$ from $X ^ { \ i }$ at the epoch time $t _ { 1 } ^ { i }$ to the prediction time $t _ { 2 }$ : this gives a set of orbital elements with uncertainty

$$
Y ^ { i } , \bar { t } _ { 2 } , H ; \quad \Gamma _ { Y i }
$$

where the new covariance matrix $\Gamma _ { Y ^ { i } }$ is given by an equation analogous to (8.20). As already mentioned, the elements $Y ^ { \imath }$ can be given in a different coordinate system, e.g., Cartesian coordinates. It follows again from formula (8.20) that the conditional covariance matrix $\Gamma _ { Y ^ { i } }$ has rank 4, that is, it is not positive definite with a two-dimensional null space.

The second step is to compute the observation function $\mathcal { A } : Y ^ { \ i } \mapsto A ^ { \ i }$ with $A ^ { i }$ the attributable predicted at the new observation epoch $t _ { 2 }$ . Since the light leaves the observed body at a time earlier than $t _ { 2 }$ an aberration correction has to be applied again. The Jacobian matrix of partial derivatives of the prediction function $F$ is the $4 \times 6$ matrix

$$
\left. \frac { \partial \mathcal { A } } { \partial Y } \right| _ { Y ^ { i } } .
$$

Generically $^ { 9 }$ this matrix has rank 4. A formula similar to (8.20) for covariance propagation holds also for mappings between spaces of different dimensions, provided the rank of the Jacobian matrix is maximum, see (3.10):

$$
{ \Gamma } _ { A ^ { i } } = \left. \frac { \partial \boldsymbol { A } } { \partial \boldsymbol { Y } } \right| _ { \boldsymbol { Y ^ { i } } } \Gamma _ { \boldsymbol { Y ^ { i } } } \left[ \left. \frac { \partial \boldsymbol { A } } { \partial \boldsymbol { Y } } \right| _ { \boldsymbol { Y ^ { i } } } \right] ^ { \boldsymbol { T } } .
$$

By (8.20), taking into account the zeros of $\Gamma _ { X ^ { i } }$ , this formula implies

$$
\Gamma _ { A ^ { i } } = \left. \frac { \partial \mathcal { A } ^ { \prime } } { \partial X } \right| _ { X ^ { i } } \Gamma _ { X ^ { i } } \left[ \left. \frac { \partial \mathcal { A } ^ { \prime } } { \partial X } \right| _ { X ^ { i } } \right] ^ { T } = \left. \frac { \partial \mathcal { A } ^ { \prime } } { \partial A } \right| _ { X ^ { i } } \Gamma _ { A _ { 1 } } \left[ \left. \frac { \partial \mathcal { A } ^ { \prime } } { \partial A } \right| _ { X ^ { i } } \right] ^ { T }
$$

where $\mathcal { A } ^ { \prime } = \mathcal { A } \circ \Phi$ and the derivatives are with respect to the attributable $A$ at time $t _ { 1 }$ . What is the rank of the $4 \times 4$ matrix $\Gamma _ { A ^ { i } }$ ? The following two statements give a partial answer. First, for $\bar { t } _ { 2 } \to \bar { t } _ { 1 }$ , $A ^ { \ i }$ has $A _ { 1 }$ as limit, the transformation between the two attributables approaches the identity and $\Gamma _ { A ^ { i } }  \Gamma _ { A _ { 1 } }$ , which has rank 4. Thus for $t _ { 2 } - t _ { 1 }$ small enough the rank of $\Gamma _ { A ^ { i } }$ is 4. However, we do not know how small $t _ { 2 } - t _ { 1 }$ has to be for this to be guaranteed.

Second, generically the rows of $\partial A ^ { \prime } / \partial X$ are linearly independent, and they do not belong to the null space of $\Gamma _ { X ^ { i } }$ . Thus generically $\Gamma _ { A ^ { i } }$ has rank 4. However, a matrix can be of maximum rank but numerically degenerate if its conditioning number is larger than the inverse of the machine accuracy. In this case, the matrix has an inverse in exact arithmetic, but the computation of the inverse is numerically unstable and requires the utmost caution.

Thus we expect, in almost all cases, the matrix $\Gamma _ { A ^ { i } }$ to be invertible. We can think of $\Gamma _ { A ^ { i } }$ as the marginal covariance matrix associated to the portion $A ^ { i }$ of the attributable orbital elements $Y ^ { \ i } = [ A ^ { \ i } , B _ { 2 } ^ { \ i } ]$ . Indeed, the uncertainty of the attributable $A ^ { \ i }$ is computed without making any assumption on the non-measured quantities $B _ { 2 } ^ { i } = ( \rho _ { 2 } ^ { i } , \dot { \rho } _ { 2 } ^ { i } )$ . By the rule dual to the one used for the conditional matrices, the marginal normal matrix $C _ { A ^ { i } } = \Gamma _ { A ^ { i } } ^ { - 1 }$ generically exists, but it may be difficult to compute. $1 0$ If the inverse matrix

$$
M = \left[ \left. \frac { \partial \mathcal { A } ^ { \prime } } { \partial A } \right| _ { X ^ { i } } \right] ^ { - 1 }
$$

exists, then $C _ { A ^ { i } }$ can be computed by the formula derived from (8.23)

$$
C _ { A ^ { i } } = M ^ { T } C _ { A _ { 1 } } M .
$$

Thus it is possible in most (maybe not all) cases, to define a confidence ellipsoid for the prediction $A ^ { \ i }$ , corresponding to the assumption $B _ { 1 } ^ { \ i }$ , in 4-space of the attributables $A ^ { \prime }$ at time $t _ { 2 }$ :

$$
Z _ { A ^ { i } } ( \sigma ) = \bigl \{ A ^ { \prime } \bigl | ( A ^ { \prime } - A ^ { i } ) ^ { T } C _ { A ^ { i } } ( A ^ { \prime } - A ^ { i } ) \leq \sigma ^ { 2 } \bigr \} .
$$

This is actually the interior part of a three-dimensional ellipsoid in the fourdimensional space of the attributables, where the second attributable is predicted to be, within a confidence level described by the parameter $\sigma$ . However, this confidence parameter $\sigma$ cannot be interpreted as a $\chi$ . In fact, it is not possible to provide a probabilistic prediction model, unless there is a way to assign probabilities to the points in the admissible region.11

# Triangulated ephemerides

We can draw the conclusions from the discussion in this section and give a definition of the confidence region for the prediction $A ^ { \ i }$ even in the case we are discussing, that is when the only information available is an attributable.

The confidence region for the attributable orbital elements derived from the attributable $A _ { 1 }$ is $Z _ { X } ( \sigma )$ defined by (8.21); we assume it can be approximated by the product $Z _ { X } ^ { 1 } ( \sigma )$ , defined by (8.22). The image on the attributables space at time $t _ { 1 }$ of the admissible region $\mathcal { D } ( A _ { 1 } )$ is a two-dimensional compact manifold with boundary $V = \mathcal { A } ( \Phi \left( \mathcal { D } ( A _ { 1 } ) \right) )$ . We have no way to explicitly compute this manifold as a function of $B = ( \rho , \dot { \rho } )$ , because the map $X  { \mathcal { A } } ^ { \prime } ( X )$ does not have an analytic expression ( $\mathcal { A } ^ { \prime } ( X )$ is the predicted attributable at the second time). We can compute a triangulation of this manifold by using the image of the already computed triangulation $\{ B _ { 1 } ^ { i } \} , i = 1 , k$ , of $\mathcal { D } ( A _ { 1 } )$ . The nodes of the triangulation $A ^ { i } = { \mathcal { A } } ( \Phi ( X ^ { i } ) )$ i n the four-dimensional observations space at $t _ { 2 }$ are the predictions from the VAs $X ^ { i }$ , in turn defined by the nodes $B _ { 1 } ^ { i }$ .

![](images/be46f8a1383386e864605b02a09075c674b174282b0519256cef639d6a5d058b.jpg)  
Fig. 8.4. For the asteroid $\mathrm { 2 0 0 3 ~ B H _ { 8 4 } }$ , the observations 12 days after the discovery have been predicted in the triangulated form by using only the attributable computed with the observations of the discovery night. The ellipses indicate the projected uncertainty coming from the fit of the attributable. The recovery attributable, computed with the actually observed data of the later night, is at $- \alpha = - 1 1 1 ^ { \circ } . 8 , \ \delta = 1 1 ^ { \circ } . 9$ , well within the bundle of ellipses. Reprinted from (Milani et al. 2005a) with permission from Elsevier.

The triangulated ephemerides have to be computed in the fourdimensional predictions space, although some two-dimensional projections can be used to have a good perception of the uncertainty of the attributable and assess the difficulty of a planned recovery, see Figure 8.4.

We associate to each node of the triangulated ephemerides its covariance. We have to think of each node surrounded by its own confidence ellipsoid $Z _ { A } ^ { \ i }$ , defined by eq. (8.26); thus the projections, such as in Figure 8.4, are surrounded by a confidence ellipse. This is an approximation to the tubular neighborhood $T ( V )$ of the two-manifold $V$ which would be obtained by the union of confidence ellipsoids centered in every point of $V$ .

This tubular neighborhood, so difficult to be computed, plays an essential role in different kinds of identification: recovery, precovery, and linkage. For recovery/precovery, given a candidate attributable found either in the sky or in the archives, to decide if the objects are the same we need to assess not only how much each observation is close to the prediction(s), but also whether this discrepancy can be accounted for by the prediction uncertainty.

When planning what area (either in the sky or in the archive images) has to be scanned, the answer is simply that we need the covered area to include the projection on the celestial sphere of $T ( V )$ . This can be approximated by the union of the ellipses, the projection of each $Z _ { A } ^ { \ i }$ on the celestial sphere. It does not matter how many ellipses overlap, because we are not computing a probability density. Figure 8.4 suggests that, with some care to take into account the lower density of the predicted observations along the tiny object boundary, this approximation can give a good idea of the region to be scanned for a recovery/precovery of a certain body.

# 8.5 Linkage by sampling the admissible region

We assume that for a given object $\boldsymbol { B }$ the only observational information available is contained in two attributables, $A _ { 1 }$ at time $t _ { 1 }$ and $A _ { 2 }$ at time $t _ { 2 }$ . Neither from the first nor from the second can we compute an orbit, thus we have a linkage problem.

The idea is to generate a swarm of virtual asteroids $X ^ { i }$ , sampling as described in the previous section the confidence region of one of the two attributables, let us say $A _ { 1 }$ . Then we compute, from each of the $X ^ { i }$ , a prediction $A ^ { \ i }$ for the epoch $t _ { 2 }$ , each with its covariance matrix $\Gamma _ { A ^ { i } }$ . Generically these covariance matrices will be invertible, and the corresponding normal matrices $C _ { A ^ { i } }$ can be computed from eq. (8.25). We also know the normal matrix $C _ { 2 }$ of the attributable $A _ { 2 }$ . Thus for each virtual asteroid $X ^ { i }$ we can compute an attribution penalty according to eq. (7.6)

$$
{ \cal K } _ { 4 } ^ { i } = ( A _ { 2 } - A ^ { i } ) \cdot \left[ C _ { 2 } - C _ { 2 } \Gamma _ { 0 } C _ { 2 } \right] ( A _ { 2 } - A ^ { i } ) , \quad \Gamma _ { 0 } = \left[ C _ { 2 } + C _ { A ^ { i } } \right] ^ { - 1 }
$$

and use the values as a criterion to select some of the virtual asteroids to proceed to the orbit computation. Note that the identification penalty $K _ { 4 } ^ { \ i }$ , computed for a given node $B _ { 1 } ^ { i }$ of the triangulation of $\mathcal { D } ( A _ { 1 } )$ , does not need to be small. First, we cannot know a priori whether the two objects observed at times $t _ { 1 }$ and $t _ { 2 }$ are indeed the same. Second, even if they were the same, the value of $B _ { 1 } ^ { \ i }$ could be totally wrong with respect to the true values of the distance and its derivative at time $\bar { t } _ { 1 }$ . In both cases the two attributables cannot fit, and this will be revealed by a large value of $K _ { 4 } ^ { \ i }$ .

Thus the procedure might be as follows. If for all nodes $i$ the value of the penalty is large, say $K _ { 4 } ^ { i } > K _ { m a x }$ , then we discard the couple $( A _ { 1 } , A _ { 2 } )$ a s not likely to belong to the same body. If there are some nodes $B _ { 1 } ^ { i }$ such that $K _ { 4 } ^ { i } \le K _ { m a x }$ , then we proceed to the next step.

The value of the control $K _ { m a x }$ to be used is difficult to establish a priori, because we lack an analytical theory. We cannot use $\chi ^ { 2 }$ -tables for dimension 8, because we are sampling the confidence region with a finite number of points $B _ { 1 } ^ { \imath }$ , thus we cannot assume that the minimum among the $K _ { 4 } ^ { \ i }$ is the absolute minimum we could get by trying all values of $B _ { 1 } \in { \mathcal { D } } ( A _ { 1 } )$ , that is

$$
\begin{array} { r } { \operatorname* { m i n } _ { i = 1 , k } K _ { 4 } ^ { i } \geq \operatorname* { m i n } _ { B _ { 1 } \in { \mathcal { D } } ( A _ { 1 } ) } K _ { 4 } ( A _ { 1 } , B _ { 1 } ) } \end{array}
$$

and we cannot compute analytically the safety margin to be left to take into account this difference. We conclude that the value of $K _ { m a x }$ to be used in large-scale production of linkages can only be dictated by the analysis of the results of large-scale tests, such as the ones cited in Chapter 11.

The procedure described above provides us also with a number of best fitting corrected attributables $A _ { 2 } ^ { i } = \Gamma _ { 0 } ~ \left[ C _ { A ^ { i } } A ^ { i } + C _ { 2 } A _ { 2 } \right]$ , according to the third equation of (7.6). Each $A _ { 2 } ^ { i }$ comes with its penalty value $K _ { 4 } ^ { i }$ , which is not too large, that is, an orbit with $B _ { 1 } ^ { \ i }$ as distance and radial velocity at time $t _ { 1 } ^ { i }$ and giving the attributable $A _ { 2 } ^ { \ i }$ as observation at time $t _ { 2 }$ , can fit both $A _ { 1 }$ and $A _ { 2 }$ with not too large residuals; the fit is performed in the eight-dimensional space of the residuals of both attributables.

To start differential corrections we need a set of orbital elements to be used as first guess, with a consistent set of six coordinates at the same epoch; such a set is called a preliminary orbit. There is no requirement that such an orbit is accurate: it is only hoped that it belongs to the convergence domain of the differential corrections. To achieve this, we have a number of options, the simpler one is to use the attributable $A _ { 2 } ^ { i }$ and the value $B _ { 2 } ^ { i } = ( \rho _ { 2 } ^ { i } , \dot { \rho } _ { 2 } ^ { i } )$ as computed from the orbit $X ^ { i } = [ A _ { 1 } , B _ { 1 } ^ { i } ]$ at $t _ { 1 } ^ { i }$ . The epoch of this set of initial conditions is $\bar { t } _ { 2 } - \rho _ { 2 } ^ { i } / c$ . Another possibility is to use the attributable back-propagated (linearly) to time $t _ { 1 }$ , starting from $A _ { 2 } ^ { i }$

$$
A _ { 1 } ^ { i } = A _ { 1 } + M ( A _ { 2 } ^ { i } - A ^ { i } ) ,
$$

with $M$ from eq. (8.24), and the value $B _ { 1 } ^ { i }$ of the node, at the epoch $t _ { 1 } ^ { i }$ . In both cases, we find an orbit which could fit both attributables if the quadratic approximation of (7.6) is good enough.

In Figure 8.5 we show the linkage procedure for the asteroid 2003 $\mathrm { B H _ { 8 4 } }$ . We use the attributable of the discovery night and another attributable computed with the observations made five days later. The nodes of the triangulated admissible region with identification penalty $\begin{array} { r l r } { K _ { 4 } ^ { i } } & { { } < } & { ( 0 . 6 ) ^ { 2 } } \end{array}$ are encircled and the edges joining them are enhanced with solid lines. From each of the encircled nodes a constrained differential corrections procedure, explained in Chapter 10, allows us to obtain some orbits that fit better to the observations.

The latter are represented here by the points with the same labels as the encircled nodes; a linear fit shows that they are quite well aligned.

![](images/a7e30272b6d237bd54a34eeac53e8e310d488301816c30d9744ca3683a677721.jpg)  
Fig. 8.5. Attributable from the discovery night of $\mathrm { 2 0 0 3 ~ B H _ { 8 4 } }$ identified with the attributable from five days later. The solid lines join the nodes with penalty $K _ { 4 } ^ { i } < ( 0 . 6 ) ^ { 2 }$ , used to compute preliminary orbits: from each of them we have started a constrained differential correction procedure, finding solutions on the line of variations (see Chapter 10). Reprinted from (Milani et al. 2005a) with permission from Elsevier.

# 8.6 Linkage by the two-body integrals

We shall describe a method (Gronchi et al. 2008) to produce preliminary orbits starting from two attributables $A _ { 1 } , A _ { 2 }$ of the same Solar System body at two epochs $t _ { 1 }$ , $t _ { 2 }$ . It is based on the use of the two-body integrals, which had been proposed also in (Taff and Hall 1977).

# Angular momentum and energy

For a given attributable $A$ the angular momentum vector per unit mass can be written as a polynomial function of the radial distance and velocity $\rho , { \dot { \rho } }$

$$
\mathbf { c } ( \boldsymbol { \rho } , \dot { \boldsymbol { \rho } } ) = \mathbf { r } \times \dot { \mathbf { r } } = \mathbf { D } \dot { \boldsymbol { \rho } } + \mathbf { E } \boldsymbol { \rho } ^ { 2 } + \mathbf { F } \boldsymbol { \rho } + \mathbf { G } ,
$$

where

$$
\left\{ \begin{array} { l l } { \mathbf { D } = \mathbf { q } \times \hat { \boldsymbol { \rho } } } \\ { \mathbf { E } = \dot { \alpha } \hat { \boldsymbol { \rho } } \times \hat { \boldsymbol { \rho } } _ { \alpha } + \dot { \delta } \hat { \boldsymbol { \rho } } \times \hat { \boldsymbol { \rho } } _ { \delta } = \eta \hat { \mathbf { n } } } \\ { \mathbf { F } = \dot { \alpha } \mathbf { q } \times \hat { \boldsymbol { \rho } } _ { \alpha } + \dot { \delta } \mathbf { q } \times \hat { \boldsymbol { \rho } } _ { \delta } + \hat { \boldsymbol { \rho } } \times \dot { \mathbf { q } } } \\ { \mathbf { G } = \mathbf { q } \times \dot { \mathbf { q } } } \end{array} \right.
$$

depend only on the attributable $A$ and the motion of the observer $\mathbf { q } , \dot { \mathbf { q } }$ at the attributable time $t$ . The vectors $\hat { \rho } , \hat { \rho } _ { \alpha } , \hat { \rho } _ { \delta }$ have been defined in Section 8.1.

For the given $A$ the two-body energy as a function of $\rho , { \dot { \rho } }$

$$
2 { \mathcal { E } } ( \rho , { \dot { \rho } } ) = { \dot { \rho } } ^ { 2 } + c _ { 1 } { \dot { \rho } } + c _ { 2 } \rho ^ { 2 } + c _ { 3 } \rho + c _ { 4 } - { \frac { 2 k ^ { 2 } } { \sqrt { \rho ^ { 2 } + c _ { 5 } \rho + c _ { 0 } } } }
$$

depends on $A , \mathbf { q } , { \dot { \mathbf { q } } }$ only through the coefficients $c _ { j }$ of (8.8).

# Equating the integrals

Now take two attributables $A _ { 1 } = ( \alpha _ { 1 } , \delta _ { 1 } , \dot { \alpha } _ { 1 } , \dot { \delta } _ { 1 } )$ , $A _ { 2 } = ( \alpha _ { 2 } , \delta _ { 2 } , \dot { \alpha } _ { 2 } , \dot { \delta } _ { 2 } )$ a t epochs $t _ { 1 } , t _ { 2 }$ ; we shall use subscripts 1 and 2 referring to the different epochs. If $A _ { 1 }$ , $A _ { 2 }$ correspond to the same physical object, then the angular momentum vectors at the two epochs must coincide: this gives

$$
\mathbf { D } _ { 1 } { \dot { \rho } } _ { 1 } - \mathbf { D } _ { 2 } { \dot { \rho } } _ { 2 } = \mathbf { J } \left( \rho _ { 1 } , \rho _ { 2 } \right)
$$

where

$$
{ \bf J } ( \rho _ { 1 } , \rho _ { 2 } ) = { \bf E } _ { 2 } \rho _ { 2 } ^ { 2 } - { \bf E } _ { 1 } \rho _ { 1 } ^ { 2 } + { \bf F } _ { 2 } \rho _ { 2 } - { \bf F } _ { 1 } \rho _ { 1 } + { \bf G } _ { 2 } - { \bf G } _ { 1 } .
$$

Relation (8.31) is a system of three equations in the four unknowns $\rho _ { 1 } , \dot { \rho } _ { 1 } , \rho _ { 2 }$ , $\dot { \rho } _ { 2 }$ , with constraints

$$
\rho _ { 1 } > 0 , \ \rho _ { 2 } > 0 .
$$

By scalar multiplication of (8.31) with $\mathbf { D } _ { 1 } \times \mathbf { D } _ { 2 }$ we eliminate the variables $\dot { \rho } _ { 1 } , \dot { \rho } _ { 2 }$ and obtain the scalar equation

$$
\mathbf { D } _ { 1 } \times \mathbf { D } _ { 2 } \cdot \mathbf { J } ( \rho _ { 1 } , \rho _ { 2 } ) = 0 .
$$

The left-hand side of (8.32) is a quadratic form in the variables $\rho _ { 1 } , \rho _ { 2 }$ : we write it as

$$
q ( \rho _ { 1 } , \rho _ { 2 } ) = q _ { 2 0 } \rho _ { 1 } ^ { 2 } + q _ { 1 0 } \rho _ { 1 } + q _ { 0 2 } \rho _ { 2 } ^ { 2 } + q _ { 0 1 } \rho _ { 2 } + q _ { 0 0 }
$$

with

$$
\begin{array} { r l r } & { q _ { 2 0 } = - \mathbf { E } _ { 1 } \cdot \mathbf { D } _ { 1 } \times \mathbf { D } _ { 2 } , \quad \quad \quad } & { q _ { 0 2 } = \mathbf { E } _ { 2 } \cdot \mathbf { D } _ { 1 } \times \mathbf { D } _ { 2 } , } \\ & { q _ { 1 0 } = - \mathbf { F } _ { 1 } \cdot \mathbf { D } _ { 1 } \times \mathbf { D } _ { 2 } , \quad \quad \quad } & { q _ { 0 1 } = \mathbf { F } _ { 2 } \cdot \mathbf { D } _ { 1 } \times \mathbf { D } _ { 2 } , } \\ & { q _ { 0 0 } = \left( \mathbf { G } _ { 2 } - \mathbf { G } _ { 1 } \right) \cdot \mathbf { D } _ { 1 } \times \mathbf { D } _ { 2 } . } \end{array}
$$

In the geocentric approximation for the observations we note that $\mathbf { G } _ { i }$ is the angular momentum of the Earth at epoch $t _ { i }$ , $i = 1 , 2$ , thus ${ \bf G } _ { 1 } = { \bf G } _ { 2 }$ and $q _ { 0 0 } = 0$ . In this case there is a spurious solution $\rho _ { 1 } = \rho _ { 2 } = 0$ .

The use of the angular momentum integral to determine an orbit of a Solar System body is already present in (Mossotti 1816). More recently, Kristensen (1995) proposed a method to compute a preliminary orbit from two short arcs of observations in which the basic idea is to equate the angular momentum vectors at the two mean epochs of observations.

For the given $A _ { 1 } , A _ { 2 }$ we can also equate the corresponding two-body energies $\mathcal { E } _ { 1 } , \mathcal { E } _ { 2 }$ . By vector multiplication of (8.31) with $\mathbf { D } _ { 1 }$ and $\mathbf { D } _ { 2 }$ , projecting on the direction of $\mathbf { D } _ { 1 } \times \mathbf { D } _ { 2 }$ , we obtain

$$
\dot { \rho } _ { 1 } ( \rho _ { 1 } , \rho _ { 2 } ) = \frac { ( \mathbf { J } \times \mathbf { D } _ { 2 } ) \cdot ( \mathbf { D } _ { 1 } \times \mathbf { D } _ { 2 } ) } { | \mathbf { D } _ { 1 } \times \mathbf { D } _ { 2 } | ^ { 2 } } , \quad \dot { \rho } _ { 2 } ( \rho _ { 1 } , \rho _ { 2 } ) = \frac { ( \mathbf { J } \times \mathbf { D } _ { 1 } ) \cdot ( \mathbf { D } _ { 1 } \times \mathbf { D } _ { 2 } ) } { | \mathbf { D } _ { 1 } \times \mathbf { D } _ { 2 } | ^ { 2 } }
$$

and, substituting into $\mathcal { E } _ { 1 } = \mathcal { E } _ { 2 }$ ,

$$
\mathcal { F } _ { 1 } ( \rho _ { 1 } , \rho _ { 2 } ) - \frac { 2 k ^ { 2 } } { \sqrt { \mathcal { G } _ { 1 } ( \rho _ { 1 } ) } } = \mathcal { F } _ { 2 } ( \rho _ { 1 } , \rho _ { 2 } ) - \frac { 2 k ^ { 2 } } { \sqrt { \mathcal { G } _ { 2 } ( \rho _ { 2 } ) } } ,
$$

for some polynomial functions $\mathcal { F } _ { 1 } ( \rho _ { 1 } , \rho _ { 2 } )$ , $\mathcal { F } _ { 2 } ( \rho _ { 1 } , \rho _ { 2 } )$ , $\mathcal { G } _ { 1 } ( \rho _ { 1 } )$ , $\mathcal { G } _ { 2 } ( \rho _ { 2 } )$ with degrees $\deg ( \mathcal { F } _ { 1 } ) = \deg ( \mathcal { F } _ { 2 } ) = 4$ and $\deg ( \mathcal { G } _ { 1 } ) = \deg ( \mathcal { G } _ { 2 } ) = 2$ . By squaring twice we obtain the polynomial equation

$$
p ( \rho _ { 1 } , \rho _ { 2 } ) = \left[ ( \mathcal { F } _ { 1 } - \mathcal { F } _ { 2 } ) ^ { 2 } \mathcal { G } _ { 1 } \mathcal { G } _ { 2 } - 4 k ^ { 4 } ( \mathcal { G } _ { 1 } + \mathcal { G } _ { 2 } ) \right] ^ { 2 } - 6 4 k ^ { 8 } \mathcal { G } _ { 1 } \mathcal { G } _ { 2 } = 0
$$

with total degree 24. Some spurious solutions may have been added.

# Intersections between the curves

We study the semialgebraic intersection problem

$$
\left\{ \begin{array} { l l } { p ( \rho _ { 1 } , \rho _ { 2 } ) = 0 } \\ { q ( \rho _ { 1 } , \rho _ { 2 } ) = 0 , } \end{array} \right. \qquad \rho _ { 1 } , \rho _ { 2 } > 0
$$

with classical algebraic geometry methods, see (Cox et al. 1996). Let us write

$$
p ( \rho _ { 1 } , \rho _ { 2 } ) = \sum _ { j = 0 } ^ { 2 0 } a _ { j } ( \rho _ { 2 } ) \rho _ { 1 } ^ { j } ,
$$

where

$$
\begin{array}{c} \operatorname { d e g } ( a _ { j } ) = { \left\{ \begin{array} { l l } { 2 0 } & { { \mathrm { ~ f o r ~ } } j = 0 \ldots 4 } \\ { 2 4 - ( j + 1 ) } & { { \mathrm { ~ f o r ~ } } j = 2 k - 1 } \\ { 2 4 - j } & { { \mathrm { ~ f o r ~ } } j = 2 k } \end{array} \right. }  & { { \mathrm { w i t h ~ } } k \geq 3 } \\ { } & { { \mathrm { ~ f o r ~ } } j = 2 k } \end{array} 
$$

and

$$
q ( \rho _ { 1 } , \rho _ { 2 } ) = b _ { 2 } \ \rho _ { 1 } ^ { 2 } + b _ { 1 } \ \rho _ { 1 } + b _ { 0 } ( \rho _ { 2 } )
$$

for some univariate polynomial coefficients $a _ { i } , b _ { j }$ , depending on $\rho _ { 2 }$

We consider the resultant ${ \mathrm { R e s } } ( \rho _ { 2 } )$ of $p , q$ with respect to $\rho _ { 1 }$ : it is a polynomial with degree $\leq 4 8$ , defined as the determinant of the Sylvester matrix

$$
\operatorname { S y L v } ( \rho _ { 2 } ) = \left( \begin{array} { c c c c c c c c } { a _ { 2 0 } } & { 0 } & { b _ { 2 } } & { 0 } & { \ldots } & { \ldots } & { 0 } \\ { a _ { 1 9 } } & { a _ { 2 0 } } & { b _ { 1 } } & { b _ { 2 } } & { 0 } & { \ldots } & { 0 } \\ { \vdots } & { \vdots } & { b _ { 0 } } & { b _ { 1 } } & { b _ { 2 } } & { \ldots } & { \vdots } \\ { \vdots } & { \vdots } & { 0 } & { b _ { 0 } } & { b _ { 1 } } & { \ldots } & { \vdots } \\ { a _ { 0 } } & { a _ { 1 } } & { \vdots } & { \vdots } & { \vdots } & { b _ { 0 } } & { b _ { 1 } } \\ { 0 } & { a _ { 0 } } & { 0 } & { 0 } & { 0 } & { 0 } & { b _ { 0 } } \end{array} \right) .
$$

The positive real roots of ${ \mathrm { R e s } } ( \rho _ { 2 } )$ are the only possible values of $\rho _ { 2 }$ for a solution $( \rho _ { 1 } , \rho _ { 2 } )$ of (8.37). Thus we can use the following scheme to compute the solutions of (8.37):

(1) find the positive roots $\rho _ { 2 } ( k )$ of ${ \mathrm { R e s } } ( \rho _ { 2 } )$ by using a global solution method such as (Bini 1997);   
(2) for each $k$ solve $q ( \rho _ { 1 } , \rho _ { 2 } ( k ) ) = 0$ and compute the two possible values for $\rho _ { 1 } ( k , 1 ) , \rho _ { 1 } ( k , 2 )$ , discarding negative solutions;   
(3) compute $p ( \rho _ { 1 } ( k , 1 ) , \rho _ { 2 } ( k ) )$ , $p ( \rho _ { 1 } ( k , 2 ) , \rho _ { 2 } ( k ) )$ and select $\rho _ { 1 } ( k )$ from the pair that gives zero (at least in exact arithmetic: in practice we select the pair giving the smaller absolute value);   
(4) discard spurious solutions, resulting by squaring to obtain (8.36) from (8.35);   
(5) for the obtained values of $\rho _ { 1 } , \rho _ { 2 }$ compute the values of $\dot { \rho } _ { 1 } ( k ) , \dot { \rho } _ { 2 } ( k )$ by (8.34);   
(6) change coordinates to Cartesian heliocentric elements at times $t _ { 1 } ( k ) , t _ { 2 } ( k )$ , corrected by the aberration due to the finite velocity of the light, and by using the Poincar´e observer interpolation method (see Section 8.3);   
(7) change coordinates to Keplerian elements at times $t _ { 1 } ( k ) , t _ { 2 } ( k )$ .

Note that the values of the angular momentum vector and of the energy at a given time fix the values of the Keplerian elements $a , e , I , \Omega$ . The two attributables $A _ { 1 } , A _ { 2 }$ at epochs $t _ { 1 } , t _ { 2 }$ give eight scalar data, thus the problem is over-determined. From a non-spurious pair $( \tilde { \rho } _ { 1 } , \tilde { \rho } _ { 2 } )$ , the solution of (8.37), we obtain the same values of $a , e , I , \Omega$ at both times $\bar { t } _ { i } = \bar { t } _ { i } - \tilde { \rho } _ { i } / c , i =$ $1 , 2$ , with the aberration correction, but we must check the compatibility conditions

$$
\omega _ { 1 } = \omega _ { 2 } , ~ \ell _ { 1 } = \ell _ { 2 } + n ( \tilde { t } _ { 1 } - \tilde { t } _ { 2 } ) ,
$$

![](images/ae1e45388f85baceaff18d57f79f97be63593b72e07d5d84809a9a93f956a700.jpg)  
Fig. 8.6. Intersections of the curves $p = 0 , q = 0$ in the plane $\rho _ { 1 } , \rho _ { 2 }$ . This example is for asteroid (243) Ida and the intersection corresponding to the true ob ject is marked with an asterisk.

where $\omega _ { 1 } , \omega _ { 2 }$ and $\ell _ { 1 } , \ell _ { 2 }$ are the arguments of perihelion and the mean anomalies of the body at times $\tilde { t } _ { 1 } , \tilde { t } _ { 2 }$ and $n = k a ^ { - 3 / 2 }$ is the mean motion of the celestial body. The first of conditions (8.41) corresponds to the fifth integral of the Kepler problem, from the Laplace–Lenz vector integral (4.11), the second involves a two-body propagation (e.g., by the Kepler equation).

In Figure 8.6 we show the intersections of the algebraic curve $p ( \rho _ { 1 } , \rho _ { 2 } ) = 0$ with the conic $q ( \rho _ { 1 } , \rho _ { 2 } ) = 0$ from two attributables obtained from the orbit of the asteroid (243) Ida, assuming geocentric observations at epochs $> 3 8$ days apart. There are eight intersections with $\rho _ { 1 } , \rho _ { 2 } > 0$ : seven are shown in the figure and one is very near the origin. Removing spurious solutions only three are left, one of which gives a hyperbolic orbit and one grossly fails the conditions (8.41); the only solution left gives a very good preliminary orbit.

This method has been developed recently (Gronchi et al. 2008) and has not yet been submitted to a large-scale test. From a few examples it appears to have a good potential in providing preliminary orbits for difficult linkages between very short observed arcs, providing little information beyond the respective attributables, and separated by a time interval much larger than the arc time spans.

# 8.7 The space debris problem

Near-Earth space is filled by more than 300 000 artificial debris particles with diameter larger than 1 cm (Rossi, 2005). This population is similar to the asteroidal one because its long-term evolution is affected by highvelocity mutual collisions. Another analogy is that there is an impact risk, that is space assets (e.g., the International Space Station) could be seriously damaged by a collision with some debris (see Chapter 12). The space where the debris is placed can be divided into three main regions: low-Earth orbit (LEO), below about 2000 km, medium-Earth orbit (MEO), above 2000 km and below 36 000 km and geosynchronous Earth orbit (GEO) at about 36 000 km of altitude.

In this section we outline the theoretical basis of the orbit determination algorithms for space debris. The main problem to compute the orbits of the observed space debris is the identification $1 2$ of two or more sets of observational data. Exactly as for asteroids, the data contained in the observations during a single pass over an observing station are not enough to obtain a least squares orbit solution. As an example, if the image moves together with the fixed stars, the debris produces a trail the two extremes of which are measured: this gives us a tracklet. The information contained in such data is just the mean angular position and the first time derivatives, that is the attributable, defined by the same formula (8.1) as the asteroid case.

# Admissible regions for Earth satellites

Following Tommei et al. (2007), we use a new interpretation of eq. (8.4) with the geocentric position $\mathbf { r }$ of the debris, the geocentric position $\mathbf { q }$ of the observer, and the topocentric position $\rho$ of the debris: $\mathbf { r } = \pmb { \rho } + \mathbf { q }$ still applies, and eq. (8.2) is replaced by

$$
\mathbf { \mathcal { E } } _ { \oplus } ( \rho , \dot { \rho } ) = \frac { 1 } { 2 } \| \dot { \mathbf { r } } ( \rho , \dot { \rho } ) \| ^ { 2 } - \frac { G m _ { \oplus } } { r ( \rho ) } .
$$

Then a definition of admissible region such that only satellites of the Earth are allowed includes the condition

$$
\begin{array} { r } { \mathcal { E } _ { \oplus } ( \rho , \dot { \rho } ) \stackrel { } { = } 0 . } \end{array}
$$

Given the attributable $A$ at time $\bar { t }$ obtained from the observations, eqs. (8.5), (8.6), (8.7), and (8.8) are the same, as well as the derivation leading to the degree 6 inequality (8.11). Thus the same conclusions apply, namely the region in the $( \rho , \dot { \rho } )$ half-plane $\rho > 0$ fulfilling (8.43) has at most two connected components. One component has an open inner boundary $\rho > 0$ , if a second component exists, it is compact.

The admissible region needs to be compact for the reasons explained in the asteroid case, thus a condition defining an inner boundary needs to be added. The choice for the inner boundary depends upon the specific orbit determination task: a simple method is to add constraints $\rho _ { m i n } \le \rho \le \rho _ { m a x }$ allowing us, e.g., to focus the search of identifications on one of the three classes LEO, MEO, and GEO, as in (Tommei et al. 2007). Another natural choice for the inner boundary is to take $\rho \ge h _ { a t m }$ where $h _ { a t m }$ is the thickness of a portion of the Earth’s atmosphere in which a satellite cannot remain in orbit for a significant time span.13 As an alternative, it is possible to constrain the semimajor axis of the satellite to be larger that $R _ { \oplus } + h _ { a t m } = R$ , and this leads to an equation

$$
\mathcal { E } _ { \oplus } ( \rho , \dot { \rho } ) \geq - \frac { G m _ { \oplus } } { 2 \bar { R } }
$$

which defines another degree 6 inequality with the same coefficients as eq. (8.11) but for a different constant term. Figure 8.7 shows the interplay of different definitions of the inner boundary.

Another possible way to find an inner boundary is to exclude trajectories impacting the Earth in less than one revolution, that is to use an inequality on the perigee $q$ (Farnocchia 2008)

$$
q = a ( 1 - e ) \geq \bar { R } .
$$

By substituting into the two-body formulae from Section 4.2 we obtain

$$
\sqrt { 1 + \frac { 2 \mathcal { E } _ { \oplus } | | \mathbf { c } | | ^ { 2 } } { G ^ { 2 } m _ { \oplus } ^ { 2 } } } \leq 1 + \frac { 2 \mathcal { E } _ { \oplus } \bar { R } } { G m _ { \oplus } } .
$$

Since the left-hand side is $e \geq 0$ , we need to impose the condition

$$
1 + \frac { 2 \mathcal { E } _ { \oplus } \bar { R } } { G m _ { \oplus } } \ge 0
$$

on the right-hand side; this is again $a \geq R$ . By squaring (8.46) we obtain

$$
| | \mathbf { c } | | ^ { 2 } \geq 2 \bar { R } ( G m _ { \oplus } + \mathcal { E } _ { \oplus } \bar { R } ) .
$$

Given the expressions (8.28) for $\mathbf { c }$ and (8.42) for $\varepsilon _ { \oplus }$ , the above condition is an algebraic inequality in the variables $( \rho , \dot { \rho } )$ ; by another squaring it is possible to convert it into a polynomial equation of degree 10 in $\rho$ and degree 4 in $\dot { \rho }$ . Figure 8.7 also shows this inner boundary, as well as an alternative outer boundary constraining the apocenter $Q$ at some large value (the equations are analogous). The main limitation of this approach is that we do not have a rigorous proof that the region defined by eqs. (8.45) and (8.43) has at most two connected components.

![](images/f7cdf13d120a489d074084cb311b6875e10af93db665a83a41d4f86e18e26bfb.jpg)  
Fig. 8.7. The admissible region for an Earth satellite must be a subset of the region with negative geocentric energy. Additional constraints may be added by using the physical boundary $R =$ $R _ { \oplus } + h _ { a t m }$ defined by the atmosphere and the dynamical boundary defined by the sphere of ⊕ influence $r \le R _ { S I } \colon a \ge R , q \ge R$ and $Q \le R _ { S I }$ can be used.

# Sampling

The admissible region for space debris can be used in the same way as in the asteroid case, to be sampled by a swarm of virtual debris, which is analogous to the virtual asteroids. In this way the linkage problem is transformed into a multiple hypothesis attribution problem, for which the theory is the same as in Sections 8.4 and 8.5.

If the Delaunay triangulation method of Section 8.2 is used, the starting point is a sampling of the boundary of the admissible region. For the outer boundary this is the same as in the asteroid case, for the inner one we can use either a minimum $\rho$ or a minimum perigee $q$ , that is (8.45). The first choice is simpler and leads more easily to a reliable algorithm, because with condition (8.45) we cannot be sure of the number of connected components. A reasonable approach would be to triangulate a region with the simplest inner boundary, then discard the nodes which turn out to have a ballistic orbit with $q < R$ .

# The two-body integrals method for optical observations

Linkage between attributables belonging to space debris can also be obtained by the prime integrals method. All the formulae of Section 8.6 are the same, with the geocentric interpretation of $\mathbf { r }$ and $\mathbf { q }$ and with $G m _ { \oplus }$ in place of $k ^ { 2 }$ . The main difference is a simplification: the geocentric motion of the observer $\mathbf { q }$ has the frequency $\Omega _ { \oplus }$ , which cannot be much faster than the mean motion of the satellites, in most cases it is slower. Thus step (6) of the algorithm of the previous section is simplified, without any need for the Poincar´e observer interpolation method.

As an example, this method could be suitable for GEO debris: with two tracklets belonging to consecutive nights, that is spaced by about one orbital period, it could provide accurate preliminary orbits. There is just one pitfall to be avoided: two attributables spaced in time by one day, taken from the same station, result in an approximate rank deficiency in eq. (8.32), because $\mathbf { D } _ { 1 }$ and $\mathbf { D } _ { 2 }$ are nearly the same (Gronchi et al. 2008). Thus images of the same portion of the GEO belt have to be taken at different hours.

This method has not yet been submitted to large-scale tests; however, we have a program under way to test and compare the prime integrals and the recursive attribution methods specifically for debris in the GEO region.

# Radar attributable and admissible regions

Active artificial satellites and space debris can also be observed by radar: because of the $1 / \rho ^ { 4 }$ dependence of the signal-to-noise for radar observations, range and range-rate are currently measured only for debris in LEO. When a return signal is acquired, the antenna pointing angles are also available. Given the capability of modern radars to scan very rapidly the entire visible sky, $1 4$ radar can be used to discover all the debris above a minimum size while visible from an antenna, or a system of antennas (Mehrholz et al. 2002).

When a radar observation is performed we assume that the measured quantities (all with their own uncertainty) are the range, the range-rate, and also the antenna pointing direction, that is the debris apparent position on the celestial sphere, expressed by two angular coordinates such as right ascension $\alpha$ and declination $\delta$ . The time derivatives of these angular coordinates, $\dot { \alpha }$ and $\dot { \delta }$ , are not measured: therefore the concept of attributable must be modified and an admissible region defined in the $( { \dot { \alpha } } , { \dot { \delta } } )$ plane.

We define as radar attributable a vector

$$
A _ { r a d } = ( \alpha , \delta , \rho , \dot { \rho } ) \in [ - \pi , \pi ) \times ( - \pi / 2 , \pi / 2 ) \times \mathbb { R } ^ { + } \times \mathbb { R } ,
$$

containing the information from a radar observation, at time $t$ ; note that, by analogy with other cases, we assume $t$ is the receive time. Given a radar attributable $A _ { r a d }$ , we define as radar admissible region for a space debris the set of values of $( { \dot { \alpha } } , { \dot { \delta } } )$ such that, for the given radar attributable $A _ { r a d }$

$$
\begin{array} { r } { \mathcal { E } _ { \oplus } ( \dot { \alpha } , \dot { \delta } ) \leq 0 . } \end{array}
$$

In order to compute the admissible region we use the geocentric energy, given by the formula

$$
2 { \mathcal { E } } _ { \oplus } = { \dot { \rho } } ^ { 2 } + c _ { 1 } { \dot { \rho } } + c _ { 2 } \rho ^ { 2 } + c _ { 3 } \rho + c _ { 4 } - { \frac { 2 G m _ { \oplus } } { \sqrt { \rho ^ { 2 } + c _ { 5 } \rho + c _ { 0 } } } }
$$

analogous to eq. (8.30), as a function of the unknown quantities $\dot { \alpha }$ and $\dot { \delta }$ . Among the coefficients (8.8), only $c _ { 2 } = \eta ^ { 2 }$ and $c _ { 3 }$ depend on $\dot { \alpha }$ and $\dot { \delta }$ , thus from eq. (8.30) we have a quadratic polynomial in $\dot { \alpha }$ and $\dot { \delta }$

$$
2 \mathcal { E } _ { \oplus } = z _ { 1 1 } \dot { \alpha } ^ { 2 } + 2 z _ { 1 2 } \dot { \alpha } \dot { \delta } + z _ { 2 2 } \dot { \delta } ^ { 2 } + 2 z _ { 1 3 } \dot { \alpha } + 2 z _ { 2 3 } \dot { \delta } + z _ { 3 3 } ,
$$

with

$$
\begin{array} { r c l r c l } { z _ { 1 1 } } & { = } & { \rho ^ { 2 } \cos ^ { 2 } \delta \quad \quad } & { z _ { 1 3 } } & { = } & { \rho \dot { \mathbf { q } } \cdot \rho _ { \alpha } } \\ { z _ { 1 2 } } & { = } & { 0 } & { z _ { 2 3 } } & { = } & { \rho \dot { \mathbf { q } } \cdot \rho _ { \delta } } \\ { z _ { 2 2 } } & { = } & { \rho ^ { 2 } \quad } & { z _ { 3 3 } } & { = } & { \dot { \rho } ^ { 2 } + c _ { 1 } \dot { \rho } + c _ { 4 } - 2 G m _ { \oplus } / \sqrt { S ( \rho ) } , } \end{array}
$$

where $S ( \rho )$ is defined as in (8.9). The boundary of the admissible region in the $( { \dot { \alpha } } , { \dot { \delta } } )$ plane is then given by

$$
\mathcal { E } _ { \oplus } ( \dot { \alpha } , \dot { \delta } ) = 0 .
$$

For each value of $A _ { r a d }$ , this equation represents a conic section in the $( { \dot { \alpha } } , { \dot { \delta } } )$ plane; more precisely, since $z _ { 1 1 } , z _ { 2 2 } > 0$ and $z _ { 1 2 } = 0$ , it is an ellipse with its axes aligned with the coordinate axes. Actually, in a plane $( \dot { \alpha } \cos \delta , \dot { \delta } )$ , with the axes rescaled according to the metric of the tangent plane to the celestial sphere, the curves $\mathcal { E } _ { \oplus } ( \dot { \alpha } , \dot { \delta } ) = 0$ are circles.

The region defined by negative geocentric energy $\mathcal { E } _ { \oplus } ( \dot { \alpha } , \dot { \delta } ) \leq 0$ is the inside of one ellipse (or circle in the rescaled coordinates). Thus it is a compact set, and the problem of defining an inner boundary of the admissible region is less important than in the optical attributable case. Anyway, it is possible to define an inner boundary by constraining the semimajor axis $a > R$ , that is by eq. (8.44), resulting in a concentric inner ellipse (circle), thus in an admissible region forming an elliptic (circular) annulus.

It is also possible to exclude the ballistic trajectories by imposing $q > R$ , that is by using inequality (8.47), in which $\dot { \alpha } , \dot { \delta }$ are to be considered as variables. Then the geocentric energy is given by (8.51), and the angular momentum by

$$
\mathbf { c } = \mathbf { r } \times { \dot { \mathbf { r } } } = \mathbf { E } + \mathbf { F } { \dot { \boldsymbol { \alpha } } } + \mathbf { G } { \dot { \boldsymbol { \delta } } }
$$

where

$$
\left\{ \begin{array} { l l } { \mathbf { E } = \mathbf { r } \times \dot { \mathbf { q } } + \dot { \rho } \mathbf { q } \times \hat { \rho } , } \\ { \mathbf { F } = \mathbf { r } \times \rho \hat { \rho } _ { \alpha } , } \\ { \mathbf { G } = \mathbf { r } \times \rho \hat { \rho } _ { \delta } . } \end{array} \right.
$$

![](images/9e4de76d9a2caf71c6d6a93eed2822db7b2e9a9d9e5156e59d19839c73330885.jpg)  
Fig. 8.8. Possible shapes of a radar admissible region, including the negative energy condition (outer ellipse) and the pericenter condition (intermediate ellipse on the left, hyperbola on the right); the lower bound to the semima jor axis (inner ellipse) is implied by the pericenter condition.

Note that the geocentric vector $\mathbf { r }$ is fully determined by the radar attributable as $\mathbf { r } = \mathbf { q } + \rho \hat { \rho }$ and contains no unknown. By a sequence of simple algebraic passages, similar to those of the optical case, we can conclude that the admissible region defined by $ { \mathcal { E } _ { \oplus } } \leq 0$ and $q \geq R$ is the set of solutions of the system of three inequalities

$$
\begin{array} { r } { \mathcal { E } _ { \oplus } \leq 0 , \quad \mathcal { E } _ { \oplus } \geq - G m _ { \oplus } / 2 \bar { R } , \quad | | \mathbf { c } | | ^ { 2 } \geq 2 \bar { R } \big ( G m _ { \oplus } + \mathcal { E } _ { \oplus } \bar { R } \big ) , } \end{array}
$$

all three quadratic in the $( { \dot { \alpha } } , { \dot { \delta } } )$ variables. Thus the admissible region can be geometrically described as a region bounded by three conics: the first two are concentric ellipses (circles in the rescaled coordinates), the third one can be either an ellipse or a hyperbola, with a different center and different symmetry axes. Figure 8.8 shows the possible qualitatively different cases.

The sampling of the radar admissible region could be obtained by a Delaunay triangulation, but the algorithm would be cumbersome because of the need to distinguish geometrically distinct cases for the boundary. A simpler method would be to use a spider web sampling for the annulus, that is, in the plane of the rescaled coordinates $( \dot { \alpha } \cos \delta , \dot { \delta } )$ , to use a rectangular grid in the polar coordinates centered in the common center of the two circles. The virtual debris obtained in this way could then be tested for the condition $q > R$ and the ones failing this test discarded, if ballistic trajectories (such as very recent launches) are not among the target of the survey.

# The two-body integrals method for radar observations

The two-body integrals method for linkage of the previous section can also be applied to the case of two radar attributables $A _ { 1 } , A _ { 2 }$ with receive times $t _ { 1 } , t _ { 2 }$ . The formulae for geocentric energy and angular momentum are given by (8.51) and (8.53), polynomials of degree 2 and 1 in the unknowns $( { \dot { \alpha } } , { \dot { \delta } } )$ , respectively. Thus the system of four scalar equations obtained by equating the two energies and the two angular momentum vectors contains three linear equations and a quadratic one, and has overall algebraic degree 2. It follows that such a system can be solved by elementary algebra.

We use subscripts 1 and 2 referring to the different epochs: the angular momentum equations are

$$
\mathbf { E } _ { 1 } + \mathbf { F } _ { 1 } { \dot { \alpha } } _ { 1 } + \mathbf { G } _ { 1 } { \dot { \delta } } _ { 1 } = \mathbf { E } _ { 2 } + \mathbf { F } _ { 2 } { \dot { \alpha } } _ { 2 } + \mathbf { G } _ { 2 } { \dot { \delta } } _ { 2 } ,
$$

where $\mathbf { E } _ { i } , \mathbf { F } _ { i } , \mathbf { G } _ { i }$ for $i = 1 , 2$ are the quantities defined in (8.54) for each of the two radar attributables. The equation above is a system of three linear equations in four unknowns $( \dot { \alpha } _ { 1 } , \dot { \delta } _ { 1 } , \dot { \alpha } _ { 2 } , \dot { \delta } _ { 2 } )$ and can be solved for three unknowns as a function of one of the four. By scalar multiplication with $\mathbf { G } _ { 1 } \times \mathbf { F } _ { 2 }$ we can obtain $\dot { \alpha } _ { 1 }$ as a function of $\dot { \delta } _ { 2 }$ , and so on. This procedure fails only if the four vectors $\mathbf { F } _ { 1 } , \mathbf { F } _ { 2 } , \mathbf { G } _ { 1 } , \mathbf { G } _ { 2 }$ do not generate a linear space of dimension 3. Apart from coordinate singularities, this can happen only if $\mathbf { r } _ { 1 }$ is parallel to $\mathbf { r } _ { 2 }$ , e.g., when the time interval is equal to the orbital period.

When the equations for, say, $( \dot { \alpha } _ { 1 } , \dot { \delta } _ { 1 } , \dot { \alpha } _ { 2 } )$ as a function of $\dot { \delta } _ { 2 }$ are substituted in the equation for the energies

$$
\mathcal { E } _ { \oplus , 1 } ( \dot { \alpha } _ { 1 } , \dot { \delta } _ { 1 } ) = \mathcal { E } _ { \oplus , 2 } ( \dot { \alpha } _ { 2 } , \dot { \delta } _ { 2 } )
$$

we obtain a quadratic equation in $\dot { \delta } _ { 2 }$ , which can be solved by elementary algebra, giving at most two real solutions. Geometrically, the angular momentum equation (8.55) can be described by a straight line in a plane, e.g., in $( \dot { \alpha } _ { 2 } , \dot { \delta } _ { 2 } )$ , where the energy equation defines a conic section.

The practical application of this method to a real case of one or more radar stations surveying for space debris requires some non-trivial additional steps. In particular, it is necessary to check that the assumption that a two-body model is a good approximation for the orbit over the time span from $t _ { 1 }$ to $t _ { 2 }$ . Because the radar observations are limited to LEO, the debris performs between 12 and 16 orbits per day; this implies that in just one day the orbital perturbations due to the non-spherical shape of the Earth’s orbit are significant, especially on the longitude of the node $\Omega$ . The largest changes to $\Omega$ are due to the secular perturbation

$$
\Omega ( t _ { 2 } ) - \Omega ( t _ { 1 } ) \simeq - ( t _ { 2 } - t _ { 1 } ) \ \frac { 3 } { 2 } n \left( \frac { R _ { \oplus } } { a } \right) ^ { 2 } \frac { J _ { 2 } } { ( 1 - e ^ { 2 } ) ^ { 2 } } \cos I
$$

where $J _ { 2 } = - C _ { 2 0 }$ is the coefficient of the second zonal spherical harmonic of the Earth’s gravity field (see Section 13.2). It is possible to account for the precession of the node in a modified version of the two-body integrals method (Farnocchia 2008), obtaining a system of four algebraic equations, but the overall degree is 112. Such a system could be solved with the same methods described in the previous section and in (Gronchi et al. 2008), but it is not yet clear whether this would result in an efficient algorithm.

The simpler method, with explicit solution by elementary algebra, could be applicable if the radar system had the capability of acquiring two radar attributables from most debris within the same pass, or at most at the next pass ( $< 2$ hours later). If this was possible, it would provide a very good example of how to transform a difficult problem of orbit determination, such as linkage, into one with an elementary solution.

# 9

# METHODS BY LAPLACE AND GAUSS

In this chapter we discuss the classical methods by Laplace and Gauss to obtain some preliminary orbit, a solution of the two-body problem, given at least three observations of two angular coordinates $( \alpha , \delta )$ on the celestial sphere. We will show that these procedures are controlled by the presence of curvature, that is information beyond that contained in an attributable. We also discuss the possibility of non-unique solutions. This chapter is based on our papers (Milani et al. 2008, Gronchi 2009).

# 9.1 Attributables and curvature

If there are $m \geq 3$ observations $( \alpha _ { i } , \delta _ { i } )$ of a Solar System body $\boldsymbol { B }$ (e.g., an asteroid) at different times $t _ { i }$ , $i = 1 , m$ , we can compute an attributable $A$ by fitting both angular coordinates as a function of time with a polynomial model. In most cases a degree 2 model, centered at the mean $t$ of the times $t _ { i }$ , is satisfactory:

$$
\begin{array} { r c l } { { \alpha ( t ) } } & { { = } } & { { \alpha ( \bar { t } ) + \dot { \alpha } ( \bar { t } ) ( t - \bar { t } ) + \displaystyle \frac { 1 } { 2 } \ddot { \alpha } ( \bar { t } ) ( t - \bar { t } ) ^ { 2 } , } } \\ { { \delta ( t ) } } & { { = } } & { { \delta ( \bar { t } ) + \dot { \delta } ( \bar { t } ) ( t - \bar { t } ) + \displaystyle \frac { 1 } { 2 } \ddot { \delta } ( \bar { t } ) ( t - \bar { t } ) ^ { 2 } ; } } \end{array}
$$

the vector $( \alpha , \dot { \alpha } , \ddot { \alpha } , \delta , \dot { \delta } , \ddot { \delta } )$ is obtained as a solution of the problem of Section 5.1, together with the two $3 \times 3$ covariance matrices $1 _ { \alpha } , 1 _ { \delta } ^ { \cdot }$ . We are assuming that the $\alpha$ and $\delta$ error components are not correlated, otherwise the $6 \times 6$ covariance matrix of all the variables could be full.

# Computation of curvature

The heliocentric position of the observed body $\boldsymbol { B }$ is the vector $\mathbf { r } \in \mathbb { R } ^ { 3 }$ and the topocentric position is

$$
{ \pmb \rho } = \rho \hat { \pmb \rho } = { \bf r } - { \bf q } ,
$$

where $\mathbf { q }$ is the heliocentric position of the observer, $\hat { \rho }$ is the unit vector defining the observation direction, $\rho$ the topocentric distance of $\boldsymbol { B }$ .

We shall use an orthonormal basis adapted to the apparent path of $\boldsymbol { B }$ on the celestial sphere, that is the image of $\hat { \rho } ( t )$ . Following Danby (1988) we note that

$$
{ \bf v } = \frac { d \hat { \pmb { \rho } } } { d t } = \eta \hat { \bf v } , \hat { \bf v } \cdot \hat { \pmb { \rho } } = 0 ,
$$

where $\eta = \| \mathbf { v } \|$ is the proper motion. By using the arc length parameter $s$ , defined by $d s / d t = \eta$ , we have $d \hat { \rho } / d s = \hat { \mathbf { v } }$ . Denoting with a prime the derivative with respect to $s$ , the derivative $\hat { \mathbf { v } } ^ { \prime }$ has the properties

$$
\begin{array} { r c l } { \hat { \mathbf { v } } ^ { \prime } \cdot \hat { \pmb { \rho } } } & { = } & { \displaystyle \frac { d } { d s } \left[ \hat { \mathbf { v } } \cdot \hat { \pmb { \rho } } \right] - \hat { \mathbf { v } } \cdot \hat { \pmb { \rho } } ^ { \prime } = - 1 , } \\ { \hat { \mathbf { v } } ^ { \prime } \cdot \hat { \mathbf { v } } } & { = } & { \displaystyle \frac { 1 } { 2 } \frac { d } { d s } \| \hat { \mathbf { v } } \| ^ { 2 } = 0 ; } \end{array}
$$

in the orthonormal basis $\{ \hat { \rho } , \hat { \mathbf { v } } , \hat { \mathbf { n } } \}$ , with $\hat { \bf n } = \hat { \pmb { \rho } } \times \hat { \bf v }$ , we can express $\hat { \mathbf { v } } ^ { \prime }$ as

$$
\hat { \mathbf { v } } ^ { \prime } = - \hat { \pmb { \rho } } + \kappa \hat { \mathbf { n } }
$$

for a scalar function $\kappa$ called the geodesic curvature of the path. It measures the deviation of the path from a great circle (a geodesic on the sphere).

The second derivative of the path $\hat { \rho } ( t )$ with respect to $t$ can be computed from $\hat { \mathbf { v } } ^ { \prime }$ and is

$$
\frac { d ^ { 2 } \hat { \pmb { \rho } } } { d t ^ { 2 } } = - \eta ^ { 2 } \hat { \pmb { \rho } } + \dot { \eta } \hat { \bf v } + \kappa \eta ^ { 2 } \hat { \bf n } .
$$

The three components of the vector $d ^ { 2 } \hat { \rho } / d t ^ { 2 }$ give us information on the curvature of the path: the component along $\hat { \bf n }$ is strictly related to the geodesic curvature, that along $\hat { \mathbf { v } }$ is called the along-track acceleration, and that along $\hat { \rho }$ simply means that the path is on a sphere.

To compute the two components $\kappa \eta ^ { 2 }$ , $\dot { \eta }$ of curvature starting from the values of $( \alpha , \delta , \dot { \alpha } , \dot { \delta } , \ddot { \alpha } , \ddot { \delta } )$ , obtained by a polynomial fit of the observations, we use the orthogonal basis $\{ \hat { \rho } , \ \hat { \rho } _ { \alpha } , \ \hat { \rho } _ { \delta } \}$ , where

$$
\begin{array} { r c l } { { \hat { \rho } } } & { { = } } & { { ( \cos \delta \cos \alpha , \cos \delta \sin \alpha , \sin \delta ) , } } \\ { { } } & { { } } & { { } } \\ { { \hat { \rho } _ { \alpha } } } & { { = } } & { { \displaystyle \frac { \partial \hat { \rho } } { \partial \alpha } = ( - \cos \delta \sin \alpha , \cos \delta \cos \alpha , 0 ) , } } \end{array}
$$

$$
\hat { \rho } _ { \delta } ~ = ~ \frac { \partial \hat { \rho } } { \partial \delta } = ( - \sin \delta \cos \alpha , - \sin \delta \sin \alpha , \cos \delta ) ,
$$

with $\| \hat { \pmb \rho } \| = \| \hat { \pmb \rho } _ { \delta } \| = 1$ , $\| \hat { \pmb { \rho } } _ { \alpha } \| = \cos \delta$ . We have the following relations:

$$
\begin{array} { r c l } { { \hat { \mathbf { v } } } } & { { = } } & { { \hat { \boldsymbol { \rho } } ^ { \prime } = \alpha ^ { \prime } \hat { \pmb { \rho } } _ { \alpha } + \delta ^ { \prime } \hat { \pmb { \rho } } _ { \delta } , } } \\ { { } } & { { } } & { { } } \\ { { \hat { \mathbf { n } } } } & { { = } } & { { \hat { \boldsymbol { \rho } } \times \left( \alpha ^ { \prime } \hat { \pmb { \rho } } _ { \alpha } + \delta ^ { \prime } \hat { \pmb { \rho } } _ { \delta } \right) = - \frac { \delta ^ { \prime } } { \cos \delta } \hat { \pmb { \rho } } _ { \alpha } + \alpha ^ { \prime } \cos \delta \hat { \pmb { \rho } } _ { \delta } , } } \\ { { } } & { { } } & { { } } \\ { { \hat { \mathbf { v } } ^ { \prime } } } & { { = } } & { { \left( \alpha ^ { \prime \prime } \hat { \pmb { \rho } } _ { \alpha } + \delta ^ { \prime \prime } \hat { \pmb { \rho } } _ { \delta } \right) + \left( \alpha ^ { \prime 2 } \hat { \pmb { \rho } } _ { \alpha \alpha } + 2 \alpha ^ { \prime } \delta ^ { \prime } \hat { \pmb { \rho } } _ { \alpha \delta } + \delta ^ { \prime 2 } \hat { \pmb { \rho } } _ { \delta \delta } \right) , } } \end{array}
$$

and the second derivative vectors are

$$
\begin{array} { r c l } { { \hat { \rho } _ { \alpha \alpha } } } & { { = } } & { { \displaystyle \frac { \partial ^ { 2 } \hat { \rho } } { \partial \alpha ^ { 2 } } = ( - \cos \delta \cos \alpha , - \cos \delta \sin \alpha , 0 ) , } } \\ { { } } & { { } } & { { } } \\ { { \hat { \rho } _ { \alpha \delta } } } & { { = } } & { { \displaystyle \frac { \partial ^ { 2 } \hat { \rho } } { \partial \alpha \partial \delta } = ( \sin \delta \sin \alpha , - \sin \delta \cos \alpha , 0 ) , } } \\ { { } } & { { } } & { { } } \\ { { \hat { \rho } _ { \delta \delta } } } & { { = } } & { { \displaystyle \frac { \partial ^ { 2 } \hat { \rho } } { \partial \delta ^ { 2 } } = ( - \cos \delta \cos \alpha , - \cos \delta \sin \alpha , - \sin \delta ) . } } \end{array}
$$

We also need the scalar products1

$$
\begin{array} { r l r l } & { \hat { \rho } _ { \alpha \alpha } \cdot \hat { \rho } _ { \alpha } = 0 = \Gamma _ { \alpha \alpha , \alpha } \qquad } & & { \hat { \rho } _ { \alpha \alpha } \cdot \hat { \rho } _ { \delta } = \sin \delta \cos \delta = \Gamma _ { \alpha \alpha , \delta } } \\ & { \hat { \rho } _ { \alpha \delta } \cdot \hat { \rho } _ { \alpha } = - \sin \delta \cos \delta = \Gamma _ { \alpha \delta , \alpha } \qquad } & & { \hat { \rho } _ { \alpha \delta } \cdot \hat { \rho } _ { \delta } = 0 = \Gamma _ { \alpha \delta , \delta } } \\ & { \hat { \rho } _ { \delta \delta } \cdot \hat { \rho } _ { \alpha } = 0 = \Gamma _ { \delta \delta , \alpha } \qquad } & & { \hat { \rho } _ { \delta \delta } \cdot \hat { \rho } _ { \delta } = 0 = \Gamma _ { \delta \delta , \delta } } \end{array}
$$

to compute the geodesic curvature

$$
\kappa = \hat { \mathbf { v } } ^ { \prime } \cdot \hat { \mathbf { n } } = ( \delta ^ { \prime \prime } \alpha ^ { \prime } - \alpha ^ { \prime \prime } \delta ^ { \prime } ) \cos \delta + \alpha ^ { \prime } \left( 1 + \delta ^ { \prime 2 } \right) \sin \delta
$$

as a function of the derivatives with respect to the arc length. To obtain an expression containing the time derivatives we need to use

$$
\alpha ^ { \prime \prime } = { \frac { 1 } { \eta } } ~ { \frac { d } { d t } } ~ \left( { \frac { \dot { \alpha } } { \eta } } \right) = { \frac { \eta \ddot { \alpha } - \dot { \eta } \dot { \alpha } } { \eta ^ { 3 } } }
$$

and the analog for $\delta ^ { \prime \prime }$ ; with the terms containing $\dot { \eta }$ canceling out we obtain

$$
\kappa \eta ^ { 2 } = \frac { 1 } { \eta } \left[ ( \ddot { \delta } \dot { \alpha } - \ddot { \alpha } \dot { \delta } ) \cos \delta + \dot { \alpha } ( \eta ^ { 2 } + \dot { \delta } ^ { 2 } ) \sin \delta \right] .
$$

To compute the along-track acceleration we consider the second derivative

$$
{ \frac { d ^ { 2 } { \hat { \rho } } } { d t ^ { 2 } } } = \left( { \ddot { \alpha } } { \hat { \rho } } _ { \alpha } + { \ddot { \delta } } { \hat { \rho } } _ { \delta } \right) + \left( { \dot { \alpha } } ^ { 2 } { \hat { \rho } } _ { \alpha \alpha } + 2 { \dot { \alpha } } { \dot { \delta } } { \hat { \rho } } _ { \alpha \delta } + { \dot { \delta } } ^ { 2 } { \hat { \rho } } _ { \delta \delta } \right)
$$

so that

$$
\dot { \boldsymbol { \eta } } = \frac { d ^ { 2 } \hat { \rho } } { d t ^ { 2 } } \cdot \hat { \mathbf { v } } = \frac { \ddot { \alpha } \dot { \alpha } \cos ^ { 2 } \delta + \ddot { \delta } \dot { \delta } - \dot { \alpha } ^ { 2 } \dot { \delta } \cos \delta \sin \delta } { \eta } .
$$

1 That is, the Riemannian connection of the sphere, as expressed by the Christoffel symbols.

# 9.2 The method of Laplace

In the orthonormal basis $\{ \hat { \rho } , \hat { \mathbf { v } } , \hat { \mathbf { n } } \}$ we can write the first and second time derivatives of the topocentric vector $\rho$ as follows:

$$
\begin{array} { r c l } { \dot { \rho } } & { = } & { \dot { \rho } \hat { \rho } + \rho \eta \hat { \mathbf { v } } , } \\ { \ddot { \rho } } & { = } & { ( \rho \dot { \eta } + 2 \dot { \rho } \eta ) \hat { \mathbf { v } } + \rho \eta ^ { 2 } \kappa \hat { \mathbf { n } } + \ddot { \rho } - \rho \eta ^ { 2 } \hat { \rho } . } \end{array}
$$

The Laplace method uses the following approximations: $\mathbf { q }$ is the position of the center of the Earth (geocentric approximation) and the mass of all the planets is zero. Then the two-body formula can be used for the accelerations $\ddot { \rho }$ and $\ddot { \bf q }$

$$
{ \ddot { \rho } } = { \frac { - \mu \mathbf { r } } { r ^ { 3 } } } + { \frac { \mu \mathbf { q } } { q ^ { 3 } } }
$$

where $r$ is the heliocentric distance of the asteroid, $q$ is the heliocentric distance of the Earth, $\mu$ the mass of the Sun times the gravitational constant. Note that the denominator of the first fraction is $r ^ { 3 } = S ( \rho ) ^ { 3 / 2 }$ where

$$
S ( \rho ) = \rho ^ { 2 } + 2 q \rho \cos \epsilon + q ^ { 2 }
$$

is the same polynomial appearing in Section 8.1, with $\mathbf { q } = q \hat { \mathbf { q } }$ and $\cos \epsilon =$ ${ \hat { \mathbf { q } } } \cdot { \hat { \boldsymbol { \rho } } }$ . Equation (9.4) is a geometric relation among $q$ , $r$ , and $\rho$ and it is often called the geometric equation in the orbit determination literature.

We compute the components of $\ddot { \rho }$ along $\hat { \bf n }$ and $\hat { \bf v }$ : using ${ \hat { \pmb { \rho } } } \cdot { \hat { \mathbf { n } } } = 0$ we have

$$
{ \ddot { \rho } } \cdot { \hat { \mathbf { n } } } = { \frac { - \mu ~ \mathbf { q } \cdot { \hat { \mathbf { n } } } } { r ^ { 3 } } } + { \frac { \mu ~ \mathbf { q } \cdot { \hat { \mathbf { n } } } } { q ^ { 3 } } } = \rho \ \eta ^ { 2 } \ \kappa ,
$$

$$
\ddot { \pmb { \rho } } \cdot \hat { \bf v } = \frac { - \mu \mathbf { q } \cdot \hat { \bf v } } { r ^ { 3 } } + \frac { \mu \mathbf { q } \cdot \hat { \bf v } } { q ^ { 3 } } = \rho \dot { \eta } + 2 \dot { \rho } \eta .
$$

Let us define

$$
C = \frac { \eta ^ { 2 } \kappa q ^ { 3 } } { \mu \hat { \mathbf { q } } \cdot \hat { \mathbf { n } } } ;
$$

then, in the two-body approximation, eq. (9.5) takes the form

$$
1 - C \frac { \rho } { q } = \frac { q ^ { 3 } } { S ( \rho ) ^ { 3 / 2 } } ,
$$

which is often called the dynamical equation; in fact, it express only the $\hat { \bf n }$ component of the dynamics.

By substituting in (9.8) the possible values of $\rho$ obtained by eq. (9.4) and squaring, we obtain a polynomial equation of degree eight in $r$

$$
\begin{array} { r } { \begin{array} { r } { p ( r ) = C ^ { 2 } r ^ { 8 } - q ^ { 2 } \left( C ^ { 2 } + 2 C \cos \epsilon + 1 \right) r ^ { 6 } + 2 q ^ { 5 } ( C \cos \epsilon + 1 ) r ^ { 3 } - q ^ { 8 } = 0 , } \end{array} } \end{array}
$$

which is equivalent to eq. (9.8) if the left-hand side of (9.8) is positive, that is, only if $q / \rho > C$ .

From relation (9.6) we can compute the value of $\dot { \rho }$ from a value of $\rho$ that solves (9.5) and then define an orbit in attributable orbital elements.

# 9.3 The method of Gauss

For the times $t _ { i } , i = 1 , 2 , 3$ , let $\mathbf { r } _ { i } , \rho _ { i }$ denote the heliocentric and topocentric position of the body, respectively; ${ \bf q } _ { i }$ is the heliocentric position of the observer. The Gauss method uses three observations corresponding to the positions

$$
\mathbf { r } _ { i } = \pmb { \rho } _ { i } + \mathbf { q } _ { i } \ : \ : \ : i = 1 , 2 , 3
$$

at times $t _ { 1 } < t _ { 2 } < t _ { 3 }$ . We assume that $t _ { i } - t _ { j } , 1 \le i , j \le 3$ , is much smaller than the period of the orbit and we write $\mathcal { O } ( \Delta t )$ for the order of magnitude of the time differences. The coplanarity of the $\mathbf { r } _ { i }$ implies

$$
\lambda _ { 1 } \mathbf { r } _ { 1 } - \mathbf { r } _ { 2 } + \lambda _ { 3 } \mathbf { r } _ { 3 } = 0
$$

for some $\lambda _ { 1 } , \lambda _ { 3 } \in \mathbb { R }$ . The vector product of both sides of eq. (9.11) with $\mathbf { r } _ { 1 }$ and $\mathbf { r } _ { 3 }$ and the fact that the vectors $\mathbf { r } _ { i } \times \mathbf { r } _ { j }$ for $i \neq j$ have the same orientation as $\pmb { c } = \mathbf { r } _ { h } \times \dot { \mathbf { r } } _ { h }$ , for $h = 1 , 2 , 3$ (that is the angular momentum integral per unit mass at any of the three times) allows us to write

$$
\lambda _ { 1 } = { \frac { \mathbf { r } _ { 2 } \times \mathbf { r } _ { 3 } \cdot { \hat { c } } } { \mathbf { r } _ { 1 } \times \mathbf { r } _ { 3 } \cdot { \hat { c } } } } , \qquad \quad \lambda _ { 3 } = { \frac { \mathbf { r } _ { 1 } \times \mathbf { r } _ { 2 } \cdot { \hat { c } } } { \mathbf { r } _ { 1 } \times \mathbf { r } _ { 3 } \cdot { \hat { c } } } } \qquad { \mathrm { t r i a n g l e ~ a r e a ~ r a t i o s } } .
$$

From (9.10) and the scalar product of ${ \hat { \rho } } _ { 1 } \times { \hat { \rho } } _ { 3 }$ with eq. (9.11) we obtain

$$
\begin{array} { r } { \rho _ { 2 } \big [ \hat { \rho } _ { 1 } \times \hat { \rho } _ { 3 } \cdot \hat { \rho } _ { 2 } \big ] = \hat { \rho } _ { 1 } \times \hat { \rho } _ { 3 } \cdot \big [ \lambda _ { 1 } \mathbf { q } _ { 1 } - \mathbf { q } _ { 2 } + \lambda _ { 3 } \mathbf { q } _ { 3 } \big ] . } \end{array}
$$

The differences $\mathbf { r } _ { i } - \mathbf { r } _ { 2 } , i \ = \ 1 , 3$ , can be expanded in powers of $t _ { i j } ~ =$ $t _ { i } ~ - ~ t _ { j } ~ = ~ \mathcal { O } ( \Delta t )$ , e.g., by using the f and g series (Herrick 1971, Everhart and Pitkin 1983); thus $\mathbf { r } _ { i } = f _ { i } \mathbf { r } _ { 2 } + g _ { i } { \dot { \mathbf { r } } } _ { 2 }$ , with

$$
f _ { i } = 1 - \frac \mu 2 \frac { t _ { i 2 } ^ { 2 } } { r _ { 2 } ^ { 3 } } + \mathcal O ( \Delta t ^ { 3 } ) , \qquad g _ { i } = t _ { i 2 } \left( 1 - \frac \mu 6 \frac { t _ { i 2 } ^ { 2 } } { r _ { 2 } ^ { 3 } } \right) + \mathcal O ( \Delta t ^ { 4 } ) .
$$

Then $\mathbf { r } _ { i } \times \mathbf { r } _ { 2 } = - g _ { i } \pmb { c }$ , $\mathbf { r } _ { 1 } \times \mathbf { r } _ { 3 } = \left( f _ { 1 } g _ { 3 } - f _ { 3 } g _ { 1 } \right) c$ and

$$
\lambda _ { 1 } = \frac { g _ { 3 } } { f _ { 1 } g _ { 3 } - f _ { 3 } g _ { 1 } } , \qquad \lambda _ { 3 } = \frac { - g _ { 1 } } { f _ { 1 } g _ { 3 } - f _ { 3 } g _ { 1 } } ,
$$

$$
f _ { 1 } g _ { 3 } - f _ { 3 } g _ { 1 } = t _ { 3 1 } \left( 1 - \frac { \mu } { 6 } \frac { t _ { 3 1 } ^ { 2 } } { r _ { 2 } ^ { 3 } } \right) + \mathcal { O } ( \Delta t ^ { 4 } ) .
$$

Using (9.13) and (9.15) in (9.14) we obtain

$$
\begin{array} { r } { \lambda _ { 1 } = \cfrac { t _ { 3 2 } } { t _ { 3 1 } } \left[ 1 + \cfrac { \mu } { 6 r _ { 2 } ^ { 3 } } ( t _ { 3 1 } ^ { 2 } - t _ { 3 2 } ^ { 2 } ) \right] + \mathcal { O } ( \Delta t ^ { 3 } ) , } \\ { \lambda _ { 3 } = \cfrac { t _ { 2 1 } } { t _ { 3 1 } } \left[ 1 + \cfrac { \mu } { 6 r _ { 2 } ^ { 3 } } ( t _ { 3 1 } ^ { 2 } - t _ { 2 1 } ^ { 2 } ) \right] + \mathcal { O } ( \Delta t ^ { 3 } ) . } \end{array}
$$

Let $V = \hat { \rho } _ { 1 } \times \hat { \rho } _ { 2 } { \cdot } \hat { \rho } _ { 3 }$ . By substituting (9.16), (9.17) into (9.12), using relations $t _ { 3 1 } ^ { 2 } - t _ { 3 2 } ^ { 2 } = t _ { 2 1 } ( t _ { 3 1 } + t _ { 3 2 } )$ and $t _ { 3 1 } ^ { 2 } - t _ { 2 1 } ^ { 2 } = t _ { 3 2 } ( t _ { 3 1 } + t _ { 2 1 } )$ , we can write

$$
\begin{array} { r c l } { - V \rho _ { 2 } t _ { 3 1 } } & { = } & { \hat { \rho } _ { 1 } \times \hat { \rho } _ { 3 } \cdot ( t _ { 3 2 } \mathbf { q } _ { 1 } - t _ { 3 1 } \mathbf { q } _ { 2 } + t _ { 2 1 } \mathbf { q } _ { 3 } ) } \\ & & { + \hat { \rho } _ { 1 } \times \hat { \rho } _ { 3 } \cdot [ \cfrac { \mu } { 6 r _ { 2 } ^ { 3 } } [ t _ { 3 2 } t _ { 2 1 } ( t _ { 3 1 } + t _ { 3 2 } ) \mathbf { q } _ { 1 } + t _ { 3 2 } t _ { 2 1 } ( t _ { 3 1 } + t _ { 2 1 } ) \mathbf { c } _ { \phi }  } \\ & & {  + \mathcal { O } ( \Delta t ^ { 4 } ) . } \end{array}
$$

If the $\mathcal { O } ( \Delta t ^ { 4 } )$ terms are neglected, the coefficient of $1 / r _ { 2 } ^ { 3 }$ in (9.19) is

$$
B ( { \bf q } _ { 1 } , { \bf q } _ { 3 } ) = \frac { \mu } { 6 } t _ { 3 2 } t _ { 2 1 } \hat { \rho } _ { 1 } \times \hat { \rho } _ { 3 } \cdot \left[ \left( t _ { 3 1 } + t _ { 3 2 } \right) { \bf q } _ { 1 } + \left( t _ { 3 1 } + t _ { 2 1 } \right) { \bf q } _ { 3 } \right] .
$$

Then multiply (9.19) by $q _ { 2 } ^ { 3 } / B ( \mathbf { q } _ { 1 } , \mathbf { q } _ { 3 } )$ to obtain

$$
- \frac { V \rho _ { 2 } t _ { 3 1 } } { B ( { \bf q } _ { 1 } , { \bf q } _ { 3 } ) } q _ { 2 } ^ { 3 } = \frac { q _ { 2 } ^ { 3 } } { r _ { 2 } ^ { 3 } } + \frac { A ( { \bf q } _ { 1 } , { \bf q } _ { 2 } , { \bf q } _ { 3 } ) } { B ( { \bf q } _ { 1 } , { \bf q } _ { 3 } ) } ,
$$

where

$$
A \big ( { \bf q } _ { 1 } , { \bf q } _ { 2 } , { \bf q } _ { 3 } \big ) = q _ { 2 } ^ { 3 } \ \hat { \rho } _ { 1 } \times \hat { \rho } _ { 3 } \cdot [ t _ { 3 2 } { \bf q } _ { 1 } - t _ { 3 1 } { \bf q } _ { 2 } + t _ { 2 1 } { \bf q } _ { 3 } ] .
$$

Let

$$
C _ { 2 } = \frac { V t _ { 3 1 } q _ { 2 } ^ { 4 } } { B ( \mathbf { q } _ { 1 } , \mathbf { q } _ { 3 } ) } , \qquad \gamma _ { 2 } = - \frac { A ( \mathbf { q } _ { 1 } , \mathbf { q } _ { 2 } , \mathbf { q } _ { 3 } ) } { B ( \mathbf { q } _ { 1 } , \mathbf { q } _ { 3 } ) } ;
$$

then

$$
C _ { 2 } { \frac { \rho _ { 2 } } { q _ { 2 } } } = \gamma _ { 2 } - { \frac { q _ { 2 } ^ { 3 } } { r _ { 2 } ^ { 3 } } }
$$

is the dynamical equation of the Gauss method.

After the possible values for $r _ { 2 }$ have been found by (9.21) and the geometric equation $r _ { 2 } ^ { 2 } = \rho _ { 2 } ^ { 2 } + q _ { 2 } ^ { 2 } + 2 \rho _ { 2 } q _ { 2 } \cos \epsilon _ { 2 }$ , the velocity vector $\dot { \mathbf { r } } _ { 2 }$ can be computed by different methods, e.g., from the Gibbs formula (Herrick 1971, Chapter 8). Given the values of $\lambda _ { 1 } , \lambda _ { 3 }$ , from the scalar product of eq. (9.11) with ${ \hat { \rho } } _ { 1 } \times { \hat { \rho } } _ { 2 }$ we obtain a linear equation for $\rho _ { 3 }$ , from the scalar product with ${ \hat { \rho } } _ { 2 } \times { \hat { \rho } } _ { 3 }$ a linear equation for $\rho _ { 1 }$ ; from this we can compute $\mathbf { r } _ { 1 }$ and $\mathbf { r } _ { 3 }$ . The Gibbs method provides $\dot { \mathbf { r } } _ { 2 }$ in the form (Herrick 1971, Chapter 8)

$$
{ \dot { \mathbf { r } } } _ { 2 } = - d _ { 1 } { \mathbf { r } } _ { 1 } + d _ { 2 } { \mathbf { r } } _ { 2 } + d _ { 3 } { \mathbf { r } } _ { 3 }
$$

where

$$
\begin{array} { r c l } { { d _ { i } } } & { { = } } & { { G _ { i } + H _ { i } r _ { i } ^ { - 3 } , i = 1 , 2 , 3 , } } \\ { { } } & { { } } & { { } } \\ { { G _ { 1 } } } & { { = } } & { { \displaystyle \frac { t _ { 3 2 } ^ { 2 } } { t _ { 2 1 } t _ { 3 2 } t _ { 3 1 } } \ , G _ { 3 } = \frac { t _ { 2 1 } ^ { 2 } } { t _ { 2 1 } t _ { 3 2 } t _ { 3 1 } } \ , G _ { 2 } = G _ { 1 } - G _ { 3 } , } } \\ { { } } & { { } } & { { } } \\ { { H _ { 1 } } } & { { = } } & { { \mu t _ { 3 2 } / 1 2 \ , H _ { 3 } = \mu t _ { 2 1 } / 1 2 \ , H _ { 2 } = H _ { 1 } - H _ { 3 } . } } \end{array}
$$

When $\mathbf { r } _ { 2 }$ and $\dot { \mathbf { r } } _ { 2 }$ are available, they provide a set of initial conditions (at epoch $t _ { 2 } - \rho _ { 2 } / c ,$ ), from which we can compute two-body solutions $\mathbf { r } _ { 1 }$ , $\mathbf { r } _ { 3 }$ for the times $t _ { 1 } - \rho _ { 1 } / c , t _ { 3 } - \rho _ { 3 } / c$ (by using a two-body propagator, see Appendix A). Then the coefficients $\lambda _ { 1 }$ , $\lambda _ { 3 }$ are available from eq. (9.11), and eq. (9.12) provides an improved value of $\rho _ { 2 }$ , from which a new iteration could be started. This is just one of the many iterative methods described in the literature to improve the preliminary orbit, with the goal of obtaining smaller residuals with respect to the three observations.

As shown by Celletti and Pinzari (2005), each step in these iterative procedures used to improve the preliminary orbits (which they call a Gauss $\mathrm { \bf m a p ^ { 2 } }$ ) can be shown to increase the order in $\Delta t$ in the approximation of the exact solutions to the two-body equation of motion. Celletti and Pinzari (2006) have also shown that the iteration of a Gauss map can diverge when the solution of the degree 8 equation is far from the fixed point, outside of the convergence domain. Thus the Gauss map should be used with some caution, e.g., with a recovery procedure in case of divergence.

# 9.4 Topocentric Gauss–Laplace methods

The critical difference between the methods of Gauss and Laplace is the following. Gauss uses a truncation (to order $\mathcal { O } ( \Delta t ^ { 2 } ) )$ in the motion $\mathbf { r } ( t )$ of the asteroid but the positions of the observer (be it coincident with the center of the Earth or not) are used in their exact values. Laplace uses a truncation to the same order of the relative motion $\pmb { \rho } ( t )$ (see eq. (9.2) in Section 9.1), thus implicitly approximating the motion of the observer. In this section we examine the consequences of the difference between the techniques.

# Gauss–Laplace equivalence

To directly compare the two methods let us introduce in Gauss’ method the same approximation to order $\mathcal { O } ( \Delta t ^ { 2 } )$ in the motion of the center of the

Earth, which we assumed to coincide with the observer. Using the $f$ , $g$ series for the Earth we obtain

$$
\mathbf { q } _ { i } = \left( 1 - \frac { \mu } { 2 } \frac { t _ { i 2 } ^ { 2 } } { q _ { 2 } ^ { 3 } } \right) \mathbf { q } _ { 2 } + t _ { i 2 } \dot { \mathbf { q } } _ { 2 } + \frac { \mu } { 6 } \frac { t _ { i 2 } ^ { 3 } } { q _ { 2 } ^ { 3 } } \left[ \frac { 3 \left( \mathbf { q } _ { 2 } \cdot \dot { \mathbf { q } } _ { 2 } \right) \mathbf { q } _ { 2 } } { q _ { 2 } ^ { 2 } } - \dot { \mathbf { q } } _ { 2 } \right] + \mathcal { O } ( \Delta t ^ { 4 } ) .
$$

By substituting (9.23) in (9.19) we find

$$
B ( { \bf q } _ { 1 } , { \bf q } _ { 3 } ) = \frac { \mu } { 6 } t _ { 3 2 } t _ { 2 1 } \hat { \rho } _ { 1 } \times \hat { \rho } _ { 3 } \cdot \left[ 3 t _ { 3 1 } { \bf q } _ { 2 } + t _ { 3 1 } ( t _ { 3 2 } - t _ { 2 1 } ) \dot { \bf q } _ { 2 } + { \cal O } ( \Delta t ^ { 3 } ) \right] .
$$

If $t _ { 3 2 } - t _ { 2 1 } = t _ { 3 } + t _ { 1 } - 2 t _ { 2 } = 0$ , that is, the interpolation for $d ^ { 2 } / d t ^ { 2 }$ is done at the central value $t _ { 2 }$ , then

$$
B ( { \bf q } _ { 1 } , { \bf q } _ { 3 } ) = \frac { \mu } { 2 } t _ { 2 1 } t _ { 3 2 } t _ { 3 1 } \hat { \rho } _ { 1 } \times \hat { \rho } _ { 3 } \cdot { \bf q } _ { 2 } ( 1 + { \mathcal O } ( \Delta t ^ { 2 } ) ) ;
$$

else, if $t _ { 2 } \neq ( t _ { 1 } + t _ { 3 } ) / 2$ , the last factor is just $( 1 + \mathcal { O } ( \Delta t ) )$ . Substituting (9.23) in (9.24) we have

$$
\begin{array} { r c l } { { { \cal A } ( { \bf q } _ { 1 } , { \bf q } _ { 2 } , { \bf q } _ { 3 } ) } } & { { = } } & { { \displaystyle - \frac { \mu } { 2 } t _ { 2 1 } t _ { 3 2 } t _ { 3 1 } \hat { \rho } _ { 1 } \times \hat { \rho } _ { 3 } \cdot \{ { \bf q } _ { 2 }  } } \\ { { } } & { { } } & { { \displaystyle + \frac { 1 } { 3 } ( t _ { 2 1 } - t _ { 3 2 } ) [ \frac { 3 ( { \bf q } _ { 2 } \cdot \dot { \bf q } _ { 2 } ) { \bf q } _ { 2 } } { q _ { 2 } ^ { 2 } } - \dot { \bf q } _ { 2 } ] \} + { \mathcal O } ( \Delta t ^ { 5 } ) . } } \end{array}
$$

If, as above, $t _ { 3 2 } - t _ { 2 1 } = t _ { 3 } + t _ { 1 } - 2 t _ { 2 } = 0$ then

$$
A ( { \bf q } _ { 1 } , { \bf q } _ { 2 } , { \bf q } _ { 3 } ) = - \frac { \mu } { 2 } t _ { 2 1 } t _ { 3 2 } t _ { 3 1 } \hat { \pmb { \rho } } _ { 1 } \times \hat { \pmb { \rho } } _ { 3 } \cdot { \bf q } _ { 2 } ( 1 + { \cal O } ( \Delta t ^ { 2 } ) )
$$

and we can conclude from (9.20) that

$$
\gamma _ { 2 } = - \frac { A } { B } = 1 + \mathcal { O } ( \Delta t ^ { 2 } ) ;
$$

else, if $t _ { 2 } \neq ( t _ { 1 } + t _ { 3 } ) / 2$ , the last factor is just $( 1 + \mathcal { O } ( \Delta t ) )$ . For $V$ we use (9.1) to make a Taylor expansion of $\hat { \rho } _ { i }$ in $t _ { 2 }$ :

$$
\hat { \rho } _ { i } = \hat { \rho } _ { 2 } + t _ { i 2 } \eta \hat { \mathbf { v } } _ { 2 } + \frac { t _ { i 2 } ^ { 2 } } { 2 } ( - \eta ^ { 2 } \hat { \rho } _ { 2 } + \dot { \eta } \hat { \mathbf { v } } _ { 2 } + \kappa \eta ^ { 2 } \hat { \mathbf { n } } _ { 2 } ) + \mathcal { O } ( \Delta t ^ { 3 } ) .
$$

This implies that

$$
{ \bf { \nabla } } \times \hat { \rho } _ { 3 } \cdot \hat { \rho } _ { 2 } = \frac 1 2 \left[ t _ { 1 2 } \eta \hat { \bf { v } } _ { 2 } \times t _ { 3 2 } ^ { 2 } \kappa \eta ^ { 2 } \hat { \bf { n } } _ { 2 } - t _ { 3 2 } \eta \hat { \bf { v } } _ { 2 } \times t _ { 1 2 } ^ { 2 } \kappa \eta ^ { 2 } \hat { \bf { n } } _ { 2 } \right] \cdot \hat { \rho } _ { 2 } + { \cal O } ( \Delta t ^ { 4 }
$$

if $t _ { 2 } = ( t _ { 1 } + t _ { 3 } ) / 2$ then the term $\mathcal { O } ( \Delta t ^ { 4 } )$ vanishes and the remainder is $\mathcal { O } ( \Delta t ^ { 5 } )$ . Thus

$$
r = - \frac { \kappa \eta ^ { 3 } } { 2 } ( t _ { 1 2 } t _ { 3 2 } ^ { 2 } - t _ { 3 2 } t _ { 1 2 } ^ { 2 } ) \left( 1 + \mathcal { O } ( \Delta t ^ { 2 } ) \right) = \frac { \kappa \eta ^ { 3 } } { 2 } t _ { 2 1 } t _ { 3 2 } t _ { 3 1 } \left( 1 + \mathcal { O } ( \Delta t ^ { 2 } ) \right) ,
$$

$$
C _ { 2 } = \frac { V t _ { 3 1 } q _ { 2 } ^ { 4 } } { B } = \frac { \kappa \eta ^ { 3 } t _ { 3 1 } q _ { 2 } ^ { 4 } + \mathcal { O } ( \Delta t ^ { 3 } ) } { \mu \hat { \rho } _ { 1 } \times \hat { \rho } _ { 3 } \cdot \mathbf { q } _ { 2 } \left( 1 + \mathcal { O } ( \Delta t ) \right) } .
$$

In the denominator, ${ \hat { \rho } } _ { 1 } \times { \hat { \rho } } _ { 3 }$ computed to order $\Delta t ^ { 2 }$ is

$$
\hat { \rho } _ { 1 } \times \hat { \rho } _ { 3 } = t _ { 3 1 } \eta \hat { \bf n } _ { 2 } + \frac { t _ { 3 2 } ^ { 2 } - t _ { 1 2 } ^ { 2 } } { 2 } \left( \dot { \eta } \hat { \bf n } _ { 2 } - \kappa \eta ^ { 2 } \hat { \bf v } _ { 2 } \right) + \mathcal { O } ( \Delta t ^ { 3 } ) .
$$

As a conclusion, if $t _ { 3 2 } - t _ { 2 1 } = t _ { 3 } + t _ { 1 } - 2 t _ { 2 } = 0$ then

$$
C _ { 2 } = \frac { \kappa \eta ^ { 3 } t _ { 3 1 } q _ { 2 } ^ { 4 } + \mathcal { O } ( \Delta t ^ { 3 } ) } { \mu t _ { 3 1 } \eta q _ { 2 } \hat { \mathbf { q } } _ { 2 } \cdot \hat { \mathbf { n } } _ { 2 } + \mathcal { O } ( \Delta t ^ { 3 } ) } = \frac { \kappa \eta ^ { 2 } q _ { 2 } ^ { 3 } } { \mu \hat { \mathbf { q } } _ { 2 } \cdot \hat { \mathbf { n } } _ { 2 } } \left( 1 + \mathcal { O } ( \Delta t ^ { 2 } ) \right) ,
$$

otherwise the last factor is $( 1 + \mathcal { O } ( \Delta t ) )$ .

Thus, neglecting the difference between topocentric and geocentric observations, the coefficients of the two dynamical equations (9.8) and (9.21) are the same to order zero in $\Delta t$ , also to order one if $t _ { 2 }$ is the average time.

# Topocentric Laplace method

Now let us remove the approximation that the observer lies at the center of the Earth and introduce topocentric observations into the Laplace method. The center of mass of the Earth is at ${ \bf q } _ { \oplus }$ but the observer is at $\mathbf { q } = \mathbf { q } _ { \oplus } + \mathbf { P }$ . We derive the dynamical equation by also taking into account the acceleration contained in the geocentric position of the observer $\mathbf { P }$ , that is

$$
\frac { d ^ { 2 } \pmb { \rho } } { d t ^ { 2 } } = - \frac { \mu \mathbf { r } } { r ^ { 3 } } + \frac { \mu \mathbf { q } _ { \oplus } } { q _ { \oplus } ^ { 3 } } - \ddot { \bf P } .
$$

By scalar multiplication with $\hat { \bf n }$ , using eq. (9.1), we obtain

$$
{ \frac { d ^ { 2 } \rho } { d t ^ { 2 } } } \cdot { \hat { \mathbf { n } } } = \rho \eta ^ { 2 } \kappa = \mu \left[ q _ { \oplus } { \frac { { \hat { \mathbf { q } } } _ { \oplus } \cdot { \hat { \mathbf { n } } } } { q _ { \oplus } ^ { 3 } } } - q _ { \oplus } { \frac { { \hat { \mathbf { q } } } _ { \oplus } \cdot { \hat { \mathbf { n } } } } { r ^ { 3 } } } - P { \frac { { \hat { \mathbf { P } } } \cdot { \hat { \mathbf { n } } } } { r ^ { 3 } } } \right] - { \ddot { \mathbf { P } } } \cdot { \hat { \mathbf { n } } } .
$$

The term $P \hat { \mathbf { P } } \cdot \hat { \mathbf { n } } / r ^ { 3 }$ can be neglected. This approximation is legitimate because $P / q _ { \oplus } \leq 4 . 3 \times 1 0 ^ { - 5 }$ and the neglected term is smaller than the planetary perturbations. Thus we obtain the dynamical equation

$$
C \frac { \rho } { q _ { \oplus } } = \left( 1 - \Lambda _ { n } \right) - \frac { q _ { \oplus } ^ { 3 } } { r ^ { 3 } }
$$

where

$$
C = \frac { \eta ^ { 2 } \kappa q _ { \oplus } ^ { 3 } } { \mu \hat { \bf q } _ { \oplus } \cdot \hat { \bf n } } , ~ \Lambda _ { n } = \frac { q _ { \oplus } ^ { 2 } \ddot { \bf P } \cdot \hat { \bf n } } { \mu \hat { \bf q } _ { \oplus } \cdot \hat { \bf n } } = \frac { \ddot { \bf P } \cdot \hat { \bf n } } { \left( \mu / q _ { \oplus } ^ { 2 } \right) \hat { \bf q } _ { \oplus } \cdot \hat { \bf n } } .
$$

Note that $\Lambda _ { n }$ is singular only where $C$ is also singular. The analog of eq. (9.6), again neglecting $\mathcal { O } ( p / q _ { \oplus } )$ , is

$$
\rho \dot { \eta } + 2 \dot { \rho } \eta = \frac { \mu \hat { \bf q } _ { \oplus } \cdot \hat { \bf v } } { q _ { \oplus } ^ { 2 } } \left( 1 - \Lambda _ { v } - \frac { q _ { \oplus } ^ { 3 } } { r ^ { 3 } } \right) , \quad \Lambda _ { v } = \frac { q _ { \oplus } ^ { 2 } \ddot { \bf P } \cdot \hat { \bf v } } { \mu \hat { \bf q } _ { \oplus } \cdot \hat { \bf v } } .
$$

The important fact is that $\Lambda _ { n }$ and $\Lambda _ { v }$ are by no means small. The centripetal acceleration of the observer (towards the rotation axis of the Earth) has size $| \ddot { \mathbf { P } } | = \Omega _ { \oplus } ^ { 2 } R _ { \oplus } \cos \theta$ where $\Omega _ { \oplus }$ is the angular velocity of the Earth rotation, $R _ { \oplus }$ the radius of the Earth, and $\theta$ the latitude; the maximum of $| \ddot { \mathbf { P } } |$ is $\simeq 3 . 4$ $\mathrm { c m \thinspace s ^ { - 2 } }$ and occurs at the equator. The term $\mu / q _ { \oplus } ^ { 2 }$ in the denominator of $\Lambda _ { n }$ is the size of the heliocentric acceleration of the Earth, $\simeq 0 . 6 ~ \mathrm { c m s ^ { - 2 } }$ . Thus $\left| \Lambda _ { n } \right|$ can be $> 1$ , and the coefficient $1 - \Lambda _ { n }$ can be very different from 1 (it may even be negative). Without taking into account the observer geocentric acceleration, the classical Laplace method is not a good approximation, except when the observations of different nights are taken from the same station at the same sidereal time, so that the observer acceleration cancels out.

The common procedure for the Laplace method is to go back to the geocentric observation case by applying a topocentric correction, simulating the observations as they would appear to an observer placed at the center of the Earth. Some value of $\rho$ is assumed as a first guess, e.g., $\rho = 1$ AU (Leuschner 1913, page 15). If this value is approximately correct, by iterating the cycle (topocentric correction – Laplace determination of $\rho$ ) convergence is achieved. If the starting value is really wrong, e.g., if the object is undergoing a close approach to the Earth, the procedure may well diverge. These reliability problems discourage the use of the classical form of the Laplace method when processing a large data set, containing discoveries of different orbital classes and therefore spanning a wide range of distances.

The same argument applies to the algorithms used to improve Laplace preliminary orbits, e.g. (Leuschner 1913, Crawford et al. 1930). The difference with the Gauss map is that in the Laplace method the observations in the first approximation are treated as geocentric (or possibly corrected with an assumed distance), while in the Gauss method already the first approximation properly handles topocentric observations.

# Topocentric, Gauss–Laplace equivalence

When taking into account the displacement $\mathbf { P }$ , the Taylor expansion of ${ \bf q } _ { i } ( t )$ of eq. (9.23) is not applicable. We need to use

$$
{ \bf q } _ { i } = { \bf q } _ { 2 } + t _ { i 2 } \dot { { \bf q } } _ { 2 } + \frac { t _ { i 2 } ^ { 2 } } { 2 } \ddot { { \bf q } } _ { 2 } + \mathcal { O } ( \Delta t ^ { 3 } )
$$

where ${ \bf q } _ { 2 } ( t )$ and its derivatives contain also $\mathbf P ( t )$ . By using eq. (9.25) and assuming $t _ { 2 1 } = t _ { 3 2 }$ , (9.19) and (9.24) become

$$
\begin{array} { r l r } { B ( \mathbf { q } _ { 1 } , \mathbf { q } _ { 3 } ) } & { = } & { \displaystyle \frac { \mu \eta } { 2 } t _ { 2 1 } t _ { 3 2 } t _ { 3 1 } ^ { 2 } \hat { \mathbf { n } } _ { 2 } \cdot \mathbf { q } _ { 2 } + \mathcal { O } ( \Delta t ^ { 6 } ) , } \\ { A ( \mathbf { q } _ { 1 } , \mathbf { q } _ { 2 } , \mathbf { q } _ { 3 } ) } & { = } & { \displaystyle \frac { q _ { 2 } ^ { 3 } \eta } { 2 } t _ { 2 1 } t _ { 3 2 } t _ { 3 1 } ^ { 2 } \hat { \mathbf { n } } _ { 2 } \cdot \ddot { \mathbf { q } } _ { 2 } + \mathcal { O } ( \Delta t ^ { 6 } ) . } \end{array}
$$

Note that $\dot { \mathbf { q } } _ { 2 }$ does not appear in $A$ at this approximation level. Thus

$$
h _ { 0 } = - \frac { A } { B } = - \frac { q _ { 2 } ^ { 3 } \ \hat { \mathbf { n } } _ { 2 } \cdot \ddot { \mathbf { q } } _ { 2 } + \mathcal { O } ( \Delta t ^ { 2 } ) } { \mu \ \hat { \mathbf { n } } _ { 2 } \cdot \mathbf { q } _ { 2 } + \mathcal { O } ( \Delta t ^ { 2 } ) }
$$

and, neglecting once again $P / q _ { \oplus }$ terms,

$$
\begin{array} { r c l } { { h _ { 0 } } } & { { = } } & { { - \displaystyle \frac { q _ { 2 } ^ { 3 } \ \hat { \bf n } _ { 2 } \cdot \ddot { \bf q } _ { \oplus 2 } } { \mu \ \hat { \bf n } _ { 2 } \cdot \bf q } - \frac { q _ { 2 } ^ { 3 } \ \hat { \bf n } _ { 2 } \cdot \ddot { \bf P } _ { 2 } } { \mu \ \hat { \bf n } _ { 2 } \cdot \bf q } + { \cal O } ( \Delta t ^ { 2 } ) } } \\ { { } } & { { = } } & { { \displaystyle \frac { q _ { 2 } ^ { 3 } } { q _ { \oplus 2 } ^ { 3 } } - \frac { q _ { 2 } ^ { 3 } \ \hat { \bf n } _ { 2 } \cdot \ddot { \bf P } _ { 2 } } { \mu \ \hat { \bf n } _ { 2 } \cdot \bf q _ { 2 } } + { \cal O } ( \Delta t ^ { 2 } ) . } } \end{array}
$$

Finally

$$
\hat { \bf n } _ { 2 } \cdot { \bf q } _ { 2 } = q _ { 2 } \hat { \bf n } _ { 2 } \cdot \left( \frac { { \bf q } _ { \oplus 2 } } { q _ { 2 } } + \frac { { \bf P } _ { 2 } } { q _ { 2 } } \right) = q _ { 2 } \left( \hat { \bf n } _ { 2 } \cdot \hat { \bf q } _ { \oplus 2 } + { \cal O } \left( \frac { P _ { 2 } } { q _ { 2 } } \right) \right) ,
$$

then

$$
= 1 - \frac { q _ { \oplus 2 } ^ { 3 } \hat { \mathrm { \bf ~ n } } _ { 2 } \cdot \ddot { \mathrm { \bf ~ P } } _ { 2 } } { \mu \hat { \mathrm { \bf ~ n } } _ { 2 } \cdot \mathrm { \bf ~ q } _ { 2 } } + \mathcal { O } ( \Delta t ^ { 2 } ) + \mathcal { O } \left( \frac { P _ { 2 } } { q _ { 2 } } \right) = 1 - \Lambda _ { n 2 } + \mathcal { O } ( \Delta t ^ { 2 } ) + \mathcal { O } \left( \frac { P _ { 2 } } { q _ { 2 } } \right)
$$

where $\Lambda _ { n 2 }$ is the same quantity as $\Lambda _ { n }$ of eq. (9.27) computed at $t = t _ { 2 }$ .

The conclusion is that the Gauss method used with the heliocentric positions of the observer $\mathbf { q } _ { i } = \mathbf { q } _ { \oplus i } + \mathbf { P } _ { i }$ is equivalent to the topocentric Laplace method to lowest order in $\Delta t$ and neglecting the very small term $\mathcal { O } ( P _ { 2 } / q _ { 2 } )$ .

# Problems in the topocentric Laplace method

The Laplace method, with the geocentric approximation, is not really equivalent to the Gauss method: by using the observer positions in (9.19) and (9.24), the Gauss method naturally accounts for topocentric observations. Can we account for topocentric observations in the Laplace method (without iterations) by adding the term $\Lambda _ { n }$ from eq. (9.27)? The answer is contained in (Poincar´e 1906). To summarize the argument of Poincar´e, we can use plots showing the shape of the topocentric correction as a function of time.

Figure 9.1 shows the simulated path of an approaching asteroid as seen from an observing station. The darker portions of the curve indicate possible observations, the dotted ones are practically impossible, with an altitude $< 1 5 ^ { \circ }$ . The apparent motion of the asteroid from night to night cannot be approximated using parabolic motion segments fitted to a single night. For the geocentric path (continuous curve) the parabolic approximation to $\hat { \rho } ( t )$ , used by Laplace, would be applicable. Topocentric observations contain more information beyond the attributable; to reduce the observations to the geocenter by using the topocentric correction is a bad strategy.

![](images/738a97707a885c5617fa662e0498050baf8e6e8c3cd6417b340edfacacf3039c.jpg)  
Fig. 9.1. The path in the sky of the near-Earth asteroid (101955) $1 9 9 9 ~ \mathrm { R Q } _ { 3 6 }$ as it would have been seen in July 2005 if an observatory on Mauna Kea had been observing continuously. The solid portions of the curve are possible observations, the dotted ones are not possible (altitude $< ~ 1 5 ^ { \circ }$ ). The continuous curve shows observations from the geocenter. Coordinates are RA and DEC in radians. Reprinted from (Milani et al. 2008) with permission from Elsevier.

Poincar´e suggests computing $\Lambda _ { n } , \Lambda _ { v }$ by using, in place of $\ddot { \mathbf { P } } ( \bar { t } )$ , a value obtained by interpolating3 the positions $\mathbf { P } ( t _ { i } )$ at the times $t _ { i }$ of the observations (not limited to 3, one of the advantages of the Laplace method). Poincar´e gives no examples, but we have implemented this procedure and found that it works (see Section 8.3 and 8.6, where the same method is used). This method has not undergone a large-scale test, thus its practical advantages have not yet been assessed.

When the observations are performed from an artificial satellite (such as the Hubble Space Telescope or, in the future, from Gaia) the acceleration $\ddot { \mathbf { P } } \simeq 9 0 0 ~ \mathrm { c m s ^ { - 2 } }$ and the $\Lambda _ { n }$ and $\Lambda _ { v }$ coefficients can be up to $\simeq 1 5 0 0$ . A few hours of observations extending to several orbits produce multiple kinks as in (Marchi et al. 2004, Figure 1), containing important orbital information.

# 9.5 Number of solutions

Charlier gave a geometric interpretation of the occurrence of alternative solutions for a Laplace method preliminary orbit (Charlier 1910, Charlier 1911). He realized that (neglecting the errors in the measurements and in the model) this depends only on the position of $\boldsymbol { B }$ in a reference plane defined by the Sun, the Earth, and the body at a given time, and he was able to divide this plane into four connected components by two algebraic curves, separating regions with a unique solution from those with two solutions.

In this section we have shown that the Gauss method allows us to take into account topocentric observations in a natural way, and also the Laplace method can be modified to consider this effect. In both cases from the twobody dynamics we obtain an equation like (9.30), with the same algebraic structure as eq. (9.8) of the geocentric Laplace method, but it depends on the additional parameter $\gamma _ { 2 }$ , and reduces to eq. (9.8) only for $\gamma _ { 2 } = 1$ . Thus generically Charlier theory cannot be applied. We introduce a generalization of Charlier theory, providing a qualitative theory of alternative solutions also in the more realistic case of topocentric observations.

# The intersection problem

Assume that we have three observations of a celestial body whose motion is dominated by the gravitational attraction of the Sun.

We write $r , \rho , q , \epsilon$ for the values of the quantities corresponding to $r _ { i } , \rho _ { i } , q _ { i } , \epsilon _ { i }$ at the average time $t$ . Note that $q$ and $\mathbf { q } _ { i } , i = 1 , 2 , 3$ , can be obtained from planetary ephemerides and Earth rotation models, $\epsilon$ can be computed by interpolating the values of $\epsilon _ { i }$ (computed in turn from $\alpha _ { i } , \delta _ { i }$ , $\mathbf { q } _ { i }$ ), while $r , \rho$ are unknown because $r _ { i } , \rho _ { i }$ are also.

Actually the results we shall present do not depend on the value of $q$ . By choosing a different unit of length we could set $q = 1$ without loss of generality; we prefer to leave $q$ in all the formulae, since different units may be used in the applications of the theory to specific problems.

The geometry of the three bodies immediately gives the relation

$$
r ^ { 2 } = q ^ { 2 } + \rho ^ { 2 } + 2 q \rho \cos \epsilon \qquad \mathrm { g e o m e t r i c ~ e q u a t i o n . }
$$

Using the two-body dynamics we can deduce the following relation:

$$
\mathcal { C } \frac { \rho } { q } = \gamma - \frac { q ^ { 3 } } { r ^ { 3 } }  { \mathrm { ~ \qquad ~ } }  { \mathrm { d y n a m i c a l ~ e q u a t i o n } } ,
$$

where $\gamma , { \mathcal { C } } \in \mathbb { R }$ are constants computed from the observations, corresponding to $\gamma _ { 2 } , C _ { 2 }$ in the Gauss method, see (9.20) and to $1 - \Lambda _ { n } , C$ in the Laplace method, see eqs. (9.26) and (9.7), reducing to $1 , C$ in the geocentric approximation, see eq (9.8).

Equations (9.29) and (9.30) define surfaces of revolution around the axis $\hat { \mathbf { q } }$ passing through the center of the Sun and the observer. If the center of the Sun, the observer, and the observed body are not collinear at time $t$ , the observation line (also called the line of sight: a half-line from the observer position) and the axis $\hat { \mathbf { q } }$ define univocally a reference plane, which we shall use to study the intersection of these surfaces.

We introduce the intersection problem

$$
\left\{ \begin{array} { l l } { D ( r , \rho ) = ( q \gamma - \mathcal { C } \rho ) r ^ { 3 } - q ^ { 4 } = 0 } \\ { G ( r , \rho ) = r ^ { 2 } - q ^ { 2 } - \rho ^ { 2 } - 2 q \rho \cos { \epsilon } = 0 } \\ { r , \rho > 0 , } \end{array} \right.
$$

that is, given $( \gamma , \mathcal { C } , \epsilon ) \in \mathbb { R } ^ { 2 } \times [ 0 , \pi ]$ we search for pairs $( r , \rho )$ of strictly positive real numbers, solutions of (9.30) and (9.29). For given values of $( \gamma , \mathcal { C } , \epsilon )$ the solutions of (9.31) correspond to the intersections of the observation line with the planar algebraic curve defined by (9.30) in the reference plane (see Figure 9.2).

We can perform elimination of the variable $\rho$ by means of resultant theory (see Cox et al. 1996), thus from (9.31) we obtain the reduced problem

$$
\left\{ \begin{array} { l l } { P ( r ) = \tt r e s \left( D , G , \rho \right) = 0 } \\ { r > 0 } \end{array} \right.
$$

where ${ \tt r e s } ( D , G , \rho )$ stands for the resultant of the polynomials $D ( r , \rho )$ and $G ( r , \rho )$ with respect to the variable $\rho$ . The resultant computation gives

$$
P ( r ) = \mathcal { C } ^ { 2 } r ^ { 8 } - q ^ { 2 } ( \mathcal { C } ^ { 2 } + 2 \mathcal { C } \gamma \cos \epsilon + \gamma ^ { 2 } ) r ^ { 6 } + 2 q ^ { 5 } ( \mathcal { C } \cos \epsilon + \gamma ) r ^ { 3 } - q ^ { 8 } .
$$

The reduced formulation (9.32) is suitable to obtain an upper bound for the maximum number of solutions, in fact $P ( r )$ has only four monomials, thus by Descartes’ sign rule there are at most three positive roots of $P ( r )$ , counted with multiplicity. Note that, if $r = r$ is a component of a solution of (9.31), from (9.30) we obtain a unique value $\rho$ for the other component and, conversely, from a value $\rho$ of $\rho$ we obtain a unique $r$ ; there are no more than three values of $\rho$ that are components of the solutions of (9.31).

![](images/011d5ce542e7e31461d2e65d2c7e01dc88071173c4abdbff1bc8e88321c45bd7.jpg)  
Fig. 9.2. Geometric view of the intersection problem: given a direction of observation, the solutions are the intersections with level curves of $c$ .

We define as a spurious solution of (9.32) a positive root $r$ of $P ( r )$ that is not a component of a solution $( \bar { r } , \bar { \rho } )$ of (9.31) for any $\bar { \rho } > 0$ , that is it gives a non-positive $\rho$ through the dynamical equation (9.30).

The question is how many solutions are possible for the intersection problem, thus also for the preliminary orbit problem; from each solution of (9.31) a full set of orbital elements can be determined, in fact knowledge of the topocentric distance $\rho$ allows us to compute the corresponding value of $\dot { \rho }$ . In case of alternative solutions all of them should be used as a first guess for the differential corrections, not to miss the right solution.

# 9.6 Charlier theory

The Charlier theory describes the occurrence of alternative solutions in the problem defined by eqs. (9.8) and (9.4), with geocentric observations. Nevertheless, if we interpret $\rho$ and $q$ as the geocentric distance of the observed body and the heliocentric distance of the center of the Earth, then eq. (9.30) with $\gamma = 1$ corresponds to (9.8) and eq. (9.29) corresponds to (9.4). Therefore we shall discuss Charlier theory by studying the alternative solutions of (9.31) with $\gamma = 1$ , and we shall see that in this case the solutions of (9.31) can be at most two. The discussion presented in this section is based on (Plummer 1918).

Charlier was the first to realize that the condition for the appearance of another solution simply depends on the position of the observed body. We stress that it assumes that the two-body model for the orbit of the observed body is exact and neglects the observation and interpolation errors in the parameters ${ \mathcal { C } } , \epsilon$ . The previous hypotheses imply the following assumption:

the parameters ${ \mathcal { C } } , \epsilon$ are such that the corresponding intersection problem with $\gamma = 1$ admits at least one solution.

In real astronomical applications (9.34) may not be fulfilled and the intersection problem may have no solution. A reason for that is the presence of errors in the observations; these affect mostly the computation of $\zeta$ . However we observe that condition (9.34) may hold also taking into account these errors, therefore it is more interesting for the applications.

For each choice of ${ \mathcal { C } } , \epsilon$ the polynomial $P ( r )$ in (9.32) has three changes of sign in the sequence of its coefficients; the coefficient of $r ^ { 3 }$ is positive because from (9.30) and (9.29) we have

$$
\mathcal { C } \cos \epsilon + 1 = \frac { 1 } { 2 \rho ^ { 2 } r ^ { 3 } } \left[ ( r ^ { 3 } - q ^ { 3 } ) ( r ^ { 2 } - q ^ { 2 } ) + \rho ^ { 2 } ( r ^ { 3 } + q ^ { 3 } ) \right] > 0 \ ,
$$

thus the positive roots of $P ( r )$ can be up to three. As $P ( q ) = 0$ , there is always the physically meaningless solution corresponding to the center of the Earth, in fact, from the dynamical equation, $r = q$ corresponds to $\rho = 0$ . Using (9.34), Descartes’ sign rule and the relations

$$
P ( 0 ) = - q ^ { 8 } < 0 ; \qquad \operatorname * { l i m } _ { r  + \infty } P ( r ) = + \infty ,
$$

we conclude that there are always three positive roots of $P ( r )$ , counted with multiplicity. By (9.34) at least one of the other two positive roots $r _ { 1 } , r _ { 2 }$ is not spurious; if either $r _ { 1 }$ or $r _ { 2 }$ is spurious the solution of (9.31) is unique, otherwise we have two non-spurious solutions.

To detect the cases with two solutions we write $P ( r ) = ( r - q ) P _ { 1 } ( r )$ , with

$$
\begin{array} { l c l } { { P _ { 1 } ( r ) } } & { { = } } & { { \displaystyle \mathcal { C } ^ { 2 } r ^ { 6 } ( r + q ) + ( r ^ { 2 } + q r + q ^ { 2 } ) \left[ q ^ { 5 } - ( 2 \mathcal { C } \cos \epsilon + 1 ) q ^ { 2 } r ^ { 3 } \right] } } \\ { { P _ { 1 } ( q ) } } & { { = } } & { { \displaystyle 2 q ^ { 7 } \mathcal { C } \left( \mathcal { C } - 3 \cos \epsilon \right) . } } \end{array}
$$

From $P _ { 1 } ( 0 ) = q ^ { 7 } > 0$ and $\begin{array} { r } { \operatorname* { l i m } _ { r  + \infty } P _ { 1 } ( r ) = + \infty } \end{array}$ , it follows that if $P _ { 1 } ( q ) < 0$ then $r _ { 1 } < q < r _ { 2 }$ , thus one root of $P _ { 1 } ( r )$ is spurious. Else, if $P _ { 1 } ( q ) > 0$ either $r _ { 1 } , r _ { 2 } \ < \ q$ or $r _ { 1 } , r _ { 2 } \ > \ q$ , and because of (9.34) both roots give meaningful solutions of (9.31). If $P _ { 1 } ( q ) = 0$ there is only one non-spurious root of $P ( r )$ .

The dynamical equation gives us an expression of $c$ as an algebraic function either in bipolar coordinates $\mathcal { C } ( r , \rho )$ or in geocentric polar coordinates $\mathcal { C } ( \rho , \epsilon )$ ; we shall plot the figures in a full plane, with $- \pi < \epsilon \leq \pi$ , but the situation is symmetric with respect to the $\hat { \mathbf { q } }$ axis. Thus we can define two curves in this plane: the zero circle ${ \mathcal C } ( \rho , \epsilon ) = 0$ and the limiting curve $\mathcal { C } ( \rho , \epsilon ) - 3 \cos \epsilon = 0$ , where

![](images/f48d962163f9d6938c86122a635bc176317f29d940a14fe605b3e5893f01e09d.jpg)  
Fig. 9.3. The limiting curve and the zero circle divide the reference plane into four connected regions, two with a unique solution of (9.31) and two with two solutions (shaded in this figure). The singular curve (dotted) divides the regions with two solutions into two parts, with one solution each. The Sun and the Earth are labeled with $S$ and $E$ , respectively. We use heliocentric rectangular coordinates, and astronomical units (AU) for both axes. Reprinted from Gronchi (2009) with permission from Springer.

$$
\mathcal { C } ( \rho , \psi ) = \frac { q } { \rho } \left[ 1 - \frac { q ^ { 3 } } { r ^ { 3 } } \right] , ~ r = \sqrt { \rho ^ { 2 } + q ^ { 2 } + 2 q \rho \cos \psi } .
$$

The limiting curve has a loop inside the zero circle and two unlimited branches with $r > q$ . By the previous discussion the limiting curve and the zero circle divide the reference plane, containing the center of the Sun, the observer, and the observed body at time $t$ , into four connected components (see Figure 9.3), separating regions with a different number of solutions of the orbit determination problem. More precisely, given the position $( \rho , \epsilon )$ of a celestial body in the reference plane at time $\bar { t }$ , eq. (9.30) with $\gamma = 1$ defines a value $\mathcal { C }$ such that the intersection problem defined by $c$ , $\epsilon$ and $\gamma = 1$ has the solution $( r , \rho ) = ( \sqrt { \rho ^ { 2 } + q ^ { 2 } + 2 q \rho \cos \epsilon } , \rho )$ and, if the body is situated in a region with two solutions, we can find the second solution in the same region as the first. Using heliocentric polar coordinates $( r , \phi )$ , with $\rho ^ { 2 } = r ^ { 2 } + q ^ { 2 } - 2 q r \cos \epsilon$ , the limiting curve is given by

$$
4 - 3 { \frac { r } { q } } \cos \epsilon = { \frac { q ^ { 3 } } { r ^ { 3 } } }
$$

and, in heliocentric rectangular coordinates $( x , y ) = ( r \cos \phi , r \sin \phi )$ , by

$$
4 - 3 { \frac { x } { q } } = { \frac { q ^ { 3 } } { \left( x ^ { 2 } + y ^ { 2 } \right) ^ { 3 / 2 } } } .
$$

Figure 9.3 shows that, when the celestial body has been observed close to the opposition direction, the solution of the Laplace method of preliminary orbit determination is unique. The two tangents to the limiting curve correspond to ta $\mathrm { . n } \epsilon _ { 0 } = \mathrm { 2 }$ , thus only for $\lvert \epsilon \rvert \geq \simeq 6 3 . 4 3 ^ { \circ }$ could there be a double solution.

# 9.7 Generalization of the Charlier theory

In this section we consider the intersection problem (9.31) for a generic $\gamma \in \mathbb R$ . Given a value of $\gamma$ and the position $( \rho , \epsilon )$ of the observed body in the reference plane, in topocentric polar coordinates, eq. (9.30) defines a value of $\mathcal { C }$ such that the intersection problem defined by $( \gamma , \mathcal { C } , \epsilon )$ has the solution $( r , \rho ) = ( \sqrt { \rho ^ { 2 } + q ^ { 2 } + 2 q \rho \cos \epsilon } , \rho )$ . Therefore in the following we shall speak about the intersection problem corresponding to, or related to, $a$ fixed $\gamma \in \mathbb { R }$ and to a point of the reference plane. We introduce the following assumption, that generalizes (9.34):

the parameters $\gamma , \mathcal { C } , \epsilon$ are such that the corresponding intersection problem admits at least one solution.

Generically $r = q$ is not a root of $P ( r )$ , in fact

$$
P ( q ) = q ^ { 8 } \left( 1 - \gamma \right) \left( 2 \mathcal { C } \cos \epsilon - ( 1 - \gamma ) \right) ,
$$

thus we cannot follow the steps of Section 9.6 to define the limiting curve. From the dynamical equation we define the function

$$
\mathrm { C } ^ { ( \gamma ) } ( x , y ) = \frac { q } { \rho } \left[ \gamma - \frac { q ^ { 3 } } { r ^ { 3 } } \right] ,
$$

where $\rho = \sqrt { ( q - x ) ^ { 2 } + y ^ { 2 } }$ and $r = \sqrt { x ^ { 2 } + y ^ { 2 } }$ .

If $\gamma > 0$ we can also define the zero circle as the set of points such that $\mathrm { C } ^ { ( \gamma ) } ( x , y )$ , that is $r = r _ { 0 } = q / \sqrt [ 3 ] { \gamma }$ .

# The topology of the level curves

For each $\gamma \in \mathbb R$

$$
\operatorname* { l i m } _ { \| ( x , y ) \|  + \infty } \mathrm { C } ^ { ( \gamma ) } ( x , y ) = 0 , \qquad \operatorname* { l i m } _ { ( x , y )  ( 0 , 0 ) } \mathrm { C } ^ { ( \gamma ) } ( x , y ) = - \infty ,
$$

$$
\operatorname* { l i m } _ { ( x , y ) \to ( q , 0 ) } \mathrm { C } ^ { ( \gamma ) } ( x , y ) \left\{ \begin{array} { l l } { { = - \infty \ } } & { { \mathrm { f o r ~ } \gamma < 1 } } \\ { { \mathrm { ~ d o e s ~ n o t ~ e x i s t ~ } } } & { { \mathrm { f o r ~ } \gamma = 1 } } \\ { { = + \infty \ } } & { { \mathrm { f o r ~ } \gamma > 1 . } } \end{array} \right.
$$

The stationary points of $\mathrm { C } ^ { ( \gamma ) } ( x , y )$ have $y = 0$ and depend on $\gamma$ as follows:

for $\gamma \le 0$ there is only one saddle point, with $x \in ( 0 , \textstyle { \frac { 3 } { 4 } } q ]$ ; for $0 < \gamma < 1$ there are three points: one saddle point inside the zero circle, one saddle and one maximum point outside. $\bullet$ for $\gamma \geq 1$ there is a unique saddle point with $x < - r _ { 0 } = - q / \sqrt [ 3 ] { \gamma }$ .

This result is useful to understand the topological changes in the level curves of $\operatorname { C } ^ { ( \gamma ) } ( x , y )$ , see Figure 9.4 for all the significantly different cases, i.e. $\gamma \leq 0$ , $0 < \gamma < 1$ , $\gamma = 1$ , and $\gamma > 1$ .

Table 9.1. Number of solutions at opposition.   

<table><tr><td># solutions</td><td>0</td><td>1</td><td></td></tr><tr><td>Y≤O</td><td>C≥0</td><td>C&lt;0</td><td></td></tr><tr><td>0&lt;γ&lt;1</td><td>C &gt;Cmax</td><td>C≤o</td><td>0&lt;c&#x27;≤Cmax</td></tr><tr><td>γ=1</td><td>C≤0orC≥3</td><td>30&lt;C&lt;3</td><td></td></tr><tr><td>γ&gt;1</td><td>c≤0</td><td>C&gt;0</td><td></td></tr></table>

In Table 9.1, for each value of $\gamma$ , we describe the change with $c$ in the number of solutions, when we observe in the opposition direction. $\mathcal { C } _ { m a x }$ is the maximum value of $\operatorname { C } ^ { ( \gamma ) } ( x , y )$ .

# The singular curve

The function $\operatorname { C } ^ { ( \gamma ) } ( x , y )$ in topocentric polar coordinates $( \rho , \epsilon )$ is given by

$$
\mathrm { C } ^ { ( \gamma ) } ( \rho , \epsilon ) = \frac { q } { \rho } \left[ \gamma - \frac { q ^ { 3 } } { r ^ { 3 } } \right] , \quad \mathrm { ~ w h e r e ~ } \quad r = r ( \rho , \epsilon ) = \sqrt { \rho ^ { 2 } + q ^ { 2 } + 2 q \rho \cos { \Omega } }
$$

As the Jacobian of the transformation $( \rho , \epsilon ) \mapsto ( x , y ) = ( q + \rho \cos \epsilon , \rho , \sin \epsilon )$ has determinant equal to $\rho$ , the stationary points of $\mathrm { C } ^ { ( \gamma ) } ( \rho , \epsilon )$ just correspond

![](images/18cf4c8e96a2c529b364a126553ef4f123837e11fd97f0dce393ee48cb796c7b.jpg)  
Fig. 9.4. The level curves of $\mathrm { C } ^ { ( \gamma ) } \left( x , y \right)$ . The Sun and the Earth are denoted by $\odot$ and $\oplus$ , respectively. The saddle points are marked with $\times$ and the maximum point (present only for $0 < \gamma < 1$ ) with $^ +$ . Top left: $\gamma = - 0 . 5$ . Top right: $\gamma = 0 . 8$ . Bottom left: $\gamma = 1$ . Bottom right: $\gamma = 1 . 5$ . Reprinted from Gronchi (2009) with permission from Springer.

to those of $\mathrm { C } ^ { ( \gamma ) } ( x , y )$ . For a given $\gamma \in \mathbb { R }$ we define

$$
F ( \mathcal { C } , \rho , \epsilon ) = \mathcal { C } \frac { \rho } { q } - \gamma + \frac { q ^ { 3 } } { r ^ { 3 } ( \rho , \epsilon ) } .
$$

The tangency points between the level lines of $\mathrm { C } ^ { ( \gamma ) } ( \rho , \epsilon )$ and the observation lines fulfill the equations

$$
F ( \mathcal { C } , \rho , \epsilon ) = F _ { \rho } ( \mathcal { C } , \rho , \epsilon ) = 0
$$

for each non-stationary value $\zeta$ of $\mathrm { C } ^ { ( \gamma ) } ( \rho , \epsilon )$ , where

$$
F _ { \rho } ( \mathcal { C } , \rho , \epsilon ) = \frac { \mathcal { C } } { q } - 3 \frac { q ^ { 3 } } { r ^ { 5 } } ( \rho + q \cos { \epsilon } )
$$

is the derivative of $F ( \mathcal { C } , \rho , \epsilon )$ with respect to $\rho$ . We can eliminate the dependence on $\mathcal { C }$ in (9.38) by considering the difference

$$
F ( \mathcal { C } , \rho , \epsilon ) - \rho F _ { \rho } ( \mathcal { C } , \rho , \epsilon ) = - \gamma + \frac { q ^ { 3 } } { r ^ { 3 } } + 3 q ^ { 3 } \frac { \rho } { r ^ { 5 } } ( \rho + q \cos \epsilon ) \ ,
$$

with $r = \sqrt { \rho ^ { 2 } + q ^ { 2 } + 2 \rho q \cos \epsilon }$ . The function $r ^ { 5 } ( F - \rho F _ { \rho } )$ in heliocentric rectangular coordinates becomes

$$
\mathcal { G } ( x , y ) = - \gamma r ^ { 5 } + q ^ { 3 } ( 4 r ^ { 2 } - 3 q x ) , r = \sqrt { x ^ { 2 } + y ^ { 2 } } .
$$

We define the singular curve as the set

$$
S = \{ ( x , y ) : \mathcal { G } ( x , y ) = 0 \} .
$$

Note that $\boldsymbol { S }$ contains all the points whose polar coordinates fulfill (9.38) plus $( x , y ) = ( 0 , 0 )$ . The shape of the singular curve for different values of $\gamma$ , see Figure 9.5, is as follows. If $\gamma \neq 1$ , the singular curve $\boldsymbol { S }$ contains a number of components, each a regular and simply closed curve:

if $\gamma \leq 0$ it has a unique component, which is convex;   
if $0 < \gamma < 1$ it has two components inside and outside the zero circle;   
if $\gamma > 1$ it has a unique non-convex component intersecting the zero circle;   
$\bullet$ if $\gamma = 1$ it has a self-intersection point at the observer position $( q , 0 )$ .

# An even or an odd number of solutions

For $\gamma \leq 0$ , eq. (9.30) has no real solution if $\mathcal { C } \geq 0$ . Let us consider the polynomial $P ( r )$ defined in (9.33). If $\textit { c } < 0$ , from $P ( 0 ) < 0$ and $\begin{array} { r } { \operatorname* { l i m } _ { r \to + \infty } P ( r ) = } \end{array}$ $+ \infty$ the number of roots of $P ( r )$ in the interval $( 0 , + \infty )$ , counted with their multiplicity, is odd and none of these roots is spurious.

Assuming $\gamma > 0$ , let $r _ { 0 } = q / \sqrt [ 3 ] { \gamma }$ be the radius of the zero circle; we have

$$
P ( r _ { 0 } ) = \frac { \mathcal { C } ^ { 2 } q ^ { 8 } } { \gamma ^ { 8 / 3 } } ( 1 - \gamma ^ { 2 / 3 } ) .
$$

If $0 < \gamma < 1$ and $\mathcal { C } \neq 0$ , from $P ( 0 ) < 0 < P ( r _ { 0 } )$ and $\begin{array} { r } { \operatorname* { l i m } _ { r \to + \infty } P ( r ) = + \infty } \end{array}$ we obtain that in the interval $( 0 , r _ { 0 } )$ the number of roots of $P ( r )$ is odd, while in $( r _ { 0 } , + \infty )$ it is even. By relation (9.30) the roots of $P ( r )$ in $( 0 , r _ { 0 } )$ are spurious iff $\mathcal { C } > 0$ , those in $( r _ { 0 } , + \infty )$ are spurious iff $c < 0$ . For $\mathcal { C } = 0$ the intersection problem (9.31) reduces to $r = r _ { 0 }$ , with $\rho$ deduced from the geometric equation, and this solution is not spurious.

![](images/fd76ed96c546efb6e551076efcfabb6841772bdfa131a07508352cd0aeca65f9.jpg)  
Fig. 9.5. Singular curve (continuous line) and zero circle (dotted). Top left: $\gamma = - 0 . 5$ . Top right: $\gamma = 0 . 8$ . Bottom left: $\gamma = 1$ . Bottom right: $\gamma = 1 . 1$ . Note that the zero circle does not exist for $\gamma \leq 0$ . Reprinted from Gronchi (2009) with permission from Springer.

If $\gamma > 1$ and $\mathcal { C } \neq 0$ , from $P ( 0 ) , P ( r _ { 0 } ) < 0$ and $\begin{array} { r } { \operatorname* { l i m } _ { r \to + \infty } P ( r ) = + \infty } \end{array}$ we obtain that in the interval $( 0 , r _ { 0 } )$ the number of roots of $P ( r )$ is even, while in $( r _ { 0 } , + \infty )$ it is odd. As in the previous case, the roots of $P ( r )$ in $( 0 , r _ { 0 } )$ are spurious iff $\mathcal { C } > 0$ , those in $( r _ { 0 } , + \infty )$ iff $\textit { c } < 0$ . Since for $\gamma > 1$ we have $r _ { 0 } < q$ , there is no solution for $\mathcal { C } = 0$ if $\cos \epsilon < \sqrt { q ^ { 2 } - r _ { 0 } ^ { 2 } } / q$ , while if $\cos \epsilon \geq$ $\sqrt { q ^ { 2 } - r _ { 0 } ^ { 2 } } / q$ the solutions are $( r , \rho ) = \left( r _ { 0 } , - q \cos \epsilon \pm \sqrt { q ^ { 2 } \cos ^ { 2 } \epsilon - ( q ^ { 2 } - r _ { 0 } ^ { 2 } ) } \right)$ . We give a summary of this discussion in Table 9.2.

The bound on the solutions of the reduced problem implies that the solutions of the intersection problem cannot be more than three. In particular, for $( \gamma , \mathcal { C } , \epsilon )$ fulfilling (9.36) with $\gamma \neq 1$ , when the number of solutions of (9.31) is even, they are two, when it is odd they are either one or three.

Table 9.2. The table shows, for each value of $\gamma \neq 1$ , the values of $\boldsymbol { \mathscr { C } }$ allowing an even or an odd number of solutions of (9.31).   

<table><tr><td></td><td>even odd</td></tr><tr><td>Y≤0 c≥o</td><td>C&lt;0</td></tr><tr><td>0&lt;γ&lt;1</td><td>c&gt;0</td></tr><tr><td>γ&gt;1 c≤o</td><td>C≤0 c&gt;0</td></tr></table>

# The limiting curve

Indeed the assertion by Charlier that the occurrence of alternative solutions depends only on the position of the observed body cannot be generalized to the Gauss method of preliminary orbit determination or to the modified Laplace method, with topocentric observations; in fact the position of the body defines different intersection problems for different $\gamma \in \mathbb { R }$ . Actually for each fixed value of $\gamma \in \mathbb { R }$ we shall divide the reference plane into connected components such that, if a solution of an intersection problem lies in one of these components, then we know how many solutions occur in that problem, and all of them lie in the same component.

In the applications of this theory the parameters $\gamma , \mathcal { C } , \epsilon$ are computed from the three observations, thus there is no guarantee that assumption (9.36) holds. The failure of this assumption can occur for different reasons: mostly due to the unavoidable errors in the observations, and to the error made in considering three observations of different objects as belonging to the same.

For $\gamma \neq 1$ we define, with $r = \sqrt { x ^ { 2 } + y ^ { 2 } }$ , the sets

$$
\mathcal { D } _ { 2 } ( \gamma ) = \left\{ \begin{array} { l l } { \emptyset } & { \mathrm { ~ i f ~ } \gamma \leq 0 } \\ { \{ ( x , y ) : r > r _ { 0 } \} } & { \mathrm { ~ i f ~ } 0 < \gamma < 1 } \\ { \{ ( x , y ) : r \leq r _ { 0 } \} } & { \mathrm { ~ i f ~ } \gamma > 1 } \end{array} \right.
$$

and ${ \mathcal { D } } ( \gamma ) = \mathbb { R } ^ { \smash { \gamma } } \setminus \left( { \mathcal { D } } _ { 2 } ( \gamma ) \cup \{ ( q , 0 ) \} \right)$ . To use a simpler notation, we shall suppress the dependence on $\gamma$ in $\mathcal { D } ( \gamma ) , D _ { 2 } ( \gamma )$ . For a fixed $\gamma \neq 1$ , if we consider a point in $\mathcal { D } _ { 2 }$ and if (9.36) holds for the parameters $( \gamma , \mathcal { C } , \epsilon )$ of the corresponding intersection problem, then there are two solutions of (9.31), both contained in $\mathcal { D } _ { 2 }$ . We shall also say that $\mathcal { D } _ { 2 }$ is a region with two solutions of (9.31). Our aim is to divide the complementary set $\mathcal { D }$ into two connected regions, each with the same number of solutions of (9.31). Let ${ \mathfrak { S } } = { \mathcal { S } } \cap { \mathcal { D } }$ be the portion of the singular curve $\boldsymbol { S }$ contained in $\mathcal { D }$ . Note that $\mathfrak { S }$ is connected. In $\mathcal { D }$ the solutions of (9.31) are one or three, and the solutions lying on the singular curve have intersection multiplicity $\geq 2$ , therefore for each point $\mathrm { P } \in { \mathfrak { S } }$ the related intersection problem must have three solutions.

![](images/48a185909ef682b502e603a004ca1bb050b3a5468f10b9e91c38bc3164c1d5df.jpg)  
Fig. 9.6. We sketch the tangent intersection between an observation line and a level curve of $\mathrm { C } ^ { ( \gamma ) } \left( x , y \right)$ , giving rise to a residual point in the region $_ { \mathcal { D } }$ with an odd number of solutions. Case (a) is a generic situation, with $\mathrm { P }$ corresponding to a solution with multiplicity two and $\mathrm { P ^ { \prime } }$ corresponding to the third solution (the residual point). Case (b) is non-generic: $\mathrm { P }$ is a selfresidual point, with intersection multiplicity equal to three. Reprinted from Gronchi (2009) with permission from Springer.

There are two cases, sketched in Figure 9.6 with labels (a), (b). Case (a) is the generic situation: we have $F _ { \rho \rho } ( \mathcal { C } , \bar { \rho } , \psi ) \neq 0$ for $( \bar { \rho } , \psi )$ corresponding to P and $c$ such that $F ( { \mathcal { C } } , { \bar { \rho } } , \psi ) = 0$ , thus $\mathrm { P }$ corresponds to a solution of (9.31) with multiplicity two and there is another point $\mathrm { P } ^ { \prime } \neq \mathrm { P }$ corresponding to the third solution of (9.31). In case (b) we have $F _ { \rho \rho } ( \mathcal { C } , \bar { \rho } , \psi ) = 0$ , so that in $\mathrm { P }$ the observation line is tangent to both the singular curve and to the level curve $\mathrm { C } ^ { ( \gamma ) } ( x , y ) = \mathcal { C }$ , and it corresponds to a solution with multiplicity three of the related intersection problem. For $\gamma \neq 1$ there are only two points of the reference plane, outside the $x$ -axis, corresponding to solutions with multiplicity three (Gronchi 2009).

Let us fix $\gamma \neq 1$ and let $( \bar { \rho } , \psi )$ correspond to a point $\mathrm { ~ \textbf ~ { ~ P ~ } ~ } \in \mathrm { ~ \mathfrak ~ { ~ S ~ } ~ }$ . If $F _ { \rho \rho } ( \mathcal { C } , \bar { \rho } , \psi ) \neq 0$ , we call the residual point related to P the point $\mathrm { P } ^ { \prime } \neq \mathrm { P }$ lying on the same observation line and the same level curve of $\operatorname { C } ^ { ( \gamma ) } ( x , y )$ (see Figure 9.6 (a)). If $F _ { \rho \rho } ( \mathcal { C } , \bar { \rho } , \psi ) = 0$ we call P a self-residual point, i.e., we consider $\mathrm { P }$ as a residual point related to itself. We agree that the point $( x , y ) = ( q , 0 )$ , corresponding to the observer position, is the residual point related to $( x , y ) = ( 0 , 0 )$ , when the latter belongs to $\mathfrak { S }$ . For $\gamma = 1$ each point of the singular curve has the observer position as residual point.

Let $\gamma \neq 1$ . The limiting curve $\mathcal { L }$ is the set of all the residual points related to the points in $\mathfrak { S }$ . By the symmetry of $\mathfrak { S }$ and of the level curves of $\mathrm { C } ^ { ( \gamma ) } ( x , y )$ , the limiting curve is also symmetric with respect to the $x$ axis. If the point $( q , 0 )$ is in $\mathcal { L }$ , it is not isolated. It has the following properties:

(separating property): for $\gamma \neq 1$ the limiting curve $\mathcal { L }$ is a connected simple continuous curve, separating $\mathcal { D }$ into two connected regions $\mathcal { D } _ { 1 } , \mathcal { D } _ { 3 }$ ;

$\mathcal { D } _ { 3 }$ contains the whole portion $\mathfrak { S }$ of the singular curve. If $\gamma < 1$ then $\mathcal { L }$ is a closed curve, if $\gamma > 1$ it is unbounded;

(transversality): the level curves of $\operatorname { C } ^ { ( \gamma ) } ( x , y )$ cross $\mathcal { L }$ transversely, except for the two self-residual points and where $\mathcal { L }$ meets the $x$ axis;

(limiting property): for $\gamma \neq 1$ the limiting curve $\mathcal { L }$ divides the set $\mathcal { D }$ into two connected regions $\mathcal { D } _ { 1 } , \mathcal { D } _ { 3 }$ : the points of $\mathcal { D } _ { 1 }$ are the unique solutions of the corresponding intersection problem; the points of $\mathcal { D } _ { 3 }$ are solutions of an intersection problem with three solutions, all lying in $\mathcal { D } _ { 3 }$ .

![](images/168dce176a46b5517720378c84032875543eb633ab0cb8c1403a5536e103e847.jpg)  
Fig. 9.7. Summary of the results on alternative solutions for all the qualitatively different cases. The regions with a different number of solutions are shaded: we use light gray for two solutions, dark gray for three solutions. Top left: $\gamma = - 0 . 5$ . Top right: $\gamma = 0 . 8$ . Bottom left: $\gamma = 1$ (Charlier case). Bottom right: $\gamma = 1 . 1$ . Reprinted from Gronchi (2009) with permission from Springer.

Figure 9.7 summarizes the results for all the significantly different cases: we distinguish among regions with a unique solution of (9.31) (white), with two solutions (light gray), and with three solutions (dark gray). For $\gamma =$ $- 0 . 5$ (top left) there are only two regions, with either one or three solutions. For $\gamma = 0 . 8$ (top right) in the region outside the zero circle there are two solutions; the region inside is divided by the limiting curve into two parts, with either one or three solutions. On the bottom left, we have the Charlier case ( $\gamma = 1$ ), discussed in Section 9.6. For $\gamma = 1 . 1$ (bottom right) inside the zero circle there are two solutions; the region outside can contain either one or three solutions. In each case the singular curve separates the regions with alternative solutions into parts with only one solution each.

The numbers of solutions are generically different from those of Charlier: the solutions can be up to three, and up to two close to the opposition.

It is not easy to find a good example with three solutions; in many cases the solution nearest to the observer has distance $\rho$ too small for the heliocentric two-body approximation to be applicable. A value $\rho = 0 . 0 1$ AU corresponds approximately to the sphere of influence of the Earth, i.e., the region where the perturbation from the Earth is more important than the attraction from the Sun. Thus, a solution with such a small $\rho$ can be considered spurious because the approximation used in the Gauss and Laplace methods is poor.

An example of the qualitative changes when $\gamma _ { 2 } \neq 1$ , based upon real data, is given by the first three nights of observation of asteroid 2002 AA29: with $\epsilon \sim 7 9 ^ { \circ }$ , there is only one solution with $\rho ~ = ~ 0 . 0 4 5$ (see Figure 9.8, left) which leads to a least squares solution with $\rho = 0 . 0 4 4$ . Although the value of $\gamma _ { 2 }$ is not very far from 1 the existence of the solution depends critically on $\gamma _ { 2 } \neq 1$ : for $\gamma _ { 2 } = 1$ there would be no solution (Figure 9.8, right).

![](images/b0e8a935969a81405755c35706eff416e222c44c3aab3c4ccb11fa68dd663be3.jpg)  
Fig. 9.8. For the preliminary orbit of $2 0 0 2 \mathrm { \ A A _ { 2 9 } }$ we show the relevant level curve ( $\mathcal { C } _ { 2 } = 1 . 6 5 3$ ) and the zero circle; the observation direction is dotted. Left: using the actual value $\gamma _ { 2 } ~ = ~ 1 . 0 2 5$ . Right: using a value of $\gamma _ { 2 } ~ = ~ 1$ not accounting for topocentric observations. Reprinted from Milani et al. (2008) with permission from Elsevier.

# 10

# WEAKLY DETERMINED ORBITS

In most cases of population orbit determination the fit parameters $\mathbf { x }$ are just the initial conditions for an orbit, thus $\mathbf { x } \in \mathbb { R } ^ { 6 }$ . We assume that there are at least enough observations to compute an attributable; if the arc is short, an approximate rank deficiency can occur, with order 1 or at most 2. In this chapter we discuss the special techniques which can be used to handle this kind of weak orbit determination, how to sample large confidence regions, the origin of such weakness, typically in a too short observations time span, and the impact on the quality of the orbit solution. This chapter is based on our papers (Milani et al. 2005c, Milani et al. 2007, Milani et al. 2008).

# 10.1 The line of variations

Given any point $\mathbf { x }$ in the space of initial conditions, we can compute the $6 \times 6$ normal matrix $C ( \mathbf { x } )$ . Even when the inverse $\Gamma ( \mathbf { x } )$ cannot be computed, or is numerically unstable because of a large conditioning number, we can define

$$
Z _ { L } ( \sigma ) = \{ \mathbf { y } | ( \mathbf { y } - \mathbf { x } ) \cdot C ( \mathbf { x } ) \ ( \mathbf { y } - \mathbf { x } ) \leq \sigma ^ { 2 } \}
$$

which is an ellipsoid if $C ( \mathbf { x } )$ is positive definite. The main assumption in this chapter is that the observation information is above the minimum required to compute an attributable,1 to the point that the matrix $C ( \mathbf { x } )$ has rank $> 4$ . Still it could have rank 5, with a zero eigenvalue, or rank 6, but with a very small eigenvalue.

# Ellipsoid long axis and weak direction

Let $\mathbf { v } _ { 1 } ( \mathbf { x } )$ be an eigenvector of $C ( \mathbf { x } )$ with the smallest eigenvalue $\lambda _ { 1 } ( \mathbf { x } ) \geq 0$ :

$$
C ( \mathbf { x } ) \mathbf { v } _ { 1 } ( \mathbf { x } ) = \lambda _ { 1 } ( \mathbf { x } ) \mathbf { v } _ { 1 } ( \mathbf { x } ) .
$$

1 This implies that the number of scalar observations is $> 4$ .

The other eigenvalues $\lambda _ { j } ( \mathbf { x } ) , j = 2 , 6$ , are assumed strictly $> \lambda _ { 1 } ( \mathbf { x } )$ . In the extreme case $\lambda _ { 1 } ( \mathbf { x } ) = 0$ , $Z _ { L } ( \sigma )$ is a cylinder with axis parallel to $\mathbf { v } _ { 1 } ( \mathbf { x } )$ . If $\lambda _ { 1 } ( \mathbf { x } ) > 0$ , the longest semiaxis of the confidence ellipsoid is in the direction $\mathbf { v } _ { 1 } ( \mathbf { x } )$ and has length $k _ { 1 } ( \mathbf { x } ) = 1 / \sqrt { \lambda _ { 1 } ( \mathbf { x } ) }$ for $\sigma = 1$ . $\mathbf { v } _ { 1 } ( \mathbf { x } )$ is also an eigenvector of $\Gamma ( \mathbf { x } ) = C ^ { - 1 } ( \mathbf { x } )$ with the largest eigenvalue $1 / \lambda _ { 1 } ( \mathbf { x } ) = k _ { 1 } ^ { 2 } ( \mathbf { x } )$ , thus it defines the weak direction of the least squares fit.

If the fit were linear, the nominal solution $\mathbf { x } ^ { * }$ could be found from $C \mathrm { { \bf ~ x } ^ { * } = }$ $D$ (see Section 5.2), without iterations, and the target function would be just

$$
m Q ( \mathbf { y } ) = ( \mathbf { y } - \mathbf { x } ^ { * } ) \cdot C \left( \mathbf { y } - \mathbf { x } ^ { * } \right) + m Q ^ { * } .
$$

Let $H$ be the hyperplane spanned by the other eigenvectors ${ \bf v } _ { j } ( { \bf x } ) , j { \bf \delta } = { \bf \delta }$ $2 , \ldots , 6$ . The tip $\mathbf { x } _ { 1 } = \mathbf { x } ^ { * } + k _ { 1 } \ \mathbf { v } _ { 1 }$ of the longest axis of the confidence ellipsoid is the minimum point of the target function restricted to the affine hyperplane $\mathbf x _ { 1 } + H$ and is also a local minimum point of the target function restricted to the sphere $| \mathbf { y } - \mathbf { x } ^ { * } | = k _ { 1 } | \mathbf { v } _ { 1 } |$ . These properties, equivalent in the linear regime, are not equivalent in general.

# The weak direction vector field

For each $\mathbf { x }$ , let us select the eigenvector $\mathbf { v } _ { 1 } ( \mathbf { x } )$ to be a unit vector. Then

$$
\mathbf { F } ( \mathbf { x } ) = k _ { 1 } ( \mathbf { x } ) \mathbf { v } _ { 1 } ( \mathbf { x } ) ,
$$

with $k _ { 1 } ( \mathbf { x } ) = 1 / \sqrt { \lambda _ { 1 } ( \mathbf { x } ) }$ , is a vector field. The unit eigenvector $\mathbf { v } _ { 1 }$ is not uniquely defined, $- \mathbf { v } _ { 1 }$ is also a unit eigenvector. Thus $k _ { 1 } ( \mathbf { x } ) \mathbf { v } _ { 1 } ( \mathbf { x } )$ is what is called an axial vector, with well-defined length and direction but an arbitrary sign. However, given an axial vector field defined over a simply connected set, there is always a way to define a true vector field $\mathbf { F } ( \mathbf { x } )$ such that the function $\mathbf { x } \mapsto \mathbf { F } ( \mathbf { x } )$ is continuous. At an initial point we can select the sign according to some rule, e.g., such that the directional derivative of the semimajor axis $a$ is positive in the direction $\mathbf { v } _ { 1 } ( \mathbf { x } )$ . Then the orientation is maintained by imposing that $\mathbf { v } _ { 1 } ( \mathbf { x } )$ is continuous.

Problems could arise, for some value of $\mathbf { x }$ , if either $\lambda _ { 1 } ( \mathbf { x } ) = 0$ or the normal matrix $C ( \mathbf { x } )$ had its smallest eigenvalue of multiplicity 2. If the normal matrix is degenerate, see the discussion in Section 6.1. The exact equality of two eigenvalues does not occur generically, and even an approximate equality is rare in applications, as we have found from a large set of examples. Anyway, whenever the two smallest eigenvalues are of the same order of magnitude this method has serious limitations, as discussed in Section 10.3.