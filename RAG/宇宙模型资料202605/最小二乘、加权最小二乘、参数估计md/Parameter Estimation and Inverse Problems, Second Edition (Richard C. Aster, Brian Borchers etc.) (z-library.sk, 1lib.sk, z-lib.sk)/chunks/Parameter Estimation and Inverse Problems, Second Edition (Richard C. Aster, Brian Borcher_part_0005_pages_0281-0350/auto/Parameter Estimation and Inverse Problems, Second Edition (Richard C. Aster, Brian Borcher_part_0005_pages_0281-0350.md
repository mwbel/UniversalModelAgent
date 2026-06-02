A Markov chain is a sequence of random variables,

$$
X ^ { 0 } , X ^ { 1 } , X ^ { 2 } , \ldots ,
$$

where the probability distribution of $X ^ { n + 1 }$ depends solely on the previous value, $X ^ { n }$ , and not on earlier values of random variables in the sequence. That is,

$$
P ( X ^ { n + 1 } | X ^ { 0 } , X ^ { 1 } , \ . \ . \ . \ , X ^ { n } ) = P ( X ^ { n + 1 } | X ^ { n } ) .
$$

The particular Markov chains considered here will be time-invariant, so that the Markov chain transition kernel

$$
P ( X ^ { n } , X ^ { n + 1 } ) = P ( X ^ { n + 1 } | X ^ { n } )
$$

is independent of $n$ .

For example, consider a one-dimensional random process in which we start at $X ^ { 0 } = 0$ , and then iteratively compute $X ^ { n + 1 }$ from $X ^ { n }$ by adding an $N ( 0 , \sigma ^ { 2 } )$ realization to $X ^ { n }$ . Clearly $X ^ { n + 1 }$ depends directly on $X ^ { n }$ , and this dependence is time-invariant. The transition kernel for this Markov chain is

$$
k ( x _ { 1 } , x _ { 2 } ) = \frac { 1 } { \sqrt { 2 \pi } \sigma } e ^ { - \frac { 1 } { 2 } ( x _ { 1 } - x _ { 2 } ) ^ { 2 } / \sigma ^ { 2 } } .
$$

In the MCMC method, we are interested in Markov chains that have limiting distributions, $q ( \mathbf { x } )$ , such that

$$
\operatorname* { l i m } _ { n  \infty } { \cal P } ( X ^ { n } | X ^ { 0 } ) = q ( { \bf x } ) .
$$

Not all Markov chains have limiting distributions. For example, if $X ^ { n }$ is the sum of $n$ independent $N ( 0 , \sigma ^ { 2 } )$ random variables, $X ^ { n }$ has an $N ( 0 , n \sigma ^ { 2 } )$ distribution. This does not approach a limiting probability distribution as $n \to \infty$ .

For a general multivariate model, it can be shown that if $q ( \mathbf { x } )$ and $k ( \mathbf { x } , \mathbf { y } )$ satisfy the local balance equation

$$
q ( \mathbf { x } ) k ( \mathbf { x } , \mathbf { y } ) = q ( \mathbf { y } ) k ( \mathbf { y } , \mathbf { x } )
$$

for all models $\mathbf { x }$ and $\mathbf { y }$ , then $q ( \mathbf { x } )$ is the limiting distribution of the Markov chain. Equation (11.44) states that the rate of model transitions from $\mathbf { x }$ to $\mathbf { y }$ equals the rate from $\mathbf { y }$ to $\mathbf { x }$ .

The Metropolis-Hastings sampler is an algorithm that simulates a Markov chain with a specified limiting distribution. We will apply it to produce samples from a posterior distribution $q ( \mathbf { m } | \mathbf { d } )$ that will tend to densely sample its higher likelihood regions. With enough such samples, we can usefully characterize the posterior distribution of a Bayesian parameter estimation or inverse problem. Since the data vector $\mathbf { d }$ is given, we will simply write $q ( \mathbf { m } | \mathbf { d } )$ as $q ( \mathbf { m } )$ throughout the following development.

We begin a Metropolis-Hastings sampler implementation by picking a proposal distribution $r ( \mathbf { x } , \mathbf { y } )$ that facilitates random steps in the posterior model space. These randomly perturbed samples will subsequently be subjected to a likelihood-based test in the Metropolis-Hastings sampler. A common choice for the proposal distribution is an MVN distribution with zero covariances and variances $\sigma _ { i } ^ { 2 }$ , so that

$$
r ( x _ { i } , \ \gamma _ { i } ) \propto e ^ { - \frac { 1 } { 2 } ( x _ { i } - \gamma _ { i } ) ^ { 2 } / \sigma _ { i } ^ { 2 } } .
$$

Although $r ( \mathbf { x } , \mathbf { y } )$ cannot be implemented as a transition kernel directly, because it does not satisfy (11.44), this can be remedied by introducing a factor called the acceptance ratio,

$$
\alpha ( \mathbf { x } , \mathbf { y } ) = \operatorname* { m i n } ( 1 , s ) ,
$$

where

$$
s = \frac { q ( \mathbf { y } ) r ( \mathbf { y } , \mathbf { x } ) } { q ( \mathbf { x } ) r ( \mathbf { x } , \mathbf { y } ) } .
$$

Note that $0 \leq \alpha ( \mathbf { x } , \mathbf { y } ) \leq 1$ . Also note that

$$
\alpha ( \mathbf { y } , \mathbf { x } ) = \operatorname* { m i n } { \big ( } 1 , s ^ { - 1 } { \big ) } .
$$

At least one of $\alpha ( \mathbf { x } , \mathbf { y } )$ and $\alpha ( \mathbf { y } , \mathbf { x } )$ will thus be equal to 1, depending on whether $s$ is greater than or less than 1.

Now, let

$$
\tilde { k } ( \mathbf { x } , \mathbf { y } ) = \alpha ( \mathbf { x } , \mathbf { y } ) r ( \mathbf { x } , \mathbf { y } ) .
$$

$\alpha ( \mathbf { x } , \mathbf { y } ) \leq 1$ , so

$$
\beta ( x ) = \int _ { \mathrm {  ~ \scriptstyle { \tau } ~ } , \mathrm {  ~ { \tau } ~ } } \tilde { k } ( { \bf x } , { \bf y } ) \ d { \bf y } = \int _ { \mathrm {  ~ \scriptstyle { \tau } ~ } , \mathrm {  ~ { \tau } ~ } } \alpha ( { \bf x } , { \bf y } ) r ( { \bf x } , { \bf y } ) \ d { \bf y } \leq 1 .
$$

Thus $\tilde { k } ( \mathbf { x } , \mathbf { y } )$ is not a properly normalized transition kernel. We can, however, obtain a normalized kernel by defining

$$
k ( \mathbf { x } , \mathbf { y } ) = \tilde { k } ( \mathbf { x } , \mathbf { y } ) + ( 1 - \beta ) \delta ( \mathbf { x } - \mathbf { y } )
$$

so that

all

$$
\begin{array} { r l r }    \int _ { \mathrm {  ~ \scriptstyle { \Psi ~ } } } k ( \mathbf { x } , \mathbf { y } ) \ d y = \begin{array} { l } { \displaystyle \int _ { \mathrm {  ~ \scriptstyle { \Psi ~ } } } \alpha ( \mathbf { x } , \mathbf { y } ) r ( \mathbf { x } , \mathbf { y } ) \ d \mathbf { y } + \small { \int _ { \mathrm {  ~ \scriptstyle { \Psi ~ } } } } ( 1 - \beta ) \delta ( \mathbf { x } - \mathbf { y } ) \ d \mathbf { y } } \\ { \mathrm {  ~ \scriptstyle { \Psi ~ } ~ } \mathrm {  ~ \scriptstyle { \Psi ~ } ~ } \mathrm {  ~ \scriptstyle { \Psi ~ } ~ } \mathrm {  ~ \scriptstyle { \Psi ~ } ~ } \mathrm { \scriptscriptstyle { \mathrm {  ~ \scriptstyle { ~ \psi ~ } } ~ } } } \end{array} \end{array}
$$

A simple algorithm can now be used to generate a random value $\mathbf { y }$ from $\mathbf { x }$ that satisfies (11.44).

# Algorithm 11.1 Transition Kernel Evaluation

1. Generate a candidate $\mathbf { y }$ from $\mathbf { x }$ according to the proposal distribution $r ( \mathbf { x } , \mathbf { y } )$ .   
2. Compute $\alpha ( \mathbf { x } , \mathbf { y } )$ .   
3. With probability $\alpha$ , return the candidate $\mathbf { y }$ .   
4. With probability $1 - \alpha$ , return the previous value $\mathbf { x }$ .

Now, we need to show that $q ( \mathbf { x } )$ and $k ( \mathbf { x } , \mathbf { y } )$ as defined above satisfy the local balance equation (11.44). If $\mathbf { y } = \mathbf { x }$ , this is obviously true. For $\mathbf { y } \neq \mathbf { x }$ , we need to consider the two cases of $\alpha ( \mathbf { x } , \mathbf { y } ) = 1$ or $\alpha ( \mathbf { y } , \mathbf { x } ) = 1$ . If $\alpha ( \mathbf { x } , \mathbf { y } ) = 1$ , then

$$
\alpha ( \mathbf { y } , \mathbf { x } ) = s ^ { - 1 } = \frac { q ( \mathbf { x } ) r ( \mathbf { x } , \mathbf { y } ) } { q ( \mathbf { y } ) r ( \mathbf { y } , \mathbf { x } ) }
$$

and

$$
q ( { \bf x } ) k ( { \bf x } , { \bf y } ) = q ( { \bf x } ) \alpha ( { \bf x } , { \bf y } ) r ( { \bf x } , { \bf y } ) = q ( { \bf x } ) r ( { \bf x } , { \bf y } ) .
$$

Also,

$$
q ( { \bf y } ) k ( { \bf y } , { \bf x } ) = q ( { \bf y } ) \alpha ( { \bf y } , { \bf x } ) r ( { \bf y } , { \bf x } ) = q ( { \bf y } ) \frac { q ( { \bf x } ) r ( { \bf x } , { \bf y } ) } { q ( { \bf y } ) r ( { \bf y } , { \bf x } ) } r ( { \bf y } , { \bf x } ) = q ( { \bf x } ) r ( { \bf x } , { \bf y } ) .
$$

However, $q ( \mathbf { x } ) r ( \mathbf { x } , \mathbf { y } ) = q ( \mathbf { x } ) k ( \mathbf { x } , \mathbf { y } )$ , so

$$
q ( \mathbf { y } ) k ( \mathbf { y } , \mathbf { x } ) = q ( \mathbf { x } ) k ( \mathbf { x } , \mathbf { y } ) ,
$$

thus satisfying (11.44). A similar argument shows that (11.44) is satisfied for the case where $\alpha ( \mathbf { y } , \mathbf { x } ) = 1$ .

There are several important tactics that help to simplify the method further. Because the product of $q$ and $r$ appears in both the numerator and denominator of $s$ , we need only know these factors to constants of proportionality, and thus do not need to normalize $q$ and $r$ in individual calculations. Also note that the posterior distribution, $q ( \mathbf { m } )$ , is proportional to the product of the prior, $p ( \mathbf { m } )$ , and the likelihood, $f ( \mathbf { d } | \mathbf { m } )$ (11.3). We can thus write (11.46) as

$$
\begin{array} { r } { \alpha ( \mathbf { x } , \mathbf { y } ) = \operatorname* { m i n } { \left( 1 , \frac { p ( \mathbf { y } ) f ( \mathbf { d } | \mathbf { y } ) r ( \mathbf { y } , \mathbf { x } ) } { p ( \mathbf { x } ) f ( \mathbf { d } | \mathbf { x } ) r ( \mathbf { x } , \mathbf { y } ) } \right) } . } \end{array}
$$

If $r ( \mathbf { x } , \mathbf { y } )$ is a symmetric distribution, such as (11.45), then $r ( \mathbf { x } , \ \mathbf { y } ) = r ( \mathbf { y } , \ \mathbf { x } )$ , and we can simplify (11.57) to

$$
\alpha ( \mathbf { x } , \mathbf { y } ) = \operatorname* { m i n } { \left( 1 , \frac { q ( \mathbf { y } ) } { q ( \mathbf { x } ) } \right) } .
$$

In computational practice, numbers in the numerator of (11.58) may be extremely small, and can thus generate floating point underflow problems. This is easily avoided by evaluating $\log \alpha ( \mathbf { x } , \mathbf { y } )$ instead of $\alpha ( \mathbf { x } , \mathbf { y } )$ . We now have all the components to describe the Metropolis-Hastings sampler.

# Algorithm 11.2 The Metropolis-Hastings Sampler

Given a starting model, $\mathbf { m } ^ { 0 }$ , repeat the following steps for $j = 1 , 2 , \dots { }$ . until the posterior distribution is sufficiently sampled by the set of models $\mathbf { m } ^ { j }$ .

1. Generate a candidate model $\mathbf { c }$ from the previous model, $\mathbf { m } ^ { j }$ , using the proposal distribution $r ( \mathbf { m } ^ { j } , \mathbf { c } )$ .   
2. Compute log $\alpha ( \mathbf { m } ^ { j } , \mathbf { c } )$ .   
3. Let $t$ be a realization of a uniformly distributed random variable on [0, 1].   
4. If $\log \ t < \log \alpha ( \mathbf { m } ^ { j } , \mathbf { c } )$ , then accept the candidate model and let $\mathbf { m } ^ { j + 1 } = \mathbf { c }$ ; otherwise reject the candidate model and let $\mathbf { m } ^ { j + 1 } = \mathbf { m } ^ { j }$ .

Note that if $\log t$ is quite small, we will occasionally accept a new model that has a small acceptance ratio and thus move towards a model with reduced likelihood. This property of the algorithm helps overcome the problem of having the sampling become trapped near a localized likelihood maximum. The behavior of the algorithm and its ability to sample the posterior distribution fruitfully and efficiently will depend on the size of the steps taken in generating candidate models. In the case of the normal formulation for the proposal distribution (11.45), this will be controlled by the size of the $\sigma _ { i }$ . Smaller steps will result in higher acceptance rates, but the algorithm may be unacceptably slow at exploring the posterior distribution. Conversely, larger steps will result in lower acceptance ratios and will thus be less frequently accepted. Either situation may cause the algorithm to become stuck in a particular region of the posterior distribution. Often, the step size parameters are explored adaptively in multiple runs of the algorithm (which may be run as independent parallel processes on a multi-CPU computer system). Some studies, e.g., [51], suggest that the algorithm is optimally tuned when the new model acceptance rate is between approximately $20 \%$ and $50 \%$ .

# 11.5. ANALYZING MCMC OUTPUT

Although the limiting distribution of the Markov chain sampled by the Metropolis-Hastings algorithm is the desired posterior distribution, there are significant practical challenges in analyzing the output of an MCMC simulation.

First, successive models $m ^ { k }$ , $m ^ { k + 1 }$ , $m ^ { k + 2 }$ , . . . , produced by the simulation are typically strongly correlated with each other, but most statistical techniques require independent samples. In practice, this complication can be avoided by analyzing a subset of samples that are far apart in the sample sequence. For example, if we examine $\mathbf { m } ^ { k }$ , $\mathbf { m } ^ { k + 1 0 0 0 }$ , $\mathbf { m } ^ { k + 2 0 0 0 }$ , . . . , it is likely that samples taken 1000 steps apart will not be highly correlated. We can verify this by plotting the successive model autocorrelations for the history of sampling over some moving window length.

Second, early Metropolis-Hastings algorithm samples will be biased by the initial model $\mathbf { m } ^ { 0 }$ , which may not lie in a high likelihood region of the posterior distribution. This issue is commonly addressed by skipping over early samples in the chain to give time for the algorithm to “burn in,” and/or by running the process with a variety of starting models, either sequentially or in parallel on multiple CPUs. For example, if it is determined that samples spaced 1000 steps apart are effectively uncorrelated, then it might be reasonable to let the Metropolis-Hastings sampler establish itself for 10,000 steps before beginning to collect samples.

Once we are confident that the procedure has produced a large enough collection of effectively independent samples, we can use the results to characterize the posterior distribution. For a suitably large sample, the MAP solution can be estimated as the retrieved posterior distribution sample that has the greatest likelihood. The posterior distribution may be approximately multivariate normal, which can be established by examining model histograms and quantile-quantile (Q-Q) plots. In this case we can readily construct probability intervals for describing the posterior distribution from the sample mean and covariance using normal assumptions. However, if the distribution is distinctly non-normal, it will be more difficult to produce a simple summary of its character, particularly for very high dimensional models. A common approach is to produce and evaluate scatter plots and/or histograms that display key features of the posterior distribution and to use counting statistics to establish probability intervals.

# Example 11.4

Reconsidering the ill-posed nonlinear parameter estimation problem of Example 9.2, we apply the Metropolis-Hastings algorithm to the problem of fitting four parameters, $m _ { i }$ , to the nonlinear function

$$
d _ { i } = ( G ( \mathbf { m } ) ) _ { i } = m _ { 1 } e ^ { m _ { 2 } x _ { i } } + m _ { 3 } x _ { i } e ^ { m _ { 4 } x _ { i } }
$$

given a set of observations, $d _ { i }$ , with specified independent normally distributed data noise, specified by corresponding standard deviations $\sigma _ { i }$ . As in Example 9.2, the true model parameters are $m _ { 1 } = 1 . 0 , \ m _ { 2 } = - 0 . 5 , \ m _ { 3 } = 1 . 0 ,$ , and $m _ { 4 } = - 0 . 7 5$ ; data are produced at 25 equally spaced points, $x _ { i }$ , on the interval [1, 7]; and $N ( 0 , 0 . 0 1 ^ { 2 } )$ independent noise is added to each data element. The likelihood function is specified by

$$
f ( \mathbf { d } | \mathbf { m } ) \propto \prod _ { i = 1 } ^ { m } e ^ { - \frac { 1 } { 2 } ( d _ { i } - G ( \mathbf { m } ) _ { i } ) ^ { 2 } / \sigma _ { i } ^ { 2 } } ,
$$

which, after taking the natural logarithm, is

$$
\log ( f ( \mathbf { d } | \mathbf { m } ) ) = - \frac { 1 } { 2 } \sum _ { i = 1 } ^ { m } ( d _ { i } - G ( \mathbf { m } ) _ { i } ) ^ { 2 } / \sigma _ { i } ^ { 2 } + C ,
$$

where $C$ is the logarithm of the constant of proportionality in (11.60). We sample the posterior distribution using 410,000 steps, and produce a low-correlation set of 400 samples by allowing a 10,000 sample burn in and selecting subsequent samples spaced 1000 steps apart by down-sampling the full 410,000 length sequence. The procedure was initiated using a random model selected from a 4-dimensional uniform distribution bounded by $[ - 1 , 1 ]$ in each parameter direction and applying a uniform prior for the region $m _ { 1 } = [ 0 , 2 ]$ , $m _ { 2 } = [ - 1 , 0 ]$ , $m _ { 3 } = [ 0 , 2 ]$ , and $m _ { 4 } = [ - 1 , 0 ]$ . In each of the MCMC steps, we apply independent normally distributed random perturbations with standard deviations of 0.005 in each of the four model parameter directions, accepting or rejecting the corresponding candidate models according to the Metropolis-Hastings algorithm. The procedure produced an acceptance rate of approximately $3 9 . 5 \%$ , which is in the nominally acceptable range of not being too large or too small [51].

![](images/fff9738852e6a1b06f006ca74348f591dcb55c1258f9318494547abfd9f177aa.jpg)  
Figure 11.14 Sampled posterior distribution for Example 11.3. The true model is shown as the large black dot, and the MAP model estimated from the maximum likelihood posterior distribution sample is indicated by the open circle. 400 retrieved samples of the posterior distribution (every 1000th calculated sample from the MCMC output) are shown as gray dots. Ninety-five percent probability intervals estimated from the MCMC posterior distribution samples are shown by boxes.

Figure 11.14 shows scatter plots and histograms of the resulting sampled posterior distribution, along with the corresponding MAP solution and $9 5 \%$ probability intervals for each parameter direction, which well enclose the true solution. Figure 11.15 shows the time history of the corresponding 400 samples. The prominent quasilinear scattering trends in the output between $m _ { 2 }$ and $m _ { 3 }$ are indicative of a high degree of anticorrelation between some parameter pairs. This anticorrelation is also apparent in the sequence of parameter samples in Figure 11.15, for example in the anticorrelated trends of $m _ { 2 }$ and m3. An examination of the parameter autocorrelations for the samples shown in Figure 11.14 (Figure 11.16) shows that individual parameter estimates are effectively decorrelated after 20 or fewer steps. Figure 11.17 shows a histogram of the natural log of likelihood values for the posterior samples. The multimodal nature of this histogram is reflective of the “bumpy” likelihood function surface for this ill-posed problem with random data noise, a situation that also resulted in multiple solutions when we applied classical nonlinear solution methods in Example 9.2. However, the MCMC method here provided a sufficiently thorough search of the model space to allow us to discriminate the MAP solution from solutions corresponding to subsidiary likelihood maxima.

![](images/698eb19fb1d3779bfd3cb4fc96b2410f9c07f822f955ed4b303e639d1c746e88.jpg)  
Figure 11.15 Time history of the posterior samples plotted in Figure 11.14. True parameters are shown as gray lines.

![](images/6d7295f0add0d254e3552708048a8687db1695bd25701f520eb393ccdb08d59e.jpg)  
Figure 11.16 Twenty-point autocorrelations for posterior distribution parameters shown in Figure 11.15.

![](images/fee2f04818f682d736a9619f14784b2196421a05ade3ae29601ed1194df60d7c.jpg)  
Figure 11.17 Natural logarithm of the likelihood function for the 400 posterior distribution samples shown in Figures 11.14 and 11.15. The value for the true model is approximately −10 2, and the value for the MAP model is approximately $- 8 . 7$ .

# 11.6. EXERCISES

1. Reanalyze the data in Example 11.1 using a prior distribution that is uniform on the interval [9, 11]. Compute the posterior distribution after the first measurement of $1 0 . 3 ~ \mu \mathrm { g }$ and after the second measurement of $1 0 . 1 ~ { \mu \mathrm { g } }$ . What is the posterior mean?

2. Consider the estimation problem $\mathbf { d } = \mathbf { m }$ (i.e., where $\mathbf { G } = \mathbf { I } )$ ) in two dimensions. The data, $\mathbf { d } = [ 5 \ 1 5 ] ^ { T } ,$ have identical and independent normal errors with standard deviations of $\sqrt { 2 }$ . Apply a zero-mean MVN prior characterized by a covariance matrix where $m _ { 1 }$ and $m _ { 2 }$ have a correlation coefficient of 0.9, and equal standard deviations of $\sqrt { 5 }$ . Calculate the MAP model, and compute and plot the $50 \%$ , $90 \%$ , and $9 5 \%$ contours of the MVN distributions d, $\mathbf { m } _ { \mathrm { p r i o r } }$ , and the posterior model.

3. In writing (11.28) we made use of the matrix square root.

a. Suppose that A is a symmetric and positive definite matrix. Using the SVD, find an explicit formula for the matrix square root. Your square root should itself be a symmetric and positive definite matrix.   
b. Show that instead of using the matrix square roots of $\mathbf { C } _ { D } ^ { - 1 }$ and $\mathbf { C } _ { M } ^ { - 1 }$ , we could have used the Cholesky factorizations of $\mathbf { C } _ { D } ^ { - 1 }$ and $\mathbf { C } _ { M } ^ { - 1 }$ in formulating the least squares problem.

4. Consider the following coin tossing experiment. We repeatedly toss a coin, and each time record whether it comes up heads (0) or tails (1). The bias $b$ of the coin is the probability that it comes up heads. We have reason to believe that this is not a fair coin, so we will not assume that $b = 1 / 2$ . Instead, we will begin with a uniform prior distribution $p ( b ) = 1$ , for $0 \leq b \leq 1$ .

a. What is $f ( d | b ) \Rsh$ Note that the only possible data are 0 and 1, so this distribution will involve delta functions at $d = 0$ , and $d = 1$ .   
b. Suppose that on our first flip, the coin comes up heads. Compute the posterior distribution $q ( b | d _ { 1 } = 0 )$ .   
c. The second, third, fourth, and fifth flips are 1, 1, 1, and 1. Find the posterior distribution $q ( b | d _ { 1 } = 0 , d _ { 2 } = 1 , d _ { 3 } = 1 , d _ { 4 } = 1 , d _ { 5 } = 1 )$ . Plot the posterior distribution.   
d. What is your MAP estimate of the bias?   
e. Now, suppose that you initially felt that the coin was at least close to fair, with

$$
\begin{array} { r } { p ( b ) \propto e ^ { - 1 0 ( b - 0 . 5 ) ^ { 2 } } \quad 0 \leq b \leq 1 . } \end{array}
$$

Repeat the analysis of the five coin flips described above.

5. Apply the Bayesian method to Exercise 2 in Chapter 4. Select what you consider to be a reasonable prior. How sensitive is your solution to the prior mean and covariance?

6. Apply the Bayesian method to Exercise 9.3. Assume an MVN prior distribution for $\alpha$ and $n$ , with $\alpha$ and $n$ independent. The prior for $\alpha$ should have a mean of 0.01 and a standard deviation of 0.005, and the prior for $n$ should have a mean of 5 and a standard deviation of 3. Compare your solution with the solution that you obtained to Exercise 9.3. How sensitive is your solution to the choice of the prior?

7. Repeat Exercise 11.6, using MCMC to estimate the posterior distribution. Compare your solution to the solution that you obtained for Exercise 11.6.

8. Apply the Metropolis-Hastings sampler to produce a sampled posterior distribution for the nonlinear parameter estimation problem of Example 9.1. Use a prior distribution that is uniform on $S = [ 0 , 0 . 0 1 ]$ and $T = [ 0 , 2 ]$ , a zero covariance MVN proposal distribution, and a starting model of $( S , \ T ) = ( 5 \times 1 0 ^ { - 3 }$ , 1.0). Generate 200,000 samples using a 10,000-sample burn-in and explore independent step sizes for the two parameters in your proposal distribution to obtain a Metropolis-Hastings sampler acceptance rate between $10 \%$ and $50 \%$ . Extract every 1000th sample for analysis and establish that these 191 samples are not highly dependent by examining sample autocorrelation functions. Examine the sampled distribution to obtain the MAP model and empirical $9 5 \%$ probability intervals on $S$ and $T$ . Apply a $\mathrm { Q - }$ $\mathrm { Q }$ plot and assess the multivariate normality of the sampled posterior distribution and compare normal assumption and empirical estimates of the $9 5 \%$ probability intervals.

9. Apply the Metropolis-Hastings sampler to produce a sampled posterior distribution for the nonlinear inverse problem for gravity observations above a buried density perturbation with an unknown variable depth $m ( x )$ and a fixed density perturbation $\Delta \rho$ , as described in Exercise 10.2. Your prior should be selected to favor smooth (specified by nonzero parameter correlations) models.

# 11.7. NOTES AND FURTHER READING

The arguments for and against the use of Bayesian methods in statistics and inverse problems have raged for decades. Some classical references that provide context for these arguments include [35, 42, 80, 81, 136]. Sivia and Skilling’s book [143] is a good general introduction to Bayesian ideas for scientists and engineers. The book by Calvetti and Somersalo introduces Bayesian methods for inverse problems including Markov Chain Monte Carlo sampling and includes MATLAB examples [22]. The book by Kaipio and Somersalo provides a more detailed theoretical treatment of Bayesian methods for inverse problems and includes some interesting case studies [83]. An early paper by Tarantola and Valette on the application of the Bayesian approach was quite influential [156], and Tarantola’s book is the standard reference work on Bayesian methods for inverse problems [155]. The book by Rodgers [133] focuses on application of the Bayesian approach to problems in atmospheric sounding. The paper by Gouveia and Scales [56] discusses the relative advantages and disadvantages of Bayesian and classical methods for inverse problems. The draft textbook by Scales and Smith [137] takes a Bayesian approach to inverse problems.

In many cases the solution to an inverse problem will be used in making a decision, with measurable consequences for making the “wrong” decision. Statistical decision theory can be helpful in determining the optimal decision. The paper by Evans and Stark provides a good introduction to the application of statistical decision theory to inverse problems [48].

# Epilogue

The theme of this book has been obtaining and analyzing solutions to discretized parameter estimation problems using classical and Bayesian approaches. We have discussed computational procedures for both linear and nonlinear problems. Classical procedures produce estimates of the parameters and their associated uncertainties. In Bayesian methods, the model is a random variable, and the solution is its probability distribution.

However, there are critical issues that arise in solving these problems. When we discretize a continuous problem, the choice of the discretization scheme, basis functions, and grid spacing can have large effects on the behavior of the discretized problem and its solutions, and these effects will not be reflected in the statistical analysis of the solution of the discretized problem. The discretization errors in the solution could potentially be far larger than any explicitly computed statistical uncertainty. Thus it is important to ensure that the discretization provides an adequate approximation to the continuous problem. If no formal analysis is performed, it is at least desirable to see whether varying the discretization has a significant effect on the solutions obtained.

For well-conditioned problems with normally distributed measurement errors, we can use the classical least squares approach. This results in unbiased parameter estimates and associated confidence intervals. For ill-conditioned problems, and for problems where we have good reason to prefer a specific bias in the character of the solution, Tikhonov regularization can be applied to obtain a solution. However, regularization introduces bias into the solution, and it is impossible to even bound this bias without making additional assumptions about the model.

Although Bayesian approaches are also applicable to well-conditioned situations, they are particularly interesting in the context of ill-conditioned problems. By selecting a prior distribution, we make explicit assumptions about the model. The resulting posterior distribution is not affected by regularization bias. In the multivariate normal case for linear problems the Bayesian approach is no more difficult computationally than the least squares approach.

Various efforts have been made to avoid the use of subjective priors in the Bayesian approach. Principles such as maximum entropy can be used to derive prior distributions that have been claimed to be, in some sense, “objective.” However, we do not find these arguments completely convincing, and in many cases the choice of prior has a similar effect on the choice of the regularization operations in Tikhonov and other classical approaches. Markov Chain Monte Carlo methods present a computationally intensive methodology to sample and characterize the Bayesian posterior distribution using forward model-based likelihood calculations.

Both the classical and Bayesian approaches can be extended to nonlinear inverse problems. The computation of the estimated model parameters becomes substantially more complex in that we must solve nonlinear optimization problems which may have multiple locally optimal solutions. In both standard approaches, the statistical analysis is typically performed approximately by analyzing a linearization of the nonlinear model around the estimated parameters. However, the validity of this approach will depend on the data uncertainties and the nonlinearity of the problem. The Bayesian approach can in theory be applied when measurement errors are not normally distributed. In practice, however, the associated analytical computations can be difficult. Markov Chain Monte Carlo methods provide a very general approach for characterizing the posterior distribution that avoids the difficulties of computing it in analytical form.

# APPENDIX A

# Review of Linear Algebra

# Synopsis

A summary of essential concepts, definitions, and theorems in linear algebra used throughout this book.

# A.1. SYSTEMS OF LINEAR EQUATIONS

Recall that a system of linear equations can be solved by the process of Gaussian elimination.

# Example A.1

Consider the following system of equations:

$$
\begin{array} { l } { { x _ { 1 } + 2 x _ { 2 } + 3 x _ { 3 } = 1 4 } } \\ { { \qquad } } \\ { { x _ { 1 } + 2 x _ { 2 } + 2 x _ { 3 } = 1 1 } } \\ { { \qquad } } \\ { { x _ { 1 } + 3 x _ { 2 } + 4 x _ { 3 } = 1 9 . } } \end{array}
$$

We eliminate $x _ { 1 }$ from the second and third equations by subtracting the first equation from the second and third equations to obtain

$$
\begin{array} { r l r } & { } & { x _ { 1 } + 2 x _ { 2 } + 3 x _ { 3 } = 1 4 } \\ & { } & { - x _ { 3 } = - 3 } \\ & { } & { x _ { 2 } + x _ { 3 } = 5 . } \end{array}
$$

We would like $x _ { 2 }$ to appear in the second equation, so we interchange the second and third equations:

$$
\begin{array} { r } { x _ { 1 } + 2 x _ { 2 } + 3 x _ { 3 } = ~ 1 4 } \\ { x _ { 2 } + x _ { 3 } = ~ 5 } \\ { - x _ { 3 } = - 3 . } \end{array}
$$

Next, we eliminate $x _ { 2 }$ from the first equation by subtracting two times the second equation from the first equation:

$$
\begin{array} { c } { { x _ { 1 } + x _ { 3 } = ~ 4 } } \\ { { x _ { 2 } + x _ { 3 } = ~ 5 } } \\ { { - x _ { 3 } = - 3 . } } \end{array}
$$

We then multiply the third equation by $- 1$ to get an equation for $x _ { 3 }$

$$
\begin{array} { r } { x _ { 1 } + x _ { 3 } = 4 } \\ { x _ { 2 } + x _ { 3 } = 5 } \\ { x _ { 3 } = 3 . } \end{array}
$$

Finally, we eliminate $x _ { 3 }$ from the first two equations to obtain a solution to the original system of equations:

$$
\begin{array} { l } { x _ { 1 } = 1 } \\ { x _ { 2 } = 2 } \\ { x _ { 3 } = 3 . } \end{array}
$$

Geometrically the constraints specified by the three equations of (A.1) describe three planes that, in this case, intersect in a single point, $x _ { 1 } = 1$ , $x _ { 2 } = 2$ , $x _ { 3 } = 3$ .

In solving (A.1), we used three elementary row operations: adding a multiple of one equation to another equation, multiplying an equation by a nonzero constant, and swapping two equations. This process can be extended to solve systems of equations with an arbitrary number of variables.

In performing the elimination process, the actual names of the variables are insignificant. We could have renamed the variables in the above example to $a , b$ , and $c$ without changing the solution in any significant way. Because the actual names of the variables are insignificant, we can save space by writing down the significant coefficients from the system of equations in matrix form as an augmented matrix. The augmented matrix form is also useful in solving a system of equations in computer algorithms, where the elements of the augmented matrix are stored in an array.

In augmented matrix form (A.1) becomes

$$
{ \left[ \begin{array} { l l l } { 1 } & { 2 } & { 3 } \\ { 1 } & { 2 } & { 2 } \\ { 1 } & { 3 } & { 4 } \end{array} \right] } \ 1 4 { \bigg ] } .
$$

