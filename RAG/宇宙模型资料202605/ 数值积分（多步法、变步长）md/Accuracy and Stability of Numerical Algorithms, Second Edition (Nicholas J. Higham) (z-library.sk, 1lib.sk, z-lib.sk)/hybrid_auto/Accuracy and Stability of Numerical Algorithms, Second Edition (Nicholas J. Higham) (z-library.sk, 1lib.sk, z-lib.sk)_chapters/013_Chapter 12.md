# Chapter 12

# Iterative Refinement

The ILLIAC's memory is sufficient to accommodate a system of 39 equations

when used with Routine 51.

The additional length of Routine 100 restricts to 37

the number of equations that it can handle.

With 37 equations the operation time of Routine 100 is about

4 minutes per iteration.

— JAMES N. SNYDER, On the Improvement of the Solutions to a Set of

Simultaneous Linear Equations Using the ILLIAC (1955)

In a short mantissa computing environment

the presence of an iterative improvement routine can

significantly widen the class of solvable $Ax = b$ problems.

— GENE H. GOLUB and CHARLES F. VAN LOAN,

Matrix Computations (1996)

Most problems involve inexact input data and

obtaining a highly accurate solution to an

imprecise problem may not be justified.

— J. J. DONGARRA, J. R. BUNCH, C. B. MOLER, and G. W. STEWART,

LINPACK Users' Guide (1979)

It is shown that even a single iteration of

iterative refinement in single precision is enough to

make Gaussian elimination stable in a very strong sense.

— ROBERT D. SKEEL, Iterative Refinement Implies Numerical Stability

for Gaussian Elimination (1980)

Iterative refinement is an established technique for improving a computed solution $\widehat{x}$ to a linear system $Ax = b$ . The process consists of three steps:

1. Compute $r = b - A\hat{x}$   
2. Solve $Ad = r$ .   
3. Update $y = \widehat{x} + d$ .

(Repeat from step 1 if necessary, with $\widehat{x}$ replaced by $y$ .)

If there were no rounding errors in the computation of $r$ , $d$ , and $y$ , then $y$ would be the exact solution to the system. The idea behind iterative refinement is that if $r$ and $d$ are computed accurately enough then some improvement in the accuracy of the solution will be obtained. The economics of iterative refinement are favourable for solvers based on a factorization of $A$ , because the factorization used to compute $\widehat{x}$ can be reused in the second step of the refinement.

Traditionally, iterative refinement is used with Gaussian elimination (GE), and $r$ is computed in extended precision before being rounded to working precision. Iterative refinement for GE was used in the 1940s on desk calculators, but the first thorough analysis of the method was given by Wilkinson in 1963 [1232, 1963]. The behaviour of iterative refinement for GE is usually summarized as follows: if double the working precision is used in the computation of $r$ , and $A$ is not too ill conditioned, then the iteration produces a solution correct to working precision and the rate of convergence depends on the condition number of $A$ . In the next section we give a componentwise analysis of iterative refinement that confirms this summary and provides some further insight.

Iterative refinement is of interest not just for improving the accuracy or stability of an already stable linear system solver, but also for ameliorating instability in a less reliable solver. Examples of this usage are in Li and Demmel [786, 1998] and Dongarra, Eijkhout, and Luszczech [345, 2000], where sparse GE is performed without pivoting, for speed, and iterative refinement is used to regain stability.

# 12.1. Behaviour of the Forward Error

Let $A \in \mathbb{R}^{n \times n}$ be nonsingular and let $\widehat{x}$ be a computed solution to $Ax = b$ . Define $x_1 = \widehat{x}$ and consider the following iterative refinement process: $r_i = b - Ax_i$ (precision $\overline{u}$ ), solve $Ad_i = r_i$ (precision $u$ ), $x_{i+1} = x_i + d_i$ (precision $u$ ), $i = 1, 2, \ldots$ . For traditional iterative refinement, $\overline{u} = u^2$ . Note that in this chapter subscripts specify members of a vector sequence, not vector elements.

We henceforth define $r_i, d_i$ , and $x_i$ to be the computed quantities (to avoid a profusion of hats). The only assumption we will make on the solver is that the computed solution $\widehat{y}$ to a system $Ay = c$ satisfies

$$
(A + \Delta A) \widehat {x} = b, \quad | \Delta A | \leq u W, \tag {12.1}
$$

where $W$ is a nonnegative matrix depending on $A$ , $n$ , and $u$ (but not on $b$ ). Thus the solver need not be LU factorization or even a factorization method.

The page or so of analysis that follows is straightforward but tedious. The reader is invited to jump straight to (12.5), at least on first reading.

Consider first the computation of $r_i$ . There are two stages. First, $s_i = fl(b - Ax_i) = b - Ax_i + \Delta s_i$ is formed in the (possibly) extended precision $\overline{u}$ , so that $|\Delta s_i| \leq \overline{\gamma}_{n+1}(|b| + |A||x_i|)$ (cf. (3.11)), where $\overline{\gamma}_k \leq k\overline{u} / (1 - k\overline{u})$ . Second, the residual is rounded to the working precision: $r_i = fl(s_i) = s_i + f_i$ , where $|f_i| \leq u|s_i|$ . Hence

$$
r _ {i} = b - A x _ {i} + \Delta r _ {i}, \quad | \Delta r _ {i} | \leq u | b - A x _ {i} | + (1 + u) \bar {\gamma} _ {n + 1} (| b | + | A | | x _ {i} |).
$$

