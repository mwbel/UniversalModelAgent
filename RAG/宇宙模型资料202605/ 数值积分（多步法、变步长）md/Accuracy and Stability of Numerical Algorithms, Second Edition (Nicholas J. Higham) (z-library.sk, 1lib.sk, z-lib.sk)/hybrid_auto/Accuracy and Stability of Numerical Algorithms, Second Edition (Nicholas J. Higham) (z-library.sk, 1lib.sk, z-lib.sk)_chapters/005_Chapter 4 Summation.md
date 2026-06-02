# Chapter 4 Summation

I do hate sums.

There is no greater mistake than to call arithmetic an exact science.

There are ... hidden laws of Number

which it requires a mind like mine to perceive.

For instance, if you add a sum from the bottom up,

and then again from the top down,

the result is always different.

MRS. LA TOUCHE

Joseph Fourier introduced this delimited $\sum$ -notation in 1820, and it soon took the mathematical world by storm.

— RONALD L. GRAHAM, DONALD E. KNUTH, and

OREN PATASHNIK, Concrete Mathematics (1994)

One of the major difficulties in a practical [error] analysis

is that of description.

An ounce of analysis follows a pound of preparation.

— BERESFORD N. PARLETT, Matrix Eigenvalue Problems (1965)

Sums of floating point numbers are ubiquitous in scientific computing. They occur when evaluating inner products, means, variances, norms, and all kinds of nonlinear functions. Although at first sight summation might appear to offer little scope for algorithmic ingenuity, the usual "recursive summation" (with various orderings) is just one of a variety of possible techniques. We describe several summation methods and their error analyses in this chapter. No one method is uniformly more accurate than the others, but some guidelines can be given on the choice of method in particular cases.

# 4.1. Summation Methods

In most circumstances in scientific computing we would naturally translate a sum $\sum_{i=1}^{n} x_i$ into code of the form

$$
\begin{array}{l} s = 0 \\ f o r i = 1: n \\ s = s + x _ {i} \\ \end{array}
$$

end

This is known as recursive summation. Since the individual rounding errors depend on the operands being summed, the accuracy of the computed sum $\widehat{s}$ varies with the ordering of the $x_{i}$ . (Hence Mrs. La Touche, quoted at the beginning of the chapter, was correct if we interpret her remarks as applying to floating point arithmetic.) Two interesting choices of ordering are the increasing order $|x_1|\leq |x_2|\leq \dots \leq |x_n|$ , and the decreasing order $|x_{1}|\geq |x_{2}|\geq \dots \geq |x_{n}|$ .

Another method is pairwise summation (also known as cascade summation, or fan-in summation), in which the $x_{i}$ are summed in pairs according to

$$
y _ {i} = x _ {2 i - 1} + x _ {2 i}, \quad i = 1: \left\lfloor \frac {n}{2} \right\rfloor \quad (y _ {(n + 1) / 2} = x _ {n} \text {i f} n \text {i s o d d}),
$$

and this pairwise summation process is repeated recursively on the $y_{i}$ , $i = 1: \lfloor (n + 1) / 2 \rfloor$ . The sum is obtained in $\lceil \log_2 n \rceil$ stages. For $n = 6$ , for example, pairwise summation forms

$$
S _ {6} = \left(\left(x _ {1} + x _ {2}\right) + \left(x _ {3} + x _ {4}\right)\right) + \left(x _ {5} + x _ {6}\right).
$$

Pairwise summation is attractive for parallel computing, because each of the $\lceil \log_2 n \rceil$ stages can be done in parallel [629, 1988, §5.2.2].

A third summation method is the insertion method. First, the $x_{i}$ are sorted by order of increasing magnitude (alternatively, some other ordering could be used). Then $x_{1} + x_{2}$ is formed, and the sum is inserted into the list $x_{2},\ldots ,x_{n}$ , maintaining the increasing order. The process is repeated recursively until the final sum is obtained. In particular cases the insertion method reduces to one of the other two. For example, if $x_{i} = 2^{i - 1}$ , the insertion method is equivalent to recursive summation, since the insertion is always to the bottom of the list:

$$
\begin{array}{r c l r c l r c l}1&2&4&8&\rightarrow&\underline {{3}}&4&8&\rightarrow&\underline {{7}}&8&\rightarrow&1 5.\end{array}
$$

On the other hand, if $1 \leq x_{1} < x_{2} < \dots < x_{n} \leq 2$ , every insertion is to the end of the list, and the method is equivalent to pairwise summation if $n$ is a power of 2; for example, if $0 < \epsilon < 1/2$ ,

$$
1, 1 + \epsilon , 1 + 2 \epsilon , 1 + 3 \epsilon \quad \rightarrow \quad 1 + 2 \epsilon , 1 + 3 \epsilon , \underline {{2 + \epsilon}} \quad \rightarrow \quad 2 + \epsilon , \underline {{2 + 5 \epsilon}} \quad \rightarrow \quad 4 + 6 \epsilon .
$$

