estimator can then be better than this one for $\theta _ { 0 }$ , so there is no estimator that is preferable to all the others in the sense of the above partial ordering.

The problem is that we were trying to compare a candidate optimal estimator with a class containing all the others and for all $\theta$ . This class is much too big and the problem is too general to hope to find an estimator that stands out above all the rest. If we are to have any chance of finding optimal estimators, we must be less ambitious and restrict the class of estimators. To do this, there are three conventional methods which, for a given problem, supply objective reasons for preferring one estimator in a class which nevertheless remains extremely large.

Principle of Impartiality

The problem with the trivial estimator is that it favours the value $\theta _ { 0 }$ to the detriment of all the others, whence the idea of seeking estimators in a class that does not possess this shortcoming. The most conventional way is to restrict the search for the best estimator to the class of unbiased estimators and impose $\operatorname { E } { \big \{ } \delta ( X ) { \big \} } ~ =$ $\tau ( \theta )$ D. Comparing estimators in the sense of risk then amounts to comparing their variances. Effectively, it can be shown that, in this class, optimal estimators can be found. These are called uniform minimum variance unbiased (UMVU) estimators, with the understanding that the loss function is the quadratic function.

Bayes’ Principle

Another, less ambitious approach is to abandon any hope of minimising the risk uniformly, i.e., for all $\theta$ , and to seek the estimator which minimises a risk calculated on average over all $\theta$ . For this average to have any meaning, it must be calculated using a weighting function $\pi ( \theta )$ . We then calculate the average risk or Bayes risk $R _ { \pi }$ from

$$
R _ { \pi } ( \delta ) = \int _ { \theta } R { \big ( } \tau ( \theta ) , \delta { \big ) } \pi ( \theta ) \mathrm { d } \theta .
$$

In the Bayesian interpretation of this average, $\theta$ is a random variable with a priori probability density $\pi ( \theta )$ . A Bayes estimator is one that minimises the Bayes risk.

When taken in this way, the above notion is not controversial, but some practitioners criticise it when it is not conceivable for $\theta$ to be a random variable. They then reject the idea accepted by the Bayesian school and interpret $\pi ( \theta )$ as a measure of the subjective confidence level attributed to the possible values of $\theta$ . In any case, the Bayesian approach has the advantage that it gives a framework within which it becomes possible on the basis of acquired experience to refine the a priori density $\pi ( \theta )$ by replacing it by the a posteriori density $\psi ( \theta | X )$ . Indeed, according to the Bayes relation,

$$
\psi ( \theta | X ) = \frac { l ( X | \theta ) \pi ( \theta ) } { \int _ { \theta } l ( X | \theta ) \pi ( \theta ) } .
$$

In this expression, $l ( X \vert \theta )$ is the likelihood function, i.e., the probability density for observing $X$ , knowing $\theta$ j. The function $\psi$ is then taken as an improvement on $\pi$ in view of the experimental results $X$ .

Minimax Principle

According to this principle, the overall performance of an estimator is accounted for by noting the maximum of its attached risk, and this maximum risk is then minimised. Hence, an estimator $\delta ^ { * }$ will be a minimax estimator if

$$
\operatorname* { m a x } _ { \theta } R \big ( \tau ( \theta ) , \delta ^ { * } \big ) = \operatorname* { m i n } _ { \delta } \operatorname* { m a x } _ { \theta } R \big ( \tau ( \theta , \delta ) \big ) .
$$

The minimax risk $R _ { \mathrm { m } }$ is defined as

$$
R _ { \mathrm { m } } ( \delta ) = \operatorname* { m a x } _ { \theta } R \big ( \tau ( \theta , \delta ) \big ) .
$$

It can be shown that the minimax risk is always greater than or equal to the risk of an arbitrary Bayes estimator. If $\theta$ has finite domain of definition, it can be shown that the minimax estimator corresponds to the Bayes estimator of the most unfavourable a priori density $\pi$ . The minimax principle turns out to be a precautionary principle, which may even be qualified as pessimistic.

There are other principles leading to interesting estimators. An example is provided by non-deterministic estimates in which the same sample does not necessarily lead to the same estimate.

# 9.5.4 Properties of Estimators

The ideas discussed above suggest a more careful investigation of the properties that should be satisfied by good estimators. It is convenient to begin with convergence, which is a property that all estimators should possess, whether they are UMVU, Bayesian, or something else. The next issue is the bias and variance of estimators, and the methods available for reducing them. Finally, we discuss a fundamental result in the class of unbiased estimators, namely the non-zero lower bound of their variance.

# Convergence

Definition. A sequence of estimators $\{ { \widehat { \theta } } \}$ or, more concisely, an estimator ${ \widehat { \theta } } _ { n }$ , is f gconvergent when it converges in probability to the value it claims to estimate. According to this definition, an estimator is convergent if

$$
\forall \epsilon > 0 , \qquad \operatorname* { l i m } _ { n  \infty } \operatorname* { P r } \Bigl \{ | \hat { \theta } _ { n } - \theta | \ge \epsilon \Bigr \} = 0 .
$$

This convergence is expressed by writing ${ \widehat { \theta } } _ { n } \ { \xrightarrow { \operatorname* { P r } } } \ \theta$ .

The notion of convergence in probability is used to state the law of large numbers, which stipulates that the arithmetic mean $M$ of $n$ independent realisations $( X _ { 1 } , \ldots , X _ { n } )$ of the same random variable $X$ is a convergent estimator of its average $\mu$ (provided it exists):

$$
M = { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } X _ { i } \ { \stackrel { \mathrm { P r } } { \to } } \ \mu .
$$

This result, first discovered at the beginning of the seventeenth century, was the point of departure for probability theory in the field of experiment.

# Unbiasedness

Definition. An estimator ${ \widehat { \theta } } _ { n }$ for $\theta$ or $T _ { n }$ for $\tau ( \theta )$ is said to be unbiased if

$$
\mathbb { E } \big \{ \widehat { \theta } _ { n } \big \} = \theta \quad \mathrm { o r } \quad \mathbb { E } \big \{ T _ { n } \big \} = \tau ( \theta ) ,
$$

for all possible values of $\theta$ . If the bias is defined to be the quantity ${ \mathrm { E } } \{ { \widehat { \theta } } _ { n } \} - \theta$ , an unbiased estimator is one with zero bias.

Example. The arithmetic mean

$$
M = { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } X _ { i }
$$

is an unbiased estimator of the average $\mu$ and of the variance $\sigma ^ { 2 }$ of the parent population (provided it exists):

$$
\operatorname { E } \{ M \} = \mu .
$$

This is a simple consequence of the linearity of mathematical expectation.

The notion of bias, introduced by Gauss in 1821, corresponds to the idea of systematic error as used by physicists. Apart from the theoretical considerations discussed above, it seems reasonable to regard it as a good property if the average of the estimator is equal to the parameter that it is supposed to estimate. However, it is not necessarily a good idea to insist on dealing only with unbiased estimators, if only because there are cases where no such estimator actually exists. The following counterexample is a classic.

Example of a Situation with No Unbiased Estimator. Let $K$ be a random variable distributed according to the binomial distribution $\mathcal { B } ( n , p )$ . The number of trials $n$ is given, but the probability $p$ of success in a given trial is unknown. However, it is not $p$ that we are trying to estimate, but rather $\tau ( p ) = 1 / p$ . Let $t ( k )$ by the values taken by the estimator $T$ for $1 / p$ when we observe $k$ Dsuccesses in $n$ trials. By definition, for $T$ to be unbiased, we must have

$$
\sum _ { k = 0 } ^ { n } t ( k ) C _ { n } ^ { k } p ^ { k } ( 1 - p ) ^ { n - k } = \frac { 1 } { p } \quad \mathrm { f o r } \quad 0 < p \leq 1 .
$$

Suppose now that for a certain $p$ , the estimator $T$ is unbiased. Then the sum on the left is finite, which implies in particular that $t ( 0 )$ is finite. Now when $p  0$ , the term on the left tends to $t ( 0 )$ , whereas the term $1 / p$ !on the right can be as large as we like. Hence, $T$ cannot be unbiased for all $p$ .

This is not such an artificial example. It corresponds to the so-called capture–recapture method, which aims to estimate an animal population. Let $N$ be the population of animal species, e.g., fish in a lake. To estimate $N$ , we capture $m$ animals which are then tagged and released. After tagging, the probability of recapturing an animal is $p = m / N$ , and estimating the population $N = m / p$ amounts to estimating $1 / p$ .

In fact, to estimate $1 / p$ in an unbiased way, the animals must be recaptured up to the point where the number of tagged individuals is equal to a prechosen number $r$ . If $r + Y$ is the total number of animals that must be recaptured in order to obtain $r$ Ctagged animals, it can be shown that $( r + Y ) / r$ is the best unbiased estimator for $1 / p .$ . In this procedure, it is assumed either that $N$ Cis very large or that animals are recaptured and released immediately (drawing with replacement).

Asymptotically Unbiased Estimators

When defining asymptotic properties, it is essential to specify the order of operations when taking the limit. In the case that concerns us here, will a sequence of estimators ${ \widehat { \theta } } _ { n }$ be declared asymptotically unbiased if the limit of the expectation tends to zero, or if the expectation of the limit tends to zero? There are thus two possible definitions.

Definition: Limit of Expectation. A sequence of estimators $\{ { \widehat { \theta } } \}$ for $\theta$ will be called asymptotically unbiased if the sequence of expectations of ${ \widehat { \theta } } _ { n }$ tends to $\theta$ , i.e., if

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname { E } \{ { \widehat { \theta } } _ { n } \} = \theta .
$$

No particular comment is needed here, because this is just a sequence of scalars.

Definition: Expectation of the Limit. A sequence of estimators $\{ { \widehat { \theta } } \}$ for $\theta$ will be called asymptotically unbiased if the sequence of differences ${ \widehat { \theta } } _ { n } - \theta$ , suitably

normalised, tends in probability to a random variable of zero expectation, i.e., if there is a sequence $k _ { n }$ such that

$$
\begin{array} { r } { k _ { n } ( \widehat { \theta } _ { n } - \theta ) \xrightarrow { \mathrm { D i s t } } Y \quad \mathrm { a n d } \quad \mathrm { E } \{ Y \} = 0 . } \end{array}
$$

The normalisation constant $k _ { n }$ is often proportional to $\sqrt { n }$ , as for the central limit theorem. Convergence in distribution means that, at the limit, the two random variables obey the same distribution function, except perhaps on a set of zero measure.

An estimator can be asymptotically unbiased according to one definition and not for the other. In practice, the first definition, i.e., the limit of expectations, is assumed.

# Convergence and Absence of Bias

Convergence refers to the distribution function while absence of bias refers to the first order moment of this function. There is no particular reason for the properties of convergence and absence of bias to be related. They are independent notions. In addition, a convergent estimator is not necessarily asymptotically unbiased by either definition of the absence of asymptotic bias. The following example shows this for the limit of expectations definition. (For the expectation of the limit definition, it is easy to find a counterexample in which the limiting distribution has no average, e.g., the Cauchy distribution.)

Example. Let $\{ { \widehat { \theta } } \}$ be a sequence of estimators for zero, where the estimator ${ \widehat { \theta } } _ { n }$ is a bdiscrete random variable equal to 0 with probability $1 - 1 / n$ and $n ^ { 2 }$ bwith probability $1 / n$ . The sequence of estimators is obviously convergent since the probability associated with the point which is not at zero tends to 0 as $1 / n$ when $n  \infty$ . !However, it is biased, and its bias does not tend to zero, but rather to infinity:

$$
{ \mathrm { E } } \big \{ \widehat { \theta } _ { n } \big \} = 0 ( 1 - 1 / n ) + n ^ { 2 } / n = n .
$$

# Reduction of Bias

Unbiased estimators are of great theoretical importance since they define a class where optimal estimators can exist, but they have another advantage outside this class. If we attempt to apply the law of large numbers by taking the arithmetic mean of a set of biased estimators, we will converge toward the average of the underlying distribution, but this will not be the parameter we hoped to estimate. It will entail an error equal to the bias. This is the whole point about trying to correct any bias, or at least trying to reduce it.

Note, however, that, if we try to reduce the bias using the methods presented below when there is no unbiased estimator, we may reduce the bias of the estimator, but we will increase its variance in such a way that its mean squared error will end up being large.

When the Bias is Easy to Calculate

In certain situations, a simple calculation can correct a bias. This happens when estimating the variance of a population we shall use here as an example. Suppose we have an independent sample $( X _ { 1 } , \ldots , X _ { n } )$ for a distribution with average $\mu$ and variance $\sigma ^ { 2 }$ . The parameter to be estimated is $\sigma ^ { 2 }$ , e.g., a noise power. There are two possible cases: either the average $\mu$ is known or it is not.

If the population average is known, it can be shown that the estimator

$$
S ^ { \prime 2 } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( X _ { i } - \mu ) ^ { 2 } ,
$$

called the sample variance, is unbiased, i.e., ${ \mathrm { E } } \{ S ^ { \prime } { } ^ { 2 } \} = \sigma ^ { 2 }$ . However, if we estimate the population average by the sample mean

$$
M = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } X _ { i } ,
$$

the estimator $S ^ { \prime 2 }$ is only asymptotical unbiased. Indeed, it can be shown that for

$$
S ^ { \prime 2 } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( X _ { i } - M ) ^ { 2 } ,
$$

we have

$$
\operatorname { E } \big \{ S ^ { \prime 2 } \big \} = \sigma ^ { 2 } - \frac { \sigma ^ { 2 } } { n } .
$$

he sample variance is thus systematically smaller than the population variance.

In this case, it is easy to correct for the bias by considering the estimator

$$
S ^ { 2 } = { \frac { n } { n - 1 } } S ^ { ^ { \prime } 2 } .
$$

It follows that

$$
\operatorname { E } \left\{ S ^ { 2 } \right\} = \operatorname { E } \left\{ { \frac { n } { n - 1 } } S ^ { \prime 2 } \right\} = { \frac { n } { n - 1 } } ( \sigma ^ { 2 } - \sigma ^ { 2 } / n ) = \sigma ^ { 2 } .
$$

In order to estimate the variance of a population without bias, it is thus worth considering the estimator

$$
S ^ { 2 } = { \frac { 1 } { n - 1 } } \sum _ { i = 1 } ^ { n } ( x _ { i } - M ) ^ { 2 } .
$$

Note, however, that it has higher variance than the biased estimator $S ^ { \prime 2 }$ . Indeed, we have

$$
\mathrm { V a r } ( S ^ { 2 } ) = \frac { 2 \sigma ^ { 4 } } { n - 1 } > \mathrm { V a r } ( S ^ { \prime 2 } ) = 2 \sigma ^ { 4 } \frac { n - 1 } { n ^ { 2 } } .
$$

If an estimator $\widehat { \theta }$ is unbiased for $\theta$ , there is no reason why $g ( { \widehat { \theta } } )$ should be an unbiased estimator for $g ( \theta )$ . For example, if $g$ is a convex function, the Jensen inequality holds: ${ \mathrm { E } } \{ g ( X ) \} ~ \geq ~ g ( { \mathrm { E } } \{ X \} )$ , which shows that we should expect to observe a bias.

This is the case when estimating the standard deviation $\sigma$ . We have $\operatorname { E } \{ S ^ { 2 } \} ~ >$ $( \operatorname { E } \{ S \} ) ^ { 2 }$ , so we should expect the estimator $S ~ = ~ \sqrt { S ^ { 2 } }$ f gto be a biased estimator ffor $\sigma$ g. For a normal variable ${ \mathcal N } \mu , \sigma ^ { 2 }$ D, for example, the unbiased estimator for the standard deviation $\sigma$ is

$$
S ^ { * } = k _ { n } \left[ { \frac { 1 } { n - 1 } } \sum _ { i } ( X _ { i } - M ) ^ { 2 } \right] ^ { 1 / 2 } , \quad k _ { n } = { \sqrt { \frac { n - 1 } { 2 } } } { \frac { { \cal T } \left( { \frac { n - 1 } { 2 } } \right) } { { \cal T } \left( { \frac { n } { 2 } } \right) } } , \quad n \geq 2 ,
$$

where $\varGamma$ is the Euler function of the second kind.

When the Bias is Hard to Calculate

We then resort to resampling methods or bootstrap methods. The archetypal example is the following.

# Quenouille’s Method

If there is a bias of order $1 / n$ , this method can reduce it to order $1 / n ^ { 2 }$ . We assume that the mean value of the estimator can be expanded in powers of $1 / n$ . Half the sample is extracted, having removed one point if the sample size was odd to begin with. We then have

$$
\begin{array} { l } { { { \displaystyle { \mathbb E } \Bigl \{ \widehat \theta _ { n } \} = \theta + \frac { 1 } { n } \beta + { \cal O } ( 1 / n ^ { 2 } ) , } \ ~ } } \\ { { { \displaystyle { \mathbb E } \Bigl \{ \widehat \theta _ { 2 n } \} = \theta + \frac { 1 } { 2 n } \beta + { \cal O } ( 1 / n ^ { 2 } ) , } } } \end{array}
$$

whence

$$
\mathrm { E } \big \{ 2 \widehat { \theta } _ { 2 n } - \widehat { \theta } _ { n } \big \} = \theta + O ( 1 / n ^ { 2 } ) .
$$

The bias going as $1 / n$ has disappeared, but in general the variance of this new estimator will increase by a factor of order $1 / n$ . A better method would be to divide the $2 n$ -sample at random into two equal parts, evaluate the corresponding estimators ${ \widehat { \theta } } _ { n }$ and $\widehat { \theta } _ { n } ^ { \prime }$ , and calculate the new estimator

$$
2 \widehat { \theta } _ { 2 n } - \frac { 1 } { 2 } \widehat { ( \theta } _ { n } + \widehat { \theta } _ { n } ^ { \prime } ) .
$$

Jackknife Method

There is another method which only increases the variance by a term in $1 / n ^ { 2 }$ . This is the jackknife method. (For more details, see The Jackknife. A Review, Miller, 1974.) This involves more sophisticated calculation, but with today’s ever faster and ever cheaper electronic means of computation, the jackknife is superior to the Quenouille method described above.

Let ${ \widehat { \theta } } _ { n }$ be an estimator for $\theta$ , calculated from an $n$ -sample. Once again, expand its mean value in powers of $1 / n$ :

$$
\operatorname { E } { \big \{ } { \widehat { \theta } } _ { n } { \big \} } = \theta + \sum _ { k = 1 } ^ { \infty } { \frac { a _ { k } } { n ^ { k } } } .
$$

Now recalculate the $n$ estimators $\widehat { \theta } _ { - i }$ , each time removing a point $i$ from the $n$ -sample, and calculate the arithmetic mean of these estimators, viz.,

$$
{ \overline { { \widehat { \theta } } } } _ { n - 1 } = { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } { \widehat { \theta } } _ { - i } .
$$

Finally, define the jackknife $\widehat { \theta } _ { n } ^ { \prime }$ as

$$
\widehat { \theta } _ { n } ^ { \prime } = n \widehat { \theta } _ { n } - ( n - 1 ) \overline { { { \widehat { \theta } } } } _ { n - 1 } = \widehat { \theta } _ { n } + ( n - 1 ) \big ( \widehat { \theta } _ { n } - \overline { { { \widehat { \theta } } } } _ { n - 1 } \big ) .
$$

It can be shown that, for this estimator, the order $1 / n$ bias has also vanished.

# Efficiency

We have seen that, for unbiased estimators and for a quadratic loss function, these can be ordered according to the values of their variances. According to this idea, the estimator $\widehat { \theta } _ { 1 }$ will be preferable to $\widehat { \theta } _ { 2 }$ if $\operatorname { V a r } \left( { \widehat { \theta } } _ { 1 } \right) < \operatorname { V a r } \left( { \widehat { \theta } } _ { 2 } \right)$ . We then say that $\widehat { \theta } _ { 1 }$ is more efficient than $\widehat { \theta } _ { 2 }$ .

This raises two questions:

1. For a given unbiased estimator, can its variance be reduced?   
2. Is it possible, at least in principle, to make its variance arbitrarily small?

The answer to the first question is affirmative in some cases, but for this to be possible, there must be an exhaustive statistic. We shall see below what this involves. The answer to the second question is negative, if there is a lower bound below which the variance cannot be reduced. In general, this lower bound is not known, but an approximation can be given, viz., the Rao–Cramer bound. These considerations are ´ developed in the following.

# Reducing the Variance

Reduction of the variance involves the idea of an exhaustive summary, i.e., statistics containing everything we can hope to know about the parameter we are trying to estimate. Let us make this more precise.

Definition. A statistic $T$ is said to be exhaustive if the conditional distribution of the sample $X$ given that $T ( X ) ~ = ~ t$ does not depend on the parameter $\theta$ . If $f \left( x | T ( x ) = t \right)$ Ddenotes this conditional probability density of the sample $X$ , we jhave

$$
{ \frac { \partial } { \partial \theta } } f \bigl ( x | T ( x ) = t \bigr ) = 0 .
$$

Although abstract, this definition corresponds to what is usually done when compressing data. By keeping only the value $T ( X )$ from the original sample $X = ( X _ { 1 } , \ldots , X _ { n } )$ , we keep only what depended on $\theta$ . Indeed, the equation $T ( x ) =$ $t$ Dspecifies a hypersurface in the sample space $\mathbb { R } ^ { n }$ , and saying that $T$ Dprovides an exhaustive summary amounts to saying that only the value $t$ of this statistic is important. The distribution of ‘points’ $X _ { i }$ actually on this hypersurface is of no importance, since it does not depend on what we seek here. If we had to reconstruct a sample with the same characteristics as the original sample with regard to estimation of $\theta$ , the points could be distributed at random over the hypersurface $\textit { T } = \textit { t }$ according to the corresponding conditional distribution.

