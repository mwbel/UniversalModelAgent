It doesn’t matter, of course, the order in which we put the names into the hash. Here is a piece of code to loop over years, printing the people born in that year:

string str;   
for (Int i=1750;i<1800;i++) if (person.getinit(i)) { cout << ’\n’ << "born in $" " < < \mathrm { ~ i ~ } < < \mathrm { ~ " ~ } : \backslash \mathrm { n " ~ } ;$ while (person.getnext(str)) cout << str.data() << ’\n’; }   
}

which gives as output born in 1755: Marie Antoinette born in 1767: Andrew Jackson John Quincy Adams born in 1770: Ludwig van Beethoven born in 1775: Jane Austen born in 1791: Charles Babbage James Buchanan Samuel Morse

Notice that we could not have used null terminated C strings in this example, because $\mathrm { C } { + } { + }$ does not regard them as first-class objects that can be stored as elements of a vector. When you are using Hash or Mhash with strings, you will usually be better off using the $\mathrm { C } { + } { + }$ string class.

In $\ S 2 1 . 2$ and $\ S 2 1 . 8$ we will make extensive use of both the Hash and Mhash classes and almost all their member functions; look there for further usage examples.

By the way, Mr. Hacher’s name is from the French hacher, meaning “to mince or hash.”

# CITED REFERENCES AND FURTHER READING:

Stroustrup, B. 1997, The $C { + + }$ Programming Language, 3rd ed. (Reading, MA: Addison-Wesley), $\ S 1 7 . 6 . 2$ .[1]   
Knuth, D.E. 1997, Sorting and Searching, 3rd ed., vol. 3 of The Art of Computer Programming (Reading, MA: Addison-Wesley), $\ S 6 . 4 \mathrm { - } \ S 6 . 5$ .   
Vitter, J.S., and Chen, W-C. 1987, Design and Analysis of Coalesced Hashing (New York: Oxford University Press).

# 7.7 Simple Monte Carlo Integration

Inspirations for numerical methods can spring from unlikely sources. “Splines” first were flexible strips of wood used by draftsmen. “Simulated annealing” (we shall

![](images/2aba06665e95d8b255948fd5e0ccc4c797fdc99178bf944552ea173fc4c57119.jpg)  
Figure 7.7.1. Monte Carlo integration of a function $f ( x , y )$ in a region $W$ . Random points are chosen within an area $V$ that includes $W$ and that can easily be sampled uniformly. Of the three possible $V$ ’s shown, $V _ { 1 }$ is a poor choice because $W$ occupies only a small fraction of its area, while $V _ { 2 }$ and $V _ { 3 }$ are better choices.

see in $\ S 1 0 . 1 2 )$ is rooted in a thermodynamic analogy. And who does not feel at least a faint echo of glamor in the name “Monte Carlo method”?

Suppose that we pick $N$ random points, uniformly distributed in a multidimensional volume $V$ . Call them $x _ { 0 } , \ldots , x _ { N - 1 }$ . Then the basic theorem of Monte Carlo integration estimates the integral of a function $f$ over the multidimensional volume,

$$
\int f d V \approx V \langle f \rangle \pm V { \sqrt { \frac { \langle f ^ { 2 } \rangle - \langle f \rangle ^ { 2 } } { N } } }
$$

Here the angle brackets denote taking the arithmetic mean over the $N$ sample points,

$$
\langle f \rangle \equiv { \frac { 1 } { N } } \sum _ { i = 0 } ^ { N - 1 } f ( x _ { i } ) \qquad \left. f ^ { 2 } \right. \equiv { \frac { 1 } { N } } \sum _ { i = 0 } ^ { N - 1 } f ^ { 2 } ( x _ { i } )
$$

The “plus-or-minus” term in (7.7.1) is a one standard deviation error estimate for the integral, not a rigorous bound; further, there is no guarantee that the error is distributed as a Gaussian, so the error term should be taken only as a rough indication of probable error.

Suppose that you want to integrate a function $g$ over a region $W$ that is not easy to sample randomly. For example, $W$ might have a very complicated shape. No problem. Just find a region $V$ that includes $W$ and that can easily be sampled, and then define $f$ to be equal to $g$ for points in $W$ and equal to zero for points outside of $W$ (but still inside the sampled $V$ ). You want to try to make $V$ enclose $W$ as closely as possible, because the zero values of $f$ will increase the error estimate term of (7.7.1). And well they should: Points chosen outside of $W$ have no information content, so the effective value of $N$ , the number of points, is reduced. The error estimate in (7.7.1) takes this into account.

Figure 7.7.1 shows three possible regions $V$ that might be used to sample a complicated region $W$ . The first, $V _ { 1 }$ , is obviously a poor choice. A good choice, $V _ { 2 }$ , can be sampled by picking a pair of uniform deviates $( s , t )$ and then mapping them into $( x , y )$ by a linear transformation. Another good choice, $V _ { 3 }$ , can be sampled by, first, using a uniform deviate to choose between the left and right rectangular subregions (in proportion to their respective areas!) and, then, using two more deviates to pick a point inside the chosen rectangle.

Let’s create an object that embodies the general scheme described. (We will discuss the implementing code later.) The general idea is to create an MCintegrate object by providing (as constructor arguments) the following items:

- a vector xlo of lower limits of the coordinates for the rectangular box to be sampled   
- a vector xhi of upper limits of the coordinates for the rectangular box to be sampled   
- a vector-valued function funcs that returns as its components one or more functions that we want to integrate simultaneously   
a boolean function that returns whether a point is in the (possibly complicated) region $W$ that we want to integrate; the point will already be within the region $V$ defined by xlo and xhi   
- a mapping function to be discussed below, or NULL if there is no mapping function or if your attention span is too short   
- a seed for the random number generator

The object MCintegrate has this structure.

# struct MCintegrate {

Object for Monte Carlo integration of one or more functions in an ndim-dimensional region.

Int ndim,nfun,n; Number of dimensions, functions, and points sampled.   
VecDoub ff,fferr; Answers: The integrals and their standard errors.   
VecDoub xlo,xhi,x,xx,fn,sf,sferr;   
Doub vol; Volume of the box V .

Pointers to the user-supplied functions.

VecDoub (\*funcsp)(const VecDoub &);   
VecDoub (\*xmapp)(const VecDoub &);   
Bool (\*inregionp)(const VecDoub &);   
Ran ran;

Random number generator.

MCintegrate(const VecDoub &xlow, const VecDoub &xhigh, VecDoub funcs(const VecDoub &), Bool inregion(const VecDoub &), VecDoub xmap(const VecDoub &), Int ranseed); Constructor. The arguments are in the order described in the itemized list above.

void step(Int nstep);   
Sample an additional nstep points, accumulating the various sums.

void calcanswers();

Calculate answers ff and fferr using the current sums.

The member function step adds sample points, the number of which is given by its argument. The member function calcanswers updates the vectors ff and fferr, which contain respectively the estimated Monte Carlo integrals of the functions and the errors on these estimates. You can examine these values, and then, if you want, call step and calcanswers again to further reduce the errors.

A worked example will show the underlying simplicity of the method. Suppose that we want to find the weight and the position of the center of mass of an object of complicated shape, namely the intersection of a torus with the faces of a large box. In particular, let the object be defined by the three simultaneous conditions:

![](images/aae3fc3f4f9571759a2c98a37a989c92caee855b9d90b61019dafb43b4cd73cf.jpg)  
Figure 7.7.2. Example of Monte Carlo integration (see text). The region of interest is a piece of a torus, bounded by the intersection of two planes. The limits of integration of the region cannot easily be written in analytically closed form, so Monte Carlo is a useful technique.

$$
z ^ { 2 } + \left( \sqrt { x ^ { 2 } + y ^ { 2 } } - 3 \right) ^ { 2 } \leq 1
$$

(torus centered on the origin with major radius $= 3$ , minor radius $= 1$ )

$$
x \geq 1 \qquad y \geq - 3
$$

(two faces of the box; see Figure 7.7.2). Suppose for the moment that the object has a constant density $\rho = 1$ .

We want to estimate the following integrals over the interior of the complicated object:

$$
\int \rho d x d y d z \qquad \int x \rho d x d y d z \qquad \int y \rho d x d y d z \qquad \int z \rho d x d y d z
$$

The coordinates of the center of mass will be the ratio of the latter three integrals (linear moments) to the first one (the weight).

To use the MCintegrate object, we first write functions that describe the integrands and the region of integration $W$ inside the box $V$ .

VecDoub torusfuncs(const VecDoub &x) {

Return the integrands in equation (7.7.5), with $\rho = 1$

Doub den $\mathit { \Theta } = \mathit { \Theta } 1 \cdot$ ;   
VecDoub f(4);   
$\mathbf { f } \left[ 0 \right] \mathbf { \tau } =$ den;   
for (Int $\dot { 1 } = 1$ ;i<4; $\Dot { \ b { 1 } } + +$ ) f[i] = x[i-1]\*den;   
return f;

# }

Bool torusregion(const VecDoub &x) {   
Return the inequality (7.7.3). return SQR(x[2])+SQR(sqrt(SQR(x[0])+SQR(x[1]))-3.) <= 1.;   
}

The code to actually do the integration is now quite simple,

VecDoub xlo(3), xhi(3);   
xlo[0] $=$ 1.; xhi[0] $\mathit { \Theta } = \mathit { \Theta } 4 .$ ;   
xlo[1] $= \ - 3 .$ ; xhi[1] $= ~ 4 .$ ;   
xlo[2] $\ c = - 1$ .; xhi[2] $\mathit { \Theta } = \mathit { \Theta } 1 \cdot$ ;   
MCintegrate mymc(xlo,xhi,torusfuncs,torusregion,NULL,10201);   
mymc.step(1000000);   
mymc.calcanswers();

Here we’ve specified the box $V$ by $\tt x l o$ and xhi, created an instance of MCintegrate, sampled a million times, and updated the answers mymc.ff and mymc.fferr, which can be accessed for printing or another use.

# 7.7.1 Change of Variables

A change of variable can often be extremely worthwhile in Monte Carlo integration. Suppose, for example, that we want to evaluate the same integrals, but for a piece of torus whose density is a strong function of $Z$ , in fact varying according to

$$
\rho ( x , y , z ) = e ^ { 5 z }
$$

One way to do this is, in torusfuncs, simply to replace the statement

# Doub ${ \mathsf { d e n } } \ = \ 1 .$ ;

by the statement

Doub ${ \mathsf { d e n } } \ = \ \exp ( { \mathsf { S } } \cdot * { \mathbf { x } } [ 2 ] ) \ ;$

This will work, but it is not the best way to proceed. Since (7.7.6) falls so rapidly to zero as $Z$ decreases (down to its lower limit $^ { - 1 }$ ), most sampled points contribute almost nothing to the sum of the weight or moments. These points are effectively wasted, almost as badly as those that fall outside of the region $W$ . A change of variable, exactly as in the transformation methods of $\ S 7 . 3$ , solves this problem. Let

$$
\begin{array} { r } { d s = e ^ { 5 z } d z \qquad \mathrm { ~ s o ~ t h a t ~ } \qquad s = \frac { 1 } { 5 } e ^ { 5 z } , \quad z = \frac { 1 } { 5 } \ln ( 5 s ) } \end{array}
$$

Then $\rho d z = d s$ , and the limits $- 1 < z < 1$ become : $0 0 1 3 5 < s < 2 9 . 6 8 2$ .

The MCintegrate object knows that you might want to do this. If it sees an argument xmap that is not NULL, it will assume that the sampling region defined by xlo and xhi is not in physical space, but rather needs to be mapped into physical space before either the functions or the region boundary are calculated. Thus, to effect our change of variable, we don’t need to modify torusfuncs or torusregion, but we do need to modify $\tt x l o$ and xhi, as well as supply the following function for the argument xmap:

VecDoub torusmap(const VecDoub &s) {

Return the mapping from $s$ to $z$ defined by the last equation in (7.7.7), mapping the other coordinates by the identity map.

VecDoub xx(s);   
$\arg { \frac { \ d } { \ d t } } = { \bf \nabla } _ { 0 } . 2 \ast \mathrm { { 1 0 g } } \left( 5 . \ast \bf { _ { S } } \left[ 2 \right] \right) ,$ ;   
return xx;

Code for the actual integration now looks like this:

VecDoub slo(3), shi(3);   
slo[0] $\mathbf { \lambda } = \mathbf { \lambda } _ { 1 } . \mathbf { \lambda } ;$ shi[0] $\mathit { \Theta } = \mathit { \Theta } 4 \cdot$ ;   
slo[1] $=$ -3.; shi[1] $= ~ 4 .$ ;   
slo[2] $=$ 0.2\*exp(5.\*(-1.)); shi[2] $=$ 0.2\*exp(5.\*(1.));   
MCintegrate mymc2(slo,shi,torusfuncs,torusregion,torusmap,10201);   
mymc2.step(1000000);   
mymc2.calcanswers();

If you think for a minute, you will realize that equation (7.7.7) was useful only because the part of the integrand that we wanted to eliminate $( e ^ { 5 z } )$ was both integrable analytically and had an integral that could be analytically inverted. (Compare $\ S 7 . 3 . 2 .$ ) In general these properties will not hold. Question: What then? Answer: Pull out of the integrand the “best” factor that can be integrated and inverted. The criterion for “best” is to try to reduce the remaining integrand to a function that is as close as possible to constant.

The limiting case is instructive: If you manage to make the integrand $f$ exactly constant, and if the region $V$ , of known volume, exactly encloses the desired region $W$ , then the average of $f$ that you compute will be exactly its constant value, and the error estimate in equation (7.7.1) will exactly vanish. You will, in fact, have done the integral exactly, and the Monte Carlo numerical evaluations are superfluous. So, backing off from the extreme limiting case, to the extent that you are able to make $f$ approximately constant by change of variable, and to the extent that you can sample a region only slightly larger than $W$ , you will increase the accuracy of the Monte Carlo integral. This technique is generically called reduction of variance in the literature.

The fundamental disadvantage of simple Monte Carlo integration is that its accuracy increases only as the square root of $N$ , the number of sampled points. If your accuracy requirements are modest, or if your computer is large, then the technique is highly recommended as one of great generality. In $\ S 7 . 8$ and $\ S 7 . 9$ we will see that there are techniques available for “breaking the square root of $N$ barrier” and achieving, at least in some cases, higher accuracy with fewer function evaluations.

There should be nothing surprising in the implementation of MCintegrate. The constructor stores pointers to the user functions, makes an otherwise superfluous call to funcs just to find out the size of returned vector, and then sizes the sum and answer vectors accordingly. The step and calcanswer methods implement exactly equations (7.7.1) and (7.7.2).

MCintegrate::MCintegrate(const VecDoub &xlow, const VecDoub &xhigh, VecDoub funcs(const VecDoub &), Bool inregion(const VecDoub &), VecDoub xmap(const VecDoub &), Int ranseed) : ndim(xlow.size()), ${ \mathfrak { n } } ( 0 )$ , xlo(xlow), xhi(xhigh), x(ndim), xx(ndim), funcsp(funcs), xmapp(xmap), inregionp(inregion), vol(1.), ran(ranseed) if (xmapp) nfun $=$ funcs(xmapp(xlo)).size(); else nfun $=$ funcs(xlo).size(); ff.resize(nfun); fferr.resize(nfun);

fn.resize(nfun);   
sf.assign(nfun,0.);   
sferr.assign(nfun,0.);   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<ndim;j++) vol $\ast =$ abs(xhi[j]-xlo[j]);

# }

void MCintegrate::step(Int nstep) { Int i,j; for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<nstep; $\dot { 1 } + +$ ) { for (j=0;j<ndim; $\mathrm { j } + +$ ) x[j] $=$ xlo[j]+(xhi[j]-xlo[j])\*ran.doub(); if (xmapp) xx $=$ (\*xmapp)(x); else $\mathbf { \boldsymbol { x } } \mathbf { \boldsymbol { x } } \ = \mathbf { \boldsymbol { x } }$ ; if ((\*inregionp)(xx)) { fn $=$ (\*funcsp)(xx); for (j=0;j<nfun;j++) { sf[j] $+ =$ fn[j]; sferr[j] $+ =$ SQR(fn[j]); } } } n $+ =$ nstep;   
}   
void MCintegrate::calcanswers(){ for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<nfun;j++) { ff[j] $=$ vol\*sf[j]/n; fferr[j] $=$ vol\*sqrt((sferr[j]/n-SQR(sf[j]/n))/n); }   
}

# CITED REFERENCES AND FURTHER READING:

Robert, C.P., and Casella, G. 2006, Monte Carlo Statistical Methods, 2nd ed. (New York: Springer) Sobol’, I.M. 1994, A Primer for the Monte Carlo Method (Boca Raton, FL: CRC Press). Hammersley, J.M., and Handscomb, D.C. 1964, Monte Carlo Methods (London: Methuen). Gentle, J.E. 2003, Random Number Generation and Monte Carlo Methods, 2nd ed. (New York: Springer), Chapter 7. Shreider, Yu. A. (ed.) 1966, The Monte Carlo Method (Oxford: Pergamon). Kalos, M.H., and Whitlock, P.A. 1986, Monte Carlo Methods: Volume 1 : Basics (New York: Wiley).

# 7.8 Quasi- (that is, Sub-) Random Sequences

We have just seen that choosing $N$ points uniformly randomly in an $n$ -dimensional space leads to an error term in Monte Carlo integration that decreases as $1 / \sqrt { N }$ . In essence, each new point sampled adds linearly to an accumulated sum that will become the function average, and also linearly to an accumulated sum of squares that will become the variance (equation 7.7.2). The estimated error comes from the square root of this variance, hence the power $N ^ { - 1 / 2 }$ .

Just because this square-root convergence is familiar does not, however, mean that it is inevitable. A simple counterexample is to choose sample points that lie on a Cartesian grid, and to sample each grid point exactly once (in whatever order).

The Monte Carlo method thus becomes a deterministic quadrature scheme — albeit a simple one — whose fractional error decreases at least as fast as $N ^ { - 1 }$ (even faster if the function goes to zero smoothly at the boundaries of the sampled region or is periodic in the region).

The trouble with a grid is that one has to decide in advance how fine it should be. One is then committed to completing all of its sample points. With a grid, it is not convenient to “sample until” some convergence or termination criterion is met. One might ask if there is not some intermediate scheme, some way to pick sample points “at random,” yet spread out in some self-avoiding way, avoiding the chance clustering that occurs with uniformly random points.

A similar question arises for tasks other than Monte Carlo integration. We might want to search an $n$ -dimensional space for a point where some (locally computable) condition holds. Of course, for the task to be computationally meaningful, there had better be continuity, so that the desired condition will hold in some finite $n$ - dimensional neighborhood. We may not know a priori how large that neighborhood is, however. We want to “sample until” the desired point is found, moving smoothly to finer scales with increasing samples. Is there any way to do this that is better than uncorrelated, random samples?

The answer to the above question is “yes.” Sequences of $n$ -tuples that fill $n$ - space more uniformly than uncorrelated random points are called quasi-random sequences. That term is somewhat of a misnomer, since there is nothing “random” about quasi-random sequences: They are cleverly crafted to be, in fact, subrandom. The sample points in a quasi-random sequence are, in a precise sense, “maximally avoiding” of each other.

A conceptually simple example is Halton’s sequence [1]. In one dimension, the $j$ th number $H _ { j }$ in the sequence is obtained by the following steps: (i) Write $j$ as a number in base $b$ , where $b$ is some prime. (For example, $j = 1 7$ in base $b = 3$ is 122.) (ii) Reverse the digits and put a radix point (i.e., a decimal point base $b$ ) in front of the sequence. (In the example, we get 0:221 base 3.) The result is $H _ { j }$ . To get a sequence of $n$ -tuples in $n$ -space, you make each component a Halton sequence with a different prime base $b$ . Typically, the first $n$ primes are used.

It is not hard to see how Halton’s sequence works: Every time the number of digits in $j$ increases by one place, $j$ ’s digit-reversed fraction becomes a factor of $b$ finer-meshed. Thus the process is one of filling in all the points on a sequence of finer and finer Cartesian grids — and in a kind of maximally spread-out order on each grid (since, e.g., the most rapidly changing digit in $j$ controls the most significant digit of the fraction).

Other ways of generating quasi-random sequences have been proposed by Faure, Sobol’, Niederreiter, and others. Bratley and Fox [2] provide a good review and references, and discuss a particularly efficient variant of the Sobol’ [3] sequence suggested by Antonov and Saleev [4]. It is this Antonov-Saleev variant whose implementation we now discuss.

The Sobol’ sequence generates numbers between zero and one directly as binary fractions of length $w$ bits, from a set of $w$ special binary fractions, $V _ { i }$ ; $i = 1 , 2 , \dots , w$ , called direction numbers. In Sobol’s original method, the $j$ th number $X _ { j }$ is generated by XORing (bitwise exclusive or) together the set of $V _ { i }$ ’s satisfying the criterion on $i$ , “the $i$ th bit of $j$ is nonzero.” As $j$ increments, in other words, different ones of the $V _ { i }$ ’s flash in and out of $X _ { j }$ on different time scales. $V _ { 1 }$ alternates between being present and absent most quickly, while

![](images/409dec64a804d90a731181cd4113d753120deb0643d22d98ab3519377943c179.jpg)  
Figure 7.8.1. First 1024 points of a two-dimensional Sobol’ sequence. The sequence is generated numbertheoretically, rather than randomly, so successive points at any stage “know” how to fill in the gaps in the previously generated distribution.

$V _ { k }$ goes from present to absent (or vice versa) only every $2 ^ { k - 1 }$ steps.

Antonov and Saleev’s contribution was to show that instead of using the bits of the integer $j$ to select direction numbers, one could just as well use the bits of the Gray code of $j , G ( j )$ . (For a quick review of Gray codes, look at $\ S 2 2 . 3 .$ )

Now $G ( j )$ and $G ( j + 1 )$ differ in exactly one bit position, namely in the position of the rightmost zero bit in the binary representation of $j$ (adding a leading zero to $j$ if necessary). A consequence is that the $j + 1 \mathrm { s t }$ Sobol’-Antonov-Saleev number can be obtained from the $j$ th by XORing it with a single $V _ { i }$ , namely with $i$ the position of the rightmost zero bit in $j$ . This makes the calculation of the sequence very efficient, as we shall see.

Figure 7.8.1 plots the first 1024 points generated by a two-dimensional Sobol’ sequence. One sees that successive points do “know” about the gaps left previously, and keep filling them in, hierarchically.

We have deferred to this point a discussion of how the direction numbers $V _ { i }$ are generated. Some nontrivial mathematics is involved in that, so we will content ourselves with a cookbook summary only: Each different Sobol’ sequence (or component of an $n$ -dimensional sequence) is based on a different primitive polynomial over the integers modulo 2, that is, a polynomial whose coefficients are either 0 or 1, and which generates a maximal length shift register sequence. (Primitive polynomials modulo 2 were used in $\ S 7 . 5$ and are further discussed in $\ S 2 2 . 4 .$ ) Suppose $P$ is such a polynomial, of degree $q$ ,

<table><tr><td rowspan=1 colspan=1>Degree</td><td rowspan=1 colspan=1>Primitive Polynomials Modulo 2*</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0 (i.e., x+1)</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1 (i.e., x² + x+1)</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>1,2 (i.e.,x³ + x +1 and x³+ x²+1)</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>1,4 (i.e.,x4 +x+1 and x4 +x+1)</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>2,4,7, 11,13,14</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>1,13,16,19,22,25</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>1,4,7,8,14,19,21,28,31,32,37,41,42,50,55,56,59,62</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>14,21,22,38,47,49,50,52,56,67,70,84,97,103,115,122</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>8,13,16,22,25,44,47,52,55,59,62,67,74,81,82,87,91,94,103,104,109,122,124,137,138,143,145,152,157,167,173,176,181,182,185,191,194,199,218,220,227,229,230,234,236,241,244,253</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>4,13,19,22,50,55,64,69,98,107,115,121,127,134,140,145,152,158,161,171,181,194,199,203,208,227,242,251,253,265,266,274,283,289,295,301,316,319,324,346,352,361,367,382,395,398,400,412,419,422,426,428,433,446,454,457,472,493,505,508</td></tr><tr><td rowspan=1 colspan=2>*Expressed as a decimal integer whose binary representation gives the coefficients,from thehighest to lowest power of x.Only the internal terms are represented—the highest-order termand the constant term always have coefficient 1.</td></tr></table>

