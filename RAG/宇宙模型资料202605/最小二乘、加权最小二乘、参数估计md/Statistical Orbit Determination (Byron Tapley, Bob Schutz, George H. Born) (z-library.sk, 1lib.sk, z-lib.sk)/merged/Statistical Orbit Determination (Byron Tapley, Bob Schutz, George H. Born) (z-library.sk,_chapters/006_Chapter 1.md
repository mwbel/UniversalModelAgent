# Chapter 1

# Orbit Determination Concepts

# 1.1 INTRODUCTION

The treatment presented here will cover the fundamentals of satellite orbit determination and its evolution over the past four decades. By satellite orbit determination we mean the process by which we obtain knowledge of the satellite’s motion relative to the center of mass of the Earth in a specified coordinate system. Orbit determination for celestial bodies has been a general concern of astronomers and mathematicians since the beginning of civilization and indeed has attracted some of the best analytical minds to develop the basis for much of the fundamental mathematics in use today.

The classical orbit determination problem is characterized by the assumption that the bodies move under the influence of a central (or point mass) force. In this treatise, we focus on the problem of determining the orbits of noncelestial satellites. That is, we focus on the orbits of objects placed into orbit by humans. These objects differ from most natural objects in that, due to their size, mass, and orbit charateristics, the nongravitational forces are of significant importance. Further, most satellites orbit near to the surface and for objects close to a central body, the gravitational forces depart from a central force in a significant way.

By the state of a dynamical system, we mean the set of parameters required to predict the future motion of the system. For the satellite orbit determination problem the minimal set of parameters will be the position and velocity vectors at some given epoch. In subsequent discussions, this minimal set will be expanded to include dynamic and measurement model parameters, which may be needed to improve the prediction accuracy. This general state vector at a time, $t$ , will be denoted as $\mathbf X ( t )$ t. The general orbit determination problem can then be posed as follows.

If at some initial time, $t _ { 0 }$ , the state $\mathbf { X } _ { 0 }$ of a vehicle following a ballistic trajecttory is given and if the differential equations that govern the motion of the vehicle are known, then the equations of motion can be integrated to determine the state of the vehicle at any time. However, during an actual flight, the initial state is never known exactly. Moreover, certain physical constants as well as the mathematical specification of the forces required to define the differential equations of motion are known only approximately. Such errors will cause the actual motion to deviate from the predicted motion. Consequently, in order to determine the position of the spacecraft at some time $t > t _ { 0 }$ , it must be tracked or observed from t > ttracking stations whose positions are known precisely. With the observations of the spacecraft motion, a better estimate of the trajectory can be determined. The term “better estimate” is used since the observations will be subject to both random and systematic errors and, consequently, the estimate of the trajectory will not be exact.

The observational data will usually consist of such measurements as range, range-rate, azimuth, elevation, or other observable quantities. That is, the state variables (position, velocity, unknown model parameters, etc.) will not be observed, but rather the observable will usually be some nonlinear function of the state variables.

The problem of determining the best estimate of the state of a spacecraft, whose initial state is unknown, from observations influenced by random and systematic errors, using a mathematical model that is not exact, is referred to as the problem of state estimation. In this presentation, such a procedure will be referred to as the process of orbit determination. The word “best” is used to imply that the estimate is optimal in some as yet undefined statistical sense.

When an estimate of the trajectory has been made, the subsequent motion and values for the observations can be predicted. In the orbit determination procedure, the process of predicting the state of a vehicle is referred to as “generating an ephemeris.” An ephemeris for a space vehicle is a table of its position and velocity components as a function of time. The predicted values will differ from the true values due to the following effects:

1. Inaccuracies in the estimated state vector (i.e., position and velocity vector) caused by errors in the orbit determination process, such as:

a. Approximations involved in the method of orbit improvement and in the mathematical model,   
b. Errors in the observations,   
c. Errors in the computational procedure used in the solution process.

2. Errors in the numerical integration procedure caused by errors in the dynamical model and computer truncation and roundoff errors.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0001_pages_0001-0070/auto/images/b1132a7e23762a8db80a9a80b21240907329f03b06cadb2a8ce6a7f1967e7641.jpg)  
Figure 1.2.1: Uniform gravity field trajectory.

Consequently, the process of observation and estimation must be repeated continually as the vehicle’s motion evolves. Furthermore, the orbit determination procedure may be used to obtain better estimates of the location of tracking stations, adjust the station clocks, calibrate radar biases, obtain a better estimate of geophysical constants, and so on. In fact, any observable quantity directly affecting either the motion of the vehicle or the observation-state relationship can be determined by appropriately using the observational data.

To formulate the orbit determination problem, we will use elements of probability and statistics as well as matrix theory. Appendixes A and B contain introductory material on these topics.

# 1.2 UNIFORM GRAVITY FIELD MODEL