By writing $x_{i} = x + (x_{i} - x)$ , we obtain the bound

$$
\left| \Delta r _ {i} \right| \leq \left[ u + (1 + u) \bar {\gamma} _ {n + 1} \right] \left| A \| x - x _ {i} \right| + 2 (1 + u) \bar {\gamma} _ {n + 1} \left| A \| x \right|. \tag {12.2}
$$

For the second step we have, by (12.1), $(A + \Delta A_{i})d_{i} = r_{i}$ , where $|\Delta A_i| \leq uW$ . Now write

$$
\left(A + \Delta A _ {i}\right) ^ {- 1} = \left(A \left(I + A ^ {- 1} \Delta A _ {i}\right)\right) ^ {- 1} =: \left(I + F _ {i}\right) A ^ {- 1},
$$

where

$$
\left| F _ {i} \right| \leq u \left| A ^ {- 1} \right| W + O \left(u ^ {2}\right). \tag {12.3}
$$

Hence

$$
d _ {i} = \left(I + F _ {i}\right) A ^ {- 1} r _ {i} = \left(I + F _ {i}\right) \left(x - x _ {i} + A ^ {- 1} \Delta r _ {i}\right). \tag {12.4}
$$

For the last step,

$$
x _ {i + 1} = x _ {i} + d _ {i} + \Delta x _ {i},
$$

$$
\left| \Delta x _ {i} \right| \leq u \left| x _ {i} + d _ {i} \right| \leq u \left(\left| x - x _ {i} \right| + \left| x \right| + \left| d _ {i} \right|\right).
$$

Using (12.4) we have

$$
x _ {i + 1} - x = F _ {i} \left(x - x _ {i}\right) + \left(I + F _ {i}\right) A ^ {- 1} \Delta r _ {i} + \Delta x _ {i}.
$$

Hence

$$
\begin{array}{l} \left| x _ {i + 1} - x \right| \leq \left| F _ {i} \right| \left| x - x _ {i} \right| + \left(I + \left| F _ {i} \right|\right) \left| A ^ {- 1} \right| \left| \Delta r _ {i} \right| + u \left| x - x _ {i} \right| + u \left| x \right| + u \left| d _ {i} \right| \\ \leq | F _ {i} | | x - x _ {i} | + (I + | F _ {i} |) | A ^ {- 1} | | \Delta r _ {i} | + u | x - x _ {i} | + u | x | \\ + u (I + | F _ {i} |) \left(| x - x _ {i} | + | A ^ {- 1} | \Delta r _ {i} |\right) \\ = \left((1 + u) \left| F _ {i} \right| + 2 u I\right) \left| x - x _ {i} \right| + (1 + u) \left(I + \left| F _ {i} \right|\right) \left| A ^ {- 1} \right| \left| \Delta r _ {i} \right| + u | x |. \\ \end{array}
$$

Substituting the bound for $|\varDelta r_i|$ from (12.2) gives

$$
\begin{array}{l} \left| x _ {i + 1} - x \right| \leq \bigl (\left(1 + u\right) \left| F _ {i} \right| + 2 u I \bigr) \left| x - x _ {i} \right| \\ + (1 + u) \left(u + (1 + u) \bar {\gamma} _ {n + 1}\right) \left(I + | F _ {i} |\right) | A ^ {- 1} | | A | | x - x _ {i} | \\ + 2 (1 + u) ^ {2} \bar {\gamma} _ {n + 1} (I + | F _ {i} |) | A ^ {- 1} | | A | | x | + u | x | \\ =: G _ {i} \left| x - x _ {i} \right| + g _ {i}. \tag {12.5} \\ \end{array}
$$

Using (12.3), we estimate

$$
\begin{array}{l} G _ {i} \approx | F _ {i} | + (u + \bar {\gamma} _ {n + 1}) (I + | F _ {i} |) | A ^ {- 1} | | A | \\ \lesssim u | A ^ {- 1} | W + (u + \bar {\gamma} _ {n + 1}) (I + u | A ^ {- 1} | W) | A ^ {- 1} | | A |, \\ g _ {i} \approx 2 \bar {\gamma} _ {n + 1} (I + | F _ {i} |) | A ^ {- 1} | | A | | x | + u | x | \\ \lesssim 2 \overline {{\gamma}} _ {n + 1} (I + u | A ^ {- 1} | W) | A ^ {- 1} | | A | | x | + u | x |. \\ \end{array}
$$

As long as $A$ is not too ill conditioned and the solver is not too unstable, we have $\| G_i\|_{\infty} < 1$ , which means that the error contracts until we reach a point at which the $g_i$ term becomes significant. The limiting normwise accuracy, that is, the minimum size of $\| x - x_i\|_{\infty} / \| x\|_{\infty}$ , is roughly $\| g_i\|_{\infty} / \| x\|_{\infty} \approx 2n\overline{u}\operatorname{cond}(A,x) + u$ . Moreover, if $2n\overline{u} (I + u|A^{-1}|W)|A^{-1}||A||x|\leq \mu u|x|$ for some $\mu$ , then we can expect to obtain a componentwise relative error of order $\mu u$ , that is, $\min_i |x - x_i| \lesssim \mu u|x|$ . Note that $G_i$ is essentially independent of $\overline{u}$ , which suggests that the rate of convergence of mixed and fixed precision iterative refinement will be similar; it is only the limiting accuracy that differs.

