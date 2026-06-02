# 7.4Probability ahd statistics

The matched filtering technique discussed above (as well as other tech niques that we will meet later in this chapter) provide us with a way to optimize the signal-to-noise ratio,assuming that a given signal is indeed present in our data stream. The issue that the experimenter normally faces (especially in the field df GW experiments) is however different We do not know a priori whether a GW signal is present or not in a given stream of data,and we know even less its waveform. We can apply the matched filtering technique repeating it with many possible different filters,e.g. many possible starting times for the putative sig nal,many possible parameters describing a family of waveforms, ete and we will correspondingly extract from our data stream a number o “events”,9 with various values of the signal-to-noise ratio $S / N$ What can we conclude from this? When can we claim detection of GWs? And if we can claim detection,what can we learn from it,in particular how can we reconstruct the properties of the source (such as,for an astro physical source,its direction,its distance,its mass,etc.),and with what accuracy?

To address these questions we need to use statistical reasoning. Befort looking into the technical aspects,it is however useful to discuss more generally the statistical frameworks that one can use,as we do in the next subsection.

# 7.4.1Frequentist and Bayesian approaches

An abstract definition of probability can be obtained by considering & set $S$ with subsets $A , B , \ldots$ whose interpretation for the moment left open,and defining the probability $P$ as a real-valued function that satisfies the Kolmogorov axioms:1. For every $A$ in $S$ ， $P ( A ) \geqslant 0$ 2 For disjoint subsets (i.e. $A \cap B = 0 { \mathrm { : } }$ ）， $P ( A \cup B ) = P ( A ) + P ( B ) .$ and3. $P ( S ) = 1$ .Furthermore,one defines the conditional probability $P ( A | B )$ (i.e.the probability of $A$ given $B$ )as

$$
P ( A | B ) = \frac { P ( A \cap B ) } { P ( B ) } .
$$

There exist two main approaches to probability, frequentist (also called classical) and Bayesian,depending on the interpretations of the subsets $A , B , \ldots$

In the frequentist interpretation, $A , B , \ldots$ are the outcome of a repeat able experiment,and the probability $P ( A )$ is defined as the frequency of occurrence of $A$ ，in the limit of an infinite number of repetitions. In this interpretation,the prqbabilities of obtaining some data are of course well-defined,and it also makes sense to consider the conditional probability of obtaining some data, given some hypothesis (or given a theory,or given the value of the parameters in a theory).10 There fore,quantities such as $P$ (data|hypothesis)or $P$ (data|parameters) make sense.However,one is never allowed to speak of the probability that the parameters take a given value,nor of the probability that a hypothesis, ora theory,is correct.Hypotheses,or theories,are not the outcome of a repeatable experiment. Rather,they are correct or they are wrong, and similarly the true value of a parameter ina theory is what it is,and these are facts that are not subject to probabilistic analysis.

In the Bayesian approach,instead,one is allowed to consider the probability of a hypothesis,or of a theory,or the probability that a parameter within a theory takes a given value.To define these probabilities,one starts from the identities $P ( A \cap B ) = P ( A | B ) P ( B )$ and $P ( B \cap A ) = P ( B | A ) P ( A )$ ,which follow from the definition (7.52) of conditional probability. On the other hand, $A \cap B = B \cap A$ and therefore

$$
P ( A | B ) = \frac { P ( B | A ) P ( A ) } { P ( B ) } ,
$$

which is Bayes’ theorem.Observe alsd that,from the axioms of probability given above,it follows that

$$
P ( B ) = \sum _ { i } { P ( B | A _ { i } ) P ( A _ { i } ) } ,
$$

for any $B$ and for $A _ { i }$ disjoints and such that $\cup _ { i } A _ { i } \ = \ S$ .Therefore eq.(7.53) can be rewritten as

$$
P ( A | B ) = \frac { P ( B | A ) P ( A ) } { \sum _ { i } P ( B | A _ { i } ) P ( A _ { i } ) } ,
$$

$8 0$ the denominator is just a normalization factor.As long as $A$ and $B$ are the outcome of a repeatable experiment,eq.(7.55) would be accepted also by frequentists.In the Bayesian approach, however,one applies this to $A =$ hypothesis (or parameters,or theory） and $B =$ data.Then one fnds that

$$
P ( \mathrm { h y p o t h e s i s } | \mathrm { d a t a } ) \propto P ( \mathrm { d a t a } | \mathrm { h y p } \mathrm { \diamond } \mathrm { t h e s i s } ) P ( \mathrm { h y p o t h e s i s } ) .
$$

Ihe probability of the hypothesis given the data is called the posterior probability,and eq.(7.56) states that itis proportional to the product of wo factors.The first is the probability of the data given the hypothesis "honest”frequentist probability),Which is called the likelihood funclion.The second is the probability of the hypothesis,and is called the prior probability (or,simply,the prior).The latter cannot be determined Just by performing identical trials (so it makes no sense to a frequentist) d,in the Bayesian approach,one must make assumptions to determine It.In fact,this prior probability in geheral can even depend on subjecfive factors,and on the state of knowledge of the person that makes he analysis.In the Bayesian interpretation, $P$ (hypothesis) can be seen the “degree of belief” that the hypbthesis is true,and eq.(7.56) desribes the evolution of this degree of belief due to the fact that we have performed the measurement.The prior probability describes the degree belief in the hypothesis before the measurement was made,and the Dosterior probability describes the degree of belief after.11

![](images/dc4aa370b763e6a353107b6b1c453d3ac35ec4a21f9139fc56eced0665f7523e.jpg)

![](images/dd2ef2a96ea2dda4c69e0a1407cf442b459d2fecfb9143bba83b43a9b0d3e373.jpg)  
Fig.7.2 The Neyman construction for the lower limit $x _ { 1 }$ of the confidence interval. Here the measured value was $x _ { 0 } ~ = ~ 5$ and,to get the interval at $9 0 \%$ C.L.,we look for a Gaussian distribution such that its area at $x \geqslant 5$ (shaded region) is $5 \%$ of the total area.This is a Gaussian centered in $x _ { 1 } \simeq x _ { 0 } - 1 . 6 4 4 8 5 \sigma$ (here we used $\sigma = 1$ ).   
Fig.7.3 The same as the previous figure,for the upper limit $\scriptstyle { \mathcal { X } } _ { 2 }$ of the confidence interval. The Gaussian is now centered in $x _ { 2 } \simeq x _ { 0 } + 1 . 6 4 4 8 5 \sigma$

This difference in approach implies also an important difference among the frequentist and the Bayesian notions of confidence interval and of confidence level (C.L.). The expression “confidence interval”,without further qualifcations,refers tp the frequentist definition,and has the following meaning. Suppose that we are performing repeated identical measurements of a physical quantity $\boldsymbol { \mathscr { X } }$ .We want to express our result saying that,at a given confidence level,say $9 0 \%$ ， $x _ { 1 } < x < x _ { 2 }$ What is meant by this is the following.The true (unknown) value of $x$ isa fixed number $x _ { t }$ ,which is always the same in allrepetitions of the experiment each repetition provides a different interval $[ x _ { 1 } , x _ { 2 } ]$ ， that we want to construct in such a way that $\mathbf { \mathcal { X } } _ { t }$ will be contained inside this interval in $9 0 \%$ (or whatever the specified C.L.) of the repetitions, no matter what the true value $x _ { t }$ is.This is the frequentist concept of coverage.There is a general construction,given by Neyman in a famous l937 paper,that allows us to construct the frequentist confidence intervals.We illustrate it in the simple case in which we know that the experimental apparatus provides values distributed as a Gaussian around the true value $x _ { t }$ ,with a standard deviation $\sigma$ ，

$$
P ( x | x _ { t } ) = \frac { 1 } { ( 2 \pi \sigma ^ { 2 } ) ^ { 1 / 2 } } \exp \left\{ - \frac { ( x - x _ { t } ) ^ { 2 } } { 2 \sigma ^ { 2 } } \right\} .
$$

Suppose that a given repetiticn of the experiment yields the value $x _ { 0 }$ The Neyman's construction (using for definiteness $9 0 \%$ C.L.）proceeds by finding a value $x _ { 1 } < x _ { 0 }$ such that $5 \%$ of the area under $P ( x | x _ { 1 } )$ is at $x > x _ { 0 }$ .That is,we fix $x _ { 1 }$ by requiring that a Gaussian distribution centered on $x _ { 1 }$ ,only in $5 \%$ of the cases produces values of $x$ higher than $x _ { 0 }$ ,see Fig.7.2.If the true value ${ \boldsymbol { \mathscr { x } } } _ { t }$ were smaller than such $x _ { 1 }$ ，then the value $x _ { 0 }$ that we observed was due to a statistical fuctuation that takes place in less than $5 \%$ of the repetitions,so choosing in this way the lower limit of the interval, we are wrong at most in $5 \%$ of the cases. The upper limit of the confidence ihterval is obtained similarly,by findinga value $x _ { 2 } > x _ { 0 }$ such that $5 \%$ of the area under $P ( x | x _ { 2 } )$ isat $x < x _ { 0 }$ see Fig.7.3.Observe that the probabilistic variables in this construction are $x _ { 1 }$ and $x _ { 2 }$ ,while the true value $x _ { t }$ is fixed (and unknown).

In contrast,the Bayesian approach constructs a probability distribution for the true value $x _ { t }$ . This is obtained from the likelihood function $P ( \mathrm { d a t a } ,$ hypothesis) in eq.(7.56)，where the hypothesis is that the true value of $x$ is $x _ { t }$ and the data is the observed value $x _ { 0 }$ . We denote this likelihood function as $\Lambda ( x _ { 0 } | x _ { t } )$ .In our case, this is the same as the Gaussian given in eq. (7.57)，so $\Lambda ( x _ { 0 } | x _ { t } ) = P ( x _ { 0 } | x _ { t } )$ As long as we interpret it as the probability of obtaining the value $x _ { 0 }$ ， given that the true value is ${ \boldsymbol { \mathscr { X } } } _ { t }$ ,the likelihood function is a legitimate frequentist con cept.However,in the Bayesian approach,it is inserted into eq. (7.56) together in this case with a fat prior in $x _ { t }$ ,to get a probability density function (p.d.f.) in the variable ${ \boldsymbol { \mathscr { X } } } _ { t }$ ,given the observed value $x _ { 0 }$ ，

$$
P ( x _ { t } | x _ { 0 } ) = \frac { 1 | } { ( 2 \pi \sigma ^ { 2 } ) ^ { 1 / 2 } } \exp \left\{ - \frac { ( x _ { t } - x _ { 0 } ) ^ { 2 } } { 2 \sigma ^ { 2 } } \right\} .
$$

So,in this case we havea Gaussiandistribution centered on $x _ { 0 }$ (rather than on $x _ { 1 }$ oron $x _ { 2 }$ as in the Neyman onstruction),and we use it as a p.d.f.for $x _ { t }$ .The most probable value f $x _ { t }$ is found by maximizing this p.d.f., which of course gives $x _ { t } = x _ { 0 }$ ,and the Bayesian $9 0 \%$ confidence interval is defined as the interval which subtends an area equal to $9 0 \%$ of the total area of the p.d.f.12 In the case of a Gaussian distribution,the Bayesian and frequentist definitions give the same result for $x _ { 1 }$ and $x _ { 2 }$ ， even if the interpretation is different.However, in a general situation, the two definitions do not agree. The frequentist confidence interval, by construction,always has the prescribed coverage,i.e.we are sure that in the limit of a large number of repetitions, $9 0 \%$ (or whatever the chosen C.L.）of the confidence intervals obtained by the different repetitions of the experiment will include（“cover"） the true value $x _ { t }$ no matter what $x _ { t }$ is.This covering properties is not necessarily true in the Bayesian procedure,which in certain cases yields intervals whose frequentist coverage is less than the stated C.L. (i.e. they undercover). This can happen in particular for event-counting experiments,that obey Poisson statistics,when the data sample is small.

Beside the situation when we have small numbers, the other typical situation where the Bayesian and frequentist approaches can give sensibly different answers is when the variable $x$ ,for physical reasons,has bounded domain，and the measured values are close to the boundaries of the domain.An instructive example,that nicely illustrates the lifferent results that can be obtained with the Bayesian and the frequentist approaches in such situations,is the folowing.13 Nowadays, we know from oscillation experiments that|the three neutrinos havea small mass,with squared masses (more precisely,squared mass differences) between $1 0 ^ { - 5 }$ and $1 0 ^ { - 4 } \mathrm { e V } ^ { 2 }$ ．Before these results,a number of other experiments attempted a direct measure of the mass $m _ { \nu }$ of the electron meutrino (or more precisely,of $m _ { \nu } ^ { 2 }$ )fromtritium beta decay.In the early 1990s the experimental situation was that various experiments reported negative values for their best estimate of $m _ { \nu } ^ { 2 }$ . This is not surprising in principle since,if $m _ { \nu } ^ { 2 }$ were really zero,or anyway much smaller than he experimental accuracy (as indeed it was)，and if the distribution f the data is an unbiased Gaussian,pn average half of the ensemble of the experiments should report negative values,and statistical flucations can drive the average over the experiments in the unphysical region $m _ { \nu } ^ { 2 } < 0$ .However, these negative fluctuations happened to be so large that even the frequentist upper limit at $9 0 \%$ C.L.was negative, nd was $m _ { \nu } ^ { 2 } < - 1 6 \mathrm { e V } ^ { 2 }$ 14 To say the least,it is quite disturbing to set up a complicated experiment to come but with the conclusion that $m _ { \nu } ^ { 2 }$ Ssmaller than a negative value.The point is that this statement holds $9 0 \%$ C.L., so it should be false in $1 0 \%$ of the cases,and here we know r sure that we are in this false $1 0 \%$ .15

A possible alternative in this case is|to include our prior information hat $m _ { \nu } ^ { 2 } \geqslant 0$ ，This suggests to take a Bayesian approach with a prior p.d.f. $P ( m _ { \nu } ^ { 2 } )$ which is zero when $m _ { \nu } ^ { 2 } < \emptyset$ ,and uniform for $m _ { \nu } ^ { 2 } \geqslant 0$ ,and to se the resulting posterior p.d.f. to set the bound on $m _ { \nu } ^ { 2 }$ .Here however

12Such an interval is selected uniquely by imposing an extra requirement,typically that it is symmetric around the maximum,or that it is the minimum length interval.For a Gaussian distribution, these two conditions give of course the same result.

13We follow the paper by Cousins (1995)，“Why isn't every physicist a Bayesian?",where the reader can find a very clear exposition of the difference between the Bayesian and frequentist approaches.

14Since the early 1990s,direct experiments (i.e.experiments not based on oscillations） on the electron neutrino mass squared have improved,but still their world average is negative,see Yao et al.[Particle Data Group] (2006).

$^ { 1 5 } \mathrm { { I t } }$ should be mentioned that astrict application of the frequentist Neyman construction can never produces an upper limit in the unphysical region,but rather an empty confidence interval (which is equally disturbing)．There is however a generalization of the Neyman construction that produces nonempty intervals in the physical region, see Feldman and Cousins (1998).

the problem arises as to whether,in the region $m _ { \nu } ^ { 2 } \geqslant 0$ ,the prior should be uniform in the variable $m _ { \nu } ^ { 2 }$ orin $m _ { \nu }$ ,orin $\log m _ { \nu }$ , etc. Of course a distribution $P ( m _ { \nu } ^ { 2 } ) d m _ { \nu } ^ { 2 }$ with $P ( m _ { \nu } ^ { 2 } ) = \mathrm { c o n s t }$ . is fat with respect ro the variable $m _ { \nu } ^ { 2 }$ but,since $d m _ { \nu } ^ { 2 } = 2 m _ { \nu } d m _ { \nu }$ ,it is linearly raising witl respect to $m _ { \nu }$ .The issue is significant since the resulting upper boun depends on the choice. In this specific problem the consensus finally settled on using a fat prior in $m _ { \nu } ^ { 2 }$ ，which gave an upper bound,at $9 0$ C.L., $m _ { \nu } ^ { 2 } < 2 6 . 6 \mathrm { e V } ^ { 2 }$

A physicist that is not too nuch interested in the philosophical as pects of the debate,can take a pragmatic attitude and use a frequentis or a Bayesian approach,depending on the kind of experiment to be al alyzed.In particular, elementaty particle physics is very well suited fol the frequentist approach.This basically stems from the fact that in thi case it is the physicist that controls the parameters of the experiments (e.g.the kind of particle used in the beams,the beam energy,etc.) an can reproduce them accurately many times.We are therefore in th situation where the frequentist notion of repeated trials fits very well. The advantage is that this allows us to report objectively the outcome of the experiment,without the heed of incorporating prior (and possibly subjective） beliefs.

16In fact,in the standard compilation of experimental high-energy physics data,the Particle Data Group (PDG) “Reviews of Particle Properties",essentially all measurements and their statistical uncertainties are reported within the frequentist framework.

On the other hand in astrophysics,and even more in GW astrophysics the sources can be rare,they are not under the control of the experi menter,and each one is very interesting individually.If a single BH-BH binary coalesces,and we detect jits signal in a GW experiment,we woul obviously be very interested in lquestions such as in which direction th binary system was,at what distance from us,what were the masse of the two black holes,their spins,etc. A strict frequentist approach is inapplicable here.We do nbt have at our disposal an ensemble( identical BH-BH binaries located in that position,with the same value of the masses,etc. We just have that unique event,and we want to get the maximum out of it.In this case,a Bayesian approach can $b _ { E }$ more appropriate,since it allows us to ask questions such as“What was the most likely value of the position,masses,spin,etc.of the BHs?" For this reason,while negativeresults,giving upper limits on the rate of GW signals, should normally be expressed in frequentist terms,th discussion of parameter estimation from a given positive detection,t which we turn next,should rather be performed within the Bayesian framework.

# 7.4.2 Parameters estimation

In Section 7.3,when we introduced the matched filtering technique, we assumed that the form of $h ( t )$ is known. In practice,however, $h ( t )$ will necessarily depend on a number of free parameters.For instance,if $h ( t )$ is a short burst of GWs,among its parameters we will certainly have its time of arrival $t _ { 0 }$ .When searching for very short bursts we might simplv use a Dirac delta, so $h ( t ) = h _ { 9 } \delta ( t - t _ { 0 } )$ ,but more generally we might also wish to include its temporal width $\Delta t$ and possibly more parameters describing the shape of the pulse.For a coalescing binary,among the parameters we will have the time of entryin the interferometer bandwidth, the distance to the source, the star masses, etc.

Therefore,we must consider a family of possible waveforms,or templates, that we denote generically as $h \left( t ; \theta \right)$ ，where $\boldsymbol { \theta } = \left\{ \theta _ { 1 } , \ldots , \theta _ { N } \right\}$ isa collection of parameters. Correspondingly,we have a family of optimal filters $K ( t ; \theta )$ ,determined through eq.(7.49), $\tilde { K } ( f ; \theta ) \sim \tilde { h } \bar { ( } f ; \theta ) / \tilde { S } _ { n } ( f )$ In practice,this means that we must discretize the $\theta .$ -space,and repeat the filtering procedure many times,once for each point of this discretized parameter space (except that for some parameters the maximization procedure can be done analytically, see below).

The problem that we addressin this section is the following.Suppose that a GW signal has indeed been detected,which means that for some template $h ( t ; \theta )$ the value of $S / N$ ，determined by the optimal Wiener fltering (or by any other procedure that we specified in advance） has exceeded a predetermined threshold,and the signal satisfes further criteria that we might have set for claiming detection, such as coincidences between different detectors (we will see in more detail in Sections 7.4.3 and 7.5.3 some possible criteria that could allow us to claim a detection, at a given confdence level). How do we reconstruct the most probable value of the parameters of the source,and how we compute the error on these parameters?

This question is Bayesian in nature,so its answer is contained in the Dosterior probability. To compute the likelihood function,and hence the posterior probability，we assume for simplicity that the noise $n ( t )$ s stationary and Gaussian. From eq.(7.6) we see that the variance f the Fourier mode of the noise with frequency $f$ is proportional to $( 1 / 2 ) S _ { n } ( f )$ ,so the corresponding Gaussian probability distribution for the noise is

$$
p ( n _ { 0 } ) = { \cal N } \exp \left\{ - \frac { 1 } { 2 } \int _ { - \infty } ^ { \infty } d f \frac { | \tilde { n } _ { 0 } ( f ) | ^ { 2 } } { ( 1 / 2 ) S _ { n } ( f ) } \right\} ,
$$

where $\mathcal { N }$ is a normalization constant.|This is the probability that the noise $n ( t )$ ，which is a random variable with zero mean，has a given realization $n _ { 0 } ( t )$ .The above result $\mathfrak { c } \mathrm { { a n } }$ be rewritten very simply in erms of the scalar product (7.46) as17

$$
\begin{array} { r } { p ( n _ { 0 } ) = \mathcal { N } \exp \{ - \vert ( n _ { 0 } \vert n _ { 0 } ) / 2 \} . } \end{array}
$$

We are assuming that the output of the detector satisfies the condition br claiming detection,i.e.it is of the form $s ( t ) = h ( t ; \theta _ { t } ) + n _ { 0 } ( t )$ ，where $v ( i )$ is the specific realization of the noise in correspondence to this ivent,and $\theta _ { t }$ is the (unknown） true walue of the parameters $\theta$ The kelihood function for the observed output $s ( t )$ ，given the hypothesis Mat there is a GW signal corresponding to the parameters $\theta _ { t }$ ,is obtained plugging $n _ { 0 } = s - h ( \theta _ { t } )$ into eq. (7.62)

$$
\Lambda ( s | \theta _ { t } ) = \mathcal { N } \exp \left\{ - \frac { 1 } { 2 } ( s - h ( \theta _ { t } ) | s - h ( \theta _ { t } ) ) \right\} ,
$$

17For simplicity， we limit ourselves to the case of a single detector.The formalism can however be extended straightforwardly to multiple detectors. In this case the definition of the noise spectral density,eq.(7.6),is replaced by

$$
\langle \tilde { n } _ { a } ^ { * } ( f ) \tilde { n } _ { b } ( f ^ { \prime } ) \rangle = \delta ( f - f ^ { \prime } ) { \frac { 1 } { 2 } } [ S _ { n } ( f ) ] _ { a . b } ,
$$

where the indices $a , b$ label the detectors.This definition takes into account the possibility of correlated noise.Let ${ \bf A } ( t )$ and $\mathbf { B } ( t )$ be vectors whose components $A _ { a } ( t )$ and $B _ { a } ( t )$ are output of the single detectors,and let $[ S _ { n } ^ { - 1 } ] ^ { \bar { a } \bar { b } }$ denote the inverse matrix.The equations of this section can then be generalized to multipole detectors,using the scalar product

$$
\begin{array} { l } { { \displaystyle ( { \bf A } | { \bf B } ) = 4 \mathrm { R e } } \qquad } { \displaystyle ( 7 . }  \\ { { \displaystyle \int _ { 0 } ^ { \infty } d f \tilde { A } _ { a } ^ { * } ( f ) [ S _ { n } ^ { - 1 } ( f ) ] ^ { a b } B _ { b } ( f ) , } } \end{array}
$$

which generalizes eq.(7.46)．See the Further Reading for details.

or,introducing the short-hand notation $h _ { t } \equiv h ( \theta _ { t } )$ ，

$$
\Lambda ( s | \theta _ { t } ) = \mathcal { N } \exp \left\{ | ( h _ { t } | s ) - \frac { 1 } { 2 } ( h _ { t } | h _ { t } ) - \frac { 1 } { 2 } ( s | s ) \right\} .
$$

18 As an example of prior information, one of the typical parameters entering in the waveform is the distance $r$ to the source,and we might be searching for signals from a population of stars with a known distribution in space,e.g.a distribution $p ^ { ( 0 ) } ( r ) d r \sim r ^ { 2 } d r$ for isotropic sources,or $p ^ { ( 0 ) } ( r ) d r \sim r d r$ for sources within a few kpc from us,in the Galactic disk.Another typical parameter is the mass of the star and,for neutron stars,we know from astrophysical observations that their mass distribution is strongly concentrated around $1 . 3 5 M _ { \odot }$

In the Bayesian approach,acdording to eq. (7.56),we also introducel prior probability $p ^ { ( 0 ) } ( \theta _ { t } )$ .18 Then,the posterior probability distributio for the true value $\theta _ { t }$ ，given the observed output $s$ ，

$$
\boxed { p ( \theta _ { t } | s ) = \mathcal { N } p ^ { ( 0 ) } ( \theta _ { t } ) \exp \left\{ \vphantom { \frac { 1 } { \sum _ { t } | s | } } ( h _ { t } | s ) - \frac { 1 } { 2 } ( h _ { t } | h _ { t } ) \right\} , }
$$

where,since we are considering $p ( \theta _ { t } | s )$ as a distribution in $\theta _ { t }$ for a fixe output $s$ ,we have reabsorbed into the normalization factor $\mathcal { N }$ the term $( s | s ) / 2$ which appears in the exponential in eq.(7.64).

Once the prior distribution is given,eq.(7.65) gives the p.d.f. in th parameter space,so in principle it contains all the information tha we need. However,in this fprm the information might not be ver manageable.The $\theta .$ -space willin general be a multi-dimensional spaced large dimension.For examplefor a binary coalescence the paramete $\theta ^ { i }$ that deternine the waveform,at the post-Newtonian level,are th distance,the source's location (two angles),the orientation of the norma to the orbit (two more angles),the time at which the signal enters in tl interferometer's bandwidth,the orbital phase at that moment, the tw masses of the stars,and their \$pins,so 15 parameters in all.19 From tl probability distribution function (7.65) in such a complicated space W would like to extract some more approximate, but also more manageable information; essentially,we waht the most probable value of the variable $\theta _ { t }$ ,that we denote by $\hat { \theta }$ ,and also their corresponding errors.

19Assuming that the eccentricity can be neglected,since the orbit should be highly circular by the time the signal enters in the bandwidth of a ground-based detector，as we saw in Section 4.1.3.

20For details see,e.g.the statistics section of Yao et al. [Particle Data Groupl (2006).

There is no unique way of defining what is the most probable valu of $\theta _ { t }$ .A rule for assigning the most probable value is called an estina tor. The most important properties that an estimator must have are:" (a) Consistency:the estimator must converge to the true value as th amount of data increases. This property is so important that it is pos sessed by all commonly used e\$timators.(b) The bias $b$ is defined as th difference between the expectation value of the estimator, $E ( { \hat { \theta } } )$ (taken over a hypothetical set of similar experiments in which $\hat { \theta }$ is constructe in the same way),and the true value $\theta _ { t }$ ， $b \equiv E ( \widehat { \theta } ) - \theta _ { t }$ .When $b = 0$ the estimator is said to be unbiased.(c) Effciency:we want the smalles possible value for the variance of $\hat { \theta }$ ,and (d)Robustness,i.e. the propert of being relatively insensitive to small departure in the assumed p.d due to factors such as noise.

21As we already mentioned when discussing the example of the neutrino mass on page 350,a distribution which is flat with respect to the variables $\theta _ { t }$ is no longer flat if we make a nonlinear transformation of the parameters.Therefore this prior distribution assumes a definite choice of coordinates in the parameter space.

Two choice of estimators seems especially reasonable. The first i to define $\hat { \theta }$ as the value which maximizes the probability distributiol function (7.65).Another natural option is to define it as the average o $\theta _ { t }$ ,over the distribution (7.65).We discuss these options below.

# Maximum likelihood estimator

Let us consider first the situation in which the prior probability is fat.

Then,maximization of the posterior probability becomes the same as maximization of the likelihood $\Lambda ( s | \theta _ { t } )$ . The value of $\theta _ { t }$ that maximizes $\therefore ( s | \theta _ { t } )$ defines the maximum likelihood estimator,and we denote it by $\widehat { \theta } _ { \mathrm { M L } } ( s )$ . It is the most widely used estimator in general situations.22 It is usually simpler to maximize $\log \Lambda$ From eq. (7.64),

$$
\log \Lambda ( s | \theta _ { t } ) = ( h _ { t } | s ) - \frac 1 2 ( h _ { t } | h _ { t } ) .
$$

Since we are working at fixed $s$ ,the term $( - 1 / 2 ) ( s | s )$ in eq. (7.64) is an irrelevant constant,and we omited it.Denoting $\partial / \partial \theta _ { t } ^ { i }$ simply by $\partial _ { i }$ the value of $\hat { \theta } _ { \mathrm { M L } }$ is found by solving the equations

$$
\bigl ( \partial _ { i } h _ { t } \vert s \bigr ) - \bigl ( \partial _ { i } h _ { t } \vert h _ { t } \bigr ) = 0 .
$$

The errors $\Delta \theta ^ { i }$ can then be defined in terms of the width of the probability distribution function （7.65）at the peak.

Typically, (7.67) is a set of equations that must be solved numerically (except for some parameter such as the overall amplitude that can be eliminated analytically,see below). However, they have a rather simple geometric interpretation. The set of all possible waveforms $h ( t ; \theta )$ defines a manifold, called the manifold of the signals,parametrized by the coordinates $\theta ^ { i }$ . This is a subset of zero measure in the space of all possible functions,so the addition of generic noise $n ( t )$ to a function $h ( t ; \theta )$ will necessarily bring us out of this manifold.In Fig.7.4 we illustrate the situation with a two-dimensional manifolds of the signals. The point labeled $\theta _ { t }$ represents the true value of the signal,and therefore lies on the manifold. The addition of noise carries us outside this manifold. Since we are minimizing ${ \big ( } s - h | s - h )$ ,see eq.(7.63),the maximum likelihood estimator actually searches the point on the signal manifold which is dlosest to the output s,where distances are defined with respect to the scalar product $( \bigstar \bigstar )$

To summarize,in the Bayesian framework $\hat { \theta } _ { \mathrm { M L } }$ is determined assuming A flat prior distribution and requiring the maximization of the posterior probability (7.65),i.e.maximizing our “degree of belief”in the hypothsis that there is a GW signal. A natural question,at this point,is what is the relation between $\hat { \theta } _ { \mathrm { M L } }$ and the value of $\theta$ that provides the lighest signal-to-noise ratio in the matched filtering. We now prove that In fact they are the same. To show it we write the generic template as $\begin{array} { r } { h ( t ; \theta ) = a h _ { a } ( t ; \xi ) } \end{array}$ ，where $a$ is an amplitude,and is a free parameter, while the normalization of $h _ { a }$ has been fixed imposing some condition. We have separated the parameters $\theta$ into $a$ and the remaining parameters, that we call $\xi$ .The maximization with respect to $a$ of $\log \Lambda$ can be performed analytically since,fromeq.(7.66),23

22See any textbook on statistics， e.g. Lyons (1986)，Section 4.4,for an introduction to the maximum likelihood method and its virtues.Observe that the likelihood isa legitimate concept also in the frequentist approach．The most probable frequentist value is again identified with the maximum of the likelihood,and the confidence interval is usually defined in terms of the point where $2 \log \Lambda$ decreases by one unit with respect to its value at the maximum. In the frequentist approach,however, we cannot use the likelihood as a p.d.f. for the true values of the parameters, i.e.we cannot consider areas under the curve,and of course we cannot include priors.

![](images/af1b8f123954d62db903689f1c4ffe05085a4b1ed838c5c9c8b3c291d7938996.jpg)  
Fig.7.4 The manifolds of the signals,parametrized by the coordinates $( \theta _ { 1 } , \theta _ { 2 } )$ ．The point $\theta _ { t }$ is the true value of the signal． The addition of noise to $h ( \theta _ { t } )$ brings us outside this manifold,and the maximum likelihood estimator searches the point on the signal manifold which is closest to $s$

$$
\log \Lambda ( s | a , \xi ) = a ( h _ { a } | s ) - \frac { a ^ { 2 } } { 2 } ( h _ { a } | h _ { a } ) .
$$

Requiring $\partial \log \Lambda / \partial a = 0$ ,we get the|maximum likelihood estimate fol

$$
\hat { a } _ { \mathrm { M L } } ( s ) = \frac { \left( h _ { a } | s \right) } { \left( h _ { a } | h _ { a } \right) } .
$$

23To keep the notation lighter，we omit the subscript t (which stands for “true"） from $a$ and $\xi$ We are anyway considering p.d.f. for the true values of the parameters.

The maximization with respect to the remaining variables $\xi$ can be performed substituting this expression for $a$ into $\log \Lambda$ ,obtaining

$$
\log \Lambda ( s | \xi ) = \frac { 1 } { 2 } \frac { ( h _ { a } | s ) ^ { 2 } } { ( h _ { a } | h _ { a } ) } .
$$

The maximization of this quantity amounts to maximizing the overlap of the output $s$ with the normalized template $h _ { a } / ( h _ { a } | h _ { a } ) ^ { 1 / 2 }$ ，where the overlap is measured using the scalar product $( \bigstar \bigstar )$ ，defined in terms of the noise spectral density ${ \cal { S } } _ { n } ( f )$ .This is just the matched filtering procedure discussed in the Section 7.3. Thus, the maximum likelihood method provides a way of estimating the overall amplitude $a$ (which cannot be fixed just searchingfor the filter that maximizes the signal to-noise ratio, since eq.(7.47) is unchanged by a multiplicative rescaling of the filter $u$ ） while,for the remaining parameters,it returns the values that maximize the signal-to-noise ratio according to matched filtering.

24We also mention that another way of understanding the meaning of the maximum likelihood procedure is in term of the Neyman-Pearson criterium,which consists in maximizing the probability of detection，subject to a given false alarm probability,and leads again to the condition that $\log \Lambda$ be maximum.

# Maximum posterior probability

25In the GW literature,the log of the prior $p ^ { 0 } ( \theta )$ is sometime added to the exponential in eq.(7.65),and the resulting exponential is called again the loglikelihood function, $\log \Lambda$ ,so the corresponding estimator is called again the maximum likelihood estimator.This notation is however potentially confusing.For instance,one might be tempted to make a frequentist use of such a $" | \boldsymbol { 0 } \boldsymbol { \mathrm { g } } \boldsymbol { \Lambda } ^ { * }$ ，which is obviously incorrect,since it involves a prior probability.

In various situations we do have important prior information, and w might want to include it in the analysis,see Note 18 for examples. In this case,rather then maximizing the likelihood function,we must determine the estimator by maximizing the full posterior probability $p ( \theta _ { t } | \boldsymbol { s } )$ given in eq.(7.65),which takes into account the prior probability distri bution.25 For a generic prior,of course,the maximum of the posterior distribution will change, so it willno longer coincide with the value that gives the highest signal-to-noise ratio in the matched filtering. What happens is that the value suggested by matched filtering is weighted against our prior expectations (in a real sense,our “prejudices”）, to provide a new estimate of the most likely value for the true parameters.

When we want to include ndn-trivial prior information,some concep tual complication may appear (apart from the issue of how to choose the appropriate prior).Suppqse, for definiteness,that we have a two dimensional parameter space $( { \dot { \theta } } _ { 1 } , { \dot { \theta } } _ { 2 } )$ ,as in Fig.7.4,and that we are not interested in the variable $\theta _ { 2 }$ . Then, we can integrate the p.d.f. given in eq.(7.65）over $\theta _ { 2 }$ ,to obtain areduced p.d.f. in the variable $\theta _ { 1 }$ From the geometric interpretation given in Fig.7.4 it is clear that,as far as the likelihood function is concerned,the maximum in the variable $\theta _ { 1 }$ is the same,independentlyof whether we integrated or not over $\theta _ { 2 }$ However,once we include a generic non-fat prior probability $p ^ { ( 0 ) } ( \theta )$ this nice geometric interpretation is lost and,in general, if $( { \bar { \theta } } _ { 1 } , { \bar { \theta } } _ { 2 } )$ is the maximum of the distribution function $p ( \theta _ { 1 } , \theta _ { 2 } | s )$ ，it is no longer true that the $\bar { \theta } _ { 1 }$ is the maximum of the reduced distribution function $\begin{array} { r } { \tilde { p } ( \theta _ { 1 } | s ) = \int d \theta _ { 2 } p ( \theta _ { 1 } , \theta _ { 2 } | s ) } \end{array}$ ，obtained integrating out $\theta _ { 2 }$ .Thus,there is an ambiguity on the value pf the most probable value of $\theta _ { 1 }$ ，which depends on whether we are interested or not in $\theta _ { 2 }$ .Another possible drawback,this one common to both the maximum likelihood and the maximum posterior methods,is that we might want an estimator that minimizes the error on the parameter determination,and this in general is not the case for the maximum likelihood or maximum posterior probability estimators.These issues motivate the consideration of the Bayes estimator,in the next subsection.

# Bayes estimator

In this case the most probable values of the parameters is defined by

$$
{ \hat { \theta } } _ { \mathrm { B } } ^ { i } ( s ) \equiv \int d \theta \theta ^ { i } p ( \theta | s ) ,
$$

i.e. is the average with respect to the posterior probability distribution. The errors on the parameters is defned by the matrix

$$
\Sigma _ { B } ^ { i j } = \int d \theta [ \theta ^ { i } - { \hat { \theta } } _ { \mathrm { B } } ^ { i } ( s ) ] [ \theta ^ { j } - { \hat { \theta } } _ { \mathrm { B } } ^ { j } ( s ) ] p ( \theta | s ) ,
$$

that is,in terms of the mean square deviations from ${ \widehat { \theta } } _ { \mathrm { B } } ^ { i } ( s )$ ，where the average is taken again with respect tΦ $p ( \theta | s )$ ．Even when there is a non-trivial prior probability function,the Bayes estimator is clearly independent on whether we integrate out some variable from $p ( \theta | s )$ ，since we anyhow integrate over all the $\theta ^ { i }$ when computing $\widehat { \theta } _ { \mathrm { B } } ^ { i }$ and $\Sigma _ { B } ^ { i j }$ Furthermore,it can also be shown that,if one wants to minimize the error on the parameters,averaged over the whole parameter space,the Bayes estimator is the optimal one.

The “operational” meaning of the Bayes estimator is the following. Suppose that,after a sufficiently long run,we end up with a large ensemble of detected signals,which correspond to actual GWs,and that among them there is still a large subensemble of GW signals that produced a given output $s ( t )$ .Each of these waves will be characterized by diferent values of the true parameters $\theta _ { t }$ and therefore by a different $h ( t ; \theta _ { t } )$ that,by combining each time with a different realization of the noise $n ( t )$ ,has produced the same output $s ( t )$ .Then ${ \widehat { \theta } } _ { \mathrm { B } } ^ { i } ( s )$ is the value of $\theta ^ { i }$ ,averaged over this ensemble of signals,and $\Sigma _ { B } ^ { i j }$ is the corresponding Ims error.

Thus,the Bayes estimator has a well-defined operational meaning,and welcome mathematical properties,such as the independence on whether we integrate out some variable and the fact that it minimizes the error on parameter estimation. Its main drawback is its computational cost, since te evaluation of eq.(7.71) or of eq.(7.72) involves a multi-dimensional Integral over the space of $\theta$ variables which,as we have seen,could have A dimensionality of order 15 or larger,and furthermore at each point f this parameter space we must compute the function $p ( \theta | s )$ ，given in eq. (7.65),which requires the numerical computation of the integral wer frequencies that defines the scalar product（|).The choice of the best estimator is therefore subject to yarious considerations,including computational cost,and depends on the specifc situation. The use of the Bayes estimator goes also under the name of non-linear filtering.

Of course,in the limit of large signal-to-noise ratio (which unfortu-Iately is not expected to be the appropriate one for GW detectors,at least in the near future) these issues becomes irrelevant,and all consistent estimators give the same answer. In this limit,there is also very simple expression for the error on the parameters.If the SNR is large,the error that we make on the parameter estimation is small.For simplicity we assume that the prior $p ^ { ( 0 ) } ( \theta )$ is nearly uniform near $\theta = \hat { \theta }$ where $\hat { \theta }$ is the value produced py (any) consistent estimator,say for definiteness the maximum likelihood estimator $\hat { \theta } _ { \mathrm { M L } }$ . That is, we assume that the prior information is irrelevant for reconstructing the parameters.In eq.(7.65） we can then write $\theta ^ { i } = \hat { \theta } _ { \mathrm { M L } } ^ { i } + \Delta \theta ^ { i }$ ，and,since $\Delta \theta ^ { i }$ is small,we can expand the exponential in eq.(7.65) in powers of $\Delta \theta ^ { \ i }$ , The linear term of the expansipn vanishes because $\hat { \theta } _ { \mathrm { M L } } ^ { i }$ is, by definition. the maximum of the distribution,and to quadratic order in $\Delta \theta$ we get

$$
p ( \theta | s ) = N \exp \left\{ - \frac 1 2 \Gamma _ { i j } \Delta \theta ^ { i } \Delta \theta ^ { j } \right\} ,
$$

where $\Gamma _ { i j } = ( \partial _ { i } \partial _ { j } h | h - s ) + ( \partial _ { i } h | \partial _ { j } h )$ .Observe that,in the first term. we have $h - s = - n$ and,in the limit of large signal-to-noise ratio, $| n |$ is much smaller than $| h |$ . So in this limit the first term can be neglected. and we get

$$
\Gamma _ { i j } = ( \partial _ { i } h | \partial _ { j } h ) ,
$$

evaluated at $\boldsymbol { \theta } = \hat { \theta } _ { \mathrm { M L } }$ .This is called the Fisher information matriz Then the expectation value of the errors $\Delta \theta ^ { i }$ are given by

$$
\langle \Delta \theta ^ { i } \Delta \theta ^ { j } \rangle = ( \Gamma ^ { - 1 } ) ^ { i j } .
$$

# 7.4.3Matched filtering statistics

As we have discussed in the previous sections,a general data analysis strategy consists in performing matched filtering,applying many difer ent templates $h ( t ; \theta )$ to the data. This will result in the generation of a list of “events”(in the sense of Note 2on page 337),defined by the fact that the signal-to-noise ratio,in correspondence with some template raises over a predetermined threshold.Applying the maximum likeli hood criterium (or the maximization of the posterior probability, if we want to include prior information),we can then get the most probable value of the parameters $\theta$ ,under the hypothesis that a GW signal $h ( t ; \theta )$ was present. The issue that we want to address now is the following How well such hypothesis performed? In other words,what is the statistical significance of the fact that we found events at a given level of signal-to-noise ratio?

The answer to this question depends crucially on the statistical prop erties of the noise so,first of all,it is important to realize that in any detector we can distinguish between two kinds of noise:“well-behaved" Gaussian noise,whose probability distribution is a Gaussian,and non-Gaussian noise,which is a generic denomination for anything else. Gaussian distribution $\sim e ^ { - x ^ { \frac { \ d } { 2 } } / 2 }$ drops very fast for large values of its argument $\boldsymbol { \mathscr { x } }$ .The intuitive idea,that we will formalize below,is therefore to eliminate Gaussian noise by setting a suffciently large threshold for the signal-to-noise ratio.Non-Gaussian disturbances,however,have in general a totally different statistical distribution, characterized by long tails at large values of $S / N$ ,which decay only as a power law.26

These noises cannot be eliminated just by setting a high threshold, since they can produce events with values of $S / N$ that,in Gaussian distribution,would be inconceivably large.As a limiting case,any detector shaken by an earthquake will produce“events”with arbitrarily high values of $S / N$ . Of course,these events cannot be eliminated just by setting a high threshold in $S / N$ .Rather, they should be identified and vetoed. All detectors are equipped with sensors which monitor various aspects of the detector performance as well as environmental conditions (e.g. seismometers),so that non-Gaussian disturbances are vetoed as much as possible. However,it is practically impossible to be sure that one has identified and vetoed all possible non-Gaussian disturbances. So, while in principle one can study experimentally the noise distribution and then set a threshold so high that even non-Gaussian fluctuations would be very rare,in practice this is not possible because the resulting threshold would be much too high,and therefore would considerably degrade the sensitivity of the detector. Rather,the best way of eliminating non-Gaussian noise is to perform coincidences between two or more detectors.This is among the reasons why various different detectors have been built,and they are operated as a network.

In the following,we first discuss the statistical significance of obtaining a given value of the signal-to-noise ratio $S / N$ ，assuming that only Gaussian noise is present.This will tell us how to fix the threshold in $\hat { s } / N$ so that,at some confidence level,we know that higher values of $\ S / N$ have not been produced by Gaussian noise alone,and allows us to generate,from the data stream of the detector,a list of “events”.These events will then be subject to further scrutiny,using for instance coincilences between detectors whenever possible, with the aim of eliminating those which are due to non-Gaussian noise,and retaining the GW sig-Ials,if any. For the rest of this section we will be concerned only with Gaussian noise,while coincidences and other techniques will be discussed when we examine the various type of signals,in Sections 7.5-7.8.

In eqs.(7.42)-(7.45) we defined the signal-to-noise ratio in terms of ihe expectation value of the signal.Here however we want to study the mll statistical distribution,rather than just its expectation value, so we lefine

where $\hat { s }$ is the filtered output defined in eq. (7.41) and $N$ is given in . (7.43),that is $N$ is the root-mean-square (rms) of $\hat { s }$ when the signal sabsent.The definition of $\rho$ is therefore analogous to the definition of the signal-to-noise ratio $S / N$ ,see eqs.(7.42)-(7.45),except that in the merator we have $\hat { s }$ rather than its expectation value $\left. \hat { s } \right.$ . As a result,

$$
\rho = \frac { \hat { s } } { N } ,
$$

26For instance,a large class of phe nomena,characterized by what is called self-organized criticality,are such that the number $N$ of events that release an energy $\boldsymbol { E }$ is distributed as $d N =$ $E ^ { - \gamma } d E$ where,quite remarkably,the exponent $\gamma$ has approximately the same universal value, $\gamma \simeq 1 . 6$ ,in phenomena apparently very different.Such a law, together with the value $\gamma \simeq 1 . 6$ isin fact observed in earthquakes from different seismic faults (in which case it is called the Gutenberg-Richter law), in soft $\gamma \mathrm { . }$ -ray bursts from highly magnetized neutron stars,as well as in numerical simulations of fractures in solids. The same distribution is experimentally observed when searching for short bursts in resonant-bar GW detectors, where they are likely due to microfractures inside the bar,and give an example of the non-Gaussian noise that we will have to fight.See Dubath, Foffa,Gasparini,Maggiore and Sturani (2005),and references therein.

the relation between $\rho$ and $S / N$ is $S / N = \langle \rho \rangle$ From

$$
\hat { s } = \int _ { - \infty } ^ { \infty } d t \left[ h ( t ) + n ( t ) \right] K ( t )
$$

we see that, when $h$ is absent $\rho$ is a random variable with zero average and,since it has been normalized to its own rms,with variance equal to one.Thus,in the absence of $_ \mathrm { a }$ GW signal, the probability distribution of $\rho$ is

$$
p ( \rho | h = 0 | ) d \rho = { \frac { 1 } { \sqrt { 2 \pi } } } e ^ { - \rho ^ { 2 } / 2 } d \rho .
$$

In contrast,if in the output there is a GW signal $h$ with a signal-to-noise ratio $\bar { \rho }$ eqs.(7.76)and (7.77) give $\rho = \bar { \rho } { + } \hat { n } / N$ ,where $\begin{array} { r } { \hat { n } = \int d t n ( t ) K ( t ) . } \end{array}$ Since $N$ is just the rms of $\hat { n }$ ,in this case $\rho - \bar { \rho }$ is a Gaussian variable with zero mean and unit variance, so

$$
p ( \rho | \bar { \rho } ) d \rho = \frac { 1 } { \sqrt { 2 \pi } } e ^ { - ( \rho - \bar { \rho } ) ^ { 2 } / 2 } d \rho .
$$

![](images/bce7c508bf9e8c2cd1b9735940f0529092a368948b84bb99d0be9480d17252da.jpg)  
Fig.7.5 The probability distribution $P ( R | \bar { R } )$ ,as a function of $R$ for $\bar { R } = 2 0$ (solid line), $\bar { R } = 3 0$ (dotted line)and $\bar { R } = 5 0$ (dot-dashed line).

The variable $\rho$ is the signal- $^ { \mathrm { t p } }$ -noise ratio in amplitude. It is useful to introduce also $R \equiv \rho ^ { 2 }$ ,which is the signal-to-noise ratio in energy,since the energy of GWs is quadratic in the GW amplitude. Observe that $\rho$ ,being proportional to $h ( t )$ ,is not positive definite,and runs between $- \infty$ and $+ \infty$ ，while of course $0 \leqslant R < \infty$ . The probability distribution for $R$ ，when there is in the output a GW signal with a signal-to-noise ratio in energy $\bar { R } = \bar { \rho } ^ { 2 }$ ,follows from eq.（7.79) observing that a single value $R$ is obtained from two values of the amplitude, $\rho = \pm \sqrt { R }$ ,sothe probability of detecting an eyent with SNR in energy between $R$ and $R + d R$ ,when the SNR of the GW signal is $\bar { R }$ , is given by

$$
P ( R | \bar { R } ) d R \bumpeq p ( \rho | \bar { \rho } ) d \rho + p ( - \rho | \bar { \rho } ) d \rho ,
$$

evaluated at $\rho = R ^ { 1 / 2 }$ Writing $d \rho = d R / ( 2 R ^ { 1 / 2 } )$ , we get

$$
\begin{array} { c } { { P ( R | \bar { R } ) d R = \displaystyle \frac { d R } { 2 \sqrt { R } } \displaystyle \frac { 1 } { \sqrt { 2 \pi } } ~ \left[ e ^ { - ( \rho - \tilde { \rho } ) ^ { 2 } / 2 } + e ^ { - ( \rho + \bar { \rho } ) ^ { 2 } / 2 } \right] } } \\ { { = \displaystyle \frac { 1 } { \sqrt { 2 \pi \bar { R } } } e ^ { - ( \bar { R } + R ) / 2 } \cosh \left[ \sqrt { R \bar { R } } \right] ~ d R . } } \end{array}
$$

From this we can compute the average value of $R$ for a given $\bar { R }$ ，

$$
\langle R \rangle = \int _ { 0 } ^ { \infty } d R R P ( R | \bar { R } ) = 1 + \bar { R } .
$$

If we write $R = E / k T _ { n }$ ,where $\left| T _ { n } \right|$ has the physical meaning of an efective temperature of the noise after matched filtering,we can also rewrite eq. (7.82) as

$$
\langle E \rangle = k T _ { n } + { \bar { E } } .
$$

Therefore the average value of the detected energy is the sum of the energy $\bar { E }$ deposited in the detector by the GW,plus theenergy $k T _ { n }$ associated to the detector noise,a very natural result.In Fig.7.5 we show the form of the probability distribution $P ( R | \bar { R } )$ ，asa function of $R$ ，for different values of $\bar { R }$ .Observe that,while the average value isat $R = 1 + \bar { R }$ ，the maximum of the distribution is at a somewhat lower value. The corresponding distribution for R in the absence of signal is obtained setting $\bar { R } = 0$ in eq (7.81).In Fig.7.6 we compare the probability distribution $P ( R | \bar { R } )$ when $\bar { R } = 1 0$ with the probability distribution in the absence of signal, $P ( R | \bar { R } = 0 )$

The different behavior of the two distributions suggest that，when searching for a signal with a signal-to-noise ratio $\bar { R }$ in energy,we can discriminate a true GW signal from a fluctuation due to Gaussian noise settinga threshold in $R$ ,atavalue $R _ { t }$ that eliminates most of the noise, while retaining a large fraction of the signal distribution.Observe that anyway there will always bea false alarm probability,given by

$$
\begin{array} { l } { \displaystyle p _ { \mathrm { F A } } = \int _ { R _ { t } } ^ { \infty } d R P ( R | \bar { R } = 0 ) } \\ { \displaystyle \quad = 2 \int _ { \rho _ { t } } ^ { \infty } d \rho \ : \mathrm { e } ^ { - \rho ^ { 2 } / 2 } } \\ { \displaystyle \quad = 2 \mathrm { e r f c } \left( \rho _ { t } / \sqrt { 2 } \right) , } \end{array}
$$

where erfc $( z )$ is the complementary error function.Furthermore,there is a false dismissal probability,i.e.aprobability of losing a real GW signal, given by27

![](images/68dad36e2cc72a80cf582c930083bf06277dbec0158cc40de04e9786cbac2596.jpg)  
Fig.7.6 The probability distribution $P ( R | \bar { R } )$ ，asa function of $R$ ， for $\bar { R } = 1 0$ (solid line),compared to the probability distribution in the absence of signal, $P ( R | \bar { R } = 0 )$ (dashed).

$$
p _ { \mathrm { F D } } = \int _ { 0 } ^ { R _ { t } } d R P ( R | \bar { R } ) .
$$

The threshold $R _ { t }$ can be fixed deciding|what is the maximum false alarm level that we are willing to tolerate.This depends also crucially on the number of trials that we do with different templates.For example,for $\mathfrak { A }$ coalescing binary,one can estimate that of order $1 0 ^ { 5 }$ templates might be needed to cover with good accuracy the possible range of values of masses and spins.Furthermore,to match the template to the signal one can estimate in about $3 ~ \mathrm { m s }$ the maximum temporal mismatch between the two.In one year of data (\~ 3× 107s),one must therefore try \~ 1010 starting values of time,and for each value of time we have 1o5 templates to cover the masses and spin parameters,so overall one might have to ry1015 templates.28 Often thefalse alarm level is fixed so that the expected number of false alarms ina run will be of order a few.With a lower threshold one would be flooded by spurious events,while higher threshold have of course the effect of imcreasing the false dismissal probability.The few events obtained will then be subject to further scrutiny. Thus,if we search for a coalescence in a single detector,with one year of data and $1 0 ^ { 1 5 }$ templates,we could chose a threshold in amplitude $p _ { 1 } \simeq 8$ since this gives $p _ { F A } \sim 2 . 5 \times 1 0 ^ { - 1 5 }$ .However,performing coincidences between two detectors the probability of obtaining a false alarm simultaneously in the two detectors isthe square of the single-detector probability,if the noise in the two detectors are uncorrelated,so in this case we might want $[ 2 \mathrm { e r f c } ( \rho _ { t } / \sqrt { 2 } ) ] ^ { 2 } \cong 1 0 ^ { - 1 5 }$ ,which gives $\rho _ { t } \simeq 5 . 5$

$^ { 2 7 } \mathrm { { I n } }$ other words, whatever the value of $\bar { R }$ ,the distribution $P ( R | \bar { R } )$ is such that there is always some probability that $R$ be smaller,and even much smaller, than $\bar { R }$ ，and therefore the GW can go undetected even when the threshold $R _ { t }$ was smaller than the value $\bar { R }$ due to the GW alone.If one thinks in terms of energies,it might be counterintuitive that the energy released inside the detector can be smaller than the value that would have been released by the GW alone,in the absence of noise.Recall however that GW detectors really measure an oscillation amplitude,and the amplitude induced by the GW combines with the amplitude induced by noise with a relative phase, so noise and signal can interfere constructively or destructively. In the latter case the overall output has a smaller energy than that due to the GW signal alone.

28 We willsee however in Section 7.7.1 that all these time shifts can be taken into account simultaneously performing a single Fast Fourier Transform, which makes the problem computationally feasible.

29We reserve thecapital letter P for the distribution inenergy,i.e.in $R$ and use $\mathcal { p }$ for the distribution in amplitude, i.e. in $\rho$

In the above discussion,we assumed that the output of the detector is a single quantity $\rho$ which,in the absence of noise,has a Gaussian distribution. Actually,we will meet below examples in which we have two outputs $x , y$ ,each one with its Gaussian noise,which are combined in quadrature, so that $\rho ^ { 2 } = x ^ { 2 } + y ^ { 2 }$ In this case the corresponding distribution function can be computed as follows.For the distribution $p _ { 2 } ( \rho | h = 0 )$ in the absence on signal (where the label 2 reminds us that we have two degrees of freedom $x , y )$ ,29 we simply have

$$
\begin{array} { c } { { p _ { 2 } ( x , y | h = 0 ) d x d y = \displaystyle \frac { d x } { ( 2 \pi ) ^ { 1 / 2 } } \displaystyle \frac { d y } { ( 2 \pi ) ^ { 1 / 2 } } e ^ { - ( x ^ { 2 } + y ^ { 2 } ) / 2 } } } \\ { { = \rho d \rho \displaystyle \frac { d \theta } { 2 \pi } e ^ { - \rho ^ { 2 } / 2 } . } } \end{array}
$$

If we are not interested in the phase $\theta$ we simply integrate over it,and we get

$$
p _ { 2 } ( \rho | h = 0 ) = \rho e ^ { - \rho ^ { 2 } / 2 } ,
$$

which is called a Rayleigh distribution,or a $\chi ^ { 2 }$ distribution with two degrees of freedom. To compute the distribution in presence of signal we start from the probability distribution of $x , y$ ，given that the true GW signal has the values $x , { \bar { y } }$

$$
p _ { 2 } ( x , y | \bar { x } , \bar { y } ) d x d y \vert = \frac { 1 } { 2 \pi } e ^ { - \frac { 1 } { 2 } [ ( x - \bar { x } ) ^ { 2 } + ( y - \bar { y } ) ^ { 2 } ] } .
$$

We pass to polar coordinates, $x = \rho \cos \theta$ $y = \rho \sin \theta$ with $\rho ^ { 2 } = R$ s0 $d x d y = \rho d \rho d \theta = ( 1 / 2 ) d R d \theta$ To obtain the probability distribution $P _ { 2 } ( R | \bar { R } )$ we integrate over the phase $\theta$ ，and we also integrate over all the values of $\bar { x } , \bar { y }$ with the constraint $\bar { x } ^ { 2 } + \bar { y } ^ { 2 } = \bar { R }$ ,that is,

$$
\begin{array} { c } { { \displaystyle P _ { 2 } ( R | \bar { R } ) d R = c \frac { d R } { 2 } \int _ { 0 } ^ { 2 \pi } d \theta \int _ { - \infty } ^ { \infty } d \bar { x } d \bar { y } \delta ( \bar { x } ^ { 2 } + \bar { y } ^ { 2 } - \bar { R } ) } } \\ { { \displaystyle ~ \times \frac { 1 } { 2 \pi } \exp \{ - \frac { 1 } { 2 } [ ( x - \bar { x } ) ^ { 2 } + ( y - \bar { y } ) ^ { 2 } ] \} , } } \end{array}
$$

where $c$ is a normalization constant. The integrals are easily performed expressing also $x , { \bar { y } }$ in polar coordinates, $\bar { x } = r \cos \theta ^ { \prime }$ ， $\bar { y } = r \sin \theta ^ { \prime }$ ，so

$$
\begin{array} { l } { { \displaystyle P _ { 2 } ( R | \bar { R } ) = \mathrm { c o n s t . } \int _ { 0 } ^ { 2 \pi } d \theta \int _ { 0 } ^ { 2 \pi } d \theta ^ { \prime } \int _ { 0 } ^ { \infty } d ( r ^ { 2 } ) \delta ( r ^ { 2 } - \bar { R } ) } } \\ { { \displaystyle \quad \times \exp \{ - \frac { 1 } { 2 } ( R + \bar { R } ) + \sqrt { R \bar { R } } \cos ( \theta - \theta ^ { \prime } ) \} } } \\ { { \displaystyle \quad = \mathrm { c o n s t . } e ^ { - ( R + \bar { R } ) / 2 } \int _ { 0 } ^ { 2 \pi } d \alpha e ^ { \sqrt { R R } \cos \alpha } , } } \end{array}
$$

where $\alpha = \theta - \theta ^ { \prime }$ . The integral oyer $\alpha$ gives a modified Bessel function $I _ { 0 }$ Wefix the normalization constant requiring that $\begin{array} { r } { \int _ { 0 } ^ { \infty } P _ { 2 } ( R | \tilde { R } ) d R = 1 } \end{array}$ and we get

$$
P _ { 2 } ( R | \bar { R } ) = \frac { 1 } { 2 } e ^ { - ( R + \bar { R } ) / 2 } I _ { 0 } \left( \sqrt { R \bar { R } } \right) .
$$

More generaly $\rho ^ { 2 } = x _ { 1 } ^ { 2 } + . . . x _ { n } ^ { 2 }$ ，peringatioirt that presented above one finds30

$$
P _ { n } ( R | \bar { R } ) = \frac { 1 } { 2 } \left( \frac { R } { \bar { R } } \right) ^ { ( n - 2 ) / 4 } e ^ { - ( R + \bar { R } ) / 2 } I _ { \frac { n } { 2 } - 1 } \left( \sqrt { R \bar { R } } \right) .
$$

In Fig.7.7 we show the function $P ( R | { \bar { R } } )$ given in eq.(7.81)，which is appropriate for the case of a single degree of freedom,together with the functions $P _ { n } ( R | \bar { R } )$ for $n = 2$ and $n = 1 0$ degrees of freedom,as obtained from eq. (7.92). These distribution functions are known as the noncentral chi-squared densities with $n$ -degrees of freedom.The average value of $R$ with $n$ degrees of freedom is

$$
\begin{array} { c } { { \displaystyle \langle R \rangle = \int _ { 0 } ^ { \infty } d R R P _ { n } ( R | \bar { R } ) = n + \bar { R } , } } \\ { { \displaystyle \langle E \rangle = n ( k T _ { n } ) + \bar { E } , } } \end{array}
$$

and therefore

30See,e.g.McDonough and Whalen (1995), Sections 4.8 and 4.9.

![](images/b01a85059a9fa919b8f841f2b744d6ee927255d7a886ae2fed39c66b6d369873.jpg)  
Fig.7.7 The probability distribution $P ( R | \bar { R } )$ given in eq. (7.81) (solid line） compared to $P _ { n } ( R | \bar { R } )$ with $n = 2$ (dashed line) and with $n = 1 0$ (dot-dashed),as a function of $R$ ,for $\bar { R } = 3 0$

$$
\langle R ^ { 2 } \rangle - \langle R \rangle ^ { 2 } = 2 n + 4 \bar { R } .
$$

# 7.5 Bursts

while the variance is given by

We now begin to apply the general theory that we have developed,to specific classes of GW signals.We begin with GW bursts.A number of astrophysical phenomena,like supernova explosions or the final merging of a neutron star-neutron star binary system,can liberate a large amount of energy in GWs ina very shdrt time,typically less thana second,and sometimes as small as few milliseconds.We will refer to such signals as GW bursts,and we denote their duration by $\tau _ { g }$ In Fourier space,a GW burst therefore has a continuum spectrum of frequency over a broad range,up to a maximum frequency $f _ { \mathrm { m a x } } \sim 1 / \tau _ { g }$

# 7.5.1 Optimal signal-to-noise ratio

In principle, if we know the form of $\tilde { h } ( f )$ ，we can just plug it into eq.(7.51) to obtain the $S / N$ for a given noise spectral density of the detector.However,bursts come from|explosive and complicated phenomena,and it is very difficult to predict accurately their waveform. We can first of all make some simple order-of-magnitude estimates, distinguishing two cases.

# Narrow-band detectors

In this case the detector is sensitive only to frequencies in a bandwidth $\Delta f$ centered around a frequency $f _ { 0 }$ ，and we assume that $\Delta f$ is small with respect to the typical variation scale of the signal in frequency space.

Outside this interval,the detector is blind and $1 / S _ { n } ( f )$ in eq. (7.51) be comes practically zero. Inside this small bandwidth $h ( f )$ cannot chang much,so our ignorance of the precise waveform becomes irrelevant,an in the integrand in eq. (7.51) we can approximate $\tilde { h } ( f )$ with $\tilde { h } ( f _ { 0 } )$ .Then eq.(7.51) becomes

$$
\left( \frac { S } { N } \right) ^ { 2 } \simeq 4 | \tilde { h } ( f _ { 0 } ) | ^ { 2 } \frac { \Delta f } { S _ { n } } ,
$$

31As we willseeinChapter 8, the bandwidth of resonant-mass detectors has subsequently evolved，reaching values of order $\Delta f / f _ { 0 } \sim 0 . 1$ ,but still,in a first approximation,eq.(7.96)applies. We will also see that,for resonant-mass detectors, $S _ { n } ( f )$ is not at all a slowly varying function of $f$ around the resonance frequency $f _ { 0 }$ ，so in the estimate (7.96) we must really take an average of $1 / S _ { n } ( f )$ over the whole useful bandwidth $\Delta f$ ，and we cannot simply use $1 / S _ { \mathfrak { n } } ( f _ { 0 } )$

where $1 / S _ { n }$ is an average value of $1 / S _ { n } ( f )$ in a bandwidth $\Delta f$ centered on $f _ { 0 }$ .This was the typical situation of resonant mass detectors unti the 1990s,when the bandwidth $\Delta f$ was only of order a few $\mathrm { H z }$ ,around a frequency $f _ { 0 } \sim 1 ~ \mathrm { k H z }$ .31

# Broad-band detectors

In this case we get the signal in a bandwidth $( f _ { \operatorname* { m i n } } , f _ { \operatorname* { m a x } } )$ where $f _ { \mathrm { m a x } } |$ is the maximum frequency contained in the burst,if the detectori sensitive up to $f _ { \mathrm { m a x } }$ ,or otherwise is the maximum frequency to whicl the detector is sensitive.The detailed form of the signal is therefore important, but a first order-of-magnitude estimate can stillbe obtaine writing eq. (7.51) as

$$
\left( \frac { S } { N } \right) ^ { 2 } \sim 4 | \tilde { h } | ^ { 2 } \frac { f _ { \mathrm { m a x } } } { S _ { n } } ,
$$

where $\tilde { h }$ is a characteristic value of $\tilde { h } ( f )$ over the detector bandwidth and $S _ { n }$ is a characteristic value of $S _ { n } ( f )$

We can translate these order-of-magnitude estimates into limits on the value of the dimensionless GW amplitude $h ( t )$ that can be measured For this we assume for definitehess that the wave comes from a direction such that $F _ { + } = 1$ and $F _ { \times } = 0$ so that $h ( t )$ is the same as the amplitude $h _ { + } ( t )$ of the $^ +$ polarization. In the most general situation,we wil also have a factor which depends on $F _ { + }$ and $F _ { \times }$ and reflects the sensitivity of the detector to the given direction and polarization of the wave. To express eq.(7.51) in terms of $\dot { h } ( t )$ we need a model for the signal. Fora GW burst of amplitude $h _ { 0 }$ and duration $\tau _ { g }$ ,a crude choice could be

$$
h ( t ) = \ h _ { 0 } \quad \mathrm { i f } \ | t | < \tau _ { g } / 2
$$

and $h ( t ) = 0$ if $| t | > \tau _ { g } / 2$ . We can write it more compactly as

$$
h ( t ) = h _ { 0 } \tau _ { g } \delta _ { \mathrm { r e g } } ( t ) ,
$$

where $\delta _ { \mathrm { r e g } } ( t )$ has a rectangular shape of unit area, $\delta _ { \mathrm { r e g } } ( t ) = 1 / \tau _ { g }$ for $| t | < \tau _ { g } / 2$ and $\delta _ { \mathrm { r e g } } ( t ) = 0$ for $| | t | > \bar { \tau } _ { g } / 2$ For $\tau _ { g }  0$ $\delta _ { \mathrm { r e g } } ( t )$ becomes a Dirac delta.More generally, for a burst we can model $h ( t )$ asin eq. (7.99), choosing for $\delta _ { \mathrm { r e g } } ( t )$ a smooth function of unit area which goes to zero rather fast for $| t | \gtrsim \tau _ { g }$ Performing the Fourier transform this gives

$$
| \tilde { h } ( f ) | \sim h _ { 0 } \tau _ { g } ,
$$

times a dimensionless function of the frequency，numerically of order one,and whose details depend on the precise waveform $\delta _ { \mathrm { r e g } } ( t )$ chosen.

Actually,rather than using a functionl $\delta _ { \mathrm { r e g } } ( t )$ with a unit area,it can be more convenient to write $h ( t ) ~ = ~ h _ { 0 } g ( t )$ ，with $g ( t )$ some function peaked at $t = 0$ and with $g ( 0 ) = O ( 1 ) ,$ so that the value of $h ( t )$ near the peak is of order $h _ { 0 }$ (rather than $h _ { 0 } \delta _ { \mathrm { r e g } } ( 0 )$ as in eq. (7.99)).A simple waveform of this type is a Gaussian,

$$
h ( t ) = h _ { 0 } e ^ { - t ^ { 2 } / \tau _ { g } ^ { 2 } } ,
$$

whose Fourier transform is

$$
\tilde { h } ( f ) = h _ { 0 } \tau _ { g } \sqrt { \pi } e ^ { - ( \pi f \tau _ { g } ) ^ { 2 } } .
$$

A $f _ { 0 }$ sape isa sn aus

$$
h ( t ) = h _ { 0 } \sin ( 2 \pi f _ { 0 } t ) e ^ { - t ^ { 2 } / \tau _ { g } ^ { 2 } } ,
$$

shown in Fig.7.8. Its Fourier transformis

$$
\tilde { h } ( f ) = h _ { 0 } \tau _ { g } i \frac { \sqrt { \pi } } { 2 } \left[ e ^ { - \pi ^ { 2 } ( f - f _ { 0 } ) ^ { 2 } \tau _ { g } ^ { 2 } } \right. \left. e ^ { - \pi ^ { 2 } ( f + f _ { 0 } ) ^ { 2 } \tau _ { g } ^ { 2 } } \right] ,
$$

and is shown in Fig. 7.9.If $4 \pi ^ { 2 } f _ { 0 } ^ { 2 } \tau _ { g } ^ { 2 } \gg 1$ ，near $f = f _ { 0 }$ the second term in brackets is negligible with respect to the first (while close to $\scriptstyle f = 0$ it cancels the first term so that $\tilde { h } ( 0 ) = 0$ ),andwe basically have a Gaussian in frequency space,centered at $f = f _ { 0 }$ ,and with a value at the maximum

$$
| \tilde { h } ( f _ { 0 } ) | \simeq h _ { 0 } \tau _ { g } \Big | { \frac { \sqrt { \pi } } { 2 } } .
$$

Writing $f = f _ { 0 } { + } \Delta f$ we see that the width of the maximum $\Delta f$ is of order $1 / ( \pi \tau _ { g } )$ ,s0 $\Delta f / f _ { 0 } \sim 1 / ( \pi f _ { 0 } \tau _ { g } )$ .For $\pi f _ { 0 } { \bar { \tau } } _ { g } \ll 1$ ， $\tilde { h } ( f )$ becomes relatively fat while for $\pi f _ { 0 } \tau _ { g } \gg 1$ it is sharply peaked around $f _ { 0 }$ . Using eqs. (7.96) and (7.97) we can estimate the minimum value of the dimensionless GW amplitude $h _ { 0 }$ that can be detected at a given level of the signalto-noise ratio $S / N$ .For narrow-band detectors eq.(7.96) gives,using for definiteness the value $| \tilde { h } ( f _ { 0 } ) | \simeq h _ { 0 } \tau _ { g } \vert ( \sqrt { \pi } / 2 )$ appropriate for a sine-Gaussian waveform,

$$
( h _ { 0 } ) _ { \mathrm { m i n } } \sim \frac { 1 } { \tau _ { g } } \left( \frac { S _ { n } } { \pi \Delta f } \right) ^ { 1 / 2 } ( S / N ) ,
$$

while for broad-band detectors eq. (7.97) gives

The precise numerical factors,of course,depend on the choice of the waveform, so to fix the numerical coefficients in eqs.(7.1o6) and (7.107)

![](images/70a5cc04e1fd5808444d08866c9cad19b29253d1ca2a1ea90ed461d287249bc5.jpg)  
Fig.7.8 The sine-Gaussian function $\sin ( 2 \pi f _ { 0 } t ) e ^ { - t ^ { 2 } / \tau _ { g } ^ { 2 } }$ ,for $\tau _ { g } = 3$ ms and $f _ { 0 } = 5 0 0 ~ \mathrm { H z }$ ,as a function of $t$ (in seconds).

![](images/2ec54d17d07db38bd4f5909bbdf33469f676d7537b4b974cb1ff5ad0436400ad.jpg)  
Fig. 7.9 $| \tilde { h } ( f ) |$ (in units of $h _ { \mathrm { 0 } }$ ）fora sine-Gaussian function with $f _ { 0 } =$ $5 0 0 ~ \mathrm { H z }$ $\tau _ { g } = 3 ~ \mathrm { m s }$ (solid line） andfora sine-Gaussian function with$f _ { 0 } ~ = ~ 5 0 0 ~ \mathrm { H z }$ ， $\tau _ { g } ~ = ~ 1 ~ \mathrm { m s }$ (dashedline).

we must know the shape of the signal $\tilde { h } ( f )$ ,use the exact form of the noise $S _ { n } ( f )$ ,and perform the integnal in eq. (7.51). We see from eqs. (7.106 and(7.1o7） that in a narrow-band detector the minimum detectabl amplitude is higher by a factor $( f _ { \operatorname* { m a x } } / \Delta f ) ^ { 1 / 2 }$ ， compared to a detector which is able to maintain the same typical sensitivity $S _ { n }$ over a broad bandwidth. This reflects the fact that the narrow-band detector has access only to a portion of the Fourier modes of the burst.

Rather than expressing the result in terms of $h _ { 0 }$ , it is also common to use the so-called root-sum-square (rss) amplitude $h _ { \mathrm { r s s } }$ ,defined by

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle h _ { \mathrm { r s s } } ^ { 2 } = \int _ { - \infty } ^ { \infty } d t h ^ { 2 } ( t ) } } \\ { { } } & { { } } & { { = \displaystyle \int _ { - \infty } ^ { \infty } d f | \tilde { h } ( f ) | ^ { 2 } . } } \end{array}
$$

For the Gaussian (7.101) we have

$$
h _ { \mathrm { r s s } } ^ { 2 } = h _ { 0 } ^ { 2 } \tau _ { g } \sqrt { \frac { \pi } { 2 } } , ( \mathrm { G a u s s i a n } ) ,
$$

32In the computation,we neglect the term $\exp \{ - \pi ^ { 2 } ( f { \bf \Phi } + f _ { 0 } ) ^ { 2 } \tau _ { g } ^ { 2 } \}$ in eq.(7.104),which is small with respect to $\exp \{ - \pi ^ { 2 } ( f \ - \ f _ { 0 } ) ^ { 2 } \tau _ { g } ^ { 2 } \}$ and，when we integrateeq.(1.159)over $d f$ ，we replace $f ^ { 2 } \exp \{ - \pi ^ { 2 } ( f - f _ { 0 } ) ^ { 2 } \tau _ { q } ^ { 2 } \}$ with $f _ { 0 } ^ { 2 } \exp \{ - \pi ^ { 2 } ( f - f _ { 0 } ) ^ { 2 } \tau _ { g } ^ { 2 } \}$ and we extend the resulting integral from $- \infty$ to $+ \infty$ while,for the sine-Gaussian (7.103),

$$
h _ { \mathrm { r s s } } ^ { 2 } = h _ { 0 } ^ { 2 } \tau _ { g } \sqrt { \frac { \pi } { 8 } } \left( 1 - e ^ { - 2 \pi ^ { 2 } f _ { 0 } ^ { 2 } \tau _ { g } ^ { 2 } } \right) , \ ~ \ ~ \ ~ \ \mathrm { ( s i n e - G a u s s i a n ) . }
$$

Observe that， dimensionally, $\mathit { h } _ { \mathrm { r s s } } \sim ( \mathrm { t i m e } ) ^ { 1 / 2 }$ ,s0 $h _ { \mathrm { r s s } }$ is conventionaly quoted in $\mathrm { H z } ^ { - 1 / 2 }$ , as the strain sensitivity.

To have an idea of the numetical values of $h _ { \mathrm { r s s } }$ (or, equivalently, of $h _ { 0 }$ that could be obtained from astrophysical phenomena, we can compute the energy released in GWs by an event which produced,at the detector,a given value of $h _ { \mathrm { r s s } }$ .This can be obtained from the expression for $d E / d A d f$ given in eq. (1.159).Observe however that,for a wave coming from an arbitrary direction and with arbitrary polarization,a detector does_not measure directly $\smash { \tilde { h } _ { + } } \| \boldsymbol { f } )$ and $\tilde { h } _ { \times } ( f )$ but rather the combination $\tilde { h } ( f ) = F _ { + } \tilde { h } _ { + } ( f ) + \tilde { F } _ { \times } \tilde { h } _ { \times } \tilde { ( f ) }$ ,where $F _ { + , \times }$ are the detector pattern functions.For definiteness,we consider a GW coming from the optimal direction for the $^ +$ polarization, so we take $F _ { + } = 1$ and $F _ { \times } = 0$ and for $\tilde { h } _ { + } ( f )$ we take the sine-Gaussian waveform (7.104). We substitute this into eq.(1.159)and we get the total energy $\Delta E _ { \mathrm { r a d } }$ radiated by the source in GWs,32

$$
\begin{array} { l } { { \displaystyle \Delta E _ { \mathrm { r a d } } \simeq \left( \frac { \pi } { 2 } \right) ^ { 3 / 2 } \frac { \pi r ^ { 2 } c ^ { 3 } } { G } h _ { 0 } ^ { 2 } \tau _ { g } f _ { 0 } ^ { 2 } } } \\ { { \displaystyle \qquad = \frac { \pi ^ { 2 } r ^ { 2 } c ^ { 3 } } { G } h _ { \mathrm { r s s } } ^ { 2 } f _ { 0 } ^ { 2 } . } } \end{array}
$$

Inserting the numerical values,

<table><tr><td>△Erad ~1×10-2Moc²</td><td>fo 8kpc) 1kHz</td></tr><tr><td></td><td>(7.112</td></tr></table>

where in the second line we normalized $r$ to a value of order of the distance to the galactic center.Recall that in the above we assumed a wave coming from optimal direction.For an ensemble of waves with arbitrary direction and polarization,we must also take into account the average over the pattern functions of the detector. For an interferometer, this is a factor $2 / 5$ (see Table 7.1),so on average a burst coming from arbitrary direction,in order to producea givensignal $h _ { \mathrm { r s s } }$ in the detector, had an energy larger by a factor 5/2,compared to eq.(7.1l2).We see that a burst at the $\mathrm { k H z }$ with $h _ { \mathrm { r s s } } = 1 0 ^ { - 1 9 } \mathrm { H z ^ { - 1 / 2 } }$ ,carries away about $1 0 ^ { - 2 }$ solar masses in GWs,if it comes from a source located at typical galactic distances.

Taking $1 0 ^ { - 2 } M _ { \odot } c ^ { 2 }$ as a reference value for $\Delta E _ { \mathrm { r a d } }$ (which,as we will see in Vol. 2,is the maximum value that can be reasonably expected in cataclysmic events involving solar mass objects.Even larger energies can be released in the merging of very massive black holes),we see that a detector must reach at least a sensitivity to hrssOf order 10-19 Hz-1/2 to have some chance of detecting GW bursts from the galactic center. To be able to see a burst which releases $1 0 ^ { - 2 }$ solar masses in the Virgo cluster of galaxies,which is at $r \sim 1 4 \mathrm { M p c }$ 。one rather needs to be able toreach $h _ { r s s } \simeq 6 \times 1 0 ^ { - 2 3 } \mathrm { H z ^ { - 1 / 2 } }$ or,from eq. （7.110) with $\tau _ { g } = 1$ ms,a value of the dimensionless amplitude $h _ { 0 } \simeq 2 \times 1 0 ^ { - 2 1 }$

# 7.5.2 Time-frequency analysis

The matched filtering technique that we have discussed in Section 7.3 works well if we know the form of the signal,or if we can parametrize it with a limited number of free parameters,so that it becomes practically feasible to put a suficiently fine grid in this parameter space,and repeat the search for each point of the gridl As we will discuss in the next sections,this can be the case for the inspiral of compact binaries and, partly,for the signals due to pulsars.

Concerning bursts,the situation is different. In general, bursts may come from complicated explosive phenomena，such as supernovae,or from processes such as the final merging of coalescing binaries,which are diffcult to model. In a narrow-band detector,such as resonant bars, we only have access to a narrow range of Fourier components of the signal. Thus,in a first approximatipn it is reasonable to model the signalas flat in frequency,i.e.asa Dirac delta in time and,asa next step,we can use more realistic modelizations such as the Gaussian and the sine-Gaussian waveforms described above.However,in a broadband detector,the difference between these simple modelizations and the real waveform will become important．Thus,to exploit optimally the capabilities of a broad-band detector,one is lead to consider also other methods,which are sub-optimal with respect to matched filtering when the waveform is know precisely (since we have seen that,if the waveform is known,matched filteringis the optimal strategy) but might be more robust in the absence of detailed knowledge of the signal.

Such search algorithms can be obtained working in the time-frequency plane.To understand the usefulness of the time-frequency representa tion,suppose at first that we have a function $s ( t )$ defined on the whole real axis $- \infty < t < \infty$ .We can take its Fourier transform $\tilde { s } ( f )$ and com pute from it the power spectrum $| \tilde { s } ( f ) | ^ { 2 }$ . A plot of the power spectrul against the frequency will enable us to see immediately what are th dominant Fourier modes. However,this power spectrum knows nothing about when things happened.33

33The information about time localization，which is encoded in $s ( t )$ isof course still encoded in $\tilde { s } ( f )$ ，since from $\tilde { s } ( f )$ we can get back $s ( t )$ uniquely. However,it is lost in $| \tilde { s } ( f ) | ^ { 2 }$ ，since it was contained in the phase relation between the Fourier components,and this information is obliterated when taking the modulus. A nice example (taken from van den Berg (1999),a textbook on wavelets) is obtained if we take $s ( t )$ to be a classical symphony. Then its power spectrum will immediately reveal the dominating keys: the groundtones and their harmonics.Suppose now that we play the parts ina different order,and we even interchange smaller parts within the parts. The power spectrum would not change at all,while to the ear,which actually makes a time frequency analysis,the result is very different.

The simplest way to recovet partly this information is to take th Fourier transform not on the whole real line,but on segments of lengti $\delta t$ .When we Fourier transform the function $s ( t )$ on the interval $0 < t$ < $\delta t$ and we plot the resulting power spectrum,we find the Fourier mode that dominated the function,during this temporal span.We can then repeat it for $\delta t < t < 2 \delta t$ ,etc.Of course,on a finite segment of length $\delta t$ ，the resolution in frequency is finite,and is $1 / \delta t$ ， so we are giving up the fine details in frequency space, but we gain an understanding o when things happened. That is.rather than working in frequency space with an arbitrarily good resolution,it can be convenient to work in th time-frequency plane,making $\mathord { \ ? }$ good compromise between the accuracy in frequency and the accuracy in time.

This is particularly important when we are looking for transient phe nomena,such as GW bursts. Suppose that we are unable to compute ti detailed waveform of a burst,as it is typically the case,but still we cal give a reasonable estimate of its total duration $\delta t$ ,and of the frequency range $f _ { 1 } < f < f _ { 2 }$ where most of its power should be concentrated Then,a useful search strategy is as follows.

First of all, it is convenient to work in a discretize space.Recall tha the output of a detector is sampled at some rate $1 / \Delta t$ Then,we cal split the output into time segments,and inside each segment the outpu $s ( t )$ is given by the discrete set of values

$$
s _ { j } \equiv s ( t _ { \mathrm { s t a r t } } + j \Delta t ) ,
$$

where $t _ { \mathrm { s t a r t } }$ is the start time of the segment considered, $j = 0 , \ldots , N ,$ and $\delta t = N \Delta t$ is its length.We can then perform a discrete Fouric transform over the segment $\delta t$ by writing

34To fix the ideas,one can consider that the sampling rate $1 / \Delta t$ of an interferometer is typically of order $1 0 - 2 0$ $\mathrm { k H z }$ We can imagine that we are searching for bursts of duration $\delta t \ =$ $0 . 5 \ \mathrm { s } ,$ so frequency space is split into bins of width $2 \ \mathrm { ~ H z ~ }$ Restricting the search to the frequency range where interferometers are most sensitive,which corresponds to a bandwidth $\begin{array} { r l } { \Delta f } & { { } = } \end{array}$ $O ( 2 0 0 )$ $\mathrm { H z }$ around peak sensitivity，we have a total of $O ( 1 0 0 )$ bins in frequency, for each value of the start time of the segment.

$$
\tilde { s } _ { k } = \sum _ { j = 0 } ^ { N - 1 } { n } _ { j } \exp \left\{ \frac { 2 \pi i } N j k \right\} ,
$$

$$
\tilde { s } _ { k } = \sum _ { j = 0 } ^ { N - 1 } n ( t _ { j } ) \biggl \lceil \exp \bigl \{ 2 \pi i \bigl ( t _ { j } - t _ { \mathrm { s t a r t } } \bigr ) f _ { k } \bigr \} .
$$

where $t _ { j } = t _ { \mathrm { s t a r t } } + j \Delta t$ and

$$
f _ { k } = \frac { k } { N \Delta t } = \frac { k } { \delta t } .
$$

We see that frequencies are spaced by $1 / \delta t$ ,up to a maximum frequency equal to $N / \delta t$ (since eq.(7.114) is periodic under $k  k + N$ ），which of course is just the sampling frequency $1 / \Delta t$ .34 We can write as usua $s _ { i } = n _ { i } + h _ { i }$ ,where $n _ { i }$ is the noise and $h _ { i }$ a putative signal,and we define the Fourier transforms $\tilde { n } _ { k }$ and $\tilde { h } _ { k }$ as in eq. (7.114). The discrete version f eq. (7.6) is obtained replacing the Dirac delta by a Kronecker delta,

$$
\langle \tilde { n } _ { k } ^ { * } \tilde { n } _ { k ^ { \prime } } \rangle = \delta _ { k k ^ { \prime } } \frac { 1 } { 2 } S _ { k } ,
$$

where we used the short-hand notation $S _ { k } \equiv S _ { n } ( f _ { k } )$

If the only theoretical expectation|that we have about a signal is that it should have a duration $\delta t$ ，and should have most of its power in a frequency band $f _ { 1 } < f < f _ { 2 }$ ，with $f _ { 1 } = k _ { 1 } / \delta t$ ， $f _ { 2 } = k _ { 2 } / \delta t$ ，and $f _ { 2 } - f _ { 1 } \equiv \delta f$ ,we can form,for each possible start time $t _ { \mathrm { s t a r t } }$ ,the quantity

$$
\mathcal { E } = 4 \sum _ { k = k _ { 1 } } ^ { k _ { 2 } } \frac { | \tilde { s } _ { k } | ^ { 2 } } { S _ { k } } ,
$$

which is called the excess power statistic.We collect the values of $\mathcal { E }$ for all possible start time and,if we find $\mathrm { \AA }$ value above some given threshold,we record it as an event.35 To understand what is a statistically significant value of $\mathcal { E }$ ,observe that $\mathcal { E }$ is formed from $k _ { 2 } - k _ { 1 }$ independent complex variables $s _ { k }$ Since $( k _ { 2 } - k _ { 1 } ) / \delta t = f _ { 2 } - f _ { 1 } \equiv \delta f$ ,the number of independent real variables is

le.twice the area of the time-frequency plane explored. Therefore, even in the absence of any GW signal in the data,the average value of $\mathcal { E }$ is of order $ { \mathcal { N } } . ^ { 3 6 }$ This means that a real GW signal, in order to be visiblein $\mathcal { E }$ against the noise with a signal-to-noise ratio of order one, must give a contribution to $\mathcal { E }$ of order $\mathcal { N }$ From eq.(7.119), $\mathcal { N } \geqslant 2$ the uncertainty principle, in a quantum langauge） and,depending on the situation, one can have $\mathcal { N } \gg 1$ Comparing with eq.(7.51)，we see that,if we knew the waveform and we could make a matched fltering, such a signal would produce a value of $S / N$ of order $\mathcal { N } ^ { 1 / 2 }$ In other words,using the excess power statistic,we can detect with a signalt0-noiseratio of order one,a signal that with matched filtering would mergewithsignaltonoiseratioofoder $\mathcal { N } ^ { 1 / 2 }$ .37 This is not surprising since we know that, when we have the waveform,the matched filtering maximizes the signal-to-noise ratio. However,the excess power statistic mly needs very crude information about the signal, namely its duration and its typical frequency range,and is therefore much more robust. Furthermore,it can be proved that,if the only information on the signal Bits duration and its bandwith,the excess power method is the optimal one.

From the above discussion,it is clear that the method is viable only when $\mathcal { N }$ is not too large. For instance,for the inspiral phase of a coalescng NS-NS binary,as observed in a ground-based interferometer, we see Iomeq.(4.21) that the signal enters the bandwidth of the interferometer,say at $4 0 ~ \mathrm { H z }$ ,when the time to coalescence is $\tau = 2 5 \mathrm { ~ s ~ }$ and sweeps In frequency up to the $\mathrm { k H z }$ Taking $\delta f \sim 1 0 0 0 \mathrm { H z }$ and $\delta t \sim 2 5 ~ \mathrm { s }$ we get $\sim 5 \times 1 0 ^ { 4 }$ and $\mathcal { N } ^ { 1 / 2 } \sim 2 0 0$ ,so the excess power method would allow

35In the sense defined in Note 2 on page 337.

36More precisely， in the presence of Gaussian noise $\mathcal { E }$ follows a $\chi ^ { 2 }$ distribution with $\mathcal { N }$ degrees of freedom,while in the presence of signal it follows the corresponding non-central $\chi ^ { 2 }$ distribution,see eq.(7.92).

37For a more accurate estimate of the signal-to-noise ratio obtained restricting the frequency bandwidth,i.e. performinga band-pass filter，see Section II of Flanagan and Hughes (1998a).

us to detect signals only when|their signal-to-noise ratio,with matche filtering, is of order several hundreds. Thus,for inspiraling binaries,th excess power method is not at all competitive. Furthermore it is no needed, since in this case we Have precise calculations of the waveforn in the inspiral phase,as we saw in Chapter 5.

The situation is different fof the merging phase of a BH-BH coale cence.In this case the maximum value of $f$ can be estimated to b oforder $f _ { \mathrm { q n r } }$ ，where $f _ { \mathrm { q n r } }$ is the ringing frequency of the fundamenta quasi-normal mode of the black hole. To include the power radiate by the BH in its higher quasi-normal modes,an estimate of order $2 f _ { \mathrm { q } \mathrm { m } }$ could be more appropriate.Black hole normal modcs will be discussed i Vol.2,and we will see that $f _ { \mathrm { q n f } }$ can reach a maximum value (for rapidk spinning BHs of mass $m$ ） $f _ { \mathrm { q n r } } \equiv c ^ { 3 } / ( 2 \pi G m )$ .Observe that this is quit larger than the maximum frequency (4.39) at which the inspiral phas ends,so we finally take $\delta f \sim 2 f _ { \mathrm { q n r } } \sim c ^ { 3 } / ( \pi G m )$ .As for the merging time,we can roughly estimate that it should not be much larger thal $r _ { \mathrm { I S C O } } / c$ ，where $r _ { \mathrm { I S C O } } = 6 G m / c ^ { 2 }$ is the radius of the innermost stabl circular orbit in a Schwarzschild geometry，see eq. (4.38).Taking fo instance $\delta t \sim 2 r _ { \mathrm { I S C O } } / c = 1 2 G m / c ^ { 3 }$ ，we get the estimate $\mathcal { N } ^ { 1 / 2 } \sim 2 , \mathrm { s } \mathrm { o }$ the loss in sensitivity with respect to optimal filtering is not large. Thi is quite important,considering that the merging phase is very dificuh to model.38

38For fast spinning BHs the coalescence time willbe longer,since they must first shed some angular momentum before setting into their final state,in order that the angular momentum of the final BH does not exceed the maximum value allowed for rotating BHs.The estimate of $\mathcal { N }$ depends on the angular momentum of the BHs,but a typical value can be $\sqrt { \hphantom { - } 1 / 2 } \sim 5$ See Flanagan and Hughes (1998a),Section IIIE.

The time-frequency method |discussed here can be generalized in vail ous directions. One possibility is to consider wavelets.These are general izations of the Fourier transform,in which to a function $s ( t )$ is associated a function $S ( f , t _ { 0 } )$ of two parameters,of which $f$ is the frequency am $t _ { 0 }$ is the position in time of the signal,

$$
S ( f , t _ { 0 } ) \stackrel { \textstyle \perp } { = } \int _ { - \infty } ^ { \infty } \psi _ { f , t _ { 0 } } ^ { * } ( t ) s ( t ) .
$$

The simplest example consistslin taking

$$
\psi _ { f , t _ { 0 } } ( t ) = e ^ { - i f t } \psi ( t - t _ { 0 } ) ,
$$

where $\psi ( t - t _ { 0 } )$ is a window function centered around $t _ { 0 }$ .This Windowed Fourier Transform,or Gabor transform,as it is called,is essentially wha we have used above (more precisely,we used its discrete version),witi a sharp window function. Other choices of window functions,such as Gaussian,are more commonly used in signal analysis.

39In the literature on wavelets, this is actually written as $a ^ { - 1 / 2 } \psi \big ( ( t - t _ { 0 } ) / a \big )$ ， where $a$ is a dimensionless quantity that rescales a characteristic frequency implicit in the function $\psi$

A possible drawback of a choice such as eq.(7.121) is that the tem poral window has a fixed size,independently of the frequency.In mos type of signals,however, there is a correlation between the characteristi frequency of a given segment and the time duration of the segment,such that low-frequency pieces tend|to last longer.To take this into account the wavelet transform is defined by choosing a window function of th form $\psi ( f ( t - t _ { 0 } ) )$ (times a normalization constant $\sqrt { f }$ )，which depends explicitly on $f$ .39 In this way,at high frequencies the temporal windowi shorter,so we have a better time resolution.In a sense,wavelets provide a“microscope” that,at each point in time of the signal, zooms in and out,depending on the frequency scale of the signal. The other crucial property is that it is possible to choose wavelets so that they form an orthonormal basis,and the signal can therefore be decomposed uniquely into its component with respect to this wavelet basis, just as in the Fourier transform. Wavelets are by now widely used in signal analysis in many branches of science,and many possible choices of wavelets are available,depending on the problem at hand,see the Further Reading.

Another generalization of the time-frequency analysis discussed here consists in marking as “black”the bins in the time-frequency plane where an indicator such as the excess power statistic goes above a threshold value,and searching for structures of black bins,such as clusters. This is basically a variant of the Hough transform that we will discuss in Section 7.6.3,in the context of periodic signals.

# 7.5.3 Coincidences

Given that GW bursts can have a very short duration,even smaller than a millisecond, the output of ground-based detectors are sampled with a very high frequency, typically ${ \cal O } \vert ( 1 0 )$ kHz. In one year there are about $3 \times 1 0 ^ { 1 0 }$ ms, so even a fuctuation with a probability $\sim 1 0 ^ { - 1 0 }$ is bound to occur on average in one year worth of data. Then eq.(7.84) suggests,for bursts,a threshold on the amplitude signal-to-noise ratio of order $\rho _ { t } \simeq 6$ ,in order to have justa few false alarms per year in a detector. However, this only eliminate Gaussian noise.GW bursts are particularly well simulated by non-Gaussian events such as microcreeps in the materials or sudden external mechanical or electromagnetic disturbances. In some cases the external disturbance can be identified, and the corresponding event is therefore|vetoed,but in most cases this is impossible. To eliminate these non-Gaussian noise,the only possibility is to perform coincidences between different detectors.40

Using two or more detectors in coincidence is a standard practice in physics,at least since the early days of cosmic ray research.The idea is that,iftwo detectors are far apart,their noise are mostly uncorrelated,41 md the probability of an accidental coincidence is small，while a GW should excite both detectors nearly simultaneously. Below we discuss some of the issues that must be addressed in order to apply this idea to GW detectors.

# Relative orientation of the detectors

We have seen that the response of a detector to a GW depends on the tlative orientation between the detector and the source. To perform oincidences between two or more detectors,it is therefore optimal to orient them,taking into account their difference in location,so that their response to an incoming GW signal is the same,or at least as similar as possible,for all of them. Otherwise,a real signal can be missed simply because,when one detector was oriented favorably with respect to the source,the other had a very poor sensitivity for the same direction.42

40Observe that the use of coincident detectors also allows us to lower the threshold necessary for eliminating Gaussian noise,since now the false alarm probability, for uncorrelated detector noise,is the square of (7.84). For instance,in the example above,the threshold $\rho _ { t } ~ \simeq ~ 6$ valid for a singledetector search becomes $\rho _ { t } \simeq 4 . 5$ ina two-detector correlation (even neglecting all consistency check discussed below).

41With some exceptions.For example,seismic or electromagnetic disturbances might propagate from one detector's site to the other.

42On the other hand,detectors with different orientation can perform independent measurement of the signal,allowing to disentangle the polarizations and the arrival direction of the wave, see the discussion on page 342.

43This depends not only on the sampling time of the detector，but also on other factors,in particular on the signal-to-noise ratio of the event,since noise combines with the GW signal distorting and broadening its shape.

# Coincidence window

Each GW detector has its temporal resolution, which might for instance be of the order of few ms.43"Giyen two detectors,with variances $\sigma _ { 1 }$ and $\sigma _ { 2 }$ on the arrival time of their respective events, the corresponding variance in the coincidence searchlis $\hat { \sigma _ { 1 2 } } = \sqrt { \sigma _ { 1 } ^ { 2 } + \sigma _ { 2 } ^ { 2 } }$ , and therefore one can ask that the events be coincident within $k$ standard deviations $\sigma _ { \mathrm { { I 2 } } }$ (e.g. $k = 3$ can be a typical choice). To this uncertainty one must add the light travel time $( \Delta t ) _ { \mathrm { l i g h t } }$ between the two detectors since, depending on the source location,either the first or the second detector will be hit by the wavefront a time up to $( \Delta _ { t } ^ { } ) _ { \mathrm { l i g h t } }$ before the other. So finally one requires that the arrival times $t _ { 1 }$ and $t _ { 2 }$ in the two detectors are within a coincidence window

$$
\left| t _ { 1 } - t _ { 2 } \right| \leqslant ( \Delta t ) _ { \mathrm { l i g h t } } + k \left( \sigma _ { 1 } ^ { 2 } + \sigma _ { 2 } ^ { 2 } \right) ^ { 1 / 2 } .
$$

This typically results in a coincidence window of the order of a few tens of ms.

# Energy consistency

Another possible handle to discriminate between accidental coincidences and true GW signals is the compatibility of the signal in the two (or more) detectors. Ideally,if the GW signal is much larger than the noise, two detectors oriented in the same way should register the same energy fux,when a GW hits them.In contrast,two events due to noise which by chance happen simultaneously in the two detectors,should have uncorrelated energies.However,in practice,at moderate values of the signal-to-noise ratio the signal $h ( t )$ induced by the GW combines with the noise $n ( t )$ and,depending on the relative phase of these contributions,the output $h ( t ) + n ( t )$ fuctuates and can be either larger or smaller than the value that would be induced by the GW. Therefore, as we computed in Section 7.4.3,one has a probability distribution for the amplitudes (or for the energies) measured in the two detectors,and the compatibility criterion must take into account this probability distribution. This procedure also requires that the two detectors have a sufficiently reliable calibration in energy.

# Waveform consistency

A broadband detector has rather detailed information on the waveform and a consistency condition between the waveforms observed in the two detectors can be imposed. For instance, one of the algorithms used by LIGO for generating candidate eyents is based on the identification of connected regions（“clusters"） in the time-frequency plane where the power is not consistent,statistically,with Gaussian noise,as discussed in Section 7.5.2. Then each event is characterized by its bandwidth $( f _ { \operatorname* { m i n } } , f _ { \operatorname* { m a x } } )$ ,i.e.by the low and high frequency bounds of the cluster. One can then require, for instance,that the bandwidth of events in diferent detectors have an overlap,orat least that they are separated in frequency by no more than a fixed window $\Delta f$

# Background estimation

After having applied all these cuts,we can still have accidental coincidences that,by chance,passed them.However,the residual number of accidental coincidences can be estimated very reliably.First of all,one can simply predict it from the observed event rate in a single detector, assuming that the noise is stationary. But in fact the most direct estimation of the background is obtained using a shifting algorithm which, together with many other techniques used in GW research,was introduced by Weber. The procedure con\$ists simply in shifting the data streain of one detector with respect to the other by a time step significantly longer than the coincidence window,say $2 \textrm { s }$ ，and counting the mumber of coincidences obtained after shifting (subject to the same requirements on the coincidence window and energy compatibility imposed on the coincidences at zero time shift).These coincidences,of course, are now all accidental, since the shift has been chosen much larger than the coincidence window and therefore of the uncertainties in the arrival times.We then repeat the procedure with a different shift,say $4 \mathrm { ~ s ~ }$ and we count again the number of accidentals. One can repeat the procedure for many different shifts (the overall time shift must however be short compared to the time-scale over which the event rate in a single detector changes substantially).We then average over these shifts,and we have a rather accurate estimate of the average number of accidental coincidences,its variance,and more generally their distribution (which is found experimentally to be a Poisson distribution,as expected whenever we count a number of discrete independent events),and we can also study how these quantities depend on the energy of the events.

# 7.6Periodic sources

While a burst source is typically radiating only for a period of less than second,a periodic source emits continuously an almost monochromafic signal,so the limit on its observation comes from the total available observation time,which can be of order of years.Our intuitive discussion of matched filtering showed that,if we can follow a signal for a time $T$ ,the minimum level of signal that we can extract from the noise scales as $1 / T ^ { 1 / 2 }$ ,see eqs.(7.39)and (7.40). This means that,for periodic waves,we can extract from the noise a signal with an amplitude $h _ { 0 }$ mch smaller than the one that can be measured in the case of bursts. This opportunity, however,also comes at the expense of some complicalions,since we must able to track carefully the signal for a long period. We already met a similar situation in Chapter 6,where we studied the iming formula for the radio signals of pulsars,and we saw that there Ie two main issue to address: the intrinsic changes of the frequency of he source,and the modulation of the signal due to the motion of the

44For GWs，propagation effects between the source and the Earth,such as dispersion in the interstellar medium, are totally irrelevant,given the smallness of gravitational cross-sections.

Earth.44

If,for a moment,we neglect these effects,a periodic source emiti GWs at a frequency $f _ { 0 }$ produces in the detector a signal

where

$$
\begin{array} { r l } & { \quad h ( t ) = F _ { + } ( \theta , \phi ) h _ { + } ( t ) + F _ { \times } ( \theta , \phi ) h _ { \times } ( t ) , } \\ & { \quad \quad h _ { + } ( t ) = h _ { 0 , + } \cos ( 2 \pi f _ { 0 } t ) , } \\ & { \quad \quad h _ { \times } ( t ) = h _ { 0 , \times } \cos ( 2 \pi f _ { 0 } t + \alpha ) . } \end{array}
$$

We take by definition $f _ { 0 } > 0$ ： $h _ { 0 , A }$ are the real amplitudes for the two polarizations $( A = + , \times )$ ，and $| \alpha \rrangle$ is their relative phase. We denote by $\theta , \phi$ the angles that define the propagation direction n of the GW from the source to us,so the polar angles of the source,as seen from the Earth,are $\theta _ { s } = \pi - \theta$ and $\phi _ { s } = \phi + \pi$

Assuming for the moment that the source is,intrinsically，perfectl periodic,still the motion of the Earth modifies eqs.(7.123)-(7.125)a follows.

· Because of the Earth's rotation, the apparent position of the sourc in the sky changes,so the angles $\theta$ and $\phi$ which appear in the pattern functions change with time,and are periodic functions ol sidereal time,with period one sidereal day.If we are tracking a specific source in the sky, the time dependence of the pattern functions, $F _ { A } ( \theta ( t ) , \phi ( t ) )$ ，must therefore be taken into account and this produces a modulation of the amplitude of the signal. ·Because of the Earth's rotation and of its revolution around the Sun (or, more precisely, because of its motion with respect to the Solar System Barycenter,as discussed in Chapter 6),the relativ velocity of the Earth and the source changes with time,and this produces a time-varying Doppler shift in the frequency.

As a consequence, $h ( t )$ is not a simple monochromatic signal. We wil come back to these amplitude and phase modulations in Sections 7.6.l and 7.6.2. For the moment,however,we restrict to an observation tim $T$ suffciently short,so that these amplitude and phase modulations can be neglected.For the amplitude modulation due to the Earth's rotation this requires of course $T \ll 1$ day，while for the Doppler effect we wil quantify this requirement in Section 7.6.2. In this limit $h ( t )$ becomes monochromatic, with a frequency $f _ { 0 }$

In this simplified setting the form of the matched filter becomes obvi ous: we must limit ourselves to a bandwidth as small as possble around $f _ { 0 }$ ,since enlarging the bandwidth we accept more noise but we add no further signal. If $T$ is the total observation time,our resolution in fre quency is $1 / T$ ，see eq. (7.1O),and therefore a bandwidth as smal as possible means $\Delta f \simeq 1 / T$ .Formally，we can obtain the same result using eq. (7.49).From eqs.(7.123)-(7.125) we have, for $f > 0$

$$
\tilde { h } ( f ) = \delta ( f - f _ { 0 } ) \frac { 1 } { 2 } \left[ F _ { + } ( \theta , \phi ) h _ { 0 , + } + F _ { \times } ( \theta , \phi ) h _ { 0 , \times } e ^ { - i \alpha } \right] ,
$$

and therefore eq. (7.49) gives

$$
\begin{array} { r } { \tilde { K } ( f ) = \delta ( f - f _ { 0 } ) , } \end{array}
$$

apart from an arbitrary constant,in which we also reabsorbed $1 / S _ { n } ( f _ { 0 } )$ Of course,the Dirac delta is a mathematical idealization,and if we measure for a total observation time $T$ we must replace it by a regularized Dirac delta,

$$
\delta ( f ) = \int _ { - \infty } ^ { \infty } d t \ e ^ { i 2 \pi f t } \to \int _ { - T / 2 } ^ { T / 2 } d t \ e ^ { i 2 \pi f t } ,
$$

which has a support over a range $\Delta f \sim 1 / T$ and satisfies $\delta ( 0 ) = T$ Then eq. (7.51) becomes

$$
\begin{array} { l } { { \displaystyle \left( \frac { S } { N } \right) ^ { 2 } = \left| F _ { + } ( \theta , \phi ) h _ { 0 , + } + F _ { \times } ( \theta , \phi ) h _ { 0 , \times } e ^ { - i \alpha } \right| ^ { 2 } \int _ { 0 } ^ { \infty } d f \frac { \delta ( f - f _ { 0 } ) \delta ( 0 ) } { S _ { n } ( f ) } } } \\ { { \displaystyle ~ = \left| F _ { + } ( \theta , \phi ) h _ { 0 , + } + F _ { \times } ( \theta , \phi ) h _ { 0 , \times } e ^ { - i \alpha } \right| ^ { 2 } \frac { T } { S _ { n } ( f _ { 0 } ) } . \qquad ( 7 . 1 2 } } \end{array}
$$

Not surprisingly, the signal-to-noise ratio increases if we increase the observation time,and the dependence $S / N \sim \sqrt { T }$ is what we already found using heuristic arguments in eqs. (7.39) and (7.40).

In general, the frequency $f _ { 0 }$ is not Known in advance. However, for al exactly periodic signal,we do not need to repeat the matched filtering procedure separately for each value of the unknown parameter $f _ { 0 }$ In fact,from eq. (7.42),when $\tilde { K } ( f ) \ne \delta ( f - f _ { 0 } )$ the signal is simply S=h(fo),and the values of h(f) for all f can be computed at once performing asingle Fast Fourier Transforrh (FFT), which is a particularly cfficient algorithm.

If this were the end of the story,the search for periodic signals would simply consist in performing a single FFT on a stretch of data of length $\varLambda$ and looking for lines in the power spectrum. The signal-to-noise ratio of these line should improve with the qbservation time as $\sqrt { T }$ We will see in Section 7.6.1 and especially in Section 7.6.2 that the full story is nore complicated.

# 7.6.1 Amplitude modulation

As we pointed out above,the pattern functions depend on time because f the Earth's rotation,and are therefore periodic functions of sidereal time, with a period of one sidereal day. In the matched filtering,we must take this into account,and this results in a different amplitude modulation for each possible source ppsition.We will discuss in the next sections how to effciently scan the parameter space, in order to take this effect into account.

If we want to estimate the effect of this modulation on the sensitiv-Ity, we can however simply observe that,for integration times $T$ longer Than one day, the effect of this amplitude modulation can be taken into account averaging eq. (7.129)over the apparent motion of the sourcei one sidereal day, i.e. averagipg over allvalues of the right ascension the source,and over a rangelof values of the declination which depen on the specific orbit of the \$ource.In a first approximation，we cal replace this average with an average over the solid angle and over th polarization angle $\psi$ 45 From eq. (7.129)，using eqs.(7.33) and (7.35 we then find

45If,rather than being interested in the sensitivity to a specific source,one wants to define an average sensitivity for an ensemble of sources,then one can improve this estimate taking care of the fact that there is a statistical preference for the angles and polarizations that give a larger $S / N$ since these can be seen to larger distances.This modifies $S / N$ by factors that can be approximately estimated to be of order $( 3 / 2 ) ^ { 1 / 2 } \simeq 1 . \overset { \cdot } { 2 }$ see Thorne (1987).

<table><tr><td>(）² 2 =(F）</td><td>T h， Sn（fo）</td></tr></table>

where

$$
h _ { 0 } ^ { 2 } = h _ { 0 , + } ^ { 2 } + h _ { 0 , \times } ^ { 2 } .
$$

The values of $ { \langle F _ { + } ^ { 2 } \rangle }$ for various detectors are given in Table 7.1,recaim that $\langle F _ { + } ^ { 2 } \rangle = F / 2$ We can also rewrite eq. (7.130) as

$$
\frac { S } { N } = \frac { h _ { 0 } } { h _ { n } } ,
$$

defining the dimensionless quantity $h _ { n }$

$$
h _ { n } = \frac { 1 } { \langle F _ { \dagger } ^ { 2 } \rangle ^ { 1 / 2 } } \left( \frac { S _ { n } ( f _ { 0 } ) } { T } \right) ^ { 1 / 2 } .
$$

Therefore $h _ { n }$ is the GW amplitude that can be measured by the detectol for a periodic signal,at $S / N \mathop { = } 1$ (assuming that we have been able to correct for the phase modulation,see next section). More generally, th minimum amplitude that can be detected at a given value of $S / N$ is

$$
\overline { { ( h _ { 0 } ) _ { \mathrm { m i n } } = \frac { S / N } { \langle F _ { + } ^ { 2 } \rangle ^ { 1 / 2 } } \left( \frac { S _ { n } ( f _ { 0 } ) } { T } \right) ^ { 1 / 2 } } } .
$$

It is instructive to compare tlis result with the minimum burst ampli tude detectable at a broad-band detector,eq. (7.107). Recallng tha $S _ { n } ( f )$ has dimensions $1 / \mathrm { H z }$ ,ie.dimensions of time,we must divide it by a time in order to obtain a dimensionless quantity, such as a Gw amplitude. For bursts,we see from eq.(7.107) that this time-scaleis the duration $\tau _ { g } = 1 / f _ { \operatorname* { m a x } }$ of the burst, while for a periodic signal we se from eq.(7.l33) that it is the observation time $T$ Since $T$ can be of the order of months or years, while $\tau _ { g }$ is typically between the millisecond and a second,the minimum value of $h$ detectable for periodic signals i much smaller than for bursts.On the other hand,a periodic signal i intrinsically much weaker,since a burst emits a huge amount of energy in a very short time. We will estimate in Section 7.6.3 the maximum distances at which typical periodic signals can be seen.

For bursts,we assumed that the wave came from the optimal direction and for this reason we wrote no angular factor in cq.(7.107). For periodi signals，an average over the source position is in any case necessary because of the apparent motion of the source in the sky,leading to the amplitude modulation,and produces the angular efficiency factor (F?) in eq. (7.134).

An alternative reference quantity which is often used is h3/yr,which is defined as the minimum value of hb that can be detected at a given value of S/N,integrating for T=107s (i.e. about 1/3 of a year),

$$
h _ { 3 / \mathrm { y r } } = \frac { S / N } { \langle F _ { + } ^ { 2 } \rangle ^ { 1 / 2 } } \sqrt { S _ { n } ( f _ { 0 } ) \times \mathrm { 1 0 ^ { - 7 } H z } } .
$$

# 7.6.2 Doppler shift and phase modulation

Even if an astrophysical source emitted exactly monochromatic GWs with a frequency fo,for a detector on Earth the instantaneous value of the observed frequency f would change with time because of the Doppler effect.Recall that,to first order in v/c,the frequency measured by an lobserver with a velocity v with respect to the source is

$$
f = f _ { 0 } \left( 1 + \frac { { \bf v } \cdot \hat { \bf r } } { c } \right) ,
$$

where f is the unit vector in the direction of the source. If v·f were a constant, this would cause little concern, since it would just amount to a constant offset in the frequency and,with a single FFT,monochromatic lines at all possble frequencies are searched simultaneously. However, the velocity of the detector with respect to the source changes in time because of the Earth's rotation and because of its revolution around the Sun and this induces a time-dependehce in the observed frequency. We denote by (△v)r the change of the component of the velocity in the direction of the source,in a time T. Then the frequency f changes on the same time interval by an amount

$$
( \Delta f ) _ { \mathrm { D o p p l e r } } = f _ { 0 } { \frac { ( \Delta v ) _ { T } } { c } } .
$$

When we integrate the signal for a time T,the resolution in frequency is△f= 1/T. As long as (△f)Doppler is smaller than this resolution, all the GW signal fals into a single frequency bin and the Doppler effect can be neglected. To estimate the maximum integration time for which the Doppler effect is negligible,we consider first the effect of the Earth rotation around its axis. At a latitude of 4O degrees,the rotational velocity of the Earth is Urot = WrotR cos(40o) \~ 355 m/s, where Wrot = (2π/24 hr) and R =6.38 ×10m is the mean Earth equatorial radius.This gives Urot/c 1.2 ×10-6.During an integration time T,the Earth rotates by an angle△θ= WrotT and,if △θ <1,in order of magnitude the change of the component of the velocity in the direction of the source is given by $( \Delta v ) _ { T } / v _ { \mathrm { r o t } } \sim \Delta \theta$ i.e.

$$
( \Delta v ) _ { T } \sim v _ { \mathrm { { r o t } } } \omega _ { \mathrm { { r o t } } } T .
$$

(The precise numbers, of course, depends on the exact direction of the source with respect to the detector.) Then (△f)Dopper becomes of the

order of the frequency resolution if

$$
f _ { 0 } \left( \frac { \psi _ { \mathrm { r o t } } } { c } \right) \omega _ { \mathrm { r o t } } T \sim \frac { 1 } { T } ,
$$

which gives

$$
T \sim 6 0 \mathrm { m i n } \left( \frac { 1 \mathrm { k H z } } { f _ { 0 } } \right) ^ { 1 / 2 } .
$$

46For frequencies fo > O(40) Hz we have $T \ll 1$ day, so theapproximation $\Delta \theta \ll 1$ used to write eq.(7.138) is consistent.Otherwise,a more accurate estimate is needed.

Therefore,for waves with $f _ { 0 } \sim 1 ~ \mathrm { k H z }$ ，the Doppler effect due to the Earth's rotation around its axis becomes important after about one hour.46 It reaches its maximum value after about 12 hr (the precise numbers,again,depend on the source position),when the detector has inverted its velocity with respect to the source,△vrot = 2urot,and in this time span the frequency has changed by a total amount

$$
\left( \Delta f \right) _ { \mathrm { m a x } } ^ { \mathrm { r o t } } \sim 2 f _ { 0 } \frac { v _ { \mathrm { r o t } } } { c } \simeq \left( 2 . 4 \times 1 0 ^ { - 3 } \mathrm { H z } \left( \frac { f _ { 0 } } { \mathrm { 1 k H z } } \right) . \right.
$$

We can repeat the same reasoning for the orbital motion of the Earth around the Sun. For an order-of-magnitude estimate we can take the orbit as circular,with a radius R = 1au \~ 1.5 × 10ll m and ωorb = $2 \pi / ( 3 6 5 \mathrm { d a y s } )$ ，s0 $v _ { \mathrm { { o r b } } } \simeq 3 \times 1 0 ^ { 4 } ~ \mathrm { { m / s } }$ and $v _ { \mathrm { o r b } } / c \simeq 1 0 ^ { - 4 }$ . The maximum frequency shift induced by theEarth revolution is then

$$
\mathrm { ( } \Delta f \mathrm { ) _ { m a x } ^ { o r b } } \sim 2 f _ { 0 } \mathrm { \frac { \vert { v _ { \mathrm { o r b } } } \vert } { \vert { c } } } \simeq 0 . 2 \mathrm { H z } \left( \mathrm { \frac { ~ } { ~ } } f _ { 0 } \mathrm { \ }  \right) ,
$$

and is much larger than that due to the Earth rotation around its axis，given in eq. (7.141)，because Uorb > Urot.However,the large drift (7.142) takes place over a six months period.In an integration time T much shorter than six months,the orbital motion induces a variation (△v)r \~ VorbworbT and the corresponding frequency shift is $( \Delta f ) _ { \mathrm { D o p p l e r } } \sim f _ { 0 } \left( v _ { \mathrm { o r b } } / c \right) \omega _ { \mathrm { o r b } } T$ Similarly toeq. (7.139),the tieaf ter which the orbital Doppler shift becomes larger than the frequency resolution is given by

$$
f _ { 0 } \left( \frac { v _ { \mathrm { 0 r b } } } { \varsigma } \right) \omega _ { \mathrm { o r b } } T \sim \frac { 1 } { T } ,
$$

$$
T \sim 1 2 0  \operatorname* { m i n } ( { \frac { 1 \mathrm { k H z } } { f _ { 0 } } } ) ^ { 1 / 2 } .
$$

Therefore the Doppler shift due to the Earth rotation around its axis is the first to become important,when we increase the integration time (after about 1 hr if,for instance,fo = 1 kHz)．The orbital Doppler shift becomes of the order of the frequency resolution shortly afterwards. after an integration times of about 2 hr for fo =1 kHz,but then raises steadily;after less than one day it becomes more important than the contribution from the Earth's rotation around its axis,and it continues to raise for a six months period becoming,on the long term,the largely dominant effect.

After anintegration timeoffour months,ie. $T \simeq 1 0 ^ { 7 } \ : \mathrm { s }$ ,the frequency resolution is $\Delta f = 1 0 ^ { - 7 } ~ \mathrm { H z }$ ,which is many order of magnitudes smaller than the Doppler shifts (7.14l) and (7.142).It is interesting to see what is the form of the frequency spectrum when we are sensitive enough to resolve the time-changing Doppler shift.To simplify the geometry,we assume at first that the detector performs a simple circular motion,with frequency $\omega _ { m }$ and radius $R$ ,and that the source is in the plane of the orbital motion of the detector,as in Fig.7.1O. Since the source is at a very large distance, we have a plane wavefront propagating along the $y$ axis,and therefore proportional to $\cos [ \omega _ { 0 } ( t + \ b { y } / c ) ]$ ，where $\omega _ { 0 } = 2 \pi f _ { 0 }$ and $f _ { 0 }$ is the GW frequency. The $y$ coordinate of the detector is a function of time;we choose for definiteness the origin of time so that $y ( 0 ) = 0$ and therefore $y ( t ) = R \sin ( \omega _ { m } t )$ . Then the detector sees a signal proportional to

where

$$
\begin{array} { c } { { \cos \left[ \omega _ { 0 } \left( t + \frac { y ( t ) } { c } \right) \right] = \cos [ \omega _ { 0 } t + \beta \sin ( \omega _ { m } t ) ] , } } \\ { { { } } } \\ { { \beta = \displaystyle \frac { \omega _ { 0 } R } { c } = \frac { \omega _ { 0 } } { \omega _ { m } } ~ \frac { v } { c } , } } \end{array}
$$

with $v = \omega _ { m } R$ The parameter $\beta$ is called the modulation index,and ${ \dot { \omega _ { m } } } = 2 \pi f _ { m }$ ,where $f _ { m }$ is the modulation frequency. This signal can be written as a superposition of monochromatic waves using the identity

$$
\cos [ \omega _ { 0 } t + \beta \sin ( \omega _ { m } t ) ] = \sum _ { k = - \infty } ^ { \infty } J _ { k } ( \beta ) \cos [ ( \omega _ { 0 } + k \omega _ { m } ) t ] ,
$$

where $J _ { k } ( \beta )$ is the Bessel function.47 The signal is therefore split into a carrier at the frequency $f _ { 0 }$ ,plus an infinite number of sidebands at $f _ { 0 } \pm$ $k f _ { m } .$ for all integer $k$ ,and the power in the $k$ -th sideband is proportional to $J _ { k } ^ { 2 } ( \beta )$ . The qualitative form of this spectrum depends strongly on the modulation index $\beta$ For $\beta \to 0$ and $k$ integer we have $J _ { k } ( \beta ) \sim \beta ^ { | k | }$ ,s0 when $\beta \ll 1$ most of the power is in the carrier $( k = 0$ )，with smaller power in the sidebands $k = \pm 1$ ，even smaller power at $k = \pm 2$ etc. However, in our case $\beta$ is given byeq.(7.146)and it is large.In fact, for the rotation of the Earth around itis axis,setting $\omega _ { m } = 2 \pi / ( 2 4 \mathrm { h r } )$ and $v / c \simeq 1 . 2 \times 1 0 ^ { - 6 }$ ,eq.(7.146) gives $\beta \simeq 1 0 0 \left( f _ { 0 } / 1 \mathrm { k H z } \right)$ ，while for the orbital motion $\beta \simeq 3 \times 1 0 ^ { 6 } \left( f _ { 0 } / 1 \mathrm { k H z } \right)$ .Therefore,in the range of frequencies relevant for ground-based ihterferometers $\left( f _ { 0 } > O ( 1 0 ) \ \mathrm { H z } \right)$ ， we are always in the regime $\beta \gg 1$

The average number of sidebands into which the total power is distributed can be calculated using48

$$
\begin{array} { c } { { \langle k ^ { 2 } \rangle \equiv \displaystyle \frac { \sum _ { k = - \infty } ^ { \infty } \left| k ^ { 2 } J _ { k } ^ { 2 } ( \beta ) \right. } { \left. \sum _ { k = - \infty } ^ { \infty } J _ { k } ^ { 2 } ( \beta ) \right. } } } \\ { { \displaystyle = \frac { \beta ^ { 2 } } { 2 } , } } \end{array}
$$

so the power is distributed in $O ( \beta )$ sidebands,as shown in Fig.7.11. Once the frequency resolution $1 / T$ has become of the order of this

![](images/e48302da4627450122e5242dfd5863634efe0fe4144b854913d3adf1898d9068.jpg)  
Fig.7.10 The simplifed geometry discussed in the text.The detector $D$ performs a circular motion in the $( x , y )$ plane.The source $S$ is in the same plane,along the $y$ axis.

$^ { 4 7 } \mathrm { T h i s }$ identitycanbeobtained writing $\cos [ ( \omega _ { 0 } + k \omega _ { m } ) t .$ inside the sum，as $\cos ( \omega _ { 0 } t ) \cos ( k \omega _ { m } t ) ~ -$ $\sin ( \omega _ { 0 } t ) \sin ( k \omega _ { m } t )$ and using Gradshteyn and Ryzhik (1980),8.514.5 and 8.514.6，recalling that，for $k$ integer, $J _ { - k } ( z ) = ( - 1 ) ^ { k } { \bar { J } } _ { k } ( z )$

48 See Gradshteyn and Ryzhik (1980),   
8.536.2.

![](images/864d263046c3dfb45024b627dfbef2ef8138ad3801ff943b3a63bb71c98ed9aa.jpg)  
Fig.7.11 The quantity $J _ { k } ^ { 2 } ( \beta )$ for $\beta = 5 0$ ,as a function of $k$

Doppler line broadening,inereasing T further does not improve s stantially the signal-to-noise ratio.In fact,while a smaller frequencyh contains by definition less noise, it now also contains less signal,sim the signal gets spread over many bins.However,if at this stage signal already emerged from the noise, increasing T further we impro the resolution by which we are able to reconstruct the line shape therefore the accuracy by which we can reconstruct the source positio see Note 49 below).

Luckily, there is in principle a very simple way (borrowed from pul radio-astronomy) to correct fqr the Doppler shift.In the simple geome rical situation illustrated in Fig.7.10,we just need to define a new tim variable t'= t+y(t)/c. In terms of this variable the signal (7.145) simply proportional to cos(wot') and,performing the Fourier transfor with respect to t',all sidebands collapse into a single frequency. For generic source location,the redefinition of time that does the job is

$$
t ^ { \prime } = t + \frac { { \bf x } ( t ) { \bf \cdot } \hat { \bf r } } { c } ,
$$

where x(t) is the position of the detector (measured for instance usin the Solar System Barycenter (SSB)as a reference frame) andr is the um vector pointing toward the source. Observe that this is just the Roeme time delay that we already discussed in Section 6.2.2.We can therefon simply resample the output of the detector in terms of this new time,am we have corrected for the Doppler effect.The procedure has an adde bonus: it is quite likely that,in the Fourier spectrum of the output,the will be monochromatic lines due to instruinental noise. If such a line ha a frequency that is constant in time to a good accuracy, its signal-to noise ratio willincrease as √T, just as for a GW signal. However, whe we apply the resampling procedure,a real GW signal, which was sprea over many bins,is collapsed t a single frequency bin,an conversely a instrumental line which was monochromatic will be spread over man bins,and will finally be diluted into the noise. In other words,we an using the Doppler modulation as a powerful signature that discriminate a real GW signal from instrumental noise.

The simplicity of this solution comes however at a price: we need to know both x(t) and r with great precision. We can assume that th motion of the Earth is known to a sufficient accuracy (although,if w want to integrate for a time T\~1 yr,we need to keep under contro effects that can produce shifts△f \~10-7 Hz,and for this we must also include small effects like the oscillations of the Earth around the Earth Moon barycenter,which however are precisely known),so the main erro comes from the uncertainty on the angular position of the source.Fron eq. (7.136) we see that,in order to correct for the Doppler shift with al accuracy smaller than the experimental resolution 1/T on f,we need in order of magnitude,

$$
\frac { f _ { 0 } } { c } ( \Delta v ) _ { T } \Delta \theta < \frac { 1 } { T } ,
$$

where $( \Delta v ) _ { T }$ is the variationof thevelocityof the Earth during the observation time $T$ (recall that only the temporal variation is relevant, otherwise the Doppler effect would give just a constant offset in $f _ { 0 , }$ ， while $\Delta \theta$ is the angular resolution (in radians) on the position of the source.

If we take $( \Delta v ) _ { T } \sim \ v _ { \mathrm { o r b } } \omega _ { \mathrm { o r b } } T$ we find that,to apply the Doppler correction, we need to know the source location to an accuracy

$$
\begin{array} { r l } & { \Delta \theta < \frac { 1 } { f _ { 0 } \left( { v _ { \mathrm { o r b } } } / { c } \right) \omega _ { \mathrm { o r b } } T ^ { 2 } } } \\ & { \qquad \simeq 0 . 1 \operatorname { a r c s e c } \left( \frac { 1 0 ^ { 7 } \mathrm { s } } { \dot { T } } \right) ^ { 2 } \left( \frac { 1 \mathrm { k H z } } { f _ { 0 } } \right) . } \end{array}
$$

This expression is correct as long as the Doppler effect due to the orbital motion dominates that due to the Earth rotation around its axis,i.e. for $T \gtrsim 1$ day,and also as long as the angle $\omega _ { \mathrm { o r b } } T$ is small, since otherwise the approximation $( \Delta v ) _ { T } \sim \ v _ { \mathrm { o r b } } \omega _ { \mathrm { o r b } } T$ should rather be replaced by $( \Delta v ) _ { T } \sim v _ { \mathrm { o r b } } \sin \omega _ { \mathrm { o r b } } T$ ，so approximately eq.(7.151) is valid as long as 1da $\mathrm { y } \lesssim T { \lesssim } 4$ months.49

If we are targeting a specific source whose position is known to this accuracy or better，as is the case for many pulsars,this requirement does not pose special problems.However,as we will discuss in Vol. 2, there are many mcchanisms that can produce periodic GWs,in particular in neutron stars, that are not necessarily associated to a strong electromagnetic emission or,as with pulsars, the electromagnetic emission could be beamed in a direction that does not intersect the Earth. It is in fact quite likely that most of the potentially interesting sources of periodic GWs have no detected optical counterpart. For example, the closest observed neutron star is at a distance $r \sim 1 0 0$ pc; however, population synthesis calculations indicate that the closest one should be at a distance $r \sim 5 \mathrm { - } 1 0 ~ \mathrm { p } $ c,and then in a sphere of radius $r \sim 1 0 0$ pc there should be $O ( 1 0 ^ { 3 } - 1 0 ^ { 4 } )$ neutron stars.It is therefore of the greatest interest to perform blind searches,i.e.searches for unknown sources over the whole sky.In principle,this means that we should partition the celestial sphere in pixels with a size given by eq.(7.151) (in fact even smaller,see Note 52 in the next section),and in each one we should apply a separate Doppler correction.As we will see in the next section,for integration times of months this is impossible,even with the maximum present or foreseeable computer power.

Furthermore,we have assumed until now that the intrinsic GW frequency $f _ { 0 }$ of the source is stable,within the experimental resolution $\Delta f = 1 / T$ ,and that the only modulation comes from the relative moion of the detector.This means that we are assuming a stability of the source frequency at the level

$$
{ \begin{array} { r } { { \frac { \Delta f _ { 0 } } { f _ { 0 } } } = { \frac { 1 } { T f _ { 0 } } } } \\ { \simeq 1 \times 1 0 ^ { - 1 0 } \left( { \frac { 1 0 ^ { 7 } \mathrm { s } } { T } } \right) \left( { \frac { 1 \mathrm { k H z } } { f _ { 0 } } } \right) . } \end{array} }
$$

49Actually，one could turn the argument around and observe that,if we are so lucky that there is a periodic signal so strong that can be extracted from the noise without correcting for the Doppler shift then,following the evolution of the frequency with time, we will be able to reconstruct the position of the source to the accuracy $\Delta \theta$ given by eq.(7.151)．With present detector sensitivities,however,this possibility seems quite unlikely.

Quite remarkably, rotating neutron|stars can sometime have this stability.The main mechanism that produces a drift in their frequency i the fact that a rotating NS radiates,both electromagnetically and grav itationally，and therefore loses energy.This energy is taken from th rotational energy of the NS,which therefore spins down. Pulsars ar characterized by their spindown age T,

$$
\tau = { \frac { f } { | \dot { f } | } } ,
$$

50The spindown age is of the order of the age of the pulsar if,throughout its lifetime,the pulsar frequency evolution can be described by the equation

where $f$ is their rotational ftequency. As we saw in Section 4.2.1,fol rotation around a principal axis and in the quadrupole approximation the GWs emitted are monochromatic with a frequency $f _ { 0 } = 2 f$ , $\tau = f _ { 0 } / | \dot { f } _ { 0 } |$ .50 During the observation time $T$ ,a pulsar with spindowl age $\tau$ changes its GW frequency by an amount $\Delta f _ { 0 } = { \dot { f } } _ { 0 } T = \dot { - } f _ { 0 } T / \tau$ i.e.by

$$
{ \dot { f } } = - a f ^ { \pi }
$$

(where $a$ is a constant) and if the braking index $n > 1$ In fact,integrating the above equation we get

$$
\begin{array} { l } { \displaystyle { \frac { \Delta f _ { 0 } } { f _ { 0 } } = - \frac { T } { \tau } } } \\ { \displaystyle { \simeq - 3 . 2 \times  1 0 ^ { - 1 0 } ( \frac { 1 0 ^ { 9 } \mathrm { y r } } { \tau } ) ( \frac { T } { 1 0 ^ { 7 } \mathrm { s } } ) . } } \end{array}
$$

$$
\begin{array} { l r } { { [ f ( t ) ] ^ { - ( n - 1 ) } - [ f ( 0 ) ] ^ { - ( n - 1 ) } } } \\ { { = a ( n - 1 ) t , } } \end{array}
$$

where $t = 0$ is the time at which the pulsar was born.If the frequency at birth, $f ( 0 )$ ，was much bigger than the frequency today，and if $n > 1$ wecan neglect the term $[ f ( 0 ) ] ^ { - ( n - 1 ) }$ and the age of a pulsar is related to its present values of $f$ and $\dot { f }$ by

$$
\begin{array} { l } { t = \displaystyle \frac { 1 } { a ( n - 1 ) f ^ { n - 1 } } } \\ { = \displaystyle \frac { f } { ( n - 1 ) | \dot { f } | } } \\ { = \displaystyle \frac { \tau } { n - 1 } . } \end{array}
$$

Experimentally，the braking index $n$ typically has values $n \simeq 2 \mathrm { - } 3$ depending on the specific pulsar.

Comparing with eq. (7.152) we see that, with an integration time $T =$ 107 s,for a millisecond pulsar with fo \~1 kHz,the effect of the spindown is important if its spindown $\mathsf { \Pi } _ { \mathsf { \Phi } } ^ { \mathrm { i } } \mathrm { g e }$ is lower than $3 \times 1 0 ^ { 9 }$ yr while, if $f _ { 0 } =$ $1 0 ~ \mathrm { H z }$ ，spindown is important,again over $T \simeq 1 0 ^ { 7 }$ s,if $\tau < 3 \times 1 0 ^ { 7 }$ yr Therefore for many pulsars,and in particular for young pulsars,ovel such a long observation time the spindown must be taken into account. Actually in young pulsars the spindown rate can be so high that even the effect of the second derivative fo can become important.

For known pulsars the spindown can be measured and taken into ac count when we make the Doppler correction, while for blind searches i introduces new unknown parameters.Besides spindown, there are other reasons why the frequency of the GW emitted by a pulsar can change:

· Pulsars exhibit glitches,i.e. sudden jumps in the frequency related to rearrangements of their internal structure. These glitches can produce changes in the frequency as large as $\Delta f _ { 0 } / f _ { 0 } \sim 1 0 ^ { - 6 }$ and occur erratically,at a rate which depends strongly on the specific pulsar,but in general of the order one glitch every few years. · A large fraction of the known milisecond pulsars are in binary systems.In this case,there will be an additional Doppler fet due to the motion of the source, as we saw in Section 6.2. · Pulsar are the remnant of supernova explosions,and at birth they can receive a large kick; so their velocities can be larger than the typical velocities of the stars in their galactic neighborhood,and the pulsar proper motion can be important. Of course,if the mo tion is uniform,this onlyproduces a constant shift in the frequency However,accelerations due to gravitational felds can be important.In particular,many pulsars are found in globular clusters. In this case,the acceleration due to the Newtonian gravitational forces from all the other stars is known to produce frequency drifts comparable to the spindown rate.

·Even a uniform proper motion can be important if, during the observation time,it drives the NS out of the pixel in the sky where it was initially.For instance,a pulsar at a distance $r = 3 0 0$ pc, with a transverse velocity $v = 1 0 ^ { 3 } \mathrm { k m / s }$ with respect to our line-of-sight, in a time $T = 1 0 ^ { 7 }$ s moves by $\Delta \theta = v T / r \simeq 1 0 ^ { - 6 } \mathrm { r a d \simeq 0 . 2 }$ arcsec which,according toeq.(7.151),is of order of the accuracy $\Delta \theta$ that we need,over such an integration time $T$ ,for a pulsar radiating GWs at $f _ { 0 } \sim 1 ~ \mathrm { k H z }$

In the next section we willdiscuss how one can try to cope with these difficulties.

# 7.6.3Efficient search algorithms

Coherent searches

From the discussion of the previous section we know that,if we want to integrate the signal for a long time,we must resample the output of the detector in terms of the time $t ^ { \prime }$ defined in eq.(7.149),plus further correction for the spindown or other effects|that change the frequency. The GWs produced by a rotating NS,in the absence of spindown, has been computed in eq. (4.223). Including the Doppler effect of the detector aind the spindown of the source we can write the signal received as

$$
h ( t ) = F _ { + } ( \hat { \bf n } ( t ) ; \psi ) h _ { 0 } \frac { 1 + \cos ^ { 2 } \upsilon } { 2 } \cos \Phi ( t ) + F _ { \times } ( \hat { \bf n } ( t ) ; \psi ) h _ { 0 } \cos \upsilon \sin \Phi ( t ) ,
$$

where $h _ { 0 }$ is given in eq. (4.224)，and $4$ is the angle between the spin axis of the neutron star and the propagation direction $\hat { \bf n }$ of the GW; of course $\hat { \bf n } = - \hat { \bf r }$ ，where $\hat { \mathbf { r } }$ is the unit vector pointing toward the source, and depends on time because of the relative motion of the detector and source. The evolution of the accumulated phase $\begin{array} { r } { \Phi ( t ) = 2 \pi \int d t f ( t ) } \end{array}$ observed by the detector can be described by a Taylor expansion, writing

$$
f ( t ^ { \prime } ) = f _ { 0 } + \dot { f } _ { 0 } ( t ^ { \prime } - t _ { 0 } ^ { \prime } ) + \frac { 1 } { 2 } \ddot { f } _ { 0 } ( t ^ { \prime } - t _ { 0 } ^ { \prime } ) ^ { 2 } + \ldots ,
$$

where $t ^ { \prime }$ is the resampled time given in eq. (7.149),i.e. the time of arrival fthe signal in the Solar System Barycehter (SSB),51 and $t _ { 0 } ^ { \prime }$ is a fiducial vaiue, such that $\Phi ( t _ { 0 } ^ { \prime } )$ has the value $\phi _ { 0 }$ Then

$$
\Phi ( t ) = \phi _ { 0 } + 2 \pi \left[ f _ { 0 } ( t ^ { \prime } - t _ { 0 } ^ { \prime } ) + \frac { 1 } { 2 } \dot { f } _ { 0 } ( t ^ { \prime } - t _ { 0 } ^ { \prime } ) ^ { 2 } + \frac { 1 } { 6 } \ddot { f } _ { 0 } ( t ^ { \prime } - t _ { 0 } ^ { \prime } ) ^ { 3 } + \ldots \right] .
$$

Ofcourse,a truncated Taylor expansion is useful only if the higher order rms are small corrections during the whole observation time $T$ This is Iot the case for a neutron star in a binary system, which rather performs circular motion around the center-of-mass of the system,so eq. (7.160) oaly applies to isolated neutron stars.

5Actually，tese

$$
t ^ { \prime } = t + \frac { \mathbf { x } ( t ) \cdot \hat { \mathbf { r } } } { c } + \Delta _ { E \odot } - \Delta _ { S \odot } ,
$$

where $\Delta _ { E \odot }$ and $\Delta _ { S \odot }$ are the solar system Einstein and Shapiro time delays discussed in Section 6.2.2.However, given the detector and the source positions,the Einstein and Shapiro delays can be computed,as we did explicitly in Section 6.2.2,and introduce no new free parameter.

If our target is a given pulsar whose position, proper motion and spin down parameters are known to sufficient accuracy,the form of the signa (7.158) is fixed.Then we can simply demodulate the signal defining new variable $t ^ { \prime \prime }$ as

$$
t ^ { \prime \prime } = ( t ^ { \prime } - t _ { 0 } ^ { \prime } ) + \frac { \dot { f } _ { 0 } } { 2 f _ { 0 } } ( t ^ { \prime } - t _ { 0 } ^ { \prime } ) ^ { 2 } + \frac { \ddot { f } _ { 0 } } { 6 f _ { 0 } } ( t ^ { \prime } - t _ { 0 } ^ { \prime } ) ^ { 3 } + \ldots ,
$$

so that eq. (7.160) reads $\Phi = \phi _ { 0 } + 2 \pi f _ { 0 } t ^ { \prime \prime }$ .We resample the detectol output with respect to this variable,and then all we need to do is to perform a single Fast Fourier Transform (FFT) on this resampled stretch of data,of length $T$ . The number of spindown parameters ${ \ddot { f } } _ { 0 } , { \ddot { f } } _ { 0 } , \dots { \mathrm { t } }$ be included to have sufficient accuracy depend on the source, and on the observation time $T$

If however we want to perform a blind all-sky search,the problem becomes quickly intractable with increasing observation time $T$ Infact our parameter space is given by the angles $( \theta _ { s } , \phi _ { s } )$ of the source and by the spindown parameters $\dot { f } _ { 0 } / \dot { f } _ { 0 } , \ddot { f } _ { 0 } / f _ { 0 }$ ,etc.Observe that $f _ { 0 }$ itself does not contribute to the dimension of the parameter space; the resampling of time （7.149)is independentof $f _ { 0 }$ ,while eq. (7.161) depends only on the ratios $\dot { f } _ { 0 } / \dot { f } _ { 0 } , \ddot { f } _ { 0 } / { f } _ { 0 } , \hdots$ ，and not separately on $f _ { 0 } , { \dot { f } } _ { 0 } , { \ddot { f } } _ { 0 } , \dots$ This is a crucial advantage of the resampling technique. If,rather than resam pling the detector output,we directly used the Wiener filtering for the waveform given in eqs.(7.158) and (7.160)，then $f _ { 0 }$ would be an ad ditional parameter to be searched,and the computational cost would increase dramatically.

Then, what we should do is to discretize this parameter space,and for each point of this parameter space we should perform the appropriate demodulation (7.161) and oneFFT. This procedure is referred to as a coherent search. Its drawback is that,if we want to take advantage of the large integration time,the mesh in the discretized parameter space must become finer and finer when we increase $T$ .For instance, even in the simplest case in which the spindown parameters are negligible. and therefore the parameter space is given only by the angles $\big ( \theta _ { s } , \phi _ { s } \big )$ still the number of patches in the sky that we must consider is at least $N _ { \mathrm { p a t c h e s } } = { 4 \pi } / ( { \Delta \theta } ) ^ { 2 }$ and scales at least as $T ^ { 4 }$ ,see eq. (7.151).52

More generally,the number of mesh points depends on the kind of search that we perform. For instance,old pulsars are less demanding than young pulsars of the same frequency, since their spindown rate is lower and therefore it can be taken into account using a larger mesh in the spindown parameter space Similarly, we see from eq. (7.151) that slow pulsars (say, $f _ { 0 } < 2 0 0 ~ \mathrm { H z }$ ）are easier to analyze that fast pulsars with $f _ { 0 } \sim 1 ~ \mathrm { k H z }$

Since the time needed for data analysis grows with a large power of $T$ ，increasing $T$ we necessarily reach a point where the data analysis would take the same time as the observation time $T$ and beyond that point it would quickly becomes many orders of magnitude larger than the observation time. We can therefore take as a limit the condition that the time required by dataanalysis does not exceed the observation time used to take the same data. To have an idea of the computational requirements consider that,using $1 0 ^ { 7 } | \mathrm { s }$ of data to search for periodic GWs with frequencies up to $5 0 0 ~ \mathrm { H z }$ ,requires the calculation of a FFT with $1 0 ^ { 1 0 }$ points, which takes about ${ 1 \mathrm { s } }$ bn a teraflop computer (assuming that all $1 0 ^ { 1 0 }$ points can be held simultaneously in fast memory),and we need one such FFT for each point of the parameter space. It can be estimated53 that a coherent al-sky search of $T = 1 0 ^ { 7 } \mathrm { s }$ of data for slow, old pulsars ( $\tau > 1 0 0 0$ yr, $f _ { 0 } < 2 0 0 ~ \mathrm { H z }$ i.e.the“easier” target）requires ouly one spindown parameter and $1 0 ^ { 1 0 }$ independent points in parameter space,while for young, fast pulsar (frequencies up to $f _ { 0 } \simeq 1 ~ \mathrm { k H z }$ ， $\tau$ as low as $4 0 \mathrm { y r }$ ) three spindown parameters and $8 \times 1 0 ^ { 2 1 }$ points in parameter space are required.Then,even in the“easy”case, the analysis of four months of data would require three centuries on a teraflop computer! Requiring that the data analysis does not last more than data taking, one finds that for slow,old pulsars tle data stretch cannot be longer than $\sim 1 8$ days,while for young,fast pulsar the limit is less than one day. The disappointing conclusion is that,even if a detector can in principle take good data for months or years,a coherent blind all-sky search for pulsar using fully these data is impossible.

# Incoherent searches

A solution to the computational problem discussed above is to split the total observation time $T$ into $\mathcal { N }$ stacks of length $T _ { \mathrm { s t a c k } }$ ，with $T =$ $\mathit { N T } _ { \mathrm { s t a c k } }$ We choose $T _ { \mathrm { s t a c k } }$ so that a coherent search over such a time is computationally feasible. So the output of each coherent search over one stack is a collection of function $\tilde { h } ( f )$ ,one for each value of the parameter space.For each point in parameter space we then add the quantity $| \tilde { h } ( f ) | ^ { 2 }$ over the $\mathcal { N }$ stacks. Since in this way the phase information between the different stacks gets lost,this is called an incoherent search. If we denote by $\tau _ { \mathrm { s t a c k } }$ the time needed to perform a coherent search on a stack of data of length $T _ { \mathrm { s t a c k } }$ ,the time needed for the full incoherent search is $\tau _ { \mathrm { i n c } } = \mathcal { N } \tau _ { \mathrm { s t a c k } }$ ,while the time|needed for a full coherent search over the whole time $T$ is $\tau _ { \mathrm { c o h } } \simeq ( T / T _ { \mathrm { s t a c k } } ) ^ { n } \tau _ { \mathrm { s t a c k } } = \mathcal { N } ^ { n } \tau _ { \mathrm { s t a c k } }$ ,s0

$$
\tau _ { \mathrm { i n c } } \simeq \frac { 1 } { \sqrt { n - 1 } } \tau _ { \mathrm { c o h } } ,
$$

where the power $n$ ,as discussed above,is determined by the kind of pulsars that we are targeting. Since $h$ is large (at least $n = 5$ ，even when no spindown parameters are needed, see Note 52),it is clear that incoherent searches have a huge advantage in terms of computational cost and,for a given observation time $\dot { \boldsymbol { { \cal T } } }$ ,taking $\mathcal { N }$ sufficiently large,i.e. $T _ { s t a c k }$ sufficiently small, the computation becomes feasible.

From the point of view of sensitivity,the value of $( S / N ) ^ { 2 }$ obtained fom a single stack of length $T _ { \mathrm { s t a c k } }$ is given by eq.（7.130) replacing $T$ by $ { T _ { \mathrm { s t a c k } } }$ Adding $\mathcal { N }$ of these spectra the variance is reduced by $1 / \sqrt { \mathcal { N } }$ and therefore,for an incoherent search,eq. (7.130) becomes

$$
\left( \frac { S } { N } \right) ^ { 2 } = \langle F _ { + } ^ { 2 } \rangle \ \left( \frac { N ^ { 1 / 2 } T _ { \mathrm { s t a c k } } } { S _ { n } ( f _ { 0 } ) } \right) \ h _ { 0 } ^ { 2 }
$$

$$
= \frac { 1 } { \sqrt { \mathcal { N } } } \left. F _ { + } ^ { 2 } \right. \left( \frac { T } { S _ { n } ( f _ { 0 } ) } \right) h _ { 0 } ^ { 2 }
$$

and the minimum amplitude detectable at a given $S / N$ ,eq. (7.134) becomes

<table><tr><td>（ho）min =n</td><td>(s)</td></tr></table>

where we have defined an efficiency factor which takes into account the desired level of the signal-to-noise rati $S / N$ ,the average over the orbit of the source,which produces the facto $\langle F _ { + } ^ { 2 } \rangle ^ { 1 / 2 }$ , and the need to separate the data into $\mathcal { N }$ stack for computa tional feasibility.

<table><tr><td>n=</td><td>N1/4 (S/N) （F2）1/2，</td></tr></table>

In practice,beside being forced by computational requirements, incd herent searches are also necessary because a detector never has monthis and not even weeks, of continuous good data taking. There are alway interruption due to maintenance,period of higher noise level that mus be removed,etc.and the experimental precision that one has on the tim at which data taking resumed is not sufficiently good to recombine co herently different stacks of data. The incoherent method,of course,can be applied even when the sirgle stacks have not all the same duration and when they are not consecutive.

When performing an incoherent search each stack is demodulated, a discussed in the previous section,using a mesh of points sufficient confine the searched signal into a single bin. The individual power spe tra,before being summed,must be corrected for their relative frequency drift using a finer parameter mesh suitable for removing the phase mod ulation over the whole observation period. The simplest implementatiol of this method consists in choosing stacks of about $3 0 ~ \mathrm { { m i n } }$ ,so that th Doppler effect in each stack can simply be neglected,and within a sin gle stack no demodulation is needed. In this case a period of $1 0 ^ { 7 }$ se of data is divided into $\mathcal { N } \simeq 5 0 0 0$ stacks,and the minimum detectabl value $( h _ { 0 } ) _ { \mathrm { m i n } }$ in eq. (7.164) islarger than in a coherent search by a factol $\mathcal { N } ^ { 1 / 4 } \sim 8$ .With the difference,of course,that a blind full-sky incoher ent search of this type is computationally feasible whilea blind full-sky coherent search is not.

Alternatively,one can chobse longer stacks,say of the order of on day.These will need demodulation,but a relatively coarse mesh in parameter space will suffice to concentrate the whole signal into a single bin.Then we combine the separate stacks using a finer mesh. Of course the longer the stack,the higher is the sensitivity,but the higher is also the computational cost. Incoherent searches can also be used as a first stage in a hierarchical search:an incoherent blind all-sky search can produce a number of interesting candidate signals,for certain values of the parameters. These points in parameter space can then be examined more thoroughly with a directed coherent search.

We can now compare the experimental sensitivity given by eq.(7.164) with the signal expected from a rotating NS, given in eq. (4.224). We then find that the maximum distance $r$ which a detector can reach in a blind full-sky search for periodic GWs from rotating neutron stars is

$$
\begin{array} { l } { { r = 5 . 8 \mathrm { k p c } \left( \frac { 1 0 ^ { - 2 3 } \mathrm { H z } ^ { - 1 / 2 } } { S _ { n } ^ { 1 / 2 } ( f _ { 0 } ) } \right) \left( \frac { T } { 3 \times 1 0 ^ { 7 } \mathrm { s } } \right) ^ { 1 / 2 } } } \\ { { \quad \times \left( \frac { 1 0 0 } { \eta } \right) \left( \frac { \epsilon } { 1 0 ^ { - 6 } } \right) \left( \frac { I _ { z z } } { 1 0 ^ { 3 8 } \mathrm { k g } \mathrm { m } ^ { 2 } } \right) \left( \frac { f _ { 0 } } { 1 \mathrm { k } \mathrm { H z } } \right) ^ { 2 } . } } \end{array}
$$

The reference value $\eta = 1 0 0$ corresponds to a search for a total time $T =$ $\mathrm { 3 \times 1 0 ^ { 7 } }$ s divided into stacks with $T _ { \mathrm { s t a t k } } \simeq 3 0$ min (so $\mathcal { N } \simeq 1 . 7 \times 1 0 ^ { 4 }$ ，a factor $1 / \langle F _ { + } ^ { 2 } \rangle ^ { 1 / 2 } = \sqrt { 5 }$ as appropriatefor interferometers, see Table 7.1, and a value $S / N \simeq 4$ The strain sensitivity $S _ { n } ^ { 1 / 2 }$ has been normalized to the value expected for an advanced interferometer.

# The Hough transform

As we have seen above,in incoherent searches the observation time is divided into stacks,where the plase modulation due to Doppler effect and spindown is either negligible (if $T _ { \mathrm { s t a c k s } } \lesssim 3 0 \ \mathrm { m i n } ,$ or anyway relatively easy to correct for,so that a GW signal,if present,falls into a single frequency bin.When we compare diferent stacks,the position in frequency of the bin that contains the signal changes,because of the Doppler effect_and of the spindown.For each point in the parameter space $( \theta _ { s } , \phi _ { s } , \dot { f } _ { 0 } / f _ { 0 } , \ddot { f } _ { 0 } / f _ { 0 } , \dot { \ldots } )$ we can compute how the position of the bin should change and we can correct for it,using the resampling technique discussed in the previous section.In this way,for each point of parameter spaces,the bins are “realigned”,and the power in corresponding bins is summed.

An interesting variation on this scheme is given by the Hough transform,which is a technique used for pattern recognition in digital images.4IntheHoughtransformasafirststepratherthansuming up the power in the corresponding bins,we fix a threshold in each data stack.A bin is deemed “black”if the power in it exceeds the threshold, and "white” if it does not. In the time-frequency plane obtained aligning in frequency (with no correction) the various stacks,we therefore have a set of black pixels,as in Fig.712.

54It was developed in 1959 by Paul Hough at CERN,to analyze the tracks of particles in bubble chambers,and today is also used in astronomical data analysis.

In the case of Gaussian noise, where large fluctuations are unlikely, it would in principle be more convenient to sum up the power of the corresponding bins,rather than reducing all the information to a set of zeros (white)and ones (black). However,the Hough transform is more robust in the presence of non-Gaussian noise and large occasional external dis-