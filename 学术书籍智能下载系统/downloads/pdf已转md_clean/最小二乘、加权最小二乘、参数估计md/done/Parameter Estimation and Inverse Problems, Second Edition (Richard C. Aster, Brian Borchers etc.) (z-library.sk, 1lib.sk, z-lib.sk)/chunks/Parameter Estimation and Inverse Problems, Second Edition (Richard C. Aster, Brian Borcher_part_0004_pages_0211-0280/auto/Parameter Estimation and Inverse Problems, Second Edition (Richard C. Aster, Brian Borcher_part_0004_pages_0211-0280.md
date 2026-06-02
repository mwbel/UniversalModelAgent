and its inverse is

$$
\begin{array} { l } { { \displaystyle m _ { j } = \big ( \mathrm { D F T } ^ { - 1 } [ \mathcal { M } ] \big ) _ { j } } } \\ { { \displaystyle ~ = \frac { 1 } { n } \sum _ { k = 0 } ^ { n - 1 } \mathcal { M } _ { k } e ^ { \imath 2 \pi j k / n } . } } \end{array}
$$

Equation (8.37) states that the sequence $m _ { j }$ can be expressed as a linear combination of the $n$ basis functions $e ^ { { \imath 2 \pi j k } / { n } }$ ， where the complex weights in the linear combination are the discrete spectral elements $\mathcal { M } _ { k }$ (with an additional scaling factor of $1 / n$ in (8.37)). The DFT basis functions are orthonormal on an $n$ -point interval in that, for any integers $l$ and $k$

$$
\frac { 1 } { n } \sum _ { j = 0 } ^ { n - 1 } e ^ { \imath 2 \pi j l } e ^ { - \imath 2 \pi j k / n } = \left\{ { 1 } \atop { 0 } \right. \ l \ne k . \nonumber
$$

The DFT operations (8.35) and (8.37) are also widely referred to as the FFT and IFFT because a particularly efcient algorithm, the fast Fourier transform, is nearly ubiquitously used for their evaluation. The transforms can be calculated in MATLAB using the fft and ifft commands (note that FFT vectors and arrays in MATLAB,as is standard, are indexed beginning with one instead of zero). The DFT expression of Parseval’s theorem (8.23) is

$$
\sum _ { j = 0 } ^ { n - 1 } | m _ { j } | ^ { 2 } = \frac { 1 } { n } \sum _ { k = 0 } ^ { n - 1 } | \mathcal { M } _ { k } | ^ { 2 } .
$$

DFT spectra, $\mathcal { M } _ { k }$ ， are generally complex, discrete,and periodic,where the period is $n$ . There is an implicit assumption in DFT theory that the associated time domain sequence, $m _ { j }$ ,is also periodic with period $n$ Because of these periodicities,DFT results can be stored in complex vectors of length $n$ without loss of information,although (8.35)and (8.37) are valid for any integer index $k$ ，The DFT of a real-valued sequence has Hermitian symmetry about $k = 0$ and $k = n / 2$ , as defined by $\mathcal { M } _ { k } = \mathcal { M } _ { n - k } ^ { * }$ (see Exercise 8.2).

The mapping of the discrete spectrum index to specific frequencies is proportional to the sampling rate $f _ { s }$ .For $n$ even,the positive frequencies, $l f _ { s } / n$ ，where $l =$ 1,..., $n / 2 - 1$ , correspond to indices $k = 1$ ，， $n / 2 - 1$ , and the negative frequencies, $- l f _ { s } / n$ ,correspond to indices $k = n / 2 + 1$ ，.， $n - 1$ . The frequencies $\pm f _ { s } / 2$ have identical DFT values and correspond to index $k = n / 2$ .For $n$ odd, there is no integer $k$ corresponding to exactly half of the sampling rate. In this case, positive frequencies correspond to indices 1 through $( n - 1 ) / 2$ and negative frequencies correspond to indices $( n + 1 ) / 2$ through $n - 1$ .Figure 8.1 displays the discrete spectrum index-frequency mapping with respect to $k$ for an $n = 1 6$ -length DFT.

![](images/8a021bb4104efb3cdda27cfd14f5812178a79ada345033114211067b41f28a27.jpg)  
Figure 8.1 Frequency and index mapping for the DFT of a real-valued sequence ( ${ \mathit { n } } = 1 6 )$ sampled at $f _ { s }$ .For DFT theory to accurately represent Fourier operations on a continuous time signal, $f _ { s }$ must be greater than or equal to the Nyquist frequency (8.40).

The Hermitian symmetry of the DFT implies that, for a real-valued sequence, the spectral amplitude, $| { \mathcal { M } } |$ ， is symmetric and the spectral phase is antisymmetric with respect to $k = 0$ and $k = n / 2$ . See Figure 8.1. For this reason it is customary to just plot the spectral amplitude and phase for positive frequencies in depicting the spectrum of a real signal.

For a uniformly sampled sequence to accurately represent a continuous function that contains nonnegligible spectral energy up to some maximum frequency $f _ { \mathrm { m a x } }$ ，the sampling rate, $f _ { s }$ , must be at least as large as the Nyquist frequency, $f _ { N }$ ，so that

$$
f _ { s } \ge f _ { N } = 2 f _ { \mathrm { m a x } } .
$$

Should (8.4O) not be met, a nonlinear and generally irreversible distortion called aliasing occurs. Generally speaking,aliasing causes spectral energy at frequencies $f > f _ { s } / 2$ to be“folded” and superimposed onto the DFT spectrum within the frequency range $- f _ { s } / 2 \le f \le f _ { s } / 2$

Consider a model sequence $m _ { j }$ of length $n$ and an impulse response sequence $g _ { j }$ of length $p$ , where both sequences are synchronously and uniformly sampled at $f _ { s } = 1 / \Delta t$ The discrete convolution of the two sequences can be performed in two ways.

The first method is a serial convolution, which produces a sequence of length $^ { n + }$ $p - 1$ ：

$$
d _ { j } = \sum _ { k = 0 } ^ { n - 1 } m _ { k } g _ { j - k } \ \Delta t \quad j = 0 , \ 1 , \ . \ . \ . \ , \ n + p - 2 .
$$

Serial convolution implements the discrete approximation to the convolution integral, and is implemented in MATLAB by the conv command.

The second type of discrete convolution is a circular convolution. Circular convo-lution is applicable to two sequences of equal length. If the lengths initially differ, they may be equalized by padding the shorter of the two sequences with zeros.The result of a circular convolution is as if each sequence is first expanded to be periodic (with period $n$ ),and then serially convolved solely on the index interval $j = 0$ ,1，..., $n - 1$ A circular convolution can be implemented using the discrete counterpart of the convolution theorem,

$$
\begin{array} { r c l } { \mathbf { d } = \mathrm { D F T } ^ { - 1 } [ \mathrm { D F T } [ \mathbf { m } ] \odot \mathrm { D F T } [ \mathbf { g } ] ] \Delta t } \\ { = \mathrm { D F T } ^ { - 1 } [ \mathcal { M } \odot \mathcal { G } ] \Delta t , } \end{array}
$$

where $\mathcal { M } \odot \mathcal { G }$ indicates element-by-element multiplication of the vectors $\mathcal { M }$ and $\mathcal { G }$

A very important practical consideration is that circular convolution implemented using the discrete convolution theorem (8.42) is much more efficient than serial convolution invoked with simple summation as in (8.41). To avoid wrap-around effects arising due to the implied $n \cdot$ -length periodicity of $\mathbf { m }$ and $\mathbf { g }$ in the circular convolution, and thus obtain a result that is indistinguishable from the serial convolution (8.41),it may be necessry to pad one or both series with up to $n$ zeros and apply (8.42) on the extended sequences.Because of the factoring strategy used in the FFT algorithm, it is also desirable for computational efficiency to pad $\mathbf { m }$ and $\mathbf { g }$ to lengths that are powers of 2,or are at least have many small prime factors.

Consider the case where we have a theoretically known, or accurately estimated, system impulse response, $g ( t )$ , convolved with an unknown model, $m ( t )$ . The continuous forward problem is

$$
d ( t ) = \int _ { a } ^ { b } g ( t - \tau ) m ( \tau ) \ d \tau .
$$

Uniformly discretizing this expression using simple collocation with a sampling rate, $f _ { s } = 1 / \Delta t$ , that is rapid enough to satisfy (8.4O) and thus avoid aliasing, gives

$$
\mathbf { d } = \mathbf { G } \mathbf { m } ,
$$

where $\mathbf { d }$ and $\mathbf { m }$ are $m$ and $n$ length sequences, respectively, and $\mathbf { G }$ is a matrix with $m$ rows of length $n$ .Each row of $\mathbf { G }$ is a time-reversed and time-shifted representation of the impulse response, scaled by $\Delta t$ to approximate the convolution integral,

$$
G _ { j , k } = g _ { j - k } \Delta t .
$$

This time domain representation of a forward problem convolution was previously examined in Example 3.2.

An inverse solution using Fourier methods can be obtained by first padding $\mathbf { d }$ and $\mathbf { g }$ appropriately with zeros so that they are of some equal and suficient length, $n$ ,to render moot any wrap-around artifacts associated with circular convolution. $\mathbf { G }$ then becomes an $n$ by $n$ matrix. Applying the DFT and (8.26) allows us to cast the forward problem as a complex-valued linear system,

$$
{ \mathcal { D } } = \mathbf { G } { \mathcal { M } } .
$$

$\mathbf { G }$ in (8.46) is a complex-valued diagonal matrix with

$$
G _ { k , k } = \mathcal { G } _ { k } ,
$$

where $\mathcal { G }$ is the discrete Fourier transform of the sampled impulse response g, $\mathcal { D }$ is the discrete Fourier transform of the data vector $\mathbf { d }$ and $\mathcal { M }$ is the discrete Fourier transform of the model vector m. We can write (8.46) more simply using the element-by-element multiplication operator as

$$
\mathcal { D } = \mathcal { G } \odot \mathcal { M } .
$$

Equation (8.46) suggests a solution by spectral division, where we first solve for the Fourier transform of the model using the element-by-element division operation (or equivalently, inverting the diagonal matrix $\mathbf { G }$ in (8.46)),

$$
\mathcal { M } = \mathcal { D } \oslash \mathcal { G } ,
$$

and then obtaining the model $\mathbf { m } = \mathrm { D F T } ^ { - 1 } [ \mathcal { M } ]$

Equation (8.49) is appealing in its simplicity and efficiency. The application of (8.26), combined with the effcient FFT implementation of the DFT, reduces the necessary computational effort from solving a potentially very large linear system of time domain equations (8.44) to just three $n \cdot$ -length DFT operations (taking the DFT of the data and impulse response vectors,and then the inverse DFT of the element-by-element quotient). If $\mathbf { d }$ and $\mathbf { g }$ are real, packing/unpacking algorithms also exist that allow DFT operations to be further reduced to complex vectors of length $n / 2$

However, (8.49) does not avoid the instability that is potentially associated with deconvolution if the reciprocal of any element in $\mathcal { G }$ is large. Equation (8.49) typically requires regularization to be useful.

# 8.3.WATER LEVEL REGULARIZATION

A straightforward and widely applied method of regularizing spectral division is water level regularization. The water level strategy employs a modified impulse response spectrum, $\mathcal { G } _ { \boldsymbol { w } }$ , in (8.49),where

$$
( \mathcal { G } _ { w } ) _ { i } = \left\{ \begin{array} { l l } { \mathcal { G } _ { i } } & { ( | \mathcal { G } _ { i } | > w ) } \\ { w ( \mathcal { G } _ { i } / | \mathcal { G } _ { i } | ) } & { ( 0 < | \mathcal { G } _ { i } | \leq w ) } \\ { w } & { ( \mathcal { G } _ { i } = 0 ) . } \end{array} \right.
$$

The water level regularized model estimate is then

$$
\begin{array} { r } { \mathbf { m } _ { w } = \mathrm { D F T } ^ { - 1 } \left[ \mathscr { D } \oslash \mathcal { G } _ { w } \right] \Delta t . } \end{array}
$$

The colorful name for this technique arises from the construction of $\mathcal { G } _ { w }$ ，applying the analogy of pouring water into the low-amplitude “holes” of $\mathcal { G }$ until the spectral amplitude levels there reach $w$ . The effect in (8.51） is to prevent undesirable noise amplification from occurring at frequencies where $\| \mathcal G \|$ is small.

An optimal water level value, $\boldsymbol { \nu }$ ，will reduce the sensitivity to noise in the inverse solution while stil recovering important model features. As is typical of the regularization process, it is possible to choose a “best” solution by assessing the trade-off between the norm of the residuals (fiting the data) and the model norm (smoothness of the model） as the regularization parameter $\boldsymbol { \nu }$ is varied. In calculating a trade-off curve, Parseval’s theorem (8.39) usefully facilitates calculations of the model and residual norms from spectra without calculating inverse Fourier transforms.Note that the 2-norm of the water level-regularized solution, $\mathbf { m } _ { u }$ ， will be nonincreasing with increasing $\boldsymbol { \nu }$ because $| ( \mathcal { G } _ { u } ) _ { i } | \geq | \mathcal { G } _ { i } |$

# Example 8.1

In Example 3.2, we investigated time domain deconvolution for uniformly sampled data with a sampling rate of $\dot { \gamma } _ { s } = 2 \ \mathrm { H z }$ using the truncated single value decomposition. Here, we solve this problem using frequency-domain deconvolution regularized via the water level technique. The impulse response, true model,and noisy data for this example are plotted in Figures 3.9, 3.11,and 3.12,respectively. We first pad the 210-point data and impulse response vectors with 21O additional zeros to eliminate wrap-around artifacts, and apply the fast Fourier transform to both vectors to obtain corresponding discrete spectra. The spectral amplitudes of the impulse response, data,and noise are critical in assessing the stability of the spectral division solution. See Figure 8.2. The frequencies range from O to $f _ { s } / 2 = 1$ Hz. Because spectral amplitudes for real-valued sequences are symmetric about $k = 0$ and $k = n / 2$ (Figure 8.1), only positive frequencies are shown.

Examining the impulse response spectral amplitude, $| \mathcal { G } _ { k } |$ , in Figure 8.2, we note that it decreases by approximately three orders of magnitude between very low frequencies and half of the sampling frequency $( f _ { s } / 2 = 1 \ \mathrm { H z } )$ . The convolution theorem (8.26) shows that the forward problem convolution multiplies the spectrum of the model by $\mathcal G ( f )$ in mapping it to the data. Thus,the convolution of a general signal with broad frequency content with this impulse response will strongly attenuate higher frequencies. Figure 8.2 also shows that the spectral amplitudes of the noise-free data fall off more quickly than the impulse response. This indicates that spectral division will be a stable process for noise-free data in this problem. Figure 8.2 also shows that the spectral amplitudes of the noisy data dominate the signal at frequencies higher than $f \approx 0 . 1 ~ \mathrm { H z }$ ，Because of the small values of $\mathcal { G } _ { k }$ at these frequencies,the spectral divi-sion solution using the noisy data will be dominated by noise (as was the case in the time domain solution of Example 3.2; see Figure 3.14). Figure 8.3 shows the amplitude spectrum of the noisy data (Figure 3.14) divided by the spectrum of the impulse response. The resulting model spectrum is dominated by noise at frequencies above about $0 . 1 \mathrm { H z }$

To regularize the spectral division solution,an optimal water level, $w$ ，is sought, where $\boldsymbol { \nu }$ should be large enough to avoid the undesirable amplification of noise. Figures 8.2 and 8.3 suggest that the optimal value of $w$ is near the crossover spectral amplitude where the data spectrum is surpassed by noise,or near $w$ somewhat greater than 1. However, such a determination might be more difficult for data with a more complex spectrum,and/or where the distinction between signal and noise spectra is generally less clear. Figure 8.4 shows an L-curve for this example, which suggests an optimal $\boldsymbol { \nu }$ close to 3. Figure 8.5 shows a corresponding range of solutions, and Figure 8.6 shows the solution for $w = 3 . 1 6$

![](images/564b613fdcfb3c6e92fd9ddd3919a6f7397258c6ea093d4f45b132e43b8e2004.jpg)  
Figure 8.3 Spectral amplitudes resulting from the Fouriertransform of the noisy data divided by the Fourier transform of the impulse response (the transfer function).

![](images/7b51d30b1132dc83556cbc2db8ef7a32c05f13e9474431d564b9febe5f732349.jpg)  
Figure8.4 L-curve fora logarithmically distributed range of water level values as indicated.

The solution shown in Figure 8.6, chosen from the corner of the trade-off curve of Figure 8.4, shows features of limited resolution that are typical of regularized solutions. In this case, imperfect resolution induced by regularization is manifested by reduced amplitude,oscillatory side lobes,and model broadening relative to the true model.

# 8.4.TIKHONOV REGULARIZATION IN THE FREQUENCY DOMAIN

An alternative regularized approach to solving the frequency-domain forward problem (8.46) is to consider the system as a least squares minimization problem,as we did in Chapter 4 (e.g., (4.4)):

$$
\operatorname* { m i n } \| \mathbf G \mathcal M - \mathcal D \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathcal M \| _ { 2 } ^ { 2 } .
$$

Expressing 8.52 as an augmented forward problem gives

$$
\operatorname* { m i n } { \left\| \left[ \mathbf { G } \right] \mathcal { M } - \left[ \mathcal { D } \right] \right\| _ { 2 } ^ { 2 } } .
$$

We solve (8.53) by applying the normal equations using the conjugate transpose of the diagonal matrix $\mathbf { G }$ ， $\mathbf { G } ^ { H } ,$ which gives

$$
\big [ \mathbf { G } ^ { H } \quad \alpha \mathbf { I } \big ] \ \left[ \begin{array} { l } { \mathbf { G } } \\ { \alpha \mathbf { I } } \end{array} \right] \ \mathcal { M } = \big [ \mathbf { G } ^ { H } \quad \alpha \mathbf { I } \big ] \ \left[ \begin{array} { l } { \mathcal { D } } \\ { \mathbf { 0 } } \end{array} \right] .
$$

Equation (8.47) corresponds to the zeroth-order Tikhonov-regularized formulation

$$
( \mathbf { G } ^ { H } \mathbf { G } + \alpha ^ { 2 } \mathbf { I } ) \mathcal { M } = \mathbf { G } ^ { H } \mathcal { D } .
$$

with the frequency-domain solution,

$$
\mathcal { M } _ { \alpha } = ( \mathbf { G } ^ { H } \mathbf { G } + \alpha ^ { 2 } \mathbf { I } ) ^ { - 1 } \mathbf { G } ^ { H } \mathcal { D } .
$$

Because $\mathbf { G } ^ { H } \mathbf { G }$ is diagonal, (8.56)can be expressed solely using $n$ -length vector elementby-element operations as

$$
\mathcal { M } _ { \alpha } = ( \mathcal { G } ^ { H } \odot \mathcal { D } ) \oslash ( | \mathcal { G } | _ { 2 } ^ { 2 } + \alpha ^ { 2 } \mathbf { e } ) ,
$$

where $\mathbf { e }$ is an $n$ -length vector of ones. Applying the IDFT to $\mathcal { M } _ { \alpha }$ then produces the corresponding regularized time domain solution, m.

Although we have implemented $\| \mathcal { M } \| _ { 2 } = \| \mathrm { D F T } [ \mathbf { m } ] \| _ { 2 }$ rather than $\| \mathbf { m } \| _ { 2 }$ in (8.53) to regularize the problem, by Parseval's theorem (8.39),the norm of the model spectrum is proportional to the norm of the time domain model. Thus,(8.57) is equivalent to that obtained if we were to regularize using the norm of the model in the time domain model (although the specific values of $\alpha$ will be different).

An important consideration is that the inverse operation (8.57) is applied by elementby-element spectral division of $n$ -length vectors，so the solution can be calculated extremely eficiently relative to inverting a nondiagonal $n$ by $n$ matrix. Even with the additional calculations associated with the FFT, this methodology is typically much more efficient than a time domain approach, such as is described in Example 3.2.

To implement higher-order Tikhonov regularization, we note that

$$
\begin{array} { r l r } {  { \frac { d } { d t } m ( t ) = \frac { d } { d t } \int _ { - \infty } ^ { \infty } M ( f ) e ^ { 2 \pi f t } d f } } \\ & { } & { \displaystyle = \int _ { - \infty } ^ { \infty } \frac { \partial } { \partial t } [ M ( f ) e ^ { 2 \pi f t } ] d f } \\ & { } & { \displaystyle = \int _ { - \infty } ^ { \infty } 2 \pi \imath f M ( f ) e ^ { 2 \pi f t } d f } \\ & { } & { \displaystyle - \infty } \\ & { } & { \displaystyle = \mathcal { F } ^ { - 1 } [ 2 \pi \imath f \mathcal { M } ( f ) ] . } \end{array}
$$

Taking the Fourier transform of both sides gives

$$
\mathcal { F } \left[ \frac { d } { d t } m ( t ) \right] = 2 \pi \imath f \mathcal { M } ( f ) .
$$

Equation (8.59) enables us to effect a first derivative seminorm by multiplying each element of $\mathcal { M }$ by $2 \pi f _ { j }$ ，choosing the $f _ { j }$ to be proportional to the spectral frequency of the $j$ th-element (Figure 8.1). Proportionality is sufficient, because the exact con-stant frequency-scaling factor for converting the DFT index to frequency can be absorbed into the range of the regularization parameter $\alpha$ . Thus, we can effect pth-order Tikhonov regularization by solving

$$
\operatorname* { m i n } { \left\| \left[ \mathbf { G } \right] \mathcal { M } - \left[ \mathcal { D } \right] \right\| _ { 2 } ^ { 2 } } ,
$$

where $\mathbf { K }$ is an $n$ by $n$ diagonal matrix with diagonal elements (e.g., for $n$ even)

$$
K _ { j , j } = \left\{ { ( j - 1 ) / n } \atop { ( j - 1 ) / n - 1 } \right. \quad j = 1 , 2 , \mathrm { ~ . ~ . ~ . ~ , ~ } n / 2 \eqno { }
$$

that are proportional to the frequency represented by the jth element of $\mathcal { M }$ . The least squares solution, obtained utilizing the normal equations, is thus

$$
\mathcal { M } _ { \alpha } = ( \mathbf { G } ^ { H } \mathbf { G } + \alpha ^ { 2 } \mathbf { K } ^ { 2 p } ) ^ { - 1 } \mathbf { G } ^ { H } \mathcal { D }
$$

or

$$
\mathcal { M } _ { \alpha } = ( \mathcal { G } ^ { H } \odot \mathcal { D } ) \oslash ( | \mathcal { G } | _ { 2 } ^ { 2 } + \alpha ^ { 2 } \mathbf { k } ^ { 2 p } ) ,
$$

where $\mathbf { k } ^ { 2 p }$ is the vector composed of the diagonal elements of $\mathbf { K } ^ { 2 p }$

As with the zeroth-order solution (8.57)，(8.63) can be evaluated very efficiently with element-by-element $n$ -length vector operations. Note that the implementation of the (nonidentity） matrix $\mathbf { K }$ in (8.62) weights the higher frequency components of the model more in the regularization,and thus tends to make them small. It is thus straightforward to consider and implement more general regularization matrices that will penalize particular Fourier components (e.g.， within a particular frequency range).

# Example 8.2

Let us reconsider Example 8.1 in a Tikhonov regularization framework.

We first implement zeroth-order regularization using (8.56) and examine the tradeoff curve (Figure 8.7). The suite of solutions is shown in Figure 8.8,and a solution selected from the trade-off curve is shown in Figure 8.9 compared with the true model. Note that, compared to the water level solution shown in Figure 8.6, the Tikhonov regularized solution has better amplitude recovery and is somewhat smoother. On the other hand, the recovered zeroth-order Tikhonov regularized model shows higher amplitude structure later in the time series. Applying second-order Tikhonov regularization, we obtain a corresponding trade-off curve (Figure 8.1O) and recover a still smoother model that is generally closer to the true model than either water level or zeroth-order Tikhonov regularization (Figures 8.11 and 8.12). The final accuracy of any regularized solution will,of course, depend on properties of the true solution.In this particular case the true model is smooth,and the second-order regularization solution is closest.

![](images/6e71dc01e4522614ca9401af350daae9ced187bfc582aa679d0bc3b5f6de290b.jpg)  
Figure 8.7 L-curve for a logarithmically distributed range of regularization-parameter values, zerothorder Tikhonov regularization.

![](images/b6677abf70e4edebae615970b511002391f37632ed43a2acc8456258a5132d86.jpg)  
Figure 8.8 Zeroth-order Tikhonov regularized models corresponding to the range of regularization parameters used to construct Figure 8.7.Dashed curves show the true model,and bold trace shows the L-curve determined model with $\alpha = 0 . 4 8$

![](images/8cce630e48c7856d0b0d87db0fab9f0ce96e09b76355e4f2e8eabcf2598f8c94.jpg)  
Figure 8.9 Zeroth-order Tikhonov regularized model corresponding to $\alpha = 0 . 4 8 .$ Dashed curve shows the true model.

![](images/1e5d5cee01d72a05aeaa0e477384a6433724c6dea0e2e75651e6bf0c5a63a828.jpg)  
Figure 8.10 L-curve for a logarithmically distributed range of regularization-parameter values, second-order Tikhonov regularization.

![](images/74c9ef63709c5c70d3125be15edf92dbbe1da0fef969b0f18cf189c7e889ca0e.jpg)  
Figure 8.11 Second-order Tikhonov regularized models corresponding to the range of regularization parameters used to construct Figure 8.7. Dashed curves show the true model,and bold trace shows the L-curve determined model with $\alpha = 3 0 . 2$ (Figure 8.10).

A significant new idea introduced by the Fourier methodology is that it provides a set of orthonormal model and data basis functions of the form of (8.27),the complex exponentials, that have the property of passing through a linear system altered in phase and amplitude,but not in frequency or functional character (8.3O). This remarkable fact is the essence of the convolution theorem (8.26),which leads to frequency-domain inverse methodologies that are very efficient when coupled with the FFT algorithm. This efficiency can become critically important when larger and/or higher-dimensional models are of interest, a large number of deconvolutions must be performed, or computational speed is critical, such as in real-time applications. The spectrum of the impulse response (such as in Figures 8.2 and 8.3) can be used to understand what frequency components may exhibit instability in an inverse solution. The information contained in the spectrum of Figure 8.2 is thus analogous to that obtained with a Picard plot in the context of the SVD (Chapters 3 and 4). The Fourier perspective also provides a link between linear inverse theory and the (vast) field of linear filtering. The deconvolution problem in this context is identical to finding an optimal inverse filter to recover the model while suppressing the influence of noise, and Tikhonov regularization in the frequency domain applies a preferential filtering to the solution that reduces amplitudes of high-frequency Fourier components.

# 8.5. EXERCISES

1. Given thatthe Fourier transform ofareal-valued linear system $g ( t )$ ，

$$
\mathcal { F } [ g ( t ) ] = \mathcal { G } ( f ) = \mathrm { r e a l } ( \mathcal { G } ( f ) ) + \operatorname* { i m a g } ( \mathcal { G } ( f ) ) = \alpha ( f ) + \imath \beta ( f ) ,
$$

is Hermitian,

$$
\mathcal { G } ( f ) = \mathcal { G } ^ { * } ( - f ) ,
$$

show that convolving $g ( t )$ with $\sin ( 2 \pi f _ { 0 } t )$ and $\cos ( 2 \pi f _ { 0 } t )$ produces the scaled and phase-shifted sinusoids,

$$
\begin{array} { r l } & { \boldsymbol { g } ( t ) \ast \sin ( 2 \pi f _ { 0 } t ) = \vert \boldsymbol { \mathcal { G } } ( f _ { 0 } ) \vert \sin ( 2 \pi f _ { 0 } t + \theta ( f _ { 0 } ) ) } \\ & { \boldsymbol { g } ( t ) \ast \cos ( 2 \pi f _ { 0 } t ) = \vert \boldsymbol { \mathcal { G } } ( f _ { 0 } ) \vert \cos ( 2 \pi f _ { 0 } t + \theta ( f _ { 0 } ) ) , } \end{array}
$$

where the scale factor is the spectral amplitude,

$$
| \mathcal { G } ( f _ { 0 } ) | = ( \alpha ^ { 2 } ( f _ { 0 } ) + \beta ^ { 2 } ( f _ { 0 } ) ) ^ { \frac { 1 } { 2 } } ,
$$

and the phase-shift factor is the spectral phase

$$
\theta ( f _ { 0 } ) = \tan ^ { - 1 } \left( \frac { \beta ( f _ { 0 } ) } { \alpha ( f _ { 0 } ) } \right) .
$$

2. (a) Demonstrate using (8.35) that the DFT of an $n \cdot$ -point, real-valued sequence, $\mathbf { x }$ ， is Hermitian, i.e.,

$$
\mathcal { X } _ { n - k } = \mathcal { X } _ { k } ^ { * }
$$

(b) Demonstrate that the Hermitian symmetry shown in part (a) implies that the $N$ independent elements in a time series $\mathbf { x }$ produce $N / 2 + 1$ independent elements $N$ even) or $( N - 1 ) / 2 + 1$ independent elements ( $_ N$ odd) in the DFT $\mathcal { X }$ .As the DFT has an inverse (8.37) that reproduces $\mathbf { x }$ from $\mathcal { X }$ ,clearly information has not been lost in taking the DFT, yet the number of independent elements in $\mathbf { x }$ and $\mathcal { X }$ differ. Explain.

3.A linear damped vertical harmonic oscillator consisting of a mass suspended on a lossy spring is affixed to the surface of a terrestrial planet to function as a seismometer, where the recorded displacement, $z ( t )$ ,of the mass relative to its equilibrium position will depend on ground motion (note that when the surface of the planet moves upward, the inertia of the mass will tend to make it remain at rest,and the corresponding motion of the mass relative to its suspension system will be downward). For an upward ground displacement, $u ( t )$ , the system can be mathematically modeled as the linear differential equation (8.31) as

$$
\frac { d ^ { 2 } z } { d t ^ { 2 } } + \frac { D } { M } \frac { d z } { d t } + \frac { K } { M } z = \frac { d ^ { 2 } u } { d t ^ { 2 } } ,
$$

where the physical properties of the oscillator are defined by the mass $M$ ，the displacement-proportional spring force constant $K$ ，and the velocity-proportional damping force constant $D$

(a) By taking the Fourier transform of (8.71),obtain the transfer function $\mathcal { G } ( f ) =$ $\mathcal { Z } ( f ) / \mathcal { U } ( f )$ ,where $\mathcal { Z } ( f )$ and $\mathcal { U } ( f )$ are the Fourier transforms of $z ( t )$ and $u ( t )$ ， respectively.

In terms of $M , K$ and $D$ ,and $f _ { s } = \sqrt { K / M }$ ：

(b) For what general frequency range of ground motion will the response of this instrument be difficult to remove via a deconvolution?   
(c) For what general frequency range of ground motion will the output of this instrument be nearly identical to the true ground motion?

4.A displacement seismogram is observed from a large earthquake at a far-field seismic station, from which the source region can be approximated as a point. A much smaller aftershock from the main shock region is used as an empirical Green's function for this event. It is supposed that the observed signal from the large event should be approximately equal to the convolution of the main shock's rupture history with this empirical Green’s function. The 256-point seismogram is in the file seis.mat. The impulse response of the seismometer is in the file impresp.mat.

(a) Deconvolve the impulse response from the observed main shock seismogram using frequency-domain Tikhonov zeroth-order deconvolution to solve for the source time function of the large earthquake.Note that the source time function is expected to consist of a nonnegative pulse or set of pulses. Estimate the source duration in samples and assess any evidence for subevents and their relative dura-tions and amplitudes. Approximately what water level do you believe is best for this data set? Why?

(b) Perform second-order ( $\vert p = 2 )$ , frequency-domain Tikhonov deconvolution to solve this problem. See Exercise 8.4(b).

(c)Recast the problem as a discrete linear inverse problem,as described in the example for Chapter 3,and solve the system using second-order Tikhonov regularization.

(d) Are the results in (c) better or worse than in (a) or (b)? How and why? Compare the amount of time necessary to find the solution in each case on your computing platform.

# 8.6. NOTES AND FURTHER READING

Although we examine one-dimensional convolution and deconvolution problems here for conceptual simplicity, note that these results are readily generalizable to higher dimensions,and higher-dimensional formulations of the DFT are widely utilized.

MATLAB has a general $n \cdot$ -dimensional set of FFT algorithms,fftn and ifftn. Many regularization matrices (e.g., the $\mathbf { L }$ roughening matrices introduced for one-dimensional Tikhonov regularization in this text (4.27) and (4.28) are easily recognized as convolutions,where the rows are time-reversed sampled representations of the impulse response of the convolution effected by $\mathbf { L m }$ Fourier analysis of the frequency response of regularization matrices thus facilitates more sophisticated regularization matrix design.

In some physics and geophysics treatments, the sign convention chosen for the complex exponentials in the Fourier transform and its inverse may be reversed, so that the forward transform (8.16) has a plus sign in the exponent and the inverse transform (8.18) has a minus sign in the exponent. This alternative sign convention merely induces a complex conjugation in the spectrum that is reversed when the corresponding inverse transform is applied. An additional convention issue arises as to whether to express frequency in ${ \mathrm { H z ~ } } ( f )$ or radians per second $( \omega = 2 \pi f .$ ). Alternative Fourier transform formulations using $\omega$ differ from (8.16) and (8.18) by a simple change of variables, and introduce scaling factors of $2 \pi$ in the forward, reverse, or both transforms.

Gubbins [6O] also explores connections between Fourier and inverse theory in a geophysical context. Kak and Slaney [84] give an extensive treatment of Fourier-based methods for tomographic imaging. Vogel [169] discusses Fourier methods for image deblurring. Because of the tremendous utility of Fourier techniques, there are numerous resources on their use in the physical sciences,engineering,and pure mathematics. A basic treatment covering theory and some applications at the approximate level of this text is [2O],and a recommended advanced text on the topic is [131].

# Nonlinear Regression

# Synopsis

Common approaches to solving nonlinear regression problems are introduced, extending the development of linear regression in Chapter 2. We begin with a discussion of Newton's method,which provides a general framework for solving nonlinear systems of equations and nonlinear optimization problems.Then we discuss the Gauss-Newton (GN) and Levenberg-Marquardt (LM) methods, which are versions of Newton's method specialized for nonlinear regression problems.The distinction between LMand Tikhonov regularization is also made. Statistical aspects and implementation issues are addressed,and examples of nonlinear regression are presented.

# 9.1. INTRODUCTION TO NONLINEAR REGRESSION

In previous chapters we have concentrated on linear forward and inverse problems,and have seen that such problems are uniformly approachable using a variety of solution methods. We wil next consider problems that are nonlinear, i.e., forward and inverse problems that do not obey the rules of superposition (1.5) and scaling (1.6). There is no general theory for the solution of nonlinear parameter estimation and inverse problems. However, we wil see that iterative strategies incorporating linear concepts can be applied to solve them in many circumstances.

# 9.2. NEWTON'S METHOD FOR SOLVING NONLINEAR EQUATIONS

Consider a nonlinear system of $m$ equations in $m$ unknowns

$$
\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 } { \mathrm { . } }
$$

We will construct a sequence of vectors, $\mathbf { x } ^ { 0 } , \mathbf { x } ^ { 1 }$ ，.．.，that will converge to a solution $\mathbf { x } ^ { * }$ . If the nonlinear vector function $\mathbf { F }$ is continuously differentiable，we can construct a Taylor series approximation about some starting solution estimate, $\mathbf { x } ^ { 0 }$ ，

$$
\begin{array} { r } { \mathbf { F } \big ( \mathbf { x } ^ { 0 } + \Delta \mathbf { x } \big ) \approx \mathbf { F } \big ( \mathbf { x } ^ { 0 } \big ) + \mathbf { J } \big ( \mathbf { x } ^ { 0 } \big ) \Delta \mathbf { x } , } \end{array}
$$

where $\mathbf { J } ( \mathbf { x } ^ { 0 } )$ is the Jacobian,

$$
\mathbf { J } \big ( \mathbf { x } ^ { 0 } \big ) = \left[ \begin{array} { c c c } { \frac { \partial F _ { 1 } ( \mathbf { x } ) } { \partial x _ { 1 } } } & { \mathbf { \textnormal { . . . } } } & { \frac { \partial F _ { 1 } ( \mathbf { x } ) } { \partial x _ { m } } } \\ { \vdots } & { \ddots } & { \vdots } \\ { \frac { \partial F _ { m } ( \mathbf { x } ) } { \partial x _ { 1 } } } & { \mathbf { \textnormal { . . . } } } & { \frac { \partial F _ { m } ( \mathbf { x } ) } { \partial x _ { m } } } \end{array} \right] \Bigg \vert _ { \mathbf { x } = \mathbf { x } ^ { 0 } } .
$$

Using (9.2),and expressing the difference between the desired solution, $\mathbf { x } ^ { * }$ ,and $\mathbf { x } ^ { 0 }$ as

$$
\Delta \mathbf { x } = \mathbf { x } ^ { * } - \mathbf { x } ^ { 0 }
$$

gives

$$
\mathbf { F } ( \mathbf { x } ^ { * } ) = \mathbf { 0 } \approx \mathbf { F } ( \mathbf { x } ^ { 0 } ) + \mathbf { J } ( \mathbf { x } ^ { 0 } ) \Delta \mathbf { x } ,
$$

which produces a linear system of equations,

$$
\mathbf { J } ( \mathbf { x } ^ { 0 } ) \Delta \mathbf { x } \approx - \mathbf { F } ( \mathbf { x } ^ { 0 } ) ,
$$

that can be solved for $\Delta \mathbf { x }$ to improve the solution estimate.

# Algorithm 9.1 Newton's Method

Given a system of equations $\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 }$ and an initial solution $\mathbf { x } ^ { 0 }$ ， repeat the following steps to compute a sequence of solutions $\mathbf { x } ^ { k }$ . Stop if and when the sequence adequately converges to a solution with $\mathbf { F } ( \mathbf { x } ) = \mathbf { 0 }$

1. Calculate the Jacobian $\mathbf { J } ( \mathbf { x } ^ { k } )$ and $\mathbf { F } ( \mathbf { x } ^ { k } )$ .   
2. Solve $\mathbf { J } ( \mathbf { x } ^ { k } ) \Delta \mathbf { x } = - \mathbf { F } ( \mathbf { x } ^ { k } )$   
3.Let $\mathbf { x } ^ { k + 1 } = \mathbf { x } ^ { k } + \Delta \mathbf { x }$   
4.Let $k = k + 1$

The theoretical properties of Newton’s method are summarized in the follwing theorem. For a proof, see [39].

Theorem 9.1 If $\mathbf { \dot { x } } ^ { 0 }$ is close enough to $\mathbf { x } ^ { * }$ $\mathbf { F } ( \mathbf { x } )$ is continuously differentiable in a neighborhood of $\mathbf { \dot { x } } ^ { * }$ ，and $\mathbf { J } ( \mathbf { x } ^ { * } )$ is nonsingular, then Newton's method will converge to $\mathbf { x } ^ { * }$ . The convergence rate is quadratic in the sense that there is a constant $c$ ， such that for large $k$ ，

$$
\left\| \mathbf { x } ^ { k + 1 } - \mathbf { x } ^ { * } \right\| _ { 2 } \leq c \left\| \mathbf { x } ^ { k } - \mathbf { x } ^ { * } \right\| _ { 2 } ^ { 2 } .
$$

In practical terms,quadratic convergence means that as we approach $\mathbf { x } ^ { * }$ , the number of accurate digits in the solution doubles at each iteration. Unfortunately, if the hypotheses in the above theorem are not satisfied, then Newton's method can converge very slowly or even fail altogether.

A simple modification to Newton’s method often helps with convergence problems. In the damped Newton's method, we use the Newton’s method equations at each iteration to compute an iterative correction to the working solution. However, instead of taking the full step $\mathbf { x } ^ { k + 1 } = \mathbf { x } ^ { k } + \Delta \mathbf { x }$ , we perform a line search across solutions lying along the line $\mathbf { x } ^ { k + 1 } = \mathbf { x } ^ { k } + \alpha \Delta \mathbf { x }$ for a range of positive $\alpha$ values and take the one with minimum $\| \mathbf F ( \mathbf x ^ { k + 1 } ) \| _ { 2 }$

Now suppose that we wish to minimize a scalar-valued function $f ( \mathbf { x } )$ . If we assume that $f ( \mathbf { x } )$ is twice continuously differentiable,we can construct a Taylor series approximation,

$$
f ( \mathbf { x } ^ { 0 } + \Delta \mathbf { x } ) \approx f ( \mathbf { x } ^ { 0 } ) + \nabla f ( \mathbf { x } ^ { 0 } ) ^ { T } \Delta \mathbf { x } + \frac { 1 } { 2 } \Delta \mathbf { x } ^ { T } \mathbf { H } ( f ( \mathbf { x } ^ { 0 } ) ) \Delta \mathbf { x } ,
$$

where $\nabla f ( \mathbf { x } ^ { 0 } )$ is the gradient

$$
\begin{array} { r } { \nabla f ( \mathbf { x } ^ { 0 } ) = [ { \begin{array} { c } { \frac { \partial f ( \mathbf { x } ) } { \partial x _ { 1 } } } \\ { \vdots } \\ { \frac { \partial f ( \mathbf { x } ) } { \partial x _ { m } } } \end{array} } ]  _ { \mathbf { x } = \mathbf { x } ^ { 0 } } } \end{array}
$$

and $\mathbf { H } ( f (  { \mathbf { x } } ^ { 0 } ) )$ is the Hessian

$$
\mathbf { H } ( f ( \mathbf { x } ^ { 0 } ) ) = \left[ \begin{array} { c c c } { \frac { \partial ^ { 2 } f ( \mathbf { x } ) } { \partial x _ { 1 } ^ { 2 } } } & { \cdot \mathbf { \nabla } \cdot \mathbf { \nabla } \cdot \frac { \partial ^ { 2 } f ( \mathbf { x } ) } { \partial x _ { 1 } \partial x _ { m } } } \\ { \vdots } & { \ddots } & { \vdots } \\ { \frac { \partial ^ { 2 } f ( \mathbf { x } ) } { \partial x _ { m } \partial x _ { 1 } } } & { \cdot \mathbf { \nabla } \cdot \mathbf { \nabla } \cdot \frac { \partial ^ { 2 } f ( \mathbf { x } ) } { \partial x _ { m } ^ { 2 } } } \end{array} \right] \left[ \begin{array} { c } { \mathbf { \nabla } \cdot \mathbf { x } } \\ { \mathbf { \nabla } \cdot \mathbf { \nabla } \cdot \mathbf { \nabla } } \\ { \mathbf { \nabla } \cdot \mathbf { x } } \end{array} \right] .
$$

A necessary condition for $\mathbf { x } ^ { * }$ to be a minimum of $f ( \mathbf { x } )$ is that $\nabla f ( \mathbf { x } ^ { * } ) = \mathbf { 0 }$ . We can approximate the gradient in the vicinity of $x ^ { 0 }$ by

$$
\nabla f ( \mathbf { x } ^ { 0 } + \Delta \mathbf { x } ) \approx \nabla f ( \mathbf { x } ^ { 0 } ) + \mathbf { H } ( f ( \mathbf { x } ^ { 0 } ) ) \Delta \mathbf { x } .
$$

Setting the approximate gradient (9.11) equal to zero gives

$$
\mathbf { H } ( f ( \mathbf { x } ^ { 0 } ) ) \Delta \mathbf { x } = - \nabla f ( \mathbf { x } ^ { 0 } ) .
$$

Solving the linear system of equations (9.12) for successve solution steps leads to Newton's method for minimizing $f ( \mathbf { x } )$

Since Newton's method for minimizing $f ( \mathbf { x } )$ is exactly Newton's method for solving a nonlinear system of equations applied to $\mathbf { F } = \nabla f ( \mathbf { x } ) = \mathbf { 0 }$ , the convergence proof follows immediately from the proof of Theorem 9.1.

Theorem 9.2 If $f ( \mathbf { x } )$ is twice continuously differentiable in a neighborhood of a local minimizer $\mathbf { x } ^ { * }$ ， there is a constant $\lambda$ such that $\| \mathbf { H } ( f ( \mathbf { x } ) ) - \mathbf { H } ( f ( \mathbf { y } ) ) \| _ { 2 } \leq \lambda \| \mathbf { x } - \mathbf { y } \| _ { 2 }$ for every

vector y in the neighborhood, $\mathbf { H } ( f ( \mathbf { x } ^ { * } ) )$ is positive definite, and $\mathbf { x } ^ { 0 }$ is close enough to $\mathbf { x } ^ { * }$ ，then Newton's method will converge quadratically to $\mathbf { x } ^ { * }$

# Algorithm 9.2 Newton's Method for Minimizing $f ( \mathbf { x } )$

Given a twice continuously diffrentiable function $f ( \mathbf { x } )$ , and an initial solution $\mathbf { x } ^ { 0 }$ , repeat the following steps to compute a sequence of solutions $\mathbf { x } ^ { 1 }$ ， $\mathbf { x } ^ { 2 }$ ，.... Stop if and when the sequence adequately converges to a solution with $\nabla f ( \mathbf { x } ^ { * } ) = \mathbf { 0 }$

1. Calculate the gradient $\nabla f ( \mathbf { x } ^ { k } )$ and Hessian $\mathbf { H } ( f ( \mathbf { x } ^ { k } ) )$   
2. Solve $\mathbf { H } ( f ( \mathbf { x } ^ { k } ) ) \Delta \mathbf { x } = - \nabla f ( \mathbf { x } ^ { k } )$   
3.Let $\mathbf { x } ^ { k + 1 } = \mathbf { x } ^ { k } + \Delta \mathbf { x }$   
4.Let $k = k + 1$

Newton's method for minimizing $f ( \mathbf { x } )$ can be very effcient, but the method can also fail to converge. As with Newton's method for solving a system of equations, the convergence properties of the algorithm can be improved in practice by modifying the model update step with a line search.

# 9.3.THE GAUSS-NEWTON AND LEVENBERG-MARQUARDTMETHODS FOR SOLVING NONLINEAR LEAST SQUARES PROBLEMS

Newton's method is not directly applicable to most nonlinear regression and inverse problems. We may not have equal numbers of data points and model parameters, there may not be an exact solution to $\mathbf { G } ( \mathbf { m } ) = \mathbf { d }$ or $\mathbf { G } ( \mathbf { m } ) = \mathbf { d }$ may have multiple solutions. Here,we will use a specialized version of Newton's method to minimize a nonlinear least squares problem.

Given a nonlinear system of equations $\mathbf { G } ( \mathbf { m } ) = \mathbf { d }$ ,consider the problem of finding an $n$ -length parameter vector, m, constrained by an $n \cdot$ -length data vector, d, with associated specified data standard deviations. Our goal is to find a set of parameters that best fits the data in the sense of minimizing the 2-norm of the residuals.

As with linear regression, if we assume that the measurement errors are normally distributed, then the maximum likelihood principle leads us to minimizing the sum of squared residuals normalized by their respective standard deviations (2.12). We seek to minimize the weighted residual norm

$$
f ( \mathbf { m } ) = \sum _ { i = 1 } ^ { m } { \bigg ( } { \frac { G ( \mathbf { m } ) _ { i } - d _ { i } } { \sigma _ { i } } } { \bigg ) } ^ { 2 } .
$$

We define the scalar-valued functions

$$
f _ { i } ( \mathbf { m } ) = \frac { G ( \mathbf { m } ) _ { i } - d _ { i } } { \sigma _ { i } } i = 1 , 2 , . . . , m
$$

and the vector-valued function

$$
\mathbf { F ( m ) } = \left[ \begin{array} { c } { f _ { 1 } ( \mathbf { m } ) } \\ { \vdots } \\ { f _ { m } ( \mathbf { m } ) } \end{array} \right] .
$$

Thus

$$
f ( \mathbf { m } ) = \sum _ { i = 1 } ^ { m } f _ { i } ( \mathbf { m } ) ^ { 2 } = \| \mathbf { F } ( \mathbf { m } ) \| _ { 2 } ^ { 2 } .
$$

The gradient of $f ( \mathbf { m } )$ can be writen as the sum of the gradients of the individual terms,

$$
\nabla f ( \mathbf { m } ) = \sum _ { i = 1 } ^ { m } \nabla \big ( f _ { i } ( \mathbf { m } ) ^ { 2 } \big ) .
$$

The elements of the gradient of $f ( \mathbf { m } )$ are

$$
( { \nabla } f ( { \mathbf { m } } ) ) _ { j } = \sum _ { i = 1 } ^ { m } 2 f _ { i } ( { \mathbf { m } } ) ( { \nabla } f _ { i } ( { \mathbf { m } } ) ) _ { j } ,
$$

and the gradient can thus be written in matrix notation as

$$
\nabla f ( \mathbf { m } ) = 2 \mathbf { J } ( \mathbf { m } ) ^ { T } \mathbf { F } ( \mathbf { m } ) ,
$$

where $\mathbf { J } ( \mathbf { m } )$ is the Jacobian

$$
\mathbf { J } ( \mathbf { m } ) = \left[ \begin{array} { c c c } { \frac { \partial f _ { 1 } ( \mathbf { m } ) } { \partial m _ { 1 } } } & { \cdot \mathbf { \nabla } \cdot } & { \frac { \partial f _ { 1 } ( \mathbf { m } ) } { \partial m _ { n } } } \\ { \vdots } & { \ddots } & { \vdots } \\ { \frac { \partial f _ { m } ( \mathbf { m } ) } { \partial m _ { 1 } } } & { \cdot \mathbf { \nabla } \cdot } & { \frac { \partial f _ { m } ( \mathbf { m } ) } { \partial m _ { n } } } \end{array} \right] .
$$

Similarly, we can express the Hessian of $f ( \mathbf { m } )$ using the $f _ { i } ( \mathbf { m } )$ terms to obtain

$$
\begin{array} { l } { { \displaystyle { \bf H } ( f ( { \bf m } ) ) = \sum _ { i = 1 } ^ { m } { \bf H } ( f _ { i } ( { \bf m } ) ^ { 2 } ) } \ ~ } \\ { { \displaystyle ~ = \sum _ { i = 1 } ^ { m } { \bf H } ^ { i } ( { \bf m } ) } , } \end{array}
$$

where $\mathbf { H } ^ { i } ( \mathbf { m } )$ is the Hessian of $f _ { i } ( \mathbf { m } ) ^ { 2 }$

The $j , k$ element of $\mathbf { H } ^ { i } ( \mathbf { m } )$ is

$$
\begin{array} { l } { { \displaystyle { \cal H } _ { j , k } ^ { i } ( { \bf m } ) = \frac { \partial ^ { 2 } ( f _ { i } ( { \bf m } ) ^ { 2 } ) } { \partial m _ { j } \partial m _ { k } } } \ ~ } \\ { { \displaystyle ~ = \frac { \partial } { \partial m _ { j } } \bigg ( 2 f _ { i } ( { \bf m } ) \frac { \partial f _ { i } ( { \bf m } ) } { \partial m _ { k } } \bigg ) } \ ~ } \\ { { \displaystyle ~ = 2 \bigg ( \frac { \partial f _ { i } ( { \bf m } ) } { \partial m _ { j } } \frac { \partial f _ { i } ( { \bf m } ) } { \partial m _ { k } } + f _ { i } ( { \bf m } ) \frac { \partial ^ { 2 } f _ { i } ( { \bf m } ) } { \partial m _ { j } \partial m _ { k } } \bigg ) } . } \end{array}
$$

Thus

$$
\mathbf { H } ( f ( \mathbf { m } ) ) = 2 \mathbf { J } ( \mathbf { m } ) ^ { T } \mathbf { J } ( \mathbf { m } ) + \mathbf { Q } ( \mathbf { m } ) ,
$$

where

$$
\mathbf { Q } ( \mathbf { m } ) = 2 \sum _ { i = 1 } ^ { m } f _ { i } ( \mathbf { m } ) \mathbf { H } ( f _ { i } ( \mathbf { m } ) ) .
$$

In the Gauss-Newton (GN) method, we ignore the $\mathbf { Q } ( \mathbf { m } )$ term in (9.26) and approximate the Hessian as

$$
\mathbf { H } ( f ( \mathbf { m } ) ) \approx 2 \mathbf { J } ( \mathbf { m } ) ^ { T } \mathbf { J } ( \mathbf { m } ) .
$$

In the context of nonlinear regression, we expect that the $f _ { i } ( \mathbf { m } )$ terms will be small as we approach the optimal parameters $\mathbf { m } ^ { * }$ , so that this should be a reasonable approximation in the vicinity of the solution. Conversely, this is not a reasonable approximation for nonlinear least squares problems in which the values of $f _ { i } ( \mathbf { m } )$ can be large.

Implementing Newton's method for minimizing $f ( \mathbf { m } )$ (9.12) using the gradient (9.19)and the approximate Hessian (9.28),and dividing both sides by 2, we obtain

$$
\mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } ) \Delta \mathbf { m } = - \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { F } ( \mathbf { m } ^ { k } ) ,
$$

which provides a formula for solving for successive update steps $\Delta \mathbf { m }$ The $n$ by $n$ matrix $\mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } )$ is symmetric and positive semidefinite. If the matrix is actually positive definite then we can use the Cholesky factorization or another full-rank method to solve the system of equations for $\Delta \mathbf { m }$ However, if the matrix is singular then such straightforward approaches will fail. Although the GN method often works wellin practice, it is based on Newton's method, and can thus fail by converging to a local maximum or saddle point where $\nabla f ( \mathbf { m } ) \approx 0$ , or by not converging at all. An additional point to con-sider in using GN and other such iterative methods is that the algorithm may converge to a local minimum rather than to a global minimum (see Section 9.5).

In the Levenberg-Marquardt (LM) method, the GN method model update equations (9.29) are modified to

$$
( \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } ) + \lambda \mathbf { I } ) \Delta \mathbf { m } = - \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { F } ( \mathbf { m } ^ { k } ) ,
$$

