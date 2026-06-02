$\epsilon$ . For $N = 1 4$ , and a certain set of $c$ ’s and $\gamma$ (calculated by P. Godfrey), the error is smaller than $| \epsilon | < 1 0 ^ { - 1 5 }$ . Even more impressive is the fact that, with these same constants, the formula (6.1.5) applies for the complex gamma function, everywhere in the half complex plane Re $z > 0$ , achieving almost the same accuracy as on the real line.

It is better to implement $\ln \Gamma ( x )$ than $\Gamma ( x )$ , since the latter will overflow at quite modest values of $x$ . Often the gamma function is used in calculations where the large values of $\Gamma ( x )$ are divided by other large numbers, with the result being a perfectly ordinary value. Such operations would normally be coded as subtraction of logarithms. With (6.1.5) in hand, we can compute the logarithm of the gamma function with two calls to a logarithm and a few dozen arithmetic operations. This makes it not much more difficult than other built-in functions that we take for granted, such as sin $x$ or $e ^ { x }$ :

Doub gammln(const Doub xx) {   
Returns the value $\ln [ \Gamma ( \mathbf { x x } ) ]$ for $\mathbf { x x } > \mathbf { 0 }$ . Int j; Doub x,tmp,y,ser; static const Doub cof[14] $=$ {57.1562356658629235,-59.5979603554754912, 14.1360979747417471,-0.491913816097620199,.339946499848118887e-4, .465236289270485756e-4,-.983744753048795646e-4,.158088703224912494e-3, -.210264441724104883e-3,.217439618115212643e-3,-.164318106536763890e-3, .844182239838527433e-4,-.261908384015814087e-4,.368991826595316234e-5}; if (xx $\mathit { \Theta } < = \mathit { \Theta } 0 .$ ) throw("bad arg in gammln"); $\mathbf { y } = \mathbf { x } = \mathbf { x } \mathbf { x }$ ; tmp $= \ x + 5$ .24218750000000000; Rational 671/128. tmp $=$ ( $\mathbf { \boldsymbol { x } } { + } 0$ .5)\*log(tmp)-tmp; ser $=$ 0.999999999999997092; for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<14;j $^ { + + }$ ) ser $+ =$ cof[j]/++y; return tmp+log(2.5066282746310005\*ser/x);   
}

How shall we write a routine for the factorial function $n ! 2$ Generally the factorial function will be called for small integer values, and in most applications the same integer value will be called for many times. It is obviously inefficient to call $\exp ( \mathrm { g a m m l n } ( \mathbf { n } + 1 . ) )$ for each required factorial. Better is to initialize a static table on the first call, and do a fast lookup on subsequent calls. The fixed size 171 for the table is because 170Š is representable as an IEEE double precision value, but 171Š overflows. It is also sometimes useful to know that factorials up to 22Š have exact double precision representations (52 bits of mantissa, not counting powers of two that are absorbed into the exponent), while 23Š and above are represented only approximately.

# gamma.h

Doub factrl(const Int n) {   
Returns the value nŠ as a floating-point number. static VecDoub a(171); static Bool init=true; if (init) { init $=$ false; $\mathrm { a } \left[ 0 \right] ~ = ~ 1 . ~ ;$ ; for (Int i=1;i<171;i++) a[i] $=$ i\*a[i-1]; } if (n < 0 || n > 170) throw("factrl out of range"); return a[n];

More useful in practice is a function returning the log of a factorial, which doesn’t have overflow issues. The size of the table of logarithms is whatever you can afford in space and initialization time. The value $\mathtt { N T O P } = 2 0 0 0$ should be increased if your integer arguments are often larger.

# gamma.h

Doub factln(const Int n) {Returns ln.nŠ/.

static const Int NTOP $^ { \prime } =$ 2000;   
static VecDoub a(NTOP);   
static Bool init=true;   
if (init) { init $=$ false; for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<NTOP; $\Dot { \ b { 1 } } + +$ ) a[i] $=$ gammln(i+1.);   
}   
if $\mathbf { \Omega } _ { \mathbf { \lambda } } \mathbf { \hat { n } \Sigma } < \mathbf { \Omega } 0 \mathbf { \dot { \Omega } } .$ ) throw("negative arg in factln");   
if $\mathrm { ~ \textit ~ { ~ a ~ } ~ } <$ NTOP) return a[n];   
return gammln $( \mathtt { n } + 1 . )$ ; Out of range of table.

}

The binomial coefficient is defined by

$$
{ \binom { n } { k } } = { \frac { n ! } { k ! ( n - k ) ! } } \qquad 0 \leq k \leq n
$$

A routine that takes advantage of the tables stored in factrl and factln is

Doub bico(const Int n, const Int k) {

Returns the binomial coefficient $\textstyle { \binom { n } { k } }$ as a floating-point number.

if (n<0 || $\mathtt { k } < 0$ || k>n) throw("bad args in bico");   
if ( $\scriptstyle \mathtt { n } < 1 7 1 $ ) return floor(0.5+factrl(n)/(factrl(k)\*factrl(n-k)));   
return floor(0. $^ { 5 + }$ exp(factln(n)-factln(k)-factln(n-k)));

The floor function cleans up roundoff error for smaller values of $\mathbf { n }$ and k.

If your problem requires a series of related binomial coefficients, a good idea is to use recurrence relations, for example,

$$
{ \begin{array} { l } { \displaystyle { \binom { n + 1 } { k } } = { \frac { n + 1 } { n - k + 1 } } { \binom { n } { k } } = { \binom { n } { k } } + { \binom { n } { k - 1 } } } \\ { \displaystyle { \binom { n } { k + 1 } } = { \frac { n - k } { k + 1 } } { \binom { n } { k } } } \end{array} }
$$

Finally, turning away from the combinatorial functions with integer-valued arguments, we come to the beta function,

$$
B ( z , w ) = B ( w , z ) = \int _ { 0 } ^ { 1 } t ^ { z - 1 } ( 1 - t ) ^ { w - 1 } d t
$$

which is related to the gamma function by

$$
B ( z , w ) = { \frac { \Gamma ( z ) \Gamma ( w ) } { \Gamma ( z + w ) } }
$$

hence

Doub beta(const Doub z, const Doub w) { Returns the value of the beta function $B ( z , w )$ . return exp(gammln(z)+gammln(w)-gammln $( z + \pi )$ ); }

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapter 6.   
Lanczos, C. 1964, “A Precision Approximation of the Gamma Function,” SIAM Journal on Numerical Analysis,ser. B,vol.1,pp.86-96.[1]

# 6.2 Incomplete Gamma Function and Error Function

The incomplete gamma function is defined by

$$
P ( a , x ) \equiv \frac { \gamma ( a , x ) } { \Gamma ( a ) } \equiv \frac { 1 } { \Gamma ( a ) } \int _ { 0 } ^ { x } e ^ { - t } t ^ { a - 1 } d t \qquad ( a > 0 )
$$

It has the limiting values

$$
P ( a , 0 ) = 0 \qquad \mathrm { a n d } \qquad P ( a , \infty ) = 1
$$

The incomplete gamma function $P ( \boldsymbol { a } , \boldsymbol { x } )$ is monotonic and (for $a$ greater than one or so) rises from “near-zero” to “near-unity” in a range of $x$ centered on about $a - 1$ , and of width about $\sqrt { a }$ (see Figure 6.2.1).

The complement of $P ( \boldsymbol { a } , \boldsymbol { x } )$ is also confusingly called an incomplete gamma function,

$$
Q ( a , x ) \equiv 1 - P ( a , x ) \equiv \frac { \Gamma ( a , x ) } { \Gamma ( a ) } \equiv \frac { 1 } { \Gamma ( a ) } \int _ { x } ^ { \infty } e ^ { - t } t ^ { a - 1 } d t \qquad ( a > 0 )
$$

It has the limiting values

$$
\ Q ( a , 0 ) = 1 \qquad \mathrm { a n d } \qquad Q ( a , \infty ) = 0
$$

The notations $P ( a , x ) , \gamma ( a , x )$ , and $\Gamma ( a , x )$ are standard; the notation $Q ( a , x )$ is specific to this book.

There is a series development for $\gamma ( a , x )$ as follows:

$$
\gamma ( a , x ) = e ^ { - x } x ^ { a } \sum _ { n = 0 } ^ { \infty } \frac { \Gamma ( a ) } { \Gamma ( a + 1 + n ) } x ^ { n }
$$

One does not actually need to compute a new $\Gamma ( a + 1 + n )$ for each $n$ ; one rather uses equation (6.1.3) and the previous coefficient.

![](images/c20552309628f7ab821814fcd55d01476a945adaab277bd68eed882860956a95.jpg)  
Figure 6.2.1. The incomplete gamma function $P ( \boldsymbol a , x )$ for four values of $^ { a }$ .

A continued fraction development for $\Gamma ( a , x )$ is

$$
\Gamma ( a , x ) = e ^ { - x } x ^ { a } \left( { \frac { 1 } { x + } } { \frac { 1 - a } { 1 + } } { \frac { 1 } { x + } } { \frac { 2 - a } { 1 + } } { \frac { 2 } { x + } } \cdots \right) \qquad ( x > 0 )
$$

It is computationally better to use the even part of (6.2.6), which converges twice as fast (see $\ S 5 . 2 )$ :

$$
\Gamma ( a , x ) = e ^ { - x } x ^ { a } \left( { \frac { 1 } { x + 1 - a - } } { \frac { 1 \cdot ( 1 - a ) } { x + 3 - a - } } { \frac { 2 \cdot ( 2 - a ) } { x + 5 - a - } } \cdots \right) \qquad ( x > 0 )
$$

It turns out that (6.2.5) converges rapidly for $x$ less than about $a + 1$ , while (6.2.6) or (6.2.7) converges rapidly for $x$ greater than about $a + 1$ . In these respective regimes each requires at most a few times $\sqrt { a }$ terms to converge, and this many only near $x = a$ , where the incomplete gamma functions are varying most rapidly. For moderate values of $a$ , less than 100, say, (6.2.5) and (6.2.7) together allow evaluation of the function for all $x$ . An extra dividend is that we never need to compute a function value near zero by subtracting two nearly equal numbers.

Some applications require $P ( \boldsymbol { a } , \boldsymbol { x } )$ and $Q ( a , x )$ for much larger values of $a$ , where both the series and the continued fraction are inefficient. In this regime, however, the integrand in equation (6.2.1) falls off sharply in both directions from its peak, within a few times $\sqrt { a }$ . An efficient procedure is to evaluate the integral directly, with a single step of high-order Gauss-Legendre quadrature (-4.6) extending from $x$ just far enough into the nearest tail to achieve negligible values of the integrand. Actually it is “half a step,” because we need the dense abscissas only near $x$ , not far out on the tail where the integrand is effectively zero.

We package the various incomplete gamma parts into an object Gamma. The only persistent state is the value $\mathtt { g l n }$ , which is set to $\Gamma ( a )$ for the most recent call to $P ( \boldsymbol { a } , \boldsymbol { x } )$ or $Q ( a , x )$ . This is useful when you need a different normalization convention, for example $\gamma ( a , x )$ or $\Gamma ( a , x )$ in equations (6.2.1) or (6.2.3).

# struct Gamma : Gauleg18 {

Object for incomplete gamma function. Gauleg18 provides coefficients for Gauss-Legendre quadrature.

static const Int ASWITCH $\mathop {    }$ 100;   
static const Doub EPS;   
static const Doub FPMIN;   
Doub gln; When to switch to quadrature method.   
See end of struct for initializations.

Doub gammp(const Doub a, const Doub x) { Returns the incomplete gamma function $P ( { \boldsymbol { a } } , { \boldsymbol { x } } )$ .

if $( \texttt { x < 0 . 0 ~ } | \texttt { | a < = 0 . 0 } )$ throw("bad args in gammp"); if ( $\mathbf { \bar { x } } \ = = \ 0 . 0$ ) return 0.0; else if ((Int)a $> =$ ASWITCH) return gammpapprox $( \mathsf { a } , \mathsf { x } , 1 )$ ; Quadrature. else if $\mathit { \Pi } _ { \overline { { \mathbf { X } } } } ^ { ' } \ < \ \mathtt { a } + 1 . 0$ ) return gser(a,x); Use the series representation. else return 1.0-gcf(a,x); Use the continued fraction representation. L

Doub gammq(const Doub a, const Doub x) { Returns the incomplete gamma function $Q ( a , x ) \equiv 1 - P ( a , x )$ .

if $\mathit { \Omega } \left( \mathbf { x } \ < \ 0 . 0 \right.$ | $| \mathrm { ~  ~ a ~ } < = 0 . 0 \dot { } .$ ) throw("bad args in gammq");   
if $\mathit { \textbf { \xi } } _ { \mathbf { X } } = = \ 0 . 0 $ ) return 1.0;   
else if ((Int)a $> =$ ASWITCH) return gammpapprox $( \mathtt { a } , \mathtt { x } , 0 )$ ; Quadrature.   
else if $( \mathbf { x } ~ < ~ \mathsf { a } + 1 . 0 ) ^ { \dagger }$ ) return 1.0-gser(a,x); Use the series representation.   
else return gcf(a,x); Use the continued fraction representation.

# }

# Doub gser(const Doub a, const Doub x) {

Returns the incomplete gamma function $P ( { \boldsymbol { a } } , { \boldsymbol { x } } )$ evaluated by its series representation.   
Also sets ln $\Gamma ( a )$ as $\mathtt { g l n }$ . User should not call directly.

Doub sum,del,ap; gln=gammln(a); $\mathtt { a p - a }$ ; del $\cdot ^ { = }$ sum=1.0/a; for (;;) { ++ap; del $\ast =$ x/ap; sum $+ =$ del; if (fabs(del) $<$ fabs(sum) $^ *$ EPS) { return sum\*exp(-x+a\*log(x)-gln); } } }

# Doub gcf(const Doub a, const Doub x) {

Returns the incomplete gamma function $Q ( a , x )$ evaluated by its continued fraction representation. Also sets ln $\Gamma ( a )$ as $\mathtt { g l n }$ . User should not call directly.

Int i;   
Doub an,b,c,d,del,h;   
gln=gammln(a);   
$\mathtt { b { = } x { + } 1 } . 0 { - } \mathtt { a }$ ;   
$\mathtt { C } = 1$ .0/FPMIN;   
${ \tt d } = 1$ .0/b;   
$\mathtt { h } { = } \mathtt { d }$ ;   
for ( $\scriptstyle \dot { \mathtt { 1 } } = 1$ ;;i++) { $\mathrm { { a n \ = \ - i * ( i - a ) \ ; } }$ ; b $+ = ~ 2 . 0$ ; d=an\*d+b;

Set up for evaluating continued fraction by modified Lentz’s method (-5.2) with $b _ { 0 } = \mathbf { 0 }$ .

Iterate to convergence.

if (fabs(d) $<$ FPMIN) $\mathtt { d } =$ FPMIN; c=b+an/c; if (fabs(c) $<$ FPMIN) $c =$ FPMIN; $\mathrm { d } { = } 1$ .0/d; del=d\*c; h $\ast =$ del; if (fabs(del-1.0) $< =$ EPS) break;   
}   
return $\exp \left( - \mathrm { { x } + \mathrm { { a } * 1 0 g } \left( \mathrm { { x } } \right) - \mathrm { { g } 1 n } } \right) * \mathrm { { h } }$ ; Put factors in front. Doub gammpapprox(Doub a, Doub x, Int psig) $\left\{ \begin{array} { r l } \end{array} \right.$   
Incomplete gamma by quadrature. Returns $P ( { \boldsymbol { a } } , { \boldsymbol { x } } )$ or $Q ( a , x )$ , when psig is 1 or 0, respectively. User should not call directly.

Int j; Doub xu,t,sum,ans; Doub a1 $= \ a - 1 . 0$ , lna1 $=$ log(a1), sqrta1 $=$ sqrt(a1); ${ \bf g l n = \bf g a m m l n ( a ) }$ ; Set how far to integrate into the tail: if ( $\texttt { x } >$ a1) $\mathrm { ~ \tt ~ { ~ x ~ u ~ } ~ } =$ MAX(a1 $^ +$ 11. $^ { 5 \ast }$ sqrta1, x + 6. $^ { 0 * }$ sqrta1); else xu $=$ MAX(0.,MIN(a1 - 7.5\*sqrta1, x - 5.0\*sqrta1)); sum $\mathit { \Theta } = \mathit { \Theta } 0$ ; for (j=0;j<ngau;j++) { Gauss-Legendre. $\texttt { t } = \texttt { x } + \texttt { ( x u - x ) } * \texttt { y } [ \texttt j ]$ ; sum += w[j]\*exp(-(t-a1)+a1\*(log(t)-lna1)); ans $=$ sum\*(xu-x)\*exp(a1\*(lna1-1.)-gln); return (psig?(ans>0.0? 1.0-ans:-ans):(ans> ${ } = 0$ .0? ans:1.0+ans)); }

Doub invgammp(Doub p, Doub a);   
Inverse function on $x$ of $P ( { \boldsymbol { a } } , { \boldsymbol { x } } )$ . See $\ S 6 . 2 . 1$ . };   
const Doub Gamma::EPS $=$ numeric_limits<Doub>::epsilon();   
const Doub Gamma::FPMIN $=$ numeric_limits<Doub>::min()/EPS;

Remember that since Gamma is an object, you have to declare an instance of it before you can use its member functions. We habitually write

# Gamma gam;

as a global declaration, and then call gam.gammp or gam.gammq as needed. The structure Gauleg18 just contains the abscissas and weights for the Gauss-Legendre quadrature.

# struct Gauleg18 {

Abscissas and weights for Gauss-Legendre quadrature.

static const Int ngau $\ c = \ 1 8$ ; static const Doub y[18]; static const Doub w[18];   
};   
const Doub Gauleg18::y[18] $=$ {0.0021695375159141994,   
0.011413521097787704,0.027972308950302116,0.051727015600492421,   
0.082502225484340941, 0.12007019910960293,0.16415283300752470,   
0.21442376986779355, 0.27051082840644336, 0.33199876341447887,   
0.39843234186401943, 0.46931971407375483, 0.54413605556657973,   
0.62232745288031077, 0.70331500465597174, 0.78649910768313447,   
0.87126389619061517, 0.95698180152629142};   
const Doub Gauleg18::w[18] $=$ {0.0055657196642445571,   
0.012915947284065419,0.020181515297735382,0.027298621498568734,   
0.034213810770299537,0.040875750923643261,0.047235083490265582,   
0.053244713977759692,0.058860144245324798,0.064039797355015485,

0.068745323835736408,0.072941885005653087,0.076598410645870640,   
0.079687828912071670,0.082187266704339706,0.084078218979661945,   
0.085346685739338721,0.085983275670394821};

# 6.2.1 Inverse Incomplete Gamma Function

In many statistical applications one needs the inverse of the incomplete gamma function, that is, the value $x$ such that $P ( a , x ) = p$ , for a given value $0 \leq p \leq 1$ . Newton’s method works well if we can devise a good-enough initial guess. In fact, this is a good place to use Halley’s method (see $\ S 9 . 4$ ), since the second derivative (that is, the first derivative of the integrand) is easy to compute.

For $a > 1$ , we use an initial guess that derives from $\ S 2 6 . 2 . 2 2$ and $\ S 2 6 . 4 . 1 7$ in reference [1]. For $a \leq 1$ , we first roughly approximate $P _ { a } \equiv P ( a , 1 )$ :

$$
P _ { a } \equiv P ( a , 1 ) \approx 0 . 2 5 3 a + 0 . 1 2 a ^ { 2 } , \qquad 0 \leq a \leq 1
$$

and then solve for $x$ in one or the other of the (rough) approximations:

$$
\begin{array} { r } { P ( a , x ) \approx \left\{ \begin{array} { l l } { P _ { a } x ^ { a } , } & { x < 1 } \\ { P _ { a } + ( 1 - P _ { a } ) ( 1 - e ^ { 1 - x } ) , } & { x \geq 1 } \end{array} \right. } \end{array}
$$

An implementation is

Doub Gamma::invgammp(Doub p, Doub a) {   
Returns $x$ such that $P ( a , x ) = p$ for an argument $p$ between 0 and 1. Int j; Doub x,err,t,u,pp,lna1,afac,a $\mathsf { L } = \mathsf { a } - 1$ ; const Doub EPS $\mathop { : = } 1$ .e-8; Accuracy is the square of EPS. gln=gammln(a); if ( $\texttt { a } < = \texttt { 0 } .$ ) throw("a must be pos in invgammap"); if $\mathrm { ( p \ > = \ 1 . }$ ) return MAX(100.,a $^ +$ 100.\*sqrt(a)); if ${ \mathrm { ( p ) < = 0 } } .$ ) return 0.0; if ( $\texttt { a } > \texttt { 1 }$ .) { Initial guess based on reference [1]. lna1 $=$ log(a1); afac $=$ exp(a1\*(lna1-1.)-gln); $\mathrm { p p ~ = ~ ( p ~ < ~ 0 ~ . 5 ) ? ~ p ~ : ~ 1 }$ . - p; $\mathrm {  ~ t ~ } = \mathrm {  ~ \ s q r t { } ~ } ( - 2 . * 1 \mathrm { o g } ( \mathrm { p p } ) )$ ); $\mathrm { ~ x ~ } =$ (2.30753+t\*0.27061)/(1.+t\*(0.99229+t\*0.04481)) - t; if $( \mathtt { p } \ < \ 0 . 5 )$ ) $\mathrm { ~ \tt ~ { ~ x ~ } ~ } = \mathrm { ~ \tt ~ { ~ - ~ x ~ } ~ }$ ; $\mathrm { ~ x ~ } =$ MAX(1.e-3,a\*pow(1.-1./(9.\*a)-x/(3.\*sqrt(a)),3)); } else { Initial guess based on equations (6.2.8) t = 1.0 - a\*(0.253+a\*0.12); and (6.2.9). if (p < t) $_ { \textrm { x } } =$ pow(p/t,1./a); else x = 1.-log(1.-(p-t)/(1.-t)); } for (j=0;j<12;j++) { if ( $\mathrm { ~  ~ \bar { ~ } x ~ } < = \mathrm { ~  ~ 0 ~ } . 0 $ ) return 0.0; $x$ too small to compute accurately. err $=$ gammp(a,x) - p; if (a $> ~ 1 .$ ) t = afac\*exp(-(x-a1)+a1\*(log(x)-lna1)); else t $=$ exp(-x+a1\*log(x)-gln); $\mathrm { ~ \textbar ~ { ~ u ~ } ~ } =$ err/t; $\texttt { x } \texttt { - } \left( \texttt { t } = \texttt { u } / \left( 1 \ldots 0 . 5 * \mathtt { M I N } ( 1 . \texttt { , u * } ( ( \mathtt { a - 1 . } ) / \texttt { x } - \texttt { 1 } ) ) \right) \right) \texttt { m } \texttt { - l - w } \texttt { N } _ { \texttt { i n - w } } ( \texttt { c l - w } _ { \texttt { i n - i - j } } ) \texttt { N } _ { \texttt { i n - i - j } }$ ; Halley’s method. if ( $\begin{array} { r } { \mathrm { ~  ~ x ~ } < = \mathrm { ~  ~ 0 ~ } . } \end{array}$ ) $\textbf { x } = ~ 0 . 5 * ( \textbf { x } + \textbf { t } )$ ; Halve old value if $x$ tries to go negative. if (fabs(t) $<$ EPS\*x ) break; } return x;

# 6.2.2 Error Function

The error function and complementary error function are special cases of the incomplete gamma function and are obtained moderately efficiently by the above procedures. Their definitions are

$$
\operatorname { e r f } ( x ) = { \frac { 2 } { \sqrt { \pi } } } \int _ { 0 } ^ { x } e ^ { - t ^ { 2 } } d t
$$

and

$$
\mathrm { e r f c } ( x ) \equiv 1 - \mathrm { e r f } ( x ) = \frac { 2 } { \sqrt { \pi } } \int _ { x } ^ { \infty } e ^ { - t ^ { 2 } } d t
$$

The functions have the following limiting values and symmetries:

$$
{ \begin{array} { r l r l } & { \operatorname { e r f } ( 0 ) = 0 } & & { \operatorname { e r f } ( \infty ) = 1 \qquad \operatorname { e r f } ( - x ) = - \operatorname { e r f } ( x ) } \\ & { \operatorname { e r f c } ( 0 ) = 1 } & & { \operatorname { e r f c } ( \infty ) = 0 } & & { \operatorname { e r f c } ( - x ) = 2 - \operatorname { e r f c } ( x ) } \end{array} }
$$

They are related to the incomplete gamma functions by

$$
\operatorname { e r f } ( x ) = P \left( { \frac { 1 } { 2 } } , x ^ { 2 } \right) \qquad ( x \geq 0 )
$$

and

$$
\operatorname { e r f c } ( x ) = Q \left( { \frac { 1 } { 2 } } , x ^ { 2 } \right) \qquad ( x \geq 0 )
$$

A faster calculation takes advantage of an approximation of the form

$$
\mathrm { e r f c } ( z ) \approx t \ \mathrm { e x p } [ - z ^ { 2 } + \mathcal { P } ( t ) ] , \qquad z > 0
$$

where

$$
t \equiv { \frac { 2 } { 2 + z } }
$$

and $\mathcal { P } ( t )$ is a polynomial for $0 \leq t \leq 1$ that can be found by Chebyshev methods (-5.8). As with Gamma, implementation is by an object that also includes the inverse function, here an inverse for both erf and erfc. Halley’s method is again used for the inverses (as suggested by P.J. Acklam).

# erf.h

# struct Erf {

Object for error function and related functions.

static const Int ncof $= 2 8$ ;   
static const Doub cof[28];

Initialization at end of struct.

inline Doub erf(Doub x) {   
Return erf $( x )$ for any $x$ . if $\mathrm { (  ~ x ~ } ) = 0 \ .$ ) return 1.0 - erfccheb(x); else return erfccheb(-x) - 1.0;   
}   
inline Doub erfc(Doub x) {   
Return erfc. $( x )$ for any $x$ . if $\begin{array} { r } { \mathrm { ~  ~ \psi ~ } ( { \bf x } ) = { \bf \psi } 0 . } \end{array}$ ) return erfccheb $\mathbf { \Psi } ( \mathbf { x } )$ ; else return 2.0 - erfccheb $\left( - \mathbf { \vec { x } } \right)$ ;   
}

# Doub erfccheb(Doub z){

Evaluate equation (6.2.16) using stored Chebyshev coefficients. User should not call directly.

Int j;  
Doub t,ty,tmp, $\mathtt { d } \mathtt { = } 0$ .,dd=0.;  
if ( $\ z \ < \ 0 .$ ) throw("erfccheb requires nonnegative argument")  
$\tt { t } = \displaystyle 2 . / ( 2 . + z )$ ;  
ty $=$ 4.\*t - 2.;  
for (j=ncof-1;j>0;j--) {tmp $=$ d;d $=$ ty\*d - dd $^ +$ cof[j];dd $=$ tmp;  
}  
return t\*exp(-z\*z + 0.5\*(cof[0] $^ +$ ty\*d) - dd);

# }

# Doub inverfc(Doub p) {

Inverse of complementary error function. Returns $x$ such that erfc $( x ) = p$ for argument $p$ between 0 and 2.

Doub x,err,t,pp;   
if (p $> = \ 2 . 0 )$ return -100.; Return arbitrary large pos or neg value.   
if $( \mathbf { p } ) \ < = \ 0 . 0 )$ ) return 100.;   
$\mathrm { p p } = ( \mathrm { p } < 1 . 0 ) ? \mathrm { p } : 2 . -$ p;   
$\mathrm { ~ t ~ } = \mathrm { ~ s q r t } \left( - 2 . * \mathrm { { 1 o g } } \left( \mathrm { p p } / 2 . \right) \right) ;$ Initial guess:   
x = -0.70711\*((2.30753+t\*0.27061)/(1.+t\*(0.99229+t\*0.04481)) - t);   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<2;j $^ { + + }$ ) { err $=$ erfc(x) - pp; x $+ =$ err/(1.12837916709551257\*exp(-SQR $\mathbf { \Psi } ( \mathbf { x } )$ )-x\*err); Halley.   
return $\ : \left( \mathrm { p } < 1 . 0 ? \ : \mathrm {  ~ x ~ } : - \mathrm { x } \right) :$ ; inline Doub inverf(Doub p) {return inverfc(1.-p);}   
Inverse of the error function. Returns $x$ such that $\operatorname { s r f } ( x ) = p$ for argument $p$ between 1 and 1.

#

onst Doub Erf::cof[28] $= ~ \left\{ - 1 \atop \right.$ .3026537197817094, 6.4196979235649026e-1, 1.9476473204185836e-2,-9.561514786808631e-3,-9.46595344482036e-4, 3.66839497852761e-4,4.2523324806907e-5,-2.0278578112534e-5, -1.624290004647e-6,1.303655835580e-6,1.5626441722e-8,-8.5238095915e-8, 6.529054439e-9,5.059343495e-9,-9.91364156e-10,-2.27365122e-10, 9.6467911e-11, 2.394038e-12,-6.886027e-12,8.94487e-13, 3.13092e-13, -1.12708e-13,3.81e-16,7.106e-15,-1.523e-15,-9.4e-17,1.21e-16,-2.8e-17};

A lower-order Chebyshev approximation produces a very concise routine, though with only about single precision accuracy:

# Doub erfcc(const Doub x)

Returns the complementary error function erfc $\mathbf { \rho } ( \mathbf { x } )$ with fractional error everywhere less than $1 . 2 \times 1 0 ^ { - 7 }$ .

Doub t,z=fabs $\left( \mathbf { \boldsymbol { x } } \right)$ ,ans;   
$\mathrm { t } { = } 2 . / ( 2 . +  { \mathrm { z } } )$ ;   
ans=t\*exp(-z\*z-1.26551223+t\*(1.00002368+t\*(0.37409196+t\*(0.09678418+ t\*(-0.18628806+t\*(0.27886807+t\*(-1.13520398+t\*(1.48851587+ t\*(-0.82215223+t\*0.17087277)))))))));   
return $\mathrm { ~ ( ~ x ~ ) = ~ 0 ~ . 0 ~ }$ ? ans : 2.0-ans);

