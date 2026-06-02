<!-- source: Numerical Stability.pdf -->

<!-- pdf_type: normal; pages: 33; chunk_pages: 70 -->


<!-- chunk 0001: pages 1-33 -->
# Numerical Stability

The purpose of computing is insight, not numbers. Richard W. Hamming (1962)

The purpose of computing numbers is not yet in sight. Richard W. Hamming (1970)

# 12.1 License to Compute

The geometrical algorithms of computer–aided design systems usually employ floating–point arithmetic — a finite approximation to real–number arithmetic that sacrifices exactitude for computational efficiency and predictable memory requirements. In general, floating–point arithmetic incurs errors whenever real numbers must be stored in the computer memory, or arithmetic operations are performed on numbers already in memory. These errors are typically of small relative magnitude, but under certain circumstances they can be dramatically magnified, yielding numerical results that are essentially meaningless.

To operate a vehicle, one must obtain a driver’s license by demonstrating knowledge of the rules of the road and practical skill in managing the vehicle controls in a manner that does not endanger oneself or others. On the other hand, although scientific and engineering calculations are typically performed in floating–point arithmetic, a medium that can often incur emotional or even physical danger, it is a sad fact that most scientists and engineers are set loose on computers without first having to earn a license to compute. 1

Such considerations are especially acute in the context of computer–aided design algorithms, which carry a higher premium on reliability or “robustness” than virtually any other kind of scientific or engineering computations. The output of a CAD system is rarely an end in itself — most often, it is routed more or less directly to some manufacturing or inspection process, or to finite– element analysis programs that require topologically valid and geometrically accurate three–dimensional shape descriptions. Examples include: numerical– control machining, rapid prototyping, and robot path–planning; inspection by coordinate measuring machines; and mesh generation from solid models for finite–element stress, heat transfer, or fluid flow analysis.

The consequences of feeding erroneous or inconsistent geometric data to such downstream applications is in some cases merely frustrating and wasteful of resources, and in others dangerous or disastrous. Moreover, since the volume of data involved can often be overwhelming, imposing a manual “sanity check” between the CAD system and the end application is neither a practical nor a humane remedy. The onus is therefore on the developers and the implementors of CAD system algorithms to remain vigilant of the pitfalls of floating–point arithmetic, to seek out numerically–stable formulations, and to incorporate internal checks on the accuracy and consistency of their calculations.

Do you ever want to kick the computer? Does it iterate endlessly on your newest algorithm that should have converged in three iterations? And does it finally come to a crashing halt with the insulting message that you divided by zero? These minor trauma are, in fact, the ways the computer manages to kick you and, unfortunately, you almost always deserve it! For it is a sad fact that most of us can more readily compute than think — which might have given rise to that famous definition, “Research is when you don’t know what you are doing.”

Forman S. Acton, Numerical Methods that (Usually) Work [9]

# 12.2 Characterization of Errors

It is important to distinguish between two types of errors that typically arise in geometrical computations. Many problems that concern us do not admit a closed–form solution, expressible in finite terms. For example, the roots of high–degree polynomials are often required in computing curve and surface intersections. As noted in 3.3, however, only polynomials of degree $\leq 4$ allow a “solution by radicals” for their roots. For a polynomial $p ( t )$ of degree $> 4$ , numerical methods, such as the Newton–Raphson iteration

$$
t _ { k + 1 } = t _ { k } - { \frac { p ( t _ { k } ) } { p ^ { \prime } ( t _ { k } ) } } , \quad k = 1 , 2 , \ldots
$$

must be used to approximate the roots. This yields a sequence $t _ { 1 } , t _ { 2 } , \ldots$ of root approximations that approach the exact (simple) root $\tau$ monotonically if the initial “guess” $t _ { 0 }$ is sufficiently close to $\gamma$ . Even with a hypothetical computer capable of exact real arithmetic, one can never obtain exact solutions by such methods. Clearly, the iterations must be halted after a finite number of steps, even if they are rapidly convergent. Similarly, when an analytic function is approximated by expanding it in a Taylor series about a given point, the need to stop after a finite number of terms incurs a truncation error. We call such errors, due to the absence of a closed–form solution, approximation errors — they arise even in the hypothetical case of infinite–precision arithmetic.

On the other hand, even “simple” geometrical problems that nominally do admit closed–form solutions cannot be solved exactly in practice, because each arithmetic step of the solution procedure incurs a rounding or truncation error when real numbers are approximated by fixed–size words in the computer, i.e., one implements the solution in floating–point arithmetic. These errors, which we shall call arithmetic errors, are our main concern at present.

In general, combinations of approximation errors and arithmetic errors will arise in all but the very simplest calculations dealing with free–from curves and surfaces; it is not easy to separate or independently analyze the two. For example, since a root $\tau$ of the polynomial $p ( t )$ satisfies $p ( \tau ) = 0$ , one may plan to choose a small number $\epsilon$ and stop (12.1) at iteration $r$ , such that

$$
| p ( t _ { r } ) | \leq \epsilon .
$$

But this approach is only meaningful if the arithmetic error in computing the value of $p ( t _ { r } )$ is appreciably smaller than the chosen “tolerance” $\epsilon$ . One might think that, since iterative methods incur approximation errors, with which any arithmetic errors are inextricably mixed up, one should not worry unduly about the latter. But this kind of sloppy thinking is a recipe for trouble.

Many iterative methods are, in principle, capable of furnishing results that approach as close as we might practically desire to the exact solution — i.e., we can make the approximation error very small — if we formulate them in such a manner that the end result is not extremely sensitive to small perturbations in the input or intermediate values (i.e., to any arithmetic errors that occur). A problem formulation that has this property is said to be well–conditioned. In an ill–conditioned problem formulation, on the other hand, small input or intermediate perturbations may induce disproportionately large errors in the output — it is then impossible to compute accurate results in floating–point arithmetic, regardless of the iterative method employed.

It is only by detailed analysis of the influence of arithmetic errors — which may be viewed as perturbations of the input values in a hypothetical exact arithmetic computation — that we can quantify this notion of the condition of a problem formulation. We shall consider specific examples in due course: our purpose here has been merely to convince the reader that analyzing the effects of arithmetic error is an important issue, logically quite independent of the presence or absence of approximation errors.

# 12.3 Floating–point Computations

On account of its speed, convenience, and (in most cases) reasonable accuracy, scientific and engineering calculations almost invariably rely on floating–point arithmetic. However, the very speed of modern computers incurs greater risk of encountering those seemingly–rare circumstances in which floating–point calculations yield miserable accuracy. By bringing these pitfalls to the reader’s attention, our intent here is to to quell the usual temptation to rush to the computer and “repeat the classical blunders of generations past” [204].

# 12.3.1 Floating–point Numbers

A normalized floating–point number $f$ in base $b$ has the form

$$
f = m b ^ { e } ,
$$

where $e$ , the exponent, is an integer in a prescribed range $- E \le e \le + E$ and $m$ , the mantissa, is a (signed) fractional real number that has exactly $d$ digits in base $b$ . By “normalized” we mean that the value of $m$ satisfies

$$
1 / b \leq | m | < 1 .
$$

This ensures that all $d$ digits of the mantissa convey useful information; there are no “wasted” leading zeros. Some examples of 4–digit decimal and 12–digit binary normalized floating–point numbers are:

$$
0 . 3 0 7 4 \times 1 0 ^ { 3 } \quad \mathrm { a n d } \quad 0 . 1 0 1 1 0 1 0 0 0 1 0 1 \times 2 ^ { 7 }
$$

(we express the mantissa $m$ explicitly in base $b$ , but the exponent is decimal).

The restriction on $e$ means that no number of absolute value smaller than $1 / b ^ { E + 1 }$ or greater than or equal to $b ^ { E }$ is allowed — calculations that attempt to generate numbers outside this dynamic range will result in floating–point “underflow” or “overflow.” Also, restricting $m$ to just $d$ digits implies that the floating–point number system (12.2) is discrete rather than continuous — it encompasses only a finite set of distinct real values. Real numbers whose true values lie in between two consecutive floating–point numbers (which could be either initial input data, or values generated by arithmetic operations) must be rounded or truncated so as to have a mantissa of only $d$ digits.2

For an arbitrary real value $X$ within dynamic range, $1 / b ^ { E + 1 } \leq | X | < b ^ { E }$ , there exists an integer $e$ and a real value $\mu$ having an unrestricted number of digits in base $b$ , such that $X \equiv \mu b ^ { e }$ and $1 / b \leq | \mu | < 1$ . The floating–point approximation $x$ of the real number $X$ is then defined to be

$$
x = \operatorname { f l o a t } ( X ) = m b ^ { e } ,
$$

where $m$ is determined from $\mu$ by either rounding or truncation at the $d$ –th digit. Hence, the value of $| \mu - m |$ cannot exceed ${ \frac { 1 } { 2 } } b ^ { - d }$ (for rounding) or $b ^ { - d }$ (for truncation), and the greatest fractional error arising in the floating–point approximation of a (non–zero) real number $X$ is thus

$$
\eta \equiv \operatorname* { m a x } _ { X \neq 0 } { \frac { | \operatorname { f l o a t } ( X ) - X | } { | X | } } = k b ^ { - ( d - 1 ) } ,
$$

where the quantity $k$ is defined by

