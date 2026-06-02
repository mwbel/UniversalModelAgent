# Chapter 6

# Consider Covariance Analysis

# 6.1 INTRODUCTION

The design and subsequent performance of the statistical estimation algorithms used for orbit determination, parameter identification, and navigation applications are dependent on the accuracy with which the dynamic system and the measurements used to observe the motion can be modeled. In particular, the design of orbit determination algorithms usually begins with the defini tion of the important error sources and a statistical description of these error sources. The effect of erroneous assumptions regarding (1) the mathematical description of the force model or the measurement model, (2) the statistical properties of the random errors, and (3) the accuracy of the numerical values assigned to the unestimated measurement and force model parameters, as well as the round-off and truncation characteristics that occur in the computation process, can lead to reduced estimation accuracy and, on occasion, to fil ter divergence. The general topic of covariance analysis treats the sensitivity of the estimation accuracy to these error sources. The first topic to be treated here is the effects of errors in the constant, but nonestimated, dynamic, and measurement model parameters. Errors of this nature lead to biased estimates. A second topic to be considered is the effect of errors in statistics such as the data noise covariance and the a priori state covariance.

On occasion it may be advantageous to ignore (i.e., not estimate) certain unknown or poorly known model parameters. Consider covariance analysis is a technique to assess the impact of neglecting to estimate these parameters on the accuracy of the state estimate.

The reasons for neglecting to estimate certain parameters are:

1. It is cost effective in computer cost, memory requirements, and execution time to use as small a parameter array as possible. 2. Large dimension parameter arrays may not be “totally” observable from an observation set collected over a short time interval.

Consider covariance analysis is a “des ign tool” that can be used for sensitivity analysis to determine the optimal parameter array for a given estimation problem or to structure an estimation algorithm to achieve a more robust performance in the presence of erroneous force and/or measurement model parameters.

Covariance analysis is an outgrowth of the study of the effects of errors on an estimate of the state of a dynamical system. These errors manifest themselves as:

1. Large residuals in results obtained with a given estimation algorithm.   
2. Divergence in the sequential estimation algorithms.   
3. Incorrect navigation decisions based on an optimistic state error covariance.

As discussed in Chapter 4, the operational “fix” for the Kalman or sequential filter divergence problem caused by optimistic state error covariance estimates is the addition of process noise. In an application, the process noise model will cause the filter to place a higher weight on the most recent data. For the batch estimate, a short-arc solution, which reduces the time interval for collecting the batch of observations, can be used to achieve a similar result. Neither approach is very useful as a design tool.

The comments in the previous paragraphs can be summarized as follows. Consider covariance analysis, in the general case, attempts to quantify the effects of:

a. Nonestimated parameters, C, whose uncertainty is neglected in the estimation procedure. b. Incorrect a priori covariance for the a priori estimate of $\mathbf { X }$ . c. Incorrect a priori covariance for the measurement noise.

A consider filter will use actual data along with a priori information on certain consider parameters to improve the filter divergence characteristics due to errors in the dynamic and measurement models. The effects of bias in the unestimated model parameters is the most important of these effects and will be given primary emphasis in the following discussion.

# 6.2 BIAS IN LINEAR ESTIMATION PROBLEMS

Errors in the constant parameters that appear in the dynamic and/or measurement models may have a random distribution a priori. However, during any estimation procedure the values will be constant but unknown and, hence, must be treated as a bias. Bias errors in the estimation process are handled in one of three ways:

1. Neglected. The estimate of the state is determined, neglecting any errors in the nonestimated force model and measurement model parameters. 2. Estimated. The state vector is expanded to include dynamic and measurement model parameters that may be in error. 3. Considered. The state vector is estimated but the uncertainty in the nonestimated parameters is included in the estimation error covariance matrix. This assumes that the nonestimated parameters are constant and that their $a$ priori estimate and associated covariance matrix is known.

In sequential filteri ng analysis, an alternate approach is to compensate for the effects of model errors through the addition of a process noise model, as discussed in Section 4.9 of Chapter 4.

# 6.3 FORMULATION OF THE CONSIDER COVARIANCE MATRIX

Consider the following partitioning of the generalized state vector $\mathbf { z }$ , and observation-state mapping matrix $H$ ,

$$
\mathbf { z } = \left[ \mathbf { x } \right] , H = [ H _ { x } ; H _ { c } ]
$$

where $\mathbf { x }$ is an $n \times 1$ vector of state variables whose values are to be estimated and $\mathbf { c }$ is a $q \times 1$ vector of measurement and force model variables whose values are uncertain but whose values will not be estimated. Note that we are considering a linearized system so that c represents a vector of deviations between the true and nominal values of the consider parameters, $\mathbf { C }$ ,

$$
\mathbf { c } = \mathbf { C } - \mathbf { C } ^ { * } .
$$

The measurement model for the $i ^ { \mathrm { t h } }$ observation,

$$
\mathbf { y } _ { i } = H _ { i } \mathbf { z } _ { i } + \epsilon _ { i } , i = 1 , \ldots , l
$$

can be expressed as

$$
{ \bf y } _ { i } = H _ { x _ { i } } { \bf x } + H _ { c _ { i } } { \bf c } + \epsilon _ { i } , i = 1 , \ldots , l .
$$

Assume that an $a$ priori estimate of $\mathbf { x }$ and associated covariance (e.g., $( \overline { { \mathbf { x } } } , \overline { { P } } _ { x } ) $ ) is given along with c, an a priori estimate of $\mathbf { c }$ . The filt er equations can be derived by following the procedures used in Chapter 4. The relevant equations are

$$
{ \bf y } = H _ { x } { \bf x } + H _ { c } { \bf c } + \epsilon
$$

where

$$
\mathbf { y } = \left[ \begin{array} { c } { \mathbf { y } _ { 1 } } \\ { \mathbf { y } _ { 2 } } \\ { \vdots } \\ { \mathbf { y } _ { l } } \end{array} \right] , H _ { x } = \left[ \begin{array} { c } { H _ { x _ { 1 } } } \\ { H _ { x _ { 2 } } } \\ { \vdots } \\ { H _ { x _ { l } } } \end{array} \right] ,
$$

$$
H _ { c } = \left[ \begin{array} { c } { H _ { c _ { 1 } } } \\ { H _ { c _ { 2 } } } \\ { \vdots } \\ { H _ { c _ { l } } } \end{array} \right] , \epsilon = \left[ \begin{array} { c } { \epsilon _ { 1 } } \\ { \epsilon _ { 2 } } \\ { \vdots } \\ { \epsilon _ { l } } \end{array} \right]
$$

and

$$
\begin{array} { r l } { \mathbf { y } _ { i } ~ } & { { } = ~ } & { p \times 1 \mathrm { ~ v e c t o r ~ o f ~ } \mathrm { { f o s e r s a i o n s } } } \\ { \mathbf { y } ~ } & { { } = ~ } & { l p \times 1 \mathrm { ~ v e c t o r ~ o f ~ } \mathrm { { o b s e r s a t i o n s } } } \\ { H _ { x _ { i } } ~ } & { { } = ~ } & { p \times n \mathrm { ~ m a t r i x } } \\ { H _ { x _ { i } } ~ } & { { } = ~ } & { l p \times n \mathrm { ~ a t r i x } } \\ { H _ { c _ { i } } ~ } & { { } = ~ } & { p \times q \mathrm { ~ m a t r i x } } \\ { H _ { c _ { i } } ~ } & { { } = ~ } & { p \times q \mathrm { ~ m a t r i x } } \\ { H _ { c } ~ } & { { } = ~ } & { l p \times q \mathrm { ~ m a t r i x } } \\ { \mathbf { x } ~ } & { { } = ~ } & { n \times 1 \mathrm { ~ s t a t e ~ v e c t o r ~ o r a t e r ~ p a r a m e t e r s } } \\ { \mathbf { c } ~ } & { { } = ~ } & { q \times 1 \mathrm { ~ v e c t o r ~ o f ~ c o n s i d e r ~ p a r a m e t o r s } } \\ { \boldsymbol { \epsilon } ~ } & { { } = ~ } & { l p \times 1 \mathrm { ~ v e c t o r ~ o f ~ o b s e r s a t i o n ~ e r m o r s } } \\ { \boldsymbol { \epsilon } _ { i } ~ } & { { } = ~ } & { p \times 1 \mathrm { ~ w e c t o r ~ o f ~ n o s e r s a t i o n ~ e r m o r s } . } \end{array}
$$

Recall that unless the observation-state relationship and the state propagation equations are linear, $\mathbf { y } , \mathbf { x }$ , and c represent observation, state, and consider parameter deviation vectors, respectively. Also,

$$
E [ \epsilon _ { i } ] = 0 , \qquad E [ \epsilon _ { i } \epsilon _ { j } ^ { T } ] = R _ { i } \delta _ { i j } ,
$$

$$
E [ \epsilon \epsilon ^ { T } ] = R = \left[ \begin{array} { c c c c } { { R _ { 1 } } } & { { } } & { { } } & { { } } \\ { { } } & { { R _ { 2 } } } & { { } } \\ { { } } & { { \ddots } } & { { } } \\ { { } } & { { } } & { { } } & { { R _ { l } } } \end{array} \right] _ { l p \times l p }
$$

where $\delta _ { i j }$ is the Kronecker delta.

A priori estimates for $\mathbf { x }$ and c are given by $\overline { { \mathbf { x } } }$ and $\overline { { \mathbf { c } } }$ , where

$$
\begin{array} { r } { \overline { { \mathbf { x } } } = \mathbf { x } + \pmb { \eta } , \overline { { \mathbf { c } } } = \mathbf { c } + \pmb { \beta } . } \end{array}
$$

The errors, $\eta$ and $\beta$ , have the following statistical properties:

$$
\begin{array} { r l } & { \quad E [ \eta ] = E [ \beta ] = 0 } \\ & { E [ \eta \eta ^ { T } ] = \overline { { P } } _ { x } } \\ & { E [ \beta \beta ^ { T } ] = \overline { { P } } _ { c c } } \\ & { E [ \eta \epsilon ^ { T } ] = E [ \beta \epsilon ^ { T } ] = 0 } \\ & { E [ \eta \beta ^ { T } ] = \overline { { P } } _ { x c } . } \end{array}
$$

It is convenient to express this information in a more compact form, such as that of a data equation. From Eqs. (6.3.4) and (6.3.7)

$$
\begin{array} { r l } & { \mathbf { y } = H _ { x } \mathbf { x } + H _ { c } \mathbf { c } + \epsilon ; \epsilon \sim ( 0 , R ) } \\ & { \overline { { \mathbf { x } } } = \mathbf { x } + \eta ; \qquad \eta \sim ( 0 , \overline { { P } } _ { x } ) } \\ & { \overline { { \mathbf { c } } } = \mathbf { c } + \boldsymbol { \beta } ; } \end{array}
$$

Let

$$
\mathbf { z } = \left[ \begin{array} { l } { \mathbf { x } } \\ { \mathbf { c } } \end{array} \right] ; \tilde { \mathbf { y } } = \left[ \begin{array} { l } { \mathbf { y } } \\ { \overline { { \mathbf { x } } } } \\ { \overline { { \mathbf { c } } } } \end{array} \right] ;
$$

$$
H _ { z } = \left[ \begin{array} { l l } { H _ { x } } & { H _ { c } } \\ { I } & { 0 } \\ { 0 } & { I } \end{array} \right] ; \tilde { \epsilon } = \left[ \begin{array} { l } { \epsilon } \\ { \eta } \\ { \beta } \end{array} \right] .
$$

It follows that the observation equations can be expressed as

$$
\tilde { \mathbf { y } } = H _ { z } \mathbf { z } + \tilde { \epsilon } ; \tilde { \mathbf { \epsilon } } \sim ( 0 , \tilde { R } )
$$

where

$$
\tilde { R } = \left[ \begin{array} { l l l } { R } & { 0 } & { 0 } \\ { 0 } & { \overline { { P } } _ { x } } & { \overline { { P } } _ { x c } } \\ { 0 } & { \overline { { P } } _ { c x } } & { \overline { { P } } _ { c c } } \end{array} \right] .
$$

We wish to determine the weighted least squares estimate of $\mathbf { z }$ , obtained by choosing the value of $\mathbf { z }$ , which minimizes the performance index

$$
J = 1 / 2 \tilde { \epsilon } \tilde { R } ^ { - 1 } \tilde { \epsilon } ^ { T } .
$$

Note that the weight has been specified as the $a$ priori data noise covariance matrix. As illustrated in Section 4.3.3, the best estimate of $\mathbf { z }$ is given by

$$
\hat { \mathbf { z } } = \left( H _ { z } ^ { T } \tilde { R } ^ { - 1 } H _ { z } \right) ^ { - 1 } H _ { z } ^ { T } \tilde { R } ^ { - 1 } \tilde { \mathbf { y } }
$$

with the associated estimation error covariance matrix

$$
\begin{array} { r } { P _ { z } = E \Big [ ( \hat { \mathbf { z } } - \mathbf { z } ) ( \hat { \mathbf { z } } - \mathbf { z } ) ^ { T } \Big ] = \Big ( H _ { z } ^ { T } \tilde { R } ^ { - 1 } H _ { z } \Big ) ^ { - 1 } . } \end{array}
$$

Equations (6.3.18) and (6.3.19) may be written in partitioned form in order to isolate the quantities of interest. First define

$$
\tilde { R } ^ { - 1 } = \left[ \begin{array} { l l l } { R ^ { - 1 } } & { 0 } & { 0 } \\ { 0 } & { \overline { { M } } _ { x x } } & { \overline { { M } } _ { x c } } \\ { 0 } & { \overline { { M } } _ { c x } } & { \overline { { M } } _ { c c } } \end{array} \right] .
$$

From

$$
\tilde { R } \tilde { R } ^ { - 1 } = I ,
$$

it can be shown that

$$
\begin{array} { r c l } { \overline { { M } } _ { x x } } & { = } & { \overline { { P } } _ { x } ^ { - 1 } + \overline { { P } } _ { x } ^ { - 1 } \overline { { P } } _ { x c } \overline { { M } } _ { c c } \overline { { P } } _ { c x } \overline { { P } } _ { x } ^ { - 1 } } \\ & { = } & { ( \overline { { P } } _ { x } - \overline { { P } } _ { x c } \overline { { P } } _ { c c } ^ { - 1 } \overline { { P } } _ { c x } ) ^ { - 1 } } \\ { \overline { { M } } _ { x c } } & { = } & { - ( \overline { { P } } _ { x } - \overline { { P } } _ { x c } \overline { { P } } _ { c c } ^ { - 1 } \overline { { P } } _ { c x } ) ^ { - 1 } \overline { { P } } _ { x c } \overline { { P } } _ { c c } ^ { - 1 } } \\ & { = } & { - \overline { { M } } _ { x x } \overline { { P } } _ { x c } \overline { { P } } _ { c c } ^ { - 1 } } \\ { \overline { { M } } _ { c x } } & { = } & { - ( \overline { { P } } _ { c c } - \overline { { P } } _ { c x } \overline { { P } } _ { x } ^ { - 1 } \overline { { P } } _ { x c } ) ^ { - 1 } \overline { { P } } _ { c x } \overline { { P } } _ { x } ^ { - 1 } = \overline { { M } } _ { x c } ^ { T } } \\ { \overline { { M } } _ { c c } } & { = } & { ( \overline { { P } } _ { c c } - \overline { { P } } _ { c x } \overline { { P } } _ { x } ^ { - 1 } \overline { { P } } _ { x c } ) ^ { - 1 } . } \end{array}
$$

From Eq. (6.3.18) it follows that

$$
\big ( H _ { z } ^ { T } \tilde { R } ^ { - 1 } H _ { z } \big ) \hat { \mathbf { z } } = H _ { z } ^ { T } \tilde { R } ^ { - 1 } \tilde { \mathbf { y } }
$$

or

$$
\left[ \begin{array} { c c } { \left( H _ { x } ^ { T } R ^ { - 1 } H _ { x } + \overline { { M } } _ { x x } \right) } & { \left( H _ { x } ^ { T } R ^ { - 1 } H _ { c } + \overline { { M } } _ { x c } \right) } \\ { \left( H _ { c } ^ { T } R ^ { - 1 } H _ { x } + \overline { { M } } _ { c x } \right) } & { \left( H _ { c } ^ { T } R ^ { - 1 } H _ { c } + \overline { { M } } _ { c c } \right) } \end{array} \right] \left[ \begin{array} { c c } { \hat { \mathbf { x } } } \\ { \hat { \mathbf { c } } } \end{array} \right]
$$

$$
\mathbf { \Psi } = \left[ \begin{array} { l } { H _ { x } ^ { T } R ^ { - 1 } y + \overline { { M } } _ { x x } \overline { { x } } + \overline { { M } } _ { x c } \overline { { c } } } \\ { H _ { c } ^ { T } R ^ { - 1 } y + \overline { { M } } _ { c x } \overline { { x } } + \overline { { M } } _ { c c } \overline { { c } } } \end{array} \right] .
$$

Rewriting Eq. (6.3.27) as

$$
\left[ \begin{array} { l l } { M _ { x x } } & { M _ { x c } } \\ { M _ { c x } } & { M _ { c c } } \end{array} \right] \left[ \begin{array} { l } { \hat { \mathbf { x } } } \\ { \hat { \mathbf { c } } } \end{array} \right] = \left[ \begin{array} { l } { \mathbf { N } _ { x } } \\ { \mathbf { N } _ { c } } \end{array} \right]
$$

leads to the simultaneous equations

$$
\begin{array} { r l r } { M _ { x x } \hat { \bf x } + M _ { x c } \hat { \bf c } } & { { } = } & { { \bf N } _ { x } } \\ { M _ { c x } \hat { \bf x } + M _ { c c } \hat { \bf c } } & { { } = } & { { \bf N } _ { c } } \end{array}
$$

where

$$
\begin{array} { l c l } { { M _ { x x } } } & { { = } } & { { H _ { x } ^ { T } R ^ { - 1 } H _ { x } + \overline { { { M } } } _ { x x } } } \\ { { M _ { x c } } } & { { = } } & { { H _ { x } ^ { T } \ R ^ { - 1 } H _ { c } + \overline { { { M } } } _ { x c } } } \\ { { M _ { c x } } } & { { = } } & { { H _ { c } ^ { T } R ^ { - 1 } \ H _ { x } + \overline { { { M } } } _ { c x } = M _ { x c } ^ { T } } } \\ { { M _ { c c } } } & { { = } } & { { H _ { c } ^ { T } R ^ { - 1 } H _ { c } + \overline { { { M } } } _ { c c } } } \\ { { { \bf N } _ { x } } } & { { = } } & { { H _ { x } ^ { T } R ^ { - 1 } { \bf y } + \overline { { { M } } } _ { x x } \overline { { { \bf x } } } + \overline { { { M } } } _ { x c } \overline { { { \bf z } } } } } \\ { { { \bf N } _ { c } } } & { { = } } & { { H _ { c } ^ { T } R ^ { - 1 } { \bf y } + \overline { { { M } } } _ { c x } \overline { { { \bf x } } } + \overline { { { M } } } _ { c c } \overline { { { \bf z } } } . } } \end{array}
$$

From Eq. (6.3.29) it follows that

$$
{ \hat { \mathbf { x } } } = M _ { x x } ^ { - 1 } \mathbf { N } _ { x } \ - \ M _ { x x } ^ { - 1 } M _ { x c } { \hat { \mathbf { c } } } .
$$

If Eq. (6.3.32) is substituted into Eq. (6.3.30), the following result is obtained:

$$
M _ { c x } ( M _ { x x } ^ { - 1 } { \mathbf { N } } _ { x } - M _ { x x } ^ { - 1 } M _ { x c } \hat { \mathbf { c } } ) + M _ { c c } \hat { \mathbf { c } } = \mathbf { N } _ { c }
$$

or

$$
( M _ { c c } - M _ { c x } M _ { x x } ^ { - 1 } M _ { x c } ) \hat { \mathbf { c } } = \mathbf { N } _ { c } - M _ { c x } M _ { x x } ^ { - 1 } \mathbf { N } _ { x }
$$

and

$$
\hat { \mathbf { c } } = ( M _ { c c } - M _ { c x } M _ { x x } ^ { - 1 } M _ { x c } ) ^ { - 1 } ( \mathbf { N } _ { c } - M _ { c x } M _ { x x } ^ { - 1 } \mathbf { N } _ { x } ) .
$$

The value for cˆ determined by Eq. (6.3.33) can be substituted into Eq. (6.3.32) to obtain $\hat { \bf x }$ .

The covariance matrix for the errors in $\hat { \bf x }$ and cˆ given by Eq. (6.3.19) can be

written in partitioned form as

$$
\left[ \begin{array} { l l } { P _ { x x } } & { P _ { x c } } \\ { P _ { c x } } & { P _ { c c } } \end{array} \right] = \left[ \begin{array} { l l } { M _ { x x } } & { M _ { x c } } \\ { M _ { c x } } & { M _ { c c } } \end{array} \right] ^ { - 1 }
$$

where $M _ { x x } , M _ { c x } , M _ { x c }$ , and $M _ { c c }$ are defined by Eq. (6.3.31). From the equation

$$
\left[ \begin{array} { l l } { M _ { x x } } & { M _ { x c } } \\ { M _ { c x } } & { M _ { c c } } \end{array} \right] \left[ \begin{array} { l l } { P _ { x x } } & { P _ { x c } } \\ { P _ { c x } } & { P _ { c c } } \end{array} \right] = \left[ \begin{array} { l l } { I } & { 0 } \\ { 0 } & { I } \end{array} \right] .
$$

It can be shown that

$$
\begin{array} { l c l } { { P _ { c x } } } & { { = } } & { { - M _ { c c } ^ { - 1 } M _ { c x } P _ { x x } } } \\ { { P _ { x c } } } & { { = } } & { { - M _ { x x } ^ { - 1 } M _ { x c } P _ { c c } } } \\ { { P _ { x x } } } & { { = } } & { { ( M _ { x x } - M _ { x c } M _ { c c } ^ { - 1 } M _ { c x } ) ^ { - 1 } } } \\ { { P _ { c c } } } & { { = } } & { { ( M _ { c c } - M _ { c x } M _ { x x } ^ { - 1 } M _ { x c } ) ^ { - 1 } . } } \end{array}
$$

Note that

$$
P _ { x c } = P _ { c x } ^ { T } .
$$

The expression for $P _ { x x }$ can be written in an alternate form. Using the Schur identity (Theorem 4 of Appendix B) and letting

$$
\begin{array} { r c l } { { A } } & { { = } } & { { M _ { x x } } } \\ { { B } } & { { = } } & { { - M _ { x c } M _ { c c } ^ { - 1 } } } \\ { { C } } & { { = } } & { { M _ { c x } , } } \end{array}
$$

it can be shown that

$$
P _ { x x } = M _ { x x } ^ { - 1 } + M _ { x x } ^ { - 1 } M _ { x c } \big ( M _ { c c } - M _ { c x } M _ { x x } ^ { - 1 } M _ { x c } \big ) ^ { - 1 } M _ { c x } M _ { x x } ^ { - 1 } .
$$

If we use the definition

$$
P _ { x } = M _ { x x } ^ { - 1 } = ( H _ { x } ^ { T } R ^ { - 1 } H _ { x } + \overline { { { M } } } _ { x x } ) ^ { - 1 } ,
$$

and define $S _ { x c }$ as (in Section 6.4 we will show Eq. (6.3.43) to be the sensitivity matrix)

$$
S _ { x c } \equiv - M _ { x x } ^ { - 1 } M _ { x c }
$$

and using Eq. (6.3.39) to define $P _ { c c }$ , we can write Eq. (6.3.41) as

$$
\begin{array} { r } { P _ { x x } = P _ { x } + S _ { x c } P _ { c c } S _ { x c } ^ { T } . } \end{array}
$$

Also, from Eqs. (6.3.37) and (6.3.44) we have

$$
P _ { x c } = S _ { x c } P _ { c c } = P _ { c x } ^ { T } .
$$

Using Eqs. (6.3.39), (6.3.42), and (6.3.44) we may write Eqs. (6.3.32) and (6.3.33) as

$$
\begin{array} { r c l } { \hat { \mathbf { x } } } & { = } & { P _ { x } \mathbf { N } _ { x } + S _ { x c } \hat { \mathbf { c } } } \\ { \hat { \mathbf { c } } } & { = } & { P _ { c c } ( \mathbf { N } _ { c } + S _ { x c } ^ { T } \mathbf { N } _ { x } ) . } \end{array}
$$

The consider estimate is obtained by choosing not to compute $\hat { \mathbf { c } }$ and $P _ { c c }$ but to fix them at their a priori values $\overline { { \mathbf { c } } }$ and $\overline { { P } } _ { c c }$ , respectively. In this case, the equations that require modification are

$$
\begin{array} { r c l } { P _ { c c } } & { = } & { \overline { { P } } _ { c c } } \\ { P _ { x x } } & { = } & { P _ { x } + S _ { x c } \overline { { P } } _ { c c } S _ { x c } ^ { T } } \\ { P _ { x c } } & { = } & { S _ { x c } \overline { { P } } _ { c c } } \\ { \hat { \mathbf { x } } } & { = } & { P _ { x } \mathbf { N } _ { x } + S _ { x c } \overline { { \mathbf { c } } } . } \end{array}
$$

The a priori covariance of the state and consider parameters, $\overline { { P } } _ { x c }$ , generally is unknown and assumed to be the null matrix. For the case where $\overline { { P } } _ { x c } = 0$ , Eq. (6.3.31) reduces to

$$
\begin{array} { r c l } { { M _ { x x } } } & { { = } } & { { H _ { x } ^ { T } R ^ { - 1 } H _ { x } + \overline { { { P } } } _ { x } ^ { - 1 } \equiv P _ { x } ^ { - 1 } } } \\ { { M _ { x c } } } & { { = } } & { { H _ { x } ^ { T } R ^ { - 1 } H _ { c } . } } \end{array}
$$

Hence,

$$
S _ { x c } = - M _ { x x } ^ { - 1 } M _ { x c }
$$

reduces to

$$
S _ { x c } = - P H _ { x } ^ { T } R ^ { - 1 } H _ { c } .
$$

The computational algorithm for the batch consider filte r is

$$
G i \nu e n \colon \overline { { \mathbf { x } } } , \overline { { \mathbf { c } } } , \overline { { P } } _ { x } , \overline { { P } } _ { x c } , \overline { { P } } _ { c c } , R _ { i } , H _ { x _ { i } } , H _ { c _ { i } } \mathrm { a n d } \mathbf { y } _ { i } , i = 1 \cdots l
$$

$\overline { { M } } _ { x x } , \overline { { M } } _ { x c }$ , and $\overline { { M } } _ { c c }$ are given by Eqs. (6.3.22), (6.3.23), and (6.3.25), respectively.

Compute:

$$
\begin{array} { l c l } { { M _ { x x } } } & { { = } } & { { \displaystyle { H _ { x } ^ { T } R ^ { - 1 } H _ { x } + \overline { { { M } } } _ { x x } } } } \\ { { } } & { { = } } & { { \displaystyle \sum _ { i = 1 } ^ { l } H _ { x _ { i } } ^ { T } R _ { i } ^ { - 1 } H _ { x _ { i } } + \overline { { { M } } } _ { x x } = P _ { x } ^ { - 1 } } } \end{array}
$$

