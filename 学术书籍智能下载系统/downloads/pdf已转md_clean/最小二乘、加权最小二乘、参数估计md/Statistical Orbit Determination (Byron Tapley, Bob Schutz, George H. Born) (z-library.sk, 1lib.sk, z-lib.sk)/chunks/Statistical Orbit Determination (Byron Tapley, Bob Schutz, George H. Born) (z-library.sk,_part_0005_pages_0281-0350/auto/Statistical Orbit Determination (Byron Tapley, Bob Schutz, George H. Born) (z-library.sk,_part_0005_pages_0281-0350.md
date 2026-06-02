where

$$
\Phi ( t _ { k } , t _ { k } ) = I ,
$$

show that

$$
\begin{array} { r l } & { \dot { \Phi } ( t _ { i } , t _ { k } ) = A ( t _ { i } ) \Phi ( t _ { i } , t _ { k } ) } \\ & { \Phi ( t _ { i } , t _ { j } ) = \Phi ( t _ { i } , t _ { k } ) \Phi ( t _ { k } , t _ { j } ) } \\ & { \Phi ^ { - 1 } ( t _ { i } , t _ { k } ) = \Phi ( t _ { k } , t _ { i } ) } \\ & { \dot { \Phi } ^ { - 1 } ( t _ { i } , t _ { k } ) = - \Phi ^ { - 1 } ( t _ { i } , t _ { k } ) A ( t _ { i } ) . } \end{array}
$$

(3) Given a vector of observations, $\mathbf { y } = H \mathbf { x } + \epsilon$ with weighting matrix $W$ , and $a$ priori information, $( \overline { { \mathbf { x } } } , \overline { { W } } )$ , determine the least squares estimate for $\hat { \bf x }$ . (Note that $W$ corresponds to $R ^ { - 1 }$ and $\overline { W }$ to $\bar { P } _ { 0 } ^ { - 1 }$ in the case where we have statistical information on $\epsilon$ and $\bar { \bf x }$ .) Let the performance index be

$$
J ( x ) = 1 / 2 ~ \epsilon ^ { T } W \epsilon + 1 / 2 ~ \overline { { { \eta } } } ^ { T } \overline { { { W } } } \overline { { { \eta } } }
$$

where $\overline { { \eta } }$ is the error in the $a$ priori estimate $\overline { { \mathbf { x } } }$ ,

$$
\overline { { \pmb { \eta } } } = \overline { { \bf x } } - { \bf x } .
$$

Answer: $\hat { \mathbf { x } } = ( H ^ { T } W H + \overline { { W } } ) ^ { - 1 } ( H ^ { T } W \mathbf { y } + \overline { { W } } \overline { { \mathbf { x } } } )$

(4) Determine the state transition matrix associated with the matrix

$$
A = \left[ \begin{array} { c c } { { a } } & { { 0 } } \\ { { b } } & { { g } } \end{array} \right] , a \neq g , \mathrm { a n d } \dot { \Phi } = A \Phi , \Phi \left( t _ { 0 } , t _ { 0 } \right) = I .
$$

(5) Express the linear system of equations

$$
{ \ddot { x } } = - a b x
$$

in the matrix form

$$
{ \dot { \mathbf { x } } } = A \mathbf { x } ,
$$

where

$$
\mathbf { x } = { \left[ \begin{array} { l } { x } \\ { \dot { x } } \end{array} \right] } .
$$

Find the state transition matrix for this system.

(6) Show that the matrix

$$
\Phi \left( t , t _ { 0 } \right) = { \left[ \begin{array} { l l } { 3 e ^ { a t } } & { 0 } \\ { 0 } & { 2 e ^ { - b t } } \end{array} \right] }
$$

satisfies the relation

$$
{ \dot { \Phi } } = A \Phi
$$

but that $\Phi ( t , t _ { 0 } )$ is not a transition matrix. (Assume $t _ { 0 } = 0$ .)

(7) Show that whenever $\Phi ( t , t _ { k } )$ satisfies Eq. (4.2.22), it is symplectic; that is, $\Phi ( t , t _ { k } ) ^ { T } J \phi ( t , t _ { k } ) = J$ .

(8) The displacement of a particle, under the influence of a constant acceleration $\ddot { x } _ { 0 }$ , can be expressed as

$$
x ( t ) = x _ { 0 } + \dot { x } _ { 0 } t + \frac { 1 } { 2 } \ddot { x } _ { 0 } t ^ { 2 } ,
$$

where $x _ { 0 }$ is the initial displacement, ${ \dot { x } } _ { 0 }$ is the initial velocity, and $\ddot { x } _ { 0 }$ is the acceleration at the initial time, $t _ { 0 } = 0$ .

(a) By successive differentiation of this expression, show that the linear system

$$
{ \dot { \mathbf { x } } } = A \mathbf { x }
$$

describes the motion, where

$$
\mathbf { x } = { \left[ \begin{array} { l } { x } \\ { \dot { x } } \\ { \ddot { x } } \end{array} \right] } \ ; A = { \left[ \begin{array} { l } { 0 1 0 } \\ { 0 0 1 } \\ { 0 0 0 } \end{array} \right] } \ .
$$

(b) Prove that the transition matrix $\Phi ( t , t _ { 0 } )$ of the system in (a) is

$$
\Phi ( t , t _ { 0 } ) = \left[ \begin{array} { c c c } { { 1 } } & { { ( t - t _ { 0 } ) } } & { { ( t - t _ { 0 } ) ^ { 2 } / 2 } } \\ { { 0 } } & { { 1 } } & { { ( t - t _ { 0 } ) } } \\ { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right]
$$

first by differentiating $\Phi$ and showing that $\dot { \Phi } ( t , t _ { 0 } ) = A \Phi ( t , t _ { 0 } )$ where $\Phi ( t _ { 0 } , t _ { 0 } ) = I$ , and then by integrating this system of differential equations.

(c) Show that $\Phi ( t , t _ { 0 } )$ can be represented as

$$
\begin{array} { l } { \displaystyle \Phi ( t , t _ { 0 } ) = e ^ { A ( t - t _ { 0 } ) } } \\ { \displaystyle = I + \sum _ { n = 1 } ^ { \infty } \frac { 1 } { n ! } A ^ { n } ( t - t _ { 0 } ) ^ { n } . } \end{array}
$$

(d) Calculate $\Phi \left( t _ { 0 } , t \right)$ by direct inversion.

(e) Let $\Phi ^ { - 1 } ( t , t _ { 0 } ) = \Theta ( t , t _ { 0 } )$ and show that

$$
\dot { \Theta } ( t , t _ { 0 } ) = - \Theta ( t , t _ { 0 } ) A , \Theta \left( t _ { 0 } , t _ { 0 } \right) = I
$$

by integration and comparison with the results of $d$ .

(f) Calculate $\Phi \left( t _ { 2 } , t _ { 1 } \right)$ by finding the product $\Phi \left( t _ { 2 } , t _ { 0 } \right) \Phi \left( t _ { 0 } , t _ { 1 } \right)$ .

(g) Compare this result with the result obtained by integrating the equation

$$
\dot { \Phi } \left( t , t _ { 1 } \right) = A \Phi \left( t , t _ { 1 } \right) ,
$$

with the condition $\Phi \left( t _ { 1 } , t _ { 1 } \right) = I$ .

(h) Show that

$$
\frac { \partial \mathbf { x } } { \partial \mathbf { x } _ { 0 } } = \Phi \left( t , t _ { 0 } \right) ,
$$

where ${ \bf x } ^ { T } = ( x \dot { x } \ddot { x } )$ and $\mathbf { x } _ { 0 } ^ { T } = \left( x _ { 0 } \ \dot { x } _ { 0 } \ \ddot { x } _ { 0 } \right)$ .

(9) The equations of motion for a satellite moving in the vicinity of a body with a homogeneous mass distribution can be expressed as

$$
{ \ddot { \mathbf { r } } } = - { \frac { \mu \mathbf { r } } { r ^ { 3 } } }
$$

where $\mathbf { r }$ is the position vector, $\ddot { \mathbf { r } }$ is the acceleration vector, and where $r =$ $| \mathbf { r } |$ . Let ${ \textbf { v } } = { \dot { \textbf { r } } }$ denote the velocity vector, and express the equations in first-order form as

$$
\left[ \dot { \bar { \mathbf { r } } } \right] = \left[ \begin{array} { c } { \mathbf { v } } \\ { \dot { \mathbf { v } } } \end{array} \right] .
$$

(a) The relations that define the deviations from a given reference orbit due to deviations in $\mathbf { r }$ and $\mathbf { v }$ and $\mu$ at a given time $t _ { 0 }$ can be used to analyze the trajectory sensitivity. Show that

$$
{ \frac { d } { d t } } \left[ \delta \mathbf { r } \right] = { \left[ \begin{array} { l l } { ~ 0 } & { I } \\ { { \frac { \partial \mathbf { f } } { \partial \mathbf { r } } } } & { ~ 0 } \end{array} \right] } \left[ { \begin{array} { l } { \delta \mathbf { r } } \\ { \delta \mathbf { v } } \end{array} } \right] - \left[ { \begin{array} { l } { 0 } \\ { \mathbf { r } } \\ { r ^ { 3 } } \end{array} } \right] \delta \mu ,
$$

where

$$
\mathbf { f } = - { \frac { \mu \mathbf { r } } { r ^ { 3 } } }
$$

$$
- \frac { \partial \mathbf { f } } { \partial \mathbf { r } } = \left[ \begin{array} { c c c c } { \frac { \mu } { r ^ { 3 } } - 3 \mu \frac { x _ { 1 } ^ { 2 } } { r ^ { 5 } } } & { - 3 \mu \frac { x _ { 1 } x _ { 2 } } { r ^ { 5 } } } & { - 3 \mu \frac { x _ { 1 } x _ { 3 } } { r ^ { 5 } } } \\ { - 3 \mu \frac { x _ { 1 } x _ { 2 } } { r ^ { 5 } } } & { \frac { \mu } { r ^ { 3 } } - 3 \mu \frac { x _ { 2 } ^ { 2 } } { r ^ { 5 } } } & { - 3 \mu \frac { x _ { 2 } x _ { 3 } } { r ^ { 5 } } } \\ { - 3 \mu \frac { x _ { 1 } x _ { 3 } } { r ^ { 5 } } } & { - 3 \mu \frac { x _ { 2 } x _ { 3 } } { r ^ { 5 } } } & { \frac { \mu } { r ^ { 3 } } - 3 \mu \frac { x _ { 3 } ^ { 2 } } { r ^ { 5 } } } \end{array} \right] .
$$

Note that $\partial \mathbf { f } / \partial \mathbf { r }$ is symmetric.

(b) The constant $\mu$ is a physical constant and $\delta \mu$ represents the error in the knowledge of $\mu$ . Show that the error in $\mathbf { r } ( t )$ and $\mathbf { v } ( t )$ can be related to the error in $\mu$ by the following expression (Hint: Use the solution for $x ( t )$ given by Eq. (4.9.14).):

$$
{ \bigg [ } \delta \mathbf { r } ( t ) { \bigg ] } = \Phi ( t , t _ { 0 } ) { \bigg [ } { \delta \mathbf { r } _ { 0 } } { \bigg ] } - \delta \mu \int _ { t _ { 0 } } ^ { t } \Phi ( t , \tau ) { \left[ \begin{array} { l } { 0 } \\ { \mathbf { r } } \\ { r ^ { 3 } } \end{array} \right] } d \tau .
$$

(10) Assume an orbit plane coordinate system for Exercise 9 with $\mu = 1$ .

(a) Generate a “true” solution by numerically integrating the resulting differential equations

$$
\begin{array} { c } { \ddot { x } = - \displaystyle \frac { x } { r ^ { 3 } } } \\ { \ddot { y } = - \displaystyle \frac { y } { r ^ { 3 } } } \\ { r ^ { 2 } = x ^ { 2 } + y ^ { 2 } } \end{array}
$$

for the initial conditions

$$
\begin{array} { r } { \mathbf { X } ( t _ { 0 } ) = \left( \begin{array} { l } { x } \\ { y } \\ { \dot { x } } \\ { \dot { y } } \end{array} \right) _ { t = t _ { 0 } } = \left( \begin{array} { l } { 1 . 0 } \\ { 0 . 0 } \\ { 0 . 0 } \\ { 1 . 0 } \end{array} \right) . } \end{array}
$$

Save the values of the state vector $\mathbf { X } ( t _ { i } )$ for $t _ { i } = i * 1 0 . ; i = 0 , \ldots , 1 0$

(b) Perturb the previous set of initial conditions by an amount

$$
\mathbf { X } ^ { * } ( t _ { 0 } ) = \mathbf { X } ( t _ { 0 } ) - \delta \mathbf { X } ( t _ { 0 } )
$$

where

$$
\delta { \bf X } ( t _ { 0 } ) = \left( \begin{array} { c } { { 1 \times 1 0 ^ { - 6 } } } \\ { { - 1 \times 1 0 ^ { - 6 } } } \\ { { 1 \times 1 0 ^ { - 6 } } } \\ { { 1 \times 1 0 ^ { - 6 } } } \end{array} \right)
$$

and numerically integrate this “nomina l” trajectory along with the associated state transition matrix to find $\mathbf { X } ^ { * } ( t _ { i } )$ and $\Phi ( t _ { i } , t _ { 0 } )$ at $t _ { i } =$ $i * 1 0 . ; i = 0 , \dots , 1 0$ .

(c) For this problem, $\Phi ( t _ { i } , t _ { 0 } )$ is symplectic. Demonstrate this for $\Phi ( t _ { 1 0 0 } , t _ { 0 } )$ by multiplying it by $\Phi ^ { - 1 } ( t _ { 1 0 0 } , t _ { 0 } )$ , given by Eq. (4.2.22), and showing that the result is the identity matrix.

(d) Calculate the perturbation vector, $\delta { \bf X } ( t _ { i } )$ , by the following two methods:

$$
\begin{array} { r c l } { \delta \mathbf { X } ( t _ { i } ) = \mathbf { X } ( t _ { i } ) - \mathbf { X } ^ { * } ( t _ { i } ) } \\ { \delta \mathbf { X } ( t _ { i } ) = \Phi ( t _ { i } , t _ { 0 } ) \delta \mathbf { X } ( t _ { 0 } ) } \end{array}
$$

and compare the results of (1) and (2). A program such as Matlab works well for this problem.

(11) Show that if the acceleration on a spacecraft is derivable from a potential function,

$$
\ddot { \mathbf { r } } = \nabla U
$$

then the state transition matrix is symplectic; that is, Eq. (4.2.13) is true under the assumption that the state vector is

$$
\mathbf { x } = { \left[ \begin{array} { l } { \mathbf { r } } \\ { \mathbf { v } } \end{array} \right] } .
$$

(12) Given the spring-mass system, as shown,

![](images/748b6c26ef474be8c79cd7ffda227ab4229baebc628be89b83c37ffac827ff47.jpg)

$$
m { \ddot { x } } + c { \dot { x } } + k x + F \sin \omega t = 0 .
$$

Assume that we wish to estimate $x , \dot { x } , F , c$ , and $h$ using observations $\rho$ .   
Derive the $A$ and $\widetilde { H }$ matrix for this state vector.

(13) Given a point mass falling under the acceleration of gravity and being observed by range observations, $\rho$ , as shown. Determine the state transition matrix, and the $\widetilde { H }$ and $H$ matrices. Assume the state vector is to be estimated at $t _ { 0 } = 0$ .

![](images/96f2a59c0c4e37b50ed9365cbeb259df85732dbf9a966a661ab37f5045d21f35.jpg)

$$
\begin{array} { r } { \operatorname { l e t } { \mathbf { X } } = \left[ \begin{array} { l } { \begin{array} { l } { x } \\ { y } \\ { \dot { x } } \\ { \dot { y } } \\ { g } \\ { \dot { y } } \end{array} } \right] , \qquad \stackrel { \circledast } { \begin{array} { l } { ( } 0 . ~ t _ { 0 } ) } \\ { x = x _ { 0 } } \\ { \dot { x } = \dot { x } _ { 0 } } \\ { { y } = y _ { 0 } } \\ { \dot { y } = \dot { y } _ { 0 } } \end{array} }  \end{array} \end{array}
$$

(14) Given a simple pendulum with range observations $| \rho |$ , from a fix ed point, as shown in the figure.

(a) Write the equations of motion and form the observation-state matrix $\widetilde { \boldsymbol { H } } )$ and the state propagation matrix $( A )$ . Assume the state vector is

$$
\mathbf { X } = \left[ { \stackrel { \ominus } { \ominus } } \right] .
$$

(b) Assume small oscillations; that is, $\sin \Theta \approx \Theta$ , $\cos \Theta \approx 1$ . Solve the equations of motion and derive expressions for the state transition matrix.

(c) How does the assumption that $\Theta$ is small differ from a linearized formulation of this problem?

$$
\sum _ { \rho } ^ { | \star  } \sum _ { i = \pmb { \mathscr { S } } _ { 0 } } ^ { | \star  } x _ { 0 } \frac {  1 } {    } \sum _ { l } ^ { | \star  } {  \mathrm { a t } \ : t = t _ { 0 } , \Theta = \Theta _ { 0 } , \dot { \Theta } = \dot { \Theta } _ { 0 } \vphantom { | \star | } }
$$

(d) Write a computer program to process range observations of the pendulum mass using both a batch processor and a sequential filt er.   
(e) Generate a set of observations and process these observations using both the batch and sequential estimation algorithms. Use both perfect observations and observations with random noise.

(15) Write a computer program to process range and range-rate data for the spring-mass system of Section 4.8.2. Use the following data set (or create your own), which has Gaussian noise with mean zero and $\sigma _ { \rho } = 0 . 2 5 \mathrm { m }$ and $\sigma _ { \dot { \rho } } = 0 . 1 0 \mathrm { m / s }$ added. Use the same initial conditions given in Example 4.8.2. Use a weighting matrix, $W$ , that reflects the noise on the data,

$$
E [ \epsilon \epsilon ^ { T } ] = R = \left[ \begin{array} { c c } { \sigma _ { \rho } ^ { 2 } } & { 0 } \\ { 0 } & { \sigma _ { \dot { \rho } } ^ { 2 } } \end{array} \right] = \left[ \begin{array} { c c } { . 0 6 2 5 } & { 0 } \\ { 0 } & { . 0 1 } \end{array} \right] = W ^ { - 1 } .
$$

Observation Data   

<table><tr><td>Time</td><td>p(m)</td><td>p(m/s)</td></tr><tr><td>0.00</td><td>6.37687486186586</td><td>-0.00317546143535849</td></tr><tr><td>1.00</td><td>5.50318198665912</td><td>1.17587430814596</td></tr><tr><td>2.00</td><td>5.94513302809067</td><td>-1.47058865193489</td></tr><tr><td>3.00</td><td>6.30210798411686</td><td>0.489030779000695</td></tr><tr><td>4.00</td><td>5.19084347133671</td><td>0.993054430595876</td></tr><tr><td>5.00</td><td>6.31368240334678</td><td>-1.40470245576321</td></tr><tr><td>6.00</td><td>5.80399842220377</td><td>0.939807575607138</td></tr><tr><td>7.00</td><td>5.45115048359871</td><td>0.425908088320457</td></tr><tr><td>8.00</td><td>5.91089305965839</td><td>-1.47604467619908</td></tr><tr><td>9.00</td><td>5.6769731201352</td><td>1.42173765213734</td></tr><tr><td>10.00</td><td>5.25263404969825</td><td>-0.12082311844776</td></tr></table>

Answer after three iterations:

$$
\begin{array} { r l } & { x _ { 0 } = 2 . 9 5 7 1 m , \quad v _ { 0 } = - 0 . 1 2 6 0 m / s } \\ & { \rho _ { \mathrm { R M S } } = 0 . 2 4 7 m , \dot { \rho } _ { \mathrm { R M S } } = 0 . 0 8 7 5 m / s } \\ & { \sigma _ { x _ { 0 } } = 0 . 0 4 5 0 m , \sigma _ { v _ { 0 } } = 0 . 0 7 9 4 m / s , \rho _ { x _ { 0 } v _ { 0 } } = 0 . 0 4 2 6 } \end{array}
$$

(16) Repeat Exercise 15, except program the sequential processor algorithm. Use the same initial conditions. Solve for the state at each observation time. Map the state estimate and covariance matrix from the final time to the initial time and show that they agree with the batch results.

(17) Given: The equation of motion of a particle moving in a uniform gravity field influence d by a resistive drag force; for example,

$$
m { \ddot { \mathbf { r } } } = - m g \mathbf { j } - m \mathbf { D }
$$

where

$$
\mathbf { D } = { \frac { 1 } { 2 } } \rho \beta { \dot { r } } { \dot { \mathbf { r } } } ,
$$

and the sequence of observations

$$
\rho _ { i } = \sqrt { ( x - x _ { s } ) _ { i } ^ { 2 } + ( y - y _ { s } ) _ { i } ^ { 2 } } i = 1 , \ldots , m .
$$

![](images/6c5144d08f24c3208f3a974288775c80304639643aea455b8cccee83040c7753.jpg)

Set up the necessary equations to estimate the initial position and velocity of the particle assuming that $\beta$ and $x _ { s }$ , $y _ { s }$ are unknown but constant forcemodel and measurement-model parameters to be estimated. Discuss the conditions necessary to ensure complete parameter observability.

(18) Given the following dynamic system

$$
\begin{array} { l } { \ddot { x } = - k x - \beta x ^ { 2 } + c \sin \omega t } \\ { \rho _ { i } = \sqrt { d ^ { 2 } + ( \ell + x _ { i } ) ^ { 2 } } + \epsilon _ { i } ; i = 1 , \dots , m . } \end{array}
$$

$$
E [ \epsilon _ { i } ] = 0 , ~ E [ \epsilon _ { i } \epsilon _ { j } ] = \sigma _ { i } ^ { 2 } \delta _ { i j }
$$

Set up all necessary equations for sequentially estimating the position and velocity of the system from observations $( \rho _ { i } )$ . Assume that $[ d , \ell , k , \beta , c ]$ are unknowns to be estimated. State clearly all information that must be given as input information beyond what is given in the problem statement.

(19) Given the observation-state relation

$$
y ( t ) = \sum _ { i = 1 } ^ { 3 } ( t ) ^ { i } x _ { i } ,
$$

and the observation sequence at $t = 1$ , $y \left( 1 \right) = 2$ , and at $t = 2 , \ y ( 2 ) = 1$ .

Find the “bes t” estimate of $\mathbf { x } _ { i }$ , $i = 1$ , 2, 3. (Hint: There are fewer observations than unknowns, so use the minimum norm solution.)

(20) Given the observation state relation ${ \bf y } = H \boldsymbol { x } + \epsilon$ , where $x$ is a scalar and given that

$$
\begin{array} { r l } & { \mathbf { y } = \left[ \mathbf { 1 } \right] , } \\ & { \mathbf { y } = \left[ \mathbf { 2 } \right] , \mathrm { ~ a n d ~ } E [ \epsilon ] = 0 , } \\ & { \mathbf { R } = E \left[ \epsilon \epsilon ^ { T } \right] = \left[ \begin{array} { l l l } { \frac { 1 } { 2 } } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] , H = \left[ \begin{array} { l } { 1 } \\ { 1 } \\ { 1 } \end{array} \right] } \end{array}
$$

with a priori information, ${ \overline { { x } } } = 2$ and $\begin{array} { r } { \sigma ^ { 2 } ( \overline { { x } } ) = \frac { 1 } { 2 } } \end{array}$ .

(a) Using $R ^ { - 1 }$ as the weighting matrix, find $\hat { x }$ using the batch processing algorithm.   
(b) What is the standard deviation of the estimation error associated with ${ \hat { x } } ?$   
(c) What is the best estimate of the observation error, ˆ-?

(21) Given the system

$$
\begin{array} { l } { { \displaystyle x ( t ) = x _ { 0 } + \dot { x } _ { 0 } t + \frac { 1 } { 2 } \ddot { x } _ { 0 } t ^ { 2 } ; t _ { 0 } = 0 \nonumber } } \\ { { \dot { x } ( t ) = \dot { x } _ { 0 } + \ddot { x } _ { 0 } t } } \\ { { \ddot { x } ( t ) = \ddot { x } _ { 0 } } } \end{array}
$$

with

$$
\mathbf { X } ( t ) = \left[ \begin{array} { l } { x } \\ { \dot { x } } \\ { \ddot { x } } \end{array} \right] , \overline { { P } } _ { 0 } = \left[ \begin{array} { l l l } { 4 } & { 0 } & { 0 } \\ { 0 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] , \overline { { \mathbf { X } } } ( t _ { 0 } ) = \left[ \begin{array} { l } { 1 } \\ { 1 } \\ { 1 } \end{array} \right] .
$$

At $t _ { 1 } = 1$ , an observation of $x ( t )$ is made; that is, $Y ( t _ { 1 } ) = x ( t _ { 1 } ) = 2$ . The variance of the error in $Y ( t _ { 1 } )$ is $\sigma ^ { 2 } ( \epsilon _ { Y } ) = 1$ .

(a) Compute $\hat { \mathbf X } ( t _ { 0 } )$ using the batch processing algorithm. Answer:

$$
\hat { \mathbf { X } } ( t _ { 0 } ) = \left[ \begin{array} { l } { 2 1 / 2 9 } \\ { 2 5 / 2 9 } \\ { 2 8 / 2 9 } \end{array} \right]
$$

(b) Using the sequential processing algorithm, determine $\hat { \mathbf X } ( t _ { 0 } )$ . Remember you are to solve for $\hat { \mathbf X } ( t _ { 0 } )$ , not $\hat { \mathbf X } ( t _ { 1 } )$ . You should get identical results to part a.

(c) Compute $\hat { \mathbf X } ( t _ { 1 } )$ using the sequential algorithm, then map $\hat { \mathbf X } ( t _ { 1 } )$ to $t _ { 0 }$ using the state transition matrix. You should get the same value of $\hat { \mathbf { X } } ( t _ { 0 } )$ as you computed in parts a and b.

Answer:

$$
\begin{array} { r } { \hat { \mathbf { X } } ( t _ { 1 } ) = \left[ \begin{array} { l } { 6 0 / 2 9 } \\ { 5 3 / 2 9 } \\ { 2 8 / 2 9 } \end{array} \right] } \end{array}
$$

(22) Assume a vehicle is moving along a rectilinear path with a constant acceleration. The generic equation of motion is

$$
x ( t ) = x _ { 0 } \ + v _ { 0 } t + \frac { 1 } { 2 } a t ^ { 2 } .
$$

At discrete constant intervals of time $t = t _ { i } , i = 0 , 1 , 2 , 3 \ldots 1 0$ the position and velocity of the vehicle are observed.

(a) Set up a flo w chart for the batch and sequential estimation algorithm to estimate a state vector consisting of the position, velocity, and acceleration. For the batch algorithm estimate the state at $t _ { 0 }$ , and for the sequential estimate the state at $t _ { i }$ .   
(b) Write a program (using Matlab or a similar software package) to solve for the state vector using the batch processor. Include an a priori covariance matrix and a measurement weighting matrix and the capability to map the state estimate and the estimation error covariance matrix from the epoch to any desired time. Generate a sequence of simulated observations to which random noise is added. Solve for the state vector and associated covariance matrix at $t _ { 0 }$ . Map these quantities to the final time for comparison with results from the sequential processor in part c.   
(c) Repeat part b for the sequential processor and estimate the state at $t _ { i }$ , $i = 1 \dots 1 0$ . Compare results at the final measurement time with the mapped results of the batch solution of part b.   
(d) Experiment with your program by changing the a priori covariance and weighting matrix. Write a brief report describing your results.

(23) For the problem posed in Section 4.7.1:

(a) Show that the exact value for $P _ { 2 }$ is given by Eq. (4.7.24).

(b) Under the assumption that $1 + \epsilon ^ { 2 } = 1$ , show that the conventional Kalman filt er yields

$$
P _ { 2 } = \frac { 1 } { 1 - 2 \epsilon } \left[ \begin{array} { r r } { - 1 } & { 1 } \\ { 1 } & { - 1 } \end{array} \right] .
$$

(c) Under the assumption that $1 + \epsilon ^ { 2 } = 1 $ , show that the batch processor yields

$$
P _ { 2 } = \frac { 1 } { 1 - 2 \epsilon } \left[ \begin{array} { c c } { { 1 } } & { { - ( 1 + \epsilon ) } } \\ { { - ( 1 + \epsilon ) } } & { { 2 } } \end{array} \right] = \left[ \begin{array} { c c } { { 1 + 2 \epsilon } } & { { - ( 1 + 3 \epsilon ) } } \\ { { - ( 1 + 3 \epsilon ) } } & { { 2 ( 1 + 2 \epsilon ) } } \end{array} \right] ,
$$

which agrees with the exact result to $O ( \epsilon )$ , thus illustrating the improved numerical behavior of the batch over the sequential processor.

(24) Two observations are taken of the parameter $x$ ,

$$
y _ { 1 } = x + \epsilon _ { 1 } , y _ { 2 } = x + \epsilon _ { 2 } ,
$$

where $\epsilon _ { 1 }$ and $\epsilon _ { 2 }$ are zero mean random noise. It is known that the variance of $\epsilon _ { 2 }$ is twice the variance of $\epsilon _ { 1 }$ . Determine the weighted least squares estimate of $x$ .

(25) Derive the following two equations for the estimation error covariance matrix:

(a) Beginning with Eq. (4.4.29), derive the expression for the estimation error covariance matrix given by Eq. (4.4.30). Assume that

$$
E \left[ ( \bar { \bf x } - { \bf x } ) \epsilon ^ { T } \right] = 0 .
$$

(b) Beginning with the equation for $\hat { \bf x }$ (Eq. 4.7.16), derive the Joseph formulation for the measurement update of the estimation error covariance matrix given by Eq. (4.7.19).

(c) Show that the Joseph formulation for the measurement update of $P$ is equivalent to the conventional Kalman update given by Eq. (4.7.18),

$$
P = ( I - K { \widetilde { H } } ) { \overline { { P } } } .
$$

(26) For the joint density function given by Eq. (4.5.4),

(a) Determine the MLE of $\sigma$ .

(b) Show that the MLE of $\alpha$ given by Eq. (4.5.8) is unbiased.

(27) Let $\mathbf { X } = [ x _ { 1 } x _ { 2 } \dots x _ { n } ] ^ { T }$ have a multivariate Gaussian distribution with each component of $\mathbf { X }$ having the same (unknown) mean $\alpha$ ,

$$
f \left( \mathbf { X } ; \alpha \right) = \frac { 1 } { ( 2 \pi ) ^ { n / 2 } | P | ^ { \frac { 1 } { 2 } } } \exp [ - \frac { 1 } { 2 } ( \mathbf { X } - A \alpha ) ^ { T } P ^ { - 1 } ( \mathbf { X } - A \alpha ) ]
$$

with

$$
A = { \left( \begin{array} { l } { 1 } \\ { 1 } \\ { \vdots } \\ { 1 } \end{array} \right) } ~ .
$$

(a) Identify the likelihood function and show that the expression for the maximum likelihood estimate of $\alpha$ is ${ \hat { \alpha } } = ( A ^ { T } P ^ { - 1 } { \bar { A ) } } ^ { - 1 } A ^ { T } P ^ { - 1 } \mathbf { X }$ . (b) Show that $\hat { \alpha }$ is an unbiased estimator of $\alpha$ .

(28) Given the estimator ${ \hat { \mathbf { x } } } = { \overline { { \mathbf { x } } } } + K \left( \mathbf { y } - H { \overline { { \mathbf { x } } } } \right)$ , state all necessary conditions on $\overline { { \mathbf { x } } }$ and $\mathbf { y }$ for $\hat { \bf x }$ to be an unbiased estimate of $\mathbf { x }$ .

(29) Given: Random variables $X$ and $Y$ and

$$
Y = a \pm b X
$$

where $a$ and $b$ are constants. Show that the correlation coeffic ient $\rho \left( X , Y \right)$ has the value

$$
\rho \left( X , Y \right) = \pm 1 .
$$

(30) Given that $\mathbf { x }$ is an $n \times 1$ vector of random variables with mean $\overline { { \mathbf { x } } }$ and covariance $P$ . Let $\mathbf { y }$ be an $m \times 1$ vector of random variables related to $\mathbf { x }$ by

$$
\mathbf { y } = H \mathbf { x } + \epsilon
$$

where $\epsilon$ is zero mean with covariance $R$ and is independent of $\mathbf { x }$ .

(a) Find the mean of y.

(b) Show that the variance-covariance of y is given by

$$
\begin{array} { c } { { P _ { y } = E \left[ ( { \bf y } - \overline { { { \bf y } } } ) ( { \bf y } - \overline { { { \bf y } } } ) ^ { T } \right] } } \\ { { { \bf \phi } = H P H ^ { T } + R . } } \end{array}
$$

(c) Show that the covariance of $\mathbf { x }$ and $\mathbf { y }$ is

$$
P _ { \bf x y } \equiv E [ ( { \bf x } - \overline { { \bf x } } ) ( { \bf y } - \overline { { \bf y } } ) ^ { T } ] = P H ^ { T } .
$$

(31) An estimate, $\hat { \bf x }$ is made of $\mathbf { x }$ (an $n \times 1$ vector), based on $m$ observations $\mathbf { y }$ $\mathbf { \chi } _ { m } > n \mathbf { \chi } ,$ ), where

$$
\mathbf { y } = H \mathbf { x } + \epsilon
$$

and

$$
\epsilon \mathrm { i s } N ( \overline { { \epsilon } } , R ) .
$$

An a priori value of $\mathbf { x }$ is given:

$$
{ \overline { { \mathbf { x } } } } = \mathbf { x } + \mathbf { e }
$$

where $\mathbf { e }$ is $N \left( 0 , { \overline { { P } } } \right)$ . Assume $E \left[ \mathbf { e } \epsilon ^ { T } \right] = 0$ .

The estimate is

$$
\hat { \mathbf { x } } = \overline { { \mathbf { x } } } + K ( \mathbf { y } - H \overline { { \mathbf { x } } } ) .
$$

(a) What is the bias for this estimator?

(b) What is the variance-covariance associated with the estimation error for $\hat { \mathbf { x } } ?$ Note that $\hat { \bf x }$ is biased so use the definition of $P$ given in the answer.

(c) Show that by redefining the noise vector to be $\epsilon = \overline { { \epsilon } } + \epsilon ^ { \prime }$ , and by including $\overline { { \epsilon } }$ in the state vector, an unbiased estimator may be formed. Assume that an a priori estimate of $\overline { { \epsilon } }$ with covariance $P _ { \overline { { \epsilon } } }$ is available.

# Answer:

(a) $E [ \hat { \mathbf { x } } ] = \mathbf { x } + K \overline { { \epsilon } } , \mathrm { b i a s } = K \bar { \epsilon }$ (b) $P = ( I - K H ) \overline { { P } } ( I - K H ) ^ { T } + K R K ^ { T }$ where

$$
R = E \left[ ( \epsilon - \overline { { \epsilon } } ) ( \epsilon - \overline { { \epsilon } } ) ^ { T } \right]
$$

and

$$
\begin{array} { l } { P \equiv E \left[ ( \tilde { \mathbf { e } } - E ( \tilde { \mathbf { e } } ) ) ( \tilde { \mathbf { e } } - E ( \tilde { \mathbf { e } } ) ) ^ { T } \right] } \\ { \tilde { \mathbf { e } } \equiv \hat { \mathbf { x } } - \mathbf { x } , E ( \tilde { \mathbf { e } } ) = K \overline { { \epsilon } } } \end{array}
$$

(32) Assuming we are given no $a$ priori information on $\hat { \bf x }$ ,

(a) show that there is no correlation between the residual observation error, $\hat { \mathbf { y } } - \mathbf { y } = \hat { \pmb { \epsilon } }$ , and the estimation error, $\hat { \mathbf { x } } - \mathbf { x }$ , that

$$
E \left[ \widehat { \epsilon } ( \widehat { \mathbf { x } } - \mathbf { x } ) ^ { T } \right] = 0 .
$$

If this were not zero, it would mean that we had not extracted all of the available information from the observations.

Hint: Use

$$
\begin{array} { r l } & { \hat { \mathbf { \epsilon } } = \mathbf { y } - H \hat { \mathbf { x } } } \\ & { \hat { \mathbf { x } } = ( H ^ { T } R ^ { - 1 } H ) ^ { - 1 } H ^ { T } R ^ { - 1 } \mathbf { y } } \\ & { \mathbf { y } = H \mathbf { x } + \mathbf { \epsilon } , \quad E [ \mathbf { \epsilon } ] = 0 , \quad E [ \mathbf { \epsilon } \mathbf { \epsilon } ^ { T } ] = R . } \end{array}
$$

(b) Assuming that a priori information is given; that is, $\bar { \mathbf { x } } = \mathbf { x } + \pmb { \eta }$ where $E [ \pmb { \eta } ] = 0 , E [ \pmb { \eta } \pmb { \eta } ^ { T } ] = \overline { { P } }$ and $E [ \epsilon \eta ^ { T } ] = 0$ . Show that $E [ \hat { \epsilon } ( \hat { \mathbf { x } } - \mathbf { x } ) ^ { T } ] =$ 0 is still true.

(33) Occasionally a priori information, $\overline { { \mathbf { x } } }$ and $\overline { { P } }$ , used to initiate a batch filter is obtained from processing an earlier batch of data so that the errors in $\overline { { \mathbf { x } } }$ and the observation error, $\epsilon$ , are correlated. Derive the expression for the covariance matrix of the estimation error, $P$ , assuming

$$
\begin{array} { r l } & { P = E \left[ ( \hat { \mathbf { x } } - \mathbf { x } ) ( \hat { \mathbf { x } } - \mathbf { x } ) ^ { T } \right] } \\ & { \hat { \mathbf { x } } = ( \overline { { P } } ^ { - 1 } + H ^ { T } R ^ { - 1 } H ) ^ { - 1 } ( \overline { { P } } ^ { - 1 } \overline { { \mathbf { x } } } + H ^ { T } R ^ { - 1 } \mathbf { y } ) , } \end{array}
$$

$$
\begin{array} { r l } & { \overline { { \mathbf { x } } } = \mathbf { x } + \epsilon _ { \overline { { \mathbf { x } } } } , ~ E ( \epsilon _ { \overline { { \mathbf { x } } } } ) = 0 , ~ E ( \epsilon _ { \overline { { \mathbf { x } } } } \epsilon _ { \overline { { \mathbf { x } } } } ^ { T } ) = \overline { { P } } , } \\ & { \mathbf { y } = H \mathbf { x } + \epsilon , E \left[ \epsilon \right] = 0 , ~ E \left[ \epsilon \epsilon ^ { T } \right] = R , } \\ & { ~ E \left[ \epsilon \epsilon _ { \overline { { \mathbf { x } } } } ^ { T } \right] = M . } \end{array}
$$

Answer:

$$
\begin{array} { r l } & { P = ( \overline { { P } } ^ { - 1 } + H ^ { T } R ^ { - 1 } H ) ^ { - 1 } + ( \overline { { P } } ^ { - 1 } + H ^ { T } R ^ { - 1 } H ) ^ { - 1 } } \\ & { \quad \times [ H ^ { T } R ^ { - 1 } M \overline { { P } } ^ { - 1 } + \overline { { P } } ^ { - 1 } M ^ { T } R ^ { - 1 } H ] ( \overline { { P } } ^ { - 1 } + H ^ { T } R ^ { - 1 } H ) ^ { - 1 } . } \end{array}
$$

(34) Given that

$$
\begin{array} { c } { \hat { \mathbf { x } } _ { k } = \mathbf { x } _ { k } + \pmb { \eta } _ { k } } \\ { \hat { \mathbf { x } } _ { k + 1 } = \mathbf { x } _ { k + 1 } + \pmb { \eta } _ { k + 1 } } \end{array}
$$

and

$$
\mathbf { x } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) \mathbf { x } _ { k } + \Gamma ( t _ { k + 1 } , t _ { k } ) \mathbf { u } _ { k } ,
$$

where

$$
E [ \pmb { \eta } _ { k } ] = E [ \pmb { \eta } _ { k + 1 } ] = 0
$$

and $\mathbf { x } _ { k }$ and $\mathbf { x } _ { k + 1 }$ are the true values, show that

$$
P \eta _ { k } \eta _ { k + 1 } = E [ \eta _ { k } \eta _ { k + 1 } ^ { T } ] = P _ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) ( I - K _ { k + 1 } H _ { k + 1 } ) ^ { T } .
$$