In order to show that a statistic is exhaustive, it is often simpler to appeal to the following criterion.

Theorem. Factorisation or Fisher–Neyman Criterion. A statistic $T$ is exhaustive for estimating $\theta$ if and only if the likelihood function of the sample can be factorised in the form

$$
L ( x , \theta ) = l ( t , \theta ) h ( x ) ,
$$

where $x$ denotes a value taken by the sample, i.e., . $( X _ { 1 } = x _ { 1 } , \ldots , X _ { n } = x _ { n } )$ /, and $L$ D Dis the probability distribution at this point (or just the probability if the variables are discrete). The functions $l$ and $h$ must be positive.

Example: Poisson Distribution. For an independent and identically distributed sample with Poisson distribution, we have

$$
\operatorname* { P r } \{ X = x \} = \prod _ { i = 1 } ^ { n } { \frac { \lambda ^ { x _ { i } } } { x _ { i } ! } } \mathrm { e } ^ { - \lambda } = { \frac { \lambda ^ { \sum x _ { i } } \mathrm { e } ^ { - n \lambda } } { \prod x _ { i } ! } } .
$$

This satisfies the factorisation criterion with $h ( x ) = 1 / \prod x _ { i } !$ and the statistic $T =$ $\textstyle \sum _ { i = 1 } ^ { n } x _ { i }$ is exhaustive for the parameter $\lambda$ D of the Poisson distribution.

With this idea in hand, we can now state a version of the Rao–Blackwell theorem for the case of quadratic loss functions.

Rao–Blackwell Theorem. If $\widehat { \theta }$ is an unbiased estimator of $\tau ( \theta )$ and if the sampling law admits an exhaustive statistic $T$ , then the estimator $\widehat { \theta } _ { 1 }$ calculated from

$$
\widehat { \theta } _ { 1 } = \mathrm { E } \big \{ \widehat { \theta } | T = t \big \}
$$

is unbiased and has smaller variance than the original estimator:

$$
\forall \theta , \quad \operatorname { V a r } ( { \widehat { \theta } } _ { 1 } ) < \operatorname { V a r } ( { \widehat { \theta } } ) ,
$$

unless the estimators turn out to be identical.

The improvement achieved by the Rao–Blackwell theorem does not guarantee that the new estimator has minimal variance, however. For this to be the case, the statistic $T$ must also be complete.

Definition. The statistic $T$ is said to be complete if the expectation of all integrable functions of $T$ is non-degenerate, i.e., if

$$
\forall \theta , g \in L ^ { 1 } , \quad \operatorname { E } \{ g ( T ) \} = 0 \Longrightarrow g ( t ) = 0 .
$$

The $\theta$ dependence is contained in the sampling distribution used to calculate the expectation.

Example: Binomial Distribution. The sample $X$ of size $k = 1$ is drawn from a binomial distribution with unknown parameter $\theta$ D, while the parameter $n$ is known. The statistic $T = X$ is trivially exhaustive. Show that it is also complete. For all integrable $g$ ,

$$
\begin{array} { c l c } { \displaystyle \forall \theta \in ( 0 , 1 ) , \quad \operatorname { E } \{ g ( T ) \} = \sum _ { x = 0 } ^ { n } g ( x ) C _ { n } ^ { x } \theta ^ { x } ( 1 - \theta ) ^ { n - x } = 0 } \\ { \displaystyle } & { \qquad = ( 1 - \theta ) ^ { n } \sum _ { x = 0 } ^ { n } g ( x ) C _ { n } ^ { x } \left( \frac { \theta } { 1 - \theta } \right) ^ { x } = 0 . } \end{array}
$$

The last expression is a polynomial in $\theta / ( 1 - \theta )$ of degree $n$ which vanishes for infinitely many values of its variable. It is therefore identically zero and $g ( x ) = 0$ . A similar result can be proven for a sample of arbitrary size $k$ and for $\textstyle T = \sum _ { i = 1 } ^ { k } X _ { i }$

Lehmann–Scheffe Theorem.´ If $T$ is an exhaustive and complete statistic, then the improvement of $\widehat { \theta }$ under the conditions of the Rao–Blackwell theorem has smaller variance. The resulting estimator $\widehat { \theta } _ { 1 }$ is thus the UMVU estimator.

Example. Following Tassi (see the bibliography), consider the case where an object has probability $p$ of possessing some feature considered to be exceptional in some sense. The objects are arranged into $r$ classes and $n$ objects are then drawn independently from each class. The number of objects per class is relatively unimportant, provided it is greater than $n$ . The class itself is said to be exceptional if there is at least one exceptional object among the $n$ objects drawn out, and otherwise it is said to be ordinary. Let $X _ { i }$ be the number of exceptional objects in the sample of size $n$ drawn from class $i$ . The problem is to estimate without bias, given the data $( X _ { 1 } , \ldots , X _ { r } )$ , the probability $\theta$ that a class is ordinary.

Consider the variable $\mathbf { 1 } _ { X _ { i } = 0 }$ , which is the indicator function for class $i$ to be ordinary. If we set $\widehat { \theta } = \mathbf { 1 } _ { X _ { i } = 0 }$ D, the estimator is a Bernoulli variable with parameter $\theta$ . We then have

$$
\mathbb { E } \big \{ \widehat { \theta } \big \} = \mathbb { E } \{ { \bf 1 } _ { X _ { i } = 0 } \} = \theta ,
$$

and this estimator is thus unbiased. In order to improve it using the Rao–Blackwell theorem, we require an exhaustive statistic for estimation of $\theta$ . The likelihood function of the data $( X _ { 1 } , \ldots , X _ { r } )$ is the product of $r$ binomially distributed random variables. We have

$$
L ( x , \theta ) = \prod _ { i = 1 } ^ { r } C _ { n } ^ { X _ { i } } p ^ { X _ { i } } ( 1 - p ) ^ { n - X _ { i } } = \left( \frac { p } { 1 - p } \right) ^ { \sum _ { i } X _ { i } } ( 1 - p ) ^ { n r } \prod _ { i = 1 } ^ { r } C _ { n } ^ { X _ { i } } .
$$

This is indeed in the form (9.26) and the statistic $\textstyle T = \sum _ { i = 1 } ^ { r } X _ { i }$ is exhaustive for $p$ . It is also exhaustive for $\theta$ , which depends only on $p$ D D. The estimator $h ( \widehat { \theta } )$ improved by Rao–Blackwell is then

$$
h ( \widehat { \theta } ) = \mathrm { E } \big \{ \widehat { \theta } | T = t \big \} .
$$

Considering the class $i = 1$ for calculation of $\widehat { \theta }$ , it follows that

$$
h ( \widehat { \theta } ) = \mathrm { E } \big \{ \widehat { \theta } | T = t \big \} = \mathrm { P r } \{ X _ { 1 } = 0 | T = t \} = \frac { \mathrm { P r } \{ X _ { 1 } = 0 , T = t \} } { \mathrm { P r } \{ T = t \} } .
$$

The sampling model is binomial, whence

$$
\frac { \operatorname* { P r } \left\{ X _ { 1 } = 0 , \sum _ { i = 2 } ^ { r } X _ { i } = t \right\} } { \operatorname* { P r } \left\{ \sum _ { i = 1 } ^ { r } X _ { i } = t \right\} } = \frac { C _ { n r - n } ^ { \mathrm { T } } } { C _ { n r } ^ { \mathrm { T } } } .
$$

This estimator depends only on the value of the variable $T$ , denoted by $h ( T )$ . Then

$$
h ( T ) = { \frac { C _ { n r - n } ^ { T } } { C _ { n r } ^ { T } } } .
$$

Since we have seen that this statistic is also complete, $h ( T )$ is therefore the UMVU estimator for $\theta$ .

# 9.5.5 Frechet or Rao–Cram ´ er Inequality ´

Since the variance of an estimator can be reduced under certain conditions, it is then legitimate to ask how far such a reduction can be taken. Clearly, the variance cannot be less than zero, but is there a strictly positive bound below which, for a given problem, it is impossible to find an estimator achieving this level of performance? The problems relating to the search for this bound involve theoretical and practical features of great importance, which we shall discuss in this section.

An unbiased estimator which reaches this limiting variance will be preferable to all others in the sense of quadratic risk. It will be called the optimal estimator and hence will be the UMVU estimator. However, in the general case, there is no way to find the optimal limit. On the other hand, it is possible to give an approximation, namely the Rao–Cramer bound, or´ minimum variance bound. Furthermore, there is a large class of estimators that actually reach this bound, known as efficient estimators, which we shall now examine.

Such an estimator $T$ , by assumption unbiased, has mean $\operatorname { E } \{ T \} = \tau ( \theta )$ and variance $\operatorname { V a r } ( T ) ~ = ~ \operatorname { E } \{ { \bigl [ } T - \tau ( \theta ) { \bigr ] } ^ { 2 } \}$ f g D. To calculate this variance, we use the D mathematical expectation operator, which is a linear operator and with which we can associate a scalar product. This scalar product obeys the Cauchy–Schwartz inequality. Let $\psi$ be a function of the $n$ -sample (denoted by $X$ ) and the parameter $\theta$ to be estimated. By the Cauchy–Schwartz inequality,

$$
\begin{array} { r } { \mathrm { E } \{ \big [ T - \tau ( \theta ) \big ] ^ { 2 } \} \mathrm { E } \{ \psi ( X , \theta ) ^ { 2 } \} \geq \Big [ \mathrm { E } \{ \big [ T - \tau ( \theta ) \big ] \psi ( X , \theta ) \} \Big ] ^ { 2 } , } \end{array}
$$

whence, given that $\mathbb { E } \{ [ T - \tau ( \theta ) ] ^ { 2 } \} = \mathrm { V a r } ( T )$

$$
\operatorname { V a r } ( T ) \geq { \frac { \left[ \operatorname { E } \left\{ { \bigl [ } T - \tau ( \theta ) { \bigr ] } \psi ( X , \theta ) \right\} \right] ^ { 2 } } { \operatorname { E } \left\{ \psi ( X , \theta ) ^ { 2 } \right\} } } .
$$

Equality obtains if and only if the function $\psi$ is proportional to $T - \tau ( \theta )$ , that is, if and only if

$$
\psi ( X , \theta ) = A ( \theta ) \big [ T - \tau ( \theta ) \big ] .
$$

The inequality (9.32) can in principle be used to find the optimal bound, since

$$
\mathrm { V a r } ( T ) \geq \operatorname* { m a x } _ { \psi } \frac { \Big [ \mathrm { E } \big \{ \big [ T - \tau ( \theta ) \big ] \psi ( X , \theta ) \big \} \Big ] ^ { 2 } } { \mathrm { E } \big \{ \psi ( X , \theta ) ^ { 2 } \big \} } .
$$

However, it is almost impossible for all $T$ and $\tau ( \theta )$ and all parent populations to exhibit the optimal bound by calculating the maximum. The best that can be done is to find a function $\psi$ that provides a bound close enough to the optimal bound. If the function $\psi$ is not well chosen, we find a lower bound that is too small, e.g., if $\psi$ does not depend on $X$ , we will find $\mathrm { V a r } ( T ) \geq 0$ , which we already knew. In order to find a best lower bound, we must identify a common case where the function $\psi$ has the above form (9.33), so that the bound is attained. For this particular case, the bound obtained will be the optimal one.

Let us consider the case where the $n$ -sample $X$ comes from a normal parent distribution with known mean $\mu$ and variance $\sigma ^ { 2 }$ , and the parameter $\theta$ to be estimated is the mean $\mu$ , estimated by the empirical average $M$ . Assume also that the sample is made up of independepent and identically distributed random variables.

First we calculate the likelihood function for this $n$ -sample:

$$
L ( X | \theta ) = \prod _ { i = 1 } ^ { n } { \frac { 1 } { \sigma { \sqrt { 2 \pi } } } } \exp \left[ - { \frac { 1 } { 2 } } \left( { \frac { X _ { i } - \theta } { \sigma } } \right) ^ { 2 } \right] .
$$

The product is eliminated by taking the logarithm of the expression to give

$$
\ln { \cal L } = - n \ln ( \sigma \sqrt { 2 \pi } ) - \sum _ { i = 1 } ^ { n } \frac { 1 } { 2 } \left( \frac { X _ { i } - \theta } { \sigma } \right) ^ { 2 } .
$$

We now eliminate the constant and the square by differentiating with respect to $\theta$ to obtain

$$
{ \frac { \partial \ln L } { \partial \theta } } = { \frac { 1 } { \sigma ^ { 2 } } } \sum _ { i = 1 } ^ { n } x _ { i } - { \frac { n \theta } { \sigma ^ { 2 } } } = { \frac { n } { \sigma ^ { 2 } } } ( M - \theta ) .
$$

We then see that in the particular case of estimation of the mean $\mu$ of a normal population with known variance by the arithmetic mean $M$ , the function $\partial \ln L / \partial \theta$ has precisely the form (9.33) which makes the Cauchy–Schwartz inequality into an equality. In this case the resulting bound is the optimal bound.

For an arbitrary population and when estimating a function of an arbitrary parameter $\theta$ by a statistic $T$ , we can be sure that the variance of $T$ will always be greater than or equal to the limit found if we replace the function $\psi$ by $\partial \ln L / \partial \theta$ in the Cauchy–Schwartz inequality. It will not be the optimal bound but it is of great practical importance because of the case giving rise to it. It is called the minimum variance bound (MVB).

It remains to actually calculate this bound, and to do this, we have to find the various expectation values appearing in (9.32). The calculation is relatively simple and we shall not go into the details here. Note, however, that the final result is only valid when the operations of integration and differentiation with respect to the parameter to be estimated can be legitimately interchanged, e.g., when the integration bounds do not depend on this parameter. With this proviso, if the estimator $T$ is unbiased, we deduce the following inequality for the variance, known as the Rao–Cramer or Fr ´ echet inequality: ´

$$
\boxed { \mathrm { V a r } ( T ) \geq \frac { \left[ \tau ^ { \prime } ( \theta ) \right] ^ { 2 } } { \mathrm { E } \{ - \partial ^ { 2 } \ln L / \partial \theta ^ { 2 } \} } . }
$$

We have seen that the relatively arbitrary choice of function $\psi$ implies that this lower bound is not necessarily attained. For it to be attained, a necessary and sufficient condition is

$$
\frac { \partial } { \partial \theta } \ln { \cal L } = A ( \theta ) \big [ T - \tau ( \theta ) \big ] ,
$$

where $A ( \theta )$ is an arbitrary function of the parameter $\theta$ to be estimated. If the variance of an estimator reaches this bound, it is called the minimum variance bound (MVB).

# 9.5.6 Efficient Estimators

When the MVB is attained, we have

$$
\frac { \partial \ln { \cal L } } { \partial \theta } = A ( \theta ) \big [ T - \tau ( \theta ) \big ] .
$$

Substituting this directly into (9.38), we obtain

$$
\operatorname { V a r } ( T ) = { \frac { \tau ^ { \prime } ( \theta ) } { A ( \theta ) } } ,
$$

and if $\tau ( \theta ) = \theta$ ,

$$
\operatorname { V a r } ( T ) = { \frac { 1 } { A ( \theta ) } } .
$$

The last two expressions can in some cases be used to find the variance of an MVB estimator rather easily, as illustrated by the following examples.

Example: Variance of the Arithmetic Mean of a Normal Distribution. For an $n$ -sample drawn from a normal distribution with known variance $\sigma ^ { 2 }$ and for estimation of the mean $\theta$ by the arithmetic mean $T \ = \ M$ , we saw earlier that we had

$$
{ \frac { \partial } { \partial \theta } } \ln L = { \frac { n } { \sigma ^ { 2 } } } ( M - \theta ) , \quad { \mathrm { h e n c e } } \quad A ( \theta ) = { \frac { n } { \sigma ^ { 2 } } } ,
$$

so that

$$
\operatorname { V a r } ( T ) = { \frac { \sigma ^ { 2 } } { n } } .
$$

Example: Variance of the Sample Variance of a Normal Distribution. Consider a normal population with probability distribution

$$
f ( x ) = \frac { 1 } { \sqrt { 2 \pi } \theta } \exp \left( - \frac { x ^ { 2 } } { 2 \theta ^ { 2 } } \right) .
$$

The average is known and can be assumed to be zero, but the variance $\theta ^ { 2 }$ is not known. We then have

$$
{ \frac { \partial \ln L } { \partial \theta } } = { \frac { n } { \theta ^ { 3 } } } \left( { \frac { 1 } { n } } \sum X _ { i } ^ { 2 } - \theta ^ { 2 } \right) = { \frac { n } { \theta ^ { 3 } } } { \bigl ( } S ^ { \prime 2 } - \theta ^ { 2 } { \bigr ) } .
$$

The form of the function $\partial \ln L / \partial \theta$ naturally suggests choosing the statistic

$$
S ^ { \prime 2 } = { \frac { 1 } { n } } \sum X _ { i } { } ^ { 2 }
$$

as estimator for $\theta ^ { 2 }$ . This estimator will be MVB provided that it is unbiased. It is easy to demonstrate that this last condition is satisfied since

$$
\operatorname { E } \{ S ^ { \prime 2 } \} = \int { s ^ { 2 } } L \mathrm { d } \mathbf { x } = { \frac { 1 } { n } } \sum _ { i } \int { X _ { i } } ^ { 2 } L \mathrm { d } \mathbf { x } = { \frac { 1 } { n } } \sum _ { i } \theta ^ { 2 } = \theta ^ { 2 } .
$$

Therefore, $S ^ { \prime 2 }$ is indeed an MVB estimator for the function $\tau ( \theta ) = \theta ^ { 2 }$ . We can immediately calculate its variance to be

$$
\operatorname { V a r } ( S ^ { \prime 2 } ) = { \frac { \tau ^ { \prime } ( \theta ) } { n / \theta ^ { 3 } } } = { \frac { 2 \theta } { n / \theta ^ { 3 } } } = { \frac { 2 \theta ^ { 4 } } { n } } .
$$

The standard deviation, denoted here by $\theta$ , is usually denoted by $\sigma$ , whence

$$
\operatorname { V a r } ( S ^ { \prime 2 } ) = { \frac { 2 \sigma ^ { 4 } } { n } } .
$$

We thus find the variance of the sample variance for a normal sample with known mean.

# 9.5.7 Efficiency of an Estimator

Let $T$ be a convergent unbiased estimator for estimating $\tau ( \theta )$ . Its efficiency is measured by the reciprocal of the ratio of its variance to the limiting variance given by the MVB:

$$
\mathrm { E f f } ( T ) = \frac { \mathrm { V a r } _ { \mathrm { M V B } } ( \theta ) } { \mathrm { V a r } ( T ) } .
$$

The estimator $T$ will be said to be efficient if it has efficiency equal to 1 (or $100 \%$ ), or in other words if it attains its MVB. As already noted, the MVB is not necessarily attained and an optimal estimator is not necessarily efficient.

# 9.5.8 Biased Estimators

Let $T$ be a biased estimator for $\theta$ . By the definition of bias, we have

$$
\mathrm { e } T = \theta + b ( \theta ) .
$$

If we choose the function $\tau ( \theta ) = \theta + b ( \theta )$ , we have

$$
\mathrm { e } T = \tau ( \theta ) ,
$$

which shows that $T$ is an unbiased estimator for $\tau ( \theta )$ . Let us apply the Rao–Cramer´ formula for this function $\tau$ . We find $\tau ^ { \prime } ( \theta ) = 1 + b ^ { \prime } ( \theta )$ , and also

$$
\operatorname { V a r } ( T ) \equiv \operatorname { E } \{ \left[ t - { \bigl ( } \theta + b ( \theta ) { \bigr ) } \right] ^ { 2 } \} = \operatorname { E } \{ ( T - \theta ) ^ { 2 } \} - b ^ { 2 } ( \theta ) .
$$

The term $\mathrm { E } \big \{ ( T - \theta ) ^ { 2 } \big \}$ is the mean squared error (MSE) in $T$ . We have just seen that it is always greater than or equal to the variance of $T$ . Finally, we may write

$$
\mathbb { E } \big \{ ( T - \theta ) ^ { 2 } \big \} = \operatorname { V a r } ( T ) + b ^ { 2 } ( \theta ) \geq \frac { \big [ 1 + b ^ { \prime } ( \theta ) \big ] ^ { 2 } } { \mathbb { E } \big \{ - \partial ^ { 2 } \ln L / \partial \theta ^ { 2 } \big \} } + b ^ { 2 } ( \theta ) .
$$

While it is true that the mean squared error in a biased estimator is always greater than its variance, the example below shows that it is possible to find a biased estimator for which the mean squared error is smaller than the smallest variance associated with the class of unbiased estimators.

Example: Estimating the Parameter of an Exponential Distribution. Consider an independent and identically distributed $n$ -sample $( X _ { 1 } , \ldots , X _ { n } )$ drawn from a population with exponential distribution having mean $\theta$ :

$$
f ( x ) = { \frac { 1 } { \theta } } \exp \left( - { \frac { x } { \theta } } \right) , \quad { \mathrm { w h e r e } } \quad \operatorname { E } \{ X _ { i } \} = \theta , \quad \operatorname { V a r } ( X _ { i } ) = \theta ^ { 2 } .
$$

Let us choose the arithmetic mean $\overline { { X } }$ as estimator for $\theta$ . We know that it is an unbiased estimator for the population average, and hence $\operatorname { E } \{ { \overline { { X } } } \} = \theta$ . In this case, its mean squared error with respect to $\theta$ is equal to its variance:

$$
\mathsf { e } ( \overline { { X } } - \theta ) ^ { 2 } = \mathrm { E } \Big \{ \big ( \overline { { X } } - \mathrm { E } \big \{ \overline { { X } } \big \} \big ) ^ { 2 } \big \} \equiv \mathrm { V a r } ( \overline { { X } } ) .
$$

