# Chapter 24

# The Fast Fourier Transform and Applications

Once the [FFT] method was established

it became clear that it had a long and interesting prehistory

going back as far as Gauss.

But until the advent of computing machines

it was a solution looking for a problem.

— T. W. KÖRNER, Fourier Analysis (1988)

Life as we know it would be very different without the FFT.

CHARLES F. VAN LOAN, Computational

Frameworks for the Fast Fourier Transform (1992)

# 24.1. The Fast Fourier Transform

The matrix-vector product $y = F_{n}x$ , where

$$
F _ {n} = \left(\exp (- 2 \pi i (r - 1) (s - 1) / n)\right) _ {r, s = 1} ^ {n},
$$

is the key computation in the numerical evaluation of Fourier transforms. If the product is formed in the obvious way then $O(n^{2})$ operations are required. The fast Fourier transform (FFT) is a way to compute $y$ in just $O(n\log n)$ operations. This represents a dramatic reduction in complexity.

The FFT is best understood (at least by a numerical analyst!) by interpreting it as the application of a clever factorization of the discrete Fourier transform (DFT) matrix $F_{n}$ .

Theorem 24.1 (Cooley-Tukey radix 2 factorization). If $n = 2^t$ then the DFT matrix $F_{n}$ may be factorized as

$$
F _ {n} = A _ {t} \dots A _ {1} P _ {n}, \tag {24.1}
$$

where $P_{n}$ is a permutation matrix and

$$
\begin{array}{l} A _ {k} = I _ {2 ^ {t - k}} \otimes B _ {2 ^ {k}}, \\ B _ {2 ^ {k}} = \left[ \begin{array}{c c} I _ {r} & \varOmega_ {r} \\ I _ {r} & - \varOmega_ {r} \end{array} \right], \qquad r = 2 ^ {k - 1}, \\ \Omega_ {r} = \operatorname {d i a g} \left(1, \omega_ {k}, \dots , \omega_ {k} ^ {r - 1}\right), \quad \omega_ {k} = \exp \left(- 2 \pi i / 2 ^ {k}\right). \\ \end{array}
$$

Proof. See Van Loan [1182, 1992, Thm. 1.3.3]. $\square$

The theorem shows that we can write $y = F_{n}x$ as

$$
y = A _ {t} \dots A _ {1} P _ {n} x,
$$

which is formed as a sequence of matrix-vector products. It is the sparsity of the $A_{k}$ (two nonzeros per row) that yields the $O(n\log n)$ operation count.

We will not consider the implementation of the FFT, and therefore we do not need to define the "bit reversing" permutation matrix $P_{n}$ in (24.1). However, the way in which the weights $\omega_{k}^{j}$ are computed does affect the accuracy. We will assume that computed weights $\widehat{\omega}_{k}^{j}$ are used that satisfy, for all $j$ and $k$ ,

$$
\widehat {\omega} _ {k} ^ {j} = \omega_ {k} ^ {j} + \epsilon_ {k j}, \quad | \epsilon_ {k j} | \leq \mu . \tag {24.2}
$$

Among the many methods for computing the weights are ones for which we can take $\mu = cu$ , $\mu = cu\log j$ , and $\mu = cuj$ , where $c$ is a constant that depends on the method; see Van Loan [1182, 1992, §1.4].

We are now ready to prove an error bound.

Theorem 24.2. Let $\widehat{y} = fl(F_n x)$ , where $n = 2^t$ , be computed using the Cooley-Tukey radix 2 FFT, and assume that (24.2) holds. Then

$$
\frac {\| y - \widehat {y} \| _ {2}}{\| y \| _ {2}} \leq \frac {t \eta}{1 - t \eta}, \quad \eta := \mu + \gamma_ {4} (\sqrt {2} + \mu).
$$

Proof. Note first that $\| A_k\| _2 = \| B_{2^k}\| _2 = \sqrt{2}$ and

