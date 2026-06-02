Linear prediction is especially successful at extrapolating signals that are smooth and oscillatory, though not necessarily periodic. In such cases, linear prediction often extrapolates accurately through many cycles of the signal. By contrast, polynomial extrapolation in general becomes seriously inaccurate after at most a cycle or two. A prototypical example of a signal that can successfully be linearly predicted is the height of ocean tides, for which the fundamental 12-hour period is modulated in phase and amplitude over the course of the month and year, and for which local hydrodynamic effects may make even one cycle of the curve look rather different in shape from a sine wave.

We already remarked that equation (13.6.10) is not necessarily the best way to estimate the covariances $\phi _ { k }$ from the data set. In fact, results obtained from linear prediction are remarkably sensitive to exactly how the $\phi _ { k }$ ’s are estimated. One particularly good method is due to Burg [1], and involves a recursive procedure for increasing the order $M$ by one unit at a time, at each stage re-estimating the coefficients $d _ { j }$ , $j = 0 , \ldots , M - 1$ so as to minimize the residual in equation (13.6.13). Although further discussion of the Burg method is beyond our scope here, the method is implemented in the following routine [1,2] for estimating the LP coefficients $d _ { j }$ of a data set.

# void memcof(VecDoub_I &data, Doub &xms, VecDoub_O &d) {

Given a real vector of data[0..n-1], this routine returns m linear prediction coefficients as d[0..m-1], and returns the mean square discrepancy as xms.

Int k,j,i, $\mathbf { n } =$ data.size(), $\mathrm { m } { = } \mathrm { d }$ .size();   
Doub $\mathtt { p } { = } 0 . 0$ ;   
VecDoub wk1(n),wk2(n),wkm(m);   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) p $+ =$ SQR(data[j]);   
xms=p/n;   
wk1[0] $=$ data[0];   
wk2[n-2] $=$ data[n-1];   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<n-1;j $^ { + + }$ ) { wk1[j] $=$ data[j]; wk2[j-1] $=$ data[j];   
}   
for ( $\scriptstyle 1 = 0$ ;k<m;k++) { Doub num $_ { 1 = 0 }$ .0,denom $\mathtt { = 0 }$ .0; for ( $\scriptstyle \mathbf { j } = 0$ ;j<(n-k-1);j++) { num $+ =$ (wk1[j]\*wk2[j]); denom $+ =$ (SQR(wk1[j])+SQR(wk2[j])); } d[k] $^ { = 2 }$ .0\*num/denom; xms $\ast =$ (1.0-SQR(d[k])); for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<k; $\dot { 1 } + +$ ) d[i] $=$ wkm[i]-d[k]\*wkm[k-1-i]; The algorithm is recursive, building up the answer for larger and larger values of m until the desired value is reached. At this point in the algorithm, one could return the vector d and scalar xms for a set of LP coefficients with k (rather than m) terms. if $( \mathrm { k \Omega } = = \mathrm { m } - 1$ ) return; for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<=k;i++) wkm[i] $=$ d[i]; for (j=0;j<(n-k-2); $\mathrm { j } + + \mathrm { i }$ ) { wk1[j] $- =$ (wkm[k]\*wk2[j]); wk2[j] $=$ wk2[j+1]-wkm[k]\*wk1[j+1]; }   
}   
throw("never get here in memcof");

Here are procedures for rendering the LP coefficients stable (if you choose to do so) and for extrapolating a data set by linear prediction, using the original or massaged LP coefficients. The routine zroots $( \ S 9 . 5 )$ is used to find all complex roots of a polynomial.

# void fixrts(VecDoub_IO &d) {

Given the LP coefficients d[0..m-1], this routine finds all roots of the characteristic polynomial (13.6.14), reflects any roots that are outside the unit circle back inside, and then returns a modified set of coefficients d[0..m-1].

Bool polish=true;   
Int i,j, $\mathtt { m } = \mathtt { d }$ .size();   
VecComplex a $\left( \mathtt { m } + 1 \right)$ ,roots(m);   
a[m] $= 1$ .0;   
for $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<m;j++) Set up complex coefficients for polynomial root a[j] $=$ -d[m-1-j]; finder.   
zroots(a,roots,polish); Find all the roots.   
for (j=0;j<m;j++) Look for a root outside the unit circle, and reflect if (abs(roots[j]) > 1.0) it back inside. roots[j] $= 1$ .0/conj(roots[j]);   
a[0] $=$ -roots[0]; Now reconstruct the polynomial coefficients,   
a[1] $= 1$ .0;   
for (j=1;j<m;j++) { by looping over the roots a[j+1] $^ { = 1 }$ .0; for (i=j; $\dot { 1 } > = 1$ ;i--) and synthetically multiplying. a[i] $= \mathtt { a }$ [i-1]-roots[j]\*a[i]; a[0] $=$ -roots[j]\*a[0];   
for (j=0;j<m;j++) The polynomial coefficients are guaranteed to be d[m-1-j] $=$ -real(a[j]); real, so we need only return the real part as new LP coefficients.

Given data[0..ndata-1], and given the data’s LP coefficients d[0..m-1], this routine applies equation (13.6.11) to predict the next nfut data points, which it returns in the array future[0..nfut-1]. Note that the routine references only the last m values of data, as initial values for the prediction.

Int k,j,ndata=data.size(), $\mathrm { m } =$ d.size(),nfut $=$ future.size();   
Doub sum,discrp;   
VecDoub reg(m);   
for $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<m; $\mathrm { j } + +$ ) reg[j] $=$ data[ndata-1-j];   
for $( \ j = 0$ ;j<nfut; $\mathrm { j } + +$ ) { discrp ${ = } 0$ .0; This is where you would put in a known discrepancy if you were reconstructing a function by linear predictive coding rather than extrapolating a function by linear prediction. See text. sum $\cdot ^ { = }$ discrp; for $( \mathrm { k } = 0$ ;k<m;k $^ { + + }$ ) sum $+ =$ d[k]\*reg[k]; for $( \mathtt { k } { = } \mathtt { m } { - } 1 ; \mathtt { k } { > } { = } 1 ; \mathtt { k } { - }$ --) reg[k] $\equiv$ reg[k-1]; [If you want to implement circular future[j] $=$ reg[0] $=$ sum; arrays, you can avoid this shift-  
} ing of coefficients.]

# 13.6.3 Removing the Bias in Linear Prediction

You might expect that the sum of the $d _ { j }$ ’s in equation (13.6.11) (or, more generally, in equation 13.6.2) should be 1, so that, e.g., adding a constant to all the data points $y _ { i }$ yields a prediction that is increased by the same constant. However, the $d _ { j }$ ’s do not sum to 1 but, in general, to a value slightly less than one. This fact reveals a subtle point, that the estimator of classical linear prediction is not unbiased, even though it does minimize the mean square discrepancy. At any place where the measured autocorrelation does not imply a better estimate, the equations of linear prediction tend to predict a value that tends toward zero.

Sometimes, that is just what you want. If the process that generates the $y _ { i }$ ’s in fact has zero mean, then zero is the best guess absent other information. At other times, however, this behavior is unwarranted. If you have data that show only small variations around a positive value, you don’t want linear predictions that droop toward zero.

Often it is a workable approximation to subtract the mean off your data set, perform the linear prediction, and then add the mean back. This procedure contains the germ of the correct solution; but the simple arithmetic mean is not quite the correct constant to subtract. In fact, an unbiased estimator is obtained by subtracting from every data point an autocorrelation-weighted mean defined by [3,4]

$$
\overline { { { y } } } \equiv \sum _ { \beta } \left[ \phi _ { \mu \nu } + \eta _ { \mu \nu } \right] _ { \alpha \beta } ^ { - 1 } y _ { \beta } \Bigg / \sum _ { \alpha \beta } \left[ \phi _ { \mu \nu } + \eta _ { \mu \nu } \right] _ { \alpha \beta } ^ { - 1 }
$$

With this subtraction, the sum of the LP coefficients should be unity, up to roundoff and differences in how the $\phi _ { k }$ ’s are estimated.

Equations (3.7.14) and (3.7.15), given in connection with kriging, are in fact exactly equivalent to equations (13.6.6) and (13.6.7) if the mean (13.6.18) is used to remove the estimator bias. To prove this, start by writing the inverse of the matrix (3.7.13) in the obvious partitioned form (e.g., using equation 2.7.23).

# 13.6.4 Linear Predictive Coding (LPC)

A different, though related, method to which the formalism above can be applied is the “compression” of a sampled signal so that it can be stored more compactly. The original form should be exactly recoverable from the compressed version. Obviously, compression can be accomplished only if there is redundancy in the signal. Equation (13.6.11) describes one kind of redundancy: It says that the signal, except for a small discrepancy, is predictable from its previous values and from a small number of LP coefficients. Compression of a signal by the use of (13.6.11) is thus called linear predictive coding, or $L P C$ .

The basic idea of LPC (in its simplest form) is to record as a compressed file (i) the number of LP coefficients $M$ ; (ii) their $M$ values, e.g., as obtained by memcof; (iii) the first $M$ data points; and then (iv) for each subsequent data point only its residual discrepancy $x _ { i }$ (equation 13.6.1). When you are creating the compressed file, you find the residual by applying (13.6.1) to the previous $M$ points, subtracting the sum from the actual value of the current point. When you are reconstructing the original file, you add the residual back in, at the point indicated in the routine predic.

It may not be obvious why there is any compression at all in this scheme. After all, we are storing one value of residual per data point! Why not just store the original data point? The answer depends on the relative sizes of the numbers involved. The residual is obtained by subtracting two very nearly equal numbers (the data and the linear prediction). Therefore, the discrepancy typically has only a very small number of nonzero bits. These can be stored in a compressed file. How do you do it in a high-level language? A rudimentary approach would be to scale your data to have integer values, say between $+ 1 0 0 0 0 0 0$ and $- 1 0 0 0 0 0 0$ (supposing that you need six significant figures). Now modify equation (13.6.11) by enclosing the sum term in an “integer part of” operator. The discrepancy will now, by definition, be an integer. Experiment with different values of $M$ to find LP coefficients that make the range of the discrepancy as small as you can. If you can get to within a range of $\pm 1 2 7$ (and in our experience this is not at all difficult), then you can write it to a file as a single byte. This is a compression factor of 4, compared to 4-byte integer or floating formats.

Notice that the LP coefficients are computed using the quantized data, and that the discrepancy is also quantized, i.e., quantization is done both outside and inside the LPC loop. If you are careful in following this prescription, then, apart from the initial quantization of the data, you will not introduce even a single bit of roundoff error into the compression-reconstruction process: While the evaluation of the sum in (13.6.11) may have roundoff errors, the residual that you store is the value that, when added back to the sum, gives exactly the original (quantized) data value. Notice also that you do not need to massage the LP coefficients for stability; by adding the residual back in to each point, you never depart from the original data, so instabilities cannot grow. There is therefore no need for fixrts, above.

Look at $\ S 2 2 . 5$ to learn about Huffman coding, which will further compress the residuals by taking advantage of the fact that smaller values of discrepancy will occur more often than larger values. A very primitive version of Huffman coding would be this: If most of the discrepancies are in the range $\pm 1 2 7$ , but an occasional one is outside, then reserve the value 127 to mean “out of range,” and then record on the file (immediately following the 127) a full-word value of the out-of-range discrepancy. Section 22.5 explains how to do much better.

There are many variant procedures that all fall under the rubric of LPC:

- If the spectral character of the data is time-variable, then it is best not to use a single set of LP coefficients for the whole data set, but rather to partition the data into segments, computing and storing different LP coefficients for each segment.   
- If the data are really well characterized by their LP coefficients, and you can tolerate some small amount of error, then don’t bother storing all of the residuals. Just do linear prediction until you are outside of tolerances, and then reinitialize (using $M$ sequential stored residuals) and continue predicting.   
- In some applications, most notably speech synthesis, one cares only about the spectral content of the reconstructed signal, not the relative phases. In this case, one need not store any starting values at all, but only the LP coefficients for each segment of the data. The output is reconstructed by driving these coefficients with initial conditions consisting of all zeros except for one nonzero spike. A speech synthesizer chip may have of order $1 0 \mathrm { { L P } }$ coefficients, which change perhaps 20 to 50 times per second.   
- Some people believe that it is interesting to analyze a signal by LPC, even when the residuals $x _ { i }$ are not small. The $x _ { i }$ ’s are then interpreted as the underlying “input signal” that, when filtered through the all-poles filter defined by the LP coefficients (see $\ S 1 3 . 7 )$ , produces the observed “output signal.” LPC reveals simultaneously, it is said, the nature of the filter and the particular input that is driving it. We are skeptical of these applications; the literature, however, is full of extravagant claims.

# CITED REFERENCES AND FURTHER READING:

Childers, D.G. (ed.) 1978, Modern Spectrum Analysis (New York: IEEE Press), especially the paper by J. Makhoul, “Linear Prediction: A Tutorial Review,” reprinted from Proceedings of the IEEE,vol.63,p.561,1975.

Burg, J.P. 1968, “A New Analysis Technique for Time Series Data,” reprinted in Childers, 1978.[1]

Anderson, N. 1974, “On the Calculation of Filter Coefficients for Maximum Entropy Spectral Analysis,” Geophysics, vol. 39, pp. 69–72, reprinted in Childers, 1978.[2]

Cressie, N. 1991, “Geostatistical Analysis of Spatial Data,” in Spatial Statistics and Digital Image Analysis (Washington: National Academy Press).[3]

Press, W.H., and Rybicki, G.B. 1992, “Interpolation, Realization, and Reconstruction of Noisy, Irregularly Sampled Data,” Astrophysical Journal, vol. 398, pp. 169–176.[4]

# 13.7 Power Spectrum Estimation by the Maximum Entropy (All-Poles) Method

The FFT is not the only way to estimate the power spectrum of a process, nor is it necessarily the best way for all purposes. To see how one might devise another method, let us enlarge our view for a moment, so that it includes not only real frequencies in the Nyquist interval $- f _ { c } < f < f _ { c }$ , but also the entire complex frequency plane. From that vantage point, let us transform the complex $f$ -plane to a new plane, called the $z$ -transform plane or z-plane, by the relation

$$
z \equiv e ^ { 2 \pi i f \Delta }
$$

where $\Delta$ is, as usual, the sampling interval in the time domain. Notice that the Nyquist interval on the real axis of the $f$ -plane maps one-to-one onto the unit circle in the complex $z$ -plane.

If we now compare (13.7.1) to equations (13.4.4) and (13.4.6), we see that the FFT power spectrum estimate (13.4.5) for any real sampled function $c _ { k } \equiv c ( t _ { k } )$ can be written, except for normalization convention, as

$$
P ( f ) = \left| \sum _ { k = - N / 2 } ^ { N / 2 - 1 } c _ { k } z ^ { k } \right| ^ { 2 }
$$

Of course, (13.7.2) is not the true power spectrum of the underlying function $c ( t )$ , but only an estimate. We can see in two related ways why the estimate is not likely to be exact. First, in the time domain, the estimate is based on only a finite range of the function $c ( t )$ , which may, for all we know, have continued from $t = - \infty$ to $\infty$ . Second, in the $z$ -plane of equation (13.7.2), the finite Laurent series offers, in general, only an approximation to a general analytic function of $Z$ . In fact, a formal expression for representing “true” power spectra (up to normalization) is

$$
P ( f ) = \left| \sum _ { k = - \infty } ^ { \infty } c _ { k } z ^ { k } \right| ^ { 2 }
$$

This is an infinite Laurent series that depends on an infinite number of values $c _ { k }$ . Equation (13.7.2) is just one kind of analytic approximation to the analytic function of $z$ represented by (13.7.3), the kind, in fact, that is implicit in the use of FFTs to estimate power spectra by periodogram methods. It goes under several names, including direct method, all-zero model, and moving average (MA) model. The term “all-zero” in particular refers to the fact that the model spectrum can have zeros in the $z$ -plane, but not poles.

If we look at the problem of approximating (13.7.3) more generally, it seems clear that we could do a better job with a rational function, one with a series of type (13.7.2) in both the numerator and the denominator. Less obviously, it turns out that there are some advantages in an approximation whose free parameters all lie in the denominator, namely,

$$
P ( f ) \approx { \frac { 1 } { \left| \displaystyle \sum _ { k = - M / 2 } ^ { M / 2 } b _ { k } z ^ { k } \right| ^ { 2 } } } = { \frac { a _ { 0 } } { \left| 1 + \displaystyle \sum _ { k = 1 } ^ { M } a _ { k } z ^ { k } \right| ^ { 2 } } }
$$

Here the second equality brings in a new set of coefficients $a _ { k }$ ’s, which can be determined from the $b _ { k }$ ’s using the fact that $z$ lies on the unit circle. The $b _ { k }$ ’s can be thought of as being determined by the condition that power series expansion of (13.7.4) agree with the first $M + 1$ terms of (13.7.3). In practice, as we shall see, one determines the $b _ { k }$ ’s or $a _ { k }$ ’s by another method.

The differences between the approximations (13.7.2) and (13.7.4) are not just cosmetic. They are approximations of very different character. Most notable is the fact that (13.7.4) can have poles, corresponding to infinite power spectral density, on the unit $z$ -circle, i.e., at real frequencies in the Nyquist interval. Such poles can provide an accurate representation for underlying power spectra that have sharp, discrete “lines” or delta-functions. By contrast, (13.7.2) can have only zeros, not poles, at real frequencies in the Nyquist interval, and must thus attempt to fit sharp spectral features with, essentially, a polynomial. The approximation (13.7.4) goes under several names: all-poles model, maximum entropy method (MEM), autoregressive model (AR). We need only find out how to compute the coefficients $a _ { 0 }$ and the $a _ { k }$ ’s from a data set, so that we can actually use (13.7.4) to obtain spectral estimates.

A pleasant surprise is that we already know how! Look at equation (13.6.11) for linear prediction. Compare it with linear filter equations (13.5.1) and (13.5.2), and you will see that, viewed as a filter that takes input $x$ ’s into output $y$ ’s, linear prediction has a filter function

$$
\mathcal { H } ( f ) = \frac { 1 } { 1 - \displaystyle \sum _ { j = 0 } ^ { N - 1 } d _ { j } z ^ { - ( j + 1 ) } }
$$

Thus, the power spectrum of the $y$ ’s should be equal to the power spectrum of the $x$ ’s multiplied by $| { \mathcal { H } } ( f ) | ^ { 2 }$ . Now let us think about what the spectrum of the input $x$ ’s is, when they are residual discrepancies from linear prediction. Although we will not prove it formally, it is intuitively believable that the $x$ ’s are independently random and therefore have a flat (white noise) spectrum. (Roughly speaking, any residual correlations left in the $x$ ’s would have allowed a more accurate linear prediction, and would have been removed.) The overall normalization of this flat spectrum is just the mean square amplitude of the $x$ ’s. But this is exactly the quantity computed in equation (13.6.13) and returned by the routine memcof as xms. Thus, the coefficients $a _ { 0 }$ and $a _ { k }$ in equation (13.7.4) are related to the LP coefficients returned by memcof simply by

$$
a _ { 0 } = \tt x m s a _ { k } = - d ( k - 1 ) , \quad k = 1 , \ldots , M
$$

There is also another way to describe the relation between the $a _ { k }$ ’s and the autocorrelation components $\phi _ { k }$ . The Wiener-Khinchin theorem (12.0.13) says that the Fourier transform of the autocorrelation is equal to the power spectrum. In $z$ -transform language, this Fourier transform is just a Laurent series in $z$ . The equation that is to be satisfied by the coefficients in equation (13.7.4) is thus

