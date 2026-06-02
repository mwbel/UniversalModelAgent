# struct Expondist {

Exponential distribution. Doub bet; Expondist(Doub bbet) : bet(bbet) { Constructor. Initialize with $\beta$ . if (bet $< = ~ 0 .$ ) throw("bad bet in Expondist"); } Doub p(Doub x) { Return probability density function. if ( $\mathbf { \Phi } _ { \mathbf { x } } < \mathbf { \Phi } 0 .$ ) throw("bad x in Expondist"); return bet\*exp(-bet\*x); } Doub cdf(Doub x) { Return cumulative distribution function. if $( \mathbb { x } \ < \ 0 .$ ) throw("bad x in Expondist"); return 1.-exp(-bet\*x); Doub invcdf(Doub p) { Return inverse cumulative distribution function. if $\mathtt { ( p < 0 }$ . || $\mathrm {  ~ p ~ } > = \mathrm {  ~ 1 ~ } .$ ) throw("bad p in Expondist"); return -log(1.-p)/bet; }   
};

# 6.14.6 Weibull Distribution

The Weibull distribution generalizes the exponential distribution in a way that is often useful in hazard, survival, or reliability studies. When the lifetime (time to failure) of an item is exponentially distributed, there is a constant probability per unit time that an item will fail, if it has not already done so. That is,

$$
{ \mathrm { h a z a r d } } \equiv { \frac { p ( x ) } { P ( > x ) } } \propto { \mathrm { c o n s t a n t } }
$$

Exponentially lived items don’t age; they just keep rolling the same dice until, one day, their number comes up. In many other situations, however, it is observed that an item’s hazard (as defined above) does change with time, say as a power law,

$$
{ \frac { p ( x ) } { P ( > x ) } } \propto x ^ { \alpha - 1 } , \qquad \alpha > 0
$$

The distribution that results is the Weibull distribution, named for Swedish physicist Waloddi Weibull, who used it as early as 1939. When $\alpha > 1$ , the hazard increases with time, as for components that wear out. When $0 < \alpha < 1$ , the hazard decreases with time, as for components that experience “infant mortality.”

We say that

$$
x \sim \mathrm { { W e i b u l l } } ( \alpha , \beta ) \qquad \mathrm { { i f f } } \qquad y \equiv \left( { \frac { x } { \beta } } \right) ^ { \alpha } \sim \mathrm { { E x p o n e n t i a l } } ( 1 )
$$

The probability density is

$$
p ( x ) = \left( { \frac { \alpha } { \beta } } \right) \left( { \frac { x } { \beta } } \right) ^ { \alpha - 1 } e ^ { - ( x / \beta ) ^ { \alpha } } , \qquad x > 0
$$

The cdf is

$$
{ \mathrm { c d f } } \equiv P ( < x ) \equiv \int _ { 0 } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = 1 - e ^ { - ( x / \beta ) ^ { \alpha } }
$$

The inverse cdf is

$$
x ( P ) = \beta [ - \log ( 1 - P ) ] ^ { 1 / \alpha }
$$

For $0 < \alpha < 1$ , the distribution has an infinite (but integrable) cusp at $x = 0$ and is monotonically decreasing. The exponential distribution is the case of $\alpha = 1$ . When $\alpha > 1$ , the distribution is zero at $x = 0$ and has a single maximum at the value $x = \beta [ ( \alpha - 1 ) / \alpha ] ^ { 1 / \alpha }$ .

The mean and variance are given by

$$
\begin{array} { c l c r } { \mu = \beta \Gamma ( 1 + \alpha ^ { - 1 } ) } \\ { \sigma ^ { 2 } = \beta ^ { 2 } \left\{ \Gamma ( 1 + 2 \alpha ^ { - 1 } ) - \left[ \Gamma ( 1 + \alpha ^ { - 1 } ) \right] ^ { 2 } \right\} } \end{array}
$$

With correct normalization, equation (6.14.22) becomes

$$
{ \mathrm { h a z a r d } } \equiv { \frac { p ( x ) } { P ( > x ) } } = \left( { \frac { \alpha } { \beta } } \right) \left( { \frac { x } { \beta } } \right) ^ { \alpha - 1 }
$$

# 6.14.7 Lognormal Distribution

Many processes that live on the positive $x$ -axis are naturally approximated by normal distributions on the $ { \mathbf { \hat { \theta } } } _ { \mathrm { { l o g } } } ( x )$ -axis,” that is, for $- \infty < \log ( x ) < \infty$ . A simple, but important, example is the multiplicative random walk, which starts at some positive value $x _ { 0 }$ , and then generates new values by a recurrence like

$$
x _ { i + 1 } = \left\{ \begin{array} { l l } { x _ { i } ( 1 + \epsilon ) } & { \mathrm { w i t h } \mathrm { p r o b a b i l i t y } 0 . 5 } \\ { x _ { i } / ( 1 + \epsilon ) } & { \mathrm { w i t h } \mathrm { p r o b a b i l i t y } 0 . 5 } \end{array} \right.
$$

Here $\epsilon$ is some small, fixed, constant.

These considerations motivate the definition

$$
x \sim \operatorname { L o g n o r m a l } ( \mu , \sigma ) \qquad { \mathrm { i f f } } \qquad u \equiv { \frac { \log ( x ) - \mu } { \sigma } } \sim \operatorname { N } ( 0 , 1 )
$$

or the equivalent definition

$$
\begin{array} { c } { { x \sim \mathrm { L o g n o r m a l } ( \mu , \sigma ) , \qquad \sigma > 0 } } \\ { { p ( x ) = \displaystyle \frac { 1 } { \sqrt { 2 \pi } \sigma x } \exp \left( - \frac { 1 } { 2 } \left[ \frac { \log ( x ) - \mu } { \sigma } \right] ^ { 2 } \right) , \qquad x > 0 } } \end{array}
$$

Note the required extra factor of $x ^ { - 1 }$ in front of the exponential: The density that is “normal” is $p ( \log x ) d \log x$ .

While $\mu$ and $\sigma$ are the mean and standard deviation in $\log x$ space, they are not so in $x$ space. Rather,

$$
\begin{array} { r l } & { \mathrm { M e a n } \{ \mathrm { L o g n o r m a l } ( \mu , \sigma ) \} = e ^ { \mu + \frac { 1 } { 2 } \sigma ^ { 2 } } } \\ & { \quad \mathrm { V a r } \{ \mathrm { L o g n o r m a l } ( \mu , \sigma ) \} = e ^ { 2 \mu } e ^ { \sigma ^ { 2 } } ( e ^ { \sigma ^ { 2 } } - 1 ) } \end{array}
$$

The cdf is given by

$$
\operatorname { c d f } \equiv P ( < x ) \equiv \int _ { 0 } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = { \frac { 1 } { 2 } } \mathrm { e r f c } \left( - { \frac { 1 } { \sqrt { 2 } } } \left[ { \frac { \log ( x ) - \mu } { \sigma } } \right] \right)
$$

The inverse to the cdf involves the inverse complementary error function,

$$
x ( P ) = \exp [ \mu - \sqrt { 2 } \sigma \mathrm { e r f c } ^ { - 1 } ( 2 P ) ]
$$

# struct Lognormaldist : Erf {

# erf.h

Lognormal distribution, derived from the error function Erf.

Doub mu, sig; Lognormaldist(Doub mmu $\qquad = \ 0 .$ , Doub ssig $\begin{array} { r l } { \mathbf { \Psi } } & { { } = \mathbf { \Psi } \perp \mathbf { \Psi } . } \end{array}$ .) : mu(mmu), sig(ssig) { if (sig $< = ~ 0 .$ ) throw("bad sig in Lognormaldist"); } Doub p(Doub x) { Return probability density function. if ( $\begin{array} { r } { \mathrm { ~  ~ x ~ } < 0 . } \end{array}$ ) throw("bad x in Lognormaldist"); if ( $\mathbf { x } \ = = \ 0 .$ ) return 0.; return (0.398942280401432678/(sig\*x))\*exp(-0.5\*SQR((log(x)-mu)/sig)); } Doub cdf(Doub x) { Return cumulative distribution function. if ( $\mathbf { \Phi } _ { \mathbf { x } } < \mathbf { \Phi } 0 .$ ) throw("bad x in Lognormaldist"); if ( $\mathbf { x } \ = = \ 0 .$ ) return 0.; return 0.5\*erfc(-0.707106781186547524\*(log(x)-mu)/sig); } Doub invcdf(Doub p) { Return inverse cumulative distribution function. if $_ { \mathrm { ~ \tiny ~ Q ~ } } < = \mathrm { ~ \tiny ~ 0 ~ }$ . $| \mathbf { \Psi } | \mathbf { \Psi } \supset = \mathbf { \Psi } 1 .$ ) throw("bad p in Lognormaldist"); return exp(-1.41421356237309505\*sig\*inverfc(2.\*p)+mu); } };

Multiplicative random walks like (6.14.29) and lognormal distributions are key ingredients in the economic theory of efficient markets, leading to (among many other results) the celebrated Black-Scholes formula for the probability distribution of the price of an investment after some elapsed time $\tau$ . A key piece of the Black-Scholes derivation is implicit in equation (6.14.32): If an investment’s average return is zero (which may be true in the limit of zero risk), then its price cannot simply be a widening lognormal distribution with fixed $\mu$ and increasing $\sigma$ , for its expected value would then diverge to infinity! The actual Black-Scholes formula thus defines both how $\sigma$ increases with time (basically as $\tau ^ { 1 / 2 }$ ) and how $\mu$ correspondingly decreases with time, so as to keep the overall mean under control. A simplified version of the Black-Scholes formula can be written as

$$
\begin{array} { r } { S ( \tau ) \sim S ( 0 ) \times \mathrm { L o g n o r m a l } \left( r \tau - \frac { 1 } { 2 } \sigma ^ { 2 } \tau , \sigma \sqrt { \tau } \right) } \end{array}
$$

where $S ( \tau )$ is the price of a stock at time $\tau , r$ is its expected (annualized) rate of return, and $\sigma$ is now redefined to be the stock’s (annualized) volatility. The definition of volatility is that, for small values of $\tau$ , the fractional variance of the stock’s price is $\sigma ^ { 2 } \tau$ . You can check that (6.14.35) has the desired expectation value $E [ S ( \tau ) ] =$ $S ( 0 )$ , for all $\tau$ , if $r = 0$ . A good reference is [3].

# 6.14.8 Chi-Square Distribution

The chi-square (or $\chi ^ { 2 }$ ) distribution has a single parameter $\nu > 0$ that controls both the location and width of its peak. In most applications $\nu$ is an integer and is referred to as the number of degrees of freedom (see $\ S 1 4 . 3 )$ .

The defining probability density is

$$
\begin{array} { c c } { { \chi ^ { 2 } \sim \mathrm { C h i s q u a r e } ( \nu ) , } } & { { \nu > 0 } } \\ { { p ( \chi ^ { 2 } ) d \chi ^ { 2 } = \frac { 1 } { 2 ^ { \frac { 1 } { 2 } \nu } \Gamma ( { \frac { 1 } { 2 } } \nu ) } ( \chi ^ { 2 } ) ^ { \frac { 1 } { 2 } \nu - 1 } \exp \left( - { \frac { 1 } { 2 } } \chi ^ { 2 } \right) d \chi ^ { 2 } , } } & { { \chi ^ { 2 } > 0 } } \end{array}
$$

where we have written the differentials $d \chi ^ { 2 }$ merely to emphasize that $\chi ^ { 2 }$ , not $\chi$ , is to be viewed as the independent variable.

The mean and variance are given by

$$
\begin{array} { r } { \mathrm { M e a n } \{ \mathrm { C h i s q u a r e } ( \nu ) \} = \nu } \\ { \mathrm { V a r } \{ \mathrm { C h i s q u a r e } ( \nu ) \} = 2 \nu } \end{array}
$$

When $\nu \geq 2$ there is a single mode at $\chi ^ { 2 } = \nu - 2$ .

The chi-square distribution is actually just a special case of the gamma distribution, below, so its cdf is given by an incomplete gamma function $P ( \boldsymbol { a } , \boldsymbol { x } )$ ,

$$
{ \mathrm { c d f } } \equiv P ( < \chi ^ { 2 } ) \equiv P ( \chi ^ { 2 } | \nu ) \equiv \int _ { 0 } ^ { \chi ^ { 2 } } p ( \chi ^ { 2 \prime } ) d \chi ^ { 2 \prime } = P \left( { \frac { \nu } { 2 } } , { \frac { \chi ^ { 2 } } { 2 } } \right)
$$

One frequently also sees the complement of the cdf, which can be calculated either from the incomplete gamma function $P ( \boldsymbol { a } , \boldsymbol { x } )$ , or from its complement $Q ( a , x )$ (often more accurate if $P$ is very close to 1):

$$
\mathcal { Q } ( \chi ^ { 2 } | \nu ) \equiv 1 - P ( \chi ^ { 2 } | n ) = 1 - P \left( \frac { \nu } { 2 } , \frac { \chi ^ { 2 } } { 2 } \right) \equiv Q \left( \frac { \nu } { 2 } , \frac { \chi ^ { 2 } } { 2 } \right)
$$

The inverse cdf is given in terms of the function that is the inverse of $P ( \boldsymbol { a } , \boldsymbol { x } )$ on its second argument, which we here denote $P ^ { - 1 } ( a , p )$ :

$$
x ( P ) = 2 P ^ { - 1 } \left( { \frac { \nu } { 2 } } , P \right)
$$

# struct Chisqdist : Gamma {

$\chi ^ { 2 }$ distribution, derived from the gamma function Gamma.

Doub nu,fac;   
Chisqdist(Doub nnu) : nu(nnu) {   
Constructor. Initialize with $\nu$ . if $\mathrm {  ~ \Omega ~ } ^ { \prime } \mathrm {  ~ \ n u ~ } < = \mathrm {  ~ \Omega ~ } 0 .$ ) throw("bad nu in Chisqdist"); fac $\mathit { \Theta } = \mathit { \Theta } 0$ .693147180559945309\*(0.5\*nu)+gammln(0.5\*nu);   
}   
Doub p(Doub x2) {   
Return probability density function. if $( \mathbf { x } 2 \ < = \ 0 .$ ) throw("bad x2 in Chisqdist"); return exp(-0.5\*(x2-(nu-2.)\*log(x2))-fac);   
}   
Doub cdf(Doub x2) {

Return cumulative distribution function. if $\left( \mathbf { x } 2 \ < \ 0 . \right.$ ) throw("bad x2 in Chisqdist"); return gammp $( 0 . 5 * \mathrm { n u } , 0 . 5 * \mathrm { x } 2 )$ ; Doub invcdf(Doub p) { Return inverse cumulative distribution function. if ${ \mathrm { ( p ~ < ~ } } 0$ . $| \mathrm { ~ \bf ~ \underline { ~ } { ~ \underline { ~ } { ~ p ~ } ~ } ~ } > = \mathrm { ~ \bf ~ 1 ~ } .$ ) throw("bad p in Chisqdist"); return 2.\*invgammp(p,0.5\*nu); } };

# 6.14.9 Gamma Distribution

The gamma distribution is defined by

$$
\begin{array} { r l r l } { x \sim \mathrm { G a m m a } ( \alpha , \beta ) , } & { } & { \alpha > 0 , \beta > 0 } \\ { p ( x ) = \displaystyle \frac { \beta ^ { \alpha } } { \Gamma ( \alpha ) } x ^ { \alpha - 1 } e ^ { - \beta x } , } & { } & { x > 0 } \end{array}
$$

The exponential distribution is the special case with $\alpha = 1$ . The chi-square distribution is the special case with $\alpha = \nu / 2$ and $\beta = 1 / 2$ .

The mean and variance are given by,

$$
\begin{array} { r } { \mathrm { M e a n } \{ \mathrm { G a m m a } ( \alpha , \beta ) \} = \alpha / \beta } \\ { \mathrm { V a r } \{ \mathrm { G a m m a } ( \alpha , \beta ) \} = \alpha / \beta ^ { 2 } } \end{array}
$$

When $\alpha \geq 1$ there is a single mode at $x = ( \alpha - 1 ) / \beta$ .

Evidently, the cdf is the incomplete gamma function

$$
{ \mathrm { c d f } } \equiv P ( < x ) \equiv \int _ { 0 } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = P \left( \alpha , \beta x \right)
$$

while the inverse cdf is given in terms of the inverse of $P ( \boldsymbol { a } , \boldsymbol { x } )$ on its second argument by

$$
x ( P ) = \frac { 1 } { \beta } P ^ { - 1 } \left( \alpha , P \right)
$$

# struct Gammadist : Gamma {

amma distribution, derived from the gamma function Gamma.

Doub alph, bet, fac;   
Gammadist(Doub aalph, Doub bbet $\qquad = \ 1 \ .$ ) : alph(aalph), bet(bbet) {   
Constructor. Initialize with $\pmb { \alpha }$ and $\beta$ . if (alph $\scriptstyle < = \ 0$ . || bet $< = ~ 0 .$ ) throw("bad alph,bet in Gammadist"); fac $=$ alph\*log(bet)-gammln(alph);   
}   
Doub p(Doub x) {   
Return probability density function. if ( $\mathbf { \bar { x } } \ < = \ 0 .$ ) throw("bad x in Gammadist"); return exp(-bet\*x+(alph-1.)\*log(x)+fac);   
}   
Doub cdf(Doub x) {   
Return cumulative distribution function. if $\mathbf { \Phi } _ { \mathbf { x } } < \mathbf { \Phi } 0 .$ ) throw("bad x in Gammadist"); return gammp(alph,bet\*x);   
}

Doub invcdf(Doub p) { Return inverse cumulative distribution function. if $\mathrm { ~ ( ~ p ~ < ~ 0 ~ }$ . | $| \texttt { p } > = \texttt { 1 } .$ ) throw("bad p in Gammadist"); return invgammp(p,alph)/bet; } };

# 6.14.10 F-Distribution

The $F$ -distribution is parameterized by two positive values $\nu _ { 1 }$ and $\nu _ { 2 }$ , usually (but not always) integers.

The defining probability density is

$$
\begin{array} { c } { { F \sim \mathrm { F } ( \nu _ { 1 } , \nu _ { 2 } ) , \qquad \nu _ { 1 } > 0 , \nu _ { 2 } > 0 } } \\ { { \qquad \nu _ { 1 } ^ { \frac 1 2 \nu _ { 1 } } \nu _ { 2 } ^ { \frac 1 2 \nu _ { 2 } } } } \\ { { p ( F ) = \displaystyle \frac { \nu _ { 1 } ^ { \frac 1 2 \nu _ { 1 } } \nu _ { 2 } ^ { \frac 1 2 } } { B ( \frac 1 2 \nu _ { 1 } , \frac 1 2 \nu _ { 2 } ) } \frac { F ^ { \frac 1 2 \nu _ { 1 } - 1 } } { ( \nu _ { 2 } + \nu _ { 1 } F ) ^ { ( \nu _ { 1 } + \nu _ { 2 } ) / 2 } } , \qquad F > 0 } } \end{array}
$$

where $B ( a , b )$ denotes the beta function. The mean and variance are given by

$$
\begin{array} { r l r } & { \mathrm { M e a n } \{ \mathrm { F } ( \nu _ { 1 } , \nu _ { 2 } ) \} = \frac { \nu _ { 2 } } { \nu _ { 2 } - 2 } , } & { \quad \nu _ { 2 } > 2 } \\ & { \mathrm { V a r } \{ \mathrm { F } ( \nu _ { 1 } , \nu _ { 2 } ) \} = \frac { 2 \nu _ { 2 } ^ { 2 } ( \nu _ { 1 } + \nu _ { 2 } - 2 ) } { \nu _ { 1 } ( \nu _ { 2 } - 2 ) ^ { 2 } ( \nu _ { 2 } - 4 ) } , } & { \quad \nu _ { 2 } > 4 } \end{array}
$$

When $\nu _ { 1 } \geq 2$ there is a single mode at

$$
F = \frac { \nu _ { 2 } ( \nu _ { 1 } - 2 ) } { \nu _ { 1 } ( \nu _ { 2 } + 2 ) }
$$

For fixed $\nu _ { 1 }$ , if $\nu _ { 2 } \to \infty$ , the $F$ -distribution becomes a chi-square distribution, namely

$$
\operatorname* { l i m } _ { \nu _ { 2 } \to \infty } \mathrm { F } ( \nu _ { 1 } , \nu _ { 2 } ) \cong \frac { 1 } { \nu _ { 1 } } { \mathrm { C h i s q u a r e } } ( \nu _ { 1 } )
$$

where $\ Y q$ means “are identical distributions.”

The $F$ -distribution’s cdf is given in terms of the incomplete beta function $I _ { x } ( a , b )$ by

$$
{ \mathrm { c d f } } \equiv P ( < x ) \equiv \int _ { 0 } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = I _ { \nu _ { 1 } F / ( \nu _ { 2 } + \nu _ { 1 } F ) } \left( { \frac { 1 } { 2 } } \nu _ { 1 } , { \frac { 1 } { 2 } } \nu _ { 2 } \right)
$$

while the inverse cdf is given in terms of the inverse of $I _ { x } ( a , b )$ on its subscript argument by

$$
\begin{array} { c } { { u \equiv I _ { p } ^ { - 1 } \left( \frac { 1 } { 2 } \nu _ { 1 } , \frac { 1 } { 2 } \nu _ { 2 } \right) } } \\ { { x ( P ) = \displaystyle \frac { \nu _ { 2 } u } { \nu _ { 1 } ( 1 - u ) } } } \end{array}
$$

A frequent use of the $F$ -distribution is to test whether two observed samples have the same variance.

struct Fdist : Beta {   
$F$ distribution, derived from the beta function Beta. Doub nu1,nu2; Doub fac; Fdist(Doub nnu1, Doub nnu2) : nu1(nnu1), nu2(nnu2) { Constructor. Initialize with $\nu _ { 1 }$ and $\nu _ { 2 }$ . if (nu1 $\scriptstyle < = \ 0$ . || nu2 $< = ~ 0 .$ ) throw("bad nu1,nu2 in Fdist"); fac = 0.5\*(nu1\*log(nu1)+nu2\*log(nu2))+gammln(0.5\*(nu1+nu2)) -gammln(0.5\*nu1)-gammln(0.5\*nu2); } Doub p(Doub f) { Return probability density function. if ( ${ \mathrm { ~  ~ \cdot ~ } } { \mathrm { ~  ~ \cdot ~ } } < = { \mathrm { ~  ~ 0 ~ } } .$ ) throw("bad f in Fdist"); return exp((0.5\*nu1-1.)\*log(f)-0.5\*(nu1+nu2)\*log(nu2+nu1\*f)+fac); } Doub cdf(Doub f) { Return cumulative distribution function. if ( $. . . < . . .$ ) throw("bad f in Fdist"); return betai(0. $^ { 5 \ast }$ nu1,0.5\*nu2,nu1\*f/(nu2+nu1\*f)); } Doub invcdf(Doub p) { Return inverse cumulative distribution function. if $_ { \mathrm { ~ \tiny ~ Q ~ } } < = \mathrm { ~ \tiny ~ 0 ~ }$ . $| \mathbf { \Psi } | \mathbf { \Psi } \supset = \mathbf { \Psi } 1 .$ ) throw("bad p in Fdist"); Doub $\mathrm { ~ x ~ } =$ invbetai(p,0.5\*nu1,0.5\*nu2); return nu2\*x/(nu1\*(1.-x)); }   
};

# 6.14.11 Beta Distribution

The beta distribution is defined on the unit interval $0 < x < 1$ by

$$
\begin{array} { c } { { x \sim \mathrm { B e t a } ( \alpha , \beta ) , \qquad \alpha > 0 , \beta > 0 } } \\ { { p ( x ) = \displaystyle \frac { 1 } { B ( \alpha , \beta ) } x ^ { \alpha - 1 } ( 1 - x ) ^ { \beta - 1 } , \qquad 0 < x < 1 } } \end{array}
$$

The mean and variance are given by

$$
\begin{array} { l } { { \displaystyle \mathrm { M e a n } \{ \mathrm { B e t a } ( \alpha , \beta ) \} = \frac { \alpha } { \alpha + \beta } } } \\ { { \displaystyle \mathrm { V a r } \{ \mathrm { B e t a } ( \alpha , \beta ) \} = \frac { \alpha \beta } { ( \alpha + \beta ) ^ { 2 } ( \alpha + \beta + 1 ) } } } \end{array}
$$

When $\alpha > 1$ and $\beta > 1$ , there is a single mode at $( \alpha - 1 ) / ( \alpha + \beta - 2 )$ . When $\alpha < 1$ and $\beta < 1$ , the distribution function is “U-shaped” with a minimum at this same value. In other cases there is neither a maximum nor a minimum.

In the limit that $\beta$ becomes large as $\alpha$ is held fixed, all the action in the beta distribution shifts toward $x = 0$ , and the density function takes the shape of a gamma distribution. More precisely,

$$
\operatorname* { l i m } _ { \beta \to \infty } \beta \operatorname { B e t a } ( \alpha , \beta ) \cong \operatorname { G a m m a } ( \alpha , 1 )
$$

The cdf is the incomplete beta function

$$
\mathsf { c d f } \equiv P ( < x ) \equiv \int _ { 0 } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = I _ { x } \left( \alpha , \beta \right)
$$

while the inverse cdf is given in terms of the inverse of $I _ { x } ( \alpha , \beta )$ on its subscript argument by

$$
x ( P ) = I _ { p } ^ { - 1 } ( \alpha , \beta )
$$

# struct Betadist : Beta {

Beta distribution, derived from the beta function Beta.

Doub alph, bet, fac; Betadist(Doub aalph, Doub bbet) : alph(aalph), bet(bbet) { Constructor. Initialize with $\pmb { \alpha }$ and $\beta$ . if (alph $< = ~ 0$ . || bet $< = ~ 0 .$ ) throw("bad alph,bet in Betadist"); fac $=$ gammln(alph $\cdot ^ { + }$ bet)-gammln(alph)-gammln(bet); } Doub p(Doub x) { Return probability density function. if $\mathrm { ~  ~ \omega ~ } < = \mathrm { ~  ~ 0 ~ }$ . $| \mathbf { \Psi } | \mathbf { \Psi } \ \mathbf { x } \ > = \ 1 .$ ) throw("bad x in Betadist"); return exp((alph-1.)\*log(x)+(bet-1.)\*log(1.-x)+fac); } Doub cdf(Doub x) { Return cumulative distribution function. if $\mathit { \Omega } _ { \mathrm { ~ x ~ } } < \mathit { \Omega } 0$ . || $\begin{array} { r } { \mathrm { ~ z ~ } > ~ 1 . } \end{array}$ ) throw("bad x in Betadist"); return betai(alph,bet,x); } Doub invcdf(Doub p) { Return inverse cumulative distribution function. if $\mathrm { ~ ( ~ p ~ < ~ 0 ~ }$ . $| \mathsf { I } \ \mathsf { p } > \ \mathsf { 1 } .$ ) throw("bad p in Betadist"); return invbetai(p,alph,bet); } };

# 6.14.12 Kolmogorov-Smirnov Distribution

The Kolmogorov-Smirnov or $K S$ distribution, defined for positive $Z$ , is key to an important statistical test that is discussed in $\ S 1 4 . 3$ . Its probability density function does not directly enter into the test and is virtually never even written down. What one typically needs to compute is the cdf, denoted $P _ { K S } ( z )$ , or its complement, $Q _ { K S } ( z ) \equiv 1 - P _ { K S } ( z )$ .

The cdf $P _ { K S } ( z )$ is defined by the series

$$
P _ { K S } ( z ) = 1 - 2 \sum _ { j = 1 } ^ { \infty } ( - 1 ) ^ { j - 1 } \exp ( - 2 j ^ { 2 } z ^ { 2 } )
$$

or by the equivalent series (nonobviously so!)

$$
P _ { K S } ( z ) = \frac { \sqrt { 2 \pi } } { z } \sum _ { j = 1 } ^ { \infty } \exp { \left( - \frac { ( 2 j - 1 ) ^ { 2 } \pi ^ { 2 } } { 8 z ^ { 2 } } \right) }
$$

Limiting values are what you’d expect for cdf’s named “ $P$ ” and “ $Q$ ”:

