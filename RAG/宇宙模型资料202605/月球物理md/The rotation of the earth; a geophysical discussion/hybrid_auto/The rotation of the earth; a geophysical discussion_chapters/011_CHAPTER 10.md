# CHAPTER 10

# THE CHANDLER WOBBLE

# 1. The astronomical evidence

The latitude component $m_{1}$ before and after removal of the seasonal terms is shown in fig. 7.4. The non-seasonal residue reveals 14-month oscillations in wave 'packets' consisting of something like 10 cycles. This is brought out more clearly from a plot (fig. 10.1)

![](images/c8e9361c4360210cd5e59033a2ef5d43e4af0c0d3e2a92e61a33739da2af1d57.jpg)  
Fig. 10.1. The un-normalized autocorrelation $R_{11}(\tau)$ (solid) and cross-correlation $R_{12}(\tau)$ (dashed) for the unsmoothed ILS observations. The abscissa gives $\tau$ , the number of months $m_2$ is lagged. The ordinate is in units of $(0^{\circ}01)^{3}$ . $R_{22}(\tau)$ is similar to $R_{11}(\tau)$ but somewhat higher; only the point $R_{22}(0)$ is shown.

of the un-normalized autocorrelation $R_{11}(\tau)$ and cross-correlation $R_{12}(\tau)$ , where

$$
R _ {u v} (\tau) = \left\langle m _ {u} (t) m _ {v} (t - \tau) \right\rangle , \tag {10.1.1}
$$

the average $\langle \rangle$ being taken over time $t$ . The amplitude of the autocorrelation is reduced by approximately 10 per cent for a lag, $\tau$ , equal to one wave period, thus indicating a damping time of roughly a decade. From the cross-correlation we find that the oscillations are in phase if $m_2$ is advanced by one-fourth the wave period. This is the expected relation for positive (east-to-west) motion.

Fig. 10.2 shows the smoothed spectra (A.2.4, 6) of the unsmoothed ILS latitudes and of the latitude of Washington (fig. 7.4). Rudnick's unsmoothed spectrum is included for comparison. The analyses are not altogether equivalent. Rudnick's computation gives the spectra $S^{+}$ and $S^{-}$ of positive and negative rotation.* Starting with

* Rudnick's published values refer to $(m^{+})^{2}$ in units of $(0^{\prime \prime}01)^{2}$ . In our convention, the power per harmonic equals the mean-square amplitude, $\frac{1}{2}(m^{+})^{2}$ , and the power density $S^{+} = \frac{1}{2} T(m^{+})^{2}$ , where $T = 54.4$ years is the length of record. Accordingly, Rudnick's values are multiplied by 27.2 to give $S^{+}$ in $(0^{\prime \prime}01)^{2} / c$ /year,

the relationships (6.7.6) it can be shown that

$$
S ^ {\pm} = \frac {1}{2} \left[ S _ {1 1} + S _ {2 2} \pm 2 \left(- S _ {1 2} ^ {\prime}\right) \right] \tag {10.1.2}
$$

We find that $S_{11}, S_{22}$ and $-S_{13}'$ are nearly equal, so that

$$
S ^ {+} \approx S _ {1 1}, \quad S ^ {-} \ll S _ {1 1}. \tag {10.1.3}
$$

If the data were consistent, then all spectra in fig. 10.2 should look nearly alike.

![](images/575e8f316ad7a6da76a38fe0a7cbd1347b9087e0beb0723f2be31ec0915903c2.jpg)  
Fig. 10.2. Power spectra of latitude. Solid lines: $\overline{S_{11}}$ and $\overline{S_{22}}$ , 1900 to 1954, from ILS. Dashed lines, open circles: $\frac{1}{2} S^{+}$ , 1891 to 1945, from Kulikov's complication, according to Rudnick. Dashed lines, solid circles: Washington latitude for 1916-1952. The ordinate gives power density in units of $(0^{2}01)^{3} / c/$ year.

Another difference is that Rudnick's spectrum is not smoothed. In the unsmoothed spectrum the energy associated with a single harmonic should be regarded as a random variable possessing a Rayleigh distribution and consequently a standard deviation as great at its expected value. The purpose of the smoothing procedure is to combine many adjoining harmonics into a single estimate with a smaller standard deviation. Resolution is traded for reliability. In the present application the amount of data is so limited that the resulting smoothing is negligible. The only reason for obtaining smoothed spectra is that the computing procedure was readily available. In the smoothed spectra a single harmonic of unit power is split into three adjoining harmonics containing $\frac{1}{4}, \frac{1}{2}, \frac{1}{4}$ units of power.

In view of these considerations the differences in the shape of spectra are no larger than is to be expected. Thus even half a century of observations is strikingly limited in its ability to determine the form of the spectrum. Differences in area under the curves are significant and may be due, at least in part, to the lack of overlap between the records.

We shall describe the spectral peak by three parameters: (1) its area, (2) its central frequency, and (3) some measure of its departure from a spectral line. The parameters depend somewhat on the type of curve to be fitted to the peak. Rudnick's procedure is to replace the frequency of nutation, $\sigma_0$ , by the complex frequency

$$
\sigma_ {0} = \sigma_ {0} + i \alpha , \tag {10.1.4}
$$

where $\sigma_0$ and $\alpha$ are real positive constants. Accordingly, we must replace

$$
\frac {\mathrm {d} \mathbf {m}}{\mathrm {d} t} - i \sigma_ {0} \mathbf {m} = - i \sigma_ {0} \boldsymbol {\Psi} \tag {6.3.6}
$$

$$
\mathrm {b y} ^ {*} \quad \frac {\mathrm {d} \mathbf {m}}{\mathrm {d} t} - i \sigma_ {0} \mathbf {m} = - i \sigma_ {0} \Psi \tag {10.1.5}
$$

which contains an additional term, $\pmb{\alpha}\mathbf{m}$ ; this term leads to a damping of the free motion, according to

$$
\mathbf {m} = \mathrm {e} ^ {i \sigma_ {0} t} = \mathrm {e} ^ {- \alpha t} (\cos \sigma_ {0} t + i \sin \sigma_ {0} t). \tag {10.1.6}
$$

* Rudnick (1956) writes— $i\sigma_0\psi$ on the right side of the equation.

For circular positive polarization the power transmission (see 6.7.10) equals

$$
I ^ {2} (f) = \frac {f _ {0} ^ {2}}{(\alpha / 2 \pi) ^ {2} + (f - f _ {0}) ^ {2}} = \frac {S _ {0} ^ {+}}{S _ {1} ^ {+}} \tag {10.1.7}
$$

where $S_0^+(f)$ and $S_i^+(f)$ are the output and input spectra for positive motion. The power transmission is peaked at $f = f_0$ and attains half the peak value at $f = f_0 \pm \alpha / (2\pi)$ . The area under the curve (including negative frequencies) is

$$
2 \int_ {0} ^ {\infty} \frac {f _ {0} ^ {2}}{(\alpha / 2 \pi) ^ {2} + (f - f _ {0}) ^ {2}} d f = \frac {2 \pi^ {2} f _ {0} ^ {2}}{\alpha}. \tag {10.1.8}
$$

The sharpness of the peak is conveniently portrayed by the dimensionless parameter

$$
Q = \frac {\sigma_ {0}}{2 \alpha} = \frac {\pi f _ {0}}{\alpha}. \tag {10.1.9}
$$

We may assume that the input spectrum is flat over the narrow range of frequencies contained in the Chandler wobble. The recorded spectrum is then of the form $S_{1}^{+}(f_{0})I^{2}(f)$ , and the total power in the Chandler wobble is given by

$$
\frac {2 \pi^ {2} f _ {0} ^ {2}}{\alpha} S _ {i} ^ {+} (f). \tag {10.1.10}
$$

The constant parameters $f_0, \alpha, S_i^+$ can be determined by fitting (10.1.7) to the computed spectra. The fitting has been done by the method of maximum likelihood (§ A.2), following a suggestion by Jeffreys (personal communication). The results are given in table 10.1*; one of the fittings is shown in fig. 7.5.†

* The summations (A.2.8) extend over all harmonics in the Chandler peak. The indicated probability ranges in table 10.1 correspond to values for which $\varphi$ has half its peak value. The ranges for $f_0$ and $S^+$ were obtained by varying the parameters $f_0$ and $A$ separately: for $\alpha, A$ and $B$ were varied concurrently so that $A^2 / B$ retained the value associated with maximum $\varphi$ (total power is held constant).

For the smoothed spectra neighboring harmonics are not independent, but every other harmonic is nearly so, according to (A.2.6). For that reason separate analyses of even harmonics, and of odd harmonics, were conducted for the ILS observations. Furthermore, the smoothing lowers and spreads the spectra. If the unsmoothed spectra is of the form (A.2.7), the smoothed spectrum is

$$
\overline {{S _ {n}}} = \frac {A (1 + 2 \epsilon^ {2})}{B (1 + 4 \epsilon^ {2}) + \left(f _ {n} - f _ {0}\right) ^ {2}}, \tag {10.1.11}
$$

where $\epsilon^{-1} = 2\tau_0\alpha/\pi$ is the number of harmonics (assumed large) between the half-power points. For the ILS values, $\epsilon^{-1} = 2\cdot 2$ and $1\cdot 2$ for even and odd harmonics, respectively, and no adjustment is possible. Values of $1/\alpha$ may then be regarded as lower limits. For the Washington latitudes, $\epsilon^{-1} = 2\cdot 9$ , and corrected values have been included in table 10.1.

