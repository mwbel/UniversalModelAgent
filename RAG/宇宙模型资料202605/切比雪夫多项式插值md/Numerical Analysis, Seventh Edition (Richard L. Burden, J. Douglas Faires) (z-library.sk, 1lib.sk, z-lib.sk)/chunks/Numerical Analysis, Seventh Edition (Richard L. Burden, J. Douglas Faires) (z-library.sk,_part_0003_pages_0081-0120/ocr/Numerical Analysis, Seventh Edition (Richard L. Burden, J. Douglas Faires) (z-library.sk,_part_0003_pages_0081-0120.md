Use the Secant method to find a solution to $x = \cos x $ . In Example 1 we compared functional iteration and Newton's method with the initial approximation $p _ { 0 } = \pi / 4$ . Here we need two initial approximations. Table 2.5 lists the calculations with $p _ { 0 } = 0 . 5$ ， $p _ { 1 } = \pi / 4$ ， and the formula

$$
p _ { n } = p _ { n - 1 } - { \frac { ( p _ { n - 1 } - p _ { n - 2 } ) ( \cos p _ { n - 1 } - p _ { n - 1 } ) } { ( \cos p _ { n - 1 } - p _ { n - 1 } ) - ( \cos p _ { n - 2 } - p _ { n - 2 } ) } } , \quad { \mathrm { f o r ~ } } n \geq 2 ,
$$

from Algorithm 2.4.

Table 2.5   

<table><tr><td></td></tr><tr><td>Pn</td></tr><tr><td>n</td></tr><tr><td>0 0.5</td></tr><tr><td></td></tr><tr><td>1 0.7853981635</td></tr><tr><td>2 0.7363841388</td></tr><tr><td>3 0.7390581392</td></tr><tr><td>4 0.7390851493</td></tr><tr><td>5 0.7390851332</td></tr></table>

By comparing the results here with those in Example 1,we see that $p _ { 5 }$ is accurate to the tenth decimal place. The convergence of the Secant method is much faster than functional iteration but slightly slower than Newton's method,which obtained this degree of accuracy with $p _ { 3 }$ . This is generally true. (See Exercise 12 of Section 2.4.)

Newton's method or the Secant method is often used to refine an answer obtained by another technique, such as the Bisection method,since these methods require a good first approximation but generally give rapid convergence.

Each successive pair of approximations in the Bisection method brackets a root $p$ of the equation; that is, for each positive integer $\pmb { n }$ , a root lies between $a _ { n }$ and $b _ { n }$ . This implies that, for each $\pmb { n }$ , the Bisection method iterations satisfy

$$
\vert p _ { n } - p \vert < { \frac { 1 } { 2 } } \vert a _ { n } - b _ { n } \vert ,
$$

which provides an easily calculated error bound for the approximations. Root bracketing is not guaranteed for either Newton's method or the Secant method. Table 2.4 contains results from Newton's method applied to $f ( x ) = \cos x - x .$ ，where an approximate root was found to be 0.7390851332. Notice that this root is not bracketed by either $p _ { 0 } , p _ { 1 }$ or $p _ { 1 }$ ， $p _ { 2 }$ . The Secant method approximations for this problem are given in Table 2.5. The initial approximations $p _ { 0 }$ and $p _ { 1 }$ bracket the root, but the pair of approximations $p _ { 3 }$ and $p _ { 4 }$ fail to do so.

The method of False Position (also called Regula Falsi ） generates approximations in the same manner as the Secant method, but it includes a test to ensure that the root is bracketed between successive iterations. Although it is not a method we generally recommend, it illustrates how bracketing can be incorporated.

First choose initial approximations $p _ { 0 }$ and $p _ { 1 }$ with $f ( p _ { 0 } ) \cdot f ( p _ { 1 } ) < 0$ . The approximation $p _ { 2 }$ is chosen in the same manner as in the Secant method,as the $x$ -intercept of the line joining $( p _ { 0 } , f ( p _ { 0 } ) )$ and $( p _ { 1 } , f ( p _ { 1 } ) )$ . To decide which secant line to use to compute $p _ { 3 }$ ,we check $f ( p _ { 2 } ) \cdot f ( p _ { 1 } )$ . If this value is negative, then $p _ { I }$ and $p _ { 2 }$ bracket a root, and we choose $p _ { 3 }$ as the $x$ -intercept of the line joining $( p _ { 1 } , f ( p _ { 1 } ) )$ and $( p _ { 2 } , f ( p _ { 2 } ) )$ . If not, we choose $p _ { 3 }$ as the $x$ -intercept of the line joining $( p _ { 0 } , f ( p _ { 0 } ) )$ and $( p _ { 2 } , f ( p _ { 2 } ) )$ , and then interchange the indices on $p _ { 0 }$ and $p _ { 1 }$ . In a similar manner, once $p _ { 3 }$ is found, the sign of $f ( p _ { 3 } ) \cdot f ( p _ { 2 } )$ determines whether we use $p _ { 2 }$ and $p _ { 3 }$ or $p _ { 3 }$ and $p _ { 1 }$ to compute $p _ { 4 }$ . In the latter case a relabeling of $p _ { 2 }$ and $p _ { 1 }$ is performed. The relabeling ensures that the root is bracketed between successive iterations. The process is described in Algorithm 2.5,and Figure 2.10 shows how the iterations can differ from those of the Secant method.In this illustration, the first three approximations are the same, but the fourth approximations differ.

![](images/219e47556881cb8597cc82724094b2a8207413b844a62fb129a92f222f7bcd89.jpg)  
Figure 2.10

# Method of False Position

To find a solution to $f ( x ) = 0$ given the continuous function $f$ on the interval $[ p _ { 0 } , p _ { 1 } ]$ where $f ( p _ { 0 } )$ and $f ( p _ { 1 } )$ have opposite signs:

INPUT initial approximations $p _ { 0 } , p _ { 1 }$ ; tolerance TOL; maximum number of iterations $N _ { 0 }$ ·

OUTPUT approximate solution $p$ or message of failure.

Step 1 Set $i = 2$ ；$\begin{array} { r } { q _ { 0 } = f ( p _ { 0 } ) ; } \\ { q _ { 1 } = f ( p _ { 1 } ) . } \end{array}$

Step 2 While $i \leq N _ { 0 }$ do Steps 3-7.

Step 4 If $| p - p _ { 1 } | < T O L$ then OUTPUT $( p )$ ； (The procedure was successful.) STOP.

Step5Se $\begin{array} { r } { \mathfrak { t } i = i + 1 ; } \\ { q = f ( p ) . } \end{array}$

Step 6 If $q \cdot q _ { 1 } < 0$ then set $p _ { 0 } = p _ { 1 }$

$$
q _ { 0 } = q _ { 1 } .
$$

$$
\begin{array} { r l } { t e p \gamma } & { { } S e t p _ { 1 } = p ; } \\ { q _ { 1 } = q . } \end{array}
$$

# Step 8OUTPUT('Method failed after $N _ { 0 }$ iterations, $N _ { 0 } = , N _ { 0 }$ ； (The procedure unsuccessful.) STOP.

# EXAMPLE 3

Table 2.6 shows the results of the method of False Position applied to $f ( x ) = \cos x - x$ with the same initial approximations we used for the Secant method in Example 2. Notice that the approximations agree through $p _ { 3 }$ and that the method of False Position requires an additional iteration to obtain the same accuracy as the Secant method.

Table 2.6   

<table><tr><td rowspan=1 colspan=1>n                      Pn</td></tr><tr><td rowspan=1 colspan=1>0           0.51           0.7853981635</td></tr><tr><td rowspan=1 colspan=1>2           0.7363841388</td></tr><tr><td rowspan=1 colspan=1>3           0.7390581392</td></tr><tr><td rowspan=1 colspan=1>4           0.7390848638</td></tr><tr><td rowspan=1 colspan=1>5           0.7390851305</td></tr><tr><td rowspan=1 colspan=1>6           0.7390851332</td></tr></table>

The added insurance of the method of False Position commonly requires more calculation than the Secant method, just as the simplification that the Secant method provides over Newton's method usually comes at the expense of additional iterations.Further examples of the positive and negative features of these methods can be seen by working Exercises 13 and 14.

# Exercise Set 2.3

1.Let $f ( x ) = x ^ { 2 } - 6$ and $p _ { 0 } = 1$ . Use Newton's method to find $p _ { 2 }$

2.Let $f ( x ) = - x ^ { 3 } - \cos x$ and $p _ { 0 } = - 1$ . Use Newton's method to find $_ { p _ { 2 } }$ . Could $p _ { 0 } = 0$ be used?

3.Let $f ( x ) = x ^ { 2 } - 6$ With $p _ { 0 } = 3$ and $p _ { 1 } = 2$ ,find $p _ { 3 }$

$\clubsuit$ Use the Secant method. ${ \bf { b } } .$ Use the method of False Position. c. Which of (a) or (b) is closer to $\sqrt { 6 } ?$

4.Let $f ( x ) = - x ^ { 3 } - \cos x$ . With $p _ { 0 } = - 1$ and $p _ { 1 } = 0$ ,find $p _ { 3 }$

a.Use the Secant method. b.Use the method of False Position.

5.Use Newton's method to find solutions accurate to within $1 0 ^ { - 4 }$ for the following problems.

$$
\begin{array} { c c } { { x ^ { 3 } - 2 x ^ { 2 } - 5 = 0 , \quad \left[ 1 , 4 \right] \qquad } } & { { { \bf b . } \quad x ^ { 3 } + 3 x ^ { 2 } - 1 = 0 , \quad \left[ - 3 , - 2 \right] } } \\ { { x - \cos x = 0 , \quad \left[ 0 , \pi / 2 \right] \qquad } } & { { { \bf d . } \quad x - 0 . 8 - 0 . 2 \sin x = 0 , \quad \left[ 0 , \pi / 2 \right] } } \end{array}
$$

6.Use Newton's method to find solutions accurate to within $1 0 ^ { - 5 }$ for the following problems a. $e ^ { x } + 2 ^ { - x } + 2 \cos x - 6 = 0 \quad { \mathrm { f o r ~ } } 1 \leq x \leq 2$ b. $\ln ( x - 1 ) + \cos ( x - 1 ) = 0$ for 1.3≤x≤2 c. $2 x \cos 2 x - ( x - 2 ) ^ { 2 } = 0 \quad { \mathrm { f o r ~ } } 2 \leq x \leq 3 { \mathrm { ~ a n d ~ } } 3 \leq x \leq 4$ d. $( x - 2 ) ^ { 2 } - \ln x = 0 \quad { \mathrm { f o r ~ } } 1 \leq x \leq 2 { \mathrm { ~ a n d ~ } } e \leq$ $e \leq x \leq 4$ e. $e ^ { x } - 3 x ^ { 2 } = 0 \quad { \mathrm { ~ f o r ~ } } 0 \leq x \leq 1 { \mathrm { ~ a n d ~ } } 3 \leq x \leq { 5 }$ f. $\sin x - e ^ { - x } = 0 \quad { \mathrm { ~ f o r ~ } } 0 \leq x \leq 1 \ 3 \leq x \leq 4$ and $6 \leq x \leq 7$

7.Repeat Exercise 5 using (i) the Secant method and (ii) the method of False Position.

8.Repeat Exercise 6 using (i) the Secant method and (ii) the method of False Position.

9. Use Newton's method to approximate,to within $1 0 ^ { - 4 }$ , the value of $x$ that produces the point on the graph of $y = x ^ { 2 }$ that is closest to (1,0).[Hint: Minimize $[ d ( x ) ] ^ { 2 }$ ，where $d ( x )$ represents the distance from $( x , x ^ { 2 } )$ to (1,0).]

10. Use Newton's method to approximate, to within $1 0 ^ { - 4 }$ , the value of $\pmb { x }$ that produces the point on the graph of $y = 1 / x$ that is closest to (2, 1).

11.The following describes Newton's method graphically: Suppose that $f ^ { \prime } ( x )$ exists on $[ a , b ]$ and that $f ^ { \prime } ( x ) \neq 0$ on $[ a , b ]$ . Further, suppose there exists one $p \in [ a , b ]$ such that $f ( p ) =$ $0$ 、and let $p _ { 0 } ~ \in ~ [ a , b ]$ be arbitrary. Let $p _ { 1 }$ be the point at which the tangent line to $f$ at $( p _ { 0 } , f ( p _ { 0 } ) )$ crosses the $\pmb { x }$ -axis. For each $n \geq 1$ ,let ${ p _ { n } }$ be the $\pmb { x }$ -intercept of the line tangent to $f$ at $( p _ { n - 1 } , f ( p _ { n - 1 } ) )$ . Derive the formula describing this method.

12.Use Newton's method to solve the equation

$$
0 = { \frac { 1 } { 2 } } + { \frac { 1 } { 4 } } x ^ { 2 } - x \sin x - { \frac { 1 } { 2 } } \cos 2 x , \quad { \mathrm { w i t h ~ } } p _ { 0 } = { \frac { \pi } { 2 } } .
$$

Iterate using Newton's method until an accuracy of $1 0 ^ { - 5 }$ is obtained. Explain why the result seems unusual for Newton's method. Also, solve the equation with $p _ { 0 } = 5 \pi$ and $p _ { 0 } = 1 0 \pi$

13. The fourth-degree polynomial

$$
f ( x ) = 2 3 0 x ^ { 4 } + 1 8 x ^ { 3 } + 9 x ^ { 2 } - 2 2 1 x - 9
$$

has two real zeros, one in $\left[ - 1 , 0 \right]$ and the other in [0,1]. Attempt to approximate these zeros to within $1 0 ^ { - 6 }$ using the

a. Method of False Position b. Secant method c. Newton's method

Use the endpoints of each interval as the initial approximations in (a)and(b)and the midpoints as the initial approximation in (c).

14. The function $f ( x ) = \tan \pi x - 6$ has a zero at $( 1 / \pi )$ arctan $6 \approx 0 , 4 4 7 4 3 1 5 4 3$ .Let $p _ { 0 } = 0$ and $p _ { 1 } = 0 . 4 8$ ,and use ten iterations of each of the following methods to approximate this root. Which method is most successful and why?

a. Bisection method b. Method of False Position c. Secant method

15.The iteration equation for the Secant method can be writen in the simpler form

$$
p _ { n } = { \frac { f ( p _ { n - 1 } ) p _ { n - 2 } - f ( p _ { n - 2 } ) p _ { n - 1 } } { f ( p _ { n - 1 } ) - f ( p _ { n - 2 } ) } } .
$$

Explain why, in general,this iteration equation is likelyto be less accurate than the one given in Algorithm 2.4.

16.The equation $x ^ { 2 } - 1 0 \cos x = 0$ has two solutions, ±1.3793646. Use Newton's method to approximate the solutions to within $1 0 ^ { - 5 }$ with the following values of $p _ { 0 }$

a. $\begin{array} { l l } { { \mathrm {  ~ \sigma ~ } = - 1 0 0 } } & { { \mathrm {  ~ \psi ~ } { \bf { b } } _ { \ast } \mathrm {  ~ \psi ~ } p _ { 0 } = - 5 0 \mathrm {  ~ \psi ~ } \qquad { \bf { c } } . \mathrm {  ~ \psi ~ } p _ { 0 } = - 2 5 } } \\ { { \mathrm {  ~ \sigma ~ } = 2 5 } } & { { \mathrm {  ~ \psi ~ } { \bf { e } } . \mathrm {  ~ \psi ~ } p _ { 0 } = 5 0 \mathrm {  ~ \psi ~ } \qquad { \bf { f } } . \mathrm {  ~ \psi ~ } p _ { 0 } = 1 0 0 } } \end{array}$ d $p _ { 0 } = 2 5$

17.Use Maple to determine how many iterations of Newton's method with $p _ { 0 } = \pi / 4$ are needed to find a root of $f ( x ) = \cos x - x$ to within $1 0 ^ { - 1 0 0 }$

18.Repeat Exercise 17 with $\begin{array} { r } { p _ { 0 } = \frac { 1 } { 2 } , p _ { 1 } = \frac { \pi } { 4 } } \end{array}$ , and the Secant method.

19. The function described by $f ( x ) = \ln ( x ^ { 2 } + 1 ) - e ^ { 0 . 4 x } \cos \pi$ x has an infinite number of zeros.

${ \pmb { \mathrm { a } } } _ { \pmb { \mathrm { \cdot } } }$ Determine, within $1 0 ^ { - 6 }$ , the only negative zero.   
$\smash { \mathbf { b } } _ { \bullet }$ Determine, within $1 0 ^ { - 6 }$ , the four smallest positive zeros.   
$\pmb { \mathbb { c } } _ { \bullet }$ Determine a reasonable initial approximation to find the nth smallest positive zero of $f$ {Hint: Sketch an approximate graph of $f$ .]   
d. Use part (c) to determine, within $1 0 ^ { - 6 }$ , the 25th smallest positive zero of $f$

20.Find an approximation for $\lambda$ , accurate to within $1 0 ^ { - 4 }$ , for the population equation

$$
1 , 5 6 4 , 0 0 0 = 1 , 0 0 0 , 0 0 0 e ^ { \lambda } + \frac { 4 3 5 , 0 0 0 } { \lambda } ( e ^ { \lambda } - 1 ) ,
$$

discussed in the introduction to this chapter. Use this value to predict the population at the end of the second year, assuming that the immigration rate during this year remains at 435,000 individuals per year.

21.The sum of two numbers is 20. If each number is added to its square root, the product of the two sums is 155.55. Determine the two numbers to within $1 0 ^ { - 4 }$ ，

22.The accumulated value of a savings account based on regular periodic payments can be determined from the annuity due equation,

$$
A = { \frac { P } { i } } \{ ( 1 + i ) ^ { n } - 1 \} .
$$

In this equation, $\pmb { A }$ is the amount in the account, $P$ is the amount regularly deposited, and i is the rate of interest per period for the $\pmb { n }$ deposit periods. An engineer would like to have a savings account valued at $\$ 750,000$ upon retirement in 2O years and can afford to put $\$ 1500$ per month toward this goal. What is the minimal interest rate at which this amount can be invested, assuming that the interest is compounded monthly?

23.Problems involving the amount of money required to pay off a mortgage over a fixed period of time involve the formula

$$
A = { \frac { P } { i } } [ 1 - ( 1 + i ) ^ { - n } ] ,
$$

known as an ordinary annuity equation. In this equation, $\pmb { A }$ is the amount of the mortgage, $P$ is the amount of each payment, and $\pmb { i }$ is the interest rate per period for the n payment periods. Suppose that a 30-year home mortgage in the amount of $\$ 135,000$ is needed and that the borrower can afford house payments of at most $\$ 1000$ per month. What is the maximal interest rate the borrower can afford to pay?

24.A drug administered to a patient produces a concentration in the blood stream given by $c ( t ) =$ $A t e ^ { - t / 3 }$ milligrams per milliliter, t hours after A units have been injected. The maximum safe concentration is $1 \ m g / \ m \}$

a. What amount should be injected to reach this maximum safe concentration, and when does this maximum occur?   
b. An additional amount of this drug is to be administered to the patient after the concentration falls to $0 . 2 5 ~ \mathrm { m g / m l }$ . Determine, to the nearest minute, when this second injection should be given.   
c. Assume that the concentration from consecutive injections is additive and that $75 \%$ of the amount originally injected is administered in the second injection. When is it time for the third injection?

25.Let $f ( x ) = 3 ^ { 3 x + 1 } - 7 \cdot 5 ^ { 2 x }$

$\bullet$ Use the Maple commands solve and fsolve to try to find al roots of $f$ $\mathbf { b } .$ Plot $f ( x )$ to find initial approximations to roots of $f$ $\bullet \bullet$ Use Newton's method to find roots of $f$ to within $1 0 ^ { - 1 6 }$ ， d. Find the exact solutions of $f ( x ) = 0$ algebraically.

26.Repeat Exercise 25 using $f ( x ) = 2 ^ { x ^ { 2 } } - 3 \cdot 7 ^ { x + 1 }$ ·

27.The logistic population growth model is described by an equation of the form

$$
P ( t ) = \frac { P _ { L } } { 1 - c e ^ { - k t } } ,
$$

where $P _ { L } , c ,$ and $k > 0$ are constants, and $P ( t )$ is the population at time t. $P _ { L }$ represents the limiting value of the population since $\begin{array} { r } { \operatorname* { l i m } _ { t \to \infty } P ( t ) = P _ { L } } \end{array}$ . Use the census data for the years 1950,i960, and 1970 listed in the table on page 104 to determine the constants $P _ { L } , c .$ and $k$ for a logistic growth model. Use the logistic model to predict the population of the United States in 1980 and in 2010,assuming ${ \pmb t } = { \pmb 0 }$ at 1950. Compare the 1980 prediction to the actual value.

28.The Gompertz population growth model is described by

$$
P ( t ) = P _ { L } e ^ { - c e ^ { - k t } } ,
$$

where $P _ { L }$ ,c, and $k > 0$ are constants, and $P ( t )$ is the population at time t. Repeat Exercise 27 using the Gompertz growth model in place of the logistic model.

29.Player A willsut out (win by a score of 21-O) player $\mathbf { B }$ in a game of racquetball with probability

$$
P = \frac { 1 + p } { 2 } \left( \frac { p } { 1 - p + p ^ { 2 } } \right) ^ { 2 1 } ,
$$

where $p$ denotes the probability A will win any specific rally (independent of the server). (See [Keller, J], p.267.) Determine, to within $1 0 ^ { - 3 }$ , the minimal value of $\pmb { p }$ that will ensure that A will shut out B in at least half the matches they play.

30.In the design of al-terrain vehicles, it is necessary to consider the failure of the vehicle when attempting to negotiate two types of obstacles. One type of failure is called hang-up failure and occurs when the vehicle atempts to cross an obstacle that causes the bottom of the vehicle to touch the ground. The other type of failure is called nose-in failure and occurs when the vehicle descends into a ditch and its nose touches the ground.

The accompanying figure, adapted from [Bek], shows the components associated with the nose-in failure of a vehicle. In that reference it is shown that the maximum angle $\pmb { \alpha }$ that can be negotiated by a vehicle when $\beta$ is the maximum angle at which hang-up failure does not occur satisfies the equation

$$
\begin{array} { r } { A \sin \alpha \cos \alpha + B \sin ^ { 2 } \alpha - C \cos \alpha - E \sin \alpha = 0 , } \end{array}
$$

where

$$
\begin{array} { r l } & { A = l \sin \beta _ { 1 } , \quad B = l \cos \beta _ { 1 } , \quad C = ( h + 0 . 5 D ) \sin \beta _ { 1 } - 0 . 5 D \tan \beta _ { 1 } , } \\ & { E = ( h + 0 . 5 D ) \cos \beta _ { 1 } - 0 . 5 D . } \end{array}
$$

a. It is stated that when $l = 8 9$ in., $h = 4 9$ in., $D = 5 5$ in.,and $\beta _ { \mathrm { l } } = 1 1 . 5 ^ { \circ }$ , angle $\pmb { \alpha }$ is approximately $3 3 ^ { \circ }$ . Verify this result.

b.Find $\pmb { \alpha }$ for the situation when $l , h$ , and $\beta _ { 1 }$ are the same as in part (a) but $D = 3 0$ in.

![](images/fa839ae3fe1a7a5602dab667983b1164290bbb2068eb383cc7132a6bbec638e4.jpg)

# 2.4 Error Analysis for Iterative Methods

In this section we investigate the order of convergence.of functional iteration schemes and, as a means of obtaining rapid convergence,rediscover Newton's method. We also consider ways of accelerating the convergence of Newton's method in special circumstances. First, however, we need a procedure for measuring how rapidly a sequence converges.

# Definition 2.6

Suppose $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ is a sequence that converges to $p$ ，with $p _ { n } \neq p$ for all $\pmb { n }$ . If positive constants $\lambda$ and $\pmb { \alpha }$ exist with

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { | p _ { n + 1 } - p | } { | p _ { n } - p | ^ { \alpha } } } = \lambda ,
$$

then $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ converges to $\pmb { p }$ of order $\pmb { \alpha }$ , with asymptotic error constant $\pmb { \lambda }$

An iterative technique of the form $p _ { n } = g ( p _ { n - 1 } )$ is said to be of order $\pmb { \alpha }$ if the sequence $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ converges to the solution $p = g ( p )$ of order $\pmb { \alpha }$

In general, a sequence with a high order of convergence converges more rapidly than a sequence with a lower order. The asymptotic constant affects the speed of convergence but is not as important as the order. Two cases of order are given special attention.

iIf $\alpha = 1$ , the sequence is linearly convergent.   
(ii）If $\alpha = 2$ , the sequence is quadratically convergent.

The next example compares a linearly convergent sequence to one that is quadratically convergent. It shows why we try to find methods that produce higher-order convergeni sequences.

Suppose that $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ is linearly convergent to O with

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { | p _ { n + 1 } | } { | p _ { n } | } } = 0 . 5
$$

and that $\{ \tilde { p } _ { n } \} _ { n = 0 } ^ { \infty }$ is quadratically convergent to O with the same asymptotic error constant,

$$
\operatorname* { l i m } _ { n  \infty } \frac { | \tilde { p } _ { n + 1 } | } { | \tilde { p } _ { n } | ^ { 2 } } = 0 . 5 .
$$

For simplicity, suppose that

$$
\frac { | p _ { n + 1 } | } { | p _ { n } | } \approx 0 . 5 \quad \mathrm { a n d } \quad \frac { | \tilde { p } _ { n + 1 } | } { | \tilde { p } _ { n } | ^ { 2 } } \approx 0 . 5 .
$$

For the linearly convergent scheme, this means that

$$
| p _ { n } - 0 | = | p _ { n } | \approx 0 . 5 | p _ { n - 1 } | \approx ( 0 . 5 ) ^ { 2 } | p _ { n - 2 } | \approx \cdot \cdot \cdot \approx ( 0 . 5 ) ^ { n } | p _ { 0 } | ,
$$

whereas the quadratically convergent procedure has

$$
\begin{array} { r l } & { | \tilde { p } _ { n } - 0 | = | \tilde { p } _ { n } | \approx 0 . 5 | \tilde { p } _ { n - 1 } | ^ { 2 } \approx ( 0 . 5 ) [ 0 . 5 | \tilde { p } _ { n - 2 } | ^ { 2 } ] ^ { 2 } = ( 0 . 5 ) ^ { 3 } | \tilde { p } _ { n - 2 } | ^ { 4 } } \\ & { \qquad \approx ( 0 . 5 ) ^ { 3 } [ ( 0 . 5 ) | \tilde { p } _ { n - 3 } | ^ { 2 } ] ^ { 4 } = ( 0 . 5 ) ^ { 7 } | \tilde { p } _ { n - 3 } | ^ { 8 } } \\ & { \qquad \approx \cdot \cdot \approx ( 0 . 5 ) ^ { 2 ^ { n } - 1 } | \tilde { p } _ { 0 } | ^ { 2 ^ { n } } . } \end{array}
$$

# Table 2.7

Table 2.7 ilustrates the relative speed of convergence of the sequences to O when $| p _ { 0 } | =$ $| \tilde { p } _ { 0 } | = 1$ .   

<table><tr><td>Linear Convergence Sequence {pn)0 (0.5) n</td><td>Quadratic Convergence Sequence (P0 (0.5)2-1</td></tr><tr><td>1 5.0000 × 10-1</td><td>5.0000 × 10-1</td></tr><tr><td>2 2.5000 × 10-1</td><td>1.2500 × 10-1</td></tr><tr><td>3 1.2500 × 10-1 10-2</td><td>7.8125 × 10-3</td></tr><tr><td>4 6.2500 ×</td><td>3.0518 × 10-5</td></tr><tr><td>5 3.1250 × 10-2 10-2</td><td>4.6566 × 10-10</td></tr><tr><td>6 1.5625 ×</td><td>1.0842 × 10-19 10-39</td></tr><tr><td>7 7.8125 × 10-3</td><td>5.8775 ×</td></tr></table>

The quadratically convergent sequence is within $1 0 ^ { - 3 8 }$ of O by the seventh term. At least 126 terms are needed to ensure this accuracy for the linearly convergent sequence.

Quadratically convergent sequences generally converge much more quickly than those that converge only linearly,but many techniques that generateconvergent sequences do so only linearly.

Let $g \in C [ a , b ]$ be such that $g ( x ) \in \{ a , b \}$ , for all $x \in [ a , b ]$ . Suppose, in addition, that $g ^ { \prime }$ is continuous on $( a , b )$ and a positive constant $k < 1$ exists with

$$
| g ^ { \prime } ( x ) | \leq k , \quad { \mathrm { f o r ~ a l l ~ } } x \in ( a , b ) .
$$

If $g ^ { \prime } ( p ) \neq 0$ , then for any number $p _ { 0 }$ in $[ a , b ]$ , the sequence

$$
p _ { n } = g ( p _ { n - 1 } ) , \quad \mathrm { f o r } n \geq 1 ,
$$

converges only linearly to the unique fixed point $p$ in $[ a , b ]$

ProofWe know from the Fixed-Point Theorem 2.3 in Section 2.2 that the sequence converges to $\pmb { p }$ . Since $\pmb { g } ^ { \prime }$ exists on $\left[ a , b \right]$ , we can apply the Mean Value Theorem to $\pmb { g }$ to show that for any $\pmb { n }$ ，

$$
p _ { n + 1 } - p = g ( p _ { n } ) - g ( p ) = g ^ { \prime } ( \xi _ { n } ) ( p _ { n } - p ) ,
$$

where $\xi _ { n }$ is between $p _ { n }$ and $p$ . Since $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ converges to $p$ , we also have $\{ \xi _ { n } \} _ { n = 0 } ^ { \infty }$ converging to $p$ . Since $\pmb { g } ^ { \prime }$ is continuous on $[ a , b ]$ ,we have

$$
\operatorname* { l i m } _ { n  \infty } g ^ { \prime } ( \xi _ { n } ) = g ^ { \prime } ( p ) .
$$

Thus,

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { p _ { n + 1 } - p } { p _ { n } - p } } = \operatorname* { l i m } _ { n \to \infty } g ^ { \prime } ( \xi _ { n } ) = g ^ { \prime } ( p ) \quad { \mathrm { a n d } } \quad \operatorname* { l i m } _ { n \to \infty } { \frac { | p _ { n + 1 } - p | } { | p _ { n } - p | } } = | g ^ { \prime } ( p ) | .
$$

Hence, if ${ \pmb g } ^ { \prime } ( { \pmb p } ) \neq { \bf 0 }$ ,fixed-point iteration exhibits linear convergence with asymptotic error constant $| { \pmb g } ^ { \prime } ( { \pmb p } ) |$ · ■ ■

Theorem 2.7 implies that higher-order convergence for fixed-point methods can occur only when $g ^ { \prime } ( p ) = 0 .$ . The next result describes additional conditions that ensure the quadratic convergence we seek.

Let $p$ be a solution of the equation ${ \pmb x } = { \pmb g } ( { \pmb x } )$ . Suppose that $g ^ { \prime } ( p ) = 0$ and ${ \pmb g } ^ { \prime \prime }$ is continuous and strictly bounded by $\pmb { M }$ on an open interval $\pmb { I }$ containing $p$ . Then there exists a $\delta > 0$ such that, for $p _ { 0 } \in [ p - \delta , p + \delta ]$ ， the sequence defined by $p _ { n } = g ( p _ { n - 1 } )$ ， when $n \geq 1$ ， converges at least quadratically to $p$ . Moreover, for suffciently large values of $\pmb { n }$ ，

$$
| p _ { n + 1 } - p | < \frac { M } { 2 } | p _ { n } - p | ^ { 2 } .
$$

Proof Choose $\pmb { k }$ in (0, 1) and $\delta > 0$ such that on the interval $[ p - \delta , p + \delta ] ,$ contained in $\pmb { I }$ ， we have $| g ^ { \prime } ( x ) | \leq k$ and ${ \pmb g } ^ { \prime \prime }$ continuous. Since $| g ^ { \prime } ( x ) | \le k < 1$ ， the argument used in the proof of Theorem 2.5 in Section 2.3 shows that the terms of the sequence $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ are contained in $[ p - \delta , p + \delta ]$ . Expanding $g ( x )$ in a linear Taylor polynomial for

$x \in [ p \neg \delta , p \neg \delta ]$ gives

$$
g ( x ) = g ( p ) + g ^ { \prime } ( p ) ( x - p ) + \frac { g ^ { \prime \prime } ( \xi ) } { 2 } ( x - p ) ^ { 2 } ,
$$

where ${ \pmb \xi }$ lies between $\pmb { x }$ and $p$ . The hypotheses $g ( p ) = p$ and $g ^ { \prime } ( p ) = 0$ imply that

$$
g ( x ) = p + { \frac { g ^ { \prime \prime } ( \xi ) } { 2 } } ( x - p ) ^ { 2 } .
$$

In particular, when ${ \mathfrak { x } } = p _ { n }$

$$
p _ { n + 1 } = g ( p _ { n } ) = p + \frac { g ^ { \prime \prime } ( \xi _ { n } ) } { 2 } ( p _ { n } - p ) ^ { 2 } ,
$$

with $\xi _ { n }$ between $p _ { n }$ and $p$ .Thus,

$$
p _ { n + 1 } - p = { \frac { g ^ { \prime \prime } ( \xi _ { n } ) } { 2 } } ( p _ { n } - p ) ^ { 2 } .
$$

Since $| g ^ { \prime } ( x ) | \leq k < 1$ on $[ p - \delta , p + \delta ]$ and $\pmb { g }$ maps $[ p - \delta , p + \delta ]$ into itself, it follows fromtheFixed-PointTheoremthat $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ converges to $p$ .But $\xi _ { n }$ is between $p$ and $p _ { n }$ for each $n , s 0 \left\{ \xi _ { n } \right\} _ { n = 0 } ^ { \infty }$ also converges to $p$ ,and

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { | p _ { n + 1 } - p | } { | p _ { n } - p | ^ { 2 } } } = { \frac { | g ^ { \prime \prime } ( p ) | } { 2 } } .
$$