To illustrate some of the basic ideas involved in the orbit determination process, consider the flight of a vehicle moving under the influence of a uniform gravitational field, as shown in Fig. 1.2.1. In the preliminary design of the trajectory, an initial state $\mathbf { X } _ { 0 } ^ { * }$ (i.e., the initial position and the initial velocity vectors), is selected in such a way that the vehicle will follow a desired nominal (or design) trajectory. In practice, however, the design conditions are never realized. Hence, the true initial state, $\mathbf { X } _ { 0 }$ , will differ from the nominal initial state, $\mathbf { X } _ { 0 } ^ { * }$ , and consequently, the true trajectory followed by the vehicle will differ from the nominal trajectory. An indication of these two trajectories is given in Fig. 1.2.1. Here the true trajectory is denoted as $\mathbf { X }$ , the nominal trajectory as $\mathbf { X } ^ { * }$ , and the best estimate of the true trajectory is indicated by $\hat { \bf X }$ . To determine an estimate, $\hat { \bf X }$ , of the true trajectory of the vehicle, tracking information must be used.

Figure 1.2.1 shows a tracking station at a point whose coordinates are $( X _ { s } , Y _ { s } )$ Assume that the range (linear distance along the line of sight), $\rho$ X , Y, and the elevation, $\theta$ ρ, of the line of sight to the satellite can be measured. The tracking information, or θobservations, $\rho$ and $\theta$ , at any time depend on the true state of the satellite and the ρ θposition of the tracking station. Since the true position of the satellite is unknown, the calculated or modeled values of the observations will depend on the nominal position of the satellite and the location of the tracking station at the time the observation is made. The difference between observed and calculated observations at the observation time provides the information used to obtain an improved estimate of the satellite’s motion. Other observations such as range rate, $\dot { \rho }$ , and elevation rate, $\dot { \theta }$ ρ, which depend on both the velocity and position of the satellite θand tracking station, could also be used to determine $\hat { \mathbf X }$ . Note that range rate is the line of sight velocity that is, the projection of the spacecraft’s velocity vector on to the range vector

$$
{ \dot { \rho } } = { \frac { { \dot { \rho } } \cdot \rho } { \rho } } .
$$

# 1.2.1 FORMULATION OF THE PROBLEM

For the uniform gravity field model, the differential equations of motion can be expressed as

$$
\begin{array} { l c l } { \ddot { X } ( t ) } & { = } & { 0 } \\ { \ddot { Y } ( t ) } & { = } & { - g , } \end{array}
$$

where $g$ is the gravitational acceleration and is assumed to be constant. Integration gof Eq. (1.2.1) leads to

$$
\begin{array} { l c l } { { X ( t ) } } & { { = } } & { { X _ { 0 } + \dot { X } _ { 0 } t } } \\ { { Y ( t ) } } & { { = } } & { { Y _ { 0 } + \dot { Y } _ { 0 } t - g \frac { t ^ { 2 } } { 2 } , } } \\ { { \dot { X } ( t ) } } & { { = } } & { { \dot { X } _ { 0 } } } \\ { { \dot { Y } ( t ) } } & { { = } } & { { \dot { Y } _ { 0 } - g t } } \end{array}
$$

where $t$ represents the time, and the reference time, $t _ { 0 }$ , is chosen to be zero. The subscript 0 indicates values of the quantities at $t _ { 0 }$ . Now, providing the values of

$X _ { 0 } , Y _ { 0 } , \dot { X } _ { 0 } , \dot { Y } _ { 0 }$ , and $g$ are given, Eq. (1.2.2) can be used to predict the position X Y X Y gand velocity of the vehicle at any time. However, as previously indicated, the values of these quantities are never known exactly in practice, and it is the task of the orbit determination procedure to estimate their values.

# 1.2.2 THE EQUATION OF THE ORBIT

The parameter $t$ can be eliminated in the last two of Eq. (1.2.2) to obtain the tcurve followed by the vehicle in the $( X , Y )$ plane; that is,

$$
t = \frac { X - X _ { 0 } } { \dot { X } _ { 0 } } .
$$

Hence,

$$
{ \cal { Y } } ( t ) = { \cal { Y } } _ { 0 } + \frac { \dot { Y } _ { 0 } } { \dot { X } _ { 0 } } ( X - X _ { 0 } ) - { \frac { 1 } { 2 } } \frac { g } { \dot { X } _ { 0 } ^ { 2 } } ( X - X _ { 0 } ) ^ { 2 } .
$$

