# Exercise

Show that a Hamiltonian system is never globally ergodic. What is refered to as an ergodic system in this case is the flow on the energy shell with the Liouville measure (3.13).

Another fundamental concept for the study of chaotic motion is that of ‘mixing'.As motivation we take the classic example in Arnold and Avez (1968)-a glass containing 2O percent rum and 80 percent Coca Cola (fig. 3.1O). If they are separated so that the region $\pmb { A }$ is the region originally occupied by the rum and $B$ is any region in the glass,after mixing $\pmb { n }$ times the percentage of rum in $\pmb { B }$ should be roughly

$$
1 0 0 \mu ( \mathbf { T } ^ { n } A \cap B ) / \mu ( B ) \simeq 1 0 0 \mu ( A )
$$

if $\mu$ is normalized.In other words, we expect that each part of the glass will contain 20 percent of rum as $n  \infty$ . We therefore define a system to be mixing if

$$
\operatorname* { l i m } _ { n \to \infty } \mu ( \mathbf { T } ^ { n } A \cap B ) = \mu ( A ) \mu ( B )
$$

for any pair of measurable sets $\pmb { A }$ and $\pmb { B }$

The property of mixing implies ergodicity. To show this we choose an invariant measurable set $\pmb { A }$ ：

$$
\mathbf { T } ^ { n } A \cap A = A
$$

and the set $B = A$ . Then (3.24) reduces to

$$
\mu ( A ) = ( \mu ( A ) ) ^ { 2 } ,
$$

wherefore $\mu ( A ) = 0$ or 1.

![](images/93f7ac45ec456e3c810df7d091ec0b36784ad99cfbf11088ef6d46ccf853f676.jpg)  
Fig. 3.10. Mixing $20 \%$ of rum into $80 \%$ of Coca Cola, there should be an equal proportion of rum in any region $\pmb { B }$ of the glass.

Any region $\pmb { A }$ will be distorted into a very long thin strip,winding helicoidally around the torus,by successive iterations of Arnold's cat map. This system is mixing and therefore it is also ergodic. As for the translations of the torus studied in section 1.3, they do not deform a region A. The intersections of $\mathbf { T } ^ { n } A$ with a region $B$ will alternate for all $\pmb { n }$ between being empty,or having positive measure. This is an example of an ergodic system that is not mixing.

# 3.5 Entropy

A fundamental characteristic of chaotic motion is that any initial uncertainty about the system's position in phase space increases rapidly with time.Another way to put it is that successive approximate measurements of the system's position supply more information in a chaotic system than in a more ‘predictable’ system. The concept of metric entropy introduced by Kolmogorov turns this into a rigorous idea.

Let us make a partition $\pmb { \alpha }$ of phase space into $N$ disjoint regions $A _ { i }$ ,so that the probability of finding the system in any one of them is $\mu ( A _ { i } ) = \mu _ { i }$ .We then define the entropy of the partition $\pmb { \alpha }$ to be

$$
h ( \alpha ) = - \sum _ { i = 1 } ^ { N } \mu _ { i } \log \mu _ { i } .
$$

