Here $t _ { 0 }$ is an arbitrary epoch and all quantities in Eq. (4.6.1) are assumed to have been mapped to this epoch using the appropriate state transition matrices as illustrated in Eqs. (4.3.15) and (4.3.16). Because we are dealing with a linearized system, Eq. (4.6.1) generally is iterated to convergence; that is, until $\hat { \mathbf { x } } _ { 0 }$ no longer changes. Note that the two matrices in Eq. (4.6.1) that must be accumulated are $H ^ { T } R ^ { - 1 } H$ and $H ^ { T } R ^ { - 1 } \mathbf { y }$ . If $R$ is a block diagonal matrix—the observations are uncorrelated in time although correlations between the observations at any given time may exist—these matrices simply may be accumulated as follows:

$$
H ^ { T } R ^ { - 1 } H = \sum _ { i = 1 } ^ { \ell } \left[ \widetilde { H } _ { i } \Phi ( t _ { i } , t _ { 0 } ) \right] ^ { T } R _ { i } ^ { - 1 } \widetilde { H } _ { i } \Phi ( t _ { i } , t _ { 0 } )
$$

$$
\boldsymbol { H } ^ { T } \boldsymbol { R } ^ { - 1 } \mathbf { y } = \sum _ { i = 1 } ^ { \ell } [ \widetilde { H } _ { i } \Phi ( t _ { i } , t _ { 0 } ) ] ^ { T } R _ { i } ^ { - 1 } \mathbf { y } _ { i } .
$$

In general $\mathbf { X } ^ { * } ( t _ { 0 } )$ would be chosen so that $\bar { \bf x } _ { 0 } = 0$ , and $\overline { { P } } _ { 0 }$ would reflect the relative accuracy of the elements of the initial condition vector $\mathbf { X } ^ { * } ( t _ { 0 } )$ . In theory $\bar { \bf x } _ { 0 }$ and $\bar { P } _ { 0 }$ represent information and should be treated as data that are merged with the observation data, as indicated by Eq. (4.6.1). Consequently, the value of $\mathbf { X } _ { 0 } ^ { * } + \bar { \mathbf { x } } _ { 0 }$ should be held constant for the beginning of each iteration. Since the initial condition vector $\mathbf { X } _ { 0 } ^ { * }$ is augmented by the value of $\hat { \mathbf { x } } _ { 0 }$ after each iteration, that is, $( \mathbf { X } _ { 0 } ^ { * } ) _ { n } \ = \ ( \mathbf { X } _ { 0 } ^ { * } ) _ { n - 1 } + ( \hat { \mathbf { x } } _ { 0 } ) _ { n }$ , holding $\mathbf { X } _ { 0 } ^ { * } + \bar { \mathbf { x } } _ { 0 }$ constant results in the following expression for $\left( \bar { \mathbf { x } } _ { 0 } \right) _ { n }$

$$
\begin{array} { r l } & { \mathbf { X } _ { 0 } ^ { * } + \bar { \mathbf { x } } _ { 0 } = ( \mathbf { X } _ { 0 } ^ { * } ) _ { n - 1 } + ( \bar { \mathbf { x } } _ { 0 } ) _ { n - 1 } } \\ & { \qquad = ( \mathbf { X } _ { 0 } ^ { * } ) _ { n } + ( \bar { \mathbf { x } } _ { 0 } ) _ { n } } \\ & { \qquad = ( \mathbf { X } _ { 0 } ^ { * } ) _ { n - 1 } + ( \bar { \mathbf { x } } _ { 0 } ) _ { n - 1 } + ( \bar { \mathbf { x } } _ { 0 } ) _ { n } } \end{array}
$$

or

$$
( \bar { \bf x } _ { 0 } ) _ { n } = ( \bar { \bf x } _ { 0 } ) _ { n - 1 } - ( \hat { \bf x } _ { 0 } ) _ { n - 1 } .
$$

Recall from Section 4.2 that the state transition matrix is obtained by integrating

$$
{ \dot { \Phi } } ( t , t _ { k } ) = A ( t ) \Phi ( t , t _ { k } )
$$

subject to the initial conditions

$$
\Phi ( t _ { k } , t _ { k } ) = I
$$

along with the nonlinear equations, $\dot { \mathbf { X } } ^ { * } = F ( \mathbf { X } ^ { * } , t )$ , which define the nominal trajectory, $\mathbf { X } ^ { * } ( t )$ . The matrix $A ( t )$ is evaluated on the reference trajectory,

$$
A ( t ) = \frac { \partial F ( \mathbf { X } ^ { * } , t ) } { \partial \mathbf { X } }
$$

(A) Initialize for this iteration:

Set $i = 1$ . Set $t _ { i - 1 } = t _ { 0 }$ , $\mathbf { X } ^ { * } ( t _ { i - 1 } ) = \mathbf { X } _ { 0 } ^ { * }$ , $\Phi ( t _ { i - 1 } , t _ { 0 } ) = \Phi ( t _ { 0 } , t _ { 0 } ) = I$ .   
If there is an a priori estimate, set $\Lambda = \overline { { P } } _ { 0 } ^ { - 1 }$ and set $N = \overline { { P } } _ { 0 } ^ { - 1 } \bar { \mathbf { x } } _ { 0 }$ .   
If there is no a priori estimate, set $\Lambda = 0$ and set $N = 0$ .

(B) Read the next observation: $t _ { i } , \mathbf { Y } _ { i } , R _ { i }$ .

Integrate reference trajectory and state transition matrix from $t _ { i - 1 }$ to $t _ { i }$ . $\dot { \mathbf { X } } ^ { * } = F ( \mathbf { X } ^ { * } ( t ) , t )$ with initial conditions $\mathbf { X } ^ { * } ( t _ { i - 1 } )$   
$A ( t ) = [ \partial F ( \mathbf { X } , t ) / \partial \mathbf { X } ] ^ { * }$ , where ∗ means evaluated on the nominal trajectory.   
${ \dot { \Phi } } ( t , t _ { 0 } ) = A ( t ) \Phi ( t , t _ { 0 } )$ with initial conditions $\Phi ( t _ { i - 1 } , t _ { 0 } )$ .   
This gives $\mathbf { X } ^ { * } ( t _ { i } ) , \Phi ( t _ { i } , t _ { 0 } )$ .

![](images/bbcad0286f942247b57137958751a396aa9376a3de23756296757d126bc15411.jpg)

![](images/71112c9f3e2517bc85ad0e8ffad047b0a127e31db172bccc12760bb993fd6621.jpg)

![](images/33ba23dc10add28bf439865c9184ba2e310c90a5095f513e145e96d80c038aa9.jpg)  
Figure 4.6.1: Batch processing algorithm flo w chart.

where $F ( \mathbf { X } ^ { * } , t )$ is the time derivative of the state vector in the differential equations governing the time evolution of the system. The observation-state mapping matrix is given by

$$
\widetilde { H } _ { i } = \frac { \partial G ( \mathbf { X } _ { i } ^ { * } , t _ { i } ) } { \partial \mathbf { X } }
$$

where $G ( \mathbf { X } _ { i } ^ { * } , t _ { i } )$ are the observation-state relationships evaluated on the nominal or reference trajectory.

Notice that the solution for $\hat { \mathbf { x } } _ { 0 }$ involved inversion of the information matrix, $\Lambda _ { 0 }$ , where

$$
\Lambda _ { 0 } = H ^ { T } R ^ { - 1 } H + \overline { { { \cal P } } } _ { 0 } ^ { - 1 } .
$$

Generally the normal equation would not be solved by a direct inversion of $\Lambda _ { 0 }$ but rather would be solved by an indirect but more accurate technique, such as the Cholesky decomposition described in Chapter 5, Section 5.2. The sequence of operations required to implement the batch estimation process is outlined in Fig. 4.6.1. Note that the algorithm in Fig. 4.6.1 assumes that there are no observations at $t _ { 0 }$ . If observations exist at $t _ { 0 }$ , set $\overline { { \Lambda } } = \overline { { P } } _ { 0 } ^ { - 1 } + H _ { 0 } ^ { T } R _ { 0 } ^ { - 1 } H _ { 0 }$ and $N = H _ { 0 } ^ { T } R _ { 0 } ^ { - 1 } \mathbf { y } _ { 0 }$ in the initialization box, A. As previously stated, the entire sequence of computations are repeated until the estimation process has converged. If there are observations at $t _ { 0 }$ , the state transition matrix for processing these observations is the identity matrix.

This procedure yields a minimum value of the performance index (see Eq. (4.3.24))

$$
J ( x ) = ( \hat { \mathbf { x } } _ { 0 } - \bar { \mathbf { x } } _ { 0 } ) ^ { T } \overline { { P } } _ { 0 } ^ { - 1 } ( \hat { \mathbf { x } } _ { 0 } - \bar { \mathbf { x } } _ { 0 } ) + \sum _ { i = 1 } ^ { \ell } \hat { \epsilon } _ { i } ^ { T } R _ { i } ^ { - 1 } \hat { \epsilon } _ { i }
$$

where

$$
\hat { \mathbf { \epsilon } } _ { i } = \mathbf { y } _ { i } - H _ { i } \hat { \mathbf { x } } _ { 0 }
$$

and $\hat { \epsilon } _ { i }$ is the best estimate of the observation error.

In practice, $\overline { { P } } _ { 0 }$ is generally not a realistic representation of the accuracy of $\bar { \bf x } _ { 0 }$ and it is used only to better condition the estimation error covariance matrix, $P$ . In this case, $\bar { \bf x } _ { 0 }$ usually is set to zero for each iteration and ${ \overline { { P } } } _ { 0 }$ is chosen to be a diagonal matrix with large diagonal values. Hence, the firs t term in Eq. (4.6.8) will be very small and the tracking data residuals will determine the value of $J ( x )$ . The RMS of the observation residuals generally is computed and may be used as a measure of convergence; when the RMS no longer changes the solution is assumed to be converged. The RMS is computed from

$$
\mathrm { R M S } = \left\{ \frac { \displaystyle \sum _ { i = 1 } ^ { \ell } \hat { \epsilon } _ { i } ^ { T } R _ { i } ^ { - 1 } \hat { \mathbf { \epsilon } } _ { i } } { m } \right\} ^ { 1 / 2 } .
$$

$\hat { \epsilon } _ { i }$ is a p-vector and $m = \ell \times p$ . Hence, $m$ is the total number of observations. Eq. (4.6.10) is referred to as the weighted RMS. If the RMS is computed without including the weighting matrix, $R _ { i } ^ { - 1 }$ , it may be referred to as the unweighted RMS or just the RMS.

# 4.7 THE SEQUENTIAL ESTIMATION ALGORITHM

In this section, an alternate approach to the batch processor is discussed in which the observations are processed as soon as they are received. An advantage of this approach, referred to as the sequential processing algorithm, is that the matrix to be inverted will be of the same dimension as the observation vector. Hence, if the observations are processed individually, only scalar divisions will be required to obtain the estimate of $\mathbf { x } _ { k }$ . The algorithm was developed originally by Swerling (1959), but the treatment that received more popular acclaim is due to Kalman (1960). In fact, the sequential estimation algorithm discussed here often is referred to as the Kalman filter . A number of papers and textbooks have been written describing and providing variations of the Kalman fil ter. The collection of papers edited by Sorenson (1985) contains many of the pioneering papers in this area. Also, the treatments by Bierman (1977), Liebelt (1967), Tapley (1973), Gelb (1974), Maybeck (1979), Grewal and Andrews (1993), and Montenbruck and Gill (2000) are other references.

Recall that an estimate $\hat { \mathbf { x } } _ { j }$ and a covariance matrix $P _ { j }$ can be propagated forward to a time $t _ { k }$ by the relations

$$
\begin{array} { r l } & { \overline { { \mathbf { x } } } _ { k } = \Phi ( t _ { k } , t _ { j } ) \hat { \mathbf { x } } _ { j } } \\ & { \overline { { P } } _ { k } = \Phi ( t _ { k } , t _ { j } ) P _ { j } \Phi ^ { T } ( t _ { k } , t _ { j } ) . } \end{array}
$$

Assume that we have an additional observation at $t _ { k }$ (see Eq. (4.2.6)),

$$
\mathbf { y } _ { k } = \widetilde { H } _ { k } \mathbf { x } _ { k } + \boldsymbol { \epsilon } _ { k }
$$

where $E [ \epsilon _ { k } ] = 0$ and $E [ \epsilon _ { k } \epsilon _ { j } ^ { T } ] = R _ { k } \delta _ { k j }$ , where $\delta _ { k j }$ is the Kronicker delta. We wish to process $\mathbf { y } _ { k }$ in order to determine $\hat { \mathbf { x } } _ { k }$ . The best estimate of $\mathbf { x } _ { k }$ is obtained in Eq. (4.4.29) as

$$
\begin{array} { r } { \hat { \mathbf { x } } _ { k } = \big ( \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } + \overline { { P } } _ { k } ^ { - 1 } ) ^ { - 1 } \big ( \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \mathbf { y } _ { k } + \overline { { P } } _ { k } ^ { - 1 } \overline { { \mathbf { x } } } _ { k } \big ) . } \end{array}
$$

The primary computational problems are associated with computing the $( n \times n )$ matrix inverse in Eq. (4.7.3). Recall that in the original derivation it was shown that the quantity to be inverted is the information matrix $\Lambda _ { k }$ , which yields the covariance matrix $P _ { k }$ associated with estimate $\hat { \mathbf { x } } _ { k }$ (see Eq. (4.4.30)),

$$
P _ { k } = \Lambda _ { k } ^ { - 1 } = ( \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } + \overline { { P } } _ { k } ^ { \ - 1 } ) ^ { - 1 } .
$$

From Eq. (4.7.4), it follows that

$$
\begin{array} { r } { P _ { k } ^ { - 1 } = \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } + \overline { { P } } _ { k } ^ { - 1 } . } \end{array}
$$

Premultiplying each side of Eq. (4.7.5) by $P _ { k }$ and then postmultiplying by $\overline { { P } } _ { k }$ leads to the following expressions:

$$
\overline { { P } } _ { k } = P _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } \overline { { P } } _ { k } + P _ { k }
$$

or

$$
P _ { k } = \overline { { P } } _ { k } - P _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } \overline { { P } } _ { k } .
$$

Now if Eq. (4.7.6) is postmultiplied by the quantity $H _ { k } ^ { T } { \cal R } _ { k } ^ { - 1 }$ , the following expression is obtained:

$$
\begin{array} { r l } & { \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } = P _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } [ \widetilde { H } _ { k } \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } + I ] } \\ & { \qquad = P _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } [ \widetilde { H } _ { k } \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } + R _ { k } ] R _ { k } ^ { - 1 } . } \end{array}
$$

Solving for the quantity $P _ { k } \widetilde { H } _ { k } ^ { T } { R _ { k } ^ { - 1 } }$ leads to

$$
\begin{array} { r } { P _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } = \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } [ \widetilde { H } _ { k } \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } + R _ { k } ] ^ { - 1 } . } \end{array}
$$

This relates the a priori covariance matrix $\overline { { P } } _ { k }$ to the $a$ posteriori covariance matrix $P _ { k }$ . If Eq. (4.7.9) is used to eliminate $P _ { k } \widetilde { H } _ { k } ^ { T } { R _ { k } ^ { - 1 } }$ in Eq. (4.7.7), the following result is obtained:

$$
\begin{array} { r } { P _ { k } = \overline { { P } } _ { k } - \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } [ \widetilde { H } _ { k } \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } + R _ { k } ] ^ { - 1 } \widetilde { H } _ { k } \overline { { P } } _ { k } . } \end{array}
$$

Equation (4.7.10) also can be derived by using the Schur identity (Theorem 4 of Appendix B). Note that Eq. (4.7.10) is an alternate way of computing the inverse in Eq. (4.7.4). In Eq. (4.7.10), the matrix to be inverted is of dimension $p \times p$ , the same dimensions as the observation error covariance matrix. If the observations are processed as scalars (i.e., one at a time), only a scalar division is required. If the weighting matrix, $K _ { k }$ (sometimes referred to as the Kalman gain or simply gain matrix), is defined as

$$
\begin{array} { r } { K _ { k } \equiv \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } [ \widetilde { H } _ { k } \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } + R _ { k } ] ^ { - 1 } , } \end{array}
$$

then Eq. (4.7.10) can be expressed in the compact form

$$
P _ { k } = [ I - K _ { k } { \widetilde { H } } _ { k } ] { \overline { { P } } } _ { k } .
$$

If Eq. (4.7.4) is substituted into Eq. (4.7.3), the sequential form for computing $\hat { \mathbf { x } } _ { k }$ can be written as

$$
\hat { \mathbf { x } } _ { k } = P _ { k } [ \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \mathbf { y } _ { k } + \overline { { P } } _ { k } ^ { - 1 } \overline { { \mathbf { x } } } _ { k } ]
$$

$$
\mathbf { \Sigma } = P _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \mathbf { y } _ { k } + P _ { k } \overline { { P } } _ { k } ^ { - 1 } \overline { { \mathbf { x } } } _ { k } .
$$

But from Eqs. (4.7.9) and (4.7.11)

$$
K _ { k } = P _ { k } \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } .
$$

Using the preceding and Eq. (4.7.12), Eq. (4.7.13) becomes

$$
\hat { \mathbf { x } } _ { k } = K _ { k } \mathbf { y } _ { k } + [ I - K _ { k } \widetilde { H } _ { k } ] \overline { { P } } _ { k } \overline { { P } } _ { k } ^ { - 1 } \overline { { \mathbf { x } } } _ { k } .
$$

Collecting terms yields

$$
\hat { \mathbf { x } } _ { k } = \overline { { \mathbf { x } } } _ { k } + K _ { k } [ \mathbf { y } _ { k } - \widetilde { H } _ { k } \overline { { \mathbf { x } } } _ { k } ] .
$$

Equation (4.7.16), with Eqs. (4.7.1), (4.7.11), and (4.7.12), can be used in a recursive fashion to compute the estimate of $\hat { \mathbf { x } } _ { k }$ , incorporating the observation $\mathbf { y } _ { k }$ .

# 4.7.1 THE SEQUENTIAL COMPUTATIONAL ALGORITHM

The algorithm for computing the estimate sequentially is summarized as

Given: $\hat { \mathbf { x } } _ { k - 1 }$ , $P _ { k - 1 }$ , $\mathbf { X } _ { k - 1 } ^ { * }$ , and $R _ { k }$ , and the observation ${ \bf Y } _ { k }$ , at $t _ { k }$ (at the initial time $t _ { 0 }$ , these would be $\mathbf { X } _ { 0 } ^ { * }$ , $\hat { \mathbf { x } } _ { 0 }$ , and $P _ { 0 }$ ).

(1) Integrate from $t _ { k - 1 }$ to $t _ { k }$ ,

$$
\begin{array} { l l } { { { \dot { \bf X } } ^ { * } = F ( { \bf X } ^ { * } , t ) , } } & { { \qquad { \bf X } ^ { * } ( t _ { k - 1 } ) = { \bf X } _ { k - 1 } ^ { * } } } \\ { { { \dot { \Phi } } ( t , t _ { k - 1 } ) = A ( t ) \Phi ( t , t _ { k - 1 } ) , } } & { { \qquad \Phi ( t _ { k - 1 } , t _ { k - 1 } ) = I . } } \end{array}
$$

(2) Compute

$$
\begin{array} { r } { \overline { { \mathbf { x } } } _ { k } = \Phi ( t _ { k } , t _ { k - 1 } ) \widehat { \mathbf { x } } _ { k - 1 } \quad \overline { { P } } _ { k } = \Phi ( t _ { k } , t _ { k - 1 } ) P _ { k - 1 } \Phi ^ { T } ( t _ { k } , t _ { k - 1 } ) . } \end{array}
$$

(3) Compute

$$
\begin{array} { r } { \mathbf { y } _ { k } = \mathbf { Y } _ { k } - G ( \mathbf { X } _ { k } ^ { * } , t _ { k } ) \qquad { \widetilde { H } } _ { k } = { \frac { \partial G ( \mathbf { X } _ { k } ^ { * } , t _ { k } ) } { \partial \mathbf { X } } } . } \end{array}
$$

(4) Compute the measurement update

$$
\begin{array} { r l } & { K _ { k } = \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } [ \widetilde { H } _ { k } \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } + R _ { k } ] ^ { - 1 } } \\ & { \hat { \mathbf { x } } _ { k } = \overline { { \mathbf { x } } } _ { k } + K _ { k } [ \mathbf { y } _ { k } - \widetilde { H } _ { k } \overline { { \mathbf { x } } } _ { k } ] } \\ & { P _ { k } = [ I - K _ { k } \widetilde { H } _ { k } ] \overline { { P } } _ { k } . } \end{array}
$$

(5) Replace $k$ with $k + 1$ and return to (1).

Equation (4.7.1) is known as the time update and Eq. (4.7.18) is called the measurement update equation. The flow chart for the sequential computational algorithm is given in Fig. 4.7.1. If there is an observation at $t _ { 0 }$ , a time update is not performed but a measurement update is performed.

Note that we do not multiply $\widetilde { H } _ { k }$ by the state transition matrix, since the observation at $\mathbf { y } _ { k }$ is not accumulated at another time epoch, as is the case for the batch processor. Also, note that the differential equations for the state transition matrix are reinitialized at each observation epoch. Therefore, the state transition matrix is reinitialized at each observation epoch. If there is more than one observation at each epoch and we are processing them as scalars, we would set $\Phi ( t _ { i } , t _ { i } ) = I$ after processing the first observation at each epoch; $P$ and $\hat { \bf x }$ are not time updated until we move to the next observation epoch. The estimate of the state of the nonlinear system at $t _ { k }$ is given by $\hat { \mathbf { X } } _ { k } = \mathbf { \bar { X } } _ { k } ^ { * } + \hat { \mathbf { x } } _ { k }$ .

One disadvantage of both the batch and sequential algorithm lies in the fact that if the true state and the reference state are not close together then the linearization assumption leading to Eq. (4.2.6) may not be valid and the estimation process may diverge. The extended sequential filter algorithm (see Section 4.7.3) is often used to overcome problems with the linearity assumption.

A second unfavorable characteristic of the sequential estimation algorithm is that the state estimation error covariance matrix may approach zero as the number of observations becomes large. The sketch in Fig. 4.7.2 illustrates the behavior of the trace of the state estimation error covariance matrix as discrete observations are processed. As illustrated in this sketch, the trace grows between observations and is reduced by the amount, trace $( K \widetilde { H } \overline { { P } } )$ , after each observation. Hence, the magnitude of the covariance matrix elements will decrease depending on the density, information content, and accuracy of the observations.

Examination of the estimation algorithm shows that as $P _ { k } \to 0$ the gain approaches zero, and the estimation procedure will become insensitive to the observations. Consequently, the estimate will diverge due to either errors introduced in the linearization procedure, computational errors, or errors due to an incomplete mathematical model. To overcome this problem, process noise often is added to the state propagation equations (see Section 4.9).

In addition to these two problems, the Kalman filter may diverge because of numerical difficultie s associated with the covariance measurement update, given by Eq. (4.7.12). This problem is described in the next section.

# Numerical Considerations

The conventional Kalman filte r, which uses the covariance update, (4.7.12), can sometimes fail due to numerical problems with this equation. The covariance

![](images/60d483baad66a3a0c5aeaff6c324403706079b6ca401638d9485d7d69f86669f.jpg)

<table><tr><td>↓ Time Update</td></tr><tr><td>Xi=Φ(ti,ti-1)xi-1</td></tr><tr><td>Pi=Φ(ti,ti-1)Pi-1ΦT(ti,ti-1)</td></tr><tr><td>↓</td></tr></table>

Compute: observation deviation, observation-state matrix, gain matrix

$$
\begin{array} { r l } & { \mathbf { y } _ { i } = \mathbf { Y } _ { i } - G ( \mathbf { X } _ { i } ^ { * } , t _ { i } ) } \\ & { { \widetilde { H } } _ { i } = [ \partial G ( \mathbf { X } , t _ { i } ) / \partial \mathbf { X } ] ^ { * } } \\ & { K _ { i } = { \overline { { P } } } _ { i } { \widetilde { H } } _ { i } ^ { T } ( { \widetilde { H } } _ { i } { \overline { { P } } } _ { i } { \widetilde { H } } _ { i } ^ { T } + R _ { i } ) ^ { - 1 } } \end{array}
$$

Measurement Update

$$
\begin{array} { r l } & { \hat { \mathbf { x } } _ { i } = \bar { \mathbf { x } } _ { i } + K _ { i } [ \mathbf { y } _ { i } - \widetilde { H } _ { i } \bar { \mathbf { x } } _ { i } ] } \\ & { P _ { i } = ( I - K _ { i } \widetilde { H } _ { i } ) \overline { { P } } _ { i } } \\ & { \quad i = i + 1 . } \end{array}
$$

Thus: $t _ { i }$ becomes $t _ { i - 1 }$ , $\mathbf { X } ^ { * } ( t _ { i } )$ becomes $\mathbf { X } ^ { * } ( t _ { i - 1 } )$

![](images/a76d23720b91a2b81fbaf7bba57968bb92e54ec95491cae1f999e9fe198616a4.jpg)  
Figure 4.7.1: Sequential processing algorithm flo w chart.

![](images/299625b25f1bd7c3ae75b1409a6bd181cb5611d29252f027e0825fa15f560299.jpg)  
Figure 4.7.2: Illustration of the behavior of the trace of the state estimation error covariance matrix.

matrix may lose its properties of symmetry and become nonpositive definite when the computations are carried out with the finite digit arithmetic of the computer. In particular, this equation can fail to yield a symmetric positive definite result when a large a priori covariance is reduced by the incorporation of very accurate observation data.

In order to prevent these problems, several alternate algorithms have been suggested. A common alternative is to use the form of the equation given by Bucy and Joseph (1968):