$$
\begin{array} { r l } { P _ { K S } ( 0 ) = 0 \qquad } & { { } P _ { K S } ( \infty ) = 1 } \\ { Q _ { K S } ( 0 ) = 1 \qquad } & { { } Q _ { K S } ( \infty ) = 0 } \end{array}
$$

Both of the series (6.14.56) and (6.14.57) are convergent for all $z > 0$ . Moreover, for any $Z$ , one or the other series converges extremely rapidly, requiring no more than three terms to get to IEEE double precision fractional accuracy. A good place to switch from one series to the other is at $z \approx 1 . 1 8$ . This renders the KS functions computable by a single exponential and a small number of arithmetic operations (see code below).

Getting the inverse functions $P _ { K S } ^ { - 1 } ( P )$ and $Q _ { K S } ^ { - 1 } ( \boldsymbol { Q } )$ , which return a value of $Z$ from a $P$ or $Q$ value, is a little trickier. For $Q \lesssim 0 . 3$ (that is, $P \gtrsim 0 . 7 $ ), an iteration based on (6.14.56) works nicely:

$$
\begin{array} { c } { { x _ { 0 } \equiv 0 } } \\ { { x _ { i + 1 } = \frac 1 2 Q + x _ { i } ^ { 4 } - x _ { i } ^ { 9 } + x _ { i } ^ { 1 6 } - x _ { i } ^ { 2 5 } + \cdots } } \\ { { z ( Q ) = \sqrt { - \frac 1 2 \log ( x _ { \infty } ) } } } \end{array}
$$

For $x \lesssim 0 . 0 6$ you only need the first two powers of $x _ { i }$

For larger values of $Q$ , that is, $P \ \lesssim \ 0 . 7$ , the number of powers of $x$ required quickly becomes excessive. A useful approach is to write (6.14.57) as

$$
\begin{array} { l } { { y \log ( y ) = - \displaystyle \frac { \pi P ^ { 2 } } { 8 } \left( 1 + y ^ { 4 } + y ^ { 1 2 } + \cdots + y ^ { 2 j ( j - 1 ) } + \cdots \right) ^ { - 1 } } } \\ { { z ( P ) = \displaystyle \frac { \pi / 2 } { \sqrt { - \log ( y ) } } } } \end{array}
$$

If we can get a good enough initial guess for $y$ , we can solve the first equation in (6.14.60) by a variant of Halley’s method: Use values of $y$ from the previous iteration on the right-hand side of (6.14.60), and use Halley only for the $y \log ( y )$ piece, so that the first and second derivatives are analytically simple functions.

A good initial guess is obtained by using the inverse function to $y \log ( y )$ (the function invxlogx in $\ S 6 . 1 1 \ r ,$ ) with the argument $- \pi P ^ { 2 } / 8$ . The number of iterations within the invxlogx function and the Halley loop is never more than half a dozen in each, often less. Code for the KS functions and their inverses follows.

struct KSdist {   
Kolmogorov-Smirnov cumulative distribution functions and their inverses. Doub pks(Doub z) { Return cumulative distribution function. if $( z \ < \ 0 .$ ) throw("bad z in KSdist"); if $\ _ { Z } \ = = \ 0 .$ ) return 0.; if $\mathit { \Theta } _ { \Xi } < 1 . 1 8 $ ) { Doub y $=$ exp(-1.23370055013616983/SQR(z)); return 2.25675833419102515\*sqrt(-log(y)) \*(y + pow(y,9) + pow(y,25) $^ +$ pow(y,49)); } else { Doub x $=$ exp(-2.\*SQR(z)); return 1. - 2.\*(x - pow(x,4) $^ +$ pow(x,9)); } } Doub qks(Doub z) { Return complementary cumulative distribution function. if $\ . \ z \ < \ 0 .$ ) throw("bad z in KSdist"); if $\ , z \ = \ 0 .$ ) return 1.; if ( $z \ < \ 1 . 1 8 ,$ ) return 1.-pks(z); Doub $\mathbf { x } \ = \ \exp ( - 2 . { * } \mathrm { S } \mathsf { q } \mathrm { R } ( \mathbf { z } ) )$ ; return ${ 2 . * ( { \bf x } \mathrm { ~ - ~ } \mathrm { p o w } ( { \bf x } , 4 ) \mathrm { ~ + ~ } \mathrm { p o w } ( { \bf x } , 9 ) ) } ;$ Doub invqks(Doub q) {

Return inverse of the complementary cumulative distribution function.

Doub y,logy,yp,x,xp,f,ff,u,t; if (q $\scriptstyle < = 0$ . $| \textsf { l q } > \textsf { 1 } .$ ) throw("bad q in KSdist"); if $( { \mathsf { q } } \ ) = = \ { \mathsf { 1 } } .$ ) return 0.; if $( \mathsf { q } > 0 . 3 )$ ) { $\texttt { f } = \texttt { - } 0$ .392699081698724155\*SQR(1.-q); $\mathrm { ~ y ~ } =$ invxlogx(f); Initial guess. do { $\mathrm { \ y p ~ = ~ y _ { \mathrm { ~ } } }$ ; logy $=$ log(y); ff $=$ f/SQR(1.+ pow(y,4)+ pow(y,12)); $u \ =$ (y\*logy-ff)/(1.+logy); Newton’s method correction. $\mathrm { ~ y ~ } = \mathrm { ~ y ~ } -$ ( $t = u$ /MAX(0.5,1.-0.5\*u/(y\*(1.+logy)))); Halley. } while (abs(t/y)>1.e-15); return 1.57079632679489662/sqrt(-log(y)); } else { $\mathrm { ~ x ~ } = \mathrm { ~ 0 ~ } . 0 3$ ; do { Iteration (6.14.59). $\mathbf { x p } \ = \ \mathbf { x } _ { \mathrm { ~ \scriptsize ~ . ~ } }$ ; x = 0.5\*q+pow(x,4)-pow(x,9); if $\mathrm { ~ ( ~ x ~ } > \ 0 . 0 6 )$ x $+ =$ pow(x,16)-pow(x,25); } while (abs((xp-x)/x)>1.e-15); return sqrt(-0.5\*log(x)); } } Doub invpks(Doub p) {return invqks(1.-p);} Return inverse of the cumulative distribution function.

# 6.14.13 Poisson Distribution

The eponymous Poisson distribution was derived by Poisson in 1837. It applies to a process where discrete, uncorrelated events occur at some mean rate per unit time. If, for a given period, $\lambda$ is the mean expected number of events, then the probability distribution of seeing exactly $k$ events, $k \geq 0$ , can be written as

$$
\begin{array} { c c } { { k \sim \mathrm { P o i s s o n } ( \lambda ) , } } & { { \lambda > 0 } } \\ { { p ( k ) = \displaystyle \frac { 1 } { k ! } \lambda ^ { k } e ^ { - \lambda } , } } & { { \ k = 0 , 1 , . . . } } \end{array}
$$

Evidently $\begin{array} { r } { \sum _ { k } p ( k ) = 1 } \end{array}$ , since the $k$ -dependent factors in (6.14.61) are just the series expansion of $e ^ { \lambda }$ .

The mean and variance of Poisson $( \lambda )$ are both $\lambda$ . There is a single mode at $k = \lfloor \lambda \rfloor$ , that is, at $\lambda$ rounded down to an integer.

The Poisson distribution’s cdf is an incomplete gamma function $Q ( a , x )$ ,

$$
P _ { \lambda } ( < k ) = Q ( k , \lambda )
$$

Since $k$ is discrete, $P _ { \lambda } ( < k )$ is of course different from $P _ { \lambda } ( \leq k )$ , the latter being given by

$$
P _ { \lambda } ( \leq k ) = Q ( k + 1 , \lambda )
$$

Some particular values are

$$
P _ { \lambda } ( < 0 ) = 0 \qquad P _ { \lambda } ( < 1 ) = e ^ { - \lambda } \qquad P _ { \lambda } ( < \infty ) = 1
$$

Some other relations involving the incomplete gamma functions $Q ( \boldsymbol { a } , \boldsymbol { x } )$ and $P ( \boldsymbol { a } , \boldsymbol { x } )$ are

$$
\begin{array} { r l } & { P _ { \lambda } ( \geq k ) = P ( k , \lambda ) = 1 - Q ( k , \lambda ) } \\ & { P _ { \lambda } ( > k ) = P ( k + 1 , \lambda ) = 1 - Q ( k + 1 , \lambda ) } \end{array}
$$

Because of the discreteness in $k$ , the inverse of the cdf must be defined with some care: Given a value P, we define $k _ { \lambda } ( P )$ as the integer such that

$$
P _ { \lambda } ( < k ) \le P < P _ { \lambda } ( \le k )
$$

In the interest of conciseness, the code below cheats a little bit and allows the righthand $<$ to be $\leq$ . If you may be supplying $P$ ’s that are exact $P _ { \lambda } ( < k )$ ’s, then you will need to check both $k _ { \lambda } ( P )$ as returned, and $k _ { \lambda } ( P ) + 1$ . (This will essentially never happen for “round” $P$ ’s like 0.95, 0.99, etc.)

# struct Poissondist : Gamma {

oisson distribution, derived from the gamma function Gamma. Doub lam; Poissondist(Doub llam) : lam(llam) { Constructor. Initialize with . if (lam $< = ~ 0 .$ ) throw("bad lam in Poissondist"); } Doub $\mathfrak { p } ( \mathtt { I n t } \ \mathtt { n } )$ { Return probability density function. if $\smash { \left( \mathrm { ~ n ~ } < \mathrm { ~ } 0 \right) }$ ) throw("bad n in Poissondist"); return exp(-lam + n\*log(lam) - gammln(n+1.)); } Doub cdf(Int n) { Return cumulative distribution function. if $\mathrm { ~ ( ~ n ~ < ~ } 0 \mathrm { ) ~ }$ ) throw("bad n in Poissondist"); if ( $\mathbf { \bar { n } _ { \theta } } = \mathbf { \bar { \Phi } } 0$ ) return 0.; return gammq((Doub)n,lam); }

# Int invcdf(Doub p) {

# Given argument $P$ , return integer $_ n$ such that $P ( < n ) \leq P \leq P ( < n + 1 )$

Int n,nl,nu, $\mathtt { i n c } = 1$ ; if (p $< = ~ 0$ . | $| \mathrm { ~  ~ p ~ } > = 1 .$ ) throw("bad p in Poissondist"); if (p $<$ exp(-lam)) return 0; $\mathrm { ~ n ~ } =$ (Int)MAX(sqrt(lam),5.); Starting guess near peak of density. if $( \mathtt { p } <$ cdf(n)) { Expand interval until we bracket. do { $\mathrm { ~ n ~ } =$ MAX(n-inc,0); inc $\ast = ~ 2$ ; } while (p < cdf(n)); nl $= \mathrm { ~ n ~ }$ ; nu $\mathbf { \Sigma } = \texttt { n } +$ inc/2; } else { do { n $+ =$ inc; inc $\ast = ~ 2$ ; } while (p > cdf(n)); nu $= \mathrm { ~ n ~ }$ ; $\mathtt { n 1 } = \mathtt { n }$ - inc/2; } while (nu-nl>1) { Now contract the interval by bisection. $\mathrm { ~ n ~ } = \mathrm { ~ \left( n 1 + n u \right) / 2 ~ }$ ; if $. { \mathrm { ~ p ~ } } <$ cdf $\mathbf { \Psi } ( \mathbf { n } )$ ) $\mathrm { \Omega } \mathfrak { n } \mathfrak { u } \ = \mathrm { \Omega } \mathfrak { n }$ ; else nl $\mathbf { \Phi } = \mathbf { \Phi } _ { \mathbf { n } }$ ; } return nl; }

# 6.14.14 Binomial Distribution

Like the Poisson distribution, the binomial distribution is a discrete distribution over $k \geq 0$ . It has two parameters, $n \geq 1$ , the “sample size” or maximum value for which $k$ can be nonzero; and $p$ , the “event probability” (not to be confused with $p ( k )$ , the probability of a particular $\mathrm { k }$ ). We write

$$
\begin{array} { r l } { k \sim \mathrm { B i n o m i a l } ( n , p ) , \ } & { { } n \geq 1 , \ 0 < p < 1 } \\ { p ( k ) = { \binom { n } { k } } p ^ { k } ( 1 - p ) ^ { n - k } , \ } & { { } k = 0 , 1 , \ldots , n } \end{array}
$$

where $\binom { n } { k }$ is, of course, the binomial coefficient.

The mean and variance are given by

$$
\begin{array} { l } { { \mathrm { M e a n } \{ { \mathrm { B i n o m i a l } } ( n , p ) \} = n p } \atop { \mathrm { V a r } \{ { \mathrm { B i n o m i a l } } ( n , p ) \} = n p ( 1 - p ) } } \end{array}
$$

There is a single mode at the value $k$ that satisfies

$$
( n + 1 ) p - 1 < k \leq ( n + 1 ) p
$$

The distribution is symmetrical iff $\begin{array} { r } { p = \frac { 1 } { 2 } } \end{array}$ . Otherwise it has positive skewness for $\begin{array} { r } { p < { \frac { 1 } { 2 } } } \end{array}$ and negative for $\begin{array} { r } { p > \frac { 1 } { 2 } } \end{array}$ . Many additional properties are described in [2].

The Poisson distribution is obtained from the binomial distribution in the limit $n  \infty , p  0$ with the $n p$ remaining finite. More precisely,

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname { B i n o m i a l } ( n , \lambda / n ) \cong \operatorname { P o i s s o n } ( \lambda )
$$

The binomial distribution’s cdf can be computed from the incomplete beta function $I _ { x } ( a , b )$ ,

$$
P ( < k ) = 1 - I _ { p } ( k , n - k + 1 )
$$

so we also have (analogously to the Poisson distribution)

$$
\begin{array} { l } { P ( \leq k ) = 1 - I _ { p } ( k + 1 , n - k ) } \\ { P ( > k ) = I _ { p } ( k + 1 , n - k ) } \\ { P ( \geq k ) = I _ { p } ( k , n - k + 1 ) } \end{array}
$$

Some particular values are

$$
P ( < 0 ) = 0 \qquad P ( < [ n + 1 ] ) = 1
$$

The inverse cdf is defined exactly as for the Poisson distribution, above, and with the same small warning about the code.

# struct Binomialdist : Beta {

Binomial distribution, derived from the beta function Beta.

Int n;   
Doub pe, fac;   
Binomialdist(Int nn, Doub ppe) : n(nn), pe(ppe) {   
Constructor. Initialize with $_ { n }$ (sample size) and $p$ (event probability). if $( \mathtt { n ~ < = ~ 0 ~ } \mid \mid \mathtt { p e ~ < = ~ 0 ~ . ~ } \mid \mid \mathtt { p e ~ > = ~ 1 . ~ } )$ throw("bad args in Binomialdist");

fac $=$ gammln(n+1.); 1 Doub p(Int k) { Return probability density function. if (k < 0) throw("bad k in Binomialdist"); if $\mathrm { ~ ( ~ k ~ > ~ n ~ ) ~ }$ ) return 0.; return exp(k\*log(pe)+(n-k)\*log(1.-pe) +fac-gammln(k+1.)-gammln(n-k+1.)); } Doub cdf(Int k) { Return cumulative distribution function. if (k < 0) throw("bad k in Binomialdist"); if $\mathbf { \Phi } _ { \mathbf { k } } \ \mathbf { \Phi } = \mathbf { \Phi } _ { 0 }$ ) return 0.; if $\mathrm { ~ ( ~ k ~ > ~ n ~ ) ~ }$ ) return 1.; return 1. - betai((Doub)k,n-k+1.,pe); } Int invcdf(Doub p) { Given argument $P$ , return integer $_ n$ such that $P ( < n ) \leq P \leq P ( < n + 1 )$ . Int k,kl,ku, $\mathtt { i n c } = 1$ ; if (p $\scriptstyle < = \ 0$ . || $\mathrm { ~ p ~ } > = \mathrm { ~ 1 ~ . ~ }$ ) throw("bad p in Binomialdist"); $\mathrm { ~ \bf ~ k ~ } =$ MAX(0,MIN(n,(Int)(n\*pe))); Starting guess near peak of density. if $\cdot \mathtt { p } <$ cdf(k)) { Expand interval until we bracket. do { $\mathrm { ~ \bf ~ k ~ } =$ MAX(k-inc,0); inc $\ast = ~ 2$ ; } while $( \mathtt { p } \ <$ cdf(k)); $\mathbf { k } 1 \ = \ \mathbf { k } ;$ $\mathtt { k u \textbf { = k } + }$ inc/2; } else { do { ${ \bf k } \ = \ { \tt M I N } \left( { \tt k } { + } \mathrm { i n c } \ , \mathrm { n } { + } 1 \right) ;$ inc $\ast = ~ 2$ ; } while (p > cdf(k)); ku $\mathbf { \lambda } = \mathbf { \lambda } _ { \mathbf { k } } ;$ ; $\mathrm { ~ k ~ 1 ~ } = \mathrm { ~ k ~ }$ - inc/2; } while (ku-kl>1) { Now contract the interval by bisectio $k ~ = ~ \left( \mathrm { k } \mathrm { 1 } \mathrm { + } \mathrm { k } \mathrm { u } \right) / 2$ ; if $\mathrm { ~ ( ~ p ~ < ~ }$ cdf $\mathbf { \Psi } ( \mathbf { k } )$ ) $\mathtt { k u } \ = \ \mathtt { k }$ ; else $\mathrm { ~ \ k ~ } ] \ = \ \mathrm { ~ k ~ }$ ; } return kl; }

# CITED REFERENCES AND FURTHER READING:

Johnson, N.L. and Kotz, S. 1970, Continuous Univariate Distributions, 2 vols. (Boston: Houghton Mifflin).[1]   
Johnson, N.L. and Kotz, S. 1969, Discrete Distributions (Boston: Houghton Mifflin).[2]   
Gelman, A., Carlin, J.B., Stern, H.S., and Rubin, D.B. 2003, Bayesian Data Analysis, 2nd ed. (Boca Raton, FL: Chapman & Hall/CRC), Appendix A.   
Lyuu, Y-D. 2002, Financial Engineering and Computation (Cambridge, UK: Cambridge University Press).[3]

# 7.0 Introduction

It may seem perverse to use a computer, that most precise and deterministic of all machines conceived by the human mind, to produce “random” numbers. More than perverse, it may seem to be a conceptual impossibility. After all, any program produces output that is entirely predictable, hence not truly “random.”

Nevertheless, practical computer “random number generators” are in common use. We will leave it to philosophers of the computer age to resolve the paradox in a deep way (see, e.g., Knuth [1] $\ S 3 . 5$ for discussion and references). One sometimes hears computer-generated sequences termed pseudo-random, while the word random is reserved for the output of an intrinsically random physical process, like the elapsed time between clicks of a Geiger counter placed next to a sample of some radioactive element. We will not try to make such fine distinctions.

A working definition of randomness in the context of computer-generated sequences is to say that the deterministic program that produces a random sequence should be different from, and — in all measurable respects — statistically uncorrelated with, the computer program that uses its output. In other words, any two different random number generators ought to produce statistically the same results when coupled to your particular applications program. If they don’t, then at least one of them is not (from your point of view) a good generator.

The above definition may seem circular, comparing, as it does, one generator to another. However, there exists a large body of random number generators that mutually do satisfy the definition over a very, very broad class of applications programs. And it is also found empirically that statistically identical results are obtained from random numbers produced by physical processes. So, because such generators are known to exist, we can leave to the philosophers the problem of defining them.

The pragmatic point of view is thus that randomness is in the eye of the beholder (or programmer). What is random enough for one application may not be random enough for another. Still, one is not entirely adrift in a sea of incommensurable applications programs: There is an accepted list of statistical tests, some sensible and some merely enshrined by history, that on the whole do a very good job of ferreting out any nonrandomness that is likely to be detected by an applications program (in this case, yours). Good random number generators ought to pass all of these tests, or at least the user had better be aware of any that they fail, so that he or she will be able to judge whether they are relevant to the case at hand.

For references on this subject, the one to turn to first is Knuth [1]. Be cautious about any source earlier than about 1995, since the field progressed enormously in the following decade.

# CITED REFERENCES AND FURTHER READING:

Knuth, D.E. 1997, Seminumerical Algorithms, 3rd ed., vol. 2 of The Art of Computer Programming (Reading, MA: Addison-Wesley),Chapter 3,especially $\ S 3 . 5 . [ 1 ]$

Gentle, J.E. 2003, Random Number Generation and Monte Carlo Methods, 2nd ed. (New York: Springer).

# 7.1 Uniform Deviates

Uniform deviates are just random numbers that lie within a specified range, typically 0.0 to 1.0 for floating-point numbers, or 0 to $2 ^ { 3 2 } - 1$ or $2 ^ { 6 4 } - 1$ for integers. Within the range, any one number is just as likely as any other. They are, in other words, what you probably think “random numbers” are. However, we want to distinguish uniform deviates from other sorts of random numbers, for example, numbers drawn from a normal (Gaussian) distribution of specified mean and standard deviation. These other sorts of deviates are almost always generated by performing appropriate operations on one or more uniform deviates, as we will see in subsequent sections. So, a reliable source of random uniform deviates, the subject of this section, is an essential building block for any sort of stochastic modeling or Monte Carlo computer work.

The state of the art for generating uniform deviates has advanced considerably in the last decade and now begins to resemble a mature field. It is now reasonable to expect to get “perfect” deviates in no more than a dozen or so arithmetic or logical operations per deviate, and fast, “good enough” deviates in many fewer operations than that. Three factors have all contributed to the field’s advance: first, new mathematical algorithms; second, better understanding of the practical pitfalls; and, third, standardization of programming languages in general, and of integer arithmetic in particular — and especially the universal availability of unsigned 64-bit arithmetic in C and $\mathrm { C } { + } { + }$ . It may seem ironic that something as down-in-the-weeds as this last factor can be so important. But, as we will see, it really is.

The greatest lurking danger for a user today is that many out-of-date and inferior methods remain in general use. Here are some traps to watch for:

- Never use a generator principally based on a linear congruential generator (LCG) or a multiplicative linear congruential generator (MLCG). We say more about this below.   
Never use a generator with a period less than $\sim 2 ^ { 6 4 } \approx 2 \times 1 0 ^ { 1 9 }$ , or any generator whose period is undisclosed. Never use a generator that warns against using its low-order bits as being completely random. That was good advice once, but it now indicates an obsolete algorithm (usually a LCG).

- Never use the built-in generators in the C and $\mathrm { C } { + } { + }$ languages, especially rand and srand. These have no standard implementation and are often badly flawed.

If all scientific papers whose results are in doubt because of one or more of the above traps were to disappear from library shelves, there would be a gap on each shelf about as big as your fist.

You may also want to watch for indications that a generator is overengineered, and therefore wasteful of resources:

- Avoid generators that take more than (say) two dozen arithmetic or logical operations to generate a 64-bit integer or double precision floating result. - Avoid using generators (over-)designed for serious cryptographic use. - Avoid using generators with period $> 1 0 ^ { 1 0 0 }$ . You really will never need it, and, above some minimum bound, the period of a generator has little to do with its quality.

Since we have told you what to avoid from the past, we should immediately follow with the received wisdom of the present:

An acceptable random generator must combine at least two (ideally, unrelated) methods. The methods combined should evolve independently and share no state. The combination should be by simple operations that do not produce results less random than their operands.

If you don’t want to read the rest of this section, then use the following code to generate all the uniform deviates you’ll ever need. This is our suspenders-and-belt, full-body-armor, never-any-doubt generator; and, it also meets the above guidelines for avoiding wasteful, overengineered methods. (The fastest generators that we recommend, below, are only ${ \sim } 2 . 5 \times$ faster, even when their code is copied inline into an application.)

# ran.h struct Ran {

Implementation of the highest quality recommended generator. The constructor is called with an integer seed and creates an instance of the generator. The member functions int64, doub, and int32 return the next values in the random sequence, as a variable type indicated by their names. The period of the generator is 	 3:138  1057.