(35) Consider the linear system define d in Exercise 21. Assume $t _ { 0 } = 0$ ; otherwise replace $t$ with $( t - t _ { 0 } )$ .

$$
\Phi ( t , t _ { 0 } ) = { \frac { \partial X ( t ) } { \partial X ( t _ { 0 } ) } } = { \left[ 0 t \ \frac { t ^ { 2 } } { 2 } \right] } 
$$

and

$$
\overline { { P } } _ { 0 } = \left[ \begin{array} { c c c } { 4 0 0 } \\ { 0 2 0 } \\ { 0 0 1 } \end{array} \right] .
$$

(a) Show that the time update for $P$ at the first measurement time, $t _ { 1 }$ , obtained by integrating the differential equation for $\dot { \overline { { P } } }$ (Eq. 4.9.36) with initial conditions $\overline { { P } } _ { 0 }$ is given by

$$
\overline { { { \cal P } } } ( t _ { 1 } ) = \left[ \begin{array} { l l l l l l l } { { } } & { { 4 + 2 t _ { 1 } + \frac { t _ { 1 } ^ { 4 } } { 4 } } } & { { } } & { { } } & { { 2 t _ { 1 } + \frac { t _ { 1 } ^ { 3 } } { 3 } } } & { { } } & { { \frac { t _ { 1 } ^ { 2 } } { 2 } \nonumber } } & { { } } \\ { { } } & { { 2 t _ { 1 } + \frac { t _ { 1 } ^ { 3 } } { 3 } } } & { { } } & { { } } & { { 2 + t _ { 1 } ^ { 2 } } } & { { } } & { { t _ { 1 } \nonumber } } & { { } } \\ { { } } & { { \frac { t _ { 1 } ^ { 2 } } { 2 } } } & { { } } & { { } } & { { t _ { 1 } } } & { { } } & { { 1 } } & { { } } \end{array} \right] .
$$

(b) Show that this agrees with the conventional time update given by

$$
\overline { { \boldsymbol { P } } } ( t _ { 1 } ) = \Phi ( t _ { 1 } , t _ { 0 } ) \overline { { \boldsymbol { P } } } _ { 0 } \Phi ^ { T } ( t _ { 1 } , t _ { 0 } ) .
$$

(36) Given the information matrix

$$
\Lambda = \left[ \begin{array} { r r r } { { 1 3 } } & { { 2 } } & { { 6 } } \\ { { 2 } } & { { 2 } } & { { 6 } } \\ { { 6 } } & { { 6 } } & { { 1 8 } } \end{array} \right] .
$$

Are all three elements of the state vector observable? Why or why not?

(37) In Example 4.2.1 the state vector includes $X , Y , X _ { s }$ , and $Y _ { s }$ . Are all of these quantities observable? Why or why not?

(38) Given a 2D state vector, $\mathbf { X }$ , with

$$
\begin{array} { r } { E [ \mathbf { X } ] = 0 , \quad E [ \mathbf { X } \mathbf { X } ^ { T } ] = P = \left[ \begin{array} { l l } { 4 } & { 1 } \\ { 1 } & { 2 } \end{array} \right] . } \end{array}
$$

Sketch the $2 \sigma$ probability ellipse.

(39) For the transformation of coordinates

$$
\left[ { x ^ { \prime } } \right] = \left[ \begin{array} { r r } { \cos \theta } & { \sin \theta } \\ { - \sin \theta } & { \cos \theta } \end{array} \right] \left[ \begin{array} { r } { x + 2 } \\ { y + 2 } \end{array} \right] ,
$$

determine $\overline { { x } } ^ { \prime } , \overline { { y } } ^ { \prime }$ , and $P ^ { \prime }$ where $\bar { x } ^ { \prime } = E ( x ^ { \prime } ) , \bar { y } ^ { \prime } = E ( y ^ { \prime } )$ and

$$
P ^ { \prime } = \left[ \begin{array} { l l l } { \begin{array} { l } { \sigma ^ { 2 } ( x ^ { \prime } ) } \end{array} } & { \begin{array} { l } { \mu _ { 1 1 } ( x ^ { \prime } y ^ { \prime } ) } \end{array} } \\ { \begin{array} { l } { \mu _ { 1 1 } ( x ^ { \prime } y ^ { \prime } ) } \end{array} } & { \begin{array} { l } { \sigma ^ { 2 } ( y ^ { \prime } ) } \end{array} } \end{array} \right] .
$$

(40) The differential equation for the Ornstein-Uhlenbeck process, a first-order Gauss-Markov process, is

$$
\dot { \eta } ( t ) + \beta \eta ( t ) = u ( t )
$$

with initial conditions $\eta = \eta \left( t _ { 0 } \right)$ , at $t = t _ { 0 }$ where $u \left( t \right)$ is a Gaussian white noise process with mean zero. Show that the solution is given by

$$
\eta \left( t \right) = \eta \left( t _ { 0 } \right) e ^ { - \beta \left( t - t _ { 0 } \right) } + \int _ { t _ { 0 } } ^ { t } e ^ { - \beta \left( t - \tau \right) } u \left( \tau \right) d \tau .
$$

(41) Generate 1000 equally spaced observations of one cycle of a sine wave with amplitude 1 and period 10. Add Gaussian random noise with zero mean and variance $= 0 . 2 5$ . Set up a sequential estimation procedure to estimate the amplitude of the sine wave as a function of time using the noisy raw data. Model the sine wave as a Gauss-Markov process as given by Eq. (4.9.60),

$$
\eta _ { i + 1 } = m _ { i + 1 } \eta _ { i } + \Gamma _ { i + 1 } u _ { i }
$$

where

$$
u _ { i } = N ( 0 , 1 )
$$

$$
\begin{array} { l } { { m _ { i + 1 } = e ^ { - \beta ( t _ { i + 1 } - t _ { i } ) } } } \\ { { \ ~ } } \\ { { \Gamma _ { i + 1 } = \sqrt { \displaystyle \frac { \sigma ^ { 2 } } { 2 \beta } ( 1 - m _ { i + 1 } ^ { 2 } ) } } } \\ { { \ ~ \beta = \displaystyle \frac { 1 } { \tau } } } \end{array}
$$

and $\tau$ is the time constant. The sequential algorithm is given by

$$
\begin{array} { r l } & { \bar { \eta } _ { i } = \Phi ( t _ { i } , t _ { i - 1 } ) \hat { \eta } _ { i - 1 } \quad ( i = 1 , 2 \dots 1 0 0 0 ) } \\ & { \Phi ( t _ { i } , t _ { i - 1 } ) = m _ { i } = e ^ { - \beta ( t _ { i } - t _ { i - 1 } ) } } \\ & { \overline { { P } } _ { i } = \Phi ( t _ { i } , t _ { i - 1 } ) P _ { i - 1 } \Phi ^ { T } ( t _ { i } , t _ { i - 1 } ) + \Gamma _ { i } Q _ { i - 1 } \Gamma _ { i } ^ { T } } \end{array}
$$

