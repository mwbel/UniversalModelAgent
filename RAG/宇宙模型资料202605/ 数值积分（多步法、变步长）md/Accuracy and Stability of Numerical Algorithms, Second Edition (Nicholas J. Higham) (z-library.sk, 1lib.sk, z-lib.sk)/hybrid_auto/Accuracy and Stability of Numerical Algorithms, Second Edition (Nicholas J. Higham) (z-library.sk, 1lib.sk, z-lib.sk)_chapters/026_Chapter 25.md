# Chapter 25

# Nonlinear Systems and Newton's Method

Not a single student showed up for Newton's second lecture, and throughout almost every lecture for the next seventeen years ...

Newton talked to an empty room.

— MICHAEL WHITE, Isaac Newton: The Last Sorcerer (1997)

[On Newton's method]

If we start with an approximation to a zero which is appreciably more accurate than the

limiting accuracy which we have just described,

a single iteration will usually spoil this very good approximation and produce one with an error which is typical of the limiting accuracy.

— J. H. WILKINSON, Rounding Errors in Algebraic Processes (1963)

# 25.1. Newton's Method

Newton's method is a key tool in scientific computing for solving nonlinear equations and optimization problems. Our interest in this chapter is in Newton's method for solving algebraic systems of nonlinear equations.

Let $F: \mathbb{R}^n \to \mathbb{R}^n$ be continuously differentiable and denote by $J$ its Jacobian matrix $\left( \frac{\partial F_i}{\partial x_j} \right)$ . Given a starting vector $x_0$ , Newton's method for finding a solution of $F(x) = 0$ generates a sequence $\{x_i\}$ defined by

$$
J \left(x _ {i}\right) \left(x _ {i + 1} - x _ {i}\right) = - F \left(x _ {i}\right), \quad i \geq 0. \tag {25.1}
$$

The attraction of the method stems from the fact that, under appropriate conditions, it converges rapidly to a solution from any starting vector $x_0$ sufficiently close to that solution. In particular, if the Jacobian is nonsingular at the solution then the rate of convergence is quadratic [333, 1983, Thm. 5.2.1].

Computationally, Newton's method is implemented as

solve $J(x_{i})d_{i} = -F(x_{i})$

$$
x _ {i + 1} = x _ {i} + d _ {i}.
$$

In practical computation rounding and other errors are introduced, so the computed iterates $\widehat{x}_i$ actually satisfy

$$
\widehat {x} _ {i + 1} = \widehat {x} _ {i} - \left(J \left(\widehat {x} _ {i}\right) + E _ {i}\right) ^ {- 1} \left(F \left(\widehat {x} _ {i}\right) + e _ {i}\right) + \varepsilon_ {i}, \tag {25.2}
$$

where

- $e_i$ is the error made when computing the residual $F(\widehat{x}_i)$ ,   
- $E_{i}$ is the error incurred in forming $J(\widehat{x}_i)$ and solving the linear system for $d_{i}$ , and   
- $\varepsilon_{i}$ is the error made when adding the correction $\widehat{d}_i$ to $\widehat{x}_i$ .

Note that the term $E_{i}$ in (25.2) enables the model to cover modified Newton methods, in which the Jacobian is held constant for several iterations in order to reduce the cost of the method.

The question of interest in this chapter is how the various errors in (25.2) affect the convergence of Newton's method. In particular, it is important to know the limiting accuracy and limiting residual, that is, how small $\| x_{*} - \widehat{x}_{i}\|$ and $\| F(\widehat{x}_i)\|$ are guaranteed to become as $n$ increases, where $x_{*}$ is the solution to which the iteration would converge in the absence of errors. One might begin an analysis by arguing that (sufficiently small) errors made on a particular iteration are damped out by Newton's method, since the method is locally convergent. However, we are concerned in (25.2) with systematic errors, possibly much larger than the working precision, and how the errors from different iterations interact is not obvious.

In the next section we give general error analysis results for Newton's method in floating point arithmetic that cater for a wide variety of situations: they allow for extended precision in computation of the residual and the use of possibly unstable linear system solvers.

# 25.2. Error Analysis

We assume that $F(\widehat{x}_i)$ is computed in the possibly extended precision $\overline{u} \leq u$ before rounding back to working precision $u$ , and that $\widehat{d_i}$ and $\widehat{x}_i$ are computed at precision $u$ . Hence we assume that there exists a function $\psi$ depending on $F$ , $\widehat{x}_i$ , and $\overline{u}$ such that

$$
\left\| e _ {i} \right\| \leq u \| F \left(\widehat {x} _ {i}\right) \| + \psi (F, \widehat {x} _ {i}, \bar {u}). \tag {25.3}
$$

The norm in this chapter denotes any absolute vector norm and the corresponding subordinate matrix norm. Note that standard error analysis shows that $\| e_i\| \leq u\| F(\widehat{x}_i)\|$ is the best we can obtain in practice for both mixed and fixed precision. We assume that the error $E_{i}$ satisfies

$$
\left\| E _ {i} \right\| \leq u \phi (F, \hat {x} _ {i}, n, u), \tag {25.4}
$$

for some function $\phi$ that reflects both the instability of the linear system solver and the error made when approximating or forming $J(\widehat{x}_i)$ . In practice, we certainly have $\phi(F, \widehat{x}_i, n, u) \geq \|J(\widehat{x}_i)\|$ . For the error $\varepsilon_i$ , we have

$$
\left\| \varepsilon_ {i} \right\| \leq u (\left\| \widehat {x} _ {i} \right\| + \left\| \widehat {d} _ {i} \right\|).
$$

Finally, we assume that $J$ is Lipschitz continuous with constant $\beta$ , that is,

$$
\| J (v) - J (w) \| \leq \beta \| v - w \| \quad \text {f o r a l l} v, w \in \mathbb {R} ^ {n}.
$$

The first result bounds the limiting accuracy.

Theorem 25.1 (Tisseur). Assume that there is an $x_*$ such that $F(x_*) = 0$ and $J_* = J(x_*)$ is nonsingular with

$$
u \kappa \left(J _ {*}\right) \leq \frac {1}{8}. \tag {25.5}
$$

Assume also that for $\phi$ in (25.4),

$$
u \| J \left(\widehat {x} _ {i}\right) ^ {- 1} \| \phi (F, \widehat {x} _ {i}, n, u) \leq \frac {1}{8} \text {f o r a l l} i. \tag {25.6}
$$

Then, for all $x_0$ such that

$$
\beta \| J _ {*} ^ {- 1} \| \| x _ {0} - x _ {*} \| \leq \frac {1}{8}, \tag {25.7}
$$

Newton's method in floating point arithmetic generates a sequence $\{\widehat{x}_i\}$ whose normwise relative error decreases until the first $i$ for which

$$
\frac {\left\| \widehat {x} _ {i + 1} - x _ {*} \right\|}{\left\| x _ {*} \right\|} \approx \frac {\left\| J _ {*} ^ {- 1} \right\|}{\left\| x _ {*} \right\|} \psi (F, x _ {*}, \bar {u}) + u. \tag {25.8}
$$

Proof. See Tisseur [1138, 2001, §2.2].

As a check, we note that in the absence of errors $u$ , $\psi(F,v,\overline{u})$ , and $\phi(F,v,n,u)$ are all zero and thus Theorem 25.1 implies local convergence of Newton's method.

In words, Theorem 25.1 says that if $J(x_{*})$ is not too ill conditioned, the Jacobian evaluation and the solver are not too inaccurate, the Lipschitz constant $\beta$ is not too large, and the initial guess $x_0$ is not too far from $x_{*}$ , then the limiting accuracy is proportional to the condition of the Jacobian at the solution and the accuracy with which the residual is evaluated. Note that the term $\phi$ does not appear in (25.8), which shows that errors in evaluating $J$ and solving the linear system do not affect the limiting accuracy, provided they are not too large. The details of the analysis in [1138, 2001] show that these latter errors do affect the rate of convergence and that this rate is essentially independent of $\overline{u}$ .

The next result bounds the limiting residual.

Theorem 25.2 (Tisseur). Assume that there is an $x_{*}$ such that $F(x_{*}) = 0$ , that $J_{*} = J(x_{*})$ is nonsingular, that (25.5) and (25.6) are satisfied, and that the limiting accuracy $g \approx \| J_{*}^{-1}\| \psi(F,x_{*},\overline{u}) + u\| x_{*}\|$ satisfies $\beta g\| J_{*}^{-1}\| \leq 1/8$ . Then, for all $x_{0}$ such that (25.7) holds, the sequence $\{\| F(\widehat{x}_i)\| \}$ of residual norms generated by Newton's method in floating point arithmetic decreases until

$$
\left\| F \left(\widehat {x} _ {i + 1}\right) \right\| \approx \psi (F, \widehat {x} _ {i}, \bar {u}) + u \| J \left(\widehat {x} _ {i}\right) \| \left\| \widehat {x} _ {i} \right\|. \tag {25.9}
$$

Proof. See Tisseur [1138, 2001, §2.3]. $\square$

Theorem 25.2 shows that, under very similar conditions to those in Theorem 25.1, the limiting residual is at the level of the error made in computing the residual plus the term $u\| J(\widehat{x}_i)\| \| \widehat{x}_i\|$ . This latter term is inevitable: from the Taylor series

$$
F (x _ {*} + \varDelta x _ {*}) = F (x _ {*}) + J (x _ {*}) \varDelta x _ {*} + O (\| \varDelta x _ {*} \| ^ {2}),
$$

we see that merely rounding the exact solution to $\widetilde{x}_{*} = x_{*} + \Delta x_{*}$ , $\| \Delta x_{*} \| \leq u \| x_{*} \|$ gives

$$
\| F (\tilde {x} _ {*}) \| \lesssim \| J (x _ {*}) \| \| \Delta x _ {*} \| \leq u \| J (x _ {*}) \| \| x _ {*} \|.
$$

As for the limiting accuracy, the limiting residual does not depend on the errors in evaluating $J$ or in solving the linear systems, and the analysis in [1138, 2001] shows that the rate of decrease of the residual does not depend on $\overline{u}$ .

Theorems 25.1 and 25.2 confirm the folklore that Newton's method must be provided with good function values if it is to work well in practice.

# 25.3. Special Cases and Experiments

A particularly simple but important special case of Newton's method is iterative refinement of linear systems. Iterative refinement, described in Chapter 12, is equivalent to Newton's method with $F(x) = b - Ax : \mathbb{R}^n \to \mathbb{R}^n$ , for which $J(x) = A$ , and thus we can take the Lipschitz constant $\beta = 0$ .

If the residual $r = F(\hat{x})$ is computed at precision $\overline{u}$ (for example, using the Extended and Mixed Precision BLAS described in §27.10 when $\overline{u} < u$ ), then for $\psi$ in (25.3) we can take

$$
\psi (F, \widehat {x}, \bar {u}) = \bar {\gamma} _ {n + 1} (\| A \| \| \widehat {x} \| + \| b \|),
$$

where

$$
\overline {{\gamma}} _ {n} = \frac {n \bar {u}}{1 - n \bar {u}}.
$$

Theorem 25.1 then shows that if $u\kappa(A)$ is sufficiently less than 1 and if the linear system solver is not too unstable then iterative refinement reduces the relative forward error until

$$
\frac {\| \widehat {x} _ {i} - x \|}{\| x \|} \approx u + \kappa (A) \overline {{\gamma}} _ {n + 1}.
$$

If $\overline{u} = u^2$ then the relative error is of order $u$ provided that $n\kappa(A)u \leq 1$ .

Under the same assumptions, Theorem 25.2 shows further that the norm of the residual $r = b - Ax$ decreases until

$$
\left\| \widehat {r} _ {i} \right\| \approx \max  \left(\bar {\gamma} _ {n + 1}, u\right) \left(\left\| A \right\| \left\| \widehat {x} \right\| + \| b \|\right),
$$

so that, exploiting the connection between the residual and the backward error in Theorem 7.1, iterative refinement yields a normwise backward error $\eta(\widehat{x}) \approx \max(\overline{\gamma}_{n+1}, u)$ . These conclusions agree with those in §§12.1 and 12.2, modulo the use of normwise analysis in this chapter rather than componentwise analysis. This analysis of Newton's method therefore loses little by its generality.

To illustrate the analysis numerically we consider the eigenvalue problem $Ax = \lambda x$ , which can be posed as the nonlinear system $F(v) = 0$ , where

$$
F (v) = \left[ \begin{array}{c} (A - \lambda I) x \\ e _ {s} ^ {T} x - 1 \end{array} \right], \quad v = \left[ \begin{array}{l} x \\ \lambda \end{array} \right]. \tag {25.10}
$$

The last component of $F$ serves to normalize the eigenvector, and here $s$ is some fixed integer. The Jacobian is

$$
J (v) = \left[ \begin{array}{c c} A - \lambda I & - x \\ e _ {s} ^ {T} & 0 \end{array} \right],
$$

for which we can take the Lipschitz constant to be $2\| A\|$ . The eigenvalue $\lambda$ of interest is assumed to be simple, which implies that $J(v)$ is nonsingular at the solution. For the evaluation of $F$ at $\widehat{v}_i = [\widehat{x}_i\widehat{\lambda}_i]^T$ we have

$$
\psi (F, \widehat {v} _ {i}, \overline {{u}}) = \overline {{\gamma}} _ {n + 1} \big (\left\| A \right\| + \left| \widehat {\lambda} _ {i} \right| \big) \| \widehat {x} _ {i} \|.
$$

In a MATLAB experiment we used Newton's method to compute the smallest eigenvalue and corresponding eigenvector of the $10 \times 10$ Frank matrix. The Frank matrix [443, 1958] (MATLAB's gallery('frank')) is an upper Hessenberg matrix with integer entries and its eigenvalues are notoriously ill conditioned. We obtained the exact eigenpair using 50 digit arithmetic with MATLAB's Symbolic Math Toolbox. For the starting vector $v_{0}$ we used the exact eigenpair rounded to 2 binary digits and we took $s = 4$ . We implemented the iteration with the residual computed both at the working precision $(\overline{u} = u)$ and at twice the working precision $(\overline{u} = u^{2})$ , the latter using the Symbolic Math Toolbox; linear systems were solved by GEPP. The 2-norm relative errors $\| v - \widehat{v}_i \|_2 / \| v \|_2$ and residuals $\| F(\widehat{v}_i) \|_2$ are shown in Figure 25.1. With $\overline{u} = u$ , Newton's method is able to provide a solution with relative error of order $10^{-10}$ , but with $\overline{u} = u^2$ full accuracy is obtained. The

