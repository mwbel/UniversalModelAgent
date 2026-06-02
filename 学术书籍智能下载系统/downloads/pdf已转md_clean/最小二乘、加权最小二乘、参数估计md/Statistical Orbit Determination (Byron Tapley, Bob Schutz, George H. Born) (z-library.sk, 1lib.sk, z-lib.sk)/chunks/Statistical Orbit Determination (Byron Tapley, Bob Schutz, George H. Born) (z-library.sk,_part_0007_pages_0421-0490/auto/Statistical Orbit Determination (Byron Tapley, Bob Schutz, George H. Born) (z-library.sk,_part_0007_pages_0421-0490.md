Since $P _ { c _ { k } } = E [ \Delta \hat { \mathbf x } _ { c _ { k } } \Delta \hat { \mathbf x } _ { c _ { k } } ^ { T } ]$ , it follows that

$$
P _ { c _ { k } } = P _ { k } + S _ { k } { \overline { { P } } } _ { c c } S _ { k } ^ { T }
$$

where

$$
P _ { k } = E \big [ ( \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ^ { * } ) ( \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ^ { * } ) ^ { T } \big ] .
$$

$P _ { k }$ is the conventional $\mathtt { f }$ ter data noise covariance given by Eq. (6.5.28). Also,

$$
E \big [ \big ( \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ^ { * } \big ) ( \bar { \mathbf { c } } - \mathbf { c } ) ^ { T } \big ] = 0 ,
$$

because errors in the conventional filter estimate are by definition independent of errors in the consider parameters.

# 6.6 PROPAGATION OF THE ERROR COVARIANCE

The models for propagating the covariance matrix from time $t _ { j }$ to $t _ { k }$ can be obtained by noting that

Filter:

$$
P _ { k } = E \big [ ( \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ) ( \hat { \mathbf { x } } _ { k } \ - \ \mathbf { x } _ { k } ) ^ { T } \big ]
$$

where

$$
\hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } = \Phi ( t _ { k } , t _ { j } ) [ \hat { \mathbf { x } } _ { j } - \mathbf { x } _ { j } ]
$$

and

Consider:

$$
P _ { c _ { k } } = E \big [ ( \hat { \mathbf { x } } _ { c _ { k } } - \mathbf { x } _ { k } ) ( \hat { \mathbf { x } } _ { c _ { k } } - \mathbf { x } _ { k } ) ^ { T } \big ]
$$

where

$$
\begin{array} { r c l } { \hat { \mathbf { x } } _ { c _ { k } } - \mathbf { x } _ { k } } & { = } & { \left[ \Phi ( t _ { k } , t _ { j } ) \hat { \mathbf { x } } _ { c _ { j } } + \theta ( t _ { k } , t _ { j } ) \bar { \mathbf { c } } ) \right] } \\ & & { } & \\ & & & { - \left[ \Phi ( t _ { k } , t _ { j } ) \mathbf { x } _ { j } + \theta ( t _ { k } , t _ { j } ) \mathbf { c } \right] . } \end{array}
$$

Substituting Eqs. (6.6.2) and (6.6.4) into Eqs. (6.6.1) and (6.6.3), respectively, and performing the expected value operation leads to

Filter:

$$
P _ { k } = \Phi ( t _ { k } , t _ { j } ) P _ { j } \Phi ^ { T } ( t _ { k } , t _ { j } )
$$

and

Consider:

$$
\begin{array} { r c l } { P _ { c _ { k } } } & { = } & { E \Big \{ \big [ \Phi ( t _ { k } , t _ { j } ) \big ( \hat { \mathbf { x } } _ { c _ { j } } - \mathbf { x } _ { j } \big ) + \theta ( t _ { k } , t _ { j } ) \big ( \overline { { \mathbf { c } } } - \mathbf { c } \big ) \big ] \big [ \mathbf { \nabla } \big ] ^ { T } \Big \} } \\ & { = } & { \Phi ( t _ { k } , t _ { j } ) P _ { c _ { j } } \Phi ^ { T } ( t _ { k } , t _ { j } ) + \theta ( t _ { k } , t _ { j } ) \overline { { P } } _ { c c } \theta ^ { T } ( t _ { k } , t _ { j } ) } \\ & { + } & { \Phi ( t _ { k } , t _ { j } ) S _ { j } \overline { { P } } _ { c c } \theta ^ { T } ( t _ { k } , t _ { j } ) + \theta ( t _ { k } , t _ { j } ) \overline { { P } } _ { c c } S _ { j } ^ { T } \Phi ^ { T } ( t _ { k } , t _ { j } ) . } \end{array}
$$

This result is obtained by noting from Eq. (6.4.7) that

$$
P _ { x c _ { j } } = E \big [ \big ( \hat { \mathbf { x } } _ { c _ { j } } - \mathbf { x } _ { j } \big ) ( \overline { { \mathbf { c } } } - \mathbf { c } ) ^ { T } \big ] = S _ { j } \overline { { P } } _ { c c }
$$

and

$$
P _ { c x _ { j } } = \overline { { P } } _ { c c } S _ { j } ^ { T }
$$

where we have used the notation

$$
S _ { j } \equiv S _ { x c _ { j } } .
$$

By defining

$$
S _ { k } = \Phi ( t _ { k } , t _ { j } ) S _ { j } + \theta ( t _ { k } , t _ { j } )
$$

and using

$$
P _ { c j } = P _ { j } + S _ { j } \overline { { P } } _ { c c } S _ { j } ^ { T }
$$

from Eq. (6.5.32), we can write Eq. (6.6.6) for the consider covariance $P _ { c k }$ as

$$
P _ { c _ { k } } = P _ { k } + S _ { k } \overline { { P } } _ { c c } S _ { k } ^ { T } .
$$

The second term in the consider covariance will always be at least positive semidefinite and, as a consequence

$$
\mathrm { T r a c e } [ P _ { c _ { k } } ] > \mathrm { T r a c e } [ P _ { k } ] .
$$

Hence, the effect of the uncertainty in the consider parameters will lead to a larger uncertainty in the value of the estimate at a given time.

$P _ { x c }$ is propagated as follows

$$
\begin{array} { l c l } { P _ { x c _ { k } } } & { = } & { E \big [ ( \hat { \mathbf { x } } _ { c _ { k } } - \mathbf { x } _ { k } ) \beta ^ { T } \big ] } \\ & { = } & { E \big [ \Phi ( t _ { k } , t _ { j } ) ( \hat { \mathbf { x } } _ { c _ { j } } - \mathbf { x } _ { j } ) + \theta ( t _ { k } , t _ { j } ) ( \overline { { \mathbf { c } } } - \mathbf { c } ) \beta ^ { T } \big ] } \\ & { = } & { \Phi ( t _ { k } , t _ { j } ) P _ { x c _ { j } } + \theta ( t _ { k } , t _ { j } ) \overline { { P } } _ { c c } } \end{array}
$$

or $P _ { x c _ { k } }$ may be determined directly from $S _ { k }$ by using Eq. (6.6.7) and Eq. (6.6.9),

$$
P _ { x c _ { k } } = S _ { k } \overline { { P } } _ { c c } .
$$

Mapping of the complete consider covariance matrix may be written more compactly as follows. Define

$$
\mathbb { V } ( t _ { k } , t _ { j } ) \equiv \left[ \begin{array} { c c } { \Phi \left( t _ { k } , t _ { j } \right) } & { \theta ( t _ { k } , t _ { j } ) } \\ { 0 } & { I } \end{array} \right]
$$

then

$$
\mathbf { P } _ { c _ { k } } = \Psi ( t _ { k } , t _ { j } ) \mathbf { P } _ { c j } \Psi ^ { T } ( t _ { k } , t _ { j } ) .
$$

Recall that

$$
\mathbf { P } _ { c _ { k } } \equiv \left[ \begin{array} { l l } { P _ { c _ { k } } } & { P _ { x c _ { k } } } \\ { P _ { c x _ { k } } } & { \overline { { P } } _ { c c } } \end{array} \right]
$$

where the expressions for $P _ { c _ { k } }$ and $P _ { x c _ { k } }$ are given by Eqs. (6.6.11) and (6.6.13) respectively.

# 6.7 SEQUENTIAL CONSIDER COVARIANCE ANALYSIS

The algorithms for consider covariance analysis developed in batch form also can be developed in sequential form. The batch algorithm for $\hat { \bf x }$ can be modified to function in sequential form as follows.

Write Eq. (6.3.72) at the $k ^ { \mathrm { t h } }$ stage

$$
\hat { \mathbf { x } } _ { c _ { k } } = \hat { \mathbf { x } } _ { k } - P _ { k } H _ { x _ { k } } ^ { T } R _ { k } ^ { - 1 } H _ { c _ { k } } \overline { { \mathbf { c } } }
$$

where

$$
P _ { k } = \left( \overline { { P } } _ { k } ^ { - 1 } + \sum _ { i = 1 } ^ { k } H _ { x _ { i } } ^ { T } R _ { i } ^ { - 1 } H _ { x _ { i } } \right) ^ { - 1 }
$$

and

$$
H _ { x _ { k } } ^ { T } R _ { k } ^ { - 1 } H _ { c _ { k } } = \sum _ { i = 1 } ^ { k } H _ { x _ { i } } ^ { T } R _ { i } ^ { - 1 } H _ { c _ { i } }
$$

that is, $\overline { { P } } _ { 0 }$ , $H _ { x _ { i } }$ , and $H _ { c _ { i } }$ all have been mapped to the appropriate time $t _ { k }$ (e.g., $\overline { { P } } _ { k } = \Phi ( t _ { k } , t _ { 0 } ) \overline { { P } } _ { 0 } , \Phi ^ { T } ( t _ { k } , t _ { 0 } ) )$ , and $H _ { x _ { i } }$ and $H _ { c _ { i } }$ are defined by Eq. (6.5.23) and (6.5.24), respectively,

$$
H _ { x _ { i } } = \widetilde { H } _ { x _ { i } } \Phi ( t _ { i } , t _ { k } ) .
$$

The sensitivity matrix $S _ { k }$ is given by

$$
\boldsymbol { S _ { k } } = \frac { \partial \hat { \mathbf { x } } _ { k } } { \partial \overline { { \mathbf { c } } } } = - P _ { k } H _ { x _ { k } } ^ { T } R _ { k } ^ { - 1 } H _ { c _ { k } } .
$$

Hence (see also Eq. (6.4.5)),

$$
\hat { \mathbf { x } } _ { c _ { k } } = \hat { \mathbf { x } } _ { k } + S _ { k } \overline { { \mathbf { c } } } .
$$

The $a$ priori value of $\hat { \mathbf { x } } _ { c _ { k } }$ is given by

$$
\overline { { \mathbf { x } } } _ { c _ { k } } = \boldsymbol { \Phi } ( t _ { k } , t _ { k - 1 } ) \hat { \mathbf { x } } _ { c _ { k - 1 } } + \theta ( t _ { k } , t _ { k - 1 } ) \overline { { \mathbf { c } } } .
$$

Substituting Eq. (6.7.5) at the $k - 1 ^ { \mathrm { s t } }$ stage into Eq. (6.7.6) yields

$$
\overline { { \mathbf { x } } } _ { c _ { k } } = \Phi ( t _ { k } , t _ { k - 1 } ) \hat { \mathbf { x } } _ { k - 1 } + \big ( \Phi ( t _ { k } , t _ { k - 1 } ) S _ { k - 1 } + \theta ( t _ { k } , t _ { k - 1 } ) \big ) \overline { { \mathbf { c } } } .
$$

Define

$$
\overline { { { S } } } _ { k } = \Phi ( t _ { k } , t _ { k - 1 } ) S _ { k - 1 } + \theta ( t _ { k } , t _ { k - 1 } ) ,
$$

then

$$
\begin{array} { r } { \overline { { \mathbf { x } } } _ { c _ { k } } = \overline { { \mathbf { x } } } _ { k } + \overline { { S } } _ { k } \overline { { \mathbf { c } } } . } \end{array}
$$

Recall that $\overline { { \mathbf { x } } } _ { k }$ and $\hat { \mathbf { x } } _ { k }$ are the values of these quantities assuming there are no errors in the consider parameters (i.e., $\mathbf { c } = \overline { { \mathbf { c } } } = 0$ ) and $\overline { { P } } _ { c c }$ is the null matrix.

The deviation of $\overline { { \mathbf { x } } } _ { c k }$ in Eq. (6.7.9) from the true value of $\mathbf { x } _ { c }$ may be written in terms of the error in each component

$$
\delta \mathbf { \overline { { x } } } _ { c _ { k } } = \delta \mathbf { \overline { { x } } } _ { k } + \overline { { S } } _ { k } \delta \mathbf { \overline { { c } } }
$$

Multiplying Eq. (6.7.10) by its transpose and taking the expected value yields

$$
\begin{array} { r } { E \Big [ \delta \mathbf { \overline { { x } } } _ { c _ { k } } \delta \mathbf { \overline { { x } } } _ { c _ { k } } ^ { T } \Big ] = \overline { { P } } _ { c _ { k } } = E \Big [ \delta \mathbf { \overline { { x } } } _ { k } \delta \mathbf { \overline { { x } } } _ { k } ^ { T } \Big ] + \overline { { S } } _ { k } E \Big [ \beta \beta ^ { T } \Big ] \overline { { S } } _ { k } ^ { \textit { T } } } \end{array}
$$

where $\delta \overline { { \mathbf { c } } } = \overline { { \mathbf { c } } } - \mathbf { c } = \boldsymbol { \beta }$ , and all cross covariances are zero because $\delta \overline { { \mathbf { x } } } _ { k }$ is by definition independent of the consider parameters. Hence,

$$
\overline { { P } } _ { c _ { k } } = \overline { { P } } _ { k } + \overline { { S } } _ { k } \overline { { P } } _ { c c } \overline { { S } } _ { k } ^ { T } .
$$

Note that this equation is equivalent to Eq. (6.6.11) since both these equations simply map the consider covariance matrix forward in time.

The measurement update for $\overline { { P } } _ { c _ { k } }$ is defined by

$$
P _ { c _ { k } } = E \left[ \left( \hat { \mathbf { x } } _ { c _ { k } } - \mathbf { x } _ { k } \right) \left( \hat { \mathbf { x } } _ { c _ { k } } - \mathbf { x } _ { k } \right) ^ { T } \right] .
$$

Using Eq. (6.7.5), we may write the error in $\hat { \mathbf { x } } _ { c _ { k } }$ as

$$
\delta \hat { \mathbf { x } } _ { c _ { k } } = \delta \hat { \mathbf { x } } _ { k } + S _ { k } \delta \overline { { \mathbf { c } } } .
$$

Hence Eq. (6.7.13) may be written as

$$
P _ { c _ { k } } = E \left[ \delta \hat { \mathbf { x } } _ { c _ { k } } \delta \hat { \mathbf { x } } _ { c _ { k } } ^ { T } \right] = E \left[ \delta \hat { \mathbf { x } } _ { k } \delta \hat { \mathbf { x } } _ { k } ^ { T } \right] + S _ { k } E \left[ \beta \boldsymbol { \beta } ^ { T } \right] S _ { k } ^ { T }
$$

or

$$
P _ { c _ { k } } = P _ { k } + S _ { k } \overline { { P } } _ { c c } S _ { k } ^ { T } .
$$

The cross covariances $\overline { { P } } _ { x c _ { k } }$ and $P _ { x c _ { k } }$ are obtained from Eqs. (6.7.10) and (6.7.14), respectively,

$$
\begin{array} { l c l } { \overline { { P } } _ { x c _ { k } } } & { = } & { E \left[ \delta \overline { { \mathbf { x } } } _ { c _ { k } } \beta ^ { T } \right] } \\ & { = } & { \overline { { S } } _ { k } \overline { { P } } _ { c c } } \\ { P _ { x c _ { k } } } & { = } & { E \left[ \delta \hat { \mathbf { x } } _ { c _ { k } } \beta ^ { T } \right] } \\ & { = } & { S _ { k } \overline { { P } } _ { c c } . } \end{array}
$$

To obtain an expression for the measurement update of $\overline { { S } } _ { k }$ , note that an analogy with the expression for $\hat { \mathbf { x } } _ { k }$ of Eq. (4.7.16), $\hat { \mathbf { x } } _ { c _ { k } }$ , may be written as

$$
\hat { \mathbf { x } } _ { c _ { k } } = \overline { { \mathbf { x } } } _ { c _ { k } } + K _ { k } \big ( \mathbf { y } _ { k } - \widetilde { H } _ { x _ { k } } \overline { { \mathbf { x } } } _ { c _ { k } } - \widetilde { H } _ { c _ { k } } \overline { { \mathbf { c } } } \big ) .
$$

Using Eq. (6.7.9) this may be written as

$$
\hat { \mathbf { x } } _ { c _ { k } } = \overline { { \mathbf { x } } } _ { k } + \overline { { S } } _ { k } \overline { { \mathbf { c } } } + K _ { k } \left[ \mathbf { y } _ { k } - \widetilde { H } _ { x _ { k } } \left( \overline { { \mathbf { x } } } _ { k } + \overline { { S } } _ { k } \overline { { \mathbf { c } } } \right) - \widetilde { H } _ { c _ { k } } \overline { { \mathbf { c } } } \right]
$$

and recognizing that $\hat { \mathbf { x } } _ { k } = \bar { \mathbf { x } } _ { k } + K _ { k } ( \mathbf { y } _ { k } - \widetilde { H } _ { x _ { k } } \bar { \mathbf { x } } _ { k } )$ , Eq. (6.7.20) becomes

$$
\hat { \mathbf { x } } _ { c _ { k } } = \hat { \mathbf { x } } _ { k } + ( \overline { { S } } _ { k } - K _ { k } \widetilde { H } _ { x _ { k } } \overline { { S } } _ { k } - K _ { k } \widetilde { H } _ { c _ { k } } ) \overline { { \mathbf { c } } } .
$$

Comparing this with Eq. 6.7.5), it is seen that

$$
S _ { k } = ( I - K _ { k } { \widetilde H } _ { x _ { k } } ) \overline { { S } } _ { k } - K _ { k } { \widetilde H } _ { c _ { k } } .
$$

We now have the equations needed to write the computational algorithm for the sequential consider covariance filter.

$$
G i \nu e n \colon P _ { k - 1 } , \hat { \mathbf { x } } _ { k - 1 } , S _ { k - 1 } , \widetilde { H } _ { x _ { k } } , \widetilde { H } _ { c _ { k } } , \mathbf { y } _ { k }
$$

1. Compute the time updates

$$
\begin{array} { r c l } { \overline { { P } } _ { k } } & { = } & { \Phi \left( t _ { k } , t _ { k - 1 } \right) P _ { k - 1 } \Phi ^ { T } ( t _ { k } , t _ { k - 1 } ) } \\ { K _ { k } } & { = } & { \overline { { P } } _ { k } \widetilde { H } _ { x _ { k } } ^ { T } ( \widetilde { H } _ { x _ { k } } \overline { { P } } _ { k } \widetilde { H } _ { x _ { k } } ^ { T } + R _ { k } ) ^ { - 1 } } \\ { \overline { { S } } _ { k } } & { = } & { \Phi ( t _ { k } , t _ { k - 1 } ) S _ { k - 1 } + \theta ( t _ { k } , t _ { k - 1 } ) } \\ { \overline { { \mathbf { x } } } _ { k } } & { = } & { \Phi ( t _ { k } , t _ { k - 1 } ) \widehat { \mathbf { x } } _ { k - 1 } } \\ { \overline { { \mathbf { x } } } _ { c _ { k } } } & { = } & { \overline { { \mathbf { x } } } _ { k } + \overline { { S } } _ { k } \overline { { \mathbf { c } } } } \\ { \overline { { P } } _ { c _ { k } } } & { = } & { \overline { { P } } _ { k } + \overline { { S } } _ { k } \overline { { P } } _ { c e } \overline { { S } } _ { k } ^ { T } } \\ { \overline { { P } } _ { x c _ { k } } } & { = } & { \Phi \left( t _ { k } , t _ { k - 1 } \right) P _ { x c _ { k - 1 } } + \theta ( t _ { k } , t _ { k - 1 } ) \overline { { P } } _ { c c } } \\ & { = } & { \overline { { S } } _ { k } \overline { { P } } _ { c c } . } \end{array}
$$

2. Compute the measurement update

$$
\begin{array} { r c l } { P _ { k } } & { = } & { ( I - K _ { k } \widetilde { H } _ { x k } ) \overline { { P } } _ { k } } \\ { S _ { k } } & { = } & { ( I - K _ { k } \widetilde { H } _ { x k } ) \overline { { S } } _ { k } - K _ { k } \widetilde { H } _ { c _ { k } } } \\ { \hat { \mathbf { x } } _ { k } } & { = } & { \overline { { \mathbf { x } } } _ { k } + K _ { k } ( \mathbf { y } _ { k } - \widetilde { H } _ { x _ { k } } \overline { { \mathbf { x } } } _ { k } ) } \\ { \hat { \mathbf { x } } _ { c _ { k } } } & { = } & { \hat { \mathbf { x } } _ { k } + S _ { k } \overline { { \mathbf { c } } } } \\ { P _ { c _ { k } } } & { = } & { P _ { k } + S _ { k } \overline { { P } } _ { c c } S _ { k } ^ { T } } \\ { P _ { x c _ { k } } } & { = } & { S _ { k } \overline { { P } } _ { c c } . } \end{array}
$$

Note that $\bar { \mathbf { x } } _ { c _ { 0 } } = \bar { \mathbf { x } } _ { 0 }$ (from Eq. 6.7.9); the consider parameters do not affect the $a$ priori value of $\bar { \mathbf { x } } _ { c _ { 0 } }$ , hence $\bar { S } _ { 0 } = 0$ and

$$
S _ { 0 } = - K _ { 0 } { \widetilde H } _ { c _ { 0 } } .
$$

Normally in a covariance analysis one would be interested only in computing the consider covariances; hence, the estimates for $\hat { \bf x }$ and $\hat { \mathbf { x } } _ { c }$ need not be computed. Generally process noise is not included in a consider covariance analysis. However, if process noise has been included, Eq. (6.7.23) is replaced by

$$
\overline { { { P } } } _ { k } = \Phi ( t _ { k } , t _ { k - 1 } ) P _ { k - 1 } \Phi ^ { T } ( t _ { k } , t _ { k - 1 } ) + \Gamma ( t _ { k } , t _ { k - 1 } ) Q _ { k - 1 } \Gamma ^ { T } ( t _ { k } , t _ { k - 1 } ) .
$$

# 6.8 EXAMPLE: FREELY FALLING POINT MASS

A point mass is in free fall only under the influence of gravity. Observations of range, $x$ , are made from a fix ed referent point. Set up the consider analysis equations assuming that $x$ is estimated and $g$ is a consider parameter, and that $\overrightarrow { P } _ { 0 } = I$ , $R = I$ , $\overline { { P } } _ { c c } = \Pi$ , and $\overline { { P } } _ { x c } = 0$ .

![](images/5d59c770ee405b0cce55d441cb60e0fb1764d3aed4410ffc1f47a6b328800199.jpg)

