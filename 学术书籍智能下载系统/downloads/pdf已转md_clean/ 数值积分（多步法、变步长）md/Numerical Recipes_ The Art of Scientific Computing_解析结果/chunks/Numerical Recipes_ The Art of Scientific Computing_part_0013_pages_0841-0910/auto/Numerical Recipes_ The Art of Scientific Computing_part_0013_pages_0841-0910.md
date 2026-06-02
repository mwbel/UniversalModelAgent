![](images/7c195fcbb06f0c8f481069f0f2f8f439a48e0d51f665bffe0a7dbbe8fae6be66.jpg)  
Figure 15.6.5. Relation of the confidence region ellipse $\Delta \chi ^ { 2 } = 1$ to quantities computed by singular value decomposition. The vectors $\mathbf { V } _ { ( i ) }$ are unit vectors along the principal axes of the confidence region. The semi-axes have lengths equal to the reciprocal of the singular values $w _ { i }$ . If the axes are all scaled by some constant factor $\pmb { \alpha }$ , $\Delta \chi ^ { 2 }$ is scaled by the factor $\alpha ^ { 2 }$ .

but generally more convenient, form. The columns of the matrix $\mathbf { V }$ are an orthonormal set of $M$ vectors that are the principal axes of the $\Delta \chi ^ { 2 } =$ constant ellipsoids. We denote the columns as $\mathbf { V } _ { ( 0 ) } \ldots \mathbf { V } _ { ( M - 1 ) }$ . The lengths of those axes are inversely proportional to the corresponding singular values $w _ { 0 } \dots { } \psi _ { M - 1 }$ ; see Figure 15.6.5. The boundaries of the ellipsoids are thus given by

$$
\Delta \chi ^ { 2 } = w _ { 0 } ^ { 2 } ( { \bf V } _ { ( 0 ) } \cdot \delta { \bf a } ) ^ { 2 } + \cdots + w _ { M - 1 } ^ { 2 } ( { \bf V } _ { ( M - 1 ) } \cdot \delta { \bf a } ) ^ { 2 }
$$

which is the justification for writing equation (15.4.18) above. Keep in mind that it is much easier to plot an ellipsoid given a list of its vector principal axes than given its matrix quadratic form: Loop over points $\mathbf { z }$ on a unit sphere in any desired way (e.g., by latitude and longitude) and plot the mapped points

$$
\delta { \bf a } = \sqrt { \Delta \chi ^ { 2 } } \sum _ { i } \frac { 1 } { w _ { i } } ( { \bf z } \cdot { \bf V } _ { ( i ) } ) { \bf V } _ { ( i ) }
$$

The formula for the covariance matrix $\mathbf { C }$ in terms of the columns $\mathbf { V } _ { ( i ) }$ is

$$
\mathbf { C } = \sum _ { i = 0 } ^ { M - 1 } \frac { 1 } { w _ { i } ^ { 2 } } \mathbf { V } _ { ( i ) } \otimes \mathbf { V } _ { ( i ) }
$$

or, in components,

$$
C _ { j k } = \sum _ { i = 0 } ^ { M - 1 } \frac { 1 } { w _ { i } ^ { 2 } } V _ { j i } V _ { k i }
$$

A method for plotting error ellipses (2-dimensions) or ellipsoids (3-dimensions) from the covariance matrix $\mathbf { C }$ directly, not using its principal axes, is described in $\ S 1 6 . 1 . 1$ .

# CITED REFERENCES AND FURTHER READING:

Davison, A.C., and Hinkley, D.V. 1997, Bootstrap Methods and Their Application (New York: Cambridge University Press).   
Efron, B. 1982, The Jackknife, the Bootstrap, and Other Resampling Plans (Philadelphia: S.I.A.M.).[1]   
Efron, B., and Tibshirani, R. 1993, An Introduction to the Bootstrap (Boca Raton, FL: CRC Press).[2]   
Lupton, R. 1993, Statistics in Theory and Practice (Princeton, NJ: Princeton University Press), Chapters 10–11.   
Avni, Y. 1976, “Energy Spectra of X-Ray Clusters of Galaxies,” Astrophysical Journal, vol. 210, pp. 642–646.[3]   
Lampton, M., Margon, M., and Bowyer, S. 1976, “Parameter Estimation in X-ray Astronomy,” Astrophysical Journal, vol. 208,pp.177-190.   
Brownlee, K.A. 1965, Statistical Theory and Methodology, 2nd ed. (New York: Wiley).   
Martin, B.R. 1971, Statistics for Physicists (New York: Academic Press).

# 15.7 Robust Estimation

The concept of robustness has been mentioned in passing several times already. In $\ S 1 4 . 1$ we noted that the median was a more robust estimator of central value than the mean; in $\ S 1 4 . 6$ it was mentioned that rank correlation is more robust than linear correlation. The concept of outlier points as exceptions to a Gaussian model for experimental error was discussed in $\ S 1 5 . 1$ .

The term “robust” was coined in statistics by G.E.P. Box in 1953. Various definitions of greater or lesser mathematical rigor are possible for the term, but in general, referring to a statistical estimator, it means “insensitive to small departures from the idealized assumptions for which the estimator is optimized” [1,2,3]. The word “small” can have two different interpretations, both important: either fractionally small departures for all data points, or else fractionally large departures for a small number of data points. It is the latter interpretation, leading to the notion of outlier points, that is generally the most stressful for statistical procedures.

Statisticians have developed various sorts of robust statistical estimators. Many, if not most, can be grouped into one of three categories.

M-estimates follow from maximum likelihood arguments very much as equations (15.1.6) and (15.1.8) followed from equation (15.1.3). M-estimates are usually the most relevant class for model fitting, that is, estimation of parameters. We therefore consider these estimates in some detail below.

L-estimates are “linear combinations of order statistics.” These are most applicable to estimations of central value and central tendency, though they can occasionally be applied to some problems in estimation of parameters. Two “typical” L-estimates will give you the general idea. They are (i) the median, and (ii) Tukey’s trimean, defined as the weighted average of the first, second, and third quartile points in a distribution, with weights 1/4, 1/2, and 1/4, respectively.

$R$ -estimates are estimates based on rank tests. For example, the equality or inequality of two distributions can be estimated by the Wilcoxon test of computing the mean rank of one distribution in a combined sample of both distributions. The Kolmogorov-Smirnov statistic (equation 14.3.17) and the Spearman rankorder correlation coefficient (14.6.1) are R-estimates in essence, if not always by formal definition.

![](images/ae2e5e65a3fd9245ce96e89e28f087adca64bb9a54e33b0f07e16fbd802b4d61.jpg)  
Figure 15.7.1. Examples where robust statistical methods are desirable: (a) A one-dimensional distribution with a tail of outliers; statistical fluctuations in these outliers can prevent accurate determination of the position of the central peak. (b) A distribution in two dimensions fitted to a straight line; nonrobust techniques such as least-squares fitting can have undesired sensitivity to outlying points.

Some other kinds of robust techniques, coming from the fields of optimal control and filtering rather than from the field of mathematical statistics, are mentioned at the end of this section. Some examples where robust statistical methods are desirable are shown in Figure 15.7.1.

# 15.7.1 Estimation of Parameters by Local M-Estimates

Suppose we know that our measurement errors are not normally distributed. Then, in deriving a maximum likelihood formula for the estimated parameters a in a model $y ( x | \mathbf { a } )$ , we would write instead of equation (15.1.3)

$$
P = \prod _ { i = 0 } ^ { N - 1 } \left\{ \exp \left[ - \rho ( y _ { i } , y \left\{ x _ { i } | \mathbf { a } \right\} ) \right] \Delta y \right\}
$$

where the function $\rho$ is the negative logarithm of the probability density. Taking the logarithm of (15.7.1) analogously with (15.1.5), we find that we want to minimize the expression

$$
\sum _ { i = 0 } ^ { N - 1 } \rho ( y _ { i } , y \left\{ x _ { i } \left| \mathbf { a } \right. \right\} )
$$

Very often, it is the case that the function $\rho$ depends not independently on its two arguments, measured $y _ { i }$ and predicted $y ( x _ { i } )$ , but only on their difference, at least if scaled by some weight factors $\sigma _ { i }$ that we are able to assign to each point. In this case the M-estimate is said to be local, and we can replace (15.7.2) by the prescription

$$
{ \mathrm { m i n i m i z e ~ o v e r ~ { \mathbf { a } } ~ } } \quad \quad \sum _ { i = 0 } ^ { N - 1 } \rho \left( { \frac { y _ { i } - y ( x _ { i } | \mathbf { a } ) } { \sigma _ { i } } } \right)
$$

where the function $\rho ( z )$ is a function of a single variable $z \equiv [ y _ { i } - y ( x _ { i } ) ] / \sigma _ { i }$

If we now define the derivative of $\rho ( z )$ to be a function $\psi ( z )$ ,

$$
\psi ( z ) \equiv { \frac { d \rho ( z ) } { d z } }
$$

then the generalization of (15.1.8) to the case of a general M-estimate is

$$
0 = \sum _ { i = 0 } ^ { N - 1 } \frac { 1 } { \sigma _ { i } } \psi \left( \frac { y _ { i } - y ( x _ { i } ) } { \sigma _ { i } } \right) \left( \frac { \partial y ( x _ { i } | \mathbf { a } ) } { \partial a _ { k } } \right) \qquad k = 0 , \dots , M - 1
$$

If you compare (15.7.3) to (15.1.3) and (15.7.5) to (15.1.8), you see at once that the specialization for normally distributed errors is

$$
\rho ( z ) = { \textstyle { \frac { 1 } { 2 } } } z ^ { 2 } \qquad \psi ( z ) = z \qquad \mathrm { ( n o r m a l ) }
$$

If the errors are distributed as a double or two-sided exponential, namely

$$
\mathrm { P r o b ~ \{ y } _ { \it { i } } - y ( x _ { \it { i } } ) \} \sim \exp \left( - \left| \frac { y _ { i } - y ( x _ { i } ) } { \sigma _ { i } } \right| \right)
$$

then, by contrast,

$$
\rho ( x ) = | z | \qquad \psi ( z ) = \operatorname { s g n } ( z ) \qquad { \mathrm { ( d o u b l e ~ e x p o n e n t i a l ) } }
$$

Comparing to equation (15.7.3), we see that in this case the maximum likelihood estimator is obtained by minimizing the mean absolute deviation, rather than the mean square deviation. Here the tails of the distribution, although exponentially decreasing, are asymptotically much larger than any corresponding Gaussian.

A distribution with even more extensive — and therefore sometimes even more realistic — tails is the Cauchy or Lorentzian distribution,

$$
\mathrm { P r o b ~ \{ } y _ { \it i } - y ( x _ { \it i } ) \} \sim \frac { 1 } { 1 + \displaystyle \frac { 1 } { 2 } \left( \frac { y _ { i } - y ( x _ { i } ) } { \sigma _ { i } } \right) ^ { 2 } }
$$

This implies

$$
\rho ( z ) = \log \left( 1 + { \frac { 1 } { 2 } } z ^ { 2 } \right) \qquad \psi ( z ) = { \frac { z } { 1 + { \frac { 1 } { 2 } } z ^ { 2 } } } \qquad { \mathrm { ( L o r e n t z i a n ) } }
$$

Notice that the $\psi$ function occurs as a weighting function in the generalized normal equations (15.7.5). For normally distributed errors, equation (15.7.6) says that the more deviant the points, the greater the weight. By contrast, when tails are somewhat more prominent, as in (15.7.7), then (15.7.8) says that all deviant points get the same relative weight, with only the sign information used. Finally, when the tails are even larger, (15.7.10) says the $\psi$ increases with deviation, then starts decreasing, so that very deviant points — the true outliers — are not counted at all in the estimation of the parameters.

This general idea, that the weight given individual points should first increase with deviation, then decrease, motivates some additional prescriptions for $\psi$ that do not especially correspond to standard, textbook probability distributions. Two examples are

Andrew’s sine

$$
\psi ( z ) = \left\{ \begin{array} { l l } { \sin ( z / c ) \quad } & { | z | < c \pi } \\ { 0 } & { | z | > c \pi } \end{array} \right.
$$

If the measurement errors happen to be normal after all, with standard deviations $\sigma _ { i }$ , then it can be shown that the optimal value for the constant $c$ is $c = 2 . 1$ .

Tukey’s biweight

$$
\psi ( z ) = \left\{ \begin{array} { l l } { z ( 1 - z ^ { 2 } / c ^ { 2 } ) ^ { 2 } } & { \quad | z | < c } \\ { 0 } & { \quad | z | > c } \end{array} \right.
$$

where the optimal value of $c$ for normal errors is $c = 6 . 0$ .

# 15.7.2 Numerical Calculation of M-Estimates

To fit a model by means of an M-estimate, you first decide which M-estimate you want, that is, which matching pair $\rho , \psi$ you want to use. We rather like (15.7.8) or (15.7.10).

You then have to make an unpleasant choice between two fairly difficult problems. Either find the solution of the nonlinear set of $M$ equations (15.7.5), or else minimize the single function in $M$ variables (15.7.3).

Notice that the function (15.7.8) has a discontinuous $\psi$ and a discontinuous derivative for $\rho$ . Such discontinuities frequently wreak havoc on both general nonlinear equation solvers and general function minimizing routines. You might now think of rejecting (15.7.8) in favor of (15.7.10), which is smoother. However, you will find that the latter choice is also bad news for many general equation solving or minimization routines: Small changes in the fitted parameters can drive $\psi ( z )$ off its peak into one or the other of its asymptotically small regimes. Therefore, different terms in the equation spring into or out of action (almost as bad as analytic discontinuities).

Don’t despair. If your computer is fast enough, or if your patience is great enough, this is an excellent application for the downhill simplex minimization algorithm exemplified in Amoeba (-10.5) or Amebsa (-10.12). Those algorithms make no assumptions about continuity; they just ooze downhill and will work for virtually any sane choice of the function $\rho$ .

It is very much to your (patience) advantage to find good starting values, however. Often this is done by first fitting the model by the standard $\chi ^ { 2 }$ (nonrobust) techniques, e.g., as described in $\ S 1 5 . 4$ or $\ S 1 5 . 5$ . The fitted parameters thus obtained are then used as starting values in Amoeba, now using the robust choice of $\rho$ and minimizing the expression (15.7.3).

# 15.7.3 Fitting a Line by Minimizing Absolute Deviation

Occasionally there is a special case that happens to be much easier than is suggested by the general strategy outlined above. The case of equations (15.7.7) $- \left( 1 5 . 7 . 8 \right)$ , when the model is a simple straight line,

$$
y ( x | a , b ) = a + b x
$$

and where the weights $\sigma _ { i }$ are all equal, happens to be such a case. The problem is precisely the robust version of the problem posed in equation (15.2.1) above, namely fit a straight line through a set of data points. The merit function to be minimized is

$$
\sum _ { i = 0 } ^ { N - 1 } | y _ { i } - a - b x _ { i } |
$$

rather than the $\chi ^ { 2 }$ given by equation (15.2.2).

The key simplification is based on the following fact: The median $c _ { M }$ of a set of numbers $c _ { i }$ is also the value that minimizes the sum of the absolute deviations

$$
\sum _ { i } | c _ { i } - c _ { M } |
$$

(Proof: Differentiate the above expression with respect to $c _ { M }$ and set it to zero.) It follows that, for fixed $b$ , the value of $a$ that minimizes (15.7.14) is

$$
a = { \mathrm { m e d i a n } } \{ y _ { i } - b x _ { i } \}
$$

Equation (15.7.5) for the parameter $b$ is

$$
0 = \sum _ { i = 0 } ^ { N - 1 } x _ { i } \ \mathrm { s g n } ( y _ { i } - a - b x _ { i } )
$$

(where $\operatorname { s g n } ( 0 )$ is to be interpreted as zero). If we replace $a$ in this equation by the implied function $a ( b )$ of (15.7.15), then we are left with an equation in a single variable that can be solved by bracketing and bisection, as described in $\ S 9 . 1$ . (In fact, it is dangerous to use any fancier method of root finding, because of the discontinuities in equation 15.7.16.)

Here is an object that does all this. It calls select (-8.5) to find the median. The bracketing and bisection are built into the routine, as is the linear fit that generates the initial guesses for $a$ and $b$ .

# struct Fitmed {

Object for fitting a straight line $y = a + b x$ to a set of points $( x _ { i } , y _ { i } )$ , by the criterion of least absolute deviations. Call the constructor to calculate the fit. The answers are then available as the variables a, b, and abdev (the mean absolute deviation of the points from the line).

Int ndata;   
Doub a, b, abdev;   
VecDoub_I &x, &y;

Answers.

Fitmed(VecDoub_I &xx, VecDoub_I &yy) : ndata(xx.size()), x(xx), y(yy) { Constructor. Given a set of data points xx[0..ndata-1], yy[0..ndata-1], sets a, b, and abdev.

Int j;   
Doub b1,b2,del,f,f1,f2,sigb,temp;   
Doub sx=0.0,sy=0.0,sxy ${ \tt = } 0$ .0,sxx ${ = } 0$ .0,chisq=0.0;   
for (j=0;j<ndata;j $^ { + + }$ ) { As a first guess for a and b, we will find the sx $+ =$ x[j]; least-squares fitting line. sy $+ =$ y[j]; sxy $+ =$ x[j]\*y[j]; sxx $+ =$ SQR(x[j]);   
}   
del=ndata\*sxx-sx\*sx;   
a=(sxx\*sy-sx\*sxy)/del; Least-squares solutions.   
$\mathtt { b } =$ (ndata\*sxy-sx\*sy)/del;   
for (j ${ = } 0$ ;j<ndata;j $^ { + + }$ ) chisq $+ =$ (temp=y[j]-(a+b\*x[j]),temp\*temp);   
sigb $^ { + = }$ sqrt(chisq/del); The standard deviation will give some idea of   
b1=b; how big an iteration step to take.   
f1=rofunc(b1);   
if (sigb $>$ 0.0) { ${ \tt b 2 } = { \tt b } +$ SIGN(3.0\*sigb,f1); Guess bracket as $_ { 3 - \sigma }$ away, in the downhill dif2=rofunc(b2); rection known from f1. if ( $\ b 2 \ = =$ b1) { abdev $/ =$ ndata; return; } while (f1\*f2 > 0.0) { Bracketing. b=b2+1. $^ { 6 * }$ (b2-b1); b1=b2; f1=f2; $mathtt { b 2 = b }$ ; f2=rofunc(b2); } sigb $\scriptstyle 1 = 0$ .01\*sigb; while (abs(b2-b1) $>$ sigb) { b=b1+0.5\*(b2-b1); Bisection. if (b $= =$ b1 || b $= =$ b2) break; f=rofunc(b); if (f\*f1 >= 0.0) { f1=f; $\mathtt { b 1 } = \mathtt { b }$ ; } else { $\mathtt { f } 2 \mathtt { = } \mathtt { f }$ ; $mathtt { b 2 = b }$ ; } }   
}   
abdev /= ndata;   
Doub rofunc(const Doub b) {   
Evaluates the right-hand side of equation (15.7.16) for a given value of b. const Doub EPS=numeric_limits<Doub>::epsilon(); Int j; Doub d,sum $_ { 1 = 0 }$ .0;

VecDoub arr(ndata); for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<ndata; ${ \dot { \bf { j } } } ^ { + + }$ ) arr[j]=y[j]-b\*x[j]; if ((ndata & 1) $\scriptstyle \mathbf { \mu = } \mathbf { \mu 1 }$ ) { a=select((ndata-1)>>1,arr); } else { j=ndata >> 1; $\mathtt { a } = 0 \mathtt { , } 5 \ast$ (select(j-1,arr)+select(j,arr)); abdev=0.0; for (j=0;j<ndata;j++) { d=y[j]-(b\*x[j]+a); abdev $+ =$ abs(d); if (y[j] $\ ! =$ 0.0) d /= abs(y[j]); if (abs(d) $>$ EPS) sum $+ =$ (d >= 0.0 ? x[j] : -x[j]); return sum; } };

# 15.7.4 Other Robust Techniques

Sometimes you may have a priori knowledge about the probable values and probable uncertainties of some parameters that you are trying to estimate from a data set. In such cases you may want to perform a fit that takes this advance information properly into account, neither completely freezing a parameter at a predetermined value (as in Fitlin $\ S 1 5 . 4 )$ nor completely leaving it to be determined by the data set. The formalism for doing this is called “use of a priori covariances.”

A related problem occurs in signal processing and control theory, where it is sometimes desired to “track” (i.e., maintain an estimate of) a time-varying signal in the presence of noise. If the signal is known to be characterized by some number of parameters that vary only slowly, then the formalism of Kalman filtering tells how the incoming raw measurements of the signal should be processed to produce best parameter estimates as a function of time. For example, if the signal is a frequencymodulated sine wave, then the slowly varying parameter might be the instantaneous frequency. The Kalman filter for this case is called a phase-locked loop and is implemented in the circuitry of modern radio receivers [4,5].

# CITED REFERENCES AND FURTHER READING:

Huber, P.J. 1981, Robust Statistics (New York: Wiley).[1]   
Maronna, R., Martin, D., and Yohai, V. 2006, Robust Statistics: Theory and Methods (Hoboken, NJ: Wiley).[2]   
Launer, R.L., and Wilkinson, G.N. (eds.) 1979, Robustness in Statistics (New York: Academic Press).[3]   
Sayed, A.H. 2003, Fundamentals of Adaptive Filtering (New York: Wiley-IEEE).[4]   
Harvey, A.C. 1989, Forecasting, Structural Time Series Models and the Kalman Filter (Cambridge, UK: Cambridge University Press).[5]

# 15.8 Markov Chain Monte Carlo

In this section and the next we redress somewhat the imbalance, at this point, between frequentist and Bayesian methods of modeling. Like Monte Carlo integration, Markov chain Monte Carlo or MCMC is a random sampling method. Unlike Monte Carlo integration, however, the goal of MCMC is not to sample a multidimensional region uniformly. Rather, the goal is to visit a point $\mathbf { X }$ with a probability proportional to some given distribution function $\pi ( \mathbf { x } )$ . The distribution $\pi ( \mathbf { x } )$ is not quite a probability, because it is not necessarily normalized to have unity integral over the sampled region; but it is proportional to a probability.

Why would we want to sample a distribution in this way? The answer is that Bayesian methods, often implemented using MCMC, provide a powerful way of estimating the parameters of a model and their degree of uncertainty. A typical case is that there is a given set of data D, and that we are able to calculate the probability of the data set given the values of the model parameters $\mathbf { X }$ , that is, $P ( { \bf D } | { \bf x } )$ . If we assume a prior $P ( \mathbf { x } )$ , then Bayes’ theorem says that the (posterior) probability of the model is proportional to $\pi ( \mathbf { x } ) \equiv P ( \mathbf { D } | \mathbf { x } ) P ( \mathbf { x } )$ , but with an unknown normalizing constant. Because of this unknown constant, $\pi ( \mathbf { x } )$ is not a normalized probability density. But if we can sample from it, we can estimate any quantity of interest, for example its mean or variance. Indeed, we can readily recover a normalized probability density by observing how often we sample a given volume $d \mathbf { x }$ . Often even more useful, we can observe the distribution of any single component or set of components of the vector $\mathbf { X }$ , equivalent to marginalizing (i.e., integrating over) the other components.

We could in principle obtain all the same information by ordinary Monte Carlo integration over the region of interest, computing the value of $\pi ( \mathbf { x } _ { i } )$ at every (uniformly) sampled point $\mathbf { X } _ { i }$ . The huge advantage of MCMC is that it “automatically” puts its sample points preferentially where $\pi ( \mathbf { x } )$ is large (in fact, in direct proportion). In a high-dimensional space, or where $\pi ( \mathbf { x } )$ is expensive to compute, this can be advantageous by many orders of magnitude.

Two insights, originally due to Metropolis and colleagues in the early 1950s, lead to feasible MCMC methods. The first is the idea that we should try to sample $\pi ( \mathbf { x } )$ not via unrelated, independent points, but rather by a Markov chain, a sequence of points $\mathbf { x } _ { 0 } , \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots$ that, while locally correlated, can be shown to eventually visit every point $\mathbf { X }$ in proportion to $\pi ( \mathbf { x } )$ , the ergodic property. Here the word “Markov” means that each point $\mathbf { X } _ { i }$ is chosen from a distribution that depends only on the value of the immediately preceding point $\mathbf { X } _ { i - 1 }$ . In other words, the chain has memory extending only to one previous point and is completely defined by a transition probability function of two variables $p ( \mathbf { x } _ { i } | \mathbf { x } _ { i - 1 } )$ , the probability with which $\mathbf { X } _ { i }$ is picked given a previous point $\mathbf { X } _ { i - 1 }$ .

The second insight is that if $p ( \mathbf { x } _ { i } | \mathbf { x } _ { i - 1 } )$ is chosen to satisfy the detailed balance equation,

$$
\pi ( \mathbf { x } _ { 1 } ) p ( \mathbf { x } _ { 2 } | \mathbf { x } _ { 1 } ) = \pi ( \mathbf { x } _ { 2 } ) p ( \mathbf { x } _ { 1 } | \mathbf { x } _ { 2 } )
$$

then (up to some technical conditions) the Markov chain will in fact sample $\pi ( \mathbf { x } )$ ergodically. This amazing fact is worthy of some contemplation. Equation (15.8.1) expresses the idea of $p$ hysical equilibrium in the reversible transition

$$
{ \bf x } _ { 1 } \longleftrightarrow { \bf x } _ { 2 }
$$

That is, if $\mathbf { X } _ { 1 }$ and $\mathbf { X } _ { 2 }$ occur in proportion to $\pi ( \mathbf { x } _ { 1 } )$ and $\pi ( \mathbf { x } _ { 2 } )$ , respectively, then the overall transition rates in each direction, each the product of a population density and a transition probability, are the same. To see that this might have something to do with the Markov chain being ergodic, integrate both sides of equation (15.8.1) with

respect to $\mathbf { X } _ { 1 }$ :

$$
\int p ( \mathbf { x } _ { 2 } | \mathbf { x } _ { 1 } ) \pi ( \mathbf { x } _ { 1 } ) d \mathbf { x } _ { 1 } = \pi ( \mathbf { x } _ { 2 } ) \int p ( \mathbf { x } _ { 1 } | \mathbf { x } _ { 2 } ) d \mathbf { x } _ { 1 } = \pi ( \mathbf { x } _ { 2 } )
$$

The left-hand side of equation (15.8.3) is the probability of $\mathbf { X } _ { 2 }$ , computed by integrating over all possible values of $\mathbf { X } _ { 1 }$ with the corresponding transition probability. The right-hand side is seen to be the desired $\pi ( \mathbf { x } _ { 2 } )$ . So equation (15.8.3) says that if $\mathbf { X } _ { 1 }$ is drawn from $\pi$ , then so is its successor in the Markov chain, $\mathbf { X } _ { 2 }$ .

We also need to show that the equilibrium distribution is rapidly approached from any starting point $\mathbf { X } _ { 0 }$ . While the formal proof is beyond our scope, a heuristic proof is to recognize that, because of ergodicity, even very unlikely values $\mathbf { X } _ { 0 }$ will be visited by the equilibrium Markov chain once in a great while. Since the chain has no past memory, choosing any such point as a starting point $\mathbf { X } _ { 0 }$ is equivalent to just picking up the equilibrium distribution chain at that particular point in time, q.e.d. In practice we need to recognize that when we start from a very unlikely point, successor points will themselves be quite unlikely until we rejoin a more probable part of the distribution. There is thus a need to burn-in an MCMC chain by stepping through, and discarding, a certain number of points $\mathbf { X } _ { i }$ . Below, we discuss how to determine the length of the burn-in.

We can gain a better understanding the nature of the approach to $\pi$ using concepts from $\ S 1 1 . 0$ and (in the next chapter) $\ S 1 6 . 3$ . Heuristically, let us pretend that the states $x _ { i }$ are discrete. Then $p ( x _ { j } | x _ { i } ) \ \equiv \ P _ { i j }$ is a transition matrix satisfying equation (16.3.1). The discussion following equation (16.3.4) shows that the matrix $\mathbf { P } ^ { T }$ must have at least one unity eigenvalue. In fact, the vector $\pi$ (the discrete form of the distribution $\pi ( \mathbf { x } )$ ) is an eigenvector of $\mathbf { P } ^ { T }$ with unity eigenvalue, by equation (15.8.3).

Can there be eigenvalues with magnitude greater than unity? No. Suppose to the contrary that $\lambda > 1$ is the largest eigenvalue, with eigenvector v. Then, repeatedly applying $\mathbf { P } ^ { T }$ ,

$$
\operatorname* { l i m } _ { n  \infty } \quad ( \mathbf { P } ^ { T } ) ^ { n } \cdot \mathbf { v } = \lambda ^ { n } \mathbf { v }  \infty \times \mathbf { v }
$$

Any starting distribution that contains even a tiny piece of $\mathbf { V }$ (always possible to arrange) will be driven to have values either $< 0$ or $> 1$ , which is impossible. Hence it must be that $\lambda \leq 1$ .

From an arbitrary starting distribution $\mathbf { u }$ , repeated steps of $\mathbf { P } ^ { T }$ must thus converge to $\pi$ geometrically, with a rate that is asymptotically the magnitude of the second-largest eigenvalue, which will be $< 1$ if $\pi$ is the unique equilibrium distribution. If the second eigenvalue is small, the distribution $p ( x _ { j } | x _ { i } )$ is said to be rapidly mixing.

Obviously missing from this discussion, and beyond our scope, is a discussion of degenerate eigenvalues (related to the question of uniqueness) and a continuous, rather than discrete, treatment. In practice, one rarely knows enough about $\mathbf { P }$ to compute useful bounds on the second eigenvalue a priori.

# 15.8.1 Metropolis-Hastings Algorithm

Unless we can find a transition probability function $p ( \mathbf { x } _ { 2 } | \mathbf { x } _ { 1 } )$ that satisfies the detailed balance equation (15.8.1), we have no way to proceed. Luckily, Hastings [1], generalizing Metropolis’ work, has given a very general prescription:

Pick a proposal distribution $q ( \mathbf { x } _ { 2 } | \mathbf { x } _ { 1 } )$ . This can be pretty much anything you want, as long as a succession of steps generated by it can, in principle, reach everywhere in the region of interest. For example, $q ( \mathbf { x } _ { 2 } | \mathbf { x } _ { 1 } )$ might be a multivariate normal distribution centered on $\mathbf { X } _ { 1 }$ .

Now, to generate a step starting at $\mathbf { X } _ { 1 }$ , first generate a candidate point $\mathbf { X } _ { 2 c }$ by drawing from the proposal distribution. Second, calculate an acceptance probability $\alpha ( \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 c } )$ by the formula

$$
\alpha ( \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 c } ) = \operatorname* { m i n } \left( 1 , \frac { \pi ( \mathbf { x } _ { 2 c } ) q ( \mathbf { x } _ { 1 } | \mathbf { x } _ { 2 c } ) } { \pi ( \mathbf { x } _ { 1 } ) q ( \mathbf { x } _ { 2 c } | \mathbf { x } _ { 1 } ) } \right)
$$

Finally, with probability $\alpha ( \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 c } )$ , accept the candidate point and set ${ \bf x } _ { 2 } = { \bf x } _ { 2 c }$ ; otherwise reject it and leave the point unchanged (that is, ${ \bf x } _ { 2 } = { \bf x } _ { 1 }$ ). The net result of this process is a transition probability,