$$
\left\| \left| A _ {k} \right| \right\| _ {2} = \left\| \left| B _ {2 ^ {k}} \right| \right\| _ {2} = \left\| \left[ \begin{array}{l l} I & I \\ I & I \end{array} \right] \right\| _ {2} = 2 = \sqrt {2} \| A _ {k} \| _ {2}. \tag {24.3}
$$

Denote by $\widehat{A}_k$ the matrix defined in terms of the computed $\widehat{\omega}_k^j$ . Then

$$
\begin{array}{l} \widehat {y} = f l \left(\widehat {A} _ {t} \dots \widehat {A} _ {1} P _ {n} x\right), \\ = \left(\widehat {A} _ {t} + \Delta \widehat {A} _ {t}\right) \dots \left(\widehat {A} _ {1} + \Delta \widehat {A} _ {1}\right) P _ {n} x, \\ \end{array}
$$

where, using the fact that each $A_{k}$ has only two nonzeros per row, and recalling that we are using complex arithmetic, $|\Delta \tilde{A}_k| \leq \gamma_4 |\tilde{A}_k|$ , and hence

$$
\| \Delta \widehat {A} _ {k} \| _ {2} \leq \| | \Delta \widehat {A} _ {k} | \| _ {2} \leq \gamma_ {4} \| | \widehat {A} _ {k} | \| _ {2}.
$$

In view of (24.2),

$$
\widehat {A} _ {k} = A _ {k} + \Delta A _ {k}, \quad \| \Delta A _ {k} \| _ {2} \leq \sqrt {2} \mu = \mu \| A _ {k} \| _ {2}. \tag {24.4}
$$

Hence, using (24.3) and (24.4),

$$
\| \left| \widehat {A} _ {k} \right| \| _ {2} \leq \| \left| A _ {k} \right| \| _ {2} + \| \left| \Delta A _ {k} \right| \| _ {2} \leq (\sqrt {2} + \mu) \| A _ {k} \| _ {2}.
$$

Overall, then,

$$
\begin{array}{l} \widehat {y} = \left(A _ {t} + E _ {t}\right) \dots \left(A _ {1} + E _ {1}\right) P _ {n} x, \\ \left\| E _ {k} \right\| _ {2} \leq \left(\mu + \gamma_ {4} (\sqrt {2} + \mu)\right) \left\| A _ {k} \right\| _ {2} = \eta \left\| A _ {k} \right\| _ {2}. \\ \end{array}
$$

Invoking Lemma 3.6 we find that

$$
\begin{array}{l} \| y - \widehat {y} \| _ {2} \leq \left[ (1 + \eta) ^ {t} - 1 \right] \| A _ {t} \| _ {2} \dots \| A _ {1} \| _ {2} \| P _ {n} \| _ {2} \| x \| _ {2} \\ \leq \frac {t \eta}{1 - t \eta} 2 ^ {t / 2} \| x \| _ {2}, \tag {24.5} \\ \end{array}
$$

using Lemma 3.1 for the second inequality. Finally, because $F_{n}$ is $\sqrt{n}$ times a unitary matrix $(F_{n}^{*}F_{n} = nI)$ , $\| x\|_{2} = n^{-1 / 2}\| y\|_{2} = 2^{-t / 2}\| y\|_{2}$ .

Theorem 24.2 says that the Cooley-Tukey radix 2 FFT yields a tiny forward error, provided that the weights are computed stably. It follows immediately that the computation is backward stable, since $\widehat{y} = y + \Delta y = F_{n}x + \Delta y$ implies $\widehat{y} = F_n(x + \Delta x)$ with $\| \Delta x\| _2 / \| x\| _2 = \| \Delta y\| _2 / \| y\| _2$ . If we form $y = F_{n}x$ by conventional multiplication using the exact $F_{n}$ , then (Problem 3.7) $|y - \widehat{y} |\leq \gamma_{n + 2}|F_n||x|$ , so $\| y - \widehat{y}\| _2\leq n^{1 / 2}\gamma_{n + 2}\| y\| _2$ . Hence when $\mu$ is of order $u$ , the FFT has an error bound