The partitions into $N$ regions with the maximum entropy are the ones for which $\mu _ { i } = 1 / N$ for all i: $h = 1 0 \mathrm { g } N$ 、This follows from the fact that the function $\phi ( x ) = - x \log x$ (fig.3.11） is convex in the interval [0,1]. Therefore,

$$
\phi \Biggl ( N ^ { - 1 } \sum _ { j = 1 } ^ { N } x _ { j } \Biggr ) \geq N ^ { - 1 } \sum _ { j = 1 } ^ { N } \phi ( x _ { j } )
$$

and hence

$$
\begin{array} { r } { h ( \alpha ) = \sum \phi ( \mu _ { i } ) \le N \phi ( N ^ { - 1 } \sum \mu _ { i } ) = N \phi ( N ^ { - 1 } ) = \log N . } \end{array}
$$

The trivial partition, where one of the regions has unit measure,is the only one with zero entropy.

The probability of finding the system in a region $A _ { i }$ of the partition $\pmb { \alpha }$ may or may not be independent of the probability of finding it in the region $B _ { j }$ of the partition $\beta$ .For example,a mixing system that was in $B _ { j }$ to start with will certainly be in $\mathbf { T } ^ { n } B _ { j }$ - scattered throughout phase space after a large number $\pmb { n }$ of iterations.In this case the probabilities of the partitions $\beta$ and $\alpha \equiv \operatorname* { l i m } \mathbf { T } ^ { n } \beta$ for $n  \infty$ ,are independent. The combined partition into the regions $A _ { i } \cap B _ { j }$ with probabilities $\mu _ { i j } = \mu ( A _ { i } \cap B _ { j } )$ is denoted $\alpha \lor \beta$ f $\pmb { \alpha }$ and $\beta$ are independent, $\mu _ { i j } = \mu _ { i } \mu _ { j } .$

![](images/30e19587c12ae7ef2daf05d7aa82dba9c202f1c1c1b1f4af138c1cb689c2ccf3.jpg)  
Fig.3.11. The convexity of $\phi ( x ) = - x \log x$ is fundamental for the proof of important properties of the metric entropy.

# Exercise

Show that, if $\pmb { \alpha }$ and $\beta$ are independent, the entropy ofthe combined partition is

$$
h ( \alpha \vee \beta ) = h ( \alpha ) + h ( \beta ) .
$$

When $\pmb { \alpha }$ and $\beta$ are not independent, we define the conditional probability of finding the system in $A _ { i }$ , given that it is in $B _ { j }$ as

$$
\begin{array} { r } { \mu _ { i / j } = \mu _ { i j } / \mu _ { j } . } \end{array}
$$

The combined entropy then becomes

$$
\begin{array} { l } { { \displaystyle h ( \alpha \vee \beta ) = - \sum _ { i j } \mu _ { j } \mu _ { i / j } ( \log \mu _ { j } + \log \mu _ { i / j } ) } } \\ { { \displaystyle \qquad = - \sum _ { j } \mu _ { j } \log \mu _ { j } \sum _ { i } \mu _ { i / j } - \sum _ { j } \mu _ { j } \sum _ { i } \mu _ { i / j } \log \mu _ { i / j } } } \end{array}
$$

Defining the conditional entropy of $\pmb { \alpha }$ relative to $B _ { j }$ as

$$
h ( \alpha / B _ { j } ) = - \sum _ { i } \mu _ { i / j } \log \mu _ { i / j }
$$

and the conditional entropy ofα relative to the partition $\beta$ as the mean value

for $h ( \alpha / B _ { j } )$

$$
\begin{array} { r } { h ( \boldsymbol { \alpha } / \beta ) = \displaystyle \sum _ { j } \mu _ { j } h ( \boldsymbol { \alpha } / B _ { j } ) , } \end{array}
$$

we obtain

$$
h ( \alpha \vee \beta ) = h ( \beta ) + h ( \alpha / \beta ) .
$$

# Exercise

Use the convexity of the function in fig. 3.11 to prove that

$$
h ( \alpha / \beta ) \leq h ( \alpha ) .
$$

We can now return to the question of incomplete information about the system and its evolution. If a measurement localizes the system in one of the regions $A _ { j } .$ ，we reduce the uncertainty concerning its localization. The information produced by the measurement consists of the removal of uncertainty that preceded this event.The larger the uncertainty,the greater willbe the amount of information obtained by its removal. The entropy of a partition $\pmb { \alpha }$ has been shown to have properties that permit us to consider it as a measure of the uncertainty of $\pmb { \alpha }$ . We can therefore define the quantity of information obtained by localizing the system in one of the regions $A _ { j }$ as $h ( \alpha )$

If we make a measurement on $\pmb { \alpha } ,$ , having already ascertained the $B _ { j }$ into which the system belongs in the partition $\beta _ { : }$ ，the average increase of information will be $h ( \alpha / \beta )$ .This additional information is a maximum if $\pmb { \alpha }$ and $\beta$ are independent -in this case a measurement of $\beta$ in no way reduces the uncertainty of $\pmb { \alpha }$ .Though we have found that the present definition of entropy has desirable properties, it may still appear somewhat arbitrary. However,it is shown in Khinchin(1957) that this is the only definition that satisfies conditions (3.29) and (3.35).

We focus on the sequence of partitions $\mathbf { T } ^ { n } \alpha .$ It is demonstrated in Arnold and Avez (1968) that the limit

$$
h ( \alpha , \mathbf { T } ) \equiv \operatorname* { l i m } _ { n  \infty } { \frac { h ( \alpha \vee \mathbf { T } \alpha \vee \cdots \vee \mathbf { T } ^ { n - 1 } \alpha ) } { n } }
$$

exists. We call $h ( \alpha , \mathbf { T } )$ the entropy of $\pmb { \alpha }$ relative to $\mathbf { T }$ .Finally we define the metric entropy of the map $\mathbf { T }$ as

$$
h ( { \bf T } ) \equiv \operatorname* { s u p } h ( \alpha , { \bf T } ) ,
$$

where the supremum extends over all measurable partions. Evidently we always have $h ( \mathbf { T } ) \geq 0$

# Exercise

Prove that the metric entropy is invariant with respect to a coordinate transformation $\mathbf { x } ^ { \prime } = \mathbf { F } ( \mathbf { x } )$ ,that is, $h ( \mathbf { T } ) = h ( \mathbf { F } { \cdot } \mathbf { T } { \cdot } \mathbf { F } ^ { - 1 } )$ .

It is not usually feasible to compute the metric entropy of a dynamical system directly from its definition. Yet it is worthwhile to try to gain a feeling for the process involved. Each iteration leads to a new combined partition, which results from the addition of the boundaries of the regions $\mathbf { T } ^ { n } A _ { j }$ to the boundaries of all the previous partitions. For example, if the original partition divided phase space into $2 N$ regions ofequal measure and each iteration of the map led to a new partition that cut each region in half, then $h ( \alpha \vee \cdots \vee \mathbf { T } ^ { n - 1 } \alpha ) = n \log 2 + \log N ,$ so $h ( \alpha , T ) = \log 2$ This example shows that positive entropy requires exponential growth, with $\pmb { n } .$ of the number of regions in $\alpha \lor \cdots \lor \mathbf { T } ^ { n - 1 } \alpha .$ But it must be remembered that the number of regions in $\mathbf { T } ^ { n } \mathfrak { Q }$ is the same as that in $\pmb { \alpha }$ ,so an exponential growth of the combined partition demands an exponential growth of the boundary of the regions $\mathbf { T } ^ { n } A _ { j } .$ Only thus can the boundaries of $\mathbf { T } ^ { n } \mathfrak { Q }$ cut a constant proportion of the ever diminishing regions $\alpha \lor \cdots \lor \mathbf { T } ^ { n - 1 } \alpha .$ This does not occur for the translations of the torus studied in section 1.3.The length of the boundary of any region $\mathbf { T } ^ { n } A _ { j }$ is constant; hence, the entropy $h ( \alpha , \mathbf { T } )$ is zero for any partition $\pmb { \alpha }$ ,even though this system is ergodic.

For the cat map we do have exponential stretching of the boundaries of each region along the direction of the eigenvector $\xi _ { 1 }$ corresponding to the eigenvalue $\lambda _ { 1 }$ . If each region were collapsed back on itself as was the case with the horseshoe (but fitting exactly,as the full cat map itself), each region would be divided into $\lambda _ { 1 }$ equal regions. The result would be that

$$
h ( \mathbf { T } ) = \log \lambda _ { 1 } .
$$

This is the correct result, proved by Sinai (1959), which implies that the existence of many extra regions (due to the boundaries not fitting properly) is counterbalanced by the fact that the entropy is actually smaller than the maximum log $N$ .This result can be generalized to $r .$ -dimensional tori: if a linear map $\mathbf { T }$ of the torus has $r$ real and distinct eigenvalues, then

$$
h ( { \bf T } ) = \sum _ { | \lambda _ { i } | > 1 } \log | \lambda _ { i } | .
$$

It is usually very dificult to verify whether the properties of ergodicity, mixing and positive entropy hold for a given Hamiltonian system.The first systems for which this has been achieved are billiards,that is,the free motion of a particle in the plane within a given boundary.Usually one considers that the particle undergoes specular reflection at the boundary, but in Sinai's billiard shown in fig. 3.12a this is true only for encounters with the circular barrier. The boundary conditions along the square are taken to be periodic,so that the billiard in fact has the topology of a torus. The periodic representation of the torus is shown in fig. 3.12b. This system was proved by Sinai (1970) to have allthe chaotic properties,including positive entropy. Another system proved to be chaotic by Buminovitch(1974) is the stadium: the interior of a pair of semicircles joined by two straight segments.

![](images/eecf52632a248c865ab48d70d570faf42ea3cdaa6e6543126554d7498fd3702b.jpg)  
Fig.3.12. In Sinai's billiard the particle undergoes specular reflection at the circular barrier,while the boundary conditions on the square are periodic.Thus,the square in (a) is in fact a torus with the periodic representation depicted in (b).

The concept of entropy permits us to quantify the decay of information brought about by the entire flow of the system. Yet the loss of memory about approximate initial conditions is a local property of chaotic motion. Let us consider a small ball of radius $\varepsilon ( 0 )$ centred on the initial position of some orbit in phase space.The successive images of the ball will be distorted under the map T.In the limit $\varepsilon ( 0 ) \to 0$ ,we can use the linearized map DT,so that the ball develops into a small ellipsoid. Naming the principal axes of the ellipsoid as $\varepsilon _ { i } ( n )$ ，we define the $L$ yapunov exponents as

$$
\gamma _ { i } = \operatorname* { l i m } _ { \varepsilon ( 0 ) \to 0 } \operatorname* { l i m } _ { n \to \infty } \frac { 1 } { n } \log \frac { \varepsilon _ { i } ( n ) } { \varepsilon ( 0 ) } .
$$

# Exercise

Define the Lyapunov exponents in terms of the tangent space vectors introduced in chapter 2.

For a periodic orbit of period $r$ ,the above limit evidently exists and the $\gamma _ { i }$ are just the eigenvalues of $\mathcal { M } ^ { r } = D \mathbf { T } ^ { r }$ .Where periodic orbits are dense, we therefore expect that most orbits will have Lyapunov exponents. This is indeed the content of a theorem of Oseledec (1968), which holds under very general conditions.Furthermore,for a hyperbolic set with dense orbits, almost all orbits will share the same Lyapunov exponents. The largest positive exponent measures the rate of divergence between neighbouring orbits, whereas negative exponents measure convergence rates along stable manifolds. For a Hamiltonian system $\textstyle \sum \gamma _ { i } = 1$ ，whereas $\textstyle \sum \gamma _ { i } < 1$ for dissipative systems.

It was shown in the preceding section that the metric entropy will be positive only if the frontiers of a typical region grow exponentially with time.The possibility of choosing such a region as the small ball used to define the Lyapunov exponent suggests that positive entropy is connected to positive Lyapunov exponents. In the case of linear maps of the torus we simply have $\gamma _ { i } = \ln \vert \lambda _ { i } \vert$ , so equation (3.40) becomes

$$
h ( \mathbf { T } ) = \sum _ { \gamma _ { i } > 1 } \gamma _ { i } .
$$

Pesin (1977) has indeed shown that (3.42) can be generalized for a single region of connected chaotic motion. If there is more than one region (separated by invariant curves or manifolds), the generalization is

$$
h ( { \bf T } ) = \int d \mu \sum _ { \gamma _ { i } > 1 } \ d _ { 1 } \gamma _ { i } ( { \bf x } ) .
$$

This connection between the Lyapunov exponents and the metric entropy is of great practical importance, since the latter are much easier to compute.Lichtenberg and Lieberman (1983,chap.5) present a detailed discussion of this subject and provide many references.

# 3.6 The principle of uniformity

Hyperbolic sets are characterized by dense orbits and by a dense population of periodic orbits. The ergodic theory,briefly outlined in the two preceding sections, relies on the former and neglects the latter. Yet a dense orbit mimics every periodic orbit of the system arbitrarily closely for many periods, so it should be possible to replace the time average over a “typical orbit'by an average over allthe periodic orbits. Clearly the chaotic orbit will remain close to very unstable periodic orbits for a shorter time than the relatively stable ones.It follows that the mean over periodic orbits must be a weighted average.

The principle of uniform density of periodic orbits is most easily presented in the case of an area-preserving map in a region of area $\pmb { A }$ ,asin the appendix of Hannay and Ozorio de Almeida (1984).Let us consider a peaked function $\delta _ { \varepsilon } ( \mathbf { x } )$ ,centred on the origin but normalized to unity for all ε, so that for $\varepsilon \to 0$ it becomes a two-dimensional Dirac $\delta$ function. Then $\delta _ { \varepsilon } ( \mathbf { x } _ { n } - \mathbf { x } _ { 0 } )$ is a function of $\mathbf { x } _ { 0 }$ defined throughout the area $\pmb { A }$ ，which has peaks in all the regions where orbits return very close to their starting positions after precisely $\pmb { n }$ iterations. Another function of $\mathbf { x } _ { 0 }$ that we can construct is

$$
\Delta _ { \varepsilon , N } ( \mathbf { x } _ { 0 } ) = \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \delta _ { \varepsilon } ( \mathbf { x } _ { n } - \mathbf { x } _ { 0 } ) ,
$$

peaked in all the regions with orbits that return to a small neighbourhood of $\mathbf { x } _ { 0 }$ for some iteration $n \geq N$

One of the consequences of the Poincaré recurrence theorem discussed in section 3.4 is that all points of an area-preserving map are nonwandering; that is,the image of any neighbourhood $U$ of $x _ { 0 }$ will eventually intersect $U$ If we take this neighbourhood to be the area ε around $\mathbf { x } _ { 0 }$ , we see that there will be a peak of $\Delta _ { \mathfrak { e } , N }$ in the neighbourhood of any point $\mathbf { x } _ { 0 }$ in the limit $N \to \infty$ .This uniform distribution of peaks will make $\Delta _ { \varepsilon , N } ( \mathbf { x } _ { 0 } )$ a smooth function over $\pmb { A }$ . In fact, we can estimate when this will happen: Defining $\nu ( N )$ to be the number of periodic points with period equal to or smaller than $N$ ,the number of peaks in $\Delta _ { \varepsilon , N }$ will be equal to or greater than $\nu ( N )$ (equality being obtained in the limit $\varepsilon \to 0$ ). The smoothing of $\Delta _ { \varepsilon , N }$ will then occur when

$$
\varepsilon \nu ( N ) \gg A .
$$

For an ergodic system we can readily calculate this smooth limit, since

$$
\operatorname* { l i m } _ { N  \infty } \Delta _ { \varepsilon , N } ( \mathbf { x } _ { 0 } ) = \operatorname* { l i m } _ { N  \infty } \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \delta _ { \varepsilon } ( \mathbf { x } _ { n } - \mathbf { x } _ { 0 } ) = \overline { { \delta } } _ { \varepsilon } ( \mathbf { x } _ { n } - \mathbf { x } ) _ { \mathbf { x } _ { 0 } = \mathbf { x } } .
$$

It is important to note that the‘time' average on the right side is now taken over a function of $\mathbf { x } _ { 0 }$ ,centred on the immobile point $\mathbf { x }$ .The limit exists for almost all $\mathbf { x } _ { 0 }$ and in particular for $\mathbf { x } _ { 0 } = \mathbf { x }$ . The ergodic property then becomes

$$
\operatorname* { l i m } _ { N  \infty } \Delta _ { \varepsilon , N } ( \mathbf { x } _ { 0 } ) = \langle \delta _ { \varepsilon } ( \mathbf { x } _ { 0 } - \mathbf { x } ) \rangle = A ^ { - 1 } .
$$

The principle of uniformity can now be stated as the conjecture that we can take the limit $\pmb { \varepsilon }  \mathbf { 0 }$ on the left side of (3.47) before the $N \to \infty$ limit. In practice this means that we can make the $\pmb { \ell }$ neighbourhoods sufficiently

smallso as to be able to neglect the contribution of nonperiodic orbits to $\Delta _ { \mathfrak { s } , N }$ , while making $\nu ( N )$ large enough for (3.45) to be valid. In conclusion

$$
\operatorname* { l i m } _ { N  \infty } \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \delta ( \mathbf { x } _ { n } - \mathbf { x } _ { 0 } ) = \frac { 1 } { A }
$$

is a sum over periodic orbits,though the equation makes sense only for arbitrarily small smoothing of the $\delta$ functions.Integrating both sides of (3.48) over $\mathbf { x } _ { 0 }$ , we obtain the sum rule over periodic points,

$$
\operatorname* { l i m } _ { N \to \infty } N ^ { - 1 } \sum _ { n = 1 } ^ { N } \sum _ { j = 1 } ^ { \nu ( n ) - \nu ( n - 1 ) } | \mathrm { d e t } ( \mathcal { M } _ { j } ^ { n } - 1 ) | ^ { - 1 } \to 1 .
$$

The weight of a periodic point is given by a factor that appeared in(2.23). It depends on the stability matrix $\mathcal { M }$ introduced in section 2.3 and is unbounded as the linearized map $D \mathbf { T } ^ { n }$ approaches the unit map.

For a fully chaotic system with positive entropy $h ( \mathbf { T } )$ the weight of an orbit of very high period will have the limit

$$
| \mathrm { d e t } ( \mathcal { M } _ { j } ^ { n } - { \bf 1 } ) | ^ { - 1 } \underset { n  \infty } { \longrightarrow } | ( e ^ { n \gamma } - 1 ) ( e ^ { - n \gamma } - 1 ) | ^ { - 1 } \underset { n  \infty } { \longrightarrow } e ^ { - n \gamma } = \exp [ - n h ( { \bf T } ) ] ,
$$

where $\gamma$ is the positive Lyapunov exponent. The contribution of any finite number of orbits to the sum in (3.49) can be neglected,so we can use (3.50) for all the orbits. Since the contribution of each orbit is $n \ { \mathsf { e x p } } ( - n h )$ we obtain the average number of periodic orbits with period $\pmb { n }$ as

$$
\nu ( n ) - \nu ( n - 1 ) { \underset { n \to \infty } { \longrightarrow } } \exp ( n h ) / n .
$$

The above argument is strictly valid only if $\pmb { n }$ is a prime number. Otherwise, we have neglected the repeated contribution of orbits for which $n / m$ is an integer for some integer m.However, taking(3.51) as a first approximation we verify that the number of orbits with period $n / m$ is indeed exponentially smaller than the number with period $\pmb { n }$ .Rigourous results concerning uniformity and exponential proliferation of periodic orbits are presented by Parry and Pollicot (1983) and Parry (1984).

# Exercise

Though the uniformity principle is restricted to ergodic systems, show that Birkhoff's local ergodic theorem can be used to extend the validity of the sum rule (3.49) to systems that are merely recurrent.

The uniformity principle and the sum rule may be applied to the Poincaré map of a Hamiltonian system. It is worthwhile, however, to extend them to the continuous periodic orbits in the flow itself. The first difficulty is that ergodic flow on the energy shell does not preserve area, though it does conserve the Liouville measure (3.13). For this reason we define the shell $\delta$ function $\delta _ { \mu } ( \mathbf { x } )$ by its properties

$$
\delta _ { \mu } ( { \bf x } ) = 0 , \qquad { \bf x } \ne 0
$$

(choosing the origin to lie on the shell and

$$
\int d \mu \delta _ { \mu } ( { \bf x } ) = 1 .
$$

Just as with the usual Dirac $\delta$ functions,we must understand this to be the limit of peaked functions,but I will leave out explicit reference to the smearing parameter so as not to encumber the notation.

The time average can be written in the form

$$
\bar { \delta } _ { \mu } ( { \bf x } ( t ) - { \bf x } ) = \operatorname * { l i m } _ { T  \infty } \frac { 1 } { 2 T } \int _ { - T } ^ { T } d t \bar { \delta } _ { \mu } ( { \bf x } ( t ) - { \bf x } ) ,
$$

where the slash in the integral sign excludes an arbitrarily small neighbourhood of the origin. Its equivalence to the configurational average

$$
\langle \delta _ { \mu } ( { \bf x } ( 0 ) - { \bf x } ) \rangle = \mu ^ { - 1 } = ( d V / d E ) ^ { - 1 } ,
$$

for the choice of $\mathbf { x } ( 0 ) = \mathbf { x }$ , leads to the uniformity in ${ \bf x } ( 0 )$ of

$$
\operatorname * { l i m } _ { T  \infty } \frac { 1 } { 2 T } \int _ { - T } ^ { T } d t \bar { \delta } _ { \mu } ( { \bf x } ( t ) - { \bf x } ( 0 ) ) = \mu ^ { - 1 } .
$$

This formula for the uniform distribution of periodic orbits is exactly analogous to the one for maps.The need to exclude a neighbourhood of the origin from the average over time here becomes evident.

The sum rule over periodic orbits is obtained by integrating over the measure $\mu$ of the whole shell:

$$
\operatorname* { l i m } _ { T \to \infty } \frac { 1 } { 2 T } \int _ { - T } ^ { T } d t \int d \mu \delta _ { \mu } ( \mathbf { x } ( t ) - \mathbf { x } ( 0 ) ) = 1 .
$$

The configurational integral can be subdivided into integrals in the neighbourhood of each periodic orbit.For each of these we can introduce the local coordinate system presented in section 2.5. The shell $\delta$ function $\delta _ { \mu }$ then takes on the simple form

$$
\delta _ { \mu } ( \theta , P , Q ) = ( d H / d J ) \delta ( \theta , P , Q ) .
$$

Consequently,

$$
\begin{array} { l } { \displaystyle \int _ { j \mathrm { f h o r b i t } } d t d \mu \delta _ { \mu } ( \mathbf { x } ( t ) - \mathbf { x } ( 0 ) ) = \displaystyle \int d t d \theta _ { 0 } d P _ { 0 } d Q _ { 0 } \delta ( \theta _ { 0 } + \omega _ { j } t - ( \theta _ { 0 } + 2 \pi m ) ) } \\ { \displaystyle \qquad \times \delta ( ( P , Q ) _ { t } - ( P , Q ) _ { 0 } ) } \\ { \displaystyle = | \tau _ { j } | | \det \{ \mathcal { M } _ { j } ^ { m } - 1 \} | ^ { - 1 } , \qquad ( 3 . 5 } \end{array}
$$

so that the sum rule becomes

$$
\operatorname* { l i m } _ { T \to \infty } \frac { 1 } { 2 T } \sum _ { | m \tau _ { j } | < T } | \tau _ { j } | | \operatorname* { d e t } \left\{ \mathcal { M } _ { j } ^ { m } - \mathbf { 1 } \right\} | ^ { - 1 } = 1 .
$$

As in the discrete case, it is not necessary to presuppose ergodicity to arrive at this sum rule,though it is essential to the unformity principle(3.56). For a system with positive entropy we can neglect the contribution of multiple repetitions of periodic orbits,just as in the discrete case. For large periods the number of periodic orbits increases exponentially, permitting us to define the weighted density of periodic orbits,

$$
f ( \tau ) = \sum _ { j } | \tau _ { j } | | \operatorname* { d e t } \{ \mathcal { M } _ { j } - \mathbf { 1 } \} | ^ { - 1 } \delta ( \tau - \tau _ { j } ) \underset { \tau \to \infty } { \longrightarrow } 1 ,
$$

as can be verified by integrating over $\tau$

In chapter 9, which presents the theory of the quantum energy spectrum in terms of the classical periodic orbits, the factor $| \mathsf { d e t } ( \mathcal { M } ^ { m } - \mathsf { 1 } ) | ^ { - 1 }$ will reappear and (3.61) becomes the basis for an important result concerning correlations of the spectrum.

# 4

# Normal forms

Having established the ubiquity of periodic orbits in dynamical systems, we now return to the study of the motion near a given periodic orbit, fixed point or point of equilibrium.The Hartman-Grobman theorem of section 2.2 guarantees the existence of a continuous coordinate transformation that linearizes the vector field near a hyperbolic fixed point, but no indication is given as to how to construct this transformation. The method of normal forms,invented by Poincaré, consists of eliminating nonlinear terms of the vector field by successive polynomial transformations. If this process can be carried out to all orders,the resulting compound transformation can be shown to be convergent in some cases, and an analytic reduction of the nonlinear vector field to a linear one is thus achieved. This transformation can be approximated to arbitrary accuracy.

One of the cases in which this process can never be carried out is that of Hamiltonian systems. The Hamiltonian cannot generally be made quadratic by a canonical transformation, though Birkhoff showed that it can be simplified into a form that shares some of the important features of quadratic Hamiltonians.For hyperbolic points this transformation is analytic in a narrow neighbourhood of the separatrices,allowing us to calculate precisely some homoclinic orbits and the periodic orbit families that accumulate on them.

The elimination of nonlinear terms of low order near stable points in Hamiltonian systems allows a qualitative understanding of the motion in their neighbourhood, even though the transformation cannot be extended to infinite orders. This is important in the case of the bifurcation of stable orbits discussed at the end of this chapter. The nonconvergence of the Birkhoff transformation is due to the intricate nature of the motion in these regions,which is studied in chapters 5 and 6.

# 4.1 General systems

A linear coordinate transformation can take a dynamical system into the form

$$
\dot { \mathbf { x } } = \mathcal { L } \mathbf { x } + \mathbf { g } _ { k } ( \mathbf { x } ) + \mathbf { g } _ { k + 1 } ( \mathbf { x } ) + \cdots
$$

in the neighbourhood of the origin,an equilibrium with $N$ distinct eigenvalues. Here $\mathcal { L }$ is a diagonal matrix with elements $\lambda _ { j }$ ，and the components of the vector fields $\mathbf { g } _ { j }$ are homogeneous polynomials of order $j .$ We seek a nonlinear coordinate transformation

$$
\mathbf { x } = \mathbf { y } + \mathbf { h } ( \mathbf { y } ) ,
$$

the components of $\mathbf { h }$ being homogeneous polynomials of order $\mathbf { k }$ ，that eliminates $\mathbf { g } _ { \pmb { k } }$ from the dynamical system. Introducing (4.2) into (4.1), we obtain

$$
\begin{array} { r l } & { \dot { \mathbf { y } } = ( \mathbf { 1 } + \hat { \alpha } \mathbf { h } / \hat { \sigma } \mathbf { y } ) ^ { - 1 } \{ \mathcal { L } ( \mathbf { y } + \mathbf { h } ( \mathbf { y } ) ) + \mathbf { g } _ { k } ( \mathbf { y } + \mathbf { h } ( \mathbf { y } ) ) + \cdots \} } \\ & { \quad = \mathcal { L } \mathbf { y } + \{ \mathcal { L } \mathbf { h } ( \mathbf { y } ) - ( \hat { \alpha } \mathbf { h } / \hat { \sigma } \mathbf { y } ) \mathcal { L } \mathbf { y } + \mathbf { g } _ { k } ( \mathbf { y } ) \} + \cdots , } \end{array}
$$

neglecting all terms of order $\geq k + 1$ . The required polynomials $h _ { j } ( \mathbf { y } )$ thus satisfy the equations

$$
\lambda _ { j } h _ { j } - \sum _ { i } { \frac { \partial h _ { j } } { \partial y _ { i } } } \lambda _ { i } y _ { i } = g _ { k j } .
$$

The substitution of $h _ { j }$ by any of its monomials $\left( y _ { 1 } ^ { m _ { 1 } } \cdots y _ { N } ^ { m _ { N } } \right)$ on the left side of (4.4) gives

$$
\lambda _ { j } ( y _ { 1 } ^ { m _ { 1 } } \cdots y _ { N } ^ { m _ { N } } ) - \sum _ { i } \lambda _ { i } y _ { i } \frac { \partial } { \partial y _ { i } } ( y _ { 1 } ^ { m _ { 1 } } \cdots y _ { N } ^ { m _ { N } } ) = \left( \lambda _ { j } - \sum _ { i } \lambda _ { i } m _ { i } \right) ( y _ { 1 } ^ { m _ { 1 } } \cdots y _ { N } ^ { m _ { N } } ) ;
$$

so we can solve (4.4) by choosing the coefficients of the monomials in $h _ { j }$ to be equal to the coefficients in $g _ { k j }$ divided by $\begin{array} { r l } { \big ( \sum _ { i } \lambda _ { i } m _ { i } - \lambda _ { j } \big ) } \end{array}$ ·

The transformation eliminating the terms ${ \bf g } _ { k } ( { \bf x } )$ from the vector field modifies the higher-order terms,but the form of the dynamical system will be the same as (4.1), with $k$ replaced by $k + 1$ .The process of elimination can be carried through indefinitely unless there exists a vector $\mathbf { m }$ with positive integer components,for which

$$
\lambda _ { j } = \sum _ { i = 1 } ^ { N } m _ { i } \lambda _ { i } = \mathbf { m } \cdot \boldsymbol { \mathcal { L } }
$$

for one of the eigenvalues. The equality (4.6) is known as the resonance condition,and the smallest $k = \textstyle \sum _ { i } m _ { i }$ for which it holds is the order of the resonance. We can obviously eliminate all the terms $\mathbf { g } _ { 2 } \cdots \mathbf { g } _ { k - 1 }$ of a resonant system of order $k _ { : }$ ，and if the system is nonresonant,we can formally eliminate all the nonlinear terms.Examples of resonant systems are those with $\lambda _ { 1 } = 2 \lambda _ { 2 }$ (second order) and $\lambda _ { 1 } + \lambda _ { 2 } = 0$ (third order, since $\lambda _ { 1 } = 2 \lambda _ { 1 } + \lambda _ { 2 } )$ . The relation $2 \lambda _ { 1 } = 3 \lambda _ { 2 }$ does not imply a resonance.

It is easy to correlate some resonances to the configuration of the motion. This is the case of a conjugate pair of imaginary eigenvalues. As we have seen in section 1.2, the linear motion then has a centre, so that the nonlinear terms may push the orbits either towards the origin or away from it. The case of two degenerate real (negative) eigenvalues can likewise be understood.The linear motion is then radial towards the origin. This is the borderline between two nodes, having either eigenvector as the ‘fast' or the ‘slow' axis. A perturbation may also make the dynamical matrix undiagonalizable.

Example. Consider the system ${ \dot { \mathbf { x } } } = \mathbf { f } ( { \mathbf { x } } )$

$$
\dot { x } _ { 1 } = \lambda _ { 1 } x _ { 1 } , \qquad \dot { x } _ { 2 } = \lambda _ { 2 } x _ { 2 } + a x _ { 1 } ^ { 3 } .
$$

The transformation $\mathbf x \to \mathbf y$

$$
y _ { 1 } = x _ { 1 } ^ { 3 } , \qquad y _ { 2 } = x _ { 2 } ,
$$

linearizes this system in the form

$$
\dot { y } _ { 1 } = 3 \lambda _ { 1 } y _ { 1 } , \qquad \dot { y } _ { 2 } = \lambda _ { 2 } y _ { 2 } + a y _ { 1 } .
$$

This system can be diagonalized by the transformation $\mathbf y \to \mathbf Y$ ：

$$
Y _ { 1 } = y _ { 1 } , \qquad Y _ { 2 } = y _ { 2 } - { \frac { a } { 3 \lambda _ { 1 } - \lambda _ { 2 } } } y _ { 2 } .
$$

Finally, the transformation $\mathbf { Y }  \pmb { \mathbb { \mathfrak { X } } } .$

$$
Y _ { 1 } = \mathfrak { x } _ { 1 } ^ { 3 } , \qquad Y _ { 2 } = \mathfrak { x } _ { 2 } ,
$$

brings the dynamical system to the form $\pmb { \dot { \ x } } = \pmb { D } \mathbf { f } ( \pmb { \ x } )$ .The full transformation $\pmb { \mathscr { X } }  \pmb { \mathscr { X } }$ is simply

$$
\pmb { x } _ { 1 } = \pmb { x } _ { 1 } , \qquad \pmb { x } _ { 2 } = \pmb { x } _ { 2 } + \frac { a } { 3 \lambda _ { 1 } - \lambda _ { 2 } } \pmb { x } _ { 1 } ^ { 3 } .
$$

It is analytic everywhere unless there is a resonance: $\lambda _ { 2 } = 3 \lambda _ { 1 }$ . In this case there is nothing special about the resonant system itself. However, it becomes impossible to diagonalize the degenerate linear system (4.10).

# Exercise

It is possible to reduce systems with degenerate eigenvalues to a normal form if the eigenvalues are degenerate, though the solution no longer decouples in terms of monomials (Arnold,1982). Find the linear equations for the coefficients in $\mathbf { h }$ for $k = 2$ if the diagonal matrix can be reduced only to a two-dimensional Jordan block.

The absence of an exact resonance does not guarantee the convergence of the normal-form transformation to the resulting linear system. The problem is that the resonance condition may be approached closely many times with arbitrary precision,as $| { \bf m } | \to \infty$ ． This is known as the small-denominator problem: Some of the coefficients of the successive normal-form transformations become arbitrarily large. The necessary and sufficient condition for this not to occur is that $\mathcal { L }$ lie in the Poincaré domain: All the eigenvalues lie on one side of a straight line on the complex $\lambda$ plane,whereas the origin lies on the other side.To see that this is sufficient, we project all the eigenvalues onto the normal to the straight line, as in fig. 4.1. All of these will be greater than or equal to the distance between the straight line and the origin.Hence,the linear combination of eigenvalues $\mathbf { m } \cdot \mathcal { L }$ has an arbitrarily large normal projection as $| { \bf m } |  \infty$ It must therefore become greater than the projection of any individual eigenvalue.

![](images/98f5142658ba318a0998b9e616645aebe8b988acef76d92a1be9b659b0c1cb73.jpg)  
Fig. 4.1.The eigenvalues lie in the Poincareé domain if they areallon the opposite side of a straight line with respect to the origin.Convergence of the normal form in some neighbourhood of the origin is guaranteed in this case.

Poincaré demonstrated the convergence of the normal-form transformation ina neighbourhood of the equilibrium for eigenvalues in the Poincaré domain. In the Siegel domain, complementary to the Poincaré domain, convergence is still possible according to Siegel's theorem (demonstrated in Arnold,1982,sec.28). The sufficient condition is that there exist positive numbers $c$ and $\nu$ such that

$$
| \lambda _ { j } - \mathbf { m } \cdot \mathcal { L } | \geq C / | \mathbf { m } | ^ { \nu }
$$

for each eigenvalue $\lambda _ { j }$ and for all positive-integer vectors m. This strange condition resembles the one for the convergence of the circle map, to be discussed in detail in the next chapter.

There are two alternatives by which we can extend the normal-form analysis to periodic orbits. One is to consider the Poincaré section near a periodic orbit and to derive the normal form in the neighbourhood of the fixed point. This procedure, presented in Arnold (1982), is simple for general systems, but its adaptation to Hamiltonian systems is not easy. Otherwise,we can use periodic coordinates based on the periodic orbit, as in section 2.5,and work with the reduced time-dependent system.

Consider,then,the linear part of this time periodic system:

$$
\dot { \mathbf { x } } = \mathcal { A } ( t ) \mathbf { x } .
$$

We now define the matrix $\mathcal { L }$ so that the map after the period $2 \pi$ takes the form

$$
\mathbf { x } = \exp ( 2 \pi \mathcal { L } ) \mathbf { x } _ { 0 } = \left( \exp \int _ { 0 } ^ { 2 \pi } \mathcal { A } ( t ) d t \right) \mathbf { x } _ { 0 } .
$$

The coordinate transformation

$$
\mathbf { x } = \left( \exp \int _ { 0 } ^ { t } { \mathcal { A } } ( t ) d t \right) \exp ( - t { \mathcal { L } } ) \mathbf { y }
$$

can then be verified to reduce (4.14) to the time-dependent linear system

$$
\dot { \mathbf { y } } = \mathcal { L } \mathbf { y } .
$$

f $\mathcal { L }$ has distinct eigenvalues, it can be diagonalized, so we will suppose $\mathcal { L }$ to be diagonal as in the time-independent theory.

We seek again a nonlinear coordinate transformation that eliminates the term $\mathbf { g } _ { \pmb { k } }$ (of order $\geq 2$ ）from the expansion

$$
\dot { \mathbf { x } } = \mathcal { L } \mathbf { x } + \mathbf { g } _ { k } ( \mathbf { x } , t ) + \mathbf { g } _ { k + 1 } ( \mathbf { x } , t ) + \cdots .
$$

Thus substitution

$$
\mathbf { x } = \mathbf { y } + \mathbf { h } ( \mathbf { y } , t ) ,
$$

where h is a vector with polynomial components $h _ { j }$ in $\mathbf { y }$ that has periodic coefficients in $t$ ,leads to the set of equations

$$
\lambda _ { j } h _ { j } - \sum _ { i } \frac { \partial h _ { j } } { \partial y _ { i } } \lambda _ { i } y _ { i } - \frac { \partial h _ { j } } { \partial t } = - g _ { k j } ( \mathbf { y } , t ) .
$$

Expanding the components in Fourier series,

$$
h _ { j } ( { \bf y } , t ) = \sum _ { \substack { l = - \infty } } ^ { \infty } \sum _ { m _ { 1 } + \cdots + m _ { N } = k } h _ { j , m , l } y _ { 1 } ^ { m _ { 1 } } \cdots y _ { N } ^ { m _ { N } } e ^ { i l t } ,
$$

and proceeding likewise with the field components $g _ { k j }$ ，we obtain the formal solution

$$
h _ { j , \mathbf { m } , l } = \frac { g _ { k j , \mathbf { m } , l } } { i l + \mathbf { m } \cdot \mathcal { L } - \lambda _ { j } } ,
$$

unless the resonance condition

$$
\lambda _ { j } = \mathbf { m } \cdot \boldsymbol { \mathcal { L } } + i l
$$

is satisfied.

The question of convergence of the normal-form series is dealt with in much the same way as in the time-dependent problem.The difference lies in the imaginary number $i l .$ ,which limits the Poincaré domain to be the set of matrices $\mathcal { L }$ ，the eigenvalues of which have all positive real parts or all negative real parts. Convergence is guaranteed in the Poincaré domain, whereas small denominators again appear in the complementary Siegel domain.

# 4.2 The Birkhoff normal form

It was shown in section 1.2 that the eigenvalues of Hamiltonian systems always arise in pairs: $\lambda , - \lambda .$ In the context of normal forms they therefore have a third-order resonance.Hence,it is impossible to linearize Hamiltonian systems by an analytic canonical transformation. The best that one can aim for is to simplify their Taylor expansion at an equilibrium or periodic orbit,as with non-Hamiltonian resonances treated by Arnold (1982) and Guckenheimer and Holmes (1983).

The special feature of the Birkhoff normal form is that it is a reduction of the Hamiltonian rather than the full dynamical system. The generating function $\pmb { S } ( \pmb { \mathfrak { p } } , \pmb { \mathfrak { q } } , t )$ defines implicitly a canonical transformation $( { \pmb { \mathsf { p } } } , { \pmb { \mathsf { q } } } ) \to ( { \pmb { \mathsf { p } } } , { \pmb { \mathsf { q } } } )$ by the equations

$$
{ \bf p } = \partial S / \partial { \bf q } , \qquad { \bf q } = \partial S / \partial { \bf p } .
$$

The Hamiltonian is concomitantly transformed by

$$
H ( \mathfrak { p } , \mathfrak { q } ) = H ( \mathfrak { p } , \mathfrak { q } ) + \partial S / \partial t .
$$

The idea is thus to study the effect of polynomial generating functions on the Taylor expansion of the Hamiltonian. The treatment here will be limited to a single degree of freedom, to avoid encumbering the notation, for the generalization is obvious. Since the system is time periodic,the foregoing also applies to the neighbourhood of a periodic orbit of an autonomous system with two freedoms,as discussed in section 2.5.

The simplest case is the unstable equilibrium. The Taylor-Fourier expansion of the Hamiltonian then has the form

$$
H ( p , q , t ) = \lambda p q + \sum _ { \alpha + \beta = k } ^ { \infty } \ \sum _ { l = - \infty } ^ { \infty } H _ { \alpha \beta l } p ^ { \alpha } q ^ { \beta } \exp ( i l t ) ,
$$

where $k > 2$ . This is transformed by the generating function

$$
S ( { \mathfrak { p } } , q , t ) = { \mathfrak { p } } q + \sum _ { \alpha + \beta = k } \ \sum _ { l = - \infty } ^ { \infty } S _ { \alpha \beta l } { \mathfrak { p } } ^ { \alpha } q ^ { \beta } \exp ( i l t ) .
$$

According to (4.24) the first term of $s$ generates the identity transformation. The second term will be small, of order $k _ { : }$ ，near the origin. The series for the first two partial derivative,

$$
\begin{array} { l } { { \displaystyle p = \partial S / \partial q = \mathfrak { p } \Bigg [ 1 + \sum _ { \iota , \alpha + \beta = k } \beta S _ { \alpha \beta \iota } \mathfrak { p } ^ { \alpha - 1 } q ^ { \beta - 1 } \exp ( i l t ) \Bigg ] , } } \\ { { \displaystyle \mathfrak { q } = \partial S / \partial \mathfrak { p } = q \Bigg [ 1 + \sum _ { \iota , \alpha + \beta = k } \alpha S _ { \alpha \beta \iota } \mathfrak { p } ^ { \alpha - 1 } q ^ { \beta - 1 } \exp ( i l t ) \Bigg ] , } } \\ { { \displaystyle \partial S / \partial t = \sum _ { \iota , \alpha + \beta = k } i l S _ { \alpha \beta \iota } \mathfrak { p } ^ { \alpha } q ^ { \beta } \exp ( i l t ) , } } \end{array}
$$

can be inverted up to order $k$ to yield the explicit transformation,

$$
\begin{array} { l } { { \displaystyle p = \mathfrak { p } \Bigg [ 1 + \sum _ { \iota , \alpha + \beta = k } \beta S _ { \alpha \beta \iota } \mathfrak { p } ^ { \alpha - 1 } \mathfrak { q } ^ { \beta - 1 } \exp ( i l t ) + \cdots \Bigg ] , } } \\ { { \displaystyle q = \mathfrak { q } \Bigg [ 1 - \sum _ { \iota , \alpha + \beta = k } \alpha S _ { \alpha \beta \iota } \mathfrak { p } ^ { \alpha - 1 } \mathfrak { q } ^ { \beta - 1 } \exp ( i l t ) + \cdots \Bigg ] , } } \\ { { \displaystyle \frac { \partial S } { \partial t } = \sum _ { \iota , \alpha + \beta = k } i l S _ { \alpha \beta \iota } \mathfrak { p } ^ { \alpha } \mathfrak { q } ^ { \beta } \exp ( i l t ) + \cdots . } } \end{array}
$$

The quadratic part of the Hamiltonian becomes

$$
\lambda p q = \lambda \mathfrak { p q } \Bigg [ 1 + \sum _ { \substack { l , \alpha + \beta = k } } ( \beta - \mathfrak { \alpha } ) \mathfrak { p } ^ { \alpha - 1 } \mathfrak { q } ^ { \beta - 1 } \exp ( i l t ) + \cdots \Bigg ] ,
$$

so the full Hamiltonian takes the form

$$
H ( \mathfrak { p } , \mathfrak { q } , t ) = \lambda \mathfrak { p } \mathfrak { q } + \sum _ { l , \alpha + \beta = k } \left\{ H _ { \alpha \beta l } + [ \lambda ( \beta - \alpha ) - i l ] \mathbb { S } _ { \alpha \beta l } \mathfrak { p } ^ { \alpha } \mathfrak { q } ^ { \beta } \exp ( i l t ) + \cdots \right\} .
$$

We can therefore eliminate all the terms of order $k$ with the choice

$$
S _ { \alpha \beta l } = \frac { - H _ { \alpha \beta l } } { \lambda ( \beta - \alpha ) - i l } ,
$$

except for the term $\alpha = \beta , l = 0$ ，that is, the term $H _ { \alpha \alpha 0 } ( { \mathfrak { p q } } ) ^ { \alpha }$ .Note that the inclusion of such a term in (4.26), with 2α <k, would not alter in any way the form of the $k \mathrm { \cdot }$ -order terms in (4.31). Hence,we can iterate the process of eliminating higher and higher order terms of the Hamiltonian, so as to obtain the kth-order Birkhoff normal form

$$
H ( { \mathfrak { p } } , { \mathfrak { q } } , t ) = \lambda { \mathfrak { p } } { \mathfrak { q } } + H _ { 2 } ( { \mathfrak { p } } { \mathfrak { q } } ) ^ { 2 } + \cdots + H _ { k } ( { \mathfrak { p } } { \mathfrak { q } } ) ^ { k / 2 } + \sum _ { l , \alpha + { \beta } = k + 1 } H _ { \alpha \beta l } { \mathfrak { p } } ^ { \alpha } { \mathfrak { q } } ^ { \beta } \exp ( i l t )
$$

for any even $k$

Differentiating the Hamiltonian in the normal form results in a polynomial dynamical system with odd-order terms, which correspond to the resonant terms of the Poincaré normal form discussed in the previous section. Within that context the Hamiltonian system is in the Siegel domain; that is, in addition to the exact resonances, it is also subject to small denominators. The nontrivial content of Birkhoff's construction is seen from the fact that there are no small denominators in the successive transformations whose generating functions have coefficients given by (4.32).The expectation that the normal-form transformation is convergent for $k \to \infty$ is indeed borne out by Moser (1956) for a disc around the origin. We shall discuss the motion near an unstable orbit in the next section.

The Hamiltonian near a stable equilibrium has the Taylor-Fourier expansion

$$
H ( { \mathfrak { p } } , { \mathfrak { q } } , t ) = { \frac { \omega } { 2 } } ( { \mathfrak { p } } ^ { 2 } + { \mathfrak { q } } ^ { 2 } ) + \sum _ { \alpha + \beta = 3 } ^ { \alpha + \beta = \infty } \sum _ { l } H _ { \alpha \beta l } ^ { \prime } { \mathfrak { p } } ^ { \alpha } { \mathfrak { q } } ^ { \beta } \exp ( i l t ) ,
$$

where $k > 2$ 、This form is not convenient for the deduction of the normal-form transformation, so we complexify the Hamiltonian; that is, considering $p$ and $\pmb q$ to be complex variables,we make the linear transformation

$$
z = p + i q , \qquad z ^ { * } = p - i q .
$$

The variables $\pmb { z }$ and $z ^ { * }$ are considered to be independent.However, if the initial conditions for $p$ and $q$ are real, $z ( t )$ and $z ^ { * } ( t )$ will remain complex conjugate solutions for all $t _ { : }$ ,as discussed in section 1.1.

# Exercise

Verify that the trajectories $z ( t )$ and $z ^ { * } ( t )$ satisfy Hamilton's equations with the Hamiltonian

$$
- 2 i H ( p ( z , z ^ { * } ) , q ( z , z ^ { * } ) , t ) = - i \omega z z ^ { * } + \sum _ { \alpha + \beta = 3 } ^ { \alpha + \beta = \infty } \sum _ { l } H _ { \alpha \beta l } z ^ { \alpha } z ^ { * \beta } \exp ( i l t ) .
$$

Following exactly the same method as for the unstable case, we can now reduce the Hamiltonian to the kth-order normal form:

$$
- 2 i H = - i { \omega _ { 3 3 } } ^ { * } + H _ { 2 } ( { _ 3 3 } ^ { * } ) ^ { 2 } + \cdots + H _ { k } ( { _ { 3 3 } } ^ { * } ) ^ { k / 2 }
$$

That is,we eliminate the‘nondiagonal’ coefficients of the Hamiltonian through the choice

$$
S _ { \alpha \beta l } = \frac { i H _ { \alpha \beta l } } { \omega ( \alpha - \beta ) - l }
$$

for the coefficients of the generating function

$$
S ( { \bf { \bar { 3 } } } , z ^ { * } , t ) = { \bf { \bar { 3 } } } z ^ { * } + \sum _ { \substack { l , \alpha + \beta = k } } S _ { \alpha \beta l } { \bf { \bar { 3 } } } ^ { \alpha } z ^ { * \beta } \exp ( i l t )
$$

of the transformation $( z , z ^ { * } ) \to ( { \mathfrak { z } } , { \mathfrak { z } } ^ { * } )$

This process can be carried through indefinitely only if the frequency $\omega$ is not a rational number. Otherwise, the maximum order for the normal form will be the highest $\alpha + \beta = k$ for which the resonance condition

$$
\omega ( \alpha - \beta ) - l = 0
$$

is not met. Even for irrational frequencies we are beset by small denominators,arising for all $\alpha , \beta$ and $l .$ ,such that $l ( \alpha - \beta )$ is a good rational approximation to $\omega$ .These near resonances lead usually to the divergence of the normal form for stable periodic orbits, as will be shown in section 4.4. Only the time-independent Hamiltonian with a single freedom is exempt from resonances or small denominators.

The procedure for deducing the normal form for autonomous systems with two freedoms (or more) is essentially the same as above. If the linearized Hamiltonian is $\lambda _ { 1 } p _ { 1 } q _ { 1 } + \lambda _ { 2 } p _ { 2 } q _ { 2 }$ , we can use the real coordinates, obtaining a normal form with small denominators (and resonances if $\lambda _ { 1 }$ and $\lambda _ { 2 }$ are rationally related). For $\lambda _ { 1 } p _ { 1 } q _ { 1 } + ( \omega _ { 2 } / 2 ) ( p _ { 2 } ^ { 2 } + q _ { 2 } ^ { 2 } ) .$ ，we proceed by complexifying the $( p _ { 2 } , q _ { 2 } )$ coordinates.The resultant normal form has no small denominators. Finally,we complexify both pairs of coordinates to obtain the normal form for a stable equilibrium. This is the case that is studied most extensively in spite of the presence of small denominators. Most presentations follow a more abstract algebraic approach,which leads to useful computational methods. These are reviewed by Lichtenberg and Lieberman (1983).

# Exercise

Show that the complexification

$$
\begin{array} { r l } { p _ { 1 } ^ { \prime } = p _ { 1 } - i p _ { 2 } , \quad } & { { } q _ { 1 } ^ { \prime } = q _ { 1 } + i q _ { 2 } } \\ { p _ { 2 } ^ { \prime } = p _ { 1 } + i p _ { 2 } , \quad } & { { } q _ { 2 } ^ { \prime } = q _ { 1 } - i q _ { 2 } } \end{array}
$$

takes the linear Hamiltonian system $H = \lambda ( p _ { 1 } q _ { 1 } + p _ { 2 } q _ { 2 } ) + \omega ( p _ { 1 } q _ { 2 } - q _ { 1 } p _ { 2 } ) ,$ with a complex quartet of eigenvalues, into the form $H ^ { \prime } = ( \lambda - i \omega ) p _ { 1 } ^ { \prime } q _ { 1 } ^ { \prime } +$ $( \lambda + i \omega ) p _ { 2 } ^ { \prime } q _ { 2 } ^ { \prime }$ . Show that the normal form for $H ^ { \prime }$ has no small denominators.

# 4.3 Homoclinic motion revisited

The Birkhoff-Moser theorem,which establishes the existence of an analytic transformation reducing an unstable time-periodic system to its Birkhoff normal form,also applies to maps. This is obvious for the Poincaré map of the system,and Moser (1956) proves that one can always interpolate a time-periodic Hamiltonian system, given an area-preserving map. The normal form of the map will simply be the Poincaré map of the normal form for the interpolated time-periodic system. Since the normalized Hamiltonian is independent of time and depends only on the product pq: $H ( { \mathfrak { p } } , { \mathfrak { q } } , t ) = f ( \xi ) .$ where $\xi = { \mathfrak { p } } { \mathfrak { q } }$ ,Hamilton's equations have the form

$$
{ \dot { \mathfrak { p } } } = - ( d f / d \xi ) \mathfrak { p } , \qquad { \dot { \mathfrak { q } } } = ( d f / d \xi ) \mathfrak { q } .
$$

Verifying that $\xi$ and hence $d f / d \xi$ are constants of the motion, we can immediately integrate (4.42) and so obtain the Poincaré map for a period of $2 \pi , { \pmb x } ^ { \prime } = { \bf T } _ { N } ( { \pmb x } ) ,$ as

$$
{ \bf p } ^ { \prime } = U ( { \bf p q } ) { \bf p } , \qquad { \bf q } ^ { \prime } = U ^ { - 1 } ( { \bf p q } ) { \bf q } ,
$$

where

$$
U ( \xi ) = \exp ( - i 2 \pi d f / d \xi ) .
$$

For a time-periodic system we get a different normal-form transformation for each Poincaré map by fixing $t$ in (4.26) and (4.27). Of course, it is not necessary to go through the business of interpolating systems once the existence of the normal form for maps has been proved. All that must be done is to evaluate the coefficients of

$$
U ( \mathfrak { p q } ) = \lambda { \left[ 1 + \sum _ { \alpha = 1 } ^ { \infty } U _ { 2 \alpha } ( \mathfrak { p q } ) ^ { \alpha } \right] }
$$

and the normal-form transformation $\mathbf { x } = \mathbf { N } ( \pmb { \mathfrak { x } } )$

$$
\begin{array} { l } { { \displaystyle p = { \mathfrak { p } } + \sum _ { \alpha + \beta = 2 } ^ { \infty } p _ { \alpha \beta } { \mathfrak { p } } ^ { \alpha } { \mathfrak { q } } ^ { \beta } } , } \\ { { \displaystyle q = { \mathfrak { q } } + \sum _ { \alpha + \beta = 2 } ^ { \infty } q _ { \alpha \beta } { \mathfrak { p } } ^ { \alpha } { \mathfrak { q } } ^ { \beta } } , } \end{array}
$$

by direct substitution into the map $\mathbf { x } ^ { \prime } = \mathbf { T } ( \mathbf { x } )$

$$
\begin{array} { l } { { p ^ { \prime } = \lambda p + \displaystyle \sum _ { \alpha + \beta = 2 } ^ { \infty } p _ { \alpha \beta } ^ { \prime } p ^ { \alpha } q ^ { \beta } , } } \\ { { \displaystyle q ^ { \prime } = \lambda ^ { - 1 } q + \displaystyle \sum _ { \alpha + \beta = 2 } ^ { \infty } q _ { \alpha \beta } ^ { \prime } p ^ { \alpha } q ^ { \beta } . } } \end{array}
$$

Moser (1956) proves the convergence of the normal-form transformation in a small disc surrounding the origin. This is not of immediate use, because the disc is an unstable region, only briefly visited by most points. It is therefore important to show that the region of convergence can be extended,as in da Silva Ritter, Ozorio de Almeida and Douady (1987), for an analytic map whose inverse $\mathbf { T } ^ { - 1 }$ is also analytic. This is possible because the normal map (4.43) is defined in terms of the function $U ( { \mathfrak { p } } { \mathfrak { q } } ) .$ ， which is itself invariant under the mapping. If the series for the normal map converges for $( \mathfrak { p } _ { 0 } , \mathfrak { q } _ { 0 } )$ in $D _ { 0 }$ ，it converges for all $( { \mathfrak { p } } , { \mathfrak { q } } )$ such that ${ \mathfrak { p q } } \leq { \mathfrak { p } } _ { 0 } { \mathfrak { q } } _ { 0 }$ . The relation between the invariant curves and the region of convergence $D _ { 0 }$ and $\mathbf { N } ( D _ { 0 } )$ for the original and the normalized system is shown in fig. 4.2.

Let us now define the transformations

$$
{ \bf N } _ { m } = { \bf T } ^ { - m } { \cdot } { \bf N } { \cdot } { \bf T } _ { N } ^ { m } , \qquad { \bf N } _ { 0 } = { \bf N }
$$

for all positive or negative m. Since $\mathbf { N }$ is analytic in $D _ { 0 } , \mathbf { N } _ { - m }$ is analytic in the region

$$
\begin{array} { r } { D _ { m } = \mathbf { T } _ { N } ^ { m } ( D _ { 0 } ) . } \end{array}
$$

All the regions $D _ { n }$ have points in common, namely, some neighbourhood

![](images/832d93e1bd180772e130fd6540fec9a3003e14d908c1e3fb07a127aa4de1ec0e.jpg)  
Fig. 4.2. The circle of convergence $D _ { 0 }$ and the invariant hyperbolas that touch it are distorted by the normal-form transformation $\mathbf { N }$

of the origin (fig. 4.3). Moreover, ${ \bf N } _ { 0 }$ and $\mathbf { N } _ { m }$ coincide in the region where they both converge:

$$
\mathbf { N } _ { m } = \mathbf { T } ^ { - m } { \boldsymbol { \cdot } } \mathbf { N } { \boldsymbol { \cdot } } \mathbf { T } _ { N } ^ { m } = \mathbf { N } { \boldsymbol { \cdot } } \mathbf { T } _ { N } ^ { m } { \boldsymbol { \cdot } } \mathbf { N } ^ { - 1 } { \boldsymbol { \cdot } } \mathbf { N } { \boldsymbol { \cdot } } \mathbf { T } ^ { m } = \mathbf { N } .
$$

The same is true for any pair of regions $D _ { m }$ and $D _ { m ^ { \prime } }$ , so we can define the extended normal-form transformation to be

$$
\mathbb { N } = \operatorname* { l i m } _ { \kappa  \infty } \bigcup _ { m = - K } ^ { K } \mathbf { N } _ { m } ,
$$

which will be analytic in the region

$$
\mathbb { D } = \operatorname* { l i m } _ { \kappa  \infty } \bigcup _ { m = - K } ^ { K } D _ { m } .
$$

Because of (4.5O), the Taylor series for each $\mathbf { N } _ { m }$ will be identical with the series for $\mathbf { N } _ { 0 }$ , but we must show that the region of convergence for the Taylor series of $\mathbf { N } _ { m }$ indeed extends far out of $D _ { 0 }$ . This is done in da Silva Ritter, Ozorio de Almeida and Douady (1987) by complexifying, that is,by using the fact that the convergence of the series for $\mathbf { N } _ { 0 } ( \pmb { x } _ { 0 } )$ implies the convergence of the Taylor series for $\mathbf { N } _ { 0 } ( \mathfrak { z } )$ for $| \mathfrak { z } _ { 1 } | \leq | \mathfrak { x } _ { 1 0 } |$ and $| 3 _ { 2 } | \leq | \mathfrak { X } _ { 2 0 } |$ .Therefore,inside this region there are no poles, nor are there any in the complex regions $D _ { \mathfrak { n } \mathfrak { c } }$ obtained from it by the transformations (4.48). This fact in turn ensures the convergence of the Taylor series in $D _ { \mathrm { n c } }$

The separatrices of the map $\mathbf { T }$ are the images of the $\mathbf { \boldsymbol { x } } _ { 1 } = 0$ and $\mathfrak { X } _ { 2 } = 0$ axes under the transformation $\mathbb { N } ( { \pmb x } )$ The extension of the Birkhoff-Moser theorem guarantees that the normal form converges, indefinitely far out along the separatrices. As a consequence we can calculate homoclinic (and heteroclinic) points from the images of both axes under N. (Heteroclinic points are calculated from the normal forms for two unstable points.) Though it is not difficult to compute some homoclinic points directly by following orbits along the stable and unstable manifolds, it is only the above method that provides the entire homoclinic orbit with uniform precision.All that has to be done is to follow the linear orbit of the normal coordinates for the homoclinic point, before transforming back to $\mathbf { x }$ .This last step is not even necessary close to the origin, since there $\mathbb { N }$ is asymptotic to the identity.

![](images/4e1d99db21081f2d0436bb9bb4c973a628992d55fbc9c64ce6725a8baea58b14.jpg)  
Fig. 4.3. All the images $D _ { n }$ of $D _ { 0 }$ have a common intersection, which includes the origin.

The normal-form transformation also converges along invariant square hyperbolas very close to the $\mathfrak { x } _ { 1 } = 0$ and $\mathfrak { X } _ { 2 } = 0$ axes. The images of these curves self-intersect near the homoclinic points. These self-intersections are not generally periodic points,but a simple argument due to Birkhoff (1927) shows that they give rise to an infinite sequence of periodic points. Consider the orbit of a point of self-intersection; generally there will be $n - 1$ images along the invariant curve,say the inner one in fig. 4.4a, while the nth image lies beyond the self-intersection. However, the average spacing between the points on the orbit diminishes continuously as the invariant curves come closer to the separatrices, that is, for self-intersections that approach the homoclinic point. There will thus be an invariant curve where the nth image of the self-intersection comes back to itself exactly - the nth-order periodic orbit.By the same token we find an $( n + 1 )$ -order periodic orbit and so on.

![](images/c356bd31bf844491c9ca4a6a3fc840166999eb1a680ff4daa337f1f42b3f4de7.jpg)  
Fig.4.4. (a) The three self-intersecting curves within the stable and the unstable manifolds are the images of invariant hyperbolas.There are five images of the point of intersection on the inner curve and six on the outer curve. The boundary curve supports a periodic orbit of period 6. (b) Here the pair of curves supports a single periodic orbit of period 15.(c) A periodic orbit of period 24 is supported on three open invariant curves.

There are many other families of periodic points that accumulate on the homoclinic point in the limit of infinite periods.For instance, there are the families based on the mutual intersections of a pair of invariant curves shown in fig.4.4b.These are obtained by requiring that two families of curves satisfy two conditions: The orbit of each one of the intersections must land exactly on the other intersection. This is also the situation for the simplest heteroclinic points.Figure 4.4c sketches a periodic orbit based on three invariant curves. In general we can find periodic orbits bound to any number $k$ of invariant curves.In the limit where $k \to \infty$ , we obtain recurrent chaotic orbits.

The larger the period of the orbit, the closer will be the hyperbolas on which they travel to the $\pmb { \mathscr { X } }$ axes.In this limit the map $\mathbf { T } _ { N }$ becomes linear. Since the periodic points accumulate on the homoclinic point, their position is accurately given by a linearization of the normal-form transformation around the homoclinic point. Combining both linearizations,we arrive at explicit linear equations for the periodic points,which are asymptotically exact in the limit of high periods.To achieve this, let us consider both images $( \mathfrak { x } _ { 1 } ^ { * } , 0 )$ and $( 0 , \pmb { x } _ { 2 } ^ { * } )$ of the homoclinic point $\mathbf { x } ^ { * }$ under the transformation $\mathbb { N } ^ { - 1 }$ (fig. 4.5). We define $\mathbb { N } _ { 1 }$ and $\mathbb { N } _ { 2 }$ to be the restrictions of $\mathbb { N }$ to neighbourhoods of these two points. A periodic point of order m, with normal coordinates ${ \pmb x } _ { m }$ ， propagates from near $( 0 , \mathfrak { x } _ { 2 } ^ { * } )$ by $\mathbf { T } _ { N } ^ { m }$ into the neighbourhood of $( \mathfrak { x } _ { 1 } ^ { * } , 0 )$ .It satisfies the equation

$$
\begin{array} { r } { \pmb { \mathfrak { x } } _ { m } = \mathbb { N } _ { 2 } ^ { - 1 } \cdot \mathbb { N } _ { 1 } \cdot \pmb { \mathrm { T } } _ { N } ^ { m } ( \pmb { \mathfrak { x } } _ { m } ) . } \end{array}
$$

Linearizing $\mathbb { N } _ { j }$ around the images of the homoclinic point and the normal map $\mathbf { T } _ { N } ^ { m }$

$$
\begin{array} { r } { \left[ \pmb { \chi } _ { 1 } ^ { \prime } \right] = \mathcal { L } ^ { m } \pmb { \chi } = \left[ \begin{array} { l l } { \lambda } & { 0 } \\ { 0 } & { \lambda ^ { - 1 } } \end{array} \right] ^ { m } \pmb { x } , } \end{array}
$$

we can approximate (4.53) by the linear equation

$$
\begin{array} { r } { \mathcal { R } ^ { m } \pmb { x } \equiv D [ { \mathbb { N } } _ { 2 } ^ { - 1 } \cdot { \mathbb { N } } _ { 1 } \cdot { \mathbf { T } } _ { N } ^ { m } ] \pmb { x } = ( 0 , \pmb { x } _ { 2 } ^ { \ast } ) + ( D { \mathbb { N } } _ { 2 } ) ^ { - 1 } ( D { \mathbb { N } } _ { 1 } ) [ \mathcal { L } ^ { m } \pmb { x } - ( \pmb { x } _ { 1 } ^ { \ast } , 0 ) ] . } \end{array}
$$

A periodic orbit $\pmb { x } _ { m _ { J } } . . . . _ { m _ { 1 } }$ with $m _ { 1 }$ points on one hyperbola, $m _ { 2 }$ on another and so on up to $m _ { J }$ on the Jth hyperbola is obtained from the solution of the equation

$$
\Biggl ( \prod _ { j = 1 } ^ { J } \mathcal { R } _ { m _ { J } } - 1 \Biggr ) \pmb { \mathscr { x } } _ { m _ { J } \cdots m _ { 1 } } = 0 .
$$

![](images/ee8d04c17d39f59bbd55104c347cecb51c31c1725d35a577c5f7792608a816f1.jpg)  
Fig. 4.5. $\mathbb { N } _ { 1 } ( { \mathbf { x } } )$ and $ { \mathbb { N } } _ { 2 } ( {  { \mathbf { x } } } )$ are,respectively， the restrictions of $\mathbb { N } ( { \mathbf { x } } )$ to the neighbourhoods of the pre-images of the homoclinic point $( \mathfrak { x } _ { 1 } ^ { * } , 0 )$ and $( 0 , \pmb { x } _ { 2 } ^ { * } )$

Contrary to appearances,(4.56) is not a homogeneous equation, the inhomogeneous terms arising from the normal coordinates for the homoclinic point in (4.55). Thus,we obtain a unique solution for any set of indices $m _ { 1 } \cdots m _ { J }$ . The resulting approximation for ${ \mathfrak { X } } _ { m _ { J } \cdots m _ { 1 } }$ becomes asymptotically exact in the limit where all the $m _ { J } \to \infty$

It is interesting that the presence of denumerable periodic orbits is a consequence of the Smale-Birkhoff theorem and ultimately derives from the nonlinearity of the map T.It may seen strange to calculate these orbits from a linear map,but it must be borne in mind that the linearization is performed around the homoclinic point and not the origin.We are familiar with chaotic maps where the orbits are ‘folded back in'.This is the case of Arnold's cat map,which also has denumerable periodic orbits,and even for Smale's horseshoe, developed as a simplified model of homoclinic motion.

The computational feasibility of calculating homoclinic orbits from the Birkhoff normal form was verified by Ozorio de Almeida, Coutinho and da Silva Ritter (1985) for the family of quadratic maps

$$
\begin{array} { r } { x _ { 1 } ^ { \prime } = x _ { 1 } \cosh \alpha + ( x _ { 2 } - x _ { 1 } ^ { 2 } ) \sinh \alpha , } \\ { x _ { 2 } ^ { \prime } = x _ { 2 } \sinh \alpha + ( x _ { 2 } - x _ { 1 } ^ { 2 } ) \cosh \alpha . } \end{array}
$$

This can be proved to be equivalent to all quadratic maps with a hyperbolic fixed point at the origin, just as the similar map used by Henon (1969) is equivalent to all quadratic maps containing an elliptic fixed point. Figures 4.6a and b show,respectively,the separatrices calculated by iterating points on the separatrices close to the origin and by the normal form. Da Silva Ritter et al. (1987) achieved the calculation of unstable orbits that returned to themselves after ten iterations within an accuracy of twenty-one significant figures,by calculating the self-intersection of invariant curves! Good agreement was found with the periodic points calculated from the explicit linear equation (4.56) (with $J = 1$ ),and the accuracy of the points calculated in this way was seen to improve with $\pmb { n }$

This technique can evidently be extended to the calculation of heteroclinic points and their satellite periodic orbits and to the calculation of homoclinic (heteroclinic) points of time-periodic Hamiltonian systems with one freedom. Though the numerical convergence of the normal form is vcry fast,the very large $\pmb { \mathscr { X } }$ coordinates needed to calculate ‘higher homoclinic points' arising from the mutual intersections of long loops of the separatrices may not be accessible. It seems likely that the present formalism can be used to compute homoclinic and periodic orbits near unstable equilibria for which the normal form has no small denominators.

![](images/36dd0fa61506abccb0a9af79b658402b2eb772784a31b8911ae1d73e67d6dc5f.jpg)  
Fig.4.6. (a) Points on the stable and unstable manifolds obtained by positive and negative iterations on the linear approximation of the manifolds very near the origin,for $\alpha = 1 . 4 .$ (b) The two separatrices calculated from the Birkhoff normal form up to twentieth order.

# 4.4 Bifurcations of stable periodic orbits

In the absence of an exact resonance, the cancelling of all the off-diagonal' terms in the normalform for a stable periodic orbit leads to the formal series

$$
- 2 i H = - i \omega z z ^ { * } + H _ { 2 } ( z z ^ { * } ) ^ { 2 } + \cdots .
$$

We can cast this into real variables by merely reversing the transformation (4.35), so that

$$
H = \omega \bigg ( \frac { p ^ { 2 } + q ^ { 2 } } { 2 } \bigg ) + H _ { 2 } \bigg ( \frac { p ^ { 2 } + q ^ { 2 } } { 2 } \bigg ) ^ { 2 } + \cdots ,
$$

or we can use the canonical polar coordinates (1.48), that is,action-angle variables,

$$
p = ( 2 I ) ^ { 1 / 2 } \sin \phi , \qquad q = ( 2 I ) ^ { 1 / 2 } \cos \phi ,
$$

to obtain

$$
H = \omega I + H _ { 2 } I ^ { 2 } + \cdots .
$$

The Hamiltonian not only is integrable, because of the loss of its time dependence,but also is independent of $\theta$ .The circles centred on the origin are invariant circles, just as with the quadratic Hamiltonian $\omega I =$ $\omega ( p ^ { 2 } + q ^ { 2 } ) / 2$ . The difference is that the motion along each circle no longer has the universal angular velocity $\omega$ .Indeed,from Hamilton's equations

$$
\dot { \phi } ( I ) = \omega + 2 H _ { 2 } I + \cdots .
$$

Even though the normal form does not usually converge, we can bring any nonresonant Hamiltonian to coincide with it in its lowest terms. The normal form therefore provides an accurate approximation of the motion close to the origin,that is,the periodic orbit of an autonomous two-freedom system.In this expanded picture (fig. 4.7), the invariant circle of the normal form corresponds to a thin torus surrounding the periodic orbit. Neighbouring orbits wind around such tori. The frequency Qf rotation $\dot { \phi } ( I )$ varies continuously,so that arbitrarily close to the origin there are Birkhoff tori for which $\dot { \phi } = l / k$ is a rational number. The orbits on these tori are periodic,for the orbits of the Poincaré map $t \to t + 2 \pi$ close after $k$ iterations.

Let us focus on one of these periodic tori, while altering the energy. It was shown in section 2.5 that typical periodic orbits are members of one-parameter families, where the energy can be chosen as the parameter. Generally the linear frequency will be a monotonic function $\omega ( E )$ over a small energy range. So if the periodic orbit torus lies close to the periodic orbit at the orign,we may choose instead

$$
\iota ; = \omega ( E ) - l / k
$$

![](images/6f0ab1ee4e879cbd27d297d680816a267177f7d0b0ff107d4055ba4b575e7642.jpg)  
Fig.4.7. The invariant circle of the normal form corresponds to a thin torus surrounding the periodic orbit.

as the parameter for the family. Substituting $l / k$ on the left side of (4.62) and taking $\omega$ from (4.63), the action variable for the periodic torus is sen to be

$$
I _ { l / k } = - \varepsilon / ( 2 H _ { 2 } ) + O ( \varepsilon ^ { 2 } ) .
$$

Thus, the periodic torus collapses onto the origin as $\varepsilon \to 0$ ,which is exactly the resonance condition. This event resembles the generic Hopf bifurcations of dissipative systems described by Arnold (1982) and Guckenheimer and Holmes (1983). The orbits on the periodic torus are fixed points of the kth iteration of the Poincareé map. According to the ‘Birkhoff picture', this entire family of fixed points collapses onto the central fixed point when a resonance occurs. This is a complete alteration of the ‘linear picture', where at resonance all points become fixed points. The resonance condition for the Poincaré map is the same as (2.33).

As the resonance condition is approached, one of the denominators in the normal-form transformation becomes arbitrarily large. The Birkhoff normal form does not hold through the resonance, so we must work instead with a resonant normal form, including all the terms that blow up the transformation exactly at the resonance. This has the form

$$
- 2 i H = - i \omega z z ^ { * } + H _ { 2 } ( z z ^ { * } ) ^ { 2 } + \cdots + H _ { k 0 l } z ^ { k } e ^ { i l t } + H _ { 0 k , - l } z ^ { * k } e ^ { - i l t } + \cdots ,
$$

showing explicitly the resonant term of lowest order, since this will have the strongest effect near the origin,where the bifurcation takes place. Though the resonant terms cannot be cancelled when $\pmb \varepsilon = 0$ ，we can still eliminate the time dependence by means of the canonical time-dependent

transformation

$$
\zeta = z \exp ( i l t / k ) , \qquad \zeta ^ { * } = z ^ { * } \exp ( - i l t / k ) ,
$$

generated implicitly by

$$
\sigma ( z , \zeta ^ { * } , t ) = z \zeta ^ { * } \exp ( i l t / k ) .
$$

Applying (4.25), we obtain

$$
- 2 i H = - i \varepsilon \zeta \zeta ^ { * } + H _ { 2 } ( \zeta \zeta ^ { * } ) ^ { 2 } + \cdots + 2 i \operatorname { I m } ( H _ { k 0 l } \zeta ^ { k } ) + \cdots ,
$$

using the fact that $H _ { 0 k , - m } = - H _ { k 0 m } ^ { * }$ for $H$ to be real. In the real polar coordinates

$$
\zeta = ( 2 I ) ^ { 1 / 2 } \exp ( i \phi ) ,
$$

the Hamiltonian takes the form

$$
H ( I , \phi ) = \varepsilon I + H _ { 2 } I ^ { 2 } + \cdots + a I ^ { k / 2 } \sin ( k \phi ) .
$$

So the coordinate transformation (4.66) takes the system to rotating coordinates in which the periodic torus (4.64) becomes a circle of fixed points. For $k > 4$ the last term,as well as the higher $\phi$ independent terms, are smaller than the first two as $I \to 0$ .We can then consider the effect of the $\phi$ dependent term as a perturbation. Because of it, in general $( d H / d \phi ) _ { I _ { l / k } } \not = 0$ ，so that the only fixed points on the periodic torus have $\phi = ( \pi / 2 + n \pi ) / k$ ，As a first approximation around the unperturbed torus $I _ { l / k }$ ，we have

$$
H ( I , \phi ) = H _ { 2 } ( I - I _ { \mathit { l } / k } ) ^ { 2 } + a I _ { \mathit { l } / k } ^ { k / 2 } \sin k \phi ,
$$

which can be recognized as the Hamiltonian for the pendulum; its level curves are shown in fig. 4.8. So one-half of the periodic points are stable and one-half unstable.The stable points are surrounded by closed invariant curves known as islands or island tori in the extended two-freedom system. These correspond to librations of the pendulum. The pendulum rotations are distortions of the unperturbed Birkhoff invariant curves [horizontal lines, in the $( I , \phi )$ coordinates]. Between rotations and librations lie the separatrices.Since the system is time independent, we obtain their equation from the level curve with the energy of the unstable fixed point:

$$
I - I _ { \iota / k } = [ a I _ { \iota / k } ^ { k / 2 } ( 1 - \sin k \phi ) / H _ { 2 } ] ^ { 1 / 2 } .
$$

Therefore, the maximum area of the islands is of order $\varepsilon ^ { k / 4 }$ .For $k > 4$ the islands shrink faster than the periodic tori as $\pmb { \varepsilon }  0$ 、Thus,the‘Birkhoff picture', though qualitatively incorrect right down to $\varepsilon \to 0$ ，becomes quantitatively accurate: It is impossible to distinguish a very thin resonance from a torus in a computation.

![](images/ed27622bf42773cb60df6a4f7d8baad63682189ac88d0a2eb2cbb24a9384d7a1.jpg)  
Fig.4.8. The Hamiltonian for the resonant normal form is approximately the same as for a pendulum with angular momentum $I - I _ { l / k }$

The foregoing analysis focused on a single periodic Birkhoff torus followed through the exact resonance by means of a survey of the family of periodic orbits placed at the origin. For a single energy $E$ there is an infinite number of periodic Birkhoff tori, the frequency of which approximates the irrational frequency $\omega ( E )$ arbitrarily well. The above theory can be applied to every one of them.In each case the periodic Birkhoff torus breaks up into $2 k$ periodic points,corresponding to a single pair of stable and unstable periodic orbits in the extended system. These resonances are dense near the origin, so the Birkhoff normal form cannot converge onto the wrong picture of the motion.

We note that even the resonant normal form does not converge. To start with,it displays only a single resonance, so it is wrong in the region of rotations of the pendulum Hamiltonian(4.62).To the truncated resonant normal form, we must add the time-dependent remainder. We therefore expect that the separatrices will split into the transverse homoclinic intersections studied in chapter 3.Yet the closer the periodic Birkhoff torus is to the origin, the smaler will this remainder be,so this region of chaotic motion becomes very narrow as the resonant region collapses on the origin.

There remains the al-important question of whether any tori subsist between this dense set of resonances,and indeed whether the islands themselves are not actually swept away by the homoclinic windings of the separatrices.Note that this whole analysis now can be applied to the stable periodic satellite orbit. We then obtain dense resonances among the islands,containing in turn stable periodic orbits and so on. It turns out that typical stable motion is actually harder to analyse than the chaotic unstable motion, our principal subject until now. The preeminent result in this area is the theorem of Kolmogorov,Arnold and Moser, to be discussed in chapter 6,after the preliminary consideration of maps of the circle in chapter 5.

# Exercises

1. Verify that the transformation(4.66) also eliminates the time dependence of all the higher-order resonant terms. Therefore the resonant normal form is integrable up to any order.   
2.Deduce the normal form for the neighbourhood of a stable equilibrium of an autonomous system with two freedoms.   
3. Show that, in the case of an exact resonance in exercise 2,a coordinate transformation will eliminate the dependence of the Hamiltonian on one of the angles. The corresponding action is an independent constant of the motion.

The resonances of order $k \leq 4$ have different structures.The case where $k = 3$ is analysed by Arnold (1978,app.7). Only a single unstable satellite orbit appears, corresponding to three fixed points. However, satellite fixed points exist on both sides of the resonance (fig. 4.9). The fourth-order resonance can happen generically in two forms. One follows the higherorder resonances,whereas the other is analogous to the third-order resonance.

The resonances of order 1 and 2 are the hardest to analyse.The problem is that it becomes impossible to separate clearly the quadratic part of the Hamiltonian as in (4.34) before starting the analysis.These cases were sorted out by Meyer (197O) in his complete analysis of generic bifurcations of area-preserving maps. Just as with the unstable points studied in section 4.3,there is a unique relation between the normal form for a periodic Hamiltonian and its Poincaré section. The normal forms for all the generic bifurcations of fixed points of area-preserving maps are shown in fig. 4.9.

According to the figure we have second-order resonances for both stable and unstable fixed points. These are known as period-doubling bifurcations, since the satellite periodic orbits have twice the period of the central orbit.

Fig. 4.9.Normal forms for all the generic bifurcations of periodic orbits. The first column specifies the ratio of the periodicity of the bifurcating orbit to the original orbit. For $n > 5$ all orbits follow the same pattern with pairs of stable and unstable satellite orbits.   

<table><tr><td rowspan=1 colspan=1>Repetitionnumberm</td><td rowspan=1 colspan=1>Linearizedmap M atresonance</td><td rowspan=1 colspan=1>Linearizedmap Mmatresonance</td><td rowspan=1 colspan=1>Fixed pts oftrue Mmoffresonance,E&gt;0</td><td rowspan=1 colspan=1>Fixed pts oftrue Mm offresonance,E&lt;0</td><td rowspan=1 colspan=1>Normalform</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>小</td><td rowspan=1 colspan=1>小</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>Eq²+q³+p²</td></tr><tr><td rowspan=2 colspan=1>2</td><td rowspan=2 colspan=1>小</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1>Eq2+q4 +p²</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>日</td><td rowspan=1 colspan=1>Identity</td><td rowspan=1 colspan=1>文</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Eq²+q3-qp²</td></tr><tr><td rowspan=1 colspan=1>4a</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Identity</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>EI +CI²+al² sin(4)|C| &gt; |a|case</td></tr><tr><td rowspan=1 colspan=1>4b</td><td rowspan=1 colspan=1>日</td><td rowspan=1 colspan=1>Identity</td><td rowspan=1 colspan=1>88</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>EI+CI²+al² sin(4Φ)|C|&lt;|a|case</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Identity</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>EI+Cr²a15/2 sin(5Φ)</td></tr><tr><td rowspan=1 colspan=1>&gt;5</td><td rowspan=1 colspan=5>Natural extension of case 5</td></tr></table>

In the same way,we can refer to the nth-order resonance as a period $\pmb { n }$ -ling bifurcation.It is common for the period doubling of a stable periodic orbit to be followed by a cascade of successive period doublings of the stable periodic orbits,resulting from each bifurcation. This event has been analysed by Bountis (1981), Greene et al. (1981) and Collet, Eckmann and Koch (1981) for area-preserving maps, though its scaling properties were first studied in dissipative maps by Feigenbaum (1978,1979). In a finite parameter range (energy in Poincaré sections), there occurs an infinite number of bifurcations, resulting in an infinite number of unstable periodic orbits of arbitrarily high period. The previously stable region thus turns into a domain of hyperbolic chaotic motion, as studied in chapter 3. For dissipative maps this is often refered to as the‘universal route to chaos'. We have seen that it is not the only route for conservative maps, where chaotic motion may appear through the homoclinic bifurcation.

The situation for the quadratic map (4.57) is illustrative.For low values of the parameter $\pmb { \alpha }$ ,there is an elliptic fixed point,as well as the hyperbolic fixed point at the origin (fig. 4.1O). This starts to undergo period-doubling bifurcations for $\begin{array} { r } { \alpha > \alpha _ { 0 } \simeq 1 . 6 7 . } \end{array}$ However,for this parameter the homoclinic windings of the separatrices have already swept away practically all the invariant curves surrounding the stable point. Thus, in this case perioddoubling bifurcations appear only as a final step in the path to completely chaotic motion.

Meyer classified all the generic bifurcations of periodic orbits in area-preserving maps, that is,for all periodic orbits with‘nothing special' about them.Does the classification apply to the reversible maps introduced in section 2.5,or to maps with other symmetries? We found there that an inversion R,for which $\mathbf { R } \mathbf { R } = \mathbf { 1 }$ ,is invariant with respect to a coordinate transformation. So if a map has, say, a reflection symmetry, its normal form will also have an inversion symmetry. Furthermore, this symmetry is asymptotic to a reflection for points close to the origin,because the normal-form transformation reduces there to the identity. Therefore,only symmetric terms of the normal form will have nonzero coefficients. Symmetries may therefore cancel the generic resonant term of the normal form.We must then look for the lowest resonant terms that are not cancelled,obtaining in this way a resonant normal form for the symmetric orbit,as in Aguiar, Malta, Baranger and Davies (1987).

# Exercises

1. Show that a single reflection symmetry does not alter the normal form for resonances of order $n \geq 3$

![](images/ca7c7375da029c49f80cbe5e837975eac88e07c625fd9decc43ba06541b56fb2.jpg)  
Fig. 4.10.Orbits of the quadratic map (4.57) for $\pmb { \alpha } = \mathbf { 0 . 2 }$ (a) and $\alpha = 0 . 9$ (b).

2. Show that a pair of reflection symmetries cancels the coefficient of the lowest resonant term for $n = 3$ .The symmetric resonant normal-form Hamiltonian has level curves resembling the sixth-order resonance,but there are two pairs of satelite orbits of period three.

Whatever the symmetry properties of the map, the possibilities for a bifurcation are limited by a geometric constraint: The Poincaré index of a closed curve $c$ that passes no fixed points is defined by Greene et al. (1981)as the number of times that the vector $\mathbf { T } ( \mathbf { x } ) - \mathbf { x }$ encircles the origin as $\mathbf { x }$ traverses $c$ ，taken to be positive or negative,respectively,as the encirclement and traversal are in the same or in opposite directions. For example, the index of a small curve around a single ordinary hyperbolic, elliptic or inversion hyperbolic point is respectively -1,1 or 1. Provided that $c$ crosses no fixed points, the index is a continuous function of $c$ Being integer-valued,it must be constant. Thus,we speak of the index of a fixed point, meaning the index of any closed curve surrounding it and no other fixed points. The index is summable - that is, the index of a curve, formed by traversing first one and then another curve, is the sum of the separate indices, so the index of any curve is the sum of the indices of the fixed points that it contains. Continuity of the map in its parameter then implies that the sum of the indices of the fixed points in a given region is constant as the parameter is varied, so long as none of them crosses the boundary of the chosen region. This limits the ways in which bifurcations can take place.

# Exercise

Show that in a period $\pmb { n }$ -ling bifurcation, with $n > 2$ , elliptic and ordinary hyperbolic orbits must be created in pairs, whatever the symmetry constraints.

# 5

# Maps on the circle

The motion along thin tori surrounding stable periodic orbits in the Birkhoff approximation was studied in section 1.3. The Poincaré maps on such tori are translations of the circle (rotations).According to the analysis in section 4.4, the periodic Birkhoff tori and their neighbours are broken up by the nearly resonant terms of the Hamiltonian, which generate small denominators in the normal-form transformation. Even so,the survival of nonperiodic tori is not excluded,as will be confirmed by the theorem of Kolmogorov, Arnold and Moser in chapter 6. Understanding the motion near stable periodic orbits thus requires a preliminary study of general motion on tori, or their Poincaré sections - maps on the circle.

There is a didactic incentive that perhaps even outweighs the abovementioned physical motivation for the study of circle maps.In the context of these maps, many of the mathematical difficulties that beset the analysis of stable motion manifest themselves in their clearest, simplest form. We will analyse the effect of the near commensurability of frequencies, that is,rational rotation numbers. The attempt to reduce general maps to rotations leads once again to small denominators. Convergence in their presence is possible,but this result is so surprising that considerable effort will be spent in sketching proof.

# 5.1 The rotation number

Consider the general dynamical system

$$
\begin{array} { r } { \dot { \pmb { \theta } } = \pmb { \omega } ( \pmb { \theta } ) , } \end{array}
$$

defined on the two-dimensional torus $0 \leq \theta _ { j } \leq 2 \pi$ .The orbits are given by

$$
\cfrac { d \theta _ { 2 } } { d \theta _ { 1 } } = \cfrac { \omega _ { 2 } ( \pmb { \theta } ) } { \omega _ { 1 } ( \pmb { \theta } ) }
$$

if $\omega _ { 1 } ( \pmb { \theta } ) \neq 0$ The Poincaré map $T \langle \theta _ { 2 } \to \theta _ { 2 } ^ { \prime }$ associates to each point $\theta _ { 2 }$ (and $\theta _ { 1 } = 0$ )the solution of (5.2) for $\theta _ { 1 } = 2 \pi$ (fig.5.1). This diffeomorphism

![](images/b9143889819a988429704f075c1b0bcf1cc324e756e525d6f39636c0c2e5f568.jpg)  
Fig. 5.1. The Poincaré map associates to each point $\theta _ { 2 0 }$ the intersection of its orbit with the line $\theta _ { 1 } = 2 \pi$

can always be written in the form

$$
T \theta = \theta + F ( \theta ) ,
$$

dropping the index of $\theta _ { 2 }$ . The angular function $f ( \theta )$ satisfies

$$
F ( \theta + 2 \pi ) = F ( \theta ) \qquad \mathrm { a n d } \qquad d F / d \theta > - 1 .
$$

The rotation number for the map $T$ is defined as

$$
\mu = { \frac { 1 } { 2 \pi } } \operatorname* { l i m } _ { k \to \infty } { \frac { F ( \theta ) + F ( T \theta ) + \cdots + F ( T ^ { k - 1 } \theta ) } { k } } .
$$

In the case where $T$ is a rotation, $2 \pi \mu$ will therefore be just the rotation angle.It is important to show that the above limit exists and that it is independent of $\theta _ { \astrosun }$ The following proof is borrowed from Arnold (1982).

Let us consider the angle by which the point $\theta$ is rotated under the kth power of the map $T$ ：

$$
F _ { k } ( \theta ) = F ( \theta ) + F ( T \theta ) + \cdots + F ( T ^ { k - 1 } \theta ) .
$$

Since $T ( \theta + 2 \pi ) = T ( \theta ) + 2 \pi$ and hence $T ^ { k } ( \theta + 2 \pi ) = T ^ { k } ( \theta ) + 2 \pi .$ it follows that, if $| \theta _ { 1 } - \theta _ { 2 } | < 2 \pi$ then

$$
| F _ { k } ( \boldsymbol { \theta } _ { 1 } ) - F _ { k } ( \boldsymbol { \theta } _ { 2 } ) | < 2 \pi .
$$

Furthermore, because $F _ { k }$ is $2 \pi$ -periodic, we can add any multiple of $2 \pi$ to either $\theta _ { 1 }$ or $\theta _ { 2 }$ ,so that in fact (5.7) holds for any $\theta _ { 1 }$ and $\theta _ { 2 }$ .Taking now $m _ { k }$ to be the integer for which

$$
2 \pi m _ { k } \leq F _ { k } ( 0 ) \leq 2 \pi ( m _ { k } + 1 ) ,
$$

we obtain from (5.7)

$$
| F _ { k } ( \theta ) - 2 \pi m _ { k } | < 4 \pi
$$

and hence

$$
\left| \frac { F _ { k } ( \theta ) } { 2 \pi k } - \frac { m _ { k } } { k } \right| < \frac { 2 } { k } .
$$

So far we have shown only that $F _ { k } / 2 \pi k$ is contained in an interval $\sigma _ { k } = { ( { ( { m _ { k } - 2 } ) } / { k } \mathrm { . } }$ $( m _ { k } + 2 ) / k )$ ，which vanishes with $k ^ { - 1 }$ . This does not necessarily imply that $m _ { k } / k$ has a constant limit. However, we now note that

$$
\frac { F _ { k l } ( \theta ) } { 2 \pi k l } { = \frac { 1 } { l } \sum _ { i = 0 } ^ { l - 1 } \frac { F _ { k } ( T ^ { i } \theta ) } { 2 \pi k } } .
$$

Each of the terms $F _ { k } ( T ^ { i } \theta ) / 2 \pi k$ is contained in the interval $\sigma _ { k }$ ,so that

$$
\left| \frac { F _ { k l } ( \theta ) } { 2 \pi k l } - \frac { m _ { k } } { k } \right| < \frac { 2 } { k } .
$$

Now $F _ { k l } ( \theta ) / 2 \pi k l$ also belongs to the interval $\sigma _ { l }$ ,which tends to zero with $l ^ { - 1 }$ It follows that all pairs of intervals ${ \pmb { \sigma } } _ { \pmb { k } }$ and $\sigma _ { l }$ intersect one another. Since they both tend to zero, the unique common point of intersection is the rotation number itself.

An immediate corollary is that a map with a periodic orbit must have a rational rotation number. After all if $\theta _ { 0 }$ returns after $r$ iterations, its image on a periodic straight line under $T ^ { r }$ will be $\theta _ { 0 } + 2 \pi s$ where $\pmb { s }$ is an integer. Therefore, $F _ { l r } ( \theta _ { 0 } ) = 2 \pi s l$ for all $l ,$ ，so the rotation number is just $s / r$ Conversely, if $F _ { r } ( \theta ) > 2 \pi s$ for all $\theta _ { ; }$ ，we cannot have $s / r$ as the rotation number, the same being the case if $F _ { r } ( \theta )$ is always smaller than $2 \pi s$ Therefore, $\mu = s / r$ implies that $F _ { r } ( \theta ) = 2 \pi s$ for some $\theta$ ，Thus,a rational rotation number always implies the existence of at least one periodic orbit.

If the rotation number is irrational, the map has no periodic orbit. This means that, for all $\theta , F _ { r } ( \theta ) > 2 \pi s .$ if $\mu > s / r$ ,no matter how good an approximation $s / r$ may be to $\mu$ . For each $\theta$ the order of the points $( \theta , T \theta , . . . , T ^ { k } \theta )$ on the circle is the same as for the irrational rotation $2 \pi \mu$ Otherwise,the switching of the order of $\theta$ and $T ^ { r } \theta$ in an interval $( \theta _ { 1 } , \theta _ { 2 } )$ would imply the existence of a periodic orbit in this interval.

# 5.2 Reduction of circle maps to rotations

We have seen how an irrational rotation number imposes a strong restriction on a differentiable mapping.It is therefore plausible that there exists a coordinate transformation that reduces the map to a mere rotation. This is indeed the content of Denjoy's theorem (see Arnold, 1982,or Guckenheimer and Holmes,1983, for a proof): If a twice-differentiable diffeomorphism of the circle has an irrational rotation number $\mu _ { : }$ itis topologically equivalent to a rotation of the circle by the angle $2 \pi \mu$

There exists then a continuous transformation capable of reducing the map to a rotation, but this transformation is not necessarily differentiable. Denjoy's theorem is somewhat analogous to the Hartman-Grobman theorem. The latter guarantees a local topological equivalence between a map in the neighbourhood of a hyperbolic point and its linearization, whereas the former guarantees a global equivalence for circle maps. In both cases,a problem arises only if we insist that the transformations be differentiable.

Surprisingly,perhaps,there is another theorem (Arnold,1982) which asserts that only diffeomorphisms of the circle with rational rotation numbers are structurally stable.A suficient condition for this is that all the periodic orbits be nondegenerate, that is,that the derivative of the rth powers of the map be nonzero. In other words, if we consider a one-parameter family of maps,a map with nondegenerate periodic orbits is topologically equivalent to all the maps in a given neighbourhood. All of these must have the same rotation number. Conversely the neighbourhood of a map with an irrational rotation number will contain maps that do not coincide with it under any coordinate transformation. Let $\pmb { \alpha }$ be the parameter; then $\mu ( \alpha )$ is a function that is constant for some interval of $\pmb { \alpha }$ at every rational value of $\mu$ ，Since the rational numbers are dense among the real numbers, it is appropriate to wonder whether there are any points $\pmb { \alpha }$ for which $\mu ( { \boldsymbol { \alpha } } )$ is irrational. If the answer is negative, then $\mu ( \alpha )$ will have a graph that is a staircase with finite irregular steps. Otherwise, the values of $\pmb { \alpha }$ for which $\mu ( \alpha )$ are irrational form a Cantor set. The graph of $\mu ( \alpha )$ will then bea devil's staircase with infinitely small steps, as described by Mandelbrot (1982)

In this confusing situation it is best to analyse a concrete example (Arnold, 1965):

$$
T _ { \alpha } ( \theta ) = \theta + \alpha + \varepsilon \sin \theta
$$

in the limit where $\varepsilon \to 0$ .We proceed by determining the region in the $( \alpha , \varepsilon )$ plane,for which there exists a periodic orbit of period $\mu = s / r$ For $\varepsilon = 0$ ，

there is just the single point $\alpha = 2 \pi s / r$ . Thus, we seek the small parameters εand $\alpha ^ { \prime } = \alpha - 2 \pi s / r$ ,for which the equation

$$
\theta = T ^ { r } ( \theta ) = \theta + 2 \pi s + r \alpha ^ { \prime } + \varepsilon \sum _ { j = 0 } ^ { r - 1 } \sin ( T ^ { j } \theta )
$$

has a solution.

For $\mu = 1$ ,(5.14) reduces to

$$
0 = \alpha ^ { \prime } + \varepsilon \sin \theta ,
$$

wherefore the straight segments

$$
| { \boldsymbol { \alpha } } ^ { \prime } | = \varepsilon
$$

bound the region with $\mu = 1$ (or 0). For $\begin{array} { r } { \mu = \frac { 1 } { 2 } } \end{array}$ ,(5.14) becomes

$$
0 = 2 \alpha ^ { \prime } + \varepsilon \sin \theta + \varepsilon \sin ( \theta + \pi + \alpha ^ { \prime } + \varepsilon \sin \theta ) .
$$

Expanding the last term around $\theta + \pi$ ,we obtain

$$
( 2 - \varepsilon \cos \theta ) \alpha ^ { \prime } = ( \varepsilon ^ { 2 } / 2 ) \sin 2 \theta .
$$

Thus, as $\varepsilon \to 0$ ，we have the condition

$$
| \alpha ^ { \prime } | \leq \varepsilon ^ { 2 } / 4 .
$$

# Exercise

Show that the equation for an orbit of period 3 reduces to

$$
3 \alpha ^ { \prime } - \sin ( 2 \pi / 3 ) \varepsilon ^ { 2 } = - \varepsilon ^ { 3 } \cos ( \theta + 4 \pi / 3 ) \cos ( \theta + 2 \pi / 3 ) \sin \theta
$$

and hence the condition for a periodic orbit is just

$$
| \alpha ^ { \prime } - \varepsilon ^ { 2 } / 2 \sqrt { 3 } | \leq \varepsilon ^ { 3 } / 4 .
$$

The regions of the $( \alpha , \varepsilon )$ plane where the rotation number is $1 , \ { \scriptstyle { \frac { 1 } { 2 } } } , \ { \scriptstyle { \frac { 1 } { 3 } } }$ and $\textstyle { \frac { 2 } { 3 } }$ are indicated in fig. 5.2.For $r > 1$ they touch the $\pmb { \alpha }$ axis in a cusp, which becomes narrower as $r$ increases.For larger $r$ we still find that the interval of $\pmb { \alpha }$ for which the map has rotation number $s / r$ is $O ( \varepsilon ^ { r } )$ Since $1 \leq s < r$ ，there are $r - 1$ such intervals; the total length of the regions where $\mu$ is rational is of order $\varepsilon + \varepsilon ^ { 2 } + 2 \varepsilon ^ { 3 } + \cdots$ ,a convergent series the sum of which vanishes as $\varepsilon \to 0$ .Thus,in this case the parameters $\pmb { \alpha }$ ,for which the map has an irrational rotation number,form a Cantor set with finite Lebesgue measure. The function $\mu ( \alpha )$ is a devil's staircase. Even so, any interval of $\pmb { \alpha }$ will be crossed by the‘tongues' in fig. 5.2,where $\mu$ is rational,so no map with an irrational rotation number is structurally stable.

![](images/a58393a57b46aed0547bbdc453e3bde84d03ec930e444daa4163292c40fe567e.jpg)  
Fig.5.2. The ‘tongues',which reach down to the rational numbers on the $_ x$ axis, are the parameter ranges with the given rational rotation numbers. The ‘tongues' become thinner as the rational denominators increase.

We have seen that the parameter $\alpha / 2 \pi$ need not coincide with the rotation number, even though the function $f ( \theta ) = \varepsilon \sin \theta$ satisfies

$$
\int _ { 0 } ^ { 2 \pi } f ( \theta ) d \theta = 0 .
$$

However, for maps with irrational rotation numbers, $\alpha / 2 \pi$ is indeed the rotation number. In these cases Denjoy's theorem guarantees that the map can be transformed into a rotation for which time averages and configurational averages coincide, so $\bar { f } ( \theta ) = 0$ .The definition (5.5) of the rotation number is just the average of $\vert \alpha + f ( \theta ) \vert / 2 \pi .$ ,so the rotation number is exactly $\alpha / 2 \pi$ Conversely, if $\alpha / 2 \pi$ is an irrational rotation number, then $f ( \theta )$ has zero average in a map with the form of (5.13). The picture is then that, for each irrational number times $2 \pi$ along the line $\varepsilon = 0$ in fig. 5.2, there is a vertical segment along which the map has the same irrational rotation number. The height of this segment will be limited by some spreading‘rational tongue'.

The possibility that $T _ { \alpha }$ has an irrational rotation number depends on $\pmb { \alpha }$ being‘sufficiently irrational’ in some sense. Denjoy's theorem then guarantees that a homeomorphism will turn $T _ { \alpha }$ into a mere rotation. In section 5.4 we will find that for sufficiently small ε there may even be analytic reductions of $T _ { \alpha }$ into a rotation.However, we must first examine more closely this concept of being ‘sufficiently irrational'.

# 5.3 Approximating irrational numbers by rational numbers

Irrational numbers can be approximated by rational numbers to arbitrarily high accuracy. For example $\pi$ is approximated by the sequence

$$
\begin{array} { c } { { s } } \\ { { r = \displaystyle { \frac { 3 } { 1 } , \frac { 3 1 } { 1 0 ^ { \circ } } , \frac { 3 1 4 } { 1 0 0 ^ { \circ } } , \frac { 3 1 4 2 } { 1 0 0 0 ^ { \circ } } , \frac { 3 1 4 1 6 } { 1 0 0 0 0 ^ { \circ } } , \cdots , } } } \end{array}
$$

which provides better approximations as $r$ increases. Thus, for decimal approximations we obtain

$$
\left| \mu - { \frac { s } { r } } \right| < { \frac { 1 } { r } } ,
$$

with $r _ { n } = 1 0 ^ { n } $ , and a similar inequality holds for any other basis.

For a finite sequence of $\pmb { n }$ terms,some bases will lead to better approximations than others, but extending the sequence to higher terms we find that this advantage will be reversed in favour of another basis. Thus,it is worthwhile to look for a basis-independent sequence,such as the sequence of continued fractions:

$$
\mu _ { n } = a _ { 0 } + \frac { 1 } { a _ { 1 } } +
$$

$$
+ { \frac { 1 } { a _ { n } } } .
$$

These approximants

$$
\mu _ { n } = s _ { n } / r _ { n }
$$

obey the following recursion relation,

$$
\begin{array} { r } { s _ { n } = a _ { n } s _ { n - 1 } + s _ { n - 2 } , } \\ { r _ { n } = a _ { n } r _ { n - 1 } + r _ { n - 2 } , } \end{array}
$$

for $n \geq 2$

This result is demonstrated in Khinchin (1963),a source of many other important results on continued fractions. We proceed by induction, supposing that (5.27) holds up to order $n - 1$ Defining

$$
{ \frac { s _ { n - 1 } ^ { \prime } } { r _ { n - 1 } ^ { \prime } } } = a _ { 1 } + { \frac { 1 } { a _ { 2 } } } \qquad 
$$

$$
+ \frac { 1 } { a _ { n } } ,
$$

we have

$$
\begin{array} { l } { { S _ { n } = a _ { 0 } s _ { n - 1 } ^ { \prime } + r _ { n - 1 } ^ { \prime } , } } \\ { { \nonumber } } \\ { { r _ { n } = s _ { n - 1 } ^ { \prime } } } \end{array}
$$

and by hypothesis

$$
\begin{array} { r l } & { S _ { n - 1 } ^ { ' } = a _ { n } S _ { n - 2 } ^ { ' } + S _ { n - 3 } ^ { ' } , } \\ & { } \\ & { r _ { n - 1 } ^ { \prime } = a _ { n } r _ { n - 2 } ^ { \prime } + r _ { n - 3 } ^ { \prime } . } \end{array}
$$

Introducing (5.30) into (5.29) and rearranging the terms, we immediately retrieve (5.27),which evidently holds for $n = 2$

The sequence of integers $a _ { n }$ determines the sequence of approximants $( r _ { n } , s _ { n } )$ .Consider the graphical construction, presented in Arnold (1982) and shown in fig. 5.3,by which the pairs $( r _ { n } , s _ { n } )$ are pictured as the integer coordinates of points on the plane. The real numbers are associated with the slope of straight lines passing through the origin. Thus,an irrational number corresponds to a straight line that avoids all the points on the integer lattice in fig. 5.3.A good sequence of approximants to the irrational number $\mu$ is the sequence of vectors $\mathbf { v } _ { n } = ( r _ { n } , s _ { n } )$ , which starts with ${ \bf v } _ { 0 } = ( 1 , 0 )$ and $\mathbf { v } _ { 1 } = ( 0 , 1 )$ .Vectors ${ \pmb { \nu } } _ { \pmb { n } }$ are obtained by adding to $\mathbf { v } _ { n - 2 }$ the vector $\mathbf { v } _ { n - 1 }$ multiplied by the largest integer ${ a } _ { n }$ for which $\begin{array} { r } { { \bf { v } } _ { n } = { a } _ { n } { \bf { v } } _ { n - 1 } - { \bf { v } } _ { n } } \end{array}$ still remains on the same side of the straight line as $\yen 2$ . The resulting approximant $( r _ { n } , s _ { n } )$ satisfies the recursion relation (5.27); hence, the sequence $a _ { 0 } , a _ { 1 } , \ldots$ determines its unique continued-fraction representation.In the limit where $n \to \infty$ we obtain the irrational number as an infinite continued fraction.

![](images/773487337150e92ce06a313337d9d60d66b6ac1036c98319cd3074ca01b83e08.jpg)  
Fig. 5.3.The sequence of vectors ${ \pmb v } _ { \pmb n }$ supplies ideal approximations to the irrational slope of the straight line.

How do the continued-fraction approximations compare with those depending on a basis? The diference between two approximants $\mu _ { n }$ and $\mu _ { n + 1 }$ is

$$
\left| { \frac { s _ { n } } { r _ { n } } } - { \frac { s _ { n + 1 } } { r _ { n + 1 } } } \right| = \left| { \frac { s _ { n } r _ { n + 1 } - s _ { n + 1 } r _ { n } } { r _ { n } r _ { n + 1 } } } \right| = { \frac { 1 } { r _ { n } r _ { n + 1 } } } ,
$$

since the numerator of the second term is the area of the parallelogram formed by the vectors ${ \pmb v } _ { n }$ and $\forall _ { n + 1 }$ . This area is 1 for the pair $\left( \mathbf { v } _ { 0 } , \mathbf { v } _ { 1 } \right)$ ,and successive parallelograms have a common side and the same height. The approximants are alternately greater and smaller than $\mu$ and $r _ { n + 1 } \geq r _ { n }$ ， so they all satisfy the inequality

$$
\left| \mu - { \frac { s } { r } } \right| < { \frac { 1 } { r ^ { 2 } } } .
$$

Thus, the continued-fraction sequence converges much more rapidly onto an irrational number than any basis-dependent sequence. The larger the numbers $a _ { n }$ ,the better the convergence; after all, some $a _ { n } = \infty$ if $\mu$ is a rational number. In contrast, the hardest number to approximate by rationals is the golden mean,

$$
\mu = { \cfrac { 1 } { 1 + { \cfrac { 1 } { 1 + } } } } = { \cfrac { { \sqrt { 5 } } - 1 } { 2 } } .
$$

Can we find a sequence of approximants satisfying even more favourable Diophantine conditions than (5.32)? The answer is that (5.32) is the best that can be guaranteed uniformly for all the real numbers.This follows from the result that,for most numbers $\pmb { \mu }$ in the interval [O,1] and for all $\pmb { \sigma } > 0$ there exists a number $K ( \mu , \sigma )$ ，such that

$$
\left| \mu - { \frac { s } { r } } \right| \geq { \frac { K } { r ^ { 2 + \sigma } } }
$$

for all pairs of integers $( r , s )$ . Any infinite sequence of approximants for $\mu$ must have $r _ { n } \to \infty$ ， so that beyond a certain element $K / r _ { n } ^ { 2 + \sigma } > 1 / r _ { n } ^ { 2 + \sigma ^ { \prime } }$ ， whatever the number $\pmb { K }$ 、Therefore,since $0 < \sigma ^ { \prime } \leq \sigma$ and $\pmb { \sigma }$ can be made as small as we like, the numbers satisfying the Diophantine conditions (5.34) cannot be approximated to better accuracy than (5.32).

To demonstrate (5.34) we first fix $\pmb { s }$ and $r$ .Consider now the set of numbers $\mu$ for which these inequalities are violated. They form an interval of length $2 K / r ^ { 2 + \sigma }$ .The union of all these intervals with the same $r$ has a total length equal to or smaller than $2 K / r ^ { 1 + \sigma }$ since $s \leq r .$ Summing over all the r's we obtain a set, the Lebesgue measure of which is $C K$ ，where

$$
C = 2 \sum _ { r = 1 } ^ { \infty } r ^ { - ( 1 + \sigma ) } < \infty .
$$

By choosing $\pmb { K }$ arbitrarily small, we make the measure of the set of points that violates (5.34) as small as we like.Thus,the set of numbers that infringes these Diophantine conditions for any $\pmb { K }$ has zero measure.

The numbers that satisfy the conditions (5.34) for a given pair of $\sigma > 0$ and $K > 0$ are known as numbers of type $( K , \sigma )$ .1 This is the basis for the vague concept of ‘sufficiently irrational' used in the previous sections; that is, the numbers of type $( K , \sigma )$ with larger maximal $\pmb { K }$ or smaller minimal $\pmb { \sigma }$ may be thought of as the‘more irrational'.

# 5.4 Kolmogorov's method

According to Denjoy's theorem, a map with an irrational rotation number is always conjugate to a rotation by a homeomorphism. Just as with the Hartman-Grobman theorem, the proof is nonconstructive, so we now seek the required transformation in a manner analogous to the method of normal forms, that is,by iterated simplifications.

Consider a map of the form

$$
\theta  T \theta = \theta + 2 \pi \mu + f ( \theta ) .
$$

As we saw in section 5.2, the only requirement on $f ( \theta )$ for the irational parameter $\mu$ to be the rotation number is that this function have zero

1 Obviously a number of type $( K , \sigma )$ is also a number of type $( K ^ { \prime } , \sigma )$ or $( K , \pmb { \sigma } ^ { \prime } )$ if $K ^ { \prime } \le K$ and $\pmb { \sigma } ^ { \prime } \geq \pmb { \sigma }$

average. We will also suppose that $f ( \theta )$ is an analytic periodic function in the strip $| \operatorname { I m } \theta | < \rho$ of the complex plane, where

$$
\operatorname { s u p } | f ( \theta ) | \equiv \| f \| _ { \rho } < \varepsilon .
$$

# Exercise

Determine the bound on the function $f ( \theta )$ in (5.13)for the strip $| \operatorname { I m } \theta | < \rho$

We now seek a diffeomorphism

$$
\phi  G \phi = \phi + g ( \phi ) = \theta ,
$$

which brings the map $T$ to the rotation $U$ (by the angle $2 \pi \mu _ { \cdot }$ .Thus, $G$ satisfies

$$
T \cdot G \phi = G \cdot U \phi ,
$$

leading to the functional equation

$$
g ( \phi + 2 \pi \mu ) - g ( \phi ) = f ( \phi + g ( \phi ) ) .
$$

The problem is to establish for what rotation numbers (5.40) has a solution.

If $f$ is of order ε, it is plausible that $g$ is too. So expanding $f _ { : }$ we obtain as a first approximation to $\pmb { G }$ the transformation

$$
\phi  G _ { 0 } \phi = \phi + g ^ { 0 } ( \phi ) = \theta ,
$$

where the function $g ^ { 0 } ( \phi )$ satisfies the equation

$$
g ^ { 0 } ( \phi + 2 \pi \mu ) - g ^ { 0 } ( \phi ) = f ( \phi ) .
$$

If we expand $f ( \phi )$ and $g ^ { 0 } ( \phi )$ in Fourier series,

$$
f ( \phi ) = \sum _ { l } f _ { l } \exp ( i l \phi )
$$

and

$$
g ^ { 0 } ( \phi ) = \sum _ { l } g _ { l } ^ { 0 } \exp ( i l \phi ) ,
$$

equation (5.42) reduces to

$$
\sum _ { l } g _ { l } ^ { 0 } [ \exp ( i 2 \pi l \mu ) - 1 ] \exp ( i l \phi ) = \sum _ { l } f _ { l } \exp ( i l \phi ) ,
$$

with the formal solution

$$
g _ { l } ^ { 0 } = \frac { f _ { l } } { \exp ( \mathrm { i } 2 \pi l \mu ) - 1 } .
$$

There is no exact resonance among the coefficients, because the rotation number was assumed irrational.However, there will be arbitrarily small denominators on the right side,just as with the normal forms of chapter 4. We have now developed the tools with which to tackle such a tricky convergence problem. If $\mu$ is of type $( K , \sigma ) _ { : }$ ，that is,it satisfies the Diophantine conditions (5.34), the distance of $l \mu$ to the nearest integer is greater than $K / | l | ^ { 1 + \sigma }$ .The numbers 1 and $\mathsf { e x p } ( i 2 \pi l \mu )$ are separated by the arc $2 \pi l \mu$ along the unit circle.We seek a lower bound for the length of the chord that joins them. Since the minimum ratio between chord and arc is $2 / \pi$ ,the former satisfies the inequality

$$
| \exp ( i 2 \pi l \mu ) - 1 | \geq \frac { 2 } { \pi } ( 2 \pi l \mu ) \geq \frac { 4 K } { | l | ^ { 1 + \sigma } } .
$$

The convergence of the Fourier series for $g ^ { 0 } ( \phi )$ depends on the exponential decay of the coefficients $f _ { l }$ being capable of dominating the power law decay of the denominators allowed by (5.46). This can be shown directly from the definition

$$
f _ { l } = ( 2 \pi ) ^ { - 1 } \int _ { 0 } ^ { 2 \pi } f ( \phi ) \exp ( - i l \phi ) d \phi .
$$

We can move the path of integration to $\operatorname { I m } \phi = - \rho$ for $l > 0$ ，since $f$ is analytic in a strip of this width and the vertical integrals along $\mathbf { R e } \phi = 0$ and $2 \pi$ cancel each other. Thus,

$$
f _ { \scriptscriptstyle { l } } = ( 2 \pi ) ^ { - 1 } \int _ { 0 } ^ { 2 \pi } f ( \phi - i \rho ) \exp ( - i l \phi - l \rho ) d \phi \leq \varepsilon \exp ( - | l | \rho ) ,
$$

using (5.37). Conversely, for a given sequence of coefficients $f _ { l }$ satisfying (5.48), we can guarantee that the corresponding Fourier series converges to an analytic function $f ( \phi )$ in a strip of width $2 \rho$ .We can even determine a bound on $g ^ { 0 } ( \phi )$ in the narrower strip of width $2 ( \rho - \delta )$

$$
\begin{array} { r l } & { \| g ^ { 0 } \| _ { \rho - \delta } \le \displaystyle \sum _ { l } ( \varepsilon / 4 K ) | l | ^ { 1 + \sigma } \exp ( - | l | \rho ) | \exp ( i l \phi ) | } \\ & { \qquad \le ( \varepsilon / 4 K ) \displaystyle \sum _ { l } | l | ^ { 2 } \exp ( - | l | \rho ) \exp [ | l | ( \rho - \delta ) ] } \\ & { \qquad = \displaystyle \frac { \varepsilon } { 4 K } \displaystyle \frac { d ^ { 2 } } { d \delta ^ { 2 } } \sum _ { l } \exp ( - | l | \delta ) } \\ & { \qquad \le \displaystyle \frac { 2 \varepsilon } { 4 K } \displaystyle \frac { d ^ { 2 } } { d \delta ^ { 2 } } \displaystyle \frac { 1 } { 1 - \exp ( - \delta ) } \le \varepsilon D \delta ^ { - 3 } , } \end{array}
$$

assuming that $\sigma < 1$ and $\delta < 1$ . Using more delicate majorations Arnold

(1982) obtains the norm

$$
\| g ^ { 0 } \| _ { \rho - \delta } \leq \varepsilon C \delta ^ { - 2 - \sigma } ,
$$

in which the number $c$ [like $D$ in (5.49)] depends only on $K$ and $\pmb { \sigma }$

The transformation $G _ { 0 }$ reduces $T$ to a rotation up to order $\varepsilon ^ { 2 }$ In analogy to the theory of normal forms, we can attempt to eliminate the difference between $T$ and a rotation up to order $\varepsilon ^ { 3 }$ and so on. The problem is the difficulty of demonstrating the convergence of this procedure.

A fruitful alternative method was proposed by Kolmogorov (1954): Instead of eliminating terms of higher and higher order,we apply the same procedure as described above to $T _ { 1 }$ , the result of the transformation $G _ { 0 }$ on $T .$ This produces a new transformation $G _ { 1 }$ and so on. The convergence is improved, in exact analogy to Newton's method, for determining the roots of a function.This consists of linearizing the function $f ( x )$ about the point $\scriptstyle { \mathfrak { x } } _ { 0 }$ ，yielding a first approximation $x _ { 1 }$ to the root of $f ( x )$ (fig.5.4). Instead of seeking to improve this approximation by taking the quadratic expansion of $f ( x )$ about $x _ { 0 }$ ，we now take a new linear approximation about $x _ { 1 }$ ，and this process is iterated indefinitely. It is readily verified that the nth approximation $f ( x _ { n } ) = O ( \varepsilon ^ { 2 n } ) .$ instead of $O ( \varepsilon ^ { n } )$ obtained for approximations by a power series.

We therefore construct the transformation

$$
T _ { 1 } = G _ { 0 } ^ { - 1 } \cdot T \cdot G _ { 0 } ;
$$

![](images/995ad7bb75790a0a4b3b15121a5d78b3e630909315012d382734aa172b987e4b.jpg)  
Fig.5.4. Newton's method for finding the root of a function relies on iterating linear approximations and so converges much better than making polynomial approximations at a fixed initial point.

that is, $T _ { 1 }$ is the transformation $T$ viewed with the coordinates $\phi$ defined by (5.41). If we substituted $G$ for $G _ { 0 }$ in (5.51), $T _ { 1 }$ would be the rotation $U$ .The problem is now to quantify the statement that $T _ { 1 }$ ，

$$
\phi \to T _ { 1 } \phi \equiv \phi + 2 \pi \mu + f _ { 1 } ( \phi ) ,
$$

is closer to a rotation than $T .$ The residue $f _ { 1 } ( \phi )$ between $T _ { 1 }$ and $U$ must have zero average just as $f ( \phi )$ We estimate $f _ { 1 } ( \phi )$ from the relation $G _ { 0 } \cdot T _ { 1 } \phi \equiv T \cdot G _ { 0 } \phi$ ：

$$
\phi + 2 \pi \mu + f _ { 1 } ( \phi ) + g ^ { 0 } ( \phi + 2 \pi \mu + g _ { 1 } ( \phi ) ) \equiv \phi + g ^ { 0 } ( \phi ) + 2 \pi \mu + f ( \phi + g ^ { 0 } ( \phi ) ) .
$$

Hence,

$$
f _ { 1 } ( \phi ) = [ f ( \phi + g ^ { 0 } ( \phi ) ) - f ( \phi ) ] - [ g ^ { 0 } ( \phi + 2 \pi \mu + f _ { 1 } ( \phi ) ) - g ^ { 0 } ( \phi + 2 \pi \mu ) ] ,
$$

using (5.42) to rearrange the terms. The mean value theorem provides a norm for the first bracket:

$$
\parallel f ( \phi + g ^ { 0 } ( \phi ) ) - f ( \phi ) \parallel _ { \rho - \delta } \leq \parallel d f / d \phi \parallel _ { \rho - \delta } \parallel g ^ { 0 } \parallel _ { \rho - \delta } .
$$

The norm for $d f / d \phi$ is easily shown to be $O ( \varepsilon \delta ^ { - 2 } )$ by proceeding as in (5.49). Together with (5.50), we thus obtain

$$
\| f ( \phi + g ^ { 0 } ( \phi ) ) - f ( \phi ) \| _ { \rho - \delta } \leq C ^ { \prime } \varepsilon ^ { 2 } \delta ^ { - 5 } .
$$

Careful consideration of the second square bracket in(5.54) yields a similar result; that is, we have

$$
\| f _ { 1 } \| _ { \rho - \delta } \leq C ^ { \prime \prime } \varepsilon ^ { 2 } \delta ^ { - 5 } .
$$

The norm $\parallel f _ { 1 } \parallel$ estimates the ‘error' in the approximation of $T _ { 1 }$ by $U$ ， a rotation. The order of the ‘error’ doubles at each successive approximation, just as in Newton's method. Still, it is not yet clear that we can iterate indefinitely these approximations, since a finite choice for $\delta$ will ‘eat away’ the convergence strip $\rho$ after a finite number of iterations, whereas any attempt to reduce $\delta$ leads to a small denominator in (5.57). The only way out is to take a diminishing sequence of $\delta _ { n } \mathbf { \bar { s } } ,$ such as

$$
\delta _ { 0 } = \delta < { \scriptstyle { \frac { 1 } { 2 } } } , \qquad \delta _ { n } = \delta _ { n - 1 } ^ { 3 / 2 } , \qquad \rho _ { n } = \rho _ { n - 1 } - \delta _ { n - 1 } .
$$

Then

$$
\sum _ { n } \delta _ { n } < \delta _ { 0 } \sum _ { n } ( \delta _ { 0 } ^ { 1 / 2 } ) ^ { n } < \frac { \rho } { 2 }
$$

if $\delta _ { 0 }$ is sufficiently small.

The final step is to connect the norms $\parallel f _ { n } \parallel$ to the sequence of $\delta _ { n } ^ { \phantom { \dagger } }$ s. For a sufficiently large integer $m$ ，we can replace (5.57) by

$$
\begin{array} { r } { \| f _ { 1 } \| _ { \rho - \delta } \leq \varepsilon ^ { 2 } \delta _ { 0 } ^ { - m } . } \end{array}
$$

But $\delta _ { n } \leq \delta _ { 0 }$ , so the residue of successive approximations satisfies

$$
\| f _ { n } \| _ { \rho _ { n } } \leq \| f _ { n - 1 } \| ^ { 2 } \delta _ { n - 1 } ^ { - m } .
$$

The number $m$ , common to all the inequalities (5.61), depends only on $\pmb { K }$ and $\pmb { \sigma } .$ . We now specify

$$
\begin{array} { r } { \varepsilon = \delta _ { 0 } ^ { N } , } \end{array}
$$

where $N$ is chosen large enough for

$$
2 N - m \ge 3 N / 2 .
$$

Thus, using (5.60) and (5.58),

$$
\begin{array} { r } { \| f _ { 1 } \| _ { \rho _ { 1 } } \leq \delta _ { 0 } ^ { 3 N / 2 } = \delta _ { 1 } ^ { N } , } \end{array}
$$

whereas repeated use of (5.61) yields

$$
\| f _ { n } \| _ { \rho _ { n } } \leq \delta _ { n } ^ { N } .
$$

We have shown that Kolmogorov's method converges for $\pmb { \sigma } < 1$ and for small enough $\varepsilon ( K )$ .Of course, we could have done the same for $\sigma < 2$ 、 obtaining a smaller estimate for ε. The more delicate majorations in the proof of Arnold (1982)，on which this exposition is based,provide convergence for a much wider range of $\varepsilon ( K , \sigma )$ .The range of convergence is actually much wider still， since Herman (1979) proved that even diffeomorphisms not close to rotations can be conjugate to them by a diffeomorphism.

So far it has not been possible to apply Herman's methods to the problems of Hamiltonian dynamics to be studied in the following chapter. The proof of Siegel’s theorem also tackles the small-denominator problem, without having to rely on Kolmogorov's method. The latter retains its paramount importance as the basis of the theorem of Kolmogorov, Arnold and Moser. For this reason it has been worthwhile to give a full account of it for the simplest relevant application.

# 6

# Integrable and quasi-integrable systems

In the previous chapter we attained global understanding of a very simple kind of system. We now return to full Hamiltonian systems, but these will be restricted in such a way as to allow a global knowledge of their main characteristics.This class of integrable systems contains all the solved problems in classical mechanics,as well as the truncations of the Birkhoff normal forms studied in chapter 4. We will find that no limitation need be made on the number of freedoms of an integrable system.In fact, their definition can be extended up to an infinite number of freedoms,leading to the solution of important partial differential equations,but this subject lies beyond the scope of this book.

We start by defining integrable systems and by studying the geometry of their invariant surfaces.This leads to the definition of general action-angle variables. The consideration of a few simple examples elicits the concept of caustics,that is,singularities of the projections of invariant surfaces.We will discuss briefly Thom and Arnold's classification of some of the simpler generic caustics.

In conclusion we will study perturbations of integrable systems. In section 6.5 we will discuss the averaging principle, which is then related to a stationary perturbation theory,reminiscent of the resonant normal forms encountered in section 4.4. This evokes the question of survival of the invariant surfaces of an integrable system after a perturbation, to be answered by the Kolmogorov, Arnold and Moser (KAM theorem). The sketch of its proof relies on that of the analytical reduction of circle maps to rotations presented in section 5.4.

# 6.1 Invariant tori

A necessary condition for a system with $L$ freedoms to be integrable is that it have $L$ independent constants of the motion. The Hamiltonian of an autonomous system $H ( \mathbf { x } )$ is a constant function; therefore, there must be

$L - 1$ other functions with the property that

$$
\frac { d } { d t } F ( \mathbf { x } ( t ) ) = \sum _ { l = 1 } ^ { L } \left( \frac { \partial F } { \partial q _ { l } } \frac { \partial H } { \partial p _ { l } } - \frac { \partial F } { \partial p _ { l } } \frac { \partial H } { \partial q _ { l } } \right) = \left\{ F , H \right\} = 0 ,
$$

where the penultimate term defines the Poisson bracket of the functions $F$ and $H .$ .The antisymmetry of the Poisson bracket implies that $H$ will also be a constant of the motion for the Hamiltonian $F .$ . A fundamental property (demonstrated in Arnold,1978, sec.39) is that the flows ${ \bf x } _ { H } ( t )$ and ${ \bf x } _ { F } ( t ^ { \prime } )$ generated by two Hamiltonians that satisfy (6.1) commute: Whichever the order in which we‘switch on' the Hamiltonian $F$ for the time $t ^ { \prime }$ and $H$ for the time $t ,$ ,the system arrives at the same point $\mathbf { x }$ ,if it started out from the same point $\mathbf { x } _ { 0 }$ 1

The $L$ constants of the motion must be independent; that is,at each point $\mathbf { x }$ the vector fields $\dot { \bf x } _ { i } = \mathcal { \bar { J } } \partial F _ { i } / \partial { \bf x }$ and $\dot { \bf x } _ { j } = \mathcal { J } \partial F _ { j } / \partial { \bf x }$ [with $\mathcal { J }$ given by (1.37)] must be linearly independent. The last condition defining an integrable system is that each pair of functions $F _ { i }$ and $F _ { j }$ be in involution:

$$
\bigl \{ F _ { i } , F _ { j } \bigr \} = 0 .
$$

This condition encompasses (6.1) if we identify $H ( \mathbf { x } ) = F _ { L } ( \mathbf { x } )$

Each orbit of an integrable system is contained in an $L$ dimensional surface $T ,$ ，resulting from the multiple intersection of the $L$ surfaces $F _ { j } ( \mathbf { x } ) = \mathsf { c o n s t }$ ,each with $( 2 L - 1 )$ dimensions. The condition of involution guarantees that we would obtain the same invariant surface by choosing any one of the functions $F _ { j } ( \mathbf { x } )$ as the Hamiltonian,or even by choosing any arbitrary function of the $F _ { j } ^ { ~ , } \mathrm { { s } }$ The $L$ Hamiltonians define $L$ vector fields tangent to $T _ { \ast }$ ,because each vector is tangent to an orbit contained in this surface.

Let us consider again equation (6.1). Comparison with (1.38) establishes that the Poisson bracket of two functions $F$ and $H$ is merely the skew product $\dot { \mathbf { X } } _ { F } \wedge \dot { \mathbf { X } } _ { H }$ ，that is, the symplectic area or (reduced) action of the parallelogram formed by these two vectors. The $L$ vectors $\dot { \bf x } _ { l }$ ,corresponding to the $L$ functions $F _ { t }$ ,can be taken as a basis for the tangent plane to the invariant surface $T .$ Hence, the condition of involution implies that the symplectic area is null for any pair of vectors tangent to $T .$ This differential result can evidently be extended to any reducible circuit on $T _ { \ast }$ a property that defines a null or Lagrangian surface.

Consider now the orbits defined by the $L$ independent vector fields $\dot { \mathbf { x } } _ { l } ,$ starting from an arbitrary point $\mathbf { x } _ { 0 }$ on the surface $T .$ The positions along each orbit result from the action of the one-parameter groups of canonical transformations

$$
G _ { l } ^ { t _ { l } } \mathbf { x } _ { 0 } = \mathbf { x } ( t _ { l } , \mathbf { x } _ { 0 } )
$$

with the properties

$$
G _ { l } ^ { t _ { l } } G _ { l } ^ { s _ { l } } = G _ { l } ^ { t _ { l } + s _ { l } } \qquad \mathrm { a n d } \qquad ( G ^ { t _ { l } } ) ^ { - 1 } = G ^ { - t _ { l } } .
$$

Since these $L$ groups commute,

$$
G _ { k } ^ { t _ { k } } G _ { l } ^ { t _ { l } } = G _ { l } ^ { t _ { l } } G _ { k } ^ { t _ { k } } ,
$$

we can define the action of the commutative group

$$
\mathbf { G } ^ { t } = G _ { 1 } ^ { t _ { 1 } } \cdots G _ { L } ^ { t _ { L } } ,
$$

with $\mathbf { t } = ( t _ { 1 } , \dots , t _ { L } )$

It is easy to define an invariant measure on $T$ for the motion generated by any of the Hamiltonians $F$ .Each of these preserves the Liouville measure $\delta ( F _ { l } ( \mathbf { x } ) - E _ { l } ) d \mathbf { x } ;$ therefore,

$$
d \mu = \prod _ { l = 1 } ^ { L } \delta ( F _ { l } ( \mathbf { x } ) - E _ { l } ) d \mathbf { x } ,
$$

will be invariant on $T .$ We can thus apply the Poincaré recurrence theorem (section 3.4) to the case of bounded motion, that is, when $T$ is a compact surface. The implication is that, in any neighbourhood of a point $\mathbf { x } _ { 0 }$ ,some point ${ \bf x } _ { 0 } ^ { ' }$ will return to this neighbourhood after some time $t _ { l }$ For a group of flows that commute, this result can be strengthened: We can bring $\mathbf { x } _ { 0 }$ to $\mathbf { x } _ { 0 } ^ { \prime }$ by means of the action of the element $\mathbf { G } ^ { \delta \mathbf { t } }$ of the group $\mathbf { G } ^ { \mathbf { t } }$ Thus,

$$
G _ { l } ^ { t _ { l } } \mathbf { x } _ { 0 } = \mathbf { G } ^ { - \delta t } G _ { l } ^ { t _ { l } } \mathbf { G } ^ { \delta t } \mathbf { x } _ { 0 }
$$

is a point that has returned close to $\mathbf { x } _ { 0 }$ after the time $t _ { l } ,$ under the flow generated by $F _ { l }$

We can take the $t _ { l } \mathbf { \vec { s } }$ as coordinates on $T$ by fixing an initial point $\mathbf { x } _ { 0 }$ because $\mathbf { G } ^ { \mathbf { t } }$ is a commutative group. This arrangement is sketched in fig. 6.1 for $L = 2$ within a three-dimensional subspace.Consider the orbit $\gamma _ { 1 }$ of $\mathbf { x } _ { 0 }$ under the action of $F _ { 1 }$ . It returns to $\mathbf { x } _ { 0 } ^ { \prime }$ in a neighbourhood of $\mathbf { x } _ { 0 }$ after a time $t _ { 1 } ^ { \prime }$ . In fact, $\gamma _ { 1 }$ must intersect the $t _ { 1 } = 0$ coordinate plane in a time $t _ { 1 } ^ { * }$ . To see this, note that $\gamma _ { 1 }$ returns close to $\mathbf { x } _ { 0 }$ , where its velocity $\dot { \bf x } _ { 1 }$ is transverse to this plane. The configuration is sketched in fig. 6.2a for $L = 2 .$ If we now switch off $\boldsymbol { F } _ { 1 }$ and switch on any one of the other Hamiltonians $\pmb { F }$ , the system will move on a t surface which is a new image of $t _ { 1 } = 0$ .But this motion, without any participation of $\boldsymbol { F } _ { 1 }$ ,determines a plane in the t coordinates, which reduces to a vertical straight line for $L = 2$ (fig. 6.2b). The plane $t _ { 1 } = t _ { 1 } ^ { * }$ contains a new image of the t origin, $\mathbf { x _ { 0 } }$ .The vector joining the origin to this point generates an irreducible circuit on $T ,$ since reducible curves are represented by closed loops in the t coordinates.

![](images/71e8510266508203e38e4c1ecc38d41f21334d3921031121f72f1a10120d7f49.jpg)  
Fig. 6.1. The velocity vectors $D G ^ { \dagger } \mathbf { X _ { 0 } }$ are tangent to the torus and the lines $G _ { l } ^ { t _ { l } } \mathbf { X _ { 0 } }$ can be used as coordinates on the torus.

By repeating the same procedure for $\gamma _ { 2 }$ , the curve $G _ { 2 } ^ { t _ { 2 } } \mathbf { x } _ { 0 }$ , we obtain the image of the coordinate plane $t _ { 2 } = 0$ as a parallel plane with the constant coordinate $t _ { 2 } ^ { * }$ and so on for all the other coordinates. The set of all these planes with $t _ { j } = \pm t _ { j } ^ { * }$ forms an $L$ cube centred on the origin. On each of the $L$ pairs of faces there will be a different image of the origin (Fig. 6.2b), such that the vector joining it to the origin corresponds to an irreducible circuit on $T .$ The vectors with tips on $t = \pm t _ { j } ^ { * }$ correspond to the same circuit

Fig. 6.2. (a) The coordinate line $\gamma _ { 1 }$ eventually returns close to $\mathbf { x _ { 0 } }$ ,with its velocity $\dot { \bf x } _ { 1 }$ nearly parallel to $\dot { \bf x } _ { 1 } ( { \bf x } _ { 0 } )$ (b)In the $t$ coordinates the $t _ { 2 }$ axis has multiple images separated bya period $t _ { 1 } ^ { * }$ .Traversals from the origin to its images represent irreducible circuits on the torus $T .$

![](images/9e4d52e48ba3e8b87cc529d9e665c0ac265e0f481811790c68143468ee204272.jpg)

traversed in opposite senses,and all the linear combinations of these vectors supply multiple windings of the irreducible circuits.

If the neighbourhood surrounding the origin is chosen to be small, then each image of the origin will be close to the centre of the cube face,as shown in fig. 6.2b. However, $\gamma _ { j }$ may intersect the $t _ { j } = 0$ plane many times just outside this neighbourhood for $t _ { j } < t _ { j } ^ { * }$ . By increasing the size of the neighbourhood we incorporate these intersections,so that the time $t _ { j } ^ { * }$ for the first crossing in the neighbourhood is reduced.The structure is still the same, with the $2 L$ images of the origin lying in the faces of a cube (farther from their centre). If the neighbourhood is suficiently large (for instance, if it covers uniquely the entire surface $T$ )， we obtain minimum times $t _ { j } ^ { * }$ corresponding to the first traversal of the planes $t _ { j } = 0$

The advantage is that we now obtain the discrete group of all the irreducible circuits on $T .$ If we label the images of the origin on the faces of the cube by $\mathbf { e } _ { l }$ ,then the members of the group are specified by

$$
\mathbf { t } = n _ { 1 } \mathbf { e } _ { 1 } + \cdots + n _ { L } \mathbf { e } _ { L } ,
$$

where $n _ { l }$ is an integer. There can be no other points in this group, because there are none inside the cube by construction and we can bring any point outside to the inside by adding to it one of the vectors t in (6.9). Finally we note that this group is independent of the point $\mathbf { x } _ { 0 }$ ，since for any point $\mathbf { x } = \mathbf { G } ^ { \mathbf { r } } \mathbf { x } _ { 0 }$ ，

$$
\mathbf { G } ^ { \mathrm { t } } \mathbf { x } = \mathbf { G } ^ { \mathrm { t + } \mathbf { r } } \mathbf { x } _ { 0 } = \mathbf { G } ^ { \mathrm { r } } \mathbf { x } _ { 0 } = \mathbf { x } ,
$$

for the t's satisfying (6.9). We have thus shown that there are exactly $L$ independent circuits passing through any point of the invariant surface. It follows that $T$ is an $L$ torus,that is,a common torus in the case where $L = 2$

We can now make a linear transformation from the t coordinates to the $\pmb { \phi }$ coordinates, the axes of which are the vectors $\mathbf { e } _ { l }$ ，so that $\phi _ { l }$ varies in the interval $( 0 , 2 \pi )$ from the origin to the tip of the vector.In these coordinates $T$ is the Cartesian product of $L$ circles and the movement generated by the Hamiltonian $H ( \mathbf { x } )$ is rectilinear and uniform:

$$
\pmb { \phi } ( t ) = \pmb { \phi } ( 0 ) + \pmb { \omega } t .
$$

We conclude that the motion of an integrable system can be reduced to a translation on a torus,the properties of which were studied in section 1.3. This result constitutes the main content of the Liouville-Arnold theorem. We will conclude its discussion by showing that a canonical transformation can always be found such that the motion on the torus is given by (6.11).

The obvious choice would be to take the $\pmb { L }$ variables $\mathbf { F }$ and $\pmb { L }$ angles $\pmb { \phi }$ as coordinates for an integrable system. The problem is that the transformation $( \pmb { \mathrm { p } } , \pmb { \mathrm { q } } )  ( \pmb { \mathrm { F } } , \pmb { \phi } )$ would not be canonical in general, entailing the loss of the Hamiltonian form of the system. So we must find new constants of the motion $\mathbf { I } ( \mathbf { F } )$ that are canonically conjugate to the angles $\pmb { \phi }$

The condition for the transformation $( \pmb { \mathrm { p } } , \pmb { \mathrm { q } } )  ( \pmb { \mathrm { I } } , \pmb { \phi } )$ to be canonical is that it preserve the symplectic area for any closed loop in phase space:

$$
\oint \mathbf { p } \cdot d \mathbf { q } = \oint \mathbf { I } \cdot d { \boldsymbol { \phi } } .
$$

Since the angles $\pmb { \phi }$ have no dimension, it follows that the new variables I must have the dimension of an action. Each $L$ -dimensional torus is characterized by $L$ irreducible circuits.We can therefore associate the $L$ variables Ito the symplectic area of these circuits,as long as allthe possible deformations of a given irreducible loop have the same action. This condition is indeed satisfied by the invariant tori of an integrable system, because all the deformations of an irreducible circuit are obtained by adding to it a reducible 'loop of zero action. We thus define the action variables

$$
I _ { j } = ( 2 \pi ) ^ { - 1 } \oint _ { \gamma _ { j } } \mathbf { p } \cdot d \mathbf { q } ,
$$

where $\gamma _ { j }$ is the jth irreducible circuit on the torus.Provided that the Jacobian determinant $\partial \mathbf { I } / \partial \mathbf { F }$ is nonzero, we can substitute $H ( \mathbf { F } ) = H ( \mathbf { I } )$

It remains to show that the variables conjugate to I are the required angles $\phi$ .To this end we note that the Lagrangian property of the torus implies the existence of the function

$$
S ( \mathbf { q } , \mathbf { I } ) = \int _ { \mathbf { q _ { 0 } } } ^ { \mathbf { q _ { } } } \mathbf { p _ { I } } ( \mathbf { q } ) \cdot d \mathbf { q } .
$$

In a two-dimensional phase space the torus specified by a given Iis a closed curve,so that $p _ { I } ( q )$ is an even number of points.Generally the $L$ -dimensional torus also intersects transversely the $L$ -dimensional plane $\mathbf { q } = \mathbf { c o n s t }$ in discrete points within the $2 L$ -dimensional phase space. The function $s$ is therefore multivalued. If we choose $S ( \mathbf { q } , \mathbf { I } )$ as the generating function for a canonical transformation $( \pmb { \mathrm { p } } , \pmb { \mathrm { q } } )  ( \pmb { \mathrm { I } } , \pmb { \phi } ^ { \prime } )$ ,the transformation is implicitly given by

$$
\partial S / \partial { \bf q } = { \bf p } , \qquad \partial S / \partial { \bf I } = \phi ^ { \prime } .
$$

For an irreducible circuit of the torus, $\gamma _ { i }$ , the change of the angles $\phi _ { j } ^ { \prime }$ is

simply

$$
( \Delta \phi _ { j } ^ { \prime } ) _ { \gamma _ { i } } = \Delta _ { \gamma _ { i } } \frac { \partial S } { \partial I _ { j } } = \frac { \partial } { \partial I _ { j } } \Delta _ { \gamma _ { i } } S = \frac { \partial } { \partial I _ { j } } 2 \pi I _ { j } = 2 \pi \delta _ { i j } .
$$

So the conjugate angles $\pmb { \phi } _ { j } ^ { \prime } = \pmb { \phi } _ { j }$ ,the privileged angular coordinates on the torus.

The solution of an integrable system can thus be found in principle by determining the canonical transformation $( \pmb { \mathrm { p } } , \pmb { \mathrm { q } } )  ( \mathbf { I } , \pmb { \phi } )$ ，which is guaranteed to exist.There is no general method for achieving this end,but once the transformation has been found, we obtain Hamilton's equations in the form

$$
{ \dot { \bf I } } = - \frac { \partial H } { \partial { \dot { \phi } } } ( { \bf I } ) = 0 , \qquad { \dot { \phi } } = \frac { \partial H } { \partial { \bf I } } = { \pmb { \omega } } .
$$

So the motion is given by (6.11), with the frequencies $\pmb { \omega }$ specified by (6.17). Generally the motion will be multiply periodic,admitting the Fourier expansion

$$
\begin{array} { r } { \mathbf { q } ( t ) = \displaystyle \sum _ { \mathbf { m } } \mathbf { q } _ { \mathbf { m } } ( \mathbf { I } ) \exp [ i \mathbf { m } \cdot ( \pmb { \omega } t + \pmb { \phi } _ { 0 } ) ] , } \\ { \mathbf { p } ( t ) = \displaystyle \sum _ { \mathbf { m } } \mathbf { p } _ { \mathbf { m } } ( \mathbf { I } ) \exp [ i \mathbf { m } \cdot ( \pmb { \omega } t + \pmb { \phi } _ { 0 } ) ] . } \end{array}
$$

# 6.2 Examples of integrable systems

The simplest case is that of a system with a single freedom and a Hamiltonian of the form

$$
H = p ^ { 2 } / 2 m + V ( q )
$$

for energies $E < V ( \infty )$ and $E < V ( - \infty )$ .The tori are then $p$ -symmetric level curves of the Hamiltonian. The corresponding action variable is just

$$
I = ( 2 \pi ) ^ { - 1 } \oint p d q = \pi ^ { - 1 } \int _ { q _ { 1 } } ^ { q _ { 2 } } d q \{ 2 m [ E - V ( q ) ] \} ^ { 1 / 2 } ,
$$

where the $q _ { j }$ are the turning points,for which $p = 0$

Example. The square well; a ball rolling freely with speed $v$ between two walls separated by a distance d. It is assumed that the ball has elastic collisions with the walls. This ‘square well' is more familiar in quantum mechanics. The action is obtained from fig. 6.3 as

$$
I = ( 2 \pi ) ^ { - 1 } ( \mathrm { a r e a ~ o f ~ r e c t a n g l e } ) = m v d / \pi .
$$

![](images/208464718225a490ce7ce56ffb3784c34a670bc50f229df31b7e6ce97336237f.jpg)  
Fig. 6.3. The action variable for the square well is obtained from the area of the rectangle in phase space.

Since the corresponding energy is $E = m v ^ { 2 } / 2$ ，the Hamiltonian is just

$$
H ( I ) = ( \pi I ) ^ { 2 } / ( 2 m d ^ { 2 } ) .
$$

In this case the angle variable depends linearly on $q$ ,which already has a (piecewise) uniform motion.

# Exercise

Show that the dependence of the Hamiltonian $p ^ { 2 } / 2 m + C \tan ^ { 2 } ( \pi / q )$ on the action variable tends to that of (6.22) in the limit of high energies.

Example.The harmonic oscillator. The Hamiltonian has the form

$$
H ( p , q ) = p ^ { 2 } / 2 + \omega ^ { 2 } q ^ { 2 } / 2 = E .
$$

The level curve is an ellipse with semiaxes $( 2 E ) ^ { 1 / 2 }$ and $( 2 E ) ^ { 1 / 2 } / \omega$ , so that

$$
I = ( 2 \pi ) ^ { - 1 } ( \mathrm { a r e a ~ o f ~ a n ~ e l l i p s e } ) = E / \omega ,
$$

![](images/322a06a06f9e4af9d5f0a828f5f7b129e6520b88c5c0df173c67b6e058d940eb.jpg)  
Fig. 6.4. The ratio $\partial \phi / \partial q$ is proportional to the $\delta p$ separating level curves whose actions differ by $\delta I$

that is,

$$
H ( I ) = \omega I .
$$

The angular frequency $\phi = \omega$ is therefore the same for all ellipses.

Of course, this is just the case of linear motion around a stable equilibrium already analysed in chapter 1.Through the canonical rescaling $( p , q ) {  } ( p ^ { \prime } , q ^ { \prime } ) = ( \omega ^ { - 1 / 2 } p , \omega ^ { 1 / 2 } q ) ,$ ,the Hamiltonian reduces to the standard form $\omega ( p ^ { \prime 2 } + q ^ { \prime 2 } ) / 2$ .We hence recognize the action-angle variables as the canonical polar coordinates in the $( p ^ { \prime } , q ^ { \prime } )$ plane,defined by (1.49).

The angular variable for a one-freedom system is

$$
\phi ( q ) = { \frac { \partial } { \partial I } } \int _ { q _ { 0 } } ^ { q } d q p ( q , I )
$$

within an additive constant. We can therefore visualize $\partial \phi / \partial q$ to be proportional to the $\delta p$ separating level curves that have actions differing by SI (fig. 6.4).Evidently, $\partial \phi / \partial q \to \infty$ when $q \to q _ { j }$ ,a turning point. The angular distribution along the invariant curve can also be understood directly from Liouville's theorem. The conservation of area by the flow implies that the linearly moving angle becomes stretched where invariant curves approach each other and compressed where they separate.

![](images/63bade952d24bc5de79f97e44db5142a492ee1099935fbd0260b3da3ce3f734a.jpg)  
Fig. 6.5. The efect of a canonical shear transformation on the level curves is that the turning points no longer have $\pmb { \mathrm { p } } = \pmb { 0 }$

# Exercise

Show that, if $s$ is the length along the elliptic level curve of the harmonic Oscillator (6.23), then the ratio between $d \phi / d s$ at the tips of the major and minor axes is $\omega ^ { 2 }$

Other examples and properties of one-freedom systems are discussed in Percival and Richards (1982). Note that general coordinate transformations will destroy the simple form of Hamiltonians (6.19). The turning points will then no longer coincide with the zeros of $p$ along the level curve. One such class of transformations consists of the symplectic (linear) transformations studied in section 1.2.Another one includes the shears

$$
p ^ { \prime } = p - A ( q ) , \qquad q ^ { \prime } = q .
$$

The effect of a linear shear on the levelcurves is shown in fig. 6.5.Evidently, the composition of two canonical transformations is again canonical. In the case of polynomial transformations,Engel (1958) proved that they can always be reduced to the composition of a symplectic transformation with a shear.

Example. Motion under a central force. The energy has the form

$$
H ( p _ { r } , p _ { \theta } , r , \theta ) = \frac { 1 } { 2 m } p _ { r } ^ { 2 } + \frac { 1 } { 2 m r ^ { 2 } } p _ { \theta } ^ { 2 } + V ( r )
$$

for the geometry indicated in fig. 6.6a. The angular momentum $p _ { \pmb { \theta } }$ isa constant of the motion, because the Hamiltonian is independent of $\theta .$ It is readily verified that $H$ and $p _ { \pmb { \theta } }$ are in involution, so this two-freedom system is integrable.

Two irreducible circuits for the torus, labeled by a given energy and angular momentum, are the rotation in $\theta$ with constant $r$ and the libration in $r$ with constant $\theta$ . The corresponding action variables are

$$
I _ { 2 } = ( 2 \pi ) ^ { - 1 } \int _ { 0 } ^ { 2 \pi } p _ { \theta } d \theta = p _ { \theta }
$$

and

$$
I _ { 1 } = \frac { 1 } { 2 \pi } \oint p _ { r } d r = \frac { 1 } { \pi } \int _ { r _ { 1 } } ^ { r _ { 2 } } \left\{ 2 m \Biggl [ E - \frac { 1 } { 2 m r ^ { 2 } } I _ { 2 } ^ { 2 } - V ( r ) \Biggr ] \right\} ^ { 1 / 2 } d r ,
$$

where $r _ { 1 }$ and $r _ { 2 }$ are the turning points for the libration shown in fig. $6 . 6 \mathrm { b }$ The action $I _ { 2 }$ may be positive or negative and $H ( I _ { 1 } , I _ { 2 } )$ ,obtained from the inversion of (6.29), is symmetric in this variable (fig. 6.7).

![](images/27531205e9a4284311e19aa8e0786ffbd95965932d7caf50c83cfb5608cfeae6.jpg)  
Fig.6.6. (a) The central force always points in the direction of the origin,and its magnitude depends only on the coordinate r. (b) The turning points for the librations are the same as for the one-dimensional motion with the effective potential $V ( r ) + p _ { \theta } ^ { 2 } / 2 m r ^ { 2 }$ .(c) The invariant torus projects as an annulus in configuration space; its boundaries are the caustics.

The invariant torus projects into configuration space $( r , \theta )$ or $( q _ { 1 } , q _ { 2 } )$ as an annulus (fig. 6.6c). Each point within it is the image of two points of the torus, with the two values $\pm p _ { r }$ allowed by(6.27) for fixed $H = E$ and $p _ { \theta }$ .The boundary of the torus projection is known as the caustic.It is composed of the two circles $r = r _ { 1 }$ and $r = r _ { 2 }$ ， where the two pre-images on the torus coalesce. The torus defined by the same energy, but angular momentum $- \pmb { p _ { \pmb { \theta } } }$ ,has the same caustics.

The Hamiltonian depends nonlinearly on $I _ { 1 }$ and $I _ { 2 }$ ，entailing the continuous variation of the frequencies

$$
{ \pmb \omega } = \frac { \partial { \cal H } } { \partial { \bf I } } ( { \bf I } )
$$

![](images/699d4eb4c7b5723707639c912918cf31ab9fcf12eadaafe95f14c957d4a68518.jpg)  
Fig. 6.7. The level curves of $H ( I _ { 1 } , I _ { 2 } )$ are symmetric in $I _ { 2 }$

among the invariant tori. In any neighbourhood $( \delta I _ { 1 } , \delta I _ { 2 } )$ of the action variables we find tori with rationally related frequencies,that is,tori where all the orbits are periodic.The case of the Kepler problem,in which all tori have periodic orbits,is singular- there are other constants of the motion beyond angular momentum and energy. Another instance,in which all the orbits are periodic,is that of the isotropic harmonic oscillator with $V ( r ) = \omega ^ { 2 } r ^ { 2 }$ .The extra constants of the motion in this case will be discussed in the following example.

Example. Separable systems. These are characterized by Hamiltonians of the form

$$
H ( \mathbf { p } , \mathbf { q } ) = \sum _ { l = 1 } ^ { L } H _ { l } ( p _ { l } , q _ { l } ) .
$$

All the partial Hamiltonians $H _ { l }$ are in involution with one another and with the full Hamiltonian $H$ .Choosing the corresponding partial energies $E _ { \imath }$ as constants of the motion,we obtain the action variables $I _ { \imath }$ independently from equations like (6.2O). The most powerful general method for integrating the equations of motion, that of Hamilton and Jacobi, relies on transformations to coordinates that separate the Hamiltonian. This is discussed by Arnold (1978) and Goldstein (198O). It follows that the Hamilton-Jacobi method can be applied only to integrable systems.

In the case of a two-dimensional harmonic oscillator or of a pair of uncoupled oscillators, the Hamiltonian will be

$$
\begin{array} { r } { H ( \mathbf { I } ) = \omega _ { 1 } I _ { 1 } + \omega _ { 2 } I _ { 2 } . } \end{array}
$$

Its level curves are straight-line segments (fig. 6.8). The frequencies are the same for all tori, so that all orbits are periodic if the $\omega _ { j }$ are rationally related. Otherwise,the orbits are all open.In the case where $\omega _ { 1 } = \omega _ { 2 }$ , the oscillator is isotropic.The fact that all orbits are then periodic may be attributed to the existence of a further constant of the motion $p _ { \pmb { \theta } }$ ,independent of $H _ { 1 }$ and $H _ { 2 }$ .The intersection of the level curves of these three functions is a closed curve,which defines the orbit.

The caustics for the torus of a separable system of two freedoms are easily found from the construction shown in fig. 6.9. The independence of the motion in the conjugate planes $\left( { { p } _ { 1 } } , { { q } _ { 1 } } \right)$ and $\left( { { p } _ { 2 } } , { { q } _ { 2 } } \right)$ implies that the caustics are straight-line segments corresponding to the turning points. Therefore, the torus projects onto the configuration plane as a rectangle. Any point $\pmb q$ inside it corresponds to four points on the torus with coordinates $( p _ { 1 } ^ { \pm } , q _ { 1 } ^ { \pm } )$ Two pairs coalesce on the (double) caustic. This projection of a smooth torus would be impossible were it embedded in three-dimensional space rather than in four dimensions. We can still ‘visualize' this projection by considering a vertical tyre tube (i.e., the position in which it rolls on the ground). When emptied of air, it collapses into a rectangle on the floor, just as our separable torus, but it is no longer smooth. In a four-dimensional space we can now fillit out along the fourth dimension' without altering the projection.

![](images/19d990c5bc5236a411e6c23a9705b9ea798fcb44300c440fd85977dbc3ccfeab.jpg)  
Fig. 6.8. The Hamiltonian for a two-dimensional oscillator is a linear function of the actions.

![](images/0b7522c60187ffcceba544a1566ed98e1701a0edb8aada2508621acc21890902.jpg)  
Fig.6.9. From the phase graphs of the two independent motions of a separable system,we obtain the projection of the torus onto the configuration space.Each point inside the rectangle is the image of four points inside the torus.

A final important example of integrable systems is provided by the normal-form Hamiltonians,which approximately describe the motion surrounding a stable periodic orbit, studied in section 4.4. Truncating the Birkhoff normal form, we obtain an integrable system, the action-angle variables of which are $I$ and $\pmb { J }$ 、Even the resonant normal forms are integrable systems and almost all points lie on tori, though this is not true for the points lying along separatrices in the $( I , \theta )$ plane.The reason is that these are level curves of the reduced Hamiltonian $H ( I , \theta )$ (a constant of the motion) with the same partial energy as one of its equilibria. At such a point the vector field $( { \dot { I } } , { \dot { \theta } } ) = 0 .$ ，contrary to the assumptions in the Arnold-Liouville theorem. The phase space of a system with separatrices cannot be globally transformed to action-angle variables. This is possible only for each separate family of tori.

# 6.3 Caustics

The previous examples have made familiar the fact that ${ \pmb \ p } ( { \pmb q } )$ for an invariant torus and hence the action $S ( \mathbf { q } )$ ,defined by(6.14),are multivalued functions. The caustics limiting the motion in configuration space are the boundaries of the branches of $S ( \mathbf { q } )$ . They correspond to the set of points in phase space where

$$
\operatorname* { d e t } d { \mathfrak { p } } / d { \mathfrak { q } } = \infty .
$$

The way that different branches of $S ( \mathbf { q } )$ join together at a caustic can be analysed by means of its Legendre transform,

$$
S ( { \bf { p } } ) = { \bf { p } } { \bf { \cdot q } } - S ( { \bf { q } } ) ,
$$

where ${ \bf q } ( { \bf p } )$ is given by (6.15). In the case of one freedom, we can make the graphical construction shown in fig. 6.10. The Lagrangian condition on the

![](images/17048aa3933bba4d1184a76dee79caf1a969a55f193c877d6e83cf7a827685f9.jpg)  
Fig. 6.10. Graphical construction of the action $s ( \mathfrak { p } )$ given $\pmb { S ( \mathfrak { q } ) } ;$ together they make up the area of a rectangle.

invariant torus implies that

$$
\oint \mathbf { q } \cdot d \mathbf { p } = - \oint \mathbf { p } \cdot d \mathbf { q } = 0 .
$$

Therefore, the function

$$
S ( \mathbf { p } ) = \int _ { \mathbf { p } _ { 0 } } ^ { \mathbf { p } } \mathbf { q } \cdot d \mathbf { p }
$$

is the same function defined by (6.34) within an additive constant. This function is also multivalued, and its branches join at caustics of the projection of the torus onto the p space (fig. 6.11). However, $S ( \mathbf { \boldsymbol { \mathsf { p } } } )$ is a one-toone function in the neighbourhood of the caustics of $S ( \mathbf { q } )$ Differentiating (6.36),

$$
\begin{array} { r } { \mathbf { q } = \partial S ( \mathbf { p } ) / \partial \mathbf { p } , } \end{array}
$$

![](images/f00ba4f348987d012076bd60d3799fe5a52289be8c10458b55b94f769c73e07c.jpg)  
Fig. 6.11. The function $s ( \mathfrak { p } )$ is multivalued like ${ \pmb S } ( { \pmb q } )$ .The branches meet at the caustics $p ^ { + }$ and $p ^ { - }$