$$
p ( \mathbf { x } _ { 2 } | \mathbf { x } _ { 1 } ) = q ( \mathbf { x } _ { 2 } | \mathbf { x } _ { 1 } ) \alpha ( \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } ) , \qquad ( \mathbf { x } _ { 2 } \neq \mathbf { x } _ { 1 } )
$$

To see how this satisfies detailed balance, first multiply equation (15.8.5) by the denominator in the second argument of the min function. Then write down the identical equation, but exchange $\mathbf { X } _ { 1 }$ and $\mathbf { X } _ { 2 }$ . From these pieces, one writes,

$$
\begin{array} { r l r } & { } & { \pi ( \mathbf { x } _ { 1 } ) q ( \mathbf { x } _ { 2 } | \mathbf { x } _ { 1 } ) \alpha ( \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } ) = \operatorname* { m i n } [ \pi ( \mathbf { x } _ { 1 } ) q ( \mathbf { x } _ { 2 } | \mathbf { x } _ { 1 } ) , \pi ( \mathbf { x } _ { 2 } ) q ( \mathbf { x } _ { 1 } | \mathbf { x } _ { 2 } ) ] } \\ & { } & { = \operatorname* { m i n } [ \pi ( \mathbf { x } _ { 2 } ) q ( \mathbf { x } _ { 1 } | \mathbf { x } _ { 2 } ) , \pi ( \mathbf { x } _ { 1 } ) q ( \mathbf { x } _ { 2 } | \mathbf { x } _ { 1 } ) ] } \\ & { } & { = \pi ( \mathbf { x } _ { 2 } ) q ( \mathbf { x } _ { 1 } | \mathbf { x } _ { 2 } ) \alpha ( \mathbf { x } _ { 2 } , \mathbf { x } _ { 1 } ) ~ } \end{array}
$$

which, using equation (15.8.6), can be seen to be exactly the detailed balance equation (15.8.1).

It is often possible to choose the proposal distribution $q ( \mathbf { x } _ { 2 } | \mathbf { x } _ { 1 } )$ in such a way as to simplify equation (15.8.5). For example, if $q ( \mathbf { x } _ { 2 } | \mathbf { x } _ { 1 } )$ depends only on the absolute difference $\left| \mathbf { x } _ { 1 } - \mathbf { x } _ { 2 } \right|$ , as in the case of a normal distribution with fixed covariance, then the ratio $q ( \mathbf { x } _ { 1 } | \mathbf { x } _ { 2 c } ) / q ( \mathbf { x } _ { 2 c } | \mathbf { x } _ { 1 } )$ is just 1. Another case that occurs frequently is when, for some component $x$ of $\mathbf { X }$ , $q ( x _ { 2 c } | x _ { 1 } )$ is lognormally distributed with a mode at $x _ { 1 }$ . In that case the ratio for this component is $x _ { 2 c } / x _ { 1 }$ (cf. equation 6.14.31).

# 15.8.2 Gibbs Sampler

An important special case of the Metropolis-Hastings algorithm is the Gibbs sampler. (Historically, the Gibbs sampler was developed independently of Metropolis-Hastings, see [2,5], but we discuss it here in a unified framework.) The Gibbs sampler is based on the fact that a multivariate distribution is uniquely determined by the set of all of its full conditional distributions; but if you don’t know what this means, just read on anyway.

A full conditional distribution of $\pi ( \mathbf { x } )$ is obtained by holding all of the components of x constant except one (call it $x$ ), and then sampling as a function of $x$ alone. In other words, it is the distribution that you see when you “drill through” $\pi ( \mathbf { x } )$ along a coordinate direction, and with fixed values of all the other coordinates. We’ll denote a full conditional distribution by the notation $\pi ( x \mid \mathbf { x } ^ { - } )$ , where $\mathbf { x } ^ { - }$ means “values of all the coordinates except one.” (To keep the notation readable, we are suppressing an index $i$ that would tell which component of $\mathbf { X }$ is $x$ .)

Suppose that we construct a Metropolis-Hastings chain that allows only the one coordinate $x$ to vary. Then equation (15.8.5) would look like this:

$$
\alpha ( x _ { 1 } , x _ { 2 c } | \mathbf { x } ^ { - } ) = \operatorname* { m i n } \left( 1 , \frac { \pi ( x _ { 2 c } | \mathbf { x } ^ { - } ) q ( x _ { 1 } | x _ { 2 c } , \mathbf { x } ^ { - } ) } { \pi ( x _ { 1 } | \mathbf { x } ^ { - } ) q ( x _ { 2 c } | x _ { 1 } , \mathbf { x } ^ { - } ) } \right)
$$

Now let’s pick as our proposal distribution,

$$
q ( x _ { 2 } | x _ { 1 } , \mathbf { x } ^ { - } ) = \pi ( x _ { 2 } | \mathbf { x } ^ { - } )
$$

Look what happens: The second argument of the min function becomes 1, so the acceptance probability $\alpha$ is also 1. In other words, if we propose a value $x _ { 2 }$ from the full conditional distribution $\pi ( x _ { 2 } | \mathbf { x } ^ { - } )$ , we can always accept it. The advantage is obvious. The disadvantage is that the full conditional distribution must be properly normalized as a probability distribution — otherwise how could we use it as a transition probability? Thus, we will usually need to calculate (either analytically or by numerical integration) the normalizing constant

$$
\int \pi ( x | \mathbf x ^ { - } ) d x
$$

for every $\mathbf { x } ^ { - }$ of interest, and we will need to have a practical algorithm for drawing $x _ { 2 }$ from the thus-normalized distribution. Note that these one-dimensional normalizing constants are much easier to compute than would be the multidimensional normalizing constant for the whole distribution $\pi ( \mathbf { x } )$ .

The full Gibbs sampler operates as follows: Cycle through each component of $\mathbf { X }$ in turn. (A fixed cyclical order is usually used, but choosing a component randomly each time is also fine.) For each component, hold all the other components fixed and draw a new value $x$ from the full conditional distribution $\pi ( x \mid \mathbf { x } ^ { - } )$ of all possible values of that component. (This is where you might have to do a numerical integral at each step.) Set the component to the new value and go on to the next component.

You can see that the Gibbs sampler is “more global” than the regular Metropolis-Hastings algorithm. At each step, a component of $\mathbf { X }$ gets reset to a value completely independent of its previous value (independent, at least, in the conditional distribution). If we tried to get behavior like this with regular Metropolis-Hastings, by proposing really big multivariate normal steps, say, we would get nowhere, since the steps would be almost always rejected!

On the other hand, the need to draw from a normalized conditional distribution can be a real killer in terms of computational workload. Gibbs sampling can be recommended enthusiastically when the components of $\mathbf { X }$ have discrete, not continuous, values, and not too many possible values for each component. In that case the normalization is just a sum over not-too-many terms, and the Gibbs sampler can be very efficient. For the case of continuous variables, you are probably better off with regular Metropolis-Hastings, unless your particular problem admits to some fast, tricky way of getting the normalizations.

Don’t confuse the Gibbs sampler with the tactic of doing regular Metropolis-Hastings steps along one component at a time. For the latter, we restrict the proposal distribution to proposing a change in a single component, either randomly chosen or else cycling through all the components in a regular order. This is sometimes useful if it lets us compute $\pi ( \mathbf { x } )$ more efficiently (e.g., using saved pieces from the previous calculation on components that have not changed). What makes this not Gibbs is that we calculate an acceptance probability in the regular way, with equation (15.8.5) and the full distribution $\pi ( \mathbf { x } )$ , which need not be normalized.

# 15.8.3 MCMC: A Worked Example

A number of practical details regarding MCMC are best discussed in the context of a worked example:

At the beginning of an experiment, events occur Poisson randomly with a mean rate $\lambda _ { 1 }$ , but only every $k _ { 1 } t h$ event is recorded. Then, at time $t _ { c }$ , the mean rate changes to $\lambda _ { 2 }$ , but now only every $k _ { 2 } t h$ event is recorded. We are given the times $t _ { 0 } , \ldots , t _ { N - 1 }$ of the $N$ recorded events. Oh, by the way, the values $\lambda _ { 1 }$ , $\lambda _ { 2 } , k _ { 1 } , l$ $k _ { 2 }$ , and $t _ { c }$ are all unknown. We want to find them.

Let’s decompose the separate parts of the calculation into separate objects. First we need an object that represents the point $\mathbf { X }$ . Although we’ve been discussing $\mathbf { X }$ as if it were a vector, it can actually be a mixture of continuous, discrete, boolean, or any other kind of variable. In our example we have both continuous and discrete variables.

# struct State {

Worked MCMC example: Structure containing the components of $\mathbf { x }$

Doub lam1, lam2;   
Doub tc;   
Int k1, k2;   
Doub plog; $\lambda _ { 1 }$ and $\bar { \lambda } _ { 2 }$   
$t _ { c }$   
$k _ { 1 }$ and $k _ { 2 }$   
Set to $\log { P }$ by Plog, below.

State(Doub la1, Doub la2, Doub t, Int kk1, Int kk2) : lam1(la1), lam2(la2), tc(t), k1(kk1), k2(kk2) {} State() {};

};

The constructor is used to set initial values. (The plog variable is not part of $\mathbf { X }$ , but it will be used later.)

Next, we need an object for calculating $\pi ( \mathbf { x } ) = P ( \mathbf { D } | \mathbf { x } )$ , the probability of the data given the parameters. For our example, we need to use a couple of facts about Poisson processes: If a Poisson process has a rate $\lambda$ , then the waiting time to the $k$ th event is distributed as Gamma $( k , \lambda )$ , that is,

$$
p ( \tau | k , \lambda ) = \frac { \lambda ^ { k } } { ( k - 1 ) ! } \tau ^ { k - 1 } e ^ { - \lambda \tau }
$$

where $\tau = t _ { i + k } - t _ { i }$ . (Compare equation 6.14.41, and also $\ S 7 . 3 . 1 0$ .) The exponential distribution is a special case with $k = 1$ . Further, probabilities for non-overlapping intervals such as $t _ { i + k } - t _ { i }$ and $t _ { i + 2 k } - t _ { i + k }$ are independent. It follows that, for our example,

$$
P ( \mathbf { D } | \mathbf { x } ) = \prod _ { t _ { i } \leq t _ { c } } p ( t _ { i + 1 } - t _ { i } | k _ { 1 } , \lambda _ { 1 } ) \times \prod _ { t _ { i } > t _ { c } } p ( t _ { i + 1 } - t _ { i } | k _ { 2 } , \lambda _ { 2 } )
$$

where $p ( \tau | k , \lambda )$ is as given in (15.8.11), and where $t _ { i }$ is now the $i$ th recorded time. (In the words following equation 15.8.11, $t _ { i }$ was the $i$ th event whether recorded or not.)

Actually, as the amount of data gets large, $P ( { \bf D } | { \bf x } )$ is likely to over- or underflow, so it is best to calculate $\log { P }$ . It is important to make this calculation as efficient as possible, because it will be done at every step. Particularly important is to minimize the amount of looping over all the data points. In our example, if you take the logarithm of equations (15.8.11) and (15.8.12), you’ll see that the individual $t _ { i }$ ’s enter into $\log { P }$ only as a sum of intervals and sum of log of intervals, less than and greater than $t _ { c }$ . An efficient way to proceed is thus to digest the data once and store two cumulative sums. Then, given a value $t _ { c }$ , we can find our place in the table of sums by bisection and read off the left and right sums directly. There is thus no loop over the data at all! Life is rarely so good, but when it is, then carpe diem. The resulting object looks like this:

# struct Plog {

Functor that calculates $\log { P }$ of a State. VecDoub &dat; Int ndat; VecDoub stau, slogtau;

Bind to data vector.

Plog(VecDoub &data) : dat(data), ndat(data.size()),   
stau(ndat), slogtau(ndat)   
Constructor. Digest the data vector for subsequent fast calculation of $\log { P }$ . The data are   
assumed to be sorted in ascending order. Int i; stau[0] $=$ slogtau[0] $\mathit { \Theta } = \mathit { \Theta } 0 .$ ; for ( $\dot { 1 } = 1$ ;i<ndat; $\dot { \bf 1 } + +$ ) { stau[i] $=$ dat[i]-dat[0]; Equal to sum of intervals. slogtau[i] $=$ slogtau[i-1] $^ +$ log(dat[i]-dat[i-1]); }   
}

Doub operator() (State &s) { Return log $P$ of s, and also set s.plog. Int i,ilo,ihi,n1,n2; Doub st1,st2,stl1,stl2, ans; ilo $\mathit { \Theta } = \mathit { \Theta } 0$ ; ihi $=$ ndat-1; while (ihi-ilo>1) { Bisection to find where is $t _ { c }$ in the data. $\begin{array} { r l } { \dot { \bf \lambda } _ { 1 } } & { { } = } \end{array}$ (ihi+ilo) >> 1; if (s.tc $>$ dat[i]) ilo ${ \boldsymbol { = } } { \dot { \boldsymbol { \bot } } }$ ; else ihi ${ \bf = } \dot { \bf 1 }$ ; } $\mathrm { ~ \tt ~ { ~ n ~ 1 ~ } ~ } =$ ihi; $\mathtt { n 2 } \ =$ ndat-1-ihi; st1 $=$ stau[ihi]; st2 $=$ stau[ndat-1]-st1; stl1 $=$ slogtau[ihi]; stl2 $=$ slogtau[ndat-1]-stl1; Equations (15.8.11) and (15.8.12): ans $=$ n1\*(s.k1\*log(s.lam1)-factln(s.k1-1))+(s.k1-1)\*stl1-s.lam1\*st1; ans $\scriptstyle + = \ \mathtt { n } 2 *$ (s.k2 $^ *$ log(s.lam2)-factln(s.k2-1))+(s.k2-1)\*stl2-s.lam2\*st2; return (s.plog $=$ ans); } };

The Plog object is the only place that the data enter, and they enter only through the constructor. All other parts of the calculation see the data only through the calculation of $\log { P }$ .

Next we come to the proposal generator, which we call Proposal. It doesn’t have any contact with the data, or with $\log { P }$ . All it needs to know about is the domain of $\mathbf { X }$ (that is, State). It is worth thinking hard about the proposal generator. Although “almost any” generator will work in theory, a poor generator will take longer than the age of the universe to converge, while a good, rapidly mixing generator can go like lightning. This is where MCMC starts becoming an art.

Our example is designed to furnish an illustration of this in the interaction between the $\lambda$ parameters and their corresponding $k$ ’s. The mean rate of recorded counts is $\lambda / k$ . Since $\lambda$ is a continuous variable, we will be proposing relatively small changes in it at each step. Since $k$ is discrete, there is no such thing as a small change, especially when $k$ is small.

If we naively write a generator that proposes random independent changes in $\lambda$ and $k$ , then, after we have settled down to roughly the right value of $\lambda / k$ , essentially all proposals for changing $k$ will be rejected. The reason is that the acceptable step in $\lambda$ required for a change in $k$ from 1 to 2 (say) is so large (doubling $\lambda$ ) that our generator will pick it only, say, every billion years! If we are not smart enough to recognize this problem ahead of time, we can find it experimentally by inspecting the Markov chain as it evolves and noting the proposals to change $k$ are never accepted.

A solution in our case is to have two kinds of steps. The first changes $\lambda$ (by a small amount) and keeps $k$ fixed. The second changes $k$ and $\lambda$ , keeping $\lambda / k$ fixed. We choose randomly between the two kinds of steps, mostly choosing the first kind.

The general issue here is what to do when $\pi ( \mathbf { x } )$ defines some highly correlated directions among the components in $\mathbf { X }$ . If you can recognize these directions, your proposal generator should, at least sometimes, generate proposals along them. Otherwise, it will have to propose very small steps, if they are ever to be accepted. In our example, this latter choice was made impossible by the discreteness in $k$ , forcing us to diagnose and confront the issue directly. So, although Proposal doesn’t directly have to know about $\log { P }$ , you may need a qualitative understanding of $\log { P }$ when you design Proposal.

Since only Proposal knows the algorithm by which a proposal is generated, this object must also calculate, and return, the ratio $q ( \mathbf { x } _ { 1 } | \mathbf { x } _ { 2 c } ) / q ( \mathbf { x } _ { 2 c } | \mathbf { x } _ { 1 } )$ , which is needed in equation (15.8.5). Here is an example that proposes small lognormal steps for the variables $\lambda _ { 1 }$ , $\lambda _ { 2 }$ , and $t _ { c }$ , or else proposes incrementing $k _ { 1 }$ and $k _ { 2 }$ by $1 , 0$ , or $^ { - 1 }$ , with corresponding changes in the $\lambda$ ’s as described above.

# struct Proposal {

Functor implementing the proposal distribution. Normaldev gau; Doub logstep;

Proposal(Int ranseed, Doub lstep) : gau(0.,1.,ranseed), logstep(lstep) {} void operator() (const State &s1, State &s2, Doub &qratio) { Given state s1, set state s2 to a proposed candidate. Also set qratio to $q ( \mathbf { s } 1 | \mathbf { s } 2 ) / q ( \mathbf { s } 2 | \mathbf { s } 1 )$ .

Doub r=gau.doub();   
if $\mathbf { \chi } _ { \mathbf { \chi } } ( \mathbf { \chi } _ { \mathbf { \chi } } ) = \mathbf { \chi } _ { 0 . 9 }$ ) { Lognormal steps holding the $k$ ’s constant. s2.lam1 $=$ s1.lam1 $^ *$ exp(logstep\*gau.dev()); s2.lam2 $=$ s1.lam2 $^ *$ exp(logstep\*gau.dev()); s2.tc $=$ s1.tc $^ *$ exp(logstep\*gau.dev()); s2.k1 $=$ s1.k1; s2.k2 $=$ s1.k2; qratio $=$ (s2.lam1/s1.lam1)\*(s2.lam2/s1.lam2)\*(s2.tc/s1.tc); Factors for lognormal steps.   
} else { Steps that change $k _ { 1 }$ and/or $k _ { 2 }$ . r=gau.doub();   
if (s1.k1>1) { if $( x < 0$ .5) s2.k1 $=$ s1.k1; else if $_ { x < 0 . 7 5 }$ ) s2. $\mathbf { k } \mathbf { 1 } \ = \ \mathbf { s } \mathbf { 1 } . \mathbf { k } \mathbf { 1 } \ +$ 1; else s2.k1 $=$ s1.k1 - 1;   
} else { $k _ { 1 } = 1$ requires special treatment. if (r<0.75) s2.k1 $=$ s1.k1; else s2.k1 $=$ s1.k1 + 1;   
s2.lam1 $=$ s2.k1\*s1.lam1/s1.k1;   
r=gau.doub(); Now all the same for $k _ { 2 }$ .   
if (s1.k2>1) { if $( x < 0$ .5) s2.k2 $=$ s1.k2; else if ( $x { < } 0 . 7 5$ ) $\mathbf { s } 2 \mathbf { \cdot } \mathbf { k } 2 \mathbf { \ } = \mathbf { \ s } 1 \mathbf { \cdot } \mathbf { k } 2 \mathbf { \ } + \mathbf { \ } 1$ ; else s2.k2 $=$ s1.k2 - 1;   
} else { if (r<0.75) s2.k2 $=$ s1.k2; else s2.k2 $=$ s1.k2 + 1;   
}   
s2.lam2 $=$ s2.k2\*s1.lam2/s1.k2;   
s2.tc $=$ s1.tc;   
qratio $= ~ 1$ .;

(We use the convenient fact that since Normaldev is derived from Ran, it contains both normal and uniform random number generators.)

How shall we set logstep, the size of the proposed lognormal step? A rule of thumb for proposals like this with an adjustable scale is that the average acceptance probability ought to be roughly between 0:1 and 0:4. If it is very much smaller, then decrease the step size parameter; if it is much larger, then increase the step size parameter. In our example, the value logstep $= 0 . 0 1$ (i.e., proposed changes on the order of $\pm 1 \%$ ) gives good results.

Finally, there is a function that takes a specified number of steps, implementing equation (15.8.5). This short piece of code is about the only “universal” part of MCMC; it has no persistent state and gets all the information it needs via the State, Plog, and Proposal structures. As we have seen, these are all problem-dependent and benefit from cleverness and special tricks.

# mcmc.h

Doub mcmcstep(Int m, State &s, Plog &plog, Proposal &propose) { Take m MCMC steps, starting with (and updating) s.

State sprop; Storage for candidate.   
Doub qratio,alph,ran;   
Int accept ${ = } 0$ ;   
plog(s);   
for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<m;i++) { Loop over steps. propose(s,sprop,qratio); alph $=$ min(1.,qratio\*exp(plog(sprop)-s.plog)); Equation (15.8.5). ran $=$ propose.gau.doub(); if (ran $<$ alph) { Accept the candidate. s $=$ sprop; plog(s); accept++; }   
}   
return accept/Doub(m);

![](images/3cae564dbabcac5c511dacb4c92a234b604ebb5c3b30706a05bcf8156556eeaf.jpg)  
Figure 15.8.1. Evolution of model parameters $\lambda _ { 1 }$ , $\lambda _ { 2 }$ , and $t _ { C }$ as a function of Markov chain Monte Carlo step. In this example, the burn-in time is seen to be $\sim 1 0 0 0$ steps, after which the Markov chain explores the equilibrium distribution.

Let’s try it all out. We’ll assume $N = 1 0 0 0$ data points $t _ { i }$ and start $\mathbf { X }$ with the values $\lambda _ { 1 } = 1$ , $\lambda _ { 2 } = 3$ , $t _ { c } = 1 0 0$ , and $k _ { 1 } = k _ { 2 } = 1$ . (Secretly, we know that the data were generated using actual values $3 , 2 , 2 0 0 , 1 , 2$ ; respectively.) The random seed is 10102, and the lognormal stepsize is 0:01. We’ll take 1000 steps of burn-in, and thereafter store values after every 10 steps. Driver code in main for this run is

VecDoub times(1000); Fill the vector times here.   
State s(1.,3.,100.,1,1);   
Plog plog(times);   
Proposal propose(10102,.01);   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<1000;i++) accept $=$ mcmcstep(1,s,plog,propose); Burn-in.   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<10000;i++) { Production. accept $=$ mcmcstep(10,s,plog,propose); Save values, increment averages, etc., here.   
}

Figure 15.8.1 shows the evolution of the parameters $\lambda _ { 1 }$ , $\lambda _ { 2 }$ and $t _ { c }$ . During burnin, you can see the parameters heading toward equilibrium, mostly monotonically, but with the exception of $\lambda _ { 2 }$ , which goes rapidly toward the value 1, with the value $k \ = \ 1$ . These values indeed replicate the mean rate of the recorded data. Only when it is near convergence (around step 560), does the model discover that the $t _ { i }$ ’s greater than $t _ { c }$ don’t actually fit an exponential distribution $( k _ { 2 } ~ = ~ 1 )$ ) but $d o$ fit a gamma distribution with the same mean rate, but with $k _ { 2 } = 2$ (the correct answer). Had we not provided Proposal with a step that tests for this, we would likely have converged to a wrong answer. More precisely, we would have produced a model whose true burn-in time was, unknowably, a figurative billion years.

Figure 15.8.2 shows how $\lambda _ { 1 }$ and $\lambda _ { 2 }$ distribute themselves during $1 0 ^ { 5 }$ steps after step 1000. This is the payoff of MCMC: We learn not just about most likely parameter values, but also details about how well the parameters are determined by this particular data set. We could also have shown any joint distribution of interest, or computed any average quantity, for example

![](images/72c2588b387da8d6ad249084d8ce1bcb5cd607c26d1f70cbc679f8f618d89da2.jpg)  
Figure 15.8.2. After burn-in, the MCMC model is run for an additional $1 0 ^ { 5 }$ steps. Parameter values are saved every 10 steps, giving the histograms shown for parameters $\lambda _ { 1 }$ and $\lambda _ { 2 }$ . These histograms represent the inferred parameter values and their uncertainties. The model data were generated with parameters $\lambda _ { 1 } = 3$ and $\lambda _ { 2 } = 2$ . The inferred values for this particular sample of 1000 data points are seen to be about as accurate as should be expected from their uncertainties.

$$
\langle \lambda _ { 1 } \rangle = \frac { 1 } { n - k } \sum _ { i = k } ^ { n - 1 } ( \lambda _ { 1 } ) _ { i }
$$

Here $k = 1 0 0 0$ is the number of burn-in steps, which we reject; $n = k + 1 0 ^ { 5 }$ is the number of steps that are averaged; and $( \lambda _ { 1 } ) _ { i }$ denotes the value of $\lambda _ { 1 }$ at the $i$ th step. Sums like (15.8.13) are called ergodic averages.