$$
\begin{array} { r l } { M _ { \mathrm { e x } } } & { = \phantom { - } M _ { \mathrm { e } } N ^ { - 1 } M _ { \mathrm { e } } + \overline { { M } } _ { \mathrm { e x } } } \\ & { = \phantom { - } \frac { 1 } { \mathrm { e } ^ { - \mathrm { i } \epsilon _ { \mathrm { x } } } } B _ { \mathrm { e } } ^ { 2 } \mu _ { \mathrm { x } } ^ { - 1 } H _ { \mathrm { e } } + \overline { { M } } _ { \mathrm { e x } } } \\ { M _ { \mathrm { e x } } } & { = \phantom { - } M _ { \mathrm { e x } } ^ { + 1 } } \\ { M _ { \mathrm { e x } } } & { = \phantom { - } \frac { \sum _ { m } ^ { - 1 } R _ { \mathrm { e } } ^ { 2 } R _ { \mathrm { e } } ^ { - 1 } R _ { \mathrm { e } } } { \rho _ { \mathrm { x } } ^ { - 1 } } + \overline { { M } } _ { \mathrm { e x } } } \\ { \overline { { P } } _ { \mathrm { x } } } & { = \phantom { - } M _ { \mathrm { e x } } ^ { + 1 } } \\ { \overline { { S } } _ { \mathrm { e x } } } & { = \phantom { - } \frac { \sum _ { m } ^ { - 1 } M _ { \mathrm { e x } } ^ { + 1 } } { \rho _ { \mathrm { x } } ^ { - 1 } } } \\ { \mathbf { N } _ { \mathrm { s } } } & { = \phantom { - } \frac { \sum _ { m } ^ { - 1 } R _ { \mathrm { e x } } ^ { 2 } } { \rho _ { \mathrm { x } } ^ { - 1 } } } \\ { \mathbf { \tilde { S } } _ { \mathrm { e x } } } & { = \phantom { - } M _ { \mathrm { e x } } ^ { - 1 } } \\ { \mathbf { \tilde { S } } _ { \mathrm { e x } } } & { = \phantom { - } M _ { \mathrm { e x } } ^ { - 1 } } \\ { \mathbf { \tilde { S } } _ { \mathrm { e x } } } & { = \phantom { - } M _ { \mathrm { e x } } ^ { - 1 } M _ { \mathrm { e x } } ^ { - 1 } \mathbf { \tilde { S } } _ { \mathrm { e x } } + \overline { { P } } _ { \mathrm { e x } } ^ { - 1 } } \\ { \mathbf { \tilde { S } } _ { \mathrm { e x } } } & { = \phantom { - } M _ { \mathrm { e x } } ^ { - 1 } } \\ { \rho _ { \mathrm { e x } } } &  = \mathbf { \tilde { S } } _  \mathrm  e x  \end{array}
$$

Equation (6.3.66) may also be written as

$$
P _ { x x } = P _ { x } + P _ { x c } \overline { { P } } _ { c c } ^ { - 1 } P _ { x c } ^ { T } .
$$

The complete consider covariance matrix may be written as

$$
\mathbf { P _ { c } } = E \left\{ \left[ \begin{array} { l } { \hat { \mathbf { x } } _ { c } - \mathbf { x } } \\ { \overline { { \mathbf { c } } } - \mathbf { c } } \end{array} \right] \left[ ( \hat { \mathbf { x } } _ { c } - \mathbf { x } ) ^ { T } \mathbf { \Psi } ( \overline { { \mathbf { c } } } - \mathbf { c } ) ^ { T } \right] \right\} = \left[ \begin{array} { l l } { P _ { x x } } & { P _ { x c } } \\ { P _ { c x } } & { \overline { { P } } _ { c c } } \end{array} \right]
$$

where $P _ { x x }$ is the consider covariance associated with the state vector of estimated parameters, $\mathbf { x }$ .

Note also that the expression for $\hat { \mathbf { x } } _ { c }$ can be written

$$
\begin{array} { r c l } { \hat { \mathbf { x } } _ { c } } & { = } & { P _ { x } \mathbf { N } _ { x } - P _ { x } M _ { x c } \mathbf { \overline { { c } } } } \\ { \hat { \mathbf { x } } _ { c } } & { = } & { \hat { \mathbf { x } } - P _ { x } M _ { x c } \mathbf { \overline { { c } } } } \end{array}
$$

or, from Eq. (6.3.53)

$$
\hat { \mathbf { x } } _ { c } = \hat { \mathbf { x } } - P _ { x } H _ { x } ^ { T } R ^ { - 1 } H _ { c } \overline { { \mathbf { c } } }
$$

where $\hat { \bf x }$ and $P _ { x }$ are the values of those parameters obtained from a batch processor, which assumes there are no errors in the consider parameters (i.e., $\mathbf { C ^ { * } } = \mathbf { C }$ and $P _ { x c }$ , $\overline { { P } } _ { c c }$ , $\mathbf { c }$ , and c are all zero).

# 6.4 THE SENSITIVITY AND PERTURBATION MATRICES

Several other matrices are often associated with the concept of consider analysis. The sensitivity matrix is defined to be

$$
S _ { x c } = \frac { \partial \hat { \mathbf { x } } _ { c } } { \partial \hat { \mathbf { c } } }
$$

which from Eq. (6.3.32) is

$$
S _ { x c } = - M _ { x x } ^ { - 1 } M _ { x c } .
$$

From Eq. (6.3.52)

$$
S _ { x c } = - P M _ { x c } ,
$$

and using Eq. (6.3.53) $S _ { x c }$ becomes

$$
S _ { x c } = - P H _ { x } ^ { T } R ^ { - 1 } H _ { c } .
$$

Hence, Eq. (6.3.71) may be written as

$$
\hat { \mathbf { x } } _ { c } = \hat { \mathbf { x } } + S _ { x c } \overline { { \mathbf { c } } } .
$$

Recall from Eq. (6.3.66) that the consider covariance can be written in terms of the sensitivity matrix as

$$
P _ { x x } = P _ { x } + S _ { x c } \overline { { P } } _ { c c } S _ { x c } ^ { T } .
$$

Also, using Eq. (6.3.67) the covariance, $P _ { x c }$ , can be written as

$$
P _ { x c } = S _ { x c } \overline { { P } } _ { c c } .
$$

The sensitivity matrix describes how $\hat { \mathbf { x } } _ { c }$ varies with respect to the consider parameters, c. Another commonly used matrix is the perturbation matrix defined by

$$
\Gamma = S _ { x c } \cdot \left[ \mathrm { d i a g o n a l } \left( \sigma _ { c } \right) \right]
$$

where the elements of the diagonal matrix are the standard deviations of the consider parameters. Each element, $\Gamma _ { i j }$ , gives the error in the estimate of $\mathbf { x } _ { i }$ due to a one-sigma error in the consider parameter $c _ { j }$ .

Additional discussion of consider covariance analysis can be found in Bierman (1977).

# 6.4.1 EXAMPLE APPLICATION OF A SENSITIVITY AND PERTURBATION MATRIX

Assume we have a state vector comprised of coordinates $x$ and $y$ and a parameter $\alpha$ , and consider parameters $\gamma$ and $\delta$ ,

$$
\mathbf { X } = { \left[ \begin{array} { l } { x } \\ { y } \\ { \alpha } \end{array} \right] } , \quad \mathbf { c } = { \left[ \begin{array} { l } { \gamma } \\ { \delta } \end{array} \right] } .
$$

The perturbation matrix is defined by

$$
\Gamma \equiv S _ { x c } \cdot [ \mathrm { d i a g } \sigma _ { c } ] = \left[ \begin{array} { l l } { \frac { \partial \hat { x } } { \partial \gamma } } & { \frac { \partial \hat { x } } { \partial \delta } } \\ { \frac { \partial \hat { y } } { \partial \gamma } } & { \frac { \partial \hat { y } } { \partial \delta } } \\ { \frac { \partial \hat { \alpha } } { \partial \gamma } } & { \frac { \partial \hat { \alpha } } { \partial \delta } } \end{array} \right] \left[ \begin{array} { l l } { \sigma _ { \gamma } } & { 0 } \\ { 0 } & { \sigma _ { \delta } } \end{array} \right]
$$

or

$$
\Gamma = \left[ \begin{array} { l l } { \displaystyle \frac { \partial \hat { x } } { \partial \gamma } \sigma _ { \gamma } } & { \displaystyle \frac { \partial \hat { x } } { \partial \delta } \sigma _ { \delta } } \\ { \displaystyle \frac { \partial \hat { y } } { \partial \gamma } \sigma _ { \gamma } } & { \displaystyle \frac { \partial \hat { y } } { \partial \delta } \sigma _ { \delta } } \\ { \displaystyle \frac { \partial \hat { \alpha } } { \partial \gamma } \sigma _ { \gamma } } & { \displaystyle \frac { \partial \hat { \alpha } } { \partial \delta } \sigma _ { \delta } } \end{array} \right] .
$$

Hence, the errors in the state estimate due to one-sigma errors in the consider parameters are given by

$$
\begin{array} { r c l } { { \Delta \hat { x } } } & { { = } } & { { \displaystyle \frac { \partial \hat { x } } { \partial \gamma } \sigma _ { \gamma } + \frac { \partial \hat { x } } { \partial \delta } \sigma _ { \delta } } } \\ { { \Delta \hat { y } } } & { { = } } & { { \displaystyle \frac { \partial \hat { y } } { \partial \gamma } \sigma _ { \gamma } + \frac { \partial \hat { y } } { \partial \delta } \sigma _ { \delta } } } \\ { { \Delta \hat { \alpha } } } & { { = } } & { { \displaystyle \frac { \partial \hat { \alpha } } { \partial \gamma } \sigma _ { \gamma } + \frac { \partial \hat { \alpha } } { \partial \delta } \sigma _ { \delta } . } } \end{array}
$$

Note that the information in $\Gamma$ is meaningful only if $\overline { { P } } _ { c c }$ (the covariance matrix of the errors in the consider parameters) is diagonal.

We may now form the consider covariance matrix. For simplicity, assume that

$\overline { { P } } _ { c c }$ is diagonal. Using Eq. (6.4.6) we may write $P _ { x x }$ in terms of $\Gamma$

$$
P _ { x x } = P _ { x } + S _ { x c } \overline { { P } } _ { c c } S _ { x c } ^ { T } = P _ { x } + \Gamma \Gamma ^ { T } .
$$

The contribution of the consider parameters is given by

$$
\begin{array} { r c l } { { S _ { x c } \overline { { { P } } } _ { c c } \ S _ { x c } ^ { T } } } & { { = } } & { { P _ { x c } S _ { x c } ^ { T } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { = } } & { { \left[ \begin{array} { l l } { { \displaystyle \frac { \partial \hat { x } } { \partial \gamma } \sigma _ { \gamma } ^ { 2 } } } & { { \displaystyle \frac { \partial \hat { x } } { \partial \delta } \sigma _ { \delta } ^ { 2 } } } \\ { { \displaystyle \frac { \partial \hat { y } } { \partial \gamma } \sigma _ { \gamma } ^ { 2 } } } & { { \displaystyle \frac { \partial \hat { y } } { \partial \delta } \sigma _ { \delta } ^ { 2 } } } \\ { { \displaystyle \frac { \partial \hat { \alpha } } { \partial \gamma } \sigma _ { \gamma } ^ { 2 } } } & { { \displaystyle \frac { \partial \hat { \alpha } } { \partial \delta } \sigma _ { \delta } ^ { 2 } } } \end{array} \right] \left[ \begin{array} { l l l } { { \displaystyle \frac { \partial \hat { x } } { \partial \gamma } } } & { { \displaystyle \frac { \partial \hat { y } } { \partial \gamma } } } & { { \displaystyle \frac { \partial \hat { \alpha } } { \partial \gamma } } } \\ { { \displaystyle \frac { \partial \hat { x } } { \partial \delta } } } & { { \displaystyle \frac { \partial \hat { y } } { \partial \delta } } } & { { \displaystyle \frac { \partial \hat { \alpha } } { \partial \delta } } } \end{array} \right] . } } \end{array}
$$

The diagonal terms of this matrix are

$$
= \left[ \begin{array} { c } { \left( \frac { \partial \hat { x } } { \partial \gamma } \right) ^ { 2 } \sigma _ { \gamma } ^ { 2 } + \left( \frac { \partial \hat { x } } { \partial \delta } \right) ^ { 2 } \sigma _ { \delta } ^ { 2 } } \\ { \left( \frac { \partial \hat { y } } { \partial \gamma } \right) ^ { 2 } \sigma _ { \gamma } ^ { 2 } + \left( \frac { \partial \hat { y } } { \partial \delta } \right) ^ { 2 } \sigma _ { \delta } ^ { 2 } } \\ { \left( \frac { \partial \hat { x } } { \partial \gamma } \right) ^ { 2 } \sigma _ { \gamma } ^ { 2 } + \left( \frac { \partial \hat { \alpha } } { \partial \delta } \right) ^ { 2 } \sigma _ { \gamma } ^ { 2 } + \left( \frac { \partial \hat { \alpha } } { \partial \delta } \right) ^ { 2 } \sigma _ { \delta } ^ { 2 } } \end{array} \right]
$$

or in simplified notation, the upper triangular portion of this symmetric matrix is given by

$$
S _ { x c } \overline { { { P } } } _ { c c } S _ { x c } ^ { T } = \left[ \begin{array} { c c c } { { \sigma _ { \hat { x } } ^ { 2 } } } & { { \sigma _ { \hat { x } } \sigma _ { \hat { y } } \rho _ { x y } } } & { { \sigma _ { \hat { x } } \sigma _ { \hat { \alpha } } \rho _ { x \alpha } } } \\ { { } } & { { \sigma _ { \hat { y } } ^ { 2 } } } & { { \sigma _ { \hat { y } } \sigma _ { \hat { \alpha } } \rho _ { y \alpha } } } \\ { { } } & { { } } & { { \sigma _ { \hat { \alpha } } ^ { 2 } } } \end{array} \right] _ { \mathrm { c o n s i d e r } } .
$$

For example, the total consider variance for the state variable, $x$ , is given by

$$
\begin{array} { r c l } { { \sigma _ { \hat { x } } ^ { 2 } } } & { { = } } & { { [ \sigma _ { \hat { x } } ^ { 2 } ] _ { \mathrm { d a t a  n o i s e } } + \left( \displaystyle \frac { \partial \hat { x } } { \partial \gamma } \right) ^ { 2 } \sigma _ { \gamma } ^ { 2 } + \left( \displaystyle \frac { \partial \hat { x } } { \partial \delta } \right) ^ { 2 } \sigma _ { \delta } ^ { 2 } } } \\ { { } } & { { = } } & { { [ \sigma _ { \hat { x } } ^ { 2 } ] _ { \mathrm { d a t a n n o i s e } } + [ \sigma _ { \hat { x } } ^ { 2 } ] _ { \mathrm { c o n s i d e r } } . } } \end{array}
$$

Comments:

1. If $\overline { { P } } _ { c c }$ is diagonal, then the diagonal elements of $P _ { x x }$ consist of the variance due to data noise plus the sum of the squares of the perturbations due to each consider parameter.

2. Off diagonal terms of the consider portion of $P _ { x x }$ contain correlations between errors in the estimated parameters caused by the consider parameters.

3. If di $\overline { { P } } _ { c c }$ is a full matrix, nal terms become $S _ { x c } \overline { { P } } _ { c c } S _ { x c } ^ { T }$ becomes much more complex, and thef the covariances (correlations) between consider parameters.

For example, consider the case where $\overline { { P } } _ { c c }$ is a full matrix and $\mathbf { X } = [ x y ] ^ { T }$ and ${ \bf c } = [ c _ { 1 } c _ { 2 } ] ^ { T }$ are $2 \times 1$ vectors. Then

$$
\begin{array} { r } { S _ { x c } \overline { { P } } _ { c c } S _ { x c } ^ { T } = \left[ \begin{array} { c c } { \displaystyle \frac { \partial \hat { x } } { \partial c _ { 1 } } } & { \displaystyle \frac { \partial \hat { x } } { \partial c _ { 2 } } } \\ { \displaystyle \frac { \partial \hat { y } } { \partial c _ { 1 } } } & { \displaystyle \frac { \partial \hat { y } } { \partial c _ { 2 } } } \end{array} \right] \left[ \begin{array} { c c } { \boldsymbol { \sigma } _ { c _ { 1 } } ^ { 2 } } & { \displaystyle \mu _ { 1 2 } } \\ { \displaystyle \mu _ { 1 2 } } & { \boldsymbol { \sigma } _ { c _ { 2 } } ^ { 2 } } \end{array} \right] S _ { x c } ^ { T } . } \end{array}
$$

If this is expanded, the 1,1 element becomes

$$
( P _ { c } ) _ { 1 1 } = \left( \frac { \partial \hat { x } } { \partial c _ { 1 } } \right) ^ { 2 } \sigma _ { c _ { 1 } } ^ { 2 } + 2 \frac { \partial \hat { x } } { \partial c _ { 1 } } \frac { \partial \hat { x } } { \partial c _ { 2 } } \mu _ { 1 2 } + \left( \frac { \partial \hat { x } } { \partial c _ { 2 } } \right) ^ { 2 } \sigma _ { c _ { 2 } } ^ { 2 } .
$$

Depending on the sign of the components of the second term on the right-hand side, the consider uncertainty of $x$ could be greater or less than that for the case where $\overline { { P } } _ { c c }$ is diagonal. In general, inclusion of the correlations between the consider parameters (e.g., $\mu _ { 1 2 }$ ) results in a reduction in the consider variances.

# 6.5 INCLUSION OF TIME-DEPENDENT EFFECTS

In this section we will discuss consider covariance analysis under the assumption that the state vector is time dependent. However, in this chapter we will only “consider” the effect on the state vector of errors in constant measurement or model parameters.

The dynamical equations associated with the consider covariance model can be derived as follows. The differential equations for state propagation are given by (see Chapter 4):

$$
\dot { \mathbf { X } } = F ( { \mathbf { X } } , { \mathbf { C } } , t ) .
$$

Expanding Eq. (6.5.1) in a Taylor series to first order about a nominal trajectory yields

$$
{ \dot { \bf X } } = F ( { \bf X } ^ { * } , { \bf C } ^ { * } , t ) + \left[ \frac { \partial F } { \partial { \bf X } } \right] ^ { * } ( { \bf X } - { \bf X } ^ { * } ) + \left[ \frac { \partial F } { \partial { \bf C } } \right] ^ { * } ( { \bf C } - { \bf C } ^ { * } ) + . . .
$$

Define

$$
{ \dot { \mathbf { x } } } \equiv { \dot { \mathbf { X } } } - F ( \mathbf { X } ^ { * } , \mathbf { C } ^ { * } , t ) = \left[ { \frac { \partial F } { \partial \mathbf { X } } } \right] ^ { * } \left( \mathbf { X } - \mathbf { X } ^ { * } \right) + \left[ { \frac { \partial F } { \partial \mathbf { C } } } \right] ^ { * } \left( \mathbf { C } - \mathbf { C } ^ { * } \right) .
$$

This may be written as

$$
{ \dot { \mathbf { x } } } = A ( t ) \mathbf { x } ( t ) + B ( t ) \mathbf { c }
$$

where

$$
\begin{array} { r c l } { \mathbf { x } ( t ) } & { = } & { \mathbf { X } ( t ) - \mathbf { X } ^ { * } ( t ) } \\ { \mathbf { c } } & { = } & { \mathbf { C } - \mathbf { C } ^ { * } } \\ { A ( t ) } & { = } & { \left[ \cfrac { \partial F } { \partial \mathbf { X } } \right] ^ { * } } \\ { B ( t ) } & { = } & { \left[ \cfrac { \partial F } { \partial \mathbf { C } } \right] ^ { * } . } \end{array}
$$

For the conventional filter model $\mathbf { c } = 0$ , and the solution for Eq. (6.5.4) is

$$
\mathbf { x } ( t ) = \Phi ( t , t _ { k } ) \mathbf { x } ( t _ { k } ) .
$$

The general solution of Eq. (6.5.4) can be obtained by the method of variation of parameters to yield

$$
\mathbf { x } ( t ) = \Phi ( t , t _ { k } ) \mathbf { x } _ { k } + \theta ( t , t _ { k } ) \mathbf { c } .
$$

In Eq. (6.5.8), the $n \times n$ mapping matrix, $\Phi ( t , t _ { k } )$ , and the $n \times q$ mapping matrix, $\theta ( t , t _ { k } )$ , are defined as

$$
\begin{array} { l } { { \displaystyle \Phi ( t , t _ { k } ) = \frac { \partial { \bf X } ( t ) } { \partial { \bf X } ( t _ { k } ) } } } \\ { { \displaystyle \theta ( t , t _ { k } ) = \frac { \partial { \bf X } ( t ) } { \partial { \bf C } ( t _ { k } ) } . } } \end{array}
$$

The corresponding differential equations for $\Phi ( t , t _ { k } )$ and $\theta ( t , t _ { k } )$ are obtained by differentiating Eq. (6.5.1) and recognizing that differentiation with respect to time and $\mathbf { X } ( t _ { k } )$ and $\mathbf { C }$ are interchangeable for functions whose derivatives are continuous. From Eq. (6.5.1)

$$
\frac { \partial \dot { \mathbf X } } { \partial \mathbf X ( t _ { k } ) } = \frac { \partial F } { \partial \mathbf X ( t _ { k } ) } ,
$$

which may be written as

$$
\frac { d } { d t } \frac { \partial \mathbf { X } ( t ) } { \partial \mathbf { X } ( t _ { k } ) } = \left[ \frac { \partial F } { \partial \mathbf { X } ( t ) } \right] ^ { * } \frac { \partial \mathbf { X } ( t ) } { \partial \mathbf { X } ( t _ { k } ) }
$$

or

$$
{ \dot { \Phi } } ( t , t _ { k } ) = A ( t ) \Phi ( t , t _ { k } )
$$

with initial conditions $\Phi ( t _ { 0 } , t _ { 0 } ) = I$ . Likewise,

$$
\frac { d } { d t } \frac { \partial \mathbf { X } ( t ) } { \partial \mathbf { C } ( t _ { k } ) } = \left[ \frac { \partial F } { \partial \mathbf { X } ( t ) } \right] ^ { * } \frac { \partial \mathbf { X } ( t ) } { \partial \mathbf { C } ( t _ { k } ) } + \left[ \frac { \partial F } { \partial \mathbf { C } } \right] ^ { * }
$$

becomes

$$
\dot { \theta } ( t , t _ { k } ) = A ( t ) \theta ( t , t _ { k } ) + B ( t )
$$

with initial conditions $\theta ( t _ { 0 } , t _ { 0 } ) = 0$ . Note that if $C$ is partitioned as

$$
\mathbf { C } ^ { T } = [ \mathbf { C } _ { d } ^ { T } : \mathbf { C } _ { m } ^ { T } ]
$$

where $\mathbf { C } _ { d }$ are dynamic model parameters and $\mathbf { C } _ { m }$ are measurement model parameters, then $\theta$ can be written as

$$
\theta = [ \theta _ { d } \colon \theta _ { m } ]
$$

where the solution for $\theta _ { m }$ will be $\theta _ { m } ( t , t _ { k } ) = 0$ , the null matrix. This follows since measurement model parameters do not appear in the dynamic equations.

The estimation errors for the conventional filter model (Eq. 6.5.7) and the consider model (Eq. 6.5.8), labeled here as Filter and Consider, are mapped according to

Filter:

$$
\tilde { \mathbf { x } } ( t ) = \hat { \mathbf { x } } ( t ) - \mathbf { x } ( t ) = \boldsymbol { \Phi } ( t , t _ { k } ) \tilde { \mathbf { x } } _ { k }
$$

where $\tilde { \mathbf { x } } _ { k } = \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k }$ and all quantities are computed assuming there are no consider parameters.

Consider:

$$
\begin{array} { r c l } { \tilde { \mathbf { x } } _ { c } ( t ) } & { = } & { \hat { \mathbf { x } } _ { c } ( t ) - \mathbf { x } ( t ) } \\ & { = } & { [ \boldsymbol { \Phi } ( t , t _ { k } ) \hat { \mathbf { x } } _ { c _ { k } } + \boldsymbol { \theta } ( t , t _ { k } ) \bar { \mathbf { c } } ] - [ \boldsymbol { \Phi } ( t , t _ { k } ) \mathbf { x } _ { k } + \boldsymbol { \theta } ( t , t _ { k } ) \mathbf { c } ] } \\ & { = } & { \boldsymbol { \Phi } ( t , t _ { k } ) ( \hat { \mathbf { x } } _ { c _ { k } } - \mathbf { x } _ { k } ) + \boldsymbol { \theta } ( t , t _ { k } ) ( \bar { \mathbf { c } } - \mathbf { c } ) ( 6 . 5 . 1 } \\ & { = } & { \boldsymbol { \Phi } ( t , t _ { k } ) \tilde { \mathbf { x } } _ { c _ { k } } + \boldsymbol { \theta } ( t , t _ { k } ) \boldsymbol { \beta } } \end{array}
$$

where $\tilde { \mathbf { x } } _ { c _ { k } } = \hat { \mathbf { x } } _ { c _ { k } } - \mathbf { x } _ { k }$ and $\beta = \bar { \mathbf { c } } - \mathbf { c }$

We have included the conventional filter results in this section to illustrate differences with the consider fil ter. Remember that the conventional filter results assume that there are no errors in the consider parameters $\mathbf { C ^ { * } } = \mathbf { C }$ ). Hence, the true value, $\mathbf { x } _ { k }$ , for the fil ter results is different from the true value for the consider results.

The respective observation models are

Filter:

$$
\mathbf { y } _ { j } = \tilde { H } _ { x _ { j } } \mathbf { x } _ { j } + \boldsymbol { \epsilon } _ { j } \quad j = 1 , \ldots , l .
$$

Consider:

$$
\begin{array} { r } { { \bf y } _ { j } = \tilde { H } _ { x _ { j } } { \bf x } _ { j } + \tilde { H } _ { c _ { j } } { \bf c } + \epsilon _ { j } \quad j = 1 , \ldots , l . } \end{array}
$$

The state vector, $\mathbf { x } _ { j }$ , is replaced by its value at the estimation epoch $t _ { k }$ , by using Eq. (6.5.7),

Filter:

$$
{ \bf y } _ { j } = \tilde { H } _ { x _ { j } } \Phi ( t _ { j } , t _ { k } ) { \bf x } _ { k } + \epsilon _ { j } .
$$

The consider expression for $\mathbf { y } _ { j }$ is obtained by recognizing that

$$
{ \bf y } _ { j } = \tilde { H } _ { x _ { j } } \Big [ \Phi ( t _ { j } , t _ { k } ) { \bf x } _ { k } + \theta ( t _ { j } , t _ { k } ) { \bf c } \Big ] + \tilde { H } _ { c _ { j } } { \bf c } + \epsilon _ { j } .
$$

This equation may be written as

