# Chapter 1

# Principles of Finite Precision Computation

Numerical precision is the very soul of science.

— SIR D'ARCY WENTWORTH THOMPSON, On Growth and Form (1942)

There will always be a small but steady demand for error-analysts to ... expose bad algorithms' big errors and, more important, supplant bad algorithms with provably good ones.

— WILLIAM M. KAHAN, Interval Arithmetic Options in the Proposed IEEE Floating Point Arithmetic Standard (1980)

Since none of the numbers which we take out from logarithmic and trigonometric tables admit of absolute precision, but are all to a certain extent approximate only, the results of all calculations performed by the aid of these numbers can only be approximately true ...

It may happen, that in special cases the effect of the errors of the tables is so augmented that we may be obliged to reject a method, otherwise the best, and substitute another in its place.

CARLFRIEDRICHGAUSS,TheoriaMotus (1809)

Backward error analysis is no panacea; it may explain errors but not excuse them.

— HEWLETT-PACKARD, HP-15C Advanced Functions Handbook (1982)

This book is concerned with the effects of finite precision arithmetic on numerical algorithms $^2$ , particularly those in numerical linear algebra. Central to any understanding of high-level algorithms is an appreciation of the basic concepts of finite precision arithmetic. This opening chapter briskly imparts the necessary background material. Various examples are used for illustration, some of them familiar (such as the quadratic equation) but several less well known. Common misconceptions and myths exposed during the chapter are highlighted towards the end, in §1.19.

This chapter has few prerequisites and few assumptions are made about the nature of the finite precision arithmetic (for example, the base, number of digits, or mode of rounding, or even whether it is floating point arithmetic). The second chapter deals in detail with the specifics of floating point arithmetic.

A word of warning: some of the examples from §1.12 onward are special ones chosen to illustrate particular phenomena. You may never see in practice the extremes of behaviour shown here. Let the examples show you what can happen, but do not let them destroy your confidence in finite precision arithmetic!

# 1.1. Notation and Background

We describe the notation used in the book and briefly set up definitions needed for this chapter.

Generally, we use

$$
\begin{array}{c c c} \text {c a p i t a l l e t t e r s} & A, B, C, \varDelta , \varLambda & \text {f o r m a t r i c e s}, \\ \text {s u b s c r i p t e d l o w e r c a s e l e t t e r s} & a _ {i j}, b _ {i j}, c _ {i j}, \delta_ {i j}, \lambda_ {i j} & \text {f o r m a t r i x e l e m e n t s}, \\ \text {l o w e r c a s e l e t t e r s} & x, y, z, c, g, h & \text {f o r v e c t o r s}, \\ \text {l o w e r c a s e G r e k l e t t e r s} & \alpha , \beta , \gamma , \theta , \pi & \text {f o r s c a l a r s}, \end{array}
$$

following the widely used convention originally introduced by Householder [644, 1964].

The vector space of all real $m \times n$ matrices is denoted by $\mathbb{R}^{m \times n}$ and the vector space of real $n$ -vectors by $\mathbb{R}^n$ . Similarly, $\mathbb{C}^{m \times n}$ denotes the vector space of complex $m \times n$ matrices. A superscript "T" denotes transpose and a superscript "∗" conjugate transpose.

Algorithms are expressed using a pseudocode based on the MATLAB language [576, 2000], [824]. Comments begin with the $\%$ symbol.

Submatrices are specified with the colon notation, as used in MATLAB and Fortran 90/95: $A(p;q,r;s)$ denotes the submatrix of $A$ formed by the intersection of rows $p$ to $q$ and columns $r$ to $s$ . As a special case, a lone colon as the row or column specifier means to take all entries in that row or column; thus $A(:,j)$ is the $j$ th column of $A$ , and $A(i,:)$ the $i$ th row. The values taken by an integer variable are also described using the colon notation: " $i = 1:n"$ means the same as " $i = 1,2,\ldots,n"$ .

Evaluation of an expression in floating point arithmetic is denoted $fl(\cdot)$ , and we assume that the basic arithmetic operations $op = +, -, *, /$ satisfy

$$
f l (x \operatorname {o p} y) = (x \operatorname {o p} y) (1 + \delta), \quad | \delta | \leq u. \tag {1.1}
$$

Here, $u$ is the unit roundoff (or machine precision), which is typically of order $10^{-8}$ or $10^{-16}$ in single and double precision computer arithmetic, respectively, and between $10^{-10}$ and $10^{-12}$ on pocket calculators. For more on floating point arithmetic see Chapter 2.

Computed quantities (and, in this chapter only, arbitrary approximations) wear a hat. Thus $\widehat{x}$ denotes the computed approximation to $x$ .

Definitions are often (but not always) indicated by “:=” or “=:”, with the colon next to the object being defined.

We make use of the floor and ceiling functions: $\lfloor x\rfloor$ is the largest integer less than or equal to $x$ , and $\lceil x\rceil$ is the smallest integer greater than or equal to $x$ .

The normal distribution with mean $\mu$ and variance $\sigma^2$ is denoted by $N(\mu, \sigma^2)$ .

We measure the cost of algorithms in flops. A flop is an elementary floating point operation: $+, -, /, \text{or} *$ . We normally state only the highest-order terms of flop counts. Thus, when we say that an algorithm for $n \times n$ matrices requires $2n^{3}/3$ flops, we really mean $2n^{3}/3 + O(n^{2})$ flops.

Other definitions and notation are introduced when needed.

Except where stated otherwise, all our numerical experiments were carried out in MATLAB 6.1 (R12.1) [824] on a Pentium III machine under Windows 98 or Windows ME, sometimes in conjunction with the Symbolic Math Toolbox [825]. Thus our computations were done in IEEE standard floating point arithmetic with unit roundoff $u = 2^{-53} \approx 1.1 \times 10^{-16}$ . Sometimes, we simulate single precision arithmetic ( $u \approx 6 \times 10^{-8}$ ) by rounding the result of every elementary operation to single precision (using the function chop from the Matrix Computation Toolbox—see Appendix D).

# 1.2. Relative Error and Significant Digits

Let $\widehat{x}$ be an approximation to a real number $x$ . The most useful measures of the accuracy of $\widehat{x}$ are its absolute error

$$
E _ {\mathrm {a b s}} (\widehat {x}) = | x - \widehat {x} |,
$$

and its relative error

$$
E _ {\mathrm {r e l}} (\widehat {x}) = \frac {| x - \widehat {x} |}{| x |}
$$

(which is undefined if $x = 0$ ). An equivalent definition of relative error is $E_{\mathrm{rel}}(\widehat{x}) = |\rho|$ , where $\widehat{x} = x(1 + \rho)$ . Some authors omit the absolute values from these definitions. When the sign is important we will simply talk about "the error $x - \widehat{x}$ ".

In scientific computation, where answers to problems can vary enormously in magnitude, it is usually the relative error that is of interest, because it is scale independent: scaling $x \to \alpha x$ and $\widehat{x} \to \alpha \widehat{x}$ leaves $E_{\mathrm{rel}}(\widehat{x})$ unchanged.

Relative error is connected with the notion of correct significant digits (or correct significant figures). The significant digits in a number are the first nonzero digit and all succeeding digits. Thus 1.7320 has five significant digits, while 0.0491 has only three. What is meant by correct significant digits in a number that approximates another seems intuitively clear, but a precise definition is problematic, as we explain in a moment. First, note that for a number $\widehat{x}$ with $p$ significant

digits there are only $p + 1$ possible answers to the question, "How many correct significant digits does $\widehat{x}$ have?" (assuming $\widehat{x}$ is not a constant such as 2.0 that is known exactly). Therefore the number of correct significant digits is a fairly crude measure of accuracy in comparison with the relative error. For example, in the following two cases $\widehat{x}$ agrees with $x$ to three but not four significant digits by any reasonable definition, yet the relative errors differ by a factor of about 44:

$$
\begin{array}{l} x = 1. 0 0 0 0 0, \quad \widehat {x} = 1. 0 0 4 9 9, \quad E _ {\text {r e l}} (\widehat {x}) = 4. 9 9 \times 1 0 ^ {- 3}, \\ x = 9. 0 0 0 0 0, \quad \widehat {x} = 8. 9 9 8 9 9, \quad E _ {\text {r e l}} (\widehat {x}) = 1. 1 2 \times 1 0 ^ {- 4}. \\ \end{array}
$$

Here is a possible definition of correct significant digits: an approximation $\widehat{x}$ to $x$ has $p$ correct significant digits if $\widehat{x}$ and $x$ round to the same number to $p$ significant digits. Rounding is the act of replacing a given number by the nearest $p$ significant digit number, with some rule for breaking ties when there are two nearest. This definition of correct significant digits is mathematically elegant and agrees with intuition most of the time. But consider the numbers

$$
\boldsymbol {x} = 0. 9 9 4 9, \quad \widehat {\boldsymbol {x}} = 0. 9 9 5 1.
$$

According to the definition $\widehat{x}$ does not have two correct significant digits ( $x \to 0.99$ , $\widehat{x} \to 1.0$ ), but does have one and three correct significant digits! A definition of correct significant digits that does not suffer from the latter anomaly states that $\widehat{x}$ agrees with $x$ to $p$ significant digits if $|x - \widehat{x}|$ is less than half a unit in the $p$ th significant digit of $x$ . However, this definition implies that 0.123 and 0.127 agree to two significant digits, whereas many people would say that they agree to less than two significant digits.

In summary, while the number of correct significant digits provides a useful way in which to think about the accuracy of an approximation, the relative error is a more precise measure (and is base independent). Whenever we give an approximate answer to a problem we should aim to state an estimate or bound for the relative error.

When $x$ and $\widehat{x}$ are vectors the relative error is most often defined with a norm, as $\| x - \widehat{x} \| / \| x \|$ . For the commonly used norms $\| x \|_{\infty} \coloneqq \max_i |x_i|$ , $\| x \|_1 \coloneqq \sum_i |x_i|$ , and $\| x \|_2 \coloneqq (x^T x)^{1/2}$ , the inequality $\| x - \widehat{x} \| / \| x \| \leq \frac{1}{2} \times 10^{-p}$ implies that components $\widehat{x}_i$ with $|\widehat{x}_i| \approx \| x \|$ have about $p$ correct significant decimal digits, but for the smaller components the inequality merely bounds the absolute error.

A relative error that puts the individual relative errors on an equal footing is the componentwise relative error

$$
\max  _ {i} \frac {\left| x _ {i} - \widehat {x} _ {i} \right|}{\left| x _ {i} \right|},
$$

which is widely used in error analysis and perturbation analysis (see Chapter 7, for example).

As an interesting aside we mention the "tablemaker's dilemma". Suppose you are tabulating the values of a transcendental function such as the sine function and a particular entry is evaluated as 0.124|500000000 correct to a few digits in the last place shown, where the vertical bar follows the final significant digit to be tabulated. Should the final significant digit be 4 or 5? The answer depends

on whether there is a nonzero trailing digit, and there is no simple bound on how many digits we have to compute in order to answer the question.

# 1.3. Sources of Errors

There are three main sources of errors in numerical computation: rounding, data uncertainty, and truncation.

Rounding errors, which are an unavoidable consequence of working in finite precision arithmetic, are largely what this book is about. The remainder of this chapter gives basic insight into rounding errors and their effects.

Uncertainty in the data is always a possibility when we are solving practical problems. It may arise in several ways:

- from errors of measurement or estimation (possibly large: data in engineering and economics [835, 1999], for example, is usually accurate to only a few digits),   
- from errors in storing the data on the computer (rounding errors—tiny),   
- from the result of errors (big or small) in an earlier computation if the data is itself the solution to another problem.

