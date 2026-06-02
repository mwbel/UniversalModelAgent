in between $- f _ { c }$ and $f _ { c }$ . Then we look to the Fourier transform to tell whether the continuous function has been competently sampled (aliasing effects minimized). We do this by looking to see whether the Fourier transform is already approaching zero as the frequency approaches $f _ { c }$ from below or $- f _ { c }$ from above. If, on the contrary, the transform is going toward some finite value, then chances are that components outside of the range have been folded back over onto the critical range.

# 12.1.2 Discrete Fourier Transform

We now estimate the Fourier transform of a function from a finite number of its sampled points. Suppose that we have $N$ consecutive sampled values,

$$
h _ { k } \equiv h ( t _ { k } ) , \qquad t _ { k } \equiv k \Delta , \qquad k = 0 , 1 , 2 , \ldots , N - 1
$$

so that the sampling interval is $\Delta$ . To make things simpler, let us also suppose that $N$ is even. If the function $h ( t )$ is nonzero only in a finite interval of time, then that whole interval of time is supposed to be contained in the range of the $N$ points given. Alternatively, if the function $h ( t )$ goes on forever, then the sampled points are supposed to be at least “typical” of what $h ( t )$ looks like at all other times.

With $N$ numbers of input, we will evidently be able to produce no more than $N$ independent numbers of output. So, instead of trying to estimate the Fourier transform $H ( f )$ at all values of $f$ in the range $- f _ { c }$ to $f _ { c }$ , let us seek estimates only at the discrete values

$$
f _ { n } \equiv \frac { n } { N \Delta } , \qquad n = - \frac { N } { 2 } , \dots , \frac { N } { 2 }
$$

The extreme values of $n$ in (12.1.5) correspond exactly to the lower and upper limits of the Nyquist critical frequency range. If you are really on the ball, you will have noticed that there are $N + 1$ , not $N$ , values of $n$ in (12.1.5); it will turn out that the two extreme values of $n$ are not independent (in fact they are equal), but all the others are. This reduces the count to $N$ .

The remaining step is to approximate the integral in (12.0.1) by a discrete sum:

$$
H ( f _ { n } ) = \int _ { - \infty } ^ { \infty } h ( t ) e ^ { 2 \pi i f _ { n } t } d t \approx \sum _ { k = 0 } ^ { N - 1 } h _ { k } ~ e ^ { 2 \pi i f _ { n } t _ { k } } \Delta = \Delta \sum _ { k = 0 } ^ { N - 1 } h _ { k } ~ e ^ { 2 \pi i k n / N }
$$

Here equations (12.1.4) and (12.1.5) have been used in the final equality. The final summation in equation (12.1.6) is called the discrete Fourier transform of the $N$ points $h _ { k }$ . Let us denote it by $H _ { n }$ ,

$$
H _ { n } \equiv \sum _ { k = 0 } ^ { N - 1 } h _ { k } \ e ^ { 2 \pi i k n / N }
$$

The discrete Fourier transform maps $N$ complex numbers (the $h _ { k }$ ’s) into $N$ complex numbers (the $H _ { n }$ ’s). It does not depend on any dimensional parameter, such as the time scale $\Delta$ . The relation (12.1.6) between the discrete Fourier transform of a set of numbers and their continuous Fourier transform when they are viewed as samples of a continuous function sampled at an interval $\Delta$ can be rewritten as

$$
H ( f _ { n } ) \approx \Delta H _ { n }
$$

where $f _ { n }$ is given by (12.1.5).

Up to now we have taken the view that the index $n$ in (12.1.7) varies from $- N / 2$ to $N / 2$ (cf. 12.1.5). You can easily see, however, that (12.1.7) is periodic in $n$ , with period $N$ . Therefore, $H _ { - n } = H _ { N - n }$ , $n = 1 , 2 , \ldots$ With this conversion in mind, one generally lets the $n$ in $H _ { n }$ vary from 0 to $N - 1$ (one complete period). Then $n$ and $k$ (in $h _ { k }$ ) vary exactly over the same range, so the mapping of $N$ numbers into $N$ numbers is manifest. When this convention is followed, you must remember that zero frequency corresponds to $n = 0$ and positive frequencies $0 ~ < ~ f ~ < ~ f _ { c }$ correspond to values $1 \leq n \leq N / 2 - 1$ , while negative frequencies $- f _ { c } < f < 0$ correspond to $N / 2 + 1 \le n \le N - 1$ . The value $n = N / 2$ corresponds to both $f = f _ { c }$ and $f = - f _ { c }$ .

The discrete Fourier transform has symmetry properties almost exactly the same as the continuous Fourier transform. For example, all the symmetries in the table following equation (12.0.3) hold if we read $h _ { k }$ for $h ( t )$ , $H _ { n }$ for $H ( f )$ , and $H _ { N - n }$ for $H ( - f )$ . (Likewise, “even” and “odd” in time refer to whether the values $h _ { k }$ at $k$ and $N - k$ are identical or the negative of each other.)

The formula for the discrete inverse Fourier transform, which recovers the set of $h _ { k }$ ’s exactly from the $H _ { n }$ ’s is

$$
h _ { k } = \frac { 1 } { N } \sum _ { n = 0 } ^ { N - 1 } H _ { n } \ e ^ { - 2 \pi i k n / N }
$$

Notice that the only differences between (12.1.9) and (12.1.7) are (i) changing the sign in the exponential, and (ii) dividing the answer by $N$ . This means that a routine for calculating discrete Fourier transforms can also, with slight modification, calculate the inverse transforms.

The discrete form of Parseval’s theorem is

$$
\sum _ { k = 0 } ^ { N - 1 } | h _ { k } | ^ { 2 } = \frac { 1 } { N } \sum _ { n = 0 } ^ { N - 1 } | H _ { n } | ^ { 2 }
$$

There are also discrete analogs to the convolution and correlation theorems (equations 12.0.10 and 12.0.12), but we shall defer them to $\ S 1 3 . 1$ and $\ S 1 3 . 2$ , respectively.

# CITED REFERENCES AND FURTHER READING:

Brigham, E.O. 1974, The Fast Fourier Transform (Englewood Cliffs, NJ: Prentice-Hall).   
James, J.F. 2002, A Student’s Guide to Fourier Transforms, 2nd ed. (Cambridge, UK: Cambridge University Press)   
Elliott, D.F., and Rao, K.R. 1982, Fast Transforms: Algorithms, Analyses, Applications (New York: Academic Press).

# 12.2 Fast Fourier Transform (FFT)

How much computation is involved in computing the discrete Fourier transform (12.1.7) of $N$ points? For many years, until the mid-1960s, the standard answer was this: Define $W$ as the complex number

$$
W \equiv e ^ { 2 \pi i / N }
$$

Then (12.1.7) can be written as

$$
H _ { n } = \sum _ { k = 0 } ^ { N - 1 } W ^ { n k } h _ { k }
$$

In other words, the vector of $h _ { k }$ ’s is multiplied by a matrix whose $( n , k )$ th element is the constant $W$ to the power $n \times k$ . The matrix multiplication produces a vector result whose components are the $H _ { n }$ ’s. This matrix multiplication evidently requires $N ^ { 2 }$ complex multiplications, plus a smaller number of operations to generate the required powers of $W$ . So, the discrete Fourier transform appears to be an $O ( N ^ { 2 } )$ process. These appearances are deceiving! The discrete Fourier transform can, in fact, be computed in $O ( N \log _ { 2 } N )$ operations with an algorithm called the fast Fourier transform, or FFT. The difference between $N \log _ { 2 } N$ and $N ^ { 2 }$ is immense. With $N \ = \ 1 0 ^ { 8 }$ , for example, it is a factor of several million, comparable to the ratio of one second to one month. The existence of an FFT algorithm became generally known only in the mid-1960s, from the work of J.W. Cooley and J.W. Tukey. Retrospectively, we now know (see [1]) that efficient methods for computing the DFT had been independently discovered, and in some cases implemented, by as many as a dozen individuals, starting with Gauss in 1805!

One “rediscovery” of the FFT, that of Danielson and Lanczos in 1942, provides one of the clearest derivations of the algorithm. Danielson and Lanczos showed that a discrete Fourier transform of length $N$ can be rewritten as the sum of two discrete Fourier transforms, each of length $N / 2$ . One of the two is formed from the evennumbered points of the original $N$ , the other from the odd-numbered points. The proof is simply this:

$$
\begin{array} { r l } {  { F _ { k } = \sum _ { j = 0 } ^ { N - 1 } e ^ { 2 \pi i j k / N } f _ { j } } } \\ & { = \sum _ { j = 0 } ^ { N / 2 - 1 } e ^ { 2 \pi i k ( 2 j ) / N } f _ { 2 j } + \sum _ { j = 0 } ^ { N / 2 - 1 } e ^ { 2 \pi i k ( 2 j + 1 ) / N } f _ { 2 j + 1 } } \\ & { = \displaystyle \sum _ { j = 0 } ^ { N / 2 - 1 } e ^ { 2 \pi i k j / ( N / 2 ) } f _ { 2 j } + W ^ { N } \sum _ { j = 0 } ^ { N / 2 - 1 } e ^ { 2 \pi i k j / ( N / 2 ) } f _ { 2 j + 1 } } \\ & { = F _ { k } ^ { \prime } + W ^ { k } \ F _ { k } ^ { \prime } } \end{array}
$$

In the last line, $W$ is the same complex constant as in (12.2.1), $F _ { k } ^ { e }$ denotes the $k$ th component of the Fourier transform of length $N / 2$ formed from the even components of the original $f _ { j }$ ’s, while $F _ { k } ^ { o }$ is the corresponding transform of length $N / 2$ formed from the odd components. Notice also that $k$ in the last line of (12.2.3) varies from 0 to $N$ , not just to $N / 2$ . Nevertheless, the transforms $F _ { k } ^ { e }$ and $F _ { k } ^ { o }$ are periodic in $k$ with length $N / 2$ . So each is repeated through two cycles to obtain $F _ { k }$ .

The wonderful thing about the Danielson-Lanczos lemma is that it can be used recursively. Having reduced the problem of computing $F _ { k }$ to that of computing $F _ { k } ^ { e }$ and $F _ { k } ^ { o }$ , we can do the same reduction of $F _ { k } ^ { e }$ to the problem of computing the transform of its $N / 4$ even-numbered input data and $N / 4$ odd-numbered data. In other words, we can define $F _ { k } ^ { e e }$ and $F _ { k } ^ { e o }$ to be the discrete Fourier transforms of the points that are respectively even-even and even-odd on the successive subdivisions of the data.

Although there are ways of treating other cases, by far the easiest case is the one in which the original $N$ is an integer power of 2. In fact, we categorically recommend that you only use FFTs with $N$ a power of 2. If the length of your data set is not a power of 2, pad it with zeros up to the next power of 2. (We will give more sophisticated suggestions in subsequent sections below.) With this restriction on $N$ , it is evident that we can continue applying the Danielson-Lanczos lemma until we have subdivided the data all the way down to transforms of length one. What is the Fourier transform of length one? It is just the identity operation that copies its one input number into its one output slot! In other words, for every pattern of $\log _ { 2 } N$ $e$ ’s and $o$ ’s, there is a one-point transform that is just one of the input numbers $f _ { n }$ ,

$$
F _ { k } ^ { e o e e o e o \cdots o e e } = f _ { n } \qquad { \mathrm { f o r ~ s o m e } } n
$$

(Of course this one-point transform actually does not depend on $k$ , since it is periodic in $k$ with period 1.)

The next trick is to figure out which value of $n$ corresponds to which pattern of $e$ ’s and $o$ ’s in equation (12.2.4). The answer is: Reverse the pattern of $e$ ’s and $o$ ’s, then let $e \ = \ 0$ and $o = 1$ , and you will have, in binary, the value of $n$ . Do you see why it works? It is because the successive subdivisions of the data into even and odd are tests of successive low-order (least significant) bits of $n$ . This idea of bit reversal can be exploited in a very clever way that, along with the Danielson-Lanczos lemma, makes FFTs practical: Suppose we take the original vector of data $f _ { j }$ and rearrange it into bit-reversed order (see Figure 12.2.1), so that the individual numbers are in the order not of $j$ , but of the number obtained by bit reversing $j$ . Then the bookkeeping on the recursive application of the Danielson-Lanczos lemma becomes extraordinarily simple. The points as given are the one-point transforms. We combine adjacent pairs to get two-point transforms, then combine adjacent pairs of pairs to get four-point transforms, and so on, until the first and second halves of the whole data set are combined into the final transform. Each combination takes of order $N$ operations, and there are evidently $\log _ { 2 } N$ combinations, so the whole algorithm is of order $N \log _ { 2 } N$ (assuming, as is the case, that the process of sorting into bit-reversed order is no greater in order than $N \log _ { 2 } N )$ ).

This, then, is the structure of an FFT algorithm: It has two sections. The first section sorts the data into bit-reversed order. Luckily this takes no additional storage, since it involves only swapping pairs of elements. (If $k _ { 1 }$ is the bit reverse of $k _ { 2 }$ , then $k _ { 2 }$ is the bit reverse of $k _ { 1 }$ .) The second section has an outer loop that is executed $\log _ { 2 } N$ times and calculates, in turn, transforms of length $2 , 4 , 8 , \ldots , N$ . This series of operations is often called a butterfly. For each stage of the process, two nested inner loops range over the subtransforms already computed and the elements of each transform, implementing the Danielson-Lanczos lemma. The operation is made more efficient by restricting external calls for trigonometric sines and cosines to the outer loop, where they are made only $\log _ { 2 } N$ times. Computation of the sines and cosines of multiple angles is through simple recurrence relations in the inner loops (cf. 5.4.6).

![](images/cf59e0383bd5ed0a96ac4ec000d4119351c9defc6d550e69e5878a05f94c2f6c.jpg)  
Figure 12.2.1. Reordering an array (here of length 8) by bit reversal, (a) between two arrays, versus (b) in place. Bit-reversal reordering is a necessary part of the fast Fourier transform (FFT) algorithm.

# 12.2.1 Bare FFT Routine and Helper Interfaces

Experience convinces us that a good way to package the FFT is as (i) a bare routine with a minimal interface, plus also (ii) a small set of interface objects that make it easier to get data in and out of the bare routine. The bare FFT routine given below is based on one originally written by N.M. Brenner. The input quantities are the number of complex data points n $( = N )$ , a pointer to the data array $( \mathtt { d a t a } [ 0 . . 2 * \mathtt { n } ^ { - 1 } ] )$ ), and isign, which is set to either $\pm 1$ and is the sign of $i$ in the exponential of equation (12.1.7). When isign is set to $^ { - 1 }$ , the routine thus calculates the inverse transform (12.1.9) — except that it does not multiply by the normalizing factor $1 / N$ that appears in that equation. You do that yourself. We test to be sure that $\mathbf { n }$ is a power of 2 by the $\mathrm { C } { + } { + }$ idiom $\mathtt { n } \& ( \mathtt { n } ^ { - 1 } )$ , which is zero only if $\mathbf { n }$ is, in binary, 1 followed by any number of zeros.

Notice that the argument $\mathbf { n }$ is the number of complex data points. The actual length of the Doub array (data $[ 0 \ldots 2 * \mathtt { n } - 1 ]$ ) is $2 \mathtt { n }$ , with each complex value occupying two consecutive locations. In other words, data[0] is the real part of $f _ { 0 }$ , data[1] is the imaginary part of $f _ { 0 }$ , and so on up to data $[ 2 * \mathtt { n } - 2 ]$ , which is the real part of $f _ { N - 1 }$ , and data $[ 2 * \mathtt { n } - 1 ]$ , which is the imaginary part of $f _ { N - 1 }$ .

The FFT routine gives back the $F _ { n }$ ’s packed in exactly the same fashion, as n complex numbers. The real and imaginary parts of the zero frequency component $F _ { 0 }$ are in data[0] and data[1]; the smallest nonzero positive frequency has real and imaginary parts in data[2] and data[3]; the smallest (in magnitude) nonzero negative frequency has real and imaginary parts in data $[ 2 * \mathtt { n } - 2 ]$ and data $[ 2 * \mathtt { n } - 1 ]$ . Positive frequencies increasing in magnitude are stored in the real-imaginary pairs data[4], data[5] up to data[n-2], data[n-1]. Negative frequencies of increasing magnitude are stored in data $[ 2 * \mathtt { n } - 4 ]$ , data $[ 2 * \mathtt { n } - 3 ]$ down to data $[ \mathtt { n } + 2 ]$ , data $\left[ \tt n + 3 \right]$ . Finally, the pair data[n], data $[ \mathrm { n } { + } 1 ]$ contains the real and imaginary parts of the one aliased point that contains the most positive and the most negative frequencies. You should try to develop a familiarity with this storage arrangement of complex spectra, also shown in Figure 12.2.2, since it is the practical standard.

![](images/02926fe322533f0a687e2d0cbe69cf6972884c20c47d9f1c5d2de0fe0a34b675.jpg)  
Figure 12.2.2. Input and output arrays for FFT. (a) The input array contains $N$ (a power of 2) complex time samples in a real array of length $2 N$ , with real and imaginary parts alternating. (b) The output array contains the complex Fourier spectrum at $N$ values of frequency. Real and imaginary parts again alternate. The array starts with zero frequency, works up to the most positive frequency (which is aliased with the most negative frequency). Negative frequencies follow, from the second-most negative up to the frequency just below zero.

# void four1(Doub \*data, const Int n, const Int isign) {

Replaces data $[ 0 \ldots 2 * \mathtt { n } - 1 ]$ by its discrete Fourier transform, if isign is input as 1; or replaces data[0.. $^ { 2 * \mathbf { n } - 1 ] }$ by n times its inverse discrete Fourier transform, if isign is input as $^ { - 1 }$ . data is a complex array of length n stored as a real array of length $^ { 2 * \mathrm { n } }$ . n must be an integer power of 2.