predictions from the analysis are a little pessimistic, but correctly indicate that doubling the precision will not improve the residual (because $\| J(v) \| \| v \| \approx 10^6$ at the solution, and so the second term in (25.9) dominates), but will achieve a fully accurate solution. For comparison, the eigenpair computed by MATLAB's eig command has relative error $3 \times 10^{-8}$ and residual $5 \times 10^{-10}$ .

# 25.4. Conditioning

In order to determine the sensitivity of the solution of a nonlinear system to perturbations in the data it is first necessary to decide what is the data. The problem formulation, $F(x) = 0$ , does not explicitly specify the data and hence does not enable us to identify the allowable perturbations of $F$ . We will assume that $F$ depends parametrically on a vector $d$ of data:

$$
F (x) \equiv F (x; d), \qquad d \in \mathbb {R} ^ {m}.
$$

In many cases it is clear what are the problem parameters and hence how to define $d$ . For a linear system, $F(x) = b - Ax$ , $d$ naturally comprises the elements of $A$ and/or $b$ , while for the eigenproblem (25.10) we can take $d = \operatorname{vec}(A)$ . In other cases the choice of $d$ should be guided by the source of errors. For example, if $F(x) = x - \cos(x) \in \mathbb{R}$ then we can assume that

$$
f l (F (x)) = \left(1 + \delta_ {3}\right) \bigl (x - \left(1 + \delta_ {2}\right) \cos \bigl (x \bigl (1 + \delta_ {1} \bigr) \bigr) \bigr), \qquad | \delta_ {i} | \leq \tilde {\gamma} _ {1}, \quad i = 1: 3,
$$