Ullong u,v,w;   
Ran(Ullong j) : v(4101842887655102017LL), w(1) {   
Constructor. Call with any integer seed (except value of $\mathtt { v }$ above). $\mathrm { ~ u ~ } = \mathrm { ~ j ~ }$ ^ v; int64(); $\mathrm { ~ v ~ } = \mathrm { ~ u ~ }$ ; int64(); $\texttt { w } = \texttt { v }$ ; int64();   
}   
inline Ullong int64() {   
Return 64-bit random integer. See text for explanation of method. $\texttt { u } = \texttt { u } *$ 2862933555777941757LL $^ +$ 7046029254386353087LL; $\texttt { V } \hat { } = \texttt { V } > > \texttt { 1 7 }$ ; $\texttt { V } \hat { } = \texttt { V } < < \texttt { 3 1 }$ ; $\texttt { v } \hat { } = \texttt { v } > > \texttt { 8 }$ ; $\kappa =$ 4294957665U\*(w & 0xffffffff) $^ +$ $\left( \mathrm { ~ w ~ } > > \ 3 2 \right)$ ; Ullong $\texttt { x } = \texttt { u } \hat { }$ ( $\mathbf { \chi } _ { \mathrm { ~ u ~ } } < < \mathbf { \chi } _ { 2 1 } )$ ; $\texttt { x } \hat { } = \texttt { x } > > 3 5$ ; $\mathrm { ~  ~ x ~ } \hat { \mathrm { ~  ~ \mu ~ } } = \mathrm { ~  ~ x ~ } < < \mathrm { ~  ~ 4 ~ } _ { \mathrm { i } }$ ; return $( { \texttt { x } } + { \texttt { v } } ) \ { \hat { } } \sim { \ } _ { \texttt { w } }$ ;   
inline Doub doub() { return 5.42101086242752217E-20 $^ *$ int64(); }   
Return random double-precision floating value in the range 0. to 1.   
inline Uint int32() { return (Uint)int64(); }   
Return 32-bit random integer.

# };

The basic premise here is that a random generator, because it maintains internal state between calls, should be an object, a struct. You can declare more than one instance of it (although it is hard to think of a reason for doing so), and different instances will in no way interact.

The constructor Ran() takes a single integer argument, which becomes the seed for the sequence generated. Different seeds generate (for all practical purposes) completely different sequences. Once constructed, an instance of Ran offers several different formats for random output. To be specific, suppose you have created an instance by the declaration

# Ran myran(17);

where myran is now the name of this instance, and 17 is its seed. Then, the function myran.int64() returns a random 64-bit unsigned integer; the function myran.int32() returns an unsigned 32-bit integer; and the function myran.doub() returns a double-precision floating value in the range 0:0 to 1:0. You can intermix calls to these functions as you wish. You can use any returned random bits for any purpose. If you need a random integer between 1 and n (inclusive), say, then the expression $1 ~ +$ myran.int64() $\%$ $\left( \mathtt { n } \mathrm { - } 1 \right)$ is perfectly OK (though there are faster idioms than the use of $\%$ ).

In the rest of this section, we briefly review some history (the rise and fall of the LCG), then give details on some of the algorithmic methods that go into a good generator, and on how to combine those methods. Finally, we will give some further recommended generators, additional to Ran above.

# 7.1.1 Some History

With hindsight, it seems clear that the whole field of random number generation was mesmerized, for far too long, by the simple recurrence equation

$$
I _ { j + 1 } = a I _ { j } + c { \pmod { m } }
$$

Here $m$ is called the modulus, $a$ is a positive integer called the multiplier, and $c$ (which may be zero) is nonnegative integer called the increment. For $c \neq 0$ , equation (7.1.1) is called a linear congruential generator (LCG). When $c = 0$ , it is sometimes called a multiplicative LCG or MLCG.

The recurrence (7.1.1) must eventually repeat itself, with a period that is obviously no greater than $m$ . If $m , a$ ; and $c$ are properly chosen, then the period will be of maximal length, i.e., of length $m$ . In that case, all possible integers between 0 and $m - 1$ occur at some point, so any initial “seed” choice of $I _ { 0 }$ is as good as any other:

The sequence just takes off from that point, and successive values $I _ { j }$ are the returned “random” values.

The idea of LCGs goes back to the dawn of computing, and they were widely used in the 1950s and thereafter. The trouble in paradise first began to be noticed in the mid-1960s (e.g., [1]): If $k$ random numbers at a time are used to plot points in $k$ -dimensional space (with each coordinate between 0 and 1), then the points will not tend to “fill up” the $k$ -dimensional space, but rather will lie on $( k - 1 )$ -dimensional “planes.” There will be at most about $m ^ { 1 / k }$ such planes. If the constants $m$ and $a$ are not very carefully chosen, there will be many fewer than that. The number $m$ was usually close to the machine’s largest representable integer, often $\sim 2 ^ { 3 2 }$ . So, for example, the number of planes on which triples of points lie in three-dimensional space can be no greater than about the cube root of $2 ^ { 3 2 }$ , about 1600. You might well be focusing attention on a physical process that occurs in a small fraction of the total volume, so that the discreteness of the planes can be very pronounced.

Even worse, many early generators happened to make particularly bad choices for $m$ and $a$ . One infamous such routine, RANDU, with $a \ : = \ : 6 5 5 3 9$ and $m = 2 ^ { 3 1 }$ , was widespread on IBM mainframe computers for many years, and widely copied onto other systems. One of us recalls as a graduate student producing a “random” plot with only 11 planes and being told by his computer center’s programming consultant that he had misused the random number generator: “We guarantee that each number is random individually, but we don’t guarantee that more than one of them is random.” That set back our graduate education by at least a year!

LCGs and MLCGs have additional weaknesses: When m is chosen as a power of 2 (e.g., RANDU), then the low-order bits generated are hardly random at all. In particular, the least significant bit has a period of at most 2, the second at most 4, the third at most 8, and so on. But, if you don’t choose m as a power of 2 (in fact, choosing $m$ prime is generally a good thing), then you generally need access to double-length registers to do the multiplication and modulo functions in equation (7.1.1). These were often unavailable in computers of the time (and usually still are).

A lot of effort subsequently went into “fixing” these weaknesses. An elegant number-theoretical test of $m$ and $a$ , the spectral test, was developed to characterize the density of planes in arbitrary dimensional space. (See [2] for a recent review that includes graphical renderings of some of the appallingly poor generators that were used historically, and also [3].) Schrage’s method [4] was invented to do the multiplication $a I _ { j }$ with only 32-bit arithmetic for $m$ as large as $2 ^ { 3 2 } - 1$ , but, unfortunately, only for certain $a$ ’s, not always the best ones. The review by Park and Miller [5] gives a good contemporary picture of LCGs in their heyday.

Looking back, it seems clear that the field’s long preoccupation with LCGs was somewhat misguided. There is no technological reason that the better, non-LCG, generators of the last decade could not have been discovered decades earlier, nor any reason that the impossible dream of an elegant “single algorithm” generator could not also have been abandoned much earlier (in favor of the more pragmatic patchwork in combined generators). As we will explain below, LCGs and MLCGs can still be useful, but only in carefully controlled situations, and with due attention to their manifest weaknesses.

# 7.1.2 Recommended Methods for Use in Combined Generators

Today, there are at least a dozen plausible algorithms that deserve serious consideration for use in random generators. Our selection of a few is motivated by aesthetics as much as mathematics. We like algorithms with few and fast operations, with foolproof initialization, and with state small enough to keep in registers or firstlevel cache (if the compiler and hardware are able to do so). This means that we tend to avoid otherwise fine algorithms whose state is an array of some length, despite the relative simplicity with which such algorithms can achieve truly humongous periods. For overviews of broader sets of methods, see [6] and [7].

To be recommendable for use in a combined generator, we require a method to be understood theoretically to some degree, and to pass a reasonably broad suite of empirical tests (or, if it fails, have weaknesses that are well characterized). Our minimal theoretical standard is that the period, the set of returned values, and the set of valid initializations should be completely understood. As a minimal empirical standard, we have used the second release (2003) of Marsaglia’s whimsically named Diehard battery of statistical tests [8]. An alternative test suite, NIST-STS [9], might be used instead, or in addition.

Simply requiring a combined generator to pass Diehard or NIST-STS is not an acceptably stringent test. These suites make only ${ \sim } 1 0 ^ { 7 }$ calls to the generator, whereas a user program might make $1 0 ^ { 1 2 }$ or more. Much more meaningful is to require that each method in a combined generator separately pass the chosen suite. Then the combination generator (if correctly constructed) should be vastly better than any one component. In the tables below, we use the symbol “¾” to indicate that a method passes the Diehard tests by itself. (For 64-bit quantities, the statement is that the 32 high and low bits each pass.) Correspondingly, the words “can be used as random,” below, do not imply perfect randomness, but only a minimum level for quick-and-dirty applications where a better, combined, generator is just not needed.

We turn now to specific methods, starting with methods that use 64-bit unsigned arithmetic (what we call Ullong, that is, unsigned long long in the Linux/Unix world, or unsigned __int64 on planet Microsoft).

(A) 64-bit Xorshift Method. This generator was discovered and characterized by Marsaglia [10]. In just three XORs and three shifts (generally fast operations) it produces a full period of $2 ^ { 6 4 } - 1$ on 64 bits. (The missing value is zero, which perpetuates itself and must be avoided.) High and low bits pass Diehard. A generator can use either the three-line update rule, below, that starts with $< <$ , or the rule that starts with $> >$ . (The two update rules produce different sequences, related by bit reversal.)

$$
\begin{array} { r l } { \mathrm { s t a t e : ~ } } & { x ( \mathrm { u n s i g n e d ~ 6 4 - b i t } ) } \\ { \mathrm { i n i t i a l i z e : ~ } } & { x \neq 0 } \\ { \mathrm { u p d a t e : ~ } } & { x \gets x \wedge ( x \ > \ \circ \ \mathfrak { a } _ { 1 } ) , } \\ & { x \gets x \wedge ( x \ \ll \ \mathfrak { a } _ { 2 } ) , } \\ & { x \gets x \wedge ( x \ > \ \circ \ \mathfrak { a } _ { 3 } ) ; } \\ { \mathrm { o r ~ } } & { x \gets x \wedge ( x \ \ll \ \mathfrak { a } _ { 1 } ) , } \\ & { x \gets x \wedge ( x \ > \ \mathfrak { a } _ { 2 } ) , } \end{array}
$$

x x ^ .x << a3/I can use as random: x (all bits) ¾ can use in bit mix: x (all bits) can improve by: output 64-bit MLCG successor period: $2 ^ { 6 4 } - 1$

Here is a very brief outline of the theory behind these generators: Consider the 64 bits of the integer as components in a vector of length 64, in a linear space where addition and multiplication are done modulo 2. Noting that XOR $( \wedge )$ is the same as addition, each of the three lines in the updating can be written as the action of a $6 4 \times$ 64 matrix on a vector, where the matrix is all zeros except for ones on the diagonal, and on exactly one super- or subdiagonal (corresponding to $< <$ or $> >$ ). Denote this matrix as $\mathbf { S } _ { k }$ , where $k$ is the shift argument (positive for left-shift, say, and negative for right-shift). Then, one full step of updating (three lines of the updating rule, above) corresponds to multiplication by the matrix $\mathbf { T } \equiv \mathbf { S } _ { k _ { 3 } } \mathbf { S } _ { k _ { 2 } } \mathbf { S } _ { k _ { 1 } }$ .

One next needs to find triples of integers $( k _ { 1 } , k _ { 2 } , k _ { 3 } )$ , for example $( 2 1 , - 3 5 , 4 )$ , that give the full $M \equiv 2 ^ { 6 4 } - 1$ period. Necessary and sufficient conditions are that ${ \bf { \bar { T } } } ^ { M } = { \bf { 1 } }$ (the identity matrix) and that $\mathbf T ^ { N } \neq \mathbf { \bar { 1 } }$ for these seven values of $N$ : $M / 6 7 0 0 4 1 7$ , M=65537, $M / 6 4 1$ , M=257, M=17, $M / 5$ , and $M / 3$ , that is, $M$ divided by each of its seven distinct prime factors. The required large powers of $\mathbf { T }$ are readily computed by successive squarings, requiring only on the order of $6 4 ^ { 4 }$ operations. With this machinery, one can find full-period triples $( k _ { 1 } , k _ { 2 } , k _ { 3 } )$ by exhaustive search, at a reasonable cost.

Brent [11] has pointed out that the 64-bit xorshift method produces, at each bit position, a sequence of bits that is identical to one produced by a certain linear feedback shift register (LFSR) on 64 bits. (We will learn more about LFSRs in $\ S 7 . 5 . )$ The xorshift method thus potentially has some of the same strengths and weaknesses as an LFSR. Mitigating this, however, is the fact that the primitive polynomial equivalent of a typical xorshift generator has many nonzero terms, giving it better statistical properties than LFSR generators based, for example, on primitive trinomials. In effect, the xorshift generator is a way to step simultaneously 64 nontrivial onebit LFSR registers, using only six fast, 64-bit operations. There are other ways of making fast steps on LFSRs, and combining the output of more than one such generator [12,13], but none as simple as the xorshift method.

While each bit position in an xorshift generator has the same recurrence, and therefore the same sequence with period $2 ^ { 6 4 } - 1$ , the method guarantees offsets to each sequence such that all nonzero 64-bit words are produced across the bit positions during one complete cycle (as we just saw).

A selection of full-period triples is tabulated in [10]. Only a small fraction of full-period triples actually produce generators that pass Diehard. Also, a triple may pass in its $< <$ -first version, and fail in its $> >$ -first version, or vice versa. Since the two versions produce simply bit-reversed sequences, a failure of either sense must obviously be considered a failure of both (and a weakness in Diehard). The following recommended parameter sets pass Diehard for both the $< <$ and $> >$ rules. The sets near the top of the list may be slightly superior to the sets near the bottom. The column labeled ID assigns an identification string to each recommended generator that we will refer to later.

<table><tr><td rowspan=1 colspan=1>ID</td><td rowspan=1 colspan=1>a1</td><td rowspan=1 colspan=1>a2</td><td rowspan=1 colspan=1>a3</td></tr><tr><td rowspan=2 colspan=1>A1A2</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>35</td><td rowspan=2 colspan=1>45</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>41</td></tr><tr><td rowspan=1 colspan=1>A3</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>31</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1>A4</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>29</td><td rowspan=1 colspan=1>14</td></tr><tr><td rowspan=1 colspan=1>A5</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>29</td><td rowspan=1 colspan=1>11</td></tr><tr><td rowspan=1 colspan=1>A6</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>13</td></tr><tr><td rowspan=1 colspan=1>A7</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>37</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>A8</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>43</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>A9</td><td rowspan=1 colspan=1>23</td><td rowspan=1 colspan=1>41</td><td rowspan=1 colspan=1>18</td></tr></table>

It is easy to design a test that the xorshift generator fails if used by itself. Each bit at step $i + 1$ depends on at most 8 bits of step $i$ , so some simple logical combinations of the two timesteps (and appropriate masks) will show immediate nonrandomness. Also, when the state passes though a value with only small numbers of 1 bits, as it must eventually do (so-called states of low Hamming weight), it will take longer than expected to recover. Nevertheless, used in combination, the xorshift generator is an exceptionally powerful and useful method. Much grief could have been avoided had it, instead of LCGs, been discovered in 1949!

(B) Multiply with Carry (MWC) with Base $\ b { b } = 2 ^ { 3 2 }$ . Also discovered by Marsaglia, the base $b$ of an MWC generator is most conveniently chosen to be a power of 2 that is half the available word length (i.e., $b = 3 2$ for 64-bit words). The MWC is then defined by its multiplier $a$ .

state: $x$ (unsigned 64-bit)   
initialize: $\begin{array} { r l } & { 1 \leq x \leq 2 ^ { 3 2 } - 1 } \\ & { x  a ( x \& [ 2 ^ { 3 2 } - 1 ] ) + ( x \gg 3 2 ) } \\ & { x ( \mathrm { l o w } 3 2 \mathrm { b i t s } ) \quad \ast } \\ & { x ( \mathrm { a l l } 6 4 \mathrm { b i t s } ) } \end{array}$   
update:   
can use as random:   
can use in bit mix:   
can improve by: output 64-bit xorshift successor to 64 bit $x$   
period: $( 2 ^ { 3 2 } a - 2 ) / 2$ (a prime)

An MWC generator with parameters $b$ and $a$ is related theoretically [14] to, though not identical to, an LCG with modulus $m = a b - 1$ and multiplier $a$ . It is easy to find values of $a$ that make $m$ a prime, so we get, in effect, the benefit of a prime modulus using only power-of-two modular arithmetic. It is not possible to choose $a$ to give the maximal period $m$ , but if $a$ is chosen to make both $m$ and $( m - 1 ) / 2$ prime, then the period of the MCG is $( m - 1 ) / 2$ , almost as good. A fraction of candidate $a$ ’s thus chosen passes the standard statistical test suites; a spectral test [14] is a promising development, but we have not made use of it here.

Although only the low $b$ bits of the state $x$ can be taken as algorithmically random, there is considerable randomness in all the bits of $x$ that represent the product $a b$ . This is very convenient in a combined generator, allowing the entire state $x$ to be used as a component. In fact, the first two recommended $a$ ’s below give $a b$ so close to $2 ^ { 6 4 }$ (within about $2 \mathrm { p p m } ,$ that the high bits of $x$ actually pass Diehard. (This is a good example of how any test suite can fail to find small amounts of highly nonrandom behavior, in this case as many as 8000 missing values in the top 32 bits.)

Apart from this kind of consideration, the values below are recommended with no particular ordering.

<table><tr><td>ID</td><td>a</td></tr><tr><td>B1</td><td>4294957665</td></tr><tr><td>B2</td><td>4294963023</td></tr><tr><td>B3</td><td>4162943475</td></tr><tr><td>B4</td><td>3947008974</td></tr><tr><td>B5</td><td>3874257210</td></tr><tr><td>B6</td><td>2936881968</td></tr><tr><td>B7</td><td>2811536238</td></tr><tr><td>B8</td><td>2654432763</td></tr><tr><td>B9</td><td>1640531364</td></tr></table>

(C) LCG Modulo $2 ^ { 6 4 }$ . Why in the world do we include this generator after vilifying it so thoroughly above? For the parameters given (which strongly pass the spectral test), its high 32 bits almost, but don’t quite, pass Diehard, and its low 32 bits are a complete disaster. Yet, as we will see when we discuss the construction of combined generators, there is still a niche for it to fill. The recommended multipliers $a$ below have good spectral characteristics [15].

state: $x$ (unsigned 64-bit)   
initialize: any value   
update: x ax C c .mod $2 ^ { 6 4 }$ /   
can use as random: $x$ (high 32 bits, with caution)   
can use in bit mix: $x$ (high 32 bits)   
can improve by: output 64-bit xorshift successor   
period: $2 ^ { 6 4 }$

<table><tr><td>ID</td><td>a</td><td>c (any odd value ok)</td></tr><tr><td>C1</td><td>3935559000370003845</td><td>2691343689449507681</td></tr><tr><td>C2</td><td>3202034522624059733</td><td>4354685564936845319</td></tr><tr><td>C3</td><td>2862933555777941757</td><td>7046029254386353087</td></tr></table>

(D) MLCG Modulo $2 ^ { 6 4 }$ . As for the preceding one, the useful role for this generator is strictly limited. The low bits are highly nonrandom. The recommended multipliers have good spectral characteristics (some from [15]).

state: $x$ (unsigned 64-bit)   
initialize: $x \neq 0$   
update: $x \gets a x$ .mod $2 ^ { 6 4 }$ /   
can use as random: $x$ (high 32 bits, with caution)   
can use in bit mix: $x$ (high 32 bits)   
can improve by: output 64-bit xorshift successor   
period: $2 ^ { 6 2 }$

<table><tr><td rowspan=1 colspan=1>ID</td><td rowspan=1 colspan=1>a</td></tr><tr><td rowspan=2 colspan=1>D1D2</td><td rowspan=1 colspan=1>2685821657736338717</td></tr><tr><td rowspan=1 colspan=1>7664345821815920749</td></tr><tr><td rowspan=1 colspan=1>D3</td><td rowspan=1 colspan=1>4768777513237032717</td></tr><tr><td rowspan=1 colspan=1>D4</td><td rowspan=1 colspan=1>1181783497276652981</td></tr><tr><td rowspan=1 colspan=1>D5</td><td rowspan=1 colspan=1>702098784532940405</td></tr></table>

(E) MLCG with $m \gg 2 ^ { 3 2 }$ , $\mathbf { \nabla } m$ Prime. When 64-bit unsigned arithmetic is available, the MLCGs with prime moduli and large multipliers of good spectral character are decent 32-bit generators. Their main liability is that the 64-bit multiply and 64-bit remainder operations are quite expensive for the mere 32 (or so) bits of the result.

state: initialize: $\begin{array} { r l } & { x \mathrm { ~ ( u n s i g n e d ~ 6 4 - b i t ) } } \\ & { 1 \leq x \leq m - 1 } \\ & { x  a x \mathrm { ~ ( m o d ~ } m \mathrm { ) } } \\ & { x \quad ( 1 \leq x \leq m - 1 ) \mathrm { ~ o r ~ l o w ~ } 3 2 \mathrm { ~ b i t s ~ \quad ~ \ast ~ } } \\ & { \mathrm { ( s a m e ) } } \\ & { m - 1 } \end{array}$   
update:   
can use as random:   
can use in bit mix:   
period:

The parameter values below were kindly computed for us by P. L’Ecuyer. The multipliers are about the best that can be obtained for the prime moduli, close to powers of 2, shown. Although the recommended use is for only the low 32 bits (which all pass Diehard), you can see that (depending on the modulus) as many as 43 reasonably good bits can be obtained for the cost of the 64-bit multiply and remainder operations.

<table><tr><td rowspan=1 colspan=1>ID</td><td rowspan=1 colspan=1>m</td><td rowspan=1 colspan=1>a</td></tr><tr><td rowspan=1 colspan=1>E1E2E3</td><td rowspan=1 colspan=1>239-7 = 549755813881</td><td rowspan=1 colspan=1>100141463050882325708129</td></tr><tr><td rowspan=1 colspan=1>E4E5E6</td><td rowspan=1 colspan=1>241-21 = 2199023255531</td><td rowspan=1 colspan=1>518378110707396639568</td></tr><tr><td rowspan=1 colspan=1>E7E8E9</td><td rowspan=1 colspan=1>242-11 = 4398046511093</td><td rowspan=1 colspan=1>178197821143071542852</td></tr><tr><td rowspan=1 colspan=1>E10E11E12</td><td rowspan=1 colspan=1>243-57 = 8796093022151</td><td rowspan=1 colspan=1>209625920521632006881</td></tr></table>

(F) MLCG with $m \gg 2 ^ { 3 2 }$ , $\pmb { m }$ Prime, and $a ( m - 1 ) \approx 2 ^ { 6 4 }$ . A variant, for use in combined generators, is to choose $m$ and $a$ to make $a ( m - 1 )$ as close as possible to $2 ^ { 6 4 }$ , while still requiring that $m$ be prime and that $a$ pass the spectral test. The purpose of this maneuver is to make $a x$ a 64-bit value with good randomness in its high bits, for use in combined generators. The expense of the multiply and remainder operations is still the big liability, however. The low 32 bits of $x$ are not significantly less random than those of the previous MLCG generators E1–E12.

state: $x$ (unsigned 64-bit)   
initialize: $1 \leq x \leq m - 1$   
update: $x \gets a x$ .mod m/   
can use as random: $x$ . $( 1 \leq x \leq m - 1 )$ or low 32 bits ¾   
can use in bit mix: $^ { a x }$ (but don’t use both $a x$ and $x$ ) ¾   
can improve by: output 64-bit xorshift successor of $^ { a x }$   
period: m  1

<table><tr><td>ID</td><td>m</td><td>a</td></tr><tr><td>F1</td><td>1148 × 232 + 11 = 4930622455819</td><td>3741260</td></tr><tr><td>F2</td><td>1264× 23² +9 = 5428838662153</td><td>3397916</td></tr><tr><td>F3</td><td>2039× 232 +3 = 8757438316547</td><td>2106408</td></tr></table>

# 7.1.3 How to Construct Combined Generators

While the construction of combined generators is an art, it should be informed by underlying mathematics. Rigorous theorems about combined generators are usually possible only when the generators being combined are algorithmically related; but that in itself is usually a bad thing to do, on the general principle of “don’t put all your eggs in one basket.” So, one is left with guidelines and rules of thumb.

The methods being combined should be independent of one another. They must share no state (although their initializations are allowed to derive from some convenient common seed). They should have different, incommensurate, periods. And, ideally, they should “look like” each other algorithmically as little as possible. This latter criterion is where some art necessarily enters.

The output of the combination generator should in no way perturb the independent evolution of the individual methods, nor should the operations effecting combination have any side effects.

The methods should be combined by binary operations whose output is no less random than one input if the other input is held fixed. For 32- or 64-bit unsigned arithmetic, this in practice means that only the $^ +$ and $\wedge$ operators can be used. As an example of a forbidden operator, consider multiplication: If one operand is a power of 2, then the product will end in trailing zeros, no matter how random is the other operand.

All bit positions in the combined output should depend on high-quality bits from at least two methods, and may also depend on lower-quality bits from additional methods. In the tables above, the bits labeled “can use as random” are considered high quality; those labeled “can use in bit mix” are considered low quality, unless they also pass a statistical suite such as Diehard.

There is one further trick at our disposal, the idea of using a method as a successor relation instead of as a generator in its own right. Each of the methods described above is a mapping from some 64-bit state $x _ { i }$ to a unique successor state $x _ { i + 1 }$ . For a method to pass a good statistical test suite, it must have no detectable correlations between a state and its successor. If, in addition, the method has period $2 ^ { 6 4 }$ or $2 ^ { 6 4 } - 1$ , then all values (except possibly zero) occur exactly once as successor states.

Suppose we take the output of a generator, say C1 above, with period $2 ^ { 6 4 }$ , and run it through generator A6, whose period is $2 ^ { 6 4 } - 1$ , as a successor relation. This is conveniently denoted by “A6(C1),” which we will call a composed generator. Note that the composed output is emphatically not fed back into the state of C1, which continues unperturbed. The composed generator A6(C1) has the period of C1, not, unfortunately, the product of the two periods. But its random mapping of C1’s output values effectively fixes C1’s problems with short-period low bits. (The better so if the form of A6 with left-shift first is used.) And, A6(C1) will also fix A6’s weakness that a bit depends only on a few bits of the previous state. We will thus consider a carefully constructed composed generator as being a combined generator, on a par with direct combining via $^ +$ or ^.

Composition is inferior to direct combining in that it costs almost as much but does not increase the size of the state or the length of the period. It is superior to direct combining in its ability to mix widely differing bit positions. In the previous example we would not have accepted $\mathbf { A } 6 { + } \mathbf { C } 1$ as a combined generator, because the low bits of C1 are so poor as to add little value to the combination; but A6(C1) has no such liability, and much to recommend it. In the preceding summary tables of each method, we have indicated recommended combinations for composed generators in the table entries, “can improve by.”

We can now completely describe the generator in Ran, above, by the pseudoequation,

$$
\mathrm { R a n } = [ \mathrm { A l } _ { l } ( \mathbf { C } 3 ) + \mathrm { A } 3 _ { r } ] \wedge \mathbf { B } 1
$$

that is, the combination and/or composition of four different generators. For the methods A1 and A3, the subscripts $l$ and $r$ denote whether a left- or right-shift operation is done first. The period of Ran is the least common multiple of the periods of C3, A3, and B1.

The simplest and fastest generator that we can readily recommend is

$$
{ \tt R a n q 1 } \equiv { \tt D 1 } ( { \tt A 1 } _ { r } )
$$

implemented as

struct Ranq1 {   
Recommended generator for everyday use. The period is $\approx 1 . 8 \times 1 0 ^ { 1 9 }$ . Calling conventions same as Ran, above.

Ullong v;Ranq1(Ullong j) : v(4101842887655102017LL) {$ { \texttt { v } } \hat { } = :$ j;$\qquad \mathtt { v } =$ int64();}inline Ullong int64() {$\tau \ \hat { \mathbf { \Omega } } = \textbf { v } > > \ 2 1$ ; $\texttt { v } \hat { } = \texttt { v } < < \texttt { 3 5 }$ ; $\texttt { V } \hat { } = \texttt { V } > > \texttt { 4 }$ ;return $^ { \texttt { v } * }$ 2685821657736338717LL;}inline Doub doub() { return 5.42101086242752217E-20 $^ *$ int64(); }inline Uint int32() { return (Uint)int64(); }};

Ranq1 generates a 64-bit random integer in 3 shifts, 3 xors, and one multiply, or a double floating value in one additional multiply. Its method is concise enough to go easily inline in an application. It has a period of “only” $1 . 8 \times 1 0 ^ { 1 9 }$ , so it should not be used by an application that makes more than $\sim 1 0 ^ { 1 2 }$ calls. With that restriction, we think that Ranq1 will do just fine for $9 9 . 9 9 \%$ of all user applications, and that Ran can be reserved for the remaining $0 . 0 1 \%$ .

If the “short” period of Ranq1 bothers you (which it shouldn’t), you can instead use

$$
\mathrm { R a n q } 2 \equiv \mathrm { A } 3 _ { r } \wedge \mathrm { B } 1
$$

whose period is $8 . 5 \times 1 0 ^ { 3 7 }$ .

# .h struct Ranq2 {

Backup generator if Ranq1 has too short a period and Ran is too slow. The period is $\approx 8 . 5 \times$ $1 0 ^ { 3 7 }$ . Calling conventions same as Ran, above.

Ullong v,w; Ranq2(Ullong j) : v(4101842887655102017LL), w(1) { $\scriptstyle \mathtt { v } \ \hat { } =$ j; $\kappa =$ int64(); $\qquad \mathtt { v } \ =$ int64(); } inline Ullong int64() { $\bar { \tau } \stackrel {  } { = } \texttt { V } > > 1 7$ ; $\texttt { v } \hat { } = \texttt { v } < < \texttt { 3 1 }$ ; $\texttt { v } \hat { } = \texttt { v } > > \texttt { 8 }$ ; $\kappa =$ 4294957665U\*(w & 0xffffffff) $^ +$ $\mathit { \Pi } _ { \mathbb { W } } ^ { ' } > > \mathit { \Omega } 3 2 )$ ; return $ { \texttt { v } } ^ { \star }  { \texttt { w } }$ ; } inline Doub doub() { return 5.42101086242752217E-20 $^ *$ int64(); } inline Uint int32() { return (Uint)int64(); } };

# 7.1.4 Random Hashes and Random Bytes

Every once in a while, you want a random sequence $H _ { i }$ whose values you can visit or revisit in any order of $i$ ’s. That is to say, you want a random hash of the integers $i$ , one that passes serious tests for randomness, even for very ordered sequences of $i$ ’s. In the language already developed, you want a generator that has no state at all and is built entirely of successor relationships, starting with the value $i$ .

An example that easily passes the Diehard test is

$$
{ \tt R a n h a s h } \equiv { \tt A } 2 _ { l } ( { \tt D } 3 ( { \tt A } 7 _ { r } ( { \tt C } 1 ( i ) ) ) )
$$

Note the alternation between successor relations that utilize 64-bit multiplication and ones using shifts and XORs.

# ran.h struct Ranhash {

High-quality random hash of an integer into several numeric types. inline Ullong int64(Ullong u) { Returns hash of u as a 64-bit integer. Ullong $ { \texttt { v } } =  { \texttt { u } } *$ 3935559000370003845LL $^ +$ 2691343689449507681LL; $\texttt { v } \hat { } = \texttt { v } > > 2 1$ ; $\bar { \tau } = \texttt { V } < < \texttt { 3 7 }$ ; $\texttt { v } \hat { } = \texttt { v } > > \texttt { 4 }$ ; ${ \textbf { \texttt { v } } } * =$ 4768777513237032717LL; $\texttt { v } \hat { } = \texttt { v } < < \texttt { 2 0 }$ ; v ^= v >> 41; $\texttt { V } \hat { } = \texttt { V } < < \texttt { 5 }$ ; return v; inline Uint int32(Ullong u) Returns hash of u as a 32-bit integer. { return (Uint)(int64(u) & 0xffffffff) ; } inline Doub doub(Ullong u) Returns hash of u as a double-precision floating value between 0. and 1. return 5.42101086242752217E-20 $^ *$ int64(u); }

Since Ranhash has no state, it has no constructor. You just call its $\mathtt { i n t } 6 4 ( i )$ function, or any of its other functions, with your value of $i$ whenever you want.

Random Bytes. In a different set of circumstances, you may want to generate random integers a byte at a time. You can of course pull bytes out of any of the above recommended combination generators, since they are constructed to be equally good on all bits. The following code, added to any of the generators above, augments them with an int8() method. (Be sure to initialize bc to zero in the constructor.)

Ullong breg;   
Int bc;   
inline unsigned char int8() { if (bc--) return (unsigned char)(breg $> > = ~ 8 )$ ; breg $=$ int64(); bc $= ~ 7$ ; return (unsigned char)breg;   
}

If you want a more byte-oriented, though not necessarily faster, algorithm, an interesting one — in part because of its interesting history — is Rivest’s RC4, used in many Internet applications. RC4 was originally a proprietary algorithm of RSA, Inc., but it was protected simply as a trade secret and not by either patent or copyright. The result was that when the secret was breached, by an anonymous posting to the Internet in 1994, RC4 became, in almost all respects, public property. The name RC4 is still protectable, and is a trademark of RSA. So, to be scrupulous, we give the following implementation another name, Ranbyte.

# struct Ranbyte {

nerator for random bytes using the algorithm generally known as RC4.   
Int s[256],i,j,ss;   
Uint v;   
Ranbyte(Int u) {   
Constructor. Call with any integer seed. $\qquad \mathtt { v } \ =$ 2244614371U ^ u; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; i<256; $\dot { \bf 1 } + +$ ) {s[i] = i;} for $\scriptstyle \dot { \ j } = 0$ , $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; i<256; $\mathbf { i } + + \mathbf { i }$ ) { ss $=$ s[i]; j = (j + ss + ( $\cdot \mathrm { ~  ~ v ~ } > > 2 4 )$ ) & 0xff; s[i] = s[j]; s[j] $=$ ss; $\begin{array} { c c c c c } { \mathrm { ~  ~ v ~ } = } & { ( \mathrm { ~  ~ v ~ } < < 2 4 ) } & { | } & { ( \mathrm { ~  ~ v ~ } > > 8 ) : } \end{array}$ ; } ${ \\mathrm { ~ \bf ~ i ~ } } = { \mathrm { ~ \bf ~ j ~ } } = { \mathrm { ~ \bf ~ 0 ~ } } _ { \mathrm { { i } } }$ ; for (Int $\mathtt { k } = 0$ ; $\mathtt { k } < 2 5 6$ ; $\mathrm { k } { + + }$ ) int8();   
}   
inline unsigned char int8() {   
Returns next random byte in the sequence. $\begin{array} { r c l } { \dot { \textbf { \ i } } } & { = } & { \left( \dot { \bf 1 } { + } 1 \right) } \end{array}$ & 0xff; ss = s[i]; ${ \dot { \textbf { j } } } =$ (j+ss) & 0xff; s[i] $=$ s[j]; s[j] $=$ ss; return (unsigned char)(s[(s[i] $+ \tt s$ [j]) & 0xff]);   
}   
Uint int32() {   
Returns a random 32-bit integer constructed from 4 random bytes. Slow! $\tt { v } = 0$ ; for (int $\mathtt { k } = 0$ ; k<4; k++) { $\begin{array} { r l r } { \mathrm { ~ i ~ } = } & { { } ( \mathrm { i } + 1 ) } \end{array}$ ) & 0xff; ${ \bf s } { \bf s } = { \bf s } [ \mathrm { i } ]$ ; ${ \mathrm { ~ j ~ } } =$ (j+ss) & 0xff; s[i] $=$ s[j]; s[j] $=$ ss; v = (v << 8) | s[(s[i]+s[j]) & 0xff]; } return v;

# Doub doub() {

Returns a random double-precision floating value between 0. and 1. Slow!! return 2.32830643653869629E-10 $^ *$ ( int32() $^ +$ 2.32830643653869629E-10 $^ *$ int32() );   
}

# };

Notice that there is a lot of overhead in starting up an instance of Ranbyte, so you should not create instances inside loops that are executed many times. The methods that return 32-bit integers, or double floating-point values, are slow in comparison to the other generators above, but are provided in case you want to use Ranbyte as a test substitute for another, perhaps questionable, generator.

If you find any nonrandomness at all in Ranbyte, don’t tell us. But there are several national cryptological agencies that might, or might not, want to talk to you!

# 7.1.5 Faster Floating-Point Values

The steps above that convert a 64-bit integer to a double-precision floating-point value involves both a nontrivial type conversion and a 64-bit floating multiply. They are performance bottlenecks. One can instead directly move the random bits into the right place in the double word with union structure, a mask, and some 64-bit logical operations; but in our experience this is not significantly faster.

To generate faster floating-point values, if that is an absolute requirement, we need to bend some of our design rules. Here is a variant of “Knuth’s subtractive generator,” which is a so-called lagged Fibonacci generator on a circular list of 55 values, with lags 24 and 55. Its interesting feature is that new values are generated directly as floating point, by the floating-point subtraction of two previous values.

# ran.h struct Ranfib {

Implements Knuth’s subtractive generator using only floating operations. See text for cautions.

Doub dtab[55], dd;   
Int inext, inextp;   
Ranfib(Ullong j) : inext(0), inextp(31) {   
Constructor. Call with any integer seed. Uses Ranq1 to initialize. Ranq1 init(j); for (int $\mathtt { k } = 0$ ; k<55; $\mathrm { k } { + + }$ ) dtab[k] $=$ init.doub();   
}   
Doub doub() {   
Returns random double-precision floating value between 0. and 1. if ( $^ { + + }$ inext $\scriptstyle = = { \mathsf { 5 5 } }$ ) inext $\mathit { \Theta } = \mathit { \Theta } 0$ ; if ( $^ { + + }$ inextp $= =$ 55) inextp $\qquad = \ 0$ ; dd $=$ dtab[inext] - dtab[inextp]; if (dd $< 0 \dot { . }$ ) dd $+ = \ 1 . 0$ ; return (dtab[inext] $=$ dd);   
inline unsigned long int32()   
Returns random 32-bit integer. Recommended only for testing purposes. { return (unsigned long)(doub() $^ *$ 4294967295.0);}

# };

The int32 method is included merely for testing, or incidental use. Note also that we use Ranq1 to initialize Ranfib’s table of 55 random values. See earlier editions of Knuth or Numerical Recipes for a (somewhat awkward) way to do the initialization purely internally.

Ranfib fails the Diehard “birthday test,” which is able to discern the simple relation among the three values at lags 0, 24, and 55. Aside from that, it is a good, but not great, generator, with speed as its principal recommendation.

# 7.1.6 Timing Results

Timings depend so intimately on highly specific hardware and compiler details, that it is hard to know whether a single set of tests is of any use at all. This is especially true of combined generators, because a good compiler, or a CPU with sophisticated instruction look-ahead, can interleave and pipeline the operations of the individual methods, up to the final combination operations. Also, as we write, desktop computers are in transition from 32 bits to 64, which will affect the timing of 64-bit operations. So, you ought to familiarize yourself with C’s “clock_t clock(void)” facility and run your own experiments.

That said, the following tables give typical results for routines in this section, normalized to a $3 . 4 ~ \mathrm { G H z }$ Pentium CPU, vintage 2004. The units are $1 0 ^ { 6 }$ returned values per second. Large numbers are better.

<table><tr><td>Generator</td><td>int64()</td><td>doub()</td><td>int8()</td></tr><tr><td>Ran</td><td>19</td><td>10</td><td>51</td></tr><tr><td>Ranq1</td><td>39</td><td>13</td><td>59</td></tr><tr><td>Ranq2</td><td>32</td><td>12</td><td>58</td></tr><tr><td>Ranfib</td><td></td><td>24</td><td></td></tr><tr><td>Ranbyte</td><td></td><td></td><td>43</td></tr></table>

The int8() timings for Ran, Ranq1, and Ranq2 refer to versions augmented as indicated above.

# 7.1.7 When You Have Only 32-Bit Arithmetic

Our best advice is: Get a better compiler! But if you seriously must live in a world with only unsigned 32-bit arithmetic, then here are some options. None of these individually pass Diehard.

# (G) 32-Bit Xorshift RNG

state: $x$ (unsigned 32-bit)   
initialize: update: $\begin{array} { l } { x \neq 0 } \\ { x  x \land ( x \lor \mathrm { > } \vdash b _ { 1 } ) , } \\ { x  x \land ( x \ll b _ { 2 } ) , } \\ { x  x \land ( x \lor \mathrm { > } \vdash b _ { 3 } ) ; } \\ { x  x \land ( x \ll b _ { 1 } ) , } \\ { x  x \land ( x \lor \mathrm { > } \vdash b _ { 2 } ) , } \\ { x  x \land ( x \ll b _ { 3 } ) ; } \end{array}$ or   
can use as random: $x$ (32 bits, with caution)   
can use in bit mix: $x$ (32 bits)   
can improve by: output 32-bit MLCG successor   
period: $2 ^ { 3 2 } - 1$

<table><tr><td rowspan=1 colspan=1>ID</td><td rowspan=1 colspan=1>b1</td><td rowspan=1 colspan=1>b2</td><td rowspan=1 colspan=1>b3</td></tr><tr><td rowspan=1 colspan=1>G1</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>17</td><td rowspan=2 colspan=1>53</td></tr><tr><td rowspan=1 colspan=1>G2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>13</td></tr><tr><td rowspan=1 colspan=1>G3</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>6</td></tr><tr><td rowspan=1 colspan=1>G4</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>G5</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>G6</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>G7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>7</td></tr><tr><td rowspan=1 colspan=1>G8</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>6</td></tr><tr><td rowspan=1 colspan=1>G9</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>5</td></tr></table>

# (H) MWC with Base $b = 2 ^ { 1 6 }$

state: initialize: update:

$x , y$ (unsigned 32-bit)   
$1 \leq x , y \leq 2 ^ { 1 6 } - 1$   
$x  a \ ( x \& \ [ 2 ^ { 1 6 } - 1 ] ) + ( x \ > > \ 1 6 )$   
$y  b \ ( y \ \& \ [ 2 ^ { 1 6 } - 1 ] ) + ( y \ > > \ 1 6 )$   
$( x ~ < < ~ 1 6 ) + y$   
same, or (with caution) $x$ or $y$   
output 32-bit xorshift successor   
$( 2 ^ { 1 6 } a - 2 ) ( 2 ^ { 1 6 } b - 2 ) / 4$ (product of two primes)

can use as random: can use in bit mix: can improve by: period:

<table><tr><td rowspan=1 colspan=1>ID</td><td rowspan=1 colspan=1>a</td><td rowspan=1 colspan=1>b</td></tr><tr><td rowspan=1 colspan=1>H1</td><td rowspan=1 colspan=1>62904</td><td rowspan=2 colspan=1>4187434653</td></tr><tr><td rowspan=1 colspan=1>H2</td><td rowspan=1 colspan=1>64545</td></tr><tr><td rowspan=1 colspan=1>H3</td><td rowspan=1 colspan=1>34653</td><td rowspan=1 colspan=1>64545</td></tr><tr><td rowspan=1 colspan=1>H4</td><td rowspan=1 colspan=1>57780</td><td rowspan=1 colspan=1>55809</td></tr><tr><td rowspan=1 colspan=1>H5</td><td rowspan=1 colspan=1>48393</td><td rowspan=1 colspan=1>57225</td></tr><tr><td rowspan=1 colspan=1>H6</td><td rowspan=1 colspan=1>63273</td><td rowspan=1 colspan=1>33378</td></tr></table>

# (I) LCG Modulo $2 ^ { 3 2 }$

state: $x$ (unsigned 32-bit)   
initialize: any value   
update: $x  a x + c$ .mod $2 ^ { 3 2 }$ /   
can use as random: not recommended   
can use in bit mix: not recommended   
can improve by: output 32-bit xorshift successor   
period: $2 ^ { 3 2 }$

<table><tr><td rowspan=1 colspan=1>ID</td><td rowspan=1 colspan=6>a</td><td rowspan=1 colspan=1>c (any odd ok)</td></tr><tr><td rowspan=2 colspan=1>I1I213</td><td rowspan=2 colspan=6>137238374928913364532024337845</td><td rowspan=2 colspan=1>12897061011640531513797082193</td></tr><tr><td rowspan=1 colspan=2>2024337845</td><td rowspan=1 colspan=3>2024337845</td></tr><tr><td rowspan=4 colspan=1>I4I5</td><td rowspan=3 colspan=2></td><td rowspan=3 colspan=4>32310901</td><td></td></tr><tr><td rowspan=2 colspan=1></td><td></td></tr><tr><td rowspan=1 colspan=1>626627237</td></tr><tr><td rowspan=1 colspan=6>29943829</td><td rowspan=1 colspan=1>1013904223</td></tr></table>

# (J) MLCG Modulo 232

state: $x$ (unsigned 32-bit)   
initialize: $x \neq 0$   
update: $x \gets a x$ .mod $2 ^ { 3 2 }$ /   
can use as random: not recommended   
can use in bit mix: not recommended   
can improve by: output 32-bit xorshift successor   
period: $2 ^ { 3 0 }$

<table><tr><td>ID</td><td>a</td></tr><tr><td>J1</td><td>1597334677</td></tr><tr><td></td><td>741103597</td></tr><tr><td></td><td>1914874293</td></tr><tr><td></td><td>990303917</td></tr><tr><td>我</td><td>747796405</td></tr></table>

A high-quality, if somewhat slow, combined generator is

$$
\mathrm { R a n l i m } 3 2 \equiv [ \mathrm { G } 3 _ { l } ( \mathrm { I } 2 ) + \mathrm { G } 1 _ { r } ] \wedge [ \mathrm { G } 6 _ { l } ( \mathrm { H } 6 _ { b } ) + \mathrm { H } 5 _ { b } ]
$$

implemented as

struct Ranlim32 { High-quality random generator using only 32-bit arithmetic. Same conventions as Ran. Period $\approx 3 . 1 \dot { 1 } \times \dot { 1 0 } ^ { 3 7 }$ . Recommended only when 64-bit arithmetic is not available.

Uint u,v,w1,w2; Ranlim32(Uint j) : v(2244614371U), w1(521288629U), w2(362436069U) { $\mathrm { ~ u ~ } = \mathrm { ~ j ~ }$ ^ v; int32(); $\texttt { v } = \texttt { u }$ ; int32(); } inline Uint int32() { $\texttt { u } = \texttt { u } *$ 2891336453U $^ +$ 1640531513U; $\texttt { V } \hat { } = \texttt { V } > > \ 1 3$ ; $\texttt { V } \hat { } = \texttt { V } < < \texttt { 1 7 }$ ; $\texttt { v } \hat { } = \texttt { v } > > \texttt { 5 }$ ; $\mathrm { w 1 } ~ = ~ 3 3 3 7 8 ~ *$ (w1 & 0xffff) $^ +$ $\left( \mathbf { w } 1 \ > \ 1 6 \right)$ ; $\mathtt { w } 2 ~ = ~ 5 7 2 2 5 ~ *$ (w2 & 0xffff) $^ +$ (w2 >> 16); Uint $\texttt { x } = \texttt { u } \hat { }$ (u << 9); x $\hat { \mathrm { ~ \bf ~ \chi ~ } } = \mathrm { ~ \bf ~ z ~ } > >$ 17; x $ { \hat { \mathbf { \phi } } } <  { \mathbf { \hat { z } } } \leq  { \mathbf { \phi } } \times  { \mathbf { \hat { z } } } <  { \mathbf { \phi } } 6$ ; Uint $\mathrm { ~ y ~ } = \mathrm { ~ w ~ 1 ~ } \ \hat { \ }$ ( $\tau 1 < < 1 7 )$ ; y $\hat { \mathbf { \beta } } = \texttt { y } > > \mathbf { \beta } 1 5$ ; $\mathrm { ~ y ~ } \ \hat { ~ } = \mathrm { ~ y ~ } < < \ 5$ ; return $( { \bf x } { \mathrm { ~ + ~ } } { \mathrm v } ) { \mathrm { ~ \hat { ~ } { ~ ( ~ y ~ + ~ } } } { \mathrm w } 2 )$ ; inline Doub doub() { return 2.32830643653869629E-10 $^ *$ int32(); } inline Doub truedoub() { return 2.32830643653869629E-10 $^ *$ ( int32() + 2.32830643653869629E-10 $^ *$ int32() ); } };

Note that the doub() method returns floating-point numbers with only 32 bits of precision. For full precision, use the slower truedoub() method.

# CITED REFERENCES AND FURTHER READING:

Gentle, J.E. 2003, Random Number Generation and Monte Carlo Methods, 2nd ed. (New York: Springer), Chapter 1.   
Marsaglia, G 1968, “Random Numbers Fall Mainly in the Planes”, Proceedings of the National Academy of Sciences, vol. 61, pp. 25-28.[1]   
Entacher, K. 1997, “A Collection of Selected Pseudorandom Number Generators with Linear Structures”, Technical Report No. 97, Austrian Center for Parallel Computation, University of Vienna. [Available on the Web at multiple sites.][2]   
Knuth, D.E. 1997, Seminumerical Algorithms, 3rd ed., vol. 2 of The Art of Computer Programming (Reading,MA: Addison-Wesley).[3]   
Schrage, L. 1979, “A More Portable Fortran Random Number Generator,” ACM Transactions on Mathematical Software, vol.5, pp.132-138.[4]   
Park, S.K., and Miller, K.W. 1988, “Random Number Generators: Good Ones Are Hard to Find,” Communications of the ACM,vol.31,pp.1192-1201.[5]   
L’Ecuyer, P. 1997 “Uniform Random Number Generators: A Review,” Proceedings of the 1997 Winter Simulation Conference,Andradótir, S.et al.,eds.(Piscataway, NJ: IEEE).[6]   
Marsaglia, G. 1999, “Random Numbers for C: End, at Last?”, posted 1999 January 20 to sci.stat.math.[7]   
Marsaglia, G. 2003, “Diehard Battery of Tests of Randomness v0.2 beta,” $^ { 2 0 0 7 + }$ at http://www.cs.hku.hk/\~diehard/.[8]   
Rukhin, A. et al. 2001, “A Statistical Test Suite for Random and Pseudorandom Number Generators”, NIST Special Publication 800-22 (revised to May 15, 2001).[9]   
Marsaglia, G. 2003, “Xorshift RNGs”, Journal of Statistical Software, vol. 8, no. 14, pp. 1-6.[10]   
Brent, R.P. 2004, “Note on Marsaglia’s Xorshift Random Number Generators”, Journal of Statistical Software, vol. 11, no.5,pp. 1-5.[11]   
L’Ecuyer, P. 1996, “Maximally Equidistributed Combined Tausworthe Generators,” Mathematics of Computation, vol. 65, pp. 203-213.[12]   
L’Ecuyer, P. 1999, “Tables of Maximally Equidistributed Combined LSFR Generators,” Mathematics of Computation, vol. 68,pp.261-269.[13]   
Couture, R. and L’Ecuyer, P. 1997, “Distribution Properties of Multiply-with-Carry Random Number Generators,” Mathematics of Computation, vol. 66, pp. 591-607.[14]   
L’Ecuyer, P. 1999, “Tables of Linear Congruential Generators of Different Sizes and Good Lattice Structure”, Mathematics of Computation, vol. 68, pp. 249-260.[15]

# 7.2 Completely Hashing a Large Array

We introduced the idea of a random hash or hash function in $\ S 7 . 1 . 4$ . Once in a while we might want a hash function that operates not on a single word, but on an entire array of length $M$ . Being perfectionists, we want every single bit in the hashed output array to depend on every single bit in the given input array. One way to achieve this is to borrow structural concepts from algorithms as unrelated as the Data Encryption Standard (DES) and the Fast Fourier Transform (FFT)!

DES, like its progenitor cryptographic system LUCIFER, is a so-called “block product cipher” [1]. It acts on 64 bits of input by iteratively applying (16 times, in fact) a kind of highly nonlinear bit-mixing function. Figure 7.2.1 shows the flow of information in DES during this mixing. The function $g$ , which takes 32 bits into 32 bits, is called the “cipher function.” Meyer and Matyas [1] discuss the importance of the cipher function being nonlinear, as well as other design criteria.

DES constructs its cipher function $g$ from an intricate set of bit permutations and table lookups acting on short sequences of consecutive bits. For our purposes, a different function $g$ that can be rapidly computed in a high-level computer language is preferable. Such a function probably weakens the algorithm cryptographically. Our purposes are not, however, cryptographic: We want to find the fastest $g$ , and the smallest number of iterations of the mixing procedure in Figure 7.2.1, such that our output random sequence passes the tests that are customarily applied to random number generators. The resulting algorithm is not DES, but rather a kind of “pseudo-DES,” better suited to the purpose at hand.

![](images/f474e184c1327ddc145b14df7a7602f396c3b79d5fe55008eb3edc52183cd8f6.jpg)  
Figure 7.2.1. The Data Encryption Standard (DES) iterates a nonlinear function $_ g$ on two 32-bit words, in the manner shown here (after Meyer and Matyas [1]).

Following the criterion mentioned above, that $g$ should be nonlinear, we must give the integer multiply operation a prominent place in $g$ . Confining ourselves to multiplying 16- bit operands into a 32-bit result, the general idea of $g$ is to calculate the three distinct 32- bit products of the high and low 16-bit input half-words, and then to combine these, and perhaps additional fixed constants, by fast operations (e.g., add or exclusive-or) into a single 32-bit result.

There are only a limited number of ways of effecting this general scheme, allowing systematic exploration of the alternatives. Experimentation and tests of the randomness of the output lead to the sequence of operations shown in Figure 7.2.2. The few new elements in the figure need explanation: The values $C _ { 1 }$ and $C _ { 2 }$ are fixed constants, chosen randomly with the constraint that they have exactly 16 1-bits and $^ { 1 6 0 }$ -bits; combining these constants via exclusive-or ensures that the overall $g$ has no bias toward 0- or 1-bits. The “reverse halfwords” operation in Figure 7.2.2 turns out to be essential; otherwise, the very lowest and very highest bits are not properly mixed by the three multiplications.

It remains to specify the smallest number of iterations $N _ { i t }$ that we can get away with. For purposes of this section, we recommend $N _ { i t } = 2$ . We have not found any statistical deviation from randomness in sequences of up to $1 0 ^ { 9 }$ random deviates derived from this scheme. However, we include $C _ { 1 }$ and $C _ { 2 }$ constants for $N _ { i t } \le 4$ .

# void psdes(Uint &lword, Uint &rword) {

Pseudo-DES hashing of the 64-bit word (lword,rword). Both 32-bit arguments are returned hashed on all bits.

const int NITER $^ { * 2 }$ ;   
static const Uint c1[4] ${ \boldsymbol { = } } \{$ 0xbaa96887L, 0x1e17d32cL, 0x03bcdc3cL, 0x0f33d1b2L};   
static const Uint c2[4] $= \downarrow$ 0x4b0f3b58L, 0xe874f0c3L, 0x6955c5a6L, 0x55a7ca46L};   
Uint i,ia,ib,iswap,itmph $\mathtt { \mathtt { = 0 } }$ ,itmpl $_ { = 0 }$ ;   
for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<NITER; $\mathbf { i } + + \mathbf { i }$ ) {   
Perform niter iterations of DES logic, using a simpler (noncryptographic) nonlinear func  
tion instead of DES’s. ia $=$ (iswap=rword) ^ c1[i]; The bit-rich constants c1 and (below) itmpl $=$ ia & 0xffff; c2 guarantee lots of nonlinear mixitmph $=$ ia >> 16; ing.

![](images/66847a2538c8d1b36330b778d3a3a83e2250cda8a4326340231c9ec2a83d1467.jpg)  
Figure 7.2.2. The nonlinear function $_ g$ used by the routine psdes.

ib=itmpl\*itmpl+ \~(itmph\*itmph); rword $=$ lword ^ (((ia $=$ (ib >> 16) ((ib & 0xffff) << 16)) ^ c2[i])+itmpl\*itmph); lword $=$ iswap; }

Thus far, this doesn’t seem to have much to do with completely hashing a large array. However, psdes gives us a building block, a routine for mutually hashing two arbitrary 32-bit integers. We now turn to the FFT concept of the butterfly to extend the hash to a whole array.

The butterfly is a particular algorithmic construct that applies to an array of length $N$ , a power of 2. It brings every element into mutual communication with every other element in about $N \log _ { 2 } N$ operations. A useful metaphor is to imagine that one array element has a disease that infects any other element with which it has contact. Then the butterfly has two properties of interest here: (i) After its $\log _ { 2 } N$ stages, everyone has the disease. Furthermore, (ii) after $j$ stages, $2 ^ { j }$ elements are infected; there is never an “eye of the needle” or “necking down” of the communication path.

The butterfly is very simple to describe: In the first stage, every element in the first half of the array mutually communicates with its corresponding element in the second half of the array. Now recursively do this same thing to each of the halves, and so on. We can see by induction that every element now has a communication path to every other one: Obviously it works when $N = 2$ . And if it works for $N$ , it must also work for $2 N$ , because the first step gives every element a communication path into both its own and the other half of the array, after which it has, by assumption, a path everywhere.

We need to modify the butterfly slightly, so that our array size $M$ does not have to be a power of 2. Let $N$ be the next larger power of 2. We do the butterfly on the (virtual) size $N$ , ignoring any communication with nonexistent elements larger than $M$ . This, by itself, doesn’t do the job, because the later elements in the first $N / 2$ were not able to “infect” the second $N / 2$ (and similarly at later recursive levels). However, if we do one extra communication between elements of the first $N / 2$ and second $N / 2$ at the very end, then all missing communication paths are restored by traveling through the first $N / 2$ elements.

The third line in the following code is an idiom that sets n to the next larger power of 2 greater or equal to m, a miniature masterpiece due to S.E. Anderson [2]. If you look closely, you’ll see that it is itself a sort of butterfly, but now on bits!

# void hashall(VecUint &arr) {

Replace the array arr by a same-sized hash, all of whose bits depend on all of the bits in arr.   
Uses psdes for the mutual hash of two 32-bit words.   
Int $\mathbb { m } =$ arr.size(), $\tt { n } { = } \tt { m } { - } 1$ ;   
$\mathrm { n } | = \mathrm { n } > > 1$ ; $n \left| = \mathrm { n } > > 2 \right.$ ; $\mathtt { n } | = \mathtt { n } > > 4$ ; $n \left| = \mathtt { n } > > 8 \right.$ ; n $_ 1 | = \mathtt { n } > > 1 6$ ; $\mathrm { \ n } { + } + $ ;   
Incredibly, n is now the next power of $2 \geq \mathtt { m }$ .   
Int nb=n,nb2=n>>1,j,jb;   
if $\scriptstyle \mathbf { n < 2 }$ ) throw("size must be $> ~ 1 "$ );   
while (nb $> ~ 1$ ) { for (jb=0;jb<n-nb+1;jb $+ =$ nb) for (j=0;j<nb2; ${ \dot { \mathrm { 3 } } } \mathrm { + + }$ ) if (jb+j+nb2 < m) psdes(arr[jb+j],arr[jb+j+nb2]); nb $=$ nb2; nb2 $> > = ~ 1$ ;   
n $\scriptstyle > 2 \ = \ n > > 1$ ;   
if (m $! = \mathrm { ~ \tt ~ n ~ } )$ ) for (j=nb2;j<m;j++) psdes(arr[j],arr[j-nb2]);   
Final mix needed only if m is not a power of 2.