Int nn,mmax,m,j,istep,i;   
Doub wtemp,wr,wpr,wpi,wi,theta,tempr,tempi;   
if ( $\cdot \mathbf { n } { < } 2$ || n& $( \mathtt { n - 1 } )$ ) throw("n must be power of 2 in four1");   
$\mathrm { ~ n ~ n ~ } = \mathrm { ~ n ~ } < < \mathrm { ~ 1 ~ }$ ;   
$\mathrm { ~ j ~ } = \mathrm { ~ 1 ~ }$ ;   
for ( $\dot { \mathbf { 1 } } = 1$ ;i<nn; $\scriptstyle \dot { 1 } + = 2$ ) { This is the bit-reversal section of the if (j > i) { routine. SWAP(data[j-1],data[i-1]); Exchange the two complex numbers. SWAP(data[j],data[i]); } ${ \mathrm { m } } { = } { \mathrm { n } }$ ; while $\mathrm { ~ m ~ } > = \mathrm { ~ 2 ~ }$ && $\dot { \mathrm { ~ \ j ~ } } > \mathfrak { m } )$ { ${ \mathrm { ~ j ~ } } \ \mathrm { ~ \ -- ~ } { \mathrm { ~ m } } ;$

m >>= 1; } j += m; } Here begins the Danielson-Lanczos section of the routine. mmax $^ { - 2 }$ ; while (nn > mmax) { Outer loop executed $\log _ { 2 } { \tt n }$ times. istep=mmax $< < ~ 1$ ; theta isign\*(6.28318530717959/mmax); Initialize the trigonometric recurrence. wtemp $\mid =$ sin(0. $^ { 5 * }$ theta); wpr $=$ -2.0\*wtemp\*wtemp; wpi $\equiv$ sin(theta); $\mathtt { w r } { = } 1$ .0; $\scriptstyle { \mathfrak { j } } = 0$ .0; for $\mathrm { ( m } { = } 1$ ;m<mmax; $\mathtt { m } + = 2$ ) { Here are the two nested inner loops. for ( $\dot { 1 } = \mathtt { m }$ ; $\scriptstyle { \dot { 1 } } < = { \mathtt { n n } }$ ; $\dot { \bf 1 } + =$ istep) { j=i+mmax; This is the Danielson-Lanczos fortempr=wr\*data[j-1]-wi\*data[j]; mula: tempi $=$ wr\*data[j]+wi\*data[j-1]; data[j-1] $=$ data[i-1]-tempr; data[j] $=$ data[i]-tempi; data[i-1] += tempr; data[i] $+ =$ tempi; wr=(wtemp=wr)\*wpr-wi\*wpi+wr; Trigonometric recurrence. wi $=$ wi\*wpr+wtemp\*wpi+wi; } mmax=istep; }

For an interface at a slightly higher level, we can overload the bare four1 with equivalent functions that input and output data as either a VecDoub of length $2 N$ or a VecComplex of length $N$ :

In these overloaded versions, however, you are still responsible for decoding on your own the wraparound order. To get an interface that takes care of that for you, we can define an object WrapVecDoub that creates a real vector (or binds a reference to an existing one) and then defines methods for addressing the vector as if it were a complex vector of half the size. Since the WrapVecDoub object also knows about wraparound periodicity, you can access frequencies either by subscripts $\left[ 0 \cdot \cdot \mathbf { n } ^ { - 1 } \right]$ or $[ - \mathtt { n } / 2 . . . \mathtt { n } / 2 - 1 ]$ , or, for that matter, any n consecutive complex components. The object has a conversion operator to VecDoub, so you can (e.g.) send it directly to four1.

# struct WrapVecDoub {

Object for accessing a VecDoub as if it were a complex vector of half the length, with wraparound periodicity.

VecDoub vvec;   
VecDoub &v;   
Int n, mask;

Used when data are stored internally.

WrapVecDoub(const Int nn) : vvec(nn), v(vvec), n(nn/2), mask(n-1) {validate();} Constructor. Declare a new vector with nn real components (half as many complex).

WrapVecDoub(VecDoub &vec) : v(vec), n(vec.size()/2), mask(n-1) {validate();} Constructor. Bind the data in an existing vector vec for access as if complex.

void validate() {if (n&(n-1)) throw("vec size must be power of 2");}

inline Complex& operator[] (Int i) {return (Complex &)v[(i&mask) << 1];} Reduce any integer i to the periodic range [0..n] and return that complex component. Can also be an l-value.

inline Doub& real(Int i) {return v[(i&mask) << 1];} As above, but return the real part only. Can also be an l-value.

inline Doub& imag(Int i) {return v[((i&mask) << 1)+1];} As above, but return the imaginary part only. Can also be an l-value.

operator VecDoub&() {return v;}

Conversion operator. Allows a WrapVecDoub object to be sent to any function that expects a VecDoub.

# };

Here are some sample lines of code (not a useful program) that show how WrapVecDoub can be used:

Int j, $\mathtt { n } = 2 5 6$ ;   
VecDoub dat $( 2 \ast \mathtt { n } )$ ;   
WrapVecDoub data1(dat), data2 $^ { , 2 * \mathrm { n } ) }$ );   
for $( \ j = 0$ ;j<n; $\mathrm { j } { + + } )$ { data1[j] $=$ Complex(.. data2.real(j) $=$ ; data2.imag(j) $=$ ;   
}   
four1(data1,1);   
four1(data2,1);   
for (j=-n/2;j<n/2;j $^ { + + }$ ) { $=$ data1.real(j); $=$ data2[j];   
} 256 complex components, e.g.   
A real vector to hold them.   
Examples of the two constructors.   
Loop over complex components.   
Set a complex value directly, or set real and imag separately.

Invokes four1(VecDoub&,Int) through the conversion operator. Can address negative frequencies directly! Get real part of component $j$ . Get component as a complex value.

# 12.2.2 Decomposing the FFT for Parallelism

It is possible to decompose the calculation of an FFT of size $N$ into a set of smaller FFTs that can be done independently of one another. This can be useful either to achieve parallelism or to allow more versatile memory management. The basic idea is to address the input array as if it were a two-dimensional array of size $m \times M$ , where $N = m M$ and $N , m$ , and $M$ are all powers of 2. Then the components of $f$ can be addressed as

$$
f [ J m + j ] , \qquad 0 \leq j < m , 0 \leq J < M
$$

where the $j$ index changes more rapidly, the $J$ index more slowly, and brackets denote $\mathrm { C } { + } { + }$ subscripts.

What we want to compute is the FFT of the original array of length $N$ , which we can write as

$$
F [ k M + K ] \equiv \sum _ { j , J } e ^ { 2 \pi i ( k M + K ) ( J m + j ) / ( M m ) } f ( J m + j ) ,
$$

You can see that the indices $k$ and $K$ address the desired result (FFT of the original array), with $K$ varying more rapidly.

From equation (12.2.6) it is easy to verify the identity

$$
F [ k M + K ] = \sum _ { j } \Biggl \{ e ^ { 2 \pi i j k / m } \biggl [ e ^ { 2 \pi i j K / ( M m ) } \biggl ( \sum _ { J } e ^ { 2 \pi i J K / M } f ( J m + j ) \biggr ) \biggr ] \Biggr \}
$$

But this, reading it from the innermost operation outward, is just the method that we need:

- For each value of $j$ form a vector of input values whose components vary with $J , 0 \le J < M$ . This is basically a transpose operation.   
- FFT each such vector. (OK to do in parallel.) Notationally, the $J$ index now becomes a $K$ index. Multiply each component by a phase factor $\exp [ 2 \pi i j K / ( M m ) ]$ . Rearrange the data so that they are accessible as a set of vectors whose components vary with $j , 0 \le j < m$ , another transpose operation. FFT each such vector. (OK to do in parallel.) The $j$ index now becomes a $k$ index. The answer is now available as $F [ k M + K ]$ . It takes a third transpose operation to get it back into the desired order (with $k$ varying most rapidly).

Even though two FFTs are performed on each element, the operations count is about the same as for the ordinary FFT: The first set of FFTs scales as $N \log M$ , the second set as $N \log m$ , and the total is thus $N \log ( M n ) = N \log N$ .

For further discussion, see [2], where the above is called the six-step framework. You can easily eliminate the first two of the three transpose operations by writing a new four1 routine with an additional stride argument, specifying the constant increment between logically “next” components. The stride will be $m$ for the first set of FFTs, and 1 for the second set. An algorithm very similar to this is called the four-step framework. See [2,3] for more details.

Related decompositions, called zoom transforms, can be used to get an approximation to the spectrum of a long data stream, at high resolution in only certain frequency bands. See [4-6].

# 12.2.3 Other FFT Algorithms

We should mention that there are a number of variants on the basic FFT algorithm given above. As we have seen, that algorithm first rearranges the input elements into bit-reverse order, then builds up the output transform in $\log _ { 2 } N$ iterations. In the literature, this sequence is called a decimation-in-time or Cooley-Tukey FFT algorithm. It is also possible to derive FFT algorithms that first go through a set of $\log _ { 2 } N$ iterations on the input data, and rearrange the output values into bit-reverse order. These are called decimation-in-frequency or Sande-Tukey FFT algorithms. For some applications, such as convolution (-13.1), one takes a data set into the Fourier domain and then, after some manipulation, back out again. In these cases it is possible to avoid all bit reversing. You use a decimation-in-frequency algorithm (without its bit reversing) to get into the “scrambled” Fourier domain, do your operations there, and then use an inverse algorithm (without its bit reversing) to get back to the time domain. While elegant in principle, this procedure does not in practice save much computation time, since the bit reversals represent only a small fraction of an FFT’s operations count, and since most useful operations in the frequency domain require a knowledge of which points correspond to which frequencies.

Another class of FFTs subdivides the initial data set of length $N$ not all the way down to the trivial transform of length 1, but rather only down to some other small power of 2, for example $N \ = \ 4$ , base-4 FFTs, or $N \ = \ 8$ , base-8 FFTs. These small transforms are then done by small sections of highly optimized coding that take advantage of special symmetries of that particular small $N$ . For example, for $N \ = \ 4$ , the trigonometric sines and cosines that enter are all $\pm 1$ or 0, so many multiplications are eliminated, leaving largely additions and subtractions. These can be faster than simpler FFTs by some significant, but not overwhelming, factor, e.g., 20 or $30 \%$ .

There are also FFT algorithms for data sets of length $N$ not a power of 2. They work by using relations analogous to the Danielson-Lanczos lemma to subdivide the initial problem into successively smaller problems, not by factors of 2, but by whatever small prime factors happen to divide $N$ . The larger that the largest prime factor of $N$ is, the worse this method works. If $N$ is prime, then no subdivision is possible, and the user (whether he knows it or not) is taking a slow Fourier transform, of order $N ^ { 2 }$ instead of order $N \log _ { 2 } N$ . Our advice is to stay clear of such FFT implementations, with perhaps one class of exceptions, the Winograd Fourier transform algorithms. Winograd algorithms are in some ways analogous to the base-4 and base-8 FFTs. Winograd has derived highly optimized codings for taking small- $N$ discrete Fourier transforms, e.g., for $N = 2 , 3 , 4 , 5 , 7 , 8 , 1 1 , 1 3 , 1 6 .$ . The algorithms also use a different and clever way of combining the subfactors. The method involves a reordering of the data both before the hierarchical processing and after it, but it allows a significant reduction in the number of multiplications in the algorithm. For some especially favorable values of $N$ , the Winograd algorithms can be significantly (e.g., up to a factor of 2) faster than the simpler FFT algorithms of the nearest integer power of 2. This advantage in speed, however, must be weighed against the considerably more complicated data indexing involved in these transforms, and the fact that the Winograd transform cannot be done “in place.”

Finally, an interesting class of transforms for doing convolutions quickly is number-theoretic transforms [7,8]. These schemes replace floating-point arithmetic with integer arithmetic modulo some large prime $N { + } 1$ , and the $N$ th root of 1 by the modulo arithmetic equivalent. Strictly speaking, these are not Fourier transforms at all, but the properties are quite similar and computational speed can be far superior. On the other hand, their use is somewhat restricted to quantities like correlations and convolutions since the transform itself is not easily interpretable as a “frequency” spectrum.

# CITED REFERENCES AND FURTHER READING:

Brigham, E.O. 1974, The Fast Fourier Transform (Englewood Cliffs, NJ: Prentice-Hall).[1]   
Nussbaumer, H.J. 1982, Fast Fourier Transform and Convolution Algorithms (New York: Springer).   
Elliott, D.F., and Rao, K.R. 1982, Fast Transforms: Algorithms, Analyses, Applications (New York: Academic Press).   
Walker, J.S. 1996, Fast Fourier Transforms, 2nd ed. (Boca Raton, FL: CRC Press)   
Bloomfield, P. 1976, Fourier Analysis of Time Series – An Introduction (New York: Wiley).   
Van Loan, C. 1992, Computational Frameworks for the Fast Fourier Transform (Philadelphia: S.I.A.M.).[2]   
Press, W.H., Teukolsky, S.A., Vetterling, W.T., and Flannery, B.P. 1996, Numerical Recipes in Fortran 90: The Artof Parallel Scientific Computing (Cambridge, UK: Cambridge University Press), $\ S 2 2 . 4$ .[3]   
Yip, P.C.Y. 1976, “Some Aspects of the Zoom Transform,” IEEE Transactions on Computers, vol. C-25, pp. 287–296.[4]   
Hung, E.K.L. 1981, “A Multiresolution Sampled-Data Spectrum Analyzer for a Detection System,” IEEE Transactions on Acoustics, Speech and Signal Processing, vol.ASSP-29,pp.163- 170.[5]   
de Wild, R., Nieuwkerk, L.R., and van Sinttruyen, J.S. 1987, “Method for Partial Spectrum Computation,” IEE Proceedings $F$ (Radar and Signal Processing), vol. 134, pp. 659–666[6]   
Beauchamp, K.G. 1984, Applications of Walsh Functions and Related Functions (New York: Academic Press) [non-Fourier transforms].   
Pollard, J.M. 1971, “The Fast Fourier Transform in a Finite Field,” Mathematics of Computation, vol. 25, pp. 365–374.[7]   
McClellan, J.H., and Rader, C.M. 1979, Number Theory in Digital Signal Processing (New York: Prentice-Hall).[8]   
Heideman, M.T., Johnson, D.H., and Burris, C.S. 1984, “Gauss and the History of the Fast Fourier Transform,” IEEE ASSP Magazine, pp. 14–21 (October).

# 12.3 FFT of Real Functions

It happens frequently that the data whose FFT is desired consist of real-valued samples $f _ { j }$ ; $j = 0 \ldots N - 1$ . To use four1, we put these into a complex array with all imaginary parts set to zero. The resulting transform $F _ { n }$ ; $n = 0 \dots N - 1$ satisfies $\left( F _ { N - n } \right) ^ { * } = F _ { n }$ . Since this complex-valued array has real values for $F _ { 0 }$ and $F _ { N / 2 }$ , and $( N / 2 ) - 1$ other independent values $F _ { 1 } \dots F _ { N / 2 - 1 }$ , it has the same $2 ( N / 2 - 1 ) + 2 = N$ “degrees of freedom” as the original, real data set. However, the use of the full complex FFT algorithm for real data is inefficient, both in execution time and in storage required. You would think that there is a better way.

Actually, there are two better ways.

# 12.3.1 Transform of Two Real Functions Simultaneously

The first better way is “mass production”: Pack two separate real functions into the input array in such a way that their individual transforms can be separated from the result. This may remind you of a one-cent sale, at which you are coerced to purchase two of an item when you only need one. However, remember that for correlations and convolutions the Fourier transforms of two functions are involved, and this is a handy way to do them both at once.

Here is how to exploit the symmetry of the FFT to handle two real functions at once: Pack the two data arrays as the real and imaginary parts, respectively, of the complex input array of four1 and take the transform. This gives

$$
H _ { n } = \sum _ { j } e ^ { 2 \pi i j n / N } ( f _ { j } + i g _ { j } )
$$

Now look at the $N - n$ component, and take its complex conjugate,

$$
( H _ { N - n } ) ^ { * } = \left( \sum _ { j } e ^ { 2 \pi i j ( N - n ) / N } ( f _ { j } + i g _ { j } ) \right) ^ { * } = \sum _ { j } e ^ { 2 \pi i j n / N } ( f _ { j } - i g _ { j } )
$$

where we have used $f _ { j } ^ { * } = f _ { j }$ and $g _ { j } ^ { * } = g _ { j }$ . Now, adding and subtracting equations (12.3.1) and (12.3.2) gives

$$
H _ { n } + H _ { N - n } ^ { * } = 2 F _ { n } , \qquad H _ { n } - H _ { N - n } ^ { * } = 2 i G _ { n }
$$

Equations (12.3.3) with $n = 0 , 1 , \ldots , N / 2$ easily yield the independent (zero and positive frequency) components of the two desired transforms $F _ { n }$ and $G _ { n }$ . Note that $F _ { 0 } , G _ { 0 } , F _ { N / 2 }$ , and $G _ { N / 2 }$ are real (using $H _ { 0 } = H _ { N }$ ), but that the other values are, in general, complex.

What about the reverse process? This is even easier. Using the symmetries $F _ { N - n } = F _ { n } ^ { * }$ and $G _ { N - n } \ = \ G _ { n } ^ { * }$ , form $F _ { n } + i G _ { n }$ for $0 \leq n < N$ . Now take the inverse FFT. The real and imaginary parts of the resulting complex array are the two desired real functions.

The only potential drawback of this method occurs if $f$ and $g$ are very different in scale. Then roundoff error can cause the smaller function’s FFT to be inaccurate.

# 12.3.2 FFT of a Single Real Function

To implement the second method, which allows us to perform the FFT of a single real function without redundancy, we split the data set in half, thereby forming two real arrays of half the size. We can apply the method above to these two, but of course the result will not be the transform of the original data. It will be a schizophrenic combination of two transforms, each of which has half of the information we need. Fortunately, this schizophrenia is treatable. It works like this:

The right way to split the original data is to take the even-numbered $f _ { j }$ as one data set, and the odd-numbered $f _ { j }$ as the other. The beauty of this is that we can take the original real array and treat it as a complex array $h _ { j }$ of half the length. The first data set is the real part of this array, and the second is the imaginary part, just as was described above. No repacking is required. In other words, $h _ { j } = f _ { 2 j } + i f _ { 2 j + 1 }$ , $j = 0 , \ldots , N / 2 - 1$ . We submit this to four1, and it gives back a complex array $H _ { n } = F _ { n } ^ { e } + i F _ { n } ^ { o }$ , $n = 0 , \ldots , N / 2 - 1$ with

$$
\begin{array} { l } { { { \cal F } _ { n } ^ { e } = \displaystyle \sum _ { k = 0 } ^ { N / 2 - 1 } f _ { 2 k } e ^ { 2 \pi i k n / ( N / 2 ) } } } \\ { { { \cal F } _ { n } ^ { o } = \displaystyle \sum _ { k = 0 } ^ { N / 2 - 1 } f _ { 2 k + 1 } e ^ { 2 \pi i k n / ( N / 2 ) } } } \end{array}
$$

The previous discussion tells us how to separate the two transforms $F _ { n } ^ { e }$ and $F _ { n } ^ { o }$ out of $H _ { n }$ . How do you work them into the transform $F _ { n }$ of the original data set $f _ { j }$ ? Simply glance back at equation (12.2.3):

$$
F _ { n } = F _ { n } ^ { e } + e ^ { 2 \pi i n / N } F _ { n } ^ { o } \qquad n = 0 , \dots , N - 1
$$

Expressed directly in terms of the transform $H _ { n }$ of our real (masquerading as complex) data set, the result is

$$
F _ { n } = \frac { 1 } { 2 } ( H _ { n } + H _ { N / 2 - n } ^ { * } ) - \frac { i } { 2 } ( H _ { n } - H _ { N / 2 - n } ^ { * } ) e ^ { 2 \pi i n / N } \qquad n = 0 , \dots , N - 1
$$

A few remarks:

- Since frequ $F _ { N - n } ^ { * } = F _ { n }$ , there is no point in saving the entire spectrum. The positiveufficient and can be stored in the same array as the original data. The operation can, in fact, be done in place.   
- Even so, we need values $H _ { n }$ ; $n = 0 , \ldots , N / 2$ , whereas four1 gives only the values $n = 0 , \ldots , N / 2 - 1$ . Symmetry to the rescue, ${ \cal H } _ { N / 2 } = { \cal H } _ { 0 }$ .   
- The values $F _ { 0 }$ and $F _ { N / 2 }$ are real and independent. In order to actually get the entire $F _ { n }$ in the original array space, it is convenient to put $F _ { N / 2 }$ into the imaginary part of $F _ { 0 }$ .   
- Despite its complicated form, the process above is invertible. First peel $F _ { N / 2 }$ out of $F _ { 0 }$ . Then construct

$$
\begin{array} { l } { { F _ { n } ^ { e } = { \frac { 1 } { 2 } } ( F _ { n } + F _ { N / 2 - n } ^ { * } ) } } \\ { { F _ { n } ^ { o } = { \frac { 1 } { 2 } } e ^ { - 2 \pi i n / N } ( F _ { n } - F _ { N / 2 - n } ^ { * } ) \qquad n = 0 , \dots , N / 2 - 1 } } \end{array}
$$

and use four1 to find the inverse transform of $H _ { n } = F _ { n } ^ { ( 1 ) } + i F _ { n } ^ { ( 2 ) }$ . Surprisingly, the actual algebraic steps are virtually identical to those of the forward transform.

Here is a representation of what we have said:

# void realft(VecDoub_IO &data, const Int isign) {

Calculates the Fourier transform of a set of n real-valued data points. Replaces these data (which are stored in array data $\left[ 0 \cdot \cdot \mathbf { n } \mathbf { - } 1 \right]$ ) by the positive frequency half of their complex Fourier transform. The real-valued first and last components of the complex transform are returned as elements data[0] and data[1], respectively. n must be a power of 2. This routine also calculates the inverse transform of a complex data array if it is the transform of real data. (Result in this case must be multiplied by $2 / \mathtt { n }$ .)

Int i,i1,i2,i3,i4,n=data.size();   
Doub $\mathtt { c 1 = 0 }$ .5,c2,h1r,h1i,h2r,h2i,wr,wi,wpr,wpi,wtemp;   
Doub theta $^ { = 3 }$ .141592653589793238/Doub $. n { > } > 1 )$ ; Initialize the recurrence.   
if (isign $\scriptstyle = = \ 1$ ) { $\mathsf { c } 2 \ = \ - 0 . 5$ ; four1(data,1); The forward transform is here.   
} else { $\mathtt { c 2 = 0 }$ .5; Otherwise set up for an inverse transtheta $=$ -theta; form.   
}   
wtemp=sin(0.5\*theta);   
wpr $=$ -2.0\*wtemp\*wtemp;   
wpi sin(theta);   
$\mathtt { w r } = 1$ .0+wpr;   
wi=wpi;   
for (i=1;i<(n>>2);i++) { i2=1+(i1=i+i); $\div 4 = 1 +$ (i3=n-i1); h1r=c1\*(data[i1]+data[i3]); h1i $=$ c1\*(data[i2]-data[i4]); h2r= -c2\*(data[i2]+data[i4]); h2i ${ . } =$ c2\*(data[i1]-data[i3]); data[i1]=h1r+wr\*h2r-wi\*h2i; data[i2] $=$ h1i+wr\*h2i+wi\*h2r; data[i3] $=$ h1r-wr\*h2r+wi\*h2i; data[i4] $=$ -h1i+wr\*h2i+wi\*h2r; $\kappa x =$ (wtemp=wr)\*wpr-wi\*wpi+wr; wi $\equiv$ wi\*wpr+wtemp\*wpi+wi;   
}   
if (isign $\scriptstyle = = \ 1$ ) { data[0] $=$ (h1r=data[0])+data[1]; data[1] $=$ h1r-data[1];   
} else { data[0] $= _ { \mathsf { C } } 1 *$ ((h1r $=$ data[0])+data[1]); data[1] $=$ c1\*(h1r-data[1]); four1(data,-1);   
}   
Case $\mathtt { i } = 0$ done separately below.   
The two separate transforms are separated out of data.   
Here they are recombined to form the true transform of the original real data.   
The recurrence.   
Squeeze the first and last data together to get them all within the original array.   
This is the inverse transform for the case isign $\scriptstyle = - 1$ .

You can’t use WrapVecDoub (-12.2) to access the output of realft as complex values; it assumes a wraparound order that is not valid when we are storing only the positive part of the spectrum. An even simpler trick, however, is to define an inline function

inline Complex\* Cmplx(VecDoub &d) {return (Complex \*)&d[0];}

and then write things like

Cmplx(data)[k] $=$ Complex(...   
cvalue $=$ Cmplx(data)[k];

when you want to set or get the $\mathtt { k } ^ { t h }$ complex value in data, viewed as a complex array. (You are still responsible for separating the two real values stored in the first complex component, however.)

# CITED REFERENCES AND FURTHER READING:

Brigham, E.O. 1974, The Fast Fourier Transform (Englewood Cliffs, NJ: Prentice-Hall), $\ S 1 0 – 1 0$ .   
Sorensen, H.V., Jones, D.L., Heideman, M.T., and Burris, C.S. 1987, “Real-Valued Fast Fourier Transform Algorithms,” IEEE Transactions on Acoustics, Speech, and Signal Processing, vol. ASSP-35, pp. 849–863.   
Hockney, R.W. 1971, in Methods in Computational Physics, vol. 9 (New York: Academic Press).   
Russ, J.C. 2002, The Image Processing Handbook, 4th ed. (Boca Raton, FL: CRC Press)   
Clarke, R.J. 1985, Transform Coding of Images, (Reading, MA: Addison-Wesley).   
Gonzalez, R.C., and Woods, R.E. 1992, Digital Image Processing, 2nd ed. (Reading, MA: Addison-Wesley).

# 12.4 Fast Sine and Cosine Transforms

Among their other uses, the Fourier transforms of functions can be used to solve differential equations (see $\ S 2 0 . 4 )$ . The most common boundary conditions for the solutions are (i)

![](images/eb71230505bdf930b303916d6126d4ec511a950b17291b1306f1172fba073c57.jpg)  
Figure 12.4.1. Basis functions used by the Fourier transform (a), sine transform (b), and cosine transform (c) are plotted. The first five basis functions are shown in each case. (For the Fourier transform, the real and imaginary parts of the basis functions are both shown.) While some basis functions occur in more than one transform, the basis sets are distinct. For example, the sine transform functions labeled (1), (3), (5) are not present in the Fourier basis. Any of the three sets can expand any function in the interval shown; however, the sine or cosine transform best expands functions matching the boundary conditions of the respective basis functions, namely zero function values for sine, zero derivatives for cosine.

they have the value zero at the boundaries, or (ii) their derivatives are zero at the boundaries. In the first instance, the natural transform to use is the sine transform, while in the second, one of several variations of the cosine transform is a natural choice.

# 12.4.1 Sine Transform

The sine transform is given by

$$
F _ { k } = \sum _ { j = 1 } ^ { N - 1 } f _ { j } \sin ( \pi j k / N ) 
$$

where $f _ { j } , \ j = 0 , \ldots , N - 1$ is the data array, and $f _ { 0 } \equiv 0$ .

At first blush this appears to be simply the imaginary part of the discrete Fourier transform. However, the argument of the sine differs by a factor of two from the value that would make this so. The sine transform uses sines only as a complete set of functions in the interval from 0 to $2 \pi$ , and, as we shall see, the cosine transform uses cosines only. By contrast, the normal FFT uses both sines and cosines, but only half as many of each. (See Figure 12.4.1.)

The expression (12.4.1) can be “force-fit” into a form that allows its calculation via the FFT. The idea is to extend the given function rightward past its last tabulated value. We extend the data to twice their length in such a way as to make them an odd function about $j = N$ , with $f _ { N } = 0$ ,

$$
f _ { 2 N - j } \equiv - f _ { j } \qquad j = 0 , \dots , N - 1
$$

Consider the FFT of this extended function:

$$
F _ { k } = \sum _ { j = 0 } ^ { 2 N - 1 } f _ { j } e ^ { 2 \pi i j k / ( 2 N ) }
$$

The half of this sum from $j ~ = ~ N$ to $j ~ = ~ 2 N - 1$ can be rewritten with the substitution $j ^ { \prime } = 2 N - j$ ,

$$
\begin{array} { l } { { \displaystyle \sum _ { j = N } ^ { 2 N - 1 } f _ { j } e ^ { 2 \pi i j k / ( 2 N ) } = \sum _ { j ^ { \prime } = 1 } ^ { N } f _ { 2 N - j ^ { \prime } } e ^ { 2 \pi i ( 2 N - j ^ { \prime } ) k / ( 2 N ) } } } \\ { { \displaystyle \qquad = - \sum _ { j ^ { \prime } = 0 } ^ { N - 1 } f _ { j ^ { \prime } } e ^ { - 2 \pi i j ^ { \prime } k / ( 2 N ) } } } \end{array}
$$

so that

$$
\begin{array} { c } { { { \displaystyle F _ { k } = \sum _ { j = 0 } ^ { N - 1 } f _ { j } \left[ e ^ { 2 \pi i j k / ( 2 N ) } - e ^ { - 2 \pi i j k / ( 2 N ) } \right] } } } \\ { { { } } } \\ { { { = 2 i \sum _ { j = 0 } ^ { N - 1 } f _ { j } \sin ( \pi j k / N ) } } } \end{array}
$$

Thus, up to a factor $2 i$ we get the sine transform from the FFT of the extended function.

This method introduces a factor of two inefficiency into the computation by extending the data. This inefficiency shows up in the FFT output, which has zeros for the real part of every element of the transform. For a one-dimensional problem, the factor of two may be bearable, especially in view of the simplicity of the method. When we work with partial differential equations in two or three dimensions, though, the factor becomes four or eight, so efforts to eliminate the inefficiency are well rewarded.

From the original real data array $f _ { j }$ we will construct an auxiliary array $y _ { j }$ and apply to it the routine realft. The output will then be used to construct the desired transform. For the sine transform of data $f _ { j } , \ j = 1 , \dots , N - 1$ , the auxiliary array is

$$
\begin{array} { l } { { y _ { 0 } = 0 } } \\ { { } } \\ { { y _ { j } = \sin ( j \pi / N ) ( f _ { j } + f _ { N - j } ) + \frac { 1 } { 2 } ( f _ { j } - f _ { N - j } ) \qquad j = 1 , \ldots , N - 1 } } \end{array}
$$

This array is of the same dimension as the original. Notice that the first term is symmetric about $j = N / 2$ and the second is antisymmetric. Consequently, when realft is applied to $y _ { j }$ , the result has real parts $R _ { k }$ and imaginary parts $I _ { k }$ given by

$$
\begin{array} { l } { { \displaystyle R _ { k } = \sum _ { j = 0 } ^ { N - 1 } y _ { j } \cos ( 2 \pi j k / N ) } } \\ { ~ } \\ { { \displaystyle \quad = \sum _ { j = 1 } ^ { N - 1 } ( f _ { j } + f _ { N - j } ) \sin ( j \pi / N ) \cos ( 2 \pi j k / N ) } } \\ { { \displaystyle \quad = \sum _ { j = 0 } ^ { N - 1 } 2 f _ { j } \sin ( j \pi / N ) \cos ( 2 \pi j k / N ) } } \end{array}
$$

$$
\begin{array} { r l } & { \quad = \displaystyle \sum _ { j = 0 } ^ { N - 1 } f _ { j } \left[ \sin \frac { ( 2 k + 1 ) j \pi } { N } - \sin \frac { ( 2 k - 1 ) j \pi } { N } \right] } \\ & { \quad = F _ { 2 k + 1 } - F _ { 2 k - 1 } } \\ { I _ { k } = \displaystyle \sum _ { j = 0 } ^ { N - 1 } y _ { j } \sin ( 2 \pi j k / N ) } \\ & { \quad = \displaystyle \sum _ { j = 1 } ^ { N - 1 } ( f _ { j } - f _ { N - j } ) \frac { 1 } { 2 } \sin ( 2 \pi j k / N ) } \\ & { \quad = \displaystyle \sum _ { j = 0 } ^ { N - 1 } f _ { j } \sin ( 2 \pi j k / N ) } \\ & { \quad = \displaystyle \sum _ { j = 0 } ^ { N - 1 } f _ { j } \sin ( 2 \pi j k / N ) } \\ & { \quad = F _ { 2 k } } \\ & { \quad = F _ { 2 k } } \end{array}
$$

Therefore, $F _ { k }$ can be determined as follows:

$$
F _ { 2 k } = I _ { k } \qquad F _ { 2 k + 1 } = F _ { 2 k - 1 } + R _ { k } \qquad k = 0 , \ldots , ( N / 2 - 1 )
$$

The even terms of $F _ { k }$ are thus determined very directly. The odd terms require a recursion, the starting point of which follows from setting $k = 0$ in equation (12.4.9) and using $F _ { 1 } = - F _ { - 1 }$

$$
\begin{array} { r } { F _ { 1 } = \frac { 1 } { 2 } R _ { 0 } } \end{array}
$$

The implementing program is

# void sinft(VecDoub_IO &y) {

Calculates the sine transform of a set of n real-valued data points stored in array $\mathtt { y } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ . The number n must be a power of 2. On exit, y is replaced by its transform. This program, without changes, also calculates the inverse sine transform, but in this case the output array should be multiplied by $2 / \mathtt { n }$ .

Int j,n=y.size();   
Doub sum,y1,y2,theta,wi ${ = } 0$ .0, $\mathtt { w r } { = } 1$ .0,wpi,wpr,wtemp;   
theta $^ { = 3 }$ .141592653589793238/Doub(n); Initialize the recurrence.   
wtemp=sin(0.5\*theta);   
wpr -2.0\*wtemp\*wtemp;   
wpi $\equiv$ sin(theta);   
y[0] ${ = } 0$ .0;   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<(n>>1)+1;j++) { wr=(wtemp=wr)\*wpr-wi\*wpi+wr; Calculate the sine for the auxiliary array. wi=wi\*wpr+wtemp\*wpi+wi; The cosine is needed to continue the recurrence. y1=wi\*(y[j]+y[n-j]); Construct the auxiliary array. y2=0.5\*(y[j]-y[n-j]); y[j]=y1+y2; Terms $j$ and $N - j$ are related. y[n-j]=y1-y2;   
realft(y,1); Transform the auxiliary array.   
y[0] $\ast = 0$ .5; Initialize the sum used for odd terms below.   
sum=y[1]=0.0;   
for (j=0;j<n-1; $\mathrm { j } + = 2 .$ ) { sum $+ =$ y[j]; y[j]=y[j+1]; Even terms determined directly. y[j+1]=sum; Odd terms determined by this running sum.   
}

The sine transform, curiously, is its own inverse. If you apply it twice, you get the original data, but multiplied by a factor of $N / 2$ .

# 12.4.2 Cosine Transform

The other common boundary condition for differential equations is that the derivative of the function is zero at the boundary. In this case, the natural transform is the cosine transform. There are several possible ways of defining the transform. Each can be thought of as resulting from a different way of extending a given array to create an even array of double the length, and/or from whether the extended array contains $2 N - 1 , 2 N$ , or some other number of points. In practice, only two of the numerous possibilities are useful, so we will restrict ourselves to just these two.

The first form of the cosine transform uses $N + 1$ data points:

$$
F _ { k } = \frac { 1 } { 2 } [ f _ { 0 } + ( - 1 ) ^ { k } f _ { N } ] + \sum _ { j = 1 } ^ { N - 1 } f _ { j } \cos ( \pi j k / N )
$$

It results from extending the given array to an even array about $j = N$ , with

$$
f _ { 2 N - j } = f _ { j } , \qquad j = 0 , \dots , N - 1
$$

If you substitute this extended array into equation (12.4.3) and follow steps analogous to those leading up to equation (12.4.5), you will find that the Fourier transform is just twice the cosine transform (12.4.11). Another way of thinking about the formula (12.4.11) is to notice that it is the Chebyshev-Gauss-Lobatto quadrature formula (see $\ S 4 . 6 )$ , often used in Clenshaw-Curtis adaptive quadrature (see $\ S 5 . 9$ , equation 5.9.4).

Once again the transform can be computed without the factor of two inefficiency. In this case the auxiliary function is

$$
y _ { j } = { \textstyle \frac { 1 } { 2 } } ( f _ { j } + f _ { N - j } ) - \sin ( j \pi / N ) ( f _ { j } - f _ { N - j } ) \qquad j = 0 , \ldots , N - 1
$$

Instead of equation (12.4.9), realft now gives

$$
F _ { 2 k } = R _ { k } \qquad F _ { 2 k + 1 } = F _ { 2 k - 1 } + I _ { k } \qquad k = 0 , \ldots , ( N / 2 - 1 )
$$

The starting value for the recursion for odd $k$ in this case is

$$
F _ { 1 } = \frac { 1 } { 2 } ( f _ { 0 } - f _ { N } ) + \sum _ { j = 1 } ^ { N - 1 } f _ { j } \cos ( j \pi / N )
$$

This sum does not appear naturally among the $R _ { k }$ and $I _ { k }$ , and so we accumulate it during the generation of the array $y _ { j }$ .

Once again this transform is its own inverse, and so the following routine works for both directions of the transformation. Note that although this form of the cosine transform has $N + 1$ input and output values, it passes an array only of length $N$ to realft.

# void cosft1(VecDoub_IO &y) {

Calculates the cosine transform of a set $\mathtt { y } [ 0 \ldots \mathtt { n } ]$ of real-valued data points. The transformed data replace the original data in array y. n must be a power of 2. This program, without changes, also calculates the inverse cosine transform, but in this case the output array should be multiplied by $2 / \mathtt { n }$ .

const Doub $\mathtt { P I } = 3$ .141592653589793238;   
Int j, $\mathrm { n } { = } \mathrm { y }$ .size()-1;   
Doub sum,y1,y2,theta,wi ${ = } 0$ .0,wpi,wpr,wr=1.0,wtemp;   
VecDoub yy(n); Need array of length n, not $\tt { n } { + } 1$ , for realft.   
theta $\mathtt { \Gamma = P T / n }$ ; Initialize the recurrence.   
wtemp=sin(0.5\*theta);   
$\boldsymbol { \mathrm { w p r } } \ = \ - 2$ .0\*wtemp\*wtemp;   
wpi $=$ sin(theta);   
sum $\mathtt { \mathtt { = 0 } }$ .5\*(y[0]-y[n]);   
yy[0] ${ = } 0$ .5\*(y[0]+y[n]);   
for $\scriptstyle \dot { \mathcal { I } } = 1$ ;j<n/2;j $^ { + + }$ ) {

Carry out the recurrence.

Calculate the auxiliary function.

The values for $j$ and $N - j$ are related.

wr=(wtemp=wr)\*wpr-wi\*wpi+wr; wi=wi\*wpr+wtemp\*wpi+wi; y1=0.5\*(y[j]+y[n-j]); y2=(y[j]-y[n-j]); yy[j]=y1-wi\*y2; yy[n-j]=y1+wi\*y2; sum += wr\*y2; yy[n/2]=y[n/2]; realft(yy,1); for (j=0;j<n;j++) y[j]=yy[j]; y[n]=y[1]; y[1] $=$ sum; for (j=3;j<n; $\mathrm { j } + = 2 \mathrm { \cdot }$ ) { sum $+ =$ y[j]; y[j] $=$ sum; }

Carry along this sum for later use in unfolding the transform.   
$\mathtt { y } [ \mathtt { n } / 2 ]$ unchanged.   
Calculate the transform of the auxiliary function.

sum is the value of $F _ { 1 }$ in equation (12.4.15).

Equation (12.4.14).

}