Some remarks should be made about equation (15.8.13): One is allowed to average all steps, even though successive steps are not independent samples of $\pi ( \mathbf { x } )$ . One would also be allowed to include in the average only every mth step, where you choose $m$ to be greater than some empirically observed correlation time in the Markov chain. The latter is sometimes recommended as a means of estimating the standard error of $\left. \lambda _ { 1 } \right.$ , just as in Monte Carlo integration. (Compare equations 7.7.1 and 7.7.2.) Warning: Doing this in the context of a finite data set is often associated with conceptual error. While it is true that as $n  \infty$ , equation (15.8.13) does converge to a precise value, it is not true that this value has anything to do with the actual (population) value of $\lambda _ { 1 }$ . Rather, it is just the best apparent (sample) value of $\lambda _ { 1 }$ for this particular data set. The relation of this apparent value to the actual value has nothing to do with the standard error of $\left. \lambda _ { 1 } \right.$ , but is instead indicated by the width of the distribution of all the $( \lambda _ { 1 } ) _ { i }$ ’s.

Figure 15.8.2 illustrates this point well. By running the model for a long time, we could achieve beautifully precise distributions that have extremely well-converged means. But they would not be centered on the (here secretly known) true values 3 and 2. You should run an MCMC model only (i) long enough to be sure (or sure enough) that there was sufficient burn-in, and (ii) long enough to characterize distributions well enough that the error in mean quantities of interest is reasonably small compared with the observed dispersion of those quantities in the Markov chain.

# 15.8.4 Other Aspects of MCMC

We have said little about how to determine the necessary length of burn-in, other than to advise you to look at the output (which is always a good idea). There is in fact a large literature on this subject [2-4]. A number of so-called convergence diagnostic tools have been developed. The problem is that, even when you use these tools, you really must look at the output anyway; so their added value is often not large. It is always a good idea to have the length of burn-in be at least 1 or $2 \%$ of the total length of your run, which will be determined by the accuracy that you need in estimating model parameters. Keep in mind that it is easy to construct scary examples of distributions $\pi ( \mathbf { x } )$ full of false convergence traps. The more you know about your distribution, the better off you will be.

Multiple, independent Markov chains can be run to explore a single distribution $\pi ( \mathbf { x } )$ . On a single processor the only reason to do this would be to meet some unusual need for independent samples of the distribution. However, on machines with multiple processors, this is a natural way of achieving efficient parallelization.

We have assumed that the number of dimensions in $\mathbf { X }$ is fixed. It is possible to have models, however, in which the number of fitted parameters is itself a variable. These variable dimension models require special care in the design of proposal distributions that can step between different numbers of dimensions. See the paper by Phillips and Smith in [2] for an introduction.

# 15.8.5 Importance Sampling and MCMC

In $\ S 7 . 9$ we noted that the error in Monte Carlo integration could be reduced by importance sampling, where we write (in the notation of this section)

$$
I \equiv \int f ( \mathbf { x } ) d \mathbf { x } = \int { \frac { f ( \mathbf { x } ) } { p ( \mathbf { x } ) } } p ( \mathbf { x } ) d \mathbf { x }
$$

for an aptly chosen $p$ . We saw that the ideal $p$ would (i) resemble $f$ in functional form, cf. equation (7.9.6), and (ii) admit to a good method for sampling uniformly over $p ( \mathbf { x } ) d \mathbf { x }$ .

You might think that MCMC provides a great general-purpose way to sample over any $p$ and thus make importance sampling easy to implement in all cases. Unfortunately, no. The problem, once again (as for the Gibbs sampler), is the normalizing constant. MCMC’s great virtue is that it samples over a distribution $\pi ( \mathbf { x } )$ without requiring that it be normalized. If you ask what normalized probability distribution $p ( \mathbf { x } )$ is actually being sampled over, it is of course

$$
p ( \mathbf { x } ) = \frac { \pi ( \mathbf { x } ) } { \int \pi ( \mathbf { x } ) d \mathbf { x } }
$$

Equation (15.8.14) then becomes

$$
I \equiv \int f ( \mathbf { x } ) d \mathbf { x } = \int \pi ( \mathbf { x } ) d \mathbf { x } \ \times \ \int { \frac { f ( \mathbf { x } ) } { \pi ( \mathbf { x } ) } } p ( \mathbf { x } ) d \mathbf { x }
$$

The differential $p ( \mathbf { x } ) d \mathbf { x }$ can be sampled over by MCMC, knowing only $\pi ( \mathbf { x } )$ ; no problem. The $\pi ( \mathbf { x } )$ in the denominator of the integrand can also be readily computed. But we have, in general, no easy way to calculate that pesky normalizing constant, $\textstyle { \int } \pi ( \mathbf { x } ) d \mathbf { x }$ .

Sometimes, though not often, you can construct a function $\pi ( \mathbf { x } )$ that both resembles $f$ and also can be integrated analytically, so that the normalizing constant is knowable. Then, yes, by all means use MCMC to sample $\pi ( \mathbf { x } )$ . In this case the idea of recording only every mth step, after choosing $m$ large enough so that the points thus chosen are independent samples, is not a bad idea after all. In fact you’ll have to do this if you expect to use the error estimate in equation (7.9.3) as written.

Finally, if the integral that you really want is

$$
J \equiv { \frac { \int f ( \mathbf { x } ) \pi ( \mathbf { x } ) d \mathbf { x } } { \int \pi ( \mathbf { x } ) d \mathbf { x } } } = \int f ( \mathbf { x } ) p ( \mathbf { x } ) d \mathbf { x }
$$

with $f ( \mathbf { x } )$ and $\pi ( \mathbf { x } )$ both known (and $p ( \mathbf { x } )$ only implied), then MCMC is exactly what you need. It provides uniform samples over $p ( \mathbf { x } ) d \mathbf { x }$ , and no calculation of a normalizing constant is needed.

# CITED REFERENCES AND FURTHER READING:

Hastings, W.K. 1970, “Monte Carlo Sampling Methods Using Markov Chains and Their Applications,” Biometrika, vol. 57, pp. 97–109.[1]   
Gilks, W.R., Richardson, S., and Spiegelhalter, D.J., eds. 1996, Markov Chain Monte Carlo in Practice (Boca Raton, FL: Chapman & Hall/CRC), especially Chapter 1.[2]   
Gamerman, D. 1997, Markov Chain Monte Carlo: Stochastic Simulation for Bayesian Inference (London: Chapman & Hall). [3]   
Neal, R.M. 1993, “Probabilistic Inference Using Markov Chain Monte Carlo Methods,” Technical Report CRG-TR-93-1, Department of Computer Science, University of Toronto. Available at http://www.cs.toronto.edu/\~radford/ftp/review.pdf. [4]   
Casella, G., and George, E.I. 1992, “Explaining the Gibbs Sampler,” American Statistician, vol. 46, no. 3, pp. 167–174.[5]   
Tanner, M.A. 2005, Tools for Statistical Inference: Methods for the Exploration of Posterior Distributions and Likelihood Functions,3rd ed.(New York: Springer).   
Liu, J.S. 2002, Monte Carlo Strategies in Scientific Computing (New York: Springer).   
Beichl, I., and Sullivan, F. (eds.) 2006, Computing in Science and Engineering, special issue on Monte Carlo Methods, vol. 8, no. 2 (March/April), pp. 7–47.

# 15.9 Gaussian Process Regression

Some types of statistical models do not depend on knowing (or guessing) parameterized functional forms, and thus lie outside of the parameter-fitting paradigm that has thus far occupied our attention. As an alternative to assuming that our data have some functional form, we can assume that they have some statistical property. A common example is to assume that the data, viewed as an entire set, is drawn from some multivariate normal (Gaussian) distribution in a high-dimensional space. That distribution is allowed to have a complicated correlation structure: The individual data points are not assumed to be independent. We can then ask, given the data points that we observe, what are the most probable values for other quantities of interest, for example the values of variables at points other than the ones measured. Of course, as previously, we are also encouraged to ask not just about the most probable values, but about the whole distribution around the most probable values. This general scheme is called Gaussian process regression.

We have already met examples of Gaussian process regression twice before in this book, though under different names. In $\ S 3 . 7$ we discussed kriging as a multidimensional interpolation technique. Later, in $\ S 1 3 . 6$ , we discussed linear prediction, mostly in the context of one-dimensional data such as time series. Here we can usefully merge some of the ideas in those two sections.

As we presented it in $\ S 3 . 7$ , kriging was an interpolation, not a fitting, technique. This was evident from the facts that (i) the interpolated function output by the Krig object went exactly through the measured data points, and (ii) we never discussed how to input measurement errors. However, the Krig object’s constructor did have an argument err, introduced with the mysterious remark that you should leave it set to NULL until you read $\ S 1 5 . 9$ . Well, here we are!

We did incorporate measurement errors in $\ S 1 3 . 6$ , although they were there called noise. In particular, equations (13.6.6) and (13.6.7) can be used (after some change of notation and algebraic manipulation) to derive the appropriate generalization of equations (3.7.14) and (3.7.15) to the case where the measurements $y _ { i }$ , $i = 0 , \ldots , N - 1$ , have errors characterized by some covariance matrix $\pmb { \Sigma }$ . In most cases $\pmb { \Sigma }$ will be simply a diagonal matrix with elements $\sigma _ { i } ^ { 2 }$ , the squares of the individual errors. The answers are

$$
\widehat { y } _ { * } = \mathbf { V } _ { * } \cdot ( \mathbf { V } - \Sigma ^ { \prime } ) ^ { - 1 } \cdot \mathbf { Y }
$$

and

$$
\operatorname { V a r } ( \widehat { y } _ { * } ) = \mathbf { V } _ { * } \cdot ( \mathbf { V } - \Sigma ^ { \prime } ) ^ { - 1 } \cdot \mathbf { V } _ { * }
$$

where

$$
\pmb { \Sigma } ^ { \prime } \equiv \left( \begin{array} { l l } { \pmb { \Sigma } } & { 0 } \\ { 0 } & { 0 } \end{array} \right)
$$

That is, we simply subtract $\pmb { \Sigma }$ (suitably augmented by bordering zeros) from $\mathbf { V }$ (equation 3.7.13) before inverting the matrix. The argument err, input as the $\sigma _ { i }$ ’s (not squared), does this for the case of diagonal measurement errors. Note that err has type Doub\*. If your errors are stored in a VecDoub, then you’ll send &err[0] to the Krig constructor. (Sorry about this hack. The purpose was to make NULL a possible default value.)

So, no new code is needed in this section. In Krig, you already have a serviceable multidimensional Gaussian process regression fitting routine, all ready to go.

When you are fitting, rather than interpolating, it is a good idea to pay more attention to the choice of variogram model than we did in $\ S 3 . 7$ . While for simple applications there is nothing wrong with the power-law model implemented in the Powvargram object

$$
v ( r ) = \alpha r ^ { \beta }
$$

several other models are widely used. These include the exponential model,

$$
v ( r ) = b [ 1 - \exp ( - r / a ) ]
$$

the spherical model,

$$
v ( r ) = { \left\{ \begin{array} { l l } { b \left( { \frac { 3 } { 2 } } { \frac { r } { a } } - { \frac { 1 } { 2 } } { \frac { r ^ { 3 } } { a ^ { 3 } } } \right) \qquad } & { 0 \leq r \leq a } \\ { b \qquad } & { a \leq r } \end{array} \right. }
$$

and various anisotropic models for which $v ( \mathbf { r } )$ is not just a function of the magnitude $r$ . See [1,2] for derivations and examples.

We should also mention the so-called nugget effect, though, in our opinion, its name vastly outshines its utility. If $v ( \mathbf { r } )$ does not go to zero as $\mathbf r  0$ , but instead goes to some constant $v _ { 0 }$ , then the resulting variogram describes a distribution that decorrelates by some finite amount in an infinitesimal distance. That is, if you find a gold nugget at location $\mathbf { X }$ , there is no certainty that you’ll find another one at location $\mathbf { x } + \delta \mathbf { x }$ , no matter how small you make $\displaystyle { \delta \mathbf { x } }$ . Some practitioners deem it desirable to allow for a nonzero nugget effect, allowing nonzero values of $v _ { 0 }$ when they empirically fit $v ( r )$ from a data set. That seems debatable to us; but in deference to such opinion we have given the Powvargram constructor an otherwise undocumented argument, nug, for feeding in the value $v _ { 0 }$ of your choice. (We draw the line at actually fitting for such a parameter!)

Beyond debatable, and actually incorrect, however, is to confuse the nugget effect with the effect of measurement error. They seem superficially similar: Measurement error also decorrelates measured values, even at arbitrarily small distances (even zero). Conceptually, and mathematically, however, they are different. Referring to equation (3.7.13), a nugget effect adds a constant positive value to all the off-diagonal $v _ { i j }$ ’s. Measurement errors, on the other hand, subtract (not necessarily constant) negative values from the diagonal $v _ { i i }$ ’s. These actions do not have equivalent effects on equations (3.7.14) and (3.7.15). This can readily be seen in Figure 15.9.1, which may also help elucidate the difference between kriging interpolation and kriging fitting. Only panel (d) in the figure shows a correct use of kriging for data with measurement errors, that is, kriging fitting with errors $\sigma _ { i }$ . Panels (b) and (c) show the results of kriging interpolation with and without a nugget effect. One sees that even with a positive nugget, the interpolated curve goes exactly through the data points, which is incorrect when measurement errors are significant. The legitimate use of kriging interpolation (as in $\ S 3 . 7 )$ is for smooth functions that are “exactly” known at scattered points. Kriging fits using $\sigma _ { i }$ ’s (this section) are for data with errors.

# CITED REFERENCES AND FURTHER READING:

Cressie, N. 1991, Statistics for Spatial Data (New York: Wiley).[1]   
Wackernagel, H. 1998, Multivariate Geostatistics, 2nd ed. (Berlin: Springer).[2]   
Isaaks, E.H., and Srivastava, R.M. 1989, Applied Geostatistics (New York: Oxford University Press).   
Rasmussen, C.E., and Williams, C.K.I. 2006, Gaussian Processes for Machine Learning (Cambridge, MA: MIT Press).   
Rybicki, G.B., and Press, W.H. 1992, “Interpolation, Realization, and Reconstruction of Noisy, Irregularly Sampled Data,” Astrophys. J., vol. 398, pp. 169–176.   
Deutsch, C.V., and Journel, A.G. 1992, GSLIB: Geostatistical Software Library and User’s Guide (New York: Oxford University Press).

![](images/43ddb36d27570c652e3b6de45e042ca8aafbd47d668c18f93a7223bb4d7b7fc5.jpg)  
Figure 15.9.1. One-dimensional examples of interpolation and fitting by kriging. (a) Synthetic data points generated from the known curve (dashed line) with Gaussian errors (r.m.s. magnitude 0.1). (b) Result of kriging interpolation. Equation (3.7.14) is plotted as the solid line, while the $_ { 1 - \sigma }$ estimated interpolation errors (3.7.15) are shown as the shaded band. The interpolation error is seen to be meaningless for data with measurement errors. (c) Same as (b), but with a nugget effect of 0:1. (d) Result of kriging fit (equations 15.9.1 and 15.9.2) using the actual measurement errors. This is the correct use of kriging for data with errors.

# Classification and Inference

# 16.0 Introduction

This chapter groups together a selection of computational techniques whose common feature is that they treat problems of classification and inference on complex models. Given substantially more space, the chapter might have been expanded to be a more complete survey of machine learning; but at its present length, it cannot pretend to be such. (A few general references are given below.)

Classification and inference, in a loose sense, are also the goals of many of the purely statistical methods that we already discussed in Chapters 14 and 15, and the line between such techniques and machine learning is a fuzzy one. This chapter’s topics tend to have one or both of two characteristics: the underlying model (i) has discrete or combinatorial aspects that distinguish it from “classical” statistical methods, and/or (ii) has empirical or heuristic aspects that make exact statistical treatments unattainable.

There is a list of important topics, related to those in this chapter, that we would have wanted to include if only they could have been reduced to suitable length. Bayesian networks is at the top of this list. Section 16.0.1 gives an example of the kind of problem that a Bayesian network can solve. Other significant topics that we must omit include

- genetic algorithms   
- neural nets   
- kernel methods more general than those discussed in $\ S 1 6 . 5$

# 16.0.1 Bayesian networks

These are sometimes called Bayes nets, Bayesian learning networks, or belief networks. Here we want only to give a flavor of the method, so that you will know when to consult the references below.

A Bayesian network consists of nodes, each of which can have a value. The values can be ftrue,falseg, or a set of possibilities like flow, medium, highg, or an integer. Figure 16.0.1 shows an example where all the nodes have true/false values.

![](images/8a6d0dcc11892301536f5ec633a058cb76b4a4399974cf79d22f9ee5060506bb.jpg)  
Figure 16.0.1. Example of a Bayesian network. Evidence about any node can be propagated to give probabilistic conclusions about any other node.

Each node in a network has a set of prior probabilities or priors that give the likelihood of its values absent any additional evidence. If a node has one or more parents, then its priors are conditioned on the values of the parents. For example, referring to the Figure, we might have

<table><tr><td>P(Illegally-Parked = true)</td><td></td></tr><tr><td>0.20</td><td></td></tr></table>

<table><tr><td>Bad-N&#x27;hood</td><td>P(Car-Stolen = true|Bad-N&#x27;hood)</td></tr><tr><td>true</td><td>0.05</td></tr><tr><td>false</td><td>0.001</td></tr></table>

<table><tr><td>Alzheimers</td><td>Drunk</td><td>P(Memory-Lapse = true |Alzheimers,Drunk)</td></tr><tr><td>true</td><td>true</td><td>0.999</td></tr><tr><td>true</td><td>false</td><td>0.95</td></tr><tr><td>false</td><td>true</td><td>0.50</td></tr><tr><td>false</td><td>false</td><td>0.01</td></tr></table>

And so on, for all the other nodes.

Things get interesting when we have some evidence to assimilate into the network. For example, you might be coming out of a bar in a bad neighborhood, walking with some difficulty, and be unable to find your car. Is it stolen? The Bayesian network theory gives algorithms for propagating information both up (from “Can’t find car?”) and down (from “Bad neighborhood?”) to get new posterior estimates for the probabilities at all nodes, including, here, “Car stolen?” You can also compute in advance the value of new evidence. For example, how much would it help to call the police and see if there is a police report of a towed or recovered, stolen, car?

For more than this brief taste, see [1-3].

# CITED REFERENCES AND FURTHER READING:

Hastie, T., Tibshirani, R., and Friedman, J.H. 2003, The Elements of Statistical Learning (Berlin: Springer).

Duda, R.O., Hart, P.E., and Stork, D.G. 2000, Pattern Classification, 2nd ed. (New York: Wiley).   
Witten, I.H., and Frank, E. 2005, Data Mining: Practical Machine Learning Tools and Techniques, 2nd ed. (San Francisco: Morgan Kaufmann).   
Mitchell, T.M. 1997, Machine Learning (New York: McGraw-Hill).   
Vapnik, V. 1998, Statistical Learning Theory (New York: Wiley).   
Russell, S., and Norvig, P. 2002, Artificial Intelligence: A Modern Approach, 2nd ed. (Upper Saddle River, NJ: Prentice-Hall).   
Haykin, S. 1998, Neural Networks: A Comprehensive Foundation, 2nd ed. (Upper Saddle River, NJ: Prentice-Hall).   
Bishop, C.M. 1996, Neural Networks for Pattern Recognition (New York: Oxford University Press).   
Korb, K.B., and Nicholson, A.E. 2004, Bayesian Artificial Intelligence (Boca Raton, FL: Chapman & Hall/CRC).[1]   
Neapolitan, R.E. 1990, Probabilistic Reasoning in Expert Systems (New York: Wiley).[2]   
Jensen, F.V. 2001, Bayesian Networks and Decision Graphs (New York: Springer).[3]

# 16.1 Gaussian Mixture Models and k-Means Clustering

Gaussian mixture models, so called, are one of the simplest examples of classification by unsupervised learning. They are also one of the simplest examples where solution by the $E M$ (expectation-maximization) algorithm proves highly successful.

Here is the setup: You are given $N$ data points in an $M$ -dimensional space, usually with $M$ in the range one to a few (say, three or four dimensions, tops). You want to “fit” the data, in this special sense: Find a set of $K$ multivariate Gaussian distributions that best represents the observed distribution of data points. The number $K$ is fixed in advance but the means and covariances of the distributions are unknown,

What makes the exercise “unsupervised” is that you are not told which of the $N$ data points come from which of the $K$ Gaussians. Indeed, one of the desired outputs is, for each data point $n$ , an estimate of the probability that it came from distribution number $k$ . This probability is denoted $P ( k | n )$ or $p _ { n k }$ , where (using a zero-based counting scheme) $0 \leq k < K$ and $0 ~ \leq ~ n ~ < ~ N$ . The matrix $p _ { n k }$ is sometimes called the responsibility matrix, because its entries indicate how much “responsibility” component $k$ has for data point $n$ .

Thus, given the data points, say as an $N \times M$ matrix whose rows are vectors of length $M$ , there are a whole bunch of parameters that we want to estimate:

$$
\begin{array} { r l } { \mu _ { k } \quad } & { ( \mathrm { t h e } K \mathrm { m e a n s , e a c h a v e c t o r o f l e n g t h } M ) } \\ { \Sigma _ { k } \quad } & { ( \mathrm { t h e } K \mathrm { c o v a r i a n c e m a t r i c e s , e a c h o f s i z e } M \times M ) } \\ { P ( k | n ) \equiv p _ { n k } \quad } & { ( \mathrm { t h e } K \mathrm { p r o b a b i l i t i e s } \mathrm { f o r e a c h o f } N \mathrm { d a t a p o i n t s } ) } \end{array}
$$

We will also get some additional estimates as by-products: $P ( k )$ denotes the fraction of all data points in component $k$ , that is, the probability that a data point chosen at random is in $k$ ; $P ( \mathbf { x } )$ denotes the probability (actually a probability density) of finding a data point at some position $\mathbf { X }$ , where $\mathbf { X }$ is the $M$ -dimensional position vector; and $\mathcal { L }$ denotes the overall likelihood of the estimated parameter set.

In fact, $\mathcal { L }$ is the key to the whole problem. $\mathcal { L }$ is defined, as usual, as proportional to the probability of the data set, given all the fitted parameters. We find the best values for the parameters by maximizing the likelihood $\mathcal { L }$ . You can also think of this as maximizing the posterior probability of the parameters, given uniform or very broad priors.

Let’s work backward from $\mathcal { L }$ . Since the data points are (assumed) independent, $\mathcal { L }$ is the product of the probabilities of finding a point at each observed position ${ \bf { X } } _ { n }$ ,

$$
\mathcal { L } = \prod _ { n } P ( \mathbf { x } _ { n } )
$$

We can split $P ( \mathbf { x } _ { n } )$ into its contribution from each of the $K$ Gaussians and write

$$
P ( \mathbf { x } _ { n } ) = \sum _ { k } N ( \mathbf { x } _ { n } \mid { \pmb \mu } _ { k } , { \pmb \Sigma } _ { k } ) P ( k )
$$

where $N ( \mathbf { x } \mid \pmb { \mu } , \pmb { \Sigma } )$ is the multivariate Gaussian density,

$$
N ( { \bf x } \mid { \pmb \mu } , { \pmb \Sigma } ) = \frac { 1 } { ( 2 \pi ) ^ { M / 2 } \operatorname* { d e t } ( { \pmb \Sigma } ) ^ { 1 / 2 } } \exp [ - \frac { 1 } { 2 } ( { \bf x } - { \pmb \mu } ) \cdot { \pmb \Sigma } ^ { - 1 } \cdot ( { \bf x } - { \pmb \mu } ) ]
$$

$P ( \mathbf { x } _ { n } )$ is sometimes called the mixture weight of the data point $\mathbf { X } _ { n }$ . We can “take apart” $P ( \mathbf { x } _ { n } )$ into its $K$ individual contributions, giving the individual probabilities

$$
p _ { n k } \equiv P ( k | n ) = \frac { N ( \mathbf { x } _ { n } | \pmb { \mu } _ { k } , \pmb { \Sigma } _ { k } ) P ( k ) } { P ( \mathbf { x } _ { n } ) }
$$

Equations (16.1.2) through (16.1.5) are a prescription for calculating $\mathcal { L }$ and the $p _ { n k }$ ’s, given the data, and given values for the $\pmb { \mu } _ { k }$ ’s, $\Sigma _ { k }$ ’s, and $P ( k )$ . In the language of the EM algorithm, this is called an expectation step or $E$ -step.

But how do we get the $\pmb { \mu } _ { k }$ ’s, $\Sigma _ { k }$ ’s, and $P ( k )$ ?

Suppose we knew the $p _ { n k }$ ’s. A familiar theorem for the one-dimensional Gaussian distribution is that the maximum likelihood estimate of its mean is just the arithmetic mean of a set of points drawn from it. This theorem straightforwardly generalizes to yield maximum likelihood estimates for the means, and covariance matrices, of multivariate Gaussians. A further small generalization is that, since we know only probabilistically whether a particular point is drawn from a particular Gaussian, we should count only the appropriate fraction $p _ { n k }$ of each point. These considerations result in the following maximum likelihood estimates:

$$
\begin{array} { l } { \displaystyle \widehat { \pmb { \mu } } _ { k } = \sum _ { n } p _ { n k } \mathbf { x } _ { n } \bigg / \sum _ { n } p _ { n k } } \\ { \displaystyle \widehat { \pmb { \Sigma } } _ { k } = \sum _ { n } p _ { n k } ( \mathbf { x } _ { n } - \widehat { \pmb { \mu } } _ { k } ) \otimes ( \mathbf { x } _ { n } - \widehat { \pmb { \mu } } _ { k } ) \bigg / \sum _ { n } p _ { n k } } \end{array}
$$

and, in a similar vein,

$$
\widehat { P } ( k ) = \frac { 1 } { N } \sum _ { n } p _ { n k }
$$

“Hats” here denote estimators; however, this is a notational nicety that we will henceforth ignore. Equations (16.1.6) and (16.1.7) are the so-called maximization step or $M$ -step of the EM algorithm.

What we have motivated thus far is that right at the maximum likelihood solution, both the E-step and the M-step relations will hold. That is, the maximum likelihood parameters are a stationary point for both E-steps and M-steps. The power of the EM algorithm derives from the more powerful theorem (beyond our scope to prove here) that, starting from any parameter values, an iteration of E-step followed by an M-step will increase the likelihood value $\mathcal { L }$ ; and that repeated iterations will converge to (at least a local) likelihood maximum. Often, happily, the convergence is to the global maximum.

The EM algorithm, in brief, is thus

- Guess starting values for the $\pmb { \mu } _ { k }$ ’s, $\Sigma _ { k }$ ’s, and fractions $P ( k )$ .   
- Repeat: An E-step to get new $p _ { n k }$ ’s and new $\mathcal { L }$ , followed by an M-step to get new $\pmb { \mu } _ { k }$ ’s, $\Sigma _ { k }$ ’s, and $P ( k )$ .   
- Quit when the value of $\mathcal { L }$ is no longer changing.

One important practical detail is that the values of the Gaussian density function will often be so small as to underflow to zero. It is therefore important to work with logarithms of these densities, rather than the densities themselves, e.g.,

$$
\log N ( { \mathbf x } \mid \mu , { \boldsymbol \Sigma } ) = - \frac { 1 } { 2 } ( { \mathbf x } - { \boldsymbol \mu } ) \cdot { \boldsymbol \Sigma } ^ { - 1 } \cdot ( { \mathbf x } - { \boldsymbol \mu } ) - \frac { M } { 2 } \log ( 2 \pi ) - \frac { 1 } { 2 } \log \operatorname* { d e t } ( { \boldsymbol \Sigma } )
$$

A problem arises with equation (16.1.3), where we need to take the sum of quantities, all of which may be so small as to underflow if ever reconstructed from their logarithms. The solution to this problem is the so-called log-sum-exp formula,

$$
\log \biggl ( \sum _ { i } \exp ( z _ { i } ) \biggr ) = z _ { \operatorname* { m a x } } + \log \biggl ( \sum _ { i } \exp ( z _ { i } - z _ { \operatorname* { m a x } } ) \biggr )
$$

where the $z _ { i }$ ’s are the logarithms that we are using to represent small quantities and $z _ { \mathrm { m a x } }$ is their maximum. Equation (16.1.9) guarantees that at least one exponentiation won’t underflow, and that any that do could have been neglected anyway.

Figure 16.1.1 shows an example of how the EM algorithm converges to a solution with 1000 two-dimensional data points and four components. As the number of data points increases, the topography of the likelihood space gets smoother, with fewer local minima, so that it becomes more and more likely that the global maximum will be found (as in this case).

You should always inspect an EM solution for reasonableness. If you are getting hung up on an unacceptable local maximum, one strategy is to do a series of independent runs, using $K$ randomly chosen data points as the starting means in each case. (Be sure that you don’t duplicate a data point in the starting guesses.) Then pick the best one, i.e., the one that converges to the largest log-likelihood.

Here is a structure that implements the EM algorithm for Gaussian mixture models, given only the data points and initial estimates of the means $\pmb { \mu } _ { k }$ . The constructor sets the problem up, and does one initial E-step and M-step. Thereafter, the user alternately calls the estep() and mstep() routines, until convergence is achieved, as signaled by the return value of estep(), the change in log-likelihood, becoming sufficiently small (say, $1 0 ^ { - 6 }$ ). The results are then available in the structure members means, resp, frac, and sig.

![](images/4629db071cb6f0b2ac73e49ac0a0523f816b66efdc38b36700b725620c914911.jpg)  
Figure 16.1.1. Example of a Gaussian mixture model in $M = 2$ dimensions, with $N = 1 0 0 0$ data points and $K = 4$ components. Left: Evolution of the estimated means and covariances, shown as 2- sigma ellipses. The ellipses are plotted after each iteration of an E-step and M-step (see text). Right: The converged result. The leftmost two components converged rapidly. The rightmost component took about 10 iterations to get to near-convergence; only after it had done so did the central component shrink down to a converged result.

# struct preGaumixmod {

For nonwizards, this is basically a typedev of Mat_mm as an $\mathtt { m m } \times \mathtt { m m }$ matrix. For wizards, what is going on is that we need to set a static variable mmstat before defining Mat_mm, and this must happen before the Gaumixmod constructor is invoked.

static Int mmstat; struct Mat_mm : MatDoub {Mat_mm() : MatDoub(mmstat,mmstat) {} }; preGaumixmod(Int mm) {mmstat $=$ mm;} }; Int preGaumixmod::mmstat $\ c = - 1$ ;