# CITED REFERENCES AND FURTHER READING:

Meyer, C.H. and Matyas, S.M. 1982, Cryptography: A New Dimension in Computer Data Security (New York: Wiley).[1]

Zonst, A.E. 2000, Understanding the FFT, 2nd revised ed. (Titusville, FL: Citrus Press).

Anderson, S.E. 2005, “Bit Twiddling Hacks,” $^ { 2 0 0 7 + }$ at http://graphics.stanford.edu/ \~seander/bithacks.html .[2]

Data Encryption Standard,1977 January 15, Federal Information Processing Standards Publication, number 46 (Washington: U.S. Department of Commerce, National Bureau of Standards).

Guidelines forImplementing and Using the NBS Data Encryption Standard,1981 April1,Federal Information Processing Standards Publication, number 74 (Washington: U.S. Department of Commerce, National Bureau of Standards).

# 7.3 Deviates from Other Distributions

In $\ S 7 . 1$ we learned how to generate random deviates with a uniform probability between 0 and 1, denoted $\mathrm { U } ( 0 , 1 )$ . The probability of generating a number between $x$ and $x + d x$ is

$$
p ( x ) d x = { \left\{ \begin{array} { l l } { d x } & { 0 \leq x < 1 } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

and we write

$$
x \sim \mathrm { U } ( 0 , 1 )
$$

As in $\ S 6 . 1 4$ , the symbol $\sim$ can be read as “is drawn from the distribution.”

In this section, we learn how to generate random deviates drawn from other probability distributions, including all of those discussed in $\ S 6 . 1 4$ . Discussion of specific distributions is interleaved with the discussion of the general methods used.

# 7.3.1 Exponential Deviates

Suppose that we generate a uniform deviate $x$ and then take some prescribed function of it, $y ( x )$ . The probability distribution of $y$ , denoted $p ( y ) d y$ , is determined by the fundamental transformation law of probabilities, which is simply

$$
| p ( y ) d y | = | p ( x ) d x |
$$

or

$$
p ( y ) = p ( x ) \left| { \frac { d x } { d y } } \right|
$$

As an example, take

$$
y ( x ) = - \ln ( x )
$$

with $x \sim \mathrm { U } ( 0 , 1 )$ . Then

$$
p ( y ) d y = \left| { \frac { d x } { d y } } \right| d y = e ^ { - y } d y
$$

which is the exponential distribution with unit mean, Exponential .1/, discussed in $\ S 6 . 1 4 . 5$ . This distribution occurs frequently in real life, usually as the distribution of waiting times between independent Poisson-random events, for example the radioactive decay of nuclei. You can also easily see (from 7.3.6) that the quantity $y / \beta$ has the probability distribution $\beta e ^ { - \beta y }$ , so

$$
y / \beta \sim \mathrm { E x p o n e n t i a l } \left( \beta \right)
$$

We can thus generate exponential deviates at a cost of about one uniform deviate, plus a logarithm, per call.

struct Expondev : Ran {   
Structure for exponential deviates. Doub beta; Expondev(Doub bbeta, Ullong i) : Ran(i), beta(bbeta) {} Constructor arguments are $\beta$ and a random sequence seed. Doub dev() Return an exponential deviate. Doub u; do u $=$ doub(); while $\mathit { \Omega } _ { \lambda } ^ { ' } = = \mathit { \Omega } 0 . \mathit { \check { \Psi } } .$ ); return -log(u)/beta; }   
};

Our convention here and in the rest of this section is to derive the class for each kind of deviate from the uniform generator class Ran. We use the constructor to set the distribution’s parameters and set the initial seed for the generator. We then provide a method dev() that returns a random deviate from the distribution.

# 7.3.2 Transformation Method in General

Let’s see what is involved in using the above transformation method to generate some arbitrary desired distribution of $y$ ’s, say one with $p ( y ) ~ = ~ f ( y )$ for some positive function $f$ whose integral is 1. According to (7.3.4), we need to solve the differential equation

![](images/4d640d1cbe0a89b22cf2a074907ca7f56a5fad2dd37922fedd7a66f7bfdeae86.jpg)  
Figure 7.3.1. Transformation method for generating a random deviate $y$ from a known probability distribution $p ( y )$ . The indefinite integral of $p ( y )$ must be known and invertible. A uniform deviate $x$ is chosen between 0 and 1. Its corresponding $y$ on the definite-integral curve is the desired deviate.

$$
{ \frac { d x } { d y } } = f ( y )
$$

But the solution of this is just $x = F ( y )$ , where $F ( y )$ is the indefinite integral of $f ( y )$ . The desired transformation that takes a uniform deviate into one distributed as $f ( y )$ is therefore

$$
y ( x ) = F ^ { - 1 } ( x )
$$

where $F ^ { - 1 }$ is the inverse function to $F$ . Whether (7.3.9) is feasible to implement depends on whether the inverse function of the integral of $f ( y )$ is itself feasible to compute, either analytically or numerically. Sometimes it is, and sometimes it isn’t.

Incidentally, (7.3.9) has an immediate geometric interpretation: Since $F ( y )$ is the area under the probability curve to the left of $y$ , (7.3.9) is just the prescription: Choose a uniform random $x$ , then find the value $y$ that has that fraction $x$ of probability area to its left, and return the value $y$ . (See Figure 7.3.1.)

# 7.3.3 Logistic Deviates

Deviates from the logistic distribution, as discussed in $\ S 6 . 1 4 . 4$ , are readily generated by the transformation method, using equation (6.14.15). The cost is again dominated by one uniform deviate, and a logarithm, per logistic deviate.

struct Logisticdev : Ran   
Structure for logistic deviates. Doub mu,sig; Logisticdev(Doub mmu, Doub ssig, Ullong i) : Ran(i), mu(mmu), sig(ssig) {} Constructor arguments are $\mu , \sigma$ , and a random sequence seed. Doub dev() { Return a logistic deviate. Doub u; do u $=$ doub(); while $( \mathrm { u } * ( 1 \ : . - \mathrm { u } ) = = \ : 0 \ : . )$ ; return mu $^ +$ 0.551328895421792050\*sig\*log(u/(1.-u)); }   
};

# 7.3.4 Normal Deviates by Transformation (Box-Muller)

Transformation methods generalize to more than one dimension. If $x _ { 1 } , x _ { 2 } , \ldots$ are random deviates with a joint probability distribution $p ( x _ { 1 } , x _ { 2 } , . . . ) d x _ { 1 } d x _ { 2 } . . . .$ , and if $y _ { 1 } , y _ { 2 } , \ldots$ are each functions of all the $x$ ’s (same number of $y$ ’s as $x$ ’s), then the joint probability distribution of the $y$ ’s is

$$
p ( y _ { 1 } , y _ { 2 } , \ldots ) d y _ { 1 } d y _ { 2 } \ldots = p ( x _ { 1 } , x _ { 2 } , \ldots ) \left| { \frac { \partial ( x _ { 1 } , x _ { 2 } , \ldots ) } { \partial ( y _ { 1 } , y _ { 2 } , \ldots ) } } \right| d y _ { 1 } d y _ { 2 } \ldots
$$

where $| \partial ( \mathrm { ~  ~ \theta ~ } ) / \partial ( \mathrm { ~  ~ \theta ~ } ) |$ is the Jacobian determinant of the $x$ ’s with respect to the $y$ ’s (or the reciprocal of the Jacobian determinant of the $y$ ’s with respect to the $x$ ’s).

An important historical example of the use of (7.3.10) is the Box-Muller method for generating random deviates with a normal (Gaussian) distribution (-6.14.1):

$$
p ( y ) d y = \frac { 1 } { \sqrt { 2 \pi } } e ^ { - y ^ { 2 } / 2 } d y
$$

Consider the transformation between two uniform deviates on (0,1), $x _ { 1 } , x _ { 2 }$ , and two quantities $y _ { 1 } , y _ { 2 }$ ,

$$
\begin{array} { r } { y _ { 1 } = \sqrt { - 2 \ln x _ { 1 } } \cos 2 \pi x _ { 2 } } \\ { y _ { 2 } = \sqrt { - 2 \ln x _ { 1 } } \sin 2 \pi x _ { 2 } } \end{array}
$$

Equivalently we can write

$$
\begin{array} { l } { { \displaystyle x _ { 1 } = \exp \left[ - \frac { 1 } { 2 } ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) \right] } } \\ { { \displaystyle x _ { 2 } = \frac { 1 } { 2 \pi } \arctan \frac { y _ { 2 } } { y _ { 1 } } } } \end{array}
$$

Now the Jacobian determinant can readily be calculated (try it!):

$$
\frac { \partial ( x _ { 1 } , x _ { 2 } ) } { \partial ( y _ { 1 } , y _ { 2 } ) } = \left| \frac { \frac { \partial x _ { 1 } } { \partial y _ { 1 } } } { \frac { \partial x _ { 2 } } { \partial y _ { 1 } } } \right. \frac { \left. \frac { \partial x _ { 1 } } { \partial y _ { 2 } } \right| } { \left. \frac { \partial x _ { 2 } } { \partial y _ { 2 } } \right| } = - \left[ \frac { 1 } { \sqrt { 2 \pi } } e ^ { - y _ { 1 } ^ { 2 } / 2 } \right] \left[ \frac { 1 } { \sqrt { 2 \pi } } e ^ { - y _ { 2 } ^ { 2 } / 2 } \right]
$$

Since this is the product of a function of $y _ { 2 }$ alone and a function of $y _ { 1 }$ alone, we see that each $y$ is independently distributed according to the normal distribution (7.3.11).

One further trick is useful in applying (7.3.12). Suppose that, instead of picking uniform deviates $x _ { 1 }$ and $x _ { 2 }$ in the unit square, we instead pick $v _ { 1 }$ and $v _ { 2 }$ as the ordinate and abscissa of a random point inside the unit circle around the origin. Then the sum of their squares, $R ^ { 2 } \equiv v _ { 1 } ^ { 2 } + v _ { 2 } ^ { 2 }$ , is a uniform deviate, which can be used for $x _ { 1 }$ , while the angle that $( v _ { 1 } , v _ { 2 } )$ defines with respect to the $v _ { 1 }$ -axis can serve as the random angle $2 \pi x _ { 2 }$ . What’s the advantage? It’s that the cosine and sine in (7.3.12) can now be written as $v _ { 1 } / \sqrt { R ^ { 2 } }$ and $v _ { 2 } / \sqrt { R ^ { 2 } }$ , obviating the trigonometric function calls! (In the next section we will generalize this trick considerably.)

Code for generating normal deviates by the Box-Muller method follows. Consider it for pedagogical use only, because a significantly faster method for generating normal deviates is coming, below, in $\ S 7 . 3 . 9$ .

struct Normaldev_BM : Ran {   
Structure for normal deviates. Doub mu,sig; Doub storedval; Normaldev_BM(Doub mmu, Doub ssig, Ullong i) : Ran(i), mu(mmu), sig(ssig), storedval(0.) {} Constructor arguments are $\mu$ , $\sigma$ , and a random sequence seed. Doub dev( Return a normal deviate. Doub v1,v2,rsq,fac; if (storedval $\scriptstyle = = 0$ .) { We don’t have an extra deviate handy, so do { v1=2.0\*doub()-1.0; pick two uniform numbers in the square ex-$\mathtt { v } 2 = 2$ .0\*doub()-1.0; tending from $^ { - 1 }$ to $+ 1$ in each direction, rsq=v1\*v1+v2\*v2; see if they are in the unit circle, } while (rsq $> = ~ 1 . 0$ || $\mathtt { r s q } = = 0 . 0 )$ ; or try again. fac=sqrt(-2.0\*log(rsq)/rsq); Now make the $\mathsf { B o x }$ -Muller transformation to storedval $=$ v1\*fac; get two normal deviates. Return one and return mu $^ +$ sig\*v2\*fac; save the other for next time. } else { We have an extra deviate handy, fac $=$ storedval; storedval $\qquad = \ 0 .$ ; return mu $^ +$ sig\*fac; so return it. } }   
};

# 7.3.5 Rayleigh Deviates

The Rayleigh distribution is defined for positive $z$ by

$$
\begin{array} { r l r } { p ( z ) d z = z \exp \left( - \frac { 1 } { 2 } z ^ { 2 } \right) d z } & { { } } & { ( z > 0 ) } \end{array}
$$

Since the indefinite integral can be done analytically, and the result easily inverted, a simple transformation method from a uniform deviate $x$ results:

$$
z = \sqrt { - 2 \ln x } , \quad x \sim \mathrm { U } ( 0 , 1 )
$$

A Rayleigh deviate $z$ can also be generated from two normal deviates $y _ { 1 }$ and $y _ { 2 }$ by

$$
z = \sqrt { y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } } , \quad y _ { 1 } , y _ { 2 } \sim \mathrm { N } ( 0 , 1 )
$$