$\dagger$ See also footnote on p. 174.

Table 10.1. Parameters of Chandler Wobble.   

<table><tr><td>Interval</td><td>r</td><td>f0-1Years</td><td>α-1Years</td><td>S+(0°01)3/c/year</td><td>Chandler Power (0°01)a</td><td>Q</td></tr><tr><td colspan="7">ILS values smoothed by Kulikov; power spectrum according to Rudnick, 1956.*</td></tr><tr><td>1891 to 1945</td><td>1 to 544</td><td>1·193 ± 0·011</td><td>11·4 (+ 5·3, - 4·2)</td><td>0·58 (+ 0·25, - 0·16)</td><td>96</td><td>30</td></tr><tr><td colspan="7">Unsmoothed ILS values: smoothed spectrum for even and odd harmonics, respectively.</td></tr><tr><td>even 1899 to 1954</td><td>1 to 480</td><td>1·183 ± 0·013</td><td>11·4 (+ 5·6, - 4·7)</td><td>0·86 (+ 0·45, - 0·27)</td><td>143</td><td>30</td></tr><tr><td>odd 1899 to 1954</td><td>1 to 480</td><td>1·178 ± 0·008</td><td>22·4 (+ 11·1, - 8·7)</td><td>0·61 (+ 0·31, - 0·18)</td><td>196</td><td>60</td></tr><tr><td colspan="7">Washington latitudes: smoothed spectrum.</td></tr><tr><td>1916 to 1952</td><td>1 to 360</td><td>1·183 ± 0·016</td><td>6·7 (+ 3·1, - 2·7)</td><td>1·02 (+ 0·41, - 0·27)</td><td>99</td><td>18</td></tr><tr><td>adjusted according to (10.1.11)</td><td></td><td></td><td>8·4 (+ 3·8, - 3·4)</td><td>0·76 (+ 0·31, - 0·20)</td><td></td><td>23</td></tr><tr><td colspan="7">Smoothed ILS values: according to Jeffreys, 1952.</td></tr><tr><td>1908 to 1921</td><td>0, 3, 6</td><td>1·202 ± 0·016</td><td>15·2 ± 1·6</td><td></td><td></td><td>40</td></tr><tr><td colspan="7">Unsmoothed ILS values, according to Walker and Young, 1957.</td></tr><tr><td rowspan="3">1899 to 1954</td><td>1, 2</td><td>1·287 ± 0·26</td><td>2·27 ± 0·49</td><td></td><td></td><td>6</td></tr><tr><td>1 to 16</td><td>1·198</td><td></td><td></td><td></td><td></td></tr><tr><td>6 to 16</td><td>1·179</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">1900 to 1934</td><td>1, 2</td><td>1·267 ± 0·041</td><td>2·81 ± 0·86</td><td></td><td></td><td>7</td></tr><tr><td>1 to 16</td><td>1·202</td><td></td><td></td><td></td><td></td></tr><tr><td>6 to 16</td><td>1·186</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">1900 to 1920</td><td>1, 2</td><td>1·238 ± 0·033</td><td>4·18 ± 1·94</td><td></td><td></td><td>11</td></tr><tr><td>1 to 16</td><td>1·201</td><td></td><td></td><td></td><td></td></tr><tr><td>6 to 16</td><td>1·193</td><td></td><td></td><td></td><td></td></tr></table>