$$
\frac { a _ { 0 } } { \left| 1 + \sum _ { k = 1 } ^ { M } a _ { k } z ^ { k } \right| ^ { 2 } } \approx \sum _ { j = - M } ^ { M } \phi _ { j } z ^ { j }
$$

The approximately equal sign in (13.7.7) has a somewhat special interpretation. It means that the series expansion of the left-hand side is supposed to agree with the right-hand side term-by-term from $z ^ { - M }$ to $z ^ { M }$ . Outside this range of terms, the right-hand side is obviously zero, while the left-hand side will still have nonzero terms. Notice that $M$ , the number of coefficients in the approximation on the left-hand side, can be any integer up to $N$ , the total number of autocorrelations available. (In practice, one often chooses $M$ much smaller than $N$ .) $M$ is called the order or number of poles of the approximation.

Whatever the chosen value of $M$ , the series expansion of the left-hand side of (13.7.7) defines a certain sort of extrapolation of the autocorrelation function to lags larger than $M$ , in fact even to lags larger than $N$ , i.e., larger than the run of data can actually measure. It turns out that this particular extrapolation can be shown to have, among all possible extrapolations, the maximum entropy in a definable information-theoretic sense. Hence the name maximum entropy method, or MEM. The maximum entropy property has caused MEM to acquire a certain “cult” popularity; one sometimes hears that it gives an intrinsically “better” estimate than is given by other methods. Don’t believe it. MEM has the very cute property of being able to fit sharp spectral features, but there is nothing else magical about its power spectrum estimates.

The operations count in memcof scales as the product of $N$ (the number of data points) and $M$ (the desired order of the MEM approximation). If $M$ were chosen to be as large as $N$ , then the method would be much slower than the $N \log N$ FFT methods of the previous section. In practice, however, one usually wants to limit the order (or number of poles) of the MEM approximation to a few times the number of sharp spectral features that one desires it to fit. With this restricted number of poles, the method will smooth the spectrum somewhat, but this is often a desirable property. While exact values depend on the application, one might take $M = 1 0$ or 20 or 50 for $N = 1 0 0 0$ or 10000. In that case, MEM estimation is not much slower than FFT estimation.

We feel obliged to warn you that memcof can be a bit quirky at times. If the number of poles or number of data points is too large, roundoff error can be a problem, even in double precision. With “peaky” data (i.e., data with extremely sharp spectral features), the algorithm may suggest split peaks even at modest orders, and the peaks may shift with the phase of the sine wave. Also, with noisy input functions, if you choose too high an order, you will find spurious peaks galore! Some experts recommend the use of this algorithm in conjunction with more conservative methods, like periodograms, to help choose the correct model order and to avoid getting too fooled by spurious spectral features. MEM can be finicky, but it can also do remarkable things. We recommend that you try it out, cautiously, on your own problems. We now turn to the evaluation of the MEM spectral estimate from its coefficients.

The MEM estimation (13.7.4) is a function of continuously varying frequency $f$ . There is no special significance to specific equally spaced frequencies as there was in the FFT case. In fact, since the MEM estimate may have very sharp spectral features, one wants to be able to evaluate it on a very fine mesh near to those features, but perhaps only more coarsely farther away from them. Here is a function that, given the coefficients already computed, evaluates (13.7.4) and returns the estimated power spectrum as a function of $f \Delta$ (the frequency times the sampling interval). Of course, $f \Delta$ should lie in the Nyquist range between $- 1 / 2$ and $1 / 2$ .

Doub evlmem(const Doub fdt, VecDoub_I &d, const Doub xms)   
Given d[0..m-1] and xms as returned by memcof, this function returns the power spectrum estimate $P ( f )$ as a function of fdt $= f \dot { \Delta }$ .

# Int i;

Doub sumr $\scriptstyle \cdot = 1$ .0,sumi ${ = } 0$ .0, $\mathtt { w r } { = } 1$ .0,wi=0.0,wpr,wpi,wtemp,theta;

Set up for recurrence relations.

Loop over the terms in the sum.

Int $\mathtt { m } = \mathtt { d }$ .size();   
thet $_ { 1 } = 6$ .28318530717959\*fdt;   
wpr cos(theta);   
wpi $\equiv$ sin(theta);   
for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<m; $\dot { \bf 1 } + +$ ) { $\kappa x =$ (wtemp=wr)\*wpr-wi\*wpi; wi=wi\*wpr+wtemp\*wpi; sumr $- =$ d[i]\*wr; sumi $- =$ d[i]\*wi;   
}   
return xms/(sumr\*sumr+sumi\*sumi);

These accumulate the denominator of (13.7.4).

![](images/7866d0eff8ef9f4e768a33f8ecdc14d2e429842f5922f7a2d7f87c59aa58eeac.jpg)  
Figure 13.7.1. Sample output of maximum entropy spectral estimation. The input signal consists of 512 samples of the sum of two sinusoids of very nearly the same frequency, plus white noise with about equal power. Shown is an expanded portion of the full Nyquist frequency interval (which would extend from zero to 0.5). The dashed spectral estimate uses 20 poles; the dotted, 40; the solid, 150. With the larger number of poles, the method can resolve the distinct sinusoids, but the flat noise background is beginning to show spurious peaks. (Note logarithmic scale.)

Be sure to evaluate $P ( f )$ on a fine enough grid to find any narrow features that may be there! Such narrow features, if present, can contain virtually all of the power in the data. You might also wish to know how the $P ( f )$ produced by the routines memcof and evlmem is normalized with respect to the mean square value of the input data vector. The answer is

$$
\int _ { - 1 / 2 } ^ { 1 / 2 } P ( f \Delta ) d ( f \Delta ) = 2 \int _ { 0 } ^ { 1 / 2 } P ( f \Delta ) d ( f \Delta ) = \mathrm { m e a n ~ s q u a r e ~ v a l u e ~ o f ~ d a t a }
$$

Sample spectra produced by the routines memcof and evlmem are shown in Figure 13.7.1.

# CITED REFERENCES AND FURTHER READING:

Childers, D.G. (ed.) 1978, Modern Spectrum Analysis (New York: IEEE Press), Chapter II. Kay, S.M., and Marple, S.L. 1981, “Spectrum Analysis: A Modern Perspective,” Proceedings of the IEEE,vol.69,pp.1380-1419.

# 13.8 Spectral Analysis of Unevenly Sampled Data

Thus far, we have been dealing exclusively with evenly sampled data,

$$
h _ { n } = h ( n \Delta ) \qquad n = \dots , - 3 , - 2 , - 1 , 0 , 1 , 2 , 3 , \dots .
$$

where $\Delta$ is the sampling interval, whose reciprocal is the sampling rate. Recall also (-12.1) the significance of the Nyquist critical frequency

$$
f _ { c } \equiv \frac { 1 } { 2 \Delta }
$$

as codified by the sampling theorem: A sampled data set like equation (13.8.1) contains complete information about all spectral components for a signal $h ( t )$ containing only frequencies below the Nyquist frequency, and scrambled or aliased information about any signals containing frequencies larger than the Nyquist frequency. The sampling theorem thus defines both the attractiveness and the limitation of any analysis of an evenly spaced data set.

There are situations, however, where evenly spaced data cannot be obtained. A common case is where instrumental dropouts occur, so that data are obtained only on a (not consecutive integer) subset of equation (13.8.1), the so-called missing data problem. Another case, common in observational sciences like astronomy, is that the observer cannot completely control the time of the observations, but must simply accept a certain dictated set of $t _ { i }$ ’s.

There are some obvious ways to get from unevenly spaced $t _ { i }$ ’s to evenly spaced ones, as in equation (13.8.1). Interpolation is one way: Lay down a grid of evenly spaced times on your data and interpolate values onto that grid; then use FFT methods. In the missing data problem, you only have to interpolate on missing data points. If a lot of consecutive points are missing, you might as well just set them to zero, or perhaps “clamp” the value at the last measured point. However, the experience of practitioners of such interpolation techniques is not reassuring. Generally speaking, such techniques perform poorly. Long gaps in the data, for example, often produce a spurious bulge of power at low frequencies (wavelengths comparable to gaps).

A completely different method of spectral analysis for unevenly sampled data, one that mitigates these difficulties and has some other very desirable properties, was developed by Lomb [1], based in part on earlier work by Barning [2] and Van´ıcekˇ [3], and additionally elaborated by Scargle [4]. The Lomb method (as we will call it) evaluates data, and sines and cosines, only at times $t _ { i }$ that are actually measured. Suppose that there are $N$ data points $h _ { i } \equiv h ( t _ { i } ) , i = 0 , . . . , N - 1$ . Then first find the mean and variance of the data by the usual formulas,

$$
\overline { { { h } } } \equiv \frac { 1 } { N } \sum _ { i = 0 } ^ { N - 1 } h _ { i } \qquad \sigma ^ { 2 } \equiv \frac { 1 } { N - 1 } \sum _ { i = 0 } ^ { N - 1 } ( h _ { i } - \overline { { { h } } } ) ^ { 2 }
$$

Now, the Lomb normalized periodogram (spectral power as a function of angular frequency $\omega \equiv 2 \pi f > 0$ ) is defined by

$$
P _ { N } ( \omega ) \equiv \frac { 1 } { 2 \sigma ^ { 2 } } \left\{ \frac { \left[ \sum _ { j } ( h _ { j } - \overline { { h } } ) \cos \omega ( t _ { j } - \tau ) \right] ^ { 2 } } { \sum _ { j } \cos ^ { 2 } \omega ( t _ { j } - \tau ) } + \frac { \left[ \sum _ { j } ( h _ { j } - \overline { { h } } ) \sin \omega ( t _ { j } - \tau ) \right] ^ { 2 } } { \sum _ { j } \sin ^ { 2 } \omega ( t _ { j } - \tau ) } \right\}
$$

Here $\tau$ is defined by the relation

$$
\tan ( 2 \omega \tau ) = { \frac { \sum _ { j } \sin 2 \omega t _ { j } } { \sum _ { j } \cos 2 \omega t _ { j } } }
$$

The constant $\tau$ is a kind of offset that makes $P _ { N } ( \omega )$ completely independent of shifting all the $t _ { i }$ ’s by any constant. Lomb shows that this particular choice of offset has another, deeper, effect: It makes equation (13.8.4) identical to the equation that one would obtain if one

estimated the harmonic content of a data set, at a given frequency $\omega$ , by linear least-squares fitting to the model

$$
h ( t ) = A \cos \omega t + B \sin \omega t
$$

This fact gives some insight into why the method can give results superior to FFT methods: It weights the data on a “per-point” basis instead of on a “per-time interval” basis, when uneven sampling can render the latter seriously in error.

A very common occurrence is that the measured data points $h _ { i }$ are the sum of a periodic signal and independent (white) Gaussian noise. If we are trying to determine the presence or absence of such a periodic signal, we want to be able to give a quantitative answer to the question, “How significant is a peak in the spectrum $P _ { N } ( \omega ) ? ^ { \prime \prime }$ In this question, the null hypothesis is that the data values are independent Gaussian random values. A very nice property of the Lomb normalized periodogram is that the viability of the null hypothesis can be tested fairly rigorously, as we now discuss.

The word “normalized” refers to the factor $\sigma ^ { 2 }$ in the denominator of equation (13.8.4). Scargle [4] shows that with this normalization, at any particular $\omega$ and in the case of the null hypothesis, $P _ { N } ( \omega )$ has an exponential probability distribution with unit mean. In other words, the probability that $P _ { N } ( \omega )$ will be between some positive $z$ and $z + d z$ is $\exp ( - z ) d z$ . It readily follows that, if we scan some $M$ independent frequencies, the probability that none give values larger than $z$ is $( 1 - e ^ { - z } ) ^ { M }$ . So

$$
P ( > z ) \equiv 1 - ( 1 - e ^ { - z } ) ^ { M }
$$

is the false-alarm probability of the null hypothesis, that is, the significance level of any peak in $P _ { N } ( \omega )$ that we do see. A small value for the false-alarm probability indicates a highly significant periodic signal.

To evaluate this significance, we need to know $M$ . After all, the more frequencies we look at, the less significant is some one modest bump in the spectrum. (Look long enough, find anything!) A typical procedure will be to plot $P _ { N } ( \omega )$ as a function of many closely spaced frequencies in some large frequency range. How many of these are independent?

Before answering, let us first see how accurately we need to know $M$ . The interesting region is where the significance is a small (significant) number, $\ll 1$ . There, equation (13.8.7) can be series expanded to give

$$
P ( > z ) \approx M e ^ { - z }
$$

We see that the significance scales linearly with $M$ . Practical significance levels are numbers like 0:05, 0:01, 0:001, etc. An error of even $\pm 5 0 \%$ in the estimated significance is often tolerable, since quoted significance levels are typically spaced apart by factors of 5 or 10. So our estimate of $M$ need not be very accurate.

Horne and Baliunas [5] give results from extensive Monte Carlo experiments for determining $M$ in various cases. In general, $M$ depends on the number of frequencies sampled, the number of data points $N$ , and their detailed spacing. It turns out that $M$ is very nearly equal to $N$ when the data points are approximately equally spaced and when the sampled frequencies “fill” (oversample) the frequency range from 0 to the Nyquist frequency $f _ { c }$ (equation 13.8.2). Further, the value of $M$ is not importantly different for random spacing of the data points than for equal spacing. When a larger frequency range than the Nyquist range is sampled, $M$ increases proportionally. About the only case where $M$ differs significantly from the case of evenly spaced points is when the points are closely clumped, say into groups of three; then (as one would expect) the number of independent frequencies is reduced by a factor of about 3.

The program period, below, calculates an effective value for $M$ based on the above rough-and-ready rules and assumes that there is no important clumping. This will be adequate for most purposes. In any particular case, if it really matters, it is not too difficult to compute a better value of $M$ by simple Monte Carlo: Holding fixed the number of data points and their locations $t _ { i }$ , generate synthetic data sets of Gaussian (normal) deviates, find the largest values of $P _ { N } ( \omega )$ for each such data set (using the accompanying program), and fit the resulting distribution for $M$ in equation (13.8.7).

Figure 13.8.1 shows the results of applying the method as discussed so far. In the upper figure, the data points are plotted against time. Their number is $N = 1 0 0$ , and their distribution in $t$ is Poisson random. There is certainly no sinusoidal signal evident to the eye. The lower figure plots $P _ { N } ( \omega )$ against frequency $f = \omega / 2 \pi$ . The Nyquist critical frequency that would obtain if the points were evenly spaced is at $f = f _ { c } = 0 . 5$ . Since we have searched up to about twice that frequency, and oversampled the $f$ ’s to the point where successive values of $P _ { N } ( \omega )$ vary smoothly, we take $M = 2 N$ . The horizontal dashed and dotted lines are (respectively from bottom to top) significance levels 0.5, 0.1, 0.05, 0.01, 0.005, and 0.001. One sees a highly significant peak at a frequency of 0.81. That is in fact the frequency of the sine wave that is present in the data. (You will have to take our word for this!)

![](images/34029d3f99e85e3e9db73bf5dc23a67d405e4ce326a3935f18a2dd8b9ecde091.jpg)  
Figure 13.8.1. Example of the Lomb algorithm in action. The 100 data points (upper figure) are at random times between 0 and 100. Their sinusoidal component is readily uncovered (lower figure) by the algorithm, at a significance level $p < 0 . 0 0 1$ . If the 100 data points had been evenly spaced at unit interval, the Nyquist critical frequency would have been 0.5. Note that, for these unevenly spaced points, there is no visible aliasing into the Nyquist range.

Note that two other peaks approach but do not exceed the $50 \%$ significance level; that is about what one might expect by chance. It is also worth commenting on the fact that the significant peak was found (correctly) above the Nyquist frequency and without any significant aliasing down into the Nyquist interval! That would not be possible for evenly spaced data. It is possible here because the randomly spaced data have some points spaced much closer than the “average” sampling rate, and these remove ambiguity from any aliasing.

Implementation of the normalized periodogram in code is straightforward, with, however, a few points to be kept in mind. We are dealing with a slow algorithm. Typically, for $N$ data points, we may wish to examine on the order of $2 N$ or $4 N$ frequencies. Each combination of frequency and data point has, in equations (13.8.4) and (13.8.5), not just a few adds or multiplies, but four calls to trigonometric functions; the operations count can easily reach several hundred times $N ^ { 2 }$ . It is highly desirable — in fact results in a factor 4 speedup — to replace these trigonometric calls by recurrences. That is possible only if the sequence of frequencies examined is a linear sequence. Since such a sequence is probably what most users would want anyway, we have built this into the implementation.

At the end of this section we describe a way to evaluate equations (13.8.4) and (13.8.5) approximately, but to any desired degree of approximation — by a fast method [6] whose operation count goes only as $N \log N$ . This faster method should be used for long data sets.

The lowest independent frequency $f$ to be examined is the inverse of the span of the input data, $\operatorname* { m a x } _ { i } \left( t _ { i } \right) - \operatorname* { m i n } _ { i } \left( t _ { i } \right) \equiv T$ . This is the frequency such that the data can include one complete cycle. In subtracting off the data’s mean, equation (13.8.4) already assumed that you are not interested in the data’s zero frequency piece — which is just that mean value. In an FFT method, higher independent frequencies would be integer multiples of $1 / T$ . Because we are interested in the statistical significance of any peak that may occur, however, we had better (over-)sample more finely than at interval $1 / T$ , so that sample points lie close to the top of any peak. Thus, the accompanying program includes an oversampling parameter, called ofac; a value ofac $\gtrsim 4$ might be typical in use. We also want to specify how high in frequency to go, say $f _ { h i }$ . One guide to choosing $f _ { h i }$ is to compare it with the Nyquist frequency $f _ { c }$ that would obtain if the $N$ data points were evenly spaced over the same span $T$ , that is, $f _ { c } = N / ( 2 T )$ . The accompanying program includes an input parameter hifac, defined as $f _ { h i } / f _ { c }$ . The number of different frequencies $N _ { P }$ returned by the program is then given by

$$
N _ { P } = { \frac { \circ { \bf f a c } \times \tt h i f a c } { 2 } } N
$$

(You have to remember to dimension the output arrays to at least this size.)

The trigonometric recurrences should be done in double precision even if you convert the rest of the routine to single precision. The code embodies a few tricks with trigonometric identities, to decrease roundoff errors. If you are an aficionado of such things, you can puzzle it out. A final detail is that equation (13.8.7) will fail because of roundoff error if $z$ is too large; but equation (13.8.8) is fine in this regime.