The effects of errors in the data are generally easier to understand than the effects of rounding errors committed during a computation, because data errors can be analysed using perturbation theory for the problem at hand, while intermediate rounding errors require an analysis specific to the given method. This book contains perturbation theory for most of the problems considered, for example, in Chapters 7 (linear systems), 20 (the least squares problem), 21 (underdetermined systems), and 25 (nonlinear systems).

Analysing truncation errors, or discretization errors, is one of the major tasks of the numerical analyst. Many standard numerical methods (for example, the trapezium rule for quadrature, Euler's method for differential equations, and Newton's method for nonlinear equations) can be derived by taking finitely many terms of a Taylor series. The terms omitted constitute the truncation error, and for many methods the size of this error depends on a parameter (often called $h$ , "the step-size") whose appropriate value is a compromise between obtaining a small error and a fast computation.

Because the emphasis of this book is on finite precision computation, with virtually no mention of truncation errors, it would be easy for the reader to gain the impression that the study of numerical methods is dominated by the study of rounding errors. This is certainly not the case. Trefethen explains it well when he discusses how to define numerical analysis [1153, 1992]:

Rounding errors and instability are important, and numerical analysts will always be the experts in these subjects and at pains to ensure that the unwary are not tripped up by them. But our central mission is to compute quantities that are typically uncomputable, from an analytic point of view, and to do it with lightning speed.

In this quotation "uncomputable" means that approximations are necessary, and thus Trefethen's point is that developing good approximations is a more fundamental task than analysing the effects of rounding errors on those approximations.

A possible way to avoid rounding and truncation errors (but not data errors) is to try to solve a problem using a symbolic manipulation package, such as Maple [815] (perhaps via MATLAB's Symbolic Math Toolbox [825]) or Mathematica[3] [818], [1253, 1999]. Indeed, we have used this approach to compute "exact answers" in some of our numerical experiments. While we acknowledge the value of symbolic manipulation as part of the toolkit of the scientific problem solver, we do not study it in this book.

# 1.4. Precision Versus Accuracy

The terms accuracy and precision are often confused or used interchangeably, but it is worth making a distinction between them. Accuracy refers to the absolute or relative error of an approximate quantity. Precision is the accuracy with which the basic arithmetic operations $+, -, *, /$ are performed, and for floating point arithmetic is measured by the unit roundoff $u$ (see (1.1)). Accuracy and precision are the same for the scalar computation $c = a * b$ , but accuracy can be much worse than precision in the solution of a linear system of equations, for example.

It is important to realize that accuracy is not limited by precision, at least in theory. This may seem surprising, and may even appear to contradict many of the results in this book. However, arithmetic of a given precision can be used to simulate arithmetic of arbitrarily high precision, as explained in §27.9. (The catch is that such simulation is too expensive to be of practical use for routine computation.) In all our error analyses there is an implicit assumption that the given arithmetic is not being used to simulate arithmetic of a higher precision.

# 1.5. Backward and Forward Errors

Suppose that an approximation $\widehat{y}$ to $y = f(x)$ is computed in an arithmetic of precision $u$ , where $f$ is a real scalar function of a real scalar variable. How should we measure the "quality" of $\widehat{y}$ ?

In most computations we would be happy with a tiny relative error, $E_{\mathrm{rel}}(\widehat{y}) \approx u$ , but this cannot always be achieved. Instead of focusing on the relative error of $\widehat{y}$ we can ask, "For what set of data have we actually solved our problem?", that is, for what $\Delta x$ do we have $\widehat{y} = f(x + \Delta x)$ ? In general, there may be many such $\Delta x$ , so we should ask for the smallest one. The value of $|\Delta x|$ (or min $|\Delta x|$ ), possibly divided by $|x|$ , is called the backward error. The absolute and relative errors of $\widehat{y}$ are called forward errors, to distinguish them from the backward error. Figure 1.1 illustrates these concepts.

The process of bounding the backward error of a computed solution is called backward error analysis, and its motivation is twofold. First, it interprets rounding errors as being equivalent to perturbations in the data. The data frequently

![](images/a80a3945a63c6bf22913789a656e074453dbad0cfd37d7bda6f5116dce242d7a.jpg)  
Figure 1.1. Backward and forward errors for $y = f(x)$ . Solid line = exact; dotted line = computed.

contains uncertainties due to measurements, previous computations, or errors committed in storing numbers on the computer, as explained in §1.3. If the backward error is no larger than these uncertainties then the computed solution can hardly be criticized—it may be the solution we are seeking, for all we know. The second attraction of backward error analysis is that it reduces the question of bounding or estimating the forward error to perturbation theory, which for many problems is well understood (and only has to be developed once, for the given problem, and not for each method). We discuss perturbation theory in the next section.

A method for computing $y = f(x)$ is called backward stable if, for any $x$ , it produces a computed $\widehat{y}$ with a small backward error, that is, $\widehat{y} = f(x + \Delta x)$ for some small $\Delta x$ . The definition of "small" will be context dependent. In general, a given problem has several methods of solution, some of which are backward stable and some not.

As an example, assumption (1.1) says that the computed result of the operation $x \pm y$ is the exact result for perturbed data $x(1 + \delta)$ and $y(1 + \delta)$ with $|\delta| \leq u$ ; thus addition and subtraction are, by assumption, backward stable operations.

Most routines for computing the cosine function do not satisfy $\widehat{y} = \cos (x + \Delta x)$ with a relatively small $\Delta x$ , but only the weaker relation $\widehat{y} + \Delta y = \cos (x + \Delta x)$ , with relatively small $\Delta y$ and $\Delta x$ . A result of the form

$$
\widehat {y} + \Delta y = f (x + \Delta x), \quad | \Delta y | \leq \epsilon | y |, \quad | \Delta x | \leq \eta | x | \tag {1.2}
$$

is known as a mixed forward-backward error result and is illustrated in Figure 1.2. Provided that $\epsilon$ and $\eta$ are sufficiently small, (1.2) says that the computed value $\widehat{y}$ scarcely differs from the value $\widehat{y} + \Delta y$ that would have been produced by an input $x + \Delta x$ scarcely different from the actual input $x$ . Even more simply, $\widehat{y}$ is almost the right answer for almost the right data.

In general, an algorithm is called numerically stable if it is stable in the mixed forward-backward error sense of (1.2) (hence a backward stable algorithm can certainly be called numerically stable). Note that this definition is specific to problems where rounding errors are the dominant form of errors. The term stability has different meanings in other areas of numerical analysis.

![](images/52c75f9df3880eb354534c1bc13a88797d8b97be80fc786f0848d95a421e9fab.jpg)  
Figure 1.2. Mixed forward-backward error for $y = f(x)$ . Solid line = exact; dotted line = computed.

# 1.6. Conditioning

The relationship between forward and backward error for a problem is governed by the conditioning of the problem, that is, the sensitivity of the solution to perturbations in the data. Continuing the $y = f(x)$ example of the previous section, let an approximate solution $\widehat{y}$ satisfy $\widehat{y} = f(x + \Delta x)$ . Then, assuming for simplicity that $f$ is twice continuously differentiable,

$$
\widehat {y} - y = f (x + \varDelta x) - f (x) = f ^ {\prime} (x) \varDelta x + \frac {f ^ {\prime \prime} (x + \theta \varDelta x)}{2 !} (\varDelta x) ^ {2}, \quad \theta \in (0, 1),
$$

and we can bound or estimate the right-hand side. This expansion leads to the notion of condition number. Since

$$
\frac {\widehat {y} - y}{y} = \left(\frac {x f ^ {\prime} (x)}{f (x)}\right) \frac {\varDelta x}{x} + O \big ((\varDelta x) ^ {2} \big),
$$

the quantity

$$
c (x) = \left| \frac {x f ^ {\prime} (x)}{f (x)} \right|
$$

measures, for small $\Delta x$ , the relative change in the output for a given relative change in the input, and it is called the (relative) condition number of $f$ . If $x$ or $f$ is a vector then the condition number is defined in a similar way using norms, and it measures the maximum relative change, which is attained for some, but not all, vectors $\Delta x$ .

As an example, consider the function $f(x) = \log x$ . The condition number is $c(x) = |1 / \log x|$ , which is large for $x \approx 1$ . This means that a small relative change in $x$ can produce a much larger relative change in $\log x$ for $x \approx 1$ . The reason is that a small relative change in $x$ produces a small absolute change in $f(x) = \log x$ (since $f(x + \Delta x) \approx f(x) + f'(x)\Delta x = f(x) + \Delta x / x$ ), and that change in $\log x$ may be large in a relative sense.

# 1.7 CANCELLATION

When backward error, forward error, and the condition number are defined in a consistent fashion we have the useful rule of thumb that

$$
\text {f o r w a r d} \lesssim \text {c o n d i t i o n} \times \text {b a c k w a r d} \text {e r r o r},
$$

with approximate equality possible. One way to interpret this rule of thumb is to say that the computed solution to an ill-conditioned problem can have a large forward error. For even if the computed solution has a small backward error, this error can be amplified by a factor as large as the condition number when passing to the forward error.

One further definition is useful. If a method produces answers with forward errors of similar magnitude to those produced by a backward stable method, then it is called forward stable. Such a method need not be backward stable itself. Backward stability implies forward stability, but not vice versa. An example of a method that is forward stable but not backward stable is Cramer's rule for solving a $2 \times 2$ linear system, which is discussed in §1.10.1.

# 1.7. Cancellation

Cancellation is what happens when two nearly equal numbers are subtracted. It is often, but not always, a bad thing. Consider the function $f(x) = (1 - \cos x) / x^2$ . With $x = 1.2 \times 10^{-5}$ the value of $\cos x$ rounded to 10 significant figures is

$$
c = 0. 9 9 9 9 9 9 9 9 9 9 9,
$$

so that

$$
1 - c = 0. 0 0 0 0 0 0 0 0 0 1.
$$

Then $(1 - c) / x^2 = 10^{-10} / 1.44 \times 10^{-10} = 0.6944 \ldots$ , which is clearly wrong given the fact that $0 \leq f(x) < 1 / 2$ for all $x \neq 0$ . A 10-significant-figure approximation to $\cos x$ is therefore not sufficient to yield a value of $f(x)$ with even one correct figure. The problem is that $1 - c$ has only 1 significant figure. The subtraction $1 - c$ is exact, but this subtraction produces a result of the same size as the error in $c$ . In other words, the subtraction elevates the importance of the earlier error. In this particular example it is easy to rewrite $f(x)$ to avoid the cancellation. Since $\cos x = 1 - 2\sin^2(x / 2)$ ,

$$
f (x) = \frac {1}{2} \left(\frac {\sin (x / 2)}{x / 2}\right) ^ {2}.
$$

Evaluating this second formula for $f(x)$ with a 10-significant-figure approximation to $\sin (x / 2)$ yields $f(x) = 0.5$ , which is correct to 10 significant figures.

To gain more insight into the cancellation phenomenon consider the subtraction (in exact arithmetic) $\widehat{x} = \widehat{a} -\widehat{b}$ , where $\widehat{a} = a(1 + \varDelta a)$ and $\widehat{b} = b(1 + \varDelta b)$ . The terms $\varDelta a$ and $\varDelta b$ are relative errors or uncertainties in the data, perhaps attributable to previous computations. With $x = a - b$ we have

$$
\left| \frac {x - \widehat {x}}{x} \right| = \left| \frac {- a \Delta a + b \Delta b}{a - b} \right| \leq \max  (| \Delta a |, | \Delta b |) \frac {| a | + | b |}{| a - b |}.
$$

The relative error bound for $\widehat{x}$ is large when $|a - b| \ll |a| + |b|$ , that is, when there is heavy cancellation in the subtraction. This analysis shows that subtractive cancellation causes relative errors or uncertainties already present in $\widehat{a}$ and $\widehat{b}$ to be magnified. In other words, subtractive cancellation brings earlier errors into prominence.

It is important to realize that cancellation is not always a bad thing. There are several reasons. First, the numbers being subtracted may be error free, as when they are from initial data that is known exactly. The computation of divided differences, for example, involves many subtractions, but half of them involve the initial data and are harmless for suitable orderings of the points (see §5.3 and §22.3). The second reason is that cancellation may be a symptom of intrinsic ill conditioning of a problem, and may therefore be unavoidable. Third, the effect of cancellation depends on the role that the result plays in the remaining computation. For example, if $x \gg y \approx z > 0$ then the cancellation in the evaluation of $x + (y - z)$ is harmless.

# 1.8. Solving a Quadratic Equation

Mathematically, the problem of solving the (real) quadratic equation $ax^2 + bx + c = 0$ is trivial: there are two roots (if $a \neq 0$ ), given by

$$
x = \frac {- b \pm \sqrt {b ^ {2} - 4 a c}}{2 a}. \tag {1.3}
$$

Numerically, the problem is more challenging, as neither the successful evaluation of (1.3) nor the accuracy of the computed roots can be taken for granted.

The easiest issue to deal with is the choice of formula for computing the roots. If $b^2 \gg |4ac|$ then $\sqrt{b^2 - 4ac} \approx |b|$ , and so for one choice of sign the formula (1.3) suffers massive cancellation. This is damaging cancellation because one of the arguments, $fl(\sqrt{b^2 - 4ac})$ , is inexact, so the subtraction brings into prominence the earlier rounding errors. How to avoid the cancellation is well known: obtain the larger root (in absolute value), $x_1$ , from

$$
x _ {1} = \frac {- \left(b + \mathrm {s i g n} (b) \sqrt {b ^ {2} - 4 a c}\right)}{2 a},
$$

and the other from the equation $x_{1}x_{2} = c / a$ .

Unfortunately, there is a more pernicious source of cancellation: the subtraction $b^{2} - 4ac$ . Accuracy is lost here when $b^{2} \approx 4ac$ (the case of nearly equal roots), and no algebraic rearrangement can avoid the cancellation. The only way to guarantee accurate computed roots is to use extended precision (or some trick tantamount to the use of extended precision) in the evaluation of $b^{2} - 4ac$ .

Another potential difficulty is underflow and overflow. If we apply the formula (1.3) in IEEE single precision arithmetic (described in §2.3) to the equation $10^{20}x^2 - 3 \cdot 10^{20}x + 2 \cdot 10^{20} = 0$ then overflow occurs, since the maximum floating point number is of order $10^{38}$ ; the roots, however, are innocuous: $x = 1$ and $x = 2$ . Dividing through the equation by $\max(|a|, |b|, |c|) = 3 \cdot 10^{20}$ cures the problem, but this strategy is ineffective for the equation $10^{-20}x^2 - 3x + 2 \cdot 10^{20} = 0$ , whose roots

are $10^{20}$ and $2 \cdot 10^{20}$ . In the latter equation we need to scale the variable: defining $x = 10^{20}y$ gives $10^{20}y^2 - 3 \cdot 10^{20}y + 2 \cdot 10^{20} = 0$ , which is the first equation we considered. These ideas can be built into a general scaling strategy (see the Notes and References), but the details are nontrivial.

As this discussion indicates, not only is it difficult to devise an accurate and robust algorithm for solving a quadratic equation, but it is a nontrivial task to prepare specifications that define precisely what "accurate" and "robust" mean for a given system of floating point arithmetic.

# 1.9. Computing the Sample Variance

In statistics the sample variance of $n$ numbers $x_{1},\ldots ,x_{n}$ is defined as

$$
s _ {n} ^ {2} = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} \left(x _ {i} - \bar {x}\right) ^ {2}, \tag {1.4}
$$

where the sample mean

$$
\bar {x} = \frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i}.
$$