$$
P _ { k } = ( I - K _ { k } \widetilde { H } _ { k } ) \overline { { P } } _ { k } ( I - K _ { k } \widetilde { H } _ { k } ) ^ { T } + K _ { k } R _ { k } K _ { k } ^ { T } .
$$

Note that this formulation will always yield a symmetric result for $P _ { k }$ , although it may lose its positive definite quality for a poorly observed system.

The most common solution to numerical problems with the covariance update is to use a square root formulation to update the covariance matrix. The square root algorithms are discussed in Chapter 5.

An example of a poorly conditioned system taken from Bierman (1977, p. 96, Example V.2) illustrates the numerical instability problem. Consider the problem of estimating $x _ { 1 }$ and $x _ { 2 }$ from scalar measurements $z _ { 1 }$ and $z _ { 2 }$ , where

$$
\begin{array} { l } { { z _ { 1 } = x _ { 1 } + \epsilon x _ { 2 } + v _ { 1 } } } \\ { { \ } } \\ { { z _ { 2 } = x _ { 1 } + x _ { 2 } + v _ { 2 } . } } \end{array}
$$

We assume that the observation noise $v _ { 1 }$ and $v _ { 2 }$ are uncorrelated, zero mean random variables with unit variance. If $v _ { 1 }$ and $v _ { 2 }$ do not have unit variance or are correlated, we can perform a simple whitening transformation so that their covariance matrix is the identity matrix (Bierman, 1977, or see Section 5.7.1). In matrix form,

$$
{ \Big [ } z _ { 1 } { \Big ] } = { \Big [ } { 1 \ \epsilon { \Big ] } } \left[ { x _ { 1 } { \Big ] } } + { \Big [ } v _ { 1 } { \Big ] } \right. .
$$

Assume that the $a$ priori covariance associated with our knowledge of $[ x _ { 1 } \ x _ { 2 } ]$ is given by

$$
{ \overline { { P } } } _ { 1 } = \sigma ^ { 2 } I
$$

where $\sigma = 1 / \epsilon$ and $0 < \epsilon \ll 1$ . The quantity $\epsilon$ is assumed to be small enough such that computer round-off produces

$$
\begin{array} { c } { { 1 + \epsilon ^ { 2 } = 1 , } } \\ { { \mathrm { a n d } } } \\ { { 1 + \epsilon \neq 1 ; } } \end{array}
$$

that is, $1 + \epsilon ^ { 2 }$ rounds to 1 and $1 + \epsilon$ does not. Note that $\sigma = 1 / \epsilon$ is large; hence, this is an illustration of the problem where accurate data is being combined with a large a priori covariance.

This estimation problem is well posed. The observation $z _ { 1 }$ provides an estimate of $x _ { 1 }$ which, when combined with $z _ { 2 }$ , should determine $x _ { 2 }$ . However, the conventional Kalman update to $P$ given by Eq. (4.7.12) will result in failure of the filte r.

The observations will be processed one at a time. Let the gain and estimation error covariance associated with $z _ { 1 }$ be denoted as $K _ { 1 }$ and $P _ { 1 }$ , respectively. Similar definitions apply for $z _ { 2 }$ .

The exact solution yields

$$
K _ { 1 } = \frac { 1 } { 1 + 2 \epsilon ^ { 2 } } \left[ { 1 \atop \epsilon } \right] .
$$

The estimation error covariance associated with processing $z _ { 1 }$ is

$$
P _ { 1 } = \frac { 1 } { 1 + 2 \epsilon ^ { 2 } } \left[ \begin{array} { c c } { { 2 } } & { { - \sigma } } \\ { { - \sigma } } & { { \sigma ^ { 2 } + 1 } } \end{array} \right] .
$$

After processing $z _ { 2 }$ it can be shown that the exact solution for the estimation error covariance is

$$
P _ { 2 } = \frac { 1 } { \beta } \left[ \begin{array} { c c } { 1 + 2 \epsilon ^ { 2 } } & { - ( 1 + \epsilon ) } \\ { - ( 1 + \epsilon ) } & { 2 + \epsilon ^ { 2 } } \end{array} \right] ,
$$

where

$$
\beta = 1 - 2 \epsilon + 2 \epsilon ^ { 2 } ( 2 + \epsilon ^ { 2 } )
$$

and we see that both $P _ { 1 }$ and $P _ { 2 }$ are symmetric and positive definite.

The conventional Kalman filter, subject to Eq. (4.7.21), yields

$$
K _ { 1 } = { \left[ \begin{array} { l } { 1 } \\ { \epsilon } \end{array} \right] }
$$

and

$$
P _ { 1 } = \left[ \begin{array} { c c } { { 0 } } & { { - \sigma } } \\ { { - \sigma } } & { { \sigma ^ { 2 } } } \end{array} \right] .
$$

Note that $P _ { 1 }$ is no longer positive definite and the filter will not produce correct results. If $z _ { 2 }$ is processed, the conventional Kalman filter yields

$$
P _ { 2 } = \frac { 1 } { 1 - 2 \epsilon } \left[ \begin{array} { r r } { - 1 } & { 1 } \\ { 1 } & { - 1 } \end{array} \right] .
$$

Note that $P _ { 2 }$ does not have positive terms on the diagonal and $| P _ { 2 } | = 0$ . Hence, the conventional Kalman filter has failed.

By way of comparison, the Joseph formulation yields

$$
\begin{array} { l } { P _ { 1 } = \left[ \begin{array} { c c } { 2 } & { - \sigma } \\ { - \sigma } & { \sigma ^ { 2 } } \end{array} \right] } \\ { P _ { 2 } = \left[ \begin{array} { c c } { 1 + 2 \epsilon } & { - ( 1 + 3 \epsilon ) } \\ { - ( 1 + 3 \epsilon ) } & { ( 2 + \epsilon ) } \end{array} \right] } \end{array}
$$

which are symmetric and positive definite and agree with the exact solution to $O ( \epsilon )$ .

It should be pointed out that the batch processor for this problem, under the same assumption that $1 + \epsilon ^ { 2 } = 1 $ , yields

$$
P _ { 2 } = \left[ \begin{array} { c c } { { 1 + 2 \epsilon } } & { { - ( 1 + 3 \epsilon ) } } \\ { { - ( 1 + 3 \epsilon ) } } & { { 2 ( 1 + 2 \epsilon ) } } \end{array} \right] .
$$

This agrees to $O ( \epsilon )$ with the exact solution for $P _ { 2 }$ . The batch solution is not as sensitive as the conventional Kalman filt er to computer round-off errors. An intuitive understanding of this can be had by examining the equations for $P$ .

For the batch processor

$$
P = ( \overline { { P } } _ { 0 } ^ { \ - 1 } + \sum _ { i = 1 } ^ { \ell } H _ { i } ^ { T } R ^ { - 1 } H _ { i } ) ^ { - 1 } ,
$$

and for the sequential processor

$$
P = ( I - \overline { { P } } \widetilde { H } ^ { T } ( \widetilde { H } \overline { { P } } \widetilde { H } ^ { T } + R ) ^ { - 1 } \widetilde { H } ) \overline { { P } } .
$$

![](images/fd86a46bed129bb97d07da78bff502948dec04c255142bc17d00ddb43fb70d17.jpg)  
Figure 4.7.3: Difference of the exact trace of $P _ { 2 }$ and that for various algorithms versus the value of $\epsilon$ on the abscissa.

Hence, if very accurate tracking data (small values for the elements of $R$ ) are combined with a large a priori (large values for the elements of $\overline { { P } }$ ), the sequential algorithm will ignore the data contribution, $R$ , when it adds $\widetilde { H } \overline { { P } } \widetilde { H } ^ { T } + R$ ; whereas the batch processor will tend to ignore $\overline { { P } } _ { 0 } ^ { - 1 }$ and base its solution on the strength of the data when it computes $( \Sigma H ^ { T } R ^ { - 1 } H + \overline { { P } } _ { 0 } ^ { - 1 } )$ . It is emphasized that for sequential processing of the data the preferred solution to this problem is to use one of the square root formulations for propagating the covariance or information matrix discussed in Chapter 5.

Figure 4.7.3 shows the difference between the exact value of the trace of $P _ { 2 }$ and the trace computed using various algorithms on a 16-digit machine. Notice that the conventional Kalman update yields an error of O(1) for $\epsilon \simeq 1 0 ^ { - 8 }$ , whereas the Joseph and Potter algorithms approach this value for $\epsilon = 1 0 ^ { - 1 5 }$ . Also, the Givens and Householder algorithms, which are introduced in Chapter 5, and the batch algorithm are all highly accurate.

# 4.7.2 THE EXTENDED SEQUENTIAL ESTIMATION ALGORITHM

To minimize the effects of errors due to the neglect of higher order terms in the linearization procedure leading to Eq. (4.2.6), the extended form of the sequential estimation algorithm is sometimes used. This algorithm is often referred to as the Extended Kalman Filter (EKF). The primary difference between the sequential and the extended sequential algorithm is that the reference trajectory for the extended sequential algorithm is updated after each observation to reflect the best estimate of the true trajectory. For example, after processing the $k ^ { \mathrm { t h } }$ observation, the best estimate of the state vector at $t _ { k }$ is used to provide new initial conditions for the reference trajectory,

$$
( \mathbf { X } _ { k } ^ { * } ) _ { \mathrm { n e w } } = \hat { \mathbf { X } } _ { k } = \mathbf { X } _ { k } ^ { * } + \hat { \mathbf { x } } _ { k } .
$$

Using $\hat { \mathbf { X } } _ { k }$ for the reference trajectory leads to $\hat { \mathbf { x } } _ { k } = 0$ , which will result in $\bar { \bf x } _ { k + 1 } =$ 0. The integration for the reference trajectory and the state transition matrix is reinitialized at each observation epoch, and the equations are integrated forward from $t _ { k }$ to $t _ { k + 1 }$ . The estimate for $\hat { \mathbf { x } } _ { k + 1 }$ is then computed from

$$
\hat { \mathbf { x } } _ { k + 1 } = K _ { k + 1 } \mathbf { y } _ { k + 1 }
$$

where $K _ { k + 1 }$ and $\mathbf { y } _ { k + 1 }$ are computed based on the new reference orbit. Then, the reference orbit is updated at time $t _ { k + 1 }$ by incorporating $\hat { \mathbf { x } } _ { k + 1 }$ and the process proceeds to $t _ { k + 2 }$ . The process of incorporating the estimate at each observation point into the reference trajectory for propagating to the next observation epoch leads to the reference trajectory being the prediction of the estimate of the nonlinear state; for example, $\mathbf { X } ^ { * } ( t ) = \dot { \mathbf { X } } ( t )$ .

In actual practice, it is not a good idea to update the reference trajectory using the first observations. This is particularly true if the observations contain significant noise. After a few observations have been processed, the estimates of $\hat { \bf x }$ will stabilize, and the trajectory update can be initiated.

The advantage of the extended sequential algorithm is that convergence to the best estimate will be more rapid because errors introduced in the linearization process are reduced. In addition, because the state estimate deviation, $\hat { { \bf x } } ( t )$ , need not be mapped between observations, it is not necessary to compute the state transition matrix. The estimation error covariance matrix, $P ( t )$ , can be mapped by integrating the matrix differential equation (4.9.35) discussed in Section 4.9.

The major disadvantage of the extended sequential algorithm is that the differential equations for the reference trajectory must be reinitialized after each observation is processed.

# 4.7.3 THE EXTENDED SEQUENTIAL COMPUTATIONAL ALGORITHM

The algorithm for computing the extended sequential estimate can be summarized as follows:

Given: $P _ { k - 1 }$ , $\hat { \mathbf X } _ { k - 1 }$ and ${ \bf Y } _ { k } , R _ { k }$

(1) Integrate from $t _ { k - 1 }$ to $t _ { k }$

$$
\begin{array} { l } { \dot { \mathbf { X } } ^ { * } = F ( \mathbf { X } ^ { * } , t ) , \qquad \mathbf { X } ^ { * } ( t _ { k - 1 } ) \mathbf { \Omega } = \hat { \mathbf { X } } _ { k - 1 } } \\ { \dot { \Phi } ( t , t _ { k - 1 } ) = A ( t ) \Phi ( t , t _ { k - 1 } ) , \Phi ( t _ { k - 1 } , t _ { k - 1 } ) = I . } \end{array}
$$

(2) Compute

$$
\begin{array} { r l } & { \overline { { P } } _ { k } = \Phi ( t _ { k } , t _ { k - 1 } ) P _ { k - 1 } \Phi ^ { T } ( t _ { k } , t _ { k - 1 } ) } \\ & { \mathbf { y } _ { k } = \mathbf { Y } _ { k } - G ( \mathbf { X } _ { k } ^ { * } , t _ { k } ) } \\ & { \widetilde { H } _ { k } = \partial G ( \mathbf { X } _ { k } ^ { * } , t _ { k } ) / \partial \mathbf { X } _ { k } . } \end{array}
$$

(3) Compute

$$
\begin{array} { r l } & { K _ { k } = \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } [ \widetilde { H } _ { k } \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } + R _ { k } ] ^ { - 1 } } \\ & { \hat { \mathbf { X } } _ { k } = \mathbf { X } _ { k } ^ { * } + K _ { k } \mathbf { y } _ { k } } \\ & { P _ { k } = [ I - K _ { k } \widetilde { H } _ { k } ] \overline { { P } } _ { k } . } \end{array}
$$

(4) Replace $k$ with $k + 1$ and return to (1).

The flo w chart for the extended sequential computational algorithm is given in Fig. 4.7.4.

# 4.7.4 THE PREDICTION RESIDUAL

It is of interest to examine the variance of the predicted residuals, which are sometimes referred to as the innovation, or new information, which comes from each measurement. The predicted residual, or innovation, is the observation residual based on the a priori or predicted state , $\bar { \mathbf { x } } _ { k }$ , at the observation time, $t _ { k }$ , and is defined as

$$
\beta _ { k } = \mathbf { y } _ { k } - \widetilde { H } _ { k } \overline { { \mathbf { x } } } _ { k } .
$$

As noted previously,

$$
\begin{array} { r } { \overline { { \mathbf { x } } } _ { k } = \mathbf { x } _ { k } + \pmb { \eta } _ { k } } \\ { \mathbf { y } _ { k } = \widetilde { H } _ { k } \mathbf { x } _ { k } + \epsilon _ { k } } \end{array}
$$

where $\mathbf { x } _ { k }$ is the true value of the state deviation vector and $\eta _ { k }$ is the error in $\bar { \bf x } _ { k }$ Also,

$$
E [ \pmb { \eta } _ { k } ] = 0 , E [ \pmb { \eta } _ { k } \pmb { \eta } _ { k } ^ { T } ] = \overline { { P } } _ { k }
$$

and

$$
\begin{array} { c } { E [ \epsilon _ { k } ] = 0 , E [ \epsilon _ { k } \epsilon _ { k } ^ { T } ] = R _ { k } } \\ { E [ \epsilon _ { k } \eta _ { k } ^ { T } ] = 0 . } \end{array}
$$

From these conditions it follows that $\beta _ { k }$ has mean

$$
\begin{array} { l } { { \displaystyle E [ \beta _ { k } ] \equiv \overline { { \beta } } _ { k } = E \big ( \widetilde { H } _ { k } \mathbf { x } _ { k } + \epsilon _ { k } - \widetilde { H } _ { k } \overline { { \mathbf { x } } } _ { k } \big ) } } \\ { ~ = E \big ( \epsilon _ { k } - \widetilde { H } \pmb { \eta } _ { k } \big ) = 0 } \end{array}
$$

and variance-covariance

$$
\begin{array} { r l } & { P _ { \beta _ { k } } = E [ ( \beta _ { k } - \widetilde { \beta } _ { k } ) ( \beta _ { k } - \widetilde { \beta } _ { k } ) ^ { T } ] = E [ \beta _ { k } \beta _ { k } ^ { T } ] } \\ & { \quad \quad = E [ ( \mathbf { y } _ { k } - \widetilde { H } _ { k } \overline { { \mathbf { x } } } _ { k } ) ( \mathbf { y } _ { k } - \widetilde { H } _ { k } \overline { { \mathbf { x } } } _ { k } ) ^ { T } ] } \\ & { \quad \quad = E [ ( \epsilon _ { k } - \widetilde { H } _ { k } \eta _ { k } ) ( \epsilon _ { k } - \widetilde { H } _ { k } \eta _ { k } ) ^ { T } ] } \\ & { P _ { \beta _ { k } } = R _ { k } + \widetilde { H } _ { k } \widetilde { P } _ { k } \widetilde { H } _ { k } ^ { T } . } \end{array}
$$

Hence, for a large prediction residual variance-covariance, the Kalman gain

$$
K _ { k } = \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } P _ { \beta _ { k } } ^ { - 1 }
$$

will be small, and the observation will have little influence on the estimate of the state. Also, large values of the prediction residual relative to the prediction residual standard deviation may be an indication of bad tracking data and hence may be used to edit data from the solution.

# 4.8 EXAMPLE PROBLEMS

This section provides several examples that involve processing observations with the batch and sequential processors.

# 4.8.1 LINEAR SYSTEM

Given: A system described by

$$
\mathbf { x } ( t _ { i + 1 } ) = { \left[ \begin{array} { l } { x _ { 1 } ( t _ { i + 1 } ) } \\ { x _ { 2 } ( t _ { i + 1 } ) } \end{array} \right] } = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { x _ { 1 } ( t _ { i } ) } \\ { x _ { 2 } ( t _ { i } ) } \end{array} \right] }
$$

![](images/8dabb60293eb43d2a585e8a97a8069b690434857bb41fd3ecd327dc40f6fbc7b.jpg)  
Figure 4.8.1: Extended sequential processing algorithm flo w chart.

and observation-state relationship

$$
\left[ \begin{array} { c } { y _ { 1 } ( t _ { i } ) } \\ { y _ { 2 } ( t _ { i } ) } \end{array} \right] = \left[ \begin{array} { c c } { 0 } & { 1 } \\ { 1 / 2 } & { 1 / 2 } \end{array} \right] \left[ \begin{array} { c } { x _ { 1 } ( t _ { i } ) } \\ { x _ { 2 } ( t _ { i } ) } \end{array} \right] + \left[ \begin{array} { c } { \epsilon _ { 1 } } \\ { \epsilon _ { 2 } } \end{array} \right]
$$

with a priori information

$$
\overline { { \mathbf { x } } } _ { 0 } = \overline { { \mathbf { x } } } ( t _ { 0 } ) = \left[ \begin{array} { l } { \overline { { x } } _ { 1 } ( t _ { 0 } ) } \\ { \overline { { x } } _ { 2 } ( t _ { 0 } ) } \end{array} \right] = \left[ \begin{array} { l } { 3 } \\ { 2 } \end{array} \right] , \overline { { P } } _ { 0 } = \overline { { P } } ( t _ { 0 } ) = \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right]
$$

$$
W ^ { - 1 } = R = E \left\{ \left[ \epsilon _ { 1 } \atop \epsilon _ { 2 } \right] \left[ \epsilon _ { 1 } \epsilon _ { 2 } \right] \right\} = \left[ \begin{array} { l l } { { 2 } } & { { 0 } } \\ { { 0 } } & { { 3 / 4 } } \end{array} \right]
$$

and observations at $t _ { 1 }$ given by

$$
{ \left[ \begin{array} { l } { y _ { 1 } ( t _ { 1 } ) } \\ { y _ { 2 } ( t _ { 1 } ) } \end{array} \right] } = { \left[ \begin{array} { l } { 6 } \\ { 4 } \end{array} \right] } .
$$

(1) Using the batch processor algorithm, determine the best estimate of $\mathbf { x } ( t _ { 0 } )$ based on observations $y _ { 1 } ( t _ { 1 } )$ and $y _ { 2 } ( t _ { 1 } ) , \overline { { \mathbf { x } } } ( t _ { 0 } ) , \overline { { P } } ( t _ { 0 } )$ , and $R$ .

(2) Using the sequential algorithm and the information given, determine $\hat { \mathbf { x } } ( t _ { 1 } )$ the best estimate of $\mathbf { x } ( t _ { 1 } )$ .

(3) Show that $\hat { \mathbf { x } } ( t _ { 0 } )$ obtained in (1), when mapped forward to $t _ { 1 }$ is equal to $\hat { \mathbf { x } } ( t _ { 1 } )$ obtained in (2). Show that $P _ { 0 }$ from the batch processor mapped forward to $t _ { 1 }$ agrees with $P _ { 1 }$ from the sequential processor.

(1) Batch Processor

$$
\begin{array} { r l } & { \Phi ( t _ { i + 1 } , t _ { i } ) = \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } \\ & { \qquad \widetilde { H } = \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 1 / 2 } & { 1 / 2 } \end{array} \right] , \quad \overline { { P } } _ { o } = \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] , \quad \overline { { \mathbf { x } } } _ { o } = \left[ \begin{array} { l } { 3 } \\ { 2 } \end{array} \right] } \\ & { W ^ { - 1 } = R = \left[ \begin{array} { l l } { 2 } & { 0 } \\ { 0 } & { 3 / 4 } \end{array} \right] } \\ & { \qquad \mathbf { y } = \left[ \begin{array} { l } { y _ { 1 } ( t _ { 1 } ) } \\ { y _ { 2 } ( t _ { 1 } ) } \end{array} \right] = \left[ \begin{array} { l } { 6 } \\ { 4 } \end{array} \right] . } \end{array}
$$

The computational algorithm for the batch processor is given in Section 4.6.

$$
\begin{array} { r l } & { \hat { \mathbf { x } } _ { 0 } = ( \overline { { P } } _ { 0 } ^ { - 1 } + H _ { 1 } ^ { T } W H _ { 1 } ) ^ { - 1 } ( H _ { 1 } ^ { T } W \mathbf { y } + \overline { { P } } _ { 0 } ^ { - 1 } \overline { { \mathbf { x } } } _ { 0 } ) } \\ & { H _ { 1 } = \widetilde { H } _ { 1 } \Phi ( t _ { 1 } , t _ { 0 } ) = \left[ \begin{array} { c c } { 0 } & { 1 } \\ { 1 / 2 } & { 1 / 2 } \end{array} \right] \left[ \begin{array} { c c } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] = \left[ \begin{array} { c c } { 0 } & { 1 } \\ { 1 / 2 } & { 1 } \end{array} \right] } \end{array}
$$

$$
\begin{array} { r l } & { \tilde { \mathbf { x } } _ { 0 } = \left\{ \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] + \left[ \begin{array} { l l } { 0 } & { 1 / 2 } \\ { 1 } & { 1 } \end{array} \right] \left[ \begin{array} { l l } { 1 / 2 } & { 0 } \\ { 0 } & { 4 / 3 } \end{array} \right] \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 1 / 2 } & { 1 } \end{array} \right] \right\} ^ { - 1 } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \left\{ \left[ \begin{array} { l l } { 0 } & { 1 / 2 } \\ { 1 } & { 1 } \end{array} \right] \left[ \begin{array} { l l } { 1 / 2 } & { 0 } \\ { 0 } & { 4 / 3 } \end{array} \right] \left[ \begin{array} { l } { 6 } \\ { 4 } \end{array} \right] + \left[ \frac { 3 2 } { 2 } \right] \right\}  \\ & { \quad \quad \quad \quad \tilde { \mathbf { x } } _ { o } = \left[ \begin{array} { l l } { 4 / 3 } & { 2 / 3 } \\ { 2 / 3 } & { 1 7 / 6 } \end{array} \right] ^ { - 1 } \left[ \begin{array} { l } { 1 7 / 3 } \\ { 3 1 / 3 } \end{array} \right] } \\ & { \quad \quad \quad \tilde { \mathbf { x } } _ { o } = \left[ \begin{array} { l l } { 1 7 / 2 0 } & { - 1 / 5 } \\ { - 1 / 5 } & { 2 / 5 } \end{array} \right] \left[ \begin{array} { l } { 1 7 / 3 } \\ { 3 1 / 3 } \end{array} \right] } \\ & { \quad \quad \quad \quad \quad \tilde { \mathbf { x } } _ { 0 } = \left[ \begin{array} { l l } { 2 / 3 } & { - 1 / 5 } \end{array} \right] \left[ \begin{array} { l } { 1 7 / 3 } \\ { 3 1 / 3 } \end{array} \right] } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \tilde { \mathbf { x } } _ { 0 } = \left[ \begin{array} { l } { 2 / 3 } \\ { 3 } \end{array} \right] } \end{array}
$$

Note that

$$
P _ { 0 } = \left[ \begin{array} { c c } { { \ 1 7 / 2 0 } } & { { \ - 1 / 5 } } \\ { { - 1 / 5 } } & { { \ 2 / 5 } } \end{array} \right] .
$$

The correlation matrix, computed from $P _ { 0 }$ , has standard deviations on the diagonal and correlation coefficient s for the lower off-diagonal terms,

$$
\left[ \begin{array} { c } { \sigma _ { x _ { 1 } } } \\ { \rho _ { x _ { 1 } x _ { 2 } } \sigma _ { x _ { 2 } } } \end{array} \right] = \left[ \begin{array} { c c } { \phantom { - } . 9 2 2 } \\ { - . 3 4 3 } & { . 6 3 2 } \end{array} \right] .
$$

(2) Sequential Processor

$$
\begin{array} { r l } & { \hat { \mathbf { x } } _ { 1 } = \overline { { \mathbf { x } } } _ { 1 } + \overline { { P } } _ { 1 } \widetilde { H } _ { 1 } ^ { T } ( W _ { 1 } ^ { - 1 } + \widetilde { H } _ { 1 } \overline { { P } } _ { 1 } \widetilde { H } _ { 1 } ^ { T } ) ^ { - 1 } \big ( \mathbf { y } _ { 1 } - \widetilde { H } _ { 1 } \overline { { \mathbf { x } } } _ { 1 } \big ) } \\ & { \qquad = \overline { { \mathbf { x } } } _ { 1 } + K _ { 1 } \big ( \mathbf { y } _ { 1 } - \widetilde { H } _ { 1 } \overline { { \mathbf { x } } } _ { 1 } \big ) } \end{array}
$$

