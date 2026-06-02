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
