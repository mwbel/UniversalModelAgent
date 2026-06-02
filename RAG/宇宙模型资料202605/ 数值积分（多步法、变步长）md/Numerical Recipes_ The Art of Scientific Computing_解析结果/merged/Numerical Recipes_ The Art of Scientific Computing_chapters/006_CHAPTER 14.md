# CHAPTER 14

# 14.0 Introduction

In this chapter and the next, the concept of data enters the discussion more prominently than before.

Data consist of numbers, of course. But these numbers are given to the computer, not produced by it. These are numbers to be treated with considerable respect, neither to be tampered with, nor subjected to a computational process whose character you do not completely understand. You are well advised to acquire a reverence for data, rather different from the “sporty” attitude that is sometimes allowable, or even commendable, in other numerical tasks.

The analysis of data inevitably involves some trafficking with the field of statistics, that wonderful gray area that is not quite a branch of mathematics — and just as surely not quite a branch of science. In the following sections, you will repeatedly encounter the following paradigm, usually called a tail test or $p$ -value test:

- apply some formula to the data to compute “a statistic”   
compute where the value of that statistic falls in a probability distribution that is computed on the basis of some “null hypothesis” if it falls in a very unlikely spot, way out on a tail of the distribution, conclude that the null hypothesis is false for your data set

If a statistic falls in a reasonable part of the distribution, you must not make the mistake of concluding that the null hypothesis is “verified” or “proved.” That is the curse of statistics, that it can never prove things, only disprove them! At best, you can substantiate a hypothesis by ruling out, statistically, a whole long list of competing hypotheses, every one that has ever been proposed. After a while your adversaries and competitors will give up trying to think of alternative hypotheses, or else they will grow old and die, and then your hypothesis will become accepted. Sounds crazy, we know, but that’s how science works!

In this book we make a somewhat arbitrary distinction between data analysis procedures that are model-independent and those that are model-dependent. In the former category, we include so-called descriptive statistics that characterize a data set in general terms: its mean, variance, and so on. We also include statistical tests that seek to establish the “sameness” or “differentness” of two or more data sets, or that seek to establish and measure a degree of correlation between two data sets. These subjects are discussed in this chapter.

In the other category, model-dependent statistics, we lump the whole subject of fitting data to a theory, parameter estimation, least-squares fits, and so on. Those subjects are introduced in Chapter 15.

Section 14.1 deals with so-called measures of central tendency, the moments of a distribution, the median and mode. In $\ S 1 4 . 2$ we learn to test whether different data sets are drawn from distributions with different values of these measures of central tendency. This leads naturally, in $\ S 1 4 . 3$ , to the more general question of whether two distributions can be shown to be (significantly) different.

In $\ S 1 4 . 4 - \ S 1 4 . 7$ , we deal with measures of association for two distributions. We want to determine whether two variables are “correlated” or “dependent” on one another. If they are, we want to characterize the degree of correlation in some simple ways. The distinction between parametric and nonparametric (rank) methods is emphasized. Information-theoretic methods are discussed in $\ S 1 4 . 7$ . Section 14.9 introduces the concept of data smoothing, and discusses the particular case of Savitzky-Golay smoothing filters.

This chapter draws mathematically on the material on special functions that was presented in Chapter 6, especially $\ S 6 . 1 - \ S 6 . 4$ and $\ S 6 . 1 4$ . You may wish, at this point, to review those sections.

Bayesian methods make little appearance in this chapter, but become more prominent in the two chapters following this one.

# CITED REFERENCES AND FURTHER READING:

Bevington, P.R., and Robinson, D.K. 2002, Data Reduction and Error Analysis for the Physical Sciences, 3rd ed. (New York: McGraw-Hill).   
Taylor, J.R. 1997, An Introduction to Error Analysis, 2nd ed. (Sausalito, CA: University Science Books).   
Devore, J.L. 2003, Probability and Statistics for Engineering and the Sciences, 6th ed. (Belmont, CA: Duxbury Press).   
Wall, J.V., and Jenkins, C.R. 2003, Practical Statistics for Astronomers (Cambridge, UK: Cambridge University Press).   
Lupton, R. 1993, Statistics in Theory and Practice (Princeton, NJ: Princeton University Press).

# 14.1 Moments of a Distribution: Mean, Variance, Skewness, and So Forth

When a set of values has a sufficiently strong central tendency, that is, a tendency to cluster around some particular value, then it may be useful to characterize the set by a few numbers that are related to its moments, the sums of integer powers of the values.

Best known is the mean of the values $x _ { 0 } , \ldots , x _ { N - 1 }$

$$
\overline { { x } } = \frac { 1 } { N } \sum _ { j = 0 } ^ { N - 1 } x _ { j }
$$

which estimates the value around which central clustering occurs. Note the use of an overbar to denote the mean; angle brackets are an equally common notation, e.g., $\langle x \rangle$ . You should be aware that the mean is not the only available estimator of this quantity, nor is it necessarily the best one. For values drawn from a probability distribution with very broad “tails,” the mean may converge poorly, or not at all, as the number of sampled points is increased. Alternative estimators, the median and the mode, are mentioned at the end of this section.

Having characterized a distribution’s central value, one conventionally next characterizes its “width” or “variability” around that value. Here again, more than one measure is available. Most common is the variance,

$$
\operatorname { V a r } ( x _ { 0 } \ldots x _ { N - 1 } ) = { \frac { 1 } { N - 1 } } \sum _ { j = 0 } ^ { N - 1 } ( x _ { j } - { \overline { { x } } } ) ^ { 2 }
$$

or its square root, the standard deviation,

$$
\sigma ( x _ { 0 } \dots x _ { N - 1 } ) = \sqrt { \mathrm { V a r } ( x _ { 0 } \dots x _ { N - 1 } ) }
$$

Equation (14.1.2) estimates the mean squared deviation of $x$ from its mean value. There is a long story about why the denominator of (14.1.2) is $N - 1$ instead of $N$ . If you have never heard that story, you should consult any good statistics text. Here we will be content to note that the $N - 1$ should be changed to $N$ if you are ever in the situation of measuring the variance of a distribution whose mean $\overbar { x }$ is known a priori rather than being estimated from the data. (We might also comment that if the difference between $N$ and $N - 1$ ever matters to you, then you are probably up to no good anyway — e.g., trying to substantiate a questionable hypothesis with marginal data.)

If we calculate equation (14.1.1) many times with different sets of sampled data (each set having $N$ values), the values $\textstyle { \overline { { x } } }$ will themselves have a standard deviation. This is called the standard error of the estimated mean $\overbar { x }$ . When the underlying distribution is Gaussian, it is given approximately by $\sigma / \sqrt { N }$ . Correspondingly, there is a standard error of the estimated variance, equation (14.1.2), which is approximately $\sigma ^ { 2 } \sqrt { 2 / N }$ , and a standard error for the estimated $\sigma$ , equation (14.1.3), which is approximately $\sigma / \sqrt { 2 N }$ .

As the mean depends on the first moment of the data, so do the variance and standard deviation depend on the second moment. It is not uncommon, in real life, to be dealing with a distribution whose second moment does not exist (i.e., is infinite). In this case, the variance or standard deviation is useless as a measure of the data’s width around its central value: The values obtained from equations (14.1.2) or (14.1.3) will not converge with increased numbers of points, nor show any consistency from data set to data set drawn from the same distribution. This can occur even when the width of the peak looks, by eye, perfectly finite. A more robust estimator of the width is the average deviation or mean absolute deviation, defined by

$$
\mathrm { A D e v } ( x _ { 0 } \ldots x _ { N - 1 } ) = { \frac { 1 } { N } } \sum _ { j = 0 } ^ { N - 1 } | x _ { j } - { \overline { { x } } } |
$$

One often substitutes the sample median $x _ { \mathrm { m e d } }$ for $\overbar { x }$ in equation (14.1.4). For any fixed sample, the median in fact minimizes the mean absolute deviation.

Statisticians have historically sniffed at the use of (14.1.4) instead of (14.1.2), since the absolute value brackets in (14.1.4) are “nonanalytic” and make theoremproving more difficult. In recent years, however, the fashion has changed, and the subject of robust estimation (meaning, estimation for broad distributions with significant numbers of “outlier” points) has become a popular and important one. Higher moments, or statistics involving higher powers of the input data, are almost always less robust than lower moments or statistics that involve only linear sums or (the lowest moment of all) counting.

That being the case, the skewness or third moment, and the kurtosis or fourth moment should be used with caution or, better yet, not at all.

The skewness characterizes the degree of asymmetry of a distribution around its mean. While the mean, standard deviation, and average deviation are dimensional quantities, that is, have the same units as the measured quantities $x _ { j }$ , the skewness is conventionally defined in such a way as to make it nondimensional. It is a pure number that characterizes only the shape of the distribution. The usual definition is

$$
\operatorname { S k e w } ( x _ { 0 } \ldots x _ { N - 1 } ) = { \frac { 1 } { N } } \sum _ { j = 0 } ^ { N - 1 } \left[ { \frac { x _ { j } - { \overline { { x } } } } { \sigma } } \right] ^ { 3 }
$$

where $\sigma = \sigma ( x _ { 0 } \dots x _ { N - 1 } )$ is the distribution’s standard deviation (14.1.3). A positive value of skewness signifies a distribution with an asymmetric tail extending out toward more positive $x$ ; a negative value signifies a distribution whose tail extends out toward more negative $x$ (see Figure 14.1.1).

Of course, any set of $N$ measured values is likely to give a nonzero value for (14.1.5), even if the underlying distribution is in fact symmetrical (has zero skewness). For (14.1.5) to be meaningful, we need to have some idea of its standard error. Unfortunately, that depends on the shape of the underlying distribution, and rather critically on its tails! For the idealized case of a normal (Gaussian) distribution, the standard error of (14.1.5) is approximately $\sqrt { 1 5 / N }$ when $\textstyle { \overline { { x } } }$ is the true mean and $\sqrt { 6 / N }$ when it is estimated by the sample mean, (14.1.1). (Yes, using the sample mean is likely to give a more accurate estimate than using the true mean!) In real life it is good practice to believe in skewnesses only when they are several or many times as large as this.

The kurtosis is also a nondimensional quantity. It measures the relative peakedness or flatness of a distribution. Relative to what? A normal distribution! What else? A distribution with positive kurtosis is termed leptokurtic; the outline of the Matterhorn is an example. A distribution with negative kurtosis is termed platykurtic; the outline of a loaf of bread is an example. (See Figure 14.1.1.) And, as you no doubt expect, an in-between distribution is termed mesokurtic.

The conventional definition of the kurtosis is

![](images/092ebe8bc9dac84f6897c668a3fdc75f4f6e365122aa7041ec37562f70ffa923.jpg)  
Figure 14.1.1. Distributions whose third and fourth moments are significantly different from a normal (Gaussian) distribution. (a) Skewness or third moment. (b) Kurtosis or fourth moment.

$$
\mathrm { K u r t } ( x _ { 0 } \ldots x _ { N - 1 } ) = \left\{ \frac { 1 } { N } \sum _ { j = 0 } ^ { N - 1 } \left[ \frac { x _ { j } - \overline { { x } } } { \sigma } \right] ^ { 4 } \right\} - 3
$$

where the $^ { - 3 }$ term makes the value zero for a normal distribution.

The standard error of (14.1.6) as an estimator of the kurtosis of an underlying normal distribution is $\sqrt { 9 6 / N }$ when $\sigma$ is the true standard deviation, and $\sqrt { 2 4 / N }$ when it is the sample estimate (14.1.3). (Yes, you are better off using the sample variance.) However, the kurtosis depends on such a high moment that there are many real-life distributions for which the standard deviation of (14.1.6) as an estimator is effectively infinite.

Calculation of the quantities defined in this section is perfectly straightforward. Many textbooks use the binomial theorem to expand out the definitions into sums of various powers of the data, e.g., the familiar

$$
\mathrm { V a r } ( x _ { 0 } \dots x _ { N - 1 } ) = \frac { 1 } { N - 1 } \biggl [ \left( \sum _ { j = 0 } ^ { N - 1 } x _ { j } ^ { 2 } \right) - N \overline { { x } } ^ { 2 } \biggr ] \approx \overline { { x ^ { 2 } } } - \overline { { x } } ^ { 2 }
$$

but this can magnify the roundoff error by a large factor and is generally unjustifiable in terms of computing speed. A clever way to minimize roundoff error, especially for large samples, is to use the corrected two-pass algorithm [1]: First calculate $\overline { { x } }$ , then calculate $\operatorname { V a r } ( x _ { 0 } \dots x _ { N - 1 } )$ by

$$
\mathrm { V a r } ( x _ { 0 } \ldots x _ { N - 1 } ) = { \frac { 1 } { N - 1 } } \left\{ \sum _ { j = 0 } ^ { N - 1 } ( x _ { j } - { \overline { { x } } } ) ^ { 2 } - { \frac { 1 } { N } } \Biggl [ \sum _ { j = 0 } ^ { N - 1 } ( x _ { j } - { \overline { { x } } } ) \Biggl ] ^ { 2 } \right\}
$$

The second sum would be zero if $\overbar { x }$ were exact, but otherwise it does a good job of correcting the roundoff error in the first term.

if $\mathit { \Omega } _ { \mathrm { ~ n ~ } } < = \mathit { \Omega } 1 )$ throw("n must be at least 2 in moment");   
$\mathtt { s } = 0 \mathtt { . 0 }$ ; First pass to get the mean.   
for ( $\scriptstyle { \mathrm { i } = 0 }$ ;j<n;j++) s $+ =$ data[j];   
ave=s/n;   
adev=var skew=curt ${ = } 0$ .0; Second pass to get the first (absolute), sec  
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) { ond, third, and fourth moments of the adev $+ =$ abs( $\mathbf { s } =$ data[j]-ave); deviation from the mean. ep $+ = \mathrm { ~ s ~ } ;$ var $+ = \mathrm { ( p { = } s { * } s ) }$ ; skew $+ = \mathrm { \ l ~ ( ~ p ~ \ast = \mathrm { \Large ~ s ~ ) ~ } }$ ; curt $+ = { \begin{array} { l } { ( { \mathfrak { p } } } \end{array} } * = { \begin{array} { l } { { \mathfrak { s } } } \end{array} } )$ ;   
adev $/ = \texttt { n }$ ;   
var (var-ep\*ep/n)/(n-1); Corrected two-pass formula.   
sdev=sqrt(var); Put the pieces together according to the con  
if (var $! = ~ 0 . 0 \dot { }$ ) { ventional definitions. skew $/ =$ (n\*var\*sdev); curt=curt/(n\*var\*var)-3.0;   
} else throw("No skew/kurtosis when variance $\mathit { \Theta } = \mathit { \Theta } 0$ (in moment)");

# 14.1.1 Semi-lnvariants

The mean and variance of independent random variables are additive: If $x$ and $y$ are drawn independently from two, possibly different, probability distributions, then

$$
{ \overline { { ( x + y ) } } } = { \overline { { x } } } + { \overline { { y } } } \qquad \operatorname { V a r } ( x + y ) = \operatorname { V a r } ( x ) + \operatorname { V a r } ( x )
$$

Higher moments are not, in general, additive. However, certain combinations of them, called semi-invariants, are in fact additive. If the centered moments of a distribution are denoted $M _ { k }$ ,

$$
M _ { k } \equiv \left. { { ( x _ { i } - \overline { { x } } ) } ^ { k } } \right.
$$

so that, e.g., $M _ { 2 } = \operatorname { V a r } ( x )$ , then the first few semi-invariants, denoted $I _ { k }$ , are given by

$$
\begin{array} { c c c } { { I _ { 2 } = M _ { 2 } } } & { { I _ { 3 } = M _ { 3 } } } & { { I _ { 4 } = M _ { 4 } - 3 M _ { 2 } ^ { 2 } } } \\ { { } } & { { } } & { { I _ { 5 } = M _ { 5 } - 1 0 M _ { 2 } M _ { 3 } } } & { { I _ { 6 } = M _ { 6 } - 1 5 M _ { 2 } M _ { 4 } - 1 0 M _ { 3 } ^ { 2 } + 3 0 M _ { 2 } ^ { 3 } } } \end{array}
$$

Notice that the skewness and kurtosis, equations (14.1.5) and (14.1.6), are simple powers of the semi-invariants,

$$
\mathrm { S k e w } ( x ) = I _ { 3 } / I _ { 2 } ^ { 3 / 2 } \qquad \mathrm { K u r t } ( x ) = I _ { 4 } / I _ { 2 } ^ { 2 }
$$

A Gaussian distribution has all its semi-invariants higher than $I _ { 2 }$ equal to zero. A Poisson distribution has all of its semi-invariants equal to its mean. For more details, see [2].

# 14.1.2 Median and Mode

The median of a probability distribution function $p ( x )$ is the value $x _ { \mathrm { m e d } }$ for which larger and smaller values of $x$ are equally probable:

$$
\int _ { - \infty } ^ { x _ { \mathrm { m e d } } } p ( x ) d x = { \frac { 1 } { 2 } } = \int _ { x _ { \mathrm { m e d } } } ^ { \infty } p ( x ) d x
$$

The median of a distribution is estimated from a sample of values $x _ { 0 } , \ldots , x _ { N - 1 }$ by finding that value $x _ { i }$ which has equal numbers of values above it and below it. Of course, this is not possible when $N$ is even. In that case it is conventional to

estimate the median as the mean of the unique two central values. If the values $x _ { j }$ ; $j = 0 , \ldots , N - 1$ , are sorted into ascending (or, for that matter, descending) order, then the formula for the median is

$$
x _ { \mathrm { m e d } } = \left\{ \begin{array} { l l } { x _ { ( N - 1 ) / 2 } , } & { N \mathrm { ~ o d d } } \\ { \frac { 1 } { 2 } ( x _ { ( N / 2 ) - 1 } + x _ { N / 2 } ) , } & { N \mathrm { ~ e v e n } } \end{array} \right.
$$

If a distribution has a strong central tendency, so that most of its area is under a single peak, then the median is an estimator of the central value. It is a more robust estimator than the mean is: The median fails as an estimator only if the area in the tails is large, while the mean fails if the first moment of the tails is large; it is easy to construct examples where the first moment of the tails is large even though their area is negligible.

To find the median of a set of values, one can proceed by sorting the set and then applying (14.1.14). This is a process of order $N \log N$ . You might rightly think that this is wasteful, since it yields much more information than just the median (e.g., the upper and lower quartile points, the deciles, etc.). In fact, we saw in $\ S 8 . 5$ that the element $x _ { ( N - 1 ) / 2 }$ can be located in of order $N$ operations. Consult that section for routines, including a method for getting a good approximation to the median in a single pass through the data.

The mode of a probability distribution function $p ( x )$ is the value of $x$ where it takes on a maximum value. The mode is useful primarily when there is a single, sharp maximum, in which case it estimates the central value. Occasionally, a distribution will be bimodal, with two relative maxima; then one may wish to know the two modes individually. Note that, in such cases, the mean and median are not very useful, since they will give only a “compromise” value between the two peaks.

# CITED REFERENCES AND FURTHER READING:

Bevington, P.R., and Robinson, D.K. 2002, Data Reduction and Error Analysis for the Physical Sciences, 3rd ed. (New York: McGraw-Hil), Chapter 1.   
Spiegel, M.R., Schiller, J., and Srinivasan, R.A. 2000, Schaum’s Outline of Theory and Problem of Probability and Statistics,2nd ed. (New York: McGraw-Hill).   
Stuart, A., and Ord, J.K. 1994, Kendall’s Advanced Theory of Statistics, 6th ed. (London: Edward Arnold) [previous eds. published as Kendall, M., and Stuart, A., The Advanced Theory of Statistics], vol.1, $\ S 1 0 . 1 5$   
Norusis, M.J. 2006, SPSS 14.0 Guide to Data Analysis (Englewood Cliffs, NJ: Prentice-Hall).   
Chan, T.F., Golub, G.H., and LeVeque, R.J. 1983, “Algorithms for Computing the Sample Variance: Analysis and Recommendations,” American Statistician, vol. 37, pp. 242–247.[1]   
Cramér, H. 1946, Mathematical Methods of Statistics (Princeton, NJ: Princeton University Press), $\ S 1 5 . 1 0$ .[2]

# 14.2 Do Two Distributions Have the Same Means or Variances?

Not uncommonly we want to know whether two distributions have the same mean. For example, a first set of measured values may have been gathered before some event, a second set after it. We want to know whether the event, a “treatment” or a “change in a control parameter,” made a difference.

Our first thought is to ask “how many standard deviations” one sample mean is from the other. That number may in fact be a useful thing to know. It does relate to the strength or “importance” of a difference of means if that difference is genuine. However, by itself, it says nothing about whether the difference is genuine, that is, statistically significant. A difference of means can be very small compared to the standard deviation, and yet very significant, if the number of data points is large. Conversely, a difference may be moderately large but not significant, if the data are sparse. We will be meeting these distinct concepts of strength and significance several times in the next few sections.

A quantity that measures the significance of a difference of means is not the number of standard deviations that they are apart, but the number of so-called standard errors that they are apart. The standard error of a set of values measures the accuracy with which the sample mean estimates the population (or “true”) mean. Typically the standard error is equal to the sample’s standard deviation divided by the square root of the number of points in the sample.

# 14.2.1 Student's t-Test for Significantly Different Means

Applying the concept of standard error, the conventional statistic for measuring the significance of a difference of means is termed Student’s t. When the two distributions are thought to have the same variance, but possibly different means, then Student’s $t$ is computed as follows: First, estimate the standard error of the difference of the means, $s _ { D }$ , from the “pooled variance” by the formula

$$
s _ { D } = \sqrt { \frac { \sum _ { i \in A } ( x _ { i } - \overline { { x } } _ { A } ) ^ { 2 } + \sum _ { i \in B } ( x _ { i } - \overline { { x } } _ { B } ) ^ { 2 } } { N _ { A } + N _ { B } - 2 } \left( \frac { 1 } { N _ { A } } + \frac { 1 } { N _ { B } } \right) } 
$$

where each sum is over the points in one sample, the first or second; each mean likewise refers to one sample or the other; and $N _ { A }$ and $N _ { B }$ are the numbers of points in the first and second samples, respectively. Second, compute $t$ by

$$
t = { \frac { { \overline { { x } } } _ { A } - { \overline { { x } } } _ { B } } { s _ { D } } }
$$

Third, evaluate the $p$ -value or significance of this value of $t$ for Student’s distribution with $N _ { A } + N _ { B } - 2$ degrees of freedom, by equation (6.14.11).

The $p$ -value is a number between zero and one. It is the probability that $| t |$ could be this large or larger just by chance, for distributions with equal means. Therefore, a small numerical value of the $p$ -value (0.01 or 0.001) means that the observed difference is “very significant.” The function $A ( t | \nu )$ in equation (6.14.11) is one minus the $p$ -value.

As a routine, we have

void ttest(VecDoub_I &data1, VecDoub_I &data2, Doub &t, Doub &prob) Given the arrays data1[0..n1-1] and data2[0..n2-1], returns Student’s $t$ as $^ \texttt { t }$ , and its $p$ - value as prob, small values of prob indicating that the arrays have significantly different means. The data arrays are assumed to be drawn from populations with the same true variance. {

Beta beta;

Doub var1,var2,svar,df,ave1,ave2;   
Int n1 $=$ data1.size(), n2=data2.size();   
avevar(data1,ave1,var1);   
avevar(data2,ave2,var2);   
df=n1+n2-2;   
svar $^ { * = }$ ((n1-1)\*var1+(n2-1)\*var2)/df;   
$\mathtt { t = }$ (ave1-ave2)/sqrt(svar\*(1.0/n1+1.0/n2));   
prob beta.betai(0.5\*df,0.5,df/(df+t\*t));

See equation (6.14.11).

which makes use of the following routine for computing the mean and variance of a set of numbers,

void avevar(VecDoub_I &data, Doub &ave, Doub &var) {   
Given array data[0..n-1], returns its mean as ave and its variance as var. Doub s,ep; Int j, $\mathbf { n } { = }$ data.size(); ave=0.0; for ( $\scriptstyle { \dot { \ j } } = 0$ ;j<n;j++) ave $+ =$ data[j]; ave $\mathbf { \Omega } / = \mathbf { \Omega } _ { \mathrm { ~ n ~ } }$ ; var=ep=0.0; for $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<n;j++) { $\mathrm { s } =$ data[j]-ave; ep $+ = \textsf { s } ;$ ; var $+ =$ s\*s; var=(var-ep\*ep/n)/(n-1); Corrected two-pass formula (14.1.8)   
}

The next case to consider is where the two distributions have significantly different variances, but we nevertheless want to know if their means are the same or different. (A treatment for baldness has caused some patients to lose all their hair and turned others into werewolves, but we want to know if it helps cure baldness on the average!) Be suspicious of the unequal-variance $t$ -test: If two distributions have very different variances, then they may also be substantially different in shape; in that case, the difference of the means may not be a particularly useful thing to know.

To find out whether the two data sets have variances that are significantly different, you use the $F$ -test, described later on in this section.

The relevant statistic for the unequal-variance $t$ -test is

$$
t = \frac { \overline { { x } } _ { A } - \overline { { x } } _ { B } } { [ \mathrm { V a r } ( x _ { A } ) / N _ { A } + \mathrm { V a r } ( x _ { B } ) / N _ { B } ] ^ { 1 / 2 } }
$$

This statistic is distributed approximately as Student’s $t$ with a number of degrees of freedom equal to

$$
\begin{array} { r l r } {  { \frac { [ \frac { \mathrm { V a r } ( x _ { A } ) } { N _ { A } } + \frac { \mathrm { V a r } ( x _ { B } ) } { N _ { B } } ] ^ { 2 } } { [ \mathrm { V a r } ( x _ { A } ) / N _ { A } ] ^ { 2 } } } } \\ & { } & { \frac { [ \mathrm { V a r } ( x _ { A } ) / N _ { A } ] ^ { 2 } } { N _ { A } - 1 } + \frac { [ \mathrm { V a r } ( x _ { B } ) / N _ { B } ] ^ { 2 } } { N _ { B } - 1 } } \end{array}
$$

Expression (14.2.4) is in general not an integer, but equation (6.14.11) doesn’t care. The routine is

void tutest(VecDoub_I &data1, VecDoub_I &data2, Doub &t, Doub &prob) { Given the arrays data1[0..n1-1] and data2[0..n2-1], this routine returns Student’s t as t, and its $p$ -value as prob, small values of prob indicating that the arrays have significantly different means. The data arrays are allowed to be drawn from populations with unequal variances.

Beta beta;   
Doub var1,var2,df,ave1,ave2;   
Int n1 $=$ data1.size(), $\mathtt { n 2 } =$ data2.size();   
avevar(data1,ave1,var1);   
avevar(data2,ave2,var2);   
$\scriptstyle \pm =$ (ave1-ave2)/sqrt(var1/n1+var2/n2);   
df $\mathop { : = }$ SQR(var1/n1+var2/n2)/(SQR(var1/n1)/(n1-1)+SQR(var2/n2)/(n2-1));   
prob=beta.betai(0.5\*df,0.5,df/(df+SQR(t)));

# }

Our final example of a Student’s $t$ -test is the case of paired samples. Here we imagine that much of the variance in both samples is due to effects that are point-bypoint identical in the two samples. For example, we might have two job candidates who have each been rated by the same ten members of a hiring committee. We want to know if the means of the ten scores differ significantly. We first try ttest above, and obtain a value of prob that is not especially significant (e.g., $> 0 . 0 5 \ )$ ). But perhaps the significance is being washed out by the tendency of some committee members always to give high scores and others always to give low scores, which increases the apparent variance and thus decreases the significance of any difference in the means. We thus try the paired-sample formulas,

$$
\begin{array} { l } { \displaystyle \mathrm { C o v } ( x _ { A } , x _ { B } ) \equiv \frac { 1 } { N - 1 } \sum _ { i = 0 } ^ { N - 1 } ( x _ { A i } - \overline { { x } } _ { A } ) ( x _ { B i } - \overline { { x } } _ { B } ) } \\ { \displaystyle s _ { D } = \left[ \frac { \mathrm { V a r } ( x _ { A } ) + \mathrm { V a r } ( x _ { B } ) - 2 \mathrm { C o v } ( x _ { A } , x _ { B } ) } { N } \right] ^ { 1 / 2 } } \\ { \displaystyle t = \frac { \overline { { x } } _ { A } - \overline { { x } } _ { B } } { s _ { D } } } \end{array}
$$

where $N$ is the number in each sample (number of pairs). Notice that it is important that a particular value of $i$ label the corresponding points in each sample, that is, the ones that are paired. The $p$ -value for the $t$ statistic in (14.2.7) is evaluated for $N - 1$ degrees of freedom.

The routine is

# void tptest(VecDoub_I &data1, VecDoub_I &data2, Doub &t, Doub &prob) {

Given the paired arrays data1[0..n-1] and data2[0..n-1], this routine returns Student’s t for paired data as t, and its $p$ -value as prob, small values of prob indicating a significant difference of means.

# Beta beta;

Int j, $\mathbf { n } =$ data1.size();   
Doub var1,var2,ave1,ave2,sd,df,cov=0.0;   
avevar(data1,ave1,var1);   
avevar(data2,ave2,var2);   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n; $j + + ,$ ) cov $+ =$ (data1[j]-ave1)\*(data2[j]-ave2);   
cov $\prime =$ (df=n-1);   
sd=sqrt((var1+var2-2.0\*cov)/n);   
$\mathtt { t } =$ (ave1-ave2)/sd;   
prob=beta.betai(0.5\*df,0.5,df/(df+t\*t));

# 14.2.2 F-Test for Significantly Different Variances

The $F$ -test tests the hypothesis that two samples have different variances by trying to reject the null hypothesis that their variances are actually consistent. The statistic $F$ is the ratio of one variance to the other, so values either $\gg 1$ or $\ll 1$ will indicate very significant differences. The distribution of $F$ in the null case is given in equation (6.14.49), which is evaluated using the routine betai. In the most common case, we are willing to disprove the null hypothesis (of equal variances) by either very large or very small values of $F$ , so the correct $p$ -value is two-tailed, the sum of two incomplete beta functions. It turns out, by equation (6.4.3), that the two tails are always equal; we need compute only one, and double it. Occasionally, when the null hypothesis is strongly viable, the identity of the two tails can become confused, giving an indicated probability greater than one. Changing the probability to two minus itself correctly exchanges the tails. These considerations and equation (6.4.3) give the routine

# id ftest(VecDoub_I &data1, VecDoub_I &data2, Doub &f, Doub &prob) {

Given the arrays data1[0..n1-1] and data2[0..n2-1], this routine returns the value of f, and its $p$ -value as prob. Small values of prob indicate that the two arrays have significantly different variances.

Beta beta;   
Doub var1,var2,ave1,ave2,df1,df2;   
Int n1 $=$ data1.size(), n2=data2.size();   
avevar(data1,ave1,var1);   
avevar(data2,ave2,var2);   
if (var1 $>$ var2) { Make $F$ the ratio of the larger variance to the smaller $\mathtt { f } =$ var1/var2; one. df1=n1-1; df2=n2-1;   
} else { $\mathtt { f } =$ var2/var1; df1=n2-1; df2=n1-1;   
}   
prob $=$ 2.0\*beta.betai(0.5\*df2,0.5\*df1,df2/(df2+df1\*f));   
if (prob $>$ 1.0) prob $^ { = 2 }$ .-prob;

# CITED REFERENCES AND FURTHER READING:

Spiegel, M.R., Schiller, J., and Srinivasan, R.A. 2000, Schaum’s Outline of Theory and Problem of Probability and Statistics,2nd ed.(New York: McGraw-Hil).   
Lupton, R. 1993, Statistics in Theory and Practice (Princeton, NJ: Princeton University Press), Chapter 9.   
Devore, J.L. 2003, Probability and Statistics for Engineering and the Sciences, 6th ed. (Belmont, CA: Duxbury Press), Chapters 7–8.   
Norusis, M.J. 2006, SPSS 14.0 Guide to Data Analysis (Englewood Cliffs, NJ: Prentice-Hall).

# 14.3 Are Two Distributions Different?

Given two sets of data, we can generalize the questions asked in the previous section and ask the single question: Are the two sets drawn from the same distribution function, or from different distribution functions? Equivalently, in proper statistical language, “Can we disprove, to a certain required level of significance, the null hypothesis that two data sets are drawn from the same population distribution function?” Disproving the null hypothesis in effect proves that the data sets are from different distributions. Failing to disprove the null hypothesis, on the other hand, only shows that the data sets can be consistent with a single distribution function. One can never prove that two data sets come from a single distribution, since, e.g., no practical amount of data can distinguish between two distributions that differ only by one part in $1 0 ^ { 1 0 }$ .

Proving that two distributions are different, or showing that they are consistent, is a task that comes up all the time in many areas of research: Are the visible stars distributed uniformly in the sky? (That is, is the distribution of stars as a function of declination — position in the sky — the same as the distribution of sky area as a function of declination?) Are educational patterns the same in Brooklyn as in the Bronx? (That is, are the distributions of people as a function of last-grade-attended the same?) Do two brands of fluorescent lights have the same distribution of burnout times? Is the incidence of chicken pox the same for first-born, second-born, third-born children, etc.?

These four examples illustrate the four combinations arising from two different dichotomies: (1) The data are either continuous or binned. (2) Either we wish to compare one data set to a known distribution, or we wish to compare two equally unknown data sets. The data sets on fluorescent lights and on stars are continuous, since we can be given lists of individual burnout times or of stellar positions. The data sets on chicken pox and educational level are binned, since we are given tables of numbers of events in discrete categories: first-born, second-born, etc.; or 6th grade, 7th grade, etc. Stars and chicken pox, on the other hand, share the property that the null hypothesis is a known distribution (distribution of area in the sky, or incidence of chicken pox in the general population). Fluorescent lights and educational level involve the comparison of two equally unknown data sets (the two brands, or Brooklyn and the Bronx).

One can always turn continuous data into binned data, by grouping the events into specified ranges of the continuous variable(s): declinations between 0 and 10 degrees, 10 and 20, 20 and 30, etc. Binning involves a loss of information, however. Also, there is often considerable arbitrariness as to how the bins should be chosen. Along with many other investigators, we prefer to avoid unnecessary binning of data.

The accepted test for differences between binned distributions is the chi-square test. For continuous data as a function of a single variable, the most generally accepted test is the Kolmogorov-Smirnov test. We consider each in turn.

# 14.3.1 Chi-Square Test

Suppose that $N _ { i }$ is the number of events observed in the $i$ th bin, and that $n _ { i }$ is the number expected according to some known distribution. Note that the $N _ { i }$ ’s are integers, while the $n _ { i }$ ’s may not be. Then the chi-square statistic is

$$
\chi ^ { 2 } = \sum _ { i } \frac { ( N _ { i } - n _ { i } ) ^ { 2 } } { n _ { i } }
$$

where the sum is over all bins. A large value of $\chi ^ { 2 }$ indicates that the null hypothesis (that the $N _ { i }$ ’s are drawn from the population represented by the $n _ { i }$ ’s) is

rather unlikely.

Any term $j$ in (14.3.1) with $0 = n _ { j } = N _ { j }$ should be omitted from the sum. A term with $n _ { j } = 0 , ~ N _ { j } \neq 0$ gives an infinite $\chi ^ { 2 }$ , as it should, since in this case the $N _ { i }$ ’s cannot possibly be drawn from the $n _ { i }$ ’s!

The chi-square probability function $ { \mathcal { Q } } ( \chi ^ { 2 } | \nu )$ is an incomplete gamma function, and was already discussed in $\ S 6 . 1 4$ (see equation 6.14.38). Strictly speaking, $ { \mathcal { Q } } ( \chi ^ { 2 } | \nu )$ is the probability that the sum of the squares of $\nu$ random normal variables of unit variance (and zero mean) will be greater than $\chi ^ { 2 }$ . The terms in the sum (14.3.1) are not exactly the squares of a normal variable. However, if the number of events in each bin is large $( \gg 1 )$ ), then the normal distribution is approximately achieved and the chi-square probability function is a good approximation to the distribution of (14.3.1) in the case of the null hypothesis. Its use to estimate the $p$ -value significance of the chi-square test is standard (but see $\ S 1 4 . 3 . 2 )$ .

The appropriate value of $\nu$ , the number of degrees of freedom, bears some additional discussion. If the data are collected with the model $n _ { i }$ ’s fixed — that is, not later renormalized to fit the total observed number of events $\Sigma N _ { i }$ — then $\nu$ equals the number of bins $N _ { B }$ . (Note that this is not the total number of events!) Much more commonly, the $n _ { i }$ ’s are normalized after the fact so that their sum equals the sum of the $N _ { i }$ ’s. In this case, the correct value for $\nu$ is $N _ { B } - 1$ , and the model is said to have one constraint (knstrn $\sp { = 1 }$ in the program below). If the model that gives the $n _ { i }$ ’s has additional free parameters that were adjusted after the fact to agree with the data, then each of these additional “fitted” parameters decreases $\nu$ (and increases knstrn) by one additional unit.

We have, then, the following program:

# oid chsone(VecDoub_I &bins, VecDoub_I &ebins, Doub &df,

Doub &chsq, Doub &prob, const Int knstrn $^ { = 1 }$ ) {

Given the array bins[0..nbins-1] containing the observed numbers of events, and an array ebins[0..nbins-1] containing the expected numbers of events, and given the number of constraints knstrn (normally one), this routine returns (trivially) the number of degrees of freedom df, and (nontrivially) the chi-square chsq and the $p$ -value prob. A small value of prob indicates a significant difference between the distributions bins and ebins. Note that bins and ebins are both double arrays, although bins will normally contain integer values.

Gamma gam;   
Int j,nbins=bins.size();   
Doub temp;   
df=nbins-knstrn;   
chsq=0.0;   
for ( $\scriptstyle { \dot { \ j } } = 0$ ;j<nbins;j++) { if (ebins[j]<0.0 || (ebins[j] $= = 0$ . && bins[j]>0.)) throw("Bad expected number in chsone"); if (ebins[j] $= = 0 \ . 0$ && bins[j] $= = 0 \ . 0$ ) { --df; No data means one less degree of free-} else { dom. temp=bins[j]-ebins[j]; chsq $+ =$ temp\*temp/ebins[j]; }   
prob=gam.gammq(0.5\*df,0.5\*chsq); Chi-square probability function. See $\ S 6 . 2$ .

Next we consider the case of comparing two binned data sets. Let $R _ { i }$ be the number of events in bin $i$ for the first data set and $S _ { i }$ the number of events in the same bin $i$ for the second data set. Then the chi-square statistic is

$$
\chi ^ { 2 } = \sum _ { i } \frac { ( R _ { i } - S _ { i } ) ^ { 2 } } { R _ { i } + S _ { i } }
$$

Comparing (14.3.2) to (14.3.1), you should note that the denominator of (14.3.2) is not just the average of $R _ { i }$ and $S _ { i }$ (which would be an estimator of $n _ { i }$ in 14.3.1). Rather, it is twice the average, the sum. The reason is that each term in a chi-square sum is supposed to approximate the square of a normally distributed quantity with unit variance. The variance of the difference of two normal quantities is the sum of their individual variances, not the average.

If the data were collected in such a way that the sum of the $R _ { i }$ ’s is necessarily equal to the sum of $S _ { i }$ ’s, then the number of degrees of freedom is equal to one less than the number of bins, $N _ { B } - 1$ (that is, $\mathtt { k n s t r n } = \mathtt { l } _ { }$ ), the usual case. If this requirement were absent, then the number of degrees of freedom would be $N _ { B }$ . Example: A birdwatcher wants to know whether the distribution of sighted birds as a function of species is the same this year as last. Each bin corresponds to one species. If the birdwatcher takes his data to be the first 1000 birds that he saw in each year, then the number of degrees of freedom is $N _ { B } - 1$ . If he takes his data to be all the birds he saw on a random sample of days, the same days in each year, then the number of degrees of freedom is $N _ { B }$ $( \mathtt { k n s t r n } = 0 )$ ). In this latter case, note that he is also testing whether the birds were more numerous overall in one year or the other: That is the extra degree of freedom. Of course, any additional constraints on the data set lower the number of degrees of freedom (i.e., increase knstrn to more positive values) in accordance with their number.

The program is

# void chstwo(VecDoub_I &bins1, VecDoub_I &bins2, Doub &df,

Doub &chsq, Doub &prob, const Int knstrn $^ { = 1 }$ ) {

Given the arrays bins1[0..nbins-1] and bins2[0..nbins-1], containing two sets of binned data, and given the number of constraints knstrn (normally 1 or 0), this routine returns the number of degrees of freedom df, the chi-square chsq, and the $p$ -value prob. A small value of prob indicates a significant difference between the distributions bins1 and bins2. Note that bins1 and bins2 are both double arrays, although they will normally contain integer values.

Gamma gam;   
Int j,nbins=bins1.size();   
Doub temp;   
df=nbins-knstrn;   
chsq ${ = } 0$ .0;   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<nbins;j++) if (bins1[j] $\mathrm { = = ~ 0 , 0 }$ && bins2[j] $\mathrm { ~  ~ \omega ~ } = \mathrm { ~  ~ 0 ~ } . 0$ ) --df; No data means one less degree of freeelse { dom. temp=bins1[j]-bins2[j]; chsq $+ =$ temp\*temp/(bins1[j]+bins2[j]); }   
prob=gam.gammq(0.5\*df,0.5\*chsq); Chi-square probability function. See $\ S 6 . 2$

# }

Equation (14.3.2) and the routine chstwo both apply to the case where the total number of data points is the same in the two binned sets, or to the case where any difference in the totals is part of what is being tested for. For intentionally unequal sample sizes, the formula analogous to (14.3.2) is

$$
\chi ^ { 2 } = \sum _ { i } \frac { ( \sqrt { S / R } R i - \sqrt { R / S } S _ { i } ) ^ { 2 } } { R _ { i } + S _ { i } }
$$

where

$$
R \equiv \sum _ { i } R _ { i } \qquad S \equiv \sum _ { i } S _ { i }
$$

are the respective numbers of data points. It is straightforward to make the corresponding change in chstwo. The fact that $R _ { i }$ and $S _ { i }$ occur in the denominator of equation (14.3.3) with equal weights may seem unintuitive, but the following heuristic derivation shows how this comes about: In the null hypothesis that $R _ { i }$ and $S _ { i }$ are drawn from the same distribution, we can estimate the probability associated with bin $i$ as

$$
\widehat { p } _ { i } = \frac { R _ { i } + S _ { i } } { R + S }
$$

The expected number of counts is thus

$$
{ \widehat { R } } _ { i } = R { \widehat { p } } _ { i } \qquad { \mathrm { a n d } } \qquad { \widehat { S } } _ { i } = S { \widehat { p } } _ { i }
$$

and the chi-square statistic summing over all observations is

$$
\chi ^ { 2 } = \sum _ { i } \frac { ( R _ { i } - \widehat { R } _ { i } ) ^ { 2 } } { \widehat { R } _ { i } } + \sum _ { i } \frac { ( S _ { i } - \widehat { S } _ { i } ) ^ { 2 } } { \widehat { S } _ { i } }
$$

Substituting equations (14.3.6) and (14.3.5) into equation (14.3.7) gives, after some algebra, exactly equation (14.3.3). Although there are $2 N _ { B }$ terms in equation (14.3.7), the number of degrees of freedom is actually $N _ { B } - 1$ (minus any additional constraints), the same as equation (14.3.2), because we implicitly estimated $N _ { B } + 1$ parameters, the $\widehat { p } _ { i }$ ’s and the ratio of the two sample sizes. This number of degrees of freedom must thus be subtracted from the original $2 N _ { B }$ .

For three or more samples, see equation (14.4.3) and related discussion.

# 14.3.2 Chi-Square with Small Numbers of Counts

When a significant fraction of bins have small numbers of counts $\approx 1 0$ , say), then the $\chi ^ { 2 }$ statistics (14.3.1), (14.3.2), and (14.3.3) are not well approximated by a chi-square probability function. Let us quantify this problem and suggest some remedies.

Consider first equation (14.3.1). In the null hypothesis, the count in an individual bin, $N _ { i }$ , is a Poisson deviate of mean $n _ { i }$ , so it occurs with probability

$$
p ( N _ { i } | n _ { i } ) = \exp ( - n _ { i } ) \frac { n _ { i } ^ { N _ { i } } } { N _ { i } ! }
$$

(cf. equation 6.14.61). We can calculate the mean $\mu$ and variance $\sigma ^ { 2 }$ of the term $( N _ { i } - n _ { i } ) ^ { 2 } / n _ { i }$ by evaluating the appropriate expectation values. There are various analytical ways to do this. The sums, and the answers, are

$$
\begin{array} { c } { { \displaystyle \mu = \sum _ { N _ { i } = 0 } ^ { \infty } p ( N _ { i } | n _ { i } ) \frac { ( N _ { i } - n _ { i } ) ^ { 2 } } { n _ { i } } = 1 } } \\ { { \displaystyle \sigma ^ { 2 } = \left\{ \sum _ { N _ { i } = 0 } ^ { \infty } p ( N _ { i } | n _ { i } ) \left[ \frac { ( N _ { i } - n _ { i } ) ^ { 2 } } { n _ { i } } \right] ^ { 2 } \right\} - \mu ^ { 2 } = 2 + \frac { 1 } { n _ { i } } } } \end{array}
$$

Now we can see what the problem is: Equation (14.3.9) says that each term in (14.3.1) adds, on average, 1 to the value of the $\chi ^ { 2 }$ statistic, and slightly more than 2 to its variance. But the variance of the chi-square probability function is exactly twice its mean (equation 6.14.37). If a significant fraction of $n _ { i }$ ’s are small, then quite probable values of the $\chi ^ { 2 }$ statistic will appear to lie farther out on the tail than they actually are, so that the null hypothesis may be rejected even when it is true.

Several approximate remedies are possible. One is simply to rescale the observed $\chi ^ { 2 }$ statistic so as to “fix” its variance, an idea due to Lucy [1]. If we define

$$
Y ^ { 2 } \equiv \nu + \sqrt { \frac { 2 \nu } { 2 \nu + \sum _ { i } n _ { i } ^ { - 1 } } } \left( \chi ^ { 2 } - \nu \right)
$$

where $\nu$ is the number of degrees of freedom (see discussion above), then $Y ^ { 2 }$ is asymptotically approximated by the chi-square probability function even when many $n _ { i }$ ’s are small. The basic idea in (14.3.10) is to subtract off the mean, rescale the difference from the mean, and then add back the mean. Lucy [1] also defines a similar $Z ^ { 2 }$ statistic by rescaling not the $\chi ^ { 2 }$ sum of all the terms, but the terms individually, using equation (14.3.9) separately for each.

Another possibility, valid when $\nu$ is large, is to use the central limit theorem directly. From its mean and standard deviation, we now know that the $\chi ^ { 2 }$ statistic must be approximately the normal distribution,

$$
\chi ^ { 2 } \sim \mathrm { N } \left( \nu , \left[ 2 \nu + \sum _ { i } n _ { i } ^ { - 1 } \right] ^ { 1 / 2 } \right)
$$

We can then obtain $p$ -values from equation (6.14.2), computing a complementary error function. (The $p$ -value is one minus that cdf.)

The same ideas go through in the case of two binned data sets, with counts $R _ { i }$ and $S _ { i }$ , and total numbers of counts $R$ and $S$ (equation 14.3.3, with equation 14.3.2 as the special case with $R = S$ ). Now, in the null hypothesis, and glossing over some technical issues beyond our scope, we can think of $T _ { i } \equiv R _ { i } + S _ { i }$ as being fixed, while $R _ { i }$ is a random variable drawn from the binomial distribution

$$
R _ { i } \sim \mathrm { B i n o m i a l } \left( T _ { i } , { \frac { R } { R + S } } \right)
$$

(see equation 6.14.67). Calculating moments over the binomial distribution, one can obtain as analogs of equations (14.3.9)

$$
\left. \begin{array} { c l c r } { { \mu = 1 } } \\ { { } } \\ { { \sigma ^ { 2 } = 2 + \left[ \displaystyle \frac { ( R + S ) ^ { 2 } } { R S } - 6 \right] \displaystyle \frac { 1 } { R _ { i } + S _ { i } } } } \end{array} \right.
$$

Notice that, now, depending on the values of $R$ and $S$ , the variance can be either greater or less than its nominal value 2, and that it is less than 2 for the case $R \ : = \ : S$ . The formulas (14.3.9) and (14.3.13) are originally due to Haldane [2] (see also [3]).

Summing over $i$ , one obtains the analogs of equations (14.3.10) and (14.3.11) simply by the replacement,

$$
\sum _ { i } n _ { i } ^ { - 1 } \longrightarrow \left[ \frac { ( R + S ) ^ { 2 } } { R S } - 6 \right] \sum _ { i } \frac { 1 } { R _ { i } + S _ { i } }
$$

In fact, equation (14.3.9) is a limiting form of equation (14.3.13) in just the same limit that Poisson is a limiting form of binomial, namely

$$
S \to \infty , \quad { \frac { R } { R + S } } S _ { i } \to n _ { i } , \quad R _ { i } \to N _ { i }
$$

There are also other ways of treating small-number counts, including the likelihood ratio test [4], the modified Neyman $\chi ^ { 2 }$ [5], and the $c h i$ -square-gamma statistic [5].

![](images/de104fa0323fde8e1cda23020887e958b25f755d6ee9af7d78ecae2df333e5bf.jpg)  
Figure 14.3.1. Kolmogorov-Smirnov statistic $D$ . A measured distribution of values in $x$ (shown as $N$ dots on the lower abscissa) is to be compared with a theoretical distribution whose cumulative probability distribution is plotted as $P ( x )$ . A step-function cumulative probability distribution $S _ { N } ( x )$ is constructed, one that rises an equal amount at each measured point. $D$ is the greatest distance between the two cumulative distributions.

# 14.3.3 Kolmogorov-Smirnov Test

The Kolmogorov-Smirnov (or $K – S$ ) test is applicable to unbinned distributions that are functions of a single independent variable, that is, to data sets where each data point can be associated with a single number (lifetime of each lightbulb when it burns out, or declination of each star). In such cases, the list of data points can be easily converted to an unbiased estimator $S _ { N } ( x )$ of the cumulative distribution function of the probability distribution from which it was drawn: If the $N$ events are located at values $x _ { i }$ ; $i = 0 , \ldots , N - 1$ , then $S _ { N } ( x )$ is the function giving the fraction of data points to the left of a given value $x$ . This function is obviously constant between consecutive (i.e., sorted into ascending order) $x _ { i }$ ’s and jumps by the same constant $1 / N$ at each $x _ { i }$ . (See Figure 14.3.1.)

Different distribution functions, or sets of data, give different cumulative distribution function estimates by the above procedure. However, all cumulative distribution functions agree at the smallest allowable value of $x$ (where they are zero) and at the largest allowable value of $x$ (where they are unity). (The smallest and largest values might of course be $\pm \infty$ .) So it is the behavior between the largest and smallest values that distinguishes distributions.

One can think of any number of statistics to measure the overall difference between two cumulative distribution functions: the absolute value of the area between them, for example, or their integrated mean square difference. The Kolmogorov-Smirnov $D$ is a particularly simple measure: It is defined as the maximum value of the absolute difference between two cumulative distribution functions. Thus, for comparing one data set’s $S _ { N } ( x )$ to a known cumulative distribution function $P ( x )$ , the ${ \mathrm { K } } { - } S$ statistic is

$$
D = \operatorname* { m a x } _ { - \infty < x < \infty } | S _ { N } ( x ) - P ( x ) |
$$

while for comparing two different cumulative distribution functions $S _ { N _ { 1 } } ( x )$ and $S _ { N _ { 2 } } ( x )$ , the ${ \mathrm { K } } { - } S$ statistic is

$$
D = \operatorname* { m a x } _ { - \infty < x < \infty } \left| S _ { N _ { 1 } } ( x ) - S _ { N _ { 2 } } ( x ) \right|
$$

What makes the K–S statistic useful is that its distribution in the case of the null hypothesis (data sets drawn from the same distribution) can be calculated, at least to a useful approximation, thus giving the $p$ -value significance of any observed nonzero value of $D$ . A central feature of the K–S test is that it is invariant under reparametrization of $x$ ; in other words, you can locally slide or stretch the $x$ -axis in Figure 14.3.1, and the maximum distance $D$ remains unchanged. For example, you will get the same significance using $x$ as using $\log x$ .

The function that enters into the calculation of the $p$ -value was discussed previously in $\ S 6 . 1 4$ , was defined in equations (6.14.56) and (6.14.57), and was implemented in the object KSdist. In terms of the function $Q _ { K S }$ , the $p$ -value of an observed value of $D$ (as a disproof of the null hypothesis that the distributions are the same) is given approximately [6] by the formula

$$
\mathrm { P r o b a b i l i t y ~ } ( D > \mathrm { o b s e r v e d ~ } ) = { \cal Q } \kappa s \Big ( \left[ \sqrt { N _ { e } } + 0 . 1 2 + 0 . 1 1 / \sqrt { N _ { e } } \right] D \Big )
$$

where $N _ { e }$ is the effective number of data points, $N _ { e } = N$ for the case (14.3.16) of one distribution, and

$$
N _ { e } = \frac { N _ { 1 } N _ { 2 } } { N _ { 1 } + N _ { 2 } }
$$

for the case (14.3.17) of two distributions, where $N _ { 1 }$ is the number of data points in the first distribution and $N _ { 2 }$ the number in the second.

The nature of the approximation involved in (14.3.18) is that it becomes asymptotically accurate as the $N _ { e }$ becomes large, but is already quite good for $N _ { e } \ge 4$ , as small a number as one might ever actually use. (See [6].)

Here is the routine for the case of one distribution:

# void ksone(VecDoub_IO &data, Doub func(const Doub), Doub &d, Doub &prob)

Given an array data[0..n-1], and given a user-supplied function of a single variable func that is a cumulative distribution function ranging from 0 (for smallest values of its argument) to 1 (for largest values of its argument), this routine returns the $\mathsf { K } { \mathsf { - } } { \mathsf { S } }$ statistic d and the $p$ -value prob. Small values of prob show that the cumulative distribution function of data is significantly different from func. The array data is modified by being sorted into ascending order. {

Int j, $\mathbf { n } =$ data.size();   
Doub dt,en,ff,fn,fo ${ = } 0$ .0;   
KSdist ks;   
sort(data);   
$\Theta \mathtt { n } = \mathtt { n }$ ;   
$\mathtt { d } \mathtt { = } 0$ .0;   
for (j=0;j<n;j++) { fn=(j+1)/en;   
If the data are already sorted into ascending order, then this call can be omitted.   
Loop over the sorted data points.   
Data’s c.d.f. after this step. ff=func(data[j]); dt=MAX(abs(fo-ff),abs(fn-ff)); if (dt $>$ d) d=dt; fo=fn;   
}   
en $\equiv$ sqrt(en);   
prob=ks.qks((en+0.12+0.11/en)\*d); Compare to the user-supplied function.   
Maximum distance.

Compute $p$ -value.

While the K-S statistic is intended for use with a continuous distribution, it can also be used for a discrete distribution. In this case, it can be shown that the test is conservative, that is, the statistic returned is no larger than in the continuous case. If you allow discrete variables in the case of two distributions, you have to consider how to deal with ties. The standard way to handle ties is to combine all the tied data points and add them to the cdf at once (see, e.g., [7]). This refinement is included in the routine kstwo.

# void kstwo(VecDoub_IO &data1, VecDoub_IO &data2, Doub &d, Doub &prob)

Given an array data1[0..n1-1], and an array data2[0..n2-1], this routine returns the K–S statistic d and the $p$ -value prob for the null hypothesis that the data sets are drawn from the same distribution. Small values of prob show that the cumulative distribution function of data1 is significantly different from that of data2. The arrays data1 and data2 are modified by being sorted into ascending order.

Int j $_ { 1 = 0 }$ ,j $_ { 2 } = 0$ ,n1=data1.size(),n2=data2.size();   
Doub d1,d2,dt,en1,en2,en,fn $\mathtt { \Omega } = 0$ .0,fn2=0.0;   
KSdist ks;   
sort(data1);   
sort(data2);   
en1=n1;   
en2=n2;   
$\mathtt { d } \mathtt { = } 0$ .0;   
while (j1 < n1 && j2 < n2) { If we are not done... if ((d1 $=$ data1[j1]) $< =$ ( $\scriptstyle \mathrm { d } 2 =$ data2[j2])) Next step is in data1. do fn1=++j1/en1; while (j1 $<$ n1 && d1 $= =$ data1[j1]); if (d2 $< =$ d1) Next step is in data2. do fn2 $= + \cdot$ +j2/en2; while (j2 $<$ n2 && d2 $= =$ data2[j2]); if ((dt=abs(fn2-fn1)) $>$ d) d=dt;   
}   
en=sqrt(en1\*en2/(en1+en2));   
prob=ks.qks((en+0.12+0.11/en)\*d); Compute $p$ -value.

# 14.3.4 Variants on the K-S Test

The sensitivity of the $\mathrm { K } { - } S$ test to deviations from a cumulative distribution function $P ( x )$ is not independent of $x$ . In fact, the K–S test tends to be most sensitive around the median value, where $P ( x ) = 0 . 5$ , and less sensitive at the extreme ends of the distribution, where $P ( x )$ is near 0 or 1. The reason is that the difference $| S _ { N } ( x ) - P ( x ) |$ does not, in the null hypothesis, have a probability distribution that is independent of $x$ . Rather, its variance is proportional to $P ( x ) [ 1 - P ( x ) ]$ , which is largest at $P = 0 . 5$ . Since the K–S statistic (14.3.16) is the maximum difference over all $x$ of two cumulative distribution functions, a deviation that might be statistically significant at its own value of $x$ gets compared to the expected chance deviation at $P = 0 . 5$ and is thus discounted. A result is that, while the $\mathrm { K } { - } S$ test is good at finding shifts in a probability distribution, especially changes in the median value, it is not always so good at finding spreads, which more affect the tails of the probability distribution, and which may leave the median unchanged.

One way of increasing the power of the K–S statistic out on the tails is to replace $D$ (equation 14.3.16) by a so-called stabilized or weighted statistic [8-10], for example the Anderson-Darling statistic,

$$
D ^ { * } = \operatorname* { m a x } _ { - \infty < x < \infty } { \frac { | S _ { N } ( x ) - P ( x ) | } { \sqrt { P ( x ) [ 1 - P ( x ) ] } } }
$$

Unfortunately, there is no simple formula analogous to equation (14.3.18) for this statistic, although Noe´ [11] gives a computational method using a recursion relation and provides a graph of numerical results. There are many other possible similar statistics, for example

$$
D ^ { * * } = \int _ { P = 0 } ^ { 1 } \frac { [ S _ { N } ( x ) - P ( x ) ] ^ { 2 } } { P ( x ) [ 1 - P ( x ) ] } d P ( x )
$$

which is also discussed by Anderson and Darling (see [9]).

Another approach, which we prefer as simpler and more direct, is due to Kuiper [12,13]. We already mentioned that the standard K–S test is invariant under reparametrizations of the variable $x$ . An even more general symmetry, which guarantees equal sensitivities at all values of $x$ , is to wrap the $x$ -axis around into a circle (identifying the points at $\pm \infty$ ), and to look for a statistic that is now invariant under all shifts and parametrizations on the circle. This allows, for example, a probability distribution to be “cut” at some central value of $x$ and the left and right halves to be interchanged, without altering the statistic or its significance.

Kuiper’s statistic, defined as

$$
V = D _ { + } + D _ { - } = \operatorname* { m a x } _ { - \infty < x < \infty } \left[ S _ { N } ( x ) - P ( x ) \right] + \operatorname* { m a x } _ { - \infty < x < \infty } \left[ P ( x ) - S _ { N } ( x ) \right]
$$

is the sum of the maximum distance of $S _ { N } ( x )$ above and below $P ( x )$ . You should be able to convince yourself that this statistic has the desired invariance on the circle: Sketch the indefinite integral of two probability distributions defined on the circle as a function of angle around the circle, as the angle goes through several times $3 6 0 ^ { \circ }$ . If you change the starting point of the integration, $D _ { + }$ and $D _ { - }$ change individually, but their sum is constant.

Furthermore, there is a simple formula for the asymptotic distribution of the statistic $V$ , directly analogous to equations (14.3.18) – (14.3.19). Let

$$
\mathcal Q _ { K P } ( \lambda ) = 2 \sum _ { j = 1 } ^ { \infty } ( 4 j ^ { 2 } \lambda ^ { 2 } - 1 ) e ^ { - 2 j ^ { 2 } \lambda ^ { 2 } }
$$

which is monotonic and satisfies

$$
\begin{array} { r } { \mathcal { Q } _ { K P } ( 0 ) = 1 \qquad \mathcal { Q } _ { K P } ( \infty ) = 0 } \end{array}
$$

In terms of this function the $p$ -value is [6]

$$
\mathrm { P r o b a b i l i t y ~ } ( V > \mathrm { o b s e r v e d } ) = \mathcal { Q } _ { K P } \left( \left[ \sqrt { N _ { e } } + 0 . 1 5 5 + 0 . 2 4 / \sqrt { N _ { e } } \right] V \right)
$$

Here $N _ { e }$ is $N$ in the one-sample case or is given by equation (14.3.19) in the case of two samples.

Of course, Kuiper’s test is ideal for any problem originally defined on a circle, for example, to test whether the distribution in longitude of something agrees with some theory, or whether two somethings have different distributions in longitude. (See also [14].)

We will leave to you the coding of routines analogous to ksone, kstwo, and KSdist:: qks. (For $\lambda < 0 . 4$ , don’t try to do the sum 14.3.23. Its value is 1, to 7 figures, but the series can require many terms to converge, and loses accuracy to roundoff.)

Two final cautionary notes: First, we should mention that all varieties of the K–S test lack the ability to discriminate some kinds of distributions. A simple example is a probability distribution with a narrow “notch” within which the probability falls to zero. Such a distribution is of course ruled out by the existence of even one data point within the notch, but, because of its cumulative nature, a $\mathrm { K } { - } S$ test would require many data points in the notch before signaling a discrepancy.

Second, we should note that, if you estimate any parameters from a data set (e.g., a mean and variance), then the distribution of the K–S statistic $D$ for a cumulative distribution function $P ( x )$ that uses the estimated parameters is no longer given by equation (14.3.18). In general, you will have to determine the new distribution yourself, e.g., by Monte Carlo methods.

# CITED REFERENCES AND FURTHER READING:

Devore, J.L. 2003, Probability and Statistics for Engineering and the Sciences, 6th ed. (Belmont, CA: Duxbury Press), Chapter 14. Lupton, R. 1993, Statistics in Theory and Practice (Princeton, NJ: Princeton University Press), Chapter 14. Lucy, L.B. 2000, “Hypothesis Testing for Meagre Data Sets,” Monthly Notices of the Royal Astronomical Society, vol. 318, pp. 92-100.[1] Haldane, J.B.S. 1937, “The Exact Value of the Moments of the Distribution of $\chi ^ { 2 }$ , Used as a Test of Goodness of Fit, When Expectations Are Small,” Biometrika, vol. 29, pp. 133–143.[2] Read, T.R.C., and Cressie, N.A.C. 1988, Goodness-of-Fit Statistics for Discrete Multivariate Data (New York: Springer), pp. 140–144.[3] Baker, S., and Cousins, R.D. 1984, “Clarification of the Use of Chi-Square and Likelihood Functions in Fits to Histograms,” Nuclear Instruments and Methods in Physics Research, vol. 221, pp. 437–442.[4] Mighell, K.J. 1999, “Parameter Estimation in Astronomy with Poisson-Distributed Data. I.The $\chi _ { \gamma } ^ { 2 }$ Statistic,” Astrophysical Journal, vol. 518, pp. 380–393[5] Stephens, M.A. 1970, “Use of Kolmogorov-Smirnov, Cramer-von Mises and Related Statistics without Extensive Tables,” Journal of the Royal Statistical Society, ser. B, vol. 32, pp. 115–   
122.[6] Hollander, M., and Wolfe, D.A. 1999, Nonparametric Statistical Methods, 2nd ed. (New York: Wiley), p. 183.[7] Anderson, T.W., and Darling, D.A. 1952, “Asymptotic Theory of Certain Goodness of Fit Criteria Based on Stochastic Processes,” Annals of Mathematical Statistics, vol. 23, pp. 193–   
212.[8] Darling, D.A. 1957, “The Kolmogorov-Smirnov, Cramer-von Mises Tests,” Annals of Mathematical Statistics,vol. 28,pp.823-838.[9] Michael, J.R. 1983, “The Stabilized Probability Plot,” Biometrika, vol. 70, no. 1, pp. 11–17.[10] Noé, M. 1972, “The Calculation of Distributions of Two-Sided Kolmogorov-Smirnov Type Statistics,” Annals of Mathematical Statistics, vol. 43, pp. 58–64.[11] Kuiper, N.H. 1962, “Tests Concerning Random Points on a Circle,” Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen,ser. A.,vol.63,pp.38-47.[12] Stephens, M.A. 1965, “The Goodness-of-Fit Statistic $V _ { n }$ : Distribution and Significance Points,” Biometrika, vol. 52, pp.309-321.[13] Fisher, N.I., Lewis, T., and Embleton, B.J.J. 1987, Statistical Analysis of Spherical Data (New York: Cambridge University Press).[14]

# 14.4 Contingency Table Analysis of Two Distributions

In this section and the next three sections, we deal with measures of association for two distributions. The situation is this: Each data point has two or more different quantities associated with it, and we want to know whether knowledge of one quantity gives us any demonstrable advantage in predicting the value of another quantity. In many cases, one variable will be an “independent” or “control” variable, and another will be a “dependent” or “measured” variable. Then, we want to know if the latter variable is in fact dependent on or associated with the former variable. If it is, we want to have some quantitative measure of the strength of the association. One often hears this loosely stated as the question of whether two variables are correlated or uncorrelated, but we will reserve those terms for a particular kind of association (linear, or at least monotonic), as discussed in $\ S 1 4 . 5$ and $\ S 1 4 . 6$ .

Notice that, as in previous sections, the different concepts of significance and strength appear: The association between two distributions may be very significant even if that association is weak — if the quantity of data is large enough.

It is useful to distinguish among some different kinds of variables, with different categories forming a loose hierarchy.

- A variable is called nominal if its values are the members of some unordered set. For example, “state of residence” is a nominal variable that (in the U.S.) takes on one of 50 values; in astrophysics, “type of galaxy” is a nominal variable with the three values “spiral,” “elliptical,” and “irregular.”   
A variable is termed ordinal if its values are the members of a discrete, but ordered, set. Examples are grade in school, planetary order from the Sun (Mercury $= 1$ , Venus $= 2$ , : : :), and number of offspring. There need not be any concept of “equal metric distance” between the values of an ordinal variable, only that they be intrinsically ordered. We will call a variable continuous if its values are real numbers, as are times, distances, temperatures, etc. (Social scientists sometimes distinguish between interval and ratio continuous variables, but we do not find that distinction very compelling.)

A continuous variable can always be made into an ordinal one by binning it into ranges. If we choose to ignore the ordering of the bins, then we can turn it into a nominal variable. Nominal variables constitute the lowest type of the hierarchy, and therefore the most general. For example, a set of several continuous or ordinal variables can be turned, if crudely, into a single nominal variable, by coarsely binning each variable and then taking each distinct combination of bin assignments as a single nominal value. When multidimensional data are sparse, this is often the only sensible way to proceed.

The remainder of this section will deal with measures of association between nominal variables. For any pair of nominal variables, the data can be displayed as a contingency table, a table whose rows are labeled by the values of one nominal variable, whose columns are labeled by the values of the other nominal variable, and whose entries are nonnegative integers giving the number of observed events for each combination of row and column (see Figure 14.4.1). The analysis of association between nominal variables is thus called contingency table analysis or cross-

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.red</td><td rowspan=1 colspan=1>1.green</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0. male</td><td rowspan=1 colspan=1>#ofred malesNo0</td><td rowspan=1 colspan=1>#of green malesN01</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>#ofmalesNo·</td></tr><tr><td rowspan=1 colspan=1>1. female</td><td rowspan=1 colspan=1>#of red femalesN10</td><td rowspan=1 colspan=1>#of green femalesN11</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>#offemalesN1</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1># of redN.0</td><td rowspan=1 colspan=1># of greenN.1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>total #N</td></tr></table>

tabulation analysis.

The remainder of this section gives an approach, based on the chi-square statistic, that does a good job of characterizing the significance of association but is only so-so as a measure of the strength (principally because its numerical values have no very direct interpretations). We will return to contingency table analysis in $\ S 1 4 . 7$ with an approach, based on the information-theoretic concept of entropy, that will say little about the significance of association (use chi-square for that!) but is capable of very elegantly characterizing the strength of an association already known to be significant.

# 14.4.1 Measures of Association Based on Chi-Square

Some notation first: Let $N _ { i j }$ denote the number of events that occur with the first variable $x$ taking on its $i$ th value and the second variable $y$ taking on its $j$ th value. Let $N$ denote the total number of events, the sum of all the $N _ { i j }$ ’s. Let $N _ { i }$  denote the number of events for which the first variable $x$ takes on its $i$ th value regardless of the value of $y ; N _ { \cdot j }$ is the number of events with the $j$ th value of $y$ regardless of $x$ . So we have

$$
\begin{array} { l } { { N _ { i } . = \displaystyle \sum _ { j } N _ { i j } \qquad N . _ { j } = \sum _ { i } N _ { i j } } } \\ { { N = \displaystyle \sum _ { i } N _ { i } . = \sum _ { j } N . _ { j } } } \end{array}
$$

In other words, “dot” is a placeholder that means, “sum over the missing index”. $N _ { \cdot j }$ and $N _ { i }$  are sometimes called the row and column totals or marginals, but we will use these terms cautiously since we can never keep straight which are the rows and which are the columns!

The null hypothesis is that the two variables $x$ and $y$ have no association. In this case, the probability of a particular value of $x$ given a particular value of $y$ should be the same as the probability of that value of $x$ regardless of $y$ . Therefore, in the null hypothesis, the expected number for any $N _ { i j }$ , which we will denote $n _ { i j }$ , can be calculated from only the row and column totals,

$$
\frac { n _ { i j } } { N _ { \cdot j } } = \frac { N _ { i } } { N } \qquad \mathrm { w h i c h i m p l i e s } \qquad n _ { i j } = \frac { N _ { i } . N _ { \cdot j } } { N }
$$

Notice that if a column or row total is zero, then the expected number for all the entries in that column or row is also zero; in that case, the never-occurring bin of $x$ or $y$ should simply be removed from the analysis.

The chi-square statistic is now given by equation (14.3.1), which, in the present case, is summed over all entries in the table:

$$
\chi ^ { 2 } = \sum _ { i , j } \frac { ( N _ { i j } - n _ { i j } ) ^ { 2 } } { n _ { i j } }
$$

The number of degrees of freedom is equal to the number of entries in the table (product of its row size and column size) minus the number of constraints that have arisen from our use of the data themselves to determine the $n _ { i j }$ . Each row total and column total is a constraint, except that this overcounts by one, since the total of the column totals and the total of the row totals both equal $N$ , the total number of data points. Therefore, if the table is of size $I$ by $J$ , the number of degrees of freedom is $I J - I - J + 1$ . Equation (14.4.3), along with the chi-square probability function (-6.2), now give the significance of an association between the variables $x$ and $y$ . Incidentally, the two-sample chi-square test for equality of distributions, equation (14.3.3), is a special case of equation (14.4.3) with $J = 2$ and with the $y$ variable simply a label distinguishing the two samples.

Suppose there is a significant association. How do we quantify its strength, so that (e.g.) we can compare the strength of one association with another? The idea here is to find some reparametrization of $\chi ^ { 2 }$ that maps it into some convenient interval, like 0 to 1, where the result is not dependent on the quantity of data that we happen to sample, but rather depends only on the underlying population from which the data were drawn. There are several different ways of doing this. Two of the more common are called Cramer’s $V$ and the contingency coefficient $C$ .

The formula for Cramer’s $V$ is

$$
V = \sqrt { \frac { \chi ^ { 2 } } { N \operatorname* { m i n } \left( I - 1 , J - 1 \right) } }
$$

where $I$ and $J$ are again the numbers of rows and columns, and $N$ is the total number of events. Cramer’s $V$ has the pleasant property that it lies between zero and one inclusive, equals zero when there is no association, and equals one only when the association is perfect: All the events in any row lie in one unique column, and vice versa. (In chess parlance, no two rooks, placed on a nonzero table entry, can capture each other.)

In the case of $I = J = 2$ , Cramer’s $V$ is also referred to as the phi statistic.

The contingency coefficient $C$ is defined as

$$
C = \sqrt { \frac { \chi ^ { 2 } } { \chi ^ { 2 } + N } }
$$

It also lies between zero and one, but (as is apparent from the formula) it can never achieve the upper limit. While it can be used to compare the strength of association of two tables with the same $I$ and $J$ , its upper limit depends on $I$ and $J$ . Therefore it can never be used to compare tables of different sizes.

The trouble with both Cramer’s $V$ and the contingency coefficient $C$ is that, when they take on values in between their extremes, there is no very direct interpretation of what that value means. For example, you are in Las Vegas, and a friend tells you that there is a small, but significant, association between the color of a croupier’s eyes and the occurrence of red and black on his roulette wheel. Cramer’s $V$ is about 0.028, your friend tells you. You know what the usual odds against you are (because of the green zero and double zero on the wheel). Is this association sufficient for you to make money? Don’t ask us! For a measure of association that is directly applicable to gambling, look at $\ S 1 4 . 7$ .

void cntab(MatInt_I &nn, Doub &chisq, Doub &df, Doub &prob, Doub &cramrv, Doub &ccc)

Given a two-dimensional contingency table in the form of an array $\mathtt { n n } [ 0 . \mathtt { \_ n i - 1 } ] [ 0 \_ . \mathtt { \_ n j - 1 } ]$ of integers, this routine returns the chi-square chisq, the number of degrees of freedom df, the $p$ - value prob (small values indicating a significant association), and two measures of association, Cramer’s $V$ (cramrv) and the contingency coefficient $C$ (ccc).

const Doub TINY $\sp { \prime } = 1$ .0e-30; A small number.   
Gamma gam;   
Int i,j,nnj,nni,minij,ni $=$ nn.nrows(),nj=nn.ncols();   
Doub sum $_ { 1 = 0 }$ .0,expctd,temp;   
VecDoub sumi(ni),sumj(nj);   
nni=ni; Number of rows...   
nnj=nj; ...and columns.   
for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<ni; $\dot { \bf 1 } + +$ ) { Get the row totals. sumi[i]=0.0; for (j=0;j<nj;j $^ { + + }$ ) { sumi[i] $+ =$ nn[i][j]; sum $+ =$ nn[i][j]; if (sumi[i] == 0.0) --nni; Eliminate any zero rows by reducing the num-  
} ber.   
for (j=0;j<nj;j++) { Get the column totals. sumj[j]=0.0; for (i=0;i<ni;i++) sumj[j] $+ =$ nn[i][j]; if (sumj[j] $\mathrm { = = } \ 0 . 0$ ) --nnj; Eliminate any zero columns.   
}   
df=nni\*nnj-nni-nnj+1; Corrected number of degrees of freedom.   
chisq=0.0;   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<ni;i++) { Do the chi-square sum. for (j=0;j<nj;j++) { expctd=sumj[j]\*sumi[i]/sum; temp=nn[i][j]-expctd; chisq $+ =$ temp\*temp/(expctd+TINY); Here TINY guarantees that any } eliminated row or column will not contribute to the sum. } prob=gam.gammq(0. $^ { 5 \ast }$ df,0.5\*chisq);   
minij $=$ nni $<$ nnj ? nni-1 : nnj-1;   
cramrv $=$ sqrt(chisq/(sum\*minij));   
ccc=sqrt(chisq/(chisq+sum));

Chi-square probability function.

# CITED REFERENCES AND FURTHER READING:

Agresti, A. 2002, Categorical Data Analysis, 2nd ed. (New York: Wiley). Mickey, R.M., Dunn, O.J., and Clark, V.A. 2004, Applied Statistics: Analysis of Variance and Regression, 3rd ed.(New York:Wiley). Norusis, M.J. 2006, SPSS 14.0 Guide to Data Analysis (Englewood Cliffs, NJ: Prentice-Hall).

# 14.5 Linear Correlation

We next turn to measures of association between variables that are ordinal or continuous, rather than nominal. Most widely used is the linear correlation coefficient. For pairs of quantities $( x _ { i } , y _ { i } )$ ; $i = 0 , \ldots , N - 1$ , the linear correlation coefficient $r$ (also called the product-moment correlation coefficient, or Pearson’s $r$ ) is given by the formula

$$
r = { \frac { \sum _ { i } ( x _ { i } - { \overline { { x } } } ) ( y _ { i } - { \overline { { y } } } ) } { \sqrt { \sum _ { i } ( x _ { i } - { \overline { { x } } } ) ^ { 2 } } { \sqrt { \sum _ { i } ( y _ { i } - { \overline { { y } } } ) ^ { 2 } } } } }
$$

where, as usual, $\overbar { x }$ is the mean of the $x _ { i }$ ’s and $\overline { { y } }$ is the mean of the $y _ { i }$ ’s.

The value of $r$ lies between $^ { - 1 }$ and 1, inclusive. It takes on a value of 1, termed “complete positive correlation,” when the data points lie on a perfect straight line with positive slope, with $x$ and $y$ increasing together. The value 1 holds independent of the magnitude of the slope. If the data points lie on a perfect straight line with negative slope, $y$ decreasing as $x$ increases, then $r$ has the value $^ { - 1 }$ ; this is called “complete negative correlation.” A value of $r$ near zero indicates that the variables $x$ and $y$ are uncorrelated.

When a correlation is known to be significant, $r$ is one conventional way of summarizing its strength. In fact, the value of $r$ can be translated into a statement about what residuals (root-mean-square deviations) are to be expected if the data are fitted to a straight line by the least-squares method (see $\ S 1 5 . 2$ , especially equation 15.2.13). Unfortunately, $r$ is a rather poor statistic for deciding whether an observed correlation is statistically significant and/or whether one observed correlation is significantly stronger than another. The reason is that $r$ is ignorant of the individual distributions of $x$ and $y$ , so there is no universal way to compute its distribution in the case of the null hypothesis.

About the only general statement that can be made is this: If the null hypothesis is that $x$ and $y$ are uncorrelated, and if the distributions for $x$ and $y$ each have enough convergent moments (“tails” die off sufficiently rapidly), and if $N$ is large (typically $> ~ 5 0 0 )$ , then $r$ is distributed approximately normally, with a mean of zero and a standard deviation of $1 / \sqrt { N }$ . In that case, the (double-sided) significance of the correlation, that is, the probability that $| r |$ should be larger than its observed value in the null hypothesis, is

$$
\mathrm { e r f c } \left( \frac { \lvert r \rvert \sqrt { N } } { \sqrt { 2 } } \right)
$$

where $\operatorname { e r f c } ( x )$ is the complementary error function, equation (6.2.10), computed by the routines Erf.erfc or erfcc of $\ S 6 . 2$ . A small value of (14.5.2) indicates that the two distributions are significantly correlated. (See expression 14.5.9 below for a more accurate test.)

Most statistics books try to go beyond (14.5.2) and give additional statistical tests that can be made using $r$ . In almost all cases, however, these tests are valid only for a very special class of hypotheses, namely that the distributions of $x$ and $y$ jointly form a binormal or two-dimensional Gaussian distribution around their mean values, with joint probability density

$$
\begin{array} { r } { p ( x , y ) d x d y = \mathrm { { c o n s t . } } \times \exp \left[ - \frac { 1 } { 2 } ( a _ { 0 0 } x ^ { 2 } - 2 a _ { 0 1 } x y + a _ { 1 1 } y ^ { 2 } ) \right] d x d y } \end{array}
$$

where $a _ { 0 0 } , a _ { 0 1 }$ ; and $a _ { 1 1 }$ are arbitrary constants. For this distribution $r$ has the value

$$
r = - \frac { a _ { 0 1 } } { \sqrt { a _ { 0 0 } a _ { 1 1 } } }
$$

There are occasions when (14.5.3) may be known to be a good model of the data. There may be other occasions when we are willing to take (14.5.3) as at least a rough-and-ready guess, since many two-dimensional distributions do resemble a binormal distribution, (that is, a two-dimensional Gaussian) at least not too far out on their tails. In either situation, we can use (14.5.3) to go beyond (14.5.2) in any of several directions:

First, we can allow for the possibility that the number $N$ of data points is not large. Here, it turns out that the statistic

$$
t = r { \sqrt { \frac { N - 2 } { 1 - r ^ { 2 } } } }
$$

is distributed in the null case (of no correlation) like Student’s $t$ -distribution with $\nu ~ = ~ N - 2$ degrees of freedom, whose two-sided significance level is given by $1 - A ( t | \nu )$ (equation 6.14.11) [1]. As $N$ becomes large, this significance and (14.5.2) become asymptotically the same, so that one never does worse by using (14.5.5), even if the binormal assumption is not well substantiated.

Second, when $N$ is only moderately large $( \geq 1 0 )$ ), we can compare whether the difference of two significantly nonzero $r$ ’s, e.g., from different experiments, is itself significant. In other words, we can quantify whether a change in some control variable significantly alters an existing correlation between two other variables. This is done by using Fisher’s z-transformation to associate each measured $r$ with a corresponding $Z$ :

$$
z = { \frac { 1 } { 2 } } \ln \left( { \frac { 1 + r } { 1 - r } } \right)
$$


<!-- chunk 0012: pages 771-840 -->
Then, each $Z$ is approximately normally distributed with a mean value

$$
\overline { { z } } = \frac { 1 } { 2 } \left[ \ln \left( \frac { 1 + r _ { \mathrm { t r u e } } } { 1 - r _ { \mathrm { t r u e } } } \right) + \frac { r _ { \mathrm { t r u e } } } { N - 1 } \right]
$$

where $r _ { \mathrm { t r u e } }$ is the actual or population value of the correlation coefficient, and with a standard deviation

$$
\sigma ( z ) \approx { \frac { 1 } { \sqrt { N - 3 } } }
$$

Equations (14.5.7) and (14.5.8), when they are valid, give several useful statistical tests [1]. For example, the significance level at which a measured value of $r$ differs from some hypothesized value $r _ { \mathrm { t r u e } }$ is given by

$$
\mathrm { e r f c } \left( \frac { \left. z - \overline { { z } } \right. \sqrt { N - 3 } } { \sqrt { 2 } } \right)
$$

where $Z$ and $\overline { z }$ are given by (14.5.6) and (14.5.7), with small values of (14.5.9) indicating a significant difference. (Setting $\overline { { z } } ~ = ~ 0$ makes expression 14.5.9 a more accurate replacement for expression 14.5.2 above.) Similarly, the significance of a difference between two measured correlation coefficients $r _ { 1 }$ and $r _ { 2 }$ is

$$
\mathrm { e r f c } \left( \frac { | z _ { 1 } - z _ { 2 } | } { \sqrt { 2 } \sqrt { \frac { 1 } { N _ { 1 } - 3 } + \frac { 1 } { N _ { 2 } - 3 } } } \right)
$$

where $z _ { 1 }$ and $z _ { 2 }$ are obtained from $r _ { 1 }$ and $r _ { 2 }$ using (14.5.6), and where $N _ { 1 }$ and $N _ { 2 }$ are, respectively, the number of data points in the measurement of $r _ { 1 }$ and $r _ { 2 }$ .

All of the significances above are two-sided. If you wish to disprove the null hypothesis in favor of a one-sided hypothesis, such as that $r _ { 1 } > r _ { 2 }$ (where the sense of the inequality was decided a priori), then (i) if your measured $r _ { 1 }$ and $r _ { 2 }$ have the wrong sense, you have failed to demonstrate your one-sided hypothesis, but (ii) if they have the right ordering, you can multiply the significances given above by 0.5, which makes them more significant.

But keep in mind: These interpretations of the $r$ statistic can be completely meaningless if the joint probability distribution of your variables $x$ and $y$ is too different from a binormal distribution.

void pearsn(VecDoub_I &x, VecDoub_I &y, Doub &r, Doub &prob, Doub &z)

Given two arrays $\mathbf { x } \left[ 0 \ldots \ldots \right] $ and $\mathtt { y } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ , this routine computes their correlation coefficient $r$ (returned as $\mathbf { r }$ ), the $p$ -value at which the null hypothesis of zero correlation is disproved (prob whose small value indicates a significant correlation), and Fisher’s $z$ (returned as $_ { z }$ ), whose value can be used in further statistical tests as described above.   
{

Will regularize the unusual case of complete correlation.

const Doub TINY $^ { \prime = 1 }$ .0e-20;   
Beta beta;   
Int j, $\mathrm { n } { = } \mathrm { x }$ .size();   
Doub yt,xt,t,df;   
Doub syy=0.0,sxy=0.0,sxx=0.0,ay=0.0,ax=0.0;   
for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<n;j++) { ax += x[j]; ay $+ =$ y[j];   
}

Find the means.

ax /= n;   
ay /= n;   
for (j=0;j<n;j++) { Compute the correlation coefficient. xt=x[j]-ax; yt=y[j]-ay; sxx $+ =$ xt\*xt; syy $+ =$ yt\*yt; sxy $+ =$ xt\*yt;   
7   
$\mathbf { r } { } =$ sxy/(sqrt(sxx\*syy)+TINY);   
$z { = } 0$ .5\*log((1.0+r+TINY)/(1.0-r+TINY)); Fisher’s z transformation.   
$\mathtt { d f } = \mathtt { n } - 2$ ;   
t=r\*sqrt(df/((1.0-r+TINY) $^ *$ (1.0+r+TINY))); Equation (14.5.5).   
prob beta.betai(0. $^ { 5 \ast }$ df,0.5,df/(df+t\*t)); Student’s t probability.   
// prob $=$ erfcc(abs( $^ { 2 * }$ sqrt(n-1.0))/1.4142136);   
For large n, this easier computation of prob, using the short routine erfcc, would give   
approximately the same value.

# CITED REFERENCES AND FURTHER READING:

Taylor, J.R. 1997, An Introduction to Error Analysis, 2nd ed. (Sausalito, CA: University Science Books), Chapter 9.   
Mickey, R.M., Dunn, O.J., and Clark, V.A. 2004, Applied Statistics: Analysis of Variance and Regression,3rd ed. (New York:Wiley).   
Devore, J.L. 2003, Probability and Statistics for Engineering and the Sciences, 6th ed. (Belmont, CA: Duxbury Press), Chapter 12.   
Hoel, P.G. 1971, Introduction to Mathematical Statistics, 4th ed. (New York: Wiley), Chapter 7.   
Korn, G.A., and Korn, T.M. 1968, Mathematical Handbook for Scientists and Engineers, 2nd rev. ed., reprinted 2000 (New York: Dover), $\ S 1 9 . 7$ .   
Norusis, M.J. 2006, SPSS 14.0 Guide to Data Analysis (Englewood Cliffs, NJ: Prentice-Hall).   
Stuart, A., and Ord, J.K. 1994, Kendall’s Advanced Theory of Statistics, 6th ed. (London: Edward Arnold) [previous eds. published as Kendall, M., and Stuart, A., The Advanced Theory of Statistics], $\ S 1 6 . 2 8$ and $\ S 1 6 . 3 3$ .[1]

# 14.6 Nonparametric or Rank Correlation

It is precisely the uncertainty in interpreting the significance of the linear correlation coefficient $r$ that leads us to the important concepts of nonparametric or rank correlation. As before, we are given $N$ pairs of measurements $( x _ { i } , y _ { i } )$ . Before, difficulties arose because we did not necessarily know the probability distribution function from which the $x _ { i }$ ’s or $y _ { i }$ ’s were drawn.

The key concept of nonparametric correlation is this: If we replace the value of each $x _ { i }$ by the value of its rank among all the other $x _ { i }$ ’s in the sample, that is, $1 , 2 , 3 , \ldots , N$ , then the resulting list of numbers will be drawn from a perfectly known distribution function, namely uniformly from the integers between 1 and $N$ , inclusive. Better than uniformly, in fact, since if the $x _ { i }$ ’s are all distinct, then each integer will occur precisely once. If some of the $x _ { i }$ ’s have identical values, it is conventional to assign to all these “ties” the mean of the ranks that they would have had if their values had been slightly different. This midrank will sometimes be an integer, sometimes a half-integer. In all cases the sum of all assigned ranks will be the same as the sum of the integers from 1 to $N$ , namely $\textstyle { \frac { 1 } { 2 } } N ( N + 1 )$ .

Of course we do exactly the same procedure for the $y _ { i }$ ’s, replacing each value by its rank among the other $y _ { i }$ ’s in the sample.

Now we are free to invent statistics for detecting correlation between uniform sets of integers between 1 and $N$ , keeping in mind the possibility of ties in the ranks. There is, of course, some loss of information in replacing the original numbers by ranks. We could construct some rather artificial examples where a correlation could be detected parametrically (e.g., in the linear correlation coefficient $r$ ) but could not be detected nonparametrically. Such examples are very rare in real life, however, and the slight loss of information in ranking is a small price to pay for a very major advantage: When a correlation is demonstrated to be present nonparametrically, then it is really there! (That is, to a certainty level that depends on the significance chosen.) Nonparametric correlation is more robust than linear correlation, more resistant to unplanned defects in the data, in the same sort of sense that the median is more robust than the mean. For more on the concept of robustness, see $\ S 1 5 . 7$ .

As always in statistics, some particular choices of a statistic have already been invented for us and consecrated, if not beatified, by popular use. We will discuss two, the Spearman rank-order correlation coefficient $\left( r _ { s } \right)$ , and Kendall’s tau $( \tau )$ .

# 14.6.1 Spearman Rank-Order Correlation Coefficient

Let $R _ { i }$ be the rank of $x _ { i }$ among the other $x$ ’s and $S _ { i }$ be the rank of $y _ { i }$ among the other $y$ ’s, with ties being assigned the appropriate midrank as described above. Then the rank-order correlation coefficient is defined to be the linear correlation coefficient of the ranks, namely,

$$
r _ { s } = \frac { \sum _ { i } ( R _ { i } - \overline { { R } } ) ( S _ { i } - \overline { { S } } ) } { \sqrt { \sum _ { i } ( R _ { i } - \overline { { R } } ) ^ { 2 } } \sqrt { \sum _ { i } ( S _ { i } - \overline { { S } } ) ^ { 2 } } }
$$

The significance of a nonzero value of $r _ { s }$ is tested by computing

$$
t = r _ { s } \sqrt { \frac { N - 2 } { 1 - r _ { s } ^ { 2 } } }
$$

which is distributed approximately as Student’s distribution with $N - 2$ degrees of freedom. A key point is that this approximation does not depend on the original distribution of the $x$ ’s and $y$ ’s; it is always the same approximation, and always pretty good.

It turns out that $r _ { s }$ is closely related to another conventional measure of nonparametric correlation, the so-called sum squared difference of ranks, defined as

$$
D = \sum _ { i = 0 } ^ { N - 1 } ( R _ { i } - S _ { i } ) ^ { 2 }
$$

(This $D$ is sometimes denoted $D ^ { * * }$ , where the asterisks are used to indicate that ties are treated by midranking.)

When there are no ties in the data, the exact relation between $D$ and $r _ { s }$ is

$$
r _ { s } = 1 - \frac { 6 D } { N ^ { 3 } - N }
$$

When there are ties, the exact relation is slightly more complicated: Let $f _ { k }$ be the number of ties in the $k$ th group of ties among the $R _ { i }$ ’s, and let $g _ { m }$ be the number of ties in the mth group of ties among the $S _ { i }$ ’s. Then it turns out that

$$
r _ { s } = \frac { 1 - \displaystyle \frac { 6 } { N ^ { 3 } - N } \left[ D + \frac { 1 } { 1 2 } \sum _ { k } ( f _ { k } ^ { 3 } - f _ { k } ) + \frac { 1 } { 1 2 } \sum _ { m } ( g _ { m } ^ { 3 } - g _ { m } ) \right] } { \displaystyle \left[ 1 - \frac { \sum _ { k } ( f _ { k } ^ { 3 } - f _ { k } ) } { N ^ { 3 } - N } \right] ^ { 1 / 2 } \left[ 1 - \frac { \sum _ { m } ( g _ { m } ^ { 3 } - g _ { m } ) } { N ^ { 3 } - N } \right] ^ { 1 / 2 } }
$$

holds exactly. Notice that if all the $f _ { k }$ ’s and all the $g _ { m }$ ’s are equal to one, meaning that there are no ties, then equation (14.6.5) reduces to equation (14.6.4).

In (14.6.2) we gave a $t$ -statistic that tests the significance of a nonzero $r _ { s }$ . It is also possible to test the significance of $D$ directly. The expectation value of $D$ in the null hypothesis of uncorrelated data sets is

$$
\bar { D } = \frac { 1 } { 6 } ( N ^ { 3 } - N ) - \frac { 1 } { 1 2 } \sum _ { k } ( f _ { k } ^ { 3 } - f _ { k } ) - \frac { 1 } { 1 2 } \sum _ { m } ( g _ { m } ^ { 3 } - g _ { m } )
$$

its variance is

$$
\mathrm { V a r } ( D ) = { \frac { ( N - 1 ) N ^ { 2 } ( N + 1 ) ^ { 2 } } { 3 6 } } \left[ 1 - { \frac { \sum _ { k } ( f _ { k } ^ { 3 } - f _ { k } ) } { N ^ { 3 } - N } } \right] \left[ 1 - { \frac { \sum _ { m } ( g _ { m } ^ { 3 } - g _ { m } ) } { N ^ { 3 } - N } } \right]
$$

and it is approximately normally distributed, so that the significance level is a complementary error function (cf. equation 14.5.2). Of course, (14.6.2) and (14.6.7) are not independent tests, but simply variants of the same test. In the program that follows, we calculate both the significance level obtained by using (14.6.2) and the significance level obtained by using (14.6.7); their discrepancy will give you an idea of how good the approximations are. You will also notice that we break off the task of assigning ranks (including tied midranks) into a separate function, crank.

void spear(VecDoub_I &data1, VecDoub_I &data2, Doub &d, Doub &zd, Doub &probd, Doub &rs, Doub &probrs)

Given two data arrays, data1[0..n-1] and data2[0..n-1], this routine returns their sum squared difference of ranks as $D$ , the number of standard deviations by which $D$ deviates from its null-hypothesis expected value as zd, the two-sided $p$ -value of this deviation as probd, Spearman’s rank correlation $r _ { s }$ as rs, and the two-sided $p$ -value of its deviation from zero as probrs. The external routines crank (below) and sort2 $( \ S 8 . 2 )$ are used. A small value of either probd or probrs indicates a significant correlation (rs positive) or anticorrelation (rs negative). {

Beta bet;   
Int j,n=data1.size();   
Doub vard,t,sg,sf,fac,en3n,en,df,aved;   
VecDoub wksp1(n),wksp2(n);   
for $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<n;j++) {   
wksp1[j]=data1[j];   
wksp2[j] $=$ data2[j];   
}   
sort2(wksp1,wksp2); Sort each of the data arrays, and convert the encrank(wksp1,sf); tries to ranks. The values sf and sg return sort2(wksp2,wksp1); the sums $\sum ( f _ { k } ^ { 3 } - f _ { k } )$ and $\sum ( g _ { m } ^ { 3 } - g _ { m } )$ , crank(wksp2,sg); respectively.   
d=0.0;   
for (j=0;j<n;j++) Sum the squared difference of ranks. d $+ =$ SQR(wksp1[j]-wksp2[j]);   
$\mathtt { e n } \mathtt { = n }$ ;   
en3n=en\*en\*en-en;   
aved=en3n/6.0-(sf+sg)/12.0;   
fac (1.0-sf/en3n) $^ *$ (1.0-sg/en3n);   
vard $\equiv$ ((en-1.0)\*en\*en\*SQR(en+1.0)/36.0)\*fac;   
zd $=$ (d-aved)/sqrt(vard);   
probd=erfcc(abs(zd)/1.4142136);   
rs=(1.0-(6.0/en3n)\*( $\mathrm { d } +$ (sf+sg)/12.0))/sqrt(fac);   
fac=(rs+1.0)\*(1.0-rs);   
if (fac $> ~ 0 . 0$ ) { t=rs\*sqrt((en-2.0)/fac); df=en-2.0; probrs=bet.betai(0. $^ { 5 \ast }$ df,0.5,df/(df+t\*t));   
} else probrs=0.0; Expectation value of $D$ ,   
and variance of $D$ give   
number of standard deviations and $p$ -value.   
Rank correlation coefficient, and its $t$ -value,   
give its $p$ -value.

# }

# void crank(VecDoub_IO &w, Doub &s)

Given a sorted array $\mathtt { w } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ , replaces the elements by their rank, including midranking of ties, and returns as s the sum of $f ^ { \dot { 3 } } - f$ , where $f$ is the number of elements in each tie.

Int $\scriptstyle { \dot { \mathsf { J } } } = 1$ ,ji,jt, $\mathrm { n } { = } \mathrm { w }$ .size();   
Doub t,rank;   
$\mathtt { s } = 0 . 0$ ;   
while (j < n) { if (w[j] != w[j-1]) { Not a tie. w[j-1]=j; ++j; } else { A tie: for (jt=j+1;jt $< = \mathtt { n }$ && $\mathrm { { w } [ j t { - } 1 ] = = \mathrm { { w } [ j { - } 1 ] \ ; \ j t { + } + ) } }$ ; How far does it go? rank=0.5\*(j+jt-1); This is the mean rank of the tie, for (ji=j;ji $< =$ (jt-1);ji $^ { + + }$ ) so enter it into all the tied entries, w[ji-1]=rank; t=jt-j; s += (t\*t\*t-t); and update s. j=jt; }   
}   
if (j == n) w[n-1] $= _ { \mathrm { n } }$ ; If the last element was not tied, this is rank.

# 14.6.2 Kendall's Tau

Kendall’s $\tau$ is even more nonparametric than Spearman’s $r _ { s }$ or $D$ . Instead of using the numerical difference of ranks, it uses only the relative ordering of ranks: higher in rank, lower in rank, or the same in rank. But in that case we don’t even have to rank the data! Ranks will be higher, lower, or the same if and only if the values are larger, smaller, or equal, respectively. On balance, we prefer $r _ { s }$ as being the more straightforward nonparametric test, but both statistics are in general use. In fact, $\tau$ and $r _ { s }$ are very strongly correlated and, in most applications, are effectively the same test.

To define $\tau$ , we start with the $N$ data points $( x _ { i } , y _ { i } )$ . Now consider all $\scriptstyle { \frac { 1 } { 2 } } N ( N -$ 1/ pairs of data points, where a data point cannot be paired with itself, and where the points in either order count as one pair. We call a pair concordant if the relative ordering of the ranks of the two $x$ ’s (or for that matter the two $x$ ’s themselves) is the same as the relative ordering of the ranks of the two $y$ ’s (or for that matter the two $y$ ’s themselves). We call a pair discordant if the relative ordering of the ranks of the two $x$ ’s is opposite from the relative ordering of the ranks of the two $y$ ’s. If there is a tie in either the ranks of the two $x$ ’s or the ranks of the two $y$ ’s, then we don’t call the pair either concordant or discordant. If the tie is in the $x$ ’s, we will call the pair an “extra $y$ pair.” If the tie is in the $y$ ’s, we will call the pair an “extra $x$ pair.” If the tie is in both the $x$ ’s and the $y$ ’s, we don’t call the pair anything at all. Are you still with us?

Kendall’s $\tau$ is now the following simple combination of these various counts:

You can easily convince yourself that this must lie between 1 and $^ { - 1 }$ , and that it takes on the extreme values only for complete rank agreement or complete rank reversal, respectively.

More important, Kendall has worked out, from the combinatorics, the approximate distribution of $\tau$ in the null hypothesis of no association between $x$ and $y$ . In this case, $\tau$ is approximately normally distributed, with zero expectation value and a variance of

$$
\mathrm { V a r } ( \tau ) = { \frac { 4 N + 1 0 } { 9 N ( N - 1 ) } }
$$

The following program proceeds according to the above description, and therefore loops over all pairs of data points. Beware: This is an $O ( N ^ { 2 } )$ algorithm, unlike the algorithm for $r _ { s }$ , whose dominant sort operations are of order $N \log N$ . If you are routinely computing Kendall’s $\tau$ for data sets of more than a few thousand points, you may be in for some serious computing. If, however, you are willing to bin your data into a moderate number of bins, then read on.

void kendl1(VecDoub_I &data1, VecDoub_I &data2, Doub &tau, Doub &z, Doub &prob) Given data arrays data1[0..n-1] and data2[0..n-1], this program returns Kendall’s $\tau$ as tau, its number of standard deviations from zero as z, and its two-sided $p$ -value as prob. Small values of prob indicate a significant correlation (tau positive) or anticorrelation (tau negative). {

Loop over first member of pair, and second member.

Int is $ \scriptstyle = 0$ ,j,k,n2=0,n1=0,n=data1.size();   
Doub svar,aa,a2,a1;   
for $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<n-1;j++) { for (k=j+1;k<n;k++) { a1=data1[j]-data1[k]; a2=data2[j]-data2[k]; aa=a1\*a2; if (aa $! = ~ 0 . 0 )$ { ++n1; $+ + \mathtt { n 2 }$ ; aa > 0.0 ? ++is : --is; } else { if (a1 $\ ! = \ 0 . 0 \dot { } .$ ) $+ + \mathtt { n 1 }$ ; if (a2 $\ ! = \ 0 . 0$ ) $+ + \mathtt { n } 2$ ; } }

Neither array has a tie.

One or both arrays have ties.   
An “extra $x "$ event.   
An “extra y” event. tau=is/(sqrt(Doub(n1))\*sqrt(Doub(n2)));   
svar $^ { * = }$ (4.0\*n+10.0)/(9.0\*n\*(n-1.0));   
$z =$ tau/sqrt(svar);   
prob $=$ erfcc(abs(z)/1.4142136); Equation (14.6.8).   
Equation (14.6.9).

$p$ -value.

Sometimes it happens that there are only a few possible values each for $x$ and $y$ . In that case, the data can be recorded as a contingency table (see $\ S 1 4 . 4 )$ that gives the number of data points for each contingency of $x$ and $y$ .

Spearman’s rank-order correlation coefficient is not a very natural statistic under these circumstances, since it assigns to each $x$ and $y$ bin a not-very-meaningful midrank value and then totals up vast numbers of identical rank differences. Kendall’s tau, on the other hand, with its simple counting, remains quite natural. Furthermore, its $O ( N ^ { 2 } )$ algorithm is no longer a problem, since we can arrange for it to loop over pairs of contingency table entries (each containing many data points) instead of over pairs of data points. This is implemented in the program that follows.

Note that Kendall’s tau can be applied only to contingency tables where both variables are ordinal, i.e., well-ordered, and that it looks specifically for monotonic correlations, not for arbitrary associations. These two properties make it less general than the methods of $\ S 1 4 . 4$ , which applied to nominal, i.e., unordered, variables and arbitrary associations.

Comparing kendl1 above with kendl2 below, you will see that we have changed a number of variables from int to double. This is because the number of events in a contingency table might be sufficiently large as to cause overflows in some of the integer arithmetic, while the number of individual data points in a list could not possibly be that large (for an $O ( N ^ { 2 } )$ routine!).

# void kendl2(MatDoub_I &tab, Doub &tau, Doub &z, Doub &prob)

Given a two-dimensional table tab[0..i-1][0..j-1], such that tab[k][l] contains the number of events falling in bin k of one variable and bin l of another, this program returns Kendall’s $\tau$ as tau, its number of standard deviations from zero as $_ { z }$ , and its two-sided $p$ -value as prob. Small values of prob indicate a significant correlation (tau positive) or anticorrelation (tau negative) between the two variables. Although tab is a double array, it will normally contain integral values.

Int k,l,nn,mm,m2,m1,lj,li,kj,ki, $\dot { \bf 1 } =$ tab.nrows(),j=tab.ncols();   
Doub svar, $\mathtt { s } = 0$ .0,points,pairs,en $\scriptstyle 2 = 0$ .0,en1=0.0;   
$\mathrm { \ n n = i } * \mathrm { j }$ ; Total number of entries in contingency table.   
points=tab[i-1][j-1];   
for ( $\scriptstyle 1 = 0$ ;k $< =$ nn-2;k++) { Loop over entries in table, ki=(k/j); decoding a row, kj=k-j\*ki; and a column. points $+ =$ tab[ki][kj]; Increment the total count of events. for (l=k+1;l<=nn-1;l++) Loop over other member of the pair, $\mathbf { 1 } \dot { \mathbf { 1 } } = \mathbf { 1 }$ /j; decoding its row lj ${ } = 1$ -j\*li; and column. $\mathrm { m m } { = } \left( \mathrm { m 1 { = } 1 i { - } k i } \right) { * } \left( \mathrm { m 2 { = } 1 j { - } k j } \right) $ ; pairs $=$ tab[ki][kj]\*tab[li][lj]; if (mm $\iota = \ 0$ ) { Not a tie. en1 $+ =$ pairs; en2 $+ =$ pairs; s $+ =$ (mm > 0 ? pairs : -pairs); Concordant, or discordant. } else { if (m1 $! = ~ 0 ^ { \cdot }$ ) en1 $+ =$ pairs; if (m2 $\smash { \ ! = \ 0 }$ ) en2 $+ =$ pairs; } } tau=s/sqrt(en1\*en2);   
svar $^ { * = }$ (4.0\*points+10.0)/(9.0\*points\*(points-1.0));   
$_ { z = }$ tau/sqrt(svar);   
prob=erfcc(abs(z)/1.4142136);

# CITED REFERENCES AND FURTHER READING:

Lupton, R. 1993, Statistics in Theory and Practice (Princeton, NJ: Princeton University Press), Chapter 13.   
Lehmann, E.L. 1975, Nonparametrics: Statistical Methods Based on Ranks (San Francisco: Holden-Day); reprinted 2006 (New York: Springer).   
Hollander, M., and Wolfe, D.A. 1999, Nonparametric Statistical Methods, 2nd ed. (New York: Wiley).   
Downie, N.M., and Heath, R.W. 1965, Basic Statistical Methods, 2nd ed. (New York: Harper & Row), pp. 206–209.   
Norusis, M.J. 2006, SPSS 14.0 Guide to Data Analysis (Englewood Cliffs, NJ: Prentice-Hall).

# 14.7 Information-Theoretic Properties of Distributions

In this section we return to nominal distributions, that is to say, to distributions with discrete outcomes that have no meaningful ordering. Information theory [1-3] provides a different, and sometimes very useful, perspective on the nature of such a distribution p with outcomes $i$ , $0 \leq i \leq I - 1$ , and associated probabilities $p _ { i }$ , and on the relation between two or more such distributions. We develop that perspective in this section, starting with a review of some key concepts.

# 14.7.1 Entropy of a Distribution

Suppose that we make $M$ sequential, independent draws from a distribution $\mathbf { p }$ , thus generating a message that describes the outcomes, an $M$ -vector of integers $i _ { j }$ , each in the range $0 \leq i _ { j } \leq I - 1$ , with $j = 0 , \ldots , M - 1$ . We want to send the message to a waiting confederate, but we first want to compress it (that is, encode it) into the most parsimonious format, say into the smallest possible number of bits, $B$ . We can calculate a lower bound on $B$ by equating $2 ^ { B }$ , the number of possible different compressed messages, to a statistical estimate of the number of likely input messages. That equation, in the limit of $M$ becoming very large, is

$$
2 ^ { B } \approx { \frac { M ! } { \prod _ { i } ( M p _ { i } ) ! } }
$$

The rationale for the right-hand side is that our message will contain very nearly $M p _ { i }$ occurrences of the integer $i$ for each $i$ , so the count of messages will be very nearly the number of ways that we can arrange $M$ objects of $I$ types, with $M p _ { i }$ of them identical for each type $i$ . Taking the logarithm of equation (14.7.1), using Stirling’s approximation on the factorials, and keeping only terms that scale as fast as $M$ , we readily obtain

$$
B \approx - M \sum _ { i = 0 } ^ { I - 1 } p _ { i } \log _ { 2 } p _ { i } \equiv M H _ { 2 } ( \mathbf { p } )
$$

where $H _ { 2 } ( \mathbf { p } )$ is called the entropy (in bits) of the distribution $\mathbf { p }$ , a terminology borrowed from statistical physics. The subscript 2 is to remind us that the logarithm has

base 2. We can also define an entropy with base $e$

$$
H ( \mathbf { p } ) \equiv - \sum _ { i = 0 } ^ { I - 1 } p _ { i } \ln p _ { i } = - ( \ln 2 ) \sum _ { i = 0 } ^ { I - 1 } p _ { i } \log _ { 2 } p _ { i } = ( \ln 2 ) H _ { 2 } ( \mathbf { p } )
$$

If $H _ { 2 } ( \mathbf { p } )$ is measured in bits, then $H ( \mathbf { p } )$ will be measured in nats, with $1 \ \mathrm { n a t } =$ 1:4427 bits. In evaluating (14.7.3), note that

$$
\operatorname* { l i m } _ { p \to 0 } p \ln p = 0
$$

The value $H ( \mathbf { p } )$ lies between 0 and $\ln { I }$ . It is zero only when one of the $p _ { i }$ ’s is one, all the others zero.

Although we derived $B$ as a lower bound, a central result of information theory is that, in the limit of large $M$ , one can find codes that actually achieve that bound. (Arithmetic coding, described in $\ S 2 2 . 6$ , is an example of such a code.) Heuristically, one can interpret equation (14.7.2) as saying that it takes, on average, $- \log _ { 2 } { p _ { i } }$ bits (a positive number, since $p _ { i } ~ < ~ 1 \AA$ ) to encode an outcome $i$ . Thus, the compressed message size is $M$ times the expectation of $- \log _ { 2 } { p _ { i } }$ over outcomes occurring with probability $p _ { i }$ .

Yet a different view of entropy arises if we consider the game of “twenty questions,” where by repeated yes/no questions you try to eliminate all except one correct possibility for an unknown object. Better yet, let us consider a generalization of the game, where you are allowed to ask multiple choice questions as well as binary (yes/no) ones. The categories in your multiple choice questions are supposed to be mutually exclusive and exhaustive (as are “yes” and “no”).

The value to you of an answer increases with the number of possibilities that it eliminates. More specifically, an answer that eliminates all except a fraction $p$ of the remaining possibilities can be assigned a value $- \ln p$ . The purpose of the logarithm is to make the value additive, since, e.g., one question that eliminates all but 1/6 of the possibilities is considered as good as two questions that, in sequence, reduce the number by factors 1/2 and 1/3.

So that is the value of an answer; but what is the value of a question? If there are $I$ possible answers to the question and the fraction of possibilities consistent with answer $i$ is $p _ { i }$ , then the value of the question is the expectation value of the value of the answer, which is just $- \sum _ { i } p _ { i } \ln p _ { i }$ or $H ( \mathbf { p } )$ , as above.

As already mentioned, the entropy is zero only if one of the $p _ { i }$ ’s is unity, with all the others zero. In this case, the question is valueless, since its answer is preordained. $H ( \mathbf { p } )$ takes on its maximum value when all the $p _ { i }$ ’s are equal, in which case the question is sure to eliminate all but a fraction $1 / I$ of the remaining possibilities.

A third, still different, view of entropy comes from thinking about bets (or, more politely, “investments”). A fair bet on an outcome $i$ of probability $p _ { i }$ is one that has a payoff $o _ { i } = 1 / p _ { i }$ . This is the unique payoff (per unit wagered) for which, in the long run, the bettor will neither win nor lose, since in expectation value

$$
\langle o _ { i } \rangle = p _ { i } o _ { i } = 1
$$

Suppose you have the opportunity to bet repeatedly on a game offering fair bets on each outcome. This is not very interesting as a money-making proposition. But suppose that you are clairvoyant and can know in advance the outcome of each play (although you cannot affect that outcome). Now you’re in business! You always put your money on the winning choice of $i$ . How much money can you make?

Since your profit on each (sure thing!) wager scales multiplicatively with your accumulated wealth, the appropriate figure of merit is the the average doubling rate, or, equivalently, $e$ -folding rate, at which you can increase your capital. Since you always win, but can’t control the outcome, this is given by

$$
W \equiv \langle \ln o _ { i } \rangle = \langle - \ln p _ { i } \rangle = - \sum _ { i } p _ { i } \ln p _ { i } = H ( \mathbf { p } )
$$

In other words, the entropy of a distribution is the e-folding rate of capital for a fair game about which you have perfect predictive information. While this may seem fanciful, we will see in $\ S 1 4 . 7 . 3$ how it generalizes to the more realistic case where you have only imperfect, perhaps very small, predictive information.

# 14.7.2 Kullback-Leibler Distance

Back in the context of message compression, suppose that events occur with a distribution $\mathbf { p }$ , that is, $p _ { i } , 0 \leq i \leq I - 1$ , but we try to compress the message of their outcomes with a code that is optimized for some other distribution $\mathbf { q }$ , that is, $q _ { i }$ $, 0 \leq i \leq I - 1$ . Our code therefore takes about $- \log _ { 2 } { q _ { i } }$ bits, or $- \ln q _ { i }$ nats, to encode outcome $i$ , and the average compressed length per outcome is

$$
- \sum _ { i } p _ { i } \ln q _ { i } = H ( { \bf p } ) + \sum _ { i } p _ { i } \ln { \frac { p _ { i } } { q _ { i } } } \equiv H ( { \bf p } ) + D ( { \bf p } \| { \bf q } )
$$

The quantity

$$
D ( \mathbf { p } \| \mathbf { q } ) \equiv \sum _ { i } p _ { i } \ln { \frac { p _ { i } } { q _ { i } } }
$$

is called the Kullback-Leibler distance between $\mathbf { p }$ and $\mathbf { q }$ , also called the relative entropy between the two distributions. We can easily prove that it is nonnegative, since

$$
- D ( \mathbf { p } \| \mathbf { q } ) = \sum _ { i } p _ { i } \ln \left( { \frac { q _ { i } } { p _ { i } } } \right) \leq \sum _ { i } p _ { i } \left( { \frac { q _ { i } } { p _ { i } } } - 1 \right) = 1 - 1 = 0
$$

where the inequality follows from the fact that

$$
\ln w \leq w - 1
$$

(Of course we already knew it had to be nonnegative, because we knew that $H ( \mathbf { p } )$ was the smallest possible compressed message size for the distribution $\mathbf { p }$ .) The Kullback-Leibler distance between two distributions is zero only when the two distributions are identical. The Kullback-Leibler distance between any distribution $\mathbf { p }$ and the uniform distribution $\mathbf { U }$ is just the difference between the entropy of $\mathbf { p }$ and the maximum possible entropy $\ln { I }$ , that is,

$$
H ( \mathbf { p } ) + D ( \mathbf { p } \| \mathbf { U } ) = \ln I
$$

This is illustrated in Figure 14.7.1. Just like entropy, the Kullback-Leibler distance is measured in bits or nats, depending on whether the logarithms are taken base 2 or $e$ , respectively.

![](images/2c797a61ce4ab816fe0b18bb36ab821c7e7fbeb413b5633d0a91e0f8eb5d74fb.jpg)  
Figure 14.7.1. Relation between the entropy of a distribution $\mathbf { p }$ , its Kullback-Leibler distance to the uniform distribution $\mathbf { U }$ , and its maximum possible entropy $\ln { I }$ .

Notice that the Kullback-Leibler distance is not symmetric, nor (it turns out) does it satisfy the triangle inequality. So it is not a true metric distance. It is, however, a useful measure of the degree by which some “target” distribution $\mathbf { q }$ differs from some “base” distribution $\mathbf { p }$ . We now give a couple of examples of where it naturally occurs.

Example 1. Suppose that we are seeing events drawn from the distribution $\mathbf { p }$ , but we want to rule out an alternative hypothesis that they are drawn from $\mathbf { q }$ . We might do this by computing a likelihood ratio,

$$
\mathcal { L } = \frac { p ( \mathrm { D a t a } | \mathbf { p } ) } { p ( \mathrm { D a t a } | \mathbf { q } ) } = \prod _ { \mathrm { d a t a } } \frac { p _ { i } } { q _ { i } }
$$

and rejecting the alternative hypothesis $\mathbf { q }$ if this ratio is larger than some large number, say $1 0 ^ { 6 }$ . (In the above shorthand notation, the product over “data” means that we substitute for $i$ in each factor the particular outcome of that factor’s individual data event.) Taking the logarithm of equation (14.7.12), you can easily see that, under hypothesis $\mathbf { p }$ , the average increase in ln $\mathcal { L }$ per data event is just $D ( \mathbf { p } \| \mathbf { q } )$ . In other words, the Kullback-Leibler distance is the expected log-likelihood with which a false hypothesis $\mathbf { q }$ can be rejected, per event. As we might expect, this has something to do with “how different” $\mathbf { q }$ is from p.

As a Bayesian aside, the reason that the above likelihood test is unsatisfyingly asymmetric is that, without the notion of a prior, we have no way to treat hypotheses $\mathbf { p }$ and $\mathbf { q }$ democratically. But suppose that $p ( \mathbf { p } )$ is the prior probability of $\mathbf { p }$ , so that $p ( \mathbf { q } ) = 1 - p ( \mathbf { p } )$ is the prior for $\mathbf { q }$ . Then the Bayes odds ratio on the two hypotheses is

$$
\mathrm { O . R . } = { \frac { p ( \mathbf { p } | \mathrm { D a t a } ) } { p ( \mathbf { q } | \mathrm { D a t a } ) } } = { \frac { p ( \mathrm { D a t a } | \mathbf { p } ) p ( \mathbf { p } ) } { p ( \mathrm { D a t a } | \mathbf { q } ) p ( \mathbf { q } ) } } = { \frac { p ( \mathbf { p } ) } { p ( \mathbf { q } ) } } \prod _ { \mathrm { d a t a } } { \frac { p _ { i } } { q _ { i } } }
$$

The figure of merit is now the expected increase in $\mathrm { l n } ( \mathrm { O . R . } )$ if $\mathbf { p }$ is true, minus the expected increase (that is, plus the expected decrease) if $\mathbf { q }$ is true, which can readily be seen to be

$$
p ( \mathbf { p } ) D ( \mathbf { p } \| \mathbf { q } ) + p ( \mathbf { q } ) D ( \mathbf { q } \| \mathbf { p } )
$$

per data event, which has the appropriate symmetry. We can use expression (14.7.14) to estimate how many data events we will need on average to distinguish between two distributions. Notice that in the case of a uniform (“noninformative”) prior, $p ( { \bf p } ) = p ( { \bf q } ) = 0 . 5$ , we get just the symmetrized average of the two Kullback-Leibler distances.

Example 2. Meanwhile, back at the racetrack where we are offered payoffs of $o _ { i }$ on events with probability $p _ { i } , \sum _ { i } p _ { i } = 1$ , we want to work out the best way to divide our capital across all the possible outcomes $i$ of each race. Suppose we bet a fraction $b _ { i }$ on outcome $i$ . Analgously to equation (14.7.6), we want to maximize the

average e-folding rate,

$$
W = \langle \ln ( b _ { i } o _ { i } ) \rangle = \sum _ { i } p _ { i } \ln ( b _ { i } o _ { i } )
$$

subject to the constraint

$$
\sum _ { i } b _ { i } = 1
$$

An easy calculation (using a Lagrange multiplier to impose the constraint) gives the result that the maximum occurs for

$$
b _ { i } = p _ { i }
$$

completely independent of the values $o _ { i }$ ! This remarkable result is called proportional betting, or sometimes Kelly’s formula [4].

In practice, the distribution $\mathbf { p }$ is imperfectly known, both to you and to the bookie at the track. Suppose that you estimate the outcome probabilities as $\mathbf { q }$ , while the bookie’s estimate is $\mathbf { r }$ . If the bookie is feeling generous, he offers payoffs that are fair bets according to his estimate,

$$
o _ { i } = 1 / r _ { i }
$$

while you place proportional bets with $b _ { i } = q _ { i }$ . Your e-folding rate is now

$$
W = \langle \ln ( b _ { i } o _ { i } ) \rangle = \sum _ { i } p _ { i } \ln { \frac { q _ { i } } { r _ { i } } } = D ( \mathbf { p } \| \mathbf { r } ) - D ( \mathbf { p } \| \mathbf { q } )
$$

This will be positive if and only if your estimate of the probabilities is better than the bookie’s, that is, closer as measured by the Kullback-Leibler distance. Betting, in other words, is a competition between you and the bookie over who can better estimate the true odds.

A more realistic variant is to assume that the bookie offers payoffs of only some fraction $f < 1$ of his reciprocal probability estimates. Then (you can work out), you can win only if

$$
D ( \mathbf { p } \| \mathbf { r } ) - D ( \mathbf { p } \| \mathbf { q } ) > - \ln f
$$

# 14.7.3 Conditional Entropy and Mutual Information

We now want to look at the association of two variables. Let us return to the guessing game that was discussed in $\ S 1 4 . 7 . 1$ . Suppose we are deciding what question to ask next in the game and have to choose between two candidates, or possibly want to ask both in one order or another. Suppose that one question, $x$ , has $I$ possible answers, labeled by $i$ , and that the other question, $y$ , has $J$ possible answers, labeled by $j$ . Then the possible outcomes of asking both questions form a contingency table whose entries are the joint outcome probabilities $p _ { i j }$ , normalized by

$$
\sum _ { i = 0 } ^ { I - 1 } \sum _ { j = 0 } ^ { J - 1 } p _ { i j } \equiv \sum _ { i , j } p _ { i j } = 1
$$

We use the same “dot” notation as in $\ S 1 4 . 4$ to denote the row and column sums, so that $p _ { i }$  is the probability of outcome $i$ asking question $x$ only, while $p . _ { j }$ is the probability of outcome $j$ asking question $y$ only. The entropies of the questions $x$ and $y$ are thus, respectively,

$$
H ( x ) = - \sum _ { i } p _ { i } . \ln p _ { i } . \qquad H ( y ) = - \sum _ { j } p . _ { j } \ln p . _ { j }
$$

The entropy of the two questions together is

$$
H ( x , y ) = - \sum _ { i , j } p _ { i j } \ln p _ { i j }
$$

Now what is the entropy of the question $y$ given $x$ (that is, if $x$ is asked first)? It is the expectation value over the answers to $x$ of the entropy of the restricted $y$ distribution that lies in a single column of the contingency table (corresponding to the $x$ answer):

$$
H ( y | x ) = - \sum _ { i } p _ { i } . \sum _ { j } \frac { p _ { i j } } { p _ { i } } \ln \frac { p _ { i j } } { p _ { i } . } = - \sum _ { i , j } p _ { i j } \ln \frac { p _ { i j } } { p _ { i } . }
$$

Correspondingly, the entropy of $x$ given $y$ is

$$
H ( x | y ) = - \sum _ { j } p . j \sum _ { i } \frac { p _ { i j } } { p . j } \ln \frac { p _ { i j } } { p . j } = - \sum _ { i , j } p _ { i j } \ln \frac { p _ { i j } } { p . j }
$$

We can readily prove that the entropy of $y$ given $x$ is never more than the entropy of $y$ alone, i.e., that asking $x$ first can only reduce the usefulness of asking $y$ (in which case the two variables are associated):

$$
\begin{array} { l } { { \displaystyle H ( y | x ) - H ( y ) = - \sum _ { i , j } p _ { i j } \ln \frac { p _ { i j } / p _ { i \cdot } } { p _ { j \cdot } } } } \\ { { \displaystyle = \sum _ { i , j } p _ { i j } \ln \frac { p _ { \cdot j } p _ { i \cdot } } { p _ { i j } } } } \\ { { \displaystyle \le \sum _ { i , j } p _ { i j } \left( \frac { p _ { \cdot j } p _ { i \cdot } } { p _ { i j } } - 1 \right) } } \\ { { \displaystyle = \sum _ { i , j } p _ { i \cdot } p _ { \cdot j } - \sum _ { i , j } p _ { i j } } } \\ { { \displaystyle = 1 = 1 = 0 } } \end{array}
$$

Quantities like $H ( x | y )$ or $H ( y | x )$ are called conditional entropies. You can easily show that

$$
H ( x , y ) = H ( x ) + H ( y | x ) = H ( y ) + H ( x | y )
$$

sometimes called the chain rule for entropies. It immediately follows that

$$
H ( x ) - H ( x | y ) = H ( y ) - H ( y | x ) \equiv I ( x , y )
$$

$$
\begin{array}{c} \overleftarrow { \overleftarrow { \overleftarrow { } } H ( x ) \overleftarrow { \overleftarrow { \overleftarrow { } } H ( x , y ) \overbrace { \begin{array} { \overleftarrow { } } H ( y ) \overleftarrow { \overleftarrow { } } H ( y )  } \end{array} } }  \\ { \overleftarrow { } H ( x | y ) \longrightarrow \overleftarrow { \overleftarrow { } H ( y | x )  } } \end{array} 
$$

Figure 14.7.2. Relations among the entropies, conditional entropies, and mutual information of two variables. The quantities shown as segment lengths are always positive.

a quantity called the mutual information between $x$ and $y$ , given explicitly by

$$
I ( x , y ) = \sum _ { i , j } p _ { i j } \ln \left( \frac { p _ { i j } } { p _ { i \cdot } p _ { \cdot j } } \right)
$$

Notice that the mutual information is symmetrical, $I ( x , y ) = I ( y , x )$ .

Figure 14.7.2 provides a handy way to visualize the additive relations and inequalities among the quantities discussed. As before, all the quantities are measured in bits or nats. Using mutual information, one can make statements like this about the degree of association of two variables: “The variables have information (entropy) 6.5 and 4.2 bits, respectively. However, their mutual information is 3.8 bits, so together they provide only 6.9 bits of information.”

As a more detailed example, let us go back to the racetrack one last time. Suppose that you have some side information relevant to the outcome, but not completely predictive. That is, $x$ is the random variable of which outcome $i$ wins, while $y$ is a random variable whose value $j$ you know. Instead of a simple set of probabilities $p _ { i }$ , we now have a contingency table of joint outcomes, $p _ { i j }$ . How should you bet, and what is your expected e-folding rate?

First, we need to generalize equation (14.7.17). Suppose that $b _ { i j }$ is the fraction of assets that we bet on outcome $i$ when our side information has the value $j$ . There are now $J$ separate constraints,

$$
\sum _ { i } b _ { i j } = 1 , \qquad 0 \leq j \leq J - 1
$$

For simplicity, let us take the case where the payoffs are for fair bets (but without the side information), $o _ { i } = 1 / p _ { i }$  . Then we want to maximize

$$
W = \left. \ln { \frac { b _ { i j } } { p _ { i } . } } \right. = \sum _ { i , j } p _ { i j } \ln { \frac { b _ { i j } } { p _ { i } . } }
$$

A simple calculation, now with $J$ distinct Lagrange multipliers, gives the result,

$$
b _ { i j } = { \frac { p _ { i j } } { p \cdot { } _ { j } } }
$$

This is again proportional betting, except that it is now conditioned on the value $j$ that is known to us. Substituting equation (14.7.32) into (14.7.31) gives

$$
W = \sum _ { i , j } p _ { i j } \ln \left( { \frac { p _ { i j } } { p _ { i \cdot } p _ { \cdot j } } } \right) = I ( x , y )
$$

We see that the expected e-folding rate is exactly the mutual information between $x$ and $y$ . In other words, we can make money if and only if our side information $y$ has nonzero mutual information with the outcome $x$ . As in equation (14.7.20), you can easily work out more realistic cases where the payouts are not fair bets, or are based on inexact estimates of the true probabilities. A special case of equation (14.7.33) is when the side information $y$ predicts the outcome $x$ perfectly. Then, $I ( x , y ) = H ( x ) = H ( y ) = H ( x , y )$ and we recover exactly equation (14.7.6).

# 14.7.4 Uncertainty Coefficients

By analogy with the various coefficients of correlation discussed earlier in this chapter, one sometimes sees uncertainty coefficients defined from the various entropies defined above (and in Figure 14.7.2). The uncertainty coefficient of $y$ with respect to $x$ , denoted $U ( y | x )$ , is defined by

$$
U ( y | x ) \equiv \frac { H ( y ) - H ( y | x ) } { H ( y ) }
$$

This measure lies between 0 and 1, with the value 0 indicating that $x$ and $y$ have no association and the value 1 indicating that knowledge of $x$ completely predicts $y$ . For in-between values, $U ( y | x )$ gives the fraction of $y$ ’s entropy $H ( y )$ that is lost if $x$ is already known. In our game of “twenty questions,” $U ( y | x )$ is the fractional loss in the utility of question $y$ if question $x$ is to be asked first.

If we wish to view $x$ as the dependent variable and $y$ as the independent one, then interchanging $x$ and $y$ we can of course define the dependency of $x$ on $y$ ,

$$
U ( x | y ) \equiv { \frac { H ( x ) - H ( x | y ) } { H ( x ) } }
$$

If we want to treat $x$ and $y$ symmetrically, then the useful combination turns out to be

$$
U ( x , y ) \equiv 2 \left[ \frac { H ( y ) + H ( x ) - H ( x , y ) } { H ( x ) + H ( y ) } \right]
$$

If the two variables are completely independent, then $H ( x , y ) = H ( x ) + H ( y )$ , so (14.7.36) vanishes. If the two variables are completely dependent, then $H ( x ) =$ $H ( y ) = H ( x , y )$ , so (14.7.35) equals unity. You can easily show that

$$
U ( x , y ) = \frac { H ( x ) U ( x | y ) + H ( y ) U ( y | x ) } { H ( x ) + H ( y ) }
$$

that is, that the symmetrical measure is just a weighted average of the two asymmetrical measures (14.7.34) and (14.7.35), weighted by the entropy of each variable separately.

Generally we find the entropy measures themselves, in bits or nats, more useful than the uncertainty coefficients derived from them.

# CITED REFERENCES AND FURTHER READING:

Shannon, C.E., and Weaver, W. 1949, The Mathematical Theory of Communication, reprinted 1998 (Urbana, IL: University of Illinois Press).[1]

Cover, T.M., and Thomas, J.A. 1991, Elements of Information Theory (New York: Wiley). [2]   
MacKay, D.J.C. 2003, Information Theory Inference and Learning Algorithms (Cambridge, UK: Cambridge University Press). [3]   
Kelly, J. 1956, “A New Interpretation of Information Rate,” Bell System Technical Journal, vol. 35, pp. 917–926. [4]

# 14.8 Do Two-Dimensional Distributions Differ?

We here discuss a useful generalization of the $\mathrm { K } { - } S$ test (-14.3) to two-dimensional distributions. This generalization is due to Fasano and Franceschini [1], a variant on an earlier idea due to Peacock [2].

In a two-dimensional distribution, each data point is characterized by an $( x , y )$ pair of values. An example near to our hearts is that each of the 19 neutrinos that were detected from Supernova 1987A is characterized by a time $t _ { i }$ and by an energy $E _ { i }$ (see [3]). We might wish to know whether these measured pairs $( t _ { i } , E _ { i } )$ ; $i = 0 \dots 1 8$ are consistent with a theoretical model that predicts neutrino flux as a function of both time and energy — that is, a two-dimensional probability distribution in the $( x , y )$ [here, $( t , E ) ]$ plane. That would be a one-sample test. Or, given two sets of neutrino detections, from two comparable detectors, we might want to know whether they are compatible with each other, a two-sample test.

In the spirit of the tried-and-true one-dimensional K–S test, we want to range over the $( x , y )$ -plane in search of some kind of maximum cumulative difference between two two-dimensional distributions. Unfortunately, cumulative probability distribution is not well-defined in more than one dimension! Peacock’s insight was that a good surrogate is the integrated probability in each of four natural quadrants around a given point $( x _ { i } , y _ { i } )$ , namely the total probabilities (or fraction of data) in $( x > x _ { i } , y > y _ { i } )$ /, $( x < x _ { i } , y > y _ { i } )$ /, $( x < x _ { i } , y < y _ { i } )$ /, $( x > x _ { i } , y < y _ { i }$ /. The twodimensional $\mathrm { K } { - } S$ statistic $D$ is now taken to be the maximum difference (ranging both over data points and over quadrants) of the corresponding integrated probabilities. When comparing two data sets, the value of $D$ may depend on which data set is ranged over. In that case, define an effective $D$ as the average of the two values obtained. If you are confused at this point about the exact definition of $D$ , don’t fret; the accompanying computer routines amount to a precise algorithmic definition.

Figure 14.8.1 gives a feeling for what is going on. The 65 triangles and 35 squares seem to have somewhat different distributions in the plane. The dotted lines are centered on the triangle that maximizes the $D$ statistic; the maximum occurs in the upper-left quadrant. That quadrant contains only 0.12 of all the triangles, but it contains 0.56 of all the squares. The value of $D$ is thus 0.44. Is this statistically significant?

Even for fixed sample sizes, it is unfortunately not rigorously true that the distribution of $D$ in the null hypothesis is independent of the shape of the two-dimensional distribution. In this respect the two-dimensional $\mathrm { K } { - } S$ test is not as natural as its onedimensional parent. However, extensive Monte Carlo integrations have shown that the distribution of the two-dimensional $D$ is very nearly identical for even quite different distributions, as long as they have the same coefficient of correlation $r$ , defined in the usual way by equation (14.5.1). In their paper, Fasano and Franceschini tabulate Monte Carlo results for (what amounts to) the distribution of $D$ as a function of (of course) $D$ , sample size $N$ , and coefficient of correlation $r$ . Analyzing their results, one finds that the significance levels for the two-dimensional $\mathrm { K } { - } S$ test can be summarized by the simple, though approximate, formulas

![](images/28d0a8b61db7554fec687ebcca5e61cfafc087c7a48cdbd808f9c4aaac0771d5.jpg)  
Figure 14.8.1. Two-dimensional distributions of 65 triangles and 35 squares. The two-dimensional K–S test finds that point one of whose quadrants (shown by dotted lines) maximizes the difference between fraction of triangles and fraction of squares. Then, equation (14.8.1) indicates whether the difference is statistically significant, i.e., whether the triangles and squares must have different underlying distributions.

$$
\mathrm { P r o b a b i l i t y ~ } ( D > \mathrm { o b s e r v e d ~ } ) = { \cal Q } _ { K S } \left( \frac { \sqrt { N } D } { 1 + \sqrt { 1 - r ^ { 2 } } ( 0 . 2 5 - 0 . 7 5 / \sqrt { N } ) } \right)
$$

for the one-sample case, and the same for the two-sample case, but with

$$
N = \frac { N _ { 1 } N _ { 2 } } { N _ { 1 } + N _ { 2 } } .
$$

The above formulas are accurate enough when $N \gtrsim 2 0$ , and when the indicated probability (significance level) is less than (more significant than) 0:20 or so. When the indicated probability is $> ~ 0 . 2 0$ , its value may not be accurate, but the implication that the data and model (or two data sets) are not significantly different is certainly correct. Notice that in the limit of $r  1$ (perfect correlation), equations (14.8.1) and (14.8.2) reduce to equations (14.3.18) and (14.3.19): The twodimensional data lie on a perfect straight line, and the two-dimensional K–S test becomes a one-dimensional K–S test.

The significance level for the data in Figure 14.8.1, by the way, is about 0.001. This establishes to a near-certainty that the triangles and squares were drawn from different distributions. (As in fact they were.)

Of course, if you do not want to rely on the Monte Carlo experiments embodied in equation (14.8.1), you can do your own: Generate a lot of synthetic data sets from your model, each one with the same number of points as the real data set. Compute $D$ for each synthetic data set, using the accompanying computer routines (but ignoring their calculated probabilities), and count what fraction of the time these synthetic $D$ ’s exceed the $D$ from the real data. That fraction is your significance.

One disadvantage of the two-dimensional tests, by comparison with their onedimensional progenitors, is that the two-dimensional tests require of order $N ^ { 2 }$ operations: Two nested loops of order $N$ take the place of an $N \log N$ sort. For desktop computers, this restricts the usefulness of the tests to $N$ less than several thousand.

We now give computer implementations. The one-sample case is embodied in the routine $\mathtt { k s 2 d 1 s }$ (that is, two dimensions, one sample). This routine calls a straightforward utility routine quadct to count points in the four quadrants, and it calls a user-supplied routine quadvl that must be capable of returning the integrated probability of an analytic model in each of four quadrants around an arbitrary $( x , y )$ point. A trivial sample quadvl is shown; realistic quadvls can be quite complicated, often incorporating numerical quadratures over analytic two-dimensional distributions.

void ks2d1s(VecDoub_I &x1, VecDoub_I &y1, void quadvl(const Doub, const Doub, Doub &, Doub &, Doub &, Doub &), Doub &d1, Doub &prob)

Two-dimensional Kolmogorov-Smirnov test of one sample against a model. Given the $x$ and $y$ coordinates of n1 data points in arrays x1[0..n1-1] and y1[0..n1-1], and given a usersupplied function quadvl that exemplifies the model, this routine returns the two-dimensional K-S statistic as d1, and its $p$ -value as prob. Small values of prob show that the sample is significantly different from the model. Note that the test is slightly distribution-dependent, so prob is only an estimate.

Int j,n1 $\underline { { \underline { { \mathbf { \Pi } } } } } =$ x1.size();   
Doub dum,dumm,fa,fb,fc,fd,ga,gb,gc,gd,r1,rr,sqen;   
KSdist ks;   
${ \tt d } 1 { = } 0 . 0$ ;   
for (j=0;j<n1;j++) { Loop over the data points. quadct(x1[j],y1[j],x1,y1,fa,fb,fc,fd); quadvl(x1[j],y1[j],ga,gb,gc,gd); if (fa $>$ ga) fa $+ =$ 1.0/n1; if (fb $>$ gb) fb $+ =$ 1.0/n1; if (fc $>$ gc) fc $+ =$ 1.0/n1; if (fd $>$ gd) fd $+ =$ 1.0/n1; d1=MAX(d1,abs(fa-ga)); d1=MAX(d1,abs(fb-gb)); d1=MAX(d1,abs(fc-gc)); d1=MAX(d1,abs(fd-gd)); For both the sample and the model, the distribution is integrated in each of fou quadrants, and the maximum difference is saved.

Get the linear correlation coefficient r1.

sqen=sqrt(Doub(n1));   
rr=sqrt(1.0-r1\*r1);   
Estimate the probability using the K-S probability function.   
prob=ks.qks(d1\*sqen/(1.0+rr\*(0.25-0.75/sqen)));

void quadct(const Doub x, const Doub y, VecDoub_I &xx, VecDoub_I &yy, Doub &fa, Doub &fb, Doub &fc, Doub &fd)

Given an origin $( \mathbf { x } , \mathbf { y } )$ , and an array of nn points with coordinates $\mathbf { x x } \left[ 0 \ldots \mathrm { n n - 1 } \right]$ and yy $\left[ 0 \cdot \cdot \mathbf { n } \mathbf { n } ^ { - 1 } \right]$ , count how many of them are in each quadrant around the origin, and return the normalized fractions. Quadrants are labeled alphabetically, counterclockwise from the upper right. Used by ks2d1s and ks2d2s.

Int k,na,nb,nc,nd,nn=xx.size();   
Doub ff;   
na=nb=nc=nd=0;   
for (k=0;k<nn;k++) { if (yy[k] $\scriptstyle = = \mathbf { y }$ && xx[k] $\mathbf { \Psi } = \mathbf { \Psi } \mathbf { x } .$ ) continue; if (yy[k] $>$ y) xx[k] > x ? ++na : ++nb; else xx[k] > x ? ++nd : ++nc;   
}   
ff $^ { = 1 }$ .0/nn;   
fa=ff\*na;   
fb=ff\*nb;   
fc=ff\*nc;   
fd=ff\*nd;

# quadvl.h

void quadvl(const Doub x, const Doub y, Doub &fa, Doub &fb, Doub &fc, Doub &fd) This is a sample of a user-supplied routine to be used with ks2d1s. In this case, the model distribution is uniform inside the square $- 1 < x < 1$ , $- 1 < y < 1$ . In general, this routine should return, for any point $( \mathbf { x } , \mathbf { y } )$ , the fraction of the total distribution in each of the four quadrants around that point. The fractions, fa, fb, fc, and fd, must add up to 1. Quadrants are alphabetical, counterclockwise from the upper right.

Doub qa,qb,qc,qd;   
qa=MIN(2.0,MAX(0.0,1.0-x));   
qb=MIN(2.0,MAX(0.0,1.0-y));   
qc=MIN(2.0,MAX(0.0,x+1.0));   
qd=MIN(2.0,MAX(0.0,y+1.0));   
fa=0.25\*qa\*qb;   
fb=0.25\*qb\*qc;   
fc=0.25\*qc\*qd;   
fd=0.25\*qd\*qa;

The routine ks2d2s is the two-sample case of the two-dimensional K–S test. It also calls quadct, pearsn, and KSdist::qks. Being a two-sample test, it does not need an analytic model.

void ks2d2s(VecDoub_I &x1, VecDoub_I &y1, VecDoub_I &x2, VecDoub_I &y2, Doub &d, kstes Doub &prob)

# ts 2d.h

Two-dimensional Kolmogorov-Smirnov test on two samples. Given the $x$ and $y$ coordinates of the first sample as n1 values in arrays x1[0..n1-1] and y1[0..n1-1], and likewise for the second sample, n2 values in arrays $\tt x 2$ and y2, this routine returns the two-dimensional, twosample K-S statistic as d, and its $p$ -value as prob. Small values of prob show that the two samples are significantly different. Note that the test is slightly distribution-dependent, so prob is only an estimate.

Int j,n1=x1.size(), ${ \tt n } 2 \mathrm { = } \tt { x } 2$ .size();   
Doub d1,d2,dum,dumm,fa,fb,fc,fd,ga,gb,gc,gd,r1,r2,rr,sqen;   
KSdist ks;   
$\mathtt { d 1 = 0 }$ .0;   
for $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<n1;j++) { First, use points in the first sample as origins. quadct(x1[j],y1[j],x1,y1,fa,fb,fc,fd); quadct(x1[j],y1[j],x2,y2,ga,gb,gc,gd); if (fa $>$ ga) fa $+ =$ 1.0/n1; if (fb $>$ gb) fb $+ =$ 1.0/n1; if (fc $>$ gc) fc $+ =$ 1.0/n1; if (fd $>$ gd) fd $+ =$ 1.0/n1; d1=MAX(d1,abs(fa-ga)); d1=MAX(d1,abs(fb-gb)); d1=MAX(d1,abs(fc-gc)); d1 $=$ MAX(d1,abs(fd-gd));   
}   
$\mathtt { d } 2 \mathtt { = } 0$ .0;   
for ( $\scriptstyle \mathbf { j } = 0$ ;j<n2;j++) { Then, use points in the second sample as quadct(x2[j],y2[j],x1,y1,fa,fb,fc,fd); origins. quadct(x2[j],y2[j],x2,y2,ga,gb,gc,gd); if (ga $>$ fa) ga $+ =$ 1.0/n1; if (gb $>$ fb) gb $+ =$ 1.0/n1; if (gc $>$ fc) gc $+ =$ 1.0/n1; if (gd $>$ fd) gd $+ =$ 1.0/n1; ${ \tt d } 2 =$ MAX(d2,abs(fa-ga)); d2=MAX(d2,abs(fb-gb)); d2=MAX(d2,abs(fc-gc)); d2=MAX(d2,abs(fd-gd));   
}   
d=0. $^ { 5 \ast }$ (d1+d2); Average the K-S statistics.   
sqen sqrt(n1\*n2/Doub(n1+n2));   
pearsn(x1,y1,r1,dum,dumm); Get the linear correlation coefficient for each   
pearsn(x2,y2,r2,dum,dumm); sample.   
rr=sqrt(1.0-0.5\*(r1\*r1+r2\*r2));   
Estimate the probability using the K-S probability function.   
prob ks.qks(d\*sqen/(1.0+rr\*(0.25-0.75/sqen)));

# CITED REFERENCES AND FURTHER READING:

Fasano, G. and Franceschini, A. 1987, “A Multidimensional Version of the Kolmogorov-Smirnov Test,” Monthly Notices of the Royal Astronomical Society, vol. 225, pp. 155–170.[1]   
Peacock, J.A. 1983, “Two-Dimensional Goodness-of-Fit Testing in Astronomy,” Monthly Notices of the Royal Astronomical Society,vol. 202,pp. 615-627.[2]   
Spergel, D.N., Piran, T., Loeb, A., Goodman, J., and Bahcall, J.N. 1987, “A Simple Model for Neutrino Cooling of the LMC Supernova,” Science, vol. 237, pp. 1471–1473.[3]

# 14.9 Savitzky-Golay Smoothing Filters

In $\ S 1 3 . 5$ we learned something about the construction and application of digital filters, but little guidance was given on which particular filter to use. That, of course, depends on what you want to accomplish by filtering. One obvious use for low-pass filters is to smooth noisy data.

The premise of data smoothing is that one is measuring a variable that is both slowly varying and also corrupted by random noise. Then it can sometimes be useful to replace each data point by some kind of local average of surrounding data points. Since nearby points measure very nearly the same underlying value, averaging can reduce the level of noise without (much) biasing the value obtained.

We must comment editorially that the smoothing of data lies in a murky area, beyond the fringe of some better-posed, and therefore more highly recommended, techniques that are discussed elsewhere in this book. If you are fitting data to a parametric model, for example (see Chapter 15), it is almost always better to use raw data than to use data that have been pre-processed by a smoothing procedure. Another alternative to blind smoothing is so-called “optimal” or Wiener filtering, as discussed in $\ S 1 3 . 3$ and more generally in $\ S 1 3 . 6$ . Data smoothing is probably most justified when it is used simply as a graphical technique, to guide the eye through a forest of data points all with large error bars, or as a means of making initial rough estimates of simple parameters from a graph.

In this section we discuss a particular type of low-pass filter, well-adapted for data smoothing, and termed variously Savitzky-Golay [1], least-squares [2], or DISPO (Digital Smoothing Polynomial) [3] filters. Rather than having their properties defined in the Fourier domain and then translated to the time domain, Savitzky-Golay filters derive directly from a particular formulation of the data smoothing problem in the time domain, as we will now see. Savitzky-Golay filters were initially (and are still often) used to render visible the relative widths and heights of spectral lines in noisy spectrometric data.

Recall that a digital filter is applied to a series of equally spaced data values $f _ { i } \equiv f ( t _ { i } )$ , where $t _ { i } ~ \equiv ~ t _ { 0 } + i \Delta$ for some constant sample spacing $\Delta$ and $i \ =$ $\ldots - 2 , - 1 , 0 , 1 , 2 , \ldots .$ We have seen (-13.5) that the simplest type of digital filter (the nonrecursive or finite impulse response filter) replaces each data value $f _ { i }$ by a linear combination $g _ { i }$ of itself and some number of nearby neighbors,

$$
g _ { i } = \sum _ { n = - n _ { L } } ^ { n _ { R } } c _ { n } f _ { i + n }
$$

Here $n _ { L }$ is the number of points used “to the left” of a data point $i$ , i.e., earlier than it, while $n _ { R }$ is the number used to the right, i.e., later. A so-called causal filter would have $n _ { R } = 0$ .

As a starting point for understanding Savitzky-Golay filters, consider the simplest possible averaging procedure: For some fixed $n _ { L } \ = \ n _ { R }$ , compute each $g _ { i }$ as the average of the data points from $f _ { i - n _ { L } }$ to $f _ { i + n _ { R } }$ . This is sometimes called moving window averaging and corresponds to equation (14.9.1) with constant $c _ { n } =$ $1 / ( n _ { L } + n _ { R } + 1 )$ . If the underlying function is constant, or is changing linearly with time (increasing or decreasing), then no bias is introduced into the result. Higher points at one end of the averaging interval are on the average balanced by lower points at the other end. A bias is introduced, however, if the underlying function has a nonzero second derivative. At a local maximum, for example, moving window averaging always reduces the function value. In the spectrometric application, a narrow spectral line has its height reduced and its width increased. Since these parameters are themselves of physical interest, the bias introduced is distinctly undesirable.

Note, however, that moving window averaging does preserve the area under a spectral line, which is its zeroth moment, and also (if the window is symmetric with $n _ { L } = n _ { R }$ ) its mean position in time, which is its first moment. What is violated is the second moment, equivalent to the line width.

The idea of Savitzky-Golay filtering is to find filter coefficients $c _ { n }$ that preserve higher moments. Equivalently, the idea is to approximate the underlying function within the moving window not by a constant (whose estimate is the average), but by a polynomial of higher order, typically quadratic or quartic: For each point $f _ { i }$ , we least-squares fit a polynomial to all $n _ { L } + n _ { R } + 1$ points in the moving window, and then set $g _ { i }$ to be the value of that polynomial at position $i$ . (If you are not familiar with least-squares fitting, you might want to look ahead to Chapter 15.) We make no use of the value of the polynomial at any other point. When we move on to the next point $f _ { i + 1 }$ , we do a whole new least-squares fit using a shifted window.

All these least-squares fits would be laborious if done as described. Luckily, since the process of least-squares fitting involves only a linear matrix inversion, the coefficients of a fitted polynomial are themselves linear in the values of the data. That means that we can do all the fitting in advance, for fictitious data consisting of all zeros except for a single 1, and then do the fits on the real data just by taking linear combinations. This is the key point, then: There are particular sets of filter coefficients $c _ { n }$ for which equation (14.9.1) “automatically” accomplishes the process of polynomial least-squares fitting inside a moving window.

To derive such coefficients, consider how $g _ { 0 }$ might be obtained: We want to fit a polynomial of degree $M$ in $i$ , namely $a _ { 0 } + a _ { 1 } i + \cdots + a _ { M } i ^ { M }$ , to the values $f _ { - n _ { L } } , \ldots , f _ { n _ { R } }$ . Then $g _ { 0 }$ will be the value of that polynomial at $i = 0$ , namely $a _ { 0 }$ . The design matrix for this problem (-15.4) is

$$
A _ { i j } = i ^ { j } \qquad i = - n _ { L } , \dots , n _ { R } , \quad j = 0 , \dots , M
$$

and the normal equations for the vector of $a _ { j }$ ’s in terms of the vector of $f _ { i }$ ’s is in matrix notation

$$
( \mathbf { A } ^ { T } \cdot \mathbf { A } ) \cdot \mathbf { a } = \mathbf { A } ^ { T } \cdot \mathbf { f } \qquad { \mathrm { o r } } \qquad \mathbf { a } = ( \mathbf { A } ^ { T } \cdot \mathbf { A } ) ^ { - 1 } \cdot ( \mathbf { A } ^ { T } \cdot \mathbf { f } )
$$

We also have the specific forms

$$
\left\{ \mathbf { A } ^ { T } \cdot \mathbf { A } \right\} _ { i j } = \sum _ { k = - n _ { L } } ^ { n _ { R } } A _ { k i } A _ { k j } = \sum _ { k = - n _ { L } } ^ { n _ { R } } k ^ { i + j }
$$

and

$$
\left\{ \mathbf { A } ^ { T } \cdot \mathbf { f } \right\} _ { j } = \sum _ { k = - n _ { L } } ^ { n _ { R } } A _ { k j } f _ { k } = \sum _ { k = - n _ { L } } ^ { n _ { R } } k ^ { j } f _ { k }
$$

Since the coefficient $c _ { n }$ is the component $a _ { 0 }$ when $\mathbf { f }$ is replaced by the unit vector $\mathbf { e } _ { n } , - n _ { L } \leq n < n _ { R }$ , we have

$$
c _ { n } = \left\{ ( \mathbf { A } ^ { T } \cdot \mathbf { A } ) ^ { - 1 } \cdot ( \mathbf { A } ^ { T } \cdot \mathbf { e } _ { n } ) \right\} _ { 0 } = \sum _ { m = 0 } ^ { M } \left\{ ( \mathbf { A } ^ { T } \cdot \mathbf { A } ) ^ { - 1 } \right\} _ { 0 m } n ^ { m }
$$

Equation (14.9.6) says that we need only one row of the inverse matrix. (Numerically we can get this by $L U$ decomposition with only a single backsubstitution.)

The function savgol, below, implements equation (14.9.6). As input, it takes the parameters $\mathrm { { n } } 1 = n _ { L }$ , $\mathbf { n } \mathbf { r } = n _ { R }$ , and ${ \mathfrak { m } } = M$ (the desired order). Also input is $\mathtt { n p }$ , the physical length of the output array c, and a parameter ld that for data fitting should be zero. In fact, ld specifies which coefficient among the $a _ { i }$ ’s should be returned, and we are here interested in $a _ { 0 }$ . For another purpose, namely the computation of numerical derivatives (already mentioned in $\ S 5 . 7 )$ , the useful choice is $\exists \mathsf { d } \geq 1$ . With $\exists { \textrm { d } } = \ 1$ , for example, the filtered first derivative is the convolution (14.9.1) divided by the stepsize $\Delta$ . For $\exists { \mathsf { d } } = k \ > \ 1$ , the array c must be multiplied by $k !$ to give derivative coefficients. For derivatives, one usually wants ${ \mathfrak { m } } = 4$ or larger.

<table><tr><td>M</td><td>nL</td><td>nR</td><td colspan="7">Sample Savitzky-Golay Coefficients</td></tr><tr><td>2</td><td>2</td><td>2</td><td></td><td>-0.086 0.343</td><td>0.486</td><td>0.343-0.086</td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>3</td><td>1</td><td>-0.143</td><td>0.171 0.343</td><td>0.371</td><td>0.257</td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>4</td><td>0</td><td>0.086-0.143</td><td>-0.086 0.257</td><td>0.886</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>5</td><td>5</td><td>-0.084 0.021 0.103</td><td>0.161 0.196</td><td>0.207</td><td>0.196</td><td>0.161</td><td>0.103</td><td>0.021</td><td>-0.084</td></tr><tr><td>4</td><td>4</td><td>4</td><td>0.035 -0.128</td><td>0.070 0.315</td><td>0.417</td><td>0.315</td><td>0.070</td><td>-0.128</td><td>0.035</td><td></td></tr><tr><td>4</td><td>5</td><td>5</td><td>0.042 -0.105 -0.023</td><td>0.140 0.280</td><td>0.333</td><td>0.280</td><td></td><td>0.140 -0.023 -0.105</td><td></td><td>0.042</td></tr></table>

void savgol(VecDoub_O &c, const Int np, const Int nl, const Int nr, const Int ld, const Int m)

Returns in ${ \mathsf { c } } \left[ 0 \ldots \mathrm { \tt m p } { - } 1 \right]$ , in wraparound order (N.B.!) consistent with the argument respns in routine convlv, a set of Savitzky-Golay filter coefficients. nl is the number of leftward (past) data points used, while nr is the number of rightward (future) data points, making the total number of data points used ${ \tt n } 1 + { \tt n } { \tt r } + 1$ . ld is the order of the derivative desired (e.g., $\mathtt { l d } = 0$ for smoothed function. For the derivative of order $k$ , you must multiply the array $^ \texttt { c }$ by $k ! .$ ) m is the order of the smoothing polynomial, also equal to the highest conserved moment; usual values are ${ \mathfrak { m } } = 2$ or ${ \mathfrak { m } } = 4$ .

Int j,k,imj,ipj,kk,mm;   
Doub fac,sum;   
if ( $\mathrm { n p } < \mathrm { n } \mathrm { 1 } { + } \mathrm { n } \mathrm { r } { + } \mathrm { 1 }$ || nl < 0 || nr < 0 || ld > m || nl+nr < m) throw("bad args in savgol");   
VecInt indx $\left( \mathrm { m } { + } 1 \right)$ );   
MatDoub $\mathtt { a } ( \mathtt { m } + 1 , \mathtt { m } + 1 )$ ;   
VecDoub $\mathsf { b } \left( \mathtt { m } + 1 \right)$ ;   
for (ipj ${ = } 0$ ;ipj $< =$ (m << 1);ipj $^ { + + }$ ) { Set up the normal equations of the desired sum=(ipj ? 0.0 : 1.0); least-squares fit. for $\scriptstyle ( \mathtt { k } = 1$ ;k $< =$ nr; $\mathbf { k } { + } { + }$ ) sum $+ =$ pow(Doub(k),Doub(ipj)); for $\mathrm { ( k = 1 }$ ; $\Bbbk < = \tt n 1$ ; $\mathbf { k } { + } { + }$ ) sum $+ =$ pow(Doub(-k),Doub(ipj)); mm=MIN(ipj, $2 * \mathtt { m } ^ { - }$ -ipj); for (imj $=$ -mm;imj $< =$ mm;imj $+ { = } 2$ ) a[(ipj+imj)/2][(ipj-imj)/2] $=$ sum;   
}   
LUdcmp alud(a); Solve them: LU decomposition.   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<m+1;j $^ { + + }$ ) b[j] $= 0 . 0$ ;   
b[ld] $= 1$ .0;   
Right-hand side vector is unit vector, depending on which derivative we want.   
alud.solve(b,b); Get one row of the inverse matrix.   
for (kk ${ = } 0$ ;kk<np;kk $^ { + + }$ ) c[kk] ${ = } 0$ .0; Zero the output array (it may be bigger than   
for $\mathrm { ( k \Omega = \Omega - n 1 }$ ;k<=nr;k++) { number of coefficients). sum $\mathbf { \tau } = \mathbf { \dot { \tau } }$ b[0]; Each Savitzky-Golay coefficient is the dot fac $^ { = 1 }$ .0; product of powers of an integer with the for (mm=1;mm $< = \mathtt { m }$ ;mm $^ { + + }$ ) sum $+ =$ b[mm]\*(fac \*= k); inverse matrix row. $\mathbf { k } \mathbf { k } { = } \left( \mathbf { n } \mathbf { p } { - } \mathbf { k } \right)$ % np; Store in wraparound order. c[kk] $=$ sum;   
}

As output, savgol returns the coefficients $c _ { n }$ , for $- n _ { L } \leq n \leq n _ { R }$ . These are stored in c in “wraparound order”; that is, $c _ { 0 }$ is in $\mathsf { c } \left[ 0 \right]$ , $c _ { - 1 }$ is in c[1], and so on for further negative indices. The value $c _ { 1 }$ is stored in $\mathsf { c } \left[ \mathrm { n p } { - } 1 \right]$ , $c _ { 2 }$ in $\mathsf { c } \left[ \mathrm { n p } { - } 2 \right]$ , and so on for positive indices. This order may seem arcane, but it is the natural one where causal filters have nonzero coefficients in low array elements of c. It is also the order required by the function convlv in $\ S 1 3 . 1$ , which can be used to apply the digital filter to a data set.

The table on the previous page shows some typical output from savgol. For orders 2 and 4, the coefficients of Savitzky-Golay filters with several choices of $n _ { L }$ and $n _ { R }$ are shown. The central column is the coefficient applied to the data $f _ { i }$ in obtaining the smoothed $g _ { i }$ . Coefficients to the left are applied to earlier data, to the right, to later. The coefficients always add (within roundoff error) to unity. One sees that, as befits a smoothing operator, the coefficients always have a central positive lobe, but with smaller, outlying corrections of both positive and negative sign. In practice, the Savitzky-Golay filters are most useful for much larger values of $n _ { L }$ and $n _ { R }$ , since these few-point formulas can accomplish only a relatively small amount of smoothing.

Figure 14.9.1 shows a numerical experiment using a 33-point smoothing filter, that is, $n _ { L } = n _ { R } = 1 6$ . The upper panel shows a test function, constructed to have six “bumps” of varying widths, all of height 8 units. To this function Gaussian white noise of unit variance has been added. (The test function without noise is shown as the dotted curves in the center and lower panels.) The widths of the bumps (full width at half of maximum, or FWHM) are 140, 43, 24, 17, 13, and 10, respectively.

The middle panel of Figure 14.9.1 shows the result of smoothing by a moving window average. One sees that the window of width 33 does quite a nice job of smoothing the broadest bump, but that the narrower bumps suffer considerable loss of height and increase of width. The underlying signal (dotted) is very badly represented.

The lower panel shows the result of smoothing with a Savitzky-Golay filter of the identical width and degree $M = 4$ . One sees that the heights and widths of the bumps are quite extraordinarily preserved. A trade-off is that the broadest bump is less smoothed. That is because the central positive lobe of the Savitzky-Golay filter coefficients fills only a fraction of the full 33-point width. As a rough guideline, best results are obtained when the full width of the degree 4 Savitzky-Golay filter is between 1 and 2 times the FWHM of desired features in the data. (References [3] and [4] give additional practical hints.)

Figure 14.9.2 shows the result of smoothing the same noisy “data” with broader Savitzky-Golay filters of three different orders. Here we have $n _ { L } = n _ { R } = 3 2$ (65- point filter) and $M = 2 , 4 , 6$ . One sees that, when the bumps are too narrow with respect to the filter size, even the Savitzky-Golay filter must at some point give out. The higher-order filter manages to track narrower features, but at the cost of less smoothing on broad features.

To summarize: Within limits, Savitzky-Golay filtering does manage to provide smoothing without loss of resolution. It does this by assuming that relatively distant data points have some significant redundancy that can be used to reduce the level of noise. The specific nature of the assumed redundancy is that the underlying function should be locally well-fitted by a polynomial. When this is true, as it is for smooth line profiles not too much narrower than the filter width, the performance of

![](images/e2cd7d7b5981492caa47e62aacdabdf5234290d94dcf706fa4c80d41c0a74243.jpg)  
Figure 14.9.1. Top: Synthetic noisy data consisting of a sequence of progressively narrower bumps and additive Gaussian white noise. Center: Result of smoothing the data by a simple moving window average. The window extends 16 points leftward and rightward, for a total of 33 points. Note that narrow features are broadened and suffer corresponding loss of amplitude. The dotted curve is the underlying function used to generate the synthetic data. Bottom: Result of smoothing the data by a Savitzky-Golay smoothing filter (of degree 4) using the same 33 points. While there is less smoothing of the broadest feature, narrower features have their heights and widths preserved.

Savitzky-Golay filters can be spectacular. When it is not true, these filters have no compelling advantage over other classes of smoothing filter coefficients.

A last remark concerns irregularly sampled data, where the values $f _ { i }$ are not uniformly spaced in time. The obvious generalization of Savitzky-Golay filtering would be to do a least-squares fit within a moving window around each data point, one containing a fixed number of data points to the left $( n _ { L } )$ and right $\left( n _ { R } \right)$ . Because of the irregular spacing, however, there is no way to obtain universal filter coefficients applicable to more than one data point. One must instead do the actual least-squares fits for each data point. This becomes computationally burdensome for larger $n _ { L }$ , $n _ { R }$ , and $M$ .

As a cheap alternative, one can simply pretend that the data points are equally spaced. This amounts to virtually shifting, within each moving window, the data points to equally spaced positions. Such a shift introduces the equivalent of an additional source of noise into the function values. In those cases where smoothing is useful, this noise will often be much smaller than the noise already present. Specifically, if the location of the points is approximately random within the window, then a rough criterion is this: If the change in $f$ across the full width of the $N = n _ { L } + n _ { R } + 1$ point window is less than $\sqrt { N / 2 }$ times the measurement noise on a single point, then the cheap method can be used.

![](images/4f2d71f4cccd4b1fea9cd3e4d6cc4db68b18e025603076f684cb641d519c90b3.jpg)  
Figure 14.9.2. Result of applying wider 65-point Savitzky-Golay filters to the same data set as in Figure 14.9.1. Top: degree 2. Center: degree 4. Bottom: degree 6. All of these filters are inoptimally broad for the resolution of the narrow features. Higher-order filters do best at preserving feature heights and widths, but do less smoothing on broader features.

# CITED REFERENCES AND FURTHER READING:

Savitzky A., and Golay, M.J.E. 1964, “Smoothing and Differentiation of Data by Simplified Least Squares Procedures,” Analytical Chemistry, vol. 36, pp. 1627–1639.[1]   
Hamming, R.W. 1983, Digital Filters, 2nd ed. (Englewood Cliffs, NJ: Prentice-Hall).[2]   
Ziegler, H. 1981, “Properties of Digital Smoothing Polynomial (DISPO) Filters,” Applied Spectroscopy,vol.35, pp.88-92.[3]   
Bromba, M.U.A., and Ziegler, H. 1981, “Application Hints for Savitzky-Golay Digital Smoothing Filters,” Analytical Chemistry, vol. 53, pp. 1583–1586.[4]

# 15.0 Introduction

Given a set of observations, one often wants to condense and summarize the data by fitting it to a model that depends on adjustable parameters. Sometimes the model is simply a convenient class of functions, such as polynomials or Gaussians, and the fit supplies the appropriate coefficients. Other times, the model’s parameters come from some underlying theory that the data are supposed to satisfy; examples are rate coefficients in a complex network of chemical reactions or orbital elements of a binary star. Modeling can also be used as a kind of constrained interpolation, where you want to extend a few data points into a continuous function, but with some underlying idea of what that function should look like.

One very general approach has the following paradigm: You choose or design a figure-of-merit function (merit function, for short) that measures the agreement between the data and the model with a particular choice of parameters. In frequentist statistics, the merit function is conventionally arranged so that small values represent close agreement. Bayesians choose as their merit function the probability of the parameters given the data (or often its logarithm) so that larger values represent closer agreement.

In either case, the parameters of the model are then adjusted to find a happy extremum in the merit function, yielding best-fit parameters. The adjustment process is thus a problem in minimization in many dimensions. This optimization was the subject of Chapter 10; however, there exist special, more efficient, methods that are specific to modeling, and we will discuss these in this chapter.

There are important issues that go beyond the mere finding of best-fit parameters. Data are generally not exact. They are subject to measurement errors (called noise in the context of signal processing). Thus, typical data never exactly fit the model that is being used, even when that model is correct. We need the means to assess whether or not the model is appropriate, that is, we need to test the goodnessof-fit against some useful statistical standard.

We usually also need to know the accuracy with which parameters are determined by the data set. In frequentist terms, we need to know the standard errors of the best-fit parameters. Alternatively, in Bayesian language, we want to find not just the peak of the joint parameter probability distribution, but the whole distribution.

Or we at least want to be able to sample from that distribution, typically by Markov chain Monte Carlo, as we will discuss at length in $\ S 1 5 . 8$ .

It is not uncommon in fitting data to discover that the merit function is not unimodal, with a single minimum. In some cases, we may be interested in global rather than local questions. Not, “how good is this fit?” but rather, “how sure am I that there is not a very much better fit in some corner of parameter space?” As we have seen in Chapter 10, especially $\ S 1 0 . 1 2$ , this kind of problem is generally quite difficult to solve.

The important message is that fitting of parameters is not the end-all of model parameter estimation. To be genuinely useful, a fitting procedure should provide (i) parameters, (ii) error estimates on the parameters or a way to sample from their probability distribution, and (iii) a statistical measure of goodness-of-fit. When the third item suggests that the model is an unlikely match to the data, then items (i) and (ii) are probably worthless. Unfortunately, many practitioners of parameter estimation never proceed beyond item (i). They deem a fit acceptable if a graph of data and model “looks good.” This approach is known as chi-by-eye. Luckily, its practitioners get what they deserve.

# 15.0.1 Basic Bayes

Because the discussion in this and subsequent chapters will move freely between frequentist and Bayesian methods, this is a good place to compare these two powerfully useful ways of thinking. In $\ S 1 4 . 0$ , when we discussed tail, or $p$ -value, tests, we were adopting a frequentist viewpoint. The central frequentist idea is that, given the details of a null hypothesis, there is an implied population (that is, probability distribution) of possible data sets. If the assumed null hypothesis is correct, then the actual, measured, data set is drawn from that population. (We expand on this in $\ S 1 5 . 6 . )$ It then makes sense to ask questions about how “frequently” some aspect of the measured data occurs in the population. If the answer is “very infrequently,” then the hypothesis is rejected. The frequentist viewpoint avoids questions like, “what is the probability that this hypothesis is true?” because its focus is on the distribution of data sets, not hypotheses. Indeed, whether by dogma or merely benign neglect, it eschews the machinery needed to handle the concept of a probability distribution of hypotheses.

That machinery is Bayes’ theorem, which follows from the standard axioms of probability. Bayes’ theorem relates the conditional probabilities of two events, say $A$ and $B$ :

$$
P ( A | B ) = P ( A ) { \frac { P ( B | A ) } { P ( B ) } }
$$

Here $P ( A | B )$ is the probability of $A$ given that $B$ has occurred, and similarly for $P ( B | A )$ , while $P ( A )$ and $P ( B )$ are unconditional probabilities.

Bayesians allow a broader set of uses for probabilities than frequentists. To a Bayesian, $P ( A | B )$ is a measure of the degree of plausibility of $A$ (given $B$ ) on a scale ranging from zero to one. In this broader view, $A$ and $B$ need not be repeatable events; they can indeed be propositions or hypotheses. In equation (15.0.1), $A$ might be a hypothesis and $B$ might be some data, so that $P ( A | B )$ expresses the probability of a hypothesis, given the data. The equations of probability theory thus become a set of consistent rules for conducting inference [1,2]. Interestingly, this viewpoint was universal before the 20th century. The Bernoullis (both of them), Laplace, Gauss, Legendre, and Poisson, among others, made little or no distinction between inference and probability. An opposing frequentist view, that these concepts should be kept separate, became explicit only with the work of Fisher, Box, Kendall, Neyman, and Pearson (among others), much later.

Since plausibility is itself always conditioned on some, perhaps unarticulated, set of assumptions, all Bayesian probabilities are viewed as conditional on some collective background information $I$ . Suppose $H$ is some hypothesis. Even before there exist any explicit data, a Bayesian can assign to $H$ some degree of plausibility $P ( H | I )$ , called the “Bayesian prior.” Now, when some data $D _ { 1 }$ comes along, Bayes theorem tells how to reassess the plausibility of $H$ ,

$$
P ( H | D _ { 1 } I ) = P ( H | I ) \frac { P ( D _ { 1 } | H I ) } { P ( D _ { 1 } | I ) }
$$

The factor in the numerator on the right of equation (15.0.2) is calculable as the probability of a data set given the hypothesis (comparable to “likelihood” as we will define it in $\ S 1 5 . 1 \AA$ . The denominator, called the “prior predictive probability” of the data, is in this case merely a normalization constant that can be calculated by the requirement that the probability of all hypotheses should sum to unity. (In other Bayesian contexts, the prior predictive probabilities of two qualitatively different models can be used to assess their relative plausibility.)

If some additional data $D _ { 2 }$ come along tomorrow, we can further refine our estimate of $H$ ’s probability, as

$$
P ( H | D _ { 2 } D _ { 1 } I ) = P ( H | D _ { 1 } I ) \frac { P ( D _ { 2 } | H D _ { 1 } I ) } { P ( D _ { 2 } | D _ { 1 } I ) }
$$

Using the product rule for probabilities, $P ( A B | C ) = P ( A | C ) P ( B | A C )$ , we find that equations (15.0.2) and (15.0.3) imply

$$
P ( H | D _ { 2 } D _ { 1 } I ) = P ( H | I ) \frac { P ( D _ { 2 } D _ { 1 } | H I ) } { P ( D _ { 2 } D _ { 1 } | I ) }
$$

which shows that we would have gotten the same answer if all the data $D _ { 1 } D _ { 2 }$ had been taken together.

We might wonder, before we adopt the laws of probability as our calculus of inference and thus become Bayesians, whether there are any other alternatives. The answer is, basically, no. Cox [3] showed that making a small number of very reasonable assumptions about “degree of belief” leads inevitably to the axioms of probability, and thus the application of Bayes theorem to the evaluation of hypotheses, given data. Either you become a Bayesian or else you must live in a world with no general calculus of inference.

# CITED REFERENCES AND FURTHER READING:

Bevington, P.R., and Robinson, D.K. 2002, Data Reduction and Error Analysis for the Physical Sciences, 3rd ed. (New York: McGraw-Hil), Chapters 6-11.   
Devore, J.L. 2003, Probability and Statistics for Engineering and the Sciences, 6th ed. (Belmont, CA: Duxbury Press), Chapters 12–13.   
Brownlee, K.A. 1965, Statistical Theory and Methodology, 2nd ed. (New York: Wiley).   
Martin, B.R. 1971, Statistics for Physicists (New York: Academic Press).   
Gelman, A., Carlin, J.B., Stern, H.S., and Rubin, D.B. 2004, Bayesian Data Analysis, 2nd ed. (Boca Raton, FL: Chapman & Hall/CRC).   
Sivia, D.S. 1996, Data Analysis: A Bayesian Tutorial (Oxford, UK: Oxford University Press).   
Jaynes, E.T. 1976, in Foundations of Probability Theory Statistical Inference and Statistical Theories of Science,W.L. Harper and C.A. Hooker, eds. (Dordrecht: Reidel).[1]   
Jaynes, E.T. 1985, in Maximum-Entropy and Bayesian Methods in Inverse Problems, C.R. Smith and W.T. Grandy, Jr., eds. (Dordrecht: Reidel).[2]   
Cox, R.T. 1946, “Probability, Frequency, and Reasonable Expectation,” American Journal of Physics,vol.14,pp.1-13.[3]

# 15.1 Least Squares as a Maximum Likelihood Estimator

Suppose that we are fitting $N$ data points $( x _ { i } , y _ { i } ) , i = 0 , \dots , N - 1$ , to a model that has $M$ adjustable parameters $a _ { j }$ , $j = 0 , \ldots , M - 1$ . The model predicts a functional relationship between the measured independent and dependent variables,

$$
y ( x ) = y ( x | a _ { 0 } \dots a _ { M - 1 } )
$$

where the notation indicates dependence on the parameters explicitly on the righthand side, following the vertical bar.

What, exactly, do we want to minimize to get fitted values for the $a _ { j }$ ’s? The first thing that comes to mind is the familiar least-squares fit,

$$
\mathrm { m i n i m i z e ~ o v e r ~ } a _ { 0 } \ldots a _ { M - 1 } : \qquad \sum _ { i = 0 } ^ { N - 1 } \left[ y _ { i } - y ( x _ { i } | a _ { 0 } \ldots a _ { M - 1 } ) \right] ^ { 2 }
$$

But where does this come from? What general principles is it based on?

To answer these questions, let us start by asking, “Given a particular set of parameters, what is the probability that the observed data set should have occurred?” If the $y _ { i }$ ’s take on continuous values, the probability will always be zero unless we add the phrase, “. . . plus or minus some small, fixed $\Delta y$ on each data point.” So let’s always take this phrase as understood. If the probability of obtaining the data set is too small, then we can conclude that the parameters under consideration are “unlikely” to be right. Conversely, our intuition tells us that the data set should not be too improbable for the correct choice of parameters.

To be more quantitative, suppose that each data point $y _ { i }$ has a measurement error that is independently random and distributed as a normal (Gaussian) distribution around the “true” model $y ( x )$ . And suppose that the standard deviations $\sigma$ of these normal distributions are the same for all points. Then the probability of the data set is the product of the probabilities of each point:

$$
P ( \mathrm { d a t a } \mid \mathrm { m o d e l } ) \propto \prod _ { i = 0 } ^ { N - 1 } \left\{ \exp \left[ - \frac { 1 } { 2 } \bigg ( \frac { y _ { i } - y ( x _ { i } ) } { \sigma } \bigg ) ^ { 2 } \right] \Delta y \right\}
$$

Notice that there is a factor $\Delta y$ in each term in the product.

If we are Bayesians, we proceed by invoking Bayes’ theorem, in the form

$$
P ( { \mathrm { m o d e l } } \mid { \mathrm { d a t a } } ) \propto P ( { \mathrm { d a t a } } \mid { \mathrm { m o d e l } } ) P ( { \mathrm { m o d e l } } )
$$

where $P ( { \mathrm { m o d e l } } ) = P ( a _ { 0 } \dots a _ { M - 1 } )$ is our prior probability distribution on all models. As often as not, we take a constant, noninformative prior. The most probable model, then, is the one that maximizes equation (15.1.3) or, equivalently, minimizes the negative of its logarithm,

$$
\left[ \sum _ { i = 0 } ^ { N - 1 } \frac { [ y _ { i } - y ( x _ { i } ) ] ^ { 2 } } { 2 \sigma ^ { 2 } } \right] - N \log \Delta y
$$

Since $N , \sigma$ , and $\Delta y$ are all constants, minimizing this equation is equivalent to minimizing (15.1.2).

If we are frequentists, we must get to the same destination by a more tortuous path (as is so often the case when Bayesian and frequentist methods coincide). We are not allowed to think about the notion of probability as applied to parameter sets, because, for frequentists, there is no statistical universe of models from which the parameters are drawn. We instead substitute a dictum: We identify the probability of the data given the parameters (which is computable as above), as the likelihood of the parameters given the data. This identification is entirely based on intuition. It has no formal mathematical basis in and of itself. Parameters derived in this way are called maximum likelihood estimators.

What we see is that least-squares fitting gives an answer that is both (i) the most probable parameter set in the Bayesian sense, assuming a flat prior, and (ii) the maximum likelihood estimate of the fitted parameters, in both cases $i f$ the measurement errors are independent and normally distributed with constant standard deviation. Notice that we made no assumption about the linearity or nonlinearity of the model $y ( x | a _ { 0 } \ldots )$ in its parameters $a _ { 0 } \dots a _ { M - 1 }$ . Just below, we will relax our assumption of constant standard deviations and obtain the very similar formulas for what is called “chi-square fitting” or “weighted least-squares fitting.” First, however, let us discuss further our very stringent assumption of a normal distribution.

For a hundred years or so, mathematical statisticians have been in love with the fact that the probability distribution of the sum of a very large number of very small random deviations almost always converges to a normal distribution. (For precise statements of this central limit theorem, consult [1] or other standard works on mathematical statistics.) This infatuation tended to focus interest away from the fact that, for real data, the normal distribution is often rather poorly realized, if it is realized at all. We are often taught, rather casually, that, on average, measurements will fall within $\pm \sigma$ of the true value $68 \%$ of the time, within $\pm 2 \sigma 9 5 \%$ of the time, and within $\pm 3 \sigma 9 9 . 7 \%$ of the time. Extending this, one would expect a measurement to be off by $\pm 2 0 \sigma$ only one time out of $2 \times 1 0 ^ { 8 8 }$ . We all know that “glitches” are much more likely than that!

In some instances, the deviations from a normal distribution are easy to understand and quantify. For example, in measurements obtained by counting events, the measurement errors are usually distributed as a Poisson distribution, whose cumulative probability function was already discussed in $\ S 6 . 2$ . When the number of counts going into one data point is large, the Poisson distribution converges toward a Gaussian. However, the convergence is not uniform when measured in fractional accuracy. The more standard deviations out on the tail of the distribution, the larger the number of counts must be before a value close to the Gaussian is realized. The sign of the effect is always the same: The Gaussian predicts that “tail” events are much less likely than they actually (by Poisson) are. This causes such events, when they occur, to skew a least-squares fit much more than they ought.

Other times, the deviations from a normal distribution are not so easy to understand in detail. Experimental points are occasionally just way off. Perhaps the power flickered during a point’s measurement, or someone kicked the apparatus, or someone wrote down a wrong number. Points like this are called outliers. They can easily turn a least-squares fit on otherwise adequate data into nonsense. Their probability of occurrence in the assumed Gaussian model is so small that the maximum likelihood estimator is willing to distort the whole curve to try to bring them, mistakenly, into line.

The subject of robust statistics deals with cases where the normal or Gaussian model is a bad approximation, or cases where outliers are important. We will discuss robust methods briefly in $\ S 1 5 . 7$ . All the sections between this one and that one assume, one way or the other, a Gaussian model for the measurement errors in the data. It it quite important that you keep the limitations of that model in mind, even as you use the very useful methods that follow from assuming it.

Finally, note that our discussion of measurement errors has been limited to statistical errors, the kind that will average away if we only take enough data. Measurements are also susceptible to systematic errors that will not go away with any amount of averaging. For example, the calibration of a metal meter stick might depend on its temperature. If we take all our measurements at the same wrong temperature, then no amount of averaging or numerical processing will correct for this unrecognized systematic error.

# 15.1.1 Chi-Square Fitting

We considered the chi-square statistic once before, in $\ S 1 4 . 3$ . Here it arises in a slightly different context.

If each data point $( x _ { i } , y _ { i } )$ has its own, known standard deviation $\sigma _ { i }$ , then equation (15.1.3) is modified only by putting a subscript $i$ on the symbol $\sigma$ . That subscript also propagates docilely into (15.1.5), so that the maximum likelihood estimate of the model parameters (and also the Bayesian most probable parameter set) is obtained by minimizing the quantity

$$
\chi ^ { 2 } \equiv \sum _ { i = 0 } ^ { N - 1 } \left( \frac { y _ { i } - y ( x _ { i } | a _ { 0 } \ldots a _ { M - 1 } ) } { \sigma _ { i } } \right) ^ { 2 }
$$

called the “chi-square.”

To whatever extent the measurement errors actually are normally distributed, the quantity $\chi ^ { 2 }$ is correspondingly a sum of $N$ squares of normally distributed quantities, each normalized to unit variance. Once we have adjusted the $a _ { 0 } \dots a _ { M - 1 }$ to minimize the value of $\chi ^ { 2 }$ , the terms in the sum are not all statistically independent. For models that are linear in the $a$ ’s, however, it turns out that the probability distribution for different values of $\chi ^ { 2 }$ at its minimum can nevertheless be derived analytically, and is the chi-square distribution for $N - M$ degrees of freedom. We learned how to compute this probability function using the incomplete gamma function in $\ S 6 . 2$ . In particular, equation (6.14.39) gives the probability $Q$ that the chisquare should exceed a particular value $\chi ^ { 2 }$ by chance, where $\nu = N - M$ is the number of degrees of freedom. The quantity $Q$ , or its complement $P \equiv 1 - Q$ , is frequently tabulated in appendices to statistics books, or it can be computed as $P = { \tt C h i s q d i s t } ( \nu )$ .invcdf $( \chi ^ { 2 } )$ by the routine in $\ S 6 . 1 4 . 8$ . It is quite common, and usually not too wrong, to assume that the chi-square distribution holds even for models that are not strictly linear in the $a$ ’s.

This computed probability gives a quantitative measure for the goodness-of-fit of the model. If $Q$ is a very small probability for some particular data set, then the apparent discrepancies are unlikely to be chance fluctuations. Much more probably either (i) the model is wrong — can be statistically rejected, or (ii) someone has lied to you about the size of the measurement errors $\sigma _ { i }$ — they are really larger than stated.

While above we were quick to poke fun at the frequentist’s foundations for maximum likelihood estimation (or lack thereof), we must now take aim at strict Bayesians: There are no good fully Bayesian methods for assessing goodness-offit, that is, for comparing the probability of a best-fit model to that of a nonspecific alternative hypothesis like “the model is wrong.” The problem is that the strict application of Bayes theorem requires either (i) a comparison between two well-posed hypotheses (the odds ratio), or (ii) a normalization of the probability of the best-fit model against an integral of such probabilities over all possible models (the normalizing constant). In most situations neither of these is available. Sensible Bayesians usually fall back to $p$ -value tail statistics like chi-square probability when they really need to know if a model is wrong.

Another important point is that the chi-square probability $Q$ does not directly measure the credibility of the assumption that the measurement errors are normally distributed. It assumes they are. In most, but not all, cases, however, the effect of nonnormal errors is to create an abundance of outlier points. These decrease the probability $Q$ , so that we can add another possible, though less definitive, conclusion to the above list: (iii) the measurement errors may not be normally distributed.

Possibility (iii) is fairly common, and also fairly benign. It is for this reason that reasonable experimenters are often rather tolerant of low probabilities $Q$ . It is not uncommon to deem acceptable on equal terms any models with, say, $Q > 0 . 0 0 1$ . This is not as sloppy as it sounds: Truly wrong models will often be rejected with vastly smaller values of $Q$ , $1 0 ^ { - 1 8 }$ , say. However, if day-in and day-out you find yourself accepting models with $Q \sim 1 0 ^ { - 3 }$ , you really should track down the cause.

If you happen to know the actual distribution law of your measurement errors, then you might wish to Monte Carlo simulate some data sets drawn from a particular model, cf. $\ S 7 . 3 - \ S 7 . 4$ . You can then subject these synthetic data sets to your actual fitting procedure, so as to determine both the probability distribution of the $\chi ^ { 2 }$ statistic and also the accuracy with which your model parameters are reproduced by the fit. We discuss this further in $\ S 1 5 . 6$ . The technique is very general, but it can also be slow.

At the opposite extreme, it sometimes happens that the probability $Q$ is too large, too near to 1, literally too good to be true! Nonnormal measurement errors cannot in general produce this disease, since the normal distribution is about as “compact” as a distribution can be. Almost always, the cause of too good a chisquare fit is that the experimenter, in a “fit” of conservativism, has overestimated his or her measurement errors. Very rarely, too good a chi-square signals actual fraud, data that have been “fudged” to fit the model.

A rule of thumb is that a “typical” value of $\chi ^ { 2 }$ for a “moderately” good fit is $\chi ^ { 2 } \approx \nu$ . More precise is the statement that the $\chi ^ { 2 }$ statistic has a mean $\nu$ and a standard deviation $\sqrt { 2 \nu }$ and, asymptotically for large $\nu$ , becomes normally distributed.

In some cases the uncertainties associated with a set of measurements are not known in advance, and considerations related to $\chi ^ { 2 }$ fitting are used to derive a value for $\sigma$ . If we assume that all measurements have the same standard deviation, $\sigma _ { i } = \sigma$ , and that the model does fit well, then we can proceed by first assigning an arbitrary constant $\sigma$ to all points, next fitting for the model parameters by minimizing $\chi ^ { 2 }$ , and finally recomputing

$$
\sigma ^ { 2 } = \sum _ { i = 0 } ^ { N - 1 } [ y _ { i } - y ( x _ { i } ) ] ^ { 2 } / ( N - M )
$$

Obviously, this approach prohibits an independent assessment of goodness-of-fit, a fact occasionally missed by its adherents. When, however, the measurement error is not known, this approach at least allows some kind of error bar to be assigned to the points.

If we take the derivative of equation (15.1.6) with respect to the parameters $a _ { k }$ we obtain equations that must hold at the chi-square minimum:

$$
0 = \sum _ { i = 0 } ^ { N - 1 } \left( { \frac { y _ { i } - y \left( x _ { i } \right) } { \sigma _ { i } ^ { 2 } } } \right) \left( { \frac { \partial y \left( x _ { i } | \ldots a _ { k } \ldots \right) } { \partial a _ { k } } } \right) \qquad k = 0 , \ldots , M - 1
$$

Equation (15.1.8) is, in general, a set of $M$ nonlinear equations for the $M$ unknown $a _ { k }$ . Various of the procedures described subsequently in this chapter derive from (15.1.8) and its specializations.

# CITED REFERENCES AND FURTHER READING:

Lupton, R. 1993, Statistics in Theory and Practice (Princeton, NJ: Princeton University Press), Chapters 10–11.[1]   
Devore, J.L. 2003, Probability and Statistics for Engineering and the Sciences, 6th ed. (Belmont, CA: Duxbury Press), Chapter 6.   
Gelman, A., Carlin, J.B., Stern, H.S., and Rubin, D.B. 2004, Bayesian Data Analysis, 2nd ed. (Boca Raton, FL: Chapman & Hall/CRC), Chapter 8.

# 15.2 Fitting Data to a Straight Line

A concrete example will make the considerations of the previous section more meaningful. We consider the problem of fitting a set of $N$ data points $( x _ { i } , y _ { i } )$ to a straight-line model

$$
y ( x ) = y ( x | a , b ) = a + b x
$$

This problem is often called linear regression, a terminology that originated, long ago, in the social sciences. We assume that the uncertainty $\sigma _ { i }$ associated with each

measurement $y _ { i }$ is known, and that the $x _ { i }$ ’s (values of the dependent variable) are known exactly.

To measure how well the model agrees with the data, we use the chi-square merit function (15.1.6), which in this case is

$$
\chi ^ { 2 } ( a , b ) = \sum _ { i = 0 } ^ { N - 1 } \left( \frac { y _ { i } - a - b x _ { i } } { \sigma _ { i } } \right) ^ { 2 }
$$

If the measurement errors are normally distributed, then this merit function will give maximum likelihood parameter estimations of $a$ and $b$ ; if the errors are not normally distributed, then the estimations are not maximum likelihood but may still be useful in a practical sense. In $\ S 1 5 . 7$ , we will treat the case where outlier points are so numerous as to render the $\chi ^ { 2 }$ merit function useless.

Equation (15.2.2) is minimized to determine $a$ and $b$ . At its minimum, derivatives of $\chi ^ { 2 } ( a , b )$ with respect to $a , b$ vanish:

$$
\begin{array} { l } { \displaystyle 0 = \frac { \partial \chi ^ { 2 } } { \partial a } = - 2 \sum _ { i = 0 } ^ { N - 1 } \frac { y _ { i } - a - b x _ { i } } { \sigma _ { i } ^ { 2 } } } \\ { \displaystyle 0 = \frac { \partial \chi ^ { 2 } } { \partial b } = - 2 \sum _ { i = 0 } ^ { N - 1 } \frac { x _ { i } \left( y _ { i } - a - b x _ { i } \right) } { \sigma _ { i } ^ { 2 } } } \end{array}
$$

These conditions can be rewritten in a convenient form if we define the following sums:

$$
{ \begin{array} { r l } { S \equiv \displaystyle \sum _ { i = 0 } ^ { N - 1 } { \frac { 1 } { \sigma _ { i } ^ { 2 } } } } & { S _ { x } \equiv \displaystyle \sum _ { i = 0 } ^ { N - 1 } { \frac { x _ { i } } { \sigma _ { i } ^ { 2 } } } \quad S _ { y } \equiv \displaystyle \sum _ { i = 0 } ^ { N - 1 } { \frac { y _ { i } } { \sigma _ { i } ^ { 2 } } } } \\ { S _ { x x } \equiv \displaystyle \sum _ { i = 0 } ^ { N - 1 } { \frac { x _ { i } ^ { 2 } } { \sigma _ { i } ^ { 2 } } } } & { S _ { x y } \equiv \displaystyle \sum _ { i = 0 } ^ { N - 1 } { \frac { x _ { i } y _ { i } } { \sigma _ { i } ^ { 2 } } } } \end{array} }
$$

With these definitions (15.2.3) becomes

$$
\begin{array} { c } { { a S + b S _ { x } = S _ { y } } } \\ { { a S _ { x } + b S _ { x x } = S _ { x y } } } \end{array}
$$

The solution of these two equations in two unknowns is calculated as

$$
\begin{array} { l } { \Delta \equiv S S _ { x x } - ( S _ { x } ) ^ { 2 } } \\ { a = \frac { S _ { x x } S _ { y } - S _ { x } S _ { x y } } { \Delta } } \\ { b = \frac { S S _ { x y } - S _ { x } S _ { y } } { \Delta } } \end{array}
$$

Equation (15.2.6) gives the solution for the best-fit model parameters $a$ and $b$ .

We are not done, however. We must estimate the probable uncertainties in the estimates of $a$ and $b$ , since obviously the measurement errors in the data must introduce some uncertainty in the determination of those parameters. If the data are

independent, then each contributes its own bit of uncertainty to the parameters. Consideration of propagation of errors shows that the variance $\sigma _ { f } ^ { 2 }$ in the value of any function will be

$$
\sigma _ { f } ^ { 2 } = \sum _ { i = 0 } ^ { N - 1 } \sigma _ { i } ^ { 2 } \left( \frac { \partial f } { \partial y _ { i } } \right) ^ { 2 }
$$

For the straight line, the derivatives of $a$ and $b$ with respect to $y _ { i }$ can be directly evaluated from the solution:

$$
\begin{array} { r l r } & { \frac { \partial a } { \partial y _ { i } } = \frac { S _ { x x } - S _ { x } x _ { i } } { \sigma _ { i } ^ { 2 } \Delta } } & \\ & { \frac { \partial b } { \partial y _ { i } } = \frac { S x _ { i } - S _ { x } } { \sigma _ { i } ^ { 2 } \Delta } } & \end{array}
$$

Summing over the points as in (15.2.7), we get

$$
\begin{array} { l } { \sigma _ { a } ^ { 2 } = S _ { x x } / \Delta } \\ { \sigma _ { b } ^ { 2 } = S / \Delta } \end{array}
$$

which are the variances in the estimates of $a$ and $b$ , respectively. We will see in $\ S 1 5 . 6$ that an additional number is also needed to characterize properly the probable uncertainty of the parameter estimation. That number is the covariance of $a$ and $b$ , and (as we will see below) is given by

$$
\mathrm { C o v } ( a , b ) = - S _ { x } / \Delta
$$

The coefficient of correlation between the uncertainty in $a$ and the uncertainty in $b$ , which is a number between $^ { - 1 }$ and 1, follows from (15.2.10) (compare equation 14.5.1),

$$
r _ { a b } = \frac { - S _ { x } } { \sqrt { S S _ { x x } } }
$$

A positive value of $r _ { a b }$ indicates that the errors in $a$ and $b$ are likely to have the same sign, while a negative value indicates the errors are anticorrelated, likely to have opposite signs.

We are still not done. We must estimate the goodness-of-fit of the data to the model. Absent this estimate, we have not the slightest indication that the parameters $a$ and $b$ in the model have any meaning at all! The probability $Q$ that a value of chi-square as poor as the value (15.2.2) should occur by chance is

$$
\mathcal { Q } = 1 - \mathrm { c h i s q d i s t } ( N - 2 ) . \mathrm { i n v c d f } ( \chi ^ { 2 } )
$$

Here Chisqdist is our object embodying the chi-square distribution function (see $\ S 6 . 1 4 . 8 )$ and invcdf is its inverse cumulative distribution function. If $Q$ is larger than, say, 0:1, then the goodness-of-fit is believable. If it is larger than, say, 0:001, then the fit may be acceptable if the errors are nonnormal or have been moderately underestimated. If $Q$ is less than 0:001, then the model and/or estimation procedure can rightly be called into question. In this latter case, turn to $\ S 1 5 . 7$ to proceed further.

If you do not know the individual measurement errors of the points $\sigma _ { i }$ , and are proceeding (dangerously) to use equation (15.1.7) for estimating these errors, then here is the procedure for estimating the probable uncertainties of the parameters $a$ and $b$ : Set $\sigma _ { i } \equiv 1$ in all equations through (15.2.6), and multiply $\sigma _ { a }$ and $\sigma _ { b }$ , as obtained from equation (15.2.9), by the additional factor $\sqrt { \chi ^ { 2 } / ( N - 2 ) }$ , where $\chi ^ { 2 }$ is computed by (15.2.2) using the fitted parameters $a$ and $b$ . As discussed above, this procedure is equivalent to assuming a good fit, so you get no independent goodnessof-fit probability $Q$ .

In $\ S 1 4 . 5$ we promised a relation between the linear correlation coefficient $r$ (equation 14.5.1) and a goodness-of-fit measure, $\chi ^ { 2 }$ (equation 15.2.2). For unweighted data (all $\sigma _ { i } = 1$ ), that relation is

$$
\chi ^ { 2 } = ( 1 - r ^ { 2 } ) \sum _ { i = 0 } ^ { N - 1 } ( y _ { i } - \overline { { y } } ) ^ { 2 }
$$

For data with varying errors $\sigma _ { i }$ , the above equations remain valid if the sums in equations (15.2.13) and (14.5.1) are weighted by $1 / \sigma _ { i } ^ { 2 }$ .

The following object, Fitab, carries out exactly the operations that we have discussed. You call its constructor either with, or without, errors $\sigma _ { i }$ . If the $\sigma _ { i }$ ’s are known, the calculations exactly correspond to the formulas above. However, when $\sigma _ { i }$ ’s are unavailable, the routine assumes equal values of $\sigma$ for each point and assumes a good fit, as discussed in $\ S 1 5 . 1$ .

The formulas (15.2.6) are susceptible to roundoff error. Accordingly, we rewrite them as follows: Define

$$
t _ { i } = \frac { 1 } { \sigma _ { i } } \left( x _ { i } - \frac { S _ { x } } { S } \right) , \qquad i = 0 , 1 , \dots , N - 1
$$

and

$$
S _ { t t } = \sum _ { i = 0 } ^ { N - 1 } t _ { i } ^ { 2 }
$$

Then, as you can verify by direct substitution,

$$
\begin{array} { c } { { b = \displaystyle \frac { 1 } { S _ { t t } } \sum _ { i = 0 } ^ { N - 1 } \frac { i \beta y _ { i } } { \sigma _ { i } } } } \\ { { \ } } \\ { { a = \displaystyle \frac { S _ { y } - S _ { x } b } { S } } } \\ { { \sigma _ { a } ^ { 2 } = \displaystyle \frac { 1 } { S } \left( 1 + \frac { S _ { x } ^ { 2 } } { S S _ { t t } } \right) } } \\ { { \sigma _ { b } ^ { 2 } = \displaystyle \frac { 1 } { S _ { t t } } \sum _ { i \neq i } ^ { N } } } \\ { { \mathrm { C o v } ( a , b ) = - \frac { S _ { x } } { S S _ { t t } } } } \\ { { \ } } \\ { { r _ { a b } = \displaystyle \frac { \mathrm { C o v } ( a , b ) } { \sigma _ { a } \sigma _ { b } } } } \end{array}
$$

# struct Fitab {

Object for fitting a straight line $y = a + b x$ to a set of points $( x _ { i } , y _ { i } )$ , with or without available errors $\sigma _ { i }$ . Call one of the two constructors to calculate the fit. The answers are then available as the variables a, b, siga, sigb, chi2, and either q or sigdat.

Int ndata;   
Doub a, b, siga, sigb, chi2, q, sigdat; Answers.   
VecDoub_I &x, &y, &sig;

# Fitab(VecDoub_I &xx, VecDoub_I &yy, VecDoub_I &ssig)

: ndata(xx.size()), $\mathbf { x } \left( \mathbf { x x } \right)$ , y(yy), sig(ssig), chi2(0.), q(1.), sigdat(0.) { Constructor. Given a set of data points x[0..ndata-1], y[0..ndata-1] with individual standard deviations sig[0..ndata-1], sets a,b and their respective probable uncertainties siga and sigb, the chi-square chi2, and the goodness-of-fit probability q (that the fit would have $\chi ^ { 2 }$ this large or larger).

Gamma gam;   
Int i;   
Doub ss ${ = } 0$ .,sx $_ { = 0 }$ .,sy ${ \tt = } 0$ .,st2=0.,t,wt,sxoss;   
$\mathtt { b } = 0 . 0$ ; Accumulate sums ...   
for (i=0;i<ndata;i++) { wt=1.0/SQR(sig[i]); ...with weights ss $+ =$ wt; sx += x[i]\*wt; sy $+ =$ y[i]\*wt;   
}   
sxoss=sx/ss;   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<ndata;i++) { $\mathtt { t } =$ (x[i]-sxoss)/sig[i]; st2 $+ =$ t\*t; b $+ =$ t\*y[i]/sig[i];   
}   
b /= st2; Solve for $a , b , \sigma _ { a }$ , and $\sigma _ { b }$ .   
$\mathtt { a } =$ (sy-sx\*b)/ss;   
siga=sqrt((1.0+sx\*sx/(ss\*st2))/ss);   
sigb sqrt(1.0/st2); Calculate $\chi ^ { 2 }$ .   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<ndata; $\dot { \bf 1 } + +$ ) chi2 $+ =$ SQR((y[i]-a-b\*x[i])/sig[i]);   
if (ndata>2) q=gam.gammq(0. $^ { 5 \ast }$ (ndata-2),0.5\*chi2); Equation (15.2.12

# Fitab(VecDoub_I &xx, VecDoub_I &yy)

: ndata(xx.size()), x(xx), y(yy), sig(xx), chi2(0.), q(1.), sigdat(0.) { Constructor. As above, but without known errors (sig is not used). The uncertainties siga and sigb are estimated by assuming equal errors for all points, and that a straight line is a good fit. q is returned as 1.0, the normalization of chi2 is to unit standard deviation on all points, and sigdat is set to the estimated error of each point.

Int i;   
Doub ss,sx $_ { = 0 }$ .,sy=0.,st2=0.,t,sxoss;   
$\mathtt { b } = 0 \ , \ 0$ ; Accumulate sums ...   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<ndata;i++) { sx $+ = \textbf { x } [ \mathrm { i } ]$ ; ...without weights. sy $+ = \texttt { y } [ \texttt { i } ]$ ;   
}   
ss=ndata;   
sxoss $=$ sx/ss;   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<ndata;i++) { $\mathtt { t } = \mathtt { x }$ [i]-sxoss; st2 $+ =$ t\*t; b $+ =$ t\*y[i];   
}   
b /= st2; Solve for $a , b , \sigma _ { a }$ , and $\sigma _ { b }$ .   
$\mathtt { a } =$ (sy-sx\*b)/ss;   
siga=sqrt((1.0+sx\*sx/(ss\*st2))/ss);   
sigb=sqrt(1.0/st2); Calculate $\chi ^ { 2 }$ .   
for (i=0;i<ndata;i++) chi2 $+ =$ SQR(y[i]-a-b\*x[i]);

if (ndata $> ~ 2 )$ sigdat ${ } = { }$ sqrt(chi2/(ndata-2)); siga $\ast =$ sigdat; sigb $\ast =$ sigdat; } };

For unweighted data evaluate typical sig using chi2, and adjust the standard deviations.

# CITED REFERENCES AND FURTHER READING:

Bevington, P.R., and Robinson, D.K. 2002, Data Reduction and Error Analysis for the Physical Sciences, 3rd ed. (New York: McGraw-Hil), Chapter 6.   
Devore, J.L. 2003, Probability and Statistics for Engineering and the Sciences, 6th ed. (Belmont, CA: Duxbury Press), Chapter 12.

# 15.3 Straight-Line Data with Errors in Both Coordinates

If experimental data are subject to measurement error not only in the $y _ { i }$ ’s, but also in the $x _ { i }$ ’s, then the task of fitting a straight-line model

$$
y ( x ) = a + b x
$$

is considerably harder. It is straightforward to write down the $\chi ^ { 2 }$ merit function for this case,

$$
\chi ^ { 2 } ( a , b ) = \sum _ { i = 0 } ^ { N - 1 } \frac { ( y _ { i } - a - b x _ { i } ) ^ { 2 } } { \sigma _ { y i } ^ { 2 } + b ^ { 2 } \sigma _ { x i } ^ { 2 } }
$$

where $\sigma _ { x i }$ and $\sigma _ { y i }$ are, respectively, the $x$ and $y$ standard deviations for the $i$ th point. The weighted sum of variances in the denominator of equation (15.3.2) can be understood both as the variance in the direction of the smallest $\chi ^ { 2 }$ between each data point and the line with slope $b$ , and also as the variance of the linear combination $y _ { i } - a - b x _ { i }$ of two random variables $x _ { i }$ and $y _ { i }$ ,

$$
\operatorname { V a r } ( y _ { i } - a - b x _ { i } ) = \operatorname { V a r } ( y _ { i } ) + b ^ { 2 } \operatorname { V a r } ( x _ { i } ) = \sigma _ { y _ { i } } ^ { 2 } + b ^ { 2 } \sigma _ { x { i } } ^ { 2 } \equiv 1 / w _ { i }
$$

The sum of the square of $N$ random variables, each normalized by its variance, is thus chisquare distributed.

We want to minimize equation (15.3.2) with respect to $a$ and $b$ . Unfortunately, the occurrence of $b$ in the denominator of equation (15.3.2) makes the resulting equation for the slope $\partial \chi ^ { 2 } / \partial b = 0$ nonlinear. However, the corresponding condition for the intercept, $\partial \chi ^ { 2 } / \partial \stackrel { \star } { a } = \stackrel {  } { 0 }$ , is still linear and yields

$$
a = \left[ \sum _ { i } w _ { i } ( y _ { i } - b x _ { i } ) \right] \bigg / \sum _ { i } w _ { i }
$$

where the $w _ { i }$ ’s are defined by equation (15.3.3). A reasonable strategy, now, is to use the machinery of Chapter 10 (e.g., a Brent object) for minimizing a general one-dimensional function to minimize with respect to $b$ while using equation (15.3.4) at each stage to ensure that the minimum with respect to $b$ is also minimized with respect to $a$ .

Because of the finite error bars on the $x _ { i }$ ’s, the minimum $\chi ^ { 2 }$ as a function of $b$ will be finite, though usually large, when $b$ equals infinity (line of infinite slope). The angle $\theta \equiv$

![](images/d2a1f7365d67bab9713ea28336330ac9d2c4afbcc3ddc6971687086f0f92c250.jpg)  
Figure 15.3.1. Standard errors for the parameters $^ { a }$ and $^ { b }$ . The point $B$ can be found by varying the slope $^ { b }$ while simultaneously minimizing the intercept $^ { a }$ . This gives the standard error $\sigma _ { b }$ and also the value $s$ . The standard error $\sigma _ { a }$ can then be found by the geometric relation $\sigma _ { a } ^ { 2 } = s ^ { 2 } + r ^ { 2 }$ .

arctan $b$ is thus more suitable as a parametrization of slope than $b$ itself. The value of $\chi ^ { 2 }$ will then be periodic in $\theta$ with period $\pi$ (not $2 \pi !$ ). If any data points have very small $\sigma _ { y }$ ’s but moderate or large $\sigma _ { x }$ ’s, then it is also possible to have a maximum in $\chi ^ { 2 }$ near zero slope, $\theta \approx 0$ . In that case, there can sometimes be two $\chi ^ { 2 }$ minima, one at positive slope and the other at negative. Only one of these is the correct global minimum. It is therefore important to have a good starting guess for $b$ (or $\theta$ ). Our strategy, implemented below, is to scale the $y _ { i }$ ’s so as to have variance equal to the with weights derived from the (sca $x _ { i }$ ’s, an) sum a conventional (as in . This yields a good s $\ S 1 5 . 2 )$ linear fit guess for $\sigma _ { y i } ^ { 2 } + \sigma _ { x i } ^ { 2 }$   
$b$ if the data are even plausibly related to a straight-line model.

Finding the standard errors $\sigma _ { a }$ and $\sigma _ { b }$ on the parameters $a$ and $b$ is more complicated. We will see in $\ S 1 5 . 6$ that, in appropriate circumstances, the standard errors in $a$ and $b$ are the respective projections onto the $a$ - and $b$ -axes of the “confidence region boundary” where $\chi ^ { 2 }$ takes on a value one greater than its minimum, $\Delta \chi ^ { 2 } = 1$ . In the linear case of $\ S 1 5 . 2$ , these projections follow from the Taylor series expansion

$$
\Delta \chi ^ { 2 } \approx \frac { 1 } { 2 } \left[ \frac { \partial ^ { 2 } \chi ^ { 2 } } { \partial a ^ { 2 } } ( \Delta a ) ^ { 2 } + \frac { \partial ^ { 2 } \chi ^ { 2 } } { \partial b ^ { 2 } } ( \Delta b ) ^ { 2 } \right] + \frac { \partial ^ { 2 } \chi ^ { 2 } } { \partial a \partial b } \Delta a \Delta b
$$

Because of the present nonlinearity in $b$ , however, analytic formulas for the second derivatives are quite unwieldy; more important, the lowest-order term frequently gives a poor approximation to $\Delta \chi ^ { 2 }$ . Our strategy is therefore to find the roots of $\Delta \chi ^ { 2 } = 1$ numerically, by adjusting the value of the slope $b$ away from the minimum. In the program below, the general root finder zbrent is used. It may occur that there are no roots at all — for example, if all error bars are so large that all the data points are compatible with each other. It is important, therefore, to make some effort at bracketing a putative root before refining it (cf. $\ S 9 . 1 )$ .

Because $a$ is minimized at each stage of varying $b$ , successful numerical root finding leads to a value of $\Delta a$ that minimizes $\chi ^ { 2 }$ for the value of $\Delta b$ that gives $\Delta \chi ^ { 2 } = 1$ . This (see Figure 15.3.1) directly gives the tangent projection of the confidence region onto the $b$ -axis, and thus $\sigma _ { b }$ . It does not, however, give the tangent projection of the confidence region onto the $a$ -axis. In the figure, we have found the point labeled $B$ ; to find $\sigma _ { a }$ we need to find the point $A$ . Geometry to the rescue: To the extent that the confidence region is approximated by an ellipse, you can prove (see figure) that $\sigma _ { a } ^ { 2 } = r ^ { 2 } + s ^ { 2 }$ . The value of $s$ is known from having found the point $B$ . The value of $r$ follows from equations (15.3.2) and (15.3.3) applied at the $\chi ^ { 2 }$ minimum (point $o$ in the figure), giving

$$
r ^ { 2 } = 1 { \Big / } \sum _ { i } w _ { i }
$$

Actually, since $b$ can go through infinity, this whole procedure makes more sense in $( a , \theta )$ space than in $( a , b )$ space. That is, in fact, how the following program works. Since it is conventional, however, to return standard errors for $a$ and $b$ , not $a$ and $\theta$ , we finally use the relation

$$
\sigma _ { b } = \sigma _ { \theta } / \cos ^ { 2 } \theta
$$

We caution that if $b$ and its standard error are both large, so that the confidence region actually includes infinite slope, then the standard error $\sigma _ { b }$ is not very meaningful. The functor Chixy is normally called only by the routine Fitexy. However, if you want, you can yourself explore the confidence region by making repeated calls to Chixy (whose argument is an angle $\theta$ , not a slope $b$ ), after a single initializing call to Fitexy.

Be aware that the literature on the seemingly straightforward subject of this section is generally confusing and sometimes plain wrong. Deming’s [1] early treatment is sound, but its reliance on Taylor expansions gives inaccurate error estimates. References [2-4] are reliable, more recent, general treatments with critiques of earlier work. York [5] and Reed [6] usefully discuss the simple case of a straight line as treated here, but the latter paper has some errors, corrected in [7]. All this commotion has attracted the Bayesians [8-10], who have still different points of view.

A final caution, repeated from $\ S 1 5 . 0$ , is that if the goodness-of-fit is not acceptable (returned probability is too small), the standard errors $\sigma _ { a }$ and $\sigma _ { b }$ are surely not believable. In dire circumstances, you might try scaling all your $x$ and $y$ error bars by a constant factor until the probability is acceptable (0.5, say), to get more plausible values for $\sigma _ { a }$ and $\sigma _ { b }$ .

Implementing code is given in a Webnote [11].

# CITED REFERENCES AND FURTHER READING:

Deming, W.E. 1943, Statistical Adjustment of Data (New York: Wiley), reprinted 1964 (New York: Dover).[1]   
Jefferys, W.H. 1980, “On the Method of Least Squares,” Astronomical Journal, vol. 85, pp. 177– 181; see also vol. 95, p. 1299 (1988).[2]   
Jefferys, W.H. 1981, “On the Method of Least Squares — Part Two,” Astronomical Journal, vol. 86, pp. 149–155; see also vol. 95, p. 1300 (1988).[3]   
Lybanon, M. 1984, “A Better Least-Squares Method When Both Variables Have Uncertainties,” American Journal of Physics, vol.52,pp.22-26.[4]   
York, D. 1966, “Least-Squares Fitting of a Straight Line,” Canadian Journal of Physics, vol. 44, pp. 1079–1086.[5]   
Reed, B.C. 1989, “Linear Least-Squares Fits with Error in Both Coordinates,” American Journal of Physics,vol. 57, pp. 642-646;see also vol. 58,p.189,and vol.58,p. 1209.[6]   
Reed, B.C. 1992, “Linear Least-squares Fits with Errors in Both Coordinates. II: Comments on Parameter Variances,” American Journal of Physics, vol. 60, pp. 59–62.[7]   
Zellner, A. 1971, An Introduction to Bayesian Inference in Econometrics (New York: Wiley); reprinted 1987 (Malabar, FL: R. E. Krieger).[8]   
Gull, S.F. 1989, in Maximum Entropy and Bayesian Methods, J. Skilling, ed. (Boston: Kluwer).[9]   
Jaynes, E.T. 1991, in Maximum-Entropy and Bayesian Methods, Proceedings of the 10th International Workshop,W.T.Grandy, Jr.,and L.H. Schick,eds.(Boston: Kluwer).[10]   
Macdonald, J.R., and Thompson, W.J. 1992, “Least-Squares Fitting When Both Variables Contain Errors: Pitfalls and Possibilities,” American Journal of Physics, vol. 60, pp. 66–73.

Numerical Recipes Software 2007, “Code Implementation for Fitexy,” Numerical Recipes Webnote No.19,at http://www.nr.com/webnotes?19 [11]

# 15.4 General Linear Least Squares

An immediate generalization of $\ S 1 5 . 2$ is to fit a set of data points $( x _ { i } , y _ { i } )$ to a model that is not just a linear combination of 1 and $x$ (namely $a + b x$ ), but rather a linear combination of any $M$ specified functions of $x$ . For example, the functions could be $1 , x , x ^ { 2 } , \ldots , x ^ { M - 1 }$ , in which case their general linear combination,

$$
y ( x ) = a _ { 0 } + a _ { 1 } x + a _ { 2 } x ^ { 2 } + \cdots + a _ { M - 1 } x ^ { M - 1 }
$$

is a polynomial of degree $M - 1$ . Or, the functions could be sines and cosines, in which case their general linear combination is a Fourier series. The general form of this kind of model is

$$
y ( x ) = \sum _ { k = 0 } ^ { M - 1 } a _ { k } X _ { k } ( x )
$$

where the quantities $X _ { 0 } ( x ) , \ldots , X _ { M - 1 } ( x )$ are arbitrary fixed functions of $x$ , called the basis functions.

Note that the functions $X _ { k } ( x )$ can be wildly nonlinear functions of $x$ . In this discussion, “linear” refers only to the model’s dependence on its parameters $a _ { k }$ .

For these linear models we generalize the discussion of the previous section by defining a merit function

$$
\chi ^ { 2 } = \sum _ { i = 0 } ^ { N - 1 } \left[ \frac { y _ { i } - \sum _ { k = 0 } ^ { M - 1 } a _ { k } X _ { k } ( x _ { i } ) } { \sigma _ { i } } \right] ^ { 2 }
$$

As before, $\sigma _ { i }$ is the measurement error (standard deviation) of the $i$ th data point, presumed to be known. If the measurement errors are not known, they may all (as discussed at the end of $\ S 1 5 . 1 )$ be set to the constant value $\sigma = 1$ .

Once again, we will pick as best parameters those that minimize $\chi ^ { 2 }$ . There are several different techniques available for finding this minimum. Two are particularly useful, and we will discuss both in this section. To introduce them and elucidate their relationship, we need some notation.

Let A be a matrix whose $N \times M$ components are constructed from the $M$ basis functions evaluated at the $N$ abscissas $x _ { i }$ , and from the $N$ measurement errors $\sigma _ { i }$ , by the prescription

$$
A _ { i j } = { \frac { X _ { j } ( x _ { i } ) } { \sigma _ { i } } }
$$

The matrix A is called the design matrix of the fitting problem. Notice that in general A has more rows than columns, $N \ \geq \ M$ , since there must be more data points than model parameters to be solved for. (You can fit a straight line to two points, but not a very meaningful quintic!) The design matrix is shown schematically in Figure 15.4.1.

$$
\left\{ \begin{array} { l l l l l l l l } { x _ { 1 } } & { \left( \displaystyle \frac { X _ { i , j } ( x _ { 1 } ) } { \sigma _ { 0 } } \right) } & { \frac { X _ { i , 1 } ( x _ { 1 } ) } { \sigma _ { 0 } } } & { \cdots } & { \frac { X _ { M , i } ( x _ { 1 } ) } { \sigma _ { 0 } } } \\ { x _ { 1 } } & { \left( \displaystyle \frac { X _ { i , j } ( x _ { 1 } ) } { \sigma _ { 1 } } \right) } & { \frac { X _ { i , 1 } ( x _ { 1 } ) } { \sigma _ { 1 } } } & { \cdots } & { \frac { X _ { M , i } ( x _ { 1 } ) } { \sigma _ { 1 } } } \\ { \frac { \sigma _ { 0 } } { \sigma _ { 1 } } } & { \Biggl . } & { \Biggl . } & { \Biggl . } \\ { \frac { \sigma _ { 0 } } { \sigma _ { 1 } } } & { \Biggl . } & { \Biggl . } & { \Biggl . } \\ { \frac { \sigma _ { 1 } } { \sigma _ { 1 } } } & { \Biggl . } & { \Biggl } & { \Biggl . } & { \Biggl \{ \begin{array} { l l l } { X _ { i , 1 } ( x _ { 1 } ) } & { X _ { i , 1 } ( x _ { 1 } ) } & { \cdots } & { X _ { M , i } ( x _ { 1 } ) } \\ { \Biggl . } & { \Biggl . } & { \Biggl . } \\ { \Biggl . } & { \Biggl . } & { \Biggl . } \\ { \Biggl \{ \Biggl . } \frac { X _ { i , 1 } ( x _ { 1 } ) } { \sigma _ { 1 } } } & { \Biggl . } & { \cdots } & { \Biggl . } & { \Biggl . } \\ { \Biggl . } & { \Biggl . } & { \Biggl . } & { \Biggl . } & { \Biggl . } \end{array} \right\} \end{array}
$$

Also define a vector $\mathbf { b }$ of length $N$ by

$$
b _ { i } = \frac { y _ { i } } { \sigma _ { i } }
$$

and denote the $M$ vector whose components are the parameters to be fitted, $a _ { 0 } , . . .$ ;   
$a _ { M - 1 }$ , by a.

# 15.4.1 Solution by Use of the Normal Equations

The minimum of (15.4.3) occurs where the derivative of $\chi ^ { 2 }$ with respect to all $M$ parameters $a _ { k }$ vanishes. Specializing equation (15.1.8) to the case of the model (15.4.2), this condition yields the $M$ equations

$$
0 = \sum _ { i = 0 } ^ { N - 1 } \frac { 1 } { \sigma _ { i } ^ { 2 } } \Biggl [ y _ { i } - \sum _ { j = 0 } ^ { M - 1 } a _ { j } X _ { j } ( x _ { i } ) \Biggr ] X _ { k } ( x _ { i } ) \qquad k = 0 , \ldots , M - 1
$$

Interchanging the order of summations, we can write (15.4.6) as the matrix equation

$$
\sum _ { j = 0 } ^ { M - 1 } \alpha _ { k j } a _ { j } = \beta _ { k }
$$

where

$$
\alpha _ { k j } = \sum _ { i = 0 } ^ { N - 1 } { \frac { X _ { j } ( x _ { i } ) X _ { k } ( x _ { i } ) } { \sigma _ { i } ^ { 2 } } } \qquad { \mathrm { o r , ~ e q u i v a l e n t l y , } } \qquad \alpha = \mathbf { A } ^ { T } \cdot \mathbf { A }
$$

an $M \times M$ matrix, and

$$
{ \boldsymbol { \beta } } _ { k } = \sum _ { i = 0 } ^ { N - 1 } { \frac { y _ { i } X _ { k } ( x _ { i } ) } { \sigma _ { i } ^ { 2 } } } \qquad { \mathrm { o r , e q u i v a l e n t l y , } } \qquad { \boldsymbol { \beta } } = \mathbf { A } ^ { T } \cdot \mathbf { b }
$$

a vector of length $M$ .

The equations (15.4.6) or (15.4.7) are called the normal equations of the leastsquares problem. They can be solved for the vector of parameters a by the standard methods of Chapter 2, notably $L U$ decomposition and backsubstitution, Choleksy decomposition, or Gauss-Jordan elimination. In matrix form, the normal equations can be written as either

$$
\alpha \cdot { \mathbf { a } } = \beta \qquad { \mathrm { o r ~ a s } } \qquad \left( { \mathbf { A } } ^ { T } \cdot { \mathbf { A } } \right) \cdot { \mathbf { a } } = { \mathbf { A } } ^ { T } \cdot { \mathbf { b } }
$$

The inverse matrix $\mathbf { C } \equiv \mathbf { \alpha } \mathbf { \alpha } ^ { - 1 }$ , called the covariance matrix, is closely related to the probable (or, more precisely, standard) uncertainties of the estimated parameters a. To estimate these uncertainties, consider that

$$
a _ { j } = \sum _ { k = 0 } ^ { M - 1 } \alpha _ { j k } ^ { - 1 } \beta _ { k } = \sum _ { k = 0 } ^ { M - 1 } C _ { j k } \left[ \sum _ { i = 0 } ^ { N - 1 } \frac { y _ { i } X _ { k } ( x _ { i } ) } { \sigma _ { i } ^ { 2 } } \right]
$$

and that the variance associated with the estimate $a _ { j }$ can be found as in (15.2.7) from

$$
\sigma ^ { 2 } ( a _ { j } ) = \sum _ { i = 0 } ^ { N - 1 } \sigma _ { i } ^ { 2 } \left( \frac { \partial a _ { j } } { \partial y _ { i } } \right) ^ { 2 }
$$

Note that $\alpha _ { j k }$ is independent of $y _ { i }$ , so that

$$
\frac { \partial a _ { j } } { \partial y _ { i } } = \sum _ { k = 0 } ^ { M - 1 } C _ { j k } X _ { k } ( x _ { i } ) / \sigma _ { i } ^ { 2 }
$$

Consequently, we find that

$$
\sigma ^ { 2 } ( a _ { j } ) = \sum _ { k = 0 } ^ { M - 1 } \sum _ { l = 0 } ^ { M - 1 } C _ { j k } C _ { j l } \left[ \sum _ { i = 0 } ^ { N - 1 } \frac { X _ { k } ( x _ { i } ) X _ { l } ( x _ { i } ) } { \sigma _ { i } ^ { 2 } } \right]
$$

The final term in brackets is just the matrix $\pmb { \alpha }$ . Since this is the matrix inverse of $\mathbf { C }$ , (15.4.14) reduces immediately to

$$
\sigma ^ { 2 } ( a _ { j } ) = C _ { j j }
$$

In other words, the diagonal elements of $\mathbf { C }$ are the variances (squared uncertainties) of the fitted parameters a. It should not surprise you to learn that the offdiagonal elements $C _ { j k }$ are the covariances between $a _ { j }$ and $a _ { k }$ (cf. 15.2.10); but we shall defer discussion of these to $\ S 1 5 . 6$ .

We will now give a routine that implements the above formulas for the general linear least-squares problem, by the method of normal equations. Since we wish to compute not only the solution vector a but also the covariance matrix C, it is most convenient to use Gauss-Jordan elimination (routine gaussj of $\ S 2 . 1 \rrangle$ ) to perform the linear algebra. The operation count in this application is no larger than that for $L U$ decomposition. If you have no need for the covariance matrix, however, you can save a factor of 3 on the linear algebra by switching to $L U$ decomposition, without computation of the matrix inverse. In theory, since $\bar { \mathbf { A } ^ { T } }$ A is positive-definite, Cholesky decomposition is the most efficient way to solve the normal equations. However, in practice, most of the computing time is spent in looping over the data to form the equations, and Gauss-Jordan is quite adequate.

We need to warn you that the solution of a least-squares problem directly from the normal equations is rather susceptible to roundoff error, because the condition number of the matrix $\pmb { \alpha }$ is the square of the condition number of A. An alternative, and preferred, technique involves $\boldsymbol { \mathcal { Q } R }$ decomposition $( \ S 2 . 1 0 , \ S 1 1 . 4$ , and $\ S 1 1 . 7 $ ) of the design matrix A. This is essentially what we did at the end of $\ S 1 5 . 2$ for fitting data to a straight line, but without invoking all the machinery of $\boldsymbol { \mathcal { Q } R }$ to derive the necessary formulas. Later in this section, we will discuss other difficulties in the least-squares problem, for which the cure is singular value decomposition (SVD), of which we give an implementation. It turns out that SVD also fixes the roundoff problem, so it is our recommended technique for all but “easy” least-squares problems. It is for these easy problems that the following routine, which solves the normal equations, is intended.

The object Fitlin, below, has one “value-added feature” that can be quite useful in practical work: Frequently it is a matter of art to decide which parameters $a _ { k }$ in a model should be fit from the data set, and which should be held constant at fixed values, for example values predicted by a theory or measured in a previous experiment. One wants, therefore, to have a convenient means for “freezing” and “unfreezing” the parameters $a _ { k }$ . In the following code, the total number of parameters $a _ { k }$ is denoted ma (called $M$ above) and is deduced from the size of the vector that is returned by the user-supplied fitting function routine. The Fitlin object maintains a boolean array ia[0..ma-1]. Components that are false indicate that you want the corresponding elements of the parameter vector $\mathtt { a } \left[ 0 \dots \cdot \mathrm { m a } ^ { - 1 } \right]$ to be held fixed at their input values. Components that are true indicate parameters that should be fitted for. On output, any frozen parameters will have their variances, and all their covariances, set to zero in the covariance matrix.

# struct Fitlin {

Object for general linear least-squares fitting by solving the normal equations, also including the ability to hold specified parameters at fixed, specified values. Call constructor to bind data vectors and fitting functions. Then call any combination of hold, free, and fit as often as desired. fit sets the output quantities a, covar, and chisq.

# fitlin.h

Int ndat, ma;   
VecDoub_I &x,&y,&sig;   
VecDoub (\*funcs)(const Doub);   
VecBool ia; VecDoub a;   
MatDoub covar;   
Doub chisq;

Output values. a is the vector of fitted coefficients, covar is its covariance matrix, and chisq is the value of $\chi ^ { 2 }$ for the fit.

: ndat(xx.size()), x(xx), y(yy), sig(ssig), funcs(funks) { Constructor. Binds references to the data arrays xx, yy, and ssig, and to a user-supplied function funks $\mathbf { \Psi } ( \mathbf { x } )$ that returns a VecDoub containing ma basis functions evaluated at $x = \mathtt { x }$ . Initializes all parameters as free (not held).

ma $=$ funcs(x[0]).size();   
a.resize(ma);   
covar.resize(ma,ma);   
ia.resize(ma);   
for (Int $\scriptstyle { \dot { 1 } } = 0$ ;i<ma; $\dot { \bf 1 } + +$ ) ia[i] $=$ true;

void hold(const Int i, const Doub val) {ia[i] $=$ false; a[i] $=$ val;} void free(const Int i) {ia[i] $=$ true;}

Optional functions for holding a parameter, identified by a value i in the range $0 , \ldots , \mathtt { m a - 1 }$ , fixed at the value val, or for freeing a parameter that was previously held fixed. hold and free may be called for any number of parameters before calling fit to calculate best-fit values for the remaining (not held) parameters, and the process may be repeated multiple times. Alternatively, you can set the boolean vector ia directly, before calling fit.

# void fit() {

Solve the normal equations for $\chi ^ { 2 }$ minimization to fit for some or all of the coefficients a[0..ma-1] of a function that depends linearly on a, $\begin{array} { r } { y = \sum _ { i } \mathsf { a } _ { i } \times \mathbf { f u n k s } _ { i } ( x ) } \end{array}$ . Set answer values for a[0..ma-1], $\chi ^ { 2 } =$ chisq, and the covariance matrix covar[0..ma-1][0..ma-1]. (Parameters held fixed by calls to hold will return zero covariances.)

Int i,j,k,l,m,mfit ${ = } 0$ ;   
Doub ym,wt,sum,sig2i;   
VecDoub afunc(ma);   
for (j ${ = } 0$ ;j<ma;j++) if (ia[j]) mfit++;   
if (mfit $\scriptstyle = = \ 0$ ) throw("lfit: no parameters to be fitted");   
MatDoub temp(mfit,mfit,0.),beta(mfit,1,0.);   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<ndat;i++) { Loop over data to accumulate coefficients of afunc $=$ funcs(x[i]); the normal equations. ym=y[i]; if (mfit $<$ ma) { Subtract off dependences on known pieces for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<ma;j++) of the fitting function. if (!ia[j]) ym -= a[j]\*afunc[j]; } sig2i $^ { = 1 }$ .0/SQR(sig[i]); for (j=0,l=0;l<ma;l++) { Set up matrix and r.h.s. for matrix inversion. if (ia[l]) { wt=afunc[l]\*sig2i; for (k=0,m=0; $\mathtt { m } < = 1$ ;m++) if (ia[m]) temp[j][k $+ + ]$ $+ =$ wt\*afunc[m]; beta[j $\left| + + \right]$ [0] $+ =$ ym\*wt; } }   
  
for (j ${ = } 1$ ;j<mfit;j++) for $\scriptstyle \mathtt { k } = 0$ ;k<j;k++) temp[k][j] $=$ temp[j][k];   
gaussj(temp,beta); Matrix solution.   
for (j=0, $\mathtt { 1 } = 0$ ;l<ma;l++) if (ia[l]) a[l] $=$ beta[j $+ + ]$ [0];   
Spread the solution to appropriate positions in a, and evaluate $\chi ^ { 2 }$ of the fit.   
chisq ${ = } 0$ .0;   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<ndat;i++) { afunc $=$ funcs(x[i]); sum=0.0; for (j ${ = } 0$ ;j<ma;j++) sum $+ =$ a[j]\*afunc[j]; chisq $+ =$ SQR((y[i]-sum)/sig[i]);   
}   
for (j ${ = } 0$ ;j<mfit;j++) for $\scriptstyle ( \mathtt { k } = 0$ ;k<mfit;k++) covar[j][k] $=$ temp[j][k];   
for (i=mfit;i<ma;i++) Rearrange covariance matrix into the correct for (j ${ = } 0$ ;j $< \dot { 1 } + 1$ ;j++) covar[i][j] $=$ covar[j][i]=0.0; order.   
$\mathrm { k } =$ mfit-1;   
for (j=ma-1;j>=0;j--) {

if (ia[j]) { for (i=0;i<ma; $\dot { \bar { \lambda } } + +$ ) SWAP(covar[i][k],covar[i][j]); for (i=0;i<ma; $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \rho } } } ,$ ) SWAP(covar[k][i],covar[j][i]); k--; } } } };

Typical use of Fitlin will look something like this:

const Int npts=: : :   
VecDoub xx(npts),yy(npts),ssig(npts); Fitlin myfit(xx,yy,ssig,cubicfit); myfit.fit();

where (in this example) cubicfit is a user-supplied function that might look like this:

VecDoub cubicfit(const Doub x) {VecDoub ans(4);ans[0] $\qquad = \ 1 \ .$ ;for (Int $\dot { \bf 1 } = 1$ ;i<4;i $^ { + + }$ ) ans[i] $=$ x\*ans[i-1];return ans;  
}

# 15.4.2 Solution by Use of Singular Value Decomposition

In some applications, the normal equations are perfectly adequate for linear least-squares problems. However, in many other cases the normal equations are very close to singular. A zero pivot element may be encountered during the solution of the linear equations (e.g., in gaussj), in which case you get no solution at all. Or a very small pivot may occur, in which case you typically get fitted parameters $a _ { k }$ with very large magnitudes that are delicately (and unstably) balanced to cancel out almost precisely when the fitted function is evaluated.

Why does this commonly occur? A mathematical reason is that the condition number of the matrix $\pmb { \alpha }$ is the square of the condition number of A. But an additional physical reason is that, more often than experimenters would like to admit, data do not clearly distinguish between two or more of the basis functions provided. If two such functions, or two different combinations of functions, happen to fit the data about equally well — or equally badly — then the matrix $\pmb { \alpha }$ , unable to distinguish between them, neatly folds up its tent and becomes singular. There is a certain mathematical irony in the fact that least-squares problems are both overdetermined (number of data points greater than number of parameters) and underdetermined (ambiguous combinations of parameters exist); but that is how it frequently is. The ambiguities can be extremely hard to notice a priori in complicated problems.

Enter singular value decomposition (SVD). This would be a good time for you to review the material in $\ S 2 . 6$ , which we will not repeat here. In the case of an overdetermined system, SVD produces a solution that is the best approximation in the least-squares sense, cf. equation (2.6.10). That is exactly what we want. In the case of an underdetermined system, SVD produces a solution whose values (for us, the $a _ { k }$ ’s) are smallest in the least-squares sense, cf. equation (2.6.8). That is also what we want: When some combination of basis functions is irrelevant to the fit, that combination will be driven down to a small, innocuous, value, rather than pushed up to delicately canceling infinities.

In terms of the design matrix A (equation 15.4.4) and the vector $\mathbf { b }$ (equation 15.4.5), minimization of $\chi ^ { 2 }$ in (15.4.3) can be written as

$$
\mathrm { f i n d } \qquad \mathbf { a } \qquad \mathrm { t h a t \ m i n i m i z e s } \qquad \chi ^ { 2 } = | \mathbf { A } \cdot \mathbf { a } - \mathbf { b } | ^ { 2 }
$$

Comparing to equation (2.6.9), we see that this is precisely the problem that routines in the SVD object are designed to solve. The solution, which is given by equation (2.6.12), can be rewritten as follows: If $\mathbf { U }$ and $\mathbf { V }$ enter the SVD decomposition of A according to equation (2.6.1), as computed by SVD, then let the vectors $\mathbf { U } _ { ( i ) } \ : i =$ $0 , \ldots , M - 1$ denote the columns of $\mathbf { U }$ (each one a vector of length $N$ ), and let the vectors $\mathbf { V } _ { ( i ) } \ : i = 0 , \ldots , M - 1$ denote the columns of $\mathbf { V }$ (each one a vector of length $M _ { ☉ }$ ). Then the solution (2.6.12) of the least-squares problem (15.4.16) can be written as

$$
\mathbf { a } = \sum _ { i = 0 } ^ { M - 1 } \left( { \frac { \mathbf { U } _ { ( i ) } \cdot \mathbf { b } } { w _ { i } } } \right) \mathbf { V } _ { ( i ) }
$$

where the $w _ { i }$ are, as in $\ S 2 . 6$ , the singular values calculated by SVD.

Equation (15.4.17) says that the fitted parameters a are linear combinations of the columns of $\mathbf { V }$ , with coefficients obtained by forming dot products of the columns of $\mathbf { U }$ with the weighted data vector (15.4.5). Though it is beyond our scope to prove here, it turns out that the standard (loosely, “probable”) errors in the fitted parameters are also linear combinations of the columns of $\mathbf { V }$ . In fact, equation (15.4.17) can be written in a form displaying these errors as

$$
\mathbf { a } = \left[ \sum _ { i = 0 } ^ { M - 1 } \left( { \frac { \mathbf { U } _ { ( i ) } \cdot \mathbf { b } } { w _ { i } } } \right) \mathbf { V } _ { ( i ) } \right] \pm { \frac { 1 } { w _ { 0 } } } \mathbf { V } _ { ( 0 ) } \pm \cdots \pm { \frac { 1 } { w _ { M - 1 } } } \mathbf { V } _ { ( M - 1 ) }
$$

Here each $\pm$ is followed by a standard deviation. The amazing fact is that, decomposed in this fashion, the standard deviations are all mutually independent (uncorrelated). Therefore they can be added together in root-mean-square fashion. What is going on is that the vectors $\mathbf { V } _ { ( i ) }$ are the principal axes of the error ellipsoid of the fitted parameters a (see $\ S 1 5 . 6 )$ .

It follows that the variance in the estimate of a parameter $a _ { j }$ is given by

$$
\sigma ^ { 2 } ( a _ { j } ) = \sum _ { i = 0 } ^ { M - 1 } \frac { 1 } { w _ { i } ^ { 2 } } [ { \bf V } _ { ( i ) } ] _ { j } ^ { 2 } = \sum _ { i = 0 } ^ { M - 1 } \left( \frac { V _ { j i } } { w _ { i } } \right) ^ { 2 }
$$

whose result should be identical to (15.4.14). As before, you should not be surprised at the formula for the covariances, here given without proof,

$$
\mathrm { C o v } ( a _ { j } , a _ { k } ) = \sum _ { i = 0 } ^ { M - 1 } \left( \frac { V _ { j i } V _ { k i } } { w _ { i } ^ { 2 } } \right)
$$

We introduced this subsection by noting that the normal equations can fail by encountering a zero pivot. We have not yet, however, mentioned how SVD overcomes this problem. The answer is: If any singular value $w _ { i }$ is zero, its reciprocal in equation (15.4.18) should be set to zero, not infinity. (Compare the discussion preceding equation 2.6.7.) This corresponds to adding to the fitted parameters a a zero multiple, rather than some random large multiple, of any linear combination of basis functions that are degenerate in the fit. It is a good thing to do!

Moreover, if a singular value $w _ { i }$ is nonzero but very small, you should also define its reciprocal to be zero, since its apparent value is probably an artifact of roundoff error, not a meaningful number. A plausible answer to the question “how small is small?” is to edit in this fashion all singular values whose ratio to the largest singular value is less than $N$ times the machine precision $\epsilon$ . (This is a more conservative recommendation than the default in $\ S 2 . 6$ , which scales as $N ^ { 1 / 2 }$ .)

There is another reason for editing even additional singular values, ones large enough that roundoff error is not a question. Singular value decomposition allows you to identify linear combinations of variables that just happen not to contribute much to reducing the $\chi ^ { 2 }$ of your data set. Editing these can sometimes reduce the probable error errors on your coefficients quite significantly, while increasing the minimum $\chi ^ { 2 }$ only negligibly. We will learn more about identifying and treating such cases in $\ S 1 5 . 6$ .

Generally speaking, we recommend that you always use SVD techniques instead of using the normal equations. SVD’s only significant disadvantage is that it requires extra storage of order $N \times M$ for the design matrix and its decomposition. Storage is also required for the $M \times M$ matrix V , but this is instead of the same-sized matrix for the coefficients of the normal equations. SVD can be significantly slower than solving the normal equations; however, its great advantage, that it (theoretically) cannot fail, more than makes up for the speed disadvantage.

The following object, Fitsvd, has an interface almost identical to Fitlin, above. An additional optional parameter in the constructor sets the threshold for editing singular values.

# struct Fitsvd {

Object for general linear least-squares fitting using singular value decomposition. Call constructor to bind data vectors and fitting functions. Then call fit, which sets the output quantities a, covar, and chisq.

(Why is x a pointer? Explained in $\ S 1 5 . 4 . 4 . $

Int ndat, ma;   
Doub tol;   
VecDoub_I \*x,&y,&sig;   
VecDoub (\*funcs)(const Doub);   
VecDoub a;   
MatDoub covar;   
Doub chisq;

Output values. a is the vector of fitted coefficients, covar is its covariance matrix, and chisq is the value of $\chi ^ { 2 }$ for the fit.

Fitsvd(VecDoub_I &xx, VecDoub_I &yy, VecDoub_I &ssig, VecDoub funks(const Doub), const Doub TOL $^ { = 1 }$ .e-12) : ndat(yy.size()), x(&xx), xmd(NULL), y(yy), sig(ssig), funcs(funks), tol(TOL) {}

Constructor. Binds references to the data arrays xx, yy, and ssig, and to a user-supplied function funks $\mathbf { \Psi } ( \mathbf { x } )$ that returns a VecDoub containing ma basis functions evaluated at $x = \mathtt { x }$ . If TOL is positive, it is the threshold (relative to the largest singular value) for discarding small singular values. If it is $\leq 0$ , the default value in SVD is used.

# void fit() {

Solve by singular value decomposition the $\chi ^ { 2 }$ minimization that fits for the coefficients a[0..ma-1] of a function that depends linearly on a, $\begin{array} { r } { y = \sum _ { i } \mathsf { a } _ { i } \times \mathbf { f u n k s } _ { i } ( x ) } \end{array}$ . Set answer values for a[0..ma-1], chisq $= \chi ^ { 2 }$ , and the covariance matrix covar[0..ma-1][0..ma-1].

Int i,j,k;   
Doub tmp,thresh,sum;   
if (x) ma $=$ funcs( $( * \mathbf { x } )$ [0]).size();   
else ma $=$ funcsmd(row(\*xmd,0)).size(); (Discussed in $\ S 1 5 . 4 . 4 . )$   
a.resize(ma);   
covar.resize(ma,ma);   
MatDoub aa(ndat,ma);   
VecDoub b(ndat),afunc(ma);   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<ndat; $\mathbf { i } + +$ ) { Accumulate coefficients of the if (x) afunc=funcs((\*x)[i]); design matrix. else afunc=funcsmd(row(\*xmd,i)); (Discussed in $\ S 1 5 . 4 . 4 .$ ) tmp $^ { = 1 }$ .0/sig[i]; for ( $\scriptstyle { \mathsf { i } } = 0$ ;j<ma;j++) aa[i][j] $=$ afunc[j]\*tmp; b[i]=y[i]\*tmp;   
}   
SVD svd(aa); Singular value decomposition.   
thresh $=$ (tol > 0. ? tol\*svd.w[0] : -1.);   
svd.solve(b,a,thresh); Solve for the coefficients.   
chisq=0.0; Evaluate chi-square.   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<ndat; $\dot { \bf 1 } + +$ ) { sum $_ { = 0 }$ .; for (j ${ = } 0$ ;j<ma;j++) sum $+ =$ aa[i][j]\*a[j]; chisq $+ =$ SQR(sum-b[i]);   
}   
for (i=0;i<ma;i++) { Sum contributions to covariance for ( $\scriptstyle \mathrm { j = 0 }$ ;j<i+1;j++) { matrix (15.4.20). sum $\mathtt { i } = 0 . 0$ ; for ( $\scriptstyle 1 = 0$ ;k<ma;k++) if (svd.w[k] $>$ svd.tsh) sum $+ =$ svd.v[i][k]\*svd.v[j][k]/SQR(svd.w[k]); covar[j][i] $=$ covar[i][j] $=$ sum; }   
}

# }

From here on, code for multidimensional fits, to be discussed in $\ S 1 5 . 4 . 4$ .   
MatDoub_I \*xmd;   
VecDoub (\*funcsmd)(VecDoub_I &); Fitsvd(MatDoub_I &xx, VecDoub_I &yy, VecDoub_I &ssig,   
VecDoub funks(VecDoub_I &), const Doub TOL $^ { = 1 }$ .e-12)   
: ndat(yy.size()), x(NULL), xmd(&xx), y(yy), sig(ssig),   
funcsmd(funks), tol(TOL) {}   
Constructor for multidimensional fits. Exactly the same as the previous constructor, except that xx is now a matrix whose rows are the multidimensional data points and funks is now a function of a multidimensional data point (as a VecDoub).

VecDoub row(MatDoub_I &a, const Int i) { Utility. Returns the row of a MatDoub as a VecDoub. Int j, $\mathrm { n } = \mathrm { a }$ .ncols(); VecDoub ans(n); for (j ${ = } 0$ ;j<n;j++) ans[j] $=$ a[i][j]; return ans; } };

For degenerate or nearly degenerate problems, if you want to try different singular value thresholds, you call the Fitsvd constructor once. Then, as many times as you want, “reach in” and increase tol, then call fit again and examine the resulting value of chisq (and optionally also the covariance matrix). Keep going as long as chisq does not increase by too much. To learn what is “too much,” see $\ S 1 5 . 6$ ; but a few $\times 0 . 1$ is almost always OK.

# 15.4.3 Examples

Be aware that some apparently nonlinear problems can be expressed so that they are linear. For example, an exponential model with two parameters $a$ and $b$ ,

$$
y ( x ) = a \exp ( - b x )
$$

can be rewritten as

$$
\log [ y ( x ) ] = c - b x
$$

which is linear in its parameters $c$ and $b$ . (Of course you must be aware that such transformations do not exactly take Gaussian errors into Gaussian errors.)

Also watch out for “nonparameters,” as in

$$
y ( x ) = a \exp ( - b x + d )
$$

Here the parameters $a$ and $d$ are, in fact, indistinguishable. This is a good example of where the normal equations will be exactly singular, and where SVD will find a zero singular value. SVD will then make a least-squares choice for setting a balance between $a$ and $d$ (or, rather, their equivalents in the linear model derived by taking the logarithms). However — and this is true whenever SVD gives back a zero singular value — you are better advised to figure out analytically where the degeneracy is among your basis functions, and then make appropriate deletions in the basis set.

We already gave an example of a user-supplied fitting-function routine, cubicfit, above. Here are two further examples. First, we trivially generalize cubicfit for polynomials of an arbitrary, preset, degree:

Global variable for the degree plus one.

# fit examples.h

# VecDoub fpoly(const Doub x) {

Fitting routine for a polynomial of degree fpoly_np-1. Int j; VecDoub p(fpoly_np); $\mathrm { p } \left[ 0 \right] = 1$ .0; for ( $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<fpoly_np;j++) p[j]=p[j-1]\*x; return p;

# }

The second example is slightly less trivial. It is used to fit Legendre polynomials up to some order fleg_nl to a data set. (Note that, for most uses, the data should satisfy $- 1 \leq x \leq 1 .$ )

Int fleg_nl = 10;

Global variable for the degree plus one.

# fit examples.h

# VecDoub fleg(const Doub x) {

Fitting routine for an expansion with nl Legendre polynomials, evaluated using the recurrence relation as in $\ S 5 . 4$ .

Int j;   
Doub twox,f2,f1,d;   
VecDoub pl(fleg_nl);   
pl $[ 0 ] = 1$ .;   
pl $\left[ 1 \right] = \mathbf { x }$ ;   
if (fleg_nl $> 2$ ) { twox $^ { - 2 }$ .\*x; $\pm 2 \mathrm { = x }$ ; d=1.; for ( $\scriptstyle \mathbf { j } = 2$ ;j<fleg_nl;j++)

$\mathtt { f } 1 = \mathtt { d } + +$ ; f2+=twox; pl[j] $=$ (f2\*pl[j-1]-f1\*pl[j-2])/d; } } return pl;

# 15.4.4 Multidimensional Fits

If you are measuring a single variable $y$ as a function of more than one variable — say, a vector of variables $\mathbf { X }$ — then your basis functions will be functions of a vector, $X _ { 0 } ( \mathbf { x } ) , \ldots , X _ { M - 1 } ( \mathbf { x } )$ . The $\chi ^ { 2 }$ merit function is now

$$
\chi ^ { 2 } = \sum _ { i = 0 } ^ { N - 1 } \left[ \frac { y _ { i } - \sum _ { k = 0 } ^ { M - 1 } a _ { k } X _ { k } ( \mathbf { x } _ { i } ) } { \sigma _ { i } } \right] ^ { 2 }
$$

All of the preceding discussion goes through unchanged, with $x$ replaced by $\mathbf { X }$ . In fact, we anticipated this in the coding of Fitsvd, above, which can do multidimensional general linear fits as easily as one-dimensional. Here is how:

A second, overloaded, constructor in Fitsvd substitutes a matrix xx for what was previously a vector. The rows of the matrix are the ndat data points. The number of columns is the dimensionality of the space (that is, of $\mathbf { X }$ ). Similarly, the user-supplied function funks now takes a vector argument, an $\mathbf { X }$ . A simple example (fitting a quadratic function to data in two dimensions) might be

VecDoub quadratic2d(VecDoub_I &xx) { VecDoub ans(6); Doub $\tt x { = } \tt x x$ [0], $\scriptstyle \mathbf { y } = \mathbf { x } \mathbf { x } [ 1 ]$ ; ans[0] $= ~ 1$ ; ans[1] $=$ x; ans[2] $\begin{array} { r l r } { \mathbf { \Psi } } & { { } = } & { \mathbf { y } : \mathbf { x } \equiv } \end{array}$ ; ans[3] $=$ x\*x; ans[4] $=$ x\*y; ans[5] $=$ y\*y; return ans;   
}

Be sure that the argument of your user function has exactly the type “VecDoub_I &” (and not, for example, “VecDoub &” or “VecDoub_I”), since strict $\mathrm { C } { + + }$ compilers are picky about this.

The two constructors in Fitsvd communicate to fit whether data points are one-dimensional or multidimensional by setting either xmd or $_ \texttt { x }$ to NULL. This explains the oddity that x was bound to the user data as a pointer, while y and sig were bound as references. (Yes, we know this is a bit of a hack!)

# CITED REFERENCES AND FURTHER READING:

Bevington, P.R., and Robinson, D.K. 2002, Data Reduction and Error Analysis for the Physical Sciences, 3rd ed. (New York: McGraw-Hill), Chapter 7.   
Lupton, R. 1993, Statistics in Theory and Practice (Princeton, NJ: Princeton University Press), Chapter 11.   
Lawson, C.L., and Hanson, R. 1974, Solving Least Squares Problems (Englewood Cliffs, NJ: Prentice-Hall); reprinted 1995 (Philadelphia: S.I.A.M.).   
Monahan, J.F. 2001, Numerical Methods of Statistics (Cambridge, UK: Cambridge University Press), Chapter 5.   
Forsythe, G.E., Malcolm, M.A., and Moler, C.B. 1977, Computer Methods for Mathematical Computations (Englewood Cliffs,NJ: Prentice-Hall), Chapter 9.   
Gelman, A., Carlin, J.B., Stern, H.S., and Rubin, D.B. 2004, Bayesian Data Analysis, 2nd ed. (Boca Raton, FL: Chapman & Hall/CRC), Chapter 14.

# 15.5 Nonlinear Models

We now consider fitting when the model depends nonlinearly on the set of $M$ unknown parameters $a _ { k } , k = 0 , 1 , \dots , M - 1$ . We use the same approach as in previous sections, namely to define a $\chi ^ { 2 }$ merit function and determine best-fit parameters by its minimization. With nonlinear dependences, however, the minimization must proceed iteratively. Given trial values for the parameters, we develop a procedure that improves the trial solution. The procedure is then repeated until $\chi ^ { 2 }$ stops (or effectively stops) decreasing.

How is this problem different from the general nonlinear function minimization problem already dealt with in Chapter 10? Superficially, not at all. Sufficiently close to the minimum, we expect the $\chi ^ { 2 }$ function to be well approximated by a quadratic form, which we can write as

$$
\begin{array} { r } { \chi ^ { 2 } ( \mathbf { a } ) \approx \gamma - \mathbf { d } \cdot \mathbf { a } + \frac { 1 } { 2 } \mathbf { a } \cdot \mathbf { D } \cdot \mathbf { a } } \end{array}
$$

where $\mathbf { d }$ is an $M$ -vector and $\mathbf { D }$ is an $M \times M$ matrix. (Compare equation 10.8.1.) If the approximation is a good one, we know how to jump from the current trial parameters $\mathbf { a } _ { \mathrm { c u r } }$ to the minimizing ones $\mathbf { a } _ { \mathrm { m i n } }$ in a single leap, namely

$$
\mathbf { a } _ { \mathrm { m i n } } = \mathbf { a } _ { \mathrm { c u r } } + \mathbf { D } ^ { - 1 } \cdot \left[ - \nabla \chi ^ { 2 } ( \mathbf { a } _ { \mathrm { c u r } } ) \right]
$$

(Compare equation 10.9.4.)

On the other hand, (15.5.1) might be a poor local approximation to the shape of the function that we are trying to minimize at $\mathbf { a } _ { \mathrm { c u r } }$ . In that case, about all we can do is take a step down the gradient, as in the steepest descent method (-10.8). In other words,

$$
\mathbf { a } _ { \mathrm { n e x t } } = \mathbf { a } _ { \mathrm { c u r } } - \mathrm { c o n s t a n t } \times \nabla \chi ^ { 2 } ( \mathbf { a } _ { \mathrm { c u r } } )
$$

where the constant is small enough not to exhaust the downhill direction.

To use (15.5.2) or (15.5.3), we must be able to compute the gradient of the $\chi ^ { 2 }$ function at any set of parameters a. To use (15.5.2) we also need the matrix $\mathbf { D }$ , which is the second derivative matrix (Hessian matrix) of the $\chi ^ { 2 }$ merit function, at any a.

Now, this is the crucial difference from Chapter 10: There, we had no way of directly evaluating the Hessian matrix. We were given only the ability to evaluate the function to be minimized and (in some cases) its gradient. Therefore, we had to resort to iterative methods not just because our function was nonlinear, but also in order to build up information about the Hessian matrix. Sections 10.9 and 10.8 concerned themselves with two different techniques for building up this information.

Here, life is much simpler. We know exactly the form of $\chi ^ { 2 }$ , since it is based on a model function that we ourselves have specified. Therefore, the Hessian matrix is known to us. Thus we are free to use (15.5.2) whenever we care to do so. The only reason to use (15.5.3) will be failure of (15.5.2) to improve the fit, signaling failure of (15.5.1) as a good local approximation.

# 15.5.1 Calculation of the Gradient and Hessian

The model to be fitted is

$$
y = y ( x | \mathbf { a } )
$$

and the $\chi ^ { 2 }$ merit function is

$$
\chi ^ { 2 } ( \mathbf { a } ) = \sum _ { i = 0 } ^ { N - 1 } \left[ \frac { y _ { i } - y ( x _ { i } | \mathbf { a } ) } { \sigma _ { i } } \right] ^ { 2 }
$$

The gradient of $\chi ^ { 2 }$ with respect to the parameters a, which will be zero at the $\chi ^ { 2 }$ minimum, has components

$$
\frac { \partial \chi ^ { 2 } } { \partial a _ { k } } = - 2 \sum _ { i = 0 } ^ { N - 1 } \frac { \left[ y _ { i } - y ( x _ { i } | \mathbf { a } ) \right] } { \sigma _ { i } ^ { 2 } } \frac { \partial y ( x _ { i } | \mathbf { a } ) } { \partial a _ { k } } \qquad k = 0 , 1 , \ldots , M - 1
$$

Taking an additional partial derivative gives

$$
\frac { \partial ^ { 2 } \chi ^ { 2 } } { \partial a _ { k } \partial a _ { l } } = 2 \sum _ { i = 0 } ^ { N - 1 } \frac { 1 } { \sigma _ { i } ^ { 2 } } \left[ \frac { \partial y ( x _ { i } | \mathbf { a } ) } { \partial a _ { k } } \frac { \partial y ( x _ { i } | \mathbf { a } ) } { \partial a _ { l } } - [ y _ { i } - y ( x _ { i } | \mathbf { a } ) ] \frac { \partial ^ { 2 } y ( x _ { i } | \mathbf { a } ) } { \partial a _ { l } \partial a _ { k } } \right]
$$

It is conventional to remove the factors of 2 by defining

$$
\beta _ { k } \equiv - \frac 1 2 \frac { \partial \chi ^ { 2 } } { \partial a _ { k } } \qquad \alpha _ { k l } \equiv \frac 1 2 \frac { \partial ^ { 2 } \chi ^ { 2 } } { \partial a _ { k } \partial a _ { l } }
$$

making $\begin{array} { r } { \pmb { \alpha } = \frac { 1 } { 2 } \mathbf { D } } \end{array}$ in equation (15.5.2), in terms of which that equation can be rewritten as the set of linear equations:

$$
\sum _ { l = 0 } ^ { M - 1 } \alpha _ { k l } \delta a _ { l } = \beta _ { k }
$$

This set is solved for the increments $\displaystyle { \delta \boldsymbol { a } _ { l } }$ that, added to the current approximation, give the next approximation. In the context of least squares, the matrix $\pmb { \alpha }$ , equal to one-half times the Hessian matrix, is usually called the curvature matrix.

Equation (15.5.3), the steepest descent formula, translates to

$$
\delta \boldsymbol { a } _ { l } = \mathrm { c o n s t a n t } \times \boldsymbol { \beta } _ { l }
$$

Note that the components $\alpha _ { k l }$ of the Hessian matrix (15.5.7) depend both on the first derivatives and on the second derivatives of the basis functions with respect to their parameters. Some treatments proceed to ignore the second derivative without comment. We will ignore it also, but only after a few comments.

Second derivatives occur because the gradient (15.5.6) already has a dependence on $\partial y / \partial a _ { k }$ , and so the next derivative simply must contain terms involving $\partial ^ { 2 } y / \partial a _ { l } \partial a _ { k }$ . The second derivative term can be dismissed when it is zero (as in the linear case of equation 15.4.8) or small enough to be negligible when compared to the term involving the first derivative. It also has an additional possibility of being ignorably small in practice: The term multiplying the second derivative in equation (15.5.7) is $\left[ y _ { i } - y ( x _ { i } | \mathbf { a } ) \right]$ . For a successful model, this term should just be the random measurement error of each point. This error can have either sign, and should in general be uncorrelated with the model. Therefore, the second derivative terms tend to cancel out when summed over $i$ .

Inclusion of the second derivative term can in fact be destabilizing if the model fits badly or is contaminated by outlier points that are unlikely to be offset by compensating points of opposite sign. From this point on, we will always use as the definition of $\alpha _ { k l }$ the formula

$$
\alpha _ { k l } = \sum _ { i = 0 } ^ { N - 1 } \frac { 1 } { \sigma _ { i } ^ { 2 } } \left[ \frac { \partial y ( x _ { i } | \mathbf { a } ) } { \partial a _ { k } } \frac { \partial y ( x _ { i } | \mathbf { a } ) } { \partial a _ { l } } \right]
$$

This expression more closely resembles its linear cousin (15.4.8). You should understand that minor (or even major) fiddling with $\pmb { \alpha }$ has no effect at all on what final set of parameters a is reached, but affects only the iterative route that is taken in getting there. The condition at the $\chi ^ { 2 }$ minimum, that $\beta _ { k } = 0$ for all $k$ , is independent of how $\pmb { \alpha }$ is defined.

# 15.5.2 Levenberg-Marquardt Method

Marquardt [1] put forth an elegant method, related to an earlier suggestion of Levenberg, for varying smoothly between the extremes of the inverse-Hessian method (15.5.9) and the steepest descent method (15.5.10). The latter method is used far from the minimum, switching continuously to the former as the minimum is approached. This Levenberg-Marquardt method (also called the Marquardt method) works very well in practice if you can guess plausible starting guesses for your parameters. It has become a standard nonlinear least-squares routine.

The method is based on two elementary, but important, insights. Consider the “constant” in equation (15.5.10). What should it be, even in order of magnitude? What sets its scale? There is no information about the answer in the gradient. That tells only the slope, not how far that slope extends. Marquardt’s first insight is that the components of the Hessian matrix, even if they are not usable in any precise fashion, give some information about the order-of-magnitude scale of the problem.

The quantity $\chi ^ { 2 }$ is nondimensional, i.e., is a pure number; this is evident from its definition (15.5.5). On the other hand, $\beta _ { k }$ has the dimensions of $1 / a _ { k }$ , which may well be dimensional, i.e., have units like $\mathrm { c m } ^ { - 1 }$ , or kilowatt-hours, or whatever. (In fact, each component of $\beta _ { k }$ can have different dimensions!) The constant of proportionality between $\beta _ { k }$ and $\delta \boldsymbol { a } _ { k }$ must therefore have the dimensions of $a _ { k } ^ { 2 }$ . Scan the components of $\pmb { \alpha }$ and you see that there is only one obvious quantity with these dimensions, and that is $1 / \alpha _ { k k }$ , the reciprocal of the diagonal element. So that must set the scale of the constant. But that scale might itself be too big. So let’s divide the constant by some (nondimensional) fudge factor $\lambda$ , with the possibility of setting $\lambda \gg 1$ to cut down the step. In other words, replace equation (15.5.10) by

$$
\delta a _ { l } = \frac { 1 } { \lambda \alpha _ { l l } } \beta _ { l } \qquad \mathrm { o r } \qquad \lambda \alpha _ { l l } \delta a _ { l } = \beta _ { l }
$$

It is necessary that $\alpha _ { l l }$ be positive, but this is guaranteed by definition (15.5.11) — another reason for adopting that equation.

Marquardt’s second insight is that equations (15.5.12) and (15.5.9) can be combined if we define a new matrix $\alpha ^ { \prime }$ by the following prescription:

$$
\begin{array} { l } { { \alpha _ { j j } ^ { \prime } \equiv \alpha _ { j j } ( 1 + \lambda ) } } \\ { { \alpha _ { j k } ^ { \prime } \equiv \alpha _ { j k } \qquad ( j \ne k ) } } \end{array}
$$

and then replace both (15.5.12) and (15.5.9) by

$$
\sum _ { l = 0 } ^ { M - 1 } \alpha _ { k l } ^ { \prime } \delta a _ { l } = \beta _ { k }
$$

When $\lambda$ is very large, the matrix $\alpha ^ { \prime }$ is forced into being diagonally dominant, so equation (15.5.14) goes over to be identical to (15.5.12). On the other hand, as $\lambda$ approaches zero, equation (15.5.14) goes over to (15.5.9).

Given an initial guess for the set of fitted parameters a, the recommended Marquardt recipe is as follows:

- Compute $\chi ^ { 2 } ( \mathbf { a } )$ .   
- Pick a modest value for $\lambda$ , say $\lambda = 0 . 0 0 1$ .   
- $( \dag )$ Solve the linear equations (15.5.14) for ${ \delta \bf a }$ and evaluate $\chi ^ { 2 } ( \mathbf { a } + \delta \mathbf { a } )$ .   
If $\chi ^ { 2 } ( \mathbf { a } + \delta \mathbf { a } ) \geq \chi ^ { 2 } ( \mathbf { a } )$ , increase $\lambda$ by a factor of 10 (or any other substantial factor) and go back to $( \dag )$ .   
- If $\chi ^ { 2 } ( \mathbf { a } + \delta \mathbf { a } ) < \chi ^ { 2 } ( \mathbf { a } )$ , decrease $\lambda$ by a factor of 10, update the trial solution $\mathbf { a } \gets \mathbf { a } + \delta \mathbf { a }$ , and go back to $( \dag )$ .

Also necessary is a condition for stopping. Iterating to convergence (to machine accuracy or to the roundoff limit) is generally wasteful and unnecessary since the minimum is at best only a statistical estimate of the parameters a. As we will see in $\ S 1 5 . 6$ , a change in the parameters that changes $\chi ^ { 2 }$ by an amount $\ll 1$ is never statistically meaningful.

Furthermore, it is not uncommon to find the parameters wandering around near the minimum in a flat valley of complicated topography. The reason is that Marquardt’s method generalizes the method of normal equations (-15.4); hence it has the same problem as that method with regard to near-degeneracy of the minimum. Outright failure by a zero pivot is possible, but unlikely. More often, a small pivot will generate a large correction that is then rejected, the value of $\lambda$ being then increased. For sufficiently large $\lambda$ , the matrix $\pmb { \alpha } ^ { \prime }$ is positive-definite and can have no small pivots. Thus the method does tend to stay away from zero pivots, but at the cost of a tendency to wander around doing steepest descent in very unsteep degenerate valleys.

These considerations suggest that, in practice, one might as well stop iterating after a few occurrences of $\chi ^ { 2 }$ decreasing by a negligible amount, say either less than 0:001 absolutely or (in case roundoff prevents that being reached) fractionally. Don’t stop after a step where $\chi ^ { 2 }$ increases more than trivially: That only shows that $\lambda$ has not yet adjusted itself optimally.

Once the acceptable minimum has been found, one wants to set $\lambda \ : = \ : 0$ and compute the matrix

$$
\mathbf { C } \equiv \mathbf { \alpha } \mathbf { \alpha } ^ { - 1 }
$$

which, as before, is the estimated covariance matrix of the standard errors in the fitted parameters a (see next section).

The following object, Fitmrq, implements Marquardt’s method for nonlinear parameter estimation. The user interface is intentionally very close to that of Fitlin in $\ S 1 5 . 4$ . In particular, the feature of being able to freeze or unfreeze chosen parameters is available here, too.

One difference from Fitlin is that you have to supply an initial guess for the parameters a. Now that is a can of worms! When you are fitting for parameters that enter highly nonlinearly, there is no reason in the world that the $\chi ^ { 2 }$ surface should have only a single minimum. Marquardt’s method embodies no magical insight into finding the global minimum; it’s just a downhill search. Often, it should be the endgame strategy for fitting parameters, preceded by perhaps cruder, and likely problem-specific, methods for getting into the right general basin of convergence.

Another difference between Fitmrq and Fitlin is the format of the usersupplied function funks. Since Fitmrq needs both function and gradient values, funks is now coded as a void function returning answers through arguments passed by reference. An example is given below. You call Fitmrq’s constructor once, to bind your data vectors and function. Then (after any optional calls to hold or free) you call fit, which sets values for a, chisq, and covar. The curvature matrix alpha is also available. Note that the original vector of parameter guesses that you send to the constructor is not modified; rather, the answer is returned in a.

# struct Fitmrq {

Object for nonlinear least-squares fitting by the Levenberg-Marquardt method, also including the ability to hold specified parameters at fixed, specified values. Call constructor to bind data vectors and fitting functions and to input an initial parameter guess. Then call any combination of hold, free, and fit as often as desired. fit sets the output quantities a, covar, alpha, and chisq.

static const Int NDONE $= 4$ , ITMAX $\equiv$ 1000; Convergence parameters.   
Int ndat, ma, mfit;   
VecDoub_I &x,&y,&sig;   
Doub tol;   
void (\*funcs)(const Doub, VecDoub_I &, Doub &, VecDoub_O &);   
VecBool ia;   
VecDoub a; Output values. a is the vector of fitted coefficients, MatDoub covar; covar is its covariance matrix, alpha is the cur-MatDoub alpha; vature matrix, and chisq is the value of $\chi ^ { 2 }$ for Doub chisq; the fit.

Fitmrq(VecDoub_I &xx, VecDoub_I &yy, VecDoub_I &ssig, VecDoub_I &aa, void funks(const Doub, VecDoub_I &, Doub &, VecDoub_O &), const Doub TOL=1.e-3) : ndat(xx.size()), ma(aa.size()), x(xx), y(yy), sig(ssig), tol(TOL), funcs(funks), ia(ma), alpha(ma,ma), a(aa), covar(ma,ma) {

Constructor. Binds references to the data arrays xx, yy, and ssig, and to a user-supplied function funks that calculates the nonlinear fitting function and its derivatives. Also inputs the initial parameters guess aa (which is copied, not modified) and an optional convergence tolerance TOL. Initializes all parameters as free (not held).

for (Int $\scriptstyle \dot { 1 } = 0$ ;i<ma;i++) ia[i] $=$ true;

void hold(const Int i, const Doub val) {ia[i] $=$ false; a[i] $=$ val;} void free(const Int i) {ia[i] $=$ true;}

Optional functions for holding a parameter, identified by a value i in the range $0 , \ldots , \mathtt { m a - 1 }$ , fixed at the value val, or for freeing a parameter that was previously held fixed. hold and free may be called for any number of parameters before calling fit to calculate best-fit values for the remaining (not held) parameters, and the process may be repeated multiple times.

# void fit() {

Iterate to reduce the $\chi ^ { 2 }$ of a fit between a set of data points x[0..ndat-1], y[0..ndat-1] with individual standard deviations sig[0..ndat-1], and a nonlinear function that depends on ma coefficients a[0..ma-1]. When $\chi ^ { 2 }$ is no longer decreasing, set best-fit values for the parameters a[0..ma-1], and chisq $= \chi ^ { 2 }$ , covar[0..ma-1][0..ma-1], and alpha[0..ma-1][0..ma-1]. (Parameters held fixed will return zero covariances.)

Int j,k,l,iter,done $\mathtt { \mathtt { = 0 } }$ ;   
Doub alamda=.001,ochisq;   
VecDoub atry(ma),beta(ma),da(ma);   
mfit=0;   
for (j ${ = } 0$ ;j<ma;j++) if (ia[j]) mfit++;   
MatDoub oneda(mfit,1), temp(mfit,mfit);   
mrqcof(a,alpha,beta); Initialization.   
for (j ${ = } 0$ ;j<ma; ${ \dot { \bf { J } } } ^ { + + }$ ) atry[j] $= a$ [j];   
ochisq=chisq;   
for (iter ${ \tt = } 0$ ;iter<ITMAX;iter $^ { + + }$ ) { if (done $= =$ NDONE) alamda $_ { = 0 }$ .; Last pass. Use zero alamda. for (j ${ = } 0$ ;j<mfit;j++) { Alter linearized fitting matrix, by augmenting difor ( $\scriptstyle \mathbf { k } = 0$ ;k<mfit;k++) covar[j][k] $=$ alpha[j][k]; agonal elements. covar[j][j] $=$ alpha[j][j] $^ *$ (1.0+alamda); for ( $\scriptstyle \mathbf { k } = 0$ ;k<mfit;k++) temp[j][k] $=$ covar[j][k]; oneda[j][0] $\ c =$ beta[j]; } gaussj(temp,oneda); Matrix solution. for (j ${ = } 0$ ;j<mfit;j++) { for ( $\scriptstyle \mathbf { k } = 0$ ;k<mfit;k++) covar[j][k] $=$ temp[j][k]; da[j] $=$ oneda[j][0]; if (done $\scriptstyle = =$ NDONE) { Converged. Clean up and return. covsrt(covar); covsrt(alpha); return; for (j=0,l=0;l<ma; $^ { 1 + + }$ ) Did the trial succeed? if (ia[l]) atry[l] $= a$ [l] $^ +$ da[j++]; mrqcof(atry,covar,da); if (abs(chisq-ochisq) $<$ MAX(tol,tol\*chisq)) done++; if (chisq $<$ ochisq) { Success, accept the new solution. alamda $* = ~ 0 , 1$ ; ochisq=chisq; for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<mfit;j $^ { + + }$ ) { for $\scriptstyle 1 = 0$ ;k<mfit;k++) alpha[j][k] $=$ covar[j][k]; beta[j] $=$ da[j]; } for ( $\scriptstyle \mathbf { 1 } = 0$ ;l<ma; $1 + +$ ) a[l] $=$ atry[l]; } else { Failure, increase alamda. alamda $* = \ 1 0 \lrcorner 0$ ; chisq=ochisq; }   
}   
throw("Fitmrq too many iterations");

void mrqcof(VecDoub_I &a, MatDoub_O &alpha, VecDoub_O &beta) { Used by fit to evaluate the linearized fitting matrix alpha, and vector beta as in (15.5.8), and to calculate $\chi ^ { 2 }$ .

Int i,j,k,l,m;   
Doub ymod,wt,sig2i,dy;   
VecDoub dyda(ma);   
for ( $\scriptstyle \mathrm { j = 0 }$ ;j<mfit;j++) { Initialize (symmetric) alpha, beta. for $\scriptstyle \mathbf { k } = 0$ ;k $\cdot < =$ j; $\mathrm { k } { + + }$ ) alpha[j][k] ${ = } 0$ .0; beta[j] ${ = } 0$ .;   
}   
chisq ${ = } 0$ .;   
for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<ndat; $\dot { \bf 1 } + + \dot { }$ ) { Summation loop over all data. funcs(x[i],a,ymod,dyda); sig2i $= 1$ .0/(sig[i]\*sig[i]); dy=y[i]-ymod; for (j=0,l=0;l<ma;l++) { if (ia[l]) { wt=dyda[l]\*sig2i; for $\scriptstyle ( \mathtt { k } = 0$ , $\mathtt { m } = 0$ ;m<l+1;m++) if (ia[m]) alpha[j][k $\cdot + + ]$ $+ =$ wt\*dyda[m]; beta[j++] $+ =$ dy\*wt; } } chisq $+ =$ dy\*dy\*sig2i; And find $\chi ^ { 2 }$ .   
}   
for (j=1;j<mfit;j++) Fill in the symmetric side. for $( \mathtt { k } = 0$ ;k<j;k $^ { + + }$ ) alpha[k][j] $=$ alpha[j][k];

# void covsrt(MatDoub_IO &covar) {

Expand in storage the covariance matrix covar, so as to take into account parameters that are being held fixed. (For the latter, return zero covariances.)

Int i,j,k; for (i=mfit;i<ma; $\dot { \bar { \lambda } } + +$ ) for ( $\scriptstyle \mathbf { j } = 0$ ;j $< \dot { 1 } + 1$ ;j++) covar[i][j] $=$ covar[j][i]=0.0; $\mathrm { k } =$ mfit-1; for (j=ma-1;j>=0;j--) { if (ia[j]) { for (i=0;i<ma; $\dot { \bar { \lambda } } + +$ ) SWAP(covar[i][k],covar[i][j]); for (i=0;i<ma;i++) SWAP(covar[k][i],covar[j][i]); k--; } } }

};

# 15.5.3 Example

The following function fgauss is an example of a user-supplied function funks. Used with Fitmrq, it fits for the model

$$
y ( x ) = \sum _ { k = 0 } ^ { K - 1 } B _ { k } \exp \biggl [ - \biggl ( \frac { x - E _ { k } } { G _ { k } } \biggr ) ^ { 2 } \biggr ]
$$

which is a sum of $K$ Gaussians, each with a variable position, amplitude, and width.   
We store the parameters in the order $B _ { 0 } , E _ { 0 } , G _ { 0 } , B _ { 1 } , E _ { 1 } , G _ { 1 } , . . . , B _ { K - 1 } , E _ { K - 1 }$ ;   
$G _ { K - 1 }$ .

void fgauss(const Doub x, VecDoub_I &a, Doub &y, VecDoub_O &dyda) { $y ( x ; a )$ is the sum of na/3 Gaussians (15.5.16). The amplitude, center, and width of the Gaussians are stored in consecutive locations of a: $\mathsf { a } [ 3 k ] = B _ { k }$ , $\mathsf { a } [ 3 k + 1 ] = E _ { k }$ , $\mathtt { a } [ 3 k + 2 ] =$ $G _ { k }$ , $k = 0 , . . . , \mathtt { n a } / 3 - 1$ . The dimensions of the arrays are a[0..na-1], dyda[0..na-1].

Int i,na=a.size();   
Doub fac,ex,arg;   
$\scriptstyle { \mathtt { y } } = 0$ .;   
for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<na-1; $\dot { 1 } + = 3$ ) { arg=(x-a[i+1])/a[i+2]; ex=exp(-SQR(arg));

# fit examples.h

fac $= \mathtt { a }$ [i]\*ex\*2.\*arg; y $+ =$ a[i]\*ex; dyda[i] $=$ ex; dyda[i+1] $=$ fac/a[i+2]; dyda[i+2] $=$ fac\*arg/a[i+2]; }

# 15.5.4 More Advanced Methods for Nonlinear Least Squares

You will need more capability than Fitmrq can supply if either (i) it is converging too slowly, or (ii) it is converging to a local minimum that is not the one you want. Several options are available.

NL2SOL [3] is a highly regarded nonlinear least-squares implementation with many advanced features. For example, it keeps the second-derivative term we dropped in the Levenberg-Marquardt method whenever it would be better to do so, a so-called full Newton-type method.

A different variant on the Levenberg-Marquardt algorithm is to implement it as a model-trust region method for minimization (see $\ S 9 . 7$ and ref. [2]) applied to the special case of a least-squares function. A code of this kind due to More´ [4] can be found in MINPACK [5].

# CITED REFERENCES AND FURTHER READING:

Bevington, P.R., and Robinson, D.K. 2002, Data Reduction and Error Analysis for the Physical Sciences, 3rd ed. (New York: McGraw-Hil), Chapter 8.   
Monahan, J.F. 2001, Numerical Methods of Statistics (Cambridge, UK: Cambridge University Press), Chapters 5–9.   
Seber, G.A.F., and Wild, C.J. 2003, Nonlinear Regression (Hoboken, NJ: Wiley).   
Gelman, A., Carlin, J.B., Stern, H.S., and Rubin, D.B. 2004, Bayesian Data Analysis, 2nd ed. (Boca Raton, FL: Chapman & Hall/CRC).   
Jacobs, D.A.H. (ed.) 1977, The State of the Art in Numerical Analysis (London: Academic Press), Chapter III.2 (by J.E. Dennis).   
Marquardt, D.W. 1963, Journal of the Society for Industrial and Applied Mathematics, vol. 11, pp. 431–441.[1]   
Dennis, J.E., and Schnabel, R.B. 1983, Numerical Methods for Unconstrained Optimization and Nonlinear Equations; reprinted 1996 (Philadelphia: S.I.A.M.).[2]   
Dennis, J.E., Gay, D.M, and Welsch, R.E. 1981, “An Adaptive Nonlinear Least-Squares Algorithm,” ACM Transactions on Mathematical Software, vol. 7, pp. 348–368; op. cit., pp. 369– 383.[3].   
Moré, J.J. 1977, in Numerical Analysis, Lecture Notes in Mathematics, vol. 630, G.A. Watson, ed. (Berlin: Springer), pp. 105–116.[4]   
Moré, J.J., Garbow, B.S., and Hillstrom, K.E. 1980, User Guide for MINPACK-1, Argonne National Laboratory Report ANL-80-74.[5]

# 15.6 Confidence Limits on Estimated Model Parameters

Several times already in this chapter we have made statements about the standard errors, or uncertainties, in a set of $M$ estimated parameters a. We have given some formulas for computing standard deviations or variances of individual parameters (equations 15.2.9, 15.4.15, and 15.4.19), as well as some formulas for covariances between pairs of parameters (equation 15.2.10; remark following equation 15.4.15; equation 15.4.20; equation 15.5.15).

In this section, we want to be more explicit regarding the precise meaning of these quantitative uncertainties, and to give further information about how quantitative confidence limits on fitted parameters can be estimated. The subject can get somewhat technical, and even somewhat confusing, so we will try to make precise statements, even when they must be offered without proof.

Figure 15.6.1 shows the conceptual scheme of an experiment that “measures” a set of parameters. There is some underlying true set of parameters $\mathbf { a } _ { \mathrm { t r u e } }$ that are known to Mother Nature but hidden from the experimenter. These true parameters are statistically realized, along with random measurement errors, as a measured data set, which we will symbolize as ${ \mathcal { D } } _ { ( 0 ) }$ . The data set ${ \mathcal { D } } _ { ( 0 ) }$ is known to the experimenter. He or she fits the data to a model by $\chi ^ { 2 }$ minimization or some other technique and obtains measured, i.e., fitted, values for the parameters, which we here denote a.0/.

Because measurement errors have a random component, ${ \mathcal { D } } _ { ( 0 ) }$ is not a unique realization of the true parameters $\mathbf { a _ { \mathrm { t r u e } } }$ . Rather, there are infinitely many other realizations of the true parameters as “hypothetical data sets” each of which could have been the one measured, but happened not to be. Let us symbolize these by $\mathcal { D } _ { ( 1 ) } , \mathcal { D } _ { ( 2 ) } , \ldots .$ . Each one, had it been realized, would have given a slightly different set of fitted parameters, ${ \bf a } _ { ( 1 ) } , { \bf a } _ { ( 2 ) } , \dots .$ , respectively. These parameter sets $\mathbf { a } _ { ( i ) }$ therefore occur with some probability distribution in the $M$ -dimensional space of all possible parameter sets a. The actual measured set ${ \bf a } _ { ( 0 ) }$ is one member drawn from this distribution.

Even more interesting than the probability distribution of $\mathbf { a } _ { ( i ) }$ would be the distribution of the difference $\mathbf { a } _ { ( i ) } - \mathbf { a } _ { \mathrm { t r u e } }$ . This distribution differs from the former one by a translation that puts Mother Nature’s true value at the origin. If we knew this distribution, we would know everything that there is to know about the quantitative uncertainties in our experimental measurement ${ \bf a } _ { ( 0 ) }$ .

So the name of the game is to find some way of estimating or approximating the probability distribution of $\mathbf { a } _ { ( i ) } - \mathbf { a } _ { \mathrm { t r u e } }$ without knowing $\mathbf { a } _ { \mathrm { t r u e } }$ and without having available to us an infinite universe of hypothetical data sets.

# 15.6.1 Monte Carlo Simulation of Synthetic Data Sets

Although the measured parameter set ${ \bf a } _ { ( 0 ) }$ is not the true one, let us consider a fictitious world in which it was the true one. Since we hope that our measured parameters are not too wrong, we hope that that fictitious world is not too different from the actual world with parameters $\mathbf { a } _ { \mathrm { t r u e } }$ . In particular, let us hope — no, let us assume — that the shape of the probability distribution $\mathbf { a } _ { ( i ) } - \mathbf { a } _ { ( 0 ) }$ in the fictitious world is the same, or very nearly the same, as the shape of the probability distribution $\mathbf { a } _ { ( i ) } - \mathbf { a } _ { \mathrm { t r u e } }$ in the real world. Notice that we are not assuming that ${ \bf a } _ { ( 0 ) }$ and $\mathbf { a } _ { \mathrm { t r u e } }$ are equal; they are certainly not. We are only assuming that the way in which random errors enter the experiment and data analysis does not vary rapidly as a function of $\mathbf { a } _ { \mathrm { t r u e } }$ , so that ${ \bf a } _ { ( 0 ) }$ can serve as a reasonable surrogate.

![](images/992c3948e54500e501df9c61639eabb29072fb4adbb5ea721254afae90d7ee64.jpg)  
Figure 15.6.1. A statistical universe of data sets from an underlying model. True parameters $\mathbf { a } _ { \mathrm { ~ t r u e ~ } }$ are realized in a data set, from which fitted (observed) parameters ${ \bf a } _ { ( 0 ) }$ are obtained. If the experiment were repeated many times, new data sets and new values of the fitted parameters would be obtained.

Now, often, the distribution of $\mathbf { a } _ { ( i ) } - \mathbf { a } _ { ( 0 ) }$ in the fictitious world is within our power to calculate (see Figure 15.6.2). If we know something about the process that generated our data, given an assumed set of parameters ${ \bf a } _ { ( 0 ) }$ , then we can usually figure out how to simulate our own sets of “synthetic” realizations of these parameters as “synthetic data sets.” The procedure is to draw random numbers from appropriate distributions (cf. $\ S 7 . 3 - \ S 7 . 4 )$ so as to mimic our best understanding of the underlying process and measurement errors in our apparatus. With such random draws, we construct data sets with exactly the same numbers of measured points, and precisely the same values of all control (independent) variables, as our actual data set ${ \mathcal { D } } _ { ( 0 ) }$ . Let us call these simulated data sets $\mathcal { \hat { D } } _ { . } ^ { S } ( 1 ) , \mathcal { D } _ { \underline { { ( 2 ) } } , \cdot } ^ { S } \dots .$ By construction, these are supposed to have exactly the same statistical relationship to ${ \bf a } _ { ( 0 ) }$ as the $\mathcal { D } _ { ( i ) }$ ’s have to $\mathbf { a } _ { \mathrm { t r u e } }$ . (For the case where you don’t know enough about what you are measuring to do a credible job of simulating it, see below.)

Next, for each $\mathcal { D } _ { ( j ) } ^ { S }$ , perform exactly the same procedure for estimation of parameters,rameters ${ \bf a } _ { ( 0 ) }$ $\chi ^ { 2 }$ minimization, as was performed oing simulated measured parameters $\mathbf { a } _ { ( 1 ) } ^ { S } , \mathbf { a } _ { ( 2 ) } ^ { S } , \ldots .$ ta to get the pa- Each simulated measured parameter set yields a point $\mathbf { a } _ { ( i ) } ^ { S } - \mathbf { a } _ { ( 0 ) }$ . Simulate enough data sets and enough derived simulated measured parameters, and you map out the desired probability distribution in $M$ dimensions.

![](images/6d66a2b7abcd3f61634737826edd78c254272e53f298cf1a4f493fcdb3833745.jpg)  
Figure 15.6.2. Monte Carlo simulation of an experiment. The fitted parameters from an actual experiment are used as surrogates for the true parameters. Computer-generated random numbers are used to simulate many synthetic data sets. Each of these is analyzed to obtain its fitted parameters. The distribution of these fitted parameters around the (known) surrogate true parameters is thus studied.

In fact, the ability to do Monte Carlo simulations in this fashion has revolutionized many fields of modern experimental science. Not only is one able to characterize the errors of parameter estimation in a very precise way; one can also try out on the computer different methods of parameter estimation, or different data reduction techniques, and seek to minimize the uncertainty of the result according to any desired criteria. Offered the choice between mastery of a five-foot shelf of analytical statistics books and middling ability at performing statistical Monte Carlo simulations, we would surely choose to have the latter skill.

# 15.6.2 Quick-and-Dirty Monte Carlo: The Bootstrap Method

Here is a powerful technique that can often be used when you don’t know enough about the underlying process, or the nature of your measurement errors, to do a credible Monte Carlo simulation. Suppose that your data set consists of $N$ independent and identically distributed (or iid) “data points.” Each data point probably consists of several numbers, e.g., one or more control variables (uniformly distributed, say, in the range that you have decided to measure) and one or more associated measured values (each distributed however Mother Nature chooses). “Iid” means that the sequential order of the data points is not of consequence to the process that you are using to get the fitted parameters a. For example, a $\chi ^ { 2 }$ sum like (15.5.5) does not care in what order the points are added. Even simpler examples are the mean value of a measured quantity and the mean of some function of the measured quantities.

The bootstrap method [1] uses the actual data set ${ \mathcal { D } } _ { ( 0 ) } ^ { S }$ , with its $N$ data points, to generate any number of synthetic data sets DS.1/; $\mathcal { D } _ { ( 1 ) } ^ { S } , \mathcal { D } _ { ( 2 ) } ^ { S } , \ldots ,$ D S.2/; : : : , also with N data points. The procedure is simply to draw $N$ data points at a time with replacement from the set D S.0/. Because of the replacement, you do not simply get back your original data set each time. You get sets in which a random fraction of the original points, typically $\sim 1 / e \approx 3 7 \%$ , are replaced by duplicated original points. Now, exactly as in the previous discussion, you subject these data sets to the same estimation procedure as $\mathbf { a } _ { ( 1 ) } ^ { S } , \mathbf { \bar { a } } _ { ( 2 ) } ^ { S } , \ldots .$ d on the actual data, giving a set These will be distributed around ${ \bf a } _ { ( 0 ) }$ imulated measured parametersin close to the same way that ${ \bf a } _ { ( 0 ) }$ is distributed around $\mathbf { a } _ { \mathrm { t r u e } }$ .

Sounds like getting something for nothing, doesn’t it? In fact, it took a while for the bootstrap method to become accepted by statisticians. By now, however, enough theorems have been proved to render the bootstrap reputable (see [2] for references). The basic idea behind the bootstrap is that the actual data set, viewed as a probability distribution consisting of delta functions at the measured values, is in most cases the best — or only — available estimator of the underlying probability distribution. It takes courage, but one can often simply use that distribution as the basis for Monte Carlo simulations.

Watch out for cases where the bootstrap’s iid assumption is violated. For example, if you have made measurements at evenly spaced intervals of some control variable, then you can usually get away with pretending that these are iid uniformly distributed over the measured range. However, some estimators of a (e.g., ones involving Fourier methods) might be particularly sensitive to all the points on a grid being present. In that case, the bootstrap is going to give a wrong distribution. Also watch out for estimators that look at anything like small-scale clumpiness within the $N$ data points, or estimators that sort the data and look at sequential differences. Obviously the bootstrap will fail on these, too. (The theorems justifying the method are still true, but some of their technical assumptions are violated by these examples.)

For a large class of problems, however, the bootstrap does yield easy, very quick, Monte Carlo estimates of the errors in an estimated parameter set.

# 15.6.3 Confidence Limits

Rather than present all details of the probability distribution of errors in parameter estimation, it is common practice to summarize the distribution in the form of confidence limits. The full probability distribution is a function defined on the $M$ - dimensional space of parameters a. A confidence region (or confidence interval) is just a region of that $M$ -dimensional space (hopefully a small region) that contains a certain (hopefully large) percentage of the total probability distribution. You point to a confidence region and say, e.g., “there is a $9 9 \%$ chance that the true parameter values fall within this region around the measured value.”

It is worth emphasizing that you, the experimenter, get to pick both the confidence level $9 9 \%$ in the above example) and the shape of the confidence region. The only requirement is that your region does include the stated percentage of probability. Certain percentages are, however, customary in scientific usage: $6 8 . 3 \%$ (the lowest confidence worthy of quoting), $90 \%$ , $9 5 . 4 \%$ , $9 9 \%$ , and $9 9 . 7 3 \%$ . Higher confidence levels are conventionally “ninety-nine point nine : : : nine.” As for shape, obviously you want a region that is compact and reasonably centered on your measurement a.0/, since the whole purpose of a confidence limit is to inspire confidence in that measured value. In one dimension, the convention is to use a line segment centered on the measured value; in higher dimensions, ellipses or ellipsoids are most frequently used.

![](images/2b413c77c2f7a4ef4501f9b60abcabaa2ee7f3f9a31e011a3d25ee75a7cdd12e.jpg)  
Figure 15.6.3. Confidence intervals in one and two dimensions. The same fraction of measured points (here $6 8 \%$ ) lies (i) between the two vertical lines, (ii) between the two horizontal lines, (iii) within the ellipse.

You might suspect, correctly, that the numbers $6 8 . 3 \%$ , $9 5 . 4 \%$ , and $9 9 . 7 3 \%$ and the use of ellipsoids, have some connection with a normal distribution. That is true historically, but not always relevant nowadays. In general, the probability distribution of the parameters will not be normal, and the above numbers, used as levels of confidence, are purely matters of convention.

Figure 15.6.3 sketches a possible probability distribution for the case $M = 2$ . Shown are three different confidence regions that might usefully be given, all at the same confidence level. The two vertical lines enclose a band (horizontal interval) that represents the $68 \%$ confidence interval for the variable $a _ { 0 }$ without regard to the value of $a _ { 1 }$ . Similarly the horizontal lines enclose a $68 \%$ confidence interval for $a _ { 1 }$ . The ellipse shows a $68 \%$ confidence interval for $a _ { 0 }$ and $a _ { 1 }$ jointly. Notice that to enclose the same probability as the two bands, the ellipse must necessarily extend outside of both of them (a point we will return to below).

# 15.6.4 Constant Chi-Square Boundaries as Confidence Limits

When the method used to estimate the parameters ${ \bf a } _ { ( 0 ) }$ is chi-square minimization, as in the previous sections of this chapter, then there is a natural choice for the shape of confidence intervals, whose use is almost universal. For the observed data set ${ \mathcal { D } } _ { ( 0 ) }$ , the value of $\chi ^ { 2 }$ is a minimum at ${ \bf a } _ { ( 0 ) }$ . Call this minimum value $\chi _ { \mathrm { m i n } } ^ { 2 }$ . If the vector a of parameter values is perturbed away from ${ \bf a } _ { ( 0 ) }$ , then $\chi ^ { 2 }$ increases. The region within which $\chi ^ { 2 }$ increases by no more than a set amount $\Delta \chi ^ { 2 }$ defines some $M$ -dimensional confidence region around ${ \bf a } _ { ( 0 ) }$ . If $\Delta \chi ^ { 2 }$ is set to be a large number, this will be a big region; if it is small, it will be small. Somewhere in between there will be choices of $\Delta \chi ^ { 2 }$ that cause the region to contain, variously, $68 \%$ , $90 \%$ , etc., of probability distribution for a’s, as defined above. These regions are taken as the confidence regions for the parameters ${ \bf a } _ { ( 0 ) }$ .

Very frequently one is interested not in the full $M$ -dimensional confidence region, but in individual confidence regions for some smaller number $\nu$ of parameters. For example, one might be interested in the confidence interval of each parameter taken separately (the bands in Figure 15.6.3), in which case $\nu = 1$ . In that case, the natural confidence regions in the $\nu$ -dimensional subspace of the $M$ -dimensional parameter space are the projections of the $M$ -dimensional regions defined by fixed $\Delta \chi ^ { 2 }$ into the $\nu$ -dimensional spaces of interest. In Figure 15.6.4, for the case $M = 2$ , we show regions corresponding to several values of $\Delta \chi ^ { 2 }$ . The one-dimensional confidence interval in $a _ { 1 }$ corresponding to the region bounded by $\Delta \chi ^ { 2 } = 1$ lies between the lines $A$ and $A ^ { \prime }$ .

Note that it is the projection of the higher-dimensional region on the lowerdimension space that is used, not the intersection. The intersection would be the band between $Z$ and $Z ^ { \prime }$ . It is never used. It is shown in the figure only for the purpose of making this cautionary point, that it should not be confused with the projection.

# 15.6.5 Probability Distribution of Parameters in the Normal Case

You may be wondering why we have, in this section up to now, made no connection at all with the error estimates that come out of the $\chi ^ { 2 }$ fitting procedure, most notably the covariance matrix $C _ { i j }$ . The reason is this: $\chi ^ { 2 }$ minimization is a useful means for estimating parameters even if the measurement errors are not normally distributed. While normally distributed errors are required if the $\chi ^ { 2 }$ parameter estimate is to be a maximum likelihood estimator (-15.1), one is often willing to give up that property in return for the relative convenience of the $\chi ^ { 2 }$ procedure. Only in extreme cases, i.e., measurement error distributions with very large “tails,” is $\chi ^ { 2 }$ minimization abandoned in favor of more robust techniques, as will be discussed in $\ S 1 5 . 7$ .

However, the formal covariance matrix that comes out of a $\chi ^ { 2 }$ minimization has a clear quantitative interpretation only if (or to the extent that) the measurement errors actually are normally distributed. In the case of nonnormal errors, you are “allowed”

- to fit for parameters by minimizing $\chi ^ { 2 }$ $\bullet$ to use a contour of constant $\Delta \chi ^ { 2 }$ as the boundary of your confidence region - to use Monte Carlo simulation or detailed analytic calculation in determining

![](images/d20a86242dc7994edcc2600b06b3c53bbe3874c740f210124dd5e6a6f077c907.jpg)  
Figure 15.6.4. Confidence region ellipses corresponding to values of chi-square larger than the fitted minimum. The solid curves, with $\Delta \chi ^ { 2 } = 1 . 0 0 , 2 . 7 1 , 6 . 6 3$ , project onto one-dimensional intervals $A A ^ { \prime }$ , $B B ^ { \prime }$ , $C C ^ { \prime }$ . These intervals — not the ellipses themselves — contain $6 8 . 3 \%$ , $90 \%$ , and $9 9 \%$ of normally distributed data. The ellipse that contains $6 8 . 3 \%$ of normally distributed data is shown dashed and has $\dot { \Delta x ^ { 2 } } = 2 . 3 0$ . For additional numerical values, see the table on p. 815.

which contour $\Delta \chi ^ { 2 }$ is the correct one for your desired confidence level - to give the covariance matrix $C _ { i j }$ as the “formal covariance matrix of the fit.”

You are not allowed

- to use formulas that we now give for the case of normal errors, which establish quantitative relationships among $\Delta \chi ^ { 2 }$ , $C _ { i j }$ , and the confidence level.

Here are the key theorems that hold when (i) the measurement errors are normally distributed, and either (ii) the model is linear in its parameters or (iii) the sample size is large enough that the uncertainties in the fitted parameters a do not extend outside a region in which the model could be replaced by a suitable linearized model. [Note that condition (iii) does not preclude your use of a nonlinear routine like Fitmrq to find the fitted parameters.]

Theorem A. $\chi _ { \mathrm { m i n } } ^ { 2 }$ is distributed as a chi-square distribution with $N - M$ degrees of freedom, where $N$ is the number of data points and $M$ is the number of fitted parameters. This is the basic theorem that lets you evaluate the goodness-of-fit of the model, as discussed above in $\ S 1 5 . 1$ . We list it first to remind you that unless the goodness-of-fit is credible, the whole estimation of parameters is suspect.

Theorem $B$ . If $\mathbf { a } _ { ( j ) } ^ { S }$ is drawn from the universe of simulated data sets with actual parameters ${ \bf a } _ { ( 0 ) }$ , then the probability distribution of $\delta \mathbf { a } \equiv \mathbf { a } _ { ( j ) } ^ { S } - \mathbf { a } _ { ( 0 ) }$ is the multivariate normal distribution

$$
P ( \delta { \bf a } ) d a _ { 0 } \ldots d a _ { M - 1 } = \mathrm { c o n s t . } \times \exp \left( - { \textstyle { \frac { 1 } { 2 } } } \delta { \bf a } \cdot \alpha \cdot \delta { \bf a } \right) d a _ { 0 } \ldots d a _ { M - 1 }
$$

where $\pmb { \alpha }$ is the curvature matrix defined in equation (15.5.8).

Theorem $C _ { ☉ }$ . If $\mathbf { a } _ { ( j ) } ^ { S }$ is drawn from the universe of simulated data sets with actual parameters ${ \bf a } _ { ( 0 ) }$ , then the quantity $\Delta \chi ^ { 2 } \equiv \chi ^ { 2 } ( \mathbf { a } _ { ( j ) } ) - \chi ^ { 2 } ( \mathbf { a } _ { ( 0 ) } )$ is distributed as a chi-square distribution with $M$ degrees of freedom. Here the $\chi ^ { 2 }$ ’s are all evaluated using the fixed (actual) data set ${ \mathcal { D } } _ { ( 0 ) }$ . This theorem makes the connection between particular values of $\Delta \chi ^ { 2 }$ and the fraction of the probability distribution that they enclose as an $M$ -dimensional region, i.e., the confidence level of the $M$ -dimensional confidence region.

Theorem $D$ . Suppose that $\mathbf { a } _ { ( j ) } ^ { S }$ is drawn from the universe of simulated data sets (as above); that its first $\nu$ components $a _ { 0 } , \ldots , a _ { \nu - 1 }$ are held fixed; and that its maialue $M - \nu$ aried so as to minimize is distributed as a chi- $\chi ^ { 2 }$ . Call this minimumare distribution with $\chi _ { \nu } ^ { 2 }$ $\Delta \chi _ { \nu } ^ { 2 } \equiv \chi _ { \nu } ^ { 2 } - \chi _ { \mathrm { m i n } } ^ { 2 }$ $\nu$ connects the projected $\Delta \chi ^ { 2 }$ region with a confidence level. In the figure, a point that is held fixed in $a _ { 1 }$ and allowed to vary in $a _ { 0 }$ minimizing $\chi ^ { 2 }$ will seek out the ellipse whose top or bottom edge is tangent to the line of constant $a _ { 1 }$ , and is therefore the line that projects it onto the smaller-dimensional space.

As a first example, let us consider the case $\nu ~ = ~ 1$ , where we want to find the confidence interval of a single parameter, say $a _ { 0 }$ . Notice that the chi-square distribution with $\nu = 1$ degree of freedom is the same distribution as that of the square of a single normally distributed quantity. Thus $\Delta \chi _ { \nu } ^ { 2 } < 1$ occurs $6 8 . 3 \%$ of the time ( $1 \AA ^ { - \sigma }$ for the normal distribution), $\Delta \chi _ { \nu } ^ { 2 } < 4$ occurs $9 5 . 4 \%$ of the time ( $2 \sigma$ for the normal distribution), $\Delta \chi _ { \nu } ^ { 2 } < 9$ occurs $9 9 . 7 3 \%$ of the time $3 \cdot \sigma$ for the normal distribution), etc. In this manner you find the $\Delta \chi _ { \nu } ^ { 2 }$ that corresponds to your desired confidence level. (Additional values are given in the table on the next page.)

Let $\delta \mathbf { a }$ be a change in the parameters whose first component is arbitrary, $\delta \boldsymbol { a } _ { 0 }$ , but the rest of whose components are chosen to minimize the $\Delta \chi ^ { 2 }$ . Then Theorem D applies. The value of $\Delta \chi ^ { 2 }$ is given in general by

$$
\Delta \chi ^ { 2 } = \delta \mathbf { a } \cdot \boldsymbol { \alpha } \cdot \delta \mathbf { a }
$$

which follows from equation (15.5.8) applied at $\chi _ { \mathrm { m i n } } ^ { 2 }$ where $\beta _ { k } \ = \ 0$ . Since ıa by hypothesis minimizes $\chi ^ { 2 }$ in all but its zeroth component, components 1 through $M - 1$ of the normal equations (15.5.9) continue to hold. Therefore, the solution of (15.5.9) is

$$
\delta \mathbf { a } = { \boldsymbol { \alpha } } ^ { - 1 } \cdot { \left( \begin{array} { l } { c } \\ { 0 } \\ { \vdots } \\ { 0 } \end{array} \right) } = \mathbf { C } \cdot { \left( \begin{array} { l } { c } \\ { 0 } \\ { \vdots } \\ { 0 } \end{array} \right) }
$$

where $c$ is one arbitrary constant that we get to adjust to make (15.6.1) give the desired left-hand value. Plugging (15.6.2) into (15.6.1) and using the fact that $\mathbf { C }$ and $\pmb { \alpha }$ are inverse matrices of one another, we get

$$
c = \delta a _ { 0 } / C _ { 0 0 } \qquad \mathrm { a n d } \qquad \Delta \chi _ { \nu } ^ { 2 } = ( \delta a _ { 0 } ) ^ { 2 } / C _ { 0 0 }
$$

<table><tr><td colspan="5">△x² as a Function of Confidence Level p and Number of Parameters of Interest v</td></tr><tr><td>P</td><td colspan="3">V 1 2 3 4</td><td>5 6</td></tr><tr><td>68.27%</td><td>1.00 2.30</td><td>3.53</td><td>4.72</td><td>5.89 7.04</td></tr><tr><td>90%</td><td>2.71 4.61</td><td>6.25</td><td>7.78 9.24</td><td>10.6</td></tr><tr><td>95.45%</td><td>4.00 6.18</td><td>8.02</td><td>9.72</td><td>11.3 12.8</td></tr><tr><td>99%</td><td>6.63 9.21</td><td>11.3</td><td>13.3</td><td>15.1 16.8</td></tr><tr><td>99.73%</td><td>9.00 11.8</td><td>14.2</td><td>16.3 18.2</td><td>20.1</td></tr><tr><td>99.99%</td><td>15.1 18.4</td><td>21.1</td><td>23.5</td><td>25.7 27.9</td></tr></table>

$$
\delta a _ { 0 } = \pm \sqrt { \Delta \chi _ { \nu } ^ { 2 } } \sqrt { C _ { 0 0 } }
$$

At last! A relation between the confidence interval $\pm \delta a _ { 0 }$ and the formal standard error $\sigma _ { 0 } \equiv \sqrt { C _ { 0 0 } }$ . Not unreasonably, we find that the $68 \%$ confidence interval is $\pm \sigma _ { 0 }$ , the $9 5 \%$ confidence interval is $\pm 2 \sigma _ { 0 }$ , etc.

These considerations hold not just for the individual parameters $a _ { i }$ , but also for any linear combination of them: If

$$
b \equiv \sum _ { k = 0 } ^ { M - 1 } c _ { i } a _ { i } = \mathbf { c } \cdot \mathbf { a }
$$

then the $68 \%$ confidence interval on $b$ is

$$
\delta b = \pm \sqrt { \mathbf { c } \cdot \mathbf { C } \cdot \mathbf { c } }
$$

However, these simple, normal-sounding numerical relationships do not hold in the case $\nu \ > \ 1$ [3]. In particular, $\Delta \chi ^ { 2 } ~ = ~ 1$ is not the boundary, nor does it project onto the boundary, of a $6 8 . 3 \%$ confidence region when $\nu > 1$ . If you want to calculate not confidence intervals in one parameter, but confidence ellipses in two parameters jointly, or ellipsoids in three, or higher, then you must follow the following prescription for implementing Theorems C and D above:

- Let $\nu$ be the number of fitted parameters whose joint confidence region you wish to display, $\nu \leq M$ . Call these parameters the “parameters of interest.”   
- Let $p$ be the confidence limit desired, e.g., $p = 0 . 6 8$ or $p = 0 . 9 5$ .   
- Find $\Delta$ (i.e., $\Delta \chi ^ { 2 }$ ) such that the probability of a chi-square variable with $\nu$ degrees of freedom being less than $\Delta$ is $p$ . For some useful values of $p$ and $\nu$ , $\Delta$ is given in the table above. For other values, you can use the invcdf method of the Chisqdist object in $\ S 6 . 1 4 . 8$ with $p$ as the argument.   
- Take the $M \times M$ covariance matrix $\mathbf { C _ { \lambda } } = \pmb { \alpha } ^ { - 1 }$ of the chi-square fit. Copy the intersection of the $\nu$ rows and columns corresponding to the parameters of interest into a $\nu \times \nu$ matrix denoted $\mathbf { C } _ { \mathrm { p r o j } }$ .   
- Invert the matrix $\mathbf { C } _ { \mathrm { p r o j } }$ . (In the one-dimensional case this was just taking the reciprocal of the element $C _ { 0 0 }$ .)

- The equation for the elliptical boundary of your desired confidence region in the $\nu$ -dimensional subspace of interest is

$$
\Delta = \delta \mathbf { a } ^ { \prime } \cdot \mathbf { C } _ { \mathrm { p r o j } } ^ { - 1 } \cdot \delta \mathbf { a } ^ { \prime }
$$

where ${ \boldsymbol { \delta } } \mathbf { a } ^ { \prime }$ is the $\nu$ -dimensional vector of parameters of interest.

If you are confused at this point, you may find it helpful to compare Figure 15.6.4 and the table on the previous page considering the case $M = 2$ with $\nu = 1$ and $\nu = 2$ . You should be able to verify the following statements: (i) The horizontal band between $C$ and $C ^ { \prime }$ contains $9 9 \%$ of the probability distribution, so it is a confidence limit on $a _ { 1 }$ alone at this level of confidence. (ii) Ditto the band between $B$ and $B ^ { \prime }$ at the $90 \%$ confidence level. (iii) The dashed ellipse, labeled by $\Delta \chi ^ { 2 } = 2 . 3 0$ , contains $6 8 . 3 \%$ of the probability distribution, so it is a confidence region for $a _ { 0 }$ and $a _ { 1 }$ jointly, at this level of confidence.

Another point of possible confusion might also be worth airing here. In $\ S 1 5 . 1 . 1$ , when we discussed the use of $\chi ^ { 2 }$ as a goodness-of-fit statistic, we mentioned that ap “moderately good” fit could have a $\chi ^ { 2 }$ value that differed by as much as $\pm \sqrt { 2 \nu }$ from its expected value $\nu$ (now the total number of degrees of freedom $N - M$ , not $\nu$ as used above). Indeed, the suggested tail probability that embodies this advice is $\mathcal { Q } = 1 - \mathtt { C h i s q d i s t } ( \nu ) .$ .invcdf $( \chi ^ { 2 } )$ . Yet, in the discussion above, we seem to be saying that small changes in $\chi ^ { 2 }$ , as little as $\pm 1$ or $\pm 2 . 7 1$ (see table on the previous page), are significant. Can both statements be true?

Yes. In $\ S 1 5 . 1 . 1$ we were considering the variation in $\chi ^ { 2 }$ over a population of hypothetical data sets with the same parameter values, p $\mathbf { a } _ { \mathrm { t r u e } }$ (cf. Figure 15.6.1). These values vary by typically $\pm \sqrt { 2 \nu }$ . By contrast, in the discussion above, we took a single data set and held it fixed. We then asked, essentially as an exercise in propagation of errors, how much uncertainty in the fitted parameter values $\mathbf { a } _ { 0 }$ was generated by the uncertainties in the data. One way to see that these are quite different concepts is to think about how they should each scale with $N$ , the number of data points. As $N$ gets large, $\chi ^ { 2 }$ scales as $N$ , while its variation over hypothetical data sets scales as $N ^ { 1 / 2 }$ , essentially a random walk. Now imagine a varying around its fitted value $\mathbf { a } _ { 0 }$ by a small amount, $\mathbf { a } = \mathbf { a } _ { 0 } + \boldsymbol { \delta } \mathbf { a }$ . The change in $\chi ^ { 2 }$ scales with the number of terms in the sum, $N$ , and quadratically with distance from the minimum,

$$
\delta \chi ^ { 2 } \propto N ( \delta \mathbf { a } ) ^ { 2 }
$$

As the number of data points increases, we reasonably expect the parameters to become more accurately determined, scaling as

$$
\delta \mathbf { a } \propto N ^ { - 1 / 2 }
$$

Combining these two equations, we find that $\delta \chi ^ { 2 }$ for the minimum significant change in parameters ${ \delta \bf a }$ scales as $N ^ { 0 }$ , that is, as a constant. In fact, Theorems B and C above tell us that this is not just reasonable expectation on our part; it is actually true.

# 15.6.6 Confidence Limits from Singular Value Decomposition

When you have obtained your $\chi ^ { 2 }$ fit by singular value decomposition (-15.4), the information about the fit’s formal errors comes packaged in a somewhat different,


<!-- chunk 0013: pages 841-910 -->
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


<!-- chunk 0014: pages 911-980 -->
and

$$
0 = \frac { \partial \mathcal { L } } { \partial b } = \sum _ { i } \alpha _ { i } y _ { i }
$$

Substituting equations (16.5.13) and (16.5.14) back into (16.5.12) gives the reduced Lagrangian

$$
\begin{array} { l } { { \displaystyle { \mathcal { L } } ( { \boldsymbol { \alpha } } ) = \sum _ { j } \alpha _ { j } - \frac { 1 } { 2 } \sum _ { j , k } \alpha _ { j } y _ { j } ( \mathbf { x } _ { j } \cdot \mathbf { x } _ { k } ) y _ { k } \alpha _ { k } } } \\ { { \displaystyle \equiv \mathbf { e } \cdot { \boldsymbol { \alpha } } - \frac { 1 } { 2 } { \boldsymbol { \alpha } } \cdot \mathrm { d i a g } ( \mathbf { y } ) \cdot { \mathbf { G } } \cdot \mathrm { d i a g } ( \mathbf { y } ) \cdot { \boldsymbol { \alpha } } } } \end{array}
$$

In the second form of the above equation we introduce some convenient matrix notation: e is the vector whose components are all unity, diag denotes a diagonal matrix formed from a vector in the obvious way, and $\mathbf { G }$ is the Gram matrix of dot products of all the $\mathbf { X } _ { j }$ ’s,

$$
G _ { i j } \equiv { \bf x } _ { i } \cdot { \bf x } _ { j }
$$

Remember that subscripts on $\mathbf { X }$ don’t indicate components, but rather index which data point is referenced.

The dual problem, in toto, thus turns out to be

<table><tr><td>minimize: subject to:</td><td>1α ·diag(y)·G·diag(y)·α-e·α αi&gt;0 for all i α·y=0 (from 16.5.14)</td></tr></table>

We also have the Karush-Kuhn-Tucker relation,

$$
\widehat { \alpha } _ { i } \left[ y _ { i } ( \widehat { \mathbf { w } } \cdot \mathbf { x } _ { i } + b ) - 1 \right] = 0
$$

Equation (16.5.13) tells how to get the optimal solution $\widehat { \mathbf { w } }$ of the primal problem from the solution $\widehat { \pmb { \alpha } }$ of the dual. Equation (16.5.18) is then used to get $\widehat { b }$ : Find any nonzero $\alpha _ { i }$ , then, with the corresponding $y _ { i } , \mathbf { x } _ { i }$ , and $\widehat { \mathbf { w } }$ , solve the above relation for $\widehat { b }$ . Alternatively, one can average out some roundoff error by taking a weighted average of $\alpha _ { i }$ ’s,

$$
\widehat { b } = \sum _ { i } \widehat { \alpha } _ { i } ( y _ { i } - \widehat { \mathbf { w } } \cdot \mathbf { x } _ { i } ) \Big / \sum _ { i } \alpha _ { i }
$$

Finally, the decision rule is $f ( \mathbf { x } ) = { \widehat { \mathbf { w } } } \cdot \mathbf { x } + { \widehat { b } }$ .

A few observations will become important later:

- Data points with nonzero $\widehat { \alpha } _ { i }$ satisfy the constraints as equalities, i.e., they are support vectors. The only place that the data $\mathbf { X } _ { i }$ ’s appear in (16.5.17) is in the Gram matrix $\mathbf { G }$ . The only part of the calculation that scales with $n$ (the dimensionality of the feature vector) is computing the components of the Gram matrix. - All other parts of the calculation scale with $m$ , the number of data points.

Thus, in going from primal to dual, we have substituted for a problem that scales (mostly) with the dimensionality of the feature matrix a problem that scales (mostly) with the number of data points. This might seem odd, because it makes problems with huge numbers of data points difficult. However, it makes easy, as we will soon see, problems with moderate amounts of data but huge feature vectors. This is in fact the regime where SVMs really shine.

# 16.5.4 The 1-Norm Soft-Margin SVM and Its Dual

The next important generalization is to relax the unrealistic assumption that there exists a hyperplane that separates the training data, i.e., get rid of the “oracle.” We do this by introducing a so-called slack variable $\xi _ { i }$ for each data point $\mathbf { X } _ { i }$ . If the data point is one that can be separated by a fat plane, then $\xi _ { i } = 0$ . If it can’t be, then $\xi _ { i } > 0$ is the amount of the discrepancy, expressed by the modified inequality

$$
y _ { i } ( \mathbf { w } \cdot \mathbf { x } _ { i } + b ) \geq 1 - \xi _ { i }
$$

We must of course build in an inducement for the optimization to make the $\xi _ { i }$ ’s as small as possible, zero whenever possible. We thus have a trade-off between making the $\xi _ { i }$ ’s small and making the fat plane fat. In other words, we now have a problem that requires not only optimization, but also regularization, in the same sense as the discussion in $\ S 1 8 . 4$ . In the notation of equation (18.4.12), our quadratic forms $( { \bf w } \cdot { \bf w }$ or $\mathcal { L }$ ) are examples of $\mathcal { A }$ ’s. We need to invent a regularizing operator $\mathcal { B }$ that expresses our hopes for the $\xi _ { i }$ ’s, and then minimize $\mathcal { A } + \lambda \mathcal { B }$ , instead of just $\mathcal { A }$ alone. As we vary $\lambda$ in the range $0 < \lambda < \infty$ , we explore a regularization trade-off curve.

The $I$ -norm soft-margin SVM adopts, as the name indicates, a linear sum of the (positive) $\xi _ { i }$ ’s as its regularization operator. The primal problem is thus

$$
{ \left| \begin{array} { l l l } { { \mathrm { m i n i m i z e } } ; } & { { \frac { 1 } { 2 } } \mathbf { w } \cdot \mathbf { w } + \lambda \sum _ { i } \xi _ { i } } \\ { { \mathrm { s u b j e c t ~ t o } } ; } & { \xi _ { i } \geq 0 , } \\ { } & { y _ { i } ( \mathbf { w } \cdot \mathbf { x } _ { i } + b ) \geq 1 - \xi _ { i } \quad } & { i = 1 , \ldots , m } \end{array} \right. }
$$

A possible variant is the 2-norm soft-margin SVM, where the regularization term would be $\textstyle \sum _ { i } \xi _ { i } ^ { 2 }$ ; however, this gives somewhat more complicated equations, so we will put it beyond our scope here.

Along the trade-off curve $0 < \lambda < \infty$ , we vary from a a solution that prefers a really fat fat plane (no matter how many points are inside, or on the wrong side, of it) to a solution that is so miserly in allowing discrepancies that it settles for a fat plane with hardly any margin at all. The former is less accurate on the training data but possibly more robust on new data; the latter is as accurate as possible on the training data but possibly fragile (and less accurate) on new data. As in Chapter 19, the choice of $\lambda$ is a design trade-off that you have to make. (However, we give you some guidance, below.)

Importantly, any nonnegative value of $\lambda$ allows there to be some solution, whether the data are linearly separable or not. You can see this by noting that $\mathbf { w } = 0$ is always a feasible (but not optimal) solution of (16.5.21) for sufficiently large positive $\xi _ { i }$ ’s, no matter what the value of $\lambda$ . If there is a feasible solution, there must, of course, be an optimal solution.

The very astute reader might notice that $\lambda$ here seems to have the opposite qualitative sense from the $\lambda$ ’s in Chapter 19. Specifically, $\lambda  0$ (here) gives the “softer,” more robust, solution, while in Chapter 19 it is $\lambda \to \infty$ that, in a similar way, favors a priori smoothness. The reason for this switch is that the quadratic program (16.5.21) becomes the quadratic program (16.5.6) in the limit $\lambda \to \infty$ , not 0. This is because there are no $\xi _ { i }$ ’s in the constraints in (16.5.6), so (16.5.21) must, in the limit, force them to zero, requiring infinite $\lambda$ . Correspondingly, as $\lambda$ approaches zero, the $\xi _ { i }$ ’s become unconstrained. So the regularization term here indeed does act with the opposite sense from Chapter 19, because of the way it acts through the constraints, not the main functional.

Curiously, the dual to the 1-norm soft-margin SVM turns out to be almost identical to the dual of the (unrealistic) maximum margin SVM (16.5.17). Omitting details of the calculation, the result is

<table><tr><td>minimize: subject to:</td><td>2α ·diag(y)·G·diag(y)·α -e· α 0≤αi≤λ for all i</td></tr></table>

That is, the only difference is that there is now a constraining upper bound of $\lambda$ on $\alpha _ { i }$ in addition to the lower bound of zero. (This kind of constraint is called a box constraint.)

The formula for $\widehat { \mathbf { w } }$ is unchanged from equation (16.5.13), while the Karush-Kuhn-Tucker conditions now become

$$
\begin{array} { r l r } & { } & { ( \widehat { \alpha } _ { i } - \lambda ) \widehat { \xi } _ { i } = 0 } \\ & { } & { \widehat { \alpha } _ { i } \left[ y _ { i } ( \widehat { \bf w } \cdot { \bf x } _ { i } + \widehat { b } ) - 1 + \widehat { \xi } _ { i } \right] = 0 } \end{array}
$$

We see that, except for rare degenerate cases of double zeros,

$$
\begin{array} { r c l } { { \widehat { \alpha } _ { i } = 0 } } & { { \longleftrightarrow } } & { { \mathrm { d a t a ~ p o i n t ~ } i \mathrm { ~ o n ~ c o r r e c t ~ s i d e ~ o f ~ f a t ~ p l a n e } } } \\ { { 0 < \widehat { \alpha } _ { i } < \lambda } } & { { \Longleftrightarrow } } & { { \mathrm { d a t a ~ p o i n t ~ } i \mathrm { ~ c x a c t l y ~ o n ~ f a t ~ p l a n e ~ b o u n d a r y ~ ( a ~ s u p p o r t ~ v a l t ~ a ~ ) } } } \\ { { \widehat { \alpha } _ { i } = \lambda } } & { { \Longleftrightarrow } } & { { \mathrm { d a t a ~ p o i n t ~ } i \mathrm { ~ n s i d e , ~ o r ~ o n ~ w r o n g ~ s i d e , ~ o f ~ f a t ~ p l a n e } } } \end{array}
$$

Here again we see that, as we reduce $\lambda$ toward zero, pinning more and more $\alpha _ { i }$ ’s at the value $\lambda$ , we get solutions with increasing numbers of “wrong” points, but fatter fat planes.

The roundoff-averaged estimator for $\widehat { b }$ , analogous to equation (16.5.19), is

$$
\widehat { b } = \sum _ { i } \widehat { \alpha } _ { i } ( \lambda - \widehat { \alpha } _ { i } ) ( y _ { i } - \widehat { \mathbf { w } } \cdot \mathbf { x } _ { i } ) \Big / \sum _ { i } \widehat { \alpha } _ { i } ( \lambda - \widehat { \alpha } _ { i } )
$$

Although the linear assumption (that is, using hyperplanes to separate the data) is still somewhat restrictive, the model defined by (16.5.22) does have some practical utility in problems where there is some reason to believe that the response is (at least somewhat) linear in the components of the feature vector. But that is far from the end of the story.

# 16.5.5 The Kernel Trick

Finally, we get to the generalization that gives SVMs their real power. Imagine an embedding function $\varphi$ that maps $n$ -dimensional feature vectors, in some manner, into a much higher $N$ -dimensional space,

$$
\mathbf { x } \quad ( n \mathrm { - d i m e n s i o n a l ) } \quad \longrightarrow \quad \varphi ( \mathbf { x } ) \quad ( N \mathrm { - d i m e n s i o n a l ) }
$$

![](images/19a42d053741507fd41af6abf07b7fabf6e07b4299e5386e2fea1bfae8355826.jpg)  
Figure 16.5.2. When feature vectors are mapped from a lower-dimensional space (here 2) to a higherdimensional embedding space (here 3), nonlinear separation surfaces can become well approximated by linear ones. In practice, very high-dimensional embedding spaces are used, but they enter the SVM calculation only implicitly, through the “kernel trick.”

The basic idea, as shown in Figure 16.5.2, is that a very nonlinear separating surface in the $n$ -dimensional space might map into (or be well approximated by) a linear hyperplane in the $N$ -dimensional space.

To see why this might work, consider this mapping from two to five dimensions:

$$
( x _ { 0 } , x _ { 1 } ) \quad { \overset { \varphi } { \longrightarrow } } \quad ( x _ { 0 } ^ { 2 } , x _ { 0 } x _ { 1 } , x _ { 1 } ^ { 2 } , x _ { 0 } , x _ { 1 } )
$$

With this mapping, a decision rule $f ( \mathbf { x } )$ that is constructed as linear in the embedding space becomes general enough to include all linear and quadratic forms (lines, ellipses, hyperbolas) in the original feature space, namely,

$$
f ( \mathbf { x } ) = F [ \varphi ( \mathbf { x } ) ] \equiv \mathbf { W } \cdot \varphi ( \mathbf { x } ) + B
$$

where we are using uppercase letters for quantities in the embedding space. Although $N = 5$ in this example, it might instead have a value like a million or a billion (we’ll see how this works in a minute).

Give our data, how do we find $\mathbf { W }$ and $B$ in the embedding space? Let’s try exactly as before, but just in the higher-dimensional space. The primal problem (compare to equation 16.5.21) is

$$
\begin{array} { l l } { \mathrm { m i n i m i z e } ; \quad \frac { 1 } { 2 } { \bf W } \cdot { \bf W } + \lambda \displaystyle \sum _ { i } \Xi _ { i } } \\ { \mathrm { s u b j e c t } { \bf t o } ; \quad \Xi _ { i } \geq 0 , } \\ { \quad \quad \quad \quad \quad \quad y _ { i } ( { \bf W } \cdot \varphi ( { \bf x } _ { i } ) + B ) \geq 1 - \Xi _ { i } \quad } & { i = 1 , \dots , m } \end{array}
$$

Uh-oh! This is a quadratic programming problem in a million- or billion-dimensional space, not likely to be tractable on your ordinary desktop computer.

What about the dual problem? It turns out to be

$$
{ \begin{array} { r l } { { \boxed { \mathrm { m i n i m i z e : } } } \quad { \frac { 1 } { 2 } } \alpha \cdot \mathrm { d i a g } ( \mathbf { y } ) \cdot \mathbf { K } \cdot \mathrm { d i a g } ( \mathbf { y } ) \cdot { \boldsymbol { \alpha } } - \mathbf { e } \cdot { \boldsymbol { \alpha } } } \\ { { \mathrm { s u b j e c t ~ t o : } } \quad 0 \leq \alpha _ { i } \leq \lambda \qquad { \mathrm { f o r ~ a l l ~ } } i } \\ { \quad \alpha \cdot \mathbf { y } = 0 \qquad } \end{array} }
$$

This is exactly the same as (16.5.22), except that the Gram matrix $G _ { i j }$ has been replaced by the so-called kernel $K _ { i j }$ ,

$$
K _ { i j } \equiv K ( \mathbf { x } _ { i } , \mathbf { x } _ { j } ) \equiv \varphi ( \mathbf { x } _ { i } ) \cdot \varphi ( \mathbf { x } _ { j } )
$$

Well, this is progress. The quadratic programming problem (16.5.30) is no harder than the original problem (16.5.22)! Both live in a space of dimension $m$ , the number of data points, and both get fed a fixed matrix, precalculated from the data: $G _ { i j }$ in one case, $K _ { i j }$ in the other.

We have succeeded in maneuvering the “curse of dimensionality” into a very tight corner, namely the calculation of just the $m ^ { 2 }$ values $K _ { i j }$ . Now we annihilate it entirely with the kernel trick:

The “trick” is that we never really need to know the mapping $\varphi ( \mathbf x )$ at all. All we need is a way of computing a kernel $K _ { i j }$ that could have come from some mapping $\varphi ( \mathbf x )$ , that is, a matrix of size $m \times m$ with the mathematical properties of an inner product space in higher dimension. We already know one possible kernel, namely the Gram matrix $G _ { i j }$ . Here are some provable properties of kernel functions $K ( \mathbf { x } _ { i } , \mathbf { x } _ { j } )$ in general:

- $K _ { i j } = K ( \mathbf x _ { i } , \mathbf x _ { j } )$ must be symmetric in $i$ and $j$ and must have nonnegative eigenvalues (Mercer’s theorem).   
- Any multinomial combination of kernel functions is a kernel function. That is, you can freely combine kernel functions by multiplication, addition, and scaling by a constant. $K ( \varphi ( \mathbf x _ { i } ) , \varphi ( \mathbf x _ { j } ) )$ is a kernel if $K ( , )$ is one, for any $\varphi$ . This generalizes the original idea of the embedding space.   
- $K ( \mathbf { x } _ { i } , \mathbf { x } _ { j } ) = g ( \mathbf { x } _ { i } ) g ( \mathbf { x } _ { j } )$ is always a kernel, for any function $g$ .

Once you settle on a kernel and solve the quadratic programming problem (16.5.30), then your final decision rule for any new feature vector $\mathbf { X }$ is

$$
f ( { \bf x } ) = \sum _ { i } \widehat { \alpha } _ { i } y _ { i } K ( { \bf x } _ { i } , { \bf x } ) + \widehat { b }
$$

where (again using the averaging trick)

$$
\widehat { b } = \sum _ { i } \widehat { \alpha } _ { i } ( \lambda - \widehat { \alpha } _ { i } ) [ y _ { i } - \sum _ { j } \widehat { \alpha } _ { i } y _ { j } K ( \mathbf { x } _ { j } , \mathbf { x } _ { i } ) ] \Big / \sum _ { i } \widehat { \alpha } _ { i } ( \lambda - \widehat { \alpha } _ { i } )
$$

While the construction of the ideal kernel for any particular problem can involve some art, some very generic kernels turn out to be quite powerful in solving realworld problems. Often you can just try a few of these and pick the one that works best. The following are good ones to try first:

linear: $\begin{array} { r l } & { K ( \mathbf { x } _ { i } , \mathbf { x } _ { j } ) = \mathbf { x } _ { i } \cdot \mathbf { x } _ { j } } \\ & { K ( \mathbf { x } _ { i } , \mathbf { x } _ { j } ) = ( \mathbf { x } _ { i } \cdot \mathbf { x } _ { j } ) ^ { d } , \qquad 2 \leq d \leq 2 0 } \\ & { K ( \mathbf { x } _ { i } , \mathbf { x } _ { j } ) = ( a \mathbf { x } _ { i } \cdot \mathbf { x } _ { j } + b ) ^ { d } } \\ & { K ( \mathbf { x } _ { i } , \mathbf { x } _ { j } ) = \operatorname { t a n h } ( a \mathbf { x } _ { i } \cdot \mathbf { x } _ { j } + b ) } \\ & { K ( \mathbf { x } _ { i } , \mathbf { x } _ { j } ) = \exp ( - \frac { 1 } { 2 } | \mathbf { x } _ { i } - \mathbf { x } _ { j } | ^ { 2 } / \sigma ^ { 2 } ) } \end{array}$ power: (say) polynomial: sigmoid: Gaussian radial basis function:

![](images/41addd7662e6ddc430e31820f158759b17a3b666b36f252a9fb76e61a0b9b69e.jpg)  
Figure 16.5.3. SVMs that “learn” to partition the plane. The input data are drawn from four twodimensional Gaussians, slightly overlapping, with diagonally opposite ones given the same label $\mathbf { \bar { x } }$ or o). Heavy solid lines are the decision rule surfaces $f ( \mathbf { x } ) = \mathbf { 0 }$ derived by the SVMs. Lighter lines show $f ( \mathbf { x } ) = \pm 1$ . (a) Polynomial kernel with $d = 8$ . (b) Gaussian radial basis function kernel.

See $\ S 2 . 3$ of [5] for additional standard kernels. Chapter 13 of [5] describes many specialized kernels, e.g., for comparing strings or passages of text, for image recognition, and for a number of other applications.

Figure 16.5.3 shows a test example using both a polynomial kernel with $d =$ 8 and a Gaussian radial basis kernel. It is characteristic of the Gaussian kernel that it is more influenced by local nearest neighbor effects (which may be good or bad, depending on the application), while polynomial kernels seek smoother, more global solutions.

Although it is beyond our scope in this section, we should mention that the kernel trick is applicable not only to SVMs (that is, to algorithms based on separating hyperplanes), but also to a number of other pattern recognition algorithms, for example principal component analysis (PCA) and the Fisher discriminant algorithm. See [5] and [6] for extensive treatments of these kernel-based learning algorithms.

# 16.5.6 Some Practical Advice on SVMs

The Gaussian radial basis function kernel is very popular, because it has only one adjustable parameter, $\sigma$ , and it is easy to guess a first value to try, namely any characteristic distance between nearby points in the feature space. As mentioned, the Gaussian kernel classifies to some degree by the local neighborhood consensus.

For the polynomial kernels, start by choosing $a$ and $b$ to make $a { \bf x } _ { i } \cdot { \bf x } _ { j } + b$ lie between $\pm 1$ for all $i$ and $j$ . The power $d$ has a (very rough) interpretation as how many different features you want the comparison to “mix.” That is, $d \ = \ 1$ (linear) partitions the space by one feature at at time; $d = 2$ looks at pairs of features simultaneously, and so on. Also very roughly, the difference between power and polynomial is whether you want to consider only exactly $d$ features at a time (power), or all combinations of $d$ or fewer features (polynomial). These interpretations should not be taken too seriously, however. Specifically, larger $d$ is not always better.

We have not said much about how to choose $\lambda$ , the regularization parameter.

Try $\lambda \ : = \ : 1$ first, then try increasing and decreasing it by factors of 10. There is typically a broad plateau, as a function of $\log _ { 1 0 } ( \lambda )$ , where the precise value of $\lambda$ doesn’t matter much. There is some belief that $\langle \mathbf { \bar { x } } _ { i } \cdot \mathbf { x } _ { j } \rangle ^ { - 1 }$ or $\langle K ( \mathbf { x } _ { i } , \mathbf { x } _ { j } ) \rangle ^ { - 1 }$ , where angle brackets denote averages over all $i , j$ pairs, are good starting guesses; but for properly scaled kernels these should not be too different from unity in any case.

As you vary $\lambda$ and repeatedly solve the quadratic program, look at the fraction of $\alpha _ { i }$ ’s that are pinned at zero, pinned at $\lambda$ , or floating between these limits. A good profile will often have the biggest fraction at zero, a smaller (but not necessarily much smaller) fraction at $\lambda$ , and the smallest fraction in between (see equation 16.5.24 for interpretation). These fractions are also often good indicators for adjusting parameters in your kernel. Naturally you will also be looking at the fraction of your training data that is predicted correctly, that is, has $y _ { i } f ( \mathbf { x } _ { i } ) > 0$ .

Below, we will give a short, self-contained program for finding the solution to SVMs; but for anything other than small problems you will want to use a more sophisticated software package. There are many tricks and shortcuts that can speed the solution of an SVM relative to the general problem of quadratic programming — good SVM packages take advantage of these. For example, a good package should take advantage of sparseness in the feature vectors to save on computation. Our favorite package is Thorsten Joachims’ SVMlight [7], available for free on the Web. Gist [8] is another popular free implementation. The Web site cited in [2] has a page with links to a wide variety of SVM software.

# 16.5.7 The Mangasarian-Musicant Variant and Its Solution by SOR

Mangasarian and Musicant [9,10] have suggested a very slight variant of equation (16.5.21), and its kernel generalization, that has the interesting property that it can be solved, quite compactly, by the method of successive overrelaxation (SOR; see $\ S 2 0 . 5 . 1 \AA ,$ ). In particular, a complete SVM solution program using SOR is less than 100 lines long. We discuss this M-M variant here, and implement it in code, just because of its brevity. We have used this code for problems of up to several thousand data points, with feature vectors of length several hundred. Such problems take seconds to solve on a desktop machine. For larger problems, our advice is that you use the more efficient specialized packages [7,8]. SVMlight, for example, is typically about an order of magnitude faster than the code we give below.

The primal problem in the 1-norm soft-margin form of the M-M variant is

<table><tr><td></td><td>minimize:μw·w+b²+𝜆∑ i</td></tr><tr><td>subject to:§i ≥ 0,</td><td>yi(w·Xi+b)≥1-$i i=1,...,m</td></tr></table>

The only difference from (16.5.21) is that a term $b ^ { 2 }$ has been added to the functional that is minimized. On its face, this should have the effect of slightly favoring hyperplanes closer to the origin, all else being equal, an innocuous (albeit arbitrary) change. The real purpose of the $b ^ { 2 }$ term, however, is its algebraic effect when we calculate the dual problem:

$$
\begin{array} { r } { \left| \begin{array} { l l } { \mathrm { m i n i m i z e : } \quad } & { \frac { 1 } { 2 } \boldsymbol { \alpha } \cdot \mathrm { d i a g } ( \mathbf { y } ) \cdot ( \mathbf { G } + \mathbf { e } \otimes \mathbf { e } ) \cdot \mathrm { d i a g } ( \mathbf { y } ) \cdot { \boldsymbol { \alpha } } - \mathbf { e } \cdot { \boldsymbol { \alpha } } } \\ { \mathrm { s u b j e c t ~ t o : } \quad 0 \leq \alpha _ { i } \leq \lambda \qquad } & { \mathrm { f o r ~ a l l ~ } i } \end{array} \right. } \end{array}
$$

Aside from an extra term e $\otimes$ e (the matrix of all ones) now added to the Gram matrix, the main change from (16.5.21) is that the equality constraint is gone! This renders the solution much more tractable numerically. The dual problem also now has a simpler expression for $\widehat { b }$ ,

$$
\widehat { b } = \sum _ { i } \widehat { \alpha } _ { i } y _ { i }
$$

(As before, $\widehat { \mathbf { w } }$ is computed from 16.5.13.)

When we do the kernel trick, the only change in (16.5.36) is to change $G _ { i j }$ to $K _ { i j }$ . Equation (16.5.37) still holds, but $\widehat { b }$ is actually superfluous since the decision rule can be written directly as

$$
f ( { \bf x } ) = \sum _ { i } \widehat { \alpha } _ { i } y _ { i } [ K ( { \bf x } _ { i } , { \bf x } ) + 1 ]
$$

Mangasarian and Musicant have shown that the solution of the M-M variant SVM is often identical to the solution of the the standard 1-norm soft-margin SVM (albeit with a different value of $\lambda$ ) and is almost never significantly different. What is quite different, however, is that (16.5.36) and its kernel version can be solved by the following, linearly convergent, relaxation procedure:

- Define $\mathbf { M } \equiv \mathrm { d i a g } ( \mathbf { y } ) \cdot ( \mathbf { K } + \mathbf { e } \otimes \mathbf { e } ) \cdot \mathrm { d i a g } ( \mathbf { y } ) .$   
- Initialize all the $\alpha _ { i }$ ’s to zero.   
- Repeat ad libitum the relaxation replacement, for $i = 1 , 2 , \dots , m$ ,

$$
\alpha _ { i } \gets \mathcal { P } \biggl [ \alpha _ { i } - \omega \frac { 1 } { M _ { i i } } \biggl ( \sum _ { j } M _ { i j } \alpha _ { j } - 1 \biggr ) \biggr ]
$$

Here $\mathcal { P }$ is the projection operator that just puts $\alpha$ back into its allowed range. [Note the similarity to the method of projection onto convex sets (POCS) in $\ S 1 9 . 5 . 2 . ]$

$$
\mathcal { P } = \left\{ \begin{array} { l l } { 0 , } & { \alpha < 0 } \\ { \alpha , } & { 0 \leq \alpha \leq \lambda } \\ { \lambda , } & { \alpha > \lambda } \end{array} \right.
$$

The constant $\omega$ is the overrelaxation parameter, exactly as in $\ S 2 0 . 5 . 1$ . You pick it in the range $0 < \omega < 2$ . In our experience, the convergence rate does not depend sensitively on $\omega$ . If you don’t have a better idea, take $\omega = 1 . 3$ .

Our implementation begins with a virtual class that defines the interface to a kernel function,

# svm.h

# struct Svmgenkernel {

Virtual class that defines what a kernel structure needs to provide.

Int m, kcalls;   
MatDoub ker;   
VecDoub_I &y;   
MatDoub_I &data; No. of data points; counter for kernel calls.   
Locally stored kernel matrix.   
Must provide reference to the $y _ { i }$ ’s.   
Must provide reference to the $\mathbf { x } _ { i } \mathbf { \ ' } _ { \mathbf { s } }$ .

Svmgenkernel(VecDoub_I &yy, MatDoub_I &ddata) : m(yy.size()),kcalls(0),ker(m,m),y(yy),data(ddata) {} Every kernel structure must provide a kernel function that returns the kernel for arbitrary feature vectors. virtual Doub kernel(const Doub \*xi, const Doub $* _ { \mathbf { X } , \mathbf { j } } ) ~ = ~ 0$ ; inline Doub kernel(Int i, Doub \*xj) {return kernel(&data[i][0],xj);} Every kernel structure’s constructor must call fill to fill the ker matrix. void fill() { Int i,j; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<m; $\dot { 1 } + +$ ) for (j ${ = } 0$ ;j ${ \tt { \tt { \tt { \tt { \Lambda } } } } } = \dot { \tt { \tt { \tt { 1 } } } }$ ;j $^ { + + }$ ) { ker[i][j] $=$ ker[j][i] $=$ kernel(&data[i][0],&data[j][0]); } } };

Basically, a kernel structure is required to provide references to the data (the $\mathbf { X } _ { i }$ ’s) and the ${ \bf y } _ { i }$ ’s, a matrix of kernel values for all pairs of data points, and two forms of the kernel function: one with two arbitrary feature vectors as arguments, and another with one argument a data point and the other an arbitrary feature vector. Here are three examples of kernels, for three of the standard kernels in equation (16.5.34), built on the above Svmgenkernel.

# struct Svmlinkernel : Svmgenkernel {

Kernel structure for the linear kernel, the dot product of two feature vectors (with overall means of each component subtracted).

Int n; VecDoub mu; Svmlinkernel(MatDoub_I &ddata, VecDoub_I &yy) Constructor is called with the $m \times n$ data matrix, and the vector of $y _ { i }$ ’s, length $_ m$ . : Svmgenkernel(yy,ddata), n(data.ncols()), mu(n) { Int i,j; for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<n;j $^ { + + }$ ) mu[j] $\qquad = \ 0$ .; for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<m; $\dot { \bar { \lambda } } + +$ ) for ( ${ = } 0$ ;j<n;j++) mu[j] $+ =$ data[i][j]; for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j $^ { + + }$ ) mu[j] /= m; fill(); } Doub kernel(const Doub \*xi, const Doub \*xj) { Doub dott $\mathit { \Theta } = \mathit { \Theta } 0 .$ ; for (Int $\mathtt { k } = 0$ ; k<n; $\mathbf { k } { + } { + } \mathbf { \cdot }$ ) dott $+ =$ (xi[k]-mu[k])\*(xj[k]-mu[k]); return dott; } };

# struct Svmpolykernel : Svmgenkernel {

Kernel structure for the polynomial kernel. Int n; Doub a, b, d; Svmpolykernel(MatDoub_I &ddata, VecDoub_I &yy, Doub aa, Doub bb, Doub dd) Constructor is called with the $m \times n$ data matrix, the vector of $y _ { i }$ ’s, length $m$ , and the constants a, $^ { b }$ , and $d$ . : Svmgenkernel(yy,ddata), n(data.ncols()), a(aa), b(bb), d(dd) {fill();} Doub kernel(const Doub \*xi, const Doub \*xj) { Doub dott $\qquad = \ 0 .$ ; for (Int $\mathtt { k } = 0$ ; $\mathtt { k } < \mathtt { n }$ ; $\mathrm { k } { + } { + }$ ) dott $+ =$ xi[k]\*xj[k]; return pow(a\*dott+b,d); }   
};

struct Svmgausskernel : Svmgenkernel { Kernel structure for the Gaussian radial basis function kernel. Int n;

Doub sigma;   
Svmgausskernel(MatDoub_I &ddata, VecDoub_I &yy, Doub ssigma)   
Constructor is called with the $m \times n$ data matrix, the vector of $y _ { i }$ ’s, length m, and the constant $\sigma$ .

: Svmgenkernel(yy,ddata), n(data.ncols()), sigma(ssigma) {fill();} Doub kernel(const Doub \*xi, const Doub \*xj) { Doub dott $\qquad = \ 0 .$ ; for (Int $\mathtt { k } = 0$ ; k<n; $\mathrm { k } { + + }$ ) dott $+ =$ SQR(xi[k]-xj[k]); return ex ${ \mathsf p } ( - 0 . 5 *$ dott/(sigma\*sigma)); } };

The above is all prefatory to the SVM solution structure. You declare an instance of Svm with your kernel as the argument. It then makes available three functions: relax performs one “group” of relaxation steps and returns the norm of how much change in $\pmb { \alpha }$ has occurred. (We define “group” below.) You call relax repeatedly, with $\lambda$ and $\omega$ as arguments, until the returned value is small enough: $1 0 ^ { - 3 }$ or $1 0 ^ { - 4 }$ is usually plenty. Then (and only then) you may repeatedly call either of two forms of predict, which returns the decision rule $f ( \mathbf { x } )$ . One form of predict returns the prediction for data points, the other for arbitrary new feature vectors. If you want to examine the $\alpha _ { i }$ ’s, or count how many are pinned at 0 or $\lambda$ , you can examine the vector alph.

struct Svm {   
Class for solving SVM problems by the SOR method. Svmgenkernel &gker; Reference bound to user’s kernel (and data). Int m, fnz, fub, niter; VecDoub alph, alphold; Vectors of $\pmb { \alpha }$ ’s before and after a step. Ran ran; Random number generator. Bool alphinit; Doub dalph; Change in norm of the $\pmb { \alpha }$ ’s in one step. Svm(Svmgenkernel &inker) : gker(inker), m(gker.y.size()), alph(m), alphold(m), ran(21), alphinit(false) {} Constructor binds the user’s kernel and allocates storage. Doub relax(Doub lambda, Doub om) { Perform one group of relaxation steps: a single step over all the ˛’s, and multiple steps over only the interior ˛’s. Int iter,j,jj,k,kk; Doub sum; Index when $\pmb { \alpha }$ ’s are sorted by value. VecDoub pinsum(m); Stored sums over noninterior variables. if (alphinit $= =$ false) { Start all $\pmb { \alpha }$ ’s at 0. for $( \mathrm { j } = 0$ ; j<m; ${ \mathrm { j } } + + { \mathrm { . } }$ ) alph[j] = 0.; alphinit $=$ true; } alphold $=$ alph; Save old ˛’s. Here begins the relaxation pass over all the ˛’s. Indexx x(alph); Sort $\pmb { \alpha }$ ’s, then find first nonzero one. for (fnz ${ } = 0$ ; fnz<m; fnz $^ { + + }$ ) if (alph[x.indx[fnz]] $\begin{array} { r l } { \mathbf { l } = } & { { } 0 . } \end{array}$ ) break; for (j=fnz; j<m-2; ${ \mathrm { j } } + + { \mathrm { , } }$ ) { Randomly permute all the nonzero $\pmb { \alpha }$ ’s. $\mathrm { ~ \bf ~ k ~ } = \mathrm { ~ j ~ } + \mathrm { ~ \bf ~ \ k ~ }$ (ran.int32() % (m-j)); SWAP(x.indx[j],x.indx[k]); } for (jj ${ = } 0$ ; jj<m; jj++) { Main loop over ˛’s. $\dot { \textbf { j } } = \textbf { x }$ .indx[jj]; sum $\mathit { \Theta } = \mathit { \Theta } 0 .$ ; for (kk=fnz; kk<m; kk++) { Sums start with first nonzero. $\mathrm { ~ \tt ~ { ~ k ~ } ~ } = \mathrm { ~ \tt ~ { ~ x ~ } ~ }$ .indx[kk]; sum $+ =$ (gker.ker[j][k] $^ +$ 1.)\*gker.y[k]\*alph[k]; } alph[j] $=$ alph[j] - (om/(gker.ker[j][j]+1.))\*(gker.y[j]\*sum-1.); alph[j] $=$ MAX(0.,MIN(lambda,alph[j])); Projection operator. if (jj $<$ fnz && alph[j]) SWAP(x.indx[--fnz],x.indx[jj]);   
} (Above) Make an $\pmb { \alpha }$ active if it becomes nonzero.   
Here begins the relaxation passes over the interior ˛’s.   
Indexx y(alph); Sort. Identify interior $\pmb { \alpha }$ ’s.   
for (fnz ${ = } 0$ ; fnz<m; fnz $^ { + + }$ ) if (alph[y.indx[fnz]] $\begin{array} { r l } { \mathbf { l } = } & { { } 0 . } \end{array}$ ) break;   
for (fub=fnz; fub<m; fub $^ { + + }$ ) if (alph[y.indx[fub]] $= =$ lambda) break;   
for (j=fnz; j<fub-2; ${ \mathrm { j } } + +$ ) { Permute. $\mathrm { ~ \bf ~ k ~ } = \mathrm { ~ j ~ } + \mathrm { ~ \bf ~ \ k ~ }$ (ran.int32() % (fub-j)); SWAP(y.indx[j],y.indx[k]);   
}   
for (jj=fnz; jj<fub; jj++) { Compute sums over pinned $\pmb { \alpha }$ ’s just j $=$ y.indx[jj]; once. sum $\mathit { \Theta } = \mathit { \Theta } 0 \ : .$ .; for (kk=fub; kk<m; kk $^ { + + }$ ) { $\mathrm { ~ \bf ~ k ~ } =$ y.indx[kk]; sum $+ =$ (gker.ker[j][k] $^ +$ 1.)\*gker.y[k]\*alph[k]; } pinsum[jj] $=$ sum;

ter $=$ MAX(Int(0.5\*(m+1.0)\*(m-fnz+1.0)/(SQR(fub-fnz+1.0))),1);

Calculate a number of iterations that will take about half as long as the full pass just completed.

for (iter ${ = } 0$ ; iter<niter; iter++) { Main loop over ˛’s. for (jj=fnz; jj<fub; jj $^ { + + }$ ) { ${ \dot { \textbf { j } } } =$ y.indx[jj]; sum $=$ pinsum[jj]; for (kk=fnz; kk<fub; kk++) { k = y.indx[kk]; sum $+ =$ (gker.ker[j][k] $^ +$ 1.)\*gker.y[k]\*alph[k]; } alph[j] $=$ alph[j] - (om/(gker.ker[j][j]+1.))\*(gker.y[j]\*sum-1.); alph[j] $=$ MAX(0.,MIN(lambda,alph[j])); }   
dalph $\qquad = \ 0 .$ .; Return change in norm of $\pmb { \alpha }$ vector.   
for (j ${ = } 0$ ;j<m;j $^ { + + }$ ) dalph $+ =$ SQR(alph[j]-alphold[j]);   
return sqrt(dalph);

# Doub predict(Int k) {

Call only after convergence via repeated calls to relax. Returns the decision rule $f ( \mathbf { x } )$ for data point k.

Doub sum $\qquad = \ 0 .$ .;   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<m; ${ \mathrm { j } } + + { \mathrm { . } }$ ) sum $+ =$ alph[j]\*gker.y[j]\*(gker.ker[j][k]+1.0);   
return sum;

Doub predict(Doub \*x) {

Call only after convergence via repeated calls to relax. Returns the decision rule $f ( \mathbf { x } )$ for an arbitrary feature vector.

Doub sum $\qquad = \ 0$ .;for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<m; ${ \mathrm { j } } + + { \mathrm { . } }$ ) sum $+ =$ alph[j]\*gker.y[j]\*(gker.kernel(j,x)+1.0);return sum;}};

Although the enforced brevity doesn’t allow for too many optimizing tricks, Svm does have a couple that bear mentioning:

First, each call to the relax routine performs, as previously mentioned, a group of relaxations. Specifically, it does one full relaxation pass over all the $\alpha _ { i }$ ’s, and then multiple passes over only the “interior” $\alpha _ { i }$ ’s, i.e., those that are not pinned at either 0 or $\lambda$ . These passes are typically much faster than the full pass, since most variables are typically pinned. To realize the gain, sums over pinned variables that don’t vary are computed only once at the beginning of these multiple passes. The number of such passes is calculated dynamically so as to take about half as long as the full pass just taken.

Second, before each pass (both the full and interior), the order of the variables is randomized by a permutation generated from a Ran object (-7.1). This randomization speeds up the convergence by as much as an order of magnitude.

# CITED REFERENCES AND FURTHER READING:

Boser, B.E., Guyon, I.M., and Vapnik, V.N. 1992, in D. Haussler, ed., Proceedings of the 5th Annual ACM Workshop on Computational Learning Theory (New York: ACM Press).[1]   
Christianini, N. and Shawe-Taylor, J. 2000, An Introduction to Support Vector Machines (Cambridge, U.K.: Cambridge University Press); related Web site http://www.support-vector.net.[2]   
Bazaraa, M.S., Sherali, H.D., and Shetty, C.M. 2006, Nonlinear Programming: Theory and Algorithms,3rd ed. (Hoboken,NJ: Wiley).[3]   
den Hertog, D. 1994, Interior Point Approach to Linear, Quadratic and Convex Programming: Algorithms and Complexity (Dordrecht:Kluwer).[4]   
Schölkopf, B. and Smola, A.J. 2002, Learning with Kernels: Support Vector Machines, Regularization, Optimization,and Beyond (Cambridge, MA: MIT Press).[5]   
Shawe-Taylor, J. and Christianini, N. 2004, Kernel Methods for Pattern Analysis (Cambridge, UK: Cambridge University Press).[6]   
Vapnik, V. 1998, Statistical Learning Theory (New York: Wiley).   
Joachims, T. 1999–, SVMlight, Implementing Support Vector Machines in C, at http://svmlight.joachims.org.[7]   
Noble, W.S. and Pavlidis, P. 1999–, Gist: Software Tools for Support Vector Machine Classificationand for Kernel Principal Components Analysis,at http://microarray.cpmc.columbia.edu/gist.[8]   
Mangasarian, O.L. and Musicant, D.R. 1999, “Successive Overrelaxation for Support Vector Machines,” IEEE Transactions on Neural Networks, vol. 10, no. 5, p. 1032.[9]   
Mangasarian, O.L. and Musicant, D.R. 2001, in Complementarity: Applications, Algorithms and Extensions, M.C.Ferris, O.L.Mangasarian and J.-S.Pang,eds.(Dordrecht: Kluwer) pp.233- 251.[10]

# Integration of Ordinary Differential Equations

# 17.0 Introduction

Problems involving ordinary differential equations (ODEs) can always be reduced to the study of sets of first-order differential equations. For example the second-order equation

$$
{ \frac { d ^ { 2 } y } { d x ^ { 2 } } } + q ( x ) { \frac { d y } { d x } } = r ( x )
$$

can be rewritten as two first-order equations,

$$
\begin{array} { l } { \displaystyle { \frac { d y } { d x } = z ( x ) } } \\ { \displaystyle { \frac { d z } { d x } = r ( x ) - q ( x ) z ( x ) } } \end{array}
$$

where $Z$ is a new variable. This exemplifies the procedure for an arbitrary ODE. The usual choice for the new variables is to let them be just derivatives of each other (and of the original variable). Occasionally, it is useful to incorporate into their definition some other factors in the equation, or some powers of the independent variable, for the purpose of mitigating singular behavior that could result in overflows or increased roundoff error. Let common sense be your guide: If you find that the original variables are smooth in a solution, while your auxiliary variables are doing crazy things, then figure out why and choose different auxiliary variables.

The generic problem in ordinary differential equations is thus reduced to the study of a set of $N$ coupled first-order differential equations for the functions $y _ { i } , ~ i =$ $0 , 1 , \ldots , N - 1$ , having the general form

$$
\frac { d y _ { i } ( x ) } { d x } = f _ { i } ( x , y _ { 0 } , \ldots , y _ { N - 1 } ) , \qquad i = 0 , \ldots , N - 1
$$

where the functions $f _ { i }$ on the right-hand side are known.

A problem involving ODEs is not completely specified by its equations. Even more crucial in determining how to attack the problem numerically is the nature of the problem’s boundary conditions. Boundary conditions are algebraic conditions on the values of the functions $y _ { i }$ in (17.0.3). In general they can be satisfied at discrete specified points, but do not hold between those points, i.e., are not preserved automatically by the differential equations. Boundary conditions can be as simple as requiring that certain variables have certain numerical values, or as complicated as a set of nonlinear algebraic equations among the variables.

Usually, it is the nature of the boundary conditions that determines which numerical methods will be feasible. Boundary conditions divide into two broad categories.

- In initial value problems all the $y _ { i }$ are given at some starting value $x _ { s }$ , and it is desired to find the $y _ { i }$ ’s at some final point $x _ { f }$ , or at some discrete list of points (for example, at tabulated intervals). In two-point boundary value problems, on the other hand, boundary conditions are specified at more than one $x$ . Typically, some of the conditions will be specified at $x _ { s }$ and the remainder at $x _ { f }$ .

This chapter will consider exclusively the initial value problem, deferring two-point boundary value problems, which are generally more difficult, to Chapter 18.

The underlying idea of any routine for solving the initial value problem is always this: Rewrite the $d y$ ’s and $d x$ ’s in (17.0.3) as finite steps $\Delta y$ and $\Delta x$ , and multiply the equations by $\Delta x$ . This gives algebraic formulas for the change in the functions when the independent variable $x$ is “stepped” by one “stepsize” $\Delta x$ . In the limit of making the stepsize very small, a good approximation to the underlying differential equation is achieved. Literal implementation of this procedure results in Euler’s method (equation 17.1.1, below), which is, however, not recommended for any practical use. Euler’s method is conceptually important, however; one way or another, practical methods all come down to this same idea: Add small increments to your functions corresponding to derivatives (right-hand sides of the equations) multiplied by stepsizes.

In this chapter we consider three major types of practical numerical methods for solving initial value problems for ODEs:

- Runge-Kutta methods   
- Richardson extrapolation and its particular implementation as the Bulirsch-Stoer method   
- predictor-corrector methods, also known as multistep methods.

A brief description of each of these types follows.

1. Runge-Kutta methods propagate a solution over an interval by combining the information from several Euler-style steps (each involving one evaluation of the right-hand $f$ ’s), and then using the information obtained to match a Taylor series expansion up to some higher order.

2. Richardson extrapolation uses the powerful idea of extrapolating a computed result to the value that would have been obtained if the stepsize had been very much smaller than it actually was. In particular, extrapolation to zero stepsize is the desired goal. The first practical ODE integrator that implemented this idea was developed by Bulirsch and Stoer, and so extrapolation methods are often called Bulirsch-Stoer methods.

3. Predictor-corrector methods or multistep methods store the solution along the way, and use those results to extrapolate the solution one step advanced; they then correct the extrapolation using derivative information at the new point. These are best for very smooth functions.

Runge-Kutta used to be what you used when (i) you didn’t know any better, or (ii) you had an intransigent problem where Bulirsch-Stoer was failing, or (iii) you had a trivial problem where computational efficiency was of no concern. However, advances in Runge-Kutta methods, particularly the development of higher-order methods, have made Runge-Kutta competitive with the other methods in many cases. Runge-Kutta succeeds virtually always; it is usually the fastest method when evaluating $f _ { i }$ is cheap and the accuracy requirement is not ultra-stringent $( \lesssim 1 0 ^ { - 1 0 }$ ), or in general when moderate accuracy $( \lesssim 1 0 ^ { - 5 } )$ is required. Predictor-corrector methods have a relatively high overhead and so come into their own only when evaluating $f _ { i }$ is expensive. However, for many smooth problems, they are computationally more efficient than Runge-Kutta. In recent years, Bulirsch-Stoer has been replacing predictor-corrector in many applications, but it is too soon to say that predictorcorrector is dominated in all cases. However, it appears that only rather sophisticated predictor-corrector routines are competitive. Accordingly, we have chosen not to give an implementation of predictor-corrector in this book. We discuss predictorcorrector further in $\ S 1 7 . 6$ , so that you can use a packaged routine knowledgeably should you encounter a suitable problem. In our experience, the relatively simple Runge-Kutta and Bulirsch-Stoer routines we give are adequate for most problems.

Each of the three types of methods can be organized to monitor internal consistency. This allows numerical errors, which are inevitably introduced into the solution, to be controlled by automatic (adaptive) changing of the fundamental stepsize. We always recommend that adaptive stepsize control be implemented, and we will do so below.

In general, all three types of methods can be applied to any initial value problem. Each comes with its own set of debits and credits that must be understood before it is used.

Section 17.5 of this chapter treats the subject of stiff equations, relevant both to ordinary differential equations and also to partial differential equations (Chapter 20).

# 17.0.1 Organization of the Routines in This Chapter

We have organized the routines in this chapter into three nested levels, enabling modularity and sharing common code wherever possible.

The highest level is the driver object, which starts and stops the integration, stores intermediate results, and generally acts as an interface with the user. There is nothing canonical about our driver object, Odeint. You should consider it to be an example, and you can customize it for your particular application.

The next level down is a stepper object. The stepper oversees the actual incrementing of the independent variable $x$ . It knows how to call the underlying algorithm routine. It may reject the result, set a smaller stepsize, and call the algorithm routine again, until compatibility with a predetermined accuracy criterion has been achieved. The stepper’s fundamental task is to take the largest stepsize consistent with specified performance. Only when this is accomplished does the true power of an algorithm come to light.

All our steppers are derived from a base object called StepperBase: StepperDopr5 and StepperDopr853 (two Runge-Kutta routines), StepperBS and StepperStoerm (two Bulirsch-Stoer routines), and StepperRoss and StepperSIE

(for so-called stiff equations).

Standing apart from the stepper, but interacting with it at the same level, is an Output object. This is basically a container into which the stepper writes the output of the integration, but it has some intelligence of its own: It can save, or not save, intermediate results according to several different prescriptions that are specified by its constructor. In particular, it has the option to provide so-called dense output, that is, output at user-specified intermediate points without loss of efficiency.

The lowest or “nitty-gritty” level is the piece we call the algorithm routine. This implements the basic formulas of the method, starts with dependent variables $y _ { i }$ at $x$ , and calculates new values of the dependent variables at the value $x + h$ . The algorithm routine also yields some information about the quality of the solution after the step. The routine is dumb, however, in that it is unable to make any adaptive decision about whether the solution is of acceptable quality. Each algorithm routine is implemented as a member function dy() in its corresponding stepper object.

# 17.0.2 The Odeint Object

It is a real time saver to have a single high-level interface to what are otherwise quite diverse methods. We use the Odeint driver for a variety of problems, notably including garden-variety ODEs or sets of ODEs, and definite integrals (augmenting the methods of Chapter 4). The Odeint driver is templated on the stepper. This means that you can usually change from one ODE method to another in just a few keystrokes. For example, changing from the Dormand-Prince fifth-order Runge-Kutta method to Bulirsch-Stoer is as simple as changing the template parameter from StepperDopr5 to StepperBS.

The Odeint constructor simply initializes a bunch of things, including a call to the stepper constructor. The meat is in the integrate routine, which repeatedly invokes the step routine of the stepper to advance the solution from $x _ { 1 }$ to $x _ { 2 }$ . It also calls the functions of the Output object to save the results at appropriate points.

# template<class Stepper>

struct Odeint { river for ODE solvers with adaptive stepsize control. The template parameter should be one the derived classes of StepperBase defining a particular integration algorithm. static const Int MAXSTP $^ { \prime = }$ 50000; Take at most MAXSTP steps. Doub EPS; Int nok; Int nbad; Int nvar; Doub x1,x2,hmin; bool dense; true if dense output requested by VecDoub y,dydx; out. VecDoub &ystart; Output &out; typename Stepper::Dtype &derivs; Get the type of derivs from the Stepper s; stepper. Int nstp; Doub x,h; Odeint(VecDoub_IO &ystartt,const Doub xx1,const Doub xx2, const Doub atol,const Doub rtol,const Doub h1, const Doub hminn,Output &outt,typename Stepper::Dtype &derivss);

Constructor sets everything up. The routine integrates starting values ystart[0..nvar-1] from xx1 to xx2 with absolute tolerance atol and relative tolerance rtol. The quantity h1 should be set as a guessed first stepsize, hmin as the minimum allowed stepsize (can be zero). An Output object out should be input to control the saving of intermediate values.

On output, nok and nbad are the number of good and bad (but retried and fixed) steps taken, and ystart is replaced by values at the end of the integration interval. derivs is the user-supplied routine (function or functor) for calculating the right-hand side derivative.

void integrate(); };

Does the actual integration.

template<class Stepper>   
Odeint<Stepper>::Odeint(VecDoub_IO &ystartt, const Doub xx1, const Doub xx2, const Doub atol, const Doub rtol, const Doub h1, const Doub hminn, Output &outt,typename Stepper::Dtype &derivss) : nvar(ystartt.size()), y(nvar),dydx(nvar),ystart(ystartt),x(xx1),nok(0),nbad(0), x1(xx1),x2(xx2),hmin(hminn),dense(outt.dense),out(outt),derivs(derivss), s(y,dydx,x,atol,rtol,dense) { EPS=numeric_limits<Doub>::epsilon(); h=SIGN(h1,x2-x1); for (Int $\scriptstyle \dot { 1 } = 0$ ;i<nvar;i++) y[i]=ystart[i]; out.init(s.neqn,x1,x2);   
}   
template<class Stepper>   
void Odeint<Stepper>::integrate() { derivs(x,y,dydx); if (dense) Store initial values. out.out(-1,x,y,s,h); else out.save(x,y); for (nstp $\scriptstyle 1 = 0$ ;nstp<MAXSTP;nstp $^ { + + }$ ) { if ((x+h\*1.0001-x2)\*(x2-x1) > 0.0) $\mathtt { h } = \mathtt { x } 2 - \mathtt { x }$ ; If stepsize can overshoot, decrease. s.step(h,derivs); Take a step. if (s.hdid $\mathbf { \Psi } = \mathbf { \Psi } \mathbf { h } .$ ) $^ { + + }$ nok; else $^ { + + }$ nbad; if (dense) out.out(nstp,x,y,s,s.hdid); else out.save(x,y); if ( $( { \bf x } { - \bf x } 2 ) * ( { \bf x } 2 { - \bf x } 1 ) > = 0 . 0 )$ { Are we done? for (Int $\scriptstyle \dot { 1 } = 0$ ;i<nvar; $\dot { \bf 1 } + +$ ) ystart[i]=y[i]; Update ystart. if (out.kmax $>$ 0 && abs(out.xsave[out.count-1]-x2) > 100.0\*abs(x2)\*EPS) out.save(x,y); Make sure last step gets saved. return; Normal exit. if (abs(s.hnext) $< =$ hmin) throw("Step size too small in Odeint"); $\mathtt { h } = \mathtt { s }$ .hnext; throw("Too many steps in routine Odeint");   
}

The Odeint object doesn’t know in advance which specific stepper object it will be instantiated with. It does, however, rely on the fact that the stepper object will be derived from, and thus have the methods in, this StepperBase object, which serves as the base class for all subsequent ODE algorithms in this chapter:

# struct StepperBase {

Used for dense output.

Base class for all ODE algorithms. Doub &x; Doub xold; VecDoub &y,&dydx; Doub atol,rtol; bool dense; Doub hdid; Doub hnext;

Actual stepsize accomplished by the step routine.   
Stepsize predicted by the controller for the next step.   
Doub EPS;   
Int n,neqn; neqn $= \mathbf { n }$ except for StepperStoerm.   
VecDoub yout,yerr; New value of y and error estimate.   
StepperBase(VecDoub_IO &yy, VecDoub_IO &dydxx, Doub &xx, const Doub atoll, const Doub rtoll, bool dens) : x(xx),y(yy),dydx(dydxx),atol(atoll), rtol(rtoll),dense(dens),n(y.size()),neqn(n),yout(n),yerr(n) {} Input to the constructor are the dependent variable vector y[0..n-1] and its derivative dydx[0..n-1] at the starting value of the independent variable $\mathbf { x }$ . Also input are the absolute and relative tolerances, atol and rtol, and the boolean dense, which is true if dense output is required.

# 17.0.3 The Output Object

Output is controlled by the various constructors in the Output structure. The default constructor, with no arguments, suppresses all output. The constructor with argument nsave provides dense output provided nsave $> 0$ . This means output at values of $x$ of your choosing, not necessarily the natural places that the stepper method would land. The output points are nsave $+ ~ 1$ uniformly spaced points including x1 and $_ { \tt X 2 }$ . If nsave $\leq 0$ , output is saved at every integration step, that is, only at the points where the stepper happens to land. While most of your needs should be met by these options, you should find it easy to modify Output for your particular application.

# struct Output {

Structure for output from ODE solver such as odeint.

Output() : kmax(-1),dense(false),count(0) {}   
Default constructor gives no output.   
Output(const Int nsavee) kmax(500),nsave(nsavee),count(0),xsave(kmax) Constructor provides dense output at nsave equally spaced intervals. If nsave $\leq 0$ , output is saved only at the actual integration steps.   
dense $=$ nsave > 0 ? true : false;   
}

nvar=neqn; if (kmax $= = - 1$ ) return; ysave.resize(nvar,kmax); if (dense) $\mathtt { x 1 } \mathtt { = x 1 } 0$ ; $\mathbf { x } 2 =$ xhi; xout=x1; dxout $=$ (x2-x1)/nsave; } }

void resize() {   
Resize storage arrays by a factor of two, keeping saved data. Int kold=kmax; kmax $\ast = ~ 2$ ; VecDoub tempvec(xsave);   
xsave.resize(kmax);   
for (Int $\mathtt { k } = 0$ ; k<kold; $\mathrm { k } { + } { + }$ ) xsave[k] $=$ tempvec[k];   
MatDoub tempmat(ysave);   
ysave.resize(nvar,kmax);   
for (Int $\scriptstyle \dot { 1 } = 0$ ; i<nvar; $\dot { 1 } + +$ ) for (Int $\mathtt { k } = 0$ ; k<kold; $\mathrm { k } { + + }$ ) ysave[i][k] $=$ tempmat[i][k];

# }

template <class Stepper>   
void save_dense(Stepper &s, const Doub xout, const Doub h) {   
Invokes dense_out function of stepper routine to produce output at xout. Normally called by out rather than directly. Assumes that xout is between xold and $\mathtt { x o l d + h }$ , where the stepper must keep track of xold, the location of the previous step, and $\mathtt { x } = \mathtt { x } \circ \mathtt { l d } + \mathtt { h }$ , the current step. if (count $= =$ kmax) resize(); for (Int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<nvar; $\dot { \bf 1 } + + \dot { }$ ) ysave[i][count] $= \tt s$ .dense_out(i,xout,h); xsave[count++] $=$ xout;   
}   
void save(const Doub x, VecDoub_I &y) {   
Saves values of current x and $\mathtt { y }$ . if (kmax $\scriptstyle < = 0$ ) return; if (count $= =$ kmax) resize(); for (Int $\scriptstyle \dot { 1 } = 0$ ;i<nvar; $\dot { 1 } + + \dot { 2 }$ ) ysave[i][count]=y[i]; xsave[count $+ + ] = _ { \mathbb { X } }$ ;

# template <class Stepper>

void out(const Int nstp,const Doub x,VecDoub_I &y,Stepper &s,const Doub h) { Typically called by Odeint to produce dense output. Input variables are nstp, the current step number, the current values of $\mathbf { x }$ and y, the stepper s, and the stepsize h. A call with nstp $\scriptstyle 1 = - 1$ saves the initial values. The routine checks whether $\mathbf { x }$ is greater than the desired output point xout. If so, it calls save_dense.

if (!dense) throw("dense output not set in Output!"); if (nstp $\mathbf { \Phi } = \mathbf { \Phi } - 1 \mathbf { \Phi }$ ) { save(x,y); xout $+ =$ dxout; } else { while $( ( \bf { x } - \bf { x } \mathrm { o u t } ) * ( \bf { x } 2 - \bf { x } 1 ) > 0 . 0 )$ { save_dense(s,xout,h); xout $+ =$ dxout; } } } };

# 17.0.4 A Quick-Start Example

Before we dive deep into the pros and cons of the different stepper types (the meat of this chapter), let’s see how to code the solution of an actual problem. Suppose we want to solve Van der Pol’s equation, which when written in first-order form is

$$
\begin{array} { l } { y _ { 0 } ^ { \prime } = y _ { 1 } } \\ { y _ { 1 } ^ { \prime } = [ ( 1 - y _ { 0 } ^ { 2 } ) y _ { 1 } - y _ { 0 } ] / \epsilon } \end{array}
$$

First encapsulate (17.0.4) in a functor (see $\ S 1 . 3 . 3 )$ . Using a functor instead of a bare function gives you the opportunity to pass other information to the function, such as the values of fixed parameters. Every stepper class in this chapter is accordingly templated on the type of the functor defining the right-hand side derivatives. For our example, the right-hand side functor looks like:

struct rhs_van { Doub eps; rhs_van(Doub epss) : eps(epss) {} void operator() (const Doub x, VecDoub_I &y, VecDoub_O &dydx) { dydx[ $\mathrm { . 0 ] = y [ 1 ] }$ ; dydx[1] $=$ ((1.0-y[0]\*y[0])\*y[1]-y[0])/eps; }   
};

The key thing is the line beginning void operator(): It always should have this form, with the definition of dydx following. Here we have chosen to specify $\epsilon$ as a parameter in the constructor so that the main program can easily pass a specific value to the right-hand side. Alternatively, you could have omitted the constructor, relying on the compiler-supplied default constructor, and hard-coded a value of $\epsilon$ in the routine. Note, of course, that there is nothing special about the name rhs_van.

We will integrate from 0 to 2 with initial conditions $y _ { 0 } = 2$ , $y _ { 1 } = 0$ and with $\epsilon = 1 0 ^ { - 3 }$ . Then your main program will have declarations like the following:

const Int nvar $^ { * 2 }$ ;   
const Doub atol $= 1$ .0e-3, rtol=atol, h1=0.01, hmin=0.0, x1=0.0, x2=2.0;   
VecDoub ystart(nvar);   
ystart[0] $= 2 . 0$ ;   
ystart[1] ${ = } 0$ .0;   
Output out(20); Dense output at 20 points plus x1.   
rhs_van d(1.0e-3); Declare d as a rhs_van object.   
Odeint<StepperDopr5<rhs_van> $>$ ode(ystart,x1,x2,atol,rtol,h1,hmin,out,d);   
ode.integrate();

Note how the Odeint object is templated on the stepper, which in turn is templated on the derivative object, rhs_van in this case. The space between the two closing angle brackets is necessary; otherwise the compiler parses $> >$ as the right-shift operator!

The number of good steps taken is available in ode.nok and the number of bad steps in ode.nbad. The output, which is equally spaced, can be printed by statements like

for (Int $\scriptstyle { \dot { 1 } } = 0$ ;i<out.count;i++) cout $< <$ out.xsave[i] << " " << out.ysave[0][i] << " " << out.ysave[1][i] << endl;

You can alternatively save output at the actual integration steps by the declaration

Output out(-1);

or suppress all saving of output with

# Output out;

In this case, the solution values at the endpoint are available in ystart[0] and ystart[1], overwriting the starting values.

# CITED REFERENCES AND FURTHER READING:

Gear, C.W. 1971, Numerical Initial Value Problems in Ordinary Differential Equations (Englewood Cliffs, NJ: Prentice-Hall).

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), Chapter 5.   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), Chapter 7.   
Hairer, E., Nørsett, S.P., and Wanner, G. 1993, Solving Ordinary Differential Equations I. Nonstiff Problems, 2nd ed. (New York: Springer)   
Hairer, E., Nørsett, S.P., and Wanner, G. 1996, Solving Ordinary Differential Equations II. Stiff and Differential-Algebraic Problems,2nd ed. (New York: Springer)   
Lambert, J. 1973, Computational Methods in Ordinary Differential Equations (New York: Wiley).   
Lapidus, L., and Seinfeld, J. 1971, Numerical Solution of Ordinary Differential Equations (New York: Academic Press).

# 17.1 Runge-Kutta Method

The formula for the Euler method is

$$
y _ { n + 1 } = y _ { n } + h f ( x _ { n } , y _ { n } )
$$

which advances a solution from $x _ { n }$ to $x _ { n + 1 } \equiv x _ { n } + h$ . The formula is unsymmetrical: It advances the solution through an interval $h$ , but uses derivative information only at the beginning of that interval (see Figure 17.1.1). That means (and you can verify by expansion in power series) that the step’s error is only one power of $h$ smaller than the correction, i.e., $O ( h ^ { 2 } )$ added to (17.1.1).

There are several reasons that Euler’s method is not recommended for practical use, among them, (i) the method is not very accurate when compared to other, fancier, methods run at the equivalent stepsize, and (ii) neither is it very stable (see $\ S 1 7 . 5$ below).

Consider, however, the use of a step like (17.1.1) to take a “trial” step to the midpoint of the interval. Then use the values of both $x$ and $y$ at that midpoint to compute the “real” step across the whole interval. Figure 17.1.2 illustrates the idea. In equations,

$$
\begin{array} { c } { { k _ { 1 } = h f ( x _ { n } , y _ { n } ) } } \\ { { k _ { 2 } = h f \left( x _ { n } + \frac { 1 } { 2 } h , y _ { n } + \frac { 1 } { 2 } k _ { 1 } \right) } } \\ { { y _ { n + 1 } = y _ { n } + k _ { 2 } + O ( h ^ { 3 } ) } } \end{array}
$$

As indicated in the error term, this symmetrization cancels out the first-order error term, making the method second order. [A method is conventionally called $n$ th order if its error term is $O ( h ^ { n + 1 } ) . ]$ In fact, (17.1.2) is called the second-order Runge-Kutta or midpoint method.

We needn’t stop there. There are many ways to evaluate the right-hand side $f ( x , y )$ that all agree to first order, but that have different coefficients of higher-order error terms. Adding up the right combination of these, we can eliminate the error terms order by order. That is the basic idea of the Runge-Kutta method. Abramowitz and Stegun [1] and Gear [2] give various specific formulas that derive from this basic idea. By far the most often used is the classical fourth-order Runge-Kutta formula, which has a certain sleekness of organization about it:

![](images/d889331628b222ffabf5272ce6d68aae6f0a41aff0467dfeb17ae5bf1affffd9.jpg)  
Figure 17.1.1. Euler’s method. In this simplest (and least accurate) method for integrating an ODE, the derivative at the starting point of each interval is extrapolated to find the next function value. The method has first-order accuracy.

![](images/3e9759ecbd503feb65194223881e89214095938257ab20d0f67134bf472da55e.jpg)  
Figure 17.1.2. Midpoint method. Second-order accuracy is obtained by using the initial derivative at each step to find a point halfway across the interval, then using the midpoint derivative across the full width of the interval. In the figure, filled dots represent final function values, while open dots represent function values that are discarded once their derivatives have been calculated and used.

$$
\begin{array} { l } { { k _ { 1 } = h f ( x _ { n } , y _ { n } ) } } \\ { { k _ { 2 } = h f ( x _ { n } + \frac { 1 } { 2 } h , y _ { n } + \frac { 1 } { 2 } k _ { 1 } ) } } \\ { { k _ { 3 } = h f ( x _ { n } + \frac { 1 } { 2 } h , y _ { n } + \frac { 1 } { 2 } k _ { 2 } ) } } \\ { { k _ { 4 } = h f ( x _ { n } + h , y _ { n } + k _ { 3 } ) } } \\ { { y _ { n + 1 } = y _ { n } + \frac { 1 } { 6 } k _ { 1 } + \frac { 1 } { 3 } k _ { 2 } + \frac { 1 } { 3 } k _ { 3 } + \frac { 1 } { 6 } k _ { 4 } + O ( h ^ { 5 } ) } } \end{array}
$$

The fourth-order Runge-Kutta method requires four evaluations of the righthand side per step $h$ (see Figure 17.1.3). This will be superior to the midpoint method (17.1.2) $i f$ at least twice as large a step is possible with (17.1.3) for the same accuracy. Is that so? The answer is: often, perhaps even usually, but surely not always! This takes us back to a central theme, namely that high order does not always mean high accuracy. The statement “fourth-order Runge-Kutta is generally superior to secondorder” is a true one, but as much a statement about the kind of problems that people solve as a statement about strict mathematics.

For many scientific users, fourth-order Runge-Kutta is not just the first word on ODE integrators, but the last word as well. In fact, you can get pretty far on this old workhorse, especially if you combine it with an adaptive stepsize algorithm. Keep in mind, however, that the old workhorse’s last trip may well be to take you to the poorhouse: Newer Runge-Kutta methods are much more efficient, and Bulirsch-Stoer or predictor-corrector methods can be even more efficient for problems where very high accuracy is a requirement. Those methods are the high-strung racehorses. Runge-Kutta is for ploughing the fields. However, even the old workhorse is more nimble with new horseshoes. In $\ S 1 7 . 2$ we will give a modern implementation of a Runge-Kutta method that is quite competitive as long as very high accuracy is not required. An excellent discussion of the pitfalls in constructing a good Runge-Kutta code is given in [3].

![](images/5c1cf4aee6a5c3cc7199026b5bd7d681d9dcdc38d638479d9fe8d5dcc4c0be4b.jpg)  
Figure 17.1.3. Fourth-order Runge-Kutta method. In each step the derivative is evaluated four times: once at the initial point, twice at trial midpoints, and once at a trial endpoint. From these derivatives the final function value (shown as a filled dot) is calculated. (See text for details.)

Here is the routine $\tt r k 4$ for carrying out one classical Runge-Kutta step on a set of n differential equations. This routine is completely separate from the various stepper routines introduced in the previous section and given in the rest of the chapter. It is meant for only the most trivial applications. You input the values of the independent variables, and you get out new values that are stepped by a stepsize h (which can be positive or negative). You will notice that the routine requires you to supply not only function derivs for calculating the right-hand side, but also values of the derivatives at the starting point. Why not let the routine call derivs for this first value? The answer will become clear only in the next section, but in brief is this: This call may not be your only one with these starting conditions. You may have taken a previous step with too large a stepsize, and this is your replacement. In that case, you do not want to call derivs unnecessarily at the start. Note that the routine that follows has, therefore, only three calls to derivs.

void rk4(VecDoub_I &y, VecDoub_I &dydx, const Doub x, const Doub h, VecDoub_O &yout, void derivs(const Doub, VecDoub_I &, VecDoub_O &))

Given values for the variables $\mathtt { y } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ and their derivatives dydx[0..n-1] known at x, use the fourth-order Runge-Kutta method to advance the solution over an interval h and return the incremented variables as yout[0..n-1]. The user supplies the routine derivs(x,y,dydx), which returns derivatives dydx at x.

Int n=y.size();   
VecDoub dym(n),dyt(n),yt(n);   
Doub hh=h\*0.5;   
Doub h6=h/6.0;   
Doub xh=x+hh; First step.   
Second step.   
for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) yt[i]=y[i]+hh\*dydx[i];   
derivs(xh,yt,dyt);   
for (Int $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) yt[i]=y[i]+hh\*dyt[i];   
derivs(xh,yt,dym);   
for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) { yt[i]=y[i]+h\*dym[i]; dym[i] $+ =$ dyt[i];   
}   
derivs(x+h,yt,dyt);   
for (Int $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) yout[i]=y[i]+h6\*(dydx[i]+dyt[i]+2.0\*dym[i]);

Third step.

Fourth step. Accumulate increments with proper weights.

The Runge-Kutta method treats every step in a sequence of steps in an identical manner. Prior behavior of a solution is not used in its propagation. This is mathematically proper, since any point along the trajectory of an ordinary differential equation can serve as an initial point. The fact that all steps are treated identically also makes it easy to incorporate Runge-Kutta into relatively simple “driver” schemes.

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, $\ S 2 5 . 5$ .[1]   
Gear, C.W. 1971, Numerical Initial Value Problems in Ordinary Differential Equations (Englewood Cliffs, NJ: Prentice-Hall), Chapter 2.[2]   
Shampine, L.F., and Watts, H.A. 1977, “The Art of Writing a Runge-Kutta Code, Part I,” in Mathematical Software Ill, J.R. Rice,ed. (New York: Academic Press)，pp. 257-275；1979, “The Art of Writing a Runge-Kutta Code. II,” Applied Mathematics and Computation, vol. 5, pp. 93–121.[3]

# 17.2 Adaptive Stepsize Control for Runge-Kutta

A good ODE integrator should exert some adaptive control over its own progress, making frequent changes in its stepsize. Usually the purpose of this adaptive stepsize control is to achieve some predetermined accuracy in the solution with minimum computational effort. Many small steps should tiptoe through treacherous terrain, while a few great strides should speed through smooth uninteresting countryside. The resulting gains in efficiency are not mere tens of percents or factors of two; they can sometimes be factors of ten, a hundred, or more. Sometimes accuracy may be demanded not directly in the solution itself, but in some related conserved quantity that can be monitored.

Implementation of adaptive stepsize control requires that the stepping algorithm signal information about its performance, most important, an estimate of its truncation error. In this section we will learn how such information can be obtained. Obviously, the calculation of this information will add to the computational overhead, but the investment will generally be repaid handsomely.

With fourth-order Runge-Kutta, the most straightforward technique by far is step doubling (see, e.g., [1]). We take each step twice, once as a full step, then, independently, as two half-steps (see Figure 17.2.1). How much overhead is this, say in terms of the number of evaluations of the right-hand sides? Each of the three separate Runge-Kutta steps in the procedure requires 4 evaluations, but the single and double sequences share a starting point, so the total is 11. This is to be compared not to 4, but to 8 (the two half-steps), since — stepsize control aside — we are achieving the accuracy of the smaller (half-) stepsize. The overhead cost is therefore a factor 1.375. What does it buy us?

Let us denote the exact solution for an advance from $x$ to $x + 2 h$ by $y ( x + 2 h )$ and the two approximate solutions by $y _ { 1 }$ (one step $2 h$ ) and $y _ { 2 }$ (two steps each of size $h$ ). Since the basic method is fourth order, the true solution and the two numerical approximations are related by

$$
\begin{array} { c } { { y ( x + 2 h ) = y _ { 1 } + ( 2 h ) ^ { 5 } \phi + O ( h ^ { 6 } ) + \ldots } } \\ { { y ( x + 2 h ) = y _ { 2 } + 2 ( h ^ { 5 } ) \phi + O ( h ^ { 6 } ) + \ldots . } } \end{array}
$$

where, to order $h ^ { 5 }$ , the value $\phi$ remains constant over the step. [Taylor series expansion tells us the $\phi$ is a number whose order of magnitude is $y ^ { ( 5 ) } ( x ) / 5 ! . ]$ The first expression in (17.2.1) involves $( 2 h ) ^ { 5 }$ since the stepsize is $2 h$ , while the second expression involves $2 ( h ^ { 5 } )$ since the error on each step is $h ^ { 5 } \phi$ . The difference between the two numerical estimates is a convenient indicator of truncation error,

$$
\Delta \equiv y _ { 2 } - y _ { 1 }
$$

It is this difference that we shall endeavor to keep to a desired degree of accuracy, neither too large nor too small. We do this by adjusting $h$ .

It might also occur to you that, ignoring terms of order $h ^ { 6 }$ and higher, we can solve the two equations in (17.2.1) to improve our numerical estimate of the true solution $y ( x + 2 h )$ , namely,

$$
y ( x + 2 h ) = y _ { 2 } + \frac { \Delta } { 1 5 } + O ( h ^ { 6 } )
$$

This estimate is accurate to fifth order, one order higher than the original Runge-Kutta steps (Richardson extrapolation again!). However, we can’t have our cake and eat it too: (17.2.3) may be fifth-order accurate, but we have no way of monitoring its truncation error. Higher order is not always higher accuracy! Use of (17.2.3) rarely does harm, but we have no way of directly knowing whether it is doing any good. Therefore we should use $\Delta$ as the error estimate and take as “gravy” any additional accuracy gain derived from (17.2.3). In the technical literature, use of a procedure like (17.2.3) is called “local extrapolation.”

Step doubling has been superseded by a more efficient stepsize adjustment algorithm based on embedded Runge-Kutta formulas, originally invented by Merson and popularized in a method of Fehlberg. An interesting fact about Runge-Kutta formulas is that for orders $M$ higher than four, more than $M$ function evaluations are required. This accounts for the popularity of the classical fourth-order method: It seems to give the most bang for the buck. However, Fehlberg discovered a fifthorder method with six function evaluations where another combination of the six functions gives a fourth-order method. The difference between the two estimates of $y ( x + h )$ can then be used as an estimate of the truncation error to adjust the stepsize. Since Fehlberg’s original formula, many other embedded Runge-Kutta formulas have been found.

![](images/6bc89a09f872592ea7be85af036f6dfb49de9658f84b97396d40a4c630620f51.jpg)  
Figure 17.2.1. Step doubling as a means for adaptive stepsize control in fourth-order Runge-Kutta. Points where the derivative is evaluated are shown as filled circles. The open circle represents the same derivatives as the filled circle immediately above it, so the total number of evaluations is 11 per two steps. Comparing the accuracy of the big step with the two small steps gives a criterion for adjusting the stepsize on the next step, or for rejecting the current step as inaccurate.

As an aside, the general question of how many function evaluations are required for a Runge-Kutta method of a given order is still open. Order 5 requires 6 function evaluations, order 6 requires 7, order 7 requires 9, order 8 requires 11. It is known that for order $M \ \geq \ 8$ , at least $M + 3$ evaluations are required. The highest order explicitly constructed method so far is order 10, with 17 evaluations. The calculation of the coefficients of these high-order methods is very complicated.

We will spend most of this section setting up an efficient fifth-order Runge-Kutta method, coded in the routine StepperDopr5. This will allow us to explore the various issues that have to be dealt with in any Runge-Kutta scheme. However, ultimately you should not use this routine except for low accuracy requirements $( \lesssim$ $1 0 ^ { - 3 } )$ ) or trivial problems. Use the more efficient higher-order Runge-Kutta code StepperDopr853 or the Bulirsch-Stoer code StepperBS.

The general form of a fifth-order Runge-Kutta formula is

$$
\begin{array} { r l } & { k _ { 1 } = h f ( x _ { n } , y _ { n } ) } \\ & { k _ { 2 } = h f ( x _ { n } + c _ { 2 } h , y _ { n } + a _ { 2 1 } k _ { 1 } ) } \\ & { ~ \qquad \cdots } \\ & { k _ { 6 } = h f ( x _ { n } + c _ { 6 } h , y _ { n } + a _ { 6 1 } k _ { 1 } + \cdots + a _ { 6 5 } k _ { 5 } ) } \\ & { y _ { n + 1 } = y _ { n } + b _ { 1 } k _ { 1 } + b _ { 2 } k _ { 2 } + b _ { 3 } k _ { 3 } + b _ { 4 } k _ { 4 } + b _ { 5 } k _ { 5 } + b _ { 6 } k _ { 6 } + O ( h ^ { 6 } ) } \end{array}
$$

The embedded fourth-order formula is

$$
y _ { n + 1 } ^ { * } = y _ { n } + b _ { 1 } ^ { * } k _ { 1 } + b _ { 2 } ^ { * } k _ { 2 } + b _ { 3 } ^ { * } k _ { 3 } + b _ { 4 } ^ { * } k _ { 4 } + b _ { 5 } ^ { * } k _ { 5 } + b _ { 6 } ^ { * } k _ { 6 } + O ( h ^ { 5 } )
$$

and so the error estimate is

$$
\Delta \equiv y _ { n + 1 } - y _ { n + 1 } ^ { * } = \sum _ { i = 1 } ^ { 6 } ( b _ { i } - b _ { i } ^ { * } ) k _ { i }
$$

The particular values of the various constants that we favor are those found by Dormand and Prince [2] and given in the table on the next page. These give a more efficient method than Fehlberg’s original values, with better error properties.

We said that the Dormand-Prince method needs six function evaluations per step, yet the table on the next page shows seven and the sums in equations (17.2.5) and (17.2.6) should really go up to $i \ = \ 7$ . What’s going on? The idea is to use $y _ { n + 1 }$ itself to provide a seventh stage. Because $f ( x _ { n } + h , y _ { n + 1 } )$ has to be evaluated anyway to start the next step, this costs nothing (unless the step is rejected because the error is too big). This trick is called FSAL (first-same-as-last). You can see in the table that the coefficients in the last row are the same as the $b _ { i }$ column.

<table><tr><td colspan="11">Dormand-Prince 5(4) Parameters for Embedded Runga-Kutta Method</td></tr><tr><td>i</td><td>Ci</td><td colspan="6">aij</td><td>bi 35</td><td></td><td>b</td></tr><tr><td>1</td><td></td><td colspan="6"></td><td></td><td>384</td><td>5179 57600</td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0 500</td><td></td><td>0 7571</td></tr><tr><td>3</td><td></td><td></td><td>品</td><td></td><td></td><td></td><td></td><td>1113 125</td><td></td><td>16695 393</td></tr><tr><td>4</td><td></td><td>4</td><td>5</td><td>3</td><td></td><td></td><td></td><td></td><td>192</td><td>640 92097</td></tr><tr><td>5</td><td></td><td>19372 6561</td><td>25360 2187</td><td>64448 6561</td><td>212 729</td><td>5103</td><td></td><td></td><td>2187 6784</td><td>339200</td></tr><tr><td>6</td><td>1</td><td>9017 3168</td><td>355 33</td><td>46732 5247</td><td>49 176</td><td>18656</td><td></td><td></td><td>11 84</td><td>187 2100</td></tr><tr><td>7</td><td>1</td><td>35 384</td><td>0</td><td>500 1113</td><td>125 192</td><td>2187 6784</td><td>8</td><td></td><td>0</td><td>1 40</td></tr><tr><td>j=</td><td colspan="2"></td><td>1 2</td><td>3</td><td>4</td><td></td><td>5</td><td>6</td><td></td><td></td></tr></table>

Now that we know, at least approximately, what our error is, we need to consider how to keep it within desired bounds. We require

$$
| \Delta | = | y _ { n + 1 } - y _ { n + 1 } ^ { * } | \leq \mathsf { s c a l e }
$$

where

$$
\mathtt { s c a l e } = \mathtt { a t o l } + | y | \mathtt { r t o l }
$$

Here atol is the absolute error tolerance and rtol is the relative error tolerance. (Practical detail: In a code, you use $\operatorname* { m a x } ( | y _ { n } | , | y _ { n + 1 } | )$ for $| y |$ in the above formula in case one of them is close to zero.)

Our notation hides the fact that $\Delta$ is actually a vector of desired accuracies, $\Delta _ { i }$ , one for each equation in the set of ODEs. In practice one takes some norm of the vector $\Delta$ . While taking the maximum component value is fine (i.e., rescaling the stepsize according to the needs of the “worst-offender” equation), we will use the usual Euclidean norm. Also, while atol and rtol could be different for each component of $y$ , we will take them as constant. So define

$$
\mathrm { e r r } = \sqrt { \frac { 1 } { N } \sum _ { i = 0 } ^ { N - 1 } \left( \frac { \Delta _ { i } } { \tt s c a l e } _ { i } \right) ^ { 2 } }
$$

and accept the step if $\mathbf { e r r } \leq 1$ , otherwise reject it.

What is the relation between the scaled error err and $h ?$ According to (17.2.4) $_ - \left( 1 7 . 2 . 5 \right)$ , $\Delta$ scales as $h ^ { 5 }$ and hence so does err. If we take a step $h _ { 1 }$ and produce an error $\tt e r r 1$ , therefore, the step $h _ { 0 }$ that would have given some other value ${ \tt e r r } _ { 0 }$ is readily estimated as

$$
h _ { 0 } = h _ { 1 } \left| \frac { \mathrm { e r r } _ { 0 } } { \mathrm { e r r } _ { 1 } } \right| ^ { 1 / 5 }
$$

Let $\mathtt { e r r 0 }$ denote the desired error, which is 1 in an efficient integration. Then equation (17.2.10) is used in two ways: If $\tt e r r 1$ is larger than 1 in magnitude, the equation tells how much to decrease the stepsize when we retry the present (failed) step. If $\tt e r r 1$ is smaller than 1, on the other hand, then the equation tells how much we can safely increase the stepsize for the next step. Local extrapolation means that we use the fifth-order value $y _ { n + 1 }$ , even though the error estimate actually applies to the fourth-order value ynC1.

How is the quantity err related to some looser prescription like “get a solution good to one part in $1 0 ^ { 6 ^ { , 9 } \cdot } \ ?$ That can be a subtle question, and it depends on exactly what your application is. You may be dealing with a set of equations whose dependent variables differ enormously in magnitude. In that case, you probably want to use fractional errors, $\mathsf { a t o l } = 0$ , $\tt r t o l = \epsilon$ , where $\epsilon$ is the number like $1 0 ^ { - 6 }$ or whatever. On the other hand, you may have oscillatory functions that pass through zero but are bounded by some maximum values. In that case you probably want to set ato $1 = { \tt r t o l } = \epsilon$ . This latter choice is the safest in general, and should usually be your first choice.

Here is a more technical point. The error criteria mentioned thus far are “local,” in that they bound the error of each step individually. In some applications you may be unusually sensitive about a “global” accumulation of errors, from beginning to end of the integration and in the worst possible case where the errors all are presumed to add with the same sign. Then, the smaller the stepsize $h$ , the more steps between your starting and ending values of $x$ . In such a case you might want to set scale proportional to $h$ , typically to something like

$$
\mathtt { s c a l e } = \epsilon h \times \mathtt { d y d x } [ \mathrm { i } ]
$$

This enforces fractional accuracy $\epsilon$ not on the values of $y$ but (much more stringently) on the increments to those values at each step. But now look back at (17.2.10). The exponent $1 / 5$ is no longer correct: When the stepsize is reduced from a too-large value, the new predicted value $h _ { 1 }$ will fail to meet the desired accuracy when scale is also altered to this new $h _ { 1 }$ value. Instead of $1 / 5$ , we must scale by the exponent $1 / 4$ for things to work out.

Error control that tries to constrain the global error by setting the scale factor proportional to $h$ is called “error per unit step,” as opposed to the original “error per step” method. As a point of principle, controlling the global error by controlling the local error is very difficult. The global error at any point is the sum of the global error up to the start of the last step plus the local error of that step. This cumulative nature of the global error means it depends on things that cannot always be controlled, like stability properties of the differential equation. Accordingly, we recommend the straightforward “error per step” method in most cases. If you want to estimate the global error of your solution, you have to integrate again with a reduced tolerance and use the change in the solution as an estimate of the global error. This works $i f$ the stepsize controller produces errors roughly proportional to the tolerance, which is not always guaranteed.

Because our error estimates are not exact, but only accurate to the leading order in $h$ , we are advised to put in a safety factor $S$ that is a few percent smaller than unity. Equation (17.2.10) (with $\mathbf { e r r } _ { 0 } = 1$ and the subscripts $1  n$ and $0  n + 1 \gamma$ ) is thus replaced by

$$
h _ { n + 1 } = S h _ { n } \left( { \frac { 1 } { \mathrm { e r r } _ { n } } } \right) ^ { 1 / 5 }
$$

Moreover, experience shows that it is not wise to let the stepsize increase or decrease too fast, and not to let the stepsize increase at all if the previous step was rejected. In StepperDopr5, the stepsize cannot increase by more than a factor of 10 nor decrease by more than a factor of 5 in a single step.

# 17.2.1 Pl Stepsize Control

One situation in which the above stepsize controller has difficulty is when the stepsize is being limited by the stability properties of the integration method, rather than the accuracy of the individual steps. (We will see more about this in $\ S 1 7 . 5$ o n stiff differential equations.) The stepsize increases slowly as successive steps are accepted, until the method becomes unstable. The controller responds to the sudden increase in the error by cutting the stepsize drastically, and the cycle repeats itself. Similar problems can occur when the solution to the differential equation enters a region with drastically different behavior than the previous region. A long sequence of alternating accepted and rejected steps ensues. Since rejected steps are expensive, it is worth improving the stepsize control.

The most effective way to do this seems to be to use ideas from control theory. The integration routine and the differential equation play the role of the process, like a chemical plant manufacturing a product. The stepsize $h$ is the input and the error estimate err is the output. (The numerical solution is also output, but it is not used for stepsize control.) The controller is the stepsize control algorithm. It tries to hold the error at the prescribed tolerance by varying the stepsize. Deriving an improved stepsize controller from control theory ideas is beyond our scope here, so we will introduce some basic concepts and then refer you to the literature for derivations and a fuller explanation [6-8].

The standard stepsize controller (17.2.12), when expressed in the language of control theory, is known as an integrating controller, with $\log h$ as the discrete control variable. This means that the control variable is obtained by “integrating” the control error signal. It is well known in control theory that more stable control can be achieved by adding an additional term proportional to the control error. This is called a PI controller, where the $\mathrm { P }$ stands for proportional feedback and the I for integral feedback. Instead of (17.2.12), the resulting algorithm takes the simple form

$$
h _ { n + 1 } = S h _ { n } { \mathrm { e r r } } _ { n } ^ { - \alpha } { \mathrm { e r r } } _ { n - 1 } ^ { \beta }
$$

Typically $\alpha$ and $\beta$ should be scaled as $1 / k$ , where $k$ is the exponent of $h$ in err $k = 5$ for a fifth-order method). Setting $\alpha = 1 / k$ , $\beta = 0$ recovers the classical controller (17.2.12). Nonzero $\beta$ improves the stability but loses some efficiency for “easy” parts of the solution. A good compromise [6] is to set

$$
\beta \approx 0 . 4 / k , \qquad \alpha \approx 0 . 7 / k = 1 / k - 0 . 7 5 \beta
$$

# 17.2.2 Dense Output

Adaptive stepsize control means the algorithm marches along producing $y$ values at $x$ ’s that it chooses itself. What if you want output at values that you specify? The simplest option is just to integrate from one desired output point to the next. But if you specify a lot of output points, this is inefficient: The code has to take steps based on where you want output, rather than the “natural” stepsizes it would like to choose. High-order methods like to take large steps for smooth solutions, so the problem is especially acute in this case.

The solution is to find an interpolation method that uses information produced during the integration and is of an order comparable to the order of the method so that full accuracy of the solution is preserved. This is called providing a dense output method.

For example, any method has available $y$ and $d y / d x = f$ at the beginning and end of the step. These four quantities specify a cubic interpolating polynomial:

$$
y ( x _ { n } + \theta h ) = ( 1 - \theta ) y _ { n } + \theta y _ { n + 1 } + \theta ( \theta - 1 ) [ ( 1 - 2 \theta ) ( y _ { n + 1 } - y _ { n } ) + ( \theta - 1 ) h f _ { n } + \theta h f _ { n + 1 } ]
$$

where $0 ~ \leq ~ \theta ~ \leq ~ 1$ . Evaluating this polynomial at any $\theta$ in the interval gives a value of $y$ that is third-order accurate, as you can verify by Taylor expansion in $h$ . (Equation 17.2.15 is an example of Hermite interpolation, which uses both function and derivative values.)

We are interested, however, in integration methods with order higher than three, so higher-order dense output formulas are needed. The general approach for Runge-Kutta methods is to regard the $b _ { i }$ coefficients in (17.2.4) as polynomials in $\theta$ instead of constants. This defines a continuous solution,

$$
y ( x _ { n } + \theta h ) = y _ { n } + b _ { 1 } ( \theta ) k _ { 1 } + b _ { 2 } ( \theta ) k _ { 2 } + b _ { 3 } ( \theta ) k _ { 3 } + b _ { 4 } ( \theta ) k _ { 4 } + b _ { 5 } ( \theta ) k _ { 5 } + b _ { 6 } ( \theta ) k _ { 6 }
$$

and we require the polynomials $b _ { i } ( \theta )$ to approximate the true solution to the required order. Equation (17.2.15) is a special case of this.

The Dormand-Prince fifth-order method allows dense output of order four without any further function evaluations. This is usually sufficient: The number of steps to get to a typical point scales as $1 / h$ , so the global error at that point is typically $O ( h ^ { 5 } )$ (fourth order). (Fifth-order dense output, needed, for example, for full accuracy in $y ^ { \prime } ( x _ { n } + \theta h )$ , turns out to need two extra function evaluations per step.) StepperDopr5 contains a dense output option based on the formulas in [3] as simplified in [4].

Dense output simplifies problems where you don’t know in advance how far to integrate. You want to locate the position $x _ { c }$ where some condition is satisfied. Examples include integrating the equations of stellar structure out from the center of the star until the pressure goes to zero at the surface, or the study of limit cycles when one integrates until the solution reaches the Poincare section for the first time.´ Write the condition as finding the zero of some function:

$$
g \left( x , y _ { i } ( x ) \right) = 0
$$

Monitor $g$ in the output routine. When $g$ changes sign between two steps, use the dense output routine to supply function values to your favorite root-finding routine, such as bisection or Newton’s method.

# 17.2.3 Implementation

Here follows the implementation of the fifth-order Dormand-Prince method.

# template <class D>

struct StepperDopr5 : StepperBase {   
Dormand-Prince fifth-order Runge-Kutta step with monitoring of local truncation error to ensure accuracy and adjust stepsize.

typedef D Dtype; Make the type of derivs a VecDoub k2,k3,k4,k5,k6; VecDoub rcont1,rcont2,rcont3,rcont4,rcont5; VecDoub dydxnew; StepperDopr5(VecDoub_IO &yy, VecDoub_IO &dydxx, Doub &xx, const Doub atoll, const Doub rtoll, bool dens); void step(const Doub htry,D &derivs); void dy(const Doub h,D &derivs); void prepare_dense(const Doub h,D &derivs); Doub dense_out(const Int i, const Doub x, const Doub h); Doub error(); struct Controller { Doub hnext,errold; bool reject; Controller(); bool success(const Doub err, Doub &h); }; Controller con; };

The constructor simply invokes the base class instructor and initializes variables:

template <class D>   
StepperDopr5<D>::StepperDopr5(VecDoub_IO &yy,VecDoub_IO &dydxx,Doub &xx, const Doub atoll,const Doub rtoll,bool dens) StepperBase(yy,dydxx,xx,atoll,rtoll,dens), k2(n),k3(n),k4(n),k5(n),k6(n), rcont1(n),rcont2(n),rcont3(n),rcont4(n),rcont5(n),dydxnew(n) {   
Input to the constructor are the dependent variable $\mathtt { y } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ and its derivative dydx[0..n-1]   
at the starting value of the independent variable x. Also input are the absolute and relative   
tolerances, atol and rtol, and the boolean dense, which is true if dense output is required. EPS=numeric_limits<Doub>::epsilon();

}

The step method is the actual stepper. It attempts a step, invokes the controller to decide whether to accept the step or try again with a smaller stepsize, and sets up the coefficients in case dense output is needed between $x$ and $x + h$ .

# template <class D>

void StepperDopr5<D>::step(const Doub htry,D &derivs) {

Attempts a step with stepsize htry. On output, y and $\mathbf { x }$ are replaced by their new values, hdid is the stepsize that was actually accomplished, and hnext is the estimated next stepsize.

Doub h=htry; Set stepsize to the initial trial value.   
for (;;) { dy(h,derivs); Take a step. Doub err $\underline { { \underline { { \cdot } } } } =$ error(); Evaluate accuracy. if (con.success(err,h)) break; Step rejected. Try again with reduced h set if (abs(h) $< =$ abs(x)\*EPS) by controller. throw("stepsize underflow in StepperDopr5");   
}   
if (dense) Step succeeded. Compute coefficients for dense prepare_dense(h,derivs); output.   
dydx=dydxnew; Reuse last derivative evaluation for next step.   
y=yout;   
xold=x; Used for dense output.   
$\texttt { x } + =$ (hdid $\mathbf { \tau } = \mathbf { h }$ );   
hnext $=$ con.hnext;

# stepperdopr5.h

The algorithm routine dy does the six steps plus the seventh FSAL step, and computes $y _ { n + 1 }$ and the error $\Delta$ .

template <class D>   
void StepperDopr5<D>::dy(const Doub h,D &derivs) {   
Given values for n variables $\mathtt { y } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ and their derivatives dydx[0..n-1] known at x, use the   
fifth-order Dormand-Prince Runge-Kutta method to advance the solution over an interval h and   
store the incremented variables in yout[0..n-1]. Also store an estimate of the local truncation   
error in yerr using the embedded fourth-order method. static const Doub $\scriptstyle { \mathtt { C } } 2 = 0$ .2, $\mathtt { C 3 = 0 }$ .3, $\mathtt { c 4 } mathtt { = 0 }$ .8, $\mathtt { C 5 } = 8$ .0/9.0,a21 ${ = } 0$ .2,a3 $_ { 1 = 3 }$ .0/40.0, a32=9.0/40.0,a41=44.0/45.0,a42 $=$ -56.0/15.0,a43=32.0/9.0,a51=19372.0/6561.0, a52 $=$ -25360.0/2187.0,a53=64448.0/6561.0,a54=-212.0/729.0,a61=9017.0/3168.0, a62=-355.0/33.0,a63=46732.0/5247.0,a64=49.0/176.0,a65=-5103.0/18656.0, a71=35.0/384.0,a73 500.0/1113.0,a74=125.0/192.0,a75=-2187.0/6784.0, a76=11.0/84.0,e1=71.0/57600.0,e3=-71.0/16695.0,e4=71.0/1920.0, e5=-17253.0/339200.0,e6=22.0/525.0,e7=-1.0/40.0; VecDoub ytemp(n); Int i; for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) First step. ytemp[i]=y[i]+h\*a21\*dydx[i]; derivs(x+c2\*h,ytemp,k2); Second step. for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n; $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \beta } } } .$ ) ytemp[i]=y[i]+h\*(a31\*dydx[i]+a32\*k2[i]); derivs(x+c3\*h,ytemp,k3); Third step. for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) ytemp[i]=y[i]+h\*(a41\*dydx[i]+a42\*k2[i]+a43\*k3[i]); derivs(x+c4\*h,ytemp,k4); Fourth step. for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n; $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \rho } } } ,$ ) ytemp[i]=y[i] $^ { + \mathrm { h * } }$ (a51\*dydx[i]+a52\*k2[i]+a53\*k3[i]+a54\*k4[i]); derivs(x+c5\*h,ytemp,k5); Fifth step. for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) ytemp[i]=y[i] $^ { + \mathrm { h * } }$ (a61\*dydx[i]+a62\*k2[i]+a63\*k3[i]+a64\*k4[i]+a65\*k5[i]); Doub xph=x+h; derivs(xph,ytemp,k6); Sixth step. for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) Accumulate increments with proper weights. yout[i]=y[i]+h\*(a71\*dydx[i]+a73\*k3[i]+a74\*k4[i]+a75\*k5[i]+a76\*k6[i]); derivs(xph,yout,dydxnew); Will also be first evaluation for next step. for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n; $\dot { 1 } + +$ ) { Estimate error as difference between fourth- and fifth-order methods. yerr[i] $- \mathrm { h * }$ (e1\*dydx[i]+e3\*k3[i]+e4\*k4[i]+e5\*k5[i]+e6\*k6[i]+e7\*dydxnew[i]); }   
}

The routine prepare_dense uses the coefficients of [4] to set up the dense output quantities. Our coding of the dense output is closely based on that of the Fortran code DOPRI5 of [5].

template <class D>   
void StepperDopr5<D>::prepare_dense(const Doub h,D &derivs) {   
Store coefficients of interpolating polynomial for dense output in rcont1...rcont5. VecDoub ytemp(n); static const Doub d1 $=$ -12715105075.0/11282082432.0, d3=87487479700.0/32700410799.0, d4=-10690763975.0/1880347072.0, d5=701980252875.0/199316789632.0, d6=-1453857185.0/822651844.0, d7=69997945.0/29380423.0; for (Int $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) { rcont1[i]=y[i]; Doub ydiff=yout[i]-y[i]; rcont2[i]=ydiff; Doub bspl $=$ h\*dydx[i]-ydiff; rcont3[i] $=$ bspl; rcont4[i] $=$ ydiff-h\*dydxnew[i]-bspl;

rcont5[i] $- \mathrm { h * }$ (d1\*dydx[i]+d3\*k3[i]+d4\*k4[i]+d5\*k5[i]+d6\*k6[i]+ d7\*dydxnew[i]); }

The next routine, dense_out, uses the coefficients stored by the previous routine to evaluate the solution at an arbitrary point.

template <class D>   
Doub StepperDopr5<D>::dense_out(const Int i,const Doub x,const Doub h) {   
Evaluate interpolating polynomial for y[i] at location $\mathbf { x }$ , where xold $\leq \mathbf { x } \leq \mathbf { x } \circ \mathbf { l } \mathsf { d } + \mathbf { h }$ . Doub $\mathbf { s } =$ (x-xold)/h; Doub s $\scriptstyle 1 = 1$ . $0 \mathrm { - s }$ ; return rcont1[i]+s\*(rcont2[i]+s1\*(rcont3[i]+s\*(rcont4[i]+s1\*rcont5[i])));

The error routine converts $\Delta$ into the scaled quantity err.

# stepperdopr5.h

template <class D>   
Doub StepperDopr5<D>::error() {   
Use yerr to compute norm of scaled error estimate. A value less than one means the step was successful.   
Doub err $\mathtt { \mathtt { \mathtt { \mathtt { \mathtt { \mathtt { \mathtt { \mathtt \beta } } } } } } } = 0$ .0,sk;   
for (Int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<n; $\dot { \bar { \lambda } } + +$ ) { sk=atol+rtol\*MAX(abs(y[i]),abs(yout[i])); err $+ =$ SQR(yerr[i]/sk);   
}   
return sqrt(err/n);

# }

Finally, the controller tests whether err $\leq 1$ and adjusts the stepsize. The default setting is beta $= 0$ (no PI control). Set beta to 0.04 or 0.08 to turn on PI control.

template <class D>   
StepperDopr5<D>::Controller::Controller() : reject(false), errold(1.0e-4) {}   
Step size controller for fifth-order Dormand-Prince method.   
template <class D>   
bool StepperDopr5<D>::Controller::success(const Doub err,Doub &h) {   
Returns true if err $\leq 1$ , false otherwise. If step was successful, sets hnext to the estimated   
optimal stepsize for the next step. If the step failed, reduces h appropriately for another try. static const Doub beta ${ = } 0$ .0,alpha ${ = } 0$ .2-beta\*0.75,saf $\mathtt { e } = 0$ .9,minscale $: = 0 \ . 2$ , maxscal $_ { \beta = 1 0 }$ .0; Set beta to a nonzero value for PI control. beta $\mathbf { \varepsilon } = \mathbf { 0 . 0 4 } – 0 . 0 8$ is a good default. Doub scale; if (err <= 1.0) { Step succeeded. Compute hnext. if (err $\scriptstyle = = \ 0 . 0$ ) scale $=$ maxscale; else { PI control if beta $\neq 0$ . scale=safe\*pow(err,-alpha)\*pow(errold,beta); if (scale<minscale) scale=minscale; Ensure minscale  hnext=h  maxscale. if (scale>maxscale) scale=maxscale; } if (reject) Don’t let step increase if last one was rehnext=h\*MIN(scale,1.0); jected. else hnext=h\*scale; errold=MAX(err,1.0e-4); Bookkeeping for next call. reject=false; return true; } else { Truncation error too large, reduce stepsize.

scale $\risingdotseq$ MAX(safe\*pow(err,-alpha),minscale); h $\ast =$ scale; reject=true; return false; } }

#

A warning: Don’t be too greedy in specifying atol and rtol. The punishment for excessive greediness is interesting and worthy of Gilbert and Sullivan’s Mikado: The routine can always achieve an apparent zero error by making the stepsize so small that quantities of order $h y ^ { \prime }$ add to quantities of order $y$ as if they were zero. Then the routine chugs happily along taking infinitely many infinitesimal steps and never changing the dependent variables one iota. (On a supercomputer, you guard against this catastrophic loss of your time allocation by signaling on abnormally small stepsizes or on the dependent variable vector remaining unchanged from step to step. On a desktop computer, you guard against it by not taking too long a lunch hour while the program is running.)

# 17.2.4 Dopr853 - An Eighth-Order Method

Once you understand the above implementation of StepperDopr5, then you have the framework for essentially any Runge-Kutta method. For production work, we recommend that you use the following method, StepperDopr853. It is again a Dormand-Prince embedded method, this time of eighth order that uses 12 function evaluations. The original version used a sixth-order embedded method for error estimation. However, it turned out that the error estimation was not robust in certain circumstances because the last evaluation point happened not to be used in computing the error. Accordingly, Hairer, Norsett, and Wanner ¨ [5] constructed both fifth-order and third-order embedded methods that use the last point. Then the error is estimated as

$$
\mathsf { e r r } = \mathsf { e r r } _ { 5 } \frac { \mathsf { e r r } _ { 5 } } { \sqrt { ( \mathsf { e r r } _ { 3 } ) ^ { 2 } + 0 . 0 1 ( \mathsf { e r r } _ { 5 } ) ^ { 2 } } }
$$

Most of the time, $\mathsf { e r r } _ { 5 } \ll \mathsf { e r r } _ { 3 }$ , so $\mathsf { e r r } = { O } ( h ^ { 8 } )$ . If the estimation breaks down so that either $_ { \tt e r r 3 }$ gets small or $_ { \tt e r r 5 }$ gets large, then err will still give a reasonable basis for stepsize control. This method has worked well in practice and is the basis for the $\mathbf { \Delta } ^ { 6 6 } 8 5 3 ^ { , 9 }$ in the name of the method.

For an eighth-order method we would like seventh-order dense output. It turns out this requires three more function evaluations. Our coding of the dense output follows closely the Fortran implementation of [5]. Since the code is somewhat lengthy, but basically similar to StepperDopr5, we give it as StepperDopr853 in a Webnote [9].

# CITED REFERENCES AND FURTHER READING:

Gear, C.W. 1971, Numerical Initial Value Problems in Ordinary Differential Equations (Englewood Cliffs, NJ: Prentice-Hall).[1]   
Dormand, J.R, and Prince, P.J. 1980, “A Family of Embedded Runge-Kutta Formulae,” Journal of Computational and Applied Mathematics,vol.6,pp.19-26.[2]   
Shampine, L.F., and Watts, H.A. 1977, “The Art of Writing a Runge-Kutta Code, Part I,” in Mathematical Software Ill,J.R. Rice,ed.(New York:Academic Press)，pp.257-275；1979, “The Art of Writing a Runge-Kutta Code. II,” Applied Mathematics and Computation, vol. 5, pp. 93–121.   
Forsythe, G.E., Malcolm, M.A., and Moler, C.B. 1977, Computer Methods for Mathematical Computations (Englewood Cliffs, NJ: Prentice-Hall).   
Dormand, J.R, and Prince, P.J. 1986, “Runge-Kutta Triples,” Computers and Mathematics with Applications,vol. 12A,pp.1007-1017.[3]   
Shampine, L.F. 1986, “Some Practical Runge-Kutta Formulas,” Mathematics of Computation, vol. 46, pp. 135–150.[4]   
Hairer, E., Nørsett, S.P., and Wanner, G. 1993, Solving Ordinary Differential Equations I. Nonstiff Problems,2nd ed. (New York: Springer).Fortran codes at http://www.unige.ch/\~hairer/software.html.[5]   
Gustafsson, K. 1991, “Control Theoretic Techniques for Stepsize Selection in Explicit Runge-Kutta Methods,” ACM Transactions on Mathematical Software, vol. 17, pp. 533-554.[6]   
Hairer, E., Nørsett, S.P., and Wanner, G. 1996, Solving Ordinary Differential Equations II. Stiff and Differential-Algebraic Problems,2nd ed. (New York: Springer),p.28.[7]   
Söderlind, G. 2003, “Digital Filters in Adaptive Time-stepping,” ACM Transactions on Mathematical Software,vol.29,pp.1-26.[8]   
Numerical Recipes Software 2007, “Routine Implementing an Eighth-order Runge-Kutta Method,” Numerical Recipes Webnote No.20,at http://www.nr.com/webnotes?20 [9]

# 17.3 Richardson Extrapolation and the Bulirsch-Stoer Method

The techniques in this section are for differential equations containing smooth functions. With just three caveats, we believe that the Bulirsch-Stoer method, discussed here, is the best-known way to obtain high accuracy solutions to ordinary differential equations with minimal computational effort. The caveats are these:

- If you have a nonsmooth problem, for example, a differential equation whose right-hand side involves a function that is evaluated by table look-up and interpolation, go back to Runge-Kutta with an adaptive stepsize choice. That method does an excellent job of feeling its way through rocky or discontinuous terrain. It is also an excellent choice for a quick-and-dirty, low accuracy solution of a set of equations.   
- The techniques in this section are not particularly good for differential equations that have singular points inside the interval of integration. A regular solution must tiptoe very carefully across such points. Runge-Kutta with adaptive stepsize can sometimes effect this; more generally, there are special techniques available for such problems, beyond our scope here but touched on in $\ S 1 8 . 6$ . There may be a few problems that are both very smooth and have right-hand sides that are very expensive to evaluate, for which predictor-corrector methods, discussed in $\ S 1 7 . 6$ , are the methods of choice.

The methods in this section involve three key ideas. The first is Richardson’s deferred approach to the limit, which we already met in $\ S 4 . 3$ on Romberg integration. The idea is to consider the final answer of a numerical calculation as itself being an analytic function (if a complicated one) of an adjustable parameter like the stepsize $h$ . That analytic function can be probed by performing the calculation with various values of $h$ , none of them being necessarily small enough to yield the accuracy that we desire. When we know enough about the function, we fit it to some analytic form and then evaluate it at that mythical and golden point $h = 0$ (see Figure 17.3.1). Richardson extrapolation is a method for turning straw into gold! (Lead into gold for alchemist readers.)

![](images/854cea8f192802addf3d02d9e69344b5b4165739204ba486782b58789b1c4efa.jpg)  
Figure 17.3.1. Richardson extrapolation as used in the Bulirsch-Stoer method. A large interval $H$ is spanned by different sequences of finer and finer substeps. Their results are extrapolated to an answer that is supposed to correspond to infinitely fine substeps. In the Bulirsch-Stoer method, the integrations are done by the modified midpoint method, and the extrapolation technique is polynomial extrapolation.

The second idea has to do with what kind of fitting function is used. Bulirsch and Stoer first recognized the strength of rational function extrapolation in Richardson-type applications. That strength is to break the shackles of the power series and its limited radius of convergence, out only to the distance of the first pole in the complex plane. Rational function fits can remain good approximations to analytic functions even after the various terms in powers of $h$ all have comparable magnitudes. In other words, $h$ can be so large as to make the whole notion of the “order” of the method meaningless — and the method can still work superbly. Nevertheless, more recent experience suggests that for smooth problems straightforward polynomial extrapolation is slightly more efficient than rational function extrapolation. (This may tell us more about the kinds of problems used for tests than about the methods themselves.) In any event, we will adopt polynomial extrapolation as our default. You might wish at this point to review $\ S 3 . 2$ , where polynomial function extrapolation was already discussed.

The third idea is to to use an integration method whose error function is strictly even, allowing the rational function or polynomial approximation to be in terms of the variable $h ^ { 2 }$ instead of just $h$ . We will expand on this idea in the next subsection, on the modified midpoint method.

Put these ideas together and you have the Bulirsch-Stoer method [1]. A single Bulirsch-Stoer step takes us from $x$ to $x + H$ , where $H$ is supposed to be quite a large — not at all infinitesimal — distance. That single step is a grand leap consisting of many (e.g., dozens to hundreds) substeps of the modified midpoint method, which are then extrapolated to zero stepsize.

# 17.3.1 Modified MidpointMethod

The modified midpoint method advances a vector of dependent variables $y ( x )$ from a point $x$ to a point $x + H$ by a sequence of $n$ substeps each of size $h$ ,

$$
h = H / n
$$

In principle, one could use the modified midpoint method in its own right as an ODE integrator. In practice, the method finds its most important application as a part of the more powerful Bulirsch-Stoer technique,.

The number of right-hand side evaluations required by the modified midpoint method is $n + 1$ . The formulas for the method are

$$
\begin{array} { c c c } { z _ { 0 } \equiv y ( x ) } & & & \\ { z _ { 1 } = z _ { 0 } + h f ( x , z _ { 0 } ) } & & \\ { z _ { m + 1 } = z _ { m - 1 } + 2 h f ( x + m h , z _ { m } ) } & { \mathrm { f o r } } & { m = 1 , 2 , \ldots , n - 1 } \\ { y ( x + H ) \approx y _ { n } \equiv \frac { 1 } { 2 } [ z _ { n } + z _ { n - 1 } + h f ( x + H , z _ { n } ) ] } & & { ( 1 7 . 3 \times \frac { n ! } { x ^ { 0 } + h ^ { 0 } } ) } \end{array}
$$

Here the $Z$ ’s are intermediate approximations that march along in steps of $h$ , while $y _ { n }$ is the final approximation to $y ( x + H )$ . The method is basically a “centered difference” or “midpoint” method (compare equation 17.1.2), except at the first and last points. Those give the qualifier “modified.”

The modified midpoint method is a second-order method, like (17.1.2), but with the advantage of requiring (asymptotically for large $n$ ) only one derivative evaluation per step $h$ instead of the two required by second-order Runge-Kutta.

The usefulness of the modified midpoint method to the Bulirsch-Stoer technique (-17.3) derives from a “deep” result about equations (17.3.2), due to Gragg. It turns out that the error of (17.3.2), expressed as a power series in $h$ , the stepsize, contains only even powers of $h$ ,

$$
y _ { n } - y ( x + H ) = \sum _ { i = 1 } ^ { \infty } \alpha _ { i } h ^ { 2 i }
$$

where $H$ is held constant but $h$ changes by varying $n$ in (17.3.1). The importance of this even power series is that, if we play our usual tricks of combining steps to knock out higher-order error terms, we can gain two orders at a time!

For example, suppose $n$ is even, and let $y _ { n / 2 }$ denote the result of applying (17.3.1) and (17.3.2) with half as many steps, $n  n / 2$ . Then the estimate

$$
y ( x + H ) \approx { \frac { 4 y _ { n } - y _ { n / 2 } } { 3 } }
$$

is fourth-order accurate, the same as fourth-order Runge-Kutta, but requires only about 1.5 derivative evaluations per step $h$ instead of Runge-Kutta’s four evaluations. Don’t be too anxious to implement (17.3.4), since we will soon do even better.

Now would be a good time to look back at the routine qsimp in $\ S 4 . 2$ , and especially to compare equation (4.2.4) with equation (17.3.4) above. You will see that the transition in Chapter 4 to the idea of Richardson extrapolation, as embodied in Romberg integration of $\ S 4 . 3$ , is exactly analogous to the transition in going from this section to the next one.

A routine that implements the modified midpoint method will be given as part of the implementation of StepperBS, in the dy member function.

# 17.3.2 The Bulirsch-Stoer Method

Consider attempting to cross the interval $H$ using the modified midpoint method with increasing values of $n$ , the number of substeps. Bulirsch and Stoer originally proposed the sequence

$$
n = 2 , 4 , 6 , 8 , 1 2 , 1 6 , 2 4 , 3 2 , 4 8 , 6 4 , 9 6 , \ldots , [ n _ { j } = 2 n _ { j - 2 } ] , \ldots
$$

More recent work by Deuflhard [2,3] suggests that the sequence

$$
n = 2 , 4 , 6 , 8 , 1 0 , 1 2 , 1 4 , \ldots , [ n _ { j } = 2 ( j + 1 ) ] , \ldots .
$$

is usually more efficient. For each step, we do not know in advance how far up this sequence we will go. After each successive $n$ is tried, a polynomial extrapolation is attempted. That extrapolation gives both extrapolated values and error estimates. If the errors are not satisfactory, we go higher in $n$ . If they are satisfactory, we go on to the next step and begin anew with $n = 2$ .

Of course there must be some upper limit, beyond which we conclude that there is some obstacle in our path in the interval $H$ , so that we must reduce $H$ rather than just subdivide it more finely. Moreover, precision loss sets in if we choose too fine a subdivision. In the implementations below, the maximum number of $n$ ’s to be tried is called KMAXX. We usually take this equal to 8; the eighth value of the sequence (17.3.6) is 16, so this is the maximum number of subdivisions of $H$ that we allow.

We enforce error control, as in the Runge-Kutta method, by monitoring internal consistency and adapting the stepsize to match a prescribed bound on the local truncation error. Each new result from the sequence of modified midpoint integrations allows a tableau like that in equation (3.2.2) to be extended by one additional set of diagonals. Write the tableau as a lower triangular matrix:

$$
\begin{array} { c c c c c } { { T _ { 0 0 } } } & { { } } & { { } } & { { } } & { { } } \\ { { T _ { 1 0 } } } & { { T _ { 1 1 } } } & { { } } & { { } } & { { } } \\ { { T _ { 2 0 } } } & { { T _ { 2 1 } } } & { { T _ { 2 2 } } } & { { } } & { { } } \\ { { \ldots } } & { { \ldots } } & { { \ldots } } & { { \ldots } } & { { } } \end{array}
$$

Here $T _ { k 0 } = y _ { k }$ , where $y _ { k }$ is $y ( x _ { n } + H )$ computed with the stepsize $h _ { k } = H / n _ { k }$ . Neville’s algorithm, equation (3.2.3), with $P$ replaced by $T$ , $x _ { i } = h _ { i } ^ { 2 }$ , and $x = 0$ , can be written

$$
T _ { k , j + 1 } = T _ { k j } + { \frac { T _ { k j } - T _ { k - 1 , j } } { ( n _ { k } / n _ { k - j } ) ^ { 2 } - 1 } } \qquad j = 0 , 1 , \ldots , k - 1
$$

Each new stepsize $h _ { i }$ starts a new row in the tableau, and then the polynomial extrapolation fills the rest of the row. Each new element in the tableau comes from the two closest elements in the previous column. Elements in the same column have the same order, and $T _ { k k }$ , the last element in each row, is the highest-order approximation with that stepsize. The difference between the last two elements in a row is taken as the (conservative) error estimate. How should we use this error estimate to adjust the stepsize? A good strategy was originally proposed by Deuflhard [2,3]. We will use a modified version [4], next described.

# 17.3.3 Stepsize Control Algorithm for Bulirsch-Stoer

The elements in the tableau are actually vectors corresponding to the vector $y$ of dependent variables. Accordingly, define

$$
\mathsf { e r r } _ { k } = \| T _ { k k } - T _ { k , k - 1 } \|
$$

where the norm is the same scaled norm used in equation (17.2.9). Error control is enforced by requiring $\mathsf { e r r } _ { k } \le 1$ .

Now $T _ { k k }$ is of order $2 k + 2$ and $T _ { k , k - 1 }$ is of order $2 k$ , which is therefore the order of $\tt e r r { k }$ . In other words,

$$
\mathbf { e r r } _ { k } \sim H ^ { 2 k + 1 }
$$

Thus a simple estimate of a new stepsize $H _ { k }$ to obtain convergence in a fixed column $k$ would be (cf. equation 17.2.12)

$$
H _ { k } = H S _ { 1 } \left( { \frac { S _ { 2 } } { \mathrm { e r r } _ { k } } } \right) ^ { 1 / ( 2 k + 1 ) }
$$

where $S _ { 1 }$ and $S _ { 2 }$ are safety factors smaller than one.

Which column $k$ should we aim to achieve convergence in? Let’s compare the work required for different $k$ . Suppose $A _ { k }$ is the work to obtain row $k$ of the extrapolation tableau. Assume the work is dominated by the cost of evaluating the functions defining the righthand sides of the differential equations. For $n _ { k }$ subdivisions in $H$ , the number of function evaluations can be found from the recurrence

$$
\begin{array} { c } { { A _ { 0 } = n _ { 0 } + 1 } } \\ { { { } } } \\ { { A _ { k + 1 } = A _ { k } + n _ { k + 1 } } } \end{array}
$$

The work per unit step to get column $k$ is therefore

$$
W _ { k } = \frac { A _ { k } } { H _ { k } }
$$

The optimal column index is the one that minimizes $W _ { k }$ . The strategy is to set a target $k$ for the next step, and then choose the stepsize from (17.3.11) to try to get convergence (i.e., $\mathsf { e r r } _ { k } \le 1 \dot { }$ ) for that value of $k$ on the next step.

In practice, you compute the extrapolation tableau (17.3.7) row by row, but only test for convergence within an order window between $k - 1$ and $k + 1$ . The rationale for the order window is that if convergence appears to occur before column $k - 1$ , it is often spurious, resulting from some fortuitously small error estimate in the extrapolation. On the other hand, if you need to go beyond $k + 1$ to obtain convergence, your local model of the convergence behavior is obviously not very good and you need to cut the stepsize and reestablish it.

Here are the steps:

- Test for convergence in column $k - 1$ : If $\mathsf { e r r } _ { k - 1 } \le 1$ , accept $T _ { k - 1 , k - 1 }$ . Set the new target as

$$
k _ { \mathrm { n e w } } = \left\{ \begin{array} { l l } { k - 2 } & { \mathrm { i f ~ } W _ { k - 2 } < 0 . 8 W _ { k - 1 } \mathrm { ~ ( o r d e r ~ d e c r e a s e ) } } \\ { k } & { \mathrm { i f ~ } W _ { k - 1 } < 0 . 9 W _ { k - 2 } \mathrm { ~ ( o r d e r ~ i n c r e a s e ) } } \\ { k - 1 } & { \mathrm { o t h e r w i s e } } \end{array} \right.
$$

Set the corresponding stepsize as

$$
H _ { \mathrm { n e w } } = \left\{ \begin{array} { l l } { H _ { k _ { \mathrm { n e w } } } } & { \mathrm { i f } ~ k _ { \mathrm { n e w } } = k - 1 ~ \mathrm { o r } ~ k - 2 } \\ { H _ { k - 1 } \frac { A _ { k } } { A _ { k - 1 } } } & { \mathrm { i f } ~ k _ { \mathrm { n e w } } = k } \end{array} \right.
$$

The idea behind the last formula is that you can’t set $H _ { \mathrm { n e w } } ~ = ~ H _ { k }$ because you’re stopping the integration in row $k - 1$ so you don’t compute $H _ { k }$ . However, since $k$ is supposedly optimal, $W _ { k } \approx W _ { k - 1 }$ , which gives the last formula for $H _ { \mathrm { n e w } }$ .

- If $\mathtt { e r r } _ { k - 1 } > 1$ : Check if you can expect convergence by row $k + 1$ by estimating what $\scriptstyle { \mathtt { e r r } } _ { k + 1 }$ will be. Assuming one is in the asymptotic regime, one can show that

$$
\mathrm { e r r } _ { k } \approx \left( { \frac { n _ { 0 } } { n _ { k } } } \right) ^ { 2 } \mathrm { e r r } _ { k - 1 }
$$

and hence that $\boldsymbol { \mathrm { e r r } } _ { k + 1 }$ will be greater than one if approximately

$$
\mathrm { e r r } _ { k - 1 } > \left( { \frac { n _ { k } } { n _ { 0 } } } \right) ^ { 2 } \left( { \frac { n _ { k + 1 } } { n _ { 0 } } } \right) ^ { 2 }
$$

If this condition is satisfied, reject the step and restart with $k _ { \mathrm { n e w } }$ and $H _ { \mathrm { n e w } }$ chosen according to (17.3.14) and (17.3.15).

- If (17.3.17) is not satisfied, compute the next row of the tableau (i.e., for the target value of $k$ ) and see if convergence is attained for column $k$ . Thus, if $\mathsf { e r r } _ { k } \le 1$ , accept the step and continue with

$$
k _ { \mathrm { n e w } } = { \left\{ \begin{array} { l l } { k - 1 } & { { \mathrm { i f } } \ W _ { k - 1 } < 0 . 8 W _ { k } \ ( { \mathrm { o r d e r } } \ { \mathrm { d e c r e a s e } } ) } \\ { k + 1 } & { { \mathrm { i f } } \ W _ { k } < 0 . 9 W _ { k - 1 } \ ( { \mathrm { o r d e r } } \ { \mathrm { i n c r e a s e } } ) } \\ { k } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

Set the corresponding stepsize as

$$
H _ { \mathrm { n e w } } = \left\{ \begin{array} { l l } { H _ { k _ { \mathrm { n e w } } } } & { \mathrm { i f ~ } k _ { \mathrm { n e w } } = k \mathrm { ~ o r ~ } k - 1 } \\ { H _ { k } \frac { A _ { k + 1 } } { A _ { k } } } & { \mathrm { i f ~ } k _ { \mathrm { n e w } } = k + 1 } \end{array} \right.
$$

- If $\mathbf { e r r } _ { k } > 1$ , check if you can expect convergence by the next row. Analogously to (17.3.17), check if

$$
\mathrm { e r r } _ { k } > \left( \frac { n _ { k + 1 } } { n _ { 0 } } \right) ^ { 2 }
$$

If this condition is satisfied, reject the step and restart with $k _ { \mathrm { n e w } }$ and $H _ { \mathrm { n e w } }$ chosen according to (17.3.18) and (17.3.19).

- If (17.3.17) is not satisfied, compute row $k + 1$ of the tableau. If $\mathrm e x x _ { k + 1 } \le 1$ , accept the step. Set the new target with the following prescription:

$$
{ \begin{array} { l l } { k _ { \mathrm { { n e w } } } = k } \\ { \operatorname { i f } W _ { k - 1 } < 0 . 8 W _ { k } } & { k _ { \mathrm { { n e w } } } = k - 1 ( { \mathrm { o r d e r } } { \mathrm { d e c r e a s e } } ) } \\ { \operatorname { i f } W _ { k + 1 } < 0 . 9 W _ { k _ { \mathrm { { n e w } } } } } & { k _ { \mathrm { { n e w } } } = k + 1 ( { \mathrm { o r d e r } } { \mathrm { i n c r e a s e } } ) } \end{array} }
$$

The stepsize is set as in (17.3.19).

- If $\mathtt { e r r } _ { k + 1 } ~ > ~ 1$ , reject the step. Restart with $k _ { \mathrm { n e w } }$ and $H _ { \mathrm { n e w } }$ chosen according to (17.3.18) and (17.3.19).

Two important refinements to this strategy are

- After a step is rejected, the order and stepsize are not allowed to increase.

- $H _ { \mathrm { n e w } }$ computed from equation (16.4.5) is not allowed to change too rapidly in one step. It is restricted by

$$
\frac { F } { S _ { 4 } } \leq \frac { H _ { \mathrm { n e w } } } { H } \leq \frac { 1 } { F } \qquad F \equiv S _ { 3 } ^ { 1 / ( 2 k + 1 ) }
$$

The default values of the parameters are $S _ { 3 } = 0 . 0 2$ , $S _ { 4 } = 4$ .

For the first step, the target $k$ is estimated crudely from the requested precision, but the step is accepted if the error is small enough for any smaller $k$ . For the last step, the stepsize is decreased to be the length of the remaining integration interval, so a similar increase in the order window is allowed.

# 17.3.4 Dense Output

The basic Bulirsch-Stoer step $H$ is typically much larger than in Runge-Kutta methods because of the high orders invoked, so a dense output option is even more important. Our implementation once again is based closely on the coding in [4], which is based on [5].

A dense output algorithm turns out to be possible only for certain stepsize sequences, for example increasing by fours:

$$
n = 2 , 6 , 1 0 , 1 4 , 1 8 , 2 2 , 2 6 , 3 0 , . . .
$$

The idea is to do Hermite interpolation using the function and derivative values at the beginning and end of the step. These are supplemented with values of the function and its derivatives at the midpoint obtained by extrapolation of values saved during the integration.

The error of the Hermite interpolation needs to be monitored. If it is too big, the step is rejected and the stepsize reduced appropriately. The error estimate of the interpolation is also used if necessary to limit the size of the next step after a successful step.

# 17.3.5 Implementation

The use of StepperBS is exactly the same as the use of the Runge-Kutta routines. For example, to solve the problem at the end of $\ S 1 7 . 2$ , everything is exactly the same except the line

Odeint<StepperDopr5<rhs_van> $>$ ode(ystart,x1,x2,atol,rtol,h1,hmin,out,d); is replaced by

# Odeint<StepperBS<rhs_van> > ode(ystart,x1,x2,atol,rtol,h1,hmin,out,d);

The object StepperBS implements a Bulirsch-Stoer step. Some of its functions are declared virtual because the algorithm StepperStoerm will be implemented as a derived class from it in the next section, and these functions will be overridden. As with StepperDopr5, the class is templated on the functor class defining the right-hand side derivatives.

# template <class D>

struct StepperBS : StepperBase {

Bulirsch-Stoer step with monitoring of local truncation error to ensure accuracy and adjust stepsize.

typedef D Dtype; Make the type of derivs available to odeint.   
static const Int KMAXX $^ { = 8 }$ ,IMAXX $\ c =$ KMAXX+1;   
KMAXX is the maximum number of rows used in the extrapolation.   
Int k_targ; Optimal row number for convergence.   
VecInt nseq; Stepsize sequence.   
VecInt cost; $A _ { k }$ .   
MatDoub table; Extrapolation tableau.   
VecDoub dydxnew;   
Int mu; Used for dense output.   
MatDoub coeff; Coefficients used in extrapolation tableau.   
VecDoub errfac; Used to compute dense interpolation error.   
MatDoub ysave; ysave and fsave store values and derivatives to be MatDoub fsave; used for dense output.   
VecInt ipoint; Keeps track of where values are stored in fsave.   
VecDoub dens; Stores quantities for dense interpolating polynomial.   
StepperBS(VecDoub_IO &yy, VecDoub_IO &dydxx, Doub &xx, const Doub atol,

const Doub rtol, bool dens); void step(const Doub htry,D &derivs); virtual void dy(VecDoub_I &y, const Doub htot, const Int k, VecDoub_O &yend, Int &ipt, D &derivs); void polyextr(const Int k, MatDoub_IO &table, VecDoub_IO &last); virtual void prepare_dense(const Doub h,VecDoub_I &dydxnew, VecDoub_I &ysav, VecDoub_I &scale, const Int k, Doub &error); virtual Doub dense_out(const Int i,const Doub x,const Doub h); virtual void dense_interp(const Int n, VecDoub_IO &y, const Int imit);

Detailed implementations of the member functions are given in a Webnote [6].

# CITED REFERENCES AND FURTHER READING:

Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), -7.2.14.[1]   
Gear, C.W. 1971, Numerical Initial Value Problems in Ordinary Differential Equations (Englewood Cliffs, NJ: Prentice-Hall), $\ S 6 . 1 . 4$ and $\ S 6 . 2$ .   
Deuflhard, P. 1983, “Order and Stepsize Control in Extrapolation Methods,” Numerische Mathematik,vol.41, pp.399-422.[2]   
Deuflhard, P. 1985, “Recent Progress in Extrapolation Methods for Ordinary Differential Equations,” SIAM Review, vol. 27, pp. 505–535.[3]   
Hairer, E., Nørsett, S.P., and Wanner, G. 1993, Solving Ordinary Differential Equations I. Nonstiff Problems,2nd ed.(New York: Springer).Fortran codes at http://www.unige.ch/\~hairer/software.html.[4]   
Hairer, E., and Ostermann, A. 1990, “Dense Output for Extrapolation Methods,” Numerische Mathematik,vol.58,pp.419-439.[5]   
Numerical Recipes Software 2007, “StepperBS Implementations,” Numerical Recipes Webnote No.21,at http://www.nr.com/webnotes?21 [6]

# 17.4 Second-Order Conservative Equations

Usually when you have a system of high-order differential equations to solve it is best to reformulate them as a system of first-order equations, as discussed in $\ S 1 7 . 0$ . There is a particular class of equations that occurs quite frequently in practice where you can gain about a factor of two in efficiency by differencing the equations directly. The equations are secondorder systems where the derivative does not appear on the right-hand side:

$$
y ^ { \prime \prime } = f ( x , y ) , \qquad y ( x _ { 0 } ) = y _ { 0 } , \qquad y ^ { \prime } ( x _ { 0 } ) = z _ { 0 }
$$

As usual, $y$ can denote a vector of values.

Stoermer’s rule, dating back to 1907, has been a popular method for discretizing such systems. With $h = H / m$ we have

$$
\begin{array} { l } { { y _ { 1 } = y _ { 0 } + h [ z _ { 0 } + \frac { 1 } { 2 } h f ( x _ { 0 } , y _ { 0 } ) ] } } \\ { { y _ { k + 1 } - 2 y _ { k } + y _ { k - 1 } = h ^ { 2 } f ( x _ { 0 } + k h , y _ { k } ) , \qquad k = 1 , \dots , m - 1 } } \\ { { z _ { m } = ( y _ { m } - y _ { m - 1 } ) / h + \frac { 1 } { 2 } h f ( x _ { 0 } + H , y _ { m } ) } } \end{array}
$$

Here $z _ { m }$ is $y ^ { \prime } ( x _ { \mathbf { 0 } } + H )$ . Henrici showed how to rewrite equations (17.4.2) to reduce roundoff error by using the quantities $\Delta _ { k } \equiv y _ { k + 1 } - y _ { k }$ . Start with

$$
\begin{array} { l } { \Delta _ { 0 } = h [ z _ { 0 } + \frac { 1 } { 2 } h f ( x _ { 0 } , y _ { 0 } ) ] } \\ { y _ { 1 } = y _ { 0 } + \Delta _ { 0 } } \end{array}
$$

Then, for $k = 1 , \ldots , m - 1$ , set

$$
\begin{array} { c } { { \Delta _ { k } = \Delta _ { k - 1 } + h ^ { 2 } f ( x _ { 0 } + k h , y _ { k } ) } } \\ { { y _ { k + 1 } = y _ { k } + \Delta _ { k } } } \end{array}
$$

Finally compute the derivative from

$$
\begin{array} { r } { z _ { m } = \Delta _ { m - 1 } / h + \frac { 1 } { 2 } h f ( x _ { 0 } + H , y _ { m } ) } \end{array}
$$

Gragg again showed that the error series for equations (17.4.3) – (17.4.5) contains only even powers of $h$ , and so the method is a logical candidate for extrapolation a la Bulirsch-Stoer. \`

Here is the StepperStoerm routine:

# template <class D>

struct StepperStoerm : StepperBS<D> {

Stoermer’s rule for integrating $\bar { y ^ { \prime \prime } } = f ( x , y )$ for a system of equations.

# stepperstoerm.h

using StepperBS<D>::x; using StepperBS<D>::xold; using StepperBS<D>::y;   
using StepperBS<D>::dydx; using StepperBS<D>::dense; using StepperBS<D>::n;   
using StepperBS<D>::KMAXX; using StepperBS<D>::IMAXX; using StepperBS<D>::nseq;   
using StepperBS<D>::cost; using StepperBS<D>::mu; using StepperBS<D>::errfac;   
using StepperBS<D>::ysave; using StepperBS<D>::fsave;   
using StepperBS<D>::dens; using StepperBS<D>::neqn;   
MatDoub ysavep;   
StepperStoerm(VecDoub_IO &yy, VecDoub_IO &dydxx, Doub &xx, const Doub atol, const Doub rtol, bool dens);   
void dy(VecDoub_I &y, const Doub htot, const Int k, VecDoub_O &yend, Int &ipt,D &derivs);   
void prepare_dense(const Doub h,VecDoub_I &dydxnew, VecDoub_I &ysav, VecDoub_I &scale, const Int k, Doub &error);   
Doub dense_out(const Int i,const Doub x,const Doub h);   
void dense_interp(const Int n, VecDoub_IO &y, const Int imit);

# };

Because the base class StepperBS is templated on the derivs class, the derived class StepperStoerm does not automatically inherit its member variables. This is the reason for the using declarations.

Note that in order to reuse the StepperBS code and make StepperStoerm a derived class, the arrays $\mathbb { y }$ and dydx are of length $2 n$ for a system of $n$ second-order equations. The values of $y$ are stored in the first $n$ elements of $_ \texttt { y }$ , while the first derivatives are stored in the second $n$ elements. The right-hand side $f$ is stored in the first $n$ elements of the array dydx, which therefore actually contains $y ^ { \prime \prime }$ ; the second $n$ elements are unused.

The constructor has to redefine the costs $A _ { k }$ because there are half the number of function evaluations per step compared with the midpoint method:

# template <class D>

StepperStoerm<D>::StepperStoerm(VecDoub_IO &yy, VecDoub_IO &dydxx, Doub &xx, const Doub atoll,const Doub rtoll, bool dens)

: StepperBS $\mathrm { \Phi }$ (yy,dydxx,xx,atoll,rtoll,dens),ysavep(IMAXX,n/2) {

Constructor. On input, $\mathtt { y } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ contains $y$ in its first $\mathbf { n } / 2$ elements and $y ^ { \prime }$ in its second $\mathtt { n } / 2$ elements, all evaluated at $\mathbf { x }$ . The vector dydx $\left[ 0 \cdot \cdot \mathbf { n } \mathbf { - } 1 \right]$ contains the right-hand side function $f$ (also evaluated at $\mathbf { x }$ ) in its first $\mathbf { n } / 2$ elements. Its second $\mathtt { n } / 2$ elements are not referenced. Also input are the absolute and relative tolerances, atol and rtol, and the boolean dense, which is true if dense output is required.

Number of equations.   
Redefine cost: half as many function evaluations as Bulirsch-Stoer.   
Coefficients for interpolation error are different too.   
neqn=n/2;   
cost[0] $=$ nseq[0]/2+1;   
for (Int $\mathtt { k } = 0$ ;k<KMAXX;k $^ { + + }$ ) cost[k+1] $=$ cost[k]+nseq[k+1]/2;   
for (Int $\scriptstyle \dot { 1 } = 0$ ; i<2\*IMAXX+1; i++) { Int $\dot { 1 } \mathtt { p } 7 = \dot { 1 } + 7$ ; Doub fac ${ = } 1$ .5/ip7; errfac[i] $=$ fac\*fac\*fac; Doub e = 0.5\*sqrt(Doub(i+1)/ip7);

for (Int j=0; $\scriptstyle { \dot { \mathbf { J } } } < = { \dot { \mathbf { I } } }$ ; ${ \mathrm { j } } + +$ ) { errfac[i] $\ast = \mathrm { ~ e ~ } / \left( \mathrm { j + 1 } \right)$ ; } } }

Here is the routine dy that implements Stoermer’s rule:

void StepperStoerm<D>::dy(VecDoub_I &y, const Doub htot, const Int k, VecDoub_O &yend, Int &ipt, D &derivs) {

Stoermer step. Inputs are $y$ , $H$ , and $k$ . The output is returned as yend[0..2n-1]. The counter ipt keeps track of saving the right-hand sides in the correct locations for dense output.

VecDoub ytemp(n);   
Int nstep=nseq[k];   
Doub h=htot/nstep; Stepsize this trip.   
Doub ${ \tt h } 2 = 2$ .0\*h;   
for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<neqn;i++) { First step. ytemp[i]=y[i]; Int ni neqn+i; ytemp[ni]=y[ni]+h\*dydx[i];   
}   
Doub xnew=x;   
Int nstp2=nstep/2;   
for (Int nn $^ { = 1 }$ ;nn $< =$ nstp2;nn $^ { + + }$ ) { General step. if (dense && nn $= =$ (nstp2 $+ 1$ 1)/2) { for (Int $\scriptstyle \dot { 1 } = 0$ ;i<neqn; $\dot { \bf 1 } + +$ ) { ysavep[k][i]=ytemp[neqn+i]; ysave[k][i]=ytemp[i]+h\*ytemp[neqn+i]; } } for (Int i=0;i<neqn;i++) ytemp[i] $+ =$ h2\*ytemp[neqn+i]; xnew $+ = \ \ln 2$ ; derivs(xnew,ytemp,yend); Store derivatives temporarily in yend. if (dense && abs(nn-(nstp2+1)/2) < k+1) { ipt++; for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<neqn; $\dot { \bar { \lambda } } + +$ ) fsave[ipt][i] $=$ yend[i]; } if (nn $! =$ nstp2) { for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<neqn; $\dot { \bf 1 } + +$ ) ytemp[neqn+i] $+ =$ h2\*yend[i]; }   
}   
for (Int i=0;i<neqn;i++) { Last step. Int ni $=$ neqn+i; yend[ni]=ytemp[ni]+h\*yend[i]; yend[i]=ytemp[i];   
}

The dense output routines are in a Webnote [1].

# CITED REFERENCES AND FURTHER READING:

Deuflhard, P. 1985, “Recent Progress in Extrapolation Methods for Ordinary Differential Equations,” SIAM Review, vol. 27, pp. 505–535.   
Hairer, E., Nørsett, S.P., and Wanner, G. 1993, Solving Ordinary Differential Equations I. Nonstiff Problems, 2nd ed.(New York: Springer). Fortran codes at http://www.unige.ch/\~hairer/software.html.

Numerical Recipes Software 2007, “Dense Output for Stoermer’s Rule,” Numerical Recipes Webnote No. 22, at http://www.nr.com/webnotes?22 [1]

# 17.5 Stiff Sets of Equations

As soon as one deals with more than one first-order differential equation, the possibility of a stiff set of equations arises. Stiffness typically occurs in a problem where there are two or more very different scales of the independent variable on which the dependent variables are changing. For example, consider the following set of equations [1]:

$$
\begin{array} { l } { { u ^ { \prime } = 9 9 8 u + 1 9 9 8 v } } \\ { { \phantom { u ^ { \prime } = } \phantom { } } } \\ { { v ^ { \prime } = - 9 9 9 u - 1 9 9 9 v } } \end{array}
$$

with boundary conditions

$$
u ( 0 ) = 1 \qquad v ( 0 ) = 0
$$

By means of the transformation

$$
\begin{array} { r } { u = 2 y - z \qquad v = - y + z } \end{array}
$$

we find the solution

$$
\begin{array} { l } { u = 2 e ^ { - x } - e ^ { - 1 0 0 0 x } } \\ { v = - e ^ { - x } + e ^ { - 1 0 0 0 x } } \end{array}
$$

If we integrated the system (17.5.1) with any of the methods given so far in this chapter, the presence of the $e ^ { - 1 0 0 0 x }$ term would require a stepsize $h \ll 1 / 1 0 0 0$ for the method to be stable (the reason for this is explained below). This is so even though the $e ^ { - 1 0 0 0 x }$ term is completely negligible in determining the values of $u$ and $v$ as soon as one is away from the origin (see Figure 17.5.1).

This is the generic disease of stiff equations: We are required to follow the variation in the solution on the shortest length scale to maintain the stability of the integration, even though accuracy requirements allow a much larger stepsize.

To see how we might cure this problem, consider the single equation

$$
y ^ { \prime } = - c y
$$

where $c > 0$ is a constant. The explicit (or forward) Euler scheme for integrating this equation with stepsize $h$ is

$$
y _ { n + 1 } = y _ { n } + h y _ { n } ^ { \prime } = ( 1 - c h ) y _ { n }
$$

The method is called explicit because the new value $y _ { n + 1 }$ is given explicitly in terms of the old value $y _ { n }$ . Clearly the method is unstable if $h > 2 / c$ , for then $| y _ { n } | \to \infty$ as $n  \infty$ even though the solution of (17.5.5) is bounded.

![](images/19e6f0d584554286519433e63a966c2be1724c900af181a21df06a93a570166e.jpg)  
Figure 17.5.1. Example of an instability encountered in integrating a stiff equation (schematic). Here it is supposed that the equation has two solutions, shown as solid and dashed lines. Although the initial conditions are such as to give the solid solution, the stability of the integration (shown as the unstable dotted sequence of segments) is determined by the more rapidly varying dashed solution, even after that solution has effectively died away to zero. Implicit integration methods are the cure.

The simplest cure is to resort to implicit differencing, where the right-hand side is evaluated at the new $y$ location. In this case, we get the backward Euler scheme:

or

$$
\begin{array} { l } { y _ { n + 1 } = y _ { n } + h y _ { n + 1 } ^ { \prime } } \\ { \qquad } \\ { y _ { n + 1 } = { \frac { y _ { n } } { 1 + c h } } } \end{array}
$$

The method is absolutely stable: Even as $h  \infty$ , $y _ { n + 1 } \to 0$ , which is in fact the correct solution of the differential equation. If we think of $x$ as representing time, then the implicit method converges to the true equilibrium solution (i.e., the solution at late times) for large stepsizes. This nice feature of implicit methods holds only for linear systems, but even in the general case implicit methods give better stability. Of course, we give up accuracy in following the evolution toward equilibrium if we use large stepsizes, but we maintain stability.

These considerations can easily be generalized to sets of linear equations with constant coefficients:

$$
\mathbf { y } ^ { \prime } = - \mathbf { C } \cdot \mathbf { y }
$$

Consider first the usual case where the matrix $\mathbf { C }$ can be diagonalized by a similarity transformation (cf. eqn. 11.0.11)

$$
\mathbf { T } \cdot \mathbf { C } \cdot \mathbf { T } ^ { - 1 } = \mathrm { d i a g } ( \lambda _ { 0 } \dots \lambda _ { N - 1 } )
$$

where $\lambda _ { i }$ are the eigenvalues of $\mathbf { C }$ . If we define the vector $\mathbf { z } ( x )$ by $\mathbf { z } = \mathbf { T } ^ { - 1 } \cdot \mathbf { y } ( x )$ , then equation (17.5.9) becomes

$$
\mathbf { z } ^ { \prime } = - \mathrm { d i a g } ( \lambda _ { 0 } \dots \lambda _ { N - 1 } ) \cdot \mathbf { z }
$$

This is a set of $N$ independent equations for the components of $\mathbf { z }$ with solution

$$
\mathbf { z } = \mathrm { d i a g } ( e ^ { - \lambda _ { 0 } x } \dots e ^ { - \lambda _ { N - 1 } x } ) \cdot \mathbf { z } _ { 0 }
$$

Thus the solution of the original equation is

$$
\mathbf { y } = \mathbf { T } \cdot \mathrm { d i a g } ( e ^ { - \lambda _ { 0 } x } \dots e ^ { - \lambda _ { N - 1 } x } ) \cdot \mathbf { T } ^ { - 1 } \cdot \mathbf { y } _ { 0 }
$$

We will be interested in the stable solutions, that is, those that decay as $x \to \infty$ . (This notion can be made more rigorous by considering Liapunov stability, the idea that if $\mathbf { y } _ { 0 }$ is small then $\mathbf { y }$ is small for all $x > 0$ .) From equation (17.5.13) we see that the criterion for stable solutions is

$$
\begin{array} { r } { \mathrm { R e } \lambda _ { i } > 0 \qquad i = 0 , \dots , N - 1 } \end{array}
$$

What if the matrix $\mathbf { C }$ in equation (17.5.9) cannot be diagonalized? Then it can always be transformed to so-called Jordan canonical form, which is the “closest” it can come to being made diagonal. Using this form, one can show that criterion (17.5.14) is still the stability criterion [2].

Now consider solving equation (17.5.9) by explicit differencing as in equation (17.5.6):

$$
\mathbf { y } _ { n + 1 } = ( \mathbf { 1 } - \mathbf { C } h ) \cdot \mathbf { y } _ { n }
$$

and so

$$
{ \bf y } _ { n } = ( { \bf 1 } - { \bf C } h ) ^ { n } \cdot { \bf y } _ { 0 }
$$

If C can be diagonalized, it has a complete set of eigenvectors $\{ \pmb { \xi } _ { i } \}$ that can be used as a basis to expand $\mathbf { y } _ { 0 }$ :

$$
{ \bf y } _ { 0 } = \sum _ { i = 0 } ^ { N - 1 } \alpha _ { i } \pmb { \xi } _ { i }
$$

Substituting this expansion in equation (17.5.16) gives

$$
{ \bf y } _ { n } = \sum _ { i = 0 } ^ { N - 1 } \alpha _ { i } ( 1 - h \lambda _ { i } ) ^ { n } \pmb { \xi } _ { i }
$$

If the original differential equation is stable, we require the difference scheme to be stable in that it must have bounded solutions, that is, ${ \bf y } _ { n }$ must be bounded as $n  \infty$ . From equation (17.5.18) we see that stability of the difference scheme requires

$$
| 1 - h \lambda _ { i } | < 1 \qquad i = 0 , \ldots , N - 1
$$

If the $\lambda _ { i }$ are all real, then since they are positive for the differential equation to be stable, the stability criterion for the difference scheme is

$$
h < \frac { 2 } { \lambda _ { \operatorname* { m a x } } }
$$

where $\lambda _ { \mathrm { m a x } }$ is the largest eigenvalue of $\mathbf { C }$ .

As usual, if C cannot be diagonalized and so does not have a complete set of eigenvectors, then by working with the Jordan canonical form one can show the same result.

Consider now implicit differencing, which gives

$$
\mathbf { y } _ { n + 1 } = \mathbf { y } _ { n } + h \mathbf { y } _ { n + 1 } ^ { \prime }
$$

$$
{ \bf y } _ { n + 1 } = ( { \bf 1 } + { \bf C } h ) ^ { - 1 } \cdot { \bf y } _ { n }
$$

Criterion (17.5.19) becomes

$$
| 1 + h \lambda _ { i } | ^ { - 1 } < 1 \qquad i = 0 , \dots , N - 1
$$

which is satisfied for all $h$ — the method is stable for all stepsizes. The penalty we pay for this stability is that we are required to invert a matrix at each step.

Not all equations are linear with constant coefficients, unfortunately! For the system

$$
\mathbf { y } ^ { \prime } = \mathbf { f } \left( \mathbf { y } \right)
$$

implicit differencing gives

$$
\mathbf { y } _ { n + 1 } = \mathbf { y } _ { n } + h \mathbf { f } \left( \mathbf { y } _ { n + 1 } \right)
$$

In general this is some nasty set of nonlinear equations that has to be solved iteratively at each step. Suppose we try linearizing the equations, as in Newton’s method:

$$
\mathbf { y } _ { n + 1 } = \mathbf { y } _ { n } + h \left[ \mathbf { f } \left( \mathbf { y } _ { n } \right) + \left. { \frac { \partial \mathbf { f } } { \partial \mathbf { y } } } \right| _ { \mathbf { y } _ { n } } \cdot \left( \mathbf { y } _ { n + 1 } - \mathbf { y } _ { n } \right) \right]
$$

Here $\partial \mathbf { f } / \partial \mathbf { y }$ is the matrix of the partial derivatives of the right-hand side (the Jacobian matrix). Rearrange equation (17.5.26) into the form

$$
\mathbf { y } _ { n + 1 } = \mathbf { y } _ { n } + h \left[ \mathbf { 1 } - h { \frac { \partial \mathbf { f } } { \partial \mathbf { y } } } \right] ^ { - 1 } \cdot \mathbf { f } \left( \mathbf { y } _ { n } \right)
$$

If $h$ is not too big, only one iteration of Newton’s method may be accurate enough to solve equation (17.5.25) using equation (17.5.27). In other words, at each step we have to invert the matrix

$$
\mathbf { 1 } - h { \frac { \partial \mathbf { f } } { \partial \mathbf { y } } }
$$

to find ${ \bf y } _ { n + 1 }$ . Solving implicit methods by linearization is called a “semi-implicit” method, so equation (17.5.27) is the semi-implicit Euler method. It is not guaranteed to be stable, but it usually is, because the behavior is locally similar to the case of a constant matrix C described above.

So far we have dealt only with implicit methods that are first-order accurate. While these are very robust, most problems will benefit from higher-order methods. There are three important classes of higher-order methods for stiff systems:

- Generalizations of the Runge-Kutta method. These consist of implicit methods, where nonlinear equations are solved by Newton iteration at each step, and semi-implicit methods that solve linear equations analogous to (17.5.27). These semi-implicit methods are often called Rosenbrock methods. The first good implementation of these ideas was by Kaps and Rentrop, and so these methods are also called Kaps-Rentrop methods. Generalizations of the Bulirsch-Stoer method, which extrapolate a semi-implicit sequence of integrations to zero stepsize. Predictor-corrector methods, most of which are descendants of Gear’s backward differentiation method.

We shall give implementations of Rosenbrock and extrapolation methods. An example of a good implicit Runge-Kutta code in Fortran is RADAU [3], while several stiff predictor-corrector–type Fortran codes (LSODE, DEBDF, VODE and MEBDF) are available from Netlib [5].

Here is an important point: It is absolutely crucial to scale your variables properly when integrating stiff problems with automatic stepsize adjustment. As in our nonstiff routines, you will be asked to supply absolute and relative tolerances atol and rtol. In stiff problems, there are often strongly decreasing pieces of the solution that you are not particularly interested in following once they are small. Thus you should almost never integrate with a pure relative error criterion by setting $\mathsf { a t o l } = 0$ . A good default choice is $\mathtt { a t o l } = \mathtt { r t o l }$ , or sometimes a few orders of magnitude smaller.

One final warning: Solving stiff problems can sometimes lead to catastrophic precision loss. Double precision is often a requirement, not an option.

# 17.5.1 Rosenbrock Methods

These methods have the advantage of being relatively simple to understand and implement. For moderate accuracies (tolerances of order $1 0 ^ { - 4 } – \mathrm { i } 0 ^ { - 5 }$ ) and moderate-sized systems $N \lesssim 1 0$ ), they are competitive with the more complicated algorithms. For more stringent parameters, Rosenbrock methods remain reliable; they merely become less efficient than competitors like the semi-implicit extrapolation method (see below).

A Rosenbrock method seeks a solution of the form

$$
\mathbf { y } ( x _ { 0 } + h ) = \mathbf { y } _ { 0 } + \sum _ { i = 1 } ^ { s } b _ { i } \mathbf { k } _ { i }
$$

where the corrections $\mathbf { k } _ { i }$ are found by solving $s$ linear equations that generalize the structure in (17.5.27):

$$
( \mathbf { 1 } - \gamma h \mathbf { f } ^ { \prime } ) \cdot \mathbf { k } _ { i } = h \mathbf { f } \left( \mathbf { y } _ { 0 } + \sum _ { j = 1 } ^ { i - 1 } \alpha _ { i j } \mathbf { k } _ { j } \right) + h \mathbf { f } ^ { \prime } \cdot \sum _ { j = 1 } ^ { i - 1 } \gamma _ { i j } \mathbf { k } _ { j } , \qquad i = 1 , \dots , s
$$

Here we denote the Jacobian matrix by $\mathbf { f } ^ { \prime }$ . The coefficients $\gamma , b _ { i } , \alpha _ { i j }$ , and $\gamma _ { i j }$ are fixed constants independent of the problem. If $\gamma = \gamma _ { i j } = 0$ , this is simply a Runge-Kutta scheme. Equations (17.5.30) can be solved successively for $\mathbf { k } _ { 1 } , \mathbf { k } _ { 2 } , \ldots .$ .

To minimize the matrix-vector multiplications on the right-hand side of (17.5.30), rewrite the equations in terms of quantities

$$
{ \bf g } _ { i } = \sum _ { j = 1 } ^ { i - 1 } \gamma _ { i j } { \bf k } _ { j } + \gamma { \bf k } _ { i }
$$

The equations then take the form (for four stages as an example)

$$
\begin{array} { r l } & { ( { \bf 1 } / \gamma h - { \bf f } ^ { \prime } ) \cdot { \bf g } _ { 1 } = { \bf f } ( { \bf y } _ { 0 } ) } \\ & { ( { \bf 1 } / \gamma h - { \bf f } ^ { \prime } ) \cdot { \bf g } _ { 2 } = { \bf f } ( { \bf y } _ { 0 } + a _ { 2 1 } { \bf g } _ { 1 } ) + c _ { 2 1 } { \bf g } _ { 1 } / h } \\ & { ( { \bf 1 } / \gamma h - { \bf f } ^ { \prime } ) \cdot { \bf g } _ { 3 } = { \bf f } ( { \bf y } _ { 0 } + a _ { 3 1 } { \bf g } _ { 1 } + a _ { 3 2 } { \bf g } _ { 2 } ) + ( c _ { 3 1 } { \bf g } _ { 1 } + c _ { 3 2 } { \bf g } _ { 2 } ) / h } \\ & { ( { \bf 1 } / \gamma h - { \bf f } ^ { \prime } ) \cdot { \bf g } _ { 4 } = { \bf f } ( { \bf y } _ { 0 } + a _ { 4 1 } { \bf g } _ { 1 } + a _ { 4 2 } { \bf g } _ { 2 } + a _ { 4 3 } { \bf g } _ { 3 } ) + ( c _ { 4 1 } { \bf g } _ { 1 } + c _ { 4 2 } { \bf g } _ { 2 } + c _ { 4 3 } { \bf g } _ { 3 } ) / h } \end{array}
$$

Here $a _ { i j }$ and $c _ { i j }$ can be expressed in terms of $\alpha _ { i j }$ and $\gamma _ { i j }$

Note that systems where the right-hand side f $( \mathbf { y } , x )$ depends explicitly on $x$ can be handled by adding $x$ to the list of dependent variables so that the system to be solved is

$$
{ \binom { \mathbf { y } } { x } } ^ { \prime } = { \binom { \mathbf { f } } { 1 } }
$$

In the routine given below, we have explicitly carried out this replacement for you, so the routines can handle right-hand sides of the form f $( \mathbf { y } , x )$ without any special effort on your part.

Crucial to the success of a stiff integration scheme is an automatic stepsize adjustment algorithm. Kaps and Rentrop [6] discovered an embedded or Runge-Kutta-Fehlberg method as described in $\ S 1 7 . 2$ : Two estimates of the form (17.5.29) are computed, the “real” one $\mathbf { y }$ and a lower-order estimate $\widehat { \mathbf { y } }$ with different coefficients $\widehat { b } _ { i } , i = 1 , \ldots , \widehat { s }$ , where $\widehat { s } < s$ but the $\mathbf { k } _ { i }$ are the same. The difference between y and $\widehat { \mathbf { y } }$ leads to an estimate of the local truncation error, which can then be used for stepsize control. Kaps and Rentrop showed that the smallest value of $s$ for which embedding is possible is $s = 4$ , ${ \hat { s } } = 3$ , leading to a fourth-order method. By a suitable choice of parameters, only three function evaluations are needed for the four stages in each step.

In recent years, Kaps-Rentrop has lost favor to so-called stiffly stable methods, an implementation of which we give here as the routine StepperRoss (Rosenbrock Stiffly Stable), based on the Fortran routine RODAS [3]. It is also a fourth-order method with a third-order embedded method for stepsize control. Despite having six stages with six function evaluations, the enhanced stability makes it significantly more efficient than the Kaps-Rentrop method. Moreover, it has a simple dense output feature.

As with the earlier stepper routines in this chapter, you have to provide a functor for derivs, the right-hand side routine. In the structure you now must also supply a function called jacobian that returns $\mathbf { f } ^ { \prime }$ and $\partial \mathbf { f } / \partial x$ as functions of $x$ and $\mathbf { y }$ . If $x$ does not occur explicitly on the right-hand side, then dfdx will be zero. Usually the Jacobian matrix will be available to you by analytic differentiation of the right-hand side f . If not, your routine will have to compute it by numerical differencing with appropriate increments $\Delta \mathbf { y }$ . We will give an example of a complete derivative and jacobian structure at the end of this subsection.

The class StepperRoss uses a set of constants, which are provided by deriving the class from a class Ross_constants. This latter class is listed in a Webnote [4]. Here is the declaration of StepperRoss:

# template <class D>

struct StepperRoss : StepperBase, Ross_constants

Fourth-order stiffly stable Rosenbrock step for integrating stiff ODEs, with monitoring of local truncation error to adjust stepsize.

typedef D Dtype; Make the type of derivs available to odeint. MatDoub dfdy; f 0 VecDoub dfdx; @f=@x VecDoub k1,k2,k3,k4,k5,k6; VecDoub cont1,cont2,cont3,cont4; MatDoub a; StepperRoss(VecDoub_IO &yy, VecDoub_IO &dydxx, Doub &xx, const Doub atoll, const Doub rtoll, bool dens); void step(const Doub htry,D &derivs); void dy(const Doub h,D &derivs); void prepare_dense(const Doub h,VecDoub_I &dydxnew); Doub dense_out(const Int i, const Doub x, const Doub h); Doub error(); struct Controller { Doub hnext; bool reject; bool first_step; first_step, errold, and hold are used by Doub errold; the predictive controller. Doub hold; Controller(); bool success(Doub err, Doub &h); }; Controller con; };

The implementation will seem very familiar if you’ve looked at StepperDopr5, the explicit Runge-Kutta routine. Note that in the algorithm routine dy of StepperRoss, the linear equations (17.5.32) are solved by first computing the $L U$ decomposition of the matrix $\mathbf { 1 } / \gamma h - \mathbf { f } ^ { \prime }$ using the routine LUdcmp. Then the six $\mathbf { g } _ { i }$ are found by backsubstitution of the six different right-hand sides using the routine solve in LUdcmp. Thus each step of the integration requires one call to jacobian and six calls to derivs (one call outside dy and five calls inside). The evaluation of the Jacobian matrix is roughly equivalent to $N$ evaluations of the right-hand side f (although it can often be less than this, especially if commonality of code can be exploited). Thus this scheme involves about $N + 6$ function evaluations per step. Note that if $N$ is large and the Jacobian matrix is sparse, you should replace the $L U$ decomposition by a suitable sparse matrix procedure.

# template <class D>

StepperRoss<D>::StepperRoss(VecDoub_IO &yy, VecDoub_IO &dydxx, Doub &xx, const Doub atoll,const Doub rtoll, bool dens) : StepperBase(yy,dydxx,xx,atoll,rtoll,dens),dfdy ${ ( \mathtt { n } , \mathtt { n } ) }$ ,dfdx(n),k1(n),k2(n), k3(n),k4(n),k5(n),k6(n),cont1(n),cont2 $\mathbf { \eta } ( \mathtt { n } )$ ,cont3(n),cont4(n),a(n,n) {   
Input to the constructor are the dependent variable y[0..n-1] and its derivative dydx[0..n-1]   
at the starting value of the independent variable x. Also input are the absolute and relative   
tolerances, atol and rtol, and the boolean dense, which is true if dense output is required.

EPS=numeric_limits<Doub>::epsilon();

# }

# template <class D>

oid StepperRoss<D>::step(const Doub htry,D &derivs) {

Attempts a step with stepsize htry. On output, y and x are replaced by their new values, hdid is the stepsize that was actually accomplished, and hnext is the estimated next stepsize.

VecDoub dydxnew(n);   
Doub $\mathrm { \ h = }$ htry; Set stepsize to the initial trial value.   
derivs.jacobian(x,y,dfdx,dfdy); Compute the Jacobian and $\partial \mathbf { f } / \partial x$ .   
for (;;) { dy(h,derivs); Take a step. Doub err $^ { * = }$ error(); Evaluate accuracy. if (con.success(err,h)) break; Step rejected. Try again with reduced h set if (abs(h) $< =$ abs(x)\*EPS) by controller. throw("stepsize underflow in StepperRoss");   
}   
derivs(x+h,yout,dydxnew); Step succeeded.   
if (dense) Compute coefficients for dense output. prepare_dense(h,dydxnew);   
dydx ${ \bf \Phi } = { \bf \Phi }$ dydxnew; Reuse last derivative evaluation for next step.   
y=yout;   
xold $= \mathrm { x }$ ; Used for dense output.   
x += (hdid=h);   
hnext=con.hnext;

# }

# template<class D>

void StepperRoss<D>::dy(const Doub h,D &derivs) {

Given values for n variables y[0..n-1] and their derivatives dydx[0..n-1] known at $\mathbf { x }$ , use the fourth-order stiffly stable Rosenbrock method to advance the solution over an interval h and store the incremented variables in yout[0..n-1]. Also store an estimate of the local truncation error in yerr using the embedded third-order method.

VecDoub ytemp(n),dydxnew(n);   
Int i;   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) { Set up the matrix $\mathbf { 1 } / \gamma h - \mathbf { f } ^ { \prime }$ . for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j $^ { + + }$ ) a[i][j] $=$ -dfdy[i][j]; a[i][i] $+ = \mathrm { ~ 1 \AA 0 / \left( \ g a m * h \right) }$ ;   
}   
LUdcmp alu(a); $_ { L U }$ decomposition of the matrix.   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<n; $\dot { \bf 1 } + + )$ Set up right-hand side for ${ \bf g } _ { 1 }$ . ytemp[i] $=$ dydx[i]+h\*d1\*dfdx[i];   
alu.solve(ytemp,k1); Solve for g1.   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) Compute intermediate values of $\mathtt { y }$ . ytemp[i]=y[i]+a21\*k1[i];   
derivs(x+c2\*h,ytemp,dydxnew); Compute dydx at the intermediate values.   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<n; $\mathbf { i } + + \mathbf { i }$ ) Set up right-hand side for $\mathbf { g } _ { 2 }$ . ytemp[i] $=$ dydxnew[i]+h\*d2\*dfdx[i]+c21\*k1[i]/h;

alu.solve(ytemp,k2); Solve for $\mathbf { g } _ { 2 }$ . for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) Compute intermediate values of $\mathtt { y }$ . ytemp[i]=y[i]+a31\*k1[i] $^ +$ a32\*k2[i]; derivs(x+c3\*h,ytemp,dydxnew); Compute dydx at the intermediate values. for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) Set up right-hand side for ${ \bf g } _ { 3 }$ . ytemp[i] $=$ dydxnew[i]+h\*d3\*dfdx[i]+(c31\*k1[i]+c32\*k2[i])/h; alu.solve(ytemp,k3); Solve for ${ \bf g } _ { 3 }$ . for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) Compute intermediate values of y. ytemp[i]=y[i]+a41\*k1[i]+a42\*k2[i]+a43\*k3[i]; derivs(x+c4\*h,ytemp,dydxnew); Compute dydx at the intermediate values. for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) Set up right-hand side for $\mathbf { g } _ { 4 }$ . ytemp[i] $=$ dydxnew[i]+h\*d4\*dfdx[i] $^ +$ (c41\*k1[i]+c42\*k2[i]+c43\*k3[i])/h; alu.solve(ytemp,k4); Solve for g4. for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) Compute intermediate values of y. ytemp[i]=y[i]+a51\*k1[i]+a52\*k2[i]+a53\*k3[i]+a54\*k4[i]; Doub xph=x+h; derivs(xph,ytemp,dydxnew); Compute dydx at the intermediate values. for (i=0;i<n;i++) Set up right-hand side for $\mathbf { g } _ { 5 }$ . k6[i] $=$ dydxnew[i] $^ +$ (c51\*k1[i]+c52\*k2[i]+c53\*k3[i]+c54\*k4[i])/h; alu.solve(k6,k5); Solve for g5. for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n; $\dot { \bf 1 } + +$ ) Compute the embedded solution. ytemp[i] $+ =$ k5[i]; derivs(xph,ytemp,dydxnew); Last derivative evaluation. for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) Compute the solution and the error. k6[i] $=$ dydxnew[i] $^ +$ (c61\*k1[i]+c62\*k2[i]+c63\*k3[i]+c64\*k4[i]+c65\*k5[i])/h; alu.solve(k6,yerr); for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n; $\dot { \bf 1 } + +$ ) yout[i] $=$ ytemp[i]+yerr[i]; template <class D> void StepperRoss<D>::prepare_dense(const Doub h,VecDoub_I &dydxnew) { Store coefficients of interpolating polynomial for dense output in cont1...cont4. for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) { cont1[i]=y[i]; cont2[i]=yout[i]; cont3[i] $=$ d21\*k1[i]+d22\*k2[i]+d23\*k3[i] $^ +$ d24\*k4[i]+d25\*k5[i]; cont4[i] $=$ d31\*k1[i]+d32\*k2[i]+d33\*k3[i]+d34\*k4[i]+d35\*k5[i]; } template <class D> Doub StepperRoss<D>::dense_out(const Int i,const Doub x,const Doub h) { Evaluate interpolating polynomial for y[i] at location x, where $\mathbf { x } { \circ } 1 { \mathsf { d } } \leq \mathbf { x } \leq \mathbf { x } { \circ } 1 { \mathsf { d } } + \mathbf { h }$ . Doub $\mathrm { s } =$ (x-xold)/h; Doub s $\scriptstyle 1 = 1$ .0-s; return cont1[i]\*s1+s\*(cont2[i]+s1\*(cont3[i]+s\*cont4[i])); template <class D> Doub StepperRoss<D>::error() { Use yerr to compute norm of scaled error estimate. A value less than one means the step was successful. Doub err ${ \tt = } 0$ .0,sk; for (Int $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) sk=atol+rtol\*MAX(abs(y[i]),abs(yout[i])); err $+ =$ SQR(yerr[i]/sk); } return sqrt(err/n); }

Stepsize control depends on the fact that

$$
\begin{array} { r } { { \mathbf { y } } _ { \mathrm { e x a c t } } = { \mathbf { y } } + O ( h ^ { 5 } ) } \\ { { \mathbf { y } } _ { \mathrm { e x a c t } } = \widehat { { \mathbf { y } } } + O ( h ^ { 4 } ) } \end{array}
$$

Thus

$$
| \mathbf { y } - { \hat { \mathbf { y } } } | = O ( h ^ { 4 } )
$$

Referring back to the steps leading from equation (17.2.4) to equation (17.2.12), we see that the new stepsize should be chosen as in equation (17.2.12) but with the exponent 1/5 replaced by 1/4. Also, experience shows that it is wise to prevent too large a stepsize change in one step, otherwise we will probably have to undo the large change in the next step. We adopt 0.2 and 6 as the maximum allowed decrease and increase of $h$ in one step.

Methods for integrating stiff equations do not suffer from the stability limitations that led to the PI controller of $\ S 1 7 . 2 . 1$ . However, stiff problems often need a rapid decrease in stepsize even when the previous step is successful. Also, sometimes the effective order of the method can be lower than the simple Taylor series prediction. Gustafsson [7] has proposed a predictive controller that does a good job of dealing with these problems. The resulting formula is

$$
h _ { n + 1 } = S h _ { n } \left( { \frac { 1 } { \mathsf { e r r } _ { n } } } \right) ^ { 1 / 4 } { \frac { h _ { n } } { h _ { n - 1 } } } \left( { \frac { \mathsf { e r r } _ { n - 1 } } { \mathsf { e r r } _ { n } } } \right) ^ { 1 / 4 }
$$

It is used only when a step is accepted.

template <class D>   
StepperRoss<D>::Controller::Controller() : reject(false), first_step(true) {}   
Step size controller for fourth-order Rosenbrock method.   
template <class D>   
bool StepperRoss<D>::Controller::success(Doub err, Doub &h) {   
Returns true if err $\leq 1$ , false otherwise. If step was successful, sets hnext to the estimated   
optimal stepsize for the next step. If the step failed, reduces h appropriately for another try. static const Doub safe ${ = } 0$ .9,fac $\mathtt { 1 } = 5$ .0,fac $^ { 2 = 1 }$ .0/6.0; Doub fac=MAX(fac2,MIN(fac1,pow(err,0.25)/safe)); Doub hnew=h/fac; Ensure 1=fac1  hnew=h  1=fac2. if (err $< = ~ 1 .$ .0) { Step succeeded. if (!first_step) { Predictive control. Doub facpred (hold/h)\*pow(err\*err/errold,0.25)/safe; facpred=MAX(fac2,MIN(fac1,facpred)); fac=MAX(fac,facpred); hnew=h/fac; } first_step=false; hold=h; errold=MAX(0.01,err); if (reject) Don’t let step increase if last one was rejected. hnew= $( \mathbf { h _ { \alpha } } > = \mathbf { \beta } 0 . 0 $ ? MIN(hnew,h) : MAX(hnew,h)); hnext=hnew; reject=false; return true; } else { Truncation error too large, reduce stepsize. $\mathrm { \ h = }$ hnew; reject=true; return false; }

As an example of how StepperRoss is used, one can solve the system

$$
\begin{array} { l } { { y _ { 0 } ^ { \prime } = - . 0 1 3 y _ { 0 } - 1 0 0 0 y _ { 0 } y _ { 2 } } } \\ { { y _ { 1 } ^ { \prime } = - 2 5 0 0 y _ { 1 } y _ { 2 } } } \\ { { y _ { 2 } ^ { \prime } = - . 0 1 3 y _ { 0 } - 1 0 0 0 y _ { 0 } y _ { 2 } - 2 5 0 0 y _ { 1 } y _ { 2 } } } \end{array}
$$

with initial conditions

$$
y _ { 0 } ( 0 ) = 1 , \qquad y _ { 1 } ( 0 ) = 1 , \qquad y _ { 2 } ( 0 ) = 0
$$

(This is test problem D4 in [8].) We integrate the system up to $x = 5 0$ with an initial stepsize of $h = 2 . 9 \times 1 0 ^ { - 4 }$ using Odeint. We set atol $= { \tt r t o l } = 1 0 ^ { - 5 }$ . The right-hand side routine for this problem is given below. Even though the ratio of largest to smallest decay constants for this problem is around $1 0 ^ { 6 }$ , StepperRoss succeeds in integrating this set in only 11 steps with 67 function evaluations. By contrast, the explicit Runge-Kutta routine StepperDopr5 requires almost 60,000 steps and over 400,000 function evaluations!

# struct rhs {

void operator() (const Doub x, VecDoub_I &y, VecDoub_O &dydx) { dydx[0] $=$ -0.013\*y[0]-1000.0\*y[0]\*y[2]; dydx[1] $=$ -2500.0\*y[1]\*y[2]; dydx[2] $=$ -0.013\*y[0]-1000.0\*y[0]\*y[2]-2500.0\*y[1]\*y[2]; } void jacobian(const Doub x, VecDoub_I &y, VecDoub_O &dfdx, MatDoub_O &dfdy) { Int n=y.size(); for (Int $\scriptstyle \dot { 1 } = 0$ ;i<n; $\dot { \bf 1 } + +$ ) dfdx[i] ${ = } 0$ .0; dfdy[0][0] $=$ -0.013-1000.0\*y[2]; dfdy[0][1] $= ~ 0 . 0$ ; dfdy[0][2] $= - 1 0 0 0 . 0 { * } \mathrm { y } \left[ 0 \right]$ ; dfdy[1][0] $= ~ 0 . 0$ ; dfdy[1][1] = -2500.0\*y[2]; dfdy[1][2] $=$ -2500.0\*y[1]; dfdy[2][0] $=$ -0.013-1000.0\*y[2]; dfdy[2][1] $=$ -2500.0\*y[2]; dfdy[2][2] $=$ -1000.0\*y[0]-2500.0\*y[1]; } };

# 17.5.2 Semi-lmplicit Extrapolation Method

The Bulirsch-Stoer method, which discretizes the differential equation using the modified midpoint rule, does not work for stiff problems. For many years, successful extrapolationtype routines for stiff equations were based on an algorithm of Bader and Deuflhard [9]. This algorithm uses a semi-implicit version of the midpoint method that has an even error series.

Not long afterward, however, Deuflhard [10] investigated a semi-implicit version of the Euler method, equation (17.5.27). This does not have an even error series. Nevertheless, it turns out that for high precision, using this method as the basis of an extrapolation scheme is even more efficient than using the semi-implicit midpoint rule. (Some theoretical insight into this behavior is provided in $\ S \nabla \mathrm { I } . 5$ of [3].) Since StepperRoss is generally satisfactory for low precision, this method is a good companion. We give it as StepperSie (“Semi-Implicit Euler”).

The basic equation of the method is equation (17.5.27) rewritten in the form

$$
\left[ \mathbf { 1 } / h - { \frac { \partial \mathbf { f } } { \partial \mathbf { y } } } \right] \cdot ( \mathbf { y } _ { n + 1 } - \mathbf { y } _ { n } ) = \mathbf { f } ( \mathbf { y } _ { n } )
$$

A sequence of stepsizes $h _ { i } = H / n _ { i }$ is used with this equation to advance the solution a distance $H$ . The linear equations are solved with $L U$ decomposition. Polynomial extrapolation is used as in the original Bulirsch-Stoer method, except that in equation (17.3.8) the ratio of stepsizes is not squared because the error series is not even.

Instead of making the replacement (17.5.33) in the above formula, it turns out to be slightly better to add a single simplified Newton iteration of the fully implicit Euler step (17.5.25):

$$
{ \bf y } _ { n + 1 } = { \bf y } _ { n } + h { \bf f } \left( x _ { n + 1 } , { \bf y } _ { n + 1 } \right) \longrightarrow \left[ { \bf 1 } - h { \frac { \partial { \bf f } } { \partial { \bf y } } } \right] \cdot \left( { \bf y } _ { n + 1 } - { \bf y } _ { n } \right) = h { \bf f } \left( x _ { n + 1 } , { \bf y } _ { n } \right)
$$

This costs an extra function evaluation but avoids the computation of $\partial \mathbf { f } / \partial x$ . In the code, we leave $\partial \mathbf { f } / \partial x$ as an argument of the jacobian function for compatibility with StepperRoss, but it is not used.

Another difference from StepperRoss is that the Jacobian does not have to be exact. Its main role is to ensure stability, not accuracy. Accordingly, the code has a test to see when the Jacobian needs to be recomputed.

Differences from StepperBS include

- The default stepsize sequence is

$$
n = 2 , 3 , 4 , 6 , 8 , 1 2 , 1 6 , 2 4 , 3 2 , 4 8 , 6 4 , \ldots , [ n _ { j } = 2 n _ { j - 2 } ] , \ldots
$$

- The work per unit step now includes the cost of Jacobian evaluations as well as function evaluations. We count one Jacobian evaluation as equivalent to five function evaluations by default, but it could be as large as $N$ , the number of equations. The work per unit step also includes the cost of the $L U$ decomposition and the backsubstitutions, each set by default to the cost of a function evaluation. Several checks for instability are included. If the estimated error $\tt e r r { k }$ starts increasing with $k$ during a step, the step is restarted with the stepsize reduced by a factor of two. Similarly, a stability test is made for $k = 0 , 1$ during the Euler step and the step is rejected if the test is failed. You could add a test for failure of the $L U$ decomposition and similarly reduce the stepsize if that happened.

The routine, which is based on the Fortran routine SEULEX [3], next follows.

# 17.5.3 Implementation of Semi-Implicit Extrapolation Method

The routine StepperSie is an excellent routine for all stiff problems, competitive with the best Gear-type routines. StepperRoss is often better in execution time for moderate $N$ and $\epsilon \lesssim 1 0 ^ { - 5 }$ . The detailed implementation is listed in a Webnote [11].

# CITED REFERENCES AND FURTHER READING:

Gear, C.W. 1971, Numerical Initial Value Problems in Ordinary Differential Equations (Englewood Cliffs, NJ: Prentice-Hall).[1]   
Hairer, E., Nørsett, S.P., and Wanner, G. 1993, Solving Ordinary Differential Equations I. Nonstiff Problems,2nd ed.(New York: Springer).Fortran codes at http://www.unige.ch/\~hairer/software.html.[2]   
Hairer, E., Nørsett, S.P., and Wanner, G. 1996, Solving Ordinary Differential Equations II. Stiff and Differential-Algebraic Problems,2nd ed. (New York: Springer).[3]   
Numerical Recipes Software 2007, “Constants for Stiffly Stable Rosenbrock Method,” Numerical Recipes Webnote No. 23,at http://www.nr.com/webnotes?23 [4]   
Netlib: http://www.netlib.org/.[5]   
Kaps, P., and Rentrop, P. 1979, “Generalized Runge-Kutta Methods of Order Four with Stepsize Control for Stiff Ordinary Differential Equations,” Numerische Mathematik, vol. 33, pp. 55– 68.[6]   
Gustafsson, K. 1994, “Control Theoretic Techniques for Stepsize Selection in Implicit Runge-Kutta Methods,” ACM Transactions on Mathematical Software, vol. 20, pp. 496-517.[7]   
Enright, W.H., and Pryce, J.D. 1987, “Two FORTRAN Packages for Assessing Initial Value Methods,” ACM Transactions on Mathematical Software, vol. 13, pp. 1–27.[8]   
Bader, G., and Deuflhard, P. 1983, “A Semi-Implicit Mid-Point Rule for Stiff Systems of Ordinary Differential Equations,” Numerische Mathematik, vol. 41, pp. 373–398.[9]   
Deuflhard, P. 1985, “Recent Progress in Extrapolation Methods for Ordinary Differential Equations,” SIAM Review, vol. 27, pp. 505–535.[10]   
Numerical Recipes Software 2007, “StepperSie Implementation,” Numerical Recipes Webnote No.24,athttp://www.nr.com/webnotes?24[11]   
Deuflhard, P. 1983, “Order and Stepsize Control in Extrapolation Methods,” Numerische Mathematik,vol. 41, pp.399-422.   
Enright, W.H., Hull, T.E., and Lindberg, B. 1975, “Comparing Numerical Methods for Stiff Systems of ODE’s,” BIT, vol. 15, pp. 10–48.   
Wanner, G. 1988, in Numerical Analysis 1987, Pitman Research Notes in Mathematics, vol. 170, D.F. Griffiths and G.A. Watson, eds. (Harlow, Essex, UK: Longman Scientific and Technical).   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer).

# 17.6 Multistep, Multivalue, and Predictor-Corrector Methods

The terms “multistep” and “multivalue” describe two different ways of implementing essentially the same integration technique for ODEs. Predictor-corrector is a particular subcategory of these methods — in fact, the most widely used. Accordingly, the name predictor-corrector is often loosely used to denote all these methods.

We suspect that predictor-corrector integrators have had their day, and that they are no longer the method of choice for most problems in ODEs. For high-precision applications, or applications where evaluations of the right-hand sides are expensive, Bulirsch-Stoer dominates. For convenience, or for moderate precision, adaptivestepsize Runge-Kutta dominates. Predictor-corrector methods have been, we think, squeezed out in the middle. There is possibly only one exceptional case: highprecision solution of very smooth equations with very complicated right-hand sides, as we will describe later.

Nevertheless, these methods have had a long historical run. Textbooks are full of information on them, and there are a lot of standard ODE programs around that are based on predictor-corrector methods. Many capable researchers have a lot of experience with predictor-corrector routines, and they see no reason to make a precipitous change of habit. It is not a bad idea for you to be familiar with the principles involved, and even with the sorts of bookkeeping details that are the bane of these methods. Otherwise, there will be a big surprise in store when you first have to fix a problem in a predictor-corrector routine.

Let us first consider the multistep approach. Think about how integrating an ODE is different from finding the integral of a function: For a function, the integrand has a known dependence on the independent variable $x$ and can be evaluated at will. For an ODE, the “integrand” is the right-hand side, which depends both on $x$ and on the dependent variables $y$ . Thus, to advance the solution of $y ^ { \prime } = f ( x , y )$ from $x _ { n }$ to $x$ , we have

$$
y ( x ) = y _ { n } + \int _ { x _ { n } } ^ { x } f ( x ^ { \prime } , y ) d x ^ { \prime } 
$$

In a single-step method like Runge-Kutta or Bulirsch-Stoer, the value $y _ { n + 1 }$ at $x _ { n + 1 }$ depends only on $y _ { n }$ . In a multistep method, we approximate $f ( x , y )$ by a polynomial passing through several previous points $x _ { n } , x _ { n - 1 } , \ldots .$ and possibly also through $x _ { n + 1 }$ . The result of evaluating the integral (17.6.1) at $x = x _ { n + 1 }$ is then of the form

$$
y _ { n + 1 } = y _ { n } + h ( \beta _ { 0 } y _ { n + 1 } ^ { \prime } + \beta _ { 1 } y _ { n } ^ { \prime } + \beta _ { 2 } y _ { n - 1 } ^ { \prime } + \beta _ { 3 } y _ { n - 2 } ^ { \prime } + \cdots )
$$

where $y _ { n } ^ { \prime }$ denotes $f ( x _ { n } , y _ { n } )$ , and so on. If $\beta _ { 0 } = 0$ , the method is explicit; otherwise it is implicit. The order of the method depends on how many previous steps we use to get each new value of $y$ .

Consider how we might solve an implicit formula of the form (17.6.2) for $y _ { n + 1 }$ Two methods suggest themselves: functional iteration and Newton’s method. In functional iteration, we take some initial guess for $y _ { n + 1 }$ , insert it into the right-hand side of (17.6.2) to get an updated value of $y _ { n + 1 }$ , insert this updated value back into the right-hand side, and continue iterating. But how are we to get an initial guess for $y _ { n + 1 } ?$ Easy! Just use some explicit formula of the same form as (17.6.2). This is called the predictor step. In the predictor step we are essentially extrapolating the polynomial fit to the derivative from the previous points to the new point $x _ { n + 1 }$ and then doing the integral (17.6.1) in a Simpson-like manner from $x _ { n }$ to $x _ { n + 1 }$ . The subsequent Simpson-like integration, using the prediction step’s value of $y _ { n + 1 }$ to interpolate the derivative, is called the corrector step. The difference between the predicted and corrected function values supplies information on the local truncation error that can be used to control accuracy and to adjust stepsize.

If one corrector step is good, aren’t many better? Why not use each corrector as an improved predictor and iterate to convergence on each step? Answer: Even if you had a perfect predictor, the step would still be accurate only to the finite order of the corrector. This incurable error term is on the same order as that which your iteration is supposed to cure, so you are at best changing only the coefficient in front of the error term by a fractional amount. So dubious an improvement is certainly not worth the effort. Your extra effort would be better spent in taking a smaller stepsize.

As described so far, you might think it desirable or necessary to predict several intervals ahead at each step, then to use all these intervals, with various weights, in a Simpson-like corrector step. That is not a good idea. Extrapolation is the least stable part of the procedure, and it is desirable to minimize its effect. Therefore, the integration steps of a predictor-corrector method are overlapping, each one involving several stepsize intervals $h$ , but extending just one such interval farther than the previous ones. Only that one extended interval is extrapolated by each predictor step.

The most popular predictor-corrector methods are probably the Adams-Bashforth-Moulton schemes, which have good stability properties. The Adams-Bashforth part is the predictor. For example, the third-order case is

$$
y _ { n + 1 } = y _ { n } + { \frac { h } { 1 2 } } ( 2 3 y _ { n } ^ { \prime } - 1 6 y _ { n - 1 } ^ { \prime } + 5 y _ { n - 2 } ^ { \prime } ) + O ( h ^ { 4 } )
$$

Here information at the current point $x _ { n }$ , together with the two previous points $x _ { n - 1 }$ and $x _ { n - 2 }$ (assumed equally spaced), is used to predict the value $y _ { n + 1 }$ at the next point, $x _ { n + 1 }$ . The Adams-Moulton part is the corrector. The third-order case is

$$
\mathrm { \mathrm { . o r r e c t o r : } } \qquad y _ { n + 1 } = y _ { n } + { \frac { h } { 1 2 } } ( 5 y _ { n + 1 } ^ { \prime } + 8 y _ { n } ^ { \prime } - y _ { n - 1 } ^ { \prime } ) + O ( h ^ { 4 } )
$$

Without the trial value of $y _ { n + 1 }$ from the predictor step to insert on the right-hand side, the corrector would be a nasty implicit equation for $y _ { n + 1 }$ . (Despite the names, these formulas are actually all due to Adams.)

There are actually three separate processes occurring in a predictor-corrector method: the predictor step, which we call P; the evaluation of the derivative $y _ { n + 1 } ^ { \prime }$ from the latest value of $y$ , which we call E; and the corrector step, which we call C.

In this notation, iterating $m$ times with the corrector (a practice we inveighed against earlier) would be written $\mathrm { P } ( \mathrm { E C } ) ^ { m }$ . One also has the choice of finishing with a C or an E step. The lore is that a final E is superior, so the strategy usually recommended is PECE.

Notice that a PC method with a fixed number of iterations (say, one) is an explicit method. When we fix the number of iterations in advance, the final value of $y _ { n + 1 }$ can be written as some complicated function of known quantities. Thus fixed iteration PC methods lose the strong stability properties of implicit methods and should only be used for nonstiff problems.

For stiff problems we must use an implicit method if we want to avoid having tiny stepsizes. (Not all implicit methods are good for stiff problems, but fortunately some good ones such as the Gear formulas are known.) We then appear to have two choices for solving the implicit equations: functional iteration to convergence, or Newton iteration. However, it turns out that for stiff problems functional iteration will not even converge unless we use tiny stepsizes, no matter how close our prediction is! Thus Newton iteration is usually an essential part of a multistep stiff solver. For convergence, Newton’s method doesn’t particularly care what the stepsize is, as long as the prediction is accurate enough.

Multistep methods, as we have described them so far, suffer from two serious difficulties when one tries to implement them:

- Since the formulas require results from equally spaced steps, adjusting the stepsize is difficult. Starting and stopping present problems. For starting, we need the initial values plus several previous steps to prime the pump. Stopping is a problem because equal steps are unlikely to land directly on the desired termination point.

Older implementations of PC methods have various cumbersome ways of dealing with these problems. For example, they might use Runge-Kutta to start and stop. Changing the stepsize requires considerable bookkeeping to do some kind of interpolation procedure. Fortunately, both these drawbacks disappear with the multivalue approach.

For multivalue methods (also called Nordsieck methods), the basic data available to the integrator are the first few terms of the Taylor series expansion of the solution at the current point $x _ { n }$ . The aim is to advance the solution and obtain the expansion coefficients at the next point $x _ { n + 1 }$ . This is in contrast to multistep methods, where the data are the values of the solution at $x _ { n } , x _ { n - 1 } , \ldots .$ We’ll illustrate the idea by considering a four-value method, for which the basic data are

$$
\begin{array} { r } { \mathbf { y } _ { n } \equiv \left( \begin{array} { c } { y _ { n } } \\ { h y _ { n } ^ { \prime } } \\ { ( h ^ { 2 } / 2 ) y _ { n } ^ { \prime \prime } } \\ { ( h ^ { 3 } / 6 ) y _ { n } ^ { \prime \prime \prime } } \end{array} \right) } \end{array}
$$

It is also conventional to scale the derivatives with the powers of $h = x _ { n + 1 } - x _ { n }$ as shown. Note that here we use the vector notation $\mathbf { y }$ to denote the solution and its first few derivatives at a point, not the fact that we are solving a system of equations with many components $y$ .

In terms of the data in (17.6.5), we can approximate the value of the solution $y$

at some point $x$ :

$$
y ( x ) = y _ { n } + ( x - x _ { n } ) y _ { n } ^ { \prime } + { \frac { ( x - x _ { n } ) ^ { 2 } } { 2 } } y _ { n } ^ { \prime \prime } + { \frac { ( x - x _ { n } ) ^ { 3 } } { 6 } } y _ { n } ^ { \prime \prime \prime }
$$

Set $x = x _ { n + 1 }$ in equation (17.6.6) to get an approximation to $y _ { n + 1 }$ . Differentiate equation (17.6.6) and set $x = x _ { n + 1 }$ to get an approximation to $y _ { n + 1 } ^ { \prime }$ , and similarly for $y _ { n + 1 } ^ { \prime \prime }$ and $y _ { n + 1 } ^ { \prime \prime \prime }$ . Call the resulting approximation $\widetilde { { \bf y } } _ { n + 1 }$ , where the tilde is a reminder that all we have done so far is a polynomial extrapolation of the solution and its derivatives; we have not yet used the differential equation. You can easily verify that

$$
\widetilde { { \bf y } } _ { n + 1 } = { \bf B } \cdot { \bf y } _ { n }
$$

where the matrix $\mathbf { B }$ is

$$
\mathbf { B } = { \left( \begin{array} { l l l l } { 1 } & { 1 } & { 1 } & { 1 } \\ { 0 } & { 1 } & { 2 } & { 3 } \\ { 0 } & { 0 } & { 1 } & { 3 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} \right) }
$$

We now write the actual approximation to ${ \bf y } _ { n + 1 }$ that we will use by adding a correction to $\widetilde { { \bf y } } _ { n + 1 }$ :

$$
\mathbf { y } _ { n + 1 } = \widetilde { \mathbf { y } } _ { n + 1 } + \alpha \mathbf { r }
$$

Here $\mathbf { r }$ will be a fixed vector of numbers, in the same way that $\mathbf { B }$ is a fixed matrix. We fix $\alpha$ by requiring that the differential equation

$$
y _ { n + 1 } ^ { \prime } = f ( x _ { n + 1 } , y _ { n + 1 } )
$$

be satisfied. The second of the equations in (17.6.9) is

$$
h y _ { n + 1 } ^ { \prime } = h \widetilde { y } _ { n + 1 } ^ { \prime } + \alpha r _ { 1 }
$$

and this will be consistent with (17.6.10) provided

$$
r _ { 1 } = 1 , \qquad \alpha = h f ( x _ { n + 1 } , y _ { n + 1 } ) - h \widetilde { y } _ { n + 1 } ^ { \prime }
$$

The values of $r _ { 0 } , r _ { 2 }$ , and $r _ { 3 }$ are free for the inventor of a given four-value method to choose. Different choices give different orders of method (i.e., through what order in $h$ the final expression 17.6.9 actually approximates the solution) and different stability properties.

An interesting result, not obvious from our presentation, is that multivalue and multistep methods are entirely equivalent. In other words, the value $y _ { n + 1 }$ given by a multivalue method with given $\mathbf { B }$ and $\mathbf { r }$ is exactly the same value given by some multistep method with given $\beta$ ’s in equation (17.6.2). For example, it turns out that the Adams-Bashforth formula (17.6.3) corresponds to a four-value method with $r _ { 0 } = 0$ , $r _ { 2 } = 3 / 4$ , and $r _ { 3 } = 1 / 6$ . The method is explicit because $r _ { 0 } = 0$ . The Adams-Moulton method (17.6.4) corresponds to the implicit four-value method with $r _ { 0 } = 5 / 1 2 , r _ { 2 } = 3 / 4$ , and $r _ { 3 } = 1 / 6$ . Implicit multivalue methods are solved the same way as implicit multistep methods: either by a predictor-corrector approach using an explicit method for the predictor, or by Newton iteration for stiff systems.

Why go to all the trouble of introducing a whole new method that turns out to be equivalent to a method you already knew? The reason is that multivalue methods allow an easy solution to the two difficulties we mentioned above in actually implementing multistep methods.

Consider first the question of stepsize adjustment. To change stepsize from $h$ to $h ^ { \prime }$ at some point $x _ { n }$ , simply multiply the components of ${ \bf y } _ { n }$ in (17.6.5) by the appropriate powers of $h ^ { \prime } / h$ , and you are ready to continue to $x _ { n } + h ^ { \prime }$ .

Multivalue methods also allow a relatively easy change in the order of the method: Simply change $\mathbf { r }$ . The usual strategy for this is first to determine the new stepsize with the current order from the error estimate. Then check what stepsize would be predicted using an order one greater and one smaller than the current order. Choose the order that allows you to take the biggest next step. Being able to change order also allows an easy solution to the starting problem: Simply start with a first-order method and let the order automatically increase to the appropriate level.

For moderate accuracy requirements, the most efficient choice is almost always a Runge-Kutta routine like StepperDopr853. For high accuracy, StepperBS is both robust and efficient. For very smooth functions, a variable-order PC method can invoke very high orders. If the right-hand side of the equation is relatively complicated, so that the expense of evaluating it outweighs the bookkeeping expense, then the best PC packages can outperform Bulirsch-Stoer on such problems. As you can imagine, however, such a variable-stepsize, variable-order method is not trivial to program. If you suspect that your problem is suitable for this treatment, we recommend the use of a packaged PC routine. For further details consult [1-3].

Our prediction is that, as extrapolation methods like Bulirsch-Stoer continue to gain sophistication, they will eventually beat out PC methods in all applications. We are willing, however, to be corrected.

# CITED REFERENCES AND FURTHER READING:

Gear, C.W. 1971, Numerical Initial Value Problems in Ordinary Differential Equations (Englewood Cliffs, NJ: Prentice-Hall), Chapter 9.[1]   
Shampine, L.F., and Gordon, M.K. 1975, Computer Solution of Ordinary Differential Equations. The Initial Value Problem. (San Francisco: W.H Freeman).[2]   
Hairer, E., Nørsett, S.P., and Wanner, G. 1993, Solving Ordinary Differential Equations I. Nonstiff Problems,2nd ed.(New York: Springer).[3]   
Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), Chapter 5.   
Kahaner, D., Moler, C., and Nash, S. 1989, Numerical Methods and Software (Englewood Cliffs, NJ: Prentice-Hall), Chapter 8.   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), Chapter 7.

# 17.7 Stochastic Simulation of Chemical Reaction Networks

We are so used to thinking of chemical (or nuclear) reaction networks as implying sets of continuous differential equations, that it takes an effort to remember

their underlying discrete, atomic, nature. To give an example, we have all learned to translate a set of reactions like

$$
\begin{array} { r } { A + X \xrightarrow { k _ { 0 } } 2 X } \\ { X + Y \xrightarrow { k _ { 1 } } 2 Y } \\ { Y \xrightarrow { k _ { 2 } } B } \end{array}
$$

into a set of differential equations (rate equations) governing the concentrations of each species,

$$
{ \begin{array} { l } { { \frac { d [ A ] } { d t } } = - k _ { 0 } [ A ] [ X ] \equiv - a _ { 0 } } \\ { { \frac { d [ X ] } { d t } } = k _ { 0 } [ A ] [ X ] - k _ { 1 } [ X ] [ Y ] \equiv a _ { 0 } - a _ { 1 } } \\ { { \frac { d [ Y ] } { d t } } = k _ { 1 } [ X ] [ Y ] - k _ { 2 } [ Y ] \equiv a _ { 1 } - a _ { 2 } } \\ { { \frac { d [ B ] } { d t } } = k _ { 2 } [ Y ] \equiv a _ { 2 } } \end{array} }
$$

where $a _ { 0 } , ~ a _ { 1 }$ , and $a _ { 2 }$ are respectively the rates of the three reactions in equation (17.7.1).

Increasingly in biological applications, however, one is faced with situations where the actual numbers of reacting molecules is so small that discreteness effects and fluctuations become important. In such cases, one needs to replace continuum concentrations like $[ X ]$ and ŒY  with actual numbers of molecular species. The equations (17.7.2) now become meaningless. What we need to do is directly simulate the discrete reactions in (17.7.1), assigning a sequence of stochastically generated times, and corresponding discrete changes in species numbers, to the occurrences of each reaction. This task is known as stochastic simulation, from the original work of Gillespie [1]. Stochastic simulation is a remarkably simple, and elegant, technique. Like many powerful tools, it can be both used and misused, as we will discuss.

Before we get to the details, it is useful to formalize some aspects of the structure of equations (17.7.1) and (17.7.2). In general, we have $M$ reactions occurring among $N$ species. Each reaction $j = 0 , \ldots , M - 1$ , has an instantaneous rate, denoted $a _ { j }$ . In the discrete case, $1 / a _ { j }$ is the mean time until the next occurrence of reaction $j$ , if no other reaction happens first. An important point is that each rate $a _ { j }$ depends only on the numbers of those species on the left-hand side of reaction $j$ , its reactants. Define a reactant matrix $\lambda _ { i j }$ by

$$
\lambda _ { i j } = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } { \mathrm { s p e c i e s ~ } } S _ { i } { \mathrm { ~ i s ~ a n ~ i n p u t ~ t o ~ r e a c t i o n ~ } } j } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

On the output side (products), each set of reactions $j$ is characterized by a state change matrix $\nu _ { i j }$ whose $i , j$ component is the net change in the number of species $S _ { i }$ due to one occurrence of reaction $j$ . (The $j$ th column of this matrix is often called the state change vector for reaction $j$ .) In terms of these quantities, the conventional rate equations, like (17.7.2), can be written in general as

$$
\frac { d [ S _ { i } ] } { d t } = \sum _ { j = 0 } ^ { M - 1 } \nu _ { i j } a _ { j } ( \{ [ S _ { k } ] \} ) , \quad k \mathrm { ~ s . t . ~ } \lambda _ { k j } \neq 0 , \quad i = 0 , \ldots , N - 1
$$

But back to the discrete case: At an instant in time, if we know all the $S _ { i }$ ’s, we can compute all the rates $a _ { j }$ . Since rates are additive, the total rate at which something will happen is

$$
a _ { \mathrm { t o t } } = \sum _ { j = 0 } ^ { M - 1 } a _ { j }
$$

Moreover, because the system is assumed to be “memoryless” (except for the $S _ { j }$ ’s) and “well-mixed,” the probability distribution of times to this next occurrence of some reaction $j$ must be exponentially distributed (like radioactive decay). Furthermore, given that some reaction occurs, it is easy to state what is the probability distribution of which reaction it is: It will be reaction $j$ with probability $a _ { j } / a _ { \mathrm { t o t } }$ .

This is all there is, conceptually, to stochastic simulation. The rest is just implementation details, including some clever tricks to speed up the calculation. The steps in the so-called direct method are

- Draw a random number $U _ { 1 }$ , uniform in Œ0; 1, and compute the time $\tau$ to the next reaction by

$$
\tau = \frac { 1 } { a _ { \mathrm { t o t } } } \log { \left( \frac { 1 } { U _ { 1 } } \right) }
$$

(This generates an exponential distribution; cf. $\ S 7 . 3 .$ )

- Draw a second uniform random number $U _ { 2 }$ in Œ0; 1 and find the smallest $k$ such that

$$
\sum _ { j = 0 } ^ { k } a _ { j } > a _ { \mathrm { t o t } } U _ { 2 }
$$

A value $k$ will thus be chosen with probability ${ a } _ { k } / { a } _ { \mathrm { t o t } }$

- Increment the time $t$ by $\tau$ .   
- Update each $S _ { i }$ by adding the value $\nu _ { i k }$ .   
- Go back to the first step.

# 17.7.1 Speeding Up the Direct Method

We can speed up the direct method, first, by identifying all steps that are (naively) of $O ( M )$ or $O ( N )$ and finding ways to make them $O ( 1 )$ (or maybe log); and second, by hand-crafting the inner loop of the program to have the fastest possible execution. The second of these tasks is very important and can make or break a stochastic simulation code’s performance; but, unfortunately, it is very machine-, compiler-, and problem-dependent, so it is outside our scope here.

As for the first task, we first note that realistic reaction networks of any size almost always have very sparse reactant and state change matrices: Reactions generally involve only one or two reactants and produce at most a few products. Therefore, it is important to use some kind of sparse matrix structure for the matrices that occur.

When $\nu _ { i j }$ is stored sparsely, for example, the updating step is reduced from $O ( N )$ to $O ( 1 )$ .

Next, we note that most $a _ { j }$ ’s are unchanged after each reaction occurs. After a reaction $k$ , for example, the only $a _ { j }$ ’s that need to be recomputed are those with reactants (inputs) that were changed by a nonzero entry in the $k$ th column of the $\nu _ { j k }$ matrix. A way to formalize this is by a dependency graph or dependency matrix $G$ , whose component $G _ { j k }$ is nonzero only if reaction $k$ changes a species that is an input to reaction $j$ . With a moment of thought, you will figure out that the matrix $G$ can be obtained by the logical matrix multiplication of $\lambda ^ { T }$ and $\nu$ , namely

$$
G _ { i j } = \bigcup _ { k } \lambda _ { k i } \cap \nu _ { k j }
$$

where $\cup$ denotes logical-or, $\cap$ denotes logical-and, and the C convention of “true iff nonzero” is assumed. Now, after each reaction $j$ , we only update the $a _ { i }$ ’s indicated by the $j$ th column of $G _ { i j }$ . Of course we must also store $G$ in a sparse format.

Finally, there is the question of how to speed up the choice of which reaction to update, equation (17.7.7), which can be at worst $O ( M )$ . Here there are two schools of thought. The one that we implement below, following advice in [3], takes advantage of the fact that for many, if not most, actual applications, a small number of reactions $( \ll M )$ ) dominate the reaction rates. If we arrange the order of the $a _ { j }$ ’s in equation (17.7.7) with these dominant reactions first, then it can take, on average, only O(1) tests to select the next reaction. In [3], it is suggested to do preliminary runs to find which reactions dominate. We prefer the more transparent alternative, implemented below, of just letting frequent reactions adaptively bubble up in a priority list.

The other school of thought, called the next reaction method [2], is discussed separately, below. It cleverly changes $O ( M )$ to something like ${ \cal O } ( \log M )$ , even in the most unfavorable case. However, the number of operations in the inner program loop is significantly larger than for the (optimized, as above) direct method. Which method is fastest is very likely problem- and implementation-dependent.

For the modest test case illustrated, namely the set of three reactions (17.7.1), most of the optimizations illustrated in the following code are unnecessary, and likely counterproductive. However, the intent is to be illustrative of what a code for larger problems would look like.

# struct Stochsim {

bject for stochastic simulation of a set of chemical reactions.

VecDoub s;   
VecDoub a;   
MatDoub instate, outstate;   
NRvector<NRsparseCol> outchg, depend;   
VecInt pr;   
Doub t, asum;   
Ran ran;   
typedef Doub(Stochsim::\*rateptr)();   
rateptr \*dispatch;

Sparse matrices $\nu _ { i j }$ and $G _ { i j }$ Priority list.

Obscure ${ \mathsf { C } } { + } { + }$ used to create a vector dispatch of function pointers to the rate functions.

# // begin user section

Replace this section, using as a template the example (17.7.1) shown here, by the particulars of your reaction network. If you have a large number of reactions, you will want to generate the matrices instate and outstate externally, and pass them as globals (or read them here).

static const Int mm $\scriptstyle = 3$ ;   
static const Int nn $_ { = 4 }$ ; Set number of reactions.   
Set number of species.

Doub k0,k1,k2; Doub rate0() {return k0\*s[0]\*s[1];} Doub rate1() {return k1\*s[1]\*s[2];} Doub rate2() {return k2\*s[2];} void describereactions () {

Declare any rate constants needed.   
Your rate functions go here.

You provide a function with this name that sets any constants that you have defined and sets the instate and outstate matrices to describe your reactions.

The reactant matrix $\lambda _ { i j }$

$\mathbf { k } 0 \ = \ 0 . 0 1$ ; $\mathrm { k } 1 ~ = ~ . 1$ ; $\mathbf { k } 2 \ = \ 1 .$ ; Doub indat[] = { 1.,0.,0., 1.,1.,0., 0.,1.,1., 0.,0.,0. }; instate $=$ MatDoub(nn,mm,indat); Doub outdat[] $= \downarrow$ -1.,0.,0., 1.,-1.,0., 0.,1.,-1., 0.,0.,1. }; outstate $=$ MatDoub(nn,mm,outdat); dispatch[0] $=$ &Stochsim::rate0; dispatch[1] $=$ &Stochsim::rate1; dispatch[2] $=$ &Stochsim::rate2; } // end user section

The state change matrix $\nu _ { i j }$

You must also point the dispatch table entries to the correct rate functions.

Stochsim(VecDoub &sinit, Int seed=1)   
Constructor. Input initial species numbers and an optional random seed.   
: s(sinit), $\mathsf { a } ( \mathsf { m m } , 0 . )$ , outchg(mm), depend(mm), pr(mm), t(0.),   
asum(0.), ran(seed), dispatch(new rateptr[mm]) { Int i,j,k,d; describereactions(); sparmatfill(outchg,outstate); MatDoub dep(mm,mm); for ( $\scriptstyle \dot { 1 } = 0$ ;i<mm; $\dot { \bf 1 } + +$ ) for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<mm;j++) { Logical matrix multiply calculates the $\texttt { d } = \texttt { 0 }$ ; dependency matrix. for $\scriptstyle \mathbf { k } = 0$ ;k<nn;k++) $\mathrm { ~ d ~ } = \mathrm { ~ d ~ } \mid \mid$ (instate[k][i] && outstate[k][j]); dep[i][j] $\mathit { \Theta } = \mathit { \Theta } \mathtt { d }$ ; } sparmatfill(depend,dep); for (i=0;i<mm; $\dot { \bf 1 } + +$ ) { Calculate all initial rates. pr[i] $= \dot { \mathrm { ~ \scriptsize ~ 1 ~ ; ~ } }$ a[i] $=$ (this->\*dispatch[i])(); asum $+ = \texttt { a } [ \mathrm { i } ]$ ; }   
}

# \~Stochsim() {delete [] dispatch;}

# Doub step() {

Take a single stochastic step (one reaction) and return the new time.

Int i,n,m, $\mathtt { k } = 0$ ;   
Doub tau,atarg,sum,anew;   
if (asum $\mathrm { = } \mathrm { = } \mathrm { ~ 0 ~ . ~ }$ ) {t $* = ~ 2 .$ .; return t;} tau $=$ -log(ran.doub())/asum;   
atarg $=$ ran.doub()\*asum;   
sum $=$ a[pr[0]];   
while (sum $<$ atarg) sum $+ =$ a[pr[++k]];   
$\mathrm { ~ m ~ } = \mathrm { ~ p r [ k ] ~ }$ ;   
if $\mathrm { ~ ( ~ \mathbf ~ k ~ } > \mathrm { ~ \boldsymbol ~ O ~ } ,$ ) SWAP(pr[k],pr[k-1]);   
if $\mathrm { ( k \Omega ) = = \ m m - 1 } .$ ) asum $=$ sum;

Rare: All reactions have stopped exactly, so double the time until the user notices!

Equation (17.7.7).

Move reaction up on the priority list. Free update of asum fixes accumulated roundoff.

$\mathrm { ~ n ~ } =$ outchg[m].nvals; for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<n;i++) { Apply state change vector. $\mathrm { ~ \bf ~ k ~ } =$ outchg[m].row_ind[i]; s[k] $+ =$ outchg[m].val[i]; } $\mathrm { ~ n ~ } =$ depend[m].nvals; for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n; $\mathbf { i } + +$ ) { Recalculate rates required by depen-$\mathrm { ~ \bf ~ k ~ } =$ depend[m].row_ind[i]; dency matrix. anew $=$ (this->\*dispatch[k])(); asum $+ =$ (anew - a[k]); a[k] $=$ anew; } if (t\*asum < 0.1) Rare: Rates heading toward zero. for (asum $_ { = 0 }$ ., $\mathtt { i } = 0$ ;i<mm; $\mathbf { i } + +$ ) asum $+ =$ a[i]; Better recalculate asum. return $( \ t \ + = \ \tan )$ ; }

Note that Stochsim uses some arcane $\mathrm { C } { + + }$ syntax (“array of pointers to member functions”) in connection with the identifier dispatch. The underlying idea is simple, and important: We want to jump directly to the appropriate user-supplied rate function, as directed by an integer index. There are various ways of coding this, but what you don’t want to have is a long chain of if tests that would be $O ( M )$ instead of $O ( 1 )$ . (Perhaps we should believe that C’s switch statement is always properly implemented by compilers as a fast table dispatch, but we don’t.)

The utility routine that constructs a sparse matrix out of a full one is this (cf. -2.7):

void sparmatfill(NRvector<NRsparseCol> &sparmat, MatDoub &fullmat) {   
Utility that fills a sparse matrix from a full one. See $\ S 2 . 7$ . Int n,m,nz,nn=fullmat.nrows(),mm=fullmat.ncols(); if (sparmat.size() $! = \ \mathtt { m m } .$ ) throw("bad sizes"); for $\mathrm { { m } = 0 \ ; \mathrm { { m } < \mathrm { { m m } \ ; \mathrm { { m } + + } } } } )$ { for $( \mathtt { n z - n - 0 } ; \mathtt { n < n n } ; \mathtt { n + + } )$ if (fullmat[n][m]) nz++; sparmat[m].resize(nn,nz); for ( $\scriptstyle \mathtt { n z } = \mathtt { n } = 0$ ;n<nn; $\mathrm { n } { + } { + }$ ) if (fullmat[n][m]) { sparmat[m].row_ind[nz] $= \mathrm { ~ n ~ }$ ; sparmat[m].val[nz++] $=$ fullmat[n][m]; } }   
}

As a cultural note, the system (17.7.1) is not just any old chemical reaction network, but is actually a form of the Lotka-Volterra equation, discovered independently by Alfred J. Lotka and Vito Volterra in 1925–1926. In fact, it’s not originally a chemical reaction network at all, but a set of relationships intended to model predator-prey relationships. The first equation says, roughly, that rabbits (X) eat grass (A) to produce more rabbits. The second says that foxes (Y) eat rabbits $( \mathrm { X } )$ to produce more foxes. The third says that foxes don’t live forever. (For some reason, rabbits do live forever in this model, unless they are eaten by foxes.)

Figure 17.7.1 shows an example of the system’s evolution, starting with initial conditions $A = 1 5 0$ , $X = Y = 1 0$ , and $B = 0$ . One sees two cycles of prey population growth, with predator growth following, and then a collapse of both populations. After the second cycle, by a fluctuation, the predator population goes to zero, from which it cannot recover. At the end of the evolution shown, the prey population is starting to recover; but it is not a happy ending, because, by now, the food supply is running out. The world of stochastic simulation is a harsh one. Stochastic effects are genuinely dominant in this example: Exactly the same equations and initial conditions, but with a different random seed, give entirely different evolutions.

![](images/43c120c526c365b84b73c55e57327100f5fb220af38c991577735d4f726b81c2.jpg)  
Figure 17.7.1. Evolution of the reaction network (17.7.1). This network evolves by the Lotka-Volterra equations, originally developed as a model for predator-prey interactions. Stochastic effects are important; with different random seeds, different time histories occur.

# 17.7.2 Next Reaction Method

The next reaction method [2] starts by computing not a single reaction time, equation (17.7.6), but rather a separate next reaction time for each reaction $j$ ,

$$
\tau _ { j } = \frac { 1 } { a _ { j } } \log \left( \frac { 1 } { U _ { j } } \right)
$$

where the $U _ { j }$ ’s are independent uniform random deviates in Œ0; 1. These times are all stored in a heap (see $\ S 8 . 3 )$ , so that the smallest value can be easily accessed at the top of the heap (call it $k$ ). The following steps are now repeatedly executed:

- Do reaction $k$ and update the affected $S _ { i }$ ’s (using the matrix $\nu _ { i k }$ ). Increment time $t$ by $\tau _ { k }$ . Compute a next time for reaction $k$ (using equation 17.7.9 and adding $t$ ) and store it on the heap.   
- For every affected reaction $j$ (as determined by a nonzero entry $G _ { j k }$ ), correct its stored next time by the formula

$$
\tau _ { j } \gets \frac { a _ { j , \mathrm { o l d } } } { a _ { j , \mathrm { n e w } } } ( \tau _ { j } - t ) + t
$$

This is called time reuse. In effect, it reuses the random deviate $U _ { j }$ that originally generated $\tau _ { j }$ , but it corrects the resulting time prediction for an intermediate step function change in $a _ { j }$ . Sounds dodgy, we know, but it is probabilistically sound.

- Get the heap back into order by bubbling elements up or down as required. This is where the complexity of the inner loop gets increased, to as much as ${ \cal O } ( \log M )$ .

Unquestionably, one can construct reaction networks for which the next reaction method is considerably faster than the optimized direct method. However, networks dominated by a small number of fast reactions are so common in practice that this performance advantage should not be assumed a priori [3].

# 17.7.3 Practical Advice

Don’t ever use a stochastic simulation method — of any flavor — unless your problem is genuinely stochastic. Instead, use the deterministic rate equations (17.7.4) with a good stiff equation solver like StepperSie in $\ S 1 7 . 5$ . Such solvers are not limited by the rate of the fastest reaction, and will frequently be orders of magnitude faster than any stochastic method. (We are reliably informed that an unconscionable number of CPU hours are wasted by misguided researchers who think that the stochastic simulation method is an all-purpose tool for reaction networks.)

Just to show you how easy this is, here is how you would do the Lotka-Volterra problem (17.7.2) by integrating the equations directly. First encode the right-hand side f and the Jacobian of the right-hand side in a structure. (The $( i , j )$ element of the Jacobian is $\partial f _ { i } / \partial y _ { j }$ .)

# struct rhs {

Doub k0,k1,k2; rhs(Doub kk0, Doub kk1, Doub kk2) : k0(kk0),k1(kk1),k2(kk2) {} void operator() (const Doub x, VecDoub_I &y, VecDoub_O &dydx) { dydx[0] $=$ -k0\*y[0]\*y[1]; dydx[1] $=$ k0\*y[0]\*y[1]-k1\*y[1]\*y[2]; dydx[2] $=$ k1\*y[1]\*y[2]-k2\*y[2]; dydx[3] $=$ k2\*y[2]; } void jacobian(const Doub x, VecDoub_I &y, VecDoub_O &dfdx, MatDoub_O &dfdy) { Int n=y.size(); for (Int $\mathtt { i } = 0$ ;i<n;i++) dfdx[i] ${ = } 0$ .0; dfdy[0][0] $=$ -k0\*y[1]; dfdy[0][1] $=$ -k0\*y[0]; dfdy[0][2] $= ~ 0 . 0$ ; dfdy[0][3] $= ~ 0 , 0$ ; dfdy[1][0] $=$ k0\*y[1]; dfdy[1][1] $=$ k0\*y[0]-k1\*y[2]; dfdy[1][2] $=$ -k1\*y[1]; dfdy[1][3] $\mathbf { \Omega } = \mathbf { \Omega } 0 . 0 :$ ; dfdy[2][0] $= ~ 0 , 0$ ; dfdy[2][1] $=$ k1\*y[2]; dfdy[2][2] $=$ k1\*y[1]-k2; dfdy[2][3] $= ~ 0 . 0$ ; dfdy[3][0] $\mathbf { \Omega } = \mathbf { \Omega } 0 . 0 :$ ; dfdy[3][1] $\mathbf { \Omega } = \mathbf { \Omega } 0 . 0 :$ ; dfdy[3][2] $\ l = \ \mathbf { k } 2$ ; dfdy[3][3] $= ~ 0 , 0$ ; } };

Next set the parameters for Odeint, for example

const Int $\mathtt { n } { = } 4$ ;   
Doub rtol ${ = } 1$ .0e-7,atol $^ { = 1 }$ .0e-4\*rtol,h1 $= 1$ .0e-6,hmin=0.0,x1=0.0,x2=15.0;   
VecDoub ystart(n);   
ystart[0] $=$ 150.0;   
ystart[1] $= 1 0 . 0$ ; ystart[2] $=$ 10.0;   
ystart[3] ${ = } 0$ .0;   
Output out(100); Output at 100 uniform points rhs d(0.01,0.1,1.0); Declare d as a rhs object.   
Odeint<StepperSIE<rhs> $>$ ode(ystart,x1,x2,atol,rtol,h1,hmin,out,d);   
ode.integrate();

Note how the values of $k _ { 0 }$ , $k _ { 1 }$ , and $k _ { 2 }$ are passed as arguments in the constructor call that declares d. These particular values don’t make the system of equations particularly stiff, so you could use a standard integrator. However, this is not true in general for real-world examples.

The output, which is equally spaced, can be printed by statements like for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<out.count;i++) cout $< <$ out.xsave[i] $< < ~ "$ " << out.ysave[0][i] << " " << out.ysave[1][i] << " " << out.ysave[2][i] $< <$ endl;

If your network’s fastest reactions are not stochastic, but there are some slower reactions where stochastic effects are important, then look into so-called hybrid methods (e.g., [4]).

# CITED REFERENCES AND FURTHER READING:

Gillespie, D.T. 1976, “A General Method for Numerically Simulating the Stochastic Time Evolution of Coupled Chemical Reactions,” Journal of Computational Physics, vol. 11, pp. 403– 434.[1]   
Gibson, M.A., and Bruck, J. 2000, “Efficient Exact Stochastic Simulation of Chemical Systems with Many Species and Many Channels,” Journal of Physical Chemistry A, vol. 104, pp. 1876–1889.[2]   
Cao, Y., Li, H., and Petzold, L. 2004, “Efficient Formulation of the Stochastic Simulation Algorithm for Chemically Reacting Systems,” Journal of Chemical Physics, vol. 121, pp. 4059– 4067.[3]   
Salis, H., and Kaznessis, Y. 2005, “Accurate Hybrid Stochastic Simulation of a System of Coupled Chemical or Biochemical Reactions,” Journal of Chemical Physics, vol. 122, art. 054103.[4]

# Two-Point Boundary Value Problems

# 18.0 Introduction

When ordinary differential equations are required to satisfy boundary conditions at more than one value of the independent variable, the resulting problem is called a two-point boundary value problem. As the terminology indicates, the most common case by far is where boundary conditions are supposed to be satisfied at two points — usually the starting and ending values of the integration. However, the phrase “two-point boundary value problem” is also used loosely to include more complicated cases, e.g., where some conditions are specified at endpoints, others at interior (usually singular) points.

The crucial distinction between initial value problems (Chapter 17) and twopoint boundary value problems (this chapter) is that in the former case we are able to start an acceptable solution at its beginning (initial values) and just march it along by numerical integration to its end (final values), while in the present case the boundary conditions at the starting point do not determine a unique solution to start with — and a “random” choice among the solutions that satisfy these (incomplete) starting boundary conditions is almost certain not to satisfy the boundary conditions at the other specified point(s).

It should not surprise you that iteration is in general required to meld these spatially scattered boundary conditions into a single global solution of the differential equations. For this reason, two-point boundary value problems require considerably more effort to solve than do initial value problems. You have to integrate your differential equations over the interval of interest, or perform an analogous “relaxation” procedure (see below), at least several, and sometimes very many, times. Only in the special case of linear differential equations can you say in advance just how many such iterations will be required.

The “standard” two-point boundary value problem has the following form: We desire the solution to a set of $N$ coupled first-order ordinary differential equations, satisfying $n _ { 1 }$ boundary conditions at the starting point $x _ { 1 }$ and a remaining set of $n _ { 2 } = N - n _ { 1 }$ boundary conditions at the final point $x _ { 2 }$ . (Recall that all differential equations of order higher than first can be written as coupled sets of first-order

![](images/40405644f6abe8297ffbfa90463f4c6143462034da52233680d4cc1d365c3694.jpg)  
Figure 18.0.1. Shooting method (schematic). Trial integrations that satisfy the boundary condition at one endpoint are “launched.” The discrepancies from the desired boundary condition at the other endpoint are used to adjust the starting conditions, until boundary conditions at both endpoints are ultimately satisfied.

equations; cf. $\ S 1 7 . 0 . \rangle$ )

The differential equations are

$$
\frac { d y _ { i } ( x ) } { d x } = g _ { i } ( x , y _ { 0 } , y _ { 1 } , \ldots , y _ { N - 1 } ) \qquad i = 0 , 1 , \ldots , N - 1
$$

At $x _ { 1 }$ , the solution is supposed to satisfy

$$
B _ { 1 j } ( x _ { 1 } , y _ { 0 } , y _ { 1 } , \ldots , y _ { N - 1 } ) = 0 \qquad j = 0 , \ldots , n _ { 1 } - 1
$$

while at $x _ { 2 }$ , it is supposed to satisfy

$$
B _ { 2 k } ( x _ { 2 } , y _ { 0 } , y _ { 1 } , \ldots , y _ { N - 1 } ) = 0 \qquad k = 0 , \ldots , n _ { 2 } - 1
$$

There are two distinct classes of numerical methods for solving two-point boundary value problems. In the shooting method (-18.1) we choose values for all of the dependent variables at one boundary. These values must be consistent with any boundary conditions for that boundary, but otherwise are arranged to depend on arbitrary free parameters whose values we initially “randomly” guess. We then integrate the ODEs by initial value methods, arriving at the other boundary (and/or any interior points with boundary conditions specified). In general, we find discrepancies from the desired boundary values there. Now we have a multidimensional root-finding problem, as was treated in $\ S 9 . 6$ and $\ S 9 . 7$ : Find the adjustment of the free parameters at the starting point that zeros the discrepancies at the other boundary point(s). If we liken integrating the differential equations to following the trajectory of a shot from gun to target, then picking the initial conditions corresponds to aiming (see Figure 18.0.1). The shooting method provides a systematic approach to taking a set of “ranging” shots that allow us to improve our “aim” systematically.

As another variant of the shooting method (-18.2), we can guess unknown free parameters at both ends of the domain, integrate the equations to a common midpoint, and seek to adjust the guessed parameters so that the solution joins “smoothly” at the fitting point. In all shooting methods, trial solutions satisfy the differential


<!-- chunk 0015: pages 981-1050 -->
![](images/9e88795f3857bd7be0897a0e28479ec33f1aa5c6fa50b595d8054621db7644f4.jpg)  
Figure 18.0.2. Relaxation method (schematic). An initial solution is guessed that approximately satisfies the differential equation and boundary conditions. An iterative process adjusts the function to bring it into close agreement with the true solution.

equations “exactly” (or as exactly as we care to make our numerical integration), but the trial solutions come to satisfy the required boundary conditions only after the iterations are finished.

Relaxation methods use a different approach. The differential equations are replaced by finite difference equations on a mesh of points that covers the range of the integration. A trial solution consists of values for the dependent variables at each mesh point, not satisfying the desired finite difference equations, nor necessarily even satisfying the required boundary conditions. The iteration, now called relaxation, consists of adjusting all the values on the mesh so as to bring them into successively closer agreement with the finite difference equations and, simultaneously, with the boundary conditions (see Figure 18.0.2). For example, if the problem involves three coupled equations and a mesh of 100 points, we must guess and improve 300 variables representing the solution.

With all this adjustment, you may be surprised that relaxation is ever an efficient method, but (for the right problems) it really is! Relaxation works better than shooting when the boundary conditions are especially delicate or subtle, or where they involve complicated algebraic relations that cannot easily be solved in closed form. Relaxation works best when the solution is smooth and not highly oscillatory. Such oscillations would require many grid points for accurate representation. The number and position of required points may not be known a priori. Shooting methods are usually preferred in such cases, because their variable stepsize integrations adjust naturally to a solution’s peculiarities.

Relaxation methods are often preferred when the ODEs have extraneous solutions that, while not appearing in the final solution satisfying all boundary conditions, may wreak havoc on the initial value integrations required by shooting. The typical case is that of trying to maintain a dying exponential in the presence of growing exponentials.

Good initial guesses are the secret of efficient relaxation methods. Often one has to solve a problem many times, each time with a slightly different value of some parameter. In that case, the previous solution is usually a good initial guess when the parameter is changed, and relaxation will work well.

Until you have enough experience to make your own judgment between the two methods, you might wish to follow the advice of your authors, who are notorious computer gunslingers: We always shoot first, and only then relax.

# 18.0.1 Problems Reducible to the Standard Boundary Problem

There are two important problems that can be reduced to the standard boundary value problem described by equations $( 1 8 . 0 . 1 ) - ( 1 8 . 0 . 3 )$ . The first is the eigenvalue problem for differential equations. Here the right-hand side of the system of differential equations depends on a parameter $\lambda$ ,

$$
{ \frac { d y _ { i } ( x ) } { d x } } = g _ { i } ( x , y _ { 0 } , \dots , y _ { N - 1 } , \lambda )
$$

and one has to satisfy $N + 1$ boundary conditions instead of just $N$ . The problem is overdetermined and in general there is no solution for arbitrary values of $\lambda$ . For certain special values of $\lambda$ , the eigenvalues, equation (18.0.4) does have a solution.

We reduce this problem to the standard case by introducing a new dependent variable

$$
y _ { N } \equiv \lambda
$$

and another differential equation

$$
{ \frac { d y _ { N } } { d x } } = 0
$$

An example of this trick is given in $\ S 1 8 . 4$ .

The other case that can be put in the standard form is a free boundary problem. Here only one boundary abscissa $x _ { 1 }$ is specified, while the other boundary $x _ { 2 }$ is to be determined so that the system (18.0.1) has a solution satisfying a total of $N + 1$ boundary conditions. Here we again add an extra constant dependent variable:

$$
\begin{array} { c } { { y _ { N } \equiv x _ { 2 } - x _ { 1 } } } \\ { { } } \\ { { { \frac { d y _ { N } } { d x } } = 0 } } \end{array}
$$

We also define a new independent variable $t$ by setting

$$
x - x _ { 1 } \equiv t y _ { N } , \qquad 0 \leq t \leq 1
$$

The system of $N + 1$ differential equations for $d y _ { i } / d t$ is now in the standard form, with $t$ varying between the known limits 0 and 1.

# CITED REFERENCES AND FURTHER READING:

Keller, H.B. 1968, Numerical Methods for Two-Point Boundary-Value Problems; reprinted 1991 (New York: Dover).   
Kippenhan, R., Weigert, A., and Hofmeister, E. 1968, in Methods in Computational Physics, vol. 7 (New York: Academic Press), pp. 129ff.   
Eggleton, P.P. 1971, “The Evolution of Low Mass Stars,” Monthly Notices of the Royal Astronomical Society,vol.151, pp.351-364.   
London, R.A., and Flannery, B.P. 1982, “Hydrodynamics of X-Ray Induced Stellar Winds,” Astrophysical Journal, vol. 258, pp.260-269.   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 7 . 3 - \ S 7 . 4$ .

# 18.1 The Shooting Method

In this section we discuss “pure” shooting, where the integration proceeds from $x _ { 1 }$ to $x _ { 2 }$ , and we try to match boundary conditions at the end of the integration. In the next section, we describe shooting to an intermediate fitting point, where the solution to the equations and boundary conditions is found by launching “shots” from both sides of the interval and trying to match continuity conditions at some intermediate point.

Our implementation of the shooting method exactly implements multidimensional, globally convergent Newton-Raphson (-9.7). It seeks to zero $n _ { 2 }$ functions of $n _ { 2 }$ variables. The functions are obtained by integrating $N$ differential equations from $x _ { 1 }$ to $x _ { 2 }$ . Let us see how this works.

At the starting point $x _ { 1 }$ there are $N$ starting values $y _ { i }$ to be specified, but subject to $n _ { 1 }$ conditions. Therefore there are $n _ { 2 } = N - n _ { 1 }$ freely specifiable starting values. Let us imagine that these freely specifiable values are the components of a vector $\mathbf { V }$ that lives in a vector space of dimension $n _ { 2 }$ . Then you, the user, knowing the functional form of the boundary conditions (18.0.2), can write a function or functor that generates a complete set of $N$ starting values $\mathbf { y }$ , satisfying the boundary conditions at $x _ { 1 }$ , from an arbitrary vector value of $\mathbf { V }$ in which there are no restrictions on the $n _ { 2 }$ component values. In other words, (18.0.2) converts to a prescription

$$
y _ { i } ( x _ { 1 } ) = y _ { i } ( x _ { 1 } ; V _ { 0 } , \ldots , V _ { n _ { 2 } - 1 } ) \qquad i = 0 , \ldots , N - 1
$$

In the routine Shoot below, the function or functor that implements (18.1.1) will be called load, but you can pass it as an argument to the routine with any name of your choosing.

Notice that the components of $\mathbf { V }$ might be exactly the values of certain “free” components of $\mathbf { y }$ , with the other components of $\mathbf { y }$ determined by the boundary conditions. Alternatively, the components of $\mathbf { V }$ might parametrize the solutions that satisfy the starting boundary conditions in some other convenient way. Boundary conditions often impose algebraic relations among the $y _ { i }$ , rather than specific values for each of them. Using some auxiliary set of parameters often makes it easier to “solve” the boundary relations for a consistent set of $y _ { i }$ ’s. It makes no difference which way you go, as long as your vector space of $\mathbf { V }$ ’s generates (through 18.1.1) all allowed starting vectors $\mathbf { y }$ .

Given a particular $\mathbf { V }$ , a particular $\mathbf { y } ( x _ { 1 } )$ is thus generated. It can then be turned into a $\mathbf { y } ( x _ { 2 } )$ by integrating the ODEs to $x _ { 2 }$ as an initial value problem (e.g., using Chapter 17’s Odeint). Now, at $x _ { 2 }$ , let us define a discrepancy vector $\mathbf { F }$ , also of dimension $n _ { 2 }$ , whose components measure how far we are from satisfying the $n _ { 2 }$ boundary conditions at $x _ { 2 }$ (18.0.3). Simplest of all is just to use the right-hand sides of (18.0.3),

$$
F _ { k } = B _ { 2 k } ( x _ { 2 } , \mathbf { y } ) \qquad k = 0 , \ldots , n _ { 2 } - 1
$$

As in the case of $\mathbf { V }$ , however, you can use any other convenient parametrization, as long as your space of $\mathbf { F }$ ’s spans the space of possible discrepancies from the desired boundary conditions, with all components of $\mathbf { F }$ equal to zero if and only if the boundary conditions at $x _ { 2 }$ are satisfied. Below, you will be asked to supply a user-written function or functor that uses (18.0.3) to convert an $N$ -vector of ending values $\mathbf { y } ( x _ { 2 } )$ into an $n _ { 2 }$ -vector of discrepancies $\mathbf { F }$ . Inside Shoot, this function is called score.

Now, as far as Newton-Raphson is concerned, we are nearly in business. We want to find a vector value of $\mathbf { V }$ that zeros the vector value of $\mathbf { F }$ . We do this by invoking the globally convergent Newton’s method implemented in the routine newt of $\ S 9 . 7$ . Recall that the heart of Newton’s method involves solving the set of $n _ { 2 }$ linear equations

$$
\mathbf { J } \cdot \boldsymbol { \delta } \mathbf { V } = - \mathbf { F }
$$

and then adding the correction back,

$$
{ \bf V } ^ { \mathrm { n e w } } = { \bf V } ^ { \mathrm { o l d } } + \delta { \bf V }
$$

In (18.1.3), the Jacobian matrix $\mathbf { J }$ has components given by

$$
J _ { i j } = \frac { \partial F _ { i } } { \partial V _ { j } }
$$

It is not feasible to compute these partial derivatives analytically. Rather, each requires a separate integration of the $N$ ODEs, followed by the evaluation of

$$
\frac { \partial F _ { i } } { \partial V _ { j } } \approx \frac { F _ { i } ( V _ { 0 } , \dots , V _ { j } + \Delta V _ { j } , \dots ) - F _ { i } ( V _ { 0 } , \dots , V _ { j } , \dots ) } { \Delta V _ { j } }
$$

This is done automatically for you in the functor NRfdjac that comes with newt. The only input to newt that you have to provide is the routine vecfunc that calculates $\mathbf { F }$ by integrating the ODEs. Here is the appropriate routine, a functor called Shoot, that is to be passed as the actual argument in newt:

template <class L, class R, class S>   
struct Shoot {   
Functor for use with newt to solve a two-point boundary value problem by shooting. Int nvar; Number of coupled ODEs. Doub x1,x2; Start and end points. L &load; Supplies initial values for ODEs from $\mathtt { v } [ 0 \dots \mathrm { n } 2 \AA ^ { - 1 } ]$ . R &d; Supplies derivative information to the ODE integrator. S &score; Returns the n2 functions that ought to be zero to satisfy Doub atol,rtol; the boundary conditions at $\tt x 2$ . Doub h1,hmin; VecDoub y; Shoot(Int nvarr, Doub xx1, Doub xx2, L &loadd, R &dd, S &scoree) nvar(nvarr), x1(xx1), x2(xx2), load(loadd), d(dd), score(scoree), atol(1.0e-14), rtol(atol), hmin(0.0), y(nvar) {}

Routine for use with newt to solve a two-point boundary value problem for nvar coupled ODEs by shooting from x1 to $\tt x 2$ . Initial values for the nvar ODEs at x1 are generated from the n2 input coefficients v[0..n2-1], using the user-supplied routine load.

This is the functor used by newt. It integrates the ODEs to x2 using an eighth-order Runge-Kutta method with absolute and relative tolerances atol and rtol, initial stepsize h1, and minimum stepsize hmin. At $\mathbf { x } 2$ it calls the user-supplied routine score and returns the n2 functions that ought to be zero. newt uses a globally convergent Newton’s method to adjust the values of v until the returned functions are in fact zero.

$\mathtt { h 1 } = \left( \mathtt { x 2 } \mathtt { - x 1 } \right) / 1 0 0 \ldots 0 ;$ ; y=load(x1,v); Output out; No output generated by Odeint. Odeint<StepperDopr853<R> $>$ integ(y,x1,x2,atol,rtol,h1,hmin,out,d); integ.integrate(); return score(x2,y); } };

Note that Shoot is templated on the load, right-hand side for Odeint, and score routines. In practice, you will almost always want to write these as functors rather than functions. This makes communicating the various parameters in the problem easy — just pass them as parameters in the constructors.

For some problems the initial stepsize $\Delta V$ might depend sensitively upon the initial conditions. It is straightforward to alter load to compute a suggested stepsize h1 as a member variable and feed it fist to Shoot and hence to NRfdjac when the Shoot object is passed to newt.

A complete cycle of the shooting method thus requires $n _ { 2 } + 1$ integrations of the $N$ coupled ODEs: one integration to evaluate the current degree of mismatch, and $n _ { 2 }$ for the partial derivatives. Each new cycle requires a new round of $n _ { 2 } + 1$ integrations. This illustrates the enormous extra effort involved in solving two-point boundary value problems compared with initial value problems.

If the differential equations are linear, then only one complete cycle is required, since $( 1 8 . 1 . 3 ) - ( 1 8 . 1 . 4 )$ should take us right to the solution. A second round can be useful, however, in mopping up some (never all) of the roundoff error.

As given here, Shoot uses the high-efficiency eighth-order Runge-Kutta method of $\ S 1 7 . 2$ to integrate the ODEs, but any of the other methods of Chapter 17 could just as well be used.

You, the user, must supply Shoot with: (i) a function or functor load $( \mathbb { x } 1 , \mathbb { v } )$ that returns the n-vector $\mathtt { y } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ (satisfying the starting boundary conditions, of course), given the freely specifiable variables of $\mathtt { v } [ 0 \dots \mathrm { n } 2 \AA ^ { - 1 } ]$ at the initial point $\tt x 1$ ; (ii) a function or functor $\mathtt { s c o r e } ( \mathtt { x } 2 , \mathtt { y } )$ that returns the discrepancy vector $\mathtt { f } [ 0 \ldots$ $\mathtt { n } 2 \mathtt { - } 1 ]$ of the ending boundary conditions, given the vector $\mathtt { y } [ 0 \dots \underbrace { \mathtt { n } ^ { - 1 } } ]$ at the endpoint $_ { \tt X 2 }$ ; (iii) a starting vector $\mathtt { v } [ 0 \dots \mathrm { n } 2 \AA ^ { - 1 } ]$ ; (iv) a function or functor, called d in the routine, for the ODE integration; and other obvious parameters as described in the header comment above.

In $\ S 1 8 . 4$ we give a sample program illustrating how to use Shoot.

# CITED REFERENCES AND FURTHER READING:

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America).   
Keller, H.B. 1968, Numerical Methods for Two-Point Boundary-Value Problems; reprinted 1991 (New York: Dover).

# 18.2 Shooting to a Fitting Point

The shooting method described in $\ S 1 8 . 1$ tacitly assumed that the “shots” would be able to traverse the entire domain of integration, even at the early stages of convergence to a correct solution. In some problems it can happen that, for very wrong starting conditions, an initial solution can’t even get from $x _ { 1 }$ to $x _ { 2 }$ without encountering some incalculable, or catastrophic, result. For example, the argument of a square root might go negative, causing the numerical code to crash. Simple shooting would be stymied.

A different, but related, case is where the endpoints are both singular points of the set of ODEs. One frequently needs to use special methods to integrate near the singular points, analytic asymptotic expansions, for example. In such cases it is feasible to integrate in the direction away from a singular point, using the special method to get through the first little bit and then reading off “initial” values for further numerical integration. However, it is generally not feasible to integrate into a singular point. Usually the desired boundary condition is that one wants a regular solution at the singular point, but integrating into a singularity is guaranteed to pick out a singular solution, which by definition is growing as one integrates inward. Any small numerical inaccuracy will include some admixture of the “wrong” solution, which grows and swamps the desired solution.

The solution to the above-mentioned difficulties is shooting to a fitting point. Instead of integrating from $x _ { 1 }$ to $x _ { 2 }$ , we integrate first from $x _ { 1 }$ to some point $x _ { f }$ that is between $x _ { 1 }$ and $x _ { 2 }$ ; and second from $x _ { 2 }$ (in the opposite direction) to $x _ { f }$ .

If (as before) the number of boundary conditions imposed at $x _ { 1 }$ is $n _ { 1 }$ , and the number imposed at $x _ { 2 }$ is $n _ { 2 }$ , then there are $n _ { 2 }$ freely specifiable starting values at $x _ { 1 }$ and $n _ { 1 }$ freely specifiable starting values at $x _ { 2 }$ . (If you are confused by this, go back to $\ S 1 8 . 1 .$ .) We can therefore define an $n _ { 2 }$ -vector $\mathbf { V } ^ { ( 1 ) }$ of starting parameters at $x _ { 1 }$ and a prescription load1(x1,v1) for mapping $\mathbf { V } ^ { ( 1 ) }$ into a $\mathbf { y }$ that satisfies the boundary conditions at $x _ { 1 }$ :

$$
y _ { i } ( x _ { 1 } ) = y _ { i } ( x _ { 1 } ; V _ { 0 } ^ { ( 1 ) } , \ldots , V _ { n _ { 2 } - 1 } ^ { ( 1 ) } ) \qquad i = 0 , \ldots , N - 1
$$

Likewise we can define an $n _ { 1 }$ -vector $\mathbf { V } ^ { ( 2 ) }$ of starting parameters at $x _ { 2 }$ and a prescription load2 $( \mathtt { x } 2 , \mathtt { v } 2 )$ for mapping $\mathbf { V } ^ { ( 2 ) }$ into a $\mathbf { y }$ that satisfies the boundary conditions at $x _ { 2 }$ :

$$
y _ { i } ( x _ { 2 } ) = y _ { i } ( x _ { 2 } ; V _ { 0 } ^ { ( 2 ) } , \ldots , V _ { n _ { 1 } - 1 } ^ { ( 2 ) } ) \qquad i = 0 , \ldots , N - 1
$$

We thus have a total of $N$ freely adjustable parameters in the combination of V .1/ and V .2/. The N conditions that must be satisfied are that there be agreement in $N$ components of $\mathbf { y }$ at $x _ { f }$ between the values obtained integrating from one side and from the other,

$$
y _ { i } ( x _ { f } ; { \mathbf { V } } ^ { ( 1 ) } ) = y _ { i } ( x _ { f } ; { \mathbf { V } } ^ { ( 2 ) } ) \qquad i = 0 , \ldots , N - 1
$$

In some problems, the $N$ matching conditions can be better described (physically, mathematically, or numerically) by using $N$ different functions $F _ { i }$ ; $i = 0 \dots N - 1$ , each possibly depending on the $N$ components $y _ { i }$ . In those cases, (18.2.3) is replaced by

$$
F _ { i } [ { \bf y } ( x _ { f } ; { \bf V } ^ { ( 1 ) } ) ] = F _ { i } [ { \bf y } ( x _ { f } ; { \bf V } ^ { ( 2 ) } ) ] \qquad i = 0 , \dots , N - 1
$$

In the program below, a user-supplied function or functor, called score(xf,y) in the routine, is supposed to map an input $N$ -vector y into an output $N$ -vector F . In most cases, you can simply use the identity mapping $\mathbf { F } = \mathbf { y }$ .

Shooting to a fitting point uses globally convergent Newton-Raphson exactly as in $\ S 1 8 . 1$ . Comparing closely with the routine Shoot of the previous section, you should have no difficulty in understanding the following routine Shootf. The main differences in use are that you have to supply both load1 and load2. Also, in the calling program you must supply initial guesses for $\mathtt { v 1 } [ 0 \dots \mathrm { n 2 } \overline { { 2 } } \overline { { - 1 } } ]$ and $\mathtt { v } 2 [ 0 \dots \mathrm { n } 1 - 1 ]$ . Once again, a sample program illustrating shooting to a fitting point is given in $\ S 1 8 . 4$ .

template <class L1, class L2, class R, class S> struct Shootf {

Functor for use with newt to solve a two-point boundary value problem by shooting to a fitting point.

Int nvar,n2; nvar is the number of coupled ODEs.   
Doub x1,x2,xf; Start and end points and fitting point.   
L1 &load1; load1 and load2 supply initial values for the ODEs.   
L2 &load2;   
R &d; Supplies derivative information to the ODE integrator.   
S &score; Computes the mismatch of the solutions at the fitting   
Doub atol,rtol; point.   
Doub h1,hmin;   
VecDoub y,f1,f2;   
Shootf(Int nvarr, Int nn2, Doub xx1, Doub xx2, Doub xxf, L1 &loadd1, L2 &loadd2, R &dd, S &scoree) : nvar(nvarr), n2(nn2), x1(xx1), x2(xx2), xf(xxf), load1(loadd1), load2(loadd2), d(dd), score(scoree), atol(1.0e-14), rtol(atol), hmin(0.0), y(nvar), f1(nvar), f2(nvar) {}

Routine for use with newt to solve a two-point boundary value problem for nvar coupled ODEs by shooting from $\tt x 1$ and $\tt x 2$ to a fitting point xf. Initial values for the nvar ODEs at x1 are generated from the n2 coefficients v1 and the user-supplied routine load1. Likewise, those at $\tt x 2$ are from the n1=nvar-n2 coefficients v2, using load2. The coefficients v1 and v2 should be stored in a single array v[0..nvar-1] in the main program with v1 in $\mathtt { v } [ 0 \dots \mathrm { n } 2 \AA ^ { - 1 } ]$ and v2 in v[n2..nvar-1].

VecDoub operator() (VecDoub_I &v) {

This is the functor used by newt. It integrates the ODEs to xf using an eighth-order Runge-Kutta method with absolute and relative tolerances atol and rtol, initial stepsize h1, and minimum stepsize hmin. At xf it calls the user-supplied routine score to evaluate the nvar functions f1 and f2 that ought to match at xf. The differences are returned on output. newt uses a globally convergent Newton’s method to adjust the values of v until the differences are zero. A user-supplied function or functor d supplies derivative information to the ODE integrator (see Chapter 17).

VecDoub v2(nvar-n2,&v[n2]); h1=(x2-x1)/100.0; y=load1(x1,v); Path from x1 to xf with best trial values v1. Output out; No output generated by Odeint. Odeint<StepperDopr853<R> $>$ integ1(y,x1,xf,atol,rtol,h1,hmin,out,d); integ1.integrate(); f1=score(xf,y); y=load2(x2,v2); Path from x2 to xf with best trial values v2. Odeint<StepperDopr853<R> $>$ integ2(y,x2,xf,atol,rtol,h1,hmin,out,d); integ2.integrate(); f2=score(xf,y); for (Int $\scriptstyle \dot { 1 } = 0$ ;i<nvar;i++) f1[i] $- =$ f2[i]; return f1; } };

There are boundary value problems where even shooting to a fitting point fails — the integration interval has to be partitioned by several fitting points with the solution being matched at each such point. For more details see [1].

# CITED REFERENCES AND FURTHER READING:

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America).   
Keller, H.B. 1968, Numerical Methods for Two-Point Boundary-Value Problems; reprinted 1991 (New York: Dover).   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 7 . 3 . 5 - \ S 7 . 3 . 6 .$ [1]

# 18.3 Relaxation Methods

In relaxation methods we replace ODEs by approximate finite difference equations (FDEs) on a grid or mesh of points that spans the domain of interest. As a typical example, we could replace a general first-order differential equation

$$
{ \frac { d y } { d x } } = g ( x , y )
$$

with an algebraic equation relating function values at two points $k , k - 1$ :

$$
y _ { k } - y _ { k - 1 } - \left( x _ { k } - x _ { k - 1 } \right) g \left[ { \textstyle { \frac { 1 } { 2 } } } ( x _ { k } + x _ { k - 1 } ) , { \textstyle { \frac { 1 } { 2 } } } ( y _ { k } + y _ { k - 1 } ) \right] = 0
$$

The form of the FDE in (18.3.2) illustrates the idea, but not uniquely: There are many ways to turn the ODE into an FDE. When the problem involves $N$ coupled first-order ODEs represented by FDEs on a mesh of $M$ points, a solution consists of values for $N$ dependent functions given at each of the $M$ mesh points, or $N \times M$ variables in all. The relaxation method determines the solution by starting with a guess and improving it, iteratively. As the iterations improve the solution, the result is said to relax to the true solution.

While several iteration schemes are possible, for most problems our old standby, multidimensional Newton’s method, works well. The method produces a matrix equation that must be solved, but the matrix takes a special, “block diagonal” form that allows it to be inverted far more economically both in time and storage than would be possible for a general matrix of size $( M N ) \times ( M N )$ . Since $M N$ can easily be several thousand or more, this is crucial for the feasibility of the method.

Our implementation couples at most pairs of points, as in equation (18.3.2). More points can be coupled, but then the method becomes more complex. We will provide enough background so that you can write a more general scheme if you have the patience to do so.

Let us develop a general set of algebraic equations that represent the ODEs by FDEs. The ODE problem is exactly identical to that expressed in equations $( 1 8 . 0 . 1 ) - ( 1 8 . 0 . 3 )$ , where we had $N$ coupled first-order equations that satisfy $n _ { 1 }$ boundary conditions at one end of the interval and $n _ { 2 } = N - n _ { 1 }$ boundary conditions at the other. We first define a mesh or grid by a set of $k = 0 , 1 , . . . , M - 1$ points at which we supply values for the independent variable $x _ { k }$ . In particular, $x _ { 0 }$ is the initial boundary and $x _ { M - 1 }$ is the final boundary. We use the notation $\mathbf { y } _ { k }$ to refer to the entire set of dependent variables $y _ { 0 } , y _ { 1 } , \dots , y _ { N - 1 }$ at point $x _ { k }$ . At an arbitrary point $k$ in the middle of the mesh, we approximate the set of $N$ first-order ODEs by algebraic relations of the form

$$
0 = \mathbf { E } _ { k } \equiv \mathbf { y } _ { k } - \mathbf { y } _ { k - 1 } - ( x _ { k } - x _ { k - 1 } ) \mathbf { g } _ { k } ( x _ { k } , x _ { k - 1 } , \mathbf { y } _ { k } , \mathbf { y } _ { k - 1 } ) , k = 1 , 2 , \ldots , M - 1
$$

The notation signifies that $\mathbf { g } _ { k }$ can be evaluated using information from both points $k , k - 1$ The FDEs labeled by $\mathbf { E } _ { k }$ provide $N$ equations coupling $2 N$ variables at points $k , k - 1$ . There

are $M - 1$ points, $k = 1 , 2 , \ldots , M - 1$ , at which difference equations of the form (18.3.3) apply. Thus the FDEs provide a total of $( M - 1 ) N$ equations for the $M N$ unknowns. The remaining $N$ equations come from the boundary conditions.

At the first boundary we have

$$
0 = \mathbf { E } _ { 0 } \equiv \mathbf { B } ( x _ { 0 } , \mathbf { y } _ { 0 } )
$$

while at the second boundary

$$
0 = { \bf E } _ { M } \equiv { \bf C } ( x _ { M - 1 } , { \bf y } _ { M - 1 } )
$$

The vectors $\mathbf { E } _ { 0 }$ and $\mathbf { B }$ have only $n _ { 1 }$ nonzero components, corresponding to the $n _ { 1 }$ boundary conditions at $x _ { 0 }$ . It will turn out to be useful to take these nonzero components to be the last $n _ { 1 }$ components. In other words, $E _ { j , 0 } \neq 0$ only for $j ~ = ~ n _ { 2 } , n _ { 2 } + 1 , \ldots , N - 1$ . At the other boundary, only the first $n _ { 2 }$ components of $\mathbf { E } _ { M }$ and $\mathbf { C }$ are nonzero: $E _ { j , M } \neq 0$ only for $j = 0 , 1 , \ldots , n _ { 2 } - 1$ .

The “solution” of the FDE problem in $( 1 8 . 3 . 3 ) - ( 1 8 . 3 . 5 )$ consists of a set of variables $y _ { j , k }$ , the values of the $N$ variables $y _ { j }$ at the $M$ points $x _ { k }$ . The algorithm we describe below requires an initial guess for the $y _ { j , k }$ . We then determine increments $\Delta y _ { j , k }$ such that $y _ { j , k } +$ $\Delta y _ { j , k }$ is an improved approximation to the solution.

Equations for the increments are developed by expanding the FDEs in first-order Taylor series with respect to small changes $\Delta \mathbf { y } _ { k }$ . At an interior point, $k = 1 , 2 , \ldots , M - 1$ , this gives

$$
\mathbf { E } _ { k } ( \mathbf { y } _ { k } + \Delta \mathbf { y } _ { k } , \mathbf { y } _ { k - 1 } + \Delta \mathbf { y } _ { k - 1 } ) \approx \mathbf { E } _ { k } ( \mathbf { y } _ { k } , \mathbf { y } _ { k - 1 } ) + \sum _ { n = 0 } ^ { N - 1 } { \frac { \partial \mathbf { E } _ { k } } { \partial y _ { n , k - 1 } } } \Delta y _ { n , k - 1 } + \sum _ { n = 0 } ^ { N - 1 } { \frac { \partial \mathbf { E } _ { k } } { \partial y _ { n , k } } } \Delta y _ { n , k - 1 } .
$$

For a solution we want the updated value $\mathbf { E } ( \mathbf { y } + \Delta \mathbf { y } )$ to be zero, so the general set of equations at an interior point can be written in matrix form as

$$
\sum _ { n = 0 } ^ { N - 1 } S _ { j , n } \Delta y _ { n , k - 1 } + \sum _ { n = N } ^ { 2 N - 1 } S _ { j , n } \Delta y _ { n - N , k } = - E _ { j , k } , \quad j = 0 , 1 , \ldots , N - 1
$$

where

$$
S _ { j , n } = \frac { \partial E _ { j , k } } { \partial y _ { n , k - 1 } } , S _ { j , n + N } = \frac { \partial E _ { j , k } } { \partial y _ { n , k } } , n = 0 , 1 , \ldots , N - 1
$$

The quantity $S _ { j , n }$ is an $N \times 2 N$ matrix at each point $k$ . Each interior point thus supplies a block of $N$ equations coupling $2 N$ corrections to the solution variables at the points $k , k - 1$ .

Similarly, the algebraic relations at the boundaries can be expanded in a first-order Taylor series for increments that improve the solution. Since $\mathbf { E } _ { 0 }$ depends only on $\mathbf { y } _ { 0 }$ , we find at the first boundary

$$
\sum _ { n = 0 } ^ { N - 1 } S _ { j , n } \Delta y _ { n , 0 } = - E _ { j , 0 } , \quad j = n _ { 2 } , n _ { 2 } + 1 , \dots , N - 1
$$

where

$$
S _ { j , n } = \frac { \partial E _ { j , 0 } } { \partial y _ { n , 0 } } , \quad n = 0 , 1 , \ldots , N - 1
$$

At the second boundary,

$$
\sum _ { n = 0 } ^ { N - 1 } S _ { j , n } \Delta y _ { n , M - 1 } = - E _ { j , M } , \quad j = 0 , 1 , \ldots , n _ { 2 } - 1
$$

where

$$
S _ { j , n } = \frac { \partial E _ { j , M } } { \partial y _ { n , M - 1 } } , \quad n = 0 , 1 , \ldots , N - 1
$$

![](images/5412fcf8dff9c46c0b217aeb42c3ef963c305d76c6127bf6319c7b76b08b470f.jpg)  
Figure 18.3.1. Matrix structure of a set of linear finite difference equations (FDEs) with boundary conditions imposed at both endpoints. Here $\mathbf { X }$ represents a coefficient of the FDEs, V represents a component of the unknown solution vector, and B is a component of the known right-hand side. Empty spaces represent zeros. The matrix equation is to be solved by a special form of Gaussian elimination. (See text for details.)

We thus have in equations $( 1 8 . 3 . 7 ) - ( 1 8 . 3 . 1 2 )$ a set of linear equations to be solved for the corrections $\Delta \mathbf { y }$ , iterating until the corrections are sufficiently small. The equations have a special structure, because each $S _ { j , n }$ couples only points $k , k - 1$ . Figure 18.3.1 illustrates the typical structure of the complete matrix equation for the case of five variables and four mesh points, with three boundary conditions at the first boundary and two at the second. The $3 \times 5$ block of nonzero entries in the top left-hand corner of the matrix comes from the boundary condition $S _ { j , n }$ at point $k \ = \ 0$ . The next three $5 \times 1 0$ blocks are the $S _ { j , n }$ at the interior points, coupling variables at mesh points (2,1), (3,2), and (4,3). Finally we have the block corresponding to the second boundary condition.

We can solve equations $( 1 8 . 3 . 7 ) \mathrm { ~ - ~ } ( 1 8 . 3 . 1 2 )$ for the increments $\Delta \mathbf { y }$ using a form of Gaussian elimination that exploits the special structure of the matrix to minimize the total number of operations, and that minimizes storage of matrix coefficients by packing the elements in a special blocked structure. (You might wish to review Chapter 2, especially $\ S 2 . 2$ , if you are unfamiliar with the steps involved in Gaussian elimination.) Recall that Gaussian elimination consists of manipulating the equations by elementary operations such as dividing rows of coefficients by a common factor to produce unity in diagonal elements, and adding appropriate multiples of other rows to produce zeros below the diagonal. Here we take advantage of the block structure by performing a bit more reduction than in pure Gaussian elimination, so that the storage of coefficients is minimized. Figure 18.3.2 shows the form that we wish to achieve by elimination, just prior to the backsubstitution step. Only a small subset of the reduced $M N \times M N$ matrix elements needs to be stored as the elimination progresses. Once the matrix elements reach the stage in Figure 18.3.2, the solution follows quickly by a backsubstitution procedure.

Furthermore, the entire procedure, except the backsubstitution step, operates only on one block of the matrix at a time. The procedure contains four types of operations: (1) partial reduction to zero of certain elements of a block using results from a previous step; (2) elimination of the square structure of the remaining block elements such that the square section contains unity along the diagonal, and zero in off-diagonal elements; (3) storage of the

![](images/c7a59aa34bc9bec1338be88b6bd92855d84aa8fba30894ff6d2a560837a58fb7.jpg)  
Figure 18.3.2. Target structure of the Gaussian elimination. Once the matrix of Figure 18.3.1 has been reduced to this form, the solution follows quickly by backsubstitution.

$$
{ \begin{array} { r l } { ( { \mathrm { a } } ) ~ { \mathrm { ~ D ~ D ~ D ~ A ~ A ~ } } \qquad } & { { \mathrm { ~ V ~ } } \qquad { \mathrm { A } } } \\ { { \mathrm { ~ D ~ D ~ D ~ A ~ A ~ } } \qquad } & { { \mathrm { ~ V ~ } } \qquad { \mathrm { A } } } \\ { { \mathrm { ~ D ~ D ~ D ~ A ~ A ~ } } \qquad } & { { \mathrm { ~ V ~ } } \qquad { \mathrm { A } } } \\ { } & { { \mathrm { ~ V ~ } } \qquad { \mathrm { ~ A } } } \\ { ( { \mathrm { b } } ) ~ 1 ~ 0 ~ 0 ~ { \mathrm { ~ S ~ S ~ } } \qquad } & { { \mathrm { ~ V ~ } } \qquad { \mathrm { S } } } \\ { } & { { \mathrm { ~ 0 ~ 1 ~ 0 ~ S ~ S ~ } } \qquad { \mathrm { ~ V ~ } } \qquad { \mathrm { S } } } \\ { } & { { \mathrm { ~ 0 ~ 0 ~ 1 ~ 5 ~ S ~ } } \qquad { \mathrm { ~ V ~ } } \qquad { \mathrm { S } } } \end{array} }
$$

Figure 18.3.3. Reduction process for the first (upper-left) block of the matrix in Figure 18.3.1. (a) Original form of the block, (b) final form. (See text for explanation.)

remaining nonzero coefficients for use in later steps; and (4) backsubstitution. We illustrate the steps schematically by figures.

Consider the block of equations describing corrections available from the initial boundary conditions. We have $n _ { 1 }$ equations for $N$ unknown corrections. We wish to transform the first block so that its left-hand $n _ { 1 } \times n _ { 1 }$ square section becomes unity along the diagonal and zero in off-diagonal elements. Figure 18.3.3 shows the original and final forms of the first block of the matrix. In the figure we designate matrix elements that are subject to diagonalization by “D” and elements that will be altered by “A”; in the final block, elements that are stored are labeled by “S.” We get from start to finish by selecting in turn $n _ { 1 }$ “pivot” elements from among the first $n _ { 1 }$ columns, normalizing the pivot row so that the value of the “pivot” element is unity, and adding appropriate multiples of this row to the remaining rows so that they contain zeros in the pivot column. In its final form, the reduced block expresses values for the corrections to the first $n _ { 1 }$ variables at mesh point 0 in terms of values for the remaining $n _ { 2 }$ unknown corrections at point 0, i.e., we now know what the first $n _ { 1 }$ elements are in terms of the remaining $_ { n _ { 2 } }$ elements. We store only the final set of $_ { n _ { 2 } }$ nonzero columns from the initial block, plus the column for the altered right-hand side of the matrix equation.

We must emphasize here an important detail of the method. To exploit the reduced storage allowed by operating on blocks, it is essential that the ordering of columns in the s matrix of derivatives be such that pivot elements can be found among the first $n _ { 1 }$ rows of the matrix. This means that the $n _ { 1 }$ boundary conditions at the first point must contain some dependence on the first $\mathbf { j } { = } 0 , 1 , \ldots , { } n _ { 1 } - 1$ dependent variables, y[j][0]. If not, then the original square $n _ { 1 } \times n _ { 1 }$ subsection of the first block will appear to be singular, and the method will fail. Alternatively, we would have to allow the search for pivot elements to involve all $N$ columns of the block, and this would require column swapping and far more bookkeeping. The code provides a simple method of reordering the variables, i.e., the columns of the s matrix, so that this can be done easily. End of important detail.

![](images/c2f4c981a4b2d6e126f7e31f3f27ecfc940271c9320b144c1dc3a5453054b8a9.jpg)  
Figure 18.3.4. Reduction process for intermediate blocks of the matrix in Figure 18.3.1. (a) Original form, (b) final form. (See text for explanation.)

Next consider the block of $N$ equations representing the FDEs that describe the relation between the $2 N$ corrections at points 1 and 0. The elements of that block, together with results from the previous step, are illustrated in Figure 18.3.4. Note that by adding suitable multiples of rows from the first block we can reduce to zero the first $n _ { 1 }$ columns of the block (labeled by $\because \angle ^ { \dag }$ ), and, to do so, we will need to alter only the columns from $n _ { 1 }$ to $N - 1$ and the vector element on the right-hand side. Of the remaining columns we can diagonalize a square subsection of $N \times N$ elements, labeled by “D” in the figure. In the process we alter the final set of $n _ { 2 }$ columns, denoted “A” in the figure. The second half of the figure shows the block when we finish operating on it, with the stored $n _ { 2 } \times N$ elements labeled by “S.”

If we operate on the next set of equations corresponding to the FDEs coupling corrections at points 2 and 1, we see that the state of available results and new equations exactly reproduces the situation described in the previous paragraph. Thus, we can carry out those steps again for each block in turn through block $M - 1$ . Finally on block $M$ we encounter the remaining boundary conditions.

Figure 18.3.5 shows the final block of $n _ { 2 }$ FDEs relating the $N$ corrections for variables at mesh point $M - 1$ , together with the result of reducing the previous block. Again, we can first use the prior results to zero the first $n _ { 1 }$ columns of the block. Now, when we diagonalize the remaining square section, we strike gold: We get values for the final $n _ { 2 }$ corrections at mesh point $M - 1$ .

With the final block reduced, the matrix has the desired form shown previously in Figure 18.3.2, and the matrix is ripe for backsubstitution. Starting with the bottom row and working up toward the top, at each stage we can simply determine one unknown correction in terms of known quantities.

The object Solvde organizes the steps described above. The principal procedures used in the algorithm are performed by functions called internally by Solvde. The function red eliminates leading columns of the s matrix using results from prior blocks. pinvs diagonalizes the square subsection of s and stores unreduced coefficients. bksub carries out the backsubstitution step. The user of Solvde must understand the calling arguments, as described below, and supply an object Difeq, called by Solvde, with a method smatrix that evaluates the s matrix for each block.

![](images/f9500ac9b93850c6d4662973321d3941f92f02418834ac8dd69d87c47673a222.jpg)  
Figure 18.3.5. Reduction process for the last (lower-right) block of the matrix in Figure 18.3.1. (a) Original form, (b) final form. (See text for explanation.)

Most of the arguments in the constructor call to Solvde have already been described, but some require discussion. On input, array y[j][k] contains the initial guess for the solution, with $\dot { \mathsf { J } }$ labeling the dependent variables at mesh points $\mathtt { k }$ . The problem involves ne FDEs spanning points $\mathtt { k } = 0$ ,..., $\mathtt { m } - 1$ . nb boundary conditions apply at the first point $\mathtt { k } = 0$ . The array indexv[j] establishes the correspondence between columns of the s matrix; equations (18.3.8), (18.3.10), and (18.3.12); and the dependent variables. As described above, it is essential that the nb boundary conditions at $\mathtt { k } = 0$ involve the dependent variables referenced by the first nb columns of the s matrix. Thus, columns $\dot { ] }$ of the s matrix can be ordered by the user in Difeq to refer to derivatives with respect to the dependent variable indexv[j].

The function only attempts itmax correction cycles before returning, even if the solution has not converged. The parameters conv, slowc, and scalv relate to convergence. Each inversion of the matrix produces corrections for ne variables at m mesh points. We want these to become vanishingly small as the iterations proceed, but we must define a measure for the size of corrections. This error “norm” is very problem-specific, so the user might wish to rewrite this section of the code as appropriate. In the program below we compute a value for the average correction err by summing the absolute value of all corrections, weighted by a scale factor appropriate to each type of variable:

$$
\mathsf { e r r } = \frac { 1 } { \mathrm { m \times n e } } \sum _ { \mathrm { k } = 0 } ^ { \mathrm { m - 1 } } \sum _ { \mathrm { j } = 0 } ^ { \mathrm { n e - 1 } } \frac { \left| \Delta Y \left[ \mathrm { j } \right] \left[ \mathrm { k } \right] \right| } { \mathrm { s c a l v } \left[ \mathrm { j } \right] }
$$

When err $\leq$ conv, the method has converged. Note that the user gets to supply an array scalv that measures the typical size of each variable.

Obviously, if err is large, we are far from a solution, and perhaps it is a bad idea to believe that the corrections generated from a first-order Taylor series are accurate. The number slowc modulates the application of corrections. After each iteration we apply only a fraction of the corrections found by matrix inversion:

$$
Y [ \mathbf { j } ] [ \mathbf { k } ]  Y [ \mathbf { j } ] [ \mathbf { k } ] + \frac { \mathsf { s l o w c } } { \mathsf { m a x } ( \mathbf { s l o w c , e r r } ) } \Delta Y [ \mathbf { j } ] [ \mathbf { k } ]
$$

Thus, when ${ \tt e r r } >$ slowc only a fraction of the corrections are used, but when err $\leq$ slowc the entire correction gets applied.

As already mentioned, the constructor initializes the array $\mathtt { y } [ 0 \AA \cdot \cdot \mathrm { n e } \mathrm { - } 1 ] \ [ 0 \AA \cdot \cdot \mathrm { m } \mathrm { - } 1 ]$ in Solvde with the trial solution. Internally, workspace arrays $\mathsf { c } \left[ 0 \ldots \mathsf { n e } \mathrm { - 1 } \right] \left[ 0 \ldots \mathsf { n e } \mathrm { - n b } \right] \left[ 0 \ldots \mathsf { m } \right]$ , $\mathbf { s } \left[ 0 , . . \mathrm { n e } { - } 1 \right] \left[ 0 . . 2 \ast \mathrm { n e } \right]$ are allocated. The array $^ \texttt { c }$ is the blockbuster: It stores the unreduced elements of the matrix built up for the backsubstitution step. If there are m mesh points, then there will be $\mathtt { m } + 1$ blocks, each requiring ne rows and $\mathtt { n e - n b + 1 }$ columns. Although large, this is small compared with $( \mathtt { n e } \times \mathtt { m } ) ^ { 2 }$ elements required for the whole matrix if we did not break it into blocks.

We now describe the workings of the user-supplied object Difeq. The constructor can be used to pass problem-specific information from your main program. The object must contain a method smatrix with the following declaration:

void smatrix(const Int k, const Int k1, const Int k2, const Int jsf, const Int is1, const Int isf, VecInt_I &indexv, MatDoub_O &s, MatDoub_I &y);

As the declaration shows, the only information passed from Difeq to Solvde is the matrix of derivatives $\mathbf { s } \left[ 0 , . . \mathrm { n e } { - } 1 \right] \left[ 0 . . 2 \ast \mathrm { n e } \right]$ ; all other arguments are input to smatrix and should not be altered. k indicates the current mesh point, or block number. k1, k2 label the first and last points in the mesh. If $\mathrm { ~ \bf ~ k ~ } = \mathrm { ~ \bf ~ k 1 ~ }$ or $\texttt { k } > \texttt { k } 2$ , the block involves the boundary conditions at the first or final point; otherwise the block acts on FDEs coupling variables at points $\mathtt { k } { - } 1$ , k.

The convention on storing information into the array s[i][j] follows that used in equations (18.3.8), (18.3.10), and (18.3.12): Rows i label equations and columns $\dot { \mathsf { J } }$ refer to derivatives with respect to dependent variables in the solution. Recall that each equation will depend on the ne dependent variables at either one or two points. Thus, $\dot { ] }$ runs from 0 to either ne-1 or $2 { \ast } \mathtt { n e - 1 }$ . The column ordering for dependent variables at each point must agree with the list supplied in indexv[j]. Thus, for a block not at a boundary, the first column multiplies $\Delta Y ( \mathrm { 1 = i n d e x v } \left[ 0 \right] , \mathrm { k - 1 } )$ , and the column ne multiplies $\Delta Y ( \tt { 1 } \mathrm { { = } i n d e x v [ 0 ] , k ) }$ . The parameters is1, isf give the numbers of the starting and final rows that need to be filled in the s matrix for this block. jsf labels the column in which the difference equations $E _ { j , k }$ of equations $( 1 8 . 3 . 3 ) - ( 1 8 . 3 . 5 )$ are stored. Thus, s[i][jsf] is the vector on the right-hand side of the matrix. The reason for the minus sign is that smatrix supplies the actual difference equation, $E _ { j , k }$ , not its negative. Note that Solvde supplies a value for jsf such that the difference equation is put in the column just after all derivatives in the s matrix. Thus, smatrix expects to find values entered into s[i][j] for rows $\mathbf { i s } 1 \leq \mathbf { i } \leq$ isf and $0 \leq \mathrm { j } \leq \mathrm { j } \mathbf { s } \mathbf { f }$ .

Finally, the quantities $\mathbf { s } \left[ 0 . \mathbf { \nabla } . \mathtt { n s i - 1 } \right] \left[ 0 . \mathbf { \nabla } . \mathtt { n s j - 1 } \right]$ and $\mathtt { y } [ 0 \mathrm { . . n y j - 1 } ] [ 0 \mathrm { . . n y k - 1 } ]$ sup ply smatrix with storage for s and the values of the solution variables y for this iteration. An example of how to use this routine is given in the next section.

Detailed implementing code for Solvde is given in a Webnote [1], many ideas in which are due to Eggleton [2].

# 18.3.1 “Algebraically Difficult" Sets of Differential Equations

Relaxation methods allow you to take advantage of an additional opportunity that, while not obvious, can speed up some calculations enormously. It is not necessary that the set of variables $\underline { { y } } _ { j , k }$ correspond exactly with the dependent variables of the original differential equations. They can be related to those variables through algebraic equations. Obviously, it is necessary only that the solution variables allow us to evaluate the functions $y , g , \mathbf { B } , \mathbf { C }$ that are used to construct the FDEs from the ODEs. In some problems, $g$ depends on functions of $y$ that are known only implicitly, so that iterative solutions are necessary to evaluate functions in the ODEs. Often one can dispense with this “internal” nonlinear problem by defining a new set of variables from which both $y , g$ and the boundary conditions can be obtained directly. A typical example occurs in physical problems where the equations require the solution of a complex equation of state that can be expressed in more convenient terms using variables other than the original dependent variables in the ODE. While this approach is analogous to performing an analytic change of variables directly on the original ODEs, such an analytic transformation might be prohibitively complicated. The change of variables in the relaxation method is easy and requires no analytic manipulations.

# CITED REFERENCES AND FURTHER READING:

Numerical Recipes Software 2007, “Solvde Implementation,” Numerical Recipes Webnote No. 25, at http://www.nr.com/webnotes?25 [1]   
Eggleton, P.P. 1971, “The Evolution of Low Mass Stars,” Monthly Notices of the Royal Astronomical Society,vol. 151,pp.351-364.[2]   
Keller, H.B. 1968, Numerical Methods for Two-Point Boundary-Value Problems; reprinted 1991 (New York: Dover).   
Kippenhan, R., Weigert, A., and Hofmeister, E. 1968, in Methods in Computational Physics, vol. 7 (New York: Academic Press), pp. 129ff.

# 18.4 A Worked Example: Spheroidal Harmonics

The best way to understand the algorithms of the previous sections is to see them employed to solve an actual problem. As a sample problem, we have selected the computation of spheroidal harmonics. (The more common name is spheroidal angle functions, but we prefer the explicit reminder of the kinship with spherical harmonics.) We will show how to find spheroidal harmonics, first by the method of relaxation (-18.3), and then by the methods of shooting (-18.1) and shooting to a fitting point (-18.2).

Spheroidal harmonics typically arise when certain partial differential equations are solved by separation of variables in spheroidal coordinates. They satisfy the following differential equation on the interval $- 1 \leq x \leq 1$ :

$$
\frac { d } { d x } \left[ ( 1 - x ^ { 2 } ) \frac { d S } { d x } \right] + \left( \lambda - c ^ { 2 } x ^ { 2 } - \frac { m ^ { 2 } } { 1 - x ^ { 2 } } \right) S = 0
$$

Here $m$ is an integer, $c$ is the “oblateness parameter,” and $\lambda$ is the eigenvalue. Despite the notation, $c ^ { 2 }$ can be positive or negative. For $c ^ { 2 } > 0$ , the functions are called “prolate,” while if $c ^ { 2 } < 0$ they are called “oblate.” The equation has singular points at $x = \pm 1$ and is to be solved subject to the boundary conditions that the solution be regular at $x = \pm 1$ . Only for certain values of $\lambda$ , the eigenvalues, will this be possible.

If we consider first the spherical case, where $c \ = \ 0$ , we recognize the differential equation for Legendre functions $P _ { n } ^ { m } ( x )$ . In this case the eigenvalues are $\lambda _ { m n } = n ( n + 1 )$ , $n = m , m + 1 , \ldots$ The integer $n$ labels successive eigenvalues for fixed $m$ : When $n = m$ we have the lowest eigenvalue, and the corresponding eigenfunction has no nodes in the interval $- 1 < x < 1$ ; when $n = m + 1$ we have the next eigenvalue, and the eigenfunction has one node inside $( - 1 , 1 )$ ; and so on.

A similar situation holds for the general case $c ^ { 2 } \neq 0$ . We write the eigenvalues of (18.4.1) as $\lambda _ { m n } ( c )$ and the eigenfunctions as $S _ { m n } ( x ; c )$ . For fixed $m , n = m , m +$ $1 , \ldots$ labels the successive eigenvalues.

The computation of $\lambda _ { m n } ( c )$ and $S _ { m n } ( x ; c )$ traditionally has been quite difficult. Complicated recurrence relations, power series expansions, etc., can be found in [1-3]. Cheap computing makes evaluation by direct solution of the differential equation quite feasible.

The first step is to investigate the behavior of the solution near the singular points $x = \pm 1$ . Substituting a power series expansion of the form

$$
S = ( 1 \pm x ) ^ { \alpha } \sum _ { k = 0 } ^ { \infty } a _ { k } ( 1 \pm x ) ^ { k }
$$

in equation (18.4.1), we find that the regular solution has $\alpha = m / 2$ . (Without loss of generality we can take $m \geq 0$ since $m  - m$ is a symmetry of the equation.) We get an equation that is numerically more tractable if we factor out this behavior. Accordingly we set

$$
S = ( 1 - x ^ { 2 } ) ^ { m / 2 } y
$$

We then find from (18.4.1) that $y$ satisfies the equation

$$
( 1 - x ^ { 2 } ) { \frac { d ^ { 2 } y } { d x ^ { 2 } } } - 2 ( m + 1 ) x { \frac { d y } { d x } } + ( \mu - c ^ { 2 } x ^ { 2 } ) y = 0
$$

where

$$
\mu \equiv \lambda - m ( m + 1 )
$$

Both equations (18.4.1) and (18.4.4) are invariant under the replacement $x $ $- x$ . Thus the functions $S$ and $y$ must also be invariant, except possibly for an overall scale factor. (Since the equations are linear, a constant multiple of a solution is also a solution.) Because the solutions will be normalized, the scale factor can only be $\pm 1$ . If $n - m$ is odd, there are an odd number of zeros in the interval $( - 1 , 1 )$ . Thus we must choose the antisymmetric solution $y ( - x ) = - y ( x )$ , which has a zero at $x = 0$ . Conversely, if $n - m$ is even, we must have the symmetric solution. Thus

$$
y _ { m n } ( - x ) = ( - 1 ) ^ { n - m } y _ { m n } ( x )
$$

and similarly for $S _ { m n }$

The boundary conditions on (18.4.4) require that $y$ be regular at $x = \pm 1$ . In other words, near the endpoints the solution takes the form

$$
y = a _ { 0 } + a _ { 1 } ( 1 - x ^ { 2 } ) + a _ { 2 } ( 1 - x ^ { 2 } ) ^ { 2 } + \cdots
$$

Substituting this expansion in equation (18.4.4) and letting $x \to 1$ , we find that

$$
a _ { 1 } = - \frac { \mu - c ^ { 2 } } { 4 ( m + 1 ) } a _ { 0 }
$$

Equivalently,

$$
y ^ { \prime } ( 1 ) = \frac { \mu - c ^ { 2 } } { 2 ( m + 1 ) } y ( 1 )
$$

A similar equation holds at $x \ = \ - 1$ with a minus sign on the right-hand side. The irregular solution has a different relation between function and derivative at the endpoints.

Instead of integrating the equation from $^ { - 1 }$ to 1, we can exploit the symmetry (18.4.6) to integrate from 0 to 1. The boundary condition at $x = 0$ is

$$
\begin{array} { l l } { { y ( 0 ) = 0 , } } & { { n - m \mathrm { ~ o d d } } } \\ { { y ^ { \prime } ( 0 ) = 0 , } } & { { n - m \mathrm { ~ e v e n } } } \end{array}
$$

A third boundary condition comes from the fact that any constant multiple of a solution $y$ is a solution. We can thus normalize the solution. We adopt the normalization that the function $S _ { m n }$ has the same limiting behavior as $P _ { n } ^ { m }$ at $x = 1$ :

$$
\operatorname * { l i m } _ { x \to 1 } ( 1 - x ^ { 2 } ) ^ { - m / 2 } S _ { m n } ( x ; c ) = \operatorname * { l i m } _ { x \to 1 } ( 1 - x ^ { 2 } ) ^ { - m / 2 } P _ { n } ^ { m } ( x )
$$

Various normalization conventions in the literature are tabulated by Flammer [1].

Imposing three boundary conditions for the second-order equation (18.4.4) turns it into an eigenvalue problem for $\lambda$ or equivalently for $\mu$ . We write it in the standard form by setting

$$
\begin{array} { r } { y _ { 0 } = y } \\ { y _ { 1 } = y ^ { \prime } } \\ { y _ { 2 } = \mu } \end{array}
$$

Then

$$
\begin{array} { l } { { y _ { 0 } ^ { \prime } = y _ { 1 } } } \\ { { y _ { 1 } ^ { \prime } = \displaystyle \frac { 1 } { 1 - x ^ { 2 } } \left[ 2 x ( m + 1 ) y _ { 1 } - ( y _ { 2 } - c ^ { 2 } x ^ { 2 } ) y _ { 0 } \right] } } \\ { { y _ { 2 } ^ { \prime } = 0 } } \end{array}
$$

The boundary condition at $x = 0$ in this notation is

$$
\begin{array} { l l } { { y _ { 0 } = 0 , } } & { { n - m \mathrm { o d d } } } \\ { { y _ { 1 } = 0 , } } & { { n - m \mathrm { e v e n } } } \end{array}
$$

At $x = 1$ we have two conditions:

$$
\begin{array} { l } { \displaystyle { y _ { 1 } = \frac { y _ { 2 } - c ^ { 2 } } { 2 ( m + 1 ) } y _ { 0 } } } \\ { \displaystyle { y _ { 0 } = \operatorname* { l i m } _ { x \to 1 } ( 1 - x ^ { 2 } ) ^ { - m / 2 } P _ { n } ^ { m } ( x ) = \frac { ( - 1 ) ^ { m } ( n + m ) ! } { 2 ^ { m } m ! ( n - m ) ! } \equiv \gamma } } \end{array}
$$

We are now ready to illustrate the use of the methods of previous sections on this problem.

# 18.4.1 Relaxation

If we just want a few isolated values of $\lambda$ or $S$ , shooting is probably the quickest method. However, if we want values for a large sequence of values of $c$ , relaxation is better. Relaxation rewards a good initial guess with rapid convergence, and the previous solution should be a good initial guess if $c$ is changed only slightly.

For simplicity, we choose a uniform grid on the interval $0 \leq x \leq 1$ . For a total of $M$ mesh points, we have

$$
\begin{array} { l } { \displaystyle { h = \frac { 1 } { M - 1 } } } \\ { \displaystyle { x _ { k } = k h , \quad k = 0 , 1 , \ldots , M - 1 } } \end{array}
$$

At interior points $k = 1 , 2 , \ldots , M - 1$ , equation (18.4.15) gives

$$
E _ { 0 , k } = y _ { 0 , k } - y _ { 0 , k - 1 } - { \frac { h } { 2 } } ( y _ { 1 , k } + y _ { 1 , k - 1 } )
$$

Equation (18.4.16) gives

$$
\begin{array} { l } { E _ { 1 , k } = y _ { 1 , k } - y _ { 1 , k - 1 } - \beta _ { k } } \\ { \times \left[ \frac { ( x _ { k } + x _ { k - 1 } ) ( m + 1 ) ( y _ { 1 , k } + y _ { 1 , k - 1 } ) } { 2 } - \alpha _ { k } \frac { ( y _ { 0 , k } + y _ { 0 , k - 1 } ) } { 2 } \right] } \end{array}
$$

where

$$
\begin{array} { l } { \displaystyle \alpha _ { k } = \frac { y _ { 2 , k } + y _ { 2 , k - 1 } } { 2 } - \frac { c ^ { 2 } ( x _ { k } + x _ { k - 1 } ) ^ { 2 } } { 4 } } \\ { \displaystyle \beta _ { k } = \frac { h } { 1 - \frac { 1 } { 4 } ( x _ { k } + x _ { k - 1 } ) ^ { 2 } } } \end{array}
$$

Finally, equation (18.4.17) gives

$$
E _ { 2 , k } = y _ { 2 , k } - y _ { 2 , k - 1 }
$$

Now recall that the matrix of partial derivatives $S _ { i , j }$ of equation (18.3.8) is defined so that $i$ labels the equation and $j$ the variable. In our case, $j$ runs from 0 to 2 for $y _ { j }$ at $k - 1$ and from 3 to 5 for $y _ { j }$ at $k$ . Thus equation (18.4.23) gives

$$
\begin{array} { l l l } { { S _ { 0 , 0 } = - 1 , \quad } } & { { S _ { 0 , 1 } = - \displaystyle \frac { h } { 2 } , \quad } } & { { S _ { 0 , 2 } = 0 } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { S _ { 0 , 3 } = 1 , \quad \quad S _ { 0 , 4 } = - \displaystyle \frac { h } { 2 } , \quad \quad S _ { 0 , 5 } = 0 } } \end{array}
$$

Similarly equation (18.4.24) yields

$$
\begin{array} { l l } { { S _ { 1 , 0 } = \alpha _ { k } \beta _ { k } / 2 , ~ } } & { { S _ { 1 , 1 } = - 1 - \beta _ { k } ( x _ { k } + x _ { k - 1 } ) ( m + 1 ) / 2 , } } \\ { { S _ { 1 , 2 } = \beta _ { k } ( y _ { 0 , k } + y _ { 0 , k - 1 } ) / 4 , ~ } } & { { S _ { 1 , 3 } = S _ { 1 , 0 } , } } \\ { { S _ { 1 , 4 } = 2 + S _ { 1 , 1 } , ~ } } & { { S _ { 1 , 5 } = S _ { 1 , 2 } } } \end{array}
$$

while from equation (18.4.27) we find

$$
\begin{array} { l l } { { S _ { 2 , 0 } = 0 , \quad } } & { { S _ { 2 , 1 } = 0 , \quad \quad S _ { 2 , 2 } = - 1 } } \\ { { S _ { 2 , 3 } = 0 , \quad } } & { { S _ { 2 , 4 } = 0 , \quad \quad S _ { 2 , 5 } = 1 } } \end{array}
$$

At $x = 0$ we have the boundary condition

$$
E _ { 2 , 0 } = \left\{ { { y _ { 0 , 0 } } , \begin{array} { l l } { { n - m \mathrm { { \ o d d } } } } \\ { { { y _ { 1 , 0 } } , } } \end{array} } \right.
$$

Recall the convention adopted in the solvde routine that for one boundary condition at $k = 0$ only $S _ { 2 , j }$ can be nonzero. Also, $j$ takes on the values 3 to 5 since the boundary condition involves only $y _ { k }$ , not $y _ { k - 1 }$ . Accordingly, the only nonzero values of $S _ { 2 , j }$ at $x = 0$ are

$$
\begin{array} { l l } { { S _ { 2 , 3 } = 1 , \quad } } & { { n - m \mathrm { ~ o d d } } } \\ { { S _ { 2 , 4 } = 1 , \quad } } & { { n - m \mathrm { ~ e v e n } } } \end{array}
$$

At $x = 1$ we have

$$
\begin{array} { l l } { { E _ { 0 , M } = y _ { 1 , M - 1 } - \displaystyle \frac { y _ { 2 , M - 1 } - c ^ { 2 } } { 2 ( m + 1 ) } y _ { 0 , M - 1 } } } \\ { { E _ { 1 , M } = y _ { 0 , M - 1 } - \gamma } } \end{array}
$$

Thus

$$
\begin{array} { l l l } { { S _ { 0 , 3 } = - { \frac { y _ { 2 , M - 1 } - c ^ { 2 } } { 2 ( m + 1 ) } } , \quad } } & { { S _ { 0 , 4 } = 1 , \quad } } & { { S _ { 0 , 5 } = - { \frac { y _ { 0 , M - 1 } } { 2 ( m + 1 ) } } } } \\ { { S _ { 1 , 3 } = 1 , \quad } } & { { S _ { 1 , 4 } = 0 , \quad } } & { { S _ { 1 , 5 } = 0 } } \end{array}
$$

Here now is the sample program that implements the above algorithm. We need a main program, sfroid, that calls the routine Solvde, and we must supply the object Difeq to be passed to Solvde. For simplicity we choose an equally spaced mesh of $\mathtt { m } = 4 1$ points, that is, $h = . 0 2 5$ . As we shall see, this gives good accuracy for the eigenvalues up to moderate values of $n - m$ .

Since the boundary condition at $x = 0$ does not involve $y _ { 0 }$ if $n - m$ is even, we have to use the indexv feature of Solvde. Recall that the value of indexv[j] describes which column of s[i][j] the variable y[j] has been put in. If $n - m$ is even, we need to interchange the columns for $y _ { 0 }$ and $y _ { 1 }$ so that there is not a zero pivot element in s[i][j].

The program prompts for values of $m$ and $n$ . It then computes an initial guess for $y$ based on the Legendre function $P _ { n } ^ { m }$ . It next prompts for $c ^ { 2 }$ , solves for $y$ , prompts for $c ^ { 2 }$ , solves for $y$ using the previous values as an initial guess, and so on.

Int main_sfroid(void)   
Sample program using Solvde. Computes eigenvalues of spheroidal harmonics $S _ { m n } ( x ; c )$ for $m \geq 0$ and $n \geq m$ . In the program, $m$ is mm, ${ \overset { \smile } { c } } ^ { 2 }$ is $^ { c 2 }$ , and $\gamma$ of equation (18.4.20) is anorm. {   
const Int M=40,MM=4;   
const Int NE=3,NB $\scriptstyle = 1$ ,NYJ $\mathop { : = }$ NE,NYK=M+1;   
Int mm=3, $_ { \mathrm { 2 } } = 5$ ,mpt=M+1;   
VecInt indexv(NE);   
VecDoub x(M+1),scalv(NE);   
MatDoub y(NYJ,NYK);   
Int itmax $\mathtt { \Pi } = 1 0 0$ ;   
Doub c2[] $=$ {16.0,20.0,-16.0,-20.0};   
Doub conv $= 1$ .0e-14,slowc $= 1$ .0, $\scriptstyle 1 = 1$ .0/M;   
if ((n+mm & 1) $\ ! = \ 0$ ) { No interchanges necessary. indexv[0] ${ = } 0$ ; indexv[1] $= 1$ ; indexv[2] $^ { = 2 }$ ;   
} else { Interchange $y _ { 0 }$ and $y _ { 1 }$ . indexv[0] $= 1$ ; indexv[1] ${ = } 0$ ; indexv[2] $^ { = 2 }$ ;   
1   
Doub anorm $^ { = 1 }$ .0; Compute .   
if (mm $\ ! = \ 0$ ) { Doub $\mathtt { q 1 } = \mathtt { n }$ ; for (Int $\bf { i } \mathrm { = } 1 ; \bf { i } \mathrm { < = } \mathrm { m m ; \bf { i } \mathrm { + + } } ) ~ \mathrm { a n o r m ~ \bf { = ~ } } - 0 . 5 \mathrm { * } \mathrm { a n o r m * ( n \mathrm { + + } ) * ( q 1 \mathrm { - - } / \bf { i } ) ; }$   
for (Int $\mathtt { k } = 0$ ;k<M;k++) { Initial guess. x[k] $=$ k\*h; Doub fac $_ { \lfloor = 1 }$ .0-x[k] $^ { * \mathrm { x } }$ [k]; Doub fac2 $: = .$ exp((-mm/2.0)\*log(fac1));

y[0][k] $=$ plgndr(n,mm,x[k])\*fac2; $P _ { n } ^ { m }$ from $\ S 6 . 7$ . Doub deriv = -((n-mm+1)\*plgndr $( \mathtt { n } + 1$ n ,mm,x[k])- Derivative of $P _ { n } ^ { m }$ from a recur-$( \mathtt { n } + 1 ) * \mathtt { x }$ [k]\*plgndr(n,mm,x[k]))/fac1; rence relation. y[1][k]=mm\*x[k]\*y[0][k]/fac1+deriv\*fac2; y[2][k] ${ \bf \delta } = { \bf n } { * } \left( { \bf n } { + } 1 \right) { \bf - } { \bf n } { \bf m } { * } \left( { \bf { \bar { \ n } } } { \bf m } { + } 1 \right)$ ; } x[M] $= 1$ .0; Initial guess at $x = 1$ done sepy[0][M] $=$ anorm; arately. y[2][M] ${ \bf \delta } = { \bf n } { * } \left( { \bf n } { + } 1 \right) { \bf - m m } { * } \left( { \bf m m } { + } 1 \right)$ ; y[1][M] $=$ y[2][M]\*y[0][M]/(2.0\*(mm+1.0)); scalv[0] $=$ abs(anorm); Set scaling. scalv[1] $=$ (y[1][M] $>$ scalv[0] ? y[1][M] : scalv[0]); scalv[2] $=$ (y[2][M] $>$ 1.0 ? y[2][M] : 1.0); for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<MM;j $^ { + + }$ ) { Difeq difeq(mm,n,mpt,h,c2[j],anorm,x); Set up Difeq object. Solvde solvde(itmax,conv,slowc,scalv,indexv,NB,y,difeq); cout $< <$ endl $< < \mathrm { ~ " ~ } \mathrm { ~ m ~ } = \mathrm { ~ " ~ } < <$ setw(3) $< <$ mm; cout << " $\mathrm { ~ \tt ~ n ~ } = \mathrm { ~ \tt ~ n ~ } < <$ setw(3) << n << " c\*\*2 = "; cout $< <$ fixed $< <$ setprecision(3) $< <$ setw(7) << c2[j]; cout << " lamda $=$ " << setprecision(6) $< <$ (y[2][0] $\scriptstyle + \operatorname* { m m } + \left( \mathrm { m m } + 1 \right) .$ ); cout $< <$ endl; Return for another value of $c ^ { 2 }$ . } return 0;

# struct Difeq {

Provides matrix s for Solvde.

const Int &mm,&n,&mpt; These variables are defined in sfroid.   
const Doub &h,&c2,&anorm;   
const VecDoub &x;   
Difeq(const Int &mmm, const Int &nn, const Int &mptt, const Doub &hh, const Doub &cc2, const Doub &anormm, VecDoub_I &xx) : mm(mmm), n(nn), mpt(mptt), h(hh), c2(cc2), anorm(anormm), x(xx) {}   
void smatrix(const Int k, const Int k1, const Int k2, const Int jsf, const Int is1, const Int isf, VecInt_I &indexv, MatDoub_O &s, MatDoub_I &y)   
Returns matrix s for solvde.   
{

Doub temp,temp1,temp2;

if $( \mathrm { ~ k ~ } = = \mathrm { ~ k ~ 1 ~ }$ ) { Boundary condition at first point.if ((n+mm & 1) $\smash { \ ! = \ 0 }$ ) {s[2][3+indexv[0]] $= 1$ .0; Equation (18.4.32).s[2][3+indexv[1]]=0.0;s[2][3+indexv[2]]=0.0;s[2][jsf]=y[0][0]; Equation (18.4.31).} else {s[2][3+indexv[0]] ${ = } 0$ .0; Equation (18.4.32).s[2][3+indexv[1]] ${ = } 1$ .0;s[2][3+indexv[2]]=0.0;s[2][jsf]=y[1][0]; Equation (18.4.31).}  
} else if (k > k2-1) { Boundary conditions at last point.s[0][3+indexv[0]] $=$ -(y[2][mpt-1]-c2)/(2.0\*(mm+1.0)); (18.4.35).s[0][3+indexv[1]] ${ = } 1$ .0;s[0][3+indexv[2]] $=$ -y[0][mpt-1]/(2. $^ { 0 * }$ (mm+1.0));s[0][jsf]=y[1][mpt-1]-(y[2][mpt-1]-c2)\*y[0][mpt-1]/ (18.4.33).(2.0\*(mm+1.0));s[1][3+indexv[0]] $= 1$ .0; Equation (18.4.36).s[1][3+indexv[1]]=0.0;s[1][3+indexv[2]] ${ = } 0$ .0;

s[1][jsf]=y[0][mpt-1]-anorm; Equation (18.4.34).} else { Interior point.s[0][indexv[0]] $= - 1 . 0$ ; Equation (18.4.28).s[0][indexv[1]] $=$ -0.5\*h;s[0][indexv[2]]=0.0;s[0][3+indexv[0]] $^ { = 1 }$ .0;s[0][3+indexv[1]] = -0.5\*h;s[0][3+indexv[2]]=0.0;temp1 $= \mathbf { x }$ [k] $+ \mathbf { x }$ [k-1];temp=h/(1.0-temp1\*temp1\*0.25);temp $_ { 2 = 0 }$ .5\*(y[2][k]+y[2][k-1])-c2\*0.25\*temp1\*temp1;s[1][indexv[0]] $=$ temp\*temp2 $^ { * 0 }$ .5; Equation (18.4.29).s[1][indexv[1]] $=$ -1.0-0.5\*temp\*(mm+1.0)\*temp1;s[1][indexv[2]] ${ = } 0$ .25\*temp\*(y[0][k]+y[0][k-1]);s[1][3+indexv[0]] $= \tt s$ [1][indexv[0]];s[1][3+indexv[1]] $^ { = 2 }$ . $0 + \tt s$ [1][indexv[1]];s[1][3+indexv[2]] $= \tt s$ [1][indexv[2]];s[2][indexv[0]] ${ = } 0$ .0; Equation (18.4.30).s[2][indexv[1]] ${ = } 0$ .0;s[2][indexv[2]] $=$ -1.0;s[2][3+indexv[0]]=0.0;s[2][3+indexv[1]] ${ = } 0$ .0;s[2][3+indexv[2]] $= 1$ .0;s[0][jsf]=y[0][k]-y[0][k-1]-0.5\*h\*(y[1][k]+y[1][k-1]); (18.4.s[1][jsf]=y[1][k]-y[1][k-1]-temp\*((x[k]+x[k-1]) (18.4.\*0.5\*(mm+1.0)\*(y[1][k]+y[1][k-1])-temp2$* 0 \AA . 5 *$ (y[0][k]+y[0][k-1]));s[2][jsf]=y[2][k]-y[2][k-1]; Equation (18.4.27).}};

You can run the program and check it against values of $\lambda _ { m n } ( c )$ given in the tables at the back of Flammer’s book [1] or in Table 21.1 of Abramowitz and Stegun [2]. Typically it converges in about three iterations. The table below gives a few comparisons.

<table><tr><td colspan="4">Selected Output of sfroid</td></tr><tr><td>m</td><td>c2 n</td><td>2exact</td><td>λsfroid</td></tr><tr><td>2</td><td>2</td><td>0.1 6.01427 1.0 6.14095</td><td>6.01427 6.14095</td></tr><tr><td rowspan="3">2</td><td>5</td><td>4.0 6.54250</td><td>6.54253</td></tr><tr><td>1.0</td><td>30.4361</td><td>30.4372</td></tr><tr><td>16.0</td><td>36.9963</td><td>37.0135</td></tr><tr><td>4</td><td>11 -1.0</td><td>131.560</td><td>131.554</td></tr></table>

# 18.4.2 Shooting

To solve the same problem via shooting (-18.1), we supply a functor Rhs that implements equations $( 1 8 . 4 . 1 5 ) - ( 1 8 . 4 . 1 7 )$ . We will integrate the equations over the range $- 1 \leq x \leq 0$ . We provide the functor Load, which sets the eigenvalue $y _ { 2 }$ to its current best estimate, $\tt V [ 0 ]$ . It also sets the boundary values of $y _ { 0 }$ and $y _ { 1 }$ using equations (18.4.20) and (18.4.19) (with a minus sign corresponding to $x \ = \ - 1$ ). Note that the boundary condition is actually applied a distance dx from the boundary to avoid having to evaluate $y _ { 1 } ^ { \prime }$ right on the boundary. The functor Score follows from equation (18.4.18).

# struct Rhs {

Evaluates derivatives for Odeint. Int m; Doub c2; Rhs(Int mm, Doub cc2) : m(mm), c2(cc2) {} Constructor gets parameters from main. void operator() (const Doub x, VecDoub_I &y, VecDoub_O &dydx) { dydx[0]=y[1]; dydx[1] $=$ (2.0\*x\*(m+1.0)\*y[1]-(y[2]-c2\*x\*x)\*y[0])/(1.0-x\*x); dydx[2] $= 0 . 0$ ; }   
};

# struct Load {

Supplies starting values for integration at $x = - 1 + d x$ . Int n,m; Doub gmma,c2,dx; VecDoub y; Load(Int nn, Int mm, Doub gmmaa, Doub cc2, Doub dxx) : n(nn), m(mm), gmma(gmmaa), c2(cc2), dx(dxx), y(3) {} Constructor gets parameters from main. VecDoub operator() (const Doub x1, VecDoub_I &v) { Doub $\ y 1 ~ = ~ ( ~ ( \mathtt { n } \mathrm { - m } ~ \& ~ 1 ) ~ : = ~ 0 ~ ? ~ \mathrm { - g m m a ~ : ~ \ g m m a ) ~ } ;$ y[2] $= \tt v$ [0]; $\begin{array} { r } { \texttt { y } [ 1 ] ~ = ~ - \left( \texttt { y } [ 2 ] - \texttt c 2 \right) * \texttt { y } 1 / \left( 2 * \left( \texttt m + 1 \right) \right) ; } \end{array}$ $\mathtt { y } [ 0 ] = \mathtt { y } 1 + \mathtt { y } [ 1 ] * \mathrm { d } \mathtt { x } ;$ ; return y; }   
};   
struct Score {   
Computes amount by which boundary condition at $x = 0$ is violated. Int n,m; VecDoub f; Score(Int nn, Int mm) : n(nn), m(mm), f(1) {} Constructor gets parameters from main. VecDoub operator() (const Doub xf, VecDoub_I &y) { $\mathbf { f } \ [ 0 ] = \left( \ ( \mathbf { n } - \mathbf { m } \& \ \mathbf { 1 } ) \quad : = \ 0 \ \ ? \ \mathbf { y } \ [ 0 ] \ \ : \ \mathbf { y } \ [ 1 ] \ \right)$ ; return f; }   
};   
Int main_sphoot(void) {   
Sample program using Shoot. Computes eigenvalues of spheroidal harmonics $S _ { m n } ( x ; c )$ for   
$m \geq 0$ and $n \geq m$ . Note how the functor vecfunc for newt is provided by Shoot (-18.1). const Int $ \mathbb { N } 2 { = } 1 , \mathbb { M } \mathbb { M } { = } 3$ ; Bool check; VecDoub $\mathrm { v }$ (N2); Int j, $^ { \mathrm { m = 3 } , \mathrm { n = 5 } }$ ; Doub ${ \mathsf { c } } 2 \left[ { \mathsf { 1 } } = \left\{ 1 . 5 , - 1 . 5 , 0 . 0 \right\} \right.$ ; Int nvar $\scriptstyle = 3$ ; Number of equations. Doub d $\tt c { = } 1$ .0e-8; Avoid evaluating derivatives exactly at $x = - 1$ . for $\scriptstyle ( j = 0$ ;j<MM; ${ \dot { \mathsf { J } } } ^ { + + }$ ) { Doub gmma $^ { = 1 }$ .0; Compute $\gamma$ of equation (18.4.20). Doub $\mathtt { q 1 } = \mathtt { n }$ ; for (Int $\mathbf { i } { = } 1 \ ; \mathbf { i } < = \mathrm { I m } \ ; \mathbf { i } { + } { + } ) \quad \mathrm { g m m a } \quad { \ast } { = } \ - 0 \ . 5 { * } \left( \mathrm { n { + } i } \right) { * } \left( \mathrm { q } 1 { - } { - } / \mathbf { i } \right)$ ; $\mathrm { v } \left[ 0 \right] = \mathrm { n } { * \left( \mathrm { n } { + } 1 \right) } - \mathrm { m } { * \left( \mathrm { m } { + } 1 \right) } + \mathrm { c } 2 \left[ \mathrm { j } \right] / 2 . \mathrm { 0 } \mathrm { ~ }$ ; Initial guess for eigenvalue.

Doub x1= -1.0+dx; Set range of integration. Doub $\mathtt { x 2 = 0 , 0 }$ ; Load load(n,m,gmma,c2[j],dx); Set up Load, Rhs, and Score objects ... Rhs d(m,c2[j]); Score score(n,m); .. use them to set up Shoot object ... Shoot<Load,Rhs,Score> shoot(nvar,x1,x2,load,d,score); newt(v,check,shoot); ... and use it to find v that zeros vector f in if (check) { Score. cout << "shoot failed; bad initial guess" << endl; } else { cout << " " << "mu(m,n)" << endl; cout $< <$ fixed $< <$ setprecision(6); cout << setw(12) << v[0] << endl; } return 0;

# 18.4.3 Shooting to a Fitting Point

For variety we illustrate Shootf from $\ S 1 8 . 2$ by integrating over the whole range $- 1 + d x \leq x \leq 1 - d x$ , with the fitting point chosen to be at $x = 0$ . The routine Rhsfpt is identical to Rhs for Shoot since we are integrating the same equation. Now, however, there are two load routines. The functor Load1 for $x = - 1$ is essentially identical to Load above. At $x = 1$ , Load2 sets the function value $y _ { 0 }$ and the eigenvalue $y _ { 2 }$ to their best current estimates, $\tt v 2 [ 0 ]$ and v2[1], respectively. If you quite sensibly make your initial guess of the eigenvalue the same in the two intervals, then v1[0] will stay equal to v2[1] during the iteration. The functor Score computes the degree of mismatch of the three function values at the fitting point.

struct Rhsfpt { Int m; Doub c2; Rhsfpt(Int mm, Doub cc2) : m(mm), c2(cc2) {} void operator() (const Doub x, VecDoub_I &y, VecDoub_O &dydx) { dydx[0] $\mathbf { \mu } = \mathbf { y }$ [1]; dydx[1] $=$ (2.0\*x\*(m+1.0)\*y[1]-(y[2]-c2\*x\*x)\*y[0])/(1.0-x\*x); dydx[2] $= 0 . 0$ ; }   
};

# struct Load1 {

Supplies starting values for integration at $x = - 1 + d x$ . Int n,m; Doub gmma,c2,dx; VecDoub y; Load1(Int nn, Int mm, Doub gmmaa, Doub cc2, Doub dxx) : n(nn), m(mm), gmma(gmmaa), c2(cc2), dx(dxx), y(3) {} VecDoub operator() (const Doub x1, VecDoub_I &v1) { Doub $\begin{array} { r } { \mathrm { y 1 ~ = ~ ( ( n - m ~ \& ~ 1 ) ~ \theta 1 = ~ 0 ~ \theta ? - g m m a ~ : ~ \ g m m a ) ~ ; } } \end{array}$ y[2]=v1[0]; $\begin{array} { r } { \mathbb { y } \left[ 1 \right] ~ = ~ - \left( \mathbb { y } \left[ 2 \right] - \mathtt { c } 2 \right) { * \mathrm { y } 1 } / \left( 2 * \left( \mathtt { m } + 1 \right) \right) ; } \end{array}$ y[0]=y1+y[1]\*dx; return y; }   
};

# struct Load2 {

Supplies starting values for integration at $x = 1 - d x$ . Int m; Doub c2; VecDoub y; Load2(Int mm, Doub cc2) : m(mm), c2(cc2), y(3) {} VecDoub operator() (const Doub x2, VecDoub_I &v2) { y[2] $=$ v2[1]; y[0] $=$ v2[0]; y[1] $=$ (y[2]-c2)\*y[0]/(2\*(m+1)); return y; }   
};   
struct Score {   
Computes the mismatch of the solutions at the fitting point $x = 0$ . VecDoub f; Score() : f(3) {} VecDoub operator() (const Doub xf, VecDoub_I &y) { for (Int i=0;i<3;i++) f[i]=y[i]; return f; }   
};

# Int main_sphfpt(void) {

Sample program using Shootf. Computes eigenvalues of spheroidal harmonics $S _ { m n } ( x ; c )$ for $m \geq 0$ and $n \geq m$ . Note how the functor vecfunc for newt is provided by Shootf $( \ S 1 8 . 2 )$ . The routine Rhsfpt is the same as Rhs for sphoot.

const Int $\mathbb { N } 1 = 2$ ,N2=1,NTOT $\mathop {  }$ N1+N2,MM=3;   
Bool check;   
VecDoub $\mathtt { v }$ (NTOT);   
Int j, $\mathrm { m } = 3$ , $\mathtt { n } = 5$ , $\scriptstyle \mathtt { n 2 } = \mathtt { N 2 }$ ;   
Doub c2[] $=$ {1.5,-1.5,0.0};   
Int nvar $^ { * = }$ NTOT; Number of equations.   
Doub $\mathtt { d x } { = } 1$ .0e-8; Avoid evaluating derivatives exactly at $x = \pm 1$ .   
for $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<MM; $\mathrm { j } + +$ ) { Doub gmma $^ { = 1 }$ .0; Compute $\gamma$ of equation (18.4.20). Doub $\mathtt { q 1 } = \mathtt { n }$ ; for (In $\mathbf { \partial } ; \mathbf { i } = 1 ; \mathbf { i } < = \mathrm { I m } ; \mathbf { i } + + ) \mathbf { \partial } \operatorname { g m m } { \mathbf { a } } * = \mathbf { \partial } - 0 . 5 * ( \mathrm { n + i } ) * ( \mathrm { q } 1 \mathrm { -- } / \mathbf { i } )$ ; $\mathrm { v } \left[ 0 \right] = \mathrm { n } { \ast } \left( \mathrm { n } { + } 1 \right) { - } \mathrm { m } { \ast } \left( \mathrm { m } { + } 1 \right) { + } \mathrm { c } 2 \left[ { \bf j } \right] / 2 . 0 ;$ Initial guess for eigenvalue and function value. v[2]=v[0]; $\mathrm { ~ v ~ } [ 1 ] = \mathrm { g m m a } \ast \left( 1 . 0 - \left( \mathrm { v } \left[ 2 \right] - \mathrm { c } 2 \left[ \mathrm { j } \right] \right) \ast \mathrm { d } \mathrm { x } / \left( 2 \ast \left( \mathrm { m } + 1 \right) \right) \right) ;$ Doub $\mathbf { x } 1 = \mathbf { \Gamma } - 1$ . $0 +$ dx; Set range of integration. Doub $\tt x 2 = 1$ .0-dx; Doub x $\therefore = 0 , 0$ ; Fitting point. Load1 load1(n,m,gmma,c2[j],dx);Set up Load1, Load2, Rhsfpt, and Score Load2 load2(m,c2[j]); objects ... Rhsfpt d(m,c2[j]); Score score; Shootf<Load1,Load2,Rhsfpt,Score> shootf(nvar,n2,x1,x2,xf,load1, load2,d,score); ... use them to set up Shootf object ... newt(v,check,shootf); ... and use it to find v that zeros vector f in if (check) { Score. cout $< <$ "shootf failed; bad initial guess" << endl; } else { cout << " " << "mu(m,n)" << endl; cout $< <$ fixed $< <$ setprecision(6); cout << setw(12) $< < \texttt { v }$ [0] << endl; }   
}   
return 0;

# CITED REFERENCES AND FURTHER READING:

Flammer, C. 1957, Spheroidal Wave Functions (Stanford, CA: Stanford University Press); reprinted 2005 (New York: Dover).[1]

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, -21.[2]

Morse, P.M., and Feshbach, H. 1953, Methods of Theoretical Physics, Part II (New York: McGraw-Hill), pp. 1502ff.[3]

# 18.5 Automated Allocation of Mesh Points

In relaxation problems, you have to choose values for the independent variable at the mesh points. This is called allocating the grid or mesh. The usual procedure is to pick a plausible set of values and, if it works, to be content. If it doesn’t work, increasing the number of points usually cures the problem.

If we know ahead of time where our solutions will be rapidly varying, we can put more grid points there and less elsewhere. Alternatively, we can solve the problem first on a uniform mesh and then examine the solution to see where we should add more points. We then repeat the solution with the improved grid. The object of the exercise is to allocate points in such a way as to represent the solution accurately.

It is also possible to automate the allocation of mesh points, so that it is done “dynamically” during the relaxation process. This powerful technique not only improves the accuracy of the relaxation method, but also (as we will see in the next section) allows internal singularities to be handled in quite a neat way. Here we learn how to accomplish the automatic allocation.

We want to focus attention on the independent variable $x$ and consider two alternative reparametrizations of it. The first, we term $q$ ; this is just the coordinate corresponding to the mesh points themselves, so that $q = 0$ at $\mathtt { k } = 0$ , $q = 1$ at $\Bbbk = 1$ , and so on. Between any two mesh points we have $\Delta q = 1$ . In the change of independent variable in the ODEs from $x$ to $q$ ,

$$
{ \frac { d \mathbf { y } } { d x } } = \mathbf { g }
$$

becomes

$$
{ \frac { d \mathbf { y } } { d q } } = \mathbf { g } { \frac { d x } { d q } } 
$$

In terms of $q$ , equation (18.5.2) as an FDE might be written

$$
{ \bf y } _ { k } - { \bf y } _ { k - 1 } - \frac { 1 } { 2 } \bigg [ \bigg ( { \bf g } \frac { d x } { d q } \bigg ) _ { k } + \bigg ( { \bf g } \frac { d x } { d q } \bigg ) _ { k - 1 } \bigg ] = 0
$$

or some related version. Note that $d x / d q$ should accompany $\mathbf { g }$ . The transformation between $x$ and $q$ depends only on the Jacobian $d x / d q$ . Its reciprocal $d q / d x$ is proportional to the density of mesh points.

Now, given the function $\mathbf { y } ( x )$ , or its approximation at the current stage of relaxation, we are supposed to have some idea of how we want to specify the density of mesh points. For example, we might want $d q / d x$ to be larger where $\mathbf { y }$ is changing rapidly, or near to the boundaries, or both. In fact, we can probably make up a formula for what we would like $d q / d x$ to be proportional to. The problem is that we do not know the proportionality constant. That is, the formula that we might invent would not have the correct integral over the whole range of $x$ so as to make $q$ vary from 0 to $M - 1$ , according to its definition. To solve this problem we introduce a second reparametrization $Q ( q )$ , where $\boldsymbol { Q }$ is a new independent variable. The relation between $\boldsymbol { Q }$ and $q$ is taken to be linear, so that a mesh spacing formula for $d Q / d x$ differs only in its unknown proportionality constant. A linear relation implies

$$
{ \frac { d ^ { 2 } Q } { d q ^ { 2 } } } = 0
$$

or, expressed in the usual manner as coupled first-order equations,

$$
{ \frac { d Q ( x ) } { d q } } = \psi \qquad { \frac { d \psi } { d q } } = 0
$$

where $\psi$ is a new intermediate variable. We add these two equations to the set of ODEs being solved.

Completing the prescription, we add a third ODE that is just our desired mesh-density function, namely

$$
\phi ( x ) = { \frac { d Q } { d x } } = { \frac { d Q } { d q } } { \frac { d q } { d x } }
$$

where $\phi ( x )$ is chosen by us. Written in terms of the mesh variable $q$ , this equation is

$$
\frac { d x } { d q } = \frac { \psi } { \phi ( x ) }
$$

Notice that $\phi ( x )$ should be chosen to be positive-definite, so that the density of mesh points is everywhere positive. Otherwise (18.5.7) can have a zero in its denominator.

To use automated mesh spacing, you add the three ODEs (18.5.5) and (18.5.7) to your set of equations, i.e., to the array y[j][k]. Now $x$ becomes a dependent variable! $\boldsymbol { Q }$ and $\psi$ also become new dependent variables. Normally, evaluating $\phi$ requires little extra work since it will be composed from pieces of the $g$ ’s that exist anyway. The automated procedure allows one to investigate quickly how the numerical results might be affected by various strategies for mesh spacing. (A special case occurs if the desired mesh spacing function $\boldsymbol { Q }$ can be found analytically, i.e., $d Q / d x$ is directly integrable. Then, you need to add only two equations, those in 18.5.5, and two new variables $x , \psi$ .)

As an example of a typical strategy for implementing this scheme, consider a system with one dependent variable $y ( x )$ . We could set

$$
d Q = \frac { d x } { \Delta } + \frac { | d \ln { y } | } { \delta }
$$

or

$$
\phi ( x ) = \frac { d Q } { d x } = \frac { 1 } { \Delta } + \left| \frac { d y / d x } { y \delta } \right|
$$

where $\Delta$ and $\delta$ are constants that we choose. The first term would give a uniform spacing in $x$ if it alone were present. The second term forces more grid points to be used where $y$ is changing rapidly. The constants act to make every logarithmic change in $y$ of an amount $\delta$ about as “attractive” to a grid point as a change in $x$ of amount $\Delta$ . You adjust the constants according to taste. Other strategies are possible, such as a logarithmic spacing in $x$ , where $d x$ in the first term is replaced with $d \ln x$ .

# CITED REFERENCES AND FURTHER READING:

Eggleton, P.P. 1971, “The Evolution of Low Mass Stars,” Monthly Notices of the Royal Astronomical Society,vol.151, pp.351-364.   
Kippenhan, R., Weigert, A., and Hofmeister, E. 1968, in Methods in Computational Physics, vol. 7 (New York: Academic Press), pp. 129ff.

# 18.6 Handling Internal Boundary Conditions or Singular Points

Singularities can occur in the interiors of two-point boundary value problems. Typically, there is a point $x _ { s }$ at which a derivative must be evaluated by an expression of the form

$$
S ( x _ { s } ) = \frac { N ( x _ { s } , { \bf y } ) } { D ( x _ { s } , { \bf y } ) }
$$

where the denominator $D ( x _ { s } , \mathbf { y } ) = 0$ . In physical problems with finite answers, singular points usually come with their own cure: Where $D \to 0$ , there the physical solution $\mathbf { y }$ must be such as to make $N  0$ simultaneously, in such a way that the ratio takes on a meaningful value. This constraint on the solution $\mathbf { y }$ is often called a regularity condition. The condition that $D ( x _ { s } , \mathbf { y } )$ satisfy some special constraint at $x _ { s }$ is entirely analogous to an extra boundary condition, an algebraic relation among the dependent variables that must hold at a point.

We discussed a related situation earlier, in $\ S 1 8 . 2$ , when we described the “fitting point method” to handle the task of integrating equations with singular behavior at the boundaries. In those problems you are unable to integrate from one side of the domain to the other. However, the ODEs do have well-behaved derivatives and solutions in the neighborhood of the singularity, so it is readily possible to integrate away from the point. Both the relaxation method and the method of shooting to a fitting point handle such problems easily. Also, in those problems the presence of singular behavior served to isolate some special boundary values that had to be satisfied to solve the equations.

The difference here is that we are concerned with singularities arising at intermediate points, where the location of the singular point depends on the solution, so is not known a priori. Consequently, we face a circular task: The singularity prevents us from finding a numerical solution, but we need a numerical solution to find its location. Such singularities are also associated with selecting a special value for some variable that allows the solution to satisfy the regularity condition at the singular point. Thus, internal singularities take on aspects of being internal boundary conditions.

One way of handling internal singularities is to treat the problem as a free boundary problem, as discussed at the end of $\ S 1 8 . 0$ . Suppose, as a simple example, we consider the equation

$$
{ \frac { d y } { d x } } = { \frac { N ( x , y ) } { D ( x , y ) } }
$$

where $N$ and $D$ are required to pass through zero at some unknown point $x _ { s }$ . We add the equation

$$
z \equiv x _ { s } - x _ { 1 } \qquad { \frac { d z } { d x } } = 0
$$

where $x _ { s }$ is the unknown location of the singularity, and change the independent variable to $t$ by setting

$$
x - x _ { 1 } = t z , \qquad 0 \leq t \leq 1
$$

The boundary conditions at $t = 1$ become

$$
N ( x , y ) = 0 , \qquad D ( x , y ) = 0
$$

Use of an adaptive mesh as discussed in the previous section is another way to overcome the difficulties of an internal singularity. For the problem (18.6.2), we add the mesh spacing equations

$$
\begin{array} { l } { { \frac { d Q } { d q } = \psi } } \\ { { \frac { d \psi } { d q } = 0 } } \end{array}
$$

with a simple mesh spacing function that maps $x$ uniformly into $q$ , where $q$ runs from 0 to $M - 1$ , with $M$ the number of mesh points:

$$
Q ( x ) = x - x _ { 1 } , \quad { \frac { d Q } { d x } } = 1
$$

Having added three first-order differential equations, we must also add their corresponding boundary conditions. If there were no singularity, these could simply be

$$
\left. \begin{array} { l l } { \mathrm { a t } q = 0 : } & { x = x _ { 1 } , \quad Q = 0 } \\ { \mathrm { a t } q = M - 1 : } & { x = x _ { 2 } } \end{array} \right.
$$

and a total of $N$ values $y _ { i }$ specified at $q = 0$ . In this case the problem is essentially an initial value problem with all boundary conditions specified at $x _ { 1 }$ and the mesh spacing function is superfluous.

However, in the actual case at hand we impose the conditions

$$
\begin{array} { l l l } { { \mathrm { a t ~ } q = 0 : } } & { { x = x _ { 1 } , } } & { { Q = 0 } } \\ { { \mathrm { a t ~ } q = M - 1 : } } & { { N ( x , y ) = 0 , } } & { { D ( x , y ) = 0 } } \end{array}
$$

and $N - 1$ values $y _ { i }$ at $q \ : = \ : 0$ . The “missing” $y _ { i }$ is to be adjusted, in other words, so as to make the solution go through the singular point in a regular (zero-over-zero) rather than irregular (finite-over-zero) manner. Notice also that these boundary conditions do not directly impose a value for $x _ { 2 }$ , which becomes an adjustable parameter that the code varies in an attempt to match the regularity condition.

In this example the singularity occurred at a boundary, and the complication arose because the location of the boundary was unknown. In other problems we might wish to continue the integration beyond the internal singularity. For the example given above, we could simply integrate the ODEs to the singular point, and then as a separate problem recommence the integration from the singular point on as far we care to go. However, in other cases the singularity occurs internally, but does not completely determine the problem: There are still some more boundary conditions to be satisfied further along in the mesh. Such cases present no difficulty in principle, but do require some adaptation of the relaxation code given in $\ S 1 8 . 3$ . In effect, all you need to do is to add a “special” block of equations at the mesh point where the internal boundary conditions occur, and do the proper bookkeeping.

Figure 18.6.1 illustrates a concrete example where the overall problem contains five equations with two boundary conditions at the first point, one “internal” boundary condition, and two final boundary conditions. The figure shows the structure of the overall matrix equations along the diagonal in the vicinity of the special block. In the middle of the domain, blocks typically involve five equations (rows) in ten unknowns (columns). For each block prior to the special block, the initial boundary conditions provided enough information to zero the first two columns of the blocks. The five FDEs eliminate five more columns, and the final three columns need to be stored for the backsubstitution step (as described in $\ S 1 8 . 3 \AA$ ). To handle the extra condition, we break the normal cycle and add a special block with only one equation: the internal boundary condition. This effectively reduces the required storage of unreduced coefficients by one column for the rest of the grid, and allows us to reduce to zero the first three columns of subsequent blocks. The functions red, pinvs, and bksub can readily handle these cases with minor recoding, but each problem makes for a special case, and you will have to make the modifications as required.

# CITED REFERENCES AND FURTHER READING:

London, R.A., and Flannery, B.P. 1982, “Hydrodynamics of X-Ray Induced Stellar Winds,” Astrophysical Journal, vol. 258,pp.260-269.

![](images/40bef1fd2c6ab6b356706012d606879a94577e9022c245c7733c3103d8df942b.jpg)  
Figure 18.6.1. FDE matrix structure with an internal boundary condition. The internal condition introduces a special block. (a) Original form, compare with Figure 18.3.1; (b) final form, compare with Figure 18.3.2.

# Integral Equations and Inverse Theory