# struct Gaumixmod : preGaumixmod {

ve for a Gaussian mixture model from a set of data points and initial guesses of $k$ means.   
Int nn, kk, mm; Nos. of data points, components, and dimensions.   
MatDoub data, means, resp; Local copies of ${ \bf x } _ { n }$ ’s, ${ \pmb \mu } _ { k }$ ’s, and the ${ p } _ { n k }$ ’s.   
VecDoub frac, lndets; $P ( k )$ ’s and log det $\pmb { \Sigma } _ { k }$ ’s.   
vector<Mat_mm> sig; $\pmb { \Sigma } _ { k }$ ’s   
Doub loglike; $\log \mathcal { L }$ .   
Gaumixmod(MatDoub &ddata, MatDoub &mmeans) : preGaumixmod(ddata.ncols()),   
nn(ddata.nrows()), kk(mmeans.nrows()), mm(mmstat), data(ddata), means(mmeans),   
resp(nn,kk), frac(kk), lndets(kk), sig(kk) {   
Constructor. Arguments are the data points (as rows in a matrix) and initial guesses for   
the means (also as rows in a matrix). Int i,j,k; for $( \mathrm { k } = 0$ ;k<kk;k++) { frac[k] $= ~ 1$ ./kk; Uniform prior on $P ( k )$ . for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<mm; $\dot { \bf 1 } + +$ ) { for ( $\scriptstyle { \dot { \ j } } = 0$ ;j<mm;j++) sig[k][i][j] $\qquad = \ 0 .$ .; sig[k][i][i] $=$ 1.0e-10; See text at end of this section. } } estep(); Perform one initial E-step and M-step. User mstep(); is responsible for calling additional steps   
} until convergence is obtained.   
Doub estep() {   
Perform one E-step of the EM algorithm. Int k,m,n;   
Doub tmp,sum,max,oldloglike;   
VecDoub u(mm),v(mm);   
oldloglike $=$ loglike;   
for $\scriptstyle ( \mathtt { k } = 0$ ;k<kk;k++) { Outer loop for computing the ${ p } _ { n k }$ ’s. Cholesky choltmp(sig[k]); Decompose $\pmb { \Sigma } _ { k }$ in the outer loop. lndets[k] $=$ choltmp.logdet(); for $\scriptstyle \mathtt { n } = 0$ ;n<nn; $\mathbf { n } { + } +$ ) { Inner loop for ${ p } _ { n k }$ ’s. for ( $\scriptstyle { \mathtt { m } } = 0$ ;m<mm; $\mathrm { m } { + } { + }$ ) u[m] $=$ data[n][m]-means[k][m]; choltmp.elsolve(u,v); Solve $\mathbf { L } \cdot \mathbf { v } = \mathbf { u }$ . for (sum $_ { 1 = 0 }$ ., $\mathtt { m = 0 }$ ; $\mathtt { m } < \mathtt { m m }$ ; $\mathrm { m } { + + } \dot { } .$ ) sum $+ =$ SQR(v[m]); resp[n][k] $= - 0 . 5 *$ (sum $^ +$ lndets[k]) $^ +$ log(frac[k]); }

At this point we have unnormalized logs of the ${ p } _ { n k }$ ’s. We need to normalize using log-sum-exp and compute the log-likelihood. loglike $\mathit { \Theta } = \mathit { \Theta } 0$ ; for $( \mathtt { n } { = } 0 ; \mathtt { n } { < } \mathtt { n } \mathtt { n } ; \mathtt { n } { + } + )$ { Separate normalization for each n. max $=$ -99.9e99; Log-sum-exp trick begins here. for $\scriptstyle \mathtt { k } = 0$ ;k<kk;k++) if (resp[n][k] $>$ max) max $=$ resp[n][k]; for (sum $_ { = 0 }$ ., $\mathtt { k } = 0$ ; k<kk; $\mathrm { k } { + } { + } \mathrm { i }$ ) sum $+ =$ exp(resp[n][k]-max); tmp $=$ max $^ +$ log(sum); for $\scriptstyle \mathbf { k } = 0$ ;k<kk;k++) resp[n][k] $=$ exp(resp[n][k] - tmp); loglike $+ =$ tmp; } return loglike - oldloglike; When abs of this is small, then we have } converged. void mstep() { Perform one M-step of the EM algorithm. Int j,n,k,m; Doub wgt,sum; for (k=0;k<kk;k++) { wgt=0.; for $\scriptstyle \mathtt { n } = 0$ ;n<nn;n++) wgt $+ =$ resp[n][k]; frac[k] $=$ wgt/nn; Equation (16.1.7). for (m=0;m<mm;m++) { for (sum $_ { = 0 }$ ., $\mathtt { n } = 0$ ; n<nn; $\mathrm { n } { + } { + } \mathrm { i }$ ) sum $+ =$ resp[n][k]\*data[n][m]; means[k][m] $=$ sum/wgt; Equation (16.1.6). for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<mm;j++) { for (sum $_ { = 0 }$ ., $\scriptstyle \mathtt { n } = 0$ ; n<nn; n++) { sum $+ =$ resp[n][k] $^ *$ (data[n][m]-means[k][m])\*(data[n][j]-means[k][j]); sig[k][m][j] $=$ sum/wgt; Equation (16.1.6). } } } }

About the only place that Gaumixmod can fail algorithmically (as distinct from converging to a poor, local, solution) is by encountering a zero or negative diagonal element in the Cholesky decomposition. As a result, all sins tend to appear, sometimes confusingly, as exceptions at that point in the code. If you are getting such exceptions, here are some possibilities:

- You have duplicated vectors in your initial guesses for the $\pmb { \mu } _ { k }$ ’s. - One or more of your $\pmb { \mu } _ { k }$ ’s is so distant from all data points that it is not “attracting” enough of them to solve for the parameters of its component. Try using random data points as starting guesses, or reduce $K$ . You may just have too few data points $N$ to support a nondegenerate model with $K$ components. Reduce $K$ or get more data!

- Rarely, you might want to change the constant $1 . 0 { \mathsf { e } } ^ { - 1 0 }$ that initializes the diagonal components of $\Sigma _ { k }$ in the code. (See discussion under “K-Means Clustering,” below.) - You can reduce the number of parameters in $\pmb { \Sigma }$ , as we now discuss.

Occasionally data are too sparse, or too noisy, to give meaningful results for all the components of the covariance matrices $\Sigma _ { k }$ . In such cases, you can impose simpler covariance models by changing the re-estimation formulas for $\pmb { \Sigma }$ in equation (16.1.6). One step of simplification is to make $\pmb { \Sigma }$ diagonal, while still allowing different variances for the different dimensions. The re-estimation formula for the diagonal components of $\Sigma _ { k }$ is then

$$
( \widehat { \pmb { \Sigma } } _ { k } ) _ { m m } = \sum _ { n } p _ { n k } [ ( { \pmb x } _ { n } ) _ { m } - ( \widehat { \pmb { \mu } } _ { k } ) _ { m } ] ^ { 2 } \bigg / \sum _ { n } p _ { n k }
$$

where subscripts $m$ indicate that particular component of the vector. Set nondiagonal components of $\Sigma _ { k }$ to zero.

Even more drastic, we can replace $\pmb { \Sigma } _ { k }$ by a single scalar (that is, spherical) variance by using the re-estimation formula

$$
( \widehat { \boldsymbol { \Sigma } } _ { k } ) = \mathbf { 1 } \times \left( \sum _ { n } p _ { n k } | \mathbf { x } _ { n } - \widehat { \boldsymbol { \mu } } _ { k } | ^ { 2 } \Big / \sum _ { n } p _ { n k } \right)
$$

where 1 is the identity matrix.

We have not coded these options in Gaumixmod, but they are easy to add.

# 16.1.1 A Note on the Use of Cholesky Decomposition

It is worth remarking briefly on the use of Cholesky decomposition (-2.9) in this and similar manipulations of multivariate Gaussians.

In the Gaumixmod routine above, we need a way of inverting the covariance matrices — or, more precisely, an efficient way to compute expressions like y ${ \pmb { \Sigma } } ^ { - 1 }$ y . Because the covariance matrix $\pmb { \Sigma }$ is symmetric and positive-definite, the Cholesky decomposition, which has fewer operations than other methods, can be used, giving

$$
\boldsymbol { \Sigma } = \mathbf { L } \cdot \mathbf { L } ^ { T }
$$

where $\mathbf { L }$ is a lower triangular matrix, implying

$$
Q = \mathbf { y } \cdot \mathbf { \Sigma } \mathbf { \Sigma } ^ { - 1 } \cdot \mathbf { y } = \left| \mathbf { L } ^ { - 1 } \cdot \mathbf { y } \right| ^ { 2 }
$$

Since $\mathbf { L }$ is triangular, $\mathbf { L } ^ { - 1 } \cdot \mathbf { y }$ can be obtained efficiently by backsubstitution.

Another very convenient use for the decomposition (16.1.12) is in the mundane task of drawing error ellipses, as in Figure 16.1.1 (or, similarly, error ellipsoids in three dimensions). The locus of points $\mathbf { X }$ that are one standard deviation (“1-sigma”) away from the mean $\mu$ is given by

$$
1 = ( \mathbf { x } - { \pmb \mu } ) \cdot { \pmb \Sigma } ^ { - 1 } \cdot ( \mathbf { x } - { \pmb \mu } ) \quad \Rightarrow \quad \left| \mathbf { L } ^ { - 1 } \cdot ( \mathbf { x } - { \pmb \mu } ) \right| = 1
$$

Now suppose that $\mathbf { z }$ is a point on the unit circle (two dimensions) or unit sphere (three dimensions). Then, by substitution into equation (16.1.14), you can easily see that

$$
\mathbf { x } = \mathbf { L } \cdot \mathbf { z } + \pmb { \mu }
$$

![](images/f036016a84367c8aa886bf3c5372e2b14be5f98daf8533d43e321fd84c8ca2f7.jpg)  
Figure 16.1.2. Output of $\mathbf { k }$ -means clustering as applied to the same data as Figure 16.1.1, with $K = 6$ components. The final assignments are shown as different plotted symbols. The centers of the large circles are the locations of the final means. (The radius of those circles is arbitrary, for visibility only.) Unlike Gaussian mixture modeling, $\mathbf { k }$ -means clustering can’t split a point probabilistically between two components, so many points from the Gaussian at the upper left are mistakenly assigned to the central component. Also, k-means clustering needs more than one component to model a Gaussian with a large aspect ratio, because it clusters by radial distance.

is a point on the 1-sigma locus. Going around the unit circle in $\mathbf { z }$ , and using the mapping (16.1.15), gives the desired ellipse. Put a constant 2 in front of the $\mathbf { L }$ in (16.1.15) for 2-sigma ellipses, and so forth.

We already remarked, in $\ S 7 . 4$ , on the closely related use of Cholesky decomposition to generate multivariate Gaussian deviates from a given covariance matrix.

# 16.1.2 K-Means Clustering

One interesting simplification of Gaussian mixture modeling has an independent history and is known as $k$ -means clustering. We forget about the $\Sigma _ { k }$ covariances matrices completely, and we forget about probabilistic assignments of data points to components. Instead, each data point gets assigned to one (and only one) of the $K$ components.

The E-step is simply: Assign each data point $\mathbf { X } _ { n }$ to the component $k$ whose mean $\pmb { \mu } _ { k }$ it is closest to, by Euclidean distance.

The M-step is simply: For all $k$ , re-estimate the mean $\pmb { \mu } _ { k }$ as the average of data points ${ \bf { X } } _ { n }$ assigned to component $k$ .

The convergence criterion is: Stop when an E-step doesn’t change the assignment of any data point (in which case the M-step would also produce unchanged $\pmb { \mu } _ { k }$ ’s).

Interestingly, convergence is guaranteed — you can’t get into an infinite loop of, say, shifting a point back and forth between two components. Despite its simplicity, $\mathrm { k \Omega }$ -means clustering can be quite useful: It is very fast, and it converges very rapidly. It can be used as a method to reduce a large number of data points to a much smaller number of “centers,” which can then be used as starting points for more sophisticated methods.

For example, you might use $\mathrm { k }$ -means clustering to get starting values for a Gaussian mixture model that has difficulty converging to a good, global maximum. If $K$ is the ultimate number of components that you want, you might use $\mathbf { k }$ -means to get down to $\sim 3 \times K$ components, then (repeatedly) randomly select $K$ of these as starting guesses for the Gaussian model.

Be alert to the fact that $\mathrm { k \Omega }$ -means clustering has an intrinsically “spherical” view of the world, because of its Euclidean “nearest-to” assignments. If you have components that might have big aspect ratios, be sure to set $K$ large enough so that these can be represented by several different centers. Figure 16.1.2 shows the same input data as Figure 16.1.1, now clustered by $\mathbf { k }$ -means. The Gaussians at the lower left and right have broken up into two centers each. The Gaussian at the upper left is only a single component, because it has had many of its points misclassified into the central component. (A Gaussian mixture model would have assigned those points probabilistically to both components.)

Code for $\mathrm { k \Omega }$ -means classification is similar to, but much shorter than, the previous code for a Gaussian mixture model:

# struct Kmeans {

Solve for a $\mathsf { k }$ -means clustering model from a set of data points and initial guesses of the means.   
Output is a set of means and an assignment of each data point to one component. Int nn, mm, kk, nchg;   
MatDoub data, means;   
VecInt assign, count;   
Kmeans(MatDoub &ddata, MatDoub &mmeans) : nn(ddata.nrows()), mm(ddata.ncols()), kk(mmeans.nrows()), data(ddata), means(mmeans), assign(nn), count(kk) { Constructor. Arguments are the data points (as rows in a matrix), and initial guesses for the means (also as rows in a matrix). estep();   
mstep();

Perform one initial E-step and M-step. User is responsible for calling additional steps until convergence is obtained.

# Int estep() {

Perform one E-step. Int k,m,n,kmin; Doub dmin,d; nchg $\mathit { \Theta } = \mathit { \Theta } 0$ ; for ( $\scriptstyle \mathtt { k } = 0$ ;k<kk;k++) count[k] = 0; for $\scriptstyle \mathtt { . n = 0 }$ ;n<nn;n++) { dmin $=$ 9.99e99; for $\scriptstyle ( \mathtt { k } = 0$ ;k<kk; $\mathrm { k } { + + }$ ) { for ( $\scriptstyle \mathtt { d } = 0$ ., $\scriptstyle { \mathtt { m } } = 0$ ; m<mm; $\mathbb { m } { + + }$ ) d $+ =$ SQR(data[n][m]-means[k][m]); if (d $<$ dmin) {dmin $\mathit { \Theta } = \mathit { \Theta } \mathtt { d }$ ; kmin $\mathbf { \mu } = \mathbf { \mu } _ { \mathrm { \ k } } ;$ } } if (kmin ! $! =$ assign[n]) nchg++; assign[n] $=$ kmin; count[kmin] $^ { + + }$ ; return nchg;   
}   
void mstep() {   
Perform one M-step. Int n,k,m; for $( \mathrm { k } = 0$ ;k<kk;k++) for $\scriptstyle { \mathtt { m } } = 0$ ;m<mm;m++) means[k][m] $\mathit { \Theta } = \mathit { \Theta } 0 \ : .$ .; for ( $\scriptstyle 1 = 0$ ;n<nn;n++) for $\scriptstyle { \mathtt { m } } = 0$ ;m<mm;m++) means[assign[n]][m] $+ =$ data[n][m]; for (k=0;k<kk;k++) {

if (count[k] $> 0 \dot { }$ ) for $\scriptstyle ( { \mathtt { m } } = 0$ ;m<mm;m++) means[k][m] /= count[k]; } } };

Incidentally, $\mathbf { k }$ -means clustering is not only a simplification of Gaussian mixture models; it is actually a limiting case. If the $\pmb { \Sigma } _ { k }$ matrices are all held fixed as

$$
\pmb { \Sigma } _ { k } = \epsilon \pmb { 1 }
$$

with $\epsilon$ infinitesimal and 1 the identity matrix, then the component $k$ with mean closest to $\mathbf { X } _ { n }$ will be assigned all of the responsibility $p _ { n k }$ for that $n$ . The re-estimation of the $\pmb { \mu } _ { k }$ ’s then is identical to $\mathbf { k }$ -means clustering. The theorem that proves that the EM algorithm converges for Gaussian mixtures can easily be modified to prove the convergence of $\mathrm { k }$ -means clustering. (Basically, there is a hidden log-likelihood function that can be shown to increase at each step.)

Indeed, we can now explain the obscure constant $1 . 0 { \mathsf { e } } ^ { - 1 0 }$ in the initialization part of Gaumixmod: It is a value for $\epsilon$ that makes that routine’s first E-step, M-step iteration be one of k-means clustering.

# CITED REFERENCES AND FURTHER READING:

McLachlan, G. and Peel, D. 2000, Finite Mixture Models (New York: Wiley).

Moore, A.W. 2004, “Clustering with Gaussian Mixtures,” at http://www.cs.cmu.edu/\~awm.

Dempster, A.P., Laird, N.M., and Rubin, D.B. 1977, “Maximum Likelihood from Incomplete Data via the EM Algorithm,” Journal of the Royal Statistical Society, Series B, vol. 39, pp. 1-38. [The original paper on EM methods.]

Tanner, M.A. 2005, Tools for Statistical Inference: Methods for the Exploration of Posterior Distributions and Likelihood Functions,3rd ed. (New York: Springer).

# 16.2 Viterbi Decoding

In this section we discuss models with discrete states, and how to use data to estimate what state a model is in, or what succession of states it traverses by allowed transitions. By state, we mean some discrete condition that can be characterized as a node on a directed graph like that in Figure 16.2.1. By transition, we mean moving along one of the directed edges of the graph. If you want to characterize a continuous variable in the context of this section, you need to define a set of discrete bins for its possible values, and make these the states.

The setup we describe is slightly more general than its close cousin, the directed graph of stages and states that defined the dynamic programming (DP) problem in $\ S 1 0 . 1 3$ . For some applications, the estimation problem of interest does live on a graph that has states and stages, exactly like DP; but for other applications, we need a general directed graph. We’ll consider both types below.

Historically, problems involving the estimation of states have arisen in diverse, and often noncommunicating, fields. There are often multiple names for single concepts. (We saw this previously in the Bellman-Dijkstra-Viterbi algorithm for DP.) This history also makes it hard to give, in this section, a unified treatment with a single narrative. A more practical approach is to go through a couple of examples from different fields, and then, afterward, make some comparisons and give some advice.

![](images/0271dc5be1d425ab5e7bb29bb1a6ea87fc0a904b6b8c41d838eef6223b0d7b61.jpg)  
Figure 16.2.1. Graph of a dynamical system with five states. Allowed transitions are shown by arrows.

# 16.2.1 Error-Correcting Codes and Soft-Decision Decoding

An $( N , K )$ binary block code is a list of $2 ^ { K }$ binary codewords, each of length $N > K$ bits, designed to send a $K$ -bit message in such a way that it can be received correctly even if one or more of the $N$ bits arrive garbled (that is, 0 instead of 1, or vice versa). Two simple examples are shown below. In these particular cases, the message bits are the initial bits of the codeword, but that need not be true in general. Assigning any permutation of the codewords to message words is, effectively, the same code; likewise an arbitrary permutation of the bits in all the codewords (permuting bit-columns in the table).

<table><tr><td rowspan=1 colspan=2>(6,3) Shortened Hammingmessage    codeword</td></tr><tr><td rowspan=3 colspan=1>000001010</td><td rowspan=1 colspan=1>000000</td></tr><tr><td rowspan=1 colspan=1>001110</td></tr><tr><td rowspan=1 colspan=1>010101</td></tr><tr><td rowspan=1 colspan=1>011</td><td rowspan=1 colspan=1>011011</td></tr><tr><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>100011</td></tr><tr><td rowspan=1 colspan=1>101</td><td rowspan=1 colspan=1>101101</td></tr><tr><td rowspan=1 colspan=1>110</td><td rowspan=1 colspan=1>110110</td></tr><tr><td rowspan=1 colspan=1>111</td><td rowspan=1 colspan=1>111000</td></tr></table>

<table><tr><td rowspan=1 colspan=2>(7,4) Hammingmessage  codeword</td></tr><tr><td rowspan=2 colspan=1>00000001</td><td rowspan=1 colspan=1>0000000</td></tr><tr><td rowspan=1 colspan=1>0001011</td></tr><tr><td rowspan=1 colspan=1>0010</td><td rowspan=1 colspan=1>0010111</td></tr><tr><td rowspan=1 colspan=1>0011</td><td rowspan=1 colspan=1>0011100</td></tr><tr><td rowspan=1 colspan=1>0100</td><td rowspan=1 colspan=1>0100110</td></tr><tr><td rowspan=1 colspan=1>0101</td><td rowspan=1 colspan=1>0101101</td></tr><tr><td rowspan=1 colspan=1>0110</td><td rowspan=1 colspan=1>0110001</td></tr><tr><td rowspan=1 colspan=1>0111</td><td rowspan=1 colspan=1>0111010</td></tr><tr><td rowspan=1 colspan=1>1000</td><td rowspan=1 colspan=1>1000101</td></tr><tr><td rowspan=1 colspan=1>1001</td><td rowspan=1 colspan=1>1001110</td></tr><tr><td rowspan=1 colspan=1>1010</td><td rowspan=1 colspan=1>1010010</td></tr><tr><td rowspan=1 colspan=1>1011</td><td rowspan=1 colspan=1>1011001</td></tr><tr><td rowspan=1 colspan=1>1100</td><td rowspan=1 colspan=1>1100011</td></tr><tr><td rowspan=1 colspan=1>1101</td><td rowspan=1 colspan=1>1101000</td></tr><tr><td rowspan=1 colspan=1>1110</td><td rowspan=1 colspan=1>1110100</td></tr><tr><td rowspan=1 colspan=1>1111</td><td rowspan=1 colspan=1>1111111</td></tr></table>

Both of the codes shown have the property that their Hamming distance is 3. This means that all pairs of codewords differ in at least three bits. This is the property of the code that makes it “error correcting on one bit.” If you receive a codeword with one of its bits wrong, then (i) it will not be in the above table, and (ii) there will be a unique codeword in the table that differs from it in one bit position. So, trying each bit position in turn, you can figure out what was the intended codeword.

A longer code, with a larger Hamming distance $d$ , can be error correcting for more than one garbled bit, in fact for $( d - 1 ) / 2$ bits (rounding down). An $( N , K )$ code can have $d$ as large as $N - K$ . However, trying all possible corrections until you find a valid codeword is a very poor decode strategy!

For so-called linear codes it is possible to construct a parity-check matrix $\mathbf { P }$ with the property that multiplying it by the vector of received bits (and doing all arithmetic modulo 2) gives a vector, the so-called syndrome, that is either all zeros (indicating that the received bits are ok) or else it uniquely corresponds to a mask (termed a coset leader) that tells which bits need correcting. So this error-correction algorithm, called syndrome decoding, can be summarized as:

- multiply the received bits by the parity-check matrix to get the syndrome, - do a table lookup of the syndrome to get the coset leader, and - XOR the coset leader with the received bits to get a valid codeword.

For example, the parity check matrix for the .7; 4/ Hamming code, above, is

$$
\mathbf { P } = { \left( \begin{array} { l l l l l l l l } { 1 } & { 1 } & { 1 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } & { 1 } & { 0 } & { 1 } & { 0 } \\ { 1 } & { 0 } & { 1 } & { 1 } & { 0 } & { 0 } & { 1 } \end{array} \right) }
$$

(Convert codewords to column vectors by reading from left to right.) The lookup table relating syndrome to coset leader is

<table><tr><td rowspan=1 colspan=1>syndrome</td><td rowspan=1 colspan=1>coset leader</td></tr><tr><td rowspan=3 colspan=1>000001010</td><td rowspan=1 colspan=1>0000000</td></tr><tr><td rowspan=1 colspan=1>0000001</td></tr><tr><td rowspan=1 colspan=1>0000010</td></tr><tr><td rowspan=1 colspan=1>011</td><td rowspan=1 colspan=1>0001000</td></tr><tr><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>0000100</td></tr><tr><td rowspan=1 colspan=1>101</td><td rowspan=1 colspan=1>1000000</td></tr><tr><td rowspan=2 colspan=1>110111</td><td rowspan=1 colspan=1>0100000</td></tr><tr><td rowspan=1 colspan=1>0010000</td></tr></table>

This particular code is called a perfect code because the number of syndromes exactly equals the number of coset leaders with one nonzero bit, plus 1 for the zero syndrome, a numerological coincidence. There are very few perfect codes, because there are very few sets of integers satisfying

$$
1 + { \binom { N } { 1 } } + \cdots + { \binom { N } { e } } = 2 ^ { N - K }
$$

where $e$ is the number of bits corrected. Probably the most nontrivial perfect code is the Golay code, with $N = 2 3$ , $K = 1 2$ , and $e = 3$ . (Check out the numerology yourself.)

It’s no big deal if a code is not perfect. It just means that there are some extra syndromes that correct some errors of more than $e$ bits, but not enough to correct all such errors. You include these extra syndromes in the table, and run the algorithm exactly as already described. However, if a code is too far from perfect, you are wasting syndromes without gaining more bits of sure correction.

In practical applications, $N$ and $K$ are larger than these examples. For example, the lowest level of error correction on an audio compact disk (CD) is a .28; 24/ Reed-Solomon (RS) code, which can correct $\textit { e } = \textit { } 2$ bits. (On a CD, bits of the output codewords from many consecutive blocks are then interleaved and further protected by an RS(32,28) code.) Reed-Solomon codes are typically decoded by a more efficient process than syndrome decoding, using the so-called Berlekamp-Massey algorithm.