under a reasonable assumption on the cosine evaluation (cf. the discussion on page 7). A suitable choice of $d$ is then

$$
F (x; d) = x - d _ {1} \cos x.
$$

The reasoning is that the multiplicative factor $1 + \delta_3$ can have little influence when solving $F(x) = 0$ , while the $1 + \delta_1$ factor can safely be absorbed into the perturbation in the solution space.

Suppose now that $F(x_{*};d) = 0$ , that $F$ is a sufficiently smooth function of $x$ and $d$ , and that $F_{x}(x_{*};d)$ is nonsingular, where we write

$$
F _ {x} = \left(\frac {\partial F _ {i}}{\partial x _ {j}}\right) \in \mathbb {R} ^ {n \times n}, \quad F _ {d} = \left(\frac {\partial F _ {i}}{\partial d _ {j}}\right) \in \mathbb {R} ^ {n \times m}.
$$

For $\| \Delta d \|$ sufficiently small the implicit function theorem tells us that there is a unique $\Delta x$ such that $F(x_{*} + \Delta x; d + \Delta d) = 0$ . A Taylor series expansion about $(x_{*}, d)$ gives

$$
F (x _ {*} + \Delta x; d + \Delta d) = F _ {x} (x _ {*}; d) \Delta x + F _ {d} (x _ {*}; d) \Delta d + O (\max  (\| \Delta x \|, \| \Delta d \|) ^ {2}),
$$