From the problem definition

$$
{ \begin{array} { l } { { \overline { { \mathbf { x } } } } _ { 1 } = \Phi ( t _ { 1 } , t _ { 0 } ) { \overline { { \mathbf { x } } } } _ { o } } \\ { = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { 3 } \\ { 2 } \end{array} \right] } = { \left[ \begin{array} { l } { 5 } \\ { 2 } \end{array} \right] } } \end{array} }
$$

$$
{ \begin{array} { r l } & { { \overline { { P } } } _ { 1 } = \Phi ( t _ { 1 } , t _ { 0 } ) { \overline { { P } } } _ { o } \Phi ^ { T } ( t _ { 1 } , t _ { 0 } ) } \\ & { \quad = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 1 } & { 1 } \end{array} \right] } = { \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 1 } \end{array} \right] } } \end{array} }
$$

$$
\overline { { P } } _ { 1 } \widetilde { H } _ { 1 } ^ { T } = \left[ \begin{array} { c c } { 2 } & { 1 } \\ { 1 } & { 1 } \end{array} \right] \left[ \begin{array} { c c } { 0 } & { 1 / 2 } \\ { 1 } & { 1 / 2 } \end{array} \right] = \left[ \begin{array} { c c } { 1 3 / 2 } \\ { 1 } & { 1 } \end{array} \right]
$$

$$
\widetilde { H } _ { 1 } \overline { { { P } } } _ { 1 } \widetilde { H } _ { 1 } ^ { T } = \left[ \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { 1 / 2 } } & { { 1 / 2 } } \end{array} \right] \left[ \begin{array} { c c } { { 1 } } & { { 3 / 2 } } \\ { { 1 } } & { { 1 } } \end{array} \right] = \left[ \begin{array} { c c } { { 1 } } & { { 1 } } \\ { { 1 } } & { { 5 / 4 } } \end{array} \right]
$$

$$
\begin{array} { r l } & { ( W _ { 1 } ^ { - 1 } + \widetilde { H } _ { 1 } \overline { { P } } _ { 1 } \widetilde { H } _ { 1 } ^ { T } ) ^ { - 1 } = \left[ \left( \begin{array} { c c } { 2 } & { 0 } \\ { 0 } & { 3 / 4 } \end{array} \right) + \left( \begin{array} { c c } { 1 } & { 1 } \\ { 1 } & { 5 / 4 } \end{array} \right) \right] ^ { - 1 } } \\ & { \qquad = \left[ \begin{array} { c c } { 2 / 5 } & { - 1 / 5 } \\ { - 1 / 5 } & { 3 / 5 } \end{array} \right] } \end{array}
$$

$$
\begin{array} { r l } & { K _ { 1 } = \overline { { P } } _ { 1 } \widetilde { H } _ { 1 } ^ { T } ( W _ { 1 } ^ { - 1 } + \widetilde { H } _ { 1 } \overline { { P } } _ { 1 } \widetilde { H } _ { 1 } ^ { T } ) ^ { - 1 } } \\ & { \quad = \left[ 1 3 / 2 \right] \left[ \begin{array} { c c } { 2 / 5 } & { - 1 / 5 } \\ { - 1 / 5 } & { 3 / 5 } \end{array} \right] = \left[ \begin{array} { c c } { 1 / 1 0 } & { 7 / 1 0 } \\ { 1 / 5 } & { 2 / 5 } \end{array} \right] . } \end{array}
$$

With these results,

$$
\begin{array} { r l } &  \hat { \mathbf { x } } _ { 1 } = \left[ \begin{array} { l } { 5 } \\ { 2 } \end{array} \right] + \left[ \begin{array} { l l } { 1 / 1 0 } & { 7 / 1 0 } \\ { 1 / 5 } & { 2 / 5 } \end{array} \right] \left\{ \begin{array} { l } { \left[ 6 \right] - \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 1 / 2 } & { 1 / 2 } \end{array} \right] \left[ \begin{array} { l } { 5 } \\ { 2 } \end{array} \right] \right\} } \\ & { \quad = \left[ \begin{array} { l l } { 5 } \\ { 2 } \end{array} \right] + \left[ \begin{array} { l l } { 1 / 1 0 } & { 7 / 1 0 } \\ { 1 / 5 } & { 2 / 5 } \end{array} \right] \left[ \begin{array} { l } { 4 } \\ { 1 / 2 } \end{array} \right] } \\ & { \quad \hat { \mathbf { x } } _ { 1 } = \left[ \begin{array} { l } { 5 \frac { 3 } { 4 } } \\ { 3 } \end{array} \right] } \\ & { \quad P _ { 1 } = \left( I - K _ { 1 } \widetilde { H } _ { 1 } \right) \overline { { P } } _ { 1 } } \\ & { \quad = \left\{ \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] - \left[ \begin{array} { l l } { 7 / 2 0 } & { 9 / 2 0 } \\ { 1 / 5 } & { 2 / 5 } \end{array} \right] \right\} \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 1 } & { 1 } \end{array} \right] } \\ & { \quad P _ { 1 } = \left[ \begin{array} { l l } { 1 7 / 2 0 } & { 1 / 5 } \\ { 1 / 5 } & { 2 / 5 } \end{array} \right] . } \end{array} \end{array}
$$

(3) Map $\hat { \mathbf { x } } _ { o }$ obtained with the batch processor to $t _ { 1 }$ .

$$
{ \begin{array} { r l } & { { \hat { \mathbf { x } } } _ { 1 } = \Phi ( t _ { 1 } , t _ { 0 } ) { \hat { \mathbf { x } } } _ { 0 } } \\ & { \quad = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { 2 { \frac { 3 } { 4 } } } \\ { 3 } \end{array} \right] } } \\ & { \quad = { \left[ \begin{array} { l } { 5 { \frac { 3 } { 4 } } } \\ { 3 } \end{array} \right] } } \end{array} }
$$

Hence, the batch and sequential estimates and covariances at $t _ { 1 }$ agree.

Note that $P _ { 0 }$ from the batch processor may be mapped to $t _ { 1 }$ by

$$
\begin{array} { c } { P _ { 1 } = \Phi ( t _ { 1 } , t _ { 0 } ) P _ { 0 } \Phi ^ { T } ( t _ { 1 } , t _ { 0 } ) } \\ { = \left[ \begin{array} { c c } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { c c } { 1 7 / 2 0 } & { - 1 / 5 } \\ { - 1 / 5 } & { 2 / 5 } \end{array} \right] \left[ \begin{array} { c c } { 1 } & { 0 } \\ { 1 } & { 1 } \end{array} \right] } \end{array}
$$

![](images/f8cccd098e2cbecc543102d68a35cd22304a95c277c639fbe667d37a2bad0de8.jpg)  
Figure 4.8.2: Spring-mass system.

$$
P _ { 1 } = \left[ { \begin{array} { r r } { 1 7 / 2 0 } & { 1 / 5 } \\ { 1 / 5 } & { 2 / 5 } \end{array} } \right] ,
$$

which agrees with the sequential processor results.

# 4.8.2 SPRING-MASS PROBLEM

A block of mass $m$ is attached to two parallel vertical walls by two springs as shown in Fig. 4.8.2. $k _ { 1 }$ and $k _ { 2 }$ are the spring constants. $h$ is the height of the position $P$ on one of the walls, from which the distance, $\rho$ , and the rate of change of distance of the block from $P$ , $\dot { \rho }$ , can be observed.

Let the horizontal distances be measured with respect to the point $O$ where the line $O P$ , the lengths of the springs, and the center of mass of the block are all assumed to be in the same vertical plane. Then, if $\bar { x }$ denotes the position of the block at static equilibrium, the equation of motion of the block is given by

$$
{ \ddot { x } } \equiv { \dot { v } } = - ( k _ { 1 } + k _ { 2 } ) ( x - { \bar { x } } ) / m .
$$

Let

$$
\omega ^ { 2 } = ( k _ { 1 } + k _ { 2 } ) / m .
$$

Since $\bar { x }$ is an arbitrary constant we have set it to zero so that Eq. (4.8.1) can be

written as

$$
\dot { v } + \omega ^ { 2 } x = 0 .
$$

Consider the problem of estimating the position and the velocity of the block with respect to the reference point $O$ , by using the range and range-rate measurements of the block from the point, $P$ . In order to formulate this problem mathematically, the estimation state vector is taken as ${ \bf X } ^ { T } = [ x \textbf { } v ]$ . Then the system dynamics are represented by

$$
{ \dot { \bf X } } = F ( { \bf X } , t ) = \left[ { \dot { x } } \right] = \left[ { v \atop - \omega ^ { 2 } x } \right] = \left[ \begin{array} { c c } { 0 } & { 1 } \\ { - \omega ^ { 2 } } & { 0 } \end{array} \right] \ \left[ \begin{array} { c } { x } \\ { v } \end{array} \right] \ .
$$

The observation vector is

$$
\mathbf { Y } ( t ) = \left[ \rho \atop \dot { \rho } \right] .
$$

Also,

$$
G ( \mathbf { X } ^ { * } , t ) = \left[ \rho \atop \dot { \rho } \right] ^ { * } = \left[ \sqrt { x ^ { 2 } + h ^ { 2 } } \right] ^ { * } .
$$

The system parameters are $m , k _ { 1 } , k _ { 2 }$ (from dynamics), and $h$ (from geometry).

Note that the state propagation equation, Eq. (4.8.3), is linear in the state variables $\mathbf { x }$ and $v$ . However, the observation-state equation, Eq. (4.8.4), is nonlinear. Hence, the system must be linearized about a reference solution. Accordingly, let

$$
\delta \mathbf { X } ( t ) = { \bigg [ } x ( t ) - x ^ { * } ( t ) { \bigg ] }
$$

and we will solve for $\delta \hat { \mathbf X } ( t _ { 0 } ) \equiv \delta \hat { \mathbf X } _ { 0 }$ and

$$
\begin{array} { c } { \delta \dot { \mathbf { X } } ( t ) = A ( t ) \delta \mathbf { X } ( t ) } \\ { \mathbf { y } ( t ) = \widetilde { H } \delta \mathbf { X } ( t ) } \end{array}
$$

where

$$
\mathbf { y } ( t ) = \mathbf { Y } ( t ) - G ( \mathbf { X } ^ { * } , t )
$$

$$
\begin{array} { r l } & { \boldsymbol { A } ( t ) = \left[ \begin{array} { c c } { 0 } & { 1 } \\ { - \omega ^ { 2 } } & { 0 } \end{array} \right] } \\ & { \boldsymbol { \widetilde { H } } = \left[ \begin{array} { c c } { \frac { \boldsymbol { x } } { \rho } } & { 0 } \\ { \left( \frac { \boldsymbol { v } } { \rho } - \frac { \boldsymbol { x } ^ { 2 } { \boldsymbol { v } } } { \rho ^ { 3 } } \right) } & { \frac { \boldsymbol { x } } { \rho } } \end{array} \right] . } \end{array}
$$

The solution to Eq. (4.8.3) is given by (assuming $t _ { 0 } = 0$ )

$$
\begin{array} { r l } & { x ( t ) = x _ { 0 } \cos \omega t + \frac { v _ { 0 } } { \omega } \sin \omega t } \\ & { v ( t ) = v _ { 0 } \cos \omega t - x _ { 0 } \omega \sin \omega t . } \end{array}
$$

Hence, we could determine the state transition matrix by differentiating Eq. (4.8.5),

$$
\Phi ( t , 0 ) = \frac { \partial { \bf X } ( t ) } { \partial { \bf X } ( t _ { 0 } ) } .
$$

Alternatively, the solution to the variational equation

$$
{ \dot { \Phi } } ( t , 0 ) = A ( t ) \Phi ( t , 0 ) , \quad \Phi ( 0 , 0 ) = I
$$

is given by

$$
\begin{array} { r } { \Phi ( t , 0 ) = \left[ \begin{array} { c c } { \cos \omega t } & { \frac { 1 } { \omega } \sin \omega t } \\ { - \omega \sin \omega t } & { \cos \omega t } \end{array} \right] } \end{array}
$$

hence,

$$
\begin{array} { r } { \delta \mathbf { X } ( t ) = \Phi ( t , 0 ) \delta \mathbf { X } ( t _ { 0 } ) . } \end{array}
$$

Also,

$$
H _ { i } = \widetilde { H } _ { i } \Phi ( t _ { i } , 0 ) .
$$

Perfect observations were simulated for a period of 10 seconds at one-second intervals (see Table 4.8.1), assuming the following values for the system parameters and the initial condition for the state parameters:

Table 4.8.1: Observation Data   

<table><tr><td>Time (s)</td><td>p(m)</td><td>p(m/s)</td></tr><tr><td></td><td></td><td></td></tr><tr><td>0.00</td><td>6.1773780845922</td><td>0</td></tr><tr><td>1.00</td><td>5.56327661282686</td><td>1.31285863495514</td></tr><tr><td>2.00</td><td>5.69420161397342</td><td>-1.54488114381612</td></tr><tr><td>3.00</td><td>6.15294262127432</td><td>0.534923988815733</td></tr><tr><td>4.00</td><td>5.46251322092491</td><td>0.884698415328368</td></tr><tr><td>5.00</td><td>5.83638064328625</td><td>-1.56123248918054</td></tr><tr><td>6.00</td><td>6.08236452736002</td><td>1.00979943157547</td></tr><tr><td>7.00</td><td>5.40737619817037</td><td>0.31705117039215</td></tr><tr><td>8.00</td><td>5.97065615746125</td><td>-1.37453070975606</td></tr><tr><td>9.00</td><td>5.97369258835895</td><td>1.36768169443236</td></tr><tr><td>10.00</td><td>5.40669060248179</td><td>-0.302111588503166</td></tr></table>

$$
\begin{array} { r l } & { k _ { 1 } = 2 . 5 ~ \mathrm { N / m } } \\ & { k _ { 2 } = 3 . 7 ~ \mathrm { N / m } } \\ & { m = 1 . 5 ~ \mathrm { k g } } \\ & { ~ h = 5 . 4 ~ \mathrm { m } } \\ & { x _ { 0 } = 3 . 0 ~ \mathrm { m } } \\ & { v _ { 0 } = 0 . 0 ~ \mathrm { m / s } . } \end{array}
$$

The 11 perfect observations were processed using the batch processor with the following a priori values:

$$
\mathbf { X } _ { 0 } ^ { * } = \left[ \begin{array} { c } { 4 . 0 } \\ { 0 . 2 } \end{array} \right] , \overline { { { P } } } _ { 0 } = \left[ \begin{array} { c c } { 1 0 0 0 } & { 0 } \\ { 0 } & { 1 0 0 } \end{array} \right] , \mathrm { a n d } \delta \overline { { \mathbf { X } } } _ { 0 } = \left[ \begin{array} { c } { 0 } \\ { 0 } \end{array} \right] .
$$

The computed observations were calculated with the exact values of $k _ { 1 } , k _ { 2 }$ , $m$ , and $h$ from Eq. (4.8.6); $\mathbf { X } _ { 0 } ^ { * }$ was used for the values of $x _ { 0 } ^ { * }$ and $v _ { 0 } ^ { * }$ .

The least squares solution for $\delta { \bf X } _ { 0 }$ is given by (assuming that $W _ { i } ^ { - 1 } = R _ { i } = I )$

$$
\delta { \hat { \mathbf { X } } } _ { 0 } = \left( \sum _ { i = 0 } ^ { 1 0 } H _ { i } ^ { T } H _ { i } + { \overline { { P } } } _ { 0 } ^ { - 1 } \right) ^ { - 1 } \left( \sum _ { i = 0 } ^ { 1 0 } H _ { i } ^ { T } y _ { i } + { \overline { { P } } } _ { 0 } ^ { - 1 } \delta { \overline { { \mathbf { X } } } } _ { 0 } \right)
$$

and the best estimate of the initial state is

$$
\hat { \mathbf { X } } _ { 0 } = \mathbf { X } _ { 0 } ^ { * } + \delta \hat { \mathbf { X } } _ { 0 } .
$$

After each iteration shift the a priori state deviation vector so that

$$
( \delta { \bar { \mathbf { X } } } _ { 0 } ) _ { n } = ( \delta { \bar { \mathbf { X } } } _ { 0 } ) _ { n - 1 } - ( \delta { \hat { \mathbf { X } } } _ { 0 } ) _ { n - 1 }
$$

following Eq. (4.6.4) and Fig. 4.6.1.

After four iterations the estimate for the state at $t = 0$ is

$$
\left[ \hat { \bf X } _ { 0 } \right] = \left[ \begin{array} { l } { \hat { x } _ { 0 } } \\ { \hat { v } _ { 0 } } \end{array} \right] = \left[ \begin{array} { l } { 3 . 0 0 0 1 9 \mathrm { m } } \\ { 1 . 1 8 1 8 1 \times 1 0 ^ { - 3 } \mathrm { m } / \mathrm { s } } \end{array} \right] .
$$

The computed standard deviations and correlation coefficient are

$$
\sigma _ { x _ { 0 } } = 0 . 4 1 1 \mathrm { ~ m } , \sigma _ { v _ { 0 } } = 0 . 7 6 5 \mathrm { ~ m } / \mathrm { s } , \mathrm { a n d } \rho _ { x _ { 0 } v _ { 0 } } = 0 . 0 4 0 6 . \mathrm { ~ }
$$

The mean of the residuals is $\rho _ { \mathrm { m e a n } } = - 4 . 3 0 \times 1 0 ^ { - 5 } \mathrm { m }$ , $\dot { \rho } _ { \mathrm { m e a n } } = - 1 . 7 6 \times 1 0 ^ { - 6 }$ $\mathrm { m } / \mathrm { s }$ . The RMS of residuals is $\rho _ { R M S } = 1 . 1 6 \times 1 0 ^ { - 4 } \mathrm { m } , \dot { \rho } _ { \mathrm { R M S } } = 4 . 6 6 \times 1 0 ^ { - 4 } \mathrm { m } / \mathrm { s }$ .

# 4.9 STATE NOISE COMPENSATION ALGORITHM

In addition to the effects of the nonlinearities, the effects of errors in the dynamical model can lead to divergence in the estimate. See, for example, the discussion in Schlee et al., (1967) . As pointed out previously, for a sufficiently large number of observations the elements of the covariance matrix $P _ { k }$ will asymptotically approach zero and the estimation algorithm will be insensitive to any further observations. This condition can lead to filter divergence. One approach to preventing this divergence is to recognize that the linearized equations for propagating the estimate of the state are in error and to compensate for this by assuming that the error in the linearized dynamics can be approximated by process noise.

The state dynamics of a linear system under the influence of process noise are described by

$$
{ \dot { \mathbf { x } } } ( t ) = A ( t ) \mathbf { x } ( t ) + B ( t ) \mathbf { u } ( t )
$$

where $A ( t )$ and $B ( t )$ are known functions of time. The vector ${ \bf \delta u } ( t )$ is dimension $m \times 1$ , and $B ( t )$ is an $n \times m$ matrix. The functional form of ${ \bf \delta u } ( t )$ can include a number of processes, including constant, piecewise constant, correlated, or white noise. In the following discussion, the function ${ \bf \delta u } ( t )$ (called state or process noise) is assumed to be a white noise process with

$$
\begin{array} { c } { E [ { \mathbf { u } ( t ) } ] = 0 } \\ { E [ { \mathbf { u } ( t ) \mathbf { u } ^ { T } ( \tau ) } ] = Q ( t ) \delta ( t - \tau ) } \end{array}
$$

where $\delta ( t - \tau )$ is the Dirac Delta, and $Q$ is called the process noise covariance matrix.

The algorithm that results from the assumption that ${ \bf \delta u } ( t )$ is white noise with known covariance is known as State Noise Compensation (SNC). The use of more sophisticated models such as the process to compensate for state and/or measurement model errors generally is referred to as Dynamic Model Compensation (DMC). In the case of DMC, process noise parameters are often included in the state vector to be estimated. Appendix F provides more details on SNC and DMC.

The solution of Eq. (4.9.1) can be obtained by the method of variation of parameters. The homogeneous equation is given by

$$
\dot { \mathbf { x } } ( t ) = A ( t ) \mathbf { x } ( t )
$$

which, as previously noted, has a solution of the form

$$
\begin{array} { r } { { \bf x } ( t ) = \Phi ( t , t _ { 0 } ) { \bf C } _ { 0 } . } \end{array}
$$

The method of variation of parameters selects $\mathbf { C } _ { 0 }$ as a function of time so that

$$
\mathbf { x } ( t ) = \Phi ( t , t _ { 0 } ) \mathbf { C } ( t ) .
$$

It follows then that

$$
\dot { { \mathbf x } } ( t ) = \dot { \Phi } ( t , t _ { 0 } ) { \mathbf C } ( t ) + \Phi ( t , t _ { 0 } ) \dot { { \mathbf C } } ( t ) .
$$

Substituting Eq. (4.9.6) into Eq. (4.9.1) yields

$$
{ \dot { \Phi } } ( t , t _ { 0 } ) \mathbf { C } ( t ) + \Phi ( t , t _ { 0 } ) { \dot { \mathbf { C } } } ( t ) = A ( t ) \mathbf { x } ( t ) + B ( t ) \mathbf { u } ( t ) .
$$

Recall that

$$
\dot { \Phi } ( t , t _ { 0 } ) = A ( t ) \Phi ( t , t _ { 0 } ) .
$$

Substituting Eq. (4.9.8) into Eq. (4.9.7) and using Eq. (4.9.5) reduces Eq. (4.9.7) to

$$
\Phi ( t , t _ { 0 } ) \dot { \mathbf { C } } ( t ) = B ( t ) \mathbf { u } ( t ) .
$$

Hence,

$$
\dot { { \bf C } } ( t ) = \Phi ^ { - 1 } ( t , t _ { 0 } ) B ( t ) { \bf u } ( t ) .
$$

Integrating Eq. (4.9.10) yields

$$
\mathbf { C } ( t ) = \mathbf { C } _ { 0 } + \int _ { t _ { 0 } } ^ { t } \Phi ^ { - 1 } ( \tau , t _ { 0 } ) B ( \tau ) \mathbf { u } ( \tau ) d \tau .
$$

Substituting Eq. (4.9.11) into Eq. (4.9.5) results in

$$
\mathbf { x } ( t ) = \Phi ( t , t _ { 0 } ) \mathbf { C } _ { 0 } + \int _ { t _ { 0 } } ^ { t } \Phi ( t , t _ { 0 } ) \Phi ^ { - 1 } ( \tau , t _ { 0 } ) B ( \tau ) \mathbf { u } ( \tau ) d \tau .
$$

Using the properties of the transition matrix, we may write

$$
\Phi ( t , t _ { 0 } ) \Phi ^ { - 1 } ( \tau , t _ { 0 } ) = \Phi ( t , t _ { 0 } ) \Phi ( t _ { 0 } , \tau ) = \Phi ( t , \tau ) .
$$

At $t = t _ { 0 }$ , $\mathbf { x } ( t _ { 0 } ) = \mathbf { x } _ { 0 }$ ; hence, Eq. (4.9.12) can be used to determine that ${ \bf C } _ { 0 } = { }$ $\mathbf { x } _ { \mathrm { 0 } }$ . With these results, Eq. (4.9.12) can be written as

$$
{ \bf x } ( t ) = \Phi ( t , t _ { 0 } ) { \bf x } _ { 0 } + \int _ { t _ { 0 } } ^ { t } \Phi ( t , \tau ) B ( \tau ) { \bf u } ( \tau ) d \tau .
$$

Equation (4.9.14) is the general solution for the inhomogeneous Eq. (4.9.1) and indicates how the true state propagates under the influence of process noise.

The equations for propagating the state estimate $\hat { \mathbf { x } } ( t _ { k - 1 } )$ to the next observation time, $t _ { k }$ , are obtained by recalling that

$$
\begin{array} { r } { \overline { { \mathbf { x } } } ( t ) = E [ \mathbf { x } ( t ) | \mathbf { y } _ { k - 1 } ] \quad \mathrm { f o r } \quad t \geq t _ { k - 1 } ; } \end{array}
$$

that is, the expected value of ${ \bf x } ( t )$ given observations through $t _ { k - 1 }$ . Also, because we have observations through $t _ { k - 1 }$

$$
\overline { { \mathbf { x } } } ( t _ { k - 1 } ) = \hat { \mathbf { x } } ( t _ { k - 1 } ) .
$$

Differentiating Eq. (4.9.15) and using Eq. (4.9.1) gives

$$
\begin{array} { r l } & { \dot { \overline { { \mathbf { x } } } } ( t ) = E \left[ \dot { \mathbf { x } } ( t ) | \mathbf { y } _ { k - 1 } \right] } \\ & { \qquad = E \left[ \left\{ A ( t ) \mathbf { x } ( t ) + B ( t ) \mathbf { u } ( t ) \right\} | \mathbf { y } _ { k - 1 } \right] } \\ & { \qquad = A ( t ) E \left[ \mathbf { x } ( t ) | \mathbf { y } _ { k - 1 } \right] . } \end{array}
$$

Since $E [ \mathbf { u } ( t ) ] = 0$ , it follows then that

$$
\dot { \mathbf { x } } ( t ) = \boldsymbol { A } ( t ) \overline { { \mathbf { x } } } ( t )
$$

with initial conditions $\overline { { \mathbf { x } } } ( t _ { k - 1 } ) = \hat { \mathbf { x } } ( t _ { k - 1 } )$ . In Eq. (4.9.17), the assumption has been made that the state noise ${ \bf \delta u } ( t )$ has zero mean and is independent of the observations,

$$
E [ { \bf u } ( t ) | { \bf y } _ { k - 1 } ] = E [ { \bf u } ( t ) ] = 0 .
$$

Hence, if the mean of the process noise is zero, $\begin{array} { r } { ( E [ \mathbf { u } ( t ) ] = 0 , } \end{array}$ ), then the equation for propagating the state estimate is the same as without process noise,