![](images/9212fbee36fb86bc97d78fe456baa856416f4e125cc9070d86fb5f6c565f86b8.jpg)  
Figure 24.1. Error in FFT followed by inverse FFT ("o"). Dashed line is error bound.

smaller than that for conventional multiplication by a factor even greater than the reduction in complexity of the method. To sum up, the FFT is perfectly stable.

The inverse transform $x = F_{n}^{-1}y = n^{-1}F_{n}^{*}y$ can again be computed in $O(n\log n)$ operations using the Cooley-Tukey radix 2 factorization, and $\| x - \widehat{x}\| _2 / \| x\| _2$ satisfies the same bound as in Theorem 24.2. (Strictly, we should replace $t$ by $t + 1$ in the bound to account for the rounding error in dividing by $n$ .)

For other variations of the FFT, based on different radices or different factorizations of $F_{n}$ , results analogous to Theorem 24.2 hold.

A simple way to test the error bounds is to compute the FFT followed by the inverse transform, $\widehat{x} = fl(F_n^{-1}fl(F_nx))$ , and to evaluate $e_n = \| x - \widehat{x}\| _2 / \| x\| _2$ . Our analysis gives the bound $e_n\leq 2\log_2n\eta +O(\eta^2)$ . Figure 24.1 plots $e_n$ and the approximate error bound $2\log_{2}nu$ for $n = 2^{k}$ , $k = 0:21$ , with random $x$ from the normal $N(0,1)$ distribution (the FFTs were computed using MATLAB's fft and ifft functions). The errors grow at roughly the same rate as the bound and are on average about a factor of 10 smaller than the bound.

# 24.2. Circulant Linear Systems

A circulant matrix (or circulant, for short) is a special Toeplitz matrix in which the diagonals wrap around:

$$
C = C (c) = \left[ \begin{array}{c c c c} c _ {1} & c _ {n} & \ldots & c _ {2} \\ c _ {2} & c _ {1} & \ldots & \vdots \\ \vdots & \ddots & \ddots & c _ {n} \\ c _ {n} & \ldots & c _ {2} & c _ {1} \end{array} \right] \in \mathbb {C} ^ {n \times n}.
$$

Circulant matrices have the important property that they are diagonalized by the DFT matrix $F_{n}$ :

$$
F _ {n} C F _ {n} ^ {- 1} = D = \operatorname {d i a g} \left(d _ {i}\right).
$$

Moreover, the eigenvalues are given by $d = F_{n}c$ , where $c = [c_{1}, c_{2}, \ldots, c_{n}]^{T}$ . Hence a linear system $Cx = b$ can be solved in $O(n\log n)$ operations with the aid of the FFT as follows:

(1) $d = F_{n}c$   
(2) $g = F_{n}b$   
(3) $h = D^{-1}g$   
(4) $x = F_n^{-1}h$

The computation involves two FFTs, a diagonal scaling, and an inverse FFT. We now analyse the effect of rounding errors. It is convenient to write the result of Theorem 24.2 in the equivalent form (from (24.5))

$$
\widehat {y} = \left(F _ {n} + \Delta F _ {n}\right) x, \quad \| \Delta F _ {n} \| _ {2} \leq n ^ {1 / 2} \frac {t \eta}{1 - t \eta} =: f (n, u). \tag {24.6}
$$

Steps (1) and (2) yield

$$
\begin{array}{l} \widehat {d} = \left(F _ {n} + \Delta_ {1}\right) c, \quad \| \Delta_ {1} \| _ {2} \leq f (n, u), \tag {24.7} \\ \widehat {g} = \left(F _ {n} + \Delta_ {2}\right) b, \quad \| \Delta_ {2} \| _ {2} \leq f (n, u). \\ \end{array}
$$

For steps (3) and (4) we have, using Lemma 3.5,

$$
\begin{array}{l} \widehat {h} = (I + E) \widehat {D} ^ {- 1} \widehat {g}, \quad | E | \leq \sqrt {2} \gamma_ {4} I, \\ \widehat {x} = \left(F _ {n} ^ {- 1} + \Delta_ {3}\right) \widehat {h}, \quad \| \Delta_ {3} \| _ {2} \leq n ^ {- 1} f (n, u). \\ \end{array}
$$

Putting these equations together we have

$$
\begin{array}{l} \widehat {x} = \left(F _ {n} ^ {- 1} + \Delta_ {3}\right) (I + E) \widehat {D} ^ {- 1} \left(F _ {n} + \Delta_ {2}\right) b \\ = \left(I + \Delta_ {3} F _ {n}\right) F _ {n} ^ {- 1} \cdot (I + E) \widehat {D} ^ {- 1} \cdot F _ {n} \left(I + F _ {n} ^ {- 1} \Delta_ {2}\right) b, \\ \end{array}
$$

or

$$
F _ {n} ^ {- 1} \widehat {D} (I + E) ^ {- 1} F _ {n} \cdot \left(I + \Delta_ {3} F _ {n}\right) ^ {- 1} \widehat {x} = \left(I + F _ {n} ^ {- 1} \Delta_ {2}\right) b. \tag {24.8}
$$

Note that $F_{n}^{-1}\widehat{D} (I + E)^{-1}F_{n}$ is a circulant, since $\widehat{D} (I + E)^{-1}$ is diagonal. Hence (24.8) can be written as the circulant system

$$
C (c + \Delta c) (\widehat {x} + \Delta \widehat {x}) = b + \Delta b,
$$

where

$$
\max  \left\{\frac {\| \Delta b \| _ {2}}{\| b \| _ {2}}, \frac {\| \Delta \widehat {x} \| _ {2}}{\| \widehat {x} \| _ {2}} \right\} \leq \frac {n ^ {- 1 / 2} f (n , u)}{1 - n ^ {- 1 / 2} f (n , u)}
$$

and, working to first order,

$$
\begin{array}{l} c + \Delta c = F _ {n} ^ {- 1} (I + E) ^ {- 1} \hat {d} \\ = F _ {n} ^ {- 1} (I + E) ^ {- 1} \left(F _ {n} + \Delta_ {1}\right) c \\ \approx c + F _ {n} ^ {- 1} \left(\Delta_ {1} - E F _ {n}\right) c, \\ \end{array}
$$

so that

$$
\left\| \Delta c \right\| _ {2} \leq n ^ {- 1 / 2} (f (n, u) + \sqrt {2} \gamma_ {4} \sqrt {n}) \| c \| _ {2}.
$$

We summarize our findings as follows.

Theorem 24.3 (Yalamov). Let $C \in \mathbb{C}^{n \times n}$ be a circulant and suppose the system $Cx = b$ is solved by the FFT process described above, where the FFT satisfies (24.6). Then the computed solution $\widehat{x}$ satisfies $C(c + \Delta c)(\widehat{x} + \Delta \widehat{x}) = b + \Delta b$ , where

$$
\operatorname * {m a x} \left\{\frac {\| \varDelta c \| _ {2}}{\| c \| _ {2}}, \frac {\| \varDelta b \| _ {2}}{\| b \| _ {2}}, \frac {\| \varDelta \widehat {x} \| _ {2}}{\| \widehat {x} \| _ {2}} \right\} \leq \eta \log_ {2} n + 6 u + O (u ^ {2}).
$$

The conclusion is that the computed solution from the FFT method for solving a circulant system is very close to the exact solution of a slightly perturbed circulant system. This is a structured mixed forward-backward error result. The computed solution $\hat{x}$ does not, in general, itself solve a nearby circulant system, as can be verified experimentally by computing the "circulant backward error" using techniques from [574, 1992]. The basic reason for the lack of this stronger form of stability is that there are too few parameters in the matrix onto which to throw the backward error.

A forward error bound can be obtained by applying standard perturbation theory to Theorem 24.3: the forward error is bounded by a multiple of $\kappa_{2}(C)u$ . That the forward error can be as large as $\kappa_{2}(C)u$ is clear from the analysis above, because (24.7) shows that the computed eigenvalue $\min_i|\widehat{d}_i|$ is contaminated by an error of order $u\max_i|\widehat{d}_i|$ .

# 24.3. Notes and References

For a unified treatment of the many different versions of the FFT, including implementation details, see Van Loan [1182, 1992].

For a comprehensive survey of the discrete Fourier transform see Briggs and Henson [165, 1995].

The Cooley-Tukey radix 2 FFT was presented in [267, 1965], which is one of the most cited mathematics papers of all time [611, 1998, p. 217].

The history of the FFT is discussed by Cooley [265, 1990], [266, 1994] and Cooley and Tukey [268, 1993]. Cooley [265, 1990] states that the earliest known reference to the FFT is an obscure 1866 paper of Gauss in neoclassic Latin, and he recommends that researchers not publish papers in neoclassic Latin!

Theorem 24.2 is not new, but the proof is more concise than most in the literature. In the first edition of this book the bound of Theorem 24.2 had an extra factor $\sqrt{n}$ , owing to a less sharp analysis. Early references that derive error bounds using the matrix factorization formulation of the FFT are Gentleman and Sande [473, 1966] and Ramos [971, 1971]. A full list of references for error analysis of the FFT up to 1992 is given by Van Loan [1182, 1992, §1.4]. Schatzman [1015, 1996] and Tasche and Zeuner [1129, 2001] discuss the effect of errors in the weights on the computed FFT.

Linzer [793, 1992] showed that the FFT-based circulant solver is forward stable and posed the question of whether or not the solver is backward stable. Backward

error analysis given in the first edition of this book answered this question positively. Yalamov [1264, 2000] shows that the solver is actually structured mixed forward-backward stable, and Theorem 24.3 incorporates this stronger result.

One application of circulant linear systems is in the preconditioned conjugate gradient method for solving Toeplitz systems. The idea of using a circulant preconditioner was suggested by Strang [1091, 1986], and the theory and practice of this technique is now well developed. For more details see Chan and Ng [211, 1996] and the references therein. A good source of results about circulant matrices is the book by Davis [294, 1979].

Highly efficient implementations of the FFT are available in the FFTW software (the "fastest Fourier transform in the west") [447, 1998]; see http://www.ffftw.org/. This software provides automatically optimized C routines for the FFT in one or more dimensions.

# Problems

24.1. (Bailey [53, 1993], Percival [935, 2002]) In high-precision multiplication we have two integer $n$ -vectors $x$ and $y$ representing high-precision numbers and we wish to form the terms $z_k = \sum_{j=1}^k x_j y_{k+1-j}$ , $k = 1:n$ . By padding the vectors with $n$ zeros, these products can be expressed in the form $z_k = \sum_{j=1}^{2n} x_j y_{k+1-j}$ , where $k + 1 - j$ is interpreted as $k + 1 - j + n$ if $k + 1 - j$ is negative. These products represent a convolution: a matrix-vector product involving a circulant matrix. Analogously to the linear system solution in §24.2, this product can be evaluated in terms of discrete Fourier transforms as $z = F_n^{-1}(F_n x \cdot F_n y)$ , where the dot denotes componentwise multiplication of two vectors. Since $x$ and $y$ are integer vectors, the $z_i$ should also be integers, but in practice they will be contaminated by rounding errors. Obtain a bound on $z - \widehat{z}$ and deduce a sufficient condition for the nearest integer vector to $\widehat{z}$ to be the exact $z$ .