Indeed, the relation between equations (7.3.16) and (7.3.17) is immediately evident in the equation for the Box-Muller method, equation (7.3.12), if we square and sum that method’s two normal deviates $y _ { 1 }$ and $y _ { 2 }$ .

# 7.3.6 Rejection Method

The rejection method is a powerful, general technique for generating random deviates whose distribution function $p ( x ) d x$ (probability of a value occurring between $x$ and $x + d x ,$ ) is known and computable. The rejection method does not require that the cumulative distribution function (indefinite integral of $p ( x ) { \ddot { } }$ ) be readily computable, much less the inverse of that function — which was required for the transformation method in the previous section.

The rejection method is based on a simple geometrical argument (Figure 7.3.2):

![](images/7e9df5a5bc3f129e9e3f9da95c15d8d7888937fe57de8fbbc228f15a1ed03925.jpg)  
Figure 7.3.2. Rejection method for generating a random deviate $x$ from a known probability distribution $p ( x )$ that is everywhere less than some other function $f ( x )$ . The transformation method is first used to generate a random deviate $x$ of the distribution $f$ (compare Figure 7.3.1). A second uniform deviate is used to decide whether to accept or reject that $x$ . If it is rejected, a new deviate of $f$ is found, and so on. The ratio of accepted to rejected points is the ratio of the area under $p$ to the area between $p$ and $f$ .

Draw a graph of the probability distribution $p ( x )$ that you wish to generate, so that the area under the curve in any range of $x$ corresponds to the desired probability of generating an $x$ in that range. If we had some way of choosing a random point in two dimensions, with uniform probability in the area under your curve, then the $x$ value of that random point would have the desired distribution.

Now, on the same graph, draw any other curve $f ( x )$ that has finite (not infinite) area and lies everywhere above your original probability distribution. (This is always possible, because your original curve encloses only unit area, by definition of probability.) We will call this $f ( x )$ the comparison function. Imagine now that you have some way of choosing a random point in two dimensions that is uniform in the area under the comparison function. Whenever that point lies outside the area under the original probability distribution, we will reject it and choose another random point. Whenever it lies inside the area under the original probability distribution, we will accept it.

It should be obvious that the accepted points are uniform in the accepted area, so that their $x$ values have the desired distribution. It should also be obvious that the fraction of points rejected just depends on the ratio of the area of the comparison function to the area of the probability distribution function, not on the details of shape of either function. For example, a comparison function whose area is less than 2 will reject fewer than half the points, even if it approximates the probability function very badly at some values of $x$ , e.g., remains finite in some region where $p ( x )$ is zero.

It remains only to suggest how to choose a uniform random point in two dimensions under the comparison function $f ( x )$ . A variant of the transformation method $( \ S 7 . 3 )$ does nicely: Be sure to have chosen a comparison function whose indefinite integral is known analytically, and is also analytically invertible to give $x$ as a function of “area under the comparison function to the left of $x$ .” Now pick a uniform deviate between 0 and $A$ , where $A$ is the total area under $f ( x )$ , and use it to get a corresponding $x$ . Then pick a uniform deviate between 0 and $f ( x )$ as the $y$ value for the two-dimensional point. Finally, accept or reject according to whether it is respectively less than or greater than $p ( x )$ .

So, to summarize, the rejection method for some given $p ( x )$ requires that one find, once and for all, some reasonably good comparison function $f ( x )$ . Thereafter, each deviate generated requires two uniform random deviates, one evaluation of $f$ (to get the coordinate $y$ ) and one evaluation of $p$ (to decide whether to accept or reject the point $x , y )$ . Figure 7.3.1 illustrates the whole process. Then, of course, this process may need to be repeated, on the average, $A$ times before the final deviate is obtained.

# 7.3.7 Cauchy Deviates

The “further trick” described following equation (7.3.14) in the context of the Box-Muller method is now seen to be a rejection method for getting trigonometric functions of a uniformly random angle. If we combine this with the explicit formula, equation (6.14.6), for the inverse cdf of the Cauchy distribution (see $\ S 6 . 1 4 . 2 )$ , we can generate Cauchy deviates quite efficiently.

# struct Cauchydev : Ran {

Structure for Cauchy deviates. Doub mu,sig; Cauchydev(Doub mmu, Doub ssig, Ullong i) : Ran(i), mu(mmu), sig(ssig) {} Constructor arguments are $\mu$ , $\sigma$ , and a random sequence seed. Doub dev() { Return a Cauchy deviate. Doub v1,v2; do { Find a random point in the unit semicircle. $\scriptstyle \mathtt { v 1 } = 2$ .0\*doub()-1.0; $\mathtt { v } 2 =$ doub(); } while (SQR(v1)+SQR(v2) $> = ~ 1$ . || $\mathrm { v } 2 \ \mathrm { = } \ 0 . )$ ; return mu $^ +$ sig\*v1/v2; Ratio of its coordinates is the tangent of a } random angle.   
};

# 7.3.8 Ratio-of-Uniforms Method

In finding Cauchy deviates, we took the ratio of two uniform deviates chosen to lie within the unit circle. If we generalize to shapes other than the unit circle, and combine it with the principle of the rejection method, a powerful variant emerges. Kinderman and Monahan [1] showed that deviates of virtually any probability distribution $p ( x )$ can be generated by the following rather amazing prescription:

- Construct the region in the $( u , v )$ plane bounded by $0 \leq u \leq [ p ( v / u ) ] ^ { 1 / 2 }$ .   
- Choose two deviates, $u$ and $v$ , that lie uniformly in this region.   
- Return $v / u$ as the deviate.

Proof: We can represent the ordinary rejection method by the equation in the $( x , p )$ plane,

$$
p ( x ) d x = \int _ { p ^ { \prime } = 0 } ^ { p ^ { \prime } = p ( x ) } d p ^ { \prime } d x
$$

Since the integrand is 1, we are justified in sampling uniformly in $( x , p ^ { \prime } )$ as long as $p ^ { \prime }$ is within the limits of the integral (that is, $0 < p ^ { \prime } < p ( x ) )$ . Now make the change of variable

$$
\begin{array} { c } { { \frac { v } { u } = x } } \\ { { u ^ { 2 } = p } } \end{array}
$$

![](images/254c323f805148e7f7de3807ac2ddd1569c822d606e2afd039177c2eb42979e2.jpg)  
Figure 7.3.3. Ratio-of-uniforms method. The interior of this teardrop shape is the acceptance region for the normal distribution: If a random point is chosen inside this region, then the ratio $v / u$ will be a normal deviate.

Then equation (7.3.18) becomes

$$
p ( x ) d x = \int _ { p ^ { \prime } = 0 } ^ { p ^ { \prime } = p ( x ) } d p ^ { \prime } d x = \int _ { u = 0 } ^ { u = \sqrt { p ( x ) } } \frac { \partial ( p , x ) } { \partial ( u , v ) } d u d v = 2 \int _ { u = 0 } ^ { u = \sqrt { p ( v / u ) } } d u d v
$$

because (as you can work out) the Jacobian determinant is the constant 2. Since the new integrand is constant, uniform sampling in $( u , v )$ with the limits indicated for $u$ is equivalent to the rejection method in $( x , p )$ .

The above limits on $u$ very often define a region that is “teardrop” shaped. To see why, note that the locii of constant $x = v / u$ are radial lines. Along each radial, the acceptance region goes from the origin to a point where $u ^ { 2 } = p ( x )$ . Since most probability distributions go to zero for both large and small $x$ , the acceptance region accordingly shrinks toward the origin along radials, producing a teardrop. Of course, it is the exact shape of this teardrop that matters. Figure 7.3.3 shows the shape of the acceptance region for the case of the normal distribution.

Typically this ratio-of-uniforms method is used when the desired region can be closely bounded by a rectangle, parallelogram, or some other shape that is easy to sample uniformly. Then, we go from sampling the easy shape to sampling the desired region by rejection of points outside the desired region.

An important adjunct to the ratio-of-uniforms method is the idea of a squeeze. A squeeze is any easy-to-compute shape that tightly bounds the region of acceptance of a rejection method, either from the inside or from the outside. Best of all is when you have squeezes on both sides. Then you can immediately reject points that are outside the outer squeeze and immediately accept points that are inside the inner squeeze. Only when you have the bad luck of drawing a point between the two squeezes do you actually have to do the more lengthy computation of comparing with the actual rejection boundary. Squeezes are useful both in the ordinary rejection method and in the ratio-of-uniforms method.

# 7.3.9 Normal Deviates by Ratio-of-Uniforms

Leva [2] has given an algorithm for normal deviates that uses the ratio-of-uniforms method with great success. He uses quadratic curves to provide both inner and outer squeezes that hug the desired region in the $( u , v )$ plane (Figure 7.3.3). Only about $1 \%$ of the time is it necessary to calculate an exact boundary (requiring a logarithm).

The resulting code looks so simple and “un-transcendental” that it may be hard to believe that exact normal deviates are generated. But they are!

struct Normaldev : Ran {   
Structure for normal deviates. Doub mu,sig; Normaldev(Doub mmu, Doub ssig, Ullong i) : Ran(i), mu(mmu), sig(ssig){} Constructor arguments are $\mu , \sigma$ , and a random sequence seed. Doub dev() { Return a normal deviate. Doub u,v,x,y,q; do { $u \ =$ doub(); $\qquad \mathtt { v } =$ 1.7156\*(doub()-0.5); x = u - 0.449871; $\mathtt { y } =$ abs(v) $^ +$ 0.386595; q = SQR(x) $^ +$ y\*(0.19600\*y-0.25472\*x); while (q > 0.27597 && (q $>$ 0.27846 || SQR(v) > -4.\*log(u)\*SQR(u))); return mu $^ +$ sig\*v/u; }   
};

Note that the while clause makes use of C’s (and $\mathrm { C } { + + }$ ’s) guarantee that logical expressions are evaluated conditionally: If the first operand is sufficient to determine the outcome, the second is not evaluated at all. With these rules, the logarithm is evaluated only when q is between 0:27597 and 0:27846.

On average, each normal deviate uses 2.74 uniform deviates. By the way, even though the various constants are given only to six digits, the method is exact (to full double precision). Small perturbations of the bounding curves are of no consequence. The accuracy is implicit in the (rare) evaluations of the exact boundary.

# 7.3.10 Gamma Deviates

The distribution $\mathrm { G a m m a } ( \alpha , \beta )$ was described in $\ S 6 . 1 4 . 9$ . The $\beta$ parameter enters only as a scaling,

$$
\mathrm { G a m m a } ( \alpha , \beta ) \cong \frac { 1 } { \beta } \mathrm { G a m m a } ( \alpha , 1 )
$$

(Translation: To generate a $\mathrm { G a m m a } ( \alpha , \beta )$ deviate, generate a $\mathrm { G a m m a } ( \alpha , 1 )$ deviate and divide it by $\beta$ .)

If $\alpha$ is a small positive integer, a fast way to generate $x \sim \mathrm { G a m m a } ( \alpha , 1 )$ is to use the fact that it is distributed as the waiting time to the $\alpha$ th event in a Poisson random process of unit mean. Since the time between two consecutive events is just the exponential distribution Exponential .1/, you can simply add up $\alpha$ exponentially distributed waiting times, i.e., logarithms of uniform deviates. Even better, since the sum of logarithms is the logarithm of the product, you really only have to compute the product of $a$ uniform deviates and then take the log. Because this is such a special case, however, we don’t include it in the code below.

When $\alpha < 1$ , the gamma distribution’s density function is not bounded, which is inconvenient. However, it turns out [4] that if

$$
y \sim \mathrm { G a m m a } ( \alpha + 1 , 1 ) , \qquad u \sim \mathrm { U n i f o r m } ( 0 , 1 )
$$

then

$$
y u ^ { 1 / \alpha } \sim \mathrm { G a m m a } ( \alpha , 1 )
$$

We will use this in the code below.

For $\alpha > 1$ , Marsaglia and Tsang [5] give an elegant rejection method based on a simple transformation of the gamma distribution combined with a squeeze. After transformation, the gamma distribution can be bounded by a Gaussian curve whose area is never more than $5 \%$ greater than that of the gamma curve. The cost of a gamma deviate is thus only a little more than the cost of the normal deviate that is used to sample the comparison function. The following code gives the precise formulation; see the original paper for a full explanation.

# struct Gammadev : Normaldev {

Structure for gamma deviates.

Doub alph, oalph, bet; Doub a1,a2; Gammadev(Doub aalph, Doub bbet, Ullong i) : Normaldev $( 0 . , 1 . , \mathrm { i } )$ , alph(aalph), oalph(aalph), bet(bbet) { Constructor arguments are $\pmb { \alpha }$ , $\beta$ , and a random sequence seed. if (alph $< = ~ 0 .$ ) throw("bad alph in Gammadev"); if (alph $< ~ 1 .$ ) alph $+ = \textit { 1 } .$ ; a1 $=$ alph-1./3.; $\mathsf { a } 2 \ = \ 1$ ./sqrt(9.\*a1); } Doub dev() { Return a gamma deviate by the method of Marsaglia and Tsang. Doub u,v,x; do { do { $_ { \textrm { x } } =$ Normaldev::dev(); $\ l { \textsc { v } } = \ l { \textsc { 1 } }$ . + a2\*x; } while $\mathit { \Pi } _ { \mathbf { v } } \ < = \ 0 . )$ ; $\mathrm { ~ v ~ } = \mathrm { ~ v * v * v } ;$ $u \ =$ doub(); } while $\texttt { u } > 1$ . - 0.331 $^ *$ SQR(SQR(x)) && log(u) $>$ 0.5\*SQR(x) $^ +$ a1\*(1.-v+log(v))); Rarely evaluated. if (alph $= =$ oalph) return a1\*v/bet; else { Case where $\alpha < 1$ , per Ripley. do $\mathbf { u } =$ doub(); while $\mathrm {  ~ u ~ } = = 0 .$ ); return pow(u,1./oalph)\*a1\*v/bet; } } };

There exists a sum rule for gamma deviates. If we have a set of independent deviates $y _ { i }$ with possibly different $\alpha _ { i }$ ’s, but sharing a common value of $\beta$ ,

$$
y _ { i } \sim \mathrm { G a m m a } ( \alpha _ { i } , \beta )
$$

then their sum is also a gamma deviate,

$$
y \equiv \sum _ { i } y _ { i } \sim \mathrm { G a m m a } ( \alpha _ { T } , \beta ) , \qquad \alpha _ { T } = \sum _ { i } \alpha _ { i }
$$

If the $\alpha _ { i }$ ’s are integers, you can see how this relates to the discussion of Poisson waiting times above.

# 7.3.11 Distributions Easily Generated by Other Deviates

From normal, gamma and uniform deviates, we get a bunch of other distributions for free. Important: When you are going to combine their results, be sure that all distinct instances of Normaldist, Gammadist, and Ran have different random seeds! (Ran and its derived classes are sufficiently robust that seeds $i , i + 1 , \ldots$ are fine.)

# Chi-Square Deviates (cf. -6.14.8)

This one is easy:

$$
\mathrm { C h i s q u a r e } ( \nu ) \cong \mathrm { G a m m a } \Big ( \frac { \nu } { 2 } , \frac { 1 } { 2 } \Big ) \cong 2 \mathrm { G a m m a } \Big ( \frac { \nu } { 2 } , 1 \Big )
$$

# Student-t Deviates (cf. -6.14.3)

Deviates from the Student-t distribution can be generated by a method very similar to the Box-Muller method. The analog of equation (7.3.12) is

$$
y = \sqrt { \nu ( u _ { 1 } ^ { - 2 / \nu } - 1 ) } \cos { 2 \pi u _ { 2 } }
$$

If $u _ { 1 }$ and $u _ { 2 }$ are independently uniform, $\mathbf { U } ( 0 , 1 )$ , then

$$
y \sim \mathrm { S t u d e n t } ( \nu , 0 , 1 )
$$

or

$$
\mu + \sigma y \sim \mathrm { S t u d e n t } ( \nu , \mu , \sigma )
$$

Unfortunately, you can’t do the Box-Muller trick of getting two deviates at a time, because the Jacobian determinant analogous to equation (7.3.14) does not factorize. You might want to use the polar method anyway, just to get cos $2 \pi u _ { 2 }$ , but its advantage is now not so large.