Equation (1.2.4) can be recognized readily as the equation of a parabola. This equation is analogous to the conic curve obtained as the solution to motion in an inverse square force field (see Chapter 2). It should be noted that Eqs. (1.2.3) and (1.2.4) still involve the values of the four initial conditions. The relation indicates that if the vehicle was at $X ^ { \prime }$ , then it must also have been at $Y ^ { \prime }$ obtained from Eq. X(1.2.4). It is also obvious that any real value of $X$ Yis possible, and it has associated with it a unique $Y$ X. However, the converse is not true. For each possible value of $Y$ Y, there are usually two values of $X$ possible. The time epoch, $t ^ { \prime }$ , corresponding Yto the point $( X ^ { \prime } , Y ^ { \prime } )$ Xcan be determined from the relation $t ^ { \prime } = ( X ^ { \prime } - \bar { X } _ { 0 } ) / \dot { X } _ { 0 }$ . X , Y t X X /XThis relation is analogous to Kepler’s equation for the motion in an inverse square force field. Since the epoch of time must be associated with the determination of the state of the vehicle if an ephemeris is to be generated and since the time is an integral part of all observations, the solution in the form of Eqs. (1.2.3) and (1.2.4) is usually not convenient for most orbit determination procedures.

In the subsequent discussions, either the differential equations, Eq. (1.2.1), or their solution in the form of Eq. (1.2.2) will be used.

# 1.2.3 THE ROLE OF THE OBSERVATION

As an example of the orbit determination procedure, consider the situation in which the state is observed at some time epoch, $t _ { j }$ . Then if $X _ { j } , Y _ { j } , \dot { X } _ { j }$ and $\dot { Y } _ { j }$ are given at $t _ { j }$ t X Y X, Eq. (1.2.2) can be used to form four equations in terms of Y tfour unknowns. This system of equations can be used to determine the unknown components of the initial state. For example, from Eq. (1.2.2) it follows that

$$
\begin{array} { r l r } { \left[ \begin{array} { l } { X _ { j } } \\ { Y _ { j } + g t _ { j } ^ { 2 } / 2 } \\ { \dot { X } _ { j } } \\ { \dot { Y } _ { j } + g t _ { j } } \end{array} \right] } & { = } & { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { t _ { j } } & { 0 } \\ { 0 } & { 1 } & { 0 } & { t _ { j } } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { l } { X _ { 0 } } \\ { Y _ { 0 } } \\ { \dot { X } _ { 0 } } \\ { \dot { Y } _ { 0 } } \end{array} \right] . } \end{array}
$$

Then, the initial state can be determined as follows:

$$
\begin{array} { r l r } { \left[ \begin{array} { l } { X _ { 0 } } \\ { Y _ { 0 } } \\ { \dot { X } _ { 0 } } \\ { \dot { Y } _ { 0 } } \end{array} \right] } & { { } = } & { \left[ \begin{array} { l l l l } { 1 } & { 0 } & { t _ { j } } & { 0 } \\ { 0 } & { 1 } & { 0 } & { t _ { j } } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] ^ { - 1 } \left[ \begin{array} { l } { X _ { j } } \\ { Y _ { j } + g t _ { j } ^ { 2 } / 2 } \\ { \dot { X } _ { j } } \\ { \dot { Y } _ { j } + g t _ { j } } \end{array} \right] . } \end{array}
$$

Providing that the matrix inverse in Eq. (1.2.5) exists, the true initial state ${ \bf X } _ { 0 } ^ { T } = { }$ $[ X _ { 0 } , Y _ { 0 } , \overset { \cdot } { X } _ { 0 } , \overset { \cdot } { Y _ { 0 } } ]$ can be determined.

, Y , X , YUnfortunately, in an actual trajectory or orbit determination process, the individual components of the state generally cannot be observed directly. Rather, the observations consist of nonlinear functions of the state; for example, range, elevation, range rate, and so on. In this case, the nonlinear observation-state relationship is

$$
\begin{array} { r c l } { \rho } & { = } & { \sqrt { ( X - X _ { s } ) ^ { 2 } + ( Y - Y _ { s } ) ^ { 2 } } } \\ { \tan \theta } & { = } & { ( Y - Y _ { s } ) / ( X - X _ { s } ) } \\ { \dot { \rho } } & { = } & { \displaystyle \frac { 1 } { \rho } [ ( X - X _ { s } ) ( \dot { X } - \dot { X } _ { s } ) + ( Y - Y _ { s } ) ( \dot { Y } - \dot { Y } _ { s } ) ] } \\ { \dot { \theta } } & { = } & { \displaystyle \frac { 1 } { \rho ^ { 2 } } [ ( X - X _ { s } ) ( \dot { Y } - \dot { Y } _ { s } ) - ( \dot { X } - \dot { X } _ { s } ) ( Y - Y _ { s } ) ] , } \end{array}
$$