$$
\overline { { \mathbf { x } } } ( t ) = \Phi ( t , t _ { k - 1 } ) \hat { \mathbf { x } } _ { k - 1 } .
$$

One could derive a solution for the case where the mean is nonzero. In the case where $E [ \mathbf { u } ( t ) ] = \overline { { \mathbf { u } } }$ , the solution would be obtained by applying the expectation operator to Eq. (4.9.14) to yield

$$
\overline { { { \bf x } } } ( t ) = \boldsymbol \Phi ( t , t _ { k - 1 } ) \hat { \bf x } _ { k - 1 } + \Gamma ( t _ { k } , t _ { k - 1 } ) \overline { { { \bf u } } }
$$

where $\Gamma ( t _ { k } , t _ { k - 1 } )$ is defined by Eq. (4.9.47).

The equation for propagation of the estimation error covariance matrix is obtained by using the definition for $\overline { { P } } ( t )$ , given by

$$
\overline { { P } } ( t ) = E [ ( \bar { \mathbf { x } } ( t ) - \mathbf { x } ( t ) ) ( \overline { { \mathbf { x } } } ( t ) - \mathbf { x } ( t ) ) ^ { T } | \mathbf { y } _ { k - 1 } ] \ t \geq t _ { k - 1 } .
$$

Let

$$
\Delta \mathbf { x } ( t ) \equiv \overline { { \mathbf { x } } } ( t ) - \mathbf { x } ( t ) .
$$

Then

$$
\overline { { P } } ( t ) = E [ \Delta \mathbf x \Delta \mathbf x ^ { T } | \mathbf y _ { k - 1 } ]
$$

and differentiating $\overline { { P } } ( t )$ yields

$$
\begin{array} { l } { \displaystyle { \dot { \overline { { P } } } ( t ) = E \left[ \frac { d } { d t } \Delta \mathbf { x } \Delta \mathbf { x } ^ { T } | \mathbf { y } _ { k - 1 } \right] } } \\ { \displaystyle { ~ = E \left[ \Delta \dot { \mathbf { x } } \Delta \mathbf { x } ^ { T } + \Delta \mathbf { x } \Delta \dot { \mathbf { x } } ^ { T } | \mathbf { y } _ { k - 1 } \right] . } } \end{array}
$$

From Eqs. (4.9.1) and (4.9.17)

$$
\begin{array} { l } { \Delta \dot { \mathbf { x } } ( t ) = \dot { \bar { \mathbf { x } } } ( t ) - \dot { \mathbf { x } } ( t ) } \\ { = A ( t ) \bar { \mathbf { x } } ( t ) - A ( t ) \mathbf { x } ( t ) - B ( t ) \mathbf { u } ( t ) . } \end{array}
$$

Hence,

$$
\Delta \dot { \mathbf { x } } ( t ) = A ( t ) \Delta \mathbf { x } ( t ) - B ( t ) \mathbf { u } ( t ) .
$$

Substituting Eq. (4.9.23) into Eq. (4.9.22) yields

$$
\begin{array} { r l } & { \dot { \overline { { P } } } ( t ) = E \left[ \left\{ ( A ( t ) \Delta \mathbf { x } - B ( t ) \mathbf { u } ( t ) ) \Delta \mathbf { x } ^ { T } + \Delta \mathbf { x } ( A ( t ) \Delta \mathbf { x } - B ( t ) \mathbf { u } ( t ) ) ^ { T } \right\} | \mathbf { y } _ { k - 1 } \right] } \\ & { \quad \quad = A ( t ) E \left[ \Delta \mathbf { x } \Delta \mathbf { x } ^ { T } | \mathbf { y } _ { k - 1 } \right] - B ( t ) E \left[ \mathbf { u } ( t ) \Delta \mathbf { x } ^ { T } | \mathbf { y } _ { k - 1 } \right] } \\ & { \quad \quad \quad + E \left[ \Delta \mathbf { x } \Delta \mathbf { x } ^ { T } | \mathbf { y } _ { k - 1 } \right] A ^ { T } ( t ) - E \left[ \Delta \mathbf { x } \mathbf { u } ^ { T } ( t ) | \mathbf { y } _ { k - 1 } \right] B ^ { T } ( t ) } \end{array}
$$

and using Eq. (4.9.21)

$$
\begin{array} { r l } & { \dot { \overline { { P } } } ( t ) = A ( t ) \overline { { P } } ( t ) + \overline { { P } } ( t ) A ^ { T } ( t ) - B ( t ) E \left[ \mathbf { u } ( t ) \Delta \mathbf { x } ^ { T } | \mathbf { y } _ { k - 1 } \right] } \\ & { ~ - E \left[ \Delta \mathbf { x } \mathbf { u } ^ { T } ( t ) | \mathbf { y } _ { k - 1 } \right] B ^ { T } ( t ) . } \end{array}
$$

The solution for $\Delta { \bf x } ( t )$ now is needed to substitute into Eq. (4.9.24). Note that the solution for Eq. (4.9.23) is identical in form to the solution of Eq. (4.9.1) given by Eq. (4.9.14). Substituting Eq. (4.9.14) with appropriate subscripts into the last term of Eq. (4.9.24) yields

$$
\begin{array} { r l r } {  { E [ \Delta \mathbf { x } ( t ) \mathbf { u } ^ { T } ( t ) | \mathbf { y } _ { k - 1 } ] = E [ \Phi ( t , t _ { k - 1 } ) \Delta \mathbf { x } _ { k - 1 } \mathbf { u } ^ { T } ( t ) | \mathbf { y } _ { k - 1 } ] } } & { ( 4 . } & \\ & { } & { - E [ \int _ { t _ { k - 1 } } ^ { t } \Phi ( t , \tau ) B ( \tau ) \mathbf { u } ( \tau ) \mathbf { u } ^ { T } ( t ) d \tau | \mathbf { y } _ { k - 1 } ] } \end{array}
$$

where $t \geq t _ { k - 1 }$ . However,

$$
E \left[ \Delta \mathbf { x } _ { k - 1 } \mathbf { u } ^ { T } ( t ) | \mathbf { y } _ { k - 1 } \right] = 0
$$

since the forcing function ${ \bf \delta u } ( t )$ cannot influe nce the state at a time $t _ { k - 1 }$ for $t \geq$

$t _ { k - 1 }$ . Hence,

$$
E \left[ \Delta \mathbf { x } ( t ) \mathbf { u } ^ { T } ( t ) | \mathbf { y } _ { k - 1 } \right] = - \int _ { t _ { k - 1 } } ^ { t } \Phi ( t , \tau ) B ( \tau ) E \left[ \mathbf { u } ( \tau ) \mathbf { u } ^ { T } ( t ) d \tau | \mathbf { y } _ { k - 1 } \right] .
$$

From Eq. (4.9.2)

$$
E \left[ \mathbf { u } ( \tau ) \mathbf { u } ^ { T } ( t ) \right] = Q ( t ) \delta ( t - \tau )
$$

where $\delta ( t - \tau )$ is the Dirac delta function, which is defined to be zero everywhere except at $\tau = t$ , where it is infinite in such a way that the integral of $\delta ( t - \tau )$ across the singularity is unity; the Dirac delta function is defined by

$$
\delta ( t ) = \operatorname* { l i m } _ { \epsilon \to 0 } \delta _ { \epsilon } ( t )
$$

where

$$
\delta _ { \epsilon } ( t ) = \left\{ \begin{array} { l } { { 0 \left| t \right| > \frac { \epsilon } { 2 } } } \\ { { \frac { 1 } { \epsilon } \left| t \right| < \frac { \epsilon } { 2 } } } \end{array} . \right.
$$

![](images/c0656d5fbbc52304c452e3c22d7a859b207d7912805973d710659946a122f91f.jpg)

This definit ion implies that

$$
\int _ { t _ { 1 } } ^ { t _ { 2 } } \delta ( t - \tau ) d \tau = \int _ { t - \epsilon / 2 } ^ { t + \epsilon / 2 } \delta ( t - \tau ) d \tau = 1 .
$$

Substituting Eq. (4.9.27) into Eq. (4.9.26) gives

$$
E \left[ \Delta \mathbf { x u } ^ { T } ( t ) | \mathbf { y } _ { k - 1 } \right] = - \int _ { t _ { k - 1 } } ^ { t } \Phi ( t , \tau ) B ( \tau ) Q ( t ) \delta ( t - \tau ) d \tau .
$$

Now

$$
\int _ { - \infty } ^ { \infty } \delta ( t - \tau ) d \tau = \operatorname* { l i m } _ { \epsilon \to 0 } \left[ \int _ { - \infty } ^ { t - \epsilon / 2 } 0 d \tau + \int _ { t - \epsilon / 2 } ^ { t + \epsilon / 2 } \frac 1 \epsilon d \tau + \int _ { t + \epsilon / 2 } ^ { \infty } 0 d \tau \right] .
$$

Hence, Eq. (4.9.28) becomes

$$
E \left[ \Delta \mathbf { x } ( t ) \mathbf { u } ^ { T } ( t ) | \mathbf { y } _ { k - 1 } \right] =
$$

$$
- \operatorname* { l i m } _ { \epsilon \to 0 } \left[ \int _ { t _ { k - 1 } } ^ { t - \epsilon / 2 } \ d 0 \ d d \tau + \int _ { t - \epsilon / 2 } ^ { t } \Phi ( t , \tau ) B ( \tau ) Q ( t ) ( \frac { 1 } { \epsilon } ) \ d { d \tau } \right] .
$$

Since $\epsilon$ is small, $\Phi ( t , \tau )$ and $B ( \tau )$ can be expanded in a Taylor series about $\Phi ( t , t )$ and $B ( t )$ , respectively. To this end, let

$$
\Phi ( t , \tau ) = \Phi ( t , t ) - \dot { \Phi } ( t , t ) ( t - \tau ) + O ( t - \tau ) ^ { 2 } .
$$

The second term of this equation is negative, since $t \geq \tau$ . Using the fact that $\Phi ( t , t ) = I$ and ${ \dot { \Phi } } ( t , t ) = { \bar { A } } ( t ) \Phi ( t , t )$ , we can write

$$
\Phi ( t , \tau ) = I - A ( t ) ( t - \tau ) + O ( t - \tau ) ^ { 2 } .
$$

Similarly we can expand $B ( \tau )$ :

$$
B ( \tau ) = B ( t ) - \frac { d } { d t } B ( t ) ( t - \tau ) + O ( t - \tau ) ^ { 2 } .
$$

Substituting Eqs. (4.9.31) and (4.9.32) into Eq. (4.9.29) yields

$$
\begin{array} { l } { { E \left[ \Delta { \mathbf { x u } } ^ { T } ( t ) | { \mathbf { y } } _ { k - 1 } \right] = - \displaystyle \operatorname* { l i m } _ { \epsilon \to 0 } \frac { 1 } { \epsilon } \int _ { t - \epsilon / 2 } ^ { t } \Bigg [ [ I - A ( t ) ( t - \tau ) ] [ B ( t ) Q ( t ) } } \\ { { \begin{array} { l } { { - \frac { d } { d t } B ( t ) Q ( t ) ( t - \tau ) ] + O ( t - \tau ) ^ { 2 } \Bigg ] d \tau } } \\ { { - \frac { \operatorname* { l i m } } { \epsilon \to 0 } \int _ { t - \epsilon / 2 } ^ { t } \left[ B ( t ) Q ( t ) - \frac { d } { d t } B ( t ) Q ( t ) ( t - \tau ) \right. } } \\ { { \left. - A ( t ) B ( t ) Q ( t ) ( t - \tau ) \right. } } \\ { { \left. + A ( t ) \frac { d } { d t } B ( t ) Q ( t ) ( t - \tau ) ^ { 2 } \right. } } \\ { { \left. + O ( t - \tau ) ^ { 2 } \right] \frac { d \tau } { \epsilon } . } } \end{array} } } \end{array}
$$

Ignoring higher order terms $( O ( t - \tau ) ^ { 2 } )$ in Eq. (4.9.33) results in

$$
\begin{array} { l } { { \displaystyle E [ \Delta { \bf x } ( t ) { \bf u } ^ { T } ( t ) | { \bf y } _ { k - 1 } ] = - \operatorname* { l i m } _ { \epsilon  0 } \frac { 1 } { \epsilon } \int _ { t - \epsilon / 2 } ^ { t } \Bigg \{ B ( t ) Q ( t ) - [ A ( t ) B ( t ) Q ( t )  } } \\ { { \displaystyle  + \frac { d } { d t }  B ( t ) Q ( t ) ] ( t - \tau ) \} d \tau } . } \end{array}
$$

Defining $\begin{array} { r } { K ( t ) = A ( t ) B ( t ) Q ( t ) + \frac { d } { d t } B ( t ) Q ( t ) } \end{array}$ and carrying out the integration

$$
\begin{array} { l } { { E [ \Delta { \bf x u } ^ { T } ( t ) | { \bf y } _ { k - 1 } ] = - \operatorname* { l i m } _ { \epsilon  0 } \frac 1 { \epsilon } [ B ( t ) Q ( t ) \tau - K ( t ) ( t \tau - \frac { \tau ^ { 2 } } { 2 } ) ] _ { t - \frac { \epsilon } { 2 } } ^ { t } } } \\ { { \mathrm { ~ } = - \operatorname* { l i m } _ { \epsilon  0 } \frac 1 { \epsilon } [ B ( t ) Q ( t ) \frac { \epsilon } { 2 } - K ( t ) ( \frac { \epsilon ^ { 2 } } { 8 } ) ] } } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle = - \operatorname* { l i m } _ { \epsilon  0 } [ \frac { B ( t ) Q ( t ) } 2 - \frac { K ( t ) } 8 \epsilon ] } } \\ { { \mathrm { } } } \\ { { \displaystyle = - \frac { B ( t ) Q ( t ) } 2 . } } \end{array}
$$

Substituting (4.9.34) and its transpose into (4.9.24) leads to

$$
\dot { \overline { { P } } } ( t ) = A ( t ) \overline { { P } } ( t ) + \overline { { P } } ( t ) A ^ { T } ( t ) + B ( t ) Q ( t ) B ^ { T } ( t ) .
$$

Equation (4.9.35) is an $n \times n$ matrix differential equation whose solution may be obtained by integrating with the initial conditions $\overline { { P } } ( t _ { k } ) = P _ { k }$ ; that is, the measurement update of the estimation error covariance matrix at $t _ { k }$ .

Equation (4.9.35) also can be expressed in integral form by using the method of variation of parameters. The homogeneous differential equation is given by

$$
\dot { \overline { { { P } } } } ( t ) = A ( t ) \overline { { { P } } } ( t ) + \overline { { { P } } } ( t ) A ^ { T } ( t ) ,
$$

which has the solution

$$
\overline { { P } } ( t ) = \Phi ( t , t _ { 0 } ) P _ { 0 } \Phi ^ { T } ( t , t _ { 0 } ) ,
$$

where for convenience, $t _ { k - 1 }$ has been replaced by $t _ { 0 }$ . Letting $P _ { 0 }$ become a function of time, Eq. (4.9.37) becomes

$$
\begin{array} { r l } & { \dot { \overline { { P } } } ( t ) = \dot { \Phi } ( t , t _ { 0 } ) P _ { 0 } { \Phi } ^ { T } ( t , t _ { 0 } ) } \\ & { \qquad + { \Phi } ( t , t _ { 0 } ) P _ { 0 } \dot { \Phi } ^ { T } ( t , t _ { 0 } ) + { \Phi } ( t , t _ { 0 } ) \dot { P } _ { 0 } { \Phi } ^ { T } ( t , t _ { 0 } ) . } \end{array}
$$

Equating Eqs. (4.9.35) and (4.9.38)

$$
\begin{array} { r l } & { A ( t ) \overline { { P } } ( t ) + \overline { { P } } ( t ) A ^ { T } ( t ) + B ( t ) Q ( t ) B ^ { T } ( t ) = \dot { \Phi } ( t , t _ { 0 } ) P _ { 0 } { \Phi } ^ { T } ( t , t _ { 0 } ) } \\ & { \qquad + \ \Phi ( t , t _ { 0 } ) P _ { 0 } \dot { \Phi } ^ { T } ( t , t _ { 0 } ) + \Phi ( t , t _ { 0 } ) \dot { P } _ { 0 } { \Phi } ^ { T } ( t , t _ { 0 } ) . \qquad ( } \end{array}
$$

However, from Eqs. (4.9.36) and (4.9.37)

$$
\begin{array} { r } { A ( t ) \overline { { P } } ( t ) + \overline { { P } } ( t ) A ^ { T } ( t ) = \dot { \Phi } ( t , t _ { 0 } ) P _ { 0 } { \Phi } ^ { T } ( t , t _ { 0 } ) } \\ { + \Phi ( t , t _ { 0 } ) P _ { 0 } \dot { \Phi } ^ { T } ( t , t _ { 0 } ) . } \end{array}
$$

Using Eq. (4.9.40), Eq. (4.9.39) reduces to

$$
\Phi ( t , t _ { 0 } ) \dot { P } _ { 0 } \Phi ^ { T } ( t , t _ { 0 } ) = B ( t ) Q ( t ) B ^ { T } ( t ) ,
$$

or

$$
\dot { P } _ { o } = \Phi ^ { - 1 } ( t , t _ { 0 } ) B ( t ) Q ( t ) B ^ { T } ( t ) \Phi ^ { - T } ( t , t _ { 0 } ) .
$$

Integrating Eq. (4.9.41) results in

$$
P _ { 0 } ( t ) - P _ { 0 } = \int _ { t _ { 0 } } ^ { t } \Phi ( t _ { 0 } , \tau ) B ( \tau ) Q ( \tau ) B ^ { T } ( \tau ) \Phi ^ { T } ( t _ { 0 } , \tau ) d \tau .
$$

Substituting Eq. (4.9.42) into (4.9.37)

$$
\begin{array} { r l r } {  { \overline { { P } } ( t ) = \Phi ( t , t _ { 0 } ) [ P _ { 0 } + \int _ { t _ { 0 } } ^ { t } \Phi ( t _ { 0 } \tau ) B ( \tau ) Q ( \tau ) B ^ { T } ( \tau ) \Phi ^ { T } ( t _ { 0 } , \tau ) d \tau ] \Phi ^ { T } ( t , t _ { 0 } ) } } \\ & { } & { \qquad = \Phi ( t , t _ { 0 } ) P _ { 0 } \Phi ^ { T } ( t , t _ { 0 } ) + \int _ { t _ { 0 } } ^ { t } \Phi ( t , t _ { 0 } ) \Phi ( t _ { 0 } , \tau ) B ( \tau ) Q ( \tau ) B ^ { T } ( \tau ) } \\ & { } & { \qquad \times \Phi ^ { T } ( t _ { 0 } , \tau ) \Phi ^ { T } ( t , t _ { 0 } ) d \tau . } \end{array}
$$

If we use

$$
\Phi ( t , t _ { 0 } ) \Phi ( t _ { 0 } \tau ) = \Phi ( t , \tau ) ,
$$

and

$$
\Phi ^ { T } ( t _ { 0 } , \tau ) \Phi ^ { T } ( t , t _ { 0 } ) = [ \Phi ( t , t _ { 0 } ) \Phi ( t _ { 0 } , \tau ) ] ^ { T } = \Phi ^ { T } ( t , \tau ) ,
$$

then after letting $t _ { 0 } = t _ { k - 1 }$ , Eq. (4.9.43) becomes

$$
\begin{array} { l } { \displaystyle \overline { { P } } ( t ) = \Phi ( t , t _ { k - 1 } ) P _ { k - 1 } \Phi ^ { T } ( t , t _ { k - 1 } ) } \\ { \displaystyle \qquad + \int _ { t _ { k - 1 } } ^ { t } \Phi ( t , \tau ) B ( \tau ) Q ( \tau ) B ^ { T } ( \tau ) \Phi ^ { T } ( t , \tau ) d \tau . } \end{array}
$$

Equations (4.9.19) and (4.9.44) are the equations for propagating the estimate of the state and the covariance for a continuous system. Since the orbit determination problem generally consists of a continuous system (the trajectory) subjected to discrete observations, it is convenient to use Eq. (4.9.19) to propagate the state estimate and to discretize Eq. (4.9.44). This can be accomplished by replacing $t$ with $t _ { k + 1 }$ and assuming that $\mathbf { u } ( \tau )$ is a white random sequence rather than a process. Thus, as indicated in Fig. 4.9.1, ${ \bf \delta u } ( t )$ is considered to be a piecewise constant function with covariance

$$
E [ \mathbf { u } ( t _ { i } ) \mathbf { u } ^ { T } ( t _ { j } ) ] = Q _ { i } \delta _ { i j } \delta _ { i j } = \left\{ { 1 i = j \atop 0 i \neq j } \right.
$$

where the Dirac delta function has been replaced by its analog for the discrete case, the Kroneker delta function. In the discrete case, Eq. (4.9.14) becomes

$$
\mathbf { x } ( t _ { k + 1 } ) \equiv \mathbf { x } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) \mathbf { x } _ { k } \ + \Gamma ( t _ { k + 1 } , t _ { k } ) \mathbf { u } _ { k }
$$

where

$$
\Gamma ( t _ { k + 1 } , t _ { k } ) = \int _ { t _ { k } } ^ { t _ { k + 1 } } \Phi ( t _ { k + 1 } , \tau ) B ( \tau ) d \tau .
$$

![](images/4dc9b7c24b54776aee43014d19a293d6d283bb12da83d90b52f1355bc73fa07b.jpg)  
Figure 4.9.1: A white random sequence.

$\Gamma ( t _ { k + 1 } , t _ { k } )$ is referred to as the process noise transition matrix, and Eq. (4.9.47) is an $n \times m$ quadrature since $\Phi ( t _ { k + 1 } , \tau )$ and $B ( \tau )$ are known functions. Using the definit ion of the estimation error covariance matrix

$$
\overline { { P } } _ { k + 1 } = E [ ( \overline { { \mathbf { x } } } _ { k + 1 } - { \mathbf { x } } _ { k + 1 } ) ( \overline { { \mathbf { x } } } _ { k + 1 } - { \mathbf { x } } _ { k + 1 } ) ^ { T } ]
$$

and substituting Eqs. (4.9.46) and (4.9.19) into (4.9.48) leads to

$$
\begin{array} { r } { \overline { { P } } _ { k + 1 } = E \Bigg \{ \left[ \Phi ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { x } } _ { k } - \Phi ( t _ { k + 1 } , t _ { k } ) \mathbf { x } _ { k } - \Gamma ( t _ { k + 1 } , t _ { k } ) \mathbf { u } _ { k } \right] } \\ { \times \left[ \Phi ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { x } } _ { k } - \Phi ( t _ { k + 1 } , t _ { k } ) \mathbf { x } _ { k } - \Gamma ( t _ { k + 1 } , t _ { k } ) \mathbf { u } _ { k } \right] ^ { T } \Bigg \} . } \end{array}
$$

Note that $E [ ( \widehat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ) \mathbf { u } _ { k } ^ { T } ] = 0$ ; that is, $\mathbf { u } _ { k }$ cannot affect the estimation error at $t _ { k }$ since a finite time must evolve for $\mathbf { u } _ { k }$ to affect the state. Finally, carrying out the expectation operation in Eq. (4.9.49) yields

$$
\overline { { P } } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) P _ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) + \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) .
$$

The estimation error covariance matrix $\overline { { P } } _ { k + 1 }$ can be obtained by integrating the differential equation for $\dot { \overline { P } }$ given by Eq. (4.9.35), or $\overline { { P } } _ { k + 1 }$ may be obtained by using the state and process noise transition matrices as indicated in Eq. (4.9.50). A comparison of Eq. (4.9.35) and Eq. (4.9.50) indicates the following:

1. Since $P ( t )$ is symmetric, only $n ( n + 1 ) / 2$ of the $n \times n$ system of equations represented by Eq. (4.9.35) must be integrated. However, the $n ( n + 1 ) / 2$ equations are coupled and must be integrated as a single first-order system of dimension $n ( n + 1 ) / 2$ .

2. The $n \times n$ system represented by Eq. (4.9.50) can be separated into an $n \times n$ system of differential equations for $\Phi$ and an $n \times m$ quadrature for

Γ. Furthermore, the $n \times n$ system of equations represented by the solution for $\Phi ( t _ { k + 1 } , t _ { k } )$ can be integrated as a sequence of $n \times 1$ column vectors.

The comparison between the two methods indicates that integration of fewer equations is required to obtain the solution for $\overline { { P } } ( t )$ with Eq. (4.9.35). However, the integration of these equations may be more difficult than the integration associated with the larger system represented by Eq. (4.9.50) since they are coupled.

The equations for determining $\hat { \bf x }$ using the sequential processing algorithm are unchanged whenever a zero-mean process noise is included. However, as has been shown, the equations that propagate the estimation error covariance matrix do change; that is, the first of Eq. (4.7.31) is replaced by Eq. (4.9.50). Generally, the batch processing algorithm is not used with process noise because mapping of the process noise effects from the observation times to the epoch time is cumbersome. It further results in a normal matrix with an observation weighting matrix that will be nondiagonal and whose dimension is equal to $m \times m$ , where $m$ is the total number of observations. Computation of the inverse of the normal matrix will be so cumbersome that the normal equation solution involving process noise in the data accumulation interval is impractical. For example, a one-day tracking period for the TOPEX/Poseidon satellite by the French tracking system, DORIS, typically yields 5000–7000 doppler observations.

The advantage of using the process noise compensated sequential estimation algorithm lies in the fact that the asymptotic value of $\overline { { P } } ( t )$ will approach a nonzero value determined by the magnitude of $Q ( t )$ . That is, for certain values of $Q ( t )$ , the increase in the state error covariance matrix $\overline { { P } } ( t )$ during the interval between observations will balance the decrease in the covariance matrix that occurs at the observation point. In this situation, the estimation procedure will always be sensitive to new observations.