In augmented notation, the elementary row operations become adding a multiple of one row to another row, multiplying a row by a nonzero constant, and interchanging

two rows. The Gaussian elimination process is essentially identical to the process used in Example A.1, with the final version of the augmented matrix given by

$$
{ \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { 1 } \\ { 2 } \\ { 3 } \end{array} \right] } .
$$

Definition A.1 A matrix is said to be in reduced row echelon form (RREF) if it has the following properties:

1. The first nonzero element in each row is a 1. The first nonzero row elements of the matrix are called pivot elements. A column in which a pivot element appears is called a pivot column.   
2. Except for the pivot element, all elements in pivot columns are 0s.   
3. Each pivot element is to the right of the pivot elements in previous rows.   
4. Any rows consisting entirely of 0s are at the bottom of the matrix.

In solving a system of equations in augmented matrix form, we apply elementary row operations to reduce the augmented matrix to RREF and then convert back to conventional notation to read off the solutions. The process of transforming a matrix into RREF can easily be automated. In MATLAB, this is done by the rref command.

It can be shown that any linear system of equations has either no solutions, exactly one solution, or infinitely many solutions [95]. In a system of two dimensions, for example, lines represented by the equations can fail to intersect (no solution), intersect at a point (one solution), or intersect in a line (many solutions). The following example shows how to determine the number of solutions from the RREF of the augmented matrix.

# Example A.2

Consider a system of two equations in three variables that has many solutions:

$$
\begin{array} { r } { x _ { 1 } + x _ { 2 } + x _ { 3 } = 0 } \\ { x _ { 1 } + 2 x _ { 2 } + 2 x _ { 3 } = 0 . } \end{array}
$$

We put this system of equations into augmented matrix form and then find the RREF, which is

$$
{ \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } \end{array} \right] } { \left[ \begin{array} { l } { 0 } \\ { 0 } \end{array} \right] } .
$$

We can translate this back into equation form as

$$
\begin{array} { r } { x _ { 1 } = 0 } \\ { \qquad } \\ { x _ { 1 } + x _ { 3 } = 0 . } \end{array}
$$

Clearly, $x _ { 1 }$ must be 0 in any solution to the system of equations. However, $x _ { 2 }$ and $x _ { 3 }$ are not fixed. We could treat $x _ { 3 }$ as a free variable and allow it to take on any value. Whatever value $x _ { 3 }$ takes on, $x _ { 2 }$ must be equal to $- { x } _ { 3 }$ . Geometrically, this system of equations describes the intersection of two planes, where the intersection consists of points on the line $x _ { 2 } = - x _ { 3 }$ in the $x _ { 1 } = 0$ plane.

A linear system of equations may have more equation constraints than variables, in which case the system of equations is over-determined. Although over-determined systems often have no solutions, it is possible for an over-determined system of equations to have either many solutions or exactly one solution.

Conversely, a system of equations with fewer equations than variables is underdetermined. Although in many cases under-determined systems of equations have infinitely many solutions, it is also possible for such systems to have no solutions.

A system of equations with all 0s on the right-hand side is homogeneous. Every homogeneous system of equations has at least one solution, the trivial solution in which all of the variables are 0s. A system of equations with a nonzero right-hand side is nonhomogeneous.

# A.2. MATRIX AND VECTOR ALGEBRA

As we have seen in the previous section, a matrix is a table of numbers laid out in rows and columns. A vector is a matrix consisting of a single column or row of numbers (vectors in this text are typically expressed as column vectors). In general, matrices and vectors may contain complex numbers as well as real numbers. With the exception of Chapter 8, all of the vectors and matrices in this book are real.

There are several important notational conventions used here for matrices and vectors. Boldface capital letters such as A, $\mathbf { B }$ , . . . are used to denote matrices. Boldface lower-case letters such as $\mathbf { x }$ , y, . . . are used to denote vectors. Lower-case letters or Greek letters such as ${ \it m } , n , \alpha , \beta , \ldots .$ . will be used to denote scalars.

At times we will need to refer to specific parts of a matrix. The notation $A _ { i , j }$ denotes the element of the matrix $\mathbf { A }$ in row $i$ and column $j .$ . We denote the jth element of the vector $\mathbf { x }$ by $x _ { j }$ . The notation $\mathbf { A } _ { \cdot , j }$ is used to refer to column $j$ of the matrix A, while $\mathbf { A } _ { i } ,$ · refers to row $i$ of A.

We can also construct larger matrices from smaller matrices. The notation $\mathbf { A } =$ $[ \mathbf { B } \ \mathbf { C } ]$ means that the matrix $\mathbf { A }$ is composed of the matrices $\mathbf { B }$ and $\mathbf { C }$ , with matrix $\mathbf { C }$ to the right of $\mathbf { B }$ .

If $\mathbf { A }$ and $\mathbf { B }$ are two matrices of the same size, we can add them by simply adding corresponding elements. Similarly, we can subtract B from A by subtracting the corresponding elements of $\mathbf { B }$ from those of A. We can multiply a scalar times a matrix by multiplying the scalar times each matrix element. Because vectors are just $n$ by 1 matrices, we can perform the same arithmetic operations on vectors. A zero matrix, 0, is a matrix composed of all zero elements. A zero matrix plays the same role in matrix algebra as the scalar 0, with

$$
\begin{array} { c } { \mathbf { A + 0 } = \mathbf { A } } \\ { \mathbf { \qquad } } \\ { \mathbf { \qquad = 0 + A } . } \end{array}
$$

Using vector notation, we can write a linear system of equations in vector form.

# Example A.3

Recall the system of equations (A.9),

$$
\begin{array} { r } { x _ { 1 } + x _ { 2 } + x _ { 3 } = 0 \quad } \\ { x _ { 1 } + 2 x _ { 2 } + 2 x _ { 3 } = 0 , } \end{array}
$$

from Example A.2. We can write this in vector form as

$$
x _ { 1 } \left[ 1 \atop 1 \right] + x _ { 2 } \left[ 1 \atop 2 \right] + x _ { 3 } \left[ 1 \atop 2 \right] = \left[ 0 \atop 0 \right] .
$$

The expression on the left-hand side of (A.15) where vectors are multiplied by scalars and the results are summed together is called a linear combination.

If A is an $m$ by $n$ matrix, and $\mathbf { x }$ is an $n$ element vector, we can multiply A times $\mathbf { x }$ where the product is defined by

$$
\mathbf { A } \mathbf { x } = x _ { 1 } \mathbf { A } . _ { , 1 } + x _ { 2 } \mathbf { A } . _ { , 2 } + \cdot \cdot \cdot + x _ { n } \mathbf { A } . _ { , n } .
$$

# Example A.4

Given

$$
\mathbf { A } = { \left[ \begin{array} { l l l } { 1 } & { 2 } & { 3 } \\ { 4 } & { 5 } & { 6 } \end{array} \right] }
$$

and

$$
\mathbf { x } = { \left[ \begin{array} { l } { 1 } \\ { 0 } \\ { 2 } \end{array} \right] } ,
$$

then

$$
\mathbf { A } \mathbf { x } = 1 \left[ { 1 } atop { 4 } \right] + 0 \left[ { 2 } \atop { 5 } \right] + 2 \left[ { 3 } \atop { 6 } \right] = { \binom { 7 } { 1 6 } } .
$$

The formula (A.16) for $\mathbf { A x }$ is a linear combination much like the one that occurred in the vector form of a system of equations. It is possible to write any linear system of equations in the form $\mathbf { A x } = \mathbf { b }$ , where $\mathbf { A }$ is a matrix containing the coefficients of the variables in the equations, $\mathbf { b }$ is a vector containing the coefficients on the right-hand sides of the equations, and $\mathbf { x }$ is a vector containing the variables.