void period(VecDoub_I &x, VecDoub_I &y, const Doub ofac, const Doub hifac, VecDoub_O &px, VecDoub_O &py, Int &nout, Int &jmax, Doub &prob) {

Given n data points with abscissas $\mathbf { x } \left[ 0 \ldots \ldots \right] $ (which need not be equally spaced) and ordinates $\mathtt { y } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ , and given a desired oversampling factor ofac (a typical value being 4 or larger), this routine fills array px[0..nout-1] with an increasing sequence of frequencies (not angular frequencies) up to hifac times the “average” Nyquist frequency, and fills array py[0..nout-1] with the values of the Lomb normalized periodogram at those frequencies. The arrays x and y are not altered. The vectors px and py are resized to nout (eq. 13.8.9) if their initial size is less than this; otherwise, only their first nout components are filled. The routine also returns jmax such that py[jmax] is the maximum element in py, and prob, an estimate of the significance of that maximum against the hypothesis of random noise. A small value of prob indicates that a significant periodic signal is present.

const Doub TWOP ${ \tt T } { = } 6$ .283185307179586476;   
Int i,j, $\mathbf { n } { = } \mathbf { x }$ .size(),np=px.size();   
Doub ave,c,cc,cwtau,effm,expy,pnow,pymax,s,ss,sumc,sumcy,sums,sumsh, sumsy,swtau,var,wtau,xave,xdif,xmax,xmin,yy,arg,wtemp;   
VecDoub wi(n),wpi(n),wpr(n),wr(n);   
nout $=$ Int(0.5\*ofac\*hifac\*n);   
if (np $<$ nout) {px.resize(nout); py.resize(nout);}   
avevar(y,ave,var); Get mean and variance of the input data.   
if (var $\scriptstyle = = 0 . 0$ ) throw("zero variance in period");   
xmax=xmin $= 8$ [0]; Go through data to get the range of abscis  
for (j=0;j<n;j++) { sas. if (x[j] $>$ xmax) xmax $= \mathrm { x }$ [j]; if (x[j] $<$ xmin) xmin $= 8$ [j];   
}   
xdif $=$ xmax-xmin;   
xave ${ = } 0$ .5\*(xmax+xmin);   
pymax $_ { = 0 }$ .0;   
pnow ${ \tt = } 1$ .0/(xdif\*ofac); Starting frequency.   
for ( $\scriptstyle \mathbf { j } = 0$ ;j<n;j++) { Initialize values for the trigonometric recurarg=TWOPI\*((x[j]-xave)\*pnow); rences at each data point. wpr[j] $=$ -2.0\*SQR(sin(0.5\*arg));

wpi[j]=sin(arg); wr[j]=cos(arg); wi[j]=wpi[j]; for (i=0;i<nout;i++) { Main loop over the frequencies to be evalupx[i]=pnow; ated. sumsh=sumc=0.0; First, loop over the data to get $\tau$ and related for (j=0;j<n;j++) { quantities. c=wr[j]; $\mathrm { { s } = }$ wi[j]; sumsh $+ =$ s\*c; sumc $+ =$ (c-s)\*(c+s); } wtau $= 0$ .5\*atan2(2.0\*sumsh,sumc); swtau=sin(wtau); cwtau $! ^ { = }$ cos(wtau); sums $=$ sumc=sumsy=sumcy ${ \tt = } 0$ .0; Then, loop over the data again to get the for (j=0;j<n;j++) { periodogram value. $\mathrm { { s } = }$ wi[j]; $c =$ wr[j]; ss $=$ s\*cwtau-c\*swtau; cc=c\*cwtau+s\*swtau; sums $+ =$ ss\*ss; sumc $+ =$ cc\*cc; yy=y[j]-ave; sumsy $+ =$ yy\*ss; sumcy $+ =$ yy\*cc; wr[j] $=$ ((wtemp=wr[j])\*wpr[j]-wi[j]\*wpi[j])+wr[j]; Update the trigonowi[j] $=$ (wi[j]\*wpr[j]+wtemp\*wpi[j])+wi[j]; metric recurrences. } py[i] ${ = } 0$ . $^ { 5 \ast }$ (sumcy\*sumcy/sumc+sumsy\*sumsy/sums)/var; if (py[i] $> =$ pymax) pymax=py[jmax=i]; pnow $+ =$ 1.0/(ofac\*xdif); The next frequency. expy=exp(-pymax); Evaluate statistical significance of the maxeffm $^ { 1 = 2 }$ . $^ { 0 * }$ nout/ofac; imum. prob $=$ effm\*expy; if (prob $>$ 0.01) prob $\ L _ { 1 } = \ L _ { 1 }$ .0-pow(1.0-expy,effm);

# 13.8.1 Fast Computation of the Lomb Periodogram

We here show how equations (13.8.4) and (13.8.5) can be calculated — approximately, but to any desired precision — with an operation count only of order $N _ { P } \log N _ { P }$ . The method uses the FFT, but it is in no sense an FFT periodogram of the data. It is an actual evaluation of equations (13.8.4) and (13.8.5), the Lomb normalized periodogram, with exactly that method’s strengths and weaknesses. This fast algorithm, due to Press and Rybicki [6], makes feasible the application of the Lomb method to data sets at least as large as $1 0 ^ { 6 }$ points; it is already faster than straightforward evaluation of equations (13.8.4) and (13.8.5) for data sets as small as 60 or 100 points.

Notice that the trigonometric sums that occur in equations (13.8.5) and (13.8.4) can be reduced to four simpler sums. If we define

$$
S _ { h } \equiv \sum _ { j = 0 } ^ { N - 1 } ( h _ { j } - \overline { { h } } ) \sin ( \omega t _ { j } ) \qquad C _ { h } \equiv \sum _ { j = 0 } ^ { N - 1 } ( h _ { j } - \overline { { h } } ) \cos ( \omega t _ { j } )
$$

and

$$
S _ { 2 } \equiv \sum _ { j = 0 } ^ { N - 1 } \sin ( 2 \omega t _ { j } ) \qquad C _ { 2 } \equiv \sum _ { j = 0 } ^ { N - 1 } \cos ( 2 \omega t _ { j } )
$$

then

$$
\begin{array} { l } { { \displaystyle \sum _ { j = 0 } ^ { N - 1 } ( h _ { j } - \overline { { h } } ) \cos \omega ( t _ { j } - \tau ) = C _ { h } \cos \omega \tau + S _ { h } \sin \omega \tau } } \\ { { \displaystyle \sum _ { j = 0 } ^ { N - 1 } ( h _ { j } - \overline { { h } } ) \sin \omega ( t _ { j } - \tau ) = S _ { h } \cos \omega \tau - C _ { h } \sin \omega \tau } } \\ { { \displaystyle \sum _ { j = 0 } ^ { N - 1 } \cos ^ { 2 } \omega ( t _ { j } - \tau ) = \frac { N } { 2 } + \frac { 1 } { 2 } C _ { 2 } \cos ( 2 \omega \tau ) + \frac { 1 } { 2 } S _ { 2 } \sin ( 2 \omega \tau ) } } \\ { { \displaystyle \sum _ { j = 0 } ^ { N - 1 } \sin ^ { 2 } \omega ( t _ { j } - \tau ) = \frac { N } { 2 } - \frac { 1 } { 2 } C _ { 2 } \cos ( 2 \omega \tau ) - \frac { 1 } { 2 } S _ { 2 } \sin ( 2 \omega \tau ) } } \end{array}
$$

Now notice that $i f$ the $t _ { j }$ s were evenly spaced, then the four quantities $\mathrm { S } _ { h } , C _ { h } , S _ { 2 }$ , and $C _ { 2 }$ could be evaluated by two complex FFTs, and the results could then be substituted back through equation (13.8.12) to evaluate equations (13.8.5) and (13.8.4). The problem is therefore only to evaluate equations (13.8.10) and (13.8.11) for unevenly spaced data.

Interpolation, or rather reverse interpolation — we will here call it extirpolation — provides the key. Interpolation, as classically understood, uses several function values on a regular mesh to construct an accurate approximation at an arbitrary point. Extirpolation, just the opposite, replaces a function value at an arbitrary point by several function values on a regular mesh, doing this in such a way that sums over the mesh are an accurate approximation to sums over the original arbitrary point.

It is not hard to see that the weight functions for extirpolation are identical to those for interpolation. Suppose that the function $h ( t )$ to be extirpolated is known only at the discrete (unevenly spaced) points $h ( t _ { i } ) \equiv h _ { i }$ , and that the function $g ( t )$ (which will be, e.g., cos ! t ) can be evaluated anywhere. Let $\widehat { t } _ { k }$ be a sequence of evenly spaced points on a regular mesh. Then Lagrange interpolation (-3.2) gives an approximation of the form

$$
g ( t ) \approx \sum _ { k } w _ { k } ( t ) g ( \widehat { t } _ { k } )
$$

where $w _ { k } ( t )$ are interpolation weights. Now let us evaluate a sum of interest by the following scheme:

$$
\sum _ { j = 0 } ^ { N - 1 } h _ { j } g ( t _ { j } ) \approx \sum _ { j = 0 } ^ { N - 1 } h _ { j } \biggl [ \sum _ { k } w _ { k } ( t _ { j } ) g ( \hat { t } _ { k } ) \biggr ] = \sum _ { k } \Bigg [ \sum _ { j = 0 } ^ { N - 1 } h _ { j } w _ { k } ( t _ { j } ) \Bigg ] g ( \hat { t } _ { k } ) \equiv \sum _ { k } \hat { h } _ { k } g ( \hat { t } _ { k } )
$$

Here $\begin{array} { r } { \widehat { h } _ { k } \equiv \sum _ { j } h _ { j } w _ { k } ( t _ { j } ) } \end{array}$ . Notice that equation (13.8.14) replaces the original sum by one on the regular mesh. Notice also that the accuracy of equation (13.8.13) depends only on the fineness of the mesh with respect to the function $g$ and has nothing to do with the spacing of the points $t _ { j }$ or the function $h$ ; therefore, the accuracy of equation (13.8.14) also has this property.

The general outline of the fast evaluation method is therefore this: (i) Choose a mesh size large enough to accommodate some desired oversampling factor, and large enough to have several extirpolation points per half-wavelength of the highest frequency of interest. (ii) Extirpolate the values $h _ { i }$ onto the mesh and take the FFT; this gives $S _ { h }$ and $C _ { h }$ in equation (13.8.10). (iii) Extirpolate the constant values 1 onto another mesh, and take its FFT; this, with some manipulation, gives $S _ { 2 }$ and $C _ { 2 }$ in equation (13.8.11). (iv) Evaluate equations (13.8.12), (13.8.5), and (13.8.4), in that order.

There are several other tricks involved in implementing this algorithm efficiently. You can figure most out from the code, but we will mention the following points: (a) A nice way to get transform values at frequencies $2 \omega$ instead of $\omega$ is to stretch the time-domain data by a factor 2, and then wrap it to double-cover the original length. (This trick goes back to Tukey.) In the program, this appears as a modulo function. (b) Trigonometric identities are used to get from the left-hand side of equation (13.8.5) to the various needed trigonometric functions of $\omega \tau$ . $\mathrm { C } { + } { + }$ identifiers like, e.g., cwt and hs2wt represent quantities like, e.g., $\cos \omega \tau$ and ${ \frac { 1 } { 2 } } \sin ( 2 \omega \tau ) $ . (c) The function spread does extirpolation onto the $M$ most nearly centered mesh points around an arbitrary point; its turgid code evaluates coefficients of the Lagrange interpolating polynomials, in an efficient manner.

# void fasper(VecDoub_I &x, VecDoub_I &y, const Doub ofac, const Doub hifac, VecDoub_O &px, VecDoub_O &py, Int &nout, Int &jmax, Doub &prob) {

Given n data points with abscissas $\mathbf { x } \left[ 0 \ldots \ldots \right] $ (which need not be equally spaced) and ordinates $\mathtt { y } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ , and given a desired oversampling factor ofac (a typical value being 4 or larger), this routine fills array px[0..nout-1] with an increasing sequence of frequencies (not angular frequencies) up to hifac times the “average” Nyquist frequency, and fills array py[0..nout-1] with the values of the Lomb normalized periodogram at those frequencies. The arrays x and y are not altered. The vectors px and py are resized to nout (eq. 13.8.9) if their initial size is less than this; otherwise, only their first nout components are filled. The routine also returns jmax such that py[jmax] is the maximum element in py, and prob, an estimate of the significance of that maximum against the hypothesis of random noise. A small value of prob indicates that a significant periodic signal is present.

const Int MACC ${ = } 4$ ;   
Int j,k,nwk,nfreq,nfreqt, $\mathrm { n } { = } \mathrm { x }$ .size(),np=px.size();   
Doub ave,ck,ckk,cterm,cwt,den,df,effm,expy,fac,fndim,hc2wt,hs2wt, hypo,pmax,sterm,swt,var,xdif,xmax,xmin;   
nout $=$ Int(0.5\*ofac\*hifac\*n);   
nfreqt ${ } . = { }$ Int(ofac\*hifac\*n\*MACC); Size the FFT as next power of 2 above   
nfreq=64; nfreqt.   
while (nfreq $<$ nfreqt) nfreq $< < = ~ 1$ ;   
nwk=nfreq $< < ~ 1$ ;   
if (np $<$ nout) {px.resize(nout); py.resize(nout);}   
avevar(y,ave,var); Compute the mean, variance, and range   
if (var $= =$ 0.0) throw("zero variance in fasper"); of the data.   
xmin $\mathbf { \Phi } _ { \cdot } = \mathbf { x }$ [0];   
xmax=xmin;   
for (j=1;j<n;j++) { if (x[j] < xmin) xmin=x[j]; if (x[j] $>$ xmax) xmax=x[j];   
xdif=xmax-xmin;   
VecDoub wk1(nwk,0.); Zero the workspaces.   
VecDoub wk2(nwk,0.);   
fac=nwk/(xdif\*ofac);   
fndim=nwk;   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) { Extirpolate the data into the workspaces. ck=fmod((x[j]-xmin)\*fac,fndim); ckk $^ { - 2 }$ .0\*(ck++); ckk=fmod(ckk,fndim); $^ { + + }$ ckk; spread(y[j]-ave,wk1,ck,MACC); spread(1.0,wk2,ckk,MACC);   
}   
realft(wk1,1); Take the Fast Fourier Transforms.   
realft(wk2,1);   
df $\ l = 1$ .0/(xdif\*ofac);   
pmax $=$ -1.0;   
for ( $\scriptstyle 1 = 2$ , $\scriptstyle \mathrm { j } = 0$ ;j<nout;j++,k+=2) { Compute the Lomb value for each frehypo=sqrt(wk2[k]\*wk2[k]+wk2[k+1]\*wk2[k+1]); quency. hc2wt ${ = } 0$ .5\*wk2[k]/hypo; hs2wt ${ = } 0$ .5\*wk2[k+1]/hypo; cwt $=$ sqrt(0.5+hc2wt); swt $=$ SIGN(sqrt(0.5-hc2wt),hs2wt); den $_ { = 0 }$ .5\*n+hc2wt\*wk2[k]+hs2wt\*wk2[k+1]; cterm $\cdot ^ { = }$ SQR(cwt\*wk1[k]+swt\*wk1[k+1])/den; sterm $_ { 1 } =$ SQR(cwt\*wk1[k+1]-swt\*wk1[k])/(n-den); px[j] $=$ (j+1)\*df; py[j] $=$ (cterm+sterm)/(2.0\*var);

if (py[j] $>$ pmax) pmax=py[jmax=j]; } expy exp(-pmax); Estimate significance of largest peak value. effm $^ { 1 = 2 }$ .0\*nout/ofac; prob $=$ effm\*expy; if (prob $>$ 0.01) prob $^ { 1 = 1 }$ .0-pow(1.0-expy,effm);

void spread(const Doub y, VecDoub_IO &yy, const Doub x, const Int m) { Given an array yy[0..n-1], extirpolate (spread) a value y into m actual array elements that best approximate the “fictional” (i.e., possibly noninteger) array element number x. The weights used are coefficients of the Lagrange interpolating polynomial.

static Int nfac[11] $= \{ 0$ ,1,1,2,6,24,120,720,5040,40320,362880 Int ihi,ilo,ix,j,nden,n=yy.size(); Doub fac; if ( $\mathrm { ~ m ~ } > \ 1 0$ ) throw("factorial table too small in spread"); ix=Int(x); if ( $\mathbf { \nabla } \cdot \mathbf { x } \ = =$ Doub(ix)) yy[ix-1] += y; else { ilo $\ c =$ MIN(MAX(Int(x-0.5\*m),0),Int(n-m)); ihi $=$ ilo+m; nden=nfac[m]; fac=x-ilo-1; for (j=ilo+1;j<ihi; ${ \dot { \bf { J } } } ^ { + + }$ ) fac \*= (x-j-1); yy[ihi-1] $+ =$ y\*fac/(nden\*(x-ihi)); for (j $=$ ihi-1;j>ilo;j--) { nden $\cdot ^ { = }$ (nden/(j-ilo))\*(j-ihi); yy[j-1] $+ =$ y\*fac/(nden\*(x-j)); } } }

# CITED REFERENCES AND FURTHER READING:

Lomb, N.R. 1976, “Least-Squares Frequency Analysis of Unequally Spaced Data,” Astrophysics and Space Science,vol.39,pp.447-462.[1]   
Barning, F.J.M. 1963, “The Numerical Analysis of the Light-Curve of 12 Lacertae,” Bulletin of the Astronomical Institutes of the Netherlands,vol.17,pp.22-28.[2]   
Vanícek, P. 1971, “Further Development and Properties of the Spectral Analysis by Least Squares,” ˇ Astrophysics and Space Science, vol.12, pp.10-33.[3]   
Scargle, J.D. 1982, “Studies in Astronomical Time Series Analysis II. Statistical Aspects of Spectral Analysis of Unevenly Sampled Data,” Astrophysical Journal, vol. 263, pp. 835–853.[4]   
Horne, J.H., and Baliunas, S.L. 1986, “A Prescription for Period Analysis of Unevenly Sampled Time Series,” Astrophysical Journal, vol. 302, pp. 757–763.[5]   
Press, W.H. and Rybicki, G.B. 1989, “Fast Algorithm for Spectral Analysis of Unevenly Sampled Data,” Astrophysical Journal, vol. 338, pp. 277–280.[6]

# 13.9 Computing Fourier Integrals Using the FFT

Not uncommonly, one wants to calculate accurate numerical values for integrals of the form

$$
I = \int _ { a } ^ { b } e ^ { i \omega t } h ( t ) d t \ ,
$$

or the equivalent real and imaginary parts

$$
I _ { c } = \int _ { a } ^ { b } \cos ( \omega t ) h ( t ) d t \qquad I _ { s } = \int _ { a } ^ { b } \sin ( \omega t ) h ( t ) d t \ ,
$$

and one wants to evaluate this integral for many different values of $\omega$ . In cases of interest, $h ( t )$ is often a smooth function, but it is not necessarily periodic in $[ a , b ]$ , nor does it necessarily go to zero at $a$ or $b$ . While it seems intuitively obvious that the force majeure of the FFT ought to be applicable to this problem, doing so turns out to be a surprisingly subtle matter, as we will now see.

Let us first approach the problem naively, to see where the difficulty lies. Divide the interval $[ a , b ]$ into $M$ subintervals, where $M$ is a large integer, and define

$$
\Delta \equiv \frac { b - a } { M } , \quad t _ { j } \equiv a + j \Delta , \quad h _ { j } \equiv h ( t _ { j } ) , \quad j = 0 , \ldots , M
$$

Notice that $h _ { 0 } ~ = ~ h ( a )$ and $h _ { M } \ = \ h ( b )$ , and that there are $M + 1$ values $h _ { j }$ . We can approximate the integral $I$ by a sum,

$$
I \approx \Delta \sum _ { j = 0 } ^ { M - 1 } h _ { j } \exp ( i \omega t _ { j } )
$$

which is at any rate first-order accurate. (If we centered the $h _ { j }$ ’s and the $t _ { j }$ ’s in the intervals, we could be accurate to second order.) Now, for certain values of $\omega$ and $M$ , the sum in equation (13.9.4) can be made into a discrete Fourier transform, or DFT, and evaluated by the fast Fourier transform (FFT) algorithm. In particular, we can choose $M$ to be an integer power of 2 and define a set of special $\omega$ ’s by

$$
\omega _ { m } \Delta \equiv \frac { 2 \pi m } { M }
$$

where $m$ has the values $m = 0 , 1 , \ldots , M / 2 - 1$ . Then equation (13.9.4) becomes

$$
I ( \omega _ { m } ) \approx \Delta e ^ { i \omega _ { m } a } \sum _ { j = 0 } ^ { M - 1 } h _ { j } e ^ { 2 \pi i m j / M } = \Delta e ^ { i \omega _ { m } a } [ \mathrm { D F T } ( h _ { 0 } \dots h _ { M - 1 } ) ] _ { m }
$$

Equation (13.9.6), while simple and clear, is emphatically not recommended for use: It is likely to give wrong answers!

The problem lies in the oscillatory nature of the integral (13.9.1). If $h ( t )$ is at all smooth, and if $\omega$ is large enough to imply several cycles in the interval $[ a , b ]$ — in fact, $\omega _ { m }$ in equation (13.9.5) gives exactly $m$ cycles — then the value of $I$ is typically very small, so small that it is easily swamped by first-order, or even (with centered values) second-order, truncation error. Furthermore, the characteristic “small parameter” that occurs in the error term is not $\Delta / ( b - a ) = 1 / M$ , as it would be if the integrand were not oscillatory, but $\omega \Delta$ , which can be as large as $\pi$ for $\omega$ ’s within the Nyquist interval of the DFT (cf. equation 13.9.5). The result is that equation (13.9.6) becomes systematically inaccurate as $\omega$ increases.

It is a sobering exercise to implement equation (13.9.6) for an integral that can be done analytically and to see just how bad it is. We recommend that you try it.

Let us therefore turn to a more sophisticated treatment. Given the sampled points $h _ { j }$ , we can approximate the function $h ( t )$ everywhere in the interval $[ a , b ]$ by interpolation on nearby $h _ { j }$ ’s. The simplest case is linear interpolation, using the two nearest $h _ { j }$ ’s, one to the left and one to the right. A higher-order interpolation, e.g., would be cubic interpolation, using two points to the left and two to the right — except in the first and last subintervals, where we must interpolate with three $h _ { j }$ ’s on one side, one on the other.

The formulas for such interpolation schemes are (piecewise) polynomial in the independent variable $t$ , but with coefficients that are of course linear in the function values $h _ { j }$

Although one does not usually think of it in this way, interpolation can be viewed as approximating a function by a sum of kernel functions (which depend only on the interpolation scheme) times sample values (which depend only on the function). Let us write

$$
h ( t ) \approx \sum _ { j = 0 } ^ { M } h _ { j } ~ \psi \left( \frac { t - t _ { j } } { \Delta } \right) + \sum _ { j = \mathrm { e n d p o i n t s } } h _ { j } ~ \varphi _ { j } \left( \frac { t - t _ { j } } { \Delta } \right)
$$

Here $\psi ( s )$ is the kernel function of an interior point: It is zero for $s$ sufficiently negative or sufficiently positive and becomes nonzero only when $s$ is in the range where the $h _ { j }$ multiplying it is actually used in the interpolation. We always have $\psi ( 0 ) = 1$ and $\psi ( m ) = 0$ ; $m =$ $\pm 1 , \pm 2 , . . .$ ; since interpolation right on a sample point should give the sampled function value. For linear interpolation, $\psi ( s )$ is piecewise linear, rises from 0 to 1 for $s$ in $( - 1 , 0 )$ , and falls back to 0 for $s$ in $( 0 , 1 )$ . For higher-order interpolation, $\psi ( s )$ is made up piecewise of segments of Lagrange interpolation polynomials. It has discontinuous derivatives at integer values of $s$ , where the pieces join, because the set of points used in the interpolation changes discretely.

As already remarked, the subintervals closest to $a$ and $b$ require different (noncentered) interpolation formulas. This is reflected in equation (13.9.7) by the second sum, with the special endpoint kernels $\varphi _ { j } ( s )$ . Actually, for reasons that will become clearer below, we have included all the points in the first sum (with kernel $\psi$ ), so the $\varphi _ { j }$ ’s are actually differences between true endpoint kernels and the interior kernel $\psi$ . It is a tedious, but straightforward, exercise to write down all the $\varphi _ { j } ( s )$ ’s for any particular order of interpolation, each one consisting of differences of Lagrange interpolating polynomials spliced together piecewise.

Now apply the integral operator $\begin{array} { r } { \int _ { a } ^ { b } d t \exp ( i \omega t ) } \end{array}$ to both sides of equation (13.9.7), interchange the sums and integral, and make the changes of variable $s = ( t - t _ { j } ) / \Delta$ in the first sum and $s = ( t - a ) / \Delta$ in the second sum. The result is

$$
I \approx \Delta e ^ { i \omega a } \Biggl [ W ( \theta ) \sum _ { j = 0 } ^ { M } h _ { j } e ^ { i j \theta } + \sum _ { j = \mathrm { e n d p o i n t s } } h _ { j } \alpha _ { j } \left( \theta \right) \Biggr ]
$$

Here $\theta \equiv \omega \Delta$ , and the functions $W ( \theta )$ and $\alpha _ { j } ( \theta )$ are defined by

$$
\begin{array} { l } { { \displaystyle { \cal W } ( \theta ) \equiv \int _ { - \infty } ^ { \infty } d s e ^ { i \theta s } \psi ( s ) } } \\ { { \displaystyle \alpha _ { j } ( \theta ) \equiv \int _ { - \infty } ^ { \infty } d s e ^ { i \theta s } \varphi _ { j } ( s - j ) } } \end{array}
$$

The key point is that equations (13.9.9) and (13.9.10) can be evaluated, analytically, once and for all, for any given interpolation scheme. Then equation (13.9.8) is an algorithm for applying “endpoint corrections” to a sum that (as we will see) can be done using the FFT, giving a result with high-order accuracy.

We will consider only interpolations that are left-right symmetric. Then symmetry implies

$$
\varphi _ { M - j } \left( s \right) = \varphi _ { j } \left( - s \right) \qquad \alpha _ { M - j } \left( \theta \right) = e ^ { i \theta M } \alpha _ { j } ^ { * } \left( \theta \right) = e ^ { i \omega \left( b - a \right) } \alpha _ { j } ^ { * } \left( \theta \right)
$$

where $^ *$ denotes complex conjugation. Also, $\psi ( s ) = \psi ( - s )$ implies that $W ( \theta )$ is real.

Turn now to the first sum in equation (13.9.8), which we want to do by FFT methods. To do so, choose some $N$ that is an integer power of 2 with $N \geq M + 1$ . (Note that $M$ need not be a power of 2, so $M = N - 1$ is allowed.) If $N > M + 1$ , define $h _ { j } \equiv 0$ ; $M + 1 < j \leq N - 1$ , i.e., “zero-pad” the array of $h _ { j }$ ’s so that $j$ takes on the range $0 \le j \le N - 1$ . Then the sum can be done as a DFT for the special values $\omega = \omega _ { n }$ given by

$$
\omega _ { n } \Delta \equiv \frac { 2 \pi n } { N } \equiv \theta \qquad n = 0 , 1 , \ldots , \frac { N } { 2 } - 1
$$

For fixed $M$ , the larger $N$ is chosen, the finer the sampling in frequency space. The value $M$ , on the other hand, determines the highest frequency sampled, since $\Delta$ decreases with increasing $M$ (equation 13.9.3), and the largest value of $\omega \Delta$ is always just under $\pi$ (equation 13.9.12). In general it is advantageous to oversample by at least a factor of 4, i.e., $N > 4 M$ (see below). We can now rewrite equation (13.9.8) in its final form as

$$
\begin{array} { r l } & { I ( \omega _ { n } ) = \Delta e ^ { i \omega _ { n } a } \Big \{ W ( \theta ) [ \mathrm { D F T } ( h _ { 0 } \dots h _ { N - 1 } ) ] _ { n } } \\ & { \qquad + \alpha _ { 0 } ( \theta ) h _ { 0 } + \alpha _ { 1 } ( \theta ) h _ { 1 } + \alpha _ { 2 } ( \theta ) h _ { 2 } + \alpha _ { 3 } ( \theta ) h _ { 3 } + \dots } \\ & { \qquad + e ^ { i \omega ( b - a ) } \left[ \alpha _ { 0 } ^ { * } ( \theta ) h _ { M } + \alpha _ { 1 } ^ { * } ( \theta ) h _ { M - 1 } + \alpha _ { 2 } ^ { * } ( \theta ) h _ { M - 2 } + \alpha _ { 3 } ^ { * } ( \theta ) h _ { M - 3 } + \dots \right] \Big \} } \end{array}
$$

For cubic (or lower) polynomial interpolation, at most the terms explicitly shown above are nonzero; the ellipses $( \ldots )$ can therefore be ignored, and we need explicit forms only for the functions $W , \alpha _ { 0 } , \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 }$ , calculated with equations (13.9.9) and (13.9.10). We have worked these out for you, in the trapezoidal (second-order) and cubic (fourth-order) cases. Here are the results, along with the first few terms of their power series expansions for small $\theta$ :

# Trapezoidal order:

$$
\begin{array} { l } { { W ( \theta ) = \displaystyle \frac { 2 ( 1 - \cos \theta ) } { \theta ^ { 2 } } \approx 1 - \frac { 1 } { 1 2 } \theta ^ { 2 } + \frac { 1 } { 3 6 0 } \theta ^ { 4 } - \frac { 1 } { 2 0 1 6 0 } \theta ^ { 6 } } } \\ { { \displaystyle \alpha _ { 0 } ( \theta ) = - \frac { ( 1 - \cos \theta ) } { \theta ^ { 2 } } + i \frac { ( \theta - \sin \theta ) } { \theta ^ { 2 } } } } \\ { { \displaystyle ~ \approx - \frac { 1 } { 2 } + \frac { 1 } { 2 4 } \theta ^ { 2 } - \frac { 1 } { 7 2 0 } \theta ^ { 4 } + \frac { 1 } { 4 0 3 2 0 } \theta ^ { 6 } + i \theta \left( \frac { 1 } { 6 } - \frac { 1 } { 1 2 0 } \theta ^ { 2 } + \frac { 1 } { 5 0 4 0 } \theta ^ { 4 } - \frac { 1 } { 3 6 2 8 8 0 } \theta ^ { 6 } \right) } } \end{array}
$$

$$
\alpha _ { 1 } = \alpha _ { 2 } = \alpha _ { 3 } = 0
$$

Cubic order:

$$
\begin{array} { l } { { W ( \theta ) = \left( \frac { 6 + \theta ^ { 2 } } { 3 \theta ^ { 4 } } \right) \left( 3 - 4 \cos \theta + \cos 2 \theta \right) \approx 1 - \frac { 1 1 } { 7 2 0 } \theta ^ { 4 } + \frac { 2 3 } { 1 5 1 2 0 } \theta ^ { 6 } } } \\ { { \nonumber } } \\ { { \alpha _ { 0 } ( \theta ) = \frac { \left( - 4 2 + 5 \theta ^ { 2 } \right) + \left( 6 + \theta ^ { 2 } \right) \left( 8 \cos \theta - \cos 2 \theta \right) } { 6 \theta ^ { 4 } } + i \frac { \left( - 1 2 \theta + 6 \theta ^ { 3 } \right) + \left( 6 + \theta ^ { 2 } \right) \sin 2 \theta } { 6 \theta ^ { 4 } } } } \\ { { \approx - \frac { 2 } { 3 } + \frac { 1 } { 4 5 } \theta ^ { 2 } + \frac { 1 0 3 } { 1 5 1 2 0 } \theta ^ { 4 } - \frac { 1 6 9 } { 2 2 6 8 0 0 } \theta ^ { 6 } + i \theta \left( \frac { 2 } { 4 5 } + \frac { 2 } { 1 0 5 } \theta ^ { 2 } - \frac { 8 } { 2 8 3 5 } \theta ^ { 4 } + \frac { 8 6 } { 4 6 7 7 7 5 } \theta ^ { 6 } \right) } } \end{array}
$$

$$
\begin{array} { r l } & { \alpha _ { 1 } ( \theta ) = \frac { 1 4 ( 3 - \theta ^ { 2 } ) - 7 ( 6 + \theta ^ { 2 } ) \cos \theta } { 6 \theta ^ { 4 } } + i \frac { 3 0 \theta - 5 ( 6 + \theta ^ { 2 } ) \sin \theta } { 6 \theta ^ { 4 } } } \\ & { \qquad \approx \frac { 7 } { 2 4 } - \frac { 7 } { 1 8 0 } \theta ^ { 2 } + \frac { 5 } { 3 4 5 6 } \theta ^ { 4 } - \frac { 7 } { 2 5 9 2 0 0 } \theta ^ { 6 } + i \theta \left( \frac { 7 } { 7 2 } - \frac { 1 } { 1 6 8 } \theta ^ { 2 } + \frac { 1 1 } { 7 2 5 7 6 } \theta ^ { 4 } - \frac { 1 3 } { 5 9 8 7 5 2 0 } \theta ^ { 6 } \right) } \end{array}
$$

$$
\begin{array} { c }  { \alpha _ { 2 } ( \theta ) = \displaystyle { \frac { - 4 ( 3 - \theta ^ { 2 } ) + 2 ( 6 + \theta ^ { 2 } ) \cos \theta } { 3 \theta ^ { 4 } } + i \frac { - 1 2 \theta + 2 ( 6 + \theta ^ { 2 } ) \sin \theta } { 3 \theta ^ { 4 } } } } \\  { \approx - \displaystyle { \frac { 1 } { 6 } + \frac { 1 } { 4 5 } \theta ^ { 2 } - \frac { 5 } { 6 0 4 8 } \theta ^ { 4 } + \frac { 1 } { 6 4 8 0 0 } \theta ^ { 6 } + i \theta \left( - \frac { 7 } { 9 0 } + \frac { 1 } { 2 1 0 } \theta ^ { 2 } - \frac { 1 1 } { 9 0 7 2 0 } \theta ^ { 4 } + \frac { 1 3 } { 7 4 8 4 4 0 0 } \theta ^ { 6 } \right) } } \\ { { \approx } } \end{array}
$$

The program dftcor, below, implements the endpoint corrections for the cubic case. Given input values of $\omega$ $\upsilon , \Delta , a , b$ ; and an array with the eight values $h _ { 0 } , \hdots , h _ { 3 } , h _ { M - 3 } , \hdots , h _ { M }$ it returns the real and imaginary parts of the endpoint corrections in equation (13.9.13), and the factor $W ( \theta )$ . The code is turgid, but only because the formulas above are complicated. The formulas have cancellations to high powers of $\theta$ . It is therefore necessary to compute the right-hand sides in double precision, even when the corrections are desired only to single precision. It is also necessary to use the series expansion for small values of $\theta$ . The optimal cross-over value of $\theta$ depends on your machine’s wordlength, but you can always find it experimentally as the largest value where the two methods give identical results to machine precision.

void dftcor(const Doub w, const Doub delta, const Doub a, const Doub b, VecDoub_I &endpts, Doub &corre, Doub &corim, Doub &corfac) {

For an integral approximated by a discrete Fourier transform, this routine computes the correction factor that multiplies the DFT and the endpoint correction to be added. Input is the angular frequency w, stepsize delta, lower and upper limits of the integral a and b, while the array endpts contains the first 4 and last 4 function values. The correction factor $W ( \theta )$ is returned as corfac, while the real and imaginary parts of the endpoint correction are returned as corre and corim.

Doub a0i,a0r,a1i,a1r,a2i,a2r,a3i,a3r,arg,c,cl,cr,s,sl,sr,t,t2,t4,t6, cth,ctth,spth2,sth,sth4i,stth,th,th2,th4,tmth2,tth4i;   
th=w\*delta;   
if ( $a > =$ b || th $<$ 0.0e0 || th $>$ 3.1416e0) throw("bad arguments to dftcor");   
if (abs(th) $<$ 5.0e-2) { Use series. $\mathtt { t = }$ th; $\scriptstyle \pm 2 =$ t\*t; t4=t2\*t2; t6=t4\*t2; corfac $^ { = 1 }$ .0-(11.0/720.0)\*t4+(23.0/15120.0)\*t6; a0r=(-2.0/3.0)+t2/45. $^ { 0 + }$ (103.0/15120.0)\*t4-(169.0/226800.0)\*t6; a1r $^ { \ast = }$ (7.0/24.0)-(7.0/180.0)\*t2+(5.0/3456.0)\*t4-(7.0/259200.0)\*t6; a2r=(-1.0/6.0)+t2/45.0-(5.0/6048.0)\*t4+t6/64800.0; a3r $^ { \ast = }$ (1.0/24.0)-t2/180. $0 +$ (5.0/24192.0)\*t4-t6/259200.0; a0i=t\*(2.0/45. $^ { 0 + }$ (2.0/105.0)\*t2-(8.0/2835.0)\*t4+(86.0/467775.0)\*t6); a1i=t\*(7.0/72.0-t2/168. $0 +$ (11.0/72576.0)\*t4-(13.0/5987520.0)\*t6); a2i=t\*(-7.0/90.0+t2/210.0-(11.0/90720.0)\*t4+(13.0/7484400.0)\*t6); a3i=t\*(7.0/360.0-t2/840. $^ { 0 + }$ (11.0/362880.0)\*t4-(13.0/29937600.0)\*t6);   
} else { Use trigonometric formulas. cth $\cdot ^ { = }$ cos(th); sth=sin(th); ctth=cth\*cth-sth\*sth; stth $^ { = 2 }$ .0e0\*sth\*cth; th2 $=$ th\*th; th4 th2\*th2; tmth2 $^ { \circ 3 }$ .0e0-th2; spth2 ${ = } 6$ .0e0+th2; sth4i $^ { = 1 }$ .0/(6.0e0\*th4); tth4i $^ { = 2 }$ .0e0\*sth4i; corfac=tth4i\*spth2\*(3.0e0-4.0e0\*cth+ctth); a0r=sth4i\*(-42.0e0+5.0e0\*th2+spth2\*(8.0e0\*cth-ctth)); a0i=sth4i\*(th\*(-12.0e0+6.0e0\*th2)+spth2\*stth); a1r=sth4i\*(14.0e0\*tmth2-7.0e0\*spth2\*cth); a1i=sth4i\*(30.0e0\*th-5.0e0\*spth2\*sth); a2r=tth4i\*(-4.0e0\*tmth2+2.0e0\*spth2\*cth); a2i ${ . } =$ tth4i\*(-12.0e0\*th+2.0e0\*spth2\*sth); a3r $^ { * = }$ sth4i\*(2.0e0\*tmth2-spth2\*cth); a3i=sth4i\*(6.0e0\*th-spth2\*sth);   
}   
cl=a0r\*endpts[0] $^ +$ a1r\*endpts[1]+a2r\*endpts[2]+a3r\*endpts[3];   
sl=a0i\*endpts[0] $^ +$ a1i\*endpts[1]+a2i\*endpts[2]+a3i\*endpts[3];   
cr $=$ a0r\*endpts[7]+a1r\*endpts[6]+a2r\*endpts[5]+a3r\*endpts[4];   
sr $\underline { { \underline { { \cdot } } } } =$ -a0i\*endpts[7]-a1i\*endpts[6]-a2i\*endpts[5]-a3i\*endpts[4]; arg=w\*(b-a);   
c=cos(arg);   
s=sin(arg);   
corre=cl+c\*cr-s\*sr;   
corim=sl+s\*cr+c\*sr;

Since the use of dftcor can be confusing, we also give an illustrative program dftint that uses dftcor to compute equation (13.9.1) for general $a , b , \omega$ , and $h ( t )$ . Several points within this program bear mentioning: The constants $\mathbb { M }$ and NDFT correspond to $M$ and $N$ in the above discussion. On successive calls, we recompute the Fourier transform only if $a$ or $b$ or $h ( t )$ has changed.

Since dftint is designed to work for any value of $\omega$ satisfying $\omega \Delta < \pi$ , not just the special values returned by the DFT (equation 13.9.12), we do polynomial interpolation of degree MPOL on the DFT spectrum. You should be warned that a large factor of oversampling $N \gg M$ ) is required for this interpolation to be accurate. After interpolation, we add the endpoint corrections from dftcor, which can be evaluated for any $\omega$ .

While dftcor is good at what it does, the routine dftint is illustrative only. It is not a general-purpose program, because it does not adapt its parameters M, NDFT, MPOL or its interpolation scheme to any particular function $h ( t )$ . You will have to experiment with your own application.

void dftint(Doub func(const Doub), const Doub a, const Doub b, const Doub w, Doub &cosint, Doub &sinint) {

Example program illustrating how to use the routine dftcor. The user supplies an external function func that returns the quantity $h ( t )$ . The routine then returns $\textstyle \int _ { a } ^ { b } \cos ( \omega t ) h ( t ) d t$ as cosint and $\textstyle \int _ { a } ^ { b } \sin ( \omega t ) h ( t ) d t$ as sinint.

static Int init ${ = } 0$ ;   
static Doub (\*funcold)(const Doub);   
static Doub aold $\ c = - 1$ .e30,bold $\qquad = \quad - 1$ .e30,delta;   
const Int M=64,NDFT $\ddots$ 1024,MPOL=6;   
The values of M, NDFT, and MPOL are merely illustrative and should be optimized for your   
particular application. M is the number of subintervals, NDFT is the length of the FFT (a   
power of 2), and MPOL is the degree of polynomial interpolation used to obtain the desired   
frequency from the FFT.   
const Doub TWOP $\mathtt { I } { = } 6$ .283185307179586476;   
Int j,nn;   
Doub c,cdft,corfac,corim,corre,en,s,sdft;   
static VecDoub data(NDFT),endpts(8);   
VecDoub cpol(MPOL),spol(MPOL),xpol(MPOL);   
if (init $\downarrow = ~ 1$ $| \texttt { | a } : =$ aold || b $\ ! =$ bold || func $! =$ funcold) { Do we need to initialize, or is only $\omega$ changed? init ${ = } 1$ ; aold=a; bold=b; funcold=func; delta (b-a)/M; for ( $\scriptstyle \mathbf { j } = 0$ ;j<M+1;j++) Load the function values into the data data[j] $=$ func(a+j\*delta); array. for (j=M+1;j<NDFT;j++) Zero-pad the rest of the data array. data[j]=0.0; for (j ${ = } 0$ ;j<4;j++) { Load the endpoints. endpts[j] $=$ data[j]; endpts[j+4] $=$ data[M-3+j]; } realft(data,1); realft returns the unused value corresponding to $\omega _ { N / 2 }$ in data[1]. We actually want this element to contain the imaginary part corresponding to $\omega _ { 0 }$ , which is zero. data[1] ${ = } 0$ .0;   
}   
Now interpolate on the DFT result for the desired frequency. If the frequency is an $\omega _ { n }$ ,

i.e., the quantity en is an integer, then cdft $=$ data[2\*en-2], sdft ${ } = { }$ data[2\*en-1], and you could omit the interpolation.

en $\equiv$ w\*delta\*NDFT/TWOPI+1.0;   
nn $\ c =$ MIN(MAX(Int(en-0.5\*MPOL+1.0),1),NDFT/2-MPOL+1); Leftmost point for the for $\scriptstyle \dot { \ j } = 0$ ;j<MPOL;j++,nn++) { interpolation. cpol[j] $=$ data[2\*nn-2];   
spol[j] $=$ data[2\*nn-1];   
xpol[j]=nn;   
}   
cdft $=$ Poly_interp(xpol,cpol,MPOL).interp(en);   
sdft $=$ Poly_interp(xpol,spol,MPOL).interp(en);   
dftcor(w,delta,a,b,endpts,corre,corim,corfac); Now get the endpoint corcdft $\ast =$ corfac; rection and the mulsdft $\ast =$ corfac; tiplicative factor $W ( \theta )$ . cdft $+ =$ corre;   
sdft $+ =$ corim;   
$\mathtt { c } =$ delta\*cos(w\*a); Finally multiply by $\Delta$ and $\exp ( i \omega a )$ . s=delta\*sin(w\*a);   
cosint=c\*cdft-s\*sdft;   
sinint=s\*cdft+c\*sdft;

# }

Sometimes one is interested only in the discrete frequencies $\omega _ { m }$ of equation (13.9.5), the ones that have integral numbers of periods in the interval $[ a , b ]$ . For smooth $h ( t )$ , the value of $I$ tends to be much smaller in magnitude at these $\omega$ ’s than at values in between, since the integral half-periods tend to cancel precisely. (That is why one must oversample for interpolation to be accurate: $I ( \omega )$ is oscillatory with small magnitude near the $\omega _ { m }$ ’s.) If you want these $\omega _ { m }$ ’s without messy (and possibly inaccurate) interpolation, you have to set $N$ to a multiple of $M$ (compare equations 13.9.5 and 13.9.12). In the method implemented above, however, $N$ must be at least $M + 1$ , so the smallest such multiple is $2 M$ , resulting in a factor ${ \sim } 2$ unnecessary computing. Alternatively, one can derive a formula like equation (13.9.13), but with the last function sample $h _ { M } = h ( b )$ omitted from the DFT, but included entirely in the endpoint correction for $h _ { M }$ . Then one can set $M = N$ (an integer power of 2) and get the special frequencies of equation (13.9.5) with no additional overhead. The modified formula is

$$
\begin{array} { l } { { I ( \omega _ { m } ) = \Delta e ^ { i \omega _ { m } a } \Big \{ W ( \theta ) [ \mathrm { D F T } ( h _ { 0 } \dots h _ { M - 1 } ) ] _ { m } } } \\ { { \qquad + \alpha _ { 0 } ( \theta ) h _ { 0 } + \alpha _ { 1 } ( \theta ) h _ { 1 } + \alpha _ { 2 } ( \theta ) h _ { 2 } + \alpha _ { 3 } ( \theta ) h _ { 3 } } } \\ { { \qquad + e ^ { i \omega ( b - a ) } \left[ A ( \theta ) h _ { M } + \alpha _ { 1 } ^ { * } ( \theta ) h _ { M - 1 } + \alpha _ { 2 } ^ { * } ( \theta ) h _ { M - 2 } + \alpha _ { 3 } ^ { * } ( \theta ) h _ { M - 3 } \right] \Big \} } } \end{array}
$$

where $\theta \equiv \omega _ { m } \Delta$ and $A ( \theta )$ is given by

$$
A ( \theta ) = - \alpha _ { 0 } ( \theta )
$$

for the trapezoidal case, or

$$
\begin{array} { r } { A ( \theta ) = \frac { ( - 6 + 1 1 \theta ^ { 2 } ) + ( 6 + \theta ^ { 2 } ) \cos 2 \theta } { 6 \theta ^ { 4 } } - i \ \mathrm { I m } [ \alpha _ { 0 } ( \theta ) ] } \\ { \approx \frac { 1 } { 3 } + \frac { 1 } { 4 5 } \theta ^ { 2 } - \frac { 8 } { 9 4 5 } \theta ^ { 4 } + \frac { 1 1 } { 1 4 1 7 5 } \theta ^ { 6 } - i \ \mathrm { I m } [ \alpha _ { 0 } ( \theta ) ] } \end{array}
$$

for the cubic case.

Factors like $W ( \theta )$ arise naturally whenever one calculates Fourier coefficients of smooth functions, and they are sometimes called attenuation factors [1]. However, the endpoint corrections are equally important in obtaining accurate values of integrals. Narasimhan and Karthikeyan [2] have given a formula that is algebraically equivalent to our trapezoidal formula. However, their formula requires the evaluation of two FFTs, which is unnecessary. The basic idea used here goes back at least to Filon [3] in 1928 (before the FFT!). He used Simpson’s rule (quadratic interpolation). Since this interpolation is not left-right symmetric, two Fourier transforms are required. An alternative algorithm for equation (13.9.14) has been given by Lyness in [4]; for related references, see [5]. To our knowledge, the cubic-order formulas derived here have not previously appeared in the literature.

Calculating Fourier transforms when the range of integration is $( - \infty , \infty )$ can be tricky. If the function falls off reasonably quickly at infinity, you can split the integral at a large enough value of $t$ . For example, the integration to $+ \infty$ can be written

$$
\begin{array} { l } { \displaystyle \int _ { a } ^ { \infty } e ^ { i \omega t } h ( t ) d t = \int _ { a } ^ { b } e ^ { i \omega t } h ( t ) d t + \int _ { b } ^ { \infty } e ^ { i \omega t } h ( t ) d t } \\ { = \displaystyle \int _ { a } ^ { b } e ^ { i \omega t } h ( t ) d t - \frac { h ( b ) e ^ { i \omega b } } { i \omega } + \frac { h ^ { \prime } ( b ) e ^ { i \omega b } } { ( i \omega ) ^ { 2 } } - \cdots } \end{array}
$$

The splitting point $b$ must be chosen large enough that the remaining integral over $( b , \infty )$ is small. Successive terms in its asymptotic expansion are found by integrating by parts. The integral over $( a , b )$ can be done using dftint. You keep as many terms in the asymptotic expansion as you can easily compute. See [6] for some examples of this idea. More powerful methods, which work well for long-tailed functions but which do not use the FFT, are described in [7-9].

# CITED REFERENCES AND FURTHER READING:

Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), -2.3.4.[1]   
Narasimhan, M.S. and Karthikeyan, M. 1984, “Evaluation of Fourier Integrals Using a FFT with Improved Accuracy and Its Applications,” IEEE Transactions on Antennas and Propagation, vol. 32, pp. 404–408.[2]   
Filon, L.N.G. 1928, “On a Quadrature Formula for Trigonometric Integrals,” Proceedings of the Royal Society of Edinburgh,vol.49,pp.38-47.[3]   
Giunta, G. and Murli, A. 1987, “A Package for Computing Trigonometric Fourier Coefficients Based on Lyness’s Algorithm,” ACM Transactions on Mathematical Software, vol. 13, pp. 97– 107.[4]   
Lyness, J.N. 1987, in Numerical Integration, P. Keast and G. Fairweather, eds. (Dordrecht: Reidel).[5]   
Pantis, G. 1975, “The Evaluation of Integrals with Oscillatory Integrands,” Journal of Computational Physics,vol.17,pp.229-233.[6]   
Blakemore, M., Evans, G.A., and Hyslop, J. 1976, “Comparison of Some Methods for Evaluating Infinite Range Oscillatory Integrals,” Journal of Computational Physics, vol. 22, pp. 352– 376.[7]   
Lyness, J.N., and Kaper, T.J. 1987, “Calculating Fourier Transforms of Long Tailed Functions,” SIAM Journal on Scientific and Statistical Computing,vol.8,pp.1005-1011.[8]   
Thakkar, A.J., and Smith, V.H. 1975, “A Strategy for the Numerical Evaluation of Fourier Sine and Cosine Transforms to Controlled Accuracy,” Computer Physics Communications, vol. 10, pp. 73–79.[9]

# 13.10 Wavelet Transforms

Like the fast Fourier transform (FFT), the discrete wavelet transform (DWT) is a fast, linear operation that operates on a data vector whose length is an integer power of 2, transforming it into a numerically different vector of the same length. Also like the FFT, the wavelet transform is invertible and in fact orthogonal — the inverse transform, when viewed as a big matrix, is simply the transpose of the transform.

Both FFT and DWT, therefore, can be viewed as a rotation in function space, from the input space (or time) domain, where the basis functions are the unit vectors $\mathbf { e } _ { i }$ , or Dirac delta functions in the continuum limit, to a different domain. For the FFT, this new domain has basis functions that are the familiar sines and cosines. In the wavelet domain, the basis functions are somewhat more complicated and have the fanciful names “mother functions” and “wavelets.”

Of course there are an infinity of possible bases for function space, almost all of them uninteresting! What makes the wavelet basis interesting is that, unlike sines and cosines, individual wavelet functions are quite localized in space; simultaneously, like sines and cosines, individual wavelet functions are quite localized in frequency or (more precisely) characteristic scale. As we will see below, the particular kind of dual localization achieved by wavelets renders large classes of functions and operators sparse, or sparse to some high accuracy, when transformed into the wavelet domain. Analogously with the Fourier domain, where a class of computations, like convolutions, becomes computationally fast, there is a large class of computations — those that can take advantage of sparsity — that becomes computationally fast in the wavelet domain [1].

Unlike sines and cosines, which define a unique Fourier transform, there is not one single unique set of wavelets; in fact, there are infinitely many possible sets. Roughly, the different sets of wavelets make different trade-offs between how compactly they are localized in space, how smooth they are, and whether they have any special boundary conditions. (There are further fine distinctions.)

# 13.10.1 Daubechies Wavelet Filter Coefficients

A particular set of wavelets is specified by a particular set of numbers, called wavelet filter coefficients. Here, we will largely restrict ourselves to wavelet filters in a class discovered by Daubechies [2]. This class includes members ranging from highly localized to highly smooth. The simplest (and most localized) member, often called DAUB4, has only four coefficients, $c _ { 0 } , \ldots , c _ { 3 }$ . For the moment we specialize to this case for ease of notation.

Consider the following transformation matrix acting on a column vector of data to its right:

$$
\left[ { \begin{array} { l l l l l l l l l } { c _ { 0 } } & { c _ { 1 } } & { c _ { 2 } } & { c _ { 3 } } & & & & & \\ { c _ { 3 } } & { - c _ { 2 } } & { c _ { 1 } } & { - c _ { 0 } } & & & & & \\ & { c _ { 0 } } & { c _ { 1 } } & { c _ { 2 } } & { c _ { 3 } } & & & & \\ & & { c _ { 3 } } & { - c _ { 2 } } & { c _ { 1 } } & { - c _ { 0 } } & & & & \\ { \vdots } & { \vdots } & & & & { \ddots } & & & & \\ & & & & & { c _ { 0 } } & { c _ { 1 } } & { c _ { 2 } } & { c _ { 3 } } \\ & & & & & & & { c _ { 3 } } & { - c _ { 2 } } & { c _ { 1 } } & { - c _ { 0 } } \\ { c _ { 2 } } & { c _ { 3 } } & & & & & & { c _ { 0 } } & { c _ { 1 } } \\ { c _ { 1 } } & { - c _ { 0 } } & & & & & & { c _ { 3 } } & { - c _ { 2 } } \end{array} } \right]
$$

Here blank entries signify zeroes. Note the structure of this matrix. The first row convolves four consecutive data points with the filter coefficients $c _ { 0 } \ldots , c _ { 3 }$ ; likewise, the third, fifth, and other odd rows. If the even rows followed this pattern, offset by one, then the matrix would be a circulant, that is, an ordinary convolution that could be done by FFT methods. (Note how the last two rows wrap around like convolutions with periodic boundary conditions.) Instead of convolving with $c _ { 0 } , \ldots , c _ { 3 }$ , however, the even rows perform a different convolution, with coefficients $c _ { 3 } , - c _ { 2 } , c _ { 1 } , - c _ { 0 }$ . The action of the matrix, overall, is thus to perform two related convolutions, then to decimate each of them by half (throw away half the values), and interleave the remaining halves.

It is useful to think of the filter $c _ { 0 } , \ldots , c _ { 3 }$ as being a smoothing filter, call it $H$ , something like a moving average of four points. Then, because of the minus signs, the filter $c _ { 3 } , - c _ { 2 } , c _ { 1 } , - c _ { 0 }$ , call it $G$ , is not a smoothing filter. (In signal processing contexts, $H$ and $G$ are called quadrature mirror filters [3].) In fact, the $c$ ’s are chosen so as to make $G$ yield, insofar as possible, a zero response to a sufficiently smooth data vector. This is done by requiring the sequence $c _ { 3 } , - c _ { 2 } , c _ { 1 } , - c _ { 0 }$ to have a certain number of vanishing moments. When this is the case for $p$ moments (starting with the zeroth), a set of wavelets is said to satisfy an “approximation condition of order $p$ .” This results in the output of $H$ , decimated by half, accurately representing the data’s “smooth” information. The output of $G$ , also decimated, is referred to as the data’s “detail” information [4].

For such a characterization to be useful, it must be possible to reconstruct the original data vector of length $N$ from its $N / 2$ smooth or s-components and its $N / 2$ detail or d-components. That is effected by requiring the matrix (13.10.1) to be orthogonal, so that its inverse is just the transposed matrix

$$
\left[ \begin{array} { l l l l l l l l l } { c _ { 0 } } & { c _ { 3 } } & & & { \cdots } & & & & { c _ { 2 } } & { c _ { 1 } } \\ { c _ { 1 } } & { - c _ { 2 } } & & & { \cdots } & & & & { c _ { 3 } } & { - c _ { 0 } } \\ { c _ { 2 } } & { c _ { 1 } } & { c _ { 0 } } & { c _ { 3 } } & & & & & \\ { c _ { 3 } } & { - c _ { 0 } } & { c _ { 1 } } & { - c _ { 2 } } & & & & & \\ & & { \ddots } & & & & & & \\ & & & { c _ { 2 } } & { c _ { 1 } } & { c _ { 0 } } & { c _ { 3 } } & & \\ & & & & { c _ { 3 } } & { - c _ { 0 } } & { c _ { 1 } } & { - c _ { 2 } } & \\ & & & & & { c _ { 2 } } & { c _ { 1 } } & { c _ { 0 } } & { c _ { 3 } } \\ & & & & & & { c _ { 3 } } & { - c _ { 0 } } & { c _ { 1 } } & { - c _ { 2 } } \end{array} \right]
$$

One sees immediately that matrix (13.10.2) is inverse to matrix (13.10.1) if and only if these two equations hold,

$$
\begin{array} { r } { c _ { 0 } ^ { 2 } + c _ { 1 } ^ { 2 } + c _ { 2 } ^ { 2 } + c _ { 3 } ^ { 2 } = 1 } \\ { c _ { 2 } c _ { 0 } + c _ { 3 } c _ { 1 } = 0 } \end{array}
$$

If additionally we require the approximation condition of order $p = 2$ , then two additional relations are required,

$$
\begin{array} { r } { c _ { 3 } - c _ { 2 } + c _ { 1 } - c _ { 0 } = 0 } \\ { 0 c _ { 3 } - 1 c _ { 2 } + 2 c _ { 1 } - 3 c _ { 0 } = 0 } \end{array}
$$

Equations (13.10.3) and (13.10.4) are four equations for the four unknowns $c _ { 0 } , \ldots , c _ { 3 }$ , first recognized and solved by Daubechies. The unique solution (up to a left-right reversal) is

$$
\begin{array} { c c c } { { c _ { 0 } = ( 1 + \sqrt { 3 } ) / 4 \sqrt { 2 } } } & { { } } & { { c _ { 1 } = ( 3 + \sqrt { 3 } ) / 4 \sqrt { 2 } } } \\ { { } } & { { } } & { { c _ { 2 } = ( 3 - \sqrt { 3 } ) / 4 \sqrt { 2 } } } & { { } } & { { c _ { 3 } = ( 1 - \sqrt { 3 } ) / 4 \sqrt { 2 } } } \end{array}
$$

In fact, DAUB4 is only the most compact of a sequence of wavelet sets: If we had six coefficients instead of four, there would be three orthogonality requirements in equation (13.10.3) (with offsets of zero, two, and four), and we could require the vanishing of $p = 3$ moments in equation (13.10.4). In this case, DAUB6, the solution coefficients can also be expressed in closed form,

$$
{ \begin{array} { l l } { c _ { 0 } = ( 1 + { \sqrt { 1 0 } } + { \sqrt { 5 + 2 { \sqrt { 1 0 } } } } ) / 1 6 { \sqrt { 2 } } } & { \quad c _ { 1 } = ( 5 + { \sqrt { 1 0 } } + 3 { \sqrt { 5 + 2 { \sqrt { 1 0 } } } } ) / 1 6 { \sqrt { 2 } } } \\ { c _ { 2 } = ( 1 0 - 2 { \sqrt { 1 0 } } + 2 { \sqrt { 5 + 2 { \sqrt { 1 0 } } } } ) / 1 6 { \sqrt { 2 } } } & { \quad c _ { 3 } = ( 1 0 - 2 { \sqrt { 1 0 } } - 2 { \sqrt { 5 + 2 { \sqrt { 1 0 } } } } ) / 1 6 { \sqrt { 2 } } } \\ { c _ { 4 } = ( 5 + { \sqrt { 1 0 } } - 3 { \sqrt { 5 + 2 { \sqrt { 1 0 } } } } ) / 1 6 { \sqrt { 2 } } } & { \quad c _ { 5 } = ( 1 + { \sqrt { 1 0 } } - { \sqrt { 5 + 2 { \sqrt { 1 0 } } } } ) / 1 6 { \sqrt { 2 } } } \end{array} }
$$

For higher $p$ , the coefficients are available only numerically, e.g., tabulated in [5] or [6]. (We use some of these below.) The number of coefficients increases by two each time $p$ is increased by one.

# 13.10.2 Discrete Wavelet Transform

We have not yet defined the discrete wavelet transform (DWT), but we are almost there: The DWT consists of applying a wavelet coefficient matrix like (13.10.1) hierarchically, first to the full data vector of length $N$ , then to the “smooth” vector of length $N / 2$ , then to the “smooth-smooth” vector of length $N / 4$ , and so on until only a trivial number of “smooth-: : :-smooth” components (usually 2 or 4) remain. The procedure is sometimes called a pyramidal algorithm [4], for obvious reasons. The output of the DWT consists of these remaining components and all the “detail” components that were accumulated along the way. A diagram should make the procedure clear:

<table><tr><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>So</td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1>s0S1</td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1>S</td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1>S</td><td rowspan=2 colspan=4></td><td rowspan=2 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1>do</td></tr><tr><td rowspan=1 colspan=1>y2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S1</td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>S</td><td rowspan=2 colspan=4>etc.</td><td rowspan=2 colspan=1>中</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>d1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S3</td><td rowspan=1 colspan=1>13.10.1</td><td rowspan=1 colspan=1>D1</td><td rowspan=1 colspan=1>permute</td></tr><tr><td rowspan=1 colspan=1>y4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S2</td><td rowspan=1 colspan=1>permute</td><td rowspan=1 colspan=1>Do</td><td rowspan=1 colspan=3></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>y5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>d2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>D2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>D1</td><td rowspan=1 colspan=4></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=3 colspan=1></td><td rowspan=3 colspan=1>13.10.1→</td><td rowspan=1 colspan=1>S3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>D2</td><td rowspan=1 colspan=3></td><td rowspan=1 colspan=2></td></tr><tr><td rowspan=1 colspan=1>d3</td><td rowspan=1 colspan=1>permute</td><td rowspan=1 colspan=1>S7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>D3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>D3</td><td rowspan=1 colspan=4></td><td rowspan=1 colspan=1>D3</td></tr><tr><td rowspan=1 colspan=1>S4</td><td rowspan=1 colspan=1>permute</td><td rowspan=1 colspan=1>do</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>do</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>do</td><td rowspan=1 colspan=4></td><td rowspan=1 colspan=1>do</td></tr><tr><td rowspan=1 colspan=1>y9</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>d4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>d1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>d1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>d1</td><td rowspan=1 colspan=4></td><td rowspan=2 colspan=1>d</td></tr><tr><td rowspan=1 colspan=1>y10</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>d2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>d2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>d2</td><td rowspan=1 colspan=4></td></tr><tr><td rowspan=4 colspan=1>y11y12y13y14y15</td><td rowspan=4 colspan=1></td><td rowspan=4 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1>d</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>d3</td><td rowspan=1 colspan=1></td><td rowspan=4 colspan=1></td><td rowspan=4 colspan=4></td><td rowspan=4 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>d4</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>d5</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>d</td><td rowspan=1 colspan=1></td></tr></table>

If the length of the data vector were a higher power of 2, there would be more stages of applying (13.10.1) (or any other wavelet coefficients) and permuting. The endpoint will always be a vector with two $\pmb { \mathscr { s } }$ ’s and a hierarchy of $\mathcal { D }$ ’s, $D$ ’s, $d$ ’s, etc. Notice that once $d$ ’s are generated, they simply propagate through to all subsequent stages.

A value $d _ { i }$ of any level is termed a “wavelet coefficient” of the original data vector; the final values $\mathcal { B } _ { 0 } , \mathcal { B } _ { 1 }$ should strictly be called “mother-function coefficients,” although the term “wavelet coefficients” is often used loosely for both $d$ ’s and final $\mathcal { S }$ ’s. Since the full procedure is a composition of orthogonal linear operations, the whole DWT is itself an orthogonal linear operator.

To invert the DWT, one simply reverses the procedure, starting with the smallest level of the hierarchy and working (in equation 13.10.7) from right to left. The inverse matrix (13.10.2) is of course used instead of the matrix (13.10.1).

As already noted, the matrices (13.10.1) and (13.10.2) embody periodic (“wraparound”) boundary conditions on the data vector. One normally accepts this as a minor inconvenience: The last few wavelet coefficients at each level of the hierarchy are affected by data from both ends of the data vector. By circularly shifting the matrix (13.10.1) $N / 2$ columns to the left, one can symmetrize the wraparound; but this does not eliminate it. It is in fact possible to eliminate the wraparound completely by altering the coefficients in the first and last few rows of (13.10.1), giving an orthogonal matrix that is purely band-diagonal. This variant can be useful when, e.g., the data vary by many orders of magnitude from one end of the data vector to the other. We discuss it in $\ S 1 3 . 1 0 . 5$ , below.

Here is a DWT routine, wt1, that performs the pyramidal algorithm (or its inverse if isign is negative) on some data vector $\mathtt { a } \left[ 0 \dots \cdot \mathbf { n } ^ { - 1 } \right]$ . Successive applications of the wavelet filter, and accompanying permutations, are performed by the object wlet, of class Wavelet, to be described below. The routine wt1 also provides for the possibility of preconditioning and postconditioning steps, which we won’t need until a later subsection.

# void wt1(VecDoub_IO &a, const Int isign, Wavelet &wlet)

One-dimensional discrete wavelet transform. This routine implements the pyramid algorithm, replacing a[0..n-1] by its wavelet transform (for isign $^ { = 1 }$ ), or performing the inverse operation (for isign $= - 1$ ). Note that n MUST be an integer power of 2. The object wlet, of type Wavelet, is the underlying wavelet filter. $\mathsf { E x }$ amples of Wavelet types are Daub4, Daubs, and Daub4i. {

Int nn, $\mathtt { n } = \mathtt { a }$ .size(); if $\mathit { \Theta } _ { \mathrm { ~ n ~ } } < \mathit { \Theta } 4 ,$ ) return; if (isign $> = \ 0 \mathrm { { . } }$ ) { Wavelet transform. wlet.condition(a,n,1); for $\scriptstyle { \mathrm { ( n n = n } ; \mathrm { n n } > = 4 ; \mathrm { n n } > > = 1 }$ ) wlet.filt(a,nn,isign); Start at largest hierarchy, and work toward smallest. } else { for $\scriptstyle \mathtt { ( n n { = } 4 ; n n { < } = 1 ; n n { < } < = 1 }$ ) wlet.filt(a,nn,isign); Start at smallest hierarchy, and work toward largest. wlet.condition $( \mathsf { a } , \mathsf { n } , - 1 )$ ; } }

The Wavelet class is an “abstract base class,” meaning that it is really only a promise that specific wavelets that derive from it will contain a method called filt, the actual wavelet filter. Wavelet also provides a default, null, pre- and postconditioning method. The class Daub4 is derived from Wavelet and is intended for use with wt1. Its filt method implements the matrices (13.10.1) and (13.10.2), along with the permutation shown in (13.10.7).

struct Wavelet { virtual void filt(VecDoub_IO &a, const Int n, const Int isign) $\mathit { \Theta } = \mathit { \Theta } 0$ ; virtual void condition(VecDoub_IO &a, const Int n, const Int isign) {}   
};   
struct Daub4 : Wavelet { void filt(VecDoub_IO &a, const Int n, const Int isign) { Applies the Daubechies 4-coefficient wavelet filter to data vector a[0..n-1] (for isign $^ { = 1 }$ ) or applies its transpose (for isign $\imath { = } { - } 1$ ). Used hierarchically by routines wt1 and wtn. const Doub $\mathtt { C O = 0 }$ .4829629131445341, $\mathtt { C 1 } = 0$ .8365163037378077, $\mathtt { C 2 = 0 }$ .2241438680420134, $\scriptstyle \mathrm { C } 3 = - 0$ .1294095225512603; Int nh,i,j; if $\smash { \left( \mathbf { n } \ < \ 4 \right) }$ ) return; VecDoub wksp(n); n $\mathrm { ~ \texttt ~ { ~ h ~ } ~ } = \mathrm { ~ \texttt ~ { ~ n ~ } ~ } > > \mathrm { ~ \texttt ~ { ~ 1 ~ } ~ }$ ; if (isign $> = \ 0 $ ) { Apply filter. for $\scriptstyle \dot { 1 } = 0$ , $\scriptstyle \left. \vert = 0 \right.$ ;j<n-3;j $+ { = } 2$ ,i++) { wksp[i] $=$ C0\*a[j]+C1\*a[j+1]+C2\*a[j+2]+C3\*a[j+3]; wksp[i+nh] $=$ C3\*a[j]-C2\*a[j+1]+C1\*a[j+2]-C0\*a[j+3]; } wksp[i] $=$ C0\*a[n-2]+C1\*a[n-1]+C2\*a[0]+C3\*a[1]; wksp[i+nh] $=$ C3\*a[n-2]-C2\*a[n-1]+C1\*a[0]-C0\*a[1]; } else { Apply transpose filter. wksp[0] $=$ C2\*a[nh-1]+C1\*a[n-1]+C0\*a[0]+C3\*a[nh]; wksp[1] $=$ C3\*a[nh-1]-C0\*a[n-1]+C1\*a[0]-C2\*a[nh]; for (i=0,j=2;i<nh-1;i++) { wksp[j++] $=$ C2\*a[i]+C1\*a[i+nh]+C0\*a[i+1]+C3\*a[i+nh+1]; wksp[j++] $=$ C3\*a[i]-C0\*a[i+nh]+C1\*a[i+1]-C2\*a[i+nh+1]; } } for (i=0;i<n;i++) a[i] $=$ wksp[i]; }   
};