and the positive parameter $\lambda$ is adjusted during the course of iterations to ensure convergence. One important reason for this modification is to ensure that the matrix on the left-hand side of (9.3O) is nonsingular. Since the matrix in this system of equations is symmetric and positive definite,we can use the Cholesky factorization to efficiently solve the system for the model update steps $\delta \mathbf { m }$

For very large values of $\lambda$ ，

$$
\mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } ) + \lambda \mathbf { I } \approx \lambda \mathbf { I } ,
$$

and the solution to (9.30) is

$$
\Delta \mathbf { m } \approx - \frac { 1 } { \lambda } \nabla f ( \mathbf { m } ) .
$$

This is called a steepest-descent step, meaning that the algorithm simply moves down-gradient to most rapidly reduce $f ( \mathbf { m } )$ . The steepest-descent approach provides very slow but certain convergence to a local minimum. Conversely, for very small values of $\lambda$ ,the LM method reverts to the GN method (9.29),which gives potentially fast but uncertain convergence.

A challenge associated with implementing the LM method is determining the optimal value of $\lambda$ . The general strategy is to use small values of $\lambda$ in situations where the GN method is working well, but to increase $\lambda$ when the GN method fails to make progress in reducing the residual norm. A simple approach is to start with a small value of $\lambda$ ,and then adjust it in every iteration. If the LM method leads to a residual norm reduction, then update $\mathbf { m }$ and decrease $\lambda$ by a constant multiplicative factor (e.g.,a factor of 2) before the next iteration. Conversely, if the LM method does not improve the solution,we then increase $\lambda$ by a constant factor and try again,repeating this process until a model update is found that decreases the residual norm. Robust implementations of the LM method use more sophisticated strategies for adjusting $\lambda$ ,but even this simple strategy works surprisingly well.