We now show that $\overline { { X } }$ is MVB by calculating $\partial \ln L / \partial \theta$ :

$$
\ln { \cal L } = - n \ln \theta - \frac { 1 } { \theta } \sum _ { i = 1 } ^ { n } X _ { i } ,
$$

$$
{ \frac { \partial \ln L } { \partial \theta } } = - { \frac { n } { \theta } } + { \frac { 1 } { \theta ^ { 2 } } } \sum _ { i = 1 } ^ { n } X _ { i } = { \frac { n } { \theta ^ { 2 } } } ( \overline { { X } } - \theta ) .
$$

This shows that $\overline { { X } }$ is indeed MVB for estimating $\theta$ , whence it follows immediately that

$$
\operatorname { V a r } ( { \overline { { X } } } ) = { \frac { \theta ^ { 2 } } { n } } .
$$

On the other hand, the estimator $\widehat { X } = n \overline { { X } } / ( n + 1 )$ is biased but its mean squared error is smaller than the MVB $\theta ^ { 2 } / n$ D Cof the unbiased estimators. Indeed, it is biased:

$$
\operatorname { E } \{ \widehat { X } \} = \frac { n } { n + 1 } \theta , \qquad b _ { n } ( \theta ) = - \frac { \theta } { n + 1 } ,
$$

but we have the inequalities

$$
\operatorname { V a r } ( { \widehat { X } } ) = { \frac { n } { ( n + 1 ) ^ { 2 } } } \theta ^ { 2 } < \operatorname { E } \left\{ ( { \widehat { X } } - \theta ) ^ { 2 } \right\} = { \frac { \theta ^ { 2 } } { n + 1 } } < \operatorname { V a r } ( { \overline { { X } } } ) = { \frac { \theta ^ { 2 } } { n } } .
$$

This example shows that it can be too restrictive to search for the best estimator only in the class of unbiased estimators.

# 9.5.9 Minimum Variance Bound and Fisher Information

The non-negative quantity

$$
I _ { n } ( \theta ) \equiv \operatorname { E } { \Biggl \{ } \left( { \frac { \partial } { \partial \theta } } \ln L \right) ^ { 2 } { \Biggr \} } = \operatorname { E } { \Biggl \{ } - { \frac { \partial ^ { 2 } } { \partial \theta ^ { 2 } } } \ln L { \Biggr \} }
$$

is called the Fisher information contained in the $n$ -sample. Since the random variable $\partial \ln L / \partial \theta$ has zero mean, the Fisher information is just the reciprocal of the variance of this random variable.

For independent and identically distributed samples, this quantity depends only the size of the $n$ -sample and the probability distribution of the parent population, and we have shown that $I _ { n } ( \theta ) = n I _ { 1 } ( \theta )$ . This means that, in the case where the Rao– DCramer inequality applies, the variance of an estimator ´ $T$ decreases more slowly than $1 / n$ . The inequality then becomes

$$
\operatorname { V a r } ( T ) \geq { \frac { \left[ \tau ^ { \prime } ( \theta ) \right] ^ { 2 } } { n I _ { 1 } ( \theta ) } } .
$$

When estimating the midpoint of a uniform probability density on $( 0 , \theta ]$ , the estimator

$$
\frac { 1 } { 2 } \big [ X _ { ( n ) } + X _ { ( 1 ) } \big ]
$$

of the mean $\theta / 2$ has asymptotic variance

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname { v a r } \left( { \frac { 1 } { 2 } } \big [ X _ { ( n ) } + X _ { ( 1 ) } \big ] \right) = { \frac { 1 } { 2 n ^ { 2 } } } .
$$

This asymptotic variance decreases faster than the Rao–Cramer bound because this´ is exactly the case where this bound does not apply. Indeed, the mathematical expectation is given by the integral $\begin{array} { r } { \int _ { 0 } ^ { \theta } \mathrm { d } x } \end{array}$ , and the upper bound is a function of the parameter to be estimated, whence the Rao–Cramer does not apply. ´

The bounds deduced from the Rao–Cramer inequalities are adapted to the case´ where measurement errors are small around the estimated parameter. By this we mean that these errors have a distribution close to normal. When the errors are large, e.g., close to a Cauchy distribution, there are then better suited bounds, i.e., greater than the Rao–Cramer bounds.´

# 9.5.10 Multidimensional Case

When the experimenter wishes to make joint estimates of a set of $k$ parameters $( \theta _ { 1 } , \ldots , \theta _ { k } )$ , there is a generalisation of the Rao–Cramer inequality. This appeals to ´

the Fisher information matrix $J$ , with elements $J _ { i j }$ given by

$$
J _ { i j } = \operatorname { E } \left\{ - { \frac { \partial ^ { 2 } } { \partial \theta _ { i } \partial \theta _ { j } } } \log L \right\} .
$$

If $V$ denotes the matrix of variances and covariances for the paramters $\theta$ , the inequality is given symbolically by $V ~ \geq ~ J ^ { - 1 }$ . We use the convention that an inequality sign $>$ between matrices means that their difference is a positive definite matrix, i.e., all its eigenvalues are positive, while $\geq$ means that at least one eigenvalue may be zero.

From a practical standpoint, this means that the error ellipse at the confidence level $\gamma$ , i.e.,

$$
\begin{array} { r } { ( \theta - \widehat { \theta } ) ^ { \mathrm { T } } \mathsf { V } ^ { - 1 } ( \theta - \widehat { \theta } ) = k _ { \gamma } ^ { 2 } , } \end{array}
$$

encompasses the confidence region calculated with the matrix $J$ , i.e.,

$$
\begin{array} { r } { ( \boldsymbol { \theta } - \widehat { \boldsymbol { \theta } } ) ^ { \mathrm { T } } \mathbf { J } ( \boldsymbol { \theta } - \widehat { \boldsymbol { \theta } } ) = k _ { \gamma } ^ { 2 } . } \end{array}
$$

This last confidence region can be used as an approximation to the actual confidence region. The scalar $k _ { \gamma } ^ { 2 }$ is calculated (under the normal distribution hypothesis) using the distribution function $F$ of a $\chi ^ { 2 }$ distribution with $k$ degrees of freedom: $k _ { \gamma } ^ { 2 } =$ $F ^ { - 1 } ( 1 - \gamma )$ .

# 9.5.11 Robust Estimators

As we have already seen, there are generally several estimators for the same parameter $\theta$ . Among other things, the arithmetic mean, median, and midpoint of the sample are often considered to estimate the population average. For example, for a normal distribution, the arithmetic mean of the sample is unbiased and MVB. It is thus the best possible estimator and there is no reason to look for any other. But which one should we choose when we do not know the nature of the parent population, or when we do know that but there is contamination by measurement errors of unknown type? To fix ideas, we shall consider three very different parent populations and give the asymptotic variances of the three previous estimators. As these three densities are symmetric, it is in fact the position of the axis of symmetry that we seek to determine. To simplify, we shall take all scale factors equal to unity. We then obtain Table 9.7, in which values in bold type are the smallest possible.

We see in this example that, if we have no idea what kind of underlying parent population we are dealing with, it is safer to use the median, in order to obtain a finite variance in all cases. We may consider Table 9.7 as the loss matrix for a game against nature, where we can in fact only lose in this case. The median is chosen according to the minimax strategy, i.e., minimising the maximum loss. The median is said to be a reliable or robust estimator for this set of populations.

Table 9.7 Asymptotic variance of three different populations. The uniform distribution is taken here over the interval from 0 to 1   

<table><tr><td></td><td>Uniform distribution</td><td>Normal distribution</td><td>Cauchy distribution</td></tr><tr><td rowspan="2">Median</td><td>1</td><td>元</td><td>π²</td></tr><tr><td>4n</td><td>2n</td><td>4n</td></tr><tr><td rowspan="2">Mean</td><td>1</td><td>1</td><td rowspan="2">8</td></tr><tr><td>12n</td><td>n</td></tr><tr><td rowspan="2">Midpoint</td><td>1</td><td>π²</td><td rowspan="2">8</td></tr><tr><td>2n2</td><td>24 ln n</td></tr></table>

There are several other reliable estimators for the symmetry axis of a population with symmetric distribution. Depending on their type, they can be suitable for a range of different populations. Here are some of them:

• Truncated or Trimmed Mean. Consider the symmetric bilateral truncated mean. We remove $2 q$ points from the ordered $n$ -sample

$$
( X _ { ( 1 ) } \leq X _ { ( 2 ) } \leq \ldots \leq X _ { ( n ) } ) ,
$$

namely the $q$ smallest and the $q$ largest, to obtain the new sample

$$
( X _ { ( q + 1 ) } \leq . . . \leq X _ { ( n - q ) } ) .
$$

The truncation parameter is defined here as

$$
\alpha = { \frac { q } { n } } ,
$$

and the arithmetic mean of the remaining $( n - 2 q )$ -sample will be called the mean symmetrically truncated at $100 \%$  and denoted by $T _ { \alpha }$ . We will thus have

$$
T _ { \alpha } = \frac { 1 } { ( n - 2 q ) } \sum _ { i = q + 1 } ^ { n - q } X _ { ( i ) } .
$$

Note that $\alpha$ is generally fixed between 0 and 1. We then calculate $q = \lfloor \alpha n \rfloor$ . In this case, the mean is truncated by at most $100 \%$ and at least $1 0 0 ( \alpha - 1 / n ) \%$ .

• Winsorized Mean. The procedure is the same as for the truncated mean, except that we replace the $q$ smallest values by $X _ { ( q + 1 ) }$ and the $q$ largest by $X _ { ( n - q ) }$ , then calculate the mean:

$$
W _ { \alpha } = \frac { 1 } { n } \left[ \sum _ { i = q + 1 } ^ { n - q } X _ { ( i ) } + q \big [ X _ { ( q + 1 ) } + X _ { ( n - q ) } \big ] \right] .
$$

• Hodges–Lehmann Median. We construct the new sample $( Y _ { 1 1 } , Y _ { 1 2 } , \ldots , Y _ { n n } )$ from the sample $( X _ { 1 } , \ldots , X _ { n } )$ by the rule

$$
Y _ { i j } = \frac { 1 } { 2 } ( X _ { i } + X _ { j } ) ,
$$

and we define the Hodges–Lehmann median $\mathrm { H L }$ as the median of the $Y _ { i j }$ .

• Midpoint. This statistic is the point located at equal distance from the two outermost points, and it is thus equal to

$$
P = { \frac { 1 } { 2 } } \bigl [ X _ { ( 1 ) } + X _ { ( n ) } \bigr ] .
$$

Example: Asymptotic Variances of Several Estimators for the Cauchy Distribution. Consider an independent and identically distributed $n$ -sample drawn from a Cauchy distribution with probability distribution

$$
f ( x ) = { \frac { 1 } { \pi { \big [ } 1 + ( x - \theta ) ^ { 2 } { \big ] } } } .
$$

The asymptotic variances of different estimators for $\theta$ are given in Table 9.8. From the table, we see that the mean truncated at $38 \%$ is only slightly less efficient, but much easier to calculate than the estimate of the maximum likelihood in this optimal case.

# 9.5.12 Some Classic Methods

It seems that effective estimators can be obtained by implementing a method that takes into account both the observed data $x$ and what is known about the unknown parameter $\theta$ . For this purpose, we might consider looking for the value of $\theta$ that maximises the a posteriori probability density $\psi ( \theta | x )$ , or a functional of this. However, $\psi$ jis written as the product of the likelihood $l ( x | \theta )$ and the a priori probability density $\pi ( \theta )$ , and if we do not possess information about $\theta$ , $\pi ( \theta )$ remains undetermined. We may then attempt to maximise the likelihood and look for $\widehat { \theta }$ as solution of the implicit equation: $l ( x | \theta ) = \mathrm { m a x } _ { \theta } l ( x | \theta )$ . The estimator j Dfound in this way is the estimator for the maximum likelihood.

Table 9.8 Asymptotic variance of various estimators for $\theta _ { 0 }$   

<table><tr><td>Estimator</td><td>Asymptotic variance</td></tr><tr><td>Maximumlikelihood</td><td>2 n</td></tr><tr><td>Mean truncated at 38%</td><td>2.28 R n</td></tr><tr><td>Median</td><td>2.47 3 4n</td></tr></table>

This estimator is often found as a solution to the equations $\partial l / \partial \theta \ : = \ : 0$ with $\partial ^ { 2 } l / \partial \theta ^ { 2 } \ < \ 0$ D. Under these conditions, it can be shown that the estimator $\widehat { \theta }$ is convergent. In addition, the quantity

$$
\left( - \frac { \partial ^ { 2 } l } { \partial \theta ^ { 2 } } \bigg | _ { \theta = \widehat { \theta } } \right) ^ { 1 / 2 } ( \widehat { \theta } - \theta )
$$

behaves roughly like a normal random variable with zero mean and unit variance. This shows that, provided that the associated moments exist, the maximum likelihood estimator is asymptotically unbiased and asymptotically efficient. It is this result that gives the maximum likelihood estimator its special status.

If the problem reduces to estimating the mean $\mu = \mu ( \theta )$ of a normal sample, the likelihood function is equal to $\exp ( - \chi ^ { 2 } / 2 )$ Dup to a multiplicative constant, where $\chi ^ { 2 }$ is a quadratic form equal to $( x - \mu ) ^ { \mathrm { { T } } } V ^ { - 1 } ( x - \mu )$ , with $V$ the variance– covariance matrix of $x$ and $X ^ { \mathrm { T } }$ the transpose of $X$ . This therefore amounts to looking for the maximum of $l$ or $\log { l }$ and the maximum likelihood then corresponds to the minimum of the form $( x - \mu ) ^ { \mathrm { { T } } } V ^ { - 1 } ( x - \mu )$ . This remark introduces the  underlying idea of the least squares method, discussed here in the normal case and for measurements of unequal accuracy.

Outside the normal case, the least squares method (or least $\chi ^ { 2 }$ for measurements of unequal accuracy) does not always yield optimal estimators. However, there is another favourable situation, namely the linear case. This refers to a situation in which the mean $\mu$ depends linearly on the unknown parameters $\theta$ , and no assumptions are made about the type of data apart from the existence of $\mu$ and $V$ . In particular, we do not necessarily know the probability density. The decomposition of $\mu$ in terms of a polynomial basis or in a Fourier series expansion are two examples of linear situations. The coefficients of these expansions are the unknown parameters $\theta$ . If $\mu = X \theta$ is the matrix equation expressing the linear dependence of the model $\mu$ on $\theta$ Dand if $y$ denotes the data (it is traditional to use $y$ rather than $x$ in this case), the least squares estimators are given by the expression ${ \widehat { \theta } } = ( X ^ { \operatorname { T } } X ) ^ { - 1 } X ^ { \operatorname { T } } y$ in the case where the matrix $V$ Dis the identity matrix (and we may always reduce to this case by a change of variables). The Gauss–Markov theorem states that these estimators are unbiased and that, for each parameter $\theta$ , they have the smallest variance in the class of linear estimators. It is remarkable that the estimator $\widehat { \theta }$ has optimal properties without any reference to the probability density of the measurements $y$ .

The maximum likelihood and least squares methods often provide good estimators, but they can prove to be unacceptable. They may be the best in a class that turns out to be too small, e.g., normal case or class of unbiased estimators. They may also exhibit anomalies, e.g., if the operator $( X ^ { \mathrm { T } } X ) ^ { - 1 }$ does not exist. In this case, one must revert to the idea mentioned at the beginning of this section, namely to introduce a certain dose of a priori knowledge about the desired estimator. This aim can be achieved by means of a regularising function $g$ which reflects the faithfulness of the solution with respect to what is expected of $\theta$ . The likelihood $l$ reflects the faithfulness to the data. With this in mind, we look for estimators maximising the quantity $f = \lambda _ { 0 } l + \lambda _ { 1 } g$ , where $\lambda _ { 0 } + \lambda _ { 1 } = 1 .$ The scalars $\lambda _ { 0 }$ and $\lambda _ { 1 }$ D C C Dare Lagrange multipliers, accounting respectively for the relative importance of data fidelity and the relative importance of the a priori knowledge of $\theta$ . The Bayesian framework provides a natural probabilistic interpretation of this method. Indeed, the maximum of $\psi$ coincides with the maximum of $\log \psi$ , which can be written $\log \psi = \log l + \log \pi$ , a form which can be identified with $f$ . Many methods D Cfor finding estimators are based on this idea whenever the conventional methods fail. They are classified according to the nature of the regularising function, e.g., entropy maximum, Tikhonov regularisation, pseudo-inverse, etc., or the nature of its probabilistic interpretation in the Bayesian framework. Examples of these methods can be found elsewhere in this book. The difficulty is often to find the weighting by the multipliers $\lambda _ { 0 }$ and $\lambda _ { 1 }$ which leads to optimal estimators. Cross-validation is one approach that tackles this very problem.

# 9.6 From Data to Object: the Inverse Problem

In this section,12 we discuss the procedures for obtaining the best possible estimate of the observed object, using all the information available about the instrument used for the observation and about sources of noise intrinsic to the instrument or to the received signal, but also the information we possess concerning the source itself, which is generally not totally unknown. We use the term data to refer to the complete set of measured values resulting from the observation process. By taking into account all this information in a suitable way, not only is the object better reconstructed by data processing, but error bars affecting this reconstruction can be estimated. Figure 9.13 illustrates these procedures schematically.

The developments and tools described in the following can be applied to a very broad range of data types encountered in astrophysical observation: images with any format and at all wavelengths, spectra, polarisation rates as a function of frequency, and so on. However, in order to make the following more concrete and to illustrate it with examples, we have chosen to discuss only wavefront sensing and image processing, and to develop examples taken from the areas of adaptive optics, which began in the 1990s (see Sect. 6.3), and interferometry (see Sect. 6.4). Indeed, these two areas have considerably stimulated such processing techniques. Readers will then be able to adapt the ideas discussed here to other cases they may encounter in radioastronomy, high energy observation, etc.

![](images/bfeda1025597adbd3628625c60d84535d58cf85f0a7bfbc21e002b8ff20c6106.jpg)  
Fig. 9.13 Schematic view of the inverse problem and of the various solutions discussed in this section

# 9.6.1 Posing the Problem

# Forward Problem

Consider the following classic problem in physics. An initial object such as an electromagnetic wave propagates through a system that will affect it in some way, e.g., atmospheric turbulence, an instrument involving aberrations and diffraction, etc. We can deduce the properties of the output wave if we know all the properties of the system, such as would be included in a forward or direct model, or data formation model for this system. This is the basic principle of end-to-end models, discussed in Sect. 9.2.

This can be illustrated by wavefront sensing as carried out in adaptive optics, i.e., the measurement of aberrations intrinsic to the telescope or due to the passage through turbulent atmospheric layers, using a (Hartmann–Shack) wavefront sensor. The relevant physical quantity here is the phase $\varphi ( \boldsymbol { r } , t )$ on the exit pupil of the telescope, which contains all the information regarding the aberrations suffered by the wave. The measurement data are the average slopes of the phase in two perpendicular directions, viz., $\partial \phi ( \boldsymbol { r } , t ) / \partial x$ and $\partial \phi ( \boldsymbol { r } , t ) / \partial y$ , on each Hartmann–Shack subaperture, which can be recorded together in a vector i . The calculation of the slopes $_ i$ given the phase $\varphi$ is a classic forward problem in physics. It requires a choice of data formation model.

An end-to-end forward model includes models for data formation right up to detection, and even up to data storage when data are transmitted with compression. It thus takes into account photon noise, detector readout noise, digitiser quantisation noise, and data compression noise, if any (see Sect. 9.2).

# Inverse Problem

The problem here is work back up from the data to knowledge of the object that originated the data. This is called the inverse problem. It involves inverting the data formation model. Our senses and our brains solve such inverse problems all the time, analysing the information received, e.g., by the retina, and deducing positions in space, 3D shapes, and so on. This is also the most common situation for the observer in astronomy, who makes deductions from observations and attempts to conclude as accurately as possible about some set of properties of the source.

In physics, and especially in astronomy, the processing of experimental data thus consists in solving an inverse problem, in practice, after a data reduction or preprocessing stage which aims to correct for instrumental defects in such a way that the data can be correctly described by the chosen forward model (see Sect. 9.4).

Estimating (see Sect. 9.5) or working back up to the phase $\varphi$ from the slope vector $_ i$ is the inverse problem of Hartmann–Shack wavefront sensing. It involves inverting the corresponding data formation model.

Let us consider another example, taken from another spectral region. The $\gamma$ ray astronomy mission INTEGRAL (see Sect. 5.2.5) has three instruments capable of carrying out spectral analysis, namely, JEM-X, IBIS ISGRI+PICSIT, and SPI. Each of these can measure the spectrum of the observed source, here the black hole binary system Cygnus X-1. The data formation model is contained in a software called XSPEC, and an a priori model of the source containing a certain number of free parameters is injected into this. The simulated output of this software is then compared with measurements from each of the instruments, and the free parameters are fitted in the best possible way, in a sense to be made precise shortly, as shown in Fig. 9.14.

We shall see below that inversion can often take advantage of statistical knowledge regarding measurement error, generally modelled as noise. Naive inversion methods are often characterised by instability, in the sense that the inevitable measurement noise is amplified in an uncontrolled way during inversion, leading to an inacceptable solution. In this case, where the data alone are insufficient to obtain an acceptable solution, more sophisticated inversion methods, called regularised inversion methods, are brought to bear. They incorporate further constraints to impose a certain regularity on the solution, compatible with what is known $a$ priori about it. This is a key point: in data processing, we introduce supplementary information as dictated by our prior knowledge of the object. For example, a brightness can only take positive values, an object such as a stellar disk is bounded spatially by a contour, a temporal fluctuation cannot contain frequencies above a certain threshold, and so on.