For larger sets of wavelet coefficients, the wraparound of the last rows or columns is a programming inconvenience. An efficient implementation would handle the wraparounds as special cases, outside of the main loop. For now, we will content ourselves with a more general scheme involving some extra arithmetic at run-time.

The following class, Daubs, takes an integer argument $n$ in its constructor and creates a wavelet object with the filter DAUBn. Slightly better than “Hobson’s choice,” you can choose $n \ = \ 4$ ; 12; or 20. For other values of $n$ you will need to add additional coefficient tables (e.g., from [6]).

# struct Daubs : Wavelet {

Structure for initializing and using the DAUBn wavelet filter for any $_ n$ whose coefficients are provided (here $n = 4$ ; 12; 20).

Int ncof,ioff,joff;   
VecDoub cc,cr;   
static Doub c4[4],c12[12],c20[20];   
Daubs(Int n) : ncof $\mathbf { \Psi } ( \mathbf { n } )$ , cc(n), cr(n) { Int i; ioff $=$ joff $\mathbf { \Sigma } = \mathbf { \Sigma } - \left( \mathbf { n } \mathbf { \Sigma } > \mathbf { \Sigma } 1 \right)$ ; // ioff $\qquad = \ - 2 :$ ; joff $= - \mathtt { n } + \mathtt { 2 }$ ; Alternative centering. (Used by Daub4, above.) if $( \mathrm { ~ n ~ } = = \mathrm { ~ 4 ~ } )$ ) for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; $\mathbf { i } < \mathbf { n }$ ; $\mathbf { i } + +$ ) cc[i] $=$ c4[i]; else if $\mathbf { \bar { n } } \ = = \ 1 2$ ) for ( $\scriptstyle \dot { 1 } = 0$ ; i<n; $\dot { \bf 1 } + +$ ) cc[i] $=$ c12[i]; else if $\mathbf { \bar { n } } \ \mathbf { = } \ 2 0 \mathbf { \bar { . } }$ ) for ( $\scriptstyle \dot { \mathtt { 1 } } = 0$ ; i<n; $\dot { 1 } + +$ ) cc[i] $=$ c20[i]; else throw("n not yet implemented in Daubs"); Doub $\mathsf { s i g } = - 1 . 0$ ; for ( $\scriptstyle \dot { 1 } = 0$ ; i<n; $\Dot { \ b { 1 } } + +$ ) { cr[n-1-i] $=$ sig\*cc[i]; sig $=$ -sig; } } void filt(VecDoub_IO &a, const Int n, const Int isign); See below.   
};   
Doub Daubs::c4[4] $=$ {0.4829629131445341,0.8365163037378079, 0.2241438680420134,-0.1294095225512604};   
Doub Daubs::c12[12] $=$ {0.111540743350, 0.494623890398, 0.751133908021, 0.315250351709,-0.226264693965,-0.129766867567, 0.097501605587, 0.027522865530,-0.031582039318, 0.000553842201, 0.004777257511,-0.001077301085};   
Doub Daubs::c20[20] $=$ {0.026670057901, 0.188176800078, 0.527201188932, 0.688459039454, 0.281172343661,-0.249846424327, -0.195946274377, 0.127369340336, 0.093057364604, -0.071394147166,-0.029457536822, 0.033212674059, 0.003606553567,-0.010733175483, 0.001395351747, 0.001992405295,-0.000685856695,-0.000116466855, 0.000093588670,-0.000013264203};