$$
\begin{array} { r } { \mathbf { y } _ { j } = \left[ \tilde { H } _ { x _ { j } } \tilde { H } _ { c _ { j } } \right] \left[ \begin{array} { c c } { \Phi ( t _ { j } , t _ { k } ) } & { \theta ( t _ { j } , t _ { k } ) } \\ { 0 } & { I } \end{array} \right] \left[ \begin{array} { c } { \mathbf { x } _ { k } } \\ { \mathbf { c } } \end{array} \right] + \epsilon _ { j } } \end{array}
$$

or

$$
\begin{array} { r } { \mathbf { y } _ { j } = \left[ \tilde { H } _ { x _ { j } } \Phi ( t _ { j } , t _ { k } ) \colon \tilde { H } _ { x _ { j } } \theta ( t _ { j } , t _ { k } ) + \tilde { H } _ { c _ { j } } \right] \left[ \begin{array} { l } { \mathbf { x } _ { k } } \\ { \mathbf { c } } \end{array} \right] + \epsilon _ { j } . } \end{array}
$$

By using the definitions

$$
{ \cal H } _ { x _ { j } } \equiv \tilde { \cal H } _ { x _ { j } } \Phi ( t _ { j } , t _ { k } ) \quad j = 1 , \ldots , l
$$

$$
{ \cal H } _ { c _ { j } } \equiv \tilde { H } _ { x _ { j } } \theta ( t _ { j } , t _ { k } ) + \tilde { H } _ { c _ { j } } \quad j = 1 , \ldots , l
$$

and

$$
\mathbf { y } \equiv \left[ \begin{array} { c } { \mathbf { y } _ { 1 } } \\ { \vdots } \\ { \mathbf { y } _ { l } } \\ { \mathbf { y } _ { l } } \end{array} \right] , \qquad H _ { x } \equiv \left[ \begin{array} { c } { H _ { x _ { 1 } } } \\ { \vdots } \\ { H _ { x _ { l } } } \end{array} \right] ,
$$

$$
H _ { c } \equiv \left[ \begin{array} { c } { { H _ { c _ { 1 } } } } \\ { { \vdots } } \\ { { } } \\ { { H _ { c _ { l } } } } \end{array} \right] , \quad \epsilon \equiv \left[ \begin{array} { c } { { \epsilon _ { 1 } } } \\ { { \vdots } } \\ { { } } \\ { { \epsilon _ { l } } } \end{array} \right]
$$

the two cumulative observation models used in Section 6.3 can then be obtained,

Filter:

$$
\mathbf { y } = H _ { x } \mathbf { x } _ { k } + \epsilon
$$

Consider:

$$
{ \bf y } = H _ { x } { \bf x } _ { k } + H _ { c } { \bf c } + \epsilon
$$

where $E [ \epsilon ] = 0$ and $E [ \epsilon \epsilon ^ { T } ] = R$ . The associated error covariance matrix for the filter model at the epoch, $t _ { k }$ , is

$$
\begin{array} { r } { P _ { x k } = E \big [ ( \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ) ( \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } ) ^ { T } \big ] = \big [ H _ { x } ^ { T } R ^ { - 1 } H _ { x } + \overline { { P } } _ { k } ^ { - 1 } \big ] ^ { - 1 } . } \end{array}
$$

To simplify, notation $P _ { x x }$ is being replaced by $P _ { c }$ , $S _ { x c }$ is being replaced by $S$ , and $P _ { x }$ is being replaced by $P$ for the remainder of this chapter.

The consider covariance is given by

$$
P _ { x x _ { k } } \equiv P _ { c _ { k } } = E \bigl [ ( \hat { \mathbf { x } } _ { c _ { k } } - \mathbf { x } _ { k } ) ( \hat { \mathbf { x } } _ { c _ { k } } - \mathbf { x } _ { k } ) ^ { T } \bigr ] .
$$

From Eq. (6.4.5)

$$
\hat { \mathbf { x } } _ { c _ { k } } = \hat { \mathbf { x } } _ { k } + S _ { k } \overline { { \mathbf { c } } } .
$$

However, the true value of $\mathbf { x } _ { k }$ for the consider covariance analysis is given by

$$
\mathbf { x } _ { k } = \mathbf { x } _ { k } ^ { * } + S _ { k } \mathbf { c }
$$

where $\mathbf { x } _ { k } ^ { * }$ is the true value of $\mathbf { x } _ { k }$ for the conventional fil ter $\mathbf { C ^ { * } } = \mathbf { C }$ ) and there are no errors in the consider parameters. $S _ { k } \mathbf { c }$ is the contribution due to the true value of $\mathbf { c }$ , the error in the consider parameters. Hence, $\Delta \hat { \mathbf x } _ { c _ { k } }$ , the error in the consider estimate, $\hat { \mathbf { x } } _ { c _ { k } }$ , is given by

$$
\Delta \hat { \bf x } _ { c _ { k } } \equiv \hat { \bf x } _ { c _ { k } } - { \bf x } _ { k } = \hat { \bf x } _ { k } - { \bf x } _ { k } ^ { * } + S _ { k } ( \overline { { \bf c } } - { \bf c } ) .
$$


<!-- chunk 0007: pages 421-490 -->
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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/5d59c770ee405b0cce55d441cb60e0fb1764d3aed4410ffc1f47a6b328800199.jpg)

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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/5c02357bb2e451d1f5a5f5210bb30ade45321943e1803d352ac25cc28a5c6798.jpg)  
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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/0cbeb694c3dc85ae910af8b3092b3eb66edb6a456b6387b72633f68b053089f1.jpg)  
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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/765f19b25c07a653f025cafa72677efd1a832529240e80970f75958a804ec8b9.jpg)

Assume: $\sigma ( x _ { 0 } ) = \sigma ( g ) = \sigma ( \rho ) = 1$ , and small oscillations so that the equation of motion is linear.

(a) Define: $\Phi ( t , t _ { 0 } ) , \theta ( t , t _ { 0 } ) , H _ { x } , H _ { c } .$ .

(b) Assuming $\sqrt { g / l } \ = \ 1 0$ and observations are taken at $t = 0 , 1 , 2 ,$ , compute the data noise covariance, the sensitivity, perturbation, and consider covariance matrices. Discuss the interpretation of these matrices. Assume $x _ { 0 } = \ell = 1$ , ${ \overline { { P } } } = R = I$ , $\theta _ { 0 } = 0 . 0 1$ rad, and $\dot { \theta } _ { 0 } = 0$ .

Answer:

6. Examine the problem of estimating the position and velocity of a spacecraft in low Earth orbit from ground-based range measurements. The dynamic model is chosen as a simple “flat Earth.” Assume range measurements are taken from a single station. Derive the expression for the consider covariance matrix for the estimated and consider parameters shown.

Estimate: $X , Y , \dot { X } , \dot { Y }$ Consider: $g , X _ { s } , Y _ { s }$ Observe: $\rho$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/583a75c2b99e702d4c7e7560ce1efc90a30b2e4def3f1f9325d869497b607b3d.jpg)

7. A vehicle travels in a straight line according to the following equation:

$$
u ( t ) = u _ { 0 } + e t + f t ^ { 2 }
$$

where

$$
\begin{array} { l } { { u = \mathrm { d i s t a n c e ~ f r o m ~ o r i g i n } } } \\ { { \ } } \\ { { t = \mathrm { t i m e } } } \\ { { \ } } \\ { { e , f = \mathrm { c o n s t a n t s } . } } \end{array}
$$

A tracking station location a distance $s$ from the origin takes range measurements $\rho$ .

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/b4dd03c6564c09fc55f5c300263ae651530130412e62141f32ec99392d043e79.jpg)

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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/9fb0d5a3d37b8f90a0c64eefce47d48206ed9e22d9d6a6c4dc279bc387e67c14.jpg)

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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/a5b80b96ed91b5fe8bed30bed2c2e28fe1140dd8b28c83649d3eaf361d8f39b8.jpg)  
Density function of a continuous random variable

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/175e1c0cafea89ad97ac835c33d14bdaa7ff386ff72e31481d7e9465bbdc8d65.jpg)  
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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/9aeaf9fd4f75236e73d5880655f19b0cbe2000dc2af5d4bbd17f3ddd2ae2b3c9.jpg)

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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/557d8e1a033a8a2e86e22eef519d071d9feac012b7a5bd521af8b859fd5409a1.jpg)

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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/c2906d3f240eca4583c76a87e768195ff1fa69971b0a3b38efd5aaeff063cb64.jpg)

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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/ea1558d609fc8fd325b6c8769dcc259cb92eac3bc4a0bbeb9bab953b073fc397.jpg)

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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/6bb31af82a80d1f1f79ae535a73e90db770978979275c49137345a2b458ef7e8.jpg)

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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/7428ef121f4ab20f270a569714e2dcb86bba431369962f93411639e2aa6c00b2.jpg)

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

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/41dc79eba0db478e1c6face81a285c52b7d6f59c3f56e8d490813c4fa3778621.jpg)

If we move the second mode further out without changing the density function between the origin and the median, the median remains fix ed but the mean moves to the right.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0007_pages_0421-0490/auto/images/9033807cc62b7617250ae7adb43217c51b74b1bc0295a1aceb7d31ab5b00e328.jpg)

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


<!-- chunk 0008: pages 491-560 -->
# B.2 RANK

• The rank of a matrix is the dimension of its largest square nonsingular submatrix; that is, one whose determinant is nonzero.

• The rank of the product AB of the two matrices $\mathbf { A }$ and $\mathbf { B }$ is less than or equal to the rank of $\mathbf { A }$ and is less than or equal to the rank of $\mathbf { B }$ .

• The rank of the sum of $\textbf { A + B }$ is less than or equal to the rank of $\mathbf { A }$ plus the rank of $\mathbf { B }$ .

• If A is an $n \times n$ matrix and if $| \mathbf { A } | = 0$ , then the rank of $\mathbf { A }$ is less than $n$ .

• If the rank of $\mathbf { A }$ is less than $n$ , then all the rows of $\mathbf { A }$ are not independent; likewise, all the columns of $\mathbf { A }$ are not independent ( $\mathbf { A }$ is $n \times n$ ).

• If the rank of $\mathbf { A }$ is $m \leq n$ , then the number of linearly independent rows is $m$ ; also, the number of linearly independent columns is $m$ ( $\mathbf { A }$ is $n \times n$ ).

• If $\mathbf { A } ^ { T } \mathbf { A } \ = \ 0$ , then $\textbf { A } = \textbf { 0 }$ .

• The rank of a matrix is unaltered by multiplication by a nonsingular matrix; that is, if A, $\mathbf { B }$ , and $\mathbf { C }$ are matrices such that AB and BC exist and if A and $\mathbf { C }$ are nonsingular, then $\rho \left( \mathbf { A } \mathbf { B } \right) \ = \ \rho \left( \mathbf { B } \mathbf { C } \right) \ = \ \rho \left( \mathbf { B } \right) . \rho \left( \mathbf { B } \right) \ = \mathbf { r }$ ank of $\mathbf { B }$ .

• If the product AB of two square matrices is 0, then $\mathbf { A } = 0 , \mathbf { B } = 0$ , or A and $\mathbf { B }$ are both singular.

• If A and $\mathbf { B }$ are $n \times n$ matrices of rank $r$ and $s$ , respectively, then the rank of AB is greater than or equal to $r \ + \ s \ - \ n$ .

• The rank of $\mathbf { A A } ^ { T }$ equals the rank of ${ \bf A } ^ { T } { \bf A }$ , equals the rank of A, equals the rank of ${ \mathbf A } ^ { T }$ .

# B.3 QUADRATIC FORMS

• The rank of the quadratic form $\mathbf { Y } ^ { T } \mathbf { A Y }$ is defined as the rank of the matrix A where $\mathbf { Y }$ is a vector and $\textbf { Y } \neq 0$ .

• The quadratic form $\mathbf { Y } ^ { T } \mathbf { A Y }$ is said to be positive definit $e$ if and only if $\mathbf { Y } ^ { T } \mathbf { A Y } > 0$ for all vectors $\mathbf { Y }$ where $\textbf { Y } \neq 0$ .

• A quadratic form $\mathbf { Y } ^ { T } \mathbf { A Y }$ is said to be positive semidefinite if and only if $\mathbf { Y } ^ { T } \mathbf { A Y } \geq 0$ for all $\mathbf { Y }$ , and $\mathbf { Y } ^ { T } \mathbf { A Y } = \mathbf { \zeta } 0$ for some vector $\textbf { Y } \neq 0$ .

• A quadratic form $\mathbf { Y } ^ { T } \mathbf { A Y }$ that may be either positive definite or positive semidefini te is called nonnegative definite .

• The matrix A of a quadratic form $\mathbf { Y } ^ { T } \mathbf { A Y }$ is said to be positive definite (semidefinite) when the quadratic form is positive defini te (semidefinite ).

• If $\mathbf { P }$ is a nonsingular matrix and if $\mathbf { A }$ is positive definite (semidefinite), then $\mathbf { P } ^ { T } \mathbf { A P }$ is positive definite (semidefinit e).

• A necessary and sufficie nt condition for the symmetric matrix A to be positive definite is that there exist a nonsingular matrix $\mathbf { P }$ such that $\mathbf { A } = \bar { \mathbf { P } } \mathbf { P } ^ { T }$ .

• A necessary and sufficient condition that the matrix A be positive definite, where

$$
\textbf { A } = \begin{array} { l } { \left[ \begin{array} { l } { a _ { 1 1 } \ a _ { 1 2 } \dots a _ { 1 n } } \\ { a _ { 2 1 } \ a _ { 2 2 } \dots a _ { 2 n } } \\ { \vdots \quad \vdots \quad \ddots \quad \vdots } \\ { a _ { n 1 } a _ { n 2 } \dots a _ { n n } } \end{array} \right] } \end{array}
$$

is that the following inequalities hold:

$$
\begin{array} { r } { a _ { 1 1 } > 0 , \left| \begin{array} { l } { a _ { 1 1 } a _ { 1 2 } } \\ { a _ { 2 1 } a _ { 2 2 } } \\ { a _ { 2 1 } a _ { 2 2 } } \end{array} \right| > 0 , \ldots \left| \begin{array} { l } { a _ { 1 1 } a _ { 1 2 } \ldots a _ { 1 n } } \\ { a _ { 2 1 } a _ { 2 2 } \ldots a _ { 2 n } } \\ { \vdots \quad \vdots \quad \vdots \quad \ldots \quad \vdots } \\ { a _ { n 1 } a _ { n 2 } \ldots a _ { n n } } \end{array} \right| > 0 . } \end{array}
$$

• If $\mathbf { A }$ is an $m \times n$ matrix of rank $n < m$ , then ${ \bf A } ^ { T } { \bf A }$ is positive definite and $\mathbf { A A } ^ { T }$ is positive semidefinite.

• If $\mathbf { A }$ is an $m \times n$ matrix of rank $k < n$ and $k < m$ , then ${ \bf A } ^ { T } { \bf A }$ and $\mathbf { A A } ^ { T }$ are each positive semidefinite.

• A matrix that may be either positive definite or positive semidefinite is said to be nonnegative defini te.

• If $\mathbf { A }$ and $\mathbf { B }$ are symmetric conformable matrices, A is said to be greater than $\mathbf { B }$ if $\mathbf { A } - \mathbf { B }$ is nonnegative definite.

# B.4 DETERMINANTS

• For each square matrix A, there is a uniquely defined scalar called the determinant of $\mathbf { A }$ and denoted by $| \mathbf { A } |$ .

• The determinant of a diagonal matrix is equal to the product of the diagonal elements.

• If A and $\mathbf { B }$ are $n \times n$ matrices, then $\mathbf { \left| A B \right| } = \mathbf { \left| B A \right| } = \mathbf { \left| A \right| } \mathbf { \left| B \right| }$ .

• If A is singular if and only if $| \mathbf { A } | = 0$ .

• If $\mathbf { C }$ is an $n \ \times \ n$ matrix such that ${ \bf C } ^ { T } { \bf C } \ = \ { \bf I }$ , then $\mathbf { C }$ is said to be an orthogonal matrix, and ${ \bf C } ^ { T } = { \bf C } ^ { - 1 }$ .

• If $\mathbf { C }$ is an orthogonal matrix, then $| { \bf C } | = + 1$ or $| { \bf C } | = - 1$

• If $\mathbf { C }$ is an orthogonal matrix, then $| \mathbf { C } ^ { T } \mathbf { A C } | = | \mathbf { A } |$ .

• The determinant of a positive definit e matrix is positive.

• The determinant of a triangular matrix is equal to the product of the diagonal elements.

• The determinant of a matrix is equal to the product of its eigenvalues.

• $| \mathbf { A } | = | \mathbf { A } ^ { T } |$

• $| \mathbf { A } ^ { - 1 } | = 1 / \left| \mathbf { A } \right|$ , if $| \mathbf { A } | \neq 0$ .

• If $\mathbf { A }$ is a square matrix such that

$$
\mathbf { A } = { \left[ \begin{array} { l } { \mathbf { A } _ { 1 1 } \mathbf { A } _ { 1 2 } } \\ { \mathbf { A } _ { 2 1 } \mathbf { A } _ { 2 2 } } \end{array} \right] }
$$

where $\mathbf { A } _ { 1 1 }$ and $\mathbf { A } _ { 2 2 }$ are square matrices, and if $\mathbf { A } _ { 1 2 } { \mathbf { \Omega } } = { \mathbf { \Omega } } 0$ or $\mathbf { A } _ { 2 1 } ~ = ~ 0$ , then $| \mathbf { A } | = | \mathbf { A } _ { 1 1 } | | \mathbf { A } _ { 2 2 } |$ .

• If ${ \bf A } _ { 1 }$ and ${ \bf A } _ { 2 }$ are symmetric and ${ \bf A } _ { 2 }$ is positive defini te and if ${ \bf A } _ { 1 } ~ - ~ { \bf A } _ { 2 }$ is positive semidefinite (or positive definite), then $| \mathbf { A } _ { 1 } | \geq | \mathbf { A } _ { 2 } |$ .

# B.5 MATRIX TRACE

• The trace of a matrix A, which will be written $\operatorname { t r } \left( \mathbf { A } \right)$ , is equal to the sum of the diagonal elements of $\mathbf { A }$ ; that is,

$$
t r \left( \mathbf { A } \right) = \sum _ { i = 1 } ^ { n } a _ { i i } .
$$

• $\operatorname { t r } ( \mathbf { A } \mathbf { B } ) = \operatorname { t r } ( \mathbf { B } \mathbf { A } )$

• $\operatorname { t r } ( \mathrm { A B C } ) = \operatorname { t r } ( \mathbf { C A B } ) = \operatorname { t r } ( \mathbf { B C A } )$ ; that is, the trace of the product of matrices is invariant under any cyclic permutation of the matrices.

• Note that the trace is defined only for a square matrix.

• If $\mathbf { C }$ is an orthogonal matrix, $\operatorname { t r } \left( \mathbf { C } ^ { T } \mathbf { A C } \right) = \operatorname { t r } \left( \mathbf { A } \right)$ .

# B.6 EIGENVALUES AND EIGENVECTORS

• A characteristic root (eigenvalue) of a $p \ \times \ p$ matrix $\mathbf { A }$ is a scalar $\lambda$ such that $\mathbf { A X } = \lambda \mathbf { X }$ for some vector $\mathbf { X } \neq 0$ .

• The vector $\mathbf { X }$ is called the characteristic vector (eigenvector) of the matrix A.

• The characteristic root of a matrix A can be defined as a scalar $\lambda$ such that $| \mathbf { A } \ - \ \lambda \mathbf { I } | \ = \ 0$ .

• $| \mathbf { A } \ - \ \lambda \mathbf { I } |$ is a pth degree polynomial in $\lambda$ .

• This polynomial is called the characteristic polynomial, and its roots are the characteristic roots of the matrix A.

• The number of nonzero characteristic roots of a matrix A is equal to the rank of A.

• The characteristic roots of $\mathbf { A }$ are identical with the characteristic roots of $\mathbf { C A C } ^ { - 1 }$ . If C is an orthogonal matrix, it follows that A and $\mathbf { C A C } ^ { T }$ have identical characteristic roots; that is, ${ \bf C } ^ { T } = { \bf C } ^ { - 1 }$ .

• The characteristic roots of a symmetric matrix are real; that is, if $\mathbf { A } = \mathbf { A } ^ { T }$ , the characteristic polynomial of $| \mathbf { A } = \lambda \mathbf { I } | = 0$ has all real roots.

• The characteristic roots of a positive definit e matrix A are positive; the characteristic roots of a positive semidefinite matrix are nonnegative.

# B.7 THE DERIVATIVES OF MATRICES AND VECTORS

• Let $\mathbf { X }$ be an $n \times 1$ vector and let $Z$ be a scalar that is a function of $\mathbf { X }$ . The derivative of $Z$ with respect to the vector $\mathbf { X }$ , which will be written $\partial Z / \partial \mathbf { X }$ , will mean the $1 \times n$ row vector∗

$$
\begin{array} { r } { \mathbf { C } \equiv \left[ \frac { \partial Z } { \partial x _ { 1 } } \frac { \partial Z } { \partial x _ { 2 } } \dots \frac { \partial Z } { \partial x _ { n } } \right] . } \end{array}
$$

• If X, C, and $Z$ are as defined previously, then

$$
\partial Z / \partial \mathbf { X } = \mathbf { C } .
$$

• If A and $\mathbf { B }$ are $m \times 1$ vectors, which are a function of the $n \times 1$ vector $\mathbf { X }$ , and we define

$$
\frac { \partial ( \mathbf { A } ^ { T } \mathbf { B } ) } { \partial \mathbf { X } }
$$

to be a row vector as in Eq. (B.7.1), then

$$
\partial ( \mathbf { A } ^ { T } \mathbf { B } ) / \partial \mathbf { X } = \mathbf { B } ^ { T } \frac { \partial \mathbf { A } } { \partial \mathbf { X } } + \mathbf { A } ^ { T } \frac { \partial \mathbf { B } } { \partial \mathbf { X } }
$$

where

$$
\frac { \partial \mathbf { A } } { \partial \mathbf { X } }
$$

is an $m \times n$ matrix whose $i j$ element is

$$
\frac { \partial A _ { i } } { \partial X _ { j } }
$$

and

$$
\frac { \partial ( \mathbf { A } ^ { T } \mathbf { B } ) } { \partial \mathbf { X } }
$$

is a $1 \times n$ row vector.†

• If $\mathbf { A }$ is an $m \times 1$ vector that is a function of the $n \times 1$ vector $\mathbf { X }$ , and $W$ is an $m \times m$ symmetric matrix such that

$$
Z = \mathbf { A } ^ { T } W \mathbf { A } = \mathbf { A } ^ { T } W ^ { 1 / 2 } W ^ { 1 / 2 } \mathbf { A } .
$$

Let ${ \bf B } \equiv W ^ { 1 / 2 } { \bf A }$ , then

$$
Z = \mathbf { B } ^ { T } \mathbf { B } .
$$

From Eq. (B.7.3)

$$
\frac { \partial Z } { \partial \mathbf { X } } = 2 \mathbf { B } ^ { T } \frac { \partial \mathbf { B } } { \partial \mathbf { X } }
$$

where

$$
\frac { \partial { \bf B } } { \partial { \bf X } } = W ^ { 1 / 2 } \frac { \partial { \bf A } } { \partial { \bf X } } .
$$

• Let A be a $p \times 1$ vector, $\mathbf { B }$ be a $q \times 1$ vector, and $C$ be a $p \ \times \ q$ matrix whose $i j ^ { \mathrm { t h } }$ element equals $c _ { i j }$ . Let

$$
Z = \mathbf { A } ^ { T } C \mathbf { B } \ = \ \sum _ { m = 1 } ^ { q } \sum _ { n = 1 } ^ { p } a _ { n } c _ { n m } b _ { m } .
$$

Then $\partial Z / \partial C = \mathbf { A B } ^ { T }$ .

Proof: $\partial Z / \partial C$ will be a $p \ \times \ q$ matrix whose $i j ^ { \mathrm { t h } }$ element is $\partial Z / \partial c _ { i j }$

Assuming that $C$ is not symmetric and that the elements of $C$ are independent,

$$
\frac { \partial Z } { \partial c _ { i j } } \ : = \ : \frac { \partial \ : \left( \displaystyle \sum _ { m = 1 } ^ { q } \ : \sum _ { n = 1 } ^ { p } a _ { n } c _ { n m } b _ { m } \right) } { \partial c _ { i j } } \ : = \ : a _ { i } \ : b _ { j } .
$$

Thus the $i j ^ { \mathrm { t h } }$ element of $\partial Z / \partial C$ is $a _ { i } b _ { j }$ . Therefore, it follows that

$$
\frac { \partial Z } { \partial C } = \mathbf { A B } ^ { T } .
$$

• The derivative of a matrix product with respect to a scalar is given by

$$
{ \frac { d } { d t } } \left\{ \mathbf { A } ( t ) \mathbf { B } ( t ) \right\} = { \frac { d \mathbf { A } ( t ) } { d t } } \mathbf { B } ( t ) + \mathbf { A } ( t ) { \frac { d \mathbf { B } ( t ) } { d t } } .
$$

See Graybill (1961) for additional discussion of the derivatives of matrices and vectors.

# B.8 MAXIMA AND MINIMA

• If $\begin{array} { r c l } { y } & { = } & { f \left( x _ { 1 } , x _ { 2 } , . . . , x _ { n } \right) } \end{array}$ is a function of $n$ variables and if all partial derivatives $\partial y / \partial x _ { i }$ are continuous, then $y$ attains its maxima and minima only at the points where

$$
{ \frac { \partial y } { \partial x _ { 1 } } } = { \frac { \partial y } { \partial x _ { 2 } } } = \ldots = { \frac { \partial y } { \partial x _ { n } } } = 0 .
$$

• If $f \left( x _ { 1 } , x _ { 2 } , . . . , x _ { n } \right)$ is such that all the firs t and second partial derivatives are continuous, then at the point where

$$
{ \frac { \partial f } { \partial { x } _ { 1 } } } = { \frac { \partial f } { \partial { x } _ { 2 } } } = \ldots = { \frac { \partial f } { \partial { x } _ { n } } } = 0
$$

the function has

– a minimum, if the matrix $\mathbf { K }$ , where the $i j$ th element of $\mathbf { K }$ is $\partial ^ { 2 } f / \partial x _ { i } \partial x _ { j }$ , is positive definite.   
– a maximum, if the matrix $- \mathbf { K }$ is positive definit e.

In these two theorems on maxima and minima, remember that the $x _ { i }$ are independent variables.

• If the $x _ { i }$ are not independent, that is, there are constraints relating them, we use the method of Lagrange multipliers. Suppose that we have a function $f ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ we wish to maximize (or minimize) subject to the constraint that $h ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } ) = 0$ . The equation $h = 0$ describes a surface in space and the problem is one of maximizing $f ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ as $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ vary on the curve of intersection of the two surfaces. At a maximum point the derivative of $f$ must be zero along the intersection curve; that is, the directional derivative along the tangent must be zero. The directional derivative is the component of the vector $\nabla f$ along the tangent. Hence, $\nabla f$ must lie in a plane normal to the intersection curve at this point. This plane must also contain $\nabla h$ ; that is, $\nabla f$ and $\nabla h$ are coplanar at this point. Hence, there must exist a scalar $\lambda$ such that

$$
\nabla f + \lambda \nabla h = 0
$$

at the maximum point. If we define

$$
F \equiv f + \lambda h
$$