![](images/e338e716c61557abab2c29554edc05b2500b409d78b65cda6c37e8c5e9a290c8.jpg)  
Fig. 9.14 Spectrum of the accreting binary system Cygnus X-1, viewed by the various instruments of the $\gamma$ -ray observatory INTEGRAL. The model fitted to the data is a hybrid model, in which electrons in the corona have a non-thermal distribution. From Cadolle-Bel M. et al., Soc. Fr. Astron. Astroph., Scientific Highlights 2006, p. 191

It is extremely productive to conceive of data processing explicitly as the inversion of a forward problem. To begin with, this forces us to model the whole data formation process, so that each step can be taken into account in the inversion. It also allows us to analyse existing methods, e.g., a typical deconvolution, or filtering, as discussed in Sect. 9.1.3, and to clearly identify the underlying assumptions, or the defects. It is then possible to conceive of methods that take advantage of knowledge concerning the data formation process as well as knowledge of the source or the relevant physical quantity, available a priori, i.e., before the measurements are made.

In the following, we discuss the basic notions and tools required to tackle the resolution of an inverse problem, a subject that has been deeply transformed by the advent of powerful computational tools. For the purposes of this textbook,13 the tools discussed are illustrated on several relatively simple, i.e., linear, inverse problems encountered in astronomy: wavefront reconstruction from measurements by a Hartmann–Shack sensor, adaptive optics corrected image restoration and multispectral image reconstruction in nulling interferometry (see Sect. 6.6). We shall not discuss extensions to non-linear problems, which do exist, however.

# 9.6.2 Well-Posed Problems

Let the relevant physical quantity be $o$ , referred to as the object in what follows. It could be the phase of the wave in the case of a wavefront sensor, a star or galaxy in the case of an image in the focal plane of a telescope, the spectrum of a quasar in the case of a spectrograph, etc. Let $i$ be the measured data.14 This could be the slopes measured by the Hartmann–Shack sensor, an image, a spectrum, etc. We shall consider for the moment that $o$ and $i$ are continuous quantities, i.e., functions of space, time, or both, belonging to Hilbert spaces denoted by $X$ and $Y$ .

The forward model, deduced from physics and from the known properties of the instrument, can be used to calculate a model of the data in the case of observation of a known object. This is what is done in a data simulation operation:

$$
i = H ( o ) .
$$

We shall restrict attention here to linear forward models, whence

$$
i = H o ,
$$

where $H$ is a continuous linear operator mapping $X$ into $Y$ . It was in this context that Hadamard15 introduced the concept of well-posed problems.

When the forward model is linear and translation invariant, e.g., for imaging by a telescope within the isoplanatic patch (see Sect. 6.2), $H$ is a convolution operator and there is a function $h$ called

the point spread function $( P S F )$ such that

$$
i = H o = h \star o .
$$

We seek to invert (9.71), i.e., to find $o$ for a given $i$ . We say that the problem is well posed in the sense of Hadamard if the solution $o$ satisfies the usual conditions for existence and uniqueness, but also the less well known condition of stability, i.e., the solution depends continuously on the data $i$ . In other words, a small change in the data — in practice, another realisation of the random noise — only brings about a small change in the solution. These three conditions, known as Hadamard’s conditions, are expressed mathematically in the following way:

• Existence. There exists $o \in X$ such that $i = H o$ , i.e., $i \in \operatorname { I m } ( H )$ , the image or range of $H$ .   
• Uniqueness. The kernel of $H$ contains only zero, i.e., $\operatorname { K e r } ( H ) = \{ 0 \}$ .   
• Stability. The inverse of $H$ on $\operatorname { I m } ( H )$ is continuous.

Note that for the stability condition the inverse of $H$ on $\operatorname { I m } ( H )$ , denoted by $H ^ { - 1 }$ , is well defined, because we assume that $\begin{array} { l l l } { \operatorname { K e r } ( H ) } & { = } & { \{ 0 \} } \end{array}$ . Note also that the stability condition is equivalent to requiring the set $\operatorname { I m } ( H )$ gto be closed, i.e., $\operatorname { I m } ( H ) = { \dot { \overline { { \operatorname { I m } ( H ) } } } }$ .

DFor many inverse problems, even the first two of these conditions are not satisfied, let alone the third. Indeed, on the one hand $\operatorname { I m } ( H )$ is the set of possible images when there is no noise, a smaller set than the space of noisy data to which $i$ belongs. For example, in imaging, $\operatorname { I m } ( H )$ is a vector space that contains no frequency greater than the optical cutoff frequency of the telescope $( D / \lambda )$ , whereas the noise will contain such frequencies. In general, the existence of a solution is therefore not guaranteed. On the other hand, the kernel of $H$ contains all objects unseen by the instrument. So for a Hartmann–Shack sensor, these are the unseen spatial modes, e.g., described in terms of Zernike polynomials, such as the piston mode $( Z _ { 1 } )$ or the so-called waffle mode. For an imager, these are the spatial frequencies of the object above the optical cutoff frequency of the telescope. The kernel is therefore generally not just $\{ 0 \}$ and uniqueness is not granted.

f gThe mathematician Nashed introduced the idea of a well-posed problem in the sense of least squares, which provides a way to ensure existence (in practice) and uniqueness of the solution and then to show that inversion in the least squares sense does not lead to a good solution of the inverse problem owing to its instability, also called non-robustness to noise.16 It thus remains ill-posed.

We say that $\hat { o } _ { \mathrm { L S } }$ is a least-squares solution to the problem (9.71) if

$$
\| i - H \hat { o } _ { \mathrm { L S } } \| ^ { 2 } = \operatorname* { i n f } _ { o } \| i - H o \| ^ { 2 } ,
$$

where $\parallel \parallel$ is the Euclidean or $L _ { 2 }$ norm. Nashed then showed the following:

• Existence. A least-squares solution exists if and only if $i \in \operatorname { I m } ( H ) + \operatorname { I m } ( H ) ^ { \perp }$ . This condition is always satisfied if $\operatorname { I m } ( H )$ is closed.

• Uniqueness. If several solutions exist, we choose the unique solution with minimal norm, i.e., we project the solution on to the orthogonal complement $\operatorname { K e r } ( H ) ^ { \perp }$ of the kernel. We denote this by $H ^ { \dagger } i$ , and call it the generalised inverse. The operator $H ^ { \dagger }$ associates the least-squares solution of $i ~ = ~ H o$ of minimal norm, i.e., the only solution in $\operatorname { K e r } ( H ) ^ { \perp }$ , to all $i \in \operatorname { I m } ( H ) + \operatorname { I m } ( H ) ^ { \perp }$ .

Moreover, it can be shown that $H ^ { \dagger }$ is continuous if and only if $\operatorname { I m } ( H )$ is closed.

We say that the problem (9.71) is well-posed in the least-squares sense if there exists a unique least-squares solution (with minimal norm) and it is stable, i.e., it depends continuously on the data $i$ . We then see that the problem (9.71) is indeed well posed in the sense of least squares if and only if $H ^ { \dagger }$ is continuous, i.e., if and only if $\operatorname { I m } ( H )$ is closed. And for many operators, e.g., when $H$ is the convolution with a square-integrable response $h$ , this condition is not satisfied.

We can understand the meaning of such a solution intuitively by characterising the least-squares solutions. Let $H$ be a continuous linear operator from a Hilbert space $X$ to the Hilbert space $Y$ . Then the following three propositions are equivalent:

1. $\begin{array} { r } { \| i - H \hat { o } _ { \mathrm { L S } } \| ^ { 2 } = \operatorname* { i n f } _ { o \in X } \| i - H o \| ^ { 2 } } \end{array}$ :   
2. $H ^ { * } H \hat { o } _ { \mathrm { L S } } = H ^ { * } i$ 2 k, where $H ^ { * }$ kis the adjoint of $H$ (normal equation).   
3. $H \hat { o } _ { \mathrm { L S } } = P i$ , where $P$ is the (orthogonal) projection operator of $Y$ on $\overline { { \mathrm { I m } ( H ) } }$ .

In particular, characterisation (3) tells us that the least-squares solution exactly solves the original equation (9.71) when the data $i$ are projected onto the (closure of the) set of all possible data in the absence of noise, i.e., $\overline { { \mathrm { I m } ( H ) } }$ .

In finite dimensions, i.e., for all practical (discretised) problems, a vector subspace is always closed. As a consequence, we can be sure of both the existence and the continuity of the generalised inverse. However, the ill-posed nature of the continuous problem does not disappear by discretisation. It simply looks different: the mathematical instability of the continuous problem, reflected by the non-continuity of the generalised inverse in infinite dimensions, resurfaces as a numerical instability of the discretised problem. The discretised inverse problem in finite dimensions is ill-conditioned, as we shall explain shortly. The conditioning of a discretised inverse problem characterises the robustness to noise during inversion. It is related to the dynamic range of the eigenvalues of $H ^ { * } H$ (a matrix in finite dimensions), and worsens as the dynamic range increases.

# 9.6.3 Conventional Inversion Methods

In the following, we shall assume that the data, which have been digitised (see Sect. 9.1.3), are discrete, finite in number, and gathered together into a vector $_ i$ . In imaging, for an image of size $N \times N$ , $_ i$ is a vector of dimension $N ^ { 2 }$ which concatenates the rows or the columns of the image (in a conceptual rather than computational sense).

The first step in solving the inverse problem is to discretise also the sought object $\pmb { o }$ by expanding it on to a finite basis, that is, a basis of pixels or cardinal sine functions for an image, or a basis of Zernike polynomials for a phase representing aberrations. The model relating $\pmb { o }$ and $_ i$ is thus an approximation to the continuous forward model of (9.70) or (9.71). By explicitly incorporating the measurement errors in the form of additive noise $\pmb { n }$ (a vector whose components are random variables), this can be written

$$
\pmb { i } = H ( \pmb { o } ) + \pmb { n } ,
$$

in the general case, and

$$
\pmb { i } = H \pmb { o } + \pmb { n } ,
$$

in the linear case, where $H$ is a matrix. In the special case where $H$ represents a discrete convolution, the forward model can be written

$$
i = h \star o + n ,
$$

where $\pmb { h }$ is the PSF of the system and $\star$ denotes the discrete convolution.

Note that, in the case of photon noise, the noise is not additive in the sense that it depends on non-noisy data $H o$ . Equation (9.74) then abuses notation somewhat.17

# Least-Squares Method

The most widely used method for estimating the parameters $\pmb { o }$ from the data $_ i$ is the least-squares method. The idea is to look for $\hat { \pmb { o } } _ { \mathrm { L S } }$ which minimises the mean squared deviation between the data $_ i$ Oand the data model $H ( o )$ :

$$
\hat { \pmb { o } } _ { \mathrm { L S } } = \arg \operatorname* { m i n } _ { \pmb { o } } \| \pmb { i } - \pmb { H } ( \pmb { o } ) \| ^ { 2 } ,
$$

where arg min is the argument of the minimum and $\parallel \parallel$ is the Euclidean norm. k kThis method was first published by Legendre18 in 1805, and was very likely discovered by Gauss19 a few years earlier but without publishing. Legendre used the

least-squares method to estimate the ellipticity of the Earth from arc measurements, with a view to defining the metre.

When the measurement model is linear and given by (9.75), the solution is analytic and can be obtained by setting the gradient of the criterion (9.77) equal to zero:

$$
H ^ { \mathrm { T } } H \hat { \pmb { \ o } } _ { \mathrm { L S } } = H ^ { \mathrm { T } } \pmb { i } .
$$

If $H ^ { \mathrm { T } } H$ can be inverted, i.e., if the rank of the matrix $H$ is equal to the dimension of the unknown vector $\mathbf { \delta } _ { \pmb { o } }$ , then the solution is unique and given by

$$
\begin{array} { r } { \hat { \pmb \sigma } _ { \mathrm { L S } } = \left( H ^ { \mathrm { T } } H \right) ^ { - 1 } H ^ { \mathrm { T } } \pmb { i } . } \end{array}
$$

Otherwise, as in infinite dimension (see Sect. 9.6.2), there are infinitely many solutions, but only one of them has minimal norm (or ‘energy’). This is the generalised inverse, written $H ^ { \dagger } i$ .

# Relation Between Least Squares and Inverse Filter

When the image formation process can be modelled by a convolution, the translation invariance of the imaging leads to a particular structure of the matrix $H$ . This structure is approximately the structure of a circulant matrix (for a 1D convolution), or block circulant with circulant blocks (for a 2D convolution). In this approximation, which amounts to making the PSF $\pmb { h }$ periodic, the matrix $H$ is diagonalised by discrete Fourier transform (DFT), which can be calculated by an FFT algorithm, and its eigenvalues are the values of the transfer function $\tilde { h }$ (defined as the DFT of $\pmb { h }$ ). The minimal norm least-squares solution of the last section can then be written in the discrete Fourier domain:20

$$
\tilde { \partial } _ { \mathrm { L S } } ( \boldsymbol { u } ) = \frac { \tilde { h } ^ { * } ( \boldsymbol { u } ) \tilde { i } ( \boldsymbol { u } ) } { | \tilde { h } ( \boldsymbol { u } ) | ^ { 2 } } = \frac { \tilde { i } } { \tilde { h } } ( \boldsymbol { u } ) \qquad \forall \boldsymbol { u } \ \mathrm { s u c h ~ t h a t } \ \tilde { h } ( \boldsymbol { u } ) \neq 0 , \quad \mathrm { a n d } \ 0 \ \mathrm { i f } \ \tilde { h } ( \boldsymbol { u } ) = 0 ,
$$

where the tilde represents the discrete Fourier transform. In the case of a convolutive data model, the least-squares solution is thus identical to the inverse filter, up to the above-mentioned approximation.

# Maximum Likelihood Method

In the least-squares method, the choice of a quadratic measure of the deviation between the data $_ i$ and the data model $H ( o )$ is only justified by the fact that the solution can then be obtained by analytical calculation. Furthermore, this method makes no use whatever of any knowledge one may possess about the statistical properties of the noise. But this information about the noise can be used to interpret the least-squares method, and more importantly to extend it.

We model the measurement error $\pmb { n }$ as noise with probability distribution $p _ { \mathrm { n } } ( \pmb { n } )$ . According to (9.74), the distribution of the data $_ i$ conditional to the object, i.e., for a given object o (hence supposed known), is then21

$$
p ( i | \pmb { o } ) = p _ { \mathrm { n } } \big ( i - H ( \pmb { o } ) \big ) .
$$

Equation (9.81) can be used to draw realisations of noisy data knowing the object, i.e., to simulate data. On the other hand, in an inverse problem, one has only one realisation of the data, namely those actually measured, and the aim is to estimate the object. The maximum likelihood (ML) method consists precisely in reversing the point of view on $p ( i | o )$ by treating $\mathbf { \delta } _ { \pmb { o } }$ as variable, with $_ i$ fixed equal to the data, and seeking the object $\pmb { o }$ j that maximises $p ( i | o )$ . The quantity $p ( i | o )$ viewed as a function of $\pmb { o }$ j jis then called the likelihood of the data, and the object $\hat { \pmb { o } } _ { \mathrm { M L } }$ which Omaximises it is the one which makes the actually observed data the most likely:22

$$
{ \hat { \pmb { o } } } _ { \mathrm { M L } } = \arg \operatorname* { m a x } _ { \pmb { o } } p ( i | \pmb { o } ) .
$$

The most widely used model for noise is without doubt the centered (i.e. zero mean) Gaussian model, characterised by its covariance matrix $C _ { \mathrm { n } }$ :

$$
p ( i | o ) \propto \exp \left\{ - \frac { 1 } { 2 } \big [ i - H ( o ) \big ] ^ { \mathrm { T } } C _ { \mathrm { n } } ^ { - 1 } \big [ i - H ( o ) \big ] \right\} .
$$

The noise is called white noise (see Appendix B) if its covariance matrix is diagonal. If this matrix is also proportional to the identity matrix, then the noise is called stationary or homogeneous (white noise). The readout noise of a CCD detector (see Sect. 7.4.6) is often modelled by such a stationary centered Gaussian noise. Photon noise is white, but it has a Poisson distribution (see Appendix B), which can be shown, for high fluxes, to tend towards a non-stationary Gaussian distribution with variance equal to the signal detected on each pixel.

Maximising the likelihood is obviously equivalent to minimising a criterion defined to be the negative of the logarithm of the likelihood and called the neg-log-likelihood:

$$
J _ { i } ( \pmb { \sigma } ) = - \ln p ( i | \pmb { \sigma } ) .
$$

In the case of Gaussian noise, the neg-log-likelihood is

$$
J _ { i } ( \pmb { o } ) = \frac { 1 } { 2 } \big [ i - H ( \pmb { o } ) \big ] ^ { \mathrm { T } } C _ { \mathrm { n } } ^ { - 1 } \big [ i - H ( \pmb { o } ) \big ] .
$$

If the noise is also white, we have

$$
J _ { i } ( \pmb { o } ) = \frac { 1 } { 2 } \sum _ { k } \frac { | i ( k ) - H ( \pmb { o } ) ( k ) | ^ { 2 } } { \pmb { \sigma } _ { \mathrm { n } } ^ { 2 } ( k ) } ,
$$

where ${ \pmb \sigma } _ { \mathrm { n } } ^ { 2 } ( k )$ are the elements on the diagonal of the matrix $C _ { \mathfrak { n } }$ . $J _ { i } ( \pmb { o } )$ is a weighted least squares criterion. If the noise is also stationary with variance $\sigma _ { \mathrm { n } } ^ { 2 }$ , then $J _ { i } ( \pmb { \sigma } ) = \| i - H ( \pmb { \sigma } ) \| ^ { 2 } / 2 \sigma _ { \mathrm { n } } ^ { 2 }$ is precisely the ordinary, as opposed to weighted, least squares criterion.

The least squares method can thus be interpreted as a maximum likelihood method in the case of stationary white Gaussian noise. Conversely, if the noise distribution is known but different, the maximum likelihood method can take this knowledge of the noise into account and then generalises the least squares method.

# Example: Wavefront Reconstruction by the Maximum Likelihood Method

Consider a Hartmann–Shack wavefront sensor that measures aberrations due to atmospheric turbulence on a ground-based telescope. The phase at the exit pupil is expanded on a basis of Zernike polynomials $Z _ { k }$ , the degree of which is necessarily limited in practice to some maximal value $k _ { \mathrm { m a x } }$ :

$$
\varphi ( x , y ) = \sum _ { k = 1 } ^ { k _ { \mathrm { m a x } } } o _ { k } Z _ { k } ( x , y ) .
$$

We thus seek $\pmb { o }$ , the set of coefficients $o _ { k }$ of this expansion, by measuring the average slopes and inserting them into a measurement vector $_ i$ . The data model is precisely (9.75), viz., $i = H \pmb { \sigma } + \pmb { n }$ , where $H$ is basically the differentiation operator and is D Cknown as the interaction matrix.

In the simulation presented below, the sensor contains $2 0 \times 2 0$ subapertures of which only 276 receive light, owing to a central obstruction of $33 \%$  by the secondary mirror. This gives 552 slope measurements. The true turbulent phase $\varphi$ is a linear combination of $k _ { \mathrm { m a x } } = 8 6 1$ Zernike polynomials, drawn from a Kolmogorov distribution. The matrix $H$ Dthus has dimensions $5 5 2 \times 8 6 1$ . The noise on the slopes is stationary white Gaussian noise with variance equal to the variance of the non-noisy slopes, implying a signal-to-noise ratio of 1 on each measurement. Under such conditions, the maximum likelihood estimate of the phase is identical to the least squares solution (see last subsection). The matrix $H ^ { \mathrm { T } } H$ in (9.79) has dimensions $k _ { \mathrm { m a x } } \times k _ { \mathrm { m a x } }$ and cannot be inverted because we only have 552 measurements. The generalised inverse solution cannot be used because it is completely dominated by noise. A remedy often adopted here is to reduce the dimension $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } }$ of the space of unknowns $\mathbf { \delta } _ { \pmb { o } }$ during reconstruction of the wavefront. This remedy is one of the known regularisation methods, referred to as regularisation by dimension control. An example of reconstruction for different values of $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } }$ is shown in Fig. 9.15.

For $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } } = 2 1 0$ max , a value well below the number of measurements, the reconstructed phase Dis already unacceptable. The particular shape is due to the fact that the telescope has a central obstruction, whence there are no data at the centre of the pupil.

![](images/5d0d52d8e9b33b86571ea0aae03f3196b743f1df96912e23b466af198d06d7dc.jpg)  
Fig. 9.15 Wavefront sensing on a pupil. Top left: Simulated phase (called true phase). Other figures: Phases reconstructed by maximum likelihood (ML) by varying the number of reconstructed modes

This example clearly illustrates the case where, although the matrix $H ^ { \mathrm { T } } H$ can be inverted, it is ill-conditioned, i.e., it has eigenvalues very close to 0, leading to uncontrolled noise amplification.

Truncating the solution space to lower values of $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } }$ produces more reasonable solutions, but on the one hand the optimal choice of $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } }$ depends on the levels of turbulence and noise and this adjustment is difficult to achieve in practice, while on the other hand this truncation introduces a modelling error, since it amounts to neglecting all the components of the turbulent phase beyond $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } }$ . We shall see below how the introduction of a priori knowledge regarding the spatial regularity of the phase (Kolmogorov spectrum) can lead to a better solution without this ad hoc reduction of the space of unknowns.

# Interpreting the Failure of Non-Regularised Methods

The failure of the maximum likelihood method illustrated in the above example may seem surprising given the good statistical properties of this method, which is an estimator that converges towards the true value of the parameters when the number of data tends to infinity, which is asymptotically efficient, etc. However, these good properties are only asymptotic, i.e., they only concern situations where there is good statistical contrast, defined simply as the ratio of the number of measurements to the number of unknowns.