and so

$$
\Delta x = - F _ {x} \left(x _ {*}; d\right) ^ {- 1} F _ {d} \left(x _ {*}; d\right) \Delta d + O \left(\left\| \Delta d \right\| ^ {2}\right),
$$

which expresses the perturbation in the solution in terms of the perturbation in the data. It is then clear that the condition number defined by

$$
\operatorname {c o n d} (F, x _ {*}; d) := \operatorname * {l i m} _ {\epsilon \to 0} \operatorname * {s u p} \Bigg \{\frac {\| \varDelta x \| _ {\infty}}{\epsilon \| x _ {*} \| _ {\infty}}: F (x _ {*} + \varDelta x; d + \varDelta d) = 0, \| \varDelta d \| \leq \epsilon \| d \| \Bigg \}
$$

![](images/106750172efa6d42c6bfd274fdfb0af9980e5d2751d796265354f3a2e38af016.jpg)

![](images/83b409e0b58f1146f5a4f5cd27738cd809292a88f4261c0b675d7abef6b73d6e.jpg)  
Figure 25.1. Newton's method with $\overline{u} = u$ (top) and $\overline{u} = u^2$ (bottom).

is given by

$$
\operatorname {c o n d} (F, x _ {*}; d) = \| F _ {x} \left(x _ {*}; d\right) ^ {- 1} F _ {d} \left(x _ {*}; d\right) \| \frac {\| d \|}{\| x _ {*} \|}. \tag {25.11}
$$