Definition A.2 If A is a matrix of size $m$ by $n$ , and $\mathbf { B }$ is a matrix of size $n$ by $r$ , then the product $\mathbf { C } = \mathbf { A } \mathbf { B }$ is obtained by multiplying $\mathbf { A }$ times each of the columns of $\mathbf { B }$ and assembling the matrix vector products in $\mathbf { C }$ :

$$
\mathbf { C } = \bigl [ \mathbf { A } \mathbf { B } . , \mathbf { \partial } _ { 1 } \ \mathbf { A } \mathbf { B } . , 2 \ \cdot \ \cdot \ \mathbf { A } \mathbf { B } . , \bigr ] .
$$

This approach given in (A.20) for calculating a matrix-matrix product will be referred to as the matrix-vector method.

Note that the product (A.20) is only possible if the two matrices are of compatible sizes. If A has m rows and $n$ columns, and $\mathbf { B }$ has $n$ rows and $r$ columns, then the product AB exists and is of size $m$ by $r$ . In some cases, it is thus possible to multiply AB but not BA. It is important to note that when both AB and BA exist, AB is not generally equal to BA!

An alternate way to compute the product of two matrices is the row-column expansion method, where the product element $C _ { i , j }$ is calculated as the matrix product of row $i$ of A and column $j$ of $\mathbf { B }$ .

# Example A.5

Let

$$
\mathbf { A } = { \left[ \begin{array} { l l } { 1 } & { 2 } \\ { 3 } & { 4 } \\ { 5 } & { 6 } \end{array} \right] }
$$

and

$$
\mathbf { B } = { \left[ \begin{array} { l l } { 5 } & { 2 } \\ { 3 } & { 7 } \end{array} \right] } .
$$

The product matrix $\mathbf { C } = \mathbf { A } \mathbf { B }$ will be of size 3 by 2. We compute the product using both methods. First, using the matrix-vector approach (A.20), we have

$$
\begin{array} { r l } { \mathbf { C } = \left[ \mathbf { A } \mathbf { B } , _ { \cdot 1 } \ \mathbf { A } \mathbf { B } , _ { \cdot 2 } \right] } \\ { = { \left[ 5 \left[ \begin{array} { l } { 1 } \\ { 3 } \\ { 5 } \end{array} \right] } + 3 \left[ \begin{array} { l } { 2 } \\ { 4 } \\ { 6 } \end{array} \right] } & { 2 { \left[ \begin{array} { l } { 1 } \\ { 3 } \\ { 5 } \end{array} \right] } + 7 { \left[ \begin{array} { l } { 2 } \\ { 4 } \\ { 6 } \end{array} \right] } { \right] } } \\ { = { \left[ \begin{array} { l l } { 1 1 } & { 1 6 } \\ { 2 7 } & { 3 4 } \\ { 4 3 } & { 5 2 } \end{array} \right] } . } \end{array}
$$

Next, we use the row-column approach:

$$
{ \begin{array} { r l } & { \mathbf { C } = { \left[ \begin{array} { l l } { 1 \cdot 5 + 2 \cdot 3 } & { 1 \cdot 2 + 2 \cdot 7 } \\ { 3 \cdot 5 + 4 \cdot 3 } & { 3 \cdot 2 + 4 \cdot 7 } \\ { 5 \cdot 5 + 6 \cdot 3 } & { 5 \cdot 2 + 6 \cdot 7 } \end{array} \right] } } \\ & { \mathbf { \Lambda } = { \left[ \begin{array} { l l } { 1 1 } & { 1 6 } \\ { 2 7 } & { 3 4 } \\ { 4 3 } & { 5 2 } \end{array} \right] } . } \end{array} }
$$

Definition A.3 The $n$ by $n$ identity matrix ${ \mathbf I } _ { n }$ is composed of 1s in the diagonal and 0s in the off-diagonal elements.

For example, the 3 by 3 identity matrix is

$$
\mathbf { I } _ { 3 } = { \left[ \begin{array} { l l l } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } .
$$

We often write I without specifying the size of the matrix in situations where the size of matrix is obvious from the context. It is easily shown that if $\mathbf { A }$ is an $m$ by $n$ matrix, then

$$
\begin{array} { c } { \mathbf { A } \mathbf { I } _ { n } = \mathbf { A } } \\ { \mathbf { \Lambda } } \\ { \mathbf { \Lambda } = \mathbf { I } _ { m } \mathbf { A } . } \end{array}
$$

Thus, multiplying by I in matrix algebra is similar to multiplying by 1 in conventional scalar algebra.

We have not defined matrix division, but it is possible at this point to define the matrix algebra equivalent of the reciprocal.

Definition A.4 If A is an $n$ by $n$ matrix, and there is a matrix $\mathbf { B }$ such that

$$
\mathbf { A B } = \mathbf { B A } = \mathbf { I } ,
$$

then $\mathbf { B }$ is the inverse of A. We write $\mathbf { B } = \mathbf { A } ^ { - 1 }$ .

How do we compute the inverse of a matrix? If $\mathbf { A B } = \mathbf { I }$ , then

$$
\left[ \mathbf { A } \mathbf { B } . , _ { 1 } ~ \mathbf { A } \mathbf { B } . , _ { 2 } ~ . ~ . ~ . ~ \mathbf { A } \mathbf { B } . , _ { n } \right] = \mathbf { I } .
$$

Since the columns of the identity matrix and $\mathbf { A }$ are known, we can solve

$$
\mathbf { A B } _ { \cdot , 1 } = { \left[ \begin{array} { l } { 1 } \\ { 0 } \\ { \vdots } \\ { 0 } \end{array} \right] }
$$

to obtain $\mathbf { B } _ { 1 }$ . We can find the remaining columns of the inverse in the same way. If any of these systems of equations are inconsistent, then $\mathbf { A } ^ { - 1 }$ does not exist.

The inverse matrix can be used to solve a system of linear equations with $n$ equations and $n$ variables. Given the system of equations $\mathbf { A x } = \mathbf { b }$ , and $\mathbf { A } ^ { - 1 }$ , we can multiply $\mathbf { A x } = \mathbf { b }$ on both sides by the inverse to obtain

$$
\mathbf { A } ^ { - 1 } \mathbf { A x } = \mathbf { A } ^ { - 1 } \mathbf { b } .
$$

Because

$$
\begin{array} { r } { \mathbf { A } ^ { - 1 } \mathbf { A } \mathbf { x } = \mathbf { I } \mathbf { x } } \\ { = \mathbf { x } , } \end{array}
$$

this gives the solution

$$
\mathbf { x } = \mathbf { A } ^ { - 1 } \mathbf { b } .
$$

This argument shows that if $\mathbf { A } ^ { - 1 }$ exists, then for any right-hand side $\mathbf { b }$ , a system of equations has a unique solution. If $\mathbf { A } ^ { - 1 }$ does not exist, then the system of equations may have either many solutions or no solution.

Definition A.5 When A is an $n$ by $n$ matrix, $\mathbf { A } ^ { k }$ is the product of $k$ copies of A. By convention, we define $\mathbf { A } ^ { 0 } = \mathbf { I }$ .

Definition A.6 The transpose of a matrix A, denoted $\mathbf { A } ^ { T } ,$ , is obtained by taking the columns of A and writing them as the rows of the transpose. We will also use the notation $\mathbf { A } ^ { - T }$ for $( \mathbf { A } ^ { - 1 } ) ^ { T } .$ .

# Example A.6

Let

$$
\mathbf { A } = { \left[ \begin{array} { l l } { 2 } & { 1 } \\ { 5 } & { 2 } \end{array} \right] } .
$$

Then

$$
\mathbf { A } ^ { T } = { \left[ \begin{array} { l l } { 2 } & { 5 } \\ { 1 } & { 2 } \end{array} \right] } .
$$

Definition A.7 A matrix is symmetric if $\mathbf { A } = \mathbf { A } ^ { T } .$ .

Although many elementary textbooks on linear algebra consider only square diagonal matrices, we will have occasion to refer to $m$ by $n$ matrices that have nonzero elements only on the diagonal.

Definition A.8 An $m$ by $n$ matrix $\mathbf { A }$ is diagonal if $A _ { i , j } = 0$ whenever $i \neq j$ .

Definition A.9 An $m$ by $n$ matrix $\mathbf { R }$ is upper-triangular if $R _ { i , j } = 0$ whenever $i > j$ .   
A matrix $\mathbf { L }$ is lower-triangular if ${ \bf L } ^ { T }$ is upper-triangular.

# Example A.7

The matrix

$$
\mathbf { S } = { \left[ \begin{array} { l l l l l } { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 2 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 3 } & { 0 } & { 0 } \end{array} \right] }
$$

is diagonal, and the matrix

$$
\mathbf { R } = { \left[ \begin{array} { l l l } { 1 } & { 2 } & { 3 } \\ { 0 } & { 2 } & { 4 } \\ { 0 } & { 0 } & { 5 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] }
$$

is upper-triangular.

Theorem A.1 The following statements are true for any scalars s and t and matrices A, B, and C. It is assumed that the matrices are of the appropriate size for the operations involved and that whenever an inverse occurs, the matrix is invertible.

1. $\mathbf { A } + \mathbf { 0 } = \mathbf { 0 } + \mathbf { A } = \mathbf { A }$ .   
2. $\mathbf { A } + \mathbf { B } = \mathbf { B } + \mathbf { A }$ .   
3. $( \mathbf { A } + \mathbf { B } ) + \mathbf { C } = \mathbf { A } + ( \mathbf { B } + \mathbf { C } )$ .   
4. $\mathbf { A } ( \mathbf { B C } ) = ( \mathbf { A B } ) \mathbf { C }$ .   
5. $\mathbf { A } ( \mathbf { B } + \mathbf { C } ) = \mathbf { A B } + \mathbf { A C }$ .   
6. $( \mathbf { A } + \mathbf { B } ) \mathbf { C } = \mathbf { A } \mathbf { C } + \mathbf { B } \mathbf { C }$ .   
7. $( s t ) \mathbf { A } = s ( t \mathbf { A } )$ .   
8. $s ( \mathbf { A B } ) = ( s \mathbf { A } ) \mathbf { B } = \mathbf { A } ( s \mathbf { B } )$ .   
9. $( s + t ) \mathbf { A } = s \mathbf { A } + t \mathbf { A }$ .   
10. $s ( \mathbf { A } + \mathbf { B } ) = s \mathbf { A } + s \mathbf { B }$ .   
11. $( \mathbf { A } ^ { T } ) ^ { T } = \mathbf { A }$ .   
12. $( s \mathbf { A } ) ^ { T } = s ( \mathbf { A } ^ { T } )$ .   
13. $( \mathbf { A } + \mathbf { B } ) ^ { T } = \mathbf { A } ^ { T } + \mathbf { B } ^ { T } .$   
14. $( \mathbf { A } \mathbf { B } ) ^ { T } = \mathbf { B } ^ { T } \mathbf { A } ^ { T } .$ .   
15. $( \mathbf { A } \mathbf { B } ) ^ { - 1 } = \mathbf { B } ^ { - 1 } \mathbf { A } ^ { - 1 } .$ .   
16. $( \mathbf { A } ^ { - 1 } ) ^ { - 1 } = \mathbf { A }$ .   
17. $( \mathbf { A } ^ { T } ) ^ { - 1 } = ( \mathbf { A } ^ { - 1 } ) ^ { T } .$ .   
18. If $\mathbf { A }$ and $\mathbf { B }$ are $n$ by $n$ matrices,

The first 10 rules in this list are identical to rules of conventional algebra, and you should have little trouble in applying them. The rules involving transposes and inverses are new, but they can be mastered without too much trouble.

Some students have difficulty with the following statements, which would appear to be true on the surface, but that are in fact false for at least some matrices.

1. $\mathbf { A } \mathbf { B } = \mathbf { B } \mathbf { A }$ .   
2. If $\mathbf { A } \mathbf { B } = \mathbf { 0 }$ , then $\mathbf { A } = \mathbf { 0 }$ or $\mathbf { B } = \mathbf { 0 }$ .   
3. If $\mathbf { A } \mathbf { B } = \mathbf { A } \mathbf { C }$ and $\mathbf { A } \neq 0$ , then $\mathbf { B } = \mathbf { C }$ .

It is a worthwhile exercise to construct examples of 2 by 2 matrices for which each of these statements is false.

# A.3. LINEAR INDEPENDENCE

Definition A.10 The vectors $\mathbf { v } _ { 1 }$ , $\mathbf { v } _ { 2 }$ , . . . , ${ \bf v } _ { n }$ are linearly independent if the system of equations

$$
c _ { 1 } \mathbf { v } _ { 1 } + c _ { 2 } \mathbf { v } _ { 2 } + \cdot \cdot \cdot + c _ { n } \mathbf { v } _ { n } = \mathbf { 0 }
$$

has only the trivial solution $\mathbf { c } = \mathbf { 0 }$ . If there are multiple solutions, then the vectors are linearly dependent.

Determining whether a set of vectors is linearly independent is simple. Just solve the above system of equations (A.42).

# Example A.8

Let

$$
\mathbf { A } = { \left[ \begin{array} { l l l } { 1 } & { 2 } & { 3 } \\ { 4 } & { 5 } & { 6 } \\ { 7 } & { 8 } & { 9 } \end{array} \right] } .
$$

Are the columns of A linearly independent vectors? To determine this we set up the system of equations $\mathbf { A x } = \mathbf { 0 }$ in an augmented matrix, and then find the RREF,

$$
{ \left[ \begin{array} { l l l } { 1 } & { 0 } & { - 1 } \\ { 0 } & { 1 } & { 2 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] } ^ { } { \boldsymbol { 0 } } { \Bigg ] } .
$$

The solutions are

$$
{ \bf x } = x _ { 3 } \left[ \begin{array} { r } { 1 } \\ { - 2 } \\ { 1 } \end{array} \right] .
$$

We can set $x _ { 3 } = 1$ and obtain the nonzero solution,

$$
\mathbf { x } = { \left[ - 2 \right] } { \begin{array} { r } { 1 } \\ { - 2 } \\ { 1 } \end{array} } .
$$

Thus, the columns of A are linearly dependent.

There are a number of important theoretical consequences of linear independence. For example, it can be shown that if the columns of an $n$ by $n$ matrix A are linearly independent, then $\mathbf { A } ^ { - 1 }$ exists, and the system of equations $\mathbf { A x } = \mathbf { b }$ has a unique solution for every right-hand side $\mathbf { b }$ [95].

# A.4. SUBSPACES OF $\pmb { R } ^ { n }$

So far, we have worked with vectors of real numbers in the $n$ -dimensional space $R ^ { n } .$ . There are a number of properties of $R ^ { n }$ that make it convenient to work with vectors. First, the operation of vector addition always works. We can take any two vectors in $R ^ { n }$ and add them together and get another vector in $R ^ { n } .$ Second, we can multiply any vector in $R ^ { n }$ by a scalar and obtain another vector in $R ^ { n } .$ . Finally, we have the 0 vector, with the property that for any vector $\mathbf { x }$ , $\mathbf { x } + \mathbf { 0 } = \mathbf { 0 } + \mathbf { x } = \mathbf { x }$ .

Definition A.11 A subspace $W$ of $R ^ { n }$ is a subset of $R ^ { n }$ that satisfies the three properties:

1. If $\mathbf { x }$ and $\mathbf { y }$ are vectors in $W$ , then $\mathbf x + \mathbf y$ is also a vector in $W$ . 2. If $\mathbf { x }$ is a vector in $W$ and $s$ is any real scalar, then $s \mathbf { x }$ is also a vector in $W$ . 3. The 0 vector is in $W$ . A subspace of $R ^ { n }$ is nontrivial if it contains vectors other than the 0 vector.

# Example A.9

In $R ^ { 3 }$ , the plane $P$ defined by the equation

$$
x _ { 1 } + x _ { 2 } + x _ { 3 } = 0
$$

is a subspace of $R ^ { n } .$ . To see this, note that if we take any two vectors in the plane and add them together, we get another vector in the plane. If we take a vector in this plane and multiply it by any scalar, we get another vector in the plane. Finally, 0 is a vector in the plane.

Subspaces are important because they provide an environment within which all of the rules of matrix-vector algebra apply. An especially important subspace of $R ^ { n }$ that we will work with is the null space of an $m$ by $n$ matrix.

Definition A.12 Let A be an $m$ by $n$ matrix. The null space of $\mathbf { A }$ , written $N ( \mathbf { A } )$ , is the set of all vectors $\mathbf { x }$ such that $\mathbf { A x } = \mathbf { 0 }$ .

To show that $N ( \mathbf { A } )$ is actually a subspace of $R ^ { n }$ , we need to show that:

1. If $\mathbf { x }$ and $\mathbf { y }$ are in $N ( \mathbf { A } )$ , then $\mathbf { A x } = \mathbf { 0 }$ and $\mathbf { A } \mathbf { y } = \mathbf { 0 }$ . By adding these equations, we find that $\mathbf { A } ( \mathbf { x } + \mathbf { y } ) = \mathbf { 0 }$ . Thus $\mathbf x + \mathbf y$ is in $N ( \mathbf { A } )$ .

2. If $\mathbf { x }$ is in $N ( \mathbf { A } )$ and $s$ is any scalar, then $\mathbf { A x } = \mathbf { 0 }$ . We can multiply this equation by s to get $s \mathbf { A } \mathbf { x } = \mathbf { 0 }$ . Thus $\mathbf { A } ( s \mathbf { x } ) = \mathbf { 0 }$ , and $s \mathbf { x }$ is in $N ( \mathbf { A } )$ .

3. $\mathbf { A } \mathbf { 0 } = \mathbf { 0 }$ , so 0 is in $N ( \mathbf { A } )$

Computationally, the null space of a matrix can be determined by solving the system of equations $\mathbf { A x } = \mathbf { 0 }$ .

# Example A.10

Let

$$
\mathbf { A } = { \left[ \begin{array} { l l l l } { 3 } & { 1 } & { 9 } & { 4 } \\ { 2 } & { 1 } & { 7 } & { 3 } \\ { 5 } & { 2 } & { 1 6 } & { 7 } \end{array} \right] } .
$$

To find the null space of A, we solve the system of equations $\mathbf { A x } = \mathbf { 0 }$ . To solve the equations, we put the system of equations into an augmented matrix,

$$
{ \left[ \begin{array} { l l l l l } { 3 } & { 1 } & { 9 } & { 4 } \\ { 2 } & { 1 } & { 7 } & { 3 } \\ { 5 } & { 2 } & { 1 6 } & { 7 } \end{array} \right] } ^ { 0 } { \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { 0 } \end{array} \right] } ,
$$

and find the RREF,

$$
{ \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 2 } & { 1 } \\ { 0 } & { 1 } & { 3 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] } { \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { 0 } \end{array} \right] } .
$$

From the augmented matrix, we find that

$$
\mathbf { x } = x _ { 3 } \left[ { - 3 \atop 1 } \right] + x _ { 4 } \left[ { - 1 \atop 0 } \right] .
$$

Any vector in the null space can be written as a linear combination of the above vectors, so the null space is a two-dimensional plane within $R ^ { 4 }$ .

Now, consider the problem of solving $\mathbf { A x } = \mathbf { b }$ , where

$$
\mathbf { b } = { \left[ \begin{array} { l } { 2 2 } \\ { 1 7 } \\ { 3 9 } \end{array} \right] }
$$

and one particular solution is

$$
\mathbf { p } = { \left[ \begin{array} { l } { 1 } \\ { 2 } \\ { 1 } \\ { 2 } \end{array} \right] } .
$$

We can take any vector in the null space of $\mathbf { A }$ and add it to this solution to obtain another solution. Suppose that $\mathbf { x }$ is in $N ( \mathbf { A } )$ . Then

$$
\begin{array} { r l } & { \mathbf { A } ( \mathbf { x } + \mathbf { p } ) = \mathbf { A } \mathbf { x } + \mathbf { A } \mathbf { p } } \\ & { ~ \mathbf { A } ( \mathbf { x } + \mathbf { p } ) = \mathbf { 0 } + \mathbf { b } } \\ & { ~ \mathbf { A } ( \mathbf { x } + \mathbf { p } ) = \mathbf { b } . } \end{array}
$$

For example,

$$
\mathbf { x } = \left[ { 2 \atop 1 } \right] + 2 \left[ { - 3 \atop 1 } \right] + 3 \left[ { - 1 \atop 0 } \right]
$$

is also a solution to $\mathbf { A x } = \mathbf { b }$ .

In the context of inverse problems, the null space is critical because the presence of a nontrivial null space leads to nonuniqueness in the solution to a linear system of equations.

Definition A.13 A basis for a subspace $W$ is a set of vectors $\mathbf { v } _ { 1 } , \ldots . . . , \mathbf { v } _ { p }$ such that:

1. Any vector in $W$ can be written as a linear combination of the basis vectors.

2. The basis vectors are linearly independent.

A particularly simple and useful basis is the standard basis.

Definition A.14 The standard basis for $R ^ { n }$ is the set of vectors $\mathbf { e } _ { 1 } , \ldots . . . , \mathbf { e } _ { n }$ such that the elements of $\mathbf { e } _ { i }$ are all zero except for the ith element, which is 1.