The second important form of the cosine transform is defined by

$$
F _ { k } = \sum _ { j = 0 } ^ { N - 1 } f _ { j } \cos { \frac { \pi k ( j + { \frac { 1 } { 2 } } ) } { N } }
$$

with inverse

$$
f _ { j } = \frac 2 N \sum _ { k = 0 } ^ { N - 1 } F _ { k } \cos \frac { \pi k ( j + \frac 1 2 ) } N
$$

Here the prime on the summation symbol means that the term for $k = 0$ has a coefficient of $\textstyle { \frac { 1 } { 2 } }$ in front. This form arises by extending the given data, defined for $j = 0 , \ldots , N - 1$ , to $j = N , \ldots , 2 N - 1$ in such a way that they are even about the point $N - { \frac { 1 } { 2 } }$ and periodic. (They are therefore also even about $j = - \frac { 1 } { 2 }$ .) The form (12.4.17) is related to Gauss-Chebyshev quadrature (see equation 4.6.19), to Chebyshev approximation (-5.8, equation 5.8.7), and Clenshaw-Curtis quadrature (-5.9).

This form of the cosine transform is useful when solving differential equations on “staggered” grids, where the variables are centered midway between mesh points. It is also the standard form in the field of data compression and image processing.

The auxiliary function used in this case is similar to equation (12.4.13):

$$
y _ { j } = { \frac { 1 } { 2 } } ( f _ { j } + f _ { N - j - 1 } ) + \sin { \frac { \pi ( j + { \frac { 1 } { 2 } } ) } { N } } ( f _ { j } - f _ { N - j - 1 } ) \qquad j = 0 , \ldots , N - 1
$$

Carrying out the steps similar to those used to get from (12.4.6) to (12.4.9), we find

$$
\begin{array} { l } { { F _ { 2 k } = \cos \displaystyle \frac { \pi k } { N } R _ { k } - \sin \displaystyle \frac { \pi k } { N } I _ { k } } } \\ { { F _ { 2 k - 1 } = \sin \displaystyle \frac { \pi k } { N } R _ { k } + \cos \displaystyle \frac { \pi k } { N } I _ { k } + F _ { 2 k + 1 } } } \end{array}
$$

Note that equation (12.4.20) gives

$$
\begin{array} { r } { F _ { N - 1 } = \frac { 1 } { 2 } R _ { N / 2 } } \end{array}
$$

Thus the even components are found directly from (12.4.19), while the odd components are found by recursing (12.4.20) down from $k = N / 2 - 1$ , using (12.4.21) to start.

Since the transform is not self-inverting, we have to reverse the above steps to find the inverse. Here is the routine:

# void cosft2(VecDoub_IO &y, const Int isign) {

Calculates the “staggered” cosine transform of a set $\mathtt { y } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ of real-valued data points. The transformed data replace the original data in array y. n must be a power of 2. Set isign to $+ 1$ for a transform, and to $^ { - 1 }$ for an inverse transform. For an inverse transform, the output array should be multiplied by $2 / \mathtt { n }$ .

Transform the auxiliary function.   
Even terms.   
const Doub $\mathtt { P I } = 3$ .141592653589793238;   
Int i,n=y.size();   
Doub sum,sum1,y1,y2,ytemp,theta,w $\scriptstyle { \frac { } { } } = 0$ .0,   
theta ${ = } 0$ . $5 { * } \mathrm { P I / n }$ ;   
wr1=cos(theta);   
wi1=sin(theta);   
$\boldsymbol { \mathrm { w p r } } \ = \ - 2$ .0\*wi1\*wi1;   
wpi=sin(2. $^ { 0 * }$ theta);   
if (isign $\mathbf { \omega } = \mathbf { \omega } 1$ ) { for (i=0;i<n/2;i++) { y1=0.5\*(y[i]+y[n-1-i]); y2=wi1\*(y[i]-y[n-1-i]); y[i]=y1+y2; y[n-1-i]=y1-y2; wr1=(wtemp=wr1)\*wpr-wi1\*wpi+wr1; wi1=wi1\*wpr+wtemp\*wpi+wi1; } realft(y,1); for (i=2;i<n;i+=2) { wr=(wtemp=wr)\*wpr-wi\*wpi+wr; wi=wi\*wpr+wtemp\*wpi+wi; y1=y[i]\*wr-y[i+1]\*wi; y2=y[i+1]\*wr+y[i]\*wi; y[i]=y1; y[i+1]=y2; } sum=0.5\*y[1]; for (i=n-1;i>0;i-=2) { sum1 $_ { , } =$ sum; sum $+ =$ y[i]; y[i] $=$ sum1; }   
} else if (isign == -1) { ytemp=y[n-1]; for (i=n-1;i>2;i-=2) y[i]=y[i-2]-y[i]; y[1]=2.0\*ytemp; for (i=2;i<n; $\scriptstyle \dot { 1 } + = 2$ ) { wr=(wtemp=wr)\*wpr-wi\*wpi+wr; wi=wi\*wpr+wtemp\*wpi+wi; y1=y[i]\*wr+y[i+1]\*wi; y2=y[i+1]\*wr-y[i]\*wi; y[i]=y1; y[i+1]=y2; } realft(y,-1); for (i=0;i<n/2;i++) { y1=y[i]+y[n-1-i]; y2=(0.5/wi1)\*(y[i]-y[n-1-i]); y[i]=0.5\*(y1+y2); y[n-1-i]=0.5\*(y1-y2); wr1=(wtemp=wr1)\*wpr-wi1\*wpi+wr1; wi1=wi1\*wpr+wtemp\*wpi+wi1; }   
}

Form difference of odd terms.

Calculate $R _ { k }$ and $I _ { k }$

Invert auxiliary array.

An alternative way of implementing this algorithm is to form an auxiliary function by copying the even elements of $f _ { j }$ into the first $N / 2$ locations, and the odd elements into the next $N / 2$ elements in reverse order. However, it is not easy to implement the alternative algorithm without a temporary storage array and we prefer the above in-place algorithm.

Finally, we mention that there exist fast cosine transforms for small $N$ that do not rely on an auxiliary function or use an FFT routine. Instead, they carry out the transform directly, often coded in hardware for fixed $N$ of small dimension [1].

# CITED REFERENCES AND FURTHER READING:

Walker, J.S. 1996, Fast Fourier Transforms, 2nd ed. (Boca Raton, FL: CRC Press)

Rao, K.R. and Yip, P. 1990, Discrete Cosine Transform: Algorithms, Advantages, Applications (San Diego, CA: Academic Press)

Hou, H.S. 1987, “A Fast, Recursive Algorithm for Computing the Discrete Cosine Transform,” IEEE Transactions on Acoustics, Speech,and Signal Processing, vol. ASSP-35,pp.1455- 1461 [see for additional references].

Chen, W., Smith, C.H., and Fralick, S.C. 1977, “A Fast Computational Algorithm for the Discrete Cosine Transform,” IEEE Transactions on Communications, vol. COM-25, pp. 1004– 1009.[1]

# 12.5 FFT in Two or More Dimensions

Given a complex function $h ( k _ { 1 } , k _ { 2 } )$ defined over the two-dimensional grid $0 \leq$ $k _ { 1 } \leq N _ { 1 } - 1$ ; $0 \leq k _ { 2 } \leq N _ { 2 } - 1$ , we can define its two-dimensional discrete Fourier transform as a complex function $H ( n _ { 1 } , n _ { 2 } )$ , defined over the same grid,

$$
H ( n _ { 1 } , n _ { 2 } ) \equiv \sum _ { k _ { 2 } = 0 } ^ { N _ { 2 } - 1 } \sum _ { k _ { 1 } = 0 } ^ { N _ { 1 } - 1 } \mathrm { e x p } ( 2 \pi i k _ { 2 } n _ { 2 } / N _ { 2 } ) \mathrm { e x p } ( 2 \pi i k _ { 1 } n _ { 1 } / N _ { 1 } ) h ( k _ { 1 } , k _ { 2 } )
$$

By pulling the “subscripts $2 ^ { \circ }$ exponential outside of the sum over $k _ { 1 }$ , or by reversing the order of summation and pulling the “subscripts $1 ^ { \circ }$ outside of the sum over $k _ { 2 }$ , we can see instantly that the two-dimensional FFT can be computed by taking onedimensional FFTs sequentially on each index of the original function. Symbolically,

$$
\begin{array} { r l r } & { } & { H ( n _ { 1 } , n _ { 2 } ) = { \mathrm { F F T - o n - i n d e x - 1 ~ } } ( { \mathrm { F F T - o n - i n d e x - 2 ~ } } [ h ( k _ { 1 } , k _ { 2 } ) ] ) } \\ & { } & { = { \mathrm { F F T - o n - i n d e x - 2 ~ } } ( { \mathrm { F F T - o n - i n d e x - 1 ~ } } [ h ( k _ { 1 } , k _ { 2 } ) ] ) } \end{array}
$$

For this to be practical, of course, both $N _ { 1 }$ and $N _ { 2 }$ should be some efficient length for an FFT, usually a power of 2. Programming a two-dimensional FFT, using (12.5.2) with a one-dimensional FFT routine, is a bit clumsier than it seems at first. Because the one-dimensional routine requires that its input be in consecutive order as a onedimensional complex array, you find that you are endlessly copying things out of the multidimensional input array and then copying things back into it. This is not recommended technique. Rather, you should use a multidimensional FFT routine, such as the one we give below.

The generalization of (12.5.1) to more than two dimensions, say to $L$ dimensions, is evidently

$$
\begin{array} { c } { { \displaystyle H ( n _ { 1 } , \ldots , n _ { L } ) \equiv \sum _ { k _ { L } = 0 } ^ { N _ { L } - 1 } \cdots \sum _ { k _ { 1 } = 0 } ^ { N _ { 1 } - 1 } \exp ( 2 \pi i k _ { L } n _ { L } / N _ { L } ) \times \cdots } } \\ { { \times \exp ( 2 \pi i k _ { 1 } n _ { 1 } / N _ { 1 } ) h ( k _ { 1 } , \ldots , k _ { L } ) } } \end{array}
$$

where $n _ { 1 }$ and $k _ { 1 }$ range from 0 to $N _ { 1 } - 1 , \ldots$ , and $n _ { L }$ and $k _ { L }$ range from 0 to $N _ { L } - 1$ . How many calls to a one-dimensional FFT are in (12.5.3)? Quite a few! For each value of $k _ { 1 } , k _ { 2 } , \ldots , k _ { L - 1 }$ you FFT to transform the $L$ index. Then for each value of $k _ { 1 } , k _ { 2 } , \ldots , k _ { L - 2 }$ and $n _ { L }$ you FFT to transform the $L - 1$ index. And so on. It is best to rely on someone else having done the bookkeeping for once and for all.

The inverse transforms of (12.5.1) or (12.5.3) are just what you would expect them to be: Change the $i$ ’s in the exponentials to $- i$ ’s, and put an overall factor of $1 / ( N _ { 1 } { \times } { \dots } { \times } N _ { L } )$ in front of the whole thing. Most other features of multidimensional FFTs are also analogous to features already discussed in the one-dimensional case:

- Frequencies are arranged in wraparound order in the transform, but now for each separate dimension. The input data are also treated as if they were wrapped around. If they are discontinuous across this periodic identification (in any dimension), then the spectrum will have some excess power at high frequencies because of the discontinuity. The fix, if you care, is to remove multidimensional linear trends. If you are doing spatial filtering and are worried about wraparound effects, then you need to zero-pad all around the border of the multidimensional array. However, be sure to notice how costly zero-padding is in multidimensional transforms. If you use too thick a zero-pad, you are going to waste a lot of storage, especially in three or more dimensions!   
- Aliasing occurs as always if sufficient bandwidth limiting does not exist along one or more of the dimensions of the transform.

The routine fourn that we furnish herewith is a descendant of one written by N.M. Brenner. It requires as input (i) a vector, telling the length of the array in each dimension, e.g., .32; 64/ (note that these lengths must all be powers of 2, and are the numbers of complex values in each direction); (ii) the usual scalar equal to $\pm 1$ indicating whether you want the transform or its inverse; and, finally, (iii) the array of data. The number of dimensions is determined from the length of the vector in (i).

A few words about the data array: fourn accesses it as a one-dimensional array of real numbers, that is, data $[ 0 \dots ( 2 N _ { 1 } N _ { 2 } \dots N _ { L } ) - 1 ]$ , of length equal to twice the product of the lengths of the $L$ dimensions. It assumes that the array represents an $L$ -dimensional complex array, with individual components ordered as follows: (i) each complex value occupies two sequential locations, a real part followed by an imaginary; (ii) the first subscript changes least rapidly as one goes through the array; the last subscript changes most rapidly (that is, “store by rows,” the $\mathrm { C } { + + }$ norm). Figure 12.5.1 illustrates the format of the output array.

As for four1 earlier, we find it useful to give a bare form of the routine, where the data array is passed as a pointer, and then an overloaded function that passes the data array (by reference) as a VecDoub.

![](images/037c2ba5d2dfc22d98b31309447f69878e112293e4b86a853d6180fe3cc7231f.jpg)  
Figure 12.5.1. Storage arrangement of frequencies in the output $H ( f _ { 1 } , f _ { 2 } )$ of a two-dimensional FFT. The input data is a two-dimensional $N _ { 1 } \times N _ { 2 }$ array $h ( t _ { 1 } , t _ { 2 } )$ (stored by columns of complex numbers). The output is also stored by complex columns. Each column corresponds to a particular value of $f _ { 2 }$ , as shown in the figure. Within each column, the arrangement of frequencies $f _ { 1 }$ is exactly as shown in Figure 12.2.2. $\Delta _ { 1 }$ and $\Delta _ { 2 }$ are the sampling intervals in the 1 and 2 directions, respectively. The total number of (real) array elements is $2 N _ { 1 } N _ { 2 }$ . The program fourn can also do more than two dimensions, and the storage arrangement generalizes in the obvious way.

# void fourn(Doub \*data, VecInt_I &nn, const Int isign) {

Replaces data by its ndim-dimensional discrete Fourier transform, if isign is input as 1. nn[0..ndim-1] is an integer array containing the lengths of each dimension (number of complex values), which must all be powers of 2. data is a real array of length twice the product of these lengths, in which the data are stored as in a multidimensional complex array: real and imaginary parts of each element are in consecutive locations, and the rightmost index of the array increases most rapidly as one proceeds along data. For a two-dimensional array, this is equivalent to storing the array by rows. If isign is input as $^ { - 1 }$ , data is replaced by its inverse transform times the product of the lengths of all dimensions.

Int idim,i1,i2,i3,i2rev,i3rev,ip1,ip2,ip3,ifp1,ifp2;   
Int ibit,k1,k2,n,nprev,nrem,ntot ${ = } 1$ ,ndim=nn.size();   
Doub tempi,tempr,theta,wi,wpi,wpr,wr,wtemp;   
for (idim=0;idim<ndim;idim $^ { + + }$ ) ntot $\ast =$ nn[idim]; Total no. of complex values.   
if (ntot<2 || ntot&(ntot-1)) throw("must have powers of 2 in fourn");   
nprev=1;   
for (idim=ndim-1;idim> $\scriptstyle \mathtt { \mathtt { . 0 } }$ ;idim--) { Main loop over the dimensions. n=nn[idim]; nrem=ntot/(n\*nprev); ip1=nprev << 1; ip2=ip1\*n; ip3=ip2\*nrem; i2rev=0; for (i2=0;i2<ip2;i2+=ip1) { This is the bit-reversal secif (i2 < i2rev) { tion of the routine.

for (i1=i2;i1<i2+ip1-1;i1 $+ { = } 2$ ) { for ( $\therefore 3 = \dot { \bf 1 } 1$ ;i3<ip3;i3+=ip2) { i3rev=i2rev+i3-i2; SWAP(data[i3],data[i3rev]); SWAP(data[i3+1],data[i3rev+1]); } } } ibit $=$ ip2 >> 1; while (ibit $> =$ ip1 && i2rev+1 $>$ ibit) { i2rev $- =$ ibit; ibit $> > = ~ 1$ ; } i2rev $+ =$ ibit; } ifp1 ${ . } =$ ip1; Here begins the Danielsonwhile (ifp1 $<$ ip2) { Lanczos section of the ifp2=ifp1 << 1; routine. theta isign\*6.28318530717959/(ifp2/ip1); Initialize for the trigonometwtemp=sin(0.5\*theta); ric recurrence. wpr $=$ -2.0\*wtemp\*wtemp; wpi=sin(theta); $\mathtt { w r } = 1$ .0; wi=0.0; for (i3=0;i3<ifp1;i3 $+ =$ ip1) { for (i1=i3;i1<i3+ip1-1;i1 $+ { = } 2$ ) for (i2=i1;i2<ip3;i2 $+ =$ ifp2) { $\mathtt { k 1 } \mathtt { = i } 2$ ; Danielson-Lanczos formula: k2=k1+ifp1; tempr=wr\*data[k2]-wi\*data[k2+1]; tempi $=$ wr\*data[k2+1]+wi\*data[k2]; data[k2] $=$ data[k1]-tempr; data[k2+1] $=$ data[k1+1]-tempi; data[k1] $+ =$ tempr; data[k1+1] $+ =$ tempi; } } wr=(wtemp=wr)\*wpr-wi\*wpi+wr; Trigonometric recurrence. wi=wi\*wpr+wtemp\*wpi+wi; } ifp1=ifp2; } nprev \*= n;