In the traditional use of iterative refinement, $\overline{u} = u^2$ , and one way to summarize our findings is as follows.

Theorem 12.1 (mixed precision iterative refinement). Let iterative refinement be applied to the nonsingular linear system $A x = b$ , using a solver satisfying (12.1) and with residuals computed in double the working precision. Let $\eta = u \| |A^{-1}|(|A| + W) \|_{\infty}$ . Then, provided $\eta$ is sufficiently less than 1, iterative refinement reduces the forward error by a factor approximately $\eta$ at each stage, until $\| x - \widehat{x}_i \|_{\infty} / \| x \|_{\infty} \approx u$ .

For LU factorization, Theorem 9.4 shows that we can take

$$
u W \equiv \gamma_ {3 n} | \widehat {L} | | \widehat {U} |, \tag {12.6}
$$

where $\widehat{L}$ and $\widehat{U}$ are the computed LU factors. In this case Theorem 12.1 is stronger than the standard results in the literature, which have $\kappa_{\infty}(A)u$ in place of $\eta \approx u\| |A^{-1}(|A| + 3n|\widehat{L} ||\widehat{U} |)\|_{\infty}$ . We can have $\eta \ll \kappa_{\infty}(A)u$ , since $\eta$ is independent of the row scaling of $A$ (as long as the scaling does not cause changes in the pivot sequence). For example, if $|\widehat{L} ||\widehat{U} |\approx |A|$ then $\eta \approx 3n\mathrm{cond}(A)u$ , and $\mathrm{cond}(A)$ can be arbitrarily smaller than $\kappa_{\infty}(A)$ .

Consider now the case where $\overline{u} = u$ , which is called fixed precision iterative refinement. We have an analogue of Theorem 12.1.

Theorem 12.2 (fixed precision iterative refinement). Let iterative refinement in fixed precision be applied to the nonsingular linear system $Ax = b$ of order $n$ , using a solver satisfying (12.1). Let $\eta = u\| |A^{-1}|(|A| + W)\|_{\infty}$ . Then, provided $\eta$ is sufficiently less than 1, iterative refinement reduces the forward error by a factor approximately $\eta$ at each stage, until $\| x - \widehat{x}_i\|_{\infty} / \| x\|_{\infty}\lesssim 2n\operatorname {cond}(A,x)u$ .

The key difference between mixed and fixed precision iterative refinement is that in the latter case a relative error of order $u$ is no longer ensured. But we do have a relative error bound of order $\operatorname{cond}(A, x)u$ . This is a stronger bound than holds for the original computed solution $\widehat{x}$ , for which we can say only that

$$
\frac {\| x - \widehat {x} \| _ {\infty}}{\| x \| _ {\infty}} \lesssim u \frac {\| | A ^ {- 1} | W | x | \| _ {\infty}}{\| x \| _ {\infty}}.
$$

In fact, a relative error bound of order $\operatorname{cond}(A,x)u$ is the best we can possibly expect if we do not use higher precision, because it corresponds to the uncertainty introduced by making componentwise relative perturbations to $A$ of size $u$ (see

Theorem 7.4); this level of uncertainty is usually present, because of errors in computing $A$ or in rounding its elements to floating point form.

The gist of this discussion is that iterative refinement is beneficial even if residuals are computed only at the working precision. This fact became widely appreciated only after the publication of Skeel's 1980 paper [1041, 1980]. One reason for the delayed appreciation may be that comments such as that made by Forsythe and Moler, "It is absolutely essential that the residuals $r_k$ be computed with a higher precision than that of the rest of the computation" [431, 1967, p. 49], were incorrectly read to mean that without the use of higher precision no advantage at all could be obtained from iterative refinement. In the next section we will see that fixed precision iterative refinement does more than just produce a cond $(A, x)$ $u$ -bounded forward error for LU factorization—it brings componentwise backward stability as well.

# 12.2. Iterative Refinement Implies Stability

We saw in the last section that fixed precision iterative refinement can improve the accuracy of a computed solution to $Ax = b$ . The question arises of what the refinement process does to the backward error. To answer this question we give a general backward error analysis that is applicable to a wide class of linear equation solvers. Throughout this section, "iterative refinement" means fixed precision iterative refinement.

We assume that the computed solution $\widehat{x}$ to $Ax = b$ satisfies

$$
\left| b - A \widehat {x} \right| \leq u \big (g (A, b) | \widehat {x} | + h (A, b) \big), \tag {12.7}
$$

where $g: \mathbb{R}^{n \times (n + 1)} \to \mathbb{R}^{n \times n}$ and $h: \mathbb{R}^{n \times (n + 1)} \to \mathbb{R}^n$ have nonnegative entries. The functions $g$ and $h$ may depend on $n$ and $u$ as well as on the data $A$ and $b$ . We also assume that the residual $r = b - A\widehat{x}$ is computed in such a way that

$$
\left| \widehat {r} - r \right| \leq u t (A, b, \widehat {x}), \tag {12.8}
$$

where $t: \mathbb{R}^{n \times (n + 2)} \to \mathbb{R}^n$ is nonnegative. If $r$ is computed in the conventional way, then we can take

$$
t (A, b, \widehat {x}) = \frac {\gamma_ {n + 1}}{u} (| A | | \widehat {x} | + | b |). \tag {12.9}
$$