In practice,a careful LM implementation offers the good performance of the GN method as well as robust convergence properties,and LM is usually the method of choice for smal- to medium-sized nonlinear least squares problems.

Note that although the LM stabilization term λI in (9.3O) resembles expressions used elsewhere (e.g., Chapter 4) for Tikhonov regularization purposes,it does not alter the ultimate model achieved at convergence. The λI term is used to stabilize the solution of the linear system of equations that determines the search direction to be used.Because the λI term is only used as a way to improve the convergence of the algorithm,and does not enter into the residual norm objective function that is being minimized, it does not regularize the nonlinear least squares problem. We discuss the regularization of nonlinear problems in Chapter 10.

# 9.4. STATISTICAL ASPECTS OF NONLINEAR LEAST SQUARES

Recall from Appendix B that if a vector $\mathbf { d }$ has a multivariate normal distribution,and A is an appropriately sized matrix, then Ad also has a multivariate normal distribution with an associated covariance matrix

$$
\operatorname { C o v } ( \mathbf { A } \mathbf { d } ) = \mathbf { A } \operatorname { C o v } ( \mathbf { d } ) \mathbf { A } ^ { T } .
$$

In Chapter 2, we applied this formula to the linear least squares problem for $\mathbf { G m } = \mathbf { d }$ ， which we solved by the normal equations. The resulting formula for $\operatorname { C o v } ( \mathbf { m } )$ was

$$
\begin{array} { r } { \mathrm { C o v } ( \mathbf { m } _ { L _ { 2 } } ) = ( \mathbf { G } ^ { T } \mathbf { G } ) ^ { - 1 } \mathbf { G } ^ { T } \mathrm { C o v } ( \mathbf { d } ) \mathbf { G } ( \mathbf { G } ^ { T } \mathbf { G } ) ^ { - 1 } . } \end{array}
$$

In the simplest case, where $\mathbf { C o v } ( \mathbf { d } ) = \sigma ^ { 2 } \mathbf { I } .$ (9.34) simplified to

$$
\begin{array} { r } { \mathrm { C o v } ( { \bf m } _ { L _ { 2 } } ) = \sigma ^ { 2 } ( { \bf G } ^ { T } { \bf G } ) ^ { - 1 } . } \end{array}
$$

For the nonlinear regression problem，we no longer have a linear relationship between the data and the estimated model parameters,so we cannot assume that the estimated model parameters have a multivariate normal distribution,and cannot use the above formulas. However, we can obtain useful corresponding formulas by linearization if the data errors are not too large.

If small data perturbations result in small model perturbations in a nonlinear system, we can consider a linearization of the misfit function (9.15) about a solution, $\mathbf { m } ^ { * }$ ：