This result implies that the sequence $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ is quadratically convergent if $g ^ { \prime \prime } ( p ) \neq 0$ and of higher-order convergence if $g ^ { \prime \prime } ( p ) = 0$

Since $g ^ { \prime \prime }$ is continuous and strictly bounded by $M$ on the interval $[ p - \delta , p + \delta ]$ ,this also implies that, for sufficiently large values of $\pmb { n }$ ，

$$
| p _ { n + 1 } - p | < \frac { M } { 2 } | p _ { n } - p | ^ { 2 } .
$$

Theorems 2.7 and 2.8 tell us that our search for quadratically convergent fixed-point methods should point in the direction of functions whose derivatives are zero at the fixed point.

The easiest way to construct a fixed-point problem associated with a root-finding problem $f ( x ) = 0$ is to subtract a multiple of $f ( x )$ from $\pmb { x }$ . So let us consider

$$
p _ { n } = g ( p _ { n - 1 } ) , \quad \mathrm { f o r } n \geq 1 ,
$$

for $\pmb { g }$ in the form

$$
g ( x ) = x - \phi ( x ) f ( x ) ,
$$

where $\phi$ is a differentiable function that will be chosen later.

For the iterative procedure derived from $\pmb { g }$ to be quadratically convergent, we need tc have ${ \pmb g } ^ { \prime } ( { \pmb p } ) = { \bf 0 }$ when $f ( p ) = 0$ . Since