![](images/5b2bdea95927dba5c942d25f629039f68b7daa91357cde1412da389934c091ad.jpg)  
Figure 6.3.1. Exponential integrals $E _ { n } ( x )$ for $n = 0 , 1 , 2 , 3 , 5$ ; and 10, and the exponential integral $\operatorname { E i } ( x )$ .

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapters 6, 7, and 26.[1]

Pearson, K. (ed.) 1951, Tables of the Incomplete Gamma Function (Cambridge, UK: Cambridge University Press).

# 6.3 Exponential Integrals

The standard definition of the exponential integral is

$$
E _ { n } ( x ) = \int _ { 1 } ^ { \infty } { \frac { e ^ { - x t } } { t ^ { n } } } d t , \qquad x > 0 , \quad n = 0 , 1 , \ldots .
$$

The function defined by the principal value of the integral

$$
\operatorname { E i } ( x ) = - \int _ { - x } ^ { \infty } { \frac { e ^ { - t } } { t } } d t = \int _ { - { \infty } } ^ { x } { \frac { e ^ { t } } { t } } d t , \qquad x > 0
$$

is also called an exponential integral. Note that $\operatorname { E i } ( - x )$ is related to $- E _ { 1 } ( x )$ by analytic continuation. Figure 6.3.1 plots these functions for representative values of their parameters.

The function $E _ { n } ( x )$ is a special case of the incomplete gamma function

$$
E _ { n } ( x ) = x ^ { n - 1 } \Gamma ( 1 - n , x )
$$

We can therefore use a similar strategy for evaluating it. The continued fraction — just equation (6.2.6) rewritten — converges for all $x > 0$ :

$$
E _ { n } ( x ) = e ^ { - x } \left( { \frac { 1 } { x + } } { \frac { n } { 1 + } } { \frac { 1 } { x + } } { \frac { n + 1 } { 1 + } } { \frac { 2 } { x + } } \cdots \right)
$$

We use it in its more rapidly converging even form,

$$
E _ { n } ( x ) = e ^ { - x } \left( { \frac { 1 } { x + n - } } { \frac { 1 \cdot n } { x + n + 2 - } } { \frac { 2 ( n + 1 ) } { x + n + 4 - } } \cdots \right)
$$

The continued fraction only really converges fast enough to be useful for $x \gtrsim 1$ . For $0 < x \lesssim 1$ , we can use the series representation

$$
E _ { n } ( x ) = { \frac { ( - x ) ^ { n - 1 } } { ( n - 1 ) ! } } [ - \ln x + \psi ( n ) ] - \sum _ { \stackrel { m = 0 } { m \neq n - 1 } } ^ { \infty } { \frac { ( - x ) ^ { m } } { ( m - n + 1 ) m ! } }
$$

The quantity $\psi ( n )$ here is the digamma function, given for integer arguments by

$$
\psi ( 1 ) = - \gamma , \qquad \psi ( n ) = - \gamma + \sum _ { m = 1 } ^ { n - 1 } \frac { 1 } { m }
$$

where $\gamma = 0 . 5 7 7 2 1 5 6 6 4 9 \ldots$ is Euler’s constant. We evaluate the expression (6.3.6) in order of ascending powers of $x$ :

$$
\begin{array} { c } { { E _ { n } ( x ) = - \displaystyle \left[ \frac { 1 } { ( 1 - n ) } - \frac { x } { ( 2 - n ) \cdot 1 } + \frac { x ^ { 2 } } { ( 3 - n ) ( 1 \cdot 2 ) } - \cdots + \frac { ( - x ) ^ { n - 2 } } { ( - 1 ) ( n - 2 ) ! } \right] } } \\ { { + \displaystyle \frac { ( - x ) ^ { n - 1 } } { ( n - 1 ) ! } [ - \ln x + \psi ( n ) ] - \displaystyle \left[ \frac { ( - x ) ^ { n } } { 1 \cdot n ! } + \frac { ( - x ) ^ { n + 1 } } { 2 \cdot ( n + 1 ) ! } + \cdots \right] } } \end{array}
$$

The first square bracket is omitted when $n = 1$ . This method of evaluation has the advantage that, for large $n$ , the series converges before reaching the term containing $\psi ( n )$ . Accordingly, one needs an algorithm for evaluating $\psi ( n )$ only for small $n , n \stackrel { < } { \sim }$ $2 0 - 4 0$ . We use equation (6.3.7), although a table lookup would improve efficiency slightly.

Amos [1] presents a careful discussion of the truncation error in evaluating equation (6.3.8) and gives a fairly elaborate termination criterion. We have found that simply stopping when the last term added is smaller than the required tolerance works about as well.

Two special cases have to be handled separately:

$$
\begin{array} { l } { \displaystyle E _ { 0 } ( \boldsymbol { x } ) = \frac { e ^ { - x } } { x } } \\ { \displaystyle E _ { n } ( 0 ) = \frac { 1 } { n - 1 } , \qquad n > 1 } \end{array}
$$

The routine expint allows fast evaluation of $E _ { n } ( x )$ to any accuracy EPS within the reach of your machine’s precision for floating-point numbers. The only modification required for increased accuracy is to supply Euler’s constant with enough significant digits. Wrench [2] can provide you with the first 328 digits if necessary!

Doub expint(const Int n, const Doub x) Evaluates the exponential integral $E _ { n } ( x )$ . {

static const Int MAXI $\mathtt { \tau } = 1 0 0$ ;   
static const Doub EULER $_ { = 0 }$ .577215664901533, EPS=numeric_limits<Doub>::epsilon(), BIG $\mathbf { \bar { \mathbf { \tau } } }$ numeric_limits<Doub>::max()\*EPS; Here MAXIT is the maximum allowed number of iterations; EULER is Euler’s con ; EPS is the desired relative error, not smaller than the machine precision; BIG number near the largest representable floating-point number.   
Int i,ii,nm1 $= \mathtt { n } - 1$ ;   
Doub a,b,c,d,del,fact,h,psi,ans;   
if ( $\mathrm { ~ \textit ~ { ~ n ~ } ~ } < \mathrm { ~ \textit ~ { ~ O ~ } ~ }$ || $\texttt { x } < 0 . 0$ || $\scriptstyle \mathbf { \underline { { x } } } = = 0 . 0$ && $\scriptstyle ( \mathtt { n } = = 0 \ \mid \mid \ \mathtt { n } = = 1 ) ) \ .$ ) throw("bad arguments in expint");   
if $\mathbf { \Omega } _ { \mathrm { ~ n ~ } } = = \mathbf { \Omega } 0$ ) ans ${ } = { }$ exp $( - \mathbf { x } ) / \mathbf { x }$ ; Special case.   
else { if $( \textbf { x } = = \ 0 . 0$ ) ans $= 1$ .0/nm1; Another special case. else { if $\mathit { \check { \Psi } } _ { \mathrm { ~ X ~ } } > \ 1 . 0 \ \rangle$ { Lentz’s algorithm (-5.2). ${ \tt b } = { \tt x } + { \tt n }$ ; $c =$ BIG; $\mathtt { d } \mathtt { = } 1$ .0/b; $\mathtt { h } = \mathtt { d }$ ; for ( $\dot { \ b _ { 1 } } = 1$ ;i $\cdot < =$ MAXIT;i++) { a = -i\*(nm1+i); b $+ = ~ 2 . 0$ ; d=1.0/(a\*d+b); Denominators cannot be zero. c=b+a/c; del=c\*d; h $* =$ del; if (abs(del-1.0) $< =$ EPS) { ans=h\*exp(-x); return ans; } } throw("continued fraction failed in expint"); } else { Evaluate series. ans $=$ (nm1 $\iota { = } 0$ ? 1.0/nm1 : -log(x)-EULER); Set first term. fact $= 1$ .0; for ( $\dot { \ b _ { 1 } } = 1$ ;i $< =$ MAXIT;i++) { fact $\ast = \mathbf { \Gamma } - \mathbf { x } / \mathrm { i }$ ; if (i ! $\downarrow =$ nm1) del $=$ -fact/(i-nm1); else { psi $=$ -EULER; Compute $\psi ( n )$ . for ( $\dot { 1 } \dot { 1 } = 1$ ;ii $< =$ nm1;ii $^ { + + }$ ) psi $+ =$ 1.0/ii; del=fact\*(-log(x)+psi); ans $+ =$ del; if (abs(del) $<$ abs(ans)\*EPS) return ans; } throw("series failed in expint"); } }   
return ans;

A good algorithm for evaluating Ei is to use the power series for small $x$ and the asymptotic series for large $x$ . The power series is

$$
\operatorname { E i } ( x ) = \gamma + \ln x + { \frac { x } { 1 \cdot 1 ! } } + { \frac { x ^ { 2 } } { 2 \cdot 2 ! } } + \cdots
$$

where $\gamma$ is Euler’s constant. The asymptotic expansion is

$$
\operatorname { E i } ( x ) \sim { \frac { e ^ { x } } { x } } \left( 1 + { \frac { 1 ! } { x } } + { \frac { 2 ! } { x ^ { 2 } } } + \cdots \right)
$$

The lower limit for the use of the asymptotic expansion is approximately $| \ln { \tt E P S } |$ , where EPS is the required relative error.

Doub ei(const Doub x) { mputes the exponential integral $\operatorname { E i } ( x )$ for $x > 0$ . static const Int MAXIT $^ { \prime = 1 }$ 100; static const Doub EULER $_ { = 0 }$ .577215664901533, EPS=numeric_limits<Doub>::epsilon(), FPMIN=numeric_limits<Doub>::min()/EPS; Here MAXIT is the maximum number of iterations allowed; EULER is Euler’s constant $\gamma$ ; EPS is the relative error, or absolute error near the zero of Ei at $x = 0 . 3 7 2 5$ ; FPMIN is a number close to the smallest representable floating-point number. Int k; Doub fact,prev,sum,term; if ( $\varpi \ : < = \ : 0 . 0 \dot { . }$ ) throw("Bad argument in ei"); if ( $\texttt { x } <$ FPMIN) return log(x)+EULER; Special case: Avoid failure of convergence if (x <= -log(EPS)) { test because of underflow. sum $\mathord { \left[ - 0 \mathrm { ~ , ~ } 0 \mathrm { ~ } \right] }$ ; Use power series. fact ${ = } 1$ .0; for $\scriptstyle ( \mathtt { k } = 1$ ;k $< =$ MAXIT;k++) { fact $\ast = ~ \mathrm { { \ x / k } }$ ; term=fact/k; sum $+ =$ term; if (term $<$ EPS\*sum) break; } if (k $>$ MAXIT) throw("Series failed in ei"); return sum+log(x)+EULER; else { Use asymptotic series. sum $= 0$ .0; Start with second term. term $= 1$ .0; for $\mathtt { k } = 1$ ;k $< =$ MAXIT;k++) { prev=term; term $\ast = ~ \mathrm { k } / \mathrm { x }$ ; if (term $<$ EPS) break; Since final sum is greater than one, term itself approximates the relative error. if (term $<$ prev) sum $+ =$ term; Still converging: Add new term. else { sum $- =$ prev; Diverging: Subtract previous term and break; exit. } } return exp(x)\*(1.0+sum)/x; }

# CITED REFERENCES AND FURTHER READING:

Stegun, I.A., and Zucker, R. 1974, “Automatic Computing Methods for Special Functions. II. The Exponential Integral $E _ { n } ( x )$ ,” Journal of Research of the National Bureau of Standards,

vol. 78B, pp. 199–216; 1976, “Automatic Computing Methods for Special Functions. III. The Sine, Cosine, Exponential Integrals, and Related Functions,” op. cit., vol. 80B, pp. 291–311.

Amos D.E. 1980, “Computation of Exponential Integrals,” ACM Transactions on Mathematical Software,vol.6,pp.365-377[1]; also vol.6, pp.420-428.

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapter 5.

Wrench J.W. 1952, “A New Calculation of Euler’s Constant,” Mathematical Tables and OtherAids to Computation,vol. 6,p. 255.[2]

# 6.4 Incomplete Beta Function

The incomplete beta function is defined by

$$
I _ { x } ( a , b ) \equiv \frac { B _ { x } ( a , b ) } { B ( a , b ) } \equiv \frac { 1 } { B ( a , b ) } \int _ { 0 } ^ { x } t ^ { a - 1 } ( 1 - t ) ^ { b - 1 } d t \qquad ( a , b > 0 )
$$

It has the limiting values

$$
I _ { 0 } ( a , b ) = 0 \qquad I _ { 1 } ( a , b ) = 1
$$

and the symmetry relation

$$
I _ { x } ( a , b ) = 1 - I _ { 1 - x } ( b , a )
$$

If $a$ and $b$ are both rather greater than one, then $I _ { x } ( a , b )$ rises from “near-zero” to “near-unity” quite sharply at about $x = a / ( a + b )$ . Figure 6.4.1 plots the function for several pairs $( a , b )$ .

The incomplete beta function has a series expansion

$$
I _ { x } ( a , b ) = \frac { x ^ { a } ( 1 - x ) ^ { b } } { a B ( a , b ) } \left[ 1 + \sum _ { n = 0 } ^ { \infty } \frac { B ( a + 1 , n + 1 ) } { B ( a + b , n + 1 ) } x ^ { n + 1 } \right]
$$

but this does not prove to be very useful in its numerical evaluation. (Note, however, that the beta functions in the coefficients can be evaluated for each value of $n$ with just the previous value and a few multiplies, using equations 6.1.9 and 6.1.3.)

The continued fraction representation proves to be much more useful:

$$
I _ { x } ( a , b ) = { \frac { x ^ { a } ( 1 - x ) ^ { b } } { a B ( a , b ) } } \left[ { \frac { 1 } { 1 + } } { \frac { d _ { 1 } } { 1 + } } { \frac { d _ { 2 } } { 1 + } } \cdots \right]
$$

where

$$
\begin{array} { c } { { d _ { 2 m + 1 } = - \displaystyle \frac { ( a + m ) ( a + b + m ) x } { ( a + 2 m ) ( a + 2 m + 1 ) } } } \\ { { d _ { 2 m } = \displaystyle \frac { m ( b - m ) x } { ( a + 2 m - 1 ) ( a + 2 m ) } } } \end{array}
$$

This continued fraction converges rapidly for $x \ < \ ( a + 1 ) / ( a + b + 2 )$ , except when $a$ and $b$ are both large, when it can take $O ( \sqrt { \operatorname* { m i n } ( a , b ) } )$ iterations. For $x \ >$ $( a + 1 ) / ( a + b + 2 )$ we can just use the symmetry relation (6.4.3) to obtain an equivalent computation in which the convergence is again rapid. Our computational strategy is thus very similar to that used in Gamma: We use the continued fraction except when $a$ and $b$ are both large, in which case we do a single step of high-order Gauss-Legendre quadrature.

![](images/b13ef3b387045e0f83d128d9c2e140487de117395e1af8964610bca545ae9b53.jpg)  
Figure 6.4.1. The incomplete beta function $I _ { x } ( a , b )$ for five different pairs of $( a , b )$ . Notice that the pairs .0:5; 5:0/ and .5:0; 0:5/ are symmetrically related as indicated in equation (6.4.3).

Also as in Gamma, we code an inverse function using Halley’s method. When $a$ and $b$ are both $\geq 1$ , the initial guess comes from $\ S 2 6 . 5 . 2 2$ in reference [1]. When either is less than 1, the guess comes from first crudely approximating

$$
\int _ { 0 } ^ { 1 } t ^ { a - 1 } ( 1 - t ) ^ { b - 1 } d t \approx { \frac { 1 } { a } } \left( { \frac { a } { a + b } } \right) ^ { a } + { \frac { 1 } { b } } \left( { \frac { b } { a + b } } \right) ^ { b } \equiv S
$$

which comes from breaking the integral at $t = a / ( a + b )$ and ignoring one factor in the integrand on each side of the break. We then write

$$
I _ { x } ( a , b ) \approx \left\{ \begin{array} { l l } { x ^ { a } / ( S a ) } & { x \leq a / ( a + b ) } \\ { ( 1 - x ) ^ { b } / ( S b ) } & { x > a / ( a + b ) } \end{array} \right.
$$

and solve for $x$ in the respective regimes. While crude, this is good enough to get well within the basin of convergence in all cases.

# struct Beta : Gauleg18 {

Object for incomplete beta function. Gauleg18 provides coefficients for Gauss-Legendre quadrature.

static const Int SWITCH=3000; When to switch to quadrature method.   
static const Doub EPS, FPMIN; See end of struct for initializations.

Doub betai(const Doub a, const Doub b, const Doub x) { Returns incomplete beta function $I _ { x } ( a , b )$ for positive $^ { a }$ and $^ { b }$ , and $x$ between 0 and 1.

Doub bt;   
if ( $\texttt { a } < = \texttt { 0 } . 0$ || b $< = \ 0 . 0$ ) throw("Bad a or b in routine betai");   
if $( \texttt { x } < 0 . 0 \ | \ | \ \texttt { x } > \ 1 . 0 )$ throw("Bad x in routine betai");   
if $( \mathrm {  ~ x ~ } = = \mathrm {  ~ 0 ~ } . 0 | | \mathrm {  ~ x ~ } = = \mathrm {  ~ 1 ~ } . 0 )$ ) return x;   
if ( $\texttt { a } >$ SWITCH && b $>$ SWITCH) return betaiapprox(a,b,x);   
bt=exp(gammln(a+b)-gammln(a)-gammln(b)+a\*log(x)+b\*log(1.0-x));   
if $\left( \mathrm { x } < \left( \mathrm { a } + 1 . 0 \right) / \left( \mathrm { a } + \mathrm { b } + 2 . 0 \right) \right.$ ) return bt\*betacf(a,b,x)/a;   
else return 1.0-bt\*betacf(b,a,1.0-x)/b;

# Doub betacf(const Doub a, const Doub b, const Doub x) {

Evaluates continued fraction for incomplete beta function by modified Lentz’s method (-5.2). User should not call directly.

Int m,m2;   
Doub aa,c,d,del,h,qab,qam,qap;   
qab $= \mathtt { a } + 1$ b; These q’s will be used in factors that   
qap $\mathtt { \Gamma } _ { 1 } = \mathtt { a } + 1$ .0; occur in the coefficients (6.4.6).   
qam=a-1.0;   
c=1.0; First step of Lentz’s method.   
$\mathtt { d } \mathtt { = } 1$ .0-qab\*x/qap;   
if (fabs(d) $<$ FPMIN) d=FPMIN;   
d=1.0/d;   
h=d;   
for (m=1;m<10000;m++) { $\mathtt { m } 2 \mathrm { = } 2 \ast \mathtt { m }$ ; aa=m\*(b-m)\*x/((qam+m2)\*(a+m2)); d=1.0+aa\*d; One step (the even one) of the recurif (fabs(d) $<$ FPMIN) $\mathrm { d } \mathrm { = }$ FPMIN; rence. c=1.0+aa/c; if (fabs(c) $<$ FPMIN) $c =$ FPMIN; $\mathtt { d } \mathtt { = } 1$ .0/d; $\mathrm {  ~ h ~ \ * = ~ \ d * c }$ ; aa = -(a+m)\*(qab+m)\*x/((a+m2)\*(qap+m2)); $\mathrm { d } { = } 1$ .0+aa\*d; Next step of the recurrence (the odd if (fabs(d) $<$ FPMIN) $\mathrm { d } \mathrm { = }$ FPMIN; one). c=1.0+aa/c; if (fabs(c) $<$ FPMIN) $c =$ FPMIN; $\mathtt { d } \mathtt { = } 1$ .0/d; del=d\*c; h $\ast =$ del; if (fabs(del-1.0) $< =$ EPS) break; Are we done?   
}   
return h;

Doub betaiapprox(Doub a, Doub b, Doub $\mathbf { x }$ ) { Incomplete beta by quadrature. Returns $I _ { x } ( a , b )$ . User should not call directly.

Int j;   
Doub xu,t,sum,ans;   
Doub a $1 \ = \ \mathsf { a } { - } 1 . 0$ , $ { \mathbf { b } }  { \mathbf { 1 } } ~ = ~  { \mathbf { b } } - 1 . 0$ , $\mathrm { \ m u ~ = ~ a / ( a + b ) }$ ;   
Doub lnmu $\cdot ^ { = }$ log(mu),lnmuc=log(1.-mu);   
${ \texttt { t } } =$ sqrt(a\*b/(SQR(a+b)\*(a+b+1.0)));   
if $x > a / ( a + b )$ ) { Set how far to integrate into the tail: if $( \textbf { x } > = \textbf { 1 } . 0 )$ ) return 1.0; $\mathrm { ~ x u ~ } =$ MIN(1.,MAX(mu $^ +$ 10.\*t, $\textbf { x } + \textbf { 5 } . 0 { * } \mathrm { t } ) \big )$ ;   
} else {

if $\mathit { \Psi } ( \mathbf { x } \ < = \ 0 . 0 ) $ ) return 0.0; xu $=$ MAX(0.,MIN(mu - 10.\*t, x - 5.0\*t)); } sum = 0; for (j=0;j<18;j++) { Gauss-Legendre. t = x + (xu-x)\*y[j]; sum += w[j]\*exp(a1\*(log(t)-lnmu)+b1\*(log(1-t)-lnmuc)); ans $=$ sum\*(xu-x)\*exp(a1\*lnmu-gammln(a)+b1\*lnmuc-gammln(b)+gammln(a+b)); return ans>0.0? 1.0-ans : -ans;

Doub invbetai(Doub p, Doub a, Doub b) {   
Inverse of incomplete beta function. Returns $x$ such that $I _ { x } ( a , b ) = p$ for argument $p$ between 0 and 1.

const Doub EPS $\ l = \ 1$ .e-8; Doub pp,t,u,err,x,al,h,w,afac,a1=a-1.,b1=b-1.; Int j; if $( \mathtt { p } \ < = \ 0 .$ ) return 0.; else if ( $\mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ }$ ) return 1.; else if ( $a > = 1$ . && b $> = ~ 1 ,$ ) { Set initial guess. See text. $\mathrm { { p p } ~ = ~ ( p ~ < ~ 0 ~ . 5 ) ? ~ p ~ : ~ 1 . }$ - p; $\texttt { t } = \texttt { s q r t } ( - 2 . * 1 \circ \mathtt { g } ( \mathtt { p p } ) )$ ; $\mathrm { ~ x ~ } =$ (2.30753+t\*0.27061)/(1.+t\*(0.99229+t\*0.04481)) - t; if $( \mathtt { p } \ < \ 0 . 5 )$ $\mathrm { ~ \tt ~ { ~ x ~ } ~ } = \mathrm { ~ \tt ~ - { ~ x ~ } ~ }$ ; $\mathrm { { \bf { a } } } \mathrm { { \bf { 1 } } } = ( { \tt S Q R } ( { \bf { x } } ) - 3 . ) / 6 .$ ; h = 2./(1./(2.\*a-1.)+1./(2.\*b-1.)); $\kappa =$ (x\*sqrt(al+h)/h)-(1./(2.\*b-1)-1./(2.\*a-1.))\*(al+5./6.-2./(3.\*h)); x = a/(a+b\*exp(2.\*w)); } else { Doub lna $=$ log(a/(a+b)), lnb $=$ log(b/(a+b)); $\begin{array} { r l } { \mathbf { \epsilon } _ { \mathbf { { t } } } } & { { } = } \end{array}$ exp(a\*lna)/a; $\mathrm { ~ \textbar ~ { ~ u ~ } ~ } =$ exp(b\*lnb)/b; $\mathrm { ~  ~ w ~ } = \mathrm { ~ t ~ } + \mathrm { ~  ~ \Omega ~ }$ u; if $( \mathbb { p } \ < \ \pm / \mathbb { w } )$ x = pow(a\*w\*p,1./a); else $\texttt { x } = \texttt { 1 }$ . - pow(b\*w\*(1.-p),1./b); } afac $=$ -gammln(a)-gammln(b)+gammln(a+b); for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<10;j++) { if ( $\mathrm { ~  ~ x ~ } = = \mathrm { ~  ~ 0 ~ }$ . || $\begin{array} { r } { \mathbf { x } \ = = \ 1 . } \end{array}$ ) return x; a or $^ { b }$ too small for accurate calcuerr $=$ betai(a,b,x) - p; lation. $\begin{array} { r l } { \tplus } & { { } = } \end{array}$ exp(a1\*log(x)+b1\*log(1.-x) $^ +$ afac); $u \ =$ err/t; Halley: $\begin{array} { r l } { \mathbf { x } } & { { } - = } \end{array}$ (t = u/(1.-0.5\*MIN(1.,u\*(a1/x - b1/(1.-x))))); if $\mathbf { \Phi } _ { \mathbf { x } } \mathbf { \Phi } < = \mathbf { \Phi } 0 .$ ) $\textbf { x } = ~ 0 \ : . 5 * ( \textbf { x } + \textbf { t } )$ ; Bisect if $x$ tries to go neg or $> 1$ . if $\mathbf { \Psi } ( \mathbf { x _ { \alpha } } > = \mathbf { \Psi } 1 .$ ) $\textbf { x } = \ 0 . 5 * ( \textbf { x } + \textbf { t } + \textbf { 1 . } )$ ; if (fabs(t) $<$ EPS\*x && ${ \\mathrm { ~ j ~ } } > { \mathrm { ~ 0 ~ } } ,$ ) break; } return x; } onst Doub Beta::EPS $=$ numeric_limits<Doub>::epsilon(); onst Doub Beta::FPMIN $=$ numeric_limits<Doub>::min()/EPS;

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapters 6 and 26.[1]   
Pearson, E., and Johnson, N. 1968, Tables of the Incomplete Beta Function (Cambridge, UK: Cambridge University Press).

# 6.5 Bessel Functions of Integer Order

This section presents practical algorithms for computing various kinds of Bessel functions of integer order. In $\ S 6 . 6$ we deal with fractional order. Actually, the more complicated routines for fractional order work fine for integer order too. For integer order, however, the routines in this section are simpler and faster.

For any real $\nu$ , the Bessel function $J _ { \nu } ( x )$ can be defined by the series representation

$$
J _ { \nu } ( x ) = \left( { \frac { 1 } { 2 } } x \right) ^ { \nu } \sum _ { k = 0 } ^ { \infty } { \frac { ( - { \frac { 1 } { 4 } } x ^ { 2 } ) ^ { k } } { k ! \Gamma ( \nu + k + 1 ) } }
$$

The series converges for all $x$ , but it is not computationally very useful for $x \gg 1$ .

For $\nu$ not an integer, the Bessel function $Y _ { \nu } ( x )$ is given by

$$
Y _ { \nu } ( x ) = \frac { J _ { \nu } ( x ) \cos ( \nu \pi ) - J _ { - \nu } ( x ) } { \sin ( \nu \pi ) }
$$

The right-hand side goes to the correct limiting value $Y _ { n } ( x )$ as $\nu$ goes to some integer $n$ , but this is also not computationally useful.

For arguments $x \_ { \nu }$ , both Bessel functions look qualitatively like simple power laws, with the asymptotic forms for $0 < x \ll \nu$

$$
\begin{array} { l l l } { { J _ { \nu } ( x ) \sim \displaystyle { \frac { 1 } { \Gamma ( \nu + 1 ) } } \left( \frac { 1 } { 2 } x \right) ^ { \nu } } } & { { ~ \nu \geq 0 } } \\ { { \displaystyle Y _ { 0 } ( x ) \sim \frac { 2 } { \pi } \ln ( x ) } } & { { } } \\ { { \displaystyle Y _ { \nu } ( x ) \sim - \frac { \Gamma ( \nu ) } { \pi } \left( \frac { 1 } { 2 } x \right) ^ { - \nu } } } & { { ~ \nu > 0 } } \end{array}
$$

For $x > \nu$ , both Bessel functions look qualitatively like sine or cosine waves whose amplitude decays as $x ^ { - 1 / 2 }$ . The asymptotic forms for $x \gg \nu$ are

$$
\begin{array} { l } { { J _ { \nu } ( x ) \sim \displaystyle { \sqrt { \frac { 2 } { \pi x } } } \cos \left( x - \frac { 1 } { 2 } \nu \pi - \frac { 1 } { 4 } \pi \right) } } \\ { { { \cal Y } _ { \nu } ( x ) \sim \displaystyle { \sqrt { \frac { 2 } { \pi x } } } \sin \left( x - \frac { 1 } { 2 } \nu \pi - \frac { 1 } { 4 } \pi \right) } } \end{array}
$$

In the transition region where $x \sim \nu$ , the typical amplitudes of the Bessel functions are on the order