To choose between these methods we need error analysis, which we develop in the next section.

# 4.2. Error Analysis

Error analysis can be done individually for the recursive, pairwise, and insertion summation methods, but it is more profitable to recognize that each is a special case of a general algorithm and to analyze that algorithm.

Algorithm 4.1. Given numbers $x_{1}, \ldots, x_{n}$ this algorithm computes $S_{n} = \sum_{i=1}^{n} x_{i}$ .

Let $S = \{x_{1},\ldots ,x_{n}\}$

repeat while $S$ contains more than one element

Remove two numbers $x$ and $y$ from $S$

and add their sum $x + y$ to $\mathcal{S}$ .

end

Assign the remaining element of $S$ to $S_{n}$

Note that since there are $n$ numbers to be added and hence $n - 1$ additions to be performed, there must be precisely $n - 1$ executions of the repeat loop.

First, let us check that the previous methods are special cases of Algorithm 4.1. Recursive summation (with any desired ordering) is obtained by taking $x$ at each stage to be the sum computed on the previous stage of the algorithm. Pairwise summation is obtained by $\lceil \log_2 n \rceil$ groups of executions of the repeat loop, in each group of which the members of $S$ are broken into pairs, each of which is summed. Finally, the insertion method is, by definition, a special case of Algorithm 4.1.

Now for the error analysis. Express the $i$ th execution of the repeat loop as $T_{i} = x_{i_{1}} + y_{i_{1}}$ . The computed sums satisfy (using (2.5))

$$
\widehat {T} _ {i} = \frac {x _ {i _ {1}} + y _ {i _ {1}}}{1 + \delta_ {i}}, \quad | \delta_ {i} | \leq u, \quad i = 1: n - 1. \tag {4.1}
$$

The local error introduced in forming $\widehat{T}_i$ is $\delta_i\widehat{T}_i$ . The overall error is the sum of the local errors (since summation is a linear process), so overall we have

$$
E _ {n} := S _ {n} - \widehat {S} _ {n} = \sum_ {i = 1} ^ {n - 1} \delta_ {i} \widehat {T} _ {i}. \tag {4.2}
$$

The smallest possible error bound is therefore

$$
\left| E _ {n} \right| \leq u \sum_ {i = 1} ^ {n - 1} \left| \widehat {T} _ {i} \right|. \tag {4.3}
$$

(This is actually in the form of a running error bound, because it contains the computed quantities—see §3.3.) It is easy to see that $|\widehat{T}_i| \leq \sum_{j=1}^n |x_j| + O(u)$ for each $i$ , and so we have also the weaker bound

$$
\left| E _ {n} \right| \leq (n - 1) u \sum_ {i = 1} ^ {n} \left| x _ {i} \right| + O \left(u ^ {2}\right). \tag {4.4}
$$

This is a forward error bound. A backward error result showing that $\widehat{S}_n$ is the exact sum of terms $x_i(1 + \epsilon_i)$ with $|\epsilon_i| \leq \gamma_{n-1}$ can be deduced from (4.1), using the fact that no number $x_i$ takes part in more than $n-1$ additions.

The following criterion is apparent from (4.2) and (4.3):

In designing or choosing a summation method to achieve high accuracy, the aim should be to minimize the absolute values of the intermediate sums $T_{i}$ .

The aim specified in this criterion is surprisingly simple to state. However, even if we concentrate on a specific set of data the aim is difficult to achieve, because minimizing the bound in (4.3) is known to be NP-hard [708, 2000]. Some insight can be gained by specializing to recursive summation.

For recursive summation, $T_{i-1} = S_i \coloneqq \sum_{j=1}^i x_j$ , and we would like to choose the ordering of the $x_i$ to minimize $\sum_{i=2}^n |\widehat{S}_i|$ . This is a combinatorial optimization problem that is too expensive to solve in the context of summation. A reasonable compromise is to determine the ordering sequentially by minimizing, in turn, $|x_1|, |\widehat{S}_2|, \ldots, |\widehat{S}_{n-1}|$ . This ordering strategy, which we denote by Psum, can be implemented with $O(n \log n)$ comparisons. If we are willing to give up the property that the ordering is influenced by the signs of the $x_i$ we can instead use the increasing ordering, which in general will lead to a larger value of $\sum_{i=2}^n |\widehat{S}_i|$ than that for the Psum ordering. If all the $x_i$ have the same sign then all these orderings are equivalent. Therefore when summing nonnegative numbers by recursive summation the increasing ordering is the best ordering, in the sense of having the smallest a priori forward error bound.

How does the decreasing ordering fit into the picture? For the summation of positive numbers this ordering has little to recommend it. The bound (4.3) is no smaller, and potentially much larger, than it is for the increasing ordering. Furthermore, in a sum of positive terms that vary widely in magnitude the decreasing ordering may not allow the smaller terms to contribute to the sum (which is why the harmonic sum $\sum_{i=1}^{n} 1/i$ "converges" in floating point arithmetic as $n \to \infty$ ). However, consider the example with $n = 4$ and