then Eq. (B.8.3) is equivalent to $\nabla F = 0$ . Hence,

$$
{ \frac { \partial F } { \partial x _ { 1 } } } = { \frac { \partial F } { \partial x _ { 2 } } } = \cdots = { \frac { \partial F } { \partial x _ { n } } } = 0 .
$$

These $n$ equations together with $h = 0$ provide us with $n + 1$ equations and $n + 1$ unknowns $( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } , \lambda )$ . We have assumed that all first partial derivatives are continuous and that $\partial h / \partial x _ { i } \neq 0$ for all $i$ at the point.

• If there are additional constraints we introduce additional Lagrange multipliers in Eq. (B.8.3); for example,

$$
\nabla f + \lambda _ { 1 } \nabla h _ { 1 } + \lambda _ { 2 } \nabla h _ { 2 } + \cdot \cdot \cdot \lambda _ { k } \nabla h _ { k } = 0 .
$$

# B.9 USEFUL MATRIX INVERSION THEOREMS

Theorem 1: Let $\mathbf { A }$ and $\mathbf { B }$ be $n \ \times \ n$ positive definite (PD) matrices. If $\mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 }$ is PD, then $\mathbf { A } + \mathbf { B }$ is PD and

$$
( \mathbf { A } + \mathbf { B } ) ^ { - 1 } = \mathbf { B } ^ { - 1 } ( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } ) ^ { - 1 } \mathbf { A } ^ { - 1 }
$$

$$
\mathbf { \Sigma } = \mathbf { A } ^ { - 1 } \left( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } \right) ^ { - 1 } \mathbf { B } ^ { - 1 } .
$$

Proof: From the identity

$$
( \mathbf { A } + \mathbf { B } ) ^ { - 1 } \ : = \ : [ \mathbf { A } \left( \mathbf { A } ^ { - 1 } \ : + \ : \mathbf { B } ^ { - 1 } \right) \mathbf { B } ] ^ { - 1 } \ : = \ : \mathbf { B } ^ { - 1 } ( \mathbf { A } ^ { - 1 } \ : + \ : \mathbf { B } ^ { - 1 } ) ^ { - 1 } \mathbf { A } ^ { - 1 }
$$

or

$$
( \mathbf { A } + \mathbf { B } ) ^ { - 1 } = [ \mathbf { B } ( \mathbf { B } ^ { - 1 } + \mathbf { A } ^ { - 1 } ) \mathbf { A } ] ^ { - 1 } = \mathbf { A } ^ { - 1 } ( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } ) ^ { - 1 } \mathbf { B } ^ { - 1 } .
$$

Theorem 2: Let $\mathbf { A }$ and $\mathbf { B }$ be $n \times n$ PD matrices. If $\mathbf { A } + \mathbf { B }$ is PD, then $\mathbf { I } + \mathbf { A } \mathbf { B } ^ { - 1 }$ and $\mathbf { I } + \mathbf { B } \mathbf { A } ^ { - 1 }$ are PD and

$$
\begin{array} { r } { ( \mathbf { A } + \mathbf { B } ) ^ { - 1 } = \mathbf { B } ^ { - 1 } - \mathbf { B } ^ { - 1 } ( \mathbf { I } + \mathbf { A } \mathbf { B } ^ { - 1 } ) ^ { - 1 } \mathbf { A } \mathbf { B } ^ { - 1 } } \\ { = \mathbf { A } ^ { - 1 } - \mathbf { A } ^ { - 1 } ( \mathbf { I } + \mathbf { B } \mathbf { A } ^ { - 1 } ) ^ { - 1 } \mathbf { B } \mathbf { A } ^ { - 1 } . } \end{array}
$$

Proof: From the identity

$$
\mathbf { A } ^ { - 1 } = ( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } ) - \mathbf { B } ^ { - 1 }
$$

premultiply by $\mathbf { B } ^ { - 1 } ( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } ) ^ { - 1 }$ and use Theorem 1

$$
\begin{array} { r l } & { \mathbf { B } ^ { - 1 } \big ( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } \big ) ^ { - 1 } \mathbf { A } ^ { - 1 } = \mathbf { B } ^ { - 1 } \big ( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } \big ) ^ { - 1 } \big ( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } \big ) } \\ & { \qquad - \mathbf { B } ^ { - 1 } \big ( \mathbf { A } ^ { - 1 } + \mathbf { B } ^ { - 1 } \big ) ^ { - 1 } \mathbf { B } ^ { - 1 } } \\ & { \qquad = \mathbf { B } ^ { - 1 } - \mathbf { B } ^ { - 1 } \big [ \mathbf { A } ^ { - 1 } \big ( \mathbf { I } + \mathbf { A } \mathbf { B } ^ { - 1 } \big ) \big ] ^ { - 1 } \mathbf { B } ^ { - 1 } } \\ & { \qquad = \mathbf { B } ^ { - 1 } - \mathbf { B } ^ { - 1 } \big ( \mathbf { I } + \mathbf { A } \mathbf { B } ^ { - 1 } \big ) ^ { - 1 } \mathbf { A } \mathbf { B } ^ { - 1 } . } \end{array}
$$

The left-hand side of this equation is $( \mathbf { A } + \mathbf { B } ) ^ { - 1 }$ (from Theorem 1). Hence,

$$
( \mathbf { A } + \mathbf { B } ) ^ { - 1 } = \mathbf { B } ^ { - 1 } - \mathbf { B } ^ { - 1 } ( \mathbf { I } + \mathbf { A } \mathbf { B } ^ { - 1 } ) ^ { - 1 } \mathbf { A } \mathbf { B } ^ { - 1 } .
$$

Theorem 3: If $\mathbf { A }$ and $\mathbf { B }$ are PD matrices of order $n$ and $m$ , respectively, and if $\mathbf { C }$ is of order $n \times m$ , then

$$
( \mathbf { C } ^ { T } \mathbf { A } ^ { - 1 } \mathbf { C } + \mathbf { B } ^ { - 1 } ) ^ { - 1 } \mathbf { C } ^ { T } \mathbf { A } ^ { - 1 } = \mathbf { B } \mathbf { C } ^ { T } ( \mathbf { A } + \mathbf { C B C } ^ { T } ) ^ { - 1 }
$$

provided the inverse exists.

Proof: From the identity

$$
\mathbf { C } ^ { T } ( \mathbf { A } ^ { - 1 } \mathbf { C B C } ^ { T } + \mathbf { I } ) ( \mathbf { I } + \mathbf { A } ^ { - 1 } \mathbf { C B C } ^ { T } ) ^ { - 1 } \equiv \mathbf { C } ^ { T }
$$

we have

$$
( \mathbf { C } ^ { T } \mathbf { A } ^ { - 1 } \mathbf { C B C } ^ { T } + \mathbf { C } ^ { T } ) ( \mathbf { A } ^ { - 1 } ( \mathbf { A } + \mathbf { C B C } ^ { T } ) ) ^ { - 1 } = \mathbf { C } ^ { T }
$$

or

$$
( \mathbf { C } ^ { T } \mathbf { A } ^ { - 1 } \mathbf { C } + \mathbf { B } ^ { - 1 } ) \mathbf { B } \mathbf { C } ^ { T } ( \mathbf { A } + \mathbf { C B } \mathbf { C } ^ { T } ) ^ { - 1 } \mathbf { A } = \mathbf { C } ^ { T } .
$$

Now premultiply by $( \mathbf { C } ^ { T } \mathbf { A } ^ { - 1 } \mathbf { C } + \mathbf { B } ^ { - 1 } ) ^ { - 1 }$ and postmultiply by $\mathbf { A } ^ { - 1 }$ , which yields

$$
\mathbf { B } \mathbf { C } ^ { T } ( \mathbf { A } + \mathbf { C B C } ^ { T } ) ^ { - 1 } = ( \mathbf { C } ^ { T } \mathbf { A } ^ { - 1 } \mathbf { C } + \mathbf { B } ^ { - 1 } ) ^ { - 1 } \mathbf { C } ^ { T } \mathbf { A } ^ { - 1 } .
$$

Theorem 4: The Schur Identity or insideout rule. If $\mathbf { A }$ is a PD matrix of order $n$ , and if $\mathbf { B }$ and $\mathbf { C }$ are any conformable matrices such that BC is order $n$ , then

$$
( \mathbf { A } + \mathbf { B C } ) ^ { - 1 } = \mathbf { A } ^ { - 1 } - \mathbf { A } ^ { - 1 } \mathbf { B } ( \mathbf { I } + \mathbf { C A } ^ { - 1 } \mathbf { B } ) ^ { - 1 } \mathbf { C A } ^ { - 1 } .
$$

Proof: Define

$$
\mathbf { X } = ( \mathbf { A } + \mathbf { B } \mathbf { C } ) ^ { - 1 } .
$$

Then

$$
\begin{array} { r } { \left( \mathbf { A } + \mathbf { B C } \right) \mathbf { X } = \mathbf { I } } \\ { \mathbf { A X } + \mathbf { B C X } = \mathbf { I } . } \end{array}
$$

Solve Eq. (B.9.5) for CX. First multiply by ${ { \bf A } ^ { - 1 } }$ to yield

$$
\mathbf { X } + \mathbf { A } ^ { - 1 } \mathbf { B } \mathbf { C } \mathbf { X } = \mathbf { A } ^ { - 1 } .
$$

Premultiply Eq. (B.9.6) by $\mathbf { C }$

$$
\mathbf { C } \mathbf { X } + \mathbf { C } \mathbf { A } ^ { - 1 } \mathbf { B } \mathbf { C } \mathbf { X } = \mathbf { C } \mathbf { A } ^ { - 1 } .
$$

Then

$$
\mathbf { C } \mathbf { X } = ( \mathbf { I } + \mathbf { C } \mathbf { A } ^ { - 1 } \mathbf { B } ) ^ { - 1 } \mathbf { C } \mathbf { A } ^ { - 1 } .
$$

Substitute Eq. (B.9.7) into Eq. (B.9.6) to yield

$$
\mathbf { X } = ( \mathbf { A } + \mathbf { B C } ) ^ { - 1 } = \mathbf { A } ^ { - 1 } - \mathbf { A } ^ { - 1 } \mathbf { B } ( \mathbf { I } + \mathbf { C A } ^ { - 1 } \mathbf { B } ) ^ { - 1 } \mathbf { C A } ^ { - 1 } .
$$

# B.10 REFERENCE

Graybill, F. A., An Introduction to Linear Statistical Models, McGraw-Hill, New York, 1961.

# Appendix C

# Equations of Motion

# C.1 LAGRANGE PLANETARY EQUATIONS

If the perturbing force $\mathbf { f }$ is conservative, it follows that f is derivable from a disturbing function, $D$ , such that $\mathbf { f } = \nabla D$ . The force f will produce temporal changes in the orbit elements that can be expressed by Lagrange’s Planetary Equations (e.g., Kaula, 1966):

$$
\begin{array} { r l } & { \frac { d a } { d t } = \frac { 2 } { n a } \frac { \partial D } { \partial M } } \\ & { \frac { d e } { d t } = \frac { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } { n a ^ { 2 } e } \left( ( 1 - e ^ { 2 } ) ^ { 1 / 2 } \frac { \partial D } { \partial M } - \frac { \partial D } { \partial \omega } \right) } \\ & { \frac { d i } { d t } = \frac { 1 } { h \sin i n } \left( \cos i \frac { \partial D } { \partial \omega } - \frac { \partial D } { \partial \Omega } \right) } \\ & { \frac { d \Omega } { d l } = \frac { 1 } { h \sin i n } \frac { \partial D } { \partial i } } \\ & { \frac { d \omega } { d t } = - \frac { \cos i } { h \sin i n } \frac { \partial D } { \partial i } + \frac { ( 1 - e ^ { 2 } ) ^ { 1 / 2 } } { n a ^ { 2 } e } \frac { \partial D } { \partial e } } \\ & { \frac { d M } { d t } = n - \frac { 1 - e ^ { 2 } } { n a ^ { 2 } e } \frac { \partial D } { \partial e } - \frac { 2 } { n a } \frac { \partial D } { \partial i } . } \end{array}
$$

Note that $h = n a ^ { 2 } [ 1 - e ^ { 2 } ] ^ { 1 / 2 }$ .

# C.2 GAUSSIAN FORM

If the perturbing force f is expressed as

$$
\mathbf { f } = \hat { R } \overline { { u } } _ { r } + \hat { T } \overline { { u } } _ { T } + \hat { N } \overline { { u } } _ { n }
$$

where the unit vectors are defined by the $R T N$ directions (radial, along-track, and cross-track) and $\hat { R } , \hat { T } , \hat { N }$ represent force components, the temporal changes in orbit elements can be expressed in the Gaussian form of Lagrange’s Planetary Equations (e.g., Pollard, 1966) as:

$$
\begin{array} { r l } & { \frac { d \delta } { d t } = \frac { 2 e ^ { 2 \pi \epsilon } } { h } \sin \hat { t } + \frac { 2 e ^ { 2 \pi \epsilon } h } { \mu \nu ^ { 2 } } } \\ & { + \frac { d \delta } { d t } - \frac { 1 } { h } \Big [ i \sin \hat { t } h + \hat { T } \big ( e + 2 \cos \hat { t } + c \cos ^ { 2 } \hat { t } / \mathcal { A } ( 1 + c \cos \hat { t } ) \big ) } \\ & { + \frac { d \delta } { d t } - \frac { 1 } { h } \cos ( \omega + f ) / \mathcal { A } } \\ & { - \frac { d \delta } { d t } - \frac { 1 } { h } \cos ( \omega + f ) / \mathcal { A } } \\ & { \frac { d \delta } { d t } - \frac { 1 } { h } \sin \hat { t } - \frac { 1 } { h } \cos ( \omega + f ) / \mathcal { A } } \\ & { + \frac { d \delta } { d t } - \frac { 1 } { \mu \nu } \cos \hat { t } / \mathcal { A } - \sin ( \omega + f ) / \mathcal { A } } \\ & { \quad \quad + \frac { ( d \delta ) } { d t } + \eta \theta \sin \hat { t } / \mathcal { A } } \\ & { \frac { d \mathcal { A } } { d t } = - \frac { 1 } { \mu \nu } \Big ( \frac { 2 } { \pi } - \frac { 1 - e ^ { 2 \pi \epsilon } } { e } \operatorname* { s u p } \Big ( \hat { T } / \mathcal { A } ( 1 + c \cos \hat { t } ) \Big ) \hat { \mathcal { A } } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \end{array}
$$

The Gaussian form applies to either conservative or nonconservative forces.

# C.3 REFERENCES

Kaula, W. M., Theory of Satellite Geodesy, Blaisdell Publishing Co., Waltham, MA, 1966 (republished by Dover Publications, New York, 2000).

Pollard, H., Mathematical Introduction to Celestial Mechanics, Prentice-Hall, Inc., Englewood Cliffs, NJ, 1966.

# Appendix D

# Constants

# D.1 PHYSICAL CONSTANTS∗

The speed of light is an important fundamental constant since it effectively defines the length scale in a range measurement. As described in Chapter 3, the range measurement actually is based on a measurement of the time required for a signal to travel from the transmitter to the receiver. This time interval measurement is converted into a distance measurement (range) using the speed of light, $c$ . The value of $c$ was adopted by the International Astronomical Union (IAU) in 1976, to be a defining constant with the value

$$
c = 2 9 9 , 7 9 2 , 4 5 8 \mathrm { ~ m } \mathrm { s } ^ { - 1 } .
$$

The constant of gravitation, $G$ , is experimentally determined. A recent value is (Mohr and Taylor, 2003)

$$
G = 6 . 6 7 3 \times 1 0 ^ { - 1 1 } \pm 1 . 0 \times 1 0 ^ { - 1 3 } \mathrm { m ^ { 3 } \ k g ^ { - 1 } \ s ^ { - 2 } } .
$$

The IAU (1976) System of Astronomical Constants can be found in The Astronomical Almanac for the Year 2000 on pages K6 and K7. Updated constants are given by Seidelmann (1992) and McCarthy (1996).

# D.2 EARTH CONSTANTS

For an Earth-orbiting satellite, the normalized gravity coefficients $\hat { C } _ { l m }$ and $\bar { S } _ { l m }$ ), $G M$ , and $a _ { e }$ are required. Recent determinations include the WGS-84 (DMA, 1987), JGM-3 field (Tapley et al., 1996), EGM-96 (Lemoine et al., 1998),

and the GRIMS-C1 (Gruber et al., 2000). The degree and order eight subset of JGM-3 is given in the Table D.1 with standard deviations. Conversion of normalized coefficients to conventional coefficients can be accomplished by:

$$
\begin{array} { l } { { C _ { l m } = N _ { l m } \bar { C } _ { l m } } } \\ { { S _ { l m } = N _ { l m } \bar { S } _ { l m } } } \\ { { N _ { l m } = \sqrt { \displaystyle \frac { ( l - m ) ! ( 2 l + 1 ) ( 2 - \delta _ { 0 m } ) } { ( l + m ) ! } } } } \end{array}
$$

where $\delta _ { 0 m }$ is the Kronecker delta function, which is zero when $m$ is not zero, otherwise it is one. Furthermore, for zonal harmonics, the commonly used $J _ { \ell }$ correspond to $m = 0$ , and

$$
J _ { l } = - C _ { l 0 } .
$$

The ellipsoidal model of the Earth was described in Chapter 2. Current ellipsoid parameters adopted by the IERS (McCarthy, 1996) are:

$$
a _ { e } = 6 3 7 8 1 3 6 . 4 9 \pm 0 . 1 \mathrm { m }
$$

$$
1 / f = 2 9 8 . 2 5 6 4 5 \pm 0 . 0 0 0 0 1 .
$$

# D.3 LUNAR, SOLAR, AND PLANETARY MASSES

Additional parameters required for the description of satellite motion include the gravitational parameters for the Sun, Moon, and planets. The values that are used with the planetary ephemerides, such as DE-405 (Standish, et al., 1997), are given in Table D.2. Additional information can be found in McCarthy (1996), Seidelmann (1992), and Standish et al. (1997). All mass parameters have been determined from observations; consult the references for uncertainties.

Table D.1 JGM-3 Earth Gravity Model   

<table><tr><td>lm</td><td>T</td><td>S</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>啦</td><td>i</td></tr><tr><td>20</td><td>-0.48416954845647E-03</td><td>0.00000000000000E+00</td><td>0.4660E-10</td><td>0.0000E+00</td></tr><tr><td>30</td><td>0.95717059088800E-06</td><td>0.00000000000000E+00</td><td>0.3599E-10</td><td>0.0000E+00</td></tr><tr><td>40</td><td>0.53977706835730E-06</td><td>0.00000000000000E+00</td><td>0.1339E-09</td><td>0.0000E+00</td></tr><tr><td>50</td><td>0.68658987986543E-07</td><td>0.00000000000000E+00</td><td>0.8579E-10</td><td>0.0000E+00</td></tr><tr><td>60</td><td>-0.14967156178604E-06</td><td>0.00000000000000E+00</td><td>0.2428E-09</td><td>0.0000E+00</td></tr><tr><td>70</td><td>0.90722941643232E-07</td><td>0.00000000000000E+00</td><td>0.2604E-09</td><td>0.0000E+00</td></tr><tr><td>80</td><td>0.49118003174734E-07</td><td>0.00000000000000E+00</td><td>0.3996E-09</td><td>0.0000E+00</td></tr><tr><td>2 1</td><td>-0.18698764000000E-09</td><td>0.11952801000000E-08</td><td>0.0000E+00</td><td>0.0000E+00</td></tr><tr><td>31</td><td>0.20301372055530E-05</td><td>0.24813079825561E-06</td><td>0.1153E-09</td><td>0.1152E-09</td></tr><tr><td>41</td><td>-0.53624355429851E-06</td><td>-0.47377237061597E-06</td><td>0.8693E-10</td><td>0.8734E-10</td></tr><tr><td></td><td>-0.62727369697705E-07</td><td>-0.94194632134383E-07</td><td>0.2466E-09</td><td>0.2465E-09</td></tr><tr><td>6</td><td>-0.76103580407274E-07</td><td>0.26899818932629E-07</td><td>0.2702E-09</td><td>0.2752E-09</td></tr><tr><td></td><td>0.28028652203689E-06</td><td>0.94777317813313E-07</td><td>0.4361E-09</td><td>0.4344E-09</td></tr><tr><td></td><td>0.23333751687204E-07</td><td>0.58499274939368E- -07</td><td>0.5070E-09</td><td>0.5137E-09</td></tr><tr><td>2</td><td>0.24392607486563E-05</td><td>-0.14002663975880E- -05</td><td>0.3655E-10</td><td>0.3709E-10</td></tr><tr><td>2</td><td>0.90470634127291E-06</td><td>-0.61892284647849E-06</td><td>0.9378E-10</td><td>0.9375E-10</td></tr><tr><td>42</td><td>0.35067015645938E-06</td><td>0.66257134594268E-06</td><td>0.1559E-09</td><td>0.1560E-09</td></tr><tr><td></td><td>0.65245910276353E-06</td><td>-0.32333435244435E-06</td><td>0.2392E-09</td><td>0.2398E-09</td></tr><tr><td>62</td><td>0.48327472124892E-07</td><td>-0.37381591944355E-06</td><td>0.3145E-09</td><td>0.3160E-09</td></tr><tr><td>72</td><td>0.32976022742410E-06</td><td>0.93193696831045E-07</td><td>0.4635E-09</td><td>0.4587E-09</td></tr><tr><td>82</td><td>0.80070663931587E-07</td><td>0.65518559097464E-07</td><td>0.5185E-09</td><td>0.5323E-09</td></tr><tr><td>33</td><td>0.72114493982309E-06</td><td>0.14142039847354E-05</td><td>0.5755E-10</td><td>0.5720E-10</td></tr><tr><td>43</td><td>0.99086890577441E-06</td><td>-0.20098735484731E-06</td><td>0.7940E-10</td><td>0.7942E-10</td></tr><tr><td>53</td><td>-0.45183704808780E-06</td><td>-0.21495419346421E-06</td><td>0.1599E-09</td><td>0.1616E-09</td></tr><tr><td>63</td><td>0.57020965757974E-07</td><td>0.88894738008251E-08</td><td>0.2598E-09</td><td>0.2574E-09</td></tr><tr><td>73</td><td>0.25050152675038E-06</td><td>-0.21732010845254E-06</td><td>0.3656E-09</td><td>0.3736E-09</td></tr><tr><td>83</td><td>-0.19251764331400E-07</td><td>-0.86285836534248E-07</td><td>0.4947E-09</td><td>0.4918E-09</td></tr><tr><td>44</td><td>-0.18848136742527E-06</td><td>0.30884803690355E-06</td><td>0.7217E-10</td><td>0.7228E-10</td></tr><tr><td>54</td><td>-0.29512339302196E-06</td><td>0.49741427230934E-07</td><td>0.9264E-10</td><td>0.9288E-10</td></tr><tr><td>64</td><td>-0.86228032619800E-07</td><td>-0.47140511232148E-06</td><td>0.1656E-09</td><td>0.1663E-09</td></tr><tr><td>74</td><td>-0.27554096307403E-06</td><td>-0.12414151248516E-06</td><td>0.2665E-09</td><td>0.2656E-09</td></tr><tr><td>84</td><td>-0.24435806439297E-06</td><td>0.69857074850431E-07</td><td>0.4033E-09</td><td>0.4063E-09</td></tr><tr><td>55</td><td>0.17483157769990E-06</td><td>-0.66939293724911E-06</td><td>0.8139E-10</td><td>0.8131E-10</td></tr><tr><td>65</td><td>-0.26711227171966E-06</td><td>-0.53641016466390E-06</td><td>0.8465E-10</td><td>0.8510E-10</td></tr><tr><td>75</td><td>0.16440038146411E-08</td><td>0.18075335233506E-07</td><td>0.1832E-09</td><td>0.1835E-09</td></tr><tr><td>85</td><td>-0.25498410010257E-07</td><td>0.89090297494640E-07</td><td>0.2586E-09</td><td>0.2571E-09</td></tr><tr><td>66</td><td>0.95016518338557E-08</td><td>-0.23726147889522E-06</td><td>0.8021E-10</td><td>0.8081E-10</td></tr><tr><td>76</td><td>-0.35884263307918E-06</td><td>0.15177808443426E-06</td><td>0.5899E-10</td><td>0.5913E-10</td></tr><tr><td>86</td><td>-0.65859353864388E-07</td><td>0.30892064157956E-06</td><td>0.1566E-09</td><td>0.1569E-09</td></tr><tr><td>77</td><td>0.13795170564076E-08</td><td>0.24128594080773E-07</td><td>0.9709E-10</td><td>0.9747E-10</td></tr><tr><td>87</td><td>0.67262701848734E-07</td><td>0.74813196768710E-07</td><td>0.9308E-10</td><td>0.9378E-10</td></tr><tr><td>88</td><td>-0.12397061395498E-06</td><td>0.12044100668766E-06</td><td>0.1379E-09</td><td>0.1384E-09</td></tr></table>

$G M _ { \mathrm { E a r t h } } = 3 . 9 8 6 0 0 4 4 1 5 \times 1 0 ^ { 1 4 } \pm 8 \times 1 0 ^ { 5 } \mathrm { m } ^ { 3 } \mathrm { s } ^ { - 2 }$ $a _ { e } = 6 3 7 8 1 3 6 . 3 \ : \mathrm { m }$

Table D.2   
Lunar, Solar and Planetary Masses   

<table><tr><td>Planet</td><td>GM (m³ s-2)</td></tr><tr><td>Mercury</td><td>2.203208 × 1013</td></tr><tr><td>Venus</td><td>3.248586 × 1014</td></tr><tr><td>Mars</td><td>4.282831 × 1013</td></tr><tr><td>Jupiter</td><td>1.267128 × 1017</td></tr><tr><td>Saturn</td><td>3.794063× 1016</td></tr><tr><td>Uranus</td><td>5.794549 ×1015</td></tr><tr><td>Neptune</td><td>6.836534 × 1015</td></tr><tr><td>Pluto</td><td>9.816009 × 1011</td></tr><tr><td>Moon</td><td>4.902801 × 1012</td></tr><tr><td>Sun</td><td>1.327124 × 1020</td></tr></table>

The Earth-Moon mass ratio is 81.30056 and 1 Astronomical Uni $= 1 4 9$ , 597, 870, 691 m, as provided with DE-405.

Note that using the Earth-Moon mass ratio in Table D.2 yields $G M _ { \mathrm { M o o n } } =$ $4 . 9 0 2 8 0 4 \times 1 0 ^ { 1 2 } m ^ { 3 } s ^ { - 2 }$ based on the $G M _ { \mathrm { E a r t h } }$ =from JGM-3. The difference with $G M _ { \mathrm { M o o n } }$ 10in Table D.2 is caused by the $G M _ { \mathrm { E a r t h } }$ adopted in DE-405.

# D.4 REFERENCES

Defense Mapping Agency, Department of Defense World Geodetic System 1984, DMA Technical Report 8350.2, Washington, DC, September, 1987.

Gruber, T., A. Bode, C. Reigber, P. Schwintzer, G. Balmino, R. Biancale, J. Lemoine, “GRIM5-C1: Combination solution of the global gravity field to degree and order 120,” Geophys. Res. Ltrs., Vol. 27, No. 24, pp. 4005–4008, December 2000.

Lemoine, F., S. Kenyon, J. Factor, R. Trimmer, N. Pavlis, D. Chinn, C. Cox, S. Klosko, S. Luthcke, M. Torrence, Y. Wang, R. Williamson, E. Pavlis, R. Rapp, and T. Olson, The development of the Joint NASA GSFC and the National Imagery and Mapping Agency (NIMA) Geopotential Model EGM96, NASA/TP–1998–206861, Greenbelt, MD, July 1998.

Le Systeme International d’Unites (SI), Bureau International des Poids et Mesures, Sevres, France, 1991.

McCarthy, D. (ed.), IERS Conventions (1996), IERS Technical Note 21, International Earth Rotation Service, Observatoire de Paris, July 1996.

Mohr, P. J., and B. Taylor, “The fundamental physical constants,” Physics Today, Vol. 56, No. 8, Supplement, pp. BG6–BG13, August 2003.

Seidelmann, P. (ed.), Explanatory Supplement to the Astronomical Almanac, University Science Books, Mill Valley, CA, 1992.

Standish, E. M., X. Newhall, J. Williams, and W. Folkner, JPL Planetary and Lunar Ephemerides (CD-ROM), Willmann-Bell, Inc., Richmond, VA 1997.

Tapley, B. D., M. Watkins, J. Ries, G. Davis, R. Eanes, S. Poole, H. Rim, B. Schutz, C. Shum, R. Nerem, F. Lerch, J. Marshall, S. Klosko, N. Pavlis, and R. Williamson, “The Joint Gravity Model 3,” J. Geophys. Res., Vol. 101, No. B12, pp. 28,029–28,049, December 10, 1996.

# Appendix E

# Analytical Theory for Near-Circular Orbits

# E.1 DESCRIPTION

An analytical theory for the variation of the orbit elements under the influence of the zonal harmonics $J _ { 2 }$ through $J _ { 5 }$ has been developed by Brouwer (1959). This appendix presents a simplificat ion of his equations for the time variation of the orbit elements for a near-circular orbit under the influence of $J _ { 2 }$ . The classical elements $e$ and $\omega$ used by Brouwer have been replaced by $h = e \sin \omega$ and $k = e \cos \omega$ since the argument of perigee is not well defined for a nearcircular orbit. The analytical solutions are given by (Born et al., 2001):

$$
\begin{array} { r l } & { a ( t ) = \hat { a } + k _ { 1 } \cos { 2 \hat { b } } } \\ & { h ( t ) = \hat { k } ( t ) + k _ { 2 } \sin { \hat { \beta } } + k _ { 3 } \sin { 3 \hat { \beta } } } \\ & { k ( \hat { t } ) = \hat { k } ( t ) + k _ { 4 } \cos { \hat { \beta } } + k _ { 3 } \cos { 3 \hat { \beta } } } \\ & { \hat { \iota } ( t ) = \hat { \iota } ( t ) + k _ { 5 } \cos { 2 \hat { \beta } } } \\ & { \Omega ( t ) = \hat { \Omega } + k _ { 6 } \sin { 2 \hat { \beta } } } \\ & { \beta ( \hat { t } ) = \hat { \beta } + k _ { 7 } \sin { 2 \hat { \beta } } + k _ { 8 } ( t - t _ { 0 } ) ^ { 2 } } \\ & { \hat { h } ( t ) = \hat { e } \sin { \hat { \alpha } } } \\ & { \hat { \Omega } - \hat { \Omega } ( t _ { 0 } ) + k _ { 9 } ( t - t _ { 0 } ) } \\ & { \hat { \omega } = \hat { w } ( t _ { 0 } ) + k _ { 1 0 } ( t - t _ { 0 } ) } \\ & { \hat { \beta } = \hat { \beta } ( t _ { 0 } ) + k _ { 1 1 } ( t - t _ { 0 } ) } \end{array}
$$

where $\beta = \omega + M$ and $( ^ { - } )$ represents the mean value of the element. Mean values are given by

$$
\begin{array} { r l } & { \quad \bar { a } = a ( t _ { 0 } ) - K _ { 1 } \cos 2 \beta ( t _ { 0 } ) } \\ & { \quad \bar { h } ( t _ { 0 } ) = \bar { e } \sin \bar { \omega } ( t _ { 0 } ) = h ( t _ { 0 } ) - K _ { 2 } \sin \beta ( t _ { 0 } ) - K _ { 3 } \sin 3 \beta ( t _ { 0 } ) } \\ & { \quad \bar { k } ( t _ { 0 } ) = \bar { e } \cos \bar { \omega } ( t _ { 0 } ) = k ( t _ { 0 } ) - K _ { 4 } \cos \beta ( t _ { 0 } ) - K _ { 3 } \cos 3 \beta ( t _ { 0 } ) } \\ & { \quad \bar { e } = \sqrt { \bar { h } ^ { 2 } ( t _ { 0 } ) + \bar { k } ^ { 2 } ( t _ { 0 } ) } } \\ & { \quad \quad \bar { \omega } ( t _ { 0 } ) = \mathrm { a t a n 2 ~ } \left( \bar { h } ( t _ { 0 } ) , \bar { k } ( t _ { 0 } ) \right) } \\ & { \quad \quad \bar { \tau } = i ( t _ { 0 } ) - K _ { 5 } \cos 2 \beta ( t _ { 0 } ) } \\ & { \quad \quad \sum _ { \bar { \omega } ( t _ { 0 } ) } = \Omega ( t _ { 0 } ) - K _ { 6 } \sin 2 \beta ( t _ { 0 } ) } \\ & { \quad \quad \bar { \beta } ( t _ { 0 } ) = \beta ( t _ { 0 } ) - K _ { 7 } \sin 2 \beta ( t _ { 0 } ) . } \end{array}
$$

Also,

$$
\begin{array} { r l } & { E _ { 1 } = 3 \cdots \gamma _ { 2 } e ^ { 2 \theta } } \\ & { K _ { 3 } = \gamma _ { 2 } ^ { \prime } ( 1 6 \frac { \theta } { 2 } ) ^ { 2 } } \\ & { K _ { 3 } = \frac { 3 } { 2 } ( 1 6 \frac { \theta } { 2 } ) ^ { 2 } } \\ & { K _ { 3 } = \frac { \gamma _ { 1 } } { 2 } e ^ { 2 \theta } } \\ & { K _ { 4 } = \frac { 3 } { 2 } ( 1 6 - \frac { 1 5 } { 2 } \delta ^ { 2 } ) } \\ & { K _ { 4 } = \frac { 3 } { 2 } ( 1 6 \frac { \theta } { 2 } ) ^ { 2 } } \\ & { K _ { 5 } = \frac { 3 } { 2 } \gamma _ { 2 } e ^ { 3 \theta } } \\ & { K _ { 6 } = \frac { 3 } { 2 } \gamma _ { 5 } \theta ^ { 3 } } \\ & { K _ { 7 } = \frac { 3 } { 2 } \gamma _ { 1 } ( 1 - 8 6 \pi ^ { 2 } ) } \\ & { K _ { 8 } = \frac { 3 } { 2 } \theta \gamma _ { 2 } ^ { \prime } ( \gamma _ { 2 } \theta _ { 3 } ^ { 2 } \frac { \theta } { 2 } ) } \\ & { K _ { 8 } = - \frac { 3 } { 8 } \theta \gamma _ { 2 } \theta \gamma _ { 3 } ^ { \prime } } \\ & { K _ { 8 } = - \frac { 3 } { 2 } \theta \gamma _ { 4 } ( 1 - \delta \pi ^ { 2 } ) } \\ & { K _ { 8 } = \frac { 3 } { 2 } \gamma _ { 2 } \theta ( 1 + \delta \pi ^ { 2 } ) } \\ & { K _ { 1 1 } = \pi ^ { 2 } \delta ( 1 + \delta \pi ^ { 2 } ) . } \end{array}
$$

and

$$
\begin{array} { c } { { \displaystyle \gamma _ { 2 } = \frac { J _ { 2 } } { 2 } \left( \frac { R } { \bar { a } } \right) ^ { 2 } } } \\ { { \displaystyle \theta = \cos \bar { \imath } } } \\ { { \displaystyle \delta = \sin \bar { \imath } } } \end{array}
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0008_pages_0491-0560/auto/images/9038d09aa29a0906ec65d2b9c87fb811e5e0968af63183bd53d6595dc2a9f5d6.jpg)  
Figure E.1.1: Analytical solution results for the QUIKSCAT orbit using Eq. (E.1.1).

$$
\begin{array} { r l } & { \bar { n } { = } \displaystyle \frac { \mu ^ { 1 / 2 } } { \bar { a } ^ { 3 / 2 } } , \qquad \mu { = } G M } \\ & { \rho { = } \mathrm { a v e r a g e ~ a t m o s p h e r i c ~ d e n s i t y ~ a t ~ s a t e l l i t e ~ a l t i t u d e } } \\ & { v _ { \mathrm { r e l } } { = } \mathrm { a v e r a g e ~ v e l o c i t y ~ o f ~ t h e ~ s a t e l l i t e ~ r e l a t i v e ~ t o ~ t h e ~ a t m o s p h e r e } } \end{array}
$$

This representation is based on the solution developed by Brouwer (1959), except for the last term in the $\beta ( t )$ expression, $k _ { 8 } ( t - t _ { 0 } ) ^ { 2 }$ . This quadratic term is introduced to compensate for drag.

Note that it is not necessary to iterate to determine mean values because this is a first-order theory in $J _ { 2 }$ . It is necessary to use $\bar { a }$ to compute $\bar { n }$ in order to avoid an error of $O ( J _ { 2 } )$ in computing $K _ { 1 1 }$ .

Other useful equations are

$$
\begin{array} { l } { \displaystyle { r ( t ) = \frac { a ( t ) \left[ 1 - \left( h ( t ) ^ { 2 } + k ^ { 2 } ( t ) \right) \right] } { 1 + k ( t ) \cos \beta ( t ) + h ( t ) \sin \beta ( t ) } } } \\ { \displaystyle { e ( t ) = \sqrt { h ^ { 2 } ( t ) + k ^ { 2 } ( t ) } } } \end{array}
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0008_pages_0491-0560/auto/images/0c01e80c6c1dbd32dcbec5f18acbe3368b21b4bf975523f9117f449a55f246af.jpg)  
Figure E.1.2: Difference between QUIKSCAT analytical solutions and numerical integration.