$$
g ^ { \prime } ( x ) = 1 - \phi ^ { \prime } ( x ) f ( x ) - f ^ { \prime } ( x ) \phi ( x ) ,
$$

we have

gp $) = 1 - \phi ^ { \prime } ( p ) f ( p ) - f ^ { \prime } ( p ) \phi ( p ) = 1 - \phi ^ { \prime } ( p ) \cdot 0 - f ^ { \prime } ( p ) \phi ( p ) = 1 - f ^ { \prime } ( p ) \phi ( p ) ,$ and $g ^ { \prime } ( p ) = 0$ if and only if $\phi ( p ) = 1 / f ^ { \prime } ( p )$

If we let $\phi ( x ) = 1 / f ^ { \prime } ( x )$ , then we will ensure that $\phi ( p ) = 1 / f ^ { \prime } ( p )$ and produce the quadratically convergent procedure

$$
p _ { n } = g ( p _ { n - 1 } ) = p _ { n - 1 } - \frac { f ( p _ { n - 1 } ) } { f ^ { \prime } ( p _ { n - 1 } ) } .
$$

This, of course, is simply Newton's method.

In the preceding discussion, the restriction was made that $f ^ { \prime } ( p ) \neq 0$ ,where $p$ is the solution to $f ( x ) = 0$ . From the definition of Newton's method, it is clear that difficulties might occur if $f ^ { \prime } ( p _ { n } )$ goes to zero simultaneously with $f ( p _ { n } )$ . In particular, Newton's method and the Secant method will generally give problems if $f ^ { \prime } ( p ) = 0$ when $f ( p ) = 0$ To examine these difficulties in more detail, we make the following definition.

# Definition 2.9

A solution $p$ of $f ( x ) = 0$ is a zero of multiplicity $m$ of $f$ if for $x \neq p$ ， we can write $f ( x ) = ( x - p ) ^ { m } q ( x )$ ， where $\begin{array} { r } { \operatorname* { l i m } _ { x \to p } q ( x ) \neq 0 } \end{array}$

In essence, $q ( x )$ represents that portion of $f ( x )$ that does not contribute to the zero of $f$ . The following result gives a means to easily identify simple zeros of a function, those that have multiplicity one.

$f \in C ^ { 1 } [ a , b ]$ has a simple zero at $p$ in $( a , b )$ if and only if $f ( p ) = 0$ ,but $f ^ { \prime } ( p ) \neq 0$

Proof If $f$ has a simple zero at $p$ ,then $f ( p ) = 0$ and $f ( x ) = ( x - p ) q ( x )$ ，where$\begin{array} { r } { \operatorname* { l i m } _ { x \to p } q ( x ) \neq 0 } \end{array}$ . Since $f \in C ^ { 1 } [ a , b ]$ ，

$$
f ^ { \prime } ( p ) = \operatorname* { l i m } _ { x \to p } f ^ { \prime } ( x ) = \operatorname* { l i m } _ { x \to p } [ q ( x ) + ( x - p ) q ^ { \prime } ( x ) ] = \operatorname* { l i m } _ { x \to p } q ( x ) \neq 0 .
$$

Conversely, if $f ( p ) = 0$ ,but $f ^ { \prime } ( p ) \neq 0$ , expand $f$ in a zeroth Taylor polynomial about $p$ Then

$$
f ( x ) = f ( p ) + f ^ { \prime } ( \xi ( x ) ) ( x - p ) = ( x - p ) f ^ { \prime } ( \xi ( x ) ) ,
$$

where $\xi ( x )$ is between $\pmb { x }$ and $p$ . Since $f \in C ^ { 1 } \{ a , b \} .$

$$
\operatorname* { l i m } _ { x \to p } f ^ { \prime } ( \xi ( x ) ) = f ^ { \prime } \left( \operatorname* { l i m } _ { x \to p } \xi ( x ) \right) = f ^ { \prime } ( p ) \neq 0 .
$$

Letting $q = f ^ { \prime } \circ \xi$ gives $f ( x ) = ( x - p ) q ( x )$ , where $\begin{array} { r } { \operatorname* { l i m } _ { x \to p } q ( x ) \neq 0 } \end{array}$ Thus, $f$ has a simple zero at $p$ ...

The following generalization of Theorem 2.1O is considered in Exercise 10.

Theorem 2.11 The function $f \in C ^ { m } [ a , b ]$ has a zero of multiplicity $_ { m }$ at $p$ in $( a , b )$ if and only if

$$
0 = f ( p ) = f ^ { \prime } ( p ) = f ^ { \prime \prime } ( p ) = \cdot \cdot \cdot = f ^ { ( m - 1 ) } ( p ) , \quad \mathrm { b u t } \quad f ^ { ( m ) } ( p ) \neq 0 .
$$

The result in Theorem 2.10 implies that an interval about $p$ exists where Newton's method converges quadratically to $p$ for any initial approximation $p _ { 0 } = p$ , provided that $p$ is a simple zero. The following example shows that quadratic convergence may not occur if the zero is not simple.

# EXAMPLE 2

Consider $f ( x ) = e ^ { x } - x - 1$ . Since $f ( 0 ) = e ^ { 0 } - 0 - 1 = 0$ and $f ^ { \prime } ( 0 ) = e ^ { 0 } - 1 = 0$ ,but $f ^ { \prime \prime } ( 0 ) = e ^ { 0 } = 1$ ， $f$ has a zero of multiplicity two at $p = 0$ . In fact, $f ( x )$ can be expressed in the form

$$
f ( x ) = ( x - 0 ) ^ { 2 } \frac { e ^ { x } - x - 1 } { x ^ { 2 } } ,
$$

where,by L'Hopital's rule,

$$
\operatorname* { l i m } _ { x \to 0 } { \frac { e ^ { x } - x - 1 } { x ^ { 2 } } } = \operatorname* { l i m } _ { x \to 0 } { \frac { e ^ { x } - 1 } { 2 x } } = \operatorname* { l i m } _ { x \to 0 } { \frac { e ^ { x } } { 2 } } = { \frac { 1 } { 2 } } \neq 0 .
$$

The terms generated by Newton's method applied to $f$ with $p _ { 0 } ~ = ~ 1$ are shown in Table 2.8.The sequence is clearly converging to O, but not quadratically. The graph of $f$ is shown in Figure 2.11.

Table 2.8   

<table><tr><td>n</td><td>Pn</td><td>n</td><td>Pn</td></tr><tr><td>0</td><td>1.0</td><td>9</td><td>2.7750 × 10-3</td></tr><tr><td>1</td><td>0.58198</td><td>10</td><td>1.3881 × 10-3</td></tr><tr><td>2</td><td>0.31906</td><td>11</td><td>6.9411 × 10-4</td></tr><tr><td>3</td><td>0.16800</td><td>12</td><td>3.4703 × 10-4</td></tr><tr><td>4</td><td>0.08635</td><td>13</td><td>1.7416 × 10-4</td></tr><tr><td>5</td><td>0.04380</td><td>14</td><td>8.8041 × 10-5</td></tr><tr><td>6</td><td>0.02206</td><td>15</td><td>4.2610 × 10-5</td></tr><tr><td>7</td><td>0.01107</td><td>16</td><td>1.9142 × 10-6</td></tr><tr><td>8</td><td>0.005545</td><td></td><td></td></tr></table>

![](images/7bc26ab22d8eaeae45f9556f3c87889a080c8bb4f78929548a5270ccac96a2f5.jpg)  
Figure 2.11

One method of handling the problem of multiple roots is to define

$$
\mu ( x ) = \frac { f ( x ) } { f ^ { \prime } ( x ) } .
$$

If $p$ is a zero of $f$ of multiplicity $m$ and $f ( x ) = ( x - p ) ^ { m } q ( x )$ , then

$$
\begin{array} { c } { { \mu ( x ) = \displaystyle \frac { ( x - p ) ^ { m } q ( x ) } { m ( x - p ) ^ { m - 1 } q ( x ) + ( x - p ) ^ { m } q ^ { \prime } ( x ) } } } \\ { { = ( x - p ) \displaystyle \frac { q ( x ) } { m q ( x ) + ( x - p ) q ^ { \prime } ( x ) } } } \end{array}
$$

also has a zero at $p$ . However, $q ( p ) \neq 0$ ,so

$$
\frac { q ( p ) } { m q ( p ) + ( p - p ) q ^ { \prime } ( p ) } = \frac { 1 } { m } \neq 0 ,
$$

and $p$ is a simple zero of $\mu$ . Newton's method can then be applied to $\mu$ to give

$$
g ( x ) = x - { \frac { \mu ( x ) } { \mu ^ { \prime } ( x ) } } = x - { \frac { f ( x ) / f ^ { \prime } ( x ) } { \{ [ f ^ { \prime } ( x ) ] ^ { 2 } - [ f ( x ) ] [ f ^ { \prime \prime } ( x ) ] \} / [ f ^ { \prime } ( x ) ] ^ { 2 } } }
$$

or

$$
g ( x ) = x - { \frac { f ( x ) f ^ { \prime } ( x ) } { [ f ^ { \prime } ( x ) ] ^ { 2 } - f ( x ) f ^ { \prime \prime } ( x ) } } .
$$

If $g$ has the required continuity conditions, functional iteration applied to $g$ will be quadratically convergent regardless of the multiplicity of the zero of $f$ . Theoretically, the only drawback to this method is the additional calculation of $f ^ { \prime \prime } ( x )$ and the more laborious procedure of calculating the iterates. In practice, however, multiple roots can cause serious roundoff problems since the denominator of (2.11) consists of the difference of two numbers that are both close to 0.

# EXAMPlE 3

Table 2.9 lists the approximations to the double zero at ${ \boldsymbol { x } } = { \bf 0 }$ of $f ( x ) = e ^ { x } - x - 1$ using $p _ { n } = g ( p _ { n - 1 } )$ ,for $n \geq 1$ ,where $\pmb { g }$ is given by (2.11). The results were recorded using a calculator with ten digits of precision. The initial approximation of $p _ { 0 } = 1$ was chosen so that the entries can be compared with those in Table 2.8.What Table 2.9 does not show is that no improvement to the zero approximation $- 2 . 8 0 8 5 2 1 7 \times 1 0 ^ { - 7 }$ occurs in subsequent computations using this calculator since both the numerator and the denominator approach 0. ■ In Example 3 of Section 2.2 we solved $f ( x ) = x ^ { 3 } + 4 x ^ { 2 } - 1 0 = 0$ for the zero $p =$ 1.36523o01. To compare convergence for a zero of multiplicity one by Newton's method and the modified Newton's method listed in Eq. (2.11), let

Table 2.9   

<table><tr><td>n</td><td>Pn</td></tr><tr><td>1</td><td>-2.3421061 × 10-1</td></tr><tr><td>2</td><td>-8.4582788 × 10-3</td></tr><tr><td>3</td><td>-1.1889524 × 10-5</td></tr><tr><td>4</td><td>-6.8638230 × 10-6</td></tr><tr><td>5</td><td>-2.8085217 × 10-7</td></tr><tr><td></td><td></td></tr></table>

$$
p _ { n } = p _ { n - 1 } - \frac { p _ { n - 1 } ^ { 3 } + 4 p _ { n - 1 } ^ { 2 } - 1 0 } { 3 p _ { n - 1 } ^ { 2 } + 8 p _ { n - 1 } } ,
$$

and, from $p _ { n } = g ( p _ { n - 1 } )$ ， where $g$ is given by Eq. (2.11),

$$
p _ { n } = p _ { n - 1 } - \frac { ( p _ { n - 1 } ^ { 3 } + 4 p _ { n - 1 } ^ { 2 } - 1 0 ) ( 3 p _ { n - 1 } ^ { 2 } + 8 p _ { n - 1 } ) } { ( 3 p _ { n - 1 } ^ { 2 } + 8 p _ { n - 1 } ) ^ { 2 } - ( p _ { n - 1 } ^ { 3 } + 4 p _ { n - 1 } ^ { 2 } - 1 0 ) ( 6 p _ { n - 1 } + 8 ) } .
$$

With $p _ { 0 } = 1 . 5$ ,the first three iterates for (i) and (ii) are shown in Table 2.10. The results illustrate the rapid convergence of both methods in the case of a simple zero.

Table 2.10   

<table><tr><td>(i)</td><td>(ii)</td></tr><tr><td>1.37333333 P1</td><td>1.35689898</td></tr><tr><td>P2 1.36526201</td><td>1.36519585</td></tr><tr><td>P3 1.36523001</td><td>1.36523001</td></tr></table>

# ExErcise Set 2.4

1.Use Newton’s method to find solutions accurate to within $1 0 ^ { - 5 }$ to the following problems.

a. $x ^ { 2 } - 2 x e ^ { - x } + e ^ { - 2 x } = 0 , \quad { \mathrm { f o r ~ } } 0 \leq x \leq 1$ ${ \bf b } _ { \bullet }$ $\cos ( x + { \sqrt { 2 } } ) + x ( x / 2 + { \sqrt { 2 } } ) = 0 , \quad \mathrm { f o r } - 2 \leq x \leq - 1$ c. $x ^ { 3 } - 3 x ^ { 2 } ( 2 ^ { - x } ) + 3 x ( 4 ^ { - x } ) - 8 ^ { - x } = 0 ,$ for0≤x ≤1 d. $e ^ { 6 x } + 3 ( \ln 2 ) ^ { 2 } e ^ { 2 x } - ( \ln 8 ) e ^ { 4 x } - ( \ln 2 ) ^ { 3 } = 0 , ~ \mathrm { f o r } - 1 \leq x \leq 0$

2. Repeat Exercise 1 using the modified Newton-Raphson method described in Eq. (2.11). I: there an improvement in speed or accuracy over Exercise 1?

3.Use Newton's method and the modified Newton-Raphson method described in Eq.(2.11) to find a solution accurate to within $1 0 ^ { - 5 }$ to the problem

$$
e ^ { 6 x } + 1 . 4 4 1 e ^ { 2 x } - 2 . 0 7 9 e ^ { 4 x } - 0 . 3 3 3 0 = 0 , \quad \mathrm { f o r } \ - 1 \leq x \leq 0 .
$$

This is the same problem as 1(d) with the coeficients replaced by their four-digit approximations. Compare the solutions to the results in 1(d) and 2(d).

4.Show that the following sequences converge linearly to $p = 0$ . How large must $\pmb { n }$ be before $| p _ { n } - p | \leq 5 \times 1 0 ^ { - 2 } ?$

a. $p _ { n } = { \frac { 1 } { n } } , \quad n \geq 1$ ${ \bf b . } \quad p _ { n } = { \frac { 1 } { n ^ { 2 } } } , \quad n \ge 1$

5.a. Show that for any positive integer $k$ , the sequence defined by $p _ { n } ~ = ~ 1 / n ^ { k }$ converges linearly to $p = 0$

b.For each pair of integers $k$ and $\pmb { m }$ , determine a number $N$ for which $1 / N ^ { k } < 1 0 ^ { - m }$

6.a.Show that the sequence $p _ { n } = 1 0 ^ { - 2 ^ { r } }$ converges quadratically to 0. ${ \bf h } _ { \bullet }$ Show that the sequence $p _ { n } = 1 0 ^ { - n ^ { k } }$ does not converge to O quadratically, regardless of the size of the exponent $k > 1$   
7.a. Construct a sequence that converges to O of order 3. $\mathbf { b } _ { \bullet }$ Suppose $\alpha > 1$ . Construct a sequence that converges to O zero of order $\pmb { \alpha }$ ·

8. Suppose $p$ is a zero of multiplicity $m$ of $f$ ，where $f ^ { \prime \prime \prime }$ is continuous on an open interval containing $p$ . Show that the following fixed-point method has $g ^ { \prime } ( p ) = 0$ ：

