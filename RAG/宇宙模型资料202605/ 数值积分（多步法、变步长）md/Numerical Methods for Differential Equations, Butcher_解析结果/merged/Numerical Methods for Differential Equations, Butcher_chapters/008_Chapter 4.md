# Chapter 4

# Linear Multistep Methods

# 40 Preliminaries

# 400 Fundamentals

This chapter, devoted entirely to the analysis of linear multistep methods, follows on from the introduction to these methods presented in Section 24. We use the notation and ideas introduced there, but attempt to fill in missing details. In particular, we show in the present section how the concepts of consistency, stability and convergence are interrelated and give more of a theoretical justification for the concept of ‘order’. This analysis depends heavily on the use of difference equations, especially on the conditions for the solution of a linear difference equation to be bounded. For a difference equation,

$$
y _ { n } = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } ,
$$

we recall that all solutions are bounded if and only if the polynomial

$$
z ^ { k } - \alpha _ { 1 } z ^ { k - 1 } - \alpha _ { 2 } z ^ { k - 2 } - \cdot \cdot \cdot - \alpha _ { k }
$$

has all its zeros in the closed unit disc and all multiple zeros in the interior of this disc.

The direct applicability of this result to a linear multistep method $[ \alpha , \beta ]$ , in which the approximate solution at $x _ { n }$ is computed by

$$
\begin{array} { r l } & { y _ { n } = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } } \\ & { \qquad + \beta _ { 0 } h f ( x _ { n } , y _ { n } ) + \beta _ { 1 } h f ( x _ { n - 1 } , y _ { n - 1 } ) + \cdot \cdot \cdot + \beta _ { k } h f ( x _ { n - k } , y _ { n - k } ) , } \end{array}
$$

is clear. We wish to be able to solve a wide variety of initial value problems in a reliable manner, and amongst the problems for which we need good answers is certainly the simple problem for which $f ( x , y ) = 0$ . In this case the solution approximations are related by (400a), and stable behaviour for this problem becomes essential. It is a remarkable fact that convergence hinges on this stability result alone, as well as on consistency requirements.

As in Section 24 we write the method as $[ \alpha , \beta ]$ , where

$$
\begin{array} { l } { \alpha ( z ) = 1 - \alpha _ { 1 } z - \alpha _ { 2 } z ^ { 2 } - \cdot \cdot \cdot - \alpha _ { k } z ^ { k } , } \\ { \beta ( z ) = \beta _ { 0 } + \beta _ { 1 } z + \beta _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + \beta _ { k } z ^ { k } , } \end{array}
$$

or in the more traditional formulation as $( \rho , \sigma )$ , where

$$
\begin{array} { l } { \rho ( z ) = z ^ { k } - \alpha _ { 1 } z ^ { k - 1 } - \alpha _ { 2 } z ^ { k - 2 } - \cdot \cdot \cdot - \alpha _ { k } , } \\ { \quad } \\ { \sigma ( z ) = \beta _ { 0 } z ^ { k } + \beta _ { 1 } z ^ { k - 1 } + \beta _ { 2 } z ^ { k - 2 } + \cdot \cdot \cdot + \beta _ { k } . } \end{array}
$$

# 401 Starting methods

As we pointed out in Subsection 246, linear multistep methods require starting methods even to carry out a single step. We consider, in general terms, some of the procedures used to obtain starting values; we then discuss any unifying characteristics they might have.

One obvious approach to starting a $k$ -step method is to carry out $k - 1$ steps with a Runge–Kutta method, preferably of the same order as the linear multistep method itself. An interesting variation of this standard procedure is to use specially constructed Runge–Kutta methods which make it possible to move forward several steps at a time (Gear, 1980).

A second approach, which fits naturally into the style of linear multistep methods, is to solve a system of equations representing the integrals of $y ^ { \prime } ( x )$ from $x _ { 0 }$ to each of $x _ { 1 }$ , $x _ { 2 }$ , . . . , $x _ { k - 1 }$ written, in each case, as a quadrature formula with abscissae at these same points. We illustrate this in the case of the third order Adams–Bashforth method

$$
y _ { n } = y _ { n - 1 } + { \frac { h } { 1 2 } } { \bigl ( } 2 3 f ( x _ { n - 1 } , y _ { n - 1 } ) - 1 6 f ( x _ { n - 2 } , y _ { n - 2 } ) + 5 f ( x _ { n - 3 } , y _ { n - 3 } ) { \bigr ) } ,
$$

for which appropriate quadrature formulae, adapted to a differential equation, are

$$
\begin{array} { l } { { y _ { 1 } = y _ { 0 } + \displaystyle \frac { h } { 1 2 } \big ( 5 f ( x _ { 0 } , y _ { 0 } ) + 8 f ( x _ { 1 } , y _ { 1 } ) - f ( x _ { 2 } , y _ { 2 } ) \big ) , } } \\  { \big \} _ { 2 } = y _ { 0 } + \displaystyle \frac { h } { 3 } \big ( f ( x _ { 0 } , y _ { 0 } ) + 4 f ( x _ { 1 } , y _ { 1 } ) + f ( x _ { 2 } , y _ { 2 } ) \big ) . } \end{array}
$$

These equations are solved by functional iteration to yield approximations $y _ { 1 } \approx y ( x _ { 1 } )$ and $y _ { 2 } \approx y ( x _ { 2 } )$ .

In modern variable order codes, it is usual to start with order 1 or order 2, and to adapt to higher orders when this becomes possible and when it becomes advantageous from an efficiency point of view. This means that order $k$ may be reached after many steps with varying stepsize.

The common feature of these approaches to starting a linear multistep method is that each is, in reality, a Runge–Kutta method possessing multiple outputs, to furnish approximations at a number of equally spaced points. For example, the iteration scheme given by (401a) and (401b) can be represented by the Runge–Kutta scheme

<table><tr><td>：</td><td>0</td><td>0 0</td></tr><tr><td></td><td>中</td><td>1 12</td></tr><tr><td></td><td>G</td><td></td></tr><tr><td></td><td></td><td>1</td></tr><tr><td></td><td></td><td></td></tr><tr><td rowspan="3"></td><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td>中立</td></tr></table>

in which the two output approximations are for $y _ { 1 }$ and $y _ { 2 }$ , respectively. This scheme, like any starting procedure of Runge–Kutta type, has a property we assume for starting schemes used for the definition of convergence. This is that the quantities computed as approximations to $y _ { i }$ , $i = 1 , 2 , \ldots , k - 1$ , all converge to $y ( x _ { 0 } )$ as $h  0$ .

# 402 Convergence

We consider the approximation of $y ( { \overline { { x } } } )$ by a linear multistep method, with $h = ( \overline { { x } } - x _ { 0 } ) / m$ , using initial values

$$
\begin{array} { l } { { y _ { 0 } } = \phi _ { 0 } { \left( y ( { x _ { 0 } } ) , h \right) } , } \\ { { y _ { 1 } } = \phi _ { 1 } { \left( y ( { x _ { 0 } } ) , h \right) } , } \\ { { \mathrm { ~ } } } \\ { { \vdots \qquad \vdots } } \\ { { y _ { k - 1 } } = \phi _ { k - 1 } { \left( y ( { x _ { 0 } } ) , h \right) } . } \end{array}
$$

After the initial values have been evaluated, the values of $y _ { n }$ , for $n =$ $k , k + 1 , \ldots , m$ , are found in turn, using the linear $k$ -step method $[ \alpha , \beta ]$ . It is assumed that for $i = 1 , 2 , \ldots , k - 1$ ,

$$
\left\| \phi _ { i } \left( y ( x _ { 0 } ) , h \right) - y ( x _ { 0 } ) \right\| \to 0 , \quad { \mathrm { ~ a s ~ } } h \to 0 .
$$

Definition 402A Consider a linear multistep method used with a starting method as described in the previous discussion. Let $Y _ { m }$ denote the approximation to $y ( { \overline { { x } } } )$ found using $_ { T I l }$ steps with $h = ( \overline { { x } } - x _ { 0 } ) / m$ . The function $f$ is assumed to be continuous and to satisfy a Lipschitz condition in its second variable. The linear multistep method is said to be ‘convergent’ if, for any such initial value problem,

$$
\| Y _ { m } - y ( { \overline { { x } } } ) \| \to 0 , \ a s \ m \to \infty .
$$

# 403 Stability

For a general initial value problem, the computed solution satisfies

$$
y _ { n } = \sum _ { i = 1 } ^ { k } \alpha _ { i } y _ { n - i } + h \sum _ { i = 0 } ^ { k } \beta _ { i } f ( x _ { n - i } , y _ { n - i } ) .
$$

However, for the one-dimensional problem for which $f ( x , y ) = 0$ , we have the simpler difference equation

$$
y _ { n } = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } .
$$

Definition 403A A linear multistep method $\lfloor \alpha , \beta \rfloor$ is ‘stable’ if the difference equation (403a) has only bounded solutions.

Because stability concepts of one sort or another abound in the theory of initial value problems, ‘stability’ is often referred to as ‘zero-stability’ $^ -$ for example, in Lambert (1991)) $-$ or as ‘stability in the sense of Dahlquist’.

# 404 Consistency

Just as the initial value problem $y ^ { \prime } ( x ) = 0$ , with initial condition $y ( x _ { 0 } ) = 0$ , motivated the concept of stability, so the same problem, with initial value $y ( x _ { 0 } ) = 1$ , can be used to introduce preconsistency. We want to ensure that this problem can be solved exactly, starting from the exact initial value. Suppose the numerical solution is known to have the correct value at $x =$ $x _ { n - k } , x _ { n - k + 1 } , . . . , x _ { n - 1 }$ so that $y _ { i } = y ( x _ { i } ) = 1$ , for $i = n { - } k , n { - } k { + } 1 , \ldots , n { - } 1$ . Under these assumptions, the result computed at step $n$ will be

$$
y _ { n } = \alpha _ { 1 } + \alpha _ { 2 } + \cdot \cdot \cdot + \alpha _ { k } ,
$$

and this will equal the correct value $y _ { n } = 1$ if and only if

$$
1 = \alpha _ { 1 } + \alpha _ { 2 } + \cdot \cdot \cdot + \alpha _ { k } .
$$

Definition 404A A linear multistep method satisfying (404a) is said to be ‘preconsistent’.

Now consider the differential equation

$$
y ^ { \prime } ( x ) = 1 , \qquad y ( x _ { 0 } ) = 0 ,
$$

with exact solution at the step values

$$
y _ { i } = h i .
$$

If this solution has been found for $i = n - k , n - k + 1 , \ldots , n - 1$ , then it is also correct for $i = n$ if and only if

$$
\iota h = \alpha _ { 1 } ( n - 1 ) h + \alpha _ { 2 } ( n - 2 ) h + \cdot \cdot \cdot + \alpha _ { k } ( n - k ) h + h \big ( \beta _ { 0 } + \beta _ { 1 } + \cdot \cdot \cdot + \beta _ { k } \big ) .
$$

Assuming the method is preconsistent, the factor $h$ can be cancelled and then $n$ times (404a) can be subtracted. We then find

$$
\alpha _ { 1 } + 2 \alpha _ { 2 } + \cdot \cdot \cdot + k \alpha _ { k } = \beta _ { 0 } + \beta _ { 1 } + \cdot \cdot \cdot + \beta _ { k } .
$$

This leads to the following definition:

Definition 404B A linear multistep method satisfying (404a) and (404b) is said to be ‘consistent’.

Another way of looking at the consistency conditions is to suppose that $y _ { i } =$ $y ( x _ { i } ) { + } O ( h ^ { 2 } )$ and that $f ( x _ { i } , y _ { i } ) = y ^ { \prime } ( x _ { i } ) \ – O ( h )$ , for $i = n { - } k , n { - } k { + } 1 , \ldots , n { - } 1$ , and to consider the computation of $y _ { n }$ using the equation

$$
{ \begin{array} { r l } & { y _ { n } - h \beta _ { 0 } f ( x _ { n } , y _ { n } ) } \\ & { \qquad = \alpha _ { 1 } y _ { n - 1 } + \alpha _ { 2 } y _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } y _ { n - k } } \\ & { \qquad + h ( \beta _ { 1 } f ( x _ { n - 1 } , y _ { n - 1 } ) + \beta _ { 2 } f ( x _ { n - 2 } , y _ { n - 2 } ) + \cdot \cdot \cdot + \beta _ { k } f ( x _ { n - k } , y _ { n - k } ) ) } \\ & { \qquad = \alpha _ { 1 } y ( x _ { n - 1 } ) + \alpha _ { 2 } y ( x _ { n - 2 } ) + \cdot \cdot \cdot + \alpha _ { k } y ( x _ { n - k } ) } \\ & { \qquad + h ( \beta _ { 1 } y ^ { \prime } ( x _ { n - 1 } ) + \beta _ { 2 } y ^ { \prime } ( x _ { n - 2 } ) + \cdot \cdot \cdot + \beta _ { k } y ^ { \prime } ( x _ { n - k } ) ) . } \end{array} }
$$

Expand the right-hand side by Taylor’s theorem about $x _ { n }$ , and we find

$$
\begin{array} { r l r } {  { \big ( \alpha _ { 1 } + \alpha _ { 2 } + \cdot \cdot \cdot + \alpha _ { k } \big ) y ( x _ { n } ) } } \\ & { } & { \qquad + \big ( \beta _ { 1 } + \cdot \cdot \cdot + \beta _ { k } - \alpha _ { 1 } - 2 \alpha _ { 2 } - \cdot \cdot \cdot - k \alpha _ { k } \big ) h y ^ { \prime } ( x _ { n } ) + O ( h ^ { 2 } ) . } \end{array}
$$

This will give the correct answer of

$$
y ( x _ { n } ) - h \beta _ { 0 } y ^ { \prime } ( x _ { n } ) ,
$$

to within $O ( h ^ { 2 } )$ , if and only if

$$
\alpha _ { 1 } + \alpha _ { 2 } + \cdot \cdot \cdot + \alpha _ { k } = 1
$$

and

$$
\alpha _ { 1 } + 2 \alpha _ { 2 } + \cdot \cdot \cdot + k \alpha _ { k } = \beta _ { 0 } + \beta _ { 1 } + \cdot \cdot \cdot + \beta _ { k } .
$$

Hence, we can view the two requirements of consistency as criteria that the computed solution is capable of maintaining accuracy to within $O ( h ^ { 2 } )$ over one step, and therefore over several steps.

# 405 Necessity of conditions for convergence

We formally prove that stability and consistency are necessary for convergence. Note that the proofs are based on the same simple problems that were introduced in Subsections 403 and 404.

Theorem 405A A convergent linear multistep method is stable.

Proof. If the method were not stable, there would exist an unbounded sequence $\eta$ satisfying the difference equation

$$
\eta _ { n } = \alpha _ { 1 } \eta _ { n - 1 } + \alpha _ { 2 } \eta _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } \eta _ { n - k } .
$$

Define the sequence $\zeta$ by

$$
\zeta _ { n } = \operatorname* { m a x } _ { i = 0 } ^ { n } | \eta _ { i } | ,
$$

so that $\zeta$ converges monotonically to $\infty$ . Consider the solution of the initial value problem

$$
y ^ { \prime } ( x ) = 0 , \qquad y ( 0 ) = 0 ,
$$

with $\overline { { x } } = 1$ . Assuming that $n$ steps are to be performed, we use a stepsize $h = 1 / n$ and initial values $y _ { i } = \eta _ { i } / \zeta _ { n }$ , for $i = 0 , 1 , \ldots , k - 1$ . The condition that $y _ { i } \to 0$ for $0 \leq i \leq k - 1$ is satisfied because $\zeta _ { n }  \infty$ . The approximation computed for $y ( { \overline { { x } } } )$ is equal to $\eta _ { n } / \zeta _ { n }$ . Because the $\zeta$ sequence is unbounded, there will be an infinite number of values of $n$ for which $\left| \zeta _ { n } \right|$ is greater than the greatest magnitude amongst previous members of this sequence. For such values of $n$ , $| \eta _ { n } / \zeta _ { n } | ~ = ~ 1$ , and therefore the sequence $n \mapsto \eta _ { n } / \zeta _ { n }$ cannot converge to $0$ . 

Theorem 405B A convergent linear multistep method is preconsistent.

Proof. By Theorem 405A, we can assume that the method is stable. Let $\eta$ be defined as the solution to the difference equation

$$
\eta _ { n } = \alpha _ { 1 } \eta _ { n - 1 } + \alpha _ { 2 } \eta _ { n - 2 } + \cdot \cdot \cdot + \alpha _ { k } \eta _ { n - k } ,
$$

with initial values $\eta _ { 0 } = \eta _ { 1 } = \cdot \cdot \cdot = \eta _ { k - 1 } = 1$ . The computed solution of the problem

$$
y ^ { \prime } ( x ) = 0 , \qquad y ( 0 ) = 1 , \qquad { \overline { { x } } } = 1 ,
$$

using $n$ steps, is equal to $y _ { n } = \eta _ { n }$ . Since this converges to $^ { 1 }$ as $n  \infty$ , it follows that, for any $\epsilon > 0$ , there exists an $n$ sufficiently large so that $| y _ { i } - 1 | \le \epsilon$

for $i = n - k$ , $n - k + 1$ , $\cdot \cdot \cdot$ , $n$ . Hence,

$$
\begin{array} { l } { \displaystyle { \left| 1 - \alpha _ { 1 } - \alpha _ { 2 } - \cdots \cdots - \alpha _ { k } \right| \leq \left| \eta _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } \eta _ { n - i } \right| + \left( 1 + \sum _ { i = 1 } ^ { k } | \alpha _ { i } | \right) \epsilon } } \\ { \displaystyle { \qquad = \left( 1 + \sum _ { i = 1 } ^ { k } | \alpha _ { i } | \right) \epsilon } . } \end{array}
$$

Because this can be arbitrarily small, it follows that

$$
1 - \alpha _ { 1 } - \alpha _ { 2 } - \cdot \cdot \cdot - \alpha _ { k } = 0 .
$$

Theorem 405C A convergent linear multistep is consistent.

Proof. We note first that

$$
\alpha _ { 1 } + 2 \alpha _ { 2 } + \cdot \cdot \cdot + k \alpha _ { k } \neq 0 ,
$$

since, if the expression were zero, the method would not be stable. Define the sequence $\eta$ by

$$
\eta _ { i } = \frac { \beta _ { 0 } + \beta _ { 1 } + \cdot \cdot \cdot + \beta _ { k } } { \alpha _ { 1 } + 2 \alpha _ { 2 } + \cdot \cdot \cdot + k \alpha _ { k } } i , \qquad i = 0 , 1 , 2 , \ldots .
$$

Consider the numerical solution of the initial value problem

$$
y ^ { \prime } ( x ) = 1 , \qquad y ( 0 ) = 0 ,
$$

with the output computed at $\overline { { x } } = 1$ , and with $n$ steps computed with stepsize $h = 1 / n$ . Choose starting approximations as

$$
y _ { i } = \frac { 1 } { n } \eta _ { i } ,
$$

for $i = 0 , 1 , 2 , \ldots , k - 1$ , so that these values converge to zero as $n \longrightarrow \infty$ . We verify that the computed solution for all values of $i = 0 , 1 , 2 , \ldots , n$ is given also by (405a), and it follows that the approximation at $x = 1$ is

$$
{ \frac { \beta _ { 0 } + \beta _ { 1 } + \cdot \cdot \cdot + \beta _ { k } } { \alpha _ { 1 } + 2 \alpha _ { 2 } + \cdot \cdot \cdot + k \alpha _ { k } } } ,
$$

independent of $n$ . Because convergence implies that the limit of this is $^ { 1 }$ , it follows that

$$
\beta _ { 0 } + \beta _ { 1 } + \cdot \cdot \cdot + \beta _ { k } = \alpha _ { 1 } + 2 \alpha _ { 2 } + \cdot \cdot \cdot + k \alpha _ { k } .
$$

Given that a linear multistep is stable and consistent, we prove that it is convergent. We assume that the differential equation under consideration has the autonomous form

$$
y ^ { \prime } ( x ) = f ( y ( x ) )
$$