$$
x = \left[ \begin{array}{l l l l} 1, & M, & 2 M, & - 3 M \end{array} \right], \tag {4.5}
$$

where $M$ is a floating point number so large that $fl(1 + M) = M$ (thus $M > u^{-1}$ ). The three orderings considered so far produce the following results:

$$
\text {I n c r e a s i n g :} \quad \widehat {S} _ {n} = f l (1 + M + 2 M - 3 M) = 0,
$$

$$
\text {P s u m :} \quad \widehat {S} _ {n} = f l (1 + M - 3 M + 2 M) = 0,
$$

$$
\text {D e c r e a s i n g :} \quad \widehat {S} _ {n} = f l (- 3 M + 2 M + M + 1) = 1.
$$

Thus the decreasing ordering sustains no rounding errors and produces the exact answer, while both the increasing and Psum orderings yield computed sums with relative error 1. The reason why the decreasing ordering performs so well in this example is that it adds the "1" after the inevitable heavy cancellation has taken place, rather than before, and so retains the important information in this term. If we evaluate the term $\mu = \sum_{i=2}^{n} |\widehat{S}_i|$ in the error bound (4.3) for example (4.5) we find

$$
\text {I n c r e a s i n g :} \mu = 4 M, \quad \text {P s u m :} \mu = 3 M, \quad \text {D e c r e a s i n g :} \mu = M + 1,
$$

so (4.3) "predicts" that the decreasing ordering will produce the most accurate answer, but the bound it provides is extremely pessimistic since there are no rounding errors in this instance.

Extrapolating from this example, we conclude that the decreasing ordering is likely to yield greater accuracy than the increasing or Psum orderings whenever there is heavy cancellation in the sum, that is, whenever $\left|\sum_{i=1}^{n} x_i\right| \ll \sum_{i=1}^{n} |x_i|$ .

Turning to the insertion method, a good explanation of the insertion strategy is that it attempts to minimize, one at a time, the terms $|\widehat{T}_1|, \ldots, |\widehat{T}_{n-1}|$ in the error bound (4.3). Indeed, if the $x_i$ are all nonnegative the insertion method minimizes this bound over all instances of Algorithm 4.1.

Finally, we note that a stronger form of the bound (4.4) holds for pairwise summation. It can be deduced from (4.3) or derived directly, as follows. Assume for simplicity that $n = 2^r$ . Unlike in recursive summation each addend takes part in the same number of additions, $\log_2 n$ . Therefore we have a relation of the form

$$
\widehat {S} _ {n} = \sum_ {i = 1} ^ {n} x _ {i} \prod_ {k = 1} ^ {\log_ {2} n} \left(1 + \delta_ {k} ^ {(i)}\right), \qquad | \delta_ {k} ^ {(i)} | \leq u,
$$

which leads to the bound

$$
\left| E _ {n} \right| \leq \gamma_ {\log_ {2} n} \sum_ {i = 1} ^ {n} \left| x _ {i} \right|. \tag {4.6}
$$

Since it is proportional to $\log_2 n$ rather than $n$ , this is a smaller bound than (4.4), which is the best bound of this form that holds in general for Algorithm 4.1.

# 4.3. Compensated Summation

We have left to last the compensated summation method, which is recursive summation with a correction term cleverly designed to diminish the rounding errors. Compensated summation is worth considering whenever an accurate sum is required and computations are already taking place at the highest precision supported by the hardware or the programming language in use.

In 1951 Gill [488, 1951] noticed that the rounding error in the sum of two numbers could be estimated by subtracting one of the numbers from the sum, and he made use of this estimate in a Runge-Kutta code in a program library for the EDSAC computer. Gill's estimate is valid for fixed point arithmetic only. Kahan [686, 1965] and Møller [870, 1965] both extended the idea to floating point arithmetic. Møller shows how to estimate $a + b - fl(a + b)$ in chopped arithmetic,

![](images/7f6d9bbb9702092c9efe0357cf818deebc8e50cd61a38b786e0a9af4bf48fb22.jpg)  
Figure 4.1. Recovering the rounding error.

while Kahan uses a slightly simpler estimate to derive the compensated summation method for computing $\sum_{i=1}^{n} x_i$ .

The estimate used by Kahan is perhaps best explained with the aid of a diagram. Let $a$ and $b$ be floating point numbers with $|a| \geq |b|$ , let $\widehat{s} = fl(a + b)$ , and consider Figure 4.1, which uses boxes to represent the significands of $a$ and $b$ . The figure suggests that if we evaluate

$$
e = - \left[ \left(a + b\right) - a\right) - b ] = (a - \widehat {s}) + b
$$

in floating point arithmetic, in the order indicated by the parentheses, then the computed $\widehat{e}$ will be a good estimate of the error $(a + b) - \widehat{s}$ . In fact, for rounded floating point arithmetic in base 2, we have