Computing $s_n^2$ from this formula requires two passes through the data, one to compute $\overline{x}$ and the other to accumulate the sum of squares. A two-pass computation is undesirable for large data sets or when the sample variance is to be computed as the data is generated. An alternative formula, found in many statistics textbooks, uses about the same number of operations but requires only one pass through the data:

$$
s _ {n} ^ {2} = \frac {1}{n - 1} \left(\sum_ {i = 1} ^ {n} x _ {i} ^ {2} - \frac {1}{n} \left(\sum_ {i = 1} ^ {n} x _ {i}\right) ^ {2}\right). \tag {1.5}
$$

This formula is very poor in the presence of rounding errors because it computes the sample variance as the difference of two positive numbers, and therefore can suffer severe cancellation that leaves the computed answer dominated by roundoff. In fact, the computed answer can be negative, an event aptly described by Chan, Golub, and LeVeque [214, 1983] as “a blessing in disguise since this at least alerts the programmer that disastrous cancellation has occurred”. In contrast, the original formula (1.4) always yields a very accurate (and nonnegative) answer, unless $n$ is large (see Problem 1.10). Surprisingly, current calculators from more than one manufacturer (but not Hewlett-Packard) appear to use the one-pass formula, and they list it in their manuals.

As an example, if $x = [10000, 10001, 10002]^T$ then, in single precision arithmetic ( $u \approx 6 \times 10^{-8}$ ), the sample variance is computed as 1.0 by the two-pass formula (relative error 0) but 0.0 by the one-pass formula (relative error 1). It might be argued that this data should be shifted by some estimate of the mean before applying the one-pass formula ( $x_i \to x_i - d$ , $i = 1:n$ , which does not change $s_n^2$ ), but a good estimate is not always available and there are alternative one-pass algorithms that will always produce an acceptably accurate answer. For example,

instead of accumulating $\sum_{i}x_{i}$ and $\sum_{i}x_{i}^{2}$ we can accumulate

$$
M _ {k} := \frac {1}{k} \sum_ {i = 1} ^ {k} x _ {i} \quad \mathrm {a n d} \quad Q _ {k} := \sum_ {i = 1} ^ {k} (x _ {i} - M _ {k}) ^ {2} = \sum_ {i = 1} ^ {k} x _ {i} ^ {2} - \frac {1}{k} \left(\sum_ {i = 1} ^ {k} x _ {i}\right) ^ {2},
$$

which can be done via the updating formulae

$$
\begin{array}{l} M _ {1} = x _ {1}, \quad M _ {k} = M _ {k - 1} + \frac {x _ {k} - M _ {k - 1}}{k}, \quad k = 2: n, (1.6a) \\ Q _ {1} = 0, \quad Q _ {k} = Q _ {k - 1} + \frac {(k - 1) \left(x _ {k} - M _ {k - 1}\right) ^ {2}}{k}, \quad k = 2: n, (1.6b) \\ \end{array}
$$

after which $s_n^2 = Q_n / (n - 1)$ . Note that the only subtractions in these recurrences are relatively harmless ones that involve the data $x_i$ . For the numerical example above, (1.6) produces the exact answer. The updating formulae (1.6) are numerically stable, though their error bound is not as small as the one for the two-pass formula (it is proportional to the condition number $\kappa_N$ in Problem 1.7).

The problem of computing the sample variance illustrates well how mathematically equivalent formulae can have different numerical stability properties.

# 1.10. Solving Linear Equations

For an approximate solution $y$ to a linear system $Ax = b$ ( $A \in \mathbb{R}^{n \times n}$ , $b \in \mathbb{R}^n$ ) the forward error is defined as $\|x - y\| / \|x\|$ , for some appropriate norm. Another measure of the quality of $y$ , more or less important depending on the circumstances, is the size of the residual $r = b - Ay$ . When the linear system comes from an interpolation problem, for example, we are probably more interested in how closely $Ay$ represents $b$ than in the accuracy of $y$ . The residual is scale dependent: multiply $A$ and $b$ by $\alpha$ , and $r$ is multiplied by $\alpha$ . One way to obtain a scale-independent quantity is to divide by $\|A\|\|y\|$ , yielding the relative residual

$$
\rho (y) := \frac {\| b - A y \|}{\| A \| \| y \|}.
$$

The importance of the relative residual is explained by the following result, which was probably first proved by Wilkinson (see the Notes and References). We use the 2-norm, defined by $\| x\| _2 = (x^T x)^{1 / 2}$ and $\| A\| _2 = \max_{x\neq 0}\| Ax\| _2 / \| x\| _2$

Lemma 1.1. With the notation above, and for the 2-norm,

$$
\rho (y) = \operatorname * {m i n} \left\{\frac {\| \varDelta A \| _ {2}}{\| A \| _ {2}}: (A + \varDelta A) y = b \right\}.
$$

Proof. If $(A + \Delta A)y = b$ then $r \coloneqq b - Ay = \Delta Ay$ , so $\| r \|_2 \leq \| \Delta A \|_2 \| y \|_2$ , giving

$$
\frac {\| \Delta A \| _ {2}}{\| A \| _ {2}} \geq \frac {\| r \| _ {2}}{\| A \| _ {2} \| y \| _ {2}} = \rho (y). \tag {1.7}
$$

On the other hand, $(A + \Delta A)y = b$ for $\Delta A = r y^T /(y^T y)$ and $\| \varDelta A\| _2=\|r\|_2/\|y\|_2$ , so the bound (1.7) is attainable.

Lemma 1.1 says that $\rho(y)$ measures how much $A$ (but not $b$ ) must be perturbed in order for $y$ to be the exact solution to the perturbed system, that is, $\rho(y)$ equals a normwise relative backward error. If the data $A$ and $b$ are uncertain and $\rho(y)$ is no larger than this uncertainty (e.g., $\rho(y) = O(u)$ ) then the approximate solution $y$ must be regarded as very satisfactory. For other problems the backward error may not be as easy to compute as it is for a general linear system, as we will see for the Sylvester equation (§16.2), the least squares problem (§20.7), and the problem of minimum norm solution of an underdetermined system (§21.2).

To illustrate these concepts we consider two specific linear equation solvers: Gaussian elimination with partial pivoting (GEPP) and Cramer's rule.

# 1.10.1. GEPP Versus Cramer's Rule

Cramer's rule says that the components of the solution to a linear system $Ax = b$ are given by $x_{i} = \operatorname*{det}(A_{i}(b)) / \operatorname*{det}(A)$ , where $A_{i}(b)$ denotes $A$ with its $i$ th column replaced by $b$ . These formulae are a prime example of a method that is mathematically elegant, but useless for solving practical problems. The two flaws in Cramer's rule are its computational expense and its numerical instability. The computational expense needs little comment and is, fortunately, explained in most modern linear algebra textbooks (for example, Strang [1092, 1993] cautions the student that "it would be crazy to solve equations that way"). The numerical instability is less well known, but not surprising. It is present even for $n = 2$ , as a numerical example shows.

We formed a $2 \times 2$ system $Ax = b$ with condition number $\kappa_{2}(A) = \| A \|_{2} \| A^{-1} \|_{2} \approx 10^{13}$ , and solved the system by both Cramer's rule and GEPP in MATLAB (unit roundoff $u \approx 1.1 \times 10^{-16}$ ). The results were as follows, where $r = b - A \widehat{x}$ :