![](images/147fe625bf286a692fcdde8f42f1c8102870049df6ef3fbbcc86540b26a628f5.jpg)  
Figure 16.2.2. Trellises associated with four binary codes. The graph is traversed from left to right. A zero is output when any dotted edge is traversed, a one for a solid edge. Every path yields a valid codeword.

Now take a deep breath. Everything we have discussed thus far is what is called hard-decision decoding (HDD), meaning that hard decisions are made as to whether each incoming bit is a 1 or 0, with the error-correction algorithm acting on the resulting, possibly garbled, codeword. Virtually all coding theory utilized HDD until the early 1970s. Then came the giant leap forward with the recognition by multiple practitioners that Viterbi’s 1967 decoding algorithm (an independent rediscovery of Bellman-Dijkstra, we might now say) could utilize “soft” data about each bit as easily as hard.

To understand soft-decision decoding (SDD), let us first note that every binary code can be represented by the kind of stage/state graph that we met in dynamic programming (-10.13), which, in the present context, is called a trellis. Figure 16.2.2 shows the trellises for the two codes given explicitly above, as well as for the schoolbook examples of a repetition code (“tell me three times”) and a parity code. The latter, with $d = 1$ , is error detecting, but not error correcting.

Although arrows are not shown, the trellis is traversed from left to right. Any such path on the trellis generates a valid codeword. A zero bit is emitted when a dotted edge is traversed, a one bit for a solid edge. You encode message bits by deciding whether to branch up or down, when you have a choice. Notice that you don’t get such a choice at every stage: “Forced” edges generate precisely the extra codeword bits that the code’s redundancy requires.

Although every code has a trellis, it is not so easy to find the minimal trellis, the one that has the fewest possible states at its maximum expansion. MacKay [1] gives a brief introduction; many additional references are in [3].

The first great idea behind soft-decision decoding is that we don’t need to decide whether an incoming bit is a 0 or 1. Rather, we just need to assign a probability to each possibility (summing to unity, of course). For example, a bit’s value may be determined by whether an instantaneous voltage is positive or negative — but the voltage measurement has some Gaussian spread of errors. If the voltage is many standard deviations positive, or negative, then the respective probabilities are very close to one or zero; but if the voltage is only $t ~ = ~ 0 . 5$ (say) standard deviations away from zero, we may want to assign a probability of 0.6915 to one more favored outcome, and 0.3085 to the less favored, since

$$
\frac { 1 } { \sqrt { 2 \pi } } \int _ { - \infty } ^ { 0 . 5 } e ^ { - z ^ { 2 } / 2 } d z \approx 0 . 6 9 1 5
$$

(By the end of this section we will be more sophisticated about the notion of assigning probabilities to transitions.)

The second great idea is that the problem of finding the maximum likelihood path through a trellis — that is, the path with the maximum product of the probabilities at each stage — is just a dynamic programming problem, where the cost of traversing an edge whose probability is $p$ is taken as $- \log ( p )$ , a positive number, since $0 \leq p \leq 1$ . The minimum cost path, with this metric, is the maximum likelihood path. In each stage, all the 0 edges (dotted lines in the figure) get one probability, and all the 1 edges (solid lines) get its complement. The edge probabilities can, and in general will, vary with each bit received (that is, from stage to stage), since the noise and path loss can vary with time.

Take these two ideas together and you have soft-decision decoding using the Viterbi algorithm.

The following tableau decodes one codeword for the shortened Hamming .6; 3/ code given above. In this example, five of the six bits are received fairly unambiguously, while one bit (the second) is seen to be rather ambiguous. Nevertheless, the algorithm treats all bits equally “softly.” Reviewing $\ S 1 0 . 1 3$ as necessary, you should be able to see where all the numbers in the tableau come from, as well as how the darker path (which is the final “hard” decision for the codeword 011011) is obtained by backtracking. Given the appropriate cost function, the routine dynpro in $\ S 1 0 . 1 3$ does exactly this calculation.

![](images/c7a437c77a92ff16b68870d341fd5f0cc9a64e0ed918abf482dbb7c655929108.jpg)

$$
\begin{array} { r l } { \mathrm { P r o b } ( 0 ) = } & { { } \begin{array} { c c c c c c c } { 9 7 } & { . 6 2 } & { . 0 4 } & { . 9 6 } & { . 0 1 } & { . 0 6 } \end{array} } \\ { \mathrm { P r o b } ( 1 ) = } &  { } \begin{array} { c c c c c c c } { . 0 3 } & { . 3 8 } & { . 9 6 } & { . 0 4 } & { . 9 9 } & { . 9 4 } \end{array} \end{array}
$$

You might have the “bright idea” of converting the final minimum path length, 1.15 in the above example, into a probability by taking its negative exponential. The result is 0.3166. Does this mean that you’ll get the right codeword only $31 \%$ of the time? No! Go stand in the corner! You are confusing likelihood with probability. The likelihoods of all eight codewords (not found by the DP algorithm, but computed exhaustively) are, for this example,

<table><tr><td rowspan=1 colspan=1>codeword</td><td rowspan=1 colspan=1>likelihood</td></tr><tr><td rowspan=1 colspan=1>000000</td><td rowspan=1 colspan=1>0.000014</td></tr><tr><td rowspan=1 colspan=1>001110</td><td rowspan=1 colspan=1>0.001372</td></tr><tr><td rowspan=1 colspan=1>010101</td><td rowspan=1 colspan=1>0.000006</td></tr><tr><td rowspan=1 colspan=1>011011</td><td rowspan=1 colspan=1>0.316126</td></tr><tr><td rowspan=1 colspan=1>100011</td><td rowspan=1 colspan=1>0.000665</td></tr><tr><td rowspan=1 colspan=1>101101</td><td rowspan=1 colspan=1>0.000007</td></tr><tr><td rowspan=1 colspan=1>110110</td><td rowspan=1 colspan=1>0.000001</td></tr><tr><td rowspan=1 colspan=1>111000</td><td rowspan=1 colspan=1>0.000006</td></tr></table>

You can see that the likelihoods don’t add up to 1, and that the favored path wins over any competitor by a large factor. (Bayesians: We know that this paragraph is making you break out in a rash. We are on your side, and will have more to say about this in $\ S 1 6 . 3 . 4 .$ )

In the above example, the second bit was merely ambiguous. What if it had instead been really wrong, indicating, say, 0.99 probability of having a value zero? No problem. Since the underlying code is one-bit error correcting, the DP algorithm will readily decide to traverse the unlikely single edge, since the alternative would be to traverse two or more unlikely edges on other bits. However, if we made the second bit incorrect with probability 0:999999, the algorithm would “correct” two other bits instead, which, under the circumstances, would be the best decision.

You can see that it is not meaningful to say exactly how many bits $e$ a softdecision decode algorithm can correct. It just makes the best choice determined by the probabilities. As another example, we might consider the simple parity code shown in Figure 16.2.2. With a hard-decision decode, parity does not give enough information to correct a single bit. With a soft-decision algorithm, however, the parity bit can cast the deciding vote if some other bit is wavering too close to an ambiguous $50 \%$ probability level.

Soft-decision decoding algorithms are available for essentially all codes in use today, including Reed-Solomon codes and the important turbo codes [2] that are beyond our scope. Some important applications (e.g., trellis coded modulation), use short trellises whose end states loop around to become identified with their start states. The Viterbi algorithm is applied to long sequences of input symbols that loop through the trellis many times. In trellis coded modulation, the symbols being (softly) decoded are not single bits, but locations in the complex phase plane that comprise a carefully chosen constellation centered at the origin (for example, a hexagonal lattice).

# CITED REFERENCES AND FURTHER READING:

Lin, S. and Costello, D.J. 2004, Error Control Coding, 2nd ed. (Upper Saddle River, NJ: Pearson-Prentice Hall).   
Blahut, R.E. 2002, Algebraic Codes for Data Transmission (Cambridge, UK: Cambridge University Press).   
MacKay, D.J.C. 2003, Information Theory, Inference, and Learning Algorithms (Cambridge, UK: Cambridge University Press).[1]   
Schlegel, C. and Perez, L. 2000, Trellis and Turbo Coding, (Piscataway, NJ: IEEE Press).[2]   
“Special Issue on Codes and Complexity”, 1996, IEEE Transactions on Information Theory, vol. 42, no. 6, pp. 1649-2064.[3]

![](images/76b11d33f414f00f58befb8b74fa0f5ebd72785f6b0ef9f58aa88da552b775df.jpg)  
Figure 16.3.1. Example of a Markov model. Transitions occur between states along the directed edges shown. Each outgoing edge is labeled by its probability. The sum of the probabilities on the outgoing edges from each state is 1. This model is called “Teen Life.”

# 16.3 Markov Models and Hidden Markov Modeling

Trellises, like those in $\ S 1 6 . 2$ , are directed graphs without any loops, so a path that begins at the leftmost node inevitably ends, after a finite number of stages, at the rightmost node. The more general Markov model lives on a graph that can have loops (as in Figure 16.2.1), so some paths can continue indefinitely. Indeed, as a convention, one can add a self-loop (a directed edge connecting a state to itself) to any state that would otherwise have “no way out.” Then, all paths can be continued indefinitely, even those whose fate is to remain stuck in a single state.

To turn such a directed graph into a Markov model (also known as a Markov chain or first-order Markov process), we simply label all of its edges with transition probabilities, such that the sum of probabilities over the outgoing edges from each node is 1. Figure 16.3.1 shows an example, a Markov model with five states, that we call “Teen Life.”

A single realization of a Markov model is a random path that moves from state to state according to the model’s probabilities. These are conveniently organized into a transition matrix A whose element $A _ { i j }$ is the probability associated with an $i  j$ transition, that is, the probability of moving to state $j$ , given state $i$ as the starting point. A valid transition matrix satisfies

$$
0 \leq A _ { i j } \leq 1 \qquad \mathrm { a n d } \qquad \sum _ { j } A _ { i j } = 1
$$

The transition matrix for Teen Life (Figure 16.3.1) is

$$
\mathbf { A } = { \left( \begin{array} { l l l l l } { 0 } & { 0 . 7 } & { 0 . 1 } & { 0 } & { 0 . 2 } \\ { 0 . 2 } & { 0 . 4 } & { 0 } & { 0 . 2 } & { 0 . 2 } \\ { 0 } & { 1 . 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 . 3 } & { 0 } & { 0 . 7 } & { 0 } \\ { 0 . 1 } & { 0 . 1 } & { 0 } & { 0 } & { 0 . 8 } \end{array} \right) }
$$

where the states are numbered in the order (Eat, Hang, Study, Talk, and Sleep).

A routine for generating a realization of a Markov model from its $M \times M$ transition matrix, using the Ran structure of $\ S 7 . 1$ to get random numbers, is straightforward.

void markovgen(const MatDoub_I &atrans, VecInt_O &out, Int istart ${ = } 0$ , Int seed $^ { = 1 }$ ) {

Generate a realization of an $M$ -state Markov model, given its $M \times M$ transition matrix atrans. The vector out is filled with integers in the range $0 \ldots M - 1$ . The starting state is the optional argument istart (defaults to 0). seed is an optional argument that sets the seed of the random number generator.

Int i, ilo, ihi, ii, j, $\textrm { \textmu } =$ atrans.nrows(), $\mathrm { ~ \bf ~ n ~ } =$ out.size();   
MatDoub cum(atrans); Temporary matrix to hold cumulative probabilities.   
Doub r;   
Ran ran(seed); Use the random number generator Ran.   
if (m $! =$ atrans.ncols()) throw("transition matrix must be square");   
for ( $\scriptstyle \dot { \mathtt { 1 } } = 0$ ; i<m; i++) { Fill cum and die if clearly not a transition matrix. for $\mathrm { ( j } { = } 1$ ; j<m; ${ \mathrm { j } } + +$ ) cum[i][j] $+ =$ cum[i][j-1]; if (abs(cum[i][m-1]-1.) > 0.01) throw("transition matrix rows must sum to 1");   
${ \dot { \mathrm { ~  ~ } } } =$ istart; The current state is kept in j.   
out[0] $=$ j;   
for ( $\dot { 1 } \dot { 1 } = 1$ ; ii<n; ii $^ { + + }$ ) { Main loop. $\mathbf { r } =$ ran.doub()/cum[j][m-1]; Slightly-off normalization gets corrected here. ilo $\mathbf { \lambda } = \mathbf { \lambda } _ { 0 } ;$ ; ihi $\qquad = \ \ln ;$ while (ihi-ilo $> ~ 1 \AA$ ) { Use bisection to find location among the cumu-$\begin{array} { r l } { \dot { \bf \lambda } _ { 1 } } & { { } = } \end{array}$ (ihi+ilo) >> 1; lative probabilities. if ( $. \mathbf { r } \mathbf { > }$ cum[j][i-1]) ilo $\mathbf { \Sigma } = \mathbf { \Sigma } _ { \mathrm { ~ i ~ } } ^ { \ast }$ ; else ihi $\mathbf { \Sigma } = \mathbf { \Sigma } _ { \mathrm { ~ i ~ } }$ ; } out[ii] $\mathbf { \dot { \omega } } = \mathbf { \dot { \omega } } \mathbf { j } \mathbf { \omega } = \mathbf { \dot { \omega } }$ ilo; Set new current state.   
}

What makes the transition matrix a matrix, and not just a table of probabilities, is its connection to ensembles of realizations of the corresponding Markov model. An ensemble can be characterized by the components of a population vector $\mathbf { s } _ { t }$ whose components give the number of models in each state at time $t$ . (Here and below, we use $t$ as an integer, discrete time variable. On a trellis it would be called a stage instead of a time.) For Teen Life, we can give names to the components of $\mathbf { s } _ { t }$ corresponding to the states: $( E , H , S , T , Z )$ .

If all the models in the ensemble are evolved by one timestep (one transition), then the population vector $\mathbf { s } _ { t }$ turns into $\mathbf { s } _ { t + 1 }$ by the matrix multiplication

$$
\mathbf { s } _ { t + 1 } = \mathbf { A } ^ { T } \mathbf { s } _ { t }
$$

The transpose operation is needed only because two common conventions are at odds: The time order $i  j$ for $A _ { i j }$ versus the left matrix multiplication of a column vector (whose implicit time ordering is “from” the second index “to” the first). Given a matrix, you can easily tell whether it is intended to be an $\mathbf { A }$ or an $\mathbf { A } ^ { T }$ , by whether, respectively, its rows or columns sum to unit probability.

Note that we can evolve more than one step at a time, by precomputing powers of $\mathbf { A } ^ { T }$ . So, $\mathbf { s } _ { t + n } = ( \mathbf { A } ^ { T } ) ^ { n } \mathbf { s } _ { t }$ , for example.

Every Markov model has at least one equilibrium distribution of states that remains unaffected when multiplied by $\mathbf { A } ^ { T }$ . To prove this, we write

$$
\mathbf { A } ^ { T } \mathbf { s } _ { e } = \mathbf { s } _ { e } \qquad \iff \qquad ( \mathbf { A } ^ { T } - \mathbf { 1 } ) \mathbf { s } _ { e } = \mathbf { 0 }
$$

where $\mathbf { s } _ { e }$ is the sought-after equilibrium state. Equation (16.3.4) can hold if and only if $\mathbf { A } ^ { T } - \mathbf { 1 }$ is a singular matrix. Since the columns of $\mathbf { A } ^ { T }$ all sum to 1, the columns of $\mathbf { A } ^ { T } - \mathbf { 1 }$ all sum to zero, and hence are linearly dependent, q.e.d. Equivalently, we have proved that $\mathbf { A } ^ { T }$ has at least one eigenvalue equal to 1. The corresponding eigenvector is an equilibrium distribution of states. If there is only one eigenvalue equal to 1, the equilibrium is unique. For the Teen Life model, there is one eigenvalue of 1, and the corresponding eigenvector (normalized so that its components sum to unity) is approximately $( 0 . 0 9 9 , 0 . 2 9 7 , 0 . 0 0 1 , 0 . 1 9 8 , 0 . 3 9 5 )$ . (This teenager spends about $3 9 . 5 \%$ of his/her time sleeping, $1 9 . 8 \%$ talking on the phone, $0 . 1 \%$ studying, and so forth.)

Do almost all starting distributions converge to a unique equilibrium, in which case the model is said to be ergodic? Not necessarily. Two things can go wrong. First, if there is more than one eigenvalue equal to 1, a model will converge to some different linear combination of the corresponding eigenvectors for different starting distributions. Such models are said to fail the test of irreducibility. Second, the model may have a periodic limit cycle, so that, for most starting distributions, it doesn’t converge at all. Such models are said to fail the test of aperiodicity. The theorem (and vocabulary test) is: Irreducibility and aperiodicity imply ergodicity.

One way to diagnose these conditions is to perform successive squarings of the matrix $\mathbf { A } ^ { T }$ to take it to a very high power, say $2 ^ { 3 2 }$ . This requires $O ( 3 2 M ^ { 3 } )$ operations for a model with $M$ states. (While there are more sophisticated methods, none scale better than $M ^ { 3 }$ .) If all $M$ columns in the result are converging to identical vectors, then there is just one eigenvalue (unity), and all starting distributions will converge to its eigenvector (which is in fact the repeated column vector). The model is then ergodic.

Otherwise, locate any rows in the power matrix that are zero, and cross out those rows and their corresponding columns. (These are states that become permanently unpopulated as the model evolves.) Then, check to see if the remaining columns are all eigenvectors with unit eigenvalue. You can do the test by multiplying each such column by the original $\mathbf { A } ^ { T }$ . If all columns pass the test, then there are multiple equilibria, but all starting distributions will converge to some combination of them. If any column fails the test, then the model has a periodic limit cycle. There are still equilibria, given by the eigenvectors of unit eigenvalue, but a starting state must be very special to evolve to one. Indeed, such states are a set of measure zero, and we can say that the equilibria are unstable.

A simple example with multiple equilibria and periodic limit cycles is the transition matrix

$$
\mathbf { A } ^ { \prime } = \left( \begin{array} { c c c c c } { 0 } & { 1 . 0 } & { 0 } & { 0 } & { 0 } \\ { 1 . 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 . 7 } & { 0 } & { 0 . 3 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 . 0 } \\ { 0 } & { 0 } & { 0 } & { 1 . 0 } & { 0 } \end{array} \right)
$$

corresponding to the graph

![](images/ec8cbcefab1f8eefa3461844ae7d7fbb7af7ab47ca92bc51c7f02faada36cd86.jpg)

${ \mathbf { A } } ^ { \prime T }$ has two eigenvectors with unit eigenvalue (you can guess them from the graph): $( 0 . 5 , 0 . 5 , 0 , 0 , 0 )$ and $( 0 , 0 , 0 , 0 . 5 , 0 . 5 )$ . However, ${ \mathbf { A } } ^ { \prime T }$ to the power $2 ^ { 3 2 }$ does not have

these as any of its columns, but is rather

$$
( \mathbf { A } ^ { \prime T } ) ^ { 2 ^ { 3 2 } } = { \left( \begin{array} { l l l l l } { 1 . 0 } & { 0 } & { 0 . 7 } & { 0 } & { 0 } \\ { 0 } & { 1 . 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 . 0 } & { 0 } \\ { 0 } & { 0 } & { 0 . 3 } & { 0 } & { 1 . 0 } \end{array} \right) }
$$

thus showing that the model has only unstable equilibria. (The little identity matrix blocks are merely artifacts of the limit cycles having period 2, while $2 ^ { 3 2 }$ is even. In general, you will get some other pattern.)

Successive squaring is a poor way to get the equilibrium distribution for a model that is known (or guessed) to have a single stable equilibrium. A better way, since we already know the eigenvalue, is inverse iteration. Just solve the equation

$$
\left( \mathbf { A } ^ { T } - \mathbf { 1 } \right) \mathbf { s } _ { e } = \mathbf { b }
$$

by $L U$ decomposition (-2.3), with the right-hand vector $\mathbf { b } = ( 1 , 1 , \ldots , 1 )$ . If your solver complains about the zero pivot instead of substituting a small value for it (which is what we want for this application), then use the matrix . $( \mathbf { A } ^ { T } - 0 . 9 9 9 9 9 9 \times \mathbf { 1 } )$ instead. In either case, you will want to renormalize $\mathbf { s } _ { e }$ , to make, e.g., its components have unit sum.

You can test for multiple equilibria by perturbing the right-hand side vector and seeing if you get the same $\mathbf { s } _ { e }$ . If you do have multiple equilibria, it is probably time to turn to the methods of Chapter 11 and calculate $\mathbf { A } ^ { T }$ ’s eigenvalues and eigenvectors directly.

That is all (in fact, more) than we want to tell about Markov models in general. We turn now to the real business at hand, which is to estimate statistically the state of a “hidden” Markov model, given only partial or imperfect information.

# 16.3.1 Hidden Markov Models

In a hidden Markov model (HMM), we don’t get to observe the state of the model directly. Rather, whenever it is in any state $i$ (one of $M$ states), it emits a symbol $k$ , chosen probabilistically from a set of $K$ symbols. The probability of emitting symbol number $k$ from state number $i$ is denoted by

$$
b _ { i } ( k ) \equiv P ( { \mathrm { s y m b o l } } k \mid { \mathrm { s t a t e } } i ) \qquad ( 0 \leq i < M , \quad 0 \leq k < K )
$$

with the normalization condition

$$
\sum _ { k = 0 } ^ { K - 1 } b _ { i } ( k ) = 1 \qquad ( 0 \leq i < M )
$$

Thus, when the model evolves through $N$ timesteps, the hidden states are a vector of integers,

$$
\mathbf { s } = \{ s _ { t } \} = ( s _ { 0 } , s _ { 1 } , \dots s _ { N - 1 } )
$$

each in the range $0 \leq s _ { i } < M$ , while the observations or data are a vector of integers,

$$
\mathbf { y } = \{ y _ { t } \} = ( y _ { 0 } , y _ { 1 } , \dots y _ { N - 1 } )
$$

each in the range $0 \leq y _ { i } < K$ .

For the Teen Life example, here is a table of symbols and their probabilities of being emitted from each state, in response to the repeated parental query, “What are you doing?”:

<table><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1>i=0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>k</td><td rowspan=1 colspan=1>symbol</td><td rowspan=1 colspan=1>meaning</td><td rowspan=1 colspan=1>Eat</td><td rowspan=1 colspan=1>Hang</td><td rowspan=1 colspan=1>Study</td><td rowspan=1 colspan=1>Talk</td><td rowspan=1 colspan=1>Sleep</td></tr><tr><td rowspan=2 colspan=1>0123</td><td rowspan=3 colspan=1>0SbgZ</td><td rowspan=1 colspan=1>[silence]“T&#x27;m studying!”“T&#x27;m busy!”</td><td rowspan=2 colspan=1>0.2000.8</td><td rowspan=1 colspan=1>0.200.6</td><td rowspan=2 colspan=1>01.000</td><td rowspan=2 colspan=1>0.30.20.40.1</td><td rowspan=2 colspan=1>0.5000</td></tr><tr><td rowspan=2 colspan=1>[grunt][snore]</td><td rowspan=2 colspan=1>0.80</td><td rowspan=1 colspan=1>0.2</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0.5</td></tr></table>

The key point is that the emitted symbols give only incomplete, or garbled, state information (e.g., the claim of studying when actually talking on the phone). A state can emit more than one possible symbol, and a symbol can be emitted by more than one possible state. Nevertheless, our goal is to make the best statistical reconstruction of the vector s from $\mathbf { y }$ .

More specifically, at each time $t$ we want to estimate

$$
P _ { t } ( i ) \equiv P ( s _ { t } = i \mid \mathbf { y } )
$$

the probability that the actual state of the system is $i$ at time $t$ , given all the data. (If the word “probability” in this context bothers you, you may think of it as a likelihood.)

Let $\alpha _ { t } ( i )$ be defined for $t = 0 \dots N - 1$ and $i = 0 \dots M - 1$ as the probability of the observed data up to time $t$ (that is, $y _ { 0 } \ldots y _ { t } )$ , given that we are in state $i$ at time $t$ . Since we are not specifying any of the previous states, we must sum over all possible paths that get to state $i$ at time $t$ . Thus,

$$
\alpha _ { 0 } ( i ) = b _ { i } ( y _ { 0 } ) \qquad \quad \alpha _ { t } ( i ) = \sum _ { i _ { 0 } , i _ { i } , \ldots , i _ { t - 1 } } b _ { i _ { 0 } } ( y _ { 0 } ) A _ { i _ { 0 } i _ { 1 } } b _ { i _ { 1 } } ( y _ { 1 } ) \ldots A _ { i _ { t - 1 } i } b _ { i } ( y _ { t } ) \qquad ( 1 \leq t < N )
$$

In other words, each transition contributes to the product both a transition probability and a symbol probability, and we sum over all possible combinations of previous states, that is, all possible values of $i _ { 0 } , i _ { 1 } , \dots , i _ { t - 1 }$ , each in the range $0 \ldots M - 1$ .

Since $\alpha _ { t } ( i )$ is the probability of data given state, it can also be interpreted as the likelihood of the state, given the data; or, if we are Bayesians (and we are!), as the unnormalized posterior probability of being in state $i$ , which can be normalized simply by dividing by $\textstyle \sum _ { i } \alpha _ { t } ( i )$ . However, equation (16.3.13) seems useless for a big and a little reason. Big: It has exponentially many terms to evaluate. Little: it uses only part of the data (the data earlier in time) to estimate the state $i$ at time $t$ . It is what is called a forward estimate.

Amazingly, both problems are easy to fix. It is not hard to see that the $\alpha _ { t } ( i )$ ’s satisfy a recurrence relation that advances them all one step in $t$ :

$$
\alpha _ { t + 1 } ( j ) = \sum _ { i = 0 } ^ { M - 1 } \alpha _ { t } ( i ) A _ { i j } b _ { j } ( y _ { t + 1 } ) \qquad ( 0 \leq j < M ) \quad { \mathrm { f o r } } \quad t = 0 , \ldots , N - 2
$$

One step of this recurrence takes only $O ( M ^ { 2 } )$ operations, so the whole table of $\alpha _ { t } ( i )$ ’s can be computed in $O ( N M ^ { 2 } )$ .

To fix the second problem, we come at the issue from “the other end of time.” Let $\beta _ { t } ( i )$ be defined for $t = N - 1 \ldots 0$ and $i = 0 \dots M - 1$ as the probability of the future observed data $( y _ { t + 1 } , y _ { t + 2 } , \dots y _ { N - 1 } )$ again given that we are in state $i$ at time $t$ . Analogously to the $\alpha$ ’s, we have

$$
\beta _ { t } ( i ) = \sum _ { i _ { t + 1 } , . . . , i _ { N - 1 } } A _ { i i _ { t + 1 } } b _ { i _ { t + 1 } } ( y _ { t + 1 } ) \ . . . \ A _ { i _ { N - 2 } i _ { N - 1 } } b _ { i _ { N - 1 } } ( y _ { N - 1 } )
$$

with the special case $\beta _ { N - 1 } ( i ) ~ = ~ 1$ . (Because there are no data to the future of $t = N - 1$ , those data’s probability is by definition 1.) In the formula for the $\beta _ { t } ( i )$ ’s there is a factor in the product for each future transition probability and each future symbol probability (fixing the symbols to be the actual $y$ ’s of course). Just as for the $\alpha$ ’s, the $\beta$ ’s can be interpreted as likelihoods, or unnormalized posterior probabilities. And, wonderfully, equation (16.3.15) can be solved by a backward recurrence,

$$
\beta _ { t - 1 } ( i ) = \sum _ { j = 0 } ^ { M - 1 } A _ { i j } b _ { j } ( y _ { t } ) \beta _ { t } ( j ) \qquad ( 0 \le i < M ) \quad \mathrm { f o r } \quad t = N - 1 , \ldots , 1 
$$

Calculating all the $\beta$ ’s for $t = N - 1 , N - 2 , \dots , 0$ is called a backward estimate.

Now here is the big payoff: From the definitions of the $\alpha$ ’s and $\beta$ ’s, the product $\alpha _ { t } ( i ) \beta _ { t } ( i )$ is the unnormalized posterior probability of state $i$ at time $t$ given all the data. If we normalize it by dividing by

$$
\mathcal { L } _ { t } = \sum _ { i = 0 } ^ { M - 1 } \alpha _ { t } ( i ) \beta _ { t } ( i )
$$

we get the desired estimate of the probability of each separate state at each separate time,

$$
P _ { t } ( i ) = \frac { \alpha _ { t } ( i ) \beta _ { t } ( i ) } { \mathcal { L } _ { t } }
$$

Further, it follows from the definitions (16.3.13) and (16.3.15) that $\mathcal { L } _ { t }$ is actually independent of $t$ , so we can omit the subscript $t$ and calculate it only once. (In practice, one often renormalizes at each time $t$ for greater numerical stability, however.) The value of $\mathcal { L }$ can be interpreted as the probability (or likelihood) of the whole data set, given the parameters of the model.

Equations (16.3.14) and (16.3.16), taken together, are called the forward-backward algorithm for state estimation in a hidden Markov model.

Translating HMM into code, we start with a structure that will hold the various quantities that come into play, and its constructor. You construct an HMM structure by specifying a transition probability matrix A (N.B.: not $\mathbf { A } ^ { T }$ ), a symbol probability matrix $b _ { i k } \equiv b _ { i } ( k )$ , and a vector of observed data y.

struct HMM {   
Structure for a hidden Markov model and its methods. MatDoub a, b; Transition matrix and symbol probability matrix VecInt obs; Observed data. Int fbdone; Int mstat, nobs, ksym; Number of states, observations, and symbols. Int lrnrm; MatDoub alpha, beta, pstate; Matrices $\pmb { \alpha }$ , $\beta$ , and $P _ { i } ( t )$ . VecInt arnrm, brnrm; Doub BIG, BIGI, lhood; HMM(MatDoub_I &aa, MatDoub_I &bb, VecInt_I &obs); Constructor; see below. void forwardbackward(); HMM state estimation. void baumwelch(); HMM parameter re-estimation. Doub loglikelihood() {return log(lhood)+lrnrm\*log(BIGI);} Returns the log-likelihood computed by forwardbackward().   
};

HMM::HMM(MatDoub_I &aa, MatDoub_I &bb, VecInt_I &obss) : a(aa), b(bb), obs(obss), fbdone(0), mstat(a.nrows()), nobs(obs.size()), ksym(b.ncols()), alpha(nobs,mstat), beta(nobs,mstat), pstate(nobs,mstat), arnrm(nobs), brnrm(nobs), BIG(1.e20), BIGI(1./BIG) Constructor. Input are the transition matrix aa, the symbol probability matrix bb, and the observed vector of symbols obss. Local copies are made, so the input quantities need not be preserved by the calling program.

Int i,j,k;

# Doub sum;

Although space constraints make us generally stingy about printing code for checking input, we will save you a lot of grief by doing so in this case. If you get “matrix not normalized” errors, you probably have your matrix transposed. Note that normalization errors ${ < } 1 \%$ are silently fixed.

if (a.ncols() $\ ! =$ mstat) throw("transition matrix not square");   
if (b.nrows() $! =$ mstat) throw("symbol prob matrix wrong size");   
for ( $\scriptstyle { \dot { 1 } } = 0$ ; i<nobs; $\dot { 1 } + +$ ) { if (obs[i] < 0 || obs[i] $> =$ ksym) throw("bad data in obs");   
}   
for $\scriptstyle \dot { \bar { 1 } } = 0$ ; i<mstat; i++) { sum $=$ 0.; for ( $\scriptstyle \mathbf { j } = 0$ ; j<mstat; $\mathrm { j } + +$ ) sum $+ =$ a[i][j]; if (abs(sum - 1.) $>$ 0.01) throw("transition matrix not normalized"); for (j $_ { | = 0 }$ ; j<mstat; ${ \mathrm { j } } + +$ ) a[i][j] / $\stackrel { \cdot } { = }$ sum;   
}   
for $\scriptstyle \dot { 1 } = 0$ ; i<mstat; i++) { sum $=$ 0.; for $\scriptstyle 1 = 0$ ; k<ksym; $\mathbf { k } { + } { + }$ ) sum $+ =$ b[i][k]; if (abs(sum - 1.) $>$ 0.01) throw("symbol prob matrix not normalized"); for $\scriptstyle ( \mathtt { k } = 0$ ; k<ksym; $\mathbf { k } { + } { + }$ ) b[i][k] $/ =$ sum;   
}