First we give an asymptotic result that does not make any further assumptions on the linear equation solver.

Theorem 12.3. Let $A \in \mathbb{R}^{n \times n}$ be nonsingular. Suppose the linear system $Ax = b$ is solved in floating point arithmetic using a solver $S$ together with one step of iterative refinement. Assume that the computed solution $\widehat{x}$ produced by $S$ satisfies (12.7) and that the computed residual $\widehat{r}$ satisfies (12.8). Then the corrected solution $\widehat{y}$ satisfies

$$
| b - A \widehat {y} | \leq u (h (A, \widehat {r}) + t (A, b, \widehat {y}) + | A | | \widehat {y} |) + u q, \tag {12.10}
$$

where $q = O(u)$ if $t(A,b,\widehat{x}) - t(A,b,\widehat{y}) = O(\| \widehat{x} -\widehat{y}\|_{\infty})$

Proof. The residual $r = b - A\widehat{x}$ of the original computed solution $\widehat{x}$ satisfies

$$
\left| r \right| \leq u (g (A, b) | \widehat {x} | + h (A, b)). \tag {12.11}
$$

The computed residual is $\widehat{r} = r + \varDelta r$ , where $|\varDelta r|\leq ut(A,b,\widehat{x})$ . The computed correction $\widehat{d}$ satisfies

$$
A \widehat {d} = \widehat {r} + f _ {1}, \quad | f _ {1} | \leq u (g (A, \widehat {r}) | \widehat {d} | + h (A, \widehat {r})). \tag {12.12}
$$

Finally, for the corrected solution we have

$$
\widehat {y} = f l (\widehat {x} + \widehat {d}) = \widehat {x} + \widehat {d} + f _ {2}, \quad | f _ {2} | \leq u (| \widehat {x} | + | \widehat {d} |). \tag {12.13}
$$

Collecting together the above results we obtain

$$
b - A \widehat {y} = b - A \widehat {x} - A \widehat {d} - A f _ {2} = \widehat {r} - \Delta r - A \widehat {d} - A f _ {2} = - f _ {1} - \Delta r - A f _ {2}.
$$

Hence

$$
\begin{array}{l} \left| b - A \widehat {y} \right| \leq u \left(g (A, \widehat {r}) | \widehat {d} | + h (A, \widehat {r})\right) + u t (A, b, \widehat {x}) + u | A | \left(| \widehat {x} | + | \widehat {d} |\right) \tag {12.14} \\ = u \left(h (A, \widehat {r}) + t (A, b, \widehat {y}) + | A | | \widehat {y} |\right) + u q, \\ \end{array}
$$

where

$$
q = t (A, b, \widehat {x}) - t (A, b, \widehat {y}) + g (A, \widehat {r}) | \widehat {d} | + | A | (| \widehat {x} | - | \widehat {y} | + | \widehat {d} |).
$$

The claim about the order of $q$ follows since $\widehat{x} - \widehat{y}$ , $|\widehat{x}| - |\widehat{y}|$ , and $\widehat{d}$ are all of order $u$ .

Theorem 12.3 shows that, to first order, the componentwise relative backward error $\omega_{|A|,|b|}$ will be small after one step of iterative refinement as long as $h(A,\widehat{r})$ and $t(A,b,\widehat{y})$ are bounded by a modest scalar multiple of $|A||\widehat{y}| + |b|$ . This is true for $t$ if the residual is computed in the conventional way (see (12.9)), and in some cases we may take $h\equiv 0$ , as shown below. Note that the function $g$ of (12.7) does not appear in the first-order term of (12.10). This is the essential reason why iterative refinement improves stability: potential instability manifested in $g$ is suppressed by the refinement stage.

A weakness of Theorem 12.3 is that the bound (12.10) is asymptotic. Since a strict bound for $q$ is not given, it is difficult to draw firm conclusions about the size of $\omega_{|A|,|b|}$ . The next result overcomes this drawback, at the cost of some specialization (and a rather long proof).

We introduce a measure of ill scaling of the vector $|B||x|$ ,

$$
\sigma (B, x) = \frac {\operatorname* {m a x} _ {i} (| B | | x |) _ {i}}{\operatorname* {m i n} _ {i} (| B | | x |) _ {i}}.
$$

Theorem 12.4. Under the conditions of Theorem 12.3, suppose that $g(A,b) = G|A|$ and $h(A,b) = H|b|$ , where $G, H \in \mathbb{R}^{n \times n}$ have nonnegative entries, and that the residual is computed in the conventional manner. Then there is a function

$$
f \left(t _ {1}, t _ {2}\right) \approx \left(t _ {2} \left(t _ {1} + n + 1\right) / \operatorname {c o n d} \left(A ^ {- 1}\right) + 2 \left(t _ {1} + n + 2\right) ^ {2} \left(1 + u t _ {2}\right) ^ {2}\right) / (n + 1)
$$

such that if

$$
\operatorname {c o n d} (A ^ {- 1}) \sigma (A, \widehat {y}) \leq \left(f (\| G \| _ {\infty}, \| H \| _ {\infty}) u\right) ^ {- 1}
$$

then

$$
| b - A \widehat {y} | \leq 2 \gamma_ {n + 1} | A | | \widehat {y} |.
$$

Proof. As with the analysis in the previous section, this proof can be skipped without any real loss of understanding. From (12.14) in the proof of Theorem 12.3, using the formula (12.9) for $t$ , we have