<table><tr><td colspan="3">Cramer&#x27;s rule</td><td>GEPP</td></tr><tr><td>x̂</td><td>r/(\|A\|2\|\widehat{x}\|2)</td><td>x̂</td><td>r/(\|A\|2\|\widehat{x}\|2)</td></tr><tr><td>1.0000</td><td>1.5075 × 10-7</td><td>1.0002</td><td>-4.5689 × 10-17</td></tr><tr><td>2.0001</td><td>1.9285 × 10-7</td><td>2.0004</td><td>-2.1931 × 10-17</td></tr></table>

The scaled residual for GEPP is pleasantly small—of order the unit roundoff. That for Cramer's rule is 10 orders of magnitude larger, showing that the computed solution $\widehat{x}$ from Cramer's rule does not closely satisfy the equations, or, equivalently, does not solve a nearby system. The solutions themselves are similar, both being accurate to three significant figures in each component but incorrect in the fourth significant figure. This is the accuracy we would expect from GEPP because of the rule of thumb "forward error $\lesssim$ condition number $\times$ backward error". That Cramer's rule is as accurate as GEPP in this example, despite its large residual, is perhaps surprising, but it is explained by the fact that Cramer's rule is forward stable for $n = 2$ ; see Problem 1.9. For general $n$ , the accuracy and stability of Cramer's rule depend on the method used to evaluate the determinants, and satisfactory bounds are not known even for the case where the determinants are evaluated by GEPP.

The small residual produced by GEPP in this example is typical: error analysis shows that GEPP is guaranteed to produce a relative residual of order $u$ when $n = 2$ (see §9.3). To see how remarkable a property this is, consider the rounded

version of the exact solution: $z = f l(x) = x + \Delta x$ , where $\| \Delta x \|_2 \leq u \| x \|_2$ . The residual of $z$ satisfies $\| b - A z \|_2 = \| -A \Delta x \|_2 \leq u \| A \|_2 \| x \|_2 \approx u \| A \|_2 \| z \|_2$ . Thus the computed solution from GEPP has about as small a residual as the rounded exact solution, irrespective of its accuracy.

Expressed another way, the errors in GEPP are highly correlated so as to produce a small residual. To emphasize this point, the vector [1.0006, 2.0012], which agrees with the exact solution of the above problem to five significant figures (and therefore is more accurate than the solution produced by GEPP), has a relative residual $\| r\| _2 / (\| A\| _2\| \widehat{x}\| _2)$ of order $10^{-6}$ .

# 1.11. Accumulation of Rounding Errors

Since the first electronic computers were developed in the 1940s, comments along the following lines have often been made: "The enormous speed of current machines means that in a typical problem many millions of floating point operations are performed. This in turn means that rounding errors can potentially accumulate in a disastrous way." This sentiment is true, but misleading. Most often, instability is caused not by the accumulation of millions of rounding errors, but by the insidious growth of just a few rounding errors.

As an example, let us approximate $e = \exp(1)$ by taking finite $n$ in the definition $e := \lim_{n \to \infty} (1 + 1/n)^n$ . Table 1.1 gives results computed in single precision ( $u \approx 6 \times 10^{-8}$ ).

The approximations are poor, degrading as $n$ approaches the reciprocal of the machine precision. For $n$ a power of 10, $1/n$ has a nonterminating binary expansion. When $1 + 1/n$ is formed for $n$ a large power of 10, only a few significant digits from $1/n$ are retained in the sum. The subsequent exponentiation to the power $n$ , even if done exactly, must produce an inaccurate approximation to $e$ (indeed, doing the exponentiation in double precision does not change any of the numbers shown in Table 1.1). Therefore a single rounding error is responsible for the poor results in Table 1.1.

There is a way to compute $(1 + 1/n)^n$ more accurately, using only single precision arithmetic; it is the subject of Problem 1.5.

Strassen's method for fast matrix multiplication provides another example of the unpredictable relation between the number of arithmetic operations and the error. If we evaluate $fl(AB)$ by Strassen's method, for $n \times n$ matrices $A$ and $B$ , and we look at the error as a function of the recursion threshold $n_0 \leq n$ , we find that while the number of operations decreases as $n_0$ decreases from $n$ to 8, the error typically increases; see §23.2.2.

# 1.12. Instability Without Cancellation

It is tempting to assume that calculations free from subtractive cancellation must be accurate and stable, especially if they involve only a small number of operations. The three examples in this section show the fallacy of this assumption.

Table 1.1. Computed approximations $\widehat{f}_n = fl\big((1 + 1 / n)^n\big)$ to $e = 2.71828\ldots$   

<table><tr><td>n</td><td>f̂n</td><td>|e- f̂n|</td></tr><tr><td>10^1</td><td>2.593743</td><td>1.25 × 10^-1</td></tr><tr><td>10^2</td><td>2.704811</td><td>1.35 × 10^-2</td></tr><tr><td>10^3</td><td>2.717051</td><td>1.23 × 10^-3</td></tr><tr><td>10^4</td><td>2.718597</td><td>3.15 × 10^-4</td></tr><tr><td>10^5</td><td>2.721962</td><td>3.68 × 10^-3</td></tr><tr><td>10^6</td><td>2.595227</td><td>1.23 × 10^-1</td></tr><tr><td>10^7</td><td>3.293968</td><td>5.76 × 10^-1</td></tr></table>

# 1.12.1. The Need for Pivoting

Suppose we wish to compute an LU factorization

$$
A = \left[ \begin{array}{c c} \epsilon & - 1 \\ 1 & 1 \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ l _ {2 1} & 1 \end{array} \right] \left[ \begin{array}{c c} u _ {1 1} & u _ {1 2} \\ 0 & u _ {2 2} \end{array} \right], \qquad 0 <   \epsilon \ll 1.
$$

Clearly, $u_{11} = \epsilon$ , $u_{12} = -1$ , $l_{21} = \epsilon^{-1}$ , and $u_{22} = 1 - l_{21}u_{12} = 1 + \epsilon^{-1}$ . In floating point arithmetic, if $\epsilon$ is sufficiently small then $\widehat{u}_{22} = fl(1 + \epsilon^{-1})$ evaluates to $\epsilon^{-1}$ . Assuming $l_{21}$ is computed exactly, we then have

$$
A - \widehat {L} \widehat {U} = \left[ \begin{array}{c c} \epsilon & - 1 \\ 1 & 1 \end{array} \right] - \left[ \begin{array}{c c} 1 & 0 \\ \epsilon^ {- 1} & 1 \end{array} \right] \left[ \begin{array}{c c} \epsilon & - 1 \\ 0 & \epsilon^ {- 1} \end{array} \right] = \left[ \begin{array}{c c} 0 & 0 \\ 0 & 1 \end{array} \right].
$$

Thus the computed LU factors fail completely to reproduce $A$ . Notice that there is no subtraction in the formation of $\widehat{L}$ and $\widehat{U}$ . Furthermore, the matrix $A$ is very well conditioned $(\kappa_{\infty}(A) = 4 / (1 + \epsilon))$ . The problem, of course, is with the choice of $\epsilon$ as the pivot. The partial pivoting strategy would interchange the two rows of $A$ before factorizing it, resulting in a stable factorization.

# 1.12.2. An Innocuous Calculation?

For any $x \geq 0$ the following computation leaves $x$ unchanged:

for $i = 1:60$

$$
x = \sqrt {x}
$$

end

for $i = 1:60$

$$
x = x ^ {2}
$$

end

Since the computation involves no subtractions and all the intermediate numbers lie between 1 and $x$ , we might expect it to return an accurate approximation to $x$ in floating point arithmetic.

On the HP 48G calculator, starting with $x = 100$ the algorithm produces $x = 1.0$ . In fact, for any $x$ , the calculator computes, in place of $f(x) = x$ , the

function