An alternative method uses the quotients of normal and gamma deviates. If we have

$$
x \sim \mathrm { N } ( 0 , 1 ) , \qquad y \sim \mathrm { G a m m a } \Big ( \frac { \nu } { 2 } , \frac { 1 } { 2 } \Big )
$$

then

$$
x \sqrt { \nu / y } \sim \mathrm { S t u d e n t } ( \nu , 0 , 1 )
$$

Beta Deviates (cf. -6.14.11)

If

$$
x \sim \operatorname { G a m m a } ( \alpha , 1 ) , \qquad y \sim \operatorname { G a m m a } ( \beta , 1 )
$$

then

$$
\frac { x } { x + y } \sim \operatorname { B e t a } ( \alpha , \beta )
$$

# F-Distribution Deviates (cf. -6.14.10)

If

$$
\begin{array} { r } { x \sim \mathrm { B e t a } ( \frac { 1 } { 2 } \nu _ { 1 } , \frac { 1 } { 2 } \nu _ { 2 } ) } \end{array}
$$

(see equation 7.3.33), then

$$
\frac { \nu _ { 2 } x } { \nu _ { 1 } ( 1 - x ) } \sim \mathrm { F } ( \nu _ { 1 } , \nu _ { 2 } )
$$

![](images/4462aa9a4a983a6ea4e9de77058ac7a346c9b9d615d9f3dd944c0a604de04c48.jpg)  
Figure 7.3.4. Rejection method as applied to an integer-valued distribution. The method is performed on the step function shown as a dashed line, yielding a real-valued deviate. This deviate is rounded down to the next lower integer, which is output.

# 7.3.12 Poisson Deviates

The Poisson distribution, Poisson $( \lambda )$ , previously discussed in $\ S 6 . 1 4 . 1 3$ , is a discrete distribution, so its deviates will be integers, $k$ . To use the methods already discussed, it is convenient to convert the Poisson distribution into a continuous distribution by the following trick: Consider the finite probability $p ( k )$ as being spread out uniformly into the interval from $k$ to $k + 1$ . This defines a continuous distribution $q _ { \lambda } ( k ) d k$ given by

$$
q _ { \lambda } ( k ) d k = \frac { \lambda ^ { \lfloor k \rfloor } e ^ { - \lambda } } { \lfloor k \rfloor ! } d k
$$

where $\lfloor k \rfloor$ represents the largest integer $\leq k$ . If we now use a rejection method, or any other method, to generate a (noninteger) deviate from (7.3.36), and then take the integer part of that deviate, it will be as if drawn from the discrete Poisson distribution. (See Figure 7.3.4.) This trick is general for any integer-valued probability distribution. Instead of the “floor” operator, one can equally well use “ceiling” or “nearest” — anything that spreads the probability over a unit interval.

For $\lambda$ large enough, the distribution (7.3.36) is qualitatively bell-shaped (albeit with a bell made out of small, square steps). In that case, the ratio-of-uniforms method works well. It is not hard to find simple inner and outer squeezes in the $( u , v )$ plane of the form $v ^ { 2 } = Q ( u )$ , where $Q ( u )$ is a simple polynomial in $u$ . The only trick is to allow a big enough gap between the squeezes to enclose the true, jagged, boundaries for all values of $\lambda$ . (Look ahead to Figure 7.3.5 for a similar example.)

For intermediate values of $\lambda$ , the jaggedness is so large as to render squeezes impractical, but the ratio-of-uniforms method, unadorned, still works pretty well.

For small $\lambda$ , we can use an idea similar to that mentioned above for the gamma distribution in the case of integer $a$ . When the sum of independent exponential deviates first exceeds $\lambda$ , their number (less 1) is a Poisson deviate $k$ . Also, as explained for the gamma distribution, we can multiply uniform deviates from $\mathrm { U } ( 0 , 1 )$ instead of adding deviates from Exponential .1/.

These ideas produce the following routine.

ct Poissondev : Ran {   
cture for Poisson deviates.   
Doub lambda, sqlam, loglam, lamexp, lambold;   
VecDoub logfact;   
Int swch;   
Poissondev(Doub llambda, Ullong i) : Ran(i), lambda(llambda), logfact(1024,-1.), lambold(-1.) {}   
Constructor arguments are  and a random sequence seed.   
Int dev()   
Return a Poisson deviate using the most recently set value of . Doub u,u2,v,v2,p,t,lfac; Int k; if (lambda $< ~ 5 .$ ) { Will use product of uniforms method if (lambda $\downarrow =$ lambold) lamexp $\mid =$ exp(-lambda); $\mathrm { ~ k ~ } = \mathrm { ~ - 1 ~ }$ ; t=1.; do { ++k; t $\ast =$ doub(); } while (t > lamexp); } else { Will use ratio-of-uniforms method. if (lambda $\downarrow =$ lambold) { sqlam $=$ sqrt(lambda); loglam $=$ log(lambda); for (;;) { $\mathrm { ~ \textbar ~ { ~ u ~ } ~ } =$ 0.64\*doub(); v = -0.68 $^ +$ 1.28\*doub(); if (lambda $>$ 13.5) { Outer squeeze for fast rejection. $\quad \mathtt { v } 2 =$ SQR(v); if ( $\mathrm {  ~ v ~ } > = \mathrm {  ~ 0 ~ }$ .) {if $( \mathtt { v } 2 \ > \ 6 . 5 * \mathtt { u } * ( 0 . 6 4 \mathrm { - } \mathtt { u } ) * ( \mathtt { u } + 0 . 2 )$ ) continue;} else {if $( \nu 2 \ > \ 9 . 6 { \ast } { \mu } * ( 0 . 6 6 { - \mu } ) * ( \mu + 0 . 0 7 ) )$ continue;} } $\mathrm { ~ \bf ~ k ~ } =$ Int(floor(sqlam\*(v/u)+lambda+0.5)); if (k < 0) continue; u2 $=$ SQR(u); if (lambda $>$ 13.5) { Inner squeeze for fast acceptance. if ( $\mathrm {  ~ v ~ } > = \mathrm {  ~ 0 ~ }$ .) {if $( \mathrm { v } 2 ~ < ~ 1 5 . 2 { * } \mathrm { u } 2 { * } ( 0 . 6 1 \mathrm { - } \mathrm { u } ) { * } ( 0 . 8 \mathrm { - } \mathrm { u } ) )$ ) break;} else {if $( \mathrm { v } 2 ~ < ~ 6 . 7 6 * \mathrm { u } 2 * ( 0 . 6 2 \mathrm { - u } ) * ( 1 . 4 \mathrm { - u } )$ ) break;} } if $( \mathrm { ~ k ~ } < \mathrm { ~ } 1 0 2 4 )$ { if (logfact[k] < 0.) logfact[k] $=$ gammln(k+1.); lfac $=$ logfact[k]; } else lfac $=$ gammln(k+1.); $\mathtt { p } \ =$ sqlam\*exp(-lambda $^ +$ k\*loglam - lfac); Only when we must. if $\mathtt { . u 2 } < \mathtt { p } )$ break; } lambold $=$ lambda; return k;   
Int dev(Doub llambda) {   
Reset  and then return a Poisson deviate. lambda $=$ llambda; return dev();

![](images/8935ba798ee6987b47fdd2776be2e58e9bf81868a8338b3aba7936676d732b34.jpg)  
Figure 7.3.5. Ratio-of-uniforms method as applied to the generation of binomial deviates. Points are chosen randomly in the $( u , v )$ -plane. The smooth curves are inner and outer squeezes. The jagged curves correspond to various binomial distributions with $n > 6 4$ and $n p > 3 0$ . An evaluation of the binomial probability is required only when the random point falls between the smooth curves.

In the regime $\lambda > 1 3 . 5$ , the above code uses about 3:3 uniform deviates per output Poisson deviate and does 0:4 evaluations of the exact probability (costing an exponential and, for large $k$ , a call to gammln).

Poissondev is slightly faster if you draw many deviates with the same value $\lambda$ , using the dev function with no arguments, than if you vary $\lambda$ on each call, using the one-argument overloaded form of dev (which is provided for just that purpose). The difference is just an extra exponential $\lambda < 5$ ) or square root and logarithm $\lambda \geq 5$ ). Note also the object’s table of previously computed log-factorials. If your $\lambda$ ’s are as large as $\sim 1 0 ^ { 3 }$ , you might want to make the table larger.

# 7.3.13 Binomial Deviates

The generation of binomial deviates $k \ \sim \ \mathrm { B i n o m i a l } ( n , p )$ involves many of the same ideas as for Poisson deviates. The distribution is again integer-valued, so we use the same trick to convert it into a stepped continuous distribution. We can always restrict attention to the case $p \leq 0 . 5$ , since the distribution’s symmetries let us trivially recover the case $p > 0 . 5$ .

When $n > 6 4$ and $n p > 3 0$ , we use the ratio-of-uniforms method, with squeezes shown in Figure 7.3.5. The cost is about 3:2 uniform deviates, plus 0:4 evaluations of the exact probability, per binomial deviate.

It would be foolish to waste much thought on the case where $n \ > \ 6 4$ and $n p < 3 0$ , because it is so easy simply to tabulate the cdf, say for $0 \leq k < 6 4$ , and then loop over $k$ ’s until the right one is found. (A bisection search, implemented below, is even better.) With a cdf table of length 64, the neglected probability at the end of the table is never larger than $\sim 1 0 ^ { - 2 0 }$ . (At $1 0 ^ { 9 }$ deviates per second, you could run 3000 years before losing a deviate.)

What is left is the interesting case $n < 6 4$ , which we will explore in some detail, because it demonstrates the important concept of bit-parallel random comparison.

Analogous to the methods for gamma deviates with small integer $a$ and for Poisson deviates with small $\lambda$ , is this direct method for binomial deviates: Generate $n$ uniform deviates in $\mathrm { U } ( 0 , 1 )$ . Count the number of them $< p$ . Return the count as $k \sim \mathrm { B i n o m i a l } ( n , p )$ . Indeed this is essentially the definition of a binomial process!

The problem with the direct method is that it seems to require $n$ uniform deviates, even when the mean value of $k$ is much smaller. Would you be surprised if we told you that for $n \leq 6 4$ you can achieve the same goal with at most seven 64-bit uniform deviates, on average? Here is how.

Expand $p < 1$ into its first 5 bits, plus a residual,

$$
p = b _ { 1 } 2 ^ { - 1 } + b _ { 2 } 2 ^ { - 2 } + \cdots + b _ { 5 } 2 ^ { - 5 } + p _ { r } 2 ^ { - 5 }
$$

where each $b _ { i }$ is 0 or 1, and $0 \leq p _ { r } \leq 1$ .

Now imagine that you have generated and stored 64 uniform $\mathbf { U } ( 0 , 1 )$ deviates, and that the 64-bit word $P$ displays just the first bit of each of the 64. Compare each bit of $P$ to $b _ { 1 }$ . If the bits are the same, then we don’t yet know whether that uniform deviate is less than or greater than $p$ . But if the bits are different, then we know that the generator is less than $p$ (in the case that $b _ { 1 } = 1$ ) or greater than $p$ (in the case that $b _ { 1 } = 0 \}$ ). If we keep a mask of “known” versus “unknown” cases, we can do these comparisons in a bit-parallel manner by bitwise logical operations (see code below to learn how). Now move on to the second bit, $b _ { 2 }$ , in the same way. At each stage we change half the remaining unknowns to knowns. After five stages (for $n = 6 4 .$ ) there will be two remaining unknowns, on average, each of which we finish off by generating a new uniform and comparing it to $p _ { r }$ . (This requires a loop through the 64 bits; but since $\mathrm { C } { + } { + }$ has no bitwise “popcount” operation, we are stuck doing such a loop anyway. If you can do popcounts, you may be better off just doing more stages until the unknowns mask is zero.)

The trick is that the bits used in the five stages are not actually the leading five bits of 64 generators, they are just five independent 64-bit random integers. The number five was chosen because it minimizes $\overline { { 6 4 } } \times 2 ^ { - j } + j$ , the expected number of deviates needed.

So, the code for binomial deviates ends up with three separate methods: bitparallel direct, cdf lookup (by bisection), and squeezed ratio-of-uniforms.

truct Binomialdev : Ran {   
tructure for binomial deviates. Doub pp,p,pb,expnp,np,glnp,plog,pclog,sq; Int n,swch; Ullong uz,uo,unfin,diff,rltp; Int pbits[5]; Doub cdf[64]; Doub logfact[1024]; Binomialdev(Int nn, Doub ppp, Ullong i) : Ran(i), pp(ppp), n(nn) { Constructor arguments are $_ n$ , $p$ , and a random sequence seed. Int j; pb $= \mathrm { ~ p ~ } = \mathrm { ~ ( p p ~ } < = \mathrm { ~ 0 ~ . 5 ~ : ~ } \mathrm { ~ p p ~ } : \mathrm { ~ 1 ~ . 0 \mathrm { - p p } ) ~ } ;$ if $( \mathrm { ~ n ~ } < = \ 6 4 )$ ) { Will use bit-parallel direct method. $\mathtt { u } z = 0$ ; uo $=$ 0xffffffffffffffffLL; $\tt r l t p = 0$ ; for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<5;j++) pbits[j] = 1 & ((Int)(pb \*= 2.)); pb $- =$ floor(pb); Leading bits of $p$ (above) and remaining swch $\mathit { \Theta } = \mathit { \Theta } 0$ ; fraction. } else if $( \mathtt { n } * \mathtt { p } \ < \ 3 0 .$ ) { Will use precomputed cdf table. cdf[0] $=$ exp(n\*log(1-p)); for ( $\mathrm { j } = 1$ ;j<64;j++) cdf[j] $=$ cdf[j-1] $^ +$ exp(gammln $( \mathtt { n } + 1$ .) -gammln(j+1.)-gammln(n-j+1.)+j\*log(p)+(n-j)\*log(1.-p)); swch $\ c = ~ 1$ ;   
} else { Will use ratio-of-uniforms method. np = n\*p; glnp=gammln(n+1.); plog=log(p); pclog=log(1.-p); sq=sqrt(np\*(1.-p)); if (n $<$ 1024) for ( $\scriptstyle \mathrm { j = 0 }$ ;j $< = \mathtt { n }$ ;j++) logfact[j] $=$ gammln(j+1.); swch $= ~ 2$ ;   
}   
dev() {   
turn a binomial deviate.   
Int j,k,kl,km;   
Doub y,u,v,u2,v2,b;   
if (swch $\scriptstyle = = 0$ ) { unfin $=$ uo; Mark all bits as ”unfinished.” for (j ${ = } 0$ ;j<5;j++) { Compare with first five bits of $p$ diff $=$ unfin & (int64()^(pbits[j]? uo : uz)); Mask of diff. if (pbits[j]) rltp $| =$ diff; Set bits to 1, meaning ran $< p$ . else rltp $=$ rltp & \~diff; Set bits to 0, meaning ran $> p$ . unfin $=$ unfin & \~diff; Update unfinished status. } $\mathtt { k } = 0$ ; Now we just count the events. for (j ${ = } 0$ ;j<n;j++) { if (unfin & 1) {if (doub() $<$ pb) $+ + \mathrm { k } ; \}$ Clean up unresolved ca else {if (rltp & 1) ++k;} or use bit answer. unfin $> > = ~ 1$ ; rltp >>= 1;   
} else if (swch $\scriptstyle \mathbf { \mu = } \mathbf { \mu 1 }$ ) { Use stored cdf. $\mathrm { ~ y ~ } =$ doub(); $\mathbf { k } \mathbf { 1 } ~ = ~ - 1$ ; $\mathrm { ~ k ~ } = \ 6 4$ ; while (k-kl>1) { $\begin{array} { r l } { \mathrm { k m } } & { { } = \begin{array} { r l } { \left( \mathrm { k } \mathrm { 1 } { + } \mathrm { k } \right) / 2 \ } \end{array} } \end{array}$ ; if (y $<$ cdf[km]) $\texttt { k } = \texttt { k m }$ ; else $\mathtt { k 1 } \ = \ \mathtt { k m }$ ; }   
} else { Use ratio-of-uniforms method. for (;;) { $\mathrm { ~ \tt ~ u ~ } = \mathrm { ~ 0 ~ }$ .645\*doub(); v = -0.63 $^ +$ 1.25\*doub(); $\mathrm { v } 2 \ = \ \mathrm { S Q R } ( \mathrm { v } )$ ; Try squeeze for fast rejection: if $\begin{array} { r } { \mathrm { ~  ~ \omega ~ } } \\ { \nabla \mathrm { ~  ~ \omega ~ } } \end{array} > = \mathrm { ~  ~ 0 ~ } .$ ) {if $( \mathtt { v } 2 \ > \ 6 . 5 * \mathtt { u } * ( 0 . 6 4 5 \mathtt { - u } ) * ( \mathtt { u } + 0 . 2 )$ ) continue;} else {if $( \mathrm { v } 2 ) 8 . 4 \ast \mathrm { u } \ast ( 0 . 6 4 5 \mathrm { - u } ) \ast ( \mathrm { u } + 0 . 1 ) ^ { \cdot }$ ) continue;} $\mathrm { ~ \bf ~ k ~ } =$ Int(floor $( \mathtt { s q } \ast ( \mathtt { v } / \mathtt { u } ) + \mathtt { n p } + 0 . 5 ) )$ ; if $\mathrm { ~ ( ~ k ~ < ~ } 0 \mathrm { ~ ) ~ }$ ) continue; $\tt { u } 2 \ =$ SQR(u); Try squeeze for fast acceptance: if $\begin{array} { r } { \check { \mathbf { \Xi } } _ { \mathbb { V } } \ > = \ 0 . } \end{array}$ ) {if $( \nu 2 ~ < ~ 1 2 . 2 5 * \mathrm { u } 2 * ( 0 . 6 1 5 \mathrm { - u } ) * ( 0 . 9 2 \mathrm { - u } ) ^ { } )$ ) break;} else {if $( \mathtt { v } 2 ~ < ~ 7 . 8 4 \mathtt { * u } 2 \mathtt { * } ( 0 . 6 1 5 \mathtt { - u } ) \mathtt { * } ( 1 . 2 \mathtt { - u } )$ ) break;} b $=$ sq\*exp(glnp+k\*plog+(n-k)\*pclog Only when we must. - (n < 1024 ? logfact[k]+logfact[n-k] : gammln(k+1.)+gammln(n-k+1.))); if (u2 < b) break; }   
}   
if (p != pp) k = n - k;   
return k;

If you are in a situation where you are drawing only one or a few deviates each for many different values of $n$ and/or $p$ , you’ll need to restructure the code so that $n$ and $p$ can be changed without creating a new instance of the object and without reinitializing the underlying Ran generator.

# 7.3.14 When You Need Greater Speed

In particular situations you can cut some corners to gain greater speed. Here are some suggestions.

- All of the algorithms in this section can be speeded up significantly by using Ranq1 in $\ S 7 . 1$ instead of Ran. We know of no reason not to do this. You can gain some further speed by coding Ranq1’s algorithm inline, thus eliminating the function calls.   
- If you are using Poissondev or Binomialdev with large values of $\lambda$ or $n$ , then the above codes revert to calling gammln, which is slow. You can instead increase the length of the stored tables.   
- For Poisson deviates with $\lambda < 2 0$ , you may want to use a stored table of cdfs combined with bisection to find the value of $k$ . The code in Binomialdev shows how to do this.   
- If your need is for binomial deviates with small $n$ , you can easily modify the code in Binomialdev to get multiple deviates $( \sim 6 4 / n$ , in fact) from each execution of the bit-parallel code.   
Do you need exact deviates, or would an approximation do? If your distribution of interest can be approximated by a normal distribution, consider substituting Normaldev, above, especially if you also code the uniform random generation inline.   
If you sum exactly 12 uniform deviates $U ( 0 , 1 )$ and then subtract 6, you get a pretty good approximation of a normal deviate $N ( 0 , 1 )$ . This is definitely slower then Normaldev (not to mention less accurate) on a general-purpose CPU. However, there are reported to be some special-purpose signal processing chips in which all the operations can be done with integer arithmetic and in parallel.

See Gentle [3], Ripley [4], Devroye [6], Bratley [7], and Knuth [8] for many additional algorithms.

# CITED REFERENCES AND FURTHER READING:

Kinderman, A.J. and Monahan, J.F 1977, “Computer Generation of Random Variables Using the Ratio of Uniform Deviates,” ACM Transactions on Mathematical Software, vol. 3, pp. 257– 260.[1]   
Leva, J.L. 1992. “A Fast Normal Random Number Generator,” ACM Transactions on Mathematical Software,vol.18, no.4, pp. 449-453.[2]   
Gentle, J.E. 2003, Random Number Generation and Monte Carlo Methods, 2nd ed. (New York: Springer), Chapters 4–5.[3]   
Ripley, B.D. 1987, Stochastic Simulation (New York: Wiley).[4]   
Marsaglia, G. and Tsang W-W. 2000, “A Simple Method for Generating Gamma Variables,” ACM Transactions on Mathematical Software,vol.26,no.3,pp.363-372.[5]   
Devroye, L. 1986, Non-Uniform Random Variate Generation (New York: Springer).[6]   
Bratley, P., Fox, B.L., and Schrage, E.L. 1983, A Guide to Simulation, 2nd ed. (New York: Springer).[7].   
Knuth, D.E. 1997, Seminumerical Algorithms, 3rd ed., vol. 2 of The Art of Computer Programming (Reading, MA: Addison-Wesley),pp.125ff.[8]

# 7.4 Multivariate Normal Deviates

A multivariate random deviate of dimension $M$ is a point in $M$ -dimensional space. Its coordinates are a vector, each of whose $M$ components are random — but not, in general, independently so, or identically distributed. The special case of multivariate normal deviates is defined by the multidimensional Gaussian density function

$$
N ( { \bf x } \mid { \pmb \mu } , { \pmb \Sigma } ) = \frac { 1 } { ( 2 \pi ) ^ { M / 2 } \operatorname* { d e t } ( { \pmb \Sigma } ) ^ { 1 / 2 } } \exp [ - \frac { 1 } { 2 } ( { \bf x } - { \pmb \mu } ) \cdot { \pmb \Sigma } ^ { - 1 } \cdot ( { \bf x } - { \pmb \mu } ) ]
$$

where the parameter $\pmb { \mu }$ is a vector that is the mean of the distribution, and the parameter $\pmb { \Sigma }$ is a symmetrical, positive-definite matrix that is the distribution’s covariance.

There is a quite general way to construct a vector deviate $\mathbf { X }$ with a specified covariance $\pmb { \Sigma }$ and mean $\pmb { \mu }$ , starting with a vector $\mathbf { y }$ of independent random deviates of zero mean and unit variance: First, use Cholesky decomposition (-2.9) to factor $\pmb { \Sigma }$ into a left triangular matrix $\mathbf { L }$ times its transpose,

$$
\boldsymbol { \Sigma } = \mathbf { L } \mathbf { L } ^ { T }
$$

This is always possible because $\pmb { \Sigma }$ is positive-definite, and you need do it only once for each distinct $\pmb { \Sigma }$ of interest. Next, whenever you want a new deviate $\mathbf { X }$ , fill $\mathbf { y }$ with independent deviates of unit variance and then construct

$$
\mathbf { x } = \mathbf { L y } + \pmb { \mu }
$$

The proof is straightforward, with angle brackets denoting expectation values: Since the components $y _ { i }$ are independent with unit variance, we have

$$
\langle \mathbf { y } \otimes \mathbf { y } \rangle = \mathbf { 1 }
$$

where 1 is the identity matrix. Then,

$$
{ \begin{array} { r l } & { \left. \left( \mathbf { x } - { \boldsymbol { \mu } } \right) \otimes ( \mathbf { x } - { \boldsymbol { \mu } } ) \right. = \left. \left( \mathbf { L y } \right) \otimes ( \mathbf { L y } ) \right. } \\ & { \qquad = \left. \mathbf { L } ( \mathbf { y } \otimes \mathbf { y } ) \mathbf { L } ^ { T } \right. = \mathbf { L } \left. \mathbf { y } \otimes \mathbf { y } \right. \mathbf { L } ^ { T } } \\ & { \qquad = \mathbf { L } \mathbf { L } ^ { T } = \Sigma } \end{array} }
$$

As general as this procedure is, it is, however, rarely useful for anything except multivariate normal deviates. The reason is that while the components of $\mathbf { X }$ indeed have the right mean and covariance structure, their detailed distribution is not anything “nice.” The $x _ { i }$ ’s are linear combinations of the $y _ { i }$ ’s, and, in general, a linear combination of random variables is distributed as a complicated convolution of their individual distributions.

For Gaussians, however, we do have “nice.” All linear combinations of normal deviates are themselves normally distributed, and completely defined by their mean and covariance structure. Thus, if we always fill the components of y with normal deviates,

$$
y _ { i } \sim \mathrm { N } ( 0 , 1 )
$$

then the deviate (7.4.3) will be distributed according to equation (7.4.1).

Implementation is straightforward, since the Cholesky structure both accomplishes the decomposition and provides a method for doing the matrix multiplication efficiently, taking advantage of $\mathbf { L }$ ’s triangular structure. The generation of normal deviates is inline for efficiency, identical to Normaldev in $\ S 7 . 3$ .

struct Multinormaldev : Ran {   
Structure for multivariate normal deviates. Int mm; VecDoub mean; MatDoub var; Cholesky chol; VecDoub spt, pt; Multinormaldev(Ullong j, VecDoub &mmean, MatDoub &vvar) :   
Ran(j), mm(mmean.size()), mean(mmean), var(vvar), chol(var),   
spt(mm), pt(mm) {   
Constructor. Arguments are the random generator seed, the (vector) mean, and the (matrix) covariance. Cholesky decomposition of the covariance is done here.   
if (var.ncols() $! = \ \mathrm { m m } \ \mathrm { ~ \left| ~ \right| ~ }$ var.nrows() $! = \mathrm { \ m m } .$ ) throw("bad sizes");   
}

# VecDoub &dev() {

Return a multivariate normal deviate. Int i; Doub u,v,x,y,q; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<mm;i++) { Fill a vector of independent normal deviates. do { $u \ =$ doub(); v = 1.7156\*(doub()-0.5); x = u - 0.449871; $y ~ =$ abs(v) $^ +$ 0.386595; ${ \textsc { q } } =$ SQR(x) + y\*(0.19600\*y-0.25472\*x); } while (q $>$ 0.27597 && (q $>$ 0.27846 || SQR(v) > -4.\*log(u)\*SQR(u))); spt[i] $\ l = \ l { \ v } / { \ u }$ ; } chol.elmult(spt,pt); Apply equation (7.4.3). for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<mm; $\dot { 1 } + + \dot { 1 }$ ) {pt[i] $+ =$ mean[i];} return pt;   
}

};

# 7.4.1 Decorrelating Multiple Random Variables

Although not directly related to the generation of random deviates, this is a convenient place to point out how Cholesky decomposition can be used in the reverse manner, namely to find linear combinations of correlated random variables that have no correlation. In this application we are given a vector $\mathbf { X }$ whose components have a known covariance $\pmb { \Sigma }$ and mean $\mu$ . Decomposing $\pmb { \Sigma }$ as in equation (7.4.2), we assert

that

$$
\mathbf { y } = \mathbf { L } ^ { - 1 } ( \mathbf { x } - \pmb { \mu } )
$$

has uncorrelated components, each of unit variance. Proof:

$$
\begin{array} { r l } & { \langle \mathbf { y } \otimes \mathbf { y } \rangle = \left. \left( \mathbf { L } ^ { - 1 } [ \mathbf { x } - \pmb { \mu } ] \right) \otimes \left( \mathbf { L } ^ { - 1 } [ \mathbf { x } - \pmb { \mu } ] \right) \right. } \\ & { \qquad = \mathbf { L } ^ { - 1 } \left. \left( \mathbf { x } - \pmb { \mu } \right) \otimes \left( \mathbf { x } - \pmb { \mu } \right) \right. \mathbf { L } ^ { - 1 T } } \\ & { \qquad = \mathbf { L } ^ { - 1 } \pmb { \Sigma } \mathbf { L } ^ { - 1 T } = \mathbf { L } ^ { - 1 } \mathbf { L } \mathbf { L } ^ { T } \mathbf { L } ^ { - 1 T } = \mathbf { 1 } } \end{array}
$$