# }

Now, to actually do the forward-backward estimation, you call the function forwardbackward. This fills the matrix pstate, so that pstate $\mathbf { \Psi } _ { t i } = P _ { t } ( i )$ . It also sets the internal variables lhood and lrnrm so that the function loglikelihood returns the logarithm of $\mathcal { L }$ . Don’t be surprised at how large in magnitude this (negative) number can be. The probability of any particular data set of more than trivial length is astronomically small!

In the following code, the quantities BIG, BIGI, arnrm, brnrm, and lrnrm all relate to dealing with values that would far underflow an ordinary floating format. The basic idea is to renormalize as necessary, keeping track of the accumulated number of renormalizations. At the end, when an $\alpha$ , a $\beta$ , and an $\mathcal { L }$ are combined, probability values of reasonable magnitude result.

# void HMM::forwardbackward() {

HMM forward-backward algorithm. Using the stored a, b, and obs matrices, the matrices alpha, ta, and pstate are calculated. The latter is the state estimation of the model, given the data.

Int i,j,t;   
Doub sum,asum,bsum;   
for ( $\scriptstyle \dot { 1 } = 0$ ; i<mstat; $\dot { \bf 1 } + +$ ) alpha[0][i] $=$ b[i][obs[0]];   
arnrm[0] $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
for ( $\scriptstyle \cdot t = 1$ ; t<nobs; $^ { \ t + + }$ ) { Forward pass. asum $\qquad = \ 0$ ; for $( \ j = 0$ ; j<mstat; $\mathrm { j } + + )$ { sum $\qquad = \ 0 .$ .; for ( $\mathtt { i } = 0$ ; i<mstat; $\mathrm { i } + + \mathrm { j }$ ) sum $+ =$ alpha[t-1][i]\*a[i][j]\*b[j][obs[t]]; alpha[t][j] $=$ sum; asum $+ =$ sum; arnrm[t] $=$ arnrm[t-1]; Renormalize the $\pmb { \alpha }$ ’s as necessary to avoid underif (asum $<$ BIGI) { flow, keeping track of how many renormal-++arnrm[t]; izations for each $\pmb { \alpha }$ . for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ; j<mstat; $\mathrm { j } + +$ ) alpha[t][j] $\ast =$ BIG; }   
}   
for ( $\scriptstyle \dot { 1 } = 0$ ; i<mstat; $\dot { \bf 1 } + + \dot { }$ ) beta[nobs-1][i] = 1.;   
brnrm[nobs-1] $\qquad = \ 0$ ;   
for ( $\scriptstyle \pm =$ nobs-2; t>=0; t--) { Backward pass. bsum $\qquad = \ 0 .$ ; for ( $\scriptstyle { \dot { 1 } } = 0$ ; i<mstat; $\dot { 1 } + +$ ) { sum $\mathit { \Theta } = \mathit { \Theta } 0 .$ ; for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<mstat; ${ \mathrm { j } } + + { \mathrm { \rangle } }$ ) sum $+ =$ a[i][j]\*b[j][obs[t+1]]\*beta[t+1][j]; beta[t][i] $=$ sum; bsum $+ =$ sum; } brnrm[t] $=$ brnrm[t+1]; if (bsum $<$ BIGI) { Similarly, renormalize the $\beta$ ’s as necessary. ++brnrm[t]; for ( $\scriptstyle \dot { \ j } = 0$ ; j<mstat; ${ \mathrm { j } } + + { \mathrm { . } }$ ) beta[t][j] $\ast =$ BIG; }   
lhood $\mathit { \Theta } = \mathit { \Theta } 0$ .; Overall likelihood is lhood with lnorm renormal  
for ( $\scriptstyle \dot { 1 } = 0$ ; i<mstat; $\dot { \bf 1 } + +$ ) lhood $+ =$ alpha[0][i]\*beta[0][i]; izations.   
lrnrm $=$ arnrm[0] $^ +$ brnrm[0];   
while (lhood $<$ BIGI) {lhood $\ast =$ BIG; lrnrm++;}   
for ( $t = 0$ ; t<nobs; $^ { \ t + + }$ ) { Get state probabilities from $\pmb { \alpha }$ ’s and $\beta$ ’s. sum $\qquad = \ 0 .$ ; for ( $\scriptstyle { \dot { 1 } } = 0$ ; i<mstat; $\mathbf { i } + + \mathbf { i }$ ) sum $+ =$ (pstate[t][i] $=$ alpha[t][i]\*beta[t][i]); The next line is an equivalent calculation of sum. But we’d rather have the normalization of the $P _ { i } ( t )$ ’s be more immune to roundoff error. Hence we do the above sum for each value of $^ \texttt { t }$ . // sum $=$ lhood\*pow(BIGI, lrnrm - arnrm[t] - brnrm[t]); for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; i<mstat; $\dot { 1 } + + \dot { 1 }$ ) pstate[t][i] $/ { = }$ sum;   
}   
fbdone $\mathit { \Theta } = \mathit { \Theta } 1$ ; Flag prevents misuse of baumwelch(), later.

You may be wondering how well forwardbackward is able to do at predicting the hidden states of Teen Life, given just a long string of output symbols. If we take the prediction to be the state with the highest probability at each time, then this is correct about $78 \%$ of the time. Another $17 \%$ of the time, the correct state has the second-highest probability, often when the top two probabilities are nearly equal. It is an important property of HMMs that the output is not only a prediction, but also a quantitative assessment of how “sure” the model is of that prediction.

# 16.3.2 Some Variations on HMM

HMM state estimation with the forward-backward algorithm is a very flexible formalism, and many variants are possible. For example, in decoding codes on a trellis, as we did above, the symbols 0 or 1 are emitted not by the states, but by the transitions between the states. If we want to use HMM for that problem (we will say more about this below), we must replace $b _ { i } ( k )$ with $b _ { i j } ( k )$ , the probability of emitting symbol $k$ in a transition from state $i$ to state $j$ . The forward and backward recurrences now become

$$
\begin{array} { l } { \displaystyle \alpha _ { t + 1 } ( j ) = \sum _ { i = 0 } ^ { M - 1 } \alpha _ { t } ( i ) A _ { i j } b _ { i j } ( y _ { t + 1 } ) } \\ { \displaystyle \beta _ { t - 1 } ( i ) = \sum _ { j = 0 } ^ { M - 1 } A _ { i j } b _ { i j } ( y _ { t } ) \beta _ { t } ( j ) } \end{array}
$$

and we start off the $\alpha$ ’s with the special rule $\alpha _ { 0 } ( i ) = 1$ , since (like the case of $\beta _ { N - 1 } ( i )$ previously) the probability of the data is 1 before there are any data.

Another variant case is where one or more intermediate states are known exactly. In that case, one or more of the sums over $i _ { 0 } , i _ { 1 } , \dots , i _ { t - 1 }$ in equation (16.3.13) is left out, and the corresponding index on an $A$ and $b$ gets replaced by the known state number. If you track through how this affects the recurrence equation (16.3.14), you’ll see that the new procedure is

- calculate the $\alpha$ ’s forward to, and including, a known state; - zero all the $\alpha$ values at that time except for that of the known state; - don’t renormalize anything (though you feel tempted to do so); and - continue forward with the $\alpha$ ’s for the next timestep.

Proceed similarly for the $\beta$ ’s.

The opposite variant is where you have missing data, meaning that for some values of $t$ there is no observation of the symbol $\textbf { y } _ { t }$ . In this case, all you need to do is to make a special case for the symbol probability,

$$
b _ { i } ( y _ { t } ) \equiv 1 , \qquad ( 0 \leq i < M ) \qquad t \in \{ \mathrm { m i s s i n g } \}
$$

meaning that, regardless of state $i$ , the probability of observing the data (meaning no data) at time $t$ is unity. Now proceed as usual to calculate the state probabilities. If you then want to reconstruct the missing data, you can calculate its posterior probabilities,

$$
P ( y _ { t } = k \mid \mathbf { y } ) = \sum _ { i = 0 } ^ { M - 1 } P _ { i } ( t ) b _ { i } ( k ) = \sum _ { i = 0 } ^ { M - 1 } { \frac { \alpha _ { i } ( t ) \beta _ { i } ( t ) } { { \mathcal { L } } } } b _ { i } ( k ) \qquad t \in \{ { \mathrm { m i s s i n g } } \}
$$

# 16.3.3 Bayesian Re-Estimation of the Model Parameters

This is magical. The probability that we were in state $i$ at time $t$ is $\alpha _ { t } ( i ) \beta _ { t } ( i ) / \mathcal { L }$ . What is the probability, given the data $\mathbf { y }$ , that a given transition, say between time

$t$ and time $t + 1$ , was a transition between state $i$ and state $j ?$ We write, applying various of the laws of probability,

$$
\begin{array} { r l } & { P ( s _ { t } = i , s _ { t + 1 } = j \mid \mathbf { y } ) } \\ & { \qquad = P ( s _ { t + 1 } = j \mid \mathbf { y } , s _ { t } = i ) P ( s _ { t } = i \mid \mathbf { y } ) } \\ & { \qquad = \frac { P ( \mathbf { y } \mid s _ { t + 1 } = j , s _ { t } = i ) P ( s _ { t + 1 } = j \mid s _ { t } = i ) } { \sum _ { j } P ( \mathbf { y } \mid s _ { t + 1 } = j , s _ { t } = i ) P ( s _ { t + 1 } = j \mid s _ { t } = i ) } P ( s _ { t } = i \mid \mathbf { y } ) } \\ & { \qquad = \frac { [ \alpha _ { t } ( i ) b _ { j } ( y _ { t + 1 } ) \beta _ { t + 1 } ( j ) ] [ A _ { i j } ] } { \sum _ { j } [ \alpha _ { t } ( i ) b _ { j } ( y _ { t + 1 } ) \beta _ { t + 1 } ( j ) ] [ A _ { i j } ] } \frac { [ \alpha _ { t } ( i ) \beta _ { t } ( i ) ] } { \mathcal { L } } } \\ & { \qquad = \frac { \alpha _ { t } ( i ) A _ { i j } b _ { j } ( y _ { t + 1 } ) \beta _ { t + 1 } ( j ) } { \mathcal { L } } } \end{array}
$$

Note how the sum over $j$ in the denominator disappears by the recurrence (16.3.16) for $\beta _ { t } ( i )$ .

So, for a long run of data, we can compute the fraction of the time that a state $i$ transitions to state $j$ as the estimated number of $i  j$ transitions divided by the estimated number of $i$ states,

$$
\widehat { A } _ { i j } = \frac { \sum _ { t } \alpha _ { t } ( i ) A _ { i j } b _ { j } ( y _ { t + 1 } ) \beta _ { t + 1 } ( j ) } { \sum _ { t } \alpha _ { t } ( i ) \beta _ { t } ( i ) }
$$

noting that the $\mathcal { L }$ ’s cancel out. The reason for calling this quotient $\widehat { A } _ { i j }$ is that it is a re-estimation of the transition probability $A _ { i j }$ . The corresponding re-estimation of the symbol probability matrix $b _ { i } ( k )$ is the fraction of all $i$ states that emit a symbol $k$ , namely

$$
\widehat { b } _ { i } ( k ) = \frac { \sum _ { t } \delta ( y _ { t } , k ) \alpha _ { t } ( i ) \beta _ { t } ( i ) } { \sum _ { t } \alpha _ { t } ( i ) \beta _ { t } ( i ) }
$$

where $\displaystyle \delta ( j , k )$ is 1 if $j = k$ , zero otherwise.

You might think that this process is somehow circular, or that re-estimating $A _ { i j }$ and $b _ { i } ( k )$ in this fashion only introduces noise that degrades the model. Far from it! Baum and Welch first showed that replacing $A _ { i j }$ by $\widehat { A } _ { i j }$ and $b _ { j } ( k )$ by $\widehat { b } _ { j } ( k )$ , and then recalculating the probabilities of each state at each time by the forward-backward algorithm, always increases $\mathcal { L }$ , the overall likelihood of the model. It is, in fact, an EM algorithm (cf. $\ S 1 6 . 1$ , and see below). You can continue this cycle of estimating states (forward-backward) and re-estimating model probabilities (Baum-Welch), obtaining further increases in $\mathcal { L }$ , until convergence to a maximum is achieved. Equations (16.3.23) and (16.3.24) are known as Baum-Welch re-estimation.

So the magic is this: We began by estimating states in a known hidden Markov model. We now see that, just from the data, we can get not only an estimate of the states, but also an estimate of the model itself, that is, the transition probabilities and symbol probabilities. Like any iterative process, this works best if we have a good initial guess. But it will often converge to a good model from a fairly random initial guess. (You should not start with exactly uniform probabilities, because that creates a symmetry that the iteration finds hard to break.)

The code is straightforward. The updating of $b _ { i } ( k )$ comes almost for free as a byproduct of computing the denominator in the update for $A _ { i j }$ . Like the forwardbackward algorithm, Baum-Welch re-estimation takes $O ( N M ^ { 2 } )$ operations.

# void HMM::baumwelch() {

Baum-Welch re-estimation of the stored matrices a and b, using the data obs and the matrices alpha and beta as computed by forwardbackward() (which must be called first). The previous values of a and b are overwritten.

Int i,j,k,t;   
Doub num,denom,term;   
MatDoub bnew(mstat,ksym);   
Doub powtab[10]; Fill table of powers of BIGI.   
for ( $\scriptstyle { \dot { 1 } } = 0$ ; $\yen 10$ ; $\dot { \bf 1 } + +$ ) powtab[i] $=$ pow(BIGI,i-6);   
if (fbdone $\ ! = ~ 1 \AA$ ) throw("must do forwardbackward first");   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; i<mstat; i++) { Looping over i, get denominators and new b. denom $\qquad = \ 0$ .; for ( $\scriptstyle \mathbf { k } = 0$ ; k<ksym; $\mathrm { k } { + } { + }$ ) bnew[i][k] $\mathit { \Theta } = \mathit { \Theta } 0 .$ ; for ( $t = 0$ ; t<nobs-1; t++) { term $=$ (alpha[t][i]\*beta[t][i]/lhood) $^ *$ powtab[arnrm[t] $^ +$ brnrm[t] - lrnrm + 6]; denom $+ =$ term; bnew[i][obs[t]] $+ =$ term; } for (j ${ = } 0$ ; j<mstat; $\mathrm { j } + +$ ) { Inner loop over j gets elements of a. num $\mathit { \Theta } = \mathit { \Theta } 0$ .; for $t = 0$ ; t<nobs-1; t++) { num $+ =$ alpha[t][i]\*b[j][obs[t+1]]\*beta[t+1][j] \* powtab[arnrm[t] $^ +$ brnrm[t+1] - lrnrm $^ +$ 6]/lhood; } a[i][j] $\ast =$ (num/denom); } for $( \mathtt { k } \mathtt { = } 0 )$ ; k<ksym; $\mathrm { k } { + } { + } \mathrm { i }$ ) bnew[i][k] /= denom;   
}   
$\mathtt { \Delta } _ { \mathtt { b } } \ =$ bnew;   
fbdone $\mathit { \Theta } = \mathit { \Theta } 0$ ; Don’t let this routine be called again until for backward() has been called.

You must always precede a call to baumwelch by a call to forwardbackward, since the latter updates the $\alpha$ and $\beta$ tables. Also, as you alternate calls to the two functions, you monitor convergence by the value of the log-likelihood calculated by forwardbackward.

Be aware that convergence can be excruciatingly slow! The references describe methods by which convergence can be accelerated in some cases. Common difficulties are when a rare state is not correctly captured by the model, or when the model thinks that there are two states, with nearly identical transition probabilities, when there is really only one. If you have even a plausible guess for the transition probability matrix, you should use it to start. There are many applications where you shouldn’t use re-estimation at all: If you have a pretty good model to start with, just use it (via forwardbackward) to analyze your data, and don’t even think about re-estimating.

The Baum-Welch re-estimation algorithm, which dates from the mid-1960s, was generalized in the mid-1970s by Dempster, Laird, and Rubin, as the expectationmaximization (EM) algorithm, with a variety of applications to problems with missing or censored data. (An example is the Gaussian mixture model in $\ S 1 6 . 1 .$ .) In this more general language, the forward-backward algorithm is an E-step, while Baum-Welch is an M-step. Alas, one small cloud in an otherwise bright sky is that the maximum of $\mathcal { L }$ achieved by multiple EM iterations is only guaranteed to be a local, not a global, maximum.

HMM has found wide application in speech recognition, gene sequence comparison, financial models, and a variety of other fields. The references give specifics.

# 16.3.4 Comparing the Viterbi Algorithm with HMM

It is important to understand the similarities and differences between the Viterbi algorithm and hidden Markov modeling (its forward-backward algorithm in particular).

When we discussed the Viterbi algorithm in the context of decoding, we made the implicit assumption that a 1 bit was a priori as likely as a 0 bit. It is straightforward to generalize the Viterbi algorithm to include an arbitrary a priori transition probability $A _ { i j }$ , just like HMM. In that case, the probability factor on each edge (whose negative logarithm is the edge cost) is the product of two terms, again just like HMM, $A _ { i j } b _ { i j } ( k )$ , where now $b _ { i j } ( k )$ is the probability of observing the observed symbol $k$ given that an $i  j$ transition occurred.

We discussed Baum-Welch parameter re-estimation for HMMs in some detail. Re-estimation of the parameters in a Viterbi model, often called Viterbi training, is analogous. Take the most probable path output by the algorithm (or ensemble of paths collected from the decodes of many codewords). Count the number of $i  j$ transitions seen along these paths and the numbers of each symbol $k$ seen for each pair $i , j$ . Now re-estimate $A _ { i j }$ and $b _ { i j } ( k )$ by the obvious normalizations of these counts.

The Viterbi algorithm and the forward estimation part of the forward-backward algorithm are structurally very similar. In both cases, we sweep forward in time (or by stages) and assign a likelihood (or posterior probability) to each node, based on the data already seen. The difference is that Viterbi assigns to a node the probability of the single best path that reaches it, while forward-backward assigns the sum of probabilities over all possible paths to that node. Indeed the Viterbi algorithm is sometimes called the min-sum algorithm while forward-backward is referred to as the sum-product algorithm, just to highlight this distinction. (In the context of coding theory, the forward-backward algorithm is also sometimes called the BCJR or Bahl-Cocke-Jelinek-Raviv algorithm. In other contexts it is sometimes called belief propagation.)

The backward passes of the two algorithms have somewhat different structures. For Viterbi, the backward pass simply consolidates the information about the single most probable path that is already implicit in the node labeling. For forwardbackward, as we have seen, the backward pass is needed to get posterior probabilities for each node that use all the data, both ahead of and behind any time $t$ .

If you think you have a choice between using the Viterbi algorithm or using HMM, you should probably think again. Most problems clearly favor only one or the other method. If your desired output is a valid path on the graph, then HMM won’t do: It might yield a set of highly probable nodes that just don’t lie on any single path. For example, you might have the first half of one codeword and the second half of another, with no graph edge connecting the two halves. That is why decoding theory usually starts in the world of Viterbi (although, in some more complicated constructs, it can end up with a foot in each world).

On the other hand, if you care about which nodes are visited, then HMM is most likely what you want. In fact, Viterbi can give very poor results. The most probable path is often very improbable when compared to the sum of all paths that lead through a particular node, one possibly not on the most probable path. Or, another way of describing this, there may be exponentially many paths with not-too-different probabilities, so the node probabilities are determined by the statistics of where they all channel, not by which one path happens to have the highest probability.

It is very easy to “mine” HMM for alternative possibilities, since it yields seemingly every possible posterior probability that you might want to know. It is quite difficult to get anything from the Viterbi algorithm other than the single most probable path. That is because the enumeration of all possible paths is vastly harder than the enumeration of all possible nodes; the Bellman-Dijkstra-Viterbi algorithm is exquisitely good at keeping only the information that it needs. Data structures for finding more than one probable path rapidly become very complex.

Finally, we must take aim at the myth, occasionally heard, that the Viterbi algorithm, as a pure maximum likelihood (ML) estimate, is somehow “less Bayesian” than HMM. In fact, HMM is also a pure ML estimate if you look only at the state $i$ with the largest $\alpha _ { t } ( i ) \beta _ { t } ( i )$ at each time $t$ , neither normalizing its value nor looking at any other $i$ ’s. But you are then ignoring a wealth of useful information about the other possible states. (This, in part, is why you should get with the Bayesian program!) We think that both HMM and Viterbi are in fact Bayesian to the core. If there were good ways to enumerate all the other paths and their likelihoods, we would not hesitate to normalize the best-path likelihood and call it a posterior probability. It is only because of the difficulty of this enumeration that it is possible to keep the Viterbi algorithm’s Bayesian character “in the closet”; and there is no advantage, that we can see, in doing so.

# CITED REFERENCES AND FURTHER READING:

Hsu, H.P. 1997, Schaum’s Outline of Theory and Problems of Probability, Random Variables, and Random Processes (New York: McGraw-Hill).   
Häggström, O. 2002, Finite Markov Chains and Algorithmic Applications (Cambridge, UK: Cambridge University Press).   
Norris, J.R. 1998, Markov Chains, Cambridge Series in Statistical and Probabilistic Mathematics (Cambridge, UK: Cambridge University Press).   
MacDonald, I.L. and Zucchini, W. 1997, Hidden Markov and Other Models for Discrete-Valued Time Series (Boca Raton, FL: Chapman & Hall/CRC).   
McLachlan, G.J. and Krishnan, T. 1996, The EM Algorithm and Extensions (New York: Wiley).   
Rabiner, L. 1989, “A Tutorial on Hidden Harkov Models and Selected Applications in Speech Recognition,” Proceedings of the IEEE, vol. 77, no. 2, pp. 257-286. [Review article on the use of HMMs in speech recognition.]   
Eddy, S.R. 1998, “Profile Hidden Markov Models,” Bioinformatics, vol. 14, pp. 755-763. [Review article on the use of HMMs in genetics.]

# 16.4 Hierarchical Clustering by Phylogenetic Trees

Hierarchical clustering is a type of unsupervised learning: We seek algorithms that figure out how to cluster an unordered set of input data without ever being given any training data with the “right answer.” As the name implies, the output of a hierarchical clustering algorithm is a bunch of fully nested sets. The smallest sets are the individual data elements. The largest set is the whole data set. Intermediate sets are nested; that is, the intersection of any two sets is either the null set, or else the smaller of the two sets.

![](images/bea9eed3fc146803d4d265dbc0452164efafcd136c508219928467f190eaa928.jpg)  
Figure 16.4.1. Representations of hierarchical classification. Top left: Diagram showing fully nested sets. Bottom left: Equivalent parenthesized expression. Right: Binary tree (with possibly zero branch lengths).

What you need to get started with hierarchical clustering is either a set of sequences, or else a distance matrix. Character-based methods start with $n$ sequences each $m$ characters long (for example, DNA bases or protein amino acids). A toy example might be the $n = 1 6$ sequences of $m = 1 2$ characters,

0. CGGTTGGGAGCT 8. GCGCGGTGCAGC   
1. AGGTCGTGAGGT 9. AGGCGGTGCGGG   
2. TGGTTGGGGTTT 10. GGGCGGGGCGGG   
3. TGGGTGCGAGTT 11. GGGCGCTGCGGG   
4. ACGTTTGGGTGA 12. GGACGGAGGCTG   
5. AAGGTTGGGGAA 13. GGGTGGGAGCTG   
6. GTCTTTCGGGTG 14. AGGAGGCTGATG   
7. CACTTGCGGGGG 15. TGGCGGATGATG