Equation of motion: ${ \ddot { x } } = g$ State vector: $\mathbf { X } = { \left[ \begin{array} { l } { x } \\ { v } \end{array} \right] }$

System dynamics: ${ \dot { \mathbf { X } } } = F ( \mathbf { X } , t ) = { \left[ \begin{array} { l } { v } \\ { g } \end{array} \right] }$

$$
A = { \frac { \partial F } { \partial \mathbf { X } } } = { \left[ \begin{array} { l l } { { \frac { \partial v } { \partial x } } } & { { \frac { \partial v } { \partial v } } } \\ { { \frac { \partial g } { \partial x } } } & { { \frac { \partial g } { \partial v } } } \end{array} \right] } = { \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right] } ~ .
$$

The consider parameter, $C$ , is $g$ . Hence,

$$
B = \frac { \partial F } { \partial g } = \left[ \begin{array} { c } { { \displaystyle \frac { \partial v } { \partial g } } } \\ { { \displaystyle \frac { \partial g } { \partial g } } } \end{array} \right] = \left[ \begin{array} { c } { { \displaystyle 0 } } \\ { { \displaystyle 1 } } \end{array} \right] .
$$

The observation equation is

$$
\begin{array} { r c l } { { { \cal Y } ( { \bf X } , t ) } } & { { = } } & { { { \cal G } ( { \bf X } , t ) + \epsilon } } \\ { { } } & { { } } & { { = } } & { { x + \epsilon . } } \end{array}
$$

Because, $G ( \mathbf { X } , t ) = x$

$$
\begin{array} { r c l } { { { \tilde { H } } _ { x } } } & { { = } } & { { { \displaystyle \frac { \partial G } { \partial \mathbf { X } } } = \left[ \frac { \partial x } { \partial x } \ \frac { \partial x } { \partial v } \right] = [ 1 \ 0 ] } } \\ { { { \tilde { H } } _ { c } } } & { { = } } & { { { \displaystyle \frac { \partial G } { \partial g } } = 0 . } } \end{array}
$$

The differential equation for the state transition matrix is

$$
\begin{array} { r } { \dot { \Phi } = A \Phi , \quad \Phi ( t _ { o } , t _ { 0 } ) = I } \end{array}
$$

where

$$
A = \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right] .
$$

The solution for $\Phi ( t , t _ { 0 } )$ is

$$
\Phi ( t , t _ { 0 } ) = K e ^ { A ( t - t _ { 0 } ) }
$$

where $K$ is a constant matrix. Since $\Phi ( t _ { 0 } , t _ { 0 } ) = I$ , we have $K e ^ { A 0 } = I$ or $K = I$ . Therefore,

$$
\begin{array} { r l r } { \Phi ( t , t _ { 0 } ) } & { { } = } & { e ^ { A ( t - t _ { 0 } ) } } \end{array}
$$

$$
\quad = \quad I + A ( t - t _ { 0 } ) + { \frac { 1 } { 2 ! } } A ^ { 2 } ( t - t _ { 0 } ) ^ { 2 } + \ldots .
$$

Now

$$
A ^ { 2 } = { \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l l } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right] } = { \left[ \begin{array} { l l } { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} \right] } ~ .
$$

Thus, $A ^ { 2 }$ and higher powers of $A$ are all zero. Hence,

$$
\begin{array} { r c l } { \Phi ( t , t _ { 0 } ) } & { = } & { I + A ( t - t _ { 0 } ) } \\ & { = } & { \left[ \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] + \left[ \begin{array} { c c } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right] ( t - t _ { 0 } ) } \\ & { = } & { \left[ \begin{array} { c c } { 1 } & { \left( t - t _ { 0 } \right) } \\ { 0 } & { 1 } \end{array} \right] . } \end{array}
$$

The equation for the consider parameter mapping matrix is

$$
\dot { \theta } = A \theta + B , \quad \theta ( t _ { 0 } , t _ { 0 } ) = 0
$$

or

$$
\begin{array} { r } { \left[ \begin{array} { l } { \Dot { \theta } _ { 1 } } \\ { \Dot { \theta } _ { 2 } } \end{array} \right] = \left[ \begin{array} { l } { \theta _ { 2 } } \\ { 0 } \end{array} \right] + \left[ \begin{array} { l } { 0 } \\ { 1 } \end{array} \right] . } \end{array}
$$

Hence,

$$
\begin{array} { r c l } { { \dot { \theta } _ { 2 } } } & { { = } } & { { 1 } } \\ { { \theta _ { 2 } ( t , t _ { 0 } ) } } & { { = } } & { { t + k _ { 1 } . \quad A t \ t = t _ { 0 } , \quad \theta _ { 2 } = 0 } } \\ { { \theta _ { 2 } ( t , t _ { 0 } ) } } & { { = } } & { { t - t _ { 0 } . } } \end{array}
$$

Also $\dot { \theta } _ { 1 } = \theta _ { 2 }$ ; therefore,

$$
\theta _ { 1 } ( t , t _ { 0 } ) = \frac { ( t - t _ { 0 } ) ^ { 2 } } { 2 } + k _ { 2 } .
$$

At $t = t _ { 0 }$ , $\theta _ { 1 } = 0$ ; hence,

$$
\begin{array} { r c l } { { \theta _ { 1 } } } & { { = } } & { { \displaystyle \frac { ( t - t _ { 0 } ) ^ { 2 } } { 2 } } } \\ { { \theta ( t , t _ { 0 } ) } } & { { = } } & { { \left[ \begin{array} { c } { { ( t - t _ { 0 } ) ^ { 2 } / 2 } } \\ { { ( t - t _ { 0 } ) } } \end{array} \right] ~ . } } \end{array}
$$

The transformation of observation-state partials to epoch, $t _ { 0 }$ , is obtained by using Eqs. (6.5.23) and (6.5.24):

$$
\begin{array} { r c l } { H _ { x } ( t ) } & { = } & { \tilde { H } _ { x } ( t ) \Phi ( t , t _ { 0 } ) } \\ & { = } & { [ 1 \ 0 ] \ \left[ \begin{array} { c c } { 1 } & { ( t - t _ { 0 } ) } \\ { 0 } & { 1 } \end{array} \right] } \\ & { = } & { [ 1 \ ( t - t _ { 0 } ) ] } \\ { H _ { c } ( t ) } & { = } & { \tilde { H } _ { x } ( t ) \theta ( t , t _ { 0 } ) + \tilde { H } _ { c } ( t ) } \\ & { = } &  [ 1 \ 0 ] \left[ \begin{array} { c c } { ( t - t _ { 0 } ) ^ { 2 } / 2 } \\ { ( t - t _ { 0 } ) } & { \right] } \\ { = } & { ( t - t _ { 0 } ) ^ { 2 } / 2 . } \end{array} \end{array}
$$

The $( 2 \times 2 )$ normal matrix of the state and the $2 \times 1$ normal matrix of the consider parameter at time $t$ is given by

$$
\begin{array} { r l r } { ( H _ { x } ^ { T } H _ { x } ) _ { t } } & { = } & { \left[ \begin{array} { c } { 1 } \\ { ( t - t _ { 0 } ) } \end{array} \right] \left[ 1 ( t - t _ { 0 } ) \right] = \left[ \begin{array} { c c } { 1 } & { ( t - t _ { 0 } ) } \\ { ( t - t _ { 0 } ) } & { ( t - t _ { 0 } ) ^ { 2 } } \end{array} \right] } \\ { ( H _ { x } ^ { T } H _ { c } ) _ { t } } & { = } & { \left[ \begin{array} { c } { 1 } \\ { ( t - t _ { 0 } ) } \end{array} \right] \frac { ( t - t _ { 0 } ) ^ { 2 } } { 2 } = \left[ \begin{array} { c } { ( t - t _ { 0 } ) ^ { 2 } / 2 } \\ { ( t - t _ { 0 } ) ^ { 3 } / 2 } \end{array} \right] . \quad \quad } \end{array}
$$

Given that $\overline { { P } } _ { 0 } = I$ , $R = I$ and that three measurements are taken at $t = 0 , 1$ , and 2, and let $t _ { 0 } = 0$ . Then the accumulation of the normal matrices yields

$$
H _ { x } ^ { T } H _ { x } = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 0 } \end{array} \right] } + { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 1 } & { 1 } \end{array} \right] } + { \left[ \begin{array} { l l } { 1 } & { 2 } \\ { 2 } & { 4 } \end{array} \right] } = { \left[ \begin{array} { l l } { 3 } & { 3 } \\ { 3 } & { 5 } \end{array} \right] }
$$

and

$$
H _ { x } ^ { T } H _ { c } = { \left[ \begin{array} { l } { 0 } \\ { 0 } \end{array} \right] } + { \left[ \begin{array} { l } { 1 / 2 } \\ { 1 / 2 } \end{array} \right] } + { \left[ \begin{array} { l } { 2 } \\ { 4 } \end{array} \right] } = { \left[ \begin{array} { l } { 5 / 2 } \\ { 9 / 2 } \end{array} \right] } .
$$

The computed covariance at epoch, $t _ { 0 }$ , is given by

$$
P _ { 0 } = \left( H _ { x } ^ { T } H _ { x } + \overline { { P } } _ { 0 } ^ { - 1 } \right) ^ { - 1 } = \left[ \begin{array} { r r } { 4 } & { 3 } \\ { 3 } & { 6 } \end{array} \right] ^ { - 1 } = \left[ \begin{array} { r r } { 2 / 5 } & { - 1 / 5 } \\ { - 1 / 5 } & { 4 / 1 5 } \end{array} \right] .
$$

Assuming the variance of $g$ to be $\Pi$ , the consider covariance $P _ { c _ { o } }$ at the epoch is given by Eq. (6.5.32) with $k = 0$ ,

$$
\begin{array} { r } { P _ { c _ { 0 } } = P _ { 0 } + S _ { 0 } \Pi S _ { 0 } ^ { T } . } \end{array}
$$

The sensitivity matrix, $S _ { 0 }$ , is given by Eq. (6.4.4), with $R = I$ ,

$$
\begin{array} { r l r } { S _ { 0 } } & { = } & { - P _ { 0 } ( H _ { x } ^ { T } H _ { c } ) } \\ & { = } & { - \left[ \begin{array} { c c } { 2 / 5 } & { - 1 / 5 } \\ { - 1 / 5 } & { 4 / 1 5 } \end{array} \right] \left[ \begin{array} { c } { 5 / 2 } \\ { 9 / 2 } \end{array} \right] = - \left[ \begin{array} { c } { 1 / 1 0 } \\ { 7 / 1 0 } \end{array} \right] . } \end{array}
$$

Therefore,

$$
S _ { 0 } \Pi S _ { 0 } ^ { T } = \frac { \Pi } { 1 0 0 } \left[ \begin{array} { c c } { { 1 } } & { { 7 } } \\ { { 7 } } & { { 4 9 } } \end{array} \right]
$$

and the value of $P _ { c _ { 0 } }$ is given by

$$
P _ { c _ { 0 } } = \left[ { 2 / 5 - 1 / 5 \atop - 1 / 5 } \right] + \frac { \Pi } { 1 0 0 } \left[ \begin{array} { r r } { { 1 } } & { { 7 } } \\ { { 7 } } & { { 4 9 } } \end{array} \right] .
$$

Also,

$$
\begin{array} { r } { P _ { x c _ { 0 } } = S _ { 0 } \Pi = - \Pi \left[ \begin{array} { l } { 1 / 1 0 } \\ { 7 / 1 0 } \end{array} \right] . } \end{array}
$$

Finally from Eq. (6.6.16),

$$
\begin{array} { r l r } { \mathbf { P } _ { c _ { 0 } } } & { = } & { \left[ \begin{array} { l l } { P _ { c _ { 0 } } } & { P _ { x c _ { 0 } } } \\ { P _ { c x _ { 0 } } } & { \overline { { P } } _ { c c } } \end{array} \right] } \\ & { = } & { \left[ \begin{array} { l l l } { \frac { 4 0 + \Pi } { 1 0 0 } } & { \frac { - 2 0 + \Pi } { 1 0 0 } } & { \frac { - \Pi } { 1 0 } } \\ & { \frac { 8 0 + 1 4 7 \Pi } { 3 0 0 } } & { \frac { - 7 \Pi } { 1 0 } } \\ & & { \Pi } \end{array} \right] . } \end{array}
$$

Thus, the consider standard deviations of the position and velocity,

$$
\sqrt { \frac { ( 4 0 + \Pi ) } { 1 0 0 } }
$$

and

$$
\sqrt { \frac { ( 8 0 + 1 4 7 \Pi ) } { 3 0 0 } }
$$

are greater than the respective data noise standard deviations; namely, $\sqrt { 2 / 5 }$ and $\sqrt { 4 / 1 5 }$ .

# 6.8.1 PROPAGATION WITH TIME

The computed covariance is mapped from $t = 0$ to $t = 2$ by Eq. (6.6.10),