$$
P = x ^ { q } + a _ { 1 } x ^ { q - 1 } + a _ { 2 } x ^ { q - 2 } + \cdots + a _ { q - 1 } x + 1
$$

Define a sequence of integers $M _ { i }$ by the $q$ -term recurrence relation,

$$
M _ { i } = 2 a _ { 1 } M _ { i - 1 } \oplus 2 ^ { 2 } a _ { 2 } M _ { i - 2 } \oplus \cdots \oplus 2 ^ { q - 1 } M _ { i - q + 1 } a _ { q - 1 } \oplus ( 2 ^ { q } M _ { i - q } \oplus M _ { i - q } )
$$

Here bitwise XOR is denoted by $\oplus$ . The starting values for this recurrence are that $M _ { 1 } , \dots , M _ { q }$ can be arbitrary odd integers less than $2 , \ldots , 2 ^ { q }$ , respectively. Then, the direction numbers $V _ { i }$ are given by

$$
V _ { i } = M _ { i } / 2 ^ { i } \qquad i = 1 , \dots , w
$$

The table above lists all primitive polynomials modulo 2 with degree $q \leq 1 0$ . Since the coefficients are either 0 or 1, and since the coefficients of $x ^ { q }$ and of 1 are predictably 1, it is convenient to denote a polynomial by its middle coefficients taken as the bits of a binary number (higher powers of $x$ being more significant bits). The table uses this convention.

Turn now to the implementation of the Sobol’ sequence. Successive calls to the function sobseq (after a preliminary initializing call) return successive points in an $n$ -dimensional Sobol’ sequence based on the first $n$ primitive polynomials in the table. As given, the routine is initialized for maximum $n$ of 6 dimensions, and for a word length $w$ of 30 bits. These parameters can be altered by changing MAXBIT $( \equiv w )$ ) and MAXDIM, and by adding more initializing data to the arrays ip (the primitive polynomials from the table above), mdeg (their degrees), and iv (the starting values for the recurrence, equation 7.8.2). A second table, on the next page, elucidates the initializing data in the routine.

<table><tr><td rowspan=1 colspan=6>Initializing Values Used in sobseq</td></tr><tr><td rowspan=1 colspan=1>Degree</td><td rowspan=1 colspan=1>Polynomial</td><td rowspan=1 colspan=4>Starting Values</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>(3)</td><td rowspan=1 colspan=1>(5)</td><td rowspan=1 colspan=1>(15)...</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>(11)...</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>(5)...</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>(15)...</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>13...</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>9...</td></tr><tr><td rowspan=1 colspan=6>Parenthesized values are not freely specifiable,but are forced by the requiredrecurrence for this degree.</td></tr></table>

# void sobseq(const Int n, VecDoub_O &x)