$$
\begin{array} { c } { { \omega ( t ) = \mathrm { a t a n 2 } \left( h ( t ) , k ( t ) \right) } } \\ { { M ( t ) = \beta ( t ) - \omega ( t ) . } } \end{array}
$$

The equation for $r ( t )$ also can be written in terms of the mean elements as follows

$$
\begin{array} { l } { { \displaystyle r ( t ) = \bar { a } [ 1 - \bar { e } \cos \overline { { { M } } } ( t ) ] + \frac { 3 } { 4 } \frac { R ^ { 2 } } { \bar { a } } J _ { 2 } ( 3 \sin ^ { 2 } \bar { \imath } - 2 ) } } \\ { { \displaystyle ~ + \frac { 1 } { 4 } \frac { R ^ { 2 } } { a } J _ { 2 } \sin ^ { 2 } \bar { \imath } \cos 2 \bar { \beta } } } \end{array}
$$

where

$$
\overline { { { { \cal M } } } } ( t ) = \bar { \beta } ( t ) - \bar { \omega } ( t ) .
$$

# E.2 EXAMPLE

Figure E.2.1 presents the classical orbit elements and radius time history for the QUIKSCAT satellite over one day computed by using Eq. (E.1.1). Initial conditions are given on the figure. Fig. E.2.2 presents the differences between the analytical solutions and numerical integration.

We have ignored terms of $O ( e J _ { 2 } )$ and $O ( J _ { 2 } ^ { 2 } )$ in developing this theory. Here the values of $e$ and $J _ { 2 }$ are the same order of magnitude. However, errors of $O ( e J _ { 2 } )$ are dominant since reducing the initial eccentricity to $1 0 ^ { - 4 }$ reduces the periodic errors in the analytical solutions by a factor of two. Secular errors of $O ( J _ { 2 } ^ { 2 } )$ are apparent in $\Omega$ . Including secular rates of $O ( J _ { 2 } ^ { 2 } )$ , given by Brouwer (1959), reduces the RMS error in $\Omega$ by an order of magnitude.

# E.3 REFERENCES

Born, G. H., D. B. Goldstein and B. Thompson, An Analytical Theory for Orbit Determination, J. Astronaut. Sci., Vol. 49, No. 2, pp. 345–361, April–June 2001.

Brouwer, D., “Solutions of the problem of artificial satellite theory without drag,” Astron. J., Vol. 64, No. 9, pp. 378–397, November 1959.

# Appendix F

# Example of State Noise and Dynamic Model Compensation

# F.1 INTRODUCTION

Consider a target particle that moves in one dimension along the $x$ axis in the positive direction.∗ Nominally, the particle’s velocity is a constant $1 0 \mathrm { m / s e c }$ . This constant velocity is perturbed by a sinusoidal acceleration in the $x$ direction, which is unknown and is described by:

$$
\eta ( t ) = \frac { 2 \pi } { 1 0 } \cos \left( \frac { 2 \pi } { 1 0 } t \right) \mathrm { m / s e c } .
$$

The perturbing acceleration, perturbed velocity, and position perturbation (perturbed position—nominal position) are shown in Fig. F.1.1.

A measurement sensor is located at the known position $x = - 1 0 \textrm { m }$ . This sensor takes simultaneous range and range-rate measurements at a frequency of $1 0 ~ \mathrm { H z }$ . The range measurements are corrupted by uncorrelated Gaussian noise having a mean of zero and a standard deviation of $1 \textrm { m }$ . Likewise, the range-rate measurements are corrupted by uncorrelated Gaussian noise having a mean of zero and a standard deviation of $0 . 1 \mathrm { m } / \mathrm { s e c }$ . We want to estimate the state of the particle, with primary emphasis on position accuracy, using these observations given the condition that the sinusoidal perturbing acceleration is unknown. The following estimation results were generated using the extended sequential algorithm discussed in Section 4.7.3.

A simple estimator for this problem incorporates a two-parameter state vector

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0008_pages_0491-0560/auto/images/de860162f7bdb77f3ed2359709e333db3cc3901164942493f6597dc588634ebd.jpg)  
Figure F.1.1: Perturbed particle motion.

consisting of position and velocity:

$$
{ \bf X } ( t ) = \left[ \begin{array} { l } { x ( t ) } \\ { \dot { x } ( t ) } \end{array} \right] = \left[ \begin{array} { l } { x ( t _ { 0 } ) + \dot { x } ( t _ { 0 } ) ( t - t _ { 0 } ) } \\ { \dot { x } ( t _ { 0 } ) } \end{array} \right] .
$$

The dynamic model assumes constant velocity for the particle motion and does

not incorporate process noise. The state transition matrix for this estimator is:

$$
\Phi ( t , t _ { 0 } ) = { \left[ \begin{array} { l l } { 1 t - t _ { 0 } } \\ { 0 \quad 1 } \end{array} \right] }
$$

and the observation/state mapping matrix is a two-by-two identity matrix:

$$
\widetilde { H } = \left[ \begin{array} { l } { 1 0 } \\ { 0 1 } \end{array} \right] .
$$

Since the sinusoidal acceleration is not included in the dynamic model and the filter has no means of compensation for the dynamic model defici ency, the filter quickly saturates and its estimation performance is poor. Fig. F.1.2 shows the actual position errors along with the one-sigma position standard deviation bounds estimated by the filter . The position error RMS is $0 . 9 6 5 3 \mathrm { ~ m ~ }$ , and only 18.60 percent of the actual position errors are within the estimated one-sigma standard deviation bounds. Fig. F.1.3 shows the corresponding velocity errors and onesigma velocity standard deviation bounds. As with position, the velocity errors are generally well outside the standard deviation bounds.

# F.2 STATE NOISE COMPENSATION

The State Noise Compensation (SNC) algorithm (see Section 4.9) provides a means to improve estimation performance through partial compensation for the unknown sinusoidal acceleration. SNC allows for the possibility that the state dynamics are influenced by a random acceleration. A simple SNC model uses a two-state filter but assumes that particle dynamics are perturbed by an acceleration that is characterized as simple white noise:

$$
\ddot { x } ( t ) = \eta ( t ) = u ( t )
$$

where $u ( t )$ is a stationary Gaussian process with a mean of zero and a variance of $\sigma _ { u } ^ { 2 } \delta ( t - \tau )$ , and $\delta ( t - \tau )$ is the Dirac delta function. The Dirac delta function is not an ordinary function, and to be mathematically rigorous, white noise is a fictiti ous process. However, in linear stochastic models, it can be treated formally as an integrable function. Application of Eq. (4.9.1) to this case results in

$$
{ \Big [ } { \dot { x } } ( t ) { \Big ] } = { \Big [ } 0 1 { \Big ] } { \Big [ } x ( t ) { \Big ] } + { \Big [ } 0 { \Big ] } u ( t )
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0008_pages_0491-0560/auto/images/f99ba31501d1ce030fed68eff6216639eb24ce835028d6b421d7ca96eaca4d9a.jpg)  
Figure F.1.2: Position errors and estimated standard deviation bounds from the two-state filter without process noise.

where the state propagation matrix A is identified as:

$$
A = { \binom { 0 1 } { 0 0 } }
$$

and the process noise mapping matrix is:

$$
\begin{array} { r } { B = \bigg [ \begin{array} { c } { 0 } \\ { 1 } \end{array} \bigg ] . } \end{array}
$$

The state transition matrix is the same:

$$
\Phi ( t , t _ { 0 } ) = { \Bigg [ } { 1 t - t _ { 0 } } { \Bigg ] } ~ .
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0008_pages_0491-0560/auto/images/57dffb58609f5d82cd9312900618b40d2ec94c1ada7a07c141232a7af3544e90.jpg)  
Figure F.1.3: Velocity errors and estimated standard deviation bounds from the two-state filter without process noise.

The process noise covariance integral (see Eq. (4.9.44)) needed for the time update of the estimation error covariance matrix at time $t$ is expressed as:

$$
Q _ { \eta } ( t ) = \sigma _ { u } ^ { 2 } \int _ { t _ { 0 } } ^ { t } \Phi ( t , \tau ) B B ^ { T } \Phi ^ { T } ( t , \tau ) d \tau
$$

where

$$
\Phi ( t , \tau ) = \left[ { 1 \left( { t - \tau } \right) } \right] .
$$

Substituting for $B$ and $\Phi ( t , \tau )$ and evaluating results in the process noise covariance matrix:

$$
Q _ { 7 } ( t ) = \sigma _ { u } ^ { 2 } \left[ \frac { 1 } { 3 } ( t - t _ { 0 } ) ^ { 3 } \frac { 1 } { 2 } ( t - t _ { 0 } ) ^ { 2 } \right]
$$

where $t - t _ { 0 }$ is the measurement update interval; that is, $t _ { k } - t _ { k - 1 } = 0 . 1$ sec. The implication of this is that the original deterministic constant velocity model of particle motion is modified to include a random component that is a constantdiffusion Brownian motion process, $\sigma _ { u } ^ { 2 }$ being known as the diffusion coefficient (Maybeck, 1979).

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0008_pages_0491-0560/auto/images/1ec57391824d6cb269c308f97eae488e5bd07c6541c12de0738d29a35d6019fd.jpg)  
Figure F.2.1: Position errors and estimated standard deviation bounds from the two-state SNC filter .

The magnitude of the process noise covariance matrix and its effect on estimation performance are functions of this diffusion coefficient, hence $\sigma _ { u }$ is a tuning parameter whose value can be adjusted to optimize performance. Figures F.2.1 and F.2.2 show the result of the tuning process. The optimal value of $\sigma _ { u }$ is $0 . 4 2 ~ \mathrm { m / s e c ^ { 3 / 2 } }$ at which the position error RMS is $0 . 1 3 7 8 \mathrm { m }$ and 56.81 percent of the actual position errors fall within the estimated one-sigma standard deviation bounds. The large sinusoidal error signature in both position and velocity displayed by the uncompensated filter is eliminated by SNC.

Note that there is no noticable change in the position standard deviations; however, the velocity standard deviations show a significant increase when process noise is included. This increase in the velocity variances prevents the components of the Kalman gain matrix from going to zero with the attendant saturation of the filte r.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0008_pages_0491-0560/auto/images/a8940fa2726c56d42f646b700821056be1280406ede6b579c97190353ccbec65.jpg)  
Figure F.2.2: Velocity errors and estimated standard deviation bounds from the two-state filter with SNC process noise.

# F.3 DYNAMIC MODEL COMPENSATION

A more sophisticated process noise model is provided by the Dynamic Model Compensation (DMC) formulation. DMC assumes that the unknown acceleration can be characterized as a first-order linear stochastic differential equation, commonly known as a Langevin equation:

$$
\dot { \eta } ( t ) + \beta \eta ( t ) = u ( t ) ,
$$

where $u ( t )$ is a white zero-mean Gaussian process as described earlier and $\beta$ is the inverse of the correlation time:

$$
\beta = \frac { 1 } { \tau } .
$$

The solution to this Langevin equation is

$$
\eta ( t ) = \eta _ { 0 } e ^ { - \beta ( t - t _ { 0 } ) } + \int _ { t _ { 0 } } ^ { t } e ^ { - \beta ( t - \tau ) } u ( \tau ) d \tau .
$$

This is the Gauss-Markov process (more precisely known as an Ornstein-Uhlenbeck process) described in Section 4.9. Note that, unlike SNC, the DMC process noise model yields a deterministic acceleration term as well as a purely random term. The deterministic acceleration can be added to the state vector and estimated along with the velocity and position; the augmented state vector becomes a threestate filter with

$$
\mathbf { X } ( t ) = \left[ \begin{array} { l } { x ( t ) } \\ { \dot { x } ( t ) } \\ { \eta _ { D } ( t ) } \end{array} \right]
$$

where $\eta _ { D } ( t )$ is the deterministic part of $\eta ( t )$ ; that is, $\eta _ { 0 } e ^ { - \beta \left( t - t _ { 0 } \right) }$ . Since the acceleration integrates into velocity and position increments, the dynamic model of the particle’s motion becomes

$$
\mathbf { X } ( t ) = \left[ \begin{array} { c } { x _ { 0 } + \dot { x } _ { 0 } ( t - t _ { 0 } ) + \frac { \eta _ { 0 } } { \beta } ( t - t _ { 0 } ) + \frac { \eta _ { 0 } } { \beta ^ { 2 } } \left( e ^ { - \beta ( t - t _ { 0 } ) } - 1 \right) } \\ { \dot { x } _ { 0 } + \frac { \eta _ { 0 } } { \beta } \left( 1 - e ^ { - \beta ( t - t _ { 0 } ) } \right) } \\ { \eta _ { 0 } e ^ { - \beta ( t - t _ { 0 } ) } } \end{array} \right] .
$$

The correlation time, $\tau$ , can also be added to the estimated state, resulting in a four-parameter state vector. However, a tuning strategy that works well for many DMC estimation problems is to set $\tau$ to a near-optimal value and hold it constant, or nearly constant, during the estimation span. For simplicity, $\tau$ is held constant in this case, allowing the use of the three-parameter state vector just noted. The observation/state mapping matrix is a simple extension of the two-state case:

$$
\widetilde H = \left[ { 1 0 0 } \right] .
$$

Using the methods described in Example 4.2.3, the state transition matrix is found to be

$$
\Phi ( t , t _ { 0 } ) = \frac { \partial X ( t ) } { \partial X ( t _ { 0 } ) } = \left[ \begin{array} { l l l } { 1 t - t _ { 0 } \frac { 1 } { \beta } ( t - t _ { 0 } ) + \frac { 1 } { \beta ^ { 2 } } \left( e ^ { - \beta ( t - t _ { 0 } ) } - 1 \right) } & { } \\ { 0 } & { 1 } & { \frac { 1 } { \beta } \left( 1 - e ^ { - \beta ( t - t _ { 0 } ) } \right) } \\ { 0 } & { 0 } & { e ^ { - \beta ( t - t _ { 0 } ) } } \end{array} \right] .
$$

The state propagation matrix for this case is

$$
A = { \left[ \begin{array} { l l } { 0 1 } & { 0 } \\ { 0 0 } & { 1 } \\ { 0 0 } & { - \beta } \end{array} \right] }
$$

and the process noise mapping matrix is

$$
B = { \binom { 0 } { 0 } } \cdot
$$

With these, the process noise covariance integral becomes (in terms of the components of $\Phi ( t , \tau )$ )

$$
\begin{array} { r l } & { Q _ { \eta } ( t ) = \sigma _ { u } ^ { 2 } \times } \\ & { \int _ { t _ { 0 } } ^ { t } \left[ \begin{array} { c c } { \Phi _ { 1 , 3 } ^ { 2 } ( t , \tau ) } & { \Phi _ { 1 , 3 } ( t , \tau ) \Phi _ { 2 , 3 } ( t , \tau ) \Phi _ { 1 , 3 } ( t , \tau ) \Phi _ { 3 , 3 } ( t , \tau ) } \\ { \Phi _ { 2 , 3 } ( t , \tau ) \Phi _ { 1 , 3 } ( t , \tau ) } & { \Phi _ { 2 , 3 } ^ { 2 } ( t , \tau ) } & { \Phi _ { 2 , 3 } ( t , \tau ) \Phi _ { 3 , 3 } ( t , \tau ) } \\ { \Phi _ { 3 , 3 } ( t , \tau ) \Phi _ { 1 , 3 } ( t , \tau ) \Phi _ { 3 , 3 } ( t , \tau ) \Phi _ { 2 , 3 } ( t , \tau ) } & { \Phi _ { 3 , 3 } ^ { 2 } ( t , \tau ) } \end{array} \right] d \tau . } \end{array}
$$

Note that here $\tau$ designates the integration variable, not the correlation time. The expanded, integrated process noise covariance matrix terms follow: position variance:

$$
\begin{array} { l } { { \displaystyle Q _ { \eta 1 , 1 } ( t ) = \sigma _ { u } ^ { 2 } \biggl ( \frac { 1 } { 3 \beta ^ { 2 } } ( t - t _ { 0 } ) ^ { 3 } - \frac { 1 } { \beta ^ { 3 } } ( t - t _ { 0 } ) ^ { 2 } } } \\ { { \displaystyle \qquad + \frac { 1 } { \beta ^ { 4 } } ( t - t _ { 0 } ) ( 1 - 2 e ^ { - \beta ( t - t _ { 0 } ) } ) + \frac { 1 } { 2 \beta ^ { 5 } } ( 1 - e ^ { - 2 \beta ( t - t _ { 0 } ) } ) \biggr ) } } \end{array}
$$

position/velocity covariance:

$$
\begin{array} { r } { Q _ { \eta 1 , 2 } ( t ) = \sigma _ { u } ^ { 2 } \bigg ( \frac { 1 } { 2 \beta ^ { 2 } } ( t - t _ { 0 } ) ^ { 2 } - \frac { 1 } { \beta ^ { 3 } } ( t - t _ { 0 } ) ( 1 - e ^ { - \beta ( t - t _ { 0 } ) } ) } \\ { + \frac { 1 } { \beta ^ { 4 } } ( 1 - e ^ { - \beta ( t - t _ { 0 } ) } ) - \frac { 1 } { 2 \beta ^ { 4 } } ( 1 - e ^ { - 2 \beta ( t - t _ { 0 } ) } ) \bigg ) } \end{array}
$$