where $X _ { s } , Y _ { s } , \dot { X } _ { s }$ , and $\dot { Y } _ { s }$ are the position and velocity components, respectively, X Y X Yof the tracking station. Generally the station velocity components $\dot { X } _ { s }$ and $\dot { Y } _ { s }$ will X Ybe zero relative to an Earth-fixed frame unless we are accounting for tectonic plate motion. Now, if $\rho , \theta , \dot { \rho }$ and $\dot { \theta }$ are given at $t _ { j }$ , then Eq. (1.2.2) can be substituted ρ θ ρinto Eq. (1.2.6) to obtain

$$
\begin{array} { r c l } { \rho _ { j } } & { = } & { \sqrt { ( X _ { 0 } - X _ { s } + \dot { X } _ { 0 } t _ { j } ) ^ { 2 } + ( Y _ { 0 } - Y _ { s } + \dot { Y } _ { 0 } t _ { j } - g t _ { j } ^ { 2 } / 2 ) ^ { 2 } } } \\ { \theta _ { j } } & { = } & { \tan ^ { - 1 } [ ( Y _ { 0 } - Y _ { s } + \dot { Y } _ { 0 } t _ { j } - g \frac { t _ { j } ^ { 2 } } { 2 } ) / ( X _ { 0 } - X _ { s } + \dot { X } _ { 0 } t _ { j } ) ] } \\ { \dot { \rho } _ { j } } & { = } & { \cfrac { 1 } { \rho _ { j } } [ ( X _ { 0 } - X _ { s } + \dot { X } _ { 0 } t _ { j } ) ( \dot { X } _ { 0 } - \dot { X } _ { s } ) } \\ & & { + ( Y _ { 0 } - Y _ { s } + \dot { Y } _ { 0 } t _ { j } - g \frac { t _ { j } ^ { 2 } } { 2 } ) ( \dot { Y } _ { 0 } - g t _ { j } - \dot { Y } _ { s } ) ] } \end{array}
$$

$$
\begin{array} { r c l } { { \dot { \theta } _ { j } } } & { { = } } & { { \displaystyle \frac { 1 } { \rho _ { j } ^ { 2 } } [ ( X _ { 0 } - X _ { s } + \dot { X } _ { 0 } t _ { j } ) ( \dot { Y } _ { 0 } - g t _ { j } - \dot { Y } _ { s } ) } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { - ( \dot { X } _ { 0 } - \dot { X } _ { s } ) ( Y _ { 0 } - Y _ { s } + \dot { Y } _ { 0 } t _ { j } - g \frac { t _ { j } ^ { 2 } } { 2 } ) ] . } } \end{array}
$$

Symbolically Eq. (1.2.7) represents four nonlinear algebraic equations in terms of the unknown components of the initial state. If $\mathbf { Y } ^ { T }$ represents the vector whose components are the observations $[ \rho _ { j } , \theta _ { j } , \dot { \rho } _ { j } , \dot { \theta } _ { j } ]$ , then Eq. (1.2.7) can be expressed as

$$
J ( \mathbf { X } _ { 0 } ) \equiv \mathbf { Y } - G ( \mathbf { X } _ { 0 } , t ) = 0 ,
$$

where $G ( \mathbf { X } _ { 0 } , t )$ is a $4 \times 1$ vector of nonlinear functions consisting of the right-hand G , tside of Eq. (1.2.7). Eq. (1.2.8) can be solved iteratively by the Newton–Raphson iteration procedure. If $\mathbf { X } _ { 0 } ^ { n }$ represents the $n$ th approximation to the solution, then

$$
J ( \mathbf { X } _ { 0 } ^ { n + 1 } ) \cong J ( \mathbf { X } _ { 0 } ^ { n } ) + \left[ \frac { \partial J } { \partial \mathbf { X } _ { 0 } ^ { n } } \right] [ \mathbf { X } _ { 0 } ^ { n + 1 } - \mathbf { X } _ { 0 } ^ { n } ] ,
$$

according to a 2-term Taylor series approximation. Now, setting ${ \cal J } ( { \bf X } _ { 0 } ^ { n + 1 } ) = 0$ to comply with Eq. (1.2.8) and solving for $\mathbf { X } _ { 0 } ^ { n + 1 }$ leads to

$$
\mathbf { X } _ { 0 } ^ { n + 1 } = \mathbf { X } _ { 0 } ^ { n } - \left[ \frac { \partial J } { \partial \mathbf { X } _ { 0 } ^ { n } } \right] ^ { - 1 } J ( \mathbf { X } _ { 0 } ^ { n } ) ,
$$

where

$$
\frac { \partial J } { \partial \mathbf { X } _ { 0 } ^ { n } } = - \frac { \partial G ( \mathbf { X } _ { 0 } ^ { n } , t ) } { \partial \mathbf { X } _ { 0 } ^ { n } } .
$$

The process can be repeated until $| | \mathbf { X } _ { 0 } ^ { n + 1 } - \mathbf { X } _ { 0 } ^ { n } | | \leq \epsilon$ , where $\epsilon$ is a small positive number.