$$
g ( x ) = x - { \frac { m f ( x ) } { f ^ { \prime } ( x ) } } .
$$

9. Show that the Bisection Algorithm 2.1 gives a sequence with an error bound that converges linearly to 0.

10. Suppose that $f$ has m continuous derivatives.Modify the proof of Theorem 2.10 to show that $f$ has a zero of muitiplicity $m$ at $p$ if and only if

$$
0 = f ( p ) = f ^ { \prime } ( p ) = \cdots = f ^ { ( m - 1 ) } ( p ) , \quad { \mathrm { b u t ~ } } \ f ^ { ( m ) } ( p ) \neq 0 .
$$

11.The iterative method to solve $f ( x ) = 0$ ， given by the fixed-point method $g ( x ) = x$ ，where

$$
p _ { n } = g ( p _ { n - 1 } ) = p _ { n - 1 } - \frac { f ( p _ { n - 1 } ) } { f ^ { \prime } ( p _ { n - 1 } ) } - \frac { f ^ { \prime \prime } ( p _ { n - 1 } ) } { 2 f ^ { \prime } ( p _ { n - 1 } ) } \left[ \frac { f ( p _ { n - 1 } ) } { f ^ { \prime } ( p _ { n - 1 } ) } \right] ^ { 2 } , \quad \mathrm { f o r } \ n = 1 , 2 , 3 , \dots ,
$$

has $g ^ { \prime } ( p ) = g ^ { \prime \prime } ( p ) = 0$ . This will generally yield cubic $\{ \mathfrak {alpha } = 3 \}$ ）convergence. Expand the analysis of Example l to compare quadratic and cubic convergence.

12.It can be shown (see,for example, $\left[ \mathbf { D a B } \right.$ pp. 228-29) that if $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ are convergent Secant method approximations to p,the solution to f(x）= 0, then a constant C exists with $\vert p _ { n + 1 } - p \vert \approx C \vert p _ { n } - p \vert \vert p _ { n - 1 } - p \vert$ for sufficiently large values of $\pmb { n }$ . Assume $\{ p _ { n } \}$ converges to p of order α,and show that α = (1 + √5)/2. (Note: This implies that the order of conver-gence of the Secant method is approximately 1.62).

# 2.5 Accelerating Convergence

It is rare to have the luxury of quadratic convergence. We now consider a technique called Aitken's $\Delta ^ { 2 }$ method that can be used to accelerate the convergence of a sequence that is linearly convergent, regardless of its origin or application.

Suppose $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ is a linearly convergent sequence with limit $p$ . To motivate the con-struction of a sequence $\{ \hat { p } _ { n } \} _ { n = 0 } ^ { \infty }$ that converges more rapidly to $p$ than does $\{ p _ { n } \} _ { n = 0 } ^ { \infty } ,$ let us first assume that the signs of $p _ { n } - p , p _ { n + 1 } - p$ ,and $p _ { n + 2 } - p$ agree and that $\pmb { n }$ is sufficiently large that

$$
{ \frac { p _ { n + 1 } - p } { p _ { n } - p } } \approx { \frac { p _ { n + 2 } - p } { p _ { n + 1 } - p } } .
$$

Then

$$
( p _ { n + 1 } - p ) ^ { 2 } \approx ( p _ { n + 2 } - p ) ( p _ { n } - p ) ,
$$

So

$$
p _ { n + 1 } ^ { 2 } - 2 p _ { n + 1 } p + p ^ { 2 } \approx p _ { n + 2 } p _ { n } - ( p _ { n } + p _ { n + 2 } ) p + p ^ { 2 }
$$

and

$$
( p _ { n + 2 } + p _ { n } - 2 p _ { n + 1 } ) p \approx p _ { n + 2 } p _ { n } - p _ { n + 1 } ^ { 2 } .
$$

Solving for $p$ gives

$$
p \approx { \frac { p _ { n + 2 } p _ { n } - p _ { n + 1 } ^ { 2 } } { p _ { n + 2 } - 2 p _ { n + 1 } + p _ { n } } } .
$$

Adding and subtracting the terms $p _ { n } ^ { 2 }$ and $2 p _ { n } p _ { n + 1 }$ in the numerator and grouping terms appropriately gives

$$
\begin{array} { r l } & { p \approx \frac { p _ { n } ^ { 2 } - p _ { n } p _ { n + 2 } - 2 p _ { n } p _ { n + 1 } - 2 p _ { n } p _ { n + 1 } - p _ { n } ^ { 2 } - p _ { n + 1 } ^ { 2 } } { p _ { n + 2 } - 2 p _ { n + 1 } + p _ { n } } } \\ & { \quad = \frac { ( p _ { n } ^ { 2 } - p _ { n } p _ { n + 2 } + 2 p _ { n } p _ { n + 1 } ) - ( p _ { n } ^ { 2 } - 2 p _ { n } p _ { n + 1 } + p _ { n + 1 } ^ { 2 } ) } { p _ { n + 2 } - 2 p _ { n + 1 } + p _ { n } } } \\ & { \quad = p _ { n } - \frac { ( p _ { n + 1 } - p _ { n } ) ^ { 2 } } { p _ { n + 2 } - 2 p _ { n + 1 } + p _ { n } } . } \end{array}
$$

Aitken's $\Delta ^ { 2 }$ method is based on the assumption that the sequence $\{ \hat { p } _ { n } \} _ { n = 0 } ^ { \infty }$ , defined by

$$
\hat { p } _ { n } = p _ { n } - \frac { ( p _ { n + 1 } - p _ { n } ) ^ { 2 } } { p _ { n + 2 } - 2 p _ { n + 1 } + p _ { n } } ,
$$

Converges more rapidly to $p$ than does the original sequence $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$

# EXAMPLE 1

The sequence $\{ p _ { n } \} _ { n = 1 } ^ { \infty }$ ， where $p _ { n } = \cos ( 1 / n )$ , converges linearly to $p = 1$ . The first few terms of the sequences $\{ p _ { n } \} _ { n = 1 } ^ { \infty }$ and $\{ \hat { p } _ { n } \} _ { n = 1 } ^ { \infty }$ are given inTable 2.11 Itcertainy appears that $\{ \hat { p } _ { n } \} _ { n = 1 } ^ { \infty }$ converges more rapidly to $p = 1$ than does $\{ p _ { n } \} _ { n = 1 } ^ { \infty }$

Table 2.11   

<table><tr><td></td><td></td><td>Pn</td></tr><tr><td>n</td><td>Pn</td><td></td></tr><tr><td>1</td><td>0.54030</td><td>0.96178</td></tr><tr><td>2</td><td>0.87758</td><td>0.98213</td></tr><tr><td>3</td><td>0.94496</td><td>0.98979</td></tr><tr><td>4</td><td>0.96891</td><td>0.99342</td></tr><tr><td>5</td><td>0.98007</td><td>0.99541</td></tr><tr><td>6</td><td>0.98614</td><td></td></tr><tr><td>7</td><td>0.98981</td><td></td></tr></table>

The $\Delta$ notation associated with this technique has its origin in the following definition.

# Definition 2.12

1.12For a given sequence $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ , the forward difference $\Delta p _ { n }$ is defined by

$$
\Delta p _ { n } = p _ { n + 1 } - p _ { n } , \quad { \mathrm { f o r } } n \geq 0 .
$$

Higher powers, $\Delta ^ { k } p _ { n }$ , are defined recursively by

$$
\Delta ^ { k } p _ { n } = \Delta ( \Delta ^ { k - 1 } p _ { n } ) , \quad \mathrm { f o r } k \ge 2 .
$$

The definition implies that

$$
\Delta ^ { 2 } p _ { n } = \Delta ( p _ { n + 1 } - p _ { n } ) = \Delta p _ { n + 1 } - \Delta p _ { n } = ( p _ { n + 2 } - p _ { n + 1 } ) - ( p _ { n + 1 } - p _ { n } ) .
$$

So

$$
\Delta ^ { 2 } p _ { n } = p _ { n + 2 } - 2 p _ { n + 1 } + p _ { n } ,
$$

and the formula for ${ \hat { p } } _ { n }$ given in Eq. (2.12) can be written as

$$
\hat { p } = p _ { n } - \frac { ( \Delta p _ { n } ) ^ { 2 } } { \Delta ^ { 2 } p _ { n } } , \quad \mathrm { f o r } n \ge 0 .
$$

To this point in our discussion of Aitken's $\Delta ^ { 2 }$ method, we have stated that the sequence $\{ \hat { p } _ { n } \} _ { n = 0 } ^ { \infty }$ , converges to $p$ more rapidly than does the original sequence $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ , but we have not said what is meant by the term “more rapid" convergence. Theorem 2.13 explains and justifies this terminology. The proof of this theorem is considered in Exercise 14.

Suppose that $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ is a sequence that converges linearly to the limit $p$ and that for all sufcentlylarge values of $\pmb { n }$ we have $( p _ { n } - p ) ( p _ { n + 1 } - p ) > 0$ Then the sequence $\{ \hat { p } _ { n } \} _ { n = 0 } ^ { \infty }$ converges to $p$ faster than $\{ p _ { n } \} _ { n = 0 } ^ { \infty }$ in the sense that

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { { \hat { p } } _ { n } - p } { p _ { n } - p } } = 0 .
$$

By applying a modification of Aitken's $\Delta ^ { 2 }$ method to a linearly convergent sequence obtained from fixed-point iteration, we can accelerate the convergence to quadratic. This procedure is known as Steffensen's method and differs slightly from applying Aitken's $\Delta ^ { 2 }$ method directly to the linearly convergent fixed-point iteration sequence. Aitken's $\Delta ^ { 2 }$ method constructs the terms in order:

$$
\begin{array} { r l } & { p _ { 0 } , \quad p _ { 1 } = g ( p _ { 0 } ) , \quad p _ { 2 } = g ( p _ { 1 } ) , \quad \hat { p } _ { 0 } = \{ \Delta ^ { 2 } \} ( p _ { 0 } ) , } \\ & { p _ { 3 } = g ( p _ { 2 } ) , \quad \hat { p } _ { 1 } = \{ \Delta ^ { 2 } \} ( p _ { 1 } ) , \dots , } \end{array}
$$

where $\{ \Delta ^ { 2 } \}$ indicates that Eq. (2.13) is used. Steffensen's method constructs the same first four terms, $p _ { 0 } , p _ { 1 } , p _ { 2 }$ , and $\hat { p } _ { 0 }$ . However, at this step it assumes that $\hat { p } _ { 0 }$ is a beter approximation to $p$ than is ${ \pmb p } _ { 2 }$ and applies fixed-point iteration to $\hat { p } _ { 0 }$ instead of $p _ { 2 }$ . Using this notation the sequence generated is

$$
\begin{array} { r }    { \boldsymbol \begin{array} { l l l l l l } {  { { \boldsymbol { \eta } } } ^ { ( 0 ) } , } & {  { { \boldsymbol { p } } } _ { 1 } ^ { ( 0 ) } = g (  { { \boldsymbol { p } } } _ { 0 } ^ { ( 0 ) } ) , } & {  { { \boldsymbol { p } } } _ { 2 } ^ { ( 0 ) } = g (  { { \boldsymbol { p } } } _ { 1 } ^ { ( 0 ) } ) , } & {  { { \boldsymbol { p } } } _ { 0 } ^ { ( 1 ) } = \{ \Delta ^ { 2 } \} (  { { \boldsymbol { p } } } _ { 0 } ^ { ( 0 ) } ) , } & {  { { \boldsymbol { p } } } _ { 1 } ^ { ( 1 ) } = g (  { { \boldsymbol { p } } } _ { 0 } ^ { ( 1 ) } ) , \dots . } \end{array} } \end{array}
$$

Every third term is generated by Eq. (2.13); the others use fixed-point iteration on the previous term. The process is described in Algorithm 2.6.

![](images/909e43c49c8c823a26d0919d79b8d040559b800eb20aabdad0e2891d2947ae39.jpg)

# Steffensen's

To find a solution to $p = g ( p )$ given an initial approximation $p _ { 0 }$ ：

INPUTinitial approximation $p _ { 0 }$ ; tolerance TOL; maximum number of iterations $N _ { 0 }$

OUTPUT approximate solution $p$ or message of failure.

Step 1 Set $i = 1$

Step 2 While $i \leq N _ { 0 }$ do Steps 3-6.

$$
\begin{array} { r l } & { \dot { \boldsymbol { \mathrm {  { \cal { p } } } } } _ { 1 } = g ( p _ { 0 } ) ; \quad ( C o m p u t e ~ p _ { 1 } ^ { ( i - 1 ) } . ) } \\ & { p _ { 2 } = g ( p _ { 1 } ) ; \quad ( C o m p u t e ~ p _ { 2 } ^ { ( i - 1 ) } . ) } \\ & { p = p _ { 0 } - ( p _ { 1 } - p _ { 0 } ) ^ { 2 } / ( p _ { 2 } - 2 p _ { 1 } + p _ { 0 } ) . \quad ( C o m p u t e ~ p _ { 0 } ^ { ( i ) } . ) } \end{array}
$$

Step 4If $| p - p _ { 0 } | < T O L$ then OUTPUT $( p )$ ；  (Procedure completed successfully.) STOP.

Step 5Set $i = i + 1$

Step $\sigma$ Set $p _ { 0 } = p$ (Update po)

Step 7OUTPUT(‘Method failed after $N _ { 0 }$ iterations, $N _ { 0 } = \ ' , N _ { 0 } ,$ ； (Procedure completed unsuccessfully.) STOP.

Note that $\Delta ^ { 2 } p _ { n }$ may be O, which would introduce a O in the denominator of the next iterate. If this occurs, we terminate the sequence and select p $p _ { 2 } ^ { ( n - 1 ) }$ as the approximate answer.

To solve $x ^ { 3 } + 4 x ^ { 2 } - 1 0 = 0$ using Steffensen's method, let $x ^ { 3 } + 4 x ^ { 2 } = 1 0$ ,divide by $x + 4$ and solve for $x$ . This procedure produces the fixed-point method

$$
g ( x ) = \left( { \frac { 1 0 } { x + 4 } } \right) ^ { 1 / 2 } ,
$$

used in Example 3(d) of Section 2.2.

Steffensen's procedure with $p _ { 0 } = 1 . 5$ gives he valuesinTable2.12.Te ierate $p _ { 0 } ^ { ( 2 ) } =$ 1.365230013 is accurate to the ninth decimal place. In this example, Steffensen's method gave about the same accuracy as Newton's method (see Example 4 in Section 2.4).

Table 2.12   

<table><tr><td>k</td><td></td><td>P</td><td></td></tr><tr><td>0</td><td>1.5</td><td>1.348399725</td><td>1.367376372</td></tr><tr><td>1</td><td>1.365265224</td><td>1.365225534</td><td>1.365230583</td></tr><tr><td>2</td><td>1.365230013</td><td></td><td></td></tr></table>

From Example 2, it appears that Steffensen's method gives quadratic convergence without evaluating a derivative,and Theorem 2.14 verifies that this is the case.The proof of this theorem can be found in [He2, pp. 90-92] or [IK, pp.103-107].

# Theorem 2.14

Suppose that $x = g ( x )$ has the solution $p$ with $g ^ { \prime } ( p ) \neq 1$ . If there exists a $\delta > 0$ such that $g \in C ^ { 3 } [ p - \delta , p + \delta ] ,$ then Steffensen's method gives quadratic convergence for any $p _ { 0 } \in [ p - \delta , p + \delta ]$

# ExERCIse Set 2.5

1. The following sequences are linearly convergent. Generate the first five terms of the sequence $\{ \hat { p } _ { \pmb { n } } \}$ using Aitken's $\Delta ^ { 2 }$ method.

$$
\begin{array} { l } { { p _ { 0 } = 0 . 5 , \quad p _ { n } = ( 2 - e ^ { p _ { n - 1 } } + p _ { n - 1 } ^ { 2 } ) / 3 , \quad n \geq 1 } } \\ { { p _ { 0 } = 0 . 7 5 , \quad p _ { n } = ( e ^ { p _ { n - 1 } } / 3 ) ^ { 1 / 2 } , \quad n \geq 1 } } \\ { { p _ { 0 } = 0 . 5 , \quad p _ { n } = 3 ^ { - p _ { n - 1 } } , \quad n \geq 1 } } \\ { { p _ { 0 } = 0 . 5 , \quad p _ { n } = \cos p _ { n - 1 } , \quad n \geq 1 } } \end{array}
$$

2. Consider the function $f ( x ) = e ^ { 6 x } + 3 ( \ln 2 ) ^ { 2 } e ^ { 2 x } - ( \ln 8 ) e ^ { 4 x } - ( \ln 2 ) ^ { 3 }$ .Use Newton's method with $p _ { 0 } = 0$ to approximate a zero of $f$ . Generate terms until $| p _ { n + 1 } - p _ { n } | < 0 . 0 0 0 2$ . Construct the sequence $\{ \hat { p } _ { n } \}$ . Is the convergence improved?

Let $g ( x ) = \cos ( x - 1 )$ and $p _ { 0 } ^ { ( 0 ) } = 2$ . Use Steffensen's methodto find $p _ { 0 } ^ { ( 1 ) }$

4.Let $g ( x ) = 1 + ( \sin x ) ^ { 2 }$ and $p _ { 0 } ^ { ( 0 ) } = 1$ . Use Steffensen'smethod to find $p _ { 0 } ^ { ( 1 ) }$ and $p _ { 0 } ^ { ( 2 ) }$

5. Stefensen's method isaplied to afunction $g ( x )$ using $p _ { 0 } ^ { ( 0 ) } = 1$ = 1 and p2 $p _ { 2 } ^ { ( 0 ) } = 3$ to obtain $p _ { 0 } ^ { ( 1 ) } = 0 . 7 5$ . What is $p _ { \mathrm { 1 } } ^ { ( 0 ) } \bar { ? }$ r

6. Stefesn'sedisoc $g ( x )$ using $p _ { 0 } ^ { ( 0 ) } = 1$ and $p _ { 1 } ^ { ( 0 ) } = \sqrt { 2 }$ to obtain $p _ { 0 } ^ { ( 1 ) } = 2 . 7 8 0 2$ . What is $p _ { 2 } ^ { ( 0 ) } ?$

7. Use Steffensen's method to find, to an accuracy of $1 0 ^ { - 4 }$ , the root of $x ^ { 3 } - x - 1 = 0$ that lies in [1,2], and compare this to the results of Exercise 6 of Section 2.2.

8. Use Steffensen's method to find, to an accuracy of $1 0 ^ { - 4 }$ , the root of $x - 2 ^ { - x } = 0$ that lies in [0,1],and compare this to the results of Exercise 8 of Section 2.2.

9. Use Steffensen's method with $p _ { 0 } = 2$ to compute an approximation to $\sqrt { 3 }$ accurate to within $1 0 ^ { - 4 }$ . Compare this result with those obtained in Exercise $^ { 9 }$ of Section 2.2 and Exercise 10 of Section 2.1.

10. Use Steffensen's method to approximate the solutions of the following equations to within $1 0 ^ { - 5 }$

a. $x = ( 2 - e ^ { x } + x ^ { 2 } ) / 3$ , where $\pmb { g }$ is the function in Exercise 11(a) of Section 2.2.   
$\mathbf { b } _ { \bullet }$ $x = 0 . 5 ( \sin x + \cos x )$ ,where $\pmb { g }$ is the function in Exercise 11(f) of Section 2.2.   
$\pmb { \mathrm { c } } _ { \pmb { \mathrm { * } } }$ $3 x ^ { 2 } - e ^ { x } = 0$ ,where $\pmb { g }$ is the function in Exercise 12(a) of Section 2.2.   
d. $x - \cos x = 0$ ,where $\pmb { g }$ is the function in Exercise 12(b) of Section 2.2.

11.The following sequences converge to 0. Use Aitken's $\Delta ^ { 2 }$ method to generate $\{ \hat { p } _ { n } \}$ until $| \hat { p } _ { \mathfrak { n } } | \leq$ $5 \times 1 0 ^ { - 2 }$ ：

$\mathrm { a } . \quad p _ { n } = { \frac { 1 } { n } } , \quad n \geq 1$ ${ \textbf { \textit { b } } } _ { p _ { n } } = { \frac { 1 } { n ^ { 2 } } } , \quad n \geq 1$

12.A sequence $\{ p _ { n } \}$ is said to be superlinearly convergent to $p$ if

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { | p _ { n + 1 } - p | } { | p _ { n } - p | } } = 0 .
$$

a.Show that if $p _ { n }  p$ of order $\pmb { \alpha }$ for $\alpha > 1$ ,then $\{ p _ { n } \}$ is superlinearly convergent to $p$

b. Show that $\begin{array} { r } { p _ { n } = \frac { 1 } { n ^ { n } } } \end{array}$ is superlinearlyconvergent toObutdoesnotconvergetoOof rder $\pmb { \alpha }$ for any $\alpha > 1$

13.Suppose that $\{ p _ { n } \}$ is superlinearly convergent to $p$ . Show that

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { | p _ { n + 1 } - p _ { n } | } { | p _ { n } - p | } } = 1 .
$$