position/acceleration covariance:

$$
Q _ { \eta 1 , 3 } ( t ) = \sigma _ { u } ^ { 2 } \left( \frac { 1 } { 2 \beta ^ { 3 } } ( 1 - e ^ { - 2 \beta ( t - t _ { 0 } ) } ) - \frac { 1 } { \beta ^ { 2 } } ( t - t _ { 0 } ) e ^ { - \beta ( t - t _ { 0 } ) } \right)
$$

velocity variance:

$$
Q _ { \eta 2 , 2 } ( t ) = \sigma _ { u } ^ { 2 } \left( \frac { 1 } { \beta ^ { 2 } } ( t - t _ { 0 } ) - \frac { 2 } { \beta ^ { 3 } } \left( 1 - e ^ { - \beta ( t - t _ { 0 } ) } \right) + \frac { 1 } { 2 \beta ^ { 3 } } \left( 1 - e ^ { - 2 \beta ( t - t _ { 0 } ) } \right) \right)
$$

velocity/acceleration covariance:

$$
Q _ { \eta 2 , 3 } ( t ) = \sigma _ { u } ^ { 2 } \left( \frac { 1 } { 2 \beta ^ { 2 } } \left( 1 + e ^ { - 2 \beta ( t - t _ { 0 } ) } \right) - \frac { 1 } { \beta ^ { 2 } } e ^ { - \beta ( t - t _ { 0 } ) } \right)
$$

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0008_pages_0491-0560/auto/images/b1b7e4b7cb843cd05ef9da9dce3721d0d289e042724c6cf6d4b34621a0452f02.jpg)  
Figure F.3.1: Position errors and estimated standard deviation bounds from the three-state DMC filter .

acceleration variance:

$$
Q _ { \eta 3 , 3 } ( t ) = \frac { \sigma _ { u } ^ { 2 } } { 2 \beta } \left( 1 - e ^ { - 2 \beta ( t - t _ { 0 } ) } \right) .
$$

With $\tau$ fix ed at 200.0 sec (or $\beta = 0 . 0 0 5 \ \sec ^ { - 1 } ,$ ), the optimal value of $\sigma _ { u }$ is 0.26 $\mathrm { { m } / \mathrm { { s e c } ^ { 5 / 2 } } }$ . This combination produces the position error results shown in Fig. F.3.1. The position error RMS is $0 . 1 3 7 6 \mathrm { ~ m ~ }$ and 56.81 percent of the actual position errors are within the estimated one-sigma standard deviation bounds. Although not shown here, the plot of velocity errors exhibits a behavior similar to the velocity errors for the SNC filt er.

Figure F.3.2 is a plot of the RMS of the position error as a function of $\sigma _ { u }$ for both the two-state SNC filter and the three-state DMC filte r. Although the optimally tuned SNC fil ter approaches the position error RMS performance of the DMC filt er, it is much more sensitive to tuning. DMC achieves very good performance over a much broader, suboptimal range of $\sigma _ { u }$ values than does SNC.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0008_pages_0491-0560/auto/images/2a4347a4a9fd5f4445d0d42e86046bc6b9137c3adc5bfae7f14b2fc759a32db7.jpg)  
Figure F.3.2: RMS Position error as a function of $\sigma _ { u }$ for the two-state SNC and three-state DMC filters.

This is a significant advantage for DMC applications where the true state values are not available to guide the tuning effort, as they are in a simulation study, and the precisely optimal tuning parameter values are not known.

Aside from this, the DMC filter also provides a direct estimate of the unknown, unmodeled acceleration. This information could, in turn, be useful in improving the filter dynamic model. Figure F.3.3 is a plot of the estimated and true sinusoidal accelerations. This plot shows excellent agreement between the estimated and true accelerations; their correlation coefficient is 0.9306.

# F.4 REFERENCE

Maybeck, P. S., Stochastic Models, Estimation and Control, Vol. 1, Academic Press, 1979.