When n is negative, internally initializes a set of MAXBIT direction numbers for each of MAXDIM different Sobol’ sequences. When n is positive (but MAXDIM), returns as the vector $\mathbf { x } \left[ 0 \ldots \mathbf { n - 1 } \right]$ the next values from n of these sequences. (n must not be changed between initializations.) {

const Int MAXBIT $\scriptstyle = 3 0$ ,MAXDIM=6;   
Int j,k,l;   
Uint i,im,ipp;   
static Int mdeg[MAXDIM] $=$ {1,2,3,3,4,4};   
static Uint in;   
static VecUint ix(MAXDIM);   
static NRvector<Uint\*> iu(MAXBIT);   
static Uint ip[MAXDIM] $= \{ 0$ ,1,1,2,1,4};   
static Uint iv[MAXDIM\*MAXBIT] $=$ {1,1,1,1,1,1,3,1,3,3,1,1,5,7,7,3,3,5,15,11,5,15,13,9};   
static Doub fac;   
if $\mathbf { \chi } _ { \mathbf { n } } \ < \ 0$ ) { Initialize, don’t return a vector. for (k=0;k<MAXDIM; $\mathrm { k } { + } { + }$ ) ix[k] ${ = } 0$ ; $\mathtt { i n } { = } 0$ ; if (iv[0] $! = ~ 1 ^ { \prime }$ ) return; fac $^ { = 1 }$ .0/(1 << MAXBIT); for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ,k=0;j<MAXBIT;j++, $\xi + =$ MAXDIM) iu[j] $=$ &iv[k]; To allow both 1D and 2D addressing. for $( \mathrm { k } = 0$ ;k<MAXDIM; $\mathrm { k } { + } { + }$ ) { for ( $\scriptstyle \cdot j = 0$ ;j<mdeg[k]; $\mathrm { j } { + + } )$ ) iu[j][k] <<= (MAXBIT-1-j); Stored values only require normalization. for (j=mdeg[k];j<MAXBIT;j++) { Use the recurrence to get other valipp=ip[k]; ues. $\dot { \bf 1 } =$ iu[j-mdeg[k]][k]; i $\hat { \bf \Phi } =$ (i >> mdeg[k]); for ( $\ b { 1 } =$ mdeg[k]-1; $\scriptstyle 1 > = 1$ ;l--) { if (ipp & 1) i $\hat { \bf \Phi } =$ iu[j-l][k]; ipp $> > = ~ 1$ ; } iu[j][k] ${ \bf \Phi } = \dot { \bf 1 }$ ; } }   
} else { Calculate the next vector in the seim=in++; quence. for (j=0;j<MAXBIT;j++) { Find the rightmost zero bit. if (!(im & 1)) break; im $> > = ~ 1$ ; }

if (j $> =$ MAXBIT) throw("MAXBIT t im=j\*MAXDIM; for $\scriptstyle ( \mathtt { k } = 0$ ;k<MIN(n,MAXDIM); $\mathbf { \nabla } \cdot \mathbf { k } { + + }$ ) { ix[k] $\hat { \mathbf { \alpha } } =$ iv[im+k]; x[k] $\mathbf { \mu } = \ j \mathbf { \mu } _ { \mathbf { X } }$ [k]\*fac; } } }

XOR the appropriate direction number into each component of the vector and convert to a floating number.

How good is a Sobol’ sequence, anyway? For Monte Carlo integration of a smooth function in $n$ dimensions, the answer is that the fractional error will decrease with $N$ , the number of samples, as $( \ln N ) ^ { n } / N$ , i.e., almost as fast as $1 / N$ . As an example, let us integrate a function that is nonzero inside a torus (doughnut) in three-dimensional space. If the major radius of the torus is $R _ { 0 }$ and the minor radius is $r _ { 0 }$ , the minor radial coordinate $r$ is defined by

$$
r = \left( [ ( x ^ { 2 } + y ^ { 2 } ) ^ { 1 / 2 } - R _ { 0 } ] ^ { 2 } + z ^ { 2 } \right) ^ { 1 / 2 }
$$

Let us try the function

$$
f ( x , y , z ) = \left\{ \begin{array} { l l } { 1 + \cos \left( \displaystyle \frac { \pi r ^ { 2 } } { r _ { 0 } ^ { 2 } } \right) } & { \quad r < r _ { 0 } } \\ { 0 } & { \quad r \geq r _ { 0 } } \end{array} \right.
$$

which can be integrated analytically in cylindrical coordinates, giving

$$
\iiint d x d y d z f ( x , y , z ) = 2 \pi ^ { 2 } r _ { 0 } ^ { 2 } R _ { 0 }
$$

With parameters $R _ { 0 } = 0 . 6 , r _ { 0 } = 0 . 3$ , we did 100 successive Monte Carlo integrations of equation (7.8.4), sampling uniformly in the region $- 1 < x , y , z \ < \ 1$ , for the two cases of uncorrelated random points and the Sobol’ sequence generated by the routine sobseq. Figure 7.8.2 shows the results, plotting the r.m.s. average error of the 100 integrations as a function of the number of points sampled. (For any single integration, the error of course wanders from positive to negative, or vice versa, so a logarithmic plot of fractional error is not very informative.) The thin, dashed curve corresponds to uncorrelated random points and shows the familiar $N ^ { - 1 / 2 }$ asymptotics. The thin, solid gray curve shows the result for the Sobol’ sequence. The logarithmic term in the expected $( \mathrm { l n } \bar { N } ) ^ { 3 } / N$ is readily apparent as curvature in the curve, but the asymptotic $N ^ { - 1 }$ is unmistakable.

To understand the importance of Figure 7.8.2, suppose that a Monte Carlo integration of $f$ with $1 \%$ accuracy is desired. The Sobol’ sequence achieves this accuracy in a few thousand samples, while pseudo-random sampling requires nearly 100,000 samples. The ratio would be even greater for higher desired accuracies.

A different, not quite so favorable, case occurs when the function being integrated has hard (discontinuous) boundaries inside the sampling region, for example the function that is one inside the torus and zero outside,

$$
f ( x , y , z ) = \left\{ { \begin{array} { l l } { 1 ~ } & { ~ r < r _ { 0 } } \\ { 0 ~ } & { ~ r \geq r _ { 0 } } \end{array} } \right.
$$

where $r$ is defined in equation (7.8.4). Not by coincidence, this function has the same analytic integral as the function of equation (7.8.5), namely $2 \pi ^ { 2 } r _ { 0 } ^ { 2 } R _ { 0 }$ .

The carefully hierarchical Sobol’ sequence is based on a set of Cartesian grids, but the boundary of the torus has no particular relation to those grids. The result is that it is essentially random whether sampled points in a thin layer at the surface of the torus, containing on the order of $N ^ { 2 / 3 }$ points, come out to be inside or outside the torus. The square root law, applied to this thin layer, gives $N ^ { 1 / 3 }$ fluctuations in the sum, or $N ^ { - 2 / 3 }$ fractional error in the Monte Carlo integral. One sees this behavior verified in Figure 7.8.2 by the thicker gray curve. The thicker dashed curve in Figure 7.8.2 is the result of integrating the function of equation (7.8.7) using independent random points. While the advantage of the Sobol’ sequence is not quite so dramatic as in the case of a smooth function, it can nonetheless be a significant factor $( \sim 5 )$ even at modest accuracies like $1 \%$ , and greater at higher accuracies.

![](images/ab6ac918e3ca3d9f0f7f1d88dbbde807a46cf59e93cfc4ae88245f43edc80ccd.jpg)  
Figure 7.8.2. Fractional accuracy of Monte Carlo integrations as a function of number of points sampled, for two different integrands and two different methods of choosing random points. The quasi-random Sobol’ sequence converges much more rapidly than a conventional pseudo-random sequence. Quasirandom sampling does better when the integrand is smooth (“soft boundary”) than when it has step discontinuities (“hard boundary”). The curves shown are the r.m.s. averages of 100 trials.

Note that we have not provided the routine sobseq with a means of starting the sequence at a point other than the beginning, but this feature would be easy to add. Once the initialization of the direction numbers iv has been done, the $j$ th point can be obtained directly by XORing together those direction numbers corresponding to nonzero bits in the Gray code of $j$ , as described above.

# 7.8.1 The Latin Hypercube

We mention here the unrelated technique of Latin square or Latin hypercube sampling, which is useful when you must sample an $N$ -dimensional space exceedingly sparsely, at $M$ points. For example, you may want to test the crashworthiness of cars as a simultaneous function of four different design parameters, but with a budget of only three expendable cars. (The issue is not whether this is a good plan — it isn’t — but rather how to make the best of the situation!)

The idea is to partition each design parameter (dimension) into $M$ segments, so that the whole space is partitioned into $\mathbf { \Phi } _ { M ^ { N } }$ cells. (You can choose the segments in each dimension to be equal or unequal, according to taste.) With four parameters and three cars, for example, you end up with $3 \times 3 \times 3 \times 3 = 8 1$ cells.

Next, choose $M$ cells to contain the sample points by the following algorithm: Randomly choose one of the $M ^ { N }$ cells for the first point. Now eliminate all cells that agree with this point on any of its parameters (that is, cross out all cells in the same row, column, etc.), leaving $( M - 1 ) ^ { N }$ candidates. Randomly choose one of these, eliminate new rows and columns, and continue the process until there is only one cell left, which then contains the final sample point.

The result of this construction is that each design parameter will have been tested in every one of its subranges. If the response of the system under test is dominated by one of the design parameters (the main effect), that parameter will be found with this sampling technique. On the other hand, if there are important interaction effects among different design parameters, then the Latin hypercube gives no particular advantage. Use with care.

There is a large field in statistics that deals with design of experiments. A brief pedagogical introduction is [5].

# CITED REFERENCES AND FURTHER READING:

Halton, J.H. 1960, “On the Efficiency of Certain Quasi-Random Sequences of Points in Evaluating Multi-dimensional Integrals,” Numerische Mathematik, vol. 2, pp. 84–90.[1]   
Bratley P., and Fox, B.L. 1988, “Implementing Sobol’s Quasirandom Sequence Generator,” ACM Transactions on Mathematical Software, vol.14, pp. 88-100.[2]   
Lambert, J.P. 1988, “Quasi-Random Sequences in Numerical Practice,” in Numerical Mathematics— Singapore 1988, ISNM vol.86,R.P.Agarwal, Y.M. Chow,and S.J.Wilson,eds. (Basel: Birkhäuser), pp. 273–284.   
Niederreiter, H. 1988, “Quasi-Monte Carlo Methods for Multidimensional Numerical Integration.” in Numerical Integration III, ISNM vol. 85, H. Brass and G. Hämmerlin, eds. (Basel: Birkhäuser), pp. 157–171.   
Sobol’, I.M. 1967, “On the Distribution of Points in a Cube and the Approximate Evaluation of Integrals,” USSR Computational Mathematics and Mathematical Physics, vol. 7, no. 4, pp. 86–112.[3]   
Antonov, I.A., and Saleev, V.M 1979, “An Economic Method of Computing $l p _ { t }$ Sequences,” USSR Computational Mathematics and Mathematical Physics,vol.19,no.1，pp.252- 256.[4]   
Dunn, O.J., and Clark, V.A. 1974, Applied Statistics: Analysis of Variance and Regression (New York, Wiley) [discusses Latin Square].   
Czitrom, V. 1999, “One-Factor-at-a-Time Versus Designed Experiments,” The American Statistician,vol.53,pp.126-131,online at http://www.amstat.org/publications/tas/ czitrom.pdf.[5]

# 7.9 Adaptive and Recursive Monte Carlo Methods

This section discusses more advanced techniques of Monte Carlo integration. As examples of the use of these techniques, we include two rather different, fairly sophisticated, multidimensional Monte Carlo codes: vegas [1,2], and miser [4]. The techniques that we discuss all fall under the general rubric of reduction of variance (-7.7), but are otherwise quite distinct.

# 7.9.1 Importance Sampling

The use of importance sampling was already implicit in equations (7.7.6) and (7.7.7). We now return to it in a slightly more formal way. Suppose that an integrand $f$ can be written as the product of a function $h$ that is almost constant times another, positive, function $g$ . Then its integral over a multidimensional volume $V$ is

$$
\int f d V = \int ( f / g ) g d V = \int h g d V
$$

In equation (7.7.7) we interpreted equation (7.9.1) as suggesting a change of variable to $G$ , the indefinite integral of $g$ . That made $g d V$ a perfect differential. We then proceeded to use the basic theorem of Monte Carlo integration, equation (7.7.1). A more general interpretation of equation (7.9.1) is that we can integrate $f$ by instead sampling $h$ — not, however, with uniform probability density $d V$ , but rather with nonuniform density $g d V$ . In this second interpretation, the first interpretation follows as the special case, where the means of generating the nonuniform sampling of $g d V$ is via the transformation method, using the indefinite integral $G$ (see $\ S 7 . 3$ ).

More directly, one can go back and generalize the basic theorem (7.7.1) to the case of nonuniform sampling: Suppose that points $x _ { i }$ are chosen within the volume $V$ with a probability density $p$ satisfying

$$
\int p d V = 1
$$

The generalized fundamental theorem is that the integral of any function $f$ is estimated, using $N$ sample points $x _ { 0 } , \ldots , x _ { N - 1 }$ , by

$$
I \equiv \int f d V = \int \frac { f } { p } p d V \approx \left. \frac { f } { p } \right. \pm \sqrt { \frac { \left. f ^ { 2 } / p ^ { 2 } \right. - \left. f / p \right. ^ { 2 } } { N } }
$$

where angle brackets denote arithmetic means over the $N$ points, exactly as in equation (7.7.2). As in equation (7.7.1), the “plus-or-minus” term is a one standard deviation error estimate. Notice that equation (7.7.1) is in fact the special case of equation (7.9.3), with $p = { \mathrm { c o n s t a n t } } =$ $1 / V$ .

What is the best choice for the sampling density $p \mathrm { ? }$ Intuitively, we have already seen that the idea is to make $h = f / p$ as close to constant as possible. We can be more rigorous by focusing on the numerator inside the square root in equation (7.9.3), which is the variance per sample point. Both angle brackets are themselves Monte Carlo estimators of integrals, so we can write

$$
S \equiv \left. { \frac { f ^ { 2 } } { p ^ { 2 } } } \right. - \left. { \frac { f } { p } } \right. ^ { 2 } \approx \int { \frac { f ^ { 2 } } { p ^ { 2 } } } p d V - \left[ \int { \frac { f } { p } } \ p d V \right] ^ { 2 } = \int { \frac { f ^ { 2 } } { p } } \ d V - \left[ \int f d V \right] ^ { 2 }
$$

We now find the optimal $p$ subject to the constraint equation (7.9.2) by the functional variation

$$
0 = { \frac { \delta } { \delta p } } \left( \int { \frac { f ^ { 2 } } { p } } d V - \left[ \int f d V \right] ^ { 2 } + \lambda \int p d V \right)
$$

with $\lambda$ a Lagrange multiplier. Note that the middle term does not depend on $p$ . The variation (which comes inside the integrals) gives $0 = - f ^ { 2 } / p ^ { 2 } + \lambda$ or

$$
p = { \frac { | f | } { \sqrt { \lambda } } } = { \frac { | f | } { \int | f | d V } }
$$

where $\lambda$ has been chosen to enforce the constraint (7.9.2).

If $f$ has one sign in the region of integration, then we get the obvious result that the optimal choice of $p$ — if one can figure out a practical way of effecting the sampling — is that it be proportional to $\mid f \mid$ . Then the variance is reduced to zero. Not so obvious, but seen

to be true, is the fact that $p \propto | f |$ is optimal even if $f$ takes on both signs. In that case the variance per sample point (from equations 7.9.4 and 7.9.6) is

$$
S = S _ { \mathrm { o p t i m a l } } = \left( \int | f | d V \right) ^ { 2 } - \left( \int f d V \right) ^ { 2 }
$$

One curiosity is that one can add a constant to the integrand to make it all of one sign, since this changes the integral by a known amount, constant $\times V$ . Then, the optimal choice of $\boldsymbol { p }$ always gives zero variance, that is, a perfectly accurate integral! The resolution of this seeming paradox (already mentioned at the end of $\ S 7 . 7 )$ is that perfect knowledge of $p$ in equation (7.9.6) requires perfect knowledge of $\textstyle \int | f | d V$ , which is tantamount to already knowing the integral you are trying to compute!

If your function $f$ takes on a known constant value in most of the volume $V$ , it is certainly a good idea to add a constant so as to make that value zero. Having done that, the accuracy attainable by importance sampling depends in practice not on how small equation (7.9.7) is, but rather on how small is equation (7.9.4) for an implementable $p$ , likely only a crude approximation to the ideal.

# 7.9.2 Stratified Sampling

The idea of stratified sampling is quite different from importance sampling. Let us expand our notation slightly and let $\langle \langle f \rangle \rangle$ denote the true average of the function $f$ over the volume $V$ (namely the integral divided by $V$ ), while $\langle f \rangle$ denotes as before the simplest (uniformly sampled) Monte Carlo estimator of that average:

$$
\langle \langle f \rangle \rangle \equiv { \frac { 1 } { V } } \int f d V \qquad \langle f \rangle \equiv { \frac { 1 } { N } } \sum _ { i } f ( x _ { i } )
$$

The variance of the estimator, $\operatorname { V a r } \left( \langle f \rangle \right)$ , which measures the square of the error of the Monte Carlo integration, is asymptotically related to the variance of the function, $\operatorname { V a r } \left( f \right) \equiv \langle \langle f ^ { 2 } \rangle \rangle -$ $\langle \langle f \rangle \rangle ^ { 2 }$ , by the relation

$$
\operatorname { V a r } \left( \langle f \rangle \right) = { \frac { \operatorname { V a r } \left( f \right) } { N } }
$$

(compare equation 7.7.1).

Suppose we divide the volume $V$ into two equal, disjoint subvolumes, denoted $a$ and $b$ , and sample $N / 2$ points in each subvolume. Then another estimator for $\langle \langle f \rangle \rangle$ , different from equation (7.9.8), which we denote $\langle f \rangle ^ { \prime }$ , is

$$
\begin{array} { r } { \langle f \rangle ^ { \prime } \equiv \frac { 1 } { 2 } ( \langle f \rangle _ { a } + \langle f \rangle _ { b } ) } \end{array}
$$

in other words, the mean of the sample averages in the two half-regions. The variance of estimator (7.9.10) is given by

$$
\begin{array} { r } { \mathrm { { V a r } } \left( \langle f \rangle ^ { \prime } \right) = \displaystyle \frac { 1 } { 4 } \left[ { \mathrm { V a r } } \left( \langle f \rangle _ { a } \right) + { \mathrm { V a r } } \left( \langle f \rangle _ { b } \right) \right] } \\ { = \displaystyle \frac { 1 } { 4 } \left[ \frac { { \mathrm { V a r } } _ { a } \left( f \right) } { N / 2 } + \frac { { \mathrm { V a r } } _ { b } \left( f \right) } { N / 2 } \right] } \\ { = \displaystyle \frac { 1 } { 2 N } \left[ { \mathrm { V a r } } _ { a } \left( f \right) + { \mathrm { V a r } } _ { b } \left( f \right) \right] } \end{array}
$$

Here $\operatorname { V a r } _ { a } \left( f \right)$ denotes the variance of $f$ in subregion $a$ , that is, $\langle \langle f ^ { 2 } \rangle \rangle _ { a } - \langle \langle f \rangle \rangle _ { a } ^ { 2 }$ , and correspondingly for $b$ .

From the definitions already given, it is not difficult to prove the relation

$$
\begin{array} { r } { \mathrm { { V a r } } \left( f \right) = \frac { 1 } { 2 } \left[ \mathrm { { V a r } } _ { a } \left( f \right) + { \mathrm { V a r } } _ { b } \left( f \right) \right] + \frac { 1 } { 4 } \left( \langle \langle f \rangle \rangle _ { a } - \langle \langle f \rangle \rangle _ { b } \right) ^ { 2 } } \end{array}
$$

(In physics, this formula for combining second moments is the “parallel axis theorem.”) Comparing equations (7.9.9), (7.9.11), and (7.9.12), one sees that the stratified (into two subvolumes) sampling gives a variance that is never larger than the simple Monte Carlo case — and smaller whenever the means of the stratified samples, $\langle \langle f \rangle \rangle _ { a }$ and $\langle \langle f \rangle \rangle _ { b }$ , are different.

We have not yet exploited the possibility of sampling the two subvolumes with different numbers of points, say $N _ { a }$ in subregion $a$ and $N _ { b } \equiv N - N _ { a }$ in subregion $b$ . Let us do so now. Then the variance of the estimator is

$$
\mathrm { { V a r } } \left( \left. f \right. ^ { \prime } \right) = \frac { 1 } { 4 } \left[ \frac { \mathrm { { V a r } } _ { a } \left( f \right) } { N _ { a } } + \frac { \mathrm { { V a r } } _ { b } \left( f \right) } { N - N _ { a } } \right]
$$

which is minimized (one can easily verify) when

$$
\frac { N _ { a } } { N } = \frac { \sigma _ { a } } { \sigma _ { a } + \sigma _ { b } }
$$

Here we have adopted the shorthand notation $\sigma _ { a } \equiv [ \mathrm { V a r } _ { a } \left( f \right) ] ^ { 1 / 2 }$ , and correspondingly for $b$ . If $N _ { a }$ satisfies equation (7.9.14), then equation (7.9.13) reduces to

$$
\mathrm { V a r } \left( \langle f \rangle ^ { \prime } \right) = \frac { ( \sigma _ { a } + \sigma _ { b } ) ^ { 2 } } { 4 N }
$$

Equation (7.9.15) reduces to equation (7.9.9) if $\operatorname { V a r } \left( f \right) = \operatorname { V a r } _ { a } \left( f \right) = \operatorname { V a r } _ { b } \left( f \right)$ , in which case stratifying the sample makes no difference.

A standard way to generalize the above result is to consider the volume $V$ divided into more than two equal subregions. One can readily obtain the result that the optimal allocation of sample points among the regions is to have the number of points in each region $j$ proportional to $\sigma _ { j }$ (that is, the square root of the variance of the function $f$ in that subregion). In spaces of high dimensionality (say $d \gtrsim 4 ,$ this is not in practice very useful, however. Dividing a volume into $K$ segments along each dimension implies $K ^ { d }$ subvolumes, typically much too large a number when one contemplates estimating all the corresponding $\sigma _ { j }$ ’s.

# 7.9.3 Mixed Strategies

Importance sampling and stratified sampling seem, at first sight, inconsistent with each other. The former concentrates sample points where the magnitude of the integrand $\mid f \mid$ is largest, the latter where the variance of $f$ is largest. How can both be right?

The answer is that (like so much else in life) it all depends on what you know and how well you know it. Importance sampling depends on already knowing some approximation to your integral, so that you are able to generate random points $x _ { i }$ with the desired probability density $p$ . To the extent that your $p$ is not ideal, you are left with an error that decreases only as $N ^ { - 1 / 2 }$ . Things are particularly bad if your $p$ is far from ideal in a region where the integrand $f$ is changing rapidly, since then the sampled function $h = f / p$ will have a large variance. Importance sampling works by smoothing the values of the sampled function $h$ and is effective only to the extent that you succeed in this.

Stratified sampling, by contrast, does not necessarily require that you know anything about $f$ . Stratified sampling works by smoothing out the fluctuations of the number of points in subregions, not by smoothing the values of the points. The simplest stratified strategy, dividing $V$ into $N$ equal subregions and choosing one point randomly in each subregion, already gives a method whose error decreases asymptotically as $N ^ { - 1 }$ , much faster than $N ^ { - 1 / 2 }$ . (Note that quasi-random numbers, $\ S 7 . 8$ , are another way of smoothing fluctuations in the density of points, giving nearly as good a result as the “blind” stratification strategy.)

However, “asymptotically” is an important caveat: For example, if the integrand is negligible in all but a single subregion, then the resulting one-sample integration is all but useless. Information, even very crude, allowing importance sampling to put many points in the active subregion would be much better than blind stratified sampling.

Stratified sampling really comes into its own if you have some way of estimating the variances, so that you can put unequal numbers of points in different subregions, according to (7.9.14) or its generalizations, and if you can find a way of dividing a region into a practical number of subregions (notably not $K ^ { d }$ with large dimension $d$ ), while yet significantly reducing the variance of the function in each subregion compared to its variance in the full volume. Doing this requires a lot of knowledge about $f$ , though different knowledge from what is required for importance sampling.

In practice, importance sampling and stratified sampling are not incompatible. In many, if not most, cases of interest, the integrand $f$ is small everywhere in $V$ except for a small fractional volume of “active regions.” In these regions the magnitude of $\mid f \mid$ and the standard deviation $\sigma = [ \mathrm { V a r } \left( f \right) ] ^ { 1 / 2 }$ are comparable in size, so both techniques will give about the same concentration of points. In more sophisticated implementations, it is also possible to “nest” the two techniques, so that, e.g., importance sampling on a crude grid is followed by stratification within each grid cell.

# 7.9.4 Adaptive Monte Carlo: VEGAS

The VEGAS algorithm, invented by Peter Lepage [1,2], is widely used for multidimensional integrals that occur in elementary particle physics. VEGAS is primarily based on importance sampling, but it also does some stratified sampling if the dimension $d$ is small enough to avoid $K ^ { d }$ explosion (specifically, if $( K / 2 ) ^ { d } < N / 2$ , with $N$ the number of sample points). The basic technique for importance sampling in VEGAS is to construct, adaptively, a multidimensional weight function $g$ that is separable,

$$
p \propto g ( x , y , z , \ldots ) = g _ { x } ( x ) g _ { y } ( y ) g _ { z } ( z ) \ldots
$$

Such a function avoids the $K ^ { d }$ explosion in two ways: (i) It can be stored in the computer as $d$ separate one-dimensional functions, each defined by $K$ tabulated values, say — so that $K \times d$ replaces $K ^ { d }$ . (ii) It can be sampled as a probability density by consecutively sampling the $d$ one-dimensional functions to obtain coordinate vector components $( x , y , z , \ldots )$ .

The optimal separable weight function can be shown to be [1]

$$
g _ { x } ( x ) \propto \left[ \int d y \int d z \ldots \frac { f ^ { 2 } ( x , y , z , \ldots ) } { g _ { y } ( y ) g _ { z } ( z ) \ldots } \right] ^ { 1 / 2 }
$$

(and correspondingly for $y , z , \ldots )$ . Notice that this reduces to $g \propto | f |$ (7.9.6) in one dimension. Equation (7.9.17) immediately suggests VEGAS’ adaptive strategy: Given a set of $g$ -functions (initially all constant, say), one samples the function $f$ , accumulating not only the overall estimator of the integral, but also the $K d$ estimators ( $K$ subdivisions of the independent variable in each of $d$ dimensions) of the right-hand side of equation (7.9.17). These then determine improved $g$ functions for the next iteration.

When the integrand $f$ is concentrated in one, or at most a few, regions in $d$ -space, then the weight function $g$ ’s quickly become large at coordinate values that are the projections of these regions onto the coordinate axes. The accuracy of the Monte Carlo integration is then enormously enhanced over what simple Monte Carlo would give.

The weakness of VEGAS is the obvious one: To the extent that the projection of the function $f$ onto individual coordinate directions is uniform, VEGAS gives no concentration of sample points in those dimensions. The worst case for VEGAS, e.g., is an integrand that is concentrated close to a body diagonal line, e.g., one from $( 0 , 0 , 0 , \ldots )$ to $( 1 , 1 , 1 , \ldots )$ . Since this geometry is completely nonseparable, VEGAS can give no advantage at all. More generally, VEGAS may not do well when the integrand is concentrated in one-dimensional (or higher) curved trajectories (or hypersurfaces), unless these happen to be oriented close to the coordinate directions.

The routine vegas that follows is essentially Lepage’s standard version, minimally modified to conform to our conventions. (We thank Lepage for permission to reproduce the program here.) For consistency with other versions of the VEGAS algorithm in circulation, we have preserved original variable names. The parameter NDMX is what we have called $K$ , the maximum number of increments along each axis; MXDIM is the maximum value of $d$ ; some other parameters are explained in the comments.

The vegas routine performs $m = \mathtt { i } \mathtt { t m x }$ statistically independent evaluations of the desired integral, each with $N = \mathtt { n c a l 1 }$ function evaluations. While statistically independent, these iterations do assist each other, since each one is used to refine the sampling grid for the next one. The results of all iterations are combined into a single best answer, and its estimated error, by the relations

$$
I _ { \mathrm { b e s t } } = \sum _ { i = 0 } ^ { m - 1 } \frac { I _ { i } } { \sigma _ { i } ^ { 2 } } \bigg / \sum _ { i = 0 } ^ { m - 1 } \frac { 1 } { \sigma _ { i } ^ { 2 } } \qquad \sigma _ { \mathrm { b e s t } } = \left( \sum _ { i = 0 } ^ { m - 1 } \frac { 1 } { \sigma _ { i } ^ { 2 } } \right) ^ { - 1 / 2 }
$$

Also returned is the quantity

$$
\chi ^ { 2 } / m \equiv \frac { 1 } { m - 1 } \sum _ { i = 0 } ^ { m - 1 } \frac { ( I _ { i } - I _ { \mathrm { b e s t } } ) ^ { 2 } } { \sigma _ { i } ^ { 2 } }
$$

If this is significantly larger than 1, then the results of the iterations are statistically inconsistent, and the answers are suspect.

Here is the interface to vegas. (The full code is given in [3].)

void vegas(VecDoub_I &regn, Doub fxn(VecDoub_I &, const Doub), const Int init, const Int ncall, const Int itmx, const Int nprn, Doub &tgral, Doub &sd, Doub &chi2a) {

Performs Monte Carlo integration of a user-supplied ndim-dimensional function fxn over a rectangular volume specified by regn[0..2\*ndim-1], a vector consisting of ndim “lower left” coordinates of the region followed by ndim “upper right” coordinates. The integration consists of itmx iterations, each with approximately ncall calls to the function. After each iteration the grid is refined; more than 5 or 10 iterations are rarely useful. The input flag init signals whether this call is a new start or a subsequent call for additional iterations (see comments in the code). The input flag nprn (normally 0) controls the amount of diagnostic output. Returned answers are tgral (the best estimate of the integral), sd (its standard deviation), and chi2a $\cdot x ^ { 2 }$ per degree of freedom, an indicator of whether consistent results are being obtained). See text for further details.

The input flag init can be used to advantage. One might have a call with init $\scriptstyle = 0$ , ncall $\mathtt { . } 0 0 0$ , itmx $\mathtt { . = 5 }$ immediately followed by a call with init $= 1$ , ncal $\mathtt { L } = 1 0 0 0 0 0$ , itmx $^ { = 1 }$ . The effect would be to develop a sampling grid over five iterations of a small number of samples, then to do a single high accuracy integration on the optimized grid.

To use vegas for the torus example discussed in $\ S 7 . 7$ (the density integrand only, say), the function fxn would be

Doub torusfunc(const VecDoub &x, const Doub wgt) { Doub den $=$ exp(5.\*x[2]); if (SQR(x[2]) $^ +$ SQR(sqrt(SQR(x[0])+SQR(x[1]))-3.) <= 1.) return den; else return 0.;   
}

#

and the main code would be

Doub tgral, sd, chi2a;   
VecDoub regn(6);   
regn[0] $\mathit { \Theta } = \mathit { \Theta } 1 \cdot$ ; regn[3] $\mathit { \Theta } = \mathit { \Theta } 4 , \mathit { \Theta } ;$ regn[1] $=$ -3.; regn[4] $= ~ 4 .$ ;   
regn[2] $\ c = - 1$ .; regn[5] $\smash { = ~ 1 , }$ ;   
vegas(regn,torusfunc,0,10000,10,0,tgral,sd,chi2a);   
vegas(regn,torusfunc,1,900000,1,0,tgral,sd,chi2a);

Note that the user-supplied integrand function, fxn, has an argument wgt in addition to the expected evaluation point $\mathbf { x }$ . In most applications you ignore wgt inside the function. Occasionally, however, you may want to integrate some additional function or functions along with the principal function $f$ . The integral of any such function $g$ can be estimated by

$$
I _ { g } = \sum _ { i } w _ { i } g ( \mathbf { x } )
$$

where the $w _ { i }$ ’s and $\mathbf { X }$ ’s are the arguments wgt and $\mathtt { x }$ , respectively. It is straightforward to accumulate this sum inside your function $\tt f x n$ and to pass the answer back to your main program via global variables. Of course, $g ( \mathbf { x } )$ had better resemble the principal function $f$ to some degree, since the sampling will be optimized for $f$ .

The full listing of vegas is given in a Webnote [3].

# 7.9.5 Recursive Stratified Sampling

The problem with stratified sampling, we have seen, is that it may not avoid the $K ^ { d }$ explosion inherent in the obvious, Cartesian, tessellation of a $d$ -dimensional volume. A technique called recursive stratified sampling [4] attempts to do this by successive bisections of a volume, not along all $d$ dimensions, but rather along only one dimension at a time. The starting points are equations (7.9.10) and (7.9.13), applied to bisections of successively smaller subregions.

Suppose that we have a quota of $N$ evaluations of the function $f$ and want to evaluate $\langle f \rangle ^ { \prime }$ in the rectangular parallelepiped region $R = ( { \bf x } _ { a } , { \bf x } _ { b } )$ . (We denote such a region by the two coordinate vectors of its diagonally opposite corners.) First, we allocate a fraction $\boldsymbol { p }$ of $N$ toward exploring the variance of $f$ in $R$ : We sample $p N$ function values uniformly in $R$ and accumulate the sums that will give the $d$ different pairs of variances corresponding to the $d$ different coordinate directions along which $R$ can be bisected. In other words, in $p N$ samples, we estimate $\operatorname { V a r } \left( f \right)$ in each of the regions resulting from a possible bisection of $R$ ,

$$
\begin{array} { r l } & { R _ { a i } \equiv ( \mathbf { x } _ { a } , \mathbf { x } _ { b } - \frac { 1 } { 2 } \mathbf { e } _ { i } \cdot ( \mathbf { x } _ { b } - \mathbf { x } _ { a } ) \mathbf { e } _ { i } ) } \\ & { R _ { b i } \equiv ( \mathbf { x } _ { a } + \frac { 1 } { 2 } \mathbf { e } _ { i } \cdot ( \mathbf { x } _ { b } - \mathbf { x } _ { a } ) \mathbf { e } _ { i } , \mathbf { x } _ { b } ) } \end{array}
$$

Here $\mathbf { e } _ { i }$ is the unit vector in the $i$ th coordinate direction, $i = 1 , 2 , \ldots , d$ .

Second, we inspect the variances to find the most favorable dimension $i$ to bisect. By equation (7.9.15), we could, for example, choose that $i$ for which the sum of the square roots of the variance estimators in regions $R _ { a i }$ and $R _ { b i }$ is minimized. (Actually, as we will explain, we do something slightly different.)

Third, we allocate the remaining $( 1 - p ) N$ function evaluations between the regions $R _ { a i }$ and $R _ { b i }$ . If we used equation (7.9.15) to choose $i$ , we should do this allocation according to equation (7.9.14).

We now have two parallelepipeds, each with its own allocation of function evaluations for estimating the mean of $f$ . Our “RSS” algorithm now shows itself to be recursive: To evaluate the mean in each region, we go back to the sentence beginning “First,...” in the paragraph above equation (7.9.21). (Of course, when the allocation of points to a region falls below some number, we resort to simple Monte Carlo rather than continue with the recursion.)

Finally, we combine the means and also estimated variances of the two subvolumes using equation (7.9.10) and the first line of equation (7.9.11).

This completes the RSS algorithm in its simplest form. Before we describe some additional tricks under the general rubric of “implementation details,” we need to return briefly to equations $( 7 . 9 . 1 3 ) - ( 7 . 9 . 1 5 )$ and derive the equations that we actually use instead of these. The right-hand side of equation (7.9.13) applies the familiar scaling law of equation (7.9.9) twice, once to $a$ and again to $b$ . This would be correct if the estimates $\langle f \rangle _ { a }$ and $\langle f \rangle _ { b }$ were each made by simple Monte Carlo, with uniformly random sample points. However, the two estimates of the mean are in fact made recursively. Thus, there is no reason to expect equation (7.9.9) to hold. Rather, we might substitute for equation (7.9.13) the relation,

$$
\operatorname { V a r } \left( \langle f \rangle ^ { \prime } \right) = \frac { 1 } { 4 } \left[ \frac { \operatorname { V a r } _ { a } { \left( f \right) } } { N _ { a } ^ { \alpha } } + \frac { \operatorname { V a r } _ { b } { \left( f \right) } } { ( N - N _ { a } ) ^ { \alpha } } \right]
$$

where $\alpha$ is an unknown constant $\geq 1$ (the case of equality corresponding to simple Monte Carlo). In that case, a short calculation shows that $\mathrm { V a r } \overset { \cdot } { ( } \langle f \rangle ^ { \prime } )$ is minimized when

$$
\frac { N _ { a } } { N } = \frac { \mathrm { V a r } _ { a } \left( f \right) ^ { 1 / \left( 1 + \alpha \right) } } { \mathrm { V a r } _ { a } \left( f \right) ^ { 1 / \left( 1 + \alpha \right) } + \mathrm { V a r } _ { b } \left( f \right) ^ { 1 / \left( 1 + \alpha \right) } }
$$

and that its minimum value is

$$
\begin{array} { r } { \mathrm { V a r } \left( \langle f \rangle ^ { \prime } \right) \propto \left[ \mathrm { V a r } _ { a } \left( f \right) ^ { 1 / ( 1 + \alpha ) } + \mathrm { V a r } _ { b } \left( f \right) ^ { 1 / ( 1 + \alpha ) } \right] ^ { 1 + \alpha } } \end{array}
$$

Equations $( 7 . 9 . 2 2 ) - ( 7 . 9 . 2 4 )$ reduce to equations $( 7 . 9 . 1 3 ) - ( 7 . 9 . 1 5 )$ when $\alpha = 1$ . Numerical experiments to find a self-consistent value for $\alpha$ find that $\alpha \approx 2$ . That is, when equation (7.9.23) with $\alpha = 2$ is used recursively to allocate sample opportunities, the observed variance of the RSS algorithm goes approximately as $N ^ { - 2 }$ , while any other value of $\alpha$ in equation (7.9.23) gives a poorer fall-off. (The sensitivity to $\alpha$ is, however, not very great; it is not known whether $\alpha = 2$ is an analytically justifiable result or only a useful heuristic.)

The principal difference between miser’s implementation and the algorithm as described thus far lies in how the variances on the right-hand side of equation (7.9.23) are estimated. We find empirically that it is somewhat more robust to use the square of the difference of maximum and minimum sampled function values, instead of the genuine second moment of the samples. This estimator is of course increasingly biased with increasing sample size; however, equation (7.9.23) uses it only to compare two subvolumes $a$ and $b$ ) having approximately equal numbers of samples. The “max minus min” estimator proves its worth when the preliminary sampling yields only a single point, or a small number of points, in active regions of the integrand. In many realistic cases, these are indicators of nearby regions of even greater importance, and it is useful to let them attract the greater sampling weight that “max minus min” provides.

A second modification embodied in the code is the introduction of a “dithering parameter,” dith, whose nonzero value causes subvolumes to be divided not exactly down the middle, but rather into fractions $0 . 5 \pm$ dith, with the sign of the $\pm$ randomly chosen by a built-in random number routine. Normally dith can be set to zero. However, there is a large advantage in taking dith to be nonzero if some special symmetry of the integrand puts the active region exactly at the midpoint of the region, or at the center of some power-of-two submultiple of the region. One wants to avoid the extreme case of the active region being evenly divided into $2 ^ { d }$ abutting corners of a $d$ -dimensional space. A typical nonzero value of dith, on those occasions when it is useful, might be 0:1. Of course, when the dithering parameter is nonzero, we must take the differing sizes of the subvolumes into account; the code does this through the variable fracl.

One final feature in the code deserves mention. The RSS algorithm uses a single set of sample points to evaluate equation (7.9.23) in all $d$ directions. At the bottom levels of the recursion, the number of sample points can be quite small. Although rare, it can happen that in one direction all the samples are in one half of the volume; in that case, that direction is ignored as a candidate for bifurcation. Even more rare is the possibility that all of the samples are in one half of the volume in all directions. In this case, a random direction is chosen. If this happens too often in your application, then you should increase MNPT (see line if $( \mathrm { j } \mathsf { b } \ = \ - 1 ) \ldots$ in the code).

Note that miser, as given, returns as ave an estimate of the average function value $\langle \langle f \rangle \rangle$ , not the integral of $f$ over the region. The routine vegas, adopting the other convention, returns as tgral the integral. The two conventions are of course trivially related, by equation (7.9.8), since the volume $V$ of the rectangular region is known.

The interface to the miser routine is this:

# void miser(Doub func(VecDoub_I &), VecDoub_I &regn, const Int npts, const Doub dith, Doub &ave, Doub &var) {

Monte Carlo samples a user-supplied ndim-dimensional function func in a rectangular volume specified by regn[0..2\*ndim-1], a vector consisting of ndim “lower-left” coordinates of the region followed by ndim “upper-right” coordinates. The function is sampled a total of npts times, at locations determined by the method of recursive stratified sampling. The mean value of the function in the region is returned as ave; an estimate of the statistical uncertainty of ave (square of standard deviation) is returned as var. The input parameter dith should normally be set to zero, but can be set to (e.g.) 0.1 if func’s active region falls on the boundary of a power-of-two subdivision of region.

Implementing code for the torus problem in $\ S 7 . 7$ is

Doub torusfunc(const VecDoub &x) {Doub den $=$ exp(5.\*x[2]);if (SQR(x[2]) $^ +$ SQR(sqrt(SQR(x[0])+SQR(x[1]))-3.) $< = ~ 1 .$ ) return den;else return 0.;  
}

and the main code is

Doub ave, var, tgral, sd, vol = 3.\*7.\*2.;   
regn[0] $\begin{array} { r l } { \mathbf { \Phi } } & { { } = \mathbf { \Phi } _ { 1 } \qquad } \end{array}$ ; regn[3] $= ~ 4 .$ ;   
regn[1] $=$ -3.; regn[4] $\mathit { \Theta } = \mathit { \Theta } 4 .$ ;   
regn[2] $\ c = - 1$ .; regn[5] $\mathit { \Theta } = \mathit { \Theta } 1 \cdot$ ;   
miser(torusfunc,regn,1000000,0.,ave,var);   
tgral $=$ ave\*vol;   
sd $=$ sqrt(var)\*vol;

(Actually, miser is not particularly well-suited to this problem.)

The complete listing of miser is given in a Webnote [5]. The miser routine calls the short function ranpt to get a random point within a specified $d$ -dimensional region. The version of ranpt in the Webnote makes consecutive calls to a uniform random number generator and does the obvious scaling. One can easily modify ranpt to generate its points via the quasi-random routine sobseq $( \ S 7 . 8 )$ . We find that miser with sobseq can be considerably more accurate than miser with uniform random deviates. Since the use of RSS and the use of quasi-random numbers are completely separable, however, we have not made the code given here dependent on sobseq. A similar remark might be made regarding importance sampling, which could in principle be combined with RSS. (One could in principle combine vegas and miser, although the programming would be intricate.)

# CITED REFERENCES AND FURTHER READING:

Hammersley, J.M. and Handscomb, D.C. 1964, Monte Carlo Methods (London: Methuen).   
Kalos, M.H. and Whitlock, P.A. 1986, Monte Carlo Methods (New York: Wiley).   
Bratley, P., Fox, B.L., and Schrage, E.L. 1983, A Guide to Simulation, 2nd ed. (New York: Springer).   
Lepage, G.P. 1978, “A New Algorithm for Adaptive Multidimensional Integration,” Journal of Computational Physics,vol. 27,pp.192-203.[1]   
Lepage, G.P. 1980, “VEGAS: An Adaptive Multidimensional Integration Program,” Publication CLNS-80/447, Cornell University.[2]   
Numerical Recipes Software 2007, “Complete VEGAS Code Listing,” Numerical Recipes Webnote No.9,at http://www.nr.com/webnotes?9 [3]   
Press, W.H., and Farrar, G.R. 1990, “Recursive Stratified Sampling for Multidimensional Monte Carlo Integration,” Computers in Physics, vol. 4, pp. 190–195.[4]   
Numerical Recipes Software 2007, “Complete Miser Code Listing,” Numerical Recipes Webnote No.10,athttp://www.nr.com/webnotes?10 [5]

# 8.0 Introduction

This chapter almost doesn’t belong in a book on numerical methods: Sorting and selection are bread-and-butter topics in the standard computer science curriculum. However, some review of the techniques for sorting, from the perspective of scientific computing, will prove useful in subsequent chapters. We can develop some standard interfaces for later use, and also illustrate the usefulness of templates in object-oriented programming.

In conjunction with numerical work, sorting is frequently necessary when data (either experimental or numerically generated) are being processed. One has tables or lists of numbers, representing one or more independent (or control) variables, and one or more dependent (or measured) variables. One may wish to arrange these data, in various circumstances, in order by one or another of these variables. Alternatively, one may simply wish to identify the median value or the upper quartile value of one of the lists of values. (These kinds of values are generically called quantiles.) This task, closely related to sorting, is called selection.

Here, more specifically, are the tasks that this chapter will deal with:

- Sort, i.e., rearrange, an array of numbers into numerical order.   
- Rearrange an array into numerical order while performing the corresponding rearrangement of one or more additional arrays, so that the correspondence between elements in all arrays is maintained.   
Given an array, prepare an index table for it, i.e., a table of pointers telling which number array element comes first in numerical order, which second, and so on.   
- Given an array, prepare a rank table for it, i.e., a table telling what is the numerical rank of the first array element, the second array element, and so on.   
- Select the $M$ th largest element from an array.   
- Select the $M$ th largest value, or estimate arbitrary quantile values, from a data stream in one pass (i.e., without storing the stream for later processing).   
- Given a bunch of equivalence relations, organize them into equivalence classes.

For the basic task of sorting $N$ elements, the best algorithms require on the order of several times $N \log _ { 2 } N$ operations. The algorithm inventor tries to reduce the constant in front of this estimate to as small a value as possible. Two of the best algorithms are Quicksort (-8.2), invented by the inimitable C.A.R. Hoare, and Heapsort (-8.3), invented by J.W.J. Williams.

For large $N$ $\mathrm { \Delta \left( s a y \right) > \Delta 1 0 0 0 }$ ), Quicksort is faster, on most machines, by a factor of 1.5 or 2; it requires a bit of extra memory, however, and is a moderately complicated program. Heapsort is a true “sort in place,” and is somewhat more compact to program and therefore a bit easier to modify for special purposes. On balance, we recommend Quicksort because of its speed, but we implement both routines.

For small $N$ one does better to use an algorithm whose operation count goes as a higher, i.e., poorer, power of $N$ , if the constant in front is small enough. For $N < 2 0$ , roughly, the method of straight insertion (-8.1) is concise and fast enough. We include it with some trepidation: It is an $N ^ { 2 }$ algorithm, whose potential for misuse (by using it for too large an $N$ ) is great. The resultant waste of computer resource can be so awesome that we were tempted not to include any $N ^ { 2 }$ routine at all. We will draw the line, however, at the inefficient $N ^ { 2 }$ algorithm, beloved of elementary computer science texts, called bubble sort. If you know what bubble sort is, wipe it from your mind; if you don’t know, make a point of never finding out!

For $N < 5 0$ , roughly, Shell’s method (-8.1), only slightly more complicated to program than straight insertion, is competitive with the more complicated Quicksort on many machines. This method goes as $N ^ { 3 / 2 }$ in the worst case, but is usually faster.

See Refs. [1,2] for further information on the subject of sorting, and for detailed references to the literature.

# CITED REFERENCES AND FURTHER READING:

Knuth, D.E. 1997, Sorting and Searching, 3rd ed., vol. 3 of The Art of Computer Programming (Reading, MA: Addison-Wesley).[1]   
Sedgewick, R. 1998, Algorithms in C, 3rd ed. (Reading, MA: Addison-Wesley), Chapters 8– 13.[2]

# 8.1 Straight Insertion and Shell's Method

Straight insertion is an $N ^ { 2 }$ routine and should be used only for small $N$ , say $< 2 0$ .

The technique is exactly the one used by experienced card players to sort their cards: Pick out the second card and put it in order with respect to the first; then pick out the third card and insert it into the sequence among the first two; and so on until the last card has been picked out and inserted.

# sort.h template<class T>

void piksrt(NRvector<T> &arr)

Sort an array arr[0..n-1] into ascending numerical order, by straight insertion. arr is replaced on output by its sorted rearrangement.

Int i,j,n=arr.size();   
T a;   
for (j=1;j<n;j++) { a=arr[j];

Pick out each element in turn.

i=j; while (i > 0 && arr[i-1] > a) { Look for the place to insert it. arr[i] $=$ arr[i-1]; i--; } arr[i] $= \mathtt { a }$ ; Insert it. } }

Notice the use of a template in order to make the routine general for any type of NRvector, including both VecInt and VecDoub. The only thing required of the elements of type T in the vector is that they have an assignment operator and a $>$ relation. (We will generally assume that the relations $< , >$ , and $= =$ all exist.) If you try to sort a vector of elements without these properties, the compiler will complain, so you can’t go wrong.

It is a matter of taste whether to template on the element type, as above, or on the vector itself, as

# template<class T> void piksrt(T &arr)

This would seem more general, since it will work for any type T that has a subscript operator [], not just NRvectors. However, it also requires that T have some method for getting at the type of its elements, necessary for the declaration of the variable a. If T follows the conventions of STL containers, then that declaration can be written

# T::value_type a;

but if it doesn’t, then you can find yourself lost at C.

What if you also want to rearrange an array brr at the same time as you sort arr? Simply move an element of brr whenever you move an element of arr:

template<class T, class U>   
void piksr2(NRvector<T> &arr, NRvector<U> &brr)   
Sort an array arr[0..n-1] into ascending numerical order, by straight insertion, while making the corresponding rearrangement of the array brr[0..n-1].

Int i,j,n=arr.size(); T a; U b; for (j=1;j<n;j++) { Pick out each element in turn. a=arr[j]; b=brr[j]; i=j; while (i > 0 && arr[i-1] > a) { Look for the place to insert it. arr[i] $=$ arr[i-1]; brr[i] $=$ brr[i-1]; i--; } arr[i] $= a$ ; Insert it. brr[i] $= \mathrm { b }$ ; } }

Note that the types of arr and brr are separately templated, so they don’t have to be the same.

Don’t generalize this technique to the rearrangement of a larger number of arrays by sorting on one of them. Instead see $\ S 8 . 4$ .

# 8.1.1 Shell's Method

This is actually a variant on straight insertion, but a very powerful variant indeed. The rough idea, e.g., for the case of sorting 16 numbers $n _ { 0 } \ldots n _ { 1 5 }$ , is this: First sort, by straight insertion, each of the 8 groups of 2 $( n _ { 0 } , n _ { 8 } )$ , $( n _ { 1 } , n _ { 9 } )$ , . . . , $( n _ { 7 } , n _ { 1 5 } )$ . Next, sort each of the 4 groups of 4 $( n _ { 0 } , n _ { 4 } , n _ { 8 } , n _ { 1 2 } )$ , . . . , $( n _ { 3 } , n _ { 7 } , n _ { 1 1 } , n _ { 1 5 } )$ . Next sort the 2 groups of 8 records, beginning with $\left( n _ { 0 } , n _ { 2 } , n _ { 4 } , n _ { 6 } , n _ { 8 } , n _ { 1 0 } , n _ { 1 2 } , n _ { 1 4 } \right)$ . Finally, sort the whole list of 16 numbers.

Of course, only the last sort is necessary for putting the numbers into order. So what is the purpose of the previous partial sorts? The answer is that the previous sorts allow numbers efficiently to filter up or down to positions close to their final resting places. Therefore, the straight insertion passes on the final sort rarely have to go past more than a “few” elements before finding the right place. (Think of sorting a hand of cards that are already almost in order.)

The spacings between the numbers sorted on each pass through the data (8,4,2,1 in the above example) are called the increments, and a Shell sort is sometimes called a diminishing increment sort. There has been a lot of research into how to choose a good set of increments, but the optimum choice is not known. The set $\ldots , 8 , 4 , 2 , 1$ is in fact not a good choice, especially for $N$ a power of 2. A much better choice is the sequence

$$
( 3 ^ { k } - 1 ) / 2 , \ldots , 4 0 , 1 3 , 4 , 1
$$

which can be generated by the recurrence

$$
i _ { 0 } = 1 , \qquad i _ { k + 1 } = 3 i _ { k } + 1 , \quad k = 0 , 1 , \ldots
$$

It can be shown (see [1]) that for this sequence of increments the number of operations required in all is of order $N ^ { 3 / 2 }$ for the worst possible ordering of the original data. For “randomly” ordered data, the operations count goes approximately as $N ^ { 1 . 2 5 }$ , at least for $N < 6 0 0 0 0$ . For $N > 5 0$ , however, Quicksort is generally faster.

# template<class T>

# void shell(NRvector<T> &a, Int $\mathrm { m } { = } { - } 1$ )

Sort an array a[0..n-1] into ascending numerical order by Shell’s method (diminishing increment sort). a is replaced on output by its sorted rearrangement. Normally, the optional argument m should be omitted, but if it is set to a positive value, then only the first m elements of a are sorted.

Use optional argument.   
Determine the starting increment.   
Int i,j,inc, $\scriptstyle , \mathtt { n } = \mathtt { a }$ .size();   
T v;   
if ( $\mathrm { . } \mathrm { m } { > } 0 \mathrm { . }$ ) $\mathrm { ~ n ~ } =$ MIN(m,n);   
inc=1;   
do { inc $\ast = ~ 3$ ; inc++;   
} while (inc $< = \mathrm { ~ n ~ } ,$ );   
do { inc /= 3; for ( $\dot { \bf 1 } =$ inc;i<n;i++) { $\mathtt { v } = \mathtt { a }$ [i]; $\scriptstyle { \dot { \mathsf { J } } } = { \dot { \mathsf { I } } }$ ; while (a[j-inc] > v) { a[j] $= \mathtt { a }$ [j-inc]; j $- =$ inc; if (j $<$ inc) break; }

Loop over the partial sorts.

Outer loop of straight insertion.

Inner loop of straight insertion.

a[j]=v; } } while (inc > 1);

# CITED REFERENCES AND FURTHER READING:

Knuth, D.E. 1997, Sorting and Searching, 3rd ed., vol. 3 of The Art of Computer Programming (Reading, MA: Addison-Wesley), $\ S 5$ .2.1.[1] Sedgewick, R. 1998, Algorithms in C, 3rd ed. (Reading, MA: Addison-Wesley), Chapter 8.

# 8.2 Quicksort

Quicksort is, on most machines, on average, for large $N$ , the fastest known sorting algorithm. It is a “partition-exchange” sorting method: A “partitioning element” a is selected from the array. Then, by pairwise exchanges of elements, the original array is partitioned into two subarrays. At the end of a round of partitioning, the element a is in its final place in the array. All elements in the left subarray are $\leq \mathsf { a }$ while all elements in the right subarray are $\geq \mathsf { a }$ . The process is then repeated on the left and right subarrays independently, and so on.

The partitioning process is carried out by selecting some element, say the leftmost, as the partitioning element a. Scan a pointer up the array until you find an element $> \mathtt { a }$ , and then scan another pointer down from the end of the array until you find an element $< \mathtt { a }$ . These two elements are clearly out of place for the final partitioned array, so exchange them. Continue this process until the pointers cross. This is the right place to insert a, and that round of partitioning is done. The question of the best strategy when an element is equal to the partitioning element is subtle; see Sedgewick [1] for a discussion. (Answer: You should stop and do an exchange.)

For speed of execution, we don’t implement Quicksort using recursion. Thus the algorithm requires an auxiliary array of storage, of length $2 \log _ { 2 } N$ , which it uses as a push-down stack for keeping track of the pending subarrays. When a subarray has gotten down to some size $M$ , it becomes faster to sort it by straight insertion (-8.1), so we will do this. The optimal setting of $M$ is machine-dependent, but $M \ = \ 7$ is not too far wrong. Some people advocate leaving the short subarrays unsorted until the end, and then doing one giant insertion sort at the end. Since each element moves at most seven places, this is just as efficient as doing the sorts immediately, and saves on the overhead. However, on modern machines with a cache hierarchy, there is increased overhead when dealing with a large array all at once. We have not found any advantage in saving the insertion sorts till the end.

As already mentioned, Quicksort’s average running time is fast, but its worst case running time can be very slow: For the worst case it is, in fact, an $N ^ { 2 }$ method! And for the most straightforward implementation of Quicksort it turns out that the worst case is achieved for an input array that is already in order! This ordering of the input array might easily occur in practice. One way to avoid this is to use a little random number generator to choose a random element as the partitioning element. Another is to use instead the median of the first, middle, and last elements of the current subarray.

The great speed of Quicksort comes from the simplicity and efficiency of its inner loop. Simply adding one unnecessary test (for example, a test that your pointer has not moved off the end of the array) can almost double the running time! One avoids such unnecessary tests by placing “sentinels” at either end of the subarray being partitioned. The leftmost sentinel is $\leq \mathsf { a }$ , the rightmost $\geq \mathsf { a }$ . With the “medianof-three” selection of a partitioning element, we can use the two elements that were not the median to be the sentinels for that subarray.

Our implementation closely follows [1]:

# sort.h template<class T>

# void sort(NRvector<T> &arr, Int $\mathrm { m } { = } { - } 1$

Sort an array ar $\mathbf { \texttt { c } } [ 0 \ldots \mathbf { \texttt { n } } ^ { - 1 } ]$ into ascending numerical order using the Quicksort algorithm. arr is replaced on output by its sorted rearrangement. Normally, the optional argument m should be omitted, but if it is set to a positive value, then only the first m elements of arr are sorted.

static const Int $\mathtt { M } = 7$ , NSTAC $_ { ; = 6 4 }$ ;   
Here M is the size of subarrays sorted by straight insertion and NSTACK is the required   
auxiliary storage.   
Int i,ir,j,k,jstack $= - 1$ , $\mathtt { 1 } = 0$ , $\mathbf { n } =$ arr.size();   
T a;   
VecInt istack(NSTACK);   
if $\mathrm { m } { > } 0 \mathrm { \Omega }$ ) $\mathrm { ~ n ~ } =$ MIN(m,n); Use optional argument.   
$\mathtt { i r } \mathtt { = n - 1 }$ ;   
for (;;) { Insertion sort when subarray small enough. if (ir-l < M) { for $( \mathrm { j } { = } 1 { + } 1$ ;j<=ir;j++) { a=arr[j]; for (i=j-1;i>=l;i--) { if (arr[i] $\texttt { \textbf { < } } \texttt { \textbf { a } }$ ) break; arr[i+1] $=$ arr[i]; } arr[i+1]=a; } if (jstack < 0) break; ir=istack[jstack--]; Pop stack and begin a new round of partil=istack[jstack--]; tioning. } else { $\mathtt { k } =$ (l+ir) >> 1; Choose median of left, center, and right el-SWAP(arr[k],arr[l+1]); ements as partitioning element a. Also if (arr[l] $>$ arr[ir]) { rearrange so that a $[ 1 ] \le \mathtt { a } [ 1 + 1 ] \le \mathtt { a } [ \mathtt { i r } ]$ . SWAP(arr[l],arr[ir]); } if (arr[l+1] $>$ arr[ir]) { SWAP(arr[l+1],arr[ir]); } if (arr[l] $>$ arr[l+1]) { SWAP(arr[l],arr[l+1]); } $\dot { \bf z } = \bf { 1 } + 1$ ; Initialize pointers for partitioning. $\scriptstyle { \dot { \mathcal { I } } } = { \dot { \mathtt { I } } } \mathtt { r }$ ; a=arr[l+1]; Partitioning element. for (;;) { Beginning of innermost loop. do $\dot { \bf 1 } + +$ ; while (arr[i] < a); Scan up to find element $> \mathtt { a }$ . do j--; while (arr[j] $>$ a); Scan down to find element $< \mathtt { a }$ . if (j < i) break; Pointers crossed. Partitioning complete. SWAP(arr[i],arr[j]); Exchange elements. } End of innermost loop. arr[l+1] $=$ arr[j]; Insert partitioning element. arr[j] $= _ { \mathrm { a } }$ ; jstack $+ = ~ 2$ ; Push pointers to larger subarray on stack; process smaller subarray immediately.

if (jstack $> =$ NSTACK) throw("NSTACK too small in sort."); if $( \mathrm { i } \mathbf { r } \mathbf { - } \mathrm { i } \mathbf { + } 1 > = \mathrm { ~ j \mathbf { - } \mathbf { 1 } ) ~ } .$ { istack[jstack] ${ \stackrel { } { = } } { \dot { \mathtt { 1 } } } \mathtt { r }$ ; istack[jstack-1] ${ \bf \Phi } = \dot { \bf 1 }$ ; ir=j-1; } else { istack[jstack] $= \dot { \jmath } - 1$ ; istack[jstack-1] ${ } = 1$ ; $\beth = \dot { \beth }$ ; } } } }