$$
\begin{array} { l } { { J _ { \nu } ( \nu ) \sim \displaystyle { \frac { 2 ^ { 1 / 3 } } { 3 ^ { 2 / 3 } \Gamma ( \frac 2 3 ) } \frac { 1 } { \nu ^ { 1 / 3 } } \sim \frac { 0 . 4 4 7 3 } { \nu ^ { 1 / 3 } } } } } \\ { { { } } } \\ { { Y _ { \nu } ( \nu ) \sim \displaystyle { - \frac { 2 ^ { 1 / 3 } } { 3 ^ { 1 / 6 } \Gamma ( \frac 2 3 ) } \frac { 1 } { \nu ^ { 1 / 3 } } \sim - \frac { 0 . 7 7 4 8 } { \nu ^ { 1 / 3 } } } } } \end{array}
$$

which holds asymptotically for large $\nu$ . Figure 6.5.1 plots the first few Bessel functions of each kind.

The Bessel functions satisfy the recurrence relations

$$
J _ { n + 1 } ( x ) = { \frac { 2 n } { x } } J _ { n } ( x ) - J _ { n - 1 } ( x )
$$

![](images/13d54d90b9747a75c776bde5199a54e6315e13ea0b36c434ad3a8ba60cdcd814.jpg)  
Figure 6.5.1. Bessel functions $J _ { 0 } ( x )$ through $J _ { 3 } ( x )$ and $Y _ { 0 } ( x )$ through $Y _ { 2 } ( x )$ .

and

$$
Y _ { n + 1 } ( x ) = { \frac { 2 n } { x } } Y _ { n } ( x ) - Y _ { n - 1 } ( x )
$$

As already mentioned in $\ S 5 . 4$ , only the second of these, (6.5.7), is stable in the direction of increasing $n$ for $x < n$ . The reason that (6.5.6) is unstable in the direction of increasing $n$ is simply that it is the same recurrence as (6.5.7): A small amount of “polluting” $Y _ { n }$ introduced by roundoff error will quickly come to swamp the desired $J _ { n }$ , according to equation (6.5.3).

A practical strategy for computing the Bessel functions of integer order divides into two tasks: first, how to compute $J _ { 0 } , J _ { 1 } , Y _ { 0 }$ , and $Y _ { 1 }$ ; and second, how to use the recurrence relations stably to find other $J$ ’s and $Y$ ’s. We treat the first task first.

For $x$ between zero and some arbitrary value (we will use the value 8), approximate $J _ { 0 } ( x )$ and $J _ { 1 } ( x )$ by rational functions in $x$ . Likewise approximate by rational functions the “regular part” of $Y _ { 0 } ( x )$ and $Y _ { 1 } ( x )$ , defined as

$$
Y _ { 0 } ( x ) - { \frac { 2 } { \pi } } J _ { 0 } ( x ) \ln ( x ) \qquad { \mathrm { a n d } } \qquad Y _ { 1 } ( x ) - { \frac { 2 } { \pi } } \left[ J _ { 1 } ( x ) \ln ( x ) - { \frac { 1 } { x } } \right]
$$

For $8 < x < \infty$ , use the approximating forms $( n = 0 , 1$ )

$$
{ \begin{array} { r } { J _ { n } ( x ) = { \sqrt { \frac { 2 } { \pi x } } } { \biggl [ } P _ { n } { \biggl ( } { \frac { 8 } { x } } { \biggr ) } \cos ( X _ { n } ) - Q _ { n } { \biggl ( } { \frac { 8 } { x } } { \biggr ) } \sin ( X _ { n } ) { \biggr ] } } \\ { Y _ { n } ( x ) = { \sqrt { \frac { 2 } { \pi x } } } { \biggl [ } P _ { n } { \biggl ( } { \frac { 8 } { x } } { \biggr ) } \sin ( X _ { n } ) + Q _ { n } { \biggl ( } { \frac { 8 } { x } } { \biggr ) } \cos ( X _ { n } ) { \biggr ] } } \end{array} }
$$

where

$$
X _ { n } \equiv x - \frac { 2 n + 1 } { 4 } \pi
$$

and where $P _ { 0 } , P _ { 1 } , Q _ { 0 }$ , and $Q _ { 1 }$ are each polynomials in their arguments, for $0 ~ <$ $8 / x < 1$ . The $P$ ’s are even polynomials, the $Q$ ’s odd.

In the routines below, the various coefficients were calculated in multiple precision so as to achieve full double precision in the relative error. (In the neighborhood of the zeros of the functions, it is the absolute error that is double precision.) However, because of roundoff, evaluating the approximations can lead to a loss of up to two significant digits.

One additional twist: The rational approximation for $\ 0 \ < \ x \ < \ 8$ is actually computed in the form [1]

$$
J _ { 0 } ( x ) = ( x ^ { 2 } - x _ { 0 } ^ { 2 } ) ( x ^ { 2 } - x _ { 1 } ^ { 2 } ) \frac { r ( x ^ { 2 } ) } { s ( x ^ { 2 } ) }
$$

and similarly for $J _ { 1 } , \ Y _ { 0 }$ and $Y _ { 1 }$ . Here $x _ { 0 }$ and $x _ { 1 }$ are the two zeros of $J _ { 0 }$ in the interval, and $r$ and $s$ are polynomials. The polynomial $r ( x ^ { 2 } )$ has alternating signs. Writing it in terms of $6 4 - x ^ { 2 }$ makes all the signs the same and reduces roundoff error. For the approximations (6.5.9) and (6.5.10), our coefficients are similar but not identical to those given by Hart [2].

The functions $J _ { 0 } , J _ { 1 } , Y _ { 0 }$ , and $Y _ { 1 }$ share a lot of code, so we package them as a single object Bessjy. The routines for higher $J _ { n }$ and $Y _ { n }$ are also member functions, with implementations discussed below. All the numerical coefficients are declared in Bessjy but defined (as a long list of constants) separately; the listing is in a Webnote [3].

# struct Bessjy {

static const Doub xj00,xj10,xj01,xj11,twoopi,pio4;   
static const Doub j0r[7],j0s[7],j0pn[5],j0pd[5],j0qn[5],j0qd[5];   
static const Doub j1r[7],j1s[7],j1pn[5],j1pd[5],j1qn[5],j1qd[5];   
static const Doub y0r[9],y0s[9],y0pn[5],y0pd[5],y0qn[5],y0qd[5];   
static const Doub y1r[8],y1s[8],y1pn[5],y1pd[5],y1qn[5],y1qd[5];   
Doub nump,denp,numq,denq,y,z,ax,xx;

# Doub j0(const Doub x) {

Returns the Bessel function $J _ { 0 } ( \mathbf { x } )$ for any real x.

if ((ax=abs(x)) $<$ 8.0) { Direct rational function fit. rat(x,j0r,j0s,6); return nump\*(y-xj00)\*(y-xj10)/denp; } else { Fitting function (6.5.9). asp(j0pn,j0pd,j0qn,j0qd,1.); return sqrt(twoopi/ax)\*(cos(xx)\*nump/denp-z\*sin(xx)\*numq/denq); } }

# Doub j1(const Doub x) {

Returns the Bessel function $J _ { 1 } ( \mathbf { x } )$ for any real x. if ((ax=abs(x)) $<$ 8.0) { Direct rational approximation. rat(x,j1r,j1s,6); return $\mathrm { { x * n u m p * ( y ^ { - } x j 0 1 ) * ( y ^ { - } x j 1 1 ) / d e n p } ; }$ } else { Fitting function (6.5.9). asp(j1pn,j1pd,j1qn,j1qd,3.); Doub ans $=$ sqrt(twoopi/ax) $^ *$ (cos(xx)\*nump/denp-z\*sin(xx)\*numq/denq); return $\mathrm { ~ x ~ } > \ 0 . 0$ ? ans : -ans; }

Doub y0(const Doub x) {   
Returns the Bessel function $Y _ { 0 } ( \mathbf { x } )$ for positive x. if $\mathrm { ~ ( ~ x ~ < ~ } 8 . 0 \mathrm { ) }$ ) Rational function approximation of (6.5.8). Doub $\mathrm { j } 0 \mathbf { x } \ = \ \mathrm { j } 0 \left( \mathbf { x } \right)$ ; rat(x,y0r,y0s,8); return nump/denp+twoopi\*j0x\*log(x); } else { Fitting function (6.5.10). $\mathtt { a x } \mathrm { = x }$ ; asp(y0pn,y0pd,y0qn,y0qd,1.); return sqrt(twoopi/x)\*(sin(xx)\*nump/denp+z\*cos(xx)\*numq/denq); }   
Doub y1(const Doub x) {   
Returns the Bessel function $Y _ { 1 } ( \mathbf { x } )$ for positive x. if $\mathit { \Theta } _ { \overline { { \mathbf { X } } } } ~ < ~ 8 . 0$ ) { Rational function approximation of (6.5.8). Doub $\mathrm { j } 1 \mathrm { x } \ = \ \mathrm { j } 1 ( \mathrm { x } )$ ; rat(x,y1r,y1s,7); return x\*nump/denp+twoopi\*(j1x\*log(x)-1.0/x); } else { Fitting function (6.5.10). $\mathtt { a x } \mathrm { = x }$ ; asp(y1pn,y1pd,y1qn,y1qd,3.); return sqrt(twoopi/x)\*(sin(xx)\*nump/denp+z\*cos(xx)\*numq/denq); }   
} Doub jn(const Int n, const Doub x);   
Returns the Bessel function $J _ { \mathtt { n } } ( \mathbf { x } )$ for any real x and integer $\mathbf { n } \geq \mathbf { 0 }$ . Doub yn(const Int n, const Doub x);   
Returns the Bessel function $Y _ { \mathrm { { n } } } ( \mathbf { x } )$ for any positive x and integer $\mathbf { n } \geq \mathbf { 0 }$ .

void rat(const Doub x, const Doub \*r, const Doub \*s, const Int n) { Common code: Evaluates rational approximation.

$\begin{array} { r } { \mathrm { ~ y ~ } = \mathrm { ~ x * x } , } \end{array}$ $\scriptstyle 2 = 6 4 . 0 - y$ ; nump ${ } = \mathbf { r }$ [n]; denp=s[n]; for (Int $\dot { \tt 1 } = { \tt n } - 1$ ; $\scriptstyle \dot { 1 } > = 0$ ;i--) nump=nump\*z+r[i]; denp=denp\*y+s[i]; } }

void asp(const Doub \*pn, const Doub \*pd, const Doub \*qn, const Doub \*qd,   
Common code: Evaluates asymptotic approximation. const Doub fac) { $z { = } 8$ .0/ax; y=z\*z; xx=ax-fac\*pio4; nump=pn[4]; denp=pd[4]; numq=qn[4]; denq=qd[4]; for (Int i=3;i>=0;i--) { nump $\mid =$ nump\*y+pn[i]; denp=denp\*y+pd[i]; numq=numq\*y+qn[i]; denq=denq\*y+qd[i]; }   
}

We now turn to the second task, namely, how to use the recurrence formulas (6.5.6) and (6.5.7) to get the Bessel functions $J _ { n } ( x )$ and $Y _ { n } ( x )$ for $n \geq 2$ . The latter of these is straightforward, since its upward recurrence is always stable:

Doub Bessjy::yn(const Int n, const Doub x)   
Returns the Bessel function $Y _ { \mathrm { n } } ( \mathbf { x } )$ for any positive $\mathbf { x }$ and integer $\mathbf { n } \geq \mathbf { 0 }$ . {

Int j; Doub by,bym,byp,tox; if ( $\scriptstyle \mathtt { n } = = 0$ ) return y0(x); if ( $\scriptstyle \mathtt { n } = = 1$ ) return y1(x); tox $^ { = 2 }$ .0/x; by=y1(x); bym=y0(x); for ( $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<n;j++) { byp=j\*tox\*by-bym; bym=by; by $=$ byp; } return by; }

The cost of this algorithm is the calls to y1 and y0 (which generate a call to each of ${ \dot { \mathsf { J } } } ^ { 1 }$ and ${ \bf j } 0$ ), plus $O ( n )$ operations in the recurrence.

For $J _ { n } ( x )$ , things are a bit more complicated. We can start the recurrence upward on $n$ from $J _ { 0 }$ and $J _ { 1 }$ , but it will remain stable only while $n$ does not exceed $x$ . This is, however, just fine for calls with large $x$ and small $n$ , a case that occurs frequently in practice.

The harder case to provide for is that with $x \ < \ n$ . The best thing to do here is to use Miller’s algorithm (see discussion preceding equation 5.4.16), applying the recurrence downward from some arbitrary starting value and making use of the upward-unstable nature of the recurrence to put us onto the correct solution. When we finally arrive at $J _ { 0 }$ or $J _ { 1 }$ we are able to normalize the solution with the sum (5.4.16) accumulated along the way.

The only subtlety is in deciding at how large an $n$ we need start the downward recurrence so as to obtain a desired accuracy by the time we reach the $n$ that we really want. If you play with the asymptotic forms (6.5.3) and (6.5.5), you should be able to convince yourself that the answer is to start larger than the desired $n$ by an additive amount of order $[ \mathrm { c o n s t a n t } \times n ] ^ { 1 / 2 }$ , where the square root of the constant is, very roughly, the number of significant figures of accuracy.

The above considerations lead to the following function.

# bessel.h

Doub Bessjy::jn(const Int n, const Doub x) Returns the Bessel function $J _ { \mathrm { { n } } } ( \mathbf { x } )$ for any real $\mathbf { x }$ and integer $\mathbf { n } \geq \mathbf { 0 }$ . {

const Doub $\mathtt { A C C = 1 6 0 . 0 }$ ; ACC determines accuracy.   
const Int IEXP $^ { 1 } =$ numeric_limits<Doub>::max_exponent/2;   
Bool jsum;   
Int j,k,m;   
Doub ax,bj,bjm,bjp,dum,sum,tox,ans;   
if ( $\scriptstyle \mathtt { n } = = 0$ ) return ${ \bf j } 0 ( { \bf x } )$ ;   
if ( $\scriptstyle \mathbf { \cdot n } = = 1$ ) return j1 $\left( \mathbf { \boldsymbol { x } } \right)$ ;   
ax=abs(x);   
if (ax\*ax $< =$ 8.0\*numeric_limits<Doub>::min()) return 0.0;   
else if (ax $>$ Doub(n)) { Upwards recurrence from $J _ { 0 }$ and $J _ { 1 }$ .   
tox $^ { = 2 }$ .0/ax;

bjm=j0(ax); bj=j1(ax); for (j=1;j<n;j++) { bjp=j\*tox\*bj-bjm; bjm=bj; bj=bjp; } ans $=$ bj; } else { Downward recurrence from an even m here tox $^ { - 2 }$ .0/ax; computed. ${ \tt m } = 2 *$ ((n+Int(sqrt(ACC\*n)))/2); jsum=false; jsum will alternate between false and true; bjp=ans $=$ sum=0.0; when it is true, we accumulate in sum bj=1.0; the even terms in (5.4.16). for (j=m;j>0;j--) { The downward recurrence. bjm=j\*tox\*bj-bjp; bjp=bj; bj=bjm; dum=frexp(bj,&k); if (k $>$ IEXP) { Renormalize to prevent overflows. bj ${ } = 1$ dexp(bj,-IEXP); bjp $\mid =$ ldexp(bjp,-IEXP); ans $: =$ ldexp(ans,-IEXP); sum=ldexp(sum,-IEXP); if (jsum) sum $+ =$ bj; Accumulate the sum. jsum=!jsum; Change false to true or vice versa. if (j == n) ans=bjp; Save the unnormalized answer. } sum $^ { 1 = 2 }$ .0\*sum-bj; Compute (5.4.16) ans /= sum; and use it to normalize the answer. } return $\texttt { x } < 0 . 0$ && (n & 1) ? -ans : ans;

The function ldexp, used above, is a standard C and $\mathrm { C } { + } { + }$ library function for scaling the binary exponent of a number.

# 6.5.1 Modified Bessel Functions of Integer Order

The modified Bessel functions $I _ { n } ( x )$ and $K _ { n } ( x )$ are equivalent to the usual Bessel functions $J _ { n }$ and $Y _ { n }$ evaluated for purely imaginary arguments. In detail, the relationship is

$$
\begin{array} { l } { { I _ { n } ( x ) = ( - i ) ^ { n } J _ { n } ( i x ) } } \\ { { K _ { n } ( x ) = \displaystyle \frac { \pi } { 2 } i ^ { n + 1 } [ J _ { n } ( i x ) + i Y _ { n } ( i x ) ] } } \end{array}
$$

The particular choice of prefactor and of the linear combination of $J _ { n }$ and $Y _ { n }$ to form $K _ { n }$ are simply choices that make the functions real-valued for real arguments $x$ .

For small arguments $x ~ \ll ~ n$ , both $I _ { n } ( x )$ and $K _ { n } ( x )$ become, asymptotically, simple powers of their arguments

$$
{ \begin{array} { l } { \displaystyle I _ { n } ( x ) \approx { \frac { 1 } { n ! } } \left( { \frac { x } { 2 } } \right) ^ { n } \qquad n \geq 0 } \\ { \displaystyle K _ { 0 } ( x ) \approx - \ln ( x ) } \\ { \displaystyle K _ { n } ( x ) \approx { \frac { ( n - 1 ) ! } { 2 } } \left( { \frac { x } { 2 } } \right) ^ { - n } \qquad n > 0 } \end{array} }
$$

These expressions are virtually identical to those for $J _ { n } ( x )$ and $Y _ { n } ( x )$ in this region, except for the factor of $- 2 / \pi$ difference between $Y _ { n } ( x )$ and $K _ { n } ( x )$ . In the region $x \gg n$ , however, the modified functions have quite different behavior than the Bessel functions,

$$
\begin{array} { l } { { I _ { n } ( x ) \approx \displaystyle \frac { 1 } { \sqrt { 2 \pi x } } \exp ( x ) } } \\ { { K _ { n } ( x ) \approx \displaystyle \frac { \pi } { \sqrt { 2 \pi x } } \exp ( - x ) } } \end{array}
$$

The modified functions evidently have exponential rather than sinusoidal behavior for large arguments (see Figure 6.5.2). Rational approximations analogous to those for the $J$ and $Y$ Bessel functions are efficient for computing $I _ { 0 }$ , $I _ { 1 }$ , $K _ { 0 }$ , and $K _ { 1 }$ . The corresponding routines are packaged as an object Bessik. The routines are similar to those in [1], although different in detail. (All the constants are again listed in a Webnote [3].)

# struct Bessik {

static const Doub i0p[14],i0q[5],i0pp[5],i0qq[6];   
static const Doub i1p[14],i1q[5],i1pp[5],i1qq[6];   
static const Doub k0pi[5],k0qi[3],k0p[5],k0q[3],k0pp[8],k0qq[8];   
static const Doub k1pi[5],k1qi[3],k1p[5],k1q[3],k1pp[8],k1qq[8];   
Doub y,z,ax,term;   
Doub i0(const Doub x) {   
Returns the modified Bessel function $I _ { 0 } ( \mathbf { x } )$ for any real $\mathbf { x }$ . if ((ax=abs(x)) $<$ 15.0) { Rational approximation. $\begin{array} { r } { \mathbf { y } ~ = ~ \mathbf { x } * \mathbf { x } } \end{array}$ ; return poly(i0p,13,y)/poly(i0q,4,225.-y); } else { Rational approximation with $e ^ { x } / { \sqrt { x } }$ factored out. $z { = } 1$ .0-15.0/ax; return exp(ax)\*poly(i0pp,4,z)/(poly(i0qq,5,z)\*sqrt(ax)); }   
}   
Doub i1(const Doub x) {   
Returns the modified Bessel function $I _ { 1 } ( \mathbf { x } )$ for any real $\mathbf { x }$ . if ((ax=abs(x)) $<$ 15.0) { Rational approximation. $\mathtt { y } \mathtt { = x } \ast \mathtt { x }$ ; return x\*poly(i1p,13,y)/poly(i1q,4,225.-y); } else { Rational approximation with $e ^ { x } / { \sqrt { x } }$ factored out. z=1.0-15.0/ax; Doub ans $=$ exp(ax)\*poly(i1pp,4,z)/(poly(i1qq,5,z)\*sqrt(ax)); return $\mathrm { ~ x ~ } > \ 0 . 0$ ? ans : -ans; }   
}   
Doub k0(const Doub x) {   
Returns the modified Bessel function $K _ { 0 } ( \mathbf { x } )$ for positive real x. if $( \textbf { x } < = \textbf { 1 } . 0 )$ ) { Use two rational approximations. ${ \bf z } = { \bf x } * { \bf x }$ ; term $=$ poly(k0pi,4,z)\*log(x)/poly(k0qi,2,1.-z); return poly(k0p,4,z)/poly(k0q,2,1.-z)-term; } else { Rational approximation with $e ^ { - x } / { \sqrt { x } }$ factored $\scriptstyle { z = 1 . 0 / \mathbf { x } }$ ; out. return exp(-x)\*poly(k0pp,7,z)/(poly(k0qq,7,z)\*sqrt(x)); }   
Doub k1(const Doub x) {   
Returns the modified Bessel function $K _ { 1 } ( \mathbf { x } )$ for positive real x. if ( $\mathit { \check { x } } < = \mathit { 1 . 0 } \rangle$ ) { Use two rational approximations. ${ z } = \mathbf { x } * \mathbf { x }$ ; term $=$ poly(k1pi,4,z)\*log(x)/poly(k1qi,2,1.-z); return x\*(poly(k1p,4,z)/poly(k1q,2,1.-z)+term) $^ { + 1 }$ ./x; } else { Rational approximation with $e ^ { - x } / { \sqrt { x } }$ factored $z { = } 1$ .0/x; out. return exp(-x)\*poly(k1pp,7,z)/(poly(k1qq,7,z)\*sqrt(x)); }   
} Doub in(const Int n, const Doub x);   
Returns the modified Bessel function $I _ { \mathrm { { n } } } ( \mathbf { x } )$ for any real $\mathbf { x }$ and $\mathbf { n } \geq \mathbf { 0 }$ . Doub kn(const Int n, const Doub x);   
Returns the modified Bessel function $K _ { \mathfrak { n } } ( \mathbf { x } )$ for positive $\mathbf { x }$ and $\mathbf { n } \geq \mathbf { 0 }$ .

![](images/4f814f447313a9e5005e7a798908c820e15655723b52b327ba57005a123aa308.jpg)  
Figure 6.5.2. Modified Bessel functions $I _ { 0 } ( x )$ through $I _ { 3 } ( x )$ , and $K _ { 0 } ( x )$ through $K _ { 2 } ( x )$ .

inline Doub poly(const Doub \*cof, const Int n, const Doub x) { Common code: Evaluate a polynomial. Doub ans $=$ cof[n]; for (Int i=n $- 1 ; \mathrm { i } > = 0 ; \mathrm { i } -- )$ ans $=$ ans\*x+cof[i]; return ans; } };

The recurrence relation for $I _ { n } ( x )$ and $K _ { n } ( x )$ is the same as that for $J _ { n } ( x )$ and $Y _ { n } ( x )$ provided that $i x$ is substituted for $x$ . This has the effect of changing a sign in the relation,

$$
\begin{array} { l } { { I _ { n + 1 } ( x ) = - \displaystyle \left( \frac { 2 n } { x } \right) I _ { n } ( x ) + I _ { n - 1 } ( x ) } } \\ { { { } } } \\ { { K _ { n + 1 } ( x ) = + \displaystyle \left( \frac { 2 n } { x } \right) K _ { n } ( x ) + K _ { n - 1 } ( x ) } } \end{array}
$$

These relations are always unstable for upward recurrence. For $K _ { n }$ , itself growing, this presents no problem. The implementation is

# bessel.h

Doub Bessik::kn(const Int n, const Doub x) Returns the modified Bessel function $K _ { \mathfrak { n } } ( \mathbf { x } )$ for positive $\mathbf { x }$ and $\mathbf { n } \geq \mathbf { 0 }$ . {

Int j; Doub bk,bkm,bkp,tox; if ( $\scriptstyle \mathtt { n } = = 0$ ) return k0 $\mathbf { \Psi } ( \mathbf { x } )$ ; if ( $\scriptstyle \mathtt { n } = = 1$ ) return k1 $\mathbf { \Psi } ( \mathbf { x } )$ ; to $= 2$ .0/x; bkm=k0(x); bk=k1(x); for ( $\mathrm { j } = 1$ ;j<n;j++) { bkp=bkm+j\*tox\*bk; bkm $\mathbf { \tau } _ { 1 } =$ bk; bk $\ c =$ bkp; 1 return bk; }

For $I _ { n }$ , the strategy of downward recursion is required once again, and the starting point for the recursion may be chosen in the same manner as for the routine Bessjy::jn. The only fundamental difference is that the normalization formula for $I _ { n } ( x )$ has an alternating minus sign in successive terms, which again arises from the substitution of $i x$ for $x$ in the formula used previously for $J _ { n }$ :

$$
1 = I _ { 0 } ( x ) - 2 I _ { 2 } ( x ) + 2 I _ { 4 } ( x ) - 2 I _ { 6 } ( x ) + \cdots
$$

In fact, we prefer simply to normalize with a call to i0.

Doub Bessik::in(const Int n, const Doub x) Returns the modified Bessel function $I _ { \mathrm { { n } } } ( \mathbf { x } )$ for any real $\mathbf { x }$ and $\mathbf { n } \geq \mathbf { 0 }$ . {

const Doub ACC=200.0; ACC determines accuracy.   
const Int IEXP $^ { \prime } =$ numeric_limits<Doub>::max_exponent/2;   
Int j,k;   
Doub bi,bim,bip,dum,tox,ans;   
if ( $\scriptstyle \cdot = = 0$ ) return i0 $\left( \mathbf { \boldsymbol { x } } \right)$ ;   
if ( $\scriptstyle \mathbf { \cdot n } = = 1$ ) return i1 $\left( \mathbf { \boldsymbol { x } } \right)$ ;   
if (x\*x <= 8. $^ { 0 * }$ numeric_limits<Doub>::min()) return 0.0;   
else { tox $^ { - 2 }$ .0/abs(x); bip $\mid =$ ans=0.0; b $\lrcorner = 1$ .0; for (j $= 2 *$ ( $\mathrm { \Omega } \mathrm { n } +$ Int(sqrt(ACC $\ast \mathrm { n } ,$ )));j>0;j--) { Downward recurrence. bim bip+j\*tox\*bi; bip=bi; bi=bim; dum=frexp(bi,&k); if (k $>$ IEXP) { Renormalize to prevent overflows. ans $=$ ldexp(ans,-IEXP); bi $=$ ldexp(bi,-IEXP); bip=ldexp(bip,-IEXP);

} if (j == n) ans=bip; 1 ans $\ast =$ i0(x)/bi; Normalize with bessi0. return $\mathrm { ~ z ~ < ~ 0 ~ . 0 ~ }$ && (n & 1) ? -ans : ans; } }

The function ldexp, used above, is a standard C and $\mathrm { C } { + } { + }$ library function for scaling the binary exponent of a number.

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapter 9.   
Carrier, G.F., Krook, M. and Pearson, C.E. 1966, Functions of a Complex Variable (New York: McGraw-Hill), pp. 220ff.   
SPECFUN, $^ { 2 0 0 7 + }$ ,athttp://www.netlib.org/specfun.[1]   
Hart, J.F., et al. 1968, Computer Approximations (New York: Wiley), $\ S 6 . 8$ , p. 141.[2]   
Numerical Recipes Software 2007, “Coefficients Used in the Bessjy and Bessik Objects,” Numerical Recipes Webnote No.7,at http://www.nr.com/webnotes?7 [3]

# 6.6 Bessel Functions of Fractional Order, Airy Functions, Spherical Bessel Functions

Many algorithms have been proposed for computing Bessel functions of fractional order numerically. Most of them are, in fact, not very good in practice. The routines given here are rather complicated, but they can be recommended wholeheartedly.

# 6.6.1 Ordinary Bessel Functions

The basic idea is Steed’s method, which was originally developed [1] for Coulomb wave functions. The method calculates $J _ { \nu }$ , $J _ { \nu } ^ { \prime }$ , $Y _ { \nu }$ , and $\bar { Y } _ { \nu } ^ { \prime }$ simultaneously, and so involves four relations among these functions. Three of the relations come from two continued fractions, one of which is complex. The fourth is provided by the Wronskian relation

$$
W \equiv J _ { \nu } Y _ { \nu } ^ { \prime } - Y _ { \nu } J _ { \nu } ^ { \prime } = { \frac { 2 } { \pi x } }
$$

The first continued fraction, CF1, is defined by

$$
\begin{array}{c} f _ { \nu } \equiv \frac { J _ { \nu } ^ { \prime } } { J _ { \nu } } = \frac { \nu } { x } - \frac { J _ { \nu + 1 } } { J _ { \nu } }  \\ { = \frac { \nu } { x } - \frac { 1 } { 2 ( \nu + 1 ) / x - } \frac { 1 } { 2 ( \nu + 2 ) / x - } \dots } \end{array}
$$

You can easily derive it from the three-term recurrence relation for Bessel functions: Start with equation (6.5.6) and use equation (5.4.18). Forward evaluation of the continued fraction by one of the methods of $\ S 5 . 2$ is essentially equivalent to backward recurrence of the recurrence relation. The rate of convergence of CF1 is determined by the position of the turning point $x _ { \mathrm { t p } } = \sqrt { \nu ( \nu + 1 ) } \approx \nu$ , beyond which the Bessel functions become oscillatory. If $x \lesssim x _ { \mathrm { t p } }$ , convergence is very rapid. If $x \gtrsim x _ { \mathrm { t p } }$ , then each iteration of the continued fraction effectively increases $\nu$ by one until $x \lesssim x _ { \mathrm { t p } }$ ; thereafter rapid convergence sets in. Thus the number of iterations of CF1 is of order $x$ for large $x$ . In the routine besseljy we set the maximum allowed number of iterations to 10,000. For larger $x$ , you can use the usual asymptotic expressions for Bessel functions.

One can show that the sign of $J _ { \nu }$ is the same as the sign of the denominator of CF1 once it has converged.

The complex continued fraction CF2 is defined by

$$
p + i q \equiv \frac { J _ { \nu } ^ { \prime } + i Y _ { \nu } ^ { \prime } } { J _ { \nu } + i Y _ { \nu } } = - \frac { 1 } { 2 x } + i + \frac { i } { x } \ : \frac { ( 1 / 2 ) ^ { 2 } - \nu ^ { 2 } } { 2 ( x + i ) + } \ : \frac { ( 3 / 2 ) ^ { 2 } - \nu ^ { 2 } } { 2 ( x + 2 i ) + } \ : \cdots
$$

(We sketch the derivation of CF2 in the analogous case of modified Bessel functions in the next subsection.) This continued fraction converges rapidly for $x \gtrsim x _ { \mathrm { t p } }$ , while convergence fails as $x \to 0$ . We have to adopt a special method for small $x$ , which we describe below. For $x$ not too small, we can ensure that $x \gtrsim x _ { \mathrm { t p } }$ by a stable recurrence of $J _ { \nu }$ and $J _ { \nu } ^ { \prime }$ downward to a value $\nu = \mu \lesssim x$ , thus yielding the ratio $f _ { \mu }$ at this lower value of $\nu$ . This is the stable direction for the recurrence relation. The initial values for the recurrence are

$$
J _ { \nu } = \mathrm { a r b i t r a r y } , \qquad J _ { \nu } ^ { \prime } = f _ { \nu } J _ { \nu } ,
$$

with the sign of the arbitrary initial value of $J _ { \nu }$ chosen to be the sign of the denominator of CF1. Choosing the initial value of $J _ { \nu }$ very small minimizes the possibility of overflow during the recurrence. The recurrence relations are

$$
\begin{array} { l } { { J _ { \nu - 1 } = \displaystyle \frac { \nu } { x } J _ { \nu } + J _ { \nu } ^ { \prime } } } \\ { { \ J _ { \nu - 1 } ^ { \prime } = \displaystyle \frac { \nu - 1 } { x } J _ { \nu - 1 } - J _ { \nu } } } \end{array}
$$

Once CF2 has been evaluated at $\nu = \mu$ , then with the Wronskian (6.6.1) we have enough relations to solve for all four quantities. The formulas are simplified by introducing the quantity

$$
\gamma \equiv \frac { p - f _ { \mu } } { q }
$$

Then

$$
\begin{array} { l } { { J _ { \mu } = \pm \left( \displaystyle \frac { W } { q + \gamma ( p - f _ { \mu } ) } \right) ^ { 1 / 2 } } } \\ { { J _ { \mu } ^ { \prime } = f _ { \mu } J _ { \mu } } } \\ { { Y _ { \mu } = \gamma J _ { \mu } } } \\ { { Y _ { \mu } ^ { \prime } = Y _ { \mu } \left( p + \displaystyle \frac { q } { \gamma } \right) } } \end{array}
$$

The sign of $J _ { \mu }$ in (6.6.7) is chosen to be the same as the sign of the initial $J _ { \nu }$ in (6.6.4).

Once all four functions have been determined at the value $\nu = \mu$ , we can find them at the original value of $\nu$ . For $J _ { \nu }$ and $J _ { \nu } ^ { \prime }$ , simply scale the values in (6.6.4) by the ratio of (6.6.7) to the value found after applying the recurrence (6.6.5). The quantities $Y _ { \nu }$ and $Y _ { \nu } ^ { \prime }$ can be found by starting with the values in (6.6.9) and (6.6.10) and using the stable upward recurrence

$$
Y _ { \nu + 1 } = { \frac { 2 \nu } { x } } Y _ { \nu } - Y _ { \nu - 1 }
$$

together with the relation

$$
Y _ { \nu } ^ { \prime } = { \frac { \nu } { x } } Y _ { \nu } - Y _ { \nu + 1 }
$$

Now turn to the case of small $x$ , when CF2 is not suitable. Temme [2] has given a good method of evaluating $Y _ { \nu }$ and $Y _ { \nu + 1 }$ , and hence $Y _ { \nu } ^ { \prime }$ from (6.6.12), by series expansions that

accurately handle the singularity as $x \to 0$ . The expansions work only for $| \nu | \leq 1 / 2$ , and so now the recurrence (6.6.5) is used to evaluate $f _ { \nu }$ at a value $\nu = \mu$ in this interval. Then one calculates $J _ { \mu }$ from

$$
J _ { \mu } = \frac { W } { Y _ { \mu } ^ { \prime } - Y _ { \mu } f _ { \mu } }
$$

and $J _ { \mu } ^ { \prime }$ from (6.6.8). The values at the original value of $\nu$ are determined by scaling as before, and the $Y$ ’s are recurred up as before.

Temme’s series are

$$
Y _ { \nu } = - \sum _ { k = 0 } ^ { \infty } c _ { k } g _ { k } \qquad Y _ { \nu + 1 } = - \frac { 2 } { x } \sum _ { k = 0 } ^ { \infty } c _ { k } h _ { k }
$$

Here

$$
c _ { k } = { \frac { ( - x ^ { 2 } / 4 ) ^ { k } } { k ! } }
$$

while the coefficients $g _ { k }$ and $h _ { k }$ are defined in terms of quantities $p _ { k } , q _ { k }$ , and $f _ { k }$ that can be found by recursion:

$$
{ \begin{array} { r l } & { g _ { k } = f _ { k } + { \frac { 2 } { \nu } } \sin ^ { 2 } \left( { \frac { \nu \pi } { 2 } } \right) q _ { k } } \\ & { h _ { k } = - k g _ { k } + p _ { k } } \\ & { p _ { k } = { \frac { p _ { k - 1 } } { k - \nu } } } \\ & { q _ { k } = { \frac { q _ { k - 1 } } { k + \nu } } } \\ & { f _ { k } = { \frac { k f _ { k - 1 } + p _ { k - 1 } + q _ { k - 1 } } { k ^ { 2 } - \nu ^ { 2 } } } } \end{array} }
$$

The initial values for the recurrences are

$$
\begin{array} { l } { { p _ { 0 } = \displaystyle \frac { 1 } { \pi } \left( \frac { x } { 2 } \right) ^ { - \nu } \Gamma ( 1 + \nu ) } } \\ { { q _ { 0 } = \displaystyle \frac { 1 } { \pi } \left( \frac { x } { 2 } \right) ^ { \nu } \Gamma ( 1 - \nu ) } } \\ { { f _ { 0 } = \displaystyle \frac { 2 } { \pi } \frac { \nu \pi } { \sin \nu \pi } \left[ \cosh \sigma \Gamma _ { 1 } ( \nu ) + \frac { \sinh \sigma } { \sigma } \ln \left( \frac { 2 } { x } \right) \Gamma _ { 2 } ( \nu ) \right] } } \end{array}
$$

with

$$
{ \begin{array} { c } { \displaystyle \sigma = \nu \ln \left( { \frac { 2 } { x } } \right) } \\ { \displaystyle \Gamma _ { 1 } ( \nu ) = { \frac { 1 } { 2 \nu } } \left[ { \frac { 1 } { \Gamma ( 1 - \nu ) } } - { \frac { 1 } { \Gamma ( 1 + \nu ) } } \right] } \\ { \displaystyle \Gamma _ { 2 } ( \nu ) = { \frac { 1 } { 2 } } \left[ { \frac { 1 } { \Gamma ( 1 - \nu ) } } + { \frac { 1 } { \Gamma ( 1 + \nu ) } } \right] } \end{array} }
$$

The whole point of writing the formulas in this way is that the potential problems as $\nu  0$ can be controlled by evaluating $\nu \pi / \sin \nu \pi$ , $\sinh \sigma / \sigma$ , and $\Gamma _ { 1 }$ carefully. In particular, Temme gives Chebyshev expansions for $\Gamma _ { 1 } ( \nu )$ and $\Gamma _ { 2 } ( \nu )$ . We have rearranged his expansion for $\Gamma _ { 1 }$ to be explicitly an even series in $\nu$ for more efficient evaluation, as explained in $\ S 5 . 8$ .

Because $J _ { \nu }$ , $Y _ { \nu }$ , $J _ { \nu } ^ { \prime }$ , and $Y _ { \nu } ^ { \prime }$ are all calculated simultaneously, a single void function sets them all. You then grab those that you need directly from the object. Alternatively, the functions $\dot { \mathtt { J } } \mathtt { n u }$ and ynu can be used. (We’ve omitted similar helper functions for the derivatives, but you can easily add them.) The object Bessel contains various other methods that will be discussed below.

The routines assume $\nu \geq 0$ . For negative $\nu$ you can use the reflection formulas

$$
\begin{array} { r } { J _ { - \nu } = \cos \nu \pi J _ { \nu } - \sin \nu \pi Y _ { \nu } } \\ { Y _ { - \nu } = \sin \nu \pi J _ { \nu } + \cos \nu \pi Y _ { \nu } } \end{array}
$$

The routine also assumes $x > 0$ . For $x < 0$ , the functions are in general complex but expressible in terms of functions with $x > 0$ . For $x = 0$ , $Y _ { \nu }$ is singular. The complex arithmetic is carried out explicitly with real variables.

# struct Bessel {

Object for Bessel functions of arbitrary order $\nu$ , and related functions.

static const Int NUSE1 $^ { . = 7 }$ , NUSE2 $\scriptstyle : = 8$ ;   
static const Doub c1[NUSE1],c2[NUSE2];   
Doub xo,nuo;   
Doub jo,yo,jpo,ypo;   
Doub io,ko,ipo,kpo;   
Doub aio,bio,aipo,bipo;   
Doub sphjo,sphyo,sphjpo,sphypo;   
Int sphno;

Bessel() : xo(9.99e99), nuo(9.99e99), sphno(-9999) {} Default constructor. No arguments.

void besseljy(const Doub nu, const Doub x); Calculate Bessel functions $J _ { \nu } ( x )$ and $Y _ { \nu } ( x )$ and their derivatives. void besselik(const Doub $\mathbf { n u }$ , const Doub x) Calculate Bessel functions $I _ { \nu } ( x )$ and $K _ { \nu } ( x )$ and their derivatives.

Doub jnu(const Doub nu, const Doub x) {   
Simple interface returning $J _ { \nu } ( x )$ . if (nu $! =$ nuo $| \textbf { | } \textbf { x } : = \textbf { x } 0 \ $ ) besseljy(nu,x); return jo;   
}   
Doub ynu(const Doub nu, const Doub x) {   
Simple interface returning $Y _ { \nu } ( x )$ . if (nu $! =$ nuo $| \mathbf { \Psi } | \subset \mathrm { ~ \mathbb { X } ~ } : = \mathrm { ~ \mathbb { X } \circ ~ }$ ) besseljy(nu,x); return yo;   
}   
Doub inu(const Doub nu, const Doub x) {   
Simple interface returning $I _ { \nu } ( x )$ . if (nu $! =$ nuo $| \textbf { | } \textbf { x } : = \textbf { x } 0 \ $ ) besselik(nu,x); return io;   
}   
Doub knu(const Doub nu, const Doub x) {   
Simple interface returning $K _ { \nu } ( x )$ . if $\mathrm {  ~ \ l u ~ } \ ! = \ \mathrm { \ n u o ~ } \ | \ | \ \mathrm {  ~ \ x ~ } \ ! = \ \mathrm { \ x o }$ ) besselik(nu,x); return ko;   
} void airy(const Doub x);   
Calculate Airy functions $\operatorname { A i } ( x )$ and $\operatorname { B i } ( x )$ and their derivatives.   
Doub airy_ai(const Doub x);   
Simple interface returning $\operatorname { A i } ( x )$ .   
Doub airy_bi(const Doub x);   
Simple interface returning $\operatorname { B i } ( x )$ . void sphbes(const Int n, const Doub x);   
Calculate spherical Bessel functions $j _ { n } ( x )$ and $y _ { n } ( x )$ and their derivatives.   
Doub sphbesj(const Int n, const Doub x);   
Simple interface returning $j _ { n } ( x )$ .   
Doub sphbesy(const Int $\mathbf { n }$ , const Doub x);   
Simple interface returning $y _ { n } ( x )$ .

inline Doub chebev(const Doub \*c, const Int m, const Doub x) { Utility used by besseljy and besselik, evaluates Chebyshev series.

Doub d=0.0,dd $\mathtt { = 0 }$ .0,sv; Int j; for (j=m-1;j>0;j--) { sv=d; d=2.\*x\*d-dd+c[j]; dd=sv; } return x\*d-dd+0.5\*c[0]; } };

const Doub Bessel::c1[7] $= \ \ell - 1$ .142022680371168e0,6.5165112670737e-3,   
3.087090173086e-4,-3.4706269649e-6,6.9437664e-9,3.67795e-11, -1.356e-13}; const Doub Bessel::c2[8] $=$ {1.843740587300905e0,-7.68528408447867e-2,   
1.2719271366546e-3,-4.9717367042e-6,-3.31261198e-8,2.423096e-10, -1.702e-13,-1.49e-15};