14. Prove Theorem 2.13.[Hint: Let $\delta _ { n } = ( p _ { n + 1 } - p ) / ( p _ { n } - p ) - \lambda$ , and show that $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } \delta _ { n } = 0 } \end{array}$ Then express $( \hat { p } _ { n + 1 } - p ) / ( p _ { n } - p )$ in terms of $\delta _ { n } , \delta _ { n + 1 }$ ,and $\lambda$ ]

15.Let $P _ { n } ( x )$ be the $\pmb { n }$ th Taylor polynomial for $f ( x ) = e ^ { x }$ expanded about $x _ { 0 } = 0$

a. For fixed $\pmb { x }$ , show that $p _ { n } = P _ { n } ( x )$ satisfies the hypotheses of Theorem 2.13. b. Let $x = 1$ , and use Aitken's $\Delta ^ { 2 }$ method to generate the sequence $\hat { p } _ { 0 } , \ldots , \hat { p } _ { 8 }$ · c. Does Aitken's method accelerate convergence in this situation?

# 2.6 Zeros of Polynomials and Muller's Method

A polynomial of degree n has the form

$$
P ( x ) = a _ { n } x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdot \cdot \cdot + a _ { 1 } x + a _ { 0 } ,
$$

where the $a _ { i } { \bf \dot { s } }$ , called the coefficients of $P$ , are constants and $a _ { n } \neq 0$ . The zero function, $P ( x ) = 0$ for all values of $x$ , is considered a polynomial but is assigned no degree.

# Theorem 2.15 (Fundamental Theorem of Algebra)

If $P ( x )$ is a polynomial of degree $n \geq 1$ with real or complex coefficients, then $P ( x ) = 0$ has at least one (possibly complex) root.

Although Theorem 2.15 is basic to any study of elementary functions, the usual proof requires techniques from the study of complex-function theory. The reader is referred to [SaS,p. 155], for the culmination of a systematic development of the topics needed to prove Theorem 2.15.

An important consequence of Theorem 2.15 is the following corollary.

# Corollary 2.16

If $P ( x )$ is a polynomial of degree $n \geq 1$ with real or complex coefficients,then there exist unique constants $x _ { 1 } , x _ { 2 } , \ldots , x _ { k }$ ， possibly complex, and unique positive integers $m _ { 1 } , m _ { 2 }$ ， $\dots , m _ { k }$ , such that $\textstyle \sum _ { i = 1 } ^ { k } m _ { i } = n$ and

$$
P ( x ) = a _ { n } ( x - x _ { 1 } ) ^ { m _ { 1 } } ( x - x _ { 2 } ) ^ { m _ { 2 } } \cdot \cdot \cdot ( x - x _ { k } ) ^ { m _ { k } } .
$$

Corollary 2.16 states that the collection of zeros of a polynomial is unique and that, if each zero $x _ { i }$ is counted as many times as its multiplicity $m _ { i }$ , a polynomial of degree $\pmb { n }$ has exactly $\pmb { n }$ zeros.

The following corollary of the Fundamental Theorem of Algebra is used often in this section and in later chapters.

# Corollary 2.17

Let $P ( x )$ and $Q ( x )$ be polynomials of degree at most $\pmb { n }$ .If $x _ { 1 } , x _ { 2 } , \ldots , x _ { k }$ ,with $k > n$ ,are distinct numbers with $P ( x _ { i } ) = Q ( x _ { i } )$ for $i = 1 , 2 , \dots , k$ ,then $P ( x ) = Q ( x )$ for all values of $x$

To use Newton's method to locate approximate zeros of a polynomial $P ( x )$ , we need to evaluate $P ( x )$ and $P ^ { \prime } ( x )$ at specified values. Since $P ( x )$ and $P ^ { \prime } ( x )$ are both polynomials,computational effciency requires that the evaluation of these functions be done in the nested manner discussed in Section 1.2. Horner's method incorporates this nesting technique,and, as a consequence, requires only $\pmb { n }$ multiplications and $\pmb { n }$ additions to evaluate an arbitrary nth-degree polynomial.

# Theorem 2.18 (Horner's Method)

Let

$$
P ( x ) = a _ { n } x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdots + a _ { 1 } x + a _ { 0 } .
$$

If $b _ { n } = a _ { n }$ and

$$
b _ { k } = a _ { k } + b _ { k + 1 } x _ { 0 } , \quad { \mathrm { f o r ~ } } k = n - 1 , n - 2 , \dots , 1 , 0 ,
$$

then $b _ { 0 } = P ( x _ { 0 } )$ . Moreover, if

$$
Q ( x ) = b _ { n } x ^ { n - 1 } + b _ { n - 1 } x ^ { n - 2 } + \cdot \cdot \cdot + b _ { 2 } x + b _ { 1 } ,
$$

then

$$
P ( x ) = ( x - x _ { 0 } ) Q ( x ) + b _ { 0 } .
$$

Proof By the definition of $Q ( x )$ ，

$$
\begin{array} { r l } { ( x - x _ { 0 } ) Q ( x ) + b _ { 0 } = ( x - x _ { 0 } ) ( b _ { n } x ^ { n - 1 } + \cdots + b _ { 2 } x + b _ { 1 } ) + b _ { 0 } } & { { } } \\ { = ( b _ { n } x ^ { n } + b _ { n - 1 } x ^ { n - 1 } + \cdots + b _ { 2 } x ^ { 2 } + b _ { 1 } x ) } & { { } } \\ { - ( b _ { n } x _ { 0 } x ^ { n - 1 } + \cdots + b _ { 2 } x _ { 0 } x + b _ { 1 } x _ { 0 } ) + b _ { 0 } } & { { } } \\ { = b _ { n } x ^ { n } + ( b _ { n - 1 } - b _ { n } x _ { 0 } ) x ^ { n - 1 } + \cdots + ( b _ { 1 } - b _ { 2 } x _ { 0 } ) x + ( b _ { 0 } - b _ { 1 } x _ { 0 } ) ( b _ { 0 } + b _ { 1 } x _ { 0 } ) } & { { } } \end{array}
$$

By the hypothesis, $b _ { n } = a _ { n }$ and $b _ { k } - b _ { k + 1 } x _ { 0 } = a _ { k }$ ，so

$$
( x - x _ { 0 } ) Q ( x ) + b _ { 0 } = P ( x ) \quad { \mathrm { a n d } } \quad b _ { 0 } = P ( x _ { 0 } ) .
$$

# EXAMPlE 1

Use Horner's method to evaluate $P ( x ) = 2 x ^ { 4 } - 3 x ^ { 2 } + 3 x - 4$ at $x _ { 0 } = - 2$

When we use hand calculation in Horner's method, we first construct a table, which suggests the synthetic division name often applied to the technique.For this problem, the table appears as follows:

<table><tr><td rowspan="2">xo=-2</td><td rowspan="2">Coefficient of x4 a4 = 2</td><td rowspan="2">Coefficient of x3 a=0 b4xo = -4</td><td rowspan="2">Coefficient b3xo=8</td><td rowspan="2">Coefficient of x a1=3 b2xo=-10</td><td rowspan="2">Constant term a = -4 b1xo= 14</td></tr><tr><td>of x² a2=-3</td></tr><tr><td></td><td>b4=2</td><td>b=-4</td><td>b2=5</td><td>b1=-7</td><td>bo=10</td></tr></table>

So,

$$
P ( x ) = ( x + 2 ) ( 2 x ^ { 3 } - 4 x ^ { 2 } + 5 x - 7 ) + 1 0 .
$$

An additional advantage of using the Horner (or synthetic-division) procedure is that, since

$$
P ( x ) = ( x - x _ { 0 } ) Q ( x ) + b _ { 0 } ,
$$

where

$$
Q ( x ) = b _ { n } x ^ { n - 1 } + b _ { n - 1 } x ^ { n - 2 } + \cdot \cdot \cdot + b _ { 2 } x + b _ { 1 } ,
$$

differentiating with respect to $\pmb { x }$ gives

$$
P ^ { \prime } ( x ) = Q ( x ) + ( x - x _ { 0 } ) Q ^ { \prime } ( x ) \quad { \mathrm { a n d } } \quad P ^ { \prime } ( x _ { 0 } ) = Q ( x _ { 0 } ) .
$$

When the Newton-Raphson method is being used to find an approximate zero of a polynomial, $P ( x )$ and $P ^ { \prime } ( x )$ can be evaluated in the same manner.

Find an approximation to one of the zeros of

$$
P ( x ) = 2 x ^ { 4 } - 3 x ^ { 2 } + 3 x - 4 ,
$$

using Newton's method and synthetic division to evaluate $P ( x _ { n } )$ and $P ^ { \prime } ( x _ { n } )$ for each iterate $x _ { n }$ ·

With $x _ { 0 } = - 2$ as an initial approximation, we obtained $P ( - 2 )$ in Example 1 by

$$
x _ { 0 } = - 2 \quad \left\lfloor { \begin{array} { r l r l r l r l } { ~ 2 } & { } & { ~ 0 } & { ~ - 3 } & { } & { 3 } & { ~ - 4 } & { } \\ { - 4 } & { } & { 8 } & { - 1 0 } & { } & { 1 4 } & { } \\ { 2 } & { } & { - 4 } & { } & { 5 } & { } & { - 7 } & { } & { 1 0 } & { ~ = P ( - 2 ) . } \end{array} } \right.
$$

Using Theorem 2.18 and Eq. (2.14),

$$
Q ( x ) = 2 x ^ { 3 } - 4 x ^ { 2 } + 5 x - 7 \quad { \mathrm { a n d } } \quad P ^ { \prime } ( - 2 ) = Q ( - 2 ) ,
$$

so $P ^ { \prime } ( - 2 )$ can be found by evaluating $Q ( - 2 )$ in a similar manner:

$$
\begin{array} { r l r l r l } { x _ { 0 } = - 2 } & { } & { \left\lfloor \begin{array} { c c c c } { 2 } & { - 4 } & { 5 } & { - 7 } \\ { - 4 } & { 1 6 } & { - 4 2 } \end{array} \right. } \\ { 2 } & { } & { - 8 } & { 2 1 } & { } & { - 4 9 } & { } & { = Q ( - 2 ) = P ^ { \prime } ( - 2 ) } \end{array}
$$

and

$$
x _ { 1 } = x _ { 0 } - { \frac { P ( x _ { 0 } ) } { P ^ { \prime } ( x _ { 0 } ) } } = - 2 - { \frac { 1 0 } { - 4 9 } } \approx - 1 . 7 9 6 .
$$

Repeating the procedure to find $x _ { 2 }$ ，

<table><tr><td rowspan="3">-1.796</td><td>2 0 -3.592</td><td>-3 6.451</td><td>3 -6.197</td><td>14 5.742</td></tr><tr><td>2 -3.592 -3.592</td><td>3.451 12.902</td><td>.-3.197 -29.368</td><td>1.742 = P(x1)</td></tr><tr><td>2 -7.184</td><td>16.353</td><td>-32.565</td><td>= Q(x1) = P&#x27;(x1).</td></tr></table>

So $P ( - 1 . 7 9 6 ) = 1 . 7 4 2 , P ^ { \prime } ( - 1 . 7 9 6 ) = - 3 2 . 5 6 5$ ,and

$$
x _ { 2 } = - 1 . 7 9 6 - { \frac { 1 . 7 4 2 } { - 3 2 . 5 6 5 } } \approx - 1 . 7 4 2 5 .
$$

In a similar manner, $x _ { 3 } = - 1 . 7 3 8 9 7$ ,and an actual zero to five decimal places is-1.73896.

Note that the polynomial Q(x) depends on the approximation being used and changes from iterate to iterate.

Algorithm 2.7 computes $P ( x _ { 0 } )$ and $P ^ { \prime } ( x _ { 0 } )$ using Horner's method.

# Horner's

To evaluate the polynomial

$$
P ( x ) = a _ { n } x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdot \cdot \cdot + a _ { 1 } x + a _ { 0 } = ( x - x _ { 0 } ) Q ( x ) + b _ { 0 }
$$

and its derivative at $x _ { 0 }$ ：

INPUT degree n; coeficients ao, a1,... , an; xo.

OUTPUT $y = P ( x _ { 0 } ) ; z = P ^ { \prime } ( x _ { 0 } ) .$

Step 1 Set $\begin{array} { c l } { { ; y = a _ { n } ; } } & { { ( C o m p u t e ~ b _ { n } ~ f o r ~ P . ) } } \\ { { z = a _ { n } . } } & { { ( C o m p u t e ~ b _ { n - 1 } ~ f o r ~ Q . ) } } \end{array}$

Step 2 For $j = n - 1 , n - 2 , \dots , 1$ $\begin{array} { r } { \mathrm { \bar { s e t } } y = x _ { 0 } y + a _ { j } ; ( C o m p u t e b _ { j } f o r P . ) } \\ { z = x _ { 0 } z + y . ( C o m p u t e b _ { j - 1 } f o r Q . ) } \end{array}$

Step 3 Set $y = x _ { 0 } y + a _ { 0 }$ (Compute $b _ { 0 }$ for P.)