$$
a + b = \widehat {s} + \widehat {e}, \tag {4.7}
$$

that is, the computed $\widehat{e}$ represents the error exactly. This result (which does not hold for all bases) is proved by Dekker [302, 1971, Thm. 4.7], Knuth [744, 1998, Thm. C, §4.2.2], and Linnainmaa [788, 1974, Thm. 3]. Note that there is no point in computing $fl(\widehat{s} + \widehat{e})$ , since $\widehat{s}$ is already the best floating point representation of $a + b$ ! Note also that this result implies, in particular, that the error $(a + b) - \widehat{s}$ is a floating point number; for a short proof of this fact see Problem 4.6.

Kahan's compensated summation method employs the correction $e$ on every step of a recursive summation. After each partial sum is formed, the correction is computed and immediately added to the next term $x_{i}$ before that term is added to the partial sum. Thus the idea is to capture the rounding errors and feed them back into the summation. The method may be written as follows.

Algorithm 4.2 (compensated summation). Given floating point numbers $x_{1}, \ldots, x_{n}$ this algorithm forms the sum $s = \sum_{i=1}^{n} x_{i}$ by compensated summation.

$s = 0$ . $e = 0$ for $i = 1$ .. $n$ temp $= s$ $y = x_{i} + e$ $s = \text{temp} +y$ $e = (t e m p - s) + y$ $\%$ Evaluate in the order shown.   
end

The compensated summation method has two weaknesses: $\widehat{e}$ is not necessarily the exact correction, since (4.7) is based on the assumption that $|a| \geq |b|$ , and the addition $y = x_{i} + e$ is not performed exactly. Nevertheless, the use of the corrections brings a benefit in the form of an improved error bound. Knuth [744, 1998, Ex. 19, §4.2.2] shows that the computed sum $\widehat{S}_n$ satisfies

$$
\widehat {S} _ {n} = \sum_ {i = 1} ^ {n} \left(1 + \mu_ {i}\right) x _ {i}, \quad | \mu_ {i} | \leq 2 u + O \left(n u ^ {2}\right), \tag {4.8}
$$