Any nontrivial subspace $W$ of $R ^ { n }$ will have many different bases. For example, we can take any basis and multiply one of the basis vectors by 2 to obtain a new basis. It is possible to show that all bases for a subspace $W$ have the same number of basis vectors [95].

Theorem A.2 Let $W$ be a subspace of $R ^ { n }$ with basis $\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } , \ldots . \mathbf { \ v } _ { p }$ . Then all bases for $W$ have $p$ basis vectors, and $p$ is the dimension of $W$ .

It can be shown that the procedure used in the above example always produces a basis for $N ( \mathbf { A } )$ [95]. A basis for the null space of a matrix can be found in MATLAB using the null command.

Definition A.15 Let A be an $m$ by $n$ matrix. The column space or range of A (written $R ( \mathbf { A } ) )$ ) is the set of all vectors $\mathbf { b }$ such that $\mathbf { A x } = \mathbf { b }$ has at least one solution. In other words, the column space is the set of all vectors $\mathbf { b }$ that can be written as a linear combination of the columns of A.

The range is important in the context of discrete linear inverse problems, because $R ( \mathbf G )$ consists of all vectors $\mathbf { d }$ for which there is a model $\mathbf { m }$ such that $\mathbf { G m } = \mathbf { d }$ .

To find the column space of a matrix, we consider what happens when we compute the RREF of $\left[ \mathbf { A } \mid \mathbf { b } \right]$ . In the part of the augmented matrix corresponding to the lefthand side of the equations we always get the same result, namely the RREF of A. The solution to the system of equations may involve some free variables, but we can always set these free variables to 0. Thus when we are able to solve $\mathbf { A x } = \mathbf { b }$ , we can solve the system of equations by using only variables corresponding to the pivot columns in the RREF of A. In other words, if we can solve $\mathbf { A x } = \mathbf { b }$ , then we can write $\mathbf { b }$ as a linear combination of the pivot columns of A. Note that these are columns from the original matrix A, not columns from the RREF of A. An orthonormal (see below) basis for the range of a matrix can be found in MATLAB using the orth command.

# Example A.11

As in the previous example, let

$$
\mathbf { A } = { \left[ \begin{array} { l l l l } { 3 } & { 1 } & { 9 } & { 4 } \\ { 2 } & { 1 } & { 7 } & { 3 } \\ { 5 } & { 2 } & { 1 6 } & { 7 } \end{array} \right] } .
$$

To find the column space of $\mathbf { A }$ , note that the RREF of $\mathbf { A }$ is

$$
{ \left[ \begin{array} { l l l l } { 1 } & { 0 } & { 2 } & { 1 } \\ { 0 } & { 1 } & { 3 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] } .
$$

Thus, whenever we can solve $\mathbf { A x } = \mathbf { b }$ , we can find a solution in which $x _ { 3 }$ and $x _ { 4 }$ are 0. In other words, whenever there is a solution to $\mathbf { A x } = \mathbf { b }$ , we can write $\mathbf { b }$ as a linear combination of the first two columns of A:

$$
\mathbf { b } = x _ { 1 } { \left[ \begin{array} { l } { 3 } \\ { 2 } \\ { 5 } \end{array} \right] } + x _ { 2 } { \left[ \begin{array} { l } { 1 } \\ { 1 } \\ { 2 } \end{array} \right] } .
$$

Since these two vectors are linearly independent and span $R ( \mathbf { A } )$ , they form a basis for $R ( \mathbf { A } )$ . The dimension of $R ( \mathbf { A } )$ is 2.

In finding the null space and range of a matrix A, we found that the basis vectors for $N ( \mathbf { A } )$ corresponded to nonpivot columns of A, while the basis vectors for $R ( \mathbf { A } )$ corresponded to pivot columns of A. Since the matrix $\mathbf { A }$ had $n$ columns, we obtain the following theorem.

# Theorem A.3

$$
d i m ~ N ( { \bf A } ) + d i m ~ R ( { \bf A } ) = n .
$$

In addition to the null space and range of a matrix $\mathbf { A }$ , we will often work with the null space and range of the transpose of A. Since the columns of $\mathbf { A } ^ { T }$ are rows of $\mathbf { A }$ , the column space of $\mathbf { A } ^ { T }$ is also called the row space of A. Since each row of A can be written as a linear combination of the nonzero rows of the RREF of A, the nonzero rows of the RREF form a basis for the row space of A. There are exactly as many nonzero rows in the RREF of A as there are pivot columns. Thus we have the following theorem.

# Theorem A.4

$$
d i m ( R ( { \bf A } ^ { T } ) ) = d i m ~ R ( { \bf A } ) .
$$

Definition A.16 The rank of an $m$ by $n$ matrix $\mathbf { A }$ is the dimension of $R ( \mathbf { A } )$ . If $\mathrm { r a n k } ( \mathbf { A } ) = \operatorname* { m i n } ( m , n )$ , then A has full rank. If ${ \mathrm { r a n k } } ( \mathbf { A } ) = m$ , then A has full row rank. If $\operatorname { r a n k } ( \mathbf { A } ) = n$ , then $\mathbf { A }$ has full column rank. If $\operatorname { r a n k } ( \mathbf { A } ) < \operatorname* { m i n } ( m , n )$ , then A is rank deficient.

The rank of a matrix is readily found in MATLAB by using the rank command.

# A.5. ORTHOGONALITY AND THE DOT PRODUCT

Definition A.17 Let $\mathbf { x }$ and $\mathbf { y }$ be two vectors in $R ^ { n } .$ . The dot product of $\mathbf { x }$ and $\mathbf { y }$ is

$$
\mathbf { x } \cdot \mathbf { y } = \mathbf { x } ^ { T } \mathbf { y } = x _ { 1 } \gamma _ { 1 } + x _ { 2 } \gamma _ { 2 } + \cdot \cdot \cdot + x _ { n } \gamma _ { n } .
$$

Definition A.18 Let $\mathbf { x }$ be a vector in $R ^ { n } .$ . The 2-norm or Euclidean length of $\mathbf { x }$ is

$$
\| \mathbf { x } \| _ { 2 } = \sqrt { \mathbf { x } ^ { T } \mathbf { x } } = \sqrt { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + \cdot \cdot \cdot + x _ { n } ^ { 2 } } .
$$

Later we will introduce two other ways of measuring the “length” of a vector. The subscript 2 is used to distinguish this 2-norm from the other norms.

You may be familiar with an alternative definition of the dot product in which $\mathbf { x } \cdot \mathbf { y } =$ $\| \mathbf { x } \| \| \mathbf { y } \| \cos ( \theta )$ , where $\theta$ is the angle between the two vectors. The two definitions are equivalent. To see this, consider a triangle with sides $\mathbf { x }$ , y, and $\mathbf x - \mathbf y$ . See Figure A.1.

![](images/4ef469f2c7af9330024908cd6b8ea828be0d048cc2d6bf538b7886845063b918.jpg)  
Figure A.1 Relationship between the dot product and the angle between two vectors.

The angle between sides $\mathbf { x }$ and $\mathbf { y }$ is $\theta$ . By the law of cosines,

$$
\begin{array} { c } { \| \mathbf { x } - \mathbf { y } \| _ { 2 } ^ { 2 } = \| \mathbf { x } \| _ { 2 } ^ { 2 } + \| \mathbf { y } \| _ { 2 } ^ { 2 } - 2 \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } \cos ( \theta ) } \\ { \ \qquad ( \mathbf { x } - \mathbf { y } ) ^ { T } ( \mathbf { x } - \mathbf { y } ) = \mathbf { x } ^ { T } \mathbf { x } + \mathbf { y } ^ { T } \mathbf { y } - 2 \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } \cos ( \theta ) } \\ { \mathbf { x } ^ { T } \mathbf { x } - 2 \mathbf { x } ^ { T } \mathbf { y } + \mathbf { y } ^ { T } \mathbf { y } = \mathbf { x } ^ { T } \mathbf { x } + \mathbf { y } ^ { T } \mathbf { y } - 2 \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } \cos ( \theta ) } \\ { \ \qquad - 2 \mathbf { x } ^ { T } \mathbf { y } = - 2 \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } \cos ( \theta ) } \\ { \mathbf { x } ^ { T } \mathbf { y } = \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } \cos ( \theta ) . } \end{array}
$$

We can also use this formula to compute the angle between two vectors:

$$
\theta = \cos ^ { - 1 } \left( \frac { \mathbf { x } ^ { T } \mathbf { y } } { \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } } \right) .
$$

Definition A.19 Two vectors $\mathbf { x }$ and $\mathbf { y }$ in $R ^ { n }$ are orthogonal, or equivalently, perpendicular (written $\mathbf { x } \perp \mathbf { y } )$ ), if $\mathbf { x } ^ { T } \mathbf { y } = 0$ .

Definition A.20 A set of vectors $\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } , \ldots . \mathbf { v } _ { p }$ is orthogonal if each pair of vectors in the set is orthogonal.

Definition A.21 Two subspaces $V$ and $W$ of $R ^ { n }$ are orthogonal if every vector in $V$ is perpendicular to every vector in $W$ .

If $\mathbf { x }$ is in $N ( \mathbf { A } )$ , then $\mathbf { A x } = \mathbf { 0 }$ . Since each element of the product Ax can be obtained by taking the dot product of a row of $\mathbf { A }$ and $\mathbf { x } , \mathbf { x }$ is perpendicular to each row of A. Since $\mathbf { x }$ is perpendicular to all of the columns of $\mathbf { A } ^ { T }$ , it is perpendicular to $R ( \mathbf { A } ^ { T } )$ . We have the following theorem.

Theorem A.5 Let A be an m by n matrix. Then

$$
N ( \mathbf { A } ) \perp R ( \mathbf { A } ^ { T } ) .
$$

Furthermore,

$$
\begin{array} { r } { N ( { \bf A } ) + R ( { \bf A } ^ { T } ) = R ^ { n } . } \end{array}
$$

That is, any vector $\mathbf { x }$ in $R ^ { n }$ can be written uniquely as $\mathbf { x } = \mathbf { p } + \mathbf { q }$ , where $\mathbf { p }$ is in $N ( \mathbf { A } )$ and $\mathbf { q }$ is in $R ( \mathbf { A } ^ { T } )$ .

Definition A.22 A basis in which the basis vectors are orthogonal is an orthogonal basis. A basis in which the basis vectors are orthogonal and have length 1 is an orthonormal basis.

Definition A.23 An $n$ by $n$ matrix $\mathbf { Q }$ is orthogonal if the columns of $\mathbf { Q }$ are orthogonal and each column of $\mathbf { Q }$ has length 1.

With the requirement that the columns of an orthogonal matrix have length 1, using the term “orthonormal” would make logical sense. However, the definition of “orthogonal” given here is standard and we will not try to change standard usage.

Orthogonal matrices have a number of useful properties.

Theorem A.6 If $\mathbf { Q }$ is an orthogonal matrix, then:

1. $\mathbf { Q } ^ { T } \mathbf { Q } = \mathbf { Q } \mathbf { Q } ^ { T } = \mathbf { I }$ . In other words, $\mathbf { Q } ^ { - 1 } = \mathbf { Q } ^ { T }$ .   
2. For any vector $\mathbf { x }$ in $R ^ { n }$ , $\| \mathbf { Q x } \| _ { 2 } = \| \mathbf { x } \| _ { 2 } .$ .   
3. For any two vectors $\mathbf { x }$ and $\mathbf { y }$ in $R ^ { n }$ , $\mathbf { x } ^ { T } \mathbf { y } = ( \mathbf { Q } \mathbf { x } ) ^ { T } ( \mathbf { Q } \mathbf { y } ) .$

A problem that we will often encounter in practice is projecting a vector $\mathbf { x }$ onto another vector $\mathbf { y }$ or onto a subspace $W$ to obtain a projected vector $\mathbf { p }$ . See Figure A.2. We know that

$$
\mathbf { x } ^ { T } \mathbf { y } = \| \mathbf { x } \| _ { 2 } \| \mathbf { y } \| _ { 2 } \cos ( \theta ) ,
$$

where $\theta$ is the angle between $\mathbf { x }$ and $\mathbf { y }$ . Also,

$$
\cos ( \theta ) = { \frac { \| \mathbf { p } \| _ { 2 } } { \| \mathbf { x } \| _ { 2 } } } .
$$

Thus

$$
\| \mathbf { p } \| _ { 2 } = { \frac { \mathbf { x } ^ { T } \mathbf { y } } { \| \mathbf { y } \| _ { 2 } } } .
$$

Since $\mathbf { p }$ points in the same direction as $\mathbf { y }$ ,

$$
\mathbf { p } = \operatorname { p r o j } _ { \mathbf { y } } \mathbf { x } = { \frac { \mathbf { x } ^ { T } \mathbf { y } } { \mathbf { y } ^ { T } \mathbf { y } } } \mathbf { y } .
$$

The vector $\mathbf { p }$ is called the orthogonal projection or simply the projection of $\mathbf { x }$ onto $\mathbf { y }$ .

![](images/315cf57af580e29fc10670f9126c7f2d87b2f7dcb6ad9ab9475fa08c0e74884b.jpg)  
Figure A.2 The orthogonal projection of $\mathbf { x }$ onto y.

Similarly, if $W$ is a subspace of $R ^ { n }$ with an orthogonal basis $\mathbf { w } _ { 1 } , \mathbf { w } _ { 2 } , \ldots . \mathbf { \mu } . \mathbf { w } _ { p } ,$ , then the orthogonal projection of $\mathbf { x }$ onto $W$ is

$$
\mathbf { p } = \mathrm { p r o j } _ { W } \mathbf { x } = \frac { \mathbf { x } ^ { T } \mathbf { w } _ { 1 } } { \mathbf { w } _ { 1 } ^ { T } \mathbf { w } _ { 1 } } \mathbf { w } _ { 1 } + \frac { \mathbf { x } ^ { T } \mathbf { w } _ { 2 } } { \mathbf { w } _ { 2 } ^ { T } \mathbf { w } _ { 2 } } \mathbf { w } _ { 2 } + \cdot \cdot \cdot + \frac { \mathbf { x } ^ { T } \mathbf { w } _ { p } } { \mathbf { w } _ { p } ^ { T } \mathbf { w } _ { p } } \mathbf { w } _ { p } .
$$

Note that this equation can be simplified considerably if the orthogonal basis vectors are also orthonormal. In that case, $\mathbf { w } _ { 1 } ^ { \bar { T } } \mathbf { w } _ { 1 } , \mathbf { w } _ { 2 } ^ { T } \mathbf { w } _ { 2 } , \ldots . . . , \mathbf { w } _ { p } ^ { T } \mathbf { w } _ { p }$ are all 1.

It is inconvenient that the projection formula requires an orthogonal basis. The Gram-Schmidt orthogonalization process can be used to turn any basis for a subspace of $R ^ { n }$ into an orthogonal basis. We begin with a basis $\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } , \ldots . \mathbf { \mu } , \mathbf { v } _ { p } $ . The process recursively constructs an orthogonal basis by taking each vector in the original basis and then subtracting off its projection on the space spanned by the previous vectors. The formulas are

$$
\mathbf { w } _ { 1 } = \mathbf { v } _ { 1 }
$$

$$
\begin{array} { r } { \mathbf { w } _ { 2 } = \mathbf { v } _ { 2 } - \frac { \mathbf { v } _ { 1 } ^ { T } \mathbf { v } _ { 2 } } { \mathbf { v } _ { 1 } ^ { T } \mathbf { v } _ { 1 } } \mathbf { v } _ { 1 } = \mathbf { v } _ { 2 } - \frac { \mathbf { w } _ { 1 } ^ { T } \mathbf { v } _ { 2 } } { \mathbf { w } _ { 1 } ^ { T } \mathbf { w } _ { 1 } } \mathbf { w } _ { 1 } } \end{array}
$$

$$
\mathbf { w } _ { p } = \mathbf { v } _ { p } - { \frac { \mathbf { w } _ { 1 } ^ { T } \mathbf { v } _ { p } } { \mathbf { w } _ { 1 } ^ { T } \mathbf { w } _ { 1 } } } \mathbf { w } _ { 1 } - \cdot \cdot \cdot - { \frac { \mathbf { w } _ { p } ^ { T } \mathbf { v } _ { p } } { \mathbf { w } _ { p } ^ { T } \mathbf { w } _ { p } } } \mathbf { w } _ { p } .
$$

Unfortunately, the Gram-Schmidt process is numerically unstable when applied to large bases. In MATLAB the command orth provides a numerically stable way to produce an orthogonal basis from a nonorthogonal basis. An important property of orthogonal projection is that the projection of $\mathbf { x }$ onto $W$ is the point in $W$ which is closest to $\mathbf { x }$ . In the special case that $\mathbf { x }$ is in $W$ , the projection of $\mathbf { x }$ onto $W$ is $\mathbf { x }$ .

Given an inconsistent system of equations $\mathbf { A x } = \mathbf { b }$ , it is often desirable to find an approximate solution. A natural measure of the quality of an approximate solution is the norm of the difference between Ax and $\mathbf { b }$ , $\| \mathbf { A x } - \mathbf { b } \|$ . A solution that minimizes the 2-norm, $\| \mathbf { A x } - \mathbf { b } \| _ { 2 }$ , is called a least squares solution, because it minimizes the sum of the squares of the residuals.

The least squares solution can be obtained by projecting $\mathbf { b }$ onto $R ( \mathbf { A } )$ . This calculation requires us to first find an orthogonal basis for $R ( \mathbf { A } )$ . There is an alternative approach that does not require finding an orthogonal basis. Let

$$
\mathbf { A } \mathbf { x } _ { l s } = \mathrm { p r o j } _ { R ( \mathbf { A } ) } \mathbf { b } .
$$

Then, the difference between the projection (A.71) and $\mathbf { b }$ , $\mathbf { A x } _ { l s } - \mathbf { b }$ , will be perpendicular to $R ( \mathbf { A } )$ (Figure A.3). This orthogonality means that each of the columns of A will be orthogonal to $\mathbf { A x } _ { l s } - \mathbf { b }$ . Thus

$$
\mathbf { A } ^ { T } ( \mathbf { A x } _ { l s } - \mathbf { b } ) = \mathbf { 0 }
$$

![](images/466c3f0ffd37487759cd3359e2ca975d7cf47f0abdb257606c1227c0ecb023f9.jpg)  
Figure A.3 Geometric conceptualization of the least squares solution to $\mathbf { A } \mathbf { x } = \mathbf { b }$ . b generally lies in $R ^ { m }$ , but $R ( \mathbf { A } )$ is generally a subspace of $R ^ { m }$ . The least squares solution $\mathbf { x } _ { l s }$ minimizes $\| \mathbf { A x } - \mathbf { b } \| _ { 2 }$ .

or

$$
\mathbf { A } ^ { T } \mathbf { A x } _ { l s } = \mathbf { A } ^ { T } \mathbf { b } .
$$

This last system of equations is referred to as the normal equations for the least squares problem. It can be shown that if the columns of $\mathbf { A }$ are linearly independent, then the normal equations have exactly one solution for $\mathbf { x } _ { l s }$ and this solution minimizes the sum of squared residuals [95].

# A.6. EIGENVALUES AND EIGENVECTORS

Definition A.24 An $n$ by $n$ matrix A has an eigenvalue $\lambda$ with an associated eigenvector $\mathbf { x }$ if $\mathbf { x }$ is not 0, and

$$
\mathbf { A } \mathbf { x } = \lambda \mathbf { x } .
$$

To find eigenvalues and eigenvectors, we rewrite the eigenvector equation (A.74) as

$$
( \mathbf { A } - \lambda \mathbf { I } ) \mathbf { x } = \mathbf { 0 } .
$$

To find nonzero eigenvectors, the matrix $\mathbf { A } - \lambda \mathbf { I }$ must be singular. This leads to the characteristic equation,

$$
\operatorname* { d e t } ( \mathbf { A } - \lambda \mathbf { I } ) = 0 .
$$

where det denotes the determinant. For small matrices (e.g., 2 by 2 or 3 by 3), it is relatively easy to solve (A.76) to find the eigenvalues. The eigenvalues can then be substituted into (A.75), and the resulting system can then be solved to find corresponding eigenvectors. Note that the eigenvalues can, in general, be complex. For larger matrices, solving the characteristic equation becomes impractical and more sophisticated numerical methods are used. The MATLAB command eig can be used to find eigenvalues and eigenvectors of a matrix.

Suppose that we can find a set of $n$ linearly independent eigenvectors, $\mathbf { v } _ { i }$ , of an $n$ by $n$ matrix A with associated eigenvalues $\lambda _ { i }$ . These eigenvectors form a basis for $R ^ { n } .$ . We can use the eigenvectors to diagonalize the matrix as

$$
\mathbf { A } = \mathbf { P } \mathbf { A } \mathbf { P } ^ { - 1 } ,
$$

where

$$
\mathbf { P } = \left[ \mathbf { v } _ { 1 } \quad \mathbf { v } _ { 2 } \quad \ldots \quad \mathbf { v } _ { n } \right] ,
$$