In practice, and in particular in the previous example, the problem is often to estimate a number of parameters of the same order of magnitude as the number of measurements, and sometimes greater, in which case these asymptotic properties are of little help. In this commonly encountered situation of unfavourable statistical contrast, the inversion is unstable, i.e., highly sensitive to noise, which can often be interpreted as arising due to the ill-posed nature of the underlying infinite dimensional problem.

Image restoration is another typical case of this situation. Obviously, for an image containing $N \times N$ pixels, we try to reconstruct an object of the same size, and if we increase the image size, we also increase the number of unknown parameters relating to the object, without improving the statistical contrast, which remains of order unity. We have seen that the least-squares solution was in this case given by the inverse filter, and we know that this is highly unstable with regard to noise. This instability is easily understood by reinserting the measurement equation (9.76), in the Fourier domain, into the solution (9.80):

$$
\tilde { \hat { \pmb { o } } } _ { \mathrm { L S } } = \frac { \tilde { i } } { \tilde { h } } = \tilde { \pmb { o } } + \frac { \tilde { { \pmb { m } } } } { \tilde { h } } .
$$

According to this, it is clear that the noise is highly amplified for all frequencies for which the value of the transfer function $\widetilde { h }$ is close to zero. One way to reduce noise amplification would be to modify (9.80) and divide $\widetilde { i }$ by $\tilde { h }$ only for frequencies $\pmb { u }$ where the transfer function $\widetilde { h }$ is not too small. This is also a form of regularisation by controlling the dimension of the solution, very similar to the choice of $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } }$ when reconstructing a wavefront, and it suffers from the same ad hoc character and the same difficulty in its tuning.

To sum up, simple inversion methods like least squares or maximum likelihood only give satisfactory results if there is good statistical contrast. For example, maximum likelihood can be successfully applied to problems like image registration, where we seek a 2D vector in order to register two images comprising a large number of pixels. More generally, it applies to the search for the few variables of a parsimonious parametric model from a large enough data set, e.g., estimating a star’s diameter from visibilities in optical interferometry, estimating the Earth’s ellipticity from arc measurements, etc.

In many problems where the statistical contrast is not favourable, the problem is ill-conditioned and regularisation, i.e., the addition during inversion of a priori knowledge and constraints on the solution, becomes highly profitable, as we shall now show.

# 9.6.4 Inversion Methods with Regularisation

Regularisation of an inverse problem corresponds to the idea that the data alone cannot lead to an acceptable solution, so that a priori information about the regularity of the considered observed object must necessarily be introduced. Here the term regularity implies that, for physical reasons intrinsic to the object, it must have certain properties, or obey certain rules regarding sign, size, or frequency, for example. The solution then results from a compromise between the requirements of the object’s postulated regularity and of the data fidelity.

Indeed, several very different solutions, some very poor and some rather good, may be compatible with the data. For instance, in the previous example of wavefront reconstruction, the true and reconstructed phases for $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } } ~ = ~ 2 1 0$ (Fig. 9.15) give very similar likelihood values, whence Dthey are both faithful to the data. In addition, the smoother, more regular solution obtained for $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } } = 5 5$ is less well fitted, i.e., less faithful to the data than the one obtained for $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } } = 2 1 0$ D Dsince it was obtained by optimising in fewer degrees of freedom, and yet it is much closer to the true phase.

# Bayesian Estimation and the Maximum a Posteriori (MAP) Estimator

Bayesian estimation, presented briefly here, provides a natural way of combining the information brought by measurements and information available a priori. Let us assume that we have expressed our a priori knowledge of the observed object in the form of a probability distribution $p ( \pmb { o } )$ , called the a priori distribution. The idea is not to assume that the observed object really is the realisation of a random phenomenon with distribution $p ( \pmb { o } )$ . This distribution is simply taken to be representative of our a priori knowledge, i.e., it takes small values for reconstructed objects that would be barely compatible with the latter and larger values for highly compatible objects.

The Bayes rule23 provides a way of expressing the probability $p ( \pmb { o } \mid i )$ for the object $\pmb { o }$ that is conditional upon the measurement data $_ i$ jas a function of the prior probability distribution $p ( \pmb { o } )$ of the object and the probability $p ( i \mid o )$ of the jmeasurements conditional upon the object. The latter contains our knowledge of the data formation model, including the noise model. This probability $p ( \pmb { o } \mid i )$ is jcalled the posterior distribution, since it is the probability of the object given the results of the measurements. The Bayes rule is (see Sect. 9.5)

$$
p ( \pmb { \mathscr { o } } \mid i ) = \frac { p ( i \mid \pmb { \mathscr { o } } ) \times p ( \pmb { \mathscr { o } } ) } { p ( i ) } \propto p ( i \mid \pmb { \mathscr { o } } ) \times p ( \pmb { \mathscr { o } } ) .
$$

Using the last expression, how should we choose the reconstructed object $\hat { \pmb { o } }$ that Owould best estimate the true object? One commonly made choice is the maximum a posteriori (MAP) estimator. The idea is to define as solution the object that maximises the posterior distribution $p ( \pmb { o } | i )$ , so that

$$
\sigma _ { \mathrm { M A P } } = \arg \operatorname* { m a x } _ { o } p ( o \mid i ) = \arg \operatorname* { m a x } _ { o } p ( i \mid o ) \times p ( o ) .
$$

This is the most likely object given the data and our prior knowledge. The posterior distribution, viewed as a function the object, is called the posterior likelihood. Through (9.89), it takes into account the measurement data $_ i$ , the data formation model, and any prior knowledge of the object. In particular, it should be noted that, when the prior distribution $p ( \pmb { o } )$ is constant, i.e., when we have no information about the object, the MAP estimator reduces to the maximum likelihood method.

It can be shown that choosing the MAP estimator amounts to minimising the mean risk (see Sect. 9.5) for a particular cost function called the all-or-nothing cost function. However, this goes beyond the scope of this introduction to inverse problems. Other choices of cost function, such as a choice of $\hat { \pmb { o } }$ minimising the mean squared error with respect to the true object $\mathbf { \delta } _ { \pmb { o } }$ Ounder the posterior probability distribution, can also be envisaged, but they generally lead to longer computation times for obtaining the solution.24

# Equivalence with Minimisation of a Regularised Criterion

Maximising the posterior likelihood is equivalent to minimising a criterion $J _ { \mathrm { M A P } } ( \pmb { o } )$ defined as minus its logarithm. According to (9.90), this criterion can be written as the sum of two terms, viz.,

$$
J _ { \mathrm { M A P } } ( o ) = - \ln p ( i \mid o ) - \ln p ( o ) = J _ { \mathrm { i } } ( o ) + J _ { \mathrm { o } } ( o ) ,
$$

where $J _ { \mathrm { i } }$ is the data fidelity criterion deduced from the likelihood [see (9.84)], which is often a least-squares criterion, while $J _ { \mathrm { o } } ( \pmb { o } ) \triangleq - \ln p ( \pmb { o } )$ is a regularisation or penalisation criterion (for the likelihood) which reflects faithfulness to prior knowledge.

The expression for the MAP solution as the object that minimises the criterion (9.91) shows clearly that it achieves the compromise between faithfulness to the data and faithfulness to prior knowledge asserted at the beginning of this section.

When $\pmb { o }$ is not a realisation of a random phenomenon with some probability distribution $p ( \pmb { o } )$ , e.g., in the case of image restoration, $J _ { \mathrm { o } } ( \pmb { o } )$ generally includes a multiplicative factor called the regularisation coefficient or hyperparameter.25 Its value controls the exact position of the compromise. Unsupervised, i.e., automatic, fitting methods exist for this coefficient, but they go beyond the scope of this introductory account.26

# The Linear and Gaussian Case. Relation with the Wiener Filter

Here we consider the case where the data model is linear [see (9.75)], the noise is assumed to be Gaussian, and the prior probability distribution adopted for the object is also Gaussian,27 with mean $\overline { { \pmb { o } } }$ and covariance matrix $C _ { 0 }$ :

$$
p ( \pmb { \sigma } ) \propto \exp \left[ - \frac { 1 } { 2 } ( \pmb { o } - \overline { { \pmb { o } } } ) ^ { \mathrm { T } } C _ { \circ } ^ { - 1 } ( \pmb { o } - \overline { { \pmb { o } } } ) \right] .
$$

Using (9.85), we see that the criterion to minimise in order to obtain the MAP solution is

$$
J _ { \mathrm { M A P } } ( \boldsymbol { o } ) = \frac { 1 } { 2 } ( \dot { \iota } - H \boldsymbol { o } ) ^ { \mathrm { T } } C _ { \mathrm { n } } ^ { - 1 } ( \dot { \iota } - H \boldsymbol { o } ) + \frac { 1 } { 2 } ( \boldsymbol { o } - \overline { { \boldsymbol { o } } } ) ^ { \mathrm { T } } C _ { \circ } ^ { - 1 } ( \boldsymbol { o } - \overline { { \boldsymbol { o } } } ) .
$$

This criterion is quadratic in $\pmb { o }$ and thus has analytic minimum, obtained by setting the gradient equal to zero:

$$
\begin{array} { r } { \hat { \boldsymbol \sigma } _ { \mathrm { M A P } } = \left( H ^ { \mathrm { T } } C _ { \mathrm { n } } ^ { - 1 } H + C _ { \mathrm { o } } ^ { - 1 } \right) ^ { - 1 } \left( H ^ { \mathrm { T } } C _ { \mathrm { n } } ^ { - 1 } \boldsymbol { i } + C _ { \mathrm { o } } ^ { - 1 } \overline { { \boldsymbol \sigma } } \right) . } \end{array}
$$

Several remarks can throw light upon this otherwise slightly dull looking result. To begin with, the maximum likelihood solution is obtained by taking $C _ { \mathrm { o } } ^ { - 1 } = 0$ in Dthis equation. Incidentally, this shows that this solution corresponds in the Bayesian framework to assuming an infinite energy for $\mathbf { \delta } _ { \pmb { o } }$ . Then if we also take $C _ { \mathrm { n } }$ proportional to the identity matrix, we see that we recover precisely the least-squares solution of (9.79).

Finally, the case of deconvolution is particularly enlightening. The noise is assumed stationary with power spectral density (PSD) $S _ { \mathrm { n } }$ , while the prior probability distribution for the object is also assumed stationary with PSD $S _ { \mathrm { o } }$ . For all the relevant quantities, we make the same periodicity approximation as on p. 583 when examining the relation between least squares and inverse filter. All the matrices in (9.94) are then diagonalised in the same discrete Fourier basis, and the solution can be written in this basis, with ordinary rather than matrix multiplications and inverses:

$$
\tilde { \partial } _ { \mathrm { M A P } } ( u ) = \frac { \tilde { h } ^ { * } ( u ) } { | \tilde { h } | ^ { 2 } ( u ) + S _ { \mathrm { n } } / S _ { \mathrm { o } } ( u ) } \tilde { i } ( u ) + \frac { S _ { \mathrm { n } } / S _ { \mathrm { o } } ( u ) } { | \tilde { h } | ^ { 2 } ( u ) + S _ { \mathrm { n } } / S _ { \mathrm { o } } ( u ) } \tilde { \overline { { \sigma } } } ( u ) .
$$

In this expression, $S _ { \mathrm { n } } / S _ { \mathrm { o } } ( { \pmb u } )$ is the reciprocal of a signal-to-noise ratio at the spatial frequency $\pmb { u }$ and $\tilde { \mathbf { \Gamma } }$ is the Fourier transform of the a priori object, generally taken to be zero or equal to an object of constant value.

This expression is just the Wiener filter (see Sect. 9.1.3) for the case where the a priori object is not zero. For frequencies where the signal-to-noise ratio is high, this solution tends toward the inverse filter, and for frequencies where this ratio is low, the solution tends toward the a priori object. It can even be seen that, at each spatial frequency $\pmb { u }$ , the solution is on a segment that connects the maximum likelihood solution (inverse filter) to the a priori solution, with the position on the segment given by the signal-to-noise ratio:

$$
\tilde { \sigma } _ { \mathrm { M A P } } ( \boldsymbol { u } ) = \alpha \frac { \tilde { i } { ( \boldsymbol { u } ) } } { \tilde { h } } + ( 1 - \alpha ) \tilde { \bar { \sigma } } ( \boldsymbol { u } ) ,
$$

where

$$
\alpha = \frac { | \tilde { \pmb { h } } | ^ { 2 } ( \pmb { u } ) } { | \tilde { \pmb { h } } | ^ { 2 } ( \pmb { u } ) + S _ { \mathrm { n } } / S _ { 0 } ( \pmb { u } ) } .
$$

This expression clearly illustrates the fact that regularisation achieves a compromise between bias and variance that enables us to reduce the estimation error. The mean squared error on the estimated object is the square root of the sum of the squared bias and the variance of the estimator. The solution of the inverse filter (obtained for $S _ { \mathrm { n } } / S _ { \mathrm { o } } ~ = ~ 0 )$ has zero bias but amplifies the noise in an uncontrolled way, Di.e., has unbounded variance. Compared with the maximum likelihood solution, the solution (9.95) is biased toward the a priori solution $\overline { { \pmb { o } } }$ . By accepting this bias, we can significantly reduce the variance and globally reduce the mean squared error on the estimated object.

# Application to Wavefront Reconstruction

We return to the example of wavefront reconstruction from data provided by a Hartmann–Shack sensor, as discussed in Sect. 9.6.3. The noise is still assumed to be Gaussian and white with covariance matrix $C _ { \mathrm { n } } = \sigma ^ { 2 } I$ . We assume that the phase Dobeys Kolmogorov statistics and is therefore Gaussian, with known covariance matrix $C _ { 0 }$ , and depends only on the Fried parameter $r _ { 0 }$ which quantifies the strength of turbulence. The true phase has spatial variance $\sigma _ { \varphi } ^ { 2 } = 3 . 0 \ \mathrm { r a d } ^ { 2 }$ . The most likely Dphase given the measurements and taking into account this a priori information is the MAP solution given by (9.94). This solution is shown in Fig. 9.16. The estimation error corresponds to a spatial variance $\sigma _ { \mathrm { e r r } } ^ { 2 } = 0 . 7 ~ \mathrm { r a d } ^ { 2 }$ , which is lower than the Dbest solutions obtained previously by truncating the representation of the phase to a small number of Zernike polynomials $( \sigma _ { \mathrm { e r r } } ^ { 2 } = 0 . 8 \mathrm { r a d } ^ { 2 }$ , obtained for $k _ { \mathrm { m a x } } ^ { \mathrm { r e c } } = 5 5$ ).

![](images/30cefda75073c746e068fbb9c88458d40198220b5437d616139a26fac0e4c9e5.jpg)  
Fig. 9.16 Comparing reconstructed phases on a pupil. Left: Simulated turbulent phase, to be estimated. Centre: Phase estimated by MAP. Right: Best phase estimated by maximum likelihood on a truncated basis

The MAP solution takes advantage of a priori knowledge of the spatial statistics of the turbulence. To use this in adaptive optics, where the sample rate is generally well above $1 / \tau _ { 0 }$ , it is judicious to opt for a natural extension of this estimator that also exploits a priori knowledge of the temporal statistics of the turbulence. This extension is the optimal estimator of Kalman filtering.

# 9.6.5 Application to Adaptive Optics Imaging

Here we apply these tools to solve a specific inverse problem, namely, adaptive optics imaging. We shall illustrate with several examples, either by simulation or by the processing of genuine astronomical observations.

# Ingredients of the Deconvolution

Long exposure images corrected by adaptive optics (AO) must be deconvolved, because the correction is only partial. Considering that the PSF $\pmb { h }$ is known, the object $ { \hat { \mathbf { o } } } _ { \mathrm { M A P } }$ estimated by MAP is given by (9.90), i.e., it minimises the criterion O(9.91). Let us see how to define the two components of this criterion.

To be able to measure objects with high dynamic range, which are common in astronomy, the data fidelity term $J _ { \mathrm { i } }$ must incorporate a fine model of the noise, taking into account both photon noise and electronic noise. This can be done by treating the photon noise as a non-stationary Gaussian noise, and it leads to a weighted leastsquares criterion $J _ { \mathrm { i } }$ [see (9.86)] rather than an ordinary least-squares term.

For objects with sharp edges, such as artificial satellites, asteroids, or planets, a Gaussian prior (like the one leading to the Wiener filter on p. 590), or equivalently, a quadratic regularisation criterion, tends to smooth the edges and introduce spurious oscillations or ringing in their vicinity. One interpretation of this effect is that, when minimising the criterion $J _ { \mathrm { M A P } } ( \pmb { o } )$ , a quadratic regularisation attributes to a step a cost proportional to the square of its value, e.g., at the edge of an object, where there is a large difference in value between adjacent pixels. One solution is then to use an edge-preserving criterion, such as the so-called quadratic–linear or $L _ { 2 } L _ { 1 }$ criteria. These are quadratic for small discontinuities and linear for large ones. The quadratic part ensures good noise smoothing and the linear part cancels edge penalisation.

In addition, for many different reasons, we are often led to treat the PSF $\pmb { h }$ as imperfectly known. Carrying out a classic deconvolution, i.e., assuming that the point spread function is known but using an incorrect point spread function, can lead to disastrous results. Conversely, a so-called blind deconvolution, where the same criterion (9.91) is minimised but simultaneously seeking $\pmb { o }$ and $\pmb { h }$ , is highly unstable, rather like unregularised methods. A myopic deconvolution consists in jointly estimating both $\mathbf { \delta } _ { \pmb { o } }$ and $\pmb { h }$ in a Bayesian framework with a natural regularisation for the point spread function and without having to fit an additional hyperparameter. The joint MAP estimator is given by

$$
\begin{array} { l } { { ( \hat { o } , \hat { h } ) = \mathop { \arg \operatorname* { m a x } } _ { o , h } p ( o , h | i ) = \mathop { \arg \operatorname* { m a x } } _ { o , h } p ( i | o , h ) \times p ( o ) \times p ( h ) } } \\ { { \qquad = \mathop { \arg \operatorname* { m i n } } _ { o , h } \Big [ J _ { i } ( o , h ) + J _ { o } ( o ) + J _ { h } ( h ) \Big ] , } } \end{array}
$$

where $J _ { h }$ is a regularisation criterion for $\pmb { h }$ , which introduces constraints on the possible variability of the PSF.

The next section presents experimental results obtained by the MISTRAL restoration method,28 which combines the three ingredients discussed above: fine noise modelling, non-quadratic regularisation, and myopic deconvolution.

# Image Restoration from Experimental Astronomical Data

Figure 9.17a shows a long exposure image of Ganymede, a natural satellite of Jupiter, corrected by adaptive optics. This image was made on 28/09/1997 on ONERA’s adaptive optics testbed installed on the $1 . 5 2 \mathrm { ~ m ~ }$ telescope at the Observatoire de Haute-Provence in France. The imaging wavelength is $\lambda \ : = \ : 0 . 8 5 \mathrm { \ : \mu m }$ and the exposure time is $1 0 0 \mathrm { s } .$ . The estimated total flux is $8 \times 1 0 ^ { 7 }$ Dphotons and the estimated ratio $D / r _ { 0 }$ is 23. The total field of view is 7.9 arcsec, of which only half is shown here. The mean and variability of the point spread function were estimated from recordings of 50 images of a bright star located nearby. Figures 9.17b and c show restorations obtained using the Richardson–Lucy algorithm (ML for Poisson noise), stopped after 200 and 3 000 iterations, respectively.29 In the first case, similar to restoration with quadratic regularisation, the restored image is somewhat blurred and displays ringing, while in the second, very similar to the result of inverse filtering, noise dominates the restoration.

![](images/fe7ae2e62165861695695fd41fdb326927e6f3cdfa9440e1778b58edca837550.jpg)  
Fig. 9.17 (a) Corrected image of Ganymede obtained using the ONERA adaptive optics testbed on 28 September 1997. (b) Restoration using the Richardson–Lucy algorithm, stopped after 200 iterations. (c) Likewise, but stopped after 3 000 iterations. From Mugnier, L. et al., Chap. 10 of Idier, J. op. cit.

![](images/2accd8889effe86b388cece322c64d243b1f59a0913b0dd64757d6402c58fcaf.jpg)  
Fig. 9.18 (a) Deconvolution of the Ganymede image in Fig. 9.17 by MISTRAL. (b) Comparison with a wide band synthetic image obtained using the NASA/JPL database. (c) The same synthetic image, but convolved by the perfect point spread function of a $1 . 5 2 \mathrm { m }$ telescope. From Mugnier, L.M. et al., MISTRAL: A myopic edge-preserving image restoration method, with application to astronomical adaptive-optics-corrected long-exposure images, J. Opt. Soc. Am. A 21, 1841–1854, 2004

Figure 9.18a shows a myopic deconvolution implementing an edge-preserving prior, while Fig. 9.18b is a wide band synthetic image obtained by a NASA/JPL space probe30 during a Ganymede flyby. Comparing the two, we find that many features of the moon are correctly restored. A fairer comparison consists in jointly examining the myopic deconvolution carried out by MISTRAL with the image of Fig. 9.18b convolved by the perfect PSF of a $1 . 5 2 \mathrm { ~ m ~ }$ telescope, as shown in Fig. 9.18c.

# 9.6.6 Application to Nulling Interferometry

We now discuss a second example of the inversion problem, this time relating to the detection of extrasolar planets by means of a nulling interferometer (see Sect. 6.6). With the Darwin instrument, or NASA’s Terrestrial Planet Finder Interferometer, both under study during the 2000s, data will be very different from an image in the conventional sense of the term, and their exploitation will require implementation of a specific reconstruction process. They will consist, at each measurement time $t$ , of an intensity in each spectral channel . This intensity can be modelled as the integral over a certain angular region of the instantaneous transmission map of the interferometer, denoted by $R _ { t , \lambda } ( \pmb \theta )$ , which depends on the time $t$ owing to rotation of the interferometer relative to the plane of the sky, multiplied by the intensity distribution $o _ { \lambda } ( \pmb \theta )$ of the observed object. The data model is thus linear, but notably non-convolutive, thus very different from the one used in imaging. The transmission map is a simple sinusoidal function in the case of a Bracewell interferometer, but becomes more complex when more than two telescopes interfere simultaneously.