Note that $P , \Phi , Q$ , and $\Gamma$ are scalars

$$
\begin{array} { r l } & { K _ { i } = \overline { { P } } _ { i } \widetilde { H } _ { i } ^ { T } ( \widetilde { H } _ { i } \overline { { P } } _ { i } \widetilde { H } _ { i } ^ { T } + R _ { i } ) ^ { - 1 } = \frac { \overline { { P } } _ { i } } { \overline { { P } } _ { i } + 1 } } \\ & { \widehat { \eta } _ { i } = \overline { { \eta } } _ { i } + K _ { i } ( Y _ { i } - \widetilde { H } _ { i } \overline { { \eta } } _ { i } ) = \overline { { \eta } } _ { i } + K _ { i } ( Y _ { i } - \overline { { \eta } } _ { i } ) , ( Y _ { i } \mathrm { i s t } } \\ & { \mathrm { d a t a } ) } \\ & { P _ { i } = ( I - K _ { i } \widetilde { H } _ { i } ) \overline { { P } } _ { i } = K _ { i } } \\ & { \mathrm { x t ~ } i } \end{array}
$$

he observation

Ne

Plot your observations, the truth data, and $\hat { \eta }$ versus time. You will need to guess initial values for $\sigma$ and $\beta$ . Try several values to see which gives you the best results (i.e., the smallest RMS of estimation errors).

$$
\mathrm { R M S } = \left\{ \sum _ { i = 1 } ^ { N } \frac { ( T _ { i } - \hat { \eta } _ { i } ) ^ { 2 } } { N } \right\} ^ { 1 / 2 } ,
$$

where $T _ { i }$ is the true amplitude of the sine wave and $N = 1 0 0 0$ . Fig. 4.19.1 illustrates the truth, the raw data, and one example of the filtered results (not necessarily the optimal) for the indicated values of $\sigma$ and $\beta$ . The truth is the smooth curve. You may also plot a histogram of the post-fit residuals to see if they conform to a Gaussian distribution.

(42) Using the optimum values of $\sigma$ and $\tau$ determined in Exercise 41, solve for the smoothed history of $\hat { \eta } ( t )$ using the algorithm of Section 4.15.1. Plot the true values of $\eta$ , the fil ter values determined in Exercise 41, and the smoothed values. Compute the RMS of the smoothed fit. You should find the RMS from the smoothed solution somewhat smaller than the fil ter result. Fig. 4.19.2 is an example of the truth, the filter , and the smoothed results for the case illustrated in Fig. 4.19.1. Is the histogram of residuals

# Process Noise / Sine Wave Recovery

![](images/32d910aeebc3eff5c581e213ce4af266f7449ffa16bc9c849f8a6a4b36ffa97b.jpg)  
Figure 4.19.1: Process noise/sine wave recovery showing truth, raw data (truth plus noise) and the filtered solution. $\bar { \eta } _ { 0 } = 0$ , $\sigma = 2 . 4 9$ , $\beta = . 0 4 5$ .

for the smoothed solution more nearly Gaussian than those from the filter in Exercise 41?

(43) Given a system described by

$$
\mathbf { X } ( t _ { i + 1 } ) = { \left[ \begin{array} { l } { x _ { 1 } ( t _ { i + 1 } ) } \\ { x _ { 2 } ( t _ { i + 1 } ) } \end{array} \right] } = { \left[ \begin{array} { l } { 1 1 } \\ { 0 1 } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } \left( t _ { i } \right) } \\ { x _ { 2 } \left( t _ { i } \right) } \end{array} \right] } + { \left[ \begin{array} { l } { 1 1 } \\ { 1 0 } \end{array} \right] } { \left[ \begin{array} { l } { u _ { 1 } ( t _ { i } ) } \\ { u _ { 2 } ( t _ { i } ) } \end{array} \right] }
$$

$$
{ \left[ \begin{array} { l } { y _ { 1 } ( t _ { i } ) } \\ { y _ { 2 } ( t _ { i } ) } \end{array} \right] } = { \left[ \begin{array} { l } { 0 1 / 2 } \\ { 1 1 / 2 } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } \left( t _ { i } \right) } \\ { x _ { 2 } \left( t _ { i } \right) } \end{array} \right] } + { \left[ \epsilon _ { 1 } \right] }
$$

$$
\begin{array} { r } { \overline { { \mathbf { X } } } ( t _ { 0 } ) = [ \overline { { x } } _ { 1 } ( t _ { 0 } ) ] = [ 2 ] , \overline { { P } } ( t _ { 0 } ) = [ 0 ] } \\ { \overline { { x } } _ { 2 } ( t _ { 0 } ) \mathbf { . } ] } \end{array}
$$

$$
R = E \left\{ \left[ { \epsilon } _ { 1 } \right] \left[ \epsilon _ { 1 } \epsilon _ { 2 } \right] \right\} = \left[ 0 \atop 0 2 \right] ,
$$

$$
E [ u _ { 1 } ( t _ { i } ) ] = E [ u _ { 2 } ( t _ { i } ) ] = 0
$$

# Process Noise / Sine Wave Recovery

![](images/fff4443c03d7d1a2cbaacfd605f8a0a49743e46c66ef35a64a650cb11b90c022.jpg)  
Figure 4.19.2: Process noise/sine wave recovery showing the truth, the filtered, and the smoothed solution. $\bar { \eta } _ { 0 } = 0$ , $\sigma = 2 . 4 9$ , $\beta = . 0 4 5$ .

$$
E \left\{ \left[ u _ { 1 } ( t _ { i } ) \right] \left[ u _ { 1 } ( t _ { j } ) u _ { 2 } ( t _ { j } ) \right] \right\} = I \delta _ { i j } .
$$

Observations at $t _ { 1 }$ are given by

$$
\begin{array} { r } { \left[ y _ { 1 } ( t _ { 1 } ) \right] = \left[ \begin{array} { l } { 3 } \\ { 2 } \end{array} \right] . } \end{array}
$$

(a) Using the sequential estimation algorithm, determine the optimal estimate of $\mathbf { X } ( t _ { 1 } )$ and $P ( t _ { 1 } )$ .   
(b) What is the smoothed estimate of ${ \bf X } ( t _ { 0 } ) \} \mathrm { ~ }$ ？   
(c) What is the optimal estimate of $\mathbf X ( t _ { 1 } )$ if no process noise were present?

(44) Use the information fil ter to determine the optimal estimate of $\mathbf X ( t _ { 1 } )$ and $P ( t _ { 1 } )$ for Exercise $4 3 \mathrm { a }$ .

# Square Root Solution Methods for the Orbit Determination Problem

# 5.1 INTRODUCTION

In the previous chapter, the solution to the least squares estimation problem including $a$ priori information, $\overline { { P } }$ and $\overline { { \mathbf { x } } }$ , is represented in the normal equation form as

$$
( H ^ { T } W H + \overline { { P } } ^ { - 1 } ) \hat { \mathbf { x } } = H ^ { T } W y + \overline { { P } } ^ { - 1 } \overline { { \mathbf { x } } }
$$

which can be expressed as

$$
M \hat { \mathbf { x } } = N .
$$

The solution for $\hat { \bf x }$ is obtained by computing the inverse of $M$ . In practice, computational problems are encountered in forming and inverting the matrix $M =$ $H ^ { T } W H + \overline { { P } } ^ { - 1 }$ . An orthogonal transformation approach can be used to write Eq. (5.1.2) in the form

$$
R \hat { \mathbf x } = b
$$

where $R$ is an $n \times n$ upper triangular matrix ( $R$ is not the observation error covariance matrix). Then $\hat { \bf x }$ can be obtained by backward substitution. This approach has the advantage that increased numerical accuracy is achieved over conventional matrix inversion methods for solving Eq. (5.1.2). Using the orthogonal transformation approach, accuracy can be achieved with a single-precision computation that is equal to the accuracy obtained by inverting $M$ with the normal equation approach using double-precision computations.

The normal equation approach has several operational and conceptual advantages that have led to the widespread adoption of this technique for many operational orbit determination systems. Both the normal equation and orthogonal transformation approaches are described in the subsequent sections.

The solution of the linear system

$$
M \hat { \mathbf { x } } = \mathbf { N }
$$

is expressed as

$$
\hat { \mathbf { x } } = M ^ { - 1 } \mathbf { N }
$$

where the operation $M ^ { - 1 }$ implies that the inverse of the $( n \times n )$ matrix $M$ is computed and then postmultiplied by the column vector $\mathbf { N }$ . A solution based on the Cholesky decomposition of $M$ is more efficient and, in most cases, more accurate. The Cholesky decomposition is applicable only if $M$ is symmetric and positive definite, a condition satisfied for the case considered here. The following discussion first outlines the Cholesky decomposition, and describes this approach to solving the normal equations. Then a discussion of solutions based on orthogonal transformations is presented in subsequent sections.

# 5.2 CHOLESKY DECOMPOSITION

Let $M$ be a symmetric positive definite matrix, and let $R$ be an upper triangular matrix computed such that

$$
R ^ { T } R = M .
$$

(Note that $R$ is not the observation error covariance matrix.) Then Eq. (5.1.4) can be expressed as

$$
R ^ { T } R \hat { \mathbf { x } } = \mathbf { N } .
$$

If the definit ion

$$
{ \bf z } = R \hat { \bf x }
$$

is used, Eq. (5.2.2) can be written as

$$
R ^ { T } { \bf z } = { \bf N }
$$

where $R ^ { T }$ is lower triangular. The components of $\mathbf { z }$ can be determined using a forward recursion relation. Then, Eq. (5.2.3) can be solved using a backward recursion to obtain the elements of $\hat { \bf x }$ .

The elements of the error covariance matrix, $P = ( H ^ { T } W H + \overline { { { P } } } ^ { - 1 } ) ^ { - 1 } =$ $M ^ { - 1 }$ , can be obtained from the condition

$$
P = M ^ { - 1 } = ( R ^ { T } R ) ^ { - 1 } = R ^ { - 1 } R ^ { - T } = S S ^ { T }
$$

where $S$ , the inverse of the upper triangular matrix, $R$ , can be computed by an efficient backward recursion.

Equation (5.2.1) represents a set of $( n ^ { 2 } + n ) / 2$ equations for the $( n ^ { 2 } + n ) / 2$ unknown elements of the upper triangular matrix, $R$ . The expression for the Cholesky decomposition of $M$ is obtained by expanding Eq. (5.2.1) and solving term by term for the elements of $R$ (e.g., $R _ { i j }$ is determined in terms of the elements of $M$ ).

Given the elements of the $n \times n$ positive definit e matrix $M$ and the $n \times 1$ column vector $\mathbf { N }$ , the following Cholesky algorithm will yield a solution for the elements of $R , \mathbf { z } , { \hat { \mathbf { x } } }$ and the upper triangular matrix, $S$ . Step 1 of the following algorithm determines the elements of $R$ and the vector $\mathbf { z }$ . Steps 2 and 3 perform a backward recursion to form $\hat { \bf x }$ and the elements of the matrix $S = R ^ { - 1 }$ .

# 5.2.1 THE CHOLESKY ALGORITHM

The Cholesky algorithm for $R$ is derived easily by equating the elements of $R ^ { T } R$ to the elements of $M$ that are known. For example, from expanding $R ^ { T } R$ it is shown that $r _ { 1 1 } = \sqrt { M _ { 1 1 } }$ .

1) For $i = 1 , 2 , \dots , n$

$$
\begin{array} { l } { { \displaystyle r _ { i i } = \left( M _ { i i } - \sum _ { k = 1 } ^ { i - 1 } r _ { k i } ^ { 2 } \right) ^ { 1 / 2 } } } \\ { { \displaystyle r _ { i j } = \left( M _ { i j } - \sum _ { k = 1 } ^ { i - 1 } r _ { k i } r _ { k j } \right) / r _ { i i } ; \quad j = i + 1 , \dots , n . } } \end{array}
$$

The elements of $\mathbf { z }$ are obtained from an expansion of Eq. (5.2.4):

$$
z _ { i } = \left( N _ { i } - \sum _ { j = 1 } ^ { i - 1 } r _ { j i } z _ { j } \right) / r _ { i i }
$$

2) For $i = n , n - 1 , \ldots , 1$

$$
{ \hat { x } } _ { i } = \left( z _ { i } - \sum _ { j = i + 1 } ^ { n } r _ { i j } { \hat { x } } _ { j } \right) / r _ { i i } .
$$

The elements of $S$ are obtained from an expansion of $S R = I$ .

3) For $i = 1 , 2 \dots , n$

$$
\begin{array} { l } { { s _ { i i } = \displaystyle \frac { 1 } { r _ { i i } } } } \\ { { s _ { i j } = - s _ { j j } \left[ \displaystyle \sum _ { k = i } ^ { j - 1 } r _ { k j } s _ { i k } \right] ; \quad j = i + 1 , \ldots , n . } } \end{array}
$$

Examples of the application of this algorithm are given in Sections 5.6.1 and 5.6.5.

This Cholesky algorithm is a nonblock algorithm. That is, it does not use matrix multiplication. Because matrix multiplication is much faster in terms of floating point operations per second than matrix-vector operations on modern computers, a block Cholesky algorithm often will be faster than a nonblock version. In fact, the increase in speed may be a factor of three or more. See Golub and Van Loan (1996) for examples of a block Cholesky algorithm.

# 5.2.2 THE SQUARE ROOT FREE CHOLESKY ALGORITHM

Notice that calculation of the diagonal elements of $R$ requires that $n$ square roots be taken. Computationally the square root operation is expensive compared to multiplication, division, addition, or subtraction; hence, it is desirable to avoid square roots if possible. A square root free Cholesky algorithm may be developed by defining

$$
M = U D U ^ { T }
$$

where $U$ is unit upper triangular (i.e., has ones on the diagonal), and $D$ is a diagonal matrix. As in the previous section, Eq. (5.2.10) represents the $( n ^ { 2 } + n ) / 2$ equation in the $( n ^ { 2 } + n ) / 2$ unknown elements of $U$ and $D$ . The algorithm for the elements of $U$ and $D$ is obtained by expanding Eq. (5.2.10) and is given by

$$
D _ { j } U _ { i j } = M _ { i j } - \sum _ { k = j + 1 } ^ { n } M _ { j k } ^ { \prime } U _ { i k } \equiv M _ { i j } ^ { \prime } j = n , \dots , 1
$$

$$
D _ { j } = M _ { j j } - \sum _ { k = j + 1 } ^ { n } M _ { j k } ^ { \prime } U _ { j k } .
$$

The procedure is to set $j = n$ and cycle through the algorithm for $i = 1 \dots n - 1$ , solving for $D _ { n }$ and the elements of $U _ { i n }$ (i.e., the last column of $U$ ). Then set $j = n - 1$ and cycle through for $i = 1 \dots n - 2$ , solving for $D _ { n - 1 }$ and the $n - 1$ column of $U$ . Repeat this procedure for the remaining values of $j$ .

Knowing $U$ and $D$ , it is possible to solve for $\hat { \bf x }$ from Eq. (5.1.2) and Eq. (5.2.10) as follows. Note that

$$
U D U ^ { T } \hat { \mathbf { x } } = \mathbf { N }
$$

and let

$$
{ \bf z } = D U ^ { T } \hat { \bf x } .
$$

Then

$$
U \mathbf { z } = \mathbf { N } .
$$

The intermediate vector $\mathbf { z }$ can be determined from Eq. (5.2.15). The solution is a backward substitution (i.e., we solve for $z _ { n }$ , $z _ { n - 1 } \ldots z _ { 1 } ,$ ):

$$
\begin{array} { l } { { z _ { n } = N _ { n } } } \\ { { z _ { i } = N _ { i } - \displaystyle \sum _ { j = i + 1 } ^ { n } U _ { i j } z _ { j } ~ i = n - 1 , \ldots , 1 . } } \end{array}
$$

Then the elements of $\hat { \bf x }$ can be determined from Eq. (5.2.14) by using a forward substitution, as

$$
\hat { x } _ { i } = \frac { z _ { i } } { D _ { i i } } - \sum _ { j = 1 } ^ { i - 1 } U _ { j i } \hat { x } _ { j } i = 1 , 2 , \ldots n .
$$

The associated estimation error covariance is obtained from

$$
\begin{array} { c } { P = ( U D U ^ { T } ) ^ { - 1 } } \\ { = U ^ { - T } D ^ { - 1 } U ^ { - 1 } } \end{array}
$$

where

$$
\begin{array} { l l } { { \displaystyle { D _ { i i } ^ { - 1 } = 1 / D _ { i i } } \qquad i = 1 , \dots n } } \\ { { \qquad \quad j = i + 1 , \dots \cdot n } } \\ { { \displaystyle { U _ { i j } ^ { - 1 } = - \sum _ { k = i } ^ { j - 1 } U _ { i k } ^ { - 1 } U _ { k j } } } } \\ { { \qquad \quad U _ { i j } ^ { - 1 } = 0 \qquad i > j } } \\ { { \displaystyle { D _ { i j } ^ { - 1 } = 0 \qquad i \neq j . } } } \end{array}
$$

Note that none of the algorithms required to compute $\hat { \bf x }$ involve the calculation of a square root.

# 5.3 LEAST SQUARES SOLUTION VIA ORTHOGONAL TRANSFORMATION

An alternate approach that avoids some of the numerical problems encountered in the normal equation approach is described in the following discussion. The method obtains the solution by applying successive orthogonal transformations to the information array, $( H , \mathbf { y } )$ . Enhanced numerical accuracy is obtained by this approach. Consider the quadratic performance index, $J ( \mathbf { x } )$ , which minimizes the weighted sum of squares of the observation errors, $\boldsymbol { \epsilon } = \mathbf { y } - H \mathbf { x }$ (for the moment we will assume no a priori information; i.e., $\overline { { P } } ^ { - 1 } = 0$ , $\mathbf { \overline { { x } } = 0 }$ ):

$$
J ( { \bf x } ) = \epsilon ^ { T } W \epsilon = \left\| { W ^ { \frac { 1 } { 2 } } ( H { \bf x } - { \bf y } ) } \right\| ^ { 2 } = ( H { \bf x } - { \bf y } ) ^ { T } W ( H { \bf x } - { \bf y } ) .
$$

If $W$ is not diagonal, $W ^ { 1 / 2 }$ can be computed by the Cholesky decomposition. Or the prewhitening transformation described at the end of Section 5.7.1 can be applied so that $W = I$ . For notational convenience we are using $- \epsilon$ in Eq. (5.3.1).

The solution to the least squares estimation problem (as well as the minimum variance and the maximum likelihood estimation problem, under certain restrictions) is obtained by finding the value $\hat { \bf x }$ that minimizes the performance index $J ( \mathbf { x } )$ . To achieve the minimum value of $J ( \mathbf { x } )$ , we introduce the $m \times m$ orthogonal matrix, $Q$ . An orthogonal matrix has the following properties:

1. $Q Q ^ { T } = I$

2. $Q ^ { - 1 } = Q ^ { T }$ hence $Q ^ { T } Q = I$ .

3. If $Q _ { 1 }$ and $Q _ { 2 }$ are orthogonal matrices, then so is $Q _ { 1 } Q _ { 2 }$ .

4. For any vector $\mathbf { x }$

$$
\left\| Q \mathbf { x } \right\| = \left\| \mathbf { x } \right\| = ( \mathbf { x } ^ { T } \mathbf { x } ) ^ { \frac { 1 } { 2 } } .
$$

Multiplying by $Q$ does not change the Euclidean norm of a vector.

5. If $\epsilon$ is an $m$ vector of random variables with $\epsilon \sim ( O , I )$ (i.e., $E ( \epsilon ) = 0$ and $E ( \epsilon \epsilon ^ { T } ) = I )$ ), then $\overline { { \epsilon } } = Q \epsilon$ has the same properties,

$$
E ( \overline { { \epsilon } } ) = Q E ( \epsilon ) = 0 , E ( \overline { { \epsilon } } \overline { { \epsilon } } ^ { T } ) = Q E ( \epsilon \epsilon ^ { T } ) Q ^ { T } = I .
$$

It follows then that (5.3.1) can be expressed as

$$
\begin{array} { l } { { \displaystyle J ( { \bf x } ) = \left\| Q W ^ { \frac { 1 } { 2 } } ( H { \bf x } - { \bf y } ) \right\| ^ { 2 } } } \\ { { \displaystyle ~ = \left( H { \bf x } - { \bf y } \right) ^ { T } W ^ { \frac { 1 } { 2 } } Q ^ { T } Q W ^ { \frac { 1 } { 2 } } \Big ( H { \bf x } - { \bf y } \Big ) . } } \end{array}
$$

Select $Q$ such that

$$
Q W ^ { \frac { 1 } { 2 } } H = { \Biggl [ } R { \Biggr ] } { \mathrm { a n d d e f i n e ~ } } Q W ^ { \frac { 1 } { 2 } } \mathbf { y } \equiv { \Biggl [ } \mathbf { b } { \Biggr ] }
$$

where

$R$ is a $n \times n$ upper-triangular matrix of rank $n$

$O$ is a $( m - n ) \times n$ null matrix $\mathbf { b }$ is a $n \times 1$ column vector $\mathbf { e }$ is a $( m - n ) \times 1$ column vector.

The results given by Eq. (5.3.6) assume that $m > n$ and $H$ is of rank $n$ . Using Eq. (5.3.6), Eq. (5.3.5) can be written as

$$
J ( \mathbf { x } ) = | [ { \binom { R } { O } } \mathbf { x } - [ \mathbf { b } ] | ^ { 2 } .
$$

Expanding leads to

$$
J ( \mathbf { x } ) = \Big \| R \mathbf { x } - \mathbf { b } \Big \| ^ { 2 } + \Big \| \mathbf { e } \Big \| ^ { 2 } .
$$

Only the first term in Eq. (5.3.8) is a function of $\mathbf { x }$ , so the value of $\mathbf { x }$ that minimizes $J ( \mathbf { x } )$ is obtained by requiring that

$$
R \hat { \mathbf x } = \mathbf b
$$

and the minimum value of the performance index becomes (equating $J ( \hat { x } )$ in Eq. (5.3.1) and Eq. (5.3.8))

$$
J ( \hat { \mathbf { x } } ) = \left\| \mathbf { e } \right\| ^ { 2 } = \left\| W ^ { \frac { 1 } { 2 } } ( H \hat { \mathbf { x } } - \mathbf { y } ) \right\| ^ { 2 } .
$$

That is, $\lVert \mathbf e \rVert$ is the norm of the observation residual vector, which for a linear system will be equal to the weighted sum of the squares of observation residuals determined by using $\hat { \bf x }$ in Eq. (5.3.10).

# 5.4 GIVENS TRANSFORMATIONS

The procedure described in the previous section is direct and for implementation requires only that a convenient procedure for computing $Q$ be obtained. One such procedure can be developed based on the Givens plane rotation (Givens, 1958). Let $\mathbf { x }$ be a $2 \times 1$ vector having components $\mathbf { x } ^ { T } = \left[ x _ { 1 } x _ { 2 } \right]$ and let $G$ be a $2 \times 2$ orthogonal matrix associated with the plane rotation through the angle $\theta$ . Then select $G$ such that

$$
G \mathbf { x } = \mathbf { x } ^ { \prime } = { \binom { x _ { 1 } ^ { \prime } } { 0 } } .
$$

To this end, consider the transformation

$$
{ \Bigg [ } x _ { 1 } ^ { \prime } { \Bigg ] } = { \Bigg [ } { \cos \theta \sin \theta } { \Bigg ] } { \Bigg [ } x _ { 1 } { \Bigg ] }
$$

or

$$
\begin{array} { r l } & { x _ { 1 } ^ { \prime } = \quad \cos \theta x _ { 1 } + \sin \theta x _ { 2 } } \\ & { x _ { 2 } ^ { \prime } = - \sin \theta x _ { 1 } + \cos \theta x _ { 2 } . } \end{array}
$$

Equations (5.4.3) represent a system of two equations in three unknowns; that is, $x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime }$ , and $\theta$ . The Givens rotation is defined by selecting the rotation $\theta$ such that $x _ { 2 } ^ { \prime } = 0$ . That is, let