Several facts are obvious from this example:

1. The linear dependence of the state at time $t$ on the initial conditions, as tobtained in Eq. (1.2.2), usually does not occur.   
2. In general, the equations that define the solution to the orbit determination problem are nonlinear, and the solution must be obtained by a numerical iteration procedure. Note that this iteration procedure requires an initial guess for $\mathbf { X } _ { 0 }$ . This initial guess must be close enough to the true solution for convergence to occur.   
3. Since the equations are nonlinear, multiple solutions may exist; only one will correspond to the minimizing or correct solution. Generally the initial guess for $\mathbf { X } _ { 0 }$ will be close to the truth so convergence to an incorrect solution is not a problem.

This situation represents a special case of the usual orbit determination problem; that is, the case where there are as many independent observations at one epoch of time as there are unknown components of the state vector. Usually, the number of observations available at any time will be smaller than the number of components in the state vector. For example, the radar may have the capability of measuring only range, $\rho$ , and range rate, $\dot { \rho }$ , or range and elevation, $\theta$ , at any ρone point in time. The observation set $( \rho , \theta )$ ρ θis not adequate to determine the state $( \bar { X _ { 0 } , Y _ { 0 } , \dot { X } _ { 0 } , \dot { Y _ { 0 } } } )$ ρ, θ, since using Eq. (1.2.6) will lead to a set of two nonlinear equa-X , Y , X , Ytions in terms of four unknowns. However, if observations are available at any two time points $t _ { 1 }$ and $t _ { 2 }$ , then the set $( \rho _ { 1 } , \theta _ { 1 } , \rho _ { 2 } , \theta _ { 2 } )$ can be used to determine t t ρ , θ , ρ , θthe trajectory. From Eq. (1.2.7), the following equations can be obtained:

$$
\begin{array} { r c l } { \rho _ { 1 } } & { = } & { \sqrt { ( X _ { 0 } - X _ { s } + \dot { X } _ { 0 } t _ { 1 } ) ^ { 2 } + ( Y _ { 0 } - Y _ { s } + \dot { Y } _ { 0 } t _ { 1 } - g t _ { 1 } ^ { 2 } / 2 ) ^ { 2 } } } \\ { \theta _ { 1 } } & { = } & { \tan ^ { - 1 } [ ( Y _ { 0 } - Y _ { s } + \dot { Y } _ { 0 } t _ { 1 } - g t _ { 1 } ^ { 2 } / 2 ) / ( X _ { 0 } - X _ { s } + \dot { X } _ { 0 } t _ { 1 } ) ] } \\ { \rho _ { 2 } } & { = } & { \sqrt { ( X _ { 0 } - X _ { s } + \dot { X } _ { 0 } t _ { 2 } ) ^ { 2 } + ( Y _ { 0 } - Y _ { s } + \dot { Y } _ { 0 } t _ { 2 } - g t _ { 2 } ^ { 2 } / 2 ) ^ { 2 } } } \\ { \theta _ { 2 } } & { = } & { \tan ^ { - 1 } [ ( Y _ { 0 } - Y _ { s } + \dot { Y } _ { 0 } t _ { 2 } - g t _ { 2 } ^ { 2 } / 2 ) / ( X _ { 0 } - X _ { s } + \dot { X } _ { 0 } t _ { 2 } ) ] . } \end{array}
$$

Equation (1.2.10) represents four nonlinear equations in terms of four unknowns from which the unknowns can be determined as indicated by Eq. (1.2.9).

The approaches just outlined have two fundamental assumptions that cannot be realized in practice. These assumptions are:

1. Perfect knowledge of the differential equations that describe the motion.

2. Perfect observations.

The assumption of perfect knowledge of the differential equations implies that all the forces are modeled perfectly and that the values for the constant parameters used in the force model are exact. Usually, the true values for all of the parameters are not defined with complete numerical accuracy. But what is even more relevant, simplifying assumptions usually are made to reduce the computational requirements. Under such assumptions, certain unimportant or “negligible” components of the forces acting on the vehicle are omitted. As a consequence, the mathematical model used to describe the dynamical process will differ from the true process.

In general, the observations will be corrupted by random and systematic observation errors that are inherent in the measurement process. Hence, the observed value of the range, $\rho$ , or elevation, $\theta$ , will differ from the true value because of ρ θthese errors. In addition, the true and observed values for the range and the elevation will differ because of imperfect knowledge of the tracking station location, $( X _ { s } , Y _ { s } )$ .

Because of these factors, four observations will not be sufficient to determine the planar motion trajectory exactly. In the usual operational situation, many observations are made, and the trajectory is selected to give the best agreement with the observations obtained. In general the mechanism for obtaining the best estimate is to linearize the problem by expanding the equations of motion and the observation-state relationship about a reference trajectory. Deviations from the reference trajectory (e.g., position and velocity) are then determined to yield the “best” agreement with the observations. As we will see, the “best” agreement generally is based on the least squares criterion.