By judiciously combining the data, and with asymmetrical transmission maps, the contribution to the measured signal of the components of the observed object with even spatial distribution can be eliminated. These components are stellar leakage, exozodiacal light, and a fortiori zodiacal light and thermal emission from the instrument itself (which have constant level in the field of view). It is then possible to seek out only planets during image reconstruction, which corresponds to the following object model:

$$
\pmb { o } _ { \lambda } ( \pmb { \theta } ) = \sum _ { k = 1 } ^ { N _ { \mathrm { s r c } } } F _ { k , \lambda } \delta ( \pmb { \theta } - \pmb { \theta } _ { k } ) ,
$$

where $N _ { \mathrm { s r c } }$ is the number of planets, assumed known here, and $F _ { k , \lambda }$ is the spectrum of the $k$ th planet in a spectral interval $[ \lambda _ { \operatorname* { m i n } } , \lambda _ { \operatorname* { m a x } } ]$ fixed by the instrument. This parametric model can substantially constrain the inversion in so as to counterbalance the fact that the data are distinctly poorer than an image.

With this model of the object, the data formation model is

$$
i _ { t , \lambda } = \sum _ { k = 1 } ^ { N _ { \mathrm { s r c } } } R _ { t , \lambda } ( \pmb \theta _ { k } ) F _ { k , \lambda } + n _ { t , \lambda } ,
$$

where $n _ { t , \lambda }$ is the noise, assumed to be white Gaussian, whose variance $\sigma _ { t , \lambda } ^ { 2 }$ can be estimated from the data and is assumed known here. The inverse problem to be solved is to estimate the positions $\pmb \theta _ { k }$ and spectra $F _ { k , \lambda }$ of the planets, these being grouped together into two vectors $( \pmb \theta , \pmb F )$ . The ML solution is the one that minimises the following weighted least-squares criterion, given the assumptions made about the noise:

$$
J _ { \mathrm { i } } ( \theta , F ) = \sum _ { t , \lambda } { \frac { 1 } { \sigma _ { t , \lambda } ^ { 2 } } } \left[ i _ { t , \lambda } - \sum _ { k = 1 } ^ { N _ { \mathrm { s r c } } } R _ { t , \lambda } ( \theta _ { k } ) F _ { k , \lambda } \right] ^ { 2 } .
$$

As we shall see from the reconstruction results, the inversion remains difficult under the high noise conditions considered here. The object model (9.98), separable into spatial and spectral variables, already contains all spatial prior information concerning the object. It is nevertheless possible to constrain the inversion even more by including the further knowledge that the spectra we seek are positive quantities (at all wavelengths), and furthermore that they are relatively smooth functions of the wavelength. The latter fact is taken into account by incorporating a spectral regularisation into the criterion to be minimised, which measures the roughness of the spectrum:

$$
J _ { \mathrm { o } } ( F ) = \sum _ { k = 1 } ^ { N _ { \mathrm { s r c } } } \mu _ { k } \sum _ { \lambda = \lambda _ { \mathrm { m i n } } } ^ { \lambda _ { \mathrm { m a x } } } \left( \frac { \partial ^ { m } F _ { k , \lambda } } { \partial \lambda ^ { m } } \right) ^ { 2 } ,
$$

where the $m$ th derivative of the spectrum $\mathbf { \Phi } _ { m } ~ = ~ 1$ or 2 in practice) is calculated by finite differences and where the $\mu _ { k }$ Dare hyperparameters used to adjust the weight allocated to the regularisation. The MAP solution is the one minimising the composite criterion $J _ { \mathrm { M A P } } ( \pmb \theta , \pmb F ) = J _ { \mathrm { i } } ( \pmb \theta , \pmb F ) + J _ { \mathrm { o } } ( \pmb F )$ . It is a rather delicate matter to D Cimplement this minimisation because there are many local minima. We use the fact that, for each assumed position $\pmb \theta$ of the planets, the MAP estimate of the spectra, $\hat { F } ( \pmb \theta )$ , can be obtained simply because $J _ { \mathrm { M A P } }$ is quadratic in the spectra $F$ . If the latter are replaced by $\hat { F } ( \pmb \theta ) ^ { 1 }$ in $J _ { \mathrm { M A P } }$ , we obtain a partially optimised function for minimisation, which now only depends explicitly on the positions:

$$
J _ { \mathrm { M A P } } ^ { \dagger } ( \pmb { \theta } ) = J _ { \mathrm { M A P } } \big [ \pmb { \theta } , \hat { \pmb { F } } ( \pmb { \theta } ) \big ] .
$$

This criterion is minimised by a sequential search for the planets, as in the CLEAN algorithm. Figure 9.19 shows the maps of $J _ { \mathrm { M A P } } ^ { \dagger }$ obtained for a single planet as a function of the prior information used. It is clear that the constraints of positivity and smoothness imposed on the spectra significantly improve estimates of the position of the planet, by discrediting (Fig. 9.19 right) positions compatible with the data (Fig. 9.19 left and centre) but corresponding to highly chaotic spectra.

Figure 9.20 shows the estimated spectrum of an Earth-like planet. As expected, spectral regularisation avoids noise amplification and has a beneficial effect on the estimate.

![](images/c4c308e051f9c1ea0782cd234ff9c3ec4a1887bea56f605d8a9b33e50d8432ba.jpg)  
Fig. 9.19 Likelihood maps for the position of a planet. Left: Likelihood alone. Centre: Likelihood under the constraint that spectra are positive. Right: MAP, i.e., likelihood penalised by a spectral regularisation criterion. The true position of the planet is at the bottom, slightly to the left, and clearly visible on the right-hand image. From Mugnier, L., Thiebaut, E., Belu, A., in ´ Astronomy with High Contrast Imaging III, EDP Sciences, Les Ulis, 2006, and also Thiebaut, E., Mugnier, L., ´ Maximum a posteriori planet detection with a nulling interferometer, in Proceedings IAU Conf. 200, Nice, 2006

![](images/6996ebf28dbc083f229007e258502a76b5da50162ef8f88a925d20faf5b9cc31.jpg)  
Fig. 9.20 Reconstructed spectrum at the estimated position of the planet. Red: Without regularisation. Green: With regularisation. Black: True spectrum of the Earth. Same reference as for Fig. 9.19

# Problems

Note. These exercises refer also to the subjects treated in Appendixes A and B.

9.1. In each of the three examples, use the Fourier transform on the left to deduce the one on the right. Fourier transform is indicated by an arrow:

$$
\begin{array} { l } { { \displaystyle { \frac { \sin x } { x } }  \pi \pi ( \pi s ) , ( \frac { \sin x } { x } ) ^ { 2 }  \Lambda ( \pi s ) , \ } } \\ { { \displaystyle { \mathrm { e } ^ { - x ^ { 2 } }  \sqrt { \pi } \mathrm { e } ^ { - \pi ^ { 2 } s ^ { 2 } } } , \qquad \delta ( a x )  \frac { 1 } { | a | } , \ } } \\ { { \displaystyle { \mathrm { e } ^ { - x ^ { 2 } / 2 \sigma ^ { 2 } }  \sqrt { 2 \pi \sigma } \mathrm { e } ^ { - 2 \pi ^ { 2 } \sigma ^ { 2 } s ^ { 2 } } } , \mathrm { e } ^ { \mathrm { i } x }  \delta ( s - \frac { 1 } { 2 \pi } ) . \ } } \end{array}
$$

9.2. Using the convolution theorem, give an expression for

$$
\mathbf { e } ^ { - a x ^ { 2 } } \star \mathbf { e } ^ { - b x ^ { 2 } } .
$$

(Problem 6.15 is an application of this result.)

Answer. The following property is used: the Fourier transform of a convolution product is the pointwise product of the Fourier transforms of the factors in that product. This property is very useful in numerical calculations, the algorithms for multiplication being so much more rapid. Linearity and similarity properties are also used in the following deduction:

$$
\begin{array} { r l } & { F ( x ) = \mathrm { e } ^ { - a x ^ { 2 } } \star \mathrm { e } ^ { - b x ^ { 2 } } } \\ & { \qquad = \mathrm { F T } \left[ \mathrm { F T } \left[ \mathrm { e } ^ { - a x ^ { 2 } } \right] \cdot \mathrm { F T } \left[ \mathrm { e } ^ { - b x ^ { 2 } } \right] \right] } \\ & { \qquad = \mathrm { F T } \left[ \sqrt { \cfrac { \pi } { a } } \mathrm { e } ^ { - x ^ { 2 } / a } \sqrt { \cfrac { \pi } { b } } \mathrm { e } ^ { - x ^ { 2 } / b } \right] } \\ & { \qquad = \frac { \pi } { \sqrt { a b } } \mathrm { F T } \left[ \exp \left( - \frac { a + b } { a b } x ^ { 2 } \right) \right] , } \end{array}
$$

so that, finally,

$$
F ( x ) = { \frac { \pi ^ { 3 / 2 } } { \sqrt { a + b } } } \exp \left( - { \frac { a b } { a + b } } x ^ { 2 } \right) .
$$

9.3. Prove the Wiener–Khinchine theorem: The autocorrelation and spectral density are a Fourier pair. Apply it to the case of a time-dependent electric current $i ( t )$ , and its Fourier transform $\tilde { i } ( \nu )$ , where $\nu$ is a temporal frequency, and thus interpret the theorem physically in terms of power.

9.4. Compare the FTs of the convolution and the correlation products of two functions.

9.5. A signal $X ( t )$ , whose spectrum has bounded support, passes through a linear filter which has instantaneous response $F ( t )$ . Let $Y ( t )$ be the output signal. $X ( t )$ and $Y ( t )$ are sampled, giving sequences of results $\{ X _ { i } \}$ and $\left\{ Y _ { i } \right\}$ . Show that

$$
\{ Y _ { i } \} = \{ I _ { i } \} \star \{ X _ { i } \} .
$$

How can the sequence $\left\{ I _ { i } \right\}$ be found?

9.6. Filtering by Running Mean (Smoothing). Let $x ( t ) = x _ { \mathrm { s } } + n ( t )$ be a signal, where $x _ { \mathrm { s } }$ is a constant to be determined, and $n ( t )$ D Cis the stationary random noise affecting the measurement, such that $\langle n ( t ) \rangle = 0$ . Define

$$
y _ { T } ( t ) = \frac { 1 } { T } \int _ { t } ^ { t + T } x ( \theta ) \mathrm { d } \theta ,
$$

which is called the running mean of $x ( t )$ . Put $y _ { T } ( t )$ into the form of a convolution, and deduce that it is the result of a linear filtering of $x ( t )$ . Determine the transfer function $\tilde { H } ( f )$ of this filter, and its equivalent bandpass $\Delta f$ defined by

$$
\Delta f = \int _ { - \infty } ^ { + \infty } | \tilde { H } ( f ) | ^ { 2 } \mathrm { d } f .
$$

Answer. An expression equivalent to the running mean is given, up to a translation by $T / 2$ , by

$$
y _ { T } ( t ) = x ( t ) \star { \frac { 1 } { T } } \varPi \left( { \frac { t } { T } } \right) .
$$

The running mean is therefore the result of linear filtering by the filter

$$
\tilde { H } ( f ) = \mathrm { s i n c } ( T f ) ,
$$

and so, by Parseval’s theorem,

$$
\Delta f = \int \left| { \frac { 1 } { T } } \pi \left( { \frac { t } { T } } \right) \right| ^ { 2 } { \mathrm { d } } t = { \frac { 1 } { T } } .
$$

9.7. Find the autocorrelation function $R ( \tau )$ of a Gaussian process after filtering by the linear filter

$$
\tilde { H } ( \nu ) = \frac { 1 } { 1 + ( 2 \pi R C \nu ) ^ { 2 } } .
$$

9.8. Consider a stochastic process $\mathbf { x } ( t )$ . Define a new process ${ \bf x } _ { T } ( t )$ , referred to as the estimate of the mean of ${ \bf x } ( t )$ , by

$$
x _ { T } ( t ) = \frac { 1 } { 2 T } \int _ { t - T } ^ { t + T } x ( t ) \mathrm { d } t .
$$

Show that, when ${ \bf x } ( t )$ is stationary,

$$
\langle x _ { T } ( t ) \rangle = \langle x ( t ) \rangle = \eta ,
$$

and

$$
\sigma _ { { \bf x } _ { T } } ^ { 2 } = \frac { 1 } { 4 T ^ { 2 } } \int _ { - T } ^ { + T } \int _ { - T } ^ { + T } C ( t _ { 1 } - t _ { 2 } ) \mathrm { d } t _ { 1 } \mathrm { d } t _ { 2 } ,
$$

where

$$
C ( t _ { 1 } - t _ { 2 } ) = R ( t _ { 1 } - t _ { 2 } ) - \eta ^ { 2 } .
$$

Express $\sigma _ { \mathbf { x } _ { T } } ^ { 2 }$ as a function of $t _ { 1 } - t _ { 2 } = \tau$

 DApply this result to the filtering process in Problem 9.7 and deduce a simple analytic form for its variance. Graph the quantity $\sigma _ { \mathbf { x } _ { T } } ^ { 2 } ( \tau )$ and give a simple interpretation.

Apply these results to the following astrophysical problem, frequently encountered in Fourier transform spectroscopy, speckle interferometry, the study of solar oscillations, and other areas. An astronomer wishes to measure the spectral density of a process $\mathbf { x } ( t )$ , which he knows to be normal and centred. Give a practical procedure for doing this. What value of $T$ should be chosen so that the estimate of the spectral density $S _ { T } ( \nu )$ will lie within a previously chosen confidence interval?

9.9. Optimal Sampling Rate and Shannon’s Theorem. In a turbulent fluid, viscous dissipation gives a wave number cutoff $\kappa _ { \mathrm { M } }$ to the spectrum of spatial frequencies in the turbulence (see Chap. 2). Assuming the medium to be isotropic, what geometrical arrangement of temperature sensors should be set up in order to be able to reconstruct by interpolation the full temperature distribution of the medium?

A sinusoidal plane temperature wave, with wave number $\kappa _ { 0 }$ in a given direction, is superposed upon the turbulence. How is the spectral density modified?

9.10. Shannon Optimal Sampling Rate. The aim is to determine to great accuracy the period $T _ { \mathfrak { p } }$ of the Vela optical pulsar PSR 0833-45 (Fig. 7.9), knowing that it is close to $8 9 \mathrm { m s }$ . The signal is received by a photomultiplier and then sampled at the frequency $f _ { \mathrm { S } }$ . The dark current of the detector produces Poissonian noise, with a white spectral density up to $f _ { \mathrm { c } } \gg f _ { \mathrm { p } }$ , where $f _ { \mathrm { p } } = 1 / T _ { \mathrm { p } }$ . What is the optimal value of $f _ { \mathrm { S } } \mathrm { ? }$ DDetermine the signal-to-noise ratio if the measurement lasts for a time $T$ (assuming availability of all the required quantities: the magnitude of the pulsar, the transmission and quantum efficiency of the setup, the aperture of the telescope, and the noise current).

Show that $f _ { \mathrm { S } }$ must be modified if information is sought concerning the shape of the periodic signal, and explain how it must be modified. What would be the effect of such a change on the signal-to-noise ratio of the PSD?

9.11. Digitisation and Truncation. Consider two centred normal processes ${ \bf x } ( t )$ and $\mathbf { y } ( t )$ , with the same variance $\sigma ^ { 2 }$ , whose correlation is given by

$$
\langle x ( t ) y ( t ) \rangle = \rho \sigma ^ { 2 } .
$$

This is equivalent to the joint probability distribution

$$
\begin{array} { r l } & { \mathrm { p r o b } \{ X \le \mathbf { x } < X + \mathrm { d } X , ~ Y \le \mathbf { y } < Y + \mathrm { d } Y \} } \\ & { \qquad = \frac { 1 } { 2 \pi \sigma ^ { 2 } ( 1 - \rho ^ { 2 } ) ^ { 1 / 2 } } \exp \left[ - \frac { X ^ { 2 } + Y ^ { 2 } - 2 \rho X Y } { 2 \sigma ^ { 2 } ( 1 - \rho ^ { 2 } ) } \right] . } \end{array}
$$

Let $a _ { i }$ and $b _ { i }$ be samples of $x ( t )$ and $y ( t )$ taken at regular intervals $t _ { i }$ . Instead of digitising $x$ and $y$ , only their signs are recorded:

$$
a _ { i } = \left\{ { \begin{array} { l l } { + 1 { \mathrm { ~ i f ~ } } } & { x ( t ) \geq 0 , } \\ { - 1 { \mathrm { ~ i f ~ } } } & { x ( t ) < 0 , } \end{array} } \right.
$$

and similarly for $b _ { i }$ with reference to $y ( t )$ . This digitisation on one bit is extremely rapid. Show that the correlation between the new discrete random variables $a _ { i }$ and $b _ { i }$ is given by

$$
\langle a _ { i } b _ { i } \rangle = \frac { 2 } { \pi } \arcsin \rho ,
$$

so that, for weak correlation $\rho \ll 1$ ,

$$
\langle a _ { i } b _ { i } \rangle \sim \frac { 2 \rho } { \pi } \propto \langle x ( t ) y ( t ) \rangle .
$$

Assume that the spectral densities of $x ( t )$ and $y ( t )$ have bounded support (filtered signals). Let $R ( \tau )$ be the autocorrelation of the processes a and $\mathbf { b }$ , and $S ( \nu )$ their cross-spectrum (the FT of $R$ ). Show that the signal-to-noise ratio for an estimate of $S$ is only a factor $2 / \pi$ less than the signal-to-noise ratio that would be obtained by measuring the original processes $\mathbf { X }$ and $\mathbf { y }$ over the same period of time. Real time digital correlators use this property, referred to as clipping, to increase their speed of calculation.

9.12. The whole visible face of the Sun (integrated flux) is observed with a highresolution spectrometer (see Sect. 8.3.3), in the wing of an absorption line of the photosphere. The received intensity is highly-dependent on the Doppler shift of the line, which in turn depends on the line-of-sight component of the mean velocity. Once the Doppler effects due to the various relative motions of the Sun and the Earth have been corrected for, any non-zero residue is interpreted as a large scale oscillation of the Sun’s surface. A period of $1 6 0 \mathrm { m i n }$ is observed.

What is the optimal sampling of the signal? At non-polar latitudes on Earth, only daytime observation is possible. What effect does this truncation have on the observed spectrum? Show that it will contain artificial or ghost lines. If, in addition, randomly occurring cloud formations sometimes prevent sampling, what will be their effect on the PSD? This could be simulated on a personal computer. (See Grec G. et al., Nature 288, 541, 1980, for a description of such observations.)

9.13. The spectral density of an image of photospheric solar granulation, observed in white light, is given in Fig. 9.21. The frame has dimensions $1 3 \times 1 3$ arcsec. What is the spatial frequency resolution obtained in the figure? The calculation has been simplified by replacing each granulation cell by a Dirac spike. How can the calculated two-dimensional PSD be interpreted, and in particular, the apparent hexagonal structure at low frequency and the noise at high frequency?

![](images/5006120b5bba2f12935e9f838daba23cd733680c9f4888f1a384b12f813a85a0.jpg)  
Fig. 9.21 Spectral density of solar granulation. From Aime C. et al., Astr. Ap. 79, 1, 1979. With the kind permission of Astronomy and Astrophysics

9.14. Given the brightness of the sky background around $5 0 0 ~ \mathrm { { n m } }$ (see Sect. 2.3), determine the number of counts resulting from the sky background given by each pixel of a CCD (quantum efficiency $\eta \ : = \ : 0 . 6 ,$ , observing a field of $2 \times 2$ arcsec through a $3 . 6 \mathrm { m }$ Dtelescope, whose transmission is assumed to be $100 \%$ . What is the limiting magnitude of a galaxy which could be detected against this background, with a reasonable degree of confidence, in an observation lasting one hour? (Be careful not to confuse the sky background with the fluctuation of this background.) What would be gained by observing over one month, or one year?

Answer. According to Sect. 2.3.1, the sky has magnitude $m _ { \mathrm { V } } = 2 2$ arcsec $^ { - 2 }$ , which implies a sky background flux per square arcsec given by

$$
F _ { \mathrm { c } } = 3 . 9 2 \times 1 0 ^ { - 8 } \cdot 1 0 ^ { - 2 2 / 2 . 5 } = 6 . 2 1 \times 1 0 ^ { - 1 7 } \mathrm { { W m ^ { - 2 } \mu { \mathrm { m } } ^ { - 1 } \mathrm { { a r c s e c } ^ { - 2 } . } } }
$$

The number of counts due to the sky background is

$$
{ n _ { \mathrm { c } } = F _ { \mathrm { c } } S \varOmega t / ( h c / \lambda ) , }
$$

where $S$ is the collecting area of the telescope, and hence $S = 1 . 8 ^ { 2 } \pi \mathrm { ~ m } ^ { 2 }$ , $t$ is the integration time, $\varOmega$ Dis the solid angle subtended at each pixel, namely 4 arcsec2, and $h c / \lambda$ is the energy of each photon.

The number of photons required from the galaxy in order to give a reasonable confidence interval $( 3 \sigma )$ is

$$
n _ { \mathrm { g } } = 3 \sqrt { F _ { \mathrm { c } } S \varOmega t / ( h c / \lambda ) } ,
$$

implying a flux from the galaxy of

$$
\begin{array} { l } { { F } _ { \mathrm { g } } = n _ { \mathrm { g } } ( h c / \lambda ) / S t } \\ { = 3 \sqrt { ( h c / \lambda ) \Omega { F } _ { \mathrm { c } } / S t } \quad \mathrm { W } \mathrm { m } ^ { - 2 } \mu \mathrm { m } ^ { - 1 } . } \end{array}
$$

Note that the smallest detectable flux varies as $t ^ { - 1 / 2 }$ .

For $t ~ = ~ 3 6 0 0 ~ \mathrm { s }$ , $F _ { \mathrm { g } } ~ = ~ 1 . 5 6 \times 1 0 ^ { - 1 9 } { \mathrm { W } } { \mathrm { m } } ^ { - 2 } { \mu \mathrm { m } } ^ { - 1 }$ , which corresponds to a magnitude $m _ { \mathrm { V } } = 2 8 . 5$ D. For $t = 1$ month, a factor of ${ \sqrt { 2 4 \times 3 0 } } = 2 6 . 8$ is gained, D Dcorresponding to 3.5 magnitudes. For $t = 1$  Dyear, only a further 1.35 magnitudes is Dgained. This does assume that the noise remains stationary over such long periods.

9.15. A photoconducting infrared detector is placed at the focus of a $4 \mathrm { m }$ telescope, with a field of view of 10 arcsec, in the photometric $_ \mathrm { N }$ band, of spectral width $0 . 5 ~ { \mu \mathrm { m } }$ . Two terms contribute to the received signal. Firstly, the flux of photons emitted by the star, and secondly, the emission of the Earth’s atmosphere, with emissivity $\varepsilon ( \lambda )$ . How can $\varepsilon ( \lambda )$ be evaluated (Sect. 2.3)?

Taking $\varepsilon ( \lambda ) ~ = ~ 0 . 5$ for the site under consideration, calculate the thermal Datmospheric background noise. What is the limiting magnitude $m _ { \mathrm { N } }$ imposed by this background for an observation of duration $1 \mathrm { ~ s ~ }$ , or $1 \ \mathrm { h r } ?$ Suggest ways of improving the observation.

9.16. Lock-in Detection. A procedure for extracting a signal from noise. In order to extract a signal, drowned out by noise, any available information concerning the signal, such as positivity, periodicity, and so on, should be put to use, with a view to reducing the final uncertainty. Detection is particularly simple if both the frequency and the phase of the signal are known. In Fig. 9.22, the radiation $\mathbf { x } ( t )$ is periodically modulated by a rotating disk (or some equivalent device), with frequency $\omega$ and

![](images/eeba2642c146586d1c91b4611f2f18392baa256493e2b4495053a1489c4d2113.jpg)  
Fig. 9.22 Signal modulated by a rotating disk

phase $\phi$ . The signal measured is then

$$
X _ { 0 } ( t ) = n ( t ) + x ( t ) F ( t ) ,
$$

where $n ( t )$ is the detector noise, $F ( t )$ the periodic, and in general non-sinusoidal, function characterising the chopper.

The following operations are then carried out, using either analogue electronic or digital techniques:

• Filtering, $X _ { 1 } ( t ) ~ = ~ X _ { 0 } ( t ) \star H ( t )$ , where $H ( t )$ is a narrow passband filter, $\Delta \omega \ll \omega$ D, centred on $\omega$ .   
• Multiplication, $X _ { 2 } ( t ) = X _ { 1 } ( t ) \cos ( \omega t + \phi ^ { \prime } )$ .   
D C• Low-frequency filtering, for example, by running mean,

$$
X _ { 3 } ( t ) = X _ { 2 } ( t ) \star \varPi ( t / T ) , \quad \mathrm { w i t h } \quad T \gg 2 \pi / \omega .
$$

Show that this sequence of operations only leaves the part of the noise $n ( t )$ with power spectrum in $\Delta \omega$ , and then uses the phase information. In the case of white noise, estimate the output signal-to-noise ratio. If ${ \bf x } ( t )$ is random (e.g., a Poissonian process for the arrival of photons), what is the effect on the measurement?

# Chapter 10 Sky Surveys and Virtual Observatories

Astronomers have always catalogued the objects they observe and study. In ancient times, the Greek astronomer Hipparchos (between 161 and $1 2 7 \mathrm { B C }$ ) and the Chinese astronomers Shi Shen and Gan De (in the Warring States period, around $5 0 0 ~ \mathrm { B C }$ ) built up the first systematic catalogues of the celestial regions accessible from their parts of the world. Tycho Brahe did likewise, followed by surveys of non-stellar objects, such as Messier’s.1 At the end of the nineteenth century, sky surveys marked the beginning of the great modern catalogues. Computers completely transformed this landscape in the last decade of the twentieth century, by vastly increasing the volumes of data that could be stored, while improving accessibility, addressability, and communications through a range of automated systems. In this chapter, we shall consider some of the results of this revolution. In addition to the development of statistical astrophysics and systematic whole sky surveys across all wavelengths, we will also discuss the advent of virtual observatories which bring together all available maps and data about a specific object, to assist in solving whatever astrophysical problem is under investigation.

# 10.1 Statistical Astrophysics

Modern astronomy is characterised by a genuine flood of data, growing exponentially. There are several reasons for this rapid evolution. The first, rather obvious, stems from growing instrumental capacities in terms of telescope size (see Chap. 5), number of pixels on 2D detectors (see Chap. 7), and resolution and spectral range of spectrometers (see Chap. 8). Another, more subtle reason is that, in several areas of astrophysics, the desired information, whether it concern a phenomenon on the cosmic scale or a particular class of objects, can now only be firmly established by analysing a sample containing thousands up to tens of millions of individual objects. Only these large samples suffice to reduce the effects of dispersion or lack of resolution in order to isolate some very dilute effect. Very ambitious observing programmes called large surveys often involve dedicated instruments as well as general purpose instruments on large telescopes. They are carried out over months or years by international consortiums, bringing together dozens of researchers.

Galactic astronomy and modern cosmology are two disciplines that depend heavily on this type of observation. And recently, scientists interested in the more remote regions of the Solar System have also become active in the development of sky surveys, in their search for objects beyond the orbit of Neptune.

The study of the Galaxy, e.g., stellar populations, structure, and components of the interstellar medium, has given rise to many exhaustive surveys, particularly in the centimetre and millimetre wave radio regions. In other wavelength regions, satellites observing in the infrared and at high energies have supplemented these surveys. Figure 1.7 illustrates the exceptional spectral coverage obtained in this way.

Cosmology has generated some very extensive programmes, and is continuing to do so. In each endeavour, whether it be the identification of large-scale structures as instantiated by clusters and associations of galaxies, the study of the evolution of the first galaxies in the remote universe, witness to the processes involved in assembly of the first structures, or the mapping of dark matter by weak gravitational lensing effects, the images of millions of galaxies must be acquired and analysed in order to identify statistically significant trends. In this context, the need for a statistical dimension covering very large numbers of objects is well exemplified by attempts to determine cosmological parameters as accurately as possible.

The search for rare objects is rather different but nevertheless involves quite analogous needs in terms of the amount of information that must be acquired and analysed. In this case, the desired property is not shared in some tenuous way by millions of individual sources, but is particular feature of a rarefied population that can only be tracked down within a huge population of superficially similar objects by identifying some specific signature. The search for quasars, planetary nebulas, brown dwarfs, free-floating planets,2 and trans-Neptunian objects are all the subject of such ambitious programmes.

One particular type of large survey is the class of exhaustive sky surveys, i.e., covering the whole celestial sphere in a certain wavelength region. This kind of survey was first attempted in the visible at the end of the nineteenth century with the ambitious international undertaking known as the Carte du ciel.3 The aim was to produce a complete photographic atlas of the sky in the two hemispheres, comprising no fewer than 22 000 photographic plates. Unfortunately, it was never quite finished, but was taken up again with more success at the beginning of the second half of the twentieth century by the Palomar Optical Sky Survey (POSS). This particularly effective survey was carried out using the very wide field telescope invented by Bernhardt Schmidt. It was then supplemented by equivalent surveys carried out in the southern hemisphere from the vantage point of Australia and Chile. A little later, radioastronomy was to catch up, e.g., with the Parkes–MIT–NRAO (PMN) survey, closely followed by infrared astronomy with the IRAS satellite in 1983, which mapped the sky in the far infrared. And high energies have not been neglected. With surveys like the one carried out by ROSAT in the X-ray region in 1992, there is scarcely any wavelength region in which the whole sky has not already been surveyed at the time of writing (2007). Astrometric surveys are also extremely important, with the Hipparcos mission in 1989, and the even more impressive GAIA mission, planned for 2012, which should investigate a billion stars (see Chap. 4).

Concerning the analysis of data generated in this way, a large survey is characterised by several parameters, of which the most important are the field covered, the sensitivity (or depth), the completeness, and the confusion limit:

• Field. This is the area covered by the large survey. Some surveys cover the whole sky, or just one of the two hemispheres. The field must be extensive to ensure that the results are not dominated by specific effects of concentration or rarity. The term cosmic variance is generally used in observational cosmology to qualify this cause of uncertainty.   
. Sensitivity or Depth. This is the magnitude or flux of the faintest unambiguously detected objects. This is often a criterion of the kind flux $> \ n \sigma$ , where $\sigma$ is the uncertainty in the flux measurement. The depth of the survey generally depends directly on the exposure time in a given direction. The survey must be deep to ensure that reliable statistics can be obtained for particularly remote or intrinsically faint objects. Depending on the objects under investigation, a compromise is always sought between sensitivity and field, since the total time allocated to such a programme must remain within reasonable bounds of months or years.   
. Completeness. This is closely related to the last feature. It is defined as the apparent magnitude (or flux) beyond (or below) which only a given fraction (usually $50 \%$ ) of the relevant objects is effectively detected. A conventional method for determining this completeness limit is to introduce simulated data into the real data in a realistic way and then to determine the fraction effectively detected by the algorithm. A survey can by complete, in the case where almost no member of the relevant class of objects has been omitted.   
. Confusion Limit. If several sources are located in the element of spatial resolution of the observing instrument, the counts obtained will be incorrect because the apparent position and flux of the sources will be modified by the mixing with generally fainter sources. This is known as source confusion, and the resulting measurement error is referred to as confusion noise. This problem first appeared in radioastronomy, where antenna sidelobes are significant.

![](images/9506e8f956db5e7b2008d1fa35028b8c9dd2dac4de2527321daf3f470044b719.jpg)  
Fig. 10.1 Source confusion and spatial resolution in the images of a field of $6 . 6 ^ { \prime } \times 6 . 6 ^ { \prime }$ observed in the infrared and containing galaxies. Top: ISO mission, $\lambda = 1 7 0 ~ \mu \mathrm { m }$  and Spitzer mission, $\lambda = 1 6 0 \mu \mathrm { m }$ . Bottom: $\lambda = 7 0 \mu \mathrm { m }$ , $\lambda = 2 4 \mu \mathrm { m }$ D. G. Lagache et al. ARAA 43, 727, 2005, with the D Dkind permission of the publisher

The infrared region can also be sensitive to this limit, whenever the sensitivity becomes high while the angular resolution remains modest. This is exemplified by infrared space observatories like IRAS (1983), ISO (1995), and Spitzer (2003), where the telescopes, with diameters less than one metre, provide angular resolutions in the range between a few arcsec and one arcmin, while the sensitivities achieved are excellent owing to the absence of thermal background in space (see Fig. 10.1).

# 10.2 Large Sky Surveys

The period from 1980 to 2007 has certainly been the golden age for large sky surveys. A series of such programmes led to major changes in our understanding, particularly in cosmology, which until then had been restricted to largely theoretical developments, owing to the lack of sufficient observational data. This golden age is set to continue for a few more years at least, with ever more ambitious projects. Without trying to be exhaustive, we shall discuss here the large photometric, spectroscopic, and cosmic microwave background surveys summarised in Table 10.1.

Table 10.1 Some large sky surveys currently available or in progress (2007)   

<table><tr><td>Name</td><td>Means</td><td>入</td><td>Field</td></tr><tr><td colspan="4">Photometric sky surveys</td></tr><tr><td>APM</td><td>Measuring machine</td><td>Visible</td><td>Southern hemisphere</td></tr><tr><td>SDSS</td><td>Camera (ground)</td><td>Visible</td><td>10000 deg²</td></tr><tr><td>CFHTLegacy</td><td>Camera (ground)</td><td>Visible</td><td>410 +170+ 4 deg²</td></tr><tr><td>IRAS</td><td>Satellite (1983)</td><td>12,25,60,100 μm</td><td>Southern hemisphere</td></tr><tr><td>2MASS</td><td>Camera (ground)</td><td>Near infrared</td><td>Whole sky</td></tr><tr><td>DENIS</td><td>Camera (ground)</td><td>Nearinfrared</td><td>Whole sky</td></tr><tr><td>Einstein</td><td>Satellite (1979)</td><td>X ray</td><td>Whole sky</td></tr><tr><td>XMM</td><td>Satellite (1999)</td><td>X ray</td><td>5deg²</td></tr><tr><td colspan="4">Spectroscopic sky surveys</td></tr><tr><td>CfA2</td><td>Ground</td><td>Visible</td><td>17 000 deg²</td></tr><tr><td>DEEP2</td><td>Ground</td><td>Visible</td><td>3.5 deg²</td></tr><tr><td>SDSS</td><td>Ground</td><td>Visible</td><td>10000 deg²</td></tr><tr><td>VVDS wide</td><td>Ground</td><td>Visible</td><td>16 deg²</td></tr><tr><td>VVDS deep</td><td>Ground</td><td>Visible</td><td>1.5 deg²</td></tr><tr><td>ZCOSMOS</td><td>Ground</td><td>Visible</td><td>1.7 + 1.0 deg²</td></tr><tr><td colspan="4">Cosmic microwave background surveys</td></tr><tr><td>COBE</td><td>Satellite (1989)</td><td>1.25 μm-5 mm</td><td>Whole sky</td></tr><tr><td>BOOMERANG</td><td>Balloon</td><td>25-412 GHz</td><td>Southern hemisphere</td></tr><tr><td>WMAP</td><td>Satellite (2001)</td><td>22-90 GHz</td><td>Whole sky</td></tr><tr><td>PLANCK</td><td>Satellite (2008)</td><td>30-857 GHz</td><td>Whole sky</td></tr></table>

The list is impressive, but reflects the spectacular progress in cosmology over the years 1995–2005, including the discovery that the expansion of the Universe is actually accelerating, with the accompanying dark energy hypothesis, confirmation of inflation, confirmation of the flat universe model, measurements of most cosmological parameters with ever increasing accuracy, evidence for dark matter, and so on.

Large sky surveys generally use dedicated systems either in the form of a specialised instrument at the focus of a telescope that can be used for other purposes, or as a complete telescope/instrument system custom built for the task at hand. In the latter case, this system may be spaceborne.

# 10.2.1 Sky Surveys at Visible Wavelengths

# Schmidt Sky Surveys and Their Digitisation

To work effectively, these surveys must be able to access a wide field in one go, while nevertheless keeping a good angular resolution. In the optical region, the large photographic plate set up at the focus of a Schmidt telescope served this purpose well for several decades. The surveys made with these instruments from 1950 to 2000 nevertheless have a rather poor quantum efficiency, limiting them to magnitudes below 19 to 21, depending on the colour, and poor photometric quality owing to the non-linearity of the photographic emulsion. Despite these limitations and their age, these surveys are still the only ones providing access to the whole sky at resolutions of the order of a few arcsec, so they remain genuinely useful. The main drawback with them, namely that they could not directly provide digital information suitable for mass processing and archiving, is no longer a problem, thanks to systematic digitisation of the plates.

The three large Schmidt surveys were:

• SERC/AAO (Siding Spring Telescope, Australia) for the southern hemisphere $( \delta < 0 ^ { \circ }$ ). The two series of plates are denoted by J (blue) and I, from 1974 to 1987, and R from 1990 to 2000. POSSI/POSSII (Palomar Schmidt Telescope): E (red) and O (blue) for $\delta > - 2 0 ^ { \circ }$ , from 1950 to 1958. J (blue), F (red), N (band I) for $\delta > 0 ^ { \circ }$ , from 1987 to 2000. The field of a POSS plate is in general $5 ^ { \circ } \times 5 ^ { \circ }$ with mean angular resolution 3 arcsec. ESO: R (red) for $\delta < - 2 0 ^ { \circ }$ from 1978 to 1990.

These surveys were distributed to observatories the world over in the form of copies on large format photographic paper, filling enormous amounts of shelving and generally accompanied by superposable transparent sheets containing multiwavelength information about identified sources.

Today, the Schmidt sky surveys have been made available by digitising the photographic plates. This was done using specialised machines which explore the plates point by point with high mechanical accuracy, thereby translating their grey levels into digitised pixels.

The Automatic Plate Scanner (APS) at the University of Minnesota produced the POSSI E and O plate digitisations. The resulting catalogue contains 200 million objects (north) from the first epoch along with a catalogue of galaxies. All the recorded objects correspond to double detections in two colours. The Proper Motion Machine (PMM) was implemented by the US Naval Observatory (Washington, USA). The POSSI and POSSII measurements of the AAO-J, SERC, and ESO were used to produce the USNO catalogue, containing 520 million objects. Two rough magnitudes (R and B) are given for these objects. This is a reference catalogue for astrometry. The Automated Plate Measurer (APM) is in Cambridge (UK). This machine digitised the AAO-R, SERC-J, and POSSI plates. A galaxy catalogue well known to cosmologists was produced first. In 2007, two whole-sky catalogues of the northern and southern hemispheres are available. In France, MAMA is a high accuracy measuring machine at the Paris Observatory, which has been used for specific programmes rather than exhaustive coverage of sky surveys.

![](images/6560e9d09252c4beb04ae2cf9301a3e8909d690a045850fb52cc3d5a8260b0ad.jpg)  
Fig. 10.2 Focal plane of the MEGACAM camera, showing the array of 40 thinned $4 6 1 2 \times 2 0 4 8$ pixel CCDs made by EEV (UK). Source SApCEA

# Large CCD Sky Surveys

With the advent of CCD detectors (see Chap. 7) around 1980, the photographic plate was gradually superseded, although it was only during the 1990s that surveys could finally be produced with any real efficiency. It had to be possible to form very large area arrays of CCD detectors, developed specifically for this purpose. The whole area had to be sensitive without loss at edges, using rear face connections to keep the sides free, and highly accurate juxtaposition techniques had to be developed. A good example is the MEGACAM camera (see Fig. 10.2), developed by the astrophysics department of the French atomic energy authority (CEA). This simultaneously operates, at low temperatures, an array of $4 0 ~ \mathrm { C C D }$ detectors each with $4 6 1 2 \times 2 0 4 8$ pixels, manufactured by the British company EEV. This camera is set up at the primary focus of the CFH telescope (CFHT) (Hawaii) behind a dedicate focal reducer, comprising a sophisticated combination of very large lenses and a mobile image stabilisation component. An excellent image quality is achieved over almost the whole of the impressive field of view of $1 ^ { \circ } \times 1 ^ { \circ }$ .

Deep Wide-Field Photometric Surveys

These are used to probe regions exceeding the characterise size of the large scale structures in the Universe $( { \approx } 6 0 \ \mathrm { M p c } )$ , and their measurements are thus barely affected by cosmic variance. One classic use of these surveys is to measure the angular correlation function. They can also be used to select sub-samples of rare objects in the Universe.

As an illustration, let us consider the observational means and corresponding performance of deep wide-field surveys made with the CFH telescope in Hawaii:

• The first such survey, the Canada–France Deep Field (CFDF) survey, was carried out from 1996 to 1997 using the UH8K camera, an array of 8 CCDs with a field of view of 29 arcmin $\times$ 29 arcmin. This survey covered $1 \deg ^ { 2 }$ and included over 100 000 objects, down to the detection limit $I _ { A B } = 2 5 . 5$ . D The CFH12K camera, an array of $1 2 { \mathrm { ~ C C D s } }$ with a field of view of 42 arcmin $\times ~ 2 8$ arcmin, was then used to carry out the VIMOS VLT Deep Survey (VVDS) from 1999 to 2000, which covered $1 6 \mathrm { d e g ^ { 2 } }$ to a depth of $I _ { A B } = 2 4 . 8$ . D Since 2004, the MEGACAM camera has been producing a survey with an even wider field of view. The CFHT Legacy Survey (CFHT-LS) has taken five years and a half years. The aim is to image $1 7 0 \mathrm { d e g } ^ { 2 }$ of the sky (the Wide component) in 5 colours $( \mathbf { u } ^ { * } , \mathbf { g } ^ { \prime } , \mathbf { r } ^ { \prime } , \mathbf { i } ^ { \prime } , z ^ { \prime } )$ , up to magnitude $I _ { A B } = 2 5 . 5$ , and $4 ~ \mathrm { d e g } ^ { 2 }$ (the Deep component) up to magnitude $I _ { A B } = 2 8 . 3$ . CFHT-LS also D Dincludes a Very Wide component in the plane of the ecliptic to seek out trans-Neptunian objects.

Among the most important large sky surveys, we should mention the Sloan Digital Sky Survey (SDSS) carried out at the Apache Point Observatory in New Mexico (USA) since 1998. This CCD survey, which covers quarter of the northern sky around the galactic pole $( 1 0 0 0 0 ~ \mathrm { d e g ^ { 2 } } )$ and part of the galactic plane, includes 5 colours $( \mathrm { u } ^ { \prime } , \mathrm { g } ^ { \prime } , \mathrm { r } ^ { \prime } , \mathrm { i } ^ { \prime } , \mathrm { z } ^ { \prime } )$ using the filters of the US Naval Observatory (USNO) photometric system, and reaches magnitude 23 in $\mathbf { r } ^ { \prime }$ . A dedicated $2 . 5 \mathrm { ~ m ~ }$ telescope was designed to acquire $3 \times 3 ~ \mathrm { d e g } ^ { 2 }$ images, using a $5 \times 6$ array of $2 0 4 8 \times 2 0 4 8$   CCDs operating in continuous scanning mode. More than 40 Tbytes of data will be generated. A subset of around 1 Tbyte will include 1 million spectra, together with positions and mini images in each colour for more than 100 million objects.

# Ultra-Deep Field Photometric Surveys

The Hubble Space Telescope (HST) was equipped from 2002 with the Advanced Camera for Surveys (ACS), which could make images with a field of view of $2 0 2 \times 2 0 2$ arcsec2 and a pixel size of 0.049 arcsec. Before the failure that put it out of action at the beginning of 2007, it was indeed a remarkable tool for observing the faintest objects, by virtue of the unequalled resolution and contrast of its images. Two deep photometric surveys have been particularly spectacular, namely the Hubble Deep Field North and South (HDF-N and HDF-S). Objects were detected up to magnitudes $I _ { A B } = 2 7 . 6$ , although the field of view remained limited to $4 \times 4$ Darcmin2. Hence only 2 500 galaxies were observed over these two fields. The angular resolution of the images obtained with the HST was unique for studying the morphology of galaxies and spectral shifts $z > 1$ , until the advent around 2005 of the first near-infrared surveys using adaptive optics, which are in the process of changing this situation.

# Spectroscopic Sky Surveys

It is particularly in observational cosmology that the large spectroscopic surveys have been conceived as indispensable supplements to the large imaging surveys. This is because they provide a way to access the third dimension, i.e., distance, by measuring the spectral shift toward the red of light from receding galaxies.

Note that multicolour photometric surveys contain information that can be treated as a very low resolution spectrum, and can be used to estimate the distance to galaxies by examining photometric redshifts. To obtain sufficiently accurate measurements of $z$ , one must cover the broadest possible spectral region with a large number of narrow bandpass filters.

The COMBO-17 survey is a deep field survey with imaging over $0 . 7 8 \ \mathrm { d e g ^ { 2 } }$ , made using the Wide Field Imager (WFI) camera installed on the $2 . 2 \mathrm { m }$ MPG/ESO telescope at La Silla in Chile. Images are obtained in 17 optical bands, including 12 narrow filters, covering the spectral region 300– $9 0 0 \mathrm { n m }$ . The COMBO-17 sample contains 25 000 photometric spectral shifts.

Compared with the use of spectroscopic shifts, the measurement is less robust and less accurate. The error is estimated to be 10 times as great. For this reason, true spectroscopic surveys soon came to the fore.

Since it is not feasible to measure this shift efficiently galaxy by galaxy, even at the low spectral resolutions required, multi-object spectroscopic methods flourished. These fall into two main families: multi-slit spectrographs and optical fibre spectrographs in medusa mode (see Sect. 8.3).

In the nearby Universe $( z < 0 . 1 $ ), two large spectroscopic surveys have acquired a considerable amount of data since 2001:

• Two Degree Field Galaxy Redshift Survey (2dFGRS). This is an Anglo-Australian project, using the $3 . 9 \mathrm { ~ m ~ }$ telescope of the Anglo-Australian Observatory, with the Two Degree Field (2dF) multi-object spectrograph, where 400 optical fibres are automatically arranged by a robot to measure the target objects (see Chap. 8). These objects are selected automatically from digitised photographic plates of the APM Galaxy Survey. This survey covers $2 0 0 0 \ \mathrm { d e g } ^ { 2 }$ and contains at total of $2 3 0 0 0 0 z$ measurements on as many galaxies. Sloan Digital Sky Survey (SDSS). Apart from its camera (see above), the SDSS has a fibre-fed multi-object spectrograph able to acquire 640 spectra at the same time. The aim of this survey, in progress at the time of writing (2011), is to obtain the spectra of a million galaxies.

At redshifts $z$ higher than 0.3, there is still no spectroscopic sample of the size of the 2dFGRS and SDSS surveys. To illustrate the difficulty involved at high z, note that the flux observed from a galaxy at $z = 4$ is 6 000 times fainter than the flux from a similar galaxy located at $z ~ = ~ 0 . 1$ D. The compromise between the size of Dthe observed field of view, depth of observations, and fraction of objects targeted generally leads to a selection of sources established purely on the basis of a limiting apparent magnitude.

Surveys carried out between 1994 and 2000 were made using telescopes in the $4 \textrm { m }$ category and multi-object spectrographs with multiplex gain in the range 50–70. The broadest spectroscopic sample contains 2 000 galaxies with magnitudes $R < 2 1 . 5$ for the CNOC2 Galaxy Redshift Survey, which is 100 times less than the size of samples made in the near Universe. The Canada–France Redshift Survey (CFRS) made statistical analyses up to $z = 1 . 3$ , thanks to a selection of faint objects. DThe results established by CFRS are spectacular, but the sample contains fewer than 250 galaxies in each age range.

Telescopes in the $8 \textrm { m }$ category have made much deeper surveys. The K20 spectroscopic survey was carried out with the Very Large Telescope (VLT) in Chile, using the FORS1 and FORS2 spectrographs which have multiplex gains of 19 and 52, respectively. This survey measured the redshift $z$ of 550 objects. However, it was a combination of multi-object spectrographs (MOS) with very high multiplex gain and intensive use of $8 \textrm { m }$ telescopes which, in 2007, produced spectroscopic surveys containing several tens of thousands of galaxies with redshifts up to $z \approx 6$ .

Two such large, deep-field spectroscopic surveys are underway at the time of writing (2007), namely, DEEP2 and the VIMOS-VLT Deep Survey (VVDS). DEEP2 uses the DEIMOS spectrograph of the Keck II telescope. DEIMOS is a slit MOS, obtaining 75 spectra simultaneously with spectral resolution $R = 4 0 0 0$ . DEEP2 will measure the spectra of $6 5 0 0 0$ galaxies at $z > 0 . 7$ .

DThe VVDS project is based at the VLT and uses the VIsible Multi-Object Spectrograph (VIMOS). This spectrograph can observe up to 1 000 spectra simultaneously at low resolution $R = 2 0 0$ ). The aim is to acquire 150 000 galaxy redshifts up to $z = 6$ . The field of the VLT is D D30 arcmin, this being split into four subfields, each imaged spectrally through a slit mask and a grism on a CCD array. Each mask is a thin sheet of aluminium in which a high power laser has cut narrow slits. Simultaneous spectral analysis of 1 000 objects is possible with this instrument.

# 10.2.2 Infrared Sky Surveys

The first infrared survey worthy of the name was carried out from space. This was the almost complete coverage of the sky by the IRAS satellite (1983) in four bands, viz., 12, 25, 60, and $1 0 0 ~ { \mu \mathrm { m } }$ , with a resolution of about 1 arcmin. The sky was scanned continuously by placing the satellite on a polar orbit held perpendicular to the direction of the Sun, with the telescope pointing to the local vertical. The excellent sensitivity achieved here is due to the fact that the whole setup, including telescope and detectors, was cooled. Over the past 15 years, the quality of the final product has been greatly improved by three complete reprocessing operations.

Ground-based surveys in the near infrared only became feasible at the beginning of the 1990s, with the advent of detectors of appreciable size $( 2 5 6 \times 2 5 6$ pixels). The two main programmes of this kind were 2MASS and DENIS (see Table 10.1):

• $2 \ \mu \mathbf { m }$ All Sky Survey (2MASS). This is a whole-sky survey in the spectral bands J, H, and K of the near infrared, carried out using two purpose-built telescopes, one in each hemisphere. The limiting magnitudes were 17, 16.4, and 15.6, respectively.

• Deep Near Infrared Southern Sky Survey (DENIS). This is a European survey of the southern sky in the spectral bands I, J, and K, reaching limiting magnitudes of 18.5, 16.5, and 14, respectively. The survey was carried out between 1997 and 2003, using the general purpose $1 \textrm { m }$ telescope at the ESO in La Silla, Chile, which was allocated to this project on a full time basis. The survey is available in the form of images and a catalogue of point sources, supplemented by a specific catalogue for the Magellanic Clouds.

# 10.3 A Virtual Observatory

At the beginning of the twenty-first century, it became desirable to develop ways of exploiting this extraordinary wealth of survey data, so that all multiwavelength information about a region or object could be put together simultaneously in order to extract the maximum possible astrophysical value. This idea has now become a reality for any research scientist around the world. Thanks to a set of standardised tools, any scientist can obtain access to several of these databases through a computer terminal, superposing information in a uniform manner in the form of maps. This is the notion of virtual observatory, now a priority development in many countries and the subject of international coordination.

Hundreds of terabits $1 0 ^ { 1 2 }$ bits) of observation data, corresponding to several thousand billion pixels are generated by ground-based and spaceborne observatories, and at ever increasing rates. Of course, this information, stored in digital form in huge databases, is exploited by the scientists responsible for producing it, but often only to extract some rather narrow set of information, while the full content of these databases would allow others to find a wealth of other information, e.g., concerning other, previously ignored sources, nevertheless worthy of analysis in some different context. Making this data available to a wider community would certainly avoid the unnecessary duplication of costly observation nights. Observatories and space agencies have understood this simple fact and most offer this service today to the broader scientific community, providing free access to their archives after generally rather short periods of one or two years, during which exclusive access is maintained for those who made the observations.