$$
\left| b - A \hat {y} \right| \leq u H | \hat {r} | + \gamma_ {n + 1} | b | + \left(\gamma_ {n + 1} + u\right) | A | | \hat {x} | + u (I + G) | A | | \hat {d} |. \tag {12.15}
$$

The inequality (12.11) implies

$$
| b | - | A | | \widehat {x} | \leq | b - A \widehat {x} | \leq u (G | A | | \widehat {x} | + H | b |),
$$

or $(I - uH)|b| \leq (I + uG)|A||\widehat{x}|$ . If $u\| H\|_{\infty} < 1/2$ (say) then $I - uH$ is nonsingular with a nonnegative inverse satisfying $\|(I - uH)^{-1}\|_{\infty} \leq 2$ and we can solve for $|b|$ to obtain $|b| \leq (I - uH)^{-1}(I + uG)|A||\widehat{x}|$ . It follows from this relation and consideration of the rest of the proof that the simplifying step of replacing $b$ by 0 in the analysis has little effect on the bounds—it merely produces unimportant perturbations in $f$ in the statement of the theorem. Making this replacement in (12.15) and approximating $\gamma_{n+1} + u \approx \gamma_{n+1}$ , we have

$$
\left| b - A \widehat {y} \right| \leq u H | \widehat {r} | + \gamma_ {n + 1} | A | | \widehat {x} | + u (I + G) | A | | \widehat {d} |. \tag {12.16}
$$

Our task is now to bound $|A||\widehat{x}|, |\widehat{r}|$ , and $|A||\widehat{d}|$ in terms of $|\widehat{y}|$ . By manipulating (12.13) we obtain the inequality

$$
| \widehat {x} | \leq (1 - u) ^ {- 1} \left(| \widehat {y} | + (1 + u) | \widehat {d} |\right) \approx | \widehat {y} | + | \widehat {d} |. \tag {12.17}
$$

Also, we can bound $|\widehat{r}|$ by

$$
\left| \widehat {r} \right| \leq \left| r \right| + \left| \Delta r \right| \leq u \left(G | A | | \widehat {x} | + H | b |\right) + \gamma_ {n + 1} \left(| A | | \widehat {x} | + | b |\right),
$$

and dropping the $|b|$ terms and using (12.17) gives

$$
| \widehat {r} | \leq (u G + \gamma_ {n + 1} I) | A | | \widehat {x} | \leq (u G + \gamma_ {n + 1} I) | A | (\left| \widehat {y} \right| + \left| \widehat {d} \right|). \tag {12.18}
$$

Substituting from (12.17) and (12.18) into (12.16) we find

$$
\begin{array}{l} | b - A \widehat {y} | \leq (\gamma_ {n + 1} I + u H (u G + \gamma_ {n + 1} I)) | A | | \widehat {y} | \\ + \left(\gamma_ {n + 1} I + u (I + G) + u H \left(u G + \gamma_ {n + 1} I\right)\right) | A | | \widehat {d} | \\ =: \left(\gamma_ {n + 1} I + M _ {1}\right) | A | | \widehat {y} | + M _ {2} | A | | \widehat {d} |, \tag {12.19} \\ \end{array}
$$

where

$$
\begin{array}{l} \left\| M _ {1} \right\| _ {\infty} \leq u \| H \| _ {\infty} \left(u \| G \| _ {\infty} + \gamma_ {n + 1}\right), \\ \| M _ {2} \| _ {\infty} \leq \gamma_ {n + 2} + u \| G \| _ {\infty} + u \| H \| _ {\infty} (u \| G \| _ {\infty} + \gamma_ {n + 1}). \\ \end{array}
$$

Now from (12.12), making use of (12.18),

$$
\begin{array}{l} | \widehat {d} | \leq | A ^ {- 1} | (| \widehat {r} | + u G | A | | \widehat {d} | + u H | \widehat {r} |) \\ \leq | A ^ {- 1} | \bigl ((I + u H) (u G + \gamma_ {n + 1} I) | A | (| \widehat {y} | + | \widehat {d} |) + u G | A | | \widehat {d} | \bigr). \\ \end{array}
$$

After premultiplying by $|A|$ this may be rearranged as

$$
\left. (I - u M _ {3}) | A | \mid \widehat {d} \right| \leq u | A | | A ^ {- 1} | M _ {4} | A | | \widehat {y} |, \tag {12.20}
$$

where

$$
\begin{array}{l} M _ {3} = | A | | A ^ {- 1} | \big ((I + u H) (G + (\gamma_ {n + 1} / u) I) + G \big), \\ M _ {4} = (I + u H) (G + (\gamma_ {n + 1} / u) I). \\ \end{array}
$$

Using $\gamma_{n + 1} / u\leq (n + 1) / (1 - (n + 1)u)\approx n + 1$ , we have the bounds

$$
\begin{array}{l} \left\| M _ {3} \right\| _ {\infty} \leq \operatorname {c o n d} \left(A ^ {- 1}\right) \left(\left\| G \right\| _ {\infty} + n + 1\right) \left(2 + u \| H \| _ {\infty}\right), \\ \| M _ {4} \| _ {\infty} \leq (\| G \| _ {\infty} + n + 1) (1 + u \| H \| _ {\infty}). \\ \end{array}
$$