and that $f$ satisfies a Lipschitz condition with constant $L$ . These assumptions can be weakened in various ways with no change to the final result, but with considerable complication to the details. If the Lipschitz condition holds only locally, then it becomes necessary to restrict the stepsize so that it is possible to guarantee that all approximations which enter into the discussion are sufficiently close to the exact trajectory for the condition to apply. If the problem is not autonomous, so that $f ( y )$ is replaced by $f ( x , y )$ , then it is possible to allow $f$ to be Lipschitz continuous in the $y$ variable, but merely continuous in $x$ .

However, we now press ahead with consideration of the possible convergence of the solution to (406a), together with the initial information given at $x _ { 0 }$ and the requirement that the approximate solution is to be evaluated at $\scriptstyle { \overline { { x } } }$ . We always assume that $\overline { { x } } > x _ { 0 }$ , to avoid the inconvenience of having to allow for negative stepsizes.

For the rest of this subsection, it will be assumed, without further comment, that the differential equation we are attempting to solve is (406a) and that the solution is to be approximated on the interval $[ x _ { 0 } , { \overline { { x } } } ]$ with initial value information given at $x _ { 0 }$ . The stepsize $h$ will always be positive, and the Lipschitz condition holds with constant $L$ . We refer to the problem as ‘the standard initial value problem’. One further notation we use throughout is to write $M$ for a bound on $\left\| f ( y ( x ) ) \right\|$ for $x \in [ x _ { 0 } , { \overline { { x } } } ]$ . Such a bound clearly exists because

$$
\| f ( y ( x ) ) - f ( y ( x _ { 0 } ) ) \| \leq L \| y ( x ) - y ( x _ { 0 } ) \| ,
$$

and the latter quantity is bounded.

As a first step towards understanding the relationship between an approximation to $y ( { \overline { { x } } } )$ and the exact value of this quantity, we consider a quantity which measures the error generated in a single step.

Definition 406A Let $[ \alpha , \beta ]$ be a consistent linear multistep method. The ‘local truncation error’ associated with a differentiable function $_ y$ at a point $x$ with stepsize $h$ is the value of

$$
\mathcal { L } ( y , x , h ) = y ( x ) - \sum _ { i = 1 } ^ { k } \alpha _ { i } y ( x - i h ) - h \sum _ { i = 0 } ^ { k } \beta _ { i } y ^ { \prime } ( x - i h ) .
$$

We estimate the value of ${ \mathcal { L } } ( y , x , h )$ when $y$ is the exact solution to (406a), and where not only $x$ but also each $x - h i$ , for $i = 1 , 2 , \ldots , k$ , lies in the interval $[ x _ { 0 } , { \overline { { x } } } ]$ .

Lemma 406B If $y$ is the exact solution to the standard initial value problem and $x \in [ x _ { 0 } + k h , \overline { { x } } ]$ , then

$$
\| \mathcal { L } ( y , x , h ) \| \leq \sum _ { i = 1 } ^ { k } \left( \frac { 1 } { 2 } i ^ { 2 } | \alpha _ { i } | + i | i \alpha _ { i } - \beta _ { i } | \right) L M h ^ { 2 } .
$$

Proof. We first estimate $y ( x ) - y ( x - i h ) - i h y ^ { \prime } ( x )$ using the identity

$$
y ( x ) - y ( x - i h ) - h i y ^ { \prime } ( x ) = h \int _ { - i } ^ { 0 } \left( f ( y ( x + h \xi ) ) - f ( y ( x ) ) \right) d \xi ,
$$

so that

$$
\| y ( x ) - y ( x - i h ) - i h y ^ { \prime } ( x ) \| \leq h L \int _ { - i } ^ { 0 } \| y ( x + h \xi ) - y ( x ) \| d \xi ,
$$

and noting, that for $\xi \le 0$ ,

$$
\| y ( x + h \xi ) - y ( x ) \| \leq h \int _ { \xi } ^ { 0 } \| f ( x + h \overline { { \xi } } ) \| d \overline { { \xi } } \leq h | \xi | M ,
$$

so that

$$
\begin{array} { r } { \| y ( x ) - y ( x - i h ) - i h y ^ { \prime } ( x ) \| \leq \frac { 1 } { 2 } i ^ { 2 } h ^ { 2 } L M . } \end{array}
$$

From (406b), we see also that

$$
\| f ( y ( x ) ) - f ( y ( x - i h ) ) \| \leq i h L M .
$$

Because of the consistency of the method, we have $\textstyle \sum _ { i = 1 } ^ { k } \alpha _ { i } \ = \ 1$ and $\begin{array} { r } { \sum _ { i = 1 } ^ { k } ( i \alpha _ { i } - \beta _ { i } ) = \beta _ { 0 } } \end{array}$ . We now write ${ \mathcal { L } } ( y , x , h )$ in the form

$$
\begin{array} { l } { \displaystyle \mathcal { L } ( y , x , h ) = \sum _ { i = 1 } ^ { k } \alpha _ { i } ( y ( x ) - y ( x - i h ) - i h y ^ { \prime } ( x ) ) } \\ { \displaystyle + h \sum _ { i = 1 } ^ { k } ( i \alpha _ { i } - \beta _ { i } ) ( y ^ { \prime } ( x ) - y ^ { \prime } ( x - i h ) ) ; } \end{array}
$$

this is bounded by

$$
{ \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { k } i ^ { 2 } | \alpha _ { i } | L M h ^ { 2 } + \sum _ { i = 1 } ^ { k } i | i \alpha _ { i } - \beta _ { i } | L M h ^ { 2 }
$$

and the result follows.

Theorem 406C Let $\epsilon _ { n }$ denote the vector

$$
\epsilon _ { n } = y ( x _ { n } ) - y _ { n } .
$$

Then for $h _ { 0 }$ sufficiently small so that $h _ { 0 } | \beta _ { 0 } | L < 1$ and $h < h _ { 0 }$ , there exist constants $C$ and $D$ such that

$$
\left\| \epsilon _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } \epsilon _ { n - i } \right\| \leq C h \operatorname* { m a x } _ { i = 1 } ^ { k } \| \epsilon _ { n - i } \| + D h ^ { 2 } .
$$

Proof. The value of $\begin{array} { r } { \epsilon _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } \epsilon _ { n - i } - h \sum _ { i = 0 } ^ { k } \beta _ { i } ( f ( y ( x _ { n - i } ) ) - f ( y _ { n - i } ) ) } \end{array}$ i s the difference of two terms, of which the first can be bounded by a constant times $h ^ { 2 }$ , by Theorem 406B, and the second is zero. This means that

$$
\epsilon _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } \epsilon _ { n - i } = T _ { 1 } + T _ { 2 } + T _ { 3 } ,
$$

where

$$
\begin{array} { r } { \| T _ { 1 } \| = h | \beta _ { 0 } | \| f ( y ( x _ { n } ) ) - f ( y _ { n } ) \| \qquad \leq h L | \beta _ { 0 } | \cdot \| \epsilon _ { n } \| , } \end{array}
$$

$$
\| T _ { 2 } \| = h \Big \| \sum _ { i = 1 } ^ { k } \beta _ { i } \big ( f \big ( y ( x _ { n - i } ) \big ) - f \big ( y _ { n - i } \big ) \big ) \Big \| \leq h L \sum _ { i = 1 } ^ { k } | \beta _ { i } | \operatorname* { m a x } _ { i = 1 } ^ { k } \| \epsilon _ { n - i } \| ,
$$

and $\| T _ { 3 } \|$ can be bounded in terms of a constant times $h ^ { 2 }$ . We now use (406d) twice. First, assuming $h \leq h _ { 0 }$ , obtain a bound on $( 1 - h L | \beta _ { 0 } | ) \| \epsilon _ { n } \|$ in terms of $\operatorname* { m a x } _ { i = 1 } ^ { k } \| \epsilon _ { n - i } \|$ and terms that are bounded by a constant times $h ^ { 2 }$ . Hence, obtain a bound on $\| \epsilon _ { n } \|$ . Then, by inserting this preliminary result in the bound on $T _ { 1 }$ , we obtain the result of the theorem. 

Theorem 406D A stable consistent linear multistep method is convergent.

Proof. Write (406c) in the form

$$
\epsilon _ { n } = \sum _ { i = 1 } ^ { k } \alpha _ { i } \epsilon _ { n - i } + \psi _ { n } ,
$$

where, according to Theorem 406C,

$$
\| \psi _ { n } \| \leq C h \operatorname* { m a x } _ { i = 1 } ^ { k } \| \epsilon _ { n - i } \| + D h ^ { 2 } ,
$$

for $h$ sufficiently small. Define $\theta _ { 1 }$ , $\theta _ { 2 } , \ldots$ as in Subsection 141, and note that, because the method is convergent, the $\theta$ sequence is bounded. From Theorem 141A, we have

$$
\epsilon _ { n } = \sum _ { i = 0 } ^ { k - 1 } \theta _ { n - i } \widetilde { \epsilon } _ { i } + \sum _ { i = k } ^ { n } \theta _ { n - i } \psi _ { i } ,
$$

where $\widetilde { \epsilon } _ { i }$ , for $i = 0 , 1 , \ldots , k - 1$ , are linear combinations of the errors in $y _ { i }$ and tend to zero as $h  0$ . Hence we have

$$
\| \epsilon _ { n } \| \leq \Theta \sum _ { i = 0 } ^ { k - 1 } \| \widetilde { \epsilon } _ { i } \| + \Theta C h k \sum _ { i = k } ^ { n - 1 } \| \epsilon _ { i } \| + \Theta D ( n - k ) h ^ { 2 } ,
$$

where $\Theta = \operatorname* { s u p } _ { i = 1 } ^ { \infty } \left| \theta _ { i } \right|$ and the factor $k$ is introduced in the second summation in (406g) because the same maximum value of $\| \epsilon _ { n - i } \|$ may arise in up to $k$ adjacent terms. We rewrite (406g) in the form

$$
\| \epsilon _ { n } \| \leq \phi ( h ) + \Theta C h k \sum _ { i = 1 } ^ { n - 1 } \| \epsilon _ { i } \| + \Theta D n h ^ { 2 } , \quad \| \epsilon _ { 0 } \| \leq \phi ( h ) ,
$$

where $\phi ( h )$ takes positive values and will converge to zero as $h  0$ . It now follows that $\| \epsilon _ { n } \| \le u _ { n }$ , where the sequence $u$ is defined by

$$
u _ { n } = \Theta C h k \sum _ { i = 1 } ^ { n - 1 } u _ { i } + \Theta D n h ^ { 2 } + \phi ( h ) , \quad u _ { 0 } = \phi ( h ) .
$$

By subtracting (406h) with $n$ replaced by $n - 1$ , we find that

$$
u _ { n } + \frac { D h } { C k } = \left( 1 + \Theta C h k \right) \left( u _ { n - 1 } + \frac { D h } { C k } \right) ,
$$

which leads to the bound

$$
\begin{array} { r l r } & { } & { \| \epsilon _ { n } \| \le u _ { n } = ( 1 + \Theta C h k ) ^ { n } \phi ( h ) + \left( ( 1 + \Theta C h k ) ^ { n } - 1 \right) \displaystyle \frac { D h } { C k } } \\ & { } & \\ & { } & { \le \exp ( \Theta C k n h ) \phi ( h ) + ( \exp ( \Theta C k n h ) - 1 ) \displaystyle \frac { D h } { C k } . } \end{array}
$$

To complete the proof, substitute $n = m$ where $m h = \overline { { x } } - x _ { 0 }$ , so that the error in the approximation at $x = \overline { { x } }$ using $_ { I I }$ steps with stepsize $h$ is bounded by

$$
\exp ( \Theta C k ( \overline { { { x } } } - x _ { 0 } ) ) \phi ( h ) + \exp ( \Theta C k ( \overline { { { x } } } - x _ { 0 } ) ) \frac { D h } { C k } \to 0 .
$$

# Exercises 40

40.1 Find a four-stage Runge–Kutta method with $\begin{array} { r } { c _ { 2 } = \frac { 1 } { 3 } } \end{array}$ , $\begin{array} { r } { c _ { 3 } = \frac { 2 } { 3 } } \end{array}$ , $c _ { 4 } = 1$ , which satisfies the order conditions

$$
\begin{array} { c } { \displaystyle \sum _ { i = 1 } ^ { 4 } b _ { i } = \xi , } \\ { \displaystyle \sum _ { i = 1 } ^ { 4 } b _ { i } c _ { i } = \frac 1 2 \xi ^ { 2 } , } \\ { \displaystyle \sum _ { i = 1 } ^ { 4 } b _ { i } c _ { i } ^ { 2 } = \frac 1 3 \xi ^ { 3 } , } \\ { \displaystyle \sum _ { i = 1 } ^ { 4 } b _ { i } c _ { i } ^ { 2 } = \frac 1 3 \xi ^ { 3 } , } \\ { \displaystyle \sum _ { j = 1 } ^ { 4 } b _ { i } a _ { i j } c _ { j } = \frac 1 6 \xi ^ { 3 } , } \end{array}
$$

where $\xi$ is a real parameter and the elements of $A$ are independent of $\xi$ . Show how this method can be used as a starter for the predictor– corrector pair consisting of the third order Adams–Bashforth and Adams–Moulton methods.

40.2 For each of the following polynomial pairs, written as $[ \alpha ( z ) , \beta ( z ) ]$ , determine if the corresponding numerical method is consistent and stable:

1. $\left[ 1 - z , 2 z - z ^ { 2 } \right]$ ,   
2. $[ 1 - z ^ { 2 } , 2 z - z ^ { 2 } ]$ ,   
3. $[ 1 + z - 3 z ^ { 2 } + z ^ { 3 } , 3 z - z ^ { 2 } ]$   
4. $[ 1 + z - z ^ { 2 } - z ^ { 3 } , 3 + z ]$ .

40.3 Translate the conditions for stability, preconsistency and consistency from the $[ \alpha , \beta ]$ representation to the $( \rho , \sigma )$ representation.

40.4 For a linear multistep method $[ \alpha , \beta ]$ , define polynomials $a$ and $b$ by

$$
\begin{array} { l } { { a ( z ) = ( 1 + z ) ^ { k } - \alpha _ { 1 } ( 1 + z ) ^ { k - 1 } ( 1 - z ) - \alpha _ { 2 } ( 1 + z ) ^ { k - 2 } ( 1 - z ) ^ { 2 } - \cdots } } \\ { { \qquad - ( 1 - z ) ^ { k } \alpha _ { k } , } } \\ { { b ( z ) = \beta _ { 0 } ( 1 + z ) ^ { k } + \beta _ { 1 } ( 1 + z ) ^ { k - 1 } ( 1 - z ) + \beta _ { 2 } ( 1 + z ) ^ { k - 2 } ( 1 - z ) ^ { 2 } + \cdots } } \\ { { \qquad + ( 1 - z ) ^ { k } \beta _ { k } . } } \end{array}
$$

Find the conditions for stability, preconsistency and stability in terms of the polynomials $a$ and $b$ .

# 41 The Order of Linear Multistep Methods

# 410 Criteria for order

Given a linear multistep method $[ \alpha , \beta ]$ , we seek conditions on the coefficients in the polynomials $\alpha$ and $\beta$ that will guarantee that, locally, errors are $O ( h ^ { p + 1 } )$ . By this we mean that if starting values satisfy $y _ { i } = y ( x _ { i } ) + O ( h ^ { p + 1 } )$ , for $i = 0 , 1 , \ldots , k { - } 1$ , then this will imply that a similar estimate persists for $i \geq k$ . We emphasize that this is a local property in the sense that it cannot be used in a limiting case in which integration is carried to a fixed point $\overline { { x } } > x _ { 0 }$ , because the number of steps required to achieve this is approximately $( { \overline { { x } } } - x _ { 0 } ) / h$ , and this is unbounded as $h  0$ . To verify that $y _ { n } = y ( x _ { n } ) + O ( h ^ { p + 1 } )$ , assuming the same is true for the previous $k$ step values, it will be enough to estimate the value of

$$
y ( x _ { n } ) - \sum _ { i = 1 } ^ { k } \alpha _ { i } y ( x _ { n - i } ) - \sum _ { i = 0 } ^ { k } \beta _ { i } h y ^ { \prime } ( x _ { n - i } )
$$

and to show that, under appropriate smoothness assumptions, it is $O ( h ^ { p + 1 } )$ . The smoothness assumptions will be that the problem under consideration has a solution with continuous derivatives up to order $p + 1$ . This will enable us to expand (410a) in a Taylor series

$$
\begin{array} { r l } & { C _ { 0 } y ( x _ { n } ) + C _ { 1 } h y ^ { \prime } ( x _ { n } ) + C _ { 2 } h ^ { 2 } y ^ { \prime \prime } ( x _ { n } ) + \cdot \cdot \cdot } \\ & { \qquad + C _ { p } h ^ { p } y ^ { ( p ) } ( x _ { n } ) + C _ { p + 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) + \cdot \cdot \cdot } \end{array}
$$

and order $p$ will mean that $C _ { 0 } = C _ { 1 } = \cdot \cdot \cdot = C _ { p }$ . The value of $C _ { p + 1 }$ is closely related to the error constant and is non-zero unless the order is actually higher than $p$ .

Theorem 410A The constants $C _ { 0 } , C _ { 1 } , C _ { 2 } , \ldots$ . in (410b) are given by

$$
\alpha ( \exp ( - z ) ) - z \beta ( \exp ( - z ) ) = C _ { 0 } + C _ { 1 } z + C _ { 2 } z ^ { 2 } + \cdot \cdot \cdot .
$$

Proof. The coefficient of in the Taylor expansion of (410a) is equal to $\textstyle 1 - \sum _ { i = 1 } ^ { k } \alpha _ { i }$ , and this equals the constant term in the Taylor expansion of $\alpha ( \exp ( - z ) ) - z \beta ( \exp ( - z ) )$ . Now suppose that $j = 1 , 2 , \dots$ and calculate the coefficient of $y ^ { ( j ) } ( x _ { n } )$ in the Taylor expansion of (410a). This equals

$$
- \sum _ { i = 1 } ^ { k } \alpha _ { i } { \frac { ( - i ) ^ { j } } { j ! } } - \sum _ { i = 0 } ^ { k } \beta _ { i } { \frac { ( - i ) ^ { j - 1 } } { ( j - 1 ) ! } } ,
$$

where the coefficient of $\beta _ { 0 }$ is $^ { - 1 }$ if $j = 1$ and zero for $j > 1$ . This is identical to the coefficient of $z ^ { j }$ in the Taylor expansion of $\alpha ( \exp ( - z ) ) - z \beta ( \exp ( - z ) )$ .


<!-- chunk 0006: pages 351-420 -->
Altering the expression in (410c) slightly, we can state without proof a criterion for order:

Theorem 410B A linear multistep method $[ \alpha , \beta ]$ has order $p$ (or higher) if and only if

$$
\alpha ( \exp ( z ) ) + z \beta ( \exp ( z ) ) = O ( z ^ { p + 1 } ) .
$$

Because we have departed from the traditional $( \rho , \sigma )$ formulation for linear multistep methods, we restate this result in that standard notation:

Theorem 410C A linear multistep method $( \rho , \sigma )$ has order $p$ if and only if

$$
\rho ( \exp ( z ) ) - z \sigma ( \exp ( z ) ) = { \cal O } ( z ^ { p + 1 } ) .
$$

Return now to Theorem 410B and replace $\exp ( z )$ by $( 1 + z ) ^ { - 1 }$ . It is found that

$$
\alpha ( ( 1 + z ) ^ { - 1 } ) - \log ( 1 + z ) \beta ( ( 1 + z ) ^ { - 1 } ) = O ( z ^ { p + 1 } ) ,
$$

where $\log ( 1 + z )$ is defined only in $\{ z \in \mathbb { C } : | z | < 1 \}$ by its power series

$$
\log ( 1 + z ) = z - { \frac { 1 } { 2 } } z ^ { 2 } + { \frac { 1 } { 3 } } z ^ { 3 } - \cdot \cdot \cdot .
$$

Because both $\alpha ( 1 + z )$ and $\log ( 1 + z )$ vanish when $z = 0$ , it is possible to rearrange (410d) in the form given in the following result, which we present without further proof.

Theorem 410D A linear multistep formula $\lfloor \alpha , \beta \rfloor$ has order $p$ if and only if

$$
\frac { z } { \log ( 1 + z ) } \frac { \alpha ( 1 + z ) } { z } + \beta ( 1 + z ) = O ( z ^ { p } ) .
$$