and $\pmb { \Lambda }$ is a diagonal matrix of eigenvalues

$$
\Lambda _ { i i } = \lambda _ { i } .
$$

To see that this works, simply compute AP:

$$
\begin{array} { r l } { \mathbf { A P } = \mathbf { A } \left[ \mathbf { v } _ { 1 } \quad \mathbf { v } _ { 2 } \quad . ~ . ~ . ~ \mathbf { v } _ { n } \right] } & { } \\ { = \left[ \lambda _ { 1 } \mathbf { v } _ { 1 } \quad \lambda _ { 2 } \mathbf { v } _ { 2 } \quad . ~ . ~ . ~ \lambda _ { n } \mathbf { v } _ { n } \right] } & { } \\ { = \mathbf { P A } . } \end{array}
$$

Thus, $\mathbf { A } = \mathbf { P } \pmb { \Lambda } \mathbf { P } ^ { - 1 } ,$ . Not all matrices are diagonalizable, because not all matrices have $n$ linearly independent eigenvectors. However, there is an important special case in which matrices can always be diagonalized.

Theorem A.7 If A is a real symmetric matrix, then A can be written as

$$
\mathbf { A } = \mathbf { Q } \mathbf { A } \mathbf { Q } ^ { - 1 } = \mathbf { Q } \mathbf { A } \mathbf { Q } ^ { T } ,
$$

where $\mathbf { Q }$ is a real orthogonal matrix of eigenvectors of $\mathbf { A }$ , and $\pmb { \Lambda }$ is a real diagonal matrix of the eigenvalues of A.

This orthogonal diagonalization of a real symmetric matrix A will be useful later on when we consider orthogonal factorizations of general matrices.

The eigenvalues of symmetric matrices are particularly important in the analysis of quadratic forms.

Definition A.25 A quadratic form is a function of the form

$$
f ( \mathbf { x } ) = \mathbf { x } ^ { T } \mathbf { A } \mathbf { x } ,
$$

where $\mathbf { A }$ is a symmetric $n \times n$ matrix. The quadratic form $f ( \mathbf { x } )$ is positive definite if $f ( x ) \geq 0$ for all $\mathbf { x }$ and $f ( \mathbf { x } ) = 0$ only when $\mathbf { x } = \mathbf { 0 }$ . The quadratic form is positive semidefinite if $f ( \mathbf { x } ) \geq 0$ for all $\mathbf { x }$ . Similarly, a symmetric matrix A is positive definite if the associated quadratic form $f ( \mathbf { x } ) = \mathbf { x } ^ { T } \mathbf { A } \mathbf { x }$ is positive definite. The quadratic form is negative semidefinite if $- f ( \mathbf { x } )$ is positive semidefinite. If $f ( \mathbf { x } )$ is neither positive semidefinite nor negative semidefinite, then $f ( \mathbf { x } )$ is indefinite.

Positive definite quadratic forms have an important application in analytic geometry. Let A be a symmetric and positive definite matrix. Then the region defined by the inequality

$$
( \mathbf { x } - \mathbf { c } ) ^ { T } \mathbf { A } ( \mathbf { x } - \mathbf { c } ) \leq \delta
$$

is an ellipsoidal volume, with its center at c. We can diagonalize $\mathbf { A }$ as

$$
\mathbf { A } = \mathbf { P } \mathbf { A } \mathbf { P } ^ { - 1 } ,
$$

where the columns of $\mathbf { P }$ are normalized eigenvectors of $\mathbf { A }$ , and $\pmb { \Lambda }$ is a diagonal matrix whose elements are the eigenvalues of A. It can be shown that the ith eigenvector of A points in the direction of the ith semimajor axis of the ellipsoid, and the length of the√ ith semimajor axis is given by $\sqrt { \delta / \lambda _ { i } }$ [95].

An important connection between positive semidefinite matrices and eigenvalues is the following theorem.

Theorem A.8 $A$ symmetric matrix A is positive semidefinite if and only if its eigenvalues are greater than or equal to 0. A is positive definite if and only if its eigenvalues are greater than 0.

This provides a convenient way to check whether a symmetric matrix is positive semidefinite or positive definite.

The Cholesky factorization provides another way to determine whether a symmetric matrix is positive definite.

Theorem A.9 Let A be an an n by $n$ positive definite and symmetric matrix. Then A can be written uniquely as

$$
\mathbf { A } = \mathbf { R } ^ { T } \mathbf { R } = \mathbf { L } \mathbf { L } ^ { T } ,
$$

where R is a nonsingular upper-triangular matrix and ${ \bf L } = { \bf R } ^ { T }$ is a nonsingular lower-triangular matrix. Note that A can be factored in this way if and only if it is positive definite.

The MATLAB command chol can be used to compute the Cholesky factorization.

# A.7. VECTOR AND MATRIX NORMS

Although the conventional Euclidean length (A.61) is most commonly used, there are alternative ways to measure the length of a vector.

Definition A.26 Any measure of vector length satisfying the following four conditions is called a norm.

1. For any vector $\mathbf { x }$ , $\| \mathbf { x } \| \geq 0$ .   
2. For any vector $\mathbf { x }$ and any scalar $s$ , $\| s \mathbf { x } \| = | s | \| \mathbf { x } \|$ .   
3. For any vectors $\mathbf { x }$ and $\mathbf { y }$ , $\| \mathbf { x } + \mathbf { y } \| \leq \| \mathbf { x } \| + \| \mathbf { y } \|$ .   
4. $\| \mathbf { x } \| = 0$ if and only if $\mathbf { x } = \mathbf { 0 }$ .

If $\Vert { \big \vert } { \big \vert } $ satisfies conditions 1, 2, and 3, but does not satisfy condition 4, then $\Vert { \big \vert } { \big \Vert }$ is called a seminorm.

Definition A.27 The $p$ -norm of a vector in $R ^ { n }$ is defined for $p \geq 1$ by

$$
\| x \| _ { p } = ( | x _ { 1 } | ^ { p } + | x _ { 2 } | ^ { p } + \cdot \cdot \cdot + | x _ { n } | ^ { p } ) ^ { 1 / p } .
$$

It can be shown that for any $p \geq 1$ , (A.85) satisfies the conditions of Definition A.26 [53]. The conventional Euclidean length is just the 2-norm, but two other $p$ -norms are also commonly used. The 1-norm is the sum of the absolute values of the elements in $\mathbf { x }$ . The $\infty$ -norm is obtained by taking the limit as $p$ goes to infinity. The $\infty$ -norm is the maximum of the absolute values of the elements in $\mathbf { x }$ . The MATLAB command norm can be used to compute the norm of a vector, and has options for the 1, 2, and infinity norms.

The 2-norm is particularly important because of its natural connection with dot products and projections. The projection of a vector onto a subspace is the point in the subspace that is closest to the vector as measured by the 2-norm. We have also seen in (A.73) that the problem of minimizing $\| \mathbf { A x } - \mathbf { b } \| _ { 2 }$ can be solved by computing projections or by using the normal equations. In fact, the 2-norm can be tied directly to the dot product by the formula

$$
\| \mathbf { x } \| _ { 2 } = { \sqrt { \mathbf { x } ^ { T } \mathbf { x } } } .
$$

The $1 -$ and $\infty$ -norms can also be useful in finding approximate solutions to overdetermined linear systems of equations. To minimize the maximum of the residuals, we minimize $\| \mathbf { A x - b } \| _ { \infty }$ . To minimize the sum of the absolute values of the residuals, we minimize $\| \mathbf { A x } - \mathbf { b } \| _ { 1 }$ . Unfortunately, these minimization problems are generally more difficult to solve than least squares problems.

Definition A.28 Any measure of the size or length of an $m$ by $n$ matrix that satisfies the following five properties can be used as a matrix norm.

1. For any matrix A, $\| \mathbf { A } \| \geq 0$ .   
2. For any matrix $\mathbf { A }$ and any scalar $s$ , $\| s \mathbf { A } \| = | s | \| \mathbf { A } \|$ .   
3. For any matrices A and $\mathbf { B }$ , $\| \mathbf { A + B } \| \leq \| \mathbf { A } \| + \| \mathbf { B } \|$ .   
4. $\| \mathbf { A } \| = 0$ if and only if $\mathbf { A } = \mathbf { 0 }$ .   
5. For any two matrices A and $\mathbf { B }$ of compatible sizes, $\| \mathbf { A B } \| \leq \| \mathbf { A } \| \| \mathbf { B } \|$ .

Definition A.29 The $p$ -norm of a matrix A is

$$
\| \mathbf { A } \| _ { p } = \operatorname* { m a x } _ { \| \mathbf { x } \| _ { p } = 1 } \| \mathbf { A } \mathbf { x } \| _ { p } ,
$$

where $\left\| \mathbf { x } \right\| _ { p }$ and $\| \mathbf { A x } \| _ { p }$ are vector $p .$ -norms, while $\| \mathbf { A } \| _ { p }$ is the matrix $p$ -norm of A.

Solving the maximization problem of (A.87) to determine a matrix $p .$ -norm could be extremely difficult. Fortunately, there are simpler formulas for the most commonly used matrix $p$ -norms. See Exercises A.11, A.12, and C.4:

$$
\begin{array} { r } { \| \mathbf { A } \| _ { 1 } = \displaystyle \operatorname* { m a x } _ { j } \sum _ { i = 1 } ^ { m } | A _ { i , j } | } \\ { \| \mathbf { A } \| _ { 2 } = \sqrt { \lambda _ { \operatorname* { m a x } } ( \mathbf { A } ^ { T } \mathbf { A } ) } } \\ { \| \mathbf { A } \| _ { \infty } = \displaystyle \operatorname* { m a x } _ { i } \sum _ { j = 1 } ^ { n } | A _ { i , j } | , } \end{array}
$$

where $\lambda _ { \operatorname* { m a x } } ( \mathbf { A } ^ { T } \mathbf { A } )$ denotes the largest eigenvalue of $\mathbf { A } ^ { T } \mathbf { A }$ .

Definition A.30 The Frobenius norm of an $m$ by $n$ matrix is given by

$$
\| \mathbf { A } \| _ { F } = \sqrt { \sum _ { i = 1 } ^ { m } \sum _ { j = 1 } ^ { n } A _ { i , j } ^ { 2 } } .
$$

Definition A.31 A matrix norm $\parallel \parallel _ { M }$ and a vector norm $\Vert \big | \big | \big | \big | \big | \big | \big | \big | \big |$ are compatible if

$$
\left\| \mathbf { A x } \right\| _ { V } \leq \left\| \mathbf { A } \right\| _ { M } \left\| \mathbf { x } \right\| _ { V } .
$$

The matrix $p$ -norm is by its definition compatible with the vector $p$ -norm from which it was derived. It can also be shown that the Frobenius norm of a matrix is compatible with the vector 2-norm [109]. Thus the Frobenius norm is often used with the vector 2-norm.

In practice, the Frobenius norm, 1-norm, and $\infty \cdot$ -norm of a matrix are easy to compute, while the 2-norm of a matrix can be difficult to compute for large matrices. The MATLAB norm command has options for computing these matrix norms.

# A.8. THE CONDITION NUMBER OF A LINEAR SYSTEM

Suppose that we want to solve a system of $n$ equations in $n$ variables

$$
\mathbf { A x } = \mathbf { b } .
$$

Suppose further that because of measurement errors in $\mathbf { b }$ , we actually solve

$$
\begin{array} { r } { \mathbf { A } \hat { \mathbf { x } } = \hat { \mathbf { b } } . } \end{array}
$$

Can we get a bound on $\lVert \bf { x } - \hat { \bf { x } } \rVert$ in terms of $\| \mathbf { b } - { \hat { \mathbf { b } } } \| $ ? Starting with (A.93) and (A.94), we have

$$
\begin{array} { r l } & { \mathbf { A } ( \mathbf { x } - \hat { \mathbf { x } } ) = \mathbf { b } - \hat { \mathbf { b } } } \\ & { \quad ( \mathbf { x } - \hat { \mathbf { x } } ) = \mathbf { A } ^ { - 1 } ( \mathbf { b } - \hat { \mathbf { b } } ) } \\ & { \| \mathbf { x } - \hat { \mathbf { x } } \| = \| \mathbf { A } ^ { - 1 } ( \mathbf { b } - \hat { \mathbf { b } } ) \| } \\ & { \quad \| \mathbf { x } - \hat { \mathbf { x } } \| \leq \| \mathbf { A } ^ { - 1 } \| \| \mathbf { b } - \hat { \mathbf { b } } \| . } \end{array}
$$

This formula provides an absolute bound on the error in the solution. It is also worthwhile to compute a relative error bound:

$$
\begin{array} { r l } & { \frac { \| { \bf x } - { \hat { \bf x } } \| } { \| { \bf b } \| } \leq \frac { \| { \bf A } ^ { - 1 } \| \| { \bf b } - { \hat { \bf b } } \| } { \| { \bf b } \| } } \\ & { \frac { \| { \bf x } - { \hat { \bf x } } \| } { \| { \bf A } ^ { - 1 } \| } \leq \frac { \| { \bf A } ^ { - 1 } \| \| { \bf b } - { \hat { \bf b } } \| } { \| { \bf b } \| } } \\ & { \| { \bf x } - { \hat { \bf x } } \| \leq \| { \bf A } { \bf x } \| \| { \bf A } ^ { - 1 } \| \frac { \| { \bf b } - { \hat { \bf b } } \| } { \| { \bf b } \| } } \\ & { \| { \bf x } - { \hat { \bf x } } \| \leq \| { \bf A } \| \| { \bf x } \| \| { \bf A } ^ { - 1 } \| \frac { \| { \bf b } - { \hat { \bf b } } \| } { \| { \bf b } \| } } \\ & { \frac { \| { \bf x } - { \hat { \bf x } } \| } { \| { \bf x } \| } \leq \| { \bf A } \| \| { \bf x } ^ { 1 } \| \| { \bf A } ^ { - 1 } \| \frac { \| { \bf b } - { \hat { \bf b } } \| } { \| { \bf b } \| } } \\ & { \frac { \| { \bf x } - { \hat { \bf x } } \| } { \| { \bf x } \| } \leq \| { \bf A } \| \| { \bf A } ^ { - 1 } \| \frac { \| { \bf b } - { \hat { \bf b } } \| } { \| { \bf b } \| } . } \end{array}
$$

The relative error in $\mathbf { b }$ is measured by

$$
{ \frac { \| \mathbf { b } - { \hat { \mathbf { b } } } \| } { \| \mathbf { b } \| } } .
$$

The relative error in $\mathbf { x }$ is measured by

$$
\frac { \lVert \mathbf { x } - \hat { \mathbf { x } } \rVert } { \lVert \mathbf { x } \rVert } .
$$

The constant

$$
\mathrm { c o n d } ( \mathbf { A } ) = \| \mathbf { A } \| \| \mathbf { A } ^ { - 1 } \|
$$

is called the condition number of A.

Note that nothing that we did in the calculation of the condition number depends on which norm we used. The condition number can be computed using the 1-norm,

2-norm, $\infty$ -norm, or Frobenius norm. The MATLAB cond command can be used to find the condition number of a matrix using each of these norms.

The condition number provides an upper bound on how inaccurate the solution to a system of equations might be because of errors in the right-hand side. In some cases, the condition number greatly overestimates the error in the solution. As a practical matter, it is wise to assume that the error is of roughly the size predicted by the condition number. In practice, double-precision floating point arithmetic only allows us to store numbers to about 16 digits of precision. If the condition number is greater than $1 0 ^ { 1 6 }$ , then by the above inequality, there may be no accurate digits in the computer solution to the system of equations. Systems of equations with very large condition numbers are called ill-conditioned.

It is important to understand that ill-conditioning is a property of the system of equations and not of the algorithm used to solve the system of equations. Ill-conditioning cannot be fixed simply by using a better algorithm. Instead, we must either increase the precision of our floating point representation or find a different, better conditioned system of equations to solve.

# A.9. THE QR FACTORIZATION

Although the theory of linear algebra can be developed using the reduced row echelon form, there is an alternative computational approach that works better in practice. The basic idea is to compute factorizations of matrices that involve orthogonal, diagonal, and upper-triangular matrices. This alternative approach leads to algorithms that can quickly compute accurate solutions to linear systems of equations and least squares problems. In this section we introduce the QR factorization, which is one of the most widely used orthogonal matrix factorizations. Another factorization, the singular value decomposition (SVD), is introduced in Chapter 3.

Theorem A.10 Let A be an m by n matrix. A can be written as

$$
\mathbf { A } = \mathbf { Q } \mathbf { R } ,
$$

where $\mathbf { Q }$ is an m by m orthogonal matrix, and $\mathbf { R }$ is an m by n upper-triangular matrix. This is called the QR factorization of A.

The MATLAB command qr can be used to compute the QR factorization of a matrix. In a common situation, A will be an $m$ by $n$ matrix with $m > n$ , and the rank of A will be $n$ . In this case, we can write

$$
\begin{array} { r } { \mathbf { R } = \biggl [ \mathbf { R } _ { 1 } \biggr ] , } \end{array}
$$

where $\mathbf { R } _ { 1 }$ is $n$ by $n$ , and

$$
\begin{array} { r } { { \bf Q } = [ { \bf Q } _ { 1 } \quad { \bf Q } _ { 2 } ] , } \end{array}
$$

where $\mathbf { Q } _ { 1 }$ is $m$ by $n$ and $\mathbf { Q } _ { 2 }$ is $m$ by $m - n$ . In this case, the QR factorization has some important properties.

Theorem A.11 Let $\mathbf { Q }$ and $\mathbf { R }$ be the QR factorization of an m by n matrix A with $m > n$ and ran $k ( \mathbf { A } ) = n$ . Then,

1. The columns of ${ \bf Q } _ { 1 }$ are an orthonormal basis for $R ( \mathbf { A } )$ .   
2. The columns of $\mathbf { Q } _ { 2 }$ are an orthonormal basis for $N ( \mathbf { A } ^ { T } )$ .   
3. The matrix $\mathbf { R } _ { 1 }$ is nonsingular.

Now, suppose that we want to solve the least squares problem,

$$
\operatorname* { m i n } \| \mathbf { A x } - \mathbf { b } \| _ { 2 } .
$$

Since multiplying a vector by an orthogonal matrix does not change its length, this is equivalent to

$$
\operatorname* { m i n } \| \mathbf { Q } ^ { T } ( \mathbf { A x } - \mathbf { b } ) \| _ { 2 } .
$$

But

$$
{ \bf Q } ^ { T } { \bf A } = { \bf Q } ^ { T } { \bf Q } { \bf R } = { \bf R } .
$$

So, we have

$$
\operatorname* { m i n } \lVert \mathbf { R } \mathbf { x } - \mathbf { Q } ^ { T } \mathbf { b } \rVert _ { 2 }
$$

or

$$
\begin{array} { r } { \operatorname* { m i n } \| \mathbf { R } _ { 1 } \mathbf { x } - \mathbf { Q } _ { 1 } ^ { T } \mathbf { b } \| _ { 2 } . } \\ { \mathbf { 0 } \mathbf { x } - \mathbf { Q } _ { 2 } ^ { T } \mathbf { b } \| _ { 2 } } \end{array}
$$

Whatever value of $\mathbf { x }$ we pick, we will probably end up with nonzero residuals because of the $\mathbf { 0 x } - \mathbf { Q } _ { 2 } ^ { T } \mathbf { b }$ part of the least squares problem. We cannot minimize the norm of this part of the vector. However, we can find an $\mathbf { x }$ that exactly solves $\mathbf { R } _ { 1 } \mathbf { x } = \mathbf { Q } _ { 1 } ^ { T } \mathbf { b }$ . Thus, we can minimize the least squares problem by solving the square system of equations,

$$
\mathbf { R } _ { 1 } \mathbf { x } = \mathbf { Q } _ { 1 } ^ { T } \mathbf { b } .
$$

The advantage of solving this system of equations instead of the normal equations (A.73) is that the normal equations are typically much more badly conditioned than (A.115).

# A.10. COMPLEX MATRICES AND VECTORS

Although nearly all of the mathematics in this textbook involves real numbers, complex numbers do appear in Chapter 8 when we consider the Fourier transform. We assume that the reader is already familiar with arithmetic involving complex numbers including addition, subtraction, multiplication, division, and complex exponentials. Most theorems of linear algebra extend trivially from real to complex vectors and matrices. In this section we briefly discuss our notation and some important differences between the real and complex cases.

Given a complex number $z = a + b \imath$ , where $\imath$ is the $\sqrt { - 1 }$ , the complex conjugate of $z$ is $z ^ { * } = a - b \quad$ . Note that the absolute value of $z$ is

$$
| z | = { \sqrt { a ^ { 2 } + b ^ { 2 } } } = { \sqrt { z ^ { * } z } } .
$$

The main difference between linear algebra on real vectors and complex vectors is in the definition of the dot product of two vectors. We define the dot product of two complex vectors $\mathbf { x }$ and $\mathbf { y }$ to be

$$
\mathbf { x } \cdot \mathbf { y } = \mathbf { x } ^ { * ^ { T } } \mathbf { y } .
$$

The advantage of this definition is that