It is probably not immediately obvious that these sequences were generated from a balanced five-level binary tree, with GGGGGGGGGGGG at the root, and with each daughter node having two random mutations from her parent. We will see below the extent to which some of the algorithms that we discuss can figure this out from the data. A realistic case likely would have significantly longer sequences than this, and fewer mean mutations per character; the number of sequences might be either more, or fewer, than this toy.

The alternative starting point is with an $n \times n$ matrix $d _ { i j }$ of distances between all pairs of your $n$ data points, which might now be sequences, points in $N$ -dimensional space, or whatever. You are responsible for making sure that the distance matrix satisfies four conditions:

$$
\begin{array} { l l } { { d _ { i j } \geq 0 } } & { { \ \mathrm { ( p o s i t i v i t y ) } } } \\ { { d _ { i i } = 0 } } & { { \mathrm { ( z e r o ~ s e l f - d i s t a n c e ) } } } \\ { { d _ { i j } = d _ { j i } } } & { { \mathrm { ( s y m m e t r y ) } } } \\ { { d _ { i k } \leq d _ { i j } + d _ { j k } } } & { { \mathrm { ( t r i a n g l e ~ i n e q u a l i t y ) } } } \end{array}
$$

for all $i , j , k$ . We’ll discuss below how to get distances from sequences, if that’s the way you want to go.

Figure 16.4.1 shows three representations of the same hierarchical clustering of seven data elements. The two representations on the left are self-explanatory. The one on the right, the binary tree, takes explaining on one point: If, in the set diagram, $( a b ) , ( c d )$ , and $( e )$ are clustered “democratically,” then why does the binary tree select .e/ arbitrarily as the descendant of a higher node, instead of having three equal descendants from a common node?

![](images/e16d6752c6bf6bc94d14b5ca068f5114e1e74e1dc5b2843acb7a141c677c1671.jpg)  
Figure 16.4.2. Types of trees. A cladogram (A) has arbitrary branch lengths. Only the topology is intended to be represented. A phylogram or phylogenetic tree (B) is an additive tree, where the distance between any two nodes/leaves is the sum of lengths of the horizontal connecting branches. An ultrametric tree (C) is an additive tree with the property that any node has the same distance to all of its leaves (as when all lengths represent time). Tree (D) is an alternative way of drawing tree (B). Again, only horizontal distances are significant. In an unrooted tree (E), line lengths represent distances independent of orientation. The tree (E) is the unrooted depiction of (B) or (D).

The answer is just convention. Binary trees are the adopted common language of hierarchical clustering because (i) they emerge naturally from the concept of mutation events in biology, (ii) they are somewhat easier to represent in a computer than more general trees, and, (iii) they are often easier to prove theorems about. Our binary trees will almost always have the concept of branch length, a representation of some measure of difference between a parent node and its child. When we need to connect up democratically some number of nodes greater than two, we do it with zero-length branches. A convention is to view all topologies of nodes so connected as being equivalent.

# 16.4.1 Tree Basics

Figure 16.4.2 shows several ways of drawing binary trees and introduces some further terminology. The data points are leaves, meaning that they are generally taken as terminal nodes on the tree. Trees are often drawn either sideways (root left, leaves right) or upside down (root top, leaves bottom) by comparison with their arboreal namesake whose roots are on the bottom, leaves on top — at least for most trees that we see! A tree without meaningful branch lengths is usually called a cladogram. These have a rich historical tradition in pre-molecular biology but are viewed with alarm by most bioscientists today. A tree with meaningful branch lengths representing distances (in some metric) between nodes and their children, or between leaves, is called a phylogram or phylogenetic tree. (However, some authors use the terms cladogram and phylogram interchangeably, while some others use the words merely

to distinguish different drawing styles.)

To a mathematician, a phylogenetic tree is an additive tree, meaning that the tree’s path lengths induce a distance metric between any two leaves, namely the sum of path lengths up and down that connect the two leaves through their unique closest common ancestor. In real situations, the data we are given often are not exactly represented by an additive distance metric. Thus, the problem of hierarchical clustering amounts to finding a way of projecting such data onto the set of all additive trees in a useful, or statistically justifiable, way.

Given an additive tree, it is easy to compute its distance matrix $d _ { i j }$ , defined now as the matrix of all distances between pairs of leaf nodes. But what about the reverse? Given some symmetric matrix $d _ { i j }$ , is it possible to determine whether there exists an additive tree that instantiates it? Yes. One answer is the four-point condition for additive trees: Given four distinct leaves $i , j , k , l$ , an additive tree exists if and only if

$$
d _ { i j } + d _ { k l } \le \operatorname* { m a x } ( d _ { i k } + d _ { j l } , d _ { i l } + d _ { j k } )
$$

for all choices of $i , j , k , l$ . In words, this is equivalent to the statement: For all distinct $i , j , k , l$ , there is a tie for the maximum of the three sums of the form $d _ { i j } +$ $d _ { k l }$ . Later, when we discuss the neighbor-joining method, we will have a more practical algorithmic answer.

As Figure 16.4.2 illustrates, a tree can either be rooted or unrooted. An unrooted tree can always be rooted arbitrarily, by choosing any branch, grasping its midpoint between your thumb and forefinger, and then shaking the tree so that all the other branches drop downward into place. (We could give a much more mathematical description, but it would not add any clarity.) Some hierarchical clustering algorithms yield rooted trees, where the root has some meaning with respect to the data; others yield unrooted trees, although they may be drawn as if rooted, simply as a graphical convention. It’s important to keep track of which kind of algorithm you are using.

You may wonder why the data points must always be leaves (terminal nodes). Might not some data points actually be good ancestors of others? The answer is again a mixture of history and convention: If the leaves are observed living taxa, then they are by definition alive today. If “today” represents terminal nodes, then they are by definition leaves. What makes this a mere convention is that we can always connect a leaf to an ancestor node by a zero-length branch, so that ancestor-versus-living-taxon becomes a distinction without a difference. A benefit of this convention is that we always know in advance how many internal nodes will be generated by $n$ data points: $n - 1$ if the tree is rooted, or $n - 2$ for an unrooted tree, independent of the tree’s topology. (If this isn’t obvious, then draw a few pictures.)

If path length denotes, literally, evolutionary time, then a phylogenetic tree has the additional property of being ultrametric (refer to Figure 16.4.2). Ultrametric trees are defined as additive trees with the property that the distance from any node to all of its descendant leaves is the same for all such leaves. Clearly this is the case if all the leaves have the same “time distance” from their common ancestor. In the early 1960s, it was proposed that accepted mutation rates might be close enough to constant that, at the molecular level, actual evolutionary data might be close to ultrametric, i.e., that there was a “molecular clock.” For most cases, this is no longer believed to be true. For example, mutation rates in $E$ . coli have been found to vary by two orders of magnitude. Ultrametric trees are important mathematically, as we will see, but almost never realistic in their own right.

![](images/71326d152c886b0f515ab311d5eb8437e15b271c457b508c91c63cca4fbd61ba.jpg)  
Figure 16.4.3. Tree counting. (a) There is just one unrooted tree with three leaves. (b) There are three ways to add a fourth leaf. (c) For each of the trees in (b), there are five ways to add a fifth leaf. Continuing to add leaves, the number of trees with $_ { n }$ leaves is $1 \times 3 \times 5 \times \cdots \times ( 2 n - 5 )$ .

The test, analogous to equation (16.4.2), for whether a given distance matrix is ultrametric is the three-point condition,

$$
d _ { i j } \leq \operatorname* { m a x } ( d _ { i k } , d _ { j k } )
$$

for all distinct $i , j , k$ . Equivalently, in words: Among the three distances connecting three distinct leaves, there is a tie for the maximum. Here too there is a more practical algorithmic answer, which we will mention later.

There are a lot of possible ways to draw a tree that connects $n$ leaves. As Figure 16.4.3 illustrates, the number of distinct, unrooted, possibilities is

$$
N _ { \mathrm { t r e e s } } ( n ) = 1 \times 3 \times 5 \times \cdots \times ( 2 n - 5 ) \equiv ( 2 n - 5 ) ! !
$$

The fact that this expression grows super-exponentially with $n$ creates a dilemma in the field of computational phylogenetics: An algorithm that requires an explicit enumeration of, or explicit search over, all possible trees can be useful only for small values of $n$ . Thus, $N _ { \mathrm { t r e e s } } ( 1 0 ) \ \approx \ 2 \times 1 0 ^ { 6 }$ , is easy, but $N _ { \mathrm { t r e e s } } ( 2 0 ) \approx 2 \times 1 0 ^ { 2 0 }$ is practically impossible.

# 16.4.2 Strategies for the Hierarchical Clustering Problem

If you are starting with a set of sequences, then, schematically, the goal of a character-based method is to find the best of all possible trees, given the data, for some definition of “best”:

$$
\left( { \mathrm { s e q u e n c e s } } \right) { \xrightarrow { \ { \mathrm { s e a r c h ~ f o r } } \ } } \left( { \mathrm { t r e e } } \right)
$$

The two most common definitions of “best” are maximum parsimony and maximum likelihood, both of which we will say more about below [1]. Character methods are generally limited by the super-exponential explosion in the number of trees. Although the exhaustive search can be limited to some extent, for example by heuristics of various kinds, its long shadow can never be avoided entirely.

Alternatively, if you are starting with a distance matrix, the problem is to find the additive tree whose induced distance matrix (by branch lengths up and down) is closest to $d _ { i j }$ , according to some criterion of closeness. This is also an exponentially difficult problem. In practice, however, distance methods almost always use fast heuristic methods that, while provably exact only for the unrealistic case where $d _ { i j }$ already comes from an ultrametric or additive tree, actually work pretty well for distance matrices encountered in practice. In other words, the adopted scheme is

$$
\left( \begin{array} { l } { \mathrm { d i s t a n c e } } \\ { \mathrm { m a t r i x } } \end{array} \right) \xrightarrow [ ] { \mathrm { u l t r a m e t r i c ~ t r e e } } \left( \mathrm { t r e e } \right)
$$

or

$$
\left( \begin{array} { l } { \mathrm { d i s t a n c e } } \\ { \mathrm { m a t r i x } } \end{array} \right) \xrightarrow [ ] { \mathrm { a d d i t i v e ~ t r e e } } \left( \mathrm { t r e e } \right)
$$

The ability of these fast heuristic methods to give “pretty good” solutions to NP-hard problems is remarkable, and only partially understood [2].

The most widely used heuristics are all agglomerative methods, meaning that they start by connecting individual data points into small clusters, then connect those clusters, and so forth. Common ultrametric-tree heuristic methods are UPGMA, WPGMA, single linkage clustering, and complete linkage clustering. The most widely used additive-tree heuristic method — and probably the most widely used phylogenetic clustering method overall — is the neighbor-joining (NJ) method [6]. We will discuss, and implement, all the mentioned heuristic methods below.

There are a few, less-well-developed, distance-based methods that avoid heuristics by finding provably error-bounded methods for transforming an arbitrary distance matrix into the matrix of an additive tree, then exactly constructing the resulting tree [3,4],

$$
\left( \begin{array} { l } { { \mathrm { d i s t a n c e } } } \\ { { \mathrm { m a t r i x } } } \end{array} \right) { \xrightarrow { \mathrm { ~ f i n d ~ n e a r b y } } } \left( \begin{array} { l } { { \mathrm { a d d i t i v e } } } \\ { { \mathrm { m a t r i x } } } \end{array} \right) { \xrightarrow { \mathrm { ~ c o n s t r u c t i o n } } } \left( \mathrm { t r e e } \right)
$$

Though more rigorous than the heuristic methods, there is little evidence that these methods produce better results [5].

Evidently, one can always turn a character-based problem into a distance-based one by defining a distance on character sequences,

$$
\left( { \mathrm { s e q u e n c e s } } \right) { \xrightarrow { \mathrm { d i s t a n c e } } } \left( { \begin{array} { l } { { \mathrm { d i s t a n c e } } } \\ { { \mathrm { m a t r i x } } } \end{array} } \right)
$$

and then continuing with schemes (16.4.6) or (16.4.7).

The obvious distance between two sequences is their Hamming distance $H ( i , j )$ , which is defined as the number of character positions in which sequence $i$ differs from sequence $j$ , an integer between 0 and $m$ . However, when you are given not just the data, but also a statistical model defining how it was generated (i.e., “evolved”), there is often a corrected distance transformation that will give better tree reconstructions [2]. For example, the popular Cavender-Felsenstein model (whose discussion is beyond our scope) has the corrected distance transformation

$$
\begin{array} { r } { d _ { i j } = - \frac { 1 } { 2 } \log \left( 1 - 2 H ( i , j ) / m \right) } \end{array}
$$

This expression can be used directly when sequences are long enough, or mutation probabilities small enough, that the argument of the logarithm is never negative. If your data produce a negative argument, then a standard workaround is to use a multiple $1 \times$ or $2 \times$ ) of the largest computable $d _ { i j }$ for all uncomputable $d _ { i j }$ ’s. Corrected distance transformations also exist for general Markov models.

Corrected distance transformations have the defining (and desirable) property that as the sequence length increases, the matrix of observed corrected distances will converge to the distance matrix of an additive tree. (This is not true for the uncorrected Hamming distance, incidentally.) In such a case, the power of an additive-tree heuristic method like neighbor joining is much less mysterious. Corrected distance transformations thus provide a statistical justification for the use of the neighborjoining method.

# 16.4.3 Implementation of Agglomerative Methods

The general scheme of an agglomerative method is, first, to initialize $n$ active clusters, each containing one data point, and, second, to repeat the following operations exactly $n - 2$ times:

- Find the two active clusters that are closest by some prescribed distance measure.   
- Create a new active cluster that combines the two.   
- Connect the new cluster, as parent, to the two closest clusters, as children, with some prescription for the two branch lengths. Delete the two children from the active list.   
Compute, by some prescription, distances from the new cluster to the active clusters that remain.

Each repetition of these steps reduces the active cluster list by exactly one (one addition, two deletions), so after $n - 2$ repetitions there will be exactly two active clusters. You connect these either by a single branch (unrooted case), or by creating a root node between them (rooted case) with some prescription as to the two root branch lengths.

As we now turn to implementing phylogenetic tree routines, a few words of caution are in order. Hamming’s dictum, that the purpose of computing is insight, not numbers, applies here: Much of the value of a phylogenetic tree program lies in its graphics and user interface, both areas outside of our scope. If you are working with any significant quantity of real data, you probably want to use a sophisticated package. As we write, PAUP (Phylogenetic Analysis Using Parsimony) [7] is the most widely used commercial package, both for maximum parsimony trees and also for the various heuristic methods. PHYLIP (Phylogeny Inference Package) [8] is a free package for smaller trees ( $\lesssim 2 0$ taxa). TreeView is a widely used, free, program used for drawing trees in various formats. A user guide to the use of these and other programs is [9]. If the insight you desire lies in algorithmics, not production data, then you may read on.

Here is an abstract base class that implements the general agglomerative method, leaving the various “prescriptions” to be specified by particular derived classes, which we give later.

# struct Phylagglomnode {

Node for phylogenetic tree.

Int mo,ldau,rdau,nel; Doub modist,dep,seq; };

Pointers up and down; no. of elements. Branch length to parent. See text re. dep and seq.

# struct Phylagglom{

Abstract base class for constructing an agglomerative phylogenetic tree.

Int n, root, fsroot; No. of data points, root node, forced root. Doub seqmax, depmax; Max. values of seq, dep over the tree. vector<Phylagglomnode> t; The tree.   
virtual void premin(MatDoub &d, VecInt &nextp) $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
Function called before minimum search.   
virtual Doub dminfn(MatDoub &d, Int i, Int ${ \mathrm { ~ j ~ } } ) \ = \ 0$ ;   
Distance function to be minimized   
U rtua Doub dbranchfn(MatDoub &d, Int i, Int ${ \mathrm { ~ j ~ } } ) \ = \ 0$ ;   
Branch length, node i to mother (j is sister).   
virtual Doub dnewfn(MatDoub &d, Int k, Int i, Int j, Int ni, Int nj) = 0; Distance function for newly constructed nodes.   
virtual void drootbranchfn(MatDoub &d, Int i, Int j, Int ni, Int nj, Doub &bi, Doub $\mathrm { \& b j ) \ = \ 0 ; }$ ;   
Sets branch lengths to the final root node.   
Int comancestor(Int leafa, Int leafb); See text discussion of NJ. Phylagglom(const MatDoub &dist, Int fsr $\begin{array} { r l } { \mathbf { \Phi } } & { { } = \mathbf { \Phi } - \mathbf { 1 } } \end{array}$ )   
: n(dist.nrows()), fsroot(fsr), t(2\*n-1) {}   
Constructor is always called by a derived class.   
d makethetree(const MatDoub &dist) {   
utine that actually constructs the tree, called by the constructor of a derived class.   
Int i, j, k, imin, jmin, ncurr, node, ntask;   
Doub dd, dmin;   
MatDoub d(dist); Matrix d is initialized with dist.   
VecInt tp(n), nextp(n), prevp(n), tasklist $^ { \prime } 2 ^ { * } \mathtt { n } ^ { + 1 } )$ ;   
VecDoub tmp(n);   
for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<n; $\dot { \bar { \lambda } } + +$ ) { Initializations on leaf elements. nextp[i] $= \dot { \ } 1 + 1$ ; nextp and prevp are for looping on the distance prevp[i] $= \dot { \ } \dot { \ } - 1$ ; matrix even as it becomes sparse. tp[i] $=$ i; tp points from a distance matrix row to a tree t[i].ldau $=$ t[i].rdau $\ c = - 1$ ; element. t[i].nel $\ l = \ 1$ ;   
}   
prevp[0] $=$ nextp[n-1] = -1; Signifying end of loop.   
ncurr $\mathbf { \Phi } = \mathbf { \Phi } _ { \mathbf { n } }$ ;   
for (node $\mathbf { \Phi } = \mathbf { \Phi } \mathbf { n }$ ; node < 2\*n-2; node $^ { + + }$ ) { Main loop! premin(d,nextp); Any calculations needed before min finding. dmin $=$ 9.99e99; for ( $\mathtt { i } = 0$ ; $\scriptstyle \dot { 1 } > = 0$ ; $\dot { \bf 1 } =$ nextp[i]) { Find $i , j$ pair with min distance. if (tp[i] $= =$ fsroot) continue; for (j=nextp[i]; $\scriptstyle { \dot { \mathsf { J } } } > = 0$ ; j=nextp[j]) { if (tp[j] $= =$ fsroot) continue; if ((dd $=$ dminfn(d,i,j)) $<$ dmin) dmin $=$ dd; imin $=$ i; jmin $\mathit { \Theta } = \mathit { \Pi } _ { \dot { ] } }$ ; } } $\begin{array} { r l } { \dot { \mathbf { 1 } } } & { { } = } \end{array}$ imin; ${ \dot { \mathrm { ~  ~ j ~ } } } =$ jmin; t[tp[i]].mo $=$ t[tp[j]].mo $=$ node; Now set properties of the parent t[tp[i]].modist $=$ dbranchfn(d,i,j); and children. t[tp[j]].modist $=$ dbranchfn(d,j,i); t[node].ldau $=$ tp[i]; t[node].rdau $=$ tp[j]; t[node].nel $=$ t[tp[i]].nel $^ +$ t[tp[j]].nel; for $( \mathtt { k } = 0$ ; $\mathtt { k } > = 0$ ; $\mathrm { k } =$ nextp[k]) { Get new-node distances. tmp[k] $=$ dnewfn(d,k,i,j,t[tp[i]].nel,t[tp[j]].nel); 1 for $\scriptstyle \mathtt { k } = 0$ ; $\mathtt { k } > = 0$ ; ${ \bf k } = { \bf \ell }$ nextp[k]) d[i][k] $=$ d[k][i] $=$ tmp[k]; tp[i] $=$ node; New node replaces child $i$ in dist. matrix, while child if (prevp[j] $> = \ 0 \mathrm { { . } }$ ) nextp[prevp[j]] $=$ nextp[j]; $j$ gets patched around. if (nextp[j] $> = \ 0 ^ { \cdot }$ ) prevp[nextp[j]] $=$ prevp[j]; ncurr--; Endof

$\mathrm { ~ i ~ } = \mathrm { ~ 0 ~ }$ ; j = nextp[0]; Set properties of the root node. root $=$ node; t[tp[i]].mo $= ~ \ t$ [tp[j]].mo $=$ t[root].mo $=$ root; drootbranchfn(d,i,j,t[tp[i]].nel,t[tp[j]].nel, t[tp[i]].modist,t[tp[j]].modist); t[root].ldau $=$ tp[i]; t[root].rdau $=$ tp[j]; t[root].modist $= ~ \ t$ [root].dep $\mathit { \Theta } = \mathit { \Theta } 0$ .; t[root].nel $\begin{array} { r l } { \mathbf { \Psi } } & { { } = \mathbf { \Psi } + \mathbf { \Psi } } \end{array}$ [tp[i]].nel $^ +$ t[tp[j]].nel; We now traverse the tree computing seq and dep, hints for where to plot nodes in a two-dimensional representation. See text. ntask $\mathit { \Theta } = \mathit { \Theta } 0$ ; seqmax $=$ depmax $\qquad = \ 0 .$ ; tasklist[ntask++] $=$ root; while (ntask $> 0 \dot { }$ ) { $\begin{array} { r l } { \dot { \mathbf { 1 } } } & { { } = } \end{array}$ tasklist[--ntask]; if ( $\mathrm { ~ \dot ~ { ~ 2 ~ } ~ } > = \mathrm { ~ 0 ~ }$ ) { Meaning, process going down the tree. t[i].dep $=$ t[t[i].mo].dep $^ +$ t[i].modist; if (t[i].dep $>$ depmax) depmax $= ~ \ t$ [i].dep; if (t[i].ldau $\mathit { \Theta } < \mathit { \Theta } 0$ ) { A leaf node. t[i].seq $=$ seqmax $^ { + + }$ ; } else { Not a leaf node. tasklist[ntask $+ + { \bf \Gamma }$ ] $= \mathbf { \nabla } - \dot { \bf 1 } - 1$ ; tasklist[ntask $^ { + 1 }$ ] $=$ t[i].ldau; tasklist[ntask++] $=$ t[i].rdau; } else { Meaning, process coming up the tree. $\\\\\\\\mathrm { ~ i ~ } = \ - \mathrm { i } - 1$ ; t[i].seq $=$ 0. $^ { 5 * }$ (t[t[i].ldau].seq $^ +$ t[t[i].rdau].seq); } } } };

The Phylagglom structure creates a tree of Phylagglomnodes. Each node carries pointers to its mother and two daughters, and knows its number of elements (original data points), branch length to its mother, and two floating values dep and seq, which we now explain: The final while block in makethetree() does a depthfirst traversal of the finished tree. When it reaches a node in the downward direction, it sets dep to the sum of branch lengths to the root node. The variable dep is thus a hint as to where to plot the node in the depth direction. When the traversal reaches a leaf, it sets seq to a sequential numbering of leaves. When it reaches an internal node in the upward direction, it sets its seq value to the average of the seq values of its two children. The value of seq thus becomes a hint as to where to plot a node perpendicular to the depth direction. If you plot nodes by dep and seq, then plotted branches won’t cross each other.

Looking at the nested loops, you can see that makethetree() is $O ( n ^ { 3 } )$ in time. Actually, it is straightforward to reduce this to $O ( n ^ { 2 } )$ : With some extra bookkeeping, you can keep the distances in a structure that allows the shortest to be found without an $n ^ { 2 }$ search. We have not coded this, just to keep the code shorter and simpler.

# 16.4.4 Algorithms That Are Exact for Ultrametric Trees

Given a distance matrix that is exactly ultrametric, all of the agglomerative algorithms that we now discuss will (modulo some technical details) reconstruct its tree exactly. The reason that we need more than one such algorithm is because their behaviors can be somewhat different on realistic, nonultrametric, data, in the general scheme of (16.4.6). The different algorithms are distinguished by their prescriptions for computing the distances to new nodes.

![](images/e83c5d7cd79d505e2277bf296ead2aa8926882c3118a742042355fb350ecc727.jpg)  
Figure 16.4.4. Example of WPGMA agglomerative clustering on a toy problem. Strings were mutated hierarchically from GGGGGGGGGGGG to produce the input data. WPGMA and related methods (UPGMA, SLC, CLC) yield perfect results for perfectly ultrametric input data, but can deviate badly when that assumption is violated. In this example, however, it does quite well.

The weighted pair group method using arithmetic averages (WPGMA) uses this prescription: If a new cluster $k$ is formed from old clusters $i$ and $j$ , then the distance from $k$ to another active cluster $p$ is

$$
\begin{array} { r } { d _ { p k } = d _ { k p } = \frac { 1 } { 2 } ( d _ { p i } + d _ { p j } ) } \end{array}
$$

that is, just the average of distances to the two children.

Implementing code, as a class derived from Phylagglom, is

# struct Phylo_wpgma : Phylagglom {

Derived class implementing the WPGMA method. Only need to define functions that are virtual in Phylagglom.

void premin(MatDoub &d, VecInt &nextp) {} No pre-min calculations.   
Doub dminfn(MatDoub &d, Int i, Int j) {return d[i][j];}   
Doub dbranchfn(MatDoub &d, Int i, Int j) {return 0.5\*d[i][j];}   
Doub dnewfn(MatDoub &d, Int k, Int i, Int j, Int ni, Int nj) { return $0 . 5 *$ (d[i][k]+d[j][k]);} New-node distance is average.   
void drootbranchfn(MatDoub &d, Int i, Int j, Int ni, Int nj, Doub &bi, Doub &bj) {bi $=$ bj $=$ 0.5\*d[i][j];}   
Phylo_wpgma(const MatDoub &dist) : Phylagglom(dist) {makethetree(dist);} This call actually makes the tree.

};

Figure 16.4.4 shows the result of applying the WPGMA method to the toy data at the beginning of this section, using the Hamming distance as the distance metric. You can see that the tree captures almost all of the correct underlying topology, erring only in its pairing of 09 and 10 and thus missing the correct pairings 08-09 and 10-11.

The unweighted pair group method using arithmetic averages (UPGMA) uses

$$
d _ { p k } = d _ { k p } = \frac { n _ { i } d _ { p i } + n _ { j } d _ { p j } } { n _ { i } + n _ { j } }
$$

Although, paradoxically, UPGMA looks “weighted” while WPGMA looks “unweighted,” the names derive from the fact that the UPGMA formula is equivalent

to an unweighted average of distances to all of a node’s descendant leaves. The UPGMA method is the most widely used of the ultrametric heuristic methods.

Implementing code is

# struct Phylo_upgma : Phylagglom {

Derived class implementing the UPGMA method. Only need to define functions that are virtual in Phylagglom.

void premin(MatDoub &d, VecInt &nextp) {} No pre-min calculations.   
Doub dminfn(MatDoub &d, Int i, Int j) {return d[i][j];}   
Doub dbranchfn(MatDoub &d, Int i, Int j) {return 0.5\*d[i][j];}   
Doub dnewfn(MatDoub &d, Int k, Int i, Int j, Int ni, Int nj) { return (ni\*d[i][k] $^ +$ nj\*d[j][k]) / (ni+nj);} Distance is weighted.   
void drootbranchfn(MatDoub &d, Int i, Int j, Int ni, Int nj, Doub &bi, Doub &bj) {bi $=$ bj $=$ 0.5\*d[i][j];}   
Phylo_upgma(const MatDoub &dist) : Phylagglom(dist) {makethetree(dist);} This call actually makes the tree.

The single linkage clustering method and the complete linkage clustering method use, respectively, the minimum and maximum distances to the two children,

$$
\begin{array} { r l } & { d _ { p k } = d _ { k p } = \operatorname* { m i n } ( d _ { p i } , d _ { p j } ) \qquad \mathrm { ( s i n g l e ~ l i n k a g e ) } } \\ & { d _ { p k } = d _ { k p } = \operatorname* { m a x } ( d _ { p i } , d _ { p j } ) \qquad \mathrm { ( c o m p l e t e ~ l i n k a g e ) } } \end{array}
$$

Implementing code is

# struct Phylo_slc : Phylagglom {

Derived class implementing the single linkage clustering method.