The code listing for Bessel::besseljy is in a Webnote [4].

# 6.6.2 Modified Bessel Functions

Steed’s method does not work for modified Bessel functions because in this case CF2 is purely imaginary and we have only three relations among the four functions. Temme [3] has given a normalization condition that provides the fourth relation.

The Wronskian relation is

$$
W \equiv I _ { \nu } K _ { \nu } ^ { \prime } - K _ { \nu } I _ { \nu } ^ { \prime } = - { \frac { 1 } { x } }
$$

The continued fraction CF1 becomes

$$
f _ { \nu } \equiv \frac { I _ { \nu } ^ { \prime } } { I _ { \nu } } = \frac { \nu } { x } + \frac { 1 } { 2 ( \nu + 1 ) / x + } \frac { 1 } { 2 ( \nu + 2 ) / x + } \cdots
$$

To get CF2 and the normalization condition in a convenient form, consider the sequence of confluent hypergeometric functions

$$
z _ { n } ( x ) = U ( \nu + 1 / 2 + n , 2 \nu + 1 , 2 x )
$$

for fixed $\nu$ . Then

$$
\begin{array} { c } { { K _ { \nu } ( x ) = \pi ^ { 1 / 2 } ( 2 x ) ^ { \nu } e ^ { - x } z _ { 0 } ( x ) } } \\ { { \displaystyle \frac { K _ { \nu + 1 } ( x ) } { K _ { \nu } ( x ) } = \frac { 1 } { x } \left[ \nu + \frac { 1 } { 2 } + x + \left( \nu ^ { 2 } - \frac { 1 } { 4 } \right) \frac { z _ { 1 } } { z _ { 0 } } \right] } } \end{array}
$$

Equation (6.6.23) is the standard expression for $K _ { \nu }$ in terms of a confluent hypergeometric function, while equation (6.6.24) follows from relations between contiguous confluent hypergeometric functions (equations 13.4.16 and 13.4.18 in Ref. [5]). Now the functions $z _ { n }$ satisfy the three-term recurrence relation (equation 13.4.15 in Ref. [5])

$$
z _ { n - 1 } ( x ) = b _ { n } z _ { n } ( x ) + a _ { n + 1 } z _ { n + 1 }
$$

with

$$
\begin{array} { c } { b _ { n } = 2 ( n + x ) } \\ { a _ { n + 1 } = - [ ( n + 1 / 2 ) ^ { 2 } - \nu ^ { 2 } ] } \end{array}
$$

Following the steps leading to equation (5.4.18), we get the continued fraction CF2

$$
{ \frac { z _ { 1 } } { z _ { 0 } } } = { \frac { 1 } { b _ { 1 } + } } { \frac { a _ { 2 } } { b _ { 2 } + } } \cdots
$$

from which (6.6.24) gives $K _ { \nu + 1 } / K _ { \nu }$ and thus $K _ { \nu } ^ { \prime } / K _ { \nu }$

Temme’s normalization condition is that

$$
\sum _ { n = 0 } ^ { \infty } C _ { n } z _ { n } = \left( \frac { 1 } { 2 x } \right) ^ { \nu + 1 / 2 }
$$

where

$$
C _ { n } = { \frac { ( - 1 ) ^ { n } } { n ! } } { \frac { \Gamma ( \nu + 1 / 2 + n ) } { \Gamma ( \nu + 1 / 2 - n ) } }
$$

Note that the $C _ { n }$ ’s can be determined by recursion:

$$
C _ { 0 } = 1 , \qquad C _ { n + 1 } = - \frac { a _ { n + 1 } } { n + 1 } C _ { n }
$$

We use the condition (6.6.28) by finding

$$
S = \sum _ { n = 1 } ^ { \infty } C _ { n } { \frac { z _ { n } } { z _ { 0 } } }
$$

Then

$$
z _ { 0 } = \left( \frac { 1 } { 2 x } \right) ^ { \nu + 1 / 2 } \frac { 1 } { 1 + S }
$$

and (6.6.23) gives $K _ { \nu }$

Thompson and Barnett [6] have given a clever method of doing the sum (6.6.31) simultaneously with the forward evaluation of the continued fraction CF2. Suppose the continued fraction is being evaluated as

$$
{ \frac { z _ { 1 } } { z _ { 0 } } } = \sum _ { n = 0 } ^ { \infty } \Delta h _ { n }
$$

where the increments $\Delta h _ { n }$ are being found by, e.g., Steed’s algorithm or the modified Lentz’s algorithm of $\ S 5 . 2$ . Then the approximation to $S$ keeping the first $N$ terms can be found as

$$
S _ { N } = \sum _ { n = 1 } ^ { N } Q _ { n } \Delta h _ { n }
$$

Here

$$
Q _ { n } = \sum _ { k = 1 } ^ { n } C _ { k } q _ { k }
$$

and $q _ { k }$ is found by recursion from

$$
q _ { k + 1 } = ( q _ { k - 1 } - b _ { k } q _ { k } ) / a _ { k + 1 }
$$

starting with $q _ { 0 } = 0$ , $q _ { 1 } = 1$ . For the case at hand, approximately three times as many terms are needed to get $S$ to converge as are needed simply for CF2 to converge.

To find $K _ { \nu }$ and $K _ { \nu + 1 }$ for small $x$ we use series analogous to (6.6.14):

$$
K _ { \nu } = \sum _ { k = 0 } ^ { \infty } c _ { k } f _ { k } \qquad K _ { \nu + 1 } = { \frac { 2 } { x } } \sum _ { k = 0 } ^ { \infty } c _ { k } h _ { k }
$$

Here

$$
\begin{array} { r l } & { c _ { k } = \frac { ( x ^ { 2 } / 4 ) ^ { k } } { k ! } } \\ & { h _ { k } = - k f _ { k } + p _ { k } } \\ & { p _ { k } = \frac { p _ { k - 1 } } { k - \nu } } \\ & { q _ { k } = \frac { q _ { k - 1 } } { k + \nu } } \\ & { f _ { k } = \frac { k f _ { k - 1 } + p _ { k - 1 } + q _ { k - 1 } } { k ^ { 2 } - \nu ^ { 2 } } } \end{array}
$$

The initial values for the recurrences are

$$
\begin{array} { l } { \displaystyle { p _ { 0 } = \frac { 1 } { 2 } \left( \frac { x } { 2 } \right) ^ { - \nu } \Gamma ( 1 + \nu ) } } \\ { \displaystyle { q _ { 0 } = \frac { 1 } { 2 } \left( \frac { x } { 2 } \right) ^ { \nu } \Gamma ( 1 - \nu ) } } \\ { \displaystyle { f _ { 0 } = \frac { \nu \pi } { \sin \nu \pi } \left[ \cosh \sigma \Gamma _ { 1 } ( \nu ) + \frac { \sinh \sigma } { \sigma } \ln \left( \frac { 2 } { x } \right) \Gamma _ { 2 } ( \nu ) \right] } } \end{array}
$$

Both the series for small $x$ , and CF2 and the normalization relation (6.6.28) require $| \nu | \leq 1 / 2$ . In both cases, therefore, we recurse $I _ { \nu }$ down to a value $\nu = \mu$ in this interval, find $K _ { \mu }$ there, and recurse $K _ { \nu }$ back up to the original value of $\nu$ .

The routine assumes $\nu \geq 0$ . For negative $\nu$ use the reflection formulas

$$
\begin{array} { l } { { I _ { - \nu } = I _ { \nu } + \displaystyle \frac { 2 } { \pi } \sin ( \nu \pi ) K _ { \nu } } } \\ { { K _ { - \nu } = K _ { \nu } } } \end{array}
$$

Note that for large $x$ , $I _ { \nu } \sim e ^ { x }$ and $K _ { \nu } \sim e ^ { - x }$ , and so these functions will overflow or underflow. It is often desirable to be able to compute the scaled quantities $e ^ { - x } I _ { \nu }$ and $e ^ { x } K _ { \nu }$ . Simply omitting the factor $e ^ { - x }$ in equation (6.6.23) will ensure that all four quantities will have the appropriate scaling. If you also want to scale the four quantities for small $x$ when the series in equation (6.6.37) are used, you must multiply each series by $e ^ { x }$ .

As with besseljy, you can either call the void function besselik, and then retrieve the function and/or derivative values from the object, or else just call inu or knu.

The code listing for Bessel::besselik is in a Webnote [4].

# 6.6.3 Airy Functions

For positive $x$ , the Airy functions are defined by

$$
\begin{array} { l } { { \displaystyle \mathrm { A i } ( x ) = \frac { 1 } { \pi } \sqrt { \frac { x } { 3 } } K _ { 1 / 3 } ( z ) } } \\ { { \displaystyle \mathrm { B i } ( x ) = \sqrt { \frac { x } { 3 } } [ I _ { 1 / 3 } ( z ) + I _ { - 1 / 3 } ( z ) ] } } \end{array}
$$

where

$$
z = { \frac { 2 } { 3 } } x ^ { 3 / 2 }
$$

By using the reflection formula (6.6.40), we can convert (6.6.42) into the computationally more useful form

$$
\mathrm { B i } ( x ) = \sqrt { x } \left[ \frac { 2 } { \sqrt { 3 } } I _ { 1 / 3 } ( z ) + \frac { 1 } { \pi } K _ { 1 / 3 } ( z ) \right]
$$

so that Ai and Bi can be evaluated with a single call to besselik.

![](images/eafa14a0d115d32a5ac68c8bf59f0d0ba5a88fdf3bec7649b365cf682a976c93.jpg)  
Figure 6.6.1. Airy functions $\operatorname { A i } ( x )$ and $\operatorname { B i } ( x )$ .

The derivatives should not be evaluated by simply differentiating the above expressions because of possible subtraction errors near $x = 0$ . Instead, use the equivalent expressions

$$
\begin{array} { l l l } { { \displaystyle \mathrm { A i } ^ { \prime } ( x ) = - \frac { x } { \pi \sqrt { 3 } } K _ { 2 / 3 } ( z ) } } \\ { { \displaystyle \mathrm { B i } ^ { \prime } ( x ) = x \left[ \frac { 2 } { \sqrt { 3 } } I _ { 2 / 3 } ( z ) + \frac { 1 } { \pi } K _ { 2 / 3 } ( z ) \right] } } \end{array}
$$

The corresponding formulas for negative arguments are

$$
\begin{array} { l l l } { { \mathrm { A i } ( - x ) = } } & { { \displaystyle \frac { \sqrt { x } } { 2 } \left[ { \cal J } _ { 1 / 3 } ( z ) - \displaystyle \frac { 1 } { \sqrt { 3 } } { \cal Y } _ { 1 / 3 } ( z ) \right] } } \\ { { \mathrm { B i } ( - x ) = - \displaystyle \frac { \sqrt { x } } { 2 } \left[ \displaystyle \frac { 1 } { \sqrt { 3 } } { \cal J } _ { 1 / 3 } ( z ) + { \cal Y } _ { 1 / 3 } ( z ) \right] } } \\ { { \mathrm { A i } ^ { \prime } ( - x ) = } } & { { \displaystyle \frac { x } { 2 } \left[ { \cal J } _ { 2 / 3 } ( z ) + \displaystyle \frac { 1 } { \sqrt { 3 } } { \cal Y } _ { 2 / 3 } ( z ) \right] } } \\ { { \mathrm { B i } ^ { \prime } ( - x ) = } } & { { \displaystyle \frac { x } { 2 } \left[ \displaystyle \frac { 1 } { \sqrt { 3 } } { \cal J } _ { 2 / 3 } ( z ) - { \cal Y } _ { 2 / 3 } ( z ) \right] } } \end{array}
$$

# void Bessel::airy(const Doub x) {

Sets aio, bio, aipo, and bipo, respectively, to the Airy functions $\operatorname { A i } ( x )$ , $\operatorname { B i } ( x )$ and their derivatives $\operatorname { A i } ^ { \prime } ( x )$ , $\operatorname { B i } ^ { \prime } ( x )$ .

static const Doub $\mathtt { P I } = 3$ .141592653589793238, ONOVRT $ \scriptstyle = 0$ .577350269189626,THR $\ P = 1$ ./3.,TWOTHR=2.\*THR;   
Doub absx,rootx,z;   
absx $\equiv$ abs(x);   
rootx=sqrt(absx);   
$z { = }$ TWOTHR\*absx\*rootx;

if $( \textbf { x } > \ 0 . 0 )$ { besselik(THR,z); aio $=$ rootx\*ONOVRT\*ko/PI; bio $=$ rootx\*(ko/PI+2. $^ { 0 * }$ ONOVRT\*io); besselik(TWOTHR,z); aipo $=$ -x\*ONOVRT\*ko/PI; bipo $=$ x\*(ko/PI+2.0\*ONOVRT\*io); else if $( \textbf { x } < \ 0 . 0 )$ { besseljy(THR,z); aio $=$ 0.5\*rootx\*(jo-ONOVRT\*yo); bio $=$ -0.5\*rootx\*(yo+ONOVRT\*jo); besseljy(TWOTHR,z); aipo $=$ 0.5\*absx $^ *$ (ONOVRT\*yo+jo); bipo $=$ 0.5\*absx\*(ONOVRT\*jo-yo); } else { Case $x = 0$ . aio ${ = } 0$ .355028053887817; bio $=$ aio/ONOVRT; aipo $=$ -0.258819403792807; bipo $=$ -aipo/ONOVRT; } }

#

Doub Bessel::airy_ai(const Doub x) {   
Simple interface returning $\operatorname { A i } ( x )$ . if $( \textbf { x } : = \textbf { x } 0$ ) airy(x); return aio;   
}   
Doub Bessel::airy_bi(const Doub x) {   
Simple interface returning $\operatorname { B i } ( x )$ . if $( \mathrm {  ~ x ~ \unboldmath ~ } ! = \mathrm {  ~ x 0 ~ \unboldmath } )$ ) airy(x); return bio;   
}

# 6.6.4 Spherical Bessel Functions

For integer $n$ , spherical Bessel functions are defined by

$$
\begin{array} { l } { \displaystyle j _ { n } ( x ) = \sqrt { \frac { \pi } { 2 x } } J _ { n + \frac { 1 } { 2 } } ( x ) } \\ { \displaystyle y _ { n } ( x ) = \sqrt { \frac { \pi } { 2 x } } Y _ { n + \frac { 1 } { 2 } } ( x ) } \end{array}
$$

They can be evaluated by a call to besseljy, and the derivatives can safely be found from the derivatives of equation (6.6.47).

Note that in the continued fraction CF2 in (6.6.3) just the first term survives for $\nu = 1 / 2$ . Thus one can make a very simple algorithm for spherical Bessel functions along the lines of besseljy by always recursing $j _ { n }$ down to $n = 0$ , setting $p$ and $q$ from the first term in CF2, and then recursing $y _ { n }$ up. No special series is required near $x = 0$ . However, besseljy is already so efficient that we have not bothered to provide an independent routine for spherical Bessels.

void Bessel::sphbes(const Int n, const Doub x) Sets sphjo, sphyo, sphjpo, and sphypo, respectively, to the spherical Bessel functions $j _ { n } ( x )$ , $y _ { n } ( x )$ , and their derivatives ${ j _ { n } ^ { \prime } } ( x )$ , $y _ { n } ^ { \prime } ( x )$ for integer $_ n$ (which is saved as sphno).

const Doub RTPIO2 $^ { * 1 }$ .253314137315500251;   
Doub factor,order;   
if $( \ln \mathbf { \chi } < \mathbf { \chi } _ { 0 } | \mathbf { \chi } | \ : \mathrm { ~ x ~ } < = \mathbf { \chi } _ { 0 } . 0 )$ throw("bad arguments in sphbes");   
order $= \mathtt { n } + 0$ .5;   
besseljy(order,x);   
factor=RTPIO2/sqrt(x);   
sphj $\circ =$ factor\*jo;

sphyo=factor\*yo; sphjpo $=$ factor\*jpo-sphjo/(2.\*x); sphypo factor\*ypo-sphyo/(2.\*x); sphno $= \textbf { n }$ ; }