$$
\begin{array} { r } { \mathbf { F ( m ^ { * } + \Delta m ) } \approx \mathbf { F ( m ^ { * } ) } + \mathbf { J ( m ^ { * } ) } \Delta \mathbf { m } . } \end{array}
$$

Under this approximation, there is a linear relationship between changes in $\mathbf { F }$ and changes in the parameters m:

$$
\mathbf { F ( m ^ { * } + \Delta \Delta m ) } - \mathbf { F ( m ^ { * } ) } = \Delta \mathbf { F } \approx \mathbf { J ( m ^ { * } ) } \Delta \mathbf { m } .
$$

To the extent that the residual misfit terms (the elements of $\mathbf { F } ( \mathbf { m } ^ { * } ) )$ are small, the Hessian can be approximated by (9.28). In this case $\mathbf { J } ( \mathbf { m } ^ { * } )$ in nonlinear regression can take the place of $\mathbf { G }$ in linear problems (e.g.， (9.35)） to estimate the covariance of the model parameters. Equation (9.13) incorporates the respective data element standard deviations $\sigma _ { i }$ into the formula for the residual norm $f ( \mathbf { m } )$ ,and explicitly weights the nonlinear constraint equations. $\operatorname { C o v } ( \mathbf { d } )$ , in the case of independent data errors,is thus the identity matrix in such a weighted system. In this case we have

$$
\mathrm { C o v } ( \mathbf { m } ^ { * } ) \approx ( \mathbf { J } ( \mathbf { m } ^ { * } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { * } ) ) ^ { - 1 } .
$$

As in Chapter 2,we can construct a $9 5 \%$ confidence elipsoid for the fitted parameters in terms of this covariance matrix,

$$
( \mathbf { m } - \mathbf { m } ^ { * } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { * } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { * } ) ( \mathbf { m } - \mathbf { m } ^ { * } ) \leq \Delta ^ { 2 } ,
$$

where $\Delta ^ { 2 }$ is the ninety-fifth percentile of a $\chi ^ { 2 }$ distribution with $n$ degrees of freedom. It is important to reiterate that this confidence elipsoid only defines an approximate confidence region because we linearized $\mathbf { F } ( \mathbf { m } )$ in (9.37).

As in Chapter 2,there is an alternative derivation of the $9 5 \%$ confidence region for the fitted parameters in terms of $\chi ^ { 2 } ( \mathbf { m } ) - \chi ^ { 2 } ( \mathbf { m } ^ { * } )$ . If we let

$$
\chi ^ { 2 } ( \mathbf { m } ) = \| \mathbf { F } ( \mathbf { m } ) \| _ { 2 } ^ { 2 } = \mathbf { F } ( \mathbf { m } ) ^ { T } \mathbf { F } ( \mathbf { m } ) ,
$$

then the inequality

$$
\chi ^ { 2 } ( \mathbf { m } ) - \chi ^ { 2 } ( \mathbf { m } ^ { * } ) \leq \Delta ^ { 2 }
$$

defines an approximate $9 5 \%$ confidence region for $\mathbf { m } ^ { * }$ . Because of the nonlinearity in the $\chi ^ { 2 } ( \mathbf { m } )$ function, this $9 5 \%$ confidence region is typically not an elipsoid. Unfortunately, this confidence region is not exact,because this development is still based on the assumption of multivariate normality, and $\mathbf { m } ^ { * }$ , because it is not a linear combination of the data vector elements, wil not in general have a multivariate normal distribution in nonlinear problems.

Should (9.39) or (9.41) be used in practice? If $G ( \mathbf { m } )$ is not too strongly nonlinear, then there should be very little difference between the two confidence region. However, if $G ( \mathbf { m } )$ is more strongly nonlinear, then the difference between the two confidence regions may be large and neither confidence region can really be trusted. In such situations,Monte Carlo methods are a more useful and appropriate way to estimate parameter uncertainty. This is discussed further in Chapter 11.

As with linear regression, it is possible to apply nonlinear regression when the measurement errors are independent and normally distributed and the standard deviations are unknown but assumed to be equal (Section 3.3). We set the $\sigma _ { i }$ to 1 and minimize the sum of squared errors, and define a residual vector,

$$
r _ { i } = G ( \mathbf { m } ^ { * } ) _ { i } - d _ { i } \quad i = 1 , 2 , \ldots , m .
$$

Our estimate of the measurement standard deviation is then

$$
s = \sqrt { \frac { \| \mathbf { r } \| _ { 2 } ^ { 2 } } { m - n } } ,
$$

and the corresponding approximate covariance matrix for the estimated model parameters is

$$
\mathrm { C o v } ( \mathbf { m } ^ { * } ) = s ^ { 2 } ( \mathbf { J } ( \mathbf { m } ^ { * } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { * } ) ) ^ { - 1 } .
$$

Given $\mathbf { m } ^ { * }$ and $\mathrm { C o v } ( \mathbf { m } ^ { * } )$ , we can establish confidence intervals for the model parameters using the methods described in Chapter 2.As with any parameter estimation problem, it is also important to examine the residuals for systematic patterns or deviations from normality. If we have not estimated the measurement standard deviation s from the fitted residuals,then it is also important to test the $\chi ^ { 2 }$ value for goodness of fit and perform an associated $\pmb { p }$ -value test (2.21) if we have normally distributed data errors.The appropriateness of this test will depend on how well the nonlinear model is approximated by the Jacobian linearization for points near the optimal parameter values.

# Example 9.1

A classic method in hydrology for determining the transmissivity and storage coeficient of an aquifer is called the“slug test” [49].

A known volume $Q$ of water (the slug) is injected into a well,and the resulting effects on the head, $h$ ，at an observation well a distance $d$ away from the injection well are observed at various times $t$ ，The change in the head measured at the observation well typically increases rapidly and then decreases more slowly. We wish to determine the dimensionless storage coefficient, $S$ ，and the transmissivity $T$

The mathematical model for the slug test is

$$
h = { \frac { Q } { 4 \pi T t } } e ^ { - d ^ { 2 } S / ( 4 T t ) } .
$$

We know the parameters $Q = 5 0 ~ \mathrm { m } ^ { 3 }$ and $d = 6 0 \mathrm { ~ m ~ }$ ，and the times $t$ at which the head $h$ is measured. Our data are given in Table 9.1,where head measurements are roughly accurate to $0 . 0 1 \mathrm { ~ m ~ }$ $( \sigma _ { i } = 0 . 0 1 \mathrm { ~ m ~ }$ ).

The optimal parameter values are $S = 0 . 0 0 2 0 7$ and $T = 0 . 5 8 5 ~ \mathrm { m } ^ { 2 } / \mathrm { h r }$ .The observed $\chi ^ { 2 }$ value is 2.04, with a corresponding $p$ -value of O.73.Thus this fit passes the $\chi ^ { 2 }$ test. The data points and fitted curve are shown in Figure 9.1.

Using the Jacobian evaluated at the optimal parameter values,we computed an approximate covariance matrix for the fitted parameters. The resulting $9 5 \%$ confidence intervals for $S$ and $T$ are

$$
\begin{array} { l } { S = 0 . 0 0 2 0 7 \pm 0 . 0 0 0 1 2 } \\ { \ } \\ { T = 0 . 5 8 5 \pm 0 . 0 2 9 \ \mathrm { m } ^ { 2 } / \mathrm { h r } . } \end{array}
$$

Table 9.1 Slug Test Data   

<table><tr><td rowspan=1 colspan=1>t (hr)</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>50</td></tr><tr><td rowspan=1 colspan=1>h (m)</td><td rowspan=1 colspan=1>0.72</td><td rowspan=1 colspan=1>0.49</td><td rowspan=1 colspan=1>0.30</td><td rowspan=1 colspan=1>0.20</td><td rowspan=1 colspan=1>0.16</td><td rowspan=1 colspan=1>0.12</td></tr></table>

![](images/db0e7e744ba1fb00ed984b2e88fd3dfb26dbb4355520306cb4636083c7789b7e.jpg)  
Figure 9.1 Data, with one standard deviation error bars,and fitted model for the slug test.

![](images/499f95b17d8fa82c24c1af49970520fff0e2bc2c02bba9aab5e7726579b1e308.jpg)  
Figure 9.2 $\chi ^ { 2 }$ contour plot for the slug test for a wide range of parameters.The small box shows the close-up axis range displayed in Figure 9.3.

A contour plot of the $\chi ^ { 2 }$ surface obtained by varying $S$ and $T$ is shown in Figure 9.2. Note that,unlike our earlier linear regression problems,the contours are not even approximately eliptical because of the nonlinearity of the problem. However, if we zoom into the immediate vicinity of the optimal parameters (Figure 9.3),we find that the $\chi ^ { 2 }$ contours are approximately ellptical at this scale. The approximate ellipticity of the contours indicates that the linear approximation of ${ \bf G } ( { \bf m } )$ around the optimal parameter values is a reasonable approximation for model perturbations in this range.

![](images/124133e810303e726e0c059436e82e18529681e92cd2aac527b5c904276d49e2.jpg)  
Figure 9.3 Close-up $\chi ^ { 2 }$ contour plot for the immediate vicinity of the optimal parameters $\mathbf { m } ^ { * }$ for the slug test example, showing nonlinear $90 \%$ ， $9 5 \%$ (bold), and $9 9 \%$ confidence contours.The nearly elliptical contours are indicative of a approximatelylinear behavior at this scale.Dashed ellipse shows the linearized approximation to the $9 5 \%$ confidence contour calculated using (9 38). Ninety-five percent confidence intervals for the parameters calculated from (9.38)are shown as dashed lines.

# 9.5.IMPLEMENTATION ISSUES

Iterative methods for solving nonlinear problems require the computation of the functions $f _ { i } ( \mathbf { m } )$ and their partial derivatives with respect to the model parameters $m _ { j }$ These partial derivatives in turn depend on the derivatives of the nonlinear $\mathbf { G }$ ：

$$
\frac { \partial f _ { i } ( \mathbf { m } ) } { \partial m _ { j } } = \frac { 1 } { \sigma _ { i } } \frac { \partial \mathbf { G } ( \mathbf { m } ) _ { i } } { \partial m _ { j } } .
$$

In some cases, we have explicit formulas for $\mathbf { G } ( \mathbf { m } )$ and its derivatives. In other cases, $\mathbf { G } ( \mathbf { m } )$ exists only as a black box subroutine that can be called as required to evaluate the function.

When an explicit formula for $\mathbf { G } ( \mathbf { m } )$ is available,and the number of parameters is relatively small, we can differentiate analytically. There also exist automatic differen-tiation software packages that can translate the source code of a program that computes $\mathbf { G } ( \mathbf { m } )$ into a program that computes the derivatives of ${ \bf G } ( { \bf m } )$

Another approach is to use finite differences to approximate the derivatives of ${ \bf G } ( { \bf m } ) _ { i }$ .A simple first-order scheme is to employ the linearization

$$
\frac { \partial G ( \mathbf { m } ) _ { i } } { \partial m _ { j } } \approx \frac { G ( \mathbf { m } + h \mathbf { e } _ { j } ) _ { i } - G ( \mathbf { m } ) _ { i } } { h } ,
$$

where $\mathbf { e } _ { j }$ is the jth standard basis vector,and the scalar $h$ is chosen to be suitably small. However, if $h$ becomes very small, significant round-off error in the numerator of (9.49) may occur. A good rule of thumb is to set $h = \sqrt { \epsilon }$ , where $\epsilon$ is the relative accuracy of the evaluations of ${ \bf G } ( { \bf m } ) _ { i }$ . For example,if the function evaluations are accurate to O.0001, then an appropriate choice of $h$ would be about O.01. Determining the actual accuracy of function evaluations can be diffcult, especially when $\mathbf { G }$ is a black box routine. One useful assessment technique is to plot function values as a parameter of interest is varied over a small range. These plots should be smooth at the scale of $h$ When $\mathbf { G }$ is available only as a black box subroutine that can be called with particular values of $\mathbf { m }$ ，and the source code for the subroutine is not available,then the only available approach is to use finite differences.

In practice, many diffculties in solving nonlinear regression problems can be traced back to incorrect derivative computations. It is thus a good idea to cross-check any available analytical formulas for the derivative with finite-difference approximations. Many software packages for nonlinear regression include options for checking the accuracy of derivative formulas.

A second important issue in the implementation of the GN and LM methods is deciding when to terminate the iterations. We would like to stop when the gradient $\nabla f ( \mathbf { m } )$ is approximately O and $\mathbf { m }$ has stopped changing substantially from one iteration to the next. Because of scaling issues, it is not possible to set an absolute tolerance on $\| \nabla f ( \mathbf { m } ) \| _ { 2 }$ that would be appropriate for all problems. Similarly, it is difficult to pick a single absolute tolerance on $\| \mathbf { m } ^ { \bar { k } + 1 } - \mathbf { m } ^ { k } \| _ { 2 }$ or $| f ( \mathbf { m } ^ { k + 1 } ) - f ( \mathbf { m } ^ { k } ) |$

The following convergence tests have been normalized so that they will work well on a wide variety of problems.We assume that values of $\mathbf { G } ( \mathbf { m } )$ can be calculated with a relative accuracy of $\epsilon$ . To ensure that the gradient of $f ( \mathbf { m } )$ is approximately 0, we require that

$$
\| \nabla f ( \mathbf { m } ^ { k } ) \| _ { 2 } < \sqrt { \epsilon } ( 1 + | f ( \mathbf { m } ^ { k } ) | ) .
$$

To ensure that successive values of $\mathbf { m }$ are close, we require

$$
\begin{array} { r } { \| \mathbf { m } ^ { k } - \mathbf { m } ^ { k - 1 } \| _ { 2 } < \sqrt { \epsilon } ( 1 + \| \mathbf { m } ^ { k } \| _ { 2 } ) . } \end{array}
$$

Finally to make sure that the values of $f ( \mathbf { m } )$ have stopped changing, we require that

$$
| f ( \mathbf { m } ^ { k } ) - f ( \mathbf { m } ^ { k - 1 } ) | < \epsilon ( 1 + | f ( \mathbf { m } ^ { k } ) | ) .
$$

There are a number of additional problems that can arise during the solution of a nonlinear regression problem by the GN or LM methods related to the functional behavior of $f ( \mathbf { m } )$

The first issue is that our methods, because they involve calculation of the Jacobian and the Hessian, assume that $f ( \mathbf { m } )$ is a smooth function. This means not only that $f ( \mathbf { m } )$ must be continuous,but also that its first and second partial derivatives with respect to the parameters must be continuous. Figure 9.4 shows a function that is itself continuous, but has discontinuities in the first derivative at $m = 0 . 2$ and the second derivative at $m = 0 . 5$ . When $\mathbf { G } ( \mathbf { m } )$ is given by an explicit formula, it is usually easy to verify that $f ( \mathbf { m } )$ is smooth, but when $\mathbf { G } ( \mathbf { m } )$ is implemented as a black box routine it may be difficult.

A second issue is that the function $f ( \mathbf { m } )$ may have a “flat bottom.” See Figure 9.5. In such cases, there are many values of $\mathbf { m }$ that come close to fitting the data,and it is difficult to determine the optimal $\mathbf { m } ^ { * }$ . In practice, this condition is seen to occur when $\mathbf { J } ( \mathbf { m } ^ { * } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { * } )$ is nearly singular. Because of this ill-conditioning, computing accurate confidence intervals for the model parameters can be effectively impossible. We will address this difficulty in Chapter 1O by applying regularization.

The final problem that we will consider is that $f ( \mathbf { m } )$ may be nonconvex and therefore have multiple local minimum points. See Figure 9.6. The GN and LM methods are designed to converge to a local minimum, but depending on where we begin the search, there is no way to be certain that such a solution will be a global minimum. Depending on the particular problem, the optimization algorithm might well converge to a locally optimal solution.

Global optimization methods have been developed to deal with this issue [17, 75, 76,140]. Deterministic global optimization procedures can be used on problems with a very small number of variables,while stochastic search procedures can be applied to large-scale problems. Stochastic search procedures can be quite effective in practice, even though they do not find a global optimum with certainty.

However, even a deterministic global optimization procedure is not a panacea. In the context of nonlinear regression, if the nonlinear least squares problem has multiple locally optimal solutions with similar objective function values, then each of these solutions will correspond to a statistically likely solution. We cannot simply report one globally optimal solution as our best estimate and construct confidence intervals using (9.38),because this would mean ignoring other likely solutions. However, if we could show that there is one globally optimal solution and other locally optimal solutions have very small $p .$ -values, then it would be appropriate to report the globally optimal solution and corresponding confidence intervals.

Although a thorough discusson of global optimization is beyond the scope of this book,we will discuss one simple global optimization procedure called the multistart method in the next example. In the multistart method, we randomly generate a large number of initial solutions,and then apply the LM method starting with each of these initial solutions. We then examine the local minimum solutions found by the procedure, and examine ones with acceptable values of $f ( \mathbf { m } )$ . The multistart approach has two important practical advantages. First, by potentially identifying multiple locally optimal solutions,we can determine whether there is more than one statistically likely solution. Second, we can make effective use of the fast convergence of the LM method to find the locally optimal solutions.

# Example 9.2

Consider the problem of fiting a model of two superimposed exponential decay functions characterized by four parameters,

$$
\gamma _ { i } = m _ { 1 } e ^ { m _ { 2 } x _ { i } } + m _ { 3 } x _ { i } e ^ { m _ { 4 } x _ { i } } ,
$$

to a set of observations. The true model parameters are $m _ { 1 } = 1 . 0 , m _ { 2 } = - 0 . 5 , m _ { 3 } = 1 . 0$ ， and $m _ { 4 } = - 0 . 7 5$ ,and the $x _ { i }$ values are 25 evenly spaced points between 1 and 7. We compute corresponding $\gamma _ { i }$ values and add independent normally distributed noise with a standard deviation of O.O1 to obtain a synthetic data set.

We next apply the LM method to solve the problem 2O times,using random initial solutions,with each initial parameter uniformly distributed between $- 1$ and 1. This produces a total of three different locally optimal solutions (Table 9.2).

Solution number 1, with a $\chi ^ { 2 }$ value of approximately 17, has an acceptable $p$ -value of about O.69 for a regression with 21 degrees of freedom. The other two solutions have unreasonably large $\chi ^ { 2 }$ values,and hence much lower $p$ -values.We will thus analyze only the first solution. Figure 9.7 shows the data points with $1 \sigma$ error bars and the fitted curve for solution number 1,and Figure 9.8 shows the corresponding residuals normalized by the data standard deviations.Note that the majority of the residuals are within O.5 standard deviations,with a few residuals as large as 1.9 standard deviations. There is no obvious residual trend as $_ x$ ranges from 1 to 7.

Table 9.2 Locally Optimal Solutions for the Sample Problem   

<table><tr><td>Solution Number</td><td>m1</td><td>m2</td><td>m3</td><td>m4</td><td>x²</td><td>p-value</td></tr><tr><td>1</td><td>0.9874</td><td>-0.5689</td><td>1.0477</td><td>-0.7181</td><td>17.3871</td><td>0.687</td></tr><tr><td>2</td><td>1.4368</td><td>0.1249</td><td>-0.5398</td><td>-0.0167</td><td>40.0649</td><td>0.007</td></tr><tr><td>3</td><td>1.5529</td><td>-0.1924</td><td>-0.1974</td><td>-0.1924</td><td>94.7845</td><td>2 ×10-11</td></tr></table>

![](images/3230c0d69d943d6296c4f12f663fa0b7532622c5334e55940f42d319866a79f0.jpg)  
Figure 9.7 Data points and fitted curve.   
Figure 9.8 Normalized residuals corresponding to Figure 9.7.

Next, we compute the approximate covariance matrix for the model parameters using (9.38). The square roots of the diagonal elements of the covariance matrix are standard deviations for the individual model parameters. These are then used to compute $9 5 \%$ confidence intervals for model parameters. The solution parameters with $9 5 \%$ confidence intervals are

$$
\begin{array} { l } { m _ { 1 } = 0 . 9 8 \pm 0 . 2 2 } \\ { m _ { 2 } = - 0 . 5 7 \pm 0 . 7 7 } \\ { m _ { 3 } = 1 . 0 5 \pm 0 . 5 0 } \\ { m _ { 4 } = - 0 . 7 2 \pm 0 . 2 0 . } \end{array}
$$

The true parameters $( 1 , - 0 . 5 , \ 1$ ，and $- 0 . 7 5 )$ are all covered by these confidence intervals. However, there is a large degree of uncertainty. This is an example of a poorly conditioned nonlinear regresson problem in which the data do not strongly constrain the parameter values.

The correlation matrix provides some insight into the nature of the ill-conditioning in this example by quantifying strong parameter trade-offs. For our preferred solution, the correlation matrix calculated using (9.38) is

$$
\rho = \left[ { \begin{array} { r r r r } { 1 . 0 0 } & { - 0 . 8 4 } & { 0 . 6 8 } & { 0 . 8 9 } \\ { - 0 . 8 4 } & { 1 . 0 0 } & { - 0 . 9 6 } & { - 0 . 9 9 } \\ { 0 . 6 8 } & { - 0 . 9 6 } & { 1 . 0 0 } & { 0 . 9 3 } \\ { 0 . 8 9 } & { - 0 . 9 9 } & { 0 . 9 3 } & { 1 . 0 0 } \end{array} } \right] .
$$

Note the strong positive and negative correlation between pairs of parameters. The high negative correlation between $m _ { 1 }$ and $m _ { 2 }$ tells us that by increasing $m _ { 1 }$ and simultaneously decreasing $m _ { 2 }$ we can obtain a solution that is very nearly as good as our optimal solution. There are also strong negative correlations between $m _ { 2 }$ and $m _ { 3 }$ and between $m _ { 2 }$ and $m _ { 4 }$

# 9.6. EXERCISES

1. Show that (9.29) is equivalent to the normal equations (2.3) when $G ( \mathbf { m } ) = \mathbf { G } \mathbf { m }$ where $\mathbf { G }$ is a matrix of constant coefficients.

2. A recording instrument sampling at $5 0 ~ \mathrm { H z }$ records a noisy sinusoidal voltage signal in a 40-s-long record. The data are to be modeled using

$$
\gamma ( t ) = A \sin ( 2 \pi f _ { 0 } t + \phi ) + c + \sigma \eta ( t )
$$

where $\eta ( t )$ is believed to be unit standard deviation,independent,and normally distributed noise,and $\sigma$ is an unknown standard deviation.Using the data in the MATLAB data file instdata.mat, solve for the parameter $( A , f _ { 0 } , \phi , c )$ ，using the

LM method. Show that it is critical to choose a good initial solution (suitable initial parameters can be found by examining a plot of the time series by eye). Once you are satisfied that you have found a good solution, use it to estimate the noise amplitue $\sigma$ Use your solution and estimate of $\sigma$ to find corresponding covariance and correlation matrices and $9 5 \%$ parameter confidence intervals. Which pair of parameters is most strongly correlated? Are there multiple equally good solutions for this problem?

3. In hydrology, the van Genuchten model is often used to relate the volumetric water content in an unsaturated soil to the head [52]. The model is

$$
\theta ( h ) = \theta _ { r } + \frac { \theta _ { s } - \theta _ { r } } { ( 1 + ( - \alpha h ) ^ { n } ) ^ { ( 1 - 1 / n ) } }
$$

where $\theta _ { s }$ is the volumetric water content at saturation, $\theta _ { r }$ is the residual volumetric water content at a very large negative head, and $\alpha$ and $n$ are two parameters which can be fit to laboratory measurements.

The file vgdata.mat contains measurements for a loam soil at the Bosque del Apache National Wildlife Refuge in New Mexico [68]. Fit the van Genuchten model to the data. The volumetric water content at saturation is $\theta _ { s } = 0 . 4 4$ ,and the residual water content is $\theta _ { r } = 0 . 0 9$ . You may assume that the measurements of $\theta ( h )$ are accurate to about $2 \%$ of the measured values.

You will need to determine appropriate values for $\sigma _ { i }$ , write functions to compute $\theta ( h )$ and its derivatives,and then use the LM method to estimate the parameters. In doing so, you should consider whether or not this problem might have local minima. It will be helpful to know that typical values of $\alpha$ range from about O.001 to 0.02, and typical values of $n$ run from 1 to 10.

4.An alternative version of the LM method stabilizes the GN method by multiplicative damping. Instead of adding λI to the diagonal of $\mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } )$ , this method multi-plies the diagonal ofJ $[ ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } )$ by a factor of $( 1 + \lambda )$ . Show that this method can fail by producing an example in which the modified. $\mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } )$ matrix is singular, no matter how large $\lambda$ becomes.