There is now a clear desire to take a further step and provide the possibility of reconstructing the sky virtually, at all wavelengths. Online access to databases held in observatories around the world, in a user friendly format that can be directly exploited scientifically, will require the help of new information technologies and up-to-date research and analysis tools that are fast and simple to use. The aim of the European project Astrophysical Virtual Observatory (AVO), born in 2001, is precisely to provide scientific research with such tools. Supported by the European Commission, this project is piloted by the ESO with several European partners.

![](images/2f2e4ef1d83e943a9f64447869042857e769b7361c9fb1b3923bfb43624057c4.jpg)

![](images/1579dafd2bf8b25c8202359fd37699ea58eadc2ceec57d3262d654a075dec348.jpg)  
Fig. 10.3 Upper: Example of what is possible with the Aladin software at the CDS. Comparing images produced by large sky surveys, in this case, IRAS $1 0 0 \ \mu \mathrm { m }$ (left) and POSS visible (right), and superposing object identification and photometry from other catalogues (here 2MASS). Measurement values appear at the bottom. Lower: User interface for selecting image database or catalogue

The American counterpart of the AVO, also born in 2001, is the US National Virtual Observatory (NVO).4

Among those developing the AVO, two French institutes are playing an exemplary role. One is the Centre de donn´ees astronomiques de Strasbourg (CDS), run by the CNRS and the Louis Pasteur university, which specialises in archiving, and the other is the TERAPIX data centre (Traitement El´ementaire, Analyse et R´eduction des PIXels) based at the Institut d’Astrophysique de Paris, and run by the CNRS and the University of Paris 6, working upstream by processing the huge amounts of data from these large sky surveys in a fully automated way.

For many years now, the CDS has been a reference in the gathering, identification, and archiving of astronomical and bibliographical data. Its unique SIMBAD database can be accessed online. The CDS has also pioneered the notion of virtual observatory with the development of the ALADIN system, which can already be used to visualise and superpose images from the main large imaging sky surveys on a personal computer, identifying catalogued sources and supplying the corresponding photometric and astrometric data (see the example in Fig. 10.3).

The TERAPIX center was set up to exploit data provided by the MEGACAM (visible) and WIRCAM (infrared) CCD cameras operating at the focal point of the $3 . 6 \mathrm { ~ m ~ }$ Canada–France– Hawaii (CFH) telescope. It was in particular the very ambitious CFHT Legacy Survey which originally mobilised a significant fraction of the efforts at this centre. Since then, its missions have been extended and TERAPIX now processes data from other very large sky surveys.

# Appendix A Fourier Transforms

The reviews given in Appendices A and B are intended to help with the understanding of Chaps. 6, 7, and 9, and to introduce the notation used throughout the book. Although they have been written with a certain minimum of rigour, mathematical proof and systematic formalism were not the main aim. Examples have been chosen as close as possible to the themes of the book.

# A.1 Definitions and Properties

# A.1.1 Definitions

Given a function $f ( x )$ , where $x \in \mathbb { R }$ , the Fourier transform of $f ( x )$ is the function $\tilde { f } ( s )$ , where $s \in \mathbb { R }$ , and

$$
{ \tilde { f } } ( s ) = \int _ { - \infty } ^ { \infty } f ( x ) { \mathrm { e } } ^ { - 2 \mathrm { i } \pi s x } \mathrm { d } x ~ .
$$

The functions $f$ and $\tilde { f }$ are said to form a Fourier pair, and we sometimes write

$$
\tilde { f }  f \quad \mathrm { o r } \quad \tilde { f } = \mathrm { F T } [ f ] .
$$

The function $\tilde { f } ( s )$ exists if the function $f ( x )$ is bounded, integrable and has only a finite number of maxima, minima, and discontinuities. This does not necessarily imply that the transform of $\tilde { f }$ is $f$ . For the Fourier transformation to be reciprocal, i.e.,

$$
f ( x ) = \int _ { - \infty } ^ { \infty } \tilde { f } ( s ) \mathrm { e } ^ { 2 \mathrm { i } \pi s x } \mathrm { d } s ,
$$

it is sufficient that $f$ should be square-integrable, that is, that the integral

$$
\int _ { - \infty } ^ { \infty } | f ( x ) | ^ { 2 } \mathrm { d } x
$$

should exist. The definition of the FT can be extended to distributions. The FT of a distribution is not necessarily square-integrable.

The functions $f$ and $\tilde { f }$ may be either real or complex.

# Generalisation

It is possible to generalise the FT to several dimensions, if $f$ is defined on $\mathbb { R } ^ { n }$ (i.e., is a function of $n$ real variables). Let $r , w \in \mathbb { R } ^ { n }$ . Then

$$
\tilde { f } ( \boldsymbol { w } ) = \int _ { - \infty } ^ { \infty } f ( r ) \mathrm { e } ^ { - 2 \mathrm { i } \pi r \cdot \boldsymbol { w } } \mathrm { d } r \mathrm { ~ . ~ }
$$

# A Simple Interpretation

If $f ( t )$ is a function of time, $\tilde { f } ( s )$ represents its content of temporal frequencies. Similarly, if $f ( r )$ is defined on $\mathbb { R } ^ { 2 }$ , representing a two-dimensional space, the function $\tilde { f } ( \boldsymbol w )$ , where ${ \pmb w } \in \mathbb { R } ^ { 2 }$ , represents its content of spatial frequencies.

# A.1.2 Some Properties

Linearity

$$
\begin{array} { r c l } { { } } & { { } } & { { \mathrm { F T } \left[ a f \right] = a \mathrm { F T } \left[ f \right] , \quad a = \mathrm { c o n s t . } \in \mathbb { R } , } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \mathrm { F T } \left[ f + g \right] = \mathrm { F T } \left[ f \right] + \mathrm { F T } \left[ g \right] . } } \end{array}
$$

# Symmetry and Parity

Symmetry considerations are useful in the study of FTs. Let $P ( x )$ and $Q ( x )$ be the even and odd parts of $f ( x )$

$$
f ( x ) = P ( x ) + Q ( x ) .
$$

Then

$$
\tilde { f } ( s ) = 2 \int _ { 0 } ^ { \infty } P ( x ) \cos { ( 2 \pi x s ) } \mathrm { d } x - 2 \mathrm { i } \int _ { 0 } ^ { \infty } { Q ( x ) } \sin { ( 2 \pi x s ) } \mathrm { d } x \ .
$$

We also have the trivial relation

$$
\tilde { f } ( 0 ) = \int _ { - \infty } ^ { \infty } f ( x ) \mathrm { d } x \ ,
$$

Table A.1 Symmetry of Fourier pairs   

<table><tr><td>f(x)</td><td>f（s）</td></tr><tr><td>Real and even</td><td>Real and even</td></tr><tr><td>Real and odd</td><td>Imaginary and odd</td></tr><tr><td>Imaginary and even</td><td>Imaginary and even</td></tr><tr><td>Complex and even</td><td>Complex and even</td></tr><tr><td>Complex and odd</td><td>Imaginary and odd</td></tr><tr><td>Real,arbitrary</td><td>Real part even,imaginary part odd</td></tr><tr><td>Imaginary,arbitrary</td><td>Imaginarypart even,real part odd</td></tr></table>

![](images/1620660b43bba3f0e98a75a99daf2d142f76da842aaf0ecec344775fad97cf11.jpg)  
Fig. A.1 Representation of the Fourier Transform $\tilde { f } ( s )$ of an arbitrary real function $f ( x )$ , showing the real and imaginary parts

which says that the zeroth order moment corresponds to the zero frequency. This result leads to Table A.1. Figure A.1 gives a simple representation of the transform $\tilde { f } ( s )$ .

# Similarity

The similarity relation is written

$$
f ( a x )  { \frac { 1 } { | a | } } { \tilde { f } } ( { \frac { s } { a } } ) , \qquad a = { \mathrm { c o n s t a n t } } \in \mathbb { R } .
$$

The dilatation of a function causes a contraction of its transform. This easilyvisualised property is useful in understanding why the transform of a function with very compact support (i.e., which is non-zero on only a small region), has a very extended transform. In analysing temporal frequencies, we find that an impulse of short duration contains a very wide spectrum of frequencies, i.e., the shorter the impulse, the higher the frequencies its transform contains. This is the classic relation for the spectrum of a wave packet, according to which our knowledge of the properties of a signal cannot be arbitrarily precise simultaneously in both time and frequency.

# Translation

The translation of a function gives

$$
f ( x - a )  \mathrm { e } ^ { - 2 \mathrm { i } \pi a s } \ \tilde { f } ( s ) \ .
$$

A translation in one space is a phase rotation in the transform space.

# Derivative

It follows directly from the definition of a Fourier pair that

$$
\frac {  { \mathrm { d } } f ( x ) } {  { \mathrm { d } } x }  ( 2 \pi  { \mathrm { i } } s ) \tilde { f } ( s ) , \qquad \frac {  { \mathrm { d } } ^ { n } f ( x ) } {  { \mathrm { d } } x ^ { n } }  ( 2 \pi  { \mathrm { i } } s ) ^ { n } \tilde { f } ( s ) .
$$

# A.1.3 Important Special Cases in One Dimension

# Box Function

The box function, written $\varPi ( x )$ , is defined by

$$
\begin{array} { c } { { \pi ( x ) = 1 \quad \mathrm { f o r } \quad x \in \displaystyle \mathrm { \biggr ] } { - \frac { 1 } { 2 } } , + \frac { 1 } { 2 } \biggl [ \ , } } \\ { { \nonumber } } \\ { { \pi ( x ) = 0 \quad \mathrm { f o r } \quad x \in \displaystyle \mathrm { \biggr ] } { - \infty } , - \frac { 1 } { 2 } \biggl ] \ \mathrm { o r } \left[ \frac { 1 } { 2 } , + \infty \right[ \ , } } \end{array}
$$

and shown in Fig. A.2. We have likewise, for the box of width $a > 0$ ,

$$
\begin{array} { c c c } { { \displaystyle \pi \left( \frac { x } { a } \right) = 1 } } & { { \mathrm { f o r } } } & { { x \in \displaystyle \left] - \frac { a } { 2 } , + \frac { a } { 2 } \right[ , } } \\ { { } } & { { } } & { { } } \\ { { \displaystyle \pi \left( \frac { x } { a } \right) = 0 } } & { { \mathrm { f o r } \quad x \in \displaystyle \left] - \infty , - \frac { a } { 2 } \right] \mathrm { o r } \left[ \frac { a } { 2 } , + \infty \right[ . } } \end{array}
$$

![](images/334a41cf5f7beb1b069a1798041274159035871711409c5a274acfa4d195dbb7.jpg)  
Fig. A.2 The box function and its Fourier transform

The FT of the box function $\varPi ( x )$ is written

$$
\mathrm { s i n c } s = \frac { \sin ( \pi s ) } { \pi s }  \pi ( x ) ~ ,
$$

and, using the similarity relation,

$$
\pi ( { \frac { x } { a } } )  | a | \operatorname { s i n c } ( a s ) ~ .
$$

# The Dirac Distribution

The Dirac distribution $\displaystyle \delta ( \boldsymbol { x } )$ , also known as the Dirac delta function, is not strictly speaking a function. It is defined by

$$
\delta ( x ) = \int _ { - \infty } ^ { \infty } { \mathrm { e } } ^ { 2 { \mathrm { i } } \pi s x } { \mathrm { d } } s .
$$

Its Fourier transform is thus 1 on the whole interval $\mathbf { \tau } ] - \infty , \infty [$ .

# The Dirac Comb

This distribution is constructed by periodic repetition of the Dirac distribution. It is written $\sqcup \left( x \right)$ , and sometimes called the Shah function (after the Cyrillic character ttwhich it resembles):

$$
\sqcup ( x ) = \sum _ { n = - \infty } ^ { + \infty } \delta ( x - n ) ~ .
$$

This distribution has the remarkable property of being identical to its FT, i.e.,

$$
\sqcup ( x )  \sqcup ( s ) .
$$

It is also called the sampling function, because of the following property, illustrated in Fig. A.3:

$$
\sqcup ( x ) f ( x ) = \sum _ { n = - \infty } ^ { + \infty } f ( n ) \delta ( x - n ) ~ .
$$

This may be intuitively understood as follows: starting from a continuous function $f ( x )$ , the operator reads a number (here infinite) of discrete values of $f ( x )$ , which we consider as being samples from $f ( x )$ . The term sample is understood here in a meaning close to the familiar one. (See also Appendix B and Sect. 9.1.)

This function can also be used as replication operator (Fig. A.3)

$$
\sqcup ( x ) \star f ( x ) = \sum _ { n = - \infty } ^ { + \infty } f ( x - n ) ~ ,
$$

where $\star$ denotes convolution (see below).