For the special case of a linear system, $F(x) = b - Ax$ , taking $d = \operatorname{vec}(A)$ and the Frobenius norm, we find

$$
\operatorname {c o n d} (F, x _ {*}; d) = \| A ^ {- 1} \left[ \begin{array}{c c c c} x _ {1} I & x _ {2} I & \ldots & x _ {n} I \end{array} \right] \| _ {F} \frac {\| A \| _ {F}}{\| x \| _ {2}} = \| A ^ {- 1} \| _ {F} \| A \| _ {F},
$$

which agrees (modulo the nonsubordinate choice of norm) with the condition number $\kappa_{A,0}(A,x)$ in (7.5) for linear systems.

A natural question is how to reconcile the condition number (25.11) with the limiting accuracy (25.8) of Newton's method, since the latter bears no simple relationship with the former. In particular, is it possible that $\| J(x_{*})^{-1} \| = \| F_{x}(x_{*};d) \|^{-1}$ be large yet $\operatorname{cond}(F, x_{*}; d)$ small, in which case Newton's method is potentially unstable? Wozniakowski [1255, 1977] has shown that, under a moderately strong assumption on the errors in the evaluation of $F$ relative to a given set of parameters $d$ , Newton's method does achieve a forward error bounded, to first order, by a multiple of $\operatorname{cond}(F, x_{*}; d) u$ . This result does not imply any weakness in Theorem 25.1, because Theorem 25.1 makes a much weaker assumption on the errors in the evaluation of $F$ and does not involve a parameter vector $d$ . For illustration we consider the example, from [1255, 1977],