Step 4 OUTPUT $( y , z )$ ； STOP.

If the $N$ th iterate, $x _ { N }$ ,in Newton's method is an approximate zero for $P$ , then

$$
P ( x ) = ( x - x _ { N } ) Q ( x ) + b _ { 0 } = ( x - x _ { N } ) Q ( x ) + P ( x _ { N } ) \approx ( x - x _ { N } ) Q ( x ) ,
$$

so $\boldsymbol { x } - \boldsymbol { x } _ { N }$ is an approximate factor of ${ \dot { P } } ( x )$ . Letting $\hat { x } _ { 1 } = x _ { N }$ be the approximate zero of $P$ and $Q _ { 1 } ( x ) \equiv Q ( x )$ be the approximate factor gives

$$
P ( x ) \approx ( x - \hat { x } _ { 1 } ) Q _ { 1 } ( x ) .
$$

We can find a second approximate zero of $P$ by applying Newton's method to $Q _ { 1 } ( x )$ .If $P ( x )$ is an nth-degree polynomial with $\pmb { n }$ real zeros, this procedure applied repeatedly will eventually result in $( n - 2 )$ approximate zeros of $P$ and an approximate quadratic factor $Q _ { n - 2 } ( x )$ . At this stage, $Q _ { n - 2 } ( x ) = 0$ can be solved by the quadratic formula to find the last two approximate zeros of $P$ . Although this method can be used to find allthe approximate zeros, it depends on repeated use of approximations and can lead to inaccurate results.

The procedure just described is called deflation. The accuracy difficulty with deflation is due to the fact that, when we obtain the approximate zeros of $P ( x )$ , Newton's method is used on the reduced polynomial $Q _ { k } ( x )$ , that is, the polynomial having the property that

$$
P ( x ) \approx ( x - { \hat { x } } _ { 1 } ) ( x - { \hat { x } } _ { 2 } ) \cdot \cdot \cdot ( x - { \hat { x } } _ { k } ) Q _ { k } ( x ) .
$$

An approximate zero $\hat { x } _ { k + 1 }$ of $Q _ { k }$ will generally not approximate a root of $P ( x ) = 0$ as well as it does a root of the reduced equation $Q _ { k } ( x ) = 0$ ， and inaccuracy increases as $k$ increases. One way to eliminate this difficulty is to use the reduced equations to find approximations ${ \hat { x } } _ { 2 } , { \hat { x } } _ { 3 } , \dots , { \hat { x } } _ { k }$ to the zeros of $P$ , and then improve these approximations by applying Newton's method to the original polynomial $P ( x )$

A problem with applying Newton's method to polynomials concerns the possibility of the polynomial having complex roots when all the coefficients are real numbers. If the ini-tial approximation using Newton's method is a real number, all subsequent approximations will also be real numbers. One way to overcome this difficulty is to begin with a complex initial approximation and do all the computations using complex arithmetic. An alternative approach has its basis in the following theorem.

# Theorem 2.19

If $z ~ = ~ a + b i$ is a complex zero of multiplicity $m$ of the polynomial $P ( x )$ with real coeficients, then ${ \vec { z } } = a - b i$ is also a zero of multiplicity $m$ of the polynomial $P ( x )$ ,and $( x ^ { 2 } - 2 a x + a ^ { 2 } + b ^ { 2 } ) ^ { m }$ is a factor of $P ( x )$ ■

A synthetic division involving quadratic polynomials can be devised to approximately factor the polynomial so that one term will be a quadratic polynomial whose complex roots are approximations to the roots of the original polynomial. This technique was described in some detail in our second edition [BFR]. Instead of proceeding along these lines, we will now consider a method first presented by D. E. Muller [Mu]. This technique can be used for any root-finding problem, but it is particularly useful for approximating the roots of polynomials.

Muller's method is an extension of the Secant method. The Secant method begins with two initial approximations $x _ { 0 }$ and $x _ { 1 }$ and determines the next approximation $x _ { 2 }$ as the intersection of the $x$ -axis with the line through $( x _ { 0 } , f ( x _ { 0 } ) )$ and $( x _ { 1 } , f ( x _ { 1 } ) )$ . (See Figure 2.12(a).) Muller's method uses three initial approximations, $x _ { 0 } , x _ { 1 }$ ,and $x _ { 2 }$ , and determines the next approximation $x _ { 3 }$ by considering the intersection of the $x$ -axis with the parabola through $( x _ { 0 } , f ( x _ { 0 } ) )$ ， $( x _ { 1 } , f ( x _ { 1 } ) )$ ,and $( x _ { 2 } , f ( x _ { 2 } ) )$ . (See Figure 2.12(b).)

![](images/649174aac2ce80c19d3f4797be77b7c405e21598b4dc259170d74905730aec2f.jpg)  
Figure 2.12

The derivation of Muller's method begins by considering the quadratic polynomial

$$
P ( x ) = a ( x - x _ { 2 } ) ^ { 2 } + b ( x - x _ { 2 } ) + c
$$

that passes through $( x _ { 0 } , f ( x _ { 0 } ) )$ ， $( x _ { 1 } , f ( x _ { 1 } ) )$ ,and $( x _ { 2 } , f ( x _ { 2 } ) )$ . The constants $a , b ,$ ,and $c$ can be determined from the conditions

$$
\begin{array} { c } { f ( x _ { 0 } ) = a ( x _ { 0 } - x _ { 2 } ) ^ { 2 } + b ( x _ { 0 } - x _ { 2 } ) + c , } \\ { f ( x _ { 1 } ) = a ( x _ { 1 } - x _ { 2 } ) ^ { 2 } + b ( x _ { 1 } - x _ { 2 } ) + c , } \end{array}
$$

and

$$
f ( x _ { 2 } ) = a \cdot 0 ^ { 2 } + b \cdot 0 + c = c
$$

to be

$$
\begin{array} { l } { c = f ( x _ { 2 } ) , } \\ { b = \frac { ( x _ { 0 } - x _ { 2 } ) ^ { 2 } [ f ( x _ { 1 } ) - f ( x _ { 2 } ) ] - ( x _ { 1 } - x _ { 2 } ) ^ { 2 } [ f ( x _ { 0 } ) - f ( x _ { 2 } ) ] } { ( x _ { 0 } - x _ { 2 } ) ( x _ { 1 } - x _ { 2 } ) ( x _ { 0 } - x _ { 1 } ) } , } \end{array}
$$

and

$$
a = { \frac { ( x _ { 1 } - x _ { 2 } ) [ f ( x _ { 0 } ) - f ( x _ { 2 } ) ] - ( x _ { 0 } - x _ { 2 } ) [ f ( x _ { 1 } ) - f ( x _ { 2 } ) ] } { ( x _ { 0 } - x _ { 2 } ) ( x _ { 1 } - x _ { 2 } ) ( x _ { 0 } - x _ { 1 } ) } } .
$$

To determine $\pmb { x _ { 3 } }$ , a zero of $P$ ， we apply the quadratic formula to $P ( x ) = 0$ . However, because of roundoff error problems caused by the subtraction of nearly equal numbers, we apply the formula in the manner prescribed in Example 5 of Section 1.2:

$$
x _ { 3 } - x _ { 2 } = \frac { - 2 c } { b \pm \sqrt { b ^ { 2 } - 4 a c } } .
$$

This formula gives two possibilities for $x _ { 3 }$ ， depending on the sign preceding the radical term. In Muller's method, the sign is chosen to agree with the sign of $b$ . Chosen in this manner, the denominator will be the largest in magnitude and will result in $x _ { 3 }$ being selected as the closest zero of $P$ to $x _ { 2 }$ . Thus,

$$
x _ { 3 } = x _ { 2 } - \frac { 2 c } { b + \mathrm { s g n } ( b ) \sqrt { b ^ { 2 } - 4 a c } } ,
$$

where $a , b$ ,and $\pmb { c }$ are given in Eq. (2.15).

Once $x _ { 3 }$ is determined, the procedure is reinitialized using $x _ { 1 } , x _ { 2 }$ ,and $x _ { 3 }$ in place of $x _ { 0 } , x _ { 1 }$ ,and $x _ { 2 }$ to determine the next approximation, $x _ { 4 }$ . The method continues until a sat-isfactory conclusion is obtained. At each step,the method involves the radical ${ \sqrt { b ^ { 2 } - 4 a c } } ,$ so the method gives approximate complex roots when $b ^ { 2 } - 4 a c < 0$ Algorithm 2.8 implements this procedure.

# Muller's

To find a solution to $f ( x ) = 0$ given three approximations, $x _ { 0 } , x _ { 1 }$ ,and $x _ { 2 }$ ：

INPUT $x _ { 0 } , x _ { 1 } , x _ { 2 }$ ; tolerance $T O L$ ; maximum number of iterations $N _ { 0 }$

OUTPUT approximate solution $p$ or message of failure.

Step 1 Set $\begin{array} { r l } & { \mathrm { \Delta } h _ { 1 } = x _ { 1 } - x _ { 0 } ; } \\ & { \quad h _ { 2 } = x _ { 2 } - x _ { 1 } ; } \\ & { \quad \delta _ { 1 } = ( f ( x _ { 1 } ) - f ( x _ { 0 } ) ) / h _ { 1 } ; } \\ & { \quad \delta _ { 2 } = ( f ( x _ { 2 } ) - f ( x _ { 1 } ) ) / h _ { 2 } ; } \\ & { \quad d = ( \delta _ { 2 } - \delta _ { 1 } ) / ( h _ { 2 } + h _ { 1 } ) ; } \\ & { \quad i = 3 . } \end{array}$

Step 2 While $i \leq N _ { 0 }$ do Steps 3-7.

Step 3 $b = \delta _ { 2 } + h _ { 2 } d$ ； $D = ( b ^ { 2 } - 4 f ( x _ { 2 } ) d ) ^ { 1 / 2 }$ . (Note: May require complex arithmetic.)

Step 4 If $| b - D | < | b + D |$ then set $E = b + D$ else set $E = b - D$

Step 5Set $\begin{array} { l } { h = - 2 f ( x _ { 2 } ) / E ; } \\ { p = x _ { 2 } + h . } \end{array}$

$$
\begin{array} { r l } &  \mathrm  \ \ i \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \it \lambda \mathrm  \lambda \it { 1 } \cdot \mathrm  \lambda \it { 1 } \cdot \mathrm \it { 1 } \cdot \it \lambda \mathrm  \lambda \it { 1 } \cdot \mathrm \it { 1 } \cdot \mathrm \it  \lambda \it { 1 } \cdot \mathrm \it { 1 } \cdot \mathrm \it  \lambda \it { 1 } \cdot \mathrm \it { 1 } \cdot \mathrm \it  \lambda \it \cdot \mathrm  \lambda \it \Omega \it { 1 } \cdot \mathrm \it { 1 } \cdot \mathrm \it { 1 } \cdot \mathrm \it  \lambda \it \lambda \mathrm  \it \lambda \it { 1 } \cdot \mathrm \it { 1 } \cdot \mathrm \it \lambda \it  \lambda \it \cdot \mathrm \Omega \it { 1 } \cdot \mathrm \lambda \it  \lambda \mathrm { 1 } \cdot \mathrm \it \lambda \it { 1 } \cdot \mathrm \it \lambda \mathrm  \lambda \it \lambda \it { 1 } \cdot \mathrm \it \lambda \mathrm  \lambda \it \lambda \it { 1 } \cdot \mathrm \Omega \it { 1 } \cdot \mathrm \lambda \it  1 \cdot \mathrm \Omega \it { 1 } \cdot \mathrm \lambda \it \lambda \mathrm  \lambda \it \lambda \mathrm  \delta \it \lambda \it { 1 } \cdot \mathrm \lambda \mathrm  \delta \it \lambda \it \lambda \mathrm { 1 } \cdot \mathrm \Omega \it { 1 } \cdot \mathrm \lambda \mathrm  \delta \it \lambda \it \lambda \mathrm  \delta \lambda \it \lambda \mathrm { 1 } \cdot \mathrm \Omega \lambda \mathrm  \delta \it \lambda \it \lambda \mathrm { 1 } \cdot \mathrm \Omega \lambda \mathrm  \delta \it \lambda \delta \it \lambda \mathrm { 1 } \cdot \mathrm \Omega \lambda \mathrm  \delta \it \lambda \delta \it \lambda \mathrm { 1 } \cdot \mathrm \Omega \lambda \mathrm  \delta \it \lambda \delta \it \lambda \mathrm { 1 } \cdot \mathrm \Omega \lambda \mathrm  \delta \it \lambda \delta \it \lambda \mathrm  \end{array}
$$

$$
\begin{array} { l } { { \delta _ { 2 } = ( f ( x _ { 2 } ) - f ( x _ { 1 } ) ) / h _ { 2 } ; } } \\ { { d = ( \delta _ { 2 } - \delta _ { 1 } ) / ( h _ { 2 } + h _ { 1 } ) ; } } \\ { { i = i + 1 . } } \end{array}
$$

# Step 8OUTPUT('Method failed after $N _ { 0 }$ iterations, $N _ { 0 } = \ ' , N _ { 0 }$ ； (The procedure was unsuccessful.) STOP.

# EXAMPLE 3

Consider the polynomial $f ( x ) = 1 6 x ^ { 4 } - 4 0 x ^ { 3 } + 5 x ^ { 2 } + 2 0 x + 6$ Using Algorithm 2.8 with $T O L = 1 0 ^ { - 5 }$ and different values of $x _ { 0 } , x _ { 1 }$ ,and $\pmb { x } _ { 2 }$ produces the results in Table 2.13.

Table 2.13   
a.   

<table><tr><td>i</td><td>xo = 0.5, x=-0.5,x=0 f(xi) X</td></tr><tr><td>3 -0.555556 + 0.598352i</td><td>-29.4007 - 3.89872i</td></tr><tr><td>-0.435450+ 0.102101i 4</td><td>1.33223- 1.19309i</td></tr><tr><td>5</td><td>-0.390631 + 0.141852i 0.375057 - 0.670164i</td></tr><tr><td>6</td><td>-0.357699 + 0.169926i -0.146746 - 0.00744629i</td></tr><tr><td>-0.356051 + 0.162856i 7</td><td>-0.183868 × 10-² + 0.539780 × 10-3i 0.286102 × 10-5 + 0.953674× 10-6i</td></tr><tr><td>8</td><td>-0.356062 + 0.162758i</td></tr></table>

b.   

<table><tr><td>x = 0.5, i</td><td>x1 = 1.0, x2 = 1.5 f(xi) Xi</td></tr><tr><td>3</td><td>1.28785 -1.37624</td></tr><tr><td>4</td><td>1.23746 0.126941</td></tr><tr><td>5</td><td>1.24160 0.219440 × 10-2</td></tr><tr><td>6</td><td>1.24168 0.257492 × 10-4</td></tr><tr><td>7</td><td>1.24168 0.257492 × 10-4</td></tr></table>

c.

<table><tr><td>x= 2.5, i Xi</td><td>x1 = 2.0, x2 = 2.25 f(xi）</td></tr><tr><td>3</td><td>1.96059 -0.611255</td></tr><tr><td>4</td><td>1.97056 0.748825 × 10-2</td></tr><tr><td>5</td><td>1.97044 -0.295639 × 10-4</td></tr><tr><td>6</td><td>1.97044 -0.259639 × 10-4</td></tr></table>

We used Maple to generate part (c) in Table 2.13.To do this, we defined $f ( x )$ and the initial approximations by

>f:=x->16\*x^4-40\*x^3+5\*x^2+20\*x+6; ${ \bf > p 0 : = 0 . 5 ; p 1 : = - 0 . 5 ; p 2 : = 0 . 0 ; }$

We evaluated the polynomial at the initial values

$$
> \mathbf { f } \odot : = \mathbf { f } \left( \mathbf { p } 0 \right) ; \mathbf { f } \mathbf { \mathtt { l } } : = \mathbf { f } \left( \mathbf { p } \mathbf { 1 } \right) ; \mathbf { f } \mathbf { 2 } : = \mathbf { f } \left( \mathbf { p } \mathbf { 2 } \right) ;
$$

and computed $c = 6 , b = 1 0 , a = 9$ ,and $p _ { 3 } = - 0 . 5 5 5 5 5 5 5 5 5 8 + 0 . 5 9 8 3 5 1 6 4 5 2 i$ using the Muller's method formulas:

${ \tt > c : = f 2 }$ ； $\begin{array} { r l } & { \mathrm { > b : \ = ( ( p 0 { - } p 2 ) \widetilde { \gamma } 2 { * } ( \tt f 1 { - } f 2 ) - ( p 1 { - } p 2 ) \widetilde { \gamma } 2 { * } ( \tt f 0 { - } f 2 ) } ) / ( ( \tt p 0 { - } p 2 ) * ( \tt p 1 { - } p 2 ) * ( \tt p 0 { - } p 0 ) \widetilde { \gamma } 2 { * } ( \tt p 0 { - } f 2 ) } \\ & { \mathrm { > a : \ = ( \tt ( p 1 { - } p 2 ) * ( \tt f 0 { - } f 2 ) - ( p 0 { - } p 2 ) * ( \tt f 1 { - } f 2 ) } ) / ( ( \tt p 0 { - } p 2 ) * ( \tt p 1 { - } p 2 ) * ( \tt p 0 { - } p 1 ) ) \log ( \tt p 1 { - } p 2 ) } \\ & { \mathrm { > p 3 : \ = p 2 - ( 2 * c ) / \left( b + ( b / a b s ( b ) ) * g q r t ( b \widetilde { \gamma } 2 { - } 4 * a * c ) \right) } ; } \end{array}$ p1));