$$
k = \left\{ { \begin{array} { l l } { { \frac { 1 } { 2 } } } & { { \mathrm { f o r ~ r o u n d i n g } , } } \\ { { 1 } } & { { \mathrm { f o r ~ t r u n c a t i o n } . } } \end{array} } \right.
$$

The value $\eta$ given by (12.3) is usually called the machine unit.

Even “innocuous” numbers may incur rounding errors merely on input to the computer. Consider, for example, the representation of the fraction $\textstyle { \frac { 1 } { 1 0 } }$ in normalized binary floating point. In the exact value

$$
( 0 . 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 \ldots ) \times 2 ^ { - 3 } ,
$$

the bit–sequence “1100” is repeated ad infinitum in the mantissa — forcing us to round or truncate after $d$ places. The IEEE standard for double–precision floating point [1], for example, employs a 53–bit binary mantissa $^ 3$ together with rounding, giving a machine unit $\eta = \textstyle { \frac { 1 } { 2 } } 2 ^ { - 5 2 } \approx 1 0 ^ { - 1 6 }$ . Thus, assigning the decimal value 0.1 to a floating–point variable incurs an immediate relative error of maximum magnitude $\eta$ . While this may seem insignificant, there are circumstances under which it can be greatly “magnified” (see §12.4.3).

Humans are accustomed to the decimal numbers, while computers usually employ binary representations. Note that the choice of the parameters $b$ and $d$ , consistent with a specified word–size, has important practical consequences. Consider, for example, the case of single–precision arithmetic using a 32–bit word, of which 24 bits are reserved for the mantissa. If a binary representation and rounding are employed, then (12.3) with $b = 2$ , $d = 2 4$ , and $\begin{array} { r } { k = \frac { 1 } { 2 } } \end{array}$ gives

$$
\begin{array} { r } { \eta = \frac { 1 } { 2 } 2 ^ { - 2 3 } \approx 6 . 0 \times 1 0 ^ { - 8 } . } \end{array}
$$

On the other hand, in a hexadecimal representation ( $b = 1 6$ ), there is room for only $d = 6$ mantissa digits, and if truncation is employed ( $k = 1$ ) we have

$$
\eta = 1 6 ^ { - 5 } \approx 9 . 5 \times 1 0 ^ { - 7 } .
$$

The latter use of the 32–bit word, common on mainframes, yields far larger errors in storing variables or executing arithmetic operations (see Fig. 12.1).

![](images/be5cdf9de52b87cbfac589c033437c810aff07a8fefe33dd7f17a4b31e213bbd.jpg)  
Fig. 12.1. The degree 10 polynomial $p ( t ) = ( t - 0 . 1 ) ( t - 0 . 2 ) \cdot \cdot \cdot ( t - 1 . 0 )$ evaluated by Horner’s method in single–precision floating point using: binary arithmetic with rounding (on the left), and hexadecimal arithmetic with truncation (on the right). The latter gives arithmetic errors with both a greater spread and a systematic bias.

# 12.3.2 Floating–point Arithmetic

Let $^ *$ represent any of the four basic arithmetic operations $\{ + , - , \times , \div \}$ . Given two floating–point numbers $x$ and $y$ of the form (12.2), we denote the result of a floating–point arithmetic operation on them by $\mathrm { H o a t } ( x * y )$ . In general, this result differs from the exact result $x * y$ , since the latter typically exceeds the constraint of $d$ mantissa digits. However, virtually all modern computers4 have floating–point arithmetic processors designed [429] so as to ensure that the fractional error in each individual arithmetic step is also bounded by the machine unit:

$$
{ \frac { | \operatorname { f l o a t } ( x * y ) - x * y | } { | x * y | } } \leq \eta ,
$$

where we assume that $x * y \ne 0$ (and $y \ne 0$ for the case of division). This seems, at first sight, like a very promising result: it indicates that the relative error incurred in each floating–point arithmetic operation is bounded by the small quantity $\eta$ . On re–writing (12.4) in the form

$$
( 1 - \eta ) x * y \le \mathrm { H o a t } ( x * y ) \le ( 1 + \eta ) x * y ,
$$

one might hope to apply bounds of the above form to each arithmetic step of an algorithm, and hence monitor the propagation of floating–point round–off error through any calculation of interest.

By way of example, consider evaluation of the polynomial (3.1) by Horner’s method, which requires $n$ multiplications and additions:

$$
P _ { k } = t \times P _ { k - 1 } + a _ { n - k } \quad { \mathrm { f o r ~ } } k = 1 , \dots , n ,
$$

where $P _ { 0 } = a _ { n }$ , and the final step gives the value of the polynomial: $p ( t ) = P _ { n }$ . The additions and multiplications are performed in floating–point arithmetic, but for simplicity we assume $a _ { n } , \ldots , a _ { 0 }$ and $t$ are $a$ priori allowable floating– point values (i.e., there is no floating–point conversion error on input).

Now let $e _ { r }$ be a bound on the absolute error in the $r$ –th computed Horner term, i.e., this computed value equals $P _ { r } + \varDelta P _ { r }$ with $- e _ { r } \le \varDelta P _ { r } \le + e _ { r }$ . We can obtain a recursion relation for the error bounds $e _ { 0 } , e _ { 1 } , \ldots , e _ { n }$ as follows. The outcome of the $k$ –th floating–point Horner step will be

$$
[ t \times ( P _ { k - 1 } + \varDelta P _ { k - 1 } ) ( 1 + \delta ) + a _ { n - k } ] ( 1 + \epsilon ) ,
$$

where $\delta$ and $\epsilon$ are the relative errors (no greater in magnitude than $\eta$ ) arising in the floating–point multiplication and addition that constitute step $k$ . To first order in small quantities, the deviation of the computed value (12.7) from the exact one (12.6) is thus

$$
\Delta P _ { k } = t \Delta P _ { k - 1 } + t P _ { k - 1 } \delta + \left( t P _ { k - 1 } + a _ { n - k } \right) \epsilon .
$$

Noting that the term in parentheses on the right–hand side is just the (exact) $k$ –th Horner sum $P _ { k }$ , and that $- e _ { k - 1 } \leq \Delta P _ { k - 1 } \leq + e _ { k - 1 }$ and $- \eta \le \delta , \epsilon \le + \eta$ , the bound on the absolute value of the above error in $P _ { k }$ is

$$
e _ { k } = | t | e _ { k - 1 } + \left( | t | | P _ { k - 1 } | + | P _ { k } | \right) \eta .
$$

By running the recursion (12.8) starting with $e _ { 0 } = 0$ , it would seem that we can determine a rigorous bound on the error $e _ { n }$ in the value $P _ { n }$ of $p ( t )$ , as computed by the Horner method (12.6). Such an approach, which attempts to estimate and propagate the errors incurred in each arithmetic operation of a calculation, is usually called forward error analysis. Despite its simplicity and intuitive appeal, forward error analysis embodies a basic flaw that can make it seriously underestimate the significance of arithmetic errors under certain circumstances. To understand the nature of this flaw, we must consider more carefully what we mean by the “error” in a computed value.

# 12.3.3 Dangers of Digit Cancellation

Basically, equation (12.4) says that the relative error incurred in each floating– point operation is bounded by a very small quantity $\eta$ . However, caution must be urged in imputing a “practical” significance to this statement, since we have not yet given a precise meaning to the term relative error.

It is implicit in equation (12.4) that the two operands $x$ and $y$ are numbers that have ab initio exact floating–point representations. But this is hardly ever true! In practice, $x$ and $y$ usually represent approximations to arbitrary real numbers $X$ and $Y$ . At minimum, the approximate nature of $x$ and $y$ arises from the need to round $X$ and $Y$ on input (if $x$ and $y$ denote intermediate values in some calculation, they will often incorporate significantly larger accumulated round–off errors, compared to the exact values $X$ and $Y$ ). For simplicity, we consider only the case where $X$ and $Y$ are input values, so that $x$ and $y$ suffer only initial round–off errors characterized by

$$
\begin{array} { r } { \left( 1 - \eta \right) X \leq x = \mathrm { f o a t } ( X ) \leq \left( 1 + \eta \right) X , } \\ { \left( 1 - \eta \right) Y \leq y = \mathrm { f o a t } ( Y ) \leq \left( 1 + \eta \right) Y . } \end{array}
$$

In practice, of course, the error of interest incurred by the floating–point arithmetic operation $\mathrm { H o a t } ( x * y )$ is not that expressed by equation (12.4), but instead the error relative to an exact–arithmetic operation on the underlying real numbers, $X$ and $Y$ , that the floating–point numbers $x$ and y approximate — i.e., it is the quantity

$$
{ \mathrm { r e l a t i v e ~ e r r o r } } = { \frac { \left| \mathrm { H o a t } ( x * y ) - X * Y \right| } { \left| X * Y \right| } } .
$$

In most cases the quantity (12.10) is, in agreement with intuition, no more than a few times $\eta$ , and the model (12.4) thus provides a fairly reliable basis for analyzing error propagation and estimating the deviation of floating–point calculations from exact–arithmetic results — as in the discussion of Horner’s method. However, there are situations in which (12.10) can exceed $\eta$ by many orders of magnitude, and the model (12.4) fails dramatically in monitoring the true discrepancy between floating–point and exact–arithmetic results. These cases correspond to subtraction of like–signed floating–point numbers $x$ and $y$ that have identical exponents and agree in many leading digits of the mantissas (or, equivalently, the addition of such quantities of unlike sign).

In such situations, cancellation of the identical leading digits of $x$ and $y$ occurs, and hence the quantity $x * y$ actually needs no rounding for machine representation: $\operatorname { f l o a t } ( x * y ) \equiv x * y$ . The problem is thus not one of arithmetic error in the subtraction, but rather a magnification of “pre–existing” errors incurred in the floating–point conversions $x = \operatorname { f l o a t } ( X )$ and $y = \operatorname { f l o a t } ( Y )$ . To illustrate this, we use (12.9) to write

$$
x = ( 1 + \delta ) X \quad \mathrm { a n d } \quad y = ( 1 + \epsilon ) Y ,
$$

where $\delta$ and $\epsilon$ are random numbers with $- \eta \le \delta , \epsilon \le + \eta$ . We further suppose that $X$ , $Y$ are of like sign and agree in $r \geq 1$ of their leading binary digits. Noting again that floa $\operatorname { t } ( x * y ) \equiv x * y$ in such a case, expression (12.10) becomes

$$
{ \mathrm { r e l a t i v e ~ e r r o r } } = { \frac { | ( 1 + \delta ) X - ( 1 + \epsilon ) Y - ( X - Y ) | } { | X - Y | } } = { \frac { | \delta X - \epsilon Y | } { | X - Y | } } .
$$

Now the numerator of the right–hand side attains its largest value, namely

$$
\left| \delta { \cal X } - \epsilon { \cal Y } \right| = \eta \left( \left| { \cal X } \right| + \left| { \cal Y } \right| \right) ,
$$

when $\delta$ and $\epsilon$ both have absolute value $\eta$ but unlike signs, and if $X$ and $Y$ have mantissas that agree in $r$ leading bits, we have

$$
\left| X \right| + \left| Y \right| \approx 2 \left| X \right| ,
$$

and typically

$$
\left| X - Y \right| \approx 2 ^ { - r } \left| X \right|
$$

(although $\left| X - Y \right|$ may actually be much smaller). Thus the magnitude of the error, relative to exact arithmetic, is approximately

$$
\mathrm { r e l a t i v e ~ e r r o r } \approx 2 ^ { r + 1 } \eta .
$$

This error evidently becomes arbitrarily large as $r  \infty$ (note that $r$ is the number of identical bits in the real numbers $X$ and $Y$ — it is not bounded by $d$ , the number of mantissa bits in the floating–point number system).

We emphasize again the nature of the phenomenon that gives rise to the error (12.11): it is not at all an “arithmetic error” but rather a magnification of the small relative errors incurred by the conversions $^ 5$ $x = \operatorname { f l o a t } ( X )$ and $y = \operatorname { f l o a t } ( Y )$ that arises when $| X - Y | \ll | X | , | Y |$ . A simple example serves to illustrate this point: consider the addition of the two numbers, $X = 0 . 2 7 5 3 4 7$ and $Y = - 0 . 2 7 5 1 6 2$ , in 4–digit decimal floating–point arithmetic. In exact arithmetic we obtain

$$
\begin{array} { r } { X = + 0 . 2 7 5 3 4 7 } \\ { Y = - 0 . 2 7 5 1 6 2 } \\ { X + Y = + 0 . 0 0 0 1 8 5 , } \end{array}
$$

whereas converting first to floating–point by rounding gives $x = \operatorname { f l o a t } ( X ) =$ 0.2753 and $y = \operatorname { f l o a t } ( Y ) = - 0 . 2 7 5 2$ , and hence

$$
\begin{array} { r } { x = + 0 . 2 7 5 3 } \\ { y = - 0 . 2 7 5 2 } \\ { \mathrm { f l o a t } ( x + y ) = + 0 . 0 0 0 1 . } \end{array}
$$

Note that no rounding was necessary in the above floating–point calculation. However, the fractional error — relative to the exact–arithmetic result — is

$$
\mathrm { r e l a t i v e ~ e r r o r } = { \frac { | 0 . 0 0 0 1 - 0 . 0 0 0 1 8 5 | } { | 0 . 0 0 0 1 8 5 | } } \approx 0 . 4 6 .
$$

But the machine unit for 4–digit decimal floating–point is just $\begin{array} { r l r } { \frac 1 2 \times 1 0 ^ { - ( 4 - 1 ) } = } \end{array}$ $5 \times 1 0 ^ { - 4 }$ , and thus the above error exceeds $\eta$ by about 3 orders of magnitude!

# 12.3.4 Models for Error Propagation

We may summarize the preceding discussion as follows. In the absence of digit cancellation effects, the accumulation of arithmetic errors in the execution of an algorithm — as compared to exact–arithmetic results — is reasonably well described by the formula (12.5), which indicates rather small relative errors in each step, and consequently fairly mild final errors in all but very lengthy calculations. When cancellations occur, however, the “forward error analysis” model based on (12.5) fails dramatically to provide a reliable indication of the deviation from exact–arithmetic results, and cannot be easily amended to do so. In such cases, the errors that arise are not actually arithmetic errors, but rather magnifications of pre–existing errors in the operands.

The potential for large relative errors to arise through cancellation effects — as expressed by the factor $2 ^ { r + 1 }$ in equation (12.11) — seriously complicates the task of formulating systematic floating–point error propagation models. The amount of error amplification in each subtraction depends on the precise number of digits $r$ that cancel in the operands. If the latter are intermediate values in a rather lengthy calculation, $r$ would be virtually impossible to know other than through a tedious step–by–step examination of numerical values — which is clearly impractical for all but the most trivial calculations.

There is a systematic (though rather subtle) approach to floating–point error analysis that accommodates cancellation effects and avoids the tedium of a case–by–case inspection for each set of input parameters. Developed by the pioneering British numerical analyst James H. Wilkinson (1919–1986), this approach is based on computing a condition number for the given problem, coupled with a backward error analysis of it.

Instead of attempting to monitor the discrepancies between “exact” and “computed” results in a floating–point calculation, Wilkinson’s method has a radically different philosophy — it aims to show that the outcome of a finite– precision calculation on given input values is identical to what is obtained in an exact–arithmetic calculation, but with “perturbed” input values. Assessing the accuracy of floating–point calculations is then a two–stage process:

1. compute a condition number $C$ for the given problem, which characterizes the sensitivity of the output values to perturbations in the input values;   
2. perform a backward error analysis so as to determine the magnitude $\epsilon$ of the input perturbations that, in exact arithmetic, would be equivalent to the cumulative effects of round–off error during the calculation.

The product $C \epsilon$ of the condition number and “effective” input perturbations is then a measure of the floating–point error in the computed solution. These concepts will be explained in greater detail below. Although the backward error analysis method is quite general, it can become unwieldy in practice if the algorithm is not relatively simple. Quite often, just being able to compute (or estimate) the condition number gives a sufficient indication of whether or not the results of a calculation can be regarded as trustworthy.

An alternative approach to monitoring the propagation of rounding errors or other uncertainties during a calculation is by the use of interval arithmetic (see §2.4). Each variable is considered to identify a range of possible values, between specified lower and upper limits, and each value within this range is regarded equally likely as the value of the variable — there is no information on the relative probabilities of values within the specified range. If the arithmetic operations required to determine the lower and upper bounds of the resulting intervals on the right–hand side of expressions (2.10) are to be performed in floating point, it is possible to automatically adjust them to allow for the effect of round–off errors: this approach is known as “rounded” interval arithmetic. For a more detailed treatment of this topic, see [16, 226, 332, 333].

The interval widths need not necessarily reflect only round–off errors: they may also reflect inherent “physical” uncertainties associated with the variables — for example, interval arithmetic can be used to analyze the accumulation of tolerances in a mechanical assembly whose component parts have dimensional uncertainties due to manufacturing variations. Many familiar algorithms can be reformulated to accept interval operands — see, for example, [227, 228]. The use of interval arithmetic in the context of geometric modeling has been discussed in [286,338,402]. It should be noted, however, that “mindless” use of interval arithmetic can yield very pessimistic results — i.e., the interval width grows very large, whereas the true value is, with high probability, localized in a much narrower subset of the nominal interval.

# 12.4 Stability and Condition Numbers

Conceptually, we may regard a mathematical problem $\mathcal { P }$ as receiving certain numerical values as its “input” and yielding other values as its “output” or solution — we assume the output to be an analytic function of the input, even if we cannot in general express that function in closed form. We say that $\mathcal { P }$ is a stable or “well–conditioned” problem if input values that differ only slightly always define solutions that differ only slightly. If, on the other hand, input values that differ only slightly can incur dramatically different solutions, we say that $\mathcal { P }$ is an unstable or “ill–conditioned” problem. Figure 12.2 gives a schematic illustration of this concept, which may be quantified by introducing suitable metrics for the sets of input values and solutions.

![](images/57cf923c15bf8f6414486829fe9c65890461a8ce91f2a5c0cc33a0c2ce48f872.jpg)  
Fig. 12.2. The “distance” between solutions for two neighboring sets of input values distinguishes a well–conditioned problem (left) from an ill–conditioned one (right).

The condition number $C ( \mathcal { P } )$ of the problem $\mathcal { P }$ is a quantitative measure of the sensitivity of its output to changes in its input. We are speaking here of the intrinsic stability of the input–output relationship for the specified problem $\mathcal { P }$ . We make no reference to any particular algorithm or computational scheme whereby solutions are actually determined. The condition number $C ( \mathcal { P } )$ is an intrinsic property of the problem $\mathcal { P }$ , independent of any solution method.

The typical approach to formulating a condition number $\mathcal { C } ( \mathcal { P } )$ is as follows. We imagine that the input parameters to $\mathcal { P }$ suffer random perturbations, of maximum relative magnitude $\epsilon$ , about their nominal values. Corresponding perturbations of the output values will then be induced, and we require the condition number to be such that the greatest of these output perturbations is bounded by the quantity $C ( \mathcal { P } ) \epsilon$ . Thus “well–conditioned” problems have condition numbers of order unity (i.e., the input and output perturbations are comparable) while “ill–conditioned” problems will have very large condition numbers. Although we have not yet discussed backward error analysis, it will be intuitively clear that high–accuracy solutions to ill–conditioned problems are extremely difficult to compute using floating–point arithmetic.

The study of condition numbers can be useful in identifying more–stable problem formulations, and thereby obtaining more–accurate computed results. We now examine in greater detail some condition number formulations for two important problems: univariate polynomials and linear maps (i.e., matrices). The condition numbers for polynomial values and roots used below are based upon the formulations of Gautschi [209, 210]. For linear maps, the condition numbers are based on standard vector and matrix norms: see 12.4.4.

# 12.4.1 Condition of a Polynomial Value

Consider the representation

$$
p ( t ) = \sum _ { k = 0 } ^ { n } c _ { k } \phi _ { k } ( t )
$$

of a degree– $_ n$ polynomial $p ( t )$ by its coefficients $c _ { 0 } , \ldots , c _ { n }$ in a specified basis $\phi _ { 0 } ( t ) , \ldots , \phi _ { n } ( t )$ . Suppose we are interested in evaluating $p ( t )$ , but we do not know its coefficients $c _ { 0 } , \ldots , c _ { n }$ precisely. Specifically, suppose that $c _ { k }$ is in error by $\delta c _ { k }$ for each $k$ . Then the nominal value $p ( t )$ is perturbed to

$$
p ( t ) + \delta p ( t ) = \sum _ { k = 0 } ^ { n } c _ { k } \phi _ { k } ( t ) + \sum _ { k = 0 } ^ { n } \delta c _ { k } \phi _ { k } ( t ) .
$$

If the coefficient errors are assumed to be random and of a uniform relative magnitude $\epsilon$ , so that

$$
- \epsilon \leq \delta c _ { k } / c _ { k } \leq + \epsilon
$$

for $k = 0 , \ldots , n$ the perturbation $\delta p$ in $p$ evidently lies in the range

$$
- \sum _ { k = 0 } ^ { n } | \delta c _ { k } \phi _ { k } ( t ) | \ \leq \ \delta p ( t ) \ \leq \ + \sum _ { k = 0 } ^ { n } | \delta c _ { k } \phi _ { k } ( t ) | ,
$$

and using (12.13) we may write

$$
| \delta p ( t ) | \le C _ { \phi } ( p ( t ) ) \epsilon \quad \mathrm { w h e r e } \quad C _ { \phi } ( p ( t ) ) = \sum _ { k = 0 } ^ { n } | c _ { k } \phi _ { k } ( t ) | .
$$

We call $C _ { \phi } ( p ( t ) )$ the condition number for the value of $p ( t )$ with respect to its coefficients in the basis $\phi _ { 0 } ( t ) , \ldots , \phi _ { n } ( t )$ . We append the subscript $\phi$ to this condition number to emphasize that it depends on the choice of basis, as well as on the polynomial $p ( t )$ itself. Note that we make no assumption concerning the size of the fractional coefficient error $\epsilon$ in deducing the bound (12.15). Thus, the perturbation in the value of $p ( t )$ satisfies this bound for finite (not just infinitesimal) relative errors in the coefficients. We now compare condition numbers for the value of a polynomial in different bases.

Definition 12.1 A basis $\phi _ { 0 } ( t ) , \ldots , \phi _ { n } ( t )$ for polynomials of degree $n$ is said to be non–negative on the interval $t \in [ a , b ]$ if

$$
\phi _ { k } ( t ) \geq 0 \quad { \mathrm { f o r ~ a l l ~ } } t \in [ a , b ] \quad { \mathrm { a n d ~ } } k = 0 , \ldots , n .
$$

Non–negative polynomial bases are of interest in the following context [181].

Theorem 12.1 Let $\psi _ { 0 } ( t ) , \ldots , \psi _ { n } ( t )$ and $\phi _ { 0 } ( t ) , \ldots , \phi _ { n } ( t )$ be two non–negative bases for polynomials of degree $_ { n }$ on the interval $t \in [ a , b ]$ , such that the former can be expressed as a non–negative combination of the latter, i.e.,

$$
\psi _ { j } ( t ) = \sum _ { k = 0 } ^ { n } M _ { j k } \phi _ { k } ( t ) , \quad j = 0 , \ldots , n ,
$$

$$
\mathrm { w h e r e } \quad M _ { j k } \geq 0 \quad \mathrm { f o r ~ } 0 \leq j , k \leq n .
$$

Then the condition number for the value of any degree– $_ { \mathbf { \Omega } ^ { \prime } } \mathbf { \Omega } _ { \mathbf { \Omega } ^ { \prime } }$ polynomial $p ( t )$ at any point $t \in [ a , b ]$ in these bases satisfies the inequality

$$
C _ { \phi } ( p ( t ) ) \leq C _ { \psi } ( p ( t ) ) .
$$

Proof : Let $p ( t )$ have coefficients $a _ { 0 } , \ldots , a _ { n }$ in the basis $\psi _ { 0 } ( t ) , \ldots , \psi _ { n } ( t )$ :

$$
p ( t ) = \sum _ { j = 0 } ^ { n } a _ { j } \psi _ { j } ( t ) .
$$

On substituting (12.17) into (12.20), we see that the coefficients $c _ { 0 } , \ldots , c _ { n }$ of $p ( t )$ in the basis $\phi _ { 0 } ( t ) , \ldots , \phi _ { n } ( t )$ are given by

$$
c _ { k } = \sum _ { j = 0 } ^ { n } a _ { j } M _ { j k } \quad { \mathrm { f o r ~ } } k = 0 , \dots , n .
$$

Since the bases $\psi _ { 0 } ( t ) , \ldots , \psi _ { n } ( t )$ and $\phi _ { 0 } ( t ) , \ldots , \phi _ { n } ( t )$ are both non–negative on $t \in [ a , b ]$ , the condition numbers for the value of $p ( t )$ may be written as

$$
C _ { \phi } ( p ( t ) ) = \sum _ { k = 0 } ^ { n } | c _ { k } | \phi _ { k } ( t ) \quad \mathrm { a n d } \quad C _ { \psi } ( p ( t ) ) = \sum _ { j = 0 } ^ { n } | a _ { j } | \psi _ { j } ( t ) .
$$

We now substitute (12.21) into $C _ { \phi } ( p ( t ) )$ and use the triangle inequality

$$
\left| \sum _ { k = 0 } ^ { n } x _ { k } \right| \ \leq \ \sum _ { k = 0 } ^ { n } \left| x _ { k } \right|
$$

for any sequence $x _ { 0 } , \ldots , x _ { n }$ of real values, to obtain

$$
C _ { \phi } ( p ( t ) ) = \sum _ { k = 0 } ^ { n } \left| \sum _ { j = 0 } ^ { n } a _ { j } M _ { j k } \right| \phi _ { k } ( t ) \leq \sum _ { k = 0 } ^ { n } \left[ \sum _ { j = 0 } ^ { n } | a _ { j } M _ { j k } | \right] \phi _ { k } ( t ) .
$$

Thus, setting $| a _ { j } M _ { j k } | = | a _ { j } | M _ { j k }$ (since $M _ { j k } \ge 0$ for all $j , k$ ) and re–arranging the order of summation on the right–hand side of (12.24) we have

$$
C _ { \phi } ( p ( t ) ) \le \sum _ { j = 0 } ^ { n } | a _ { j } | \sum _ { k = 0 } ^ { n } M _ { j k } \phi _ { k } ( t ) = \sum _ { j = 0 } ^ { n } | a _ { j } | \psi _ { j } ( t ) = C _ { \psi } ( p ( t ) ) ,
$$

where we make use of (12.17) in the second step.

We emphasize again the general nature of the inequality (12.19) — it holds for every polynomial $p ( t )$ and for each value $t \in [ a , b ]$ if the non–negative bases $\phi _ { 0 } ( t ) , \ldots , \phi _ { n } ( t )$ and $\psi _ { 0 } ( t ) , \ldots , \psi _ { n } ( t )$ satisfy (12.17) and (12.18). The former basis then offers as a systematically more stable representation for evaluating polynomials at points $t \in [ a , b ]$ than the latter basis.

A trivial instance in which the relation (12.19) holds with equality is if we simply scale the basis functions, i.e., we set

$$
\psi _ { k } ( t ) = \lambda _ { k } \phi _ { k } ( t ) \quad \mathrm { f o r } \ k = 0 , \ldots , n ,
$$

where $\lambda _ { 0 } , \ldots , \lambda _ { n }$ are any (non–zero) constants. It is not difficult to see in this case that $C _ { \psi } ( p ( t ) ) \equiv C _ { \phi } ( p ( t ) )$ , i.e., the condition number for the value of $p ( t )$ is independent of the scaling of the basis functions. A non–trivial example is a comparison of the Bernstein basis

$$
b _ { k } ^ { n } ( t ) = { \binom { n } { k } } ( 1 - t ) ^ { n - k } t ^ { k } \quad { \mathrm { f o r ~ } } k = 0 , \dots , n ,
$$

on which the B´ezier curve and surface forms are based (see Chap. 13) with the monomial basis $1 , t , \ldots , t ^ { n }$ . Since the polynomials (12.26) are non–negative for $t \in [ 0 , 1 ]$ and the monomials are the non–negative combinations

$$
t ^ { j } = \sum _ { k = j } ^ { n } { \frac { \binom { k } { j } } { \binom { n } { j } } } b _ { k } ^ { n } ( t ) \quad { \mathrm { f o r ~ } } j = 0 , \dots , n
$$

of them [181], the Bernstein representation

$$
p ( t ) = \sum _ { k = 0 } ^ { n } c _ { k } b _ { k } ^ { n } ( t )
$$

of a polynomial is systematically more stable on the interval $t \in [ 0 , 1 ]$ than the “power” form (3.1). On the other hand, we note from the expression

$$
b _ { j } ^ { n } ( t ) = \sum _ { k = j } ^ { n } ( - 1 ) ^ { k - j } { \binom { n } { k } } { \binom { k } { j } } t ^ { k } \quad { \mathrm { f o r ~ } } j = 0 , \dots , n
$$

for the Bernstein basis in terms of the monomial basis [181] that the former are not non–negative combinations of the latter.

In fact, it can be shown [161] that the Bernstein basis is “optimally stable” in the sense of Theorem 12.1 — it is impossible to construct a non–negative basis for degree– $_ n$ polynomials on $t \in [ 0 , 1 ]$ , in terms of which the Bernstein basis can be expressed as a non–negative combination,6 so that this basis will yield systematically smaller condition numbers than the Bernstein form.

The transformation between two degree– $\boldsymbol { n }$ polynomial bases by means of a non–negative matrix establishes a partial ordering among the set of such bases that are non–negative over any specified interval, and the Bernstein basis is a minimal element of this partially–ordered set. No other commonly–used basis is known to have this property — see [161] for more complete details.

# 12.4.2 Condition of a Polynomial Root

We discussed above the stability of the value of a polynomial, with respect to perturbations of its coefficients. Many problems concerning curve and surface intersections, ray tracing of surfaces, etc., can be reduced to computing roots of polynomials, so we are also interested in analyzing their stability. Clearly, these problems are related, since a root is a point $t$ where the value is zero.

Suppose $\tau$ is a simple real root of the polynomial $p ( t )$ , i.e., $p ( \tau ) = 0 \neq p ^ { \prime } ( \tau )$ . We are interested in characterizing the sensitivity of $\tau$ to perturbations of the coefficients $c _ { 0 } , \ldots , c _ { n }$ of $p ( t )$ in the basis $\phi _ { 0 } ( t ) , \ldots , \phi _ { n } ( t )$ . We consider first an infinitesimal perturbation $\delta c _ { r }$ in the coefficient $c _ { r }$ only, and suppose that the root $\tau$ is displaced to $\tau + \delta \tau$ when $p ( t )$ is perturbed to $p ( t ) + \delta c _ { r } \phi _ { r } ( t )$ . Then we must have

$$
p ( \tau + \delta \tau ) + \delta c _ { r } \phi _ { r } ( \tau + \delta \tau ) = 0 .
$$

Moving the second term to the right and expanding both sides in Taylor series gives

$$
\sum _ { k = 1 } ^ { n } \frac { p ^ { ( k ) } ( \tau ) } { k ! } ( \delta \tau ) ^ { k } = - \delta c _ { r } \sum _ { k = 0 } ^ { n } \frac { \phi _ { r } ^ { ( k ) } ( \tau ) } { k ! } ( \delta \tau ) ^ { k } .
$$

Note that there is no constant term on the left, since $p ( \tau ) = 0$ , and the Taylor series are finite because $p ( t )$ is just a polynomial.

Keeping only first–order terms in infinitesimal quantities, we find that

$$
\operatorname * { l i m } _ { \delta c _ { r } \to 0 } \frac { \delta \tau } { \delta c _ { r } / c _ { r } } = - \frac { c _ { r } \phi _ { r } ( \tau ) } { p ^ { \prime } ( \tau ) } .
$$

This expresses the sensitivity of $\tau$ to a perturbation in the coefficient $c _ { r }$ only. If we now imagine every coefficient to be subject to a random (infinitesimal) perturbation of maximum relative magnitude $\epsilon$ ,

$$
| \delta c _ { k } / c _ { k } | \le \epsilon \quad \mathrm { f o r } \ k = 0 , \dots , n ,
$$

the greatest overall root perturbation $\delta \tau$ will be achieved when $| \delta c _ { k } | = \epsilon | c _ { k } |$ for each $k$ , and the signs of the $\delta c _ { k }$ ’s are such as to make their contributions on the right–hand side of (12.31) add up in the same sense.

Thus, we deduce that the simple root $\tau$ of $p ( t )$ will suffer a perturbation $\delta \tau$ satisfying the bound

$$
| \delta \tau | \le C _ { \phi } ( \tau ) \epsilon \mathrm { ~ w h e r e ~ } C _ { \phi } ( \tau ) = \frac { 1 } { | p ^ { \prime } ( \tau ) | } \sum _ { k = 0 } ^ { n } | c _ { k } \phi _ { k } ( \tau ) |
$$

when the coefficients $c _ { 0 } , \ldots , c _ { n }$ of $p ( t )$ in the basis $\phi _ { 0 } ( t ) , \ldots , \phi _ { n } ( t )$ are subject to random infinitesimal errors of maximum relative magnitude $\epsilon$ . We call the quantity $C _ { \phi } ( \tau )$ a root condition number for the polynomial $p ( t )$ .

Note that although $C _ { \phi } ( \tau )$ differs from $C _ { \phi } ( p ( \tau ) )$ by only the factor $1 / | p ^ { \prime } ( \tau ) |$ , the interpretation of the root condition number is rather different from that for the polynomial value. While (12.15) expresses a sharp bound on the change in the polynomial value for arbitrary coefficient perturbations, the bound (12.33) on the root displacement is valid only for infinitesimal perturbations: it is only by restricting to infinitesimal perturbations that we can omit the higher–order terms in $( 1 2 . 3 0 )$ and thus proceed to equation (12.31) and hence (12.33).

Since the factor $| p ^ { \prime } ( \tau ) |$ in $C _ { \phi } ( \tau )$ is evidently independent of the basis that we choose for the polynomial $p ( t )$ , the inequality of Theorem 12.1 with respect to condition numbers for the polynomial value in different non–negative bases applies equally to the root condition numbers. For example, if we are interested in the roots of a polynomial $p ( t )$ on $t \in [ 0 , 1 ]$ , the Bernstein form is always a better–conditioned representation for computing them than the power form.

The root condition number (12.33) is formally infinite if $p ^ { \prime } ( \tau ) = 0$ — i.e., when $\tau$ is a multiple root. This indicates that $| \delta \tau |$ actually has a faster than linear growth with $\epsilon$ . In order to characterize the dependence of $\delta \tau$ on $\epsilon$ in such instances, we return to equation (12.30) and retain only the lowest–order non–vanishing term on the left–hand side. We thus find, at an $m$ –fold root $\tau$ such that $p ( \tau ) = p ^ { \prime } ( \tau ) = \cdot \cdot \cdot = p ^ { ( m - 1 ) } ( \tau ) = 0 \neq p ^ { ( m ) } ( \tau )$ , that

$$
| \delta \tau | \le C _ { \phi } ^ { m } ( \tau ) \epsilon ^ { 1 / m } \quad \mathrm { w i t h } \quad C _ { \phi } ^ { m } ( \tau ) = \Bigg [ \frac { m ! } { | p ^ { ( m ) } ( \tau ) | } \sum _ { k = 0 } ^ { n } | c _ { k } \phi _ { k } ( \tau ) | \Bigg ] ^ { 1 / m } .
$$

We may interpret $C _ { \phi } ^ { m } ( \tau )$ as a condition number for the $m$ –fold root $\tau$ of $p ( t )$ in the basis $\phi _ { 0 } ( t ) , \ldots , \phi _ { n } ( t )$ . Again, the above bound holds only in the limit $\epsilon  0$ — note that $\epsilon ^ { 1 / m } \gg \epsilon$ when $\epsilon \ll 1$ .

# 12.4.3 Wilkinson’s Polynomial

An (in)famous polynomial, first investigated by Wilkinson [468] in 1959, offers a vivid illustration of these ideas. In the course of testing newly–implemented software for floating–point arithmetic (only fixed–point arithmetic processors were available at that time), Wilkinson attempted to compute the roots of a degree 20 polynomial. Specifically, he chose a polynomial with 20 equidistant real roots,

$$
p ( t ) = \prod _ { k = 1 } ^ { n } \left( t - k / n \right) , \quad n = 2 0 ,
$$

so as not to encounter numerical difficulties (or so he thought) on account of closely–spaced or near–multiple roots.7 Wilkinson’s approach was to multiply out expression (12.35), so as to determine the power coefficients $a _ { 0 } , \ldots , a _ { n }$ in the representation (3.1), and to use this representation in evaluating $p ( t )$ and its derivative for Newton–Raphson iterations. He discovered, in fact, that he could find few of the roots of (12.35) to more than just a few accurate digits — if at all — and was at first convinced that his software implementation of floating–point arithmetic must be plagued by bugs.

It was only on verifying this was not the case that he discovered the true source of the problem, namely, the severe ill–conditioning of the roots of $p ( t )$ with respect to its power coefficients $a _ { 0 } , \ldots , a _ { n }$ . He subsequently called this “the most traumatic experience in my career as a numerical analyst” [470].

We begin to understand why the roots of $p ( t )$ are so difficult to determine in floating–point arithmetic when we compute their condition numbers in the power basis, as given by expression (12.33). Table 12.1 lists these condition numbers, which are found to be greater than $1 0 ^ { 1 3 }$ in some instances. In other words, a minuscule coefficient perturbation of merely 1 part in $1 0 ^ { 1 3 }$ may induce displacements of order unity in the roots! Perturbations of this magnitude might certainly be expected in computing the power coefficients $a _ { 0 } , \ldots , a _ { 2 0 }$ of $p ( t )$ by multiplying out (12.35) in floating–point arithmetic.

Table 12.1. Root condition numbers for Wilkinson’s polynomial.   

<table><tr><td>root</td><td>condition number in power basis</td><td>condition number in Bernstein basis</td></tr><tr><td>0.05</td><td>2.10×101</td><td>3.41×100</td></tr><tr><td>0.10</td><td>4.39 × 103</td><td>1.45 ×10²</td></tr><tr><td>0.15</td><td>3.03 × 105</td><td>2.34 × 10³</td></tr><tr><td>0.20</td><td>1.03 × 107</td><td>2.03×104</td></tr><tr><td>0.25</td><td>2.06×108</td><td>1.11 × 105</td></tr><tr><td>0.30</td><td>2.68×109</td><td>4.15 ×105</td></tr><tr><td>0.35</td><td>2.41×1010</td><td>1.12 ×106</td></tr><tr><td>0.40</td><td>1.57 × 1011</td><td>2.22 ×106</td></tr><tr><td>0.45</td><td>7.57 × 1011</td><td>3.32 × 106</td></tr><tr><td>0.50</td><td>2.78 × 1012</td><td>3.80 ×106</td></tr><tr><td>0.55</td><td>7.82 × 1012</td><td>3.32 × 106</td></tr><tr><td>0.60</td><td>1.71 × 1013</td><td>2.22 × 106</td></tr><tr><td>0.65</td><td>2.89 ×1013</td><td>1.12 × 106</td></tr><tr><td>0.70</td><td>3.78 × 1013</td><td>4.15 ×105</td></tr><tr><td>0.75</td><td>3.78 ×1013</td><td>1.11 × 105</td></tr><tr><td>0.80</td><td>2.83 ×1013</td><td>2.03 ×104</td></tr><tr><td>0.85</td><td>1.54 ×1013</td><td>2.34×10</td></tr><tr><td>0.90</td><td>5.74 ×1012</td><td>1.45 ×10²</td></tr><tr><td>0.95</td><td>1.31 × 1012</td><td>3.41 × 100</td></tr><tr><td>1.00</td><td>1.38 × 1011</td><td>0.00 ×10°</td></tr></table>

How do such enormous root condition numbers arise? The answer lies in that dreaded blight of all finite–precision calculations, discussed in 12.3.3 — namely, the problem of error amplification through digit cancellation. Suppose we try computing the value of $p ( t )$ at the point $t = 0 . 5 2 5$ , say, by enumerating the values of its 21 constituent terms $a _ { k } t ^ { k }$ in the power form at that point (we choose a point between two roots since that value at a root is, of course, zero). The contributions of these terms, accurate to the number of digits shown, are found to be as follows:

<table><tr><td></td><td>ag t9 = -0.150051459849195639 α1o t10 = +0.203117060946715796</td></tr><tr><td>a11tl1</td><td>= -0.221153902712311843</td></tr><tr><td></td><td></td></tr><tr><td>a13 t13</td><td>= -0.135971108107894016</td></tr><tr><td>a14t14</td><td>= +0.075852737479877575</td></tr><tr><td>a15t15</td><td>= -0.033154980855819210</td></tr><tr><td></td><td>+0.011101552789116296</td></tr><tr><td>α16t16</td><td></td></tr><tr><td>a17t17</td><td>= -0.002747271750190952</td></tr><tr><td>a18t18</td><td>= +0.000473141245866219</td></tr><tr><td>a19t19</td><td>= -0.000050607637503518</td></tr><tr><td>20</td><td></td></tr><tr><td>a20</td><td>= +0.000002530381875176</td></tr><tr><td></td><td>p(t）= 0.000000000000003899</td></tr></table>

The actual value of $p ( t )$ , halfway between two consecutive roots, is seen to be just a tiny residual left over when relatively large terms of alternating sign are summed up. In fact, this value is ${ \sim } 1 3$ orders of magnitude smaller than the largest of the individual terms $a _ { k } t ^ { k }$ . A perturbation of just a single coefficient coefficient $a _ { k }$ may thus be amplified as much as $1 0 ^ { 1 3 }$ times in the value of $p ( t ) !$ Since the roots are just the points at which the polynomial value vanishes, they suffer commensurate errors.

This example shows that error amplification due to cancellation need not be confined to individual arithmetic operations, as in the example of 12.3.3 — although no two consecutive terms in (12.36) have many digits in common, the relative accuracy of the final value is still extremely susceptible to individual arithmetic errors or small perturbations in the coefficients $a _ { 0 } , \ldots , a _ { 2 0 }$ .

We have observed that the Bernstein basis on $t \in [ 0 , 1 ]$ is systematically better–conditioned than the power basis about $t = 0$ . Table 12.1 compares the Bernstein–basis root condition numbers for (12.35) with the power–basis condition numbers — we see that, for the most unstable roots, they are about 7 orders of magnitude smaller. This means that, when using the Bernstein form (12.28), we can expect to compute the roots with about seven more digits of accuracy than when using then power form (assuming that the coefficients of both forms have relative errors of similar magnitudes).

This is dramatically illustrated in Table 12.2, where we show the result of a fractional perturbation $\epsilon \approx 5 \times 1 0 ^ { - 1 0 }$ in the coefficients $a _ { 1 9 }$ and $c _ { 1 9 }$ of the power and Bernstein forms. The values shown are correct to the given number of digits — they indicate the intrinsic sensitivity of the roots to perturbations in $a _ { 1 9 }$ or $c _ { 1 9 }$ , rather than the effects of arithmetic or approximation errors in a numerical root–finding procedure. Whereas all the roots of the perturbed Bernstein form exhibit at least 8 accurate digits, many roots of the perturbed power form have $_ { n o }$ accurate digits at all — they become complex conjugate pairs! This provides an excellent illustration of the fact that the formulation of a problem can often exert a profound influence on the accuracy with which we can hope to compute the solutions of that problem.

Table 12.2. Perturbed roots of Wilkinson’s polynomial.   

<table><tr><td>exact</td><td>perturbed root</td><td>perturbed root</td></tr><tr><td>root</td><td>(power basis)</td><td>(Bernstein basis) 0.0500000000</td></tr><tr><td>0.05 0.10</td><td>0.05000000</td><td>0.1000000000</td></tr><tr><td>0.15</td><td>0.10000000 0.15000000</td><td>0.1500000000</td></tr><tr><td>0.20</td><td>0.20000000</td><td>0.2000000000</td></tr><tr><td>0.25</td><td>0.25000000</td><td>0.2500000000</td></tr><tr><td>0.30</td><td></td><td>0.3000000000</td></tr><tr><td>0.35</td><td>0.30000035 0.34998486</td><td>0.3500000000</td></tr><tr><td>0.40</td><td>0.40036338</td><td>0.4000000000</td></tr><tr><td>0.45</td><td>0.44586251</td><td>0.4500000000</td></tr><tr><td>0.50</td><td>0.50476331±</td><td>0.5000000000</td></tr><tr><td>0.55</td><td></td><td>0.5499999997</td></tr><tr><td>0.60</td><td>0.03217504i 0.58968169±</td><td>0.6000000010</td></tr><tr><td></td><td></td><td></td></tr><tr><td>0.65</td><td>0.08261649i</td><td>0.6499999972</td></tr><tr><td>0.70</td><td>0.69961791±</td><td>0.7000000053</td></tr><tr><td>0.75</td><td>0.12594150 i</td><td>0.7499999930</td></tr><tr><td>0.80</td><td>0.83653687±</td><td>0.8000000063</td></tr><tr><td>0.85</td><td>0.14063124i</td><td>0.8499999962</td></tr><tr><td>0.90</td><td>0.97512197±</td><td>0.9000000013</td></tr><tr><td>0.95</td><td>0.09701652i</td><td>0.9499999998</td></tr><tr><td>1.00</td><td>1.04234541</td><td>1.0000000000</td></tr></table>

![](images/9c16a21802309beaaeb76bd219cbb1a6d699a318501e057b6c7114693f0744ed.jpg)  
Fig. 12.3. Perturbation regions for the Bernstein (dark grey) and power (light grey) forms of a degree–6 Wilkinson polynomial with specified relative coefficient error $\epsilon$ .

Figure 12.3 shows the perturbation regions defined by (12.14) for the power and Bernstein forms of a polynomial of the Wilkinson form (12.35) with $n = 6$ and relative coefficient perturbations $\epsilon = 0 . 0 0 0 0 \dot { 2 }$ and 0.002. The intervals defined by the intersections of these regions with the $t$ –axis bound the values of the real roots. For the $\epsilon = 0 . 0 0 0 0 2$ perturbation, the width of the Bernstein– form perturbation region is narrower than the line thickness in the plot, but the power–form perturbation region is already quite prominent. For $\epsilon = 0 . 0 0 2$ , the Bernstein–form region becomes more apparent, but it is still possible to unambiguously distinguish the six real roots. However, the power–form region grows dramatically, and the identities of the original six roots are lost.

# 12.4.4 Vector and Matrix Norms

We have discussed above the stability of univariate polynomials, which may be regarded as non–linear maps from an independent variable $x$ to a dependent variable, $y = p ( x )$ — the value of the polynomial. The stability properties of maps between several variables are also important, but since the analysis is more difficult we confine our attention to linear multivariate maps, specified by matrices. In order to proceed, we need to introduce some basic concepts concerning the norms of vectors and matrices.

Let $\mathbf { v } = ( v _ { 0 } , \ldots , v _ { n } ) ^ { T }$ be a column vector $^ { 8 }$ with $n + 1$ real elements. By a norm of $\mathbf { v }$ , we mean a non–negative number that characterizes the “length” or “magnitude” of this vector. We are familiar with the Euclidean norm,

$$
\| \mathbf { v } \| _ { 2 } = \sqrt { v _ { 0 } ^ { 2 } + \cdot \cdot \cdot + v _ { n } ^ { 2 } } ,
$$

which may be regarded as a special case of the $p$ –norm defined by

$$
\| \mathbf { v } \| _ { p } = \left[ \sum _ { i = 0 } ^ { n } | v _ { i } | ^ { p } \right] ^ { 1 / p } .
$$

In the particular cases $p = 1$ and $p = \infty$ , we have

$$
\left\| \mathbf { v } \right\| _ { 1 } = \sum _ { i = 0 } ^ { n } \left| v _ { i } \right| \qquad { \mathrm { a n d } } \qquad \left\| \mathbf { v } \right\| _ { \infty } = \operatorname* { m a x } _ { 0 \leq i \leq n } \left| v _ { i } \right| .
$$

The case $p = \infty$ is sometimes called the maximum or uniform norm. For all $p$ , the norms defined by (12.38) satisfy the following conditions:

1. $\| \mathbf { v } \| _ { p } \geq 0 ~ { \mathrm { a n d } } \ \| \mathbf { v } \| _ { p } = 0 \iff \mathbf { v } = \mathbf { 0 } ;$   
2. $\left\| \alpha \mathbf { v } \right\| _ { p } = \left| \alpha \right| \left\| \mathbf { v } \right\| _ { p }$ for any scalar $\alpha$ ;   
3. $\| \mathbf { v } + \mathbf { u } \| _ { p } \leq \| \mathbf { v } \| _ { p } + \| \mathbf { u } \| _ { p }$ (the “triangle inequality”).

The triangle inequality is a consequence of Minkowski’s inequality [31]:

$$
\left[ \sum _ { i = 0 } ^ { n } ( x _ { i } + y _ { i } ) ^ { p } \right] ^ { 1 / p } \leq \left[ \sum _ { i = 0 } ^ { n } x _ { i } ^ { p } \right] ^ { 1 / p } + \left[ \sum _ { i = 0 } ^ { n } y _ { i } ^ { p } \right] ^ { 1 / p }
$$

(where $p \geq 1$ ) for sets of non–negative real numbers $x _ { 0 } , \ldots , x _ { n }$ and $y _ { 0 } , \ldots , y _ { n }$ . Note that $\| \mathbf { v } + \mathbf { u } \| _ { p } = \| \mathbf { v } \| _ { p } + \| \mathbf { u } \| _ { p }$ if and only if the vectors $\mathbf { u }$ and $\mathbf { v }$ are parallel, i.e., $u _ { k } = \alpha v _ { k }$ for some scalar $\alpha$ and $k = 0 , \ldots , n$ .

Because of the simplicity of the corresponding matrix norms, we shall use mostly the $\left\| \mathbf { v } \right\| _ { 1 }$ and $\| \mathbf { v } \| _ { \infty }$ vector norms. The following bounds indicate that the choice of $p$ does not strongly influence the value of $\left\| \mathbf { v } \right\| _ { p }$ :

Lemma 12.1 For all vectors $\mathbf { v }$ , the norm $\| \mathbf { v } \| _ { p }$ with $1 < p < \infty$ satisfies

$$
{ \frac { \left\| \mathbf { v } \right\| _ { 1 } } { ( n + 1 ) ^ { 1 - 1 / p } } } \leq \left\| \mathbf { v } \right\| _ { p } \leq \left\| \mathbf { v } \right\| _ { 1 } \quad { a n d } \quad \left\| \mathbf { v } \right\| _ { \infty } \leq \left\| \mathbf { v } \right\| _ { p } \leq ( n + 1 ) ^ { 1 / p } { \left\| \mathbf { v } \right\| _ { \infty } } .
$$

These bounds may be verified by appealing to H¨older’s inequality [31]:

$$
\sum _ { i = 0 } ^ { n } x _ { i } y _ { i } \ \leq \ \left[ \sum _ { i = 0 } ^ { n } x _ { i } ^ { p } \right] ^ { 1 / p } \left[ \sum _ { i = 0 } ^ { n } y _ { i } ^ { q } \right] ^ { 1 / q }
$$

for non–negative real numbers $x _ { 0 } , \ldots , x _ { n }$ and $y _ { 0 } , \ldots , y _ { n }$ where $p$ and $q$ satisfy

$$
\frac { 1 } { p } + \frac { 1 } { q } = 1 \quad \mathrm { a n d } \quad 1 < p , q < \infty .
$$

Since $\left\| \mathbf { v } \right\| _ { \infty } \leq \left\| \mathbf { v } \right\| _ { p } \leq \left\| \mathbf { v } \right\| _ { 1 }$ for all $\mathbf { v }$ and $1 < p < \infty$ , we may regard $\| \mathbf { v } \| _ { \infty }$ as the “smallest” of the vector norms (12.38), and $\left\| \mathbf { v } \right\| _ { 1 }$ as the “largest.”

For any real $( n + 1 ) \times ( n + 1 )$ matrix $\mathbf { M }$ , the matrix norm subordinate to or induced by the vector norm (12.38) is the non–negative number defined by

$$
\left\| \mathbf { M } \right\| _ { p } = \operatorname* { m a x } _ { \mathbf { v } \neq \mathbf { 0 } } \frac { \left\| \mathbf { M } \mathbf { v } \right\| _ { p } } { \left\| \mathbf { v } \right\| _ { p } } .
$$

Informally, we may think of the matrix norm $\left\| \mathbf { M } \right\| _ { p }$ as the greatest factor by which the “length” of any vector (as measured by the vector norm $\| \mathbf { v } \| _ { p } )$ ) is increased through the action of the linear map M. From the scaling property $\| \alpha \mathbf { v } \| _ { p } = | \alpha | \| \mathbf { v } \| _ { p }$ of the vector norm, we also have the alternative definition

$$
\| \mathbf { M } \| _ { p } = \operatorname* { m a x } _ { \| \mathbf { v } \| _ { p } = 1 } \| \mathbf { M } \mathbf { v } \| _ { p } .
$$

Note that from (12.40) we may infer the inequality

$$
\| \mathbf { M } \mathbf { v } \| _ { p } \leq \| \mathbf { M } \| _ { p } \| \mathbf { v } \| _ { p } \quad { \mathrm { f o r ~ a l l ~ } } \mathbf { v } \neq \mathbf { 0 } .
$$

Furthermore, it can be shown [256] that the bound given in (12.41) is sharp, i.e., there exists a non–zero $\mathbf { v }$ for which $\| \mathbf { M } \mathbf { v } \| _ { p } = \| \mathbf { M } \| _ { p } \| \mathbf { v } \| _ { p }$ . The following properties of the matrix norm (12.40) are easily verified:

1. $\| \mathbf { M } \| _ { p } \geq 0$ and $\| \mathbf { M } \| _ { p } = 0 \iff \mathbf { M } = \mathbf { 0 }$ ;   
2. $\left\| \alpha \mathbf { M } \right\| _ { p } = | \alpha | \left\| \mathbf { M } \right\| _ { p }$ for any scalar $\alpha$ ;   
3. $\| \mathbf { A } + \mathbf { B } \| _ { p } \leq \| \mathbf { A } \| _ { p } + \| \mathbf { B } \| _ { p }$ ;   
4. $\| \mathbf { A B } \| _ { p } \leq \| \mathbf { A } \| _ { p } \| \mathbf { B } \| _ { p }$ .

For general $p$ , the matrix norm (12.40) can be quite difficult to compute, or even estimate. However, the cases $p = 1$ and $p = \infty$ are relatively simple.

Proposition 12.1 Let $M _ { j k }$ for $0 \leq j , k \leq n$ be the matrix elements of M. Then the norms $\left\| \mathbf { M } \right\| _ { 1 }$ and $\| \mathbf { M } \| _ { \infty }$ are given by

$$
\left\| \mathbf { M } \right\| _ { 1 } = \operatorname* { m a x } _ { 0 \leq k \leq n } \sum _ { j = 0 } ^ { n } \left| M _ { j k } \right| \quad { \mathrm { a n d } } \quad \left\| \mathbf { M } \right\| _ { \infty } = \operatorname* { m a x } _ { 0 \leq j \leq n } \sum _ { k = 0 } ^ { n } \left| M _ { j k } \right|
$$

i.e., they are the greatest of the column sums and row sums of absolute values of the matrix elements $M _ { j k }$ , respectively.

Proof : First, for $\left. \mathbf { M } \right. _ { 1 }$ , we use the triangle inequality (12.23) to note that

$$
\| \mathbf { M } \mathbf { v } \| _ { 1 } = \sum _ { j = 0 } ^ { n } \left| \sum _ { k = 0 } ^ { n } M _ { j k } v _ { k } \right| \leq \sum _ { j = 0 } ^ { n } \sum _ { k = 0 } ^ { n } | M _ { j k } | \| v _ { k } | = \sum _ { k = 0 } ^ { n } \left[ \sum _ { j = 0 } ^ { n } | M _ { j k } | \right] \left| v _ { k } \right| .
$$

The term in parenthesis on the right is the sum of absolute values of matrix elements across column $k$ . Replacing this by the greatest such sum, we have

$$
\| \mathbf { M } \mathbf { v } \| _ { 1 } \leq \left[ \operatorname* { m a x } _ { 0 \leq k \leq n } \sum _ { j = 0 } ^ { n } \left| M _ { j k } \right| \right] \sum _ { k = 0 } ^ { n } \left| v _ { k } \right| = \left[ \operatorname* { m a x } _ { 0 \leq k \leq n } \sum _ { j = 0 } ^ { n } \left| M _ { j k } \right| \right] \| \mathbf { v } \| _ { 1 } ,
$$

and if column $m$ exhibits the greatest sum of absolute values, the above will hold with equality for the vector $\mathbf { v }$ given by

$$
v _ { k } = \delta _ { k m } = { \left\{ \begin{array} { l l } { 1 } & { { \mathrm { i f ~ } } k = m , } \\ { 0 } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }
$$

Thus, we have

$$
\| \mathbf { M } \| _ { 1 } = \operatorname* { m a x } _ { \mathbf { v } \neq \mathbf { 0 } } \frac { \| \mathbf { M } \mathbf { v } \| _ { 1 } } { \| \mathbf { v } \| _ { 1 } } = \operatorname* { m a x } _ { 0 \leq k \leq n } \sum _ { j = 0 } ^ { n } \left| M _ { j k } \right| .
$$

The argument for $\| \mathbf { M } \| _ { \infty }$ is quite similar:

$$
\begin{array} { l } { \displaystyle \| \mathbf { M } \mathbf { v } \| _ { \infty } =  \sum _ { 0 \leq j \leq n } ^ { \mathrm { a x } } | \sum _ { k = 0 } ^ { n } M _ { j k } v _ { k } | } \\ { \displaystyle \leq \operatorname* { m a x } _ { 0 \leq j \leq n } ^ { n } \sum _ { k = 0 } ^ { n } | M _ { j k } | | v _ { k } | \leq  [ \operatorname* { m a x } _ { 0 \leq j \leq n } \sum _ { k = 0 } ^ { n } | M _ { j k } | ] \operatorname* { m a x } _ { 0 \leq k \leq n } | v _ { k } | . } \end{array}
$$

Thus, since $\left\| \mathbf { v } \right\| _ { \infty } = \operatorname* { m a x } _ { k } \left| v _ { k } \right|$ , we may write

$$
\left\| \mathbf { M } \mathbf { v } \right\| _ { \infty } \leq \ \left[ \operatorname* { m a x } _ { 0 \leq j \leq n } \sum _ { k = 0 } ^ { n } \left| M _ { j k } \right| \right] \left\| \mathbf { v } \right\| _ { \infty } ,
$$

and we note that if $m$ is the row with the greatest sum of absolute values, the above holds with equality for the vector $\mathbf { v }$ defined by

$$
v _ { k } = \mathrm { s i g n } ( M _ { m k } ) = \left\{ \begin{array} { c l } { M _ { m k } / { | M _ { m k } | } } & { \mathrm { i f ~ } M _ { m k } \ne 0 , } \\ { 0 } & { \mathrm { i f ~ } M _ { m k } = 0 , } \end{array} \right.
$$

for $k = 0 , \ldots , n$ . Hence we deduce that

$$
\left\| \mathbf { M } \mathbf { v } \right\| _ { \infty } = \operatorname* { m a x } _ { \mathbf { v } \neq \mathbf { 0 } } \frac { \| \mathbf { M } \mathbf { v } \| _ { \infty } } { \| \mathbf { v } \| _ { \infty } } = \operatorname* { m a x } _ { 0 \leq j \leq n } \sum _ { k = 0 } ^ { n } \left| M _ { j k } \right| .
$$

From (12.42) it is clear that $\| \mathbf { M } \| _ { 1 } = \| \mathbf { M } ^ { T } \| _ { \infty }$ for any real matrix $\mathbf { M }$ and, in particular, that $\| \mathbf { M } \| _ { 1 } = \| \mathbf { M } \| _ { \infty }$ when $\mathbf { M }$ is a symmetric matrix.

The matrix norm subordinate to the $\| \cdot \| _ { 2 }$ vector norm defined by (12.37) is somewhat more difficult to compute:

Proposition 12.2 For any real $( n + 1 ) \times ( n + 1 )$ matrix $\mathbf { M }$ , let $\lambda _ { 0 } , \ldots , \lambda _ { n }$ be the $n + 1$ eigenvalues of the symmetric matrix $\mathbf { M } ^ { T } \mathbf { M }$ , and let

$$
\lambda _ { \operatorname* { m a x } } = \operatorname* { m a x } _ { 0 \leq i \leq n } \lambda _ { i } .
$$

Then the $\| \cdot \| _ { 2 }$ norm of the matrix M is given by

$$
\| \mathbf { M } \| _ { 2 } = \sqrt { \lambda _ { \operatorname* { m a x } } } .
$$

Proof : For any real vector $\mathbf { v }$ , we have $\mathbf { v } ^ { T } \mathbf { v } = \| \mathbf { v } \| _ { 2 } ^ { 2 }$ . Thus, by the definition of $\| \mathbf { M } \| _ { 2 }$ , we obtain

$$
\| \mathbf { M } \| _ { 2 } ^ { 2 } = \operatorname* { m a x } _ { \mathbf { v } \neq \mathbf { 0 } } \frac { \| \mathbf { M } \mathbf { v } \| _ { 2 } ^ { 2 } } { \| \mathbf { v } \| _ { 2 } ^ { 2 } } = \operatorname* { m a x } _ { \mathbf { v } \neq \mathbf { 0 } } \frac { ( \mathbf { M } \mathbf { v } ) ^ { T } \mathbf { M } \mathbf { v } } { \mathbf { v } ^ { T } \mathbf { v } } = \operatorname* { m a x } _ { \mathbf { v } \neq \mathbf { 0 } } \frac { \mathbf { v } ^ { T } ( \mathbf { M } ^ { T } \mathbf { M } ) \mathbf { v } } { \mathbf { v } ^ { T } \mathbf { v } } .
$$

Now let $\mathbf { e } _ { 0 } , \ldots , \mathbf { e } _ { n }$ be orthonormal eigenvectors for $\mathbf { M } ^ { T } \mathbf { M }$ , corresponding to its eigenvalues $\lambda _ { 0 } , \ldots , \lambda _ { n }$ (not necessarily all distinct), so that

$$
\mathbf { M } ^ { T } \mathbf { M } \mathbf { e } _ { i } = \lambda _ { i } \mathbf { e } _ { i } \quad \mathrm { f o r } \ i = 0 , \dots , n .
$$

In this eigensystem, any non–zero vector $\mathbf { v }$ has a representation of the form

$$
\mathbf { v } = \sum _ { i = 0 } ^ { n } c _ { i } \mathbf { e } _ { i } ,
$$

where the coefficients $\left\{ c _ { i } \right\}$ are not all zero. Since ${ \bf e } _ { j } \cdot { \bf e } _ { k } = \delta _ { j k }$ , we note that

$$
\mathbf { v } ^ { T } \mathbf { v } = \sum _ { i = 0 } ^ { n } c _ { i } ^ { 2 } \qquad { \mathrm { a n d } } \qquad \mathbf { v } ^ { T } ( \mathbf { M } ^ { T } \mathbf { M } ) \mathbf { v } = \sum _ { i = 0 } ^ { n } c _ { i } ^ { 2 } \lambda _ { i } ,
$$

and on substituting into (12.43) we have

$$
\| \mathbf { M } \| _ { 2 } ^ { 2 } = \operatorname* { m a x } _ { ( c _ { 0 } , \ldots , c _ { n } ) \neq ( 0 , \ldots , 0 ) } \frac { \sum c _ { i } ^ { 2 } \lambda _ { i } } { \sum c _ { i } ^ { 2 } } = \operatorname* { m a x } _ { 0 \leq i \leq n } \lambda _ { i } .
$$

$\| \mathbf { M } \mathbf { v } \| _ { 2 } ^ { 2 } / \| \mathbf { v } \| _ { 2 } ^ { 2 }$ attains its maximum value when $\mathbf { v } = \mathbf { e } _ { \mathrm { m a x } }$ , i.e., the eigenvector corresponding to the largest eigenvalue $\lambda _ { \mathrm { m a x } }$ .

The eigenvalues of $\mathbf { M } ^ { T } \mathbf { M }$ are called the singular values of the matrix M (they are necessarily real and non–negative), and $\| \mathbf { M } \| _ { 2 }$ is also known as the spectral norm of $\mathbf { M }$ , since $\lambda _ { \mathrm { m a x } }$ is the spectral radius of $\mathbf { M } ^ { T } \mathbf { M }$ [471]. If $\mathbf { M }$ is a symmetric matrix, we have $\mathbf { M } ^ { T } \mathbf { M } = \mathbf { M } ^ { 2 }$ , and the eigenvalues $\lambda _ { 0 } , \ldots , \lambda _ { n }$ of $\mathbf { M } ^ { T } \mathbf { M }$ are then just the squares of the eigenvalues of $\mathbf { M }$ . Thus, for $\mu _ { 0 } , \ldots , \mu _ { n }$ a symmetric matrix we may write

$$
\| { \bf M } \| _ { 2 } = \operatorname* { m a x } _ { 0 \leq i \leq n } \left| \mu _ { i } \right| .
$$

# 12.4.5 Condition of a Linear Map

We are now ready to define the condition number of a linear map. Suppose $\mathbf { M }$ is a non–singular matrix that maps $\mathbf { x } = ( x _ { 0 } , \ldots , x _ { n } )$ to $\mathbf { y } = ( y _ { 0 } , \ldots , y _ { n } )$ :

$$
\mathbf { y } = \mathbf { M } \mathbf { x } .
$$

When the “input” vector $\mathbf { x }$ suffers the perturbation $\delta \mathbf { x } = ( \delta x _ { 0 } , \ldots , \delta x _ { n } )$ , a corresponding perturbation $\delta \mathbf { y } = ( \delta { y } _ { 0 } , \ldots , \delta { y } _ { n } )$ is induced in the “output” vector, given by

$$
\delta \mathbf { y } = \mathbf { M } \delta \mathbf { x } .
$$

We characterize these perturbations by scalar fractional measures of the form

$$
\epsilon _ { \mathbf { x } } = \frac { \left\| \delta \mathbf { x } \right\| _ { p } } { \left\| \mathbf { x } \right\| _ { p } } \qquad \mathrm { a n d } \qquad \epsilon _ { \mathbf { y } } = \frac { \left\| \delta \mathbf { y } \right\| _ { p } } { \left\| \mathbf { y } \right\| _ { p } } .
$$

Now since $\mathbf { M }$ is non–singular, the inverse map

$$
\mathbf { x } = \mathbf { M } ^ { - 1 } \mathbf { y }
$$

also exists. Applying the inequality (12.41) to (12.46) and (12.48), we obtain

$$
\left\| \delta \mathbf { y } \right\| _ { p } \leq \left\| \mathbf { M } \right\| _ { p } \left\| \delta \mathbf { x } \right\| _ { p } \qquad { \mathrm { a n d } } \qquad \left\| \mathbf { x } \right\| _ { p } \leq \left\| \mathbf { M } ^ { - 1 } \right\| _ { p } \left\| \mathbf { y } \right\| _ { p } .
$$

Combining these inequalities, we see that $\epsilon _ { \mathbf { y } }$ is bounded in terms of $\epsilon _ { \mathbf { x } }$ by

$$
\epsilon _ { \mathbf { y } } \leq C _ { p } ( \mathbf { M } ) \epsilon _ { \mathbf { x } } ,
$$

where the $p$ –norm condition number $C _ { p } ( \mathbf { M } )$ of the matrix $\mathbf { M }$ is defined by

$$
C _ { p } ( \mathbf { M } ) = \| \mathbf { M } \| _ { p } \| \mathbf { M } ^ { - 1 } \| _ { p } .
$$

The condition number $C _ { p } ( \mathbf { M } )$ gives a sharp bound on the error amplification in the linear map (12.45), i.e., there always exists a perturbation $\delta \mathbf { x }$ for which (12.49) holds with equality. Note also that (12.49) does not depend upon the assumption of infinitesimal perturbations. In terms of the amplification of the output error $\epsilon _ { \mathbf { y } }$ relative to the input error $\epsilon _ { \mathbf { x } }$ , the two factors in $( 1 2 . 5 0 )$ ycan be interpreted as follows: $\| \mathbf { M } \| _ { p }$ xindicates how much larger the absolute output errors $\delta$ y are than the absolute input errors $\delta \mathbf { x }$ , while $\| \mathbf { M } ^ { - 1 } \| _ { p }$ indicates how much smaller the nominal output $\mathbf { y }$ is than the nominal input $\mathbf { x }$ .

The following useful properties of the condition numbers of non–singular matrices are not difficult to verify:

1. $C _ { p } ( \mathbf { M } ) \geq 1$ ;   
2. $C _ { p } ( \mathbf { M } ^ { - 1 } ) = C _ { p } ( \mathbf { M } )$ ;   
3. if $\mathbf { M } = \mathbf { M } _ { 1 } \mathbf { M } _ { 2 }$ then $C _ { p } ( \mathbf { M } ) \leq C _ { p } ( \mathbf { M } _ { 1 } ) C _ { p } ( \mathbf { M } _ { 2 } )$ ;   
4. $C _ { 1 } ( \mathbf { M } ) = C _ { \infty } ( \mathbf { M } )$ if $\mathbf { M }$ is symmetric;   
5. $C _ { 2 } ( \mathbf { M } ) = \sqrt { \lambda _ { \operatorname* { m a x } } / \lambda _ { \operatorname* { m i n } } }$ , where $\lambda _ { \mathrm { m i n } }$ and $\lambda _ { \mathrm { m a x } }$   
are the smallest and largest eigenvalues of $\mathbf { M } ^ { T } \mathbf { M }$ .

Property 1 implies that, in the linear map (12.45), the greatest relative error $\epsilon _ { \mathbf { y } }$ in the “output” $\mathbf { y }$ will always exceed that $\epsilon _ { \mathbf { x } }$ in the “input” $\mathbf { x }$ .

xThe condition number can also be used to characterize the sensitivity of $\mathbf { x }$ to perturbations of $\mathbf { M }$ , assuming $\mathbf { y }$ is held constant in equation (12.45). It can be shown [364] that when $\mathbf { M }$ suffers a perturbation $\delta \mathbf { M }$ , with y fixed, the induced relative uncertainty in $\mathbf { x }$ is bounded by

$$
\epsilon _ { \mathbf { x } } \leq \frac { C _ { p } ( \mathbf { M } ) \epsilon _ { \mathbf { M } } } { 1 - C _ { p } ( \mathbf { M } ) \epsilon _ { \mathbf { M } } } ,
$$

where $\epsilon _ { \mathbf { M } } = \| \delta \mathbf { M } \| _ { p } / \| \mathbf { M } \| _ { p }$ is assumed to be smaller than $1 / C _ { p } ( \mathbf { M } )$ .

MMatrix condition numbers for norms other than $p = 1$ , $2$ , $\infty$ are, in general, quite difficult to compute. However, we can bound their values in terms of the “simple” instances $C _ { 1 } ( \mathbf { M } )$ and $C _ { \infty } ( \mathbf { M } )$ as follows. It can be shown $^ { 9 }$ that any square matrix M satisfies the inequality

$$
\left\| \mathbf { M } \right\| _ { p } \leq \left\| \mathbf { M } \right\| _ { 1 } ^ { 1 / p } \left\| \mathbf { M } \right\| _ { \infty } ^ { 1 - 1 / p } .
$$

Now, since $\| \mathbf { M } \| _ { 1 }$ and $\| \mathbf { M } \| _ { \infty }$ are the greatest sums of absolute values across columns and rows, $\| \mathbf { M } \| _ { 1 } \leq ( n + 1 ) \| \mathbf { M } \| _ { \infty }$ and $\| \mathbf { M } \| _ { \infty } \leq \left( n + 1 \right) \| \mathbf { M } \| _ { 1 }$ . On substituting into the above inequality, and applying similar arguments to the inverse ${ { \bf { M } } ^ { - 1 } }$ , we obtain the relations

$$
C _ { p } ( \mathbf { M } ) \leq ( n + 1 ) ^ { 2 - 2 / p } C _ { 1 } ( \mathbf { M } ) \qquad \mathrm { a n d } \qquad C _ { p } ( \mathbf { M } ) \leq ( n + 1 ) ^ { 2 / p } C _ { \infty } ( \mathbf { M } ) .
$$

Since the condition numbers $C _ { 1 } ( \mathbf { M } )$ and $C _ { \infty } ( \mathbf { M } )$ are perhaps easiest to use in practice, it is useful to explicitly note the forms of the fractional error measures associated with them, namely

$$
\epsilon _ { \mathbf { x } } = { \frac { | \delta x _ { 0 } | + \cdots + | \delta x _ { n } | } { | x _ { 0 } | + \cdots + | x _ { n } | } } \qquad { \mathrm { f o r ~ } } p = 1 ,
$$

and

$$
\epsilon _ { { \bf x } } = \frac { \operatorname* { m a x } _ { k } | \delta x _ { k } | } { \operatorname* { m a x } _ { k } | x _ { k } | } \quad \quad \mathrm { f o r } \ p = \infty .
$$

Notwithstanding these different definitions, property 4 above indicates that, when $\mathbf { M }$ is symmetric, its condition numbers in the two norms are identical.

# 12.4.6 Basis Transformations

Consider the matrix M that maps the Bernstein coefficients ${ \bf c } = ( c _ { 0 } , \ldots , c _ { n } ) ^ { T }$ of a polynomial $p ( t )$ to its power coefficients $\mathbf { a } = ( a _ { 0 } , \ldots , a _ { n } ) ^ { T }$ :

$$
\mathbf { a } = \mathbf { M } \mathbf { c } , \qquad \mathrm { w h e r e } p ( t ) = \sum _ { k = 0 } ^ { n } a _ { k } t ^ { k } = \sum _ { k = 0 } ^ { n } c _ { k } b _ { k } ^ { n } ( t ) .
$$

The elements of M and its inverse ${ { \bf { M } } ^ { - 1 } }$ are given [147] by

$$
M _ { j k } = \left\{ { \begin{array} { l l } { ( - 1 ) ^ { j - k } { \binom { n } { j } } { \binom { j } { k } } } & { { \mathrm { i f ~ } } j \geq k , } \\ { \qquad 0 } & { { \mathrm { i f ~ } } j < k , } \end{array} } \right.
$$

and

$$
M _ { j k } ^ { - 1 } = \left\{ \begin{array} { c c } { { \binom { j } { k } } } & { { } } \\ { { \binom { n } { k } } } & { { \mathrm { i f ~ } j \geq k , } } \\ { { } } & { { } } \\ { { 0 } } & { { \mathrm { i f ~ } j < k . } } \end{array} \right.
$$

It can be shown [147] that the condition number of this matrix in the $\| \cdot \| _ { 1 }$ and $\| \cdot \| _ { \infty }$ norms is

$$
C _ { 1 } ( \mathbf { M } ) = C _ { \infty } ( \mathbf { M } ) = ( n + 1 ) { \binom { n } { \nu } } 2 ^ { \nu } , \quad { \mathrm { w h e r e ~ } } \nu = \left\lfloor { \frac { 2 ( n + 1 ) } { 3 } } \right\rfloor
$$

(the value of the “floor” function $\lfloor x \rfloor$ is the largest integer not exceeding $x$ ). For $n \geq 3$ , a good approximation to the above [147] is given by

$$
C _ { 1 } ( { \bf M } ) = C _ { \infty } ( { \bf M } ) \approx 3 ^ { n + 1 } \sqrt { \frac { n + 1 } { 4 \pi } } .
$$

Clearly, the condition number grows very rapidly with the polynomial degree $n$ , and explicit conversions between the power and Bernstein bases are quite unstable for high–degree polynomials, e.g., $C \approx 1 0 ^ { 1 0 }$ when $n = 2 0$ — see also [111]. In numerical analysis, as in all walks of life, there is no free lunch: if we wish to take advantage of the enhanced stability properties of the Bernstein representation discussed in $\ S 1 2 . 4 . 1 \mathrm { - } 1 2 . 4 . 3$ , we must formulate the problem in Bernstein form ab initio. There is nothing to be gained from explicit floating– point conversions from the power to the Bernstein basis.

On the other hand, the transformation between the Bernstein basis and the Legendre basis on $[ 0 , 1 ]$ — defined by the recurrence (3.6) with $L _ { 0 } ( t ) = 1$ and $L _ { 1 } ( t ) = 2 t - 1$ — is relatively well–conditioned. It can be shown [154] that the elements of the matrix $\mathbf { M }$ that transforms the Legendre coefficients of a degree– $\boldsymbol { n }$ polynomial into its Bernstein coefficients are given explicitly by

$$
M _ { j k } = \frac { 1 } { { \binom { n } { j } } } \sum _ { i = \operatorname* { m a x } ( 0 , j + k - n ) } ^ { \operatorname* { m i n } ( j , k ) } ( - 1 ) ^ { k + i } { \binom { k } { i } } { \binom { k } { i } } { \binom { n - k } { j - i } } ,
$$

while the elements of the inverse ${ { \bf { M } } ^ { - 1 } }$ are given by

$$
M _ { j k } ^ { - 1 } = { \frac { 2 j + 1 } { n + j + 1 } } { \binom { n } { k } } \sum _ { i = 0 } ^ { j } ( - 1 ) ^ { j + i } { \frac { { \binom { j } { i } } { \binom { j } { i } } } { { \binom { n + j } { k + i } } } }
$$

for $0 \leq j , k \leq n$ . From these expressions one may easily deduce that

$$
C _ { 1 } ( { \bf M } ) = 2 ^ { n } .
$$

for the Legendre–Bernstein basis transformation. The dependence of $C _ { \infty } ( \mathbf { M } )$ on $n$ does not admit an elementary closed–form expression, but one can easily compute it for specific $n$ values and deduce that, for all $n$ ,

$$
C _ { \infty } ( { \bf M } ) < C _ { 1 } ( { \bf M } ) .
$$

The growth of the condition number with $n$ is appreciably milder than for the power–Bernstein transformation. The Legendre form is advantageous in least– squares approximation problems. Further discussion of condition numbers for the matrices that map polynomials between the power, Bernstein, and Hermite forms may be found in [236]. Figure 12.4 summarizes these results.

![](images/deee2f339e89b129d625def69804bbef875f9bf8e06f61f0a424d45d22df304a.jpg)  
Fig. 12.4. Condition numbers $C _ { p }$ for basis transformations: Legendre–Bernstein — circles ( $p = 1$ ) and dots ( $p = \infty$ ); power–Bernstein — squares ( $p = 1$ and $\infty$ ); Bernstein–Hermite — diamonds ( $p = \infty$ ); and power–Hermite — triangles ( $p = 1$ ).

# 12.4.7 Subdivision Processes

The relation between the Bernstein coefficients $c _ { 0 } , \ldots , c _ { n }$ and $c _ { 0 } , \ldots , c _ { n }$ of a given polynomial $p ( t )$ on an interval $[ a , b ]$ and a subinterval $[ \bar { a } , b ]$ thereof is fundamental in the design of algorithms to isolate and approximate real roots on $t \in [ a , b ]$ — see §11.8. One may characterize the sensitivity of $\bar { c } _ { 0 } , \ldots , \bar { c } _ { n }$ to perturbations of uniform relative magnitude $\epsilon$ in $c _ { 0 } , \ldots , c _ { n }$ by means of a condition number for the “subdivision matrix” M defined by (11.10). In the $\| \cdot \| _ { \infty }$ norm, this is given [176] by

$$
C _ { \infty } ( \mathbf { M } ) = [ 2 f \operatorname* { m a x } ( u _ { \bar { c } } , v _ { \bar { c } } ) ] ^ { n }
$$

where $u _ { \bar { c } } = ( \bar { c } - a ) / ( b - a )$ and $v _ { \bar { c } } = ( b - \bar { c } ) / ( b - a )$ denote the barycentric coordinates of the subinterval midpoint $\begin{array} { r } { \bar { c } = \frac { 1 } { 2 } ( \bar { a } + b ) } \end{array}$ , $f = ( b - a ) / ( \bar { b } - \bar { a } )$ is the “zoom” factor of the subdivision map, and $_ { n }$ is the degree of $p ( t )$ .

# 12.4.8 Ill–posed Problems

For certain special problems, we may find that the condition number is either infinite or undefined. Thus, for example, the root condition number (12.15) becomes formally infinite at a multiple root $\tau$ , since we then have $| p ^ { \prime } ( \tau ) | = 0$ . Similarly, for a linear map specified by a singular matrix $\mathbf { M }$ , the condition number (12.50) is undefined, since the inverse ${ { \bf { M } } ^ { - 1 } }$ does not exist.

We call such “singular” cases ill–posed problems — they typically comprise a lower–dimension subset of the problem space under consideration. It may still be possible to characterize the sensitivity of the output to perturbations of the input in such cases, although the analysis will be somewhat different (as, for example, in the characterization (12.34) of the sensitivity of a multiple root to perturbations in the polynomial coefficients). In fact, the magnitudes of the condition numbers for “regular” problems are closely correlated to their “distances” from the set of ill–posed problems [125].

# 12.5 Backward Error Analysis

We have seen how to characterize the sensitivity of the solution of a problem to perturbations of its input parameters by means of the condition number. The goal of backward error analysis is to interpret the cumulative effects of the roundoff errors incurred during a particular floating–point calculation as being “equivalent” to certain input perturbations.10

Knowing the condition number and these equivalent input perturbations then allows us to accurately estimate the “quality” of the computed solution. This approach, although rather more subtle than the forward error analysis method described in 12.3, circumvents the inability of that method to fully account for cancellation effects. In essence, backward error analysis converts a question of error propagation into one of numerical stability.

# 12.5.1 Equivalent Input Errors

The basic idea underlying backward error analysis is to note that the results of floating–point arithmetic operations on operands $x$ and $y$ satisfy

$$
\begin{array} { l } { \displaystyle \mathrm { f l o a t } ( x \times y ) \equiv \left( 1 + \delta \right) x y , } \\ { \displaystyle \mathrm { f l o a t } ( x \div y ) \equiv ( 1 + \delta ) x / y , } \\ { \displaystyle \mathrm { f l o a t } ( x \pm y ) \equiv ( 1 + \delta ) x \pm ( 1 + \epsilon ) y , } \end{array}
$$

for some values $- \eta \le \delta , \epsilon \le + \eta$ . Rather than furnishing bounds on the errors incurred in floating–point arithmetic operations, the relationships (12.53) are interpreted as stating that the outcome of such operations is identical to the result of exact–arithmetic operations on perturbed operands. For multiplication and division, we associate a perturbation of relative magnitude $\leq \eta$ with just one of the two operands, whereas for addition and subtraction we must allow for such a perturbation in both operands [469].

Applying this idea to each arithmetic step of an algorithm, one can say that the final outcome of a floating–point computation is the exact result for some “neighboring” problem, corresponding to perturbed input values. The key requirement is to propagate the individual perturbations of operands in each step backward — in a symbolic, rather than numeric, manner — so as to obtain appropriate overall perturbations of the input values. These “effective”

perturbations, together with the problem condition number, yield a measure of the accuracy of a solution computed in floating–point arithmetic.

Thus, the method does not attempt a detailed step–by–step comparison of corresponding floating–point and exact–arithmetic calculations — rather, it says that the floating–point result is exact for some “nearby” problem (i.e., one with slightly different input data). Whether this hypothetical problem is sufficiently nearby to give an accurate answer depends, of course, on whether or not neighboring problems have neighboring results, i.e., on the condition of the problem. Unlike the forward error analysis approach described in §12.3.2, this method fully accommodates the possibility of cancellation effects.

# 12.5.2 Example: Horner’s Method

To illustrate the use of backward error analysis, consider the evaluation of the polynomial (3.1) by means of the Horner method (12.6). We assume again that $a _ { n } , \ldots , a _ { 0 }$ and $t$ are ab initio allowed floating–point values. The result of the $k$ –th Horner term can then be written as

$$
\begin{array} { l } { { P _ { k } = \mathrm { f o a t } ( \mathrm { f l o a t } ( t \times P _ { k - 1 } ) + a _ { n - k } ) } } \\ { { \ = ( 1 + \delta _ { k } ) ( 1 + \zeta _ { k } ) t P _ { k - 1 } + ( 1 + \epsilon _ { k } ) a _ { n - k } . } } \end{array}
$$

Here $\zeta _ { k }$ is the perturbation associated with the product, and $\delta _ { k }$ and $\epsilon _ { k }$ are the perturbations associated with the sum; these quantities are all of magnitude $\leq$ $\eta$ . We emphasize the intended interpretation of equation (12.54): it represents an exact execution of the Horner step (12.6), but with perturbed operands for example

$$
\begin{array} { r } { 1 + \zeta _ { k } ) t , \quad ( 1 + \delta _ { k } ) P _ { k - 1 } , \quad \mathrm { a n d } \quad ( 1 + \epsilon _ { k } ) a _ { n - k } } \end{array}
$$

— rather than the nominal operands $t$ , $P _ { k - 1 }$ , and $a _ { n - k }$

We are interested here only in the final computed value $P _ { n } = \mathrm { { f i o a t } } ( p ( t ) )$ of the polynomial, i.e., the value produced by a floating–point computation. By carrying through the steps (12.54) for $k = 1 , \ldots , n$ it is possible to express this value in the form

$$
\mathrm { H o a t } ( p ( t ) ) \equiv \sum _ { j = 0 } ^ { n } a _ { j } ( 1 + e _ { j } ) t ^ { j } ,
$$

i.e., the computed quantity represents the exact value of a polynomial with “perturbed” coefficients $a _ { n } ( 1 + e _ { n } ) , \dots , a _ { 0 } ( 1 + e _ { 0 } )$ in lieu of $a _ { n } , \ldots , a _ { 0 }$ .

It is not difficult to derive closed–form expressions giving the “effective” coefficient perturbations $e _ { n } , \ldots , e _ { 0 }$ in terms of the individual arithmetic–step perturbations $\delta _ { k } , \epsilon _ { k } , \zeta _ { k }$ for $k = 1 , \ldots , n$ . However, such expressions would in any case require simplification to be of practical use. This can be achieved, without formally writing down the expressions, as follows.

Upon executing (12.54) for $k = 1 , \ldots , n$ , the term with nominal coefficient $a _ { j }$ in (12.55) participates in $j$ floating–point multiplications and $j + 1$ floating– point additions (except that the $a _ { n }$ term participates in $n$ additions). If we imagine these steps to have executed in exact arithmetic, but on perturbed operands, we see that the perturbation factors in (12.55) will be of the form

$$
1 + e _ { j } = \langle 2 j + 1 \rangle \quad { \mathrm { f o r ~ } } j = 0 , \dots , n - 1 \quad { \mathrm { a n d } } \quad 1 + e _ { n } = \langle 2 n \rangle
$$

where, following Stewart [430], we introduce the notation

$$
\langle m \rangle = \prod _ { k = 1 } ^ { m } ( 1 + \lambda _ { k } ) ,
$$

the $\lambda _ { k }$ ’s denoting appropriate instances of the individual–step perturbations $\zeta _ { k }$ , $\delta _ { k }$ , $\epsilon _ { k }$ (each bounded in magnitude by $\eta$ ).

We are thus interested in finding bounds on quantities of the form (12.56). If $\eta \ll 1$ , we clearly have the approximate bound

$$
1 - m \eta \lesssim \langle m \rangle \lesssim 1 + m \eta .
$$

Assuming (as is reasonable in most practical circumstances) that $m \eta < 0 . 1$ , more rigorous bounds may be derived [110, 469] as follows. Noting that11

$$
( 1 + \eta ) ^ { m } \ : < \ : \exp ( m \eta )
$$

we have

$$
( 1 + \eta ) ^ { m } - 1 < \sum _ { k = 1 } ^ { \infty } \frac { ( m \eta ) ^ { k } } { k ! } < m \eta \sum _ { k = 0 } ^ { \infty } \left( \frac { m \eta } { 2 } \right) ^ { k } ,
$$

where the second step follows from the fact that $r ! \geq 2 ^ { r - 1 }$ for $r \geq 1$ . Now the infinite sum in the final expression is just $( 1 - \frac { 1 } { 2 } m \eta ) ^ { - 1 }$ and thus $( 1 + \eta ) ^ { m } - 1 <$ $m \eta ( 1 - \textstyle { \frac { 1 } { 2 } } m \eta ) ^ { - 1 } \lesssim 1 . 0 5 3 m \eta$ when $m \eta < 0 . 1$ . Conventionally [469], we write

$$
1 - 1 . 0 6 m \eta < \langle m \rangle < 1 + 1 . 0 6 m \eta .
$$

This completes our backward error analysis, and we can state the result as follows. If $a _ { n } , \ldots , a _ { 0 }$ are the monomial coefficients of a degree– $\boldsymbol { n }$ polynomial $p ( t )$ , the outcome $P _ { n } = \mathrm { { f l o a t } } ( p ( t ) )$ of the Horner algorithm (12.6) running in floating–point arithmetic is the exact value of a polynomial with coefficients $( 1 + e _ { n } ) a _ { n } , \ldots , ( 1 + e _ { 0 } ) a _ { 0 }$ , where the perturbations $e _ { j }$ satisfy

$$
| e _ { j } | < 1 . 0 6 ( 2 j + 1 ) \eta \quad \mathrm { f o r ~ } j = 0 , \ldots , n - 1 \quad \mathrm { a n d } \quad | e _ { n } | < 1 . 0 6 2 n \eta .
$$

These uncertainties are evidently of non–uniform magnitude — higher–order terms participate in more floating–point operations, and consequently their coefficients exhibit larger “effective” perturbations.

However, our condition numbers (12.15) and (12.33) for polynomial values and roots were based on the assumption of uniform error $\epsilon$ in the coefficients. As a conservative measure, one can multiply these condition numbers by $\epsilon =$ $e _ { n }$ (the largest perturbation) to estimate the effects of rounding errors on the computed value. Alternately, it is not too difficult to reformulate the condition numbers to allow for non–uniform coefficient perturbations.

Similar backward error analysis techniques can be applied to algorithms for systems of linear equations. For example, in the matrix equation

$$
\mathbf { M } \mathbf { x } = \mathbf { y } ,
$$

which we might solve by Gaussian elimination, the right–hand side vector $\mathbf { y }$ is the “input” and the vector of unknowns $\mathbf { x }$ is the “output.” A backward error analysis of Gaussian elimination (see, for example, Appendix 3 of [430]) then reveals that a floating–point solution to this system is equivalent to the exact solution of a perturbed system, with right–hand side $\mathbf { y } + \delta \mathbf { y }$ . Knowing the condition number $C _ { p } ( \mathbf { M } )$ of the matrix, and the relative magnitude $\epsilon _ { \mathbf { y } } =$ $\| \delta \mathbf { y } \| _ { p } / \| \mathbf { y } \| _ { p }$ yof the “effective” input perturbations, then allows us to estimate the cumulative effects of the round–off errors during the solution procedure.