$$
F (x) = \left[ \begin{array}{c} x _ {1} - x _ {2} \\ x _ {1} ^ {2} + \mu x _ {2} ^ {2} - \mu \end{array} \right], \quad \mu > 0, \tag {25.12}
$$

which has the solution $v = (\mu / (1 + \mu))^{1/2} [1 \, 1]^T$ . We regard $\mu$ as fixed and consider how to parametrize $F$ in a way that reflects the rounding errors in its evaluation. It is straightforward to show that

$$
f l (F (x)) = \operatorname {d i a g} \left(1 + \delta_ {1}, 1 + \delta_ {2}\right) \left[ \begin{array}{c} x _ {1} - x _ {2} \\ \left(1 + \delta_ {3}\right) \left(x _ {1} ^ {2} + \mu x _ {2} ^ {2}\right) - \mu \end{array} \right], \tag {25.13}
$$

where $|\delta_1|, |\delta_2| \leq u, |\delta_3| \leq \gamma_3$ . Hence we take

$$
F (x; d) = \left[ \begin{array}{c} x _ {1} - x _ {2} \\ d (x _ {1} ^ {2} + \mu x _ {2} ^ {2}) - \mu \end{array} \right],
$$

where $d = 1$ is the parameter value of interest. Since

$$
F _ {x} (v; 1) ^ {- 1} F _ {d} (v; 1) = \left[ \begin{array}{c c} 1 & - 1 \\ 2 v _ {1} & 2 \mu v _ {2} \end{array} \right] ^ {- 1} \left[ \begin{array}{c} 0 \\ v _ {1} ^ {2} + \mu v _ {2} ^ {2} \end{array} \right] = \frac {1}{2} v,
$$

it follows that, for any norm,

$$
\operatorname {c o n d} (F, v; 1) = \frac {1}{2} \quad \text {f o r a l l} \mu .
$$

Thus the problem is very well conditioned, yet the Jacobian $J(v) = F_x(v; 1)$ becomes singular as $\mu \to 0$ or $\mu \to \infty$ .

We applied Newton's method to (25.12) in MATLAB with $x_0 = [1 2]^T$ and $\mu = 10^8$ and found that the limiting residual was of order $10^{-8}$ , which is as predicted by Theorem 25.2, since $\| J(v)\| = \| F_x(v;1)\| \approx 10^8$ . It is easy to check that for this problem

$$
\psi (F, x _ {*}, \overline {{{u}}}) \approx u \mu | x _ {2} ^ {2} | \approx u \mu \approx u \| F (x _ {*}) \|,
$$

so the limiting accuracy (25.8) is roughly $\kappa(J_{*})u$ , which is of order $10^{-8}$ . However, the actual limiting accuracy was approximately $u$ , which reflects the conditioning of the problem rather than the conditioning of the Jacobian $J = F_x$ at the solution. The reason (25.8) overestimates the limiting accuracy is that it does not take account of the nature of the errors in evaluating $F$ (displayed in (25.13)).