# 1.2.4 LINEARIZATION PROCEDURE

To illustrate the linearization procedure, return to the flat Earth example discussed previously. Assuming that there are errors in each of the initial position and velocity values and in $g$ , the state vector is $X ^ { T } = [ X , Y , \dot { X } , \dot { Y } , g ]$ . It is a gstraightforward procedure to replace $X$ by $X ^ { * } + \delta X$ , $Y$ X,by $Y ^ { * } + \delta Y , \ldots$ and $g$ by $g ^ { * } + \delta g$ in Eq. (1.2.2) to obtain the equation for perturbation, or deviation, from the reference trajectory. The $( ) ^ { * }$ values represent assumed or specified values. If the equations for the reference trajectory, designated by the $( ) ^ { * }$ values, are subtracted from the result obtained by this substitution, the equations for the state deviations are obtained as

$$
\begin{array} { l c l } { \delta X } & { = } & { \delta X _ { 0 } + \delta \dot { X } _ { 0 } t } \\ { \delta Y } & { = } & { \delta Y _ { 0 } + \delta \dot { Y } _ { 0 } t - \delta g \frac { t ^ { 2 } } { 2 } } \\ { \delta \dot { X } } & { = } & { \delta \dot { X } _ { 0 } } \\ { \delta \dot { Y } } & { = } & { \delta \dot { Y } _ { 0 } - \delta g t } \\ { \delta g } & { = } & { \delta g . } \end{array}
$$

Equation (1.2.11) can be expressed in matrix form in the following manner:

$$
\begin{array} { r l r } { \left[ \begin{array} { c } { \delta X } \\ { \delta Y } \\ { \delta \dot { X } } \\ { \delta \dot { Y } } \\ { \delta g } \end{array} \right] } & { = } & { \left[ \begin{array} { c c c c c } { 1 } & { 0 } & { t } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { t } & { - t ^ { 2 } / 2 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { - t } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { c } { \delta X _ { 0 } } \\ { \delta Y _ { 0 } } \\ { \delta \dot { X } _ { 0 } } \\ { \delta \dot { Y } _ { 0 } } \\ { \delta g } \end{array} \right] . } \end{array}
$$

Equation (1.2.12) can be used to predict the deviation of the vehicle from the reference trajectory, $\mathbf { X } ^ { * } ( t )$ , at any time $t > 0$ . Note that the deviations from the true state, $\delta \mathbf { X } ( t ) \equiv \mathbf { x } ( t )$ t t >, will be caused by deviations in the original state or deviations δ t tin the gravitational acceleration, $\delta g$ . However, the quantities $\delta X _ { 0 } , \delta Y _ { 0 } , \ldots$ are δg δX , δY , . . . ,not known, and it is the problem of the orbit determination procedure to estimate their values.

In this example, both Eqs. (1.2.2) and (1.2.12) are linear. In the case of central force field motion, the equations analogous to Eq. (1.2.2) are not linear, however, and the orbit determination process is simplified considerably by the linearization procedure. Care must be taken so that deviations from the reference conditions remain in the linear range.

As mentioned earlier, the observations $\rho$ and $\theta$ , which are taken as the satellite ρ θfollows the true trajectory, are nonlinear functions of $X$ , $Y$ , $X _ { s }$ , and $Y _ { s }$ . Further-X Y Xmore, they contain random and systematic errors represented by $\epsilon _ { \rho }$ Yand $\epsilon _ { \theta }$ ; hence,

$$
\begin{array} { r c l } { \rho } & { = } & { \sqrt { ( X - X _ { s } ) ^ { 2 } + ( Y - Y _ { s } ) ^ { 2 } } + \epsilon _ { \rho } } \\ { \theta } & { = } & { \tan ^ { - 1 } \left( \frac { Y - Y _ { s } } { X - X _ { s } } \right) + \epsilon _ { \theta } . } \end{array}
$$

Our objective is to linearize the observations with respect to the reference trajectory. This can be accomplished by expanding Eq. (1.2.13) in a Taylor series about the reference or nominal trajectory as follows:

$$
\begin{array} { r l r } { \rho } & { \cong } & { \rho ^ { * } \quad + \left[ \frac { \partial \rho } { \partial X } \right] ^ { * } \left( X - X ^ { * } \right) + \left[ \frac { \partial \rho } { \partial Y } \right] ^ { * } \left( Y - Y ^ { * } \right) + \epsilon _ { \rho } } \\ { \theta } & { \cong } & { \theta ^ { * } \quad + \left[ \frac { \partial \theta } { \partial X } \right] ^ { * } \left( X - X ^ { * } \right) + \left[ \frac { \partial \theta } { \partial Y } \right] ^ { * } \left( Y - Y ^ { * } \right) + \epsilon _ { \theta } . } \end{array}
$$

Note that the partials with respect to $\dot { X } , \dot { Y }$ , and $g$ are zero since they do not appear Xexplicitly in Eq. (1.2.13). By defining

$$
\begin{array} { r c l } { { \delta \rho } } & { { = } } & { { \rho - \rho ^ { * } } } \\ { { \delta \theta } } & { { = } } & { { \theta - \theta ^ { * } } } \\ { { \delta X } } & { { = } } & { { X - X ^ { * } } } \\ { { \delta Y } } & { { = } } & { { Y - Y ^ { * } , } } \end{array}
$$

we can write Eq. (1.2.14) as

$$
\begin{array} { r l r } { \delta \rho } & { = } & { \left[ \frac { \partial \rho } { \partial X } \right] ^ { * } \delta X + \left[ \frac { \partial \rho } { \partial Y } \right] ^ { * } \delta Y + \epsilon _ { \rho } } \\ { \delta \theta } & { = } & { \left[ \frac { \partial \theta } { \partial X } \right] ^ { * } \delta X + \left[ \frac { \partial \theta } { \partial Y } \right] ^ { * } \delta Y + \epsilon _ { \theta } . } \end{array}
$$

The symbol $[ ] ^ { * }$ indicates that the value in brackets is evaluated along the nominal trajectory. In Eq. (1.2.16), terms of order higher than the first in the state deviation values have been neglected assuming that these deviations are small. This requires that the reference trajectory and the true trajectory be close at all times in the interval of interest. Now, if the following definitions are used,

$$
\begin{array} { l c l } { { { \bf y } ^ { T } } } & { { \equiv } } & { { \left[ \delta \rho \delta \theta \right] } } \\ { { } } & { { } } & { { } } \\ { { { \widetilde { H } } } } & { { { \equiv } } } &  { { \left[ \begin{array} { c } { { { \left[ \frac { \partial \rho } { \partial X } \right] } ^ { * } } } \\ { { \left[ \frac { \partial \theta } { \partial X } \right] } ^ { * } } \end{array} \begin{array} { c c c c } { { \left[ \frac { \partial \rho } { \partial Y } \right] } ^ { * } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { \left[ \frac { \partial \theta } { \partial Y } \right] } ^ { * } } & { { 0 } } & { { 0 } } & { { 0 } } \end{array} \right] } } \\ { { { \bf x } ^ { T } } } & { { \equiv } } & { { \left[ \delta X \delta Y \delta { \dot { X } } \delta { \dot { Y } } \delta { g } \right] } } \\ { { } } & { { } } & { { } } \\ { { \epsilon ^ { T } } } & { { \equiv } } & { { \left[ \epsilon _ { \rho } \epsilon _ { \theta } \right] , } } \end{array}
$$

then Eq. (1.2.16) can be expressed as the matrix equation,

$$
\begin{array} { r } { \mathbf { y } = \widetilde { H } \mathbf { x } + \boldsymbol { \epsilon } . } \end{array}
$$

In Eq. (1.2.18), y is called the observation deviation vector, $\mathbf { x }$ is the state deviation vector, $\bar { H }$ is a mapping matrix that relates the observation deviation vector Hto the state deviation vector, and $\epsilon$ is a random vector that represents the noise or error in the observations. It is common practice to refer to $\mathbf { x }$ and $\mathbf { y }$ as the state and observation vectors, respectively, even though they really represent deviations from nominal values.

# 1.2.5 STATE TRANSITION MATRIX

The matrix multiplying the initial state vector in Eq. (1.2.12) is referred to as the state transition matrix, $\Phi ( t , t _ { 0 } )$ . For the state deviation vector, $\mathbf { x }$ , defined in Eq. (1.2.17), this matrix is given by

$$
\begin{array} { r l r } { \Phi ( t , t _ { 0 } ) } & { = } & { \left[ \begin{array} { c c c c c } { 1 } & { 0 } & { t } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { t } & { - t ^ { 2 } / 2 } \\ { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } & { - t } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right] . } \end{array}
$$

The state transition matrix maps deviations in the state vector from one time to another. In this case, deviations in the state are mapped from $t _ { 0 }$ to $t$ . Note that we have arbitrarily set $t _ { 0 } = 0$ t t. For this linear example, the mapping is exact, but tin the general orbit determination case, the state equations will be nonlinear, and the state transition matrix is the linear term in a Taylor series expansion of the state vector at time $t$ about the state vector at a reference time $t _ { 0 }$ . Hence, the state t tdeviation vector and observation deviation vector at any time can be written in

terms of $\mathbf { x } _ { \mathrm { 0 } }$ , as follows:

$$
\begin{array} { r } { \mathbf { x } ( t ) = \Phi ( t , t _ { 0 } ) \mathbf { x } _ { 0 } } \\ { \mathbf { y } ( t ) = \widetilde { H } ( t ) \mathbf { x } ( t ) + \pmb { \epsilon } ( t ) . } \end{array}
$$

$\mathbf { y } ( t )$ can be written in terms of $\mathbf { x } _ { \mathrm { 0 } }$ as

$$
\mathbf { y } ( t ) = H ( t ) \mathbf { x } _ { 0 } + \epsilon ( t ) ,
$$

where

$$
H ( t ) = \widetilde { H } ( t ) \Phi ( t , t _ { 0 } ) .
$$

The problem that remains now is to determine the best estimate of $\mathbf { x } _ { \mathrm { 0 } }$ given the linearized system represented by Eqs. (1.2.20) and (1.2.21). Our problem can now be summarized as follows. Given an arbitrary epoch, $t _ { k }$ , and the state propagation equation and observation-state relationship

$$
\begin{array} { r } { { \mathbf { x } } ( t ) = \Phi ( t , t _ { k } ) { \mathbf { x } } _ { k } } \\ { { \mathbf { y } } = H { \mathbf { x } } _ { k } + \epsilon , } \end{array}
$$

find the “best” estimate of $\mathbf { x } _ { k }$ . In Eq. (1.2.23), y is an $m \times 1$ vector, $\mathbf { x }$ is an $n \times 1$ vector, $\epsilon$ is an $m \times 1$ vector, and $H$ is an $m \times n$ m nmapping matrix, where $n$ is mthe number of state variables and $m$ m nis the total number of observations. If $m$ is msufficiently large, the essential condition $m \geq n$ is satisfied.

m nIn contrast to the algebraic solutions described earlier in this chapter, the system represented by the second of Eq. (1.2.23) is always underdetermined. That is, there are $m$ -knowns (e.g., the observation deviations, y) and $m + n$ unknowns (e.g., the $m$ -observation errors, $\epsilon$ , and the $n$ -unknown components of the state mdeviation vector, $\mathbf { x } _ { k }$ n). In Chapter 4, several approaches for resolving this problem are discussed. The most straightforward is based on the method of least squares as proposed by Gauss (1809). In this approach, the best estimate for the unknown state vector, $\mathbf { x } _ { k }$ , is selected as the value $\hat { \mathbf { x } } _ { k }$ , which minimizes the sum of the squares of the calculated values of the observations errors. That is, if $\mathbf { x } _ { k } ^ { 0 }$ is any value of $\mathbf { x } _ { k }$ , then $\boldsymbol { \epsilon } ^ { 0 } = \mathbf { y } - H \mathbf { x } _ { k } ^ { 0 }$ will be the $m$ -calculated values of the observa-Htion residuals corresponding to the value $\mathbf { x } _ { k } ^ { 0 }$ m. Then, the best estimate of $\mathbf { x } _ { k }$ will be the value that leads to a minimal value of the performance index, $J ( \mathbf { x } _ { k } ^ { 0 } )$ , where

$$
J ( \mathbf { x } _ { k } ^ { 0 } ) = 1 / 2 ( \epsilon ^ { 0 T } \epsilon ^ { 0 } ) = 1 / 2 ( \mathbf { y } - H \mathbf { x } _ { k } ^ { 0 } ) ^ { T } ( \mathbf { y } - H \mathbf { x } _ { k } ^ { 0 } ) .
$$

For a minimum of this quantity, it is necessary and sufficient that

$$
 \frac { \partial J } { \partial \mathbf { x } _ { k } ^ { 0 } } | _ { \hat { \mathbf { x } } _ { k } } = 0 ; ~ \delta \mathbf { x } _ { k } ^ { 0 ^ { T } } \frac { \partial ^ { 2 } J } { \partial \mathbf { x } _ { k } ^ { 0 } \partial \mathbf { x } _ { k } ^ { 0 } } | _ { \hat { \mathbf { x } } _ { x } } \delta \mathbf { x } _ { k } ^ { 0 } > 0 .
$$

From the first of the conditions given by Eq. (1.2.25), it follows that

$$
( \mathbf { y } - H \hat { \mathbf { x } } _ { k } ) ^ { T } H = 0
$$

or by rearranging that

$$
H ^ { T } H \hat { \mathbf { x } } _ { k } = H ^ { T } \mathbf { y } .
$$

If the $n \times n$ matrix $( H ^ { T } H )$ has an inverse, the solution can be expressed as

$$
\begin{array} { r } { \hat { \mathbf x } _ { k } = ( H ^ { T } H ) ^ { - 1 } H ^ { T } \mathbf y . } \end{array}
$$