Be aware that this linear combination is not unique. In fact, once you have obtained a vector $\mathbf { y }$ of uncorrelated components, you can perform any rotation on it and still have uncorrelated components. In particular, if $\mathbf { K }$ is an orthogonal matrix, so that

$$
\mathbf { K } ^ { T } \mathbf { K } = \mathbf { K } \mathbf { K } ^ { T } = \mathbf { 1 }
$$

then

$$
\left. \left( \mathbf { K } \mathbf { y } \right) \otimes \left( \mathbf { K } \mathbf { y } \right) \right. = \mathbf { K } \left. \mathbf { y } \otimes \mathbf { y } \right. \mathbf { K } ^ { T } = \mathbf { K } \mathbf { K } ^ { T } = \mathbf { 1 }
$$

A common (though slower) alternative to Cholesky decomposition is to use the Jacobi transformation (-11.1) to decompose $\pmb { \Sigma }$ as

$$
\pmb { \Sigma } = \mathbf { V } \mathrm { d i a g } ( \sigma _ { i } ^ { 2 } ) \mathbf { V } ^ { T }
$$

where $\mathbf { V }$ is the orthogonal matrix of eigenvectors, and the $\sigma _ { i }$ ’s are the standard deviations of the (new) uncorrelated variables. Then $\mathbf { V } \mathrm { d i a g } ( \sigma _ { i } )$ plays the role of $\mathbf { L }$ in the proofs above.

Section $\ S 1 6 . 1 . 1$ discusses some further applications of Cholesky decomposition relating to multivariate random variables.

# 7.5 Linear Feedback Shift Registers

A linear feedback shift register (LFSR) consists of a state vector and a certain kind of update rule. The state vector is often the set of bits in a 32- or 64-bit word, but it can sometimes be a set of words in an array. To qualify as an LFSR, the update rule must generate a linear combination of the bits (or words) in the current state, and then shift that result onto one end of the state vector. The oldest value, at the other end of the state vector, falls off and is gone. The output of an LFSR consists of the sequence of new bits (or words) as they are shifted in.

For single bits, “linear” means arithmetic modulo 2, which is the same as using the logical XOR operation for $^ +$ and the logical AND operation for $\times$ . It is convenient, however, to write equations using the arithmetic notation. So, for an LFSR of length $n$ , the words in the paragraph above translate to

$$
\begin{array} { l } { { \displaystyle a _ { 1 } ^ { \prime } = \left( \sum _ { j = 1 } ^ { n - 1 } c _ { j } a _ { j } \right) + a _ { n } } } \\ { { \displaystyle a _ { i } ^ { \prime } = a _ { i - 1 } , \qquad i = 2 , \ldots , n } } \end{array}
$$

![](images/e4eaea2a8eaf2691a3c60857dd45659d8840abd80a973d858ff79514516877f9.jpg)  
Figure 7.5.1. Two related methods for obtaining random bits from a shift register and a primitive polynomial modulo 2. (a) The contents of selected taps are combined by XOR (addition modulo 2), and the result is shifted in from the right. This method is easiest to implement in hardware. (b) Selected bits are modified by XOR with the leftmost bit, which is then shifted in from the right. This method is easiest to implement in software.

Here $\mathbf { a } ^ { \prime }$ is the new state vector, derived from a by the update rule as shown. The reason for singling out $a _ { n }$ in the first line above is that its coefficient $c _ { n }$ must be $\equiv 1$ . Otherwise, the LFSR wouldn’t be of length $n$ , but only of length up to the last nonzero coefficient in the $c _ { j }$ ’s.

There is also a reason for numbering the bits (henceforth we consider only the case of a vector of bits, not of words) starting with 1 rather than the more comfortable 0. The mathematical properties of equation (7.5.1) derive from the properties of the polynomials over the integers modulo 2. The polynomial associated with (7.5.1) is

$$
P ( x ) = x ^ { n } + c _ { n - 1 } x ^ { n - 1 } + \cdots + c _ { 2 } x ^ { 2 } + c _ { 1 } x + 1
$$

where each of the $c _ { i }$ ’s has the value 0 or 1. So, $c _ { 0 }$ , like $c _ { n }$ , exists but is implicitly $\equiv ~ 1$ . There are several notations for describing specific polynomials like (7.5.2). One is to simply list the values $i$ for which $c _ { i }$ is nonzero (by convention including $c _ { n }$ and $c _ { 0 }$ ). So the polynomial

$$
x ^ { 1 8 } + x ^ { 5 } + x ^ { 2 } + x + 1
$$

is abbreviated as

$$
( 1 8 , 5 , 2 , 1 , 0 )
$$

Another, when a value of $n$ (here 18), and $c _ { n } = c _ { 0 } = 1$ , is assumed, is to construct a “serial number” from the binary word $c _ { n - 1 } c _ { n - 1 } \cdot \cdot \cdot c _ { 2 } c _ { 1 }$ (by convention now excluding $c _ { n }$ and $c _ { 0 }$ ). For (7.5.3) this would be 19, that is, $2 ^ { 4 } + 2 ^ { 1 } + 2 ^ { 0 }$ . The nonzero $c _ { i }$ ’s are often referred to as an LFSR’s taps.

Figure 7.5.1(a) illustrates how the polynomial (7.5.3) and (7.5.4) looks as an update process on a register of 18 bits. Bit 0 is the temporary where a bit that is to become the new bit 1 is computed.

The maximum period of an LFSR of $n$ bits, before its output starts repeating, is $2 ^ { n } - 1$ . This is because the maximum number of distinct states is $2 ^ { n }$ , but the special vector with all bits zero simply repeats itself with period 1. If you pick a random polynomial $P ( x )$ , then the generator you construct will usually not be full-period. A fraction of polynomials over the integers modulo 2 are irreducible, meaning that they can’t be factored. A fraction of the irreducible polynomials are primitive, meaning that they generate maximum period LFSRs. For example, the polynomial $x ^ { 2 } + 1 =$ $( x + 1 ) ( x + 1 )$ is not irreducible, so it is not primitive. (Remember to do arithmetic on the coefficients mod 2.) The polynomial $x ^ { 4 } + x ^ { 3 } + x ^ { 2 } + x + 1$ is irreducible, but it turns out not to be primitive. The polynomial $x ^ { 4 } + x + 1$ is both irreducible and primitive.

Maximum period LFSRs are often used as sources of random bits in hardware devices, because logic like that shown in Figure 7.5.1(a) requires only a few gates and can be made to run extremely fast. There is not much of a niche for LFSRs in software applications, because implementing equation (7.5.1) in code requires at least two full-word logical operations for each nonzero $c _ { i }$ , and all this work produces a meager one bit of output. We call this “Method I.” A better software approach, “Method II,” is not obviously an LFSR at all, but it turns out to be mathematically equivalent to one. It is shown in Figure 7.5.1(b). In code, this is implemented from a primitive polynomial as follows:

Let maskp and maskn be two bit masks,