Rheinboldt [983, 1976] argues that an appropriate condition number for $F(x) = 0$ on a closed set $S$ is

$$
C (F, S) = \frac {\operatorname* {m a x} _ {u , v \in S} \left\| F (u) - F (v) \right\| / \left\| u - v \right\|}{\operatorname* {m i n} _ {u , v \in S} \left\| F (u) - F (v) \right\| / \left\| u - v \right\|}.
$$

This quantity directly generalizes the matrix condition number $\kappa(A)$ (see Problem 6.6). If $F$ is smooth and we let $S$ shrink around a solution $x_*$ then $C(F, S)$ tends to $\kappa(J(x_*))$ . Rheinboldt's analysis leads him to conclude that "asymptotically near $z$ the conditioning of the nonlinear mapping $F$ and its derivative $F'(z)$ are the same". There is no contradiction with the analysis above: the condition number cond in (25.11) is a structured condition number whereas $C(F, S)$ corresponds to allowing arbitrary perturbations to $F$ . The example (25.12) shows the importance of exploiting structure in the problem when it is present.

# 25.5. Stopping an Iterative Method

How to terminate an iteration from a nonlinear equation solver is an important question to which there is no simple answer. Reliable termination is more difficult than in the linear equation case discussed in §17.5, since there is no concept of backward error for a nonlinear equation and the notion of "scale" (how to normalize $F$ ) is less clear.

Stopping tests can be based on the norm of the residual, $\| F(x_{i})\|$ , or the relative error. In a small neighborhood of a solution the residual and relative error can be related, because $F$ is well approximated by a linear function there. If $y$ is sufficiently close to a solution $x_{*}$ then a Taylor series gives

$$
F (y) \approx F (x _ {*}) + J (x _ {*}) (y - x _ {*}) = J (x _ {*}) (y - x _ {*}).
$$

It follows that

$$
\frac {\| F (y) \|}{\| J (x _ {*}) \|} \lesssim \| x _ {*} - y \| \lesssim \| J (x _ {*}) ^ {- 1} \| \| F (y) \|,
$$

which are familiar inequalities in the case of linear equations (see Problem 7.2). For $\| x_{*} - y\|$ sufficiently small these inequalities are rigorous if the lower bound is multiplied by $1 / 2$ and the upper bound by 2 [721, 1995, Lem. 4.3.1]. We conclude that the ratio of the relative error and the residual is bounded in terms of the conditioning of the Jacobian at the solution.

In stopping tests the relative error $\| x_{i + 1} - x_*\| /\| x_*\|$ is typically approximated by the relative difference $\| x_{i + 1} - x_i\| /\| x_{i + 1}\|$ between two successive iterates. The latter quantity is actually approximating $\| x_{i} - x_{*}\| /\| x_{*}\|$ rather than $\| x_{i + 1} -$ $x_{*}\| /\| x_{*}\|$ . For

$$
x _ {i + 1} - x _ {*} = \left(x _ {i + 1} - x _ {i}\right) + \left(x _ {i} - x _ {*}\right),
$$

and for sufficiently fast convergence $\| x_{i + 1} - x_*\| \ll \| x_i - x_*\|$ and hence the two terms on the right-hand side are of roughly equal magnitude and opposite signs. To be more precise, consider Newton's method. Quadratic convergence guarantees that

$$
\left\| x _ {i + 1} - x _ {*} \right\| \leq c \left\| x _ {i} - x _ {*} \right\| ^ {2} \tag {25.14}
$$

close to convergence, where $c$ is a constant. Now

$$
\begin{array}{l} \left\| x _ {i} - x _ {*} \right\| \leq \left\| x _ {i} - x _ {i + 1} \right\| + \left\| x _ {i + 1} - x _ {*} \right\| \\ \leq \left\| x _ {i} - x _ {i + 1} \right\| + c \| x _ {i} - x _ {*} \| ^ {2}. \\ \end{array}
$$