The value $p _ { 3 }$ was generated using complex arithmetic, as is the calculation which gives $f _ { 3 } = - 2 9 . 4 0 0 7 0 1 1 2 - 3 . 8 9 8 7 2 4 7 3 8 i .$

The actual values for the roots of the equation are 1.241677,1.970446,and -0.356062 $\pm 0 . 1 6 2 7 5 8 i$ ，which demonstrates the accuracy of the approximations from Muiller's method.

Example 3 illustrates that Muller's method can approximate the roots of polynomials with a variety of starting values.In fact,Muller's method generally converges to the root of a polynomial for any initial approximation choice, although problems can be con-structed for which convergence will not occur. For example, suppose that for some i we have $f ( x _ { i } ) = f ( x _ { i + 1 } ) = f ( x _ { i + 2 } ) \neq 0$ . The quadratic equation then reduces to a nonzero constant function and never intersects the $\pmb { x }$ -axis. This is not usually the case, however, and general-purpose software packages using Muller's method request only one initial approximation per root and will even supply this approximation as an option.

# ExErcise Set 2.6

1．Find the approximations to within $1 0 ^ { - 4 }$ to all the real zeros of the following polynomials using Newton's method.

$$
\begin{array} { l } { f ( x ) = x ^ { 3 } - 2 x ^ { 2 } - 5 } \\ { f ( x ) = x ^ { 3 } + 3 x ^ { 2 } - 1 } \\ { f ( x ) = x ^ { 3 } - x - 1 } \\ { f ( x ) = x ^ { 4 } + 2 x ^ { 2 } - x - 3 } \\ { f ( x ) = x ^ { 3 } + 4 . 0 0 1 x ^ { 2 } + 4 . 0 0 2 x + 1 . 1 0 1 } \\ { f ( x ) = x ^ { 5 } - x ^ { 4 } + 2 x ^ { 3 } - 3 x ^ { 2 } + x - 4 } \end{array}
$$

2. Find approximations to within $1 0 ^ { - 5 }$ to all the zeros of each of the following polynomials by first finding the real zeros using Newton's method and then reducing to polynomials of lower degree to determine any complex zeros.

$$
f ( x ) = x ^ { 4 } + 5 x ^ { 3 } - 9 x ^ { 2 } - 8 5 x - 1 3 6
$$

$$
\begin{array} { r l } & { \mathrm { \Delta } j \mathrm { \Delta } x \mathrm { ~ - } x \mathrm { ~ - } x \mathrm { ~ } 2 x \mathrm { ~ - } y \mathrm { \Delta } x \mathrm { ~ - } \mathrm { ~ } 0 . 3 x \mathrm { ~ - } x \mathrm { ~ } 1 . 9 0 } \\ & { f ( x ) = x ^ { 4 } - 2 x ^ { 3 } - 1 2 x ^ { 2 } + 1 6 x - 4 0 } \\ & { f ( x ) = x ^ { 4 } + x ^ { 3 } + 3 x ^ { 2 } + 2 x + 2 } \\ & { f ( x ) = x ^ { 5 } + 1 1 x ^ { 4 } - 2 1 x ^ { 3 } - 1 0 x ^ { 2 } - 2 1 x - 5 } \\ & { f ( x ) = 1 6 x ^ { 4 } + 8 8 x ^ { 3 } + 1 5 9 x ^ { 2 } + 7 6 x - 2 4 0 } \\ & { f ( x ) = x ^ { 4 } - 4 x ^ { 2 } - 3 x + 5 } \\ & { f ( x ) = x ^ { 4 } - 2 x ^ { 3 } - 4 x ^ { 2 } + 4 x + 4 } \\ & { f ( x ) = x ^ { 3 } - 7 x ^ { 2 } + 1 4 x - 6 } \end{array}
$$

3.Repeat Exercise 1 using Muller's method.

4.Repeat Exercise 2 using Muller's method.

5.Use Newton’s method to find, within $1 0 ^ { - 3 }$ ,the zeros and critical points of thefollowing functions. Use this information to sketch the graph of $f$

a. $f ( x ) = x ^ { 3 } - 9 x ^ { 2 } + 1 2$ $\begin{array} { r l } { \mathbf { b } . \ } & { { } f ( x ) = x ^ { 4 } - 2 x ^ { 3 } - 5 x ^ { 2 } + 1 2 x - 5 } \end{array}$

6. $f ( x ) = 1 0 x ^ { 3 } - 8 . 3 x ^ { 2 } + 2 . 2 9 5 x - 0 . 2 1 1 4 1 = 0$ has a root at $\pmb { x = 0 . 2 9 }$ . Use Newton's method with an initial approximation ${ x _ { 0 } = 0 . 2 8 }$ to attempt tofind thisrot.Explain what happens.

7.Use Maple to find the exact roots of the polynomial $f ( x ) = x ^ { 3 } + 4 x - 4 .$

8.Use Maple to find the exact roots of the polynomial $f ( x ) = x ^ { 3 } - 2 x - 5$

9.Use each of the following methods to find a solution in [0.1,1] accurate to within $1 0 ^ { - 4 }$ for

$$
6 0 0 x ^ { 4 } - 5 5 0 x ^ { 3 } + 2 0 0 x ^ { 2 } - 2 0 x - 1 = 0 .
$$

a. Bisection method b. Newton's method c. Secant method d.method of False Position e. Muller's method

10. Two ladders crisscross an alley of width W.Each ladder reaches from the base of one wal tc some point on the opposite wall. The ladders cross at a height $\pmb { H }$ above the pavement. Find W given that the lengths of the ladders are $x _ { 1 } = 2 0$ ft and $x _ { 2 } = 3 0 \mathrm { \ f \ }$ ,and that $H = 8$ ft.

![](images/7abcb80fdd7e9fcfd82fe78d7124abf4ecf625161f9e6f40ac7019129140b41b.jpg)

11. A can in the shape of a right circular cylinder is to be constructed to contain $1 0 0 0 ~ \mathrm { c m } ^ { 3 }$ . The circular top and bottom of the can must have a radius of $\pm 0 . 2 5 \mathrm { c m }$ more than the radius of the can so that the excess can be used to form a seal with the side. The sheet of material being formed into the side of the can must also be $\mathbf { 0 . 2 5 \ c m }$ longer than the circumference of the can so that a seal can be formed. Find, to within $1 0 ^ { - 4 }$ , the minimal amount of material needed to construct the can.

![](images/74eeb042673748381db0a293e7636b4a4a2bc3344e2b3d763c5a9ccd58c025e2.jpg)

12. In 1224,Leonardo of Pisa, better known as Fibonacci, answered a mathematical challenge of John of Palermo in the presence of Emperor Frederick I: find a root of the equation x³ + 2x² + 10x = 20.He first showed that the equation had no rational roots and no Euclidean irrational root—that is,no root in any of the forms a±√b,√a±√b,√a±√b,or√√a ± √b,where a and b are rational numbers.He then approximated the only real root, probably using an algebraic technique of Omar Khayyam involving the intersection of a circle and a parabola. His answer was given in the base-60 number system as

$$
1 + 2 2 \left( { \frac { 1 } { 6 0 } } \right) + 7 \left( { \frac { 1 } { 6 0 } } \right) ^ { 2 } + 4 2 \left( { \frac { 1 } { 6 0 } } \right) ^ { 3 } + 3 3 \left( { \frac { 1 } { 6 0 } } \right) ^ { 4 } + 4 \left( { \frac { 1 } { 6 0 } } \right) ^ { 5 } + 4 0 \left( { \frac { 1 } { 6 0 } } \right) ^ { 6 } .
$$

How accurate was his approximation?

# 2.7 Survey of Methods and Software

In this chapter we have considered the problem of solving the equation f(x） = O,where f is a given continuous function. All the methods begin with an initial approximation and generate a sequence that converges to a root of the equation, if the method is successful. If [a,b] is an interval on which f(a) and f(b) are of opposite sign,then the Bisection method and the method of False Position will converge. However, the convergence of these methods may be slow. Faster convergence is generally obtained using the Secant method or Newton's method. Good initial approximations are required for these methods, two for the Secant method and one for Newton's method, so the Bisection or the False Position method can be used as starter methods for the Secant or Newton's method.

Muller's method will give rapid convergence without a particularly good initial ap-proximation. It is not quite as effcient as Newton's method; its order of convergence near a root is approximately α = 1.84,compared to the quadratic,α = 2, order of Newton's method.However, it is better than the Secant method, whose order is approximately α = 1.62,and it has the added advantage of being able to approximate complex roots.

Deflation is generally used with Muller's method once an approximate root of a polynomial has been determined. After an approximation to the root of the deflated equation has been determined,use either Muler's method or Newton's method in the original polynomial with this root as the initial approximation. This procedure will ensure that the root being approximated is a solution to the true equation, not to the deflated equation. We recommended Muller's method for finding all the zeros of polynomials, real or complex. Muller's method can also be used for an arbitrary continuous function.

Other high-order methods are available for determining the roots of polynomials. If this topic is of particular interest, we recommend that consideration be given to Laguerre's method, which gives cubic convergence and also approximates complex roots (see [Ho, pp.176-179] for a complete discussion), the Jenkins-Traub method (see [JT]), and Brent's method (see [Bre]).

Another method of interest, Cauchy's method,is similar to Muller's method but avoids the failure problem of Muller's method when $f ( x _ { i } ) = f ( x _ { i + 1 } ) = f ( x _ { i + 2 } )$ , for some i. For an interesting discussion of this method,as well as more detail on Muller's method,we recommend [YG, Sections 4.10, 4.11, and 5.4].

Given a specified function $f$ and a tolerance, an efficient program should produce an approximation to one or more solutions of $f ( x ) = 0$ ,each having an absolute or relative error within the tolerance,and the results should be generated in a reasonable amount of time. If the program cannot accomplish this task, it should at least give meaningful explanations of why success was not obtained and an indication of how to remedy the cause of failure.

The IMSL FORTRAN subroutine ZANLY uses Muller's method with deflation to approximate a number of roots of $f ( x ) = 0$ . The routine ZBREN,due to R.P. Brent, uses a combination of linear interpolation, an inverse quadratic interpolation similar to Muller's method,and the Bisection method. It requires specifying an interval $[ a , b ]$ that contains a root. The IMSL C routine f_zeros_fcn and FORTRAN routine ZREAL are based on a variation of Muller's method and approximate zeros of a real function $f$ when only poor initial approximations are available. Routines for finding zeros of polynomials are the C routine f_zeros-poly and FORTRAN routine ZPORC, which uses the Jenkins-Traub method for finding zeros of a real polynomial; ZPLRC, which uses Laguerre's method to find zeros of a real polynomial; and the C routine c_zeros-poly and FORTRAN routine ZPOCC,which use the Jenkins-Traub method to find zeros of a complex polynomial.

The NAG C subroutine c05adc and the NAG FORTRAN subroutines CO5ADF and C05AZF use a combination of the Bisection method, linear interpolation,and extrapolation to approximate a real zero of $f ( x ) = 0$ in the interval $[ a , b ]$ . The subroutine C05AGF is similar to CO5ADF but requires a single starting value instead of an interval and returns an interval containing a root on its own. The NAG FORTRAN subroutines CO5AJF and C05AXF use a continuation method with a Secant iteration to approximate the real zero of a function. Also,NAG supplies subroutines C02AGF and C02AFF to approximate all zeros of a real polynomial or complex polynomial, respectively. Both subroutines use a modified Laguerre method to find the roots of a polynomial.

The netlib FORTRAN subroutine fzero.f uses a combination of the Bisection and Secant method developed by T. J. Dekker to approximate a real zero of $f ( x ) = 0$ in the interval $[ a , b ]$ . It requires specifying an interval $[ a , b ]$ that contains a root and returns an interval with a width that is within a specified tolerance.The FORTRAN subroutine sdzro.f uses a combination of the bisection method, interpolation,and extrapolation to find a real zero of $f ( x ) = 0$ in a given interval $\{ a , b \}$ . The routines rpzero and cpzero can be used to approximate all zeros of a real polynomial or complex polynomial, respectively. Both methods use Newton's method for systems,which will be considered in Chapter 10. All routines are given in single and double precision. These methods are available on the Internet from netlib at http://www.netlib.org/slatec/src.

Within MATLAB,the function ROOTS is used to compute all the roots, both real and complex, of a polynomial. For an arbitrary function, FZERO computes a root near a specified initial approximation to within a specified tolerance.

Maple has the procedure fsolve to find roots of equations. For example, returns the numbers -.6180339887 and 1.618033989. You can also specify a particular variable and interval to search. For example,

$$
> \mathrm { f } \tt { s o l v e } ( \tt { x } ^ { \hat { \mathrm { ~ * ~ } } 2 \mathrm { ~ - ~ } \tt { x } ^ { \mathrm { ~ - ~ } } 1 , \tt { x } , 1 . . 2 ) } ;
$$

returns only the number 1.618033989. The command fsolve uses a variety of specialized techniques that depend on the particular form of the equation or system of equations.

Notice that in spite of the diversity of methods,the professionally written packages are based primarily on the methods and principles discussed in this chapter. You should be able to use these packages by reading the manuals accompanying the packages to better understand the parameters and the specifications of the results that are obtained.

There are three books that we consider to be classics on the solution of nonlinear equations, those by Traub [Trl], by Ostrowski [Os],and by Householder [Ho]. In addition, the book by Brent [Bre] served as the basis for many of the currently used root-finding methods.

CHAPTER

# B

# Interpolation and Polynomial Approximation

A census of the population of the United States is taken every 10 years. The following table lists the population, in thousands of people, from 1940 to 1990.

<table><tr><td rowspan=3 colspan=1>Year</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=2 colspan=1>1940</td><td rowspan=2 colspan=1>1950</td><td rowspan=2 colspan=1>1960</td><td rowspan=2 colspan=1>1970</td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>1980</td><td rowspan=1 colspan=1>1990</td></tr><tr><td rowspan=1 colspan=1>Population(in thousands)</td><td rowspan=1 colspan=1>132,165</td><td rowspan=1 colspan=1>151,326</td><td rowspan=1 colspan=1>179,323</td><td rowspan=1 colspan=1>203.302</td><td rowspan=1 colspan=1>226,542</td><td rowspan=1 colspan=1>249,633</td></tr></table>

![](images/e77e647b51bba7350e5a7ad94e35085613fd4625aee986437bed8b034375fdbf.jpg)

In reviewing these data, we might ask whether they could be used to provide a reasonable estimate of the population, say, in 1965 or even in the year 2010. Predictions of this type can be obtained by using a func-tion that fits the given data. This process is called interpolation and is the subject of this chapter. This population problem is considered throughout the chapter and in Exercises 24 of Section 3.1, 14 of Section 3.2, and 24 of Section 3.4.

![](images/19382f32c414876805ebbeb11223962074da15aff62e32a25818eaa1e22047c2.jpg)  
Figure 3.1

One of the most useful and well-known classes of functions mapping the set of real numbers into itself is the class of algebraic polynomials,the set of functions of the form

$$
P _ { n } ( x ) = a _ { n } x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdots + a _ { 1 } x + a _ { 0 } ,
$$

where $\pmb { n }$ is a nonnegative integer and $a _ { 0 } , \ldots , a _ { n }$ are real constants. One reason for their importance is that they uniformly approximate continuous functions. Given any function, defined and continuous on a closed and bounded interval, there exists a polynomial that is as “close” to the given function as desired. This result is expressed precisely in the following theorem. (See Figure 3.1.)

![](images/f1d0cef59356aecdb801f8b0cf60470097fbb8141db9a68eae7ddc74311efeb8.jpg)

# Theorem 3.1

# (Weierstrass Approximation Theorem)

Suppose that $f$ is defined and continuous on $[ a , b ]$ . For each $\epsilon > 0$ , there exists a polynomial $P ( x )$ , with the property that

$$
| f ( x ) - P ( x ) \} < \epsilon , \quad { \mathrm { f o r ~ a l l ~ } } x \ { \mathrm { i n } } [ a , b ] .
$$

The proof of this theorem can be found in most elementary texts on real analysis (see, for example,[Bart, pp. 165-172]).

Another important reason for considering the class of polynomials in the approximationof functions is that the derivative and indefinite integral of a polynomial are easy to determine and are also polynomials. For these reasons, polynomials are often used for approximating continuous functions.

The Taylor polynomials were introduced in the first section of the book, where they were described as one of the fundamental building blocks of numerical analysis. Given this prominence, you might assume that polynomial interpolation would make heavy use of these functions.However, this is not the case. The Taylor polynomials agree as closely as possible with a given function at a specific point, but they concentrate their accuracy near that point. A good interpolation polynomial needs to provide a relatively accurate approximation over an entire interval, and Taylor polynomials do not generally do this. For example,suppose we calculate the first six Taylor polynomials about $x _ { 0 } = 0$ for $f ( x ) = e ^ { x }$ Since the derivatives of $f ( x )$ are all $e ^ { x }$ ，which evaluated at $x _ { 0 } = 0$ gives 1,the Taylor polynomials are