* A noise level of 0·06 (0'01) has been subtracted prior to fitting the spectrum.

The analysis by Jeffreys (1940) and by Walker and Young (1955, 1957) is closely related to the present analysis. Rudnick infers the power spectrum of the stationary series from the power spectrum of the 54-year sample. This inference consists essentially of smoothing the ragged spectrum with due regard to the large relative variance of any one spectral line.* Jeffreys, Walker and Young compute autocorrelation values and fit them by a smooth curve. The power spectrum is fitted by a curve of the type (10.1.7), the autocorrelation by (10.1.6). These are consistent choices, both following directly from the assumption of a complex frequency, $\sigma_0$ , of the Chandler wobble.

If there were ample data, the two methods would converge to the same damping time $\alpha^{-1}$ . With a limited sample, Rudnick's (1953) work suggests the sampling error in the methods is comparable provided all possible lags are used in the autocorrelation. Using less than the complete autocorrelation leads to inferior results, according to Rudnick.

Table 10.1 summarizes results for various choices of lags $r$ . Rudnick's and our results correspond to the use of all possible lags. Jeffreys's work is based essentially on a least-square fit to the autocorrelation $R(r)$ for $r = 0, 3, 6$ (unit lag is 0-1 years); this gave a period of $14\frac{1}{2}$ months and a damping time of 15 years. In their 1955 paper, Walker and Young used $R(r)$ for $r = 1, 2$ (unit lag is 1 month). They obtained periods of 15 to $15\frac{1}{2}$ months and damping times of 2-3 to 4-2 years. These results did not appear to be reasonable. In their 1957 paper the authors chose a least-square fit for $r = 1$ to 16, and $r = 6$ to 16. The results differ from one era to the next.

The consistent values are obtained for 1900 to 1920 using the largest values of $r$ , and the authors consider 1-193 years to be their best estimate of the Chandler period. This is now in excellent accord with Jeffreys's value of 1-202 years and Rudnick's value of 1-193 years. With regard to the damping time the authors permit themselves

* Jeffreys has expressed some concern regarding the validity of harmonic analysis applied to latitude observations, and this has been amplified by Walker and Young. One must interpret Jeffreys's remarks concerning harmonic analysis as applying to the search for physically significant spectral lines (with stable phase). The Fourier line spectrum as a device for estimating the continuous power spectrum is without implication of the physical meaning of any one line.

only the conclusion that it is between 10 and 30 years; Jeffreys found 15 years and Rudnick 11 years.

Gutenberg (1956) has expressed some doubt that the damping times should be anywhere near as short as 10 periods. He suggests that it is not possible to discriminate the effect of damping from the beat phenomenon between the Chandler wobble and the annual term. But in the power spectrum the annual line falls outside the broadened peak of the Chandler wobble, so that the two spectral features are adequately resolved.

Melchior (1957, p. 234) has drawn attention to the fact that the autoregression schemes followed by Walker and Young 'imply the existence of a mathematical relation between the idea of elasticity (represented by the Chandlerian period) and that of viscosity (represented by the damping), and this relation is just Maxwell's law'. The curve-fitting procedure used by Walker and Young and by Rudnick implies only a complex frequency; this in turn implies only a damped linear system. The Maxwell body is just one of an infinite number of possible linear combinations of springs and dashpots. Moreover, the curve fitting is not sufficiently definitive to favor the linear models over other types; all that can be said is that the linear models cannot be excluded by the data. But even for nonlinear models the parameters in table 10.1 retain much of their significance, with $Q$ designating some appropriately defined width of the spectrum (\$ 4.3).

# 2. The concept of an instantaneous Chandler period

The literature refers to two types of models: we shall call them the 'damped model' and the 'time-variable model'. In the preceding section we have been concerned with the damped model (Jeffreys, Walker and Young, Rudnick). The finite spectral width (or some equivalent feature) is associated with the damping of a tuned oscillator excited at random. Imperfections from elasticity in the Earth's mantle would give rise to such damping, as would the dissipation at the boundary between mantle and core if the core is viscous.

The majority of papers dealing with the Chandler wobble report that its period varies with time and that this implies corresponding

variations of the pertinent physical parameters (rigidity, ellipticity, etc.). The authors include Chandler himself, Kimura, Berg, Backlund, Wahl, Stumpff, Witting, Ledersteger, Hattori, Nicolini and Melchior. The variable period is connected to a variable amplitude according to empirical laws formulated by Melchior (1957) and based largely on his work and that of Nicolini:

(1) The period of the Chandler motion fluctuates. The maximum departure from the mean value is approximately $\pm 4$ per cent.   
(2) Period and amplitude of the Chandler motion are proportional. The correlation coefficient, according to Nicolini, is $+0.88$ .   
(3) A long Chandler period is correlated with a small amplitude of the annual motion.

The difference in the interpretation as characterized by the damped and time-variable models centers on the meaning of 'period' and the method whereby this is obtained from the record. Instantaneous period (or its inverse, the instantaneous frequency IF) can be determined from the time interval between alternate zero crossings in a record from which the annual term has been removed by suitable means. Similarly, instantaneous amplitude (IA) is the height of a peak above the record mean. The instantaneous values reported in the literature have been obtained by some such method.

Fourier frequencies (FF), on the other hand, are obtained by representing a record as a sum (or integral) of harmonic functions. The power spectrum of wobble (fig. 10.2) is an example of the application of FF. Here the power in the Chandler wobble is expressed as a sum of roughly nine values corresponding to various FF. It is in the nature of FF analysis that these values are fixed for any given record. Instantaneous values vary with time throughout the record.

Reasonably well-behaved oscillatory records can perfectly well be described in terms of IF and IA. FF likewise are a satisfactory means for describing wiggly records of stationary processes. IF and FF are not the same, but with some precaution they can be related. In general, the broader the peak (the smaller the $Q$ ) in an FF presentation, the larger will be the fluctuation of the IF throughout the record. The reported fluctuation of the Chandler frequency by as

much as $\pm 4$ per cent is roughly consistent with the $Q$ of 25 derived from the FF.*

Melchior finds support for the time-variable model from the third empirical law. His argument involves the wobble equation (6.3.6). But this equation was derived with the explicit understanding that $\sigma_0$ does not vary in time. Melchior's hypothesis of a slightly damped time-variable model does permit him to apply the steady state results by replacing $\sigma_0$ with $\sigma_0(t)$ , provided the time variation of $\sigma_0$ is slow compared to the damping time $\alpha^{-1}$ . The observed variations are rapid and therefore beyond the scope of his parametric treatment. Reducing the damping only increases the time required to reach equilibrium and does not help at all. Melchior is entitled to contemplate such rapid changes in the time-dependent parameters that might account for the fluctuations in IF, but he has not given the argument for the expected performance of his model.

The situation may be summarized as follows: The reported fluctuation in IF (empirical law 1) is in harmony with the results obtained from spectral analysis (or equivalent methods based on autocorrelation). The fluctuation in IF then does not favor the time-variable model over the linear damped oscillator. Empirical laws 2 and 3 have not been accounted for in terms of either model. Physical considerations speak against the time-variable model†: there has been no evidence of the remarkable physical changes that must accompany a change in the Chandler period by $\pm 4$ per cent.

* The distribution of the interval, $\tau$ , between alternate zero crossings for a narrow spectrum formed by a Gaussian noise has been discussed by Longuet-Higgins (1958). Let

$$
\mu_ {n} = \int_ {- \infty} ^ {\infty} f ^ {*} S (f) d f
$$

designate the $n$ th moment of the power spectrum, $S(f)$ . The mean interval, $\overline{\tau}$ , is approximately $\mu_0 / \mu_1$ . Half the values of $\tau$ lie within the range

$$
\bar {\tau} \left(1 - \frac {2}{\sqrt {3}} \delta\right) \quad \text {t o} \quad \bar {\tau} \left(1 + \frac {2}{\sqrt {3}} \delta\right)
$$

where

is assumed small. For the spectral function (10.1.7) $\overline{\tau} = f_0^{-1}$ , as expected. For this particular function, $\mu_{\mathfrak{g}}$ and hence $\delta$ are infinite, and the approximations do not apply. But it will be noted that $\delta$ is essentially the root-mean-square width of the spectrum and can be expected to have a value near $Q^{-1}$ , or 0·02 to 0·10. Departures in instantaneous period by 4 per cent, as reported, are not unexpected.

† See Newcomb's criticism of Chandler, § 7.1.

We prefer the linear damped model because it is simple and adequate and because we have found no compelling reasons for abandoning it in favor of the more complicated time-variable model.

# 3. Tidal-effective rigidity and viscosity

On the basis of table 10.1 we adopt

$$
f _ {0} ^ {- 1} = 1 \cdot 1 9 5 \pm 0 \cdot 0 1 5 \text {y e a r s} \tag {10.3.1}
$$

as an estimate for the period of the Chandler wobble. The tidal-effective Love number is then

$$
k = 0 \cdot 2 9 \pm 0 \cdot 0 1 \tag {10.3.2}
$$

according to (6.2.5). A comparison of the value to Takeuchi's estimate is given in § 10.8. For the equivalent Earth model (§ 5.6) the tidal-effective rigidities (dimensionless and dimensional) then follow from (5.6.1, 2):

$$
\mu = 2 \cdot 3 1 \pm 0 \cdot 1 0, \quad \tilde {\mu} = (8 \cdot 3 5 \pm 0 \cdot 3 6) \times 1 0 ^ {1 1} \text {d y n e s} \mathrm {c m} ^ {- 2}. \tag {10.3.3}
$$

The rigidity of steel is 8 to $9 \times 10^{11}$ dynes $\mathrm{cm}^{-2}$ .

The complex frequency, $\sigma_0 = \sigma_0 + i\alpha$ , implies a complex Love number

$$
\mathbf {k} = k \left(1 - i \frac {\mu}{2 Q}\right) \tag {10.3.4}
$$

according to (6.2.5) and (5.6.2). For a Maxwell body (5.11.5)

$$
\mathbf {k} = k \left(1 - i \frac {\mu}{1 + \mu} \frac {\tilde {\mu}}{\sigma_ {0} \tilde {\eta} _ {M}}\right) \tag {10.3.5}
$$

provided $(\tilde{\mu} / \sigma_0 \tilde{\eta}_M)$ is a small quantity. Equating imaginary parts and using (10.1.9) and (5.11.3) we obtain

$$
\tilde {\eta} _ {M} = \frac {2 Q \tilde {\mu}}{(1 + \mu) \sigma_ {0}}, \alpha^ {- 1} = (1 + \mu) \tau \qquad \qquad (1 0. 3. 6)
$$

where $\tau = \tilde{\eta}_M / \tilde{\mu}$ is the characteristic time. For $Q = 30$ , the tidal-effective viscosity $\tilde{\eta}_M$ is $10^{20} \, \text{g cm}^{-1} \, \text{sec}^{-1}$ , and the damping time $\alpha^{-1} = 13$ years.

This interpretation of the damping cannot be reconciled with the

time constant of isostatic adjustment. For a homogeneous Maxwell Earth the load operators are (5.8.4, 5.11.3, 5.7.2)

$$
\widehat {k _ {n} ^ {\prime}} = - \frac {1}{1 + N \hat {\mu}}, \quad \hat {\mu} = \frac {\mu \hat {D}}{\hat {D} + \tau^ {- 1}}, \quad N = \frac {2 (2 n ^ {2} + 4 n + 3)}{1 9 n}. \tag {5.7.2}
$$

A load suddenly applied at time 0 is reduced by deformation according to

$$
(1 + \widehat {k _ {n} ^ {\prime}}) H (t) = \frac {N \mu}{1 + N \mu} \frac {\widehat {D}}{\widehat {D} + \gamma_ {n}} H (t) = \frac {N \mu}{1 + N \mu} e ^ {- \gamma_ {n} t}, \tag {10.3.7}
$$

where $\gamma_{n}^{-1} = (1 + N\mu)\tau$ (10.3.8)

is the compensation time. The operational solution follows the rules given by Jeffreys and Jeffreys (1950, 7-051). The factor $N\mu / (1 + N\mu)$ accounts for the immediate effect due to elastic deformation.

For a load of degree 2, $N = 1$ and

$$
\gamma_ {2} ^ {- 1} = (1 + \mu) \tau = \alpha^ {- 1};
$$

hence the compensation time equals the damping time of the Chandler wobble, 13 years. For higher order loads, the compensation times are somewhat longer: $\gamma_{10}^{-1} = 90$ years and $\gamma_{30}^{-1} = 300$ years. But gravity anomalies associated with ancient geologic structures of limited horizontal extent indicate adjustment times of millions of years! The foregoing application of the Maxwell body is intended for illustration only with no implication that it can serve as a meaningful model for the real Earth.

An equally absurd model is that of a Kelvin-Voigt body. From (5.11.3) we can write

$$
\mathbf {k} = k \left(1 - i \frac {\mu}{1 + \mu} \frac {\sigma_ {0} \tilde {\eta} _ {K - V}}{\tilde {\mu}}\right) \tag {10.3.9}
$$

where $\sigma_0\tilde{\eta}_{K - V} / \tilde{\mu}$ is a small quantity. Equating imaginary parts of (10.3.9) and (10.3.4)

$$
\tilde {\eta} _ {K - V} = \frac {(1 + \mu) \tilde {\mu}}{2 Q \sigma_ {0}}, \quad \alpha^ {- 1} = \frac {(1 + \mu) \tilde {\mu}}{\sigma_ {0} ^ {2} \tilde {\eta} _ {K - V}}. \tag {10.3.10}
$$

For $Q = 30$ , the viscosity is $2 \cdot 6 \times 10^{17} \, \text{g cm}^{-1} \, \text{sec}^{-1}$ . Knopoff and MacDonald (1958) show that a Kelvin-Voigt viscosity greater than $10 \, \text{g cm}^{-1} \, \text{sec}^{-1}$ is inconsistent with the observed damping of seismic waves. The Kelvin-Voigt model fails at high frequencies, the Maxwell

model at low frequencies. The shortcomings of these two models have been discussed by Jeffreys (1917) and by Birch and Bancroft (1942).

# 4. Pole tide and Love numbers

'The sea would be set into vibration, one ocean up and another down. . . .' In these words Lord Kelvin* suggested that a wobble would induce an ocean tide. Kelvin overlooked the fact that such a tide would appreciably lengthen the wobble period leaving aside for the moment any effect of the Earth's elastic deformation; otherwise he would not have confined his search to the Eulerian period of ten months (§ 7.1).

The derivation of the equilibrium pole tide and its effect on wobble follows in a straightforward fashion from the equations already derived (see Federov, 1949; Haubrich and Munk, 1959). The equations of motion of the rotation pole are (6.3.5)

$$
\frac {\mathrm {d} \mathbf {m}}{\mathrm {d} t} - i \sigma_ {e} \mathbf {m} = - i \sigma_ {r} \boldsymbol {\phi}, \tag {10.4.1}
$$

where $\phi = \frac{c_{13} + ic_{23}}{C - A} = -\frac{a^4\rho_w\int\xi\sin\theta\cos\theta\mathrm{e}^{i\lambda}\mathrm{d}s}{C - A}$ (10.4.2)

is the excitation pole arising from the products of inertia of the pole tide, $\xi (\theta ,\lambda ;t)$ , $\rho_{w}$ is the density of sea water, and $\sigma_{e}$ is the 'elastic wobble frequency' (as if the ocean were frozen). The solution to (10.4.1) will yield the observed frequency $\sigma_0$

The equilibrium pole tide equals $(1 + k - h)U / g$ , where

$$
\begin{array}{l} U = - \omega_ {1} \omega_ {3} x _ {1} x _ {3} - \omega_ {2} \omega_ {3} x _ {2} x _ {3} \\ = - \Omega^ {2} a ^ {2} \sin \theta \cos \theta (m _ {1} \cos \lambda + m _ {2} \sin \lambda) \\ \end{array}
$$

is the potential produced by the wobble. To this we must add the Darwin correction (§ 9.2) in order to assure that ocean mass is conserved. When this is done, the resultant tide can be written

$$
\begin{array}{l} \xi = - \frac {1 + k - h}{g} \frac {\Omega^ {2} a ^ {2}}{2} \\ \times \left\{m _ {1} \left(\sin 2 \theta \cos \lambda - \frac {a _ {2} ^ {1}}{5 a _ {0} ^ {0}}\right) + m _ {2} \left(\sin 2 \theta \sin \lambda - \frac {b _ {2} ^ {1}}{5 a _ {0} ^ {0}}\right) \right\} \tag {10.4.3} \\ \end{array}
$$

* Presidential Address, 1876, Section of Mathematics and Physics, British Association for the Advancement of Science.

where $a_{n}^{m}, b_{n}^{m}$ are the coefficients of $\mathcal{C}$ (oceans) (see §A.1). Combining (10.4.1-3), the equations of motion are put in the form

$$
\left. \begin{array}{l} \frac {\mathrm {d} m _ {1}}{\mathrm {d} t} + \left(\sigma_ {e} - T _ {2} \Omega\right) m _ {2} - R \Omega m _ {1} = 0 \\ \frac {\mathrm {d} m _ {2}}{\mathrm {d} t} - \left(\sigma_ {e} - T _ {1} \Omega\right) m _ {1} + R \Omega m _ {2} = 0 \end{array} \right\} \tag {10.4.4}
$$