There is some arbitrariness in how the wavelets at each hierarchical stage are centered over the data they act on. Daubs implements one popular choice, with another shown in commented code. Consult the literature if this matters to you (it rarely does).

The implementation of Daubs::filt() is straightforward:

void Daubs::filt(VecDoub_IO &a, const Int n, const Int isign) { Applies the previously initialized Daubn wavelet filter to data vector a[0..n-1] (for isign D 1) or applies its transpose (for isign $= - 1$ ). Used hierarchically by routines wt1 and wtn.

Doub ai,ai1;   
Int i,ii,j,jf,jr,k,n1,ni,nj,nh,nmod;   
if $\mathit { \Theta } _ { \mathrm { ~ n ~ } } < \mathit { \Theta } 4 _ { \mathrm { , ~ } }$ ) return;   
VecDoub wksp(n);   
nmod $=$ ncof\*n; A positive constant equal to zero mod n.   
${ \mathfrak { n } } 1 \ = \ { \mathfrak { n } } { - } 1$ ; Mask of all bits, since n a power of 2.   
$\mathrm { ~ n h ~ } = \mathrm { ~ n ~ } > > \mathrm { ~ 1 ~ }$ ;   
for $( \ j = 0$ ;j<n;j++) wksp[j] $= 0 . 0$ ;   
if (isign $> = \ 0$ ) { Apply filter. for ( $\div \dot { 1 } = 0$ , $\scriptstyle \dot { 1 } = 0$ ;i<n; $\therefore - 2$ ,ii++) ni $=$ i+1+nmod+ioff; Pointer to be incremented and wrapped around. nj $=$ i+1+nmod+joff; for $\scriptstyle \mathtt { k } = 0$ ;k<ncof;k++) { jf = n1 & (ni+k+1); We use “bitwise and” to wrap around the jr $=$ n1 & (nj+k+1); pointers. wksp[ii] $+ =$ cc[k]\*a[jf]; wksp[ii+nh] $+ =$ cr[k]\*a[jr]; } }   
} else { Apply transpose filter. for ( $\mathtt { i } \mathtt { i } = 0$ , $\mathtt { i } = 0$ ;i<n; $\therefore - 2$ ,ii $^ { + + }$ ) { ai $=$ a[ii]; ai1 $=$ a[ii+nh]; ni $=$ i+1+nmod+ioff; See comments above. nj $=$ i+1+nmod+joff; for $\scriptstyle \mathtt { k } = 0$ ;k<ncof;k++) { jf $=$ n1 & (ni+k+1); jr $=$ n1 & (nj $+ \mathtt { k } { + } \mathtt { 1 } )$ ; wksp[jf] $+ =$ cc[k]\*ai; wksp[jr] $+ =$ cr[k]\*ai1; }

![](images/37a8f6be6aa31018788f046b5d1cbffb19a1284644c0acd8f02906deb4de1185.jpg)  
Figure 13.10.1. Wavelet functions, that is, single basis functions from the wavelet families DAUB4 and DAUB20. A complete, orthonormal wavelet basis consists of scalings and translations of either one of these functions. DAUB4 has an infinite number of cusps; DAUB20 would show similar behavior in a higher derivative.

} for (j=0;j<n;j++) a[j] $=$ wksp[j]; Copy the results back from workspace. }