$$
\begin{array} { l } { { = 1 , \quad P _ { 1 } ( x ) = 1 + x , \quad P _ { 2 } ( x ) = 1 + x + { \frac { x ^ { 2 } } { 2 } } , \quad P _ { 3 } ( x ) = 1 + x + { \frac { x ^ { 2 } } { 2 } } + { \frac { x ^ { 3 } } { 6 } } , } } \\ { { \mathrm { } } } \\ { { = 1 + x + { \frac { x ^ { 2 } } { 2 } } + { \frac { x ^ { 3 } } { 6 } } + { \frac { x ^ { 4 } } { 2 4 } } , \quad \mathrm { a n d } \quad P _ { 5 } ( x ) = 1 + x + { \frac { x ^ { 2 } } { 2 } } + { \frac { x ^ { 3 } } { 6 } } + { \frac { x ^ { 4 } } { 2 4 } } + { \frac { x ^ { 5 } } { 1 2 0 } } . } } \end{array}
$$

The graphs of the polynomials are shown in Figure 3.2. (Notice that even for the higher-degree polynomials, the error becomes progressively worse as we move away from zero.)

![](images/4b632d53776eda74a81e7da3975e5704eb45f6846efadf472f9c78b64d2153c0.jpg)  
Figure 3.2

Although better approximations are obtained for $f ( x ) = e ^ { x }$ if higher-degree Taylor polynomials are used, this is not true for all functions.Consider, as an extreme example,

using Taylor polynomials of various degrees for $f ( x ) = 1 / x$ expanded about $x _ { 0 } = 1$ to approximate $\begin{array} { r } { \bar { f } ( 3 ) = \frac { 1 } { 3 } } \end{array}$ . Since

$$
f ( x ) = x ^ { - 1 } , \ f ^ { \prime } ( x ) = - x ^ { - 2 } , \ f ^ { \prime \prime } ( x ) = ( - 1 ) ^ { 2 } 2 \cdot x ^ { - 3 } ,
$$

and, in general,

$$
f ^ { ( k ) } ( x ) = ( - 1 ) ^ { k } k ! x ^ { - k - 1 } ,
$$

the Taylor polynomials are

$$
P _ { n } ( x ) = \sum _ { k = 0 } ^ { n } \frac { f ^ { ( k ) } ( 1 ) } { k ! } ( x - 1 ) ^ { k } = \sum _ { k = 0 } ^ { n } ( - 1 ) ^ { k } ( x - 1 ) ^ { k } .
$$

To approximate $f ( 3 ) = { \begin{array} { l } { { \frac { 1 } { 3 } } } \end{array} }$ by $P _ { n } ( 3 )$ for increasing values of $n$ ，we obtain the values in Table 3.1—rather a dramatic failure!

$$
{ \frac { n } { P _ { n } ( 3 ) } } \quad { \left| \begin{array} { l l l l l l l l l l l l l l l } { ~ 0 } & { \ } & { 1 } & { \ } & { 1 } & { \ 2 } & { \ } & { 3 } & { \ } & { 4 } & { \ } & { 5 } & { \ } & { 6 } & { \ } & { 7 } & { } \\ { ~ 1 } & { \ } & { \ } & { - 1 } & { \ } & { 3 } & { \ } & { - 5 } & { \ } & { 1 1 } & { \ } & { - 2 1 } & { \ } & { 4 3 } & { \ } & { - 8 5 } & { \ } \end{array} \right| } { \left| \begin{array} { l l l l l l l l l l l l l l l l l l l l l l l l } \ \right|} \end{array}  
$$

Since the Taylor polynomials have the property that all the information used in the approximation is concentrated at the single point $x _ { 0 }$ , the type of difficulty that occurs here is quite common and limits Taylor polynomial approximation to the situation in which approximations are needed only at points close to $x _ { 0 }$ . For ordinary computational purposes it is more efficient to use methods that include information at various points, which we consider in the remainder of this chapter. The primary use of Taylor polynomials in numerical analysis is not for approximation purposes but for the derivation of numerical techniques and error estimation.

# 3.1 Interpolation and the Lagrange Polynomial

Since the Taylor polynomials are not appropriate for interpolation, alternative methods are needed. In this section we find approximating polynomials that are determined simply by specifying certain points on the plane through which they must pass.

The problem of determining a polynomial of degree one that passes through the distinct points $( x _ { 0 } , y _ { 0 } )$ and $( x _ { 1 } , y _ { 1 } )$ is the same as approximating a function $f$ for which $f ( x _ { 0 } ) = y _ { 0 }$ and $f ( x _ { 1 } ) = y _ { 1 }$ by means of a first-degree polynomial interpolating, or agreeing with, the values of $f$ at the given points. We first define the functions

$$
L _ { 0 } ( x ) = { \frac { x - x _ { 1 } } { x _ { 0 } - x _ { 1 } } } \quad { \mathrm { a n d } } \quad L _ { 1 } ( x ) = { \frac { x - x _ { 0 } } { x _ { 1 } - x _ { 0 } } } ,
$$

and then define

$$
P ( x ) = L _ { 0 } ( x ) f ( x _ { 0 } ) + L _ { 1 } ( x ) f ( x _ { 1 } ) .
$$

Since

$$
L _ { 0 } ( x _ { 0 } ) = 1 , \ L _ { 0 } ( x _ { 1 } ) = 0 , \ L _ { 1 } ( x _ { 0 } ) = 0 , \mathrm { a n d } L _ { 1 } ( x _ { 1 } ) = 1 ,
$$

we have

$$
P ( x _ { 0 } ) = 1 \cdot f ( x _ { 0 } ) + 0 \cdot f ( x _ { 1 } ) = f ( x _ { 0 } ) = y _ { 0 }
$$

and

$$
P ( x _ { 1 } ) = 0 \cdot f ( x _ { 0 } ) + 1 \cdot f ( x _ { 1 } ) = f ( x _ { 1 } ) = y _ { 1 } .
$$

So $P$ is the unique linear function passing through $( x _ { 0 } , y _ { 0 } )$ and $( x _ { 1 } , y _ { 1 } )$ . (See Figure 3.3.)

![](images/89c219560d78d6a3a6a93d09c3fe27eda027a11d271cee874a31dd82f8aeb108.jpg)  
Figure 3.3

To generalize the concept of linear interpolation, consider the construction of a polynomial of degree at most $\pmb { n }$ that passes through the $n + 1$ points

$$
( x _ { 0 } , f ( x _ { 0 } ) ) , ( x _ { 1 } , f ( x _ { 1 } ) ) , \ldots , ( x _ { n } , f ( x _ { n } ) ) .
$$

![](images/ddf87b96c9c1889a4b4ee4d979786ca38d7bdf2bd7fcdde09a754be0dac628e7.jpg)  
Figure 3.4

(See Figure 3.4.)

In this case we need to construct, for each $k = 0 , 1 , \ldots , n$ ,a function $L _ { n , k } ( x )$ with the property that $L _ { n , k } ( x _ { i } ) = 0$ when $i \neq k$ and $L _ { n , k } ( x _ { k } ) = 1$ . To satisfy $L _ { n , k } ( x _ { i } ) = 0$ for each $i \neq k$ requires that the numerator of $L _ { n , k } ( x )$ contains the term

$$
( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { k - 1 } ) ( x - x _ { k + 1 } ) \cdot \cdot \cdot ( x - x _ { n } ) .
$$

To satisfy $L _ { n , k } ( x _ { k } ) = 1$ , the denominator of $L _ { n , k } ( x )$ must be equal to this term evaluated at ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { k }$ . Thus,

$$
L _ { n , k } ( x ) = { \frac { ( x - x _ { 0 } ) \cdot \cdot \cdot ( x - x _ { k - 1 } ) ( x - x _ { k + 1 } ) \cdot \cdot \cdot ( x - x _ { n } ) } { ( x _ { k } - x _ { 0 } ) \cdot \cdot \cdot \cdot ( x _ { k } - x _ { k - 1 } ) ( x _ { k } - x _ { k + 1 } ) \cdot \cdot \cdot ( x _ { k } - x _ { n } ) } } .
$$

A sketch of the graph of a typical $L _ { n , k }$ is shown in Figure 3.5.

![](images/0f57ecfa7192ffe9e04390b673a702b8b23f3df83b912587102396d7ea0aa5fd.jpg)  
Figure 3.5

The interpolating polynomial is easily described once the form of $L _ { n , k }$ is known. This polynomial, calld the nth Lagrange interpolating polynomial, is defined in the following theorem.

# Theorem 3.2

If $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ are $n + 1$ distinct numbers and $f$ is a function whose values are given at these numbers, then a unique polynomial $P ( x )$ of degree at most $\pmb { n }$ exists with

$$
f ( x _ { k } ) = P ( x _ { k } ) , \quad { \mathrm { f o r ~ e a c h ~ } } k = 0 , 1 , \ldots , n .
$$

This polynomial is given by

$$
P ( x ) = f ( x _ { 0 } ) L _ { n , 0 } ( x ) + \cdots + f ( x _ { n } ) L _ { n , n } ( x ) = \sum _ { k = 0 } ^ { n } f ( x _ { k } ) L _ { n , k } ( x ) ,
$$

where, for each $k = 0 , 1 , \ldots , n$

$$
{ \begin{array} { r l } & { L _ { n , k } ( x ) = { \frac { ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { k - 1 } ) ( x - x _ { k + 1 } ) \cdot \cdot \cdot ( x - x _ { n } ) } { ( x _ { k } - x _ { 0 } ) ( x _ { k } - x _ { 1 } ) \cdot \cdot \cdot ( x _ { k } - x _ { k - 1 } ) ( x _ { k } - x _ { k + 1 } ) \cdot \cdot \cdot ( x _ { k } - x _ { n } ) } } } \\ & { \qquad = \displaystyle \prod _ { i = 0 } ^ { n } { \frac { ( x - x _ { i } ) } { ( x _ { k } - x _ { i } ) } } . } \end{array} }
$$

We will write $L _ { n , k } ( x )$ simply as $L _ { k } ( x )$ when there is no confusion as to its degree.

Using the numbers (or nodes) $x _ { 0 } = 2$ ， $x _ { 1 } = 2 . 5$ ,and $x _ { 2 } = 4$ to find the second interpolating polynomial for $f ( x ) = 1 / x$ requires that we determine the coeficient polynomials $L _ { 0 } ( x )$ ， $L _ { 1 } ( x )$ ,and $L _ { 2 } ( x )$ . In nested form they are

$$
\begin{array} { l } { \displaystyle { L _ { 0 } ( x ) = \frac { ( x - 2 . 5 ) ( x - 4 ) } { ( 2 - 2 . 5 ) ( 2 - 4 ) } = ( x - 6 . 5 ) x + 1 0 , \hfill } } \\ { \displaystyle { L _ { 1 } ( x ) = \frac { ( x - 2 ) ( x - 4 ) } { ( 2 . 5 - 2 ) ( 2 . 5 - 4 ) } = \frac { ( - 4 x + 2 4 ) x - 3 2 } { 3 } , \hfill } } \end{array}
$$

and

$$
L _ { 2 } ( x ) = { \frac { ( x - 2 ) ( x - 2 . 5 ) } { ( 4 - 2 ) ( 4 - 2 . 5 ) } } = { \frac { ( x - 4 . 5 ) x + 5 } { 3 } } .
$$

Since $f ( x _ { 0 } ) = f ( 2 ) = 0 . 5 , f ( x _ { 1 } ) = f ( 2 . 5 ) = 0 . 4$ ,and $f ( x _ { 2 } ) = f ( 4 ) = 0 . 2 5$ ,we have

$$
{ \begin{array} { l } { P ( x ) = \displaystyle \sum _ { k = 0 } ^ { 2 } f ( x _ { k } ) L _ { k } ( x ) } \\ { = 0 . 5 ( ( x - 6 . 5 ) x + 1 0 ) + 0 . 4 { \frac { ( - 4 x + 2 4 ) x - 3 2 } { 3 } } + 0 . 2 5 { \frac { ( x - 4 . 5 ) x + 5 } { 3 } } } \\ { = ( 0 . 0 5 x - 0 . 4 2 5 ) x + 1 . 1 5 . } \end{array} }
$$

An approximation to $f ( 3 ) = { \frac { 1 } { 3 } }$ (see Figure 3.6) is

$$
f ( 3 ) \approx P ( 3 ) = 0 . 3 2 5 .
$$

![](images/865a44a59646cafeb105d3a06458ed65184bedc6b60c970d86ed435e1cc47e0b.jpg)  
Figure 3.6

Compare this to Table 3.1, where no Taylor polynomial, expanded about $x _ { 0 } = 1$ , could be used to reasonably approximate $f ( 3 ) = { \frac { 1 } { 3 } }$

We can use a CAS to construct an interpolating polynomial. For example,in Maple we use

>interp $( \mathbb { X } , \mathbb { Y } , \mathbb { x } )$ ；

where $X$ is the list $[ x _ { 0 } , \ldots , x _ { n } ] , Y$ is the list $[ f ( x _ { 0 } ) , \ldots , f ( x _ { n } ) ]$ ,and $x$ is the variable to be used. In this example we can generate the interpolating polynomial $p = 0 . 0 5 x ^ { 2 } - 0 . 4 2 5 x +$ 1.15 with the command

>p:=interp([2,2.5,4],[0.5,0.4,0.25],x);

To evaluate $p ( 3 )$ as an approximation to $\begin{array} { r } { f ( 3 ) = \frac { 1 } { 3 } } \end{array}$ ,enter

>subs $( X = 3 , p )$ ；

which gives 0.325.

The next step is to calculate a remainder term or bound for the eror involved in approximating a function by an interpolating polynomial. This is done in the following theorem.

Suppose $x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ are distinct numbers in the interval $[ a , b ]$ and $f \in C ^ { n + 1 } [ a , b ]$ Then, for each $\pmb { x }$ in $\left[ a , b \right]$ ,a number $\xi ( x )$ in $( a , b )$ exists with

$$
f ( x ) = P ( x ) + \frac { f ^ { ( n + 1 ) } ( \xi ( x ) ) } { ( n + 1 ) ! } ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n } ) ,
$$

where $P ( x )$ is the interpolating polynomial given in Eq. (3.1).

Proof Note first that if $x \ = \ x _ { k }$ , for any $k = 0 , 1 , \ldots , n$ then $f ( x _ { k } ) = P ( x _ { k } )$ ,and choosing $\xi ( x _ { k } )$ arbitrarily in $( a , b )$ yields Eq. (3.3). If $x \neq x _ { k }$ ,for all $k = 0 , 1 , \ldots , n ,$ define the function $\pmb { g }$ for $t$ in $[ a , b ]$ by

$$
{ \begin{array} { l } { g ( t ) = f ( t ) - P ( t ) - [ f ( x ) - P ( x ) ] { \frac { ( t - x _ { 0 } ) ( t - x _ { 1 } ) \cdot \cdot \cdot ( t - x _ { n } ) } { ( x - x _ { 0 } ) ( x - x _ { 1 } ) \cdot \cdot \cdot ( x - x _ { n } ) } } } \\ { \qquad = f ( t ) - P ( t ) - [ f ( x ) - P ( x ) ] \prod _ { i = 0 } ^ { n } { \frac { ( t - x _ { i } ) } { ( x - x _ { i } ) } } . } \end{array} }
$$

Since $f \in C ^ { n + 1 } [ a , b ]$ ,and $P \in C ^ { \infty } [ a , b ]$ , it follows that $g \in C ^ { n + 1 } [ a , b ]$ .For $t = x _ { k }$ we have

$$
\cdot ( x _ { k } ) = f ( x _ { k } ) - P ( x _ { k } ) - \{ f ( x ) - P ( x ) \} \prod _ { i = 0 } ^ { n } { \frac { ( x _ { k } - x _ { i } ) } { ( x - x _ { i } ) } } = 0 - [ f ( x ) - P ( x ) ] \cdot 0 = 0
$$

Moreover,

$$
g ( x ) = f ( x ) - P ( x ) - \left[ f ( x ) - P ( x ) \right] \prod _ { i = 0 } ^ { n } { \frac { ( x - x _ { i } ) } { ( x - x _ { i } ) } } = f ( x ) - P ( x ) - \left[ f ( x ) - P ( x ) \right] \prod _ { i = 0 } ^ { n } { \frac { ( x - x _ { i } ) } { ( x - x _ { i } ) } }
$$

Thus, $g \in C ^ { n + 1 } [ a , b ]$ ,and $g$ is zero at the $n + 2$ distinct numbers $x , x _ { 0 } , x _ { 1 } , \ldots , x _ { n }$ . By the Generalized Rolle's Theorem, there exists a number $\pmb { \xi }$ in $( a , b )$ for which $g ^ { ( n + 1 ) } ( \xi ) = 0$