void fourn(VecDoub_IO &data, VecInt_I &nn, const Int isign) { Overloaded version for the case where data is of type VecDoub. fourn(&data[0],nn,isign);

# CITED REFERENCES AND FURTHER READING:

Nussbaumer, H.J. 1982, Fast Fourier Transform and Convolution Algorithms (New York: Springer).

# 12.6 Fourier Transforms of Real Data in Two and Three Dimensions

Two-dimensional FFTs are particularly important in the field of image processing. An image is usually represented as a two-dimensional array of pixel intensities, real (and usually positive) numbers. One commonly desires to filter high, or low, frequency spatial components from an image; or to convolve or deconvolve the image with some instrumental point spread function. Use of the FFT is by far the most efficient technique.

In three dimensions, a common use of the FFT is to solve Poisson’s equation for a potential (e.g., electromagnetic or gravitational) on a three-dimensional lattice that represents the discretization of three-dimensional space. Here the source terms (mass or charge distribution) and the desired potentials are also real. In two and three dimensions, with large arrays, memory is often at a premium. It is therefore important to perform the FFTs, insofar as possible, on the data “in place.” We want a routine with functionality similar to the multidimensional FFT routine fourn (-12.5), but which operates on real, not complex, input data. We give such a routine in this section. The development is analogous to that of $\ S 1 2 . 3$ leading to the one-dimensional routine realft. (You might wish to review that material at this point, particularly equation 12.3.6.)

It is convenient to think of the independent variables $n _ { 1 } , \ldots , n _ { L }$ in equation (12.5.3) as representing an $L$ -dimensional vector $\vec { n }$ in wave-number space, with values on the lattice of integers. The transform $H ( n _ { 1 } , \dots , n _ { L } )$ is then denoted $H ( \vec { n } )$ .

It is easy to see that the transform $H ( \vec { n } )$ is periodic in each of its $L$ dimensions. Specifically, if $\vec { P } _ { 1 } , \vec { P } _ { 2 } , \vec { P } _ { 3 } , \ldots$ denote the vectors $( N _ { 1 } , 0 , 0 , \ldots ) , ( 0 , N _ { 2 } , 0 , \ldots )$ , $( 0 , 0 , N _ { 3 } , \ldots )$ , and so forth, then

$$
H ( \vec { n } \pm \vec { P } _ { j } ) = H ( \vec { n } ) \qquad j = 1 , \ldots , L
$$

Equation (12.6.1) holds for any input data, real or complex. When the data are real, we have the additional symmetry

$$
H ( - \vec { n } ) = H ( \vec { n } ) ^ { * }
$$

Equations (12.6.1) and (12.6.2) imply that the full transform can be trivially obtained from the subset of lattice values $\vec { n }$ that have

$$
\begin{array} { c } { { 0 \leq n _ { 1 } \leq N _ { 1 } - 1 } } \\ { { 0 \leq n _ { 2 } \leq N _ { 2 } - 1 } } \\ { { \ldots } } \\ { { 0 \leq n _ { L } \leq \displaystyle \frac { N _ { L } } { 2 } } } \end{array}
$$

In fact, this set of values is overcomplete, because there are additional symmetry relations among the transform values that have $n _ { L } = 0$ and $n _ { L } = N _ { L } / 2$ . However, these symmetries are complicated and their use becomes extremely confusing. Therefore, we will compute our FFT on the lattice subset of equation (12.6.3), even though this requires a small amount of extra storage for the answer, i.e., the transform is not quite “in place.” (Although an in-place transform is in fact possible, we have found it virtually impossible to explain to any user how to unscramble its output, i.e., where to find the real and imaginary components of the transform at some particular frequency!)

As a “bare” routine, we will implement the multidimensional real Fourier transform for the three-dimensional case $L \ = \ 3$ , with the input data stored as a real three-dimensional array data $\left[ 0 \cdot \cdot \mathrm { n n 1 - 1 } \right] \left[ 0 \cdot \cdot \mathrm { n n 2 - 1 } \right] \left[ 0 \cdot \cdot \mathrm { n n 3 - 1 } \right]$ . This scheme will allow two-dimensional data to be processed with effectively no loss of efficiency simply by choosing $\mathtt { n n 1 } = 1$ . (Note that it must be the first dimension that is set to 1.) We also provide more convenient overloaded functions whose input data are stored as a Mat3DDoub (for three-dimensional data) or as a MatDoub (for two-dimensional data).

The output spectrum comes back packaged, logically at least, as a complex three-dimensional array that we can call spec[0..nn1-1][0..nn2-1][0..nn3/2] (cf. equation 12.6.3). In the first two of its three dimensions, the respective frequency values $f _ { 1 }$ or $f _ { 2 }$ are stored in wraparound order, that is, with zero frequency in the first index value, the smallest positive frequency in the second index value, the smallest negative frequency in the last index value, and so on (cf. the discussion leading up to routines four1 and fourn). The third of the three dimensions returns only the positive half of the frequency spectrum. Figure 12.6.1 shows the logical storage scheme. The returned portion of the complex output spectrum is shown as the unshaded part of the lower figure.

The physical, as opposed to logical, packaging of the output spectrum is necessarily a bit different from the logical packaging, because, counting components, spec doesn’t quite fit into data. The subscript range spec[0..nn1-1][0..nn2-1] [0..nn3/2-1] is returned in the input array data[0..nn1-1][0..nn2-1] [ $0 \cdot \cdot \cdot \mathrm { n n } 3 - 1 ]$ , with the correspondence

$$
\begin{array} { r l } & { \mathrm { R e } ( \mathsf { s p e c } [ \mathrm { i } 1 ] [ \mathrm { i } 2 ] [ \mathrm { i } 3 ] ) = \mathrm { d a t a } [ \mathrm { i } 1 ] [ \mathrm { i } 2 ] [ 2 * \mathrm { i } 3 ] } \\ & { \mathrm { I m } ( \mathsf { s p e c } [ \mathrm { i } 1 ] [ \mathrm { i } 2 ] [ \mathrm { i } 3 ] ) = \mathrm { d a t a } [ \mathrm { i } 1 ] [ \mathrm { i } 2 ] [ 2 * \mathrm { i } 3 + 1 ] } \end{array}
$$

The remaining “plane” of values, spec[0..nn1-1][0..nn2-1][nn3/2], is returned in the two-dimensional MatDoub array speq $[ 0 \AA . \tau \mathrm { n n } 1 - 1 ] [ 0 \AA . 2 4 \mathrm { n n } 2 - 1 ]$ , with the correspondence

$$
\begin{array} { r l } & { \mathrm { R e } ( \mathtt { s p e c } [ \mathrm { i } 1 ] [ \mathrm { i } 2 ] [ \mathrm { n n } 3 / 2 ] ) = \mathtt { s p e q } [ \mathrm { i } 1 ] [ 2 * \mathrm { i } 2 ] } \\ & { \mathrm { I m } ( \mathtt { s p e c } [ \mathrm { i } 1 ] [ \mathrm { i } 2 ] [ \mathrm { n n } 3 / 2 ] ) = \mathtt { s p e q } [ \mathrm { i } 1 ] [ 2 * \mathrm { i } 2 + 1 ] } \end{array}
$$

Note that speq contains only frequency components whose third component $f _ { 3 }$ is at the Nyquist critical frequency $\pm f _ { c }$ . In some applications these values will in fact be ignored or set to zero, since they are intrinsically aliased between positive and negative frequencies.

With this much introduction, the implementing procedure, called rlft3, is something of an anticlimax. Look in the innermost loop in the procedure, and you will see equation (12.3.6) implemented on the last transform index. The case of $\therefore 3 = 0$ is coded separately, to account for the fact that speq is to be filled instead of overwriting the input array of data. The three enclosing for loops (indices i2, i3, and i1, from inside to outside) could in fact be done in any order — their actions all commute. We chose the order shown because of the following considerations: (i)

![](images/4c1aa0f19eb630d87dc39b8f85fcd17d53df53985dc899195140c81c3c9449a0.jpg)  
Figure 12.6.1. Input and output data arrangements for $\tt r 1 f t t 3$ . All arrays shown are presumed to have a first (leftmost) dimension of range $[ 0 \cdot \cdot \cdot \mathrm { \bf n n } 1 - 1 ]$ , coming out of the page. The input data array is a real three-dimensional array data $\left[ 0 \AA . \mathrm { \bf ~ . n n 1 - 1 } \right] \left[ 0 \mathrm { \bf . ~ . n n 2 - 1 } \right] \left[ 0 \mathrm { \bf . ~ . n n 3 - 1 } \right] .$ . (For two-dimensional data, one sets $\smash { \mathtt { n n 1 } = 1 } .$ .) The output data can be viewed as a single complex array with dimensions $[ 0 , . \mathrm { \ n n } 1 - 1 ] [ 0 , . \mathrm { \ n n } 2 - 1 ] [ 0 , . \mathrm { \ n n } 3 / 2 ]$ (cf. equation 12.6.3), corresponding to the frequency components $f _ { 1 }$ and $f _ { 2 }$ being stored in wraparound order, but only positive $f _ { 3 }$ values being stored (others being obtainable by symmetry). The output data are actually returned mostly in the input array data, but partly stored in the real array speq[0..nn1-1][0..2\*nn2-1]. See text for details.

i3 should not be the inner loop, because if it is, then the recurrence relations on wr and wi become burdensome. (ii) On modern processors with a cache hierarchy, i1 should be the outer loop, because (with $\mathrm { C } { + } { + }$ order of array storage) this results in the array data, which might be very large, being accessed in block sequential order.

Keep in mind that all the computing in rlft3 is negligible, by a logarithmic factor, compared with the actual work of computing the associated complex FFT, done in the routine fourn. Complex operations are carried out explicitly in terms of real and imaginary parts. The routine rlft3 is based on an earlier routine by G.B. Rybicki. As previously, it is convenient to provide a bare routine, and then more convenient overloaded functions. The overload for three-dimensional data inputs the data as a Mat3DDoub, with speq a MatDoub. The overload for two-dimensional data inputs the data as a MatDoub, with speq a VecDoub.

# void rlft3(Doub \*data, Doub \*speq, const Int isign, const Int nn1, const Int nn2, const Int nn3) {

Given a three-dimensional real array data[0..nn1-1][0..nn2-1][0..nn3-1] (where $\mathbf { n n } 1 = 1$ for the case of a logically two-dimensional array), this routine returns (for isign $^ { = 1 }$ ) the complex fast Fourier transform as two complex arrays: On output, data contains the zero and positive frequency values of the third frequency component, while speq[0..nn1-1][0.. $\AA . 2 * \mathrm { n n } 2 \mathrm { - } 1 ]$ contains the Nyquist critical frequency values of the third frequency component. First (and second) frequency components are stored for zero, positive, and negative frequencies, in standard wraparound order. See text for description of how complex values are arranged. For $\mathrm { i } \mathsf { s i g n } \mathsf { = } \mathsf { - } 1$ , the inverse transform (times $\mathtt { n n 1 * n n 2 * n n 3 / 2 }$ as a constant multiplicative factor) is performed, with output data (viewed as a real array) deriving from input data (viewed as complex) and speq. For inverse transforms on data not generated first by a forward transform, make sure the complex input data array satisfies property (12.6.2). The dimensions nn1, nn2, nn3 must always be integer powers of 2.

Int i1,i2,i3,j1,j2,j3,k1,k2,k3,k4;   
Doub theta,wi,wpi,wpr,wr,wtemp;   
Doub c1,c2,h1r,h1i,h2r,h2i;   
VecInt nn(3);   
VecDoubp spq(nn1);   
for ( $\div 1 = 0$ ;i1<nn1;i1 $^ { + + }$ ) spq[i1] $=$ speq + 2\*nn2\*i1;   
$\mathsf { c } 1 \ = \ 0 . 5$ ;   
c2 = -0.5\*isign;   
theta $=$ isign\*(6.28318530717959/nn3);   
wtemp $=$ sin(0.5\*theta);   
wpr = -2.0\*wtemp\*wtemp;   
wpi $=$ sin(theta);   
nn[0] $=$ nn1;   
nn[1] $=$ nn2;   
nn[2] $=$ nn3 >> 1;   
if (isign $\mathbf { \omega } = \mathbf { \omega } 1$ ) { Case of forward transform. fourn(data,nn,isign); Here is where most all of the com-$\mathtt { k 1 } = 0$ ; pute time is spent. for ( $\scriptstyle { \dot { 1 } } 1 = 0$ ;i1<nn1;i1++) Extend data periodically into speq. for ( $\scriptstyle { \dot { 1 } } 2 = 0$ , $y 2 = 0$ ;i2<nn2;i2++,k1 $+ { = }$ nn3) { spq[i1][j2++] $=$ data[k1]; spq[i1][j $2 + + ]$ $=$ data[k1+1]; }

for (i1=0;i1<nn1;i1 $^ { + + }$ ) { $\mathbf { j } 1 \mathbf { = } ( \mathrm { i } 1 \mathbf { \alpha } 1 \mathbf { = } \ 0 \mathbf { \alpha } ? \mathbf { n } \mathbf { n } 1 \mathbf { - } \mathrm { i } 1 \mathbf { \alpha } : \mathbf { \alpha } 0 )$ ; Zero frequency is its own reflection, otherwise locate corresponding negative frequency in wraparound order. $\mathtt { w r } = 1$ .0; Initialize trigonometric recurrence. $\mathtt { w i } = 0 . 0$ ; for (i3=0;i3 $< =$ (nn3>>1);i3+=2) { k1=i1\*nn2\*nn3; k3=j1\*nn2\*nn3;

for (i2=0;i2<nn2;i2++,k1 $+ =$ nn3) { if $\mathrm { i } 3 \ = 0 .$ ) { Equation (12.3.6). j2=(i2 != 0 ? ((nn2-i2)<<1) : 0); h1r=c1\*(data[k1]+spq[j1][j2]); h1i=c1\*(data[k1+1]-spq[j1][j2+1]); h2i=c2\*(data[k1]-spq[j1][j2]); h2r= -c2\*(data[k1+1]+spq[j1][j2+1]); data[k1] $\ c =$ h1r+h2r; data[k1+1] $=$ h1i+h2i; spq[j1][j2] $\risingdotseq$ h1r-h2r; spq[j1][j2+1] $=$ h2i-h1i; } else { j2=(i2 != 0 ? nn2-i2 : 0); j3=nn3-i3; k2=k1+i3; k4=k3+j2\*nn3+j3; h1r=c1\*(data[k2]+data[k4]); h1i=c1\*(data[k2+1]-data[k4+1]); h2i=c2\*(data[k2]-data[k4]); h2r= -c2\*(data[k2+1]+data[k4+1]); data[k2] $=$ h1r+wr\*h2r-wi\*h2i; data[k2+1] $=$ h1i+wr\*h2i+wi\*h2r; data[k4] $=$ h1r-wr\*h2r+wi\*h2i; data[k4 $^ +$ 1] $=$ -h1i+wr\*h2i+wi\*h2r; } wr=(wtemp=wr)\*wpr-wi\*wpi+wr; Do the recurrence. wi=wi\*wpr+wtemp\*wpi+wi; }   
}   
if (isign $\ c = - 1$ ) fourn(data,nn,isign); Case of reverse trans

void rlft3(Mat3DDoub_IO &data, MatDoub_IO &speq, const Int isign) { Overloaded version for three-dimensional data. When isign is 1, replace data and spec by data’s three-dimensional FFT. When isign is 1, the inverse transform (times one-half the product of data’s dimensions) is performed. See comments in version above.

if (speq.nrows() $\downarrow =$ data.dim1() || speq.ncols() $\ ! =$ 2\*data.dim2()) throw("bad dims in rlft3"); rlft3(&data[0][0][0],&speq[0][0],isign,data.dim1(),data.dim2(),data.dim3());

void rlft3(MatDoub_IO &data, VecDoub_IO &speq, const Int isign) { Overloaded version for two-dimensional data. When isign is 1, replace data and spec by data’s two-dimensional FFT. When isign is $^ { - 1 }$ , the inverse transform (times one-half the product of data’s dimensions) is performed. See comments in version above.

if (speq.size() $! = ~ 2 *$ data.nrows()) throw("bad dims in rlft3");   
rlft3(&data[0][0],&speq[0],isign,1,data.nrows(),data.ncols());

# }

As in earlier sections of this chapter, we can use a bit of $\mathrm { C } { + + }$ trickery to access the output Fourier components (logical array spec) more easily. We define two overloaded helper functions (the first of which is identical to the definition in section $\ S 1 2 . 3 )$

inline Complex\* Cmplx(VecDoub &d) {return (Complex \*)&d[0];} inline Complex\* Cmplx(Doub ${ \ast } \mathsf { d } .$ ) {return (Complex \*)d;}

Now suppose that data is two-dimensional with input dimensions $\tt { n x }$ and ny. Then, on output, a complex frequency component $( \dot { \bf 1 } , \dot { \bf 3 } )$ , with $0 \leq \mathrm { i } \leq \mathtt { n x } / 2$ and $0 \leq \mathrm { j ~ \leq ~ }$ $\mathrm { n y } / 2 - 1$ , can be accessed as

Cmplx(data[i])[j]

![](images/6e31084fd8b6557f6f13b174dead01604a7653880e50edf16d696b008b0f5896.jpg)  
Figure 12.6.2. Fourier processing of an image. Upper left: Original image. Upper right: Blurred by lowpass filtering. Lower left: Sharpened by enhancing high frequency components. Lower right: Magnitude of the derivative operator as computed in Fourier space.

Yes, the right parenthesis really is between the subscripts! The corresponding negative (wraparound) frequencies are at

# Cmplx(data[nx-i])[j]

but now with $1 \leq \mathrm { i } \leq \mathrm { n x } / 2 - 1$ . The Nyquist critical values ${ \dot { \mathsf { J } } } = { \mathsf { n y } } / 2$ can be accessed as

# Cmplx(speq)[i]

for $0 \leq \mathrm { i } \leq \mathtt { n x } / 2$ and

# Cmplx(speq)[nx-i]

for $1 \leq \mathrm { i } \leq \mathrm { n x } / 2 - 1 .$ . If you don’t understand how this all works, a useful exercise is to locate each of these expressions in Figure 12.6.1. All of the above expressions can be l-values as well as r-values.

Figure 12.6.2 shows a test image and three examples of processing with rlft3 (using the overloaded function for two-dimensional data). The first example is a simple low-pass filter. A sharp image becomes blurry when its high-frequency spatial components are suppressed by the factor (here) max $( 1 - 6 f ^ { 2 } / f _ { c } ^ { 2 } , 0 )$ . The second example is a sharpening filter where high frequencies are enhanced. Code for producing this image looks something like this:

Int i, j, $\mathtt { n x } mathtt { = } 2 5 6$ , $\scriptstyle { \mathtt { n y } } = 2 5 6$ ; Image is $2 5 6 \times 2 5 6$ .   
MatDoub data(nx,ny);   
VecDoub speq(2\*nx);   
Doub fac; Here we would fill data with the image.   
rlft3(data,speq,1); Forward transform.   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<nx/2; $\dot { \bf 1 } + +$ ) for ( $\scriptstyle \mathbf { j } = 0$ ;j<ny/2;j++) { Loop over all frequencies exfac $=$ 1.+3.\*sqrt(SQR(i\*2./nx)+SQR(j\*2./ny)); cept Nyquist. Cmplx(data[i])[j] $\ast =$ fac; if (i>0) Cmplx(data[nx-i])[j] $\ast =$ fac; Negative (wraparound) fre-  
} quencies.   
for (j=0;j<ny/2;j++) { Loop over frequencies where i is Nyquist. fac $=$ 1.+3.\*sqrt(1.+SQR(j\*2./ny)); Cmplx(data[nx/2])[j] $\ast =$ fac;   
}   
for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<nx/2;i++) { Loop over frequencies where j is Nyquist. fac = 1.+3.\*sqrt(SQR(i\*2./nx)+1.); Cmplx(speq)[i] $\ast =$ fac; if (i>0) Cmplx(speq)[nx-i] $\ast =$ fac; Wraparound.   
}   
Cmplx(speq)[nx/2] $\ast =$ (1.+3.\*sqrt(2.)); Both i and $\mathrm { j }$ are Nyquist.   
rlft3(data,speq,-1); Reverse transform.

The third example is a derivative filter, where a Fourier component at frequency $( f _ { x } , f _ { y } )$ is multiplied by $2 \pi i ( f _ { x } ^ { 2 } + f _ { y } ^ { 2 } ) ^ { 1 / 2 }$ , and the resulting intensities are then linearly mapped into an appropriate range.

To extend rlft3 to four dimensions, you simply add an additional (outer) nested for loop in i0, analogous to the present i1. (Modifying the routine to do an arbitrary number of dimensions, as in fourn, is a good programming exercise for the reader.)

# CITED REFERENCES AND FURTHER READING:

Brigham, E.O. 1974, The Fast Fourier Transform (Englewood Cliffs, NJ: Prentice-Hall).   
Swartztrauber, P. N. 1986, “Symmetric FFTs,” Mathematics of Computation, vol. 47, pp. 323– 346.   
Hutchinson, J. 2001, in IEEE Professional Communication Society Newsletter, vol. 45, no. 3. See also http://www.lenna.org.[1]

# 12.7 External Storage or Memory-Local FFTs

Sometime in your life, you might have to compute the Fourier transform of a really large data set, larger than the size of your computer’s physical memory. In such a case, the data will be stored on some external medium, such as magnetic or optical disk. Needed is an algorithm that makes some manageable number of sequential passes through the external data, processing it on the fly and outputting intermediate results to other external media, which can be read on subsequent passes.

In fact, an algorithm of just this description was developed by Singleton [1] very soon after the discovery of the FFT. The algorithm requires four sequential storage devices, each capable of holding half of the input data. The first half of the input data is initially on one device, the second half on another.

Singleton’s algorithm is based on the observation that it is possible to bit reverse $2 ^ { M }$ values by the following sequence of operations: On the first pass, values are read alternately from the two input devices, and written to a single output device (until it holds half the data), and then to the other output device. On the second pass, the output devices become input devices, and vice versa. Now, we copy two values from the first device, then two values from the second, writing them (as before) first to fill one output device, then to fill a second. Subsequent passes read 4, 8, etc., input values at a time. After completion of pass $M - 1$ , the data are in bit-reverse order.

Singleton’s next observation is that it is possible to alternate the passes of essentially this bit-reversal technique with passes that implement one stage of the Danielson-Lanczos combination formula (12.2.3). The scheme, roughly, is this: One starts as before with half the input data on one device and half on another. In the first pass, one complex value is read from each input device. Two combinations are formed, and one is written to each of two output devices. After this “computing” pass, the devices are rewound, and a “permutation” pass is performed, where groups of values are read from the first input device and alternately written to the first and second output devices; when the first input device is exhausted, the second is similarly processed. This sequence of computing and permutation passes is repeated $M - K - 1$ times, where $2 ^ { K }$ is the size of internal buffer available to the program. The second phase of the computation consists of a final $K$ computation passes. What distinguishes the second phase from the first is that, now, the permutations are local enough to do in place during the computation. There are thus no separate permutation passes in the second phase. In all, there are $2 M - K - 2$ passes through the data.

An implementation of Singleton’s algorithm, fourfs, based on reference [1], is given in a Webnote [2].

For one-dimensional data, Singleton’s algorithm produces output in exactly the same order as a standard FFT (e.g., four1). For multidimensional data, the output is in transpose order rather than in the conventional $\mathrm { C } { + } { + }$ array order output by fourn. That is, in scanning through the data, it is the leftmost array index that cycles most quickly, then the second leftmost, and so on. This peculiarity, which is intrinsic to the method, is generally only a minor inconvenience. For convolutions, one simply computes the component-by-component product of two transforms in their nonstandard arrangement, and then does an inverse transform on the result. Note that, if the lengths of the different dimensions are not all the same, then you must reverse the order of the values in nn[0..ndim-1] (thus giving the dimensions of the transpose-order output array) before performing the inverse transform. Note also that, just like fourn, performing a transform and then an inverse results in multiplying the original data by the product of the lengths of all dimensions.

We leave it as an exercise for the reader to figure out how to reorder fourfs’s output into normal order, taking additional passes through the externally stored data. We doubt that such reordering is ever really needed.

You will likely want to modify fourfs to fit your particular application. For example, as written, $\mathtt { K B F } \equiv 2 ^ { K }$ plays the dual role of being the size of the internal buffers, and the record size of the unformatted reads and writes. The latter role limits its size to that allowed by your machine’s I/O facility. It is a simple matter to perform multiple reads for a much larger KBF, thus reducing the number of passes by a few.

Another modification of fourfs would be for the case where your virtual memory machine has sufficient address space, but not sufficient physical memory, to do an efficient FFT by the conventional algorithm (whose memory references are extremely nonlocal). In that case, you will need to replace the reads, writes, and rewinds by mappings of the arrays afa, afb, and afc into your address space. In other words, these arrays are replaced by references to a single data array, with offsets that get modified wherever fourfs performs an I/O operation. The resulting algorithm will have its memory references local within blocks of size KBF. Execution speed is thereby sometimes increased enormously, albeit at the cost of requiring twice as much virtual memory as an in-place FFT.

# CITED REFERENCES AND FURTHER READING:

Singleton, R.C. 1967, “A Method for Computing the Fast Fourier Transform with Auxiliary Memory and Limited High-speed Storage,” IEEE Transactions on Audio and Electroacoustics, vol. AU-15, pp. 91–97.[1]

Numerical Recipes Software 2007, “Code for External or Memory-Local Fourier Transform,” Numerical Recipes Webnote No.18,at http://www.nr.com/webnotes?18 [2]

Oppenheim, A.V., Schafer, R.W., and Buck, J.R. 1999, Discrete-Time Signal Processing, 2nd ed. (Englewood Cliffs, NJ: Prentice-Hall), Chapter 9.

# Fourier and Spectral Applications

# 13.0 Introduction

Fourier methods have revolutionized fields of science and engineering, from astronomy to medical imaging, from seismology to spectroscopy. In this chapter, we present some of the basic applications of Fourier and spectral methods that have made these revolutions possible.

Say the word “Fourier” to a numericist, and the response, as if by Pavlovian conditioning, will likely be “FFT.” Indeed, the wide application of Fourier methods must be credited principally to the existence of the fast Fourier transform. Better mousetraps move over: If you speed up any nontrivial algorithm by a factor of a million or so, the world will beat a path toward finding useful applications for it. The most direct applications of the FFT are to the convolution or deconvolution of data (-13.1), correlation and autocorrelation (-13.2), optimal filtering (-13.3), power spectrum estimation (-13.4), and the computation of Fourier integrals (-13.9).

As important as they are, however, FFT methods are not the be-all and end-all of spectral analysis. Section 13.5 is a brief introduction to the field of time-domain digital filters. In the spectral domain, one limitation of the FFT is that it always represents a function’s Fourier transform as a polynomial in $z = \exp ( 2 \pi i f \Delta )$ (cf. equation 12.1.7). Sometimes, processes have spectra whose shapes are not well represented by this form. An alternative form, which allows the spectrum to have poles in $Z$ , is used in the techniques of linear prediction (-13.6) and maximum entropy spectral estimation (-13.7).

Another significant limitation of all FFT methods is that they require the input data to be sampled at evenly spaced intervals. For irregularly or incompletely sampled data, other (albeit slower) methods are available, as discussed in $\ S 1 3 . 8$ .

So-called wavelet methods inhabit a representation of function space that is neither in the temporal nor in the spectral domain, but rather somewhere in-between. Section 13.10 is an introduction to this subject. Finally, $\ S 1 3 . 1 1$ is an excursion into the numerical use of the Fourier sampling theorem.

![](images/6cd756bed3c8fd6b1ab7b07851c4df568c602e606a87f0050b8c5527d1bb997e.jpg)  
Figure 13.1.1. Example of the convolution of two functions. A signal $s ( t )$ is convolved with a response function $r ( t )$ . Since the response function is broader than some features in the original signal, these are “washed out” in the convolution. In the absence of any additional noise, the process can be reversed by deconvolution.

# 13.1 Convolution and Deconvolution Using the FFT

We have defined the convolution of two functions for the continuous case in equation (12.0.9), and have given the convolution theorem as equation (12.0.10). The theorem says that the Fourier transform of the convolution of two functions is equal to the product of their individual Fourier transforms. Now, we want to deal with the discrete case. We will mention first the context in which convolution is a useful procedure, and then discuss how to compute it efficiently using the FFT.

The convolution of two functions $r ( t )$ and $s ( t )$ , denoted $r \ast s$ , is mathematically equal to their convolution in the opposite order, $s \ast r$ . Nevertheless, in most applications the two functions have quite different meanings and characters. One of the functions, say $s$ , is typically a signal or data stream, which goes on indefinitely in time (or in whatever the appropriate independent variable may be). The other function $r$ is a “response function,” typically a peaked function that falls to zero in both directions from its maximum. The effect of convolution is to smear the signal $s ( t )$ in time according to the recipe provided by the response function $r ( t )$ , as shown in Figure 13.1.1. In particular, a spike or delta-function of unit area in $s$ which occurs at some time $t _ { 0 }$ is supposed to be smeared into the shape of the response function itself, but translated from time 0 to time $t _ { 0 }$ as $r ( t - t _ { 0 } )$ .

In the discrete case, the signal $s ( t )$ is represented by its sampled values at equal time intervals $s _ { j }$ . The response function is also a discrete set of numbers $r _ { k }$ , with the following interpretation: $r _ { 0 }$ tells what multiple of the input signal in one channel (one particular value of $j$ ) is copied into the identical output channel (same value of $j$ ); $r _ { 1 }$ tells what multiple of input signal in channel $j$ is additionally copied into output channel $j + 1$ ; $r _ { - 1 }$ tells the multiple that is copied into channel $j - 1$ ; and so on for both positive and negative values of $k$ in $r _ { k }$ . Figure 13.1.2 illustrates the situation.

![](images/3a08dd60d54e35af84b8fcec56ea0388da4cb19fc8af01e7a4971fed02f87c0a.jpg)  
Figure 13.1.2. Convolution of discretely sampled functions. Note how the response function for negative times is wrapped around and stored at the extreme right end of the array $r _ { k }$ .

Example: A response function with $r _ { 0 } ~ = ~ 1$ and all other $r _ { k }$ ’s equal to zero is just the identity filter. Convolution of a signal with this response function gives identically the signal. Another example is the response function with $r _ { 1 4 } = 1 . 5$ and all other $r _ { k }$ ’s equal to zero. This produces convolved output that is the input signal multiplied by 1:5 and delayed by 14 sample intervals.

Evidently, we have just described in words the following definition of discrete convolution with a response function of finite duration $M$ :

$$
( r * s ) _ { j } \equiv \sum _ { k = - M / 2 + 1 } ^ { M / 2 } s _ { j - k } r _ { k }
$$

If a discrete response function is nonzero only in some range $- M / 2 < k \leq M / 2$ , where $M$ is a sufficiently large even integer, then the response function is called a finite impulse response (FIR), and its duration is $M$ . (Notice that we are defining $M$ as the number of nonzero values of $r _ { k }$ ; these values span a time interval of $M - 1$ sampling times.) In most practical circumstances the case of finite $M$ is the case of interest, either because the response really has a finite duration, or because we choose to truncate it at some point and approximate it by a finite-duration response function.

The discrete convolution theorem is this: If a signal $s _ { j }$ is periodic with period $N$ , so that it is completely determined by the $N$ values $s _ { 0 } , \ldots , s _ { N - 1 }$ , then its discrete convolution with a response function of finite duration $N$ is a member of the discrete Fourier transform pair,

$$
\sum _ { k = - N / 2 + 1 } ^ { N / 2 } s _ { j - k } r _ { k } \Longleftrightarrow S _ { n } R _ { n }
$$

Here $S _ { n }$ . $( n = 0 , \ldots , N - 1 )$ is the discrete Fourier transform of the values $s _ { j }$ $( j =$ $0 , \ldots , N - 1 )$ , while $R _ { n }$ $( n = 0 , \ldots , N - 1 )$ is the discrete Fourier transform of the values $r _ { k }$ . $( k = 0 , \ldots , N - 1 )$ . These values of $r _ { k }$ are the same as for the range $k = - N / 2 + 1 , \dots , N / 2$ , but in wraparound order, exactly as was described at the end of $\ S 1 2 . 2$ .

# 13.1.1 Treatment of End Effects by Zero Padding

The discrete convolution theorem presumes a set of two circumstances that are not universal. First, it assumes that the input signal is periodic, whereas real data often either go forever without repetition or else consist of one nonperiodic stretch of finite length. Second, the convolution theorem takes the duration of the response to be the same as the period of the data; they are both $N$ . We need to work around these two constraints.

The second is very straightforward. Almost always, one is interested in a response function whose duration $M$ is much shorter than the length of the data set $N$ . In this case, you simply extend the response function to length $N$ by padding it with zeros, i.e., define $r _ { k } ~ = ~ 0$ for $M / 2 \ \leq \ k \ \leq \ N / 2$ and also for $- N / 2 +$ $1 \le \le - M / 2 + 1$ . Dealing with the first constraint is more challenging. Since the convolution theorem rashly assumes that the data are periodic, it will falsely “pollute” the first output channel $( r * s ) _ { 0 }$ with some wrapped-around data from the far end of the data stream $s _ { N - 1 } , s _ { N - 2 }$ , etc. (See Figure 13.1.3.) So, we need to set up a buffer zone of zero-padded values at the end of the $s _ { j }$ vector, in order to make this pollution zero. How many zero values do we need in this buffer? Exactly as many as the most negative index for which the response function is nonzero. For example, if $r _ { - 3 }$ is nonzero while $r _ { - 4 } , r _ { - 5 } , \ldots .$ are all zero, then we need three zero pads at the end of the data: $s _ { N - 3 } = s _ { N - 2 } = s _ { N - 1 } = 0$ . These zeros will protect the first output channel $( r * s ) _ { 0 }$ from wraparound pollution. It should be obvious that the second output channel $( r * s ) _ { 1 }$ and subsequent ones will also be protected by these same zeros. Let $K$ denote the number of padding zeros, so that the last actual input data point is $s N { - } K { - } 1$ .

What now about pollution of the very last output channel? Since the data now end with $s N { - } K { - } 1$ , the last output channel of interest is $( r * s ) _ { N - K - 1 }$ . This channel can be polluted by wraparound from input channel $s _ { 0 }$ unless the number $K$ is also large enough to take care of the most positive index $k$ for which the response function $r _ { k }$ is nonzero. For example, if $r _ { 0 }$ through $r _ { 6 }$ are nonzero, while $r _ { 7 }$ ; r8 : : : are all zero, then we need at least $K = 6$ padding zeros at the end of the data: $s _ { N - 6 } = \dots =$ $s _ { N - 1 } = 0$ .

To summarize — we need to pad the data with a number of zeros on one end equal to the maximum positive duration or maximum negative duration of the response function, whichever is larger. (For a symmetric response function of duration $M$ , you will need only $M / 2$ zero pads.) Combining this operation with the padding of the response $r _ { k }$ described above, we effectively insulate the data from artifacts of undesired periodicity. Figure 13.1.4 illustrates matters.

![](images/8e1380995103e2d2083f46320d38f09881bcefcfa3e4e111aed36d4f9c5ac0b7.jpg)  
Figure 13.1.3. The wraparound problem in convolving finite segments of a function. Not only must the response function wrap be viewed as cyclic, but so must the sampled original function. Therefore, a portion at each end of the original function is erroneously wrapped around by convolution with the response function.

![](images/fc956bffc12ce597146cc098df87d21bb8ec950a082950fb54e6ba967aff3cca.jpg)  
Figure 13.1.4. Zero-padding as solution to the wraparound problem. The original function is extended by zeros, serving a dual purpose: When the zeros wrap around, they do not disturb the true convolution; and while the original function wraps around onto the zero region, that region can be discarded.

# 13.1.2 Use of FFT for Convolution

The data, complete with zero-padding, are now a set of real numbers $s _ { j }$ ; $j =$ $0 , \ldots , N - 1$ , and the response function is zero-padded out to duration $N$ and arranged in wraparound order. (Generally this means that a large contiguous section of the $r _ { k }$ ’s, in the middle of that array, is zero, with nonzero values clustered at the two extreme ends of the array.) You now compute the discrete convolution as follows: Use the FFT algorithm to compute the discrete Fourier transform of $s$ and of $r$ . Multiply the two transforms together component-by-component, remembering that the transforms consist of complex numbers. Then use the FFT algorithm to take the inverse discrete Fourier transform of the products. The answer is the convolution $r * s$ .

What about deconvolution? Deconvolution is the process of undoing the smearing in a data set that has occurred under the influence of a known response function, for example, because of the known effect of a less-than-perfect measuring apparatus. The defining equation of deconvolution is the same as that for convolution, namely (13.1.1), except now the left-hand side is taken to be known and (13.1.1) is to be considered as a set of $N$ linear equations for the unknown quantities $s _ { j }$ . Solving these simultaneous linear equations in the time domain of (13.1.1) is unrealistic in most cases, but the FFT renders the problem almost trivial. Instead of multiplying the transform of the signal and response to get the transform of the convolution, we just divide the transform of the (known) convolution by the transform of the response to get the transform of the deconvolved signal.

This procedure can go wrong mathematically if the transform of the response function is exactly zero for some value $R _ { n }$ , so that we can’t divide by it. This indicates that the original convolution has truly lost all information at that one frequency, so that a reconstruction of that frequency component is not possible. You should be aware, however, that apart from mathematical problems, the process of deconvolution has other practical shortcomings. The process is generally quite sensitive to noise in the input data, and to the accuracy to which the response function $r _ { k }$ is known. Perfectly reasonable attempts at deconvolution can sometimes produce nonsense for these reasons. In such cases you may want to make use of the additional process of optimal filtering, which is discussed in $\ S 1 3 . 3$ .

Here is our routine for convolution and deconvolution, using the FFT as implemented in realft (-12.3). The data are assumed to be stored in a VecDoub array data $\left[ 0 \cdot \cdot \mathbf { n } ^ { - 1 } \right]$ , with n an integer power of 2. The response function is assumed to be stored in wraparound order in a VecDoub array respns $\left[ 0 \cdot \cdot \cdot \mathrm { m } ^ { - 1 } \right]$ . The value of m can be any odd integer less than or equal to n, since the first thing the program does is to recopy the response function into the appropriate wraparound order in an array of length n. The answer is provided in ans, which is also used as working space.

# void convlv(VecDoub_I &data, VecDoub_I &respns, const Int isign, VecDoub_O &ans) {

Doub mag2,tmp;   
VecDoub temp(n);   
temp[0] $=$ respns[0];   
for $\scriptstyle \dot { \mathbf { 1 } } = 1$ ;i<(m+1)/2;i++) { Put respns in array of length n. temp[i] $=$ respns[i]; temp[n-i] $=$ respns[m-i];   
}   
for ( $\mathrm { i } =$ (m+1)/2;i<n-(m-1)/2;i++) Pad with zeros. temp[i]=0.0;   
for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n; $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \rho } } } ,$ ) ans[i] $=$ data[i];   
realft(ans,1); FFT both arrays.   
realft(temp,1);   
no $2 { = } \mathtt { n } { > } { > } 1$ ;   
if (isign $\scriptstyle = = \ 1$ ) { for ( $\scriptstyle \dot { 1 } = 2$ ;i<n; $\scriptstyle \dot { 1 } + = 2$ ) { Multiply FFTs to convolve. tmp=ans[i]; ans[i] $=$ (ans[i]\*temp[i]-ans[i+1]\*temp[i+1])/no2; ans[i+1] $=$ (ans[i+1]\*temp[i]+tmp\*temp[i+1])/no2; ans[0] $=$ ans[0]\*temp[0]/no2; ans[1] $=$ ans[1]\*temp[1]/no2;   
} else if (isign $\scriptstyle = { \ - 1 } ,$ ) { for (i=2;i<n; $\scriptstyle \dot { 1 } + = 2$ ) { Divide FFTs to deconvolve. if ((mag2 $\Bumpeq$ SQR(temp[i]) $^ +$ SQR(temp[i+1])) == 0.0) throw("Deconvolving at response zero in convlv"); tmp=ans[i]; ans[i] $=$ (ans[i]\*temp[i]+ans[i+1]\*temp[i+1])/mag2/no2; ans[i+1] $=$ (ans[i+1]\*temp[i]-tmp\*temp[i+1])/mag2/no2; } if (temp[0] $\scriptstyle = = \ 0 , 0$ || temp[1] $\mathrm { = = ~ 0 . 0 }$ ) throw("Deconvolving at response zero in convlv"); ans[0] $= _ { i }$ ans[0]/temp[0]/no2; ans[1] $=$ ans[1]/temp[1]/no2;   
} else throw("No meaning for isign in convlv");   
realft(ans,-1); Inverse transform back to time domain

# 13.1.3 Convolving or Deconvolving Very Large Data Sets

If your data set is so long that you do not want to fit it into memory all at once, then you must break it up into sections and convolve each section separately. Now, however, the treatment of end effects is a bit different. You have to worry not only about spurious wraparound effects, but also about the fact that the ends of each section of data should have been influenced by data at the nearby ends of the immediately preceding and following sections of data, but were not so influenced since only one section of data is in the machine at a time.

There are two, related, standard solutions to this problem. Both are fairly obvious, so with a few words of description here, you ought to be able to implement them for yourself. The first solution is called the overlap-save method. In this technique you pad only the very beginning of the data with enough zeros to avoid wraparound pollution. After this initial padding, you forget about zero-padding altogether. Bring in a section of data and convolve or deconvolve it. Then throw out the points at each end that are polluted by wraparound end effects. Output only the remaining good points in the middle. Now bring in the next section of data, but not all new data. The first points in each new section overlap the last points from the preceding section of data. The sections must be overlapped sufficiently so that the polluted output points at the end of one section are recomputed as the first of the unpolluted output points from the subsequent section. With a bit of thought you can easily determine how many points to overlap and save.

![](images/eb660aef75fb77af499d8545a5b5f363420e89291cf34d3854d95692b49801b6.jpg)  
Figure 13.1.5. The overlap-add method for convolving a response with a very long signal. The signal data are broken up into smaller pieces. Each is zero-padded at both ends and convolved (denoted by bold arrows in the figure). Finally the pieces are added back together, including the overlapping regions formed by the zero-pads.

The second solution, called the overlap-add method, is illustrated in Figure 13.1.5. Here you don’t overlap the input data. Each section of data is disjoint from the others and is used exactly once. However, you carefully zero-pad it at both ends so that there is no wraparound ambiguity in the output convolution or deconvolution. Now you overlap and add these sections of output. Thus, an output point near the end of one section will have the response due to the input points at the beginning of the next section of data properly added in to it, and likewise for an output point near the beginning of a section, mutatis mutandis.

Even when computer memory is available, there is some slight gain in computing speed in segmenting a long data set, since the FFTs’ $N \log _ { 2 } N$ is slightly slower than linear in $N$ . However, the log term is so slowly varying that you will often be much happier to avoid the bookkeeping complexities of the overlap-add or overlapsave methods: If it is practical to do so, just cram the whole data set into memory and FFT away. Then you will have more time for the finer things in life, some of which are described in succeeding sections of this chapter.

# CITED REFERENCES AND FURTHER READING:

Nussbaumer, H.J. 1982, Fast Fourier Transform and Convolution Algorithms (New York: Springer).

Elliott, D.F., and Rao, K.R. 1982, Fast Transforms: Algorithms, Analyses, Applications (New York: Academic Press).

Brigham, E.O. 1974, The Fast Fourier Transform (Englewood Cliffs, NJ: Prentice-Hall), Chapter 13.

# 13.2 Correlation and Autocorrelation Using the FFT

Correlation is the close mathematical cousin of convolution. It is in some ways simpler, however, because the two functions that go into a correlation are not as conceptually distinct as were the data and response functions that entered into convolution. Rather, in correlation, the functions are represented by different, but generally similar, data sets. We investigate their “correlation,” by comparing them both directly superposed, and with one of them shifted left or right.

We have already defined in equation (12.0.11) the correlation between two continuous functions $g ( t )$ and $h ( t )$ , which is denoted $\operatorname { C o r r } ( g , h )$ , and is a function of lag $t$ . We will occasionally show this time dependence explicitly, with the rather awkward notation $\operatorname { C o r r } ( g , h ) ( t )$ . The correlation will be large at some value of $t$ if the first function $( g )$ is a close copy of the second $( h )$ but lags it in time by $t$ , i.e., if the first function is shifted to the right of the second. Likewise, the correlation will be large for some negative value of $t$ if the first function leads the second, i.e., is shifted to the left of the second. The relation that holds when the two functions are interchanged is

$$
\operatorname { C o r r } ( g , h ) ( t ) = \operatorname { C o r r } ( h , g ) ( - t )
$$

The discrete correlation of two sampled functions $g _ { k }$ and $h _ { k }$ , each periodic with period $N$ , is defined by

$$
\displaystyle \mathrm { C o r r } ( g , h ) _ { j } \equiv \sum _ { k = 0 } ^ { N - 1 } g _ { j + k } h _ { k }
$$

The discrete correlation theorem says that this discrete correlation of two real functions $g$ and $h$ is one member of the discrete Fourier transform pair

$$
\mathrm { C o r r } ( g , h ) _ { j } \Longleftrightarrow G _ { k } H _ { k } ^ { * }
$$

where $G _ { k }$ and $H _ { k }$ are the discrete Fourier transforms of $g _ { j }$ and $h _ { j }$ , and the asterisk denotes complex conjugation. This theorem makes the same presumptions about the functions as those encountered for the discrete convolution theorem.

We can compute correlations using the FFT as follows: FFT the two data sets, multiply one resulting transform by the complex conjugate of the other, and inverse transform the product. The result (call it $r _ { k }$ ) will formally be a complex vector of length $N$ . However, it will turn out to have all its imaginary parts zero since the original data sets were both real. The components of $r _ { k }$ are the values of the correlation at different lags, with positive and negative lags stored in the by-now familiar wraparound order: The correlation at zero lag is in $r _ { 0 }$ , the first component; the correlation at lag 1 is in $r _ { 1 }$ , the second component; the correlation at lag $^ { - 1 }$ is in $r _ { N - 1 }$ , the last component; etc.

Just as in the case of convolution we have to consider end effects, since our data will not, in general, be periodic as intended by the correlation theorem. Here again, we can use zero-padding. If you are interested in the correlation for lags as large as $\pm K$ , then you must append a buffer zone of $K$ zeros at the end of both input data sets. If you want all possible lags from $N$ data points (not a usual thing), then you will need to pad the data with an equal number of zeros; this is the extreme case. So here is the program:

# void correl(VecDoub_I &data1, VecDoub_I &data2, VecDoub_O &ans) {

Computes the correlation of two real data sets data1[0..n-1] and data2[0..n-1] (including any user-supplied zero padding). n must be an integer power of 2. The answer is returned in ans[0..n-1] stored in wraparound order, i.e., correlations at increasingly negative lags are in ans[n-1] on down to ans $[ \mathtt { n } / 2 ]$ , while correlations at increasingly positive lags are in ans[0] (zero lag) on up to ans $[ \mathtt { n } / 2 \AA - 1 ]$ . Sign convention of this routine: if data1 lags data2, i.e., is shifted to the right of it, then ans will show a peak at positive lags.

Int no2,i,n=data1.size();   
Doub tmp;   
VecDoub temp(n);   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) { ans[i] $=$ data1[i]; temp[i] $=$ data2[i];   
}   
realft(ans,1); Transform both data vectors.   
realft(temp,1);   
no2=n>>1; Normalization for inverse FFT.   
for ( $\scriptstyle \dot { \mathbf { 1 } } = 2$ ;i<n; $\dot { 1 } + = 2$ ) { Multiply to find FFT of their correlation. tmp $\mid =$ ans[i]; ans[i] $=$ (ans[i]\*temp[i]+ans[i+1]\*temp[i+1])/no2; ans[i+1] $=$ (ans[i+1]\*temp[i]-tmp\*temp[i+1])/no2;   
ans[0] $=$ ans[0]\*temp[0]/no2;   
ans[1] $=$ ans[1]\*temp[1]/no2;   
realft(ans,-1); Inverse transform gives correlation.

The discrete autocorrelation of a sampled function $g _ { j }$ is just the discrete correlation of the function with itself. Obviously this is always symmetric with respect to positive and negative lags. Feel free to use the above routine correl to obtain autocorrelations, simply calling it with the same data vector in both arguments. If the inefficiency bothers you, you can edit the program so that only one call is made to realft for the forward transform.

# CITED REFERENCES AND FURTHER READING:

Brigham, E.O. 1974, The Fast Fourier Transform (Englewood Cliffs, NJ: Prentice-Hall), $\ S 1 3 - 2$

# 13.3 Optimal (Wiener) Filtering with the FFT

There are a number of other tasks in numerical processing that are routinely handled with Fourier techniques. One of these is filtering for the removal of noise from a “corrupted” signal. The particular situation we consider is this: There is some underlying, uncorrupted signal $u ( t )$ that we want to measure. The measurement process is imperfect, however, and what comes out of our measurement device is a corrupted signal $c ( t )$ . The signal $c ( t )$ may be less than perfect in either or both of two respects. First, the apparatus may not have a perfect delta-function response, so that the true signal $u ( t )$ is convolved with (smeared out by) some known response function $r ( t )$ to give a smeared signal $s ( t )$ ,

$$
s ( t ) = \int _ { - \infty } ^ { \infty } r ( t - \tau ) u ( \tau ) \ d \tau \quad \mathrm { o r } \quad S ( f ) = R ( f ) U ( f )
$$

where $S , R , U$ are the Fourier transforms of $s , r , u$ ; respectively. Second, the measured signal $c ( t )$ may contain an additional component of noise $n ( t )$ ,

$$
c ( t ) = s ( t ) + n ( t )
$$

We already know how to deconvolve the effects of the response function $r$ in the absence of any noise (-13.1); we just divide $C ( f )$ by $R ( f )$ to get a deconvolved signal. We now want to treat the analogous problem when noise is present. Our task is to find the optimal filter, $\phi ( t )$ or $\Phi ( f )$ , which, when applied to the measured signal $c ( t )$ or $C ( f )$ and then deconvolved by $r ( t )$ or $R ( f )$ , produces a signal $\widetilde { u } ( t )$ or $\widetilde U ( f )$ that is as close as possible to the uncorrupted signal $u ( t )$ or $U ( f )$ . In other words, we will estimate the true signal $U$ by

$$
\tilde { U } ( f ) = \frac { C ( f ) \Phi ( f ) } { R ( f ) }
$$

In what sense is $\widetilde { U }$ to be close to $U$ ? We ask that they be close in the leastsquare sense

$$
\int _ { - \infty } ^ { \infty } \left| { \widetilde { u } } ( t ) - u ( t ) \right| ^ { 2 } \ d t = \int _ { - \infty } ^ { \infty } \left| { \widetilde { U } } ( f ) - U ( f ) \right| ^ { 2 } \ d f \quad { \mathrm { i s ~ m i n i m i z e d } } .
$$

Substituting equations (13.3.3) and (13.3.2), the right-hand side of (13.3.4) becomes

$$
\begin{array} { l } { { \displaystyle \int _ { - \infty } ^ { \infty } \left| \frac { [ S ( f ) + N ( f ) ] \Phi ( f ) } { R ( f ) } - \frac { S ( f ) } { R ( f ) } \right| ^ { 2 } ~ d f } } \\ { { \displaystyle = \int _ { - \infty } ^ { \infty } | R ( f ) | ^ { - 2 } \left\{ | S ( f ) | ^ { 2 } \left| 1 - \Phi ( f ) \right| ^ { 2 } + \left| N ( f ) \right| ^ { 2 } \left| \Phi ( f ) \right| ^ { 2 } \right\} ~ d f } } \end{array}
$$

The signal $S$ and the noise $N$ are uncorrelated, so their cross product, when integrated over frequency $f$ , gave zero. (This is practically the definition of what we mean by noise!) Obviously (13.3.5) will be a minimum if and only if the integrand is minimized with respect to $\Phi ( f )$ at every value of $f$ . Let us search for such a solution where $\Phi ( f )$ is a real function. Differentiating with respect to $\Phi$ and setting the result equal to zero gives

$$
\Phi ( f ) = { \frac { | S ( f ) | ^ { 2 } } { \left| S ( f ) \right| ^ { 2 } + \left| N ( f ) \right| ^ { 2 } } }
$$

This is the formula for the optimal filter $\Phi ( f )$ .

Notice that equation (13.3.6) involves $S$ , the smeared signal, and $N$ , the noise. The two of these add up to be $C$ , the measured signal. Equation (13.3.6) does not contain $U$ , the “true” signal. This makes for an important simplification: The optimal filter can be determined independently of the determination of the deconvolution function that relates $S$ and $U$ .

To determine the optimal filter from equation (13.3.6) we need some way of separately estimating $| \hat { S | ^ { 2 } }$ and $| N | ^ { 2 }$ . There is no way to do this from the measured signal $C$ alone without some other information, or some assumption or guess. Luckily, the extra information is often easy to obtain. For example, we can sample a long stretch of data $c ( t )$ and plot its power spectral density using equations (12.0.15), (12.1.8), and (12.1.5). This quantity is proportional to the sum $\bar { | S | } ^ { 2 } + | N | ^ { 2 }$ , so we have

![](images/51372657e013b925a932e32b663011365567bf0075eb3b9e7431fe2ff48d9e2d.jpg)  
Figure 13.3.1. Optimal (Wiener) filtering. The power spectrum of signal plus noise shows a signal peak added to a noise tail. The tail is extrapolated back into the signal region as a “noise model.” Subtracting gives the “signal model.” The models need not be accurate for the method to be useful. A simple algebraic combination of the models gives the optimal filter (see text).

$$
| S ( f ) | ^ { 2 } + | N ( f ) | ^ { 2 } \approx P _ { c } ( f ) = | C ( f ) | ^ { 2 } \qquad 0 \le f < f _ { c }
$$

(More sophisticated methods of estimating the power spectral density will be discussed in $\ S 1 3 . 4$ and $\ S 1 3 . 7$ , but the estimation above is almost always good enough for the optimal filter problem.) The resulting plot (see Figure 13.3.1) will often immediately show the spectral signature of a signal sticking up above a continuous noise spectrum. The noise spectrum may be flat, or tilted, or smoothly varying; it doesn’t matter, as long as we can guess a reasonable hypothesis as to what it is. Draw a smooth curve through the noise spectrum, extrapolating it into the region dominated by the signal as well. Now draw a smooth curve through the signal plus noise power. The difference between these two curves is your smooth “model” of the signal power. The quotient of your model of signal power to your model of signal plus noise power is the optimal filter $\Phi ( f )$ . [Extend it to negative values of $f$ by the formula $\Phi ( - f ) = \Phi ( f ) .$ ] Notice that $\Phi ( f )$ will be close to unity where the noise is negligible, and close to zero where the noise is dominant. That is how it does its job! The intermediate dependence given by equation (13.3.6) just turns out to be the optimal way of going in between these two extremes.

Because the optimal filter results from a minimization problem, the quality of the results obtained by optimal filtering differs from the true optimum by an amount that is second order in the precision to which the optimal filter is determined. In other words, even a fairly crudely determined optimal filter (sloppy, say, at the $10 \%$ level) can give excellent results when it is applied to data. That is why the separation of the measured signal $C$ into signal and noise components $S$ and $N$ can usefully be done “by eye” from a crude plot of power spectral density. All of this may give you thoughts about iterating the procedure we have just described. For example, after designing a filter with response $\Phi ( f )$ and using it to make a respectable guess at the signal $\widetilde { U } ( f ) = \Phi ( f ) C ( \bar { f } ) / R ( f )$ , you might turn about and regard $\tilde { U } ( \bar { f } )$ as a fresh new signal that you could improve even further with the same filtering technique. Don’t waste your time on this line of thought. The scheme converges to a signal of $S ( f ) = 0$ . Converging iterative methods do exist; this just isn’t one of them.

You can use the routine four1 (-12.2) or realft $( \ S 1 2 . 3 )$ to FFT your data when you are constructing an optimal filter. To apply the filter to your data, you can use the methods described in $\ S 1 3 . 1$ . The specific routine convlv is not needed for optimal filtering, since your filter is constructed in the frequency domain to begin with. If you are also deconvolving your data with a known response function, however, you can modify convlv to multiply by your optimal filter just before it takes the inverse Fourier transform.

# CITED REFERENCES AND FURTHER READING:

Rabiner, L.R., and Gold, B. 1975, Theory and Application of Digital Signal Processing (Englewood Cliffs, NJ: Prentice-Hall).   
Nussbaumer, H.J. 1982, Fast Fourier Transform and Convolution Algorithms (New York: Springer).   
Elliott, D.F., and Rao, K.R. 1982, Fast Transforms: Algorithms, Analyses, Applications (New York: Academic Press).

# 13.4 Power Spectrum Estimation Using the FFT

In the previous section we “informally” estimated the power spectral density of a function $c ( t )$ by taking the modulus-squared of the discrete Fourier transform of some finite, sampled stretch of it. In this section we’ll do roughly the same thing, but with considerably greater attention to details. This attention will uncover some surprises.

The first detail is the normalization of the power spectrum (or power spectral density or $P S D$ ). In general, there is some relation of proportionality between a measure of the squared amplitude of the function and a measure of the amplitude of the PSD. Unfortunately, there are several different conventions for describing the normalization in each domain, and many opportunities for getting wrong the relationship between the two domains. Suppose that our function $c ( t )$ is sampled at $N$ points to produce values $c _ { 0 } \ldots c _ { N - 1 }$ , and that these points span a range of time $T$ , that is, $T = ( N - 1 ) \Delta$ , where $\Delta$ is the sampling interval. Then here are several different descriptions of the total power:

$$
{ \begin{array} { r } { \displaystyle \sum _ { j = 0 } ^ { N - 1 } \left| c _ { j } \right| ^ { 2 } \equiv { \mathrm { s u m ~ s q u a r e d ~ a m p l i t u d e } } } \\ { \displaystyle { \frac { 1 } { T } } \int _ { 0 } ^ { T } \left| c ( t ) \right| ^ { 2 } \ d t \approx { \frac { 1 } { N } } \sum _ { j = 0 } ^ { N - 1 } \left| c _ { j } \right| ^ { 2 } \equiv { \mathrm { m e a n ~ s q u a r e d ~ a m p l i t u d e } } } \end{array} }
$$

$$
\int _ { 0 } ^ { T } \left| c ( t ) \right| ^ { 2 } d t \approx \Delta \sum _ { j = 0 } ^ { N - 1 } \left| c _ { j } \right| ^ { 2 } \equiv \mathrm { t i m e - i n t e g r a l s q u a r e d a m p l i t u d e }
$$

PSD estimators, as we shall see, have an even greater variety. In this section, we consider a class of them that give estimates at discrete values of frequency $f _ { i }$ , where $i$ will range over integer values. In the next section, we will learn about a different class of estimators that produce estimates that are continuous functions of frequency $f$ . Even if it is agreed always to relate the PSD normalization to a particular description of the function normalization (e.g., 13.4.2), there are at least the following possibilities: The PSD is

- defined for discrete positive, zero, and negative frequencies, and its sum over these is the function mean squared amplitude   
- defined for zero and discrete positive frequencies only, and its sum over these is the function mean squared amplitude   
- defined in the Nyquist interval from $- f _ { c }$ to $f _ { c }$ , where $f _ { c } = 1 / ( 2 \Delta )$ , and its integral over this range is the function mean squared amplitude   
- defined from 0 to $f _ { c }$ , and its integral over this range is the function mean squared amplitude (it never makes sense to integrate the PSD of a sampled function outside of the Nyquist interval $- f _ { c }$ and $f _ { c }$ since, according to the sampling theorem, power there will have been aliased into the Nyquist interval).

It is hopeless to define enough notation to distinguish all possible combinations of normalizations. In what follows, we use the notation $P ( f )$ to mean any of the above PSDs, stating in each instance how the particular $P ( f )$ is normalized. Beware the inconsistent notation in the literature.

The method of power spectrum estimation used in the previous section is a simple version of an estimator called, historically, the periodogram. If we take an $N$ -point sample of the function $c ( t )$ at equal intervals and use the FFT to compute its discrete Fourier transform

$$
C _ { k } = \sum _ { j = 0 } ^ { N - 1 } c _ { j } \ e ^ { 2 \pi i j k / N } \qquad k = 0 , \dots , N - 1
$$

then the periodogram estimate of the power spectrum is defined at $N / 2 + 1$ frequencies as

$$
\begin{array} { c } { { \displaystyle P ( 0 ) = P ( f _ { 0 } ) = \frac { 1 } { N ^ { 2 } } | C _ { 0 } | ^ { 2 } } } \\ { { { \displaystyle P ( f _ { k } ) = \frac { 1 } { N ^ { 2 } } \biggl [ | C _ { k } | ^ { 2 } + | C _ { N - k } | ^ { 2 } \biggr ] } } } \\ { { { \displaystyle P ( f _ { c } ) = P ( f _ { N / 2 } ) = \frac { 1 } { N ^ { 2 } } \left| C _ { N / 2 } \right| ^ { 2 } } } } \end{array} \quad \begin{array} { c } { { { } } } \\ { { k = 1 , 2 , . . . , \biggl ( \frac { N } { 2 } - 1 \biggr ) } } \\ { { { } } } \end{array}
$$

where $f _ { k }$ is defined only for the zero and positive frequencies

$$
f _ { k } \equiv \frac { k } { N \Delta } = 2 f _ { c } \frac { k } { N } \qquad k = 0 , 1 , \dots , \frac { N } { 2 }
$$

By Parseval’s theorem, equation (12.1.10), we see immediately that equation (13.4.5) is normalized so that the sum of the $N / 2 + 1$ values of $P$ is equal to the mean squared amplitude of the function $c _ { j }$ .

Here is an object (Spectreg for “spectrum register”) that implements equations $( 1 3 . 4 . 4 ) - ( 1 3 . 4 . 6 )$ . Its constructor takes an integer argument $M$ that defines both the number of data points, $2 M \equiv N$ , and $M + 1$ , the number of frequencies in the estimate between 0 and $f _ { c }$ , inclusive. $M$ must be a power of 2. Spectreg has some other features that we will build on below when we learn about window functions and variance reduction. For now, the function window that appears should be defined as returning the constant 1, that is,

Doub window(Int j,Int n) {return 1.;}

# struct Spectreg {

Object for accumulating power spectrum estimates from one or more segments of data.

Int m,m2,nsum;   
VecDoub specsum, wksp;   
Spectreg(Int em) : m(em), $\mathtt { m } 2 ( 2 \ast \mathtt { m } )$ , nsum(0), specsum $( \mathrm { m } { + } 1 , 0 . )$ , wksp(m2) {   
Constructor. Sets $M$ , such that data segments will have length $^ { 2 M }$ , and the spectrum will   
be estimated at $M + 1$ frequencies. if (m & $( \mathtt { m } \mathtt { - } 1 )$ ) throw("m must be power of 2");   
}

# template<class D>

void adddataseg(VecDoub_I &data, D &window) {   
Process a data segment of length $2 M$ using the window function, which can be either a bare function or a functor.   
Int i;   
Doub w,fac,sumw $\mathit { \Theta } = \mathit { \Theta } 0 .$ ;   
if (data.size() $! = \texttt { m } 2$ ) throw("wrong size data segment")   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<m2; $\dot { \bf 1 } + +$ ) { Load the data. $\kappa =$ window(i,m2); wksp[i] $=$ w\*data[i]; sumw $+ =$ SQR(w);   
}   
fac = 2./(sumw\*m2);   
realft(wksp,1); Take its Fourier transform.   
specsum[0] $\scriptstyle + = 0$ .5\*fac\*SQR(wksp[0]);   
for ( $\scriptstyle \dot { \mathtt { 1 } } = 1$ ;i<m; $\dot { \bar { 1 } } + + \dot { bar { 1 } }$ ) specsum[i] $+ =$ fac\*(SQR(wksp[2\*i])+SQR(wksp[2\*i+1]));   
specsum[m] += 0.5\*fac\*SQR(wksp[1]);   
nsum++;

# }

# VecDoub spectrum() {

Return power spectrum estimates as a vector. You can instead just access specsum directly, and divide by nsum.

VecDoub spec $\left( \mathtt { m } + 1 \right)$ ;   
if (nsum $\scriptstyle = = \ 0$ ) throw("no data yet");   
for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; $\mathrm { i } < = \mathtt { m }$ ; $\dot { \bf 1 } + +$ ) spec[i] $=$ specsum[i]/nsum;   
return spec;