5.A cluster of 1O small earthquakes occurs in a shallow geothermal reservoir. The field is instrumented with nine seismometers,eight of which are at the surface and one of which is $3 0 0 ~ \mathrm { m }$ down a borehole. The P-wave velocity of the fractured granite medium is thought to be an approximately uniform $2 ~ \mathrm { k m } / \mathrm { s }$ .The station locations (in meters relative to a central origin) are given in Table 9.3 and in the MATLAB data file stmat.mat.

The arrival times of P-waves from the earthquakes are carefully measured at the stations,with an estimated error of approximately $1 ~ \mathrm { m s }$ .The arrival time estimates for each earthquake, $\mathrm { e } _ { i }$ , at each station (in seconds relative to an arbitrary reference), are given in Table 9.4. These data can also be found in the MATLAB data file eqdata.mat.

Table 9.3 Station Locations for the Earthquake Location Problem   

<table><tr><td>Station</td><td>x(m)</td><td>y(m)</td><td>z(m)</td></tr><tr><td>1</td><td>500</td><td>-500</td><td>0</td></tr><tr><td>2</td><td>-500</td><td>-500</td><td>0</td></tr><tr><td>3</td><td>100</td><td>100</td><td>0</td></tr><tr><td>4</td><td>-100</td><td>0</td><td>0</td></tr><tr><td>5</td><td>0</td><td>100</td><td>0</td></tr><tr><td>6</td><td>0</td><td>-100</td><td>0</td></tr><tr><td>7</td><td>0</td><td>-50</td><td>0</td></tr><tr><td>8</td><td>0</td><td>200</td><td>0</td></tr><tr><td>9</td><td>10</td><td>50</td><td>-300</td></tr></table>

Table9.4 Data for the Earthquake Location Problem. Times are in Seconds   

<table><tr><td>Station</td><td>e1</td><td>e2</td><td>e3</td><td>e4</td><td>e5</td></tr><tr><td>1</td><td>0.8423</td><td>1.2729</td><td>0.8164</td><td>1.1745</td><td>1.1954</td></tr><tr><td>2</td><td>0.8680</td><td>1.2970</td><td>0.8429</td><td>1.2009</td><td>1.2238</td></tr><tr><td>3</td><td>0.5826</td><td>1.0095</td><td>0.5524</td><td>0.9177</td><td>0.9326</td></tr><tr><td>4</td><td>0.5975</td><td>1.0274</td><td>0.5677</td><td>0.9312</td><td>0.9496</td></tr><tr><td>5</td><td>0.5802</td><td>1.0093</td><td>0.5484</td><td>0.9145</td><td>0.9313</td></tr><tr><td>6</td><td>0.5988</td><td>1.0263</td><td>0.5693</td><td>0.9316</td><td>0.9480</td></tr><tr><td>7</td><td>0.5857</td><td>1.0141</td><td>0.5563</td><td>0.9195</td><td>0.9351</td></tr><tr><td>8</td><td>0.6017</td><td>1.0319</td><td>0.5748</td><td>0.9362</td><td>0.9555</td></tr><tr><td>9</td><td>0.5266</td><td>0.9553</td><td>0.5118</td><td>0.8533</td><td>0.8870</td></tr><tr><td>Station</td><td>e6</td><td>e7</td><td>e8</td><td>e9</td><td>e10</td></tr><tr><td>1</td><td>0.5361</td><td>0.7633</td><td>0.8865</td><td>1.0838</td><td>0.9413</td></tr><tr><td>2</td><td>0.5640</td><td>0.7878</td><td>0.9120</td><td>1.1114</td><td>0.9654</td></tr><tr><td>3</td><td>0.2812</td><td>0.5078</td><td>0.6154</td><td>0.8164</td><td>0.6835</td></tr><tr><td>4</td><td>0.2953</td><td>0.5213</td><td>0.6360</td><td>0.8339</td><td>0.6982</td></tr><tr><td>5</td><td>0.2795</td><td>0.5045</td><td>0.6138</td><td>0.8144</td><td>0.6833</td></tr><tr><td>6</td><td>0.2967</td><td>0.5205</td><td>0.6347</td><td>0.8336</td><td>0.6958</td></tr><tr><td>7</td><td>0.2841</td><td>0.5095</td><td>0.6215</td><td>0.8211</td><td>0.6857</td></tr><tr><td>8</td><td>0.3025</td><td>0.5275</td><td>0.6394</td><td>0.8400</td><td>0.7020</td></tr><tr><td>9</td><td>0.2115</td><td>0.4448</td><td>0.5837</td><td>0.7792</td><td>0.6157</td></tr></table>

a.Apply the LM method to this data set to estimate least squares locations of the earthquakes.

b.Estimate the uncertainties in $x , \ y , \ z$ (in meters) and origin time (in seconds) for each earthquake using the diagonal elements of the appropriate covariance matrix. Do the earthquake locations follow any discernible trend?

Table 9.5 Data for the Lightning Mapping Array Problem   

<table><tr><td>Station</td><td>t(s)</td><td>x(km)</td><td>y(km)</td><td>z(km)</td></tr><tr><td>1</td><td>0.0922360280</td><td>-24.3471411</td><td>2.14673146</td><td>1.18923667</td></tr><tr><td>2</td><td>0.0921837940</td><td>-12.8746056</td><td>14.5005985</td><td>1.10808551</td></tr><tr><td>3</td><td>0.0922165500</td><td>16.0647214</td><td>-4.41975194</td><td>1.12675062</td></tr><tr><td>4</td><td>0.0921199690</td><td>0.450543748</td><td>30.0267473</td><td>1.06693166</td></tr><tr><td>6</td><td>0.0923199800</td><td>-17.3754105</td><td>-27.1991732</td><td>1.18526730</td></tr><tr><td>7</td><td>0.0922839580</td><td>-44.0424408</td><td>-4.95601205</td><td>1.13775547</td></tr><tr><td>8</td><td>0.0922030460</td><td>-34.6170855</td><td>17.4012873</td><td>1.14296361</td></tr><tr><td>9</td><td>0.0922797660</td><td>17.6625731</td><td>-24.1712580</td><td>1.09097830</td></tr><tr><td>10</td><td>0.0922497250</td><td>0.837203704</td><td>-10.7394229</td><td>1.18219520</td></tr><tr><td>11</td><td>0.0921672710</td><td>4.88218031</td><td>10.5960946</td><td>1.12031719</td></tr><tr><td>12</td><td>0.0921702350</td><td>16.9664920</td><td>9.64835135</td><td>1.09399160</td></tr><tr><td>13</td><td>0.0922357370</td><td>32.6468622</td><td>-13.2199767</td><td>1.01175261</td></tr></table>

6. The Lightning Mapping Array is a portable system that locates the sources of lightning radio-frequency radiation in three spatial dimensions and time [132]. The system measures the arrival times of impulsive radiation events with an uncertainty specified by a standard deviation of $7 \times 1 0 ^ { - 2 } ~ \mu \mathrm { s }$ . Measurements are made at multiple locations, typically in a region 40 to $6 0 \mathrm { k m }$ in diameter.Each station records the peak radiation event in successive $1 0 0 \mathrm { - } \mu \mathrm { s }$ time intervals; from such data,several hundred to over a thousand distinct radiation sources may typically be located per lightning discharge. Example data from the LMA are shown in Table 9.5 and are found in the MATLAB data file lightningdata.mat.

a.Use the arrival times at stations 1,2,4,6,7,8,10,and 13 to find the time and location of the associated source. Assume that radio wave signals travel along straight paths at the speed of light in a vacuum $( 2 . 9 9 7 \times 1 0 ^ { 8 } ~ \mathrm { m } / \mathrm { s } )$ .   
b.A challenge in dealing with the large number of detections from the LMA is to disentangle overlapping signals from multiple events. Locate using subsets of the data set to find the largest subset of the data for nine or more stations that gives a good solution,and compare it to the station subset from part (a).

# 9.7. NOTES AND FURTHER READING

Newton's method is central to the field of optimization [39, 58, 87,88,119],and is, because of its speed, the basis for most methods of nonlinear optimization.A number of modifications to the method are used to ensure convergence to a local minimum of $f ( \mathbf { x } )$ [58,119]. One important difficulty in Newton’s method is that, for very large problems, it may be impractical to store the Hessan matrix. Specialized methods have ben developed for the solution of such large-scale optimization problems [58, 119].

The GN and LM methods are discussed in more detail in [16,58, 119]. Statistical aspects of nonlinear regression are discussed in [7,4O,113]. A more detailed discus-sion of the termination criteria for the LM method described in Section 9.5 can be found in [58]. There are a number of freely available and commercial software packages for nonlinear regression, including GaussFit [82], MINPACK [111], and ODRPACK [18]. Automatic differentiation has applications in many areas of numerical computing, including optimization and numerical solution of ordinary and partial diferential equations. Two books that survey this topic are [34,57]. Global optimization is a large field of research. Some basic references include [17,75,76]. For a survey of global optimization methods in geophysical inversion, see [140].

# Nonlinear Inverse Problems

# Synopsis

The nonlinear regression approaches of Chapter 9 are generalized to problems requiring regularization. The Tikhonov regularization and Occam's inversion approaches are introduced. Seismic tomography and electrical conductivity inversion examples are used to illustrate the application of these methods.Resolution analysis for nonlinear problems is addressed.

# 10.1.REGULARIZING NONLINEAR LEAST SQUARES PROBLEMS

As with linear problems,the nonlinear least squares approaches can run into difficulty with ill-conditioned problems. This typically happens as the number of model parameters grows. Here,we will discuss regularization of nonlinear inverse problems and algorithms for computing a regularized solution to a nonlinear inverse problem.

The basic ideas of Tikhonov regularization can be extended to nonlinear problem. Suppose that we are given a nonlinear discrete inverse problem where an $n \cdot$ -element model m and an $m \cdot$ -element data vector $\mathbf { d }$ are related by a nonlinear system of equations $\mathbf { G } ( \mathbf { m } ) = \mathbf { d }$ .For convenience, we will assume that the m nonlinear constraint equations have been scaled to incorporate the measurement standard deviations $\sigma _ { i }$ . We seek the solution with the smallest seminorm $\| \mathbf { L m } \| _ { 2 }$ that comes sufficiently close to fitting the data vector, where $\mathbf { L }$ is an appropriate roughening matrix (e.g., (4.28)).

We can formulate this problem as

$$
\begin{array} { r l } & { \operatorname* { m i n } \| \mathbf { L m } \| _ { 2 } } \\ & { \| \mathbf { G } ( \mathbf { m } ) - \mathbf { d } \| _ { 2 } \leq \delta . } \end{array}
$$

Note that the form of the problem is virtually identical to that which was considered in the linear case (e.g., (4.25)),with the only difference being that we now have a general function ${ \bf G } ( { \bf m } )$ instead of a matrix-vector multiplication $\mathbf { G m }$ 、As in the linear case, we can reformulate this problem in terms of minimizing the misfit subject to a constraint on $\| \mathbf { L m } \| _ { 2 }$ ，

$$
\begin{array} { r l } & { \operatorname* { m i n } \lVert \mathbf G ( \mathbf { m } ) - \mathbf d \rVert _ { 2 } } \\ & { \qquad \lVert \mathbf { L m } \rVert _ { 2 } \leq \epsilon , } \end{array}
$$

or as a regularized (often referred to as “damped") least squares problem,

$$
\operatorname* { m i n } \| \mathbf G ( \mathbf { m } ) - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf L \mathbf m \| _ { 2 } ^ { 2 } .
$$

All three versions of the regularized least squares problem can be solved by applying standard nonlinear optimization software. In particular, (1O.3) is a nonlinear least squares problem, so we can apply the LM or GN methods to it. Of course,any such approach will still have to deal with the possbility of local minima that are not global minimum points. In some cases, it is possible to show that nonlinear least squares problems are convex,and thus possess only global minima. In other cases we will have to employ multistart or some other global optimization strategy to determine whether there are multiple minima.

To apply the GN method to (10.3), we rewrite it as

$$
\operatorname* { m i n } \left\| { \bf G } ( { \bf m } ) - { \bf d } \right\| _ { 2 } ^ { 2 } .
$$

The Jacobian of (1O.4) for the kth iteration is

$$
\mathbf { K } ( \mathbf { m } ^ { k } ) = \left[ \begin{array} { c } { \mathbf { J } ( \mathbf { m } ^ { k } ) } \\ { \alpha \mathbf { L } } \end{array} \right] ,
$$

where $\mathbf { J } ( \mathbf { m } ^ { k } )$ is the Jacobian of $\mathbf { G } ( \mathbf { m } ^ { k } )$ . A GN model step is obtained by applying (9.29) and solving

$$
{ \bf K } ( { \bf m } ^ { k } ) ^ { T } { \bf K } ( { \bf m } ^ { k } ) \Delta { \bf m } = - { \bf K } ( { \bf m } ^ { k } ) ^ { T } \left[ \begin{array} { c } { { \bf G } ( { \bf m } ^ { k } ) - { \bf d } } \\ { { \alpha { \bf L } { \bf m } ^ { k } } } \end{array} \right] ,
$$

or, combining (10.5)and (10.6),by solving

$$
\left( \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } ) + \alpha ^ { 2 } \mathbf { L } ^ { T } \mathbf { L } \right) \ \Delta \mathbf { m } = - \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } ( \mathbf { G } ( \mathbf { m } ^ { k } ) - \mathbf { d } ) - \alpha ^ { 2 } \mathbf { L } ^ { T } \mathbf { L } \mathbf { m } ^ { k } .
$$

Equation (1O.7) resembles the LM method (9.3O). Note, however, that $\alpha$ in (10.7) now appears in the objective function being minimized (1O.4) and thus introduces regularization. To further stabilize the iterations,as in the LM method,a variable $\lambda \mathbf { I }$ term could be added to the matrix term of the left-hand side of (1O.7) to steer iterative updates toward the direction of steepest descent. This will not be necessary if the explicit regularization of (10.7) sufficiently stabilizes the system of equations.

# Example 10.1

Consider a modified version of the cross-well tomography example from Exercise 4.3. We introduce nonlinearity by employing a more realistic forward model that incorporates ray-path bending due to seismic velocity changes. The two-dimensional velocity structure is parameterized using a 64-element matrix of uniformly spaced slownes nodes on an 8 by 8 grid spanning a $1 6 0 0 \mathrm { m }$ by $1 6 0 0 ~ \mathrm { m }$ region.