$$
\begin{array} { r } { x _ { 1 } ^ { \prime } = \quad \cos \theta x _ { 1 } + \sin \theta x _ { 2 } } \\ { 0 = - \sin \theta x _ { 1 } + \cos \theta x _ { 2 } . } \end{array}
$$

From Eq. (5.4.5), it follows that

$$
\tan \theta = \frac { x _ { 2 } } { x _ { 1 } } , \sin \theta = \frac { x _ { 2 } } { \sqrt { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } } } , \cos \theta = \frac { x _ { 1 } } { \sqrt { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } } } .
$$

The positive value associated with the square root operation is selected for the following discussion. Substituting the expression for $\sin \theta$ and $\cos \theta$ into Eq. (5.4.4) leads to

$$
x _ { 1 } ^ { \prime } = \frac { x _ { 1 } ^ { 2 } } { \sqrt { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } } } + \frac { x _ { 2 } ^ { 2 } } { \sqrt { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } } } = \sqrt { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } } .
$$

Consider the application of the transformation

$$
G ( \theta ) = \left[ \begin{array} { r } { { \cos \theta \sin \theta } } \\ { { - \sin \theta \cos \theta } } \end{array} \right]
$$

to two general row vectors $\mathbf { h } _ { i }$ and $\mathbf { h } _ { k }$ ; for example,

$$
G \left[ \begin{array} { l } { h _ { i i } \ h _ { i i + 1 } \ . . . h _ { i n } } \\ { h _ { k i } h _ { k i + 1 } \ . . . h _ { k n } } \end{array} \right] = \left[ \begin{array} { l } { h _ { i i } ^ { \prime } h _ { i i + 1 } ^ { \prime } \ . . . h _ { i n } ^ { \prime } } \\ { 0 \ h _ { k i + 1 } ^ { \prime } \cdot . . . h _ { k n } ^ { \prime } } \end{array} \right] .
$$

That is, for any two general row vectors, $\mathbf { h } _ { i }$ and $\mathbf { h } _ { k }$ , the transformation is applied to the first column so as to null $h _ { k i }$ . The transformation that accomplishes this is applied to each remaining column to obtain the transformed matrix. Hence,

$$
\begin{array} { r } { \left[ \begin{array} { l } { \cos \theta \sin \theta } \\ { - \sin \theta \cos \theta } \end{array} \right] \left[ h _ { i i } \right] = \left[ \begin{array} { l } { h _ { i i } ^ { \prime } } \\ { h _ { k i } } \end{array} \right] } \end{array}
$$

or

$$
\begin{array} { r c l } { { } } & { { } } & { { \sin \theta = h _ { k i } / \sqrt { h _ { i i } ^ { 2 } + h _ { k i } ^ { 2 } } = h _ { k i } / h _ { i i } ^ { \prime } } } \\ { { } } & { { } } & { { \cos \theta = h _ { i i } / \sqrt { h _ { i i } ^ { 2 } + h _ { k i } ^ { 2 } } = h _ { i i } / h _ { i i } ^ { \prime } } } \\ { { } } & { { } } & { { h _ { i i } ^ { \prime } = \sqrt { h _ { i i } ^ { 2 } + h _ { k i } ^ { 2 } } . } } \end{array}
$$

Then for all other columns,

$$
\begin{array} { c } { { h _ { i j } ^ { \prime } = h _ { i j } \cos \theta + h _ { k j } \sin \theta } } \\ { { { } } } \\ { { j = i + 1 , \ldots , n } } \\ { { { } h _ { k j } ^ { \prime } = - h _ { i j } \sin \theta + h _ { k j } \cos \theta . } } \end{array}
$$

By using this transformation repetitively as $k$ goes from $i + 1$ to $m$ , the remaining elements of the $i ^ { \mathrm { t h } }$ column can be nulled. Then by moving down the diagonal and applying the transformation to successive columns whose first element lies on the diagonal, a rank $n$ matrix can be reduced to an upper triangular $n \times n$ matrix with a lower $( m - n ) \times n$ null matrix. If the element to be nulled already has a value of zero, the transformation matrix will be the identity matrix and the corresponding transformation may be skipped.

As an example, the transformation to null the fourth element in the third column is shown as follows:

$$
\begin{array} { r } { \left[ \begin{array} { l } { 1 } \\ { 1 } \\ { 1 } \\ { C ^ { 4 , 3 } S ^ { 4 , 3 } } \\ { - S ^ { 4 , 3 } C ^ { 4 , 3 } } \\ { 1 } \\ { 1 } \\ { 1 } \\ { \ddots } \\ { 1 } \\ { 0 } \end{array} \right] \left[ \begin{array} { l l l l } { h _ { 1 1 } ~ h _ { 1 2 } ~ h _ { 1 3 } \cdots ~ h _ { 1 n } ~ y _ { 1 } } \\ { 0 } & { h _ { 2 2 } ~ h _ { 2 3 } \cdots ~ h _ { 2 n } ~ y _ { 2 } } \\ { 0 } & { 0 } & { h _ { 3 3 } \cdots ~ h _ { 3 n } ~ y _ { 3 } } \\ { 0 } & { 0 } & { h _ { 4 3 } \cdots ~ h _ { 4 n } ~ y _ { 4 } } \\ { 0 } & { 0 } & { h _ { 5 3 } \cdots ~ h _ { 5 n } ~ y _ { 5 } } \\ { 0 } & { 0 } & { h _ { 6 3 } \cdots ~ h _ { 6 n } ~ y _ { 6 } } \\ { \vdots } & { \vdots } & { \vdots } \\ { ~ 0 } & { 0 } & { h _ { m 3 } \cdots ~ h _ { m } ~ y _ { m } } \end{array} \right] } \end{array}
$$

$$
\begin{array} { r } { \left[ \begin{array} { c c c c c } { h _ { 1 1 } h _ { 1 2 } h _ { 1 3 } \cdots h _ { 1 n } \ y _ { 1 } } \\ { 0 } & { h _ { 2 2 } h _ { 2 3 } \cdots h _ { 2 n } \ y _ { 2 } } \\ { 0 } & { 0 } & { h _ { 3 3 } ^ { \prime \prime } \cdots h _ { 3 n } ^ { \prime \prime } \ y _ { 3 } ^ { \prime } } \\ { 0 } & { 0 } & { 0 } & { \cdots h _ { d n } ^ { \prime \prime } \ y _ { 4 } ^ { \prime \prime } } \\ { 0 } & { 0 } & { h _ { 5 3 } \cdots h _ { 5 n } \ y _ { 5 } } \\ { 0 } & { 0 } & { h _ { 6 3 } \cdots h _ { 6 n } \ y _ { 6 } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { h _ { m 3 } \cdots h _ { m n } \ y _ { m } } \end{array} \right] . } \end{array}
$$

The prime superscript identifies the two rows that are affected by this transformation (rows three and four). Notice that the location of $- \sin \theta$ in the Givens transformation matrix corresponds to the location of the element to be nulled in the $H$ matrix. For example, in the previous example both are element (4,3).

By using the transformation

$$
\begin{array} { r } { Q ^ { 5 , 3 } = \left[ \begin{array} { c } { 1 } \\ { 1 } \\ { C ^ { 5 , 3 } \ 0 S ^ { 5 , 3 } } \\ { 0 \phantom { - } 1 \ 0 } \\ { - S ^ { 5 , 3 } \ 0 C ^ { 5 , 3 } } \\ { 1 } \\ { 1 } \\ { 1 } \\ { \ddots } \\ { 1 } \end{array} \right] , } \end{array}
$$

the third and fifth rows will be transformed so that the term $h _ { 5 3 }$ will be zero.

# 5.4.1 A PRIORI INFORMATION AND INITIALIZATION

The formulation given earlier does not specifically address the question of $a$ priori information. Assume a priori information, $\overline { { \mathbf { x } } }$ and $\overline { { P } }$ , are available. The procedure is initialized by writing the a priori information in the form of a data equation; that is, in the form of $\mathbf { y } = H \mathbf { x } + \epsilon$ . This is accomplished by writing

$$
\overline { { \mathbf { x } } } = \mathbf { x } + \boldsymbol { \eta }
$$

where $\mathbf { x }$ is the true value and $\eta$ is the error in $\overline { { \mathbf { x } } }$ . We assume that

$$
E [ \pmb { \eta } ] = 0 , E [ \pmb { \eta } \pmb { \eta } ^ { T } ] = \overline { { P } } .
$$

Compute $\overline { S }$ , the upper triangular square root of $\overline { { P } }$ ,

$$
\overline { { { P } } } = \overline { { { S } } } \overline { { { S } } } ^ { T } .
$$

If $\overline { { P } }$ is not diagonal, the Cholesky decomposition may be used to accomplish this. Next compute $\overline { { R } }$ , the square root of the a priori information matrix, $\overline { { \Lambda } }$ ,

$$
\overline { { { \Lambda } } } = \overline { { { P } } } ^ { - 1 } = \overline { { { S } } } ^ { - T } \overline { { { S } } } ^ { - 1 } = \overline { { { R } } } ^ { T } \overline { { { R } } }
$$

hence,

$$
\overline { { { R } } } = \overline { { { S } } } ^ { - 1 } .
$$

Multiplying Eq. (5.4.15) by $\overline { { R } }$ yields

$$
\begin{array} { r } { \overline { { R } } \overline { { \mathbf { x } } } = \overline { { R } } \mathbf { x } + \overline { { R } } \eta . } \end{array}
$$

Define

$$
\begin{array} { r } { \overline { { \mathbf { b } } } \equiv \overline { { R } } \overline { { \mathbf { x } } } , \overline { { \eta } } \equiv \overline { { R } } \eta , } \end{array}
$$

then

$$
\overline { { \mathbf { b } } } = \overline { { R } } \mathbf { x } + \overline { { \eta } }
$$

where $\overline { { \eta } } \sim ( O , I )$ . Note that Eq. (5.4.22) expresses the a priori information in the form of the data equation, $\mathbf { y } = H \mathbf { x } + \epsilon$ . Hence, the equations we wish to solve for $\hat { \bf x }$ , using orthogonal transformations, are

$$
\begin{array} { r } { \overline { { \mathbf { b } } } = \overline { { R } } \mathbf { x } + \overline { { \eta } } } \\ { \mathbf { y } = H \mathbf { x } + \epsilon } \end{array}
$$

where $\mathbf { x }$ is an $n$ vector and $\mathbf { y }$ is an $m$ vector.

The least squares solution for $\mathbf { x }$ in Eq. (5.4.23) is found by minimizing the performance index (we assume that $\epsilon$ has been prewhitened so that $\epsilon \sim ( O , I )$ ; if not, replace $\epsilon$ with $W ^ { 1 / 2 } \epsilon$ in $J$ )

$$
\begin{array} { r l } & { J = \| \overline { { \boldsymbol { \eta } } } \| ^ { 2 } + \| \epsilon \| ^ { 2 } } \\ & { \quad = \| \overline { { R } } \mathbf { x } - \overline { { \mathbf { b } } } \| ^ { 2 } + \| H \mathbf { x } - \mathbf { y } \| ^ { 2 } } \\ & { \quad = \left\| \begin{array} { l } { \left[ \overline { { R } } \right] \mathbf { x } - \left[ \overline { { \mathbf { b } } } \right] } \\ { H } \end{array} \right\| ^ { 2 } . } \end{array}
$$

After multiplying by an orthogonal transformation, $Q$ , Eq. (5.4.24) may be written as

$$
J = \left\{ \left[ { \overline { { R } } } \right] \mathbf { x } - \left[ { \overline { { \mathbf { b } } } } \right] \right\} ^ { T } Q ^ { T } Q \left\{ \left[ { \overline { { R } } } \right] \mathbf { x } - \left[ { \overline { { \mathbf { b } } } } \right] \right\} .
$$

Choose $Q$ so that

$$
Q \left[ { \frac { \overline { { R } } } { H } } \right] = { \binom { R } { O } } , { \mathrm { a n d d e f i n e } } Q \left[ { \overline { { \mathbf { b } } } } \right] \equiv { \left[ \begin{array} { l } { \mathbf { b } } \\ { \mathbf { e } } \end{array} \right] }
$$

where $R$ is upper triangular. Eq. (5.4.24) can now be written as

$$
J = \| [ { \binom { R } { O } } \mathbf { x } - [ \mathbf { b } ] \| ^ { 2 }
$$

or

$$
J = \left\| R \mathbf { x } - \mathbf { b } \right\| ^ { 2 } + \left\| \mathbf { e } \right\| ^ { 2 }
$$

as noted before. The minimum value of $J$ is found by choosing $\hat { \bf x }$ so that

$$
R \hat { \mathbf { x } } - \mathbf { b } = 0 .
$$

The vector $\hat { \bf x }$ is obtained by the backward substitution described by Eq. (5.2.8), where $z$ and $r$ are replaced by $b$ and $R$ , respectively. Observe that $\hat { \bf x }$ usually would be determined after processing all observations. However, intermediate values of $\hat { \bf x }$ could be determined at any point in the process.

The minimum value of $J$ is given by substituting $\hat { \bf x }$ into Eq. (5.4.24):

$$
J = \left\| \mathbf { e } \right\| ^ { 2 } = \sum _ { i = 1 } ^ { m } e _ { i } ^ { 2 } = \left\| { \overline { { R } } } { \hat { \mathbf { x } } } - { \overline { { \mathbf { b } } } } \right\| ^ { 2 } + \sum _ { i = 1 } ^ { m } \left( H _ { i } { \hat { \mathbf { x } } } - y _ { i } \right) ^ { 2 } .
$$

Note that the first term on the right-hand side of Eq. (5.4.30) corresponds to the norm of the error in the a priori value for $\mathbf { x }$ multiplied by the square root of the inverse of the a priori covariance matrix,

$$
\| \overline { { R } } \hat { \mathbf { x } } - \overline { { \mathbf { b } } } \| ^ { 2 } = \| \overline { { R } } ( \hat { \mathbf { x } } - \overline { { \mathbf { x } } } ) \| ^ { 2 }
$$

which also can be expressed as

$$
\left\| \overline { { R } } ( \widehat { \mathbf { x } } - \overline { { \mathbf { x } } } ) \right\| ^ { 2 } = ( \widehat { \mathbf { x } } - \overline { { \mathbf { x } } } ) ^ { T } \overline { { P } } ^ { - 1 } ( \widehat { \mathbf { x } } - \overline { { \mathbf { x } } } ) .
$$

From Eqs. (5.4.30) and (5.4.31) it is seen that

$$
\sum _ { i = 1 } ^ { m } e _ { i } ^ { 2 } = \| \overline { { R } } ( \hat { \mathbf { x } } - \overline { { \mathbf { x } } } ) \| ^ { 2 } + \sum _ { i = 1 } ^ { m } \left( H _ { i } \hat { \mathbf { x } } - y _ { i } \right) ^ { 2 }
$$

or

$$
\begin{array} { c } { \displaystyle \sum _ { i = 1 } ^ { m } e _ { i } ^ { 2 } = \| \overline { { R } } \hat { \pmb { \eta } } \| ^ { 2 } + \displaystyle \sum _ { i = 1 } ^ { m } \hat { \epsilon } _ { i } ^ { 2 } } \\ { \displaystyle = \hat { \pmb { \eta } } ^ { T } \overline { { R } } ^ { T } \overline { { R } } \hat { \pmb { \eta } } + \displaystyle \sum _ { i = 1 } ^ { m } \hat { \epsilon } _ { i } ^ { 2 } , } \end{array}
$$

where

$$
\hat { \pmb { \eta } } = \hat { \bf x } - \overline { { { \bf x } } } , \hat { \epsilon } _ { i } = y _ { i } - H _ { i } \hat { \bf x } .
$$

Consequently, $e _ { i } \neq \hat { \epsilon } _ { i }$ ; that is, the elements of the error vector $[ \mathbf { e } ] _ { m \times 1 }$ contain a contribution from errors in the $a$ priori information as well as the observation residuals. The RMS of the observation residuals, $\boldsymbol { \hat { \epsilon } } _ { i }$ , is given by

$$
\mathrm { R M S } = \sqrt { \frac { 1 } { m } \sum _ { i = 1 } ^ { m } \hat { \epsilon } _ { i } ^ { 2 } }
$$

and from Eq. (5.4.33)

$$
\sum _ { i = 1 } ^ { m } \hat { \epsilon } _ { i } ^ { 2 } = \sum _ { i = 1 } ^ { m } e _ { i } ^ { 2 } - \hat { \eta } ^ { T } \overline { { { R } } } ^ { T } \overline { { { R } } } \hat { \eta } .
$$

If the procedure is initialized with $n$ observations in place of $a$ priori information, $\overline { { \mathbf { x } } }$ and $\overline { { P } }$ , Eq. (5.4.33) becomes

$$
\sum _ { i = 1 } ^ { m - n } e _ { i } ^ { 2 } = \sum _ { i = 1 } ^ { m } \hat { \epsilon } _ { i } ^ { 2 }
$$

and again $e _ { i } \neq \hat { \epsilon } _ { i }$ because the first $n$ observations serve the same function as $a$ priori values of $\overline { { \mathbf { x } } }$ and $\overline { { P } }$ . Here we have assumed that the weighting matrix is the identity matrix. If not, $( H _ { i } { \hat { \mathbf { x } } } - y _ { i } ) ^ { 2 }$ in Eq. (5.4.30) and subsequent equations should be replaced by $W _ { i } ( H _ { i } \hat { \mathbf { x } } - y _ { i } ) ^ { 2 }$ .

An advantage of the orthogonal transformation approach, in addition to improved accuracy, is that the sum of squares of the residuals, $e _ { i }$ , based on the final value of $\hat { \bf x }$ is computed automatically as part of the solution procedure. To obtain this result with the conventional batch processor, one would have to go through the additional computation of evaluating Eq. (5.4.30) after solving the normal equations for $\hat { \bf x }$ .

This procedure of solving the least squares problem using orthogonal transformations can be described as a square root information batch processor. If the state vector is independent of time, it could be thought of as a filter because the best estimate of $\mathbf { x }$ could be generated after processing each observation. If the state vector is a function of time, the $H$ matrix must be combined with the state transition matrix to map the state to an epoch time as described in Chapter 4. As formulated here, it could not be implemented as a $\mathbf { f }$ ter without mapping the square root information matrix, $R$ , and the state estimate, $\hat { \bf x }$ , to the appropriate time for each observation. The square root information filter with time-dependent effects is described in Section 5.10.1.

In summary, given a priori information $\overline { { R } }$ and $\overline { { \mathbf { b } } }$ and observations

$$
y _ { i } = H _ { i } \mathbf { x } + \epsilon _ { i } , i = 1 , \ldots , m ,
$$

the matrix we wish to reduce to upper triangular form is

$$
[ \begin{array} { c c } { { { \overline { { { R } } } } } } & { { { \bf { \overline { { { b } } } } } } } \\ { { { \cal H } _ { 1 } } } & { { y _ { 1 } } } \\ { { { \cal H } _ { 2 } } } & { { y _ { 2 } } } \\ { { \vdots } } & { { \vdots } } \\ { { { \cal H } _ { m } } } & { { y _ { m } } } \end{array} ] \ \{ \begin{array} { c c }  { \scriptstyle \mathrm { ~ \} n } } \\ { { \bf \sigma } } \\ { { \bf \sigma } } \end{array} 
$$

where $\overline { { R } }$ is upper triangular.

# 5.4.2 GIVENS COMPUTATIONAL ALGORITHM

For purposes of the computational algorithm we will write Eq. (5.4.38) as

$$
\begin{array} { r l r } & { \overbrace { \left[ \begin{array} { l l } { \overline { { R } } } & { \begin{array} { l } { \overline { { \mathbf { b } } } } \\ { H } & { \begin{array} { l } { \mathbf { y } } \end{array} } } \end{array} \right] } ^ { n } } &  \} \end{array} \overbrace { \begin{array} { l } { \} { n + 1 } \end{array} } } & { } \\ & { \left[ \begin{array} { l } { \begin{array} { l } { \overline { { R } } } \\ { H } \end{array} } \end{array} \right] \} n } &  \} &  \} \end{array}
$$

Lowercase $r$ and $h$ in the following algorithm represent the elements of $\widetilde { R }$ and $\widetilde { H }$ respectively, in Eq. (5.4.39).

The algorithm using the Givens rotation for reducing the $( m + n ) \times ( n + 1 )$ matrix of Eq. (5.4.39) to upper triangular form can be expressed as follows:

$\mathrm { S u m } = 0 .$ 1. Do $k = 1 , . . . , m$

2. Do $i = 1 , \ldots , n$ If ( $h _ { k i } = 0 \mathrm { ~ , ~ }$ ) Go to 2

$$
\begin{array} { r l } & { r _ { i i } ^ { \prime } = \sqrt { r _ { i i } ^ { 2 } + h _ { k i } ^ { 2 } } } \\ & { S _ { i k } = h _ { k i } / r _ { i i } ^ { \prime } } \\ & { C _ { i k } = r _ { i i } / r _ { i i } ^ { \prime } } \\ & { h _ { k i } = 0 } \\ & { r _ { i i } = r _ { i i } ^ { \prime } } \end{array}
$$

3. Do $j = i + 1 , \ldots , n + 1$

$$
\begin{array} { r l } & { r _ { i j } ^ { \prime } = C _ { i k } r _ { i j } + S _ { i k } h _ { k j } } \\ & { h _ { k j } = - S _ { i k } r _ { i j } + C _ { i k } h _ { k j } } \\ & { r _ { i j } = r _ { i j } ^ { \prime } } \end{array}
$$

Next $j$   
Next $i$   
$\begin{array} { l } { e _ { k } = h _ { k j } } \\ { \mathrm { S u m } = \mathrm { S u m } + e _ { k } ^ { 2 } } \\ { \mathrm { N e x t } \ : k } \end{array}$

After application of this algorithm, the $( n + m ) \times ( n + 1 )$ matrix will appear

as

$$
Q [ { \begin{array} { l } { { \overline { { R } } } \colon { \overline { { \mathbf { b } } } } } \\ { H \colon \mathbf { y } } \end{array} } ] = { \pmod { \overbrace { R } } } \quad { \overbrace { \mathbf { b } } } ^ { n } ] \} n
$$

which is the required form for solution of the least squares estimation problem as given by Eq. (5.3.6). Note that $r _ { i , n + 1 } ( i = 1 , \dots , n )$ and $h _ { k , n + 1 } ( k = 1 , \ldots , m )$ given by the algorithm represent $\mathbf { b }$ and $\mathbf { e }$ , respectively, in Eq. (5.4.41). Also, $\begin{array} { r } { \mathrm { S u m } = \sum _ { k = 1 } ^ { m } e _ { k } ^ { 2 } } \end{array}$ .

Once the array has been reduced to the form given by Eq. (5.4.41), subsequent observations can be included by considering the following array:

$$
\left[ \begin{array} { c } { { R \mathbf b } } \\ { { H _ { m + 1 } y _ { m + 1 } } } \\ { { 0 \mathbf \Lambda } } \end{array} \right] =
$$