# VecDoub frequencies() {

Return vector of frequencies (in units of $1 / \Delta$ ) at which estimates are made

VecDoub freq $\left( \mathrm { m } { + } 1 \right)$ ;   
for (Int $\scriptstyle { \dot { 1 } } = 0$ ; $\mathrm { i } < = \mathrm { m }$ ; $\dot { \bf 1 } + +$ ) freq[i] $=$ i\*0.5/m;   
return freq;

The naive use of Spectreg would be as follows: Declare an instance with a power-of-two value of $M$ . Call adddataseg to process a vector of data, length $2 M$ . Call spectrum and frequencies to get, respectively, the PSD estimates and the frequencies at which they are made (in units of $1 / \Delta$ ).

Before we rush to use Spectreg, however, we must now ask this question: In what sense is the periodogram estimate (13.4.5) a “true” estimator of the power spectrum of the underlying function $c ( t )$ ? You can find the answer treated in considerable detail in the literature cited (see, e.g., [1] for an introduction). Here is a summary.

First, is the expectation value of the periodogram estimate equal to the power spectrum, i.e., is the estimator correct (unbiased) on average? Well, yes and no. We wouldn’t really expect one of the $P ( f _ { k } )$ ’s to equal the continuous $P ( f )$ at exactly $f _ { k }$ , since $f _ { k }$ is supposed to be representative of a whole frequency “bin” extending from halfway from the preceding discrete frequency to halfway to the next one. We should be expecting the $P ( f _ { k } )$ to be some kind of average of $P ( f )$ over a narrow window function centered on its $f _ { k }$ . For the periodogram estimate (13.4.6), that window function, as a function of $s$ the frequency offset in bins, is