where

$$
\frac {R}{1 + k - h} = \frac {4 \pi \Omega^ {2} \rho_ {w} a ^ {6}}{A g} \left[ \frac {b _ {2} ^ {2}}{3 5} + \frac {b _ {4} ^ {2}}{6 3} - \frac {a _ {2} ^ {1} b _ {2} ^ {1}}{1 0 0 a _ {0} ^ {0}} \right] = - 0. 1 1 \times 1 0 ^ {- 4}
$$

$$
\begin{array}{l} \frac {T _ {1}}{1 + k - h} = \frac {4 \pi \Omega^ {2} \rho_ {w} a ^ {6}}{A g} \\ \times \left[ \left(\frac {a _ {0} ^ {0}}{1 5} + \frac {a _ {2} ^ {0}}{1 0 5} - \frac {4 a _ {4} ^ {0}}{3 1 5}\right) + \left(\frac {a _ {2} ^ {2}}{3 5} + \frac {a _ {4} ^ {2}}{6 3}\right) - \frac {(a _ {2} ^ {1}) ^ {2}}{1 0 0 a _ {0} ^ {0}} \right] = 3 \cdot 3 6 \times 1 0 ^ {- 4} \\ \end{array}
$$

$$
\begin{array}{l} \frac {T _ {2}}{1 + k - h} = \frac {4 \pi \Omega^ {2} \rho_ {w} a ^ {6}}{A g} \\ \times \left[ \left(\frac {a _ {0} ^ {0}}{1 5} + \frac {a _ {2} ^ {0}}{1 0 5} - \frac {4 a _ {4} ^ {0}}{3 1 5}\right) + \left(\frac {a _ {2} ^ {2}}{3 5} + \frac {a _ {4} ^ {2}}{6 3}\right) - \frac {(b _ {2} ^ {1}) ^ {2}}{1 0 0 a _ {0 .} ^ {0}} \right] = 2 \cdot 1 6 \times 1 0 ^ {- 4} \\ \end{array}
$$

The solutions are

$$
m _ {1} = M _ {1} \cos \sigma_ {0} t, \quad m _ {2} = M _ {2} \sin \left(\sigma_ {0} t + \beta\right) \tag {10.4.5}
$$

provided $\sigma_0^2 = \sigma_e^2 -(T_1 + T_2)\Omega \sigma_e - (R^2 -T_1T_2)\Omega^2,$ (10.4.6)

$$
\tan \beta = \frac {\Omega R}{\sigma_ {0}}, \quad \frac {M _ {1} ^ {2}}{M _ {2} ^ {2}} = \frac {\sigma_ {e} - T _ {2} \Omega}{\sigma_ {e} - T _ {1} \Omega}. \tag {10.4.7}
$$

Thus the frequency has been diminished from $\sigma_{e}$ to $\sigma_0$ according to (10.4.6). Inasmuch as $R\ll T_1,T_2$ , this can be written

$$
\sigma_ {0} \approx \sigma_ {e} - \frac {1}{2} \left(T _ {1} + T _ {2}\right) \Omega + 0 \left(T _ {2} \Omega / \sigma_ {e}\right) ^ {2}. \tag {10.4.8}
$$

The observed frequency is $\sigma_0 = \Omega / 437$ . For the usually accepted values of Love numbers, $1 + k - h = 0.68$ , and this gives $\sigma_{e} = \Omega / 404$ so that the oceans increase the period from 404 days to 437 days.* Without oceans, the annual term would be about half as far from resonance as it is now, and the annual wobble twice as large.

* The dominant coefficient in the expression for $T_{1} + T_{3}$ is $a_{0}^{0}$ . The decrease in frequency depends therefore to a first order on the fraction of the Earth's surface covered by oceans. This was noted by Larmor (1896) who first evaluated this effect.

But we are not concerned with the nutation frequency, $\sigma_{e}$ , of an Earth without oceans but rather with the 'elastic tidal-effective Love number', $k_{e}$ , that would be applicable under these conditions. In analogy with

$$
\sigma_ {0} = \sigma_ {r} \frac {k _ {f} - k}{k _ {f}} \tag {6.2.5}
$$

we write $\sigma_{e} = \sigma_{r}\frac{k_{f} - k_{e}}{k_{f}}.$ (10.4.9)

Equation (10.4.8) can then be written in either of the forms

$$
\sigma_ {0} = \sigma_ {e} - \frac {k _ {w}}{k _ {f}} \sigma_ {r}, \quad k = k _ {e} + k _ {w}, \tag {10.4.10}
$$

provided we define $k_{w}$ by

$$
k _ {w} = \frac {1}{2} k _ {f} \left(T _ {1} + T _ {2}\right) \frac {\Omega}{\sigma_ {r}} = \frac {9}{8 \pi} (1 + k - h) S \frac {\rho_ {w}}{\bar {\rho}}, \tag {10.4.11}
$$

where $\bar{\rho}$ is the mean density of the Earth, and

$$
S = \frac {8 \pi}{1 5} \left(a _ {0} ^ {0} + \frac {1}{7} a _ {2} ^ {0} - \frac {4}{2 1} a _ {4} ^ {0}\right) - \frac {4 \pi}{1 0 0 a _ {0} ^ {0}} [ (a _ {2} ^ {1}) ^ {2} + (b _ {2} ^ {1}) ^ {2} ] = 1 \cdot 2 0.
$$

Thus $k_{\omega}$ is that part of the Love number $k$ which is due to the oceanic pole tide.

The problem is to evaluate $k_{\theta}$ . We may regard $k = 0 \cdot 29$ as known from the frequency of the Chandler wobble. There are two procedures: (1) we regard $h = 0 \cdot 61$ as given, then it follows from (10.4.10) and (10.4.11) that

$$
\left(\Omega / \sigma_ {e}\right) = 4 0 4, \quad h = 0 \cdot 6 1 0, \quad k _ {e} = 0 \cdot 2 3 5, \quad k _ {w} = 0 \cdot 0 5 5; \tag {10.4.12}
$$

(2) for an 'equivalent' Earth (§ 5.6) the ratio $h_e / k_e$ depends only on the density distribution, not on the rigidity. Then

$$
\frac {h _ {e}}{k _ {e}} = \frac {h _ {f}}{k _ {f}} = 2. 0 5, \tag {10.4.13}
$$

where $h_{e}U / g$ is the elastic deformation of the solid Earth, and $k_{e}U / g$ the potential of this deformation. For the case of no load $h = h_{e}$ . We now obtain

$$
\left(\Omega / \sigma_ {e}\right) = 3 9 6, \quad h = 0. 4 5 7, \quad k _ {e} = 0. 2 2 3, \quad k _ {w} = 0. 0 6 9, \tag {10.4.14}
$$

which differs from (10.4.12) chiefly with regard to $h$ .

The principal result is that the tidal-effective Love number is reduced from 0·29 to approximately 0·22 after allowing for an equilibrium response of the oceans. The results are not appreciably altered by a first-order correction for load deformation (Haubrich and Munk, 1959). A complete treatment along the lines of (\$ 5.12) has not been attempted.

The asymptotic behavior is as expected. For $\rho_{w} = 0$ we have $k_{w} = 0$ and $\sigma_0 = \sigma_e$ , which is the appropriate frequency for an Earth without oceans. For a rigid Earth ( $k_{e} = 0$ , $h = 0$ ) completely surrounded by oceans, $S = 8\pi /15$ , and