# 13.10.3 What Do Wavelets Look Like?

We are now in a position to actually see some wavelets. To do so, we simply run unit vectors through any of the above discrete wavelet transforms, with isign negative so that the inverse transform is performed. Figure 13.10.1 shows the DAUB4 wavelet that is the inverse DWT of a unit vector in component 4 of a vector of length 1024, and also the DAUB20 wavelet that is the inverse of component 21. (One needs to go to a later hierarchical level for DAUB20 to avoid a wavelet with a wrapped-around tail.) Other unit vectors would give wavelets with the same shapes but different positions and scales.

One sees that both DAUB4 and DAUB20 have wavelets that are continuous. DAUB20 wavelets also have higher continuous derivatives. DAUB4 has the peculiar property that its derivative exists only almost everywhere. Examples of where it fails to exist are the points $p / 2 ^ { n }$ , where $p$ and $n$ are integers; at such points, DAUB4 is left differentiable, but not right differentiable! This kind of discontinuity — at least in some derivative — is a necessary feature of wavelets with compact support, like the Daubechies series. For every increase in the number of wavelet coefficients by two, the Daubechies wavelets gain about half a derivative of continuity. (But not exactly half; the actual orders of regularity are irrational numbers!)

![](images/4803cfb275dd48ff11cab325d4815e7ad207e4adaac5a57817280b9ce24d6c33.jpg)  
Figure 13.10.2. More wavelets, here generated from the sum of two unit vectors, ${ \bf e } _ { 9 } + { \bf e } _ { 5 7 }$ , which are in different hierarchical levels of scale, and also at different spatial positions. DAUB4 wavelets (top) are defined by a filter in coordinate space (equation 13.10.5), while Lemarie wavelets (bottom) are defined by a filter most easily written in Fourier space (equation 13.10.14).

Note that the fact that wavelets are not smooth does not prevent their having exact representations for some smooth functions, as demanded by their approximation order $p$ . The continuity of a wavelet is not the same as the continuity of functions that a set of wavelets can represent. For example, DAUB4 can represent (piecewise) linear functions of arbitrary slope: In the correct linear combinations, the cusps all cancel out. Every increase of two in the number of coefficients allows one higher order of polynomial to be exactly represented.

Figure 13.10.2 shows the result of performing the inverse DWT on the input vector ${ \bf e } _ { 9 } + { \bf e } _ { 5 7 }$ , again for the two different particular wavelets. Since 9 lies early in the hierarchical range of 8–15, that wavelet lies on the left side of the picture. Since 57 lies in a later (smaller-scale) hierarchy, it is a narrower wavelet; in the range of 32–63 it is toward the end, so it lies on the right side of the picture. Note that smaller-scale wavelets are taller, so as to have the same squared integral.