#

Doub Bessel::sphbesj(const Int n, const Doub x) {   
Simple interface returning $j _ { n } ( x )$ . if (n $\downarrow =$ sphno || x != xo) sphbes(n,x); return sphjo;   
}   
Doub Bessel::sphbesy(const Int n, const Doub x) {   
Simple interface returning $y _ { n } ( x )$ . if (n $\downarrow =$ sphno $| \textbf { | } \textbf { x } : = \textbf { x } 0 \ $ ) sphbes(n,x); return sphyo;   
}

# CITED REFERENCES AND FURTHER READING:

Barnett, A.R., Feng, D.H., Steed, J.W., and Goldfarb, L.J.B. 1974, “Coulomb Wave Functions for All Real $\eta$ and $\rho$ ,” Computer Physics Communications, vol. 8, pp. 377–395.[1]   
Temme, N.M. 1976, “On the Numerical Evaluation of the Ordinary Bessel Function of the Second Kind,” Journal of Computational Physics, vol. 21, pp. 343–350[2]; 1975, op. cit., vol. 19, pp. 324–337.[3]   
Numerical Recipes Software 2007, “Bessel Function Implementations,” Numerical Recipes Webnote No.8,at http://www.nr.com/webnotes?8 [4]   
Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapter 10.[5]   
Thompson, I.J., and Barnett, A.R. 1987, “Modified Bessel Functions $I _ { \nu } ( z )$ and $K _ { \nu } ( z )$ of Real Order and Complex Argument, to Selected Accuracy,” Computer Physics Communications, vol. 47, pp. 245–257.[6]   
Barnett, A.R. 1981, “An Algorithm for Regular and Irregular Coulomb and Bessel functions of Real Order to Machine Accuracy,” Computer Physics Communications, vol. 21, pp. 297– 314.   
Thompson, I.J., and Barnett, A.R. 1986, “Coulomb and Bessel Functions of Complex Arguments and Order,” Journal of Computational Physics, vol. 64, pp. 490–509.

# 6.7 Spherical Harmonics

Spherical harmonics occur in a large variety of physical problems, for example, whenever a wave equation, or Laplace’s equation, is solved by separation of variables in spherical coordinates. The spherical harmonic $Y _ { l m } ( \theta , \phi ) , - l \le m \le l$ ; is a function of the two coordinates $\theta , \phi$ on the surface of a sphere.

The spherical harmonics are orthogonal for different $l$ and $m$ , and they are normalized so that their integrated square over the sphere is unity:

$$
\int _ { 0 } ^ { 2 \pi } d \phi \int _ { - 1 } ^ { 1 } d ( \cos \theta ) { \cal Y } _ { l ^ { \prime } m ^ { \prime } } ^ { \ast } ( \theta , \phi ) { \cal Y } _ { l m } ( \theta , \phi ) = \delta _ { l ^ { \prime } l } \delta _ { m ^ { \prime } m }
$$

Here the asterisk denotes complex conjugation.

Mathematically, the spherical harmonics are related to associated Legendre polynomials by the equation

$$
Y _ { l m } ( \theta , \phi ) = \sqrt { \frac { 2 l + 1 } { 4 \pi } \frac { ( l - m ) ! } { ( l + m ) ! } } P _ { l } ^ { m } ( \cos \theta ) e ^ { i m \phi }
$$

By using the relation

$$
Y _ { l , - m } ( \theta , \phi ) = ( - 1 ) ^ { m } Y _ { l m } ^ { \ast } ( \theta , \phi )
$$

we can always relate a spherical harmonic to an associated Legendre polynomial with $m \geq 0$ . With $x \equiv \cos \theta$ , these are defined in terms of the ordinary Legendre polynomials (cf. $\ S 4 . 6$ and $\ S 5 . 4 )$ b y

$$
P _ { l } ^ { m } ( x ) = ( - 1 ) ^ { m } ( 1 - x ^ { 2 } ) ^ { m / 2 } \frac { d ^ { m } } { d x ^ { m } } P _ { l } ( x )
$$

Be careful: There are alternative normalizations for the associated Legendre polynomials and alternative sign conventions.

The first few associated Legendre polynomials, and their corresponding normalized spherical harmonics, are

$$
\begin{array} { r l r l } & { \frac { P _ { 0 } ^ { 0 } ( x ) } { P _ { 0 } ^ { 1 } ( x ) } = } & { 1 } & { Y _ { 0 0 } = } & { \sqrt { \frac { 1 } { 4 \pi } } } \\ & { \frac { P _ { 1 } ^ { 1 } ( x ) } { P _ { 1 } ^ { 1 } ( x ) } = } & { - ( 1 - x ^ { 2 } ) ^ { 1 / 2 } } & { Y _ { 1 1 } = - \sqrt { \frac { 3 } { 8 \pi } } \sin \theta e ^ { i \phi } } \\ & { \frac { P _ { 0 } ^ { 0 } ( x ) } { P _ { 1 } ^ { 2 } ( x ) = } } & { x } & { Y _ { 1 0 } = } & { \sqrt { \frac { 3 } { 4 \pi } } \cos \theta } \\ & { \frac { P _ { 2 } ^ { 2 } ( x ) = } { 3 ( 1 - x ^ { 2 } ) } } & { Y _ { 2 2 } = \frac { 1 } { 4 } \sqrt { \frac { 1 5 } { 2 \pi } } \sin ^ { 2 } \theta e ^ { 2 i \phi } } \\ & { P _ { 2 } ^ { 1 } ( x ) = - 3 ( 1 - x ^ { 2 } ) ^ { 1 / 2 } x } & { Y _ { 2 1 } = - \sqrt { \frac { 1 5 } { 4 \pi } } \sin \theta \cos \theta e ^ { i \phi } } \\ & { P _ { 2 } ^ { 0 } ( x ) = \frac { 1 } { 2 } ( 3 x ^ { 2 } - 1 ) } & { Y _ { 2 0 } = } & { \sqrt { \frac { 5 } { 4 \pi } } ( \frac { 3 } { 2 } \cos ^ { 2 } \theta - \frac { 1 } { 2 } ) } \end{array}
$$

There are many bad ways to evaluate associated Legendre polynomials numerically. For example, there are explicit expressions, such as

$$
\begin{array} { c } { { P _ { l } ^ { m } ( x ) = \displaystyle { \frac { ( - 1 ) ^ { m } ( l + m ) ! } { 2 ^ { m } m ! ( l - m ) ! } } ( 1 - x ^ { 2 } ) ^ { m / 2 } \biggl [ 1 - \displaystyle { \frac { ( l - m ) ( m + l + 1 ) } { 1 ! ( m + 1 ) } } \left( \frac { 1 - x } { 2 } \right) } } \\ { { + \displaystyle { \frac { ( l - m ) ( l - m - 1 ) ( m + l + 1 ) ( m + l + 2 ) } { 2 ! ( m + 1 ) ( m + 2 ) } } \left( \frac { 1 - x } { 2 } \right) ^ { 2 } - \cdots \biggl ] } } \end{array}
$$

where the polynomial continues up through the term in $( 1 - x ) ^ { l - m }$ . (See [1] for this and related formulas.) This is not a satisfactory method because evaluation of the polynomial involves delicate cancellations between successive terms, which alternate in sign. For large $l$ , the individual terms in the polynomial become very much larger than their sum, and all accuracy is lost.

In practice, (6.7.6) can be used only in single precision (32-bit) for $l$ up to 6 or 8, and in double precision (64-bit) for $l$ up to 15 or 18, depending on the precision required for the answer. A more robust computational procedure is therefore desirable, as follows.

The associated Legendre functions satisfy numerous recurrence relations, tabulated in [1,2]. These are recurrences on $l$ alone, on $m$ alone, and on both $l$ and $m$ simultaneously. Most of the recurrences involving $m$ are unstable, and so are dangerous for numerical work. The following recurrence on $l$ is, however, stable (compare 5.4.1):

$$
( l - m ) P _ { l } ^ { m } = x ( 2 l - 1 ) P _ { l - 1 } ^ { m } - ( l + m - 1 ) P _ { l - 2 } ^ { m }
$$

Even this recurrence is useful only for moderate $l$ and $m$ , since the $P _ { l } ^ { m }$ ’s themselves grow rapidly with $l$ and quickly overflow. The spherical harmonics by contrast remain bounded — after all, they are normalized to unity (eq. 6.7.1). It is exactly the square-root factor in equation (6.7.2) that balances the divergence. So the right function to use in the recurrence relation is the renormalized associated Legendre function,

$$
\widetilde { P } _ { l } ^ { m } = \sqrt { \frac { 2 l + 1 } { 4 \pi } \frac { ( l - m ) ! } { ( l + m ) ! } } P _ { l } ^ { m }
$$

Then the recurrence relation (6.7.7) becomes

$$
\widetilde { P } _ { l } ^ { m } = \sqrt { \frac { 4 l ^ { 2 } - 1 } { l ^ { 2 } - m ^ { 2 } } } \left[ x \widetilde { P } _ { l - 1 } ^ { m } - \sqrt { \frac { ( l - 1 ) ^ { 2 } - m ^ { 2 } } { 4 ( l - 1 ) ^ { 2 } - 1 } } \widetilde { P } _ { l - 2 } ^ { m } \right]
$$

We start the recurrence with the closed-form expression for the $l = m$ function,

$$
\widetilde { P } _ { m } ^ { m } = ( - 1 ) ^ { m } \sqrt { \frac { 2 m + 1 } { 4 \pi ( 2 m ) ! } } ( 2 m - 1 ) ! ! ( 1 - x ^ { 2 } ) ^ { m / 2 }
$$

Using (6.7.9) with (The notation $n ! !$ denotes the product of all odd integers less than or equal to $l = m + 1$ , and setting ${ \widetilde { P } } _ { m - 1 } ^ { m } = 0$ , we find $n$ .)

$$
\tilde { P } _ { m + 1 } ^ { m } = x \sqrt { 2 m + 3 } \tilde { P } _ { m } ^ { m }
$$

Equations (6.7.10) and (6.7.11) provide the two starting values required for (6.7.9) for general $l$ .

The function that implements this is

Doub plegendre(const Int l, const Int m, const Doub x) {

Computes the renormalized associated Legendre polynomial $\tilde { P } _ { l } ^ { m } ( x )$ , equation (6.7.8). Here m and $l$ are integers satisfying $0 \leq m \leq l$ , while $x$ lies in the range $- 1 \leq x \leq 1$ .

static const Doub $\mathtt { P I } = 3$ .141592653589793;   
Int i,ll;   
Doub fact,oldfact,pll,pmm,pmmp1,omx2;   
if $( \mathrm { m } ~ < ~ 0 ~ | ~ | ~ \mathrm { ~ m ~ } > ~ 1 $ || abs $\mathrm { ~ ( ~ x ~ ) ~ } > \mathrm { ~ 1 ~ . ~ 0 ~ }$ ) throw("Bad arguments in routine plgndr");   
pmm=1.0; Compute $\widetilde { P } _ { m } ^ { m }$ .   
if $\mathrm { ~ \textit ~ { ~  ~ } ~ } \mathrm { ~ > ~ } \mathrm { ~ 0 ~ }$ ) { $\mathtt { o m x 2 } = ( 1 \mathrm { ~ . ~ } 0 \mathrm { - x } ) * ( 1 \mathrm { ~ . ~ } 0 \mathrm { + x } )$ ; fact $^ { = 1 }$ .0; for $\mathrm { { ( i = 1 ; i < = m ; i + + ) } }$ { pmm $\ast =$ omx2\*fact/(fact+1.0); fact $+ = ~ 2 . 0$ ; }   
}   
pmm=sqrt((2\*m+1)\*pmm/(4.0\*PI));

if (m & 1) pmm=-pmm; if $\mathrm { ~  ~ \Omega ~ } . \mathrm { ~  ~ \Omega ~ } . \mathrm { ~  ~ \Omega ~ } .$ ) return pmm; else { Compute $\tilde { P } _ { m + 1 } ^ { m }$ . pmmp1=x\*sqrt(2.0\*m+3.0)\*pmm; if $\scriptstyle { \mathrm { ~ ( ~ 1 ~ } = = \mathrm { ~ ( m + 1 ) ~ } }$ ) return pmmp1; else { Compute $\widetilde { P } _ { l } ^ { m }$ , $l > m + 1$ . oldfact=sqrt(2.0\*m+3.0); for (ll=m+2;ll<=l;ll++) { fact=sqrt((4.0\*ll\*ll-1.0)/(ll\*ll-m\*m)); pll=(x\*pmmp1-pmm/oldfact)\*fact; oldfact=fact; pmm=pmmp1; pmmp1=pll; } return pll; } } }

Sometimes it is convenient to have the functions with the standard normalization, as defined by equation (6.7.4). Here is a routine that does this. Note that it will overflow for $m \gtrsim 8 0$ , or even sooner if $l \gg m$ .

Doub plgndr(const Int l, const Int m, const Doub x)   
Computes the associated Legendre polynomial $P _ { l } ^ { m } ( x )$ , equation (6.7.4). Here $m$ and $l$ are integers satisfying $0 \leq m \leq l$ , while $x$ lies in the range $- 1 \leq x \leq 1$ . These functions will overflow for $m \gtrsim 8 0$ .   
const Doub $\mathtt { P I } = 3$ .141592653589793238;   
if $\mathrm { ~ ( ~ m ~ < ~ 0 ~ ~ | ~ | ~ ~ m ~ > ~ 1 ~ }$ || abs(x) > 1.0) throw("Bad arguments in routine plgndr");   
Doub prod=1.0;   
for (Int $\scriptstyle \mathbf { j } = 1 - \mathbf { m } + 1 ; \mathbf { j } < = 1 + \mathbf { m } ; \mathbf { j } + + )$ prod $\ast = \mathrm { ~ j ~ }$ ;   
return sqrt(4.0\*PI\*prod/( $^ { 2 * 1 + 1 }$ ))\*plegendre(l,m,x);

# 6.7.1 Fast Spherical Harmonic Transforms

Any smooth function on the surface of a sphere can be written as an expansion in spherical harmonics. Suppose the function can be well-approximated by truncating the expansion at $l = { l _ { \mathrm { { m a x } } } }$ :

$$
\begin{array} { c } { { f ( \theta _ { i } , \phi _ { j } ) = \displaystyle \sum _ { l = 0 } ^ { l _ { \mathrm { m a x } } } \sum _ { m = - l } ^ { m = l } a _ { l m } Y _ { l m } ( \theta _ { i } , \phi _ { j } ) } } \\ { { = \displaystyle \sum _ { l = 0 } ^ { l _ { \mathrm { m a x } } } \sum _ { m = - l } ^ { m = l } a _ { l m } \widetilde { P } _ { l } ^ { m } ( \cos \theta _ { i } ) e ^ { i m \phi _ { j } } } } \end{array}
$$

Here we have written the function evaluated at one of $N _ { \theta }$ sample points $\theta _ { i }$ and one of $N _ { \phi }$ sample points $\phi _ { j }$ . The total number of sample points is $N = N _ { \theta } N _ { \phi }$ . In applications, typically $N _ { \theta } \sim N _ { \phi } \sim \sqrt { N }$ . Since the total number of spherical harmonics in the sum (6.7.12) is $l _ { \mathrm { m a x } } ^ { 2 }$ , we also have $l _ { \mathrm { m a x } } \sim \sqrt { N }$ .

How many operations does it take to evaluate the sum (6.7.12)? Direct evaluation of $l _ { \mathrm { m a x } } ^ { 2 }$ terms at $N$ sample points is an $O ( N ^ { 2 } )$ process. You might try to speed this up by choosing the sample points $\phi _ { j }$ to be equally spaced in angle and doing the sum over $m$ by an FFT. Each FFT is $O ( N _ { \phi } \ln { N _ { \phi } } )$ , and you have to do $O ( N _ { \theta } l _ { \mathrm { m a x } } )$ of them, for a total of $O ( N ^ { 3 / 2 } \ln N )$ operations, which is some improvement. A simple rearrangement [3-5] gives an even better way: Interchange the order of summation

$$
\sum _ { l = 0 } ^ { l _ { \mathrm { m a x } } } \sum _ { m = - l } ^ { l } \longleftrightarrow \sum _ { m = - l _ { \mathrm { m a x } } } ^ { l _ { \mathrm { m a x } } } \sum _ { l = | m | } ^ { l _ { \mathrm { m a x } } }
$$

so that

$$
f ( \theta _ { i } , \phi _ { j } ) = \sum _ { m = - l _ { \mathrm { m a x } } } ^ { l _ { \mathrm { m a x } } } q _ { m } ( \theta _ { i } ) e ^ { i m \phi _ { j } }
$$

where

$$
q _ { m } ( \theta _ { i } ) = \sum _ { l = | m | } ^ { l _ { \mathrm { m a x } } } a _ { l m } \widetilde { P } _ { l } ^ { m } ( \cos \theta _ { i } )
$$

Evaluating the sum in (6.7.15) is $O ( l _ { \mathrm { m a x } } )$ , and one must do this for $O ( l _ { \operatorname* { m a x } } N _ { \theta } ) q _ { m }$ ’s, so the total work is ${ \cal O } ( N ^ { 3 / 2 } )$ . To evaluate equation (6.7.14) by an FFT at fixed $\theta _ { i }$ is $O ( N _ { \phi } \ln { N _ { \phi } } )$ . There are $N _ { \theta }$ FFTs to be done, for a total operations count of $O ( N \ln N )$ , which is negligible in comparison. So the total algorithm is $O ( N ^ { 3 / 2 } )$ . Note that you can evaluate equation (6.7.14) either by precomputing and storing the $\widetilde { P } _ { l } ^ { m }$ ’s using the recurrence relation (6.7.9), or by Clenshaw’s method (-5.4).

What about inverting the transform (6.7.12)? The formal inverse for the expansion of a continuous function $f ( \theta , \phi )$ follows from the orthonormality of the $Y _ { l m }$ ’s, equation (6.7.1),

$$
a _ { l m } = \int \sin \theta d \theta d \phi f ( \theta , \phi ) e ^ { - i m \phi } \widetilde { P } _ { l } ^ { m } ( \cos \theta )
$$

For the discrete case, where we have a sampled function, the integral becomes a quadrature:

$$
a _ { l m } = \sum _ { i , j } w ( \theta _ { i } ) f ( \theta _ { i } , \phi _ { j } ) e ^ { - i m \phi _ { j } } \widetilde { P } _ { l } ^ { m } ( \cos \theta _ { i } )
$$

Here $w ( \theta _ { i } )$ are the quadrature weights. In principle we could consider weights that depend on $\phi _ { j }$ as well, but in practice we do the $\phi$ quadrature by an FFT, so the weights are unity. A good choice for the weights for an equi-angular grid in $\theta$ is given in Ref. [3], Theorem 3. Another possibility is to use Gaussian quadrature for the $\theta$ integral. In this case, you choose the sample points so that the cos $\theta _ { i }$ ’s are the abscissas returned by gauleg and the $w ( \theta _ { i } )$ ’s are the corresponding weights. The best way to organize the calculation is to first do the FFTs, computing

$$
g _ { m } ( \theta _ { i } ) = \sum _ { j } f ( \theta _ { i } , \phi _ { j } ) e ^ { - i m \phi _ { j } }
$$

Then

$$
a _ { l m } = \sum _ { i } w ( \theta _ { i } ) g _ { m } ( \theta _ { i } ) \widetilde { P } _ { l } ^ { m } ( \cos \theta _ { i } )
$$

You can verify that the operations count is dominated by equation (6.7.19) and scales as $O ( N ^ { 3 / 2 } )$ once again. In a real calculation, you should exploit all the symmetries that let you reduce the workload, such as $g _ { - m } = g _ { m } ^ { \ast }$ and $\tilde { P } _ { l } ^ { m } [ \cos ( \pi - \theta ) ] =$ $( - 1 ) ^ { l + m } \tilde { P } _ { l } ^ { m } ( \cos \theta )$ .

Very recently, algorithms for fast Legendre transforms have been developed, similar in spirit to the FFT [3,6,7]. Theoretically, they reduce the forward and inverse spherical harmonic transforms to $O ( N \log ^ { 2 } N )$ problems. However, current implementations [8] are not much faster than the $O ( N ^ { 3 / 2 } )$ methods above for $N \sim$ 500, and there are stability and accuracy problems that require careful attention [9]. Stay tuned!

# CITED REFERENCES AND FURTHER READING:

Magnus, W., and Oberhettinger, F. 1949, Formulas and Theorems for the Functions of Mathematical Physics (New York: Chelsea), pp. 54ff.[1]   
Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapter 8.[2]   
Driscoll, J.R., and Healy, D.M. 1994, “Computing Fourier Transforms and Convolutions on the 2–sphere,” Advances in Applied Mathematics, vol. 15, pp. 202–250.[3]   
Muciaccia, P.F., Natoli, P., and Vittorio, N. 1997, “Fast Spherical Harmonic Analysis: A Quick Algorithm for Generating and/or Inverting Full-Sky, High-Resolution Cosmic Microwave Background Anisotropy Maps,” Astrophysical Journal, vol. 488, pp. L63–66.[4]   
Oh, S.P., Spergel, D.N., and Hinshaw, G. 1999, “An Efficient Technique to Determine the Power Spectrum from Cosmic Microwave Background Sky Maps,” Astrophysical Journal, vol. 510, pp. 551–563, Appendix A.[5]   
Healy, D.M., Rockmore, D., Kostelec, P.J., and Moore, S. 2003, “FFTs for the 2-Sphere: Improvements and Variations,” Journal of Fourier Analysis and Applications, vol. 9, pp. 341–385.[6]   
Potts, D., Steidl, G., and Tasche, M. 1998, “ Fast and Stable Algorithms for Discrete Spherical Fourier Transforms,” Linear Algebra and Its Applications, vol. 275-276, pp. 433–450.[7]   
Moore, S., Healy, D.M., Rockmore, D., and Kostelec, P.J. $^ { 2 0 0 7 + }$ , SpharmonicKit. Software at http://www.cs.dartmouth.edu/\~geelong/sphere.[8]   
Healy, D.M., Kostelec, P.J., and Rockmore, D. 2004, “Towards Safe and Effective High-Order Legendre Transforms with Applications to FFTs for the 2-Sphere,” Advances in Computational Mathematics,vol.21,pp.59-105.[9]

# 6.8 Fresnel Integrals, Cosine and Sine Integrals

# 6.8.1 Fresnel Integrals

The two Fresnel integrals are defined by

$$
C ( x ) = \int _ { 0 } ^ { x } \cos \left( { \frac { \pi } { 2 } } t ^ { 2 } \right) d t , \qquad S ( x ) = \int _ { 0 } ^ { x } \sin \left( { \frac { \pi } { 2 } } t ^ { 2 } \right) d t
$$

and are plotted in Figure 6.8.1.

![](images/61816714351e29f7ffbb7d3293bb66017c95a8bc0d49bdf4094c199e08bd454d.jpg)  
Figure 6.8.1. Fresnel integrals $C ( x )$ and $S ( x )$ $( \ S 6 . 8 )$ , and Dawson’s integral $F ( x )$ (-6.9).

The most convenient way of evaluating these functions to arbitrary precision is to use power series for small $x$ and a continued fraction for large $x$ . The series are

$$
\begin{array} { l } { { C ( x ) = x - \left( \displaystyle \frac { \pi } { 2 } \right) ^ { 2 } \displaystyle \frac { x ^ { 5 } } { 5 \cdot 2 ! } + \left( \displaystyle \frac { \pi } { 2 } \right) ^ { 4 } \displaystyle \frac { x ^ { 9 } } { 9 \cdot 4 ! } - \cdots } } \\ { { S ( x ) = \left( \displaystyle \frac { \pi } { 2 } \right) \displaystyle \frac { x ^ { 3 } } { 3 \cdot 1 ! } - \left( \displaystyle \frac { \pi } { 2 } \right) ^ { 3 } \displaystyle \frac { x ^ { 7 } } { 7 \cdot 3 ! } + \left( \displaystyle \frac { \pi } { 2 } \right) ^ { 5 } \displaystyle \frac { x ^ { 1 1 } } { 1 1 \cdot 5 ! } - \cdots } } \end{array}
$$

There is a complex continued fraction that yields both $S ( x )$ and $C ( x )$ simultaneously:

$$
C ( x ) + i S ( x ) = \frac { 1 + i } { 2 } \mathrm { e r f } z , \qquad z = \frac { \sqrt { \pi } } { 2 } ( 1 - i ) x
$$

where

$$
{ \begin{array} { r l } & { e ^ { z ^ { 2 } } \operatorname { e r f c } z = { \cfrac { 1 } { \sqrt { \pi } } } \left( { \cfrac { 1 } { z + } } { \cfrac { 1 / 2 } { z + } } { \cfrac { 1 } { z + } } { \cfrac { 3 / 2 } { z + } } { \cfrac { 2 } { z + } } \cdots \right) } \\ & { \qquad = { \cfrac { 2 z } { \sqrt { \pi } } } \left( { \cfrac { 1 } { 2 z ^ { 2 } + 1 - } } { \cfrac { 1 \cdot 2 } { 2 z ^ { 2 } + 5 - } } { \cfrac { 3 \cdot 4 } { 2 z ^ { 2 } + 9 - } } \cdots \right) } \end{array} }
$$

In the last line we have converted the “standard” form of the continued fraction to its “even” form (see $\ S 5 . 2 )$ , which converges twice as fast. We must be careful not to evaluate the alternating series (6.8.2) at too large a value of $x$ ; inspection of the terms shows that $x = 1 . 5$ is a good point to switch over to the continued fraction.

Note that for large $x$

$$
C ( x ) \sim \frac { 1 } { 2 } + \frac { 1 } { \pi x } \sin \left( \frac { \pi } { 2 } x ^ { 2 } \right) , \qquad S ( x ) \sim \frac { 1 } { 2 } - \frac { 1 } { \pi x } \cos \left( \frac { \pi } { 2 } x ^ { 2 } \right)
$$

Thus the precision of the routine frenel may be limited by the precision of the library routines for sine and cosine for large $x$ .

Complex frenel(const Doub x) $\begin{array} { r } { \mathopen { } \mathclose \bgroup \left\{ \begin{array} { r l r l } \end{array} \aftergroup \egroup \right. } \end{array}$   
Computes the Fresnel integrals $S ( x )$ and $C ( x )$ for all real $x$ . $C ( x )$ is returned as the real part   
of cs and $S ( x )$ as the imaginary part. static const Int MAXIT $\scriptstyle \mathtt { \Gamma = 1 0 0 }$ ; static const Doub $\mathtt { P I } = 3$ .141592653589793238, PIBY2 $\Bumpeq$ (PI/2.0), XMIN=1.5, EPS=numeric_limits<Doub>::epsilon(), FPMIN=numeric_limits<Doub>::min(), BIG=numeric_limits<Doub>::max()\*EPS; Here MAXIT is the maximum number of iterations allowed; EPS is the relative error; FPMIN is a number near the smallest representable floating-point number; BIG is a number near the machine overflow limit; and XMIN is the dividing line between using the series and continued fraction. Bool odd; Int k,n; Doub a,ax,fact,pix2,sign,sum,sumc,sums,term,test; Complex b,cc,d,h,del,cs; if ((ax abs(x)) $<$ sqrt(FPMIN)) { Special case: Avoid failure of convergence cs=ax; test because of underflow. } else if (ax $< =$ XMIN) { Evaluate both series simultaneously. sum=sums=0.0; sumc $=$ ax; sign $= 1$ .0; fact=PIBY2\*ax\*ax; odd=true; term=ax; $\mathtt { n } = 3$ ; for $\mathrm { k } = 1$ ;k $< =$ MAXIT;k++) { term $\ast =$ fact/k; sum $+ =$ sign\*term/n; test ${ } = { }$ abs(sum)\*EPS; if (odd) { sign $=$ -sign; sums $=$ sum; sum=sumc; } else { sumc $=$ sum; sum=sums; if (term $<$ test) break; odd $= !$ odd; $\mathrm { ~ n ~ } + = \mathrm { ~ 2 ~ }$ ; } if (k $>$ MAXIT) throw("series failed in frenel"); cs=Complex(sumc,sums); } else { Evaluate continued fraction by modified pix2 $=$ PI\*ax\*ax; Lentz’s method (-5.2). b=Complex(1.0,-pix2); cc=BIG; $d = \mathrm { h } = 1$ .0/b; $\texttt { n } = \ - 1$ ; for (k=2;k $< =$ MAXIT;k++) { $\texttt { n } + = \ 2 ;$ ; $\mathrm { \ a \ = \ - n * ( n { + } 1 ) \ ; }$ ; b $\scriptstyle + = \ 4 , 0$ ; d=1.0/(a\*d+b); Denominators cannot be zero. cc=b+a/cc; del=cc\*d; h $\ast =$ del; if (abs(real(del)-1.0)+abs(imag(del)) $< =$ EPS) break; }

![](images/dc8f87c1ac8922226c8a9a8ecba7eaa3cd8c3638b2bc893bb9054a66abdf7530.jpg)  
Figure 6.8.2. Sine and cosine integrals $\mathrm { S i } ( x )$ and $\operatorname { C i } ( x )$ .

if (k > MAXIT) throw("cf failed in frenel"); h $\ast =$ Complex(ax,-ax); cs=Complex(0.5,0.5) \*(1.0-Complex(cos(0.5\*pix2),sin(0.5\*pix2))\*h); } if $\mathit { \Pi } _ { \mathrm { ~ x ~ } } < \mathit { \Pi } 0 . 0 \mathit { \Pi } _ { \mathrm { ~ \tiny ~  ~ } }$ ) cs = -cs; Use antisymmetry. return cs;