We apply an approximate ray-bending technique to estimate refracted ray paths within the slowness model and to estimate travel times and their partial derivatives with respect to the model parameters [167]. Figure 10.1 shows the true velocity model and a corresponding set of 64 ray paths. The true model consists of a background velocity of $2 . 9 \ \mathrm { k m / s }$ with large embedded fast $( + 1 0 \% )$ and slow $( - 1 5 \% )$ Gaussian-shaped anoma-lies. The data set consists of the 64 travel times between each pair of opposing sources and receivers with $N ( 0 , ( 0 . 0 0 1 \mathrm { s } ) ^ { 2 } )$ noise added.

Note that refracted ray paths tend to be“repelled” from low-velocity regions (dark shading) and are,conversely，“attracted’ to high-velocity regions (light shading) in accordance with Fermat’s least-time principle. In practice this effect makes low-velocity regions more difficult to resolve in such studies because they will be less well sampled by ray paths.

A discrete approximation of the two-dimensional Laplacian operator is used to regularize this problem. Iterative GN (1O.7） solutions were obtained for a range of 16 values of $\alpha$ ranging logarithmically from approximately 4.9 to 367. Figure 10.2 shows the suite of solutions after five iterations. An L-curve plot of seminorm versus data misfit is plotted in Figure 1O.3,along with the discrepancy principle value $\delta = 0 . 0 0 1 \cdot \sqrt { 6 4 } = 0 . 0 0 8$ Note that the two most lightly regularized solutions are out of their expected monotonically decreasing residual norm positions on the L-curve. This is because the linearization-based GN method is unable to accurately solve the corre-sponding poorly conditioned least squares systems (1O.7) in these cases. Such solutions could be improved by modifying the system of equations with an LM stabilizing term as described above. The solution best satisfying the discrepancy principle corresponds to $\alpha \approx 3 7$ (Figure 10.4).

![](images/460b7aba91b04de8603d7db1d4e4a4246f6df1351002dd9905c390493685c492.jpg)  
Figure 10.2 Suite of GN (10.7),second-order regularized solutions, ranging from least (upper left) to most (lower right) regularized,and associated $\alpha$ values.The physical dimensions and gray scale are identical to those of Figures 10.1 and 10.4.

![](images/781789a16de3c962ba03e2907bcc5bad8daf3b5afc64bcd7357f3c8750fbfb0e.jpg)  
Figure 10.3 L-curve and corresponding $\alpha$ values for the solutions of Figure 10.2.

Because we know the true model in this example, it is instructive to examine how well the regularized solutions of Figure 10.2 compare to it. Figure 10.5 shows the 2-norm model misfit as a function of $\alpha$ , and demonstrates that the discrepancy principle solution for this problem,and for this particular noise realization,is indeed close to the minimum in $\| \mathbf { m } - \mathbf { m } _ { \mathrm { { t r u e } } } \| _ { 2 }$ . Note that the solution shown in Figure 1O.4 exhibits resolution artifacts that are common in regularized solutions, such as streaking, side lobes,and amplitude under-recovery (see Example 10.3).

![](images/11441e9155b73bf5596297aee18f580070af66784460d5179ea2d807643488fe.jpg)  
Figure 10.4 Best-solution velocity structure $( \mathsf { m } / \mathsf { s } )$ , $\alpha$ selected using the discrepancy principle, $\alpha \approx 3 7$   
Figure 10.5 Model misfit 2-norm as a function of regularization parameter $\alpha _ { \iota }$ ,with preferred model highlighted.

# 10.2.OCCAM'S INVERSION

Occam's inversion is a popular algorithm for nonlinear inversion introduced by Constable,Parker, and Constable [33]. The name refers to the 14th-century philosopher Willam of Ockham, who argued that simpler explanations should always be preferred to more complicated explanations.A similar statement occurs as rule 1 in Newton's “Rules for the Study of Natural Philosophy”[118]. This principle has become known as“Occam's razor."

Occam's inversion uses the discrepancy principle,and searches for the solution that minimizes $\| \mathbf { L m } \| _ { 2 }$ subject to the constraint $\| \mathbf { G } ( \mathbf { m } ) - \mathbf { d } \| _ { 2 } \leq \delta$ . The algorithm is straightforward to implement, requires only the nonlinear forward model $\mathbf { G } ( \mathbf { m } )$ and its Jacobian, and works well in practice.

We assume that our nonlinear inverse problem has been cast in the form of (10.1). The roughening matrix $\mathbf { L }$ can be I to implement zeroth-order Tikhonov regularization,or it can be a finite difference approximation of a first (4.27) or second (4.28) derivative for higher-order regularization. In practice, Occam's inversion is often used on two- or three-dimensional problems where $\mathbf { L }$ is a discrete approximation of the Laplacian operator.

As usual, we will assume that the measurement errors in $\mathbf { d }$ are independent and normally distributed. For convenience, we will also assume that the system of equations $\mathbf { G } ( \mathbf { m } ) = \mathbf { d }$ has been scaled so that the standard deviations $\sigma _ { i }$ are equal.

The basic idea behind Occam's inversion is an iteratively applied local linearization Given a trial model $\mathbf { m } ^ { k }$ ,Taylor's theorem is applied to obtain the local approximation,

$$
\begin{array} { r } { \mathbf G ( \mathbf m ^ { k } + \Delta \mathbf m ) \approx \mathbf G ( \mathbf m ^ { k } ) + \mathbf J ( \mathbf m ^ { k } ) \Delta \mathbf m , } \end{array}
$$

where $\mathbf { J } ( \mathbf { m } ^ { k } )$ is the Jacobian,

$$
\mathbf { J } ( \mathbf { m } ^ { k } ) = \left[ \begin{array} { c c c } { \frac { \partial G _ { 1 } ( \mathbf { m } ^ { k } ) } { \partial m _ { 1 } } } & { \cdot \mathbf { \nabla } \cdot } & { \frac { \partial G _ { 1 } ( \mathbf { m } ^ { k } ) } { m _ { n } } } \\ { \vdots } & { \ddots } & { \vdots } \\ { \frac { \partial G _ { m } ( \mathbf { m } ^ { k } ) } { \partial m _ { 1 } } } & { \cdot \mathbf { \nabla } \cdot } & { \frac { \partial G _ { m } ( \mathbf { m } ^ { k } ) } { \partial m _ { n } } } \end{array} \right] .
$$

Using (10.8), the regularized least squares problem (10.3) becomes

$$
\begin{array} { r } { \operatorname* { m i n } \| \mathbf { G } ( \mathbf { m } ^ { k } ) + \mathbf { J } ( \mathbf { m } ^ { k } ) \Delta \mathbf { m } - \mathbf { d } \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf { L } ( \mathbf { m } ^ { k } + \Delta \mathbf { m } ) \| _ { 2 } ^ { 2 } , } \end{array}
$$

where the variable is $\Delta \mathbf { m }$ and $\mathbf { m } ^ { k }$ is constant. Reformulating this as a problem in which the variable is $\mathbf { m } ^ { k + 1 } = \mathbf { m } ^ { k } + \Delta \mathbf { m }$ , and letting

$$
\hat { \mathbf { d } } ( \mathbf { m } ^ { k } ) = \mathbf { d } - \mathbf { G } ( \mathbf { m } ^ { k } ) + \mathbf { J } ( \mathbf { m } ^ { k } ) \mathbf { m } ^ { k } ,
$$

gives

$$
\operatorname* { m i n } \| \mathbf { J } ( \mathbf { m } ^ { k } ) ( \mathbf { m } ^ { k } + \Delta \mathbf { m } ) - ( \mathbf { d } - \mathbf { G } ( \mathbf { m } ^ { k } ) + \mathbf { J } ( \mathbf { m } ^ { k } ) \mathbf { m } ^ { k } ) \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf { L } ( \mathbf { m } ^ { k } + \Delta \mathbf { m } ) \| _ { 2 } ^ { 2 }
$$

or

$$
\mathrm { m i n } \| \mathbf { J } ( \mathbf { m } ^ { k } ) \mathbf { m } ^ { k + 1 } - \hat { \mathbf { d } } ( \mathbf { m } ^ { k } ) \| _ { 2 } ^ { 2 } + \alpha ^ { 2 } \| \mathbf { L } ( \mathbf { m } ^ { k + 1 } ) \| _ { 2 } ^ { 2 } .
$$

Because $\mathbf { J } ( \mathbf { m } ^ { k } )$ and $\hat { \mathbf { d } } ( \mathbf { m } ^ { k } )$ are constant within a given iteration, (1O.13) is in the form of a regularized linear least squares problem. If the system is of ful rank, the solution is given by

$$
\mathbf { m } ^ { k + 1 } = \mathbf { m } ^ { k } + \Delta \mathbf { m } = \left( \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } ) + \alpha ^ { 2 } \mathbf { L } ^ { T } \mathbf { L } \right) ^ { - 1 } \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \hat { \mathbf { d } } ( \mathbf { m } ^ { k } ) .
$$

Note that this method is similar to the GN method applied to the regularized least squares problem (1O.3) (see Exercise 10.1). The difference is that in Occam's inversion the parameter $\alpha$ is dynamically adjusted so that the solution will not exceed the allowable misfit.At each iteration we pick the largest value of $\alpha$ that keeps the $\chi ^ { 2 }$ value of the solution from exceeding the bound on $\delta$ specified in (1O.1). If this is impossible, we instead pick the value of $\alpha$ that minimizes the $\chi ^ { 2 }$ value. At the end of the procedure, we should have a solution with $\chi ^ { 2 } = \delta ^ { 2 }$ . We can now state the algorithm.

# Algorithm 10.1 Occam's Inversion

Beginning with an initial solution $\mathbf { m } ^ { 0 }$ , repeat the following steps to compute a sequence of solutions $\mathbf { m } ^ { k }$ . Stop if and when the sequence converges to a solution with $\chi ^ { 2 } = \delta ^ { 2 }$

1. Calculate the Jacobian $\mathbf { J } ( \mathbf { m } ^ { k } )$ and the vector $\hat { \mathbf { d } } ( \mathbf { m } ^ { k } )$

2. Calculate updated models corresponding to a range of regularization parameter values, $\alpha$ ，

$$
\mathbf { m } ^ { k + 1 } = \left( \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \mathbf { J } ( \mathbf { m } ^ { k } ) + \alpha ^ { 2 } \mathbf { L } ^ { T } \mathbf { L } \right) ^ { - 1 } \mathbf { J } ( \mathbf { m } ^ { k } ) ^ { T } \hat { \mathbf { d } } ( \mathbf { m } ^ { k } ) .
$$

3. Choose the particular $\mathbf { m } ^ { k + 1 }$ with the largest value of $\alpha$ such that $\chi ^ { 2 } ( \mathbf { m } ^ { k + 1 } ) \leq \delta ^ { 2 }$ If no such value exists, then use the value of $\alpha$ that minimizes $\chi ^ { 2 } ( \mathbf { m } ^ { k + 1 } )$

4.Let $k = k + 1$

# Example 10.2

We will consider the problem of estimating subsurface electrical conductivities from above-ground electromagnetic induction measurements. The instrument used in this example is the Geonics EM-38 ground conductivity meter. A description of the instrument and the mathematical model of its response can be found in [69]. The mathematical model is complicated, but we will treat it as a black box,and concentrate on the inverse problem.

Measurements are taken at heights of O,10,20,30,40, 50,75,100,and $1 5 0 \mathrm { c m }$ above the surface,with the coils oriented in both the vertical and horizontal orientations. There are a total of 18 observations (Table 10.1). We will assume measurement standard deviations of $0 . 1 ~ \mathrm { m S / m }$

We discretize the subsurface electrical conductivity profile into 1O- and $2 0 \mathrm { - c m }$ thick layers and a semi-infinite layer below $2 ~ \mathrm { m }$ ， giving us 11 parameters to estimate. The forward problem function $\mathbf { G } ( \mathbf { m } )$ is available to us as a subroutine. Since we do not have simple formulas for $\mathbf { G } ( \mathbf { m } )$ , we cannot write down analytic expressions for the elements of the Jacobian. However, we can use finite difference approximations to estimate the necessary partial derivatives.

We first apply the LM method to estimate unregularized model parameters. After 50 iterations, the LM method produced the model shown in Figure 1O.6. The $\chi ^ { 2 }$ value for this model is 9.62 and there are $1 8 - 1 1 = 7$ degrees of freedom,so the model actually fits the data reasonably well. However, the least squares problem is very badly conditioned, with a condition number for $\mathbf { J } ^ { T } \mathbf { J }$ of approximately $2 \times 1 0 ^ { 1 7 }$ . Furthermore, the resulting model is unrealistic because it includes negative electrical conductivities and exhibits the high amplitudes and high-frequency oscillations that are characteristic of under-regularized solutions to inverse problems.

Table 10.1 Data for the EM-38 Example   

<table><tr><td>Height (cm) EMV (mS/m)</td></tr><tr><td>0 134.5 117.4</td></tr><tr><td>10 129.0 97.7</td></tr><tr><td>20 120.5 81.7</td></tr><tr><td>30 110.5 69.2</td></tr><tr><td>40 100.5 59.6</td></tr><tr><td>50 90.8 51.8</td></tr><tr><td>75 70.9 38.2</td></tr><tr><td>100 56.8 29.8</td></tr><tr><td>150 38.5 19.9</td></tr></table>

![](images/d14e166747026804831cf6592c173d886305751d84f50f449bd996d8fab05298.jpg)  
Figure 10.6 LM solution.

![](images/427bb5de9e5bd10eff83d3b63a8b6fef1edf635817520480d557c5f03aa22182.jpg)  
Figure 10.7 Occam's inversion solution.

We next apply Occam's inversion with second-order regularization and a discrepancy principle value of $\delta = 0 . 1 \cdot { \sqrt { 1 8 } } \approx 0 . 4 2 4$ The resulting model is shown in Figure 10.7, and Figure 1O.8 shows the true model. The Occam's inversion method provides a fairly good reproduction of the true model.

![](images/04a1e45649bf7916b075e1ef35e86c8f75761e531973b403747613e4268c2f85.jpg)  
Figure 10.8 True model.

# 10.3.MODEL RESOLUTION IN NONLINEAR INVERSE PROBLEMS

We introduced the concept of model resolution in Chapter 3 (see(3.63)) by expressing the generalized inverse solution for a linear problem as

$$
\mathbf { m } = \mathbf { R } _ { m } \mathbf { m } _ { \mathrm { t r u e } } = \mathbf { G } ^ { \dagger } \mathbf { G } \mathbf { m } _ { \mathrm { t r u e } }
$$

where $\mathbf { G }$ is a (forward problem) matrix that produces data from a model, $\mathbf { G } ^ { \dagger }$ is the generalized inverse matrix used to recover a model from data,and $\mathbf { m }$ and $\mathbf { m _ { \mathrm { t r u e } } }$ are the recovered and true models, respectively. In a linear problem, the action of mapping a model to data and then back to a recovered model can be completely characterized by the model resolution matrix $\mathbf { R } _ { m } = \mathbf { G } ^ { \dagger } \mathbf { G }$ in (10.16). In Chapter 4 we saw that this concept could easily be extended to Tikhonov regularization (4.2O), by substituting the corresponding Tikhonov inverse matrix, $\mathbf { G } ^ { \sharp }$ ,for $\mathbf { G } ^ { \dagger }$ in (10.16).

We can recast (10.16) for nonlinear problems as

$$
\mathbf { m } = G ^ { - 1 } ( G ( \mathbf { m } _ { \mathrm { t r u e } } ) )
$$

where $G ^ { - 1 }$ and $G$ are inverse and forward operators, respectively. However, the combined action of the forward and inverse operations is not representable as a matrix, such as $\mathbf { R } _ { m }$ in (1O.17),because the forward operator is a nonlinear function or algorithm, and the inverse operator is typically realized with an iterative method based on stepwise linearization, such as GN or Occam's inversion.Furthermore,model resolution for a nonlinear inversion will not only depend on the physics, model parameterization, and data collection specifics,as was the case for linear problems, but may furthermore depend on the choice of starting model used in the solution algorithm, chosen convergence criteria,and possibly on the existence of multiple equally good solutions. Finally, as with linear methods, nonlinear model resolution wil depend on the level and nature of the imposed regularization.

Because of these complexities, nonlinear resolution is typically analyzed using resolution tests. In seismic tomography, for example, it is common to evaluate the effects of nonideal resolution by generating noise-free synthetic data from a spike, checkerboard,or other test model using an identical source and receiver geometry as for the actual data in the problem of interest.A model is then recovered using the identical inverse methodology as was used for the actual data,and is compared to the test model to evaluate inversion artifacts. If there are specific features of the true model that will affect the resolution,such as a known strong velocity gradient with depth in seismic problems that significantly affects the curvature of the ray paths, those features should also be incorporated into the resolution test model. Because the problem is nonlinear, resolution analysis results will also potentially be dependent on test model amplitudes. A second resolution analysis strategy, sometimes referred to as a “squeeze” test, restricts the freedom of the model in regions that are suspected to be unnecessary or marginal for achieving an acceptable fit to the data. One example would be to modify the regularization constraints to strongly penalize model variations in the deeper part of a tomographic model to assess whether an acceptable data fit can still be achieved when structure is predominantly restricted to shallower depths.

# Example 10.3

Revisiting Example 1O.1,we calculate noise-free synthetic data for a checkerboard velocity structure,using an identical starting model and ray-path end points. The checkerboard model (Figure 10.9) consists of an 8 by 8 node $2 . 9 ~ \mathrm { k m / s }$ background model with alternating $10 \%$ variations for the 36 interior blocks. Inverting these data using the identical methodology as in Example 1O.1 for the same regularization con-straints and range of regularization parameters, we obtain the suite of models shown in Figure 1O.1O.For lower levels of regularization, the checkerboard is more apparent,while for higher levels, the horizontally varying velocity structure is substantially smoothed out. For the level of regularization chosen from the discrepancy principle for Example 10.1, $\alpha \approx 3 7$ ，we note substantial smearing that makes it diffcult to discern the full checkerboard pattern, indicating that structural variations of this character and spatial scale will be dificult to recover in some parts of the model without additional data. If we did not know the true model in Example 10.1, this test would helpfully show that we would expect significant horizontal smearing for the inversion result shown in Figure 1O.4,and that the true model anomalies are thus not necessarily horizontally elongated.

![](images/7a339c5f271d694fd5809d6ec91d89a2b7989c2d839aaeb915b5fbc56ae590f2.jpg)  
Figure 10.9 Checkerboard test model and ray paths for the cross-well tomography problem of Example 10.1.   
Figure 10.10 Suite of recovered models for a range of regularization parameter values (same as in Figure 10.2) for the checkerboard test model of Figure 10.9.

# 10.4.EXERCISES

1. Show that, for a given value of $\alpha$ , the GN (10.7) and Occam's inversion model (10.14) update steps are mathematically equivalent.

2.Recal Example 1.5,in which we had gravity anomaly observations above a density perturbation of variable depth $m ( x )$ , and fixed density $\Delta \rho$ . Use Occam's inversion to solve an instance of this inverse problem. Consider a gravity anomaly along a $1 \mathrm { - k m }$ section,with observations taken every $5 0 \textrm { m }$ ，and density perturbation of $\Delta \rho =$ $2 0 0 ~ \mathrm { k g } / \mathrm { m } ^ { 3 }$ $( 0 . 2 ~ \mathrm { g } / \mathrm { c m } ^ { 3 } )$ . The perturbation is expected to be at a depth of roughly $2 0 0 ~ \mathrm { m }$

The MATLAB data file gravprob.mat contains a vector $\mathbf { x }$ of observation locations. Use the same coordinates for your discretization of the model. The vector obs contains the actual observations.Assume that the observations are accurate to about $1 . 0 \times 1 0 ^ { - 1 2 }$