$$
W ( s ) = \frac { 1 } { N ^ { 2 } } \left[ \frac { \sin ( \pi s ) } { \sin ( \pi s / N ) } \right] ^ { 2 }
$$

Notice that $W ( s )$ has oscillatory lobes but, apart from these, falls off only about as $W ( s ) \approx ( \pi s ) ^ { - 2 }$ . This is not a very rapid fall-off, and it results in significant leakage (that is the technical term) from one frequency to another in the periodogram estimate. Notice also that $W ( s )$ happens to be zero for $s$ equal to a nonzero integer. This means that if the function $c ( t )$ is a pure sine wave of frequency exactly equal to one of the $f _ { k }$ ’s, then there will be no leakage to adjacent $f _ { k }$ ’s. But this is not the characteristic case! If the frequency is, say, one-third of the way between two adjacent $f _ { k }$ ’s, then the leakage will extend well beyond those two adjacent bins. The solution to the problem of leakage is called data windowing, and we will discuss it below.

Turn now to another question about the periodogram estimate. What is the variance of that estimate as $N$ goes to infinity? In other words, as we take more sampled points from the original function (either sampling a longer stretch of data at the same sampling rate, or else by resampling the same stretch of data with a faster sampling rate), then how much more accurate do the estimates $P _ { k }$ become? The unpleasant answer is that the periodogram estimates do not become more accurate at all! In fact, the variance of the periodogram estimate at a frequency $f _ { k }$ is always equal to the square of its expectation value at that frequency. In other words, the standard deviation is always $100 \%$ of the value, independent of $N$ !

How can this be? Where did all the information go as we added points? It all went into producing estimates at a greater number of discrete frequencies $f _ { k }$ . If we sample a longer run of data using the same sampling rate, then the Nyquist critical frequency $f _ { c }$ is unchanged, but we now have finer frequency resolution (more $f _ { k }$ ’s) within the Nyquist frequency interval; alternatively, if we sample the same length of data with a finer sampling interval, then our frequency resolution is unchanged, but the Nyquist range now extends up to a higher frequency. In neither case do the additional samples reduce the variance of any one particular frequency’s estimated PSD.

You don’t have to live with PSD estimates with $100 \%$ standard deviations, however. You simply have to know some techniques for reducing the variance of the estimates. Here are two techniques that are very nearly identical mathematically, though different in implementation. The first is to compute a periodogram estimate with finer discrete frequency spacing than you really need, and then to sum the periodogram estimates at $K$ consecutive discrete frequencies to get one “smoother” estimate at the mid-frequency of those $K$ . The variance of that summed estimate will be smaller than the estimate itself by a factor of exactly $1 / K$ , i.e., the standard deviation will be smaller than $100 \%$ by a factor $1 / { \sqrt { K } }$ . Thus, to estimate the power spectrum at $M + 1$ discrete frequencies between 0 and $f _ { c }$ inclusive, you begin by taking the FFT of $2 M K$ points (which number had better be an integer power of 2!). You then take the modulus square of the resulting coefficients, add positive and negative frequency pairs, and divide by $( 2 M K ) ^ { 2 }$ , all according to equation (13.4.5) with $N = 2 M K$ . Finally, you “bin” the results into summed (not averaged) groups of $K$ . This procedure is very easy to program, so we will not bother to give a routine for it. The reason that you sum, rather than average, $K$ consecutive points is so that your final PSD estimate will preserve the normalization property that the sum of its $M + 1$ values equals the mean square value of the function.

A second technique for estimating the PSD at $M + 1$ discrete frequencies in the range 0 to $f _ { c }$ is to partition the original sampled data into $K$ segments each of $2 M$ consecutive sampled points. Each segment is separately FFT’d to produce a periodogram estimate (equation 13.4.5 with $N \equiv 2 M$ ). Finally, the $K$ periodogram estimates are averaged at each frequency. It is this final averaging that reduces the variance of the estimate by a factor $K$ (standard deviation by $\sqrt { K }$ ). This second technique is computationally more efficient than the first technique above by a modest factor, since it is logarithmically more efficient to take many shorter FFTs than one longer one. The principal advantage of the second technique, however, is that only $2 M$ data points are manipulated at a single time, not $2 K M$ as in the first technique. This means that the second technique is the natural choice for processing long runs of data, as from a real-time device or slow storage.

In fact, you may already have noticed, the object Spectreg implements this second technique. If you call adddataseg $K$ times, with a different vector of $2 M$ data points each time, then the result returned by spectrum is the average of the $K$ periodograms. However, we should still not rush to use Spectreg. We need first to return to the matters of leakage and data windowing that were brought up after equation (13.4.7) above.

# 13.4.1 Data Windowing

The purpose of data windowing is to modify equation (13.4.7), which expresses the relation between the spectral estimate $P _ { k }$ at a discrete frequency and the actual underlying continuous spectrum $P ( f )$ at nearby frequencies. In general, the spectral power in one “bin” $k$ contains leakage from frequency components that are actually $s$ bins away, where $s$ is the independent variable in equation (13.4.7). There is, as we pointed out, quite substantial leakage even from moderately large values of $s$ . Note that $s$ is not an integer, in general, because actual frequencies can have any real value.

When we select a run of $N$ sampled points for periodogram spectral estimation, we are in effect multiplying an infinite run of sampled data $c _ { j }$ by a window function in time, one that is zero except during the total sampling time $N \Delta$ and is unity during that time. In other words, the data are windowed by a square window function. By the convolution theorem (12.0.10; but interchanging the roles of $f$ and $t$ ), the Fourier transform of the product of the data with this square window function is equal to the convolution of the data’s Fourier transform with the window’s Fourier transform. In fact, equation (13.4.7) is nothing more than the square of the discrete Fourier transform of the unity window function.

$$
W ( s ) = \frac { 1 } { N ^ { 2 } } \left[ \frac { \sin ( \pi s ) } { \sin ( \pi s / N ) } \right] ^ { 2 } = \frac { 1 } { N ^ { 2 } } \left| \sum _ { k = 0 } ^ { N - 1 } e ^ { 2 \pi i s k / N } \right| ^ { 2 }
$$

The reason for the leakage at large values of $s$ is that the square window function turns on and off so rapidly. Its Fourier transform has substantial components at high frequencies. To remedy this situation, we can multiply the input data $c _ { j } , j =$ $0 , \ldots , N - 1$ by a window function $w _ { j }$ that changes more gradually from zero to a maximum and then back to zero as $j$ ranges from 0 to $N$ . In this case, the equations for the periodogram estimator (13.4.4 – 13.4.5) become

$$
\begin{array} { c c } { { D _ { k } \equiv \displaystyle \sum _ { j = 0 } ^ { N - 1 } c _ { j } w _ { j } \ e ^ { 2 \pi i j k / N } } } & { { k = 0 , \ldots , N - 1 } } \\ { { \ } } & { { \ } } \\ { { P ( 0 ) = P ( f _ { 0 } ) = \displaystyle \frac { 1 } { W _ { s s } } \left| D _ { 0 } \right| ^ { 2 } \ ~ } } \\ { { \ } } & { { \ } } \\ { { P ( f _ { k } ) = \displaystyle \frac { 1 } { W _ { s s } } \left[ \left| D _ { k } \right| ^ { 2 } + \left| D _ { N - k } \right| ^ { 2 } \right] ~ } } & { { k = 1 , 2 , \ldots , \left( \displaystyle \frac { N } { 2 } - 1 \right) ~ , } } \\ { { \ } } & { { \ } } \\ { { P ( f _ { c } ) = P ( f _ { N / 2 } ) = \displaystyle \frac { 1 } { W _ { s s } } \left| D _ { N / 2 } \right| ^ { 2 } } } & { { } } \end{array}
$$

where $W _ { s s }$ stands for “window squared and summed,”

$$
W _ { s s } \equiv N \sum _ { j = 0 } ^ { N - 1 } w _ { j } ^ { 2 }
$$

and $f _ { k }$ is given by (13.4.6). The more general form of (13.4.7) can now be written in terms of the window function $w _ { j }$ as

$$
W ( s ) = \frac { 1 } { W _ { s s } } \left| \sum _ { k = 0 } ^ { N - 1 } e ^ { 2 \pi i s k / N } w _ { k } \right| ^ { 2 }
$$

There is a lot of perhaps unnecessary lore about the choice of a window function, and practically every function that rises from zero to a peak and then falls again has been named after someone. A few of the more common (also shown in Figure 13.4.1) are

$$
w _ { j } = 1 - \left| { \frac { j - { \frac { 1 } { 2 } } N } { { \frac { 1 } { 2 } } N } } \right| \equiv \mathrm { B a r t l e t t w i n d o w }
$$

(the “Parzen window” is a smoother, but similarly shaped, functional form)

$$
w _ { j } = { \frac { 1 } { 2 } } \left[ 1 - \cos \left( { \frac { 2 \pi j } { N } } \right) \right] \equiv \mathrm { H a n n ~ w i n d o w }
$$

![](images/c706225a2eaf342c34a59b6322b4ba3fd5de7bc2fcf37c99f206cbac7f977a92.jpg)  
Figure 13.4.1. Window functions commonly used in FFT power spectral estimation. The data segment, here of length 256, is multiplied (bin by bin) by the window function before the FFT is computed. The square window, which is equivalent to no windowing, is least recommended. The Welch and Bartlett windows are good choices.

(the “Hamming window” is similar but does not go exactly to zero at the ends)

$$
w _ { j } = 1 - \left( { \frac { j - { \frac { 1 } { 2 } } N } { { \frac { 1 } { 2 } } N } } \right) ^ { 2 } \equiv \mathrm { W e l c h ~ w i n d o w }
$$

We are inclined to follow Welch in recommending that you use either (13.4.13) or (13.4.15) in practical work. However, at the level of the discussion thus far, there is little difference between any of these (or similar) window functions. Their difference lies in subtle trade-offs among the various figures of merit that can be used to describe the narrowness or peakedness of the spectral leakage functions computed by (13.4.12). These figures of merit have such names as: highest sidelobe level (dB), sidelobe fall-off (dB per octave), equivalent noise bandwidth (bins), 3-dB bandwidth (bins), scallop loss (dB), and worst-case process loss (dB). Roughly speaking, the principal trade-off is between making the central peak as narrow as possible versus making the tails of the distribution fall off as rapidly as possible. For details, see, e.g., [2]. Figure 13.4.2 plots the leakage amplitudes for several windows already discussed.

There is a particular lore about window functions that rise smoothly from zero to unity in the first small fraction (say $10 \%$ ) of the data, then stay at unity until the last small fraction (again say $10 \%$ ) of the data, during which the window function falls smoothly back to zero. These windows will squeeze a little bit of extra narrowness out of the main lobe of the leakage function (never as much as a factor of two, however), but trade this off by widening the leakage tail by a significant factor (e.g., the reciprocal of $10 \%$ , a factor of ten). If we distinguish between the width of a window (number of samples for which it is at its maximum value) and its rise/fall time (number of samples during which it rises and falls); and if we distinguish between the FWHM (full width to half maximum value) of the leakage function’s main lobe and the leakage width (full width that contains half of the spectral power that is not contained in the main lobe), then these quantities are related roughly by

![](images/6b35f5d1159f7f7188591d24c89e6cf1a1ebb99f7b01e76de775f0539ee71b49.jpg)  
Figure 13.4.2. Leakage functions for the window functions of Figure 13.4.1. A signal whose frequency is actually located at zero offset “leaks” into neighboring bins with the amplitude shown. The purpose of windowing is to reduce the leakage at large offsets, where square (no) windowing has large sidelobes. Offset can have a fractional value, since the actual signal frequency can be located between two frequency bins of the FFT.

$$
\begin{array} { c } { { \displaystyle ( \mathrm { F W H M ~ i n ~ b i n s } ) \approx \frac { N } { ( \mathrm { w i n d o w ~ w i d t h } ) } } } \\ { { \displaystyle ( \mathrm { l e a k a g e ~ w i d t h ~ i n ~ b i n s } ) \approx \frac { N } { ( \mathrm { w i n d o w ~ r i s e / f a l l ~ t i m e } ) } } } \end{array}
$$

For the windows given above in $( 1 3 . 4 . 1 3 ) - ( 1 3 . 4 . 1 5 )$ , the effective window widths and the effective window rise/fall times are both of order ${ \scriptstyle { \frac { 1 } { 2 } } } N$ . Generally speaking, we feel that the advantages of windows whose rise and fall times are only small fractions of the data length are minor or nonexistent, and we avoid using them. One sometimes hears it said that flat-topped windows “throw away less of the data,” but we will show you two better ways of dealing with that problem, namely by overlapping data segments or by multitaper methods.

Now, at last, we really are ready to use the Spectreg object. First, choose a window function. The templating in Spectreg allows it to accept either a bare function or a functor. Use the former if your window function is fast to compute, or the latter if you want to precompute and store a more complicated window function, or one with auxiliary parameters. Examples are

Doub square(Int j,Int n) {return 1.;} Don’t use this! Doub bartlett(Int j,Int n) {return 1.-abs(2.\*j/(n-1.)-1.);} Use this, Doub welch(Int j,Int n) {return 1.-SQR(2.\*j/(n-1.)-1.);} or this...

struct Hann {   
...or this. This is an example of a functor. Int nn; VecDoub win; Hann(Int n) : nn(n), win(n) { Constructor. Compute and store the window function in a table. Doub twopi $=$ 8.\*atan(1.); for (Int $\scriptstyle { \dot { 1 } } = 0$ ;i<nn; $\dot { \bf 1 } + +$ ) win[i] $=$ 0.5\*(1.-cos(i\*twopi/(nn-1.))); } Doub operator() (Int j, Int n) { Make it a functor, able to return values as if it were a function. if $( \mathrm { { n } \ ! = \ n n } )$ ) throw("incorrect n for this Hann"); return win[j]; }   
};

Second, pick a value of $M$ and declare a Spectreg object. Third, process $K$ data segments, each of length $2 M$ . The larger $K$ , the more accurate your answer. Fourth, get the PSD estimate at $M + 1$ frequencies by a call to the spectrum method (or, to avoid copying vectors, directly from the specsum member vector).

# 13.4.2 Overlapping Data Segments

We introduced window functions to mitigate leakage, a major problem, but in doing so we have created a new problem, luckily minor, which we now address. All good window functions, because they approach zero at their endpoints, deweight, and in effect throw away, valid data. A consequence is that, for any number of data segments $K$ each of length $2 M$ , the variance of the PSD estimate is somewhat larger with a good window function than with the (bad) square window.

Sometimes you are not limited in the number of data points, but rather by the computer resources to process them. For example, the data may be pouring out of a real-time device at a high rate. In such a situation, data deweighting is not an issue. You should use Spectreg as already described, accumulating as many data segments as you need to obtain the desired accuracy. Indeed, this gives you the smallest variance estimate per computer operation.

More often, however, you are limited in the total number of data points, and you want to get the smallest variance estimate from them, but without giving up the low-leakage benefit of windowing. In this situation it turns out to be optimal, or nearly optimal, to overlap the segments by one-half of their length. The first and second sets of $M$ points become segment number 1 (length $2 M$ as usual); the second and third sets of $M$ points become segment number 2; and so on, up to segment number $K$ , which is made of the $K$ th and $K +$ 1st sets of $M$ points. The total number of sampled points is therefore $( K + 1 ) M$ , just over half as many as with nonoverlapping segments. The reduction in the variance is not a full factor of $K$ , since the segments are not statistically independent. It can be shown that the variance is instead reduced by a factor of about $9 K / 1 1$ [3]. This is, however, significantly better than the reduction of about $K / 2$ that would have resulted if the same number of data points were segmented without overlapping.

Here is an object Spectolap, derived from Spectreg as a base class, that implements the overlap method. As far as the user is concerned, the only difference is that the adddataseg method now requires a data segment of length $M$ , not $2 M$ .

# struct Spectolap : Spectreg {

Object for power spectral estimation using overlapping data segments. The user sends nonoverlapping segments of length $M$ , which are processed in pairs of length $2 M$ , with overlap.

Int first;   
VecDoub fullseg;

Spectolap(Int em) : Spectreg(em), first(1), fullseg( $^ { 2 * }$ em) {} Constructor. Sets M .

# template<class D>

void adddataseg(VecDoub_I &data, D &window) {

Process a data segment of length $M$ using the window function, which can be either a bare function or a functor.

Int i; if (data.size() $! = \ \mathtt { m } .$ ) throw("wrong size data segment"); if (first) { First segment is just stored. for ( $\mathtt { i } = 0$ ;i<m; $\mathrm { i } + +$ ) fullseg[i+m] $=$ data [i]; first $\mathbf { \lambda } = \mathbf { \lambda } _ { 0 } ;$ } else Subsequent segments are processed. for ( $\scriptstyle \dot { 1 } = 0$ ;i<m;i $^ { + + }$ ) { fullseg[i] $=$ fullseg[i+m]; fullseg[i+m] $=$ data [i]; } Spectreg::adddataseg(fullseg,window); Base class method, the data lengt } is $2 M$ . }

template<class D> void addlongdata(VecDoub_I &data, D &window) { Process a long vector of data as overlapping segments each of length $^ { 2 M }$ . Int i, k, noff, nt=data.size(), nk=(nt-1)/m; Doub del $\mathbf { \Sigma } = \mathrm { ~ n k ~ } > \mathrm { ~ 1 ~ } ?$ (nt-m2)/(nk-1.) : 0.; Target separation. if (nt $<$ m2) throw("data length too short"); for $\scriptstyle \mathbf { k } = 0$ ;k<nk;k++) { Process nk overlapping segments. noff $=$ (Int)(k\*del $+ 0$ .5); Offset is nearest integer. for ( $\scriptstyle \dot { 1 } = 0$ ;i<m2; $\dot { \bf 1 } + +$ ) fullseg[i] $=$ data[noff+i]; Spectreg::adddataseg(fullseg,window); } } };