# 411 Derivation of methods

Given the relationship between the coefficients in the $\alpha$ and $\beta$ polynomials under the condition that they have a specified order, the choice of actual methods remains. The first approach we consider is when $\alpha$ is given and $\beta$ is then chosen to achieve the required order. In Subsection 412 we consider the derivation of backward difference methods, in which $\beta$ is first specified and $\alpha$ is then derived.

To find the coefficients in Adams–Moulton methods, use $\alpha ( z ) = 1 - z$ , so

that from Theorem 410D we find

$$
{ \begin{array} { r l } & { \beta ( 1 + z ) = { \cfrac { 1 } { 1 - { \frac { 1 } { 2 } } z + { \frac { 1 } { 3 } } z ^ { 2 } - { \frac { 1 } { 4 } } z ^ { 3 } + { \frac { 1 } { 5 } } z ^ { 4 } - { \frac { 1 } { 6 } } z ^ { 5 } + \cdots } } } \\ & { \qquad = 1 + { \frac { 1 } { 2 } } z - { \frac { 1 } { 1 2 } } z ^ { 2 } + { \frac { 1 } { 2 4 } } z ^ { 3 } - { \frac { 1 9 } { 7 2 0 } } z ^ { 4 } + { \frac { 3 } { 1 6 0 } } z ^ { 5 } } \\ & { \qquad - { \frac { 8 6 3 } { 6 0 4 8 0 } } z ^ { 6 } + { \frac { 2 7 5 } { 2 4 1 9 2 } } z ^ { 7 } - { \frac { 3 3 9 5 3 } { 3 6 2 8 8 0 0 } } z ^ { 8 } } \\ & { \qquad + { \frac { 8 1 8 3 } { 1 0 3 6 8 0 0 } } z ^ { 9 } - { \frac { 3 2 5 0 4 3 3 } { 4 7 9 0 0 1 6 0 0 } } z ^ { 1 0 } + \cdots . } \end{array} }
$$

It is clear that order $k + 1$ can be obtained using a $k$ -step method because the expansion can be truncated at the term in $z ^ { k }$ , leading to an $O ( z ^ { k + 1 } )$ error and degree $k$ polynomial $\beta ( 1 + z )$ . For example, for $k = 1$ we have

$$
\begin{array} { r } { \beta ( 1 + z ) = 1 + \frac { 1 } { 2 } z , } \end{array}
$$

implying that

$$
\begin{array} { r } { \beta ( z ) = 1 + \frac { 1 } { 2 } ( z - 1 ) = \frac { 1 } { 2 } + \frac { 1 } { 2 } z , } \end{array}
$$

giving the coefficients $\beta _ { 0 } = \beta _ { 1 } = \textstyle { \frac { 1 } { 2 } }$ . If $k = 2$ we have

$$
\beta ( 1 + z ) = 1 + \textstyle { \frac { 1 } { 2 } } z - \textstyle { \frac { 1 } { 1 2 } } z ^ { 2 }
$$

and

$$
\begin{array} { r } { \beta ( z ) = 1 + \frac { 1 } { 2 } ( z - 1 ) - \frac { 1 } { 1 2 } ( z - 1 ) ^ { 2 } = \frac { 5 } { 1 2 } + \frac { 2 } { 3 } z + - \frac { 1 } { 1 2 } z ^ { 2 } , } \end{array}
$$

giving $\beta _ { 0 } = \frac { 5 } { 1 2 }$ , $\beta _ { 1 } = \textstyle { \frac { 2 } { 3 } }$ , $\beta _ { 2 } = - \frac { 1 } { 1 2 }$ . In general, we can find the coefficients by rewriting (411a) in the form

$$
\begin{array} { r l } & { \beta ( z ) = 1 + \frac { 1 } { 2 } ( z - 1 ) - \frac { 1 } { 1 2 } ( z - 1 ) ^ { 2 } + \frac { 1 } { 2 4 } ( z - 1 ) ^ { 3 } - \frac { 1 9 } { 7 2 0 } ( z - 1 ) ^ { 4 } } \\ & { \qquad + \frac { 3 } { 1 6 0 } ( z - 1 ) ^ { 5 } - \frac { 8 6 3 } { 6 0 4 8 0 } ( z - 1 ) ^ { 6 } + \frac { 2 7 5 } { 2 4 1 9 2 } ( z - 1 ) ^ { 7 } - \frac { 3 3 9 5 3 } { 3 6 2 8 8 0 0 } ( z - 1 ) ^ { 8 } } \\ & { \qquad + \frac { 8 1 8 3 } { 1 0 3 6 8 0 0 } ( z - 1 ) ^ { 9 } - \frac { 3 2 5 0 4 3 3 } { 4 7 9 0 0 1 6 0 0 } ( z - 1 ) ^ { 1 0 } + \cdots , } \end{array}
$$

and truncating at the term in $( z - 1 ) ^ { k }$ to obtain the coefficients in the $k$ -step order $k + 1$ method.

For Adams–Bashforth methods, in which $\beta _ { 0 }$ necessarily vanishes, we write $\beta ( z ) = z { \widehat { \beta } } ( z )$ , where $\widehat { \beta }$ has degree $k - 1$ for a $k$ -step method. In this case Theorem 410D can be written in the form

$$
\frac { z } { ( 1 + z ) \log ( 1 + z ) } \frac { \alpha ( 1 + z ) } { z } + \widehat { \beta } ( 1 + z ) = O ( z ^ { p } ) ,
$$

and we aim for order $p = k$ . It is found that

$$
{ \begin{array} { r l } & { { \widehat { \beta } } ( 1 + z ) = { \frac { 1 } { ( 1 + z ) \left( 1 - { \frac { 1 } { 2 } } z + { \frac { 1 } { 3 } } z ^ { 2 } - { \frac { 1 } { 4 } } z ^ { 3 } + \cdots \right) } } } \\ & { \qquad = 1 - { \frac { 1 } { 2 } } z + { \frac { 5 } { 1 2 } } z ^ { 2 } - { \frac { 3 } { 8 } } z ^ { 3 } + { \frac { 2 5 1 } { 7 2 0 } } z ^ { 4 } - { \frac { 9 5 } { 2 8 8 } } z ^ { 5 } } \\ & { \qquad + { \frac { 1 9 0 8 7 } { 6 0 4 8 0 } } z ^ { 6 } - { \frac { 5 2 5 7 } { 1 7 2 8 0 } } z ^ { 7 } + { \frac { 1 0 7 0 0 1 7 } { 3 6 2 8 8 0 0 } } z ^ { 8 } } \\ & { \qquad - { \frac { 2 5 7 1 3 } { 8 9 6 0 0 } } z ^ { 9 } + { \frac { 2 6 8 4 2 2 5 3 } { 9 5 8 0 0 3 2 0 } } z ^ { 1 0 } - \cdots , } \end{array} }
$$

so that the coefficients $\beta _ { 1 }$ , $\beta _ { 2 } , \ldots , \beta _ { k }$ can be found by selecting the coefficients of $z ^ { 0 }$ , $z ^ { 1 }$ , . . . , $z ^ { k - 1 }$ in the truncation to the term in $( z - 1 ) ^ { k - 1 }$ in the expansion

$$
\begin{array} { r } { \ddot { \beta } ( z ) = 1 - \frac { 1 } { 2 } ( z - 1 ) + \frac { 5 } { 1 2 } ( z - 1 ) ^ { 2 } - \frac { 3 } { 8 } ( z - 1 ) ^ { 3 } + \frac { 2 5 1 } { 7 2 0 } ( z - 1 ) ^ { 4 } } \end{array}
$$

$$
\begin{array} { r } { - \frac { 9 5 } { 2 8 8 } ( z - 1 ) ^ { 5 } + \frac { 1 9 0 8 7 } { 6 0 4 8 0 } ( z - 1 ) ^ { 6 } - \frac { 5 2 5 7 } { 1 7 2 8 0 } ( z - 1 ) ^ { 7 } + \frac { 1 0 7 0 0 1 7 } { 3 6 2 8 8 0 0 } ( z - 1 ) ^ { 8 } } \end{array}
$$

$$
- { \frac { 2 5 7 1 3 } { 8 9 6 0 0 } } ( z - 1 ) ^ { 9 } + { \frac { 2 6 8 4 2 2 5 3 } { 9 5 8 0 0 3 2 0 } } ( z - 1 ) ^ { 1 0 } - \cdot \cdot \cdot .
$$

For example, when $k = 2$ we have $\begin{array} { r } { { \widehat { \beta } } ( z ) = 1 - \frac { 1 } { 2 } ( z - 1 ) = \frac { 3 } { 2 } - \frac { 1 } { 2 } z } \end{array}$ leading to $\beta _ { 1 } = \begin{array} { l } { \frac { 3 } { 2 } } \end{array}$ and $\beta _ { 2 } = - \frac { 1 } { 2 }$ for the Adams–Bashforth method with order $p = 2$ . When $k = 3$ we have $\textstyle \beta ( z ) = 1 - { \frac { 1 } { 2 } } ( z - 1 ) + { \frac { 5 } { 1 2 } } ( z - 1 ) ^ { 2 } = { \frac { 2 3 } { 1 2 } } - { \frac { 4 } { 3 } } z + { \frac { 5 } { 1 2 } } z ^ { 2 }$ so that, for the Adams–Bashforth method with order $p = 3$ , we have $\beta _ { 1 } = \textstyle { \frac { 2 3 } { 1 2 } }$ , $\beta _ { 2 } = - \frac { 4 } { 3 }$ , $\beta _ { 3 } = \textstyle { \frac { 5 } { 1 2 } }$ .

Values of the Adams–Bashforth and Adams–Moulton coefficients have previously been given in Tables 244(I) and 244(II), respectively.

# 412 Backward difference methods

These methods are also known as ‘backward difference formulae’ or BDF methods. Sometimes the notation BDF $k$ is used for the order $k$ member of this family. Instead of choosing a specific $\alpha$ polynomial, we consider the choice $\beta = \beta _ { 0 }$ , where $\beta _ { 0 }$ is to be chosen for consistency. From Theorem 410D we have

$$
\alpha ( 1 + z ) = - \beta _ { 0 } \log ( 1 + z ) + O ( z ^ { p + 1 } ) .
$$

Expand $\beta _ { 0 } \log ( 1 + z )$ to terms in $z ^ { k }$ , for order $p = k$ , and then substitute $z - 1$ in place of $z$ . It is found that

$$
\alpha ( z ) = \beta _ { 0 } \Big ( - ( z - 1 ) + { \textstyle \frac { 1 } { 2 } } ( z - 1 ) ^ { 2 } - { \textstyle \frac { 1 } { 3 } } ( z - 1 ) ^ { 3 } + \cdots \Big ) ,
$$

and $\beta _ { 0 }$ is chosen so that $\alpha ( 0 ) = 1$ . For $k = p = 1$ , we have $\alpha ( z ) = \beta _ { 0 } ( 1 - z )$ , so that $\beta _ { 0 } = 1$ and $\alpha _ { 1 } = 1$ . For $k = p = 2$ ,

$$
\begin{array} { r } { \alpha ( z ) = \beta _ { 0 } \Big ( ( 1 - z ) + \frac { 1 } { 2 } ( 1 - z ) ^ { 2 } \Big ) = \beta _ { 0 } \Big ( \frac { 3 } { 2 } - 2 z + \frac { 1 } { 2 } z ^ { 2 } \Big ) , } \end{array}
$$

Coefficients of the backward difference methods up to order 7   

<table><tr><td>k</td><td>α1</td><td>α2</td><td>α3</td><td>α4</td><td>α5</td><td>α6</td><td>α7</td><td>3</td><td>C</td></tr><tr><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>B</td><td>中</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>3</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>25</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>300</td><td>300</td><td>200</td><td>药</td><td>12</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>137</td><td>137</td><td>137</td><td>137</td><td>137</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>120</td><td>150</td><td>400</td><td>75</td><td>24</td><td>10</td><td></td><td></td><td>20</td></tr><tr><td></td><td>49</td><td>49</td><td>147</td><td>49</td><td>49</td><td>147</td><td></td><td></td><td>343</td></tr><tr><td></td><td>980</td><td>490</td><td>4900</td><td>1225</td><td>196</td><td>490</td><td>20</td><td></td><td>35</td></tr><tr><td>7</td><td>363</td><td>121</td><td>1089</td><td>363</td><td>121</td><td>1089</td><td>363</td><td>363</td><td>726</td></tr></table>

giving $\begin{array} { r } { \beta _ { 0 } = \frac { 2 } { 3 } } \end{array}$ and

$$
\alpha _ { 1 } = \frac { 4 } { 3 } , ~ \alpha _ { 2 } = - \frac { 1 } { 3 } .
$$

The coefficients for these methods are given up to $p = k = 7$ in Table 412(I), where the error constant $C$ is found to be $\beta _ { 0 } / ( p + 1 )$ .

Note that the method with $p = k = 7$ is of no practical value, in terms of the criteria for convergence, because it is not stable. This remark also applies to methods with $k > 7$ .

# Exercises 41

41.1 Given $\alpha _ { 2 }$ , find $\alpha _ { 1 }$ , $\beta _ { 1 }$ and $\beta _ { 2 }$ such that the linear multistep method $( 1 - \alpha _ { 1 } z - \alpha _ { 2 } z ^ { 2 } , \beta _ { 1 } z + \beta _ { 2 } z ^ { 2 } )$ has order 2. What are the bounds on $\alpha _ { 2 }$ for which the method is convergent?

41.2 Show that all backward difference methods with $k \leq 6$ are stable.

41.3 Show that the order 7 backward difference method is not stable.

41.4 Find a stable seventh order linear multistep method of the form $( 1 - \alpha _ { 1 } z - \alpha _ { 2 } z ^ { 2 } - \cdot \cdot \cdot - \alpha _ { 8 } z ^ { 8 } , \beta _ { 0 } )$ .

# 42 Errors and Error Growth

# 420 Introduction

The result computed in a step is generally not exact, even if we ignore any errors introduced in previous steps. However, once a significant departure from the exact solution has occurred, we are in effect solving a different problem. Hence, a proper analysis of error takes account of errors generated locally, and also the accumulated effect of errors generated in previous steps. We present a simplified discussion of this phenomenon in this subsection, and discuss the limitations of this discussion in Subsection 421.

Suppose a sequence of approximations

$$
\begin{array} { c } { y _ { 1 } \approx y ( x _ { 1 } ) , } \\ { y _ { 2 } \approx y ( x _ { 2 } ) , } \\ { \vdots \qquad \vdots } \\ { y _ { n - 1 } \approx y ( x _ { n - 1 } ) , } \end{array}
$$

has been computed, and we are now computing step $n$ . If, for the moment, we ignore errors in previous steps, the value of $y _ { n }$ can be evaluated using a Taylor expansion where, for implicit methods, we need to take account of the fact that $f ( y _ { n } )$ is also being calculated. We have

$$
\begin{array} { l } { y ( x _ { n } ) - y _ { n } - h \beta _ { 0 } ( f ( y ( x _ { n } ) ) - f ( y _ { n } ) ) } \\ { \displaystyle = y ( x _ { n } ) - \sum _ { i = 1 } ^ { k } \alpha _ { i } y ( x _ { n - i } ) - h \sum _ { i = 0 } ^ { k } \beta _ { i } y ^ { \prime } ( x _ { n - 1 } ) , } \end{array}
$$

which is equal to

$$
C _ { p + 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) + O ( h ^ { p + 2 } ) .
$$

In this informal discussion, we not only ignore the term $O ( h ^ { p + 2 } )$ but also treat the value of $h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n - i } )$ as constant. This is justified in a local sense. That is, if we confine ourselves to a finite sequence of steps preceding step $n$ , then the variation in values of this quantity will also be $O ( h ^ { p + 2 } )$ , and we ignore such quantities. Furthermore, if

$$
y ( x _ { n } ) - y _ { n } - h \beta _ { 0 } ( f ( y ( x _ { n } ) ) - f ( y _ { n } ) ) \approx C _ { p + 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) ,
$$

then the assumption that $f$ satisfies a Lipschitz condition will imply that

$$
y ( x _ { n } ) - y _ { n } \approx C _ { p + 1 } h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } )
$$

and that

$$
h ( f ( y ( x _ { n } ) ) - f ( y _ { n } ) ) = O ( h ^ { p + 2 } ) .
$$

With the contributions of terms of this type thrown into the $O ( h ^ { p + 2 } )$ category, and hence capable of being ignored from the calculation, we can write a difference equation for the error in step $n$ , which will be written as $\epsilon _ { n } = y ( x _ { n } ) - y _ { n }$ , in the form

$$
\epsilon _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } \epsilon _ { n - i } = K h ^ { p + 1 } ,
$$

where $K$ is a representative value of $C _ { p + 1 } { \boldsymbol { y } } ^ { ( p + 1 ) }$

For a stable consistent method, the solution of this equation takes the form

$$
\epsilon _ { n } = - \alpha ^ { \prime } ( 1 ) ^ { - 1 } h ^ { p + 1 } n K + \sum _ { i = 1 } ^ { k } \eta _ { i } \lambda _ { i } ^ { n } ,
$$

where the coefficients $\eta _ { i }$ , $i = 1 , 2 , \ldots , k$ , depend on initial values and $\lambda _ { i }$ , $i = 1 , 2 , \ldots , k$ , are the solutions to the polynomial equation $\alpha ( \lambda ^ { - 1 } ) = 0$ .

The factor $- \alpha ^ { \prime } ( 1 ) ^ { - 1 }$ that occurs in (420a) can be written in a variety of forms, and we have

$$
- \alpha ^ { \prime } ( 1 ) = \rho ^ { \prime } ( 1 ) = \beta ( 1 ) = \sigma ( 1 ) = \alpha _ { 1 } + 2 \alpha _ { 2 } + \cdot \cdot \cdot + k \alpha _ { k } .
$$

The value of $- C \alpha ^ { \prime } ( 1 ) ^ { - 1 }$ is known as the ‘error constant’ for the method and represents the factor by which $h ^ { p + 1 } y ^ { ( p + 1 ) }$ must be multiplied to give the contribution from each step to the accumulated error. Since the method is assumed to be stable, the terms of the form $\eta _ { i } \lambda _ { i } ^ { n }$ can be disregarded compared with the linearly growing term $- \alpha ^ { \prime } ( 1 ) ^ { - 1 } h ^ { p + 1 } n K$ . If the integration is carried out to a specific output value $\scriptstyle { \overline { { x } } }$ , and $n$ steps are taken to achieve this result, then $h n = \overline { { x } } - x _ { 0 }$ . In this case we can make a further simplification and write the accumulated error as approximately

$$
- ( \overline { { x } } - x _ { 0 } ) \alpha ^ { \prime } ( 1 ) ^ { - 1 } h ^ { p } C y ^ { ( p + 1 ) } ( \overline { { x } } ) .
$$

In the next subsection, these ideas will be discussed further.

# 421 Further remarks on error growth

In Subsection 420 we gave an informal argument that, over many steps, there is a contribution to the accumulated error from step $n$ of approximately $- \alpha ^ { \prime } ( 1 ) ^ { - 1 } C _ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) h ^ { p + 1 }$ . Since we are interested in the effect of this contribution at some future point $\scriptstyle { \overline { { x } } }$ , we can consider the differential equation

$$
y ^ { \prime } ( x ) = f ( x , y ( x ) ) ,
$$

with two possible initial values at the point $ { \boldsymbol { x } } \ = \  { \boldsymbol { x } } _ { n }$ . These possible initial values are

$$
y ( x _ { n } ) \qquad { \mathrm { a n d } } \qquad y ( x _ { n } ) + \alpha ^ { \prime } ( 1 ) ^ { - 1 } C _ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) h ^ { p + 1 } ,
$$

and correspond respectively to the exact solution and to the solution perturbed by the error introduced in step $n$ .

This suggests the possibility of analysing the development of numerical errors through the differential equation

$$
z ^ { \prime } ( x ) = { \frac { \partial f ( y ( x ) ) } { \partial y } } z ( x ) + y ^ { ( p + 1 ) } ( x ) , \qquad z ( x _ { 0 } ) = 0 .
$$

![](images/ad95689aaa97c28acc8b441c3510fb2dcad8aa2b56d959957216ee28cd73602b.jpg)  
Development of accumulated errors in a single step