$$
\left[ \begin{array} { c c c c c } { R _ { 1 1 } } & { R _ { 1 2 } } & { \cdots } & { R _ { 1 n } } & { b _ { 1 } } \\ { 0 } & { R _ { 2 2 } } & { \cdots } & { R _ { 2 n } } & { b _ { 2 } } \\ { 0 } & { 0 } & { \cdots } & { R _ { 3 n } } & { b _ { 3 } } \\ { \vdots } & { } & { } & { } & { } \\ { 0 } & { 0 } & { \cdots } & { R _ { n n } } & { b _ { n } } \\ { H _ { m + 1 , 1 } H _ { m + 1 , 2 } \cdots H _ { m + 1 , n } y _ { m + 1 } } & { } & { } \\ { 0 } & { 0 } & { \cdots } & { 0 } & { e ^ { 2 } } \end{array} \right]
$$

where

$$
e ^ { 2 } = \sum _ { k = 1 } ^ { m } e _ { k } ^ { 2 } = \mathrm { S u m } .
$$

Then by application of a Givens rotation to rows 1 and $n + 1$ , $H _ { m + 1 , 1 }$ can be nulled. Successive applications moving down the main diagonal can be used to null the remaining $n - 1$ elements of the $n + 1 ^ { \mathrm { s t } }$ row and reduce the array to upper triangular form:

$$
\left[ \begin{array} { l l } { R ^ { \prime } } & { \mathbf { b } ^ { \prime } } \\ { 0 } & { e _ { m + 1 } } \\ { 0 } & { e ^ { 2 } } \end{array} \right] .
$$

Next $e ^ { 2 }$ is replaced by $e ^ { 2 } + e _ { m + 1 } ^ { 2 }$ and the procedure is repeated with the next observation, and so on. It is also obvious that a group of $m ^ { \prime }$ observations could be included by replacing the array $\left( H _ { m + 1 } , y _ { m + 1 } \right)$ with an array in which $H _ { m + 1 }$ has dimension $( m ^ { \prime } \times n )$ and $\mathbf { y } _ { m + 1 }$ has dimension $m ^ { \prime }$ . The Givens rotation would be used as before to reduce the augmented array to upper triangular form. Note that Sum is set to zero only before processing the first observation or batch of observations. Also note that if there are different observation types, e.g., range and range rate, the values of $e$ for each observation type should be stored in separate arrays.

The Givens algorithm operates on an individual row (i.e., observation) until it is in the proper form and then moves to the next row of the matrix. The algorithm can also be applied so that it operates column by column simply by interchanging the $k$ and $i$ loops. The same procedure just described for processing a new observation or batch of observations still applies. The following Givens algorithm operates on the successive columns.

$\mathrm { S u m } = 0 .$ 1. Do $i = 1 , \ldots , n$ 2. Do $k = 1 , \ldots , m$

If ( $h _ { k i } = 0 \mathrm { ~ , ~ }$ ) Go to 2

$$
\begin{array} { r l } & { r _ { i i } ^ { \prime } = \sqrt { r _ { i i } ^ { 2 } + h _ { k i } ^ { 2 } } } \\ & { S _ { i k } = h _ { k i } / r _ { i i } ^ { \prime } } \\ & { C _ { i k } = r _ { i i } / r _ { i i } ^ { \prime } } \\ & { h _ { k i } = 0 } \\ & { r _ { i i } = r _ { i i } ^ { \prime } } \end{array}
$$

3. Do $j = i + 1 , \ldots , n + 1$

$$
\begin{array} { r l } & { r _ { i j } ^ { \prime } = C _ { i k } r _ { i j } + S _ { i k } h _ { k j } } \\ & { h _ { k j } = - S _ { i k } r _ { i j } + C _ { i k } h _ { k j } } \\ & { r _ { i j } = r _ { i j } ^ { \prime } } \end{array}
$$

Next $j$

Next $k$

Next $i$

Do $\ell = 1 , \ldots , m$

$$
\mathrm { S u m } = \mathrm { S u m } + h _ { \ell , n + 1 } ^ { 2 }
$$

Next 

# 5.4.3 SQUARE ROOT FREE GIVENS TRANSFORMATION

The original Givens transformation requires the formation of square roots, which are more complex to compute than divisions or multiplications. The following procedure leads to a square root free algorithm.

Rather than seek the orthogonal transformation $Q$ , which leads to $Q W ^ { 1 / 2 } H =$ $[ R ^ { T } : 0 ] ^ { T }$ , we seek a factorization of $R$ of the form

$$
R = D ^ { \frac { 1 } { 2 } } U
$$

where $D$ is an $n \times n$ diagonal matrix and $U$ is $n \times n$ unit upper triangular matrix,

i.e.

$$
\begin{array} { r } { D ^ { 1 / 2 } = \left[ \begin{array} { l } { d _ { 1 } ^ { 1 / 2 } \qquad 0 } \\ { \quad d _ { 2 } ^ { 1 / 2 } \qquad } \\ { \cdot \qquad \cdot } \\ { 0 \qquad \quad d _ { n } ^ { 1 / 2 } } \end{array} \right] , U = \left[ \begin{array} { l l l l l } { 1 } & { U _ { 1 2 } } & { \cdot \cdot } & { U _ { 1 n } } \\ { 0 } & { 1 } & { U _ { 2 3 } } & { \cdot \cdot } & { U _ { 2 n } } \\ { \vdots } & & & { \vdots } \\ { 0 } & { \cdot \cdot } & { \cdot \cdot } & { \cdot \cdot } & { 1 } \end{array} \right] . } \end{array}
$$

Following Eq. (5.3.6) select the orthogonal matrix $Q$ , such that

$$
\begin{array} { r } { Q W ^ { \frac { 1 } { 2 } } H = \left[ \begin{array} { c } { D ^ { \frac { 1 } { 2 } } U } \\ { 0 } \end{array} \right] = \left[ \begin{array} { c c c c } { D ^ { \frac { 1 } { 2 } } \vdots } & { 0 } \\ { \cdots } & { \cdots } \\ { 0 } & { \vdots } & { 0 } \end{array} \right] \left[ \begin{array} { c } { U } \\ { \cdots } \\ { 0 } \end{array} \right] } \end{array}
$$

and

$$
Q W ^ { \frac { 1 } { 2 } } \mathbf { y } = \left[ \mathbf { b } \right] .
$$

Let

$$
{ \bf b } = D ^ { \frac { 1 } { 2 } } \widetilde { { \bf b } } .
$$

It follows from Eq. (5.3.7) that the least squares performance index can be expressed as

$$
J ( \mathbf { x } ) = \left\| \left[ { \cal D } ^ { \frac { 1 } { 2 } } U \right] \mathbf { x } - \left[ { \cal D } ^ { \frac { 1 } { 2 } } \widetilde { \mathbf { b } } \right] \right\| ^ { 2 }
$$

which for a minimum requires

$$
D ^ { \frac { 1 } { 2 } } U \hat { \mathbf { x } } = D ^ { \frac { 1 } { 2 } } \widetilde { \mathbf { b } } .
$$

Since $D ^ { 1 / 2 }$ is common to both sides of Eq. (5.4.48), the solution is

$$
U \hat { \mathbf { x } } = \widetilde { \mathbf { b } }
$$

and $\hat { \bf x }$ is obtained by backward recursion. Because the diagonals of $U$ are unitary, division by the $n$ diagonal elements is eliminated.

Consider now the use of the square root free Givens transformation to obtain the orthogonal decomposition (Gentleman, 1973). The product $W ^ { 1 / 2 } H$ can be

expressed in component form as

$$
W ^ { \frac { 1 } { 2 } } H = \left[ { \begin{array} { c c c } { \sigma _ { 1 } h _ { 1 1 } } & { \sigma _ { 1 } h _ { 1 2 } } & { \cdots } & { \sigma _ { 1 } h _ { 1 n } } \\ { \sigma _ { 2 } h _ { 2 1 } } & { \sigma _ { 2 } h _ { 2 2 } } & { \cdots } & { \sigma _ { 2 } h _ { 2 n } } \\ { \vdots } \\ { \sigma _ { m } h _ { m 1 } \sigma _ { m } h _ { m 2 } } & { \cdots } & { \sigma _ { m } h _ { m n } } \end{array} } \right]
$$

where

$$
\sigma _ { i } = W _ { i i } ^ { \frac { 1 } { 2 } } , W _ { i j } ^ { \frac { 1 } { 2 } } = 0 , i \neq j .
$$

Now consider the application of the Givens rotation, where any two rows of Eq. (5.4.19) are expressed in the form

$$
\begin{array} { r l r } & { } & { G \left[ \sqrt { d _ { i } } \qquad \sqrt { d _ { i } } \ l _ { i , i + 1 } \ \cdots \sqrt { d _ { i } } \ l _ { i n } \ \right] } \\ & { } & { \qquad \sqrt { \delta _ { k } } \ h _ { k i } \ \sqrt { \delta _ { k } } \ h _ { k , i + 1 } \cdot \cdot \cdot \sqrt { \delta _ { k } } \ h _ { k n } \ \biggr ] } \\ & { } & { = \left[ \sqrt { d _ { i } ^ { \prime } } \ \sqrt { d _ { i } ^ { \prime } } \ l _ { i , i + 1 } ^ { \prime } \ \cdots \sqrt { d _ { i } ^ { \prime } } \ l _ { i n } ^ { \prime } \ \right] . } \\ & { } & \end{array}
$$

From Eq. (5.4.50), it follows that

$$
\begin{array} { c } { \sqrt { d _ { i } } = \sigma _ { i } h _ { i i } } \\ { \ } \\ { l _ { i j } = \sigma _ { i } h _ { i j } / \sigma _ { i } h _ { i i } , j = i + 1 , \ldots , , n } \\ { \sqrt { \delta _ { k } } = \sigma _ { k } . } \end{array}
$$

Then from Eq. (5.4.51), the Givens transformation, Eq. (5.4.2), applied to the first column leads to

$$
\begin{array} { c } { { \sqrt { d ^ { \prime } } = \cos \theta \sqrt { d _ { i } } + \sin \theta \sqrt { \delta _ { k } } h _ { k i } } } \\ { { 0 = - \sin \theta \sqrt { d _ { i } } + \cos \theta \sqrt { \delta _ { k } } h _ { k i } . } } \end{array}
$$

The second of Eq. (5.4.53) can be used to obtain

$$
\tan \theta = \frac { \sin \theta } { \cos \theta } = \frac { \sqrt { \delta _ { k } } h _ { k i } } { \sqrt { d _ { i } } }
$$

and hence

$$
\sin \theta = \sqrt { \delta _ { k } } h _ { k i } \bigg / \sqrt { d _ { i } + \delta _ { k } h _ { k i } ^ { 2 } }
$$

$$
\cos \theta = \sqrt { d _ { i } } \bigg / \sqrt { d _ { i } + \delta _ { k } h _ { k i } ^ { 2 } } .
$$

Substituting (5.4.54) into (5.4.53) leads to

$$
\sqrt { d _ { i } ^ { \prime } } = \sqrt { d _ { i } + \delta _ { k } h _ { k i } ^ { 2 } } .
$$

Hence, Eq. (5.4.54) becomes

$$
\sin \theta = \sqrt { \delta _ { k } } \ h _ { k i } / \sqrt { d _ { i } ^ { \prime } } ; \cos \theta = \sqrt { d _ { i } } / \sqrt { d _ { i } ^ { \prime } } .
$$

Then for the general transformation, the $i j ^ { \mathrm { t h } }$ element of the first row is

$$
\begin{array} { r l r } & { } & { \sqrt { d _ { i } ^ { \prime } } \ell _ { i j } ^ { \prime } = \cos \theta \sqrt { d _ { i } } \ell _ { i j } + \sin \theta \sqrt { \delta _ { k } } h _ { k j } } \\ & { } & { \quad = \frac { \sqrt { d _ { i } } \sqrt { d _ { i } } } { \sqrt { d _ { i } ^ { \prime } } } \ell _ { i j } + \frac { \sqrt { \delta _ { k } } h _ { k i } \sqrt { \delta _ { k } } } { \sqrt { d _ { i } ^ { \prime } } } h _ { k j } . } \end{array}
$$

Now, dividing by $\sqrt { d _ { i } ^ { \prime } }$ , yields

$$
\ell _ { i j } ^ { \prime } = \frac { d _ { i } } { d _ { i } ^ { \prime } } \ell _ { i j } + \frac { \delta _ { k } } { d _ { i } ^ { \prime } } h _ { k i } h _ { k j } .
$$

Using the definitions

$$
\overline { { C _ { i } } } = d _ { i } / d _ { i } ^ { \prime } , \overline { { S } } _ { i } = \delta _ { k } h _ { k i } / d _ { i } ^ { \prime }
$$

Eq. (5.4.57) becomes

$$
\ell _ { i j } ^ { \prime } = \overline { { C } } _ { i } \ell _ { i j } + \overline { { S } } _ { i } h _ { k j } .
$$

Similarly, the $k j ^ { \mathrm { t h } }$ element of the $k ^ { \mathrm { t h } }$ row is

$$
\sqrt { \delta _ { k } ^ { \prime } } h _ { k j } ^ { \prime } = - \sin \theta \sqrt { d _ { i } } \ell _ { i j } + \cos \theta \sqrt { \delta _ { k } } h _ { k j } .
$$

Then, using Eq. (5.4.56) results in

$$
\sqrt { \delta _ { k } ^ { \prime } } h _ { k j } ^ { \prime } = \frac { - \sqrt { \delta _ { k } } h _ { k i } } { \sqrt { d _ { i } ^ { \prime } } } \sqrt { d _ { i } } \ l _ { i j } + \frac { \sqrt { d _ { i } } } { \sqrt { d _ { i } ^ { \prime } } } \sqrt { \delta _ { k } } h _ { k j } .
$$

Dividing by $\sqrt { \delta _ { k } ^ { \prime } }$ leads to

$$
h _ { k j } ^ { \prime } = \frac { \sqrt { d _ { i } } } { \sqrt { d _ { i } ^ { \prime } } } \frac { \sqrt { \delta _ { k } } } { \sqrt { \delta _ { k } ^ { \prime } } } h _ { k j } - \frac { \sqrt { \delta _ { k } } \sqrt { d _ { i } } } { \sqrt { d _ { i } ^ { \prime } } \sqrt { \delta _ { k } ^ { \prime } } } h _ { k i } l _ { i j } .
$$

Because $\sqrt { \delta _ { k } ^ { \prime } }$ is an arbitrary scaling factor for each element of the $k ^ { \mathrm { t h } }$ row, it is convenient to let

$$
\sqrt { \delta _ { k } ^ { \prime } } = \sqrt { \delta _ { k } } \times \frac { \sqrt { d _ { i } } } { \sqrt { d _ { i } ^ { \prime } } } .
$$

It then follows that Eq. (5.4.60) can be expressed as

$$
\begin{array} { r } { h _ { k j } ^ { \prime } = h _ { k j } - h _ { k i } l _ { i j } . } \end{array}
$$

The final values of $l _ { i j } ^ { \prime }$ become the elements of $U _ { i j }$ and $\tilde { b } _ { i }$ , and $h _ { k j } ^ { \prime }$ are the interim elements of the $_ \mathrm { H }$ matrix. The final value of $h _ { k j } ^ { \prime }$ in each row is the observation error. This will become clear from the examples of Section 5.6.

# 5.4.4 SQUARE ROOT FREE GIVENS COMPUTATIONAL ALGORITHM

If a priori information, $\overline { { \mathbf { x } } }$ and $\overline { { P } }$ , are available the algorithm is initialized by computing $\overline { S }$ and $\overline { { R } }$ where

$$
\overline { { P } } = \overline { { S } } \overline { { S } } ^ { T }
$$

and

$$
\overline { { { R } } } = \overline { { { S } } } ^ { - 1 } .
$$

The a priori information we need is ${ \overline { { D } } } , { \overline { { U } } }$ , and $\widetilde { \mathbf { b } }$ , where

$$
{ \overline { { R } } } = { \overline { { D } } } ^ { \frac { 1 } { 2 } } { \overline { { U } } } .
$$

Hence,

$$
\overline { { d } } _ { i } = \overline { { R } } _ { i i } ^ { 2 } \ i = 1 \dots n
$$

and

$$
\overline { { U } } = \left[ \begin{array} { l l l l } { 1 \overline { { U } } _ { 1 2 } \cdots \cdots \cdots \overline { { U } } _ { 1 n } } \\ { 0 \quad 1 \overline { { U } } _ { 2 3 } \cdots \overline { { U } } _ { 2 n } } \\ { 0 \quad 0 \quad 1 } & { \vdots } \\ { \vdots } & { \ddots } & { \vdots } \\ { 0 \quad \cdots \cdots \cdots \cdots } & { 1 } \end{array} \right] ,
$$

where $\overline { { d } } _ { i }$ are the square of the diagonal elements of $\overline { { R } }$ ; for example, $d _ { i } = R _ { i i } ^ { 2 }$ , $i = 1 , \ldots , n$ , and $\overline { { U } } _ { i j } = \overline { { R } } _ { i j } / \overline { { R } } _ { i i } ; i = 1 , \dots n ; j = i + 1 , n$ . Also, recall from Eq. (5.4.21) that

$$
\overline { { { \bf b } } } = \overline { { R } } \overline { { \bf x } }
$$

and the a priori value of $\widetilde { \mathbf { b } } \equiv \overline { { \widetilde { \mathbf { b } } } }$ is

$$
\overline { { \widetilde { { \bf b } } } } = \overline { { \cal D } } ^ { - \frac { 1 } { 2 } } \overline { { { \bf b } } } .
$$

Given observations $y _ { i }$ and $i = 1 \dots m$ , we now have the necessary information to execute the algorithm; that is, we wish to apply a series of orthogonal transformations, $G$ , so that

$$
\begin{array} { r l r } { G } &  { } [ \begin{array} { c c c c c } { \stackrel { n } { \longrightarrow } } & { \stackrel {  } { \longrightarrow } } & { \quad } & { \stackrel { n } { \longrightarrow } } & { \stackrel {  } { \longrightarrow } } \\ { \overline { { U } } } & { \stackrel {  } { \tilde { \textbf { b } } } } \\ { \hfill ~ [ \begin{array} { c c c c c } { y _ { 1 } } & { \frac { \pi } { \tilde { \textbf { b } } } } \\ { y _ { 1 } } & { \frac { \pi } { y _ { 1 } } } \\ { \vdots } & { \vdots } \\ { H _ { m } } & { y _ { m } } \end{array} ] \} ^ { h } } & { { } = } & { { } [ \begin{array} { c c c c c } { \overbrace { U } } & { \stackrel {  } { \tilde { \textbf { b } } } } \\ { 0 } & { \stackrel { e _ { 1 } } { e _ { 1 } } } \\ { 0 } & { \vdots } \\ { e _ { m } } \end{array} ] \Bigg \} _ { m } ^ { h } \ . } \end{array} \end{array}
$$

The computational algorithm for operating on the data one row, or one observation, at a time is as follows:

$$
\begin{array} { l l } { { \mathrm { S u m } = 0 } } \\ { { \qquad } } \\ { { U _ { i i } = 1 } } & { { \qquad i = 1 , \dots , n } } \end{array}
$$

1. Do $k = 1 , \ldots , m$

$$
\delta _ { k } = 1
$$

2. Do $i = 1 , \ldots , n$

If $h _ { k i } = 0$ ) Go to 2

$$
\begin{array} { l } { { d _ { i } ^ { \prime } = d _ { i } + \delta _ { k } h _ { k i } ^ { 2 } } } \\ { { \overline { { C } } = d _ { i } / d _ { i } ^ { \prime } } } \\ { { \overline { { S } } = \delta _ { k } h _ { k i } / d _ { i } ^ { \prime } } } \\ { { y _ { k } ^ { \prime } = y _ { k } - \bar { b } _ { i } h _ { k i } } } \\ { { \tilde { b } _ { i } - \tilde { b } _ { i } \overline { { C } } + y _ { k } \overline { { S } } } } \\ { { y _ { k } = y _ { k } ^ { \prime } } } \\ { { \delta _ { k } = \delta _ { k } \overline { { C } } } } \\ { { d _ { i } = d _ { i } ^ { \prime } } } \end{array}
$$

3. Do $j = i + 1 , \dotsc , n$

$$
\begin{array} { l } { { { h } _ { k j } ^ { \prime } = { h } _ { k j } - { U } _ { i j } { h } _ { k i } } } \\ { { { U } _ { i j } = { U } _ { i j } \overline { { C } } + { h } _ { k j } \overline { { S } } } } \\ { { { h } _ { k j } = { h } _ { k j } ^ { \prime } } } \end{array}
$$

$$
\begin{array} { l } { \operatorname { N e x t } ~ j } \\ { \operatorname { N e x t } ~ i } \\ { e _ { k } = \sqrt { \delta _ { k } } y _ { k } } \\ { \operatorname { S u m } = \operatorname { S u m } + e _ { k } ^ { 2 } } \end{array}
$$

Next k

The diagonal elements of $D$ are given by $d _ { i } ( i = 1 , \ldots , n )$ , the upper triangular elements of $U$ are given by $U _ { i j } ( i = 1 , \ldots , n , \ j = i + 1 , \ldots , n + 1 )$ , the elements of $\widetilde { \mathbf { b } }$ are given by $\tilde { b } _ { i }$ $( i = 1 , \ldots , n )$ and the elements of $\mathbf { e }$ are given by $e _ { k } ( k = 1 , \ldots , m )$ . The same procedure described for the Givens algorithm at the end of Section 5.4.2 can be used to handle multiple batches of observation data. Note that Sum and $\delta _ { k }$ are set to zero and one, respectively, only for the fir st batch of observations.

The vector $\hat { \bf x }$ is obtained from $U$ and $\widetilde { \mathbf { b } }$ by performing a back substitution using Eq. (5.4.49). Note that $D$ is not needed to compute $\hat { \bf x }$ but is needed to compute the estimation error covariance matrix, $P = U ^ { - 1 } D ^ { - 1 } U ^ { - T }$ (see Eq. (5.4.80)).

# 5.4.5 A SIMPLIFIED SQUARE ROOT FREE GIVENS TRANSFORMATION

The square root free Givens algorithm can be simplified further (Gentleman, 1973) by noting that we may write

$$
\begin{array} { r } { y _ { k } ^ { \prime } = y _ { k } - \tilde { b } _ { i } h _ { k i } } \\ { \tilde { b } _ { i } ^ { \prime } = \tilde { b } _ { i } \overline { { C } } + y _ { k } \overline { { S } } } \end{array}
$$

and

$$
\begin{array} { l } { { h _ { k j } ^ { \prime } = h _ { k j } - U _ { i j } h _ { k i } } } \\ { { U _ { i j } ^ { \prime } = U _ { i j } \overline { { C } } + h _ { k j } \overline { { S } } } } \end{array}
$$

as

$$
\begin{array} { l } { { y _ { k } ^ { \prime } = y _ { k } - \tilde { b } _ { i } h _ { k i } } } \\ { { \tilde { b } _ { i } ^ { \prime } = \tilde { b } _ { i } + y _ { k } ^ { \prime } \overline { { { S } } } } } \end{array}
$$

and

$$
\begin{array} { l } { { h _ { k j } ^ { \prime } = h _ { k j } - U _ { i j } ~ h _ { k i } } } \\ { { U _ { i j } ^ { \prime } = U _ { i j } + h _ { k j } ^ { \prime } ~ \overline { { { S } } } } } \end{array}
$$

by noting that

$$
\overline { { C } } = 1 - \overline { { S } } h _ { k i } .
$$

Hence, the algorithm may be simplified by eliminating the need to compute $\overline { { C } }$ explicitly. The computational algorithm becomes

$$
\mathrm { S u m } = 0 .
$$

1. Do $k = 1 , \ldots , m$

$$
\delta _ { k } = 1
$$