# 13.10.4 Wavelet Filters in the Fourier Domain

The Fourier transform of a set of filter coefficients $c _ { j }$ is given by

$$
H ( \omega ) = \sum _ { j } c _ { j } e ^ { i j \omega }
$$

Here $H$ is a function periodic in $2 \pi$ , and it has the same meaning as before: It is the wavelet filter, now written in the Fourier domain. A very useful fact is that the orthogonality conditions for the $c$ ’s (e.g., equation 13.10.3 above) collapse to two

simple relations in the Fourier domain,

$$
\begin{array} { r } { \frac 1 2 | H ( 0 ) | ^ { 2 } = 1 } \end{array}
$$

and

$$
\begin{array} { r } { \frac { 1 } { 2 } \left[ | H ( \omega ) | ^ { 2 } + | H ( \omega + \pi ) | ^ { 2 } \right] = 1 } \end{array}
$$

Likewise, the approximation condition of order $p$ (e.g., equation 13.10.4 above) has a simple formulation, requiring that $H ( \omega )$ have a $p$ th order zero at $\omega ~ = ~ \pi$ , or (equivalently)

$$
{ \cal H } ^ { ( m ) } ( \pi ) = 0 \qquad m = 0 , 1 , \ldots , p - 1
$$

It is thus relatively straightforward to invent wavelet sets in the Fourier domain. You simply invent a function $H ( \omega )$ satisfying equations $( 1 3 . 1 0 . 9 ) - ( 1 3 . 1 0 . 1 1 )$ . To find the actual $c _ { j }$ ’s applicable to a data (or $s$ -component) vector of length $N$ , and with periodic wraparound as in matrices (13.10.1) and (13.10.2), you invert equation (13.10.8) by the discrete Fourier transform

$$
c _ { j } = \frac { 1 } { N } \sum _ { k = 0 } ^ { N - 1 } H ( 2 \pi \frac { k } { N } ) e ^ { - 2 \pi i j k / N }
$$

The quadrature mirror filter $G$ (reversed $c _ { j }$ ’s with alternating signs), incidentally, has the Fourier representation

$$
G ( \omega ) = e ^ { - i \omega } H ^ { * } ( \omega + \pi )
$$

where the asterisk denotes complex conjugation.

In general, the above procedure will not produce wavelet filters with compact support. In other words, all $N$ of the $c _ { j }$ ’s, $j = 0 , \ldots , N - 1$ will in general be nonzero (though they may be rapidly decreasing in magnitude). The Daubechies wavelets, or other wavelets with compact support, are specially chosen so that $H ( \omega )$ is a trigonometric polynomial with only a small number of Fourier components, guaranteeing that there will be only a small number of nonzero $c _ { j }$ ’s.

On the other hand, there is sometimes no particular reason to demand compact support. Giving it up in fact allows the ready construction of relatively smoother wavelets (higher values of $p$ ). Even without compact support, the convolutions implicit in the matrix (13.10.1) can be done efficiently by FFT methods.

Lemarie’s wavelet (see [4]) has $p = 4$ , does not have compact support, and is defined by the choice of $H ( \omega )$ ,

$$
H ( \omega ) = \left[ 2 ( 1 - u ) ^ { 4 } \frac { 3 1 5 - 4 2 0 u + 1 2 6 u ^ { 2 } - 4 u ^ { 3 } } { 3 1 5 - 4 2 0 v + 1 2 6 v ^ { 2 } - 4 v ^ { 3 } } \right] ^ { 1 / 2 }
$$

where

$$
u \equiv \sin ^ { 2 } \frac { \omega } { 2 } \qquad v \equiv \sin ^ { 2 } \omega
$$

It is beyond our scope to explain where equation (13.10.14) comes from. An informal description is that the quadrature mirror filter $G ( \omega )$ deriving from equation (13.10.14) has the property that it gives identically zero when applied to any function whose odd-numbered samples are equal to the cubic spline interpolation of its even-numbered samples. Since this class of functions includes many very smooth members, it follows that $H ( \omega )$ does a good job of truly selecting a function’s smooth information content. Sample Lemarie wavelets are shown in Figure 13.10.2.

# 13.10.5 Daubechies Wavelets on the Interval

The discrete wavelet transforms that we have seen thus far are periodic and thus “live on a circle.”. Wavelets close to one edge of the data vector have tails that wrap around to the other edge. Said differently, some components of a discrete wavelet transform depend on data values at both ends of the data vector.

Most of the time, this periodicity is merely something between a curiosity and a minor nuisance, exactly like the discrete Fourier transform’s similar periodicity. Similar simple workarounds (e.g., zero-padding of the data) apply. Occasionally, however, the wraparound can produce undesirable effects, for example when the data differ by orders of magnitude at the two ends, or are smooth at one end but unsmooth at the other.

By modifying the coefficients of the wavelet filters near the two ends of the data vector, it is possible to produce wavelets that utilize only local data at each edge, that is, wavelets that “live on the interval” instead of on the circle. For such wavelets, the orthogonal matrix analogous to (13.10.1) is purely band-diagonal, and is identical to (13.10.1) except for modifications in the first and last few rows. Various such constructions have been proposed. Our favorite is that of [7].

One wrinkle needs to be mentioned: We would hope that those modified rows of the new matrix that are “detail filters” have the property of giving exactly zero when applied to smooth polynomial sequences like $1 , 1 , 1 , 1 , 1$ or $1 , 2 , 3 , 4 , 5$ . Indeed, all the period wavelets previously discussed have this property. Alas, this condition, plus orthogonality, imposes too many constraints on the coefficients, and is unachievable. It turns out, however, that a simple linear preconditioning of the first and last few data points (that is, replacing the values by linear combinations of themselves) restores the desired property. The preconditioning is done only once in the transform, not at every pyramidal level. This need for preconditioning (with a corresponding postconditioning for the inverse) is the reason that our Wavelet abstract class has a method named condition. Finally we get to use it in a nontrivial way!

Here is an implementation of DAUB4 wavelets on the interval as a class derived from Wavelet, compatible for use in wt1. The ugliness of the code reflects only the large number of new coefficients that must be provided. If you want to implement higher DAUBn’s on the interval, you’ll need even more coefficients, as found in [6] or [5].

# struct Daub4i : Wavelet {

void filt(VecDoub_IO &a, const Int n, const Int isign) {

Applies the Cohen-Daubechies-Vial 4-coefficient wavelet on the interval filter to data vector a[0..n-1] (for isign $^ { = 1 }$ ) or applies its transpose (for isign $\scriptstyle 1 = - 1$ ). Used hierarchically by routines wt1 and wtn.

const Doub $\mathtt { C O = 0 }$ .4829629131445341, $\mathtt { C 1 } = 0$ .8365163037378077,$\mathtt { C 2 = 0 }$ .2241438680420134, $\scriptstyle \mathrm { C 3 = - 0 }$ .1294095225512603;  
const Doub $\mathtt { R O O = 0 }$ .603332511928053,R01 ${ = } 0$ .690895531839104,$\mathtt { R O 2 } = - 0$ .398312997698228,R10=-0.796543516912183,R11 ${ = } 0$ .546392713959015,R12=-0.258792248333818, $\mathtt { R 2 0 = 0 }$ .0375174604524466,R21 ${ = } 0$ .457327659851769,$\mathtt { R 2 2 } = 0$ .850088102549165,R23 $\mathtt { \mathtt { = 0 } }$ .223820356983114,R24 -0.129222743354319,R30=0.0100372245644139,R31 ${ = } 0$ .122351043116799,R32 ${ = } 0$ .227428111655837,R33 $=$ -0.836602921223654,R34 ${ = } 0$ .483012921773304,R43 ${ } = 0$ .443149049637559,R44 ${ = } 0$ .767556669298114,R45=0.374955331645687,R46 ${ = } 0$ .190151418429955,R47=-0.194233407427412,R53 ${ = } 0$ .231557595006790,R54=0.401069519430217,R55=-0.717579999353722,R56=-0.363906959570891,R57 ${ = } 0$ .371718966535296,R65=0.230389043796969,R66=0.434896997965703,R67 ${ = } 0$ .870508753349866,R75=-0.539822500731772,R76=0.801422961990337,R77=-0.257512919478482;

# wavelet.h

Int nh,i,j; if $\textup { ( n < 8 ) }$ ) return; VecDoub wksp(n); nh $= \mathrm { ~ n ~ } > > \mathrm { ~ 1 ~ }$ ; if (isign $> = \ 0 $ ) { wksp[0] $=$ R00\*a[0]+R01\*a[1]+R02\*a[2]; wksp[nh] $=$ R10\*a[0]+R11\*a[1]+R12\*a[2]; wksp[1] $=$ R20\*a[0]+R21\*a[1]+R22\*a[2]+R23\*a[3]+R24\*a[4]; wksp[nh+1] $=$ R30\*a[0]+R31\*a[1]+R32\*a[2]+R33\*a[3]+R34\*a[4]; for ( $\scriptstyle \dot { 1 } = 2$ ,j $^ { = 3 }$ ;j<n-4;j+=2,i++) { wksp[i] $=$ C0\*a[j]+C1\*a[j+1]+C2\*a[j+2]+C3\*a[j+3]; wksp[i+nh] = C3\*a[j]-C2\*a[j+1]+C1\*a[j+2]-C0\*a[j+3]; wksp[nh-2] $=$ R43\*a[n-5]+R44\*a[n-4]+R45\*a[n-3]+R46\*a[n-2]+R47\*a[n-1]; wksp[n-2] $=$ R53\*a[n-5]+R54\*a[n-4]+R55\*a[n-3]+R56\*a[n-2]+R57\*a[n-1]; wksp[nh-1] $=$ R65\*a[n-3]+R66\*a[n-2]+R67\*a[n-1]; wksp[n-1] $=$ R75\*a[n-3]+R76\*a[n-2]+R77\*a[n-1]; } else { wksp[0] $=$ R00\*a[0]+R10\*a[nh]+R20\*a[1]+R30\*a[nh+1]; wksp[1] $=$ R01\*a[0]+R11\*a[nh]+R21\*a[1]+R31\*a[nh+1]; wksp[2] $=$ R02\*a[0]+R12\*a[nh]+R22\*a[1]+R32\*a[nh+1]; if $\mathbf { \tilde { \Sigma } } _ { \mathbf { n } } \ = = \ 8$ ) { wksp[3] $=$ R23\*a[1]+R33\*a[5]+R43\*a[2]+R53\*a[6]; wksp[4] $=$ R24\*a[1]+R34\*a[5]+R44\*a[2]+R54\*a[6]; } else { wksp[3] $=$ R23\*a[1]+R33\*a[nh+1]+C0\*a[2]+C3\*a[nh+2]; wksp[4] $=$ R24\*a[1]+R34\*a[nh+1]+C1\*a[2]-C2\*a[nh+2]; wksp[n-5] $=$ C2\*a[nh-3]+C1\*a[n-3]+R43\*a[nh-2]+R53\*a[n-2]; wksp[n-4] $=$ C3\*a[nh-3]-C0\*a[n-3]+R44\*a[nh-2]+R54\*a[n-2]; } for ( $\scriptstyle \dot { 1 } = 2$ ,j=5;i<nh-3;i++) { wksp[j++] $=$ C2\*a[i]+C1\*a[i+nh]+C0\*a[i+1]+C3\*a[i+nh+1]; wksp[j++] = C3\*a[i]-C0\*a[i+nh]+C1\*a[i+1]-C2\*a[i+nh+1]; } wksp[n-3] $=$ R45\*a[nh-2]+R55\*a[n-2]+R65\*a[nh-1]+R75\*a[n-1]; wksp[n-2] $=$ R46\*a[nh-2]+R56\*a[n-2]+R66\*a[nh-1]+R76\*a[n-1]; wksp[n-1] $=$ R47\*a[nh-2]+R57\*a[n-2]+R67\*a[nh-1]+R77\*a[n-1]; } for ( $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) a[i] $=$ wksp[i]; void condition(VecDoub_IO &a, const Int n, const Int isign) { Doub t0,t1,t2,t3; if $\mathbf { \zeta } ( \mathbf { n } ~ < ~ 4 )$ return; if (isign $> = ~ 0$ ) { $\mathtt { t } 0 \ = \ 0$ .324894048898962\*a[0] $+ 0$ .0371580151158803\*a[1]; t1 = 1.00144540498130\*a[1]; t2 = 1.08984305289504\*a[n-2]; t3 = -0.800813234246437\*a[n-2] $^ { + 2 }$ .09629288435324\*a[n-1]; a[0] $=$ t0; a[1] $=$ t1; a[n-2] $= \pm 2$ ; a[n-1] $=$ t3; } else { $\mathtt { t 0 } ~ =$ 3.07792649138669 $^ { * } \mathtt { a }$ [0]-0.114204567242137\*a[1]; $\ t 1 \ =$ 0.998556681198888\*a[1]; t2 $=$ 0.917563310922261\*a[n-2]; t3 = 0.350522032550918\*a[n-2] $+ 0$ .477032578540915\*a[n-1]; a[0] $\mathtt { \mathtt { = t 0 } }$ ; a[1] $=$ t1; a[n-2] $=$ t2; a[n-1] $= \mathtt { t } 3$ ; } }

Do you really need wavelets on the interval, instead of ordinary, periodic wavelets? Occasionally, yes. If you look ahead to Figure 13.10.6, which is a graphical display of two-dimensional wavelet coefficients, you can see the difference between

![](images/f817ad3614d7ab6d5601ab5d50f50de484a129925607713e091dacd07a8b230e.jpg)  
Figure 13.10.3. Top: Arbitrary test function, with cusp, sampled on a vector of length 1024. Bottom: Absolute value of the 1024 wavelet coefficients produced by the discrete wavelet transform of the function. Note log scale. The dotted curve plots the same amplitudes when sorted by decreasing size. One sees that only 130 out of 1024 coefficients are larger than $1 0 ^ { - 4 }$ (or larger than about $1 0 ^ { - 5 }$ times the largest coefficient, whose value is $\sim 1 0$ ).

allowing and suppressing wraparound.

# 13.10.6 Truncated Wavelet Approximations

Most of the usefulness of wavelets rests on the fact that wavelet transforms can usefully be severely truncated, that is, turned into sparse expansions. The case of Fourier transforms is different: FFTs are ordinarily used without truncation, to compute fast convolutions, for example. This works because the convolution operator is particularly simple in the Fourier basis. There are not, however, any standard mathematical operations that are especially simple in the wavelet basis.

To see how truncation works, consider the simple example shown in Figure 13.10.3. The upper panel shows an arbitrarily chosen test function, smooth except for a square-root cusp, sampled onto a vector of length $2 ^ { 1 0 }$ . The bottom panel (solid curve) shows, on a log scale, the absolute value of the vector’s components after it has been run through the DAUB4 discrete wavelet transform. One notes, from right to left, the different levels of hierarchy, 512–1023, 256–511, 128–255, etc. Within each level, the wavelet coefficients are nonnegligible only very near the location of the cusp, or very near the left and right boundaries of the hierarchical range (edge effects).

The dotted curve in the lower panel of Figure 13.10.3 plots the same amplitudes as the solid curve, but sorted into decreasing order of size. One can read off, for example, that the 130th largest wavelet coefficient has an amplitude less than $1 0 ^ { - 5 }$ of the largest coefficient, whose magnitude is $\sim 1 0$ (power or square integral ratio less than $1 0 ^ { - 1 0 }$ ). Thus, the example function can be represented quite accurately by only 130, rather than 1024, coefficients — the remaining ones being set to zero.

Note that this kind of truncation makes the vector sparse, but still of logical length 1024. It is very important that vectors in wavelet space be truncated according to the amplitude of the components, not their position in the vector. Keeping the first 256 components of the vector (all levels of the hierarchy except the last two) would give an extremely poor, and jagged, approximation to the function. When you compress a function with wavelets, you have to record both the values and the positions of the nonzero coefficients.

Generally, compact (and therefore unsmooth) wavelets are better for lower accuracy approximations and for functions with discontinuities (like edges). Smooth (and therefore noncompact) wavelets are better for achieving high numerical accuracy. This makes compact wavelets a good choice for image compression, for example, while it makes smooth wavelets best for fast solution of integral equations.

In real applications of wavelets to compression, components are not starkly “kept” or “discarded.” Rather, components may be kept with a varying number of bits of accuracy, depending on their magnitude. The JPEG-2000 image compression standard utilizes wavelets in such a manner.

# 13.10.7 Wavelet Transform in Multidimensions

A wavelet transform of a $d$ -dimensional array is most easily obtained by transforming the array sequentially on its first index (for all values of its other indices), then on its second, and so on. Each transformation corresponds to multiplication by an orthogonal matrix M. Because (illustrating the case $d = 2$ )

$$
\sum _ { j } M _ { n j } \biggl ( \sum _ { i } M _ { m i } a _ { i j } \biggr ) = \sum _ { i } M _ { m i } \biggl ( \sum _ { j } M _ { n j } a _ { i j } \biggr )
$$

the result is independent of the order in which the indices were transformed. The situation is exactly like that for multidimensional FFTs. A routine for effecting the multidimensional DWT can thus be modeled on a multidimensional FFT routine like fourn:

# void wtn(VecDoub_IO &a, VecInt_I &nn, const Int isign, Wavelet &wlet)

Replaces a by its ndim-dimensional discrete wavelet transform, if isign is input as 1. Here nn[0..ndim-1] is an integer array containing the lengths of each dimension (number of real values), which must all be powers of 2. a is a real array of length equal to the product of these lengths, in which the data are stored as in a multidimensional real array. If isign is input as 1, a is replaced by its inverse wavelet transform. The object wlet, of type Wavelet, is the underlying wavelet filter. Examples of Wavelet types are Daub4, Daubs, and Daub4i. {

Int idim,i1,i2,i3,k,n,nnew,nprev ${ \tt = } 1$ ,nt,ntot=1;   
Int ndim=nn.size();   
for (idim $_ { 1 = 0 }$ ;idim<ndim;idim $^ { + + }$ ) ntot $\ast =$ nn[idim];   
if (ntot&(ntot-1)) throw("all lengths must be powers of 2 in wtn");   
for (idim $_ { = 0 }$ ;idim<ndim;idim $^ { + + }$ ) { Main loop over the dimensions. $\mathbf { n } =$ nn[idim]; VecDoub wksp(n); nnew=n\*nprev; if $\mathrm { ~ ( ~ n ~ ) ~ 4 ~ }$ ) { for ( $\scriptstyle { \dot { 1 } } 2 = 0 ;$ ;i2<ntot;i2 $+ =$ nnew) { for (i1=0;i1<nprev;i1++) { for (i3=i1+i2, $\mathtt { k } = 0$ ;k<n;k++,i3 $+ =$ nprev) wksp[k] $= a$ [i3]; Copy the relevant row or column or etc. into workspace. if (isign $\scriptstyle > = 0 .$ ) { Do one-dimensional wavelet transform.

![](images/f8d867c083f96a80b0c7ef64f70bb8fb3b1dbef72ee39e0b27ca2207287e03fe.jpg)  
Figure 13.10.4. (a) Two-dimensional array of intensities (i.e., a photograph) and (b) its two-dimensional discrete wavelet transform. Darker pixels represent wavelet components that are larger in magnitude, on a logarithmic scale. Wavelets number from the upper-left corner, where the “smooth” information content is encoded.

wlet.condition(wksp,n,1); for( $\mathtt { n t } \mathtt { = n }$ ;nt $> = 4$ ;nt $> > = ~ 1$ ) wlet.filt(wksp,nt,isign); } else { Or inverse transform. for(nt=4;nt $< = _ { \mathrm { { n } } }$ ;nt <<= 1) wlet.filt(wksp,nt,isign); wlet.condition(wksp,n,-1); } for (i3=i1+i2,k=0;k<n;k++,i3 $+ =$ nprev) a[i3] $=$ wksp[k]; Copy back from workspace. } } nprev=nnew; } }