Using this equation, we might hope to be able to approximate the error after $n$ steps have been performed as

$$
- \alpha ^ { \prime } ( 1 ) ^ { - 1 } C _ { p + 1 } h ^ { p } z ( x _ { n } ) ,
$$

because the linear term in (421a) expresses the rate of growth of the separation of an already perturbed approximation and the non-linear term, when scaled by $- \alpha ^ { \prime } ( 1 ) ^ { - 1 } C _ { p + 1 } h ^ { p }$ , expresses the rate at which new errors are introduced as further steps are taken. The negative sign is consistent with the standard convention that errors are interpreted to mean the exact solution minus the approximation.

To turn this idea into a formal result it is possible to proceed in two steps. In the first step, asymptotic approximations are made. In the second, the errors in making these approximations are bounded and estimated so that they can all be bundled together in a single term which tends to zero more rapidly as $h  0$ than the asymptotic approximation to the error.

The second of these steps will not be examined in detail and the first step will be described in terms of the diagram given in Figure $4 2 1 ( \mathrm { i } ) .$ In this figure, $y ( x )$ is the exact solution and ${ \widehat { y } } ( x )$ is the function $y ( x ) + \alpha ^ { \prime } ( 1 ) ^ { - 1 } C _ { p + 1 } h ^ { p } z ( x )$ .

The function ${ \overline { { y } } } ( x )$  is the exact solution to the differential equation but with initial value at $x _ { n - 1 }$ set to $\widehat { y } ( x _ { n - 1 } )$ . In the single step from $x _ { n - 1 }$ to $x _ { n }$ , the perturbed approximation $\overline { y }$ drifts away from $y$ at an approximate rate $\left( \partial f ( y ( x ) ) / \partial y \right) \left( \overline { { y } } ( x ) - y ( x ) \right)$ , to reach a value $\overline { { y } } ( x _ { n } )$ . Add to this the contribution of local truncation error, corresponding to this step, denoted by $\begin{array} { r c l } { { \delta _ { n } } } & { { = } } & { { \alpha ^ { \prime } ( 1 ) ^ { - 1 } C _ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } ) h ^ { p + 1 } } } \end{array}$ . With this local error added, the accumulated error moves to a value ${ \widehat { y } } ( x _ { n } )$ . However, following the smoothedout curve ${ \widehat { y } } ( x )$ over the interval $[ x _ { n - 1 } , x _ { n } ]$ leads to the same point, to within $O ( h ^ { p + 2 } )$ .

# 422 The underlying one-step method

Although linear multistep methods seem to be at the opposite end of the spectrum from Runge–Kutta methods, there is a very close link between them. Suppose the method $\lfloor \alpha , \beta \rfloor$ is preconsistent and stable, and consider the equation

$$
\begin{array} { r l } & { 1 - \alpha _ { 1 } \eta ^ { - 1 } - \alpha _ { 2 } \eta ^ { - 2 } - \cdot \cdot \cdot - \alpha _ { k } \eta ^ { - k } } \\ & { \qquad - \beta _ { 0 } D - \beta _ { 1 } \eta ^ { - 1 } D - \beta _ { 2 } \eta ^ { - 2 } D - \cdot \cdot \cdot - \beta _ { k } \eta ^ { - k } D = 0 , } \end{array}
$$

where $\eta ~ \in ~ G _ { 1 }$ . In Theorem 422A, we will show that (422a) has a unique solution.

Although $\eta$ does not represent a Runge–Kutta method, it does represent a process for progressing a numerical approximation through a single time step. Suppose that the method is started using

$$
y _ { i } = y ( x _ { 0 } ) + \sum _ { t \in T } { \frac { \eta ^ { i } ( t ) h ^ { r ( t ) } } { \sigma ( t ) } } F ( t ) ( y ( x _ { 0 } ) ) , \quad i = 0 , 1 , 2 , \ldots , k - 1 ,
$$

corresponding to the group element $\eta ^ { i }$ ; then this value of $y _ { i }$ will persist for $i = k , k + 1 , \ldots .$ We will show this formally in Theorem 422C.

In the meantime, we remark that convergence of the formal series associated with $\eta ^ { i }$ is not assured, even for $i = 1$ , unless the function $f$ and the value of $h$ are restricted in some appropriate way. In this sense we can regard these ‘B-series’ as formal Taylor series.

What we really want is not $\eta$ satisfying (422a) but the mapping $\Phi$ , say, which corresponds to it. If exponentiation of $\Phi$ is taken to denote compositions, or, for negative powers, compositions of the inverse mapping, then we want to be able to define $\Phi$ by

$$
\begin{array} { r l } & { \mathrm { i d } - \alpha _ { 1 } \Phi ^ { - 1 } - \alpha _ { 2 } \Phi ^ { - 2 } - \cdot \cdot \cdot - \alpha _ { k } \Phi ^ { - k } } \\ & { \quad - h \beta _ { 0 } f - h \beta _ { 1 } ( f \circ \Phi ^ { - 1 } ) - h \beta _ { 2 } ( f \circ \Phi ^ { - 2 } ) - \cdot \cdot \cdot - h \beta _ { k } ( f \circ \Phi ^ { - k } ) = 0 . } \end{array}
$$

Because the corresponding member of $G _ { 1 }$ can be evaluated up to any required order of tree, it is regarded as satisfactory to concentrate on this representation.

Theorem 422A For any preconsistent, stable linear multistep method $\lfloor \alpha , \beta \rfloor$ , there exists a member of the group $G _ { 1 }$ satisfying (422a).

P By preconsistency, $\textstyle \sum _ { i = 1 } ^ { k } \alpha _ { i } = 1$ . Hence, (422a) is satisfied in the case $t = \emptyset$ they each evaluate to zero. Now consider a tree $t$ with $r ( t ) > 0$ and assume

that

$$
\begin{array} { r l } & { 1 ( u ) - \alpha _ { 1 } \eta ^ { - 1 } ( u ) - \alpha _ { 2 } \eta ^ { - 2 } ( u ) - \cdot \cdot \cdot - \alpha _ { k } \eta ^ { - k } ( u ) } \\ & { \qquad - \beta _ { 0 } D ( u ) - \beta _ { 1 } \eta ^ { - 1 } D ( u ) - \beta _ { 2 } \eta ^ { - 2 } D ( u ) - \cdot \cdot \cdot - \beta _ { k } \eta ^ { - k } D ( u ) = 0 , } \end{array}
$$

is satisfied for every tree $u$ satisfying $r ( u ) < r ( t )$ . We will prove that there exists a value of $\eta ( t )$ such that this equation is also satisfied if $u$ is replaced by $t$ . The coefficient of $\eta ( t )$ in $\eta ^ { - \tau } ( t )$ is equal to $i ( - 1 ) ^ { r ( t ) }$ and there are no other terms in $\eta ^ { - i } ( t )$ with orders greater than $r ( t ) - 1$ . Furthermore, all terms on the right-hand side contain only terms with orders less than $r ( t )$ . Hence, to satisfy (422a), with both sides evaluated at $t$ , it is only necessary to solve the equation

$$
( - 1 ) ^ { r ( t ) - 1 } \sum _ { i = 1 } ^ { k } i \alpha _ { i } \eta ( t ) = C ,
$$

where $C$ depends only on lower order trees. The proof by induction on $r ( t )$ is now complete, because the coefficient of $\eta ( t )$ is non-zero, by the stability of the method. $\boxed { \begin{array} { r l } \end{array} }$

Definition 422B Corresponding to a linear multistep method $\lfloor \alpha , \beta \rfloor$ , the member of $G _ { 1 }$ represents the ‘underlying one-step method’.

As we have already remarked, the mapping $\Phi$ in (422b), if it exists in more than a notional sense, is really the object of interest and this really is the underlying one-step method.

Theorem 422C Let $[ \alpha , \beta ]$ denote a preconsistent, stable linear multistep method and let $\eta$ denote a solution of (422a). Suppose that $y _ { i }$ is represented by $\eta ^ { i }$ for $i = 0 , 1 , 2 , \ldots , k - 1$ ; then $y _ { i }$ is represented by $\eta ^ { i }$ for $i = k , k + 1 , \ldots .$ .

Proof. The proof is by induction, and it will only be necessary to show that $y _ { k }$ is represented by $\eta ^ { k }$ , since this is a typical case. Multiply (422a) on the left by $\eta ^ { k }$ and we find that

$$
\begin{array} { r } { \eta ^ { k } - \alpha _ { 1 } \eta ^ { k - 1 } - \alpha _ { 2 } \eta ^ { k - 2 } - \cdot \cdot \cdot - \alpha _ { k } \qquad } \\ { - \beta _ { 0 } \eta ^ { k } D - \beta _ { 1 } \eta ^ { k - 1 } D - \beta _ { 2 } \eta ^ { k - 2 } D - \cdot \cdot \cdot - \beta _ { k } D = 0 , } \end{array}
$$

so that $y _ { k }$ is represented by $\eta ^ { k }$ .

The concept of an underlying one-step method was introduced by Kirchgraber (1986). Although the underlying method cannot be represented as a Runge–Kutta method, it can be represented as a B-series or, what is equivalent, in the manner that has been introduced here. Of more recent developments, the extension to general linear methods (Stoffer, 1993) is of particular interest. This generalization will be considered in Subsection 535.

# 423 Weakly stable methods

The stability requirement for linear multistep methods specifies that all zeros of the polynomial $\rho$ should lie in the closed unit disc with only simple zeros on the boundary. There is always a zero at 1, because of consistency, and there may or may not be other zeros on the boundary. We show in Subsection 441 that for a $k$ -step method, with $k$ even, the maximum possible order is $k + 2$ . For methods with this maximal order, it turns out that all zeros of $\rho$ lie on the unit circle and we are forced to take these methods seriously. We will write methods in the $[ \alpha , \beta ]$ terminology. A classic example is

$$
\begin{array} { l } { \alpha ( z ) = 1 - z ^ { 2 } , } \\ { \beta ( z ) = 2 z } \end{array}
$$

and this is known as the ‘leapfrog method’. Methods based on Newton–Cotes formulae were promoted by Milne (1953), and these all fall into this family.

The presence of additional zeros (that is, in addition to the single zero required by consistency) on the unit circle leads to the phenomenon known as ‘weak stability’.

A characteristic property of weakly stable methods is their difficulty in dealing with the long term integration of dissipative problems. For example, if an approximation to the solution of $y ^ { \prime } = - y$ is attempted using (423a), the difference equation for the computed results is

$$
y _ { n } + 2 h y _ { n - 1 } - y _ { n - 2 } = 0 .
$$

The general solution to (423c) is

$$
y _ { n } = A \lambda ^ { n } + B \mu ^ { n } ,
$$

where

$$
\begin{array} { l r } { \lambda ~ = ~ - h + \sqrt { 1 + h ^ { 2 } } ~ \approx ~ 1 - h + \frac { 1 } { 2 } h ^ { 2 } ~ \approx ~ \exp ( - h ) , } \\ { \mu ~ = ~ - h - \sqrt { 1 + h ^ { 2 } } ~ \approx ~ - 1 - h - \frac { 1 } { 2 } h ^ { 2 } ~ \approx ~ - \exp ( h ) , } \end{array}
$$

where $A$ and $B$ depend on initial values. Substitute the approximate values of $\lambda$ and $\mu$ into (423d) and we find

$$
y _ { n } \approx A \exp ( - n h ) + B ( - 1 ) ^ { n } \exp ( n h ) .
$$

For high values of $n$ , the second term, which represents a parasitic solution, eventually dominates the solution and produces a very poor approximation. This is in contrast to what happens for the differential equation $y ^ { \prime } = y$ , for which the solution to the corresponding difference equation takes the form $y _ { n } \approx A \exp ( n h ) + B ( - 1 ) ^ { n } \exp ( - n h )$ . In this case, the first term again corresponds to the true solution, but the second term will always be less significant.

# 424 Variable stepsize

If a sequence of approximations has already been computed using a specific stepsize and, for some reason, a decision is made to alter the stepsize, then a number of options arise as to how this might be done. For example, if a doubling of the stepsize is called for, then the necessary data might already be available without further computation. Halving the stepsize is not so convenient because new approximations to $y ( x )$ and $y ^ { \prime } ( x )$ are required at points intermediate to the information that has already been computed. However, both these are special cases and it is usually required to change the stepsize by a ratio that is perhaps greater than 0.5 and less than 2.0. We consider a very simple model example in which new values are simply found by interpolation and the integration resumed using the modified data. Another approach which we will also consider is where a generalized version of the numerical method is defined specific to whatever sequence of stepsizes actually arises.

We now examine some basic stability questions arising from the interpolation option applied to an Adams method. At the end of step $n$ , besides an approximation to $y ( x _ { n } )$ , approximations are available for $h y ^ { \prime } ( x _ { n } )$ , $h y ^ { \prime } ( x _ { n } \textrm { -- } h )$ , . . . , $h y ^ { \prime } ( x _ { n } \textrm { -- } ( p \textrm { -- } 1 ) h )$ . We need to replace these derivative approximations by approximations to $r h y ^ { \prime } ( x _ { n } )$ , $r h y ^ { \prime } ( x _ { n } - r h )$ , . . . , $r h y ^ { \prime } ( x _ { n } -$ $( p - 1 ) r h )$ , and these can be evaluated by the interpolation formula

$$
\left[ \begin{array} { c } { r h y ^ { \prime } ( x _ { n } ) } \\ { r h y ^ { \prime } ( x _ { n } - r h ) } \\ { \vdots } \\ { r h y ^ { \prime } ( x _ { n } - ( p - 1 ) r h ) } \end{array} \right] \approx { \cal V } D ( r ) { \cal V } ^ { - 1 } \left[ \begin{array} { c } { h y ^ { \prime } ( x _ { n } ) } \\ { h y ^ { \prime } ( x _ { n } - h ) } \\ { \vdots } \\ { h y ^ { \prime } ( x _ { n } - ( p - 1 ) h ) } \end{array} \right] ,
$$

where $V$ is the Vandermonde matrix

$$
V = { \left[ \begin{array} { l l l l l l } { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { 1 } & { 1 } & { 1 } & { \cdots } & { 1 } \\ { 1 } & { 2 } & { 2 ^ { 2 } } & { \cdots } & { 2 ^ { p - 1 } } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } \\ { 1 } & { p - 1 } & { ( p - 1 ) ^ { 2 } } & { \cdots } & { ( p - 1 ) ^ { p - 1 } } \end{array} \right] }
$$

and

$$
D ( r ) = \mathrm { d i a g } ( r , r ^ { 2 } , r ^ { 3 } , \ldots , r ^ { p } ) .
$$

The additional errors introduced into the computation by this change of stepsize technique can be significant. However, we are concerned here by the effect on stability. With constant stepsize, the stability of the difference equation system related to the derivative approximations is determined by

the influence matrix