$$
\begin{array} { r l } { P _ { 2 } } & { = \phantom { - } \Phi ( t _ { 2 } , t _ { 0 } ) P _ { 0 } \Phi ^ { T } ( t _ { 2 } , t _ { 0 } ) } \\ & { = \phantom { - } \left[ \begin{array} { c c } { 1 } & { 2 } \\ { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { c c } { 2 / 5 } & { - 1 / 5 } \\ { - 1 / 5 } & { 4 / 1 5 } \end{array} \right] \left[ \begin{array} { c c } { 1 } & { 0 } \\ { 2 } & { 1 } \end{array} \right] = \left[ \begin{array} { c c } { 2 / 3 } & { 1 / 3 } \\ { 1 / 3 } & { 4 / 1 5 } \end{array} \right] . } \end{array}
$$

The contribution to the propagated covariance from the consider parameter uncertainty is given by the last term of Eq. (6.6.11),

$$
S _ { 2 } \Pi S _ { 2 } ^ { T }
$$

where, from Eq. (6.6.9)

$$
\begin{array} { r c l } { { S _ { 2 } } } & { { = } } & { { \Phi ( t _ { 2 } , t _ { 0 } ) S _ { 0 } + \theta ( t _ { 2 } , t _ { 0 } ) } } \\ { { } } & { { = } } & { { \left[ \begin{array} { c c } { { 1 } } & { { 2 } } \\ { { 0 } } & { { 1 } } \end{array} \right] ~ \left[ \begin{array} { c } { { } } \\ { { - 1 / 1 0 } } \\ { { - 7 / 1 0 } } \end{array} \right] + \left[ \begin{array} { c } { { 2 } } \\ { { 2 } } \end{array} \right] } } \\ { { } } & { { = } } & { { \left[ \begin{array} { c } { { 1 / 2 } } \\ { { 1 3 / 1 0 } } \end{array} \right] ~ . } } \end{array}
$$

Therefore,

$$
S _ { 2 } \Pi S _ { 2 } ^ { T } = \left[ \begin{array} { c } { { 1 / 2 } } \\ { { 1 3 / 1 0 } } \end{array} \right] \Pi \left[ 1 / 2 \quad 1 3 / 1 0 \right] = \Pi \left[ \begin{array} { c c } { { 1 / 4 } } & { { 1 3 / 2 0 } } \\ { { 1 3 / 2 0 } } & { { 1 6 9 / 1 0 0 } } \end{array} \right] .
$$

Thus, the consider covariance propagated to time $t = 2$ is

$$
P _ { c _ { 2 } } = P _ { 2 } + S _ { 2 } \Pi S _ { 2 } ^ { T } = \left[ \begin{array} { r r } { { 2 / 3 } } & { { 1 / 3 } } \\ { { 1 / 3 } } & { { 4 / 1 5 } } \end{array} \right] + \Pi \left[ \begin{array} { r r } { { 1 / 4 } } & { { 1 3 / 2 0 } } \\ { { 1 3 / 2 0 } } & { { 1 6 9 / 1 0 0 } } \end{array} \right] .
$$

Also,

$$
P _ { x c _ { 2 } } = S _ { 2 } \Pi = { \frac { \Pi } { 2 } } \left[ \begin{array} { c } { { 1 } } \\ { { 1 3 / 5 } } \end{array} \right] .
$$

Hence,

$$
\mathbf { P } _ { c _ { 2 } } = \left[ \begin{array} { l l l } { \frac { 8 + 3 \Pi } { 1 2 } } & { \frac { 2 0 + 3 9 \Pi } { 6 0 } } & { \frac { \Pi } { 2 } } \\ & { \frac { 8 0 + 5 0 7 \Pi } { 3 0 0 } } & { \frac { 1 3 \Pi } { 1 0 } } \\ & & { \Pi } \end{array} \right]
$$

where again the consider standard deviation is greater than the computed or data noise standard deviation. Recall that in this development we have let $\sigma _ { g } ^ { 2 } = \Pi$ Also note that $P _ { c _ { 2 } } - P _ { 2 }$ is positive definit e as was the case at $t _ { 0 }$ .

# 6.8.2 THE SEQUENTIAL CONSIDER ALGORITHM

As a continuation of this example, compute $\mathbf { P } _ { c _ { 2 } }$ using the sequential consider filter algorithm. We will compute $P _ { c _ { 0 } }$ , $P _ { c _ { 1 } }$ , and $P _ { c _ { 2 } }$ based on observations at $t = 0 ; t = 0 , 1 ; t = 0 , 1$ , and 2, respectively.

Beginning with $R = I$ , $\overline { { P } } _ { 0 } = \dot { I }$ , $\overline { { P } } _ { c c } = \Pi$ , $P _ { x c _ { 0 } } = 0$ , $\widetilde { H } _ { x _ { 0 } } = [ 1 0 ]$ , $\widetilde { H } _ { c _ { 0 } } = 0$ , compute

$$
\begin{array} { l l l } { { { \cal K } _ { 0 } } } & { { = } } & { { \overline { { { P } } } _ { 0 } \widetilde { H } _ { x _ { 0 } } ^ { T } ( \widetilde { H } _ { x _ { 0 } } \overline { { { P } } } _ { 0 } \widetilde { H } _ { x _ { 0 } } ^ { T } + R ) ^ { - 1 } } } \\ { { } } & { { } } & { { } } \\ { { { \cal K } _ { 0 } } } & { { = } } & { { \left[ \begin{array} { l } { { 1 / 2 } } \\ { { 0 } } \end{array} \right] } } \\ { { } } & { { } } & { { } } \\ { { S _ { 0 } } } & { { = } } & { { - K _ { 0 } \widetilde { H } _ { c _ { 0 } } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { 0 } } \\ { { { \cal P } _ { c _ { 0 } } } } & { { = } } & { { P _ { 0 } + S _ { 0 } \Pi S _ { 0 } ^ { T } } } \\ { { } } & { { = } } & { { P _ { 0 } } } \end{array}
$$

where

$$
\begin{array} { r l r } { P _ { 0 } } & { = } & { ( I - K _ { 0 } \widetilde H _ { x _ { 0 } } ) \overline { { P } } _ { 0 } } \\ & { = } & { \left[ \begin{array} { c c } { 1 / 2 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] . } \end{array}
$$

Hence, as expected, an error in $g$ cannot affect the state at $t _ { 0 }$ and the data noise and consider covariance for the state are identical. Therefore,

$$
\mathbf { P } _ { c _ { 0 } } = \left[ \begin{array} { c c c } { 1 / 2 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { \Pi } \end{array} \right] .
$$

Now compute $\mathbf { P } _ { c _ { 1 } }$ . The time update for $P _ { 0 }$ is given by Eq. (6.7.23)

$$
\begin{array} { r c l } { \overline { { P } } _ { 1 } } & { = } & { \Phi ( t _ { 1 } , t _ { 0 } ) P _ { 0 } \Phi ^ { T } ( t _ { 1 } , t _ { 0 } ) } \\ & { = } & { \left[ \begin{array} { c c } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { c c } { 1 / 2 } & { 0 } \\ { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { c c } { 1 } & { 0 } \\ { 1 } & { 1 } \end{array} \right] } \\ & { = } & { \left[ \begin{array} { c c } { 3 / 2 } & { 1 } \\ { 1 } & { 1 } \end{array} \right] . } \end{array}
$$

Also, from Eq. (6.7.24)

$$
\begin{array} { l l l } { { K _ { 1 } } } & { { = } } & { { { \overline { { P } } } _ { 1 } { \tilde { H } } _ { x _ { 1 } } ^ { T } ( { \tilde { H } } _ { x _ { 1 } } { \overline { { P } } } _ { 1 } { \tilde { H } } _ { x _ { 1 } } ^ { T } + R ) ^ { - 1 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \left[ \begin{array} { l } { { 3 / 5 } } \\ { { 2 / 5 } } \end{array} \right] . } } \end{array}
$$

The measurement update for $\overline { { P } } _ { 1 }$ is given by Eq. (6.7.30)

$$
\begin{array} { r c l } { P _ { 1 } } & { = } & { \left( I - K _ { 1 } \widetilde { H } _ { x _ { 1 } } \right) \overline { { P } } _ { 1 } } \\ & { = } & { \left[ I - \left[ \begin{array} { c } { 3 / 5 } \\ { 2 / 5 } \end{array} \right] \left[ 1 } & { 0 \right] \left[ \begin{array} { c c } { 3 / 2 } & { 1 } \\ { 1 } & { 1 } \end{array} \right] \right. } \\ & { = } & { \left[ \begin{array} { c c } { 3 / 5 } & { 2 / 5 } \\ { 2 / 5 } & { 3 / 5 } \end{array} \right] . } \end{array}
$$

From Eq. (6.7.25), the time update for $S _ { 0 }$ is

$$
\begin{array} { r l r } { \bar { S } _ { 1 } } & { { } = } & { \Phi ( t _ { 1 } , t _ { 0 } ) S _ { 0 } + \theta ( t _ { 1 } , t _ { 0 } ) } \end{array}
$$

and the measurement update is given by Eq. (6.7.31)

$$
\begin{array} { r l r } { S _ { 1 } } & { { } = } & { ( I - K _ { 1 } \widetilde { H } _ { x _ { 1 } } ) \bar { S } _ { 1 } - K _ { 1 } \widetilde { H } _ { c _ { 1 } } . } \end{array}
$$

However, $S _ { 0 } = 0$ , so

$$
\bar { S } _ { 1 } = \left[ \begin{array} { c } { { 1 / 2 } } \\ { { 1 } } \end{array} \right]
$$

and

$$
\begin{array} { r l r } { S _ { 1 } } & { { } = } & { \left[ \begin{array} { c } { 1 / 5 } \\ { 4 / 5 } \end{array} \right] . } \end{array}
$$

From Eq. (6.7.34)

$$
\begin{array} { r c l } { P _ { c _ { 1 } } } & { = } & { P _ { 1 } + S _ { 1 } \Pi S _ { 1 } ^ { T } } \\ & { = } & { \left[ \begin{array} { l l } { 3 / 5 } & { 2 / 5 } \\ { 2 / 5 } & { 3 / 5 } \end{array} \right] + \Pi \left[ \begin{array} { l l } { 1 / 2 5 } & { 4 / 2 5 } \\ { 4 / 2 5 } & { 1 6 / 2 5 } \end{array} \right] } \end{array}
$$

and from Eq. (6.7.35)

$$
\begin{array} { r l r } { P _ { x c _ { 1 } } } & { = } & { S _ { 1 } \Pi = \left[ \begin{array} { c } { \underline { { \Pi } } } \\ { 5 } \\ { 4 \underline { { \Pi } } } \\ { 5 } \end{array} \right] . } \end{array}
$$

Substituting these results into Eq. (6.6.16) yields the desired result

$$
\mathbf { P } _ { c _ { 1 } } = \left[ \begin{array} { l l l } { \frac { 1 5 + \Pi } { 2 5 } } & { \frac { 1 0 + 4 \Pi } { 2 5 } } & { \frac { \Pi } { 5 } } \\ & { \frac { 1 5 + 1 6 \Pi } { 2 5 } } & { \frac { 4 \Pi } { 5 } } \\ & & { \Pi } \end{array} \right] .
$$

Finally, it can be shown that

$$
\begin{array} { r l r } { P _ { 2 } } & { = } & { \left[ \begin{array} { l l } { 2 / 3 } & { 1 / 3 } \\ { 1 / 3 } & { 4 / 1 5 } \end{array} \right] } \\ { \bar { S } _ { 2 } } & { = } & { \left[ \begin{array} { l } { 3 / 2 } \\ { 9 / 5 } \end{array} \right] } \end{array}
$$

$$
\begin{array} { r c l } { { S _ { 2 } } } & { { = } } & { { \left[ \begin{array} { c } { { 1 / 2 } } \\ { { 1 3 / 1 0 } } \end{array} \right] } } \\ { { } } & { { } } & { { } } \\ { { P _ { c 2 } } } & { { = } } & { { \left[ \begin{array} { c c } { { 2 / 3 } } & { { 1 / 3 } } \\ { { 1 / 3 } } & { { 4 / 1 5 } } \end{array} \right] + \Pi \left[ \begin{array} { c c } { { 1 / 4 } } & { { 1 3 / 2 0 } } \\ { { 1 3 / 2 0 } } & { { 1 6 9 / 1 0 0 } } \end{array} \right] } } \\ { { } } & { { } } & { { } } \\ { { P _ { x c _ { 2 } } } } & { { = } } & { { \Pi \left[ \begin{array} { c } { { 1 / 2 } } \\ { { 1 3 / 1 0 } } \end{array} \right] } } \end{array}
$$

and

$$
\mathbf { P } _ { c _ { 2 } } = \left[ \begin{array} { l l l } { \frac { 8 + 3 \Pi } { 1 2 } } & { \frac { 2 0 + 3 9 \Pi } { 6 0 } } & { \frac { \Pi } { 2 } } \\ & { \frac { 8 0 + 5 0 7 \Pi } { 3 0 0 } } & { \frac { 1 3 \Pi } { 1 0 } } \\ & & { \Pi } \end{array} \right]
$$

which is in agreement with results from the batch processor.

# 6.8.3 PERTURBATION IN THE STATE ESTIMATE

Since the sensitivity matrix is by definition

$$
S _ { 0 } = \frac { \partial \hat { \mathbf { X } } _ { 0 } } { \partial g } .
$$

It follows that

$$
\Delta \hat { \mathbf X } _ { 0 } = \frac { \partial \hat { \mathbf X } _ { 0 } } { \partial g } \sqrt { \Pi } .
$$

In general, if $\sigma _ { g }$ is the $1 \sigma$ uncertainty in the value of $g$ , then

$$
\Delta \hat { \mathbf { X } } _ { 0 } = \left[ \begin{array} { l } { \Delta \hat { x } _ { 0 } } \\ { \Delta \hat { x } _ { 0 } } \end{array} \right] = S _ { 0 } \sigma _ { g } = - \left[ \begin{array} { l } { 1 / 1 0 } \\ { 7 / 1 0 } \end{array} \right] \sigma _ { g }
$$

or

$$
\begin{array} { r c l } { \Delta \hat { x } _ { 0 } } & { = } & { - \sigma _ { g } / 1 0 } \\ { \Delta \hat { \dot { x } } _ { 0 } } & { = } & { - 7 \sigma _ { g } / 1 0 } \end{array}
$$

which illustrates how the estimate of the epoch state for the batch processor will be in error as a function of the uncertainty in the consider parameter $g$ after processing the three observations of this example.

# 6.9 EXAMPLE: SPRING-MASS PROBLEM

A block of mass $m$ is attached to two parallel vertical walls by two springs as shown in Fig. 4.8.2. $k _ { 1 }$ and $k _ { 2 }$ are the spring constants. $h$ is the height of the position $P$ on one of the walls, from which the distance, $\rho$ , and the rate of change of distance of the block from $P$ , $\dot { \rho }$ can be observed.

Let the horizontal distances be measured with respect to the point $O$ where the line $O P$ , the lengths of the springs, and the center of mass of the block are all assumed to be in the same vertical plane. Then, if $\textstyle { \overline { { x } } }$ denotes the position of the block at static equilibrium, the equation of motion of the block is given by

$$
{ \ddot { x } } = - ( k _ { 1 } + k _ { 2 } ) ( x - { \overline { { x } } } ) / m .
$$

$$
\omega ^ { 2 } = ( k _ { 1 } + k _ { 2 } ) / m , \mathrm { a n d } \bar { x } = 0
$$

so that Eq. (6.9.1) can be written as

$$
\ddot { x } + \omega ^ { 2 } x = 0 .
$$

Consider the problem of estimating the position and the velocity of the block with respect to the reference point $O$ , by using the range and range-rate measurements of the block from the point, $P$ . To formulate this problem mathematically, the estimation state vector is taken as $\mathbf { X } ^ { T } = \left[ x \textbf { \textit { v } } \right]$ . Then the system dynamics are represented by

$$
{ \dot { \bf X } } = F ( { \bf X } , t ) = \left[ \begin{array} { c } { { { \dot { x } } } } \\ { { { \dot { v } } } } \end{array} \right] = \left[ \begin{array} { c } { { v } } \\ { { - \omega ^ { 2 } x } } \end{array} \right] ,
$$

or in state space form

$$
{ \dot { \mathbf { X } } } = { \left[ \begin{array} { l } { { \dot { x } } } \\ { { \dot { v } } } \end{array} \right] } = { \left[ \begin{array} { l l } { ~ 0 ~ } & { 1 } \\ { - \omega ^ { 2 } } & { 0 } \end{array} \right] } { \left[ \begin{array} { l } { x } \\ { v } \end{array} \right] } ~ .
$$

The observation vector is

$$
G ( \mathbf { X } , t ) = \left[ \begin{array} { c } { \rho } \\ { \dot { \rho } } \end{array} \right] = \left[ \begin{array} { c } { \sqrt { x ^ { 2 } + h ^ { 2 } } } \\ { x \dot { x } / \rho } \end{array} \right] .
$$

Suppose that some parameters are not known exactly and that the effect of their errors on the state estimates are to be evaluated. For example, let $m , k _ { 2 }$ , and $h$ be the set of “consider parameters.” Then the consider vector $\mathbf { C }$ will be

$$
\mathbf { C } ^ { T } = \bigg [ m \colon k _ { 2 } \colon h \bigg ]
$$

and $\mathbf { c } = \mathbf { C } - \mathbf { C } ^ { * }$ . The linearized state and observation equations, including the consider parameters, are given by

$$
\begin{array} { r c l } { \delta \dot { \mathbf { X } } } & { = } & { \boldsymbol { A } ( t ) \delta \mathbf { X } + \boldsymbol { B } ( t ) \mathbf { c } } \\ & & { } & \\ { \mathbf { y } } & { = } & { \tilde { H } _ { x } \delta \mathbf { X } + \tilde { H } _ { c } \mathbf { c } } \end{array}
$$

where

$$
\delta \mathbf { X } = { \left[ \begin{array} { l } { \delta x } \\ { \delta v } \end{array} \right] }
$$

$$
A ( t ) = \left[ \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { - \omega ^ { 2 } } } & { { 0 } } \end{array} \right] , \quad B ( t ) = \left[ \begin{array} { c c c } { { 0 } } & { { 0 } } & { { 0 } } \\ { { \frac { \omega ^ { 2 } x } { m } } } & { { \frac { - x } { m } } } & { { 0 } } \end{array} \right]
$$

and

$$
\tilde { H } _ { x } = \left[ \begin{array} { l l } { { \underline { { x } } } } & { { 0 } } \\ { { \rho } } & { { 0 } } \\ { { { \underline { { \dot { x } } } } - { \frac { x ^ { 2 } { \dot { x } } } { \rho ^ { 3 } } } } } & { { { \underline { { x } } } } } \\ { { \rho } } & { { { \rho } } } \end{array} \right] , \quad \tilde { H } _ { c } = \left[ \begin{array} { l l l } { { 0 } } & { { 0 } } & { { { \underline { { h } } } } } \\ { { 0 } } & { { 0 } } & { { { \underline { { \dot { \rho } } } } } } \\ { { 0 } } & { { 0 } } & { { - { \frac { x \dot { x } h } { \rho ^ { 3 } } } } } \end{array} \right] .
$$

The solution to Eq. (6.9.4) is given by

$$
\begin{array} { r c l } { x ( t ) } & { = } & { x _ { o } \cos \omega t + \frac { v _ { o } } { \omega } \sin \omega t } \\ { v ( t ) } & { = } & { v _ { o } \cos \omega t - x _ { o } \omega \sin \omega t . } \end{array}
$$

Note that the original differential equation for the state Eq. (6.9.2) is linear; hence the filte r solution (i.e., $c = 0$ ) for

$$
\delta { \mathbf X } ( t ) = \left[ \begin{array} { l } { \delta { \mathbf x } ( t ) } \\ { \delta v ( t ) } \end{array} \right]
$$

is also given by Eq. (6.9.9) when $x _ { 0 }$ and $v _ { 0 }$ are replaced by $\delta x _ { 0 }$ and $\delta v _ { 0 }$ , respectively.

The differential equations for the filter state transition matrix are

$$
{ \dot { \Phi } } ( t , 0 ) = A ( t ) \Phi ( t , 0 ) , \quad \Phi ( 0 , 0 ) = I
$$

and the consider parameter transition matrix equations are

$$
\dot { \theta } ( t , 0 ) = A ( t ) \theta ( t , 0 ) + B ( t ) , \quad \theta ( 0 , 0 ) = 0 .
$$

Solutions to these are given by

$$
\begin{array} { r l r } { \Phi ( t , 0 ) } & { { } = } & { \left[ \begin{array} { c c } { \cos \omega t } & { \frac { 1 } { \omega } \sin \omega t } \\ { - \omega \sin \omega t } & { \cos \omega t } \end{array} \right] } \end{array}
$$

and

$$
\begin{array} { l c l } { { \theta _ { 1 1 } ( t , 0 ) } } & { { = } } & { { \displaystyle \frac { \beta _ { 2 } } { \omega } \sin \omega t + t [ - \beta _ { 2 } \cos \omega t + \beta _ { 1 } \omega \sin \omega t ] } } \\ { { } } & { { } } & { { } } \\ { { \theta _ { 1 2 } ( t , 0 ) } } & { { = } } & { { - \theta _ { 1 1 } ( t , 0 ) \omega ^ { 2 } } } \\ { { } } & { { } } & { { } } \\ { { \theta _ { 1 3 } ( t , 0 ) } } & { { = } } & { { 0 } } \\ { { \theta _ { 2 1 } ( t , 0 ) } } & { { = } } & { { \beta _ { 1 } \omega \sin \omega t + t [ \beta _ { 2 } \omega \sin \omega t + \beta _ { 1 } \omega ^ { 2 } \cos \omega t ] } } \\ { { } } & { { } } & { { } } \\ { { \theta _ { 2 2 } ( t , 0 ) } } & { { = } } & { { - \theta _ { 2 1 } / \omega ^ { 2 } } } \\ { { } } & { { } } & { { } } \\ { { \theta _ { 2 3 } ( t , 0 ) } } & { { = } } & { { 0 } } \end{array}
$$

where

$$
\beta _ { 1 } = \frac { x _ { 0 } } { 2 m } \quad \mathrm { a n d } \quad \beta _ { 2 } = \frac { \dot { x } _ { 0 } } { 2 m } .
$$

Eleven perfect observations of $\rho$ and $\dot { \rho }$ were simulated over a period of 10 seconds at one-second intervals and are given in Chapter 4 (Table 4.8.1), assuming the following values for the system parameters and the initial condition:

$$
\begin{array} { r c l } { k _ { 1 } } & { = } & { 2 . 5 ~ \mathrm { N / m } } \\ { k _ { 2 } } & { = } & { 3 . 7 ~ \mathrm { N / m } } \\ { m } & { = } & { 1 . 5 ~ \mathrm { k g } } \\ { h } & { = } & { 5 . 4 ~ \mathrm { m } } \\ { x _ { 0 } } & { = } & { 3 . 0 ~ \mathrm { m } } \\ { \dot { x } _ { 0 } } & { = } & { 0 . 0 ~ \mathrm { m / s } . } \end{array}
$$

The a priori values used are:

$$
\begin{array} { r } { \bar { \bf X } _ { 0 } = \left[ \begin{array} { c } { 4 . 0 } \\ { 0 . 2 } \end{array} \right] \quad \mathrm { a n d } \quad \overline { { \cal P } } _ { o } = \left[ \begin{array} { c c } { 1 0 0 . 0 } & { 0 } \\ { 0 } & { 1 0 . 0 } \end{array} \right] . } \end{array}
$$

When perfect values of the consider parameters, denoted by the vector $\mathbf { C }$ , are used, the batch processor “reco vers” the true estimate of the state, as shown in the example described in Section 4.8.2. However, when the consider parameters are in error, not only will the estimates of the state parameters deviate from their true values, but these errors will propagate with time. In the following cases the consider covariance is propagated with time under the influence of the indicated covariances on the consider parameters.

# Twenty Percent Error in Consider Parameters

Assume that the values of $m , k _ { 2 }$ , and $h$ actually used in the batch processor are

$$
\mathbf { C } ^ { * } = { \left[ \begin{array} { l } { m } \\ { k _ { 2 } } \\ { h } \end{array} \right] } = { \left[ \begin{array} { l } { 1 . 8 } \\ { 3 . 0 } \\ { 6 . 4 } \end{array} \right] } { \mathrm { ~ ; ~ h e n c e , ~ } } \mathbf { c } = { \left[ \begin{array} { l } { - . 3 } \\ { . 7 } \\ { - 1 } \end{array} \right] } .
$$

$\mathbf { C } ^ { * }$ is approximately 20 percent in error relative to the true values given in Eq. (6.9.13). The corresponding consider covariance is assumed to be:

$$
\overline { { { P } } } _ { c c } = \left[ \begin{array} { c c c } { { 0 . 0 9 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 . 4 9 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 1 } } \end{array} \right] .
$$

The solution for the epoch state using the observations of Table 4.8.1 and the values of the consider parameters given by Eq. (6.9.15) and a priori values given by Eq. (6.9.14) is

$$
\begin{array} { r l r } { \hat { x } _ { 0 } } & { { } = } & { 2 . 3 0 9 \pm 0 . 6 2 3 \mathrm { m } } \\ { \hat { \dot { x } } _ { 0 } } & { { } = } & { - 0 . 7 5 8 \pm 0 . 7 1 2 \mathrm { m / s } . } \end{array}
$$

The error covariance matrices are propagated with time using Eqs. (6.6.10) and (6.6.11) with $\overline { { P } } _ { c c }$ given by Eq. (6.9.16), and the results are shown in Fig. 6.9.1. The upper panel shows the error in the position estimate, and the positive values of the computed standard deviation and the consider standard deviation. The time span includes the measurement period (0–10 sec) and a prediction interval (10–20 sec). The center panel shows the previous three quantities for the velocity component. The computed and the consider covariance between the position and velocity estimates are shown in the lower panel. Note that the consider sigmas are always greater than the computed sigmas. The phase difference between the actual error and consider error is caused by the errors in $m$ and $k _ { 2 }$ , which result in an error in frequency and phase. It is also interesting to note that the state errors are bounded above by the computed sigmas in the measurement interval but not in the prediction interval.

![](images/5c02357bb2e451d1f5a5f5210bb30ade45321943e1803d352ac25cc28a5c6798.jpg)  
Figure 6.9.1: Consider analysis: Spring mass problem, $2 0 \%$ error in consider parameters.

# Five Percent Error in Consider Parameter

In this case, the only change is to $\mathbf { C } ^ { * }$ and $\overline { { P } } _ { c c }$ , with

$$
\mathbf { C } ^ { * } = \left[ \begin{array} { l } { 1 . 6 } \\ { 3 . 5 } \\ { 5 . 7 } \end{array} \right] .
$$

$\mathbf { C } ^ { * }$ is approximately 5 percent in error. The consider covariance is assumed to be:

$$
\overline { { { P } } } _ { c c } = \left[ \begin{array} { c c c } { { 0 . 0 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 . 0 4 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 . 0 9 } } \end{array} \right] .
$$

The batch solution for the epoch state is:

$$
\begin{array} { r l r } { \hat { x } _ { 0 } } & { { } = } & { 2 . 8 7 3 \pm 0 . 5 0 5 } \\ { \hat { \dot { x } } _ { 0 } } & { { } = } & { - 0 . 4 9 9 \pm 0 . 5 1 3 . } \end{array}
$$

The propagation errors and the standard deviations corresponding to this case are shown in Fig. 6.9.2. The results are similar to the previous case, except that the magnitude of error is proportionally smaller.

# 6.10 ERRORS IN THE OBSERVATION NOISE AND A PRIORI STATE COVARIANCES

The effects of errors in the assumed values of the data noise and a priori state covariance matrices for the batch processor can be evaluated as follows. Assume that the values of these matrices used in the batch processor differ from the true values (denoted by $( \quad ) ^ { * } )$ by the matrix $\delta$ ,

$$
\begin{array} { r c l } { { R ^ { * } } } & { { = } } & { { R + \delta R } } \\ { { \overline { { { P } } } _ { 0 } ^ { * } } } & { { = } } & { { \overline { { { P } } } _ { 0 } + \delta \overline { { { P } } } _ { 0 } . } } \end{array}
$$

![](images/0cbeb694c3dc85ae910af8b3092b3eb66edb6a456b6387b72633f68b053089f1.jpg)  
Figure 6.9.2: Consider analysis: spring mass problem, $5 \%$ error in consider parameters.

From Eq. (4.6.1),

$$
\hat { \mathbf { x } } = \left( H ^ { T } R ^ { - 1 } H + \overline { { P } } _ { 0 } ^ { - 1 } \right) ^ { - 1 } \left( H ^ { T } R ^ { - 1 } \mathbf { y } + \overline { { P } } _ { 0 } ^ { - 1 } \overline { { \mathbf { x } } } \right)
$$

where

$$
\begin{array} { r c l } { \overline { { \mathbf { x } } } } & { = } & { \mathbf { x } + \pmb { \eta } } \\ { \mathbf { y } } & { = } & { H \mathbf { x } + \epsilon } \end{array}
$$

and

$$
\begin{array} { l } { { E [ \eta \eta ^ { T } ] = \overline { { { \cal P } } } _ { 0 } ^ { * } } } \\ { { { } } } \\ { { E [ \epsilon \epsilon ^ { T } ] = R ^ { * } . } } \end{array}
$$

Evaluating the estimation error covariance using the assumed values of $R$ and $\overline { { P } } _ { 0 }$ results in

$$
\hat { \mathbf { x } } = \big [ H ^ { T } R ^ { - 1 } H + \overline { { P } } _ { 0 } ^ { - 1 } \big ] ^ { - 1 } \big [ H ^ { T } R ^ { - 1 } ( H _ { x } + \epsilon ) + \overline { { P } } _ { 0 } ^ { - 1 } ( \mathbf { x } + \eta ) \big ]
$$

or

$$
\begin{array} { r } { \hat { \mathbf { x } } - \mathbf { x } = \left[ H ^ { T } R ^ { - 1 } H + \overline { { P } } _ { 0 } ^ { - 1 } \right] ^ { - 1 } \left[ H ^ { T } R ^ { - 1 } \boldsymbol { \epsilon } + \overline { { P } } _ { 0 } ^ { - 1 } \pmb { \eta } \right] . } \end{array}
$$

Assuming $E [ \epsilon \eta ^ { T } ] = 0$ , we have

$$
\begin{array} { l c l } { { P _ { c } } } & { { = } } & { { E \bigl [ ( \hat { \mathbf { x } } - \mathbf { x } ) ( \hat { \mathbf { x } } - \mathbf { x } ) ^ { T } \bigr ] } } \\ { { } } & { { = } } & { { \bigl [ H ^ { T } R ^ { - 1 } H + \overline { { { P } } } _ { 0 } ^ { - 1 } \bigr ] ^ { - 1 } \bigl [ H ^ { T } R ^ { - 1 } E [ \epsilon \epsilon ^ { T } ] R ^ { - 1 } H \bigr ] } } \\ { { } } & { { } } & { { + } } \\ { { } } & { { = } } & { { P \bigl [ H ^ { T } R ^ { - 1 } R ^ { \ast } R ^ { - 1 } H + \overline { { { P } } } _ { 0 } ^ { - 1 } \overline { { { P } } } _ { 0 } ^ { - 1 } H + \overline { { { P } } } _ { 0 } ^ { - 1 } \bigr ] ^ { - 1 } } } \\ { { } } & { { = } } & { { P \bigl [ H ^ { T } R ^ { - 1 } R ^ { \ast } R ^ { - 1 } H + \overline { { { P } } } _ { 0 } ^ { - 1 } \overline { { { P } } } _ { 0 } ^ { \ast } \overline { { { P } } } _ { 0 } ^ { - 1 } \bigr ] P . } } \end{array}
$$

Substituting Eqs. (6.10.1) and (6.10.2) for $R ^ { * }$ and $\overline { { P } } _ { 0 } ^ { * }$ yields

$$
P _ { c } = P + P \big [ H ^ { T } R ^ { - 1 } \delta R R ^ { - 1 } H + \overline { { P } } _ { 0 } ^ { - 1 } \delta \overline { { P } } _ { 0 } \overline { { P } } _ { 0 } ^ { - 1 } \big ] P .
$$

The second term in Eq. (6.10.10) is the contribution to the consider covariance from errors in the data noise and $a$ priori state covariance matrices.

# 6.11 ERRORS IN PROCESS NOISE, OBSERVATION NOISE, AND STATE COVARIANCE

The effects of errors in the process noise, observation noise, and a priori state covariance matrices can be evaluated using a sequential or Kalman fil ter algorithm. Following Heffes (1996), assume that the values of these quantities used

in the filt er are given by $Q , R$ , and $\overline { { P } } _ { 0 }$ . Also,

$$
\begin{array} { l c l } { { Q ^ { * } } } & { { = } } & { { Q + \delta Q } } \\ { { } } & { { } } & { { } } \\ { { R ^ { * } } } & { { = } } & { { R + \delta R } } \\ { { } } & { { } } & { { } } \\ { { \overline { { { P } } } _ { 0 } ^ { * } } } & { { = } } & { { \overline { { { P } } } _ { 0 } + \delta \overline { { { P } } } _ { 0 } } } \end{array}
$$

where $( \quad ) ^ { * }$ represents the optimal or true value, and $\delta$ denotes the error in the assumed value.

We wish to find the covariance associated with the actual state error. The actual error in the estimated states at time $t _ { k }$ is given by

$$
\delta \mathbf { x } _ { k } = \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k }
$$

where

$$
\begin{array} { r c l } { { \hat { \mathbf { x } } _ { k } } } & { { = } } & { { \overline { { \mathbf { x } } } _ { k } + K _ { k } ( \mathbf { y } _ { k } - \widetilde { H } _ { k } \overline { { \mathbf { x } } } _ { k } ) } } \\ { { K _ { k } } } & { { = } } & { { \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } ( \widetilde { H } _ { k } \overline { { P } } _ { k } \widetilde { H } ^ { T } + R ) ^ { - 1 } } } \\ { { \mathrm { a n d } } } & { { } } & { { } } \\ { { \mathbf { y } _ { k } } } & { { = } } & { { \widetilde { H } _ { k } \mathbf { x } _ { k } + \epsilon _ { k } . } } \end{array}
$$

Here $\hat { \mathbf { x } } _ { k }$ is the state estimate obtained using $Q , R$ , and $P _ { 0 }$ in Eq. (6.11.3), and $\mathbf { x } _ { k }$ is the true value of the state at $t _ { k }$ .

Substituting Eqs. (6.11.3) and (6.11.5) into Eq. (6.11.2) yields

$$
\begin{array} { l l l } { \delta { \mathbf x } _ { k } } & { = } & { \overline { { { \mathbf x } } } _ { k } + K _ { k } ( \widetilde { H } _ { k } { \mathbf x } _ { k } + \epsilon _ { k } - \widetilde { H } _ { k } \overline { { { \mathbf x } } } _ { k } ) - { \mathbf x } _ { k } } \\ & { = } & { ( I - K _ { k } \widetilde { H } _ { k } ) ( \overline { { { \mathbf x } } } _ { k } - { \mathbf x } _ { k } ) + K _ { k } \epsilon _ { k } . } \end{array}
$$

The covariance of the actual estimation error is

$$
\begin{array} { l l l } { { P _ { k } } } & { { \equiv } } & { { E \big [ \delta { \mathbf { x } } _ { k } \delta { \mathbf { x } } _ { k } ^ { T } \big ] } } \\ { { } } & { { = } } & { { \big ( I - K _ { k } { \widetilde { H } } _ { k } \big ) \overline { { { P } } } _ { k } \big ( I - K _ { k } { \widetilde { H } } _ { k } \big ) ^ { T } + K _ { k } R ^ { * } K _ { k } ^ { T } } } \end{array}
$$

where

$$
\begin{array} { r } { \overline { { P } } _ { k } \equiv E \big [ \delta \overline { { \mathbf { x } } } _ { k } \delta \overline { { \mathbf { x } } } _ { k } ^ { T } \big ] = E \big [ ( \overline { { \mathbf { x } } } _ { k } - \mathbf { x } _ { k } ) ( \overline { { \mathbf { x } } } _ { k } - \mathbf { x } _ { k } ) ^ { T } \big ] . } \end{array}
$$

The equation relating $\overline { { P } } _ { k }$ to $P _ { k - 1 }$ is found by using the expressions that relate the state at time $t _ { k - 1 }$ to the state at $t _ { k }$ ,

$$
\begin{array} { r c l } { \overline { { \mathbf { x } } } _ { k } } & { = } & { \Phi ( t _ { k } , t _ { k - 1 } ) \hat { \mathbf { x } } _ { k - 1 } } \\ { \mathbf { x } _ { k } } & { = } & { \Phi ( t _ { k } , t _ { k - 1 } ) \mathbf { x } _ { k - 1 } + \Gamma ( t _ { k } , t _ { k - 1 } ) \mathbf { u } _ { k - 1 } . } \end{array}
$$

Thus,

$$
\begin{array} { r c l } { \delta { \overline { { \mathbf { x } } } } _ { k } } & { = } & { { \overline { { \mathbf { x } } } } _ { k } - \mathbf { x } _ { k } } \\ & { = } & { \Phi ( t _ { k } , t _ { k - 1 } ) { \hat { \mathbf { x } } } _ { k - 1 } - \Phi ( t _ { k } , t _ { k - 1 } ) \mathbf { x } _ { k - 1 } - \Gamma ( t _ { k } , t _ { k - 1 } ) \mathbf { u } _ { k - 1 } } \\ & { = } & { \Phi ( t _ { k } , t _ { k - 1 } ) ( { \hat { \mathbf { x } } } _ { k - 1 } - \mathbf { x } _ { k - 1 } ) - \Gamma ( t _ { k } , t _ { k - 1 } ) \mathbf { u } _ { k - 1 } . \qquad ( 6 . } \end{array}
$$

Substituting this into Eq. (6.11.8) yields

$$
\begin{array} { r c l } { { \overline { { { P } } } _ { k } } } & { { = } } & { { \Phi ( t _ { k } , t _ { k - 1 } ) P _ { k - 1 } \Phi ^ { T } \left( t _ { k } , t _ { k - 1 } \right) } } \\ { { } } & { { + } } & { { \Gamma ( t _ { k } , t _ { k - 1 } ) Q _ { k - 1 } ^ { * } \Gamma ^ { T } ( t _ { k } , t _ { k - 1 } ) } } \end{array}
$$

where $E [ ( \widehat { \mathbf { x } } _ { k - 1 } - \mathbf { x } _ { k - 1 } ) \mathbf { u } _ { k - 1 } ^ { T } \Gamma ^ { T } ( t _ { k } , t _ { k - 1 } ) ] = 0$ because $\mathbf x _ { k - 1 }$ is dependent on ${ \bf u } _ { k - 2 }$ but not $\mathbf { u } _ { k - 1 }$ .

Hence, the covariance of the actual error given by Eqs. (6.11.12) and (6.11.7) is

$$
\begin{array} { r c l } { { \overline { { { P } } } _ { k _ { a } } } } & { { = } } & { { \Phi ( t _ { k } , t _ { k - 1 } ) P _ { k - 1 _ { a } } \Phi ^ { T } ( t _ { k } , t _ { k - 1 } ) } } \\ { { } } & { { } } & { { + \Gamma ( t _ { k } , t _ { k - 1 } ) Q _ { k - 1 } ^ { * } \Gamma ^ { T } ( t _ { k } , t _ { k - 1 } ) } } \\ { { P _ { k _ { a } } } } & { { = } } & { { ( I - K _ { k } \widetilde { H } _ { k } ) \overline { { { P } } } _ { k _ { a } } ( I - K _ { k } \widetilde { H } _ { k } ) ^ { T } + K _ { k } R ^ { * } K _ { k } ^ { T } . } } \end{array}
$$

The recursion is initiated with $\overline { { \boldsymbol { P } } } _ { 0 _ { a } } = \overline { { \boldsymbol { P } } } _ { 0 } ^ { * }$ .

The gain matrix, $K _ { k }$ , at each stage is computed by using the suboptimal $\overline { { P } }$ and $R$ , and is initiated with $\overline { { P } } _ { 0 } \colon K _ { k }$ is given by

$$
\begin{array} { r } { K _ { k } = \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } ( \widetilde { H } _ { k } \overline { { P } } _ { k } \widetilde { H } _ { k } ^ { T } + R ) ^ { - 1 } . } \end{array}
$$

The suboptimal values of $\overline { { P } } _ { k }$ and $P _ { k }$ are given by

$$
\begin{array} { r c l } { { { \overline { { { P } } } } _ { k } } } & { { = } } & { { \Phi ( t _ { k } , t _ { k - 1 } ) P _ { k - 1 } \Phi ^ { T } ( t _ { k } , t _ { k - 1 } ) } } \\ { { } } & { { } } & { { + \Gamma ( t _ { k } , t _ { k - 1 } ) Q _ { k } \Gamma ^ { T } ( t _ { k } , t _ { k - 1 } ) } } \\ { { P _ { k } } } & { { = } } & { { ( I - K _ { k } { \widetilde { H } } _ { k } ) { \overline { { { P } } } } _ { k } . } } \end{array}
$$

Hence, there will be three covariance matrices one can compute using Eqs. (6.11.13) and (6.11.14):

1. The optimal value of $P$ based on $\overline { { P } } _ { 0 } ^ { * } , Q ^ { * } , R ^ { * }$ .

2. The actual value of $P$ determined by using $\overline { { P } } _ { 0 } ^ { * }$ , $Q ^ { * }$ , $R ^ { * }$ and $\overline { { P } } _ { 0 }$ , $Q$ , and $R$

3. The suboptimal value of $P$ determined from $\overline { { P } } _ { 0 }$ , $Q$ , and $R$ . Note that the suboptimal value of $\overline { { P } } _ { k }$ must be computed in order to determine the actual value of $P _ { k }$ .

# 6.12 COVARIANCE ANALYSIS AND ORTHOGONAL TRANSFORMATIONS

The consider covariance formulation can also be developed in square-root form by using orthogonal transformations. Consider the dynamic and measurement models given by Eqs. (6.5.8) and (6.5.18):

$$
\begin{array} { r c l } { { { \bf x } ( t ) } } & { { = } } & { { \Phi ( t , t _ { k } ) { \bf x } _ { k } + \theta ( t , t _ { k } ) { \bf c } _ { k } } } \\ { { { \bf y } _ { j } } } & { { = } } & { { \tilde { H } _ { x _ { j } } { \bf x } _ { j } + \widetilde { H } _ { c _ { j } } { \bf c } + \epsilon _ { j } , \quad j = 1 , \ldots , \ell . } } \end{array}
$$

By substituting Eq. (6.12.1) into Eq. (6.12.2) (see Eq. (6.5.22)), this set can be reduced to

$$
\begin{array} { r } { { \bf y } _ { j } = H _ { x _ { j } } { \bf x } _ { k } + H _ { c _ { j } } { \bf c } + \epsilon _ { j } , \quad j = 1 , \ldots , \ell } \end{array}
$$

where

$$
\begin{array} { l l l } { { H _ { x _ { j } } } } & { { = } } & { { \tilde { H } _ { x _ { j } } \Phi ( t _ { j } , t _ { k } ) } } \\ { { H _ { c _ { j } } } } & { { = } } & { { \tilde { H } _ { x _ { j } } \theta ( t _ { j } , t _ { k } ) + \tilde { H } _ { c _ { j } } , \quad j = 1 , \dots , \ell . } } \end{array}
$$

Then the set of $\ell$ observations can be combined as

$$
{ \bf y } = H _ { x } { \bf x } _ { k } + H _ { c } { \bf c } + \epsilon .
$$

where y, $H _ { x }$ , $H _ { c }$ , and $\epsilon$ are defined in Eq. (6.5.25).

We next need to write the a priori information on the $n$ -vector, $\mathbf { x }$ , and the $q$ -vector, $\mathbf { c }$ , in terms of a data equation. Given $a$ priori values $\bar { \bf x }$ and c¯, we may write

$$
\left[ \begin{array} { l } { \bar { \mathbf { x } } } \\ { \bar { \mathbf { c } } } \end{array} \right] = \left[ \begin{array} { l } { \mathbf { x } } \\ { \mathbf { c } } \end{array} \right] + \left[ \begin{array} { l } { \boldsymbol { \eta } } \\ { \boldsymbol { \beta } } \end{array} \right]
$$

where $\mathbf { x }$ and $\mathbf { c }$ are the true values. $\eta$ and $\beta$ have known mean and covariance,

$$
\begin{array} { r l r } { E [ \eta ] } & { = } & { E [ \beta ] = 0 } \\ { \overline { { P } } } & { = } & { E \left[ \left[ \begin{array} { l } { \eta } \\ { \beta } \end{array} \right] \left[ \eta ^ { T } \beta ^ { T } \right] \right] = E \left[ \begin{array} { l l } { \eta \eta ^ { T } } & { \eta \beta ^ { T } } \\ { \beta ^ { T } \eta } & { \beta \beta ^ { T } } \end{array} \right] } \\ & { = } & { \left[ \begin{array} { l l } { \overline { { P } } _ { x } } & { \overline { { P } } _ { x c } } \\ { \overline { { P } } _ { c x } } & { \overline { { P } } _ { c c } } \end{array} \right] . } \end{array}
$$

We may now determine the upper triangular square root of the inverse of $\overline { { P } }$ with

a Cholesky decomposition

$$
\mathrm { C h o l } \quad \left[ \begin{array} { l l } { \overline { { P } } _ { x } } & { \overline { { P } } _ { x c } } \\ { \overline { { P } } _ { c x } } & { \overline { { P } } _ { c c } } \end{array} \right] ^ { - 1 } \equiv \left[ \begin{array} { l l } { \overline { { R } } _ { x } } & { \overline { { R } } _ { x c } } \\ { 0 } & { \overline { { R } } _ { c } } \end{array} \right] .
$$

Multiplying Eq. (6.12.5) by Eq. (6.12.7) in order to write it as a data equation yields

$$
\begin{array} { r l r } { \left[ \begin{array} { l l } { \overline { { R } } _ { x } } & { \overline { { R } } _ { x c } } \\ { 0 } & { \overline { { R } } _ { c } } \end{array} \right] \left[ \begin{array} { l } { \overline { { \bf x } } } \\ { \overline { { \bf c } } } \end{array} \right] } & { = } & { \left[ \begin{array} { l l } { \overline { { R } } _ { x } } & { \overline { { R } } _ { x c } } \\ { 0 } & { \overline { { R } } _ { c } } \end{array} \right] \left[ \begin{array} { l } { { \bf x } } \\ { { \bf c } } \end{array} \right] } \\ & { + } & { \left[ \begin{array} { l l } { \overline { { R } } _ { x } } & { \overline { { R } } _ { x c } } \\ { 0 } & { \overline { { R } } _ { c } } \end{array} \right] \left[ \begin{array} { l } { \eta } \\ { \beta } \end{array} \right] . } \end{array}
$$

Because we do not intend to estimate c, we need to deal with only the first row of Eq. (6.12.8). Define

$$
\begin{array} { r c l } { \overline { { \mathbf { b } } } _ { c } } & { \equiv } & { \overline { { R } } _ { c } \overline { { \mathbf { c } } } } \\ { \overline { { \mathbf { b } } } } & { \equiv } & { \overline { { R } } _ { x } \overline { { \mathbf { x } } } + \overline { { R } } _ { x c } \overline { { \mathbf { c } } } } \\ { \overline { { \boldsymbol { \eta } } } } & { \equiv } & { \overline { { R } } _ { x } \boldsymbol { \eta } + \overline { { R } } _ { x c } \beta . } \end{array}
$$

We will not use the first of Eq. (6.12.9) unless we estimate c.

The first row of Eq. (6.12.8) becomes

$$
\begin{array} { r } { \overline { { \mathbf { b } } } = \left[ \overline { { R } } _ { x } \overline { { R } } _ { x c } \right] \left[ \begin{array} { l } { \mathbf { x } } \\ { \mathbf { c } } \end{array} \right] + \overline { { \pmb { \eta } } } . } \end{array}
$$

Using Eqs. (6.12.10) and (6.12.4) we may write the array to be upper triangularized,

$$
\begin{array} { r l } &  \overbrace { \left[ \begin{array} { l l l } { \overline { { R } } _ { x } } & { \overline { { R } } _ { x } } & { \overline { { \mathbf { b } } } } \\ { H _ { x } } & { H _ { c } } & { \mathbf { y } } \end{array} \right] } ^ { n } \} _ { \begin{array} { l } { \} \end{array} } } \end{array}
$$

We need only partially triangularize Eq. (6.12.11) by nulling the terms below the

diagonal of the first $n$ columns $\dot { n }$ is the dimension of $\mathbf { x }$ ). Hence

$$
\begin{array}{c} \begin{array} { r l r } & { } & { \overbrace { \vphantom { \int } \overline { { R } } _ { x } } ^ { n } \overbrace { R } _ { x c } ^ { q } \overbrace { \mathrm { ~ \bf ~ b ~ } } ^ { 1 } } \\ & { } & { T [ \begin{array} { c c c } { \overline { { R } } _ { x } } & { \overline { { R } } _ { x c } } & { \overline { { \mathrm { \bf ~ b ~ } } } } \\ { H _ { x } } & { H _ { c } } & { \mathrm { \bf ~ y ~ } } \end{array} ] \} ^ { n } = \overbrace { \int } ^ { \mathrm { \Large ~ [ ~  ~ \hat { R } _ { x } ~ \hat { R } _ { x c } ~ \hat { \mathrm { \bf ~ b ~ } } } } \ \overbrace { \mathrm { \bf ~ b } _ { c } } ^ { 1 } } \end{array} ] ^ { \mathrm { \Large ~ \textstyle ~  ~ \} n } } \end{array}
$$