$$
\widehat {f} (x) = \left\{ \begin{array}{l l} 0, & 0 \leq x <   1, \\ 1, & x \geq 1. \end{array} \right.
$$

The calculator is producing a completely inaccurate approximation to $f(x)$ in just 120 operations on nonnegative numbers. How can this happen?

The positive numbers $x$ representable on the HP 48G satisfy $10^{-499} \leq x \leq 9.999 \ldots \times 10^{499}$ . If we define $r(x) = x^{1/2^{60}}$ then, for any machine number $x \geq 1$ ,

$$
\begin{array}{l} 1 \leq r (x) <   r (1 0 ^ {5 0 0}) = 1 0 ^ {5 0 0 / 2 ^ {6 0}} \\ = e ^ {5 0 0 \cdot 2 ^ {- 6 0} \cdot \log 1 0} <   e ^ {1 0 ^ {- 1 5}} \\ = 1 + 1 0 ^ {- 1 5} + \frac {1}{2} \cdot 1 0 ^ {- 3 0} + \dots , \\ \end{array}
$$

which rounds to 1, since the HP 48G works to about 12 decimal digits. Thus for $x > 1$ , the repeated square roots reduce $x$ to 1.0, which the squarings leave unchanged.

For $0 < x < 1$ we have

$$
x \leq 0. \underbrace {9 9 \dots 9} _ {1 2}
$$

on a 12-digit calculator, so we would expect the square root to satisfy

$$
\begin{array}{l} \sqrt {x} \leq (1 - 1 0 ^ {- 1 2}) ^ {1 / 2} = 1 - \frac {1}{2} \cdot 1 0 ^ {- 1 2} - \frac {1}{8} \cdot 1 0 ^ {- 2 4} - \dots \\ = 0. \underbrace {9 9 \dots 9} _ {1 2} 4 \underbrace {9 9 \dots 9} _ {1 1} 8 7 4 9 9 \dots \\ \end{array}
$$

This upper bound rounds to the 12-significant-digit number $0.99 \ldots 9$ . Hence after the 60 square roots we have on the calculator a number $x \leq 0.99 \ldots 9$ . The 60 squarings are represented by $s(x) = x^{2^{60}}$ , and

$$
\begin{array}{l} s (x) \leq s (0. 9 9 \dots 9) = (1 - 1 0 ^ {- 1 2}) ^ {2 ^ {6 0}} \\ = 1 0 ^ {2 ^ {6 0} \log (1 - 1 0 ^ {- 1 2}) \log_ {1 0} e} \\ \approx 1 0 ^ {- 2 ^ {6 0} \cdot 1 0 ^ {- 1 2} \cdot \log_ {1 0} e} \\ \approx 3. 6 \times 1 0 ^ {- 5 0 0 7 0 8}. \\ \end{array}
$$

Because it is smaller than the smallest positive representable number, this result is set to zero on the calculator—a process known as underflow. (The converse situation, in which a result exceeds the largest representable number, is called overflow.)

The conclusion is that there is nothing wrong with the calculator. This innocuous-looking calculation simply exhausts the precision and range of a machine with 12 digits of precision and a 3-digit exponent.

# 1.12.3. An Infinite Sum

It is well known that $\sum_{k=1}^{\infty} k^{-2} = \pi^{2}/6 = 1.644934066848\ldots$ . Suppose we were not aware of this identity and wished to approximate the sum numerically. The most obvious strategy is to evaluate the sum for increasing $k$ until the computed

sum does not change. In single precision this yields the value 1.6447 2532, which is first attained at $k = 4096$ . This agrees with the exact infinite sum to just four significant digits out of a possible nine.

The explanation for the poor accuracy is that we are summing the numbers from largest to smallest, and the small numbers are unable to contribute to the sum. For $k = 4096$ we are forming $s + 4096^{-2} = s + 2^{-24}$ , where $s \approx 1.6$ . Single precision corresponds to a 24-bit significand, so the term we are adding to $s$ "drops off the end" of the computer word, as do all successive terms.

The simplest cure for this inaccuracy is to sum in the opposite order: from smallest to largest. Unfortunately, this requires knowledge of how many terms to take before the summation begins. With $10^{9}$ terms we obtain the computed sum 1.64493406, which is correct to eight significant digits.

For much more on summation, see Chapter 4.

# 1.13. Increasing the Precision

When the only source of errors is rounding, a common technique for estimating the accuracy of an answer is to recompute it at a higher precision and to see how many digits of the original and the (presumably) more accurate answer agree. We would intuitively expect any desired accuracy to be achievable by computing at a high enough precision. This is certainly the case for algorithms possessing an error bound proportional to the precision, which includes all the algorithms described in the subsequent chapters of this book. However, since an error bound is not necessarily attained, there is no guarantee that a result computed in $t$ -digit precision will be more accurate than one computed in $s$ -digit precision, for a given $t > s$ ; in particular, for a very ill conditioned problem both results could have no correct digits.

For illustration, consider the system $Ax = b$ , where $A$ is the inverse of the $5 \times 5$ Hilbert matrix and $b_{i} = (-1)^{i} i$ . (For details of the matrices used in this experiment see Chapter 28.) We solved the system in varying precisions with unit roundoffs $u = 2^{-t}$ , $t = 15:40$ , corresponding to about 4 to 12 decimal places of accuracy. (This was accomplished in MATLAB by using the function chop from the Matrix Computation Toolbox to round the result of every arithmetic operation to $t$ bits; see Appendix D.) The algorithm used was Gaussian elimination (without pivoting), which is perfectly stable for this symmetric positive definite matrix. The upper plot of Figure 1.3 shows $t$ against the relative errors $\| x - \widehat{x} \|_{\infty} / \| x \|_{\infty}$ and the relative residuals $\| b - A \widehat{x} \|_{\infty} / (\| A \|_{\infty} \| \widehat{x} \|_{\infty})$ . The lower plot of Figure 1.3 gives corresponding results for $A = P_{5} + 5I$ , where $P_{5}$ is the Pascal matrix of order 5. The condition numbers $\kappa_{\infty}(A)$ are $1.62 \times 10^{2}$ for the inverse Hilbert matrix and $9.55 \times 10^{5}$ for the shifted Pascal matrix. In both cases the general trend is that increasing the precision decreases the residual and relative error, but the behaviour is not monotonic. The reason for the pronounced oscillating behaviour of the relative error (but not the residual) for the inverse Hilbert matrix is not clear.

An example in which increasing the precision by several bits does not improve

![](images/f75d32228201682d3ddeb912d708c788bd239895b7b9a72388bc4ba79a4b06dd.jpg)

![](images/988612ad6464bb3eea37884192d7406a00877a53044b93f34411203e287e7036.jpg)  
pascal(5) + eye(5)   
Figure 1.3. Forward errors $\|x - \widehat{x}\|_{\infty} / \|x\|_{\infty}$ ("*") and relative residuals $\|b - A\widehat{x}\|_{\infty} / (\|A\|_{\infty} \| \widehat{x}\|_{\infty})$ ("o") versus precision $t = -\log_2 u$ on the $x$ axis.

the accuracy is the evaluation of

$$
y = x + a \sin (b x), \quad x = \frac {1}{7}, \quad a = 1 0 ^ {- 8}, \quad b = 2 ^ {2 4}. \tag {1.8}
$$

Figure 1.4 plots $t$ versus the absolute error, for precisions $u = 2^{-t}$ , $t = 10$ : 40. Since $a\sin (bx)\approx -8.55\times 10^{-9}$ , for $t$ less than about 20 the error is dominated by the error in representing $x = 1 / 7$ . For $22\leq t\leq 31$ the accuracy is (exactly) constant! The plateau over the range $22\leq t\leq 31$ is caused by a fortuitous rounding error in the addition: in the binary representation of the exact answer the 23rd to 32nd digits are 1s, and in the range of $t$ of interest the final rounding produces a number with a 1 in the 22nd bit and zeros beyond, yielding an unexpectedly small error that affects only bits 33 onwards.

A more contrived example in which increasing the precision has no beneficial effect on the accuracy is the following evaluation of $z = f(x)$ :

$$
y = \operatorname {a b s} (3 (x - 0. 5) - 0. 5) / 2 5
$$

$$
\text {i f} y = 0
$$

$$
z = 1
$$

$$
\mathrm {e l s e}
$$

$z = e^{y}$ $\%$ Store to inhibit extended precision evaluation.

$$
z = (z - 1) / y
$$

end

In exact arithmetic, $z = f(2/3) = 1$ , but in MATLAB $\widehat{z} = fl(f(2/3)) = 0.0$ in both (simulated) single precision and double precision arithmetic. A further example is provided by the "innocuous calculation" of §1.12.2, in which a step function is computed in place of $f(x) = x$ for a wide range of precisions.

![](images/0867e54f1502c2e743921ccca1fb082e323559ced780628950ebf1933cfc61be.jpg)  
Figure 1.4. Absolute error versus precision, $t = -\log_2 u$ , in evaluating (1.8).

It is worth stressing that how precision is increased can greatly affect the results obtained. Increasing the precision without preserving important properties such as monotonicity of rounding can vitiate an otherwise reliable algorithm. Increasing the precision without maintaining a correct relationship among the precisions in different parts of an algorithm can also be harmful to the accuracy.

# 1.14. Cancellation of Rounding Errors

It is not unusual for rounding errors to cancel in stable algorithms, with the result that the final computed answer is much more accurate than the intermediate quantities. This phenomenon is not universally appreciated, perhaps because we tend to look at the intermediate numbers in an algorithm only when something is wrong, not when the computed answer is satisfactory. We describe two examples. The first is a very short and rather unusual computation, while the second involves a well-known algorithm for computing a standard matrix decomposition.

# 1.14.1. Computing $(e^x - 1) / x$

Consider the function $f(x) = (e^x - 1) / x = \sum_{i=0}^{\infty} x^i / (i + 1)!$ , which arises in various applications. The obvious way to evaluate $f$ is via the algorithm

% Algorithm 1.

if $x = 0$

$$
f = 1
$$

else

$$
f = (e ^ {x} - 1) / x
$$

end

This algorithm suffers severe cancellation for $|x| \ll 1$ , causing it to produce an inaccurate answer (0 instead of 1, if $x$ is small enough). Here is an alternative:

$\%$ Algorithm 2. $y = e^{x}$ if $y = 1$ $f = 1$ else $f = (y - 1) / 1$ end

At first sight this algorithm seems perverse, since it evaluates both exp and log instead of just exp. Some results computed in MATLAB are shown in Table 1.2. All the results for Algorithm 2 are correct in all the significant figures shown, except for $x = 10^{-15}$ , when the last digit should be 1. On the other hand, Algorithm 1 returns answers that become less and less accurate as $x$ decreases.

To gain insight we look at the numbers in a particular computation with $x = 9 \times 10^{-8}$ and $u = 2^{-24} \approx 6 \times 10^{-8}$ , for which the correct answer is 1.00000005 to the significant digits shown. For Algorithm 1 we obtain a completely inaccurate result, as expected:

$$
f l \left(\frac {e ^ {x} - 1}{x}\right) \equiv f l \left(\frac {1 . 1 9 2 0 9 2 9 0 \times 1 0 ^ {- 7}}{9 . 0 0 0 0 0 0 0 0 \times 1 0 ^ {- 8}}\right) = 1. 3 2 4 5 4 7 6 6.
$$

Algorithm 2 produces a result correct in all but the last digit:

$$
f l \left(\frac {e ^ {x} - 1}{\log e ^ {x}}\right) \equiv f l \left(\frac {1 . 1 9 2 0 9 2 9 0 \times 1 0 ^ {- 7}}{1 . 1 9 2 0 9 2 8 2 \times 1 0 ^ {- 7}}\right) = 1. 0 0 0 0 0 0 0 6.
$$

Here are the quantities that would be obtained by Algorithm 2 in exact arithmetic (correct to the significant digits shown):

$$
\frac {e ^ {x} - 1}{\log e ^ {x}} \equiv \frac {9 . 0 0 0 0 0 0 4 1 \times 1 0 ^ {- 8}}{9 . 0 0 0 0 0 0 0 1 \times 1 0 ^ {- 8}} = 1. 0 0 0 0 0 0 0 5.
$$

We see that Algorithm 2 obtains very inaccurate values of $e^x - 1$ and $\log e^x$ , but the ratio of the two quantities it computes is very accurate. Conclusion: errors cancel in the division in Algorithm 2.

A short error analysis explains this striking cancellation of errors. We assume that the exp and log functions are both computed with a relative error not exceeding the unit roundoff $u$ . The algorithm first computes $\widehat{y} = e^{x}(1 + \delta)$ , $|\delta| \leq u$ . If $\widehat{y} = 1$ then $e^{x}(1 + \delta) = 1$ , so

$$
x = - \log (1 + \delta) = - \delta + \delta^ {2} / 2 - \delta^ {3} / 3 + \dots , \quad | \delta | \leq u,
$$

which implies that the correctly rounded value of $f(x) = 1 + x / 2 + x^2 / 6 + \dots$ is 1, and so $f$ has been evaluated correctly, to the working precision. If $\widehat{y} \neq 1$ then, using (1.1),

$$
\widehat {f} = f l \left(\left(\widehat {y} - 1\right) / \log \widehat {y}\right) = \frac {\left(\widehat {y} - 1\right) \left(1 + \epsilon_ {1}\right)}{\log \widehat {y} \left(1 + \epsilon_ {2}\right)} \left(1 + \epsilon_ {3}\right), \tag {1.9}
$$

Table 1.2. Computed values of $(e^x - 1) / x$ from Algorithms 1 and 2.   

<table><tr><td>x</td><td>Algorithm 1</td><td>Algorithm 2</td></tr><tr><td>10-5</td><td>1.000005000006965</td><td>1.000005000016667</td></tr><tr><td>10-6</td><td>1.000000499962184</td><td>1.000000500000167</td></tr><tr><td>10-7</td><td>1.000000049433680</td><td>1.000000050000002</td></tr><tr><td>10-8</td><td>9.999999939225290 × 10-1</td><td>1.000000005000000</td></tr><tr><td>10-9</td><td>1.000000082740371</td><td>1.000000000500000</td></tr><tr><td>10-10</td><td>1.000000082740371</td><td>1.000000000050000</td></tr><tr><td>10-11</td><td>1.000000082740371</td><td>1.000000000005000</td></tr><tr><td>10-12</td><td>1.000088900582341</td><td>1.000000000000500</td></tr><tr><td>10-13</td><td>9.992007221626408 × 10-1</td><td>1.000000000000050</td></tr><tr><td>10-14</td><td>9.992007221626408 × 10-1</td><td>1.000000000000005</td></tr><tr><td>10-15</td><td>1.110223024625156</td><td>1.000000000000000</td></tr><tr><td>10-16</td><td>0</td><td>1</td></tr></table>

where $|\epsilon_i| \leq u$ , $i = 1:3$ . Thus $\widehat{f}$ is a very accurate approximation to

$$
g (\widehat {y}) := \frac {\widehat {y} - 1}{\log \widehat {y}}.
$$

Note that $\widehat{y} = e^{x}(1 + \delta) =: e^{\widehat{x}}$ , where $\widehat{x} = x + \delta + O(\delta^2)$ . To find how $g(\widehat{y})$ compares with $g(y) = f(x)$ for $y \approx 1$ we write, using the series expansion of $f$ ,

$$
\begin{array}{l} g (\widehat {y}) - f (x) = f (\widehat {x}) - f (x) = \frac {\widehat {x} - x}{2} + O (\widehat {x} - x) ^ {2} \\ = \frac {\delta}{2} + O (\widehat {x} - x) ^ {2} \\ \approx \frac {\delta}{2} g (y) = \frac {\delta}{2} f (x). \\ \end{array}
$$

From (1.9) it follows that $\widehat{f}$ approximates $f$ with relative error at most about $3.5u$ .

The details of the analysis obscure the simplicity of the underlying explanation. The expression $(e^x - 1) / x$ cannot be accurately evaluated for a given $x \approx 0$ in floating point arithmetic, while the expression $(y - 1) / \log y$ can be accurately evaluated for a given $y \approx 1$ . Since these functions are slowly varying near $x = 0$ ( $y = 1$ ), evaluating $(y - 1) / \log y$ with an accurate, if inexact, approximation to $y = e^x \approx 1$ produces an accurate result.

Finally, we note that $f$ is the divided difference of $e^x$ at $x$ and 0: $(e^x - e^0) / (x - 0)$ , and Algorithm 2 rewrites $f$ as the reciprocal of the divided difference of $\log a$ at $y$ and 1. This example illustrates the principle that we should recognize divided differences (which may be in disguise) and take care in their evaluation when the arguments are close.

# 1.14.2. QR Factorization

Any matrix $A \in \mathbb{R}^{m \times n}$ , $m \geq n$ , has a QR factorization $A = QR$ , where $Q \in \mathbb{R}^{m \times n}$ has orthonormal columns and $R \in \mathbb{R}^{n \times n}$ is upper trapezoidal ( $r_{ij} = 0$ for $i > j$ ).

One way of computing the QR factorization is to premultiply $A$ by a sequence of Givens rotations—orthogonal matrices $G$ that differ from the identity matrix only in a $2 \times 2$ principal submatrix, which has the form

$$
\left[ \begin{array}{l l} \cos \theta & \sin \theta \\ - \sin \theta & \cos \theta \end{array} \right].
$$

With $A_1 \coloneqq A$ , a sequence of matrices $A_k$ satisfying $A_k = G_k A_{k-1}$ is generated. Each $A_k$ has one more zero than the last, so $A_p = R$ for $p = n(m - (n + 1)/2)$ . To be specific, we will assume that the zeros are introduced in the order $(n, 1), (n - 1, 1), \ldots, (2, 1); (n, 2), \ldots, (3, 2)$ ; and so on.

For a particular $10 \times 6$ matrix $A$ , Figure 1.5 plots the relative errors $\| A_k - \widehat{A}_k \|_2 / \| A \|_2$ , where $\widehat{A}_k$ denotes the matrix computed in single precision arithmetic ( $u \approx 6 \times 10^{-8}$ ). We see that many of the intermediate matrices are very inaccurate, but the final computed $\widehat{R}$ has an acceptably small relative error, of order $u$ . Clearly, there is heavy cancellation of errors on the last few stages of the computation. This matrix $A \in \mathbb{R}^{10 \times 6}$ was specially chosen, following a suggestion of Wilkinson [1244, 1985], as a full matrix such that $\| A \|_2 \approx 1$ and $A_{10}$ has the form

$$
A _ {1 0} = \left[ \begin{array}{c c c} \widetilde {a} _ {1 1} & \widetilde {a} _ {1 2} & \widetilde {A} (1, 3: n) \\ 0 & 1 & \widetilde {A} (2, 3: n) \\ 0 & y & \widetilde {A} (3: m, 3: n) \end{array} \right], \qquad \| y \| _ {2} \approx 2 u.
$$

Because $y$ is at the roundoff level, the computed $\widehat{y}$ is the result of severe subtractive cancellation and so is dominated by rounding errors. Consequently, the computed Givens rotations $\widetilde{G}_{10},\ldots ,\widetilde{G}_{17}$ , whose purpose is to zero the vector $\widehat{y}$ , and which are determined by ratios involving the elements of $\widehat{y}$ , bear little relation to their exact counterparts, causing $\widehat{A}_k$ to differ greatly from $A_{k}$ for $k = 11,12,\dots$ .

To shed further light on this behaviour, we note that the Givens QR factorization is perfectly backward stable; that is, the computed $\widehat{R}$ is the exact $R$ factor of $A + \Delta A$ , where $\| \Delta A \|_2 \leq cu \| A \|_2$ , with $c$ a modest constant depending on the dimensions (Theorem 19.10). By invoking a perturbation result for the QR factorization (namely (19.35a)) we conclude that $\| R - \widehat{R} \|_2 / \| A \|_2$ is bounded by a multiple of $\kappa_2(A) u$ . Our example is constructed so that $\kappa_2(A)$ is small ( $\approx 24$ ), so we know a priori that the graph in Figure 1.5 must eventually dip down to the unit roundoff level.

We also note that $\| Q - \widehat{Q}\| _2$ is of order $u$ in this example, as again we can show it must be from perturbation theory. Since $Q$ is a product of Givens rotations, this means that even though some of the intermediate Givens rotations are very inaccurate, their product is highly accurate, so in the formation of $Q$ , too, there is extensive cancellation of rounding errors.

# 1.15. Rounding Errors Can Be Beneficial

An old method for computing the largest eigenvalue (in absolute value) of a matrix $A$ and the corresponding eigenvector is the power method, which consists of repeatedly multiplying a given starting vector by $A$ . With scaling to avoid underflow and overflow, the process in its simplest form is

![](images/32203d5e3fb88c5c990adc6e1d1e18342f5af70b79a1a4d6e3bb79fabed505f3.jpg)  
Figure 1.5. Relative errors $\| A_k - \widehat{A}_k\|_2 / \| A\|_2$ for Givens QR factorization. The dotted line is the unit roundoff level.

$\%$ Choose a starting vector $\pmb{x}$

while not converged

$$
\begin{array}{l} x := A x \\ x := x / \left\| x \right\| _ {\infty} \\ \end{array}
$$

end

The theory says that if $A$ has a unique eigenvalue of largest modulus and $x$ is not deficient in the direction of the corresponding eigenvector $v$ , then the power method converges to a multiple of $v$ (at a linear rate).

Consider the matrix

$$
A = \left[ \begin{array}{c c c} 0. 4 & - 0. 6 & 0. 2 \\ - 0. 3 & 0. 7 & - 0. 4 \\ - 0. 1 & - 0. 4 & 0. 5 \end{array} \right],
$$

which has eigenvalues 0, 0.4394, and 1.161 (correct to the digits shown) and an eigenvector $[1,1,1]^T$ corresponding to the eigenvalue zero. If we take $[1,1,1]^T$ as the starting vector for the power method then, in principle, the zero vector is produced in one step, and we obtain no indication of the desired dominant eigenvalue-eigenvector pair. However, when we carry out the computation in MATLAB, the first step produces a vector with elements of order $10^{-16}$ and we obtain after 38 iterations a good approximation to the dominant eigenpair. The explanation is that the matrix $A$ cannot be stored exactly in binary floating point arithmetic. The computer actually works with $A + \Delta A$ for a tiny perturbation $\Delta A$ , and the dominant eigenvalue and eigenvector of $A + \Delta A$ are very good approximations to those of $A$ . The starting vector $[1,1,1]^T$ contains a nonzero (though tiny) component of the dominant eigenvector of $A + \Delta A$ . This component grows rapidly

under multiplication by $A + \Delta A$ , helped by rounding errors in the multiplication, until convergence to the dominant eigenvector is obtained.

Perhaps an even more striking example of beneficial effects of rounding errors is in inverse iteration, which is just the power method applied to the shifted and inverted matrix $(A - \mu I)^{-1}$ . The shift $\mu$ is usually an approximate eigenvalue. The closer $\mu$ is to an eigenvalue, the more nearly singular $A - \mu I$ is, and hence the larger the error in computing $y = (A - \mu I)^{-1}x$ (which is done by solving $(A - \mu I)y = x$ ). However, it can be shown that the error lies almost entirely in the direction of the required eigenvector, and so is harmless; see, for example, Parlett [926, 1998, §4.3] or Golub and Van Loan [509, 1996, §7.6.1].

# 1.16. Stability of an Algorithm Depends on the Problem

An algorithm can be stable as a means for solving one problem but unstable when applied to another problem. One example is the modified Gram-Schmidt method, which is stable when used to solve the least squares problem but can give poor results when used to compute an orthonormal basis of a matrix (see §§19.8 and 20.3).

A lesser known and much simpler example is Gaussian elimination (GE) without pivoting for computing the determinant of an upper Hessenberg matrix. A square matrix $A$ is upper Hessenberg if $a_{ij} = 0$ for $i > j + 1$ . GE transforms $A$ to upper triangular form by $n - 1$ row eliminations, one for each of the boxed entries in this $4 \times 4$ illustration:

$$
A = \left[ \begin{array}{c c c c} \times & \times & \times & \times \\ \framebox {\times} & \times & \times & \times \\ 0 & \framebox {\times} & \times & \times \\ 0 & 0 & \framebox {\times} & \times \end{array} \right] \longrightarrow \left[ \begin{array}{c c c c} \times & \times & \times & \times \\ 0 & \times & \times & \times \\ 0 & 0 & \times & \times \\ 0 & 0 & 0 & \times \end{array} \right] = U.
$$

The determinant of $A$ is given by the product of the diagonal elements of $U$ . It is easy to show that this is a stable way to evaluate $\operatorname{det}(A)$ , even though arbitrarily large multipliers may arise during the elimination. Note, first, that, if $A^{(k)}$ denotes the matrix at the start of the $k$ th stage $(A^{(1)} = A)$ , then

$$
u _ {k k} = a _ {k k} ^ {(k)} = a _ {k k} ^ {(k - 1)} - \frac {a _ {k , k - 1} ^ {(k - 1)} a _ {k - 1 , k} ^ {(k - 1)}}{a _ {k - 1 , k - 1} ^ {(k - 1)}} = a _ {k k} - \frac {a _ {k , k - 1} a _ {k - 1 , k} ^ {(k - 1)}}{a _ {k - 1 , k - 1} ^ {(k - 1)}},
$$

because the $k$ th row of $A^{(k-1)}$ is the same as the $k$ th row of $A$ . In floating point arithmetic the model (1.1) shows that the computed $\widehat{a}_{ij}^{(k)}$ satisfy

$$
\begin{array}{l} \widehat {u} _ {k k} = \widehat {a} _ {k k} ^ {(k)} = \left(a _ {k k} - \frac {a _ {k , k - 1} \widehat {a} _ {k - 1 , k} ^ {(k - 1)}}{\widehat {a} _ {k - 1 , k - 1} ^ {(k - 1)}} (1 + \epsilon_ {1} ^ {(k)}) (1 + \epsilon_ {2} ^ {(k)})\right) (1 + \epsilon_ {3} ^ {(k)}) \\ = a _ {k k} (1 + \epsilon_ {3} ^ {(k)}) - \frac {\left[ a _ {k , k - 1} (1 + \epsilon_ {1} ^ {(k)}) (1 + \epsilon_ {2} ^ {(k)}) (1 + \epsilon_ {3} ^ {(k)}) \right] \widehat {a} _ {k - 1 , k} ^ {(k - 1)}}{\widehat {a} _ {k - 1 , k - 1} ^ {(k - 1)}}, \\ \end{array}
$$

where $|\epsilon_i^{(k)}| \leq u$ , $i = 1:3$ . This equation says that the computed diagonal elements $\widehat{u}_{kk}$ are the exact diagonal elements corresponding not to $A$ , but to a

Table 1.3. Results from GE without pivoting on an upper Hessenberg matrix.   

<table><tr><td></td><td>Exact</td><td>Computed</td><td>Relative error</td></tr><tr><td rowspan="3">x:</td><td>[1.0000]</td><td>[2.3842]</td><td rowspan="3">1.3842</td></tr><tr><td>[1.0000]</td><td>[1.0000]</td></tr><tr><td>[1.0000]</td><td>[1.0000]</td></tr><tr><td>det(A):</td><td>2.0000</td><td>2.0000</td><td>1.9209 × 10-8</td></tr></table>

matrix obtained from $A$ by changing the diagonal elements to $a_{kk}(1 + \epsilon_3^{(k)})$ and the subdiagonal elements to $a_{k,k-1}(1 + \epsilon_1^{(k)})(1 + \epsilon_2^{(k)})(1 + \epsilon_3^{(k)})$ . In other words, the computed $\widehat{u}_{kk}$ are exact for a matrix differing negligibly from $A$ . The computed determinant $\widehat{d}$ , which is given by

$$
\widehat {d} = f l \left(\widehat {u} _ {1 1} \dots \widehat {u} _ {n n}\right) = \widehat {u} _ {1 1} \dots \widehat {u} _ {n n} \left(1 + \eta_ {1}\right) \dots \left(1 + \eta_ {n}\right), \quad \left| \eta_ {i} \right| \leq u,
$$

is therefore a tiny relative perturbation of the determinant of a matrix differing negligibly from $A$ , so this method for evaluating $\operatorname{det}(A)$ is numerically stable (in the mixed forward-backward error sense of (1.2)).

However, if we use GE without pivoting to solve an upper Hessenberg linear system then large multipliers can cause the solution process to be unstable. If we try to extend the analysis above we find that the computed LU factors (as opposed to just the diagonal of $U$ ) do not, as a whole, necessarily correspond to a small perturbation of $A$ .

A numerical example illustrates these ideas. Let

$$
A = \left[ \begin{array}{c c c c} \alpha & - 1 & - 1 & - 1 \\ 1 & 1 & - 1 & - 1 \\ 0 & 1 & 1 & - 1 \\ 0 & 0 & 1 & 1 \end{array} \right].
$$

We took $\alpha = 10^{-7}$ and $b = Ae$ ( $e = [1,1,1,1]^T$ ) and used GE without pivoting in single precision arithmetic ( $u \approx 6 \times 10^{-8}$ ) to solve $Ax = b$ and compute $\operatorname{det}(A)$ . The computed and exact answers are shown to five significant figures in Table 1.3. Not surprisingly, the computed determinant is very accurate. But the computed solution to $Ax = b$ has no correct figures in its first component. This reflects instability of the algorithm rather than ill conditioning of the problem because the condition number $\kappa_{\infty}(A) = 16$ . The source of the instability is the large first multiplier, $a_{21} / a_{11} = 10^7$ .

# 1.17. Rounding Errors Are Not Random

Rounding errors, and their accumulated effect on a computation, are not random. This fact underlies the success of many computations, including some of those described earlier in this chapter. The validity of statistical analysis of rounding

![](images/3884cb42d883ca21eacbd2e80f706462008f5c97c75f20e71de21700d2493f38.jpg)  
Figure 1.6. Values of rational function $r(x)$ computed by Horner's rule (marked as “ $\times$ ”), for $x = 1.606 + (k - 1)2^{-52}$ ; solid line is the “exact” $r(x)$ .

errors is discussed in §2.8. Here we simply give a revealing numerical example (due to W. Kahan).

Define the rational function

$$
r (x) = \frac {6 2 2 - x (7 5 1 - x (3 2 4 - x (5 9 - 4 x)))}{1 1 2 - x (1 5 1 - x (7 2 - x (1 4 - x)))},
$$

which is expressed in a form corresponding to evaluation of the quartic polynomials in the numerator and denominator by Horner's rule. We evaluated $r(x)$ by Horner's rule in double precision arithmetic for 361 consecutive floating point numbers starting with $a = 1.606$ , namely $x = a + (k - 1)2^{-52}$ , $k = 1:361$ ; the function $r(x)$ is virtually constant on this interval. Figure 1.6 plots the computed function values together with a much more accurate approximation to $r(x)$ (computed from a continued fraction representation). The striking pattern formed by the values computed by Horner's rule shows clearly that the rounding errors in this example are not random.

# 1.18. Designing Stable Algorithms

There is no simple recipe for designing numerically stable algorithms. While this helps to keep numerical analysts in business (even in proving each other's algorithms to be unstable!) it is not good news for computational scientists in general. The best advice is to be aware of the need for numerical stability when designing an algorithm and not to concentrate solely on other issues, such as computational cost and parallelizability.

A few guidelines can be given.

1. Try to avoid subtracting quantities contaminated by error (though such subtractions may be unavoidable).   
2. Minimize the size of intermediate quantities relative to the final solution. The reason is that if intermediate quantities are very large then the final answer may be the result of damaging subtractive cancellation. Looked at another way, large intermediate numbers swap the initial data, resulting in loss of information. The classic example of an algorithm where this consideration is important is Gaussian elimination (§9.3), but an even simpler one is recursive summation (§4.2).   
3. Look for different formulations of a computation that are mathematically but not numerically equivalent. For example, the classical Gram-Schmidt method is unstable, but a trivial modification produces the stable modified Gram-Schmidt (MGS) method (§19.8). There are two ways of using the MGS method to solve a least squares problem, the more obvious of which is unstable (§20.3).   
4. It is advantageous to express update formulae as

$$
\text {n e w} = \text {o l d} = + \text {s m a l l}
$$

if the small correction can be computed with many correct significant figures. Numerical methods are often naturally expressed in this form; examples include methods for solving ordinary differential equations, where the correction is proportional to a stepsize, and Newton's method for solving a nonlinear system. A classic example of the use of this update strategy is in iterative refinement for improving the computed solution to a linear system $Ax = b$ , in which by computing residuals $r = b - Ay$ in extended precision and solving update equations that have the residuals as right-hand sides a highly accurate solution can be computed; see Chapter 12. For another example (in which the correction is not necessarily small), see Problem 2.8.

5. Use only well-conditioned transformations of the problem. In matrix computations this amounts to multiplying by orthogonal matrices instead of nonorthogonal, and possibly, ill-conditioned matrices, where possible. See §6.2 for a simple explanation of this advice in terms of norms.   
6. Take precautions to avoid unnecessary overflow and underflow (see §27.8).

Concerning the second point, good advice is to look at the numbers generated during a computation. This was common practice in the early days of electronic computing. On some machines it was unavoidable because the contents of the store were displayed on lights or monitor tubes! Wilkinson gained much insight into numerical stability by inspecting the progress of an algorithm, and sometimes altering its course (for an iterative process with parameters): "Speaking for myself I gained a great deal of experience from user participation, and it was this that led to my own conversion to backward error analysis" [1243, 1980, pp. 112-113] (see also [1227, 1955]). It is ironic that with the wealth of facilities we now have for tracking the progress of numerical algorithms (multiple windows in colour,

graphical tools, fast printers) we often glean less than Wilkinson and his co-workers did from mere paper tape and lights.

# 1.19. Misconceptions

Several common misconceptions and myths have been dispelled in this chapter (none of them for the first time—see the Notes and References). We highlight them in the following list.

1. Cancellation in the subtraction of two nearly equal numbers is always a bad thing (§1.7).   
2. Rounding errors can overwhelm a computation only if vast numbers of them accumulate (§1.11).   
3. A short computation free from cancellation, underflow, and overflow must be accurate (§1.12).   
4. Increasing the precision at which a computation is performed increases the accuracy of the answer (§1.13).   
5. The final computed answer from an algorithm cannot be more accurate than any of the intermediate quantities; that is, errors cannot cancel (§1.14).   
6. Rounding errors can only hinder, not help, the success of a computation (§1.15).

# 1.20. Rounding Errors in Numerical Analysis

Inevitably, much of this book is concerned with numerical linear algebra, because this is the area of numerical analysis in which the effects of rounding errors are most important and have been most studied. In nonlinear problems rounding errors are often not a major concern because other forms of error dominate. Nevertheless the effects of rounding errors have been investigated in many areas of numerical analysis. Throughout the book we give pointers to the general literature (usually in the Notes and References sections), and particular topics (e.g., quadrature) can be tracked down via the index.

# 1.21. Notes and References

The term "correct significant digits" is rarely defined in textbooks; it is apparently assumed that the definition is obvious. One of the earliest books on numerical analysis, by Scarborough [1014, 1950] (first edition 1930), is noteworthy for containing theorems describing the relationship between correct significant digits and relative error.

The first definition of correct significant digits in §1.2 is suggested by Hildebrand [627, 1974, §1.4], who notes its weaknesses.

For a formal proof and further explanation of the fact that precision does not limit accuracy see Priest [955, 1992].

It is possible to develop formal definitions of numerical stability, either with respect to a particular problem, as is frequently done in research papers, or for a very general class of problems, as is done, for example, by de Jong [301, 1977]. Except in §7.6, we do not give formal definitions of stability in this book, preferring instead to adapt informally the basic notions of backward and forward stability to each problem, and thereby to minimize the amount of notation and abstraction.

Backward error analysis was systematically developed, exploited, and popularized by Wilkinson in the 1950s and 1960s in his research papers and, in particular, through his books [1232, 1963], [1233, 1965] (for more about the books see the Notes and References for Chapter 2). Backward error ideas had earlier appeared implicitly in papers by von Neumann and Goldstine [1200, 1947] and Turing [1166, 1948], both of which deal with the solution of linear systems, and explicitly in an unpublished technical report of Givens [490, 1954] on the solution of the symmetric eigenproblem by reduction to tridiagonal form followed by the use of Sturm sequences. The concept of backward error is not limited to numerical linear algebra. It is used, for example, in the numerical solution of differential equations; see Coomes, Koçak, and Palmer [269, 1995], Eirola [386, 1993], Enright [390, 1989], Sanz-Serna and Larsson [1010, 1993], and Shampine [1030, 1994, §2.2],

Conditioning of problems has been studied by numerical analysts since the 1940s, but the first general theory was developed by Rice [985, 1966]. In numerical linear algebra, developing condition numbers is part of the subject of perturbation theory, on which there is a large literature.

The solution of a quadratic equation is a classic problem in numerical analysis. In 1969 Forsythe [428, 1969] pointed out "the near absence of algorithms to solve even a quadratic equation in a satisfactory way on actually used digital computer systems" and he presented specifications suggested by Kahan for a satisfactory solver. Similar, but less technical, presentations are given by Forsythe [427, 1969], Forsythe, Malcolm, and Moler [430, 1977, §2.6], and Young and Gregory [1272, 1972, §§1.2, 3.4]. Kahan [688, 1972] and Sterbenz [1062, 1974] both present algorithms for solving a quadratic equation, accompanied by error analysis.

For more details of algorithms for computing the sample variance and their error analysis, see Chan and Lewis [215, 1979], Chan, Golub, and LeVeque [214, 1983], Barlow [71, 1991], and the references therein. Good general references on computational aspects of statistics are Kennedy and Gentle [723, 1980] and Thisted [1135, 1988].

The issues of conditioning and numerical stability play a role in any discipline in which finite precision computation is performed, but the understanding of these issues is less well developed in some disciplines than in others. In geometric computation, for example, there has been much interest since the late 1980s in the accuracy and robustness of geometric algorithms; see Milenkovic [848, 1988], Hoffmann [632, 1989], Priest [954, 1991], [955, 1992], and Shewchuk [1038, 1997].

It was after discovering Lemma 1.1 that Wilkinson began to develop backward error analysis systematically in the 1950s. He explains that in solving eigenproblems $Ax = \lambda x$ by deflation, the residual of the computed solution, $r \coloneqq A\overline{x} - \overline{\lambda}\overline{x}$ (with the normalization $\overline{x}^T\overline{x} = 1$ ), was "always at noise level relative to $A$ " [1245, 1986]. He continues, "After some years' experience of this I happened, almost by accident, to observe that ... $(A - r\overline{x}^T)\overline{x} = \overline{\lambda}\overline{x} \ldots$ In other words $\overline{\lambda}$ and $\overline{x}$ were

exact for a matrix $A - r\overline{x}^T$ and since $\| r\overline{x}^T\|_2 = \| r\|_2$ , this meant that they were exact for a matrix differing from $A$ at the noise level of the computer." For further details see [1245, 1986] or [1244, 1985].

The numerical stability of Cramer's rule for $2 \times 2$ systems has been investigated by Moler [862, 1974] and Stummel [1095, 1981, §3.3].

The example in §1.12.2 is taken from the HP-15C Advanced Functions Handbook [570, 1982], and a similar example is given by Kahan [690, 1980]. For another approach to analysing this "innocuous calculation" see Problem 3.11. The " $f(2/3)$ " example in §1.13 is also taken from [690, 1980], in which Kahan states three "anti-theorems" that are included among our misconceptions in §1.19.

The example (1.8) is adapted from an example of Sterbenz [1062, 1974, p. 220], who devotes a section to discussing the effects of rerunning a computation at higher precision.

The function $\mathrm{expm1} \coloneqq e^x - 1$ is provided in some floating point processors and mathematics libraries as a more accurate alternative to forming $e^x$ and subtracting 1 [1125, 1992]. It is important in the computation of sinh and tanh, for example (since $\sinh x = e^{-x}(e^{2x} - 1)/2$ ). Of course, it also possible to take the converse approach and express the exponential in terms of trigonometric functions: the expression $(e^x - 1)/x = (e^x + 1)\tanh(x/2)/x$ provides an accurate, if generally expensive, way to evaluate the function investigated in §1.14.1 if an accurate tanh routine is available. Algorithm 2 in §1.14.1 is due to Kahan [690, 1980].

The instability and stability of GE without pivoting applied to an upper Hessenberg matrix (§1.16) was first pointed out and explained by Wilkinson [1228, 1960]; Parlett [923, 1965] also gives a lucid discussion. In the 1950s and 1960s, prior to the development of the QR algorithm, various methods were proposed for the nonsymmetric eigenvalue problem that involved transforming a matrix to Hessenberg form $H$ and then finding the zeros of the characteristic polynomial $\operatorname{det}(H - \lambda I)$ . The most successful method of this type was Laguerre's iteration, described by Parlett [922, 1964], and used in conjunction with Hyman's method for evaluating $\operatorname{det}(H - \lambda I)$ . Hyman's method is described in §14.6.1.

Classic papers dispensing good advice on the dangers inherent in numerical computation are the "pitfalls" papers by Stegun and Abramowitz [1061, 1956] and Forsythe [429, 1970]. The book Numerical Methods That Work by Acton [4, 1970] must also be mentioned as a fount of hard-earned practical advice on numerical computation (look carefully and you will see that the front cover includes a faint image of the word "Usually" before "Work"). If it is not obvious to you that the equation $x^{2} - 10x + 1 = 0$ is best thought of as a nearly linear equation for the smaller root, you will benefit from reading Acton (see p. 58). Everyone should read Acton's "Interlude: What Not to Compute" (pp. 245-257). Acton's more recent work [5, 1996] dispenses further advice.

Finally, we mention the paper "How to Get Meaningless Answers in Scientific Computation (and What to Do About It)" by Fox [437, 1971]. Fox, a contemporary of Wilkinson, founded the Oxford Computing Laboratory and was for many years Professor of Numerical Analysis at Oxford. In this paper he gives numerous examples in which incorrect answers are obtained from plausible numerical methods (many of the examples involve truncation errors as well as rounding errors). The section titles provide a list of reasons why you might compute worthless

answers:

- Your problem might be ill conditioned.   
- Your method might be unstable.   
- You expect too much "analysis" from the computer<sup>4</sup>.   
- Your intuition fails you.   
- You accept consistency too easily.   
- A successful method may fail in slightly different circumstances.   
- Your test examples may be too special.

Fox estimates [437, 1971, p. 296] that "about 80 per cent of all the results printed from the computer are in error to a much greater extent than the user would believe."

# Problems

The road to wisdom?

Well, it's plain and simple to express:

Err

and err

anderragain

but less

and less

and less.

PIET HEIN, Grooks (1966)

1.1. In error analysis it is sometimes convenient to bound $\widetilde{E}_{\mathrm{rel}}(\widehat{x}) = |x - \widehat{x}| / |\widehat{x}|$ instead of $E_{\mathrm{rel}}(\widehat{x}) = |x - \widehat{x}| / |x|$ . Obtain inequalities between $E_{\mathrm{rel}}(\widehat{x})$ and $\widetilde{E}_{\mathrm{rel}}(\widehat{x})$ .   
1.2. (Skeel and Keiper [1044, 1993, §1.2]) The number $y = e^{\pi \sqrt{163}}$ was evaluated at $t$ -digit precision for several values of $t$ , yielding the values shown in the following table, which are in error by at most one unit in the least significant digit (the first two values are padded with trailing zeros):

<table><tr><td>t</td><td>y</td></tr><tr><td>10</td><td>262537412600000000</td></tr><tr><td>15</td><td>262537412640769000</td></tr><tr><td>20</td><td>262537412640768744.00</td></tr><tr><td>25</td><td>262537412640768744.0000000</td></tr><tr><td>30</td><td>262537412640768743.9999999999999</td></tr></table>

Does it follow that the last digit before the decimal point is 4?

1.3. Show how to rewrite the following expressions to avoid cancellation for the indicated arguments.

1. $\sqrt{x + 1} - 1$ , $x \approx 0$ .   
2. $\sin x - \sin y, x \approx y$ .   
3. $x^{2} - y^{2},x\approx y$   
4. $(1 - \cos x) / \sin x, x \approx 0$ .   
5. $c = (a^2 + b^2 - 2ab\cos \theta)^{1/2}$ , $a \approx b$ , $|\theta| \ll 1$ .

1.4. Give stable formulae for computing the square root $x + iy$ of a complex number $a + ib$ .   
1.5. [570, 1982] Show how to compute $\log(1 + x)$ accurately for all $x > -1$ , including for small $|x|$ . Assume that the log function is computed with a relative error not exceeding $u$ . (Hint: adapt the technique used in §1.14.1.) Hence, by writing $(1 + 1/n)^n = \exp(n \log(1 + 1/n))$ , show how to compute $(1 + 1/n)^n$ accurately for large $n$ .   
1.6. (Smith [1051, 1975]) Type the following numbers into your pocket calculator, and look at them upside down (you or the calculator):

<table><tr><td>07734</td><td>The famous “— world” program</td></tr><tr><td>38079</td><td>Object</td></tr><tr><td>318808</td><td>Name</td></tr><tr><td>35007</td><td>Adjective</td></tr><tr><td>57738.57734 × 1040</td><td>Exclamation on finding a bug</td></tr><tr><td>3331</td><td>A high-quality floating point arithmetic</td></tr><tr><td>√31,438,449</td><td>Fallen tree trunks</td></tr></table>

1.7. A condition number for the sample variance (1.4), here denoted by $V(x) : \mathbb{R}^n \to \mathbb{R}$ , can be defined by

$$
\kappa_ {C} := \lim  _ {\epsilon \rightarrow 0} \sup  \left\{\frac {| V (x) - V (x + \Delta x) |}{\epsilon V (x)}: | \Delta x _ {i} | \leq \epsilon | x _ {i} |, i = 1: n \right\}.
$$

Show that

$$
\kappa_ {C} = 2 \frac {\sum_ {i = 1} ^ {n} | x _ {i} - \overline {{x}} | | x _ {i} |}{(n - 1) V (x)}.
$$

This condition number measures perturbations in $x$ componentwise. A corresponding normwise condition number is

$$
\kappa_ {N} := \lim  _ {\epsilon \rightarrow 0} \sup  \left\{\frac {| V (x) - V (x + \Delta x) |}{\epsilon V (x)}: \| \Delta x \| _ {2} \leq \epsilon \| x \| _ {2} \right\}.
$$

Show that

$$
\kappa_ {N} = 2 \frac {\| x \| _ {2}}{\sqrt {(n - 1) V (x)}} = 2 \bigg (1 + \frac {n}{n - 1} \frac {\overline {{{x}}} ^ {2}}{V (x)} \bigg) ^ {1 / 2} \geq \kappa_ {C}.
$$

1.8. (Kahan, Muller, [875, 1989], Francois and Muller [442, 1991]) Consider the recurrence

$$
x _ {k + 1} = 1 1 1 - (1 1 3 0 - 3 0 0 0 / x _ {k - 1}) / x _ {k}, \quad x _ {0} = 1 1 / 2, \quad x _ {1} = 6 1 / 1 1.
$$

In exact arithmetic the $x_{k}$ form a monotonically increasing sequence that converges to 6. Implement the recurrence on your computer or pocket calculator and compare the computed $x_{34}$ with the true value 5.998 (to four correct significant figures). Explain what you see.

The following questions require knowledge of material from later chapters.

1.9. Cramer's rule solves a $2 \times 2$ system $Ax = b$ according to

$$
d = a _ {1 1} a _ {2 2} - a _ {2 1} a _ {1 2},
$$

$$
x _ {1} = \left(b _ {1} a _ {2 2} - b _ {2} a _ {1 2}\right) / d,
$$

$$
x _ {2} = \left(a _ {1 1} b _ {2} - a _ {2 1} b _ {1}\right) / d.
$$

Show that, assuming $d$ is computed exactly (this assumption has little effect on the final bounds), the computed solution $\widehat{x}$ satisfies

$$
\frac {\| x - \widehat {x} \| _ {\infty}}{\| x \| _ {\infty}} \leq \gamma_ {3} \operatorname {c o n d} (A, x), \quad \| b - A x \| _ {\infty} \leq \gamma_ {3} \operatorname {c o n d} \left(A ^ {- 1}\right) \| b \| _ {\infty},
$$

where $\gamma_3 = 3u / (1 - 3u)$ , $\operatorname{cond}(A, x) = \| |A^{-1}||A||x||_{\infty} / ||x||_{\infty}$ , and $\operatorname{cond}(A) = \|\left|A^{-1}\right|\left|A\right|\|_{\infty}$ . This forward error bound is as small as that for a backward stable method (see §§7.2, 7.6), so Cramer's rule is forward stable for $2 \times 2$ systems.

1.10. Show that the computed sample variance $\widehat{V} = fl(V(x))$ produced by the two-pass formula (1.4) satisfies

$$
\frac {| V - \widehat {V} |}{V} \leq (n + 3) u + O (u ^ {2}).
$$

(Note that this error bound does not involve the condition numbers $\kappa_{C}$ or $\kappa_{N}$ from Problem 1.7, at least in the first-order term. This is a rare instance of an algorithm that determines the answer more accurately than the data warrants!)