$$
k _ {w} = k = \frac {1}{\frac {5}{3} \frac {\bar {\rho}}{\rho_ {w}} - 1}, \sigma_ {0} = \sigma_ {r} \left(1 - \frac {k}{k _ {f}}\right).
$$

For a homogeneous Earth, $k_{f} = 3 / 2$ (§ 5.4). Thus as the ocean density approaches that of the Earth, $\rho_{w} \rightarrow \bar{\rho}$ , we find that $\sigma_{0} \rightarrow 0$ : the rotational axis becomes unstable. For the actual density distribution $k_{f} = 0.96$ so that instability is reached when $\rho_{w} = 4.5 \, \text{g cm}^{-3}$ .

The foregoing calculations emphasize the large effect of a pole tide on the Chandler wobble, provided the tide is given by the equilibrium theory. But there is a question whether the equilibrium theory applies. Even if the equilibrium theory is adequate for $p_{2}^{0}$ tides of relatively short period, such as the fortnightly, monthly, semi-annual and annual tides, this does not necessarily constitute an argument for the equilibrium response to the $p_{2}^{1}$ potential of the pole tide. Indeed, the work of Jeffreys and Vicente on the dynamics of a fluid core shows that the equilibrium theory is not applicable to the core (even though these authors use an equilibrium correction for the ocean).

Studies of the diurnal tide (also due to a $p_2^1$ potential) come closest, but these are usually restricted at the start to the assumption of a diurnal frequency. The problem is closely connected to the possibility of steady (zero frequency) motion of the $p_2^1$ types. Laplace shows that for an ocean of constant depth covering the whole Earth there is no diurnal tide (Lamb, 1932, p. 342). Under these conditions, the pole tide would be insignificant compared to the equilibrium response unless the boundary layer associated with the viscous flow

along the sea bottom has a thickness comparable to the depth of the ocean.

Under actual conditions, the pole tide is superimposed upon other motion, vastly larger, and this increases the frictional coupling between oceans and earth. Let $u$ designate the water velocity associated with the pole tide, $U$ the maximum speed of a short-period tidal current, and $h$ the water depth. The frictional force per unit mass can be written $\gamma u$ , where

$$
\gamma = \frac {4}{\pi} (0 \cdot 0 0 2 5) \frac {U}{h}
$$

according to Bowden (1953). Proudmans personal communication) has suggested that the equilibrium assumption depends on the smallness of the ratio $f_0 / \gamma$ (see Proudmans, 1916). Setting $h = 4\mathrm{km}$ $U = 6\mathrm{cm}\sec^{-1}$ gives $2\pi /\gamma = 1540$ days which is not small compared to $f_0^{-1} = 435$ days. But in regions with very large tidal currents equilibrium conditions might be approached.

For oceans of constant depth bounded by parallels of latitude (including a polar ocean), Goldsbrough (1913, 1914) demonstrates the possibility of resonance at periods of the same order as that of the Chandler wobble. In the case of meridional boundaries such long-period resonances are not possible (Colborn, 1931), provided the boundaries are vertical. Proudmans (1913) work indicates that these results would not necessarily apply to the case of an ocean shelving gradually.

Thus theoretical considerations have not yet settled the applicability of equilibrium theory to the pole tide. Can observations provide a clue?

Tide records are read hourly to an accuracy of perhaps $\pm 1$ cm. A typical amplitude of the equilibrium pole tide is $\frac{1}{2}$ cm.* Searching for the pole tide is then a marginal undertaking, even if we allow for the fact that the analysis is based on monthly averages of hourly readings. There have been a number of attempts: Christie (1900);

* This would be the value at $\theta = 45^\circ$ for a wobble of $0^{\prime \prime}14$ amplitude, according to (10.4.3). A rough estimate can be made from the following elementary considerations. The polar radius is shorter by $20\mathrm{km}$ than the equatorial radius, thus giving an average 'slope' of $20\mathrm{km}$ in $10,000\mathrm{km}$ , or $1:500$ . If the Earth were rigid and the pole moved towards a fixed observer by $0^{\prime \prime}14 (= 14\mathrm{ft} = 430\mathrm{cm})$ , then the equilibrium sea-level would sink by $430 / 500 = 0.86\mathrm{cm}$ . To allow for self-attraction and elastic deformation of the Earth, multiply by $1 + k - h$ .

Bakhuyzen (1913) uncovered records of Amsterdam sea-level going back to 1700; Przbyllok (1919); Baussan (1951); Maximov (1956). The procedure has been to divide the data into as many 7-year series as possible and to derive for each of these by Fourier analysis the amplitude and phase of the sixth harmonic, corresponding exactly to a 14-month period. Haubrich and Munk (1959) have determined the power spectrum of sea-level for all tide stations that were in operation at the turn of the century. This involves no preconceived assumption as to the frequency of the pole tide and, furthermore, furnishes an estimate of the noise level at adjoining frequencies. This noise level is very high, so much so that previous investigators would have found the amplitude at 15 months or 13 months not much less than at 14 months.

Fig. 10.3 shows the average spectrum of 11 records (six Netherlands stations are combined into a single record). Seasonal terms were subtracted from the records before analysis. The most prominent peak between zero frequency and the annual frequency occurs at $0 \cdot 84$ c/year corresponding to a period of $1 \cdot 19$ years. This is in excellent agreement with the estimate $1 \cdot 195 \pm 0 \cdot 015$ based on latitude observations. For each station the equilibrium tide level was computed month by month alongside the recorded level, using the unsmoothed latitude observations (fig. 7.4) and allowing for latitude and longitude according to (10.4.3). The co-spectrum (or in-phase component) shows a positive maximum at the pertinent frequencies, whereas the quadrature spectrum (or out-of-phase component) has none. This is the expected result for an equilibrium tide, or an equilibrium tide multiplied by a positive constant. The features are weak, and the significance marginal.

But there are some unexpected results. Comparing areas under the spectral peak associated with the equilibrium tide, and that of the recorded tide (after subtracting a noise level of $10\mathrm{cm}^2/\mathrm{c}/\mathrm{year}$ ), the power of the recorded tide is found to be four times as large; hence its amplitude is twice the equilibrium amplitude. On further examination it is found that Swinemunde, the Netherlands group, Marseilles and Bombay contribute most of the power of this peak: furthermore, that the early Swinemunde tide record (1811 to 1906) does not reveal a corresponding peak. Perhaps the precision of automatically recording

tide gauges is essential. Measurements in the nineteenth century were conducted largely with tide poles, and these might be inadequate to measure pole tides.

![](images/f875e57c676f5aa672c73bac4233142b16f9502a1f5f91b06646a14fb6e00b16.jpg)

![](images/1db5ae350db33acb3d0309378794a9a57fddfe8deda6ada193fa41637b586d73.jpg)

![](images/8d36f68a62abe9ff10478a642f981020f50593a3c57b485c680f6fd28f94b2dd.jpg)  
Cycles per year   
Fig. 10.3. Upper diagram: The power spectra of sea-level (open circles) and of the equilibrium pole tide (solid circles), in $\mathrm{cm}^2/\mathrm{c}/\mathrm{year}$ . This is based on an average of 11 stations (six Netherland stations have been combined into one record) for the years 1900 to 1954. Lower curves show the normalized co-spectrum and quadrature spectrum. Dashed lines indicate the $95\%$ significance level.

The equilibrium spectrum is based on the value $1 + k - h = 0 \cdot 68$ . For the equivalent Earth model (10.4.13) we obtain $1 + k - h = 0 \cdot 84$ , and the discrepancy is then considerably reduced. But the essential thing is that the foregoing comparison is based on the equilibrium

argument, and there is no justification for this assumption. The pole tide observations do not support it.

The spectral peak of the recorded tide is far narrower than that of the equilibrium tide. The three-point peak is just the expected signature of a line spectrum (see A.2.5), or at least of a peak narrow compared to the resolution. On this basis we find

$$
Q > 1 0 0 \tag {10.4.15}
$$

as compared to $Q \approx 35$ from the latitude observations (table 10.1). This is a most surprising result. One might conceive that the oceans have a sharp resonance peak at just this frequency. But this would be a most unlikely coincidence and furthermore would involve a degree of resonance not otherwise found in oceanic oscillations.

There is always a very real concern as to whether the peak in the pole tide spectrum is significant. Following a suggestion by Tukey, Munk and Haubrich (1958) made an analysis of the variance along the following lines: Let $S_{fg}$ designate computed spectral densities at frequencies $f$ and stations $g$ . The following two regression schemes are fitted by the method of least squares:

(1) $S_{fg} = a_g + \sin^2\theta_g\cos^2\theta_g S_f^\prime$   
(2) $S_{f_0} = b_g + \sin^2\theta_g\cos^2\theta_gS_f^{\prime \prime \prime}$