As usual, you can move any other arrays around at the same time as you sort arr. At the risk of being repetitious:

template<class T, class U>   
void sort2(NRvector<T> &arr, NRvector<U> &brr)   
Sort an array arr[0..n-1] into ascending order using Quicksort, while making the corresponding   
rearrangement of the array brr[0..n-1].   
{ const Int M=7,NSTACK $\mathop {    }$ 64; Int i,ir,j,k,jstack=-1, $\mathtt { 1 } = 0$ , $\mathbf { n } =$ arr.size(); T a; U b; VecInt istack(NSTACK); $\mathrm { i } \mathbf { r } { = } \mathbf { n } { - } 1$ ; for (;;) { Insertion sort when subarray small enough. if (ir-l < M) { for (j=l+1;j<=ir;j++) { $\mathtt { a } =$ arr[j]; $\mathtt { b } =$ brr[j]; for (i=j-1; $\mathrm { i } > = 1$ ;i--) { if (arr[i] $< = { \mathsf { a } } )$ break; arr[i+1] $=$ arr[i]; brr[i+1] $\stackrel { } { = }$ brr[i]; 1 arr[i+1] $= a$ ; brr[i+1]=b; } if (jstack < 0) break; ir=istack[jstack--]; Pop stack and begin a new round of partil=istack[jstack--]; tioning. } else { $\mathrm { k } =$ (l+ir) >> 1; Choose median of left, center, and right el-SWAP(arr[k],arr[l+1]); ements as partitioning element a. Also SWAP(brr[k],brr[l+1]); rearrange so that $\mathsf { a } [ 1 ] \leq \mathsf { a } [ 1 + 1 ] \leq \mathsf { a } [ \mathrm { i r } ]$ if (arr[l] $>$ arr[ir]) { SWAP(arr[l],arr[ir]); SWAP(brr[l],brr[ir]); if (arr[l+1] $>$ arr[ir]) { SWAP(arr[l+1],arr[ir]); SWAP(brr[l+1],brr[ir]); } if (arr[l] $>$ arr[l+1]) { SWAP(arr[l],arr[l+1]); SWAP(brr[l],brr[l+1]); } $\dot { \bar { 1 } } = 1 + 1$ ; Initialize pointers for partitioning. $\scriptstyle { \dot { \mathsf { J } } } = { \dot { \mathsf { 1 } } } { \boldsymbol { \mathbf { r } } }$ ; a=arr[l+1]; Partitioning element.

b=brr[l+1]; for (;;) { Beginning of innermost loop. do $\dot { \bf 1 } + +$ ; while (arr[i] < a); Scan up to find element $> \mathtt { a }$ . do j--; while (arr[j] $>$ a); Scan down to find element $< \mathtt { a }$ . if (j < i) break; Pointers crossed. Partitioning complete. SWAP(arr[i],arr[j]); Exchange elements of both arrays. SWAP(brr[i],brr[j]); End of innermost loop. arr[l+1] $=$ arr[j]; Insert partitioning element in both arrays. arr[j] $= \mathtt { a }$ ; brr[l+1] $=$ brr[j]; brr[j] $= \mathrm { b }$ ; jstack $+ = ~ 2$ ; Push pointers to larger subarray on stack; process smaller subarray immediately. if (jstack $> =$ NSTACK) throw("NSTACK too small in sort2."); if $( \mathrm { i } \mathbf { r } \mathbf { - } \mathrm { i } \mathbf { + } 1 \ \mathbf { > } \mathbf { = } \ \mathrm { j } \mathbf { - } \mathrm { 1 } )$ { istack[jstack] ${ \tt = } \tt { i r }$ ; istack[jstack-1] ${ \bf \Phi } = \dot { \bf 1 }$ ; $\scriptstyle { \mathrm { i } x = } { \mathrm { j } - 1 }$ ; } else { istack[jstack] $= \dot { ] } - 1$ ; istack[jstack-1] ${ = } 1$ ; $\mathbf { \vec { \tau } } _ { 1 } = \dot { \mathbf { \vec { \tau } } }$ ; } } } }

You could, in principle, rearrange any number of additional arrays along with brr, but this is inefficient if the number of such arrays is larger than one. The preferred technique is to make use of an index table, as described in $\ S 8 . 4$ .

# CITED REFERENCES AND FURTHER READING:

Sedgewick, R. 1978, “Implementing Quicksort Programs,” Communications of the ACM, vol. 21, pp. 847–857.[1]

# 8.3 Heapsort

Heapsort is slower than Quicksort by a constant factor. It is so beautiful that we sometimes use it anyway, just for the sheer joy of it. (However, we don’t recommend that you do this if your employer is paying for efficient code.) Heapsort is a true “in-place” sort, requiring no auxiliary storage. It is an $N \log _ { 2 } N$ algorithm, not only on average, but also for the worst case order of input data. In fact, its worst case is only $20 \%$ or so worse than its average running time.

It is beyond our scope to give a complete exposition on the theory of Heapsort. We mention the general principles, then refer you to the references [1,2]; or you can analyze the program yourself, if you want to understand the details.

A set of $N$ numbers $a _ { j }$ ; $j ~ = ~ 0 , \ldots , N - 1$ , is said to form a “heap” if it satisfies the relation

$$
a _ { ( j - 1 ) / 2 } \geq a _ { j } \quad \mathrm { f o r } \quad 0 \leq ( j - 1 ) / 2 < j < N
$$

![](images/b23bb47fdc7d0e2e655f99fb92916bbb84b3f89fb28b27bffbe3a3deafff18f1.jpg)  
Figure 8.3.1. Ordering implied by a “heap,” here of 12 elements. Elements connected by an upward path are sorted with respect to one another, but there is not necessarily any ordering among elements related only “laterally.”

Here the division in $j / 2$ means “integer divide,” i.e., is an exact integer or else is rounded down to the closest integer. Definition (8.3.1) will make sense if you think of the numbers $a _ { i }$ as being arranged in a binary tree, with the top, “boss,” node being $a _ { 0 }$ ; the two “underling” nodes being $a _ { 1 }$ and $a _ { 2 }$ ; their four underling nodes being $a _ { 3 }$ through $a _ { 6 }$ ; etc. (See Figure 8.3.1.) In this form, a heap has every “supervisor” greater than or equal to its two “supervisees,” down through the levels of the hierarchy.

If you have managed to rearrange your array into an order that forms a heap, then sorting it is very easy: You pull off the “top of the heap,” which will be the largest element yet unsorted. Then you “promote” to the top of the heap its largest underling. Then you promote its largest underling, and so on. The process is like what happens (or is supposed to happen) in a large corporation when the chairman of the board retires. You then repeat the whole process by retiring the new chairman of the board. Evidently the whole thing is an $N \log _ { 2 } N$ process, since each retiring chairman leads to $\log _ { 2 } N$ promotions of underlings.

Well, how do you arrange the array into a heap in the first place? The answer is again a “sift-up” process like corporate promotion. Imagine that the corporation starts out with $N / 2$ employees on the production line, but with no supervisors. Now a supervisor is hired to supervise two workers. If he is less capable than one of his workers, that one is promoted in his place, and he joins the production line. After supervisors are hired, then supervisors of supervisors are hired, and so on up the corporate ladder. Each employee is brought in at the top of the tree, but then immediately sifted down, with more capable workers promoted until their proper corporate level has been reached.

In the Heapsort implementation, the same sift-up code can be used for the initial creation of the heap and for the subsequent retirement-and-promotion phase. One execution of the Heapsort function represents the entire life-cycle of a giant corporation: $N / 2$ workers are hired; $N / 2$ potential supervisors are hired; there is a sifting up in the ranks, a sort of super Peter Principle: In due course, each of the original employees gets promoted to chairman of the board.

namespace hpsort_util { template<class T> void sift_down(NRvector<T> &ra, const Int l, const Int r) Carry out the sift-down on element ra(l) to maintain the heap structure. l and r determine the “left” and “right” range of the sift-down. { Int j,jold; T a; a=ra[l]; jold=l; $\scriptstyle { \mathrm { j } = 2 * 1 + 1 }$ ; while (j $< = \texttt { r }$ ) { if (j $< \textbf { r }$ && ra[j] $<$ ra[j+1]) $\mathrm { j } + +$ ; Compare to the better underling. if (a $> =$ ra[j]) break; Found a’s level. Terminate the siftra[jold] $=$ ra[j]; down. Otherwise, demote a and jold=j; continue. j=2\*j+1; } ra[jold] $= a$ ; Put a into its slot. }   
}

# template<class T>

void hpsort(NRvector<T> &ra)

Sort an array $\mathtt { r a } [ 0 \ldots \mathtt { n - 1 } ]$ into ascending numerical order using the Heapsort algorithm. ra is replaced on output by its sorted rearrangement.

Int i,n=ra.size();   
for (i=n/2-1; $\scriptstyle \dot { 1 } > = 0$ ; i--) The index i, which here determines the “left” range of the sift-down, i.e., the element to be sifted down, is decremented from $\tt { n } / 2 \mathrm { - } 1$ down to 0 during the “hiring” (heap creation) phase. hpsort_util::sift_down(ra,i,n-1);   
for $\scriptstyle \dot { 1 } = \mathtt { n } - 1$ ; i>0; i--) { Here the “right” range of the sift-down is decremented from $\mathtt { n } \mathtt { - } 2$ down to 0 during the “retirement-and-promotion” (heap selection) phase. SWAP(ra[0],ra[i]); Clear a space at the end of the array, and retire hpsort_util::sift_down(ra,0,i-1); the top of the heap into it.   
}

# CITED REFERENCES AND FURTHER READING:

Knuth, D.E. 1997, Sorting and Searching, 3rd ed., vol. 3 of The Art of Computer Programming (Reading, MA: Addison-Wesley), $\ S 5$ .2.3.[1] Sedgewick, R. 1998, Algorithms in C, 3rd ed. (Reading, MA: Addison-Wesley), Chapter 11.[2]

# 8.4 Indexing and Ranking

The concept of keys plays a prominent role in the management of data files. A data record in such a file may contain several items, or fields. For example, a record in a file of weather observations may have fields recording time, temperature, and wind velocity. When we sort the records, we must decide which of these fields we want to be brought into sorted order. The other fields in a record just come along for the ride and will not, in general, end up in any particular order. The field on which the sort is performed is called the key field.

For a data file with many records and many fields, the actual movement of $N$ records into the sorted order of their keys $K _ { i }$ ; $i = 0 , \ldots , N - 1$ , can be a daunting task. Instead, one can construct an index table $I _ { j }$ ; $j = 0 , \ldots , N - 1$ , such that the smallest $K _ { i }$ has $i = I _ { 0 }$ , the second smallest has $i = I _ { 1 }$ , and so on up to the largest $K _ { i }$ with $i = I _ { N - 1 }$ . In other words, the array

$$
K _ { I _ { j } } \mathrm { ~  ~ \omega ~ } _ { j } = 0 , 1 , \ldots , N - 1
$$

is in sorted order when indexed by $j$ . When an index table is available, one need not move records from their original order. Further, different index tables can be made from the same set of records, indexing them to different keys.

The algorithm for constructing an index table is straightforward: Initialize the index array with the integers from 0 to $N - 1$ ; then perform the Quicksort algorithm, moving the elements around as $i f$ one were sorting the keys. The integer that initially numbered the smallest key thus ends up in the number one position, and so on.

The concept of an index table maps particularly nicely into an object, say Indexx. The constructor takes a vector arr as its argument; it stores an index table to arr, leaving arr unmodified. Subsequently, the method sort can be invoked to rearrange arr, or any other vector, into the sorted order of arr. Indexx is not a templated class, since the stored index table does not depend on the type of vector that is indexed. However, it does need a templated constructor.

struct Indexx {Int n;VecInt indx;

template<class T> Indexx(const NRvector<T> &arr) { Constructor. Calls index and stores an index to the array arr[0..n-1]. index(&arr[0],arr.size()); Indexx() {} Empty constructor. See text.

template<class $\mathrm { T } >$ void sort(NRvector<T> &brr) {   
Sort an array brr[0..n-1] into the order defined by the stored index. brr is replaced on   
output by its sorted rearrangement. if (brr.size() $! = { \textbf { n } } )$ throw("bad size in Index sort"); NRvector<T> tmp(brr); for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j $^ { + + }$ ) brr[j] $=$ tmp[indx[j]];   
}

template<class $\mathrm { T } >$ inline const T & el(NRvector<T> &brr, Int j) const { This function, and the next, return the element of brr that would be in sorted position j according to the stored index. The vector brr is not changed.

return brr[indx[j]]; } template<class $\mathrm { T } >$ inline T & el(NRvector<T> &brr, Int j) { Same, but return an l-value. return brr[indx[j]]; }

template<class $\mathrm { \Delta T > }$ void index(const T \*arr, Int nn);   
This does the actual work of indexing. Normally not called directly by the user, but see text for exceptions.

# void rank(VecInt_O &irank) {

Returns a rank table, whose jth element is the rank of arr[j], where arr is the vector originally indexed. The smallest arr[j] has rank 0.

irank.resize(n);

for (Int j=0;j<n;j++) irank[indx[j]] = j; } };