The question of how to choose the process noise covariance matrix, $Q ( t )$ , is complex. In practice, it is often chosen as a simple diagonal matrix and its elements are determined by trial and error. Although this method can be effective for a particular estimation scenario, such a process noise matrix is not generally applicable to other scenarios. The dynamic evolution of the true states of parameters estimated in a filter typically is affected by stochastic processes that are not modeled in the filte r’s deterministic dynamic model. The process noise model is a characterization of these stochastic processes, and the process noise covariance matrix should be determined by this process noise model. Development of the process noise model will not be presented in depth here; however, extensive discussions are given by Cruickshank (1998), Ingram (1970), and Lichten (1990).

The Gauss-Markov process is used as a process noise model and will be introduced here. It is computationally well suited for describing unmodeled forces since it obeys Gaussian probability laws and is exponentially correlated in time.

# 4.9.1 THE GAUSS-MARKOV PROCESS

A first-or der Gauss-Markov process is often used for dynamic model compensation in orbit determination problems to account for unmodeled or inaccurately modeled accelerations acting on a spacecraft. A Gauss-Markov process is one that obeys a Gaussian probability law and displays the Markov property. The Markov property means that the probability density function at $t _ { n }$ given its past history at $t _ { n - 1 }$ , $t _ { n - 2 } , \ldots$ is equal to its probability density function at $t _ { n }$ given its value at $t _ { n - 1 }$ .

A Gauss-Markov process obeys a differential equation (often referred to as a Langevin equation) of the form

$$
\dot { \eta } ( t ) = - \beta \eta ( t ) + u ( t )
$$

where $u ( t )$ is white Gaussian noise with

$$
\begin{array} { c } { { E ( u ) = 0 } } \\ { { E \left[ u ( t ) u ( \tau ) \right] = \sigma ^ { 2 } \delta ( t - \tau ) } } \end{array}
$$

and

$$
\beta = \frac { 1 } { \tau } ,
$$

where $\tau$ is the time constant or correlation time (not the same as $\tau$ in Eq. (4.9.52)).

Equation (4.9.51) can be solved by the method of variation of parameters to yield

$$
\eta ( t ) = \eta ( t _ { 0 } ) e ^ { - \beta ( t - t _ { 0 } ) } + \int _ { t _ { 0 } } ^ { t } e ^ { - \beta ( t - \tau ) } u ( \tau ) d \tau .
$$

Hence, $\eta ( t )$ consists of a deterministic part and a random part. The autocorrelation function is (Maybeck, 1979)

$$
\begin{array} { l } { E \left[ { \eta ( t _ { j } ) \eta ( t _ { i } ) } \right] = e ^ { - \beta ( t _ { j } - t _ { i } ) } E \left[ { \eta ( t _ { i } ) \eta ( t _ { i } ) } \right] } \\ { \displaystyle ~ + E \left[ \left( \int _ { t _ { i } } ^ { t _ { j } } e ^ { - \beta ( t _ { j } - \tau ) } u ( \tau ) d \tau \right) \eta ( t _ { i } ) \right] } \\ { \displaystyle = e ^ { - \beta ( t _ { j } - t _ { i } ) } E \left[ \eta ( t _ { i } ) \eta ( t _ { i } ) \right] } \end{array}
$$

since the stochastic process represented by the integral consists of independent increments. The remaining expectation is the autocorrelation of $\eta ( t )$ at $t _ { i }$ :

$$
\begin{array} { l } { { \displaystyle E \left[ \eta ( t _ { i } ) \eta ( t _ { i } ) \right] \equiv \Psi ( t _ { i } , t _ { i } ) } } \\ { { \displaystyle \qquad = \eta ^ { 2 } ( t _ { 0 } ) e ^ { - 2 \beta ( t _ { i } - t _ { 0 } ) } + \frac { \sigma ^ { 2 } } { 2 \beta } \left( 1 - e ^ { - 2 \beta ( t _ { i } - t _ { 0 } ) } \right) } } \end{array}
$$

where $\sigma ^ { 2 }$ is the variance (strength) of the driving noise in Eq. (4.9.51). Using Eq. (4.9.55), equation (4.9.54) can then be written as

$$
E \left[ \eta ( t _ { j } ) \eta ( t _ { i } ) \right] = \Psi ( t _ { i } , t _ { i } ) e ^ { - \beta ( t _ { j } - t _ { i } ) } .
$$

This is important because it points out one of the salient characteristics of the first-order Gauss-Markov process; that is, its autocorrelation fades exponentially with the rate of the fade governed by the time constant, $\tau = 1 / \beta$ .

Equation (4.9.53) contains a stochastic integral that cannot, in general, be evaluated except in a statistical sense. The mean of the stochastic integral is zero since $E [ \mathbf { u } ( t ) ] = 0$ . Its variance can be shown to be (Myers, 1973)

$$
\frac { \sigma ^ { 2 } } { 2 \beta } \big ( 1 - e ^ { - 2 \beta ( t _ { j } - t _ { i } ) } \big ) .
$$

Because the stochastic integral is a Gaussian process it is uniquely defined by its mean and variance. Hence, if a function can be found with the same mean and variance it will be an equivalent process. Such a discrete process is given by

$$
L _ { k } \equiv u _ { k } \sqrt { \frac { \sigma ^ { 2 } } { 2 \beta } ( 1 - e ^ { - 2 \beta ( t _ { j } - t _ { i } ) } ) }
$$

where $u _ { k }$ is a discrete, Gaussian random sequence with mean and variance

$$
\begin{array} { r } { E [ u _ { k } ] = 0 , \ E [ u _ { k _ { i } } u _ { k _ { j } } ] = \delta _ { i j } . } \end{array}
$$

It is evident that $L _ { k }$ has the same mean and variance as the stochastic integral in Eq. (4.9.53); hence, the solution for $\eta ( t )$ is given by

$$
\begin{array} { l } { { \eta ( t _ { j } ) = e ^ { - \beta ( t _ { j } - t _ { i } ) } \eta ( t _ { i } ) } } \\ { { \qquad + u _ { k } ( t _ { i } ) \sqrt { \frac { \sigma ^ { 2 } } { 2 \beta } ( 1 - e ^ { - 2 \beta ( t _ { j } - t _ { i } ) } ) } } } \end{array}
$$

where $u _ { k } ( t _ { i } )$ is a random number chosen by sampling from a Gaussian density function with a mean of zero and variance of 1.

The degree of correlation of the random process $\eta ( t )$ is determined by the choice of $\sigma$ and $\beta$ . For a finite value of $\beta$ and $\sigma ^ { 2 } \simeq 0$ , Eq. (4.9.60) yields

$$
\eta ( t _ { j } ) = e ^ { - \beta ( t _ { j } - t _ { i } ) } \eta ( t _ { i } )
$$

and as $\beta$ becomes small, $\eta ( t _ { j } )  \eta ( t _ { i } )$ , a constant. For a finit e value of $\sigma$ and $\beta \simeq 0$ , Eq. (4.9.60) yields

$$
\eta ( t _ { j } ) = \eta ( t _ { i } ) + u _ { k } ( t _ { i } ) \sigma \sqrt { t _ { j } - t _ { i } } ;
$$

![](images/1e527882dc4ed6d738db5dcc88362cb83daf4510e232655975fe7350dc462175.jpg)  
Figure 4.9.2: Gauss-Markov process for three time constants.

that is, a random walk process.

The term $\textstyle { \frac { \sigma ^ { 2 } } { 2 \beta } }$ represents the steady-state variance of $\eta ( t )$ , the variance after a large enough time so that any transients in $\eta ( t )$ have died out and it is in steady state.

With the proper choice of $\sigma$ and $\beta$ any number of time-correlated random functions can be generated. Figure 4.9.2 illustrates three histories of $\eta ( t )$ for $\beta = 0 . 0 0 1$ , 0.1, 1.0, and $\sigma = 1 . 0$ . Note that for $\beta = 1 0 ^ { - 3 }$ , $\eta ( t )$ is essentially constant. The shape of this curve can be varied by changing $\sigma$ or $\beta$ or both.

To use the Gauss-Markov process to account for unmodeled accelerations in the orbit determination procedure we may formulate the problem as follows. The equations of motion are

$$
{ \begin{array} { r l } { { \dot { \mathbf { r } } } = \mathbf { v } } & { } \\ { { \dot { \mathbf { v } } } } & { = \mathbf { \nabla } - { \frac { \mu \mathbf { r } } { r ^ { 3 } } } + \mathbf { f } ( t ) + \pmb { \eta } ( t ) } \\ { { \dot { \pmb { \eta } } } ( t ) } & { = \mathbf { \nabla } - \beta \pmb { \eta } ( t ) + \mathbf { u } ( t ) , } \end{array} }
$$

where $\begin{array} { r l r } { \textrm { -- } \frac { \mu \mathbf { r } } { r ^ { 3 } } + \mathbf { f } ( t ) } \end{array}$ represents the known accelerations and $\pmb { \eta } ( t )$ is a $3 \times 1$ vector of unknown accelerations. The procedure is to estimate the deterministic portion of $\pmb { \eta } ( t )$ and perhaps the associated time constants as part of the state vector. The random portion of $\pmb { \eta } ( t )$ contributes to the process noise covariance matrix $Q$ . For details on implementing this algorithm see Tapley and Ingram (1973), Ingram and Tapley (1974), Cruickshank (1998), Lichten (1990), or Goldstein et al. (2001).

An example of the use of process noise for SNC and DMC for a simple problem is given in Appendix F.

# 4.10 INFORMATION FILTER

A sequential estimation algorithm can be developed by propagating the information matrix, $\Lambda \equiv P ^ { - 1 }$ (Maybeck, 1979). This form of the filter offers some numerical properties with better characteristics than the covariance filter . Writing Eq. (4.7.3) in terms of the information matrix gives

$$
\begin{array} { r } { \{ \overline { { \Lambda } } _ { k } + \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \widetilde { H } _ { k } \} \hat { \mathbf { x } } _ { k } = \overline { { \Lambda } } _ { k } \overline { { \mathbf { x } } } _ { k } + \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \mathbf { y } _ { k } } \end{array}
$$

or

$$
\Lambda _ { k } \hat { \mathbf { x } } _ { k } = \overline { { \Lambda } } _ { k } \overline { { \mathbf { x } } } _ { k } + \widetilde { H } _ { k } ^ { T } R _ { k } ^ { - 1 } \mathbf { y } _ { k } .
$$

Recall that $\overline { { P } } _ { k + 1 }$ is expressed in terms of $P _ { k }$ by Eq. (4.9.50) and $\overline { { \mathbf { x } } } _ { k }$ is obtained by propagating $\hat { \mathbf { x } } _ { k - 1 }$ according to Eq. (4.9.19). The Schur identity is given by (see Appendix B)

$$
( A + B C ) ^ { - 1 } = A ^ { - 1 } - A ^ { - 1 } B ( I + C A ^ { - 1 } B ) ^ { - 1 } C A ^ { - 1 } .
$$

In Eq. (4.9.50) let

$$
\begin{array} { l } { A = \Phi \left( t _ { k + 1 } , t _ { k } \right) P _ { k } \Phi ^ { T } \left( t _ { k + 1 } , t _ { k } \right) } \\ { B = \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } } \\ { C = \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) . } \end{array}
$$

Then, for $Q _ { k }$ nonsingular, the Schur identity yields

$$
\begin{array} { r l } & { \overline { { \Lambda } } _ { k + 1 } = \overline { { P } } _ { k + 1 } ^ { - 1 } = M ( t _ { k + 1 } ) - M ( t _ { k + 1 } ) \Gamma ( t _ { k + 1 } , t _ { k } ) } \\ & { \qquad \times \left[ \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) M ( t _ { k + 1 } ) \Gamma ( t _ { k + 1 } , t _ { k } ) + Q _ { k } ^ { - 1 } \right] ^ { - 1 } } \\ & { \qquad \times \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) M ( t _ { k + 1 } ) } \end{array}
$$

where

$$
M ( t _ { k + 1 } ) = A ^ { - 1 } = \Phi ^ { T } ( t _ { k } , t _ { k + 1 } ) P _ { k } ^ { - 1 } \Phi ( t _ { k } , t _ { k + 1 } ) .
$$

If there is no process noise, Eq. (4.10.4) reduces to

$$
\overline { { \Lambda } } _ { k + 1 } = \overline { { P } } _ { k + 1 } ^ { - 1 } = M ( t _ { k + 1 } ) .
$$

Define

$$
\begin{array} { l } { L _ { k + 1 } \equiv M ( t _ { k + 1 } ) \Gamma ( t _ { k + 1 } , t _ { k } ) \qquad } \\ { \qquad \times \left[ \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) M ( t _ { k + 1 } ) \Gamma ( t _ { k + 1 } , t _ { k } ) + Q _ { k } ^ { - 1 } \right] ^ { - 1 } . } \end{array}
$$

In terms of $L _ { k + 1 }$ , Eq. (4.10.4) becomes

$$
\begin{array} { r } { \overline { { \Lambda } } _ { k + 1 } = M ( t _ { k + 1 } ) - L _ { k + 1 } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) M ( t _ { k + 1 } ) . } \end{array}
$$

The measurement update for $\Lambda _ { k + 1 }$ is obtained by inverting Eq. (4.7.4); that is,

$$
\Lambda _ { k + 1 } = \overline { { { \Lambda } } } _ { k + 1 } + \widetilde { H } _ { k + 1 } ^ { T } R _ { k + 1 } ^ { - 1 } \widetilde { H } _ { k + 1 } .
$$

Define the following quantities:

$$
\begin{array} { r l } & { \overline { { \mathbf { D } } } _ { k } \equiv \overline { { \Lambda } } _ { k } \overline { { \mathbf { x } } } _ { k } } \\ & { \hat { \mathbf { D } } _ { k } \equiv \Lambda _ { k } \hat { \mathbf { x } } _ { k } . } \end{array}
$$

The recursion relations for $\mathbf { D }$ are given by

$$
\overline { { \mathbf { D } } } _ { k + 1 } = \overline { { \Lambda } } _ { k + 1 } \overline { { \mathbf { x } } } _ { k + 1 } .
$$

Using Eq. (4.10.7),

$$
\begin{array} { r l } & { \mathbf { \overline { { D } } } _ { k + 1 } = \{ I - L _ { k + 1 } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) \} } \\ & { \qquad \times \ : \Phi ^ { T } ( t _ { k } , t _ { k + 1 } ) P _ { k } ^ { - 1 } \Phi ( t _ { k } , t _ { k + 1 } ) \mathbf { \overline { { x } } } _ { k + 1 } } \end{array}
$$

but $\hat { \mathbf { x } } _ { k } = \Phi ( t _ { k } , t _ { k + 1 } ) \overline { { \mathbf { x } } } _ { k + 1 }$ and $\hat { \mathbf { D } } _ { k } = P _ { k } ^ { - 1 } \hat { \mathbf { x } } _ { k }$ . Hence,

$$
\begin{array} { r } { \overline { { \mathbf { D } } } _ { k + 1 } = \left\{ I - L _ { k + 1 } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) \right\} \Phi ^ { T } ( t _ { k } , t _ { k + 1 } ) \hat { \mathbf { D } } _ { k } . } \end{array}
$$

Also, from Eq. (4.10.9) and the second of Eq. (4.10.1),

$$
\begin{array} { r } { \hat { \mathbf { D } } _ { k + 1 } = \Lambda _ { k + 1 } \hat { \mathbf { x } } _ { k + 1 } = \overline { { \mathbf { D } } } _ { k + 1 } + \widetilde { H } _ { k + 1 } ^ { T } R _ { k + 1 } ^ { - 1 } \mathbf { y } _ { k + 1 } . } \end{array}
$$

The procedure starts with $a$ priori values $\overline { { P } } _ { 0 }$ and $\overline { { \mathbf { x } } } _ { \mathrm { 0 } }$ . From these compute

$$
\begin{array} { r l } & { \overline { { \Lambda } } _ { 0 } = \overline { { P } } _ { 0 } ^ { - 1 } } \\ & { \overline { { \mathbf { D } } } _ { 0 } = \overline { { \Lambda } } _ { 0 } \overline { { \mathbf { x } } } _ { 0 } . } \end{array}
$$

Next compute $M _ { 1 } , L _ { 1 } , \overline { { { \Lambda } } } _ { 1 } , \overline { { { \bf D } } } _ { 1 } , \hat { \bf D } _ { 1 }$ , and $\Lambda _ { 1 }$ from Eqs. (4.10.5), (4.10.6), (4.10.7), (4.10.13), (4.10.14), and (4.10.8). Once $\Lambda _ { k }$ becomes nonsingular, its inverse can

be computed to obtain $P _ { k }$ and the optimal estimate of $\mathbf { x }$ can be computed from Eq. (4.10.10); that is,

$$
\hat { \mathbf { x } } _ { k } = P _ { k } \hat { \mathbf { D } } _ { k } .
$$

Time updates are given by Eqs. (4.10.5), (4.10.6), (4.10.7), and (4.10.13), with initial conditions given by Eq. (4.10.15). The measurement update is accomplished using Eqs. (4.10.8) and (4.10.14).

In summary, the covariance filter and the information filt er time and measurement updates are given by

Time Update— $\epsilon$ ovariance Filter

$$
\begin{array} { r l } & { \overline { { \mathbf { x } } } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) \widehat { \mathbf { x } } _ { k } } \\ & { \overline { { P } } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) P _ { k } \Phi ^ { T } \left( t _ { k + 1 } , t _ { k } \right) } \\ & { \qquad + \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) . } \end{array}
$$

Measurement Update— $\epsilon o$ variance Filter

$$
\begin{array} { r l } & { K _ { k + 1 } = \overline { { P } } _ { k + 1 } \widetilde { H } _ { k + 1 } ^ { T } ( R _ { k + 1 } + \widetilde { H } _ { k + 1 } \overline { { P } } _ { k + 1 } \widetilde { H } _ { k + 1 } ^ { T } ) ^ { - 1 } } \\ & { \widehat { \mathbf { x } } _ { k + 1 } = \overline { { \mathbf { x } } } _ { k + 1 } + K _ { k + 1 } ( \mathbf { y } _ { k + 1 } - \widetilde { H } _ { k + 1 } \overline { { \mathbf { x } } } _ { k + 1 } ) } \\ & { P _ { k + 1 } = ( I - K _ { k + 1 } \widetilde { H } _ { k + 1 } ) \overline { { P } } _ { k + 1 } . } \end{array}
$$

# Time Update—Inf ormation Filter

$$
\begin{array} { r l } & { M ( t _ { k + 1 } ) = \Phi ^ { T } ( t _ { k } , t _ { k + 1 } ) \Lambda _ { k } \Phi ( t _ { k } , t _ { k + 1 } ) } \\ & { \qquad L _ { k + 1 } = M ( t _ { k + 1 } ) \Gamma ( t _ { k + 1 } , t _ { k } ) } \\ & { \qquad \times [ \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) M ( t _ { k + 1 } ) \Gamma ( t _ { k + 1 } , t _ { k } ) } \\ & { \qquad + Q _ { k } ^ { - 1 } ] ^ { - 1 } } \\ & { \qquad { \overline { { \mathbf { D } } } _ { k + 1 } } = \left\{ I - L _ { k + 1 } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) \right\} } \\ & { \qquad \times \Phi ^ { T } ( t _ { k } , t _ { k + 1 } ) { \overline { { \mathbf { D } } } _ { k } } } \\ &  { \qquad { \overline { { \Lambda } } _ { k + 1 } } = { \overline { { P } } _ { k + 1 } ^ { - 1 } } = \left[ I - L _ { k + 1 } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) \right] } \\ & { \qquad \times M ( t _ { k + 1 } ) . } \end{array}
$$

Measurement Update—Information Filter

$$
\begin{array} { r l } & { \hat { \mathbf { D } } _ { k + 1 } = \overline { { \mathbf { D } } } _ { k + 1 } + \widetilde { H } _ { k + 1 } ^ { T } R _ { k + 1 } ^ { - 1 } \mathbf { y } _ { k + 1 } } \\ & { P _ { k + 1 } ^ { - 1 } = \Lambda _ { k + 1 } = \overline { { \Lambda } } _ { k + 1 } + \widetilde { H } _ { k + 1 } ^ { T } R _ { k + 1 } ^ { - 1 } \widetilde { H } _ { k + 1 } } \\ & { \hat { \mathbf { x } } _ { k + 1 } = \Lambda _ { k + 1 } ^ { - 1 } \hat { \mathbf { D } } _ { k + 1 } . } \end{array}
$$

We can initialize the information fil ter with $P _ { 0 } = \infty$ or with $P _ { 0 }$ singular, and obtain valid results for $\hat { \bf x }$ once $P _ { k }$ becomes nonsingular. The Cholesky Algorithm of Chapter 5 may be used to solve for $\hat { \bf x }$ . However, the solution for $\hat { \bf x }$ is not required by the algorithm and needs to be computed only when desired. The conventional sequential estimation algorithm fails in these cases. Also, as indicated in Section 4.7.1, the conventional sequential estimator can fail in the case where very accurate measurements are processed, which rapidly reduce the estimation error covariance matrix. This can be mitigated with the information filter.

Consider the example discussed in Section 4.7.1,

$$
\overline { { { P } } } _ { 0 } = \sigma ^ { 2 } I , \quad \sigma = 1 / \epsilon , \quad \widetilde { H } _ { 1 } = \big [ 1 \ \vdots \ \epsilon \big ] , \quad R = I
$$

where $\epsilon \ll 1$ and we assume that our computer word length is such that

$$
\begin{array} { c } { { 1 + \epsilon \neq 1 } } \\ { { 1 + \epsilon ^ { 2 } = 1 . } } \end{array}
$$

The objective is to find $P _ { 1 }$ ; that is, the estimation error covariance matrix after processing one observation using the information filt er. The information filter yields

$$
\begin{array} { r l } & { M _ { 1 } = \epsilon ^ { 2 } I } \\ & { \overline { { \Lambda } } _ { 1 } = M _ { 1 } } \\ & { \Lambda _ { 1 } = \overline { { \Lambda } } _ { 1 } + \widetilde { H } _ { 1 } ^ { T } R ^ { - 1 } \widetilde { H } _ { 1 } } \\ & { \quad = \epsilon ^ { 2 } I + \left[ \begin{array} { c c } { 1 } & { \epsilon } \\ { \epsilon } & { \epsilon ^ { 2 } } \end{array} \right] } \\ & { \Lambda _ { 1 } = P _ { 1 } ^ { - 1 } = \left[ \begin{array} { c c } { 1 } & { \epsilon } \\ { \epsilon } & { 2 \epsilon ^ { 2 } } \end{array} \right] } \end{array}
$$

and

$$
P _ { 1 } = \left[ { \begin{array} { c c } { 2 } & { - \sigma } \\ { - \sigma } & { \sigma ^ { 2 } } \end{array} } \right] .
$$

This is the same symmetric, positive definite result obtained from the batch processor and agrees with the exact solution to $O ( \epsilon )$ . Because we are accumulating the information matrix at each stage, the accuracy of the information filter should be comparable to that of the batch processor. Hence, the conventional covariance filter fails for this example, but the information filt er does not.

# 4.11 BATCH AND SEQUENTIAL ESTIMATION

As described in previous sections, two general categories of estimators are used, the batch processor and the sequential processor, both with distinct advantages and disadvantages. The batch formulation provides an estimate of the state at some chosen epoch using an entire batch or set of data. This estimate and its associated covariance matrix can then be mapped to other times. The sequential processor, on the other hand, provides an estimate of the state at each observation time based on observations up to that time. This solution and its associated covariance also can be mapped to another time.

In the sequential formulation without process noise, a mathematical equivalence can be shown between the batch and sequential algorithms; given the same data set, both algorithms produce the same estimates when the estimates are mapped to the same times. In the extended form of the sequential algorithm, where the reference orbit is updated at each observation time, the algorithms are not equivalent, but numerical experiments have shown a very close agreement.

Normally, the batch and sequential algorithm will need to be iterated to convergence, whereas the extended sequential will obtain near convergence in a single iteration. The sequential algorithm, unlike the batch, requires restarting a numerical integrator at each observation time. In general, the sequential processor is used in real-time applications supporting control or other decision functions and it is appropriate to incorporate some representation of the state noise to ensure that divergence does not occur. This implementation provides a means of compensating for various error sources in the processing of ground-based or onboard data. As indicated previously, inclusion of process noise in the batch algorithm substantially complicates the solution of the normal equations by increasing the dimensions of the normal matrix from $n$ (the number of state parameters) to $m$ (the number of observations).

# 4.12 OBSERVABILITY

The property of observability refers to the ability to apply an estimator to a particular system and obtain a unique estimate for all components of the state vector. As applied to orbital mechanics, the observability property refers to the ability to obtain a unique estimate of the spacecraft state as opposed to whether the satellite can be physically observed. Cases of unobservability rarely occur for properly formulated problems. However, these cases illustrate clearly the caution that must be exercised in applying an estimation algorithm to a particular problem. An unobservable parameter can best be illustrated by the following example.

Consider a satellite moving in an orbit about a perfectly spherical planet with a homogeneous mass distribution. Assuming no forces other than the gravitational attraction of the planet, which can be represented by a point mass, the orbit will be a conic section. Suppose a laser or radar range system exists on the surface of the planet capable of measuring to infinite precision the distance between the instrument and the satellite. Assuming the planet does not rotate and only a single range measuring system exists, the previously described estimators can be applied to the problem of estimating the state of the spacecraft at some appropriate time. Consider a single pass of the satellite over the station as shown in Fig. 4.11.1, where $\mathbf { R } _ { \mathbf { S } }$ is the station position vector, assumed known. Given a sequence of range measurements, $\rho _ { i }$ , as shown, an orbit could be determined from which the computed ranges match the measured values. However, a subtle problem exists because there is no change in the location of the tracking station relative to the orbit plane; hence, multiple solutions are possible—the same range history occurs for each orbit as we rotate the orbit’s angular momentum vector about $\mathbf { R } _ { \mathbf { S } }$ keeping $\alpha$ constant. This results in an infinite number of solutions that could have the same range measurement sequence. This circumstance leads to an ambiguity in the inclination, $i$ , and longitude of the ascending node, $\Omega$ . The difficulty is not alleviated by using multiple passes, since each pass would have the same geometry relative to the station. The possible multiple solutions will be manifested by a singular normal matrix $( H ^ { T } H )$ in the ordinary least squares formulation, regardless of the number of observations used.