Here $a_{g}, b_{g}$ is the noise level at station $g$ ; $\sin^2\theta_g\cos^2\theta_gS_f''$ is the equilibrium pole tide spectrum at station $g$ based on the observed latitude spectrum $S_f''$ ; $\sin^2\theta_g\cos^2\theta_gS_f'''$ is the equilibrium pole tide on the assumption of a spectral line at 0.84 c/year. For the combined stations, (1) gives a better fit than (2) but for the European stations the reverse holds. There is a hint here that the true spectral peak may be narrower than indicated by the latitude observations but much further work needs to be done to clarify the situation.

# 5. Ellipticity of the Chandler wobble

Larmor (1896) has pointed out that the pole tide imposes a slight ellipticity on the path described by the pole of rotation. The ellipticity equals

$$
\varepsilon = 1 - \frac {M _ {1}}{M _ {2}} = \frac {1}{2} \frac {\Omega}{\sigma_ {e}} \left(T _ {1} - T _ {2}\right) = 0. 0 1 7 \tag {10.5.1}
$$

with a major axis pointing toward $\lambda_0$ east longitude, where

$$
\tan 2 \lambda_ {0} = \frac {2 R}{T _ {1} - T _ {2}} = - 0. 2 0, \quad \lambda_ {0} = - 6 ^ {\circ}. \tag {10.5.2}
$$

For comparison, the ratio of amplitudes of $m_{1}$ and $m_{2}$ was taken from the analysis of the unsmoothed latitude data, 1899-1954. The result is

$$
\varepsilon = 0 \cdot 0 1 \pm 0 \cdot 0 5,
$$

and this is not inconsistent with the computed ellipticity. Fedorov (1949) has computed the ellipticity by a similar method and obtains $\varepsilon = 0\cdot 01$ . He states that this value does not agree with the observed ellipticity. Lambert (1922) attempted to evaluate the ellipticity from a number of six-year series of latitude observations, 1900-1917. His values of $\varepsilon$ range from 0 $\cdot$ 02 to 0 $\cdot$ 20, and the direction of the major axis from $59^{\circ}\mathrm{W}$ to $116^{\circ}\mathrm{W}$ .

An ellipticity of the pole path could be caused also by a difference in the equatorial moments of inertia. From geodetic measurements Helmert (1915) reported a difference of $230\mathrm{m}$ between the equatorial semi-axes. Let $A, B, C$ denote the principal moments of inertia. From Helmert's measurements Schweydar (1916) obtained

$$
\frac {B - A}{C + \frac {1}{2} (A + B)} = \frac {1}{4 6},
$$

which gives an ellipticity $\varepsilon = 0.016$ . Modern measurements have neither confirmed nor dismissed the degree of triaxiality proposed by Helmert.

# 6. Generation

An excitation, $\Psi(t)$ , which is not purely harmonic will excite resonance response. Any mobile part of the Earth is an obvious suspect. As usual it is easier to rule out causes than to confirm them.

There have been numerous attempts to link the variations in the Chandler wobble to earthquakes and volcanic eruptions (Cecchini, 1928, pp. 91-92). In particular, the increase in activity around 1907 (fig. 7.4) has been ascribed to the great San Francisco earthquake of 1906. Quantitative considerations rule out this possibility. Consider a block $100\mathrm{km}$ by $100\mathrm{km}$ in area and $30\mathrm{km}$ high, thus

extending from the bottom of the Earth's crust to the surface. The total mass, $m$ , is then of the order of $10^{21}$ g. The block is assumed to be under compression and to expand during the earthquake, so that the surface is lifted by an amount $h = 1$ meter. The excitation pole is then of the order (omitting latitude and longitude factors)

$$
\frac {m (a + h) ^ {2} - m a ^ {2}}{C - A} = \frac {2 m a h}{C - A} = 4 \cdot 6 \times 1 0 ^ {- 1 1} = 0 ^ {\prime} 0 0 0 0 1
$$

and the resulting wobble is of the same order. The observed wobble is of the order $0^{\circ}1$ . For horizontal (strike-slip fault) displacements the same formula applies, provided we interpret $h$ as the representative horizontal slip. Conceivably this might be $10\mathrm{m}$ and the dimensions of the block $1000\mathrm{km}$ by $100\mathrm{km}$ ; even so the effect is negligible compared to observed values.

The atmosphere provides a possible mechanism, as pointed out by Volterra (1895) and Jeffreys (1940). According to Jeffreys 'the distribution of air over the Earth's surface, though mainly periodic, is not strictly so; it does not accurately repeat itself every year. It is therefore possible that the free variation of latitude is maintained by the irregular variation of the products of inertia, superimposed on the mean annual variation.' The required amount of irregular variation turns out to be of the right order of magnitude, as pointed out by Rudnick (1956, p. 142).

For a first estimate we consider spike-like departures of $\Psi(t)$ from the normal seasonal variation. Suppose these have a duration $\tau$ short compared to 14-month. The solution (6.7.3) is applicable. For definiteness, set $\tau = \sigma_0^{-1} = 2\cdot 2$ months. The induced free wobble then has an amplitude of $\sigma_0\tau |\Psi| = |\Psi|$ . The observed increase in the free motion between 1906 and 1908 could have been generated by one such spike of amplitude $|\Psi| \approx 0^{\prime \prime}1$ . This is six times the amplitude of the annual excitation function! Spikes of this order of magnitude occurring at random intervals of a few decades would maintain the Chandler wobble at its observed level.

But spikes are an inefficient means of exciting wobble. For a quantitative estimate we suppose the annual excitation function to be modulated so that its amplitude is sometimes larger, sometimes smaller. The modulation is assumed to contain all frequencies less

than $0 \cdot 5$ c/year; for definiteness we choose a triangular modulation spectrum as shown by the dashed line in fig. 10.4 (top). The sum and difference frequencies between the annual line and the modulation produce an input spectrum consisting of the annual line plus triangular side bands between $1 \pm 0 \cdot 5$ c/year. According to table 10.1 the input spectrum has a power density of roughly $0 \cdot 6(0^{\prime \prime}01)^{2} / c$ /year at the Chandler frequency. With this value the area of the triangle

![](images/87274e82f4589d53bf8cd273dad8ee0366eb510b30de2670be357320057a53db.jpg)  
Fig. 10.4. Top: The input spectrum is schematically presented by an annual line plus triangular side bands, resulting from a modulation spectrum indicated by the dashed line. Middle: The power transmission of the Earth, peaked at the Chandler frequency, 0-85 c/year. Bottom: The power spectrum of the pole of rotation; this curve is the product of the upper two. Adapted from Rudnick, 1956.

equals $0 \cdot 43(0^{\prime}01)^{2}$ . This is the power in the side bands. The power of the annual excitation function for positive motion is $\frac{1}{2}(0^{\prime}0168)^{2} = 1 \cdot 4(0^{\prime}01)^{2}$ , according to Jeffreys's values for the modified excitation (table 9.2). The side-band power is then 30 per cent of the annual term, and the root-mean-square variations in amplitude are of the order of 50 per cent. The numerical values can be varied by changing the shape of the modulation spectrum, with the restraint that the input spectrum must pass through the point $S_{i}^{+}(0 \cdot 85) = 0 \cdot 6(0^{\prime}01)^{2} / c$ /year as indicated on the figure. The side-band energy might be reduced by a factor of two, but not more, if artificial modulation spectra are to be avoided. The required year-to-year variability in the annual excitation appears to be high, but not impossibly high.

So far the required input spectrum is based on the analysis of the latitude observations. If the evidence from the pole-tide analysis is pertinent, then the computed values of $\alpha$ are too large, and the required input spectra can be reduced accordingly. For a Chandler power the required input density varies as $\alpha$ (or $Q^{-1}$ ) according to (10.1, 12, 13); if $Q$ exceeds 100, then for the triangular modulation spectrum the side-band energy is less than 10 per cent, and the root-mean-square variations in amplitude are about 30 per cent.

The straightforward approach would be to evaluate the excitation function month by month from the geophysical data and to compute the spectral density at 0.85 c/year. A more direct method would be comparison with the latitude observations by way of (6.7.1).* An attempt in this direction (with indifferent results) has been undertaken by Cowan (1950).

The conclusion is that the irregular variations in the atmosphere are of the right order of magnitude to account for the observed magnitude of the Chandler wobble. For a $Q$ of 30 (as indicated by the latitude observations) the required atmospheric variations are somewhat larger than one would like; for a $Q$ of 100 (as indicated

* This has been done while this book was in press. Hassan (1960) has computed mean monthly values of $\psi_{i}(t)$ for the period 1873 to 1950 using station-level pressures from all available stations. The spectra of $\psi_{i}$ show a rise centered on the annual line, as expected, but nevertheless the spectral density near 0.85 c/year fails to account for the observed wobble by one to two orders of magnitude (Munk and Hassan, 1961). Nor do the cross-spectra between $m_{i}$ and $\psi_{i}$ indicate the expected phases. Apparently the atmosphere plays a minor role in the generation of the Chandler wobble, and our discussion must be modified accordingly.

by the pole tide) the values are more acceptable. Earthquakes are not a possible cause. Irregular motion in the core cannot be excluded (§ 11.12).

In closing we can estimate the amount of wobble if the resonance period were to be made coincident with the period of one year. As Lambert (1931, p. 97) has pointed out, the resonance frequency $\sigma_0 = [(C - A) / A]\Omega$ would have been higher by the required amount some hundreds of million years ago if the present rate of tidal retardation in $\Omega$ can be extrapolated into the past (§ 11.6). At peak amplification the wobble is $Q$ times $0^{\prime}0168$ as compared to an amplification $7 \times 0^{\prime}0168$ under present circumstances. Apparently the annual displacement of the pole will not exceed a few hundred feet under any circumstances.

# 7. Dissipation

The spectral analysis of latitude and tide observations lead to values of $Q$ for the Chandler wobble. The values of $Q$ give information regarding the dissipation of energy in the Earth at the Chandler frequency provided the apparent damping is not due to exciting impulses of a non-random kind. The identification of the energy sink is important to the problem of polar wandering. If the energy dissipates in the mantle, the resulting anelasticity may fix the timescale for secular shifts of the pole. If the oceans or core are responsible for the damping, no such statement is possible.

First we need to estimate the rate of energy dissipation. The kinetic energy of a rigid body freely wobbling about a mean axis, $x_{3}$ , is

$$
K = \frac {1}{2} \left(A \omega_ {1} ^ {2} + A \omega_ {2} ^ {2} + C \omega_ {3} ^ {2}\right);
$$

the kinetic energy of the rigid body in steady rotation, having the same angular momentum is

$$
K _ {0} = \frac {1}{2} \frac {1}{C} [ A ^ {2} (\omega_ {1} ^ {2} + \omega_ {2} ^ {2}) + C ^ {2} \omega_ {3} ^ {2} ].
$$

The time-varying part of the kinetic energy is then

$$
\Delta K = K - K _ {0} = \frac {1}{2} H A \Omega^ {2} \left(m _ {1} ^ {2} + m _ {2} ^ {2}\right). \tag {10.7.1}
$$

Since the Earth is not rigid, any calculation of the total energy

associated with the Chandler wobble must include the elastic energy of deformation plus the potential energy resulting from the redistribution of mass. If the Earth were perfectly elastic, then the mean kinetic energy equals the mean of the sum of the elastic and potential energies. The energy is not exactly equipartitioned if dissipation is present in the system. The energy dissipated per cycle is $2\pi /Q$ times the peak energy. To terms in order $Q^{-1}$ , the kinetic energy of the wobble equals the potential and elastic energies,

$$
\Delta K = \Delta P + \Delta U + 0 (\Delta K / Q),
$$

and to a similar degree of approximation the total energy involved in the wobble is twice the mean kinetic energy.

For a root-mean-square amplitude of $0^{\prime}14$ , we obtain

$$
2 \Delta K = 8 \times 1 0 ^ {2 1} \operatorname {e r g s} = 4 \times 1 0 ^ {- 1 5} K \tag {10.7.2}
$$

for the mean energy of the Chandler wobble, and

$$
2 \Delta K \sigma_ {0} Q ^ {- 1} = 1 0 ^ {1 5} Q ^ {- 1} \operatorname {e r g s} \sec^ {- 1} \tag {10.7.3}
$$

for the mean rate of energy dissipation. This is very small compared to $3 \times 10^{19}$ ergs sec $^{-1}$ dissipated by tides (§ 11.6), or to $2 \cdot 5 \times 10^{20}$ ergs sec $^{-1}$ flowing out from the Earth due largely to radioactivity.

The interpretation of the damping of the Chandler wobble has had a long and complex history. Jeffreys (1916a) at first attributed the damping to tidal friction in the oceans. In a later paper, Jeffreys (1949) thought tidal friction to be inadequate and suggested elastic afterworking of the mantle as a suitable energy sink. This raised some problems in the interpretation of seismic data. Jeffreys in the third edition of The Earth added the core as a possible energy sink. Bondi and Gold (1955) dismiss the core and the oceans since in their model neither has a sufficient moment of inertia to affect the mantle. Jeffreys (1956) accepts the argument by Bondi and Gold and refers the damping back to the mantle. The problem is apparently closed but we wish to reopen it.

The wobble will tend to set up motions in the ocean and in the core, and indeed the ocean tide has been observed. Any friction at the bottom of the ocean or at the core-mantle boundary will oppose the motion of the solid Earth shifting in response to the wobble

of the instantaneous axis of rotation. For the case of an excitation due entirely to a torque $L_{i}$ , the equations of motion (6.1.2, 3) are

$$
\frac {\dot {m} _ {1}}{\sigma_ {r}} + m _ {2} = \frac {L _ {1}}{\Omega^ {2} (C - A)}, \quad \frac {\dot {m} _ {2}}{\sigma_ {r}} - m _ {1} = \frac {L _ {2}}{\Omega^ {2} (C - A)}, \quad \dot {m} _ {3} = \frac {L _ {3}}{C \Omega}.
$$

The approach followed by Bondi and Gold consists essentially of setting $L_{i} \sim -m_{i}$ : the frictional torque is taken about the instantaneous rotation axis. But this is not the only choice. We shall set $L_{i} \sim \varepsilon_{ijk} m_{j} (\mathrm{dm}_{k} / \mathrm{dt})$ : the frictional torque acts about an axis perpendicular to the plane defined by the instantaneous rotation axis and the vector $\mathrm{dm}_{k} / \mathrm{dt}$ , and directly opposes the motion of the solid Earth shifting in response to the wobble of the instantaneous axis. The frictional torque is then about an axis perpendicular to that taken by Bondi and Gold. The model explicitly recognizes that the wobble induces meridional motion, whereas Bondi and Gold's torque can only result from zonal motion about the instantaneous rotation axis.*

The wobble equations can now be written

$$
\frac {\dot {m} _ {1}}{\sigma_ {r}} + m _ {2} = \lambda (m _ {2} \dot {m} _ {3} - \dot {m} _ {2}) \approx - \lambda \dot {m} _ {2}, \quad \frac {\dot {m} _ {2}}{\sigma_ {r}} - m _ {1} \approx \lambda \dot {m} _ {1}, \quad (1 0. 7. 4)
$$

where $\lambda$ is a constant characterizing the frictional interaction. The solution

$$
\mathbf {m} = \mathbf {M} \exp [ (- \lambda + i) \sigma_ {r} t ]
$$

is a typically damped oscillation. For vanishingly small frictional interaction $\dot{m}_1\approx -\sigma_r m_2$ , $\dot{m}_2\approx \sigma_r m_1$ , and the frictional terms approach $-\lambda \sigma_r m_i$ in accordance with the Bondi-Gold model. But for extreme damping the two models behave altogether differently.

Core.-A detailed calculation is needed to interpret $\gamma$ . In the case of damping by the core, an upper limit can be obtained using the Bondi-Gold method. Consider a shell with moments of inertia $A$ , $A$ and $C$ enclosing a sphere having a moment $A'$ . The two bodies are set in rotation, and we examine the motion assuming that the coupling torque is given by $\Omega^{-1}\gamma \varepsilon_{ijk} \omega_j (\dot{\omega}_k - \dot{\omega}_k')$ where $\omega_k$ is the angular

velocity of the shell and $\omega_{k}^{\prime}$ is the angular velocity of the inner body. $\gamma$ is an interaction constant. The normal modes for the system include the damped wobble. This mode shows zero damping for $\gamma = 0$ , $\gamma = \infty$ ; in the latter case the bodies are rigidly joined. The damping is a maximum for

$$
\gamma = \gamma_ {0} = \frac {A}{C - A},
$$

and for this special case the wobble is attenuated according to

$$
\exp \left(- \frac {1}{2} \gamma_ {0} ^ {- 1} \Omega t\right) = \exp \left(- \frac {1}{2} \sigma_ {s} t\right) \tag {10.7.5}
$$

where $\sigma_{s}$ is the frequency of wobble of the rigid shell. The maximum damping rate is independent of the core's moment of inertia. The corresponding solution by Bondi and Gold contains a time factor

$$
\exp \left[ - \frac {1}{2} \gamma_ {0} ^ {- 1} \Omega t \frac {A ^ {\prime}}{A + A ^ {\prime}} \right]
$$

which depends on the moment of inertia, $A'$ , of the core and has a damping time $(1 + A / A')$ times that in (10.7.5).

According to (10.7.5) the amplitude decays to $e^{-1}$ of its initial value in a time $\pi^{-1}(2\pi /\sigma_s)$ ; for $\sigma_{s} = \sigma_{0}$ this equals 100 days. Thus the maximum rate of damping is more than sufficient to account for the observed damping time of at least 10 years. The question is whether the actual dissipation in the core is sufficient to account for the damping time.

We may examine the question by application of the boundary layer theory to a viscous core. The thickness of the boundary layer is $(2\eta /\Omega)^\ddagger$ and the rate of dissipation per unit area is of the order $\rho V^2 (\eta \Omega)^\ddagger$ , where $V$ is the differential velocity between core and mantle at the boundary. Jeffreys and Vicente (1957a, b) have shown that to a first approximation the core remains motionless, and under this assumption we obtain

$$
V \approx \frac {2 \pi | \mathbf {m} | a _ {\mathrm {c o r e}}}{(2 \pi / \sigma_ {s})} \approx \frac {2 \pi \times 2 5 0 \mathrm {c m}}{4 \times 1 0 ^ {7} \sec} \approx 4 \times 1 0 ^ {- 5} \mathrm {c m} \sec^ {- 1}
$$

* Jeffreys has called our attention to the fact that for periods long compared to a day the boundary layer argument applies provided we replace $\sigma$ by $\Omega$ . We are concerned with nearly horizontal motion, $u = u_{x} + iu_{y}$ . For simple harmonic oscillations the equations of motion are

$$
i \sigma \mathbf {u} + i f _ {G} \mathbf {u} = \eta \left(\partial^ {2} u / \partial z ^ {2}\right)
$$

and the Coriolis frequency $f_{\sigma}$ swamps the oscillation frequency $\sigma$ . The result is implicit in the work of Bondi and Lyttleton (1948). The flow in the boundary layer is an Ekman spiral.

for an upper limit of the differential speed. The dissipation for the entire Earth is at the rate

$$
4 \pi a _ {\text {c o r e}} ^ {2} \rho V ^ {2} (\eta \Omega) ^ {\frac {1}{2}} \approx 2 \times 1 0 ^ {8} \eta^ {\frac {1}{2}} \operatorname {e r g s} \sec^ {- 1}. \tag {10.7.6}
$$

Jeffreys's (1956) discussion of the viscosity of the core would indicate $10^{8} \, \text{cm}^{2} \, \text{sec}^{-1}$ as an upper limit for $\eta$ . The corresponding thickness of the boundary layer is $15 \, \text{km}$ , and the rate of dissipation according to (10.7.6) is $2 \times 10^{12} \, \text{ergs} \, \text{sec}^{-1}$ , as compared to the 'observed' rate of $10^{15} \, Q^{-1} \, \text{ergs} \, \text{sec}^{-1}$ (10.7.3).

Mantle. An alternative energy sink is in the mantle. Laboratory and seismic data show that the $Q$ of inorganic non-ferromagnetic solids is independent of frequency over a frequency range $10^{7}$ to $10^{-1}$ c/s (Knopoff and MacDonald, 1958). For any model involving linear friction $Q$ is frequency-dependent. Knopoff and MacDonald have therefore accounted by non-linear friction for damping in this frequency range, and they obtain values between 100 and 250 for the $Q$ of the mantle. If this behavior can be extrapolated to $10^{-7}$ c/s, as perhaps indicated by the $Q$ of the pole tide, then the conclusion is that the same non-linear processes responsible for the damping of earthquake waves are responsible for damping the Chandler wobble. A lower $Q$ (as indicated by the latitude observations) requires a mechanism other than solid friction if the motion is to be damped in the mantle. The usual resort is to a Maxwell body with a kinematic viscosity of $2 \cdot 5 \times 10^{19} \mathrm{~cm}^2 \sec^{-1}$ ( $\S 10.3$ ). Jeffreys (1956) states that such a viscosity in the lower mantle coupled with material having 300 bars strength in the upper $700 \mathrm{~km}$ could account both for the damping and gravity anomalies. Later work by Jeffreys (1958a) emphasizes a model based on Lomnitz' (1956, 1957) experiments on the finite strain of rocks. It is not obvious that Lomnitz' results are applicable to the present problem.

Oceans.—In our model the maximum damping rate is independent of the inertia of the core, and this suggests that, at least in principle, the damping could result also from the motion of the oceans relative to the sea bottom. Jeffreys (1952, p. 245) has examined this possibility and finds it to be ineffective. His argument consists of three steps: (1) the rate of dissipation for the semi-diurnal tide is of the order $10^{19}$ ergs $\mathrm{sec}^{-1}$ . On the supposition that the dissipation rates are

proportional to the square of the equilibrium amplitudes, the pole tide dissipates roughly

$$
\left(\frac {1}{2} \mathrm {c m}{3 0 \mathrm {c m}}\right) ^ {2} 1 0 ^ {1 9} = 3 \times 1 0 ^ {1 5} \operatorname {e r g s} \sec^ {- 1}.
$$

(2) But only the departure from equilibrium response is associated with dissipation. For a uniform Earth covered by oceans Jeffreys estimates this departure to be 2-5 per cent for the pole tide. For the semi-diurnal tide he sets the departure at 100 per cent, and obtains

$$
\left(\frac {2 \cdot 5}{1 0 0}\right) ^ {2} 3 \times 1 0 ^ {1 5} = 2 \times 1 0 ^ {1 2} \operatorname {e r g s} \sec^ {- 1}.
$$

(3) But the dissipation by $10^{19}$ ergs $\sec^{-1}$ of the semi-diurnal tides takes place largely in shallow seas, where the magnification due to local resonances may be important. No such magnification is to be expected for the pole tide. This leads to a further reduction 'by some hundreds', so that the final value is of the order of $10^{10}$ ergs $\sec^{-1}$ as compared to the 'observed' value of $10^{15}Q^{-1}$ ergs $\sec^{-1}$ .

(1) is based on a comparison of a $p_2^1$ and $p_2^0$ tide, and this requires justification; (2) follows from a theory for a global ocean, but in accordance with the remarks in (§ 10.4) the presence of shelving continents may entirely alter the results; with regard to (3) there is now some doubt as to whether the dissipation takes place in shallow seas (§ 11.8) and some evidence that the pole tide is in fact amplified (§ 10.4). It would appear that the oceans cannot be ruled out as a possible source of damping.

The conclusions are then as follows:

(1) If the $Q$ is between 100 and 200, as vaguely suggested by the pole-tide analysis, then solid friction in the mantle can account for the damping.   
For a $Q$ of 30 to 50, as indicated by the latitude analysis, there are many possibilities:   
(2) The damping can be in the oceans.   
(3) The lower mantle is a possible energy sink; a model involving a Maxwell viscosity is, however, unsupported by laboratory and seismic evidence.   
(4) Damping by viscosity in the core appears to be ruled out; electromagnetic damping is still a possibility (Jeffreys, 1956).

(5) Impulses of a non-random kind (originating in the core, oceans or atmosphere) can absorb as well as excite the wobble. The computed $Q$ is then not due to damping, but associated with the interaction between these loosely-coupled components.

The situation is appallingly uncertain.

# 8. The Love number $k$

Takeuchi (1950) calculated

$$
k _ {e} = 0. 2 9
$$

for the Earth on the basis of Bullen's distribution of density and elasticity. The close agreement with the observed value of the tidal-effective rigidity

$$
k = 0 \cdot 2 9 \pm 0 \cdot 0 1 \tag {10.3.2}
$$

is misleading. In the first place, the value of $k_{\bullet}$ depends critically on the surface density, $\pmb{\rho}$ . Takeuchi (1951) obtains

$$
k _ {e} = 0 \cdot 2 8 1 \quad \text {f o r} \quad \rho = 3 \cdot 0 \mathrm {g c m} ^ {- 3},
$$

$$
k _ {e} = 0 \cdot 2 5 6 \quad \text {f o r} \quad \rho = 2 \cdot 7 \mathrm {g c m} ^ {- 3},
$$

for the same model of the Earth. Furthermore, the parameters $k_{\bullet}$ and $k$ are not immediately comparable; $k_{\bullet}$ is defined for a static response of the core and does not take into account the effect of oceans on the wobble. For a comparison we must first allow for the response of core and oceans, and this is due primarily to the frictional interaction between the shell and the fluid. Unlike classical tides, gravitational effects are of second order.

The oscillations excited by the wobble are only in part communicated to a liquid core so that the inertia of the core plays only a minor role in determining the period. Indeed, if the core were a perfect fluid occupying a spherical cavity within a rigid shell, the core would not partake in the wobble at all. The fraction of the core involved in the wobble depends on the ellipticity, density distribution and viscosity of the core and on the electromagnetic forces acting on core and mantle. Only the ellipticity and density distribution as modified by the elasticity of the shell have been investigated (Jeffreys and Vicente, 1957a, b). The subtraction of the inertia of the core then reduces the period of the dynamic model, as compared to the static model, in the ratio of the inertia of the core

to the inertia of core plus shell. For a rigid outer Earth, the ratio is one-tenth, and the reduction in period is 30 days.

In quite the same way an inviscid ocean covering the whole Earth would shorten the period, though by a very small amount since the ocean's moment of inertia is minute. If, on the other hand, the ocean remained always aligned with respect to the wobbling axis, then the ocean would lengthen the period. The lengthening due to such an equilibrium tide is 33 days.

If, without any real evidence, we assume an equilibrium pole tide, then by a remarkable coincidence the adjustments in the Love number $k$ due to core and oceans appear to cancel. The equilibrium pole tide reduces the value from 0·29 to 0·23. Jeffreys and Vicente (1957) demonstrate that the dynamic effects of the core increase $k$ by about 0·08. With this cancellation we obtain a close agreement between the theoretical tidal-effective Love number

$$
k = k _ {s} - 0 \cdot 0 6 + 0 \cdot 0 8 = 0 \cdot 3 1
$$

and the observed value, 0-29. However, the precision of the theoretical value of $k$ is far smaller than that of $k_{e}$ because of the two large and as yet uncertain corrections.

# 9. Summary

The statistical properties of the latitude time series are those associated with a damped oscillator excited at random. Peak response is at a period of 1-20 years; the $Q$ is poorly determined but appears to lie between 30 and 40.* From the peak period one determines $k = 0\cdot 29$ for the tidal-effective Love number, a value consistent with Takeuchi's estimate corrected for the (uncertain) response of core and oceans. The $Q$ can be interpreted in terms of a viscosity of $10^{20}\mathrm{gcm}^{-1}\sec^{-1}$ for a Maxwell Earth, or $3\times 10^{17}\mathrm{gcm}^{-1}$ $\sec^{-1}$ for a Kelvin-Voigt Earth. Both models have severe shortcomings, and the problem of the dissipation is not solved. Irregular variations of the atmosphere are the most likely cause of the wobble.

* Note added in press. A very complete analysis by Peter Fellgett based on the method of maximum likelihood is now in the press (Monthly Notices Royal Astronomical Society). His results are: $F_0 = 1 \cdot 180 \pm 0 \cdot 012$ c/year, $d^{-1} = 12 \cdot 4$ years, Chandler power $= 259 \cdot 2(0^{\prime \prime} \cdot 01)^{2}$ . According to Fellgett the value of $\alpha^{-1}$ is 'uncertain by a factor of at least 10, and damping times as short as $2\frac{1}{2}$ years or as long as several hundred years are not excluded'. Fellgett has substantiated his uncertainty estimates with artificial time series of random numbers.