There are $\ell - q$ additional rows on the right-hand side of Eq. (6.12.12), which are not needed and are not shown here. Also, the terms $\widetilde { R } _ { c }$ and $\widetilde { \mathbf { b } } _ { c }$ are not needed to compute the consider covariance and are needed only if $\mathbf { c }$ is to be estimated. For consider covariance analysis $\overline { { \mathbf { c } } }$ is used wherever an estimate of $\mathbf { c }$ is needed. The first row of Eq. (6.12.12) yields

$$
\hat { R } _ { x } { \bf x } + \hat { R } _ { x c } \overline { { { \bf c } } } = \hat { { \bf b } } .
$$

In keeping with the notation of Section 6.3 and Eq. (6.3.70) we will refer to the estimate of $\mathbf { x }$ obtained from Eq. (6.12.13) as $\hat { \mathbf { x } } _ { c }$ ; accordingly,

$$
\hat { \mathbf { x } } _ { c } = \hat { R } _ { x } ^ { - 1 } \hat { \mathbf { b } } - \hat { R } _ { x } ^ { - 1 } \hat { R } _ { x c } \overline { { \mathbf { c } } } .
$$

The estimate of $\mathbf { x }$ obtained by ignoring $\overline { { \mathbf { c } } }$ is called the computed estimate of $\mathbf { x }$ and is given by

$$
\hat { \mathbf { x } } = \hat { R } _ { x } ^ { - 1 } \hat { \mathbf { b } } .
$$

Hence,

$$
\begin{array} { r } { \hat { \bf x } _ { c } = \hat { \bf x } - \hat { R } _ { x } ^ { - 1 } \hat { R } _ { x c } \overline { { \bf c } } . } \end{array}
$$

Comparing Eq. (6.12.16) with Eq. (6.4.5) or by recalling that the sensitivity matrix is given by

$$
S = \frac { \partial \hat { \mathbf { x } } _ { c } } { \partial \overline { { \mathbf { c } } } } ,
$$

we have

$$
S = - \hat { R } _ { x } ^ { - 1 } \hat { R } _ { x c }
$$

and Eq. (6.12.16) may be written as

$$
\hat { \mathbf { x } } _ { c } = \hat { \mathbf { x } } + S \overline { { \mathbf { c } } } .
$$

From Eq. (6.12.15) the data noise covariance matrix is given by

$$
P = ( \hat { R } _ { x } ^ { T } \hat { R } _ { x } ) ^ { - 1 } = \hat { R } _ { x } ^ { - 1 } \hat { R } _ { x } ^ { - T }
$$

and the consider covariance for $\mathbf { x }$ is (see Eq. (6.3.64))

$$
P _ { c } = P + S \overline { { { P } } } _ { c c } S ^ { T } .
$$

The cross covariance is given by Eq. (6.3.65)

$$
P _ { x c } = S \overline { { P } } _ { c c }
$$

and the complete consider covariance matrix is given by Eq. (6.3.67)

$$
{ \bf P } _ { c } = \left[ { P _ { c } \frac { P _ { x c } } { P } } \right] .
$$

We could also determine the consider covariance directly by replacing $\widetilde { R } _ { c }$ with $\overline { { R } } _ { c }$ in Eq. (6.12.12). Then,

$$
\begin{array} { r l } & { \mathbf { P } _ { \mathrm { c } } = \left[ \begin{array} { l l } { \hat { H } _ { x } } & { \hat { H } _ { x c } } \\ { 0 } & { \hat { H } _ { c } } \end{array} \right] ^ { - 1 } \left[ \begin{array} { l l } { \hat { H } _ { x } ^ { T } } & { 0 } \\ { \hat { R } _ { c } ^ { T } } & { \hat { R } _ { c } ^ { T } } \end{array} \right] ^ { - 1 } } & { ( 6 . 1 \mathbf { \hat { z } } ) } \\ & { \quad = \left[ \begin{array} { l l } { \hat { H } _ { x } ^ { - 1 } } & { - \hat { H } _ { x } ^ { - 1 } \hat { H } _ { x c } \overline { { R } } _ { c } ^ { - 1 } } \\ { 0 } & { \hat { H } _ { c } ^ { - 1 } } \end{array} \right] \left[ \begin{array} { l } { \hat { H } _ { x } ^ { - T } } \\ { - \hat { H } _ { x } ^ { - T } \hat { H } _ { x c } ^ { T } \hat { H } _ { x c } ^ { - T } } & { \hat { H } _ { c } ^ { - T } } \end{array} \right] } \\ & { \quad = \left[ \begin{array} { l l } { \hat { H } _ { x } ^ { - 1 } \hat { H } _ { x } ^ { - T } + S \overline { { R } } _ { c } ^ { - 1 } \overline { { R } } _ { c } ^ { - T } S ^ { T } \ } & { S \overline { { R } } _ { c } ^ { - 1 } \overline { { R } } _ { c } ^ { - T } } \\ { \overline { { R } } _ { c } ^ { - 1 } \overline { { R } } _ { c } ^ { - T } S ^ { T } \ } & { \overline { { R } } _ { c } ^ { - 1 } \overline { { R } } _ { c } ^ { - T } } \end{array} \right] } \\ & { \quad = \left[ \begin{array} { l l } { P _ { c } } & { P _ { c } } \\ { P _ { c } } & { \frac { P _ { c } } { P _ { c } } } \end{array} \right] . } \end{array}
$$

In component form

$$
\begin{array} { r l } & { \quad P _ { c } = \hat { R } _ { x } ^ { - 1 } \hat { R } _ { x } ^ { - T } + S \overline { { P } } _ { c c } S ^ { T } } \\ & { \quad P _ { x c } = S \overline { { P } } _ { c c } } \\ & { \quad \overline { { P } } _ { c c } = \overline { { R } } _ { c } ^ { - 1 } \overline { { R } } _ { c } ^ { - T } . } \end{array}
$$

If we wish to estimate c we would combine $\widetilde { R } _ { c }$ and $\widetilde { \mathbf { b } } _ { \mathbf { c } }$ from Eq. (6.12.12) with the a priori information on c given by the first of Eq. (6.12.9). We then perform a series of orthogonal transformations on

$$
T \left[ \begin{array} { l } { \overline { { R } } _ { c } \mathbf { \widehat { b } _ { c } } } \\ { \hat { R } _ { c } \mathbf { \widehat { b } _ { c } } } \end{array} \right] = \left[ \begin{array} { l } { \hat { R } _ { c } \hat { \mathbf { b } } _ { \mathbf { c } } } \\ { 0 \textbf { \textit { e } } } \end{array} \right]
$$