$$
J = \left[ \begin{array} { l l l l l l } { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \end{array} \right]
$$

and because $J$ is nilpotent, the dependence of quantities computed in a particular step eventually becomes insignificant. However, whenever the stepsize is altered by a factor $r$ , the influence matrix becomes

$$
V D ( r ) V ^ { - 1 } J ,
$$

and this is, in general, not nilpotent. If, for example, the interpolation approach with stepsize ratio $r$ is repeated over many steps, then (424a) might not be power-bounded and unstable behaviour will result. In the case $p = 3$ , (424a) becomes

$$
\left[ \begin{array} { c c c } { { 0 } } & { { 0 } } & { { 0 } } \\ { { 2 r ^ { 2 } - r ^ { 3 } } } & { { - \frac { 1 } { 2 } r ^ { 2 } + \frac { 1 } { 2 } r ^ { 3 } } } & { { 0 } } \\ { { 4 r ^ { 2 } - 4 r ^ { 3 } } } & { { - r ^ { 2 } + 2 r ^ { 3 } } } & { { 0 } } \end{array} \right] ,
$$

and this is not power-bounded unless $r \leq 1 . 6 9 5 6 2 0 7 6 9 5 5 9 8 6$ , a zero of the polynomial $r ^ { 3 } - r ^ { 2 } - 2$ .

As an example of the alternative technique, in which the numerical method is modified to allow for irregular mesh spacing, consider the BDF3 method. Suppose that approximate solution values are known at $x _ { n - 1 }$ , $x _ { n } - h ( 1 + r _ { 2 } ^ { - 1 } )$ and $x _ { n } - h ( 1 + r _ { 2 } ^ { - 1 } + ( r _ { 2 } r _ { 1 } ) ^ { - 1 } )$ , where $r _ { 2 }$ and $r _ { 1 }$ are the most recent stepsize ratios. We now wish to compute $y ( x _ { n } )$ using a formula of the form

$$
\begin{array} { r } { y ( x _ { n } ) \approx h \beta y ^ { \prime } ( x _ { n } ) + \alpha _ { 1 } ( r _ { 1 } , r _ { 2 } ) y ( x _ { n } - h ) + \alpha _ { 2 } ( r _ { 1 } , r _ { 2 } ) y ( x _ { n } - h ( 1 + r _ { 2 } ^ { - 1 } ) ) } \\ { + \alpha _ { 3 } ( r _ { 1 } , r _ { 2 } ) y ( x _ { n } - h ( 1 + r _ { 2 } ^ { - 1 } + ( r _ { 2 } r _ { 1 } ) ^ { - 1 } ) ) . } \end{array}
$$

Using a result equivalent to Hermite interpolation, we find that, to maintain third order accuracy,

$$
\begin{array} { l } { \alpha _ { 1 } = \displaystyle \frac { ( r _ { 2 } + 1 ) ^ { 2 } ( r _ { 1 } r _ { 2 } + r _ { 1 } + 1 ) ^ { 2 } } { ( 3 r _ { 2 } ^ { 2 } r _ { 1 } + 4 r _ { 1 } r _ { 2 } + 2 r _ { 2 } + r _ { 1 } + 1 ) ( r _ { 1 } + 1 ) } , } \\ { \alpha _ { 2 } = - \displaystyle \frac { r _ { 2 } ^ { 2 } ( r _ { 1 } r _ { 2 } + r _ { 1 } + 1 ) ^ { 2 } } { 3 r _ { 2 } ^ { 2 } r _ { 1 } + 4 r _ { 1 } r _ { 2 } + 2 r _ { 2 } + r _ { 1 } + 1 } , } \\ { \alpha _ { 3 } = \displaystyle \frac { r _ { 2 } ^ { 2 } r _ { 1 } ^ { 3 } ( r _ { 2 } + 1 ) ^ { 2 } } { ( 3 r _ { 2 } ^ { 2 } r _ { 1 } + 4 r _ { 1 } r _ { 2 } + 2 r _ { 2 } + r _ { 1 } + 1 ) ( r _ { 1 } + 1 ) } . } \end{array}
$$

Stability of this variable stepsize version of the BDF3 method will hinge on the boundedness of products of matrices of the form

$$
M = \left[ \begin{array} { c c c } { { \alpha _ { 1 } } } & { { \alpha _ { 2 } } } & { { \alpha _ { 3 } } } \\ { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } \end{array} \right] ,
$$

where the values of $r _ { 1 }$ and $r _ { 2 }$ for successive members of the product sequence are appropriately linked together.

An extreme case will be where $r _ { 1 }$ and $r _ { 2 }$ are equal and as large as possible, subject to $M$ having bounded powers. It is easy to verify that this greatest rate of continual increase in stepsize corresponds to

$$
r _ { 1 } = r _ { 2 } = r ^ { * } = { \frac { 1 + { \sqrt { 5 } } } { 2 } } .
$$

It is interesting that an arbitrary sequence of stepsize change ratios, in the interval $( 0 , r ^ { * } ]$ , still guarantees stable behaviour.

# Exercises 42

42.1 Let $C ( \theta )$ denote the error constant for the third order linear multistep method (1−(1−θ)z −θz2, 5−θ12 $\begin{array} { r } { ( 1 - ( 1 - \theta ) z - \theta z ^ { 2 } , \frac { 5 - \theta } { 1 2 } + \frac { 2 + 2 \theta } { 3 } + \frac { 5 \theta - 1 } { 1 2 } z ^ { 2 } ) } \end{array}$ 5θ−112 z2). Show that C = $\begin{array} { r } { C = \frac { 1 - \theta } { 2 4 ( 1 + \theta ) } } \end{array}$ .

42.2 Show that weakly stable behaviour is experienced with the linear multistep method $( 1 - z ^ { 3 } , \frac { 3 } { 8 } ( 1 + z ) ^ { 3 } )$ .

42.3 Show that the norm of the product of an arbitrary sequence of matrices of the form (424b) is bounded as long as each $r$ lies in the interval $[ 0 , r ^ { * } ]$ , where $r ^ { * } \approx 1 . 6 9 5 6 2 0 7 6 9 5 5 9 8 6$ .

# 43 Stability Characteristics

# 430 Introduction

In contrast to Runge–Kutta methods, in which stability regions are determined by a single stability function, the stability properties of linear multistep methods are inextricably bound up with difference equations. We consider the example of the second order Adams–Bashforth method

$$
y _ { n } = y _ { n - 1 } + { \frac { 3 } { 2 } } h f ( x _ { n - 1 } , y _ { n - 1 } ) - { \frac { 1 } { 2 } } h f ( x _ { n - 2 } , y _ { n - 2 } ) .
$$

For the differential equation $y ^ { \prime } = q y$ , this becomes

$$
y _ { n } = y _ { n - 1 } + { \frac { 3 } { 2 } } h q y _ { n - 1 } - { \frac { 1 } { 2 } } h q y _ { n - 2 } ,
$$

![](images/acfaf47d423c409db6fa6d46d4f1b01832aab6824c8f03925ca3c5a8ba99abf1.jpg)  
Stability region for the second order Adams–Bashforth method

so that stable behaviour occurs if $h q = z$ , where $z$ is such that the equation

$$
y _ { n } = \Big ( 1 + \frac { 3 } { 2 } z \Big ) y _ { n - 1 } - \frac { 1 } { 2 } z y _ { n - 2 }
$$

has only bounded solutions. This occurs when the polynomial equation

$$
w ^ { 2 } - \Big ( 1 + \frac { 3 } { 2 } z \Big ) w + \frac { 1 } { 2 } z = 0
$$

has each of its two solutions in the closed unit disc and in the interior if they happen to coincide. The stability region for this method turns out to be the unshaded part of the complex plane shown in Figure 430(i), including the boundary.

Just as for Runge–Kutta methods, a consistent explicit linear multistep method has a bounded stability region and therefore cannot be A-stable. We therefore explore implicit methods as a source of appropriate algorithms for the solution of stiff problems. It will be found that A-stability is a very restrictive property in that it is incompatible with an order greater than 2. Also in this section, we consider a non-linear stability property, known as Gstability, which is a multistep counterpart of algebraic stability introduced in Chapter 3.

For a linear multistep method $[ \alpha , \beta ]$ , the difference equation associated with the linear test problem, $y ^ { \prime } = q y$ , is

$$
\begin{array} { r l r } {  { ( 1 - z \beta _ { 0 } ) y _ { n } - ( \alpha _ { 1 } + z \beta _ { 1 } ) y _ { n - 1 } - ( \alpha _ { 2 } + z \beta _ { 1 } ) y _ { n - 2 } - \cdots } } \\ & { } & { \qquad - ( \alpha _ { k } + z \beta _ { k } ) y _ { n - k } = 0 , } \end{array}
$$

and the stability region is the set of points $h q$ in the complex plane for which (431a) has only bounded solutions as $n \longrightarrow \infty$ . To simplify the discussion, we will consider the interior of the stability region so that, for $z$ in this set, all solutions to (431a) converge to zero as $n \longrightarrow \infty$ . We will refer to this interior set as the open stability region. Write the difference equation in the form

$$
\alpha ( E ^ { - 1 } ) - z \beta ( E ^ { - 1 } ) = 0 ,
$$

and we see that the open stability region can be defined in terms of the relation

$$
\alpha ( w ^ { - 1 } ) - z \beta ( w ^ { - 1 } ) = 0 .
$$

That is, $z$ is in the open stability region if there does not exist $w$ outside the open unit disc such that the pair $( z , w )$ satisfies (431b). Stated another way, this means that if $w$ outside the open unit disc this implies that $z$ satisfying (431b) is not in the open stability region.

As a starting point in determining the stability region, it is convenient to evaluate the points on the boundary of the unit circle and to note that the mapping

$$
w \mapsto { \frac { \alpha ( w ^ { - 1 } ) } { \beta ( w ^ { - 1 } ) } }
$$

traces out a set of points which includes the boundary of the stability region. In particular cases it is easy to determine the exact boundary. Since $w \mapsto w ^ { - 1 }$ maps the unit circle to itself, while changing the sense of rotation, it is equivalent to replace (431c) by

$$
w \mapsto { \frac { \alpha ( w ) } { \beta ( w ) } } .
$$

This procedure is known as the ‘boundary locus method’ for determining stability regions, and we give some examples of its use in the next subsection.

A second procedure for determining stability regions is based on the idea of the ‘type of a polynomial’. That is, if $P$ is a polynomial of degree $n$ then the type is a triple $( n _ { 1 } , n _ { 2 } , n _ { 3 } )$ , where $n _ { 1 }$ , $n _ { 2 }$ and $n _ { 3 }$ are non-negative integers with sum exactly $n$ . The interpretation is that $n _ { 1 }$ is the number of zeros of $P$ in the open unit disc, $n _ { 2 }$ is the number of zeros on the unit circle and $n _ { 3 }$ is the number of zeros outside the closed unit disc. If we are willing to concentrate on the open stability region of a specific method, we can simplify the discussion to the question of determining whether or not the type of $P$ is $( n , 0 , 0 )$ . We will refer to such a polynomial as being ‘strongly stable’. Polynomials can be tested for this property recursively, using the following result:

Theorem 431A A polynomial $P _ { n }$ , given by

$$
P _ { n } ( w ) = a _ { 0 } w ^ { n } + a _ { 1 } w ^ { n - 1 } + \cdots + a _ { n - 1 } w + a _ { n } ,
$$

where $a _ { 0 } \neq 0$ and $n \geq 2$ , is strongly stable if and only if

$$
| a _ { 0 } | ^ { 2 } > | a _ { n } | ^ { 2 }
$$

and $P _ { n - 1 }$ is strongly stable, where

$$
\begin{array} { r l } & { P _ { n - 1 } ( w ) } \\ & { \quad = ( \overline { { a } } _ { 0 } a _ { 0 } - a _ { n } \overline { { a } } _ { n } ) w ^ { n - 1 } + ( \overline { { a } } _ { 0 } a _ { 1 } - a _ { n } \overline { { a } } _ { n - 1 } ) w ^ { n - 2 } + \cdot \cdot \cdot + ( \overline { { a } } _ { 0 } a _ { n - 1 } - a _ { n } \overline { { a } } _ { 1 } ) . } \end{array}
$$

Proof. First note that (431e) is necessary for strong stability because if it were not true, the product of the zeros could not have a magnitude less than 1. Hence, we assume that this is the case and it remains to prove that $P _ { n }$ is strongly stable if and only if the same property holds for $P _ { n - 1 }$ . It is easy to verify that

$$
w P _ { n - 1 } ( w ) = \overline { { { a } } } _ { 0 } P _ { n } ( w ) - a _ { n } w ^ { n } \overline { { { P _ { n } ( \overline { { { w } } } ^ { - 1 } ) } } } .
$$

By Rouch´e’s theorem, $w P _ { n - 1 } ( w )$ has $n$ zeros in the open unit disc if and only if the same property is true for $P _ { n } ( w )$ , and the result follows. $\boxed { \begin{array} { r l } \end{array} }$

The result of this theorem is often referred to as the Schur criterion. In the case of $n = 2$ , it leads to the two conditions

$$
\begin{array} { r l r } & { } & { | a _ { 0 } | ^ { 2 } - | a _ { 2 } | ^ { 2 } > 0 , } \\ & { } & { ( | a _ { 0 } | ^ { 2 } - | a _ { 2 } | ^ { 2 } ) ^ { 2 } - | \overline { { a } } _ { 0 } a _ { 1 } - a _ { 2 } \overline { { a } } _ { 1 } | ^ { 2 } > 0 . } \end{array}
$$

To apply the Schur criterion to the determination of the stability region for a $k$ -step method, we need to ask for which $z$ the polynomial given by

$$
P ( w ) = w ^ { k } ( \alpha ( w ^ { - 1 } ) - z \beta ( w ^ { - 1 } ) )
$$

is strongly stable. We present some examples of the use of this test in Subsection 433.

Algorithm $\mathbf { 4 3 2 } \alpha$ Boundary locus method for low order Adams–Bashforth methods   

<table><tr><td></td><td>% Second order</td></tr><tr><td>%</td><td></td></tr><tr><td></td><td>W = exp(i*linspace(O,2*pi));</td></tr><tr><td></td><td>Z = 2*W.*(w-1)./(3*w-1);</td></tr><tr><td>plot(z)</td><td></td></tr><tr><td></td><td>% Third order</td></tr><tr><td>%</td><td></td></tr><tr><td></td><td>W=exp(i*linspace(O,2*pi));</td></tr><tr><td>plot(z)</td><td>Z=12*(1-w)./(23*w-16*w.^2+5*w.^3);</td></tr><tr><td></td><td></td></tr><tr><td></td><td>% Fourth order</td></tr><tr><td>%</td><td>w=exp(i*linspace(O,2*pi));</td></tr><tr><td></td><td>Z=24*(1-w)./(55*w-59*w.^2+37*W.^3-9*W.^4);</td></tr><tr><td>plot(z)</td><td></td></tr></table>

# 432 Examples of the boundary locus method

The first example is for the second order Adams–Bashforth method (430a) for which (431c) takes the form

$$
w \mapsto \frac { 1 - w ^ { - 1 } } { \frac { 3 } { 2 } w ^ { - 1 } - \frac { 1 } { 2 } w ^ { - 2 } } .
$$

For $w = \exp ( i \theta )$ and $\theta \in [ 0 , 2 \pi ]$ , for points on the unit circle, we have $z$ values on the (possibly extended) boundary of the stability region given by

$$
z = \frac { \exp ( 2 i \theta ) - \exp ( i \theta ) } { \frac { 3 } { 2 } \exp ( i \theta ) - \frac { 1 } { 2 } } .
$$

The MATLAB code given in Algorithm $4 3 2 \alpha$ shows how this is done, and the boundary traced out is exactly as in Figure 430(i).

No confusion is possible as to which part of the complex plane divided by the boundary locus is the inside and which is the outside because, using an argument based on the Cauchy–Riemann equations, we note that the inside is always to the left of the path traced out as $w$ increases from 0 to $2 \pi$ . If we had used (431d) in place of (431c) then, of course, the path would have been traced in the opposite direction and the inside of the stability region would have been on the right. Note that in Algorithm $4 3 2 \alpha$ the third and fourth order cases are traced in the reverse direction. The stability region of the third Adams–Bashforth method, as computed by this algorithm, is given as the unshaded region of Figure 432(i).

![](images/e77f29dc130d7a2a35381330699d26765121ccaa34ee6e9abd8c387db9d332c1.jpg)  
Stability region for the third order Adams–Bashforth method

![](images/07ff1f92256924a1071a6f8d9511c39ea29bb5b69f8f4de78b511851fd15c853.jpg)  
Stability region for the fourth order Adams–Bashforth method

In the case of the fourth order method in this family, the root locus method traces out more than the boundary of the stability region, as we see in Figure 432(ii). Because crossing the locus corresponds to the shift of one of the growth factors from stable to unstable, the more heavily shaded region is doubly unstable in that it contains two unstable terms.

![](images/09e8b8d4758e6c8c9f7d092e1999510f9725d3ab6153c8191ab1e0af41fa0838.jpg)  
Stability region for the third order Adams–Moulton method

![](images/e2847c06f9e73a7cf714b1df68beb7981b1376cd92baaad159e0aee554c17ba5.jpg)  
Stability region for the second order backward difference method

We present three final examples. The Adams–Moulton method of order 3 is given in Figure 432(iii); we see that even though this method is implicit it has a bounded stability region.

Now look at the stability regions of the backward difference methods of orders 2 and 3. The first of these, shown in Figure 432(iv), indicates that the second order method is A-stable and the second, Figure 432(v), shows that the third order method is not A-stable.

![](images/a966dc9c5a14da42a517c57e7dceef80612cb0da827417a8f79cb492916ce7ec.jpg)  
Stability region for the third order backward difference method

# 433 An example of the Schur criterion

We first recompute the stability region of the second order Adams–Bashforth method. We need to find for what values of the complex number $z$ the polynomial $a _ { 0 } w ^ { 2 } + a _ { 1 } w + a _ { 2 }$ has its zeros in the open unit disc, where

$$
a _ { 0 } = 1 , \qquad a _ { 1 } = - 1 - { \frac { 3 } { 2 } } z , \qquad a _ { 2 } = { \frac { z } { 2 } } .
$$

The condition $| a _ { 0 } | ^ { 2 } - | a _ { 2 } | ^ { 2 } > 0$ is equivalent to

$$
| z | < 2 ,
$$

while the second condition $( | a _ { 0 } | ^ { 2 } - | a _ { 2 } | ^ { 2 } ) ^ { 2 } - | \overline { { { a } } } _ { 0 } a _ { 1 } - a _ { 2 } \overline { { { a } } } _ { 1 } | ^ { 2 } > 0$ simplifies to

$$
\mathrm { R e } ( z ) ( 3 | z | ^ { 2 } - 4 ) < | z | ^ { 4 } .
$$

It is easy to verify that (433b) implies (433a). Thus, by plotting the points for which (433b) holds, we recover Figure $4 3 0 ( \mathrm { i } )$ .

# 434 Stability of predictor–corrector methods

We consider examples of PEC and PECE methods. For the PEC method based on second order Adams–Bashforth as predictor and Adams–Moulton as corrector, we have the following equations for the predicted and corrected values:

$$
\begin{array} { l } { { y _ { n } ^ { * } = y _ { n - 1 } + \displaystyle \frac { 3 } { 2 } h f _ { n - 1 } ^ { * } - \displaystyle \frac { 1 } { 2 } h f _ { n - 2 } ^ { * } , } } \\ { { y _ { n } = y _ { n - 1 } + \displaystyle \frac { 1 } { 2 } h f _ { n } ^ { * } + \displaystyle \frac { 1 } { 2 } h f _ { n - 1 } ^ { * } . } } \end{array}
$$

![](images/ee04c8a3dee460a681acb16f7c1aacb063907f1bfc23ccb2ee30f36ef0985915.jpg)  
Stability regions for Adams–Moulton methods (solid lines) and PEC methods (dashed lines)

Superficially, this system describes two sequences, the $y$ and the $y ^ { * }$ which develop together. However, it is only the $y ^ { * }$ sequence that has derivative values associated with it. Hence, the $y$ sequence can conveniently be eliminated from consideration. Replace $n$ by $n + 1$ in (434a), and we find

$$
y _ { n + 1 } ^ { * } = y _ { n } + { \frac { 3 } { 2 } } h f _ { n } ^ { * } - { \frac { 1 } { 2 } } h f _ { n - 1 } ^ { * } .
$$

Add (434b) to this equation and subtract (434a), and we find

$$
y _ { n + 1 } ^ { * } = y _ { n } ^ { * } + 2 h f _ { n } ^ { * } - { \frac { 3 } { 2 } } h f _ { n - 1 } ^ { * } + { \frac { 1 } { 2 } } h f _ { n - 2 } ^ { * } .
$$

Apart from the actual values of the coefficients, this resembles an Adams– Bashforth method, and its stability region can be found in a similar way. If $\beta ^ { * }$ and $\beta$ are the respective generating polynomials for an order $p$ Adams– Bashforth method and the corresponding Adams–Moulton method, then the general form of the generating polynomial for $y ^ { * }$ in a PEC method is equal to $\widehat { \beta }$ , where

$$
\widehat { \beta } ( z ) = \beta ^ { \ast } ( z ) + \beta _ { 0 } z ( 1 - z ) ^ { p } .
$$

The value of $\beta _ { 0 }$ could be replaced by any value we wish without sacrificing the order $p$ . In fact, it could be replaced by the value of $( - 1 ) ^ { p } \beta _ { p + 1 } ^ { * }$ so that the method would actually be of order $p + 1$ . It would in this case be precisely the order $p + 1$ Adams–Bashforth method. Another advantage of pushing the order up one unit rather than accepting the standard PEC result, is that the stability region seems to be less desirable for PEC methods. This is illustrated in Figure 434(i), where the boundaries of some of these regions are shown.

![](images/8f04aebd1d960629206629689f80e8d1360d55beeb650d1887cf2744ee99c32e.jpg)  
Stability regions for PECE methods with $q = p$ (solid lines) and $q = p - 1$ methods (dashed lines). In each case $p$ is attached to the curves

PECE methods are more interesting because two derivatives are computed in each step. Thus they are in reality two-stage general linear methods. From the stability point of view, they can be analysed by eliminating $y _ { n } ^ { * }$ so that the method

$$
\begin{array} { l } { { \displaystyle y _ { n } ^ { * } = y _ { n - 1 } + h \sum _ { i = 1 } ^ { k } \beta _ { i } ^ { * } f _ { n - i } } , } \\ { { \displaystyle y _ { n } = y _ { n - 1 } + h \beta _ { 0 } f _ { n } ^ { * } + h \sum _ { i = 1 } ^ { k } \beta _ { i } f _ { n - i } } } \end{array}
$$

yields the difference equation

$$
y _ { n } = ( 1 + ( \beta _ { 0 } + \beta _ { 1 } ) z + \beta _ { 0 } \beta _ { 1 } ^ { * } z ^ { 2 } ) y _ { n - 1 } + \sum _ { i = 2 } ^ { k } ( \beta _ { i } z + \beta _ { 0 } \beta _ { i } ^ { * } z ^ { 2 } ) y _ { n - i } .
$$

Note that the step $k$ may be higher for the predictor than for the corrector but we assume that, if this is the case, sufficient zero values are added to the sequence of $\beta _ { i }$ values to make the two $k$ values effectively equal. In practice there are two options. Either both the predictor and corrector have the same order $p$ , in which case $k = p$ for the predictor and $k = p - 1$ for the corrector; or $k = p - 1$ for both predictor and corrector; in this case the predictor has order only $p - 1$ . The boundaries of the stability regions are shown in Figure 434(ii) for each of these cases.

The relatively more generous stability regions for the PECE methods, when compared with PEC methods, for $p ~ > ~ 1$ are regarded as constituting a significant advantage in carrying out a final evaluation in implementations of predictor–corrector methods. Similar comparisons apparently favour PECECE over PECE methods.

# Exercises 43

43.1 Use the Schur criterion to show that all zeros of the polynomial $7 z ^ { 3 } - 1 1 z ^ { 2 } + 5 z + 1$ lie in the unit disc.

43.2 Use the Schur criterion to show that not all zeros of the polynomial $7 z ^ { 3 } - 1 1 z ^ { 2 } + 6 z + 1$ lie in the unit disc.

43.3 Determine whether or not all zeros of the polynomial $7 z ^ { 3 } - 1 1 z ^ { 2 } + ( 5 +$ $i ) z + 1$ lie in the unit disc.

43.4 Find the stability regions for the PEC and PECE methods based on the fourth order Adams–Bashforth and Adams–Moulton methods.

# 44 Order and Stability Barriers

440 Survey of barrier results

It is a simple matter to construct a linear $k$ -step method with order $2 k$ . This can be done, for example, by finding coefficients $A _ { j }$ , $B _ { j }$ , $j = 0 , 1 , \ldots , k$ , such that

$$
{ \frac { 1 } { z ^ { 2 } ( z + 1 ) ^ { 2 } ( z + 2 ) ^ { 2 } \cdots ( z + k ) ^ { 2 } } } = \sum _ { j = 0 } ^ { k } { \frac { A _ { j } } { z + j } } + \sum _ { j = 0 } ^ { k } { \frac { B _ { j } } { ( z + j ) ^ { 2 } } }
$$

and then defining

$$
\alpha _ { j } = - { \frac { A _ { j } } { A _ { 0 } } } , \quad j = 1 , 2 , \ldots , k , \qquad \beta _ { j } = { \frac { B _ { j } } { A _ { 0 } } } , \quad j = 0 , 1 , \ldots , k .
$$

To justify this remark, consider the contour integral

$$
{ \frac { 1 } { 2 \pi i } } \oint _ { C } { \frac { \phi ( z ) d z } { \prod _ { j = 0 } ^ { k } ( z + j ) ^ { 2 } } } = \sum _ { j = 0 } ^ { k } { \frac { 1 } { 2 \pi i } } \oint _ { C } \phi ( z ) \left( { \frac { A _ { j } } { z + j } } + { \frac { B _ { j } } { ( z + j ) ^ { 2 } } } \right) d z ,
$$

where the contour $C$ consists of a counter-clockwise circle of radius $R > k$ and centre at the origin and $\phi$ is a polynomial of degree not exceeding $2 k$ . By

taking $R$ large the value of the integral can be estimated by $O ( R ^ { - 1 } )$ ; because it is constant, it must be zero. On the other hand, the terms in the partial fraction representation of the integral are

$$
\sum _ { j = 0 } ^ { k } \left( A _ { j } \phi ( - j ) + B _ { j } \phi ^ { \prime } ( - j ) \right) .
$$

For example, if $k = 3$ , we have

$$
\begin{array} { r c l } { \displaystyle { \frac { 1 } { z ^ { 2 } ( z + 1 ) ^ { 2 } ( z + 2 ) ^ { 2 } } = - \frac { 1 1 } { 1 0 8 } \frac { 1 } { z } - \frac { 1 } { 4 } \frac { 1 } { z + 1 } + \frac { 1 } { 4 } \frac { 1 } { z + 2 } + \frac { 1 1 } { 1 0 8 } \frac { 1 } { z + 3 } } } \\ { \displaystyle { + \frac { 1 } { 3 6 } \frac { 1 } { z ^ { 2 } } + \frac { 1 } { 4 } \frac { 1 } { ( z + 1 ) ^ { 2 } } + \frac { 1 } { 4 } \frac { 1 } { ( z + 2 ) ^ { 2 } } + \frac { 1 } { 3 6 } \frac { 1 } { ( z + 3 ) ^ { 2 } } , } } \end{array}
$$

leading to the values

$$
\alpha _ { 1 } = - \frac { 2 7 } { 1 1 } , \quad \alpha _ { 2 } = \frac { 2 7 } { 1 1 } , \quad \alpha _ { 3 } = 1 ,
$$

so that the method is unstable.

This is an example of a result found by Dahlquist (1956), that order $p$ is impossible for a convergent method unless $p \leq k + 1$ if $k$ is odd, and $p \leq k + 2$ if $k$ is even.

With the recognition of the importance of stiffness came the property of A-stability (Dahlquist, 1963). It has been shown, also by Dahlquist, for Astable linear multistep methods that $p$ cannot exceed 2. This result is known as the second Dahlquist barrier, in contrast to the result about the order of a convergent $k$ -step method, which is usually referred to as the first Dahlquist barrier.

# 441 Maximum order for a convergent $k$ -step method

As a starting point for the proof we present of the Dahlquist first barrier, use Theorem 410B. Modify this by substituting $z$ in (410d) with the function

$$
\frac { 2 z } { 1 - z }
$$

and then multiplying throughout by $( 1 + z ) ^ { k }$ . We then have

$$
( 1 + z ) ^ { k } \alpha \Bigl ( \frac { 1 - z } { 1 + z } \Bigr ) - \log \Big ( \frac { 1 + z } { 1 - z } \Bigr ) ( 1 + z ) ^ { k } \beta \Bigl ( \frac { 1 - z } { 1 + z } \Bigr ) = O ( z ^ { p + 1 } ) ,
$$

or, what is equivalent,

$$
{ \frac { ( 1 + z ) ^ { k } \alpha \left( { \frac { 1 - z } { 1 + z } } \right) } { z } } { \frac { z } { \log \left( { \frac { 1 + z } { 1 - z } } \right) } } - ( 1 + z ) ^ { k } \beta \Bigl ( { \frac { 1 - z } { 1 + z } } \Bigr ) = O ( z ^ { p } ) .
$$

For the rest of this subsection, including assumptions within lemmas and theorems, we write

$$
\begin{array} { r l } & { a ( z ) = a _ { 0 } + a _ { 1 } z + a _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + a _ { k } z ^ { k } = ( 1 + z ) ^ { k } \alpha \big ( \frac { 1 - z } { 1 + z } \big ) , } \\ & { } \\ & { b ( z ) = b _ { 0 } + b _ { 1 } z + b _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + b _ { k } z ^ { k } \ = ( 1 + z ) ^ { k } \beta \big ( \frac { 1 - z } { 1 + z } \big ) . } \end{array}
$$

By consistency, $a _ { 0 } = 0$ so that (441a) can be written in the form

$$
\begin{array} { c } { { ( a _ { 1 } + a _ { 2 } z + \cdots + a _ { k } z ^ { k - 1 } ) ( c _ { 0 } + c _ { 2 } z ^ { 2 } + c _ { 4 } z ^ { 4 } + \cdots ) } } \\ { { { } } } \\ { { - ( b _ { 0 } + b _ { 1 } z + b _ { 2 } z ^ { 2 } + \cdots + b _ { k } z ^ { k } ) = O ( z ^ { p } ) , } } \end{array}
$$

where

$$
{ \frac { z } { \log \left( { \frac { 1 + z } { 1 - z } } \right) } } = c _ { 0 } + c _ { 2 } z ^ { 2 } + c _ { 4 } z ^ { 4 } + \cdot \cdot \cdot .
$$

The way we use this result, when we consider the possibility that $p > k$ , is to note that this implies that the coefficients of zk+1, , $z ^ { p - 1 }$ in

$$
( a _ { 1 } + a _ { 2 } z + \cdot \cdot \cdot + a _ { k } z ^ { k - 1 } ) ( c _ { 0 } + c _ { 2 } z ^ { 2 } + c _ { 4 } z ^ { 4 } + \cdot \cdot \cdot )
$$

are zero.

We will go about this is by establishing some results on the signs of the coefficients $a _ { 1 }$ , $a _ { 2 }$ , . . . , $a _ { k }$ , $c _ { 2 }$ , $c _ { 4 }$ , . . . .

Lemma 441A If the method under consideration is stable then $a _ { 1 } > 0$ and $a _ { i } \geq 0$ , for $i = 2 , 3 , \ldots , k$ .

Proof. Write the polynomial $a$ in the form

$$
a ( z ) = ( 1 + z ) ^ { k } - \alpha _ { 1 } ( 1 + z ) ^ { k - 1 } ( 1 - z ) - \alpha _ { 2 } ( 1 + z ) ^ { k - 2 } ( 1 - z ) ^ { 2 } - \cdot \cdot \cdot - \alpha _ { k } ( 1 - z ) ^ { k } .
$$

We calculate the value of $a _ { 1 }$ , the coefficient of $z$ , to be

$$
k - ( k - 2 ) \alpha _ { 1 } - ( k - 4 ) \alpha _ { 2 } - \cdot \cdot \cdot - ( - k ) \alpha _ { k } = k \alpha ( 1 ) - 2 \alpha ^ { \prime } ( 1 ) = - 2 \alpha ^ { \prime } ( 1 ) ,
$$

because $\alpha ( 1 ) = 0$ . The polynomial $\rho$ , which we recall is defined by

$$
\rho ( z ) = z ^ { k } - \alpha _ { 1 } z ^ { k - 1 } - \alpha _ { 2 } z ^ { k - 2 } - \cdot \cdot \cdot - \alpha _ { k } ,
$$

has no real zeros greater than 1, and hence, because $\rho ( 1 ) = 0$ and because $\begin{array} { r } { \operatorname* { l i m } _ { z - > \infty } \rho ( z ) = \infty } \end{array}$ , it is necessary that $\rho ^ { \prime } ( 1 ) > 0$ . Calculate this to be

$$
\rho ^ { \prime } ( 1 ) = k - ( k - 1 ) \alpha _ { 1 } - ( k - 2 ) \alpha _ { 2 } - \cdot \cdot \cdot - \alpha _ { k - 1 } = a _ { 1 } .
$$

This completes the proof that $a _ { 1 } > 0$ .

Write $\zeta$ for a possible zero of $a$ so that, because of the relationship between this polynomial and $\alpha$ , it follows that

$$
\frac { 1 - \zeta } { 1 + \zeta }
$$

is a zero of $\alpha$ , unless it happens that $\zeta = - 1$ , in which case there is a drop in the degree of $\alpha$ . In either case, we must have $\mathrm { R e } ( \zeta ) \leq 0$ . Because all zeros of $a$ are real, or occur in conjugate pairs, the polynomial $a$ can be decomposed into factors of the form $z - \xi$ or of the form $z ^ { 2 } - 2 \xi z + ( \xi ^ { 2 } + \eta ^ { 2 } )$ , where the real number $\xi$ cannot be positive. This means that all factors have only terms with coefficients of the same sign, and accordingly this also holds for $a$ itself. These coefficients must in fact be non-negative because $a _ { 1 } > 0$ . 

Lemma 441B The coefficients $c _ { 2 }$ , $c _ { 4 }$ , . . . are all negative.

Proof. Using the series for $\log { \big ( } ( 1 + z ) / ( 1 - z ) { \big ) } / z$ , we see that $c _ { 0 }$ , $c _ { 2 }$ , $c _ { 4 }$ , . . . satisfy

$$
\bigl ( 2 + { \frac { 2 } { 3 } } z ^ { 2 } + { \frac { 2 } { 5 } } z ^ { 4 } + \cdots \bigr ) ( c _ { 0 } + c _ { 2 } z ^ { 2 } + c _ { 4 } z ^ { 4 } + \cdots ) = 1 .
$$

It follows that $c _ { 0 } = \textstyle { \frac { 1 } { 2 } }$ , $c _ { 2 } = - \textstyle { \frac { 1 } { 6 } }$ . We prove $c _ { 2 n } < 0$ by induction for $n = 2$ , $n = 3$ , . . . . If $c _ { 2 i } < 0$ for $i = 1 , 2 , \dots , n - 1$ then we multiply (441c) by $2 n + 1 - ( 2 n - 1 ) z ^ { 2 }$ . We find

$$
\sum _ { i = 0 } ^ { \infty } d _ { 2 i } z ^ { 2 i } \cdot \sum _ { i = 0 } ^ { \infty } c _ { 2 i } z ^ { 2 i } = 2 n + 1 - ( 2 n - 1 ) z ^ { 2 } ,
$$

where, for $i = 1 , 2 , \ldots , n$ ,

$$
d _ { 2 i } = \frac { 2 ( 2 n + 1 ) } { 2 i + 1 } - \frac { 2 ( 2 n - 1 ) } { 2 i - 1 } = - \frac { 8 ( n - i ) } { ( 2 i + 1 ) ( 2 i - 1 ) } ,
$$

so that $d _ { 2 i } < 0$ , for $i = 1 , 2 , \dots , n - 1$ , and $d _ { 2 n } = 0$ . Equate the coefficients of $z ^ { 2 n }$ in (441d) and we find that

$$
c _ { 2 n } = - { \frac { c _ { 2 } d _ { 2 n - 2 } + c _ { 4 } d _ { 2 n - 4 } + \cdot \cdot \cdot + c _ { 2 n - 2 } d _ { 2 } } { d _ { 0 } } } < 0 .
$$

We are now in a position to prove the Dahlquist barrier result.

Theorem 441C Let $\lfloor \alpha , \beta \rfloor$ denote a stable linear multistep method with order $p$ . Then

$$
p \leq \left\{ \begin{array} { l l } { k + 1 , } & { k o d d , } \\ { k + 2 , } & { k e v e n . } \end{array} \right.
$$

Proof. Consider first the case $k$ odd and evaluate the coefficient of $z ^ { k + 1 }$ in (441b). This equals

$$
a _ { k } c _ { 2 } + a _ { k - 2 } c _ { 4 } + \cdot \cdot \cdot + a _ { 1 } c _ { k + 1 }
$$

and, because no term is positive, the total can be zero only if each term is zero.   
However, this would mean that $a _ { 1 } = 0$ , which is inconsistent with stability.

In the case $k$ even, we evaluate the coefficient of $z ^ { k + 2 }$ in (441b). This is

$$
a _ { k - 1 } c _ { 4 } + a _ { k - 3 } c _ { 6 } + \cdot \cdot \cdot + a _ { 1 } c _ { k + 2 } .
$$

Again, every term is non-positive and because the total is zero, it again follows that $a _ { 1 } = 0$ which contradicts the assumption of stability. 

There is some interest in the methods with maximal order $2 k + 2$ , for $k$ even. For these methods, $\alpha$ has all its zeros on the unit circle. This evidently gives the methods a symmetry that suggests it might be advantageous to use them for problems whose behaviour is dominated by linear terms with purely imaginary eigenvalues. Against this possible advantage is the observation that the stability regions necessarily have empty interiors.

# 442 Order stars for linear multistep methods

In their historic paper, Wanner, Hairer and Nørsett (1978) introduced order stars on Riemann surfaces. Suppose that $\Phi ( w , z )$ is a polynomial function of two complex variables, $w \in W$ and $z \in Z$ . We assume that $Z = W = \mathbb { C }$ . The subset $R _ { \Phi }$ of $W \times Z$ defined by the relation $\Phi ( w , z ) = 0$ is a Riemann surface. Suppose that $\Phi$ has degree $r$ in $w$ and $s$ in $z$ . We may interpret $R$ as a mapping from the $Z$ plane which takes $z \in { Z }$ to the set of zeros of the equation $\Phi ( w , z ) = 0$ or as a mapping which takes $w \in W$ to the set of zeros of this same equation, but with $z$ now the unknown. The main interpretation will be that $\Phi ( w , z )$ is the characteristic polynomial $\operatorname* { d e t } ( w I - M ( z ) )$ of the stability matrix of a multivalue method. If this method has order $p$ then $\Phi ( \exp ( z ) , z ) = O ( z ^ { p + 1 } )$ . For ease of notation, we carry over concepts such as A-stability from multivalue methods, such as linear multistep methods, to the functions $\Phi$ used to characterize their stability.

Definition 442A The function $\Phi$ is $A$ -stable if $R _ { \Phi }$ has no intersection with the product set

$$
\{ w \in \mathbb { C } : | w | > 1 \} \times \{ z \in \mathbb { C } : \operatorname { R e } ( z ) \leq 0 \} .
$$

This definition is equivalent to the requirement that for any $z$ in the left half complex plane, all eigenvalues of the stability matrix are in the closed unit disc. Just as in the case of Runge–Kutta methods, for which the Riemann surface has only a single sheet, scaling the eigenvalues by $\exp ( - z )$ does not affect the behaviour on the imaginary axis or introduce or remove any poles.

![](images/0d5fc24ca6cf5d995f03160f55bab594736148e18421141a0290f12ec0ea53b7.jpg)  
Order star for the second order BDF method

![](images/42453fafe8af643434068c41b8d3e62c41328cb2941911853571121924744803.jpg)  
Order star for the third order BDF method

Hence we can consider a modified Riemann surface based on the function $\Phi ( w \exp ( z ) , z )$ . Just as for the Runge–Kutta case, one of the sheets, known as the ‘principal sheet’, behaves like $w = 1 + O ( z ^ { p + 1 } )$ and order stars appear.

We illustrate this by considering the case of the second order backward difference method, for which

$$
\Phi ( w \exp ( z ) , z ) = \left( 1 - \frac { 2 } { 3 } z \right) \exp ( 2 z ) w ^ { 2 } - \frac { 4 } { 3 } \exp ( z ) w + \frac { 1 } { 3 } ,
$$

and the third order backward difference method, for which

$$
{ \mathfrak { s } } ( w \exp ( z ) , z ) = \left( 1 - { \frac { 6 } { 1 1 } } z \right) \exp ( 3 z ) w ^ { 3 } - { \frac { 1 8 } { 1 1 } } \exp ( 2 z ) w ^ { 2 } + { \frac { 9 } { 1 1 } } \exp ( z ) w - { \frac { 2 } { 1 1 } } .
$$

For the second order case, shown in Figure 442(i), a pole at $\begin{array} { r } { z = \frac { 3 } { 2 } } \end{array}$ is marked, together with a branch point at $\begin{array} { r } { z = - \frac { 1 } { 2 } } \end{array}$ . Note that for $z \in ( \infty , - \frac { 1 } { 2 } )$ , the two roots of the equation $\Phi ( w \exp ( z ) , z ) = 0$ , for all $z$ in this real interval, have equal magnitudes. In this figure, light shading grey indicates that a region has exactly one of the sheets with magnitude greater than 1. A darker grey is used to indicate that both sheets have magnitudes greater than 1.

This method is A-stable, as we already know. This can be seen from the order star by noting that the only pole is in the right half-plane, and that the fingers do not intersect the imaginary axis. On the other hand, the third order method (Figure 442(ii)) is not A-stable because, in this case, the intersection of the imaginary axis with one the fingers is now not empty. Note that for the third order case, there is a single pole at $\begin{array} { r } { z = \frac { 1 1 } { 6 } } \end{array}$ and that three shades of grey are used to distinguish regions where one, two or three sheets have magnitudes greater than 1.

Although A-stable Runge–Kutta methods can have arbitrarily high orders, the order of A-stable linear multistep methods is restricted to 2. This was first proved using order stars (Wanner, Hairer and Nørsett, 1978), but we will use the closely related approach of order arrows (Butcher, 2002). These will be introduced in the Riemann surface case in the next subsection.

# 443 Order arrows for linear multistep methods

Given a relationship between complex numbers $z$ and $w$ defined by an equation of the form

$$
\Phi ( w \exp ( z ) , z ) = 0 ,
$$

we can define order arrows as the set of points for which $w$ is real and positive. In particular, the order arrows that emanate from zero correspond to $w$ with increasing real parts (the up arrows) and, on these arrows, $w \in ( 1 , \infty )$ , or decreasing real parts (the down arrows) and for which $w \in [ 0 , 1 )$ .

Order arrows on Riemann surfaces are illustrated for the BDF2 method (Figure 443(i)) and for the BDF3 method (Figure 443(ii)). Just as for Runge– Kutta methods, the up arrows either terminate at the pole $z = \beta _ { 0 } ^ { - 1 }$ or at $- \infty$ , and down arrows terminate at the zero $z = - \alpha _ { k } \beta _ { k } ^ { - 1 }$ or at $+ \infty$ . In interpreting these remarks, we need to allow for the possibility that the path traced out by an up or down arrow meets another arrow at a branch point of the Riemann surface. However, this special case is easily included in the general rule with a possible freedom to choose between two continuations of the incoming arrow.

The ‘principal sheet’ of the Riemann surface will refer to a neighbourhood of $( 0 , 1 )$ for which the relationship between $z$ and $w$ is injective; that is, it behaves as though $w$ is a function of $z$ . As long as $\Phi ( w , 0 )$ has only a single zero with value $w = 1$ , this idea makes sense. On the principal sheet, $w \exp ( z ) = \exp ( z ) + { \cal O } ( z ^ { p + 1 } )$ , and the behaviour at zero is similar to what happens for one-step methods. These simple ideas are enough to prove the Dahlquist second order bound:

Theorem 443A An A-stable linear multistep method cannot have order greater than 2.

![](images/a6c48597940bcb930de1e2bc67a55aae50a0c81c3c6e4be3b281c5a5b6bb9dca.jpg)  
Order arrows for order 2 BDF method

![](images/caa015d4de9e48f4ea8095f1af08bf2c09164480b8a81be6793de475a78e01f0.jpg)  
Order arrows for order 3 BDF method

Proof. If the order were greater than 2, there would be more than three up arrows emanating from the origin. At least three of these up arrows would come out in the positive direction (or possibly would be tangential to the imaginary axis). Since there is only one pole, at least two of these arrows would cross the imaginary axis (or be tangential to it). Hence, the stability region does not include all of the imaginary axis and the method is not Astable. 

We can make this result more precise by obtaining a bound on the error constant for second order A-stable methods. The result yields an optimal role for the second order Adams–Moulton method, for which the error constant is $- { \frac { 1 } { 1 2 } }$ , because

$$
\exp ( z ) - \frac { 1 + \frac { 1 } { 2 } z } { 1 - \frac { 1 } { 2 } z } = - \frac { 1 } { 1 2 } z ^ { 3 } + O ( z ^ { 4 } ) .
$$

It is not possible to obtain a positive error constant amongst A-stable second order methods, and it is not possible to obtain an error constant smaller in magnitude than for the one-step Adams–Moulton method. To prove the result we use, in place of $\exp ( z )$ , the special stability function $( 1 + \textstyle { \frac { 1 } { 2 } } z ) / ( 1 - \textstyle { \frac { 1 } { 2 } } z )$ in forming a relative stability function.

Theorem 443B Let $C$ denote the error constant for an $A$ -stable second order linear multistep method. Then

$$
C \leq - { \frac { 1 } { 1 2 } } ,
$$

with equality only in the case of the second order Adams–Moulton method.

Proof. Consider the relation

$$
\Phi \left( w \frac { 1 + \frac { 1 } { 2 } z } { 1 - \frac { 1 } { 2 } z } , z \right) = 0 .
$$

On the principal sheet, $w = 1 - ( C + { \textstyle { \frac { 1 } { 1 2 } } } ) z ^ { 3 } + O ( z ^ { 4 } )$ . It is not possible that $\begin{array} { r } { C + \frac { 1 } { 1 2 } = 0 } \end{array}$ , because there would then be at least four up arrows emanating from 0 and, as in the proof of Theorem 443A, this is impossible because there is at most one pole in the right half-plane. On the other hand, if $C + { \textstyle { \frac { 1 } { 1 2 } } } > 0$ , there would be at least two up arrows emanating from zero in the positive direction and these must cross the imaginary axis. 

# Exercises 44

44.1 Show that, for a stable linear multistep method with order $k + 2$ , all zeros of $\alpha$ are on the unit circle.

44.2 Show that the BDF3 method is not A-stable, by selecting a complex number $x$ with negative real part for which the corresponding difference equation is not stable.

# 45 One-Leg Methods and G-stability

450 The one-leg counterpart to a linear multistep method

In Dahlquist (1976) one-leg methods were introduced. Given a linear multistep method defined by the generating polynomial pair $\lfloor \alpha , \beta \rfloor$ , an alternative method can be found by replacing the weighted sum of derivative values

$$
h \beta _ { 0 } f ( x _ { n } , y _ { n } ) + h \beta _ { 1 } f ( x _ { n - 1 } , y _ { n - 1 } ) + \cdot \cdot \cdot + h \beta _ { k } f ( x _ { n - k } , y _ { n - k } ) ,
$$

by the single term

$$
h \bigg ( \sum _ { i = 0 } ^ { k } \beta _ { i } \bigg ) f \bigg ( x _ { n } - \theta h , \bigg ( \sum _ { i = 0 } ^ { k } \beta _ { i } \bigg ) ^ { - 1 } \sum _ { i = 0 } ^ { k } \beta _ { i } y _ { n - i } \bigg ) ,
$$

where $\theta$ is a weighted combination of the step numbers

$$
\theta = \frac { \sum _ { i = 0 } ^ { k } i \beta _ { i } } { \sum _ { i = 0 } ^ { k } \beta _ { i } } .
$$

For convenience, we write

$$
\widehat { \beta } _ { i } = \frac { \beta _ { i } } { \sum _ { i = 0 } ^ { k } \beta _ { i } } , \qquad i = 0 , 1 , 2 , \ldots , k .
$$

It is obvious that the linear stability of a one-leg method is the same as for the corresponding linear multistep method. However, it is possible to investigate the stability of numerical solutions of non-linear dissipative equations in a relatively simple way if the computation is carried out using one-leg methods. By contrast, the corresponding analysis for linear multistep methods becomes hopelessly complicated because of the occurrence of the same derivative terms in several steps in sequence.

Even though these stability results are derived for one-leg methods, they can be regarded as having a relevance to linear multistep method, because of a transformation that links them.

In later papers by Dahlquist and others (Dahlquist, 1983; Wantanabe and Sheikh, 1984; Hundsdorfer and Steininger, 1991), the feasibility of using oneleg methods directly, as a practical numerical algorithm, came into serious consideration. In this brief introduction to these methods, we also discuss an interpretation in terms of effective order, and review the main results on G-stability.

# 451 The concept of $G$ -stability

We recall the non-linear stability property introduced in Subsection 357. The corresponding property for one-leg methods was introduced in Dahlquist (1976) and given the name G-stability. For convenience, we consider applications only to autonomous problems

$$
y ^ { \prime } ( x ) = f ( y ( x ) ) ,
$$

and we assume that the dissipativity property holds in the sense that solution values lie in an $N$ -dimensional inner-product space, and that

$$
\langle f ( u ) - f ( v ) , u - v \rangle \leq 0 ,
$$

for all $u , v \in \mathbb { R } ^ { N }$ .

For Runge–Kutta methods, in the study of the non-linear stability property applicable to those methods, in Subsection 357, it was possible to use the norm $\| u \| = \sqrt { \langle u , u \rangle }$ to measure the drift between two approximately equal numerical approximations that takes place in step $n$ . However, for linear $k$ - step methods, each of the $k$ subvectors making up the current state vector of each approximate solution has to be taken into account. Hence, we need to construct a suitable norm on the vector space RkN .

For $U \in \mathbb { R } ^ { k N }$ , write $U _ { i }$ , $i = 1 , 2 , \ldots , k$ , for subvectors in $\mathbb { R } ^ { N }$ . That is,

$$
\begin{array} { r } { \boldsymbol { U } = \left[ \begin{array} { c } { \boldsymbol { U } _ { 1 } } \\ { \boldsymbol { U } _ { 2 } } \\ { \vdots } \\ { \boldsymbol { U } _ { k } } \end{array} \right] . } \end{array}
$$

If $U , V \in \mathbb { R } ^ { k N }$ then, given a positive definite symmetric $k \times k$ matrix $G$ , we can define an inner product $\langle \cdot \rangle _ { G }$ by

$$
\langle U , V \rangle _ { G } = \sum _ { i , j = 1 } ^ { k } g _ { i j } \langle U _ { i } , V _ { j } \rangle ,
$$

with corresponding norm

$$
\| U \| _ { G } = \sqrt { \sum _ { i , j = 1 } ^ { k } g _ { i j } \langle U _ { i } , U _ { j } \rangle } .
$$

The aim of G-stability is to discover, for a given one-leg method, if $G$ exists so that, for a problem satisfying (451b),

$$
\left\| Y ^ { ( n ) } - Z ^ { ( n ) } \right\| _ { G } ^ { 2 } - \left\| Y ^ { ( n - 1 ) } - Z ^ { ( n - 1 ) } \right\| _ { G } ^ { 2 }
$$

cannot be positive, where

$$
Y ^ { ( n ) } = \left[ \begin{array} { c } { { y _ { n } } } \\ { { y _ { n - 1 } } } \\ { { y _ { n - 2 } } } \\ { { \vdots } } \\ { { y _ { n - k + 1 } } } \end{array} \right] , \qquad Z ^ { ( n ) } = \left[ \begin{array} { c } { { z _ { n } } } \\ { { z _ { n - 1 } } } \\ { { z _ { n - 2 } } } \\ { { \vdots } } \\ { { z _ { n - k + 1 } } } \end{array} \right] ,
$$

and the $y$ and $z$ sequences are numerical approximations corresponding to two different solutions to (451a).

The only inequality at our disposal that could be used to ensure that (451c) is not positive is the dissipativity requirement applied to the only evaluations of $f$ that take place in the step. That is, we can use the fact that

$$
\bigg \langle f \bigg ( \sum _ { i = 0 } ^ { k } \widehat { \beta } _ { i } y _ { n - i } \bigg ) - f \bigg ( \sum _ { i = 0 } ^ { k } \widehat { \beta } _ { i } z _ { n - i } \bigg ) , \sum _ { i = 0 } ^ { k } \widehat { \beta } _ { i } ( y _ { n - i } - z _ { n - i } ) \bigg \rangle \leq 0 .
$$

Because

$$
y _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } y _ { n - i } = { \left( \sum _ { i = 0 } ^ { k } \beta _ { i } \right) } ^ { - 1 } f \bigg ( \sum _ { i = 0 } ^ { k } \widehat { \beta } _ { i } y _ { n - i } \bigg ) ,
$$

with a similar formula for the $z$ sequence, it follows that

$$
\left. y _ { n } - z _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } ( y _ { n - i } - z _ { n - i } ) , \sum _ { i = 0 } ^ { k } \beta _ { i } ( y _ { n - i } - z _ { n - i } ) \right. \leq 0 ,
$$