2. Do $i = 1 , \ldots , n$

If $h _ { k i } = 0$ ) go to 2

$$
\begin{array} { r l } & { d _ { i } ^ { \prime } = d _ { i } + \delta _ { k } \ h _ { k i } ^ { 2 } } \\ & { \overline { { S } } = \delta _ { k } \ h _ { k i } / d _ { i } ^ { \prime } } \\ & { y _ { k } ^ { \prime } = y _ { k } - \tilde { b } _ { i } \ h _ { k i } } \\ & { \tilde { b } _ { i } = \tilde { b } _ { i } + y _ { k } ^ { \prime } \ \overline { { S } } } \\ & { y _ { k } = y _ { k } ^ { \prime } } \\ & { \delta _ { k } = \delta _ { k } \ d _ { i } / d _ { i } ^ { \prime } } \\ & { d _ { i } = d _ { i } ^ { \prime } } \end{array}
$$

3. Do $j = i + 1 , \dotsc , n$

$$
\begin{array} { l } { { h _ { k j } ^ { \prime } = h _ { k j } - U _ { i j } \ : h _ { k i } } } \\ { { \ : U _ { i j } = U _ { i j } + h _ { k j } ^ { \prime } \ : \overline { { S } } } } \\ { { h _ { k j } = h _ { k j } ^ { \prime } } } \end{array}
$$

$$
\begin{array} { c } { { e _ { k } = \sqrt { \delta _ { k } } y _ { k } } } \\ { { \mathrm { S u m = S u m + } e _ { k } ^ { 2 } } } \end{array}
$$

This version of the square root free Givens algorithm is preferred because it involves fewer operations than that of Eq. (5.4.70).

# 5.4.6 IMPLEMENTATION CONSIDERATIONS

The following observations on the square root free algorithm are given:

1. Note that no square roots are required.

2. The algorithm assumes that a priori information ${ \overline { { D } } } , { \overline { { U } } } .$ , and $\overline { { \widetilde { \mathbf { b } } } }$ computed from $\overline { { P } }$ and $\bar { \bf x }$ is available. These are computed using Eqs. (5.4.63) through (5.4.68):

$$
\begin{array} { l } { \overline { { P } } = \overline { { S } } \overline { { S } } ^ { T } } \\ { \overline { { R } } = \overline { { S } } ^ { - 1 } } \\ { \bar { d } _ { i } = \overline { { R } } _ { i i } ^ { 2 } , i = 1 \ldots n } \\ { \overline { { U } } = \overline { { D } } ^ { - 1 / 2 } \overline { { R } } } \\ { \overline { { \tilde { \mathbf { b } } } } = \overline { { D } } ^ { - 1 / 2 } \overline { { R } } \bar { \mathbf { x } } = \overline { { U } } \bar { \mathbf { x } } } \end{array}
$$

3. If no a priori information is given the algorithm may be initialized using

$$
\begin{array} { l } { \overline { { D } } = 1 0 ^ { - 1 6 \ddag } } \\ { \overline { { U } } = I } \\ { \overline { { \widetilde { \mathbf { b } } } } = 0 . } \end{array}
$$

4. When an unprimed variable appears on both sides of an equation, this is taken to represent a replacement.

5. Remember that an orthogonal transformation does not change the norm or Euclidian length of each column of the original matrix.

6. Each of the Givens algorithms (Eqs. (5.4.40), (5.4.70), and (5.4.76)) operates on the subject matrix row by row. They can be modifie d to operate column by column by interchanging the $k$ and $i$ loops.

The value of $\hat { \bf x }$ is computed from Eq. (5.4.49),

$$
U \hat { \mathbf { x } } = \widetilde { \mathbf { b } }
$$

by using the back substitution algorithm obtained by a slight modification of Eq. (5.2.8):

$$
\begin{array} { c } { { i = n , ~ n - 1 , \ldots , 1 } } \\ { { \nonumber } } \\ { { \hat { x } _ { i } = \tilde { b } _ { i } - \displaystyle \sum _ { j = i + 1 } ^ { n } U _ { i j } \hat { x } _ { j } . } } \end{array}
$$

The estimation error covariance is computed from

$$
\begin{array} { l } { P = R ^ { - 1 } ~ R ^ { - T } } \\ { \ = ( D ^ { \frac { 1 } { 2 } } ~ U ) ^ { - 1 } ( U ^ { T } D ^ { \frac { 1 } { 2 } } ) ^ { - 1 } } \\ { \ = U ^ { - 1 } D ^ { - \frac { 1 } { 2 } } ~ D ^ { - \frac { 1 } { 2 } } U ^ { - T } } \\ { \ = U ^ { - 1 } D ^ { - 1 } U ^ { - T } } \end{array}
$$

where $U ^ { - 1 }$ may be computed by using Eq. (5.2.20).

# 5.5 THE HOUSEHOLDER TRANSFORMATION

An alternate computational approach can be developed by using orthogonal reflections rather than the planar rotations used in the previous discussions. Such transformations, which are referred to as Householder transformations (Householder, 1958), have the advantage of nulling a complete column in a single operation. Consider the following matrix

$$
\boldsymbol { T } = \boldsymbol { I } - 2 \hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T }
$$

where $\hat { \mathbf { u } } ^ { T } \hat { \mathbf { u } } = 1$ . The matrix $T$ satisfies the following conditions:

1) $T$ is symmetric.   
2) $T$ is idempotent: $T ^ { 2 } = I$ .   
3) $T$ is orthogonal: $T T ^ { T } = I$ .

Proof: The first condition follows from the definition. Then, since $\hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T }$ is symmetric and $\hat { \mathbf { u } } ^ { T } \hat { \mathbf { u } } = 1$ ,

$$
\begin{array} { r l } & { T ^ { 2 } = ( I - 2 \hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T } ) ( I - 2 \hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T } ) = I - 4 \hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T } + 4 \hat { \mathbf { u } } ( \hat { \mathbf { u } } ^ { T } \hat { \mathbf { u } } ) \hat { \mathbf { u } } ^ { T } } \\ & { \quad \quad = I - 4 \hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T } + 4 \hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T } = I . } \end{array}
$$

From Properties 1 and 2, it follows that

$$
T ^ { 2 } = T T ^ { T } = I .
$$

![](images/47f3d7354e489691be705ec54ecc2f0e6c243cc8c10a56ade4ac0d50fac3c542.jpg)  
Figure 5.5.1: An elementary reflec tion.

Matrices of the form $T$ are called elementary Hermitian matrices, elementary reflectors , or Householder transformations. The geometric notion of a reflection is shown in Fig. 5.5.1 and can be developed as follows. Let $u _ { n }$ be the plane perpendicular to $\mathbf { u }$ . Let

$$
\hat { \mathbf { u } } = \mathbf { u } \big / \lVert \mathbf { u } \rVert
$$

and let ${ \boldsymbol { T } } \mathbf { z }$ be the reflection of $\mathbf { z }$ in the plane $u _ { n }$ —the mirror image of $\mathbf { z }$ where the plane $u _ { n }$ represents the mirror. That is,

$$
\mathbf { z } = ( \mathbf { z } ^ { T } \hat { \mathbf { u } } ) \hat { \mathbf { u } } + \mathbf { v }
$$

and

$$
\begin{array} { r } { T \mathbf { z } = - ( \mathbf { z } ^ { T } \hat { \mathbf { u } } ) \hat { \mathbf { u } } + \mathbf { v } . } \end{array}
$$

Eliminating $\mathbf { v }$ leads to

$$
- T \mathbf { z } + \mathbf { z } = 2 ( \mathbf { z } ^ { T } \hat { \mathbf { u } } ) \hat { \mathbf { u } } .
$$

Therefore,

$$
\begin{array} { r } { T \mathbf { z } = \mathbf { z } - 2 ( \mathbf { z } ^ { T } \hat { \mathbf { u } } ) \hat { \mathbf { u } } } \\ { = \mathbf { z } - 2 \hat { \mathbf { u } } ( \hat { \mathbf { u } } ^ { T } \mathbf { z } ) } \\ { = \mathbf { z } - 2 \hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T } \mathbf { z } } \end{array}
$$

where we have used the fact that $\mathbf { z } ^ { T } \hat { \mathbf { u } } = \hat { \mathbf { u } } ^ { T } \mathbf { z }$ because this quantity is a scalar. Finally,

$$
T \mathbf { z } = [ I - 2 \hat { \mathbf { u } } \hat { \mathbf { u } } ^ { T } ] \mathbf { z } .
$$

Hence,

$$
\begin{array} { r } { T = I - 2 \frac { \mathbf { u } \mathbf { u } ^ { T } } { \mathbf { u } ^ { T } \mathbf { u } } } \\ { = I - \beta \mathbf { u } \mathbf { u } ^ { T } } \end{array}
$$

where

$$
\displaystyle \beta = 2 / \mathbf { u } ^ { T } \mathbf { u } = 2 \Big / \| \mathbf { u } \| ^ { 2 } .
$$

The following additional properties are of use:

4) If $u _ { j }$ , the $j ^ { t h }$ component of $\mathbf { u }$ , is zero, then $( T \mathbf { z } ) _ { j } = z _ { j }$ . That is, if the $j ^ { t h }$ component of $\mathbf { u }$ is zero, then the transformation $T$ leaves the $j ^ { t h }$ component of $\mathbf { z }$ unchanged.

Proof: This can be verified by writing down the product $\mathbf { u } \mathbf { u } ^ { T }$ and noting that the $j ^ { t h }$ row and $j ^ { t h }$ column vanish if $u _ { j }$ is zero.

5) If $\mathbf { u }$ is perpendicular to $\mathbf { z }$ , then $T \mathbf { z } = \mathbf { z }$ .

Proof: Since $T \mathbf { z } = [ I - \beta \mathbf { u } \mathbf { u } ^ { T } ] \mathbf { z } = \mathbf { z } - \beta \mathbf { u } ( \mathbf { u } ^ { T } \mathbf { z } )$ , it follows that $\mathbf { u } ^ { T } \mathbf { z } = 0$ if $\mathbf { u }$ is perpendicular to $\mathbf { z }$ and hence that $T \mathbf { z } = \mathbf { z }$ .

$$
T \mathbf { z } = \mathbf { z } - \gamma \mathbf { u } , { \mathrm { w h e r e ~ } } \ \gamma = 2 \mathbf { z } ^ { T } \mathbf { u } / \mathbf { u } ^ { T } \mathbf { u } .
$$

Proof:

$$
\begin{array} { c } { { T \mathbf { z } = \left[ I - \frac { 2 \mathbf { u } \mathbf { u } ^ { T } } { \mathbf { u } ^ { T } \mathbf { u } } \right] \mathbf { z } = \mathbf { z } - 2 \mathbf { u } \mathbf { u } ^ { T } \mathbf { z } / \mathbf { u } ^ { T } \mathbf { u } } } \\ { { \mathrm { ~ } } } \\ { { \displaystyle = \mathbf { z } - \frac { 2 \left( \mathbf { z } ^ { T } \mathbf { u } \right) \mathbf { u } } { \mathbf { u } ^ { T } \mathbf { u } } = \mathbf { z } - 2 \left( \frac { \mathbf { z } ^ { T } \mathbf { u } } { \mathbf { u } ^ { T } \mathbf { u } } \right) \mathbf { u } } } \\ { { \mathrm { ~ } } } \\ { { \displaystyle = \mathbf { z } - \gamma \mathbf { u } . } } \end{array}
$$

Here we use the fact that $\mathbf { u } ^ { T } \mathbf { z }$ is a scalar; hence, $\mathbf { u } ^ { T } \mathbf { z } = \mathbf { z } ^ { T } \mathbf { u }$ . Note that the computation of $T$ requires significantly more computation than the computation of ${ \boldsymbol { T } } \mathbf { z }$ , if property 6 is used. Furthermore, using property 6, it is not necessary that $T$ be stored; only the elements of ${ \boldsymbol { T } } \mathbf { z }$ need to be stored.

The feature of the Householder transformation, $T$ , that is of crucial interest in this discussion is that $T$ can be used to introduce zeros into any column vector, $\mathbf { z }$ . One can always find an orthogonal matrix, $T$ , such that $T \mathbf { z } = - \sigma \mathbf { e } _ { 1 }$ where $\sigma$ is a scalar and $\mathbf { e } _ { 1 }$ is a unit vector in the direction of $z _ { 1 }$ , the first component of the column vector $\mathbf { z }$ . The constant $\sigma$ can be determined up to a sign by the fact that $T$ is orthogonal. That is,

$$
\| T \mathbf { z } \| ^ { 2 } = \| - \sigma \mathbf { e } _ { 1 } \| ^ { 2 } = \sigma ^ { 2 } = \| \mathbf { z } \| ^ { 2 } = \mathbf { z } ^ { T } \mathbf { z } .
$$

Therefore,

$$
\boldsymbol { \sigma } = \pm \| \mathbf { z } \| .
$$

To obtain the specific transformation, $T$ , which accomplishes this reduction, the vector, u, must be determined. If we define u as

$$
\mathbf { u } = \mathbf { z } + \sigma \mathbf { e } = { \left[ \begin{array} { l } { z _ { 1 } } \\ { z _ { 2 } } \\ { \vdots } \\ { z _ { n } } \end{array} \right] } + { \left[ \begin{array} { l } { \sigma } \\ { 0 } \\ { \vdots } \\ { 0 _ { n } } \end{array} \right] }
$$

where

$$
\begin{array} { c } { { \mathbf { e } = [ 1 0 0 0 \cdots \cdot 0 ] ^ { T } \mathrm { i s } \mathrm { a n } n \mathrm { v e c t c } } } \\ { { \phantom { e } } } \\ { { \sigma = \mathrm { s i g n } ( z _ { 1 } ) ( \mathbf { z } ^ { T } \mathbf { z } ) ^ { \frac { 1 } { 2 } } \phantom { e } } } \end{array}
$$

then the orthogonal transformation $T = I - \beta \mathbf { u } \mathbf { u } ^ { T }$ is an elementary refle ctor and

$$
T \mathbf { z } = - \sigma \mathbf { e }
$$

where

$$
\beta = \frac { 2 } { { \bf u } ^ { T } { \bf u } } .
$$

Proof: Writing the expression for ${ \boldsymbol { T } } \mathbf { z }$ yields

$$
\begin{array} { r l } & { T \mathbf { z } = \mathbf { z } - \beta \mathbf { u } \mathbf { u } ^ { T } \mathbf { z } } \\ & { \qquad = \mathbf { z } - \beta ( \mathbf { u } ^ { T } \mathbf { z } ) \mathbf { u } } \\ & { \qquad = \mathbf { z } - \beta ( \mathbf { z } ^ { T } \mathbf { z } + \sigma \mathbf { e } ^ { T } \mathbf { z } ) \mathbf { u } } \\ & { \qquad = \mathbf { z } - \beta ( \sigma ^ { 2 } + \sigma \mathbf { e } ^ { T } \mathbf { z } ) \mathbf { u } . } \end{array}
$$

However,

$$
\begin{array} { l } { \displaystyle \beta = \frac { 2 } { \mathbf { u } ^ { T } \mathbf { u } } = 2 / ( \mathbf { z } ^ { T } \mathbf { z } + 2 \sigma \mathbf { e } ^ { T } \mathbf { z } + \sigma ^ { 2 } ) } \\ { \displaystyle = 1 / ( \sigma ^ { 2 } + \sigma \mathbf { e } ^ { T } \mathbf { z } ) } \end{array}
$$

or

$$
\beta = \frac { 1 } { \sigma u _ { 1 } }
$$

where $u _ { 1 }$ is the first element of $\mathbf { u }$ .

Substituting Eq. (5.5.16) into (5.5.15) yields

$$
{ \begin{array} { r } { T \mathbf { z } = \mathbf { z } - \mathbf { u } } \\ { = - \sigma \mathbf { e } . } \end{array} }
$$

From Eq. (5.5.14) and (5.5.17) note that

$$
\mathbf { u } ^ { T } \mathbf { u } = 2 \sigma u _ { 1 } .
$$

Also, from Eq. (5.5.9) we may write

$$
\gamma = \beta \mathbf { z } ^ { T } \mathbf { u }
$$

or

$$
\gamma = \beta \mathbf { u } ^ { T } \mathbf { z } .
$$

For each application of $T$ to a given matrix, we zero out all elements below the main diagonal of the first column. In this operation all elements will be multiplied by $\beta$ . Hence, we want to choose the sign of $\sigma$ to maximize $\lVert u _ { 1 } \rVert$ . Because $u _ { 1 } =$ $z _ { 1 } + \sigma$ , we choose the sign of $\sigma$ to be the same as that of $z _ { 1 }$ , the first element of $\mathbf { z }$ .

In summary, the Householder equations to achieve the desired transformation are

$$
\begin{array} { r l } & { \sigma = \mathrm { s i g n } \ ( z _ { 1 } ) ( \mathbf { z } ^ { T } \mathbf { z } ) ^ { 1 / 2 } } \\ & { z _ { i } ^ { \prime } = - \sigma } \\ & { u _ { 1 } = z _ { 1 } + \sigma } \\ & { u _ { i } = z _ { i } , z _ { i } ^ { \prime } = 0 , i = 2 , . . . \mathrm { n u m b e r ~ o f ~ r o w s } } \\ & { \beta = 1 / ( \sigma u _ { 1 } ) . } \end{array}
$$

The remaining columns also must have $T$ applied. From Eq. (5.5.20)

$$
\gamma _ { j } = \beta \mathbf { u } ^ { T } \mathbf { z } _ { j } , \quad j = 2 , \ldots { \mathrm { n u m b e r ~ o f ~ c o l u m n s } }
$$

where $\gamma _ { j }$ is a scalar and $\mathbf { z } _ { j }$ is the $j ^ { \mathrm { t h } }$ column of the matrix being transformed. The transformed columns, $\mathbf { z } _ { j } ^ { \prime }$ , are computed using Eq. (5.5.9):

$$
\mathbf { z } _ { j } ^ { \prime } = \mathbf { z } _ { j } - \gamma _ { j } \mathbf { u } .
$$

A more detailed algorithm is given in Section 5.5.2.

# 5.5.1 APPLICATION TO THE SOLUTION OF THE LEAST SQUARES PROBLEM

Our goal is to upper triangularize an $( n + m ) \times ( n + 1 )$ matrix using the Householder transformation:

$$
\begin{array} { r l r } { \stackrel { n } {  } 1 } & { { } \stackrel { n } {  } 1 } & { \stackrel { n } {  } 1 } \\ { T _ { n } T _ { n - 1 } \ldots T _ { 1 } } & { { } [ \begin{array} { l l } { \overline { { R } } } & { \overline { { \mathbf { b } } } } \\ { H } & { \mathbf { y } } \end{array} ] \Bigr \} n } & { { } = } & { [ \begin{array} { l l } { R } & { \mathbf { b } } \\ { 0 } & { \mathbf { e } } \end{array} ] \Bigr \} n . } \end{array}
$$

The procedure for accomplishing this is as follows. Let

$$
A \equiv \left[ \begin{array} { l l } { \overline { { R } } } & { \overline { { \mathbf { b } } } } \\ { H } & { \mathbf { y } } \end{array} \right] .
$$

The first transformation $T _ { 1 } A$ will zero all elements of the fir st column except for the first element, which will have the opposite sign of $\overline { { R } } _ { 1 1 }$ and magnitude equal to the Euclidian norm of the first column,

$$
T _ { 1 } A = \hbar - 1 \{ \begin{array} { l l } { \displaystyle \overbrace { - \sigma _ { 1 } | \tilde { a } _ { 1 1 } \tilde { a } _ { 1 2 } \cdots \tilde { a } _ { 1 n } } ^ { 1 } } \\ { \quad 0 } \\ { \quad \vdots } \\ { \quad 0 } \end{array}  \} \{ \begin{array} { l } { \displaystyle { n } } \\ { \displaystyle { \vphantom { \bigg | } } } \\ { \displaystyle { \vphantom { \bigg | } } } \\ { \displaystyle { \vphantom { \bigg | } } } \end{array}  ( 5 . 5 . )  \\  m + n - 1 \{ \begin{array} { l } { \displaystyle \overbrace { [ \begin{array} { l } { \begin{array} { r } { \begin{array} { r } { \begin{array} { r } { \begin{array} { r } { \begin{array} { r } { \end{array} } } \end{array} } \end{array} ] } { \tilde { a } _ { 1 1 } } \cdots \tilde { a } _ { 1 n } } } \\ { \displaystyle { 0 } } \\ { \quad \vdots } \\ { \displaystyle } } \\ { \quad { 0 } \end{array} }  } \end{array}  , \end{array} \end{array}
$$

The next transformation operates on $\widetilde { A } _ { 1 }$ and does not change the first row or column.

This procedure is continued, zeroing elements below the diagonal until the upper $n \times n$ portion of $A$ is upper triangular.

# 5.5.2 HOUSEHOLDER COMPUTATIONAL ALGORITHM

The computational algorithm for applying the Householder transformation is given by Bierman (1977). A few steps have been added here to aid in implementing the algorithm.

Given:

$$
\begin{array} { l l } { \bigcap _ { \mathbf { \lambda } } ^ { n } } & { \bigcap } \\ { \prod _ { \mathbf { \lambda } } ^ { n } } & { \mathbf { \lambda } ^ { \mathbf { \lambda } } } \\ { \prod _ { \mathbf { \lambda } } ^ { n } } & { \mathbf { \lambda } ^ { \mathbf { \lambda } } \mathbf { \tilde { b } } } \\ { H } & { \mathbf { \lambda } ^ { \mathbf { \lambda } } \mathbf { \tilde { y } } } \end{array} \biggr ] \} \ n  &  \equiv [ A ] _ { ( m + n ) \times ( n + 1 ) }
$$

Do $k = 1$ , $n$

$$
\begin{array} { r c l } { { \displaystyle \sigma ~ = ~ \mathrm { s i g n } ( A _ { k k } ) ~ { \Biggl ( } \sum _ { i = k } ^ { m + n } [ A _ { i k } ] ^ { 2 } { \Biggr ) } ^ { 1 / 2 } } } \\ { { \displaystyle u _ { k } ~ = ~ A _ { k k } + \sigma } } \\ { { A _ { k k } ~ = ~ - \sigma } } \\ { { u _ { i } ~ = ~ A _ { i k } ~ i ~ = k + 1 , \ldots , m + n } } \\ { { \beta ~ = ~ { \frac { 1 } { \sigma u _ { k } } } } } \end{array}
$$

Do $j = k + 1 , \dots , n + 1$

$$
\begin{array} { r c l } { { } } & { { } } & { { } } \\ { { \displaystyle \gamma } } & { { = } } & { { \beta \displaystyle \sum _ { i = k } ^ { m + n } u _ { i } A _ { i j } } } \\ { { } } & { { } } & { { } } \\ { { { \cal A } _ { i j } } } & { { = } } & { { { \cal A } _ { i j } - \gamma u _ { i } ~ i = k , \ldots , m + n } } \end{array}
$$

Next $j$

Next $k$

$$
A _ { i k } = 0 \quad i = k + 1 , \ldots , m + n
$$

$$
\mathrm { S u m } = \sum _ { i = 1 } ^ { m } [ A _ { n + i , n + 1 } ] ^ { 2 }
$$

Upon completion, the elements of $A$ represent $R , b$ , and $e$ , respectively:

$$
\overset { n } { \underset { A = \left[ \begin{array} { l l } { R } & { \mathbf { b } } \\ { 0 } & { \mathbf { e } } \end{array} \right] } { \mathrm { \Sigma } } } \mathfrak { j } _ { m }
$$

and

$$
\mathrm { S u m } = \sum _ { i = 1 } ^ { m } e _ { i } ^ { 2 } .
$$

