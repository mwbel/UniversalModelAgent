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