which is an almost ideal backward error result (a more detailed version of Knuth's proof is given by Goldberg [496, 1991]).

In [688, 1972] and [689, 1973] Kahan describes a variation of compensated summation in which the final sum is also corrected (thus “ $s = s + e$ " is appended to the algorithm above). Kahan states in [688, 1972] and proves in [689, 1973] that (4.8) holds with the stronger bound $|\mu_i| \leq 2u + O((n - i + 1)u^2)$ . The proofs of (4.8) given by Knuth and Kahan are similar; they use the model (2.4) with a subtle induction and some intricate algebraic manipulation.

The forward error bound corresponding to (4.8) is

$$
\left| E _ {n} \right| \leq \left(2 u + O \left(n u ^ {2}\right)\right) \sum_ {i = 1} ^ {n} \left| x _ {i} \right|. \tag {4.9}
$$

As long as $nu \leq 1$ , the constant in this bound is independent of $n$ , and so the bound is a significant improvement over the bounds (4.4) for recursive summation and (4.6) for pairwise summation. Note, however, that if $\sum_{i=1}^{n} |x_i| \gg |\sum_{i=1}^{n} x_i|$ , compensated summation is not guaranteed to yield a small relative error.

Another version of compensated summation has been investigated by several authors: Jankowski, Smoktunowicz, and Wozniakowski [670, 1983], Jankowski and Wozniakowski [672, 1985], Kiełbasinski [731, 1973], Neumaier [883, 1974], and Nickel [892, 1970]. Here, instead of immediately feeding each correction back into the summation, the corrections are accumulated separately by recursive summation and then the global correction is added to the computed sum. For this version of compensated summation Kiełbasinski [731, 1973] and Neumaier [883, 1974] show that

$$
\widehat {S} _ {n} = \sum_ {i = 1} ^ {n} (1 + \mu_ {i}) x _ {i}, \quad | \mu_ {i} | \leq 2 u + n ^ {2} u ^ {2}, \tag {4.10}
$$

provided $nu \leq 0.1$ ; this is weaker than (4.8) in that the second-order term has an extra factor $n$ . If $n^2 u \leq 0.1$ then in (4.10), $|\mu_i| \leq 2.1u$ . Jankowski, Smoktunowicz, and Wozniakowski [670, 1983] show that, by using a divide and conquer implementation of compensated summation, the range of $n$ for which $|\mu_i| \leq cu$ holds in (4.10) can be extended, at the cost of a slight increase in the size of the constant $c$ .

Neither the correction formula (4.7) nor the result (4.8) for compensated summation holds under the no-guard-digit model of floating point arithmetic. Indeed, Kahan [696, 1990] constructs an example where compensated summation fails to achieve (4.9) on certain Cray machines, but he states that such failure is extremely rare. In [688, 1972] and [689, 1973] Kahan gives a modification of the compensated summation algorithm in which the assignment “ $e = (temp - s) + y$ ” is replaced by

$$
\begin{array}{l} f = 0 \\ \text {i f} \operatorname {s i g n} (t e m p) = \operatorname {s i g n} (y), f = (0. 4 6 * s - s) + s, \text {e n d} \\ e = \left(\left(t e m p - f\right) - (s - f)\right) + y \\ \end{array}
$$

Kahan shows in [689, 1973] that the modified algorithm achieves (4.8) "on all North American machines with floating hardware" and explains that "The mysterious constant 0.46, which could perhaps be any number between 0.25 and 0.50, and the fact that the proof requires a consideration of known machines designs, indicate that this algorithm is not an advance in computer science."

Viten'ko [1199, 1968] shows that under the no-guard-digit model (2.6) the summation method with the optimal error bound (in a certain sense defined in [1199, 1968]) is pairwise summation. This does not contradict Kahan's result because Kahan uses properties of the floating point arithmetic beyond those in the no-guard-digit model.

A good illustration of the benefits of compensated summation is provided by Euler's method for the ordinary differential equation initial value problem $y' = f(x, y)$ , $y(a)$ given, which generates an approximate solution according to $y_{k+1} = y_k + hf_k$ , $y_0 = y(a)$ . We solved the equation $y' = -y$ with $y(0) = 1$ over $[0, 1]$ using $n$ steps of Euler's method ( $nh = 1$ ), with $n$ ranging from 10 to $10^8$ . With compensated summation we replace the statements $x = x + h$ , $y = y + h * f(x, y)$ by (with the initialization $cx = 0$ , $cy = 0$ )

$$
\begin{array}{l} d x = h + c x \\ n e w _ {-} x = x + d x \\ c x = (x - n e w \_ x) + d x \\ x = n e w _ {x} \\ d y = h * f (x, y) + c y \\ n e w _ {-} y = y + d y \\ c y = (y - n e w \_ y) + d y \\ y = n e w \_ y \\ \end{array}
$$

Figure 4.2 shows the errors $e_n = |y(1) - \widehat{y}_n|$ , where $\widehat{y}_n$ is the computed approximation to $y(1)$ . The computations were done in Fortran 90 in single precision arithmetic on a Sun SPARCstation ( $u \approx 6 \times 10^{-8}$ ). Since Euler's method has global error of order $h$ , the error curve on the plot should be approximately a straight line. For the standard implementation of Euler's method the errors $e_n$ start to increase steadily beyond $n = 20000$ because of the influence of rounding errors. With compensated summation the errors $e_n$ are much less affected by rounding errors and do not grow in the range of $n$ shown (for $n = 10^8$ , $e_n$ is about 10 times larger than it would be in exact arithmetic). Plots of U-shaped curves showing total error against stepsize are common in numerical analysis textbooks (see, e.g., Forsythe, Malcolm, and Moler [430, 1977, p. 119] and Shampine [1030, 1994, p. 259]), but the textbooks rarely point out that the "U" can be flattened out by compensated summation.

The cost of applying compensated summation in an ordinary differential equation solver is almost negligible if the function $f$ is at all expensive to evaluate. But, of course, the benefits it brings are noticeable only when a vast number of

![](images/ea8e98d293097d08ef9e171a8d5bb9b92df87ba4e6c4fcb27de6965dd60bcd38.jpg)  
Figure 4.2. Errors $|y(1) - \widehat{y}_n|$ for Euler's method with ("×") and without ("o") compensated summation.

integration steps are taken. Very-long-term integrations are undertaken in celestial mechanics, where roundoff can affect the ability to track planetary orbits. Researchers in astronomy use compensated summation, and other techniques, to combat roundoff. An example application is a 3 million year integration of the planets in the solar system by Quinn, Tremaine, and Duncan [965, 1991]; it used a linear multistep method of order 13 with a constant stepsize of 0.75 days and took 65 days of machine time on a Silicon Graphics 4D-25 workstation. See also Quinn and Tremaine [964, 1990] and Quinlan [962, 1994].

Finally, we describe an even more ingenious algorithm called doubly compensated summation, derived by Priest [955, 1992] from a related algorithm of Kahan. It is compensated summation with two extra applications of the correction process and it requires 10 instead of 4 additions per step. The algorithm is tantamount to simulating double precision arithmetic with single precision arithmetic; it requires that the summands first be sorted into decreasing order, which removes the need for certain logical tests that would otherwise be necessary.

Algorithm 4.3 (doubly compensated summation). Given floating point numbers $x_{1}, \ldots, x_{n}$ this algorithm forms the sum $s_{n} = \sum_{i=1}^{n} x_{i}$ by doubly compensated summation. All expressions should be evaluated in the order specified by the parentheses.

Sort the $x_{i}$ so that $|x_1| \geq |x_2| \geq \dots \geq |x_n|$ .

$$
s _ {1} = x _ {1}; c _ {1} = 0
$$

for $k = 2:n$

$$
y _ {k} = c _ {k - 1} + x _ {k}
$$

$$
u _ {k} = x _ {k} - \left(y _ {k} - c _ {k - 1}\right)
$$

$$
t _ {k} = y _ {k} + s _ {k - 1}
$$

$$
v _ {k} = y _ {k} - \left(t _ {k} - s _ {k - 1}\right)
$$

$$
z _ {k} = u _ {k} + v _ {k}
$$

$$
s _ {k} = t _ {k} + z _ {k}
$$

$$
c _ {k} = z _ {k} - \left(s _ {k} - t _ {k}\right)
$$

end

Priest [955, 1992, §4.1] analyses this algorithm for $t$ -digit base $\beta$ arithmetic that satisfies certain reasonable assumptions—ones which are all satisfied by IEEE arithmetic. He shows that if $n \leq \beta^{t-3}$ then the computed sum $\widehat{s}_n$ satisfies

$$
\left| s _ {n} - \widehat {s} _ {n} \right| \leq 2 u \left| s _ {n} \right|,
$$

that is, the computed sum is accurate virtually to full precision.

# 4.4. Other Summation Methods

We mention briefly two further classes of summation algorithms. The first builds the sum in a series of accumulators, which are themselves added to give the sum. As originally described by Wolfe [1252, 1964] each accumulator holds a partial sum lying in a different interval. Each term $x_{i}$ is added to the lowest-level accumulator; if that accumulator overflows it is added to the next-highest one and then reset to zero, and this cascade continues until no overflow occurs. Modifications of Wolfe's algorithm are presented by Malcolm [808, 1971] and Ross [993, 1965]. Malcolm [808, 1971] gives a detailed error analysis to show that his method achieves a relative error of order $u$ . A drawback of the algorithm is that it is strongly machine dependent. An interesting and crucial feature of Malcolm's algorithm is that on the final step the accumulators are summed by recursive summation in order of decreasing absolute value, which in this particular situation precludes severe loss of significant digits and guarantees a small relative error.

Another class of algorithms, referred to as "distillation algorithms" by Kahan [695, 1987], work as follows: given $x_{i} = fl(x_{i})$ , $i = 1:n$ , they iteratively construct floating point numbers $x_{1}^{(k)},\ldots ,x_{n}^{(k)}$ such that $\sum_{i = 1}^{n}x_{i}^{(k)} = \sum_{i = 1}^{n}x_{i}$ , terminating when $x_{n}^{(k)}$ approximates $\sum_{i = 1}^{n}x_{i}$ with relative error at most $u$ . Kahan states that these algorithms appear to have average run times of order at least $n\log n$ . Anderson [23, 1999] gives a very readable description of a distillation algorithm and offers comments on earlier algorithms, including those of Bohlender [145, 1977], Leuprecht and Oberaigner [782, 1982], and Pichat [940, 1972]. See also Kahan [695, 1987] and Priest [955, 1992, pp. 66-69] for further details and references.

# 4.5. Statistical Estimates of Accuracy

The rounding error bounds presented above can be very pessimistic, because they account for the worst-case propagation of errors. An alternative way to compare

Table 4.1. Mean square errors for nonnegative $x_{i}$ .   

<table><tr><td>Distrib.</td><td>Increasing</td><td>Random</td><td>Decreasing</td><td>Insertion</td><td>Pairwise</td></tr><tr><td>Unif(0,2μ)</td><td>0.20μ2n3σ2</td><td>0.33μ2n3σ2</td><td>0.53μ2n3σ2</td><td>2.6μ2n2σ2</td><td>2.7μ2n2σ2</td></tr><tr><td>Exp(μ)</td><td>0.13μ2n3σ2</td><td>0.33μ2n3σ2</td><td>0.63μ2n3σ2</td><td>2.6μ2n2σ2</td><td>4.0μ2n2σ2</td></tr></table>

summation methods is through statistical estimates of the error, which may be more representative of the average case. A statistical analysis of three summation methods has been given by Robertazzi and Schwartz [987, 1988] for the case of nonnegative $x_{i}$ . They assume that the relative errors in floating point addition are statistically independent and have zero mean and finite variance $\sigma^2$ . Two distributions of nonnegative $x_{i}$ are considered: the uniform distribution on $[0,2\mu ]$ , and the exponential distribution with mean $\mu$ . Making various simplifying assumptions Robertazzi and Schwartz estimate the mean square error (that is, the variance of the absolute error) of the computed sums from recursive summation with random, increasing, and decreasing orderings, and from insertion summation and pairwise summation (with the increasing ordering). Their results for the summation of $n$ numbers are given in Table 4.1.

The results show that for recursive summation the ordering affects only the constant in the mean square error, with the increasing ordering having the smallest constant and the decreasing ordering the largest; since the $x_{i}$ are nonnegative, this is precisely the ranking given by the rounding error bound (4.3). The insertion and pairwise summation methods have mean square errors proportional to $n^2$ rather than $n^3$ for recursive summation, and the insertion method has a smaller constant than pairwise summation. This is also consistent with the rounding error analysis, in which for nonnegative $x_{i}$ the insertion method satisfies an error bound no larger than pairwise summation and the latter method has an error bound with a smaller constant than for recursive summation $(\log_2 n$ versus $n$ ).

# 4.6. Choice of Method

There is a wide variety of summation methods to choose from. For each method the error can vary greatly with the data, within the freedom afforded by the error bounds; numerical experiments show that, given any two of the methods, data can be found for which either method is more accurate than the other [600, 1993]. However, some specific advice on the choice of method can be given.

1. If high accuracy is important, consider implementing recursive summation in higher precision; if feasible this may be less expensive (and more accurate) than using one of the alternative methods at the working precision. What can be said about the accuracy of the sum computed at higher precision? If $S_{n} = \sum_{i=1}^{n} x_{i}$ is computed by recursive summation at double precision (unit roundoff $u^2$ ) and then rounded to single precision, an error bound of the form $|S_{n} - \widehat{S}_{n}| \leq u |\widehat{S}_{n}| + nu^{2} \sum_{i=1}^{n} |x_{i}|$ holds. Hence a relative error of order $u$ is guaranteed if $nu \sum_{i=1}^{n} |x_{i}| \leq |S_{n}|$ . Priestest [955, 1992, pp. 62-

[63] shows that if the $x_{i}$ are sorted in decreasing order of magnitude before being summed in double precision, then $|S_{n} - \widehat{S}_{n}| \leq 2u|S_{n}|$ holds provided only that $n \leq \beta^{t-3}$ for $t$ -digit base $\beta$ arithmetic satisfying certain reasonable assumptions. Therefore the decreasing ordering may be worth arranging if there is a lot of cancellation in the sum. An alternative to extra precision computation is doubly compensated summation, which is the only other method described here that guarantees a small relative error in the computed sum.

2. For most of the methods the errors are, in the worst case, proportional to $n$ . If $n$ is very large, pairwise summation (error constant $\log_2 n$ ) and compensated summation (error constant of order 1) are attractive.   
3. If the $x_{i}$ all have the same sign then all the methods yield a relative error of at most $nu$ and compensated summation guarantees perfect relative accuracy (as long as $nu \leq 1$ ). For recursive summation of one-signed data, the increasing ordering has the smallest error bound (4.3) and the insertion method minimizes this error bound over all instances of Algorithm 4.1.   
4. For sums with heavy cancellation $(\sum_{i=1}^{n}|x_i| \gg |\sum_{i=1}^{n}x_i|)$ , recursive summation with the decreasing ordering is attractive, although it cannot be guaranteed to achieve the best accuracy.

Considerations of computational cost and the way in which the data are generated may rule out some of the methods. Recursive summation in the natural order, pairwise summation, and compensated summation can be implemented in $O(n)$ operations for general $x_{i}$ , but the other methods are more expensive since they require searching or sorting. Furthermore, in an application such as the numerical solution of ordinary differential equations, where $x_{k}$ is not known until $\sum_{i=1}^{k-1} x_{i}$ has been formed, sorting and searching may be impossible.

# 4.7. Notes and References

This chapter is based on Higham [600, 1993]. Analysis of Algorithm 4.1 can also be found in Espelid [394, 1995].

The earliest error analysis of summation is that of Wilkinson for recursive summation in [1228, 1960], [1232, 1963].

Pairwise summation was first discussed by McCracken and Dorn [833, 1964, pp. 61-63], Babuška [43, 1969], and Linz [792, 1970]. Caprani [203, 1971] shows how to implement the method on a serial machine using temporary storage of size $\lfloor \log_2 n \rfloor + 1$ (without overwriting the $x_i$ ).

The use of compensated summation with a Runge-Kutta formula is described by Vitasek [1198, 1969]. See also Butcher [189, 1987, pp. 118-120] and the experiments of Linnainmaa [788, 1974]. Davis and Rabinowitz [295, 1984, §4.2.1] discuss pairwise summation and compensated summation in the context of quadrature.

Demmel [319, 2001] analyses how much extra precision is needed in recursive summation with the (approximately) decreasing ordering in order to guarantee a computed result correct to working precision.

# Problems

4.1. Define and evaluate a condition number $C(x)$ for the summation $S_{n}(x) = \sum_{i=1}^{n} x_{i}$ . When does the condition number take the value 1?   
4.2. (Wilkinson [1232, 1963, p. 19]) Show that the bounds (4.3) and (4.4) are nearly attainable for recursive summation. (Hint: assume $u = 2^{-t}$ , set $n = 2^r$ ( $r \ll t$ ), and define

$$
x (1) = 1,
$$

$$
x (2) = 1 - 2 ^ {- t},
$$

$$
x (3: 4) = 1 - 2 ^ {1 - t},
$$

$$
x (5: 8) = 1 - 2 ^ {2 - t},
$$

：

$$
x \left(2 ^ {r - 1} + 1: 2 ^ {r}\right) = 1 - 2 ^ {r - 1 - t}.)
$$

4.3. Let $S_{n} = \sum_{i=1}^{n} x_{i}$ be computed by recursive summation in the natural order. Show that

$$
\widehat {S} _ {n} = \left(x _ {1} + x _ {2}\right) \left(1 + \theta_ {n - 1}\right) + \sum_ {i = 3} ^ {n} x _ {i} \left(1 + \theta_ {n - i + 1}\right), \quad \left| \theta_ {k} \right| \leq \gamma_ {k} = \frac {k u}{1 - k u},
$$

and hence that $E_{n} = \widehat{S}_{n} - S_{n}$ satisfies

$$
\left| E _ {n} \right| \leq \left(\left| x _ {1} \right| + \left| x _ {2} \right|\right) \gamma_ {n - 1} + \sum_ {i = 3} ^ {n} \left| x _ {i} \right| \gamma_ {n - i + 1}.
$$

Which ordering of the $x_{i}$ minimizes this bound?

4.4. Let $M$ be a floating point number so large that $fl(10 + M) = M$ . What are the possible values of $fl(\sum_{i=1}^{6} x_i)$ , where $\{x_i\}_{i=1}^6 = \{1, 2, 3, 4, M, -M\}$ and the sum is evaluated by recursive summation?   
4.5. The “ $\pm$ ” method for computing $S_{n} = \sum_{i=1}^{n} x_{i}$ is defined as follows: form the sum of the positive numbers, $S_{+}$ , and the sum of the nonpositive numbers, $S_{-}$ , separately, by any method, and then form $S_{n} = S_{-} + S_{+}$ . Discuss the pros and cons of this method.   
4.6. (Shewchuk [1038, 1997]) Consider correctly rounded binary arithmetic. Show that if $a$ and $b$ are floating point numbers then $\operatorname{err}(a, b) = a + b - fl(a + b)$ satisfies $|\operatorname{err}(a, b)| \leq \min(|a|, |b|)$ . Hence show that, barring overflow in $fl(a + b)$ , $\operatorname{err}(a, b)$ is a floating point number.   
4.7. Let $\{x_i\}$ be a convergent sequence with limit $\xi$ . Aitken's $\Delta^2$ -method (Aitken extrapolation) generates a transformed sequence $\{y_i\}$ defined by

$$
y _ {i} := x _ {i} - \frac {\left(x _ {i + 1} - x _ {i}\right) ^ {2}}{x _ {i + 2} - 2 x _ {i + 1} + x _ {i}}.
$$

Under suitable conditions (typically that $\{x_{i}\}$ is linearly convergent), the $y_{i}$ converge to $\xi$ faster than the $x_{i}$ . Which of the following expressions should be used to evaluate the denominator in the formula for $y_{i}$ ?

(a) $(x_{i + 2} - 2x_{i + 1}) + x_i$   
(b) $(x_{i + 2} - x_{i + 1}) - (x_{i + 1} - x_i)$   
(c) $(x_{i + 2} + x_i) - 2x_{i + 1}$

4.8. Analyse the accuracy of the following method for evaluating $S_{n} = \sum_{i=1}^{n} x_{i}$ :

$$
S _ {n} = \log \prod_ {i = 1} ^ {n} e ^ {x _ {i}}.
$$

4.9. In numerical methods for quadrature and for solving ordinary differential equation initial value problems it is often necessary to evaluate a function on an equally spaced grid of points on a range $[a, b]$ : $x_i := a + ih$ , $i = 0:n$ , where $h = (b - a) / n$ . Compare the accuracy of the following ways to form $x_i$ . Assume that $a$ and $b$ , but not necessarily $h$ , are floating point numbers.

(a) $x_{i} = x_{i - 1} + h\quad (x_{0} = a)$   
(b) $x_{i} = a + ih$   
(c) $x_{i} = a(1 - i / n) + (i / n)b.$

Note that (a) is typically used without comment in, for example, a Newton-Cotes quadrature rule or a Runge-Kutta method with fixed stepsize.

4.10. (RESEARCH PROBLEM) Priest [955, 1992, pp. 61-62] has proved that if $|x_1| \geq |x_2| \geq |x_3|$ then compensated summation computes the sum $x_1 + x_2 + x_3$ with a relative error of order $u$ (under reasonable assumptions on the arithmetic, such as the presence of a guard digit). He also gives the example

$$
x _ {1} = 2 ^ {t + 1}, \quad x _ {2} = 2 ^ {t + 1} - 2, \quad x _ {3} = x _ {4} = x _ {5} = x _ {6} = - (2 ^ {t} - 1),
$$

for which the exact sum is 2 but compensated summation computes 0 in IEEE single precision arithmetic ( $t = 24$ ). What is the smallest $n$ for which compensated summation applied to $x_{1},\ldots ,x_{n}$ ordered by decreasing absolute value can produce a computed sum with large relative error?