# 6.8.2 Cosine and Sine Integrals

The cosine and sine integrals are defined by

$$
\begin{array} { l } { \displaystyle \mathrm { C i } ( \boldsymbol { x } ) = \gamma + \ln \boldsymbol { x } + \int _ { 0 } ^ { \boldsymbol { x } } \frac { \cos t - 1 } { t } d t } \\ { \displaystyle \mathrm { S i } ( \boldsymbol { x } ) = \int _ { 0 } ^ { \boldsymbol { x } } \frac { \sin t } { t } d t } \end{array}
$$

and are plotted in Figure 6.8.2. Here $\gamma \approx 0 . 5 7 7 2 . . .$ is Euler’s constant. We only need a way to calculate the functions for $x > 0$ , because

$$
\mathrm { S i } ( - x ) = - \mathrm { S i } ( x ) , \qquad \mathrm { C i } ( - x ) = \mathrm { C i } ( x ) - i \pi
$$

Once again we can evaluate these functions by a judicious combination of power

series and complex continued fraction. The series are

$$
\begin{array} { l } { \displaystyle \mathrm { S i } ( x ) = x - \frac { x ^ { 3 } } { 3 \cdot 3 ! } + \frac { x ^ { 5 } } { 5 \cdot 5 ! } - \cdots } \\ { \displaystyle \mathrm { C i } ( x ) = \gamma + \ln x + \left( - \frac { x ^ { 2 } } { 2 \cdot 2 ! } + \frac { x ^ { 4 } } { 4 \cdot 4 ! } - \cdots \right) } \end{array}
$$

The continued fraction for the exponential integral $E _ { 1 } ( i x )$ is

$$
\begin{array} { l } { { \displaystyle E _ { 1 } ( i x ) = - \mathrm { C i } ( x ) + i [ \mathrm { S i } ( x ) - \pi / 2 ] } } \\ { ~ = e ^ { - i x } \left( \frac 1 { i x + } \frac 1 { 1 + } \frac 1 { i x + } \frac 2 { 1 + } \frac 2 { i x + } \dots \right) }  \\ { { \displaystyle ~ = e ^ { - i x } \left( \frac 1 { 1 + i x - } \frac 1 { 3 + i x - } \frac 2 { 5 + i x - } \dots \right) } } \end{array}
$$

The “even” form of the continued fraction is given in the last line and converges twice as fast for about the same amount of computation. A good crossover point from the alternating series to the continued fraction is $x = 2$ in this case. As for the Fresnel integrals, for large $x$ the precision may be limited by the precision of the sine and cosine routines.

# Complex cisi(const Doub x) {

Computes the cosine and sine integrals $\operatorname { C i } ( x )$ and $\mathrm { S i } ( x )$ . The function $\operatorname { C i } ( x )$ is returned as the real part of cs, and $\mathrm { S i } ( x )$ as the imaginary part. $\mathrm { C i } ( 0 )$ is returned as a large negative number and no error message is generated. For $x < 0$ the routine returns $\operatorname { C i } ( - x )$ and you must supply the $- i \pi$ yourself.

static const Int MAXIT $\mathtt { \Pi } = 1 0 0$ ; Maximum number of iterations allowed.   
static const Doub EULER ${ } = 0$ .577215664901533, PIBY2=1.570796326794897, TMIN $^ { = 2 }$ .0, EPS $=$ numeric_limits<Doub>::epsilon(), FPMIN=numeric_limits<Doub>::min() $^ { * 4 }$ .0, BIG $\scriptstyle  =$ numeric_limits<Doub>::max()\*EPS; Here EULER is Euler’s constant $\gamma$ ; PIBY2 is $\pi / 2$ ; TMIN is the dividing line between using the series and continued fraction; EPS is the relative error, or absolute error near a zero of $\operatorname { C i } ( x )$ ; FPMIN is a number close to the smallest representable floating-point number; and BIG is a number near the machine overflow limit.   
Int i,k;   
Bool odd;   
Doub a,err,fact,sign,sum,sumc,sums,t,term;   
Complex h,b,c,d,del,cs;   
if $: ( \mathrm { t } { = } { \bf a b s } \left( \mathrm { \bf x } \right) ) = = 0 . 0 \mathrm { \Omega }$ ) return -BIG; Special case.   
if ( $t >$ TMIN) { Evaluate continued fraction by modified b $\mid =$ Complex(1.0,t); Lentz’s method (-5.2). $z =$ Complex(BIG,0.0); $\mathrm { \ d } { = } \mathrm { h } { = } 1$ .0/b; for ( $\dot { \bf 1 } = 1$ ;i<MAXIT;i++) { a= -i\*i; b $+ = ~ 2 , 0$ ; d=1.0/(a\*d+b); Denominators cannot be zero. c=b+a/c; del=c\*d; h $\ast =$ del; if (abs(real(del)-1.0)+abs(imag(del)) $< =$ EPS) break; if (i $> =$ MAXIT) throw("cf failed in cisi"); $\mathrm { h } =$ Complex(cos(t),-sin(t))\*h; cs $=$ -conj(h)+Complex(0.0,PIBY2);   
} else { Evaluate both series simultaneously.

Special case: Avoid failure of convergence test because of underflow.

if (t < sqrt(FPMIN)) { sumc=0.0; sums=t; } else { sum=sums ${ } _ { , } = { }$ sumc ${ = } 0$ .0; sign=fact $= 1$ .0; odd=true; for $\mathrm { k } = 1$ ;k $< =$ MAXIT;k++) { fact $* = \mathrm { ~ t ~ } / \mathrm { k }$ ; term=fact/k; sum $+ =$ sign\*term; err=term/abs(sum); if (odd) { sign $=$ -sign; sums $=$ sum; sum=sumc; } else { sumc=sum; sum=sums; if (err $<$ EPS) break; odd=!odd; } if (k $>$ MAXIT) throw("maxits exceeded in cisi"); } cs=Complex(sumc+log(t)+EULER,sums); } if $\left( \mathbf { x } ~ < ~ 0 . 0 \right)$ cs $=$ conj(cs); return cs;

# CITED REFERENCES AND FURTHER READING:

Stegun, I.A., and Zucker, R. 1976, “Automatic Computing Methods for Special Functions. III. The Sine, Cosine, Exponential integrals, and Related Functions,” Journal of Research of the National Bureau of Standards,vol. 80B,pp.291-311； 1981,“Automatic Computing Methods for Special Functions. IV. Complex Error Function, Fresnel Integrals, and Other Related Functions,” op. cit., vol. 86, pp. 661–686.   
Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapters 5 and 7.

# 6.9 Dawson's Integral

Dawson’s Integral $F ( x )$ is defined by

$$
F ( x ) = e ^ { - x ^ { 2 } } \int _ { 0 } ^ { x } e ^ { t ^ { 2 } } d t
$$

See Figure 6.8.1 for a graph of the function. The function can also be related to the complex error function by

$$
F ( z ) = \frac { i \sqrt { \pi } } { 2 } e ^ { - z ^ { 2 } } \left[ 1 - \mathrm { e r f c } ( - i z ) \right] .
$$

A remarkable approximation for $F ( z )$ , due to Rybicki [1], is

$$
F ( z ) = \operatorname* { l i m } _ { h \to 0 } { \frac { 1 } { \sqrt { \pi } } } \sum _ { n { \mathrm { ~ o d d } } } { \frac { e ^ { - ( z - n h ) ^ { 2 } } } { n } }
$$

What makes equation (6.9.3) unusual is that its accuracy increases exponentially as $h$ gets small, so that quite moderate values of $h$ (and correspondingly quite rapid convergence of the series) give very accurate approximations.

We will discuss the theory that leads to equation (6.9.3) later, in $\ S 1 3 . 1 1$ , as an interesting application of Fourier methods. Here we simply implement a routine for real values of $x$ based on the formula.

It is first convenient to shift the summation index to center it approximately on the maximum of the exponential term. Define $n _ { 0 }$ to be the even integer nearest to $x / h$ , and $x _ { 0 } \equiv n _ { 0 } h$ , $x ^ { \prime } \equiv x - x _ { 0 }$ , and $n ^ { \prime } \equiv n - n _ { 0 }$ , so that

$$
F ( x ) \approx { \frac { 1 } { \sqrt { \pi } } } \sum _ { n ^ { \prime } = - N _ { \ \prime } ^ { n } \ \mathrm { o d d } } ^ { N } { \frac { e ^ { - ( x ^ { \prime } - n ^ { \prime } h ) ^ { 2 } } } { n ^ { \prime } + n _ { 0 } } }
$$

where the approximate equality is accurate when $h$ is sufficiently small and $N$ is sufficiently large. The computation of this formula can be greatly speeded up if we note that

$$
e ^ { - ( x ^ { \prime } - n ^ { \prime } h ) ^ { 2 } } = e ^ { - { x ^ { \prime } } ^ { 2 } } e ^ { - ( n ^ { \prime } h ) ^ { 2 } } \left( e ^ { 2 x ^ { \prime } h } \right) ^ { n ^ { \prime } }
$$

The first factor is computed once, the second is an array of constants to be stored, and the third can be computed recursively, so that only two exponentials need be evaluated. Advantage is also taken of the symmetry of the coefficients $e ^ { - ( n ^ { \prime } h ) ^ { 2 } }$ by breaking up the summation into positive and negative values of $n ^ { \prime }$ separately.

In the following routine, the choices $h = 0 . 4$ and $N = 1 1$ are made. Because of the symmetry of the summations and the restriction to odd values of $n$ , the limits on the for loops are 0 to 5. The accuracy of the result in this version is about $2 \times 1 0 ^ { - 7 }$ . In order to maintain relative accuracy near $x = 0$ , where $F ( x )$ vanishes, the program branches to the evaluation of the power series [2] for $F ( x )$ , for $| x | < 0 . 2$ .

Returns Dawson’s integral Doub dawson(const Doub $\begin{array} { c } { { \mathrm { \ x { x } } ) \mathrm { ~ \ x { ~ } } \mathrm { ~ \ x { ~ } } } } \\ { { F ( x ) = \exp ( - x ^ { 2 } ) \int _ { 0 } ^ { x } \exp ( t ^ { 2 } ) d t } } \end{array}$ for any real $x$ .

# dawson.h

static const Int NMAX $_ { = 6 }$ ;   
static VecDoub c(NMAX);   
static Bool init $=$ true;   
static const Doub $\mathtt { H } = 0 \mathtt { \Omega } . 4$ , ${ \tt A 1 } = 2$ .0/3.0, $\mathtt { A 2 = 0 }$ .4, $_ { \textrm { A 3 = 2 } }$ .0/7.0;   
Int i,n0; Flag is true if we need to initialize, else false.   
Doub d1,d2,e1,e2,sum,x2,xp,xx,ans;   
if (init) { init=false; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<NMAX;i++) c[i] $=$ exp(-SQR((2.0\*i+1.0)\*H));   
}   
if (abs(x) < 0.2) { Use series expansion. ${ \bf x } 2 \mathrm { = x * } { \bf x }$ ; ans=x\*(1.0-A1\*x2\*(1.0-A2\*x2\*(1.0-A3\*x2)));   
} else { Use sampling theorem representation. xx=abs(x); ${ \tt n } 0 = 2 *$ Int(0.5\*xx/H+0.5); xp=xx-n0\*H; e1=exp(2.0\*xp\*H);

e2=e1\*e1; d1=n0+1; d2=d1-2.0; sum=0.0; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<NMAX; $\dot { \bf 1 } + +$ ,d1 $+ { = } 2$ .0,d2- $- = 2$ .0,e1 $\mathtt { * } \mathtt { e } 2$ ) sum $+ =$ c[i]\*(e1/d1+1.0/(d2\*e1)); ans ${ = } 0$ .5641895835\*SIGN(exp(-xp\*xp),x)\*sum; Constant is $1 / { \sqrt { \pi } }$ return ans;

Other methods for computing Dawson’s integral are also known [2,3].

# CITED REFERENCES AND FURTHER READING:

Rybicki, G.B. 1989, “Dawson’s Integral and The Sampling Theorem,” Computers in Physics, vol. 3, no. 2, pp. 85–87.[1]   
Cody, W.J., Pociorek, K.A., and Thatcher, H.C. 1970, “Chebyshev Approximations for Dawson’s Integral,” Mathematics of Computation, vol. 24, pp. 171–178.[2]   
McCabe, J.H. 1974, “A Continued Fraction Expansion, with a Truncation Error Estimate, for Dawson’s Integral,” Mathematics of Computation, vol. 28, pp. 811–816.[3]

# 6.10 Generalized Fermi-Dirac Integrals

The generalized Fermi-Dirac integral is defined as

$$
F _ { k } ( \eta , \theta ) = \int _ { 0 } ^ { \infty } { \frac { x ^ { k } ( 1 + { \frac { 1 } { 2 } } \theta x ) ^ { 1 / 2 } } { e ^ { x - \eta } + 1 } } d x
$$

It occurs, for example, in astrophysical applications with $\theta$ nonnegative and arbitrary $\eta$ . In condensed matter physics one usually has the simpler case of $\theta = 0$ and omits the “generalized” from the name of the function. The important values of $k$ are $- 1 / 2 , 1 / 2 , 3 / 2$ , and $5 / 2$ , but we’ll consider arbitrary values greater than $^ { - 1 }$ . Watch out for an alternative definition that multiplies the integral by $1 / \Gamma ( k + 1 )$ .

For $\eta \ll - 1$ and $\eta \gg 1$ there are useful series expansions for these functions (see, e.g., [1]). These give, for example,

$$
\begin{array} { l } { { F _ { 1 / 2 } ( \eta , \theta ) \to \displaystyle \frac { 1 } { \sqrt { 2 \theta } } e ^ { \eta } e ^ { 1 / \theta } K _ { 1 } \left( \frac { 1 } { \theta } \right) , \quad \eta \to - \infty } } \\ { { \ } } \\ { { F _ { 1 / 2 } ( \eta , \theta ) \to \displaystyle \frac { 1 } { 2 \sqrt { 2 } } \eta ^ { 3 / 2 } \displaystyle \frac { y \sqrt { 1 + y ^ { 2 } } - \sinh ^ { - 1 } y } { ( \sqrt { 1 + y ^ { 2 } } - 1 ) ^ { 3 / 2 } } , \quad \eta \to \infty } } \end{array}
$$

Here $y$ is defined by

$$
1 + y ^ { 2 } = ( 1 + \eta \theta ) ^ { 2 }
$$

It is the middle range of $\eta$ values that is difficult to handle.

For $\theta = 0$ , Macleod [2] has given Chebyshev expansions accurate to $1 0 ^ { - 1 6 }$ for the four important $k$ values, covering all $\eta$ values. In this case, one need look no further for an algorithm. Goano [3] handles arbitrary $k$ for $\theta = 0$ . For nonzero $\theta$ , it is reasonable to compute the functions by direct integration, using variable transformation to get rapidly converging quadratures [4]. (Of course, this works also for $\theta = 0$ , but is not as efficient.) The usual transformation $x = \exp ( t - e ^ { - t } )$ handles the singularity at $x = 0$ and the exponential fall off at large $x$ (cf. equation 4.5.14). For $\eta \gtrsim 1 5$ , it is better to split the integral into two regions, $[ 0 , \eta ]$ and $[ \eta , \eta + 6 0 ]$ . (The contribution beyond $\eta + 6 0$ is negligible.) Each of these integrals can then be done with the DE rule. Between 60 and 500 function evaluations give full double precision, larger $\eta$ requiring more function evaluations. A more efficient strategy would replace the quadrature by a series expansion for large $\eta$ .

In the implementation below, note how operator() is overloaded to define both a function of one variable (for Trapzd) and a function of two variables (for DErule). Note also the syntax

Trapzd<Fermi> s(\*this,a,b);

for declaring a Trapzd object inside the Fermi object itself.

# struct Fermi {

Doub kk,etaa,thetaa; Doub operator() (const Doub t); Doub operator() (const Doub x, const Doub del); Doub val(const Doub k, const Doub eta, const Doub theta); };