If $u\| M_3\|_{\infty} < 1/2$ (say) then $(I - uM_3)^{-1} \geq 0$ with $\|(I - uM_3)^{-1}\|_{\infty} \leq 2$ and we can rewrite (12.20) as

$$
| A | | \widehat {d} | \leq u (I - u M _ {3}) ^ {- 1} | A | | A ^ {- 1} | M _ {4} | A | | \widehat {y} |. \tag {12.21}
$$

Substituting this bound into (12.19) we obtain

$$
\begin{array}{l} | b - A \hat {y} | \leq \left(\gamma_ {n + 1} I + M _ {1} + u M _ {2} (I - u M _ {3}) ^ {- 1} | A | | A ^ {- 1} | M _ {4}\right) | A | | \hat {y} | \tag {12.22} \\ =: \left(\gamma_ {n + 1} I + M _ {5}\right) | A | | \widehat {\mathcal {Y}} | \\ \leq \left(\gamma_ {n + 1} + \| M _ {5} \| _ {\infty} \sigma (A, \hat {y})\right) | A | | \hat {y} | \\ \end{array}
$$

(see Problem 12.1). Finally, we bound $\| M_5\|_{\infty}$ . Writing $g = \| G\|_{\infty}$ , $h = \| H\|_{\infty}$ , we have

$$
\begin{array}{l} \left\| M _ {5} \right\| _ {\infty} \leq u ^ {2} g h + u h \gamma_ {n + 1} + 2 u \left(\gamma_ {n + 2} + u g + u ^ {2} g h + u h \gamma_ {n + 1}\right) \\ \times \operatorname {c o n d} (A ^ {- 1}) (g + n + 1) (1 + u h) \\ \end{array}
$$

and this expression is approximately bounded by $u^2 \big( h(g + n + 1) + 2(g + n + 2)^2 (1 + uh)^2 \operatorname{cond}(A^{-1}) \big)$ . Requiring $\| M_5 \|_{\infty} \sigma(A, \widehat{y})$ not to exceed $\gamma_{n+1}$ leads to the result.

Theorem 12.4 says that as long as $A$ is not too ill conditioned, $|A||\widehat{y}|$ is not too badly scaled (cond $(A^{-1})\sigma(A, \widehat{y})$ is not too large), and the solver is not too unstable ( $f(\|G\|_{\infty}, \|H\|_{\infty})$ is not too large), then $\omega_{|A|,|\widehat{b}|} \leq 2\gamma_{n+1}$ after one step of iterative refinement. Note that the term $\gamma_{n+1}|A||\widehat{y}|$ in (12.22) comes from the error bound for evaluation of the residual, so this bound for $\omega$ is about the smallest we could expect to prove.

Let us apply Theorem 12.4 to GE with or without pivoting. If there is pivoting, assume (without loss of generality) that no interchanges are required. Theorem 9.4 shows that we can take

$$
g (A, b) \approx 3 n | \widehat {L} | | \widehat {U} |, \quad h (A, b) = 0,
$$

Table 12.1. $\omega_{|A|,|b|}$ values for $A =$ gallery('orthog',25).   

<table><tr><td colspan="3">cond(A-1)σ(A,x) = 3.0e1</td></tr><tr><td colspan="3">cond(A) = 2.1e1, κ∞(A) = 2.1e1</td></tr><tr><td>GEPP</td><td>GE</td><td>QR</td></tr><tr><td>3.5e-16</td><td>4.4e-7</td><td>3.4e-16</td></tr><tr><td>2.2e-16</td><td>7.2e-14</td><td>2.1e-16</td></tr><tr><td></td><td>1.6e-16</td><td></td></tr></table>

where $\widehat{L}, \widehat{U}$ are the computed LU factors of $A$ . To apply Theorem 12.4 we use $A \approx \widehat{L} \widehat{U}$ and write

$$
g (A, b) \approx 3 n | \widehat {L} | | \widehat {L} ^ {- 1} A | \leq 3 n | \widehat {L} | | \widehat {L} ^ {- 1} | | A |,
$$

which shows that we can take

$$
G = 3 n | \widehat {L} | | \widehat {L} ^ {- 1} |, \qquad f (\| G \| _ {\infty}, \| H \| _ {\infty}) \approx 1 8 n \| | \widehat {L} | | \widehat {L} ^ {- 1} | \| _ {\infty} ^ {2}.
$$

Without pivoting the growth factor-type term $\| |\widehat{L} ||\widehat{L}^{-1}|\|_{\infty}$ is unbounded, but with partial pivoting it cannot exceed $2^{n}$ and is typically $O(n)$ [1157, 1990].

We can conclude that, for GE with partial pivoting (GEPP), one step of iterative refinement will usually be enough to yield a small componentwise relative backward error as long as $A$ is not too ill conditioned and $|A||\widehat{y}|$ is not too badly scaled. Without pivoting the same holds true with the added proviso that the computation of the original $\widehat{x}$ must not be too unstable.

One interesting problem remains: to reconcile Theorem 12.4 with Theorem 12.2. Under the conditions of Theorem 12.4 the componentwise relative backward error is small after one step of iterative refinement, so the forward error is certainly bounded by a multiple of $\operatorname{cond}(A,x)u$ . How can this be shown (for GE) using the analysis of §12.1? An explanation is nontrivial—see Problem 12.2.

We will see applications of Theorems 12.3 and 12.4 to other types of linear equation solver in Chapters 19, 20, and 22.