![](images/4d2d4efa4c3deb36c29797fc5cec87f74bdd410c22eecdba0ee4965cb056174d.jpg)  
Figure 4.11.1: Single-station range geometry.

A unique solution can be obtained if (1) $i$ or $\Omega$ is known and not estimated, resulting in five elements being estimated, or (2) an $a$ priori covariance matrix is assigned to the state indicative of knowledge of $i$ or $\Omega$ . The problem can be avoided by other techniques as well; for example, using angular data such as azimuth and elevation or by using a second ranging station. However, this difficulty is not altered by varying the accuracy of the range measurements, or if range-rate is used instead of, or in addition to, range.

In practice, in a single pass the earth rotates slightly, resulting in a change in the station-orbit geometry. However, the resulting least squares system is frequently ill conditioned; that is, nearly singular. Numerous other examples of nonobservability exist, particularly in the recovery of spherical harmonic coefficients of the earth’s gravity field from inadequate amounts and distributions of tracking data.

The mathematical conditions for parameter observability can be derived from the observability criterion for a linear dynamical system.

Theorem: For the linear system and linear observation set,

$$
\begin{array} { r l } & { { \mathbf { x } } _ { i } = \boldsymbol { \Phi } ( t _ { i } , t _ { k } ) { \mathbf { x } } _ { k } } \\ & { { \mathbf { y } } _ { i } = \widetilde { H } _ { i } { \mathbf { x } } _ { i } + \epsilon _ { i } ; \qquad i = 1 , \dots , \ell } \end{array}
$$

complete observability of the $n \times 1$ state vector, at the general time, $t _ { k }$ , requires satisfying the condition

$$
\delta \mathbf { x } _ { k } ^ { T } \Lambda \delta \mathbf { x } _ { k } > 0
$$

for all arbitrary real vectors, $\delta \mathbf { x } _ { k }$ , where the $n \times n$ information matrix, $\Lambda$ , is defined as

$$
\Lambda = \sum _ { i = 1 } ^ { \ell } \Phi ^ { T } ( t _ { i } , t _ { k } ) \widetilde { H } _ { i } ^ { T } R _ { i } ^ { - 1 } \widetilde { H } _ { i } \Phi ( t _ { i } , t _ { k } ) = H ^ { T } R ^ { - 1 } H
$$

and $H$ is defined by Eq. (4.2.38). Hence, complete observability of the state with the data in the batch accumulated from the observation set $\mathbf { y } _ { i } ; i = 1 , \ldots , \ell$ requires that the symmetric information matrix, $\Lambda$ , be positive definite. Note that in order for $\Lambda$ to be positive definite, $H$ must be full rank.

In addition to the constraints placed on the data as a necessary criterion for observability, care in the mathematical formulation of the problem must be exercised to ensure that only a minimal set of parameters is estimated. If spurious or unnecessary parameters are included in the problem formulation, the solution will be nonobservable regardless of the data characteristics. As an example, the expression for the acceleration on a satellite due to effects of atmospheric drag can be written as

$$
\mathbf { D } = - \frac { 1 } { 2 } \frac { C _ { D } A } { m } \rho ( h ) | \mathbf { V } _ { r e l } | \mathbf { V } _ { r e l }
$$

![](images/bd694add0d6b9bf1bfee64c3f6644efbe01e6a64f80ed2364a94c20544bcb9dd.jpg)  
Figure 4.12.1: Range vs time from ground-based station.

where ${ \bf V } _ { r e l } = { \bf V } - \omega _ { e } \times { \bf r }$ , $\mathbf { V }$ is the inertial satellite velocity, $\omega _ { e }$ is the rotational velocity of the atmosphere (which is assumed to be the same as the earth’s rotational velocity), $C _ { D }$ is the satellite drag coefficient, $A$ is the satellite projected cross-sectional area, $m$ is the satellite mass, and $\rho ( h )$ is the atmospheric density at the satellite altitude, $h$ . In many applications, $C _ { D }$ , $A$ , and $m$ will be sufficiently uncertain that the errors in their a priori values may degrade the estimate of the satellite state. However, if any two or all three of these parameters are added to the state vector, a singular or nonobservable state vector will result, no matter how dense or how complete the observation set is. In this case, the $H$ matrix will have two rows that are identical except for a scalar mutiplication factor. This condition will cause $H$ to be non-full-rank and $H ^ { T } H$ to be nonpositive defini te. The single scalar parameter,

$$
\beta = \frac { C _ { D } A } { m }
$$

can be included as a state variable, and a well-posed estimation problem will occur. Two constants, say $C _ { 1 }$ and $C _ { 2 }$ , that do not appear separately in other force functions cannot be observed. Rather the product $C _ { 3 } = C _ { 1 } C _ { 2 }$ may be observed. Any state variables that are linearly related to one another cannot be uniquely determined (see Exercise 2 of Chapter 1). In general, the observability criterion tests not only the completeness of the data set in both the spatial and temporal sense, but it also tests the validity of the problem formulation.

# 4.13 ERROR SOURCES

In the application of an estimation procedure to a satellite or trajectory problem, measurements are obtained by various ground-based or on-board instruments. For example, a ground-based ranging system may make the measurements shown in Fig. 4.13.1 with time measured in minutes since the first measurement. Based on a mathematical model of the dynamical system and the measurement system, a predicted or computed measurement could be generated and compared with the actual measurement. If, in fact, the models are quite accurate, the difference (or residual) between the actual and predicted (or computed) measurements (O-C) will exhibit the random component in the measurement system as in Fig. 4.13.3. On the other hand, as is usually the case, the model has some inaccuracies associated with it, and the residual pattern will exhibit the character shown in Fig. 4.13.2. By using a polynomial function of time, the systematic component in Fig. 4.13.2 can be removed to determine the noise-only components. The data editing functions to eliminate the spurious or erroneous measurements are applied to these residuals. Finally, the edited data in Fig. 4.13.2 are used by the estimators to improve the state and the force and measurement models.

In the ideal case, the nonzero difference between the actual measurement and the predicted value should be due to the noise and biasing that occur in making the measurement. In practice, however, the mathematical models that describe the satellite force environment and those that describe the instrument performing some measurement are not completely accurate, or certain approximations are made for the benefit of computer storage and/or computer execution time, which introduce some discrepancy or error in the data processing. It is frequently necessary to ascribe the source of an error to a phenomenon in the physical world or to an approximation made in the model of the real world. Knowledge of various parameters in the mathematical models, such as the mass of the Earth or the coefficients that describe the inhomogeneous mass distribution within the Earth, have been obtained through various experiments or through use of many measurements and are only approximately known.

Typical error sources are as follows.

# • SATELLITE FORCE MODEL:

# Gravitation parameters

– Mass of the earth (GM) – Geopotential coefficients, ( $C _ { l m }$ and $S _ { l m }$ ) – Solid earth and ocean tide perturbations – Mass and position of the moon and planets – General relativistic perturbation

![](images/9d75685a1d681065aa66a3503f0a6d91584cdbb3eab8f9070fc655c74025e348.jpg)  
Figure 4.13.1: O-C, random and systematic component.

![](images/707216c84961410275f5af087c7c725e3c471c0de1dd425a92ff29417b8068a1.jpg)  
Figure 4.13.2: Random component.

# Nongravitational parameters

– Drag ( $C _ { D }$ , atmospheric density)   
– Solar and earth radiation pressure   
– Thrust (including venting and momentum dumping)   
– Other (magnetic origin, etc.)

• MEASUREMENT MODEL:

# Inertial and terrestrial coordinate systems

– Precession and nutation – Polar motion

# Ground-based measurements

– Coordinates of tracking station   
– Atmospheric effects (tropospheric and ionospheric refraction)   
– Instrument modeling   
– Clock accuracy   
– Tectonic plate motion

The error sources are dependent on the satellite under consideration, that is, satellite configuration, the orbit altitude and inclination, and measurement systems. Some of these error sources have distinct signatures in the data, and others may be very similar, thus producing aliasing between these components and making it difficult or impossible to separate their effects into individual components.

As a consequence, one constantly attempts to improve the model of the satellite environment. However, this improvement is normally done outside the operations aspect in which state estimates may be needed for an ongoing mission. To improve the gravitational model, for example, observations of various types such as range, range-rate, and angular data from different satellites would be used in a large parameter least squares solution. These large parameter solutions, in which the number of parameters may be 5000 or more, consume large amounts of computer time and, consequently, can be performed only infrequently. A family of such solutions has been generated since 1972 at the Goddard Space Flight Center and the Center for Space Research, and in several international centers. The models start with the Goddard Earth Model, GEM-1, and progress through the recent JGM-3 model (Tapley et al., 1996) developed for the TOPEX/Poseidon mission. In the case of JGM-3, a full degree-70 and order-70 solution was produced. Other solutions have been obtained at the Smithsonian Astrophysical Observatory (SAO), the Department of Defense, and by foreign institutions, including GFZ in Germany and GRGS in France.

Implicit in all of these solutions is the time standard used in solving Newton’s Equations, as well as time tagging the observations by various instruments. In the case of Newton’s Laws, a uniform time scale is inherent, and we attempt to provide such a system in time tagging the measurements. Uniform time scales are provided by atomic clocks, aside from small relativistic effects, and an operational problem exists to ensure that all clocks used in making measurements are adequately synchronized. For ground-based systems, station clocks are usually synchronized to a national standard. Clearly, in the event that a station is out of synchronization with the other stations, the measurements made at that station will produce residuals that are somewhat larger than the others.

# 4.14 ORBIT ACCURACY

In general, the orbit accuracy is dependent on the following factors:

1. Truncation error in the application of an approximating algorithm to a mathematical process;   
2. Round-off error in the application of a fini te computational precision;   
3. Mathematical model simplifications;   
4. Errors in the parameters used in the mathematical model of the physical system or the instrument model;   
5. Amount, type, and accuracy of tracking data.

For missions with high orbit-accuracy requirements, the limitation on the accuracy usually is imposed by the accuracy of the dynamical model, particularly the geopotential. But even the geopotential errors are dependent on the particular orbit; for example, an orbit at an altitude of one earth radius will be less affected by those errors than a satellite at an altitude of $8 0 0 { \mathrm { k m } }$ . The accuracy of the models is reflected in the current ability to determine an orbit for TOPEX/Poseidon (1334 km altitude) of ten days duration, which yields $1 \mathrm { c m }$ root mean square (RMS) of the laser range residuals (Tapley et al., 1994). This RMS reflects an overall orbit accuracy of about $8 \mathrm { c m }$ .

Determining the true accuracy of an orbit determination solution based on actual tracking data is difficult because the true trajectory is never known. Furthermore, the estimation error covariance matrix for a given solution is generally overly optimistic depending on the weights assigned to the tracking data. If realistic process noise has been included, the estimation error covariance matrix may be a good indicator of orbit accuracy but it is difficult to determine the level of process noise needed to properly scale the covariance matrix. This is best done through simulation studies, but these require quantitative knowledge of the error sources. Covariance analysis, described in Chapter 6, may also aid in accuracy assessment assuming statistical knowledge of the error sources is available.

A few quantitative indicators of accuracy can be examined depending on what tracking information is available. If solutions derived from different independent tracking systems are available they can be compared. The locations of most laser tracking sites are known to the centimeter level and the measurements themselves are accurate to this level. Therefore, if the satellite is tracked by lasers as it flies at high elevation over a site, the laser residuals will be a good indication of radial orbit accuracy. Furthermore, the estimation error covariance matrix can be mapped to these times, rotated to radial, along-track and cross-track directions and the radial standard deviation compared with the RMS of laser residuals. This comparison will provide a calibration of the radial component of the covariance matrix. The RMS of tracking data residuals is also an indicator of accuracy. However, small tracking residuals do not guarantee an accurate orbit because there may be a component of the satellite’s position that is insensitive to the particular tracking data type (see Section 4.12).

Another measure of accuracy is the RMS of orbit solution overlaps. For example, five days of contiguous tracking data may be fit as two arcs of three days length with one day of overlap. The RMS of the three components of overlapping position is an indicator of orbit accuracy. However, any error common to a given coordinate during the overlap period will not be evident in the RMS. Finally, orbit solutions for satellites that make any kind of metric measurements (radar altimeters, laser altimeters, SAR, etc.) can be evaluated by examining the quality of parameters based on these measurements themselves. For example, for laser or radar altimeter satellites the RMS of crossover residuals discussed in Chapter 3 are an indicator of orbit accuracy.

The accuracy just described relates to the estimation accuracy. Another important accuracy consideration occurs in the problem of prediction. Given some estimate of the satellite state, how well can the state of the spacecraft be predicted at some future time? Such prediction accuracy is important for (1) predicting and scheduling events at ground-based stations, including antenna or telescope pointing, and (2) scheduling events for future orbital maneuvers. The prediction accuracy is influenced by the same effects that influence the estimation accuracy; however, it is also dependent on the estimation accuracy itself. If, for instance, a perfect physical model was known but the state estimate used to initiate the prediction was in error, this error would grow during the prediction interval. As an example of prediction accuracy, the position of Lageos can be predicted to about 200 meters after two months. For the TOPEX/Poseidon Mission, the orbit can be predicted to about $0 . 5 \mathrm { k m }$ after a week based on tracking with laser ranging or the Global Positioning System.

# 4.15 SMOOTHING

It is often desirable to perform a smoothing operation when using a sequential filter . In this case, we are searching for the best estimate of the state at some time $t _ { k }$ based on all observations through time $t _ { \ell }$ where $\ell > k$ . For the case where there is no random component to the dynamical equation of state—for example, the no-process noise case—the batch estimation algorithm along with the prediction equation, Eqs. (4.4.19) and (4.4.22), will give the smoothed solution. However, as noted, the batch estimation approach has difficul ty including the effects of process noise. The smoothing algorithms have been developed to overcome this difficulty. Following Jazwinski (1970), the smoothing algorithm can be derived using a Bayesian approach of maximizing the density function of the state conditioned on knowledge of the observations through time, $t _ { \ell }$ . Our system is described in Section 4.9 (see Eq. (4.9.46)).

$$
\begin{array} { r } { \mathbf { x } _ { k + 1 } = \Phi ( t _ { k + 1 } , t _ { k } ) \mathbf { x } _ { k } + \Gamma ( t _ { k + 1 } , t _ { k } ) \mathbf { u } _ { k } } \\ { \mathbf { y } _ { k } = \widetilde { H } _ { k } \mathbf { x } _ { k } + \boldsymbol { \epsilon } _ { k } . \qquad } \end{array}
$$

We will use the notation $\hat { \mathbf { x } } _ { k } ^ { \ell }$ to indicate the best estimate of $\mathbf { x }$ at $t _ { k }$ based on observations through $t _ { \ell }$ , where in general $\ell > k$ . Following the Maximum Likelihood philosophy, we wish to find a recursive expression for $\hat { \mathbf { x } } _ { k } ^ { \ell }$ in terms of $\hat { \mathbf { x } } _ { k + 1 } ^ { \ell }$ , which maximizes the conditional density function

$$
p ( \mathbf { x } _ { k } , \mathbf { x } _ { k + 1 } / \mathbf { Y } _ { \ell } ) , \quad { \mathrm { w h e r e } } \quad \mathbf { Y } _ { \ell } = \mathbf { y } _ { 1 } , \mathbf { y } _ { 2 } \cdot \cdot \cdot \mathbf { y } _ { k } \cdot \cdot \cdot \mathbf { y } _ { \ell } .
$$

From Bayes Rule

$$
\begin{array} { l } { { p \left( { { \bf { x } } _ { k } } , { { \bf { x } } _ { k + 1 } } / { \bf { Y } } _ { \ell } \right) } = \displaystyle \frac { { p \left( { { { \bf { x } } _ { k } } , { { \bf { x } } _ { k + 1 } } , { \bf { Y } } _ { \ell } } \right) } } { { p \left( { { \bf { Y } } _ { \ell } } \right) } } = \displaystyle \frac { { p \left( { { { \bf { x } } _ { k } } , { { \bf { x } } _ { k + 1 } } , { \bf { Y } } _ { k } , { { \bf { y } } _ { k + 1 } } \ldots { \bf { y } } _ { \ell } } \right) } } { { p \left( { { \bf { Y } } _ { \ell } } \right) } } } \\ { ~ \displaystyle ~ = \frac { { p \left( { { { \bf { Y } } } _ { k } } \right) } } { { p \left( { { \bf { Y } } _ { \ell } } \right) } } p \left( { { { \bf { x } } _ { k } } , { { \bf { x } } _ { k + 1 } } , { { \bf { y } } _ { k + 1 } } \ldots { { \bf { y } } _ { \ell } } / { \bf { Y } } _ { k } } \right) ~ ( 4 . 1 5 ) } \\ { ~ \displaystyle ~ = \frac { { p \left( { { \bf { Y } } _ { k } } \right) } } { { p \left( { { \bf { Y } } _ { \ell } } \right) } } p \left( { { { \bf { y } } _ { k + 1 } } \ldots { \bf { y } } _ { \ell } } / { { \bf { x } } _ { k } } , { { \bf { x } } _ { k + 1 } } , { { \bf { Y } } _ { k } } \right) } \\ { ~ \displaystyle ~ \times { p \left( { { { \bf { x } } } _ { k } } , { { \bf { x } } _ { k + 1 } } / { { \bf { Y } } _ { k } } \right) } . } \end{array}
$$

Notice that

$$
p \left( \mathbf { y } _ { k + 1 } \ldots \mathbf { y } _ { \ell } / \mathbf { x } _ { k } , \mathbf { x } _ { k + 1 } , \mathbf { Y } _ { k } \right) = p \left( \mathbf { y } _ { k + 1 } \ldots \mathbf { y } _ { \ell } / \mathbf { x } _ { k + 1 } \right) ,
$$

and

$$
\begin{array} { r l } & { p \left( \mathbf { x } _ { k } , \mathbf { x } _ { k + 1 } / \mathbf { Y } _ { k } \right) = p \left( \mathbf { x } _ { k + 1 } / \mathbf { x } _ { k } , \mathbf { Y } _ { k } \right) p \left( \mathbf { x } _ { k } / \mathbf { Y } _ { k } \right) } \\ & { \qquad = p \left( \mathbf { x } _ { k + 1 } / \mathbf { x } _ { k } \right) p \left( \mathbf { x } _ { k } / \mathbf { Y } _ { k } \right) , } \end{array}
$$

since knowledge of $\mathbf { x } _ { k }$ and ${ \bf Y } _ { k }$ is redundant. Using Eqs. (4.15.3) and (4.15.4), Eq. (4.15.2) may be written

$$
\begin{array} { r l r } {  { p ( \mathbf { x } _ { k } , \mathbf { x } _ { k + 1 } / \mathbf { Y } _ { \ell } ) = \frac { p ( \mathbf { Y } _ { k } ) } { p ( \mathbf { Y } _ { \ell } ) } p ( \mathbf { y } _ { k + 1 } \ldots \mathbf { y } _ { \ell } / \mathbf { x } _ { k + 1 } ) } } \\ & { } & { \times p ( \mathbf { x } _ { k + 1 } / \mathbf { x } _ { k } ) p ( \mathbf { x } _ { k } / \mathbf { Y } _ { k } ) . } \end{array}
$$

The first three density functions on the right-hand side of Eq. (4.15.5) are independent of $\mathbf { x } _ { k }$ ; hence, we need to be concerned only with $p ( \mathbf { x } _ { k + 1 } / \mathbf { x } _ { k } )$ and $p ( \mathbf { x } _ { k } / \mathbf { Y } _ { k } )$ . Assuming that these are Gaussian and that the process noise is zero mean, it is easily shown that

$$
\begin{array} { r l } & { p ( { \mathbf x } _ { k + 1 } / { \mathbf x } _ { k } ) \sim N \big ( \Phi ( t _ { k + 1 } , t _ { k } ) { \mathbf x } _ { k } , \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) \big ) } \\ & { p ( { \mathbf x } _ { k } / { \mathbf Y } _ { k } ) \sim N ( \hat { \mathbf x } _ { k } , P _ { k } ) . } \end{array}
$$

It may seem like the covariance of $p ( \mathbf { x } _ { k + 1 } / \mathbf { x } _ { k } )$ should be

$$
\Phi ( t _ { k + 1 } , t _ { k } ) P _ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) + \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) .
$$

However, notice that this is the density function of $\mathbf { x } _ { k + 1 }$ conditioned on knowledge of $\mathbf { x } _ { k }$ . Since $P _ { k }$ describes the error in $\hat { \mathbf { x } } _ { k }$ and $\mathbf { x } _ { k }$ has occurred and is known, $P _ { k }$ must be a null matrix.

In order to maximize the conditional probability density function given in Eq. (4.15.5), we may maximize the logarithm of $p \left( \mathbf { x } _ { k + 1 } / \mathbf { x } _ { k } \right) p \left( \mathbf { x } _ { k } / \mathbf { Y } _ { k } \right)$ ,

$$
\begin{array} { l } { { \displaystyle \ln { \cal L } = - \frac { 1 } { 2 } [ { \bf x } _ { k + 1 } - \Phi \left( t _ { k + 1 } , t _ { k } \right) { \bf x } _ { k } ] ^ { T } [ \Gamma \left( t _ { k + 1 } , t _ { k } \right) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) ] ^ { - 1 } } } \\ { { \displaystyle ~ \times \left[ { \bf x } _ { k + 1 } - \Phi \left( t _ { k + 1 } , t _ { k } \right) { \bf x } _ { k } \right] - \frac { 1 } { 2 } \left[ { \bf x } _ { k } - \hat { \bf x } _ { k } \right] ^ { T } P _ { k } ^ { - 1 } \left[ { \bf x } _ { k } - \hat { \bf x } _ { k } \right] . \quad ( 4 . } } \end{array}
$$

Suppose that $\hat { \mathbf { x } } _ { k + 1 } ^ { \ell }$ , the maximizing value of $\mathbf { x } _ { k + 1 }$ based on observations through $t _ { \ell }$ , is available. We wish to find the value of $\hat { \mathbf { x } } _ { k } ^ { \ell }$ that maximizes $\ln { \cal L }$ . Differentiating $\ln { \cal L }$ with respect to $\mathbf { x } _ { k }$ and setting this to zero yields (for simplicity we have dropped time identifiers on $\Phi ( t _ { k + 1 } , t _ { k } )$ and $\Gamma ( t _ { k + 1 } , t _ { k } ) ,$ )

$$
\begin{array} { r l } & { \hat { \mathbf { x } } _ { k } ^ { \ell } = [ ( P _ { k } ^ { k } ) ^ { - 1 } + \Phi ^ { T } ( \Gamma Q \Gamma ^ { T } ) ^ { - 1 } \Phi ] ^ { - 1 } } \\ & { \quad \times [ ( P _ { k } ^ { k } ) ^ { - 1 } \hat { \mathbf { x } } _ { k } ^ { k } + \Phi ^ { T } ( \Gamma Q \Gamma ^ { T } ) ^ { - 1 } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } ] , } \end{array}
$$

using our current notation,

$$
\begin{array} { l } { P _ { k } ^ { k } \equiv P _ { k } } \\ { \hat { \mathbf { x } } _ { k } ^ { k } \equiv \hat { \mathbf { x } } _ { k } . } \end{array}
$$

Applying the Schur identity we can write this in a more conventional form

$$
\hat { \mathbf { x } } _ { k } ^ { \ell } = \hat { \mathbf { x } } _ { k } ^ { k } + S _ { k } \left( \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } - \Phi ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { x } } _ { k } ^ { k } \right)
$$

where

$$
\begin{array} { r l } & { S _ { k } = P _ { k } ^ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) [ \Phi ( t _ { k + 1 } , t _ { k } ) P _ { k } ^ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) } \\ & { ~ + \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) ] ^ { - 1 } } \\ & { = P _ { k } ^ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) ( P _ { k + 1 } ^ { k } ) ^ { - 1 } . } \end{array}
$$

Eq. (4.15.9) is the smoothing algorithm. Computation goes backward in index $k$ , with $\hat { \mathbf { x } } _ { \ell } ^ { \ell }$ , the filt er solution, as initial conditions. Note that the filter solutions for $\hat { \mathbf { x } } _ { k } ^ { k }$ , $P _ { k } ^ { k }$ , $\Phi ( t _ { k + 1 } , t _ { k } )$ , and $\Gamma ( t _ { k + 1 } , t _ { k } )$ are required and should be stored in the filtering process. The time update of the covariance matrix, $P _ { k + 1 } ^ { k }$ , may be stored or recomputed.

The equation for propagating the smoothed covariance is derived next (Jazwinski, 1970; Rausch et al., 1965) . It can easily be shown from Eq. (4.15.9) that $\hat { \mathbf { x } } _ { k } ^ { \ell }$ is unbiased; hence, the smoothed covariance is defined by

$$
P _ { k } ^ { \ell } = E \left[ ( \hat { \mathbf { x } } _ { k } ^ { \ell } - \mathbf { x } _ { k } ) ( \hat { \mathbf { x } } _ { k } ^ { \ell } - \mathbf { x } _ { k } ) ^ { T } \right] .
$$

Subtracting $\mathbf { x } _ { k }$ from both sides of Eq. (4.15.9) and moving all terms involving smoothed quantities to the LHS yields:

$$
\tilde { \mathbf { x } } _ { k } ^ { \ell } - S _ { k } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } = \tilde { \mathbf { x } } _ { k } ^ { k } - S _ { k } \Phi ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { x } } _ { k } ^ { k }
$$

where