template<class T>   
void Indexx::index(const T \*arr, Int nn)   
Indexes an array arr[0..nn-1], i.e., resizes and sets indx[0..nn-1] such that arr[indx[j]] is in ascending order for ${ \mathfrak { j } } = 0 , 1 , \dotsc , { \mathrm { n n } } - 1$ . Also sets member value n. The input array arr is not changed. nst Int M=7,NSTACK $_ { = 6 4 }$ ; t i,indxt,ir,j,k,jstack $: =$ -1, $_ { 1 = 0 }$ ; a; cInt istack(NSTACK);   
$\texttt { n } = \texttt { n n }$ ; dx.resize(n);   
$\mathtt { i r } \mathtt { = n - 1 }$ ; (j=0;j<n;j++) indx[j]=j; (;;) { if (ir-l < M) { for (j=l+1;j<=ir;j++) { indxt=indx[j]; a=arr[indxt]; for (i=j-1; $\mathrm { i } > = 1$ ;i--) { if (arr[indx[i]] $< = a ,$ ) break; indx[i+1] $=$ indx[i]; } indx[i+1] $=$ indxt; if (jstack < 0) break; ir=istack[jstack--]; $\ b { 1 } =$ istack[jstack--]; } else { $\mathtt { k } =$ (l+ir) >> 1; SWAP(indx[k],indx $\left[ 1 + 1 \right]$ ); if (arr[indx[l]] $>$ arr[indx[ir]]) { SWAP(indx[l],indx[ir]); if (arr[indx[l+1]] $>$ arr[indx[ir]]) { SWAP(indx[l+1],indx[ir]); if (arr[indx[l]] $>$ arr[indx[l+1]]) { SWAP(indx[l],indx[l+1]); $\dot { \bf z } = \bf { 1 } + 1$ ; $\scriptstyle { \dot { \mathsf { J } } } = { \dot { \mathsf { 1 } } } { \boldsymbol { \mathbf { r } } }$ ; indxt $=$ indx[l+1]; a=arr[indxt]; for (;;) { do $\dot { \bf 1 } + +$ ; while (arr[indx[i]] < a); do j--; while (arr[indx[j]] > a); if (j < i) break; SWAP(indx[i],indx[j]); indx[l+1] $=$ indx[j]; indx[j] $=$ indxt; jstack $+ = ~ 2$ ; if (jstack $> =$ NSTACK) throw("NSTACK too if (ir-i+1 $> =$ j-l) { istack[jstack] ${ \tt = i r }$ ; istack[jstack-1] ${ \bf \Phi } = \dot { \bf 1 }$ ; ir=j-1; } else {

istack[jstack] $= \mathrm { j } - 1$ ; istack[jstack-1] ${ = } 1$ ; $\beth = \dot { \beth }$ ; } } } }

A typical use of Indexx might be to rearrange three vectors (not necessarily of the same type) into the sorted order defined by one of them:

Indexx arrindex(arr);   
arrindex.sort(arr);   
arrindex.sort(brr);   
arrindex.sort(crr);

The generalization to any other number of arrays is obvious.

The Indexx object also provides a method el (for “element”) to access any vector in arr-sorted order without actually modifying that vector (or, for that matter, arr). In other words, after we index arr, say by

# Indexx arrindex(arr);

we can address an element in brr that corresponds to the jth element of a virtually sorted arr as simply arrindex.el(brr,j). Neither arr nor brr are altered from their original state. el is provided in two versions, so that it can be both an l-value (on the left-hand side of an assignment) and an r-value (in an expression).

As an aside, the reason that the internal workhorse index uses a pointer, not a vector, for its argument is so that it can be used (purists would say misused) in other situations, such as indexing one row in a matrix. That is also the reason for providing an additional, empty, constructor. If you want to index nn consecutive elements sitting around somewhere, pointed to by ptr, you write

Indexx myhack;   
myhack.index(ptr,nn);

A rank table is different from an index table. A rank table’s $j$ th entry gives the rank of the $j$ th element of the original array of keys, ranging from 0 (if that element was the smallest) to $N - 1$ (if that element was the largest). One can easily construct a rank table from an index table. Indeed, you might already have noticed the method rank in Indexx that returns just such a table, stored as a vector.

Figure 8.4.1 summarizes the concepts discussed in this section.

# 8.5 Selecting the Mth Largest

Selection is sorting’s austere sister. (Say that five times quickly!) Where sorting demands the rearrangement of an entire data array, selection politely asks for a single returned value: What is the $k$ th smallest (or, equivalently, the $m = N - 1 - k$ th largest) element out of $N$ elements? (In this convention, used throughout this section, $k$ takes on values $k = 0 , 1 , \ldots , N - 1$ , so $k = 0$ is the smallest array element and $k = N - 1$ the largest.) The fastest methods for selection do, unfortunately, rearrange the array for their own computational purposes, typically putting all smaller elements to the left of the $k$ th, all larger elements to the right, and scrambling the order within each subset. This side effect is at best innocuous, at worst downright inconvenient. When an array is very long, so that making a scratch copy of it is taxing on memory, one turns to in-place algorithms without side effects, which are slower but leave the original array undisturbed.

![](images/aec119fcc36e6f2c6702e7fc5f65ef67388c759749c8b401ebec4711abea28cf.jpg)  
Figure 8.4.1. (a) An unsorted array of six numbers. (b) Index table whose entries are pointers to the elements of (a) in ascending order. (c) Rank table whose entries are the ranks of the corresponding elements of (a). (d) Sorted array of the elements in (a).

The most common use of selection is in the statistical characterization of a set of data. One often wants to know the median element in an array (quantile $p = 1 / 2 ,$ ) or the top and bottom quartile elements (quantile $p = 1 / 4 , 3 / 4 )$ . When $N$ is odd, the exact definition of the median is that it is the $k$ th element, with $k = ( N - 1 ) / 2$ . When $N$ is even, statistics books define the median as the arithmetic mean of the elements $k = N / 2 - 1$ and $k = N / 2$ (that is, $N / 2$ from the bottom and $N / 2$ from the top). If you embrace such formality, you must perform two separate selections to find these elements. (If you do the first selection by a partition method, see below, you can do the second by a single pass through $N / 2$ elements in the right partition, looking for the smallest element.) For $N > 1 0 0$ we usually use $k = N / 2$ as the median element, formalists be damned.

A variant on selection for large data sets is single-pass selection, where we have a stream of input values, each of which we get to see only once. We want to be able to report at any time, say after $N$ values, the $k$ th smallest (or largest) value seen so far, or, equivalently, the quantile value for some $p$ . We will describe two approaches: If we care only about the smallest (or largest) $M$ values, for fixed $M$ , so that $0 \leq k < M$ , then there are good algorithms that require only $M$ storage. On the other hand, if we can tolerate an approximate answer, then there are efficient algorithms that can report at any time a good estimate of the $p$ -quantile value for any $p$ , $0 < p < 1$ . That is to say, we will get not the exact $k$ th smallest element, $k = p N$ , of the $N$ that have gone by, but something very close to it — and without requiring $N$ storage or having to know $p$ in advance.

The fastest general method for selection, allowing rearrangement, is partitioning, exactly as was done in the Quicksort algorithm (-8.2). Selecting a “random” partition element, one marches through the array, forcing smaller elements to the left, larger elements to the right. As in Quicksort, it is important to optimize the inner loop, using “sentinels” $( \ S 8 . 2 )$ to minimize the number of comparisons. For sorting, one would then proceed to further partition both subsets. For selection, we can ignore one subset and attend only to the one that contains our desired $k$ th element. Selection by partitioning thus does not need a stack of pending operations, and its operations count scales as $N$ rather than as $N \log N$ (see [1]). Comparison with sort in $\ S 8 . 2$ should make the following routine obvious.

# template<class T>

# T select(const Int k, NRvector<T> &arr)

Given k in $\left[ 0 \ldots \mathbf { n } \mathbf { - } 1 \right]$ returns an array value from arr[0..n-1] such that k array values are less than or equal to the one returned. The input array will be rearranged to have this value in location arr[k], with all smaller elements moved to arr[0..k-1] (in arbitrary order) and all larger elements in arr $[ \mathbf { k } { + } 1 \mathbf { \cdot } \mathbf { \cdot } \mathbf { n } { - } 1 ]$ (also in arbitrary order).

Int i,ir,j,l,mid, $\mathbf { n } =$ arr.size();   
T a;   
$\mathtt { 1 } = 0$ ;   
$\mathrm { i } \mathbf { r } { = } \mathbf { n } { - } 1$ ;   
for (;;) { if (ir $< = ~ 1 + 1$ ) { Active partition contains 1 or 2 elements. if ( $\scriptstyle \mathbf { i r } \ = = \ 1 + 1$ && arr[ir] $<$ arr[l]) Case of 2 elements. SWAP(arr[l],arr[ir]); return arr[k]; } else { mid=(l+ir) >> 1; Choose median of left, center, and right el-SWAP(arr[mid],arr[l+1]); ements as partitioning element a. Also if (arr[l] $>$ arr[ir]) rearrange so that a $\mathbf { \hat { \mu } } _ { \mathbf { \mu } } \mathbf { \Sigma } [ 1 ] \mathbf { \beta } \leq \mathbf { a r r } \left[ \mathbf { \hat { \mu } } _ { 1 + 1 } \right]$ , SWAP(arr[l],arr[ir]); $\mathbf { a r r } \left[ \mathbf { i r } \right] \geq \mathbf { a r r } \left[ \mathbf { \bar { 1 } + } \mathbf { 1 } \right]$ . if (arr[l+1] $>$ arr[ir]) SWAP(arr[l+1],arr[ir]); if (arr[l] $>$ arr[l+1]) SWAP(arr[l],arr[l+1]); $\dot { \bf z } = \bf { 1 } + \bf { 1 }$ ; Initialize pointers for partitioning. j=ir; a=arr[l+1]; Partitioning element. for (;;) { Beginning of innermost loop. do i++; while (arr[i] < a); Scan up to find element $> a$ . do j--; while (arr[j] $>$ a); Scan down to find element $< \mathtt { a }$ . if (j < i) break; Pointers crossed. Partitioning complete. SWAP(arr[i],arr[j]); End of innermost loop. arr[l+1] $=$ arr[j]; Insert partitioning element. arr[j] $= a$ ; if (j $> = { \bf \nabla } \mathbf { k } .$ ) ir=j-1; Keep active the partition that contains the if (j <= k) $\mathbf { \vec { \tau } } _ { 1 } = \mathbf { \vec { \tau } } _ { 1 }$ ; kth element. }   
}

If you don’t want your array arr to be rearranged, then you will want to make a scratch copy before calling select, e.g.,

# VecDoub brr(arr);

The reason for not doing this internally in select is because you may wish to call select with a variety of different values k, and it would be wasteful to copy the vector anew each time; instead, just let brr keep getting rearranged.

# 8.5.1 Tracking the M Largest in a Single Pass

Of course select should not be used for the trivial cases of finding the largest, or smallest, element in an array. Those cases, you code by hand as simple for loops.

There are also efficient ways to code the case where $k$ is bounded by some fixed $M$ , modest in comparison to $N$ , so that memory of order $M$ is not burdensome. Indeed, $N$ may not even be known: You may have a stream of incoming data values and be called upon at any time to provide a list of the $M$ largest values seen so far.

A good approach to this case is to use the method of Heapsort (-8.3), maintaining a heap of the $M$ largest values. The advantage of the heap structure, as opposed to a linear array of length $M$ , is that at most $\log M$ , rather than $M$ , operations are required every time a new data value is processed.

The object Heapselect has a constructor, by which you specify $M$ , an “add” method that assimilates a new data value, and a “report” method for getting the $k$ th largest seen so far. Note that the initial cost of a report is $O ( M \log M )$ , because we need to sort the heap; but you can then get all values of $k$ at no extra cost, until you do the next add. A special case is that getting the $M - 1 \mathrm { s } 1$ t largest is always cheap, since it is at the top of the heap; so if you have a single favorite value of $k$ , it is best to choose $M$ with $M - 1 = k$ .

# struct Heapselect {

Object for tracking the m largest values seen thus far in a stream of values.

Int m,n,srtd;   
VecDoub heap;

Heapselect(Int mm) : $\mathbf { m } \left( \mathbf { m } \mathbf { m } \right)$ , ${ \bf n } ( 0 )$ , srtd(0), heap(mm,1.e99) {} Constructor. The argument is the number of largest values to track.

# void add(Doub val) {

Assimilate a new value from the stream. Int j,k; if (n<m) { Heap not yet filled. hea $\ u [ \mathrm { n + + } ] = \mathrm { v a l } ;$ ; if ( $\mathrm { \Omega } _ { \mathrm { { n } } } = = \mathrm { { m } }$ ) sort(heap); Create initial heap by overkill! } else { if (val $>$ heap[0]) { Put it on the heap? heap[0] $=$ val; for $( \mathrm { j } = 0$ ;;) { Sift down. $\mathbf { k } { = } ( \mathrm { ~ j ~ } \ < < \ 1 ) \ + \ 1 \ \mathbf { ; }$ ; if (k $> \ m - 1$ ) break; if (k $\downarrow =$ (m-1) && heap[k] $>$ heap[k+1]) $\mathrm { k } { + + }$ ; if (heap[j] $< =$ heap[k]) break; SWAP(heap[k],heap[j]); $\scriptstyle { \dot { \mathbf { J } } } = \mathbf { k }$ ; } } n++; } srtd $\mathit { \Theta } = \mathit { \Theta } 0$ ; Mark heap as “unsorted”.   
}

# Doub report(Int k) {

Return the kth largest value seen so far. $\mathtt { k } = 0$ returns the largest value seen, $\tt k = 1$ the second largest, : : : , $\mathtt { k } = \mathtt { m } - 1$ the last position tracked. Also, k must be less than the number of previous values assimilated.

Int mm $=$ MIN $( \mathtt { n } , \mathtt { m } )$ ; if $\mathrm { ( k ) ~ } \mathrm { m m } { - } 1 .$ ) throw("Heapselect k too big"); if $( \textbf k = = \textbf { m } { - } 1$ ) return heap[0]; Always free, since top of heap. if (! srtd) { sort(heap); srtd $= ~ 1$ ; } Otherwise, need to sort the heap. return heap[mm-1-k]; }

};

# 8.5.2 Single-Pass Estimation of Arbitrary Quantiles

The data values fly by in a stream. You get to look at each value only once, and do a constant-time process on it (meaning that you can’t take longer and longer to process later and later data values). Also, you have only a fixed amount of storage memory. From time to time you want to know the median value (or 95th percentile value, or arbitrary $p$ -quantile value) of the data that you have seen thus far. How do you do this?

Evidently, with the conditions stated, you’ll have to tolerate an approximate answer, since an exact answer must require unbounded storage and (perhaps) unlimited processing. If you think that “binning” is somehow the answer, you are right. But it is not immediately obvious how to choose the bins, since you have to see a potentially unlimited amount of data before you can tell for sure how its values are distributed.

Chambers et al. [2] have given a robust, and extremely fast, algorithm, which they call $I Q$ agent, that adaptively adjusts a set of bins so that they converge to the data values of specified quantile $p$ -values. The general idea (see Figure 8.5.1) is to accumulate incoming data into batches, then to update a stored, piecewise linear, cumulative distribution function (cdf) by adding a batch’s cdf and then interpolating back to a fixed set of $p$ -values. Arbitrary requested quantile values (“incremental quantiles,” or “IQs,” hence the algorithm’s name) can be obtained at any time by linear interpolation on the stored cdf. Batching allows the program to be very efficient, with an (amortized) cost of only a small number of operations per new data value. The batching is done transparently to the user.

Similar to Heapselect, the IQagent object has add and report methods, the latter now taking a value for $p$ as its argument. In the implementation below, we use a batch size of nbuf $= 1 0 0 0$ but do an early update step with a partial batch whenever a quantile is requested. With these parameters, you should therefore request quantile information no more frequently than after every few nbuf data values, at which point you can request as many different values of $p$ as you want before continuing. The alternative is to remove the call to update from report, in which case you’ll get fast, but constant, answers, changing only after each regular batch update.

IQagent uses internally a general purpose set of 251 $p$ -values that includes integer percentile points from 10 to 90, and a logarithmically spaced set of smaller and larger values spanning $1 0 ^ { - 6 }$ to $1 - 1 0 ^ { - 6 }$ . Other $p$ -values that you request are obtained by interpolation. Of course you cannot get meaningful tail quantiles for small values of $p$ until at least several times $1 / p$ data values have been processed. Before that, the program will simply report the smallest value previously seen (or largest value previously seen, for $p  1 _ { . }$ ).

![](images/7e1329296dc24236966377ad5a339246db31242b3bad3664693dae97ceb77bd5.jpg)  
Figure 8.5.1. Algorithm for updating a piecewise linear cumulative distribution function (cdf). (a) The cdf is represented by quantile values at a fixed set of $p$ -values (here, just 3). (b) A batch of new data values (here, just 4) define a stepwise constant cdf. (c) The two cdfs are summed. New data steps are small in proportion to the new batch size versus number of data values previously processed. (d) The new cdf representation is obtained by interpolating the fixed $p$ -values to (c).

struct IQagent {   
Object for estimating arbitrary quantile values from a continuing stream of data values. static const Int nbuf $\ l = \ 1 0 0 0$ ; Batch size. You may $\times 1 0$ if you expect $>$ Int nq, nt, nd; $1 0 ^ { 6 }$ data values. VecDoub pval,dbuf,qile; Doub q0, qm;   
IQagent() : nq(251), nt(0), nd(0), pval(nq), dbuf(nbuf),   
qile(nq,0.), q0(1.e99), qm(-1.e99) {   
Constructor. No arguments. for (Int $\scriptstyle { \dot { \mathcal { I } } } = 8 5$ ; $\scriptstyle \mathtt { j } < = 1 6 5$ ; $\mathrm { j } + +$ ) pval[j] $=$ (j-75.)/100.; Set general purpose array of $p$ -values ranging from $1 0 ^ { - 6 }$ to $1 - 1 0 ^ { - 6 }$ . You can change this if you want: for (Int $\scriptstyle { \dot { \mathsf { J } } } = 8 4$ ; $\scriptstyle { \dot { \bar { \jmath } } } > = 0$ ;j--) { pval[j] $=$ 0.87191909\*pval[j+1]; pval[250-j] $=$ 1.-pval[j]; }   
}   
void add(Doub datum) {   
Assimilate a new value from the stream. dbuf[nd++] $=$ datum; if (datum $<$ q0) {q0 $=$ datum;} if (datum $>$ qm) {qm $=$ datum;}

if (nd $= =$ nbuf) update();}

Time for a batch update.

# void update() {

Batch update, as shown in Figure 8.5.1. This function is called by add or report and should not be called directly by the user.

Int $\mathrm { j } \mathrm { d } = \mathrm { 0 }$ ,jq=1,iq;   
Doub target, told ${ = } 0$ ., tnew ${ \tt = } 0$ ., qold, qnew;   
VecDoub newqile(nq); Will be new quantiles after update.   
sort(dbuf,nd);   
qold $=$ qnew $=$ qile[0] $= { \textbf { n 6 } }$ wqile[0] $=$ q0; Set lowest and highest to min   
qile[nq-1] $=$ newqile[nq-1] $=$ qm; and max values seen so far,   
pval[0] $=$ min(0.5/(nt+nd),0.5\*pval[1]); and set compatible $p$ -values.   
pval[nq-1] $=$ max(1.-0.5/(nt+nd),0.5\*(1.+pval[nq-2]));   
for (iq=1;iq<nq-1; ${ \mathrm { i } } { \mathrm { q } } + + { \mathrm { \ i } }$ ) { Main loop over target $p$ -values for intertarget $=$ (nt+nd)\*pval[iq]; polation. if (tnew $<$ target) for (;;) Here’s the guts: We locate a succession of abscissa-ordinate pairs (qnew,tnew) that are the discontinuities of value or slope in Figure 8.5.1(c), breaking to perform an interpolation as we cross each target. if (jq $<$ nq && (jd $> =$ nd || qile[jq] $<$ dbuf[jd])) { Found slope discontinuity from old CDF. qnew $=$ qile[jq]; tnew $=$ jd $^ +$ nt\*pval[jq++]; if (tnew $> =$ target) break; } else { Found value discontinuity from batch data qnew $=$ dbuf[jd]; CDF. tnew $=$ told; if (qile[jq]>qile[jq-1]) tnew $+ =$ nt\*(pval[jq]-pval[jq-1]) \*(qnew-qold)/(qile[jq]-qile[jq-1]); jd++; if (tnew $> =$ target) break; told $=$ tnew++; qold $=$ qnew; if (tnew $> =$ target) break; } told $=$ tnew; qold $=$ qnew; } Break to here and perform the new interpolation. if (tnew $= =$ told) newqile[iq] $=$ 0. $^ { 5 \ast }$ (qold+qnew); else newqile[iq] $=$ qold $^ +$ (qnew-qold)\*(target-told)/(tnew-told); told $=$ tnew; qold $=$ qnew;   
}   
qile $=$ newqile;   
nt $+ =$ nd;   
nd $\qquad = \ 0$ ;

# Doub report(Doub p) {

Return estimated p-quantile for the data seen so far. (E.g., $\mathbf { p } = \mathbf { 0 . 5 }$ for median.) Doub q; if (nd > 0) update(); You may want to remove this line. See text. Int $\scriptstyle \mathrm { j } 1 = 0$ ,jh ${ \bf \Phi } _ { \cdot } = { \bf \Phi } _ { \cdot }$ nq-1,j; while (jh-jl>1) { Locate place in table by bisection. j = (jh+jl)>>1; if (p > pval[j]) jl=j; else jh=j; } ${ \mathrm { ~ j ~ } } =$ jl; Interpolate. q $=$ qile[j] $^ +$ (qile[j+1]-qile[j])\*(p-pval[j])/(pval[j+1]-pval[j]); return MAX(qile[0],MIN(qile[nq-1],q));   
}