![](../chunks/Statistical Orbit Determination (Byron Tapley, Bob Schutz, George H. Born) (z-library.sk,_part_0008_pages_0491-0560/auto/images/7bfae3b384cb1cd49da689312e9faa6718957e69fb58f21211d785763e5e0b76.jpg)  
Figure F.3.3: Estimated and true sinusoidal accelerations.

Appendix G

# Solution of the Linearized Equations of Motion

# G.1 INTRODUCTION

The equations of motion for a satellite are given by:

$$
\begin{array} { r } { \dot { \mathbf { X } } = F ( \mathbf { X } , t ) , } \end{array}
$$

where

$$
\mathbf { X } = [ X Y Z \dot { X } \dot { Y } \dot { Z } \beta ] ^ { T } .
$$

$\mathbf { X }$ is the state vector containing six position and velocity elements and $\beta$ , an $m$ vector, represents all constant parameters such as gravity and drag coeffic ients that are to be solved for. Hence, $\mathbf { X }$ is a vector of dimension $n = m + 6$ .

Equation (G.1.1) can be linearized by expanding about a reference state vector denoted by $\mathbf { X } ^ { * }$ ,

$$
\dot { \mathbf { X } } ( t ) = \dot { \mathbf { X } } ^ { * } ( t ) + \left[ \frac { \partial \dot { \mathbf { X } } ( t ) } { \partial \mathbf { X } ( t ) } \right] ^ { * } \left( \mathbf { X } ( t ) - \mathbf { X } ^ { * } ( t ) \right) + \mathrm { h . o . t . }
$$

The $^ *$ indicates that the quantity is evaluated on the reference state. By ignoring higher-order terms (h.o.t.) and defining

$$
\mathbf { x } ( t ) \equiv \mathbf { X } ( t ) - \mathbf { X } ^ { * } ( t ) ,
$$

we can write Eq. (G.1.2) as

$$
\dot { \mathbf { x } } ( t ) = \left[ \frac { \partial \dot { \mathbf { X } } ( t ) } { \partial \mathbf { X } ( t ) } \right] ^ { * } \mathbf { x } ( t ) .
$$

Define

$$
A ( t ) \equiv \left[ \frac { \partial \dot { \bf X } ( t ) } { \partial { \bf X } ( t ) } \right] ^ { * } ,
$$

then

$$
\dot { \mathbf { x } } ( t ) = \boldsymbol { A } ( t ) \mathbf { x } ( t ) .
$$

Equation (G.1.5) is a linear system of first -order differential equations with $A ( t )$ being an $n \times n$ time varying matrix evaluated on the known reference state $\mathbf { X } ^ { * } ( t )$ . Note that $\dot { \boldsymbol { { \beta } } } = 0$ , so that

$$
\frac { \partial \dot { \boldsymbol { \beta } } } { \partial \mathbf { X } ( t ) } = 0 .
$$

Because Eq. (G.1.4) is linear† and of the form

$$
\dot { \mathbf { x } } ( t ) = A ( t ) \mathbf { x } ( t ) ,
$$

the solution can be written as

$$
{ \bf x } ( t ) = \frac { \partial { \bf x } ( t ) } { \partial { \bf x } _ { 0 } } { \bf x } _ { 0 } .
$$

It is also true that

$$
\mathbf { x } ( t ) = \frac { \partial \mathbf { X } ( t ) } { \partial \mathbf { X } _ { 0 } } \mathbf { x } _ { 0 } .
$$

This follows from the fact that the reference state does not vary in this operation,

$$
\begin{array} { c } { \displaystyle \frac { \partial \mathbf { x } ( t ) } { \partial \mathbf { x } _ { 0 } } = \frac { \partial \left( \mathbf { X } ( t ) - \mathbf { X } ^ { * } ( t ) \right) } { \partial ( \mathbf { X } _ { 0 } - \mathbf { X } _ { 0 } ^ { * } ) } } \\ { \displaystyle = \frac { \partial \mathbf { X } ( t ) } { \partial \mathbf { X } _ { 0 } } . } \end{array}
$$

The conditions under which Eq. (G.1.6) satisfies Eq. (G.1.4) are demonstrated as follows. First define

$$
\Phi ( t , t _ { 0 } ) \equiv \frac { \partial { \bf X } ( t ) } { \partial { \bf X } _ { 0 } } .
$$

Then Eq. (G.1.6) can be written as

$$
\begin{array} { r } { { \bf x } ( t ) = \Phi ( t , t _ { 0 } ) { \bf x } _ { 0 } . } \end{array}
$$

Differentiating Eq. (G.1.8) yields

$$
\dot { { \bf x } } ( t ) = \dot { \Phi } ( t , t _ { 0 } ) { \bf x } _ { 0 } .
$$

Equating Eq. (G.1.4) and Eq. (G.1.9) yields

$$
\frac { \partial \dot { \mathbf { X } } ( t ) } { \partial \mathbf { X } ( t ) } \mathbf { x } ( t ) = \dot { \Phi } ( t , t _ { 0 } ) \mathbf { x } _ { 0 } .
$$

Substituting Eq. (G.1.8) for ${ \bf x } ( t )$ into Eq. (G.1.10) results in

$$
\left[ \frac { \partial \dot { \mathbf { X } } ( t ) } { \partial \mathbf { X } ( t ) } \right] ^ { * } \Phi ( t , t _ { 0 } ) \mathbf { x } _ { 0 } = \dot { \Phi } ( t , t _ { 0 } ) \mathbf { x } _ { 0 } .
$$

Equating the coefficie nts of $\mathbf { x } _ { \mathrm { 0 } }$ in this equation yields the differential equation for $\dot { \Phi } ( t , t _ { 0 } )$ ,

$$
\dot { \Phi } ( t , t _ { 0 } ) = A ( t ) \Phi ( t , t _ { 0 } ) ,
$$

with initial conditions

$$
\Phi ( t _ { 0 } , t _ { 0 } ) = I .
$$

The matrix $\Phi ( t , t _ { 0 } )$ is referred to as the State Transition Matrix. Whenever Eqs. (G.1.11) and (G.1.12) are satisfied, the solution to $\dot { \mathbf { x } } ( t ) = A ( t ) \mathbf { x } ( t )$ is given by Eq. (G.1.8).

# G.2 THE STATE TRANSITION MATRIX

Insight into the $n \times n$ state transition matrix can be obtained as follows. Let

$$
\Phi ( t , t _ { 0 } ) \equiv \frac { \partial { \bf X } ( t ) } { \partial { \bf X } _ { 0 } } \equiv \left[ \begin{array} { l } { \phi _ { 1 } ( t , t _ { 0 } ) } \\ { \phi _ { 2 } ( t , t _ { 0 } ) } \\ { \phi _ { 3 } ( t , t _ { 0 } ) } \end{array} \right] = \left[ \begin{array} { l } { \frac { \partial { \bf r } ( t ) } { \partial { \bf X } _ { 0 } } } \\ { \frac { \partial { \bf r } ( t ) } { \partial { \bf X } _ { 0 } } } \\ { \frac { \partial \beta ( t ) } { \partial { \bf X } _ { 0 } } } \end{array} \right] .
$$

Note that $\phi _ { 3 } ( t , t _ { 0 } )$ is an $m \times n$ matrix of constants partitioned into an $m \times 6$ matrix of zeros on the left and an $m \times m$ identity matrix on the right, where $m$ is the dimension of $\beta$ and $\mathbf { X }$ is of dimension $n$ . Because of this, it is only necessary to solve the upper $6 \times n$ portion of Eq. (G.1.11).

Equation (G.1.11) also can be written in terms of a second-order differential equation. This can be shown by differentiating Eq. (G.2.1):

$$
{ \dot { \Phi } } ( t , t _ { 0 } ) = { \frac { { \partial } { \dot { \mathbf { X } } } ( t ) } { { \partial } { \mathbf { X } } _ { 0 } } } = \left[ { \dot { \phi } } _ { 1 } ( t , t _ { 0 } ) \right] = \left[ \begin{array} { c } { \frac { { \partial } { \dot { \mathbf { r } } } ( t ) } { { \partial } { \mathbf { X } } _ { 0 } } } \\ { \frac { { \partial } { \dot { \mathbf { r } } } ( t ) } { { \partial } { \mathbf { X } } _ { 0 } } } \\ { { \dot { \phi } } _ { 3 } ( t , t _ { 0 } ) \end{array} } \right]
$$

$$
\mathbf { \Gamma } = \left[ \begin{array} { c } { \frac { \partial \dot { \mathbf { r } } ( t ) } { \partial \mathbf { X } ( t ) } } \\ { \frac { \partial \ddot { \mathbf { r } } ( t ) } { \partial \mathbf { X } ( t ) } } \\ { 0 } \end{array} \right] _ { n \times n } \left[ \frac { \partial \mathbf { X } ( t ) } { \partial \mathbf { X } _ { 0 } } \right] _ { n \times n } .
$$

In these equations, 0 represents an $m \times n$ null matrix. Notice from the first of Eq. (G.2.2) that

$$
\ddot { \phi } _ { 1 } = \frac { \partial \ddot { \bf r } } { \partial { \bf X } _ { 0 } } = \dot { \phi } _ { 2 } .
$$

Hence, we could solve this second-order system of differential equations to obtain $\Phi ( t , t _ { 0 } )$ ,

$$
\begin{array} { l } { \displaystyle { \ddot { \phi } } _ { 1 } ( t , t _ { 0 } ) = \frac { \partial \ddot { \bf r } ( t ) } { \partial { \bf X } _ { 0 } } = \frac { \partial \ddot { \bf r } ( t ) } { \partial { \bf X } ( t ) } \ \frac { \partial { \bf X } ( t ) } { \partial { \bf X } _ { 0 } } \qquad } \\ { \displaystyle = \left[ \frac { \partial \ddot { \bf r } ( t ) } { \partial { \bf r } ( t ) } \frac { \partial \ddot { \bf r } ( t ) } { \partial \dot { \bf r } ( t ) } \frac { \partial \ddot { \bf r } ( t ) } { \partial \beta } \right] _ { 3 \times n } \left[ \frac { \partial \dot { \bf r } ( t ) } { \partial { \bf X } _ { 0 } } \right] _ { n \times n } } \end{array}
$$

or

$$
\ddot { \phi } _ { 1 } ( t , t _ { 0 } ) = \frac { { \partial } \ddot { \bf r } ( t ) } { { \partial } { \bf r } ( t ) } \phi _ { 1 } ( t , t _ { 0 } ) + \frac { { \partial } \ddot { \bf r } ( t ) } { { \partial } \dot { \bf r } ( t ) } \dot { \phi } _ { 1 } ( t , t _ { 0 } ) + \frac { { \partial } \ddot { \bf r } ( t ) } { { \partial } \beta } \phi _ { 3 } ( t , t _ { 0 } ) .
$$

With initial conditions

$$
\begin{array} { r l } & { \phi _ { 1 } ( t _ { 0 } , t _ { 0 } ) = \left[ [ I ] _ { 3 \times 3 } [ 0 ] _ { 3 \times ( n - 3 ) } \right] } \\ & { \dot { \phi } _ { 1 } ( t _ { 0 } , t _ { 0 } ) = \phi _ { 2 } ( t _ { 0 } , t _ { 0 } ) = [ [ 0 ] _ { 3 \times 3 } [ I ] _ { 3 \times 3 } [ 0 ] _ { 3 \times m } ] \ . } \end{array}
$$

We could solve Eq. (G.2.5), a $3 \times n$ system of second-order differential equations, instead of the $6 \times n$ first-orde r system given by Eq. (G.2.2). Recall that the partial derivatives are evaluated on the reference state and that the solution of the $m \times n$ system represented by $\dot { \phi } _ { 3 } ( t , t _ { 0 } ) = 0$ is trivial,

$$
\phi _ { 3 } ( t , t _ { 0 } ) = [ [ 0 ] _ { m \times 6 } [ I ] _ { m \times m } ] .
$$

In solving Eq. (G.2.5) we could write it as a system of $n \times n$ first-order equations,

$$
\begin{array} { r l } & { \dot { \phi } _ { 1 } ( t , t _ { 0 } ) = \phi _ { 2 } ( t , t _ { 0 } ) } \\ & { \dot { \phi } _ { 2 } ( t , t _ { 0 } ) = \frac { \partial \ddot { \bf r } ( t ) } { \partial { \bf r } ( t ) } \phi _ { 1 } ( t , t _ { 0 } ) + \frac { \partial \ddot { \bf r } ( t ) } { \partial \dot { \bf r } ( t ) } \phi _ { 2 } ( t , t _ { 0 } ) + \frac { \partial \ddot { \bf r } ( t ) } { \partial \beta } \phi _ { 3 } ( t , t _ { 0 } ) } \\ & { \dot { \phi } _ { 3 } ( t , t _ { 0 } ) = 0 . } \end{array}
$$

It is easily shown that Eq. (G.2.6) is identical to Eq. (G.1.11),

$$
\left[ \begin{array} { c } { \dot { \phi } _ { 1 } ( t , t _ { 0 } ) } \\ { \dot { \phi } _ { 2 } ( t , t _ { 0 } ) } \\ { \dot { \phi } _ { 3 } ( t , t _ { 0 } ) } \end{array} \right] _ { n \times n } = \left[ \begin{array} { c c } { [ 0 ] _ { 3 \times 3 } } & { [ I ] _ { 3 \times 3 } } & { [ 0 ] _ { 3 \times m } } \\ { \left[ \frac { \partial \vec { \bf r } ( t ) } { \partial { \bf r } ( t ) } \right] _ { 3 \times 3 } \left[ \frac { \partial \vec { \bf r } ( t ) } { \partial \dot { \bf r } ( t ) } \right] _ { 3 \times 3 } \left[ \frac { \partial \vec { \bf r } ( t ) } { \partial \beta } \right] _ { 3 \times m } } \\ { [ 0 ] _ { m \times 3 } } & { [ 0 ] _ { m \times 3 } } & { [ 0 ] _ { m \times m } } \end{array} \right] _ { n \times n } ^ { * } \left[ \begin{array} { c } { \phi _ { 1 } ( t , t _ { 0 } ) } \\ { \phi _ { 2 } ( t , t _ { 0 } ) } \\ { \phi _ { 3 } ( t , t _ { 0 } ) } \end{array} \right] _ { n \times n }
$$

or

$$
{ \dot { \Phi } } ( t , t _ { 0 } ) = A ( t ) \Phi ( t , t _ { 0 } ) .
$$

Appendix H

# Transformation between ECI and ECF Coordinates

# H.1 INTRODUCTION

The transformation between ECI and ECF coordinates is defined by Eq. (2.

$$
T _ { X Y Z } ^ { x y z } = T _ { \mathrm { E C I } } ^ { \mathrm { E C F } } = W S ^ { \prime } N P .
$$

The transformation matrices W, $S ^ { \prime }$ , N, and $\mathrm { \bf P }$ account for the following effects:

$W =$ the offset of the Earth’s angular velocity vector with respect to the $z$ axis of the ECF (see Section 2.4.2)   
$S ^ { \prime } =$ the rotation of the ECF about the angular velocity vector (see Sections 2.3.3 and 2.4.2)   
$N =$ the nutation of the ECF with respect to the ECI (see Section 2.4.1)   
$P =$ the precession of the ECF with respect to the ECI (see Section 2.4.1).

The ECI and ECF systems have fundamental characteristics described in Chapter 2. The realization of these reference systems in modern space applications is usually through the International Celestial Reference Frame (ICRF) for the ECI and the International Terrestrial Reference Frame (ITRF) for the ECF. These realizations infer certain characteristics for highest accuracy and consistency. For example, the ICRF is defined using the coordinates of extragalactic radio sources, known as quasars, where the coordinates are derived from observations obtained on the surface of the Earth with a set of large antennas known as the Very Long Baseline Interferometry (VLBI) network. The coordinates of the quasars are then linked with visible sources to an optical star catalog and the coordinates of the celestial bodies in the solar system. In a similar manner, the ITRF is realized with ground networks of SLR, LLR, GPS, and DORIS (see Chapter 3), which establish the center of mass origin of the ITRF, as well as the reference meridian.

The following sections summarize the content of the matrices required for the transformation from an ECI system to an ECF system. This discussion follows the classical formulation and it will be assumed that the ECI is realized through J2000, which is not precisely the same as the actual ICRF adopted by the International Astronomical Union. If observed values of polar motion $( x _ { p } , y _ { p } )$ and $\Delta ( \mathrm { U T 1 } )$ are used, the transformation matrix has an accuracy of better than one arc-sec. The satellite motion is especially sensitive to polar motion and the rate of change in UT1, which is related to length of day. This sensitivity enables the estimation of these parameters from satellite observations.

The International Earth Rotation Service (IERS) distributes Earth Orientation Parameters (EOP) derived from VLBI and satellite observations. The main EOP are $( x _ { p } , y _ { p } )$ , $\Delta ( \mathrm { U T } 1 )$ and corrections to the precession and nutation parameters. These parameters are empirical corrections derived from satellite and VLBI observations which account for changes resulting from tides and atmospheric effects, for example. The EOP are regularly distributed by the IERS as Bulletin B. Consult the IERS publications and web page for additional information. As the models adopted by the IERS are improved, they are documented in new releases of the IERS Standards (or “Con ventions”).

For the most part, the following discussion follows Seidelmann (1992) and McCarthy (1996). A comprehensive summary is given by Seeber (1993). A comparison of different implementations of the matrices, including a detailed review of the transformations, has been prepared by Webb (2002).

# H.2 MATRIX $P$

For this discussion, P represents the transformation from J2000 to a mean-ofdate system. If is a function of the precession of the equinoxes (see Section 2.4.1). The transformation matrix is dependent on three angles and is given by (where C represents cosine and S denotes sine):

P =

and the precession angles are given by

$$
\begin{array} { l } { \zeta _ { A } = 2 3 0 6 \prime \prime 2 1 8 1 t + 0 \prime \prime 3 0 1 8 8 t ^ { 2 } + 0 \prime \prime 0 1 7 9 9 8 t ^ { 3 } } \\ { \theta _ { A } = 2 0 0 4 \prime 3 1 0 9 t - 0 \prime \prime 4 2 6 6 5 t ^ { 2 } - 0 \prime \prime 0 4 1 8 3 3 t ^ { 3 } } \\ { z _ { A } = 2 3 0 6 \prime \prime 2 1 8 1 t + 1 \prime 0 9 4 6 8 t ^ { 2 } + 0 \prime \prime 0 1 8 2 0 3 t ^ { 3 } } \end{array}
$$

with $t$ defined as

$$
t = { \frac { [ T T - J 2 0 0 0 . 0 ] ( \mathrm { { d a y s } } ) } { 3 6 5 2 5 } } .
$$

In Eq. H.2.3, J2000.0 is January 1, 2000, 12:00 in TT, or JD 2451545.0. These equations are based on the work of Lieske, et al. (1977). Terrestrial Time (TT) is defined in Section 2.4.2.

# H.3 MATRIX $N$

The transformation from a mean-of-date system to a true-of-date system is dependent on the nutations (see Section 2.4.1). Four angles are used: the mean obliquity of the ecliptic $( \epsilon _ { m } )$ , the true obliquity of the ecliptic $\left( \epsilon _ { t } \right)$ , the nutation in longitude $( \Delta \psi )$ , and the nutation in obliquity $( \Delta \epsilon )$ . The matrix $_ \mathrm { N }$ is given by

$$
\left[ \begin{array} { l l l } { \mathbf { C } \Delta \boldsymbol { \psi } } & { - \mathbf { C } \epsilon _ { m } \mathbf { S } \Delta \boldsymbol { \psi } } & { - \boldsymbol { \mathrm { S } } \epsilon _ { m } \boldsymbol { \mathrm { S } } \Delta \boldsymbol { \psi } } \\ { \mathbf { C } \epsilon _ { t } \mathbf { S } \Delta \boldsymbol { \psi } } & { \mathbf { C } \epsilon _ { m } \mathbf { C } \epsilon _ { t } \mathbf { C } \Delta \boldsymbol { \psi } + \mathbf { S } \epsilon _ { m } \mathbf { S } \epsilon _ { t } } & { \quad \mathrm { S } \epsilon _ { m } \mathbf { C } \epsilon _ { t } \mathbf { C } \Delta \boldsymbol { \psi } - \mathbf { C } \epsilon _ { m } \mathbf { S } \epsilon _ { t } } \\ { \mathbf { S } \epsilon _ { t } \mathbf { S } \Delta \boldsymbol { \psi } } & { \mathbf { C } \epsilon _ { m } \mathbf { S } \epsilon _ { t } \mathbf { C } \Delta \boldsymbol { \psi } - \mathbf { S } \epsilon _ { m } \mathbf { C } \epsilon _ { t } } & { \quad \mathrm { S } \epsilon _ { m } \mathbf { S } \epsilon _ { t } \mathbf { C } \Delta \boldsymbol { \psi } + \mathbf { C } \epsilon _ { m } \mathbf { C } \epsilon _ { t } } \end{array} \right] ,
$$

where the mean obliquity is

$$
\epsilon _ { m } = 8 4 3 8 1 ^ { \prime \prime } 4 4 8 - 4 6 ^ { \prime \prime } 8 1 5 0 t - 0 ^ { \prime \prime } 0 0 0 5 9 t ^ { 2 } + 0 ^ { \prime \prime } 0 0 1 8 1 3 t ^ { 3 }
$$

and the true obliquity is

$$
\epsilon _ { t } = \epsilon _ { m } + \Delta \epsilon .
$$

The expression for the nutation in longitude and in obliquity is given by Mc-Carthy (1996), for example. The IAU 1980 theory of nutation is readily available in a convenient Chebychev polynomial approximation with the planetary ephemerides (Standish, et al., 1997). Corrections to the adopted series, based on observations, are provided by the IERS in Bulletin B.

# H.4 MATRIX $S ^ { \prime }$

The true-of-date rotation to a pseudo-body-fix ed system accounts for the ‘spin’ of the Earth. This diurnal rotation depends on a single angle $\alpha _ { G }$ , which is referred

to as the Greenwich Mean Sidereal Time (GMST). The matrix $S ^ { \prime }$ is identical to Eq. 2.3.20; namely,

$$
\begin{array} { r } { S ^ { \prime } = \left[ \begin{array} { c c c } { \mathrm { C } \alpha _ { G } } & { \mathrm { S } \alpha _ { G } } & { 0 } \\ { - \mathrm { S } \alpha _ { G } } & { \mathrm { C } \alpha _ { G } } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] . } \end{array}
$$

In some cases, especially when a satellite velocity vector with respect to the rotating ECF is required, the time derivative of the time-dependent elements of each of the transformation matrices will be needed. However, the time derivative of $S ^ { \prime }$ is particularly significant since the angle $\alpha _ { G }$ is the fastest changing variable in the matrices P, N, $S ^ { \prime }$ and W. The time derivative of $S ^ { \prime }$ is

$$
\dot { S } ^ { \prime } = \dot { \alpha } _ { G } \left[ \begin{array} { c c c } { - \mathrm { S } \alpha _ { G } } & { \mathrm { C } \alpha _ { G } } & { 0 } \\ { - \mathrm { C } \alpha _ { G } } & { - \mathrm { S } \alpha _ { G } } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right]
$$

where $\dot { \alpha } _ { G }$ is the rotation rate of the Earth. For some applications, this rate can be taken to be constant, but for high-accuracy applications the variability in this rate must be accounted for. According to the IERS, the average rate is $\mathrm { 7 . 2 9 2 1 1 5 1 4 6 7 0 6 4 \times 1 0 ^ { - 5 } r a d / s }$ , but this value should be adjusted using IERS Bulletin B to account for variations. The GMST for a given UT1 $( \mathrm { U T C } + \Delta ( \mathrm { U T 1 } ) )$ can be found from Kaplan, et al. (1981), modified to provide the result in radians:

$$
\begin{array} { r l } { \mathrm { G M S T ( U T 1 ) } = 4 . 8 9 4 9 6 1 2 1 2 8 2 3 0 5 8 7 5 1 3 7 5 7 0 4 4 3 0 } & { { } { \mathrm { ( H } } } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad + \Delta T \Bigl \{ 6 . 3 0 0 3 8 8 0 9 8 9 8 4 8 9 3 5 5 2 2 7 6 5 1 3 7 2 0 } & { } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ { \quad \quad \quad \quad \quad \quad + \Delta T \Bigl ( 5 . 0 7 5 2 0 9 9 9 4 1 1 3 5 9 1 4 7 8 0 5 3 8 0 5 5 2 3 \times 1 0 ^ { - 1 5 } } \\ { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad - 9 . 2 5 3 0 9 7 5 6 8 1 9 4 3 3 5 6 4 0 0 6 7 1 9 0 6 8 8 \times 1 0 ^ { - 2 4 } \Delta T \Bigr ) \Bigr \} } \end{array}
$$

where $\Delta T = \mathrm { U T 1 } - \mathrm { J 2 0 0 0 . 0 }$ , and where $\Delta T$ is in days, including the fractional part of a day.

An additional correction known as the equation of the equinoxes must be applied. For highest accuracy, additional terms amounting to a few milli-arc-sec amplitude should be applied (see McCarthy, 1996; or Simon, et al., 1994) . With the equation of the equinoxes, the angle $\alpha _ { G }$ becomes

$$
\alpha _ { G } = \mathrm { G M S T } ( \mathrm { U T 1 } ) + \Delta \psi \cos \epsilon _ { m } .
$$

# H.5 MATRIX W

The pseudo-body-fix ed system is aligned with the instantaneous pole, equator and reference meridian of the Earth. As noted in Section 2.4.2, the Earth’s spin axis is not fix ed in the Earth and two angles $( x _ { p } , y _ { p } )$ are used to describe the spin axis location with respect to an adopted ECF, such as an ITRF. Because of the small magnitude of the polar motion angles, the transformation matrix W can be represented by

$$
T _ { \mathrm { P B F } } ^ { \mathrm { B F } } = W = \left[ \begin{array} { c c c } { 1 } & { 0 } & { x _ { p } } \\ { 0 } & { 1 } & { - y _ { p } } \\ { - x _ { p } } & { y _ { p } } & { 1 } \end{array} \right] ,
$$

where the polar motion angles are expressed in radians. The angles are available in IERS Bulletin B, for example.

# H.6 REFERENCES

Aoki, S., and H. Kinoshita, “Note on the relation between the equinox and Guinot’s non-rotating origin,” Celest. Mech., Vol. 29, No. 4, pp. 335–360, 1983.

Kaplan, G. H. (ed.), The IAU Resolutions on astronomical constants, time scales, and the fundamental reference frame, USNO Circular No. 163, U.S. Naval Observatory, 1981.

Lambeck, K., Geophysical Geodesy, Clarendon Press, Oxford, 1988.

Lieske, J. H., T. Lederle, W. Fricke, and B. Morando, “Expressions for the precession quantities based upon the IAU (1976) System of Astronomical Constants,” Astronomy and Astrophysics, Vol. 58, pp. 1–16, 1977.

McCarthy, D. (ed.), IERS Conventions (1996), IERS Technical Note 21, International Earth Rotation Service, Observatoire de Paris, July 1996.

Seeber, G., Satellite Geodesy: Foundations, Methods & Applications, Walter deGruyter, New York, 1993.

Seidelmann, P. K., “1980 IAU Nutation: The Final Report of the IAU Working Group on Nutation,” Celest. Mech., Vol. 27, No. 1, pp. 79–106, 1982.

Seidelmann, P. K., Explanatory Supplement to the Astronautical Almanac, University Science Books, Mill Valley, CA, 1992.

Simon, J. L., P. Bretagnon, J. Chapront, M. Chapront-Touze, G. Francou, J. ´ Laskar, “Numerical expressions for precession formulae and mean elements for the Moon and planets,” Astronomy and Astrophysics, Vol. 282, pp. 663–683, 1994.   
Standish, E. M., X. Newhall, J. Williams, and W. Folkner, JPL Planetary and Lunar Ephemerides (CD-ROM), Willmann-Bell, Inc. Richmond, 1997.   
Webb, C.,The ICRF-ITRF Transformation: A Comparison of Fundamental Earth Orientation Models found in MSODP and CALC, The University of Texas at Austin, Center for Space Research Report CSR-02-01, Austin, TX, 2002.

# Bibliography Abbreviations

Adv. Space Res.   
AIAA   
AIAA J.   
ASME   
Astron. J.   
Celest. Mech.   
Geophys. J. Royal Astronom. Soc. Geophys. Res. Ltrs.   
IEEE J. Appl. Math.   
J. Assoc. Comput. Mach.   
J. Astronaut. Sci.   
J. Basic Engr.   
J. Geophys. Res.   
J. Guid. Cont.   
J. Guid. Cont. Dyn.   
J. Inst. Math. Applic.   
Advances in Space Research   
American Institute of Aeronautics and Astronautic   
AIAA Journal   
American Society of Mechanical Engineers   
Astronomical Journal   
Celestial Mechanics and Dynamical Astronomy   
Geophysical Journal of the Royal Astronomical Society   
Geophysical Research Letters   
Institute for Electrical and Electronics Engineers   
Journal of Applied Mathematics   
Journal of the Association of Computing Machiner   
Journal of the Astronautical Sciences   
ASME Journal of Basic Engineering   
Journal of Geophysical Research   
Journal of Guidance and Control   
Journal of Guidance, Control, and Dynamics   
Journal of the Institute of Mathematics and Its Applications   
Journal of the Insitute of Navigation   
Journal of Optimization Theory and Applications   
Journal of Spacecraft and Rockets   
Society for Industrial and Applied Mathematics   
International Society for Optical Engineering   
IEEE Transactions on Automatic Control J. ION   
J. Optim. Theory Appl. J. Spacecr. Rockets   
SIAM   
SPIE   
Trans. Auto. Cont.

# Bibliography

[1] Aoki, S., and H. Kinoshita, “Note on the relation between the equinox and Guinot’s non-rotating origin,” Celest. Mech., Vol. 29, No. 4, pp. 335–360, 1983.

[2] Ashby, N., “Relati vity and the Global Positioning System,” Physics Today, Vol. 55, No. 5, pp. 41–47, May 2002.

[3] Barlier, F., C. Berger, J. Falin, G. Kockarts, and G. Thuiller, “A thermospheric model based on satellite drag data,” Annales de Geophysique ´ , Vol. 34, No. 1, pp. 9–24, 1978.

[4] Battin, R., An Introduction to the Mathematics and Methods of Astrodynamics, American Institute of Aeronautics and Astronautics, Reston, VA, 1999.

[5] Bertiger, W., Y. Bar-Sever, E. Christensen, E. Davis, J. Guinn, B. Haines, R. Ibanez-Meier, J. Jee, S. Lichten, W. Melbourne, R. Muellerschoen, T. Munson, Y. Vigue, S. Wu, T. Yunck, B. Schutz, P. Abusali, H. Rim, W. Watkins, and P. Willis , “GPS precise tracking of TOPEX/Poseidon: Results and implications,” J. Geophys. Res., Vol. 99, No. C12, pp. 24,449– 24,462, December 15, 1995.

[6] Beutler, G., E. Brockmann, W. Gurtner, U. Hugentobler, L. Mervart, M. Rothacher, and A. Verdun, “Extended orbit modeling techniques at the CODE Processing Center of the International GPS Service for Geodynamics (IGS): theory and initial results,” Manuscripta Geodaetica, Vol. 19, No. 6, pp. 367–385, April 1994.

[7] Bierman, G. J., Factorization Methods for Discrete Sequential Estimation, Academic Press, New York, 1977.

[8] Bjorck, A., ¨ Numerical Methods for Least Squares Problems, SIAM, Philadelphia, PA, 1996.

[9] Bond, V., and M. Allman, Modern Astrodynamics, Princeton University Press, Princeton, NJ, 1996.

[10] Born, G. H., D. B. Goldstein, and B. Thompson, “An Analytical Theory for Orbit Determination”, J. Astronaut. Sci., Vol. 49, No. 2, pp. 345–361, April–June 2001.

[11] Born, G., J. Mitchell, and G. Hegler, “GEOSAT ERM – mission design,” J. Astronaut. Sci., Vol. 35, No. 2, pp. 119–134, April–June 1987.

[12] Born, G. H., B. D. Tapley, and M. L. Santee, “Orbit determination using dual crossing arc altimetry,” Acta Astronautica, Vol. 13, No. 4, pp. 157– 163, 1986.

[13] Boucher, C., Z. Altamini, and P. Sillard, The International Terrestrial Reference Frame (ITRF97), IERS Technical Note 27, International Earth Rotation Service, Observatoire de Paris, May 1999.

[14] Brouwer, D., “Sol utions of the problem of artificial satellite theory without drag,” Astron. J., Vol. 64, No. 9, pp. 378–397, November 1959.

[15] Brouwer, D., and G. Clemence, Methods of Celestial Mechanics, Academic Press, New York, 1961.

[16] Bryson, A. E., and Y. C. Ho, Applied Optimal Control, Hemisphere Publishing Corp., Washington, DC, 1975.

[17] Bucy, R., and P. Joseph, Filtering for Stochastic Processes, John Wiley & Sons, Inc., New York, 1968.

[18] Cajori, F., A History of Mathematics, MacMillan Co., New York, 1919.

[19] Carlson, N. A., “F ast triangular formulation of the square root fil ter”, AIAA J., Vol. 11, No. 9, pp. 1239-1265, September 1973.

[20] Chobotov, V. (ed.), Orbital Mechanics, American Institute of Aeronautics and Astronautics, Inc., Reston, VA, 1996.

[21] Christensen, E., B. Haines, K. C. McColl, and R. S. Nerem, “Observ ations of geographically correlated orbit errors for TOPEX/Poseidon using the Global Positioning System,” Geophys. Res. Ltrs., Vol. 21, No. 19, pp. 2175–2178, September 15, 1994.

[22] Cook, G. E., “Perturbati ons of near-circular orbits by the Earth’s gravitational potential,” Planetary and Space Science, Vol. 14, No. 5, pp. 433– 444, May 1966.

[36] El´Yasberg, P. E., Introduction to the Theory of Flight of Artifici al Earth Satellites, translated from Russian, Israel Program for Scientific Translations, 1967.

[37] Fisher, R. A., “On an absolute criteria for fitti ng frequency curves,” Mess. Math., Vol. 41, pp. 155–160, 1912.

[38] Fliegel, H., T. Gallini, and E. Swift, “Global Positioning System radiation force models for geodetic applications”, J. Geophys. Res., Vol. 97, No. B1, pp. 559–568, January 10, 1992.

[39] Freeman, H., Introduction to Statistical Inference, Addison-Wesley, 1963.

[40] Gauss, K. F., Theoria Motus Corporum Coelestium, 1809 (Translated into English: Davis, C. H., Theory of the Motion of the Heavenly Bodies Moving about the Sun in Conic Sections, Dover, New York, 1963).

[41] Gelb, A. (ed.), Applied Optimal Estimation, Massachusetts Institute of Technology Press, Cambridge, MA, 1974.

[42] Gentleman, W. M., “Lea st squares computations by Givens transformations without square roots,” J. Inst. Math. Applic., Vol. 12, pp. 329–336, 1973.

[43] Givens, W., “Computa tion of plane unitary rotations transforming a general matrix to triangular form,” J. Appl. Math., Vol. 6, pp. 26–50, 1958.

[44] Goldstein, D. B., G. H. Born, and P. Axelrad, “Real-time, autonomous, precise orbit determination using GPS,” J. ION, Vol. 48, No. 3, pp. 169– 179, Fall 2001.

[45] Golub, G. H., and C. F. Van Loan, Matrix Computations, Johns Hopkins University Press, 1996.

[46] Goodyear, W. H., “Complet ely general closed form solution for coordinates and partial derivatives of the two-body problem,” Astron. J., Vol. 70, No. 3, pp. 189–192, April 1965.

[47] Graybill, F. A., An Introduction to Linear Statistical Models, McGraw-Hill, New York, 1961.

[48] Grewal, M. S., and A. P. Andrews, Kalman Filtering: Theory and Practice, Prentice Hall, 1993.

[49] Gruber, T., A. Bode, C. Reigber, P. Schwintzer, G. Balmino, R. Biancale, J. Lemoine, “GRIM5- C1: Combination solution of the global gravity field to degree and order 120,” Geophys. Res. Ltrs., Vol. 27, No. 24, pp. 4005– 4008, December 2000.

[50] Heffes, H., “The effects of erroneous models on the Kalman filt er response”, Trans. Auto. Cont., Vol. AC-11, pp. 541–543, July 1966.

[51] Heiskanen, W., and H. Moritz, Physical Geodesy, W. H. Freeman and Co., San Francisco, 1967.

[52] Helmert, F. R., “Zur Bestimmung kleiner Flachenst ¨ ucke des Geoids aus ¨ Lothabweichungen mit Rucksicht auf Lothkr ¨ ummung”, Sitzungsberichte ¨ Preuss. Akad. Wiss., Berlin, Germany, 1900.

[53] Helstrom, C. W., Probability and Stochastic Processes for Engineers, MacMillan, 1984.

[54] Herring, T., “Model ing atmospheric delays in the analysis of space geodetic data,” in Refraction of Transatmospheric Signals in Geodesy, eds. J. C. DeMunck and T. A. Th. Spoelstra, Netherlands Geodetic Commission Publications in Geodesy, 36, pp. 157-164, 1992.

[55] Herring, T., B. Buffett, P. Mathews, and I. Shapiro, “Free nutations of the Earth: influence of inner core dynamics,” J. Geophys. Res., Vol. 96, No. B5, pp. 8259–8273, May 10, 1991.

[56] Hofmann-Wellenhof, B., H. Lichtenegger, and J. Collins, Global Positioning System: Theory and Practice, Springer-Verlag, Wien-New York, 1997.

[57] Householder, A. S., “Unita ry triangularization of a nonsymmetric matrix,” J. Assoc. Comput. Mach., Vol. 5, No. 4, pp. 339–342, October 1958.

[58] Huang, C., J. C. Ries, B. Tapley, and M. Watkins, “Rela tivistic effects for near-Earth satellite orbit determination,” Celest. Mech., Vol. 48, No. 2, 167-185, 1990.

[59] Ingram, D. S., Orbit determination in the presence of unmodeled accelerations, Ph.D. Dissertation, The University of Texas at Austin, 1970.

[60] Ingram, D. S., and B. D. Tapley, “Lunar orbit determination in the presence of unmodeled accelerations,” Celest. Mech., Vol. 9, No. 2, pp. 191–211, 1974.

[61] Jacchia, L., Thermospheric temperature, density and composition: new models, Special Report 375, Smithsonian Astrophysical Observatory, Cambridge, MA, 1977.

[62] Jazwinski, A. H., Stochastic Process and Filtering Theory, Academic Press, New York, 1970.

[63] Kalman, R. E., “A New Approach to Linear Filtering and Prediction Theory,” J. Basic Eng., Vol. 82, Series E, No. 1, pp. 35–45, March, 1960.

[64] Kalman, R. E. and R. S. Bucy, “Ne w Results in Linear Filtering and Prediction Theory,” J. Basic Eng., Vol. 83, Series D, No. 1, pp. 95–108, March, 1961.

[65] Kaminski, P. G., A. E. Bryson, and S. F. Schmidt, “Discret e square root filteri ng: A survey of current techniques,” Trans. Auto. Cont., Vol. AC-16, No. 6, pp. 727–736, December 1971.

[66] Kaplan, G. H. (ed.), The IAU Resolutions on astronomical constants, time scales, and the fundamental reference frame, USNO Circular No. 163, U.S. Naval Observatory, 1981.

[67] Kaula, W. M., Theory of Satellite Geodesy, Blaisdell Publishing Co., Waltham, 1966 (republished by Dover, New York, 2000).

[68] Kolmogorov, A. N., “Interpolation and Extrapolation of Stationary Random Sequences,” Bulletin of the Academy of Sciences of the USSR Math. Series, Vol. 5, pp. 3–14, 1941.

[69] Kovalevsky, J., I. Mueller, and B. Kolaczek (eds.), Reference Frames in Astronomy and Geophysics, Kluwer Academic Publishers, Dordrecht, 1989.

[70] Kreyszig, E., Advanced Engineering Mathematics, John Wiley & Sons, Inc., New York, 1993.

[71] Lambeck, K., The Earth’s Variable Rotation, Cambridge University Press, Cambridge, 1980.

[72] Lambeck, K., Geophysical Geodesy, Clarendon Press, Oxford, 1988.

[73] Laplace, P. S., Theorie Analytique de Probabilit ´ es´ , Paris, 1812 (The 1814 edition included an introduction, Essai Philosophique sur les Probabilites´ , which has been translated into English: Dale, A. I., Philosophical Essay on Probabilities, Springer-Verlag, New York, 1995).

[74] Lawson, C. L., and R. J. Hanson, Solving Least Squares Problems, Prentice-Hall, Inc. Englewood Cliffs, NJ, 1974 (republished by SIAM, Philadelphia, PA, 1995).

[75] Le Systeme International d’Unites (SI), Bureau International des Poids et Mesures, Sevres, France, 1991.

[76] Legendre, A. M., Nouvelles methodes pour la d ´ etermination des orbites ´ des cometes \` , Paris, 1806.

[77] Leick, A., GPS Satellite Surveying, J. Wiley & Sons, Inc., New York, 2003.

[78] Lemoine, F., S. Kenyon, J. Factor, R. Trimmer, N. Pavlis, D. Chinn, C. Cox, S. Klosko, S. Luthcke, M. Torrence, Y. Wang, R. Williamson, E. Pavlis, R. Rapp, and T. Olson, The development of the Joint NASA GSFC and the National Imagery and Mapping Agency (NIMA) Geopotential Model EGM96, NASA/TP–1998–206861, Greenbelt, MD, July 1998.

[79] Lemoine, F., D. Rowlands, S. Luthcke, N. Zelensky, D. Chinn, D. Pavlis, and G. Marr, “P recise orbit determination of GEOSAT follow-on using satellite laser ranging and intermission altimeter crossovers,” NASA/CP-2001-209986, Flight Mechanics Symposium, John Lynch (ed.), NASA Goddard Space Flight Center, Greenbelt, MD, pp. 377–392, June 2001.

[80] Lichten, S. M., “Es timation and fil tering for high precision GPS positioning applications,” Manuscripta Geodaetica, Vol. 15, pp. 159–176, 1990.

[81] Liebelt, P. B., An Introduction to Optimal Estimation, Addison-Wesley, Reading, MA, 1967.

[82] Lieske, J. H., T. Lederle, W. Fricke, and B. Morando, “Expre ssions for the precession quantities based upon the IAU (1976) System of Astronomical Constants,” Astronomy and Astrophysics, Vol. 58, pp. 1–16, 1977.

[83] Lundberg, J., and B. Schutz, “Recursion formulas of Legendre functions for use with nonsingular geopotential models,” J. Guid. Cont. Dyn., Vol. 11, No. 1, pp. 31–38, January–Fe bruary 1988.

[84] Lutchke, S. B., N. P. Zelenski, D. D. Rowlands, F. G. Lemoine, and T. A. Williams, “The 1-centimeter orbit: Jason-1 precision orbit determination using GPS, SLR, DORIS and altimeter data,” Marine Geodesy, Vol. 26, No. 3-4, pp. 399–421, 2003.

[85] Marini, J. W., and C. W. Murray, “Correction of laser range tracking data for atmospheric refraction at elevations above 10 degrees,” NASA GSFC X591-73-351, Greenbelt, MD, 1973.

[86] Markov, A. A., “The law of large numbers and the method of Least Squares,” (1898), Izbr. Trudi., Izd. Akod. Nauk, USSR, pp. 233-251, 1951.

[87] Marshall, J. A., F. J. Lerch, S. B. Luthcke, R. G. Williamson, and C. Chan, “An Assessment of TDRSS for Precision Orbit Determination,” J. Astonaut. Sci, Vol. 44, No. 1, pp. 115–127, January–March, 1996.

[102] Plummer, H. C., An Introductory Treatise on Dynamical Astronomy, Cambridge University Press, 1918 (republished by Dover Publications, New York, 1966).   
[103] Pollard, H., Mathematical Introduction to Celestial Mechanics, Prentice-Hall, Inc., Englewood Cliffs, NJ, 1966.   
[104] Press, W., B. Flannery, S. Teukolsky, and W. Vetterling, Numerical Recipes, Cambridge University Press, Cambridge, 1986.   
[105] Prussing, J., and B. Conway, Orbit Mechanics, Oxford University Press, New York, 1993.   
[106] Rausch, H. E., F. Tung, and C. T. Striebel, “Maximum likelihood estimates of linear dynamic systems,” AIAA J., Vol. 3, No. 7, pp. 1445–1450, August 1965.   
[107] Reddy, J. N., and M. L. Rasmussen, Advanced Engineering Analysis, Robert E. Krieger Publishing Co., Malabar, FL 1990.   
[108] Ries, J. C., C. Huang, M. M. Watkins, and B. D. Tapley, “Orbit determination in the relativistic geocentric reference frame,” J. Astronaut. Sci., Vol. 39, No. 2, pp. 173–181, April–J une 1991.   
[109] Ries, J. C., C. K. Shum, and B. Tapley, “Surf ace force modeling for precision orbit determination,” Geophysical Monograph Series, Vol. 73, A. Jones (ed.), American Geophysical Union, Washington, DC, 1993.   
[110] Rowlands, D. D., S. B. Luthcke, J. A. Marshall, C. M. Cox, R. G. Williamson, and S. C. Rowton, “Space Shuttle precision orbit determination in support of SLA-1 using TDRSS and GPS tracking data,” J. Astronaut. Sci., Vol. 45, No. 1, pp. 113–129, January–March 1997.   
[111] Roy, A. E., Orbital Motion, John Wiley & Sons Inc., New York, 1988.   
[112] Saastamoinen, J., “Atmospheric correction for the troposphere and stratosphere in radio ranging of satellites,” Geophysical Monograph Series, Vol. 15, S. Henriksen, A. Mancini, and B. Chovitz (eds.), American Geophysical Union, Washington, DC, pp. 247–251, 1972.   
[113] Schaub, H., and J. Junkins, Analytical Mechanics of Space Systems, American Institute of Aeronautics and Astronautics, Reston, VA, 2003.   
[114] Schlee, F. H., C. J. Standish, and N. F. Toda, “Di vergence in the Kalman filter ,” AIAA J., Vol. 5, No. 6, pp. 1114–1120, June 1967.

[115] Schutz, B., B. D. Tapley, P. Abusali, H. Rim, “Dynamic orbit determination using GPS measurements from TOPEX/Poseidon,” Geophys. Res. Ltrs., Vol. 21, No. 19, pp. 2179–2182, 1994.

[116] Seeber, G., Satellite Geodesy: Foundations, Methods & Applications, Walter de Gruyter, New York, 1993.

[118] Seidelmann, P. K. (ed.), Explanatory Supplement to the Astronomical Almanac, University Science Books, Mill Valley, CA, 1992.

[119] Shampine, L., and M. Gordon, Computer Solution of Ordinary Differential Equations, The Initial Value Problem, W. H. Freeman and Co., San Francisco, 1975.

[120] Shum, C. K., B. Zhang, B. Schutz, and B. Tapley, “Altimeter crossover methods for precise orbit determination and the mapping of geophysical parameters,” J. Astronaut. Sci., Vol. 38, No. 3, pp. 355–368, July– September 1990.

[121] Simon, J. L., P. Bretagnon, J. Chapront, M. Chapront-Touze, G. Francou, ´ J. Laskar, “Numerical expressions for precession formulae and mean elements for the Moon and planets,” Astronomy and Astrophysics, Vol. 282, pp. 663–683, 1994.

[122] Skolnik, M.I. (ed.), Radar Handbook, McGraw-Hill, New York, 1990.

[123] Smart, W. M., Celestial Mechanics, John Wiley & Sons Inc., New York, 1961.

[124] Sorenson, H. W., “Least squares estimation: from Gauss to Kalman,” IEEE Spectrum, Vol. 7, No. 7, pp. 63–68, July, 1970.

[125] Sorenson, H. W. (ed.), Kalman Filtering: Theory and Applications, IEEE Press, 1985.

[126] Standish, E. M., X. Newhall, J. Williams, and W. Folkner, JPL Planetary and Lunar Ephemerides (CD-ROM), Willmann-Bell, Inc., Richmond, VA 1997.

[127] Swerling, P., “First order error propagation in a stagewise differential smoothing procedure for satellite observations,” J. Astronaut. Sci., Vol. 6, pp. 46–52, 1959.

[128] Szebehely, V., Theory of Orbits, Academic Press, New York, 1967.

[129] Szebehely, V., and H. Mark, Adventures in Celestial Mechanics, John Wiley & Sons, Inc., New York, 1998.

[130] Tapley, B. D., “Stat istical orbit determination theory,” in Recent Advances in Dynamical Astronomy, B. D. Tapley and V. Szebehely (eds.), D. Reidel, pp. 396–425, 1973.

[131] Tapley, B. D.,“ Fundamentals of orbit determination”, in Theory of Satellite Geodesy and Gravity Field Determination, Vol. 25, pp. 235-260, Springer-Verlag, 1989.

[132] Tapley, B. D., and C. Y. Choe, “An algorithm for propagating the square root covariance matrix in triangular form,” Trans. Auto. Cont., Vol. AC-21, pp. 122–123, 1976.

[133] Tapley, B. D., and D. S. Ingram, “O rbit determination in the presence of unmodeled accelerations,” Trans. Auto. Cont., Vol. AC-18, No. 4, pp. 369– 373, August 1973.

[134] Tapley, B. D., and J. G. Peters, “A sequential estimation algorithm using a continuous $U D U ^ { T }$ covariance factorization,” J. Guid. Cont., Vol. 3, No. 4, pp. 326–331, July–August 1980.

[135] Tapley, B. D., J. Ries, G. Davis, R. Eanes, B. Schutz, C. Shum, M. Watkins, J. Marshall, R. Nerem, B. Putney, S. Klosko, S. Luthcke, D. Pavlis, R. Williamson, and N. P. Zelensky, “Pre cision orbit determination for TOPEX/Poseidon,” J. Geophys. Res., Vol. 99, No. C12, pp. 24,383– 24,404, December 15, 1994.

[136] Tapley, B. D., M. Watkins, J. Ries, G. Davis, R. Eanes, S. Poole, H. Rim, B. Schutz, C. Shum, R. Nerem, F. Lerch, J. Marshall, S. Klosko, N. Pavlis, and R. Williamson, “The Joint Gravity Model 3,” J. Geophys. Res., Vol. 101, No. B12, pp. 28,029–28,049, December 10, 1996.

[137] Thompson, B., M. Meek, K. Gold, P. Axelrad, G. Born, and D. Kubitschek, “Orbit determination for the QUIKSCAT spacecraft,” J. Spacecr. Rockets, Vol. 39, No. 6, pp. 852–858, November–Decem ber 2002.

[138] Thornton, C. L., Triangular covariance factorizations for Kalman filtering , Technical Memorandum, 33–798, Jet Propulsion Laboratory, Pasadena, CA, October 15, 1976.

[139] Torge, W., Geodesy, Walter de Gruyter, Berlin, 1980 (translated to English: Jekeli, C.).

[140] Vallado, D., Fundamentals of Astrodynamics and Applications, Space Technology Library, Microcosm Press, El Segundo, CA, 2001.

[141] Vigue, Y., B. Schutz, and P. Abusali, “Thermal force modeling for the Global Positioning System satellites using the finite element method,” $J .$ Spacecr. Rockets, Vol. 31, No. 5, pp. 866–859, 1994.

[142] Visser, P., and B. Ambrosius, “O rbit determination of TOPEX/Poseidon and TDRSS satellites using TDRSS and BRTS tracking,” Adv. Space Res., Vol. 19, pp. 1641–1644, 1997.

[143] Wahr, J. M., “The forced nutations of an elliptical, rotating, elastic, and oceanless Earth,” Geophys. J. of Royal Astronom. Soc., 64, pp. 705–727, 1981.

[144] Walpole, R. E., R. H. Myers, S. L. Myers, and Y. Keying, Probability and Statistics for Engineers and Scientists, Prentice Hall, Englewood Cliffs, NJ, 2002.

[145] Webb, C.,The ICRF-ITRF Transformation: A Comparison of Fundamental Earth Orientation Models found in MSODP and CALC, The University of Texas at Austin, Center for Space Research Report CSR-02-01, Austin, TX, 2002.

[146] Wells, D., Guide GPS Positioning, Canadian GPS Associates, Fredericton, 1987.

[147] Westfall, R., Never at Rest: A Biography of Isaac Newton, Cambridge University Press, Cambridge, 1980.

[148] Wiener, N., The Extrapolation, Interpolation and Smoothing of Stationary Time Series, John Wiley & Sons, Inc., New York, 1949.

[149] Wiesel, W. E., Spaceflight Dynamics, McGraw-Hill, 1997.

[150] Woolard, E., Theory of the rotation of the Earth around its center of mass, Astronomical Papers—American Ephemeris and Nautical Almanac, Vol. XV, Part I, U.S. Naval Observatory, Washington, DC, 1953.

# Author Index

Abusali, P., 69, 159   
Allman, M., 19, 56   
Altamini, Z., 78   
Ambrosius, B., 132   
Andrews, A. P., 199   
Axelrad, P., 116, 148, 233   
Balmino, G., 488   
Bar-Sever, Y., 125, 159   
Barlier, F., 67   
Battin, R. H., 19, 165, 167, 333   
Berger, C., 67   
Bertiger, W., 125, 159   
Bettadpur, S., 125   
Beutler, G., 68   
Biancale, R., 488   
Bierman, G. J., 199, 205, 206, 316,   
338–340, 342–345, 369–   
371, 397, 434   
Bjorck, A., 173, 180 ¨   
Bode, A., 488   
Bond, V., 19, 56   
Born, G. H., 60, 147, 148, 233, 493   
Boucher, C. Z., 78   
Brahe, T., 17   
Bretagnon, P., 520   
Brockmann, E., 68   
Brouwer, D., 28, 59, 70, 493, 495,   
497   
Bryson, A. E., 251, 331   
Bucy, R., 13, 205   
Buffett, B., 73, 113   
Cajori, F., 13   
Carlson, N. A., 338, 339   
Chapront, J., 520   
Chapront-Touze, M., 520 ´   
Chinn, D., 147, 488   
Chobotov, V., 19   
Choe, C. Y., 346   
Christensen, E., 146, 159   
Clemence, G., 28   
Collins, J., 116, 120, 123, 124, 148   
Conway, B., 19   
Cook, G. E., 60   
Cox, C. M., 132, 488   
Cruickshank, D. R., 229, 233, 499   
Curkendall, D. W., 434   
Dahlquist, G., 180   
Danby, J. M. A., 19, 24, 51, 67   
Davis, E., 159   
Davis, G., 159, 243, 244, 487   
Davis, J. C., 465   
Degnan, J., 126, 127   
Desai, S. D., 125, 160   
Deutsch, R., 185   
Dorroh, W. E., 251   
Dunn, C., 125   
Dyer, P., 343, 358   
Eanes, R., 159, 243, 244, 487   
Einstein, A., 18, 65   
El´Yasberg, P. E., 44   
Enge, P., 116   
Factor, J., 488   
Falin, J., 67   
Fisher, R. A., 13, 190   
Flannery, B., 45   
Fliegel, H., 68   
Folkner, W., 64, 74, 488, 519   
Francou, G., 520   
Franklin, G., 125   
Freeman, H., 440, 451, 465   
Fricke, W., 519   
Gallini, T., 68   
Gauss, K. F., 12, 13, 173   
Gelb, A., 199   
Gentleman, W. M., 302, 307   
Gill, E., 94, 199   
Givens, W., 292, 324, 330   
Gold, K., 148   
Goldstein, D. B., 233, 493   
Golub, G. H., 288   
Goodyear, W. H., 40, 41, 182   
Gordon, M., 45, 46   
Graybill, F. A., 331, 463, 464, 473,   
480   
Grewal, M. S., 199   
Gruber, T., 488   
Guinn, J., 159   
Gurtner, W., 68   
Haines, B. J., 125, 146, 159, 160   
Hanson, R. J., 173, 332   
Harris, I., 125   
Heffes, H., 427   
Hegler, G., 60   
Heiskanen, W., 52, 53   
Helmert, F. R., 13   
Helstrom, C. W., 440   
Herring, T., 73, 113   
Ho, Y. C., 251   
Hofmann-Wellenhof, B., 116, 120,   
124, 148   
Householder, A. S., 310   
Huang, C., 65, 116   
Hugentobler, U., 68   
Ibanez-Meier, R., 159   
Ingram, D. S., 229, 233, 369   
Jacchia, L., 67   
Jazwinski, A. H., 246, 248, 434   
Jee, J., 159   
Joseph, P. D., 205   
Junkins, J., 19   
Kalman, R. E., 13, 14, 199, 206, 208,   
334, 388   
Kaminski, P. G., 331, 343, 364, 366   
Kaula, W. M., 58, 59, 485   
Kenyon, S., 488   
Kepler, J., 17, 27   
Keying, Y., 465   
Kim, J., 125   
Klosko, S., 159, 243, 244, 487, 488   
Kockarts, G., 67   
Kolaczek, B., 18   
Kolmogorov, A. N., 13   
Kovalevsky, J., 18   
Kreyszig, E., 251   
Kruizinga, G., 125   
Kuang, D., 125   
Kubitschek, D., 148   
Lambeck, K., 64, 71   
Laplace, P. S., 13, 171   
Laskar, J., 520   
Lawson, C. L., 173, 332   
Lederle, T., 519   
Legendre, A. M., 13, 52   
Leick, A., 116   
Lemoine, F., 147, 487   
Lemoine, J., 488   
Lerch, F. J., 132, 243, 487   
Lichten, S. M., 159, 229, 233   
Lichtenegger, H., 116, 120, 123, 124,   
148   
Liebelt, P. B., 199   
Lieske, J. H., 519   
Lundberg, J., 53   
Lutchke, S. B., 132, 147, 159, 160,   
244, 488   
Marini, J. W., 112, 113   
Mark, H., 19   
Markov, A. A., 13, 230   
Marr, G., 147   
Marshall, J. A., 132, 159, 243, 244,   
487   
Mathews, P., 73, 113   
Maybeck, P. S., 199, 230, 233, 342,   
343, 345, 503   
McCarthy, D., 64, 77, 78, 487, 488,   
518–520   
McColl, K. C., 146   
McGarry, J., 126, 127   
McReynolds, S., 343, 358   
Meehan, T., 125   
Meek, M., 148   
Melbourne, W., 159   
Mervart, L., 68   
Mikhail, E. M., 251   
Mitchell, J., 60   
Mohr, P. J., 487   
Moler, C., 172   
Montenbruck, O., 94, 199   
Morando, B., 519   
Moritz, H., 52, 53, 71   
Motte, A., 17   
Moulton, F. R., 45   
Mueller, I., 18, 71   
Muellerschoen, R., 159   
Munson, T., 159   
Murray, C. W., 112, 113   
Myers, K. A., 190, 191, 231   
Myers, R. H., 465   
Myers, S. L., 465

Nandi, S., 125

Nerem, R. S., 146, 159, 243, 244,   
487   
Newhall, X., 64, 74, 488, 519   
Newton, I., 16–20, 44, 71, 162, 244   
Nguyen, D., 125

Olson, T., 488

Papoulis, A., 467   
Parkinson, B., 116   
Pavlis, D., 147, 159, 244   
Pavlis, E., 488   
Pavlis, N., 243, 487, 488   
Peters, J. G., 346   
Pines, S., 54   
Plummer, H.C., 17   
Pollard, H., 486   
Poole, S., 243, 487   
Press, W., 45   
Prussing, J., 19   
Putney, B., 159, 244   
Rapp, R., 488   
Rasmussen, M. L., 254   
Rausch, H. E., 248, 250, 365   
Reddy, J. N., 254   
Reigber, C., 488   
Ries, J. C., 65, 69, 116, 159, 243,   
244, 487   
Rim, H., 159, 243, 487   
Rogstad, T., 125   
Romans, L., 125   
Rothacher, M., 68   
Rowlands, D. D., 132, 147   
Rowton, S. C., 132   
Roy, A. E., 19   
Saastamoinen, J., 112   
Santee, M. L., 147   
Schaub, H., 19   
Schlee, F. H., 220   
Schmidt, S. F., 331   
Schutz, B. E., 53, 147, 159, 243, 244,   
487   
Schwintzer, P., 488   
Seeber, G., 94, 518   
Seidelmann, P. K., 74, 77, 487, 488,   
518   
Shampine, L., 45, 46   
Shapiro, I., 73, 113   
Shum, C. K., 69, 147, 159, 243, 244,   
487   
Sillard, P., 78   
Simon, J. L., 520   
Smart, W. M., 28   
Sorenson, H. W., 14, 199   
Spilker, J., 116   
Standish, C. J., 220   
Standish, E. M., 64, 74, 488, 519   
Striebel, C. T., 248, 250, 365   
Swerling, P., 13, 199   
Swift, E., 68   
Szebehely, V., 19, 46   
Tapley, B. D., 65, 116, 147, 159, 160,   
199, 233, 243, 244, 346,   
369, 487   
Taylor, B. N., 487   
Teukolsky, S., 45   
Thomas, J., 125   
Thompson, B., 148, 493   
Thornton, C. L., 340, 342–345, 434   
Thornton, T. H., 251   
Thuiller, G., 67   
Tien, J., 125   
Toda, N. F., 220   
Torge, W., 79   
Torrence, M., 488   
Trimmer, R., 488   
Tung, F., 248, 250, 365   
Vallado, D., 19, 26   
Van Loan, C., 172   
Verdun, A., 68   
Vetterling, W., 45   
Vigue, Y., 69, 159   
Visser, P., 132   
Wahr, J. M., 73   
Walpole, R. E., 190, 191, 465   
Wang, Y., 488   
Watkins, M. M., 65, 116, 125, 159,   
243, 244, 487   
Webb, C., 518   
Westfall, R., 17   
Wiener, N., 13   
Wiesel, W. E., 257   
Williams, J., 64, 74, 488, 519   
Williamson, R. G., 132, 159, 243,   
244, 487, 488   
Willis, P., 159   
Woolard, E., 73   
Wu, S. C., 125, 159   
Yunck, T., 159   
Zelensky, N. P., 147, 159, 244   
Zhang, B., 147

# Index

along-track direction, 42   
ambiguity, 135   
ambiguity resolution, 135   
AMOS (Air Force Maui Optical and Supercomputing), 149   
AN (ascending node), 28, 31   
angular momentum, 20–22, 28, 30, 32, 74, 90, 238, 254, 257   
apfocus, 25   
apogee, 25   
area-to-mass ratio, 67   
argument of perigee, 24, 36, 62, 63, 65, 493   
ARP (antenna reference point), 122   
AS (anti-spoofing), 120   
ascending node, 28–31, 47, 58, 60, 62 longitude of, 29, 40, 238 right ascension of, 29, 36   
autocorrelation, 230, 231, 469   
autocovariance, 469   
autumnal equinox, 31   
azimuth, 81

ballistic coefficient, 36, 66, 67   
batch processor, 190, 194, 197, 237   
Bayes theorem, 465, 466   
Bayesian estimation, 190   
biased range, 102   
bivariate normal density function, 460   
bivariate normal distribution, 460, 461   
broadcast ephemerides, 124

carrier frequencies, 116   
CCD (charge coupled device), 148   
central force, 1, 162   
central limit theorem, 465   
characteristic polynomial, 478   
characteristic root, 478   
characteristic vector, 478   
choke-ring antenna, 121   
Cholesky decomposition, 14, 198, 286, 287, 290, 295, 318, 324, 325, 330, 332, 334, 342, 384   
clock time, 102   
clock-steering, 134   
CNES (Centre National d’Etudes Spatiales), 132   
combining estimates, 258   
computed observation, 93, 179   
computed range, 97   
conditional density function, 191–193, 246, 249, 454, 461, 464, 466   
conditional probability, 247, 443, 454   
conditioning number, 332   
consider covariance, 435, 436, 438   
consider covariance analysis, 14, 245, 387, 388, 397, 400, 407, 410   
consider covariance matrix, 389, 396, 398   
consider error, 425   
consider fil ter, 388, 395, 416

consider parameters, 388–390   
constant of nutation, 73   
continuous system, 227   
coordinate system, 18   
correlation coefficient, 277, 457–459,   
463, 509   
covariance matrix coordinate trans  
formation, 257   
covariance matrix mapping, 190   
critical inclination, 59   
cross-link ranging, 125   
cross-track direction, 43   
crossover measurements, 146   
cycle slip, 134

derivative matrix, 161   
descending node, 31   
determinant, 462, 473, 475–477   
Dirac delta function, 220, 224, 227, 501   
direct effect, 63   
distribution function, 444, 452, 453, 468   
disturbing function, 49, 57, 485   
dithered, 122   
DMC (Dynamic Model Compensation), 220, 230, 233, 499, 505, 506, 508, 509   
DN (descending node), 29, 31   
Doppler effect, 109   
DORIS (Doppler Orbitography and Radio positioning Integrated by Satellite), 115, 132, 138   
downlink path, 99   
DOY (day of year), 75   
drag, 66 drag coefficie nt, 66   
dry component, 111   
dual-one-way-ranging, 125   
eccentric anomaly, 25–27, 33, 35, 37, 44   
eccentricity, 24, 28, 33, 36, 44, 57– 59, 67, 79, 82, 88, 497   
eccentricity vector, 33   
ECEF (Earth-centered, Earth-fix ed) or ECF (Earth-centered, fix ed) 32, 39, 56, 79, 82, 90, 91, 105, 135, 136, 151, 257, 517   
ECI (Earth-centered inertial), 32, 34, 43, 56, 82, 91, 105, 106, 257, 258, 517   
ecliptic, 30, 31, 46, 47, 49, 50, 63, 72, 73   
eigenvalue, 332, 478   
eigenvector, 478   
EKF (Extended Kalman Filter), 209   
elevation, 81   
elevation mask, 96   
empirical forces, 69   
empty focus, 25   
energy per unit mass, 21   
EOP (Earth Orientation Parameters), 518   
ephemeris, 37   
ephemeris parameters, 124   
ERS (European Earth Resources Satellites), 128   
escape trajectories, 25   
estimation error covariance matrix, 185   
Euler angles, 254, 255   
expected value, 222, 248, 405, 408, 445, 447, 455, 469   
extended sequential filter , 202, 209, 349   
frozen orbits, 60, 61   
gain matrix, 200, 429   
GALILEO, 118   
Gauss-Markov Process, 220, 229–232, 281, 369, 371, 506   
Gaussian distribution, 277   
general perturbations, 45, 59   
geocenter, 54   
geocentric latitude, 39, 52, 65, 78, 79, 81   
geodetic latitude, 78, 79, 113   
geometric range, 94   
Givens algorithm, 208, 298, 300, 307– 309, 327, 330, 335 rotation, 292, 298, 300, 303, 327 square root factorization algorithm, 344 square root free algorithm, 330 square root free computational algorithm, 305 square root free transformation, 301, 302, 307, 325, 326, 384 transformation, 291, 318, 320, 324, 344, 357, 384   
GLAS (Geoscience Laser Altimeter System), 130   
GLONASS (Global Navigation Satellite System), 118   
GMST (Greenwich Mean Sidereal Time), 31, 520   
GPS (Global Positioning System), 69, 70, 74, 77, 78, 87–89, 93, 115, 116, 118, 120, 122, 123, 132, 134, 140, 146, 151   
GPS-T (GPS-Time), 76, 77, 134   
GPS-week, 77   
GRACE (Gravity Recovery And Climate Experiment), 125   
Gram-Schmidt orthogonalization, 344, 345   
gravitational pertubations, 50   
ground track, 38, 40, 90, 95, 97, 100   
height above the ellipsoid, 78   
high-high, 125   
high-low, 125   
Hipparcos astrometry satellite, 148   
Householder algorithm, 208, 316, 325, 330 equations, 314 transformation, 310–312, 315, 316, 318, 322, 329, 330, 344, 357, 384   
hydrostatic component, 111   
ICESat, 128, 130, 154   
ICRF (International Celestial Reference Frame), 517, 518   
IERS (International Earth Rotation Service), 74, 78, 488, 518– 521   
IGS (International GPS Service), 124, 136   
ILRS (International Laser Ranging Service), 127   
inclination, 28   
index of refraction, 111   
indirect oblateness, 63   
inertial reference frame, 18   
information filter , 233, 235, 236, 284, 351   
information matrix, 190   
innovation, 210   
instantaneous range, 94   
ITRF (International Terrestrial Reference Frame), 78, 82, 135, 517, 518   
J2000 system, 31   
Jacobi Constant, 56   
Jacobi integral, 56, 91   
Jason-1 satellite, 159   
JD (Julian Date), 75   
Joseph covariance formulation, 205, 207, 208   
Julian day number, 75   
Kalman filter (see also sequential filter), 14, 199, 202, 207, 356, 427 gain, 200, 211   
Kepler’s Equation, 26–28, 35, 44   
kinematic solution, 148   
Kronicker delta, 199   
Lageos, 115   
Langevin equation, 230, 505   
leap seconds, 77   
least squares, 9, 14, 173, 174, 176, 177, 187, 352   
Legendre functions, 53 polynomial, 52, 53   
Legendre’s Associated Functions, 52, 53   
LEO (Low Earth Orbiter), 124, 125, 147, 148   
likelihood function, 191, 193, 194, 259, 277   
line of nodes, 22, 28–30, 47, 58   
linear approximations, 42   
linearization, 9, 160, 161, 202, 209   
LOD (length of day), 74, 91   
long-period perturbations, 48   
longitude, 78   
longitude angle, 52   
low-low, 125

M50 system, 31   
marginal distribution, 461, 463, 469   
mass distribution, 50   
matrix trace, 477   
matrizant, 40   
Maximum Likelihood Estimation, 190–   
193, 276, 277, 290   
MC (Master Clock), 77   
mean, 445   
mean anomaly, 27, 36   
mean elements, 58

mean equator and equinox of 1950.0, 32 of 2000.0, 31   
mean motion, 27   
measurement noise, 144   
measurement precision, 144   
measurement update, 202   
median, 194, 466, 467   
minimum norm, 174, 175, 273   
minimum variance, 183–186, 188, 194, 259, 290   
minimum variance estimation, 14   
Minitrack, 93   
MJD (modified Julian date), 75   
mode, 191, 194, 466, 467   
MOLA (Mars Orbiter Laser Altimeter), 130   
moment generating function, 448, 450   
multipath, 121   
multivariate normal density function, 462   
multivariate normal distribution, 462– 464   
multiway, 131   
n-body effects, 61   
navigation message, 124   
navigation solution, 148   
Newton-Raphson method, 7, 27, 180, 182   
NIMA (National Imagery and Mapping Agency), 124   
NIST (National Institute of Standards and Time), 76   
nodal period, 60, 61   
nondispersive medium, 111   
nonnegative definite , 476   
nonspherical, 54   
normal matrix, 174, 177, 187, 190, 229, 237, 238, 413   
normalized, 53   
nutation, 71–73, 82, 91, 243


<!-- chunk 0009: pages 561-563 -->
obliquity of the ecliptic, 30, 31, 63, 72, 73   
observability, 16, 178, 237, 239, 240, 273   
observation deviation vector, 11, 161, 162   
observation residual, 179, 210, 291, 322, 324, 349   
observation vector, 162   
observed minus computed, 97   
one-way range, 99   
orbit accuracy, 82   
orbit determination, 2, 159–162   
orbit plane, 21   
orbital inclination, 28   
orbital period, 44, 47, 87   
orthogonal matrix, 290, 292, 302, 312, 331, 332, 477, 478   
orthogonal processes, 470   
orthogonal transformation, 14, 301   
osculating elements, 47

performance index, 12, 173   
perifocus, 24, 25   
perigee, 24   
periodic perturbations, 58   
periodic variation, 44, 47   
perturbation matrix, 397, 398, 438   
perturbing forces, 45, 48–50, 55, 63,   
66, 69, 485   
phase, 110   
phase center, 121   
phase pseudorange, 110   
point of closest approach, 96   
polar motion, 74, 78, 82, 91, 243,   
369   
pole tides, 65   
positive definite, 475–478   
positive semidefinite, 475–478   
Potter algorithm, 334, 343   
PRARE (Precise Range and Range   
Rate Equipment), 128

precession, 71–73, 82, 91, 243   
precession of the equinoxes, 73   
predicted residual, 210   
principal axes transformation, 252   
Principia, 17   
probability density function, 183, 190, 191, 230, 443, 444, 466   
probability ellipsoid, 251, 253   
problem of three bodies, 46   
process noise, 220–222, 229, 250, 283, 284, 354, 358, 359, 369–371, 503, 507 covariance matrix, 220, 229, 233, 346 transition matrix, 228   
pseudo inverse, 175   
pseudo-random noise, 118   
pseudorange, 102   
quadratic convergence, 182   
QUIKSCAT, 495–497   
random sequence, 227, 231   
random variable, 439, 440   
random walk, 232, 370, 384   
range-rate, 107   
rank, 174, 175, 178, 186, 239, 240, 291, 293, 344, 475, 476, 478   
receive time, 136   
reference frame, 18, 48, 69, 77, 78, 103, 121, 127   
reference systems, 18   
refractivity, 111   
regression of the node, 47   
residual, 97, 99, 103, 135   
resonance, 60   
restricted problem of three bodies, 46   
RMS, 198, 297   
SA (Selective Availability), 89, 122, 137, 140, 141, 148   
Sagnac effect, 115, 116   
satellite-borne altimeters, 125   
Schur identity, 200, 233, 248, 394   
sectoral harmonics, 53   
secular change, 44, 68, 91 node rate, 47, 57, 63 perturbation, 58 rate, 58, 61, 70 variation, 47, 48, 61, 63   
semilatus rectum, 24, 33   
sensitivity matrix, 394, 397, 407, 414, 419   
sequential filte r (see also Kalman filter), 199, 201, 204, 237   
sequential processor, 190   
short-period perturbations, 48   
single difference (SD), 140–144   
sky plot, 96   
SLR (satellite laser ranging), 99, 103, 104, 125–130, 132   
smoothing, 115, 246, 248, 250, 251, 363, 364, 366, 369, 375, 377, 378, 380, 384   
SNC (state noise compensation), 220, 233, 501, 504–506, 508   
solar radiation pressure, 68, 369   
solar-synchronous, 58, 88   
solution technique accuracy, 83   
SPE (secularly precessing ellipse), 58   
special perturbations, 45   
specific energy, 21, 25   
spherical harmonic coefficients , 52   
square root covariance fil ter, 331 filter , 330 information batch processor, 297 information filter , 298, 351, 353 information matrix, 298 measurement update, 331, 332 measurement update algorithm, 333 state error covariance, 350   
square root free algorithm, 301, 340 Cholesky algorithm, 288 Cholesky decomposition, 342 Givens algorithm, 305, 308, 330 Givens rotation, 327 Givens transformation, 301, 302, 307, 325, 326 measurement update algorithm, 340   
SST (satellite-to-satellite tracking), 125   
SST measurements dual-one-way-ranging, 125 high-high, 125 high-low, 125 low-low, 125   
standard deviation, 446, 458   
standardized random variables, 457, 458, 465   
state deviation vector, 11, 161, 162, 167, 194, 211   
state noise, 220   
state transition matrix, 11, 40, 164, 167, 176, 182, 202, 501, 506, 513   
state vector, 2, 160–162   
stationary process, 470   
stochastic process, 230, 467–470   
Stokes coefficients, 52   
subsatellite point, 39   
summer solstice, 31   
symplectic, 167, 266, 269   
TAI (International Atomic Time), 76, 77   
Tapley, B. D., 69   
Taylor series, 10, 11, 160, 161, 225, 400   
TDB (Barycentric Dynamical Time), 76, 77   
TDRSS (NASA Tracking and Data Relay Satellite System), 13   
TDT (Terrestrial Dynamical Time), 76   
TEC (total electron content), 114   
tesseral harmonics, 53   
thermal force, 69   
three-way measurement, 99   
time update, 202   
time-of-flight, 99   
TLE (Two Line Element), 35   
TOPEX/Poseidon, 69, 90, 104, 128, 129, 132, 138, 146, 159, 229, 243–245   
trace, 202, 205, 208, 406, 477, 478   
Transit, 115   
TRF (Terrestrial Reference Frame), 78   
triangular square root measurement update, 335   
tropospheric delay, 111   
true anomaly, 24, 26, 27, 33, 35, 106   
true of date, 74   
TT (Terrestrial Time), 76, 77, 519   
two-way range, 99   
U–D covariance factorization, 340   
unbiased estimate, 188, 277   
uniform distribution, 450   
Universal Time, 74–76   
uplink path, 99   
USNO (U.S. Naval Observatory), 76, 77   
UTC (Coordinated Universal Time), 76, 77

variance, 183–186, 188, 446   
variance-covariance matrix, 178, 456,   
457, 460, 462   
variation of parameters, 48   
Venn diagram, 440, 441

vernal equinox, 30, 31, 46, 47, 55, 72, 73, 91   
vis viva, 21   
VLBI (Very Long Baseline Interferometry), 517, 518   
water vapor radiometers, 112   
weighted least squares, 14, 176–178, 183, 187, 194, 276, 392   
WGS-84 (World Geodetic System), 78, 89, 487   
winter solstice, 31   
y-bias force, 69   
Y-code, 134   
zonal harmonics, 53