and

$$
\hat { \mathbf { c } } = \hat { R } _ { c } ^ { - 1 } \hat { \mathbf { b } } _ { \mathbf { c } }
$$

the associated estimation error covariance for $\hat { \mathbf { c } }$ is

$$
P _ { c c } = \hat { R } _ { c } ^ { - 1 } \hat { R } _ { c } ^ { - T } .
$$

We could now replace $\overline { { \mathbf { c } } }$ with cˆ in Eq. (6.12.16) to obtain the proper estimate for $\mathbf { x }$ and replace $\overline { { R } } _ { c }$ with $\hat { R } _ { c }$ in the fir st of Eq. (6.12.23) to obtain the corresponding consider covariance matrices. This will result in $\overline { { P } } _ { c c }$ being replaced by $P _ { c c }$ in Eqs. (6.12.24) and (6.12.25).

The computational algorithm for consider covariance analysis using orthogonal transformations is as follows.

Given a priori information ${ \overline { { P } } } _ { x }$ , $\overline { { P } } _ { x c }$ , and $\overline { { P } } _ { c c }$ at an epoch time, $t _ { 0 }$ , and observations $\mathbf { y } _ { j } = \tilde { H } _ { x _ { j } } \mathbf { x } _ { j } + \tilde { H } _ { c _ { j } } \mathbf { c } + \epsilon _ { j } \quad j = 1 , \ldots , \ell .$

1. Use a Cholesky decompostion to compute the upper triangular matrix of Eq. (6.12.7). 2. Using the procedure indicated in Eqs. (6.12.8) through (6.12.10), form the matrix indicated by Eq. (6.12.11). The observations may be processed one at a time, in small batches, or simultaneously (see Chapter 5). 3. Partially upper triangularize the matrix of Eq. (6.12.11) by nulling the terms below the diagonal of the first $n$ columns to yield the results of Eq. (6.12.12). 4. After processing all observations replace $\widetilde { R } _ { c }$ in Eq. (6.12.12) with the $a$ priori value $\overline { { R } } _ { c }$ and evaluate Eq. (6.12.23) to obtain $\mathbf { P } _ { c }$ .

Note that if only a consider covariance is needed, and no estimation is to be done, the last column of Eq. (6.12.12) containing $\overline { { \mathbf { b } } }$ and $\mathbf { y }$ may be eliminated since the a priori state and the actual values of the measurements do not affect the estimation error covariance.

More extensive treatment of the square-root formulations of the covariance analysis problem including the effects of system model errors, errors in the $a$ priori statistics, and errors in correlated process noise can be found in Curkendall (1972), Bierman (1977), Thornton (1976), and Jazwinski (1970).

# 6.13 REFERENCES

Bierman, G. J., Factorization Methods for Discrete Sequential Estimation, Academic Press, New York, 1977.

Curkendall, D. W., Problems in estimation theory with applications to orbit determination, UCLA-ENG-7275, UCLA School Engr. and Appl. Sci., Los Angeles, CA, September 1972.

Heffes, H., “The effects of erroneous models on the Kalman filter response”, Trans. Auto. Cont., Vol. AC-11, pp. 541–543, July 1966.

Jazwinski, A. H., Stochastic Processes and Filtering Theory, Academic Press, New York, 1970.

Thornton, C. L., Triangular covariance factorizations for Kalman filt ering, Technical Memorandum, 33–798, Jet Propulsion Laboratory, Pasadena, CA, October 15, 1976.

# 6.14 EXERCISES

1. Map the consider covariance, $\mathbf { P } _ { c _ { 0 } }$ , for the batch algorithm from $t _ { 0 }$ to $t _ { 1 }$ for Example 6.8. Now map $\mathbf { P } _ { c _ { 2 } }$ , the result at $t _ { 2 }$ from the sequential algorithm to $t _ { 1 }$ and show that it agrees with the batch result.

Answer:

$$
\mathbf { P } _ { c _ { 1 } } = \left[ \begin{array} { c c c c } { \frac { 8 0 + 2 7 \mathrm { I I } } { 3 0 0 } } & { \frac { 2 0 - 2 7 \mathrm { I I } } { 3 0 0 } } & { - \frac { 3 \mathrm { I I } } { 1 0 } } \\ { \frac { 2 0 - 2 7 \mathrm { I I } } { 3 0 0 } } & { \frac { 8 0 + 2 7 \mathrm { I I } } { 3 0 0 } } & { \frac { 3 \mathrm { I I } } { 1 0 } } \\ { - \frac { 3 \mathrm { I I } } { 1 0 } } & { \frac { 3 \mathrm { I I } } { 1 0 } } & { \mathrm { I I } } \end{array} \right]
$$

2. Compute the consider covariance for Example 6.8 at $t = 0$ using the square root formulation of Section 6.12. Compare your results to those given in Section 6.8.

3. Beginning with Eq. (6.3.38), derive the alternate equation for $P _ { x x }$ given by Eq. (6.3.41).

4. Beginning with Eqs. (6.6.3) and (6.6.4), derive Eqs. (6.6.6) and (6.6.11).

5. Given the pendulum problem shown here. Assume that $\theta _ { 0 }$ and $\dot { \theta } _ { 0 }$ are to be estimated, that the observation is range magnitude, $\rho$ , and $x _ { 0 }$ and $g$ are to be considered.

![](images/765f19b25c07a653f025cafa72677efd1a832529240e80970f75958a804ec8b9.jpg)

Assume: $\sigma ( x _ { 0 } ) = \sigma ( g ) = \sigma ( \rho ) = 1$ , and small oscillations so that the equation of motion is linear.

(a) Define: $\Phi ( t , t _ { 0 } ) , \theta ( t , t _ { 0 } ) , H _ { x } , H _ { c } .$ .

(b) Assuming $\sqrt { g / l } \ = \ 1 0$ and observations are taken at $t = 0 , 1 , 2 ,$ , compute the data noise covariance, the sensitivity, perturbation, and consider covariance matrices. Discuss the interpretation of these matrices. Assume $x _ { 0 } = \ell = 1$ , ${ \overline { { P } } } = R = I$ , $\theta _ { 0 } = 0 . 0 1$ rad, and $\dot { \theta } _ { 0 } = 0$ .

Answer:

6. Examine the problem of estimating the position and velocity of a spacecraft in low Earth orbit from ground-based range measurements. The dynamic model is chosen as a simple “flat Earth.” Assume range measurements are taken from a single station. Derive the expression for the consider covariance matrix for the estimated and consider parameters shown.

Estimate: $X , Y , \dot { X } , \dot { Y }$ Consider: $g , X _ { s } , Y _ { s }$ Observe: $\rho$

![](images/583a75c2b99e702d4c7e7560ce1efc90a30b2e4def3f1f9325d869497b607b3d.jpg)

7. A vehicle travels in a straight line according to the following equation:

$$
u ( t ) = u _ { 0 } + e t + f t ^ { 2 }
$$

where

$$
\begin{array} { l } { { u = \mathrm { d i s t a n c e ~ f r o m ~ o r i g i n } } } \\ { { \ } } \\ { { t = \mathrm { t i m e } } } \\ { { \ } } \\ { { e , f = \mathrm { c o n s t a n t s } . } } \end{array}
$$

A tracking station location a distance $s$ from the origin takes range measurements $\rho$ .

![](images/b4dd03c6564c09fc55f5c300263ae651530130412e62141f32ec99392d043e79.jpg)

The true range at time $t$ is

$$
\rho ( t ) = u ( t ) + s .
$$

The observed range, $y ( t )$ , has some error $\epsilon ( t )$ :

$$
\begin{array} { c } { { y ( t ) = \rho ( t ) + \epsilon ( t ) } } \\ { { = u ( t ) + s + \epsilon ( t ) . } } \end{array}
$$

Assume that we wish to estimate $u ( t _ { 0 } ) = u _ { 0 }$ and $e$ , and consider $s$ and $f$ . The following observations with measurement noise of zero mean and unit variance are given.

<table><tr><td>t</td><td>y(t)</td></tr><tr><td>0</td><td>1.5</td></tr><tr><td>1</td><td>10.8</td></tr><tr><td>2</td><td>24.8</td></tr></table>

Compute $\hat { u } _ { 0 }$ , $\hat { e }$ , the computed and consider covariance matrices, and the sensitivity and perturbation matrix.

Answer:

$$
\begin{array} { r l } & { \left[ \hat { u } _ { o } \right] = \left[ 2 . 7 6 \right] , } \\ & { \left[ \hat { e } \right] = \left[ 8 . 6 9 \right] , } \\ & { \left[ \begin{array} { c c c c c } { 0 . 8 0 } & { 0 . 2 0 } & { - 0 . 6 0 } & { - 0 . 2 0 } \\ { 0 . 2 0 } & { 2 . 2 7 } & { - 0 . 2 0 } & { - 1 . 4 0 } \\ { - 0 . 6 0 } & { - 0 . 2 0 } & { 1 . 0 } & { 0 . 0 } \\ { - 0 . 2 0 } & { - 1 . 4 0 } & { 0 . 0 } & { 1 . 0 } \end{array} \right] } \end{array}
$$

8. Work the spring-mass problem of Example 6.9. Assume $k _ { 1 }$ and $k _ { 2 }$ are known exactly; estimate $x _ { 0 }$ , and $v _ { 0 }$ and consider a 20 percent error in $h$ .

9. Work Exercise 8 using the orthogonal transformation procedure of Section 6.12.

# Appendix A

# Probability and Statistics

# A.1 INTRODUCTION

A random variable $X$ is a real-valued function associated with the (chance) outcome of an experiment. That is, to each possible outcome of the experiment, we associate a real number $x$ . The collection of numbers $x _ { i }$ is called the domain of the random variable $X$ . A number $x$ is referred to as a possible value or realization or sample value of the random variable $X$ . Generally for this appendix, uppercase letters will represent random variables and lowercase letters will represent numerical values or realizations of the random variable.

Example 1:   
A coin is flipped $n$ times, let $X$ denote the number of times heads appears. The domain of $X$ is the set of numbers

$$
\left\{ x = 0 , 1 , \ldots , n \right\} .
$$

Example 2:

A point on the surface of the Earth is chosen at random. Let $X$ and $Y$ denote its latitude and longitude. The domain of the random variable $X$ and $Y$ is the pair of numbers

$$
\left\{ X , Y , - \pi / 2 \leq X \leq \pi / 2 , 0 \leq Y \leq 2 \pi \right\} .
$$

These two examples indicate the two types of random variables, discrete and continuous. The discrete random variable $X$ has as its domain or possible outcomes the finit e number of real numbers $x _ { 1 } , x _ { 2 } \ldots x _ { n }$ (see Example 1). For a continuous random variable, $X$ has as its domain or outcome an interval on the real line, and to each of these intervals a probability may be assigned. The probability at a point is zero. In Example 2, there are an infinite number of real numbers between 0 and $2 \pi$ ; hence, the probability of obtaining any one of them is zero. Consequently, we must speak of the probability of $X$ over an interval.

# A.2 AXIOMS OF PROBABILITY

To define a probability associated with the possible values of a random variable, we introduce the fundamental axioms of probability. Let $S$ represent the set of all possible outcomes of a trial or experiment. $S$ is called the sample space of the experiment. Let $A$ be any subset of points of the set $S$ (i.e., a collection of one or more possible trials). For example, in one toss of a die the certain event $S$ would be $s = 1 , 2 , 3 , 4 , 5 , 6 .$ , and a subset, $A$ , may be $a = 3$ .

Write $p$ for a function that assigns to each event $A$ a real number $p ( A )$ , called the probability of $A$ ; that is, $p ( A )$ is the numerical probability of the event $A$ occurring. For the previous example, $p ( A ) = 1 / 6$ .

In modern probability theory, the following minimal set of axioms is generally met (Helstrom, 1984)

1. $p ( A ) \geq 0$

2. $p ( S ) = 1$

3. $p ( A + B ) = p ( A ) + p ( B )$ ; $A$ and $B$ are any pair of mutually exclusive events.

Here, $p ( A + B )$ indicates the probability of $A$ or $B$ or both occurring. For axiom 3, $A$ and $B$ cannot both occur since the events are mutually exclusive. If the events are not mutually exclusive, $p ( A + B ) = p ( A ) + p ( B ) - p ( A B )$ , where $p ( A B )$ is the probability that both events $A$ and $B$ occur. Note that for mutually exclusive events $p ( A B ) = 0$ (by definition, both events cannot occur simultaneously). A Venn diagram (Freeman, 1963) can be used to demonstrate some of the concepts associated with probability. Consider an event $A$ , then we define the complement of $A$ as the event that $A$ does not happen and denote it as $\overline { { A } }$ . Thus $A$ and $\overline { { A } }$ are said to be mutually exclusive—if $A$ occurs, $\overline { { A } }$ cannot occur.

![](images/9fb0d5a3d37b8f90a0c64eefce47d48206ed9e22d9d6a6c4dc279bc387e67c14.jpg)

If $A$ and $B$ are any two events in a sample space $S$ , we define $A B$ to be the intersection of events $A$ and $B$ and assign to it all points in the space that belongs to both $A$ and $B$ ; that is, the occurrence of $A B$ implies that both events $A$ and $B$ have occurred. The intersection of $A$ and $B$ (meaning that both events have occurred) is sometimes denoted as $A \cap B = A B$ . We define the union of $A$ and $B$ (written as $A \cup B = A + B )$ as all points in the space for which $A$ or $B$ or both have occurred. For the Venn diagram shown,

$S :$ all points in the rectangle $A :$ points in horizontal hatch region $B :$ points in vertical hatch region $A B :$ points in cross hatch region $A + B :$ all points in hatched area

Example:

Throw 1 red and 1 green die. What is probability that at least one “1” will appear? Let

$$
\begin{array} { r l } { A = } & { { } \ 1 \ \mathrm { o n \ r e d \ d i e } , } \\ { \overline { { A } } = } & { { } \ 2 6 \ \mathrm { o n \ r e d \ d i e } , } \\ { B = } & { { } \ 1 \ \mathrm { o n \ g r e e n \ d i e } , } \\ { \overline { { B } } = } & { { } \ 2 6 \ \mathrm { o n \ g r e e n \ d i e } . } \end{array}
$$

The probability of at least one “1” occurring is the union of events $A$ and $B$ , $p \left( A + B \right)$ . The probability of $A$ or $B$ or both occurring is seen from the Venn diagram to be

$$
p \left( A + B \right) = p \left( A \right) + p \left( B \right) - p \left( A B \right) .
$$

Note that $p ( A ) + p ( B )$ includes $2 \times p ( A B )$ . Now,

$$
\begin{array} { r } { p \left( A \right) = 1 / 6 } \\ { p \left( \overline { { A } } \right) = 5 / 6 } \\ { p \left( B \right) = 1 / 6 } \\ { p \left( \overline { { B } } \right) = 5 / 6 } \\ { p \left( A B \right) = p \left( A \right) p \left( B \right) = 1 / 3 6 . } \end{array}
$$

Hence,

$$
p ( A + B ) = 1 / 6 + 1 / 6 - 1 / 3 6 = 1 1 / 3 6 .
$$

Note that the events $A B , A { \overline { { B } } } , { \overline { { A } } } B , { \overline { { A } } } B$ are exhaustive (i.e., one must occur), and they are exclusive (i.e., only one can occur). Hence,

$$
\begin{array} { r l } & { p ( A B , A \overline { { B } } , \overline { { A } } B , \overline { { A } } \overline { { B } } ) = p ( A B ) + p ( A \overline { { B } } ) + p ( \overline { { A } } B ) + p ( \overline { { A } } \overline { { B } } ) } \\ & { \qquad = 1 / 3 6 + 5 / 3 6 + 5 / 3 6 + 2 5 / 3 6 = 1 . } \end{array}
$$

Also, the probability of at least one “1” occurring can be expressed as

$$
\begin{array} { c } { { p ( A B ) + p ( A \overline { { { B } } } ) + p ( \overline { { { A } } } B ) = p ( A ) p ( B ) + p ( A ) p ( \overline { { { B } } } ) + p ( \overline { { { A } } } ) p ( B ) } } \\ { { { } } } \\ { { { } = ( 1 / 6 ) ( 1 / 6 ) + ( 1 / 6 ) ( 5 / 6 ) + ( 1 / 6 ) ( 5 / 6 ) } } \\ { { { } } } \\ { { { } = 1 1 / 3 6 . } } \end{array}
$$

Furthermore, the probability of two “1”s occurring is given by events $A$ and $B$ both occurring,

$$
p \left( A B \right) ^ { * } = p \left( A \right) p \left( B \right) = 1 / 3 6 .
$$

Carrying on with this example, let

$$
\begin{array} { r l r l } { A = } & { { } } & { 1 { \mathrm { ~ o n ~ r e d ~ d i e } } \quad } & { \quad D = } & { { } 1 { \mathrm { ~ o n ~ g r e e n ~ d i e } } \quad } \\ { B = } & { { } 2 { \mathrm { ~ o n ~ r e d ~ d i e } } \quad } & { } & { { } E = } & { { } 2 { \mathrm { ~ o n ~ g r e e n ~ d i e } } } \\ { C = } & { { } 3 , 4 , 5 , 6 { \mathrm { ~ o n ~ r e d ~ d i e } } \quad } & { } & { { } F = } & { 3 , 4 , 5 , 6 { \mathrm { ~ o n ~ g r e e n ~ d i e } } } \end{array}
$$

where $p \left( A \right) = p \left( B \right) = 1 / 6$ and $p \left( C \right) = 4 / 6$ .

The probability that a “1” or a $\mathbf { \vec { \nabla } } ^ { 6 } \mathbf { \vec { 2 } } ^ { 5 }$ occurs on either or both die (call this event $G )$ is given by

$$
\begin{array} { r l } & { p \left( G \right) = p ( A D ) + p ( A E ) + p ( A F ) + p ( B D ) } \\ & { \qquad + p ( B E ) + p ( B F ) + p ( D C ) + p ( E C ) } \\ & { = 1 / 3 6 + 1 / 3 6 + 4 / 3 6 + 1 / 3 6 + 1 / 3 6 } \\ & { \qquad + 4 / 3 6 + 4 / 3 6 + 4 / 3 6 } \\ & { = 2 0 / 3 6 . } \end{array}
$$

Note that $p \left( G \right)$ also can be described by

$$
\begin{array} { c } { { p \left( G \right) = p \left( A \right) + p \left( B \right) + p \left( C D \right) + p \left( C E \right) } } \\ { { = 1 / 6 + 1 / 6 + 4 / 3 6 + 4 / 3 6 = 2 0 / 3 6 . } } \end{array}
$$

If events $A$ and $B$ occur, it does not matter what happens on the green die, but if event $C$ occurs, then either event $D$ or $E$ must occur. As stated earlier, if two events $A$ and $B$ are mutually exclusive, or disjoint, then the intersection, $A \cap B$ , has no elements in common and $p \left( A B \right) = 0$ ; that is, the probability that both $A$ and $B$ occur is zero. Hence,

$$
p \left( A + B \right) = p \left( A \right) + p \left( B \right) .
$$

For example, if we throw one die and let

$$
\begin{array} { r l } { A = } & { { } \ a ^ { * } \mathrm { \mathbb { 1 } ^ { * } \ a p p e a r s } } \\ { B = } & { { } \ a ^ { * } \mathrm { \mathbb { 2 } ^ { * } \ a p p e a r s . } } \end{array}
$$

Then

$$
p \left( A + B \right) = p \left( A \right) + p \left( B \right) = 2 / 6 .
$$

# A.3 CONDITIONAL PROBABILITY

In wide classes of problems in the real world, some events of interest are those whose occurrence is conditional on the occurrence of other events. Hence, we introduce conditional probability, $p \left( A / B \right)$ . By this we mean the probability that event $A$ occurs, given that event $B$ has occurred. It is given by

$$
p \left( A / B \right) = { \frac { p \left( A B \right) } { p \left( B \right) } } .
$$

We say that two events $A$ and $B$ are independent if

$$
p \left( A / B \right) = p \left( A \right) \mathrm { a n d } p \left( B / A \right) = p \left( B \right) ;
$$

that is,

$$
p \left( A B \right) = p \left( A \right) p \left( B \right) .
$$

# A.4 PROBABILITY DENSITY AND DISTRIBUTION FUNCTIONS

For a continuous random variable, we assume that all events of practical interest will be represented by intervals on the real line and to each of these intervals a probability may be assigned. Recall that the probability at a point is zero. We define a probability density function, $f ( x )$ , which represents the probability of $X$ assuming a value somewhere in the interval $( x , \ x + d x )$ . We define probability over the interval $x , x + d x$ in terms of area,

$$
p ( x \leq X \leq x + d x ) = f ( x ) d x .
$$

For the continuous random variable, axioms 1 and 2 become

$$
\begin{array} { r l } { 1 . \quad } & { { } f \left( x \right) \geq 0 } \\ { 2 . \quad } & { { } \displaystyle \int _ { - \infty } ^ { \infty } f \left( x \right) d x = 1 . } \end{array}
$$

The third axiom becomes

$$
\textstyle p \left( a \leq X \leq c \right) = \int _ { a } ^ { c } f \left( x \right) d x
$$

which for $a < b < c$

$$
\begin{array} { c l c r } { { p \left( a \leq X \leq c \right) = \displaystyle \int _ { a } ^ { b } f \left( x \right) d x + \displaystyle \int _ { b } ^ { c } f \left( x \right) d x } } \\ { { = p \left( a \leq X \leq b \right) + p \left( b \leq X \leq c \right) . } } \end{array}
$$

Note that for the continuous random variable we need not distinguish between $a \leq X \leq c , a \leq X < c , a < X \leq c$ , and $a < X < c$ , since the probability is the same for each (i.e., the probability at a point is zero).

Out of interest in the event $X \leq x$ , we introduce $F \left( x \right)$ , the distribution function of the continuous random variable $X$ , and define it by

$$
F \left( x \right) = p \left( X \leq x \right) = \int _ { - \infty } ^ { x } f \left( t \right) d t .
$$

It follows that

$$
F ( - \infty ) = 0 \mathrm { a n d } F ( \infty ) = 1 .
$$

From elementary calculus, at points of continuity of $F$

$$
{ \frac { d F ( x ) } { d x } } = f \left( x \right)
$$

which relates distribution and density functions for continuous random variables.

Consider the following sketch of the distribution and density function of a continuous random variable $X$ .

![](images/a5b80b96ed91b5fe8bed30bed2c2e28fe1140dd8b28c83649d3eaf361d8f39b8.jpg)  
Density function of a continuous random variable

![](images/175e1c0cafea89ad97ac835c33d14bdaa7ff386ff72e31481d7e9465bbdc8d65.jpg)  
Distribution function of a continuous random variable

From the definition of the density and distribution functions we have

$$
p \left( a \leq X \leq b \right) = \int _ { a } ^ { b } f ( x ) d x = F \left( b \right) - F \left( a \right) .
$$

From axioms 1 and 2, we find

$$
0 \leq F ( x ) \leq 1
$$

and $F ( x )$ is monotonically increasing.

# A.5 EXPECTED VALUES