$$
\mathbf { x ^ { * } } ^ { T } \mathbf { x } = \sum _ { k = 1 } ^ { n } x _ { k } ^ { * } x _ { k } = \sum _ { k = 1 } ^ { n } | x _ { k } | ^ { 2 } .
$$

Thus we can then define the 2-norm of a complex vector by

$$
\| \boldsymbol { x } \| _ { 2 } = \sqrt { \mathbf { x } ^ { * } \overset { T } { \mathbf { x } } } .
$$

The combination of taking the complex conjugate and transpose, called the Hermitian transpose, occurs so frequently that we denote this by

$$
\mathbf { x } ^ { H } = \mathbf { x } ^ { * ^ { T } } .
$$

Note that for a real vector, $\mathbf { x }$ , the conjugate is simply ${ \bf x } ^ { * } = { \bf x }$ , so $\mathbf { x } ^ { H } = \mathbf { x } ^ { T } .$ In MATLAB, the apostrophe denotes the Hermitian transpose.

In general, you will almost never go wrong by using the Hermitian transpose in any linear algebra computation involving complex numbers that would normally involve a transpose when working with real vectors and matrices. For example, if we want to minimize $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ , where ${ \bf G } , { \bf m }$ , and $\mathbf { d }$ are complex, we can solve the normal equations,

$$
\mathbf { G } ^ { H } \mathbf { G } \mathbf { m } = \mathbf { G } ^ { H } \mathbf { d } .
$$

# A.11. LINEAR ALGEBRA IN SPACES OF FUNCTIONS

So far, we have considered only vectors in $R ^ { n } .$ The concepts of linear algebra can be extended to other contexts. In general, as long as the objects that we want to consider can be multiplied by scalars and added together, and as long as they obey the laws of vector algebra, then we have a vector space in which we can practice linear algebra. If we can also define a vector product similar to the dot product, then we have what is called an inner product space, and we can define orthogonality, projections, and the 2-norm.

There are many different vector spaces used in various areas of science and mathematics. For our work in inverse problems, a very commonly used vector space is the space of functions defined on an interval [a, b].

Multiplying a scalar times a function or adding two functions together clearly produces another function. In this space, the function $z ( x ) = 0$ takes the place of the 0 vector, since $f ( x ) + z ( x ) = f ( x )$ . Two functions $f ( x )$ and $g ( x )$ are linearly independent if the only solution to

$$
c _ { 1 } f ( x ) + c _ { 2 } g ( x ) = z ( x )
$$

is $c _ { 1 } = c _ { 2 } = 0$ .

We can define the dot product of two functions $f$ and $g$ to be

$$
f \cdot g = \int _ { a } ^ { b } f ( x ) g ( x ) \ d x .
$$

Another commonly used notation for this dot product or inner product of $f$ and $g$ is

$$
f \cdot g = \langle f , g \rangle .
$$

It is easy to show that this inner product has all of the algebraic properties of the dot product of two vectors in $R ^ { n } .$ A more important motivation for defining the dot product in this way is that it leads to a useful definition of the 2-norm of a function. Following√ our earlier formula that $\| x \| _ { 2 } = \sqrt { x ^ { T } x }$ , we have

$$
\| f \| _ { 2 } = { \sqrt { \int _ { a } ^ { b } f ( x ) ^ { 2 } \ d x } } .
$$

Using this definition, the distance between two functions $f$ and $g$ is

$$
\| f - g \| _ { 2 } = { \sqrt { \int _ { a } ^ { b } ( f ( x ) - g ( x ) ) ^ { 2 } \ d x } } .
$$

This measure is obviously 0 when $f ( x ) = g ( x )$ everywhere, but can also be 0 when $f ( x )$ and $g ( x )$ differ at a finite or countably infinite set of points. The measure is only nonzero if $\dot { \boldsymbol { f } } ( \boldsymbol { x } )$ and $g ( x )$ differ on an interval.

Using this inner product and norm, we can reconstruct the theory of linear algebra from $R ^ { n }$ in our space of functions. This includes the concepts of orthogonality, projections, norms, and least squares solutions.

Definition A.32 Given a collection of functions $f _ { 1 } ( x ) , f _ { 2 } ( x ) , . . . . , f _ { m } ( x )$ in an inner product space, the Gram matrix of the functions is the $m \times m$ matrix $\mathbf { \Gamma }$ , whose elements are given by

$$
\Gamma _ { i , j } = f _ { i } \cdot f _ { j } .
$$

The Gram matrix has several important properties. It is symmetric and positive semidefinite. If the functions are linearly independent, then the Gram matrix is also positive definite. Furthermore, the rank of $\mathbf { \Gamma }$ is equal to the size of the largest linearly independent subset of the functions $f _ { 1 } ( x ) , \ldots . \ldots , f _ { m } ( x )$ .

# A.12. EXERCISES

1. Let A be an $m$ by $n$ matrix with $n$ pivot columns in its RREF. Can the system of equations $\mathbf { A x } = \mathbf { b }$ have infinitely many solutions?

2. If $\mathbf { C } = \mathbf { A } \mathbf { B }$ is a 5 by 4 matrix, then how many rows does A have? How many columns does $\mathbf { B }$ have? Can you say anything about the number of columns in A?

3. Suppose that $\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 }$ , and $\mathbf { v } _ { 3 }$ are three vectors in $R ^ { 3 }$ and that $\mathbf { v } _ { 3 } = - 2 \mathbf { v } _ { 1 } + 3 \mathbf { v } _ { 2 }$ . Are the vectors linearly dependent or linearly independent?

4. Let

$$
\mathbf { A } = { \left[ \begin{array} { l l l l } { 1 } & { 2 } & { 3 } & { 4 } \\ { 2 } & { 2 } & { 1 } & { 3 } \\ { 4 } & { 6 } & { 7 } & { 1 1 } \end{array} \right] } .
$$

Find bases for ${ \cal N } ( { \bf A } ) , { \cal R } ( { \bf A } ) , { \cal N } ( { \bf A } ^ { T } )$ , and $R ( \mathbf { A } ^ { T } )$ . What are the dimensions of the four subspaces?

5. Let A be an $n$ by $n$ matrix such that $\mathbf { A } ^ { - 1 }$ exists. What are ${ \cal N } ( { \bf A } ) , { \cal R } ( { \bf A } ) , { \cal N } ( { \bf A } ^ { T } )$ and $R ( \mathbf { A } ^ { T } ) \vec { \ ? }$

6. Let A be any 9 by 6 matrix. If the dimension of the null space of $\mathbf { A }$ is 5, then what is the dimension of $R ( \mathbf { A } )$ ? What is the dimension of $R ( \mathbf { A } ^ { T } ) \vec { \ ? }$ What is the rank of A?

7. Suppose that a nonhomogeneous system of equations with four equations and six unknowns has a solution with two free variables. Is it possible to change the righthand side of the system of equations so that the modified system of equations has no solutions?

8. Let $W$ be the set of vectors $\mathbf { x }$ in $R ^ { 4 }$ such that $x _ { 1 } x _ { 2 } = 0$ . Is $W$ a subspace of $R ^ { 4 }$ ?

9. Let $\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } , \mathbf { v } _ { 3 }$ be a set of three nonzero orthogonal vectors. Show that the vectors are also linearly independent.

10. Show that if $\mathbf { x } \perp \mathbf { y }$ , then

$$
\left\| \mathbf { x } + \mathbf { y } \right\| _ { 2 } ^ { 2 } = \left\| \mathbf { x } \right\| _ { 2 } ^ { 2 } + \left\| \mathbf { y } \right\| _ { 2 } ^ { 2 } .
$$

11. In this exercise, we will derive the formula (A.88) for the 1-norm of a matrix. Begin with the optimization problem

$$
\| \mathbf { A } \| _ { 1 } = \operatorname* { m a x } _ { \| \mathbf { x } \| _ { 1 } = 1 } \| \mathbf { A } \mathbf { x } \| _ { 1 } .
$$

(a) Show that if $\| \mathbf { x } \| _ { 1 } = 1$ , then

$$
\| \mathbf { A x } \| _ { 1 } \leq \operatorname* { m a x } _ { j } \sum _ { i = 1 } ^ { m } | A _ { i , j } | .
$$

(b) Find a vector $\mathbf { x }$ such that $\| \mathbf { x } \| _ { 1 } = 1$ , and

$$
\| \mathbf { A x } \| _ { 1 } = \operatorname* { m a x } _ { j } \sum _ { i = 1 } ^ { m } | A _ { i , j } | .
$$

(c) Conclude that

$$
\| \mathbf { A } \| _ { 1 } = \operatorname* { m a x } _ { \| \mathbf { x } \| _ { 1 } = 1 } \| \mathbf { A } \mathbf { x } \| _ { 1 } = \operatorname* { m a x } _ { j } \sum _ { i = 1 } ^ { m } | A _ { i , j } | .
$$

12. Derive the formula (A.90) for the infinity norm of a matrix.

13. Let $\mathbf { A }$ be an $m$ by $n$ matrix.

(a) Show that $\mathbf { A } ^ { T } \mathbf { A }$ is symmetric.   
(b) Show that $\mathbf { A } ^ { T } \mathbf { A }$ is positive semidefinite. Hint: Use the definition of positive semidefinite rather than trying to compute eigenvalues.   
(c) Show that if $\operatorname { r a n k } ( \mathbf { A } ) = n$ , then the only solution to $\mathbf { A x } = \mathbf { 0 }$ is $\mathbf { x } = \mathbf { 0 }$ .   
(d) Use part c to show that if ra $\operatorname { n k } ( \mathbf { A } ) = n$ , then $\mathbf { A } ^ { T } \mathbf { A }$ is positive definite.   
(e) Use part $\mathrm { d }$ to show that if ra $\mathrm { n k } ( \mathbf { A } ) = n$ , then $\mathbf { A } ^ { T } \mathbf { A }$ is nonsingular.   
(f) Show that $N ( \mathbf { A } ^ { T } \mathbf { A } ) = N ( \mathbf { A } )$ .

14. Show that

$$
\operatorname { c o n d } ( \mathbf { A } \mathbf { B } ) \leq \operatorname { c o n d } ( \mathbf { A } ) \operatorname { c o n d } ( \mathbf { B } ) .
$$

15. Let A be a symmetric and positive definite matrix with Cholesky factorization,

$$
\mathbf { A } = \mathbf { R } ^ { T } \mathbf { R } .
$$

Show how the Cholesky factorization can be used to solve $\mathbf { A x } = \mathbf { b }$ by solving two systems of equations, each of which has $\mathbf { R }$ or $\mathbf { R } ^ { T }$ as its matrix.

16. Let $P _ { 3 } [ 0 , 1 ]$ be the space of polynomials of degree less than or equal to 3 on the interval [0, 1]. The polynomials $p _ { 1 } ( x ) = 1 , p _ { 2 } ( x ) = x , p _ { 3 } ( x ) = x ^ { 2 }$ , and $p _ { 4 } ( x ) = x ^ { 3 }$ form a basis for $P _ { 3 } [ 0 , 1 ]$ , but they are not orthogonal with respect to the inner product,

$$
f \cdot g = \int _ { 0 } ^ { 1 } f ( x ) g ( x ) \ d x .
$$

Use the Gram-Schmidt orthogonalization process to construct an orthogonal basis for $P _ { 3 } [ 0 , 1 ]$ . Once you have your basis, use it to find the third-degree polynomial that best approximates $f ( x ) = e ^ { - x }$ on the interval [0, 1] in the least squares sense.

# A.13. NOTES AND FURTHER READING

Much of this material is typically covered in sophomore-level linear algebra courses, and there are an enormous number of textbooks at this level. One good introductory linear algebra textbook is [95]. At a slightly more advanced level, [109] and [152] are both excellent. The book by Strang and Borre [153] reviews linear algebra in the context of geodetic problems.

Fast and accurate algorithms for linear algebra computations are a somewhat more advanced and specialized topic. A classic reference is [53]. Other good books on this topic include [38] and [164].

The extension of linear algebra to spaces of functions is a topic in the subject of functional analysis. Unfortunately, most textbooks on functional analysis assume that the reader has a considerable mathematical background. One book that is reasonably accessible to readers with limited mathematical backgrounds is [102].

# Review of Probability and Statistics

# Synopsis

A brief review is given of the topics in classical probability and statistics that are used throughout the book. Connections between probability theory and its application to the analysis of data with random measurement errors are highlighted. Note that some very different philosophical interpretations of probability theory are discussed in Chapter 11.

# B.1. PROBABILITY AND RANDOM VARIABLES

The mathematical theory of probability begins with an experiment, which has a set $S$ of possible outcomes. We will be interested in events that are subsets $A$ of $S$ .

Definition B.1 The probability function $P$ is a function defined on subsets of $S$ with the following properties:

1. $P ( S ) = 1$ .   
2. For every event $A \subseteq S$ , $P ( A ) \geq 0$ .   
3. If events $A _ { 1 } , A _ { 2 }$ , . . . , $A _ { n }$ are pairwise mutually exclusive (i.e., impossible to both occur), so that $A _ { i } \cap A _ { j }$ is empty for all pairs $i , j$ , then

$$
P ( \cup _ { i = 1 } ^ { n } A _ { i } ) = \sum _ { i = 1 } ^ { n } P ( A _ { i } ) .
$$

The probability properties given above are fundamental to developing the mathematics of probability theory. However, applying this definition of probability to real-world situations frequently requires ingenuity.

# Example B.1

Consider the experiment of throwing a dart at a dart board. We will assume that our dart thrower is an expert who always hits the dart board. The sample space $S$ consists of the points on the dart board. We can define an event $A$ that consists of the points in the bullseye, so that $P ( A )$ is the probability that the thrower hits the bullseye.

In practice, the outcome of an experiment is often a number rather than an event. Random variables are a useful generalization of the basic concept of probability.

Definition B.2 A random variable $X$ is a function $X ( s )$ that assigns a value to each outcome $s$ in the sample space $S$ .

Each time that we perform an experiment, we obtain a particular value of the random variable. These values are called realizations of the random variable.

# Example B.2

To continue our previous example, let $X$ be the function that takes a point on the dart board and returns the associated score. Suppose that throwing the dart in the bullseye scores 50 points. Then for each point $s$ in the bullseye, $X ( s ) = 5 0$ .

In this book we deal frequently with experimental measurements that can include some random measurement error.

# Example B.3

Suppose that we measure the mass of an object five times to obtain the realizations $m _ { 1 } = 1 0 . 1 ~ \mathrm { k g }$ , $m _ { 2 } = 1 0 . 0 ~ \mathrm { k g }$ , $m _ { 3 } = 1 0 . 0 ~ \mathrm { k g }$ , $m _ { 4 } = 9 . 9 ~ \mathrm { k g } .$ , and $m _ { 5 } = 1 0 . 1 ~ \mathrm { k g }$ . We will assume that there is one true mass $m$ , and that the measurements we obtained varied because of random measurement errors $e _ { i }$ , so that

$$
\begin{array} { r } { m _ { 1 } = m + e _ { 1 } , m _ { 2 } = m + e _ { 2 } , m _ { 3 } = m + e _ { 3 } , m _ { 4 } = m + e _ { 4 } , m _ { 5 } = m + e _ { 5 } . } \end{array}
$$

We can treat the measurement errors as realizations of a random variable $E$ . Equivalently, since the true mass m is just a constant, we could treat the measurements $m _ { 1 }$ , $m _ { 2 }$ , . . . , $m _ { 5 }$ as realizations of a random variable $M$ . In practice it makes little difference whether we treat the measurements or the measurement errors as random variables.

Note that in a Bayesian approach the mass $m$ of the object would itself be a random variable. This is a viewpoint that we consider in Chapter 11.

The relative probability of realization values for a random variable can be characterized by a non-negative probability density function (PDF), $f _ { X } ( x )$ , with

$$
P ( X \leq a ) = \int _ { - \infty } ^ { a } f _ { X } ( x ) \ d x .
$$

Because a random variable always has some value,

$$
\intop _ { - \infty } ^ { \infty } f _ { X } ( x ) \ d x = 1 .
$$

The following definitions give some useful random variables that frequently arise in inverse problems.

Definition B.3 The uniform random variable on the the interval [a, b] (Figure B.1) has the following PDF:

$$
f _ { U } ( x ) = \left\{ { \begin{array} { l r } { \frac { 1 } { b - a } } & { a \leq x \leq b } \\ { 0 } & { x < a } \\ { 0 } & { x > b . } \end{array} } \right.
$$

Definition B.4 The normal or Gaussian random variable (Figure B.2) has the following PDF:

$$
f _ { N } ( x ) = { \frac { 1 } { \sigma { \sqrt { 2 \pi } } } } e ^ { - { \frac { 1 } { 2 } } ( x - \mu ) ^ { 2 } / \sigma ^ { 2 } } .
$$

The notation $N ( \mu , \sigma ^ { 2 } )$ is used to denote a normal distribution with parameters $\mu$ and $\sigma$ . The standard normal random variable, $N ( 0 , 1 )$ , has $\mu = 0$ and $\sigma ^ { 2 } = 1$ .

![](images/06caaa85f9f6d0ca1245ba0e49c0c3aebd53dfc8834e50cca460b072ca752234.jpg)  
Figure B.1 The PDF for the uniform random variable on [0, 1].

![](images/4eda9f198433205b805743c01deb9433c9cfd58cf597814937d4712794fd0a5f.jpg)  
Figure B.2 The PDF of the standard normal random variable.

![](images/97fb734eed2d79d0004396fc3efbc026c08416640111c4e88d12724202bb2400.jpg)  
Figure B.3 The Student’s $t$ probability density function for $\nu = 3$ and $\nu = 2 0$ . Dashed curve shows the normal distribution $N ( 0 , 1 )$ (Figure B 2).

Definition B.5 The Student’s $\pmb { t }$ distribution with $\nu$ degrees of freedom (Figure B.3) has the PDF

$$
f _ { t } ( x ) = \frac { \Gamma ( ( \nu + 1 ) / 2 ) } { \Gamma ( \nu / 2 ) } \frac { 1 } { \sqrt { \nu \pi } } \left( 1 + \frac { x ^ { 2 } } { \nu } \right) ^ { - ( \nu + 1 ) / 2 } ,
$$

where the gamma function is

$$
\Gamma ( x ) = \int _ { 0 } ^ { \infty } \xi ^ { x - 1 } e ^ { - \xi } d \xi .
$$

The Student’s $t$ distribution is so named because W. S. Gosset used the pseudonym “Student” in publishing the first paper in which the distribution appeared. In the limit as $\nu$ goes to infinity, Student’s $t$ distribution approaches a standard normal distribution. However, for small values of $\nu$ , (B.7) has a greater percentage of extreme values than (B.6).

Definition B.6 The $\chi ^ { 2 }$ random variable has the PDF (Figure B.4)

$$
f _ { \chi ^ { 2 } } ( x ) = \frac { 1 } { 2 ^ { \nu / 2 } \Gamma ( \nu / 2 ) } x ^ { \frac { 1 } { 2 } \nu - 1 } e ^ { - x / 2 } ,
$$

where the parameter $\nu$ is the number of degrees of freedom.

Definition B.7 The exponential random variable (Figure B.5) has the PDF

$$
f _ { e x p } ( x ) = \left\{ \begin{array} { l l } { \lambda e ^ { - \lambda x } } & { x \ge 0 } \\ { 0 } & { x < 0 . } \end{array} \right.
$$

Definition B.8 The double-sided exponential random variable (Figure B.6) has the PDF

$$
f _ { d e x p } ( x ) = \frac { 1 } { \sigma \sqrt { 2 } } e ^ { - \sqrt { 2 } | x - \mu | / \sigma } .
$$

![](images/0bab3696a67196878387d27408052b06b3b35978f00ecf8f6265b87122d7560b.jpg)  
Figure B.4 The $\chi ^ { 2 }$ PDF for several values of $\nu$ .

![](images/7bd4e208287089d8244ca9f3a96ba37e7ca62c93ecbf906b83bdae70b011f7a8.jpg)  
Figure B.5 The exponential PDF $\left( \lambda = 1 \right)$ ).

![](images/d40fd1acf921ec16268068be5c6f1049af5f63d3421ed3bcb3880a089ba48e15.jpg)  
Figure B.6 The double-sided exponential PDF $( \mu = 0$ , $\sigma = 1$ ).

It can be shown that for $n$ independent random variables, $X _ { i }$ , with standard normal distributions, the random variable

$$
Z = \sum _ { i = 1 } ^ { n } X _ { i } ^ { 2 }
$$

is a $\chi ^ { 2 }$ random variable with $\nu = n$ degrees of freedom [47].

The cumulative distribution function (CDF) $F _ { X } ( a )$ of a one-dimensional random variable $X$ is given by the definite integral of the associated PDF

$$
F _ { X } ( a ) = P ( X \leq a ) = \intop _ { - \infty } ^ { a } f _ { X } ( x ) \ d x .
$$

Note that $F _ { X } ( a )$ must lie in the interval [0, 1] for all $a$ , and is a nondecreasing function of $^ a$ because of the unit area and non-negativity of the PDF.

For the uniform PDF on the unit interval, for example, the CDF is a ramp function,

$$
\begin{array} { l } { { \displaystyle F _ { U } ( a ) = \int _ { - \infty } ^ { a } f _ { u } ( z ) ~ d z } } \\ { { \displaystyle F _ { U } ( a ) = \left\{ \begin{array} { l l } { { 0 } } & { { \quad a \leq 0 } } \\ { { a } } & { { 0 \leq a \leq 1 } } \\ { { 1 } } & { { \quad a > 1 . } } \end{array} \right. } } \end{array}
$$

The PDF, $f _ { X } ( x )$ , or CDF, $F _ { X } ( a )$ , completely determine the properties of a random variable. The probability that a particular realization of $X$ will lie within a general interval [a, $b ]$ i s

$$
\begin{array} { l } { { P ( a \leq X \leq b ) = P ( X \leq b ) - P ( X \leq a ) = F _ { X } ( b ) - F _ { X } ( a ) } } \\ { { \mathrm { ~ } } } \\ { { \displaystyle = \int _ { - \infty } ^ { b } f _ { X } ( x ) ~ d x - \int _ { - \infty } ^ { a } f _ { X } ( x ) ~ d x = \int _ { a } ^ { b } f _ { X } ( x ) ~ d x . } } \end{array}
$$

# B.2. EXPECTED VALUE AND VARIANCE

Definition B.9 The expected value of a random variable $X$ , denoted by $E [ X ]$ or $\mu ( X )$ , is

$$
E [ X ] = \int _ { - \infty } ^ { \infty } x f _ { X } ( x ) \ d x .
$$

In general, if $g ( X )$ is some function of a random variable $X$ , then

$$
E [ g ( X ) ] = \int _ { - \infty } ^ { \infty } g ( x ) f _ { X } ( x ) ~ d x .
$$

Some authors use the term “mean” for the expected value of a random variable. We will reserve this term for the average of a set of data. Note that the expected value of

a random variable is not necessarily identical to the mode (the value with the largest value of $f ( x ) )$ nor is it necessarily identical to the median, the value of $_ x$ for which the value of the CDF is $F _ { X } ( x ) = 1 / 2$ .

# Example B.4

The expected value of an $N ( \mu , \sigma )$ random variable $X$ is

$$
{ \begin{array} { r l } & { E [ X ] = \displaystyle \int _ { - \infty } ^ { \infty } x { \frac { 1 } { \sigma { \sqrt { 2 \pi } } } } e ^ { - { \frac { ( x - \mu ) ^ { 2 } } { 2 \sigma ^ { 2 } } } } d x } \\ & { \qquad = \displaystyle \int _ { - \infty } ^ { \infty } { \frac { 1 } { \sigma { \sqrt { 2 \pi } } } } ( x + \mu ) e ^ { - { \frac { x ^ { 2 } } { 2 \sigma ^ { 2 } } } } d x } \\ & { \qquad = \mu \displaystyle \int _ { - \infty } ^ { \infty } { \frac { 1 } { \sigma { \sqrt { 2 \pi } } } } e ^ { - { \frac { x ^ { 2 } } { 2 \sigma ^ { 2 } } } } d x + \displaystyle \int _ { - \infty } ^ { \infty } { \frac { 1 } { \sigma { \sqrt { 2 \pi } } } } x e ^ { - { \frac { x ^ { 2 } } { 2 \sigma ^ { 2 } } } } d x . } \end{array} }
$$

The first integral term is $\mu$ because the integral of the entire PDF is 1, and the second term is 0 because it is an odd function integrated over a symmetric interval. Thus,

$$
E [ X ] = \mu .
$$

Definition B.10 The variance of a random variable $X$ , denoted by $\operatorname { V a r } ( X )$ or $\sigma _ { X } ^ { 2 }$ , is given by

$$
\begin{array} { l } { \displaystyle \mathrm { V a r } ( X ) = E [ ( X - E [ X ] ) ^ { 2 } ] } \\ { \displaystyle = E [ X ^ { 2 } ] - E [ X ] ^ { 2 } } \\ { \displaystyle = \int _ { - \infty } ^ { \infty } ( x - E [ X ] ) ^ { 2 } f _ { X } ( x ) ~ d x . } \end{array}
$$

The standard deviation of $X$ , often denoted $\sigma _ { X }$ , is

$$
\sigma _ { X } = { \sqrt { \operatorname { V a r } ( X ) } } .
$$

The variance and standard deviation serve as measures of the spread of the random variable about its expected value. Since the units of $\sigma$ are the same as the units of $\mu$ , the standard deviation is generally more practical for reporting a spread measure. However, the variance has properties that make it more useful for certain calculations.

# B.3. JOINT DISTRIBUTIONS

Definition B.11 If we have two random variables $X$ and $Y$ , they may have a joint probability density function ( JDF), $f ( x , \gamma )$ , with

$$
P ( X \leq a { \mathrm { ~ a n d ~ } } Y \leq b ) = \int _ { - \infty } ^ { a } \intop _ { - \infty } ^ { b } f ( x , \gamma ) \ d \gamma \ d x .
$$

If $X$ and $Y$ have a JDF, then we can use it to evaluate the expected value of a function of $X$ and $Y$ . The expected value of $g ( X , Y )$ is

$$
E [ g ( X , \ Y ) ] = \int _ { - \infty } ^ { \infty } \int \displaylimits _ { - \infty } ^ { \infty } g ( x , \gamma ) f ( x , \gamma ) \ d \gamma \ d x .
$$

Definition B.12 Two random variables $X$ and $Y$ are independent if a JDF exists and is defined by

$$
f ( x , \gamma ) = f _ { X } ( x ) f _ { Y } ( \gamma ) .
$$

Definition B.13 If $X$ and $Y$ have a JDF, then the covariance of $X$ and $Y$ is

$$
\operatorname { C o v } ( X , Y ) = E [ ( X - E [ X ] ) ( Y - E [ Y ] ) ] = E [ X Y ] - E [ X ] E [ Y ] .
$$

If $X$ and $Y$ are independent, then $E [ X Y ] = E [ X ] E [ Y ]$ , and $\operatorname { C o v } ( X , \ Y ) = 0$ . However, if $X$ and $Y$ are dependent, it is still possible, given some particular distributions, for $X$ and $Y$ to have $\operatorname { C o v } ( X , \ Y ) = 0$ . If $\operatorname { C o v } ( X , \ Y ) = 0$ , $X$ and $Y$ are called uncorrelated.

Definition B.14 The correlation of $X$ and $Y$ is

$$
\rho ( X , ~ Y ) = \frac { \operatorname { C o v } ( X , ~ Y ) } { \sqrt { \operatorname { V a r } ( X ) \operatorname { V a r } ( Y ) } } .
$$

Correlation is thus a scaled covariance.

Theorem B.1 The following properties of Var, Cov, and correlation hold for any random variables $X$ and $Y$ and scalars s and a.

1. $V a r ( X ) \geq 0$ .   
2. ${ \cal V } a r ( X + a ) = { \cal V } a r ( X )$ .   
3. ${ \cal { V } } a r ( s X ) = s ^ { 2 } { \cal { V } } a r ( X ) .$   
4. $V a r ( X + Y ) = V a r ( X ) + V a r ( Y ) + 2 C o \nu ( X , Y ) .$   
5. $C o \nu ( X , Y ) = C o \nu ( Y , X )$ .   
6. $\rho ( X , \ Y ) = \rho ( Y , X )$ .   
7. $- 1 \le \rho ( X , ~ Y ) \le 1$ .

The following example demonstrates the use of some of these properties.

# Example B.5

Suppose that $Z$ is a standard normal random variable. Let

$$
X = \mu + \sigma Z .
$$

Then

$$
E [ X ] = E [ \mu ] + \sigma E [ Z ]
$$

so

$$
E [ X ] = \mu .
$$

Also,

$$
\operatorname { V a r } ( X ) = \operatorname { V a r } ( \mu ) + \sigma ^ { 2 } \operatorname { V a r } ( Z ) = \sigma ^ { 2 } .
$$

Thus, if we have a program to generate random numbers with the standard normal distribution, we can use it to generate normal random numbers with any desired expected value and standard deviation. The MATLAB command randn generates independent realizations of an $N ( 0 , 1 )$ random variable.

# Example B.6

What is the CDF (or PDF) of the sum of two independent random variables $X + Y ?$ To see this, we write the desired CDF in terms of an appropriate integral over the JDF, $f ( x , \gamma )$ , which gives (Figure B.7):

$$
\begin{array} { r l } { F _ { X + Y } ( z ) } & { = P ( X + Y \leq z ) } \\ & { = \displaystyle \iint _ { z \in \mathcal { X } _ { r } } f ( x , y ) d x \ d y } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { = \displaystyle \iint \int \int \ f _ { X } ( x ) \hat { f } _ { Y } ( y ) d x \ d y , } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { = \displaystyle \int \displaystyle \int \int _ { z \in \mathcal { X } _ { r } } \int \int \hat { f } ( x ) \hat { f } _ { Y } ( y ) d x \ d y } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { = \displaystyle \iint \displaystyle \int _ { z \in \mathcal { X } _ { r } } \int \hat { f } _ { X } ( x ) \ d x \hat { f } _ { Y } ( y ) \ d y , } \\ & { = \displaystyle \int \displaystyle \int _ { z \in \mathcal { X } _ { r } } \int \hat { f } _ { X } ( x ) \ d x \hat { f } _ { Y } ( y ) \ d y . } \end{array}
$$

$$
= \int _ { - \infty } ^ { \infty } F _ { X } ( z - \gamma ) f _ { Y } ( \gamma ) \ d \gamma .
$$

The associated PDF is

$$
{ \begin{array} { l } { f _ { X + Y } ( z ) = { \cfrac { d } { d z } } \ { \displaystyle \int _ { - \infty } ^ { \infty } } \ F _ { X } ( z - y ) f _ { Y } ( y ) \ d y } \\ { = \int _ { - \infty } ^ { \infty } { \cfrac { d } { d z } } F _ { X } ( z - y ) f _ { Y } ( y ) \ d y } \\ { = \displaystyle \int _ { - \infty } ^ { \infty } f _ { X } ( z - y ) f _ { Y } ( y ) \ d y } \\ { \quad - \infty } \\ { \quad - \infty } \\ { \quad = f _ { X } ( z ) * f _ { Y } ( z ) . } \end{array} }
$$

Adding two independent random variables thus produces a new random variable that has a PDF given by the convolution of the PDFs of the two individual variables.

![](images/7e90df4d3a22255c00ec6c5fe2e391a91e6e240f50fa302f1f6d543e3f61e646.jpg)  
Figure B.7 Integration of a JDF for two independent random variables, $X$ and $Y ,$ to evaluate the CDF of $Z = X + Y$ .

The JDF can be used to evaluate the CDF or PDF arising from a general function of jointly distributed random variables. The process is identical to the previous example except that the specific form of the integral limits is determined by the specific function.

# Example B.7

Consider the product of two independent, identically distributed, standard normal random variables,

$$
Z = X Y ,
$$

with a JDF given by

$$
f ( x , \ \gamma ) = f ( x ) f ( \gamma ) = { \frac { 1 } { 2 \pi \sigma ^ { 2 } } } e ^ { - ( x ^ { 2 } + \gamma ^ { 2 } ) / 2 \sigma ^ { 2 } } .
$$

The CDF of $Z$ is

$$
F ( z ) = P ( Z \leq z ) = P ( X Y \leq z ) .
$$

For $z \le 0$ , this is the integral of the JDF over the exterior of the hyperbolas defined by $x \gamma \leq z \leq 0$ , while for $z \ge 0$ , we integrate over the interior of the complementary hyperbolas $x \gamma \leq z \geq 0$ . At $z = 0$ , the integral covers exactly half of the $( x , \gamma )$ plane (the second and fourth quadrants) and, because of the symmetry of the JDF, has accumulated half of the probability, or $1 / 2$ .

The integral is thus

$$
F ( z ) = 2 \int _ { - \infty } ^ { 0 } \int _ { z / x } ^ { \infty } \frac { 1 } { 2 \pi { \sigma } ^ { 2 } } e ^ { - ( x ^ { 2 } + \gamma ^ { 2 } ) / 2 { \sigma } ^ { 2 } } d \gamma \ d x \ ( z \leq 0 )
$$

and

$$
F ( z ) = 1 / 2 + 2 \intop _ { - \infty } ^ { 0 } \intop _ { 0 } ^ { z / x } \frac { 1 } { 2 \pi \sigma ^ { 2 } } e ^ { - ( x ^ { 2 } + \gamma ^ { 2 } ) / 2 \sigma ^ { 2 } } d \gamma \ d x \ ( z \geq 0 ) .
$$

As in the previous example for the sum of two random variables, the PDF may be obtained from the CDF by differentiating with respect to $z$ .

# B.4. CONDITIONAL PROBABILITY

In some situations we will be interested in the probability of an event happening given that some other event has also happened.

Definition B.15 The conditional probability of $A$ given that $B$ has occurred is given by

$$
P ( A | B ) = { \frac { P ( A \cap B ) } { P ( B ) } } .
$$

Arguments based on conditional probabilities are often very helpful in computing probabilities. The key to such arguments is the law of total probability.

Theorem B.2 Suppose that $B _ { 1 }$ , $B _ { 2 }$ , . . . , $B _ { n }$ are mutually disjoint and exhaustive events. That is, $B _ { i } \cap B _ { j } = \varnothing$ (the empty set) for $i \neq j$ , and

$$
\cup _ { i = 1 } ^ { n } B _ { i } = S .
$$

Then

$$
P ( A ) = \sum _ { i = 1 } ^ { n } P ( A | B _ { i } ) P ( B _ { i } ) .
$$

It is often necessary to reverse the order of conditioning in a conditional probability. Bayes’ theorem provides a way to do this.

# Theorem B.3 Bayes Theorem

$$
P ( B | A ) = \frac { P ( A | B ) P ( B ) } { P ( A ) } .
$$

# Example B.8

A screening test has been developed for a very serious but rare disease. If a person has the disease, then the test will detect the disease with probability $9 9 \%$ . If a person does not have the disease, then the test will give a false-positive detection with probability $1 \%$ . The probability that any individual in the population has the disease is $0 . 0 1 \%$ . Suppose that a randomly selected individual tests positive for the disease. What is the probability that this individual actually has the disease?

Let $A$ be the event “the person tests positive.” Let $B$ be the event “the person has the disease.” We then want to compute $P ( B | A )$ . By Bayes theorem,

$$
P ( B | A ) = \frac { P ( A | B ) P ( B ) } { P ( A ) } .
$$

We have that $P ( A | B )$ is 0.99, and that $P ( B )$ is 0.0001. To compute $P ( A )$ , we apply the law of total probability, considering separately the probability of a diseased individual testing positive and the probability of someone without the disease testing positive:

$$
P ( A ) = 0 . 9 9 \cdot 0 . 0 0 0 1 + 0 . 0 1 \cdot 0 . 9 9 9 9 = 0 . 0 1 0 0 9 8 .
$$

Thus

$$
P ( B | A ) = { \frac { 0 . 9 9 \cdot 0 . 0 0 0 1 } { 0 . 0 1 0 0 9 8 } } = 0 . 0 0 9 8 .
$$

In other words, even after a positive screening test, it is still unlikely that the individual will have the disease. The vast majority of those individuals who test positive will in fact not have the disease.

The concept of conditioning can be extended from simple events to distributions and expected values of random variables. If the distribution of $X$ depends on the value of $Y$ , then we can work with the conditional PDF $f _ { X \mid Y } ( x )$ , the conditional CDF $F _ { X \mid Y } ( a )$ , and the conditional expected value $E [ X | Y ]$ .

In this notation, we can also specify a particular value of $Y$ by using the notation $f _ { X \mid Y = \gamma }$ , $F _ { X \mid Y = \gamma }$ , or $E [ X | Y = \gamma ]$ . In working with conditional distributions and expected values, the following versions of the law of total probability can be very useful.

Theorem B.4 Given two random variables $X$ and $Y$ , with the distribution of $X$ depending on $Y$ , we can compute

$$
P ( X \leq a ) = \int _ { - \infty } ^ { \infty } P ( X \leq a | Y = \gamma ) f _ { Y } ( \gamma ) \ d \gamma
$$

and

$$
E [ X ] = \intop _ { - \infty } ^ { \infty } E [ X | Y = \gamma ] f _ { Y } ( \gamma ) d \gamma .
$$

# Example B.9

Let $U$ be a random variable uniformly distributed on (1, 2). Let $X$ be an exponential random variable with parameter $\lambda = U$ . We will find the expected value of $X$ :

$$
E [ X ] = \intop _ { 1 } ^ { 2 } E [ X | U = u ] f _ { U } ( u ) \ d u .
$$

Since the expected value of an exponential random variable with parameter $\lambda$ is $1 / \lambda$ , and the PDF of a uniform random variable on (1, 2) is $f _ { U } ( u ) = 1$ ,

$$
E [ X ] = \int _ { 1 } ^ { 2 } \frac { 1 } { u } d u = \log 2 .
$$

# B.5. THE MULTIVARIATE NORMAL DISTRIBUTION

Definition B.16 If the random variables $X _ { 1 }$ , . . . , $X _ { n }$ have a multivariate normal distribution (MVN), then the JDF is

$$
f ( { \bf x } ) = \frac { 1 } { ( 2 \pi ) ^ { n / 2 } } \frac { 1 } { \sqrt { \operatorname* { d e t } ( { \bf C } ) } } e ^ { - ( { \bf x } - { \boldsymbol \mu } ) ^ { T } { \bf C } ^ { - 1 } ( { \bf x } - { \boldsymbol \mu } ) / 2 }
$$

where $\mathbf { x } = [ X _ { 1 } , X _ { 2 } , . ~ . ~ . ~ , X _ { n } ] ^ { T }$ and $\mathbfcal \mu = [ \mu _ { 1 } , \mu _ { 2 } , \dots \dots , \mu _ { n } ] ^ { T }$ is a vector containing the expected values along each of the coordinate directions of $X _ { 1 }$ , . . . , $X _ { n }$ , and $\mathbf { C }$ contains the covariances between the random variables,

$$
C _ { i , j } = \operatorname { C o v } ( X _ { i } , X _ { j } ) .
$$

Note that if $\mathbf { C }$ is singular, then the JDF involves a division by zero, and is simply not defined.

The vector $\mu$ and the covariance matrix $\mathbf { C }$ completely characterize the MVN distribution. There are other multivariate distributions that are not completely characterized by the expected values and covariance matrix.

Theorem B.5 Let $\mathbf { x }$ be a multivariate normal random vector with expected values defined by the vector $\mu$ and covariance matrix $\mathbf { C }$ , and let $\mathbf { Y } = \mathbf { A } \mathbf { X }$ . Then $\mathbf { Y }$ is also multivariate normal, with

$$
E [ \mathbf { Y } ] = \mathbf { A } \mu
$$

and

$$
\mathbf { C o v } ( \mathbf { Y } ) = \mathbf { A C A } ^ { T } .
$$

Theorem B.6 If we have an $n$ -dimensional MVN distribution $\mathbf { x }$ with covariance matrix C and expected value $\mu$ , and the covariance matrix is of full rank, then the quantity

$$
Z = ( \mathbf { X } - { \boldsymbol { \mu } } ) ^ { T } \mathbf { C } ^ { - 1 } ( \mathbf { X } - { \boldsymbol { \mu } } )
$$

has a $\chi ^ { 2 }$ distribution with $n$ degrees of freedom.

# Example B.10

We can generate vectors that are realizations of an MVN distribution with a known mean, $\mu$ , and covariance matrix, $\mathbf { C }$ , as follows.

1. Find the lower-triangular Cholesky factorization ${ \mathbf { C } } = { \mathbf { L } } { \mathbf { L } } ^ { T }$ .   
2. Let $\mathbf { z }$ be a vector of $n$ independent $N ( 0 , 1 )$ random numbers.   
3. Let $\mathbf { X } = \mu + \mathbf { L } \mathbf { Z }$ .

We can easily show that this procedure produces the desired distribution. Because $E [ \mathbf { Z } ] = \mathbf { 0 }$ , $E [ \mathbf { X } ] = \mu + \mathbf { L 0 } = \mu$ . Also, since $\mathrm { C o v } ( \mathbf { Z } ) = \mathbf { I }$ and $\mathrm { C o v } ( \mu ) = { \bf 0 }$ , $\operatorname { C o v } ( \mathbf { X } ) =$ $\operatorname { C o v } ( \mu + \mathbf { L } \mathbf { Z } ) = \operatorname { C o v } ( \mathbf { L } \mathbf { Z } ) = \mathbf { L } \mathbf { I } \mathbf { L } ^ { T } = \mathbf { C }$ using (B.64).

# B.6. THE CENTRAL LIMIT THEOREM

Theorem B.7 Let $X _ { 1 }$ , $X _ { 2 }$ , . . . , $X _ { n }$ be independent and identically distributed (IID) random variables with a finite expected value $\mu$ and variance $\sigma ^ { 2 }$ . Let

$$
Z _ { n } = { \frac { X _ { 1 } + X _ { 2 } + \cdot \cdot \cdot + X _ { n } - n \mu } { \sqrt { n } \sigma } } .
$$

In the limit as n approaches infinity, the distribution of $Z _ { n }$ approaches the standard normal distribution.

The central limit theorem shows why quasi-normally distributed random variables appear so frequently in nature; the sum of numerous independent random variables produces an approximately normal random variable, regardless of the distribution of the underlying IID variables. In particular, this is one reason that measurement errors are often normally distributed. As we will see in Chapter 2, having normally distributed measurement errors leads us to consider least squares solutions to parameter estimation and inverse problems.

# B.7. TESTING FOR NORMALITY

Many of the statistical procedures that we will use assume that data are normally distributed. Fortunately, the statistical techniques that we describe are generally robust in the face of small deviations from normality. Large deviations from the normal distribution can cause problems. Thus, it is important to be able to examine a data set to see whether the distribution is approximately normal.

Plotting a histogram of the data provides a quick view of the distribution. The histogram should show a roughly “bell-shaped” distribution, symmetrical around a single peak. If the histogram shows that the distribution is obviously skewed, then it would be unwise to assume that the data are normally distributed.

The Q-Q plot provides a more precise graphical test of whether a set of data could have come from a particular distribution. The data points,

$$
\mathbf { d } = [ d _ { 1 } , \ d _ { 2 } , \ . \ . \ . \ , \ d _ { n } ] ^ { T } ,
$$

are first sorted in numerical order from smallest to largest into a vector $\mathbf { y }$ , which is plotted versus

$$
x _ { i } = F ^ { - 1 } ( ( i - 0 . 5 ) / n ) \quad ( i = 1 , 2 , \dots , n ) ,
$$

where $F ( x )$ is the CDF of the distribution against which we wish to compare our observations.

If we are testing to see if the elements of $\mathbf { d }$ could have come from the normal distribution, then $F ( x )$ is the CDF for the standard normal distribution:

$$
F _ { N } ( x ) = { \frac { 1 } { \sqrt { 2 \pi } } } \int _ { - \infty } ^ { x } e ^ { - { \frac { 1 } { 2 } } z ^ { 2 } } d z .
$$

If the elements of $\mathbf { d }$ are normally distributed, the $Q \mathrm { - } Q$ plot points $( \gamma _ { i } , x _ { i } )$ will follow a straight line with a slope and intercept determined by the standard deviation and expected value, respectively, of the normal distribution that produced the data.

# Example B.11

Figure B.8 shows the histogram from a set of 1000 data points. The characteristic bell-shaped curve in the histogram might make it appear at first that these data are normally distributed. The sample mean is $- 0 . 0 1$ and the sample standard deviation is 1.41.

Figure B.9 shows the Q-Q plot for these data, which makes it apparent that the data set contains substantially more extreme values than the normal distribution would predict. In fact, these data were generated according to a $t$ distribution with 5 degrees of freedom, that has broader tails than the normal distribution (Figure B.3).

![](images/fd86d31db7361d09cd9d7d50006184aaa101c4a142cbb9730f94b6312afddb37.jpg)  
Figure B.8 Histogram of a sample data set.

![](images/42e2383be4f18cc778e4ce1a49ce49a41ed7f7b30541839ad73e96abe62be110.jpg)  
Figure B.9 Q-Q plot for the sample data set.

There are a number of statistical tests for normality. These include the Kolmogorov-Smirnov test, Anderson-Darling test, and Lilliefors test. Each produces probabilistic measures called $\pmb { p }$ -values. A small $p$ -value indicates that the observed data would be unlikely if the distribution were in fact normal, while a larger $p .$ -value is consistent with normality.

# B.8. ESTIMATING MEANS AND CONFIDENCE INTERVALS

Given a collection of $n$ noisy measurements $m _ { 1 }$ , $m _ { 2 }$ , . . . , $m _ { n }$ of some quantity of interest, how can we estimate the true value $m$ , and how uncertain is this estimate? This is a classic problem in statistics.

We will assume first that the measurement errors are independent and normally distributed with expected value 0 and some unknown standard deviation $\sigma$ . Equivalently, the measurements themselves are normally distributed with expected value $m$ and standard deviation $\sigma$ .

We begin by computing the measurement average,

$$
{ \bar { m } } = { \frac { m _ { 1 } + m _ { 2 } + \cdot \cdot \cdot + m _ { n } } { n } } .
$$

This sample mean $\bar { m }$ will serve as our estimate of $m$ . We will also compute an estimate $s$ of the standard deviation

$$
s = \sqrt { \frac { \sum _ { i = 1 } ^ { n } ( m _ { i } - \bar { m } ) ^ { 2 } } { n - 1 } } .
$$

The key to our approach to estimating $m$ is the following theorem.

Theorem B.8 (The Sampling Theorem) Under the assumption that measurements are independent and normally distributed with expected value m and standard deviation $\sigma$ , the random quantity

$$
t = \frac { m - \bar { m } } { s / \sqrt { n } }
$$

has a Student’s t distribution with $n - 1$ degrees of freedom.

If we had the true standard deviation $\sigma$ instead of the estimate $s$ , then $t$ would in fact be normally distributed with expected value 0 and standard deviation 1. This does not quite work out because we have used an estimate $s$ of the standard deviation. For smaller values of $n$ , the estimate $s$ is less accurate, and the $t$ distribution therefore has fatter tails than the standard normal distribution. As $n$ becomes large, $s$ becomes a better estimate of $\sigma$ and it can be shown that the $t$ distribution converges to a standard normal distribution [47].

Let $t _ { n - 1 , 0 . 9 7 5 }$ be the $9 7 . 5 \%$ -tile of the $t$ distribution and let $t _ { n - 1 , 0 . 0 2 5 }$ be the $2 . 5 \% \AA$ -tile of the $t$ distribution. Then

$$
P \bigg ( t _ { n - 1 , 0 . 0 2 5 } \leq \frac { m - \bar { m } } { s / \sqrt { n } } \leq t _ { n - 1 , 0 . 9 7 5 } \bigg ) = 0 . 9 5 .
$$

This can be rewritten as

$$
P \big ( \big ( t _ { n - 1 , 0 . 0 2 5 } s / \sqrt { n } \big ) \leq ( m - \bar { m } ) \leq \big ( t _ { n - 1 , 0 . 9 7 5 } s / \sqrt { n } \big ) \big ) = 0 . 9 5 .
$$

We can construct the√ $9 5 \%$ confidence interval for √ $m$ as the interval from $\bar { m } +$ $t _ { n - 1 , 0 . 0 2 5 } s / \sqrt { n }$ to $\bar { m } + t _ { n - 1 , 0 . 9 7 5 } s / \sqrt { n }$ . Because the $t$ distribution is symmetric, this can√ also be written as $\bar { m } - t _ { n - 1 , 0 . 9 7 5 } s / \sqrt { n }$ to $\bar { m } + t _ { n - 1 , 0 . 9 7 5 } s / \sqrt { n }$ .

As we have seen, there is a $9 5 \%$ probability that when we construct the confidence interval, that interval will contain the true mean, m. Note that we have not said that, given a particular set of data and the resulting confidence interval, there is a $9 5 \%$ probability that $m$ is in the confidence interval. The semantic difficulty here is that $m$ is not a random variable, but is rather some true fixed quantity that we are estimating; the measurements $m _ { 1 } , m _ { 2 } , \ldots . m _ { n }$ , and the calculated m¯ , s, and confidence interval are the random quantities.

# Example B.12

Suppose that we want to estimate the mass of an object and obtain the following ten measurements of the mass (in grams):

$$
\begin{array} { r r r r r } { 9 . 9 8 } & { { } 1 0 . 0 7 } & { 9 . 9 4 } & { { } 1 0 . 2 2 } & { 9 . 9 8 } \\ { 1 0 . 0 1 } & { { } 1 0 . 1 1 } & { { } 1 0 . 0 1 } & { 9 . 9 9 } & { { } 9 . 9 2 } \end{array}
$$

The sample mean is $\bar { m } = 1 0 . 0 2 ~ \mathrm { g }$ . The sample standard deviation is $s = 0 . 0 8 8 3$ grams. The $9 7 . 5 \%$ -tile of the $t$ distribution with $n - 1 = 9$ degrees of freedom is (from a $t \cdot$ -table or function) 2.262. Thus our $9 5 \%$ confidence interval for the mean is

$$
\left[ \bar { m } - 2 . 2 6 2 s / \sqrt { n } , \bar { m } + 2 . 2 6 2 s / \sqrt { n } \right] \mathrm { g } .
$$

Substituting the values for ${ \bar { m } } , s ,$ , and $n$ , we get an interval of

$$
\left[ 1 0 . 0 2 - 2 . 2 6 2 \cdot 0 . 0 8 8 3 / \sqrt { 1 0 } , 1 0 . 0 2 + 2 . 2 6 2 \cdot 0 . 0 8 8 3 / \sqrt { 1 0 } \right] \mathrm { g }
$$

or

The above procedure for constructing a confidence interval for the mean using the $t$ distribution was based on the assumption that the measurements were normally distributed. In situations where the data are not normally distributed, this procedure can fail in a very dramatic fashion (Exercise B.9). However, it may be safe to generate an approximate confidence interval using this procedure if (1) the number $n$ of data is large (50 or more) or (2) the distribution of the data is not strongly skewed and $n$ is at least 15.

# B.9. HYPOTHESIS TESTS

In some situations we want to test whether a set of normally distributed data could reasonably have come from a normal distribution with expected value $\mu _ { 0 }$ . Applying the sampling theorem, we see that if our data did come from a normal distribution with expected value $\mu _ { 0 }$ , then there would be a $9 5 \%$ probability that

$$
t _ { \mathrm { o b s } } = \frac { \mu _ { \mathrm { 0 } } - \bar { m } } { s / \sqrt { n } }
$$

would lie in the interval

$$
[ F _ { t } ^ { - 1 } ( 0 . 0 2 5 ) , F _ { t } ^ { - 1 } ( 0 . 9 7 5 ) ] = [ t _ { n - 1 , 0 . 0 2 5 } , t _ { n - 1 , 0 . 9 7 5 } ] ,
$$

and only a $5 \%$ probability that $t$ would lie outside this interval. Equivalently, there is only a $5 \%$ probability that $| t _ { \mathrm { o b s } } | \geq t _ { n - 1 , 0 . 9 7 5 }$ .

This leads to the $\scriptstyle { \mathbf { \alpha } } _ { t } .$ -test: If $| t _ { \mathrm { o b s } } | \geq t _ { n - 1 , 0 . 9 7 5 }$ , then we reject the hypothesis that $\mu = \mu _ { 0 }$ . On the other hand, if $| t _ { \mathrm { o b s } } | < t _ { n - 1 , 0 . 9 7 5 }$ , then we cannot reject the hypothesis that $\mu = \mu _ { 0 }$ . Although the $9 5 \%$ confidence level is traditional, we can also perform the $t \cdot$ -test at a $9 9 \%$ or some other confidence level. In general, if we want a confidence level of 1 − α, then we compare |tobs| to tn−1,1−α/2.

In addition to reporting whether or not a set of data passes a $t \cdot$ -test, it is good practice to report the associated $t \cdot$ -test $p$ -value. The $p$ -value associated with a $t \cdot$ -test is the largest value of $\alpha$ for which the data passes the $t \cdot$ -test. Equivalently, it is the probability that we could have gotten a greater $t$ value than we have observed, given that all of our assumptions are correct.

# Example B.13

Consider the following data:

These appear to be roughly normally distributed, with a mean that seems to be larger than 0. We will test the hypothesis $\mu = 0$ . The $t$ statistic is

$$
t _ { \mathrm { o b s } } = \frac { \mu _ { \mathrm { 0 } } - \bar { m } } { s / \sqrt { n } } ,
$$

which, for this data set, is

$$
t _ { \mathrm { o b s } } = { \frac { 0 - 1 . 0 2 5 3 } { 1 . 1 8 9 5 / { \sqrt { 1 0 } } } } \approx - 2 . 7 2 5 .
$$

Because $| t _ { \mathrm { o b s } } |$ is larger than $t 9 , 0 . 9 7 5 = 2 . 2 6 2$ , we reject the hypothesis that these data came from a normal distribution with expected value 0 at the $9 5 \%$ confidence level.

The $t \cdot$ -test (or any other statistical test) can fail in two ways. First, it could be that the hypothesis that $\mu = \mu _ { 0 }$ is true, but our particular data set contained some unlikely values and failed the $t \cdot$ -test. Rejecting the hypothesis when it is in fact true is called a type I error. We can control the probability of a type I error by decreasing $\alpha$ .

The second way in which the $t \cdot$ -test can fail is more difficult to control. It could be that the hypothesis $\mu = \mu _ { 0 }$ was false, but the sample mean was close enough to $\mu _ { 0 }$ to pass the $t \cdot$ -test. In this case, we have a type $\mathbf { I I }$ error. The probability of a type II error depends very much on how close the true mean is to $\mu _ { \mathrm { 0 } }$ . If the true mean $\mu = \mu _ { 1 }$ is very close to $\mu _ { 0 }$ , then a type II error is quite likely. If the true mean $\mu = \mu _ { 1 }$ is very far from $\mu _ { 0 }$ , then a type II error will be less likely. Given a particular alternative hypothesis, $\mu = \mu _ { 1 }$ , we call the probability of a type $\mathrm { I I }$ error $\beta ( \mu _ { 1 } )$ , and call the probability of not making a type II error $( 1 - \beta ( \mu _ { 1 } ) )$ the power of the test. We can estimate $\beta ( \mu _ { 1 } )$ by repeatedly generating sets of $n$ random numbers with $\mu = \mu _ { 1 }$ and performing the hypothesis test on the sets of random numbers (Exercise B.10).

The results of a hypothesis test should always be reported with care. It is important to discuss and justify any assumptions (such as the normality assumption made in the $t \cdot$ -test) underlying the test. The $p$ -value should always be reported along with whether the hypothesis was rejected. If the hypothesis was not rejected and some particular alternative hypothesis is available, it is good practice to estimate the power of the hypothesis test against this alternative hypothesis. Confidence intervals for the mean should be reported along with the results of a hypothesis test.

It is important to distinguish between the statistical significance of a hypothesis test and the actual magnitude of any difference between the observed mean and the hypothesized mean. For example, with very large $n$ it is nearly always possible to achieve statistical significance at the $9 5 \%$ confidence level, even though the observed mean may differ from the hypothesis by only $1 \%$ or less.

# B.10. EXERCISES

1. Compute the expected value and variance of a uniform random variable in terms of the parameters $a$ and $b$ .

2. Compute the CDF of an exponential random variable with parameter $\lambda$ . You may find the MATLAB library function exprand.m to be useful here.

3. Show that

$$
\operatorname { C o v } ( a X , Y ) = a \operatorname { C o v } ( X , Y )
$$

and that

$$
\operatorname { C o v } ( X + Y , Z ) = \operatorname { C o v } ( X , Z ) + \operatorname { C o v } ( Y , Z ) .
$$

4. Show that the PDF for the sum of two independent uniform random variables on [a $\iota , b ] = [ 0 , 1 ]$ is

$$
f ( x ) = \left\{ \begin{array} { l l } { 0 \quad ( x \leq 0 ) } \\ { x \quad ( 0 \leq x \leq 1 ) } \\ { 2 - x \quad ( 1 \leq x \leq 2 ) } \\ { 0 \quad ( x \geq 2 ) . } \end{array} \right.
$$

5. Suppose that $X$ and $Y$ are independent random variables. Use conditioning to find a formula for the CDF of $X + Y$ in terms of the PDFs and CDFs of $X$ and $Y$ .

6. Suppose that ${ \bf x } = ( X _ { 1 } , X _ { 2 } ) ^ { T }$ is a vector composed of two random variables with a multivariate normal distribution with expected value $\mu$ and covariance matrix $\mathbf { C }$ , and that A is a 2 by 2 matrix. Use properties of expected value and covariance to show that $\mathbf { y } = \mathbf { A } \mathbf { x }$ has expected value $\mathbf { A } \mu$ and covariance $\mathbf { A } \mathbf { C } \mathbf { A } ^ { T }$ .

7. Suppose that $\mathbf { x }$ is a multivariate normal random variable with mean vector $\mu$ and covariance matrix $\mathbf { C }$ . Use Theorem B.5 to show that the ith component of $\mathbf { x }$ , $\mathbf { x } _ { i }$ , is normally distributed with mean $\mu _ { i }$ and variance $\mathbf { C } _ { i , i }$ . Hint: Let $\mathbf { A } = \mathbf { e } _ { i } ^ { T }$ , where $\mathbf { e } _ { i }$ is the ith column of the identity matrix.

8. Consider the following data, which we will assume are drawn from a normal distribution.

$$
\begin{array} { r r r r } { - 0 . 4 3 2 6 } & { { } - 1 . 6 6 5 6 } & { 0 . 1 2 5 3 } & { 0 . 2 8 7 7 } & { { } - 1 . 1 4 6 5 } \\ { 1 . 1 9 0 9 } & { { } 1 . 1 8 9 2 } & { - 0 . 0 3 7 6 } & { { } 0 . 3 2 7 3 } & { 0 . 1 7 4 6 } \end{array}
$$

Find the sample mean and standard deviation. Use these to construct a $9 5 \%$ confidence interval for the mean. Test the hypothesis $H _ { 0 } : \mu = 0$ at the $9 5 \%$ confidence level. What do you conclude? What was the corresponding $p$ -value?

9. Using MATLAB, repeat the following experiment 1000 times. Generate five exponentially distributed random numbers from the exponential probability density function (B.10) with means $\mu = 1 / \lambda = 1 0$ . You may find the library function exprand to be useful here. Use (B.74) to calculate a $9 5 \%$ confidence interval for the 1000 mean determinations. How many times out of the 1000 experiments did the $9 5 \%$ confidence interval cover the expected value of 10? What happens if you instead generate 50 exponentially distributed random numbers at a time? Discuss your results.

10. Using MATLAB, repeat the following experiment 1000 times. Use the randn function to generate a set of 10 normally distributed random numbers with expected value 10.5 and standard deviation 1. Perform a $t \cdot$ -test of the hypothesis $\mu = 1 0$ at the $9 5 \%$ confidence level. How many type II errors were committed? What is the approximate power of the $t \cdot$ -test with $n = 1 0$ against the alternative hypothesis $\mu = 1 0 . 5 ?$ Discuss your results.

11. Using MATLAB, repeat the following experiment 1000 times. Generate five exponentially distributed random numbers with expected value 10. You may find the library function exprand to be useful here. Take the average of the five random numbers. Plot a histogram and a $Q \mathrm { - } Q$ plot of the 1000 averages that you computed. Are the averages approximately normally distributed? Explain why or why not. What would you expect to happen if you took averages of 50 exponentially distributed random numbers at a time? Try it and discuss the results.

# B.11. NOTES AND FURTHER READING

Most of the material in this Appendix can be found in virtually any introductory textbook in probability and statistics. Some recent textbooks include [4, 29]. The multivariate normal distribution is a somewhat more advanced topic that is often ignored in introductory courses. Searle [139] has a good discussion of the multivariate normal distribution and its properties. Numerical methods for probability and statistics are a specialized topic. Two standard references include [89, 157].

# Review of Vector Calculus

# Synopsis

A review of key vector calculus topics, including the gradient, Hessian, Jacobian, Taylor’s theorem, and Lagrange multipliers.

# C.1. THE GRADIENT, HESSIAN, AND JACOBIAN

In vector calculus, the familiar first and second derivatives of a single-variable function are generalized to operate on vectors.

Definition C.1 Given a scalar-valued function with a vector argument, $f ( \mathbf { x } )$ , the gradient of $f$ is

$$
\begin{array} { r } { \nabla f ( \mathbf { x } ) = \left[ \begin{array} { c } { \frac { \partial f } { \partial x _ { 1 } } } \\ { \frac { \partial f } { \partial x _ { 2 } } } \\ { \vdots } \\ { \frac { \partial f } { \partial x _ { n } } } \end{array} \right] . } \end{array}
$$

The vector $\nabla f ( \mathbf { x } )$ has an important geometric interpretation in that it points in the direction in which $f ( \mathbf { x } )$ increases most rapidly at the point $\mathbf { x }$ .

Recall from single-variable calculus that if a function $f$ is continuously differentiable, then a point $x ^ { * }$ can only be a minimum or maximum point of $f$ if $\stackrel { \cdot } { f } ^ { \prime } ( x ) | _ { x = x ^ { * } } = 0$ . Similarly in vector calculus, if $f ( \mathbf { x } )$ is continuously differentiable, then a point $\mathbf { x } ^ { * }$ can only be a minimum or maximum point if $\nabla f ( \mathbf { x } ^ { * } ) = \mathbf { 0 }$ . In more than one dimension, a point $\mathbf { x } ^ { * }$ where $\nabla f ( \mathbf { x } ^ { * } ) = \mathbf { 0 }$ can also be a saddle point. Any point where $\nabla f ( \mathbf { x } ^ { * } ) = \mathbf { 0 }$ is called a critical point.