Tables 12.1-12.3 show the performance of fixed precision iterative refinement for GE without pivoting, GEPP, and Householder QR factorization (see §19.7). The matrices are as follows: **gallery** ('clement') is tridiagonal with zero diagonal entries, **gallery** ('orthog') is a symmetric and orthogonal matrix, and **gfpp** (from the Matrix Computation Toolbox) is a matrix for which the growth factor for GEPP is maximal. In each case the right-hand side $b$ was chosen as a random vector from the uniform distribution on [0, 1]. We report the componentwise relative backward errors for the initial solution and the refined iterates (refinement was terminated when $\omega_{|A|,|b|}(\widehat{y}) \leq 2u$ ). GEPP performs as predicted by both our and Skeel's analyses. In fact, iterative refinement converges in one step even when $\theta(A,x) := \mathrm{cond}(A^{-1})\sigma(A,x)$ exceeds $u^{-1}$ in the examples reported and in most others we have tried. GE also achieves a small componentwise relative backward error, but can require more than one refinement step, even when $\theta(A,x)$ is small.

Table 12.2. ${\omega }_{\left| A\right| ,\left| b\right| }$ values for $A =$ gallery('clement',50).

$\operatorname{cond}(A^{-1})\sigma(A,x) = 1.2\mathrm{e}15$ $\operatorname{cond}(A) = 1.4\mathrm{e}6, \kappa_{\infty}(A) = 3.5\mathrm{e}7$ $\frac{\text{GEPP}}{1.0\mathrm{e}-16} \quad \begin{array}{c}\text{GE} \\ \text{Fail} \end{array} \quad \begin{array}{c}\text{QR} \\ 4.9\mathrm{e}-9 \\ 1.7\mathrm{e}-16 \end{array}$

Table 12.3. $\omega_{|A|,|b|}$ values for $A = \mathbf{gfpp}(50)$ .

$\operatorname{cond}(A^{-1})\sigma(A,x) = 4.9\mathrm{e}2$ $\operatorname{cond}(A) = 50, \kappa_{\infty}(A) = 50$ GEPP GE QR  
1.7e-3 1.8e-3 1.8e-15  
5.5e-17 5.5e-17 7.0e-17

# 12.3. Notes and References

Wilkinson [1232, 1963] gave a detailed analysis of iterative refinement in a kind of scaled fixed point arithmetic called block-floating arithmetic. Moler [859, 1967] extended the analysis to floating point arithmetic. Very readable analyses of iterative refinement are given in the books by Forsythe and Moler [431, 1967, §22] and Stewart [1065, 1973, §4.5].

As we mentioned in §9.14, as early as 1948 Wilkinson had written a program for the ACE to do GEPP and iterative refinement. Other early implementations of iterative refinement are in a code for the University of Illinois' ILLIAC by Snyder [1055, 1955], the Algol code of McKeeman [836, 1962], and the Algol codes in the Handbook [154, 1966], [817, 1966]. Some of the machines for which these codes were intended could accumulate inner products in extended precision, and so were well suited to mixed precision iterative refinement.

Interest in fixed precision iterative refinement was sparked by two papers that appeared in the late 1970s. Jankowski and Wozniakowski [671, 1977] proved that an arbitrary linear equation solver is made normwise backward stable by the use of fixed precision iterative refinement, as long as the solver is not too unstable to begin with and $A$ is not too ill conditioned. Skeel [1041, 1980] analysed iterative refinement for GEPP and showed that one step of refinement yields a small componentwise relative backward error, as long as $\operatorname{cond}(A^{-1})\sigma(A,x)$ is not too large.

The analysis in §12.1 is from Higham [607, 1997] and that in §12.2 is from Higham [596, 1991].

The results for GE in §12.2 are very similar to those of Skeel [1041, 1980]. The main differences are that Skeel's analysis covers an arbitrary number of refinement steps with residuals computed at working or double the working precision, his analysis is specific to GE, and his results involve $\sigma(A, x)$ rather than $\sigma(A, \widehat{y})$ .

The most general backward error results for iterative refinement are those of

Higham [607, 1997], which apply to an arbitrary solver over an arbitrary number of refinement steps with residuals computed at working or extended precision. The analysis in [607] suggests that, as for the forward error, the rate of reduction of the componentwise relative backward error is approximately the same for both fixed and mixed precision refinement.

The quantity $\sigma(A, x)$ appearing in Theorem 12.4 can be interpreted as follows. Consider a linear system $Ax = b$ for which $(|A||x|)_i = 0$ for some $i$ . While the componentwise relative backward error $\omega_{|A|, |b|}(x)$ of the exact solution $x$ is zero, an arbitrarily small change to a component $x_j$ where $a_{ij} \neq 0$ yields $\omega_{|A|, |b|}(x + \Delta x) \geq 1$ . Therefore solving $Ax = b$ to achieve a small componentwise relative backward error can be regarded as an ill-posed problem when $|A||x|$ has a zero component. The quantity $\sigma(A, x)$ reflects this ill-posedness because it is large when $|A||x|$ has a relatively small component.

For a lucid survey of both fixed and mixed precision iterative refinement and their applications, see Björck [123, 1990]. For particular applications of fixed precision iterative refinement see Govaerts [515, 2000], Govaerts and Pryce [514, 1990], and Jankowski and Wozniakowski [672, 1985].