$$
\begin{array} { r } { \tilde { \mathbf { x } } _ { k } ^ { \ell } \equiv \hat { \mathbf { x } } _ { k } ^ { \ell } - \mathbf { x } _ { k } , \tilde { \mathbf { x } } _ { k } ^ { k } \equiv \hat { \mathbf { x } } _ { k } ^ { k } - \mathbf { x } _ { k } . } \end{array}
$$

Multiplying both sides of Eq. (4.15.12) by their respective transpose and taking the expected value yields

$$
\begin{array} { r l r } { \quad } & { } & { E \left( \tilde { \mathbf { x } } _ { k } ^ { \ell } \tilde { \mathbf { x } } _ { k } ^ { \ell ^ { T } } \right) + S _ { k } E \left( \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } \right) S _ { k } ^ { T } = } & { ( 4 . 1 \boldsymbol { : } \medskip } \\ { \quad } & { } & { E \left( \tilde { \mathbf { x } } _ { k } ^ { k } \tilde { \mathbf { x } } _ { k } ^ { k ^ { T } } \right) + S _ { k } \Phi ( t _ { k + 1 } , t _ { k } ) E \left( \hat { \mathbf { x } } _ { k } ^ { k } \hat { \mathbf { x } } _ { k } ^ { k ^ { T } } \right) \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) S _ { k } ^ { T } . } \end{array}
$$

By definiti on

$$
P _ { k } ^ { \ell } \equiv E \left[ \tilde { \mathbf { x } } _ { k } ^ { \ell } \tilde { \mathbf { x } } _ { k } ^ { \ell ^ { T } } \right]
$$

and

$$
P _ { k } ^ { k } \equiv E \left[ \tilde { \mathbf { x } } _ { k } ^ { k } \tilde { \mathbf { x } } _ { k } ^ { k ^ { T } } \right] .
$$

The cross product terms that have been dropped in Eq. (4.15.13) can be shown to be null matrices,

$$
\begin{array} { r l } & { E \left( \tilde { \mathbf { x } } _ { k } ^ { \ell } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } \right) = E \left( \hat { \mathbf { x } } _ { k } ^ { \ell } - \mathbf { x } _ { k } \right) \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } } \\ & { \qquad = E \left( \hat { \mathbf { x } } _ { k } ^ { \ell } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } \right) - E \left( \mathbf { x } _ { k } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } \right) } \\ & { \qquad = \hat { \mathbf { x } } _ { k } ^ { \ell } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } - E \left( \mathbf { x } _ { k } / \mathbf { y } _ { \ell } \right) \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } = 0 . } \end{array}
$$

Here $\hat { \bf x }$ is the conditional mean of the appropriate conditional density function and is not a random variable; hence,

$$
E \left[ \mathbf { x } _ { k } / \mathbf { y } _ { \ell } \right] \equiv \hat { \mathbf { x } } _ { k } ^ { \ell } .
$$

Likewise, for the filter results,

$$
\begin{array} { r l } & { E \left( \tilde { \mathbf { x } } _ { k } ^ { k } \hat { \mathbf { x } } _ { k } ^ { k ^ { \prime } } \right) = E \left( \hat { \mathbf { x } } _ { k } ^ { k } - \mathbf { x } _ { k } \right) \hat { \mathbf { x } } _ { k } ^ { k ^ { \prime } } } \\ & { \qquad = \hat { \mathbf { x } } _ { k } ^ { k } \hat { \mathbf { x } } _ { k } ^ { k ^ { \prime } } - E \left( \mathbf { x } _ { k } / \mathbf { y } _ { k } \right) \hat { \mathbf { x } } _ { k } ^ { k ^ { \prime } } = 0 . } \end{array}
$$

Hence, Eq. (4.15.13) becomes

$$
P _ { k } ^ { \ell } + S _ { k } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } S _ { k } ^ { T } = P _ { k } ^ { k } + S _ { k } \Phi ( t _ { k + 1 } , t _ { k } ) \hat { \mathbf { x } } _ { k } ^ { k } \hat { \mathbf { x } } _ { k } ^ { k ^ { T } } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) S _ { k } ^ { T } .
$$

Now,

$$
\begin{array} { r l } & { P _ { k + 1 } ^ { \ell } \equiv E \left\{ \left( \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } - \mathbf { x } _ { k + 1 } \right) \left( \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } - \mathbf { x } _ { k + 1 } \right) ^ { T } / \mathbf { y } _ { \ell } \right\} } \\ & { \qquad = - \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } + E \left( \mathbf { x } _ { k + 1 } \mathbf { x } _ { k + 1 } ^ { T } \right) } \end{array}
$$

or

$$
\begin{array} { r } { \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } \hat { \mathbf { x } } _ { k + 1 } ^ { \ell ^ { T } } = E ( \mathbf { x } _ { k + 1 } \mathbf { x } _ { k + 1 } ^ { T } ) - P _ { k + 1 } ^ { \ell } . } \end{array}
$$

Also, in terms of $\mathbf { x } _ { k }$ (let $G = \Phi ( t _ { k + 1 } , t _ { k } ) \mathbf { x } _ { k } + \Gamma ( t _ { k + 1 } , t _ { k } ) \mathbf { u } _ { k } )$

$$
\begin{array} { r l } & { E ( \mathbf { x } _ { k + 1 } \mathbf { x } _ { k + 1 } ^ { T } ) = E \left[ G G ^ { T } \right] } \\ & { \qquad = \Phi ( t _ { k + 1 } , t _ { k } ) E ( x _ { k } , x _ { k } ^ { T } ) \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) } \\ & { \qquad + \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) } \end{array}
$$

and

$$
\begin{array} { r l } & { P _ { k } ^ { k } = E \left\{ \left( \hat { \mathbf { x } } _ { k } ^ { k } - \mathbf { x } _ { k } \right) \left( \hat { \mathbf { x } } _ { k } ^ { k } - \mathbf { x } _ { k } \right) ^ { T } / \mathbf { y } _ { k } \right\} } \\ & { \quad \quad = - \hat { \mathbf { x } } _ { k } ^ { k } \hat { \mathbf { x } } _ { k } ^ { k ^ { T } } + E ( \mathbf { x } _ { k } \mathbf { x } _ { k } ^ { T } ) } \end{array}
$$

or

$$
\begin{array} { r } { \hat { \mathbf { x } } _ { k } ^ { k } \hat { \mathbf { x } } _ { k } ^ { k ^ { T } } = E \left( \mathbf { x } _ { k } \mathbf { x } _ { k } ^ { T } \right) - P _ { k } ^ { k } . } \end{array}
$$

Substituting Eqs. (4.15.20), (4.15.21), and (4.15.22) into (4.15.19) yields

$$
\begin{array} { r } { P _ { k } ^ { \ell } + S _ { k } \left[ - P _ { k + 1 } ^ { \ell } + \Gamma ( t _ { k + 1 } , t _ { k } ) Q _ { k } \Gamma ^ { T } ( t _ { k + 1 } , t _ { k } ) \right] S _ { k } ^ { T } } \\ { = P _ { k } ^ { k } - S _ { k } \Phi ( t _ { k + 1 } , t _ { k } ) P _ { k } ^ { k } \Phi ^ { T } ( t _ { k + 1 } , t _ { k } ) S _ { k } ^ { T } . } \end{array}
$$

Finally,

$$
\begin{array} { r } { P _ { k } ^ { \ell } = P _ { k } ^ { k } + S _ { k } \left( P _ { k + 1 } ^ { \ell } - P _ { k + 1 } ^ { k } \right) S _ { k } ^ { T } . } \end{array}
$$

Note that neither the smoothed covariance nor the observation data appear explicitly in the smoothing algorithm. The algorithm derived previously is identical to the Rauch, Tung, and Striebel smoother (1965).

Suppose there is no process noise (i.e., $Q = 0$ ), then the smoothing algorithm reduces to

$$
S _ { k } = \Phi ^ { - 1 } ( t _ { k + 1 } , t _ { k } ) ,
$$

and

$$
\begin{array} { r l } & { \hat { \mathbf { x } } _ { k } ^ { \ell } = \Phi ^ { - 1 } \bigl ( t _ { k + 1 } , t _ { k } \bigr ) \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } } \\ & { \qquad = \Phi \left( t _ { k } , t _ { k + 1 } \right) \hat { \mathbf { x } } _ { k + 1 } ^ { \ell } } \\ & { \qquad = \Phi \bigl ( t _ { k } , t _ { \ell } \bigr ) \hat { \mathbf { x } } _ { \ell } ^ { \ell } . } \end{array}
$$

Also,

$$
\begin{array} { r l } & { P _ { k } ^ { \ell } = \Phi ^ { - 1 } ( t _ { k + 1 } , t _ { k } ) P _ { k + 1 } ^ { \ell } \Phi ^ { - T } ( t _ { k + 1 } , t _ { k } ) } \\ & { \quad = \Phi \left( t _ { k } , t _ { k + 1 } \right) P _ { k + 1 } ^ { \ell } \Phi ^ { T } ( t _ { k } , t _ { k + 1 } ) } \\ & { \quad = \Phi ( t _ { k } , t _ { \ell } ) P _ { \ell } ^ { \ell } \Phi ^ { T } ( t _ { k } , t _ { \ell } ) . } \end{array}
$$

Hence, with no process noise the smoothing algorithm simply maps the final filter state estimate and covariance matrix to earlier epochs.

# 4.15.1 COMPUTATIONAL ALGORITHM FOR SMOOTHER

Given (from the filtering algorithm)

$$
\hat { \bf x } _ { \ell } ^ { \ell } , \ \hat { \bf x } _ { \ell - 1 } ^ { \ell - 1 } , \ P _ { \ell } ^ { \ell - 1 } , \ P _ { \ell - 1 } ^ { \ell - 1 } , \ \Phi ( t _ { \ell } , t _ { \ell - 1 } ) ;
$$

set $k = \ell - 1$

$$
\begin{array} { r l } & { S _ { \ell - 1 } = P _ { \ell - 1 } ^ { \ell - 1 } ~ \boldsymbol \Phi ^ { T } ( t _ { \ell } , t _ { \ell - 1 } ) ~ ( P _ { \ell } ^ { \ell - 1 } ) ^ { - 1 } } \\ & { \hat { \mathbf { x } } _ { \ell - 1 } ^ { \ell } = \hat { \mathbf { x } } _ { \ell - 1 } ^ { \ell - 1 } + S _ { \ell - 1 } ( \hat { \mathbf { x } } _ { \ell } ^ { \ell } - \boldsymbol \Phi ( t _ { \ell } , t _ { \ell - 1 } ) \hat { \mathbf { x } } _ { \ell - 1 } ^ { \ell - 1 } ) . } \end{array}
$$

Given (from the filtering algorithm and the previous step of the smoothing algorithm)

$$
{ \hat { \mathbf { x } } } _ { \ell - 2 } ^ { \ell - 2 } , \ P _ { \ell - 1 } ^ { \ell - 2 } , \ P _ { \ell - 2 } ^ { \ell - 2 } , \ { \hat { \mathbf { x } } } _ { \ell - 1 } ^ { \ell } , \ \Phi ( t _ { \ell - 1 } , t _ { \ell - 2 } ) ;
$$

set $k = \ell - 2$ , and compute

$$
\begin{array} { r l } & { S _ { \ell - 2 } = P _ { \ell - 2 } ^ { \ell - 2 } \Phi ^ { T } \left( t _ { \ell - 1 } , t _ { \ell - 2 } \right) ( P _ { \ell - 1 } ^ { \ell - 2 } ) ^ { - 1 } } \\ & { \hat { \mathbf { x } } _ { \ell - 2 } ^ { \ell } = \hat { \mathbf { x } } _ { \ell - 2 } ^ { \ell - 2 } + S _ { \ell - 2 } \left( \hat { \mathbf { x } } _ { \ell - 1 } ^ { \ell } - \Phi \left( t _ { \ell - 1 } , t _ { \ell - 2 } \right) \hat { \mathbf { x } } _ { \ell - 2 } ^ { \ell - 2 } \right) } \\ & { \qquad \vdots } \end{array}
$$

# 4.16 THE PROBABILITY ELLIPSOID

Given a normally distributed random vector, $\mathbf { x }$ , with mean $\overline { { \mathbf { x } } }$ , and variancecovariance $P$ , the function

$$
( { \bf x } - { \overline { { \bf x } } } ) ^ { T } P ^ { - 1 } ( { \bf x } - { \overline { { \bf x } } } ) = \ell ^ { 2 }
$$

is a positive definite quadratic form representing a family of hyperellipsoids of constant probability density (Mikhail, 1976; Bryson and Ho, 1975). The 3D case is important because we often are interested in the 3D ellipsoids associated with the position uncertainty of a satellite. For example, in the case of interplanetary missions, we are interested in the probability ellipsoid of the spacecraft as it impacts the plane that contains the center of gravity of the target planet and that is normal to the asymptote of the spacecraft trajectory relative to the planet. This plane, shown in Fig. 4.16.1 and referred to as the B-plane (Dorroh and Thornton, 1970), is the reference plane used in interplanetary navigation applications. The associated coordinate system has two orthogonal axes in this plane and one normal to it. The axes of the ellipsoid in the B-plane give information on the uncertainty of the nearest approach distance to the planet that is needed to give assurance that the spacecraft will not impact the planet. The out-of-plane axis relates to the accuracy of the encounter time. If the spacecraft is to be placed in orbit about the target planet, information from the covariance matrix used to generate the probability ellipsoid is used to design the capture maneuver, and to compute the a priori uncertainty of the resulting orbit parameters. Construction of the probability ellipsoid is most easily accomplished relative to the principal axes. To this end, we introduce the following theorem (Kreyszig, 1993).

Theorem: If $\mathbf { u } _ { 1 } , \mathbf { u } _ { 2 } , \ldots , \mathbf { u } _ { n }$ is an orthonormal system of eigenvectors associated, respectively, with the eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ of an $n \times n$ symmetric positive definite matrix, $P$ , and if

$$
U = [ \mathbf { u } _ { 1 } , \mathbf { u } _ { 2 } , \ldots , \mathbf { u } _ { n } ] _ { n \times n } ,
$$

![](images/ab9ec1b9314e283bee860db46b770896ccb2dd95cd88c8301b12624b0345c7a9.jpg)  
Figure 4.16.1: Probability ellipse on the B-plane.

then

$$
U ^ { T } P U = \left[ \begin{array} { l } { \lambda _ { 1 } \ 0 \ \cdots \ 0 } \\ { 0 \ \lambda _ { 2 } \cdots \ 0 } \\ { \vdots \qquad \ddots \ \vdots } \\ { 0 \ 0 \ \cdots \ \lambda _ { n } } \end{array} \right] = D \left[ \lambda _ { 1 } , \ \lambda _ { 2 } , \ldots , \ \lambda _ { n } \right] ;
$$

that is, $U ^ { T } P U$ is a diagonal matrix containing the eigenvalues of P. The normalized vectors $\mathbf { u } _ { 1 } , \mathbf { u } _ { 2 } , \ldots , \mathbf { u } _ { n }$ are called principal axes of $P$ , and the transformation matrix $U ^ { T }$ used to diagonalize $P$ is called a principal axes transformation. The matrix $U ^ { T }$ is the matrix of normalized eigenvectors and is orthogonal. For the random vector $\mathbf { x }$ with mean $\overline { { \mathbf { x } } }$ and variance-covariance, $P$ , the principal axes, $\mathbf { x } ^ { \prime }$ , are given by

$$
\mathbf { x } ^ { \prime } = U ^ { T } \mathbf { x } .
$$

The variance-covariance matrix, $P ^ { \prime }$ , associated with the principal axes is given by

$$
\begin{array} { r l } & { P ^ { \prime } \equiv E [ ( \mathbf { x } ^ { \prime } - \overline { { \mathbf { x } } } ^ { \prime } ) ( \mathbf { x } ^ { \prime } - \overline { { \mathbf { x } } } ^ { \prime } ) ^ { T } ] } \\ & { \quad = U ^ { T } E [ ( \mathbf { x } - \overline { { \mathbf { x } } } ) ( \mathbf { x } - \overline { { \mathbf { x } } } ) ^ { T } ] U } \\ & { \quad = U ^ { T } P U = D [ \lambda _ { 1 } \ldots \lambda _ { n } ] . } \end{array}
$$

In our case, $\Delta \mathbf { x }$ represents the estimation error vector defined by

$$
\Delta { \bf x } \equiv \hat { \bf x } - { \bf x } \equiv [ \tilde { x } \tilde { y } \tilde { z } ] ^ { T } ,
$$

with zero mean and variance-covariance given by

$$
P = E [ \Delta \mathbf { x } \Delta \mathbf { x } ^ { T } ] .
$$

Although this restriction is unnecessary, we will simplify matters and deal only with the three position coordinates of $\Delta \mathbf { x }$ and the associated $3 \times 3$ portion of the estimation error covariance matrix.

In this case, the equation for the probability ellipsoid is

$$
[ \tilde { x } \tilde { y } \tilde { z } ] P ^ { - 1 } \left[ \begin{array} { l } { \tilde { x } } \\ { \tilde { y } } \\ { \tilde { z } } \end{array} \right] = \ell ^ { 2 } .
$$

The ellipsoids for $\ell = 1 , 2$ , and 3 are called the $1 \sigma , 2 \sigma$ , and $3 \sigma$ error ellipsoids. The probability of the state estimate error falling inside these ellipsoids, assuming a trivariate Gaussian density function, is 0.200, 0.739, and 0.971, respectively.

To obtain the principal axes, we use the theorem just introduced and determine the matrix of normalized eigenvectors, $U$ , and the eigenvalues $\lambda _ { i }$ , $i = { 1 , 2 , 3 }$ of $P$ . The principal axes are given by

$$
\left[ \stackrel { \tilde { x } ^ { \prime } } { \tilde { y } ^ { \prime } } \right] = \boldsymbol { U } ^ { T } \left[ \stackrel { \tilde { x } } { \tilde { y } } \right] ,
$$

and the associated covariance matrix is

$$
P ^ { \prime } = U ^ { T } P U .
$$

The probability ellipsoids are given by

$$
\left[ { \tilde { x } } ^ { \prime } { \tilde { y } } ^ { \prime } { \tilde { z } } ^ { \prime } \right] { \left[ \begin{array} { l } { 1 / \lambda _ { 1 } } \\ { \qquad 1 / \lambda _ { 2 } } \\ { \qquad 1 / \lambda _ { 3 } } \end{array} \right] } { \left[ \begin{array} { l } { { \tilde { x } } ^ { \prime } } \\ { { \tilde { y } } ^ { \prime } } \\ { { \tilde { z } } ^ { \prime } } \end{array} \right] } = \ell ^ { 2 } ,
$$

or

$$
{ \frac { \tilde { x } ^ { \prime } ^ { 2 } } { \lambda _ { 1 } } } + { \frac { \tilde { y } ^ { \prime } ^ { 2 } } { \lambda _ { 2 } } } + { \frac { \tilde { z } ^ { \prime } ^ { 2 } } { \lambda _ { 3 } } } = \ell ^ { 2 } .
$$

It is convenient to arrange the eigenvectors so that $\lambda _ { 1 } > \lambda _ { 2 } > \lambda _ { 3 }$ (i.e., in order of descending values of $\lambda _ { i }$ ). The axes of the $1 \sigma$ ellipsoid are given by solving Eq.

![](images/a13172c3131df9ec303c2f907d13f523bbb7db98bbad7d74a359521d8a7953d5.jpg)  
Figure 4.16.2: Euler angles defined.

(4.16.9) for $\ell = 1$ and sequentially setting two of the coordinate values to zero; that is, to obtain the semimajor axis, $a$ , set $\tilde { x } ^ { \prime } = a$ and $\tilde { y } ^ { \prime } = \tilde { z } ^ { \prime } = 0$ . This yields

$$
a ^ { 2 } = \lambda _ { 1 } , b ^ { 2 } = \lambda _ { 2 } , c ^ { 2 } = \lambda _ { 3 } .
$$

The orientation of the ellipse relative to the original axis system is obtained by solving for the three Euler angles given by the transformation matrix, $U$ . It is convenient to choose the sign of the normalized eigenvectors so that $U$ defines a right-hand triad. This can be accomplished by requiring that ${ \bf u } _ { 1 } \times { \bf u } _ { 2 } = { \bf u } _ { 3 }$ .

The Euler angles are defined in Fig. 4.16.2. The first rotation is about the $z$ axis through the angle $\phi$ and takes the unprimed frame into the $\left( \begin{array} { l l } { \mathbf { \Phi } } & { \mathbf { \Phi } } \end{array} \right) ^ { \prime \prime \prime }$ frame. The second rotation is about the $x ^ { \prime \prime \prime }$ axis through the angle $\theta$ to the $( \mathrm { ~  ~ \sigma ~ } ) ^ { \prime \prime }$ frame, and the final rotation is about the $z ^ { \prime \prime }$ axis through the angle $\psi$ to the $( \quad ) ^ { \prime }$ or principal axes frame (Reddy and Rasmussen, 1990). This transformation is analogous to that of transforming Earth-centered, Earth-fix ed coordinates into orbital plane coordinates with the $x ^ { \prime }$ axis through perigee, the $z ^ { \prime }$ axis along the angular momentum vector, and the $y ^ { \prime }$ axis completing the right-hand triad. The transpose of the transformation matrix that accomplishes this is the matrix we have identified as $U$ ; that is, $\mathbf { x } ^ { \prime } = U ^ { T } \mathbf { x }$ where

$$
U = \left[ \begin{array} { c c c } { { C _ { \phi } C _ { \psi } - C _ { \theta } S _ { \phi } S _ { \psi } } } & { { - C _ { \phi } S _ { \psi } - C _ { \theta } S _ { \phi } C _ { \psi } } } & { { S _ { \theta } S _ { \phi } } } \\ { { S _ { \phi } C _ { \psi } + C _ { \theta } C _ { \phi } S _ { \psi } } } & { { - S _ { \phi } S _ { \psi } + C _ { \theta } C _ { \phi } C _ { \psi } } } & { { - S _ { \theta } C _ { \phi } } } \\ { { S _ { \theta } S _ { \psi } } } & { { S _ { \theta } C _ { \psi } } } & { { C _ { \theta } } } \end{array} \right] ,
$$

and where $C$ and $S$ represent cosine and sine, respectively. The Euler angles are given by

$$
\begin{array} { r l } & { \phi = \mathrm { a t a n 2 } \left[ \cfrac { U _ { 1 3 } } { - U _ { 2 3 } } \right] , 0 \leq \phi \leq 2 \pi } \\ & { \theta = \mathrm { a c o s } \left[ U _ { 3 3 } \right] , 0 \leq \theta \leq \pi } \\ & { \psi = \mathrm { a t a n 2 } \left[ \cfrac { U _ { 3 1 } } { U _ { 3 2 } } \right] , 0 \leq \psi \leq 2 \pi . } \end{array}
$$

Example: Consider a normally distributed 2D random vector, $\mathbf { x }$ , where

$$
\mathbf { x } \sim N ( 0 , P ) ,
$$

and

$$
P = \left[ { \begin{array} { l l } { 4 } & { 2 } \\ { 2 } & { 2 } \end{array} } \right] .
$$

Sketch the 1-, 2-, and $3 { - } \sigma$ probability ellipses.

The eigenvalues are given by the polynomial

$$
| P - \lambda I | = 0 ,
$$

or

$$
\begin{array} { r } { \left| \begin{array} { c c } { 4 - \lambda } & { 2 } \\ { 2 } & { 2 - \lambda } \end{array} \right| = 0 ; } \end{array}
$$

hence,

$$
\lambda ^ { 2 } - 6 \lambda + 4 = 0 ,
$$

and

$$
\lambda _ { 1 } = 5 . 2 3 6 , \quad \lambda _ { 2 } = 0 . 7 6 4 .
$$

The corresponding eigenvectors are given by

$$
[ P - \lambda _ { i } I ] { \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \end{array} \right] } = 0 , \quad i = 1 , 2 .
$$

The normalized eigenvectors are given by

$$
U = \left[ \begin{array} { c c } { { . 8 5 1 } } & { { - . 5 2 6 } } \\ { { . 5 2 6 } } & { { . 8 5 1 } } \end{array} \right] .
$$

The angle between the principal and original axes system is obtained by recognizing that the coordinate transformation matrix is given by (this can be determined by setting $\theta = \psi = 0$ in Eq. (4.16.11))

$$
U = \left[ \begin{array} { l l } { { \cos \phi } } & { { - \sin \phi } } \\ { { \sin \phi } } & { { \phantom { - } \cos \phi } } \end{array} \right] .
$$

Hence,

$$
\phi = \tan ^ { - 1 } { \frac { \sin \phi } { \cos \phi } } = 3 1 . 7 ^ { \circ }
$$

where $\phi$ is the angle between the $x _ { 1 }$ and $x _ { 1 } ^ { \prime }$ axes.

The semimajor axes $a _ { i }$ and minor axes $b _ { i }$ are given by

$$
\begin{array} { l } { { a _ { i } = \sqrt { \ell _ { i } ^ { 2 } \lambda \left( \mathrm { M a x } \right) } \ ~ } } \\ { { \ ~ } } \\ { { b _ { i } = \sqrt { \ell _ { i } ^ { 2 } \lambda ( \mathrm { M i n } ) } \ } } \end{array} { } i = 1 , 2 , 3 ; \ \ell _ { 1 } = 1 , \ \ell _ { 2 } = 2 , \ \ell _ { 3 } = 3
$$

with numerical values,

$$
\begin{array} { l l l } { { a _ { 1 } = 2 . 2 9 , } } & { { a _ { 2 } = 4 . 5 8 , } } & { { a _ { 3 } = 6 . 8 6 } } \\ { { b _ { 1 } = 0 . 8 7 , } } & { { b _ { 2 } = 1 . 7 5 , } } & { { b _ { 3 } = 2 . 6 2 } } \end{array} .
$$

The error ellipses can now be constructed:

![](images/168c0417dcfebcac5191cd0692ce8a9b9b1754b12b6bf5c86131c1d9a8531660.jpg)