We will now discuss the characteristics of probability distributions. A probability distribution is a generic term used to describe the probability behavior of a random variable. We shall now define certain useful parameters associated with probability distributions for continuous random variables. The expected value or the mean of $X$ is written $E \left( X \right)$ , and is defined by

$$
E ( X ) = \int _ { - \infty } ^ { \infty } x f ( x ) d x .
$$

Now consider a second random variable, where

$$
Y = g \left( X \right)
$$

then

$$
E \left[ g ( X ) \right] = \int _ { - \infty } ^ { \infty } g ( x ) f ( x ) d x
$$

which defines the expected value of a function of a random variable.

# A.6 EXAMPLES AND DISCUSSION OF EXPECTATION

There are particular functions, $g ( X )$ , whose expectations describe important characteristics of the probability distribution of $X$ . We will now consider several particular cases.

$E \left( X \right)$ is sometimes written as $\lambda _ { 1 }$ or $\lambda$ and is called the arithmetic mean of $X$ . Geometrically, $\lambda _ { 1 }$ is one of a number of possible devices for locating the “center” or centroid of the probability distribution with respect to the origin. The $k$ th moment of $X$ about the origin is

$$
E \left[ X ^ { k } \right] = \lambda _ { k } = \intop _ { - \infty } ^ { \infty } x ^ { k } f ( x ) d x .
$$

We also may speak of the $k$ th moment of $X$ about the mean $\lambda _ { 1 }$ . In this case, we define

$$
\mu _ { k } \equiv E ( X - \lambda _ { 1 } ) ^ { k } = \intop _ { - \infty } ^ { \infty } ( x - \lambda _ { 1 } ) ^ { k } f ( x ) d x .
$$

Note that $\mu _ { 1 } = 0$ . For $k = 2$

$$
\mu _ { 2 } = E ( X - \lambda _ { 1 } ) ^ { 2 } = \intop _ { - \infty } ^ { \infty } ( x - \lambda _ { 1 } ) ^ { 2 } f ( x ) d x .
$$

This is usually denoted as $\sigma ^ { 2 }$ or $\sigma ^ { 2 } ( X )$ and called the variance of $X$ , the variance of the probability distribution of $X$ , or the second moment of $X$ about the mean. Note that $\mu _ { 2 }$ is always greater than zero unless $p ( X = \lambda _ { 1 } ) = 1$ . In this case $\mu _ { 2 } =$ 0. The positive square root of the variance, $\sigma$ , is called the standard deviation of $X$ . It is one measure of the dispersion of the distribution about its mean value.

We interpret the density function as a mass distribution, the first moment about the origin becomes the center of gravity of the distribution, and the variance is the moment of inertia about an axis through the mean. For example, consider the following density functions:

![](images/9aeaf9fd4f75236e73d5880655f19b0cbe2000dc2af5d4bbd17f3ddd2ae2b3c9.jpg)

Both density functions $a$ and $b$ have their mean value indicated by $\lambda _ { 1 }$ . Note that the variance of $b$ obviously will be much larger than that of $a$ , since $( x - \lambda _ { 1 } ) ^ { 2 }$ generally will be larger than that of $a$ for an increment of area $d x$ .

A few useful results follow readily from the definition of the expected value (see Eq. (A.5.1)) and the fact that it is a linear operator

$$
E ( a + b X ) = a + b E ( X )
$$

where $a$ and $b$ are constants. Also,

$$
\begin{array} { l } { \displaystyle \mu _ { 1 } = \int _ { - \infty } ^ { \infty } ( x - \lambda _ { 1 } ) f ( x ) d x = \lambda _ { 1 } - \lambda _ { 1 } = 0 } \\ { \displaystyle - \infty } \\ { \displaystyle \mu _ { 2 } = \int _ { - \infty } ^ { \infty } ( x - \lambda _ { 1 } ) ^ { 2 } f ( x ) d x } \\ { \displaystyle = \int _ { - \infty } ^ { \infty } ( x ^ { 2 } - 2 x \lambda _ { 1 } + \lambda _ { 1 } ^ { 2 } ) f ( x ) d x } \\ { \displaystyle \quad - \infty } \\ { \displaystyle = \lambda _ { 2 } - 2 \lambda _ { 1 } ^ { 2 } + \lambda _ { 1 } ^ { 2 } } \\ { \displaystyle = \lambda _ { 2 } - \lambda _ { 1 } ^ { 2 } . } \end{array}
$$

The higher order moments are of theoretical importance in any distribution, but they do not have a simple geometric or physical interpretation as do $\lambda _ { 1 }$ and $\mu _ { 2 }$ .

All the information that can be known about the random variable $X$ is contained in the probability density function. In guidance and estimation applications, we are most concerned with the first two moments, namely the mean and variance. Since the probability density function will change with time, the prediction of the future values for the state of the dynamic system can be obtained by propagating the joint density function (see Section A.9) forward in time and using it to calculate the mean and variance. The equations for propagating the mean and variance of a random vector $X$ are discussed in Section 4.8 of the text.

# A.7 MOMENT GENERATING FUNCTIONS

Consider the particular case of

$$
E \left[ g ( X ) \right] = \intop _ { - \infty } ^ { \infty } g ( x ) f ( x ) d x
$$

for which

$$
g ( X ) = e ^ { \theta x }
$$

where $\theta$ is a dummy variable. Since

$$
e ^ { \theta x } = 1 + \theta x + { \frac { ( \theta x ) ^ { 2 } } { 2 ! } } + \cdot \cdot \cdot { \frac { ( \theta x ) ^ { n } } { n ! } } + \cdot \cdot \cdot
$$

substituting Eq. (A.7.2) into Eq. (A.7.1) results in

$$
E \left( e ^ { \theta x } \right) = \lambda _ { 0 } + \theta \lambda _ { 1 } + \frac { \theta ^ { 2 } \lambda _ { 2 } } { 2 ! } + ~ . . . \frac { \theta ^ { n } \lambda _ { n } } { n ! } + \cdot \cdot \cdot
$$

Thus $E ( e ^ { \theta x } )$ may be said to generate the moments $\lambda _ { 0 } , \lambda _ { 1 } \ldots \lambda _ { n }$ of the random variable $X$ . It is called the moment generating function of $X$ and is written $M _ { X } ( \theta )$ . Note that

$$
\left. \frac { \partial ^ { k } M _ { X } ( \theta ) } { \partial \theta ^ { k } } \right| _ { \theta = 0 } = \lambda _ { k } .
$$

Accepting the fact that the moment generating function for the function $h ( X )$ is given by

$$
M _ { h ( X ) } ( \theta ) = \intop _ { - \infty } ^ { \infty } e ^ { \theta h ( X ) } f ( x ) d x ,
$$

let $h ( X ) = X - \lambda _ { 1 }$ , then

$$
M _ { ( X - \lambda _ { 1 } ) } ( \theta ) = e ^ { - \theta \lambda _ { 1 } } M _ { X } ( \theta )
$$

which relates moments about the origin to moments about the mean,

$$
\mu _ { k } = \frac { \partial ^ { k } M _ { ( X - \lambda _ { 1 } ) } ( \theta ) } { \partial \theta ^ { k } } \Big | _ { \theta = 0 } .
$$

From Eqs. (A.7.3) and (A.7.6)

$$
M _ { ( X - \lambda _ { 1 } ) } ( \theta ) = e ^ { - \theta \lambda _ { 1 } } \left( \lambda _ { 0 } + \theta \lambda _ { 1 } + { \frac { \theta ^ { 2 } \lambda _ { 2 } } { 2 ! } } + \cdot \cdot \cdot { \frac { \theta ^ { n } \lambda _ { n } } { n ! } } \cdot \cdot \cdot \right)
$$

and for example,

$$
\begin{array} { l } { { \displaystyle \mu _ { 2 } = \left. \frac { \partial ^ { 2 } M _ { ( X - \lambda _ { 1 } ) } ( \theta ) } { \partial \theta ^ { 2 } } \right. _ { \theta = 0 } } } \\ { { \displaystyle \quad = \lambda _ { 1 } ^ { 2 } e ^ { - \theta \lambda _ { 1 } } ( \lambda _ { 0 } + \theta \lambda _ { 1 } ) - \lambda _ { 1 } e ^ { - \theta \lambda _ { 1 } } \lambda _ { 1 } - \lambda _ { 1 } e ^ { - \theta \lambda _ { 1 } } \lambda _ { 1 } + e ^ { - \theta \lambda _ { 1 } } \lambda _ { 2 } \Big \vert _ { \theta = 0 } } } \\ { { \displaystyle \quad = \lambda _ { 2 } - \lambda _ { 1 } ^ { 2 } , ~ \mathrm { \ r e c a l l ~ t h a t } ~ \lambda _ { 0 } = 1 . } } \end{array}
$$

This is identical to the result in Eq. (A.6.6).

# A.8 SOME IMPORTANT CONTINUOUS DISTRIBUTIONS

# A.8.1 UNIFORM OR RECTANGULAR DISTRIBUTION

If $X$ has equal probability over the range $a \leq X \leq b$ , that is, every value of $X$ in this range is equally likely to occur, we say that $X$ is uniformly distributed. Its density function is

$$
f ( x ) = { \frac { 1 } { b - a } } , \quad a \leq x \leq b
$$

$$
\begin{array} { l } { { \displaystyle F ( x ) = \int _ { - \infty } ^ { a } f ( x ) d x + \int _ { a } ^ { x } f ( t ) d t = \int _ { a } ^ { x } \frac { d t } { b - a } } } \\ { { \displaystyle F ( x ) = 0 \quad x < a } } \\ { { \displaystyle \qquad = \frac { x - a } { b - a } \quad a \leq x \leq b } } \\ { { \displaystyle = 1 \quad x > b . } } \end{array}
$$

The first two moments (mean and variance) are

$$
\begin{array} { c } { { E ( X ) = \displaystyle \int _ { a } ^ { b } x f ( x ) d x = \int _ { a } ^ { b } \frac { x d x } { b - a } } } \\ { { = \displaystyle \left[ \frac { x ^ { 2 } } { 2 ( b - a ) } \right] _ { a } ^ { b } = \frac { a + b } { 2 } } } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle \sigma ^ { 2 } ( X ) = \int _ { a } ^ { b } [ x - E ( X ) ] ^ { 2 } f ( x ) d x } \ ~ } \\ { { \displaystyle ~ = \int _ { a } ^ { b } \left( x - \frac { a + b } { 2 } \right) ^ { 2 } \frac { d x } { b - a } = \frac { ( b - a ) ^ { 2 } } { 1 2 } . } } \end{array}
$$

Graphically the uniform density function is

![](images/557d8e1a033a8a2e86e22eef519d071d9feac012b7a5bd521af8b859fd5409a1.jpg)

The uniform density function is hardly a likely description of the probability behavior of many physical systems. Its importance lies in its utility in statistical theory. Any continuous probability distribution can be converted first into a uniform distribution, then into a given continuous distribution. This often facilitates the study of the properties of the distribution, which themselves are somewhat intractable.

# A.8.2 THE GAUSSIAN OR NORMAL DISTRIBUTION

One of the most important distributions in probability theory is the one for which

$$
\begin{array} { r } { f ( x ) = \frac { 1 } { \sqrt { 2 \pi } b } \exp \left[ - \frac { 1 } { 2 } \left( \frac { x - a } { b } \right) ^ { 2 } \right] ^ { - \infty < x < \infty } . } \end{array}
$$

The moment generating function for this distribution is

$$
\begin{array} { l } { \displaystyle M _ { X } ( \theta ) = E [ e ^ { \theta x } ] = \int _ { - \infty } ^ { \infty } e ^ { \theta x } f ( x ) d x } \\ { \displaystyle M _ { X } ( \theta ) = \int _ { - \infty } ^ { \infty } \frac { e ^ { \theta x } } { \sqrt { 2 \pi } b } \exp \left[ - \frac 1 2 \left( \frac { x - a } { b } \right) ^ { 2 } \right] d x } \\ { = \exp \left[ \frac { \theta ^ { 2 } b ^ { 2 } } { 2 } + a \theta \right] . } \end{array}
$$

For details of the derivation of Eq. (A.8.5), see Freeman (1963).

From Eq. (A.8.5), we see that the mean of the normal distribution is

$$
{ \frac { \partial M _ { X } ( \theta ) } { \partial \theta } } \Big | _ { \theta = 0 } = a
$$

hence

$$
\lambda _ { 1 } = a .
$$

From Eq. (A.7.6), we have

$$
\begin{array} { c } { { M _ { X - \lambda _ { 1 } } \left( \theta \right) = e ^ { - a \theta } M _ { X } \left( \theta \right) } } \\ { { = e ^ { \theta ^ { 2 } b ^ { 2 } / 2 } } } \end{array}
$$

and from Eq. (A.8.6), the variance is

$$
\frac { \partial ^ { 2 } M _ { X - \lambda _ { 1 } } ( \theta ) } { \partial \theta ^ { 2 } } \Big | _ { \theta = 0 } = b ^ { 2 } = \sigma ^ { 2 }
$$

and $\sigma = b$ . Hence, Eq. (A.8.4) may be written

$$
\begin{array} { r } { f ( x ) = \frac { 1 } { \sqrt { 2 \pi } \sigma } \exp \left[ - \frac { 1 } { 2 } \left( \frac { x - \lambda _ { 1 } } { \sigma } \right) ^ { 2 } \right] - \infty < x < \infty . } \end{array}
$$

Using Eq. (A.8.6), it may be shown that

$$
\mu _ { 2 k + 1 } = 0 ,
$$

that is, the odd moments of a normal random variable about its mean are zero. In fact the odd moments of any symmetric distribution about its mean are zero provided that they exist.

The normal distribution is depicted graphically here:

![](images/c2906d3f240eca4583c76a87e768195ff1fa69971b0a3b38efd5aaeff063cb64.jpg)

The density function has its maximum at $X = \lambda _ { 1 }$ , is symmetric about the line $X = \lambda _ { 1 }$ , and has two inflection points at $X = \lambda _ { 1 } \pm \sigma$ (i.e., points where d2f(x)dx2 = 0), and the minimum occur at ±∞. Other interesting properties of the univariate normal distribution function are

$$
\begin{array} { r } { p ( \lambda _ { 1 } - \sigma \le X \le \lambda _ { 1 } + \sigma ) = \displaystyle \int _ { \lambda _ { 1 } - \sigma } f ( x ) d x = . 6 8 2 6 8 } \\ { p \left[ ( \lambda _ { 1 } - 2 \sigma ) \le X \le ( \lambda _ { 1 } + 2 \sigma ) \right] = . 9 5 4 4 9 } \\ { p \left[ ( \lambda _ { 1 } - 3 \sigma ) \le X \le ( \lambda _ { 1 } + 3 \sigma ) \right] = . 9 9 7 3 0 . } \end{array}
$$

# A.9 TWO RANDOM VARIABLES

The joint distribution function $F \left( x , y \right)$ of two random variables is define d as

$$
F ( x _ { 0 } , y _ { 0 } ) = p \{ X \leq x _ { 0 } , Y \leq y _ { 0 } \} .
$$

It has the following properties

$$
\begin{array} { r l r } & { 0 \le F ( x , y ) \le 1 \qquad } & { \mathrm { f o r ~ a l l ~ } x , y } \\ & { F ( - \infty , y ) = F ( x , - \infty ) = 0 , F [ \infty , \infty ] = 1 } & \\ & { F \left( \infty , y _ { 0 } \right) = p \left\{ Y \le y _ { 0 } \right\} , \quad } & { F ( x _ { 0 } , \infty ) = p \left\{ X \le x _ { 0 } \right\} } \end{array} .
$$

The concept of the density function now follows. Because $F \left( x , y \right)$ is continuous, a function $f \left( x , y \right)$ exists such that

$$
F \left( x , y \right) = \int _ { - \infty } ^ { y } \intop _ { - \infty } ^ { x } f \left( u , v \right) d u d v
$$

or the equivalent

$$
f \left( x , y \right) = \frac { \partial F ^ { 2 } ( x , y ) } { \partial x \partial y } .
$$

By definiti on,

$$
p \left( a \leq X \leq b , c \leq Y \leq d \right) = \int _ { c } ^ { d } \intop f \left( x , y \right) d x d y
$$

which is analogous to the relationship between the probability and the density function for the single random variable case. Eq. (A.9.5) may be written

$$
p \left( x \leq X \leq x + d x , y \leq Y \leq y + d y \right) = f ( x , y ) d x d y .
$$

In summary:

F (x, y) joint distribution function of $X , Y .$ .   
f (x, y) joint density function of $X$ , $Y$ .   
f (x, y) dx dy ≡ joint probability element of $X$ , $Y$ .

# A.10 MARGINAL DISTRIBUTIONS

We often want to determine the probability behavior of one random variable, given the joint probability behavior of two. This is interpreted to mean

$$
p \left( X \leq x , \mathrm { n o } \mathrm { c o n d i t i o n } \mathrm { o n } Y \right) = F \left( x , \infty \right) .
$$

For the continuous case

$$
\begin{array} { l } { { \displaystyle F ( x , \infty ) = \int _ { - \infty } ^ { x } \int _ { - \infty } ^ { \infty } f ( u , v ) d v d u = \int _ { - \infty } ^ { x } \left[ \int _ { - \infty } ^ { \infty } f ( u , v ) d v \right] d u } } \\ { { \displaystyle x } } \\ { { \displaystyle = \int _ { - \infty } ^ { x } g ( u ) d u } . } \end{array}
$$

Hence,

$$
g \left( x \right) = \intop _ { - \infty } ^ { \infty } f ( x , y ) d y
$$

is called the marginal density function of $X$ . Similarly,

$$
F \left( \infty , y \right) = \intop _ { - \infty } ^ { y } \left[ \intop _ { - \infty } ^ { \infty } f \left( u , v \right) d u \right] d v = \intop _ { - \infty } ^ { y } h \left( v \right) d v
$$

and

$$
h \left( y \right) = \intop _ { - \infty } ^ { \infty } f \left( x , y \right) d x
$$

is the marginal density function of $Y$ . Hence, the marginal density function of a random variable is obtained from the joint density function by integrating over the unwanted variable.

# A.11 INDEPENDENCE OF RANDOM VARIABLES

We have previously defined the independence of two events $A$ and $B$ by $p \left( A , B \right) = p \left( A \right) p \left( B \right)$ . For the case of random variables $X$ and $Y$ , we say that they are independent if we can factor their joint density function into

$$
f \left( x , y \right) = g \left( x \right) h \left( y \right)
$$

where $g \left( x \right)$ and $h \left( y \right)$ are the marginal density functions of $X$ and $Y$ .

# A.12 CONDITIONAL PROBABILITY

For the simple events $A$ and $B$ , we define $p \left( B / A \right)$ by

$$
p \left( B / A \right) = \frac { p \left( A B \right) } { p \left( A \right) } .
$$

In the spirit of Eq. (A.12.1), we wish to define a conditional density function for continuous random variables $X$ and $Y$ with density functions $f \left( x , y \right) , g \left( x \right)$ , and $h \left( y \right)$ . Accordingly,

$$
\begin{array} { r } { g \left( x / y \right) = \frac { f \left( x , y \right) } { h \left( y \right) } , h \left( y / x \right) = \frac { f \left( x , y \right) } { g \left( x \right) } . } \end{array}
$$

As an immediate consequence of Eq. (A.12.2), we have

$$
\begin{array} { r } { p \left( a \leq X \leq b / Y = y \right) = \overset { b } { \underset { a } { \int } } g \left( x / y \right) d x = \frac { \int _ { a } ^ { b } f \left( x , y \right) d x } { h \left( y \right) } } \end{array}
$$

$$
\begin{array} { r } { p \left( c \leq Y \leq d / X = x \right) = \int _ { c } ^ { d } h \left( y / x \right) d y = \frac { \int _ { c } ^ { d } f \left( x , y \right) d y } { g \left( x \right) } . } \end{array}
$$

Note that in Eq. (A.12.3), we are talking about $X$ and $Y$ in the vicinity of the values $x$ and $y$ .

Also,

$$
\begin{array} { r } { p ( a \leq X \leq b / c \leq Y \leq d ) = \displaystyle \frac { p ( a \leq X \leq b , c \leq Y \leq d ) } { p ( c \leq Y \leq d ) } } \\ { = \displaystyle \frac { \int _ { a } ^ { b } \int _ { c } ^ { d } f \left( x , y \right) d y d x } { \int _ { c } ^ { d } h ( y ) d y } . } \end{array}
$$

In the case of statistically independent variables, $X$ and $Y$ , the definit ion of statistical independence given by Eq. (A.11.1) leads to the following result from

Eq. (A.12.2)

$$
g \left( x / y \right) = \frac { f \left( x , y \right) } { h \left( y \right) } = \frac { g \left( x \right) h \left( y \right) } { h \left( y \right) } = g \left( x \right)
$$

$$
h \left( y / x \right) = \frac { f \left( x , y \right) } { g \left( x \right) } = h \left( y \right) .
$$

# A.13 EXPECTED VALUES OF BIVARIATE FUNCTIONS

Following the arguments for one random variable, we say that the mean or expected value $E \left[ \phi \left( X , Y \right) \right]$ of an arbitrary function $\phi ( X , Y )$ of two continuous random variables $X$ and $Y$ is given by

$$
E \left[ \phi \left( X , Y \right) \right] = \int \intop _ { - \infty } ^ { \infty } \intop \mathop { \phi } \left( x , y \right) f \left( x , y \right) d x d y .
$$

As with one random variable, the expected value of certain functions is of great importance in identifying characteristics of joint probability distributions. Such expectations include the following. Setting

$$
\phi \left( X , Y \right) = X ^ { l } Y ^ { m }
$$

gives

$$
E \left[ X ^ { l } Y ^ { m } \right] = \int \displaylimits _ { - \infty } ^ { \infty } \int \displaylimits _ { - \infty } ^ { \infty } x ^ { l } y ^ { m } f \left( x , y \right) d x d y \equiv \lambda _ { l m }
$$

written $\lambda _ { l m }$ , the $l m ^ { \mathrm { t h } }$ moment of $X$ , $Y$ about the origin. The $l m ^ { \mathrm { t h } }$ moment about the mean is obtained by setting

$$
\phi \left( X , Y \right) = { [ } X - \lambda _ { 1 0 } { ] } ^ { l } { [ } Y - \lambda _ { 0 1 } { ] } ^ { m } .
$$

This results in

$$
{ \begin{array} { r l } & { \qquad E \left\{ \left[ X - \lambda _ { 1 0 } \right] ^ { l } \left[ Y - \lambda _ { 0 1 } \right] ^ { m } \right\} } \\ & { = \displaystyle \int _ { - \infty } ^ { \infty } \int _ { - \infty } ^ { \infty } [ x - \lambda _ { 1 0 } ] ^ { l } [ y - \lambda _ { 0 1 } ] ^ { m } f ( x , y ) d x d y \equiv \mu _ { l m } } \\ & { \qquad - \infty - \infty } \end{array} }
$$

written $\mu _ { l m }$ , the $l m ^ { \mathrm { t h } }$ moment of $X , Y$ about the respective moments $\lambda _ { 1 0 }$ and $\lambda _ { 0 1 }$ . Particular cases of $\mu _ { l m }$ and $\lambda _ { l m }$ often used are