and this will imply that (451c) has the correct sign if $G$ can be selected so that the $( k + 1 ) \times ( k + 1 )$ matrix $M$ is positive semi-definite, where

$$
\boldsymbol { M } = \alpha \beta ^ { \intercal } + \beta \alpha ^ { \intercal } - \left[ \begin{array} { c c } { G } & { 0 } \\ { 0 } & { 0 } \end{array} \right] + \left[ \begin{array} { c c } { 0 } & { 0 } \\ { 0 } & { G } \end{array} \right] ,
$$

where, in this context, $\alpha$ and $\beta$ are the vectors

$$
\alpha = \left[ \begin{array} { c } { 1 } \\ { - \alpha _ { 1 } } \\ { - \alpha _ { 2 } } \\ { \vdots } \\ { - \alpha _ { k } } \end{array} \right] , \qquad \beta = \left[ \begin{array} { c } { \beta _ { 0 } } \\ { \beta _ { 1 } } \\ { \beta _ { 2 } } \\ { \vdots } \\ { \beta _ { k } } \end{array} \right] .
$$

Let $m _ { i j }$ , $i , j ~ = ~ 0 , 1 , 2 , \ldots , k$ , denote the elements of $M$ . For any vector $U \in \mathbb { R } ^ { ( k + 1 ) N }$ , the fact that $M$ is positive semi-definite implies that