a.Derive a formula for the elements of the Jacobian.   
b. Write MATLAB routines to compute the model predictions and the Jacobian for this problem.   
c.Use the supplied implementation of Occam's inversion from Example 10.2 to solve the inverse problem with second-order regularization.   
d.Discuss your results. What features in the inverse solution appear to be real? What is the resolution of your solution? Were there any difficulties with local minimum points?   
e. What would happen if the true density perturbation was instead at a depth of about $1 0 0 0 ~ \mathrm { { m } ? }$

3.Apply the GN method with explicit regularization to the EM inversion problem by modifying the MATLAB code from Example 10.2. Compare your solution with the solution obtained by Occam's inversion. Which method required more computational effort?

4. Apply Occam's inversion to a cross-well, bent-ray tomography problem with identical geometry to Example 1O.1. Use the example subroutine getj.m to forward model the travel times,calculate the Jacobian,and implement second-order regularization. Travel-time data and subroutine control parameters are contained in the MATLAB data file benddata.mat. Start with the uniform $2 9 0 0 \mathrm { m / s }$ velocity 8 by 8 node initial velocity model in benddata.mat,and assume independent and normally distributed data errors with $\sigma = 0 . 0 0 1 ~ \mathrm { m s }$

Hint: A search range of $\alpha ^ { 2 }$ between 10 and $1 0 ^ { 5 }$ is appropriate for this problem. MATLAB code for generating a second-order roughening matrix that approximates a two-dimensional Laplacian operator can be found in makerough.m.

# 10.5.NOTES AND FURTHER READING

In inverse problems with a large number of parameters, the most difficult computational problem is often computing derivatives of $\mathbf { G } ( \mathbf { m } )$ with respect to the model parameters, often referred to as Frechet derivatives [1O7]. Computation of analytic formulas is commonly impractical. Finite difference estimates require computational effort, which increases with the number of parameters and may become impractical for large problems. A promising technique for calculating Frechet derivatives is the adjoint approach [46, 154,165],which is likely to see increasing use in large problems as forward modeling capabilities advance. An alternative approach involves using the discretized differential equation as a set of constraints to be added to the nonlinear least squares problem [15].

For large-scale problems, it may be impractical to use direct factorization to solve the systems of equations (10.7) or (10.14) involved in computing the GN or Occam step. One approach in this case is to use an iterative method such as conjugate gradients to solve the linear systems of equations [58]. The conjugate gradient method can also be extended to minimize the nonlinear objective function directly [58, 142].

# Bayesian Methods

# Synopsis

Following a review of the classical least squares approach to solving inverse problems, we introduce the Bayesian approach,which treats the model as a random variable with a probability distribution that we seek to estimate.A prior distribution for the model parameters is combined with the data to produce a posterior distribution for the model parameters. In special cases, the Bayesian approach produces solutions that are equivalent to the least squares, maximum likelihood,and Tikhonov regularization solutions. Several examples of the Bayesian approach are presented. Markov Chain Monte Carlo methods for sampling from the posterior distribution are presented and demonstrated.

# 11.1.REVIEW OF THE CLASSICAL APPROACH

In the classical approach to parameter estimation and inverse problems with discrete data and models, we begin with a mathematical model of the form $\mathbf { G m } = \mathbf { d }$ in the linear case or $G ( \mathbf { m } ) = \mathbf { d }$ in the nonlinear case. We assume that there exists a true model, $\mathbf { m } _ { \mathrm { t r u e } }$ ， and a true data set, ${ \bf d } _ { \mathrm { t r u e } }$ ，such that $\mathbf { G m } _ { \mathrm { t r u e } } = \mathbf { d } _ { \mathrm { t r u e } }$ . We acquire an actual data set, $\mathbf { d } .$ which is generally the sum of ${ \bf d } _ { \mathrm { t r u e } }$ and measurement noise. Our goal is to recover $\mathbf { m _ { \mathrm { t r u e } } }$ from the noisy data.

For well-conditioned linear problems,under the assumption of independent and normally distributed data errors, the theory is well developed. In Chapter 2 it was shown that the maximum likelihood principle leads to the least squares solution, which is found by minimizing the 2-norm of the residual, $\| \mathbf { G m } - \mathbf { d } \| _ { 2 }$ . Since there is noise in the data,we should expect some misfit between the data predictions of the forward model and the data,so that observed values of the square of the 2-norm of the inverse standard deviation-weighted residual, $\chi _ { \mathrm { o b s } } ^ { 2 }$ ，will not typically be zero. We saw that the $\chi ^ { 2 }$ distribution can be used to test the goodness-of-fit of a least squares solution. We showed that the least squares solution, ${ \bf { m } } _ { L _ { 2 } }$ , is an unbiased estimate of $\mathbf { m _ { \mathrm { t r u e } } }$ . We were also able to compute a covariance matrix for the estimated parameters

$$
\mathrm { C o v } ( { \bf m } _ { L _ { 2 } } ) = ( { \bf G } ^ { T } { \bf G } ) ^ { - 1 } { \bf G } ^ { T } \mathrm { C o v } ( { \bf d } ) { \bf G } ( { \bf G } ^ { T } { \bf G } ) ^ { - 1 }
$$

to compute confidence intervals for and correlations between the estimated parameters.

This approach works very wellfor linear regression problems where the least squares problem is well-conditioned. We found, however, that in many cases the least squares problem is not well-conditioned. In such situations, the set of solutions that adequately fits the data is large and diverse,and commonly contains physically unreasonable models.

In Chapters 4 through 8,we discussed a number of approaches to regularizing the least squares problem. These approaches pick a single “best” solution out of those that adequately fit the data, based on a preference for what sort of model features constitute a good solution. Zeroth-order Tikhonov regularization selects the model that minimizes the model 2-norm $\| \mathbf { m } \| _ { 2 }$ subject to the residual norm constraint, $\| \mathbf { G m } - \mathbf { d } \| _ { 2 } < \delta$ ， while higher-order Tikhonov regularization selects the model that minimizes a model seminorm $\| \mathbf { L m } \| _ { 2 }$ subject to $\| \mathbf { G m } - \mathbf { d } \| _ { 2 } < \delta$ . We introduced $L _ { 1 }$ regularization and the related technique of total variation regularization which are now widely used in compressive sensing.

For relatively small linear problems， straightforward, insightful,and robust computation of regularized solutions can be performed with the help of singular value decomposition (SVD). For large sparse linear problems, iterative methods such as conjugate gradient least squares (CGLS) or LSQR are widely used.

For nonlinear problems,as discussed in Chapters 9 and 1O, the Gauss-Newton, Levenberg-Marquardt,or Occam's inversion methods can be used to find local minima of the nonlinear least squares problem. We showed how approximate confidence intervals for the fitted parameters can be obtained by linearizing the nonlinear model around the best fit parameters. As in linear inverse problems, the nonlinear least squares problem can be badly conditioned in which case regularization may be needed to obtain a stable solution.

Unfortunately nonlinear problems may have a large number of local minimum solutions,and finding the global minimum can be diffcult. Furthermore, if there are several local minimum solutions with acceptable data fits, then it may be difficult to select a single“best” solution.

How can we more generally justify selecting one solution from the set of models that adequately fit the data? One justification is Occam's razor, which is the philosophy that when we have several different hypotheses to consider,we should select the simplest. Solutions selected by regularization are in some sense the simplest models that fit the data. However, this approach is not by itself entirely satisfactory because different choices of the regularization term used in obtaining regularized solutions can result in very different models,and the specific choice of regularization may be subjective.

Recall from Chapter 4 (e.g., Example 4.3) that once we have regularized a least squares problem,we lose the ability to obtain statistically useful confidence intervals for the parameters because regularization introduces bias. In particular, the expected value of the regularized solution is not generally equal to the true model. In practice this regularization bias is often much more significant than the effect of noise in the data.Bounds on the error in Tikhonov regularized solution error were discussed in Section 4.8, but these estimates require knowledge of the true model that is typically not available in practice.

# 11.2.THE BAYESIAN APPROACH

The Bayesian approach is named after Thomas Bayes,an 18th-century pioneer in probability theory. The methodology is based on philosophically different ideas than we have considered so far.However, as we wil see, it frequently results in similar solutions.

The most fundamental difference between the classical and Bayesian approaches is in the conceptualization of the solution. In the classical approach, there is a specifc but unknown model $\mathbf { m _ { \mathrm { t r u e } } }$ that we would like to uncover. In the Bayesian approach the model is not deterministic, but is rather a random variable,and the solution takes the form of a probability distribution for the model parameters called the posterior distribution. Once we have this probability distribution, we can use it to answer probabilistic questions about the model, such as “What is the probability that $m 5$ is less than $1 ? ^ { \dag }$ In the classical approach such questions do not make sense, since the true model that we seek is not a random variable.

A second very important difference between the classical and Bayesian approaches is that the Bayesian approach naturally incorporates prior information about the solution, ranging from hard additional constraints to experience-based intuition. This information is expressed mathematically as a prior distribution for the model. Once data have been collected, they are combined with the prior distribution using Bayes' theorem (B.54) to produce the desired posterior distribution for the model parameters.

If no other information is available, then under the principle of indifference, we may alternatively pick a prior distribution where all model parameter values have equal likelihood. Such a prior distribution is said to be uninformative.

It should be pointed out that, in the common case where the model parameters are contained in the range $( - \infty , \infty )$ , the uninformative prior is not a proper probability distribution. This is because a probability density function $f ( x )$ does not exist which satisfies (B.4) so that

$$
\intop _ { - \infty } ^ { \infty } f ( x ) \ d x = 1
$$

and $f ( x )$ is constant.In practice, the use of this improper prior distribution in Bayesian methods can nevertheless be justified because the resulting posterior distribution for the model is a proper distribution.

One of the main objections to the Bayesian approach is that the method is “unscientific” because it allows the analyst to incorporate subjective judgments into the model that are not solely based on the data.Proponents of the approach rejoin that there are also subjective aspects to the classical approach embodied in the choice of regularization biases,and furthermore, that one is free to choose an uninformative prior distribution.

Here, we denote the prior distribution by $p ( \mathbf { m } )$ , and assume that we can compute the conditional probability distribution, $f ( \mathbf { d } | \mathbf { m } )$ , that, given a particular model, correspond-ing data,d, will be observed. Given a prior distribution,we then seek the conditional (posterior) distribution of the model parameter(s) given the data. We will denote this posterior probability distribution for the model parameters by $q ( \mathbf { m } | \mathbf { d } )$ .Bayes’theorem relates the prior and posterior distributions in a way that makes the computation of $q ( \mathbf { m } | \mathbf { d } )$ possible,and can be stated as follows.

# Theorem 11.1

$$
q ( \mathbf { m } | \mathbf { d } ) = \frac { f ( \mathbf { d } | \mathbf { m } ) _ { P } ( \mathbf { m } ) } { c }
$$

where

$$
c = \int _ { \mathrm { { a l l } } \mathrm { { m o d e l s } } } \ f ( \mathbf { d } | \mathbf { m } ) p ( \mathbf { m } ) d \mathbf { m } .
$$

Note that the constant $c$ in (11.3） simply normalizes the conditional distribution $q ( \mathbf { m } | \mathbf { d } )$ so that its integral in model space is one.

For some purposes, knowing the normalization constant, $c$ ，is not necessry. For example, we can compare two models $\hat { \mathbf { m } }$ and $\bar { \bf m }$ by computing the likelihood ratio:

$$
\frac { q ( \hat { \mathbf { m } } | \mathbf { d } ) } { q ( \bar { \mathbf { m } } | \mathbf { d } ) } = \frac { f ( \mathbf { d } | \hat { \mathbf { m } } ) p ( \hat { \mathbf { m } } ) } { f ( \mathbf { d } | \bar { \mathbf { m } } ) p ( \bar { \mathbf { m } } ) } .
$$

A very small likelihood ratio would indicate that the model $\bar { \bf m }$ is far more likely than the model $\hat { \mathbf { m } }$ Because $c$ is not always needed, (11.3) is often written as a statement of proportionality,

$$
q ( \mathbf { m } | \mathbf { d } ) \propto f ( \mathbf { d } | \mathbf { m } ) p ( \mathbf { m } ) .
$$

However, there are many other situations in which knowing $c$ in (11.3) is required. In particular, $c$ is required to compute any posterior probabilities and to compute the expected value and variance of the posterior distribution.

It is important to re-emphasize that the probability distribution $q ( \mathbf { m } | \mathbf { d } )$ does not provide a single model that we can consider to be the“answer.” However, in cases where we want to single out a representative model, it may be appropriate to identify the one corresponding to the largest value of $q ( \mathbf { m } | \mathbf { d } )$ . This model is referred to as the maximum a posteriori (MAP) model. Another possibility is to select the mean of the posterior distribution. In situations where the posterior distribution is normal, the MAP and posterior mean models will be identical.

In general, the computation of a posterior distribution using (11.3) can be difficult. The chief difficulty lies in evaluating the integral in (11.4). This integral often has very high dimensionality, and numerical integration techniques may thus be computationally daunting.

Fortunately, there are a number of useful special cases in which the computation of the posterior distribution is greatly simplified. One simplification occurs when the prior distribution $p ( \mathbf { m } )$ is uninformative, in which case (11.6) simplifies to

$$
q ( \mathbf { m } | \mathbf { d } ) \propto f ( \mathbf { d } | \mathbf { m } ) ,
$$

and the posterior distribution is precisely the likelihood function, $L ( \mathbf { m } | \mathbf { d } )$ . Under the maximum likelihood principle,we would select the model $\mathbf { m } _ { \mathrm { M L } }$ that maximizes $L ( \mathbf { m } | \mathbf { d } )$ ,which is the MAP model.

A further simplification occurs when data noise elements are independent and normally distributed with standard deviation $\sigma$ . Because the data errors are independent, we can write the likelihood function as

$$
L ( \mathbf { m } | \mathbf { d } ) = f ( \mathbf { d } | \mathbf { m } ) = f ( d _ { 1 } | \mathbf { m } ) \cdot f ( d _ { 2 } | \mathbf { m } ) \cdot \cdot \cdot f ( d _ { n } | \mathbf { m } ) .
$$

If the data points $d _ { i }$ are normally distributed with expected values given by the (linear or nonlinear) operation $( G ( \mathbf { m } ) ) _ { i }$ ,and each has standard deviation $\sigma$ , we can write

$$
f ( d _ { i } | { \bf m } ) = \frac { 1 } { \sigma \sqrt { 2 \pi } } e ^ { - \frac { ( ( G ( { \bf m } ) ) _ { i } - d _ { i } ) ^ { 2 } } { 2 \sigma ^ { 2 } } }
$$

and

$$
L ( \mathbf { m } | \mathbf { d } ) = \left( \frac { 1 } { \sigma \sqrt { 2 \pi } } \right) ^ { m } e ^ { - \sum _ { i = 1 } ^ { m } \frac { ( ( G ( \mathbf { m } ) ) _ { i } - d _ { i } ) ^ { 2 } } { 2 \sigma ^ { 2 } } } .
$$

We can maximize (11.1O) by maximizing the exponent or equivalently minimizing the negative of the exponent.

$$
\operatorname* { m i n } \ \sum _ { i = 1 } ^ { m } \frac { ( ( G ( \mathbf { m } ) ) _ { i } - d _ { i } ) ^ { 2 } } { 2 \sigma ^ { 2 } } .
$$

This is a weighted least squares problem. Thus we have shown that when we have independent and normally distributed measurement errors and we use an uninformative prior, the MAP solution is the least squares solution.

# Example 11.1

Consider a very simple parameter estimation problem where we perform repeated weighings of a microscopic object to determine its mass in micrograms. The measurement erors are normally distributed with zero mean and standard deviation $\sigma = 1 ~ { \mu \mathrm { g } }$ Our goal is to estimate the mass of the object.

For the specified normally distributed and zero mean measurement error, the probability density function for a measurement $d$ given $m$ is

$$
f ( d | m ) = \frac { 1 } { \sqrt { 2 \pi } } e ^ { - ( m - d ) ^ { 2 } / 2 } .
$$

Suppose that we weigh the mass once and obtain a measurement of $d _ { 1 } = 1 0 . 3 ~ \mu \mathrm { g }$ What do we now know about m? For an uninformative prior, (11.7) gives

$$
q ( m | d _ { 1 } = 1 0 . 3 ) \propto f ( 1 0 . 3 | m ) = \frac { 1 } { \sqrt { 2 \pi } } e ^ { - ( m - 1 0 . 3 ) ^ { 2 } / 2 } .
$$

Because (11.13) is itself a normal probability distribution, the constant of proportionality in (11.3) is 1,and the posterior distribution for the mass in micrograms (Figure 11.1) is therefore

$$
q ( m | d _ { 1 } = 1 0 . 3 ) = \frac { 1 } { \sqrt { 2 \pi } } e ^ { - ( m - 1 0 . 3 ) ^ { 2 } / 2 } .
$$

Next, suppose that we obtain a second statistically independent measurement of $d _ { 2 } =$ $1 0 . 1 ~ \mu \mathrm { g }$ . We can then use the distribution (11.14) estimated from the first measurement

![](images/678047192b58381d1c3d2a8c78b36386dc0ccda4caa119a499685c0d57704ed9.jpg)  
Figure 11.1 Posterior distribution $q ( m | d _ { 1 } = 1 0 . 3 \mu \mathrm { g } )$ , uninformative prior.

as an informative prior distribution to compute a revised posterior distribution:

$$
\begin{array} { c } { { q ( m | d _ { 1 } = 1 0 . 3 , d _ { 2 } = 1 0 . 1 ) \propto f ( d _ { 2 } = 1 0 . 1 | m ) q ( m | d _ { 1 } = 1 0 . 3 ) } } \\ { { { } } } \\ { { { } = { \displaystyle { \frac { 1 } { \sqrt { 2 \pi } } e ^ { - ( m - 1 0 . 1 ) ^ { 2 } / 2 } \frac { 1 } { \sqrt { 2 \pi } } e ^ { - ( m - 1 0 . 3 ) ^ { 2 } / 2 } } } . } } \end{array}
$$

Combining the exponents and absorbing the $1 / \sqrt { 2 \pi }$ factors into the constant of proportionality gives

$$
q ( m | d _ { 1 } = 1 0 . 3 , d _ { 2 } = 1 0 . 1 ) \propto e ^ { - ( ( m - 1 0 . 3 ) ^ { 2 } + ( m - 1 0 . 1 ) ^ { 2 } ) / 2 } .
$$

Finally, we can simplify the exponent by combining terms and completing the square to obtain

$$
( m - 1 0 . 3 ) ^ { 2 } + ( m - 1 0 . 1 ) ^ { 2 } = 2 ( m - 1 0 . 2 ) ^ { 2 } + 0 . 0 2 .
$$

Thus,

$$
q ( m | d _ { 1 } = 1 0 . 3 ~ \mu \mathrm { g } , ~ d _ { 2 } = 1 0 . 1 ) \propto e ^ { - ( 2 ( m - 1 0 . 2 ) ^ { 2 } + 0 . 0 2 ) / 2 } .
$$

The constant $e ^ { - 0 . 0 2 / 2 }$ caneabsorbeditothestantofproportioalitygiving

$$
q ( m | d _ { 1 } = 1 0 . 3 , d _ { 2 } = 1 0 . 1 ) \propto e ^ { - ( 1 0 . 2 - m ) ^ { 2 } } .
$$

Normalizing (11.19) gives a normal posterior distribution

$$
q ( m | d _ { 1 } = 1 0 . 3 , d _ { 2 } = 1 0 . 1 ) = \frac { 1 } { ( 1 / \sqrt { 2 } ) \sqrt { 2 \pi } } e ^ { - \frac { ( 1 0 . 2 - m ) ^ { 2 } } { 2 ( 1 / \sqrt { 2 } ) ^ { 2 } } } ,
$$

with mean $1 0 . 2 ~ { \mu \mathrm { g } }$ and $\sigma = 1 / \sqrt { 2 } ~ \mu \mathrm { g }$ (Figure 11.2). Since we used an uninformative prior and the measurement errors were independent and normally distributed, the MAP solution is precisely the least squares solution for this problem.

It is notable in the second part of this example that we started with a normal prior distribution,accommodated normally distributed data,and obtained a normal posterior distribution (see (11.2O)). In general we should not expect that the prior and posterior distributions will both be well-known distributions whose properties are well known. A prior distribution associated with a simple posterior distribution in this way is called a conjugate prior. There are other families of conjugate distributions for various parameter estimation problems, but in general this is unusual [51].

![](images/9ff696572019161e2a7e22d2c7f961a029e72db348ed462019efca38647ac9c9.jpg)  
Figure 11.2 Posterior distribution $q ( m | d _ { 1 } = 1 0 . 3 \mu \mathrm { g }$ $d _ { 2 } = 1 0 . 1 \mu \mathrm { g } ,$ .

# 11.3.THE MULTIVARIATE NORMAL CASE

The result shown in Example 11.1 in which a normal prior distribution and normally distributed data lead to a normal posterior distribution can be readily extended to problems with many model parameters. We next examine the problem of determining the posterior distribution for a linear model, multivariate normal (MVN) distributed data errors,and an MVN prior distribution.

Let $\mathbf { d } _ { \mathrm { { o b s } } }$ be the observed data, $\mathbf { C } _ { D }$ be the corresponding data covariance matrix, $\mathbf { m } _ { \mathrm { p r i o r } }$ be the mean of the prior distribution, and $\mathbf { C } _ { M }$ be the covariance matrix for the prior distribution. The prior distribution is thus, by (B.62),

$$
p ( \mathbf { m } ) \propto e ^ { - \frac { 1 } { 2 } ( \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } ) ^ { T } \mathbf { C } _ { M } ^ { - 1 } ( \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } ) } ,
$$