void premin(MatDoub &d, VecInt &nextp) {} No pre-min calculations.   
Doub dminfn(MatDoub &d, Int i, Int j) {return d[i][j];}   
Doub dbranchfn(MatDoub &d, Int i, Int j) {return 0.5\*d[i][j];}   
Doub dnewfn(MatDoub &d, Int k, Int i, Int j, Int ni, Int nj) { return MIN(d[i][k],d[j][k]);} New-node distance is min of children.   
void drootbranchfn(MatDoub &d, Int i, Int j, Int ni, Int nj, Doub &bi, Doub &bj) {bi $=$ bj $=$ 0.5\*d[i][j];}   
Phylo_slc(const MatDoub &dist) : Phylagglom(dist) {makethetree(dist);} This call actually makes the tree.

# };

# struct Phylo_clc : Phylagglom {

Derived class implementing the complete linkage clustering method.

void premin(MatDoub &d, VecInt &nextp) {} No pre-min calculations.   
Doub dminfn(MatDoub &d, Int i, Int j) {return d[i][j];}   
Doub dbranchfn(MatDoub &d, Int i, Int j) {return 0.5\*d[i][j];}   
Doub dnewfn(MatDoub &d, Int k, Int i, Int j, Int ni, Int nj) { return MAX(d[i][k],d[j][k]);} New-node distance is max of children.   
void drootbranchfn(MatDoub &d, Int i, Int j, Int ni, Int nj, Doub &bi, Doub &bj) {bi $=$ bj $=$ 0.5\*d[i][j];}   
Phylo_clc(const MatDoub &dist) : Phylagglom(dist) {makethetree(dist);} This call actually makes the tree.

# 16.4.5 Neighbor Joining: Exact for Additive Trees

Saitou and Nei’s neighbor-joining method (NJ) [6] is an agglomerative method with the remarkable property that it exactly reconstructs any additive tree, given that tree’s distance matrix (again modulo some technical details). NJ is probably the most widely used agglomerative method, and perhaps the most widely used method for phylogenetic tree construction overall. Real biological trees are almost never close enough to ultrametric to give UPGMA a significant advantage over NJ, so NJ is likely the method, among the fast heuristic methods, that you will want to try first.

The prescriptions for treating NJ within the framework of Phyloagglom are slightly more complicated than for the ultrametric heuristics. At each stage of forming a new cluster, we compute an auxiliary quantity,

$$
u _ { i } \equiv \frac { 1 } { n _ { a } - 2 } \sum _ { j \neq i } d _ { i j }
$$

where the sum is over active clusters, whose number is $n _ { a }$ . Then, we find not the minimum distance, per se, but the minimum of the expression

$$
d _ { i j } - u _ { i } - u _ { j }
$$

When we connect clusters $i$ and $j$ to form a new node $k$ , the branch lengths from $i$ to $k$ and from $j$ to $k$ are

$$
\begin{array} { l } { { d _ { i k } = \frac 1 2 ( d _ { i j } + u _ { i } - u _ { j } ) } } \\ { { d _ { j k } = \frac 1 2 ( d _ { i j } + u _ { j } - u _ { i } ) } } \end{array}
$$

Finally, the distance between new node $k$ and another node $p$ is

$$
d _ { p k } = d _ { k p } = \textstyle { \frac { 1 } { 2 } } ( d _ { p i } + d _ { p j } - d _ { i j } )
$$

(You can now see why Phylagglom was coded with some features that were not exercised by the ultrametric heuristics.)

# struct Phylo_nj : Phylagglom {

rived class implementing the neighbor joining (NJ) method.   
VecDoub u;   
void premin(MatDoub &d, VecInt &nextp) {   
Before finding the minimum we (re-)calculate the u’s. Int i,j,ncurr $\qquad = \ 0$ ; Doub sum; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; $\scriptstyle \dot { 1 } > = 0$ ; $\mathrm { i } =$ nextp[i]) ncurr $^ { + + }$ ; Count live entries. for ( $\scriptstyle { \dot { 1 } } = 0$ ; $\scriptstyle \dot { 1 } > = 0$ ; $\mathrm { i } =$ nextp[i]) { Compute u[i]. sum $\mathit { \Theta } = \mathit { \Theta } 0 .$ ; for ( $\scriptstyle { \dot { \ j } } = 0$ ; $\scriptstyle { \dot { \mathsf { J } } } > = 0$ ; j=nextp[j]) if (i != j) sum $+ =$ d[i][j]; u[i] $=$ sum/(ncurr-2); } }   
Doub dminfn(MatDoub &d, Int i, Int j) { return d[i][j] - u[i] - u[j]; NJ finds min of this. }   
Doub dbranchfn(MatDoub &d, Int i, Int j) { return 0.5\*(d[i][j]+u[i]-u[j]); NJ setting for branch lengths. }   
Doub dnewfn(MatDoub &d, Int k, Int i, Int j, Int ni, Int nj) { return 0. $^ { 5 * }$ (d[i][k] $^ +$ d[j][k] - d[i][j]); NJ new distances. }   
void drootbranchfn(MatDoub &d, Int i, Int j, Int ni, Int nj,   
Doub &bi, Doub &bj) { Since NJ is unrooted, it is a matter of taste how to assign branch lengths to the root This prescription plots aesthetically. bi $=$ d[i] $[ \mathrm { j } ] * ( \mathrm { n j ~ \bar { ~ } { ~ - ~ } ~ 1 ~ + ~ } 1 . \mathsf { e } { - } 1 5 ) / ( \mathrm { n i ~ \bar { ~ } { ~ + ~ } ~ \mathrm { n j ~ \bar { ~ } { ~ - ~ } 2 ~ } ~ + ~ } 2 . \mathsf { e } { - } 1 5 ) ;$ $\bf b j ~ = ~ \bf d [ i ] ~ [ j ] * ( n i ~ \bar { ~ } \cdot ~ 1 ~ + ~ 1 . e - 1 5 ) / ( n i ~ + ~ n j ~ \bar { ~ } 2 ~ + ~ 2 . e - 1 5 ) ~ ;$   
}   
Phylo_nj(const MatDoub &dist, Int $\pounds \mathrm { s r } \ = \ - 1 $ ) : Phylagglom(dist,fsr), u(n) {makethetree(dist);}

![](images/421977378694b0da12bafb18dfa504fc4a49e1f149e5240d43bd03af9bae4719.jpg)  
Figure 16.4.5. Same data as previous figure, clustered by the neighbor-joining (NJ) method. The method yields perfect results when the input data are the metric of an additive tree (which these data are not). While displayed here as if rooted, the NJ method outputs an unrooted tree (see next figure).

Computing the $u _ { i }$ ’s is here coded as an $O ( n ^ { 2 } )$ process, but it is repeated $O ( n )$ times, so it adds $O ( n ^ { 3 } )$ to the workload. It is straightforward to make this $O ( n ^ { 2 } )$ , in line with the best coding for the rest of the tree construction. When you compute the $u _ { i }$ ’s, most distances have not changed; you just need to correct those that have. We have not coded this, just to keep the code concise.

It is important to keep in mind that the neighbor-joining method intrinsically produces an unrooted tree, regardless of how the graphical output may be drawn. Figure 16.4.5 shows the tree produced by the above code, run on the same toy example as above. It is clear by inspection that, if we want to root the tree at all, we will likely do so at some different point than the one drawn. It is for just this reason that Phylo_nj’s constructor has an optional integer argument for specifying a node as an immediate daughter to a “forced” root. (You can’t specify a new root by its node number, because it doesn’t exist yet.) Also, since you may not know how Phyloagglom has numbered its internal nodes, there is a method that returns the node number of an internal node, given two leaves that have it as their first common ancestor.

Int Phylagglom::comancestor(Int leafa, Int leafb) {   
Given the node numbers of two leaves, return the node number of their first common ancestor. Int i, j; for $\mathbf { \nabla } \cdot \mathbf { i } \mathbf { \nabla } \cdot \mathbf { \partial } \mathbf { i }$ leafa; i $\ ! =$ root; $\begin{array} { r l } { \dot { \textbf { 1 } } } & { { } = } \end{array}$ t[i].mo) { for (j $=$ leafb; j $! =$ root; $j ~ = ~ t$ [j].mo) if ( $\mathbf { \partial } _ { \cdot } \mathbf { i } \ \mathbf { \partial } _ { \cdot } = \mathbf { \partial } _ { \ j }$ ) break; if $( \dot { \textbf { 1 } } ) = = \dot { \textbf { 3 } }$ ) break; } return i;

Figure 16.4.6 shows the result of rerooting the tree of Figure 16.4.5 to the common ancestor of leaves 08 and 15. The recovered topology is now seen to be almost identical to that recovered by WPGMA, except for one additional mistake in not giving 02 and 03 a common parent.

The two figures, 16.4.5 and 16.4.6, were produced by lines of code like

![](images/0129ac4282bbe6ccd540cf2005e821311465dde0894d7186b1448de462593854.jpg)  
Figure 16.4.6. Same (NJ) tree as previous figure, but displayed with a different root, so as to produce a more balanced tree.

Mat_DP dist(n,n);   
Phylo_nj mytree(dist);   
Int $\begin{array} { r l } { \dot { \bf \lambda } _ { 1 } } & { { } = } \end{array}$ mytree.comancestor(8,15);   
Phylo_nj myrerootedtree(dist,i);

Although an unlikely application, you can use neighbor joining to test whether a given distance matrix is additive: Construct the NJ tree, and then see if its induced (branch length) distance matrix is the same as the one you started with. Analogously, you can use any of the ultrametric heuristic methods to test whether a distance matrix is ultrametric.

To view a tree produced by Phyagglom, you can use the following routine to produce an output file in the so-called “Newick” or “New Hampshire” format. Most tree viewing programs (e.g., TreeView) can read such a file. Alternatively, see Webnote [10] for a routine to convert a Phyagglom to PostScript graphics directly.

void newick(Phylagglom &p, MatChar str, char \*filename) {

Output a phylogenetic tree $\mathtt { p }$ in the “Newick” or “New Hampshire” standard format. Text labels for the leaf nodes are input as the rows of str, each a null terminated string. The output file name is specified by filename.

FILE \*OUT $=$ fopen(filename,"wb");   
Int i, s, ntask $\mathit { \Theta } = \mathit { \Theta } 0$ , ${ \mathrm { ~ n ~ } } = { \mathrm { ~ p . n ~ } }$ , root $=$ p.root;   
VecInt tasklist( $^ { 2 * \mathrm { n } + 1 }$ );   
tasklist[ntask $+ + \big ] ~ = ~ ( 1 ~ < < ~ 1 6 ) ~ + ~ \mathtt { r o o t } _ { }$ ;   
while (ntask-- $> 0 \dot { }$ ) { Depth-first traversal of the tree. $\mathrm { ~ s ~ } =$ tasklist[ntask] >> 16; Code indicating context. $\begin{array} { r l } { \dot { \mathbf { 1 } } } & { { } = } \end{array}$ tasklist[ntask] & 0xffff; Node number to be processed. if ( $\overline { { \mathrm { ~ s ~ } } } = = \mathrm { ~ 1 ~ } | \mathrm { ~ } | \mathrm { ~ \bf ~ s ~ } = = \mathrm { ~ 2 ~ } )$ $\begin{array} { r } { \mathopen { } \mathclose \bgroup \left\{ \begin{array} { r l r l } \end{array} \aftergroup \egroup \right. } \end{array}$ Left or right dau, down. tasklist[ntask++] $=$ ((s+2) << 16) + p.t[i].mo; if (p.t[i].ldau $> = ~ 0$ ) { fprintf(OUT,"("); tasklist[ntask++] $\mathbf { \Sigma } = \mathbf { \Sigma } \left( 2 \mathbf { \Sigma } < < \mathbf { \Sigma } 1 6 \right)$ $^ +$ p.t[i].rdau; tasklist[ntask++] $=$ $( 1 ~ < < ~ 1 6 )$ ) $^ +$ p.t[i].ldau; } else fprintf(OUT,"%s:%f",&str[i][0],p.t[i].modist); } else if ( $\mathbf { \hat { s } } \ = = \ 3 \cdot$ ) {if (ntask $> 0 )$ ) fprintf(OUT,",\n");} Left dau up. else if ( $\mathrm { ~ s ~ } = = \mathrm { ~ 4 ~ }$ ) { Right dau up. if ( $\begin{array} { r l } { \dot { \bar { \mathbf { 1 } } } } & { { } = = } \end{array}$ root) fprintf(OUT,");\n"); else fprintf(OUT,"):%f",p.t[i].modist); }   
}   
fclose(OUT);

# 16.4.6 Maximum Likelihood and Maximum Parsimony

Both methods that we now discuss are character-based. If you have a problem that starts with a distance matrix, you can skip this section.

Maximum likelihood (or its Bayesian equivalent, maximum posterior probability) sounds like a good idea for phylogenetic inference, but it has two crippling disabilities:

First, its exact solution requires looping over (more or less) all possible trees, so it must confront a super-exponential increase of workload with $n$ , the number of data points.

Second, since you need to compute the probability of each tree, given the terminal node (leaf) data, you need to have a precise statistical model of how trees are generated, i.e., how evolution works. While there are various such models, with varying degrees of support by empirical data, no such model can convincingly claim to be a universal truth. Under different models, maximum likelihood will produce different trees.

There are heuristic methods, e.g. quartet puzzling [11], that finesse, to some extent, the first disability, at the price of yielding “solutions” that are not necessasrily the absolute global optimum. However, the combination of both disabilities generally makes maximum likelihood a method of last resort.

Maximum parsimony shares maximum likelihood’s first disability, but not its second. Since in many situations it has proved itself to be an accurate and robust method [5], a lot of work has been done on heuristics that can overcome its workload limitations, again at the price of yielding only approximate solutions, and with significant success.

The basic idea of maximum parsimony is very simple: Consider all trees that have the observed data as their leaves. By “all trees” we mean not just all tree topologies, but rather all actual trees with interior nodes that are fully labeled by posited ancestor sequences. Now, for each such tree, define its branch lengths to be the Hamming distances between parent and child. For example, if a child’s sequence differs from its parent’s in two character positions, then their connecting branch has length two. The parsimony score for a tree is the sum of all of its branch lengths. The maximum parsimony tree is the tree with the smallest parsimony score.

It turns out that one subpart of this search can be done in a computationally efficient way. The small parsimony problem is: Given the topology of a tree over the observed leaves, find the maximum parsimony way to assign sequences to all the internal nodes. Fitch’s algorithm, which is beyond our scope to describe, solves this in $O ( n m k )$ time, where $m$ is the length of the sequences and $k$ is the number of possible values for each character (e.g., $k = 4$ for DNA bases) [1].

The hard part of maximum parsimony is therefore the search over topologies. When $n$ is less than around 17, exhaustive search is possible. For larger $n$ , various techniques including random addition order, branch swapping, hill climbing, branch and bound, simulated annealing, and genetic algorithms are used singly and in combination. In general, these can give a result with only a local maximum parsimony; but the results are often very good [1,5]. Unfortunately, the details are all beyond our allowed scope here. PAUP [7] and TNT [12,13] both implement sophisticated maximum parsimony searches.

# CITED REFERENCES AND FURTHER READING:

Felsenstein, J. 2004, Inferring Phylogenies (Sunderland, MA: Sinauer).[1]

Warnow, T. 1996, “Some Combinatorial Optimization Problems in Phylogenetics,” in Proceedings of the International Colloquium on Combinatorics and Graph Theory,eds.A. Gyarfas, L. Lovasz, L.A. Szekely, Bolyai Society Mathematical Studies, vol. 7, (Budapest: Bolyai Society).[2]   
Agarwala, R. et al. 1999, “On the Approximability of Numerical Taxonomy,” SIAM Journal of Computing,vol.28,no.3, pp.1073-1085.[3]   
Cohen, J. and Farach M. 1997, in Proceedings of the 8th Annual ACM-SIAM Symposium on Discrete Algorithms SODA '97 (Philadelphia: S.I.A.M.).[4]   
Rice, K. and Warnow, T. 1997, “Parsimony Is Hard to Beat,” in Computing and Combinatorics, 3rd Annual International Conference COCOON ’97, T. Jiang and D.T. Lee, eds. (New York: Springer).[5]   
Saitou, N. and Nei, M. 1987, “The Neighbor-joining Method: A New Method for Reconstructing Phylogenetic Trees,” Molecular Biology and Evolution, vol. 4, no. 4, pp. 406-425; see also op. cit., vol. 5, no. 6, pp. 729-731.[6]   
Swofford, D. ${ 2 0 0 4 + }$ , PAUP: Phylogenetic Analysis Using Parsimony and Other Methods, version 4, at http://paup.csit.fsu.edu/.[7]   
Felsenstein, J. $^ { 2 0 0 3 + }$ , PHYLIP: Phylogeny Inference Package, version 3.6, at http://evolution.genetics.washington.edu/phylip.html.[8]   
Hall, B.G. 2004, Phylogenetic Trees Made Easy: A How-To Manual, 2nd ed. (Sunderland, MA: Sinauer).[9]   
Numerical Recipes Software 2007, “Code for Rendering a Phylagglom Tree in Simple PostScript,” Numerical Recipes Webnote No.28,at http://www.nr.com/webnotes?28 [10]   
Strimmer, K. and von Haeseler, A. 1996, “Quartet Puzzling: A Quartet Maximum Likelihood Method for Reconstructing Tree Topologies,” Molecular Biology and Evolution, vol. 13, no. 7, pp. 964-969.[11]   
Goloboff, P.A. 1999, “Analyzing Large Data Sets in Reasonable Times: Solutions for Composite Optima,” Cladistics, vol. 15, pp. 415-428; also see http://www.cladistics.com.[12]   
Nixon, K.C. 1999, “The Parsimony Ratchet, a New Method for Rapid Parsimony Analysis,” Cladistics,vol.15, pp.407-414.[13]

# 16.5 Support Vector Machines

The support vector machine or SVM, first described by Vapnik and collaborators in 1992 [1], has rapidly established itself as a powerful algorithmic approach to the problem of classification within the larger context known as supervised learning. SVMs are no more “machines” than are Turing “machines”; the use of the word is inherited from that part of computer science long known as “machine learning.” A number of classification problems whose solutions were previously dominated by neural nets and more complicated methods have been found to be straightforwardly solvable by SVMs [2]. Moreover, SVMs are generally easier to implement than are neural nets; and it is generally easier to intuit what SVMs “think they are doing” than for neural nets, which are famous for their opaqueness.

In the supervised learning problem of classification, we are given a set of training data consisting of $m$ points,

$$
( \mathbf { x } _ { i } , y _ { i } ) \qquad i = 1 , \ldots , m
$$

Each $\mathbf { X } _ { i }$ is a feature vector in $n$ dimensions (say) that describes the data point, while each corresponding $y _ { i }$ has the value $\pm 1$ , indicating whether that data point is in $( + 1 )$ or out of $( - 1 )$ the set that we want to learn to recognize. We desire a decision rule, in the form of a function $f ( \mathbf { x } )$ whose sign predicts the value of $y$ , not just for the data in the training set, but also for new values of $\mathbf { X }$ never before seen.

For some applications, the feature vector $\mathbf { X }$ truly lives in the continuous space $\mathbf { R } ^ { n }$ . However, you are allowed to be creative in mapping your problem into this framework: In many applications, the feature vector will be a binary vector that encodes the presence or absence of many “features” (hence its name). For example, the feature vector describing a DNA sequence of length $p$ could have $n = 4 p$ dimensions, with each base position using four dimensions, and having the value one in one of the four (depending on whether it is A, C, G, or T), zero in the others.

# 16.5.1 Special Case of Linearly Separable Data

One can understand SVMs conceptually as a series of generalizations from an idealized, and rather unrealistic, starting point, We discuss these generalizations sequentially in the rest of this section. The starting point is the special case of linearly separable data. In this case, we are told (by an oracle?) that there exists a hyperplane in $n$ dimensions, that is, an $n - 1$ dimensional surface defined by the equation

$$
f ( \mathbf { x } ) \equiv \mathbf { w } \cdot \mathbf { x } + b = 0
$$

that completely separates the training data. In other words, all the training points with $y _ { i } = 1$ lie on one side of the hyperplane (and thus have $f ( \mathbf { x } _ { i } ) > 0 )$ , while all the training points with $y _ { i } = - 1$ lie on the other side (and have $f ( \mathbf { x } _ { i } ) < 0 )$ ). All we have to do is find w (a normal vector to the hyperplane) and $b$ (an offset). Then $f ( \mathbf { x } )$ in equation (16.5.2) will be the decision rule.

Actually, we can do better than this. In general, more than one hyperplane will separate linearly separable data. Let’s pick the hyperplane that has the largest margin, i.e., maximizes the perpendicular distance to points nearest to the hyperplane on both sides. Specifically, given any hyperplane that separates the data, we can always scale w by a constant and adjust $b$ appropriately, to make

$$
\begin{array} { r l } { \mathbf { w } \cdot \mathbf { x } _ { i } + b \geq + 1 } & { { } { \mathrm { ~ w h e n ~ } } y _ { i } = + 1 } \\ { \mathbf { w } \cdot \mathbf { x } _ { i } + b \leq - 1 } & { { } { \mathrm { ~ w h e n ~ } } y _ { i } = - 1 } \end{array}
$$

These equations represent parallel bounding hyperplanes that separate the data (see Figure 16.5.1), a structure whimsically called a fat plane. With a bit of analytical geometry, you can easily convince yourself that the perpendicular distance between the bounding hyperplanes (twice the margin) is

$$
2 \times \mathrm { m a r g i n } = 2 ( \mathbf { w } \cdot \mathbf { w } ) ^ { - 1 / 2 }
$$

Also note that both cases of equation (16.5.3) can be summarized as the single equation

$$
y _ { i } ( \mathbf { w } \cdot \mathbf { x } _ { i } + b ) \geq 1
$$

What we see is that the fattest fat plane, also known as the maximum margin SVM, can be found by solving a particular problem in quadratic programming:

$$
{ \left| \begin{array} { l l } { \operatorname { m i n i m i z e } ; } & { { \frac { 1 } { 2 } } \mathbf { w } \cdot \mathbf { w } } \\ { \operatorname { s u b j e c t } \operatorname { t o } ; } & { y _ { i } ( \mathbf { w } \cdot \mathbf { x } _ { i } + b ) \geq 1 \qquad i = 1 , \dots , m } \end{array} \right| }
$$

![](images/431c8826dc166326e0f65e7e2eb7bbc3381a4c8a254173d4886b3677e5037951.jpg)  
Figure 16.5.1. Support vector machine (SVM) in the idealized case of linearly separable data. We want to classify regions of the plane as containing x’s or o’s. The “fat plane” defined by $- 1 \leq f ( x ) \leq 1$ is chosen to maximize the margin (shown). At such a maximum, a small number of points, the “support vectors,” will lie on the bounding planes.

Note that we minimize $\textbf { \textrm { W } } \cdot \textbf { W }$ instead of equivalently maximizing its reciprocal. The factor of $1 / 2$ merely simplifies some algebra, later.

General methods for solving quadratic programming problems like the above are discussed in [3,4]. Later in this section, we discuss a method specialized for some SVMs. For now, consider the solution of (16.5.6) and similar problems as an available “black box.”

At a solution of (16.5.6), some (usually a small number) of the data points must lie exactly on one or the other bounding hyperplane, because, otherwise, the fat plane could have been made fatter. These data points, with $f ( \mathbf { x } ) = \pm 1$ , are called the support vectors of the solution. However, despite the fact that support vector machines were originally named after these support vectors, they don’t play much of a role in the more realistic generalizations that we will soon discuss.

# 16.5.2 Primal and Dual Problems in Quadratic Programming

The first of our promised generalizations may at first sight seem a puzzling direction to go, since it consists merely of replacing one quadratic programming problem with another. We will see later, however, that this replacement has profound consequences.

The general problem in quadratic programming, known as the primal problem, can be stated as

where $f ( \mathbf { w } )$ is quadratic in w ; $g ( \mathbf { w } )$ and $h ( \mathbf { w } )$ are affine in w (i.e., linear plus a constant); and $j$ and $k$ index, respectively, the sets of inequality and equality constraints.

Every primal problem has a dual problem, which can be thought of as an alternative way of solving the primal problem (cf. $\ S 1 0 . 1 1 . 1 \ )$ . To get from the primal to the dual, one writes a Lagrangian that incorporates both the quadratic form, and — with Lagrange multipliers — all the constraints, namely,

$$
\mathcal { L } \equiv \frac { _ 1 } { ^ 2 } f ( \mathbf { w } ) + \sum _ { j } \alpha _ { j } g _ { j } ( \mathbf { w } ) + \sum _ { k } \beta _ { k } h _ { k } ( \mathbf { w } )
$$

One then writes this subset of conditions for an extremum:

$$
\frac { \partial \mathcal { L } } { \partial w _ { i } } = 0 , \qquad \frac { \partial \mathcal { L } } { \partial \beta _ { k } } = 0 ,
$$

and uses the resulting equations algebraically to eliminate $\mathbf { W }$ from $\mathcal { L }$ , in favor of $\pmb { \alpha }$ and $\beta$ (where we now write the $\alpha _ { j }$ ’s and $\beta _ { k }$ ’s as vectors). Call the result, the reduced Lagrangian, $\mathcal { L } ( \pmb { \alpha } , \pmb { \beta } )$ . Then the important result, which follows from the so-called strong duality and Kuhn-Tucker theorems (cf. $\ S 1 0 . 1 1 . 1 \ r _ { \mathrm { ~ \normalfont ~ } }$ ), is that the solution of the following dual problem is equivalent to the original primal problem:

$$
\begin{array} { r } { \left| \begin{array} { l l } { \mathrm { m a x i m i z e : } } & { \mathcal { L } ( \pmb { \alpha } , \pmb { \beta } ) } \\ { \mathrm { s u b j e c t ~ t o : } } & { \alpha _ { j } \geq 0 \qquad \mathrm { f o r ~ a l l } \ j } \end{array} \right| } \end{array}
$$

In fact, this result is more general than quadratic programming and is true, roughly speaking, for any convex $f ( \mathbf { w } )$ . Furthermore, if $\widehat { \mathbf { w } }$ is the optimal solution of the primal problem, and $\widehat { \alpha } , \widehat { \beta }$ are the optimal solutions of the dual problem, we have

$$
\begin{array} { r } { f ( \widehat { \mathbf { w } } ) = \mathcal { L } ( \widehat { \pmb { \alpha } } , \widehat { \pmb { \beta } } ) \qquad } \\ { \widehat { \alpha } _ { j } g _ { j } ( \widehat { \mathbf { w } } ) = 0 \qquad \mathrm { ~ f o r ~ a l l ~ } j } \end{array}
$$

The latter condition is called the Karush-Kuhn-Tucker complementarity condition. It says that at least one of $\widehat { \alpha } _ { j }$ and $g _ { j } ( \widehat { \mathbf { w } } )$ must be zero for each $j$ . (We previously met the linear case in equation 10.11.5.) This means that, from the solution of the dual problem, you can instantly identify inequality constraints in the primal problem that are “pinned” against their limit, namely those with nonzero $\widehat { \alpha } _ { j }$ ’s in the solution of the dual.

# 16.5.3 Dual Formulation of the Maximum Margin SVM

The above procedure is readily performed on the quadratic programming problem (16.5.6) for the maximum margin SVM. There are no $\beta _ { k }$ ’s, since there are no equality constraints. The Lagrangian (16.5.8) is

$$
\mathcal { L } = \frac { 1 } { 2 } \mathbf { w } \cdot \mathbf { w } + \sum _ { i } \alpha _ { i } [ 1 - y _ { i } ( \mathbf { w } \cdot \mathbf { x } _ { i } + b ) ]
$$

The conditions for an extremum are

$$
0 = { \frac { \partial { \mathcal { L } } } { \partial \mathbf { w } } } = \mathbf { w } - \sum _ { i } \alpha _ { i } y _ { i } \mathbf { x } _ { i } \quad \implies \quad { \widehat { \mathbf { w } } } = \sum _ { i } { \widehat { \alpha } } _ { i } y _ { i } \mathbf { x } _ { i }
$$