By increasing the precision from one refinement iteration to the next it is possible to compute solutions to arbitrarily high accuracy, an idea first suggested by Stewart in an exercise [1065, 1973, pp. 206-207]. For algorithms, see Kielbasiński [732, 1981] and Smoktunowicz and Sokolnicka [1054, 1984].

In the past, mixed precision iterative refinement could not be implemented in a portable way when the working precision was already the highest precision supported by a compiler. This is the main reason why iterative refinement is not supported in LINPACK. (The LINPACK manual lists a subroutine that implements mixed precision iterative refinement for single precision data, but it is not part of LINPACK [341, 1979, pp. 1.8-1.10].) However, with the release of the Extended and Mixed Precision BLAS (see §27.10) and the portable reference implementation for IEEE arithmetic, and with the ubiquity of IEEE arithmetic, portable mixed precision iterative refinement is now achievable.

Two important practical issues when implementing iterative refinement concern storage and convergence. For either form of refinement, a copy of the matrix $A$ needs to be kept in order to form the residual, and this necessitates an extra $n^2$ elements of storage. A test for terminating the refinement is needed. In addition to revealing when convergence has been achieved, it must signal lack of (sufficiently fast) convergence, which may certainly be experienced when $A$ is very ill conditioned. In the LAPACK driver xGESVX for LU factorization with partial pivoting, fixed precision iterative refinement is terminated if the componentwise relative backward error $\omega = \omega_{|A|,|b|}(\widehat{x}_i)$ satisfies

1. $\omega \leq u$   
2. $\omega$ has not decreased by a factor of at least 2 during the current iteration, or   
3. five iterations have been performed.

These criteria were chosen to be robust in the face of different BLAS implementations and machine arithmetics. In an implementation of mixed precision iterative refinement it is more natural to test for convergence of the sequence $\{\widehat{x}_i\}$ , with a

test such as $\| \widehat{x}_i - \widehat{x}_{i-1} \|_{\infty} / \| \widehat{x}_i \|_{\infty} \leq u$ (see, e.g., Forsythe and Moler [431, 1967, p. 65]). However, if $A$ is so ill conditioned that Theorem 12.1 is not applicable, the sequence $\widehat{x}_i$ could converge to a vector other than the solution. This behaviour is very unlikely, and Kahan [687, 1966] quotes a "prominent figure in the world of error-analysis" as saying "Anyone unlucky enough to encounter this sort of calamity has probably already been run over by a truck."

A by-product of extended precision iterative refinement is an estimate of the condition number. Since the error decreases by a factor approximately $\eta = u\| |A^{-1}||\widehat{L} ||\widehat{U} ||_{\infty}$ on each iteration for LU factorization (Theorem 12.1), the relative change in $x$ on the first iteration should be about $\eta$ , that is, $\| d_1\|_{\infty} / \| \widehat{x}\|_{\infty}\approx \eta \approx \kappa_{\infty}(A)u$ . Now that reliable and inexpensive condition estimators are available (Chapter 15) this rough estimate is less important.

An unusual application of iterative refinement is to fault-tolerant computing. Boley et al. [148, 1994] propose solving $Ax = b$ by GEPP or QR factorization, performing one step of fixed precision iterative refinement and then testing whether the a priori residual bound in Theorem 12.4 is satisfied. If the bound is violated then a hardware fault may have occurred and special action is taken.

# 12.3.1. LAPACK

Iterative refinement is carried out by routines whose names end -RFS, and these routines are called by the expert drivers (name ending -SVX). Iterative refinement is available for all the standard matrix types except triangular matrices, for which the original computed solution already has a componentwise relative backward error of order $u$ . As an example, the expert driver xGESVX uses LU factorization with partial pivoting and fixed precision iterative refinement to solve a general system of linear equations with multiple right-hand sides, and the refinement is actually carried out by the routine xGERFS.

# Problems

12.1. Show that for $A \in \mathbb{R}^{m \times n}$ and $x \in \mathbb{R}^n$ , $|A||x| \leq \sigma \| A\|_{\infty}|x|$ , where $\sigma = \max_i |x_i| / \min_i |x_i|$ .   
12.2. Use the analysis of §12.1 to show that, under the conditions of Theorem 12.4, $\| x - \widehat{x}_2 \|_{\infty} / \| x \|_{\infty}$ is bounded by a multiple of $\operatorname{cond}(A, x) u$ for GEPP after one step of fixed precision iterative refinement.   
12.3. Investigate empirically the size of $\| |L||L^{-1}|\|_{\infty}$ for $L$ from GEPP.   
12.4. (Demmel and Higham [324, 1992]) Suppose GEPP with fixed precision iterative refinement is applied to the multiple right-hand side system $AX = B$ , and that refinement of the columns of $X$ is done "in parallel": $R = B - AX$ , $AD = R$ , $Y = X + D$ . What can be said about the stability of the process if $R$ is computed by conventional multiplication but the second step is done using a fast multiplication technique for which only (13.4) holds?   
12.5. (RESEARCH PROBLEM [607, 1997]) Is one step of fixed precision iterative refinement sufficient to produce a componentwise relative backward error of order $u$

for Cholesky factorization applied to a symmetric positive definite system $Ax = b$ , assuming $\operatorname{cond}(A^{-1})\sigma(A, x)$ is not too large? Answer the same question for the diagonal pivoting method with partial pivoting applied to a symmetric system $Ax = b$ .