Here, as before, wlet is a Wavelet object that embodies a particular wavelet filter and (if required) pre-conditioner.

Figure 13.10.4 shows a sample image and its wavelet transform, represented graphically.

# 13.10.8 Compression of Images

An immediate application of the multidimensional transform wtn is to image compression. The overall procedure is to take the wavelet transform of a digitized image, and then to “allocate bits” among the wavelet coefficients in some highly nonuniform, optimized, manner. As already mentioned, large wavelet coefficients get quantized accurately, while small coefficients are quantized coarsely with only a bit or two — or else are truncated completely. If the resulting quantization levels are still statistically nonuniform, they may then be further compressed by a technique like Huffman coding (-22.5).

While a more detailed description of the “back end” of this process, namely the quantization and coding of the image, is beyond our scope, it is quite straightforward to demonstrate the “front-end” wavelet encoding with a simple truncation: We keep (with full accuracy) all wavelet coefficients larger than some threshold, and we delete (set to zero) all smaller wavelet coefficients. We can then adjust the threshold to vary the fraction of preserved coefficients.

![](images/36de336e60431cfdb3a93c1abfb16841792a1c84959a009ec3cbd686553712e8.jpg)  
Figure 13.10.5. (a) IEEE test image, $2 5 6 \times 2 5 6$ pixels with 8-bit grayscale. (b) The image is transformed into the wavelet basis; $7 7 \%$ of its wavelet components are set to zero (those of smallest magnitude); it is then reconstructed from the remaining $23 \%$ . (c) Same as (b), but $9 4 . 5 \%$ of the wavelet components are deleted. (d) Same as (c), but the Fourier transform is used instead of the wavelet transform. Wavelet coefficients are better than the Fourier coefficients at preserving relevant details.

Figure 13.10.5 shows a sequence of images that differ in the number of wavelet coefficients that have been kept. The original picture (a), which is an official IEEE test image, has 256 by 256 pixels with an 8-bit grayscale. The two reproductions following are reconstructed with $23 \%$ (b) and $5 . 5 \%$ (c) of the 65536 wavelet coefficients. The latter image illustrates the kind of compromises made by the truncated wavelet representation. High-contrast edges (the model’s right cheek and hair highlights, e.g.) are maintained at a relatively high resolution, while low-contrast areas (the model’s left eye and cheek, e.g.) are washed out into what amounts to large constant pixels. Figure 13.10.5(d) is the result of performing the identical procedure with Fourier, instead of wavelet, transforms: The figure is reconstructed from the $5 . 5 \%$ of 65536 real Fourier components having the largest magnitudes. One sees that, since sines and cosines are nonlocal, the resolution is uniformly poor across the picture; also, the deletion of any components produces a mottled “ringing” everywhere. (Practical Fourier image compression schemes therefore break up an image into small blocks of pixels, $1 6 \times 1 6$ , say, and do rather elaborate smoothing across block boundaries when the image is reconstructed.)

Viewers will sometimes choose (b) over (a), in Figure 13.10.5, as the superior image. The reason is that a “little bit” of wavelet compression has the effect of denoising the image. See [8] for a rigorous development.

# 13.10.9 Fast Solution of Linear Systems

There are interesting applications of wavelets to linear algebra. The basic idea [1] is to think of an integral operator (that is, a large matrix) as a digital image. Suppose that the operator compresses well under a two-dimensional wavelet transform, i.e., that a large fraction of its wavelet coefficients are so small as to be negligible. Then any linear system involving the operator becomes a sparse system in the wavelet basis. In other words, to solve

$$
\mathbf { A \cdot x } = \mathbf { b }
$$

we first wavelet-transform the operator A and the right-hand side $\mathbf { b }$ by

$$
\widetilde { \mathbf { A } } \equiv \mathbf { W } \cdot \mathbf { A } \cdot \mathbf { W } ^ { T } , \qquad \widetilde { \mathbf { b } } \equiv \mathbf { W } \cdot \mathbf { b }
$$

where W represents the one-dimensional wavelet transform, then solve

$$
\widetilde { { \bf A } } \cdot \widetilde { { \bf x } } = \widetilde { { \bf b } }
$$

and finally transform to the answer by the inverse wavelet transform

$$
\mathbf { x } = \mathbf { W } ^ { T } \cdot \widetilde { \mathbf { x } }
$$

(Note that the routine wtn does the complete transformation of $\mathbf { A }$ into $\widetilde { \bf A }$ .)

A typical integral operator that compresses well into wavelets has arbitrary (or even nearly singular) elements near its main diagonal, but becomes smooth away from the diagonal. An example might be

$$
A _ { i j } = { \left\{ \begin{array} { l l } { - 1 } & { { \mathrm { i f ~ } } i = j } \\ { | i - j | ^ { - 1 / 2 } } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

Figure 13.10.6 shows a graphical representation of the wavelet transform of this matrix, where $i$ and $j$ range over 0 : : : 255, using the DAUB4 wavelet, both in its conventional, periodic, implementation, and its modified form on the interval. Elements larger in magnitude than $1 0 ^ { - 3 }$ times the maximum element are shown as black pixels, while elements between $1 0 ^ { - 3 }$ and $1 0 ^ { - 6 }$ are shown in gray. White pixels are $< 1 0 ^ { - 6 }$ . The indices $i$ and $j$ each number from the lower left.

In the figure, one sees the hierarchical decomposition into power-of-two sized blocks. At the edges or corners of the various blocks, one sees edge effects caused by the wraparound wavelet boundary conditions. Apart from edge effects, within each block, the nonnegligible elements are concentrated along the block diagonals. This is a statement that, for this type of linear operator, a wavelet is coupled mainly to near neighbors in its own hierarchy (square blocks along the main diagonal) and near neighbors in other hierarchies (rectangular blocks off the diagonal).

The number of nonnegligible elements in a matrix like that in Figure 13.10.6 scales only as $N$ , the linear size of the matrix; as a rough rule of thumb it is about

![](images/149bf2492f788a20f65e525eace1f6d1eac4dfecd9b178d007997fa8ea10cdb8.jpg)  
Figure 13.10.6. Wavelet transform of a $2 5 6 \times 2 5 6$ matrix, represented graphically. The original matrix has a discontinuous cusp along its diagonal, decaying smoothly away on both sides of the diagonal. In wavelet basis, the matrix becomes sparse: Components larger than $1 0 ^ { \dot { - } 3 }$ are shown as black, components larger than $1 0 ^ { - 6 }$ as gray, and smaller-magnitude components are white. The matrix indices $i$ and $j$ number from the lower left. (a) Ordinary DAUB4 (periodic) is used. (b) Modified DAUB4 on the interval is used, eliminating wraparound artifacts and producing a more regular pattern of significant components.

$1 0 N \log _ { 1 0 } ( 1 / \epsilon )$ , where $\epsilon$ is the truncation level, e.g., $1 0 ^ { - 6 }$ . For a 2000 by 2000 matrix, then, the matrix is sparse by a factor on the order of 30.

Various numerical schemes can be used to solve sparse linear systems of this “hierarchically band-diagonal” form. Beylkin, Coifman, and Rokhlin [1] make the interesting observations that (1) the product of two such matrices is itself hierarchically band-diagonal (truncating, of course, newly generated elements that are smaller than the predetermined threshold $\epsilon$ ); and, moreover, that (2) the product can be formed in order $N$ operations.

Fast matrix multiplication enables finding the matrix inverse by Schultz’s (or Hotelling’s) method; see $\ S 2 . 5$ .

Other schemes are also possible for fast solution of hierarchically band-diagonal forms. For example, one can use the conjugate gradient method, implemented in $\ S 2 . 7$ as linbcg.

# CITED REFERENCES AND FURTHER READING:

Daubechies, I. 1992, Wavelets (Philadelphia: S.I.A.M.).

Strang, G. 1989, “Wavelets and Dilation Equations: A Brief Introduction,” SIAM Review, vol. 31, pp. 614–627.

Beylkin, G., Coifman, R., and Rokhlin, V. 1991, “Fast Wavelet Transforms and Numerical Algorithms,” Communications on Pure and Applied Mathematics, vol. 44, pp. 141–183.[1]

Daubechies, I. 1988, “Orthonormal Bases of Compactly Supported Wavelets,” Communications on Pure and Applied Mathematics,vol.41,pp. 909-996.[2]

Vaidyanathan, P.P. 1990, “Multirate Digital Filters, Filter Banks, Polyphase Networks, and Applications,” Proceedings of the IEEE, vol. 78, pp. 56–93.[3]

Mallat, S.G. 1989, “A Theory for Multiresolution Signal Decomposition: The Wavelet Representation,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 11, pp. 674– 693.[4]

Cohen, A. 1993, “Tables for Wavelet Filters Adapted to Life on an Interval,” multiple Web sites; mirrored at http://www.nr.com/contrib.[5]

Brewster, M.E. and Beylkin, G. 1994, tables from “Double Precision Wavelet Transform Library,” mirrored at http://www.nr.com/contrib.[6]   
Cohen, A., Daubechies, I., and Vial, P. 1993, “Wavelets on the Interval and Fast Wavelet Transforms,” Applied and Computational Harmonic Analysis, vol. 1, pp. 54–81.[7]   
Donoho, D. and Johnstone, I.M. 1994, “Ideal Spatial Adaptation via Wavelet Shrinkage,” Biometrika, vol. 81, no. 3, pp. 425–455.[8]

# 13.11 Numerical Use of the Sampling Theorem

We have met the sampling theorem before, in $\ S 4 . 5$ (in relation to the accuracy of the trapezoidal rule for integration); in $\ S 6 . 9$ , where we implemented an approximating formula for Dawson’s integral due to Rybicki, and in $\ S 1 2 . 1$ , where we first saw it in a Fourier context. Now that we have become Fourier sophisticates, we can readily supply a derivation of the formula in $\ S 6 . 9$ and illustrate the use of the sampling theorem as a purely numerical tool. Our discussion is identical to Rybicki [1].

For our present purposes, the sampling theorem is most conveniently stated as follows: Consider an arbitrary function $g ( t )$ and the grid of sampling points $t _ { n } = \alpha + n h$ , where $n$ ranges over the integers and $\alpha$ is a constant that allows an arbitrary shift of the sampling grid. We then write

$$
g ( t ) = \sum _ { n = - \infty } ^ { \infty } g ( t _ { n } ) \operatorname { s i n c } { \frac { \pi } { h } } ( t - t _ { n } ) + e ( t )
$$

where sinc $x \equiv \sin x / x$ . The summation over the sampling points is called the sampling representation of $g ( t )$ , and $e ( t )$ is its error term. The sampling theorem asserts that the sampling representation is exact, that is, $e ( t ) \equiv 0$ , if the Fourier transform of $g ( t )$ ,

$$
G ( \omega ) = \int _ { - \infty } ^ { \infty } g ( t ) e ^ { i \omega t } d t
$$

vanishes identically for $| \omega | \geq \pi / h$ .

When can sampling representations be used to advantage for the approximate numerical computation of functions? In order that the error term be small, the Fourier transform $G ( \omega )$ must be sufficiently small for $| \omega | \ge \pi / h$ . On the other hand, in order for the summation in (13.11.1) to be approximated by a reasonably small number of terms, the function $g ( t )$ itself should be very small outside of a fairly limited range of values of $t$ . Thus we are led to two conditions to be satisfied in order that (13.11.1) be useful numerically: Both the function $g ( t )$ and its Fourier transform $G ( \omega )$ must rapidly approach zero for large values of their respective arguments.

Unfortunately, these two conditions are mutually antagonistic — the Uncertainty Principle in quantum mechanics. There exist strict limits on how rapidly the simultaneous approach to zero can be in both arguments. According to a theorem of Hardy [2], if $g ( t ) = O ( e ^ { - t ^ { 2 } } )$ as $| t |  \infty$ and $G ( \omega ) = O ( e ^ { - \omega ^ { 2 } / 4 } )$ as $| \omega |  \infty$ , then $g ( t ) \equiv C e ^ { - t ^ { 2 } }$ , where $C$ is a constant. This can be interpreted as saying that, of all functions, the Gaussian is the most rapidly decaying in both $t$ and $\omega$ , and in this sense is the “best” function to be expressed numerically as a sampling representation.

Let us then write for the Gaussian $g ( t ) = e ^ { - t ^ { 2 } }$ ,

$$
e ^ { - t ^ { 2 } } = \sum _ { n = - \infty } ^ { \infty } e ^ { - t _ { n } ^ { 2 } } \operatorname { s i n c } { \frac { \pi } { h } } ( t - t _ { n } ) + e ( t )
$$

The error $e ( t )$ depends on the parameters $h$ and $\alpha$ as well as on $t$ , but it is sufficient for the present purposes to state the bound,

$$
| e ( t ) | < e ^ { - ( \pi / 2 h ) ^ { 2 } }
$$

which can be understood simply as the order of magnitude of the Fourier transform of the Gaussian at the point where it “spills over” into the region $| \omega | > \pi / h$ .

When the summation in (13.11.3) is approximated by one with finite limits, say from $N _ { 0 } - N$ to $N _ { 0 } + N$ , where $N _ { 0 }$ is the integer nearest to $- \alpha / h$ , there is a further truncation error. However, if $N$ is chosen so that $N > \pi / ( 2 h ^ { 2 } )$ , the truncation error in the summation is less than the bound given by (13.11.4), and, since this bound is an overestimate, we shall continue to use it for (13.11.3) as well. The truncated summation gives a remarkably accurate representation for the Gaussian even for moderate values of $N$ . For example, $| e ( t ) | \dot { < } 5 { \times } 1 0 ^ { - 5 }$ for $h = 1 / 2$ and $N = 7$ ; $| e ( t ) | < 2 \times 1 0 ^ { - 1 0 }$ for $h = 1 / 3$ and $N = 1 5$ ; and $| e ( t ) | < 7 \times 1 0 ^ { - 1 8 }$ for $h = 1 / 4$ and $N = 2 5$ .

One may ask, what is the point of such a numerical representation for the Gaussian, which can be computed so easily and quickly as an exponential? The answer is that many transcendental functions can be expressed as an integral involving the Gaussian, and by substituting (13.11.3) one can often find excellent approximations to the integrals as a sum over elementary functions.

Let us consider as an example the function $w ( z )$ of the complex variable $z = x + i y$ related to the complex error function by

$$
w ( z ) = e ^ { - z ^ { 2 } } \operatorname { e r f c } ( - i z )
$$

having the integral representation

$$
w ( z ) = { \frac { 1 } { \pi i } } \int _ { C } { \frac { e ^ { - t ^ { 2 } } d t } { t - z } }
$$

where the contour $C$ extends from $- \infty$ to $\infty$ , passing below $z$ (see, e.g., [3]). Many methods exist for the evaluation of this function (e.g., [4]). Substituting the sampling representation (13.11.3) into (13.11.6) and performing the resulting elementary contour integrals, we obtain

$$
w ( z ) \approx { \frac { 1 } { \pi i } } \sum _ { n = - \infty } ^ { \infty } h e ^ { - t _ { n } ^ { 2 } } { \frac { 1 - ( - 1 ) ^ { n } e ^ { - \pi i ( \alpha - z ) / h } } { t _ { n } - z } }
$$

where we now omit the error term. One should note that there is no singularity as $z  t _ { m }$ for some $n = m$ , but a special treatment of the mth term will be required in this case (for example, by power series expansion).

An alternative form of equation (13.11.7) can be found by expressing the complex exponential in (13.11.7) in terms of trigonometric functions and using the sampling representation (13.11.3) with $z$ replacing $t$ . This yields

$$
w ( z ) \approx e ^ { - z ^ { 2 } } + \frac { 1 } { \pi i } \sum _ { n = - \infty } ^ { \infty } h e ^ { - t _ { n } ^ { 2 } } \frac { 1 - ( - 1 ) ^ { n } \cos \pi ( \alpha - z ) / h } { t _ { n } - z }
$$

This form is particularly useful in obtaining $ { \mathrm { R e } } w ( z )$ when $| y | \ll 1$ . Note that in evaluating (13.11.7) the complex exponential inside the summation is a constant and needs to be evaluated only once; a similar comment holds for the cosine in (13.11.8).

There are a variety of formulas that can now be derived from either equation (13.11.7) or (13.11.8) by choosing particular values of $\alpha$ . Eight interesting choices are $\alpha = 0$ , $x$ , $i y$ , or $\boldsymbol { Z }$ , plus the values obtained by adding $h / 2$ to each of these. Since the error bound (13.11.3) assumed a real value of $\alpha$ , the choices involving a complex $\alpha$ are useful only if the imaginary part of $z$ is not too large. This is not the place to catalog all 16 possible formulas, and we give only two particular cases that show some of the important features.

First of all let $\alpha = 0$ in equation (13.11.8), which yields,

$$
w ( z ) \approx e ^ { - z ^ { 2 } } + \frac { 1 } { \pi i } \sum _ { n = - \infty } ^ { \infty } h e ^ { - ( n h ) ^ { 2 } } \frac { 1 - ( - 1 ) ^ { n } \cos ( \pi z / h ) } { n h - z }
$$

This approximation is good over the entire $z$ -plane. As stated previously, one has to treat the case where one denominator becomes small by expansion in a power series. Formulas for

the case $\alpha = 0$ were discussed briefly in [5]. They are similar, but not identical, to formulas derived by Chiarella and Reichel [6], using the method of Goodwin [7].

Next, let $\alpha = z$ in (13.11.7), which yields

$$
w ( z ) \approx e ^ { - z ^ { 2 } } - \frac { 2 } { \pi i } \sum _ { n \mathrm { o d d } } \frac { e ^ { - ( z - n h ) ^ { 2 } } } { n }
$$

the sum being over all odd integers (positive and negative). Note that we have made the substitution $n  - n$ in the summation. This formula is simpler than (13.11.9) and contains half the number of terms, but its error is worse if $y$ is large. Equation (13.11.10) is the source of the approximation formula (6.9.3) for Dawson’s integral, used in $\ S 6 . 9$ .

# CITED REFERENCES AND FURTHER READING:

Rybicki, G.B. 1989, “Dawson’s Integral and The Sampling Theorem,” Computers in Physics, vol. 3, no. 2, pp. 85–87.[1]   
Hardy, G.H. 1933, “A Theorem Concerning Fourier Transforms,” Journal of the London Mathematical Society, vol.8, pp.227-231.[2]   
Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands.[3]   
Gautschi, W. 1970, “Efficient Computation of the Complex Error function,” SIAM Journal on Numerical Analysis,vol.7,pp.187-198.[4]   
Armstrong, B.H., and Nicholls, R.W. 1972, Emission, Absorption and Transfer of Radiation in Heated Atmospheres (New York: Pergamon).[5]   
Chiarella, C., and Reichel, A. 1968, “On the Evaluation of Integrals Related to the Error Function,” Mathematics of Computation,vol. 22, pp.137-143.[6]   
Goodwin, E.T. 1949, “The Evaluation of Integrals of the Form $\textstyle \int _ { - x } ^ { + x } f ( x ) e ^ { - x ^ { 2 } } d x$ ,” Proceedings of the Cambridge Philosophical Society, vol.45,pp.241-245.[7]

# Statistical Description of Data

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