$$
\sum _ { i , j = 0 } ^ { k } m _ { i j } \langle U _ { i } , U _ { j } \rangle \geq 0 .
$$

Choose the vector

$$
U = \left[ \begin{array} { c } { y _ { n } - z _ { n } } \\ { y _ { n - 1 } - z _ { n - 1 } } \\ { y _ { n - 2 } - z _ { n - 2 } } \\ { \vdots } \\ { y _ { n - k + 1 } - z _ { n - k + 1 } } \\ { y _ { n - k } - z _ { n - k } } \end{array} \right] ,
$$

and we have the identity

$$
\begin{array} { r l } {  { \sum _ { i , j = 0 } ^ { k } m _ { i j } \langle y _ { n - i } - z _ { n - i } , y _ { n - j } - z _ { n - j } \rangle } \quad } & { } \\ & { = 2 \Big \langle y _ { n } - z _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } \big ( y _ { n - i } - z _ { n - i } \big ) , \displaystyle \sum _ { i = 0 } ^ { k } \beta _ { i } \big ( y _ { n - i } - z _ { n - i } \big ) \Big \rangle } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad + \big \| Y ^ { ( n - 1 ) } - Z ^ { ( n - 1 ) } \big \| _ { G } ^ { 2 } - \big \| Y ^ { ( n ) } - Z ^ { ( n ) } \big \| _ { G } ^ { 2 } . } \end{array}
$$

If the left-hand side is non-negative, and the first term on the right is nonpositive, it follows that

$$
\| Y ^ { ( n ) } - Z ^ { ( n ) } \| _ { G } \leq \| Y ^ { ( n - 1 ) } - Z ^ { ( n - 1 ) } \| _ { G } .
$$

The positive semi-definiteness of $M$ was recognized by Dahlquist (1976) as just the right condition to identify methods that behave stably for the type of non-linear problem we are considering. Accordingly we state the following definition:

Definition 451A A one-leg method $\lfloor \alpha , \beta \rfloor$ is ‘ $G$ -stable’ if M given by (451e) is positive semi-definite.

We present the example of the BDF2 method with

$$
[ \alpha ( z ) , \beta ( z ) ] = \Big ( 1 - \frac { 4 } { 3 } z + \frac { 1 } { 3 } z ^ { 2 } , \frac { 2 } { 3 } \Big ) .
$$

Write

$$
G = { \left[ \begin{array} { l l } { g _ { 1 1 } } & { g _ { 1 2 } } \\ { g _ { 1 2 } } & { g _ { 2 2 } } \end{array} \right] }
$$

and we find

$$
M = \left[ \begin{array} { c c c } { { \frac 4 3 - g _ { 1 1 } } } & { { - \frac 8 9 - g _ { 1 2 } } } & { { \frac 2 9 } } \\ { { - \frac 8 9 - g _ { 1 2 } } } & { { g _ { 1 1 } - g _ { 2 2 } } } & { { g _ { 1 2 } } } \\ { { \frac 2 9 } } & { { g _ { 1 2 } } } & { { g _ { 2 2 } } } \end{array} \right] ,
$$

which is positive semi-definite if and only if $G$ is the positive definite matrix

$$
G = \left[ \begin{array} { r r } { { \frac { 1 0 } { 9 } } } & { { - \frac { 4 } { 9 } } } \\ { { - \frac { 4 } { 9 } } } & { { \frac { 2 } { 9 } } } \end{array} \right] .
$$

452 Transformations relating one-leg and linear multistep methods

Denote the point at which the derivative is calculated in step $n$ of a one-leg method by ${ \hat { y } } _ { n }$ . Also denote the corresponding $x$ argument as ${ \widehat { x } } _ { n }$ . Hence, we have

$$
\begin{array} { l } { \displaystyle \widehat { x } _ { n } = x _ { n } - \frac { \sum _ { i = 0 } ^ { k } i \beta _ { i } } { \sum _ { i = 0 } ^ { k } \beta _ { i } } h , } \\ { \displaystyle \widehat { y } _ { n } = \left( \sum _ { i = 0 } ^ { k } \beta _ { i } \right) ^ { - 1 } \sum _ { i = 0 } ^ { k } \beta _ { i } y _ { n - i } , } \\ { \displaystyle y _ { n } = \sum _ { i = 1 } ^ { k } \alpha _ { n - i } y _ { n - i } + \left( \sum _ { i = 0 } ^ { k } \beta _ { i } \right) f ( \widehat { x } _ { n } , \widehat { y } _ { n } ) . } \end{array}
$$

Form a linear combination of ${ \widehat { y } } _ { n - i }$ , $i = 0 , 1 , \ldots , k$ , given by (452b), based on the coefficients in the $\alpha$ polynomial, and note that the operators $\alpha ( E ^ { - 1 } )$ and $\beta ( E ^ { - 1 } )$ are commutative. We have

$$
{ \widehat { y } } _ { n } - \sum _ { i = 1 } ^ { k } \alpha _ { i } { \widehat { y } } _ { n - i } = h \sum _ { i = 1 } ^ { k } \beta _ { i } f ( { \widehat { x } } _ { n } , { \widehat { y } } _ { n } ) .
$$

The relationship between the $y$ and $\hat { y }$ sequences given by (452b) and (452d) was suggested by Dahlquist (1976) as an indication that stability questions for a linear multistep method can be replaced by similar questions for the corresponding one-leg method.

# 453 Effective order interpretation

The concept of effective order, introduced in Subsections 365 and 389, gives an alternative interpretation of the relationship between the computed approximation and the exact solution.

Define the function $\gamma ( z )$ by

$$
\gamma ( z ) = \bigg ( \sum _ { i = 0 } ^ { k } \widehat { \beta } _ { i } \exp ( - i z ) \bigg ) ^ { - 1 } = \gamma _ { 0 } + \gamma _ { 1 } z + \gamma _ { 2 } z ^ { 2 } + \cdots ,
$$

where $\gamma _ { 0 } = 1$ , and the starting approximation by

$$
S ( y ) ( x ) = \sum _ { i = 0 } ^ { p } \gamma _ { i } h ^ { i } y ^ { ( i ) } ( x ) ,
$$

assuming the linear multistep method $\lfloor \alpha , \beta \rfloor$ has order $p$ . Write ${ \widehat { y } } ( x ) = S ( y ) ( x )$ . We then have

$$
\widehat { y } ( x _ { n } ) - \sum _ { i = 1 } ^ { k } \alpha _ { i } \widehat { y } ( x _ { n - i } ) = h \sum _ { i = 1 } ^ { k } \beta _ { i } f \biggr ( x _ { n } , \sum _ { i = 0 } ^ { k } \widehat { \beta } _ { i } \widehat { y } ( x _ { n - i } ) \biggr ) + O ( h ^ { p + 1 } ) .
$$

# 454 Concluding remarks on $G$ -stability

It might be suspected that amongst A-stable linear multistep methods, Gstable methods stand out as being in some way superior. Such considerations turn out to be vacuous because a linear multistep method is A-stable if and only if it is G-stable. That G-stable methods are A-stable is shown simply as in Theorem 454A below. However, the converse result is much deeper. This was proved in Dahlquist (1978). Now the easy result:

Theorem 454A A $G$ -stable linear multistep method is $A$ -stable.

Proof. We use the criterion that if $| w | < 1$ , then $z = \alpha ( w ) / \beta ( w )$ is in the right half-plane. Form the inner product $W ^ { * } M W$ , where $M$ is the matrix given by (451e) and

$$
\begin{array} { r } { W = \left[ \begin{array} { c } { 1 } \\ { w } \\ { w ^ { 2 } } \\ { \vdots } \\ { w ^ { k } } \end{array} \right] . } \end{array}
$$

We find that

$$
\alpha ( \overline { { { w } } } ) \beta ( w ) + \alpha ( w ) \beta ( \overline { { { w } } } ) = W ^ { \ast } M W + ( 1 - | w | ^ { 2 } ) \sum _ { j , l = 1 } ^ { k } g _ { j l } \overline { { { w } } } ^ { j - 1 } w ^ { l - 1 } > 0 ,
$$

so that $\mathrm { R e } \big ( \alpha ( w ) / \beta ( w ) \big ) > 0$ .

# Exercises 45

45.1 Show that the method defined by $\begin{array} { r } { \alpha ( z ) = 1 - \frac { 3 } { 2 } z + \frac { 1 } { 2 } z ^ { 2 } } \end{array}$ , $\begin{array} { r } { \beta ( z ) = \frac { 3 } { 4 } - \frac { 1 } { 4 } z } \end{array}$ , is G-stable, by finding the corresponding matrix $G$ .

45.2 Show that if $q _ { 1 } + i q _ { 2 }$ is in the left half-plane, then the differential equation

$$
y ^ { \prime } ( x ) = q y ( x )
$$

can be written as a system

$$
\left[ \begin{array} { c } { y _ { 1 } ^ { \prime } ( x ) } \\ { y _ { 2 } ^ { \prime } ( x ) } \end{array} \right] = \left[ \begin{array} { c c } { q _ { 1 } } & { - q _ { 2 } } \\ { q _ { 2 } } & { q _ { 1 } } \end{array} \right] \left[ \begin{array} { c } { y _ { 1 } ( x ) } \\ { y _ { 2 } ( x ) } \end{array} \right] ,
$$

where $y ( x ) = y _ { 1 } ( x ) + i y _ { 2 } ( x ) .$ . Furthermore, show that this system satisfies (451b), using the usual inner product.

# 46 Implementation Issues

# 460 Survey of implementation considerations

In addition to the basic algorithm giving the value of $y _ { n }$ in terms of $y _ { n - 1 }$ , $y _ { n - 2 }$ , . . . , $y _ { n - k }$ , effective use of linear multistep methods requires further tools. We have already discussed, albeit briefly, the starting process for a method with fixed order and fixed stepsize. However, linear multistep methods are seldom used in such a manner. It is usually efficient to adapt both the stepsize and the order to suit local behaviour of the computed solution, and this leads to the need for representations of the methods that will make adaptivity possible. Given that a variable order implementation is going to be used, it is easier to start at order 1 and build the order upwards as the solution develops. Reducing order is relatively easy and also needs to be built in as an option within a variable order formulation.

It is natural to make a comparison between implementation techniques for Runge–Kutta methods and for linear multistep methods. Unlike for explicit Runge–Kutta methods, interpolation and error estimation are regarded as straightforward for linear multistep methods. Not only is it possible to obtain an asymptotically correct estimate of the local truncation error, but it is a simple extension of the approximation technique to obtain a usable approximation for the local error that might have been expected if the next higher order had instead been used.

# 461 Representation of data