$$
\begin{array} { r l } { \ l } & { \ m } \\ { 0 } & { \ 0 \ \lambda _ { 0 0 } = 1 } \\ { 1 \ } & { \ 0 \ \lambda _ { 1 0 } = E \left( X \right) , \mathrm { t h e ~ m e a n ~ o f ~ } X } \\ { 0 \ } & { \ 1 \ } \\ { 0 \ } & { \ 0 \ } & { \ \mu _ { 0 0 } = 1 } \\ { 1 \ } & { \ 1 \ } & { \ \mu _ { 1 1 } = E \left\{ \left[ X - E \left( X \right) \right] \left( Y - E \left( Y \right) \right) \right\} , } \\ { 2 \ } & { \ 0 \ } & { \ \mu _ { 2 0 } = \sigma ^ { 2 } ( X ) , \mathrm { t h e ~ v a r i a n c e ~ o f ~ } X } \\ { 0 \ } & { \ 2 \ } & { \ \mu _ { 0 2 } = \sigma ^ { 2 } ( Y ) , \mathrm { t h e ~ v a r i a n c e ~ o f ~ } Y . } \end{array}
$$

Consider as an example the computation of

$$
\begin{array} { l } { \displaystyle \mu _ { 1 1 } = E ( X - \lambda _ { 1 0 } ) \big ( Y - \lambda _ { 0 1 } \big ) } \\ { \displaystyle \quad = \int _ { - \infty } \displaylimits ^ { \infty } \int \displaylimits _ { 0 } ^ { \infty } ( x - \lambda _ { 1 0 } ) \big ( y - \lambda _ { 0 1 } \big ) f ( x , y ) d x d y } \\ { \displaystyle \quad \quad - \int \displaylimits _ { - \infty } ^ { \infty } \infty } \\ { \displaystyle \quad = \int \displaylimits _ { - \infty } ^ { \infty } \int \displaylimits _ { 0 } ^ { \infty } ( x y - \lambda _ { 1 0 } y - \lambda _ { 0 1 } x + \lambda _ { 1 0 } \lambda _ { 0 1 } ) f \left( x , y \right) d x d y } \\ { \displaystyle \quad \quad - \infty - \infty } \\ { \displaystyle = \lambda _ { 1 1 } - 2 \lambda _ { 1 0 } \lambda _ { 0 1 } + \lambda _ { 1 0 } \lambda _ { 0 1 } } \\ { \displaystyle = \lambda _ { 1 1 } - \lambda _ { 1 0 } \lambda _ { 0 1 } . } \end{array}
$$

The result is analogous to Eq. (A.6.6).

# A.14 THE VARIANCE-COVARIANCE MATRIX

The symmetric matrix

$$
\begin{array} { r l } & { P = E \left[ \left[ X - E ( X ) \right] \Big [ X - E ( X ) Y - E ( Y ) \Big ] \right] } \\ & { \quad = E \left[ ( X - E ( X ) ) ^ { 2 } \qquad ( X - E ( X ) ) ( Y - E ( Y ) ) \right] } \\ & { \quad P = \left[ \sigma ^ { 2 } ( X ) \mu _ { 1 1 } \right. } \\ & { \quad \left. \mu _ { 1 1 } \quad \sigma ^ { 2 } ( Y ) \right] } \end{array}
$$

is called the variance-covariance matrix of the random variables $X$ and $Y$ . As seen from Eq. (A.14.1), the diagonals contain the variances of $X$ and $Y$ , and the off diagonal terms contain the covariances.

The covariance of the random variables $X$ and $Y$ often is written in terms of the correlation coefficient between $X$ and $Y$ , $\rho _ { X Y }$ . The correlation coefficient is defined as

$$
\begin{array} { c } { { \rho _ { X Y } \equiv \displaystyle \frac { E \{ [ X - E ( X ) ] [ Y - E ( Y ) ] \} } { \{ E [ X - E ( X ) ] ^ { 2 } \} ^ { 1 / 2 } \{ E [ Y - E ( Y ) ] ^ { 2 } \} ^ { 1 / 2 } } } }  \\ { { = \displaystyle \frac { \mu _ { 1 1 } } { \sigma ( X ) \sigma ( Y ) } . } } \end{array}
$$

The variance-covariance matrix for an $n$ -dimensional random vector, $X$ , can be written as

$$
P = \left[ \begin{array} { c c c c } { \sigma _ { 1 } ^ { 2 } } & { \rho _ { 1 2 } \sigma _ { 1 } \sigma _ { 2 } \cdots \rho _ { 1 n } \sigma _ { 1 } \sigma _ { n } } \\ {  } & {  } & {  } & {  } \\ { \rho _ { 1 2 } \sigma _ { 1 } \sigma _ { 2 } } & { \sigma _ { 2 } ^ { 2 } } & { \cdots \rho _ { 2 n } \sigma _ { 2 } \sigma _ { n } } \\ {  } & {  } & { \ddots } & { \vdots } \\ {  } & {  } & {  } & {  } \\ { \rho _ { 1 n } \sigma _ { 1 } \sigma _ { n } \rho _ { 2 n } \sigma _ { 2 } \sigma _ { n } \cdots } & { \sigma _ { n } ^ { 2 } } & {  } \end{array} \right]
$$

where $\rho _ { i j }$ is a measure of the degree of linear correlation between $X _ { i }$ and $X _ { j }$ . It can also be written as

$$
\rho _ { i j } \equiv { \frac { P _ { i j } } { \sigma _ { i } \sigma _ { j } } } , \quad i \neq j .
$$

The correlation coefficient can be shown to be the covariance between the standardized random variables

$$
\begin{array} { r } { U \equiv \frac { X - E \left( X \right) } { \sigma \left( X \right) } , V \equiv \frac { Y - E \left( Y \right) } { \sigma \left( Y \right) } . } \end{array}
$$

That is,

$$
\rho _ { X Y } = \operatorname { c o v } { ( \mathrm { U } , \mathrm { V } ) } = E [ ( U - E ( U ) ) ( V - E ( V ) ) ] .
$$

This is easily demonstrated by noting that

$$
E ( U ) = E ( V ) = 0 .
$$

Thus

$$
E [ ( U - E ( U ) ) ( V - E ( V ) ) ] = E ( U V ) .
$$

So

$$
{ \begin{array} { l } { \displaystyle \operatorname { c o v } \left( \operatorname { U V } \right) = E \left( U V \right) = E \left[ \left( { \frac { X - E ( X ) } { \sigma \left( X \right) } } \right) \left( { \frac { Y - E ( Y ) } { \sigma ( Y ) } } \right) \right] } \\ { \displaystyle \qquad = { \frac { \mu _ { 1 1 } } { \sigma \left( X \right) \sigma \left( Y \right) } } \equiv \rho _ { X Y } . } \end{array} }
$$

Hence,

$$
\operatorname { c o v } \left( \operatorname { U V } \right) = \rho _ { X Y } .
$$

Note also that

$$
\begin{array} { l } { { \displaystyle \sigma ^ { 2 } ( U ) = E [ U - E ( U ) ] ^ { 2 } = E [ U ^ { 2 } ] } } \\ { { \displaystyle \quad = \frac { E [ X - E ( X ) ] ^ { 2 } } { \sigma ^ { 2 } ( X ) } = \frac { \sigma ^ { 2 } ( X ) } { \sigma ^ { 2 } ( X ) } = 1 . } } \end{array}
$$

Likewise

$$
\sigma ^ { 2 } ( V ) = 1 .
$$

So

$$
\sigma ^ { 2 } ( U ) = \sigma ^ { 2 } ( V ) = 1 .
$$

Note that the standard deviation is defined to be the positive square root of the variance. Consequently,

$$
\rho _ { U V } = { \frac { \operatorname { c o v } \left( \operatorname { U V } \right) } { \sigma ( U ) \sigma ( V ) } } = \operatorname { c o v } \left( \operatorname { U V } \right) = \rho _ { X Y } .
$$

# A.15 PROPERTIES OF THE CORRELATIONCOEFFICIENT

It is first convenient to prove two elementary relationships for a function of two random variables. For $a$ and $b$ constant

$$
E ( a X + b Y ) = a E \left( X \right) + b E \left( Y \right) .
$$

This follows from the linear property of the expectation operator. Next,

$$
\begin{array} { c } { { \sigma ^ { 2 } ( a X + b Y ) \equiv E [ ( a X + b Y ) - E ( a X + b Y ) ] ^ { 2 } } } \\ { { = E \left[ a ( X - E ( X ) ) + b ( Y - E ( Y ) ) \right] ^ { 2 } } } \\ { { = a ^ { 2 } E [ X - E ( X ) ] ^ { 2 } + 2 a b E [ ( X - E ( X ) ) ( Y - E ( Y ) ) ] + b ^ { 2 } E [ Y - E ( Y ) ] ^ { 2 } } } \\ { { = a ^ { 2 } \sigma ^ { 2 } ( X ) + 2 a b \mu _ { 1 1 } + b ^ { 2 } \sigma ^ { 2 } ( Y ) . } } \end{array}
$$

In terms of the correlation coeffic ient defined by Eq. (A.14.2), this result becomes

$$
\sigma ^ { 2 } ( a X + b Y ) = a ^ { 2 } \sigma ^ { 2 } ( X ) + 2 a b \rho _ { X Y } \sigma ( X ) \sigma ( Y ) + b ^ { 2 } \sigma ^ { 2 } ( Y ) .
$$

Using Eqs. (A.15.1) and (A.15.2), we can demonstrate certain useful properties of $\rho$ .

It will be convenient to use the standardized random variables defined by Eq. (A.14.5). From Eq. (A.15.2), we have that

$$
\begin{array} { r l } & { \sigma ^ { 2 } ( U + V ) = \sigma ^ { 2 } ( U ) + 2 \rho _ { U V } \sigma ( U ) \sigma ( V ) + \sigma ^ { 2 } ( V ) } \\ & { \sigma ^ { 2 } ( U - V ) = \sigma ^ { 2 } ( U ) - 2 \rho _ { U V } \sigma ( U ) \sigma ( V ) + \sigma ^ { 2 } ( V ) } \end{array}
$$

but from Eq. (A.14.11)

$$
\sigma ^ { 2 } ( U ) = \sigma ^ { 2 } ( V ) = 1
$$

hence

$$
\begin{array} { r } { \sigma ^ { 2 } ( U \pm V ) = 2 ( 1 \pm \rho _ { U V } ) . } \end{array}
$$

Since by defini tion a variance is a nonnegative quantity

$$
\begin{array} { l } { { 1 + \rho _ { U V } \geq 0 } } \\ { { 1 - \rho _ { U V } \geq 0 . } } \end{array}
$$

Hence

$$
- 1 \le \rho _ { U V } \le 1
$$

and from Eq. (A.14.12)

$$
- 1 \leq \rho _ { X Y } \leq 1 .
$$

It can be shown that when $\rho _ { X Y }$ assumes its extreme values $+ 1$ or $- 1$ , the relationship between $X$ and $Y$ is perfectly linear. That is, all values of the random variable pair $X$ , $Y$ lie on a straight line of positive or negative slope.

From Eq. (A.15.3), if $\rho _ { U V } ~ = ~ + 1$

$$
\sigma ^ { 2 } ( U - V ) = 0 .
$$

Hence, $( U - V )$ is a constant with all probability concentrated at that constant. Or in terms of $X$ and $Y$

$$
{ \frac { X - E ( X ) } { \sigma ( X ) } } - { \frac { Y - E ( Y ) } { \sigma ( Y ) } } = \mathrm { c o n s t } .
$$

This is an equation of the form

$$
Y = a + b X
$$

where $b = \sigma ( Y ) / \sigma ( X )$ , a positive constant.

A similar expression may be written for $\rho _ { U V } ~ = ~ - 1$ . In this case, $b$ is a negative constant $( - \sigma ( Y ) / \sigma ( X ) )$ . Also, the converse holds. Suppose that

$$
Y = a \pm b X .
$$

Then it can easily be shown that $\mu _ { 1 1 } = \pm b \sigma ^ { 2 } ( X )$ and that $\sigma ^ { 2 } ( Y ) ~ = ~ b ^ { 2 } \sigma ^ { 2 } ( X )$ Using the definition of $\rho$ , we have $\rho _ { X Y } = \pm 1$ .

Nonlinear functional relationships between random variables do not necessarily result in the correlation coefficient assuming a value of 1.

# A.16 PROPERTIES OF COVARIANCE AND CORRELATION

From the definition of $\mu _ { 1 1 }$

$$
\mu _ { 1 1 } = E [ ( X - E ( X ) ) ( Y - E ( Y ) ) ]
$$

we see that if large values of the random variable $X$ are found paired generally with large values of $Y$ in the function $f \left( x , y \right)$ , and if small values of $X$ are paired with small values of Y, $\mu _ { 1 1 }$ and hence $\rho _ { X Y }$ will be positive. Also, if large values of $X$ are paired with small values of $Y$ in $f \left( x , y \right)$ , then $\mu _ { 1 1 }$ and hence $\rho _ { X Y }$ will be negative. Finally, if some large and small values of $X$ and $Y$ are paired then $\mu _ { 1 1 } \simeq 0$ . Graphically assume that we sample a value of $X$ and $Y$ and plot the results. Three cases are possible:

![](images/ea1558d609fc8fd325b6c8769dcc259cb92eac3bc4a0bbeb9bab953b073fc397.jpg)

An example of positive correlation would be a sampling of human height and weight. Note that if $\rho _ { X Y } = 1$ , the variance-covariance matrix will be singular.

# A.17 BIVARIATE NORMAL DISTRIBUTION

The bivariate normal density function is given by

$$
\begin{array} { r l r } & { } & { f \left( x , y \right) = \frac { 1 } { 2 \pi \sigma \left( x \right) \sigma \left( y \right) \sqrt { 1 - \rho ^ { 2 } } } \exp \left[ - \frac { 1 } { 2 \left( 1 - \rho ^ { 2 } \right) } \left\{ \left[ \frac { x - \lambda _ { 1 0 } } { \sigma \left( x \right) } \right] ^ { 2 } - \infty < x < \infty \right. \right. } \\ & { } & { \left. \left. - \rho \frac { \left[ x - \lambda _ { 1 0 } \right] \left[ y - \lambda _ { 0 1 } \right] } { \sigma \left( x \right) \sigma \left( y \right) } + \left[ \frac { y - \lambda _ { 0 1 } } { \sigma \left( y \right) } \right] ^ { 2 } \right\} \right] \qquad \mathrm { ( A . 1 7 } } \end{array}
$$

which has five parameters $\lambda _ { 1 0 } , \lambda _ { 0 1 } , \sigma ( x ) , \sigma ( y )$ , and $\rho$ . From Eq. (A.17.1) note that if $\rho = 0$ , $f ( x , y )$ may be factored into $f ( x , y ) = g ( x ) h ( y )$ . Hence, $\rho = 0$ is a sufficient condition for statistical independence of bivariate normal variables. This is not true for most density functions.

# A.18 MARGINAL DISTRIBUTIONS

It can be shown that each of the random variables in Eq. (A.17.1) is normally distributed. By carrying out the integral,

$$
g \left( x \right) = \int _ { - \infty } ^ { \infty } f \left( x , y \right) d y .
$$

It can be shown that

$$
g \left( x \right) = \frac { 1 } { \sqrt { 2 \pi } \sigma ( x ) } \exp \left[ - \frac { 1 } { 2 } \left( \frac { x - \lambda _ { 1 0 } } { \sigma ( x ) } \right) ^ { 2 } \right]
$$

which is the normal density function of $X$ . Similar results exist for the marginal distribution of $Y$ . The converse is not true—if the marginal distributions $g ( x )$ and $h ( y )$ are normal, the joint density function $f \left( x , y \right)$ is not necessarily bivariate normal.

Now consider the conditional density function

$$
h \left( y / x \right) = \frac { f \left( x , y \right) } { g ( x ) }
$$

for the normal distribution. The numerator and denominator are given by Eqs. (A.17.1) and (A.18.2), respectively. Inserting these in Eq. (A.18.3) and simplifying, we obtain

$$
\begin{array} { l } { { \displaystyle h \left( y / x \right) = \frac { 1 } { \sigma ( y ) \sqrt { 2 \pi } \sqrt { 1 - \rho ^ { 2 } } } } } \\ { { \displaystyle \times \exp - \frac { 1 } { 2 } \left[ \frac { y - \left\{ \lambda _ { 0 1 } + [ \rho \sigma ( y ) / \sigma ( x ) ] [ x - \lambda _ { 1 0 } ] \right\} } { \sigma ( y ) \sqrt { 1 - \rho ^ { 2 } } } \right] ^ { 2 } . } } \end{array}
$$

Hence, the conditional density function of $Y$ is normal with conditional mean

$$
E \left( Y / x \right) = \lambda _ { 0 1 } + \rho \frac { \sigma ( y ) } { \sigma ( x ) } [ x - \lambda _ { 1 0 } ]
$$

and conditional standard deviation

$$
\sigma ( Y / x ) = \sigma ( y ) \sqrt { 1 - \rho ^ { 2 } } .
$$

Thus the conditional as well as the marginal distribution of the bivariate normal distribution are normal. A graphic example of the conditional density function follows.

![](images/6bb31af82a80d1f1f79ae535a73e90db770978979275c49137345a2b458ef7e8.jpg)

# A.19 THE MULTIVARIATE NORMAL DISTRIBUTION

For the multivariate case, consider a vector of random variables; for example,

$$
\begin{array} { r } { \mathbf { X } = \left[ \begin{array} { l } { x _ { 1 } } \\ { x _ { 2 } } \\ { \vdots } \\ { x _ { p } } \end{array} \right] . } \end{array}
$$

The multivariate normal density function is given by

$$
f ( x _ { 1 } , x _ { 2 } , \ldots , x _ { p } ) = { \frac { 1 } { ( 2 \pi ) ^ { p / 2 } | V | ^ { 1 / 2 } } } e ^ { - 1 / 2 } \left( \mathbf { X } - \mathbf { \Lambda } \right) ^ { T } V ^ { - 1 } \left( \mathbf { X } - \mathbf { \Lambda } \right)
$$

where

$V$ is the $p \times p$ variance-covariance matrix of the vector $\mathbf { X }$ $| V |$ is the determinant of $V$   
$\pmb { \Lambda }$ is a $p \times 1$ vector of mean values of $X$ .

The matrix $V$ is defined as

$$
V = E \left\{ [ \mathbf { X } - \pmb { \Lambda } ] [ \mathbf { X } - \pmb { \Lambda } ] ^ { T } \right\}
$$

in terms of the correlation coefficient

$$
\begin{array} { l } { \rho _ { i j } = \frac { \mu _ { i j } } { \sigma ( x _ { i } ) \sigma ( x _ { j } ) } \qquad ( \mathcal { L } } \\ { V = \left[ \begin{array} { c c c c c c } { \sigma ^ { 2 } ( x _ { 1 } ) } & { \rho _ { 1 2 } \sigma ( x _ { 1 } ) \sigma ( x _ { 2 } ) \rho _ { 1 3 } \sigma ( x _ { 1 } ) \sigma ( x _ { 3 } ) \cdots \rho _ { 1 p } \sigma ( x _ { 1 } ) \sigma ( x _ { p } ) } \\ { \rho _ { 1 2 } \sigma ( x _ { 1 } ) \sigma ( x _ { 2 } ) } & { \sigma ^ { 2 } ( x _ { 2 } ) } & { \rho _ { 2 3 } \sigma ( x _ { 2 } ) \sigma ( x _ { 3 } ) \cdots \rho _ { 2 p } \sigma ( x _ { 2 } ) \sigma ( x _ { p } ) } \\ { \vdots } & & & & \\ { \rho _ { 1 p } \sigma ( x _ { 1 } ) \sigma ( x _ { p } ) \rho _ { 2 p } \sigma ( x _ { 2 } ) \sigma ( x _ { p } ) } & { \cdots } & { \cdots } & { \sigma ^ { 2 } ( x _ { p } ) } \end{array} \right] } \\ { \rho _ { 1 { p } } \qquad } \end{array} .
$$

Equation (A.19.1) is called the multivariate normal density function of a vector $\mathbf { X }$ with mean $\pmb { \Lambda }$ and variance-covariance $V$ .

The following theorems illustrate useful properties of multivariate normal density functions.

Theorem 1: If the random variables $x _ { 1 }$ , $x _ { 2 } \ldots x _ { p }$ are jointly normal, the joint marginal distribution of any subset of $s < p$ of the random variables is the $s$ -variate normal. For a proof, see Chapter 3 of Graybill (1961).

Theorem 2: If the $p \times 1$ vector $\mathbf { X }$ has the multivariate normal distribution with mean $\pmb { \Lambda }$ and covariance $V$ , then the components, $x _ { i }$ , are jointly independent if and only if the covariance of $x _ { i }$ and $x _ { j }$ for all $i \neq j$ is zero, that is, if and only if the covariance matrix $V$ is diagonal.

To prove this, we must show that the joint density function factors into the product of the marginal density functions, which by Theorem 1 are also normal. Hence, we must show that

$$
f ( x _ { 1 } , x _ { 2 } \ldots x _ { p } ) = f \left( x _ { 1 } \right) f \left( x _ { 2 } \right) \ldots f \left( x _ { p } \right)
$$

where

$$
f \left( x _ { 1 } , x _ { 2 } \ldots x _ { p } \right) = \kappa e ^ { - 1 / 2 ( \mathbf { X } - \mathbf { A } ) ^ { T } V ^ { - 1 } ( \mathbf { X } - \mathbf { A } ) }
$$

and

$$
f \left( x _ { i } \right) = \frac { 1 } { \sqrt { 2 \pi V _ { i i } } } e ^ { - 1 / 2 } \frac { ( x _ { i } - \lambda _ { i } ) ^ { 2 } } { V _ { i i } }
$$

$$
\kappa = \frac { 1 } { ( 2 \pi ) ^ { p / 2 } | V | ^ { 1 / 2 } }
$$

where $V _ { i i }$ indicates the diagonal elements of $V$ .

If $V _ { i j } = 0$ for $i \neq j$ , we have

$$
( \mathbf { X } - \mathbf { A } ) ^ { T } V ^ { - 1 } ( \mathbf { X } - \mathbf { A } ) = \sum _ { i = 1 } ^ { p } ( x _ { i } - \lambda _ { i } ) ^ { 2 } V _ { i i } ^ { - 1 } .
$$

Also,

$$
| V | ^ { 1 / 2 } = \prod _ { i = 1 } ^ { p } ( V _ { i i } ) ^ { 1 / 2 }
$$

since $V$ is a diagonal matrix. Consequently, the joint density function can be factored as indicated by Eq. (A.19.4) and the elements of $X$ are independent.

# A.19.1 THE CONDITIONAL DISTRIBUTION FOR MULTIVARIATE NORMAL VARIABLES

Theorem 3: If the $p \times 1$ vector $\mathbf { X }$ is normally distributed with mean $\pmb { \Lambda }$ and covariance $V$ and if the vector $\mathbf { X }$ is partitioned into two subvectors such that

$$
\mathbf { X } = \left[ \mathbf { X } _ { 1 } \right] , \mathbf { \Lambda } \mathbf { N } = \left[ \mathbf { \Lambda } _ { 1 } ^ { } \mathbf { 1 } _ { } \right] , { \mathrm { a n d } } \quad V = \left[ V _ { 1 1 } V _ { 1 2 } \right]
$$

then the conditional distribution of the $q \times 1$ vector $\mathbf { X } _ { 1 }$ , given that the vector ${ \bf X } _ { 2 } ~ = ~ { \bf x } _ { 2 }$ , is the multivariate normal distribution with mean $\Lambda _ { 1 } +$ $V _ { 1 2 } V _ { 2 2 } ^ { - 1 } \left( \mathbf { x } _ { 2 } { - } \mathbf { \mathbf { { A } } } _ { 2 } \right)$ and the covariance matrix $\left( V _ { 1 1 } { - } V _ { 1 2 } V _ { 2 2 } ^ { - 1 } V _ { 2 1 } \right)$ (Graybill, 1961); that is,

$$
\begin{array} { r l } & { g \left( \mathbf { X } _ { 1 } / \mathbf { X } _ { 2 } \ = \ \mathbf { x } _ { 2 } \right) = } \\ & { \frac { 1 } { \kappa ^ { * } } e ^ { - 1 / 2 [ \mathbf { X } _ { 1 } - \Lambda _ { 1 } - V _ { 1 2 } V _ { 2 2 } ^ { - 1 } ( \mathbf { x } _ { 2 } - \Lambda _ { 2 } ) ] ^ { T } [ V _ { 1 1 } - V _ { 1 2 } V _ { 2 2 } ^ { - 1 } V _ { 2 1 } ] ^ { - 1 } [ \mathbf { X } _ { 1 } - \Lambda _ { 1 } - V _ { 1 2 } V _ { 2 2 } ^ { - 1 } ( \mathbf { x } _ { 2 } - \Lambda _ { 2 } ) ] } } \end{array}
$$

where

$$
\kappa ^ { * } = ( 2 \pi ) ^ { q / 2 } | V _ { 1 1 } - V _ { 1 2 } V _ { 2 2 } ^ { - 1 } V _ { 2 1 } | ^ { 1 / 2 } .
$$

Theorem 4: The covariance matrix of the conditional distribution of $\mathbf { X } _ { 1 }$ , given ${ \bf X } _ { 2 } = { \bf x } _ { 2 }$ does not depend on $\mathbf { x } _ { 2 }$ .

Proof: The proof of this is obvious from an examination of Eq. (A.19.5); that is, $V _ { \mathbf { X } _ { 1 } / \mathbf { X } _ { 2 } = \mathbf { x } _ { 2 } } = V _ { 1 1 } - V _ { 1 2 } V _ { 2 2 } ^ { - 1 } V _ { 2 1 }$ . From Theorem 3, we also have

$$
E \left( \mathbf { X } _ { 1 } / \mathbf { X } _ { 2 } \ = \ \mathbf { x } _ { 2 } \right) = \Lambda _ { 1 } + V _ { 1 2 } V _ { 2 2 } ^ { - 1 } ( \mathbf { x } _ { 2 } \ - \ \mathbf { \Lambda } \mathbf { \Lambda } \mathbf { \Lambda } \mathbf { . } ) .
$$

If we were attempting to estimate $\mathbf { X } _ { 1 }$ , its mean value given by Eq. (A.19.6) would be a likely value to choose. Also, because the covariance of the conditional density function is independent of $\mathbf { x } _ { 2 }$ , we could generate the covariance without actually knowing the values of $\mathbf { X } _ { 2 }$ . This would allow us to perform an accuracy assessment of $\mathbf { X } _ { 1 }$ without knowing the values of $\mathbf { X } _ { 2 }$ .

# A.20 THE CENTRAL LIMIT THEOREM

If we have $n$ independent random variables $x _ { i }$ , $i = 1 \dots n$ that are identically distributed with common means $E [ x _ { i } ] = \lambda$ and (finite) variance $\sigma ^ { 2 } \left( x _ { i } \right) =$ $\sigma ^ { 2 }$ , and we form the sum

$$
W = x _ { 1 } + x _ { 2 } + \ldots x _ { n }
$$

whose mean and variance are given by

$$
\begin{array} { c } { { E \left[ W \right] = n \lambda } } \\ { { E \left( W - E \left( W \right) \right) ^ { 2 } = \sigma ^ { 2 } ( W ) = n \sigma ^ { 2 } . } } \end{array}
$$

The central limit theorem states that as $n \to \infty$ the standardized random variable of the sum

$$
Z = { \frac { W - E \left( W \right) } { \sigma \left( W \right) } }
$$

is normally distributed with mean 0 and variance 1 (Freeman, 1963). The important point is that $W$ also is distributed normally. Hence, any random variable made up of the sum of enough independent random components from the same distribution will be distributed normally. Furthermore, if $n > 3 0$ , $Z$ (and $W$ ) will be distributed normally no matter what the shape of the distribution (Walpole et al., 2002).

Another way of stating the theorem is that if sets of random samples are taken from any population, the means of these samples will tend to be distributed normally as the size of the samples becomes large (Davis, 1986).

The utility of the central limit theorem for orbit determination is that it gives some assurance that observation errors in tracking systems will tend to be distributed normally. This is because tracking system errors are usually the sum of a number of small random errors from a number of sources, including the hardware, the electronics, the mountings, and so on. This is a fundamental assumption in our development of statistical estimation algorithms.

# A.21 BAYES THEOREM

One form of Bayes theorem is simply a statement of the conditional density functions given by Eq. (A.12.2),

$$
g \left( x / y \right) = \frac { f \left( x , y \right) } { h \left( y \right) }
$$

and

$$
h \left( y / x \right) = \frac { f \left( x , y \right) } { g \left( x \right) } .
$$

Hence,

$$
g \left( x / y \right) = \frac { h \left( y / x \right) g \left( x \right) } { h \left( y \right) } .
$$

The last equations for $g \left( x / y \right)$ is the most elementary form of Bayes theorem. It is a useful starting point in the development of statistically based estimation criteria.

If we define $X$ to be the state vector and $Y$ to be the observation vector, then $g \left( x / y \right) \equiv a$ posteriori density function $h \left( y / x \right) \equiv a$ priori density function.

From a Bayesian viewpoint, we wish to develop a filter to propagate as a function of time the probability density function of the desired quantities conditioned on knowledge of the actual data coming from the measurement devices. Once such a conditional density function is propagated, the optimal estimate can be defined. Possible choices for the optimal estimate include:

1. The mean – the “cent er of the probability mass” distribution.   
2. The mode – the value of $x$ that has the highest probability, locating the peak of the density function.   
3. The median – the value of $x$ such that half the probability weight lies to the left and half to the right.

![](images/7428ef121f4ab20f270a569714e2dcb86bba431369962f93411639e2aa6c00b2.jpg)

By generating the density function, some judgment can be made as to which criterion defines the most reasonable estimate for a given purpose.

It is useful to examine the difference between the mean and median of a density function. Recall that the mean is defined as

$$
\lambda = \intop _ { - \infty } ^ { \infty } x f \left( x \right) d x
$$

and the median, $M$ , is defined as

$$
M = \intop _ { - \infty } ^ { M } f \left( x \right) d x = 1 / 2 .
$$

As an example, consider a bimodal distribution:

![](images/41dc79eba0db478e1c6face81a285c52b7d6f59c3f56e8d490813c4fa3778621.jpg)

If we move the second mode further out without changing the density function between the origin and the median, the median remains fix ed but the mean moves to the right.

![](images/9033807cc62b7617250ae7adb43217c51b74b1bc0295a1aceb7d31ab5b00e328.jpg)

# A.22 STOCHASTIC PROCESSES

Previously we have considered random variables that were not functions of time. Assume that we are given an experiment $\beta$ specified by its outcomes $\eta$ forming the space $S$ and by the probabilities of these events. To every outcome $\eta$ we now assign a time function $X \left( t , \eta \right)$ . We have thus created a family of functions, one for each $\eta$ . This family is called a stochastic process. A stochastic process is a function of two variables, $t$ and $\eta$ . The domain of $\eta$ is $S$ and the domain of $t$ is a set of real numbers the time axis (Papoulis, 1991).

For a specific outcome $\eta _ { i }$ , the expression $X \left( t , \eta _ { i } \right)$ signifies a single time function. For a specific time $t _ { i }$ , $X \left( t _ { i } , \eta \right)$ is a quantity depending on $\eta$ (i.e., a random variable). Finally, $X \left( t _ { i } , \eta _ { i } \right)$ is a mere number. In the future, $X \left( t , \eta \right)$ will be written $X \left( t \right)$ .

As an example, consider a coin tossing experiment and define $X \left( t \right)$ so that

$$
X \left( t \right) = \sin t , \mathrm { i f } \eta = \mathrm { h e a d s } ; X \left( t \right) = \cos t , \mathrm { i f } \eta = \mathrm { t a i l s } .
$$

Thus $X \left( t \right)$ consists of two regular curves; it is nevertheless a stochastic process. From the preceding, we see that $X \left( t , \eta \right)$ represents four different things:

1. A family of time functions $t$ and $\eta$ variable).

2. A single time function $t$ variable, $\eta$ fix ed).