How accurate is the IQ agent algorithm, as compared, say, to storing all $N$ data values in an array $A$ and then reporting the “exact” quantile $A _ { \lfloor p N \rfloor }$ ? There are several sources of error, all of which you can control by modifying parameters in IQagent. (We think that the default parameters will work just fine for almost all users.) First, there is interpolation error: The desired cdf is represented by a piecewise linear function between $\mathtt { n q } = 2 5 1$ stored values. For typical distributions, this limits the accuracy to three or four significant figures. We find it hard to believe that anyone needs to know a median, e.g., more accurately than this, but if you do, then you can increase the density of $p$ -values in the regions of interest.

Second, there are statistical errors. One way to characterize these is to ask what value $j$ has $A _ { j }$ closest to the quantile reported by IQ agent, and then how small is $\vert j - p N \vert$ as a fraction of $[ N p ( \hat { 1 } - p ) ] ^ { 1 / 2 }$ , the accuracy inherent in your finite sample size $N$ . If this fraction is $\lesssim 1$ , then the estimate is “good enough,” meaning that no method can do substantially better at estimating the population quantiles given your sample.

With the default parameters, and for reasonably behaved distributions, IQagent passes this test for $N \lesssim 1 0 ^ { 6 }$ . For larger $N$ , the statistical error becomes significant (though still generally smaller than the interpolation error, above). You can, however, decrease it by increasing the batch size, nbuf. Larger is always better, if you have the memory and can tolerate the logarithmic increase in the cost per point of the sort.

Although the accuracy of IQagent is not guaranteed by a provable bound, the algorithm is fast, robust, and highly recommended. For other approaches to incremental quantile estimation, including some that do give provable bounds (but have other issues), see [3,4] and references cited therein.

# 8.5.3 Other Uses for Incremental Quantile Estimation

Incremental quantile estimation provides a useful way to histogram data into variable-size bins that each contain the same number of points, without knowing in advance the bin boundaries: First, throw $N$ data values at an IQagent object. Next, choose a number of bins $m$ , and define

$$
p _ { i } \equiv \frac { i } { m } , \qquad i = 0 , \ldots , m
$$

Finally, if $q _ { i }$ is the quantile value at $p _ { i }$ , plot the $i$ th bin from $q _ { i }$ to $q _ { i + 1 }$ with a height

$$
h _ { i } = N \frac { p _ { i + 1 } - p _ { i } } { q _ { i + 1 } - q _ { i } } , \qquad i = 0 , \ldots , m - 1
$$

A different application concerns the monitoring of quantile values for changes. For example, you might be producing widgets with a parameter $T$ whose tolerance is $T \pm \delta T$ , and you want an early warning if the observed values of $T$ at the 5th and 95th percentiles start to drift.

The IQagent object is easily modified for such applications. Simply change the line nt $+ =$ nd to nt $=$ my_constant, where my_constant is the number of past widgets that you want to average over. (More precisely, the number corresponding to one e-fold of weight decrease in an exponentially decreasing average over all past production.) Now, the stored cdf combines with a new batch of data with a constant, not an increasing, weight, and you can look for changes over time in any desired quantiles.

# 8.5.4 In-Place Selection

In-place, nondestructive, selection is conceptually simple, but it requires a lot of bookkeeping, and it is correspondingly slow. The general idea is to pick some number $M$ of elements at random, to sort them, and then to make a pass through the array counting how many elements fall in each of the $M + 1$ intervals defined by these elements. The $k$ th largest will fall in one such interval — call it the “live” interval. One then does a second round, first picking $M$ random elements in the live interval, and then determining which of the new, finer, $M + 1$ intervals all presently live elements fall into. And so on, until the $k$ th element is finally localized within a single array of size $M$ , at which point direct selection is possible.

How shall we pick $M ?$ The number of rounds, $\log _ { M } N = \log _ { 2 } N / \log _ { 2 } M$ , will be smaller if $M$ is larger; but the work to locate each element among $M + 1$ subintervals will be larger, scaling as $\log _ { 2 } M$ for bisection, say. Each round requires looking at all $N$ elements, if only to find those that are still alive, while the bisections are dominated by the $N$ that occur in the first round. Minimizing $O ( N \log _ { M } N ) +$ $O ( N \log _ { 2 } M )$ thus yields the result

$$
M \sim 2 \sqrt { \log _ { 2 } N }
$$

The square root of the logarithm is so slowly varying that secondary considerations of machine timing become important. We use $M = 6 4$ as a convenient constant value.

Further discussion, and code, is in a Webnote [5].

# CITED REFERENCES AND FURTHER READING:

Sedgewick, R. 1998, Algorithms in C, 3rd ed. (Reading, MA: Addison-Wesley), pp. 126ff.[1]   
Knuth, D.E. 1997, Sorting and Searching, 3rd ed., vol. 3 of The Art of Computer Programming (Reading, MA: Addison-Wesley).   
Chambers, J.M., James, D.A., Lambert, D., and Vander Wiel, S. 2006, “Monitoring Networked Applications with Incremental Quantiles,” Statistical Science, vol. 21.[2]   
Tieney, L. 1983, “A Space-efficient Recursive Procedure for Estimating a Quantile of an Unknown Distribution,” SIAM Journal on Scientific and Statistical Computing, vol. 4, pp. 706- 711.[3]   
Liechty, J.C., Lin, D.K.J, and McDermott, J.P. 2003, “Single-Pass Low-Storage Arbitrary Quantile Estimation for Massive Datasets,” Statistics and Computing, vol. 13, pp. 91–100.[4]   
Numerical Recipes Software 2007, “Code Listing for Selip,” Numerical Recipes Webnote No. 1 1, at http://www.nr.com/webnotes?11 [5]

# 8.6 Determination of Equivalence Classes

A number of techniques for sorting and searching relate to data structures whose details are beyond the scope of this book, for example, trees, linked lists, etc. These structures and their manipulations are the bread and butter of computer science, as distinct from numerical analysis, and there is no shortage of books on the subject.

In working with experimental data, we have found that one particular such manipulation, namely the determination of equivalence classes, arises sufficiently often to justify inclusion here.

The problem is this: There are $N$ “elements” (or “data points” or whatever), numbered $0 , \ldots , N - 1$ . You are given pairwise information about whether the elements are in the same equivalence class of “sameness,” by whatever criterion happens to be of interest. For example, you may have a list of facts like: “Element 3 and element 7 are in the same class; element 19 and element 4 are in the same class; element 7 and element 12 are in the same class, : : : ” Alternatively, you may have a procedure, given the numbers of two elements $j$ and $k$ , for deciding whether they are in the same class or different classes. (Recall that an equivalence relation can be anything satisfying the RST properties: reflexive, symmetric, transitive. This is compatible with any intuitive definition of “sameness.”)

The desired output is an assignment to each of the $N$ elements of an equivalence class number, such that two elements are in the same class if and only if they are assigned the same class number.

Efficient algorithms work like this: Let $F ( j )$ be the class or “family” number of element $j$ . Start off with each element in its own family, so that $F ( j ) = j$ . The array $F ( j )$ can be interpreted as a tree structure, where $F ( j )$ denotes the parent of $j$ . If we arrange for each family to be its own tree, disjoint from all the other “family trees,” then we can label each family (equivalence class) by its most senior great-great-: : :grandparent. The detailed topology of the tree doesn’t matter at all, as long as we graft each related element onto it somewhere.

Therefore, we process each elemental datum “ $j$ is equivalent to $k ^ { \prime \prime }$ by (i) tracking $j$ up to its highest ancestor; (ii) tracking $k$ up to its highest ancestor; and (iii) giving $j$ to $k$ as a new parent, or vice versa (it makes no difference). After processing all the relations, we go through all the elements $j$ and reset their $F ( j )$ ’s to their highest possible ancestors, which then label the equivalence classes.

The following routine, based on Knuth [1], assumes that there are m elemental pieces of information, stored in two arrays of length m, lista,listb, the interpretation being that lista[j] and listb[j], $\mathrm { j } { = } 0 \ldots { } . \mathrm { m } { - } 1$ , are the numbers of two elements that (we are thus told) are related.

# void eclass(VecInt_O &nf, VecInt_I &lista, VecInt_I &listb)

Given m equivalences between pairs of n individual elements in the form of the input arrays lista[0..m-1] and listb[0..m-1], this routine returns in $\mathtt { n f } \left[ 0 \dots \dots 1 \right]$ the number of the equivalence class of each of the n elements, integers between 0 and $\mathtt { n - 1 }$ (not all such integers used).

Int l,k,j, $\mathbf { n } =$ nf.size(), $\mathfrak { m } =$ lista.size();   
for $\scriptstyle ( \mathtt { k } = 0$ ;k<n;k++) nf[k] ${ \mathrm { = k } }$ ; Initialize each element its own class.   
for $\scriptstyle 1 = 0$ ;l<m; $^ { 1 + + }$ ) { For each piece of input information... j=lista[l]; while (nf[j] $! =$ j) j=nf[j]; Track first element up to its ancestor. k=listb[l]; while (nf[k] $! =$ k) k=nf[k]; Track second element up to its ancestor. if (j $\mathbf { \updownarrow } = \mathbf { \ k } )$ ) nf[j] $\mathbf { \sigma } = \mathbf { k }$ ; If they are not already related, make them   
} so.   
for $\scriptstyle \dot { \ j } = 0$ ;j<n;j++) Final sweep up to highest ancestors. while (nf[j] $! =$ nf[nf[j]]) nf[j] $=$ nf[nf[j]];

# }

Alternatively, we may be able to construct a boolean function equiv(j,k) that returns a value true if elements $\dot { \mathsf { J } }$ and k are related, or false if they are not. Then we want to loop over all pairs of elements to get the complete picture. D. Eardley has devised a clever way of doing this while simultaneously sweeping the tree up to high ancestors in a manner that keeps it current and obviates most of the final sweep phase:

void eclazz(VecInt_O &nf, Bool equiv(const Int, const Int))

Given a user-supplied boolean function equiv that tells whether a pair of elements, each in the range 0...n-1, are related, return in nf[0..n-1] equivalence class numbers for each element. {

Int kk,jj, $\mathbf { n } =$ nf.size();nf[0] ${ = } 0$ ;for (jj=1;jj<n;jj $^ { + + }$ ) {

Loop over first element of all pairs.

nf[jj]=jj; for (kk=0;kk<jj;kk $^ { + + }$ ) { Loop over second element of all pairs. nf[kk]=nf[nf[kk]]; Sweep it up this much. if (equiv(jj+1,kk+1)) nf[nf[nf[kk]]]=jj; Good exercise for the reader to figure out why this much ancestry is necessary! } for (jj ${ = } 0$ ;jj<n;jj $^ { + + }$ ) nf[jj] $=$ nf[nf[jj]]; Only this much sweeping is needed finally.

# CITED REFERENCES AND FURTHER READING:

Knuth, D.E. 1997, Fundamental Algorithms, 3rd ed., vol. 1 of The Art of Computer Programming (Reading, MA: Addison-Wesley), $\ S 2 . 3 . 3$ .[1] Sedgewick, R. 1998, Algorithms in C, 3rd ed. (Reading, MA: Addison-Wesley), Chapter 30.

# Root Finding and Nonlinear Sets of Equations

# 9.0 Introduction

We now consider that most basic of tasks, solving equations numerically. While most equations are born with both a right-hand side and a left-hand side, one traditionally moves all terms to the left, leaving

$$
f ( x ) = 0
$$

whose solution or solutions are desired. When there is only one independent variable, the problem is one-dimensional, namely to find the root or roots of a function.

With more than one independent variable, more than one equation can be satisfied simultaneously. You likely once learned the implicit function theorem, which (in this context) gives us the hope of satisfying $N$ equations in $N$ unknowns simultaneously. Note that we have only hope, not certainty. A nonlinear set of equations may have no (real) solutions at all. Contrariwise, it may have more than one solution. The implicit function theorem tells us that “generically” the solutions will be distinct, pointlike, and separated from each other. If, however, life is so unkind as to present you with a nongeneric, i.e., degenerate, case, then you can get a continuous family of solutions. In vector notation, we want to find one or more $N$ -dimensional solution vectors $\mathbf { X }$ such that

$$
\mathbf { f } \left( \mathbf { x } \right) = \mathbf { 0 }
$$

where f is the $N$ -dimensional vector-valued function whose components are the individual equations to be satisfied simultaneously.

Don’t be fooled by the apparent notational similarity of equations (9.0.2) and (9.0.1). Simultaneous solution of equations in $N$ dimensions is much more difficult than finding roots in the one-dimensional case. The principal difference between one and many dimensions is that, in one dimension, it is possible to bracket or “trap” a root between bracketing values, and then hunt it down like a rabbit. In multidimensions, you can never be sure that the root is there at all until you have found it.

Except in linear problems, root finding invariably proceeds by iteration, and this is equally true in one or in many dimensions. Starting from some approximate trial solution, a useful algorithm will improve the solution until some predetermined convergence criterion is satisfied. For smoothly varying functions, good algorithms will always converge, provided that the initial guess is good enough. Indeed one can even determine in advance the rate of convergence of most algorithms.

It cannot be overemphasized, however, how crucially success depends on having a good first guess for the solution, especially for multidimensional problems. This crucial beginning usually depends on analysis rather than numerics. Carefully crafted initial estimates reward you not only with reduced computational effort, but also with understanding and increased self-esteem. Hamming’s motto, “the purpose of computing is insight, not numbers,” is particularly apt in the area of finding roots. You should repeat this motto aloud whenever your program converges, with sixteendigit accuracy, to the wrong root of a problem, or whenever it fails to converge because there is actually no root, or because there is a root but your initial estimate was not sufficiently close to it.

“This talk of insight is all very well, but what do I actually do?” For onedimensional root finding, it is possible to give some straightforward answers: You should try to get some idea of what your function looks like before trying to find its roots. If you need to mass-produce roots for many different functions, then you should at least know what some typical members of the ensemble look like. Next, you should always bracket a root, that is, know that the function changes sign in an identified interval, before trying to converge to the root’s value.

Finally (this is advice with which some daring souls might disagree, but we give it nonetheless) never let your iteration method get outside of the best bracketing bounds obtained at any stage. We will see below that some pedagogically important algorithms, such as the secant method or Newton-Raphson, can violate this last constraint and are thus not recommended unless certain fixups are implemented.

Multiple roots, or very close roots, are a real problem, especially if the multiplicity is an even number. In that case, there may be no readily apparent sign change in the function, so the notion of bracketing a root — and maintaining the bracket — becomes difficult. We are hard-liners: We nevertheless insist on bracketing a root, even if it takes the minimum-searching techniques of Chapter 10 to determine whether a tantalizing dip in the function really does cross zero. (You can easily modify the simple golden section routine of $\ S 1 0 . 2$ to return early if it detects a sign change in the function. And, if the minimum of the function is exactly zero, then you have found a double root.)

As usual, we want to discourage you from using routines as black boxes without understanding them. However, as a guide to beginners, here are some reasonable starting points:

- Brent’s algorithm in $\ S 9 . 3$ is the method of choice to find a bracketed root of a general one-dimensional function, when you cannot easily compute the function’s derivative. Ridders’ method $( \ S 9 . 2 )$ is concise, and a close competitor. When you can compute the function’s derivative, the routine rtsafe in $\ S 9 . 4$ , which combines the Newton-Raphson method with some bookkeeping on the bounds, is recommended. Again, you must first bracket your root. If you can easily compute two derivatives, then Halley’s method (-9.4.2) is often worth a try.

- Roots of polynomials are a special case. Laguerre’s method, in $\ S 9 . 5$ , is recommended as a starting point. Beware: Some polynomials are ill-conditioned! Finally, for multidimensional problems, the only elementary method is Newton-Raphson (-9.6), which works very well if you can supply a good first guess of the solution. Try it. Then read the more advanced material in $\ S 9 . 7$ for some more complicated, but globally more convergent, alternatives.

The routines in this chapter require that you input the function whose roots you seek. For maximum flexibility, the routines typically will accept either a function or a functor (see $\ S 1 . 3 . 3 )$ .

# 9.0.1 Graphical Search for Roots

It never hurts to look at your function, especially if you encounter any difficulty in finding its roots blindly. If you are thus hunting roots “by eye,” it is useful to have a routine that repeatedly plots a function to the screen, accepting user-supplied lower and upper limits for $x$ , automatically scaling $y$ , and making zero crossings visible. The following routine, or something like it, can occasionally save you a lot of grief.

# scrsho.h template<class T> void scrsho(T &fx) {

Graph the function or functor fx over the prompted-for interval x1,x2. Query for another plot   
until the user signals satisfaction. const Int RES $\mathtt { \mathtt { = 5 0 0 } }$ ; Number of function evaluations for each plot. const Doub XLL=75., XUR 525., YLL $\cdot ^ { = }$ 250., YUR=700.; Corners of plot, in points. char \*plotfilename $=$ tmpnam(NULL); VecDoub xx(RES), yy(RES); Doub x1,x2; Int i; for (;;) { Doub ymax $=$ -9.99e99, ymin $\ c = \ 9$ .99e99, del; cout $< <$ endl $< <$ "Enter x1 x2 ( $\bf { \chi } _ { x 1 } = \bf { \chi } _ { x 2 }$ to stop):" << endl; cin $> >$ x1 >> x2; Query for another plot, quit if $\tt x 1 { = } \tt x 2$ . if $\scriptstyle \mathbf { x } 1 = = \mathbf { x } 2$ ) break; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<RES; $\dot { 1 } + +$ ) { Evaluate the function at equal intervals. Find xx[i] $=$ x1 + i\*(x2-x1)/(RES-1.); the largest and smallest values. yy[i] $=$ fx(xx[i]); if (yy[i] $>$ ymax) ymax=yy[i]; if (yy[i] $<$ ymin) ymin=yy[i]; } del = 0.05\*((ymax-ymin) $^ +$ (ymax ${ \bf \Phi } = =$ ymin ? abs(ymax) : 0.)); Plot commands, following, are in PSplot syntax (-22.1). You can substitute commands for your favorite plotting package. PSpage pg(plotfilename); PSplot plot(pg,XLL,XUR,YLL,YUR); plot.setlimits(x1,x2,ymin-del,ymax+del); plot.frame(); plot.autoscales(); plot.lineplot(xx,yy); if (ymax\*ymin $< 0 .$ ) plot.lineseg(x1,0.,x2,0.); plot.display(); } remove(plotfilename);

# CITED REFERENCES AND FURTHER READING:

Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), Chapter 5.

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), Chapters 2, 7, and 14.   
Deuflhard, P. 2004, Newton Methods for Nonlinear Problems (Berlin: Springer).   
Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), Chapter 8.   
Householder, A.S. 1970, The Numerical Treatment of a Single Nonlinear Equation (New York: McGraw-Hill).

# 9.1 Bracketing and Bisection

We will say that a root is bracketed in the interval $( a , b )$ if $f ( a )$ and $f ( b )$ have opposite signs. If the function is continuous, then at least one root must lie in that interval (the intermediate value theorem). If the function is discontinuous, but bounded, then instead of a root there might be a step discontinuity that crosses zero (see Figure 9.1.1). For numerical purposes, that might as well be a root, since the behavior is indistinguishable from the case of a continuous function whose zero crossing occurs in between two “adjacent” floating-point numbers in a machine’s finite-precision representation. Only for functions with singularities is there the possibility that a bracketed root is not really there, as for example

$$
f ( x ) = { \frac { 1 } { x - c } }
$$

Some root-finding algorithms (e.g., bisection in this section) will readily converge to $c$ in (9.1.1). Luckily there is not much possibility of your mistaking $c$ , or any number $x$ close to it, for a root, since mere evaluation of $\vert f ( x ) \vert$ will give a very large, rather than a very small, result.

If you are given a function in a black box, there is no sure way of bracketing its roots, or even of determining that it has roots. If you like pathological examples, think about the problem of locating the two real roots of equation (3.0.1), which dips below zero only in the ridiculously small interval of about $x = \pi \pm 1 0 ^ { - 6 6 7 }$ .

In the next chapter we will deal with the related problem of bracketing a function’s minimum. There it is possible to give a procedure that always succeeds; in essence, “Go downhill, taking steps of increasing size, until your function starts back uphill.” There is no analogous procedure for roots. The procedure “go downhill until your function changes sign,” can be foiled by a function that has a simple extremum. Nevertheless, if you are prepared to deal with a “failure” outcome, this procedure is often a good first start; success is usual if your function has opposite signs in the limit $x  \pm \infty$ .

# template <class T>

# roots.h

Bool zbrac(T &func, Doub &x1, Doub &x2)

Given a function or functor func and an initial guessed range $\tt x 1$ to $\mathbf { x } 2$ , the routine expands the range geometrically until a root is bracketed by the returned values x1 and $\mathbf { x } 2$ (in which case zbrac returns true) or until the range becomes unacceptably large (in which case zbrac returns false).

const Int NTRY=50;   
const Doub FACTOR $\ L = 1$ .6;   
if $\mathbf { \bar { \Psi } } _ { \mathbf { x } 1 } \ \mathbf { \Psi } = = \ \mathbf { \Psi } _ { \mathbf { x } 2 } ,$ ) throw("Bad initial range in zbrac");   
Doub f1=func(x1);   
Doub f2=func(x2);   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<NTRY;j $^ { + + }$ ) { if (f1\*f2 $<$ 0.0) return true; if (abs(f1) $<$ abs(f2)) f1=func(x1 $+ =$ FACTOR\*(x1-x2)); else f2=func(x2 += FACTOR\*(x2-x1));   
}   
return false;

![](images/77393d599f05c30de0663e80eebaace283dac1ab7b6c94ef11135e701ecff748.jpg)  
Figure 9.1.1. Some situations encountered while root finding: (a) an isolated root $x _ { 1 }$ bracketed by two points $^ { a }$ and $^ { b }$ at which the function has opposite signs; (b) there is not necessarily a sign change in the function near a double root (in fact, there is not necessarily a root!); (c) a pathological function with many roots; in (d) the function has opposite signs at points $^ { a }$ and $^ { b }$ , but the points bracket a singularity, not a root.

Alternatively, you might want to “look inward” on an initial interval, rather than “look outward” from it, asking if there are any roots of the function $f ( x )$ in the interval from $x _ { 1 }$ to $x _ { 2 }$ when a search is carried out by subdivision into n equal intervals. The following function calculates brackets for distinct intervals that each contain one or more roots.

# template <class T>

void zbrak(T &fx, const Doub x1, const Doub x2, const Int n, VecDoub_O &xb1, VecDoub_O &xb2, Int &nroot)

Given a function or functor fx defined on the interval $[ \mathbf { x } \mathbf { 1 } , \mathbf { x } 2 ]$ , subdivide the interval into n equally spaced segments, and search for zero crossings of the function. nroot will be set to the number of bracketing pairs found. If it is positive, the arrays xb1[0..nroot-1] and xb2[0..nroot-1] will be filled sequentially with any bracketing pairs that are found. On input, these vectors may have any size, including zero; they will be resized to $\geq$ nroot. {

Int $n \mathrm { { b } = } 2 0$ ; xb1.resize(nb); xb2.resize(nb); nroot ${ = } 0$ ; Doub ${ \tt d x } = \left( { \tt x } 2 \mathrm { - x } 1 \right) / { \tt n } ;$ Determine the spacing appropriate to the mesh. Doub $\tt x { = } \tt x 1$ ; Doub fp=fx(x1); for (Int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<n;i++) { Loop over all intervals Doub fc=fx $( { \textbf { x } } + = { \mathrm { d } } \mathbf { x } )$ ; if (fc\*fp $< = ~ 0 . 0$ ) { If a sign change occurs, then record values for the xb1[nroot] $= 8$ -dx; bounds. xb2[nroot $\mathbf { \partial } + + \mathbf { \partial } ] = \mathbf { x }$ ; if(nroot $= =$ nb) { VecDoub tempvec1(xb1),tempvec2(xb2); xb1.resize(2\*nb); xb2.resize(2\*nb); for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<nb; j++) { xb1[j] $=$ tempvec1[j]; xb2[j] $=$ tempvec2[j]; } nb \*= 2; } } fp=fc; } }