After a number of steps, with constant size $h$ , have been carried out using an order $p$ method, for example by a PECE combination of Adams–Bashforth and Adams–Moulton methods, approximations are available to $y ( x _ { n } ) , h y ^ { \prime } ( x _ { n } )$ , $h y ^ { \prime } ( x _ { n - 1 } )$ , $\cdot \cdot \cdot$ , $h y ^ { \prime } ( x _ { n - p + 1 } )$ . If the stepsize is to be altered by a factor $r$ to a new value $r h$ , then there seem to be two distinct approaches to proceeding further.

The first approach is to use a modified form of the Adams formulae which enables $y ( x _ { n } + r h )$ to be written in terms of $y ( x _ { n } )$ , $h y ^ { \prime } ( x _ { n } )$ , $h y ^ { \prime } ( x _ { n - 1 } )$ , . . . , $h y ^ { \prime } ( x _ { n - p + 1 } )$ . Of course this only works for a single step. For the step after that, the data on which to base the approximation would be $y ( x _ { n } + h r )$ , $h y ^ { \prime } ( x _ { n } + h r )$ , $h y ^ { \prime } ( x _ { n } )$ , . . . , $h y ^ { \prime } ( x _ { n - p + 2 } )$ and the results computed would be approximations to $y ( x _ { n } + h r + h r \hat { r } )$ , where $\widehat { r }$ is the stepsize ratio for this new step. Rather than explore the form of the modified Adams formula in this rather ad hoc manner, write the exact quantities that the incoming data is supposed to approximate as the sequence consisting of

$$
y ( x _ { n } - h \theta _ { 1 } ) , \quad h y ^ { \prime } ( x _ { n } - h \theta _ { 1 } ) , \quad h y ^ { \prime } ( x _ { n } - h \theta _ { 2 } ) , \quad \ldots , \quad h y ^ { \prime } ( x _ { n } - h \theta _ { k } ) .
$$

The Adams–Bashforth method would then generalize to an approximation of the form

$$
y ( x _ { n } ) \approx y ( x _ { n } - h \theta _ { 1 } ) + \sum _ { i = 1 } ^ { k } \beta _ { i } ^ { * } h y ^ { \prime } ( x _ { n } - h \theta _ { i } ) ,
$$

and the Adams–Moulton to an approximation of the form

$$
y ( x _ { n } ) \approx \beta _ { 0 } h y ^ { \prime } ( x _ { n } ) + y ( x _ { n } - h \theta _ { 1 } ) + \sum _ { i = 1 } ^ { k } \beta _ { i } h y ^ { \prime } ( x _ { n } - h \theta _ { i } ) .
$$

To obtain order $p = k$ for (461a), the coefficients $\beta _ { i } ^ { * }$ , $i = 1 , 2 , \ldots , k$ , have to be chosen so that

$$
1 = \exp ( - \theta _ { 1 } z ) + z \sum _ { i = 1 } ^ { k } \beta _ { i } ^ { * } \exp ( - \theta _ { i } z ) + { \cal O } ( z ^ { p + 1 } ) ,
$$

and to obtain order $p = k + 1$ for (461b), $\beta _ { i }$ , $i = 1 , 2 , \ldots , k$ , are chosen so that

$$
1 = \exp ( - \theta _ { 1 } z ) + z \beta _ { 0 } + z \sum _ { i = 1 } ^ { k } \beta _ { i } \exp ( - \theta _ { i } z ) + O ( z ^ { p + 1 } ) .
$$

To use this approach in practice, the coefficients $\beta _ { 1 } ^ { * }$ , $\beta _ { 2 } ^ { * }$ , $\cdot \cdot \cdot$ and $\beta _ { 0 }$ , $\beta _ { 1 }$ , . . . have to be evaluated afresh every step, before any differential equation solutions are approximated. For many problems this is justified, and many codes use some sort of approach based on this technique.

The second main approach to stepsize adjustment was proposed by Nordsieck (1962) and further developed by Gear (1967, 1971). For a Nordsieck method of order $p$ , the data imported into step $n$ consists of approximations to

$$
y ( x _ { n - 1 } ) , \quad h y ^ { \prime } ( x _ { n - 1 } ) , \quad { \frac { 1 } { 2 ! } } h ^ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) , \quad { \frac { 1 } { p ! } } h ^ { p } y ^ { ( p ) } ( x _ { n - 1 } ) ,
$$

and the quantities exported from this step are approximations to

$$
y ( x _ { n } ) , \quad h y ^ { \prime } ( x _ { n } ) , \quad \frac { 1 } { 2 ! } h ^ { 2 } y ^ { \prime \prime } ( x _ { n } ) , \quad \frac { 1 } { p ! } h ^ { p } y ^ { ( p ) } ( x _ { n } ) .
$$

Note that the factors $( i ! ) ^ { - 1 }$ are inserted for convenience. When a stepsize change from $h$ to $r h$ is required, the simple adjustment of scaling the quantities in (461c) by powers of the scale factor $r$ is used. This means that they become approximations to

$$
y ( x _ { n } ) , \quad r h y ^ { \prime } ( x _ { n } ) , \quad \frac { 1 } { 2 ! } ( r h ) ^ { 2 } y ^ { \prime \prime } ( x _ { n } ) , \quad \frac { 1 } { p ! } ( r h ) ^ { p } y ^ { ( p ) } ( x _ { n } ) .
$$

Denote the vector of Nordsieck approximations imported into step $n$ by

$$
\begin{array} { l } { \eta _ { 0 } ^ { [ n - 1 ] } \approx y ( x _ { n - 1 } ) , } \\ { \eta _ { 1 } ^ { [ n - 1 ] } \approx h y ^ { \prime } ( x _ { n - 1 } ) , } \\ { \eta _ { 2 } ^ { [ n - 1 ] } \approx \displaystyle \frac { 1 } { 2 ! } h ^ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) , } \\ { \quad \quad \vdots \quad \quad \vdots } \end{array}
$$

$$
\eta _ { p } ^ { [ n - 1 ] } \approx \frac { 1 } { p ! } h ^ { p } y ^ { ( p ) } ( x _ { n - 1 } ) ,
$$

Coefficients, $\gamma _ { 0 }$ $_ { 0 } , \gamma _ { 1 } , \ldots$ , $\gamma _ { p }$ , for Nordsieck methods   

<table><tr><td></td><td></td><td>p=2 p=3 p=4 p=5 p=6</td><td></td><td></td><td></td><td>p=7</td><td>p=8</td></tr><tr><td>70</td><td></td><td></td><td>3</td><td>251</td><td>95</td><td>19087</td><td>5257</td></tr><tr><td></td><td>1</td><td>1</td><td>1</td><td>720 1</td><td>288 1</td><td>60480 1</td><td>17280 1</td></tr><tr><td>71</td><td>1</td><td></td><td>11</td><td></td><td>137</td><td>49</td><td>363</td></tr><tr><td>22</td><td></td><td>A</td><td>前</td><td>中</td><td>120</td><td>40 203</td><td>280 469</td></tr><tr><td>73</td><td></td><td></td><td></td><td></td><td></td><td>270 49</td><td>540 967</td></tr><tr><td>4</td><td></td><td></td><td></td><td></td><td></td><td>192 7</td><td>2880 7</td></tr><tr><td>5</td><td></td><td></td><td></td><td>120</td><td>新</td><td>144 7</td><td>9 23</td></tr><tr><td>76</td><td></td><td></td><td></td><td></td><td></td><td>1440 1</td><td>2160 1</td></tr><tr><td>77 78</td><td></td><td></td><td></td><td></td><td></td><td>5040</td><td>1260 1 40320</td></tr></table>

so that the result computed by the Adams–Bashforth predictor will be

$$
y _ { n } ^ { * } = \eta _ { 0 } ^ { [ n - 1 ] } + \eta _ { 1 } ^ { [ n - 1 ] } + \cdots + \eta _ { p } ^ { [ n - 1 ] } .
$$

If an approximation is also required for the scaled derivative at $x _ { n }$ , this can be found from the formula, also based on a Taylor expansion,

$$
h y ^ { \prime } ( x _ { n } ) \approx \eta _ { 1 } ^ { [ n - 1 ] } + 2 \eta _ { 2 } ^ { [ n - 1 ] } + \cdot \cdot \cdot + p \eta _ { p } ^ { [ n - 1 ] } .
$$

To find the Nordsieck equivalent to the Adams–Moulton corrector formula, it is necessary to add $\beta _ { 0 }$ multiplied by the difference between the corrected value of the scaled derivative and the extrapolated value computed by (461d). That is, the corrected value of $\eta _ { 0 } ^ { \lfloor n \rfloor }$ becomes

$$
\eta _ { 0 } ^ { [ n ] } = \beta _ { 0 } \Delta _ { n } + \eta _ { 0 } ^ { [ n - 1 ] } + \eta _ { 1 } ^ { [ n - 1 ] } + \cdot \cdot \cdot + \eta _ { p } ^ { [ n - 1 ] } ,
$$

where

$$
\Delta _ { n } = h f ( x _ { n } , y _ { n } ^ { * } ) - \sum _ { i = 1 } ^ { s } i \eta _ { i } ^ { [ n - 1 ] } .
$$

In this formulation we have assumed a PECE mode but, if further iterations are carried out, the only essential change will be that the second argument of $h f ( x _ { n } , y _ { n } ^ { * } )$ will be modified.

For constant stepsize, the method should be equivalent to the Adams predictor–corrector pair and this means that all the output values will be modified in one way or another from the result that would have been formed by simple extrapolation from the incoming Nordsieck components. Thus we can write the result computed in a step as

$$
\left[ \begin{array} { c } { \boldsymbol { \eta } _ { 0 } ^ { [ n ] } } \\ { \boldsymbol { \eta } _ { 1 } ^ { [ n ] } } \\ { \boldsymbol { \eta } _ { 2 } ^ { [ n ] } } \\ { \vdots } \\ { \boldsymbol { \eta } _ { p - 1 } ^ { [ n ] } } \\ { \boldsymbol { \eta } _ { p } ^ { [ n ] } } \end{array} \right] = \left[ \begin{array} { c } { \gamma _ { 0 } } \\ { \gamma _ { 1 } } \\ { \gamma _ { 2 } } \\ { \vdots } \\ { \gamma _ { p - 1 } } \\ { \gamma _ { p } } \end{array} \right] \boldsymbol { \Delta } _ { n } + \left[ \begin{array} { c c c c c c } { 1 } & { 1 } & { 1 } & { \cdots } & { 1 } & { 1 } \\ { 0 } & { 1 } & { 2 } & { \cdots } & { p - 1 } & { p } \\ { 0 } & { 0 } & { 1 } & { \cdots } & { \binom { p - 1 } { 2 } } & { \binom { p } { 2 } } \\ { \vdots } & { \vdots } & { \vdots } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { p } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } \end{array} \right] \left[ \begin{array} { c } { \boldsymbol { \eta } _ { 0 } ^ { [ n - 1 ] } } \\ { \boldsymbol { \eta } _ { 1 } ^ { [ n - 1 ] } } \\ { \boldsymbol { \eta } _ { 2 } ^ { [ n - 1 ] } } \\ { \vdots } \\ { \boldsymbol { \eta } _ { p - 1 } ^ { [ n - 1 ] } } \\ { \boldsymbol { \eta } _ { p } ^ { [ n - 1 ] } } \end{array} \right] .
$$

The quantities $\gamma _ { i }$ , $i = 0 , 1 , 2 , \dotsc , p$ , have values determined by the equivalence with the standard fixed stepsize method and we know at least that

$$
\gamma _ { 0 } = \beta _ { 0 } , \qquad \gamma _ { 1 } = 1 .
$$

The value selected for $\gamma _ { 1 }$ ensures that $\eta _ { 1 } ^ { \lfloor n \rfloor }$ is precisely the result evaluated from η[ ]0 using the differential equation. We can arrive at the correct values of $\gamma _ { 2 }$ , . . . , $\gamma _ { p }$ , by the requirement that the matrix

$$
\left[ \begin{array} { c c c c c } { 1 } & { 3 } & { \cdots } & { \binom { p - 1 } { 2 } } & { \binom { p } { 2 } } \\ { 0 } & { 1 } & { \cdots } & { \binom { p - 1 } { 3 } } & { \binom { p } { 3 } } \\ { \vdots } & & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { \cdots } & { 1 } & { p } \\ { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } \end{array} \right] - \left[ \begin{array} { c } { \gamma _ { 2 } } \\ { \gamma _ { 3 } } \\ { \vdots } \\ { \gamma _ { p - 1 } } \\ { \gamma _ { p } } \end{array} \right] [ 2 \quad 3 \quad \cdots \quad p - 1 \quad p ]
$$

has zero spectral radius.

Values of the coefficients $\gamma _ { i }$ , $i = 0 , 1 , \dotsc , p$ , are given in Table $4 6 1 ( \mathrm { I } )$ for $p = 2 , 3 , \ldots , 8$ .

Adjustment of stepsize is carried out by multiplying the vector of output approximations formed in (461e) at the completion of step $n$ , by the diagonal matrix $D ( r )$ before the results are accepted as input to step $n + 1$ , where

$$
D ( r ) = \operatorname { d i a g } ( 1 , r , r ^ { 2 } , . . . , r ^ { p } ) .
$$

It was discovered experimentally by Gear that numerical instabilities can result from using this formulation. This can be seen in the example $p = 3$ , where we find the values $\begin{array} { r } { \gamma _ { 2 } = \frac { 3 } { 4 } } \end{array}$ , $\textstyle \gamma _ { 3 } = { \frac { 1 } { 6 } }$ Stability is determined by products of matrices of the form

$$
\left[ \begin{array} { l l } { - { \frac { 1 } { 2 } } r ^ { 2 } } & { { \frac { 3 } { 4 } } r ^ { 2 } } \\ { - { \frac { 1 } { 3 } } r ^ { 3 } } & { { \frac { 1 } { 2 } } r ^ { 3 } } \end{array} \right] ,
$$

and for $r \geq 1 . 6 9 5 6 2$ , this matrix is no longer power-bounded.

Gear’s pragmatic solution was to prohibit changes for several further steps after a stepsize change had occurred. An alternative to this remedy will be considered in the next subsection.

# 462 Variable stepsize for Nordsieck methods

The motivation we have presented for the choice of $\gamma _ { 1 }$ , $\gamma _ { 2 }$ , . . . in the formulation of Nordsieck methods was to require a certain matrix to have zero spectral radius. Denote the vector $\gamma$ and the matrix $V$ by

$$
\gamma = \left[ \begin{array} { c } { \gamma _ { 1 } } \\ { \gamma _ { 2 } } \\ { \vdots } \\ { \gamma _ { p } } \end{array} \right] , \quad \quad V = \left[ \begin{array} { c c c c c } { 1 } & { 2 } & { 3 } & { \cdots } & { p } \\ { 0 } & { 1 } & { 3 } & { \cdots } & { \frac { 1 } { 2 } p ( p - 1 ) } \\ { 0 } & { 0 } & { 1 } & { \cdots } & { \frac { 1 } { 6 } p ( p - 1 ) ( p - 2 ) } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } \end{array} \right] ,
$$

and denote by $e _ { 1 } ^ { \mathsf { T } }$ the basis row vector $e _ { 1 } ^ { \mathsf { T } } = [ 1 \quad 0 \quad \cdot \cdot \quad 0 ]$ . The characteristic property of $\gamma$ is that the matrix

$$
( I - \gamma e _ { 1 } ^ { \mathsf { T } } ) V
$$

has zero spectral radius. When variable stepsize is introduced, the matrix in (462a) is multiplied by $D ( r ) = \mathrm { d i a g } ( r , r ^ { 2 } , r ^ { 3 } , \ldots , r ^ { p } )$ and, as we have seen, if $\gamma$ is chosen on the basis of constant $h$ , there is a deterioration in stable behaviour. We consider the alternative of choosing $\gamma$ as a function of $r$ so that

$$
\rho ( D ( r ) ( I - \gamma e _ { 1 } ^ { \mathsf { T } } ) V ) = 0 .
$$

The value of $\gamma _ { 1 }$ still retains the value 1 but, in the only example we consider, $p = 3$ , it is found that

$$
\gamma _ { 2 } = \frac { 1 + 2 r } { 2 ( 1 + r ) } , \qquad \gamma _ { 3 } = \frac { r } { 3 ( 1 + r ) } ,
$$

and we have

$$
D ( r ) ( I - \gamma e _ { 1 } ^ { \intercal } ) V = \left[ \begin{array} { c c c } { 0 } & { 0 } & { 0 } \\ { 0 } & { - \frac { r ^ { 3 } } { 1 + r } } & { \frac { 3 r ^ { 2 } } { 2 ( 1 + r ) } } \\ { 0 } & { - \frac { 2 r ^ { 4 } } { 3 ( 1 + r ) } } & { \frac { r ^ { 3 } } { 2 ( 1 + r ) } } \end{array} \right] .
$$

It is obvious that this matrix is power-bounded for all positive values of $r$ . However, if a sequence of $n$ steps is carried out with stepsize changes $r _ { 1 }$ , $r _ { 2 }$ , . . . , $r _ { n }$ then the product of matrices of the form given by (462b) for these values of $r$ to be analysed to determine stability. The spectral radius of such a product is found to be

$$
\frac { | r _ { 1 } - r _ { n } | r _ { 1 } ^ { 2 } } { 1 + r _ { 1 } } \cdot \frac { | r _ { 2 } - r _ { 1 } | r _ { 2 } ^ { 2 } } { 1 + r _ { 2 } } \cdot \frac { | r _ { 3 } - r _ { 2 } | r _ { 3 } ^ { 2 } } { 1 + r _ { 3 } } \cdot \cdot \cdot \frac { | r _ { n } - r _ { n - 1 } | r _ { n } ^ { 2 } } { 1 + r _ { n } } ,
$$

and this will be bounded by 1 as long as $r _ { i } \in [ 0 , r ^ { \star } ]$ , where $r ^ { \star }$ has the property that

$$
\frac { r _ { 1 } r _ { 2 } | r _ { 2 } - r _ { 1 } | } { \sqrt { ( 1 + r _ { 1 } ) ( 1 + r _ { 2 } ) } } \leq 1 , \quad \mathrm { w h e n e v e r ~ } r _ { 1 } , r _ { 2 } \in [ 0 , r ^ { \star } ] .
$$

It is found after some calculations that stability, in the sense of this discussion, is achieved if $r ^ { \star } \approx 2 . 1 5 9 5 4 5 4 3$ .

# 463 Local error estimation

The standard estimator for local truncation error is based on the Milne device. That is, the difference between the predicted and corrected values provides an approximation to some constant multiplied by $h ^ { p + 1 } y ^ { ( p + 1 ) } ( x _ { n } )$ , and the local truncation error can be estimated by multiplying this by a suitable scale factor.

This procedure has to be interpreted in a different way if, as in some modern codes, the predictor and corrector are accurate to different orders. We no longer have an asymptotically correct approximation to the local truncation error but to the error in the predictor, assuming this has the lower order. Nevertheless, stepsize control based on this approach often gives reliable and useful performance.

To allow for a possible increase in order, estimation is also needed for the scaled derivative one order higher than the standard error estimator. It is very difficult to do this reliably, because any approximation will be based on a linear combination of $h y ^ { \prime } ( x )$ for different $x$ arguments. These quantities in turn will be of the form $h f ( x , y ( x ) + C h ^ { p + 1 } + O ( h ^ { p + 2 } ) )$ , and the terms of the form $C h ^ { p + 1 } + O ( h ^ { p + 2 } )$ will distort the result obtained. However, it is possible to estimate the scaled order $p { + 2 }$ derivative reliably, at least if the stepsize has been constant over recent steps, by forming the difference of approximations to the order $p { + 1 }$ derivative over two successive steps. If the stepsize has varied moderately, the approximation this approximation will still be reasonable. In any case, if the criterion for increasing order turns out to be too optimistic for any specific problem, then after the first step with the new order a rejection is likely to occur, and the order will either be reduced again or else the stepsize will be lowered while still maintaining the higher order.

# Exercises 46

46.1 Show how to write $y ( x _ { n } + r h )$ in terms of $y ( x _ { n } )$ , $h y ^ { \prime } ( x _ { n } )$ and $h y ^ { \prime } ( x _ { n } - h )$ , to within $O ( h ^ { 3 } )$ . Show this approximation might be used to generalize the order 2 Adams–Bashforth method to variable stepsize.

46.2 How should the formulation of Subsection 461 be modified to represent Adams–Bashforth methods?