The algorithm can be initialized with $a$ priori $\overline { { R } }$ and $\overline { { \mathbf { b } } }$ . If no $a$ priori is available it can be initialized with $\overline { { R } } = 0 , \overline { { \mathbf { b } } } = 0$ . Alternatively we may define $A$ as

$$
\lim \limits _ { A _ { m \times ( n + 1 ) } } \overbrace { \int \limits _ { \mathrm { ~ } H } \mathrm { ~ } \overbrace { i \mathrm { ~ } \textbf { y } } } ^ { n }
$$

and the operations with index $i$ range to $m$ instead of $m + n$ . In this case the final result is

$$
\begin{array} { r l } { A = } & { { } \left[ \begin{array} { l l } { \overbrace { R } ^ { n } } & { \overbrace { \mathbf { \Gamma } \mathbf { b } } ^ { 1 } } \\ { 0 } & { \mathbf { e } } \end{array} \right] \ m \} ^ { n } } \end{array}
$$

Recall from the discussion on Givens transformation in Section 5.4.1 that

$$
\sum _ { i = 1 } ^ { m } e _ { i } ^ { 2 } = \| \overline { { R } } ( \hat { \bf x } - \overline { { \bf x } } ) \| ^ { 2 } + \sum _ { i = 1 } ^ { m } \hat { \epsilon } _ { i } ^ { 2 }
$$

where

$$
\hat { \epsilon } _ { i } = y _ { i } - H _ { i } \hat { \mathbf { x } } .
$$

If the initialization procedure of Eq. (5.5.31) is used, Eq. (5.5.33) becomes

$$
\sum _ { i = 1 } ^ { m - n } e _ { i } ^ { 2 } = \sum _ { i = 1 } ^ { m } \hat { \epsilon } _ { i } ^ { 2 } .
$$

As with the Givens transformation, the value of $\hat { \bf x }$ is obtained by a backward substitution using Eq. (5.2.8); that is, $R \hat { \mathbf { x } } = \mathbf { b }$ and

$$
\hat { x } _ { i } = \left( b _ { i } - \sum _ { j = i + 1 } ^ { n } R _ { i j } \hat { x } _ { j } \right) \bigg / R _ { i i } \quad i = n , \ldots , 1
$$

and the estimation error covariance is obtained from

$$
\begin{array} { c } { P = \Lambda ^ { - 1 } = ( R ^ { T } R ) ^ { - 1 } } \\ { = R ^ { - 1 } R ^ { - T } } \\ { = S S ^ { T } } \end{array}
$$

where $S$ is obtained from Eq. (5.2.9):

$$
\begin{array} { l } { { \displaystyle i = 1 , \ldots , n } } \\ { { \displaystyle S _ { i i } = \frac { 1 } { R _ { i i } } } } \\ { { \displaystyle S _ { i j } = - S _ { j j } \left[ \sum _ { k = i } ^ { j - 1 } R _ { k j } S _ { i k } \right] ; \quad j = i + 1 , \ldots , n . } } \end{array}
$$

# 5.6 NUMERICAL EXAMPLES

First consider a case with no a priori information. Assume we are given the observation-state matrix, $H$ , and the observation vector, $\mathbf { y }$ , as follows:

$$
\mathbf { y } = H \mathbf { x } + \epsilon
$$

where

$$
\mathbf { y } = { \left[ \begin{array} { l } { - 1 } \\ { 1 } \\ { 2 } \end{array} \right] } , H = { \left[ \begin{array} { l } { 1 - 2 } \\ { 2 - 1 } \\ { 1 } \end{array} \right] } , \mathbf { x } = { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \end{array} \right] } .
$$

Assume that the prewhitening transformation described in Section 5.7.1 has been applied so that $\epsilon \sim ( O , I )$ ; that is, $W = I$ . Use the Cholesky decomposition algorithm and the Givens and Householder transformations to solve for $\hat { \bf x }$ .

# 5.6.1 CHOLESKY DECOMPOSITION

The basic equations are

$$
H ^ { T } H \mathbf { x } = H ^ { T } \mathbf { y } , \qquad M \mathbf { x } = \mathbf { N }
$$

$$
M = H ^ { T } H = { \left[ \begin{array} { l l l } { 1 } & { 2 } & { 1 } \\ { - 2 } & { - 1 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { 1 - 2 } \\ { 2 - 1 } \\ { 1 } & { 1 } \end{array} \right] } = { \left[ \begin{array} { l l } { 6 - 3 } \\ { - 3 } & { 6 } \end{array} \right] }
$$

$$
\mathbf { N } = H ^ { T } \mathbf { y } = \left[ { \ k _ { 1 } \ \mathrm { ~ 2 ~ } \mathbf { \Omega } } 1 \right] \left[ { \ k _ { 1 } \atop \mathrm { ~ 2 } } \right] = \left[ { \ k _ { 3 } \atop \mathrm { ~ 3 } } \right] .
$$

Find $R$ such that

$$
R ^ { T } R = M , \mathrm { w h e r e } \ R \mathrm { i s \ u p p e r \ t r i a n g u l a r \ ( U T }
$$

Using the Cholesky algorithm given by Eq. (5.2.6),

$$
i = 1 , \ldots , n , j = i + 1 , \ldots , n
$$

$$
\begin{array} { l } { { r _ { i i } = \left( M _ { i i } - \displaystyle \sum _ { k = 1 } ^ { i - 1 } r _ { k i } ^ { 2 } \right) ^ { 1 / 2 } } } \\ { { r _ { i j } = \left( M _ { i j } - \displaystyle \sum _ { k = 1 } ^ { i - 1 } r _ { k i } r _ { k j } \right) / r _ { i i } , } } \end{array}
$$

the following results are obtained:

$$
i = 1 , 2 , \mathrm { a n d } j = 2 \ ( \mathrm { f o r  t h i s e x a m p l e } )
$$

$$
r _ { 1 1 } = \sqrt { 6 } , r _ { 1 2 } = - 3 / \sqrt { 6 } , r _ { 2 2 } = 3 / \sqrt { 2 }
$$

$$
R = \left[ \begin{array} { c c c c } { { \sqrt { 6 } - 3 / \sqrt { 6 } } } \\ { { 0 } } & { { 3 / \sqrt { 2 } } } \end{array} \right]
$$

$$
{ \cal R } ^ { T } { \bf z } = { \cal H } ^ { T } { \bf y }
$$

$$
\begin{array} { r } { \left[ { \begin{array} { c c } { \sqrt { 6 } \quad } & { 0 } \\ { - 3 / \sqrt { 6 } \quad } & { 3 / \sqrt { 2 } } \end{array} } \right] \left[ \begin{array} { l } { z _ { 1 } } \\ { z _ { 2 } } \end{array} \right] = \left[ \begin{array} { c } { 3 } \\ { 3 } \end{array} \right] } \end{array}
$$

$$
\mathbf { z } = { \left[ \begin{array} { l } { 3 / { \sqrt { 6 } } } \\ { 3 / { \sqrt { 2 } } } \end{array} \right] }
$$

$$
R \hat { \mathbf x } = \mathbf z
$$

$$
{ \begin{array} { r } { \left[ { \sqrt { 6 } } - 3 / { \sqrt { 6 } } \right] } \\ { 0 \quad 3 / { \sqrt { 2 } } } \end{array} } { \left[ } { \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \end{array} } { \right] } = { \frac { \left[ 3 / { \sqrt { 6 } } \right] } { 3 / { \sqrt { 2 } } } }
$$

$$
{ \hat { \mathbf { x } } } = { \left[ \begin{array} { l } { 1 } \\ { 1 } \end{array} \right] } .
$$

If this were a more complex problem, we would use Eqs. (5.2.7) and (5.2.8) to compute $\mathbf { z }$ and $\hat { \bf x }$ , respectively.

# 5.6.2 GIVENS TRANSFORMATION

For this example,

$$
G [ H : \mathbf { y } ] = { [ \begin{array} { l } { \operatorname { w h e r e } R \equiv 2 \times 2 \ { \mathrm { U T } } , } \\ { \operatorname { \rho } \operatorname { \rho } \phi \equiv 1 \times 2 \ \operatorname { n u l l } \ \operatorname* { m a t r i x } } \\ { \phi \vdots \it { e } ] } { \mathrm { , ~ i t ~ f o l l o w s ~ t h e n ~ t h a t } } \ b \equiv 2 \ \times 1 } \\ { \operatorname { a n d } e \equiv 1 \ \times 1 . } \end{array}  
$$

$G$ is computed directly here using Eq. (5.4.8).

Operating on rows 1 and 2 $( i = 1 , k = 2$ ) yields

$$
\left[ { \begin{array} { c c c } { \cos \theta } & { \sin \theta } & { 0 } \\ { - \sin \theta } & { \cos \theta } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} } \right] \left[ { \begin{array} { c c c } { 1 - 2 \div - 1 } \\ { 2 - 1 \vdots } & { 1 } \\ { 1 } & { 1 \vdots } & { 2 } \end{array} } \right]
$$

$$
h _ { i i } ^ { \prime } = \sqrt { h _ { i i } ^ { 2 } + h _ { k i } ^ { 2 } } , ~ h _ { 1 1 } ^ { \prime } = \sqrt { 1 + 4 } = \sqrt { 5 }
$$

$$
\begin{array} { c } { { \sin \theta = S = h _ { k i } / h _ { i i } ^ { \prime } = 2 / \sqrt { 5 } } } \\ { { \cos \theta = C = h _ { i i } / h _ { i i } ^ { \prime } = 1 / \sqrt { 5 } } } \end{array}
$$

$$
\begin{array} { r l r } & { } & { \left[ \begin{array} { r r r r } { 1 / \sqrt { 5 } } & { 2 / \sqrt { 5 } } & { 0 } \\ { - 2 / \sqrt { 5 } } & { 1 / \sqrt { 5 } } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { r r r r } { 1 } & { - 2 } & { - 1 } \\ { 2 } & { - 1 } & { 1 } \\ { 1 } & { 1 } & { 2 } \end{array} \right] = } \\ & { } & { \left[ \begin{array} { r r r r } { \sqrt { 5 } } & { - 4 / \sqrt { 5 } } & { 1 / \sqrt { 5 } } \\ { 0 } & { 3 / \sqrt { 5 } } & { 3 / \sqrt { 5 } } \\ { 1 } & { 1 } & { 2 } \end{array} \right] . } \end{array}
$$

Operating on rows 1 and 3 $( i = 1 , k = 3$ ) yields

$$
h _ { 1 1 } ^ { \prime } = \sqrt { 6 }
$$

$$
S = h _ { 3 1 } / h _ { 1 1 } ^ { \prime } = 1 / \sqrt { 6 } , C = h _ { 1 1 } / h _ { 1 1 } ^ { \prime } = \sqrt { 5 } / \sqrt { 6 }
$$

$$
{ \begin{array} { r l } & { { \left[ \begin{array} { l l l } { { \sqrt { 5 } } / { \sqrt { 6 } } } & { 0 } & { 1 / { \sqrt { 6 } } } \\ { 0 } & { 1 } & { 0 } \\ { - 1 / { \sqrt { 6 } } } & { 0 } & { { \sqrt { 5 } } / { \sqrt { 6 } } } \end{array} \right] } { \left[ \begin{array} { l l l } { { \sqrt { 5 } } } & { - 4 / { \sqrt { 5 } } } & { 1 / { \sqrt { 5 } } } \\ { 0 } & { 3 / { \sqrt { 5 } } } & { 3 / { \sqrt { 5 } } } \\ { 1 } & { 1 } & { 2 } \end{array} \right] } } \\ & { = { \left[ \begin{array} { l l l } { { \sqrt { 6 } } } & { - 3 / { \sqrt { 6 } } } & { 3 / { \sqrt { 6 } } } \\ { 0 } & { 3 / { \sqrt { 5 } } } & { 3 / { \sqrt { 5 } } } \\ { 0 } & { 9 / { \sqrt { 3 0 } } } & { 9 / { \sqrt { 3 0 } } } \end{array} \right] } . } \end{array} }
$$

The final operation is on rows 2 and 3 $( i = 2 , k = 3 )$ ), which results in

$$
\begin{array} { r c l } { { } } & { { } } & { { h _ { 2 2 } ^ { \prime } = \sqrt { 9 / 5 \ + \ 8 1 / 3 0 } = \sqrt { 1 3 5 / 3 0 } } } \\ { { } } & { { } } & { { S = h _ { 3 2 } / h _ { 2 2 } ^ { \prime } = 9 / \sqrt { 1 3 5 } } } \\ { { } } & { { } } & { { C = h _ { 2 2 } / h _ { 2 2 } ^ { \prime } = 3 \sqrt { 6 } / \sqrt { 1 3 5 } } } \end{array}
$$

$$
\left[ \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { 3 \sqrt { 6 } / \sqrt { 1 3 5 } } & { 9 / \sqrt { 1 3 5 } } \\ { 0 } & { - 9 / \sqrt { 1 3 5 } } & { 3 \sqrt { 6 } / \sqrt { 1 3 5 } } \end{array} \right] \left[ \begin{array} { c c c } { \sqrt { 6 } } & { - 3 / \sqrt { 6 } } & { 3 / \sqrt { 6 } } \\ { 0 } & { 3 / \sqrt { 5 } } & { 3 / \sqrt { 5 } } \\ { 0 } & { 9 / \sqrt { 3 0 } } & { 9 / \sqrt { 3 0 } } \end{array} \right]
$$

$$
= \left[ \begin{array} { c c c c } { { \sqrt { 6 } } } & { { - 3 / \sqrt { 6 } } } & { { \vdots } } & { { 3 / \sqrt { 6 } } } \\ { { 0 } } & { { 3 / \sqrt { 2 } } } & { { \vdots } } & { { 3 / \sqrt { 2 } } } \\ { { 0 } } & { { 0 } } & { { \vdots } } & { { 0 } } \end{array} \right] .
$$

We now have the necessary information to solve for $\hat { \bf x }$ . Using

$$
R \hat { \mathbf x } = \mathbf b
$$

yields

$$
\left[ \begin{array} { c c } { { \sqrt { 6 } } } & { { - 3 / \sqrt { 6 } } } \\ { { 0 } } & { { 3 / \sqrt { 2 } } } \end{array} \right] \left[ \begin{array} { c } { { \hat { x } _ { 1 } } } \\ { { \hat { x } _ { 2 } } } \end{array} \right] = \left[ 3 / \sqrt { 6 } \right] .
$$

Solving for $\hat { \bf x }$ by a backward recursion yields

$$
{ \hat { \mathbf { x } } } = { \left[ \begin{array} { l } { 1 } \\ { 1 } \end{array} \right] } .
$$

The associated covariance matrix is

$$
P = ( H ^ { T } H ) ^ { - 1 } = ( H ^ { T } G ^ { T } G H ) ^ { - 1 } = R ^ { - 1 } R ^ { - T }
$$

$$
\begin{array} { r } { P = \left[ \begin{array} { l l } { 2 / 9 } & { \mathrm { ~ } 1 / 9 } \\ { 1 / 9 } & { \mathrm { ~ } 2 / 9 } \end{array} \right] . } \end{array}
$$

Note that in this example the observation residual, $e$ , has a value of zero. This is because the three observations were perfect, from Eq. (5.5.34):

$$
\hat { \epsilon } = \mathbf { y } - H \hat { \mathbf { x } } = 0 .
$$

# 5.6.3 HOUSEHOLDER TRANSFORMATION

This algorithm is given by Eq. (5.5.29). Because there is no a priori information, we use the initialization procedure of Eq. (5.5.31).

For this example,

$$
[ H : { \bf y } ] = A = \left[ \begin{array} { r c c c } { { 1 } } & { { - 2 } } & { { - 1 } } \\ { { 2 } } & { { - 1 } } & { { 1 } } \\ { { 1 } } & { { 1 } } & { { 2 } } \end{array} \right] .
$$

Each transformation, $T$ , results in

$$
T A = \left[ \begin{array} { r r } { - \sigma } & { \cdots } \\ { \vdots } & { \widetilde { A } } \\ { 0 } & { } \end{array} \right] .
$$

Note that the algorithm given by Eq. (5.5.29) does not use the array, $\widetilde { A }$ . It simply redefines the elements of $A$ , thereby requiring less computer storage. Beginning with

$$
k = 1
$$

$$
\begin{array} { c c } { \sigma = + \sqrt { 1 + 2 ^ { 2 } + 1 } = \sqrt { 6 } } \\ { A _ { 1 1 } = - \sigma = - \sqrt { 6 } } \\ { u _ { 1 } = A _ { 1 1 } + \sigma = 1 + \sqrt { 6 } = 3 . 4 4 9 5 } \\ { u _ { 2 } = A _ { 2 1 } = 2 } \\ { u _ { 3 } = A _ { 3 1 } = 1 } \\ { \beta = \frac { 1 } { \sigma u _ { 1 } } = \frac { 1 } { \sqrt { 6 } + 6 } = 0 . 1 1 8 3 5 } \end{array}
$$

$$
j = 2
$$

$$
\begin{array} { l } { { \displaystyle \gamma = \beta \sum _ { i = 1 } ^ { 3 } u _ { i } A _ { i j } } } \\ { { \displaystyle ~ = 0 . 1 1 8 3 5 \left[ 3 . 4 4 9 5 \left( - 2 \right) ~ + ~ 2 \left( - 1 \right) ~ + ~ 1 \right] } } \\ { { \displaystyle = - 0 . 9 3 4 8 } } \end{array}
$$

$$
j = 3
$$

$$
\gamma = 0 . 1 1 8 3 5 \left[ 3 . 4 4 9 5 ( - 1 ) + 2 + 2 \right]
$$

$$
\begin{array} { c } { { A _ { 1 3 } = - 1 - . 0 6 5 1 5 \left( 3 . 4 4 9 5 \right) } } \\ { { = - 1 . 2 2 4 7 } } \end{array}
$$

$$
\begin{array} { c } { A _ { 2 3 } = 1 - 0 . 0 6 5 1 5 \left( 2 \right. } \\ { \left. = 0 . 8 6 9 7 \right. } \end{array}
$$

$$
\begin{array} { c } { { A _ { 3 3 } = A _ { 3 3 } + \gamma u _ { 3 } } } \\ { { { } } } \\ { { = 2 - 0 . 0 6 5 1 5 } } \\ { { { } } } \\ { { { } = 1 . 9 3 4 8 . } } \end{array}
$$

Hence,

$$
\left[ \begin{array} { l } { \sigma \cdots } \\ { \vdots } \\ { 0 } \end{array} \right] = \left[ \begin{array} { l l l } { - 2 . 4 4 9 5 \vdots 1 . 2 2 4 7 - 1 . 2 2 4 7 } \\ { \ldots \ldots } & { \vdots } \\ { \phantom { - } \ldots \ldots } & { \vdots } \\ { \phantom { - } 0 } & { \vdots } \\ { \phantom { - } 0 } & { \vdots } \end{array} \ldots \ldots \right]
$$

$$
k = 2
$$

$$
\begin{array} { r l } & { \sigma = \sqrt { ( 0 . 8 6 9 7 ) ^ { 2 } + ( 1 . 9 3 4 8 ) ^ { 2 } } } \\ & { \quad = 2 . 1 2 1 2 } \\ & { \widetilde { A } _ { 1 1 } = - 2 . 1 2 1 2 } \\ & { \quad u _ { 2 } = A _ { 2 2 } + \sigma = 0 . 8 6 9 7 + 2 . 1 2 1 2 } \\ & { \quad \quad = 2 . 9 9 1 } \\ & { u _ { 3 } = A _ { 3 2 } = 1 . 9 3 4 8 } \end{array}
$$

$$
\beta = { \frac { 1 } { \sigma u _ { 2 } } } = { \frac { 1 } { ( 2 . 1 2 1 2 ) ( 2 . 9 9 1 ) } } = 0 . 1 5 7 6
$$

$$
j = 3
$$

$$
\begin{array} { r l } { \gamma = \beta [ u _ { 2 } u _ { 3 } ] \left[ \begin{array} { l } { A _ { 2 2 } } \\ { A _ { 3 2 } } \end{array} \right] } & { { } } \\ { = 0 . 1 5 7 6 \left[ 2 . 9 9 1 1 . 9 3 4 8 \right] \left[ \begin{array} { l } { 0 . 8 6 9 7 } \\ { 1 . 9 3 4 8 } \end{array} \right] } & { { } } \end{array}
$$

$$
\gamma = 1
$$

$$
\begin{array} { c } { { \widetilde { A } _ { i j } = A _ { i j } - \gamma u _ { i } , j = 3 , i = 2 , 3 } } \\ { { \widetilde { A } = \left[ { 0 . 8 6 9 7 } \atop { 1 . 9 3 4 8 } \right]}  - \left[ { 2 . 9 9 1 } { \atop { 1 . 9 3 4 8 } } \right] = \left[ { - 2 . 1 2 1 2 } \atop { 0 } \right] }  \end{array}
$$

so that the final result is

$$
T A = \left[ \begin{array} { r r r } { - 2 . 4 4 9 5 } & { { 1 . 2 2 4 7 - 1 . 2 2 4 7 } } \\ { 0 - 2 . 1 2 1 2 - 2 . 1 2 1 2 } \\ { 0 } & { 0 } & { 0 } \end{array} \right]
$$

which agrees with the Givens result except for the sign, which has no effect on $\hat { \bf x }$ or $P$ . Note that, as in the case for the Givens transformation, the observation residual is zero, implying that the observations were perfect.

# 5.6.4 A MORE ILLUSTRATIVE EXAMPLE

For this example we will include a priori information and observation errors. This will illustrate how to initialize the least squares procedure with a priori information using the Cholesky decomposition and orthogonal transformations and

will also demonstrate the feature of computing the sum of squares of the observation residuals.

Assume that we are given observations

$$
\mathbf { y } = H \mathbf { x } + \epsilon
$$

and that we have prewhitened the observation errors so that $\epsilon \sim ( O , I )$ . Values for $\mathbf { y }$ and $H$ are

$$
\mathbf { y } = { \left[ \begin{array} { l } { - 1 . 1 } \\ { 1 . 2 } \\ { 1 . 8 } \end{array} \right] } , \quad H = { \left[ \begin{array} { l } { 1 - 2 } \\ { 2 - 1 } \\ { 1 } \end{array} \right] } ,
$$

with assumed a priori information

$$
\overline { { { \cal P } } } = \left[ \begin{array} { r r } { { 1 0 0 } } & { { 0 } } \\ { { 0 } } & { { 1 0 0 } } \end{array} \right] , \overline { { { \bf x } } } = \left[ \begin{array} { l } { { 2 } } \\ { { 2 } } \end{array} \right] .
$$

Our objective is to determine the best estimate, $\hat { \bf x }$ , of the constant vector $\mathbf { x }$ using the Cholesky decomposition, the Givens square root free, and Householder algorithms. We also wish to find the estimation error covariance matrix and the sum of squares of the observation residuals.

# 5.6.5 CHOLESKY DECOMPOSITION

If the observations are given unit weight, for example, $W = I$ , the normal equations are

$$
( H ^ { T } H + \overline { { P } } ^ { - 1 } ) { \bf x } = H ^ { T } { \bf y } + \overline { { P } } ^ { - 1 } \overline { { { \bf x } } }
$$

or

$$
M \mathbf { x } = \mathbf { N }
$$

where

$$
\begin{array} { l } { { \displaystyle M = H ^ { T } H + \overline { { { \cal P } } } ^ { - 1 } } } \\ { { \displaystyle { \bf N } = H ^ { T } { \bf y } + \overline { { { \cal P } } } ^ { - 1 } \overline { { { \bf x } } } . } } \end{array}
$$

Substituting $H , { \overline { { P } } } , \mathbf { y }$ , and $\overline { { \mathbf { x } } }$ into Eqs. (5.6.13) and (5.6.14) yields

$$
M = \left[ \begin{array} { c c } { { 6 . 0 1 } } & { { \mathrm { ~  ~ \omega ~ } - 3 } } \\ { { \mathrm { ~  ~ \omega ~ } - 3 } } & { { \mathrm { ~  ~ \omega ~ } 6 . 0 1 } } \end{array} \right] , \ : \ : \ : \ : \mathbf { N } = \left[ \begin{array} { c c } { { 3 . 1 2 } } \\ { { 2 . 8 2 } } \end{array} \right] .
$$

Using the Cholesky algorithm given by Eq. (5.2.6) to compute $R$ , where $M =$ $R ^ { T } ~ R$ , yields

$$
\begin{array} { r } { R = \left[ \begin{array} { c c } { 2 . 4 5 2 } & { - 1 . 2 2 4 } \\ { 0 } & { 2 . 1 2 4 } \end{array} \right] . } \end{array}
$$

From Eq. (5.2.4)

$$
R ^ { T } { \bf z } = { \bf N } ,
$$

from Eq. (5.2.7)

$$
\mathbf { z } = { \left[ \begin{array} { l } { 1 . 2 7 3 } \\ { 2 . 0 6 0 9 } \end{array} \right] } ,
$$

and from Eq. (5.2.8)

$$
\hat { \mathbf { x } } = \left[ \begin{array} { c } { 1 . 0 0 3 } \\ { . 9 7 0 } \end{array} \right] .
$$

The covariance of the estimation error is given by Eq. (5.2.5),

$$
P = E ( \hat { \mathbf { x } } - \mathbf { x } ) ( \hat { \mathbf { x } } - \mathbf { x } ) ^ { T } = R ^ { - 1 } R ^ { - T } = S S ^ { T } .
$$

$S$ is given by Eq. (5.2.9)

$$
\begin{array} { r } { S = \left[ \begin{array} { r r } { . 4 0 8 } & { { } . 2 3 5 } \\ { 0 } & { . 4 7 1 } \end{array} \right] . } \end{array}
$$

Hence,

$$
P = \left[ \begin{array} { l l } { { . 2 2 2 } } & { { . 1 1 1 } } \\ { { . 1 1 1 } } & { { . 2 2 2 } } \end{array} \right] .
$$

The sum of squares of the observation errors, including errors in the $a$ priori information, is given by

$$
\begin{array} { l } { { \displaystyle e ^ { 2 } = ( \hat { \mathbf { x } } - \overline { { \mathbf { x } } } ) ^ { T } \overline { { P } } ^ { - 1 } ( \hat { \mathbf { x } } - \overline { { \mathbf { x } } } ) + \sum _ { i = 1 } ^ { 3 } ( y _ { i } - H _ { i } \hat { \mathbf { x } } ) ^ { 2 } } } \\ { { \displaystyle ~ = . 0 2 0 5 + . 0 2 6 6 + . 0 2 6 9 + . 0 2 9 9 } } \\ { { \displaystyle e ^ { 2 } = . 1 0 3 9 . } } \end{array}
$$

# 5.6.6 SQUARE ROOT FREE GIVENS TRANSFORMATION

The initialization procedure for the orthogonal transformation algorithms is described in Section 5.4.1. This involves computing the square root of the a priori

information matrix, $\overline { { R } }$ , and $\overline { { { \bf b } } } = \overline { { R } } \overline { { \bf x } }$ . Recall that $\overline { { \boldsymbol { P } } } = \overline { { \boldsymbol { S } } } \overline { { \boldsymbol { S } } } ^ { T }$ and $\overline { { R } } = \overline { { S } } ^ { - 1 }$ . For this example

$$
\overline { { { R } } } = \left[ \begin{array} { c c } { { 0 . 1 } } & { { 0 } } \\ { { 0 } } & { { 0 . 1 } } \end{array} \right] , \quad \overline { { { \bf b } } } = \left[ \begin{array} { c } { { 0 . 2 } } \\ { { 0 . 2 } } \end{array} \right] .
$$

We will use the square root free Givens rotation given by Eq. (5.4.70). For this we need $\overline { { D } }$ and $\overline { U }$ , where $\overline { { { R } } } = \overline { { { D } } } ^ { \frac { 1 } { 2 } } \overline { { { U } } }$ . Hence,

$$
\begin{array} { r } { \overline { { D } } = \left[ \begin{array} { c c } { . 0 1 } & { 0 } \\ { 0 } & { . 0 1 } \end{array} \right] , \quad \overline { { U } } = \left[ \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] . } \end{array}
$$

The $a$ priori value of $\widetilde { \mathbf { b } }$ is given by

$$
\begin{array} { c } { { \overline { { \widetilde { \mathbf { b } } } } = \overline { { D } } ^ { - \frac { 1 } { 2 } } \overline { { \mathbf { b } } } = \overline { { D } } ^ { - \frac { 1 } { 2 } } \overline { { R } } \overline { { \mathbf { x } } } } } \\ { { = \overline { { U } } \ \overline { { \mathbf { x } } } , } } \end{array}
$$

so

$$
\overline { { \widetilde { { \bf b } } } } = \left[ \begin{array} { l } { 2 } \\ { 2 } \end{array} \right] .
$$

The matrix we wish to compress is

$$
\left[ \begin{array} { l l } { \overline { { U } } } & { \overline { { \tilde { \mathbf { b } } } } } \\ { H } & { \mathbf { y } } \end{array} \right] = \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} 2 \right] .
$$