Doub Fermi::operator() (const Doub t) {   
Integrand for trapezoidal quadrature of generalized Fermi-Dirac integral with transformation $x = \mathrm { { e x p } } ( t - e ^ { - t } )$ .   
Doub $_ \textrm { x }$ ;   
$_ { \textrm { x } = }$ exp(t-exp(-t));   
return x\*(1.0+exp(-t))\*pow(x,kk)\*sqrt(1.0+thetaa\*0.5\*x)/ (exp(x-etaa)+1.0);

# }

Doub Fermi::operator() (const Doub x, const Doub del) { Integrand for DE rule quadrature of generalized Fermi-Dirac integral.

if $\mathit { \Psi } _ { \left. \mathbf { X } \right. } ^ { \prime } < \left. \mathbf { 1 } . 0 \right.$ ) return pow(del,kk)\*sqrt(1. $^ { 0 + }$ thetaa\*0.5\*x)/(exp(x-etaa)+1.0);   
else return pow(x,kk)\*sqrt(1. $^ { 0 + }$ thetaa\*0.5\*x)/(exp(x-etaa)+1.0);

# }

# oub Fermi::val(const Doub k, const Doub eta, const Doub theta)

Computes the generalized Fermi-Dirac integral $F _ { k } ( \eta , \theta )$ , where $k > - 1$ and $\theta \ge 0$ . The accuracy is approximately the square of the parameter EPS. NMAX limits the total number of quadrature steps.

Load the arguments into the member variables for use in the function evaluations.

const Doub EPS $^ { \mathtt { = 3 } }$ .0e-9;   
const Int NMAX $= 1 1$ ;   
Doub a,aa,b,bb,hmax,olds,sum;   
$\mathbf { k } \mathbf { k } { = } \mathbf { k }$ ;   
etaa=eta;   
thetaa $\cdot ^ { = }$ theta;   
if (eta $< =$ 15.0) { a=-4.5; $\mathtt { b } = 5$ .0; Trapzd<Fermi> s(\*this,a,b); for (Int $\dot { 1 } = 1$ ; $\mathrm { i } < =$ NMAX; $\Dot { 1 } + +$ ) { sum=s.next(); if (i > 3) if (abs(sum-olds) $< =$

Set limits for $x = \exp ( t - e ^ { - t } )$ mapping.

return sum; olds $=$ sum; Save value for next convergence test. } } else { a=0.0; Set limits for DE rule. $\mathtt { b } =$ eta; aa=eta; bb ${ } ^ { 1 = }$ eta+60.0; hmax ${ = } 4$ .3; Big enough to handle negative $k$ or large $\eta$ . DErule<Fermi> s(\*this,a,b,hmax); DErule<Fermi> ss(\*this,aa,bb,hmax); for (Int $\dot { \mathbf { 1 } } = 1$ ; $\mathrm { i } < =$ NMAX; $\dot { \bar { \lambda } } + +$ ) { sum $= \tt s$ .next()+ss.next(); if ( $\textsuperscript { i } > 3 )$ if (abs(sum-olds) $< =$ EPS\*abs(olds)) return sum; olds=sum; } throw("no convergence in fermi"); return 0.0;

You get values of the Fermi-Dirac functions by declaring a Fermi object:

# Fermi ferm;

and then making repeated calls to the val function:

ans=ferm.val(k,eta,theta);

Other quadrature methods exist for these functions [5-7]. A reasonably efficient method [8] involves trapezoidal quadrature with “pole correction,” but it is restricted to $\theta \lesssim 0 . 2$ . Generalized Bose-Einstein integrals can also be computed by the DE rule or the methods in these references.

# CITED REFERENCES AND FURTHER READING:

Cox, J.P., and Giuli, R.T. 1968, Principles of Stellar Structure (New York: Gordon and Breach), vol. II, $\ S 2 4 . 7$ .[1]   
Macleod, A.J. 1998, “Fermi-Dirac Functions of Order $- 1 / 2 , 1 / 2 , 3 / 2 , 5 / 2 .$ ,” ACM Transactions on Mathematical Software,vol. 24, pp.1-12.(Algorithm 779,available from netlib.)[2]   
Goano, M. 1995, “Computation of the Complete and Incomplete Fermi-Dirac Integral,” ACM Transactions on Mathematical Software,vol.21,pp.221-232.(Algorithm 745,available from netlib.)[3]   
Natarajan, A., and Kumar, N.M. 1993, “On the Numerical Evaluation of the Generalised Fermi-Dirac Integrals,” Computer Physics Communications, vol. 76, pp. 48–50.[4]   
Pichon, B. 1989, “Numerical Calculation of the Generalized Fermi-Dirac Integrals,” Computer Physics Communications, vol.55, pp.127-136.[5]   
Sagar, R.P. 1991, “A Gaussian Quadrature for the Calculation of Generalized Fermi-Dirac Integrals,” Computer Physics Communications, vol. 66, pp. 271–275.[6]   
Gautschi, W. 1992, “On the Computation of Generalized Fermi-Dirac and Bose-Einstein Integrals,” Computer Physics Communications, vol. 74, pp. 233–238.[7]   
Mohankumar, N., and Natarajan, A. 1996, “A Note on the Evaluation of the Generalized Fermi-Dirac Integral,” Astrophysical Journal, vol. 458, pp. 233–235.[8]

![](images/aad0a5c881053367886c3db2fa92d1c4b107d1379353ccd001d3356b1ac0c490.jpg)  
Figure 6.11.1. The function $x \log ( x )$ is shown for $0 < x < 1$ . Although nearly invisible, an essential singularity at $x = 0$ makes this function tricky to invert.

# 6.11 Inverse of the Function x log(x)

The function

$$
y ( x ) = x \log ( x )
$$

and its inverse function $x ( y )$ occur in a number of statistical and information theoretical contexts. Obviously $y ( x )$ is nonsingular for all positive $x$ , and easy to evaluate. For $x$ between 0 and 1, it is negative, with a single minimum at $( x , y ) =$ $( e ^ { - 1 } , - e ^ { - 1 } )$ . The function has the value 0 at $x = 1$ , and it has the value 0 as its limit at $x = 0$ , since the linear factor $x$ easily dominates the singular logarithm.

Computing the inverse function $x ( y )$ is, however, not so easy. (We will need this inverse in $\ 8 6 . 1 4 . 1 2 .$ ) From the appearance of Figure 6.11.1, it might seem easy to invert the function on its left branch, that is, return a value $x$ between 0 and $e ^ { - 1 }$ for every value $y$ between 0 and $- e ^ { - 1 }$ . However, the lurking logarithmic singularity at $x = 0$ causes difficulties for many methods that you might try.

Polynomial fits work well over any range of $y$ that is less than a decade or so (e.g., from 0.01 to 0.1), but fail badly if you demand high fractional precision extending all the way to $y = 0$ .

What about Newton’s method? We write

$$
\begin{array} { c } { { f ( x ) \equiv x \log ( x ) - y } } \\ { { f ^ { \prime } ( x ) = 1 + \log ( x ) } } \end{array}
$$

giving the iteration

$$
x _ { i + 1 } = x _ { i } - { \frac { x _ { i } \log ( x _ { i } ) - y } { 1 + \log ( x _ { i } ) } }
$$

This doesn’t work. The problem is not with its rate of convergence, which is of course quadratic for any finite $y \ i f$ we start close enough to the solution (see $\ S 9 . 4 )$ . The problem is that the region in which it converges at all is very small, especially as $y  0$ . So, if we don’t already have a good approximation as we approach the singularity, we are sunk.

If we change variables, we can get different (not computationally equivalent) versions of Newton’s method. For example, let

$$
u \equiv \log ( x ) , \qquad x = e ^ { u }
$$

Newton’s method in $u$ looks like this:

$$
\begin{array} { l } { f ( u ) = u e ^ { u } - y } \\ { f ^ { \prime } ( u ) = ( 1 + u ) e ^ { u } } \\ { u _ { i + 1 } = u _ { i } - \displaystyle \frac { u _ { i } - e ^ { - u _ { i } } y } { 1 + u _ { i } } } \end{array}
$$

But it turns out that iteration (6.11.5) is no better than (6.11.3).

The observation that leads to a good solution is that, since its log term varies only slowly, $y = x \log ( x )$ is only very modestly curved when it is plotted in log-log coordinates. (Actually it is the negative of $y$ that is plotted, since log-log coordinates require positive quantities.) Algebraically, we rewrite equation (6.11.1) as

$$
( - y ) = ( - u ) e ^ { u }
$$

(with $u$ as defined above) and take logarithms, giving

$$
\log ( - y ) = u + \log ( - u )
$$

This leads to the Newton formulas,

$$
\begin{array} { l } { f ( u ) = u + \log ( - u ) - \log ( - y ) } \\ { f ^ { \prime } ( u ) = \frac { u + 1 } { u } } \\ { u _ { i + 1 } = u _ { i } + \frac { u _ { i } } { u _ { i } + 1 } \left[ \log \left( \frac { y } { u _ { i } } \right) - u _ { i } \right] } \end{array}
$$

It turns out that the iteration (6.11.8) converges quadratically over quite a broad region of initial guesses. For $- 0 . 2 < y < 0$ , you can just choose $^ { - 1 0 }$ (for example) as a fixed initial guess. When $- 0 . 2 \ < \ y \ < \ - e ^ { - 1 }$ , one can use the Taylor series expansion around $x = e ^ { - 1 }$ ,

$$
y ( x - e ^ { - 1 } ) = - e ^ { - 1 } + { \textstyle \frac { 1 } { 2 } } e ( x - e ^ { - 1 } ) ^ { 2 } + \cdots
$$

which yields

$$
x \approx e ^ { - 1 } - \sqrt { 2 e ^ { - 1 } ( y + e ^ { - 1 } ) }
$$

With these initial guesses, (6.11.8) never takes more than six iterations to converge to double precision accuracy, and there is just one log and a few arithmetic operations per iteration. The implementation looks like this:

# Doub invxlogx(Doub y) {

For negative $y$ , $0 > y > - e ^ { - 1 }$ , return $x$ such that $y = x \log ( x )$ . The value returned is always the smaller of the two roots and is in the range $0 < x < e ^ { - 1 }$

const Doub ooe $\qquad = \ 0$ .367879441171442322;   
Doub t,u,to ${ = } 0$ .;   
if $( \mathtt { y } ) = 0$ . || y $< =$ -ooe) throw("no such inverse value");   
if (y $< ~ - 0 . 2 )$ u $=$ log(ooe-sqrt( $^ { 2 * }$ ooe\*(y+ooe))); First approximation by inverse   
else $\mathrm { ~ u ~ } = \mathrm { ~ - 1 0 ~ }$ .; of Taylor series.   
do { See text for derivation. $\mathrm { ~ u ~ } + = \mathrm { ~ ( t = ( \log { ( y / u ) } - u ) * ( u / ( 1 . + u ) ) ~ ) ~ }$ ; if (t < 1.e-8 && abs(t+to) $< 0$ .01\*abs(t)) break; to = t;   
} while (abs(t/u) $>$ 1.e-15);   
return exp(u);

# 6.12 Elliptic Integrals and Jacobian Elliptic Functions

Elliptic integrals occur in many applications, because any integral of the form

$$
\int R ( t , s ) \ d t
$$

where $R$ is a rational function of $t$ and $s$ , and $s$ is the square root of a cubic or quartic polynomial in $t$ , can be evaluated in terms of elliptic integrals. Standard references [1] describe how to carry out the reduction, which was originally done by Legendre. Legendre showed that only three basic elliptic integrals are required. The simplest of these is

$$
I _ { 1 } = \int _ { y } ^ { x } \frac { d t } { \sqrt { ( a _ { 1 } + b _ { 1 } t ) ( a _ { 2 } + b _ { 2 } t ) ( a _ { 3 } + b _ { 3 } t ) ( a _ { 4 } + b _ { 4 } t ) } }
$$

where we have written the quartic $s ^ { 2 }$ in factored form. In standard integral tables [2], one of the limits of integration is always a zero of the quartic, while the other limit lies closer than the next zero, so that there is no singularity within the interval. To evaluate $I _ { 1 }$ , we simply break the interval $[ y , x ]$ into subintervals, each of which either begins or ends on a singularity. The tables, therefore, need only distinguish the eight cases in which each of the four zeros (ordered according to size) appears as the upper or lower limit of integration. In addition, when one of the $b$ ’s in (6.12.2) tends to zero, the quartic reduces to a cubic, with the largest or smallest singularity moving to $\pm \infty$ ; this leads to eight more cases (actually just special cases of the first eight). The 16 cases in total are then usually tabulated in terms of Legendre’s standard elliptic integral of the first kind, which we will define below. By a change of the variable of integration $t$ , the zeros of the quartic are mapped to standard locations on the real axis. Then only two dimensionless parameters are needed to tabulate Legendre’s integral. However, the symmetry of the original integral (6.12.2) under permutation of the roots is concealed in Legendre’s notation. We will get back to Legendre’s notation below. But first, here is a better approach:

Carlson [3] has given a new definition of a standard elliptic integral of the first kind,

$$
R _ { F } ( x , y , z ) = { \frac { 1 } { 2 } } \int _ { 0 } ^ { \infty } { \frac { d t } { \sqrt { ( t + x ) ( t + y ) ( t + z ) } } }
$$

where $x , y$ , and $z$ are nonnegative and at most one is zero. By standardizing the range of integration, he retains permutation symmetry for the zeros. (Weierstrass’ canonical form also has this property.) Carlson first shows that when $x$ or $y$ is a zero of the quartic in (6.12.2), the integral $I _ { 1 }$ can be written in terms of $R _ { F }$ in a form that is symmetric under permutation of the remaining three zeros. In the general case, when neither $x$ nor $y$ is a zero, two such $R _ { F }$ functions can be combined into a single one by an addition theorem, leading to the fundamental formula

$$
I _ { 1 } = 2 R _ { F } ( U _ { 1 2 } ^ { 2 } , U _ { 1 3 } ^ { 2 } , U _ { 1 4 } ^ { 2 } )
$$

where

$$
\begin{array} { l c r } { { U _ { i j } = ( X _ { i } X _ { j } Y _ { k } Y _ { m } + Y _ { i } Y _ { j } X _ { k } X _ { m } ) / ( x - y ) } } \\ { { \nonumber } } \\ { { X _ { i } = ( a _ { i } + b _ { i } x ) ^ { 1 / 2 } , \qquad Y _ { i } = ( a _ { i } + b _ { i } y ) ^ { 1 / 2 } } } \end{array}
$$

and $i , j , k , m$ is any permutation of 1; 2; 3; 4. A short-cut in evaluating these expressions is

$$
\begin{array} { c } { { U _ { 1 3 } ^ { 2 } = U _ { 1 2 } ^ { 2 } - ( a _ { 1 } b _ { 4 } - a _ { 4 } b _ { 1 } ) ( a _ { 2 } b _ { 3 } - a _ { 3 } b _ { 2 } ) } } \\ { { U _ { 1 4 } ^ { 2 } = U _ { 1 2 } ^ { 2 } - ( a _ { 1 } b _ { 3 } - a _ { 3 } b _ { 1 } ) ( a _ { 2 } b _ { 4 } - a _ { 4 } b _ { 2 } ) } } \end{array}
$$

The $U$ ’s correspond to the three ways of pairing the four zeros, and $I _ { 1 }$ is thus manifestly symmetric under permutation of the zeros. Equation (6.12.4) therefore reproduces all 16 cases when one limit is a zero, and also includes the cases when neither limit is a zero.

Thus Carlson’s function allows arbitrary ranges of integration and arbitrary positions of the branch points of the integrand relative to the interval of integration. To handle elliptic integrals of the second and third kinds, Carlson defines the standard integral of the third kind as

$$
R _ { J } ( x , y , z , p ) = { \frac { 3 } { 2 } } \int _ { 0 } ^ { \infty } { \frac { d t } { ( t + p ) { \sqrt { ( t + x ) ( t + y ) ( t + z ) } } } }
$$

which is symmetric in $x , y$ , and $z$ . The degenerate case when two arguments are equal is denoted

$$
R _ { D } ( x , y , z ) = R _ { J } ( x , y , z , z )
$$

and is symmetric in $x$ and $y$ . The function $R _ { D }$ replaces Legendre’s integral of the second kind. The degenerate form of $R _ { F }$ is denoted

$$
R _ { C } ( x , y ) = R _ { F } ( x , y , y )
$$

It embraces logarithmic, inverse circular, and inverse hyperbolic functions.

Carlson [4-7] gives integral tables in terms of the exponents of the linear factors of the quartic in (6.12.1). For example, the integral where the exponents are $( \frac { 1 } { 2 } , \frac { 1 } { 2 } , - \frac { 1 } { 2 } , - \frac { 3 } { 2 } )$ can be expressed as a single integral in terms of $R _ { D }$ ; it accounts for 144 separate cases in Gradshteyn and Ryzhik [2]!

Refer to Carlson’s papers [3-8] for some of the practical details in reducing elliptic integrals to his standard forms, such as handling complex-conjugate zeros.

Turn now to the numerical evaluation of elliptic integrals. The traditional methods [9] are Gauss or Landen transformations. Descending transformations decrease the modulus $k$ of the Legendre integrals toward zero, and increasing transformations increase it toward unity. In these limits the functions have simple analytic expressions. While these methods converge quadratically and are quite satisfactory for integrals of the first and second kinds, they generally lead to loss of significant figures in certain regimes for integrals of the third kind. Carlson’s algorithms [10,11], by contrast, provide a unified method for all three kinds with no significant cancellations.

The key ingredient in these algorithms is the duplication theorem:

$$
\begin{array} { c } { { R _ { F } ( x , y , z ) = 2 R _ { F } ( x + \lambda , y + \lambda , z + \lambda ) } } \\ { { { } } } \\ { { = R _ { F } \left( \displaystyle { \frac { x + \lambda } { 4 } } , \displaystyle { \frac { y + \lambda } { 4 } } , \displaystyle { \frac { z + \lambda } { 4 } } \right) } } \end{array}
$$

where

$$
\lambda = ( x y ) ^ { 1 / 2 } + ( x z ) ^ { 1 / 2 } + ( y z ) ^ { 1 / 2 }
$$

This theorem can be proved by a simple change of variable of integration [12]. Equation (6.12.11) is iterated until the arguments of $R _ { F }$ are nearly equal. For equal arguments we have

$$
R _ { F } ( x , x , x ) = x ^ { - 1 / 2 }
$$

When the arguments are close enough, the function is evaluated from a fixed Taylor expansion about (6.12.13) through fifth-order terms. While the iterative part of the algorithm is only linearly convergent, the error ultimately decreases by a factor of $\dot { 4 } ^ { 6 } = 4 0 9 6$ for each iteration. Typically only two or three iterations are required, perhaps six or seven if the initial values of the arguments have huge ratios. We list the algorithm for $R _ { F }$ here, and refer you to Carlson’s paper [10] for the other cases.

Stage 1: For $n = 0 , 1 , 2 , \ldots$ compute

$$
\begin{array} { r l } & { \mu _ { n } = ( x _ { n } + y _ { n } + z _ { n } ) / 3 } \\ & { X _ { n } = 1 - ( x _ { n } / \mu _ { n } ) , \quad Y _ { n } = 1 - ( y _ { n } / \mu _ { n } ) , \quad Z _ { n } = 1 - ( z _ { n } / \mu _ { n } ) } \\ & { \epsilon _ { n } = \operatorname* { m a x } ( | X _ { n } | , | Y _ { n } | , | Z _ { n } | ) } \end{array}
$$

If $\epsilon _ { n } \ <$ tol, go to Stage 2; else compute

$$
\begin{array} { r l } { \lambda _ { n } = ( x _ { n } y _ { n } ) ^ { 1 / 2 } + ( x _ { n } z _ { n } ) ^ { 1 / 2 } + ( y _ { n } z _ { n } ) ^ { 1 / 2 } ~ } & { { } } \\ { x _ { n + 1 } = ( x _ { n } + \lambda _ { n } ) / 4 , \quad y _ { n + 1 } = ( y _ { n } + \lambda _ { n } ) / 4 , \quad z _ { n + 1 } = ( z _ { n } + \lambda _ { n } ) / 4 } \end{array}
$$

and repeat this stage.

Stage 2: Compute

$$
\begin{array} { r l } & { E _ { 2 } = X _ { n } Y _ { n } - Z _ { n } ^ { 2 } , \quad E _ { 3 } = X _ { n } Y _ { n } Z _ { n } } \\ & { R _ { F } = ( 1 - \frac { 1 } { 1 0 } E _ { 2 } + \frac { 1 } { 1 4 } E _ { 3 } + \frac { 1 } { 2 4 } E _ { 2 } ^ { 2 } - \frac { 3 } { 4 4 } E _ { 2 } E _ { 3 } ) / ( \mu _ { n } ) ^ { 1 / 2 } } \end{array}
$$

In some applications the argument $p$ in $R _ { J }$ or the argument $y$ in $R _ { C }$ is negative, and the Cauchy principal value of the integral is required. This is easily handled by using the formulas

$$
\begin{array} { c } { { R _ { J } ( x , y , z , p ) = } } \\ { { \ } } \\ { { \left[ ( \gamma - y ) R _ { J } ( x , y , z , \gamma ) - 3 R _ { F } ( x , y , z ) + 3 R _ { C } ( x z / y , p \gamma / y ) \right] / ( y - p ) } } \end{array}
$$

where

$$
\gamma \equiv y + { \frac { ( z - y ) ( y - x ) } { y - p } }
$$

is positive if $p$ is negative, and

$$
R _ { C } ( x , y ) = \left( \frac { x } { x - y } \right) ^ { 1 / 2 } R _ { C } ( x - y , - y )
$$

The Cauchy principal value of $R _ { J }$ has a zero at some value of $p < 0$ , so (6.12.14) will give some loss of significant figures near the zero.

Doub rf(const Doub x, const Doub y, const Doub z) {   
Computes Carlson’s elliptic integral of the first kind, $R _ { F } ( x , y , z )$ . x, $y$ , and $z$ must be non  
negative, and at most one can be zero. static const Doub ERRTOL $\mathtt { \Omega } = 0$ .0025, THIRD $^ { 1 = 1 }$ .0/3.0, $\mathtt { C 1 } = 1$ .0/24.0, ${ \tt C } 2 { = } 0 . 1$ , $\mathtt { C 3 } = 3$ .0/44.0, $\mathtt { C 4 } = 1$ .0/14.0; static const Doub TINY $\mathtt  \mathtt  \mathtt  \mathtt  \mathtt  \mathtt  \mathtt  \mathtt \mathtt  \mathtt  \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt $ . $^ { 0 * }$ numeric_limits<Doub>::min(), $\mathtt { B I G } { = } 0 . 2 *$ numeric_limits<Doub>::max(); Doub alamb,ave,delx,dely,delz,e2,e3,sqrtx,sqrty,sqrtz,xt,yt,zt; if (MIN(MIN(x,y),z) $< ~ 0 . 0$ || MIN(MIN(x+y,x+z), $y + z$ ) $<$ TINY || MAX(MAX(x,y),z) $>$ BIG) throw("invalid arguments in rf"); xt=x; $y t = y$ ; zt=z; do { sqrtx $\cdot ^ { = }$ sqrt(xt); sqrty $=$ sqrt(yt); sqrtz sqrt(zt); alamb sqrtx\*(sqrty+sqrtz)+sqrty\*sqrtz; xt=0.25\*(xt+alamb); yt=0.25\*(yt+alamb); zt=0.25\*(zt+alamb); ave=THIRD\*(xt+yt+zt); delx (ave-xt)/ave; dely $=$ (ave-yt)/ave; delz=(ave-zt)/ave; } while (MAX(MAX(abs(delx),abs(dely)),abs(delz)) $>$ ERRTOL); e2=delx\*dely-delz\*delz; e3=delx\*dely\*delz; return (1. $^ { 0 + }$ (C1\*e2-C2-C3\*e3)\*e2+C4\*e3)/sqrt(ave);

A value of 0.0025 for the error tolerance parameter gives full double precision (16 significant digits). Since the error scales as $\epsilon _ { n } ^ { 6 }$ , we see that 0.08 would be adequate for single precision (7 significant digits), but would save at most two or three more iterations. Since the coefficients of the sixth-order truncation error are different for the other elliptic functions, these values for the error tolerance should be set to 0.04 (single precision) or 0.0012 (double precision) in the algorithm for $R _ { C }$ , and 0.05 or 0.0015 for $R _ { J }$ and $R _ { D }$ . As well as being an algorithm in its own right for certain combinations of elementary functions, the algorithm for $R _ { C }$ is used repeatedly in the computation of $R _ { J }$ .

The $\mathrm { C } { + } { + }$ implementations test the input arguments against two machine-dependent constants, TINY and BIG, to ensure that there will be no underflow or overflow during the computation. You can always extend the range of admissible argument values by using the homogeneity relations (6.12.22), below.

Doub rd(const Doub x, const Doub y, const Doub z) {   
Computes Carlson’s elliptic integral of the second kind, $R _ { D } ( x , y , z )$ . $x$ and $y$ must be nonneg  
ative, and at most one can be zero. z must be positive. static const Doub ERRTOL $_ { * 0 }$ .0015, $\mathtt { C 1 } = 3$ .0/14.0, $\mathtt { C 2 } = 1$ .0/6.0, $\mathtt { C 3 } = 9$ .0/22.0, C4=3.0/26.0, $\mathtt { C 5 = 0 } \mathtt { \ . 2 5 * C 3 }$ , $\mathrm { C 6 } { = } 1 \ . 5 { * } \mathrm { C } 4$ ; static const Doub TINY $^ { - 2 }$ . $^ { 0 * }$ pow(numeric_limits<Doub>::max(),-2./3.), BIG $\scriptstyle = 0$ .1\*ERRTOL\*pow(numeric_limits<Doub>::min(),-2./3.); Doub alamb,ave,delx,dely,delz,ea,eb,ec,ed,ee,fac,sqrtx,sqrty, sqrtz,sum,xt,yt,zt; if (MIN(x,y) $<$ 0.0 || MIN(x+y,z) $<$ TINY || MAX(MAX(x,y),z) $>$ BIG) throw("invalid arguments in rd"); xt=x; yt=y; $z { \ t } { = } z$ ; sum $= 0$ .0; fac $= 1$ .0; do { sqrtx=sqrt(xt); sqrty sqrt(yt); sqrtz $=$ sqrt(zt); alamb $=$ sqrtx\*(sqrty+sqrtz)+sqrty\*sqrtz; sum $+ =$ fac/(sqrtz\*(zt+alamb)); fac ${ = } 0$ .25\*fac; xt=0.25\*(xt+alamb); yt=0.25\*(yt+alamb); zt ${ = } 0$ .25\*(zt+alamb); ave ${ = } 0$ . $^ { 2 * }$ (xt+yt+3.0\*zt); delx $: =$ (ave-xt)/ave; dely $=$ (ave-yt)/ave; delz $=$ (ave-zt)/ave;   
} while (MAX(MAX(abs(delx),abs(dely)),abs(delz)) $>$ ERRTOL);   
ea=delx\*dely;   
eb=delz\*delz;   
ec=ea-eb;   
ed=ea-6.0\*eb;   
ee=ed+ec+ec;   
return 3.0\*sum+fac\*(1.0+ed\*(-C1+C5\*ed-C6\*delz\*ee) +delz\*(C2\*ee+delz\*(-C3\*ec+delz\*C4\*ea)))/(ave\*sqrt(ave));

# elliptint.h

Doub rj(const Doub x, const Doub y, const Doub z, const Doub p) { Computes Carlson’s elliptic integral of the third kind, $R _ { J } ( x , y , z , p )$ . $x$ , $y$ , and $z$ must be nonnegative, and at most one can be zero. $p$ must be nonzero. If $p < 0$ , the Cauchy principal value is returned.

static const Doub ERRTOL $_ { , = 0 }$ .0015, $\mathrm { C } \mathrm { 1 } = \mathrm { 3 }$ .0/14.0, $\mathtt { C 2 } = 1$ .0/3.0, $\mathtt { C 3 } = 3$ .0/22.0, C4=3.0/26.0, $\mathtt { C 5 } { = } 0 . 7 5 { * } \mathtt { C } 3$ , $\mathtt { C 6 = 1 }$ . $5 * \mathrm { C 4 }$ , ${ \mathsf { C } } 7 { = } 0 \ldots { } 5 { * } { \mathsf { C } } 2$ , $_ { \mathsf { C } } 8 \mathrm { = } \mathsf { C } 3 \mathrm { + } \mathsf { C } 3$ ;   
static const Doub TINY $\mathrm { \Delta } =$ pow(5. $^ { 0 * }$ numeric_limits<Doub>::min(),1./3.), BIG $\scriptstyle = 0$ .3\*pow(0. $^ { 2 * }$ numeric_limits<Doub>::max(),1./3.);   
Doub a,alamb,alpha,ans,ave,b,beta,delp,delx,dely,delz,ea,eb,ec,ed,ee, fac,pt,rcx,rho,sqrtx,sqrty,sqrtz,sum,tau,xt,yt,zt;   
if (MIN(MIN(x,y),z) $< ~ 0 . 0$ || MIN(MIN $( \mathbf { x } + \mathbf { y } , \mathbf { x } + \mathbf { z } )$ ),MIN $( y + z$ ,abs(p))) $<$ TINY || MAX(MAX(x,y),MAX(z,abs(p))) $>$ BIG) throw("invalid arguments in rj");   
sum $= 0$ .0;   
fac $^ { = 1 }$ .0;   
if $( \mathtt { p } > 0 . 0 )$ { $\tt x t = \tt x$ ; $\tt y t = y$ ; $z { \ t } { = } z$ ; pt=p; else { xt=MIN(MIN(x,y),z); zt=MAX(MAX(x,y),z); yt=x+y+z-xt-zt; a=1.0/(yt-p); b=a\*(zt-yt)\*(yt-xt); pt=yt+b; rho=xt\*zt/yt; tau=p\*pt/yt; rcx=rc(rho,tau);   
}   
do { sqrtx sqrt(xt); sqrty=sqrt(yt); sqrtz $=$ sqrt(zt); alamb $\mid =$ sqrtx\*(sqrty+sqrtz)+sqrty\*sqrtz; alpha SQR(pt\*(sqrtx+sqrty+sqrtz)+sqrtx\*sqrty\*sqrtz); beta=pt\*SQR(pt+alamb); sum $+ =$ fac\*rc(alpha,beta); fac ${ = } 0$ .25\*fac; xt=0.25\*(xt+alamb); yt=0.25\*(yt+alamb);

zt=0.25\*(zt+alamb); pt=0.25\*(pt+alamb); ave ${ = } 0$ .2\*(xt+yt+zt+pt+pt); delx=(ave-xt)/ave; dely $=$ (ave-yt)/ave; delz $=$ (ave-zt)/ave; delp (ave-pt)/ave; } while (MAX(MAX(abs(delx),abs(dely)), MAX(abs(delz),abs(delp))) $>$ ERRTOL); ea=delx\*(dely+delz)+dely\*delz; eb=delx\*dely\*delz; ec=delp\*delp; ed=ea-3.0\*ec; ee=eb $^ { + 2 }$ .0\*delp\*(ea-ec); ans $^ { = 3 }$ . $^ { 0 * }$ sum+fac\*(1. $^ { 0 + }$ ed\*(-C1+C5\*ed-C6\*ee)+eb\*(C7+delp\*(-C8+delp\*C4)) +delp\*ea\*(C2-delp\*C3)-C2\*delp\*ec)/(ave\*sqrt(ave)); if $_ { \mathrm { ~ \tiny ~ P ~ } } < = \mathrm { ~ \tiny ~ 0 ~ . ~ 0 ~ }$ ) ans=a\*(b\*ans+3.0\*(rcx-rf(xt,yt,zt))); return ans;

Doub rc(const Doub x, const Doub y) {   
Computes Carlson’s degenerate elliptic integral, $R _ { C } ( x , y )$ . x must be nonnegative and $y$ must be nonzero. If $y < 0$ , the Cauchy principal value is returned.   
static const Doub ERRTOL ${ = } 0$ .0012, THIRD $^ { 1 = 1 }$ .0/3.0, $\mathrm { C 1 } { = } 0 . 3$ , $\mathtt { C 2 } = 1$ .0/7.0, $\mathtt { C 3 } = 0$ .375, $\mathtt { C 4 } = 9$ .0/22.0;   
static const Doub TINY $\mathtt  \mathtt  \mathtt  \mathtt  \mathtt  \mathtt  \mathtt  \mathtt \mathtt  \mathtt  \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt $ . $^ { 0 * }$ numeric_limits<Doub>::min(), $\mathtt { B I G } = 0$ . $^ { 2 \ast }$ numeric_limits<Doub>::max(), COMP1=2.236/sqrt(TINY), COMP2 $\mathbf { \equiv }$ SQR(TINY\*BIG)/25.0;   
Doub alamb,ave,s,w,xt,yt;   
if $\mathit { \check { x } } ~ < ~ 0 . 0$ || $\ y \ = = \ 0 . 0$ || $\mathbf { x } +$ abs(y)) $<$ TINY || ( $^ { \mathbb { X } + }$ abs(y)) $>$ BIG || (y<-COMP1 && $\textbf { z } > \ 0 . 0$ && $\mathrm { ~ x ~ } <$ COMP2)) throw("invalid arguments in rc");   
if $( \mathrm { y } > 0 . 0 )$ { $\tt x t = x$ ; yt=y; $\scriptstyle { \mathtt { w } } = 1$ .0;   
} else { xt=x-y; yt= -y; w=sqrt(x)/sqrt(xt);   
}   
do { alamb $^ { - 2 }$ .0\*sqrt(xt)\*sqrt(yt)+yt; xt ${ = } 0$ .25\*(xt+alamb); yt ${ = } 0$ .25\*(yt+alamb); ave $=$ THIRD\*(xt+yt+yt); $\mathbf { s } =$ (yt-ave)/ave;   
} while (abs(s) $>$ ERRTOL);   
return w\*(1.0+s\*s\*(C1+s\*(C2+s\*(C3+s\*C4))))/sqrt(ave);

At times you may want to express your answer in Legendre’s notation. Alternatively, you may be given results in that notation and need to compute their values with the programs given above. It is a simple matter to transform back and forth. The Legendre elliptic integral of the first kind is defined as

$$
F ( \phi , k ) \equiv \int _ { 0 } ^ { \phi } { \frac { d \theta } { \sqrt { 1 - k ^ { 2 } \sin ^ { 2 } \theta } } }
$$

The complete elliptic integral of the first kind is given by

$$
K ( k ) \equiv F ( \pi / 2 , k )
$$

In terms of $R _ { F }$

$$
\begin{array} { c } { { F ( \phi , k ) = \sin \phi R _ { F } ( \cos ^ { 2 } \phi , 1 - k ^ { 2 } \sin ^ { 2 } \phi , 1 ) } } \\ { { K ( k ) = R _ { F } ( 0 , 1 - k ^ { 2 } , 1 ) } } \end{array}
$$

The Legendre elliptic integral of the second kind and the complete elliptic integral of the second kind are given by

$$
\begin{array} { l } { \displaystyle { E ( \phi , k ) \equiv \int _ { 0 } ^ { \phi } \sqrt { 1 - k ^ { 2 } \sin ^ { 2 } \theta } ~ d \theta } } \\ { \displaystyle { \quad = \sin \phi R _ { F } ( \cos ^ { 2 } \phi , 1 - k ^ { 2 } \sin ^ { 2 } \phi , 1 ) } } \\ { \displaystyle { \qquad - \frac { 1 } { 3 } k ^ { 2 } \sin ^ { 3 } \phi R _ { D } ( \cos ^ { 2 } \phi , 1 - k ^ { 2 } \sin ^ { 2 } \phi , 1 ) } } \\ { \displaystyle { E ( k ) \equiv E ( \pi / 2 , k ) = R _ { F } ( 0 , 1 - k ^ { 2 } , 1 ) - \frac { 1 } { 3 } k ^ { 2 } R _ { D } ( 0 , 1 - k ^ { 2 } , 1 ) } } \end{array}
$$

Finally, the Legendre elliptic integral of the third kind is

$$
\begin{array} { l } { \displaystyle \Pi ( \phi , n , k ) \equiv \int _ { 0 } ^ { \phi } \frac { d \theta } { \displaystyle ( 1 + n \sin ^ { 2 } \theta ) \sqrt { 1 - k ^ { 2 } \sin ^ { 2 } \theta } } } \\ { \displaystyle = \sin \phi R _ { F } ( \cos ^ { 2 } \phi , 1 - k ^ { 2 } \sin ^ { 2 } \phi , 1 ) } \\ { \displaystyle \qquad - \frac { 1 } { 3 } n \sin ^ { 3 } \phi R _ { J } ( \cos ^ { 2 } \phi , 1 - k ^ { 2 } \sin ^ { 2 } \phi , 1 , 1 + n \sin ^ { 2 } \phi ) } \end{array}
$$

(Note that this sign convention for $n$ is opposite that of Abramowitz and Stegun [13], and that their $\sin \alpha$ is our $k$ .)

Doub ellf(const Doub phi, const Doub ak) $\begin{array} { r } { \mathopen { } \mathclose \bgroup \left\{ \begin{array} { r l r l } \end{array} \aftergroup \egroup \right. } \end{array}$   
Legendre elliptic integral of the first kind $F ( \phi , k )$ , evaluated using Carlson’s function $R _ { F }$ . The argument ranges are $0 \leq \phi \leq \pi / 2$ , $0 \leq k \sin \phi \leq 1$ .

Doub s=sin(phi); return s\*rf(SQR(cos(phi)), $( 1 . 0 \mathrm { - } \mathrm { s } \ast \mathrm { a k } ) \ast ( 1 . 0 \mathrm { + } \mathrm { s } \ast \mathrm { a k } ) , 1 . 0 ) ;$ }

# elliptint.h

# Doub elle(const Doub phi, const Doub ak) $\left\{ \begin{array} { r l } \end{array} \right.$

Legendre elliptic integral of the second kind $E ( \phi , k )$ , evaluated using Carlson’s functions $R _ { D }$ and $R _ { F }$ . The argument ranges are $0 \leq \phi \leq \pi / 2$ , $0 \leq k \sin \phi \leq 1$ .

Doub cc,q,s;   
$\mathbf { s } =$ sin(phi);   
cc=SQR(cos(phi));   
$\mathsf { q } = \left( 1 \mathsf { \ldots } 0 \mathsf { - s } \mathsf { * a k } \right) \mathsf { \ldots } \left( 1 \mathsf { \ldots } 0 \mathsf { + s } \mathsf { * a k } \right) \mathsf { \ldots }$ ;   
return s\*(rf(cc,q,1.0)-(SQR(s\*ak))\*rd(cc,q,1.0)/3.0);

# elliptint.h

Doub ellpi(const Doub phi, const Doub en, const Doub ak) {

Legendre elliptic integral of the third kind $\scriptstyle \Pi ( \phi , n , k )$ , evaluated using Carlson’s functions $R J$ and $R _ { F }$ . (Note that the sign convention on $_ { n }$ is opposite that of Abramowitz and Stegun.) The ranges of $\phi$ and $k$ are $0 \leq \phi \leq \pi / 2$ , $0 \leq k \sin \phi \leq 1$ .

Doub cc,enss,q,s;   
$\mathbf { s } =$ sin(phi);   
enss=en\*s\*s;   
cc=SQR(cos(phi));   
$\mathsf { q } = \left( 1 \mathsf { \ldots } 0 \mathsf { - s } \mathsf { * a k } \right) \mathsf { \ldots } \left( 1 \mathsf { \ldots } 0 \mathsf { + s } \mathsf { * a k } \right) \vdots$ ;   
return s\*(rf(cc,q,1.0)-enss\*rj(cc,q,1.0,1.0+enss)/3.0);

# elliptint.h

Carlson’s functions are homogeneous of degree $- \frac 1 2$ and $- \frac { 3 } { 2 }$ , so

$$
\begin{array} { c } { { R _ { F } ( \lambda x , \lambda y , \lambda z ) = \lambda ^ { - 1 / 2 } R _ { F } ( x , y , z ) } } \\ { { { } } } \\ { { R _ { J } ( \lambda x , \lambda y , \lambda z , \lambda p ) = \lambda ^ { - 3 / 2 } R _ { J } ( x , y , z , p ) } } \end{array}
$$

Thus, to express a Carlson function in Legendre’s notation, permute the first three arguments into ascending order, use homogeneity to scale the third argument to be 1, and then use equations (6.12.19) – (6.12.21).

# 6.12.1 Jacobian Elliptic Functions

The Jacobian elliptic function sn is defined as follows: Instead of considering the elliptic integral

$$
u ( y , k ) \equiv u = F ( \phi , k )
$$

consider the inverse function

$$
y = \sin \phi = \sin ( u , k )
$$

Equivalently,

$$
u = \int _ { 0 } ^ { \mathrm { s n } } \frac { d y } { \sqrt { ( 1 - y ^ { 2 } ) ( 1 - k ^ { 2 } y ^ { 2 } ) } }
$$

When $k = 0$ , sn is just sin. The functions cn and dn are defined by the relations

$$
\begin{array} { r } { \mathrm { s n } ^ { 2 } + \mathrm { c n } ^ { 2 } = 1 , \qquad k ^ { 2 } \mathrm { s n } ^ { 2 } + \mathrm { d n } ^ { 2 } = 1 } \end{array}
$$

The routine given below actually takes $m _ { c } \equiv k _ { c } ^ { 2 } = 1 - k ^ { 2 }$ as an input parameter. It also computes all three functions sn, cn, and dn since computing all three is no harder than computing any one of them. For a description of the method, see [9].

void sncndn(const Doub uu, const Doub emmc, Doub &sn, Doub &cn, Doub &dn) { Returns the Jacobian elliptic functions $\mathsf { s n } ( u , k _ { c } )$ , ${ \mathsf { c n } } ( u , k _ { c } )$ , and $\mathsf { d n } ( u , k _ { c } )$ . Here $\mathtt { u u } = u$ , while emmc $= k _ { c } ^ { 2 }$ .

The accuracy is the square of CA.

static const Doub $\mathtt { C A = 1 }$ .0e-8;   
Bool bo;   
Int i,ii,l;   
Doub a,b,c,d,emc,u;   
VecDoub em(13),en(13);   
emc=emmc;   
u=uu;   
if (emc != 0.0) { bo $=$ (emc < 0.0); if (bo) { $\mathrm { d } { = } 1$ .0-emc; emc /= -1.0/d; u \*= ( $\mathtt { d } =$ sqrt(d)); } $\mathtt { a } = 1$ .0; d $\mathtt { n } { = } 1$ .0; for (i=0;i<13;i++) { $\beth = \dot { \beth }$ ; em[i] $= a$ ; en[i] $=$ (emc=sqrt(emc)); c=0.5\*(a+emc); if (abs(a-emc) $< =$ CA\*a) break; emc $\ast = \mathtt { a }$ ;

a=c; } u \*= c; sn=sin(u); cn=cos(u); if (sn $\ ! =$ 0.0) a=cn/sn; c \*= a; for (ii=l;ii>=0;ii--) b=em[ii]; a \*= c; c \*= dn; dn=(en[ii]+a)/(b+a); a=c/b; a=1.0/sqrt(c\*c+1.0); sn=(sn >= 0.0 ? a : -a); cn=c\*sn; } if (bo) { a=dn; dn=cn; $\mathtt { c n } { = } \mathtt { a }$ ; sn /= d; } } else { cn=1.0/cosh(u); dn=cn; sn=tanh(u); }

# CITED REFERENCES AND FURTHER READING:

Erdélyi, A., Magnus, W., Oberhettinger, F., and Tricomi, F.G. 1953, Higher Transcendental Functions,Vol. I,(New York: McGraw-Hill).[1]   
Gradshteyn, I.S., and Ryzhik, I.W. 1980, Table of Integrals, Series, and Products (New York: Academic Press).[2]   
Carlson, B.C. 1977, “Elliptic Integrals of the First Kind,” SIAM Journal on Mathematical Analysis, vol. 8, pp. 231–242.[3]   
Carlson, B.C. 1987, “A Table of Elliptic Integrals of the Second Kind,” Mathematics of Computation,vol.49,pp.595-606[4]; 1988,“A Table of Eliptic Integrals of the Third Kind”op.cit., vol. 51, pp. 267–280[5]; 1989, “A Table of Elliptic Integrals: Cubic Cases,” op. cit., vol. 53, pp. 327–333[6]; 1991, “A Table of Elliptic Integrals: One Quadratic Factor,” op. cit., vol. 56, pp. 267–280.[7]   
Carlson, B.C., and FitzSimons, J. 2000, “Reduction Theorems for Elliptic Integrands with the Square Root of Two Quadratic Factors,” Journal of Computational and Applied Mathematics, vol. 118,pp.71-85.[8]   
Bulirsch, R. 1965, “Numerical Calculation of Elliptic Integrals and Elliptic Functions,” Numerische Mathematik,vol.7,pp.78-90;1965,op. cit.,vol.7,pp. 353-354; 1969,op. cit.,vol.13, pp. 305–315.[9]   
Carlson, B.C. 1979, “Computing Elliptic Integrals by Duplication,” Numerische Mathematik, vol. 33, pp. 1–16.[10]   
Carlson, B.C., and Notis, E.M. 1981, “Algorithms for Incomplete Elliptic Integrals,” ACM Transactions on Mathematical Software, vol.7,pp.398-403.[11]   
Carlson, B.C. 1978, “Short Proofs of Three Theorems on Elliptic Integrals,” SIAM Journal on Mathematical Analysis, vol. 9,p. 524-528.[12]   
Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapter 17.[13]   
Mathews, J., and Walker, R.L. 1970, Mathematical Methods of Physics, 2nd ed. (Reading, MA: W.A. Benjamin/Addison-Wesley), pp. 78–79.

# 6.13 Hypergeometric Functions

As was discussed in $\ S 5 . 1 4$ , a fast, general routine for the the complex hypergeometric function $_ 2 F _ { 1 } ( a , b , c ; z )$ is difficult or impossible. The function is defined as the analytic continuation of the hypergeometric series

$$
{ \begin{array} { r l } & { _ { 2 } F _ { 1 } ( a , b , c ; z ) = 1 + { \frac { a b } { c } } { \frac { z } { 1 ! } } + { \frac { a ( a + 1 ) b ( b + 1 ) } { c ( c + 1 ) } } { \frac { z ^ { 2 } } { 2 ! } } + \cdots } \\ & { \qquad + { \frac { a ( a + 1 ) \ldots ( a + j - 1 ) b ( b + 1 ) \ldots ( b + j - 1 ) } { c ( c + 1 ) \ldots ( c + j - 1 ) } } { \frac { z ^ { j } } { j ! } } + \cdots } \end{array} }
$$

This series converges only within the unit circle $| z | < 1$ (see [1]), but one’s interest in the function is not confined to this region.

Section 5.14 discussed the method of evaluating this function by direct path integration in the complex plane. We here merely list the routines that result.

Implementation of the function hypgeo is straightforward and is described by comments in the program. The machinery associated with Chapter 17’s routine for integrating differential equations, Odeint, is only minimally intrusive and need not even be completely understood: Use of Odeint requires one function call to the constructor, with a prescribed format for the derivative routine Hypderiv, followed by a call to the integrate method.

The function hypgeo will fail, of course, for values of $Z$ too close to the singularity at 1. (If you need to approach this singularity, or the one at $\infty$ , use the “linear transformation formulas” in $\ S 1 5 . 3$ of [1].) Away from $z = 1$ , and for moderate values of $a , b , c$ , it is often remarkable how few steps are required to integrate the equations. A half-dozen is typical.

Complex hypgeo(const Complex &a, const Complex &b,const Complex &c, const Complex &z)

Complex hypergeometric function ${ } _ { 2 } F _ { 1 }$ for complex $a , b , c$ , and $z$ , by direct integration of the hypergeometric equation in the complex plane. The branch cut is taken to lie along the real axis, Re $z > 1$ .

const Doub atol $^ { = 1 }$ .0e-14,rtol $^ { = 1 }$ .0e-14; Accuracy parameters.   
Complex ans,dz,z0,y[2];   
VecDoub yy(4);   
if (norm(z) $< =$ 0.25) { Use series... hypser(a,b,c,z,ans,y[1]); return ans;   
}   
...or pick a starting point for the path integration.   
else if (real(z) $<$ 0.0) z0=Complex(-0.5,0.0);   
else if (real(z) $< = ~ 1 . 0$ ) z0=Complex(0.5,0.0); else z0=Complex(0.0,imag(z) >= 0.0 ? 0.5 : -0.5);   
dz=z-z0;   
hypser(a,b,c,z0,y[0],y[1]); Get starting function and derivative.   
yy[0] $=$ real(y[0]);   
yy[1] $=$ imag(y[0]);   
yy[2] $=$ real(y[1]);   
yy[3] $=$ imag(y[1]);   
Hypderiv d(a,b,c,z0,dz); Set up the functor for the derivatives.   
Output out; Suppress output in Odeint.   
Odeint<StepperBS<Hypderiv> $>$ ode(yy,0.0,1.0,atol,rtol,0.1,0.0,out,d);   
The arguments to Odeint are the vector of independent variables, the starting and ending values of the dependent variable, the accuracy parameters, an initial guess for the stepsize, a minimum stepsize, and the names of the output object and the derivative object. The integration is performed by the Bulirsch-Stoer stepping routine.   
ode.integrate();   
y[0] $=$ Complex(yy[0],yy[1]);   
return y[0];   
void hypser(const Complex &a, const Complex &b, const Complex &c, const Complex &z, Complex &series, Complex &deriv)   
Returns the hypergeometric series ${ } _ { 2 } F _ { 1 }$ and its derivative, iterating to machine accuracy. For   
$| z | \leq 1 / 2$ convergence is quite rapid.   
{   
deri $\mathtt { v } = 0 . 0$ ;   
Complex fac $^ { = 1 }$ .0;   
Complex temp=fac;   
Complex $\mathtt { a a } = \mathtt { a }$ ;   
Complex bb=b;   
Complex $\mathtt { C C } { = } \mathtt { C }$ ;   
for (Int $\tt { n } { = } 1$ ; $\mathtt { n < = 1 0 0 0 ; n + + } )$ ) { fac $\ast =$ ((aa\*bb)/cc); deriv $+ =$ fac; fac $\ast = \mathrm { ~ ( ~ ( ~ 1 ~ . ~ 0 / n ) \ast z ) ~ }$ ; series $=$ temp+fac; if (series $= =$ temp) return; temp=series; aa $+ = \ 1 . 0$ ; bb $+ = \ 1 . 0$ ; cc $+ = \ 1 . 0$ ;   
}   
throw("convergence failure in h

# }

# struct Hypderiv {

Functor to compute derivatives for the hypergeometric equation; see text equation (5.14.4).

Complex a,b,c,z0,dz; Hypderiv(const Complex &aa, const Complex &bb, const Complex &cc, const Complex &z00, const Complex &dzz) : a(aa),b(bb),c(cc),z0(z00),dz(dzz) {} void operator() (const Doub s, VecDoub_I &yy, VecDoub_O &dyyds) { Complex z,y[2],dyds[2]; y[0] $=$ Complex(yy[0],yy[1]); y[1]=Complex(yy[2],yy[3]); z=z0+s\*dz; dyds[0] $\mathbf { \Pi } = \mathbf { y }$ [1]\*dz; dyds[1] $=$ (a\*b\*y[0]-(c-(a+b+1.0)\*z)\*y[1])\*dz/(z\*(1.0-z)); dyyds[0] $=$ real(dyds[0]); dyyds[1] $=$ imag(dyds[0]); dyyds[2] $=$ real(dyds[1]); dyyds[3] $=$ imag(dyds[1]); } };

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands.[1]

# 6.14 Statistical Functions

Certain special functions get frequent use because of their relation to common univariate statistical distributions, that is, probability densities in a single variable. In this section we survey a number of such common distributions in a unified way, giving, in each case, routines for computing the probability density function $p ( x )$ ; the cumulative density function or cdf, written $P ( < x )$ ; and the inverse of the cumulative density function $x ( P )$ . The latter function is needed for finding the values of $x$ associated with specified percentile points or quantiles in significance tests, for example, the $0 . 5 \%$ , $5 \%$ , $9 5 \%$ or $9 9 . 5 \%$ points.

The emphasis of this section is on defining and computing these statistical functions. Section $\ S 7 . 3$ is a related section that discusses how to generate random deviates from the distributions discussed here. We defer discussion of the actual use of these distributions in statistical tests to Chapter 14.

# 6.14.1 Normal (Gaussian) Distribution

If $x$ is drawn from a normal distribution with mean $\mu$ and standard deviation $\sigma$ , then we write

$$
\begin{array} { c } { { x \sim \mathrm { N } ( \mu , \sigma ) , \sigma > 0 } } \\ { { p ( x ) = \displaystyle \frac { 1 } { \sqrt { 2 \pi } \sigma } \exp \left( - \frac { 1 } { 2 } \left[ \frac { x - \mu } { \sigma } \right] ^ { 2 } \right) } } \end{array}
$$

with $p ( x )$ the probability density function. Note the special use of the notation “” in this section, which can be read as “is drawn from a distribution.” The variance of the distribution is, of course, $\sigma ^ { 2 }$ .

The cumulative distribution function is the probability of a value $\leq x$ . For the normal distribution, this is given in terms of the complementary error function by

$$
\operatorname { c d f } \equiv P ( < x ) \equiv \int _ { - \infty } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = { \frac { 1 } { 2 } } \operatorname { e r f c } \left( - { \frac { 1 } { \sqrt { 2 } } } \left[ { \frac { x - \mu } { \sigma } } \right] \right)
$$

The inverse cdf can thus be calculated in terms of the inverse of erfc,

$$
x ( P ) = \mu - \sqrt { 2 } \sigma \mathrm { e r f c } ^ { - 1 } ( 2 P )
$$

The following structure implements the above relations.

![](images/6067bf5da51e310225eed902504246e2af8263de816533687455c48d1aa2a521.jpg)  
Figure 6.14.1. Examples of centrally peaked distributions that are symmetric on the real line. Any of these can substitute for the normal distribution either as an approximation or in applications such as robust estimation. They differ largely in the decay rate of their tails.

# struct Normaldist : Erf {

Normal distribution, derived from the error function Erf. Doub mu, sig; Normaldist(Doub mmu $\qquad = \ 0 .$ , Doub ssig $\qquad = \ 1 .$ ) : mu(mmu), sig(ssig) { Constructor. Initialize with $\mu$ and $\sigma$ . The default with no arguments is ${ \mathsf { N } } ( 0 , 1 )$ . if (sig $< = ~ 0 .$ ) throw("bad sig in Normaldist"); } Doub p(Doub x) { Return probability density function. return (0.398942280401432678/sig)\*exp(-0.5\*SQR((x-mu)/sig)); } Doub cdf(Doub x) { Return cumulative distribution function. return 0.5\*erfc(-0.707106781186547524\*(x-mu)/sig); Doub invcdf(Doub p) { Return inverse cumulative distribution function. if ( $\mathbf { \partial } \cdot \mathbf { p } < = \mathbf { \partial } 0$ . $| \mathrm { ~ l ~ } \mathrm { ~ p ~ } > = \mathrm { ~ 1 ~ } .$ ) throw("bad p in Normaldist"); return -1.41421356237309505\*sig\*inverfc $( 2 , * _ { \mathrm { P } } ) + \mathrm { m u }$ ; }   
};

We will use the conventions of the above code for all the distributions in this section. A distribution’s parameters (here, $\mu$ and $\sigma$ ) are set by the constructor and then referenced as needed by the member functions. The density function is always $\mathtt { p ( ) }$ , the cdf is cdf(), and the inverse cdf is invcdf(). We will generally check the arguments of probability functions for validity, since many program bugs can show up as, e.g., a probability out of the range Œ0; 1.

# 6.14.2 Cauchy Distribution

Like the normal distribution, the Cauchy distribution is a centrally peaked, symmetric distribution with a parameter $\mu$ that specifies its center and a parameter $\sigma$ that specifies its width. Unlike the normal distribution, the Cauchy distribution has tails that decay very slowly at infinity, as $| x | ^ { - 2 }$ , so slowly that moments higher than the zeroth moment (the area under the curve) don’t even exist. The parameter $\mu$ is therefore, strictly speaking, not the mean, and the parameter $\sigma$ is not, technically, the standard deviation. But these two parameters substitute for those moments as measures of central position and width.

The defining probability density is

$$
\begin{array} { c } { x \sim \mathrm { C a u c h y } ( \mu , \sigma ) , \qquad \sigma > 0 } \\ { p ( x ) = \displaystyle \frac { 1 } { \pi \sigma } \left( 1 + \left[ \frac { x - \mu } { \sigma } \right] ^ { 2 } \right) ^ { - 1 } } \end{array}
$$

If $x \sim { \mathrm { C a u c h y } } ( 0 , 1 )$ , then also $1 / x \sim \mathrm { C a u c h y } ( 0 , 1 )$ and also $( a x + b ) ^ { - 1 } \sim$ Cauchy $( - b / a , 1 / a )$ .

The cdf is given by

$$
\operatorname { c d f } \equiv P ( < x ) \equiv \int _ { - \infty } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = { \frac { 1 } { 2 } } + { \frac { 1 } { \pi } } \arctan \left( { \frac { x - \mu } { \sigma } } \right)
$$

The inverse cdf is given by

$$
x ( P ) = \mu + \sigma \tan \left( \pi [ P - { \textstyle { \frac { 1 } { 2 } } } ] \right)
$$

Figure 6.14.1 shows Cauchy $( 0 , 1 )$ as compared to the normal distribution $\mathrm { { N } } ( 0 , 1 )$ , as well as several other similarly shaped distributions discussed below.

The Cauchy distribution is sometimes called the Lorentzian distribution.

# struct Cauchydist {

Cauchy distribution.

Doub mu, sig;   
Cauchydist(Doub ${ \tt m m u } = 0 .$ , Doub $\mathbf { s s i g } = \mathbf { 1 . } ) \mathbf { \Sigma } : \mathrm { \ m u ( m m u ) }$ , sig(ssig) {   
Constructor. Initialize with $\mu$ and $\sigma$ . The default with no arguments is Cauchy.0; 1/. if (sig $< = ~ 0 .$ ) throw("bad sig in Cauchydist");   
}   
Doub p(Doub x) {   
Return probability density function. return 0.318309886183790671/(sig\*(1.+SQR((x-mu)/sig)));   
1   
Doub cdf(Doub x) {   
Return cumulative distribution function. return $0 . 5 \substack { + 0 }$ .318309886183790671\*atan2(x-mu,sig);   
}   
Doub invcdf(Doub p) {   
Return inverse cumulative distribution function. if $( \mathtt { p } \ < = \ 0$ . $| \texttt { p } > = 1 .$ ) throw("bad p in Cauchydist"); return mu $^ +$ sig\*tan(3.14159265358979324\*(p-0.5));   
}

# 6.14.3 Student-t Distribution

A generalization of the Cauchy distribution is the Student-t distribution, named for the early 20th century statistician William Gosset, who published under the name “Student” because his employer, Guinness Breweries, required him to use a pseudonym. Like the Cauchy distribution, the Student-t distribution has power-law tails at infinity, but it has an additional parameter $\nu$ that specifies how rapidly they decay, namely as $| t | ^ { - ( \nu + 1 ) }$ . When $\nu$ is an integer, the number of convergent moments, including the zeroth, is thus $\nu$ .

The defining probability density (conventionally written in a variable $t$ instead of $x$ ) is

$$
\begin{array} { l } { t \sim \mathrm { S t u d e n t } ( \nu , \mu , \sigma ) , \qquad \nu > 0 , \sigma > 0 } \\ { p ( t ) = \displaystyle \frac { \Gamma ( \frac { 1 } { 2 } [ \nu + 1 ] ) } { \Gamma ( \frac { 1 } { 2 } \nu ) \sqrt { \nu \pi } \sigma } \left( 1 + \frac { 1 } { \nu } \left[ \frac { t - \mu } { \sigma } \right] ^ { 2 } \right) ^ { - \frac { 1 } { 2 } ( \nu + 1 ) } } \end{array}
$$

The Cauchy distribution is obtained in the case $\nu = 1$ . In the opposite limit, $\nu \to \infty$ , the normal distribution is obtained. In pre-computer days, this was the basis of various approximation schemes for the normal distribution, now all generally irrelevant. Figure 6.14.1 shows examples of the Student-t distribution for $\nu ~ = ~ 1$ (Cauchy), $\nu = 4$ , and $\nu = 6$ . The approach to the normal distribution is evident.

The mean of Student $( \nu , \mu , \sigma )$ is (by symmetry) $\mu$ . The variance is not $\sigma ^ { 2 }$ , but rather

$$
\operatorname { V a r } \{ \operatorname { S t u d e n t } ( \nu , \mu , \sigma ) \} = \frac { \nu } { \nu - 2 } \sigma ^ { 2 }
$$

For additional moments, and other properties, see [1].

The cdf is given by an incomplete beta function. If we let

$$
x \equiv \frac { \nu } { \nu + \left( \frac { t - \mu } { \sigma } \right) ^ { 2 } }
$$

then

$$
\operatorname { c d f } \equiv P ( < t ) \equiv \int _ { - \infty } ^ { t } p ( t ^ { \prime } ) d t ^ { \prime } = { \left\{ \begin{array} { l l } { { \frac { 1 } { 2 } } I _ { x } ( { \frac { 1 } { 2 } } \nu , { \frac { 1 } { 2 } } ) , } & { t \leq \mu } \\ { 1 - { \frac { 1 } { 2 } } I _ { x } ( { \frac { 1 } { 2 } } \nu , { \frac { 1 } { 2 } } ) , } & { t > \mu } \end{array} \right. }
$$

The inverse cdf is given by an inverse incomplete beta function (see code below for the exact formulation).

In practice, the Student-t cdf is the above form is rarely used, since most statistical tests using Student-t are double-sided. Conventionally, the two-tailed function $A ( t | \nu )$ is defined (only) for the case $\mu = 0$ and $\sigma = 1$ by

$$
A ( t | \nu ) \equiv \int _ { - t } ^ { + t } p ( t ^ { \prime } ) d t ^ { \prime } = 1 - I _ { x } ( \frac { 1 } { 2 } \nu , \frac { 1 } { 2 } )
$$

with $x$ as given above. The statistic $A ( t | \nu )$ is notably used in the test of whether two observed distributions have the same mean. The code below implements both equations (6.14.10) and (6.14.11), as well as their inverses.

uct Studenttdist : Beta {   
dent-t distribution, derived from the beta function Beta.   
Doub nu, mu, sig, np, fac;   
Studenttdist(Doub nnu, Doub mmu $\qquad = \ 0 .$ , Doub ssig $\mathit { \Theta } = \mathit { \Theta } 1 \cdot$ )   
: nu(nnu), mu(mmu), sig(ssig) {   
Constructor. Initialize with $\nu$ , $\mu$ and $\sigma$ . The default with one argument is Student $( \nu , 0 , 1 )$ . if (sig $\scriptstyle < = \ 0$ . || nu $< = ~ 0 .$ ) throw("bad sig,nu in Studentdist"); ${ \tt n p } = 0 . 5 * ( \tt n u + 1 . )$ ; fac $=$ gammln(np)-gammln(0.5\*nu);   
}   
Doub p(Doub t) {   
Return probability density function. return exp(-np\*log(1.+SQR((t-mu)/sig)/nu)+fac) /(sqrt(3.14159265358979324\*nu)\*sig);   
}   
Doub cdf(Doub t) {   
Return cumulative distribution function. Doub $\mathrm { ~ p ~ } = \mathrm { ~ 0 ~ }$ .5\*betai(0. $5 * \mathrm { n u }$ , 0.5, nu/(nu+SQR((t-mu)/sig))); if $\bf \Pi _ { t } ^ { \prime } > = \ m u _ { \tau } ^ { \prime }$ ) return 1. - p; else return p;   
}   
Doub invcdf(Doub p) {   
Return inverse cumulative distribution function. if $\mathbf { \Phi } \cdot \mathbf { p } \ < = \ 0$ . $| \mathbf { \Psi } | \mathbf { \Psi } \supset = \mathbf { \Psi } 1 .$ ) throw("bad p in Studentdist"); Doub $\mathrm { ~ \tt ~ { ~ x ~ } ~ } =$ invbetai(2.\*MIN(p,1.-p), 0.5\*nu, 0.5); $\mathrm { ~ x ~ } =$ sig\*sqrt(nu\*(1.-x)/x); return $( \mathrm { p } > = 0 . 5 ? \mathrm { \ m u + x : \ m u - x ) }$ ;   
}   
Doub aa(Doub t) {   
Return the two-tailed cdf $A ( t | \nu )$ . if $\ : \mathrm { ~  ~ \cdot ~ } \ t \in \ : 0 . \ :$ ) throw("bad t in Studentdist"); return 1.-betai(0. ${ 5 * } \mathrm { n u }$ , 0.5, nu/(nu+SQR(t)));   
Doub invaa(Doub p) {   
Return the inverse, namely $t$ such that $p = A ( t | \nu )$ . if $\tt ( p < 0$ . $| \mathrm { ~ l ~ } \mathrm { ~ p ~ } > = \mathrm { ~ 1 ~ } .$ ) throw("bad p in Studentdist"); Doub $_ { \textrm { x } } =$ invbetai(1.-p, $0 . 5 { \ast } \mathrm { n u }$ , 0.5); return sqrt $\left( \mathtt { n u * } \left( 1 \ldots \right) / \mathtt { x } \right)$ ;   
}

# 6.14.4 Logistic Distribution

The logistic distribution is another symmetric, centrally peaked distribution that can be used instead of the normal distribution. Its tails decay exponentially, but still much more slowly than the normal distribution’s “exponent of the square.”

The defining probability density is

$$
p ( y ) = { \frac { e ^ { - y } } { ( 1 + e ^ { - y } ) ^ { 2 } } } = { \frac { e ^ { y } } { ( 1 + e ^ { y } ) ^ { 2 } } } = { \textstyle { \frac { 1 } { 4 } } } \mathrm { s e c h } ^ { 2 } \left( { \frac { 1 } { 2 } } y \right)
$$

The three forms are algebraically equivalent, but, to avoid overflows, it is wise to use the negative and positive exponential forms for positive and negative values of $y$ , respectively.

The variance of the distribution (6.14.12) turns out to be $\pi ^ { 2 } / 3$ . Since it is convenient to have parameters $\mu$ and $\sigma$ with the conventional meanings of mean and standard deviation, equation (6.14.12) is often replaced by the standardized logistic

distribution,

$$
\begin{array} { c c l } { { x \sim \mathrm { L o g i s t i c } ( \mu , \sigma ) , } } & { { \sigma > 0 } } \\ { { p ( x ) = \displaystyle \frac { \pi } { 4 \sqrt { 3 } \sigma } \mathrm { s e c h } ^ { 2 } \left( \displaystyle \frac { \pi } { 2 \sqrt { 3 } } \left[ \displaystyle \frac { x - \mu } { \sigma } \right] \right) } } \end{array}
$$

which implies equivalent forms using the positive and negative exponentials (see code below).

The cdf is given by

$$
\operatorname { c d f } \equiv P ( < x ) \equiv \int _ { - \infty } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = \left[ 1 + \exp \left( - { \frac { \pi } { \sqrt { 3 } } } \left[ { \frac { x - \mu } { \sigma } } \right] \right) \right] ^ { - 1 }
$$

The inverse cdf is given by

$$
x ( P ) = \mu + { \frac { \sqrt { 3 } } { \pi } } \sigma \log \left( { \frac { P } { 1 - P } } \right)
$$

struct Logisticdist {   
Logistic distribution. Doub mu, sig; Logisticdist(Doub mmu $\mathit { \Theta } = \mathit { \Theta } 0 .$ , Doub ssig $\mathit { \Theta } = \mathit { \Theta } 1 \cdot$ ) : mu(mmu), sig(ssig) { Constructor. Initialize with $\mu$ and $\sigma$ . The default with no arguments is Logistic.0; 1/. if (sig $< = ~ 0 .$ ) throw("bad sig in Logisticdist"); } Doub p(Doub x) { Return probability density function. Doub e $=$ exp(-abs(1.81379936423421785\*(x-mu)/sig)); return 1.81379936423421785\*e/(sig\*SQR(1.+e)); } Doub cdf(Doub x) { Return cumulative distribution function. Doub $\qquad \mathtt { \ e } \quad =$ exp(-abs(1.81379936423421785\*(x-mu)/sig)); if $\mathbf { \Omega } ( \mathbf { x } ) = \mathbf { \Omega } \cdot \mathbf { n } \mathbf { u } .$ ) return 1./(1.+e); Because we used abs to control overelse return ${ \mathsf { e } } / ( 1 . + { \mathsf { e } } )$ ; flow, we now have two cases. } Doub invcdf(Doub p) { Return inverse cumulative distribution function. if $( \mathtt { p } \ < = \ 0$ . | $| \mathrm { ~  ~ p ~ } > = 1 .$ ) throw("bad p in Logisticdist"); return mu $+ \ 0$ .551328895421792049\*sig\*log(p/(1.-p)); }   
};

The logistic distribution is cousin to the logit transformation that maps the open unit interval $0 < p < 1$ onto the real line $- \infty < u < \infty$ by the relation

$$
u = \log \left( { \frac { p } { 1 - p } } \right)
$$

Back when a book of tables and a slide rule were a statistician’s working tools, the logit transformation was used to approximate processes on the interval by analytically simpler processes on the real line. A uniform distribution on the interval maps by the logit transformation to a logistic distribution on the real line. With the computer’s ability to calculate distributions on the interval directly (beta distributions, for example), that motivation has vanished.

![](images/5fa30d7264f90c22ec2c86fa58c08ed1c9e7245b6302b56f0ecfac879c033c18.jpg)  
Figure 6.14.2. Examples of common distributions on the half-line $x > 0$ .

Another cousin is the logistic equation,

$$
\frac { d y } { d t } \propto y ( y _ { \mathrm { { m a x } } } - y )
$$

a differential equation describing the growth of some quantity $y$ , starting off as an exponential but reaching, asymptotically, a value $y _ { \mathrm { m a x } }$ . The solution of this equation is identical, up to a scaling, to the cdf of the logistic distribution.

# 6.14.5 Exponential Distribution

With the exponential distribution we now turn to common distribution functions defined on the positive real axis $x \ge 0$ . Figure 6.14.2 shows examples of several of the distributions that we will discuss. The exponential is the simplest of them all. It has a parameter $\beta$ that can control its width (in inverse relationship), but its mode is always at zero:

$$
\begin{array} { c } { x \displaystyle \mathrm { ~ \ w \ w o n e n u a l { } ( \boldsymbol { p } ) , ~ } \quad \mathrm { ~ } \boldsymbol { p } \mathrm { ~ } \mathrm { > ~ } 0 } \\ { p \displaystyle ( \boldsymbol { x } ) = \beta \exp ( - \beta \boldsymbol { x } ) , \qquad \boldsymbol { x } \mathrm { ~ } \mathrm { > ~ } 0 } \\ { \displaystyle \mathrm { ~ } \mathrm { c d f } \equiv P ( < \boldsymbol { x } ) \equiv \int _ { 0 } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = 1 - \exp ( - \beta x ) } \\ { x ( P ) = - \frac { 1 } { \beta } \log ( 1 - P ) } \end{array}
$$

The mean and standard deviation of the exponential distribution are both $1 / \beta$ . The median is $\log ( 2 ) / \beta$ . Reference [1] has more to say about the exponential distribution than you would ever think possible.