and the conditional distribution of the data, given $\mathbf { m }$ ,is

$$
f ( \mathbf { d } | \mathbf { m } ) \propto e ^ { - \frac { 1 } { 2 } ( \mathbf { G } \mathbf { m } - \mathbf { d } ) ^ { T } \mathbf { C } _ { D } ^ { - 1 } ( \mathbf { G } \mathbf { m } - \mathbf { d } ) } .
$$

Thus, (11.6) gives

$$
q ( \mathbf { m } | \mathbf { d } ) \propto e ^ { - \frac { 1 } { 2 } ( ( \mathbf { G } \mathbf { m } - \mathbf { d } ) ^ { T } \mathbf { C } _ { D } ^ { - 1 } ( \mathbf { G } \mathbf { m } - \mathbf { d } ) + ( \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } ) ^ { T } \mathbf { C } _ { M } ^ { - 1 } ( \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } ) ) } .
$$

Tarantola [155] showed that this can be simplified to

$$
q ( \mathbf { m } | \mathbf { d } ) \propto e ^ { - \frac { 1 } { 2 } ( \mathbf { m } - \mathbf { m } _ { \mathrm { M A P } } ) ^ { T } \mathbf { C } _ { M ^ { \prime } } ^ { - 1 } ( \mathbf { m } - \mathbf { m } _ { \mathrm { M A P } } ) } ,
$$

where ${ \bf m } _ { \mathrm { M A P } }$ is the MAP solution, and

$$
\mathbf { C } _ { M ^ { \prime } } = ( \mathbf { G } ^ { T } \mathbf { C } _ { D } ^ { - 1 } \mathbf { G } + \mathbf { C } _ { M } ^ { - 1 } ) ^ { - 1 } .
$$

The MAP solution can be found by maximizing the exponent in (1.23),or equivalently by minimizing its negative:

$$
\mathrm { m i n } ( \mathbf { G m - d } ) ^ { T } \mathbf { C } _ { D } ^ { - 1 } ( \mathbf { G m - d } ) + ( \mathbf { m - m } _ { \mathrm { p r i o r } } ) ^ { T } \mathbf { C } _ { M } ^ { - 1 } ( \mathbf { m - m } _ { \mathrm { p r i o r } } ) .
$$

The key to minimizing (11.26) is to rewrite it in terms of the matrix square roots of $\mathbf { C } _ { M } ^ { - 1 }$ and $\mathbf { C } _ { D } ^ { - 1 }$ . Notethateveryovaranematrixispositiedefiiteandhsqe positive definite matrix square root,which may be calculated in MATLAB using the sqrtm routine. This minimization problem can then be reformulated as

$$
\begin{array} { r l } & { \operatorname* { m i n } \ ( \mathbf { C } _ { D } ^ { - 1 / 2 } ( \mathbf { G m } - \mathbf { d } ) ) ^ { T } ( \mathbf { C } _ { D } ^ { - 1 / 2 } ( \mathbf { G m } - \mathbf { d } ) ) \ + } \\ & { \qquad ( \mathbf { C } _ { M } ^ { - 1 / 2 } ( \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } ) ) ^ { T } ( \mathbf { C } _ { M } ^ { - 1 / 2 } ( \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } ) ) , } \end{array}
$$

or as the standard least squares problem,

$$
\mathrm { m i n } \left\| \left[ \mathbf { C } _ { D } ^ { - 1 / 2 } \mathbf { G } \right] \mathbf { m } - \left[ \mathbf { C } _ { D } ^ { - 1 / 2 } \mathbf { d } \right] \right\| _ { 2 } ^ { 2 } .
$$

Examining the right-hand terms in (11.28), note that

$$
\begin{array} { r } { \mathrm { C o v } ( \mathbf { C } _ { D } ^ { - 1 / 2 } \mathbf { d } ) = \mathbf { C } _ { D } ^ { - 1 / 2 } \mathbf { C } _ { D } ( \mathbf { C } _ { D } ^ { - 1 / 2 } ) ^ { T } = \mathbf { I } . } \end{array}
$$

The multiplication of $\mathbf { C } _ { D } ^ { - 1 / 2 }$ times $\mathbf { d }$ in (11.28)cnusbceptalizdsdata transformation that both makes the resulting elements independent and normalizes the staddeve $\bar { \mathbf { C } } _ { M } ^ { - 1 / 2 }$ has te sae efet.

An interesting limiting case is where the prior distribution provides essentially no information. Consider an MVN prior distribution with a covariance matrix $\mathbf { C } _ { M } = \alpha ^ { 2 } \mathbf { I } .$ in the limit where $\alpha$ is extremely large.In this case,the diagonal elements of $\mathbf { C } _ { M } ^ { - 1 }$ will be extremely small, and the posterior covariance matrix (11.25) will be well-approximated by

$$
\mathbf { C } _ { M ^ { \prime } } \approx ( \mathbf { G } ^ { T } \operatorname { C o v } ( \mathbf { d } ) ^ { - 1 } \mathbf { \Sigma } \mathbf { G } ) ^ { - 1 } .
$$

If the data covariance matrix is $\mathbf { C } _ { D } = \sigma ^ { 2 } \mathbf { I }$ ,then

$$
\mathbf { C } _ { M ^ { \prime } } \approx \sigma ^ { 2 } ( \mathbf { G } ^ { T } \mathbf { G } ) ^ { - 1 } ,
$$

which is precisely the covariance matrix for the least squares model parameters in (11.1). Furthermore, when we solve (11.28) to obtain the MAP solution, we find that it simplifies to the least squares problem of minimizing $\| \mathbf { G m } - \mathbf { d } \| _ { 2 } ^ { 2 }$ . Thus,under the common assumption of normally distributed and independent data errors with constant variance, a very broad prior distribution leads to a MAP solution that is the unregularized least squares solution.

It is also worthwhile to consider what happens in the special case where $\mathbf { C } _ { D } = \sigma ^ { 2 } \mathbf { I }$ and $\mathbf { C } _ { M } = \alpha ^ { 2 } \mathbf { I }$ . In this case the corresponding matrix square roots are also proportional to identity matrices,and (11.28) simplifies to

$$
\operatorname* { m i n } \ ( 1 / \sigma ) ^ { 2 } \| ( \mathbf { G m } - \mathbf { d } ) \| _ { 2 } ^ { 2 } + ( 1 / \alpha ) ^ { 2 } \| \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } \| _ { 2 } ^ { 2 } ,
$$

which is a modified optimization problem for zeroth-order Tikhonov regularization (4.4),where the 2-norm regularization term is evaluated relative to $\mathbf { m } _ { \mathrm { p r i o r } }$ ，and the equivalent Tikhonov regularization parameter is $\sigma / \alpha$ . Thus,the MAP solution obtained by using a prior with independent and normally distributed model parameters is precisely the zeroth-order Tikhonov regularized solution obtained by solving (11.32). However, this does not mean that the Bayesian approach is entirely equivalent to Tikhonov regularization,because the Bayesian solution is a probability distribution, whereas the Tikhonov solution is a single model from that distribution.

Once we have obtained the posterior distribution, it is straightforward to generate corresponding model realizations. We may wish to do this to assess likely or unlikely model features. Following the procedure outlined in Example B.1O,we compute the Cholesky factorization of the posterior distribution covariance matrix,

$$
{ \bf C } _ { M ^ { \prime } } = { \bf R } ^ { T } { \bf R } ,
$$

and generate a random solution

$$
\mathbf { m } = \mathbf { R } ^ { T } \mathbf { s } + \mathbf { m } _ { \mathrm { M A P } } ,
$$

where the vector s consists of independent and normally distributed random numbers with a zero mean and a unit standard deviation.

# Example 11.2

We consider Bayesian solutions to the Shaw problem that was previously considered in Examples 3.3, 4.1, 4.2, 4.3, and 4.8.

We first use a relatively uninformative MVN prior distribution with mean 0.5, standard deviation O.5,and zero covariances，so that $\mathbf { C } _ { M } = 0 . 2 5 \textbf { I }$ 、As in the previous examples, the measurement noise has standard deviation $1 . 0 \times 1 0 ^ { - 6 }$ ,so that $\mathbf { C } _ { D } =$ $1 . 0 \times 1 0 ^ { - 1 2 }$ 1. Solving (11.28) produces the mMAP solution shown in Figure 11.3. Figure 11.4 shows this same solution with error bars. These error bars are not classical $9 5 \%$ confidence intervals (e.g., Figure 4.9). Rather, they are $9 5 \%$ probability intervals calculated from the MVN posterior distribution,so that there is $9 5 \%$ probability that each model parameter lies within the corresponding symmetric interval around mMAP.

![](images/8949d80b3a50096246990a1034ac0ee92bda979ccc71211e36ca7bc158d706c8.jpg)  
Figure 11.3 The MAP solution and the true model for the Shaw example using an MVN priol distribution with mean O 5,standard deviation O 5,and zero covariance.

![](images/26a1bd544c45de3badd5ead14cd0fe267396171828f7b43ca79723560e3efd5b.jpg)  
Figure11.4 The MAP solution of Figure 11.3, with $9 5 \%$ probability intervals.

Figure 11.5 shows a random solution generated from the posterior distribution. This solution varies considerably from the true model,and demonstrates great uncertainty in the inverse solution, consistent with the large $9 5 \%$ probability intervals in Figure 11.3. The roughness of this solution realization is a consequence of the fact that the prior distribution $\mathbf { C } _ { M }$ had zero covariances,so model realizations from the posterior distribution have no preference for smoothness.

![](images/ed18c6b2df84c0c4eac18372ba47df21c9cd09d98b29a6c5a1deb9497031ceac.jpg)  
Figure 11.5 A model realization for the Shaw example using an MVN prior distribution with mean 0.5, standard deviation O 5,and zero covariance.

![](images/cf6eeb76d23c848063dd66e52da660a236251ca865442e8931f7ee379375060a.jpg)  
Figure 11.6 A more restrictive zero covariance prior distribution for the Shaw problem with $9 5 \%$ probability intervals.

Next,consider a more restrictive prior distribution. Suppose we have reason to believe that the largest amplitudes in the solution should be near the center of the model. We thus choose the bell-shaped zero-covariance prior distribution depicted in Figure 11.6. Figures 11.7 and 11.8 show the resulting MAP model and its probability intervals for this case. The solution recovery is, not surprisingly, improved by our more restrictive prior model given that the true model is highly restricted and is thus consistent with the prior distribution (Figure 11.3).

![](images/bde714b7b44a4a57989ff6df90d070760a8ca1f067ad29e47696df963146e008.jpg)  
Figure 11.7 The MAP solution for the Shaw example using the prior distribution shown in Figure 11.6.

![](images/5716c58eae6861a370170d0a29e0d3cf0ddb946703bac53eaf4eac81548307f3.jpg)  
Figure 11.8 The MAP solution of Figure 11.7 with probability intervals.

These results illustrate a principal issue with applying the Bayesian approach to poorly conditioned problems.To obtain a tight posterior distribution in such cases,we will have to make strong prior assumptions. Conversely, if such assumptions are not made, then we cannot recover the true model features well. This situation is analogous to that of Tikhonov regularization,which must also impose strong and consistent model bias to produce “good” solutions and must also make strong model assumptions to estimate solution error bounds (Section 4.8).

In the previous example,we applied a prior that preferentially concentrated the model structure in a particular region (the center) by imposing a zero prior with small standard deviations near the model edges. Because this prior distribution had zero covariances,resulting model realizations were rough. Prior distributions can be readily designed to enforce smoothness constraints on realizations from the posterior distribution by specifying a nondiagonal prior covariance matrix. A straightforward way to accomplish this for a 1-dimensional model is to construct a correlation matrix with columns

$$
\begin{array} { r } { { \bf R } _ { i , . } = \mathrm { s h i f t } ( a _ { j } , i ) , } \end{array}
$$

where $a _ { j }$ is the desired sequence of parameter correlations,with a zero lag correlation of 1. The shift operator shifts the sequence (truncating as necessary) so that the zero-lag (unit) maximum of the correlation sequence is centered on element $i .$ ,and hence on the diagonal of R. Suitable sequences $a _ { i }$ that ensure the positive definiteness of $\mathbf { R }$ can be constructed using autocorrelation (e.g., using the MATLAB xcorr function). Here, we use the autocorrelation of a triangle function, which produces a cubic approximation to a Gaussian function. Given the correlation matrix, $\mathbf { R }$ ,a corresponding prior distribution covariance matrix with uniform parameter variances, $\sigma _ { M }$ ,can then be constructed as

$$
\mathbf { C } _ { M } = \sigma _ { M } ^ { 2 } \mathbf { R } .
$$

# Example 11.3

Consider the vertical seismic profile (VSP) problem first introduced in Example 1.3, which was solved and analyzed using Tikhonov regularization in Examples 4.4, 4.5, 4.6,and 4.7. We revisit this problem as a Bayesian problem, implementing an MVN prior with a covariance matrix of the form of (11.36). The model consists of 5O equally spaced slowness intervals along a $1 0 0 0 \mathrm { - m }$ vertical borehole with an interval length of $2 0 \mathrm { m }$ . Seismic travel time data are collected at 5O equally spaced depths with independent zero-mean normal erors with standard deviation of $\sigma _ { D } = 2 \times 1 0 ^ { - 4 } ~ \mathrm { s }$ ， producing a data covariance matrix $\mathbf { C } _ { D } = \sigma _ { D } ^ { 2 }$ I. We apply a prior distribution that is consistent with a seismic slownes decrease (velocity increase) with depth and has a constant gradient between known seismic slownesses from the top and the bottom of the borehole. We first impose a prior distribution standard deviation of $\sigma _ { M } = 2 \times 1 0 ^ { - 5 } \mathrm { s / m }$ on all parameters to repre-sent an estimated variability in model slownesses,and utilize a prior correlation function that falls off with a scale length of five model intervals (i.e.,a correlation of $1 / e$ at a model parameter lag of approximately five model parameters or $1 0 0 ~ \mathrm { m }$ ). The prior distribution and its parameter standard deviations are shown in Figure 11.9,and the corresponding parameter correlation function is shown in Figure 11.1O. The resulting posterior distribution and its standard deviations are shown in Figure 11.11. We next apply a prior with twice the correlation length (Figure 11.12). The resulting posterior distribution is shown in Figure 11.13.

![](images/46fc94eac9a475a0bf79c3165afb425cd765e30d656d8925756d24106d74b3ba.jpg)  
Figure 11.9 A constant-slowness gradient prior distribution and its $9 5 \%$ distribution intervals for the VSP problem.The true model is shown as the gray smooth curve.

![](images/3cdfddfb5b09a5fa4c32ea65cff0b2c4f83f8542005c6ab915a6bcc122d321c7.jpg)  
Figure 11.10 A correlation function for the prior distribution of Figure 11.9 with a $1 / e$ correlation length of approximately five parameters $( 1 0 0 \mathsf { m } )$

![](images/683c97c05cc605d4930026c1391fc554748ca352ab91c763c1ae2c9940af248b.jpg)  
Figure 11.11 MAP model obtained from the posterior distribution,and its $9 5 \%$ distribution intervals, using the prior distribution described in Figures 11.9 and 11.10.The true model is shown as the gray smooth curve.

![](images/529da890a8765d34881afb9ed238dd0a876883555e8e10870f3b5ac2950339dc.jpg)  
Figure 11.12 A correlation function for the prior distribution of Figure 11.9 with a $1 / e$ correlation length of approximately10 parameters $( 2 0 0 \mathsf { m } )$

![](images/650346aba64012bad47090159673e9ff1616865ddd505e190ff8a06b145bfc93.jpg)  
Figure 11.13 MAP model obtained from the posterior distribution,and its $9 5 \%$ distribution intervals, using the prior distribution depicted in Figures 11.9 and 11.12.The true model is shown as the gray smooth curve.

The approach described in this section can be extended to nonlinear problems. To find the MAP solution, solve the nonlinear least squares problem,

$$
\operatorname* { m i n } \quad \mathbf { G } ( \mathbf { m } ) - \mathbf { d } ) ^ { T } \mathbf { C } _ { D } ^ { - 1 } ( \mathbf { G } ( \mathbf { m } ) - \mathbf { d } ) + ( \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } ) ^ { T } \mathbf { C } _ { M } ^ { - 1 } ( \mathbf { m } - \mathbf { m } _ { \mathrm { p r i o r } } ) .
$$

One can then linearize around the MAP solution to obtain the approximate posterior covariance,

$$
\mathbf { C } _ { M ^ { \prime } } = ( \mathbf { \Delta J ( m _ { M A P } ) } ^ { T } \mathbf { C } _ { D } ^ { - 1 } \mathbf { J ( m _ { M A P } ) } + \mathbf { C } _ { M } ^ { - 1 } ) ^ { - 1 } ,
$$

where $\mathbf { J } ( \mathbf { m } )$ is the Jacobian. As with other nonlinear optimization problems,we must consider the possbility of multiple local optima. If (11.37) has multiple solutions with comparable likelihoods,then a single MAP solution and associated $\mathbf { C } _ { M ^ { \prime } }$ from (11.38) will not accurately characterize the posterior distribution.

# 11.4.THE MARKOV CHAIN MONTE CARLO METHOD

We next introduce the use of Markov Chain Monte Carlo (MCMC) methods to sample from a posterior distribution. Given a sufficient population of such samples,we can use them to characterize the solution of a Bayesian inverse problem.Because MCMC methods depend only on the forward model and associated likelihood calculations, they are easily applied to both linear and nonlinear problems.