Recall that Givens algorithm as defined by Eq. (5.4.70) operates on the matrix one row at a time. After processing the first observation we have

$$
D = \left[ \begin{array} { c c } { { \ 1 . 0 1 0 0 } } & { { \ 0 } } \\ { { \ 0 } } & { { \ 0 . 0 4 9 6 } } \end{array} \right] , \quad U = \left[ \begin{array} { c c } { { \ 1 . 0 0 } } & { { \ - 1 . 9 8 0 2 } } \\ { { \ 0 } } & { { \ 1 . 0 0 } } \end{array} \right]
$$

$$
\widetilde { \mathbf { b } } = \left[ \begin{array} { c } { - 1 . 0 6 9 3 } \\ { 1 . 6 4 0 7 } \end{array} \right] , \quad e = 0 . 0 4 0 2 .
$$

Processing the second observation results in

$$
D = \left[ \begin{array} { c c } { { 5 . 0 1 0 0 } } & { { 0 } } \\ { { 0 } } & { { 1 . 8 1 6 4 } } \end{array} \right] , \quad U = \left[ \begin{array} { c c } { { 1 . 0 ~ } } & { { - 0 . 7 9 8 4 } } \\ { { 0 } } & { { 1 . 0 } } \end{array} \right]
$$

$$
\widetilde { \mathbf { b } } = \left[ \begin{array} { l } { 0 . 2 6 3 5 } \\ { 1 . 1 4 1 8 } \end{array} \right] , \quad e = - 0 . 1 1 2 7 .
$$

After processing the third observation,

$$
\begin{array} { r l } { D = \left[ { 6 . 0 1 0 \quad 0 } \atop { 0 \quad 4 . 5 1 2 5 } \right] , U = \left[ { 1 . 0 - 0 . 4 9 9 2 } \atop { 0 \quad 1 . 0 \atop { 1 \cdots 0 } } \right] } & { { } } \\ { \tilde { \mathbf { b } } = \left[ { 0 . 5 1 9 1 } \atop { 0 . 9 7 0 1 } \right] , } & { { } e = - 0 . 2 9 9 4 . } \end{array}
$$

To compare with the Householder results we must multiply by $D ^ { 1 / 2 }$ :

$$
\left[ { \begin{array} { l } { R \mathbf { b } } \\ { 0 \ \mathbf { e } } \end{array} } \right] = \left[ { \begin{array} { c c } { D ^ { \frac { 1 } { 2 } } U } & { D ^ { \frac { 1 } { 2 } } \widetilde { \mathbf { b } } } \\ { 0 } & { \mathbf { e } } \end{array} } \right] \ \} 3
$$

$$
\mathbf { \Sigma } = \left[ \begin{array} { r r r r r } { { 2 . 4 5 1 5 } } & { { - 1 . 2 2 3 7 } } & { { 1 . 2 7 2 7 } } \\ { { 0 } } & { { 2 . 1 2 4 3 } } & { { 2 . 0 6 0 7 } } \\ { { 0 } } & { { 0 } } & { { 0 . 0 4 0 2 } } \\ { { 0 } } & { { 0 } } & { { - 0 . 1 1 2 7 } } \\ { { 0 } } & { { 0 } } & { { - 0 . 2 9 9 4 } } \end{array} \right] .
$$

In actual practice, to conserve computer storage, we would read and process the observations one at a time and store the observations residuals as

$$
e ^ { 2 } = \sum _ { i = 1 } ^ { m } e _ { i } ^ { 2 } .
$$

$\hat { \bf x }$ is computed using Eq. (5.4.49),

$$
U \hat { \mathbf { x } } = \widetilde { \mathbf { b } }
$$

or

$$
\begin{array} { r } { \Big [ 1 . 0 0 - 0 . 4 9 9 2 \Big ] \Big [ \hat { x } _ { 1 } \Big ] = \Big [ 0 . 5 1 9 1 \Big ] } \\ { 0 \qquad 1 . 0 0 \Big ] \Big [ \hat { x } _ { 2 } \Big ] = \Big [ 0 . 9 7 0 1 \Big ] } \end{array}
$$

and

$$
\begin{array} { r } { \Big [ \hat { x } _ { 1 } \Big ] = \Big [ 1 . 0 0 3 4 \Big ] . } \\ { \Big [ \hat { x } _ { 2 } \Big ] } \end{array}
$$

The sum of squares of observation residuals is given by

$$
e ^ { 2 } = \sum _ { i = 1 } ^ { 3 } e _ { i } ^ { 2 } = ( 0 . 0 4 0 2 ) ^ { 2 } + ( - 0 . 1 1 2 7 ) ^ { 2 } + ( - 0 . 2 9 9 4 ) ^ { 2 }
$$

The covariance of the estimation error is given by Eq. (5.4.80), $P = U ^ { - 1 } D ^ { - 1 } U ^ { - T ^ { \prime } }$ Equation (5.2.20) may be used to compute $U ^ { - 1 }$ ,

$$
U ^ { - 1 } = \left[ { \begin{array} { l } { 1 . 0 0 . 4 9 9 2 } \\ { 0 \quad 1 . 0 } \end{array} } \right]
$$

and

$$
{ \begin{array} { r l } & { P = { \left[ \begin{array} { l l } { 1 . 0 } & { 0 . 4 9 9 2 } \\ { 0 } & { 1 . 0 } \end{array} \right] } { \left[ \begin{array} { l l } { . 1 6 6 4 } & { 0 } \\ { 0 } & { . 2 2 1 6 } \end{array} \right] } { \left[ \begin{array} { l l } { 1 . 0 } & { 0 } \\ { 0 . 4 9 9 2 } & { 1 . 0 } \end{array} \right] } } \\ & { \quad = { \left[ \begin{array} { l l } { . 2 2 1 6 } & { . 1 1 0 6 } \\ { . 1 1 0 6 } & { . 2 2 1 6 } \end{array} \right] } . } \end{array} }
$$

Notice that the results for $\hat { \mathbf { x } } , P$ , and $e ^ { 2 }$ agree with the Cholesky results.

# 5.6.7 THE HOUSEHOLDER TRANSFORMATION

The matrix we wish to transform is given by Eq. (5.6.25). In terms of $\overline { { R } }$ and $\overline { { \mathbf { b } } }$ the matrix is given by

$$
\left[ \begin{array} { l l } { { \overline { { R } } } } & { { \overline { { \mathbf { b } } } } } \\ { { \overline { { H } } } } & { { \mathbf { y } } } \end{array} \right] = \left[ \begin{array} { l l l } { 0 . 1 } & { 0 } & { 0 . 2 } \\ { 0 } & { 0 . 1 } & { 0 . 2 } \\ { 1 } & { - 2 } & { - 1 . 1 } \\ { 2 } & { - 1 } & { 1 . 2 } \\ { 1 } & { 1 } & { 1 . 8 } \end{array} \right] .
$$

The Householder transformation algorithm given by Eq. (5.5.29) nulls the elements of each column below the main diagonal. The first transformation yields

The second transformation results in

Several points should be noted:

1. The Householder values of $R$ and $b$ are identical to the Givens results. Hence, the solution for $\hat { \bf x }$ and $P$ will be identical.   
2. Although the individual values of $e _ { i }$ differ, both algorithms yield identical values of $e ^ { 2 } = 0 . 1 0 3 9$ . This also agrees with the Cholesky result.   
3. The Euclidean norm of each column is preserved by an orthogonal transformation.   
4. The square root free Givens algorithm as derived here operates on the matrix row by row, whereas the Householder algorithm transforms column by column. The Givens algorithm can be modifie d to operate column by column (see Section 5.4.2).   
5. The orthogonal transformations do not require the formation of $H ^ { T } H$ . Hence, they will generally be more accurate than Cholesky decomposition.

# 5.7 SQUARE ROOT FILTER ALGORITHMS

Although the sequential estimation algorithms have had wide use in autonomous navigation and control applications, there has been a reluctance to adopt the sequential estimation algorithm for real-time orbit determination mission support.

The primary reason for this reluctance is due to the phenomenon of filter divergence, during which the estimate of the state can depart in an unbounded manner from the true value of the state. There are two fundamental reasons for filt er divergence. The first of these is due to inaccuracies in the mathematical model used to describe the dynamic process or in the model used to relate the observations to the state.

A second factor that can cause filter divergence is associated with the errors that occur in the measurement update of the state error covariance matrix. In particular, this matrix can become nonpositive definite, a situation that is a theoretical impossibility due to the effects of using fini te word length arithmetic to compute the update of the state error covariance matrix at the point where an observation is incorporated. Since this type of divergence is related to errors introduced during the computational procedure, it should be possible to reformulate the computational process to minimize the effects of such errors.

To accomplish this objective, several filter modificat ions, referred to as square root covariance filters, have been proposed in which the state error covariance matrix is replaced by its square root. The state error covariance matrix is obtained by multiplying the square root matrix by its transpose and will always be symmetric and positive semidefinite. Note that the algorithms presented in the remainder of this chapter are designed to accommodate scalar observations.

The motivation for considering the square root measurement update algorithms stems from the loss of significant digits that occurs in computing the measurement update of the state error covariance matrix at the observation epoch (Kaminski et al., 1971) . When the eigenvalues have a wide spread, the error introduced in the computational process can destroy the symmetry and positive definite character of the covariance matrix and filte r divergence may occur. The square root measurement update philosophy, which has been proposed to alleviate this condition, can be expressed as follows.

Define $W$ , the state error covariance matrix square root such that

$$
P = W W ^ { T } .
$$

Note that $P$ , if computed using Eq. (5.7.1), can never be nonpositive definite even in the presence of round-off or truncation errors. Furthermore, since $P$ is symmetric and positive definite, there will exist an orthogonal matrix $M$ such that

$$
P ^ { * } = { M ^ { T } } P M ,
$$

where $P ^ { * }$ is a diagonal matrix whose elements are the eigenvalues of $P$ and $M$ is the corresponding matrix of eigenvectors (Graybill, 1961). Define $W ^ { * }$ as the matrix whose diagonal elements are equal to the square root of the diagonal elements of $P ^ { * }$ :

$$
W _ { i i } ^ { * } = \sqrt { P _ { i i } ^ { * } } i = 1 , . . . , n
$$

where $P _ { i i } ^ { * } > 0$ . Then note that

$$
\begin{array} { r } { W ^ { * } W ^ { * T } = P ^ { * } = M ^ { T } P M = M ^ { T } W W ^ { T } M . } \end{array}
$$

Hence, $W ^ { * } = M ^ { T } W$ and, since $M$ is an orthogonal matrix, it follows that

$$
\begin{array} { r } { W = M W ^ { * } . } \end{array}
$$

If the matrix is symmetrical and positive definit e, there are other methods of computing the square root matrix. For example, see the Cholesky decomposition discussed in Section 5.2.

The numerical conditioning of $W$ is generally much better than that of $P$ . The conditioning number $C ( P )$ of $P$ can be defined as (Lawson and Hanson, 1974)

$$
C ( P ) = \gamma _ { \mathrm { m a x } } / \gamma _ { \mathrm { m i n } } ,
$$

where $\gamma _ { m a x }$ is the maximum eigenvalue of $P$ and $\gamma _ { m i n }$ is the minimum eigenvalue. In base 10 arithmetic with $p$ significant digits, numerical difficul ties with matrix inversion and the precision of $\hat { \bf x }$ may be encountered as $C ( P ) \to 1 0 ^ { p }$ . However, for $W$ ,

$$
C ( W ) = { \sqrt { C ( P ) } } .
$$

Hence, numerical difficulties should not be encountered until

$$
C ( W ) = 1 0 ^ { p }
$$

or

$$
C ( P ) = 1 0 ^ { 2 p } .
$$

# 5.7.1 THE SQUARE ROOT MEASUREMENT UPDATE ALGORITHMS

Using these ideas, the covariance measurement update equation, Eq. (4.7.10), can be expressed in square root form as follows:

$$
P = \overline { { P } } - \overline { { P } } H ^ { T } \left[ H \overline { { P } } H ^ { T } + R \right] ^ { - 1 } H \overline { { P } } .
$$

Now, let $P = W W ^ { T }$ and make this substitution in Eq. (5.7.6) to obtain

$$
W W ^ { T } = \overline { { { W } } } \overline { { { W } } } ^ { T } - \overline { { { W } } } \overline { { { W } } } ^ { T } H ^ { T } \left[ H \overline { { { W } } } \overline { { { W } } } ^ { T } H ^ { T } + R \right] ^ { - 1 } H \overline { { { W } } } \overline { { { W } } } ^ { T } .
$$

Using the following definitions

$$
\widetilde { F } = \overline { { { W } } } ^ { T } H ^ { T } , \alpha = ( \widetilde { F } ^ { T } \widetilde { F } + R ) ^ { - 1 } ,
$$

Eq. (5.7.7) can be expressed as

$$
\boldsymbol { W } \boldsymbol { W } ^ { T } = \overline { { \boldsymbol { W } } } [ \boldsymbol { I } - \widetilde { F } \alpha \widetilde { F } ^ { T } ] \overline { { \boldsymbol { W } } } ^ { T } .
$$

If a matrix $\widetilde { A }$ can be found such that

$$
\tilde { A } \tilde { A } ^ { T } = I - \tilde { F } \alpha \tilde { F } ^ { T } ,
$$

then Eq. (5.7.9) can be expressed as

$$
\boldsymbol { W } \boldsymbol { W } ^ { T } = \overline { { W } } \widetilde { \boldsymbol { A } } \widetilde { \boldsymbol { A } } ^ { T } \overline { { \boldsymbol { W } } } ^ { T } .
$$

Hence,

$$
W = { \overline { { W } } } \widetilde { A } .
$$

The square root measurement update algorithm can be expressed as follows:

$$
\begin{array} { l } { { \widetilde F = \overline { { W } } ^ { T } H ^ { T } } } \\ { { \alpha = ( R + \widetilde F ^ { T } \widetilde F ) ^ { - 1 } } } \\ { { K = \overline { { W } } \widetilde F \alpha } } \\ { { W = \overline { { W } } \widetilde A } } \\ { { \hat { \mathbf { x } } = \overline { { \mathbf { x } } } + K ( \mathbf { y } - H \overline { { \mathbf { x } } } ) } } \end{array}
$$

where $\widetilde { A } = [ I ~ - { \widetilde { F } } \alpha { \widetilde { F } } ^ { T } ] ^ { 1 / 2 }$ . The primary differences in the various algorithms for computing the measurement update in square root form lie in the manner in which the matrix $\widetilde { A }$ is computed. The method first used in practice is that given by Potter (Battin, 1999).

# The Potter Square Root Update

If attention is restricted to processing a single scalar observation, $\alpha$ will be a scalar. For this application, Potter considered the problem of finding the matrix $\widetilde { A }$ such that

$$
\widetilde { A } \widetilde { A } ^ { T } = [ I - \alpha \widetilde { F } \widetilde { F } ^ { T } ] = [ I - \gamma \alpha \widetilde { F } \widetilde { F } ^ { T } ] [ I - \gamma \alpha \widetilde { F } \widetilde { F } ^ { T } ] ^ { T } ,
$$

where $\gamma$ is an unspecified scalar parameter whose value is to be selected to satisfy Eq. (5.7.13). Expanding the right-hand side of Eq. (5.7.13) yields

$$
I - \alpha \widetilde { F } \widetilde { F } ^ { T } = I - 2 \alpha \gamma \widetilde { F } \widetilde { F } ^ { T } + \alpha ^ { 2 } \gamma ^ { 2 } ( \widetilde { F } \widetilde { F } ^ { T } ) ( \widetilde { F } \widetilde { F } ^ { T } ) .
$$

Canceling the identity and factoring $\widetilde { F } \widetilde { F } ^ { T }$ after noting that $\widetilde { F } ^ { T } \widetilde { F }$ is a scalar leads to

$$
( 1 - 2 \gamma + \alpha \gamma ^ { 2 } \widetilde { F } ^ { T } \widetilde { F } ) \alpha \widetilde { F } \widetilde { F } ^ { T } = 0 .
$$

The solution, $\widetilde { F } \widetilde { F } ^ { T } = 0$ , is trivial. Hence, the solution of Eq. (5.7.14) leads to the following condition:

$$
1 - 2 \gamma + \gamma ^ { 2 } \alpha \widetilde { F } ^ { T } \widetilde { F } = 0 .
$$

From Eq. (5.7.15), it follows that $\gamma$ must satisfy the following relation

$$
\gamma = \frac { 2 \pm \sqrt { 4 - 4 \alpha \widetilde { F } ^ { T } \widetilde { F } } } { 2 \alpha \widetilde { F } ^ { T } \widetilde { F } } .
$$

After some algebra, this can be simplified to

$$
\gamma = \frac { 1 } { 1 \pm \sqrt { R \alpha } } ,
$$

where the $^ +$ sign is chosen to ensure that a singular value, $\gamma = \infty$ , does not occur.

Using Eq. (5.7.16) the computational algorithm, based on the sequential estimation algorithm discussed in Chapter 4, can be expressed as follows:

Given $\overline { W }$ , H , R, x and y

Compute:

$$
\begin{array} { r l } & { \widetilde { F } = \overline { { W } } ^ { T } H ^ { T } } \\ & { \alpha = ( \widetilde { F } ^ { T } \widetilde { F } + R ) ^ { - 1 } } \\ & { \gamma = 1 / ( 1 + \sqrt { R \alpha } ) } \\ & { K = \alpha \overline { { W } } \widetilde { F } } \\ & { \widehat { \mathbf { x } } = \overline { { \mathbf { x } } } + K ( \mathbf { y } - H \overline { { \mathbf { x } } } ) } \\ & { W = \overline { { W } } - \gamma K \widetilde { F } ^ { T } . } \end{array}
$$

Note that even if $\overline { W }$ is triangular, the computation involved in Eq. (5.7.17) will result in a nontriangular form for $W$ . Also the computation of Eq. (5.7.17) involves two divisions and a square root that are not involved in the conventional Kalman algorithm. Consequently, Eq. (5.7.17) will be slower than the conventional algorithm; however, it will be more accurate. If $\overline { { P } }$ is given instead of $\overline { W }$ , a Cholesky decomposition may be used to compute $\overline { W }$ in order to initialize the algorithm.

The time update for the state error covariance square root at time $t _ { k }$ for the Potter algorithm follows directly from the time update of the state error covariance. In the general case where there is process noise