# 9.1.1 Bisection Method

Once we know that an interval contains a root, several classical procedures are available to refine it. These proceed with varying degrees of speed and sureness toward the answer. Unfortunately, the methods that are guaranteed to converge plod along most slowly, while those that rush to the solution in the best cases can also dash rapidly to infinity without warning if measures are not taken to avoid such behavior.

The bisection method is one that cannot fail. It is thus not to be sneered at as a method for otherwise badly behaved problems. The idea is simple. Over some interval the function is known to pass through zero because it changes sign. Evaluate the function at the interval’s midpoint and examine its sign. Use the midpoint to replace whichever limit has the same sign. After each iteration the bounds containing the root decrease by a factor of two. If after $n$ iterations the root is known to be within an interval of size $\epsilon _ { n }$ , then after the next iteration it will be bracketed within an interval of size

$$
\epsilon _ { n + 1 } = \epsilon _ { n } / 2
$$

neither more nor less. Thus, we know in advance the number of iterations required to achieve a given tolerance in the solution,

$$
n = \log _ { 2 } \frac { \epsilon _ { 0 } } { \epsilon }
$$

where $\epsilon _ { 0 }$ is the size of the initially bracketing interval and $\epsilon$ is the desired ending tolerance.

Bisection must succeed. If the interval happens to contain more than one root, bisection will find one of them. If the interval contains no roots and merely straddles a singularity, it will converge on the singularity.

When a method converges as a factor (less than 1) times the previous uncertainty to the first power (as is the case for bisection), it is said to converge linearly. Methods that converge as a higher power,

$$
\epsilon _ { n + 1 } = { \mathrm { c o n s t a n t } } \times ( \epsilon _ { n } ) ^ { m } \qquad m > 1
$$

are said to converge superlinearly. In other contexts, “linear” convergence would be termed “exponential” or “geometrical.” That is not too bad at all: Linear convergence means that successive significant figures are won linearly with computational effort.

It remains to discuss practical criteria for convergence. It is crucial to keep in mind that only a finite set of floating point values have exact computer representations. While your function might analytically pass through zero, it is probable that its computed value is never zero, for any floating-point argument. One must decide what accuracy on the root is attainable: Convergence to within $1 0 ^ { - 1 0 }$ in absolute value is reasonable when the root lies near 1 but certainly unachievable if the root lies near $1 0 ^ { 2 6 }$ . One might thus think to specify convergence by a relative (fractional) criterion, but this becomes unworkable for roots near zero. To be most general, the routines below will require you to specify an absolute tolerance, such that iterations continue until the interval becomes smaller than this tolerance in absolute units. Often you may wish to take the tolerance to be $\epsilon ( | x _ { 1 } | + | x _ { 2 } | ) / 2$ , where $\epsilon$ is the machine precision and $x _ { 1 }$ and $x _ { 2 }$ are the initial brackets. When the root lies near zero you ought to consider carefully what reasonable tolerance means for your function. The following routine quits after 50 bisections in any event, with $2 ^ { - 5 0 } \approx 1 0 ^ { - 1 5 }$ .

template <class $\mathrm { T } >$   
Doub rtbis(T &func, const Doub x1, const Doub x2, const Doub xacc) {   
Using bisection, return the root of a function or functor func known to lie between x1 and $\tt x 2$ The root will be refined until its accuracy is ˙xacc.   
const Int JMAX $\mathtt { = 5 0 }$ ; Maximum allowed number of bisections.   
Doub dx,xmid,rtb;   
Doub f=func(x1);   
Doub fmid=func(x2);   
if (f\*fmid $> = \ 0 . 0 $ ) throw("Root must be bracketed for bisection in rtbis");   
rtb $\mathbf { \Sigma } = \mathbf { \Sigma } _ { \mathbf { f } } \ < \ \mathbf { \Sigma } 0 . 0$ ? (dx=x2-x1,x1) : (dx=x1-x2,x2); Orient the search so that $\mathtt { f } > 0$   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<JMAX;j++) { lies at $\tt x { + d x }$ . fmid=func(xmid=rtb+(dx $* = \ 0 . 5 )$ ); Bisection loop. if (fmid $< = \ 0 . 0$ ) rtb $=$ xmid; if (abs(dx) $<$ xacc || fmid $\mathrm { ~  ~ \omega ~ } = \mathrm { ~  ~ 0 ~ . ~ 0 ~ }$ ) return rtb;   
}   
throw("Too many bisections in rtbis");

# 9.2 Secant Method, False Position Method, and Ridders' Method

For functions that are smooth near a root, the methods known respectively as false position (or regula falsi) and the secant method generally converge faster than bisection. In both of these methods the function is assumed to be approximately linear in the local region of interest, and the next improvement in the root is taken as the point where the approximating line crosses the axis. After each iteration, one of the previous boundary points is discarded in favor of the latest estimate of the root.

The only difference between the methods is that secant retains the most recent of the prior estimates (Figure 9.2.1; this requires an arbitrary choice on the first iteration), while false position retains that prior estimate for which the function value has the opposite sign from the function value at the current best estimate of the root, so that the two points continue to bracket the root (Figure 9.2.2). Mathematically, the secant method converges more rapidly near a root of a sufficiently continuous function. Its order of convergence can be shown to be the “golden ratio” 1:618 : : : , so that

$$
\operatorname* { l i m } _ { k \to \infty } | \epsilon _ { k + 1 } | \approx \mathrm { c o n s t } \times \left| \epsilon _ { k } \right| ^ { 1 . 6 1 8 }
$$

The secant method has, however, the disadvantage that the root does not necessarily remain bracketed. For functions that are not sufficiently continuous, the algorithm can therefore not be guaranteed to converge: Local behavior might send it off toward infinity.

False position, since it sometimes keeps an older rather than newer function evaluation, has a lower order of convergence. Since the newer function value will sometimes be kept, the method is often superlinear, but estimation of its exact order is not so easy.

Here are sample implementations of these two related methods. While these methods are standard textbook fare, Ridders’ method, described below, or Brent’s method, described in the next section, are almost always better choices. Figure 9.2.3 shows the behavior of the secant and false-position methods in a difficult situation.

![](images/9c4674472d84dcefae577e4283cf37bbe0a308f1e2208567d89c9a48caf87957.jpg)  
Figure 9.2.1. Secant method. Extrapolation or interpolation lines (dashed) are drawn through the two most recently evaluated points, whether or not they bracket the function. The points are numbered in the order that they are used.

![](images/158439ee96f87291f4bdb0106717fd5d60dc1b176bdf891ae34ecdf73d3e9c23.jpg)  
Figure 9.2.2. False-position method. Interpolation lines (dashed) are drawn through the most recent points that bracket the root. In this example, point 1 thus remains “active” for many steps. False position converges less rapidly than the secant method, but it is more certain.

![](images/419b089202f3a300c5b96880a99cc39e4ca142ad93dbc3d213dfcf91f376b0da.jpg)  
Figure 9.2.3. Example where both the secant and false-position methods will take many iterations to arrive at the true root. This function would be difficult for many other root-finding methods.

# template <class T>

Doub rtflsp(T &func, const Doub x1, const Doub x2, const Doub xacc) { Using the false-position method, return the root of a function or functor func known to lie between x1 and $\tt x 2$ . The root is refined until its accuracy is ˙xacc.

const Int MAXIT $\mathtt { . = } 3 0$ ; Set to the maximum allowed number of iterations.   
Doub xl,xh,del;   
Doub fl=func(x1);   
Doub fh func(x2); Be sure the interval brackets a root.   
if (fl\*fh $> 0 . 0 \dot { . }$ ) throw("Root must be bracketed in rtflsp");   
if $( \pm 1 < 0 . 0 )$ ) { Identify the limits so that xl corresponds to the low $\tt x 1 = \tt x 1$ ; side. xh $\scriptstyle = \mathtt { x } 2$ ;   
} else { $\tt x 1 = \tt x 2$ ; xh $\scriptstyle = \mathtt { x 1 }$ ; SWAP(fl,fh);   
Doub dx=xh-xl;   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<MAXIT;j++) { False-position loop. Doub rtf $=$ xl+dx\*fl/(fl-fh); Increment with respect to latest value. Doub f=func(rtf); if $\mathit { \Omega } , \mathit { \Phi } , \mathit { \Phi } , 0 , 0 ,$ ) { Replace appropriate limit. del=xl-rtf; xl=rtf; fl=f; } else { del=xh-rtf; xh=rtf; $\operatorname { f h } = \operatorname { f }$ ; dx=xh-xl; if (abs(del) $<$ xacc || $\mathrm { ~ \\underline ~ { ~ f ~ } ~ } = = \mathrm { ~ \ 0 ~ . 0 ~ } ,$ ) return rtf; Convergence.

throw("Maximum number of iterations exceeded in rtflsp");

template <class T>   
Doub rtsec(T &func, const Doub x1, const Doub x2, const Doub xacc) {   
Using the secant method, return the root of a function or functor func thought to lie between x1 and $\mathbf { x } 2$ . The root is refined until its accuracy is ˙xacc.   
const Int MAXIT $\scriptstyle = 3 0$ ; Maximum allowed number of iterations.   
Doub xl,rts;   
Doub fl=func(x1);   
Doub $\mathtt { f } =$ func(x2);   
if (abs(fl) $<$ abs(f)) Pick the bound with the smaller function value a rts=x1; the most recent guess. $\tt x 1 = \tt x 2$ ; SWAP(fl,f); else { xl=x1; rts=x2;   
}   
for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<MAXIT;j++) { Secant loop. Doub dx (xl-rts)\*f/(f-fl); Increment with respect to latest value. xl=rts; $\pounds 1 = \pounds$ ; rts $+ =$ dx; $\mathtt { f } =$ func(rts); if (abs(dx) < xacc || $\textbf { f } = = \textbf { 0 } . 0$ ) return rts; Convergence.   
}   
throw("Maximum number of iterations exceeded in rtsec");

# 9.2.1 Ridders' Method

A powerful variant on false position is due to Ridders [1]. When a root is bracketed between $x _ { 1 }$ and $x _ { 2 }$ , Ridders’ method first evaluates the function at the midpoint $x _ { 3 } = ( x _ { 1 } + x _ { 2 } ) / 2$ . It then factors out that unique exponential function that turns the residual function into a straight line. Specifically, it solves for a factor $e ^ { \boldsymbol { Q } }$ that gives

$$
f ( x _ { 1 } ) - 2 f ( x _ { 3 } ) e ^ { Q } + f ( x _ { 2 } ) e ^ { 2 Q } = 0
$$

This is a quadratic equation in $e ^ { \boldsymbol { Q } }$ , which can be solved to give

$$
e ^ { Q } = { \frac { f ( x _ { 3 } ) + \mathrm { s i g n } [ f ( x _ { 2 } ) ] \sqrt { f ( x _ { 3 } ) ^ { 2 } - f ( x _ { 1 } ) f ( x _ { 2 } ) } } { f ( x _ { 2 } ) } }
$$

Now the false-position method is applied, not to the values $f ( x _ { 1 } ) , f ( x _ { 3 } ) , f ( x _ { 2 } )$ , but to the values $\bar { f } ( x _ { 1 } ) , f ( x _ { 3 } ) e ^ { Q } , f ( x _ { 2 } ) e ^ { 2 Q }$ , yielding a new guess for the root, $x _ { 4 }$ . The overall updating formula (incorporating the solution 9.2.3) is

$$
x _ { 4 } = x _ { 3 } + ( x _ { 3 } - x _ { 1 } ) \frac { \mathrm { s i g n } [ f ( x _ { 1 } ) - f ( x _ { 2 } ) ] f ( x _ { 3 } ) } { \sqrt { f ( x _ { 3 } ) ^ { 2 } - f ( x _ { 1 } ) f ( x _ { 2 } ) } }
$$

Equation (9.2.4) has some very nice properties. First, $x _ { 4 }$ is guaranteed to lie in the interval $( x _ { 1 } , x _ { 2 } )$ , so the method never jumps out of its brackets. Second, the convergence of successive applications of equation (9.2.4) is quadratic, that is, $m = 2$ in equation (9.1.4). Since each application of (9.2.4) requires two function evaluations, the actual order of the method is $\sqrt { 2 }$ , not 2; but this is still quite respectably superlinear: The number of significant digits in the answer approximately doubles with each two function evaluations. Third, taking out the function’s “bend” via exponential (that is, ratio) factors, rather than via a polynomial technique (e.g., fitting a parabola), turns out to give an extraordinarily robust algorithm. In both reliability and speed, Ridders’ method is generally competitive with the more highly developed and better established (but more complicated) method of van Wijngaarden, Dekker, and Brent, which we next discuss.

# template <class $\mathrm { T } >$

Doub zriddr(T &func, const Doub x1, const Doub x2, const Doub xacc) { Using Ridders’ method, return the root of a function or functor func known to lie between x1 and $\mathbf { x } 2$ . The root will be refined to an approximate accuracy xacc.

const Int MAXIT $_ { - } = 6 0$ ;   
Doub fl=func(x1);   
Doub fh $\cdot ^ { = }$ func(x2);   
if ( $( \mathbf { f } 1 > 0 . 0$ && fh $< ~ 0 . 0$ ) || (fl < 0.0 && fh > 0.0)) Doub $\tt x l = \tt x l$ ; Doub xh $\scriptstyle 1 = \mathbf { x } 2$ ; Doub ans $=$ -9.99e99; Any highly unlikely value, to simplify logic for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<MAXIT; $\mathrm { i } + +$ ) { below. Doub xm=0.5\*(xl+xh); Doub fm $_ { 1 } =$ func(xm); First of two function evaluations per it-Doub $\mathtt { s } =$ sqrt(fm\*fm-fl\*fh); eration. if ( $\mathrm { ~ s ~ } = = \mathrm { ~ 0 ~ . ~ 0 ~ }$ ) return ans; Doub xnew $\scriptstyle \mathbf { \lambda } = \mathbf { x m } + ( \mathbf { x m } - \mathbf { x } \mathbf { 1 } ) * ( ( \mathbf { f } \mathbf { 1 } \ \mathbf { \lambda } > \mathbf { \lambda } \mathbf { f h } \ \overset { ? } { \mid } \ 1 . 0 \ \ : \ \mathbf { \lambda } - \mathbf { 1 } . 0 ) * \mathbf { f m } / \mathbf { s } ) \ ;$ Updating formula if (abs(xnew-ans) $< =$ xacc) return ans; ans=xnew; Doub fnew=func(ans); Second of two function evaluations per if (fnew $\scriptstyle = = \ 0 . 0 { \mathrm { . } }$ ) return ans; iteration. if (SIGN(fm,fnew) $: = ~ \mathtt { f m } .$ ) { Bookkeeping to keep the root bracketed $\tt x l = \tt x m$ ; on next iteration. fl=fm; xh=ans; fh=fnew; } else if (SIGN(fl,fnew) $! =$ fl) { xh=ans; fh=fnew; } else if (SIGN(fh,fnew) $\downarrow =$ fh) { xl=ans; fl=fnew; } else throw("never get here."); if (abs(xh-xl) $< =$ xacc) return ans; } throw("zriddr exceed maximum iterations");   
}   
else { if ( $\mathrm { ~  ~ \ell ~ } _ { , \pm 1 } = = \mathrm { ~  ~ 0 ~ } _ { , 0 } ,$ ) return x1; if $\mathrm { { ( f h ~ = = ~ 0 . 0 } }$ ) return x2; throw("root must be bracketed in zriddr.");   
}

# CITED REFERENCES AND FURTHER READING:

Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), $\ S 8 . 3$ .

Ostrowski, A.M. 1966, Solutions of Equations and Systems of Equations, 2nd ed. (New York: Academic Press), Chapter 12.   
Ridders, C.J.F. 1979, “A New Algorithm for Computing a Single Root of a Real Continuous Function,” IEEE Transactions on Circuits and Systems, vol. CAS-26, pp. 979–980.[1]

# 9.3 Van Wijngaarden-Dekker-Brent Method

While secant and false position formally converge faster than bisection, one finds in practice pathological functions for which bisection converges more rapidly. These can be choppy, discontinuous functions, or even smooth functions if the second derivative changes sharply near the root. Bisection always halves the interval, while secant and false position can sometimes spend many cycles slowly pulling distant bounds closer to a root. Ridders’ method does a much better job, but it too can sometimes be fooled. Is there a way to combine superlinear convergence with the sureness of bisection?

Yes. We can keep track of whether a supposedly superlinear method is actually converging the way it is supposed to, and, if it is not, we can intersperse bisection steps so as to guarantee at least linear convergence. This kind of super-strategy requires attention to bookkeeping detail, and also careful consideration of how roundoff errors can affect the guiding strategy. Also, we must be able to determine reliably when convergence has been achieved.

An excellent algorithm that pays close attention to these matters was developed in the 1960s by van Wijngaarden, Dekker, and others at the Mathematical Center in Amsterdam, and later improved by Brent [1]. For brevity, we refer to the final form of the algorithm as Brent’s method. The method is guaranteed (by Brent) to converge, so long as the function can be evaluated within the initial interval known to contain a root.

Brent’s method combines root bracketing, bisection, and inverse quadratic interpolation to converge from the neighborhood of a zero crossing. While the falseposition and secant methods assume approximately linear behavior between two prior root estimates, inverse quadratic interpolation uses three prior points to fit an inverse quadratic function ( $x$ as a quadratic function of $y$ ) whose value at $y = 0$ is taken as the next estimate of the root $x$ . Of course one must have contingency plans for what to do if the root falls outside of the brackets. Brent’s method takes care of all that. If the three point pairs are $[ a , f ( a ) ] , [ b , f ( b ) ] , [ c , f ( c ) ]$ , then the interpolation formula (cf. equation 3.2.1) is

$$
\begin{array} { l } { \displaystyle { x = \frac { [ y - f ( a ) ] [ y - f ( b ) ] c } { [ f ( c ) - f ( a ) ] [ f ( c ) - f ( b ) ] } + \frac { [ y - f ( b ) ] [ y - f ( c ) ] a } { [ f ( a ) - f ( b ) ] [ f ( a ) - f ( c ) ] } } } \\ { \displaystyle { + \frac { [ y - f ( c ) ] [ y - f ( a ) ] b } { [ f ( b ) - f ( c ) ] [ f ( b ) - f ( a ) ] } } } \end{array}
$$

Setting $y$ to zero gives a result for the next root estimate, which can be written as

$$
x = b + P / Q
$$

where, in terms of

$$
R \equiv f ( b ) / f ( c ) , \qquad S \equiv f ( b ) / f ( a ) , \qquad T \equiv f ( a ) / f ( c )
$$

we have

$$
\begin{array} { l } { P = S \left[ T ( R - T ) ( c - b ) - ( 1 - R ) ( b - a ) \right] } \\ { Q = ( T - 1 ) ( R - 1 ) ( S - 1 ) } \end{array}
$$