The method addlongdata in Spectolap is provided to deal with another common situation: You want to estimate the PSD at $M + 1$ frequencies (as usual), but your data are in a long vector that is not necessarily a multiple of $M$ , or $2 M$ , or a power of 2. Here we are assuming that the length of your data vector, $N _ { \mathrm { t o t } }$ , is much larger than $2 M$ . The problem is not that the number of segments $K$ is small, but rather that $K$ is not an integer. Overlapping data segments provide a nifty fix: We start with the next-larger integer number of segments, and then squeeze them together just a bit, like an accordion, until they exactly fit into $N _ { \mathrm { t o t } }$ . In other words, we overlap them by slightly more than half of their length, to get an exact fit.

Here is our plain-vanilla recommendation for PSD estimation when your $N _ { \mathrm { t o t } }$ data points are not taxing the size of memory: Pick $M$ , a power of 2, such that estimates at $M + 1$ frequencies between 0 and $f _ { c }$ (inclusive) are enough. Don’t be too greedy on $M$ , because the fractional standard deviation of your estimates will on the order of $( M / N _ { \mathrm { t o t } } ) ^ { 1 / 2 }$ . Then do

Int ntot=..., m=...;   
VecDoub data(ntot), psd(m), freq(m); Spectolap myspec(m);   
myspec.addlongdata(data,bartlett); psd $=$ myspec.spectrum()   
freq $=$ myspec.frequencies()

# 13.4.3 Multitaper Methods and Slepian Functions

Multitaper methods provide a principled approach to the trade-off between (very) low leakage and minimizing the variance of the PSD estimate. If the leakage profiles in Figure 13.4.2 are acceptable to you (and see also Figure 13.4.4 below), then you don’t need to read this section. In some applications, however, minimizing leakage is the whole game. For example, you may be looking for very weak spectral signals, either line or continuum, that can be masked by leakage from nearby strong lines. Or, you may be interested in the tail of a spectrum at high frequencies, which can be spuriously dominated by leakage from lower frequencies.

You have to give something to get something. Here, you have to accept a (small) broadening of the main lobe of the leakage function $W ( s )$ in order to (greatly) suppress leakage outside of the main lobe. Broadening the main lobe is equivalent to giving up some frequency resolution. We can parameterize this by a value $j _ { \mathrm { r e s } }$ . The goal is to minimize leakage for $| s | > j _ { \mathrm { r e s } }$ , measured in bins, in exchange for which we are willing to have leakage near unity for any $| s | < j _ { \mathrm { r e s } }$ . Typical values of $j _ { \mathrm { r e s } }$ might be in the range of 2 to 10. (We’ll see that larger values are not necessary.)

There are two key ideas in multitaper methods, somewhat independent of each other, originating in the work of Slepian [4]. The first idea is that, for a given data length $N$ and choice $j _ { \mathrm { r e s } }$ , one can actually solve for the best possible weights $w _ { j }$ , meaning the ones that make the leakage smallest among all possible choices. The beautiful and nonobvious answer (see [5]) is that the vector of optimal weights is the eigenvector corresponding to the smallest eigenvalue of the symmetric tridiagonal matrix with diagonal elements

$$
\frac { 1 } { 4 } \left[ N ^ { 2 } - ( N - 1 - 2 j ) ^ { 2 } \cos \left( \frac { 2 \pi j _ { \mathrm { r e s } } } { N } \right) \right] , \qquad j = 0 , \dots , N - 1
$$

and off-diagonal elements

$$
- { \textstyle { \frac { 1 } { 2 } } } j ( N - j ) , \qquad j = 1 , \dots , N - 1
$$

The second key idea is that the next few eigenvectors of this same matrix are also pretty good window functions. And because they are orthogonal to the first eigenvector (and each other), they give statistically independent estimates, which can be averaged together to decrease the variance of the final answer. Let $k _ { T }$ (for “taper”) denote the number of such estimates that are averaged. Figure 13.4.3 shows the first five window functions (eigenvectors number $k = 0 , \ldots , k _ { T } - 1 )$ for the case $j _ { \mathrm { r e s } } = 3$ , $N = 1 0 2 4$ . The functions (actually discrete sequences) obtained as eigenvectors of equations (13.4.18) and (13.4.19) are called Slepian functions or discrete prolate spheroidal sequences (dpss). You can see that larger values of $k$ pick up the information in data regions that were deweighted in the first eigenvector $k = 0$ . (You may have thought that window functions needed to be positive, but there is actually no such restriction in any of the discussion above.)

![](images/da02202b39a84331019653e8435683b731486f8298cbb5808cf9dfc1f6fa9e97.jpg)  
Figure 13.4.3. Slepian taper (window) functions for the case $j _ { \mathrm { r e s } } = 3$ , $k = 0 , 1 , 2 , 3 , 4$ , $N = 1 0 2 4$ Combining the power spectrum estimates of different $k$ ’s uses, effectively, more of the data segment and decreases the variance.

The reason that you can’t continue this indefinitely, using eigenvectors corresponding to larger and larger eigenvalues (increasing $k _ { T }$ ), is that the leakage of the $k \mathrm { t h }$ window function increases rather rapidly with $k$ . Only $k _ { T } < 2 j _ { \mathrm { r e s } }$ values are worth considering at all, and only for $k _ { T } \lesssim j _ { \mathrm { r e s } }$ is the leakage really tiny, which was, after all, the whole point. In Figure 13.4.3 you can already guess that $k = 3$ and 4 are going to have rather poor leakage properties, because they noticeably don’t go to zero at their endpoints. Figure 13.4.4 shows the leakage function $W ( s )$ for a variety of window functions, including those we met previously, now plotted on a logarithmic scale. Window functions shown as shaded have leakage so large as to be ruled out almost categorically; the square window is notable in this group. You can see how the main lobe of the Slepian functions extends almost exactly out to $j _ { \mathrm { r e s } }$ , and that the suppression of the sidelobes of the lowest eigenvectors (e.g., Slepian 3,0 and 3,1) is really quite remarkable.

Here is an object, again derived from Spectreg as a base class, for estimating the PSD using the multitaper method with Slepian window functions. As in the base class, the method adddataseg accepts data segments of length $2 M$ , but it now adds to the average the result of the first $k _ { T }$ tapers of resolution $j _ { \mathrm { r e s } }$ . Values for $M$ , $j _ { \mathrm { r e s } }$ and $k _ { T }$ are set in the constructor.

struct Slepian : Spectreg {   
Object for power spectral estimation using the multitaper method with Slepian tapers. Int jres, kt; MatDoub dpss; Table of Slepians. Doub p,pp,d,dd; Slepian(Int em, Int jjres, Int kkt) : Spectreg(em), jres(jjres), kt(kkt), dpss(kkt,2\*em) { Constructor sets $M$ (same meaning as previously), $j _ { \mathrm { r e s } }$ , and $k _ { T }$ , see text. if (jres $< ~ 1$ || kt $> =$ 2\*jres) throw("kt too big or jres too small"); filltable(); } void filltable(); Implementation in next subsection. void renorm(Int n) { Utility used by filltable. $_ { \mathrm { ~ p ~ } } =$ ldexp(p,n); pp = ldexp(pp,n); d = ldexp(d,n); dd $=$ ldexp(dd,n); } struct Slepwindow { Captive functor will be sent to the base class as a window function. Int k;

![](images/f53e1562d4ed90c2d5ba81cc0b6011a507fe5873949d8bddbc66f7542fa8dbdc.jpg)  
Figure 13.4.4. Leakage function $W ( s )$ for various window functions. The top row is essentially the same as Figure 13.4.2, but squared (to get power) and plotted logarithmically. The second and third rows are examples of Slepian functions, identified by $j _ { \mathrm { r e s } } , \bar { k }$ values. Small $k$ values have exceedingly small leakage for $| s | > j _ { \mathrm { r e s } } ^ { \ }$ ; but as $k$ increases, so does the leakage. Shaded functions have unacceptably large leakage and are not recommended.

MatDoub &dps; Slepwindow(Int kkt, MatDoub &dpss) : k(kkt), dps(dpss) {} Doub operator() (Int j, Int n) {return dps[k][j];} };

void adddataseg(VecDoub_I &data) Process a data segment of length $^ { 2 M }$ using $k _ { T }$ tapers. Int k; if (data.size() $\downarrow =$ m2) throw("wrong size data segment"); for $\scriptstyle ( \mathtt { k } = 0$ ;k<kt;k $^ { + + }$ ) { Loop over tapers, initializing the functor Slepwindow window(k,dpss); separately for each. Spectreg::adddataseg(data,window); } } };

We discuss the body of filltable, where the Slepian functions are actually computed, below.

![](images/35e6023d0efc911a77a0c42a4379610ba6865aec62e82e848f3fd4fb090c9c51.jpg)  
Figure 13.4.5. Slepian taper (window) functions for $k \ = \ 0$ (smallest eigenvalue) and $\begin{array} { r l } { j _ { \mathrm { r e s } } } & { { } = } \end{array}$ $2 , 3 , \ldots , 1 0$ , with $\begin{array} { r } { \bar { N } \ = \ \bar { 1 } 0 2 4 } \end{array}$ . Any of these, used by itself, is a good choice for the overlapping data segment method; see text.

First, a few words about the use and misuse of multitaper methods.

The Slepian multitaper method is fundamentally about low leakage. The fact that it can reduce the variance a bit by taking $k _ { T } > 1$ is only a secondary consideration, because there are better ways to achieve the latter goal, for example by overlapping data segments. It follows that you should never need to take $j _ { \mathrm { r e s } }$ or $k _ { T }$ very large, greater than 10, say. Your logical path for choosing parameters should be something like this: Leakage suppression of the Slepian functions is so amazingly good that you can get to any plausible desired level for the first few eigenvectors with modest $j _ { \mathrm { r e s } }$ . Find that value, and the largest acceptable value for $k _ { T }$ . The frequency resolution is now $j _ { \mathrm { r e s } }$ , measured in bins. You now pick $M$ to get the physical frequency resolution that you actually need,

$$
f _ { \mathrm { r e s } } = \frac { j _ { \mathrm { r e s } } } { 2 M \Delta }
$$

(compare equation 13.4.6). Don’t be too greedy, or you will produce an unacceptably large variance. Now, if you have $N _ { \mathrm { t o t } }$ data points, you process $N _ { \mathrm { t o t } } / ( 2 M )$ separate data segments using adddataseg.

It would be misguided to increase $j _ { \mathrm { r e s } }$ to a large value just to increase $k _ { T }$ for the purpose of variance reduction. The reason is that, for a fixed desired physical frequency resolution, you will need to increase $M$ in proportion, and thus decrease your number of separate data segments, also in proportion. You thus gain nothing in variance reduction, and (potentially) lose greatly in leakage.

If squeezing down the variance by the last little bit is important, then you might consider using only the first Slepian function for a given $j _ { \mathrm { r e s } }$ , and then using overlapping data segments. You can code this using Spectolap and Slepian as models. As $j _ { \mathrm { r e s } }$ increases, the optimal spacing of overlapped segments decreases, as you can intuit from the narrowing central peaks in Figure 13.4.5. A spacing of $0 . 7 N / \sqrt { j _ { \mathrm { r e s } } + 0 . 3 }$ , that is, overlap of $N - 0 . 7 \bar { N } / \sqrt { j _ { \mathrm { r e s } } + 0 . 3 }$ , should be about right.

# 13.4.4 Computation of the Slepian Functions

We want to find the first few eigenvectors and eigenvalues of the tridiagonal matrix, equations (13.4.18) and (13.4.19). For $N \gg 1$ (always our situation), the eigenvalues are well separated and approximately a function of $j _ { \mathrm { r e s } }$ only. A good starting approximation for the

smallest eigenvalue $\lambda _ { 0 }$ is

$$
\lambda _ { 0 } \approx 1 . 5 6 9 2 j _ { \mathrm { r e s } } - 0 . 1 0 8 5 9 - 0 . 0 6 8 7 6 2 / j _ { \mathrm { r e s } } , \qquad j _ { \mathrm { r e s } } \geq 1
$$

and a similar approximation for the spacing of the first two eigenvalues is

$$
\lambda _ { 1 } - \lambda _ { 0 } \approx 3 . 1 3 8 7 j _ { \mathrm { r e s } } - 0 . 4 7 2 7 6 - 0 . 2 0 2 7 3 / j _ { \mathrm { r e s } } , \qquad j _ { \mathrm { r e s } } \ge 1
$$

With these hints, a workable strategy is to find the eigenvalues as roots of the characteristic polynomial, using Newton’s method. As starting guesses, we use equations (13.4.21) and (13.4.22), and subsequently linear interpolation on $\lambda _ { k - 1 }$ and $\lambda _ { k }$ , to estimate $\lambda _ { k + 1 }$ . There exists a straightforward recurrence relation that evaluates the characteristic polynomial of a tridiagonal system and its first derivative simultaneously (see [6]), and more than three or four iterations are seldom required. Once the eigenvalue is in hand, the eigenvector is obtained by setting one component arbitrarily, solving the tridiagonal system for the other components, and then renormalizing the solution. The code uses an algebraically equivalent form for equation (13.4.18) that is less susceptible to roundoff error.

# void Slepian::filltable() {

Calculate Slepian functions and store in table. const Doub EPS $\ = \ 1$ .e-10, $\mathtt { P I } \ = \ 4$ .\*atan(1.); Doub xx,xnew,xold,sw,ppp,ddd,sum,bet,ssub,ssup,\*u; Int i,j,k,nl; VecDoub dg(m2),dgg(m2),gam(m2),sup(m2-1),sub(m2-1); sw $= ~ 2$ .\*SQR(sin(jres\*PI/m2)); dg[0] $=$ 0.25\*(2\*m2+sw\*SQR(m2-1.)-1.); Set up the tridiagonal matrix. for ( $\dot { \bar { 1 } } = 1$ ;i<m2;i++) { dg[i] $=$ 0.25\*(sw\*SQR(m2-1.-2\*i)+(2\*(m2-i)-1.)\*(2\*i+1.)); sub[i-1] $=$ sup[i-1] $=$ -i\*(Doub)(m2-i)/2.; } xx $\qquad = \quad - 0$ .10859 - 0.068762/jres $^ +$ 1.5692\*jres; Eigenvalue first guess xold $=$ xx + 0.47276 $^ +$ 0.20273/jres - 3.1387\*jres; for $\scriptstyle \mathtt { k } = 0$ ; k<kt; $\mathtt { k } { + } { + }$ ) { Loop over number of desired eigenvalues. $u \ =$ &dpss[k][0]; Point output vector into table. for (i=0;i<20;i++) { Loop over iterations of Newton’s method. $\tt p p = 1 . ;$ $\mathtt { p } = \mathtt { d g } [ 0 ]$ - xx; dd $\qquad = \ 0 .$ ; $\texttt { d } = \texttt { - } 1$ .; for $( \mathrm { j } = 1$ ; j<m2; ${ \mathrm { j } } + + { \mathrm { . } }$ ) { Recurrence evaluates polynomial and derivappp $=$ pp; $\mathrm { { p p } = \mathrm { { p } } }$ ; tive. ddd $=$ dd; dd $\qquad = \ \mathrm { ~ d ~ }$ ; $\mathrm {  ~ p ~ } = \mathrm {  ~ p p * }$ (dg[j]-xx) - ppp\*SQR(sup[j-1]); $\mathsf { d } \ = \ - \mathsf { p } \mathsf { p } \ +$ dd\*(dg[j]-xx) - ddd\*SQR(sup[j-1]); if (abs(p)>1.e30) renorm(-100); else if (abs(p)<1.e-30) renorm(100); } xnew $=$ xx - p/d; Newton’s method. if (abs(xx-xnew) $<$ EPS\*abs(xnew)) break; xx $=$ xnew; } xx $=$ xnew - (xold - xnew); xold $=$ xnew; for ( $\scriptstyle \dot { 1 } = 0$ ;i<m2;i++) dgg[i] $=$ dg[i] - xnew; Subtract eigenvalue from matrix ${ \bf n } 1 ~ = ~ { \bf m } 2 / 3$ ; diagonal. Then, set one com dgg[nl] $\mathit { \Theta } = \mathit { \Theta } 1 , ;$ ponent (saving current valssup $=$ sup[nl]; ssub $=$ sub[nl-1]; ues). u[0] $=$ sup[nl] $=$ sub[nl-1] $\mathit { \Theta } = \mathit { \Theta } 0$ .; bet $=$ dgg[0]; Begin tridiagonal solution. for ( $\scriptstyle \dot { \mathtt { 1 } } = 1$ ; i<m2; $\dot { 1 } + +$ ) { gam[i] $=$ sup[i-1]/bet; bet $=$ dgg[i] - sub[i-1]\*gam[i]; u[i] $=$ (( $\scriptstyle \dot { 1 } = =$ nl? 1. : 0.) - sub[i-1]\*u[i-1])/bet;

} for ( $\scriptstyle { \dot { 1 } } = \mathtt { m } 2 - 2$ ; $\scriptstyle \dot { 1 } > = 0$ ; i--) u[i] $- =$ gam[i+1]\*u[i+1];   
sup[nl] $=$ ssup; sub[nl-1] $=$ ssub; Restore saved values.   
sum $\mathit { \Theta } = \mathit { \Theta } 0 .$ ; Renormalize and fix sign convention.   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; i<m2; $\dot { 1 } + +$ ) sum $+ =$ SQR(u[i]);   
sum $=$ (u[3] $>$ 0.)? sqrt(sum) : -sqrt(sum);   
for ( $\scriptstyle { \dot { 1 } } = 0$ ; i<m2; $\dot { 1 } + +$ ) u[i] /= sum;

# CITED REFERENCES AND FURTHER READING:

Oppenheim, A.V., Schafer, R.W., and Buck, J.R. 1999, Discrete-Time Signal Processing, 2nd ed. (Englewood Cliffs, NJ: Prentice-Hall).[1]   
Harris, F.J. 1978, “On the Use of Windows for Harmonic Analysis with the Discrete Fourier Transform,” Proceedings of the IEEE, vol. 66, pp. 51–83.[2]   
Welch, P.D. 1967, ”The Use of Fast Fourier Transform for the Estimation of Power Spectra: A Method Based on Time Averaging Over Short, Modified Periodograms,” IEEE Transactions on Audio and Electroacoustics,vol. AU-15,pp.70-73.[3]   
Slepian, D. 1976, “Prolate Spheroidal Wave Functions, Fourier Analysis, and Uncertainty — V: The Discrete Case,” Bell System Technical Journal, vol. 57, pp. 1371-1430.[4]   
Percival, D.B., and Walden, A.T. 1993, Spectral Analysis for Physical Applications: Multitaper and Conventional Univariate Techniques (Cambridge, UK: Cambridge University Press).[5]   
Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), pp. 331–334.[6]   
Elliott, D.F., and Rao, K.R. 1982, Fast Transforms: Algorithms, Analyses, Applications (New York: Academic Press).

# 13.5 Digital Filtering in the Time Domain

Suppose that you have a signal that you want to filter digitally. For example, perhaps you want to apply high-pass or low-pass filtering to eliminate noise at low or high frequencies respectively; or perhaps the interesting part of your signal lies only in a certain frequency band, so that you need a bandpass filter. Or, if your measurements are contaminated by 60 $\mathrm { H z }$ power-line interference, you may need a notch filter to remove only a narrow band around that frequency. This section speaks particularly about the case in which you have chosen to do such filtering in the time domain.

Before continuing, we hope you will reconsider this choice. Remember how convenient it is to filter in the Fourier domain. You just take your whole data record, FFT it, multiply the FFT output by a filter function $\mathcal { H } ( f )$ , and then do an inverse FFT to get back a filtered data set in time domain. Here is some additional background on the Fourier technique that you will want to take into account.

- Remember that you must define your filter function $\mathcal { H } ( f )$ for both positive and negative frequencies, and that the magnitude of the frequency extremes is always the Nyquist frequency $1 / ( 2 \Delta )$ , where $\Delta$ is the sampling interval. The magnitude of the smallest nonzero frequencies in the FFT is $\pm 1 / ( \bar { N } \Delta )$ , where $N$ is the number of (complex) points in the FFT. The positive and negative frequencies to which this filter are applied are arranged in wraparound order.   
If the measured data are real, and you want the filtered output also to be real, then your arbitrary filter function should obey $\mathcal { H } ( - f ) = \mathcal { H } ( f ) ^ { * }$ . You can arrange this most easily by picking an $\mathcal { H }$ that is real and even in $f$ .

- If your chosen $\mathcal { H } ( f )$ has sharp vertical edges in it, then the impulse response of your filter (the output arising from a short impulse as input) will have damped “ringing” at frequencies corresponding to these edges. There is nothing wrong with this, but if you don’t like it, then pick a smoother $\mathcal { H } ( f )$ . To get a first-hand look at the impulse response of your filter, just take the inverse FFT of your $\mathcal { H } ( f )$ . If you smooth all edges of the filter function over some number $k$ of points, then the impulse response function of your filter will have a span on the order of a fraction $1 / k$ of the whole data record. If your data set is too long to FFT all at once, then break it up into segments of any convenient size, as long as they are much longer than the impulse response function of the filter. Use zero-padding, if necessary. You should probably remove any trend from the data, by subtracting from it a straight line through the first and last points (i.e., make the first and last points equal to zero). If you are segmenting the data, then you can pick overlapping segments and use only the middle section of each, comfortably distant from edge effects. A digital filter is said to be causal or physically realizable if its output for a particular timestep depends only on inputs at that particular timestep or earlier. It is said to be acausal if its output can depend on both earlier and later inputs. Filtering in the Fourier domain is, in general, acausal, since the data are processed “in a batch,” without regard to time ordering. Don’t let this bother you! Acausal filters can generally give superior performance (e.g., less dispersion of phases, sharper edges, less asymmetric impulse response functions). People use causal filters not because they are better, but because some situations just don’t allow access to out-of-time-order data. Time domain filters can, in principle, be either causal or acausal, but they are most often used in applications where physical realizability is a constraint. For this reason we will restrict ourselves to the causal case in what follows.

If you are still favoring time-domain filtering after all we have said, it is probably because you have a real-time application for which you must process a continuous data stream and wish to output filtered values at the same rate as you receive raw data. Otherwise, it may be that the quantity of data to be processed is so large that you can afford only a very small number of floating operations on each data point and cannot afford even a modest-sized FFT (with a number of floating operations per data point several times the logarithm of the number of points in the data set or segment).

# 13.5.1 Linear Filters

The most general linear filter takes a sequence $x _ { k }$ of input points and produces a sequence $y _ { n }$ of output points by the formula

$$
y _ { n } = \sum _ { k = 0 } ^ { M } c _ { k } \ x _ { n - k } + \sum _ { j = 0 } ^ { N - 1 } d _ { j } \ y _ { n - j - 1 }
$$

Here the $M + 1$ coefficients $c _ { k }$ and the $N$ coefficients $d _ { j }$ are fixed and define the filter response. The filter (13.5.1) produces each new output value from the current and $M$ previous input values, and from its own $N$ previous output values. If $N = 0$ , so that there is no second sum in (13.5.1), then the filter is called nonrecursive or finite impulse response (FIR). If $N \neq 0$ , then it is called recursive or infinite impulse response (IIR). (The term “IIR” connotes only that such filters are capable of having infinitely long impulse responses, not that their impulse response is necessarily long in a particular application. Typically the response of an IIR filter will drop off exponentially at late times, rapidly becoming negligible.)

The relation between the $c _ { k }$ ’s and $d _ { j }$ ’s and the filter response function $\mathcal { H } ( f )$ is

$$
\mathcal { H } ( f ) = \frac { \displaystyle \sum _ { k = 0 } ^ { M } c _ { k } e ^ { - 2 \pi i k ( f \Delta ) } } { \displaystyle 1 - \sum _ { j = 0 } ^ { N - 1 } d _ { j } e ^ { - 2 \pi i ( j + 1 ) ( f \Delta ) } }
$$

where $\Delta$ is, as usual, the sampling interval. The Nyquist interval corresponds to $f \Delta$ between $- 1 / 2$ and $1 / 2$ . For FIR filters the denominator of (13.5.2) is just unity.

Equation (13.5.2) tells how to determine $\mathcal { H } ( f )$ from the $c$ ’s and $d$ ’s. To design a filter, though, we need a way of doing the inverse, getting a suitable set of $c$ ’s and $d$ ’s — as small a set as possible, to minimize the computational burden — from a desired $\mathcal { H } ( f )$ . Entire books are devoted to this issue. Like many other “inverse problems,” it has no all-purpose solution. One clearly has to make compromises, since $\mathcal { H } ( f )$ is a full continuous function, while the short list of $c$ ’s and $d$ ’s represents only a few adjustable parameters. The subject of digital filter design concerns itself with the various ways of making these compromises. We cannot hope to give any sort of complete treatment of the subject, only sketch a couple of basic techniques to get you started. For further details, consult the specialized books (see references).

# 13.5.2 FIR (Nonrecursive) Filters

When the denominator in (13.5.2) is unity, the right-hand side is just a discrete Fourier transform. The transform is easily invertible, giving the desired small number of $c _ { k }$ coefficients in terms of the same small number of values of $\mathcal { H } ( f _ { i } )$ at some discrete frequencies $f _ { i }$ . This fact, however, is not very useful. The reason is that, for values of $c _ { k }$ computed in this way, $\mathcal { H } ( f )$ will tend to oscillate wildly in between the discrete frequencies where it is pinned down to specific values.

A better strategy, and one that is the basis of several formal methods in the literature, is this: Start by pretending that you are willing to have a relatively large number of filter coefficients, that is, a relatively large value of $M$ . Then $\mathcal { H } ( f )$ can be fixed to desired values on a relatively fine mesh, and the $M$ coefficients $c _ { k } , \ k = 0 , \ldots , M - 1$ can be found by an FFT. Next, truncate (set to zero) most of the $c _ { k }$ ’s, leaving nonzero only the first, say $K$ $( c _ { 0 } , c _ { 1 } , \dots , c _ { K - 1 } )$ and last $K - 1$ $( c _ { M - K + 1 } , \dots , c _ { M - 1 } )$ . The last few $c _ { k }$ ’s are filter coefficients at negative lag, because of the wraparound property of the FFT. But we don’t want coefficients at negative lag. Thereforea, we cyclically shift the array of $c _ { k }$ ’s, to bring everything to positive lag. (This corresponds to introducing a time delay into the filter.) Do this by copying the $c _ { k }$ ’s into a new array of length $M$ in the following order:

$$
( c _ { M - K + 1 } , \dots , c _ { M - 1 } , \ c _ { 0 } , \ c _ { 1 } , \dots , c _ { K - 1 } , \ 0 , \ 0 , \dots , 0 )
$$

To see if your truncation is acceptable, take the FFT of the array (13.5.3), giving an approximation to your original $\mathcal { H } ( f )$ . You will generally want to compare the modulus $\vert \mathcal { H } ( f ) \vert$ to your original function, since the time delay will have introduced complex phases into the filter response.

If the new filter function is acceptable, then you are done and have a set of $2 K - 1$ filter coefficients. If it is not acceptable, then you can either (i) increase $K$ and try again, or (ii) do something fancier to improve the acceptability for the same $K$ . An example of something fancier is to modify the magnitudes (but not the phases) of the unacceptable $\mathcal { H } ( f )$ to bring it more in line with your ideal, and then to FFT to get new $c _ { k }$ ’s. Once again set to zero all but the first $2 K - 1$ values of these (no need to cyclically shift since you have preserved the time-delaying phases), and then inverse transform to get a new $\mathcal { H } ( f )$ , which will often be more acceptable. You can iterate this procedure. Note, however, that the procedure will not converge if your requirements for acceptability are more stringent than your $2 K - 1$ coefficients can handle.

The key idea, in other words, is to iterate between the space of coefficients and the space of functions $\mathcal { H } ( f )$ , until a Fourier conjugate pair that satisfies the imposed constraints in both spaces is found. A more formal technique for this kind of iteration is the Remes exchange algorithm, which produces the best Chebyshev approximation to a given desired frequency response with a fixed number of filter coefficients (cf. $\ S 5 . 1 3 )$ .

# 13.5.3 IIR (Recursive) Filters

Recursive filters, whose output at a given time depends both on the current and previous inputs and on previous outputs, can generally have performance that is superior to nonrecursive filters with the same total number of coefficients (or same number of floating operations

per input point). The reason is fairly clear by inspection of (13.5.2): A nonrecursive filter has a frequency response that is a polynomial in the variable $1 / z$ , where

$$
z \equiv e ^ { 2 \pi i ( f \Delta ) }
$$

By contrast, a recursive filter’s frequency response is a rational function in $1 / z$ . The class of rational functions is especially good at fitting functions with sharp edges or narrow features, and most desired filter functions are in this category.

Nonrecursive filters are always stable. If you turn off the sequence of incoming $x _ { i }$ ’s, then after no more than $M$ steps the sequence of $y _ { j }$ ’s produced by (13.5.1) will also turn off. Recursive filters, feeding as they do on their own output, are not necessarily stable. If the coefficients $d _ { j }$ are badly chosen, a recursive filter can have exponentially growing, so-called homogeneous, modes, which become huge even after the input sequence has been turned off. This is not good. The problem of designing recursive filters, therefore, is not just an inverse problem; it is an inverse problem with an additional stability constraint.

How do you tell if the filter (13.5.1) is stable for a given set of $c _ { k }$ and $d _ { j }$ coefficients? Stability depends only on the $d _ { j }$ ’s. The filter is stable if and only if all $N$ complex roots of the characteristic polynomial equation

$$
z ^ { N } - \sum _ { j = 0 } ^ { N - 1 } d _ { j } z ^ { ( N - 1 ) - j } = 0
$$

are inside the unit circle, i.e., satisfy

$$
| z | \le 1
$$

The various methods for constructing stable recursive filters again form a subject area for which you will need more specialized books. One very useful technique, however, is the bilinear transformation method. For this topic we define a new variable $w$ that reparametrizes the frequency $f$ ,

$$
w \equiv \tan [ \pi ( f \Delta ) ] = i \left( \frac { 1 - e ^ { 2 \pi i ( f \Delta ) } } { 1 + e ^ { 2 \pi i ( f \Delta ) } } \right) = i \left( \frac { 1 - z } { 1 + z } \right)
$$

Don’t be fooled by the $i$ ’s in (13.5.7). This equation maps real frequencies $f$ into real values of $w$ . In fact, it maps the Nyquist interval $- \frac { 1 } { 2 } < f \Delta < \frac { 1 } { 2 }$ onto the real $w$ -axis $- \infty < w < + \infty$ . The inverse equation to (13.5.7) is

$$
z = e ^ { 2 \pi i ( f \Delta ) } = \frac { 1 + i w } { 1 - i w }
$$

In reparametrizing $f , w$ also reparametrizes $z$ , of course. Therefore, the condition for stability (13.5.5) – (13.5.6) can be rephrased in terms of $w$ : If the filter response $\mathcal { H } ( f )$ is written as a function of $w$ , then the filter is stable if and only if the poles of the filter function (zeros of its denominator) are all in the upper half complex plane,

$$
\operatorname { I m } ( w ) \geq 0
$$

The idea of the bilinear transformation method is that instead of specifying your desired $\mathcal { H } ( f )$ , you specify only its desired modulus square, $\begin{array} { r } { | \mathcal { H } ( f ) | ^ { 2 } = \mathcal { H } ( f ) \mathcal { H } ( f ) ^ { \ast } = } \end{array}$ $\mathcal { H } ( f ) \mathcal { H } ( - f )$ . Pick this to be approximated by some rational function in $w ^ { 2 }$ . Then find all the poles of this function in the $w$ complex plane. Every pole in the lower half-plane will have a corresponding pole in the upper half-plane, by symmetry. The idea is to form a product of only the factors with good poles, ones in the upper half-plane. This product is your stably realizable $\mathcal { H } ( f )$ . Now substitute equation (13.5.7) to write the function as a rational function in $z$ and compare with equation (13.5.2) to read off the $c$ ’s and $d$ ’s.

The procedure becomes clearer when we go through an example. Suppose we want to design a simple bandpass filter, whose lower cutoff frequency corresponds to a value $w = a$ , and whose upper cutoff frequency corresponds to a value $w = b$ , with $a$ and $b$ both positive numbers. A simple rational function that accomplishes this is

$$
| \mathcal { H } ( f ) | ^ { 2 } = \left( \frac { w ^ { 2 } } { w ^ { 2 } + a ^ { 2 } } \right) \left( \frac { b ^ { 2 } } { w ^ { 2 } + b ^ { 2 } } \right)
$$

This function does not have a very sharp cutoff, but it is illustrative of the more general case. To obtain sharper edges, one could take the function (13.5.10) to some positive integer power, or, equivalently, run the data sequentially through some number of copies of the filter that we will obtain from (13.5.10).

The poles of (13.5.10) are evidently at $w = \pm i a$ and $w = \pm i b$ . Therefore the stably realizable $\mathcal { H } ( f )$ is

$$
{ \mathcal { H } } ( f ) = \left( { \frac { w } { w - i a } } \right) \left( { \frac { i b } { w - i b } } \right) = { \frac { \left( { \frac { 1 - z } { 1 + z } } \right) b } { \left[ \left( { \frac { 1 - z } { 1 + z } } \right) - a \right] \left[ \left( { \frac { 1 - z } { 1 + z } } \right) - b \right] } }
$$

We put the $i$ in the numerator of the second factor in order to end up with real-valued coefficients. If we multiply out all the denominators, (13.5.11) can be rewritten in the form

$$
\mathcal { H } ( f ) = \frac { - \frac { b } { ( 1 + a ) ( 1 + b ) } + \frac { b } { ( 1 + a ) ( 1 + b ) } z ^ { - 2 } } { 1 - \frac { ( 1 + a ) ( 1 - b ) + ( 1 - a ) ( 1 + b ) } { ( 1 + a ) ( 1 + b ) } z ^ { - 1 } + \frac { ( 1 - a ) ( 1 - b ) } { ( 1 + a ) ( 1 + b ) } z ^ { - 2 } }
$$

from which one reads off the filter coefficients for equation (13.5.1),

$$
\begin{array} { l } { c _ { 0 } = - \displaystyle \frac { b } { ( 1 + a ) ( 1 + b ) } } \\ { c _ { 1 } = 0 } \\ { c _ { 2 } = \displaystyle \frac { b } { ( 1 + a ) ( 1 + b ) } } \\ { d _ { 0 } = \displaystyle \frac { ( 1 + a ) ( 1 - b ) + ( 1 - a ) ( 1 + b ) } { ( 1 + a ) ( 1 + b ) } } \\ { d _ { 1 } = - \displaystyle \frac { ( 1 - a ) ( 1 - b ) } { ( 1 + a ) ( 1 + b ) } } \end{array}
$$

This completes the design of the bandpass filter.

Sometimes you can figure out how to construct directly a rational function in $w$ for $\mathcal { H } ( f )$ , rather than having to start with its modulus square. The function that you construct has to have its poles only in the upper half-plane, for stability. It should also have the property of going into its own complex conjugate if you substitute $- w$ for $w$ , so that the filter coefficients will be real.

For example, here is a function for a notch filter, designed to remove only a narrow frequency band around some fiducial frequency $w = w _ { 0 }$ , where $w _ { 0 }$ is a positive number,

$$
\begin{array} { l } { \displaystyle \mathcal { H } ( f ) = \left( \frac { w - w _ { 0 } } { w - w _ { 0 } - i \epsilon w _ { 0 } } \right) \left( \frac { w + w _ { 0 } } { w + w _ { 0 } - i \epsilon w _ { 0 } } \right) } \\ { \displaystyle = \frac { w ^ { 2 } - w _ { 0 } ^ { 2 } } { ( w - i \epsilon w _ { 0 } ) ^ { 2 } - w _ { 0 } ^ { 2 } } } \end{array}
$$

In (13.5.14), the parameter $\epsilon$ is a small positive number that is the desired width of the notch, as

![](images/00022a409547e6a83a3ebfd0c8fc273a7e0adcf4d1a3f343dc87cf8e6f585536.jpg)  
Figure 13.5.1. (a) A “chirp,” or signal whose frequency increases continuously with time. (b) Same signal after it has passed through the notch filter (13.5.15). The parameter $\epsilon$ is here 0.2.   
Figure 13.5.1 shows the results of using a filter of the form (13.5.15) on a “chirp” input signal, one that glides upward in frequency, crossing the notch frequency along the way.

a fraction of $w _ { 0 }$ . Going through the algebra of substituting $z$ for $w$ gives the filter coefficients

$$
\begin{array} { r l } & { c _ { 0 } = \cfrac { 1 + w _ { 0 } ^ { 2 } } { ( 1 + \epsilon w _ { 0 } ) ^ { 2 } + w _ { 0 } ^ { 2 } } } \\ & { c _ { 1 } = - 2 \cfrac { 1 - w _ { 0 } ^ { 2 } } { ( 1 + \epsilon w _ { 0 } ) ^ { 2 } + w _ { 0 } ^ { 2 } } } \\ & { c _ { 2 } = \cfrac { 1 + w _ { 0 } ^ { 2 } } { ( 1 + \epsilon w _ { 0 } ) ^ { 2 } + w _ { 0 } ^ { 2 } } } \\ & { d _ { 0 } = 2 \cfrac { 1 - \epsilon ^ { 2 } w _ { 0 } ^ { 2 } - w _ { 0 } ^ { 2 } } { ( 1 + \epsilon w _ { 0 } ) ^ { 2 } + w _ { 0 } ^ { 2 } } } \\ & { d _ { 1 } = - \cfrac { ( 1 - \epsilon w _ { 0 } ) ^ { 2 } + w _ { 0 } ^ { 2 } } { ( 1 + \epsilon w _ { 0 } ) ^ { 2 } + w _ { 0 } ^ { 2 } } } \end{array}
$$

While the bilinear transformation may seem very general, its applications are limited by some features of the resulting filters. The method is good at getting the general shape of the desired filter, and good where “flatness” is a desired goal. However, the nonlinear mapping between $w$ and $f$ makes it difficult to design to a desired shape for a cutoff, and may move cutoff frequencies (defined by a certain number of dB) from their desired places. Consequently, practitioners of the art of digital filter design reserve the bilinear transformation for specific situations, and arm themselves with a variety of other tricks. We suggest that you do likewise, as your projects demand.

# CITED REFERENCES AND FURTHER READING:

Hamming, R.W. 1983, Digital Filters, 2nd ed. (Englewood Cliffs, NJ: Prentice-Hall).

Antoniou, A. 1979, Digital Filters: Analysis and Design (New York: McGraw-Hill).   
Parks, T.W., and Burrus, C.S. 1987, Digital Filter Design (New York: Wiley).   
Oppenheim, A.V., Schafer, R.W., and Buck, J.R. 1999, Discrete-Time Signal Processing, 2nd ed. (Englewood Cliffs, NJ: Prentice-Hall).   
Rice, J.R. 1964, The Approximation of Functions (Reading, MA: Addison-Wesley); also 1969, op. cit., Vol. 2.   
Rabiner, L.R., and Gold, B. 1975, Theory and Application of Digital Signal Processing (Englewood Cliffs, NJ: Prentice-Hall).

# 13.6 Linear Prediction and Linear Predictive Coding

We begin with a very general formulation that will allow us to make connections to various special cases. Let $\{ y _ { \alpha } ^ { \prime } \}$ be a set of measured values for some underlying set of true values of a quantity $y$ , denoted $\{ y _ { \alpha } \}$ , related to these true values by the addition of random noise,

$$
y _ { \alpha } ^ { \prime } = y _ { \alpha } + n _ { \alpha }
$$

(compare equation 13.3.2, with a somewhat different notation). Our use of a Greek subscript to index the members of the set is meant to indicate that the data points are not necessarily equally spaced along a line, or even ordered; they might be “random” points in three-dimensional space, for example. Now, suppose we want to construct the “best” estimate of the true value of some particular point $y _ { \star }$ as a linear combination of the known, noisy, values. Writing

$$
y _ { \star } = \sum _ { \alpha } d _ { \star \alpha } y _ { \alpha } ^ { \prime } + x _ { \star }
$$

we want to find coefficients $d _ { \star \alpha }$ that minimize, in some way, the discrepancy $x _ { \star }$ . The coefficients $d _ { \star \alpha }$ have a “star” subscript to indicate that they depend on the choice of point $y _ { \star }$ . Later, we might want to let $y _ { \star }$ be one of the existing $y _ { \alpha }$ ’s. In that case, our problem becomes one of optimal filtering or estimation, closely related to the discussion in $\ S 1 3 . 3$ . On the other hand, we might want $y _ { \star }$ to be a completely new point. In that case, our problem will be one of linear prediction.

A natural way to minimize the discrepancy $x _ { \star }$ is in the statistical mean square sense. If angle brackets denote statistical averages, then we seek $d _ { \star \alpha }$ ’s that minimize

$$
\begin{array} { l } { \displaystyle \left. x _ { \star } ^ { 2 } \right. = \left. \left[ \sum _ { \alpha } d _ { \star \alpha } ( y _ { \alpha } + n _ { \alpha } ) - y _ { \star } \right] ^ { 2 } \right. } \\ { = \sum _ { \alpha \beta } ( \left. y _ { \alpha } y _ { \beta } \right. + \left. n _ { \alpha } n _ { \beta } \right. ) d _ { \star \alpha } d _ { \star \beta } - 2 \sum _ { \alpha } \left. y _ { \star } y _ { \alpha } \right. d _ { \star \alpha } + \left. y _ { \star } ^ { 2 } \right. } \end{array}
$$

Here we have used the fact that noise is uncorrelated with signal, e.g., $\left. n _ { \alpha } y _ { \beta } \right. =$ 0. The quantities $\left. y _ { \alpha } y _ { \beta } \right.$ and $\langle y _ { \star } y _ { \alpha } \rangle$ describe the autocorrelation structure of the underlying data. We have already seen an analogous expression, (13.2.2), for the case of equally spaced data points on a line; we will meet correlation several times again in its statistical sense in Chapters 14 and 15. The quantities $\left. n _ { \alpha } n _ { \beta } \right.$ describe the autocorrelation properties of the noise. Often, for point-to-point uncorrelated noise, we have $\left. n _ { \alpha } n _ { \beta } \right. = \left. n _ { \alpha } ^ { 2 } \right. \delta _ { \alpha \beta } .$ . It is convenient to think of the various correlation quantities as comprising matrices and vectors,

$$
\phi _ { \alpha \beta } \equiv \left. y _ { \alpha } y _ { \beta } \right. \qquad \phi _ { \star \alpha } \equiv \left. y _ { \star } y _ { \alpha } \right. \qquad \eta _ { \alpha \beta } \equiv \left. n _ { \alpha } n _ { \beta } \right. \mathrm { o r } \left. n _ { \alpha } ^ { 2 } \right. \delta _ { \alpha \beta }
$$

Setting the derivative of equation (13.6.3) with respect to the $d _ { \star \alpha }$ ’s equal to zero, one readily obtains the set of linear equations

$$
\sum _ { \beta } \left[ \phi _ { \alpha \beta } + \eta _ { \alpha \beta } \right] d _ { \star \beta } = \phi _ { \star \alpha }
$$

If we write the solution as a matrix inverse, then the estimation equation (13.6. becomes, omitting the minimized discrepancy $x _ { \star }$ ,

$$
y _ { \star } \approx \sum _ { \alpha \beta } \phi _ { \star \alpha } \left[ \phi _ { \mu \nu } + \eta _ { \mu \nu } \right] _ { \alpha \beta } ^ { - 1 } y _ { \beta } ^ { \prime }
$$

From equations (13.6.3) and (13.6.5) one can also calculate the expected mean square value of the discrepancy at its minimum, denoted $\left. x _ { \star } ^ { 2 } \right. _ { 0 }$ ,

$$
\left. x _ { \star } ^ { 2 } \right. _ { 0 } = \left. y _ { \star } ^ { 2 } \right. - \sum _ { \beta } d _ { \star \beta } \phi _ { \star \beta } = \left. y _ { \star } ^ { 2 } \right. - \sum _ { \alpha \beta } \phi _ { \star \alpha } \left[ \phi _ { \mu \nu } + \eta _ { \mu \nu } \right] _ { \alpha \beta } ^ { - 1 } \phi _ { \star \beta }
$$

Although the notation is now different, equations (13.6.6) and (13.6.7) are close relatives to equations (3.7.14) and (3.7.15), which we exhibited without proof in connection with kriging interpolation. (See also $\ S 1 3 . 6 . 3$ , below.)

A final general result tells how much the mean square discrepancy $\left. x _ { \star } ^ { 2 } \right.$ is increased if we use the estimation equation (13.6.2) not with the best values $d _ { \star \beta }$ , but with some other values $\hat { d } _ { \star \beta }$ . The above equations then imply

$$
\left. x _ { \star } ^ { 2 } \right. = \left. x _ { \star } ^ { 2 } \right. _ { 0 } + \sum _ { \alpha \beta } ( \widehat { d } _ { \star \alpha } - d _ { \star \alpha } ) \left[ \phi _ { \alpha \beta } + \eta _ { \alpha \beta } \right] ( \widehat { d } _ { \star \beta } - d _ { \star \beta } )
$$

Since the second term is a pure quadratic form, we see that the increase in the discrepancy is only second order in any error made in estimating the $d _ { \star \beta }$ ’s.

# 13.6.1 Connection to Optimal Filtering

If we change “star” to a Greek index, say $\gamma$ , then the above formulas describe optimal filtering, generalizing the discussion of $\ S 1 3 . 3$ . One sees, for example, that if the noise amplitudes $n _ { \alpha }$ go to zero, so likewise do the noise autocorrelations $\eta _ { \alpha \beta }$ , and, canceling a matrix times its inverse, equation (13.6.6) simply becomes $y _ { \gamma } = y _ { \gamma } ^ { \prime }$ . Another special case occurs if the matrices $\phi _ { \alpha \beta }$ and $\eta _ { \alpha \beta }$ are diagonal. In that case, equation (13.6.6) becomes

$$
y _ { \gamma } = \frac { \phi _ { \gamma \gamma } } { \phi _ { \gamma \gamma } + \eta _ { \gamma \gamma } } y _ { \gamma } ^ { \prime }
$$

which is readily recognizable as equation (13.3.6) with $S ^ { 2 } \to \phi _ { \gamma \gamma }$ , $N ^ { 2 }  \eta _ { \gamma \gamma }$ . What is going on is this: For the case of equally spaced data points, and in the Fourier domain, autocorrelations become simply squares of Fourier amplitudes (Wiener-Khinchin theorem, equation 12.0.13), and the optimal filter can be constructed algebraically, as equation (13.6.9), without inverting any matrix.

More generally, in the time domain, or any other domain, an optimal filter (one that minimizes the square of the discrepancy from the underlying true value in the presence of measurement noise) can be constructed by estimating the autocorrelation matrices $\phi _ { \alpha \beta }$ and $\eta _ { \alpha \beta }$ , and applying equation (13.6.6) with $\star  \gamma$ . (Equation 13.6.8 is in fact the basis for the $\ S 1 3 . 3$ ’s statement that even crude optimal filtering can be quite effective.)

# 13.6.2 Linear Prediction

Classical linear prediction specializes to the case where the data points $y _ { \beta }$ are equally spaced along a line, $y _ { i } , i = 0 , 1 , \dotsc , N - 1$ , and we want to use $M$ consecutive values of $y _ { i }$ to predict an $M + 1 \mathrm { s t }$ . Stationarity is assumed. That is, the autocorrelation $\left. y _ { j } y _ { k } \right.$ is assumed to depend only on the difference $| j - k |$ , and not on $j$ or $k$ individually, so that the autocorrelation $\phi$ has only a single index,

$$
\phi _ { j } \equiv \left. y _ { i } y _ { i + j } \right. \approx \frac { 1 } { N - j } \sum _ { i = 0 } ^ { N - j - 1 } y _ { i } y _ { i + j }
$$

Here, the approximate equality shows one way to use the actual data set values to estimate the autocorrelation components. (In fact, there is a better way to make these estimates; see below.) In the situation described, the estimation equation (13.6.2) is

$$
y _ { n } = \sum _ { j = 0 } ^ { M - 1 } d _ { j } y _ { n - j - 1 } + x _ { n }
$$

(compare equation 13.5.1) and equation (13.6.5) becomes the set of $M$ equations for the $M$ unknown $d _ { j }$ ’s, now called the linear prediction $( L P )$ coefficients,

$$
\sum _ { j = 0 } ^ { M - 1 } \phi _ { | j - k - 1 | } d _ { j } = \phi _ { k } \qquad ( k = 1 , \ldots , M )
$$

Notice that while noise is not explicitly included in the equations, it is properly accounted for, $i f$ it is point-to-point uncorrelated: $\phi _ { 0 }$ , as estimated by equation (13.6.10) using measured values $y _ { i } ^ { \prime }$ , actually estimates the diagonal part of $\phi _ { \alpha \alpha } +$ $\eta _ { \alpha \alpha }$ , above. The mean square discrepancy $\left. x _ { n } ^ { 2 } \right.$ is estimated by equation (13.6.7) as

$$
\left. x _ { n } ^ { 2 } \right. = \phi _ { 0 } - \phi _ { 1 } d _ { 0 } - \phi _ { 2 } d _ { 1 } - \dots - \phi _ { M } d _ { M - 1 }
$$

To use linear prediction, we first compute the $d _ { j }$ ’s, using equations (13.6.10) and (13.6.12). We then calculate equation (13.6.13) or, more concretely, apply (13.6.11) to the known record to get an idea of how large are the discrepancies $x _ { i }$ . If the discrepancies are small, then we can continue applying (13.6.11) right on into the future, imagining the unknown “future” discrepancies $x _ { i }$ to be zero. In this application, (13.6.11) is a kind of extrapolation formula. In many situations, this extrapolation turns out to be vastly more powerful than any kind of simple polynomial extrapolation. (By the way, you should not confuse the terms “linear prediction” and “linear extrapolation”; the general functional form used by linear prediction is much more complex than a straight line, or even a low-order polynomial!)

However, to achieve its full usefulness, linear prediction must be constrained in one additional respect: One must take additional measures to guarantee its stability. Equation (13.6.11) is a special case of the general linear filter (13.5.1). The condition that (13.6.11) be stable as a linear predictor is precisely that given in equations (13.5.5) and (13.5.6), namely that the characteristic polynomial

$$
z ^ { N } - \sum _ { j = 0 } ^ { N - 1 } d _ { j } z ^ { ( N - 1 ) - j } = 0
$$

have all $N$ of its roots inside the unit circle

$$
| z | \le 1
$$

There is no guarantee that the coefficients produced by equation (13.6.12) will have this property. If the data contain many oscillations without any particular trend toward increasing or decreasing amplitude, then the complex roots of (13.6.14) will generally all be rather close to the unit circle. The finite length of the data set will cause some of these roots to be inside the unit circle, others outside. In some applications, where the resulting instabilities are slowly growing and the linear prediction is not pushed too far, it is best to use the “unmassaged” LP coefficients that come directly out of (13.6.12). For example, one might be extrapolating to fill a short gap in a data set; then one might extrapolate both forward across the gap and backward from the data beyond the gap. If the two extrapolations agree tolerably well, then instability is not a problem.

When instability is a problem, you have to “massage” the LP coefficients. You do this by (i) solving (numerically) equation (13.6.14) for its $N$ complex roots; (ii) moving the roots to where you think they ought to be inside or on the unit circle; and (iii) reconstituting the now-modified LP coefficients. You may think that step (ii) sounds a little vague. It is. There is no “best” procedure. If you think that your signal is truly a sum of undamped sine and cosine waves (perhaps with incommensurate periods), then you will want simply to move each root $z _ { i }$ onto the unit circle

$$
z _ { i } ~  ~ z _ { i } / | z _ { i } |
$$

In other circumstances it may seem appropriate to reflect a bad root across the unit circle

$$
z _ { i } ~  ~ 1 / z _ { i } ^ { * }
$$

This alternative has the property that it preserves the amplitude of the output of (13.6.11) when it is driven by a sinusoidal set of $x _ { i }$ ’s. It assumes that (13.6.12) has correctly identified the spectral width of a resonance, but only slipped up on identifying its time sense so that signals that should be damped as time proceeds end up growing in amplitude. The choice between (13.6.16) and (13.6.17) sometimes might as well be based on voodoo. We prefer (13.6.17).

Also magical is the choice of $M$ , the number of LP coefficients to use. You should choose $M$ to be as small as works for you, that is, you should choose it by experimenting with your data. Try $M = 5 , 1 0 , 2 0 , 4 0$ . If you need larger $M$ ’s than this, be aware that the procedure of “massaging” all those complex roots is quite sensitive to roundoff error. Double precision is crucial.