3. A random variable $\mathbf { \chi } _ { t }$ fix ed, $\eta$ variable).

4. A single number $t$ fix ed, $\eta$ fixed).

We shall assume that $X \left( t \right)$ is a real process. For a specific $t , X \left( t \right)$ is a random variable. As in the case of random variables, we have a distribution function given by

$$
F \left( x , t \right) = p \left( X \left( t \right) \leq x \right) .
$$

This is interpreted as: Given two real numbers $x$ and $t$ , the function $\boldsymbol { F } \left( \boldsymbol { x } , t \right)$ equals the probability of the event $\left\{ X \left( t \right) \ \leq \ x \right\}$ consisting of all outcomes $\eta$ such that at the specified time $t$ , the functions $X \left( t \right)$ of our process do not exceed the given number $x$ .

Associated with the distribution function is the corresponding density function

$$
f \left( x , t \right) = \frac { \partial F \left( x , t \right) } { \partial x } .
$$

These results hold at a given time and are known as the fir st order distribution and density function, respectively.

Now given two time instances $t _ { 1 }$ and $t _ { 2 }$ , consider the random variable $X \left( t _ { 1 } \right)$ and $X \left( t _ { 2 } \right)$ . Their joint distribution depends, in general, on $t _ { 1 }$ and $t _ { 2 }$ and will be denoted by $F \left( x _ { 1 } , x _ { 2 } , t _ { 1 } , t _ { 2 } \right)$

$$
F \left( x _ { 1 } , x _ { 2 } , t _ { 1 } , t _ { 2 } \right) = p \left\{ X \left( t _ { 1 } \right) \leq x _ { 1 } , X \left( t _ { 2 } \right) \leq x _ { 2 } \right\}
$$

and will be called the second-order distribution function of the process $X \left( t \right)$ . The corresponding density function is

$$
f \left( x _ { 1 } , x _ { 2 } , t _ { 1 } , t _ { 2 } \right) = \frac { \partial ^ { 2 } { \cal F } } { \partial x _ { 1 } \partial x _ { 2 } } \left( x _ { 1 } , x _ { 2 } , t _ { 1 } , t _ { 2 } \right) .
$$

The marginal distribution and density functions are given by

$$
\begin{array} { c } { F \left( x _ { 1 } , \infty , t _ { 1 } , t _ { 2 } \right) = F \left( x _ { 1 } , t _ { 1 } \right) , } \\ { \infty } \\ { f \left( x _ { 1 } , t _ { 1 } \right) = \displaystyle \int _ { - \infty } ^ { \infty } f \left( x _ { 1 } , x _ { 2 } , t _ { 1 } , t _ { 2 } \right) d x _ { 2 } . } \end{array}
$$

The conditional density is

$$
f ( X ( t _ { 1 } ) / X ( t _ { 2 } ) = ( x _ { 2 } ) = \frac { f ( x _ { 1 } , x _ { 2 } , t _ { 1 } , t _ { 2 } ) } { f ( x _ { 2 } , t _ { 2 } ) } .
$$

# A.22.1 DEFINITIONS FOR STOCHASTIC PROCESSES

Given a stochastic process $X ( t )$ , its mean ${ \boldsymbol { \eta } } \left( t \right)$ is given by the expected value of the random variable $X \left( t \right)$ ,

$$
\eta \left( t \right) = E \left\{ X \left( t \right) \right\} = \intop _ { - \infty } ^ { \infty } x f \left( x , t \right) d x .
$$

It is in general a function of time.

The autocorrelation $R \left( t _ { 1 } , t _ { 2 } \right)$ of a process $X \left( t \right)$ is the joint moment of the random variables $X \left( t _ { 1 } \right)$ and $X \left( t _ { 2 } \right)$

$$
\begin{array} { l } { { R \left( t _ { 1 } , t _ { 2 } \right) = E \left\{ X \left( t _ { 1 } \right) X \left( t _ { 2 } \right) \right\} } } \\ { { \infty \ \displaystyle \int \displaylimits _ { - \infty } ^ { \infty } \int \displaylimits _ { - \infty } ^ { \infty } f \left( x _ { 1 } , x _ { 2 } , t _ { 1 } , t _ { 2 } \right) d x _ { 1 } d x _ { 2 } } } \\ { { \displaystyle \qquad - \infty - \infty } } \end{array}
$$

and is a function of $t _ { 1 }$ and $t _ { 2 }$ . The autocorrelation is analogous to the moment about the origin.

The autocovariance of $X \left( t \right)$ is the covariance of the random variables $X \left( t _ { 1 } \right)$ and $X \left( t _ { 2 } \right)$ ,

$$
C \left( t _ { 1 } , t _ { 2 } \right) = E \left\{ \left[ X \left( t _ { 1 } \right) - \eta \left( t _ { 1 } \right) \right] \left[ X \left( t _ { 2 } \right) - \eta \left( t _ { 2 } \right) \right] \right\} .
$$

If we have two stochastic processes $X \left( t \right)$ and $Y \left( t \right)$ , these become the crosscorrelation and cross-covariance, respectively. From Eq. (A.22.9), it is seen that

$$
C \left( t _ { 1 } , t _ { 2 } \right) = R \left( t _ { 1 } , t _ { 2 } \right) - \eta \left( t _ { 1 } \right) \eta \left( t _ { 2 } \right) .
$$

The variance of the random variable $X \left( t _ { 1 } \right)$ is given by $( t _ { 1 } ~ = ~ t _ { 2 }$ )

$$
C \left( t _ { 1 } , t _ { 1 } \right) = R \left( t _ { 1 } , t _ { 1 } \right) - \eta ^ { 2 } ( t _ { 1 } ) .
$$

Two random processes $X ( t ) , Y ( t )$ are called uncorrelated if for any $t _ { 1 }$ and $t _ { 2 }$ we have

$$
R _ { X Y } \left( t _ { 1 } , t _ { 2 } \right) = E \left[ X \left( t _ { 1 } \right) Y \left( t _ { 2 } \right) \right] = \eta _ { x } \left( t _ { 1 } \right) \eta _ { y } \left( t _ { 2 } \right) ;
$$

that is,

$$
C _ { X Y } \left( t _ { 1 } , t _ { 2 } \right) = 0 .
$$

They are called orthogonal if

$$
R _ { X Y } \left( t _ { 1 } , t _ { 2 } \right) = 0 .
$$

A stochastic process $X \left( t \right)$ is stationary in the strict sense if its statistics are not affected by a shift in the time origin. This means that the two processes

$$
X \left( t \right) \ \mathrm { a n d } X \left( t + \epsilon \right)
$$

have the same statistics for any $\epsilon$ .

As a result

$$
f \left( x , t \right) = f \left( x , t + \epsilon \right)
$$

and since this is true for every $\epsilon$ , we must have the first-order density

$$
f \left( x , t \right) = f \left( x \right)
$$

independent of time, and

$$
E \left[ X \left( t \right) \right] = \eta , \mathrm { a c o n s t a n t . }
$$

The density of order two must be such that

$$
f \left( x _ { 1 } , x _ { 2 } , t _ { 1 } , t _ { 2 } \right) = f \left( x _ { 1 } , x _ { 2 } , t _ { 1 } + \epsilon , t _ { 2 } + \epsilon \right) .
$$

Because this must be true for any $\epsilon$ , it must be a function of only $t _ { 1 } ~ - ~ t _ { 2 }$ . This can be seen by noting that $t _ { 1 } + \epsilon - ( t _ { 2 } + \epsilon ) = t _ { 1 } - t _ { 2 }$ is not dependent on $\epsilon$ , hence

$$
f \left( x _ { 1 } , x _ { 2 } , t _ { 1 } , t _ { 2 } \right) = f \left( x _ { 1 } , x _ { 2 } , \tau \right)
$$

where $\tau ~ = ~ ( t _ { 1 } ~ - ~ t _ { 2 } )$ . Thus, $f \left( x _ { 1 } , x _ { 2 } , \tau \right)$ is the joint density function of the random variables

$$
X \left( t + \tau \right) \quad { \mathrm { a n d } } \quad X \left( \tau \right) .
$$

# A.23 REFERENCES

Davis, J. C., Statistics and Data Analysis in Geology, John Wiley & Sons Inc., New York, 1986.

Freeman, H., Introduction to Statistical Inference, Addison-Wesley, 1963.

Graybill, F. A., An Introduction to Linear Statistical Models, McGraw-Hill, New York, 1961.

Helstrom, C. W., Probability and Stochastic Processes for Engineers, MacMillan, New York, 1984.

Papoulis, A., Probability, Random Variables, and Stochastic Processes, McGraw-Hill, New York, 1991.

Walpole, R. E., R. H. Myers, S. L. Myers, and Y. Keying, Probability and Statistics for Engineers and Scientists, Prentice Hall, Englewood Cliffs, NJ, 2002.

# Appendix B

# Review of Matrix Concepts

# B.1 INTRODUCTION

The following matrix notation, definitions, and theorems are used extensively in this book. Much of this material is based on Graybill (1961).

• A matrix A will have elements denoted by $a _ { i j }$ , where $i$ refers to the row and $j$ to the column.   
• ${ \mathbf A } ^ { T }$ will denote the transpose of A.   
• ${ \bf A } ^ { - 1 }$ will denote the inverse of A.   
• $| \mathbf { A } |$ will denote the determinant of A.   
• The dimension of a matrix is the number of its rows by the number of its columns.   
• An $n \times m$ matrix A will have $n$ rows and $m$ columns.   
• If $m \ : = \ : 1$ , the matrix will be called an $n \times 1$ vector.   
• Given the matrices $\mathbf { A } \ = \ ( a _ { i j } )$ and $\mathbf { B } \ = \ ( b _ { i j } )$ , the product $\mathbf { A } \mathbf { B } \ = \mathbf { C } \ =$ $\left( c _ { i j } \right)$ is defined as the matrix $\mathbf { C }$ with the pqth element equal to

$$
\sum _ { s = 1 } ^ { m } a _ { p s } b _ { s q }
$$

where $m$ is the column dimension of $\mathbf { A }$ and the row dimension of $\mathbf { B }$ .

• Given

and

$$
\begin{array} { r } { \mathbf { A } = \left[ \begin{array} { l } { \mathbf { A } _ { 1 1 } \mathbf { A } _ { 1 2 } } \\ { \mathbf { A } _ { 2 1 } \mathbf { A } _ { 2 2 } } \end{array} \right] } \\ { \mathbf { B } = \left[ \begin{array} { l } { \mathbf { B } _ { 1 1 } \mathbf { B } _ { 1 2 } } \\ { \mathbf { B } _ { 2 1 } \mathbf { B } _ { 2 2 } } \end{array} \right] } \end{array}
$$

then

$$
{ \begin{array} { r l } & { \mathbf { A B } = { \left[ \mathbf { A } _ { 1 1 } \mathbf { A } _ { 1 2 } \right] } \left[ \mathbf { B } _ { 1 1 } \mathbf { B } _ { 1 2 } \right] } \\ & { \qquad \mathbf { A } _ { 2 1 } \mathbf { A } _ { 2 2 } { \Bigg ] } \left[ \mathbf { B } _ { 2 1 } \mathbf { B } _ { 2 2 } \right] } \\ & { \qquad = { \left[ \mathbf { A } _ { 1 1 } \mathbf { B } _ { 1 1 } + \mathbf { A } _ { 1 2 } \mathbf { B } _ { 2 1 } \mathbf { A } _ { 1 1 } \mathbf { B } _ { 1 2 } + \mathbf { A } _ { 1 2 } \mathbf { B } _ { 2 2 } \right] } } \\ & { \qquad \mathbf { A } _ { 2 1 } \mathbf { B } _ { 1 1 } + \mathbf { A } _ { 2 2 } \mathbf { B } _ { 2 1 } \mathbf { A } _ { 2 1 } \mathbf { B } _ { 1 2 } + \mathbf { A } _ { 2 2 } \mathbf { B } _ { 2 2 } { \Bigg ] } } \end{array} }
$$

provided the elements of $\mathbf { A }$ and $\mathbf { B }$ are conformable.

• For AB to be defined, the number of columns in A must equal the number of rows in $\mathbf { B }$ .   
• For $\textbf { A + B }$ to be defined, A and $\mathbf { B }$ must have the same dimension.   
• The transpose of ${ \mathbf A } ^ { T }$ equals A; that is, $( \mathbf { A } ^ { T } ) ^ { T } = \mathbf { A }$ .   
• The inverse of ${ { \bf A } ^ { - 1 } }$ is $\mathbf { A }$ ; that is, $( \mathbf { A } ^ { - 1 } ) ^ { - 1 } = \mathbf { A }$ .   
• The transpose and inverse symbols may be permuted; that is, $\begin{array} { r l } { ( \mathbf { A } ^ { T } ) ^ { - 1 } } & { { } = } \end{array}$ $( \mathbf { A } ^ { - 1 } ) ^ { T }$ .   
• $( \mathbf { A } \mathbf { B } ) ^ { T } \ : = \ : \mathbf { B } ^ { T } \ : \mathbf { A } ^ { T } .$   
• $( \mathbf { A } \mathbf { B } ) ^ { - 1 } \ : = \ : \mathbf { B } ^ { - 1 } \mathbf { A } ^ { - 1 }$ if $\mathbf { A }$ and $\mathbf { B }$ are each nonsingular.   
• A scalar commutes with every matrix; that is, $k \mathbf { A } = \mathbf { A } k$ .   
• For any matrix A, we have $\mathbf { I A } = \mathbf { A I } = \mathbf { A }$ .   
• All diagonal matrices of the same dimension are commutative.   
• If $\mathbf { D } _ { 1 }$ and $\mathbf { D } _ { 2 }$ are diagonal matrices, then the product is diagonal.   
• If $\mathbf { X }$ and $\mathbf { Y }$ are vectors and if $\mathbf { A }$ is a nonsingular matrix and if the equation $\mathbf { Y } \ = \ \mathbf { A } \mathbf { X }$ holds, then $\mathbf { X } = \mathbf { A } ^ { - 1 } \mathbf { Y }$ .