In practice $b$ is the current best estimate of the root and $P / Q$ ought to be a “small” correction. Quadratic methods work well only when the function behaves smoothly; they run the serious risk of giving very bad estimates of the next root or causing machine failure by an inappropriate division by a very small number ( $Q \approx 0 ,$ . Brent’s method guards against this problem by maintaining brackets on the root and checking where the interpolation would land before carrying out the division. When the correction $P / Q$ would not land within the bounds, or when the bounds are not collapsing rapidly enough, the algorithm takes a bisection step. Thus, Brent’s method combines the sureness of bisection with the speed of a higher-order method when appropriate. We recommend it as the method of choice for general one-dimensional root finding where a function’s values only (and not its derivative or functional form) are available.

# template <class $\mathrm { T } >$

Doub zbrent(T &func, const Doub x1, const Doub x2, const Doub tol)   
Using Brent’s method, return the root of a function or functor func known to lie between x1 and $\mathbf { x } 2$ . The root will be refined until its accuracy is tol.   
{   
const Int ITMAX $\cdot ^ { = }$ 100; Maximum allowed number of iterations.   
const Doub EPS $=$ numeric_limits<Doub>::epsilon();   
Machine floating-point precision.   
Doub a=x1,b=x2, ${ \tt c } = { \tt x } 2$ ,d,e,fa=func(a),fb $=$ func(b),fc,p,q,r,s,tol1,xm;   
if ( $\mathrm { ( f a ~ > ~ 0 . 0 ~ }$ && fb $> ~ 0 . 0$ ) || (fa $<$ 0.0 && fb $< 0 . 0 )$ ) throw("Root must be bracketed in zbrent");   
fc=fb;   
for (Int iter ${ \tt = } 0$ ;iter<ITMAX;iter++) { if ((fb $>$ 0.0 && fc $>$ 0.0) || (fb < 0.0 && fc < 0.0)) { $\mathtt { c } = \mathtt { a }$ ; Rename a, b, c and adjust bounding interva fc=fa; d. e=d=b-a; } if (abs(fc) < abs(fb)) { a=b; $\mathtt { b } = _ { \mathtt { C } }$ ; $\mathtt { c } = \mathtt { a }$ ; fa fb; fb=fc; fc=fa; } tol1 $^ { - 2 }$ .0\*EPS\*abs(b) $+ 0$ .5\*tol; Convergence check. xm=0.5\*(c-b); if (abs(xm) $< =$ tol1 || fb $\mathrm { = = } \ 0 . 0$ ) return b; if (abs(e) $> =$ tol1 && abs(fa) $>$ abs(fb)) { s=fb/fa; Attempt inverse quadratic interpolation. if ( $a ~ = = ~ c$ ) { p=2.0\*xm\*s; q=1.0-s; } else { q=fa/fc; r=fb/fc; p=s\*(2.0\*xm\*q\*(q-r)-(b-a)\*(r-1.0)); q=(q-1.0)\*(r-1.0)\*(s-1.0); } if $\mathrm { ( p ~ > ~ 0 . 0 } ) ,$ ) q = -q; Check whether in bounds. p=abs(p);

Doub min1 $\mathtt { . 3 }$ .0\*xm\*q-abs(tol1\*q); Doub min2 $\cdot =$ abs(e\*q); if (2.0\*p < (min1 $<$ min2 ? min1 : min2)) { e=d; Accept interpolation. d=p/q; } else { d=xm; Interpolation failed, use bisection. e=d; } } else { Bounds decreasing too slowly, use bisection. d=xm; e=d; } a=b; Move last best guess to a. fa=fb; if (abs(d) $>$ tol1) Evaluate new trial root. b $+ =$ d; else b $+ =$ SIGN(tol1,xm); fb=func(b); } throw("Maximum number of iterations exceeded in zbrent");

# CITED REFERENCES AND FURTHER READING:

Brent, R.P. 1973, Algorithms for Minimization without Derivatives (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2002 (New York: Dover), Chapters 3, 4.[1]   
Forsythe, G.E., Malcolm, M.A., and Moler, C.B. 1977, Computer Methods for Mathematical Computations (Englewood Cliffs,NJ: Prentice-Hall), $\ S 7 . 2$ .

# 9.4 Newton-Raphson Method Using Derivative

Perhaps the most celebrated of all one-dimensional root-finding routines is Newton’s method, also called the Newton-Raphson method. Joseph Raphson (1648– 1715) was a contemporary of Newton who independently invented the method in 1690, some 20 years after Newton did, but some 20 years before Newton actually published it. This method is distinguished from the methods of previous sections by the fact that it requires the evaluation of both the function $f ( x )$ and the derivative $f ^ { \prime } ( x )$ , at arbitrary points $x$ . The Newton-Raphson formula consists geometrically of extending the tangent line at a current point $x _ { i }$ until it crosses zero, then setting the next guess $x _ { i + 1 }$ to the abscissa of that zero crossing (see Figure 9.4.1). Algebraically, the method derives from the familiar Taylor series expansion of a function in the neighborhood of a point,

$$
f ( x + \delta ) \approx f ( x ) + f ^ { \prime } ( x ) \delta + { \frac { f ^ { \prime \prime } ( x ) } { 2 } } \delta ^ { 2 } + \cdots
$$

For small enough values of $\delta$ , and for well-behaved functions, the terms beyond linear are unimportant, hence $f ( x + \delta ) = 0$ implies

$$
\delta = - \frac { f ( x ) } { f ^ { \prime } ( x ) }
$$

![](images/f5daa2a77fbfe8d31869e5a6171f3ef7f94926bf64db45b5abdc754c321b7289.jpg)  
Figure 9.4.1. Newton’s method extrapolates the local derivative to find the next estimate of the root. In this example it works well and converges quadratically.

Newton-Raphson is not restricted to one dimension. The method readily generalizes to multiple dimensions, as we shall see in $\ S 9 . 6$ and $\ S 9 . 7$ , below.

Far from a root, where the higher-order terms in the series are important, the Newton-Raphson formula can give grossly inaccurate, meaningless corrections. For instance, the initial guess for the root might be so far from the true root as to let the search interval include a local maximum or minimum of the function. This can be death to the method (see Figure 9.4.2). If an iteration places a trial guess near such a local extremum, so that the first derivative nearly vanishes, then Newton-Raphson sends its solution off to limbo, with vanishingly small hope of recovery. Figure 9.4.3 demonstrates another possible pathology.

Why is Newton-Raphson so powerful? The answer is its rate of convergence: Within a small distance $\epsilon$ of $x$ , the function and its derivative are approximately

$$
\begin{array} { l } { { f ( x + \epsilon ) = f ( x ) + \epsilon f ^ { \prime } ( x ) + \epsilon ^ { 2 } \displaystyle \frac { f ^ { \prime \prime } ( x ) } { 2 } + \cdots , } } \\ { { f ^ { \prime } ( x + \epsilon ) = f ^ { \prime } ( x ) + \epsilon f ^ { \prime \prime } ( x ) + \cdots } } \end{array}
$$

By the Newton-Raphson formula,

$$
x _ { i + 1 } = x _ { i } - { \frac { f ( x _ { i } ) } { f ^ { \prime } ( x _ { i } ) } }
$$

so that

$$
\epsilon _ { i + 1 } = \epsilon _ { i } - \frac { f ( x _ { i } ) } { f ^ { \prime } ( x _ { i } ) }
$$

![](images/847c1bc26105317049f229e2b32415f9721eb4620872f497663abc48dbec82ee.jpg)  
Figure 9.4.2. Unfortunate case where Newton’s method encounters a local extremum and shoots off to outer space. Here bracketing bounds, as in rtsafe, would save the day.

![](images/d5750adcb1abd1453aa91b046ab0c7fa7b2a1497a810745f4a0cf279a3e24f87.jpg)  
Figure 9.4.3. Unfortunate case where Newton’s method enters a nonconvergent cycle. This behavior is often encountered when the function $f$ is obtained, in whole or in part, by table interpolation. With a better initial guess, the method would have succeeded.

When a trial solution $x _ { i }$ differs from the true root by $\epsilon _ { i }$ , we can use (9.4.3) to express $f ( x _ { i } )$ ; $f ^ { \prime } ( x _ { i } )$ in (9.4.4) in terms of $\epsilon _ { i }$ and derivatives at the root itself. The result is a recurrence relation for the deviations of the trial solutions

$$
\epsilon _ { i + 1 } = - \epsilon _ { i } ^ { 2 } \frac { f ^ { \prime \prime } ( x ) } { 2 f ^ { \prime } ( x ) }
$$

Equation (9.4.6) says that Newton-Raphson converges quadratically (cf. equation 9.2.3). Near a root, the number of significant digits approximately doubles with each step. This very strong convergence property makes Newton-Raphson the method of choice for any function whose derivative can be evaluated efficiently, and whose derivative is continuous and nonzero in the neighborhood of a root.

Even where Newton-Raphson is rejected for the early stages of convergence (because of its poor global convergence properties), it is very common to “polish up” a root with one or two steps of Newton-Raphson, which can multiply by two or four its number of significant figures.

For an efficient realization of Newton-Raphson, the user provides a routine that evaluates both $f ( x )$ and its first derivative $f ^ { \prime } ( x )$ at the point $x$ . The Newton-Raphson formula can also be applied using a numerical difference to approximate the true local derivative,

$$
f ^ { \prime } ( x ) \approx { \frac { f ( x + d x ) - f ( x ) } { d x } }
$$

This is not, however, a recommended procedure for the following reasons: (i) You are doing two function evaluations per step, so at best the superlinear order of convergence will be only $\sqrt { 2 }$ . (ii) If you take $d x$ too small, you will be wiped out by roundoff, while if you take it too large, your order of convergence will be only linear, no better than using the initial evaluation $f ^ { \prime } ( x _ { 0 } )$ for all subsequent steps. Therefore, Newton-Raphson with numerical derivatives is (in one dimension) always dominated by Brent’s method (-9.3). (In multidimensions, where there is a paucity of available methods, Newton-Raphson with numerical derivatives must be taken more seriously. See $\ S 9 . 6 - \ S 9 . 7 . )$

The following routine invokes a user-supplied structure that supplies the function value and the derivative. The function value is returned in the usual way as a functor by overloading operator(), while the derivative is returned by the df function in the structure. For example, to find a root of the Bessel function $J _ { 0 } ( x )$ (derivative $- J _ { 1 } ( x ) )$ you would have a structure like

struct Funcd { Bessjy bess; Doub operator() (const Doub x) { return bess.j0(x); } Doub df(const Doub x) { return -bess.j1(x); }   
};

(While you can use any name for Funcd, the name df is fixed.) Your code should then create an instance of this structure and pass it to rtnewt:

Funcd fx;   
Doub root=rtnewt(fx,x1,x2,xacc);

The routine rtnewt includes input bounds on the root $\tt x 1$ and $_ { \tt X 2 }$ simply to be consistent with previous root-finding routines: Newton does not adjust bounds, and works only on local information at the point x. The bounds are used only to pick the midpoint as the first guess, and to reject the solution if it wanders outside of the bounds.

# roots.h template <class T>

Doub rtnewt(T &funcd, const Doub x1, const Doub x2, const Doub xacc) {

Using the Newton-Raphson method, return the root of a function known to lie in the interval $[ \mathbf { x } \mathbf { 1 } , \mathbf { x } 2 ]$ . The root will be refined until its accuracy is known within ˙xacc. funcd is a usersupplied struct that returns the function value as a functor and the first derivative of the function at the point $\mathbf { x }$ as the function df (see text).

const Int JMAX $= 2 0$ ; Set to maximu   
Doub rtn $_ { = 0 }$ .5\*( $\bf { x } 1 + \bf { x } 2 )$ ; Initial guess.   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<JMAX; $\mathrm { j } + +$ ) { Doub $\mathtt { f } =$ funcd(rtn); Doub df=funcd.df(rtn); Doub dx=f/df; rtn $- =$ dx; if ((x1-rtn)\*(rtn-x2) < 0.0) throw("Jumped out of brackets in rtnewt"); if (abs(dx) $<$ xacc) return rtn; Convergence.   
}   
throw("Maximum number of iterations exceeded in rtnewt"

While Newton-Raphson’s global convergence properties are poor, it is fairly easy to design a fail-safe routine that utilizes a combination of bisection and Newton-Raphson. The hybrid algorithm takes a bisection step whenever Newton-Raphson would take the solution out of bounds, or whenever Newton-Raphson is not reducing the size of the brackets rapidly enough.

# roots.h template <class T>

Doub rtsafe(T &funcd, const Doub x1, const Doub x2, const Doub xacc) {

Using a combination of Newton-Raphson and bisection, return the root of a function bracketed between $\tt x 1$ and $\mathbf { x } 2$ . The root will be refined until its accuracy is known within ˙xacc. funcd is a user-supplied struct that returns the function value as a functor and the first derivative of the function at the point $\mathbf { x }$ as the function df (see text).

const Int MAXI $\scriptstyle \sum 1 0 0$ ; Maximum allowed number of iterations.   
Doub xh,xl;   
Doub fl=funcd $\mathbf { \Pi } ( \mathbf { x } \mathbf { 1 } )$ ;   
Doub fh=funcd(x2);   
if ( $( \mathbf { f } 1 > 0 . 0 $ && fh $> ~ 0 . 0 \dot { } ,$ ) || $( \pm 1 < 0 . 0$ && fh $< ~ 0 . 0 )$ ) throw("Root must be bracketed in rtsafe");   
if $\mathbf { \dot { f } } 1 \ = = \ 0 . 0 \mathbf { \dot { \Omega } }$ ) return x1;   
if ( $\mathrm { \Delta } \cdot \mathrm { I h } \ = = \ 0 . 0 \mathrm { \cdot }$ ) return x2;   
if ( $\mathbf { \dot { f } } 1 < 0 . 0 \dot { } \dot { }$ ) { Orient the search so that $f ( \mathbf { x } \mathbf { 1 } ) < \mathbf { 0 }$ . $\tt x l = \tt x l$ ; xh ${ \tt = } { \tt x } 2$ ;   
} else { xh=x1; $\tt x 1 = \tt x 2$ ;   
}   
Doub rts ${ = } 0$ .5\*(x1+x2); Initialize the guess for root,   
Doub dxold=abs(x2-x1); the “stepsize before last,”   
Doub dx=dxold; and the last step.   
Doub f=funcd(rts);   
Doub df $=$ funcd.df(rts);   
for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<MAXIT;j++) { Loop over allowed iterations. if ((((rts-xh)\*df-f)\*((rts-xl)\*df-f) $>$ 0.0) Bisect if Newton out of range, || (abs(2.0\*f) $>$ abs(dxold\*df))) { or not decreasing fast enough

dxold=dx; dx=0.5\*(xh-xl); rts=xl+dx; if (xl $= =$ rts) return rts; Change in root is negligible. } else { Newton step acceptable. Take it. dxold=dx; d $\mathord { \left. \kern - delimiterspace \right.} = \mathbf { f } $ /df; Doub temp=rts; rts $- =$ dx; if (temp $= =$ rts) return rts; if (abs(dx) $<$ xacc) return rts; Convergence criterion. Doub $\mathtt { f } =$ funcd(rts); Doub df=funcd.df(rts); The one new function evaluation per iteration. if $( \pm \ < \ 0 . 0 )$ ) Maintain the bracket on the root. xl=rts; else xh=rts; } throw("Maximum number of iterations exceeded in rtsafe");

For many functions, the derivative $f ^ { \prime } ( x )$ often converges to machine accuracy before the function $f ( x )$ itself does. When that is the case one need not subsequently update $f ^ { \prime } ( x )$ . This shortcut is recommended only when you confidently understand the generic behavior of your function, but it speeds computations when the derivative calculation is laborious. (Formally, this makes the convergence only linear, but if the derivative isn’t changing anyway, you can do no better.)

# 9.4.1 Newton-Raphson and Fractals

An interesting sidelight to our repeated warnings about Newton-Raphson’s unpredictable global convergence properties — its very rapid local convergence notwithstanding — is to investigate, for some particular equation, the set of starting values from which the method does, or doesn’t, converge to a root.

Consider the simple equation

$$
z ^ { 3 } - 1 = 0
$$

whose single real root is $z = 1$ , but which also has complex roots at the other two cube roots of unity, $\exp ( \pm 2 \pi i / 3 )$ . Newton’s method gives the iteration

$$
z _ { j + 1 } = z _ { j } - \frac { z _ { j } ^ { 3 } - 1 } { 3 z _ { j } ^ { 2 } }
$$

Up to now, we have applied an iteration like equation (9.4.9) only for real starting values $z _ { 0 }$ , but in fact all of the equations in this section also apply in the complex plane. We can therefore map out the complex plane into regions from which a starting value $z _ { 0 }$ , iterated in equation (9.4.9), will, or won’t, converge to $z = 1$ . Naively, we might expect to find a “basin of convergence” somehow surrounding the root $z = 1$ . We surely do not expect the basin of convergence to fill the whole plane, because the plane must also contain regions that converge to each of the two complex roots. In fact, by symmetry, the three regions must have identical shapes. Perhaps they will be three symmetric $1 2 0 ^ { \circ }$ wedges, with one root centered in each?

![](images/7e7359e4a158a3506a4a0fe9ffb4c2bc69f473953c7e8c6c27dcee477361e06e.jpg)  
Figure 9.4.4. The complex $z$ -plane with real and imaginary components in the range $( - 2 , 2 )$ . The black region is the set of points from which Newton’s method converges to the root $z = 1$ of the equation $z ^ { \tilde { 3 } } - 1 = 0$ . Its shape is fractal.

Now take a look at Figure 9.4.4, which shows the result of a numerical exploration. The basin of convergence does indeed cover $1 / 3$ the area of the complex plane, but its boundary is highly irregular — in fact, fractal. (A fractal, so called, has self-similar structure that repeats on all scales of magnification.) How does this fractal emerge from something as simple as Newton’s method and an equation as simple as (9.4.8)? The answer is already implicit in Figure 9.4.2, which showed how, on the real line, a local extremum causes Newton’s method to shoot off to infinity. Suppose one is slightly removed from such a point. Then one might be shot off not to infinity, but — by luck — right into the basin of convergence of the desired root. But that means that in the neighborhood of an extremum there must be a tiny, perhaps distorted, copy of the basin of convergence — a kind of “one-bounce away” copy. Similar logic shows that there can be “two-bounce” copies, “three-bounce” copies, and so on. A fractal thus emerges.

Notice that, for equation (9.4.8), almost the whole real axis is in the domain of convergence for the root $z = 1$ . We say “almost” because of the peculiar discrete points on the negative real axis whose convergence is indeterminate (see figure). What happens if you start Newton’s method from one of these points? (Try it.)

# 9.4.2 Halley's Method

Edmund Halley (1656–1742) was a contemporary and close friend of Newton. His contribution to root finding was to extend Newton’s method to use information from the next term in the (as we would now say it) Taylor series, the second derivative $f ^ { \prime \prime } ( x )$ . Omitting a straightforward derivation, the update formula (9.4.4) now becomes

$$
x _ { i + 1 } = x _ { i } - { \frac { f ( x _ { i } ) } { f ^ { \prime } ( x _ { i } ) \left( 1 - { \frac { f ( x _ { i } ) f ^ { \prime \prime } ( x _ { i } ) } { 2 f ^ { \prime } ( x _ { i } ) ^ { 2 } } } \right) } }
$$

You can see that the update scheme is essentially Newton-Raphson, but with an extra, hopefully small, correction term in the denominator.

It only makes sense to use Halley’s method when it is easy to calculate $f ^ { \prime \prime } ( x _ { i } )$ , often from pieces of functions that are already being used in calculating $f ( x _ { i } )$ and $f ^ { \prime } ( x _ { i } )$ . Otherwise, you might just as well do another step of ordinary Newton-Raphson. Halley’s method converges cubically; in the final convergence each iteration triples the number of significant digits. But two steps of Newton-Raphson quadruple that number.

There is no reason to think that the basin of convergence of Halley’s method is generally larger than Newton’s; more often it is probably smaller. So don’t look to Halley’s method for better convergence in the large.

Nevertheless, when you can get a second derivative almost for free, you can often usefully shave an iteration or two off Newton-Raphson by something like this,

$$
x _ { i + 1 } = x _ { i } - { \frac { f ( x _ { i } ) } { f ^ { \prime } ( x _ { i } ) } } { \Bigg / } \operatorname* { m a x } \left[ 0 . 8 , \operatorname* { m i n } \left( 1 . 2 , 1 - { \frac { f ( x _ { i } ) f ^ { \prime \prime } ( x _ { i } ) } { 2 f ^ { \prime } ( x _ { i } ) ^ { 2 } } } \right) \right]
$$

the idea being to limit the influence of the higher-order correction, so that it gets used only in the endgame. We have already used Halley’s method in just this fashion in $\ S 6 . 2 , \ S 6 . 4$ , and $\ S 6 . 1 4$ .

# CITED REFERENCES AND FURTHER READING:

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), Chapter 2.   
Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), $\ S 8 . 4$ .   
Ortega, J., and Rheinboldt, W. 1970, Iterative Solution of Nonlinear Equations in Several Variables (New York: Academic Press); reprinted 20oo (Philadelphia: S.I.A.M.).   
Mandelbrot, B.B. 1983, The Fractal Geometry of Nature (San Francisco: W.H. Freeman).   
Peitgen, H.-O., and Saupe, D. (eds.) 1988, The Science of Fractal Images (New York: Springer).

# 9.5 Roots of Polynomials

Here we give a few methods for finding roots of polynomials. These will serve for most practical problems involving polynomials of low-to-moderate degree or for well-conditioned polynomials of higher degree. Not as well appreciated as it ought to be is the fact that some polynomials are exceedingly ill-conditioned. The tiniest changes in a polynomial’s coefficients can, in the worst case, send its roots sprawling all over the complex plane. (An infamous example due to Wilkinson is detailed by Acton [1].)

Recall that a polynomial of degree $n$ will have $n$ roots. The roots can be real or complex, and they might not be distinct. If the coefficients of the polynomial are real, then complex roots will occur in pairs that are conjugate; i.e., if $x _ { 1 } = a + b i$ is a root, then $x _ { 2 } = a - b i$ will also be a root. When the coefficients are complex, the complex roots need not be related.

Multiple roots, or closely spaced roots, produce the most difficulty for numerical algorithms (see Figure 9.5.1). For example, $P ( x ) = ( x - a ) ^ { 2 }$ has a double real root at $x = a$ . However, we cannot bracket the root by the usual technique of identifying neighborhoods where the function changes sign, nor will slope-following methods such as Newton-Raphson work well, because both the function and its derivative vanish at a multiple root. Newton-Raphson may work, but slowly, since large roundoff errors can occur. When a root is known in advance to be multiple, then special methods of attack are readily devised. Problems arise when (as is generally the case) we do not know in advance what pathology a root will display.

# 9.5.1 Deflation of Polynomials

When seeking several or all roots of a polynomial, the total effort can be significantly reduced by the use of deflation. As each root $r$ is found, the polynomial is factored into a product involving the root and a reduced polynomial of degree one less than the original, i.e., $P ( x ) = ( x - r ) Q ( x )$ . Since the roots of $Q$ are exactly the remaining roots of $P$ , the effort of finding additional roots decreases, because we work with polynomials of lower and lower degree as we find successive roots. Even more important, with deflation we can avoid the blunder of having our iterative method converge twice to the same (nonmultiple) root instead of separately to two different roots.

Deflation, which amounts to synthetic division, is a simple operation that acts on the array of polynomial coefficients. The concise code for synthetic division by a monomial factor was given in $\ S 5 . 1$ . You can deflate complex roots either by converting that code to complex data type, or else — in the case of a polynomial with real coefficients but possibly complex roots — by deflating by a quadratic factor,

$$
\left[ x - ( a + i b ) \right] \left[ x - ( a - i b ) \right] = x ^ { 2 } - 2 a x + ( a ^ { 2 } + b ^ { 2 } )
$$

The routine poldiv in $\ S 5 . 1$ can be used to divide the polynomial by this factor.

Deflation must, however, be utilized with care. Because each new root is known with only finite accuracy, errors creep into the determination of the coefficients of the successively deflated polynomial. Consequently, the roots can become more and more inaccurate. It matters a lot whether the inaccuracy creeps in stably (plus or minus a few multiples of the machine precision at each stage) or unstably (erosion of successive significant figures until the results become meaningless). Which behavior occurs depends on just how the root is divided out. Forward deflation, where the new polynomial coefficients are computed in the order from the highest power of $x$ down to the constant term, was illustrated in $\ S 5 . 1$ . This turns out to be stable if the root of smallest absolute value is divided out at each stage. Alternatively, one can do backward deflation, where new coefficients are computed in order from the constant term up to the coefficient of the highest power of $x$ . This is stable if the remaining root of largest absolute value is divided out at each stage.

![](images/3fe6e40161b1978d2878f9ed5c462b33a41a255857fab87dda81deb7fcb84cd8.jpg)  
Figure 9.5.1. (a) Linear, quadratic, and cubic behavior at the roots of polynomials. Only under high magnification (b) does it become apparent that the cubic has one, not three, roots, and that the quadratic has two roots rather than none.

A polynomial whose coefficients are interchanged “end-to-end,” so that the constant becomes the highest coefficient, etc., has its roots mapped into their reciprocals. (Proof: Divide the whole polynomial by its highest power $x ^ { n }$ and rewrite it as a polynomial in $1 / x$ .) The algorithm for backward deflation is therefore virtually identical to that of forward deflation, except that the original coefficients are taken in reverse order and the reciprocal of the deflating root is used. Since we will use forward deflation below, we leave to you the exercise of writing a concise coding for backward deflation (as in $\ S 5 . 1 )$ . For more on the stability of deflation, consult [2].

To minimize the impact of increasing errors (even stable ones) when using deflation, it is advisable to treat roots of the successively deflated polynomials as only tentative roots of the original polynomial. One then polishes these tentative roots by taking them as initial guesses that are to be re-solved for, using the nondeflated original polynomial $P$ . Again you must beware lest two deflated roots are inaccurate enough that, under polishing, they both converge to the same undeflated root; in that case you gain a spurious root multiplicity and lose a distinct root. This is detectable, since you can compare each polished root for equality to previous ones from distinct tentative roots. When it happens, you are advised to deflate the polynomial just once (and for this root only), then again polish the tentative root, or use Maehly’s procedure (see equation 9.5.29 below).

Below we say more about techniques for polishing real and complex-conjugate tentative roots. First, let’s get back to overall strategy.

There are two schools of thought about how to proceed when faced with a polynomial of real coefficients. One school says to go after the easiest quarry, the real, distinct roots, by the same kinds of methods that we have discussed in previous sections for general functions, i.e., trial-and-error bracketing followed by a safe Newton-

Raphson as in rtsafe. Sometimes you are only interested in real roots, in which case the strategy is complete. Otherwise, you then go after quadratic factors of the form (9.5.1) by any of a variety of methods. One such is Bairstow’s method, which we will discuss below in the context of root polishing. Another is Muller’s method, which we here briefly discuss.

# 9.5.2 Muller's Method

Muller’s method generalizes the secant method but uses quadratic interpolation among three points instead of linear interpolation between two. Solving for the zeros of the quadratic allows the method to find complex pairs of roots. Given three previous guesses for the root $x _ { i - 2 }$ , $x _ { i - 1 }$ , $x _ { i }$ , and the values of the polynomial $P ( x )$ at those points, the next approximation $x _ { i + 1 }$ is produced by the following formulas,

$$
\begin{array} { l } { q \equiv \frac { x _ { i } - x _ { i - 1 } } { x _ { i - 1 } - x _ { i - 2 } } } \\ { A \equiv q P ( x _ { i } ) - q ( 1 + q ) P ( x _ { i - 1 } ) + q ^ { 2 } P ( x _ { i - 2 } ) } \\ { B \equiv ( 2 q + 1 ) P ( x _ { i } ) - ( 1 + q ) ^ { 2 } P ( x _ { i - 1 } ) + q ^ { 2 } P ( x _ { i - 2 } ) } \\ { C \equiv ( 1 + q ) P ( x _ { i } ) } \end{array}
$$

followed by

$$
x _ { i + 1 } = x _ { i } - ( x _ { i } - x _ { i - 1 } ) \frac { 2 C } { B \pm \sqrt { B ^ { 2 } - 4 A C } }
$$

where the sign in the denominator is chosen to make its absolute value or modulus as large as possible. You can start the iterations with any three values of $x$ that you like, e.g., three equally spaced values on the real axis. Note that you must allow for the possibility of a complex denominator, and subsequent complex arithmetic, in implementing the method.

Muller’s method is sometimes also used for finding complex zeros of analytic functions (not just polynomials) in the complex plane, for example in the IMSL routine ZANLY [3].

# 9.5.3 Laguerre's Method

The second school regarding overall strategy happens to be the one to which we belong. That school advises you to use one of a very small number of methods that will converge (though with greater or lesser efficiency) to all types of roots: real, complex, single, or multiple. Use such a method to get tentative values for all $n$ roots of your nth degree polynomial. Then go back and polish them as you desire.

Laguerre’s method is by far the most straightforward of these general, complex methods. It does require complex arithmetic, even while converging to real roots; however, for polynomials with all real roots, it is guaranteed to converge to a root from any starting point. For polynomials with some complex roots, little is theoretically proved about the method’s convergence. Much empirical experience, however, suggests that nonconvergence is extremely unusual and, further, can almost always be fixed by a simple scheme to break a nonconverging limit cycle. (This is implemented in our routine below.) An example of a polynomial that requires this cycle-breaking scheme is one of high degree $( \gtrsim 2 0 )$ , with all its roots just outside of