$$
\begin{array} { c c c c c c c c c c } { { \mathrm { m a s k p } \equiv } } & { { ( 0 } } & { { \cdots } } & { { 0 } } & { { c _ { n - 1 } } } & { { c _ { n - 2 } } } & { { \cdots } } & { { c _ { 2 } } } & { { c _ { 1 } } } \\ { { \mathrm { m a s k n } \equiv } } & { { ( 0 } } & { { \cdots } } & { { 1 } } & { { 0 } } & { { 0 } } & { { \cdots } } & { { 0 } } & { { 0 ) } } \end{array}
$$

Then, a word a is updated by

$$
\begin{array} { c c } { { \mathrm { i f } \quad ( \tt a \& m a s k n ) \quad \tt a \equiv \displaystyle ( ( a \mathrm { ~ \hat { ~ } { \theta ~ } { \theta ~ } { \theta ~ } { \theta ~ } ^ { \mathrm { { ~ \tiny ~ m a s k p } } } ) ~ \ll ~ 1 ) ~ } \mid 1 ; } } \\ { { \mathrm { e l s e ~ \tt ~ a ~ < < = ~ 1 ; } } } \end{array}
$$

You should work through the above prescription to see that it is identical to what is shown in the figure. The output of this update (still only one bit) can be taken as (a & maskn), or for that matter any fixed bit in a.

LFSRs (either Method I or Method II) are sometimes used to get random $m$ -bit words by concatenating the output bits from $m$ consecutive updates (or, equivalently for Method I, grabbing the low-order m bits of state after every $m$ updates). This is generally a bad idea, because the resulting words usually fail some standard statistical tests for randomness. It is especially a bad idea if $m$ and $2 ^ { n } - 1$ are not relatively prime, in which case the method does not even give all $m$ -bit words uniformly.

Next, we’ll develop a bit of theory to see the relation between Method I and Method II, and this will lead us to a routine for testing whether any given polynomial (expressed as a bit string of $c _ { i }$ ’s) is primitive. But, for now, if you only need a table of some primitive polynomials go get going, one is provided on the next page.

Since the update rule (7.5.1) is linear, it can be written as a matrix M that multiplies from the left a column vector of bits a to produce an updated state $\mathbf { a } ^ { \prime }$ . (Note that the low-order bits of a start at the top of the column vector.) One can readily read off

$$
\mathbf { M } = { \left[ \begin{array} { l l l l l l l } { c _ { 1 } } & { c _ { 2 } } & { \dots } & { c _ { n - 2 } } & { c _ { n - 1 } } & { 1 } \\ { 1 } & { 0 } & { \dots } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { \dots } & { 0 } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { } & { \vdots } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { \dots } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { \dots } & { 0 } & { 1 } & { 0 } \end{array} \right] }
$$

<table><tr><td></td><td></td><td></td><td></td><td>Some Primitive Polynomials Modulo 2 (after Watson [1])</td><td></td><td></td><td></td><td></td><td></td><td>1,</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>(51,</td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>(52,</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>(53,</td><td></td><td></td><td></td><td>1,</td><td></td><td>3</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>(54,</td><td></td><td></td><td></td><td></td><td></td><td>2，</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>(55,</td><td></td><td></td><td></td><td></td><td></td><td>0)</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>(56,</td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>(57,</td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td></td><td></td><td></td><td>2， 0</td><td></td><td>(58,</td><td></td><td></td><td></td><td></td><td></td><td>0 3,</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>(59,</td><td></td><td></td><td></td><td></td><td>1，</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>60,</td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>(11,</td><td></td><td></td><td></td><td></td><td></td><td>(61,</td><td></td><td></td><td>1,</td><td></td><td>0</td></tr><tr><td>(12,</td><td></td><td></td><td>1,</td><td></td><td></td><td>(62,</td><td></td><td></td><td>3，</td><td></td><td>0 0 2，</td></tr><tr><td>(13, (14,</td><td></td><td></td><td>1, 、</td><td>8</td><td></td><td>(63, 64</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(15, (16,</td><td></td><td></td><td>2，</td><td>0</td><td></td><td>(65, (66,</td><td></td><td></td><td></td><td>１１５１１２１１З２３１２２１２３</td><td>3</td></tr><tr><td>(17, (18,</td><td></td><td></td><td>1，</td><td>0</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(19,</td><td></td><td></td><td>1，</td><td>0</td><td></td><td>(69,</td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>(20, (21,</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>(22, (23, (24,</td><td></td><td></td><td></td><td></td><td></td><td>geee</td><td></td><td></td><td></td><td></td><td>3 1，0)</td></tr><tr><td>(25, (26, (27,</td><td></td><td></td><td>1，</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>1，</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0 9</td></tr><tr><td>(28,</td><td></td><td></td><td>1，</td><td>0</td><td></td><td>（78,</td><td></td><td></td><td></td><td></td><td>002</td></tr><tr><td>(29,</td><td></td><td></td><td></td><td></td><td></td><td>(79,</td><td></td><td></td><td></td><td></td><td>1,</td></tr><tr><td>(30,</td><td></td><td></td><td>1，</td><td>0</td><td></td><td>(80, (81,</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(31,</td><td></td><td></td><td></td><td>1,</td><td>0</td><td>(82,</td><td></td><td></td><td></td><td>8</td><td>1,</td></tr><tr><td>(32, (33,</td><td></td><td></td><td>315</td><td>2</td><td>0</td><td>(83， (84,</td><td></td><td></td><td></td><td></td><td>1,</td></tr><tr><td>(34,</td><td></td><td></td><td></td><td>1,</td><td>0</td><td>(85,</td><td></td><td></td><td></td><td></td><td>8</td></tr><tr><td>(35, (36,</td><td></td><td></td><td>4,</td><td>1,</td><td>0</td><td>(86, (87,</td><td></td><td></td><td></td><td></td><td>3 1，</td></tr><tr><td>(37,</td><td></td><td></td><td>3, 1,</td><td>3 1,</td><td></td><td>(88,</td><td></td><td></td><td>6２5１２１4З２5２</td><td></td><td>0</td></tr><tr><td>(38, (39,</td><td></td><td>3，</td><td></td><td></td><td></td><td>(89, (90,</td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>(40,</td><td></td><td></td><td>0</td><td></td><td></td><td>(91,</td><td></td><td></td><td></td><td></td><td>3 2，</td></tr><tr><td>(41, (42,</td><td></td><td></td><td></td><td>1,</td><td>0</td><td>(92,</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(43,</td><td></td><td></td><td></td><td></td><td></td><td>(93,</td><td></td><td></td><td></td><td></td><td>1,</td></tr><tr><td>(44,</td><td></td><td></td><td></td><td></td><td></td><td>(94,</td><td></td><td></td><td>1, 4, 4,</td><td></td><td>0 2 2,</td></tr><tr><td>(45, (46, (47,</td><td></td><td>4の44535の553&#x27;</td><td>33213</td><td>1,</td><td>0</td><td>(95, (96, (97,</td><td></td><td></td></table>

What are the conditions on $\mathbf { M }$ that give a full-period generator, and thereby prove that the polynomial with coefficients $c _ { i }$ is primitive? Evidently we must have

$$
\mathbf { M } ^ { ( 2 ^ { n } - 1 ) } = \mathbf { 1 }
$$

where 1 is the identity matrix. This states that the period, or some multiple of it, is $2 ^ { n } - 1$ . But the only possible such multiples are integers that divide $2 ^ { n } - 1$ . To rule these out, and ensure a full period, we need only check that

$$
{ \bf M } ^ { q _ { k } } \neq { \bf 1 } , \qquad q _ { k } \equiv ( 2 ^ { n } - 1 ) / f _ { k }
$$

for every prime factor $f _ { k }$ of $2 ^ { n } - 1$ . (This is exactly the logic behind the tests of the matrix T that we described, but did not justify, in $\ S 7 . 1 . 2 .$ )

It may at first sight seem daunting to compute the humongous powers of $\mathbf { M }$ in equations (7.5.8) and (7.5.9). But, by the method of repeated squaring of $\mathbf { M }$ , each such power takes only about $n$ (a number like 32 or 64) matrix multiplies. And, since all the arithmetic is done modulo 2, there is no possibility of overflow! The conditions (7.5.8) and (7.5.9) are in fact an efficient way to test a polynomial for primitiveness. The following code implements the test. Note that you must customize the constants in the constructor for your choice of $n$ (called $\mathbb { N }$ in the code), in particular the prime factors of $2 ^ { n } - 1$ . The case $n = 3 2$ is shown. Other than that customization, the code as written is valid for $n \leq 6 4$ . The input to the test is the “serial number,” as defined above following equation (7.5.4), of the polynomial to be tested. After declaring an instance of the Primpolytest structure, you can repeatedly call its test() method to test multiple polynomials. To make Primpolytest entirely self-contained, matrices are implemented as linear arrays, and the structure builds from scratch the few matrix operations that it needs. This is inelegant, but effective.

# struct Primpolytest {

Test polynomials over the integers mod 2 for primitiveness.

Int N, nfactors;   
VecUllong factors;   
VecInt t,a,p;   
Primpolytest() : N(32), nfactors(5), factors(nfactors), t(N\*N), a(N\*N), p(N\*N) { Constructor. The constants are specific to 32-bit LFSRs. Ullong factordata[5] $=$ {3,5,17,257,65537}; for (Int $\scriptstyle { \dot { 1 } } = 0$ ;i<nfactors; $\dot { \bf 1 } + + \dot { }$ ) factors[i] $=$ factordata[i];   
}   
Int ispident() { Utility to test if p is the identity matrix. Int i,j; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; i<N; $\dot { \bf 1 } + +$ ) for $\scriptstyle \dot { \ j } = 0$ ; j<N; $\mathrm { j } + +$ ) { if ( $\begin{array} { r l } { \dot { \bar { \mathbf { 1 } } } } & { { } = = } \end{array}$ j) { if (p[i\*N+j] $\smash { \downarrow = 1 }$ ) return 0; } else {if (p[i\*N+j] $\smash { \ ! = \ 0 }$ ) return 0; } } return 1;   
}   
void mattimeseq(VecInt &a, VecInt &b) { Utility for a $\ast =$ b on matrices a and b. Int i,j,k,sum; VecInt tmp(N\*N); for ( $\scriptstyle \dot { 1 } = 0$ ; i<N; $\Dot { \ b { 1 } } + +$ ) for ( $\scriptstyle { \dot { \ j } } = 0$ ; j<N; ${ \mathrm { j } } + + { \mathrm { . } }$ ) { sum $\qquad = \ 0$ ; for $\scriptstyle \mathtt { k } = 0$ ; k<N; $\mathtt { k } { + } { + }$ ) sum $+ =$ a[i\*N+k] $^ *$ b[k\*N+j]; tmp[i\*N+j] $=$ sum & 1; } for $\scriptstyle ( \mathtt { k } = 0$ ; k<N\*N; $\mathbf { k } { + } { + }$ ) a[k] $=$ tmp[k];   
}

void matpow(Ullong n) { Utility for matrix $\gamma = \mathsf { a } \mathsf { \hat { n } }$ by successive Int k; squares.

for $( \mathrm { k } = 0$ ; k<N\*N; $\mathtt { k } { + } { + }$ ) p[k] = 0; for $( \mathtt { k } = 0$ ; k<N; $\mathbf { k } { + } { + } \mathbf { \cdot }$ ) p[k\*N+k] = 1; while (1) { if (n & 1) mattimeseq(p,a); n $> > = ~ 1$ ; if $\mathbf { \Omega } _ { \mathrm { ~ n ~ } } = = \mathbf { \Omega } 0$ ) break; mattimeseq(a,a); } }

Int test(Ullong n) {   
Main test routine. Returns 1 if the polynomial with serial number n (see text) is primitive, 0 otherwise.

Int i,k,j; Ullong pow, tnm1, $\mathrm { ~ n n ~ } = \mathrm { ~ n ~ }$ ; tnm1 $=$ ((Ullong)1 << N) - 1; if (n > (tnm1 >> 1)) throw("not a polynomial of degree N"); for $( \mathrm { k } = 0$ ; k<N\*N; $\mathrm { k } { + + }$ ) t[k] $\qquad = \ 0$ ; Construct the update matrix in t. for ( $\scriptstyle { \dot { \hat { 1 } } } = 1$ ; i<N; $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \rho } } } .$ ) $\ t [ \mathrm { i } * \mathrm { N } + ( \mathrm { i } - 1 ) ] = 1 ;$ $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; while (nn) { if (nn & 1) t[j] = 1; nn $> > = ~ 1$ ; j++; } t[N-1] $\ l = \ 1$ ; for $\scriptstyle 1 = 0$ ; k<N\*N; $\mathtt { k } { + } { + }$ ) a[k] $=$ t[k]; Test that t^tnm1 is the identity matrix. matpow(tnm1); if (ispident() $! = ~ 1 )$ return 0; for ( $\scriptstyle { \dot { 1 } } = 0$ ; i<nfactors; $\dot { 1 } + +$ ) { Test that the t to the required submultipow $=$ tnm1/factors[i]; ple powers is not the identity matrix. for $\scriptstyle \mathtt { k } = 0$ ; k<N\*N; $\mathbf { k } { + } { + }$ ) a[k] $= ~ \ t$ [k]; matpow(pow); if (ispident $( ) \ = = \ 1$ ) return 0; } return 1; } };

It is straightforward to generalize this method to $n > 6 4$ or to prime moduli $p$ other than 2. If $p ^ { n } > 2 ^ { 6 \mp }$ , you’ll need a multiword binary representation of the integers $p ^ { n } - 1$ and its quotients with its prime factors, so that matpow can still find powers by successive squares. Note that the computation time scales roughly as $O ( n ^ { 4 } )$ , so $n = 6 4$ is fast, while $n = 1 0 2 4$ would be rather a long calculation.

Some random primitive polynomials for $n = 3 2$ bits (giving their serial numbers as decimal values) are 2046052277, 1186898897, 221421833, 55334070, 1225518245, 216563424, 1532859853, 1735381519, 2049267032, 1363072601, and 130420448. Some random ones for $n = 6 4$ bits are 926773948609480634, 3195735403700392248, 4407129700254524327, 256457582706860311, 5017679982664373343, and 1723461400905116882.

Given a matrix M that satisfies equations (7.5.8) and (7.5.9), there are some related matrices that also satisfy those relations. An example is the inverse of M, which you can easily verify as

$$
\mathbf { M } ^ { - 1 } = \left[ \begin{array} { c c c c c c c } { 0 } & { 1 } & { 0 } & { . . . } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { . . . } & { 0 } & { 0 } \\ { . } & { . } & { . } & { } & { . } & { . } \\ { . } & { . } & { . } & { } & { . } & { . } \\ { 0 } & { 0 } & { 0 } & { . . . } & { 0 } & { 1 } \\ { 1 } & { c _ { 1 } } & { c _ { 2 } } & { . . . } & { c _ { n - 2 } } & { c _ { n - 1 } } \end{array} \right]
$$

This is the update rule that backs up a state $\mathbf { a } ^ { \prime }$ to its predecessor state a. You can easily convert (7.5.10) to a prescription analogous to equation (7.5.1) or to Figure 7.5.1(a).

Another matrix satisfying the relations that guarantee a full period is the transpose of the

inverse (or inverse of the transpose) of $\mathbf { M }$ ,

$$
\left( \mathbf { M } ^ { - 1 } \right) ^ { T } = \left[ \begin{array} { l l l l l l } { 0 } & { 0 } & { \dots } & { 0 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { \dots } & { 0 } & { 0 } & { c _ { 1 } } \\ { 0 } & { 1 } & { \dots } & { 0 } & { 0 } & { c _ { 2 } } \\ { \vdots } & { \vdots } & & { \vdots } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { \dots } & { 1 } & { 0 } & { c _ { n - 2 } } \\ { 0 } & { 0 } & { \dots } & { 0 } & { 1 } & { c _ { n - 1 } } \end{array} \right]
$$

Surprise! This is exactly Method II, as also shown in Figure 7.5.1(b). (Work it out.)

Even more specifically, the sequence of bits output by a Method II LFSR based on a primitive polynomial $P ( x )$ is identical to the sequence output by a Method I LFSR that uses the reciprocal polynomial $x ^ { n } P ( 1 / x )$ . The proof is a bit beyond our scope, but it is essentially because the matrix $\mathbf { M }$ and its transpose are both roots of the characteristic polynomial, equation (7.5.2), while the inverse matrix $\mathbf { M } ^ { - 1 }$ and its transpose are both roots of the reciprocal polynomial. The reciprocal polynomial, as you can easily check from the definition, just swaps the positions of nonzero coefficients end-to-end. For example, the reciprocal polynomial of equation (7.5.3) is .18; 17; 16; 13; 1/. If a polynomial is primitive, so is its reciprocal.

Try this experiment: Run a Method II generator for a while. Then take $n$ consecutive bits of its output (from its highest bit, say) and put them into a Method I shift register as initialization (low bit the most recent one). Now step the two methods together, using the reciprocal polynomial in the Method I. You’ll get identical output from the two generators.

# CITED REFERENCES AND FURTHER READING:

Knuth, D.E. 1997, Seminumerical Algorithms, 3rd ed., vol. 2 of The Art of Computer Programming (Reading,MA:Addison-Wesley),pp.30ff.   
Horowitz, P., and Hill, W. 1989, The Art of Electronics, 2nd ed. (Cambridge, UK: Cambridge University Press), $\ S 9 . 3 2 - \ S 9 . 3 7$ .   
Tausworthe, R.C. 1965, “Random Numbers Generated by Linear Recurrence Modulo Two,” Mathematics of Computation, vol.19,pp.201-209.   
Watson, E.J. 1962, “Primitive Polynomials (Mod 2),” Mathematics of Computation, vol. 16, pp. 368– 369.[1]

# 7.6 Hash Tables and Hash Memories

It’s a strange dream. You’re in a kind of mailroom whose walls are lined with numbered pigeonhole boxes. A man, Mr. Hacher, sits at a table. You are standing. There is an in-basket mounted on the wall. Your job is to take letters from the inbasket and sort them into the pigeonholes.

But how? The letters are addressed by name, while the pigeonholes are only numbered. That is where Mr. Hacher comes in. You show him each letter, and he immediately tells you its pigeonhole number. He always gives the same number for the same name, while different names always get different numbers (and therefore unique pigeonholes).

Over time, as the number of addressees grows, there are fewer and fewer empty boxes until, finally, none at all. This is not a problem as long as letters arrive only for existing boxholders. But one day, you spot a new name on an envelope. With trepidation you put it in front of Mr. Hacher : : : and you wake up!

Mr. Hacher and his table are a hash table. A hash table behaves as if it keeps a running ledger of all the hash keys (the addressee names) that it has ever seen, assigns a unique number to each, and is able to look through all the names for every new query, either returning the same number as before (for a repeat key) or, for a new key, assigning a new one. There is usually also an option to erase a key.

The goal in implementing a hash table is to make all these functions take only a few computer operations each, not even ${ \cal O } ( \log N )$ . That is quite a trick, if you think about it. Even if you somehow maintain an ordered or alphabetized list of keys, it will still take ${ \cal O } ( \log N )$ operations to find a place in the list, by bisection, say. The big idea behind hash tables is the use of random number techniques $( \ S 7 . 1 )$ to map a hash key to a pseudo-random integer between 0 and $N - 1$ , where $N$ is the total number of pigeonholes. Here we definitely want pseudo-random and not random integers, because the same key must produce the same integer each time.

In first approximation, ideally much of the time, that initial pseudo-random integer, called the output of the hash function, or (for short) the key’s hash, is what the hash table puts out, i.e., the number given out by Mr. Hacher. However, it is possible that, by chance, two keys have the same hash; in fact this becomes increasingly probable as the number of distinct keys approaches $N$ , and a certainty when $N$ is exceeded (the pigeonhole principle). The implementation of a hash table therefore requires a collision strategy that ensures that unique integers are returned, even for (different) keys that have the same hash.

Many vendors’ implementations of the $\mathrm { C } { + + }$ ’s Standard Template Library (STL) provide a hash table as the class hash_map. Unfortunately, at this writing, hash_map is not a part of the actual STL standard, and the quality of vendor implementations is also quite variable. We therefore here implement our own; thereby we can both learn more about the principles involved and build in some specific features that will be useful later in this book (for example $\ S 2 1 . 8$ and -21.6).

# 7.6.1 Hash Function Object

By a hash function object we mean a structure that combines a hashing algorithm (as in $\ S 7 . 1$ ) with the “glue” needed to make a hash table. The object should map an arbitrary key type keyT, which itself may be a structure containing multiple data values, into (for our implementation) a pseudo-random 64-bit integer. All the hash function object really needs to know about keyT is its length in bytes, that is, sizeof(keyT), since it doesn’t care how those bytes are used, only that they are part of the key to be hashed. We therefore give the hash function object a constructor that tells it how many bytes to hash; and we let it access a key by a void pointer to the key’s address. Thus the object can access those bytes any way it wants.

As a first example of a hash function object, let’s just put a wrapper around the hash function algorithm of $\ S 7 . 1 . 4$ . This is quite efficient when sizeof $( \mathtt { k e y T } ) = 4$ or 8.

# struct Hashfn1 {

Example of an object encapsulating a hash function for use by the class Hashmap.

Ranhash hasher;   
Int n;   
Hashfn1(Int nn) : n(nn) {}   
Ullong fn(const void \*key) { Uint \*k; Ullong \*kk; The actual hash function.   
Size of key in bytes.   
Constructor just saves key size.   
Function that returns hash from key.

switch (n) { case 4: k = (Uint \*)key; return hasher.int64(\*k); Return 64-bit hash of 32-bit key. case 8: kk $=$ (Ullong \*)key;\ return hasher.int64(\*kk); Return 64-bit hash of 64-bit key. default: throw("Hashfn1 is for 4 or 8 byte keys only."); } } };

(Since n is constant for the life of the object, it’s a bit inefficient to be testing it on every call; you should edit out the unnecessary code when you know n in advance.)

More generally, a hash function object can be designed to work on arbitrary sized keys by incorporating them into a final hash value a byte at a time. There is a trade-off between speed and degree-of-randomness. Historically, hash functions have favored speed, with simple incorporation rules like

$$
\begin{array} { l } { { h _ { 0 } = \mathrm { s o m e ~ f i x e d ~ c o n s t a n t } } } \\ { { \ } } \\ { { h _ { i } = ( m \ h _ { i - 1 } \ \mathrm { o p } \ k _ { i } ) \quad \mathrm { m o d } \ 2 ^ { 3 2 } \qquad ( i = 1 \dots K ) } } \end{array}
$$

Here $k _ { i }$ is the $i$ th byte of the key $1 \leq i \leq K )$ ), $m$ is a multiplier with popular values that include 33, 63689, and $2 ^ { 1 6 } + 2 ^ { 6 } - 1$ (doing the multiplication by shifts and adds in the first and third cases), and “op” is either addition or bitwise XOR. You get the mod function for free when you use 32-bit unsigned integer arithmetic. However, since 64-bit arithmetic is fast on modern machines, we think that the days of small multipliers, or many operations changing only a few bits at a time, are over. We favor hash functions that can pass good tests for randomness. (When you know a lot about your keys, it is possible to design hash functions that are even better than random, but that is beyond our scope here.)

A hash function object may also do some initialization (of tables, etc.) when it is created. Unlike a random number generator, however, it may not store any historydependent state between calls, because it must return the same hash for the same key every time. Here is an example of a self-contained hash function object for keys of any length. This is the hash function object that we will use below.

# hash.h

# struct Hashfn2 {

Another example of an object encapsulating a hash function, allowing arbitrary fixed key sizes or variable-length null terminated strings. The hash function algorithm is self-contained.

static Ullong hashfn_tab[256];   
Ullong h;   
Int n;   
Hashfn2(Int nn) : n(nn) { if $\mathbf { \Phi } _ { \mathbf { { n } } } \ = \mathbf { \Phi } _ { 1 } \mathbf { \Phi } _ { \mathbf { { \Lambda } } }$ ) $\mathrm { ~ \tt ~ n ~ } = \mathrm { ~ 0 ~ }$ ; $\mathbf { \bar { h } _ { \theta } } =$ 0x544B2FBACAAF1684LL; for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<256; ${ \dot { \mathsf { J } } } ^ { + + }$ ) { for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; i<31; $\dot { \bf 1 } + +$ ) { $\mathrm { ~ \bf ~ h ~ } =$ (h >> 7) ^ h; h = (h << 11) ^ h; ${ \mathrm { ~  ~ h ~ } } = { \mathrm { ~  ~ \left( ~ h ~ \right) > ~ \thinspace ~ 1 0 ~ } } \widehat { \mathrm { ~  ~ \cdot ~ } } { \mathrm { ~  ~ h ~ } } ;$ } hashfn_tab[j] $= { \textrm { h } }$ ; }   
}   
Size of key in bytes, when fixed size.   
Null terminated string key signaled by $\mathbf { n } = \mathbf { 0 }$ or 1.   
Length 256 lookup table is initialized with values from a 64-bit Marsaglia generator stepped 31 times between each.

Ullong fn(const void \*key) { Function that returns hash from key. Int j; char \*k $=$ (char $^ *$ )key; Cast the key pointer to char pointer. $\mathrm { \textbar { h } = }$ 0xBB40E64DA205B064LL; $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; while (n $? \mathtt { j } + + \mathtt { \le ~ n ~ }$ : \*k) { Fixed length or else until null. $\mathrm { ~ h ~ } = \mathrm { ~ ( ~ h ~ \ * ~ }$ 7664345821815920749LL) hashfn_tab[(unsigned char)(\*k)]; $\mathrm { k } { + + }$ ; } return h; } }; Ullong Hashfn2::hashfn_tab[256]; Defines storage for the lookup table.

The method used is basically equation (7.6.1), but (i) with a large constant that is known to be a good multiplier for a linear congruential random number generator mod $2 ^ { 6 4 }$ , and, more importantly, (ii) a table lookup that substitutes a random (but fixed) 64-bit value for every byte value in 0 : : : 255. Note also the tweak that allows Hashfn2 to be used either for fixed length key types (call constructor with $\mathtt { n } > 1 \mathtt { \Omega }$ ) or with null terminated byte arrays of variable length (call constructor with $\mathtt { n } = 0$ or 1).

# 7.6.2 Hash Table

By hash table we mean an object with the functionality of Mr. Hacher (and his table) in the dream, namely to turn arbitrary keys into unique integers in a specified range. Let’s dive right in. In outline, the Hashtable object is

template<class keyT, class hfnT> struct Hashtable {

Instantiate a hash table, with methods for maintaining a one-to-one correspondence between arbitrary keys and unique integers in a specified range.

Int nhash, nmax, nn, ng;   
VecInt htable, next, garbg;   
VecUllong thehash;   
hfnT hash; An instance of a hash function object.   
Hashtable(Int nh, Int nv);   
Constructor. Arguments are size of hash table and max number of stored elements (keys).

Int iget(const keyT &key); Return integer for a previously set key. Int iset(const keyT &key); Return unique integer for a new key. Int ierase(const keyT &key); Erase a key. Int ireserve(); Reserve an integer (with no key). Int irelinquish(Int k); Un-reserve an integer. };

template<class keyT, class hfnT>   
Hashtable<keyT,hfnT>::Hashtable(Int nh, Int nv):   
Constructor. Set nhash, the size of the hash table, and nmax, the maximum number of elements   
(keys) that can be accommodated. Allocate arrays appropriately. hash(sizeof(keyT)), nhash(nh), nmax(nv), nn(0), ng(0), htable(nh), next(nv), garbg(nv), thehash(nv) for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<nh; $\mathrm { j } + +$ ) { htable[j] $=$ -1; } Signifies empty.   
}

A Hashtable object is templated by two class names: the class of the key (which may be as simple as int or as complicated as a multiply derived class) and the class of the hash function object (e.g., Hashfn1 or Hashfn2, above). Note how the hash function object is automatically created using the size of keyT, so the user is not responsible for knowing this value. If you are going to use variable length, null terminated byte arrays as keys, then the type of keyT is char, not char $^ *$ ; see $\ S 7 . 6 . 5$ for an example.

The hash table object is created from two integer parameters. The most important one is nm, the maximum number of objects that can be stored — in the dream, the number of pigeonholes in the room. For now, suppose that the second parameter, nh, has the same value as nm.

The overall scheme is to convert arbitrary keys into integers in the range $0 \ldots$ $\mathrm { \ n h } { - 1 }$ that index into the array htable, by taking the output of the hash function modulo nh. That array’s indexed element contains either $^ { - 1 }$ , meaning “empty,” or else an index in the range $0 \ldots \mathrm { n m } ^ { - 1 }$ that points into the arrays thehash and next. (For a computer science flavor one could do this with list elements linked by pointers, but in the spirit of numerical computation, we will use arrays; both ways are about equally efficient.)

An element in thehash contains the 64-bit hash of whatever key was previously assigned to that index. We will take the identity of two hashes as being positive proof that their keys were identical. Of course this is not really true. There is a probability of $2 ^ { - 6 4 } \sim 5 \times 1 0 ^ { - 2 0 }$ of two keys giving identical hashes by chance. To guarantee error-free performance, a hash table must in fact store the actual key, not just the hash; but for our purposes we will accept the very small chance that two elements might get confused. (Don’t use these routines if you are typically storing more than a billion elements in a single hash table. But you already knew that!)

This $1 0 ^ { - 2 0 }$ coincidence is not what is meant by hash collision. Rather, hash collisions occur when two hashes yield the same value modulo nh, so that they point to the same element in htable. That is not at all unusual, and we must provide for handling it. Elements in the array next contain values that index back into thehash and next, i.e., form a linked list. So, when two or more keys have landed on the same value $i$ , $0 \leq i < \mathrm { n h }$ , and we want to retrieve a particular one of them, it will either be in the location thehashŒi , or else in the (hopefully short) list that starts there and is linked by nextŒi, nextŒnextŒi, and so forth.

We can now say more about the value that should be initially specified for the parameter nh. For a full table with all nm values assigned, the linked lists attached to each element of htable have lengths that are Poisson distributed with a mean $\lambda \equiv \mathrm { n m / n h }$ . Thus, large $\lambda$ (nh too small) implies a lot of list traversal, while small $\lambda$ (nh too large) implies wasted space in htable. Conventional wisdom is to choose $\lambda \sim 0 . 7 5$ , in which case (assuming a good hash function) $47 \%$ of htable will be empty, $67 \%$ of the nonempty elements will have lists of length one (i.e., you get the correct key on the first try), and the mean number of indirections (steps in traversing the next pointers) is 0.42. For $\lambda = 1$ , that is, $\mathrm { \Delta \ n h } = \mathrm { \ n m }$ , the values are $37 \%$ table empty, $58 \%$ first try hits, and 0.58 mean indirections. So, in this general range, any choice is basically fine. The general formulas are

$$
{ \begin{array} { r l } & { { \mathrm { e m p t y } } { \mathrm { f r a c t i o n } } = P _ { \lambda } ( 0 ) = e ^ { - \lambda } } \\ & { { \mathrm { ~ f r s t } } { \mathrm { t r y h i t s } } = P _ { \lambda } ( 1 ) / [ 1 - P _ { \lambda } ( 0 ) ] = { \frac { \lambda e ^ { - \lambda } } { 1 - e ^ { - \lambda } } } } \\ & { { \mathrm { m e a n i n d i r e c t i o n s } } = \displaystyle \sum _ { j = 2 } ^ { \infty } { \frac { ( j - 1 ) P _ { \lambda } ( j ) } { 1 - P _ { \lambda } ( 0 ) } } = { \frac { e ^ { - \lambda } - 1 + \lambda } { 1 - e ^ { - \lambda } } } } \end{array} }
$$

where $P _ { \lambda } ( j )$ is the Poisson probability function.

Now to the implementations within Hashtable. The simplest to understand is the “get” function, which returns an index value only if the key was previously “set,” and returns $^ { - 1 }$ (by convention) if it was not. Our data structure is designed to make this as fast as possible.

template<class keyT, class hfnT>   
Int Hashtable<keyT,hfnT>::iget(const keyT &key) {   
Returns integer in 0..nmax-1 corresponding to key, or $^ { - 1 }$ if no such key was previously stored. Int j,k; Ullong $\mathrm { \nabla { p p } } =$ hash.fn(&key); Get 64-bit hash ${ \dot { \mathrm { ~  ~ } } } =$ (Int)(pp % nhash); and map it into the hash table. for (k $=$ htable[j]; k $! = ~ - 1$ ; $\mathrm { ~ \bf ~ k ~ } =$ next[k]) { Traverse linked list until an exif (thehash[k] $= = \mathtt { p p }$ ) { act match is found. return k; } return -1; Key was not previously stored.   
}

A language subtlety to be noted is that iget receives key as a const reference, and then passes its address, namely &key, to the hash function object. $\mathrm { C } { + + }$ allows this, because the hash function object’s void pointer argument is itself declared as const.

The routine that “sets” a key is slightly more complicated. If the key has previously been set, we want to return the same value as the first time. If it hasn’t been set, we initialize the necessary links for the future.

# template<class keyT, class hfnT>

Int Hashtable<keyT,hfnT>::iset(const keyT &key)

Returns integer in 0..nmax-1 that will henceforth correspond to key. If key was previously set, return the same integer as before.

Int j,k,kprev;   
Ullong pp $=$ hash.fn(&key); Get 64-bit hash   
${ \dot { \mathrm { ~  ~ } } } =$ (Int)(pp % nhash); and map it into the hash table.   
if (htable[j] $\mathbf { \omega = \omega - 1 }$ ) { Key not in table. Find a free integer, either $\mathrm { ~ k ~ } = \mathrm { ~ n g ~ } ?$ garbg[--ng] : nn++ new or previously erased. htable[j] $= \mathrm { ~ k ~ }$ ;   
} else { Key might be in table. Traverse list. for $\mathrm { ~ ( ~ k ~ } =$ htable[j]; k $! = ~ - 1$ ; $\mathrm { ~ \bf ~ k ~ } =$ next[k]) { if (thehash[k] $= =$ pp) { return k; Yes. Return previous value. kprev = k; $\mathbf { k } \ = \ \mathbf { n } \mathbf { g } \ ?$ garbg[--ng] : $\mathtt { n n } + +$ ; No. Get new integer. next[kprev] $\mathit { \Theta } = \mathit { \Theta } \mathbf { \Theta } \mathbf { k }$ ;   
}   
if ( $\begin{array} { r } { \textbf { k } > = \mathtt { n m a x } , } \end{array}$ ) throw("storing too many values");   
thehash[k] $= \ p _ { \mathrm { p } }$ ; Store the key at the new or previous integer.   
next[k] $\ c = - 1$ ;   
return k;

A word here about garbage collection. When a key is erased (by the routine immediately below), we want to make its integer available to future “sets,” so that nmax keys can always be stored. This is very easy to implement if we allocate a garbage array (garbg) and use it as a last-in first-out stack of available integers. The set routine above always checks this stack when it needs a new integer. (By the way, had we designed Hashtable with list elements linked by pointers, instead of arrays, efficient garbage collection would have been more difficult to implement; see Stroustrop [1].)

# hash.h

template<class keyT, class hfnT>   
Int Hashtable<keyT,hfnT>::ierase(const keyT &key) {   
Erase a key, returning the integer in 0..nmax-1 erased, or $^ { - 1 }$ if the key was not previously set. Int j,k,kprev; Ullong $\begin{array} { r l } { \mathtt { p p } } & { { } = } \end{array}$ hash.fn(&key); ${ \dot { \mathrm { ~  ~ } } } =$ (Int)(pp % nhash); if (htable[j] $\begin{array} { r l } { \mathbf { \Phi } = } & { { } - 1 . } \end{array}$ ) return -1; Key not previously set. kprev $\ c = - 1$ ; for (k $=$ htable[j]; k $! = ~ - 1$ ; $\mathrm { ~ \bf ~ k ~ } =$ next[k]) if (thehash[k] $= = \mathtt { p p }$ ) { Found key. Splice linked list around it. if (kprev $\begin{array} { r l } { \mathbf { \Psi } = } & { { } - 1 \mathbf { \Psi } } \end{array}$ ) htable[j] $=$ next[k]; else next[kprev] $=$ next[k]; garbg[ $\mathbb { n } \underline { { \operatorname { g } } } { + } { + } \mathbb { 1 } = \mathbb { k } ;$ Add k to garbage stack as an available integer. return k; } kprev = k; } return -1; Key not previously set.   
}

Finally, Hashtable has routines that reserve and relinquish integers in the range 0 to nmax. When an integer is reserved, it is guaranteed not to be used by the hash table. Below, we’ll use this feature as a convenience in constructing a hash memory that can store more than one element under a single key.

template<class keyT, class hfnT>   
Int Hashtable<keyT,hfnT>::ireserve() {   
Reserve an integer in 0..nmax-1 so that it will not be used by set(), and return its value. Int $\mathbf { k } \ = \ \mathbf { n } \mathbf { g } \ ?$ garbg $[ - \mathtt { - n g } ]$ : nn++ ; if (k $> =$ nmax) throw("reserving too many values"); next[k] $\ c = - 2$ ; return k;   
}   
template<class keyT, class hfnT>   
Int Hashtable<keyT,hfnT>::irelinquish(Int k) {   
Return to the pool an index previously reserved by reserve(), and return it, or return $^ { - 1 }$ if it   
was not previously reserved. if (next[k] $\ ! = \ - 2 )$ {return -1;} garbg[ng++] $\mathit { \Theta } = \mathit { \Theta } \mathbf { k }$ ; return k;   
}

# 7.6.3 Hash Memory

The Hashtable class, above, implements Mr. Hacher’s task. Building on it, we next implement your job in the dream, namely to do the actual storage and retrieval of arbitrary objects by arbitrary keys. This is termed a hash memory.

When you store into an ordinary computer memory, the value of anything previously stored there is overwritten. If you want your hash memory to behave the same way, then a hash memory class, Hash, derived from Hashtable, is almost trivial to write. The class is templated by three structure types: keyT for the key type; elT for the type of the element that is stored in the hash memory; and hfnT, as before, for the object that encapsulates the hash function of your choice.

template<class keyT, class elT, class hfnT>   
struct Hash : Hashtable<keyT, hfnT> {   
Extend the Hashtable class with storage for elements of type elT, and provide methods for storing, retrieving. and erasing elements. key is passed by address in all methods. using Hashtable<keyT,hfnT>::iget;   
using Hashtable<keyT,hfnT>::iset;   
using Hashtable<keyT,hfnT>::ierase;   
vector<elT> els;

Hash(Int nh, Int nm) : Hashtable<keyT, hfnT>(nh, nm), els(nm) {} Same constructor syntax as Hashtable.

void set(const keyT &key, const elT &el) Store an element el. {els[iset(key)] $=$ el;}

Int get(const keyT &key, elT &el) { Retrieve an element into el. Returns 0 if no element is stored under key, or 1 for success.

Int $\begin{array} { r l } { { 1 1 } } & { { } = } \end{array}$ iget(key); if (ll < 0) return 0; el $=$ els[ll]; return 1; }

elT& operator[] (const keyT &key) {

Store or retrieve an element using subscript notation for its key. Returns a reference that can be used as an l-value.

Int $\begin{array} { r l } { { 1 1 } } & { { } = } \end{array}$ iget(key); if (ll < 0) { $\begin{array} { r l } { { 1 1 } } & { { } = } \end{array}$ iset(key); els[ll] $=$ elT(); } return els[ll]; }

Int count(const keyT &key) {   
Return the number of elements stored under key, that is, either 0 or 1. Int $\begin{array} { r l } { { 1 1 } } & { { } = } \end{array}$ iget(key); return $( 1 1 < 0 \ ? \ 0 : \ 1 )$ ;   
}   
Int erase(const keyT &key) {   
Erase an element. Returns 1 for success, or 0 if no element is stored under key. return (ierase(key) $< \ 0 \ ? \ 0 \ : \ 1 )$ ;   
}

The operator[] method, above, is intended for two distinct uses. First, it implements an intuitive syntax for storing and retrieving elements, e.g.,

$$
\mathrm { { m y h a s h } [ \it { s o m e - k e y } ] = \mathrm { { } } \it { r h s } }
$$

for storing, and

$$
l h s ~ = ~ \mathrm { \ m y h a s h [ \ s o m e - } k e y { \mathrm { ~ ] ~ } }
$$

for retrieving. Note, however, that a small inefficiency is introduced, namely a superfluous call to get when an element is set for the first time. Second, the method returns a non-const reference that cannot only be used as an l-value, but also be pointed to, as in

some-pointer $=$ &myhash[ some-key ]

Now the stored element can be referenced through the pointer, possibly multiple times, without any additional overhead of key lookup. This can be an important gain in efficiency in some applications. Of course you can also use the set and get methods directly.

# 7.6.4 Hash Multimap Memory

Next turn to the case where you want to be able to store more than one element under the same key. If ordinary computer memory behaved this way, you could set a variable to a series of values and have it remember all of them! Obviously this is a somewhat more complicated an extension of Hashtable than was Hash. We will call it Mhash, where the M stands for “multivalued” or “multimap.” One requirement is to provide a convenient syntax for retrieving multiple values of a single key, one at a time. We do this by the functions getinit and getnext. Also, in Mhash, below, nmax now means the maximum number of values that can be stored, not the number of keys, which may in general be smaller.

The code, with comments, should be understandable without much additional explanation. We use the reserve and relinquish features of Hashtable so as to have a common numbering system for all stored elements, both the first instance of a key (which Hashtable must know about) and subsequent instances of the same key (which are invisible to Hashtable but managed by Mhash through the linked list nextsis).

# hash.h

template<class keyT, class elT, class hfnT> struct Mhash : Hashtable<keyT,hfnT> {

Extend the Hashtable class with storage for elements of type elT, allowing more than one element to be stored under a single key.

using Hashtable<keyT,hfnT>::iget;   
using Hashtable<keyT,hfnT>::iset;   
using Hashtable<keyT,hfnT>::ierase;   
using Hashtable<keyT,hfnT>::ireserve;   
using Hashtable<keyT,hfnT>::irelinquish;   
vector<elT> els;   
VecInt nextsis; Links to next sister element under a single key.   
Int nextget;   
Mhash(Int nh, Int nm); Same constructor syntax as Hashtable.   
Int store(const keyT &key, const elT &el); Store an element under key.   
Int erase(const keyT &key, const elT &el); Erase a specified element under key.   
Int count(const keyT &key); Count elements stored under key.   
Int getinit(const keyT &key); Prepare to retrieve elements from key.   
Int getnext(elT &el); Retrieve next element specified by getinit.   
template<class keyT, class elT, class hfnT>   
Mhash<keyT,elT,hfnT>::Mhash(Int nh, Int nm) : Hashtable<keyT, hfnT>(nh, nm), nextget(-1), els(nm), nextsis(nm) { for (Int $\scriptstyle { \dot { \ j } } = 0$ ; j<nm; ${ \mathrm { j } } + +$ ) {nextsis[j] $\ c = \ - - 2 ; \}$ Initialize to “empty”.   
}

template<class keyT, class elT, class hfnT> Int Mhash<keyT,elT,hfnT>::store(const keyT &key, const elT &el) {

Store an element el under key. Return index in 0..nmax-1, giving the storage location utilized

Int j,k;   
${ \dot { \mathrm { ~  ~ j ~ } } } =$ iset(key);   
if (nextsis[j] $= = - 2 )$ { Find root index for this key.   
It is the first object with this key.

els[j] = el; nextsis[j] = -1; 1 means it is the terminal element. return j; } else { while (nextsis[j] $! = ~ - 1 )$ {j $=$ nextsis[j];} Traverse the tree. $\mathrm { ~ \bf ~ k ~ } =$ ireserve(); Get a new index and link it into the list. els[k] $\begin{array} { r l } { = } & { { } \ominus 1 } \end{array}$ ; nextsis[j] $\mathit { \Theta } = \mathit { \Theta } \mathbf { k }$ ; nextsis[k] $\ c = - 1$ ; return k; } }

template<class keyT, class elT, class hfnT> Int Mhash<keyT,elT,hfnT>::erase(const keyT &key, const elT &el) {

Erase an element el previously stored under key. Return 1 for success, or 0 if no matching element is found. Note: The $= =$ operation must be defined for the type elT.

Save index of matching el as j.

Int $\mathrm { j ~ = ~ - 1 , k p ~ = ~ - 1 , k p p ~ = ~ - 1 ; }$ ; Int k $=$ iget(key); while (k $> = ~ 0$ ) { if (j < 0 && el $= =$ els[k]) $\dot { \mathrm { ~  ~ j ~ } } = { \bf \ k } ;$ kpp $=$ kp; $\mathrm { k p } ~ = ~ \mathrm { k }$ ; $\mathrm { k } =$ nextsis[k]; } if $( \ j \ < \ 0 )$ ) return 0; if (kpp $<$ 0) { ierase(key); nextsis[j] $= ~ - 2$ ; } else { if (j $! =$ kp) els[j] $=$ els[kp]; nextsis[kpp] $\ c = - 1$ ; irelinquish(kp); nextsis[kp] $= ~ - 2$ ; } return 1; }

No matching el found.   
The element el was unique under key.

Patch the list. Overwrite j with the terminal element and then shorten the list.

Success.

#

template<class keyT, class elT, class hfnT> Int Mhash<keyT,elT,hfnT>::count(const keyT &key) { Return the number of elements stored under key, 0 if none.

Int next, $\texttt { n } = \texttt { 1 }$ ;   
if ((next $=$ iget(key)) $< \ 0 )$ return 0;   
while ((next $=$ nextsis[next]) $> = \ 0 $ ) $\{ \mathtt { n } + +$ ;} return n;

# }

template<class keyT, class elT, class hfnT>   
Int Mhash<keyT,elT,hfnT>::getinit(const keyT &key) {   
Initialize nextget so that it points to the first element stored under key. Return 1 for success, or 0 if no such element.

nextget $=$ iget(key); return ((nextget $<$ 0)? 0 : 1); }

template<class keyT, class elT, class hfnT>   
Int Mhash<keyT,elT,hfnT>::getnext(elT &el)   
If nextget points validly, copy its element into el, update nextget to the next element with the same key, and return 1. Otherwise, do not modify el, and return 0.

if (nextget $\mathit { \Theta } < \mathit { \Theta } 0$ ) {return 0;} el $=$ els[nextget]; nextget $=$ nextsis[nextget]; return 1;

The methods getinit and getnext are designed to be used in code like this, where myhash is a variable of type Mhash:

Retrieve all elements el stored under a single key and do something with them.

if (myhash.getinit(&key)) { while (myhash.getnext(el)) 3 Here use the returned element el. }   
}

# 7.6.5 Usage Examples

Having exposed in such detail the inner workings of the Hash and Mhash classes, we may have left the impression that these are difficult to use. Quite the contrary. Here’s a piece code that declares a hash memory for integers, and then stores the birth years of some personages:

Hash<string,Int,Hashfn2> year(1000,1000);

year[string("Marie Antoinette") $\begin{array} { r l r } { \mathrm {  ~ \Omega ~ } } \end{array} | \mathrm {  ~ \Sigma ~ } \ = \ 1 7 5 5$ ;   
year[string("Ludwig van Beethoven") $\mathrm { ~ \textmu ~ } ] \mathrm { ~ \textmu ~ } = \mathrm { ~ \textmu ~ } _ { 1 } 7 7 0$ ;   
year[string("Charles Babbage" $) ] ~ = ~ 1 7 9 1$ ;

As declared, year can hold up to 1000 entries. We use the $\mathrm { C } { + } { + }$ string class as the key type. If we want to know how old Marie was when Charles was born, we can write,

Int diff $=$ year[string("Charles Babbage")] - year[string("Marie Antoinette")];   
cout $< <$ diff $< < \mathbf { \zeta } ^ { , } \setminus \mathbf { n } ^ { \prime }$ ;

which prints $\mathit { \Omega } ^ { 6 6 } 3 6 ^ { \circ }$ .

Instead of using the $\mathrm { C } { + } { + }$ string class, you can, if you must, use null terminated C strings as keys, like this:

Hash<char,Int,Hashfn2> yearc(1000,1000);   
yearc["Charles Babbage" $\mathbf { \hat { \Sigma } } [ 0 ] ] \ = \ \mathbf { \hat { \Sigma } } _ { 1 7 9 1 }$ ;

This works because Hashfn2 has a special tweak, mentioned above, for key types that are apparently one byte long. Note the required use of [0] to send only the first byte of the C string; but that byte is passed by address, so Hashfn2 knows where to find the rest of the string. (The syntax yearc[\*"Charles Babbage"] is equivalent, also sending the first byte.)

Suppose we want to go the other direction, namely store the names of people into a hash memory indexed by birth year. Since more than one person may be born in a single year, we want to use a hash multimap memory, Mhash:

Mhash<Int,string,Hashfn2> person(1000,1000);

person.store(1775, string("Jane Austen"));   
person.store(1791, string("Charles Babbage"));   
person.store(1767, string("Andrew Jackson"));   
person.store(1791, string("James Buchanan"));   
person.store(1767, string("John Quincy Adams"));   
person.store(1770, string("Ludwig van Beethoven"));   
person.store(1791, string("Samuel Morse"));   
person.store(1755, string("Marie Antoinette"));