"Solving" for $\| x_{i} - x_{*}\|$ and substituting in (25.14) gives

$$
\begin{array}{l} \left\| x _ {i + 1} - x _ {*} \right\| \leq c \left(\frac {\left\| x _ {i + 1} - x _ {i} \right\|}{1 - c \left\| x _ {i} - x _ {*} \right\|}\right) ^ {2} \\ \leq 2 c \left\| x _ {i + 1} - x _ {i} \right\| ^ {2}, \\ \end{array}
$$

for small enough $\| x_{i} - x_{*}\|$ , so the error in $x_{i + 1}$ is bounded in terms of the square of $\| x_{i + 1} - x_i\|$ .

# 25.6. Notes and References

This chapter is based on Tisseur [1138, 2001, §2.2], who gives the first comprehensive analysis of the limiting accuracy and limiting residual of Newton's method in floating point arithmetic. Earlier work on the subject includes that of Lancaster [763, 1966], Wozniakowski [1255, 1977], Ypma [1273, 1983], and Dennis and Walker [335, 1984].

Related to the results in this chapter is work on inexact Newton methods [304, 1982], which solve the Newton equations $J(x_{i})d_{i} = -F(x_{i})$ approximately—by an iterative method, for example. These methods are usually analyzed in terms of a forcing sequence $\eta_{i}$ such that the computed $x_{i}$ satisfy $\| J(x_{i})d_{i} + F(x_{i})\| \leq \eta_{i}\| F(x_{i})\|$ . The theory of inexact Newton methods does not distinguish the different sources of error and is concerned with the rate of convergence rather than with the limiting accuracy or residual in the presence of persistent rounding errors. For more details of inexact Newton methods see Kelley [721, 1995, Chap. 6] or Nocedal and Wright [894, 1999] and the references therein.

For historical background on Newton's method see Ypma [1275, 1995].

Phrasing the eigenproblem as a nonlinear system and solving it by Newton's method is an old idea. For a detailed discussion see Tisseur [1138, 2001], which contains references to the earlier literature.

Section 25.4 is based on Wozniakowski [1255, 1977]. Related issues are discussed by Chaitin-Chatelin and Fraysse [208, 1996]. The literature contains relatively little on the conditioning of the general nonlinear equations problem and the condition number (25.11) does not seem to be well known.

# Problems

25.1. (Descloux [337, 1963]) Consider the iterative process

$$
x _ {k + 1} = G \left(x _ {k}\right) + e _ {k}, \quad x _ {0} \text {g i v e n},
$$

where $G:\mathbb{R}^n\to \mathbb{R}^n$ satisfies

$$
\| G (x) - a \| \leq \beta \| x - a \| \quad \text {f o r a l l} x \in \mathbb {R} ^ {n}, \tag {25.15}
$$

for some $\beta \in (0,1)$ , and where $\| e_k\| \leq \alpha$ for all $k$ . Note that $a$ must satisfy $G(a) = a$ .

(a) Show that

$$
\begin{array}{l} \text {i f} \| x _ {k} - a \| \leq \frac {\alpha}{1 - \beta} \quad \text {t h e n} \quad \| x _ {k + 1} - a \| \leq \frac {\alpha}{1 - \beta}, \\ \text {i f} \| x _ {k} - a \| > \frac {\alpha}{1 - \beta} \quad \text {t h e n} \quad \| x _ {k + 1} - a \| <   \| x _ {k} - a \|. \\ \end{array}
$$

(b) Show that the sequence $\{x_{k}\}$ is bounded and its points of accumulation $x$ satisfy

$$
\left\| x - a \right\| \leq \frac {\alpha}{1 - \beta}.
$$

(c) Explain the practical relevance of the result of (b).

25.2. (RESEARCH PROBLEM) Extend the results reported in this chapter to problems for which the Jacobian is singular at the solution. Useful references are Griewank [525, 1985] and Ypma [1274, 1983].