# 4.16.1 TRANSFORMATION OF THE COVARIANCE MATRIX BETWEEN COORDINATE SYSTEMS

Sometimes it is desirable to transform the state vector and the estimation error covariance into alternate coordinate systems. For example, it may be of interest to view these quantities in a radial, transverse, and normal (RTN) system. Here the transverse direction is normal to the radius vector and the normal direction lies along the instantaneous angular momentum vector. RTN forms a right-hand triad.

The general transformation between any two coordinate frames (say prime to unprime) for a position vector is given by

$$
\mathbf { r } = \gamma \mathbf { r } ^ { \prime } + \mathbf { a } ,
$$

where $\gamma$ is an orthogonal transformation matrix, $\mathbf { r }$ is the vector in the unprimed frame, and a is the vector offset of the origin of the two systems expressed in the unprimed frame. Generally a will be zero unless, for example, we are transforming from a geocentric to a topocentric frame.

The velocity transforms according to

$$
\dot { \mathbf { r } } = \gamma \dot { \mathbf { r } } ^ { \prime } + \dot { \gamma } \mathbf { r } ^ { \prime } .
$$

Generally $\dot { \gamma }$ will be zero unless we are transforming from a rotating to a nonrotating frame or vice versa; for example, Earth-centered-Earth-fix ed to Earthcentered inertial (ECEF to ECI ). Let the unprimed system be the inertial, nonrotating frame. It can be shown (Wiesel, 1997) that ${ \dot { \gamma } } \mathbf { r } ^ { \prime } = { \boldsymbol { \omega } } \times \mathbf { r }$ , where $\omega$ is the angular velocity vector of the rotating frame expressed in the nonrotating frame coordinate system.

The transformation we want is ECI to RTN. We assume that the RTN frame is fix ed to the osculating orbit at each point in time; hence, $\dot { \gamma } = 0$ and

$$
\left[ \begin{array} { l } { \mathbf { r } } \\ { \mathbf { v } } \\ { \mathbf { V } } \end{array} \right] _ { \mathrm { R T N } } = \left[ \begin{array} { l l } { \gamma } & { \mathrm { ~  ~ 0 ~ } } \\ { \mathrm { ~  ~ 0 ~ } } & { \gamma } \end{array} \right] \left[ \begin{array} { l } { \mathbf { r } } \\ { \mathbf { v } } \\ { \mathbf { E C I } } \end{array} \right] _ { \mathrm { E C I } } .
$$

The covariance of the estimation error is transformed as follows:

$$
[ \hat { \bf x } - { \bf x } ] _ { \mathrm { R T N } } = \psi [ \hat { \bf x } - { \bf x } ] _ { \mathrm { E C I } } ,
$$

where

$$
\psi = \left[ \begin{array} { c c c } { \gamma } & { 0 } & { 0 } \\ { 0 } & { \gamma } & { 0 } \\ { 0 } & { 0 } & { I } \end{array} \right] \mathrm { ~ a n d ~ } \left[ \hat { \mathbf { x } } - \mathbf { x } \right] = \left[ \begin{array} { c c c } { \hat { \mathbf { r } } - \mathbf { r } } \\ { \hat { \mathbf { v } } - \mathbf { v } } \\ { \hat { \boldsymbol { \beta } } - \boldsymbol { \beta } } \end{array} \right] ,
$$

and r, $\mathbf { v }$ , and $\beta$ represent the true values of the position, velocity, and all other quantities in the state vector, respectively. It is assumed that none of the elements of $\beta$ are affected by the coordinate transformation. The desired covariance is given by

$$
\begin{array} { r l } & { P _ { \mathrm { R T N } } = E \left[ ( \hat { \mathbf { x } } - \mathbf { x } ) ( \hat { \mathbf { x } } - \mathbf { x } ) ^ { T } \right] _ { \mathrm { R T N } } } \\ & { \qquad = \psi E \left[ ( \hat { \mathbf { x } } - \mathbf { x } ) ( \hat { \mathbf { x } } - \mathbf { x } ) ^ { T } \right] _ { \mathrm { E C I } } \psi ^ { T } . } \end{array}
$$

The elements of $\gamma$ for the ECI to RTN transformation are given by

$$
\begin{array} { r l } & { \mathbf { u } _ { \mathrm { R } } = \frac { \mathbf { r } ^ { * } } { | \mathbf { r } ^ { * } | } = \epsilon _ { X } \mathbf { i } + \epsilon _ { Y } \mathbf { j } + \epsilon _ { Z } \mathbf { k } } \\ & { \mathbf { u } _ { \mathrm { T } } = \mathbf { u } _ { N } \times \mathbf { u } _ { R } = \delta _ { X } \mathbf { i } + \delta _ { Y } \mathbf { j } + \delta _ { Z } \mathbf { k } } \\ & { \mathbf { u } _ { N } = \frac { \mathbf { r } ^ { * } \times \mathbf { v } ^ { * } } { | \mathbf { r } ^ { * } \times \mathbf { v } ^ { * } | } = \alpha _ { X } \mathbf { i } + \alpha _ { Y } \mathbf { j } + \alpha _ { Z } \mathbf { k } , } \end{array}
$$

where $\mathbf { u } _ { \mathrm { R } }$ , uT, $\mathbf { u } _ { \mathrm { N } }$ are unit vectors in the RTN frame, i, j, and $\mathbf { k }$ are unit vectors in the ECI frame, and $\mathbf { r } ^ { * }$ and $\mathbf { v } ^ { * }$ are the position and velocity vectors of the reference orbit.

Equation (4.16.20) may be written

$$
\left[ \begin{array} { l } { \mathbf { u } _ { \mathrm { R } } } \\ { \mathbf { u } _ { \mathrm { T } } } \\ { \mathbf { u } _ { \mathrm { N } } } \end{array} \right] = \left[ \begin{array} { l l l } { \epsilon _ { X } ~ \epsilon _ { Y } ~ \epsilon _ { Z } } \\ { \delta _ { X } ~ \delta _ { Y } ~ \delta _ { Z } } \\ { \alpha _ { X } ~ \alpha _ { Y } ~ \alpha _ { Z } } \end{array} \right] \left[ \begin{array} { l } { \mathbf { i } } \\ { \mathbf { j } } \\ { \mathbf { k } } \end{array} \right] .
$$

Hence, the transformation matrix relating the RTN and ECI frame is

$$
\gamma = \left[ \begin{array} { l l l } { \epsilon _ { X } } & { \epsilon _ { Y } } & { \epsilon _ { Z } } \\ { \delta _ { X } } & { \delta _ { Y } } & { \delta _ { Z } } \\ { \alpha _ { X } } & { \alpha _ { Y } } & { \alpha _ { Z } } \end{array} \right] .
$$

# 4.17 COMBINING ESTIMATES

Assume we are given two unbiased and uncorrelated estimates $\hat { \mathbf { x } } _ { 1 }$ and $\hat { \mathbf { x } } _ { 2 }$ for the $n$ -vector $\mathbf { x }$ . Assume that the associated estimation errors $\pmb { \eta } _ { 1 }$ and $\eta _ { 2 }$ are Gaussian with covariance matrices $P _ { 1 }$ and $P _ { 2 }$ . Our objective is to establish a performance index and determine the combination of $\hat { \mathbf { x } } _ { 1 }$ and $\hat { \mathbf { x } } _ { 2 }$ that is an optimal, unbiased $\left( E [ \hat { \mathbf { x } } ] = \mathbf { x } \right)$ ) estimate of $\mathbf { x }$ .

Using the fact that the errors in $\hat { \mathbf { x } } _ { 1 }$ and $\hat { \mathbf { x } } _ { 2 }$ are zero mean and uncorrelated (hence, being Gaussian, they are independent), the joint density function for the

estimation errors, $\pmb { \eta } _ { 1 }$ and $\eta _ { 2 }$ , where

$$
\begin{array} { r } { \pmb { \eta } _ { 1 } = \hat { \bf x } _ { 1 } - { \bf x } } \\ { \pmb { \eta } _ { 2 } = \hat { \bf x } _ { 2 } - { \bf x } , } \end{array}
$$

is given by

$$
f ( \pmb { \eta } _ { 1 } , \pmb { \eta } _ { 2 } ) = f ( \pmb { \eta } _ { 1 } ) f ( \pmb { \eta } _ { 2 } )
$$

$$
\begin{array} { l } { { = \displaystyle \frac { 1 } { ( 2 \pi ) ^ { n / 2 } } \frac { 1 } { | P _ { 1 } | ^ { \frac { 1 } { 2 } } } e ^ { - \frac { 1 } { 2 } ( \pmb { \eta } _ { 1 } ^ { T } P _ { 1 } ^ { - 1 } \pmb { \eta } _ { 1 } ) } } } \\ { { \times \displaystyle \frac { 1 } { ( 2 \pi ) ^ { n / 2 } | P _ { 2 } | ^ { \frac { 1 } { 2 } } } e ^ { - \frac { 1 } { 2 } ( \pmb { \eta } _ { 2 } ^ { T } P _ { 2 } ^ { - 1 } \pmb { \eta } _ { 2 } ) } . } } \end{array}
$$

The method of Maximum Likelihood selects the value of $\mathbf { x }$ that maximizes the likelihood function $L = f ( \eta _ { 1 } , \eta _ { 2 } )$ . Because the density functions involved are Gaussian, all classical estimation techniques, Bayesian, Minimum Variance, or Maximum Likelihood, will yield the same results.

Maximizing the logarithm of $L$ is equivalent to maximizing $L$ . Hence, we wish to maximize

$$
\begin{array} { r l } & { \ln { L } = K - 1 / 2 \big [ \pmb { \eta } _ { 1 } ^ { T } P _ { 1 } ^ { - 1 } \pmb { \eta } _ { 1 } + \pmb { \eta } _ { 2 } ^ { T } P _ { 2 } ^ { - 1 } \pmb { \eta } \big ] } \\ & { \qquad = K - 1 / 2 \big [ ( \hat { \bf x } _ { 1 } - { \bf x } ) ^ { T } P _ { 1 } ^ { - 1 } ( \hat { \bf x } _ { 1 } - { \bf x } ) } \\ & { \qquad + ( \hat { \bf x } _ { 2 } - { \bf x } ) ^ { T } P _ { 2 } ^ { - 1 } ( \hat { \bf x } _ { 2 } - { \bf x } ) \big ] } \end{array}
$$

where

$$
K = \ln \left( \frac { 1 } { ( 2 \pi ) ^ { \eta / 2 } } \frac { 1 } { | P _ { 1 } | ^ { 1 / 2 } } \right) + \ln \left( \frac { 1 } { ( 2 \pi ) ^ { \eta / 2 } } \frac { 1 } { | P _ { 2 } | ^ { 1 / 2 } } \right) .
$$

Using Eq. (B.7.3) of Appendix B, for a maximum of $\ln { \cal L }$ , it is necessary that

$$
\frac { d \ln { \cal L } } { d { \bf x } } = - \frac { 1 } { 2 } \left[ - 2 P _ { 1 } ^ { - 1 } ( \hat { \bf x } _ { 1 } - { \bf x } ) - 2 P _ { 2 } ^ { - 1 } ( \hat { \bf x } _ { 2 } - { \bf x } ) \right] = 0 .
$$

Hence,

$$
P _ { 1 } ^ { - 1 } ( \hat { \bf x } _ { 1 } - \hat { \bf x } ) + P _ { 2 } ^ { - 1 } \left( \hat { \bf x } _ { 2 } - \hat { \bf x } \right) = 0
$$

and

$$
{ \hat { \mathbf { x } } } = ( P _ { 1 } ^ { - 1 } + P _ { 2 } ^ { - 1 } ) ^ { - 1 } [ P _ { 1 } ^ { - 1 } { \hat { \mathbf { x } } } _ { 1 } + P _ { 2 } ^ { - 1 } { \hat { \mathbf { x } } } _ { 2 } ] .
$$

Also,

$$
\frac { d ^ { 2 } \ln L } { d \mathbf { x } ^ { 2 } } = - ( P _ { 1 } ^ { - 1 } + P _ { 2 } ^ { - 1 } ) 
$$

which is negative definite; therefore, this is a maximum of $\ln { \cal L }$ .

It is easily shown that $\hat { \bf x }$ is unbiased,

$$
\begin{array} { r l } & { E \left[ \hat { \mathbf { x } } \right] = ( P _ { 1 } + P _ { 2 } ) ^ { - 1 } [ P _ { 1 } ^ { - 1 } E \left( \hat { \mathbf { x } } _ { 1 } \right) + P _ { 2 } ^ { - 1 } E \left( \hat { \mathbf { x } } _ { 2 } \right) ] } \\ & { \qquad = \mathbf { x } , } \end{array}
$$

since $E ( \hat { \mathbf { x } } _ { 1 } ) = E ( \hat { \mathbf { x } } _ { 2 } ) = \mathbf { x }$ .

The estimation error covariance, $P$ , associated with $\hat { \bf x }$ is given by

$$
P = E [ ( \hat { \mathbf { x } } - \mathbf { x } ) ( \hat { \mathbf { x } } - \mathbf { x } ) ^ { T } ] ,
$$

where

$$
\hat { \mathbf { x } } = \gamma [ P _ { 1 } ^ { - 1 } \hat { \mathbf { x } } _ { 1 } + P _ { 2 } ^ { - 1 } \hat { \mathbf { x } } _ { 2 } ] ,
$$

and

$$
\gamma \equiv ( P _ { 1 } ^ { - 1 } + P _ { 2 } ^ { - 1 } ) ^ { - 1 } .
$$

Using Eqs. (4.17.1) and the fact that

$$
E \left[ \pmb { \eta } _ { 1 } \right] = E \left[ \pmb { \eta } _ { 2 } \right] = 0 ,
$$

$$
E \left[ \pmb { \eta } _ { 1 } \pmb { \eta } _ { 1 } ^ { T } \right] = P _ { 1 } , E \left[ \pmb { \eta } _ { 2 } \pmb { \eta } _ { 2 } ^ { T } \right] = P _ { 2 } , E \left[ \pmb { \eta } _ { 1 } \pmb { \eta } _ { 2 } ^ { T } \right] = 0 ,
$$

we can write

$$
{ \hat { \bf x } } = \gamma [ P _ { 1 } ^ { - 1 } ( { \bf x } + \pmb { \eta } _ { 1 } ) + P _ { 2 } ^ { - 1 } ( { \bf x } + \pmb { \eta } _ { 2 } ) ] .
$$

Hence,

$$
\begin{array} { r } { \hat { \mathbf { x } } - \mathbf { x } = \gamma [ P _ { 1 } ^ { - 1 } \pmb { \eta } _ { 1 } + P _ { 2 } ^ { - 1 } \pmb { \eta } _ { 2 } ] , } \end{array}
$$

therefore,

$$
\begin{array} { r l } & { P = \gamma E \left\{ [ P _ { 1 } ^ { - 1 } \pmb { \eta } _ { 1 } + P _ { 2 } ^ { - 1 } \pmb { \eta } _ { 2 } ] [ P _ { 1 } ^ { - 1 } \pmb { \eta } _ { 1 } + P _ { 2 } ^ { - 1 } \pmb { \eta } _ { 2 } ] ^ { T } \right\} \gamma } \\ & { \quad = \gamma [ P _ { 1 } ^ { - 1 } P _ { 1 } P _ { 1 } ^ { - 1 } + P _ { 2 } ^ { - 1 } P _ { 2 } P _ { 2 } ^ { - 1 } ] \gamma } \\ & { \quad = \gamma } \\ & { \quad = ( P _ { 1 } ^ { - 1 } + P _ { 2 } ^ { - 1 } ) ^ { - 1 } . } \end{array}
$$

It is not necessary to assume that the errors in $\hat { \mathbf { x } } _ { 1 }$ and $\hat { \mathbf { x } } _ { 2 }$ are Gaussian. Knowing that the two estimates $\hat { \mathbf { x } } _ { 1 }$ and $\hat { \mathbf { x } } _ { 2 }$ are unbiased and uncorrelated, we could have simply chosen to minimize a performance index that yields a value of $\mathbf { x }$ that minimizes the weighted sum of squares of the estimation errors for $\hat { \bf x } _ { 1 }$ and $\hat { \mathbf { x } } _ { 2 }$ ,

$$
Q = \frac { 1 } { 2 } \left[ ( \hat { \bf x } _ { 1 } - { \bf x } ) ^ { T } P _ { 1 } ^ { - 1 } ( \hat { \bf x } _ { 1 } - { \bf x } ) + ( \hat { \bf x } _ { 2 } - { \bf x } ) ^ { T } P _ { 2 } ^ { - 1 } ( \hat { \bf x } _ { 2 } - { \bf x } ) \right] .
$$

Choosing $\mathbf { x }$ to minimize $Q$ will yield the result given by Eq. (4.17.4).

If there are $n$ independent solutions to combine, it is easily shown that

$$
\hat { \mathbf { x } } = \left( \sum _ { i = 1 } ^ { n } P _ { i } ^ { - 1 } \right) ^ { - 1 } \sum _ { i = 1 } ^ { n } P _ { i } ^ { - 1 } \hat { \mathbf { x } } _ { i } .
$$

# 4.18 REFERENCES

Battin, R., An Introduction to the Mathematics and Methods of Astrodynamics, American Institute of Aeronautics and Astronautics, Reston, VA, 1999.

Bertiger, W., Y. Bar-Sever, E. Christensen, E. Davis, J. Guinn, B. Haines, R. Ibanez-Meier, J. Jee, S. Lichten, W. Melbourne, R. Muellerschoen, T. Munson, Y. Vigue, S. Wu, T. Yunck, B. Schutz, P. Abusali, H. Rim, W. Watkins, and P. Willis , “GPS precise tracking of TOPEX/Poseidon: Results and implications,” J. Geophys. Res., Vol. 99, No. C12, pp. 24,449–24,462, December 15, 1995.

Bierman, G. J., Factorization Methods for Discrete Sequential Estimation, Academic Press, New York, 1977.

Bjorck, A., ¨ Numerical Methods for Least Squares Problems, SIAM, Philadelphia, PA, 1996.

Bryson, A. E., and Y. C. Ho, Applied Optimal Control, Hemisphere Publishing Corp., Washington, DC, 1975.

Bucy, R., and P. Joseph, Filtering for Stochastic Processes, John Wiley & Sons, Inc., New York, 1968.

Cruickshank, D. R., Genetic Model Compensation: Theory and Applications, Ph. D. Dissertation, The University of Colorado at Boulder, 1998.

Dahlquist, G., and A. Bjorck, ¨ Numerical Methods, Prentice-Hall, Englewood Cliffs, NJ, 1974 (translated to English: N. Anderson).

Desai, S. D., and B. J. Haines, “N ear real-time GPS-based orbit determination and sea surface height observations from the Jason-1 mission,” Marine Geodesy, Vol. 26, No. 3–4, pp. 187–199, 2003.

Deutsch, R., Estimation Theory, Prentice-Hall, Inc., Englewood Cliffs, NJ, 1965.

Dorroh, W. E., and T. H. Thornton, “Strate gies and systems for navigation corrections,” Astronautics and Aeronautics, Vol. 8, No. 5, pp. 50–55, May 1970.

Fisher, R. A., “On an absolute criteria for fitti ng frequency curves,” Mess. Math., Vol. 41, pp. 155–160, 1912.

Gauss, K. F., Theoria Motus Corporum Coelestium, 1809 (Translated into English: Davis, C. H., Theory of the Motion of the Heavenly Bodies Moving about the Sun in Conic Sections, Dover, New York, 1963).

Gelb, A. (ed.), Applied Optimal Estimation, MIT Press, Cambridge, MA, 1974.

Goldstein, D. B., G. H. Born, and P. Axelrad, “Real-ti me, autonomous, precise orbit determination using GPS,” J. ION, Vol. 48, No. 3, pp. 169–179, Fall 2001.

Grewal, M. S., and A. P. Andrews, Kalman Filtering: Theory and Practice, Prentice Hall, 1993.

Ingram, D. S., Orbit determination in the presence of unmodeled accelerations, Ph.D. Dissertation, The University of Texas at Austin, 1970.

Ingram, D. S., and B. D. Tapley, “Lunar orbit determination in the presence of unmodeled accelerations,” Celest. Mech., Vol. 9, No. 2, pp. 191–211, 1974.

Jazwinski, A. H., Stochastic Process and Filtering Theory, Academic Press, New York, 1970.

Kalman, R. E., “A New Approach to Linear Filtering and Prediction Theory,” J. Basic Eng., Vol. 82, Series E, No. 1, pp. 35–45, March, 1960.

Kreyszig, E., Advanced Engineering Mathematics, John Wiley & Sons, Inc., New York, 1993.

Lawson, C. L., and R. J. Hanson, Solving Least Squares Problems, Prentice-Hall, Inc. Englewood Cliffs, NJ, 1974 (republished by SIAM, Philadelphia, PA, 1995).

Lichten, S. M., “Estima tion and filteri ng for high precision GPS positioning applications,” Manuscripta Geodaetica, Vol. 15, pp. 159–176, 1990.

Liebelt, P. B., An Introduction to Optimal Estimation, Addison-Wesley, Reading, MA, 1967.

Lutchke, S. B., N. P. Zelenski, D. D. Rowlands, F. G. Lemoine, and T. A. Williams, “The 1-centimeter orbit: Jason-1 precision orbit determination using GPS, SLR, DORIS and altimeter data,” Marine Geodesy, Vol. 26, No. 3-4, pp. 399–421, 2003.

Marshall, J. A., N. P. Zelensky, S. M. Klosko, D. S. Chinn, S. B. Luthcke, K. E. Rachlin, and R. G. Williamson, “The temporal and spatial characteristics of TOPEX/Poseidon radial orbit error,” J. Geophys. Res., Vol. 99, No. C12, pp. 25,331–25,352, December 15, 1995.

Maybeck, P. S., Stochastic Models, Estimation and Control, Vol. 1, Academic Press, 1979.

Mikhail, E. M., Observations and Least Squares, University Press of America, Lanham, MD, 1976.

Moler, C., and C. Van Loan, “Ninetee n dubious ways to compute the exponential of a matrix,” SIAM Review, Vol. 20, No. 4, pp. 801–836, October 1978.

Montenbruck, O., and E. Gill, Satellite Orbits: Models, Methods and Applications, Springer, 2001.

Myers, K. A., Filtering theory methods and applications to the orbit determination problem for near-Earth satellites, Ph.D. Dissertation, The University of Texas at Austin, November 1973.1973.

Rausch, H. E., F. Tung, and C. T. Striebel, “M aximum likelihood estimates of linear dynamic systems,” AIAA J., Vol. 3, No. 7, pp. 1445–1450, August 1965.

Reddy, J. N., and M. L. Rasmussen, Advanced Engineering Analysis, Robert E. Krieger Publishing Co., Malabar, Florida, 1990.

Schlee, F. H., C. J. Standish, and N. F. Toda, “Di vergence in the Kalman filter ,” AIAA J., Vol. 5, No. 6, pp. 1114–1120, June 1967.

Schutz, B., B. D. Tapley, P. Abusali, H. Rim, “Dynamic orbit determination using GPS measurements from TOPEX/Poseidon,” Geophys. Res. Ltrs., Vol. 21, No. 19, pp. 2179–2182, 1994.

Sorenson, H. W. (ed.), Kalman Filtering: Theory and Applications, IEEE Press, 1985.

Swerling, P., “First order error propagation in a stagewise differential smoothing procedure for satellite observations,” J. Astronaut. Sci., Vol. 6, pp. 46–52, 1959.

Tapley, B. D., “Statist ical orbit determination theory,” in Recent Advances in Dynamical Astronomy, B. D. Tapley and V. Szebehely (eds.), D. Reidel, pp. 396–425, 1973.

Tapley, B. D.,“ Fundamentals of orbit determination”, in Theory of Satellite Geodesy and Gravity Field Determination, Vol. 25, pp. 235-260, Springer-Verlag, 1989.

Tapley, B. D., and D. S. Ingram, “O rbit determination in the presence of unmodeled accelerations”, Trans. Auto. Cont., Vol. AC-18, No. 4, pp. 369–373, August, 1973.

Tapley, B. D., J. Ries, G. Davis, R. Eanes, B. Schutz, C. Shum, M. Watkins, J. Marshall, R. Nerem, B. Putney, S. Klosko, S. Luthcke, D. Pavlis, R. Williamson, and N. P. Zelensky, “Preci sion orbit determination for TOPEX/ Poseidon,” J. Geophys. Res., Vol. 99, No. C12, pp. 24,383–24,404, December 15, 1994.

Tapley, B. D., M. Watkins, J. Ries, G. Davis, R. Eanes, S. Poole, H. Rim, B. Schutz, C. Shum, R. Nerem, F. Lerch, J. Marshall, S. Klosko, N. Pavlis, and R. Williamson, “The Joint Gravity Model 3”, J. Geophys. Res., Vol. 101, No. B12, pp. 28,029–28,049, December 10, 1996.

Walpole, R. E., R. H. Myers, S. L. Myers, and Y. Keying, Probability and Statistics for Engineers and Scientists, Prentice Hall, Englewood Cliffs, NJ, 2002.

Wiesel, W. E., Spaceflight Dynamics, McGraw-Hill, 1997.

# 4.19 EXERCISES

(1) A dynamical system is described by

$$
\dot { \mathbf { X } } ( t ) = \boldsymbol { A } \mathbf { X } ( t ) .
$$

Given that the state transition matrix for this system is

$$
\Phi = \left[ { \begin{array} { l } { e ^ { - 2 a t } 0 } \\ { 0 } \end{array} } \right] ,
$$

determine the matrix $A$ .

(2) Given the solution to the differential equation

$$
\dot { \mathbf { x } } ( t _ { i } ) = A ( t _ { i } ) \mathbf { x } ( t _ { i } )
$$

is

$$
\mathbf { x } ( t _ { i } ) = \boldsymbol \Phi ( t _ { i } , t _ { k } ) \mathbf { x } ( t _ { k } )
$$