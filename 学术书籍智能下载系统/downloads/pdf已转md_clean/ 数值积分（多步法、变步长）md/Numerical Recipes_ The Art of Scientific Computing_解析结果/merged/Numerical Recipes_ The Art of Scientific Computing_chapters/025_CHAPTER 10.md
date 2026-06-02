# CHAPTER 10

# 10.0 Introduction

In a nutshell: You are given a single function $f$ that depends on one or more independent variables. You want to find the value of those variables where $f$ takes on a maximum or a minimum value. You can then calculate what value of $f$ is achieved at the maximum or minimum. The tasks of maximization and minimization are trivially related to each other, since one person’s function $f$ could just as well be another’s $- f$ . The computational desiderata are the usual ones: Do it quickly, cheaply, and in small memory. Often the computational effort is dominated by the cost of evaluating $f$ (and also perhaps its partial derivatives with respect to all variables, if the chosen algorithm requires them). In such cases the desiderata are sometimes replaced by the simple surrogate: Evaluate $f$ as few times as possible.

An extremum (maximum or minimum point) can be either global (truly the highest or lowest function value) or local (the highest or lowest in a finite neighborhood and not on the boundary of that neighborhood). (See Figure 10.0.1.) Finding a global extremum is, in general, a very difficult problem. Two standard heuristics are widely used: (i) Find local extrema starting from widely varying starting values of the independent variables (perhaps chosen quasi-randomly, as in $\ S 7 . 8 )$ , and then pick the most extreme of these (if they are not all the same); or (ii) perturb a local extremum by taking a finite amplitude step away from it, and then see if your routine returns you to a better point, or “always” to the same one. More recently, so-called simulated annealing methods (-10.12) have demonstrated important successes on a variety of global extremization problems.

Our chapter title could just as well be optimization, which is the usual name for this very large field of numerical research. The importance ascribed to the various tasks in this field depends strongly on the particular interests of whom you talk to. Economists, and some engineers, are particularly concerned with constrained optimization, where there are a priori limitations on the allowed values of independent variables. For example, the production of wheat in the United States must be a nonnegative number. One particularly well-developed area of constrained optimization is linear programming, where both the function to be optimized and the constraints happen to be linear functions of the independent variables. Sections 10.10 and 10.11, which are otherwise somewhat disconnected from the rest of the material that we have chosen to include in this chapter, discuss the two major approaches to such problems, the so-called simplex algorithm and interior-point methods.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0008_pages_0491-0560/auto/images/83199decde8d7712dcb40117893af34022229efc530bf249c4b8b7e033cfed74.jpg)  
Figure 10.0.1. Extrema of a function in an interval. Points $A , C$ , and $E$ are local, but not global, maxima. Points $B$ and $F$ are local, but not global, minima. The global maximum occurs at $G$ , which is on the boundary of the interval so that the derivative of the function need not vanish there. The global minimum is at $D$ . At point $E$ , derivatives higher than the first vanish, a situation that can cause difficulty for some algorithms. The points $X$ , $Y$ , and $Z$ are said to bracket the minimum $F$ , since $Y$ is less than both $X$ and $Z$ .

Two other sections, $\ S 1 0 . 1 2$ and $\ S 1 0 . 1 3$ , also lie outside of our main thrust, but for a different reasons. As mentioned, $\ S 1 0 . 1 2$ discusses so-called annealing methods. These are stochastic, rather than deterministic, algorithms. Annealing methods have solved some problems previously thought to be practically insoluble: They address directly the problem of finding global extrema in the presence of large numbers of undesired local extrema. Section 10.13 discusses a different kind of minimization, namely that of path length along a directed graph by the technique known as dynamic programming. This will prove important later, in Chapter 16.

The other sections in this chapter constitute a selection of established algorithms for unconstrained minimization. (For definiteness, we will henceforth regard the optimization problem as that of minimization.) These sections are connected, with later ones depending on earlier ones. If you are just looking for the one “perfect” algorithm to solve your particular application, you may feel that we are telling you more than you want to know. Unfortunately, there is no perfect optimization algorithm. This is a case where we strongly urge you to try more than one method in comparative fashion. However, here are some guidelines:

For one-dimensional minimization (minimize a function of one variable), you must choose between methods that need only evaluations of the function, and methods that also require evalutations of the function’s derivative. The latter are typically more powerful, but not always enough so as to compensate for the additional calculations of derivatives. We can easily construct examples favoring one approach or

the other.

- For one-dimensional minimization without calculation of the derivative, first bracket the minimum as described in $\ S 1 0 . 2$ , and then use Brent’s method as described in $\ S 1 0 . 3$ . If your function has a discontinuous second (or lower) derivative, then the parabolic interpolations of Brent’s method are of no advantage, and you might wish to use the simplest form of golden section search, as described in $\ S 1 0 . 2$ .   
For one-dimensional minimization with calculation of the derivative, $\ S 1 0 . 4$ supplies a variant of Brent’s method that makes limited use of the first derivative information. We shy away from the alternative of using derivative information to construct high-order interpolating polynomials. In our experience, the improvement in convergence very near a smooth, analytic minimum does not make up for the tendency of polynomials sometimes to give wildly wrong interpolations at early stages, especially for functions that may have sharp, “exponential” features.

For the multidimensional case, where you want to minimize a function of two or more variables, the analog of the derivative is the gradient, a vector quantity. You now have three options: compute the gradients using your function’s known analytic form, compute the gradients by taking finite differences of computed function values, or don’t compute the gradients at all. You also get to choose between methods that require storage of order $N ^ { 2 }$ and those that require only of order $N$ , where $N$ is the number of dimensions. For moderate values of $N$ this is not a serious constraint; but if $N$ is itself the number of points in a two- or three-dimensional grid, then $N ^ { 2 }$ storage may be prohibitive.

- For minimization without gradients, the downhill simplex method due to Nelder and Mead, discussed in $\ S 1 0 . 5$ , is slow, but sure. (This use of the word “simplex” is not to be confused with the simplex method of linear programming.) The method just crawls downhill in a straightforward fashion that makes almost no special assumptions about your function. While this can be extremely slow, it can also be extremely robust. Not to be overlooked is the fact that the code is concise and completely self-contained: a general $N$ -dimensional minimization program in under 100 program lines! The storage requirement is of order $N ^ { 2 }$ , and derivative calculations are not required. When your function has some smoothness to it, but you still don’t want to compute gradients, turn to direction set methods, of which Powell’s method is the prototype (-10.7). Powell’s method requires a one-dimensional minimization subalgorithm such as Brent’s method (see above). Storage is of order $N ^ { 2 }$ . Direction set methods are much faster than the downhill simplex method. But keep reading for, possibly, an even better alternative.

Now the case where you are willing to calculate gradients from your function’s known analytic form:

- Conjugate gradient methods, as typified by the Fletcher-Reeves algorithm and the closely related and probably superior Polak-Ribiere algorithm are widely used. Conjugate gradient methods require only of order a few times $N$ storage, derivative calculations, and one-dimensional subminimization. Turn to $\ S 1 0 . 8$ for detailed discussion and implementation. - Quasi-Newton or variable metric methods are typified by the Davidon-Fletcher-

Powell (DFP) algorithm (sometimes referred to just as the Fletcher-Powell method) or the closely related Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm. These methods require of order $N ^ { 2 }$ storage, derivative calculations, and one-dimensional subminimization. Details are in $\ S 1 0 . 9$ . Our personal experience is that the quasi-Newton methods dominate the conjugate gradient methods (if you can afford the storage), but there are probably applications where the reverse is true.

Finally, the case where the method uses gradients, but you are willing to let them be calculated by extra function evaluations (and finite differences):

- In our experience, the quasi-Newton (variable metric) methods work very well in this case, so much so that they can be significantly more efficient than Powell’s method on suitable problems. In $\ S 1 0 . 9$ we give an implementation that (almost) hides the gradient calculation completely. Thus quasi-Newton is effectively our first choice of method both when you are willing to calculate gradients, and when you are not willing!

You can now proceed to scale the peaks (and/or plumb the depths) of practical optimization.

# CITED REFERENCES AND FURTHER READING:

Dennis, J.E., and Schnabel, R.B. 1983, Numerical Methods for Unconstrained Optimization and Nonlinear Equations; reprinted 1996 (Philadelphia: S.I.A.M.).   
Polak, E. 1971, Computational Methods in Optimization (New York: Academic Press).   
Gill, P.E., Murray, W., and Wright, M.H. 1981, Practical Optimization (New York: Academic Press).   
Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), Chapter 17.   
Jacobs, D.A.H. (ed.) 1977, The State of the Art in Numerical Analysis (London: Academic Press), Chapter III.1.   
Brent, R.P. 1973, Algorithms for Minimization without Derivatives (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2002 (New York: Dover).   
Dahlquist, G., and Bjorck, A. 1974, Numerical Methods (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2003 (New York: Dover), Chapter 10.

# 10.1 Initially Bracketing a Minimum

What does it mean to bracket a minimum? A root of a function is known to be bracketed by a pair of points, $a$ and $b$ , when the function has opposite sign at those two points. A minimum, by contrast, is known to be bracketed only when there is a triplet of points, $a < b < c$ (or $c < b < a$ ), such that $f ( b )$ is less than both $f ( a )$ and $f ( c )$ . In this case we know that the function (if it is smooth) has a minimum in the interval $( a , c )$ .

We consider the initial bracketing of a minimum to be an essential part of any one-dimensional minimization. There are some one-dimensional algorithms that do not require a rigorous initial bracketing. However, we would never trade the secure feeling of knowing that a minimum is “in there somewhere” for the dubious reduction of function evaluations that these nonbracketing routines may promise. Please bracket your minima (or, for that matter, your zeros) before isolating them!

There is not much theory as to how to do this bracketing. Obviously you want to step downhill. But how far? We like to take larger and larger steps, starting with some (wild?) initial guess and then increasing the stepsize at each step either by a constant factor, or else by the result of a parabolic extrapolation of the preceding points that is designed to take us to the extrapolated turning point. It doesn’t much matter if the steps get big. After all, we are stepping downhill, so we already have the left and middle points of the bracketing triplet. We just need to take a big enough step to stop the downhill trend and get a high third point.

Here is our standard routine, the function bracket. It appears in the structure Bracketmethod that serves as the base class for all the one-dimensional minimization methods we give in this chapter.

# struct Bracketmethod {

Base class for one-dimensional minimization routines. Provides a routine to bracket a minimum and several utility functions.

Doub ax,bx,cx,fa,fb,fc;   
template <class T>   
void bracket(const Doub a, const Doub b, T &func) Given a function or functor func, and given distinct initial points ax and bx, this routine searches in the downhill direction (defined by the function as evaluated at the initial points) and returns new points ax, bx, cx that bracket a minimum of the function. Also returned are the function values at the three points, fa, fb, and fc.   
{   
const Doub GOLD $^ { 1 = 1 }$ .618034,GLIMIT $\mathop { : = }$ 100.0,TINY $= 1$ .0e-20;   
Here GOLD is the default ratio by which successive intervals are magnified and GLIMIT   
is the maximum magnification allowed for a parabolic-fit step.   
ax=a; bx=b;   
Doub fu;   
fa=func(ax);   
fb=func(bx);   
if (fb > fa) { Switch roles of $^ { a }$ and $^ { b }$ so that we can go SWAP(ax,bx); downhill in the direction from $^ { a }$ to $^ { b }$ . SWAP(fb,fa);   
}   
cx=bx+GOLD $^ { * }$ (bx-ax); First guess for $c$ .   
fc=func(cx);   
while (fb $>$ fc) { Keep returning here until we bracket. Doub $\mathbf { r } { } =$ (bx-ax) $^ *$ (fb-fc); Compute $\pmb { u }$ by parabolic extrapolation from Doub q=(bx-cx)\*(fb-fa); $a , b , c$ . TINY is used to prevent any pos-Doub u=bx-((bx-cx)\*q-(bx-ax) $^ { * \mathbf { r } }$ )/ sible division by zero. (2.0\*SIGN(MAX(abs(q-r),TINY), $\mathsf { q } ^ { - \pmb { \mathbf { r } } ) }$ ); Doub ulim $\mathbf { \bar { \tau } } = \mathbf { b } \mathbf { x } + \mathbf { G } \mathbf { L } \mathbf { I } \mathbf { M } \mathbf { I } \mathbf { T } * \left( \mathbf { c } \mathbf { x } \mathbf { - } \mathbf { b } \mathbf { x } \right)$ ; We won’t go farther than this. Test various possibilities: if ( $\left( \mathrm { b x - u } \right) * \left( \mathrm { u - c x } \right) \ > \ 0 \ . 0 )$ { Parabolic $\boldsymbol { u }$ is between $^ { b }$ and $c$ : try it. fu=func(u); if (fu $<$ fc) { Got a minimum between $^ { b }$ and $c$ . ax=bx; ${ \tt b x } = { \tt u }$ ; fa=fb; fb=fu; return; } else if (fu > fb) { Got a minimum between between $^ { a }$ and $\boldsymbol { u }$ . $\mathbf { \vec { C } } \mathbf { \vec { X } } ^ { = } \mathbf { \vec { u } }$ ; fc=fu; return; } u=cx+GOLD\*(cx-bx); Parabolic fit was no use. Use default magfu=func(u); nification. } else if ((cx-u)\*(u-ulim) > 0.0) { Parabolic fit is between $c$ and fu=func(u); its allowed limit.

if (fu < fc) { shft3(bx,cx,u,u+GOLD\*(u-cx)); shft3(fb,fc,fu,func(u)); } } else if ((u-ulim) $^ *$ (ulim-cx) >= 0.0) { Limit parabolic $\pmb { u }$ to maximum u=ulim; allowed value. fu=func(u); } else { Reject parabolic $\pmb { u }$ , use default magnificau=cx+GOLD\*(cx-bx); tion. fu=func(u); shft3(ax,bx,cx,u); Eliminate oldest point and continue. shft3(fa,fb,fc,fu); } } inline void shft2(Doub &a, Doub &b, const Doub c) Utility function used in this structure or others derived from it. { $a = b$ ; $\mathtt { b } = _ { \mathtt { C } }$ ; } inline void shft3(Doub &a, Doub &b, Doub &c, const Doub d) $a = b$ ; $\mathtt { b } = _ { \mathtt { C } }$ ; $\mathtt { c } { = } \mathtt { d }$ ; } inline void mov3(Doub &a, Doub &b, Doub &c, const Doub d, const Doub e, const Doub f) { a=d; b=e; c=f; }

(Because of the housekeeping involved in moving around three or four points and their function values, the above program ends up looking deceptively formidable. That is true of several other programs in this chapter as well. The underlying ideas, however, are quite simple.)

# 10.2 Golden Section Search in One Dimension

Recall how the bisection method finds roots of functions in one dimension (-9.1): The root is supposed to have been bracketed in an interval $( a , b )$ . One then evaluates the function at an intermediate point $x$ and obtains a new, smaller bracketing interval, either $( a , x )$ or $( x , b )$ . The process continues until the bracketing interval is acceptably small. It is optimal to choose $x$ to be the midpoint of $( a , b )$ so that the decrease in the interval length is maximized when the function is as uncooperative as it can be, i.e., when the luck of the draw forces you to take the bigger bisected segment.

There is a precise, though slightly subtle, translation of these considerations to the minimization problem. The analog of bisection is to choose a new point $x$ , either between $a$ and $b$ or between $b$ and $c$ . Suppose, to be specific, that we make the latter choice. Then we evaluate $f ( x )$ . If $f ( b ) < f ( x )$ , then the new bracketing triplet of points is $( a , b , x )$ ; contrariwise, if $f ( b ) > f ( x )$ , then the new bracketing triplet is $( b , x , c )$ . In all cases, the middle point of the new triplet is the abscissa whose ordinate is the best minimum achieved so far; see Figure 10.2.1. We continue the process of bracketing until the distance between the two outer points of the triplet is tolerably small.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0008_pages_0491-0560/auto/images/5fde25ee5cccabdb18b2fc7dc418870cfd543f14a89ee8b52af5294b554a1c45.jpg)  
Figure 10.2.1. Successive bracketing of a minimum. The minimum is originally bracketed by points 1,3,2. The function is evaluated at 4, which replaces 2; then at 5, which replaces 1; then at 6, which replaces 4. The rule at each stage is to keep a center point that is lower than the two outside points. After the steps shown, the minimum is bracketed by points 5,3,6.

How small is “tolerably” small? For a minimum located at a value $b$ , you might naively think that you will be able to bracket it in as small a range as $( 1 - \epsilon ) b <$ $b < ( 1 + \epsilon ) b$ , where $\epsilon$ is your computer’s floating-point precision, a number like $1 0 ^ { - 7 }$ (for float) or $2 \times 1 0 ^ { - 1 6 }$ (for double). Not so! In general, the shape of your function $f ( x )$ near $b$ will be given by Taylor’s theorem,

$$
f ( x ) \approx f ( b ) + { \textstyle { \frac { 1 } { 2 } } } f ^ { \prime \prime } ( b ) ( x - b ) ^ { 2 }
$$

The second term will be negligible compared to the first (that is, will be a factor $\epsilon$ smaller and will act just like zero when added to it) whenever

$$
| x - b | < \sqrt { \epsilon } | b | ~ \sqrt { \frac { 2 | f ( b ) | } { b ^ { 2 } f ^ { \prime \prime } ( b ) } }
$$

The reason for writing the right-hand side in this way is that, for most functions, the final square root is a number of order unity. Therefore, as a rule of thumb, it is hopeless to ask for a bracketing interval of width less than $\sqrt { \epsilon }$ times its central value, a fractional width of only about $1 0 ^ { - 4 }$ (single precision) or $1 0 ^ { - 8 }$ (double precision). Knowing this inescapable fact will save you a lot of useless bisections!

The minimum-finding routines of this chapter will often call for a user-supplied argument tol, and return with an abscissa whose fractional precision is about $\pm \mathtt { t o l }$ (bracketing interval of fractional size about $2 \times \tt t o l$ ). Unless you have a better estimate for the right-hand side of equation (10.2.2), you should set tol equal to (or not much less than) the square root of your machine’s floating-point precision, since smaller values will gain you nothing.

It remains to decide on a strategy for choosing the new point $x$ , given $( a , b , c )$ . Suppose that $b$ is a fraction $w$ of the way between $a$ and $c$ , i.e.,

$$
{ \frac { b - a } { c - a } } = w \qquad { \frac { c - b } { c - a } } = 1 - w
$$

Also suppose that our next trial point $x$ is an additional fraction $Z$ beyond $b$ ,

$$
{ \frac { x - b } { c - a } } = z
$$

Then the next bracketing segment will either be of length $w + z$ relative to the current one, or else of length $1 - w$ . If we want to minimize the worst case possibility, then we will choose $Z$ to make these equal, namely

$$
z = 1 - 2 w
$$

We see at once that the new point is the symmetric point to $b$ in the original interval, namely with $| b - a |$ equal to $\lvert x - c \rvert$ . This implies that the point $x$ lies in the larger of the two segments ( $Z$ is positive only if $w < 1 / 2$ ).

But where in the larger segment? Where did the value of $w$ itself come from? Presumably from the previous stage of applying our same strategy. Therefore, if $Z$ is chosen to be optimal, then so was $w$ before it. This scale similarity implies that $x$ should be the same fraction of the way from $b$ to $c$ (if that is the bigger segment) as was $b$ from $a$ to $c$ , in other words,

$$
{ \frac { z } { 1 - w } } = w
$$

Equations (10.2.5) and (10.2.6) give the quadratic equation

$$
w ^ { 2 } - 3 w + 1 = 0 \qquad \mathrm { y i e l d i n g } \qquad w = { \frac { 3 - { \sqrt { 5 } } } { 2 } } \approx 0 . 3 8 1 9 7
$$

In other words, the optimal bracketing interval $( a , b , c )$ has its middle point $b$ a fractional distance 0.38197 from one end (say $a$ ), and 0.61803 from the other end (say $b$ ). These fractions are those of the so-called golden mean or golden section, whose supposedly aesthetic properties hark back to the ancient Pythagoreans. This optimal method of function minimization, the analog of the bisection method for finding zeros, is thus called the golden section search, which can be summarized as follows:

Given, at each stage, a bracketing triplet of points, the next point to be tried is that which is a fraction 0.38197 into the larger of the two intervals (measuring from the central point of the triplet). If you start out with a bracketing triplet whose segments are not in the golden ratios, the procedure of choosing successive points at the golden mean point of the larger segment will quickly converge you to the proper self-replicating ratios.

The golden section search guarantees that each new function evaluation will (after self-replicating ratios have been achieved) bracket the minimum to an interval just 0.61803 times the size of the preceding interval. This is comparable to, but not quite as good as, the 0.50000 that holds when finding roots by bisection. Note that the convergence is linear (in the language of Chapter 9), meaning that successive significant figures are won linearly with additional function evaluations. In the next section we will give a superlinear method, in which the rate at which successive significant figures are liberated increases with each successive function evaluation.

To use the golden section search, you need statements like the following:

Golden golden;   
golden.bracket(a,b,func);   
xmin=golden.minimize(func);

The value of the function at the minimum is available in golden.fmin. If you want to specify a function tolerance different from the default value of $3 . 0 \mathsf { e } ^ { - 8 }$ , simply override the default value in the constructor:

$\smash { \tan 1 = \ldots }$ Golden golden(tol);

If you want to use a specified bracket as the initial condition, omit the call to bracket and set the bracket explicitly:

golden.ax = ...; golden.bx $=$ ...; golden.cx =

Here is the routine:

struct Golden : Bracketmethod {   
Golden section search for minimum. Doub xmin,fmin; const Doub tol; Golden(const Doub toll $^ { = 3 }$ .0e-8) : tol(toll) {} template <class T> Doub minimize(T &func) Given a function or functor f, and given a bracketing triplet of abscissas ax, bx, cx (such that bx is between ax and cx, and f(bx) is less than both f(ax) and f(cx)), this routine performs a golden section search for the minimum, isolating it to a fractional precision of about tol. The abscissa of the minimum is returned as xmin, and the function value at the minimum is returned as min, the returned function value.   
{

The golden ratios.

At any given time we will keep track of four points, $^ { \mathbf { x } 0 , \mathbf { x } 1 , \mathbf { x } 2 , \mathbf { x } 3 }$ . Make $\mathtt { x 0 }$ to $\tt x 1$ the smaller segment,

and fill in the new point to be tried.

const Doub R=0.61803399, $\mathrm { C } \mathrm { = } 1$ .0-R;   
Doub x1,x2;   
Doub $\tt { x 0 = }$ ax;   
Doub x3=cx;   
if (abs(cx-bx) $>$ abs(bx-ax)) { x1=bx; x2=bx+C\*(cx-bx);   
} else { x2=bx; x1=bx-C\*(bx-ax);   
}   
Doub f1=func(x1);   
Doub f2=func(x2);   
while (abs(x3-x0) $>$ tol\*(abs(x1)+a if (f2 < f1) { shft3(x0,x1,x2,R\*x2+C\*x3); shft2(f1,f2,func(x2)); } else { shft3(x3,x2,x1,R\*x1+C\*x0); shft2(f2,f1,func(x1)); }   
}   
if (f1 < f2) { xmin=x1; The initial function evaluations. Note that we never need to evaluate the function bs(x2))) { at the original endpoints. One possible outcome,   
its housekeeping,   
and a new function evaluation.   
The other outcome,   
and its new function evaluation.   
Back to see if we are done.   
We are done. Output the best of the two current values.

fmin=f1; } else { xmin=x2; fmin=f2; } return xmin; } };

# 10.3 Parabolic Interpolation and Brent's Method in One Dimension

We already tipped our hand about the desirability of parabolic interpolation in the bracket routine of $\ S 1 0 . 1$ , but it is now time to be more explicit. A golden section search is designed to handle, in effect, the worst possible case of function minimization, with the uncooperative minimum hunted down and cornered like a scared rabbit. But why assume the worst? If the function is nicely parabolic near to the minimum — surely the generic case for sufficiently smooth functions — then the parabola fitted through any three points ought to take us in a single leap to the minimum, or at least very near to it (see Figure 10.3.1). Since we want to find an abscissa rather than an ordinate, the procedure is technically called inverse parabolic interpolation.

The formula for the abscissa $x$ that is the minimum of a parabola through three points $f ( a ) , f ( b )$ , and $f ( c )$ is

$$
x = b - { \frac { 1 } { 2 } } { \frac { ( b - a ) ^ { 2 } [ f ( b ) - f ( c ) ] - ( b - c ) ^ { 2 } [ f ( b ) - f ( a ) ] } { ( b - a ) [ f ( b ) - f ( c ) ] - ( b - c ) [ f ( b ) - f ( a ) ] } }
$$

as you can easily derive. This formula fails only if the three points are collinear, in which case the denominator is zero (the minimum of the parabola is infinitely far away). Note, however, that (10.3.1) is as happy jumping to a parabolic maximum as to a minimum. No minimization scheme that depends solely on (10.3.1) is likely to succeed in practice.

The exacting task is to invent a scheme that relies on a sure-but-slow technique, like golden section search, when the function is not cooperative, but that switches over to (10.3.1) when the function allows. The task is nontrivial for several reasons, including these: (i) The housekeeping needed to avoid unnecessary function evaluations in switching between the two methods can be complicated. (ii) Careful attention must be given to the “endgame,” where the function is being evaluated very near to the roundoff limit of equation (10.2.2). (iii) The scheme for detecting a cooperative versus noncooperative function must be very robust.

Brent’s method [1] is up to the task in all particulars. At any particular stage, it is keeping track of six function points (not necessarily all distinct), $a , b , u , v , w$ and $x$ , defined as follows: The minimum is bracketed between $a$ and $b$ ; $x$ is the point with the very least function value found so far (or the most recent one in case of a tie); $w$ is the point with the second least function value; $v$ is the previous value of $w$ ; and $u$ is the point at which the function was evaluated most recently. Also appearing in the algorithm is the point $x _ { m }$ , the midpoint between $a$ and $b$ ; however, the function is not evaluated there.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0008_pages_0491-0560/auto/images/5372286af901df7d15d03db9b41538f7b686fa71e7aab732147a8d22cfd8b9ff.jpg)  
Figure 10.3.1. Convergence to a minimum by inverse parabolic interpolation. A parabola (dashed line) is drawn through the three original points 1,2,3 on the given function (solid line). The function is evaluated at the parabola’s minimum, 4, which replaces point 3. A new parabola (dotted line) is drawn through points 1,4,2. The minimum of this parabola is at 5, which is close to the minimum of the function.

You can read the code below to understand the method’s logical organization. Mention of a few general principles here may, however, be helpful: Parabolic interpolation is attempted, fitting through the points $x , v$ , and $w$ . To be acceptable, the parabolic step must (i) fall within the bounding interval $( a , b )$ , and (ii) imply a movement from the best current value $x$ that is less than half the movement of the step before last. This second criterion ensures that the parabolic steps are actually converging to something, rather than, say, bouncing around in some nonconvergent limit cycle. In the worst possible case, where the parabolic steps are acceptable but useless, the method will approximately alternate between parabolic steps and golden sections, converging in due course by virtue of the latter. The reason for comparing to the step before last seems essentially heuristic: Experience shows that it is better not to “punish” the algorithm for a single bad step if it can make it up on the next one.

Another principle exemplified in the code is never to evaluate the function less than a distance tol from a point already evaluated (or from a known bracketing point). The reason is that, as we saw in equation (10.2.2), there is simply no information content in doing so: The function will differ from the value already evaluated only by an amount of order the roundoff error. Therefore, in the code below you will find several tests and modifications of a potential new point, imposing this restriction. This restriction also interacts subtly with the test for “doneness,” which the method takes into account.

A typical ending configuration for Brent’s method is that $a$ and $b$ are $2 \times x \times \mathtt { t o l }$ apart, with $x$ (the best abscissa) at the midpoint of $a$ and $b$ , and therefore fractionally accurate to $\pm \mathtt { t o l }$ .

The calling sequence for Brent is exactly analogous to that of Golden in the previous section. Indulge us a final reminder that tol should generally be no smaller than the square root of your machine’s floating-point precision.

# struct Brent : Bracketmethod {

Brent’s method to find a minimum.

Doub xmin,fmin;   
const Doub tol;   
Brent(const Doub toll $^ { = 3 }$ .0e-8) : tol(toll) {} template <class T>   
Doub minimize(T &func) Given a function or functor f, and given a bracketing triplet of abscissas ax, bx, cx (such that bx is between ax and cx, and f(bx) is less than both $\pmb { \mathrm { f } } \left( \mathsf { a x } \right)$ and $\pmb { \mathrm { f } } \left( \mathsf { c x } \right)$ ), this routine isolates the minimum to a fractional precision of about tol using Brent’s method. The abscissa of the minimum is returned as xmin, and the function value at the minimum is rned as min, the returned function value.   
{   
const Int ITMAX $\mathop {    }$ 100;   
const Doub CGOLD $\scriptstyle = 0$ .3819660;   
const Doub ZEPS $=$ numeric_limits<Doub>::epsilon()\*1.0e-3;   
Here ITMAX is the maximum allowed number of iterations; CGOLD is the golden ratio;   
and ZEPS is a small number that protects against trying to achieve fractional accuracy   
for a minimum that happens to be exactly zero.   
Doub a,b, $\mathtt { d } \mathtt { = } 0$ .0,etemp,fu,fv,fw,fx;   
Doub p,q,r,tol1,tol2,u,v,w,x,xm;   
Doub $\mathtt { e } = 0 . 0$ ; This will be the distance moved on the step before last.   
$\mathtt { a } =$ (ax < cx ? ax : cx); a and b must be in ascending order,   
$\mathtt { b } =$ (ax > cx ? ax : cx); but input abscissas need not be.   
$\scriptstyle \mathtt { X } = \mathtt { W } = \mathtt { V } = \mathtt { b } \mathtt { X }$ ; Initializations...   
fw=fv=fx=func(x);   
for (Int iter ${ \tt = } 0$ ;iter<ITMAX;iter++) { Main program loop. $\mathtt { x m = 0 }$ . $^ { 5 \ast }$ (a+b); tol2=2. $^ { 0 * }$ (tol1 $=$ tol\*abs(x)+ZEPS); if (abs(x-xm) $< =$ (tol2-0.5\*(b-a))) { Test for done here. fmin=fx; return xmin $= \times$ ; } if (abs(e) $>$ tol1) { Construct a trial parabolic fit. r=(x-w)\*(fx-fv); q=(x-v)\*(fx-fw); p=(x-v)\*q-(x-w)\*r; q=2.0\*(q-r); if (q > 0.0) $p \ = \ - \mathtt { p }$ ; q=abs(q); etemp=e; $\mathtt { e } \mathtt { = } \mathtt { d }$ ; if (abs(p) $> =$ abs(0.5\*q\*etemp) | $1 \texttt { p } < = \texttt { q } * \left( \mathtt { a } \mathrm { - } \underline { { x } } \right)$ | $| \mathrm { ~  ~ p ~ } > = \mathrm { q } * \left( \mathrm { b - x } \right) \rangle$ ) $\mathrm { d = C G O L D * \left( e = ( x ~ \gamma > = ~ x m ~ ? ~ \ a - x ~ : ~ \ b - x ) ~ \right) \ }$ ; The above conditions determine the acceptability of the parabolic fit. Here we take the golden section step into the larger of the two segments. else { $\mathtt { d } \mathtt { = p } / { \mathsf { q } } ;$ Take the parabolic step. $\tt u = x + d$ ; if (u-a < tol2 || b-u < tol2) d=SIGN(tol1,xm-x); } else { d $\scriptstyle \mathtt { = C G O L D * ( e = ( x \ > = \ x m \ ? \ \ a - x \ : \ b - x ) ) } ;$ ; $\mathbf { u } =$ (abs(d) $> =$ tol1 ? x+d : x+SIGN(tol1,d)); fu=func(u); This is the one function evaluation per iteration. if (fu $< =$ fx) { Now decide what to do with our funcif $\texttt { u } > = \texttt { x }$ ) $\mathrm { a } = \mathrm { x }$ ; else $\mathtt { b } \mathtt { = x }$ ; tion evaluation. shft3 $( \mathbb { v } , \mathbb { w } , \mathbb { x } , \mathbb { u } )$ ; Housekeeping follows: shft3(fv,fw,fx,fu);

} else { if (u < x) $\mathtt { a } = \mathtt { u }$ ; else $b = \pi$ ; if (fu $< =$ fw || $\textbf { \textit { w } } = = \textbf { \textit { x } } )$ ) { $\mathrm { v } = \mathrm { w }$ ; $\mathtt { w } = \mathtt { u }$ ; fv=fw; fw=fu; } else if (fu <= fv || v == x || v == w) { $\mathrm { v } = \mathrm { u }$ ; fv=fu; } } Done with housekeeping. Back for another iteration. throw("Too many iterations in brent"); } };

# CITED REFERENCES AND FURTHER READING:

Brent, R.P. 1973, Algorithms for Minimization without Derivatives (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2002 (New York: Dover), Chapter 5.[1]   
Forsythe, G.E., Malcolm, M.A., and Moler, C.B. 1977, Computer Methods for Mathematical Computations (Englewood Cliffs, NJ: Prentice-Hall), $\ S 8 . 2$ .

# 10.4 One-Dimensional Search with First Derivatives

Here we want to accomplish precisely the same goal as in the previous section, namely to isolate a functional minimum that is bracketed by the triplet of abscissas $( a , b , c )$ , but utilizing an additional capability to compute the function’s first derivative as well as its value.

In principle, we might simply search for a zero of the derivative, ignoring the function value information, using a root finder like rtflsp or zbrent $( \ S 9 . 2 - \ S 9 . 3 )$ . It doesn’t take long to reject that idea: How do we distinguish maxima from minima? Where do we go from initial conditions where the derivatives on one or both of the outer bracketing points indicate that “downhill” is in the direction out of the bracketed interval?

We don’t want to give up our strategy of maintaining a rigorous bracket on the minimum at all times. The only way to keep such a bracket is to update it using function (not derivative) information, with the central point in the bracketing triplet always that with the lowest function value. Therefore, the role of the derivatives can only be to help us choose new trial points within the bracket.

One school of thought is to “use everything you’ve got”: Compute a polynomial of relatively high order (cubic or above) that agrees with some number of previous function and derivative evaluations. For example, there is a unique cubic that agrees with function and derivative at two points, and one can jump to the interpolated minimum of that cubic (if there is a minimum within the bracket). Suggested by Davidon and others, formulas for this tactic are given in [1].

We like to be more conservative than this. Once superlinear convergence sets in, it hardly matters whether its order is moderately lower or higher. In practical problems that we have met, most function evaluations are spent in getting globally close enough to the minimum for superlinear convergence to commence. So we are more worried about all the funny “stiff” things that high-order polynomials can do (cf. Figure 3.0.1(b)), and about their sensitivities to roundoff error.

This leads us to use derivative information only as follows: The sign of the derivative at the central point of the bracketing triplet $( a , b , c )$ indicates uniquely whether the next test point should be taken in the interval $( a , b )$ or in the interval $( b , c )$ . The value of this derivative and of the derivative at the second-best-so-far point are extrapolated to zero by the secant method (inverse linear interpolation), which by itself is superlinear of order 1.618. (The golden mean again: See [1], p. 57.) We impose the same sort of restrictions on this new trial point as in Brent’s method. If the trial point must be rejected, we bisect the interval under scrutiny.

Yes, we are fuddy-duddies when it comes to making flamboyant use of derivative information in one-dimensional minimization. But we have met too many functions whose computed “derivatives” don’t integrate up to the function value and don’t accurately point the way to the minimum, usually because of roundoff errors, sometimes because of truncation error in the method of derivative evaluation.

You will see that the following routine is closely modeled on Brent in the previous section. One difference is in the input to the routine. Whereas Brent takes either a function or functor argument, Dbrent takes only a functor. The functor returns not only the function value, by overloading operator(), but also the derivative as the member function df. For example, here’s how you would code the function $x ^ { 2 }$ :

struct Funcd { Name Funcd is arbitrary. Doub operator() (const Doub x) { return x\*x; } Doub df(const Doub x) { return 2.0\*x; }   
};

To invoke Dbrent, you need statements like the following:

Dbrent dbrent;   
Funcd f;   
dbrent.bracket(a,b,f);   
xmin $\cdot ^ { = }$ dbrent.minimize(f);

The value of the function at the minimum is available in dbrent.fmin as usual. Here is the routine:

# mins.h

struct Dbrent : Bracketmethod {   
Brent’s method to find a minimum, modified to use derivatives. Doub xmin,fmin; const Doub tol; Dbrent(const Doub toll $^ { = 3 }$ .0e-8) : tol(toll) {} template <class T> Doub minimize(T &funcd) Given a functor funcd that computes a function and also its derivative function df, and given a bracketing triplet of abscissas ax, bx, cx [such that bx is between ax and cx, and f(bx) is less than both f(ax) and $\mathbf { f } \left( \mathsf { c x } \right) ]$ , this routine isolates the minimum to a fractional precision of about tol using a modification of Brent’s method that uses derivatives. The abscissa of the minimum is returned as xmin, and the minimum function value is returned as min, the returned function value. {

const Int ITMAX $\mathop {    }$ 100;

const Doub ZEPS $\equiv _ { . }$ numeric_limits<Doub>::epsilon()\*1.0e-3; Bool ok1,ok2; Will be used as flags for whether pro-Doub a,b, $\mathtt { d } \mathtt { = } 0$ .0,d1,d2,du,dv,dw,dx, $\mathtt { e } = 0$ .0; posed steps are acceptable or not. Doub fu,fv,fw,fx,olde,tol1,tol2,u,u1,u2,v,w,x,xm;

Comments following will point out only differences from the routine in Brent. Read   
that routine first.   
$\mathtt { a } =$ (ax < cx ? ax : cx);   
${ \mathrm { b } } \mathbf { = } \left( { \mathrm { a x } } \ > \ { \mathrm { c x } } \ ? \ { \mathrm { a x } } \ : \ { \mathrm { c x } } \right) ;$ ;   
$\scriptstyle \mathtt { X } = \mathtt { W } = \mathtt { V } = \mathtt { b } \mathtt { X }$ ;   
fw=fv=f $\mathbf { x } =$ funcd(x);   
dw=dv=dx=funcd.df(x); All our housekeeping chores are dou  
for (Int iter ${ = } 0$ ;iter<ITMAX;iter++) { bled by the necessity of moving xm=0.5\*(a+b); aorund derivative values as well tol1=tol\*abs(x)+ZEPS; as function values. tol2=2.0\*tol1; if (abs(x-xm) $< =$ (tol2-0.5\*(b-a))) { fmin=fx; return xmin $\mathbf { \Phi } _ { \cdot } = \mathbf { x }$ ; } if (abs(e) $>$ tol1) { d1=2.0\*(b-a); Initialize these d’s to an out-of-bracket ${ \tt d } 2 { = } { \tt d } 1$ ; value. if (dw $\downarrow =$ dx) ${ \mathrm { d } } 1 = \left( { \mathrm { w - x } } \right)$ \*dx/(dx-dw); Secant method with one point. if (dv $\mathbf { \Psi } : = \mathbf { \Psi } \mathrm { d } \mathbf { x } .$ ) $\mathrm { { d } 2 = \left( v - x \right) * \mathrm { { d } x / \left( \mathrm { { d } x - \mathrm { { d } v } } \right) } }$ ; And the other. Which of these two estimates of d shall we take? We will insist that they be within the bracket, and on the side pointed to by the derivative at $\mathbf { x }$ : $\mathtt { u 1 } \mathtt { = x } \mathtt { + d } 1$ ; $\mathtt { u } 2 \mathtt { = x } \mathtt { + d } 2$ ; ok1 $= ( \mathrm { a - u 1 } ) * ( \mathrm { u 1 - b } ) > 0 . 0$ && dx\*d1 $< = ~ 0 . 0$ ; $\mathrm { o k } 2 ~ = ~ ( \mathrm { a - u } 2 ) * ( \mathrm { u } 2 \mathrm { - } \mathrm { b } ) ~ > ~ 0 . 0$ && dx\*d2 $< = ~ 0 . 0$ ; olde $= _ { \ominus }$ ; Movement on the step before last. $\mathtt { e } = \mathtt { d }$ ; if (ok1 || ok2) { Take only an acceptable d, and if if (ok1 && ok2) both are acceptable, then take $\mathrm { d } \mathrm { = }$ (abs(d1) $<$ the smallest one.abs(d2) ? d1 : d2); else if (ok1) d=d1; else $\mathtt { d } \mathtt { = d } 2$ ; if (abs(d) $< =$ abs(0.5\*olde)) { u=x+d; if (u-a < tol2 || b-u < tol2) d=SIGN(tol1,xm-x); } else { Bisect, not golden section. $\mathsf { d } \mathsf { = } 0 . 5 \mathsf { * } \left( \mathsf { e } \mathsf { = } \left( \mathsf { d } \mathbf { x } \mathsf { \Sigma } \right) \mathsf { \Sigma } \right) \mathsf { = } \mathrm { ~ 0 ~ . 0 ~ \Sigma ~ \mathsf { \Sigma } \mathsf { ~ a } \mathrm { - } \mathbf { x } \mathrm { ~ : ~ } \mathsf { b } \mathrm { - } \mathbf { x } \mathsf { ) } \mathsf { ) ; } }$ Decide which segment by the sign of the derivative. } else { d=0.5\*( $\eleftarrow$ (dx >= 0.0 ? a-x : b-x)); } } else { d=0.5\*(e=(dx >= 0.0 ? a-x : b-x)); if (abs(d) $> =$ tol1) { $\mathtt { u } = \mathtt { x } + \mathtt { d }$ ; fu=funcd(u); } else { u=x+SIGN(tol1,d); fu=funcd(u); if (fu $>$ fx) 3 If the minimum step in the downhill fmin=fx; direction takes us uphill, then return xmin=x; we are done.

Now all the housekeeping, sigh.

} du=funcd.df(u); if (fu $< =$ fx) { if ( $\texttt { u } > = \texttt { x }$ ) $\mathtt { a } \mathtt { - } \mathtt { x }$ ; else $\mathtt { b } \mathtt { = x }$ ; mov3(v,fv,dv,w,fw,dw); mov3(w,fw,dw,x,fx,dx); mov3(x,fx,dx,u,fu,du); else { if (u < x) $\mathtt { a } = \mathtt { u }$ ; else $\mathtt { b } = \mathtt { u }$ ; if (fu $< =$ fw || $\textbf { \ w } = = \textbf { x }$ ) { mov3(v,fv,dv,w,fw,dw); mov3(w,fw,dw,u,fu,du); } else if (fu $<$ fv || v == x || v == w) { mov3(v,fv,dv,u,fu,du); } } } throw("Too many iterations in routine dbrent"); } };

# CITED REFERENCES AND FURTHER READING:

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), pp. 55; 454–458.[1]   
Brent, R.P. 1973, Algorithms for Minimization without Derivatives (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2002 (New York: Dover), p. 78.

# 10.5 Downhill Simplex Method in Multidimensions

With this section we begin consideration of multidimensional minimization, that is, finding the minimum of a function of more than one independent variable. This section stands apart from those that follow, however: All of the algorithms after this section will make explicit use of a one-dimensional minimization algorithm as a part of their computational strategy. This section implements an entirely selfcontained strategy, in which one-dimensional minimization does not figure.

The downhill simplex method is due to Nelder and Mead [1]. The method requires only function evaluations, not derivatives. It is not very efficient in terms of the number of function evaluations that it requires. Powell’s method (-10.7) or the DFP method with finite differences (-10.9) is almost surely faster in all likely applications. However, the downhill simplex method may frequently be the best method to use if the figure of merit is “get something working quickly” for a problem whose computational burden is small.

The method has a geometrical naturalness about it that makes it delightful to describe or work through:

A simplex is the geometrical figure consisting, in $N$ dimensions, of $N + 1$ points (or vertices) and all their interconnecting line segments, polygonal faces, etc. In two dimensions, a simplex is a triangle. In three dimensions, it is a tetrahedron, not necessarily the regular tetrahedron. (The simplex method of linear programming, described in $\ S 1 0 . 1 0$ , also makes use of the geometrical concept of a simplex. Otherwise it is completely unrelated to the algorithm that we are describing in this section.) In general we are only interested in simplexes that are nondegenerate, i.e., that enclose a finite inner $N$ -dimensional volume. If any point of a nondegenerate simplex is taken as the origin, then the $N$ other points define vector directions that span the $N$ -dimensional vector space.

In one-dimensional minimization, it was possible to bracket a minimum, so that the success of a subsequent isolation was guaranteed. Alas! There is no analogous procedure in multidimensional space. For multidimensional minimization, the best we can do is give our algorithm a starting guess, that is, an $N$ -vector of independent variables as the first point to try. The algorithm is then supposed to make its own way downhill through the unimaginable complexity of an $N$ -dimensional topography, until it encounters a (local, at least) minimum.

The downhill simplex method must be started not just with a single point, but with $N + 1$ points, defining an initial simplex. If you think of one of these points (it matters not which) as being your initial starting point $\mathbf { P _ { 0 } }$ , then you can take the other $N$ points to be

$$
\mathbf { P } _ { i } = \mathbf { P } _ { 0 } + \Delta \mathbf { e } _ { i }
$$

where the $\mathbf { e } _ { i }$ ’s are $N$ unit vectors, and where $\Delta$ is a constant that is your guess of the problem’s characteristic length scale. (Or, you could have different $\Delta _ { i }$ ’s for each vector direction.)

The downhill simplex method now takes a series of steps, most steps just moving the point of the simplex where the function is largest (“highest point”) through the opposite face of the simplex to a lower point. These steps are called reflections, and they are constructed to conserve the volume of the simplex (and hence maintain its nondegeneracy). When it can do so, the method expands the simplex in one or another direction to take larger steps. When it reaches a “valley floor,” the method contracts itself in the transverse direction and tries to ooze down the valley. If there is a situation where the simplex is trying to “pass through the eye of a needle,” it contracts itself in all directions, pulling itself in around its lowest (best) point. The routine name amoeba is intended to be descriptive of this kind of behavior; the basic moves are summarized in Figure 10.5.1.

Termination criteria can be delicate in any multidimensional minimization routine. Without bracketing, and with more than one independent variable, we no longer have the option of requiring a certain tolerance for a single independent variable. We typically can identify one “cycle” or “step” of our multidimensional algorithm. It is then possible to terminate when the vector distance moved in that step is fractionally smaller in magnitude than some tolerance tol. Alternatively, we could require that the decrease in the function value in the terminating step be fractionally smaller than some tolerance ftol. Note that while tol should not usually be smaller than the square root of the machine precision, it is perfectly appropriate to let ftol be of order the machine precision (or perhaps slightly larger so as not to be confused by roundoff).

Note well that either of the above criteria might be fooled by a single anomalous step that, for one reason or another, failed to get anywhere. Therefore, it is frequently a good idea to restart a multidimensional minimization routine at a point where it claims to have found a minimum. For this restart, you should reinitialize any ancillary input quantities. In the downhill simplex method, for example, you should reinitialize $N$ of the $N + 1$ vertices of the simplex again by equation (10.5.1), with $\mathbf { P } _ { 0 }$ being one of the vertices of the claimed minimum.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0008_pages_0491-0560/auto/images/628c51c22228232a1a3418549fc9eef7566cd8552f3a8dd5bc0f2d59350f9c2f.jpg)  
Figure 10.5.1. Possible outcomes for a step in the downhill simplex method. The simplex at the beginning of the step, here a tetrahedron, is shown, top. The simplex at the end of the step can be any one of (a) a reflection away from the high point, (b) a reflection and expansion away from the high point, (c) a contraction along one dimension from the high point, or (d) a contraction along all dimensions toward the low point. An appropriate sequence of such steps will always converge to a minimum of the function.

Restarts should never be very expensive; your algorithm did, after all, converge to the restart point once, and now you are starting the algorithm already there.

The routine below has three different user interfaces. The simplest requires you to supply the initial simplex as in equation (10.5.1):

Amoeba am(ftol);   
VecDoub point $=$ ...; Doub del $=$ ...;   
pmin am.minimize(point,del,func);

The value of the function at the minimum is available in am.fmin. Second, you can use equation (10.5.1) with a vector of increments $\Delta _ { i }$ :

VecDoub dels $=$ ...;   
pmin=am.minimize(point,dels,func);

Lastly, you can provide the simplex as an $( N + 1 ) \times N$ matrix whose rows are the coordinates of each vertex:

MatDoub $\mathrm { ~ p ~ } = \mathrm { ~ \cdot ~ } \cdot \mathrm { ~ }$ pmin $\cdot ^ { = }$ am.minimize(p,func);

Consider, then, our $N$ -dimensional amoeba:

# struct Amoeba {

Multidimensional minimization by the downhill simplex method of Nelder and Mead.

The number of function evaluations.

const Doub ftol;   
Int nfunc;   
Int mpts;   
Int ndim;   
Doub fmin;   
VecDoub y;   
MatDoub p; Function value at the minimum.   
Function values at the vertices of the simplex.   
Current simplex.

Amoeba(const Doub ftoll) : ftol(ftoll) {}

The constructor argument ftoll is the fractional convergence tolerance to be achieved in the function value (n.b.!).

template <class T>

VecDoub minimize(VecDoub_I &point, const Doub del, T &func)

Multidimensional minimization of the function or functor func $\mathbf { \Psi } ( \mathbf { x } )$ , where x[0..ndim-1] is a vector in ndim dimensions, by the downhill simplex method of Nelder and Mead. The initial simplex is specified as in equation (10.5.1) by a point[0..ndim-1] and a constant displacement del along each coordinate direction. Returned is the location of the minimum.

VecDoub dels(point.size(),del); return minimize(point,dels,func); } template <class T> VecDoub minimize(VecDoub_I &point, VecDoub_I &dels, T &func) Alternative interface that takes different displacements dels[0..ndim-1] in different directions for the initial simplex.

Int ndim=point.size();   
MatDoub pp(ndim $^ { + 1 }$ ,ndim);   
for (Int i=0;i<ndim+1;i++) { for (Int j=0;j<ndim;j++) pp[i][j]=point[j]; if (i !=0 ) pp[i][i-1] $+ =$ dels[i-1];   
1   
return minimize(pp,func);

template <class T> VecDoub minimize(MatDoub_I &pp, T &func)

Most general interface: initial simplex specified by the matrix pp[0..ndim][0..ndim-1]. Its ndim $^ { + 1 }$ rows are ndim-dimensional vectors that are the vertices of the starting simplex. {

const Int NMAX $\equiv$ 5000; Maximum allowed number of function evalua  
const Doub TINY $\sp { \prime } = 1$ .0e-10; tions.   
Int ihi,ilo,inhi;   
mpts=pp.nrows();   
ndim $_ { 1 } =$ pp.ncols();   
VecDoub psum(ndim),pmin(ndim),x(ndim);   
$\mathrm { { p } = }$ pp;   
y.resize(mpts);   
for (Int i=0;i<mpts; $\dot { \bf 1 } + +$ ) { for (Int j=0;j<ndim;j++) x[j] $= p$ [i][j]; y[i] $=$ func(x); } nfunc ${ = } 0$ ; get_psum(p,psum); for (;;) { ilo=0; First we must determine which point is the highest (worst), next-highest, and lowest (best), by looping over the points in the simplex. ihi $\mathit { \Pi } = \mathit { \Pi } \_ { \mathbb { Y } }$ [0]>y[1] ? (inhi $^ { = 1 }$ ,0) : (inhi $= 0$ ,1); for (Int $\scriptstyle \dot { 1 } = 0$ ;i<mpts; $\dot { \bf 1 } + +$ ) { if (y[i] $< =$ y[ilo]) ilo ${ \boldsymbol { \mathbf { \rho } } } _ { \ v { \mathbf { \rho } } } = \dot { \boldsymbol { \mathbf { \rho } } } _ { \perp }$ ; if (y[i] $>$ y[ihi]) { inhi $=$ ihi; ihi ${ \bf \Pi } = \dot { \bf 1 }$ ; } else if (y[i] $>$ y[inhi] && i $\downarrow =$ ihi) inhi ${ \tt = } \dot { \tt 1 }$ ; Doub rtol $^ { = 2 }$ .0\*abs(y[ihi]-y[ilo])/(abs(y[ihi]) $^ +$ abs(y[ilo])+TINY); Compute the fractional range from highest to lowest and return if satisfactory. if (rtol $<$ ftol) { If returning, put best point and value in slot 0. SWAP(y[0],y[ilo]); for (Int $\scriptstyle { \dot { \mathtt { 1 } } } = 0 $ ;i<ndim;i++) { SWAP(p[0][i],p[ilo][i]); pmin[i] $\tt = p$ [0][i]; fmin=y[0]; return pmin; if (nfunc $> =$ NMAX) throw("NMAX exceeded"); nfunc $+ = ~ 2$ ; Begin a new iteration. First extrapolate by a factor $^ { - 1 }$ through the face of the simplex across from the high point, i.e., reflect the simplex from the high point. Doub ytry=amotry(p,y,psum,ihi,-1.0,func); if (ytry $< =$ y[ilo]) Gives a result better than the best point, so try an additional extrapolation by a factor 2. ytry=amotry(p,y,psum,ihi,2.0,func); else if (ytry $> =$ y[inhi]) { The reflected point is worse than the second-highest, so look for an intermediate lower point, i.e., do a one-dimensional contraction. Doub ysave=y[ihi]; ytry=amotry(p,y,psum,ihi,0.5,func); if (ytry $> =$ ysave) { Can’t seem to get rid of that high point. for (Int $\mathtt { i } = 0$ ;i<mpts;i++) { Better contract around the lowest if (i $\downarrow =$ ilo) { (best) point. for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<ndim;j++) p[i][j]=psum[j] ${ = } 0$ .5\*(p[i][j]+p[ilo][j]); y[i]=func(psum); nfunc $+ =$ ndim; Keep track of function evaluations. get_psum(p,psum); Recompute psum. } else --nfunc; Correct the evaluation count. Go back for the test of doneness and the next iteration.   
inline void get_psum(MatDoub_I &p, VecDoub_O &psum)   
Utility function. for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<ndim;j++) { Doub sum $= 0 \ . 0$ ; for (Int $\scriptstyle \dot { 1 } = 0$ ;i<mpts; $\dot { \bf 1 } + +$ ) sum $+ =$ p[i][j]; psum[j] $=$ sum; } template <class T>   
Doub amotry(MatDoub_IO &p, VecDoub_O &y, VecDoub_IO &psum,   
const Int ihi, const Doub fac, T &func)   
Helper function: Extrapolates by a factor fac through the face of the simplex across from the high point, tries it, and replaces the high point if the new point is better.   
{

VecDoub ptry(ndim); Doub fac1 $\ l =$ (1.0-fac)/ndim; Doub fac2=fac1-fac; for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<ndim;j $^ { + + }$ ) ptry[j]=psum[j]\*fac1-p[ihi][j]\*fac2; Doub ytry=func(ptry); Evaluate the function at the trial point. if (ytry $<$ y[ihi]) { If it’s better than the highest, then replace the y[ihi]=ytry; highest. for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<ndim;j++) { psum[j] $+ =$ ptry[j]-p[ihi][j]; p[ihi][j] $=$ ptry[j]; } return ytry; } };

# CITED REFERENCES AND FURTHER READING:

Nelder, J.A., and Mead, R. 1965, “A Simplex Method for Function Minimization,” Computer Journal, vol.7, pp. 308-313.[1]   
Yarbro, L.A., and Deming, S.N. 1974, “Selection and Preprocessing of Factors for Simplex Optimization,” Analytica Chimica Acta, vol. 73, pp. 391–398.   
Jacoby, S.L.S, Kowalik, J.S., and Pizzo, J.T. 1972, Iterative Methods for Nonlinear Optimization Problems (Englewood Cliffs, NJ: Prentice-Hall).

# 10.6 Line Methods in Multidimensions

We know $( \ S 1 0 . 2 - \ S 1 0 . 4 )$ how to minimize a function of one variable. If we start at a point $\mathbf { P }$ in $N$ -dimensional space, and proceed from there in some vector direction n, then any function of $N$ variables $f ( \mathbf { P } )$ can be minimized along the line $\mathbf { n }$ by our one-dimensional methods. One can dream up various multidimensional minimization methods that consist of sequences of such line minimizations. Different methods will differ only by how, at each stage, they choose the next direction $\mathbf { n }$ to try. The minimization methods in the next two sections fall under this general schema of successive line minimizations. (The quasi-Newton algorithm in $\ S 1 0 . 9$ does not need very accurate line minimizations. Accordingly, it uses the approximate line minimization routine, lnsrch from $\ S 9 . 7 . 1 .$ )

In this section we provide the line minimization routine linmin as part of the base class Linemethod from which we will derive the minimization methods in the next two sections. These minimization routines regard linmin as a black-box subalgorithm, whose definition is

linmin: Given as input the vectors $\mathbf { P }$ and $\mathbf { n }$ , and the function $f$ , find the scalar $\lambda$ that minimizes $f ( \mathbf { P } +$ n/. Replace $\mathbf { P }$ by $\mathbf { P } + \lambda \mathbf { n }$ . Replace n by $\lambda \mathbf { n }$ . Done.

Since we will want to use linmin with methods whose choice of successive directions does not involve explicit computation of the function’s gradient, linmin itself cannot use gradient information. Later, in $\ S 1 0 . 8$ , we will consider a method that does use gradient information. Accordingly, there we provide a routine dlinmin that makes use of this information to reduce the total computational burden.

The obvious way to implement linmin is to use the methods of one-dimensional minimization described in $\ S 1 0 . 2 - \ S 1 0 . 4$ , but to rewrite the programs of those sections so that their bookkeeping is done on vector-valued points $\mathbf { P }$ (all lying along a given direction n) rather than scalar-valued abscissas $x$ . That straightforward task produces long routines densely populated with “for $( \mathrm { k } { = } 0 ; \mathrm { k } { < } \mathrm { n } ; \mathrm { k } { + } { + } ) ^ { 3 }$ loops.

As an alternative, we can simply reuse the one-dimensional minimization routines by constructing a functor F1dim, which gives the value of your function, say func, along the line going through the point $\mathtt { p }$ in the direction xi. The function linmin calls our familiar one-dimensional routine Brent (-10.4) and instructs it to minimize F1dim. The routine linmin communicates with F1dim “over the head” of Brent through the constructor, our usual $\mathrm { C } { + + }$ idiom.

# template <class T>

# struct Linemethod {

Base class for line-minimization algorithms. Provides the line-minimization routine linmin.

VecDoub p;   
VecDoub xi;   
T &func;   
Int n;   
Linemethod(T &funcc) : func(funcc) {}

Constructor argument is the user-supplied function or functor to be minimized.

# Doub linmin()

Line-minimization routine. Given an n-dimensional point $\mathtt { p } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ and an n-dimensional direction xi[0..n-1], moves and resets p to where the function or functor func(p) takes on a minimum along the direction xi from p, and replaces xi by the actual vector displacement that p was moved. Also returns the value of func at the returned location p. This is actually all accomplished by calling the routines bracket and minimize of Brent. {

Initial guess for brackets.

Doub ax,xx,xmin; $\mathtt { n } { = } \mathtt { p }$ .size(); F1dim<T> f1dim(p,xi,func); $\mathtt { a x } { = } 0 . 0$ ; $\tt x x { = } 1$ .0; Brent brent; brent.bracket(ax,xx,f1dim); xmin=brent.minimize(f1dim); for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) { xi[j] $\ast =$ xmin; p[j] $+ =$ xi[j]; return brent.fmin; } };

Construct the vector results to return.

template <class T>   
struct F1dim {   
Must accompany linmin in Linemethod. const VecDoub &p; const VecDoub &xi; Int n; T &func; VecDoub xt;

F1dim(VecDoub_I &pp, VecDoub_I &xii, T &funcc) : p(pp), xi(xii), n(pp.size()), func(funcc), xt(n) {} Constructor takes as inputs an n-dimensional point $\mathtt { p } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ and an n-dimensional direction xi[0..n-1] from linmin, as well as the function or functor that takes a vector argument. Doub operator() (const Doub x) Functor returning value of the given function along a one-dimensional line. { for (Int j=0;j<n;j++) xt[j]=p[j]+x\*xi[j]; return func(xt); } };

# 10.7 Direction Set (Powell's) Methods in Multidimensions

With a routine for line minimization in hand, you might think of this simple method for general multidimensional minimization: Take the unit vectors $\mathbf { e } _ { 0 } , \mathbf { e } _ { 1 } , \ldots$ $\mathbf { e } _ { N - 1 }$ as a set of directions. Using linmin, move along the first direction to its minimum, then from there along the second direction to its minimum, and so on, cycling through the whole set of directions as many times as necessary, until the function stops decreasing.

This simple method is actually not too bad for many functions. Even more interesting is why it is bad, i.e., very inefficient, for some other functions. Consider a function of two dimensions whose contour map (level lines) happens to define a long, narrow valley at some angle to the coordinate basis vectors (see Figure 10.7.1). Then the only way “down the length of the valley” going along the basis vectors at each stage is by a series of many tiny steps. More generally, in $N$ dimensions, if the function’s second derivatives are much larger in magnitude in some directions than in others, then many cycles through all $N$ basis vectors will be required in order to get anywhere. This condition is not all that unusual; according to Murphy’s Law, you should count on it.

Obviously what we need is a better set of directions than the $\mathbf { e } _ { i }$ ’s. All direction set methods consist of prescriptions for updating the set of directions as the method proceeds, attempting to come up with a set that either (i) includes some very good directions that will take us far along narrow valleys, or else (more subtly) (ii) includes some number of “noninterfering” directions with the special property that minimization along one is not “spoiled” by subsequent minimization along another, so that interminable cycling through the set of directions can be avoided.

# 10.7.1 Conjugate Directions

This concept of “noninterfering” directions, more conventionally called conjugate directions, is worth making mathematically explicit.

First, note that if we minimize a function along some direction $\mathbf { u }$ , then the gradient of the function must be perpendicular to $\mathbf { u }$ at the line minimum; if not, then there would still be a nonzero directional derivative along $\mathbf { u }$ .

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0008_pages_0491-0560/auto/images/0f95fd46687b8ee9b82ed10b3c5a3c1989a835a012a4116bcf8442cc15f8f43b.jpg)  
Figure 10.7.1. Successive minimizations along coordinate directions in a long, narrow “valley” (shown as contour lines). Unless the valley is optimally oriented, this method is extremely inefficient, taking many tiny steps to get to the minimum, crossing and re-crossing the principal axis.

Next take some particular point $\mathbf { P }$ as the origin of the coordinate system with coordinates $\mathbf { X }$ . Then any function $f$ can be approximated by its Taylor series

$$
{ \begin{array} { l } { f ( \mathbf { x } ) = f ( \mathbf { P } ) + \displaystyle \sum _ { i } { \frac { \partial f } { \partial x _ { i } } } x _ { i } + { \frac { 1 } { 2 } } \sum _ { i , j } { \frac { \partial ^ { 2 } f } { \partial x _ { i } \partial x _ { j } } } x _ { i } x _ { j } + \cdots } \\ { \approx c \textnormal { -- } \mathbf { b } \cdot \mathbf { x } \ + \ { \frac { 1 } { 2 } } \mathbf { x } \cdot \mathbf { A } \cdot \mathbf { x } } \end{array} }
$$

where

$$
c \equiv f ( \mathbf { P } ) \qquad \mathbf { b } \equiv - \nabla f | _ { \mathbf { P } } \qquad [ \mathbf { A } ] _ { i j } \equiv { \frac { \partial ^ { 2 } f } { \partial x _ { i } \partial x _ { j } } } { \bigg | } _ { \mathbf { P } }
$$

The matrix A whose components are the second partial derivative matrix of the function is called the Hessian matrix of the function at $\mathbf { P }$ .

In the approximation of (10.7.1), the gradient of $f$ is easily calculated as

$$
\nabla f = \mathbf { A } \cdot \mathbf { x } - \mathbf { b }
$$

(This implies that the gradient will vanish — the function will be at an extremum — at a value of $\mathbf { X }$ obtained by solving $\mathbf { A \cdot x } = \mathbf { b }$ . We will return to this idea in $\ S 1 0 . 9 ! \rrangle$ )

How does the gradient $\nabla f$ change as we move along some direction? Evidently

$$
\delta ( \nabla f ) = \mathbf { A } \cdot ( \delta \mathbf { x } )
$$

Suppose that we have moved along some direction $\mathbf { u }$ to a minimum and now propose to move along some new direction v. The condition that motion along $\mathbf { V }$ not spoil our minimization along $\mathbf { u }$ is just that the gradient stay perpendicular to $\mathbf { u }$ , i.e., that the change in the gradient be perpendicular to $\mathbf { u }$ . By equation (10.7.4) this is just

$$
0 = { \bf u } \cdot \delta ( \nabla f ) = { \bf u } \cdot { \bf A } \cdot { \bf v }
$$

When (10.7.5) holds for two vectors $\mathbf { u }$ and $\mathbf { V }$ , they are said to be conjugate. When the relation holds pairwise for all members of a set of vectors, they are said to be a conjugate set. If you do successive line minimizations of a function along a conjugate set of directions, then you don’t need to redo any of those directions (unless, of course, you spoil things by minimizing along a direction that they are not conjugate to).

A triumph for a direction set method is to come up with a set of $N$ linearly independent, mutually conjugate directions. Then, one pass of $N$ line minimizations will put it exactly at the minimum of a quadratic form like (10.7.1). For functions $f$ that are not exactly quadratic forms, it won’t be exactly at the minimum, but repeated cycles of $N$ line minimizations will in due course converge quadratically to the minimum.

# 10.7.2 Powell's Quadratically Convergent Method

Powell first discovered a direction set method that does produce $N$ mutually conjugate directions. Here is how it goes: Initialize the set of directions $\mathbf { u } _ { i }$ to the basis vectors,

$$
\mathbf { u } _ { i } = \mathbf { e } _ { i } \qquad i = 0 , \dots , N - 1
$$

Now repeat the following sequence of steps (“basic procedure”) until your function stops decreasing:

- Save your starting position as ${ \bf P _ { 0 } }$ .   
- For $i = 0 , \ldots , N - 1$ , move $\mathbf { P } _ { i }$ to the minimum along direction $\mathbf { u } _ { i }$ and call this point ${ \bf P } _ { i + 1 }$ .   
- For i D 0; : : : ; N  2, set ui ui C1.   
- Set ${ \bf u } _ { N - 1 }  { \bf P } _ { N } - { \bf P } _ { 0 }$ .   
- Move ${ \bf P } _ { N }$ to the minimum along direction $\mathbf { u } _ { N - 1 }$ and call this point $\mathbf { P } _ { 0 }$ .

Powell, in 1964, showed that, for a quadratic form like (10.7.1), $k$ iterations of the above basic procedure produce a set of directions $\mathbf { u } _ { i }$ whose last $k$ members are mutually conjugate. Therefore, $N$ iterations of the basic procedure, amounting to $N ( N + 1 )$ line minimizations in all, will exactly minimize a quadratic form. Brent [1] gives proofs of these statements in accessible form.

Unfortunately, there is a problem with Powell’s quadratically convergent algorithm. The procedure of throwing away, at each stage, ${ \bf u } _ { 0 }$ in favor of $\mathbf { P } _ { N } - \mathbf { P } _ { 0 }$ tends to produce sets of directions that “fold up on each other” and become linearly dependent. Once this happens, the procedure finds the minimum of the function $f$ only over a subspace of the full $N$ -dimensional case; in other words, it gives the wrong answer. Therefore, the algorithm must not be used in the form given above.

There are a number of ways to fix up the problem of linear dependence in Powell’s algorithm, among them:

1. You can reinitialize the set of directions $\mathbf { u } _ { i }$ to the basis vectors $\mathbf { e } _ { i }$ after every $N$ or $N + 1$ iterations of the basic procedure. This produces a serviceable method, which we commend to you if quadratic convergence is important for your application (i.e., if your functions are close to quadratic forms and if you desire high accuracy).

2. Brent points out that the set of directions can equally well be reset to the columns of any orthogonal matrix. Rather than throw away the information on conjugate directions already built up, he resets the direction set to calculated principal directions of the matrix A (which he gives a procedure for determining). The calculation is essentially a singular value decomposition algorithm (see $\ S 2 . 6 \AA$ . Brent has a number of other cute tricks up his sleeve, and his modification of Powell’s method is probably the best presently known. Consult [1] for a detailed description and listing of the program. Unfortunately it is rather too elaborate for us to include here.

3. You can give up the property of quadratic convergence in favor of a more heuristic scheme (due to Powell) that tries to find a few good directions along narrow valleys instead of $N$ necessarily conjugate directions. This is the method that we now implement. (It is also the version of Powell’s method given in Acton [2], from which parts of the following discussion are drawn.)

# 10.7.3 Discarding the Direction of Largest Decrease

The fox and the grapes: Now that we are going to give up the property of quadratic convergence, was it so important after all? That depends on the function that you are minimizing. Some applications produce functions with long, twisty valleys. Quadratic convergence is of no particular advantage to a program that must slalom down the length of a valley floor that twists one way and another (and another, and another, : : : — there are $N$ dimensions!). Along the long direction, a quadratically convergent method is trying to extrapolate to the minimum of a parabola that just isn’t (yet) there while the conjugacy of the $N - 1$ transverse directions keeps getting spoiled by the twists.

Sooner or later, however, we do arrive at an approximately ellipsoidal minimum (cf. equation 10.7.1 when b, the gradient, is zero). Then, depending on how much accuracy we require, a method with quadratic convergence can save us several times $N ^ { 2 }$ extra line minimizations, since quadratic convergence doubles the number of significant figures at each iteration.

The basic idea of our now-modified Powell’s method is still to take $\mathbf { P } _ { N } - \mathbf { P } _ { 0 }$ as a new direction; it is, after all, the average direction moved in after trying all $N$ possible directions. For a valley whose long direction is twisting slowly, this direction is likely to give us a good run along the new long direction. The change is to discard the old direction along which the function $f$ made its largest decrease. This seems paradoxical, since that direction was the best of the previous iteration. However, it is also likely to be a major component of the new direction that we are adding, so dropping it gives us the best chance of avoiding a buildup of linear dependence.

There are a couple of exceptions to this basic idea. Sometimes it is better not to add a new direction at all. Define

$$
f _ { 0 } \equiv f ( { \bf P } _ { 0 } ) \qquad f _ { N } \equiv f ( { \bf P } _ { N } ) \qquad f _ { E } \equiv f ( 2 { \bf P } _ { N } - { \bf P } _ { 0 } )
$$

Here $f _ { E }$ is the function value at an “extrapolated” point somewhat further along the proposed new direction. Also define $\Delta f$ to be the magnitude of the largest decrease along one particular direction of the present basic procedure iteration. ( $\Delta f$ is a positive number.) Then:

1. If $f _ { E } \ge f _ { 0 }$ , then keep the old set of directions for the next basic procedure, because the average direction $\mathbf { P } _ { N } - \mathbf { P } _ { 0 }$ is all played out.

2. If $2 \left( f _ { 0 } - 2 f _ { N } + f _ { E } \right) [ ( f _ { 0 } - f _ { N } ) - \Delta f ] ^ { 2 } \geq ( f _ { 0 } - f _ { E } ) ^ { 2 } \Delta f$ , then keep the old set of directions for the next basic procedure, because either (i) the decrease along the average direction was not primarily due to any single direction’s decrease, or (ii) there is a substantial second derivative along the average direction and we seem to be near to the bottom of its minimum.

The following routine implements Powell’s method in the version just described. In the routine, xi is the matrix whose columns are the set of directions $\mathbf { n } _ { i }$ ; otherwise the correspondence of notation should be self-evident. If the function to be minimized is provided as a functor Func

struct Func { Doub operator()(VecDoub_I &x); }; then the normal calling sequence for Powell looks something like this:

VecDoub $\mathrm { ~  ~ p ~ } = \mathrm { ~  ~ \cdot ~ } \cdot \mathrm { ~  ~ \cdot ~ }$   
Func func;   
Powell<Func> powell(func);   
p=powell.minimize(p); OK to overwrite initial guess.

The function value at the minimum is available as powell.fret.

If, on the other hand, the function to be minimized is provided as a normal $\mathrm { C } { + } { + }$ function,

Doub func(VecDoub_I &x); then the constructor call looks like this instead:

Powell<Doub (VecDoub_I &)> powell(func);

Note that the constructor takes an optional argument that specifies the function tolerance for the minimization.

template <class T>   
struct Powell : Linemethod<T>   
Multidimensional minimization by Powell’s method. Int iter; Doub fret; Value of the function at the minimum. using Linemethod<T>::func; Variables from a templated base class are not autousing Linemethod<T>::linmin; matically inherited. using Linemethod<T>::p; using Linemethod<T>::xi; const Doub ftol; Powell(T &func, const Doub ftoll $^ { = 3 }$ .0e-8) : Linemethod<T>(func), ftol(ftoll) {}

Constructor arguments are func, the function or functor to be minimized, and an optional argument ftoll, the fractional tolerance in the function value such that failure to decrease by more than this amount on one iteration signals doneness.

VecDoub minimize(VecDoub_I &pp)

Minimization of a function or functor n variables. Input consists of an initial starting point $\mathtt { p p } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ . The initial matrix ximat[0..n-1][0..n-1], whose columns contain the initial set of directions, is set to the n unit vectors. Returned is the best point found, at which point fret is the minimum function value and iter is the number of iterations taken.

{ Int n=pp.size(); MatDoub ximat $( \mathtt { n } , \mathtt { n } , 0 . 0 )$ ; for (Int $\scriptstyle { \dot { 1 } } = 0$ ;i<n; $\dot { \bf 1 } + +$ ) ximat[i][i] ${ = } 1$ .0; return minimize(pp,ximat);   
}

VecDoub minimize(VecDoub_I $\mathtt { \& p p }$ , MatDoub_IO &ximat)

Alternative interface: Input consists of the initial starting point $\mathtt { p p } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ and an initial matrix ximat[0..n-1][0..n-1], whose columns contain the initial set of directions. On output ximat is the then-current direction set.

const Int ITMAX $\mathop {    }$ 200; Maximum allowed iterations.   
const Doub TINY $\ l = 1$ .0e-25; A small number.   
Doub fptt;   
Int n=pp.size();   
$\mathtt { p - p p }$ ;   
VecDoub pt(n),ptt(n);   
xi.resize(n);   
fret=func(p);   
for (Int j=0;j<n;j++) pt[j] $= _ { \mathrm { p } }$ [j]; Save the initial point.   
for (iter ${ \tt = } 0$ ;;++iter) Doub fp=fret; Int ibig=0; Doub del ${ = } 0$ .0; Will be the biggest function decrease. for (Int i=0;i<n;i++) { In each iteration, loop over all directions in the set. for (Int $\scriptstyle { \dot { \mathbf { J } } } = 0 ;$ j<n;j++) xi[j] $=$ ximat[j][i]; Copy the direction, fptt $\equiv$ fret; fret=linmin(); minimize along it, if (fptt-fret $>$ del) { and record it if it is the largest decrease del=fptt-fret; so far. ibig=i+1; } 1 Here comes the termination criterion: if (2.0\*(fp-fret) $< =$ ftol\*(abs(fp)+abs(fret))+TINY) return p; } if (iter $= =$ ITMAX) throw("powell exceeding maximum iterations."); for (Int j=0;j<n;j++) { Construct the extrapolated point and the ptt[j]=2.0\*p[j]-pt[j]; average direction moved. Save the xi[j]=p[j]-pt[j]; old starting point. pt[j]=p[j]; } fptt=func(ptt); Function value at extrapolated point. if (fptt $<$ fp) { Doub $\mathtt { t } = 2$ .0\*(fp-2.0\*fret+fptt)\*SQR(fp-fret-del)-del\*SQR(fp-fptt); if $\mathit { \Phi } _ { \mathrm { ~ t ~ } } < \mathit { \Theta } _ { 0 . 0 } ,$ ) { fret=linmin(); Move to the minimum of the new direcfor (Int j=0;j<n;j $^ { + + }$ ) { tion, and save the new direction. ximat[j][ibig-1] $=$ ximat[j][n-1]; ximat[j][n-1] $=$ xi[j]; } } }   
}

# CITED REFERENCES AND FURTHER READING:

Brent, R.P. 1973, Algorithms for Minimization without Derivatives (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2002 (New York: Dover), Chapter 7.[1]

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), pp. 464–467.[2]   
Jacobs, D.A.H. (ed.) 1977, The State of the Art in Numerical Analysis (London: Academic Press), pp. 259–262.

# 10.8 Conjugate Gradient Methods in Multidimensions

Consider now the case where you are able to calculate, at a given $N$ -dimensional point $\mathbf { P }$ , not just the value of a function $f ( \mathbf { P } )$ but also the gradient (vector of first partial derivatives) $\nabla f ( \mathbf { P } )$ .

A rough counting argument will show how advantageous it is to use the gradient information: Suppose that the function $f$ is roughly approximated as a quadratic form, as above in equation (10.7.1),

$$
\begin{array} { r } { f ( { \bf x } ) \approx  { c } - { \bf b } \cdot { \bf x } \ + \ \frac { 1 } { 2 } \ { \bf x } \cdot { \bf A } \cdot { \bf x } } \end{array}
$$

Then the number of unknown parameters in $f$ is equal to the number of free parameters in $\mathbf { A }$ and $\mathbf { b }$ , which is $\textstyle { \frac { 1 } { 2 } } N ( N + 1 )$ , which we see to be of order $N ^ { 2 }$ . Changing any one of these parameters can move the location of the minimum. Therefore, we should not expect to be able to find the minimum until we have collected an equivalent information content, of order $N ^ { 2 }$ numbers.

In the direction set methods of $\ S 1 0 . 7$ , we collected the necessary information by making on the order of $N ^ { 2 }$ separate line minimizations, each requiring “a few” (but sometimes a big few!) function evaluations. Now, each evaluation of the gradient will bring us $N$ new components of information. If we use them wisely, we should need to make only of order $N$ separate line minimizations. That is in fact the case for the algorithms in this section and the next.

A factor of $N$ improvement in computational speed is not necessarily implied. As a rough estimate, we might imagine that the calculation of each component of the gradient takes about as long as evaluating the function itself. In that case there will be of order $N ^ { 2 }$ equivalent function evaluations both with and without gradient information. Even if the advantage is not of order $N$ , however, it is nevertheless quite substantial: (i) Each calculated component of the gradient will typically save not just one function evaluation, but a number of them, equivalent to, say, a whole line minimization. (ii) There is often a high degree of redundancy in the formulas for the various components of a function’s gradient. When this is so, especially when there is also redundancy with the calculation of the function, the calculation of the gradient may cost significantly less than $N$ function evaluations.

A common beginner’s error is to assume that any reasonable way of incorporating gradient information should be about as good as any other. This line of thought leads to the following not-very-good algorithm, the steepest descent method:

Steepest Descent: Start at a point ${ \bf P } _ { 0 }$ . As many times as needed, move from point $\mathbf { P } _ { i }$ to the point ${ \bf P } _ { i + 1 }$ by minimizing along the line from $\mathbf { P } _ { i }$ in the direction of the local downhill gradient $- \nabla f ( \mathbf { P } _ { i } )$ .

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0008_pages_0491-0560/auto/images/50c764c62eb96427d67b85f3291fd0ba39bc8f3cd274ed6af29dadb611ba857b.jpg)  
Figure 10.8.1. (a) Steepest descent method in a long, narrow “valley.” While more efficient than the strategy of Figure 10.7.1, steepest descent is nonetheless an inefficient strategy, taking many steps to reach the valley floor. (b) Magnified view of one step: A step starts off in the local gradient direction, perpendicular to the contour lines, and traverses a straight line until a local minimum is reached, where the traverse is parallel to the local contour lines.

The problem with the steepest descent method (which, incidentally, goes back to Cauchy), is similar to the problem that was shown in Figure 10.7.1. The method will perform many small steps in going down a long, narrow valley, even if the valley is a perfect quadratic form. You might have hoped that, say in two dimensions, your first step would take you to the valley floor, the second step directly down the long axis; but remember that the new gradient at the minimum point of any line minimization is perpendicular to the direction just traversed. Therefore, with the steepest descent method, you must make a right angle turn, which does not, in general, take you to the minimum. (See Figure 10.8.1.)

Just as in the discussion that led up to equation (10.7.5), we really want a way of proceeding not down the new gradient, but rather in a direction that is somehow constructed to be conjugate to the old gradient, and, insofar as possible, to all previous directions traversed. Methods that accomplish this construction are called conjugate gradient methods.

In $\ S 2 . 7$ we discussed the conjugate gradient method as a technique for solving linear algebraic equations by minimizing a quadratic form. That formalism can also be applied to the problem of minimizing a function approximated by the quadratic form (10.8.1). Recall that, starting with an arbitrary initial vector ${ \bf g } _ { 0 }$ and letting $\mathbf { h } _ { 0 } = \mathbf { g } _ { 0 }$ , the conjugate gradient method constructs two sequences of vectors from the recurrence

$$
\mathbf { g } _ { i + 1 } = \mathbf { g } _ { i } - \lambda _ { i } \mathbf { A } \cdot \mathbf { h } _ { i } \qquad \mathbf { h } _ { i + 1 } = \mathbf { g } _ { i + 1 } + \gamma _ { i } \mathbf { h } _ { i } \qquad i = 0 , 1 , 2 , \ldots
$$

The vectors satisfy the orthogonality and conjugacy conditions

$$
\mathbf { g } _ { i } \cdot \mathbf { g } _ { j } = 0 \qquad \mathbf { h } _ { i } \cdot \mathbf { A } \cdot \mathbf { h } _ { j } = 0 \qquad \mathbf { g } _ { i } \cdot \mathbf { h } _ { j } = 0 \qquad j < i
$$

The scalars $\lambda _ { i }$ and $\gamma _ { i }$ are given by

$$
\begin{array} { c } { \lambda _ { i } = \frac { \mathbf { g } _ { i } \cdot \mathbf { g } _ { i } } { \mathbf { h } _ { i } \cdot \mathbf { A } \cdot \mathbf { h } _ { i } } = \frac { \mathbf { g } _ { i } \cdot \mathbf { h } _ { i } } { \mathbf { h } _ { i } \cdot \mathbf { A } \cdot \mathbf { h } _ { i } } } \\ { \gamma _ { i } = \frac { \mathbf { g } _ { i + 1 } \cdot \mathbf { g } _ { i + 1 } } { \mathbf { g } _ { i } \cdot \mathbf { g } _ { i } } } \end{array}
$$

Equations $( 1 0 . 8 . 2 ) - ( 1 0 . 8 . 5 )$ are simply equations $( 2 . 7 . 3 2 ) - ( 2 . 7 . 3 5 )$ for a symmetric A in a new notation. (A self-contained derivation of these results in the context of function minimization is given by Polak [1].)

Now suppose that we knew the Hessian matrix A in equation (10.8.1). Then we could use the construction (10.8.2) to find successively conjugate directions $\mathbf { h } _ { i }$ along which to line-minimize. After $N$ such, we would efficiently have arrived at the minimum of the quadratic form. But we don’t know A.

Here is a remarkable theorem to save the day: Suppose we happen to have $\mathbf { g } _ { i } ~ = ~ - \nabla f ( \mathbf { P } _ { i } )$ , for some point $\mathbf { P } _ { i }$ , where $f$ is of the form (10.8.1). Suppose also that we proceed from $\mathbf { P } _ { i }$ along the direction $\mathbf { h } _ { i }$ to the local minimum of $f$ located at some point $\mathbf { P } _ { i + 1 }$ and then set $\mathbf { g } _ { i + 1 } = - \nabla f ( \mathbf { P } _ { i + 1 } )$ . Then, this $\mathbf { g } _ { i + 1 }$ is the same vector as would have been constructed by equation (10.8.2). (And we have constructed it without knowledge of A!)

Proof: By equation (10.7.3), $\mathbf { g } _ { i } = - \mathbf { A } \cdot \mathbf { P } _ { i } + \mathbf { b }$ and

$$
\mathbf { g } _ { i + 1 } = - \mathbf { A } \cdot ( \mathbf { P } _ { i } + \lambda \mathbf { h } _ { i } ) + \mathbf { b } = \mathbf { g } _ { i } - \lambda \mathbf { A } \cdot \mathbf { h } _ { i }
$$

with $\lambda$ chosen to take us to the line minimum. But at the line minimum $\mathbf { h } _ { i } \cdot \nabla f =$ $- \mathbf { h } _ { i } \cdot \mathbf { g } _ { i + 1 } = 0$ . This latter condition is easily combined with (10.8.6) to solve for $\lambda$ . The result is exactly the expression (10.8.4). But with this value of $\lambda$ , (10.8.6) is the same as (10.8.2), q.e.d.

We have, then, the basis of an algorithm that requires neither knowledge of the Hessian matrix A nor even the storage necessary to store such a matrix. A sequence of directions $\mathbf { h } _ { i }$ is constructed, using only line minimizations, evaluations of the gradient vector, and an auxiliary vector to store the latest in the sequence of $\mathbf { g }$ ’s.

The algorithm described so far is the original Fletcher-Reeves version of the conjugate gradient algorithm. Later, Polak and Ribiere introduced one tiny, but sometimes significant, change. They proposed using the form

$$
\gamma _ { i } = \frac { ( \mathbf { g } _ { i + 1 } - \mathbf { g } _ { i } ) \cdot \mathbf { g } _ { i + 1 } } { \mathbf { g } _ { i } \cdot \mathbf { g } _ { i } }
$$

instead of equation (10.8.5). “Wait,” you say, “aren’t they equal by the orthogonality conditions (10.8.3)?” They are equal for exact quadratic forms. In the real world, however, your function is not exactly a quadratic form. Arriving at the supposed minimum of the quadratic form, you may still need to proceed for another set of iterations. There is some evidence [2] that the Polak-Ribiere formula accomplishes the transition to further iterations more gracefully: When it runs out of steam, it tends to reset h to be down the local gradient, which is equivalent to beginning the conjugate gradient procedure anew.

The following routine implements the Polak-Ribiere variant, which we recommend; but changing one program line, as shown, will give you Fletcher-Reeves. The routine presumes the existence of a functor (not a function) that returns the function value by overloading operator() and also provides a function to set the vector gradient df $\left[ 0 \cdot \cdot \mathbf { n } ^ { - 1 } \right]$ evaluated at the input point p. Here’s an example for the function $x _ { 0 } ^ { 2 } + x _ { 1 } ^ { 2 }$ :

Name Funcd is arbitrary.

struct Funcd {Doub operator() (VecDoub_I &x){return x[0]\*x[0]+x[1]\*x[1];}void df(VecDoub_I &x, VecDoub_O &deriv){deriv[0] $^ { = 2 }$ . $0 * \mathbf { x }$ [0];deriv[1] $^ { = 2 }$ .0\*x[1];}  
};

To use frprmn, you need statements like the following:

Funcd funcd;   
Frprmn<Funcd> frprmn(funcd);   
VecDoub $\mathrm { ~ p ~ } = \mathrm { ~ \cdot ~ } \cdot \mathrm { ~ }$ ;   
p=frprmn.minimize(p); OK to overwrite initial guess.

The function value at the minimum is available as frprmn.fret. Note that the constructor takes an optional argument that specifies the function tolerance for the minimization.

The routine calls linmin to do the line minimizations. As already discussed, you may wish to use a modified version of linmin that uses Dbrent instead of Brent, i.e., that uses the gradient in doing the line minimizations. See note below (-10.8.1).

# template <class T>

struct Frprmn : Linemethod<T> {

Multidimensional minimization by the Fletcher-Reeves-Polak-Ribiere method.

Int iter;   
Doub fret; Value of the function at the minimum. using Linemethod<T>::func; Variables from a templated base class using Linemethod<T>::linmin; are not automatically inherited. using Linemethod<T>::p;   
using Linemethod<T>::xi;   
const Doub ftol;   
Frprmn(T &funcd, const Doub ftoll $^ { = 3 }$ .0e-8) : Linemethod<T>(funcd),   
ftol(ftoll) {}

Constructor arguments are funcd, the function or functor to be minimized, and an optional argument ftoll, the fractional tolerance in the function value such that failure to decrease by more than this amount on one iteration signals doneness.

VecDoub minimize(VecDoub_I &pp)

Given a starting point pp[0..n-1], performs the minimization on a function whose value and gradient are provided by a functor funcd (see text).

const Int ITMAX $\mathop {    }$ 200;   
const Doub EPS $^ { = 1 }$ .0e-18;   
const Doub GTOL $= 1$ .0e-8;   
Here ITMAX is the maximum allowed number of iterations; EPS is a small number to rectify the special case of converging to exactly zero function value; and GTOL is the convergence criterion for the zero gradient test. Doub gg,dgg;   
Int n=pp.size();   
p=pp;   
VecDoub g(n),h(n);

xi.resize(n); Doub fp=func(p); func.df(p,xi); for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) { g[j] $=$ -xi[j]; xi[j]=h[j]=g[j]; } for (Int its ${ = } 0$ ;its<ITMAX;its++) { Loop over iterations. iter $\underline { { \underline { { \mathbf { \Pi } } } } } = \mathbf { \partial }$ its; fret=linmin(); Next statement is one possible return: if (2.0\*abs(fret-fp) $< =$ ftol\*(abs(fret)+abs(fp)+EPS)) return p; fp=fret; func.df(p,xi); Doub test ${ = } 0$ .0; Test for convergence on zero gradient. Doub den=MAX(fp,1.0); for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) { Doub temp=abs(xi[j])\*MAX(abs(p[j]),1.0)/den; if (temp $>$ test) test $=$ temp; } if (test $<$ GTOL) return p; The other possible return. dgg=gg=0.0; for (Int j=0;j<n;j++) { gg $+ =$ g[j]\*g[j]; // dgg $+ =$ xi[j]\*xi[j]; This statement for Fletcher-Reeves. dgg $+ =$ (xi[j]+g[j])\*xi[j]; This statement for Polak-Ribiere. } if (gg == 0.0) Unlikely. If gradient is exactly zero, then return p; we are already done. Doub gam=dgg/gg; for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) { g[j] $=$ -xi[j]; xi[j] $\mathrm { \Gamma = h }$ [j]=g[j]+gam\*h[j]; } } throw("Too many iterations in frprmn"); } };

# 10.8.1 Note on Line Minimization Using Derivatives

Kindly reread $\ S 1 0 . 6$ . We here want to do the same thing, but using derivative information in performing the line minimization. Simply replace all occurrences of Linemethod in Frprmn with Dlinemethod. The routine Dlinemethod is exactly the same as Linemethod except that Brent is replaced by Dbrent and F1dim by Df1dim:

# template <class T>

# struct Dlinemethod {

Base class for line-minimization algorithms using derivative information. Provides the lineminimization routine linmin.

VecDoub p;   
VecDoub xi;   
T &func;   
Int n;   
Dlinemethod(T &funcc) : func(funcc) {}

Constructor argument is the user-supplied function or functor to be minimized.

Doub linmin()

Line-minimization routine. Given an n-dimensional point $\mathtt { p } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ and an n-dimensional direction xi[0..n-1], moves and resets p to where the function or functor func(p) takes on a minimum along the direction xi from p, and replaces xi by the actual vector displacement that p was moved. Also returns the value of func at the returned location p. All of this is actually accomplished by calling the routines bracket and minimize of Dbrent. {

Initial guess for brackets.

Doub ax,xx,xmin; $\mathrm { n } { = } _ { \mathrm { p } }$ .size(); Df1dim<T> df1dim(p,xi,func); ax=0.0; $\tt x x { = } 1$ .0; Dbrent dbrent; dbrent.bracket(ax,xx,df1dim); xmin=dbrent.minimize(df1dim); for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) { xi[j] $\ast =$ xmin; p[j] $+ =$ xi[j]; } return dbrent.fmin; }

Construct the vector results to return.

te struct Df1dim { Must accompany linmin in Dlinemethod. const VecDoub &p; const VecDoub &xi; Int n; T &funcd; VecDoub xt; VecDoub dft; Df1dim(VecDoub_I &pp, VecDoub_I &xii, T &funcdd) : p(pp), xi(xii), n(pp.size()), funcd(funcdd), xt(n), dft(n) {} Constructor takes as inputs an n-dimensional point p[0..n-1] and an n-dimensional direction xi[0..n-1] from linmin, as well as the functor funcd. Doub operator()(const Doub x) Functor returning value of the given function along a one-dimensional line. { for (Int j=0;j<n;j++) xt[j]=p[j]+x\*xi[j]; return funcd(xt); } Doub df(const Doub x) Returns the derivative along the line. { Doub df $\mathtt { 1 } = 0$ .0; funcd.df(xt,dft); Dbrent always evaluates the derivative at the for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<n;j++) same value as the function, so xt is undf1 $+ =$ dft[j]\*xi[j]; changed. return df1; } };

# CITED REFERENCES AND FURTHER READING:

Polak, E. 1971, Computational Methods in Optimization (New York: Academic Press), $\ S 2 . 3 . [ 1 ]$   
Jacobs, D.A.H. (ed.) 1977, The State of the Art in Numerical Analysis (London: Academic Press), Chapter III.1.7 (by K.W. Brodlie).[2]   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 8 . 7$ .

# 10.9 Quasi-Newton or Variable Metric Methods in Multidimensions

The goal of quasi-Newton methods, which are also called variable metric methods, is not different from the goal of conjugate gradient methods: to accumulate information from successive line minimizations so that $N$ such line minimizations lead to the exact minimum of a quadratic form in $N$ dimensions. In that case, the method will also be quadratically convergent for more general smooth functions.

Both quasi-Newton and conjugate gradient methods require that you are able to compute your function’s gradient, or first partial derivatives, at arbitrary points. The quasi-Newton approach differs from the conjugate gradient in the way that it stores and updates the information that is accumulated. Instead of requiring intermediate storage on the order of $N$ , the number of dimensions, it requires a matrix of size $N \times N$ . Generally, for any moderate $N$ , this hardly matters.

On the other hand, there is not, as far as we know, any overwhelming advantage that the quasi-Newton methods hold over the conjugate gradient techniques, except perhaps a historical one. Developed somewhat earlier, and more widely propagated, the quasi-Newton methods have by now developed a wider constituency of satisfied users. Likewise, some fancier implementations of quasi-Newton methods (going beyond the scope of this book; see below) have been developed to a greater level of sophistication on issues like the minimization of roundoff error, handling of special conditions, and so on.

Quasi-Newton methods come in two main flavors. One is the Davidon-Fletcher-Powell (DFP) algorithm (sometimes referred to as simply Fletcher-Powell). The other goes by the name Broyden-Fletcher-Goldfarb-Shanno (BFGS). The BFGS and DFP schemes differ only in details of their roundoff error, convergence tolerances, and similar “dirty” issues that are outside of our scope [1,2]. However, it has become generally recognized that, empirically, the BFGS scheme is superior in these details. We will implement BFGS in this section.

As before, we imagine that our arbitrary function $f ( \mathbf { x } )$ can be locally approximated by the quadratic form of equation (10.8.1). We don’t, however, have any information about the values of the quadratic form’s parameters A and $\mathbf { b }$ , except insofar as we can glean such information from our function evaluations and line minimizations.

The basic idea of the quasi-Newton method is to build up, iteratively, a good approximation to the inverse Hessian matrix $\mathbf { A } ^ { - 1 }$ , that is, to construct a sequence of matrices $\mathbf { H } _ { i }$ with the property

$$
\operatorname* { l i m } _ { i \to \infty } \mathbf { H } _ { i } = \mathbf { A } ^ { - 1 }
$$

Even better if the limit is achieved after $N$ iterations instead of $\infty$ .

The reason that these methods are called quasi-Newton can now be explained. Consider finding a minimum by using Newton’s method to search for a zero of the gradient of the function. Near the current point $\mathbf { X } _ { i }$ , we have to second order

$$
\begin{array} { r } { f ( \mathbf { x } ) = f ( \mathbf { x } _ { i } ) + ( \mathbf { x } - \mathbf { x } _ { i } ) \cdot \nabla f ( \mathbf { x } _ { i } ) + \frac { 1 } { 2 } ( \mathbf { x } - \mathbf { x } _ { i } ) \cdot \mathbf { A } \cdot ( \mathbf { x } - \mathbf { x } _ { i } ) } \end{array}
$$

$$
\nabla f ( \mathbf { x } ) = \nabla f ( \mathbf { x } _ { i } ) + \mathbf { A } \cdot ( \mathbf { x } - \mathbf { x } _ { i } )
$$

In Newton’s method we set $\nabla f ( \mathbf { x } ) = 0$ to determine the next iteration point:

$$
\mathbf { x } - \mathbf { x } _ { i } = - \mathbf { A } ^ { - 1 } \cdot \nabla f ( \mathbf { x } _ { i } )
$$

The left-hand side is the finite step we need to take to get to the exact minimum; the right-hand side is known once we have accumulated an accurate $\mathbf { H } \approx \mathbf { A } ^ { - 1 }$ .

The “quasi” in quasi-Newton is because we don’t use the actual Hessian matrix of $f$ , but instead use our current approximation of it. This is often better than using the true Hessian. We can understand this paradoxical result by considering the descent directions of $f$ at $\mathbf { X } _ { i }$ . These are the directions $\mathbf { p }$ along which $f$ decreases: $\nabla f \cdot \mathbf { p } < 0$ . For the Newton direction (10.9.4) to be a descent direction, we must have

$$
\nabla f ( \mathbf { x } _ { i } ) \cdot ( \mathbf { x } - \mathbf { x } _ { i } ) = - ( \mathbf { x } - \mathbf { x } _ { i } ) \cdot \mathbf { A } \cdot ( \mathbf { x } - \mathbf { x } _ { i } ) < 0
$$

which is true if $\mathbf { A }$ is positive-definite. In general, far from a minimum, we have no guarantee that the Hessian is positive-definite. Taking the actual Newton step with the real Hessian can move us to points where the function is increasing in value. The idea behind quasi-Newton methods is to start with a positive-definite, symmetric approximation to A (usually the unit matrix) and build up the approximating $\mathbf { H } _ { i }$ ’s in such a way that the matrix $\mathbf { H } _ { i }$ remains positive-definite and symmetric. Far from the minimum, this guarantees that we always move in a downhill direction. Close to the minimum, the updating formula approaches the true Hessian and we enjoy the quadratic convergence of Newton’s method.

When we are not close enough to the minimum, taking the full Newton step $\mathbf { p }$ even with a positive-definite A need not decrease the function; we may move too far for the quadratic approximation to be valid. All we are guaranteed is that initially $f$ decreases as we move in the Newton direction. Once again we can use the backtracking strategy described in $\ S 9 . 7$ to choose a step along the direction of the Newton step p, but not necessarily all the way.

We won’t rigorously derive the DFP algorithm for taking $\mathbf { H } _ { i }$ into $\mathbf { H } _ { i + 1 }$ ; you can consult [3] for clear derivations. Following Brodlie (in [2]), we will give the following heuristic motivation of the procedure.

Subtracting equation (10.9.4) at $\mathbf { X } _ { i + 1 }$ from that same equation at $\mathbf { X } _ { i }$ gives

$$
\mathbf { x } _ { i + 1 } - \mathbf { x } _ { i } = \mathbf { A } ^ { - 1 } \cdot ( \nabla f _ { i + 1 } - \nabla f _ { i } )
$$

where $\nabla f _ { j } \equiv \nabla f ( \mathbf { x } _ { j } )$ . Having made the step from $\mathbf { X } _ { i }$ to $\mathbf { X } _ { i + 1 }$ , we might reasonably want to require that the new approximation $\mathbf { H } _ { i + 1 }$ satisfy (10.9.6) as if it were actually $\mathbf { A } ^ { - 1 }$ , that is,

$$
\mathbf { x } _ { i + 1 } - \mathbf { x } _ { i } = \mathbf { H } _ { i + 1 } \cdot ( \nabla f _ { i + 1 } - \nabla f _ { i } )
$$

We might also imagine that the updating formula should be of the form $\mathbf { H } _ { i + 1 } \ =$ $\mathbf { H } _ { i } +$ correction.

What “objects” are around out of which to construct a correction term? Most notable are the two vectors $\mathbf { x } _ { i + 1 } - \mathbf { x } _ { i }$ and $\nabla f _ { i + 1 } - \nabla f _ { i }$ , and there is also $\mathbf { H } _ { i }$ . There are not infinitely many natural ways of making a matrix out of these objects, especially if (10.9.7) must hold! One such way, the $D F P$ updating formula, is

$$
\begin{array} { r l } & { \mathbf { H } _ { i + 1 } = \mathbf { H } _ { i } + \frac { \left( \mathbf { x } _ { i + 1 } - \mathbf { x } _ { i } \right) \otimes \left( \mathbf { x } _ { i + 1 } - \mathbf { x } _ { i } \right) } { \left( \mathbf { x } _ { i + 1 } - \mathbf { x } _ { i } \right) \cdot \left( \nabla f _ { i + 1 } - \nabla f _ { i } \right) } } \\ & { \quad \quad - \frac { \left[ \mathbf { H } _ { i } \cdot \left( \nabla f _ { i + 1 } - \nabla f _ { i } \right) \right] \otimes \left[ \mathbf { H } _ { i } \cdot \left( \nabla f _ { i + 1 } - \nabla f _ { i } \right) \right] } { \left( \nabla f _ { i + 1 } - \nabla f _ { i } \right) \cdot \mathbf { H } _ { i } \cdot \left( \nabla f _ { i + 1 } - \nabla f _ { i } \right) } } \end{array}
$$

where $\otimes$ denotes the “outer” or “direct” product of two vectors, a matrix: The ij component of $\textbf { u } \otimes \textbf { v }$ is $u _ { i } v _ { j }$ . (You might want to verify that 10.9.8 does indeed satisfy 10.9.7.)

The BFGS updating formula is exactly the same, but with one additional term,

$$
\cdots + [ ( \nabla f _ { i + 1 } - \nabla f _ { i } ) \cdot \mathbf { H } _ { i } \cdot ( \nabla f _ { i + 1 } - \nabla f _ { i } ) ] \ \mathbf { u } \otimes \mathbf { u }
$$

where $\mathbf { u }$ is defined as the vector

$$
\mathbf { u } \equiv { \frac { ( \mathbf { x } _ { i + 1 } - \mathbf { x } _ { i } ) } { ( \mathbf { x } _ { i + 1 } - \mathbf { x } _ { i } ) \cdot ( \nabla f _ { i + 1 } - \nabla f _ { i } ) } } - { \frac { \mathbf { H } _ { i } \cdot ( \nabla f _ { i + 1 } - \nabla f _ { i } ) } { ( \nabla f _ { i + 1 } - \nabla f _ { i } ) \cdot \mathbf { H } _ { i } \cdot ( \nabla f _ { i + 1 } - \nabla f _ { i } ) } }
$$

(You might also verify that this satisfies 10.9.7.)

You will have to take on faith — or else consult [3] for details of — the “deep” result that equation (10.9.8), with or without (10.9.9), does in fact converge to $\mathbf { A } ^ { - 1 }$ in $N$ steps, if $f$ is a quadratic form.

Here now is the routine dfpmin that implements the quasi-Newton method and uses lnsrch from $\ S 9 . 7$ . As mentioned at the end of newt in $\ S 9 . 7$ , this algorithm can fail if your variables are badly scaled. You must provide a functor with the same format as the one for frprmn in $\ S 1 0 . 8$ to calculate the function and its gradient.

# template <class T>

void dfpmin(VecDoub_IO &p, const Doub gtol, Int &iter, Doub &fret, T &funcd) Given a starting point $\mathtt { p } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ , the Broyden-Fletcher-Goldfarb-Shanno variant of Davidon-Fletcher-Powell minimization is performed on a function whose value and gradient are provided by a functor funcd (see text in $\ S 1 0 . 8 )$ . The convergence requirement on zeroing the gradient is input as gtol. Returned quantities are $\mathfrak { p } \left[ 0 \ldots \mathbf { n } ^ { - 1 } \right]$ (the location of the minimum), iter (the number of iterations that were performed), and fret (the minimum value of the function). The routine lnsrch is called to perform approximate line minimizations.   
{   
const Int ITMAX 200;   
const Doub EPS=numeric_limits<Doub>::epsilon();   
const Doub TOLX $^ { - 4 * }$ EPS,STPMX $\mathop {    }$ 100.0;   
Here ITMAX is the maximum allowed number of iterations; EPS is the machine precision;   
TOLX is the convergence criterion on $x$ values; and STPMX is the scaled maximum step length   
allowed in line searches.   
Bool check;   
Doub den,fac,fad,fae,fp,stpmax,sum $_ { = 0 }$ .0,sumdg,sumxi,temp,test;   
Int $\mathtt { n - p }$ .size();   
VecDoub dg(n),g(n),hdg(n),pnew(n),xi(n);   
MatDoub hessin ${ ( \mathrm { n , n } ) }$ ;   
fp=funcd(p); Calculate starting function value and gra  
funcd.df(p,g); dient,   
for (Int i=0;i<n;i++) { and initialize the inverse Hessian to the for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j $^ { + + }$ ) hessin[i][j]=0.0; unit matrix. hessin[i][i] $= 1$ .0; xi[i] $=$ -g[i]; Initial line direction. sum $+ =$ p[i]\*p[i];   
}   
stpmax=STPMX\*MAX(sqrt(sum),Doub(n));   
for (Int its ${ = } 0$ ;its<ITMAX;its $^ { + + }$ ) { Main loop over the iterations. iter=its; lnsrch(p,fp,g,xi,pnew,fret,stpmax,check,funcd); The new function evaluation occurs in lnsrch; save the function value in fp for the next line search. It is usually safe to ignore the value of check. fp=fret; for (Int i=0;i<n;i++) { xi[i] $=$ pnew[i]-p[i]; Update the line direction,

p[i]=pnew[i]; and the current point. } test=0.0; Test for convergence on $\Delta x$ . for (Int i=0;i<n;i++) { temp=abs(xi[i])/MAX(abs(p[i]),1.0); if (temp $>$ test) test=temp; if (test $<$ TOLX) return; for (Int i=0;i<n;i++) dg[i] $= _ { \mathrm { g } }$ [i]; Save the old gradient, funcd.df(p,g); and get the new gradient. test ${ = } 0$ .0; Test for convergence on zero gradient. den=MAX(fret,1.0); for (Int i=0;i<n;i++) { temp=abs(g[i])\*MAX(abs(p[i]),1.0)/den; if (temp $>$ test) test $=$ temp; if (test $<$ gtol) return; for (Int i=0;i<n;i++) Compute difference of gradients, dg[i] $= \tt g$ [i]-dg[i]; for (Int i=0;i<n; $\dot { 1 } + +$ ) { and difference times current matrix. hdg[i] $= 0 . 0$ ; for (Int j=0;j<n;j++) hdg[i] $+ =$ hessin[i][j]\*dg[j]; fac=fae $=$ sumdg=sumx $_ { = 0 }$ .0; Calculate dot products for the denomifor (Int i=0;i<n;i++) { nators. fac $+ =$ dg[i]\*xi[i]; fae $+ =$ dg[i]\*hdg[i]; sumdg $+ =$ SQR(dg[i]); sumxi $+ =$ SQR(xi[i]); } if (fac $>$ sqrt(EPS\*sumdg\*sumxi)) { Skip update if fac not sufficiently posifac $^ { = 1 }$ .0/fac; tive. fad $^ { = 1 }$ .0/fae; The vector that makes BFGS different from DFP: for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) dg[i] $=$ fac\*xi[i]-fad\*hdg[i]; for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n; $\dot { \bf 1 } + +$ ) { The BFGS updating formula: for (Int $\scriptstyle { \dot { \mathsf { J } } } = { \dot { \mathsf { I } } }$ ;j<n;j++) { hessin[i][j] $+ =$ fac\*xi[i]\*xi[j] -fad\*hdg[i]\*hdg[j]+fae\*dg[i]\*dg[j]; hessin[j][i]=hessin[i][j]; } } for (Int i=0;i<n;i++) { Now calculate the next direction to go, xi[i] ${ = } 0$ .0; for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) xi[i] $- =$ hessin[i][j]\*g[j]; } and go back for another iteration. ow("too many iterations in dfpmin");

Quasi-Newton methods like dfpmin work well with the approximate line minimization done by lnsrch. The routines Powell (-10.7) and Frprmn (-10.8), however, need more accurate line minimization, which is carried out by the routine linmin in Linemethod or Dlinemethod.

# 10.9.1 Quasi-Newton Methods Without Derivatives

In using Newton’s method to find a zero of a function in multidimensions, we saw in $\ S 9 . 7$ that one can use finite differences to calculate the partial derivatives instead of providing them analytically. Similarly, dfpmin very often succeeds when the gradient is calculated with finite differences. In our experience, this method often involves less total computation than one of the other methods that avoids analytic derivatives, such as Powell.

To use this idea, all you need to do is supply a suitable functor to dfpmin, which remains unchanged. Here is the code, which is very similar to that of Fdjac in $\ S 9 . 7$

template <class T>   
struct Funcd { Doub EPS; Set to approximate square root of the T &func; cision. Doub f; Funcd(T &funcc) : EPS(1.0e-8), func(funcc) {} Doub operator() (VecDoub_I &x) { return f=func(x); } void df(VecDoub_I &x, VecDoub_O &df) { Int $\mathbf { n } { = } \mathbf { x }$ .size(); VecDoub xh=x; Doub fold=f; for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) { Doub temp $= \mathrm { x }$ [j]; Doub ${ \bf h } =$ EPS\*abs(temp); if ( $\mathit { \Pi } _ { 1 } ~ = = ~ 0 . 0$ ) ${ \bf h } =$ EPS; xh[j] $=$ temp+h; Trick to reduce finite-precision error. h=xh[j]-temp; Doub fh=operator()(xh); xh[j] $=$ temp; df[j] $=$ (fh-fold)/h; } }   
};

# 10.9.2 Advanced Implementations of Variable Metric Methods

Although rare, it can conceivably happen that roundoff errors cause the matrix $\mathbf { H } _ { i }$ to become nearly singular or non-positive-definite. This can be serious, because the supposed search directions might then not lead downhill, and because nearly singular $\mathbf { H } _ { i }$ ’s tend to give subsequent $\mathbf { H } _ { i }$ ’s that are also nearly singular.

There is a simple fix for this rare problem, the same as was mentioned in $\ S 1 0 . 5$ : In case of any doubt, you should restart the algorithm at the claimed minimum point and see if it goes anywhere. Simple, but not very elegant. Modern implementations of quasi-Newton methods deal with the problem in a more sophisticated way.

Instead of building up an approximation to ${ \bf A } ^ { - 1 }$ , it is possible to build up an approximation of A itself. Then, instead of calculating the left-hand side of (10.9.4) directly, one solves the set of linear equations

$$
\mathbf { A } \cdot ( \mathbf { x } - \mathbf { x } _ { i } ) = - \nabla f ( \mathbf { x } _ { i } )
$$

At first glance this seems like a bad idea, since solving (10.9.11) is a process of order $N ^ { 3 } -$ and anyway, how does this help the roundoff problem? The trick is not to store A but rather a triangular decomposition of $\mathbf { A }$ , its Cholesky decomposition (cf. $\ S 2 . 9 \AA$ . The updating formula used for the Cholesky decomposition of $\mathbf { A }$ is of order $N ^ { 2 }$ and can be arranged to guarantee that the matrix remains positive-definite and nonsingular, even in the presence of finite roundoff. This method is due to Gill and Murray [1,2].

# CITED REFERENCES AND FURTHER READING:

Dennis, J.E., and Schnabel, R.B. 1983, Numerical Methods for Unconstrained Optimization and Nonlinear Equations; reprinted 1996 (Philadelphia: S.I.A.M.).[1]   
Jacobs, D.A.H. (ed.) 1977, The State of the Art in Numerical Analysis (London: Academic Press), Chapter III.1, $\ S 3 - \ S 6$ (by K. W. Brodlie).[2]   
Polak, E. 1971, Computational Methods in Optimization (New York: Academic Press), pp. 56ff.[3]   
Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), pp. 467–468.

# 10.10 Linear Programming: The Simplex Method

The subject of linear programming, sometimes called linear optimization, concerns itself with the following problem: For $n$ independent variables $x _ { 1 } , \ldots , x _ { n }$ minimize the function

$$
\zeta = c _ { 1 } x _ { 1 } + c _ { 2 } x _ { 2 } + \cdots + c _ { n } x _ { n }
$$

subject to the nonnegativity conditions

$$
x _ { 1 } \geq 0 , \quad x _ { 2 } \geq 0 , \quad \ldots \quad x _ { n } \geq 0
$$

and simultaneously subject to $m$ additional constraints of the form

$$
a _ { i 1 } x _ { 1 } + a _ { i 2 } x _ { 2 } + \cdots + a _ { i n } x _ { n } \leq b _ { i }
$$

or

$$
a _ { i 1 } x _ { 1 } + a _ { i 2 } x _ { 2 } + \cdots + a _ { i n } x _ { n } = b _ { i }
$$

Here $i = 1 , \ldots , m$ . Note that an inequality with ${ \bf a } \geq$ can be converted to $\mathrm { { \tt ~ 1 } } \leq \mathrm { { b y } \ m u l } .$ - tiplying by $^ { - 1 }$ . Some formulations of linear programming require you to write all the constraints with the $b$ ’s nonnegative and separately treat the $\geq$ and $\leq$ constraints. We will use the above formulation, with either sign of $b _ { i }$ , instead. However, it is still useful to refer to the inequalities with $b _ { i } \leq 0$ as $\stackrel {  } { \geq }$ inequalities” (which they would be with $b _ { i } \geq 0 \}$ ), since, as we shall see, they enter the problem in a different way from the $\leq$ inequalities.

There is no particular significance in the number of constraints $m$ being less than, equal to, or greater than the number of unknowns $n$ . Also, note that there is no special significance to minimizing $\zeta$ in equation (10.10.1): We can convert a maximizing problem to a minimizing problem by changing the signs of all the $c$ ’s. The solution $x _ { 1 } , \ldots , x _ { n }$ is the same, and the required maximum is the negative of the minimum $\zeta$ found.

A set of values $x _ { 1 } , \ldots , x _ { n }$ that satisfies the constraints $( 1 0 . 1 0 . 2 ) \textrm { -- } ( 1 0 . 1 0 . 4 )$ is called a feasible vector. The function that we are trying to minimize is called the objective function. The feasible vector that minimizes the objective function is called the optimal feasible vector. An optimal feasible vector can fail to exist for two distinct reasons: (i) There are no feasible vectors, i.e., the given constraints are incompatible, or (ii) there is no minimum, i.e., there is a direction in $n$ -space where one or more of the variables can be taken to infinity while still satisfying the constraints, giving an unbounded value for the objective function. Figure 10.10.1 summarizes some of the terminology thus far.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0008_pages_0491-0560/auto/images/29a6ebed72346b36c767d7647d6ea5f7cec2657c7914c948414076ff69c063cd.jpg)  
Figure 10.10.1. Basic concepts of linear programming. The case of only two independent variables, $x _ { 1 } , x _ { 2 }$ , is shown. The linear function $\xi$ , to be minimized, is represented by its contour lines. Nonnegativity constraints require $x _ { 1 }$ and $x _ { 2 }$ to be positive. Additional constraints may restrict the solution to regions (inequality constraints) or to surfaces of lower dimensionality (equality constraints). Feasible vectors satisfy all constraints. Feasible basic vectors also lie on the boundary of the allowed region. The simplex method steps among feasible basic vectors until the optimal feasible vector is found.

As you see, the subject of linear programming is surrounded by notational and terminological thickets. Both of these thorny defenses are lovingly cultivated by a coterie of stern acolytes who have devoted themselves to the field. Actually, the basic ideas of linear programming are quite simple. Avoiding the shrubbery, let’s elucidate the basics by means of a couple of specific examples; it should then be quite obvious how to generalize.

Why is linear programming so important? (i) Because “nonnegativity” is the usual constraint on any variable $x _ { i }$ that represents the tangible amount of some physical commodity, like guns, butter, dollars, units of vitamin E, food calories, kilowatt hours, mass, etc. Hence equation (10.10.2). (ii) Because one is often interested in additive (linear) limitations or bounds imposed by man or nature: minimum nutritional requirement, maximum affordable cost, maximum on available labor or capital, minimum tolerable level of voter approval, etc. Hence equations $( 1 0 . 1 0 . 3 ) - ( 1 0 . 1 0 . 4 )$ . (iii) Because the function that one wants to optimize may be linear, or else may at least be approximated by a linear function — since that is the problem that linear programming can solve. Hence equation (10.10.1). For a short, semipopular survey of linear programming applications, see Bland [1].

# 10.10.1 Fundamental Theorem of Linear Optimization

Imagine that we start with a full $n$ -dimensional space of candidate vectors. Then (in our mind’s eye, at least) we carve away the regions that are eliminated in turn by each imposed constraint. Since the constraints are linear, every boundary introduced by this process is a plane, or rather a hyperplane. Equality constraints of the form (10.10.4) force the feasible region onto hyperplanes of smaller dimension, while inequalities simply divide the then-feasible region into allowed and nonallowed pieces.

When all the constraints are imposed, either we are left with some feasible region or else there are no feasible vectors. Since the feasible region is bounded by hyperplanes, it is geometrically a kind of convex polyhedron or simplex (cf. $\ S 1 0 . 5 )$ . If there is a feasible region, can the optimal feasible vector be somewhere in its interior, away from the boundaries? No, because the objective function is linear. This means that it always has a nonzero vector gradient. This, in turn, means that we could always decrease the objective function by running down the gradient until we hit a boundary wall.

The boundary of any geometrical region has one less dimension than its interior. Therefore, we can now run down the gradient projected into the boundary wall until we reach an edge of that wall. We can then run down that edge, and so on, down through whatever number of dimensions, until we finally arrive at a point, a vertex of the original simplex. Since this point has all $n$ of its coordinates defined, it must be the solution of $n$ simultaneous equalities drawn from the original set of equalities and inequalities $( 1 0 . 1 0 . 2 ) - ( 1 0 . 1 0 . 4 )$ .

Points that are feasible vectors and that satisfy $n$ of the original constraints as equalities, including the nonnegativity constraints, are termed feasible basic vectors. If $n > m$ , then a feasible basic vector has at least $n - m$ of its components equal to zero, since at least that many of the constraints (10.10.2) will be needed to make up the total of $n$ . Put the other way, at most m components of a feasible basic vector are nonzero.

Put together the two preceding paragraphs and you have the Fundamental Theorem of Linear Optimization: If an optimal feasible vector exists, then there is a feasible basic vector that is optimal. (Didn’t we warn you about the terminological thicket?)

The importance of the fundamental theorem is that it reduces the optimization problem to a “combinatorial” problem, that of determining which $n$ constraints (out of the $m + n$ constraints in 10.10.2 – 10.10.4) should be satisfied by the optimal feasible vector. We have only to keep trying different combinations, and computing the objective function for each trial, until we find the best.

Doing this blindly would take halfway to forever. The simplex method, first published by Dantzig in 1948 (see [2]), is a way of organizing the procedure so that (i) a series of combinations is tried for which the objective function decreases at each step, and (ii) the optimal feasible vector is reached after a number of iterations that is almost always no larger than of order $m$ or $n$ , whichever is larger. An interesting mathematical sidelight is that this second property, although known empirically ever since the simplex method was devised, was not proved to be true until the 1982 work of Stephen Smale. (For a contemporary account, see [3].)

# 10.10.2 Writing the General Problem in Standard Form

There is a standard form for linear programming problems, and we have to learn how to write a general problem like $( 1 0 . 1 0 . 1 ) - ( 1 0 . 1 0 . 4 )$ in this standard form. For definiteness, consider the problem

$$
\mathrm { M i n i m i z e } \quad \zeta = - 4 0 x _ { 1 } - 6 0 x _ { 2 }
$$

with the $x$ ’s nonnegative and also with

$$
\begin{array} { r } { 2 x _ { 1 } + x _ { 2 } \le 7 0 } \\ { x _ { 1 } + x _ { 2 } \ge 4 0 } \\ { x _ { 1 } + 3 x _ { 2 } = 9 0 } \end{array}
$$

First, we rewrite the inequalities as equalities. We do this by adding to the problem so-called slack variables $x _ { n + 1 } , x _ { n + 2 } , . . . .$ In our example, equations (10.10.6) and (10.10.7) become

$$
\begin{array} { c l c r } { { 2 x _ { 1 } + x _ { 2 } + x _ { 3 } = 7 0 } } \\ { { - x _ { 1 } - x _ { 2 } + x _ { 4 } = - 4 0 } } \end{array}
$$

(A slack variable like $x _ { 4 }$ for ${ \mathrm { ~ a ~ } } \geq$ inequality is sometimes called a surplus variable.) Requiring the slack variables to be nonnegative makes these equalities equivalent to the original inequalities. Once they are introduced, you treat slack variables on an equal footing with the original variables $x _ { i }$ ; then, at the very end, you just ignore them. The simplex solution for each slack variable is simply the amount by which the original inequality is satisfied.

The key idea in the simplex method is to start with a feasible basic vector and make a sequence of exchanges between basic and nonbasic variables. At each step the vector stays feasible (satisfies the constraints), and the objective function decreases (or at least does not increase).

How do we find an initial feasible basic vector to start the procedure? Suppose that our example were changed so that equations (10.10.7) and (10.10.8) were both $\leq$ inequalities, like (10.10.6). Then, after introducing slack variables, we would have

$$
\begin{array} { r } { 2 x _ { 1 } + x _ { 2 } + x _ { 3 } = 7 0 } \\ { x _ { 1 } + x _ { 2 } + x _ { 4 } = 4 0 } \\ { x _ { 1 } + 3 x _ { 2 } + x _ { 5 } = 9 0 } \end{array}
$$

In this case it is easy to write down a feasible basic vector: Set the original variables $x _ { 1 }$ and $x _ { 2 }$ to zero and take $( x _ { 3 } , x _ { 4 } , x _ { 5 } ) = ( 7 0 , 4 0 , 9 0 )$ . Here $n = 2$ of the constraints, namely $x _ { 1 } \geq 0$ , $x _ { 2 } \geq 0$ , are satisfied as equalities, while $m = 3$ components of the feasible basic vector are nonzero. The variables $( x _ { 3 } , x _ { 4 } , x _ { 5 } )$ are called basic variables, while the variables that are zero, $( x _ { 1 } , x _ { 2 } )$ , are called nonbasic variables. Note that if we write equations $( 1 0 . 1 0 . 1 1 ) - ( 1 0 . 1 0 . 1 3 )$ as a $3 \times 5$ matrix equation, then the last three columns of the matrix, corresponding to the slack variables $( x _ { 3 } , x _ { 4 } , x _ { 5 } )$ , form a $3 \times 3$ unit matrix.

$\mathrm { ~ S o ~ } \leq$ constraints are easy. But how do we handle constraints like equations (10.10.7) and (10.10.8)? The trick is again to invent new variables called artificial variables. We rewrite equation (10.10.8) as

$$
x _ { 1 } + 3 x _ { 2 } + x _ { 5 } = 9 0
$$

Now equations (10.10.9), (10.10.10), and (10.10.14) are almost in the form to give us an easy initial feasible basic vector by setting $x _ { 1 } = x _ { 2 } = 0$ . The obstacle is equation (10.10.10), which would give a negative value for $x _ { 4 }$ . We have to precede the actual simplex procedure by a preliminary procedure, called phase one of the simplex method, to find an initial feasible vector. (The actual optimization is called phase two.)

In phase one, we replace our objective function (10.10.5) by a so-called auxiliary objective function,

$$
\zeta ^ { \prime } \equiv - x _ { 4 }
$$

We now perform the simplex method on the auxiliary objective function (10.10.15) with the constraints (10.10.9), (10.10.10), and (10.10.14), starting with the basis given by $x _ { 1 } = x _ { 2 } = 0$ . The variable $x _ { 4 }$ starts off negative (at $- 4 0$ ). Minimizing the function (10.10.15) drives $x _ { 4 }$ toward satisfying $x _ { 4 } \geq 0$ , the condition for feasibility. In fact, we don’t even have to solve phase one all the way to the exact minimum. As we do the exchanges between variables during this phase, we continually redefine the auxiliary objective function at each iteration to be minus the sum of all negative basic variables. As soon as all the basic variables are nonnegative, we are done with phase one.

And what if the first phase doesn’t drive the auxiliary objective function to a negative value (i.e., all basic variables nonnegative)? That signals that there is no initial feasible basic vector, i.e., that the constraints given to us are inconsistent among themselves. Report that fact, and you are done.

An artificial variable in an equality constraint is an example of a zero variable, a variable that must vanish in the optimal solution. Typically the way a zero variable gets to be zero is by being nonbasic in the optimal solution. So we can precede phase one with a “phase zero” in which we exchange each zero variable out of the basis.

One last piece of jargon: Slack and artificial variables are often called logical variables, to distinguish them from the original independent variables, which are sometimes called structural variables.

# 10.10.3 The Simplex Method: A Worked Example

The easiest way to describe the actual simplex procedure is with a worked example. We write the general linear programming problem in the following form: Minimize the objective function

$$
\zeta = \mathbf { c } \cdot \mathbf { x } = c _ { 1 } x _ { 1 } + c _ { 2 } x _ { 2 } + \cdots + c _ { n } x _ { n }
$$

subject to the constraints

$$
\mathbf { A \cdot x } = \mathbf { b }
$$

and

$$
x _ { i } \geq 0 , \qquad i = 1 , \ldots , n + m
$$

Here we assume that we started with an $m \times n$ matrix of constraint coefficients given by equations like (10.10.3) and (10.10.4). We then added slack variables to the inequality constraints and artificial variables to the equality constraints so that the constraint matrix is now the $m \times ( n + m )$ matrix A. The last $m$ columns form an $m \times m$ identity matrix. Note that the coefficients of the slack variables are taken to be $+ 1$ , so that an original $\geq$ inequality will have a negative right-hand side. For our example given in equations $( 1 0 . 1 0 . 5 ) - ( 1 0 . 1 0 . 8 )$ , transformed as in equations (10.10.9), (10.10.10), and (10.10.14), the matrix A has five columns:

$$
\mathbf { a } _ { 1 } = { \binom { 2 } { - 1 } } \quad \mathbf { a } _ { 2 } = { \binom { - 1 } { - 1 } } \quad \mathbf { a } _ { 3 } = { \binom { 1 } { 0 } } \quad \mathbf { a } _ { 4 } = { \binom { 0 } { 1 } } \quad \mathbf { a } _ { 5 } = { \binom { 0 } { 1 } }
$$

The right-hand side and the objective function coefficients are

$$
\mathbf { b } = \left( { - 4 0 } \atop 9 0 \right) \qquad \mathbf { c } = ( - 4 0 , - 6 0 , 0 , 0 , 0 ) ^ { T }
$$

We partition the matrix A into two submatrices,

$$
\mathbf { A } = \left[ \mathbf { A } _ { B } \mid \mathbf { A } _ { N } \right]
$$

where we have permuted the columns corresponding to the basic variables to be in $\mathbf { A } _ { B }$ , while the nonbasic columns are in $\mathbf { A } _ { N }$ . In our example, the initial basic variables are $( x _ { 3 } , x _ { 4 } , x _ { 5 } )$ and the initial basis $\mathbf { A } _ { B }$ is the unit matrix composed of the last three columns of A, $\mathbf { a } _ { 3 }$ , $\mathbf { a } _ { 4 }$ and $\mathbf { a } _ { 5 }$ . A basic solution of $\mathbf { A } \cdot \mathbf { x } = \mathbf { b }$ consists of a set of basic and nonbasic variables $\left[ { \bf x } _ { B } \mid { \bf x } _ { N } \right]$ with $\mathbf { x } _ { N } = 0$ . In our example, initially ${ \bf x } _ { N } = ( x _ { 1 } , x _ { 2 } ) = 0$ . The basic solution satisfies ${ \bf A } _ { B } \cdot { \bf x } _ { B } = { \bf b }$ , or $\mathbf { x } _ { B } = \mathbf { A } _ { B } ^ { - 1 } \cdot \mathbf { b }$ .

To derive the simplex method, we need one simple equation: how a basic vector changes as a nonbasic variable (i.e., one that is zero) becomes nonzero. This corresponds to starting at a vertex of the simplex and sliding along an edge toward another vertex. Suppose the variable $x _ { k }$ is the one increasing from zero. The constraint equation $\mathbf { A } \cdot \mathbf { x } = \mathbf { A } _ { B } \cdot \mathbf { x } _ { B } = \mathbf { b }$ becomes

$$
\mathbf { A } _ { B } \mathbf { x } _ { B } ^ { \prime } + \mathbf { a } _ { k } x _ { k } = \mathbf { b }
$$

since only $x _ { k }$ is nonzero among the nonbasic variables. Multiplying this equation by $\mathbf { A } _ { B } ^ { - 1 }$ gives

$$
\mathbf { x } _ { B } ^ { \prime } = \mathbf { A } _ { B } ^ { - 1 } \cdot \mathbf { b } - x _ { k } \mathbf { A } _ { B } ^ { - 1 } \cdot \mathbf { a } _ { k } = \mathbf { x } _ { B } - x _ { k } \mathbf { A } _ { B } ^ { - 1 } \cdot \mathbf { a } _ { k }
$$

The first application of equation (10.10.23) is to the idea of a reduced cost. The coefficient $c _ { i }$ in the objective function (10.10.16) is sometimes called the cost of variable $x _ { i }$ , because it represents the cost of having $x _ { i }$ amount of quantity $i$ in the objective function. The simplex method requires instead the cost of changing a variable that is zero (not in the basis) to a nonzero value. If the initial value of the objective function is $\mathbf { c } \cdot \mathbf { x } _ { B } = \mathbf { c } _ { B } \cdot \mathbf { x } _ { B }$ and the final value is $\mathbf { c } \cdot ( \mathbf { x } _ { B } ^ { \prime } + x _ { k } \mathbf { e } _ { k } )$ , where $\mathbf { e } _ { k }$ is a unit vector, then using equation (10.10.23) you find that the difference is $x _ { k } u _ { k }$ where the reduced cost of $x _ { k }$ is given by

$$
u _ { k } = c _ { k } - \mathbf { a } _ { k } \cdot \mathbf { y } , \qquad \mathbf { y } \equiv ( \mathbf { A } _ { B } ^ { - 1 } ) ^ { T } \cdot \mathbf { c } _ { B }
$$

Note that if $u _ { k } \ < \ 0$ , you can make the value of the objective function smaller by bringing $x _ { k }$ into the basis (making it nonzero).

The simplex procedure consists of the following steps:

1. Find a feasible basis (phase 1)   
2. Compute the reduced costs (10.10.24) for all $x _ { k }$ not in the basis.   
3. If $u _ { k } \geq 0$ for all $k$ , the solution is optimal: No exchange will improve things. Otherwise, choose $k$ corresponding to the most negative $u _ { k }$ as the entering column.   
4. Choose the leaving column $i$ from the minimum ratio test (motivated below): Compute

$$
\mathbf { x } _ { B } = \mathbf { A } _ { B } ^ { - 1 } \cdot \mathbf { b } , \qquad \mathbf { w } = \mathbf { A } _ { B } ^ { - 1 } \cdot \mathbf { a } _ { k }
$$

For each component $w _ { i } ~ > ~ 0$ , compute the ratio $x _ { B } ^ { i } / w _ { i }$ . Choose $i$ that corresponds to the smallest such ratio. (If no $w _ { i } ~ > ~ 0$ , the objective function is unbounded. Exit and report this.)

5. Exchange columns $i$ and $k$ and go back to step 2.

The minimum ratio test is the second application of equation (10.10.23), which can be written as

$$
( x _ { B } ^ { i } ) ^ { \prime } = x _ { B } ^ { i } - x _ { k } w _ { i }
$$

where $w _ { i }$ is defined in equation (10.10.25). For each $w _ { i } > 0$ , $x _ { B } ^ { i }$ decreases as $x _ { k }$ increases from zero. The minimum ratio test selects the $i$ corresponding to the first $x _ { B } ^ { i }$ to hit zero, while the other basis variables are still positive. The idea is to allow $x _ { k }$ to be as big as possible so that the objective function is reduced as much as possible by bringing it into the basis.

Let’s see how this applies to our example. We start with phase zero, where we remove the zero variable $x _ { 5 }$ from the basis. Suppose we choose $x _ { 2 }$ to be the incoming variable $x _ { 1 }$ would work fine, too). Using $x _ { 2 }$ , we find for the new basis and its inverse

$$
\mathbf { A } _ { B } = \left( { \begin{array} { c c c } { 1 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { - 1 } \\ { 0 } & { 0 } & { 3 } \end{array} } \right) \qquad \mathbf { A } _ { B } ^ { - 1 } = \left( { \begin{array} { c c c } { 1 } & { 0 } & { - { \frac { 1 } { 3 } } } \\ { 0 } & { 1 } & { { \frac { 1 } { 3 } } } \\ { 0 } & { 0 } & { { \frac { 1 } { 3 } } } \end{array} } \right)
$$

The new basic solution is

$$
\mathbf { x } _ { B } = { \binom { x _ { 3 } } { x _ { 4 } } } = \mathbf { A } _ { B } ^ { - 1 } \cdot \mathbf { b } = { \binom { 4 0 } { - 1 0 } }
$$

The solution (10.10.28) is not feasible because $x _ { 4 }$ is negative. We enter phase one, with $\zeta ^ { \prime } = \overline { { \mathbf { c } } } \cdot \mathbf { x } = - x _ { 4 }$ , i.e.,

$$
\overline { { \mathbf { c } } } _ { B } = \binom { 0 } { - 1 }
$$

Here the order of elements corresponds to the order $( x _ { 3 } , x _ { 4 } , x _ { 2 } )$ for the basic variables. We compute the reduced costs from equation (10.10.24). Only $k \ = \ 1$ is relevant, since $x _ { 5 }$ is never allowed to re-enter the basis (zero variable). We find

$$
\begin{array} { r } { u _ { 1 } = - \mathbf { a } _ { 1 } \cdot ( \mathbf { A } _ { B } ^ { - 1 } ) ^ { T } \cdot \overline { { \mathbf { c } } } _ { B } = - \frac { 2 } { 3 } } \end{array}
$$

which is negative, confirming that $x _ { 1 }$ should enter. For the minimum ratio test to determine which variable leaves, we need the quantity

$$
\mathbf { A } _ { B } ^ { - 1 } \cdot \mathbf { a } _ { 1 } = { \binom { \frac { 5 } { 3 } } { - { \frac { 2 } { 3 } } } }
$$

So the ratios of the elements in equation (10.10.28) to those in equation (10.10. are

$$
{ \frac { 4 0 } { 5 / 3 } } = 2 4 , \qquad { \frac { - 1 0 } { - 2 / 3 } } = 1 5 , \qquad { \frac { 3 0 } { 1 / 3 } } = 9 0
$$

The middle ratio is the minimum, so $x _ { 4 }$ goes out. (Note that in phase one we relax the requirement that $w _ { i } > 0$ , since we haven’t yet made all the variables nonnegative.)

Now the basic variables are 0 1 $\left( { { x } _ { 3 } } , { { x } _ { 1 } } , { { x } _ { 2 } } \right)$ . Proceeding as before, we find0 1

and

$$
\mathbf { A } _ { B } = \left( { \begin{array} { c c c } { 1 } & { 2 } & { 1 } \\ { 0 } & { - 1 } & { - 1 } \\ { 0 } & { 1 } & { 3 } \end{array} } \right) \qquad \mathbf { A } _ { B } ^ { - 1 } = \left( { \begin{array} { c c c } { 1 } & { { \frac { 5 } { 2 } } ^ { \sim } } & { { \frac { 1 } { 2 } } } \\ { 0 } & { - { \frac { 3 } { 2 } } } & { - { \frac { 1 } { 2 } } } \\ { 0 } & { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \end{array} } \right)
$$

$$
\mathbf { x } _ { B } = { \binom { x _ { 3 } } { x _ { 1 } } } = \mathbf { A } _ { B } ^ { - 1 } \cdot \mathbf { b } = { \binom { 1 5 } { 1 5 } }
$$

All the variables are positive, so the basis is feasible and we enter phase two, with $\mathbf { c } _ { B } ~ = ~ ( 0 , - 4 0 , - 6 0 ) ^ { \bar { T } }$ . We find the reduced cost $u _ { 4 } = - 3 0$ , so $x _ { 4 }$ re-enters the basis. The minimum ratio test (10.10.25) gives a minimum for the term involving $x _ { 3 }$ , so the next basis is $( x _ { 4 } , x _ { 1 } , x _ { 2 } )$ . The basic solution turns out to be .6; 24; 22/. When we compute the reduced cost $u _ { 3 }$ for this basis, it is positive, so we are done. The minimum occurs at $x _ { 1 } = 2 4$ , $x _ { 2 } = 2 2$ , and the minimum value, obtained by substitution in the objective function, is $- 2 2 8 0$ . The meaning of $x _ { 4 } ~ = ~ 6$ is that the inequality (10.10.7) is satisfied by 6. The other two constraints are satisfied as equalities.

The graphical interpretation of the solution procedure is shown in Figure 10.10.2. The initial basic vector is at the origin. We first proceed to the vertex $A$ , which puts us on the line where the equality (10.10.8) is satisfied. This is not a feasible point, since we are on the wrong side of the line $Y$ . So we move along the line $X$ to the vertex $B$ , which is now feasible. Finally we move to vertex $C$ , which is the minimum value of the objective function.

# 10.10.4 Degeneracy

Nonbasic variables in a basic feasible solution are all zero. If any basic variable is zero, we say the basis is degenerate. Geometrically, this situation corresponds in $n$ dimensions to having more than $n$ hyperplanes intersect at a vertex. Degeneracy can cause problems in the simplex method. Consider the simple case when three lines intersect at a point in two dimensions. Only two of the lines are necessary to define the vertex. When the leaving variable is chosen, it can correspond to the third direction at the vertex. On making this change in the basis, the objective function doesn’t improve. You can see this algebraically from equation (10.10.26): If $x _ { B } ^ { i } = 0$ and $w ^ { i } > 0$ , then a step size of zero is required for the new variable $x _ { k }$ . Clearly special measures need to be taken.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0008_pages_0491-0560/auto/images/524671d61b195e00e9f7387d866eb729ebc5c6be2c6d86bed540c357d57b2681.jpg)  
Figure 10.10.2. Graphical interpretation of the simplex solution of the problem $( 1 0 . 1 0 . 5 ) - ( 1 0 . 1 0 . 8 )$ . The initial basic vector is at the origin $o$ . To satisfy the equality (10.10.8), the first step moves to $A$ , on the line $X$ . This is not yet a feasible point, since it is on the wrong side of the line $Y$ . The next move is to $B$ , which is feasible. We enter phase two, and find that we can reduce the objective function by moving to $C$ . No further moves are possible, so we are done. Note that the figure is really the projection of a five-dimensional simplex onto the $x _ { 1 } - x _ { 2 }$ plane.

Degeneracy allows the possibility of cycling, where you keep exchanging the same set of vectors in and out of the basis without making any progress. In practice, however, cycling is almost never a problem. More common in very degenerate problems is stalling, where you spend a long time making exchanges before finally leaving the vertex.

# 10.10.5 Sparseness and Stability

If you examine the operations carried out during each simplex step, you see that a key ingredient is to solve equations of the form $\mathbf { A } _ { B } \cdot \mathbf { x } = \mathbf { b }$ and similar equations with $\mathbf { A } _ { B } ^ { T }$ . We know that a good method for doing this, absent other considerations, is to use the $L U$ decomposition of $\mathbf { A } _ { B }$ (cf. $\ S 2 . 3 )$ , since we can use partial pivoting to maintain stability. Decomposing $\mathbf { A } _ { B }$ afresh each step is expensive, but since successive bases differ only by the replacement of a single column, one can use techniques analogous to the Sherman-Morrison formula (-2.7) to update $\mathbf { L }$ and $\mathbf { U }$ .

However, most linear programming problems that occur in practice have a constraint matrix A that is very sparse. It is crucial to take advantage of this sparseness in the linear algebra procedures that make up each simplex step, since real-life problems can involve many thousands or even millions of constraints and variables. Standard $L U$ decomposition with partial pivoting to maintain stability is not desirable, because it leads to excessive fill-in, that is, the generation of nonzero matrix elements where there were zeros before. Instead, one chooses the pivot element by a trade-off between stability and sparsity. A popular strategy is based on the Markowitz criterion [4]. Here the pivot is a nonzero with the smallest product of the number of other nonzeros in its row and its column. Empirically, the Markowitz criterion works about as well as any other general strategy for minimizing fill-in. In linear programming applications, one also generally needs to impose some kind of stability criterion. In threshold partial pivoting, no pivot is less than $\alpha$ times the largest element in its row, where $\alpha$ is a parameter between zero and one. A typical value is $\alpha \sim 0 . 1$ ; $\alpha = 1$ gives straight partial pivoting.

The first stable updating procedure for sparse $L U$ decomposition was given by Bartels and Golub [5,6]. This procedure updates $\mathbf { L }$ and $\mathbf { U }$ when a column is replaced in $\mathbf { A } _ { B }$ . A good sparse $L U$ algorithm that includes the Bartels-Golub update is that of [7]. It is freely available in the software package LUSOL as part of [8], and we use it in our pedagogical implementation described below.

There are newer methods for the $L U$ decomposition and the update procedure. According to [9], the best of these is probably that of [10].

# 10.10.6 State-of-the-Art Simplex Codes

A high-quality implementation of the simplex method will have a number of features that we have not discussed so far.

- It will implement more than one variant of the simplex method. In addition to the algorithm we have described, the primal algorithm, it will typically also implement the so-called dual algorithm (duality is discussed in $\ S 1 0 . 1 1 \rangle$ . The number of iterations can be significantly reduced by the appropriate use of more than one algorithm.   
- It will accept multiple input formats for the specification of the problem, with suitable error checking.   
- It will preprocess the problem, with the aim of reducing its size and improving its numerical properties. Many complex problems are inadvertently specified in reducible form.   
- It will have multiple options for scaling the problem. As with solving linear equations, no universal scaling algorithm is known for linear programming.   
- It will have multiple options for starting the iteration, including several procedures for phase 1.   
- It will have several pricing strategies (procedures for selecting the incoming variable). These go by names like multiple pricing, Devex, and steepest edge.   
- It will have multiple pivot methods (variants of the ratio test) for the outgoing variable.   
- It will handle bounded variables, that is, variables that satisfy a requirement $l _ { i } \le x _ { i } \le u _ { i }$ instead of $x _ { i } \geq 0$ . It is possible to handle such bounds using slack variables, but that increases the size of the matrix A. A slight generalization of the algorithm we have described allows you to handle bounded variables directly.   
- It will have efficient sparse matrix algorithms.

All these issues are thoroughly discussed in [9].

There are several excellent public domain simplex implementations that incorporate most of the above items. These include CLP [11], GLPK [12] and lp solve [8]. If you are planning to do any serious LP solving, you should definitely explore these options. It may even be worthwhile to invest in a commercial LP solver. For more information on all these options, see [13]. But first look at the next section, where interior-point methods are discussed. It appears now that for many very big problems (but not all), interior-point methods can out-perform simplex methods [14-16]. Even for moderate-sized problems, an interior-point method could be your best choice.

The simplex codes mentioned above are large software efforts, with many thousands of lines of code. They are quite formidable if you want to study how the simplex algorithm works and play around with various options. Accordingly, in a Webnote [17], we give a pedagogical implementation of the simplex method. Even though it uses reasonably good sparse matrix algebra, it is slower than the public domain implementations by one to two orders of magnitude on problems with $\sim 1 0 ^ { 4 }$ variables. If you don’t care about the simplex algorithm and you just want a simple method to get your problem solved quickly without getting a public domain code up and running, take a look at our pedagogical interior-point code in the next section.

# 10.10.7 Other Topics Briefly Mentioned

Problems where the objective function and/or one or more of the constraints are replaced by expressions nonlinear in the variables are called nonlinear programming problems. The literature on such problems is vast, but outside our scope. The special case of quadratic expressions is called quadratic programming. Optimization problems where the variables take on only integer values are called integer programming problems, a special case of discrete optimization generally. Section 10.12 looks at a particular kind of discrete optimization problem.

# CITED REFERENCES AND FURTHER READING:

Bland, R.G. 1981, “The Allocation of Resources by Linear Programming,” Scientific American, vol. 244 (June), pp. 126–144.[1]   
Dantzig, G.B. 1963, Linear Programming and Extensions (Princeton, NJ: Princeton University Press).[2]   
Kolata, G. 1982, “Mathematician Solves Simplex Problem,” Science, vol. 217, p. 39.[3]   
Markowitz, H.M. 1957, “The Elimination Form of the Inverse and Its Application to Linear Programming,” Management Science, vol. 3, pp. 255–269.[4]   
Bartels. R.H., and Golub, G.H. 1969, “The Simplex Method of Linear Programming Using the LU Decomposition,” Communications of the ACM, vol. 12, pp. 266–268.[5]   
Bartels, R.H. 1971, “A Stabilization of the Simplex Method,” Numerische Mathematik, vol. 16, pp. 414–434.[6]   
Gill, P.E., Murray, W., Saunders, M.A. and Wright, M.H. 1987, “Maintaining LU Factors of a General Sparse Matrix,” Linear Algebra and Its Applications, vol. 88/89, pp. 239–270.[7]   
lp_solve,http://groups.yahoo.com/group/lp_solve.[8]   
Maros, I. 2003, Computational Techniques of the Simplex Method (Boston: Kluwer).[9]   
Suhl, U., and Suhl, L. 1990, “Computing Sparse LU Factorizations for Large-Scale Linear Programming Bases,” ORSA Journal on Computing, vol. 2, pp. 325–335; 1993, “A Fast LU Update for Linear Programming,” Annals of Operations Research, vol. 43, pp. 33–47.[10]   
CLP, http://www.coin-or.org/Clp.[11]


<!-- chunk 0009: pages 561-630 -->
GLPK (GNU Linear Programming Kit), http://www.gnu.org/software/glpk.[12]   
Linear Programming Frequently Asked Questions,http://www-unix.mcs.anl.gov/otc/ Guide/faq/linear-programming-faq.html.[13]   
Lustig, I.J., Marsten, R.E., and Shanno, D.F. 1994, “Interior Point Methods: Computational State of the Art,” ORSA Journal on Computing, vol. 6, pp. 1–14. See also Commentaries and Rejoinder, pp. 15–36.[14]   
Wright, S.J. 1997, Primal-Dual Interior-Point Methods (Philadelphia: S.I.A.M.).[15]   
Bixby, R.E. 2002, “Solving Real-World Linear Programs: A Decade and More of Progress,” Operations Research, vol. 50,pp. 3-15.[16]   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 4 . 1 0$ .   
Nemhauser, G.L., Rinnooy Kan, A.H.G., and Todd, M.J. (eds.) 1989, Optimization (Amsterdam: North-Holland).   
Gill, P.E., Murray, W., and Wright, M.H. 1991, Numerical Linear Algebra and Optimization, vol. 1 (Redwood City, CA: Addison-Wesley), Chapters 7–8.   
Ignizio, J.P., and Cavalier, T.M. 1994, Linear Programming (Englewood Cliffs, NJ: Prentice-Hall). [Undergraduate text]   
Vanderbei, R.J. 2001, Linear Programming: Foundations and Extensions, 2nd ed. (Boston: Kluwer). [Undergraduate/graduate text]   
Chvátal, V. 1983, Linear Programming (New York: Freeman). [Undergraduate text]   
Gass, S.I. 1985, Linear Programming: Methods and Applications, 5th ed. (New York: McGraw-Hill), reprinted 2003 (New York: Dover). [Undergraduate text]   
Murty, K.G. 1983, Linear Programming (New York: Wiley). [Undergraduate text]   
Numerical Recipes Software 2007, “Routine Implementing the Simplex Method,” Numerical Recipes Webnote No.12,at http://www.nr.com/webnotes?12 [17]

# 10.11 Linear Programming: Interior-Point Methods

As we mentioned in $\ S 1 0 . 1 0$ , the worst-case number of iterations for the simplex method is an exponential function of $n$ . (The worst case occurs for $m = n$ .) The average number of iterations, however, is a small multiple of $m$ . For a long time it was not known if there was another algorithm for linear programming that would be bounded by, for example, some polynomial in $n$ . In 1979, Khachian published a new algorithm [1], the ellipsoid method, that is in fact polynomial in $n$ . Disappointingly, however, in practical implementations it was much slower than the simplex method.

In 1984, the field was electrified by Karmarkar’s paper [2] describing an interiorpoint method. Not only was it polynomial in $n$ , but he claimed it solved large LP problems significantly faster than the simplex method. This claim turned out to be somewhat exaggerated, but in the frenzy of activity over the next decade interiorpoint algorithms were developed that do solve many problems much faster than the simplex method, especially very large problems. Ironically, the rivalry between the two algorithms led to improvements of about a factor of 100 in the simplex method itself over the same period. We give some recommendations on which method to use at the end of this section.

Originally, interior-point methods traversed the interior of the feasible region, homing in on the optimal vertex. So-called infeasible interior-point methods follow a path in the interior of the nonnegative region, $x _ { i } \ \geq 0$ , $i = 1 , \ldots , n$ , but possibly through the infeasible region.

To understand how interior-point methods work, we need to develop some more theory about linear programming, in particular about duality.

# 10.11.1 Dual Problem

As we saw in $\ S 1 0 . 1 0$ , any LP problem can be written in standard form:

$$
{ \left| \begin{array} { l l } { \operatorname { m i n i m i z e } } & { \mathbf { c } \cdot \mathbf { x } } \\ { \operatorname { s u b j e c t } \tan } & { \mathbf { A } \cdot \mathbf { x } = \mathbf { b } } \\ & { \mathbf { x } \geq 0 } \end{array} \right. }
$$

Here slack variables have been appended to the $x$ ’s to write all inequality constraints as equalities, but no other logical variables have been added. This is called the primal problem. Recall that if the constraints in (10.11.1) are satisfied, we say that $\mathbf { X }$ is a feasible point.

The dual problem corresponding to (10.11.1) interchanges the roles of variables and constraints: Corresponding to the $m$ constraints is a set of variables $( y _ { 1 } , \dots , y _ { m } )$ determined by

$$
\left| \begin{array} { l l } { \mathrm { m a x i m i z e } } & { \mathbf { b } \cdot \mathbf { y } } \\ { \mathrm { s u b j e c t } \tan } & { \mathbf { A } ^ { T } \cdot \mathbf { y } \leq \mathbf { c } } \\ & { \mathbf { y } \mathrm { ~ f r e e } } \end{array} \right.
$$

Here “free” means unconstrained. Most of the textbooks mentioned at the end of the previous section discuss exactly how to go from the primal problem to its dual. For a hint, see $\ S 1 6 . 5 . 2$ , where a different primal-dual problem is discussed. After that, a particularly clear discussion is in [3]. Note how the constraint matrix for the dual problem is the transpose of the matrix for the primal problem. Forming the dual of the dual simply takes you back to the primal problem.

The dual problem (10.11.2) can be rewritten by adding slack variables $( z _ { 1 } , \dots ,$ $z _ { n }$ /:

$$
\boxed { \begin{array} { r l l } { \mathrm { m a x i m i z e } } & { \mathbf { b } \cdot \mathbf { y } } & \\ { \mathrm { s u b j e c t ~ t o } } & { \mathbf { A } ^ { T } \cdot \mathbf { y } + \mathbf { z } = \mathbf { c } } \\ & { \mathbf { z } \geq 0 , \quad \mathbf { y } \mathrm { ~ f r e e ~ } } \end{array} }
$$

If $( \mathbf { y } , \mathbf { z } )$ satisfy the constraints in (10.11.3), we say that they are dual feasible. For a good introduction to the meaning of the relation between primal and dual problems, see [4].

The weak duality theorem asserts that the value of the dual objective function provides a lower bound to the value of the objective function if they are each evaluated at feasible points. Proof: $\mathbf { b } \cdot \mathbf { y } = \mathbf { y } \cdot \mathbf { A } \cdot \mathbf { \bar { x } } = \mathbf { x } \cdot \mathbf { A } ^ { T } \cdot \mathbf { y } \leq \mathbf { x } \cdot \mathbf { \bar { c } } .$ . The difference

$$
\mathbf { c } \cdot \mathbf { x } - \mathbf { b } \cdot \mathbf { y }
$$

is called the duality gap. If the primal is unbounded (the objective can be made arbitrarily negative), then the dual must be infeasible, and vice versa. Moreover, we have the strong duality theorem: If either the primal or the dual has a finite optimal solution, so does the other, and $\mathbf { c } \cdot \mathbf { x } = \mathbf { b } \cdot \mathbf { y }$ for the optimal solution.

There is a further important relation between the primal and dual variables at optimality. Consider a particular $x _ { j }$ and the corresponding $z _ { j } = ( \mathbf { c } - \mathbf { A } ^ { T } \cdot \mathbf { y } ) _ { j }$ . The Karush-Kuhn-Tucker complementarity condition says that they can’t both be strictly greater than zero: At least one must be equal to zero. In other words,

$$
x _ { j } z _ { j } = 0 , \quad j = 1 , \ldots , n
$$

Adopting the convention that an uppercase letter denotes a matrix with the corresponding lowercase vector along the diagonal, we can write equation (10.11.5) alternatively as

$$
\mathbf { X } \cdot \mathbf { Z } \cdot \mathbf { e } = 0 , \qquad \mathbf { X } = \operatorname { d i a g } ( x _ { 1 } , \ldots , x _ { n } ) , \quad \mathbf { Z } = \operatorname { d i a g } ( z _ { 1 } , \ldots , z _ { n } ) , \quad \mathbf { e } = ( 1 , \ldots , 1 )
$$

Since each $x _ { j }$ and $z _ { j }$ is nonnegative, equation (10.11.5) is equivalent to $\mathbf { x } \cdot \mathbf { z } = 0$ . In fact, this result holds in both directions: The complementary slackness theorem says that feasible solutions are optimal if and only if ${ \mathbf x } \cdot { \mathbf z } = 0$ . It is easy to show that for feasible solutions, $\mathbf { X } \cdot \mathbf { Z }$ is simply equal to the duality gap (10.11.4).

Note that complementary slackness allows the possibility that both $x _ { j }$ and $z _ { j }$ might be zero at an optimal solution. Strict complementarity is the property that exactly one of these quantities is zero for all $j$ . The Goldman-Tucker theorem says that if the primal and dual are feasible, there exists a strictly complementary pair of optimal solutions. As we’ll see, interior-point methods find such a solution.

# 10.11.2 The KKT Conditions

Linear programming is a special case of general constrained optimization, where one wants to minimize some function $f ( \mathbf { x } )$ subject to constraints. The general optimality conditions are called the Karush-Kuhn-Tucker or KKT conditions. Specialized to the LP problem (10.11.1), the KKT conditions are

$$
\begin{array} { r } { \mathbf { A } \cdot \mathbf { x } = \mathbf { b } \qquad \mathbf { x } \geq 0 } \\ { \mathbf { A } ^ { T } \cdot \mathbf { y } + \mathbf { z } = \mathbf { c } \qquad \mathbf { z } \geq 0 } \\ { \mathbf { X } \cdot \mathbf { Z } \cdot \mathbf { e } = 0 \qquad \mathbf { y } \mathrm { ~ f r e e ~ } } \end{array}
$$

Note that these are exactly the conditions that follow from strong duality and complementarity. Later we will see how to derive these conditions directly using Lagrange multipliers to handle the constraints.

The KKT conditions (10.11.7) are necessary and sufficient for $\mathbf { X }$ to be an optimal solution of (10.11.1). Moreover, they are necessary and sufficient for $( \mathbf { x } , \mathbf { y } , \mathbf { z } )$ to solve the primal and dual problems (10.11.1) and (10.11.2). In this case, we call $( \mathbf { x } , \mathbf { y } , \mathbf { z } )$ a primal-dual solution. Primal-dual interior-point methods solve the equations (10.11.7) in such a way that the inequalities are satisfied strictly at every iteration, that is, $\mathbf { x } , \mathbf { z } > 0$ .

The equations are solved using a variant of Newton’s method. Recall that if we define the vector of equations in (10.11.7) as

$$
\begin{array}{c} \mathbf { F } ( \mathbf { v } ) = \left[ \mathbf { A } ^ { \cdot } \mathbf { x } - \mathbf { b }  \\ { \mathbf { A } ^ { T } \cdot \mathbf { y } + \mathbf { z } - \mathbf { c } } \\ { \mathbf { X } \cdot \mathbf { Z } \cdot \mathbf { e } } \end{array} \right] = 0
$$

where $\mathbf { V }$ is shorthand for $( \mathbf { x } , \mathbf { y } , \mathbf { z } )$ , then Newton’s method determines the update $\Delta \mathbf { v }$ to the current point by solving

$$
\mathbf { J } \cdot \Delta \mathbf { v } = - \mathbf { F }
$$

Here $\mathbf { J }$ is the Jacobian matrix of $\mathbf { F }$ (see $\ S 9 . 7 \AA$ ). A full step with this value of $\Delta \mathbf { v }$ is usually not allowed because it would violate the condition $( { \bf { x } } , { \bf { z } } ) \ge 0$ . So the new iterate is chosen from a line search along the Newton direction:

$$
\mathbf { v } _ { \mathrm { n e w } } = \mathbf { v } _ { \mathrm { o l d } } + \alpha \Delta \mathbf { v } , \qquad \alpha \in ( 0 , 1 ]
$$

You choose $\alpha = 1$ if possible; otherwise, you choose the maximum $\alpha$ that preserves nonnegativity.

Note the importance of keeping the nonnegative variables strictly positive at all times: The Newton equation for $x _ { j } z _ { j } = 0$ is $x _ { j } \Delta z _ { j } + z _ { j } \Delta x _ { j } = - x _ { j } z _ { j }$ . Suppose $z _ { j }$ is zero. Then the Newton equation becomes $x _ { j } \Delta z _ { j } = 0$ , or $\Delta z _ { j } = 0$ . So $z _ { j }$ remains zero if it ever becomes zero. The algorithm can never recover. Of course, one should also expect difficulties if any variable gets “too close” to zero.

This simple damped Newton’s method is not a practical algorithm, because too often the allowed stepsize becomes very small $( \alpha \ll 1 \dot$ ). There are two important modifications that are crucial to producing a viable algorithm:

- Change the search direction so that it aims toward the “center” of the nonnegative region. The idea is to allow larger steps before one of the variables would become negative.   
Don’t allow the variables to come “too close” to the boundary of the nonnegative region. As discussed above, little progress tends to be made from such points.

# 10.11.3 The Central Path

One way to bias the search direction away from boundary is to arrange for all the complementarity pairs $x _ { j } z _ { j }$ to converge to zero at the same rate, say $x _ { j } z _ { j } = \tau$ , where $\tau \ \to \ 0$ during the iterations. In other words, modify the last equation in (10.11.8) so that the system becomes

$$
\mathbf { F } ( \mathbf { v } ) = \left[ \mathbf { A } \cdot \mathbf { x } - \mathbf { b } \quad \right] = { \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { \mathbf { X } \cdot \mathbf { Z } \cdot \mathbf { e } } \end{array} \right] } = { \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { \tau \mathbf { e } } \end{array} \right] }
$$

The set of solutions $\mathbf { v } ( \tau )$ to equations (10.11.11) defines the central path. Primaldual algorithms take steps toward points on the central path with $\tau > 0$ . During the iterations, $\tau  0$ and the central path homes in on the optimal solution.

If you plot the central path in the hyperspace of $( \mathbf { x } , \mathbf { z } )$ coordinates, it’s some contorted line that doesn’t look central to anything. However, if you plot it in coordinates $( x _ { 1 } z _ { 1 } , x _ { 2 } z _ { 2 } , . . . )$ , you see that it is equidistant from all the coordinate surfaces, with the optimal solution at the origin. When the current iterate is close to the central path, the next iteration can make a large step toward the optimal solution. When the current iterate is close to one of the boundaries, a good algorithm makes the next iteration get close to the central path again.

# 10.11.4 Path-Following Methods

Path-following methods don’t just aim steps in the direction of the central path; they explicitly attempt to stay close to it. These methods are currently the most successful interior-point methods. In primal-dual methods, the duality gap (10.11.4), which is equal to $\textbf { X } \cdot \textbf { Z }$ for feasible points, provides a figure-of-merit for how close one is to the optimal solution. Accordingly, we set

$$
\mu = { \bf x } \cdot { \bf z } / n , \qquad \tau = \mu \delta , \quad \delta \in [ 0 , 1 ]
$$

The quantity $\delta$ is called the centering parameter, while $\mu$ is called the duality measure. If $\delta = 1$ , the Newton step calculated from (10.11.11) is in a centering direction, toward a point at which each product $x _ { j } \ z _ { j }$ is equal to the average value $\mu$ defined in (10.11.12). On the other hand, the value $\delta = 0$ defines the Newton step for the original system (10.11.8). Good algorithms use intermediate values to trade off between improving centrality and reducing $\mu$ .

Methods that keep ı close to 1, so that unit steps $( \alpha = 1$ ) stay close to the central path, are called short-step methods. Methods that allow small values of $\delta$ are called long-step methods (less conservative choices of $\delta$ ). There is an interesting gap between theory and practice between the methods. Short-step methods have been proved to converge in $\dot { O ( } \sqrt { n } \log \frac { 1 } { \epsilon } )$ iterations, where $\epsilon$ is the desired tolerance. Long-step methods take $\begin{array} { r } { O ( n \log \frac { 1 } { \epsilon } ) } \end{array}$ iterations, according to theory. Yet in practice short-step methods take hopelessly small steps, while long-step methods provide practical algorithms.

This is a somewhat academic discussion anyway. Real-life examples take many fewer than $O ( { \sqrt { n } } )$ iterations — a few dozen is typical for large problems.

# 10.11.5 Barrier Methods

Introducing a “penalty” function is a standard technique to enforce a constraint in general optimization problems. For example, to enforce the condition $\textbf { x } \geq 0$ , consider the logarithmic penalty function

$$
\sum _ { j = 1 } ^ { n } \log x _ { j }
$$

If any $x _ { j } \to 0$ , this function tends to $- \infty$ . So instead of trying to minimize $\mathbf { c } \cdot \mathbf { X }$ in the standard primal problem (10.11.1), consider minimizing

$$
\mathbf { c } \cdot \mathbf { x } - \tau \sum _ { j = 1 } ^ { n } \log x _ { j }
$$

If one takes the limit $\tau  0$ after the minimization, we expect this to be equivalent to the original problem.

Equation (10.11.14) is called a logarithmic barrier function. It defines a family of nonlinear objective functions that gives the solution to the original problem as the parameter $\tau  0$ .

The power of the barrier function idea is that it lets us handle the constraint $\textbf { x } \geq 0$ with calculus. To minimize (10.11.14) subject to the constraint $\mathbf { A } \cdot \mathbf { x } = \mathbf { b }$ , introduce a Lagrange multiplier $- \mathbf { y }$ and extremize the Lagrangian

$$
L = \mathbf { c } \cdot \mathbf { x } - \tau \sum _ { j = 1 } ^ { n } \log x _ { j } - \mathbf { y } \cdot ( \mathbf { A } \cdot \mathbf { x } - \mathbf { b } )
$$

The optimality conditions $\nabla _ { x } L = 0$ and $\nabla _ { y } L = 0$ give

$$
\begin{array} { r } { \mathbf { A } \cdot \mathbf { x } = \mathbf { b } } \\ { \mathbf { A } ^ { T } \cdot \mathbf { y } + \tau \mathbf { X } ^ { - 1 } \cdot \mathbf { e } = \mathbf { c } } \end{array}
$$

Define the vector

$$
\mathbf { z } = \tau \mathbf { X } ^ { - 1 } \cdot \mathbf { e } , \quad \mathrm { i . e . , } \quad z _ { j } = \tau / x _ { j }
$$

Then equation (10.11.16) becomes

$$
\begin{array} { c } { \mathbf { A } \cdot \mathbf { x } = \mathbf { b } } \\ { \mathbf { A } ^ { T } \cdot \mathbf { y } + \mathbf { z } = \mathbf { c } } \\ { \mathbf { X } \cdot \mathbf { Z } \cdot \mathbf { e } = \tau \mathbf { e } } \end{array}
$$

These are exactly the equations (10.11.11) defining the central path, and they reduce to the KKT conditions (10.11.7) if we set $\tau$ to zero.

Note that equation (10.11.16) can be used to define an algorithm, the primal interior-point method, that doesn’t depend on $\mathbf { z }$ . Similarly, by starting with a logarithmic barrier function for the dual objective function, one can derive a purely dual method that doesn’t involve x. In practice, These methods are not competitive with the primal-dual methods.

Originally the logarithmic barrier function idea played an important role in motivating interior-point methods. More recently, the viewpoint has shifted to emphasize the importance of $\tau$ as defining the centering property of the algorithm rather than being simply a parameter to enforce the nonnegativity constraint.

# 10.11.6 A Primal-Dual Infeasible Interior-Point Algorithm

Let’s pull all the pieces together now to define the algorithm. Write equation (10.11.11) for the new iterate:

$$
\begin{array} { r } { \mathbf { A } \cdot ( \mathbf { x } + \Delta \mathbf { x } ) - \mathbf { b } = 0 } \\ { \mathbf { A } ^ { T } \cdot ( \mathbf { y } + \Delta \mathbf { y } ) + \mathbf { z } + \Delta \mathbf { z } - \mathbf { c } = 0 } \\ { ( \mathbf { X } + \Delta \mathbf { X } ) \cdot ( \mathbf { Z } + \Delta \mathbf { Z } ) \cdot \mathbf { e } = \tau \mathbf { e } } \end{array}
$$

Drop the quadratic term $\Delta \mathbf { X } \cdot \Delta \mathbf { Z } \cdot \mathbf { e }$ and get

$$
\begin{array} { r } { \left[ \begin{array} { c c c } { \mathbf { A } } & { \mathbf { 0 } } & { \mathbf { 0 } } \\ { \mathbf { 0 } } & { \mathbf { A } ^ { T } } & { \mathbf { 1 } } \\ { \mathbf { Z } } & { \mathbf { 0 } } & { \mathbf { X } } \end{array} \right] \left[ \begin{array} { c } { \Delta \mathbf { x } } \\ { \Delta \mathbf { y } } \\ { \Delta \mathbf { z } } \end{array} \right] = \left[ \begin{array} { c } { - \mathbf { r } _ { p } } \\ { - \mathbf { r } _ { d } } \\ { \tau \mathbf { e } - \mathbf { X } \cdot \mathbf { Z } \cdot \mathbf { e } } \end{array} \right] } \end{array}
$$

where the primal and dual residuals are defined by

$$
\begin{array} { l } { \mathbf { r } _ { p } = \mathbf { A } \cdot \mathbf { x } - \mathbf { b } } \\ { \mathbf { r } _ { d } = \mathbf { A } ^ { T } \cdot \mathbf { y } + \mathbf { z } - \mathbf { c } } \end{array}
$$

Equation (10.11.20) is simply the Newton equation (10.11.9) for (10.11.11). Note that the only nonlinearity comes from the innocuous looking quadratic term for complementary slackness. Yet it’s exactly what leads to all the difficulty!

Since $\mathbf { X }$ is a diagonal positive-definite matrix, we can trivially invert it and use the last equation in (10.11.20) to eliminate $\Delta \mathbf { z }$ from the second equation. Interchanging the order of the variables $\Delta \mathbf { x }$ and $\Delta \mathbf { y }$ , we get

$$
\begin{array} { r } { \left[ \begin{array} { c c } { \mathbf { 0 } } & { \mathbf { A } } \\ { \mathbf { A } ^ { T } } & { - \mathbf { X } ^ { - 1 } \cdot \mathbf { Z } } \end{array} \right] \left[ \Delta \mathbf { y } \right] = \left[ \begin{array} { c c } { \mathbf { - r } _ { p } } & \\ { \mathbf { z } - \tau \mathbf { X } ^ { - 1 } \cdot \mathbf { e } - \mathbf { r } _ { d } } \end{array} \right] } \end{array}
$$

Similarly, since $- \mathbf { X } ^ { - 1 } \cdot \mathbf { Z }$ is easily invertible, we can use the second equation in (10.11.22) to eliminate $\Delta \mathbf { x }$ from the first. This gives

$$
\mathbf { A } \cdot ( \mathbf { X } \cdot \mathbf { Z } ^ { - 1 } ) \cdot \mathbf { A } ^ { T } \cdot \Delta \mathbf { y } = - \mathbf { r } _ { p } + \mathbf { A } \cdot ( \mathbf { x } - \tau \mathbf { Z } ^ { - 1 } \cdot \mathbf { e } - \mathbf { X } \cdot \mathbf { Z } ^ { - 1 } \cdot \mathbf { r } _ { d } )
$$

These are called the normal equations, by analogy with the normal equations that occur in least-squares problems (cf. 15.4.10). The predecessor equations in (10.11.22) are called the augmented equations. Note that the matrix on the left-hand side of the normal equations is symmetric and positive-definite, except for some delicacy as $\mathbf { X }$ and $\mathbf { z } \ \to \ 0$ . This suggests solving them with some version of the Cholesky decomposition (-2.9).

Once $\Delta \mathbf { y }$ is determined from the normal equations, the second equation in (10.11.20) gives $\Delta \mathbf { z }$ :

$$
\Delta \mathbf { z } = - \mathbf { A } ^ { T } \cdot \Delta \mathbf { y } - \mathbf { r } _ { d }
$$

Finally, the third equation in (10.11.20) gives $\Delta \mathbf { x }$ :

$$
\Delta \mathbf { x } = - \mathbf { X } \cdot \mathbf { Z } ^ { - 1 } \cdot \Delta \mathbf { z } + \tau \mathbf { Z } ^ { - 1 } \cdot \mathbf { e } - \mathbf { x }
$$

In a feasible interior-point method, an initial point is somehow found in the feasible region, that is, with $\mathbf { r } _ { p } = \mathbf { r } _ { d } = 0$ and $( { \bf x } , { \bf z } ) > 0$ . Then equations (10.11.23) $- \left( 1 0 . 1 1 . 2 5 \right)$ are solved with $\mathbf { r } _ { p }$ and $\mathbf { r } _ { d }$ set to zero. The consensus now is that it is not necessary to do this. It is much easier to choose a point that may be infeasible initially, and allow the iterations to converge toward a feasible point. As explained above, it is still crucial to maintain nonnegativity, however.

Equation (10.11.23) contains three contributions to the step $\Delta \mathbf { y }$ and hence to $\Delta \mathbf { x }$ and $\Delta \mathbf { z }$ . First there are the terms that involve $\mathbf { r } _ { p }$ and $\mathbf { r } _ { d }$ , which drive the solution toward feasibility. Then there is the term independent of $\tau$ . It drives the solution toward optimality. In the literature, this term is called the affine scaling term, because there is a geometric interpretation of its effect in terms of a linear scaling of variables. Finally there is the term proportional to $\tau$ , which is the centering term.

Here is the framework for a simple primal-dual infeasible interior-point method:

1. Choose an initial nonnegative point.   
2. If the infeasibilities $\mathbf { r } _ { p }$ and $\mathbf { r } _ { d }$ and the complementarity gap $\mathbf { X } \cdot \mathbf { Z }$ are below the desired tolerance, exit. Otherwise, continue.   
3. Set the value of $\tau$ from equation (10.11.12). A value of $\begin{array} { r } { \delta \approx 0 . 0 2 } \end{array}$ works well.   
4. Compute the direction of the step $( \Delta \mathbf { x } , \Delta \mathbf { y } , \Delta \mathbf { z } )$ from equations $( 1 0 . 1 1 . 2 3 ) -$ (10.11.25). The solution of the normal equations is done in two steps: factorization of the matrix to some easily invertible form, followed by solution using this factorization.   
5. Determine the maximum stepsizes that do not allow the variables to become negative. Separate stepsizes can be determined for the primal and dual variables:

$$
\begin{array} { r } { \mathbf { x } _ { \mathrm { n e w } } = \mathbf { x } _ { \mathrm { o l d } } + \alpha _ { p } \Delta \mathbf { x } } \\ { \mathbf { y } _ { \mathrm { n e w } } = \mathbf { y } _ { \mathrm { o l d } } + \alpha _ { d } \Delta \mathbf { y } } \\ { \mathbf { z } _ { \mathrm { n e w } } = \mathbf { z } _ { \mathrm { o l d } } + \alpha _ { d } \Delta \mathbf { z } } \end{array}
$$

where $\alpha _ { p }$ and $\alpha _ { d }$ are initially chosen to be the largest values that keep all components of $\mathbf { X } _ { \mathrm { n e w } }$ and $\mathbf { z } _ { \mathrm { n e w } }$ nonnegative but no larger than unity. Then reduce the values of $\alpha _ { p }$ and $\alpha _ { d }$ by a safety factor $\sigma$ . A conservative choice is $\sigma = 0 . 9$ , but $\sigma = 0 . 9 9 9 9 5$ works for many problems.

6. Go back to step 2 for the next iteration.

Since in real-life linear programming the constraint matrix A is sparse, the code must take advantage of this. The various matrix products such as $\mathbf { A } \cdot \mathbf { x }$ , $\mathbf { A } ^ { T } \cdot \mathbf { y }$ and $\mathbf { A } \cdot ( \mathbf { X } \cdot \mathbf { Z } ^ { - 1 } ) \cdot \mathbf { A } ^ { T }$ should be computed efficiently. More important, the factorization and backsubstitution involved in solving the normal equations must use a suitable sparse matrix Cholesky decomposition. The factorization step in fact dominates the running time of the algorithm. Our implementation uses the relatively simple package LDL [5], combined with the package AMD [6] to compute an ordering (permutation) of the matrix that minimizes fill-in during the factorization. Both of these packages are freely available. Note that LDL has to be modified to deal with the singularities that occur as the diagonal matrix elements $x _ { j } / z _ { j } \to 0$ . It is sufficient to modify the line of code in LDL that tests for a diagonal element equal to zero to something like

if (D[k] $<$ 1.0e-40) D[k] $=$ 1.0e128;

This has the effect of setting the corresponding variable to zero, which is the desired behavior. Here is our interface NRldl.h to these packages. The full implementation is given in a Webnote [13].

extern "C" { #include "ldl.h" #include "amd.h"   
} struct NRldl   
Interface between Numerical Recipes routine intpt and the required external packages LDL and AMD.

Doub Info [AMD_INFO]; Int lnz,n,nz; VecInt PP,PPinv,PPattern,LLnz,LLp,PParent,FFlag,\*LLi; VecDoub YY,DD,\*LLx; Doub \*Ax, \*Lx, \*B, \*D, \*X, \*Y; Int \*Ai, \*Ap, \*Li, \*Lp, \*P, \*Pinv, \*Flag,\*Pattern, \*Lnz, \*Parent; NRldl(NRsparseMat &adat); Constructor only needs adat to have been declared with appropriate dimensions. void order(); AMD ordering and LDL symbolic factorization. Only needs nonzero pattern of adat, not actual values. void factorize(); Numerical factorization of matrix. void solve(VecDoub_O &y,VecDoub &rhs); Solves for y given rhs. Can be invoked multiple times after a single call to factorize. \~NRldl(); };

Here is a simple implementation of the interior-point algorithm. Although it is a pedagogical code, it is actually quite powerful — better than the pedagogical simplex code of the previous section. Below we will explain what would be required to turn this code into a serious implementation.

Doub dotprod(VecDoub_I &x, VecDoub_I &y) Compute the dot product of two vectors, $\mathbf { x } \cdot \mathbf { y }$ . {

Doub sum $_ { 1 = 0 }$ .0;   
for (Int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<x.size(); $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \beta } } } .$ ) sum $+ = \texttt { x }$ [i]\*y[i];   
return sum;

# }

Int intpt(const NRsparseMat &a, VecDoub_I &b, VecDoub_I &c, VecDoub_O &x)

Interior-point method for linear programming. On input a contains the coefficient matrix for the constraints in the form $\mathbf { A \cdot x } = \mathbf { b }$ . The right-hand side of the constraints is input in $\mathtt { b } [ 0 \dots \dots ] \mathtt { m } ^ { - 1 } ]$ . The coefficients of the objective function to be minimized, $\mathbf { c } \cdot \mathbf { x }$ , are input in $\mathtt { c } \left[ 0 \ldots \mathtt { n - 1 } \right]$ . Note that c should generally be padded with zeros corresponding to the slack variables that extend the number of columns to be n. The function returns 0 if an optimal solution is found; 1 if the problem is infeasible; 2 if the dual problem is infeasible, i.e., if the problem is unbounded or perhaps infeasible; and 3 if the number of iterations is exceeded. The solution is returned in $\mathbf { x } \left[ 0 \ldots \mathbf { n - 1 } \right]$ .

const Int MAXITS $\bullet { }$ 200; Maximum iterations.   
const Doub EP $\mathrel { \mathop : } = 1$ .0e-6; Tolerance for optimality and feasibility.   
const Doub SIGMA $_ { = 0 }$ .9; Stepsize reduction factor (conservative choice)   
const Doub DELTA $= 0 . 0 2$ ; Factor to set centrality parameter $\mu$ .   
const Doub BIG $=$ numeric_limits<Doub>::max();   
Int i,j,iter,status;   
Int $\mathtt { m } = \mathtt { a }$ .nrows;   
Int $\mathtt { n } = \mathtt { a }$ .ncols;   
VecDoub y(m),z(n),ax(m),aty(n),rp(m),rd(n),d(n),dx(n),dy(m),dz(n), rhs(m),tempm(m),tempn(n);   
NRsparseMat at=a.transpose(); Compute $\mathbf { A } ^ { T }$ .   
ADAT adat(a,at); Setup for ${ \mathbf { A \cdot D \cdot A } } ^ { T }$ , where ${ \bf D } = { \bf X } \cdot { \bf Z } ^ { - 1 }$ .   
NRldl solver(adat.ref()); Initialize interface to LDL package.   
solver.order(); AMD ordering and LDL symbolic factorization.   
Doub rpfact $= 1$ . $0 +$ sqrt(dotprod(b,b)); Compute factors for convergence test.   
Doub rdfact $= 1$ .0+sqrt(dotprod(c,c));   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) 3 Initial point. x[j] $=$ 1000.0; z[j] $=$ 1000.0;   
for (i=0;i<m;i++) { y[i] $=$ 1000.0;   
Doub normrp_old BIG;   
Doub normrd_old=BIG;   
cout << setw(4) << "iter" << setw(12) << "Primal obj." << setw(9) << "||r_p||" << setw(13) $< <$ "Dual obj." $< <$ setw(11) << "||r_d||" << setw(13) $< <$ "duality gap" << setw(16) << "normalized gap" $< <$ endl;   
cout << scientific $< <$ setprecision(4);   
for (iter ${ \tt = } 0$ ;iter<MAXITS;iter $^ { + + }$ ) Start of main loop. ax $= \mathtt { a }$ .ax(x); Compute normalized residuals $r _ { p }$ and $r _ { d }$ . for (i=0;i<m;i++) rp[i] $=$ ax[i]-b[i]; Doub normrp=sqrt(dotprod(rp,rp))/rpfact; aty=at.ax(y); for (j=0;j<n;j++) rd[j] $=$ aty[j] $+ z$ [j]-c[j]; Doub normrd=sqrt(dotprod(rd,rd))/rdfact; Doub gamma=dotprod(x,z); Duality gap is $\mathbf { x } \cdot \mathbf { z }$ for feasible points. Doub mu=DELTA\*gamma/n; Choice of $\mu$ . Doub primal_obj=dotprod(c,x); Print current iteration.   
Doub dual_obj $=$ dotprod(b,y);   
Doub gamma_norm=gamma/(1. $^ { 0 + }$ abs(primal_obj)); cout $< <$ setw(3) $< <$ iter << setw(12) $< <$ primal_obj $< <$ setw(12) << normrp $< <$ setw(12) << dual_obj << setw(12) << normrd << setw(12) << gamma << setw(12) $< <$ gamma_norm<<endl; if (normrp $<$ EPS && normrd $<$ EPS && gamma_norm $<$ EPS) return status ${ = } 0$ ; Optimal solution found. if (normrp $>$ 1000\*normrp_old && normrp > EPS) return status $^ { = 1 }$ ; Primal infeasible. if (normrd $>$ 1000\*normrd_old && normrd $>$ EPS) return status $^ { = 2 }$ ; Dual infeasible.   
for (j=0;j<n;j++) Compute step directions. First form matrix d[j] $= \mathrm { x }$ [j]/z[j]; $\mathbf { A } \cdot \mathbf { X } \cdot \mathbf { Z } ^ { - 1 } \cdot \mathbf { A } ^ { T }$ . adat.updateD(d); solver.factorize(); Factorize matrix. for (j=0;j<n;j++) Form right-hand side. tempn[j] $= \tt x$ [j]-mu/z[j]-d[j]\*rd[j]; tempm=a.ax(tempn); for (i=0;i<m;i++) rhs[i] $=$ -rp[i]+tempm[i]; solver.solve(dy,rhs); Solve for $d y$ . tempn=at.ax(dy); Solve for $d z$ .   
for (j=0;j<n;j++) dz[j]=-tempn[j]-rd[j];   
for (j=0;j<n;j++) Solve for $_ { d x }$ . dx[j]=-d[j]\*dz[j]+mu/z[j]-x[j];   
Doub alpha_p ${ = } 1$ .0; Find step length.   
for (j=0;j<n;j++) if (x[j]+alpha_p\*dx[j] < 0.0) alpha_p=-x[j]/dx[j];   
Doub alpha_ $\mathtt { d } \mathtt { = } 1$ .0;   
for (j=0;j<n;j++) if (z[j]+alpha_d\*dz[j] < 0.0) alpha_ $\scriptstyle \mathbf { d } = - z$ [j]/dz[j]; alpha_p $=$ MIN(alpha_p\*SIGMA,1.0); alpha_d $=$ MIN(alpha_d\*SIGMA,1.0); for (j=0;j<n;j++) { Step to new point. x[j] $+ =$ alpha_p\*dx[j]; z[j] $+ =$ alpha_d\*dz[j]; }   
for (i=0;i<m; $\dot { 1 } + +$ ) y[i] $+ =$ alpha_d\*dy[i]; normrp_old=normrp; Update norms. normrd_old=normrd;   
turn status $^ { = 3 }$ ; Maximum iterations exceeded.

# 10.11.7 Practical Interior-Point Codes

There are a number of important features that would be needed to turn the above simple implementation into a state-of-the-art code.

- Initial point. Choosing a good starting point cuts down the number of iterations required. A good algorithm is described in [7].   
Preprocessing. As for the simplex method, preprocessing can often reduce the size of the problem.   
- Scaling. A badly scaled problem can lead to numerical difficulties.   
- Handling bounded variables. Suppose that instead of the requirement $\textbf { x } \ge 0$ the variables are bounded:

$$
\mathbf { l } \leq \mathbf { x } \leq \mathbf { u }
$$

Here, for simplicity, we have written the vectors of lower and upper bounds, l and $\mathbf { u }$ , as being of length $n$ . In practice, only some of the variables $\mathbf { X }$ may have bounds. One way to deal with bounds is to add them to the system $\mathbf { A \cdot x } = \mathbf { b }$ with slack variables in the usual way. However, this increases the dimension of the matrix A. There is a simpler way to proceed. First, lower bounds of the form $l _ { j } \le x _ { j }$ can be handled by a simple shift: $x _ { j } ^ { \prime } = x _ { j } - l _ { j } \geq 0$ . Making this replacement everywhere allows the problem to be solved as before, and then you simply undo the shift to get the solution in terms of the original $x _ { j }$ . So without loss of generality we can assume all the bounds are of the form

$$
0 \leq \mathbf { x } \leq \mathbf { u }
$$

If we introduce slack variables s and dual slack variables $\mathbf { W }$ , the optimality conditions are

$$
\begin{array} { r } { \mathbf { A } \cdot \mathbf { x } = \mathbf { b } } \\ { \mathbf { x } + \mathbf { s } = \mathbf { u } } \\ { \mathbf { A } ^ { T } \cdot \mathbf { y } + \mathbf { z } - \mathbf { w } = \mathbf { c } } \\ { \mathbf { X } \cdot \mathbf { Z } \cdot \mathbf { e } = 0 } \\ { \mathbf { S } \cdot \mathbf { W } \cdot \mathbf { e } = 0 } \end{array}
$$

with $\mathbf { X } , \mathbf { s } , \mathbf { z }$ , and $\mathbf { W }$ all nonnegative. It is simple to change the right-hand sides of the last two equations in (10.11.29) to $\tau { \mathbf e }$ and apply Newton’s method as for equation (10.11.11). You find that the equations to be solved are very similar in form to equations $( 1 0 . 1 1 . 2 3 ) - ( 1 0 . 1 1 . 2 5 )$ .

- Predictor-corrector. Most of the time spent in an iteration goes into the factorization of the matrix in the normal equations. Given the factorization, the solve step is relatively cheap. Mehotra’s predictor-corrector method [7] takes advantage of this by using an extra solve step per iteration to improve the overall efficiency of the algorithm.

Recall that in going from equation (10.11.19) to equation (10.11.20) we dropped the term $\Delta \mathbf { X } \cdot \Delta \mathbf { Z } \cdot \mathbf { e }$ . The idea in Mehotra’s method is to first take a predictor step that solves equation (10.11.20), but with the $\tau$ term omitted. The values of $( \Delta \mathbf { x } , \Delta \mathbf { y } , \Delta \mathbf { z } )$ obtained are used to estimate $\Delta \mathbf { X } \cdot \Delta \mathbf { Z } \cdot \mathbf { e }$ . Then the corrector step solves for an additional set $( \Delta \mathbf { x } , \Delta \mathbf { y } , \Delta \mathbf { z } )$ from equation (10.11.20) with the right-hand side replaced by

$$
\left[ \begin{array} { c } { 0 } \\ { 0 } \\ { \tau \mathbf { e } - \Delta \mathbf { X } \cdot \Delta \mathbf { Z } \cdot \mathbf { e } } \end{array} \right]
$$

The value of $\tau$ in equation (10.11.30) is set differently from equation (10.11.12). First $\widehat { \mu }$ is computed using the predictor step:

$$
\widehat { \mu } = ( \mathbf { x } + \alpha _ { p } \Delta \mathbf { x } ) \cdot ( \mathbf { z } + \alpha _ { d } \Delta \mathbf { z } ) / n
$$

Here $\alpha _ { p }$ and $\alpha _ { d }$ are the largest values that maintain nonnegativity, but no larger than unity. (No safety factor is used.) Then $\tau$ is set as

$$
\tau = \left( \frac { \widehat { \mu } } { \mu } \right) ^ { 2 } \widehat { \mu }
$$

where $\mu$ is computed using the starting values of $\mathbf { X }$ and $\mathbf { z }$ as in equation (10.11.12). This heuristic choice makes $\tau$ small when the predictor step gives a large decrease in complementarity, and large otherwise.

The total step is the sum of the predictor and corrector steps. The cutdown factor from $\alpha _ { p }$ or $\alpha _ { d }$ equal to unity is calculated from a heuristic procedure described in [7] or [8].

Gondzio [9,10] has developed an extension to the predictor-corrector algorithm that incorporates higher-order corrections when they can improve the efficiency.

- Better sparse matrix algebra. While AMD is a good general-purpose choice for an ordering algorithm, LDL is a good but basic sparse Cholesky routine, chosen mainly for its simplicity and availability. More powerful algorithms are known and are starting to become publicly available.

One of the problems with the normal equations is that the matrix can be quite dense, even when A itself is rather sparse. This has motivated algorithms that solve the augmented equations (10.11.22) directly. On some problems, this leads to significant savings. A good implementation will provide both alternatives.

Solving the equations can become numerically delicate, especially as the optimal point is approached. Good implementations will use some form of iterative refinement to preserve accuracy.

- Crossover to the simplex method. Often the convergence of the interior-point algorithm slows down near the optimal point. By switching to a simplex method with a basis that is presumably close to optimal, one can get rapid convergence to the answer. This feature has the additional benefit that the optimal point is given in terms of basis vectors, whereas the interior-point solution never actually attains zeros for any x’s. Some kinds of post-analysis need the actual basis.

Interestingly, using a previously-found solution as the initial point for a “nearby” problem seldom helps much for interior-point methods. The reason is that interior-point methods don’t make good progress from a point near the boundary. The simplex method, by contrast, generally converges much more rapidly with a “warm start.” A good strategy for solving a sequence of closely related problems is therefore interior-point with crossover to an optimal basis for the first one, then simplex with a warm start for the remainder.

There are several codes that are free for noncommercial use and that give full implementations of interior-point methods. We particularly like $\operatorname { P C x }$ (in C with Fortran sparse algebra routines) [11] and HOPDM (in Fortran) [10]. For a discussion of more options, including commercial codes, see [12].

So which should you use: a simplex or an interior-point code? If you have only our codes, use the interior-point one. If you have a production implementation of either algorithm, it will probably suffice. If you are solving many large problems, however, you should have both so you can use the optimum algorithm in each case. If you are solving a large problem for the first time, there is a lot to be said for using an interior-point code. There are fewer choices to make to get almost optimal performance. By contrast, finding which particular choices of components in a simplex method give optimal performance can involve a lot of experimentation. Your first try will usually not be as good as a default interior-point code. And often the interior-point code will beat all simplex variants.

# CITED REFERENCES AND FURTHER READING:

Khachian, L. 1979, Doklady Academiia Nauk SSSR, vol. 244, pp. 191–194. English translation: “A Polynomial Time Algorithm in Linear Programming,” Soviet Mathematics Doklady, vol. 20, pp. 191–194.[1]   
Karmarkar, N. 1984, “A New Polynomial-time Algorithm for Linear Programming,” Combinatorica vol. 4, pp. 373–395.[2]   
Maros, I. 2003, Computational Techniques of the Simplex Method (Boston: Kluwer).[3]   
Nazareth, J.L. 2004, An Optimization Primer (New York: Springer).[4]   
LDL,http://www.cise.ufl.edu/research/sparse.[5]   
AMD, http://www.cise.ufl.edu/research/sparse. See also Amestoy, PR., Enseeiht-Irit, Davis, T.A., and Duff, I.S. 2004, “AMD, an Approximate Minimum Degree Ordering Algorithm.” ACM Transactions on Mathematical Software vol. 30, pp. 381–388.[6]   
Mehrotra, S. 1992, “On the Implementation of a Primal-dual Interior Point Method,” SIAM Journal on Optimization vol. 2, pp. 575-601.[7]   
Wright, S.J. 1997, Primal-Dual Interior-Point Methods (Philadelphia: S.I.A.M.).[8]   
Gondzio, J. 1996, “Multiple Centrality Corrections in a Primal-dual Method for Linear Programming,” Computational Optimization and Applications vol. 6, pp. 137–156.[9]   
HOPDM,http://www.maths.ed.ac.uk/\~gondzio/software/hopdm.html.[10]   
PCX,http://www-fp.mcs.anl.gov/otc/Tools/PCx.[11]   
Linear Programming Frequently Asked Questions,http://www-unix.mcs.anl.gov/otc/ Guide/faq/linear-programming-faq.html.[12]   
Vanderbei, R.J. 2001, Linear Programming: Foundations and Extensions, 2nd ed. (Boston: Kluwer). [Undergraduate/graduate text]   
Numerical Recipes Software 2007, “Interface to AMD and LDL Packages,” Numerical Recipes Webnote No.13,at http://www.nr.com/webnotes?13[13]

# 10.12 Simulated Annealing Methods

The method of simulated annealing [1,2] is a technique that has attracted significant attention as suitable for optimization problems of large scale, especially ones where a desired global extremum is hidden among many poorer, local extrema. For practical purposes, simulated annealing has effectively “solved” the famous traveling salesman problem of finding the shortest cyclical itinerary for a traveling salesman who must visit each of $N$ cities in turn. (Other practical methods have also been found.) The method has also been used successfully for designing complex integrated circuits: The arrangement of several hundred thousand circuit elements on a tiny silicon substrate is optimized so as to minimize interference among their connecting wires [3,4]. Surprisingly, the implementation of the algorithm is relatively simple.

Notice that the two applications cited are both examples of combinatorial minimization. There is an objective function to be minimized, as usual, but the space over which that function is defined is not simply the $N$ -dimensional space of $N$ continuously variable parameters. Rather, it is a discrete, but very large, configuration space, like the set of possible orders of cities, or the set of possible allocations of silicon “real estate” blocks to circuit elements. The number of elements in the configuration space is factorially large, so that they cannot be explored exhaustively. Furthermore, since the set is discrete, we are deprived of any notion of “continuing downhill in a favorable direction.” The concept of “direction” may not have any meaning in the configuration space.

Below, we will also discuss how to use simulated annealing methods for spaces with continuous control parameters, like those of $\ S 1 0 . 5 - \ S 1 0 . 9$ . This application is actually more complicated than the combinatorial one, since the familiar problem of “long, narrow valleys” again asserts itself. Simulated annealing, as we will see, tries “random” steps; but in a long, narrow valley, almost all random steps are uphill! Some additional finesse is therefore required.

At the heart of the method of simulated annealing is an analogy with thermodynamics, specifically with the way that liquids freeze and crystallize or metals cool and anneal. At high temperatures, the molecules of a liquid move freely with respect to one another. If the liquid is cooled slowly, thermal mobility is lost. The atoms are often able to line themselves up and form a pure crystal that is completely ordered over a distance up to billions of times the size of an individual atom in all directions. This crystal is the state of minimum energy for this system. The amazing fact is that, for slowly cooled systems, nature is able to find this minimum energy state. In fact, if a liquid metal is cooled quickly or “quenched,” it does not reach this state but rather ends up in a polycrystalline or amorphous state having somewhat higher energy.

So the essence of the process is slow cooling, allowing ample time for the redistribution of the atoms as they lose mobility. This is the technical definition of annealing, and it is essential for ensuring that a low energy state will be achieved.

Although the analogy is not perfect, there is a sense in which all of the minimization algorithms thus far in this chapter correspond to rapid cooling or quenching. In all cases, we have gone greedily for the quick, nearby solution: From the starting point, go immediately downhill as far as you can go. This, as often remarked above, leads to a local, but not necessarily a global, minimum. Nature’s own minimization algorithm is based on quite a different procedure. The so-called Boltzmann probability distribution,

$$
\mathrm { P r o b } \left( E \right) \sim \mathrm { e x p } ( - E / k T )
$$

expresses the idea that a system in thermal equilibrium at temperature $T$ has its energy probabilistically distributed among all different energy states $E$ . Even at low temperature, there is a chance, albeit a very small one, of a system being in a high energy state. Therefore, there is a corresponding chance for the system to get out of a local energy minimum in favor of finding a better, more global one. The quantity $k$ (Boltzmann’s constant) is a constant of nature that relates temperature to energy. In other words, the system sometimes goes uphill as well as downhill; but the lower the temperature, the less likely is any significant uphill excursion.

In 1953, Metropolis and coworkers [5] first incorporated these kinds of principles into numerical calculations. Offered a succession of options, a simulated thermodynamic system was assumed to change its configuration from energy $E _ { 1 }$ to energy $E _ { 2 }$ with probability $p = \exp [ - ( E _ { 2 } - E _ { 1 } ) / k T ]$ . Notice that if $E _ { 2 } < E _ { 1 }$ , this probability is greater than unity; in such cases the change is arbitrarily assigned a probability $p = 1$ , i.e., the system always took such an option. This general scheme, of always taking a downhill step while sometimes taking an uphill step, has come to be known as the Metropolis algorithm.

To make use of the Metropolis algorithm for other than thermodynamic systems, one must provide the following elements:

1. A description of possible system configurations.   
2. A generator of random changes in the configuration; these changes are the “options” presented to the system.   
3. An objective function $E$ (analog of energy) whose minimization is the goal of the procedure.   
4. A control parameter $T$ (analog of temperature) and an annealing schedule that tells how it is lowered from high to low values, e.g., after how many random changes in configuration is each downward step in $T$ taken, and how large is that step. The meaning of “high” and “low” in this context, and the assignment of a schedule, may require physical insight and/or trial-and-error experiments.

We will return to these ideas in $\ S 1 5 . 8$ , with a more rigorous discussion of Markov chain Monte Carlo and the Metropolis-Hastings algorithm.

# 10.12.1 Combinatorial Minimization: The Traveling Salesman

A concrete illustration is provided by the traveling salesman problem. The proverbial seller visits $N$ cities with given positions $( x _ { i } , y _ { i } )$ , returning finally to his or her city of origin. Each city is to be visited only once, and the route is to be made as short as possible. This problem belongs to a class known as NP-complete problems, whose computation time for an exact solution increases with $N$ as $\mathrm { e x p } ( \mathrm { c o n s t . } \times N )$ , becoming rapidly prohibitive in cost as $N$ increases. The traveling salesman problem also belongs to a class of minimization problems for which the objective function $E$ has many local minima. In practical cases, it is often enough to be able to choose from these a minimum that, even if not absolute, cannot be significantly improved upon. The annealing method manages to achieve this, while limiting its calculations to scale as a small power of $N$ .

As a problem in simulated annealing, the traveling salesman problem is handled as follows:

1. Configuration. The cities are numbered $i = 0 \dots N - 1$ and each has coordinates $( x _ { i } , y _ { i } )$ . A configuration is a permutation of the number $0 \ldots N - 1$ , interpreted as the order in which the cities are visited.   
2. Rearrangements. An efficient set of moves has been suggested by Lin [6]. The moves consist of two types: (i) A section of path is removed and then replaced with the same cities running in the opposite order; or (ii) a section of path is removed and then replaced in between two cities on another, randomly chosen, part of the path.   
3. Objective function. In the simplest form of the problem, $E$ is taken just as the total length of the journey,

$$
E = L \equiv \sum _ { i = 0 } ^ { N - 1 } \sqrt { ( x _ { i } - x _ { i + 1 } ) ^ { 2 } + ( y _ { i } - y _ { i + 1 } ) ^ { 2 } }
$$

with the convention that point $N$ is identified with point 0. To illustrate the flexibility of the method, however, we can add the following additional wrinkle: Suppose that the salesman has an irrational fear of flying over the Missis-

sippi River. In that case, we would assign each city a parameter $\mu _ { i }$ , equal to $+ 1$ if it is east of the Mississippi and $^ { - 1 }$ if it is west, and take the objective function to be

$$
E = \sum _ { i = 0 } ^ { N - 1 } \left[ \sqrt { ( x _ { i } - x _ { i + 1 } ) ^ { 2 } + ( y _ { i } - y _ { i + 1 } ) ^ { 2 } } + \lambda ( \mu _ { i } - \mu _ { i + 1 } ) ^ { 2 } \right]
$$

A penalty $4 \lambda$ is thereby assigned to any river crossing. The algorithm now finds the shortest path that avoids crossings. The relative importance that it assigns to length of path versus river crossings is determined by our choice of $\lambda$ . Figure 10.12.1 shows the results obtained. Clearly, this technique can be generalized to include many conflicting goals in the minimization.

4. Annealing schedule. This requires experimentation. We first generate some random rearrangements, and use them to determine the range of values of $\Delta E$ that will be encountered from move to move. Choosing a starting value for the parameter $T$ that is considerably larger than the largest $\Delta E$ normally encountered, we proceed downward in multiplicative steps each amounting to a $10 \%$ decrease in $T$ . We hold each new value of $T$ constant for, say, $1 0 0 N$ reconfigurations, or for $1 0 N$ successful reconfigurations, whichever comes first. When efforts to reduce $E$ further become sufficiently discouraging, we stop.

In a Webnote [7], we give a complete implementation of the above ideas for the traveling salesman problem, using the Metropolis algorithm.

# 10.12.2 Continuous Minimization by Simulated Annealing

The basic ideas of simulated annealing are also applicable to optimization problems with continuous $N$ -dimensional control spaces, e.g., finding the (ideally, global) minimum of some function $f ( \mathbf { x } )$ , in the presence of many local minima, where $\mathbf { X }$ is an $N$ -dimensional vector. The four elements required by the Metropolis procedure are now as follows: The value of $f$ is the objective function. The system state is the point $\mathbf { X }$ . The control parameter $T$ is, as before, something like a temperature, with an annealing schedule by which it is gradually reduced. And there must be a generator of random changes in the configuration, that is, a procedure for taking a random step from $\mathbf { X }$ to $\mathbf { x } + \Delta \mathbf { x }$ .

The last of these elements is the most problematical. The literature to date [8-12] describes several different schemes for choosing $\Delta \mathbf { x }$ , none of which, in our view, inspires complete confidence. The problem is one of efficiency: A generator of random changes is inefficient if, when local downhill moves exist, it nevertheless almost always proposes an uphill move. A good generator, we think, should not become inefficient in narrow valleys, nor should it become more and more inefficient as convergence to a minimum is approached. Except possibly for [8], all of the schemes that we have seen are inefficient in one or both of these situations.

Our own way of doing simulated annealing minimization on continuous control spaces is to use a modification of the downhill simplex method (-10.5). Complete code for this is given in a Webnote [9]. The technique amounts to replacing the single point $\mathbf { X }$ as a description of the system state by a simplex of $N + 1$ points. The “moves” are the same as described in $\ S 1 0 . 5$ , namely reflections, expansions, and contractions of the simplex. The implementation of the Metropolis procedure is slightly subtle: We add a positive, logarithmically distributed random variable, proportional to the temperature $T$ , to the stored function value associated with every vertex of the simplex, and we subtract a similar random variable from the function value of every new point that is tried as a replacement point. Like the ordinary Metropolis procedure, this method always accepts a true downhill step, but sometimes accepts an uphill one. In the limit $T  0$ , this algorithm reduces exactly to the downhill simplex method and converges to a local minimum.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0009_pages_0561-0630/auto/images/f3d3b8bf200243299c5ea2a5c17978b05c2b7e908028d0aef9a0a8b43e13dbe0.jpg)  
Figure 10.12.1. Traveling salesman problem solved by simulated annealing. The (nearly) shortest path among 100 randomly positioned cities is shown in (a). The dotted line is a river, but there is no penalty in crossing. In (b) the river-crossing penalty is made large, and the solution restricts itself to the minimum number of crossings, two. In (c) the penalty has been made negative: The salesman is actually a smuggler who crosses the river on the flimsiest excuse!

At a finite value of $T$ , the simplex expands to a scale that approximates the size of the region that can be reached at this temperature, and then executes a stochastic, tumbling Brownian motion within that region, sampling new, approximately random, points as it does so. The efficiency with which a region is explored is independent of its narrowness (for an ellipsoidal valley, the ratio of its principal axes) and orientation. If the temperature is reduced sufficiently slowly, it becomes highly likely that the simplex will shrink into that region containing the lowest relative minimum encountered.

As in all applications of simulated annealing, there can be quite a lot of problemdependent subtlety in the phrase “sufficiently slowly”; success or failure is quite often determined by the choice of annealing schedule. Here are some possibilities worth trying:

- Reduce $T$ to $( 1 - \epsilon ) T$ after every $m$ moves, where $\epsilon / m$ is determined by experiment.   
Budget a total of $K$ moves, and reduce $T$ after every $m$ moves to a value $T = T _ { 0 } ( 1 - k / K ) ^ { \alpha }$ , where $k$ is the cumulative number of moves thus far, and $\alpha$ is a constant, say 1, 2, or 4. The optimal value for $\alpha$ depends on the statistical distribution of relative minima of various depths. Larger values of $\alpha$ spend more iterations at lower temperature.   
- After every $m$ moves, set $T$ to $\beta$ times $f _ { 1 } - f _ { b }$ , where $\beta$ is an experimentally determined constant of order 1, $f _ { 1 }$ is the smallest function value currently represented in the simplex, and $f _ { b }$ is the best function ever encountered. However, never reduce $T$ by more than some fraction $\gamma$ at a time.

Another strategic question is whether to do an occasional restart, where a vertex of the simplex is discarded in favor of the “best-ever” point. (You must be sure that the best-ever point is not one of the other vertices of the simplex when you do this!) We have found problems for which restarts — every time the temperature has decreased by a factor of 3, say — are highly beneficial; we have found other problems for which restarts have no positive, or a somewhat negative, effect.

There is not yet enough practical experience with the method of simulated annealing to say definitively what its place among optimization methods is. The method has several extremely attractive features that are rather unique when compared with other optimization techniques.

First, it is not “greedy,” in the sense that it is not easily fooled by the quick payoff achieved by falling into unfavorable local minima. Provided that sufficiently general reconfigurations are given, it wanders freely among local minima of depth less than about $T$ . As $T$ is lowered, the number of such minima qualifying for frequent visits is gradually reduced.

Second, configuration decisions tend to proceed in a logical order. Changes that cause the greatest energy differences are sifted over when the control parameter $T$ is large. These decisions become more permanent as $T$ is lowered, and attention then shifts more to smaller refinements in the solution. For example, in the traveling salesman problem with the Mississippi River twist, if $\lambda$ is large, a decision to cross the Mississippi only twice is made at high $T$ , while the specific routes on each side of the river are determined only at later stages.

The analogies to thermodynamics may be pursued to a greater extent than we have done here. Quantities analogous to specific heat and entropy may be defined, and these can be useful in monitoring the progress of the algorithm toward an acceptable solution [1].

# CITED REFERENCES AND FURTHER READING:

Salamon, P., Sibani, P., and Frost, R. 2002, Facts, Conjectures, and Improvements for Simulated Annealing (New York: SIAM Press).   
van Laarhoven, P.J.M., and Aarts, E.H.L. 1987, Simulated Annealing: Theory and Applications (Berlin: Springer).   
Kirkpatrick, S., Gelatt, C.D., and Vecchi, M.P. 1983, “Optimization by Simulated Annealing,” Science,vol.220,pp.671-680.[1]   
Kirkpatrick, S. 1984, “Optimization by Simulated Annealing: Quantitative Studies,” Journal of Statistical Physics,vol.34,pp.975-986.[2]   
Vecchi, M.P. and Kirkpatrick, S. 1983, “Global Wiring by Simulated Annealing,” IEEE Transactions on Computer Aided Design,vol. CAD-2,pp.215-222.[3]   
Otten, R.H.J.M., and van Ginneken, L.P.P.P. 1989, The Annealing Algorithm (Boston: Kluwer) [contains many references to the literature].[4]   
Metropolis, N., Rosenbluth, A., Rosenbluth, M., Teller A., and Teller, E. 1953, “Equations of State Calculations by Fast Computing Machines,” Journal of Chemical Physics, vol. 21, pp. 1087–1092.[5]   
Lin, S. 1965, “Computer Solutions of the Traveling Salesman Problem,” Bell System Technical Journal,vol.44,pp.2245-2269.[6]   
Numerical Recipes Software 2007, “Code Implementation for the Traveling Salesman Problem,” Numericai Recipes Webnote No.14,at http://www.nr.com/webnotes?14 [7]   
Vanderbilt, D., and Louie, S.G. 1984, “A Monte Carlo Simulated Annealing Approach to Optimization over Continuous Variables,” Journal of Computational Physics, vol. 56, pp. 259–271.[8]   
Numerical Recipes Software 2007, “Code for Minimization with Simulated Annealing,” Numerical Recipes Webnote No. 15,at http://www.nr.com/webnotes?15 [9]   
Bohachevsky, I.O., Johnson, M.E., and Stein, M.L. 1986, “Generalized Simulated Annealing for Function Optimization,” Technometrics, vol. 28, pp. 209–217.[10]   
Corana, A., Marchesi, M., Martini, C., and Ridella, S. 1987, “Minimizing Multimodal Functions of Continuous Variables with the Simulated Annealing Algorithm,” ACM Transactions on Mathematical Software,vol.13,pp. 262-280.[11]   
Bélisle, C.J.P., Romeijn, H.E., and Smith, R.L. 1990, “Hide and Seek: A Simulated Annealing Algorithm for Global Optimization,” Technical Report 90–25, Department of Industrial and Operations Engineering, University of Michigan.[12]   
Christofides, N., Mingozzi, A., Toth, P., and Sandi, C. (eds.) 1979, Combinatorial Optimization (London and New York: Wiley-Interscience) [not simulated annealing, but other topics and algorithms].

# 10.13 Dynamic Programming

Dynamic programming, or $D P$ , is an optimization technique that applies when a known sequence of choices, each with a cost or benefit, is to be made and one wants to minimize the total cost, or maximize the total benefit, after the sequence has been traversed. More specifically, a problem that is amenable to dynamic programming can be broken up into an ordered series of discrete stages, and within each stage a set of discrete states. These stages and states form a directed graph (see Figure 10.13.1) that we want to traverse from a given starting state $( i = 0 )$ ) to a given ending state $( i = N$ ). Allowed decisions that take one from state $j$ in stage $i$ to state $k$ in stage $i + 1$ are edges in the graph. Their cost is denoted $c _ { j k } ( i )$ . Without any loss of generality, one can connect all the states in stage $i$ to all the states in stage $i + 1$ , but with $c _ { j k } ( i ) = \infty$ for forbidden paths.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0009_pages_0561-0630/auto/images/752bd970cb6354e0a86122336d43e7921ff77f3d02731b742bef5d46d53f1c31.jpg)  
Figure 10.13.1. Canonical dynamical programming problem. It is desired to find the lowest cost path from a starting state to an ending state through $N - 1$ intermediate stages. Each stage is characterized by a set of states (not necessarily the same at each stage). An allowed edge between state $j$ in stage $i$ and state $k$ in stage $i + 1$ has a cost denoted $c _ { j k } ( i )$ (not all labeled in the figure).

Computer science is rich in graph-theoretic problems and algorithms, but only a few of these are within the scope of this book. Dynamic programming is one of these because its basic idea is very simple and its applications are very broad. It is important that you be able to recognize a problem amenable to DP when you see one. In particular, we will use several of the concepts in this section later, in $\ S 1 6 . 2$ , when we discuss the estimation of states from probabilistic data, including probabilistic decoding algorithms.

The key idea of dynamic programming is called the Bellman, Dijkstra, or Viterbi algorithm, depending on the field of training of the caller. As shown in Figure 10.13.2, the idea is that one can do a single sweep of a stage-ordered graph from left to right, labeling each vertex by the single number that is the cost of the best way of having reached it. (Henceforth we’ll take the canonical DP problem as a costminimization problem; if your problem is instead a benefit-maximization problem, just use the negative of your benefits as costs.)

When the end state is reached, the global minimum cost of getting to it becomes known. Now, in a single backward pass, we can read off exactly what set of decisions led to this global minimum, by reconstructing which predecessor state was the one actually in the chain that led to the best result. Arriving back at the starting state, our solution is complete.

The art of DP involves, in many cases, the clever organization of the problem to minimize the number of states at each stage, so as to avoid the “curse of dimensionality” (a phrase first used by Bellman in exactly this context). Sometimes the order of the stages is not chronological at all, but merely reflects the decomposition of a

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0009_pages_0561-0630/auto/images/f4a48567b99b58f3cfec1ef2908f9e512f8a987fe5403f725c1169cf4a4e85ba.jpg)  
Figure 10.13.2. Two snapshots during the solution of a DP problem by the Bellman-Dijkstra-Viterbi algorithm. Edge costs are given as shown. Top: During the rightward sweep (here not yet complete) each state is labeled by the minimum cost to reach it, as determined solely by the labels of the preceding stage and the connecting edge costs. Bottom: After the rightward sweep is complete, the unique set of edges that produce the global minimum is found by one pass of backtracking.

problem into a convenient form for DP.

Here is a function embodying the Bellman-Dijkstra-Viterbi algorithm. You should consider this function more a precise statement of the algorithm than a production DP code. For example, it simply pushes off to the user function cost() the important issue of how to retrieve efficiently the (usually) sparse set of allowed edges that have finite costs. (You might want to consider a hash memory. See $\ S 7 . 6 .$ ） Also, this routine loops explicitly over all combinations of states $j$ and $k$ , the origin and destination states in going from stage $i$ to $i ~ + ~ 1$ . If you have a problem big enough to need some kind of sparse lookup, then you’ll want to change these explicit loops accordingly.

# VecInt dynpro(const VecInt &nstate,

Doub cost(Int jj, Int kk, Int ii)) {

Given the vector nstate whose integer values are the number of states in each stage (1 for the first and last stages), and given a function cost $( \mathbf { j } , \mathbf { k } , \mathbf { i } )$ that returns the cost of moving between state $\dot { \mathsf { J } }$ of stage i and state k of stage $\dot { \ b { \mathrm { 1 } } } + \ b { \mathrm { 1 } }$ , this routine returns a vector of the same length as nstate containing the state numbers of the lowest cost path. States number from 0, and the first and last components of the returned vector will thus always be 0.

static const Doub EP $\mathrm { { \sf S } } =$ numeric_limits<Doub>::epsilon();   
Int i, j ,k, nstage $=$ nstate.size() - 1;   
Doub a,b;   
VecInt answer(nstage+1);   
if (nstate[0] $\ ! = ~ 1$ || nstate[nstage] $\downarrow = ~ 1$ ) throw("One state allowed in first and last stages.");   
Doub \*\*best $=$ new Doub\*[nstage $+ 1 ]$ ; Allocate array-of-arrays for storing score   
best[0] $=$ new Doub[nstate[0]];   
best[0][0] $\mathit { \Theta } = \mathit { \Theta } 0 .$ ;   
for $\scriptstyle \dot { \underline { { \cdot } } } = 1$ ; $\div < =$ nstage; $\dot { \bar { \lambda } } + +$ ) { Forward sweep through stages. best[i] $=$ new Doub[nstate[i]]; for $\scriptstyle ( \mathtt { k } = 0$ ; k<nstate[i]; $\mathrm { k } { + } { + }$ ) { b $=$ BIG; for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<nstate[i-1]; ${ \mathrm { j } } + +$ ) { Find predecessor giving min cost. if ( $\mathtt { ( a \ = }$ best[i-1][j] $^ +$ cost(j,k,i-1)) < b) $\texttt { b } = \texttt { a }$ ; } best[i][k] = b; }   
}   
answer[nstage] $=$ answer[0] $\qquad = \ 0$ ;   
for ( $\mathrm { i } =$ nstage-1; i>0; i--) { Backtracking pass. $\mathrm { ~ \bf ~ k ~ } =$ answer[i+1]; b $=$ best[i+1][k]; for (j ${ = } 0$ ; j<nstate[i]; ${ \mathrm { j } } + +$ ) { Find a predecessor that gave min. Doub temp $=$ best[i][j] $^ +$ cost(j,k,i); if (fabs(b - temp) $< =$ EPS\*fabs(temp)) break; } answer[i] = j;   
}   
for ( $\dot { \bf 1 } =$ nstage; $\scriptstyle \dot { 1 } > = 0$ ; i--) delete [] best[i]; Cleanup storage.   
delete [] best;   
return answer;

# 10.13.1 Example: Order of Matrix Multiplication

Suppose we have five matrices to multiply, so as to get a result T ,

$$
\mathbf { T } = \mathbf { A } \mathbf { B } \mathbf { C } \mathbf { D } \mathbf { E }
$$

The matrices may all have different shapes, as long as the number of columns of a matrix is the same as the number of rows of the matrix immediately to its right. Matrix multiplication is associative, and we can do the multiplies in any order we want; but the total number of scalar multiplications can be quite different, depending on which order is chosen. You should be able to see this in the following figure:

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0009_pages_0561-0630/auto/images/56828a855cc3eee533a7c8008b01ba290699ee976a291353d6054b882b4721e5.jpg)

What we want to minimize is the total number of scalar multiplications. In this example, a good choice of “stage” is just how many matrix multiplications have been performed. So the stages and states might look something like this:

<table><tr><td rowspan=1 colspan=1>Stage 0</td><td rowspan=1 colspan=1>Stage 1</td><td rowspan=1 colspan=1>Stage 2</td><td rowspan=1 colspan=1>Stage 3</td><td rowspan=1 colspan=1>Stage 4</td></tr><tr><td rowspan=1 colspan=1>ABCDE</td><td rowspan=1 colspan=1>(AB)CDEA(BC)DEAB(CD)EABC(DE)</td><td rowspan=1 colspan=1>(ABC)DE(AB)(CD)E(AB)C(DE)A(BCD)EA(BC)(DE)AB(CDE)</td><td rowspan=1 colspan=1>(ABCD)E(ABC)(DE)(AB)(CDE)A(BCDE)</td><td rowspan=1 colspan=1>(ABCDE)</td></tr></table>

Here parentheses group matrix factors that are already fully multiplied (i.e., they are, by now, a single matrix). We will leave it to you to connect the states by allowed edges, and to calculate the cost of each edge in terms of the dimensions of the various matrices.

So how could we have done this example wrong? We might have identified states with all possible ways of parenthesizing ABCDE, including, for example, $\mathbf { A } ( \mathbf { B } ( \mathbf { C D } ) \mathbf { E } )$ . That is unnecessary, because only the outermost parentheses matter: A matrix state doesn’t care about the exact path taken to reach it, as long as its factors were multiplied in some associative order. The power of DP is realized when, at every stage, many histories collapse to a (relatively) small number of states, which can then be taken as ignorant of their past history.

# 10.13.2 Example: DNA Sequence Alignment

DNA sequences of different organisms, at one time identical in a common ancestor, can diverge over time by the deletion, insertion, or substitution of bases in one or the other organism’s sequence. It is desired to find the best match between two given sequences. In finding the best match, we are allowed to insert gaps in either sequence; but in the end we will be assessed a penalty for gap positions, a penalty for mismatches, and a reward for matches.

For example [2], before matching, we might have the two sequences

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0009_pages_0561-0630/auto/images/154fb5c507a5f14f6282ae3233cf4a07ca68c8560cf4488ca7c742db40e54cb6.jpg)

A possible match might be

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0009_pages_0561-0630/auto/images/bec93cd2903a7c6372471fd930aae2db771328fa88a0ef6d8b74b4789f423b59.jpg)

for which we would earn six rewards, less one mismatch penalty (shown italic) and four gap penalties. (We will consider all rewards and penalties as having positive or zero values, with the accounting done by adding rewards and subtracting penalties.)

Needleman and Wunsch [1] first pointed out that this problem is amenable to solution by DP, allowing all possible matchings to be scored, and the highest-scoring one identified. The clever idea is to form a two-dimensional array with the two sequences defining the columns and rows. In the above example, this looks like

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>G</td><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>G</td><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>A</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>G</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>G</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>G</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

A matching consists of a path through the (initially) empty boxes in the above tableau, starting in the box labeled by a zero and moving, in each step, either one box right, one box down, or diagonally down and right. A right or down move corresponds to using up a letter in the first or second sequence (respectively) without using up one in the second or first (respective) sequence. Therefore it corresponds to inserting a gap and incurs a gap penalty. A diagonal move corresponds to pairing a new character in each sequence. Therefore, it incurs either the matching reward, if the two sequences match, or a mismatch penalty, if they don’t.

Also useful is to distinguish right or down moves between two boxes in the bordering rows or columns (respectively) of the table from right or down moves in the interior of the table. The former kind don’t open gaps in either sequence, but merely allow the sequences to shift with respect to one another. So we might assess a smaller, or zero, penalty for these overall “skews.”

Now, characteristic of dynamic programming, you just fill in the boxes with the total score of the best way to reach that box, either from above it, from its left, or from the upper-left diagonal neighbor. A score is computed, naturally, by taking the score of a predecessor box and then adding the reward (or subtracting the penalty) associated with the move. Starting at the upper left, there are always boxes ready to be filled in as you work your way, by rows or columns, to the lower right.

Also characteristic of dynamic programming, when you are done filling in all the boxes, you do a backtrack pass: Start at the lower right box in the table. Now figure out the path back through the table that contributed to that best score. (It may not be unique.) Finally, translate that path into the series of letters and gaps that it implies.

A straightforward implementation of this is the following routine. Note that the matching reward is normalized to one per matched character, while the penalties for mismatches, gaps, and overall skews are input arguments. You can set all three to zero in most cases. If you set a nonzero mismatch penalty, however, you will probably also want to have a gap penalty, since otherwise the program will always avoid a mismatch by creating two gaps, one in each string.

The routine’s output includes a summary string showing where the matches, mismatches, and gaps occur. For the example above, the summary string is

$$
\scriptstyle = ! = \ = \ = \ = \ =
$$

(You can change the symbols used to your liking.)

You can modify the program in various other ways. For example, you might want to have a bigger penalty for initially opening a gap than for extending it once opened. This requires a more complicated logic in the initial filling of the cost table. As long as you are able to fill each box with the cost of the best way to reach it, then the logic of dynamic programming will still apply.

void stringalign(char \*ain, char \*bin, Doub mispen, Doub gappen, Doub skwpen, char \*aout, char \*bout, char \*summary) {

Given null terminated input strings ain and bin, and given penalties mispen, gappen, and skwpen, respectively, for mismatches, interior gaps, and gaps before/after either string, set null terminated output strings aout, bout, and summary as the aligned versions of the input strings, a summary string. User must supply storage for the output strings of size equal to the sum of the two input strings.

Int i,j,k;   
Doub dn,rt,dg; Cost of down, right, and diagonal moves.   
Int ia $=$ strlen(ain), ib $=$ strlen(bin);   
MatDoub cost(ia+1,ib+1); Cost table, as illustrated in the text.   
First we fill in the cost table.   
cost[0][0] $\qquad = \ 0 .$ ;   
for ( $\dot { \bf 1 } = 1$ ;i $\cdot { < } =$ ia; $\dot { \bf 1 } + +$ ) cost[i][0] $=$ cost[i-1][0] $^ +$ skwpen;   
for ( $\dot { 1 } = 1$ ; $\mathrm { i } < =$ ib; $\dot { 1 } + +$ ) cost[0][i] $=$ cost[0][i-1] $^ +$ skwpen;   
for ( $\dot { \bf 1 } = 1$ ; $\mathrm { i } < =$ ia;i++) for ( $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j $< =$ ib;j++) { dn $=$ cost[i-1][j] $^ +$ ((j $= =$ ib)? skwpen : gappen); $\begin{array} { r l } { \mathbb { r } \ t } & { { } = } \end{array}$ cost[i][j-1] $^ +$ ( $\mathbf { \dot { \beta } } _ { \dot { \mathbf { 1 } } } \mathbf { \beta } = \mathbf { = }$ ia)? skwpen : gappen); $\mathrm { d } \mathrm { g } \ =$ cost[i-1][j-1] $^ +$ ((ain[i-1] $= =$ bin[j-1])? -1. : mispen); cost[i][j] $=$ MIN(MIN(dn,rt),dg);   
}   
Next, we do the backtrack pass, writing the output (backward, however).   
$\dot { \bf 1 } =$ ia; j=ib; $\mathtt { k } = 0$ ;   
while ( $\mathrm { ~  ~ \dot { ~ } { ~ i ~ } ~ } > \mathrm { ~  ~ 0 ~ } \ | \mathrm { ~  ~ \dot { ~ } { ~ j ~ } ~ } > \mathrm { ~  ~ 0 ~ } )$ { $\mathrm { d } \mathrm { n ~ \ : = ~ \mathrm { r t ~ \in ~ \mathrm { d } \mathrm { g ~ \stackrel { ~ } { ~ = ~ \mathrm { ~ \scriptsize ~ 9 ~ . ~ } ~ } ~ } ~ } }$ 99e99; Any large value will do. if (i>0) dn $=$ cost[i-1][j] $^ +$ $( ( \ j { = } = \mathrm { i b } )$ )? skwpen : gappen); if $\mathrm { ( j } > 0 \mathrm { ) }$ ) rt $=$ cost[i][j-1] $^ +$ (( $\dot { \bf 1 } = =$ ia)? skwpen : gappen); if (i>0 && $\mathrm { j } > 0$ ) dg $=$ cost[i-1][j-1] $^ +$ ((ain[i-1] $= =$ bin[j-1])? -1. : mispen); if (dg $< =$ MIN(dn,rt)) { Diagonal move produces either match or inaout[k] $=$ ain[i-1]; equality. bout[k] $=$ bin[j-1]; summary[k++] $=$ ((ain[i-1] $= =$ bin[j-1])? ’=’ i--; j--; } else if (dn $<$ rt) { Down move produces a gap in the B string. aout[k] $=$ ain[i-1]; bout[k] = ’ ’; summary $\mathbf { k } + + \mathbf { l } = \mathbf { \Omega } ,$ i--; } else { Right move produces a gap in the A string. aout[k] = ’ ’; bout[k] $=$ bin[j-1]; summary[ $\mathbf { k } + + \mathbf { J } = \mathbf { \lambda } ^ { , } \mathbf { \lambda } ;$ j }   
}   
Finally, reverse the output strings.   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<k/2;i++) { SWAP(aout[i],aout[k-1-i]); SWAP(bout[i],bout[k-1-i]); SWAP(summary[i],summary[k-1-i]);   
}   
aout[k] $=$ bout[k] $=$ summary[k] $\qquad = \ 0$ ; Don’t forget the terminating nulls!

notably the generalization by Smith and Waterman [3]. There are also a number of heuristic methods for identifying sequence similarity, with names like BLAST, FASTA, BLAT, etc. The field is highly developed, so you should use the routine above only pedagogically.

# CITED REFERENCES AND FURTHER READING:

Cybenko, G. 1997, “Dynamic Programming: A Discrete Calculus of Variations,” IEEE Computational Science and Engineering,vol.4,no.1,pp.92-97.   
Bertsekas, 2001, Dynamic Programming and Optimal Control, 2nd ed., 2 vols. (Belmont, MA: Athena Scientific).   
Hillier, F.S. and Lieberman, G.J. 2002, Introduction to Operations Research, 7th ed. (New York: McGraw-Hill).   
Needleman, S.B. and Wunsch, C.D. 1970, “A General Method Applicable to the Search for Similarities in the Amino Acid Sequence of Two Proteins,” Journal of Molecular Biology, vol. 48, pp. 443-453.[1]   
Rouchka, E.C. 2001, “Dynamic Programming,” at multiple Web sites.[2]   
Smith, T.F. and Waterman, M.S. 1981, “Identification of Common Molecular Subsequences,” Journal of Molecular Biology,vol.147,pp.195-197.[3]

# 11.0 Introduction

An $N \times N$ matrix $\mathbf { A }$ is said to have an eigenvector $\mathbf { X }$ and corresponding eigenvalue $\lambda$ if

$$
\mathbf { A } \cdot \mathbf { x } = \lambda \mathbf { x }
$$

Obviously any multiple of an eigenvector $\mathbf { X }$ will also be an eigenvector, but we won’t consider such multiples as being distinct eigenvectors. (The zero vector is not considered to be an eigenvector at all.) Evidently (11.0.1) can hold only if

$$
\operatorname* { d e t } | \mathbf { A } - \lambda \mathbf { 1 } | = 0
$$

which, if expanded out, is an $N$ th degree polynomial in $\lambda$ whose roots are the eigenvalues. This proves that there are always $N$ (not necessarily distinct) eigenvalues. Equal eigenvalues coming from multiple roots are called degenerate. Root searching in the characteristic equation (11.0.2) is usually a very poor computational method for finding eigenvalues. We will learn much better ways in this chapter, as well as efficient ways for finding corresponding eigenvectors.

The above two equations also prove that every one of the $N$ eigenvalues has a (not necessarily distinct) corresponding eigenvector: If $\lambda$ is set to an eigenvalue, then the matrix $\mathbf { A } - \lambda \mathbf { 1 }$ is singular, and we know that every singular matrix has at least one nonzero vector in its nullspace (see $\ S 2 . 6 . 1 \rangle$ .

If you add $\tau \mathbf { X }$ to both sides of (11.0.1), you will easily see that the eigenvalues of any matrix can be changed or shifted by an additive constant $\tau$ by adding to the matrix that constant times the identity matrix. The eigenvectors are unchanged by this shift. Shifting, as we will see, is an important part of many algorithms for computing eigenvalues. We see also that there is no special significance to a zero eigenvalue. Any eigenvalue can be shifted to zero, or any zero eigenvalue can be shifted away from zero.

# 11.0.1 Definitions and Basic Facts

A matrix is called symmetric if it is equal to its transpose,

$$
{ \bf A } = { \bf A } ^ { T } \qquad \mathrm { o r } \qquad a _ { i j } = a _ { j i }
$$

It is called Hermitian or self-adjoint if it equals the complex conjugate of its transpose (its Hermitian conjugate, denoted by “”)

$$
\mathbf { A } = \mathbf { A } ^ { \dagger } \qquad { \mathrm { o r } } \qquad a _ { i j } = a _ { j i } *
$$

It is termed orthogonal if its transpose equals its inverse,

$$
\mathbf { A } ^ { T } \cdot \mathbf { A } = \mathbf { A } \cdot \mathbf { A } ^ { T } = \mathbf { 1 }
$$

and unitary if its Hermitian conjugate equals its inverse. Finally, a matrix is called normal if it commutes with its Hermitian conjugate,

$$
\mathbf { A \cdot A ^ { \dagger } } = \mathbf { A ^ { \dagger } } \cdot \mathbf { A }
$$

For real matrices, Hermitian means the same as symmetric, unitary means the same as orthogonal, and both of these distinct classes are normal.

The reason that Hermitian is an important concept has to do with eigenvalues. The eigenvalues of a Hermitian matrix are all real. In particular, the eigenvalues of a real symmetric matrix are all real. Contrariwise, the eigenvalues of a real nonsymmetric matrix may include real values, but may also include pairs of complexconjugate values; and the eigenvalues of a complex matrix that is not Hermitian will in general be complex.

The reason that normal is an important concept has to do with the eigenvectors. The eigenvectors of a normal matrix with nondegenerate (i.e., distinct) eigenvalues are complete and orthogonal, spanning the $N$ -dimensional vector space. For a normal matrix with degenerate eigenvalues, we have the additional freedom of replacing the eigenvectors corresponding to a degenerate eigenvalue by linear combinations of themselves. Using this freedom, we can always perform Gram-Schmidt orthogonalization (consult any linear algebra text) and find a set of eigenvectors that are complete and orthogonal, just as in the nondegenerate case. The matrix whose columns are an orthonormal set of eigenvectors is evidently unitary. A special case is that the matrix of eigenvectors of a real symmetric matrix is orthogonal, since the eigenvectors of that matrix are all real.

When a matrix is not normal, as typified by any random, nonsymmetric, real matrix, then in general we cannot find any orthonormal set of eigenvectors, nor even any pairs of eigenvectors that are orthogonal (except perhaps by rare chance). While the $N$ nonorthonormal eigenvectors will “usually” span the $N$ -dimensional vector space, they do not always do so; that is, the eigenvectors are not always complete. Such a matrix is said to be defective.

# 11.0.2 Left and Right Eigenvectors

While the eigenvectors of a nonnormal matrix are not particularly orthogonal among themselves, they do have an orthogonality relation with a different set of vectors, which we must now define. Up to now our eigenvectors have been column vectors that are multiplied to the right of a matrix A, as in (11.0.1). These, more explicitly, are termed right eigenvectors. We could also, however, try to find row vectors, which multiply A to the left and satisfy

$$
{ \bf x } \cdot { \bf A } = \lambda { \bf x }
$$

These are called left eigenvectors. By taking the transpose of equation (11.0.7), we see that every left eigenvector is the transpose of a right eigenvector of the transpose of A. Now, by comparing to (11.0.2) and using the fact that the determinant of a matrix equals the determinant of its transpose, we also see that the left and right eigenvalues of A are identical.

If the matrix A is symmetric, then the left and right eigenvectors are just transposes of each other, that is, they have the same numerical components. Likewise, if the matrix is self-adjoint, the left and right eigenvectors are Hermitian conjugates of each other. For the general nonnormal case, however, we have the following calculation: Let $\mathbf { X } _ { R }$ be the matrix formed by columns from the right eigenvectors and $\mathbf { X } _ { L }$ be the matrix formed by rows from the left eigenvectors. Then (11.0.1) and (11.0.7) can be rewritten as

$$
\mathbf { A } \cdot \mathbf { X } _ { R } = \mathbf { X } _ { R } \cdot \mathrm { d i a g } ( \lambda _ { 0 } \ldots \lambda _ { N - 1 } ) \qquad \mathbf { X } _ { L } \cdot \mathbf { A } = \mathrm { d i a g } ( \lambda _ { 0 } \ldots \lambda _ { N - 1 } ) \cdot \mathbf { X } _ { L }
$$

Multiplying the first of these equations on the left by $\mathbf { X } _ { L }$ , the second on the right by $\mathbf { X } _ { R }$ , and subtracting the two, gives

$$
( { \bf X } _ { L } \cdot { \bf X } _ { R } ) \cdot \mathrm { d i a g } ( \lambda _ { 0 } \ldots \lambda _ { N - 1 } ) = \mathrm { d i a g } ( \lambda _ { 0 } \ldots \lambda _ { N - 1 } ) \cdot ( { \bf X } _ { L } \cdot { \bf X } _ { R } )
$$

This says that the matrix of dot products of the left and right eigenvectors commutes with the diagonal matrix of eigenvalues. But the only matrices that commute with a diagonal matrix of distinct elements are themselves diagonal. Thus, if the eigenvalues are nondegenerate, each left eigenvector is orthogonal to all right eigenvectors except its corresponding one, and vice versa. By choice of normalization, the dot products of corresponding left and right eigenvectors can always be made unity for any matrix with nondegenerate eigenvalues.

If some eigenvalues are degenerate, then either the left or the right eigenvectors corresponding to a degenerate eigenvalue must be linearly combined among themselves to achieve orthogonality with the right or left ones, respectively. This can always be done by a procedure akin to Gram-Schmidt orthogonalization. The normalization can then be adjusted to give unity for the nonzero dot products between corresponding left and right eigenvectors. If the dot product of corresponding left and right eigenvectors is zero at this stage, then you have a case where the eigenvectors are incomplete! Note that incomplete eigenvectors can occur only where there are degenerate eigenvalues, but they do not always occur in such cases (in fact, they never occur for the class of “normal” matrices). See [1] for a clear discussion.

In both the degenerate and nondegenerate cases, the final normalization to unity of all nonzero dot products produces the result: The matrix whose rows are left eigenvectors is the inverse matrix of the matrix whose columns are right eigenvectors, if the inverse exists. When it does exist, equations (11.0.8) and (11.0.9) imply the useful factorizations

$$
{ \bf A } = { \bf X } _ { R } \cdot \mathrm { d i a g } ( \lambda _ { 0 } \ldots \lambda _ { N - 1 } ) \cdot { \bf X } _ { L } \quad \mathrm { a n d } \quad \mathrm { d i a g } ( \lambda _ { 0 } \ldots \lambda _ { N - 1 } ) = { \bf X } _ { L } \cdot { \bf A } \cdot { \bf X } _ { R }
$$

# 11.0.3 Diagonalization of a Matrix

From equation (11.0.10) and the fact that $\mathbf { X } _ { L }$ and $\mathbf { X } _ { R }$ are matrix inverses, we get

$$
\mathbf { X } _ { R } ^ { - 1 } \cdot \mathbf { A } \cdot \mathbf { X } _ { R } = \mathrm { d i a g } ( \lambda _ { 0 } \dots \lambda _ { N - 1 } )
$$

This is a particular case of a similarity transform of the matrix A,

$$
\begin{array} { r l r } { { \bf A } } & { { }  } & { { \bf Z } ^ { - 1 } \cdot { \bf A } \cdot { \bf Z } } \end{array}
$$

for some transformation matrix $\mathbf { Z }$ . Similarity transformations play a crucial role in the computation of eigenvalues, because they leave the eigenvalues of a matrix unchanged. This is easily seen from

$$
\begin{array} { r l } & { \operatorname* { d e t } \big | \mathbf { Z } ^ { - 1 } \cdot \mathbf { A } \cdot \mathbf { Z } - \lambda \mathbf { 1 } \big | = \operatorname* { d e t } \big | \mathbf { Z } ^ { - 1 } \cdot ( \mathbf { A } - \lambda \mathbf { 1 } ) \cdot \mathbf { Z } \big | } \\ & { \qquad = \operatorname* { d e t } | \mathbf { Z } | \operatorname* { d e t } | \mathbf { A } - \lambda \mathbf { 1 } | \operatorname* { d e t } \big | \mathbf { Z } ^ { - 1 } \big | } \\ & { \qquad = \operatorname* { d e t } | \mathbf { A } - \lambda \mathbf { 1 } | } \end{array}
$$

Equation (11.0.11) shows that any matrix with complete eigenvectors (which includes all normal matrices and “most” random nonnormal ones) can be diagonalized by a similarity transformation, that the columns of the transformation matrix that effects the diagonalization are the right eigenvectors, and that the rows of its inverse are the left eigenvectors.

For real symmetric matrices, the eigenvectors are real and orthonormal, so the transformation matrix is orthogonal. The similarity transformation is then also an orthogonal transformation of the form

$$
\begin{array} { r l r } { { \bf A } } & { { }  } & { { \bf Z } ^ { T } \cdot { \bf A } \cdot { \bf Z } } \end{array}
$$

While real nonsymmetric matrices can be diagonalized in their usual case of complete eigenvectors, the transformation matrix is not necessarily real. It turns out, however, that a real similarity transformation can “almost” do the job. It can reduce the matrix down to a form with little two-by-two blocks along the diagonal and all other elements zero. Each two-by-two block corresponds to a complex-conjugate pair of complex eigenvalues. We will see this idea exploited in some routines given later in the chapter.

The “grand strategy” of virtually all modern eigensystem routines is to nudge the matrix A toward diagonal form by a sequence of similarity transformations,

$$
\begin{array} { r l r } { \mathbf { A } } & {  } & { \mathbf { P } _ { 1 } ^ { - 1 } \cdot \mathbf { A } \cdot \mathbf { P } _ { 1 } \  \ \mathbf { P } _ { 2 } ^ { - 1 } \cdot \mathbf { P } _ { 1 } ^ { - 1 } \cdot \mathbf { A } \cdot \mathbf { P } _ { 1 } \cdot \mathbf { P } _ { 2 } } \\ & {  } & { \mathbf { P } _ { 3 } ^ { - 1 } \cdot \mathbf { P } _ { 2 } ^ { - 1 } \cdot \mathbf { P } _ { 1 } ^ { - 1 } \cdot \mathbf { A } \cdot \mathbf { P } _ { 1 } \cdot \mathbf { P } _ { 2 } \cdot \mathbf { P } _ { 3 }  \mathrm { e t c . } } \end{array}
$$

If we get all the way to diagonal form, then the eigenvectors are the columns of the accumulated transformation

$$
{ \bf X } _ { R } = { \bf P } _ { 1 } \cdot { \bf P } _ { 2 } \cdot { \bf P } _ { 3 } \cdot . . .
$$

Sometimes we do not want to go all the way to diagonal form. For example, if we are interested only in eigenvalues, not eigenvectors, it is enough to transform the matrix A to be triangular, with all elements below (or above) the diagonal zero. In this case the diagonal elements are already the eigenvalues, as you can see by mentally evaluating (11.0.2) using expansion by minors.

There are two rather different sets of techniques for implementing the grand strategy (11.0.15). It turns out that they work rather well in combination, so most modern eigensystem routines use both. The first set of techniques constructs individual $\mathbf { P } _ { i }$ ’s as explicit “atomic” transformations designed to perform specific tasks, for example zeroing a particular off-diagonal element (Jacobi transformation, $\ S 1 1 . 1 \big )$ , or a whole particular row or column (Householder transformation, $\ S 1 1 . 3$ ; elimination method, $\ S 1 1 . 6 )$ . In general, a finite sequence of these simple transformations cannot completely diagonalize a matrix. There are then two choices: either use the finite sequence of transformations to go most of the way (e.g., to some special form like tridiagonal or Hessenberg; see $\ S 1 1 . 3$ and $\ S 1 1 . 6$ below) and follow up with the second set of techniques about to be mentioned; or else iterate the finite sequence of simple transformations over and over until the deviation of the matrix from diagonal is negligibly small. This latter approach is conceptually simplest, so we will discuss it in the next section; however, for $N$ greater than $\sim 1 0$ , it is computationally inefficient by a roughly constant factor $\sim 5$ .

The second set of techniques, called factorization methods, is more subtle. Suppose that the matrix A can be factored into a left factor $\mathbf { F } _ { L }$ and a right factor $\mathbf { F } _ { R }$ . Then

$$
{ \bf A } = { \bf F } _ { L } \cdot { \bf F } _ { R } \qquad \mathrm { o r e q u i v a l e n t l y } \qquad { \bf F } _ { L } ^ { - 1 } \cdot { \bf A } = { \bf F } _ { R }
$$

If we now multiply back together the factors in the reverse order and use the second equation in (11.0.17), we get

$$
\mathbf { F } _ { R } \cdot \mathbf { F } _ { L } = \mathbf { F } _ { L } ^ { - 1 } \cdot \mathbf { A } \cdot \mathbf { F } _ { L }
$$

which we recognize as having effected a similarity transformation on A with the transformation matrix being ${ \bf F } _ { L } !$ In $\ S 1 1 . 4$ and $\ S 1 1 . 7$ we will discuss the QR method that exploits this idea.

Factorization methods also do not converge exactly in a finite number of transformations. But the better ones do converge rapidly and reliably, and, when following an appropriate initial reduction by simple similarity transformations, they are generally the methods of choice.

# 11.0.4 “Eigenpackages of Canned Eigenroutines"

You have probably gathered by now that the solution of eigensystems is a fairly complicated business. It is. It is one of the few subjects covered in this book for which we do not recommend that you avoid canned routines. On the contrary, the purpose of this chapter is precisely to give you some appreciation of what is going on inside such canned routines, so that you can make intelligent choices about using them, and intelligent diagnoses when something goes wrong.

You will find that almost all canned routines in use nowadays trace their ancestry back to routines published in Wilkinson and Reinsch’s Handbook for Automatic Computation, Vol. II, Linear Algebra [2]. This excellent reference, containing papers by a number of authors, is the Bible of the field. A public-domain implementation of the Handbook routines in Fortran is the EISPACK set of programs [3]. The routines in this chapter are translations of either the Handbook or EISPACK routines, so understanding these will take you a lot of the way toward understanding those canonical packages.

The successor to EISPACK is LAPACK [4], which also includes the linear algebra routines of LINPACK. This is a Fortran package in which a lot of attention has been paid to efficient execution on modern machines. A C translation is available as CLAPACK.

IMSL [5] and NAG [6] each provide proprietary implementations, in Fortran and C, of what are essentially the Handbook routines.

A good “eigenpackage” will provide separate routines, or separate paths through sequences of routines, for the following desired calculations:

- all eigenvalues and no eigenvectors - all eigenvalues and some corresponding eigenvectors - all eigenvalues and all corresponding eigenvectors

The purpose of these distinctions is to save compute time and storage; it is wasteful to calculate eigenvectors that you don’t need. Often one is interested only in the eigenvectors corresponding to the largest few eigenvalues, or largest few in magnitude, or few that are negative. The method usually used to calculate “some” eigenvectors is typically more efficient than calculating all eigenvectors if you desire fewer than about a quarter of the eigenvectors.

A good eigenpackage also provides separate paths for each of the above calculations for each of the following special forms of the matrix:

- real, symmetric, tridiagonal   
- real, symmetric, banded (only a small number of sub- and superdiagonals are nonzero)   
- real, symmetric   
- real, nonsymmetric   
- complex, Hermitian   
- complex, non-Hermitian

Again, the purpose of these distinctions is to save time and storage by using the least general routine that will serve in any particular application.

In this chapter, as a bare introduction, we give good routines for the following paths:

- all eigenvalues and eigenvectors of a real symmetric, tridiagonal matrix (-11.4) - all eigenvalues and eigenvectors of a real symmetric, matrix $( \ S 1 1 . 1 - \ S 1 1 . 4 )$ - all eigenvalues and eigenvectors of a complex Hermitian matrix (-11.5) - all eigenvalues and eigenvectors of a real nonsymmetric matrix $( \ S 1 1 . 6 - \ S 1 1 . 7 )$

We also discuss, in $\ S 1 1 . 8$ , how to obtain some eigenvectors of general matrices by the method of inverse iteration.

# 11.0.5 Generalized and Nonlinear Eigenvalue Problems

Many eigenpackages also deal with the so-called generalized eigenproblem [7],

$$
\mathbf { A } \cdot \mathbf { x } = \lambda \mathbf { B } \cdot \mathbf { x }
$$

where A and $\mathbf { B }$ are both matrices. Most such problems, where $\mathbf { B }$ is nonsingular, can be handled by the equivalent

$$
( \mathbf { B } ^ { - 1 } \cdot \mathbf { A } ) \cdot \mathbf { x } = \lambda \mathbf { x }
$$

Often A and $\mathbf { B }$ are symmetric and $\mathbf { B }$ is positive-definite. The matrix $\mathbf { B } ^ { - 1 } \cdot \mathbf { A }$ in (11.0.20) is not symmetric, but we can recover a symmetric eigenvalue problem by using the Cholesky decomposition $\mathbf { B } = \mathbf { L } \cdot \mathbf { L } ^ { T }$ of $\ S 2 . 9$ . Multiplying equation (11.0.19) by ${ \bf L } ^ { - 1 }$ , we get

$$
\mathbf { C } \cdot ( \mathbf { L } ^ { T } \cdot \mathbf { x } ) = \lambda ( \mathbf { L } ^ { T } \cdot \mathbf { x } )
$$

where

$$
\mathbf { C } = \mathbf { L } ^ { - 1 } \cdot \mathbf { A } \cdot ( \mathbf { L } ^ { - 1 } ) ^ { T }
$$

The matrix $\mathbf { C }$ is symmetric and its eigenvalues are the same as those of the original problem (11.0.19); its eigenfunctions are $\mathbf { L } ^ { T } \cdot \mathbf { x }$ . The efficient way to form C is first to solve the equation

$$
\mathbf { Y } \cdot \mathbf { L } ^ { T } = \mathbf { A }
$$

for the lower triangle of the matrix $\mathbf { Y }$ . Then solve

$$
\mathbf { L } \cdot \mathbf { C } = \mathbf { Y }
$$

for the lower triangle of the symmetric matrix C.

Another generalization of the standard eigenvalue problem is to problems nonlinear in the eigenvalue $\lambda$ , for example,

$$
( \mathbf { A } \lambda ^ { 2 } + \mathbf { B } \lambda + \mathbf { C } ) \cdot \mathbf { x } = 0
$$

This can be turned into a linear problem by introducing an additional unknown eigenvector y and solving the $2 N \times 2 N$ eigensystem

$$
\left( \underset { - \mathbf { A } ^ { - 1 } \cdot \mathbf { C } } { 0 } \quad \mathbf { \Phi } _ { - \mathbf { A } ^ { - 1 } \cdot \mathbf { B } } ^ { \mathbf { 1 } } \right) \cdot \binom { \mathbf { x } } { \mathbf { y } } = \lambda \binom { \mathbf { x } } { \mathbf { y } }
$$

This technique generalizes to higher-order polynomials in $\lambda$ . A polynomial of degree $M$ produces a linear $M N \times M N$ eigensystem (see [8]).

# 11.0.6 Relation to Singular Value Decomposition

The factorization of a matrix A by the use of its eigenvectors and eigenvalues, equation (11.0.10), seems similar to singular value decomposition (SVD), as was discussed in $\ S 2 . 6$ . Is it the same thing? In general, no. A first obvious difference is that SVD is not restricted to square matrices, while eigendecomposition is. But what if A is square? Are the two decompositions then identical?

In general, still no. The difference has to do with what is orthogonal to what. If for a square matrix A we write the two decompositions (cf. equation 2.6.1 or 2.6.4 and equation 11.0.10),

$$
\mathbf { A } = \mathbf { U } \cdot \mathrm { d i a g } ( w _ { 0 } \ldots { w _ { N - 1 } } ) \cdot \mathbf { V } ^ { T } = \mathbf { X } _ { R } \cdot \mathrm { d i a g } ( \lambda _ { 0 } \ldots { \lambda _ { N - 1 } } ) \cdot \mathbf { X } _ { L }
$$

then for SVD the columns of $\mathbf { U }$ are mutually orthonormal, as are the columns of $\mathbf { V }$ . There is no particular orthonormality between $\mathbf { U }$ and $\mathbf { V }$ . For the eigendecomposition, the situation is the reverse: The rows of $\mathbf { X } _ { L }$ are orthogonal to the columns of $\mathbf { X } _ { R }$ (except for those corresponding to the same eigenvalue), but there is no particular orthogonality among the rows or columns of $\mathbf { X } _ { L }$ or the rows or columns of $\mathbf { X } _ { R }$ . The two decompositions in equation (11.0.27) are just, in general, different!

However, the difference disappears when A is symmetric (or, if complex, Hermitian). In that case, equation (11.0.27) becomes

$$
\mathbf { A } = \mathbf { V } \cdot \mathrm { d i a g } ( w _ { 0 } \ldots { w _ { N - 1 } } ) \cdot \mathbf { V } ^ { T } = \mathbf { X } _ { R } \cdot \mathrm { d i a g } ( \lambda _ { 0 } \ldots { \lambda _ { N - 1 } } ) \cdot \mathbf { X } _ { R } ^ { T }
$$

and the fact that each decomposition is unique implies

$$
\mathbf { V } = \mathbf { U } = \mathbf { X } _ { R } = \mathbf { X } _ { L } ^ { T }
$$

and

$$
\lambda _ { i } = w _ { i } , \qquad i = 0 , \dots , N - 1
$$

That is, the (left and right) eigenvectors are the columns of any of the matrices listed in equation (11.0.29), and the corresponding eigenvalues and singular values are identical.

From a general matrix A, not necessarily even square, one can form the two symmetric matrices $\mathbf { A } ^ { T } \cdot \mathbf { A }$ and $\mathbf { A } \cdot \mathbf { A } ^ { T }$ . You can work out from equation (11.0.27) that the eigenvalues of either of these two matrices are squares of singular values of A. However, this doesn’t tell you about the eigenvalues of A: The matrix whose eigenvalues are the squares of the eigenvalues of A is the unrelated matrix $\mathbf { A } \cdot \mathbf { A }$ , not $\mathbf { A } ^ { \top } \cdot \mathbf { A }$ or $\mathbf { A } \cdot \mathbf { A } ^ { T }$ .

# CITED REFERENCES AND FURTHER READING:

Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), Chapter 6.[1]   
Wilkinson, J.H., and Reinsch, C. 1971, Linear Algebra, vol. II of Handbook for Automatic Computation (New York: Springer).[2]   
Smith, B.T., et al. 1976, Matrix Eigensystem Routines — EISPACK Guide, 2nd ed., vol. 6 of Lecture Notes in Computer Science (New York: Springer).[3]   
Anderson, E., et al. 1999, LAPACK User’s Guide, 3rd ed. (Philadelphia: S.I.A.M.). Online with software at $^ { 2 0 0 7 + }$ , http://www.netlib.org/lapack.[4]   
IMSL Math/Library Users Manual (Houston: IMSL Inc.)， see $^ { 2 0 0 7 + }$ ,http://www.vni.com/ products/imsl.[5]   
NAG Fortran Library(Oxford, UK: Numerical Algorithms Group),see $^ { 2 0 0 7 + }$ ,http://www.nag. co.uk, Chapter F02.[6]   
Golub, G.H., and Van Loan, C.F. 1996, Matrix Computations, 3rd ed. (Baltimore: Johns Hopkins University Press), $\ S 7 . 7 . [ 7 ]$   
Wilkinson, J.H. 1965, The Algebraic Eigenvalue Problem (New York: Oxford University Press).[8]   
Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), Chapter 13.   
Horn, R.A., and Johnson, C.R. 1985, Matrix Analysis (Cambridge: Cambridge University Press).

# 11.1 Jacobi Transformations of a Symmetric Matrix

The Jacobi method consists of a sequence of orthogonal similarity transformations of the form of equation (11.0.15). Each transformation (a Jacobi rotation) is just a plane rotation designed to annihilate one of the off-diagonal matrix elements. Successive transformations undo previously set zeros, but the off-diagonal elements nevertheless get smaller and smaller, until the matrix is diagonal to machine precision. Accumulating the product of the transformations as you go gives the matrix of eigenvectors, equation (11.0.16), while the elements of the final diagonal matrix are the eigenvalues.

The Jacobi method is absolutely foolproof for all real symmetric matrices. In particular, it returns the small eigenvalues with better relative accuracy than methods that first reduce the matrix to tridiagonal form. For matrices of order greater than about 10, however, the algorithm is slower, by a significant constant factor, than the $\boldsymbol { \mathcal { Q } R }$ method we shall give in $\ S 1 1 . 4$ . However, the Jacobi algorithm is much simpler than the more efficient methods. We thus recommend it for matrices of moderate order, where expense is not a major consideration.

The basic Jacobi rotation $\mathbf { P } _ { p q }$ is a matrix of the form

$$
\mathbf { P } _ { p q } = \left[ \begin{array} { c c c c c c } { 1 } & & & & & & \\ & { \cdots } & & & & \\ & & { c } & { \cdots } & { s } & \\ & & { \vdots } & { 1 } & { \vdots } & \\ & & { - s } & { \cdots } & { c } & \\ & & & & & { \cdots } & \\ & & & & & & { 1 } \end{array} \right]
$$

Here all the diagonal elements are unity except for the two elements $c$ in rows (and columns) $p$ and $q$ . All off-diagonal elements are zero except the two elements $s$ and $- s$ . The numbers $c$ and $s$ are the cosine and sine of a rotation angle $\phi$ , so $c ^ { 2 } + s ^ { 2 } = 1$ . A plane rotation such as (11.1.1) is used to transform the matrix A according to

$$
\mathbf { A } ^ { \prime } = \mathbf { P } _ { p q } ^ { T } \cdot \mathbf { A } \cdot \mathbf { P } _ { p q }
$$

Now, $\mathbf { P } _ { p q } ^ { T } \cdot \mathbf { A }$ changes only rows $p$ and $q$ of $\mathbf { A }$ , while $\mathbf { A } \cdot \mathbf { P } _ { p q }$ changes only columns $p$ and $q$ . Notice that the subscripts $p$ and $q$ do not denote components of $\mathbf { P } _ { p q }$ , but rather label which kind of rotation the matrix is, i.e., which rows and columns it affects. Thus the changed elements of $\mathbf { A }$ in (11.1.2) are only in rows $p$ and $q$ , and columns $p$ and $q$ , as indicated below:

$$
\mathbf { A } ^ { \prime } = \left[ \begin{array} { c c c c c c c } & { a _ { 0 p } ^ { \prime } } & & & { a _ { 0 q } ^ { \prime } } & & \\ & & { \vdots } & & & { \vdots } & \\ { a _ { p 0 } ^ { \prime } } & { \cdots } & { a _ { p p } ^ { \prime } } & { \cdots } & { a _ { p q } ^ { \prime } } & { \cdots } & { a _ { p , n - 1 } ^ { \prime } } \\ & & & { \vdots } & & & { \vdots } & \\ { a _ { q 0 } ^ { \prime } } & { \cdots } & { a _ { q p } ^ { \prime } } & { \cdots } & { a _ { q q } ^ { \prime } } & { \cdots } & { a _ { q , n - 1 } ^ { \prime } } \\ & & { \vdots } & & & { \vdots } \\ & & { a _ { n - 1 , p } ^ { \prime } } & { a _ { n - 1 , q } ^ { \prime } } & & \end{array} \right]
$$

Multiplying out equation (11.1.2) and using the symmetry of $\mathbf { A }$ , we get the explicit formulas

$$
\begin{array} { l } { { a _ { r p } ^ { \prime } = c a _ { r p } - s a _ { r q } \nonumber } } \\ { { a _ { r q } ^ { \prime } = c a _ { r q } + s a _ { r p } \nonumber } } \\ { { a _ { p p } ^ { \prime } = c ^ { 2 } a _ { p p } + s ^ { 2 } a _ { q q } - 2 s c a _ { p q } \nonumber } } \\ { { a _ { q q } ^ { \prime } = s ^ { 2 } a _ { p p } + c ^ { 2 } a _ { q q } + 2 s c a _ { p q } \nonumber } } \\ { { a _ { p q } ^ { \prime } = ( c ^ { 2 } - s ^ { 2 } ) a _ { p q } + s c ( a _ { p p } - a _ { q q } ) \nonumber } } \end{array}
$$

The idea of the Jacobi method is to try to zero the off-diagonal elements by a series of plane rotations. Accordingly, to set $a _ { p q } ^ { \prime } = 0$ , equation (11.1.7) gives the following expression for the rotation angle $\phi$ :

$$
\theta \equiv \cot 2 \phi \equiv \frac { c ^ { 2 } - s ^ { 2 } } { 2 s c } = \frac { a _ { q q } - a _ { p p } } { 2 a _ { p q } }
$$

If we let $t \equiv s / c$ , the definition of $\theta$ can be rewritten

$$
t ^ { 2 } + 2 t \theta - 1 = 0
$$

The smaller root of this equation corresponds to a rotation angle less than $\pi / 4$ in magnitude; this choice at each stage gives the most stable reduction. Using the form of the quadratic formula with the discriminant in the denominator, we can write this smaller root as

$$
t = { \frac { \operatorname { s g n } ( \theta ) } { | \theta | + { \sqrt { \theta ^ { 2 } + 1 } } } }
$$

If $\theta$ is so large that $\theta ^ { 2 }$ would overflow on the computer, we set $t = 1 / ( 2 \theta )$ . It now follows that

$$
\begin{array} { l } { c = \displaystyle \frac { 1 } { \sqrt { t ^ { 2 } + 1 } } } \\ { s = t c } \end{array}
$$

When we actually use equations (11.1.4) – (11.1.7) numerically, we rewrite them to minimize roundoff error. Equation (11.1.7) is replaced by

$$
a _ { p q } ^ { \prime } = 0
$$

The idea in the remaining equations is to set the new quantity equal to the old quantity plus a small correction. Thus we can use (11.1.7) and (11.1.13) to eliminate $a _ { q q }$ from (11.1.5), giving

$$
a _ { p p } ^ { \prime } = a _ { p p } - t a _ { p q }
$$

Similarly,

$$
\begin{array} { l } { { a _ { q q } ^ { \prime } = a _ { q q } + t a _ { p q } } } \\ { { \ } } \\ { { a _ { r p } ^ { \prime } = a _ { r p } - s ( a _ { r q } + \tau a _ { r p } ) } } \\ { { a _ { r q } ^ { \prime } = a _ { r q } + s ( a _ { r p } - \tau a _ { r q } ) } } \end{array}
$$

where $\tau$ $\tau ~ ( = \tan \phi / 2$ / is defined by

$$
\tau \equiv \frac { s } { 1 + c }
$$

One can see the convergence of the Jacobi method by considering the sum of the squares of the off-diagonal elements

$$
S = \sum _ { r \neq s } | a _ { r s } | ^ { 2 }
$$

Equations (11.1.4) – (11.1.7) imply that

$$
S ^ { \prime } = S - 2 | a _ { p q } | ^ { 2 }
$$

(Since the transformation is orthogonal, the sum of the squares of the diagonal elements increases correspondingly by $2 | a _ { p q } | ^ { 2 }$ .) The sequence of $S$ ’s thus decreases monotonically. Since the sequence is bounded below by zero, and since we can choose $a _ { p q }$ to be whatever element we want, the sequence can be made to converge to zero.

Eventually one obtains a matrix $\mathbf { D }$ that is diagonal to machine precision. The diagonal elements give the eigenvalues of the original matrix A, since

$$
\mathbf { D } = \mathbf { V } ^ { T } \cdot \mathbf { A } \cdot \mathbf { V }
$$

where

$$
\mathbf { V } = \mathbf { P } _ { 1 } \cdot \mathbf { P } _ { 2 } \cdot \mathbf { P } _ { 3 } \cdot \cdot \cdot
$$

the $\mathbf { P } _ { i }$ ’s being the successive Jacobi rotation matrices. The columns of $\mathbf { V }$ are the eigenvectors (since $\mathbf { A } \cdot \mathbf { V } = \mathbf { V } \cdot \mathbf { D }$ ). They can be computed by applying

$$
\mathbf { V } ^ { \prime } = \mathbf { V } \cdot \mathbf { P } _ { i }
$$

at each stage of calculation, where initially $\mathbf { V }$ is the identity matrix. In detail, equation (11.1.23) is

$$
\begin{array} { l } { { v _ { r s } ^ { \prime } = v _ { r s } \qquad ( s \ne p , s \ne q ) } } \\ { { v _ { r p } ^ { \prime } = c v _ { r p } - s v _ { r q } } } \\ { { v _ { r q } ^ { \prime } = s v _ { r p } + c v _ { r q } } } \end{array}
$$

We rewrite these equations in terms of $\tau$ as in equations (11.1.16) and (11.1.17) to minimize roundoff.

The only remaining question is the strategy one should adopt for the order in which the elements are to be annihilated. Jacobi’s original algorithm of 1846 searched the whole upper triangle at each stage and set the largest off-diagonal element to zero. This is a reasonable strategy for hand calculation, but it is prohibitive on a computer since the search alone makes each Jacobi rotation a process of order $N ^ { 2 }$ instead of $N$ .

A better strategy for our purposes is the cyclic Jacobi method, where one annihilates elements in strict order. For example, one can simply proceed down the rows: $\mathbf { P } _ { 0 1 } , \mathbf { P } _ { 0 2 } , . . . , \mathbf { P } _ { 0 , n - 1 }$ ; then $\mathbf { P } _ { 1 2 } , \mathbf { P } _ { 1 3 }$ , etc. One can show that convergence is generally quadratic for either the original or the cyclic Jacobi method, for nondegenerate eigenvalues. One such set of $n ( n - 1 ) / 2$ Jacobi rotations is called a sweep.

The program below, based on the implementations in [1,2], uses two further refinements:

- In the first three sweeps, we carry out the $p q$ rotation only if $| a _ { p q } | > \epsilon$ for some threshold value

$$
\epsilon = \frac { 1 } { 5 } \frac { S _ { 0 } } { n ^ { 2 } }
$$

where $S _ { 0 }$ is the sum of the off-diagonal moduli,

$$
S _ { 0 } = \sum _ { r < s } | a _ { r s } |
$$

- After four sweeps, if $| a _ { p q } | \ll | a _ { p p } |$ and $| a _ { p q } | \ll | a _ { q q } |$ , we set $| a _ { p q } | =$ 0 and skip the rotation. The criterion used in the comparison is $| a _ { p q } | <$ $1 0 ^ { - ( D + 2 ) } \big | a _ { p p } \big |$ , where $D$ is the number of significant decimal digits on the machine, and similarly for $| a _ { q q } |$ .

Typical matrices require six to ten sweeps to achieve convergence, or $3 n ^ { 2 }$ to $5 n ^ { 2 }$ Jacobi rotations. Each rotation requires of order $8 n$ floating-point operations, so the total labor is of order $2 4 n ^ { 3 }$ to $4 0 n ^ { 3 }$ operations. Calculation of the eigenvectors as well as the eigenvalues changes the operation count from $8 n$ to $1 2 n$ per rotation, which is only a $50 \%$ overhead.

The following routine implements the Jacobi method. Simply create a Jacobi object using your symmetric matrix $\mathsf { a } \left[ 0 \ldots \mathsf { n - 1 } \right] \left[ 0 \ldots \mathsf { n - 1 } \right]$ :

# Jacobi jac(a);

The vector ${ \mathsf { d } } \left[ 0 \ldots \cdot \mathbf { n } ^ { - 1 } \right]$ then contains the eigenvalues of a. During the computation, it contains the current diagonal of a. The matrix $\mathtt { v } [ 0 \AA . . \mathrm { n } ^ { - 1 } ] \ [ 0 \AA . . \mathrm { n } ^ { - 1 } ]$ outputs the normalized eigenvector belonging to $\mathtt { d } [ \mathtt { k } ]$ in column k. The parameter nrot is the number of Jacobi rotations that were needed to achieve convergence.

# struct Jacobi {

Computes all eigenvalues and eigenvectors of a real symmetric matrix by Jacobi’s method.

const Int n;   
MatDoub a,v;   
VecDoub d;   
Int nrot;   
const Doub EPS;

Jacobi(MatDoub_I &aa) : n(aa.nrows()), a(aa), v(n,n), d(n), nrot(0), EPS(numeric_limits<Doub>::epsilon())

Computes all eigenvalues and eigenvectors of a real symmetric matrix a[0..n-1][0..n-1]. On output, d[0..n-1] contains the eigenvalues of a sorted into descending order, while v[0..n-1][0..n-1] is a matrix whose columns contain the corresponding normalized eigenvectors. nrot contains the number of Jacobi rotations that were required. Only the upper triangle of a is accessed.

Initialize to the identity matrix.

Int i,j,ip,iq;   
Doub tresh,theta,tau,t,sm,s,h,g,c;   
VecDoub b(n),z(n);   
for (ip=0;ip<n;ip++) { for (iq=0;iq<n;iq++) v[ip][iq]=0.0; v[ip][ip] $= 1$ .0;   
}   
for (ip=0;ip<n;ip++) { b[ip]=d[ip] $= \mathtt { a }$ [ip][ip]; z[ip]=0.0;   
}   
for (i=1;i<=50;i++) { sm=0.0; for (ip=0;ip<n-1;ip++) { for (iq=ip+1;iq<n;iq++) sm $+ =$ abs(a[ip][iq]); } if $\mathrm { { \bf \Psi } } _ { , \bf { s m } } = = \mathrm { { \bf \Psi } } 0 . 0 \mathrm { { \bf \Psi } } ,$ ) { eigsrt(d,&v); return; } if ( $ { \mathrm { ~  ~ \cdot ~ } } _ { 1 } < 4 )$ tresh ${ = } 0$ .2\*sm/(n\*n);   
Initialize b and d to the diagonal of a.   
This vector will accumulate terms of the form $t a _ { p q }$ as in equation (11.1.14).

Sum magnitude of off-diagonal elements.

The normal return, which relies on quadratic convergence to machine underflow.

On the first three sweeps...

else tresh $_ { = 0 }$ .0; ...thereafter. for (ip=0;ip<n-1;ip++) { for (iq=ip+1;iq<n;iq++) { $\mathtt { g } = 1 0 0$ .0\*abs(a[ip][iq]); After four sweeps, skip the rotation if the off-diagonal element is small. if ( $\dot { \mathrm { ~ \scriptsize ~ \frac ~ { ~ 1 ~ } ~ } } > \mathrm { ~ \scriptsize ~ 4 ~ }$ && g $< =$ EPS\*abs(d[ip]) && $\ g \ < =$ EPS\*abs(d[iq])) a[ip][iq] ${ = } 0$ .0; else if (abs(a[ip][iq]) $>$ tresh) { h=d[iq]-d[ip]; if $( \ g \ < =$ EPS\*abs(h)) $\mathtt { t } =$ (a[ip][iq])/h; $t = 1 / ( 2 \theta )$ else { theta $= 0$ .5\*h/(a[ip][iq]); Equation (11.1.10). $\mathtt { t } = 1$ .0/(abs(theta)+sqrt(1. $0 +$ theta\*theta)); if (theta $< 0 . 0$ ) $t ~ = ~ - t$ ; $\mathtt { c } = 1$ .0/sqrt(1+t\*t); s=t\*c; tau=s/(1.0+c); h=t\*a[ip][iq]; z[ip] $\mathbf { \Sigma } - \mathbf { \Sigma } \mathbf { h }$ ; z[iq] $+ = \ \mathbf { h } ;$ ; d[ip] $- = \textrm { h }$ ; d[iq] $+ = \mathbf { \nabla } \ln$ ; a[ip][iq] ${ = } 0$ .0; for ( $\scriptstyle \mathbf { j } = 0$ ;j<ip;j $^ { + + }$ ) Case of rotations $0 \le j < p$ . rot(a,s,tau,j,ip,j,iq); for $( \mathrm { j } = \mathrm { i } \tt p + 1$ ;j<iq;j++) Case of rotations $p < j < q$ . rot(a,s,tau,ip,j,j,iq); for (j $=$ iq+1;j<n;j++) Case of rotations $q < j < n$ . rot(a,s,tau,ip,j,iq,j); for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<n;j++) rot(v,s,tau,j,ip,j,iq); ++nrot; } } for (ip=0;ip<n;ip++) { b[ip] $+ = \ z$ [ip]; d[ip] $\mathtt { \Gamma } = \mathtt { b }$ [ip]; Update d with the sum of tapq, z[ip]=0.0; and reinitialize $_ { z }$ . } } throw("Too many iterations in routine jacobi"); } inline void rot(MatDoub_IO &a, const Doub s, const Doub tau, const Int i, const Int j, const Int k, const Int l) { Doub $g = a$ [i][j]; Doub $h = a$ [k][l]; a[i][j]=g-s\*(h+g\*tau); a[k][l]=h+s\*(g-h\*tau); }

Note that the above routine assumes that underflows are set to zero. On machines where this is not true, the program must be modified. See $\ S 1 . 5 . 4$ and/or find out about the fesetenv (Linux) or __controlfp (Microsoft) functions.

The Jacobi method does not order the eigenvalues itself. We incorporate the following routine to sort the eigenvalues into descending order. The same routine is used in Symmeig in the next section. (The method, straight insertion, is $N ^ { 2 }$ rather than $N \log N$ ; but since you have just done an $N ^ { 3 }$ procedure to get the eigenvalues, you can afford yourself this little indulgence.)

# void eigsrt(VecDoub_IO &d, MatDoub_IO $\ast \ v =$ NULL)

Given the eigenvalues ${ \mathsf { d } } \left[ 0 \ldots \mathbf { n - 1 } \right]$ and (optionally) the eigenvectors $\mathtt { v } [ 0 \AA . . \mathtt { n } . \mathtt { n } \mathtt { - 1 } ] \tau 0 \AA . \mathtt { \mathtt { . n } - 1 } ]$ as determined by Jacobi $( \ S 1 1 . 1 )$ or tqli (-11.4), this routine sorts the eigenvalues into descending order and rearranges the columns of v correspondingly. The method is straight insertion. {

Int k; Int n=d.size(); for (Int $\scriptstyle { \dot { 1 } } = 0$ ;i<n-1;i++) { Doub p=d[k=i]; for (Int $\scriptstyle { \dot { \mathsf { J } } } = { \dot { \mathsf { I } } }$ ;j<n;j++) if (d[j] $> =$ p) $\scriptstyle { \mathtt { p } } = { \mathtt { d } }$ [k=j]; if (k $\vdots = \dot { \textbf { \ i } }$ ) { d[k] $=$ d[i]; d[i]=p; if (v != NULL) for (Int j=0;j<n;j++) { $\mathtt { p } = ( \ast \mathtt { v } )$ [j][i]; ( $^ { * } \mathtt { V } )$ [j][i] $=$ (\*v)[j][k]; $( * \tau )$ [j][k] ${ = } _ { \mathrm { p } }$ ; } } } }

# CITED REFERENCES AND FURTHER READING:

Golub, G.H., and Van Loan, C.F. 1996, Matrix Computations, 3rd ed. (Baltimore: Johns Hopkins University Press), $\ S 8 . 4$ .

Smith, B.T., et al. 1976, Matrix Eigensystem Routines — EISPACK Guide, 2nd ed., vol. 6 of Lecture Notes in Computer Science (New York: Springer).[1]

Wilkinson, J.H., and Reinsch, C. 1971, Linear Algebra, vol. II of Handbook for Automatic Computation (New York: Springer).[2]

# 11.2 Real Symmetric Matrices

As already mentioned, the optimum strategy in most cases for finding eigenvalues and eigenvectors is, first, to reduce the matrix to a simple form, only then beginning an iterative procedure. For symmetric matrices, the preferred simple form is tridiagonal.

Here is a routine based on this strategy that finds all eigenvalues and eigenvectors of a real symmetric matrix. It is typically a factor of about five faster than the Jacobi routine of the previous section. The implementations of the functions tred2 and tqli that reduce the matrix to tridiagonal form and then find the eigensystem are discussed in the next two sections.

There are two user interfaces, implemented as two constructors. The first constructor is the usual one:

Symmeig s(a);

It returns the eigenvalues of a in descending order in s.d $\left[ 0 \cdot \cdot \mathbf { n } ^ { - 1 } \right]$ . The normalized eigenvector corresponding to $\mathtt { d } [ \mathtt { k } ]$ is in the matrix column $\mathbf { s } \lrcorner z [ 0  \lVert \mathbf { \lVert } \cdot \mathbf { n } \mathbf { - } 1 ] [ \mathbf { k } ]$ . Setting the default argument to false suppresses the computation of the eigenvectors:

Symmeig s(a,false);

If you already have a matrix in tridiagonal form, you use the other constructor, which accepts the diagonal and subdiagonal of the matrix as vectors:

# Symmeig s(d,e);

Again, you can suppress the computation of eigenvectors by setting the default argument to false.

Here is the routine:

# struct Symmeig {

Computes all eigenvalues and eigenvectors of a real symmetric matrix by reduction to tridiagonal form followed by QL iteration.

Int n;   
MatDoub z;   
VecDoub d,e;   
Bool yesvecs;

Symmeig(MatDoub_I &a, Bool yesvec=true) : n(a.nrows()), z(a), d(n), e(n), yesvecs(yesvec)

Computes all eigenvalues and eigenvectors of a real symmetric matrix a[0..n-1][0..n-1] by reduction to tridiagonal form followed by QL iteration. On output, d[0..n-1] contains the eigenvalues of a sorted into descending order, while $\mathbf { z } \left[ 0 \cdot \mathbf { { \sigma } } \cdot \mathbf { { n } } \mathbf { - 1 } \right] \left[ 0 \cdot \mathbf { { \sigma } } \cdot \mathbf { { n } } \mathbf { - 1 } \right]$ is a matrix whose columns contain the corresponding normalized eigenvectors. If yesvecs is input as true (the default), then the eigenvectors are computed. If yesvecs is input as false, only the eigenvalues are computed.

tred2(); Reduction to tridiagonal form; see $\ S 1 1 . 3$ . tqli(); Eigensystem of tridiagonal matrix; see $\ S 1 1 . 4$ . sort();   
}   
Symmeig(VecDoub_I &dd, VecDoub_I &ee, Bool yesvec=true) n(dd.size()), d(dd), e(ee), ${ \bf z } ( { \bf n } , { \bf n } , 0 . 0 )$ , yesvecs(yesvec)

Computes all eigenvalues and (optionally) eigenvectors of a real, symmetric, tridiagonal matrix by QL iteration. On input, dd[0..n-1] contains the diagonal elements of the tridiagonal matrix. The vector ee[0..n-1] inputs the subdiagonal elements of the tridiagonal matrix, with ee[0] arbitrary. Output is the same as the constructor above.

{ for (Int i=0;i<n;i++) z[i][i] $= 1$ .0; tqli(); sort();   
void sort() { if (yesvecs) eigsrt(d,&z); else eigsrt(d);   
}   
void tred2();   
void tqli();   
Doub pythag(const Doub a, const Doub b);

# 11.3 Reduction of a Symmetric Matrix to Tridiagonal Form: Givens and Householder Reductions

The previous section outlined the grand strategy of (i) reduction to tridiagonal form, followed by (ii) finding the eigenvalues and eigenvectors of a tridiagonal matrix. In this section we implement the first of these steps.

# 11.3.1 Givens Method

The Givens reduction is a modification of the Jacobi method. Instead of trying to reduce the matrix all the way to diagonal form, we are content to stop when the matrix is tridiagonal. This allows the procedure to be carried out in a finite number of steps, unlike the Jacobi method, which requires iteration to convergence.

For the Givens method, we choose the rotation angle in equation (11.1.1) so as to zero an element that is not at one of the four “corners,” i.e., not $a _ { p p } , a _ { p q }$ , or $a _ { q q }$ in equation (11.1.3). Specifically, we first choose ${ \bf P } _ { 1 2 }$ to annihilate $a _ { 2 0 }$ (and, by symmetry, $a _ { 0 2 }$ ). Then we choose ${ \bf P } _ { 1 3 }$ to annihilate $a _ { 3 0 }$ . In general, we choose the sequence

$$
\mathbf { P } _ { 1 2 } , \mathbf { P } _ { 1 3 } , \ldots , \mathbf { P } _ { 1 , n - 1 } ; \mathbf { P } _ { 2 3 } , \ldots , \mathbf { P } _ { 2 , n - 1 } ; \ldots ; \mathbf { P } _ { n - 2 , n - 1 }
$$

where $\mathbf { P } _ { j k }$ annihilates $^ { a _ { k , j - 1 } }$ . The method works because elements such as $a _ { r p } ^ { \prime }$ and $a _ { r q } ^ { \prime }$ , with $r \neq p r \neq q$ , are linear combinations of the old quantities $a _ { r p }$ and $a _ { r q }$ , by equation (11.1.4). Thus, if $a _ { r p }$ and $a _ { r q }$ have already been set to zero, they remain zero as the reduction proceeds. Evidently, of order $n ^ { 2 } / 2$ rotations are required, and the number of multiplications in a straightforward implementation is of order $4 n ^ { 3 } / 3$ , not counting those for keeping track of the product of the transformation matrices, required for the eigenvectors.

The Householder method, to be discussed next, is just as stable as the Givens reduction and it is a factor of two more efficient, so the Givens method is not generally used. However, the Givens reduction can be reformulated to reduce the number of operations by a factor of two, and also avoid the necessity of taking square roots [1]. This appears to make the algorithm competitive with the Householder reduction. Unfortunately, this “fast Givens” reduction has to be monitored to avoid overflows, and the variables have to be periodically rescaled. There does not seem to be any compelling reason to prefer the Givens reduction over the Householder method.

# 11.3.2 Householder Method

The Householder algorithm reduces an $n \times n$ symmetric matrix A to tridiagonal form by $n - 2$ orthogonal transformations. Each transformation annihilates the required part of a whole column and whole corresponding row. The basic ingredient is a Householder matrix $\mathbf { P }$ , which has the form

$$
\mathbf { P } = \mathbf { 1 } - 2 \mathbf { w } \cdot \mathbf { w } ^ { T }
$$

where w is a real vector with $| \mathbf { w } | ^ { 2 } = 1$ . (In the present notation, the outer or matrix product of two vectors, a and $\mathbf { b }$ , is written a $\cdot \mathbf { b } ^ { T }$ , while the inner or scalar product

of the vectors is written as $\mathbf { a } ^ { T } \cdot \mathbf { b } .$ ) The matrix $\mathbf { P }$ is orthogonal, because

$$
\begin{array} { r l } & { \mathbf { P } ^ { 2 } = ( \mathbf { 1 } - 2 \mathbf { w } \cdot \mathbf { w } ^ { T } ) \cdot ( \mathbf { 1 } - 2 \mathbf { w } \cdot \mathbf { w } ^ { T } ) } \\ & { \quad \quad = \mathbf { 1 } - 4 \mathbf { w } \cdot \mathbf { w } ^ { T } + 4 \mathbf { w } \cdot ( \mathbf { w } ^ { T } \cdot \mathbf { w } ) \cdot \mathbf { w } ^ { T } } \\ & { \quad = \mathbf { 1 } } \end{array}
$$

Therefore $\mathbf { P } = \mathbf { P } ^ { - 1 }$ . But $\mathbf { P } ^ { T } = \mathbf { P }$ , and so $\mathbf { P } ^ { T } = \mathbf { P } ^ { - 1 }$ , proving orthogonality.

Rewrite $\mathbf { P }$ as

where the scalar $H$ is

$$
\mathbf { P } = \mathbf { 1 } - { \frac { \mathbf { u } \cdot \mathbf { u } ^ { T } } { H } }
$$

$$
\begin{array} { r } { H \equiv \frac { 1 } { 2 } \left| { \bf u } \right| ^ { 2 } } \end{array}
$$

and u can now be any vector. Suppose $\mathbf { X }$ is the vector composed of the first column of A. Choose

$$
\mathbf { u } = \mathbf { x } \mp | \mathbf { x } | \mathbf { e } _ { 0 }
$$

where ${ \bf e } _ { 0 }$ is the unit vector $[ 1 , 0 , \ldots , 0 ] ^ { T }$ and the choice of signs will be made later. Then

$$
{ \begin{array} { r l } & { \mathbf { P } \cdot \mathbf { x } = \mathbf { x } - { \frac { \mathbf { u } } { H } } \cdot ( \mathbf { x } \mp | \mathbf { x } | \mathbf { e } _ { 0 } ) ^ { T } \cdot \mathbf { x } } \\ & { \qquad = \mathbf { x } - { \frac { 2 \mathbf { u } \cdot ( | \mathbf { x } | ^ { 2 } \mp | \mathbf { x } | x _ { 0 } ) } { 2 | \mathbf { x } | ^ { 2 } \mp 2 | \mathbf { x } | x _ { 0 } } } } \\ & { \qquad = \mathbf { x } - \mathbf { u } } \\ & { \qquad = \pm | \mathbf { x } | \mathbf { e } _ { 0 } } \end{array} }
$$

This shows that the Householder matrix $\mathbf { P }$ acts on a given vector $\mathbf { X }$ to zero all its elements except the first one.

To reduce a symmetric matrix A to tridiagonal form, we choose the vector $\mathbf { X }$ for the first Householder matrix to be the lower $n - 1$ elements of column 0. Then the lower $n - 2$ elements will be zeroed:

Here we have written the matrices in partitioned form, with $\left( n - 1 \right) \mathbf { p }$ denoting a Householder matrix with dimensions $( n - 1 ) \times ( n - 1 )$ . The quantity $k$ is simply plus or minus the magnitude of the vector $[ a _ { 1 0 } , \dotsc , a _ { n - 1 , 0 } ] ^ { T }$ .

The complete orthogonal transformation is now

$$
\mathbf { A } ^ { \prime } = \mathbf { P } \cdot \mathbf { A } \cdot \mathbf { P } = { \left[ \begin{array} { l } { \displaystyle { \frac { a _ { 0 0 } } { k } } \left| \begin{array} { c c c } { \displaystyle { 0 } } & { \cdots } & { 0 } \\ { \displaystyle k } \\ { \displaystyle { 0 } } \\ { \vdots } \\ { \displaystyle { 0 } } \end{array} \right| } \right]} \end{array}  
$$

We have used the fact that $\mathbf { P } ^ { T } = \mathbf { P }$ .

Now choose the vector $\mathbf { X }$ for the second Householder matrix to be the bottom $n - 2$ elements of column 1, and from it construct

$$
\mathbf { P } _ { 2 } \equiv \left[ \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 1 } \\ { 0 } & { 0 } \\ { \vdots } & { \vdots } \\ { 0 } & { 0 } \end{array} \right] \ L _ { ( n - 2 ) \mathbf { P } _ { 2 } }
$$

The identity block in the upper-left corner ensures that the tridiagonalization achieved in the first step will not be spoiled by this one, while the $( n - 2 )$ -dimensional Householder matrix ${ \bf \Pi } ^ { ( n - 2 ) } { \bf P } _ { 2 }$ creates one additional row and column of the tridiagonal output. Clearly, a sequence of $n - 2$ such transformations will reduce the matrix A to tridiagonal form.

Instead of actually carrying out the matrix multiplications in $\mathbf { P } \cdot \mathbf { A } \cdot \mathbf { P }$ , we compute a vector

$$
\mathbf { p } \equiv { \frac { \mathbf { A } \cdot \mathbf { u } } { H } }
$$

Then

$$
\begin{array} { c } { \displaystyle \mathbf { A } \cdot \mathbf { P } = \mathbf { A } \cdot ( 1 - \frac { \mathbf { u } \cdot \mathbf { u } ^ { T } } { H } ) = \mathbf { A } - \mathbf { p } \cdot \mathbf { u } ^ { T } } \\ { \mathbf { A } ^ { \prime } = \mathbf { P } \cdot \mathbf { A } \cdot \mathbf { P } = \mathbf { A } - \mathbf { p } \cdot \mathbf { u } ^ { T } - \mathbf { u } \cdot \mathbf { p } ^ { T } + 2 K \mathbf { u } \cdot \mathbf { u } ^ { T } } \end{array}
$$

where the scalar $K$ is defined by

$$
K = \frac { \mathbf { u } ^ { T } \cdot \mathbf { p } } { 2 H }
$$

If we write

$$
{ \bf q } \equiv { \bf p } - K { \bf u }
$$

then we have

$$
\mathbf { A } ^ { \prime } = \mathbf { A } - \mathbf { q } \cdot \mathbf { u } ^ { T } - \mathbf { u } \cdot \mathbf { q } ^ { T }
$$

This is the computationally useful formula.

Following [2], the routine for Householder reduction given below actually starts in the column $n - 1$ of $\mathbf { A }$ , not column 0 as in the explanation above. In detail, the equations are as follows: At stage $m$ . $( m = 1 , 2 , \ldots , n - 2 )$ , the vector $\mathbf { u }$ has the form

$$
\mathbf { u } ^ { T } = [ a _ { i 0 } , a _ { i 1 } , \dots , a _ { i , i - 2 } , a _ { i , i - 1 } \pm \sqrt { \sigma } , 0 , \dots , 0 ]
$$

Here

$$
i \equiv n - m = n - 1 , n - 2 , \ldots , 2
$$

and the quantity $\sigma$ ( $\cdot | x | ^ { 2 }$ in our earlier notation) is

$$
\sigma = ( a _ { i 0 } ) ^ { 2 } + \cdots + ( a _ { i , i - 1 } ) ^ { 2 }
$$

Choose the sign of $\sqrt { \sigma }$ in (11.3.14) to be the same as the sign of $a _ { i , i - 1 }$ to lessen roundoff error.

Variables are thus computed in the following order: $\sigma , { \bf u } , H , { \bf p } , K , { \bf q } , { \bf A } ^ { \prime }$ . At any stage $m , \mathbf { A }$ is tridiagonal in its last $m - 1$ rows and columns.

No extra storage arrays are needed for the intermediate results. At stage $m$ , the vectors $\mathbf { p }$ and $\mathbf { q }$ are nonzero only in elements $0 , \ldots , i$ (recall that $i = n - m )$ , while $\mathbf { u }$ is nonzero only in elements $0 , \ldots , i - 1$ . The elements of the vector $\ominus$ are being determined in the order $n - 1 , n - 2 , \ldots$ , so we can store $\mathbf { p }$ in the elements of $\ominus$ not already determined. The vector $\mathbf { q }$ can overwrite $\mathbf { p }$ once $\mathbf { p }$ is no longer needed. We store $\mathbf { u }$ in row $i$ of a and $\mathbf { u } / H$ in column $i$ of a. Once the reduction is complete, we compute the matrices $\mathbf { Q } _ { j }$ using the quantities $\mathbf { u }$ and $\mathbf { u } / H$ that have been stored in a. Since $\mathbf { Q } _ { j }$ is an identity matrix from row and column $n - j$ on, we only need compute its elements up to row and column $n - j - 1$ . These can overwrite the $\mathbf { u }$ ’s and $\mathbf { u } / H$ ’s in the corresponding rows and columns of a, which are no longer required for subsequent $\mathbf { Q }$ ’s.

The routine tred2, given below, includes one further refinement. If the quantity $\sigma$ is zero or “small” at any stage, one can skip the corresponding transformation. A simple criterion, such as

would be fine most of the time. A more careful criterion is actually used. At stage $i$ , define the quantity

$$
\epsilon = \sum _ { k = 0 } ^ { i - 1 } \left| a _ { i k } \right|
$$

If $\epsilon = 0$ to machine precision, we skip the transformation. Otherwise we redefine

$$
a _ { i k } \quad \mathrm { b e c o m e s } \quad a _ { i k } / \epsilon
$$

and use the scaled variables for the transformation. (A Householder transformation depends only on the ratios of the elements.)

If the eigenvectors of the final tridiagonal matrix are found (for example, by the routine in the next section), then the eigenvectors of A can be obtained by applying the accumulated transformation

$$
\mathbf { Q } = \mathbf { P } _ { 1 } \cdot \mathbf { P } _ { 2 } \cdot \cdot \cdot \mathbf { P } _ { n - 2 }
$$

to those eigenvectors. We therefore form $\mathbf { Q }$ by recursion after all the $\mathbf { P }$ ’s have been determined:

$$
\begin{array} { r l } { \mathbf { Q } _ { n - 2 } = \mathbf { P } _ { n - 2 } } & { { } } \\ { \mathbf { Q } _ { j } = \mathbf { P } _ { j } \cdot \mathbf { Q } _ { j + 1 } , } & { { } \quad j = n - 3 , \ldots , 1 } \\ { \mathbf { Q } = \mathbf { Q } _ { 1 } } & { { } } \end{array}
$$

Input for the routine below is the real symmetric matrix A stored in the matrix $\mathtt { z [ 0 . . n - 1 ] } \left[ 0 . . \mathtt { n - 1 } \right]$ . On output, z contains the elements of the orthogonal matrix Q. The vector ${ \tt d } \left[ 0 \ldots \tt N \mathrm { - } 1 \right]$ is set to the diagonal elements of the tridiagonal matrix $\mathbf { A } ^ { \prime }$ , while the vector $\mathtt { e } \left[ 0 \dots \cdot \mathrm { n } ^ { - 1 } \right]$ is set to the off-diagonal elements in its components 1 through $\mathtt { n - 1 }$ , with $\mathtt { e } \left[ 0 \right] = 0$ .

Note that when dealing with a matrix whose elements vary over many orders of magnitude, it is desirable that the matrix be permuted, insofar as possible, so that the smaller elements are in the top left-hand corner. This is because the reduction is performed starting from the bottom right-hand corner, and a mixture of small and large elements there can lead to considerable rounding errors.

In the limit of large $n$ , the operation count of the Householder reduction is $4 n ^ { 3 } / 3$ for eigenvalues only, and $8 n ^ { 3 } / 3$ for both eigenvalues and eigenvectors. The routine tred2 is designed for use with the routine tqli of the next section. tqli finds the eigenvalues and eigenvectors of a symmetric tridiagonal matrix. For many years, the combination of tred2 and tqli was the most efficient known technique for finding all the eigenvalues and eigenvectors (or just all the eigenvalues) of a real symmetric matrix. For moderate-sized matrices, it is still competitive with newer, more complicated methods.

# void Symmeig::tred2()

Householder reduction of a real symmetric matrix $\mathbf { z } \left[ 0 \cdot \mathbf { { \sigma } } \cdot \mathbf { { n } } \mathbf { - 1 } \right] \left[ 0 \cdot \mathbf { { \sigma } } \cdot \mathbf { { n } } \mathbf { - 1 } \right]$ . (The input matrix A to Symmeig is stored in $_ { z }$ .) On output, $_ { z }$ is replaced by the orthogonal matrix $\mathbf { Q }$ effecting the transformation. d[0..n-1] contains the diagonal elements of the tridiagonal matrix and e[0..n-1] the off-diagonal elements, with $\mathtt { e } [ 0 ] = 0$ . If yesvecs is false, so that only eigenvalues will subsequently be determined, several statements are omitted, in which case $_ { z }$ contains no useful information on output.

Int l,k,j,i;   
Doub scale,hh,h,g,f;   
for (i=n-1;i>0;i--) { $_ { 1 } = \dot { \tt 1 } - 1$ ; ${ \bf h } =$ scale=0.0; if $\left( 1 \ > \ 0 \right)$ ) { for $\scriptstyle \mathbf { k } = 0$ ;k<i;k++) scale $+ =$ abs(z[i][k]); if (scale $\mathrm { ~  ~ \omega ~ } = \mathrm { ~  ~ 0 ~ } . 0$ ) Skip transformation. e[i] $= _ { z }$ [i][l]; else { for $\scriptstyle 1 = 0$ ;k<i;k++) { z[i][k] /= scale; Use scaled $^ { a }$ ’s for transformation. h $+ = \ z$ [i][k]\*z[i][k]; Form $\sigma$ in h. } $\scriptstyle { \frac { 1 } { 1 } } = z$ [i][l]; g=(f >= 0.0 ? -sqrt(h) : sqrt(h)); e[i]=scale\*g; $\mathrm { ~ h ~ \ - = ~ \ f * g ~ }$ ; Now h is equation (11.3.4). z[i][l]=f-g; Store u in row i of $_ { z }$ . f=0.0; for (j=0;j<i;j++) { if (yesvecs) Store $\mathbf { u } / H$ in column i of $_ { z }$ . z[j][i] $= _ { z }$ [i][j]/h; $\mathtt { g } = 0 . 0$ ; Form an element of $\mathbf { A } \cdot \mathbf { u }$ in $\mathsf { g }$ . for (k=0;k<j+1; $\mathrm { k } { + + }$ ) g $+ = \ z$ [j][k] $* z$ [i][k]; for (k=j+1;k<i; $\mathtt { k } { + } { + }$ ) g $+ = \ z$ [k][j] $* z$ [i][k]; e[j]=g/h; Form element of $\mathbf { p }$ in temporarily unus f $+ =$ e[j] $* z$ [i][j]; element of e. } hh=f/(h+h); Form $K$ , equation (11.3.11). for (j=0;j<i;j++) { Form q and store in e overwriting $\mathbf { p }$ $\scriptstyle { \mathtt { f } } = _ { z }$ [i][j]; e[j]=g=e[j]-hh\*f; for (k=0;k<j+1;k++) Reduce z, equation (11.3.13).

z[j][k] -= (f\*e[k]+g\*z[i][k]); } } } else e[i] $= _ { 2 }$ [i][l]; d[i] $\mathrm { \Phi = h }$ ; } if (yesvecs) d[0] ${ = } 0$ .0; e[0] ${ = } 0$ .0; for (i=0;i<n;i++) { Begin accumulation of transformation maif (yesvecs) { trices. if (d[i] $! =$ 0.0) { This block skipped when $\mathtt { i } = 0$ . for (j=0;j<i;j++) { $\mathtt { g } = 0 . 0$ ; for $( \mathtt { k } = 0$ ;k<i;k++) Use $\mathbf { u }$ and $\mathbf { u } / H$ stored in $_ z$ to form P Q. g $+ = \ z$ [i][k] $* z$ [k][j]; for $\scriptstyle 1 = 0$ ;k<i;k++) z[k][j] -= g\*z[k][i]; } } d[i] $= _ { 2 }$ [i][i]; z[i][i] $^ { = 1 }$ .0; Reset row and column of $_ z$ to identity for (j=0;j<i;j++) z[j][i] $= _ { 2 }$ [i][j] $= 0 . 0$ ; matrix for next iteration. } else { d[i] $= _ { z }$ [i][i]; Only this statement remains. } }

# CITED REFERENCES AND FURTHER READING:

Golub, G.H., and Van Loan, C.F. 1996, Matrix Computations, 3rd ed. (Baltimore: Johns Hopkins University Press), -5.1.[1]   
Smith, B.T., et al. 1976, Matrix Eigensystem Routines — EISPACK Guide, 2nd ed., vol. 6 of Lecture Notes in Computer Science (New York: Springer).   
Wilkinson, J.H., and Reinsch, C. 1971, Linear Algebra, vol. II of Handbook for Automatic Computation (New York: Springer).[2]

# 11.4 Eigenvalues and Eigenvectors of a Tridiagonal Matrix

We now turn to the second step in the grand strategy outlined in $\ S 1 1 . 2$ , namely computing the eigenvectors and eigenvalues of a tridiagonal matrix.

# 11.4.1 Evaluation of the Characteristic Polynomial

Once our original real symmetric matrix has been reduced to tridiagonal form, one possible way to determine its eigenvalues is to find the roots of the characteristic polynomial $p _ { n } ( \lambda )$ directly. The characteristic polynomial of a tridiagonal matrix can be evaluated for any trial value of $\lambda$ by an efficient recursion relation (see [1], for example). The polynomials of lower degree produced during the recurrence form a Sturmian sequence that can be used to localize the eigenvalues to intervals on the real axis. A root-finding method such as bisection or Newton’s method can then be employed to refine the intervals. The corresponding eigenvectors can then be found by inverse iteration (see $\ S 1 1 . 8 )$ .

Procedures based on these ideas can be found in [2,3]. If, however, more than a small fraction of all the eigenvalues and eigenvectors is required, then the factorization method next considered is much more efficient.

# 11.4.2 The QR and QL Algorithms

The basic idea behind the $\boldsymbol { \mathcal { Q } R }$ algorithm is that any real matrix can be decomposed in the form

$$
\mathbf { A } = \mathbf { Q } \cdot \mathbf { R }
$$

where Q is orthogonal and $\mathbf { R }$ is upper triangular. For a general matrix, the decomposition is constructed by applying Householder transformations to annihilate successive columns of A below the diagonal (see $\ S 2 . 1 0 \rangle$ .

Now consider the matrix formed by writing the factors in (11.4.1) in the opposite order:

$$
{ \bf A } ^ { \prime } = { \bf R } \cdot { \bf Q }
$$

Since $\mathbf { Q }$ is orthogonal, equation (11.4.1) gives $\mathbf { R } = \mathbf { Q } ^ { T } \cdot \mathbf { A }$ . Thus equation (11.4.2) becomes

$$
{ \bf A } ^ { \prime } = { \bf Q } ^ { T } \cdot { \bf A } \cdot { \bf Q }
$$

We see that $\mathbf { A } ^ { \prime }$ is an orthogonal transformation of $\mathbf { A }$ .

You can verify that a $\boldsymbol { \mathcal { Q } R }$ transformation preserves the following properties of a matrix: symmetry, tridiagonal form, and Hessenberg form (to be defined in $\ S 1 1 . 6 )$ .

There is nothing special about choosing one of the factors of $\mathbf { A }$ to be upper triangular; one could equally well make it lower triangular. This is called the $Q L$ algorithm, since

$$
\mathbf { A } = \mathbf { Q } \cdot \mathbf { L }
$$

where $\mathbf { L }$ is lower triangular. (The standard, but confusing, nomenclature $R$ and $L$ stands for whether the right or left of the matrix is nonzero.)

Recall that in the Householder reduction to tridiagonal form in $\ S 1 1 . 3$ , we started in column $n - 1$ of the original matrix. To minimize roundoff, we then exhorted you to put the biggest elements of the matrix in the lower right-hand corner, if you can. If we now wish to diagonalize the resulting tridiagonal matrix, the $Q L$ algorithm will have smaller roundoff than the $\boldsymbol { \mathcal { Q } R }$ algorithm, so we shall use $Q L$ henceforth.

The $Q L$ algorithm consists of a sequence of orthogonal transformations:

$$
\begin{array} { r l } { \mathbf { A } _ { s } = \mathbf { Q } _ { s } \cdot \mathbf { L } _ { s } } & { { } } \\ { \mathbf { A } _ { s + 1 } = \mathbf { L } _ { s } \cdot \mathbf { Q } _ { s } } & { { } \ ( = \mathbf { Q } _ { s } ^ { T } \cdot \mathbf { A } _ { s } \cdot \mathbf { Q } _ { s } ) } \end{array}
$$

The following (nonobvious!) theorem is the basis of the algorithm for a general matrix A: (i) If A has eigenvalues of different absolute value $| \lambda _ { i } |$ , then ${ \bf A } _ { S } \ $ [lower triangular form] as $s  \infty$ . The eigenvalues appear on the diagonal in increasing order of absolute magnitude. (ii) If A has an eigenvalue $| \lambda _ { i } |$ of multiplicity $p$ , ${ \bf A } _ { S } $ [lower triangular form] as $s \to \infty$ , except for a diagonal block matrix of order $p$ , whose eigenvalues $ \lambda _ { i }$ . The proof of this theorem is fairly lengthy; see, for example, [4].

The workload in the $Q L$ algorithm is $O ( n ^ { 3 } )$ per iteration for a general matrix, which is prohibitive. However, the workload is only $O ( n )$ per iteration for a tridiagonal matrix and $O ( n ^ { 2 } )$ for a Hessenberg matrix, which makes it highly efficient on these forms.

In this section we are concerned only with the case where $\mathbf { A }$ is a real, symmetric, tridiagonal matrix. All the eigenvalues $\lambda _ { i }$ are thus real. According to the theorem, if any $\lambda _ { i }$ has a multiplicity $p$ , then there must be at least $p - 1$ zeros on the sub- and superdiagonals. Thus the matrix can be split into submatrices that can be diagonalized separately, and the complication of diagonal blocks that can arise in the general case is irrelevant.

In the proof of the theorem quoted above, one finds that in general a superdiagonal element converges to zero like

$$
a _ { i j } ^ { ( s ) } \sim \left( \frac { \lambda _ { i } } { \lambda _ { j } } \right) ^ { s }
$$

Although $\lambda _ { i } < \lambda _ { j }$ , convergence can be slow if $\lambda _ { i }$ is close to $\lambda _ { j }$ . Convergence can be accelerated by the technique of shifting: If $k$ is any constant, then $\mathbf { A } - k \mathbf { 1 }$ has eigenvalues $\lambda _ { i } - k$ . If we decompose

$$
\mathbf { A } _ { s } - k _ { s } \mathbf { 1 } = \mathbf { Q } _ { s } \cdot \mathbf { L } _ { s }
$$

so that

$$
\begin{array} { r } { \mathbf { A } _ { s + 1 } = \mathbf { L } _ { s } \cdot \mathbf { Q } _ { s } + k _ { s } \mathbf { 1 } } \\ { = \mathbf { Q } _ { s } ^ { T } \cdot \mathbf { A } _ { s } \cdot \mathbf { Q } _ { s } } \end{array}
$$

then the convergence is determined by the ratio

$$
\frac { \lambda _ { i } - k _ { s } } { \lambda _ { j } - k _ { s } }
$$

The idea is to choose the shift $k _ { s }$ at each stage to maximize the rate of convergence. A good choice for the shift initially would be $k _ { s }$ close to $\lambda _ { 0 }$ , the smallest eigenvalue. Then the first row of off-diagonal elements would tend rapidly to zero. However, $\lambda _ { 0 }$ is not usually known a priori. A very effective strategy in practice (although there is no proof that it is optimal) is to compute the eigenvalues of the leading $2 \times 2$ diagonal submatrix of A. Then set $k _ { s }$ equal to the eigenvalue closer to $a _ { 0 0 }$ .

More generally, suppose you have already found $r$ eigenvalues of A. Then you can deflate the matrix by crossing out the first $r$ rows and columns, leaving

$$
\begin{array} { r } { \mathbf { A } = \left[ \begin{array} { l l l l l l l } { 0 } & & { \cdots } & { \cdots } & & & { 0 } \\ & { \cdots } & & & & & & \\ & { 0 } & & & & & & \\ { \vdots } & & & { d _ { r } } & { e _ { r } } & & & { \vdots } \\ { \vdots } & & & { e _ { r } } & { d _ { r + 1 } } & & & & \\ & & & & { \cdots } & & & { 0 } \\ & & & & & { d _ { n - 2 } } & { e _ { n - 2 } } \\ { 0 } & & { \cdots } & & & { 0 } & { e _ { n - 2 } } & { d _ { n - 1 } } \end{array} \right] } \end{array}
$$

Choose $k _ { s }$ equal to the eigenvalue of the leading $2 \times 2$ submatrix that is closer to $d _ { r }$ . One can show that the convergence of the algorithm with this strategy is generally cubic (and at worst quadratic for degenerate eigenvalues). This rapid convergence is what makes the algorithm so attractive.

Note that with shifting, the eigenvalues no longer necessarily appear on the diagonal in order of increasing absolute magnitude. The routine eigsrt (-11.1) can be used if required.

As we mentioned earlier, the $Q L$ decomposition of a general matrix is effected by a sequence of Householder transformations. For a tridiagonal matrix, however, it is more efficient to use plane rotations $\mathbf { P } _ { p q }$ . One uses the sequence $\mathbf { P } _ { 0 1 } , \mathbf { P } _ { 1 2 } , \dots , \mathbf { P } _ { n - 2 , n - 1 }$ to annihilate the elements $a _ { 0 1 } , a _ { 1 2 } , \dotsc , a _ { n - 2 , n - 1 }$ . By symmetry, the subdiagonal elements $a _ { 1 0 } , a _ { 2 1 } , \dotsc , a _ { n - 1 , n - 2 }$ will be annihilated too. Thus each $\mathbf { Q } _ { s }$ is a product of plane rotations:

$$
\mathbf { Q } _ { s } ^ { T } = \mathbf { P } _ { 1 } ^ { ( s ) } \cdot \mathbf { P } _ { 2 } ^ { ( s ) } \cdot \cdot \cdot \mathbf { P } _ { n - 1 } ^ { ( s ) }
$$

where $\mathbf { P } _ { i }$ annihilates $a _ { i - 1 , i }$ . Note that it is $\mathbf { Q } ^ { T }$ in equation (11.4.11), not $\mathbf { Q }$ , because we defined ${ \bf L } = { \bf Q } ^ { T } \cdot { \bf A }$ .

# 11.4.3 QL Algorithm with Implicit Shifts

The algorithm as described so far can be very successful. However, when the elements of A differ widely in order of magnitude, subtracting a large $k _ { s }$ from the diagonal elements can lead to loss of accuracy for the small eigenvalues. This difficulty is avoided by the $Q L$ algorithm with implicit shifts. The implicit $Q L$ algorithm is mathematically equivalent to the original $Q L$ algorithm, but the computation does not require $k _ { s } \mathbf { 1 }$ to be actually subtracted from A.

The algorithm is based on the following lemma: If A is a symmetric nonsingular matrix and ${ \bf B } = { \bf Q } ^ { T } \cdot { \bf A } \cdot { \bf Q }$ , where $\mathbf { Q }$ is orthogonal and $\mathbf { B }$ is tridiagonal with positive off-diagonal elements, then $\mathbf { Q }$ and $\mathbf { B }$ are fully determined when the last row of $\mathbf { Q } ^ { T }$ is specified. Proof: Let $\mathbf { q } _ { i } ^ { T }$ denote the row vector $i$ of the matrix $\mathbf { Q } ^ { T }$ . Then $\mathbf { q } _ { i }$ is the column vector $i$ of the matrix Q. The relation $\mathbf { B } \cdot \mathbf { Q } ^ { T } = \mathbf { Q } ^ { T } \cdot \mathbf { A }$ can be written

$$
\left[ \begin{array} { c c c c c c c } { \beta _ { 0 ~ } } & { \gamma _ { 0 ~ } } & & & & & \\ { \boldsymbol { \alpha } _ { 1 ~ } } & { \beta _ { 1 ~ } } & { \gamma _ { 1 ~ } } & & & & \\ & & & { \vdots } & & & & \\ & & & & { \boldsymbol { \alpha } _ { n - 2 ~ } } & { \beta _ { n - 2 ~ } } & { \gamma _ { n - 2 } } \\ & & & & & { \boldsymbol { \alpha } _ { n - 1 } } & { \beta _ { n - 1 } } \end{array} \right] \cdot \left[ { \begin{array} { c } { \mathbf { q } _ { 0 ~ } ^ { T } } \\ { \mathbf { q } _ { 1 ~ } ^ { T } } \\ { \vdots } \\ { \mathbf { q } _ { n - 2 } ^ { T } } \\ { \mathbf { q } _ { n - 1 } ^ { T } } \end{array} } \right] = \left[ { \begin{array} { c } { \mathbf { q } _ { 0 ~ } ^ { T } } \\ { \mathbf { q } _ { 1 ~ } ^ { T } } \\ { \vdots } \\ { \mathbf { q } _ { n - 2 } ^ { T } } \\ { \mathbf { q } _ { n - 1 } ^ { T } } \end{array} } \right] \cdot \mathbf { A }
$$

Row $n - 1$ of this matrix equation is

$$
\alpha _ { n - 1 } \mathbf { q } _ { n - 2 } ^ { T } + \beta _ { n - 1 } \mathbf { q } _ { n - 1 } ^ { T } = \mathbf { q } _ { n - 1 } ^ { T } \cdot \mathbf { A }
$$

Since $\mathbf { Q }$ is orthogonal,

$$
\mathbf { q } _ { n - 1 } ^ { T } \cdot \mathbf { q } _ { m } = \delta _ { n - 1 , m }
$$

Thus, if we postmultiply equation (11.4.13) by $\mathbf { q } _ { n - 1 }$ , we find

$$
\beta _ { n - 1 } = \mathbf { q } _ { n - 1 } ^ { T } \cdot \mathbf { A } \cdot \mathbf { q } _ { n - 1 }
$$

which is known since $\mathbf { q } _ { n - 1 }$ is known. Then equation (11.4.13) gives

$$
\alpha _ { n - 1 } \mathbf q _ { n - 2 } ^ { T } = \mathbf z _ { n - 2 } ^ { T }
$$

where

$$
\mathbf { z } _ { n - 2 } ^ { T } \equiv \mathbf { q } _ { n - 1 } ^ { T } \cdot \mathbf { A } - \beta _ { n - 1 } \mathbf { q } _ { n - 1 } ^ { T }
$$

is known. Therefore

$$
\boldsymbol { \alpha } _ { n - 1 } ^ { 2 } = \mathbf { z } _ { n - 2 } ^ { T } \mathbf { z } _ { n - 2 } ,
$$

or

$$
\alpha _ { n - 1 } = | \mathbf { z } _ { n - 2 } |
$$

and

$$
{ \bf q } _ { n - 2 } ^ { T } = { \bf z } _ { n - 2 } ^ { T } / \alpha _ { n - 1 }
$$

(where $\alpha _ { n - 1 }$ is nonzero by hypothesis). Similarly, one can show by induction that if we know ${ \bf q } _ { n - 1 } , { \bf q } _ { n - 2 } , \dots , { \bf q } _ { n - j }$ and the $\alpha$ ’s, $\beta$ ’s, and $\gamma$ ’s up to level $n - j$ , one can determine the quantities at level $n - ( j + 1 )$ .

To apply the lemma in practice, suppose one can somehow find a tridiagonal matrix $\overline { { \mathbf { A } } } _ { s + 1 }$ such that

$$
\overline { { \mathbf { A } } } _ { s + 1 } = \overline { { \mathbf { Q } } } _ { s } ^ { T } \cdot \overline { { \mathbf { A } } } _ { s } \cdot \overline { { \mathbf { Q } } } _ { s }
$$

where $\bar { \bf Q } _ { s } ^ { T }$ is orthogonal and has the same last row as ${ \bf Q } _ { s } ^ { T }$ in the original $\mathcal { Q L }$ algorithm. Then $\bar { \mathbf { Q } } _ { s } = \mathbf { Q } _ { s }$ and $\overline { { \mathbf { A } } } _ { s + 1 } = \mathbf { A } _ { s + 1 }$ .

Now, in the original algorithm, from equation (11.4.11) we see that the last row of ${ \bf Q } _ { s } ^ { T }$ is the same as the last row of P .s/n1 . But recall that P .s/ is a plane rotation designed to annihilate the $( n - 2 , n - 1 )$ element of ${ \bf A } _ { s } - k _ { s } { \bf 1 }$ . A simple calculation using the expression (11.1.1) shows that it has parameters

$$
c = \frac { d _ { n - 1 } - k _ { s } } { \sqrt { e _ { n - 1 } ^ { 2 } + ( d _ { n - 1 } - k _ { s } ) ^ { 2 } } } \ , \qquad s = \frac { - e _ { n - 2 } } { \sqrt { e _ { n - 1 } ^ { 2 } + ( d _ { n - 1 } - k _ { s } ) ^ { 2 } } }
$$

The matrix P .s/ $\mathbf { P } _ { n - 1 } ^ { ( s ) } \cdot \mathbf { A } _ { s } \cdot \mathbf { P } _ { n - 1 } ^ { ( s ) T }$ is tridiagonal with two extra elements:

$$
\left[ \begin{array} { l l l l l l } { \cdots } & { } & { } & { } & { } & { } & { } \\ { } & { \times } & { \times } & { \times } & { } & { } \\ { } & { } & { \times } & { \times } & { \times } & { \bf { x } } \\ { } & { } & { } & { \times } & { \times } & { \times } \\ { } & { } & { } & { \bf { x } } & { \times } & { \times } \end{array} \right]
$$

We must now reduce this to tridiagonal form with an orthogonal matrix whose last row is Œ0; 0; : : : ; 0; 1 so that the last row of Qx Ts w ill stay equal to P .s/ . This can be done by a sequence of Householder or Givens transformations. For the special form of the matrix (11.4.23), Givens is better. We rotate in the plane $( n - 3 , n - 2 )$ to annihilate the $( n - 3 , n - 1 )$ element. [By symmetry, the $( n - 1 , n - 3 )$ element will also be zeroed.] This leaves us with a tridiagonal form except for the extra elements $( n - 4 , n - 2 )$ and $( n - 2 , n - 4 )$ . We annihilate these with a rotation in the $( n - 4 , n - 3 )$ -plane, and so on. Thus a sequence of $n - 2$ Givens rotations is required. The result is that

$$
\mathbf { Q } _ { s } ^ { T } = \bar { \mathbf { Q } } _ { s } ^ { T } = \bar { \mathbf { P } } _ { 1 } ^ { ( s ) } \cdot \bar { \mathbf { P } } _ { 2 } ^ { ( s ) } \cdots \bar { \mathbf { P } } _ { n - 2 } ^ { ( s ) } \cdot \mathbf { P } _ { n - 1 } ^ { ( s ) }
$$

where the $\bar { \bf P }$ ’s are the Givens rotations and ${ \bf P } _ { n - 1 }$ is the same plane rotation as in the original algorithm. Then equation (11.4.21) gives the next iterate of $\mathbf { A }$ . Note that the shift $k _ { s }$ enters implicitly through the parameters (11.4.22).

The following routine tqli (“Tridiagonal $Q L$ Implicit”), based algorithmically on the implementations in [2,3], works extremely well in practice. The number of iterations for the first few eigenvalues might be four or five, say, but meanwhile the off-diagonal elements in the lower right-hand corner have been reduced too. The later eigenvalues are liberated with very little work. The average number of iterations per eigenvalue is typically 1.3–1.6. The operation count per iteration is $O ( n )$ , with a fairly large effective coefficient, say $\sim 2 0 n$ . The total operation count for the diagonalization is then very roughly $\sim 2 0 n \times ( 1 . 3 – 1 . 6 ) n \sim 3 0 n ^ { 2 }$ . If the eigenvectors are required, the statements indicated by comments are included and there is an additional, much larger, workload of about $6 n ^ { 3 }$ operations.

# void Symmeig::tqli()

$Q L$ algorithm with implicit shifts to determine the eigenvalues and (optionally) the eigenvectors of a real, symmetric, tridiagonal matrix, or of a real symmetric matrix previously reduced by tred2 $( \ S 1 1 . 3 )$ . On input, ${ \mathsf { d } } \left[ 0 \ldots \ldots \mathbf { n - 1 } \right]$ contains the diagonal elements of the tridiagonal matrix. On output, it returns the eigenvalues. The vector $\mathbf { e } \left[ 0 \ldots \mathbf { n - 1 } \right]$ inputs the subdiagonal elements of the tridiagonal matrix, with e[0] arbitrary. On output $\ominus$ is destroyed. If the eigenvectors of a tridiagonal matrix are desired, the matrix $\mathbf { z } \left[ 0 \cdot \mathbf { { \vec { \sigma } } } \mathbf { \cdot } \mathbf { n } \mathbf { - } 1 \right] \left[ 0 \cdot \mathbf { { \vec { \sigma } } } \mathbf { \cdot } \mathbf { n } \mathbf { - } 1 \right]$ is input as the identity matrix. If the eigenvectors of a matrix that has been reduced by tred2 are required, then z is input as the matrix output by tred2. In either case, column k of $_ { z }$ returns the normalized eigenvector corresponding to d[k].

Int m,l,iter,i,k;   
Doub s,r,p,g,f,dd,c,b;   
const Doub EPS=numeric_limits<Doub>::epsilon();   
for ( $\dot { \bar { 1 } } = 1$ ;i<n;i++) e[i-1] $= _ { \ominus }$ [i]; Convenient to renumber the el  
e[n-1] ${ = } 0$ .0; ements of e.   
for $\scriptstyle 1 = 0$ ;l<n; $^ { 1 + + }$ ) { iter=0; do { for $\mathrm { \ m } { = } 1$ ;m<n-1;m++) { Look for a single small subdidd=abs(d[m])+abs(d[m+1]); agonal element to split the if (abs(e[m]) $< =$ EPS\*dd) break; matrix. } if (m $! = ~ 1 \AA$ ) { if (iter++ == 30) throw("Too many iterations in tqli"); $\mathrm { g } =$ (d[l+1]-d[l])/(2.0\*e[l]); Form shift. $\mathbf { r } =$ pythag(g,1.0); g=d[m]-d[l]+e[l]/(g+SIGN(r,g)); This is $d _ { m } - k _ { s }$ . s=c=1.0; p=0.0; for (i=m-1; $\therefore > = 1$ ;i--) { A plane rotation as in the origif=s\*e[i]; nal $Q L$ , followed by Givens b=c\*e[i]; rotations to restore tridiage[i+1]=(r=pythag(f,g)); onal form. if ( $\scriptstyle \mathbf { \bar { r } } \ = \ 0 . 0$ ) { Recover from underflow. d[i+1] -= p; e[m]=0.0; break; } s=f/r; $\scriptstyle \mathtt { c } = \mathtt { g } / \mathtt { r }$ ; g=d[i+1]-p; $\mathbf { \nabla } x =$ (d[i]-g)\*s+2.0\*c\*b; d[i+1]=g+(p=s\*r); g=c\*r-b; if (yesvecs) { for $( \mathrm { k } = 0$ ;k<n;k $^ { + + }$ ) { Form eigenvectors. $\scriptstyle \mathbf { f } = z$ [k] $\left[ \dot { \bf 1 } + \pm \dot { \bf 1 } \right]$ ; z[k][i+1]=s\*z[k][i]+c\*f;

z[k][i]=c\*z[k][i]-s\*f; } } } if $\scriptstyle \mathbf { \bar { r } } \ = \ 0 . 0$ && $\mathrm { ~ i ~ } > = \mathrm { ~ 1 ~ }$ ) continue; d[l] $\mathrm { ~ -- ~ p ~ }$ ; e[l]=g; e[m] $= 0 . 0$ ; } } while (m $! = ~ 2 )$ ; } }

Doub Symmeig::pythag(const Doub a, const Doub b) {   
Computes $( a ^ { \bar { 2 } } + \bar { b } ^ { 2 } ) ^ { 1 / 2 }$ without destructive underflow or overflow. Doub absa=abs(a), absb $\mid =$ abs(b); return (absa $>$ absb ? absa\*sqrt(1. $0 +$ SQR(absb/absa)) : (absb == 0.0 ? 0.0 : absb\*sqrt(1. $^ { 0 + }$ SQR(absa/absb))));   
}

# 11.4.4 Newer Methods

There are two newer algorithms for tridiagonal symmetric systems that are generally more efficient than the $Q L$ method, especially for large matrices. The first is the divide-and-conquer method [5]. This method divides the tridiagonal matrix into two halves, solves the eigenproblems in each of the two halves, and then stitches the two solutions together to generate the solution of the original problem. The method is applied recursively, with the $Q L$ method used once the matrices are sufficiently small. The method is implemented in LAPACK as dstevd and is about 2.5 times faster than the $Q L$ method for large matrices.

The fastest method of all for the vast majority of matrices is the MRRR algorithm (Multiple Relatively Robust Representations) [6]. As we will see in $\ S 1 1 . 8$ , inverse iteration can determine the eigenvectors of a tridiagonal matrix in $O ( n ^ { 2 } )$ operations. However, clustered eigenvalues lead to eigenvectors that are not properly orthogonal to one another. Using a procedure like Gram-Schmidt to orthogonalize the vectors is $O ( n ^ { 3 } )$ . The MRRR algorithm is a sophisticated version of inverse iteration that is $O ( n ^ { 2 } )$ without requiring Gram-Schmidt. An implementation is available in LAPACK as dstegr.

# CITED REFERENCES AND FURTHER READING:

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), pp. 331–335.[1]   
Wilkinson, J.H., and Reinsch, C. 1971, Linear Algebra, vol. II of Handbook for Automatic Computation (New York: Springer).[2]   
Smith, B.T., et al. 1976, Matrix Eigensystem Routines — EISPACK Guide, 2nd ed., vol. 6 of Lecture Notes in Computer Science (New York: Springer).[3]   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), -6.6.4.[4]   
Cuppen, J.J.M. 1981, “A Divide-and-Conquer Method for the Symmetric Tridiagonal Eigenproblem,” Numerische Mathematik, vol. 36, pp. 177–195.[5]   
Dhillon, I.S., and Parlett, B.N. 2004, “Multiple Representations to Compute Orthogonal Eigenvectors of Symmetric Tridiagonal Matrices,” Linear Algebra and Its Applications, vol. 387, pp. 1–28.[6]

# 11.5 Hermitian Matrices

The complex analog of a real symmetric matrix is a Hermitian matrix, satisfying equation (11.0.4). Jacobi transformations can be used to find eigenvalues and eigenvectors, as can Householder reduction to tridiagonal form followed by $Q L$ iteration. Complex versions of the previous routines jacobi, tred2, and tqli are quite analogous to their real counterparts. For working routines, consult [1,2].

An alternative, using the routines in this book, is to convert the Hermitian problem to a real symmetric one: If ${ \mathbf { C } } = { \mathbf { A } } + i { \mathbf { B } }$ is a Hermitian matrix, then the $n \times n$ complex eigenvalue problem

$$
( \mathbf { A } + i \mathbf { B } ) \cdot ( \mathbf { u } + i \mathbf { v } ) = \lambda ( \mathbf { u } + i \mathbf { v } )
$$

is equivalent to the $2 n \times 2 n$ real problem

$$
{ \begin{array} { r l } { { \biggl [ } \mathbf { A } } & { - \mathbf { B } { \biggr ] } . { \biggl [ } \mathbf { u } { \biggr ] } = \lambda { \biggl [ } \mathbf { u } { \biggr ] } } \\ { \mathbf { B } } & { \mathbf { A } } \end{array} }
$$

Note that the $2 n \times 2 n$ matrix in (11.5.2) is symmetric: $\mathbf { A } ^ { T } = \mathbf { A }$ and $\mathbf { B } ^ { T } = - \mathbf { B }$ if $\mathbf { C }$ is Hermitian.

Corresponding to a given eigenvalue $\lambda$ , the vector

$$
\begin{array} { r } { \left[ \mathbf { - v } \right] } \\ { \mathbf { u } } \end{array}
$$

is also an eigenvector, as you can verify by writing out the two matrix equations implied by (11.5.2). Thus, if $\lambda _ { 0 } , \lambda _ { 1 } , \ldots , \lambda _ { n - 1 }$ are the eigenvalues of $\mathbf { C }$ , then the $2 n$ eigenvalues of the augmented problem (11.5.2) are $\lambda _ { 0 } , \lambda _ { 0 } , \lambda _ { 1 } , \lambda _ { 1 } , \dots , \lambda _ { n - 1 } , \lambda _ { n - 1 }$ ; each, in other words, is repeated twice. The eigenvectors are pairs of the form $\mathbf { u } + i \mathbf { v }$ and $i ( { \bf u } + i { \bf v } )$ ; that is, they are the same up to an inessential phase. Thus we solve the augmented problem (11.5.2) and choose one eigenvalue and eigenvector from each pair. These give the eigenvalues and eigenvectors of the original matrix C.

Working with the augmented matrix requires a factor of two more storage than the original complex matrix. In principle, a complex algorithm is also a factor of two more efficient in computer time than is the solution of the augmented problem. In practice, most complex implementations do not achieve this factor unless they are written entirely in real arithmetic. (Good library routines always do this.)

# CITED REFERENCES AND FURTHER READING:

Wilkinson, J.H., and Reinsch, C. 1971, Linear Algebra, vol. II of Handbook for Automatic Computation (New York: Springer).[1]   
Smith, B.T., et al. 1976, Matrix Eigensystem Routines — EISPACK Guide, 2nd ed., vol. 6 of Lecture Notes in Computer Science (New York: Springer).[2]

# 11.6 Real Nonsymmetric Matrices

The algorithms for symmetric matrices given in the preceding sections are highly satisfactory in practice. By contrast, it is impossible to design equally satisfactory algorithms for the nonsymmetric case. There are two reasons for this. First, the eigenvalues of a nonsymmetric matrix can be very sensitive to small changes in the matrix elements. Second, the matrix itself can be defective, so that there is no complete set of eigenvectors. We emphasize that these difficulties are intrinsic properties of certain nonsymmetric matrices, and no numerical procedure can “cure” them. The best we can hope for are procedures that don’t exacerbate such problems.

The presence of rounding error can only make the situation worse. With finiteprecision arithmetic, one cannot even design a foolproof algorithm to determine whether a given matrix is defective or not. Thus current algorithms generally try to find a complete set of eigenvectors and rely on the user to inspect the results. If any eigenvectors are almost parallel, the matrix is probably defective.

The strategy for finding the eigensystem of a general matrix parallels that of the symmetric case. First we reduce the matrix to a simpler form, and then we perform an iterative procedure on the simplified matrix. The simpler structure we use here is called Hessenberg form, defined later in this section. The user interface to the routine is very simple. The declaration

# Unsymmeig h(a);

computes all eigenvalues and eigenvectors of the matrix a. The eigenvalues are stored in the complex vector h.wri and the corresponding eigenvectors in the columns of the matrix h.zz. If h.wri[i] is real, the real eigenvector is in h. $z z \left[ 0 \ldots \ldots \right]$ [i]. For complex eigenvalues, if h.wri[i] has a positive imaginary part, then the complexconjugate eigenvalue is in $\mathtt { h . w r i } \left[ \mathtt { i } { + } 1 \right]$ . Only the eigenvector corresponding to h.wri[i] is returned, with the real part in $\mathtt { h . z z } [ 0 \AA . . \mathtt { n - 1 } \AA ]$ [i] and the imaginary part in $\mathtt { h . z z } [ 0 . \mathtt { \_ n - 1 } ] [ \mathrm { i } + 1 ]$ . The eigenvector corresponding to $\mathtt { h . w r i } \left[ \mathtt { i } { + } 1 \right]$ is simply the complex conjugate of this one.

Optional arguments allow you to compute only the eigenvalues, or to input a matrix already in Hessenberg form:

Unsymmeig h(a,false); Only eigenvalues computed.   
Unsymmeig h(a,true,true); Both eigenvalues and eigenvectors, Hessenberg matrix.

Here is the routine. The implementations of the various components are discussed in the rest of this section and the next.

# struct Unsymmeig {

Computes all eigenvalues and eigenvectors of a real nonsymmetric matrix by reduction to Hessenberg form followed by $Q R$ iteration.

Int n;   
MatDoub a,zz;   
VecComplex wri;   
VecDoub scale;   
VecInt perm;   
Bool yesvecs,hessen; Stores scaling from balance.   
Stores permutation from elmhes.

Unsymmeig(MatDoub_I &aa, Bool yesvec=true, Bool hessenb=false) n(aa.nrows()), a(aa), ${ \bf z } { \bf z } \left( \mathrm { n , n , 0 . 0 } \right)$ , wri(n), scale $( \mathrm { n } , 1 . 0 )$ , perm(n), yesvecs(yesvec), hessen(hessenb)

Computes all eigenvalues and (optionally) eigenvectors of a real nonsymmetric matrix $\mathbf { a } \left[ 0 \cdot \mathbf { \mathtt { n } } \mathbf { - } 1 \right] \left[ 0 \cdot \mathbf { \mathtt { n } } \mathbf { - } 1 \right]$ by reduction to Hessenberg form followed by $Q R$ iteration. If yesvecs is input as true (the default), then the eigenvectors are computed. Otherwise, only the eigenvalues are computed. If hessen is input as false (the default), the matrix is first reduced to Hessenberg form. Otherwise it is assumed that the matrix is already in Hessenberg from. On output, wri[0..n-1] contains the eigenvalues of a sorted into descending order, while zz[0..n-1][0..n-1] is a matrix whose columns contain the corresponding eigenvectors. For a complex eigenvalue, only the eigenvector corresponding to the eigenvalue with a positive imaginary part is stored, with the real part in $\mathbf { z } \mathbf { z } \left[ 0 \cdot \cdot \mathbf { n } \mathbf { - } 1 \right]$ [i] and the imaginary part in $\mathbf { h } \cdot \mathbf { z } \mathbf { z } \left[ 0 \cdot \mathbf { \mathbf { \sigma } } \cdot \mathbf { n } \mathbf { - } 1 \right] \left[ \mathbf { i } + 1 \right]$ . The eigenvectors are not normalized. {

balance(); if (!hessen) elmhes(); if (yesvecs) { for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) Initialize to unit matrix. zz[i][i] $^ { = 1 }$ .0; if (!hessen) eltran(); hqr2(); balbak(); sortvecs(); } else { hqr(); sort(); } } void balance(); void elmhes(); void eltran(); void hqr(); void hqr2(); void balbak(); void sort(); void sortvecs();

# 11.6.1 Balancing

The sensitivity of eigenvalues to rounding errors during the execution of some algorithms can be reduced by the procedure of balancing. The errors in the eigensystem found by a numerical procedure are generally proportional to the Euclidean norm of the matrix, that is, to the square root of the sum of the squares of the elements. The idea of balancing is to use similarity transformations to make corresponding rows and columns of the matrix have comparable norms, thus reducing the overall norm of the matrix while leaving the eigenvalues unchanged. A symmetric matrix is already balanced.

Balancing is a procedure with of order $N ^ { 2 }$ operations. Thus, the time taken by the procedure balance, given below, should never be significant compared to the total time required to find the eigenvalues. It is therefore recommended that you always balance nonsymmetric matrices. It never hurts, and it can substantially improve the accuracy of the eigenvalues computed for a badly balanced matrix.

The actual algorithm used is due to Osborne, as discussed in [1]. It consists of a sequence of similarity transformations by diagonal matrices D. To avoid introducing rounding errors during the balancing process, the elements of $\mathbf { D }$ are restricted to be exact powers of the radix base employed for floating-point arithmetic (i.e., 2 for all modern machines, but 16 for some historical mainframe architectures). The output is a matrix that is balanced in the norm given by summing the absolute magnitudes of the matrix elements. This is more efficient than using the Euclidean norm, and equally effective: A large reduction in one norm implies a large reduction in the other.

Note that if the off-diagonal elements of any row or column of a matrix are all zero, then the diagonal element is an eigenvalue. If the eigenvalue happens to be ill-conditioned (sensitive to small changes in the matrix elements), it will have relatively large errors when determined by the routine hqr (-11.7). Had we merely inspected the matrix beforehand, we could have determined the isolated eigenvalue exactly and then deleted the corresponding row and column from the matrix. You should consider whether such a pre-inspection might be useful in your application. (For symmetric matrices, the routines we gave will determine isolated eigenvalues accurately in all cases.)

The routine balance keeps track of the scale factors used in the balancing. If you are computing eigenvectors as well as eigenvalues, then the accumulated similarity transformation of the original matrix is undone by applying these scale factors in the routine balbak.

# void Unsymmeig::balance()

Given a matrix a[0..n-1][0..n-1], this routine replaces it by a balanced matrix with identical eigenvalues. A symmetric matrix is already balanced and is unaffected by this procedure.

const Doub RADIX $=$ numeric_limits<Doub>::radix; Bool done $=$ false; Doub sqrdx $: = \cdot$ RADIX $^ *$ RADIX; while (!done) { done=true; for (Int $\scriptstyle \dot { 1 } = 0$ ;i<n;i $^ { + + }$ ) { Calculate row and column norms. Doub $\scriptstyle { \mathtt { r } } = 0$ .0, $\mathtt { c } { = } 0$ .0; for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) if (j $\ ! =$ i) { c $+ =$ abs(a[j][i]); r += abs(a[i][j]); } if (c $\smash { ! = ~ 0 , 0 }$ && r != 0.0) { If both are nonzero, Doub $\mathrm { g } = \mathrm { x }$ /RADIX; Doub $\mathtt { f } = 1 \mathtt { \Omega } . 0$ ; Doub $\mathtt { s } \mathtt { = } \mathtt { c } \mathtt { + } \mathtt { r }$ ; while (c<g) { find the integer power of the machine f $\ast =$ RADIX; radix that comes closest to balancc $\ast =$ sqrdx; ing the matrix. $\mathtt { g } \mathrm { = } \mathtt { r } \ast$ RADIX; while (c>g) { f $^ { \prime } =$ RADIX; c /= sqrdx; } if ((c+r)/f < 0.95\*s) { done=false; $\mathrm { g } { = } 1$ .0/f; scale[i] $\ast =$ f; for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) a[i][j] $\ast = \ \mathtt { g } ;$ Apply similarity transformafor (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<n;j $^ { + + }$ ) a[j][i] $\ast =$ f; tion. } } } } 1

void Unsymmeig::balbak()   
Forms the eigenvectors of a real nonsymmetric matrix by back transforming those of the corre  
sponding balanced matrix determined by balance.   
{ for (Int $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) for (Int j=0;j<n;j++) zz[i][j] $* =$ scale[i];

# 11.6.2 Reduction to Hessenberg Form

An upper Hessenberg matrix has zeros everywhere below the diagonal except for the first subdiagonal row. For example, in the $6 \times 6$ case, the nonzero elements are

$$
\left[ { \begin{array} { l l l l l l l } { \times } & { \times } & { \times } & { \times } & { \times } & { \times } & { \times } \\ { \times } & { \times } & { \times } & { \times } & { \times } & { \times } & { \times } \\ & { \times } & { \times } & { \times } & { \times } & { \times } & { \times } \\ & & { \times } & { \times } & { \times } & { \times } & { \times } \\ & & & { \times } & { \times } & { \times } & { \times } \\ & & & & & { \times } & { \times } \end{array} } \right]
$$

By now you should be able to tell at a glance that such a structure can be achieved by a sequence of Householder transformations, each one zeroing the required elements in a column of the matrix. Householder reduction to Hessenberg form is in fact an accepted technique. An alternative, however, is a procedure analogous to Gaussian elimination with pivoting. We will use this elimination procedure since it is about a factor of two more efficient than the Householder method, and also since we want to teach you the method. It is possible to construct matrices for which the Householder reduction, being orthogonal, is stable and elimination is not, but such matrices are extremely rare in practice.

Straight Gaussian elimination is not a similarity transformation of the matrix. Accordingly, the actual elimination procedure used is slightly different. We proceed in a series of stages $r = 1 , 2 , \ldots , N - 2$ . Before the $r$ th stage, the original matrix $\mathbf { A } \equiv \mathbf { A } _ { 1 }$ has become ${ \bf A } _ { r }$ , which is upper Hessenberg up to, but not including, row and column $r - 1$ . The $r$ th stage then consists of the following sequence of operations:

- Find the element of maximum magnitude in column $r - 1$ below the diagonal. If it is zero, skip the next two “bullets” and the stage is done. Otherwise, suppose the maximum element was in row $r ^ { \prime }$ . Interchange rows $r ^ { \prime }$ and $r$ . This is the pivoting procedure. To make the permutation a similarity transformation, also interchange columns $r ^ { \prime }$ and $r$ . - For $i = r + 1 , r + 2 , \ldots , N - 1$ , compute the multiplier

$$
n _ { i r } \equiv \frac { a _ { i , r - 1 } } { a _ { r , r - 1 } }
$$

Subtract $n _ { i r }$ times row $r$ from row $i$ . To make the elimination a similarity transformation, also add $n _ { i r }$ times column $i$ to column $r$ .

A total of $N - 2$ such stages are required.

When the magnitudes of the matrix elements vary over many orders, you should try to rearrange the matrix so that the largest elements are in the top left-hand corner. This reduces the roundoff error, since the reduction proceeds from left to right.

The routine elmhes keeps track of the permutations applied during the elimination. If you are computing eigenvectors, then the accumulated similarity transformation is applied to the eigenvectors by the routine eltran, which includes any necessary permutations. The operation count is about $5 N ^ { 3 } / 3$ for large $N$ .

# void Unsymmeig::elmhes()

Reduction to Hessenberg form by the elimination method. Replaces the real nonsymmetric matrix a[0..n-1][0..n-1] by an upper Hessenberg matrix with identical eigenvalues. Recommended, but not required, is that this routine be preceded by balance. On output, the Hessenberg matrix is in elements a[i][j] with $\mathrm { ~ i ~ } \leq \mathrm { ~ j + 1 ~ }$ . Elements with $\mathrm { ~ i ~ } > \mathrm { ~ j + 1 ~ }$ are to be thought of as zero, but are returned with random values.

for (Int $\mathrm { m } = 1$ ;m<n-1;m++) { m is called $r$ in the text. Doub $\mathtt { x } = 0 \mathtt { . 0 }$ ; Int $\dot { 1 } = \mathfrak { m }$ ; for (Int j=m;j<n;j $^ { + + }$ ) { Find the pivot. if (abs(a[j][m-1]) $>$ abs(x)) { $\mathtt { x } = \mathtt { a }$ [j][m-1]; i=j; } } perm[m] ${ \boldsymbol { = } } { \dot { \boldsymbol { \mathrm { 1 } } } }$ ; Store permutation. if (i != m) { Interchange rows and columns. for (Int $\scriptstyle { \dot { \mathsf { J } } } = { \mathtt { m } } - 1$ ;j<n;j++) SWAP(a[i][j],a[m][j]); for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) SWAP(a[j][i],a[j][m]); if $( \textbf { x } : = \textbf { 0 } . 0 )$ ) { Carry out the elimination. for ( $\scriptstyle { \dot { \mathbf { 1 } } } = { \mathbf { m } } + 1$ ;i<n;i++) { Doub $\mathtt { y } = \mathtt { a }$ [i][m-1]; if (y $\ ! = \ 0 . 0 { \dot { , } }$ ) { y $\mathbf { \Psi } / = \mathbf { \Psi } \mathbf { x }$ ; a[i][m-1]=y; for (Int j=m;j<n;j++) a[i][j] $- =$ y\*a[m][j]; for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<n;j++) a[j][m] $+ =$ y\*a[j][i]; } } } } }

# void Unsymmeig::eltran()

This routine accumulates the stabilized elementary similarity transformations used in the reduction to upper Hessenberg form by elmhes. The multipliers that were used in the reduction are obtained from the lower triangle (below the subdiagonal) of a. The transformations are permuted according to the permutations stored in perm by elmhes.

for (Int mp=n-2;mp>0;mp--) { for (Int k=mp+1;k<n;k++) zz[k][mp] $= a$ [k][mp-1]; Int i=perm[mp]; if (i ! $=$ mp) { for (Int j=mp;j<n;j++) { zz[mp][j]=zz[i][j]; zz[i][j]=0.0; } zz[i][mp] ${ = } 1$ .0; } } }

# CITED REFERENCES AND FURTHER READING:

Wilkinson, J.H., and Reinsch, C. 1971, Linear Algebra, vol. II of Handbook for Automatic Computation (New York: Springer).[1]   
Smith, B.T., et al. 1976, Matrix Eigensystem Routines — EISPACK Guide, 2nd ed., vol. 6 of Lecture Notes in Computer Science (New York: Springer).[2]   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), -6.5.4.[3]

# 11.7 The QR Algorithm for Real Hessenberg Matrices

To complete the strategy for real, nonsymmetric matrices that was laid out in $\ S 1 1 . 6$ , we need to compute the eigenvalues and eigenvectors of a real Hessenberg matrix. Recall the following relations for the $\boldsymbol { \mathcal { Q } R }$ algorithm with shifts:

$$
\mathbf { Q } _ { s } \cdot ( \mathbf { A } _ { s } - k _ { s } \mathbf { 1 } ) = \mathbf { R } _ { s }
$$

where $\mathbf { Q }$ is orthogonal and $\mathbf { R }$ is upper triangular, and

$$
\begin{array} { r } { \mathbf { A } _ { s + 1 } = \mathbf { R } _ { s } \cdot \mathbf { Q } _ { s } ^ { T } + k _ { s } \mathbf { 1 } } \\ { = \mathbf { Q } _ { s } \cdot \mathbf { A } _ { s } \cdot \mathbf { Q } _ { s } ^ { T } } \end{array}
$$

The $\boldsymbol { \mathcal { Q } R }$ transformation preserves the upper Hessenberg form of the original matrix $\textbf { A } \equiv \textbf { A } _ { 1 }$ , and the workload on such a matrix is $O ( n ^ { 2 } )$ per iteration as opposed to $O ( n ^ { 3 } )$ on a general matrix. As $s  \infty$ , ${ \bf A } _ { s }$ converges to a form where the eigenvalues are either isolated on the diagonal or are eigenvalues of a $2 \times 2$ submatrix on the diagonal.

As we pointed out in $\ S 1 1 . 4$ , shifting is essential for rapid convergence. A key difference here is that a nonsymmetric real matrix can have complex eigenvalues. This means that good choices for the shifts $k _ { s }$ may be complex, apparently necessitating complex arithmetic.

Complex arithmetic can be avoided, however, by a clever trick. This trick, plus a detailed description of how the $\boldsymbol { \mathcal { Q } R }$ algorithm is used, is described in a Webnote [1].

The operation count for the $\boldsymbol { \mathcal { Q } R }$ algorithm for Hessenberg matrices is $\sim 1 0 k ^ { 2 }$ per iteration, where $k$ is the current size of the matrix. The typical average number of iterations per eigenvalue is about two, so the total operation count for all the eigenvalues is $\sim 1 0 n ^ { 3 }$ . The total operation count for both eigenvalues and eigenvectors is $\sim 2 5 n ^ { 3 }$ .

The routines hqr for the eigenvalues only, and hqr2, which computes both eigenvalues and eigenvectors, are given in full in a Webnote [2], along with a few Unsymmeig utility routines not already listed. The implementations are based algorithmically on the above description, in turn following the implementations in [3,4].

# CITED REFERENCES AND FURTHER READING:

Numerical Recipes Software 2007, “Description of the QR Algorithm for Hessenberg Matrices,” Numerical Recipes Webnote No.16,at http://www.nr.com/webnotes?16[1]   
Numerical Recipes Software 2007, “Implementations in Unsymmeig,” Numerical Recipes Webnote No. 17,at http://www.nr.com/webnotes?17 [2]   
Wilkinson, J.H., and Reinsch, C. 1971, Linear Algebra, vol. II of Handbook for Automatic Computation (New York: Springer).[3]   
Golub, G.H., and Van Loan, C.F. 1996, Matrix Computations, 3rd ed. (Baltimore: Johns Hopkins University Press), $\ S 7 . 5$ .   
Smith, B.T., et al. 1976, Matrix Eigensystem Routines — EISPACK Guide, 2nd ed., vol. 6 of Lecture Notes in Computer Science (New York: Springer).[4]

# 11.8 Improving Eigenvalues and/or Finding Eigenvectors by Inverse Iteration

The basic idea behind inverse iteration is quite simple. Let $\mathbf { y }$ be the solution of the linear system

$$
( \mathbf { A } - \tau \mathbf { 1 } ) \cdot \mathbf { y } = \mathbf { b }
$$

where $\mathbf { b }$ is a random vector and $\tau$ is close to some eigenvalue $\lambda$ of A. Then the solution y will be close to the eigenvector corresponding to $\lambda$ . The procedure can be iterated: Replace $\mathbf { b }$ by $\mathbf { y }$ and solve for a new $\mathbf { y }$ , which will be even closer to the true eigenvector.

We can see why this works by expanding both $\mathbf { y }$ and $\mathbf { b }$ as linear combinations of the eigenvectors $\mathbf { X } _ { j }$ of $\mathbf { A }$ :

$$
{ \bf y } = \sum _ { j } \alpha _ { j } { \bf x } _ { j } \qquad { \bf b } = \sum _ { j } \beta _ { j } { \bf x } _ { j }
$$

Then (11.8.1) gives

$$
\sum _ { j } \alpha _ { j } ( \lambda _ { j } - \tau ) { \bf x } _ { j } = \sum _ { j } \beta _ { j } { \bf x } _ { j }
$$

so that

$$
\alpha _ { j } = \frac { \beta _ { j } } { \lambda _ { j } - \tau }
$$

and

$$
\mathbf { y } = \sum _ { j } { \frac { \beta _ { j } \mathbf { x } _ { j } } { \lambda _ { j } - { \boldsymbol { \tau } } } }
$$

If $\tau$ is close to $\lambda _ { n }$ , say, then provided $\beta _ { n }$ is not accidentally too small, $\mathbf { y }$ will be approximately $\mathbf { X } _ { n }$ , up to a normalization. Moreover, each iteration of this procedure gives another power of $\lambda _ { j } - \tau$ in the denominator of (11.8.5). Thus the convergence is rapid for well-separated eigenvalues.

Suppose at the $k$ th stage of iteration we are solving the equation

$$
( \mathbf { A } - \tau _ { k } \mathbf { 1 } ) \cdot \mathbf { y } = \mathbf { b } _ { k }
$$

where $\mathbf { b } _ { k }$ and $\tau _ { k }$ are our current guesses for some eigenvector and eigenvalue of interest (let’s say ${ \bf { X } } _ { n }$ and $\lambda _ { n }$ ). Normalize $\mathbf { b } _ { k }$ so that $\mathbf { b } _ { k } \cdot \mathbf { b } _ { k } = 1$ . The exact eigenvector and eigenvalue satisfy

$$
{ \bf A } \cdot { \bf x } _ { n } = \lambda _ { n } { \bf x } _ { n }
$$

so

$$
( \mathbf { A } - \tau _ { k } \mathbf { 1 } ) \cdot \mathbf { x } _ { n } = ( \lambda _ { n } - \tau _ { k } ) \mathbf { x } _ { n }
$$

Since $\mathbf { y }$ of (11.8.6) is an improved approximation to ${ \bf { X } } _ { n }$ , we normalize it and set

$$
\mathbf b _ { k + 1 } = \frac { \mathbf y } { | \mathbf y | }
$$

We get an improved estimate of the eigenvalue by substituting our improved guess $\mathbf { y }$ for ${ \bf { X } } _ { n }$ in (11.8.8). By (11.8.6), the left-hand side is $\mathbf { b } _ { k }$ , so, calling $\lambda _ { n }$ our new value $\tau _ { k + 1 }$ , we find

$$
\tau _ { k + 1 } = \tau _ { k } + { \frac { 1 } { \mathbf { b } _ { k } \cdot \mathbf { y } } }
$$

While the above formulas look simple enough, in practice the implementation can be quite tricky. The first question to be resolved is when to use inverse iteration. Most of the computational load occurs in solving the linear system (11.8.6). Thus a possible strategy is first to reduce the matrix $\mathbf { A }$ to a special form that allows easy solution of (11.8.6). Tridiagonal form for symmetric matrices or Hessenberg for nonsymmetric are the obvious choices. The tridiagonal form can be solved in $O ( N )$ operations, the Hessenberg form in $O ( N ^ { 2 } )$ operations. If you then apply inverse iteration to generate all the eigenvectors, this gives an $O ( N ^ { 2 } )$ method for tridiagonal matrices. The problem is that closely spaced eigenvalues lead to eigenvectors that are not properly orthogonal to one another. Using a procedure like Gram-Schmidt to orthogonalize the vectors is $O ( n ^ { 3 } )$ , and not entirely satisfactory anyway. Accordingly, inverse iteration is generally used when one already has good eigenvalues and wants only a few selected eigenvectors.

You can write a simple inverse iteration routine yourself using $L U$ decomposition to solve (11.8.6). You can decide whether to use the general $L U$ algorithm we gave in Chapter 2 or whether to take advantage of tridiagonal or Hessenberg form. Note that, since the linear system (11.8.6) is nearly singular, you must be careful to use a version of $L U$ decomposition like that in $\ S 2 . 3$ which replaces a zero pivot with a very small number.

We have chosen not to give a general inverse iteration routine in this book, because it is quite cumbersome to take account of all the cases that can arise. Routines are given, for example, in [1-3]. If you use these, or write your own routine, you may appreciate the following pointers.

One starts by supplying an initial value $\tau _ { 0 }$ for the eigenvalue $\lambda _ { n }$ of interest. Choose a random normalized vector ${ \bf b } _ { 0 }$ as the initial guess for the eigenvector ${ \bf X } _ { n }$ , and solve (11.8.6). The new vector $\mathbf { y }$ is bigger than ${ \bf b } _ { 0 }$ by a “growth factor” $| \mathbf { y } |$ , which ideally should be large. Equivalently, the change in the eigenvalue, which by (11.8.10) is essentially $1 / \left| \mathbf { y } \right|$ , should be small. The following cases can arise:

- If the growth factor is too small initially, then we assume we have made a “bad” choice of random vector. This can happen not just because of a small $\beta _ { n }$ in (11.8.5), but also in the case of a defective matrix, when (11.8.5) does not even apply (see, e.g., [1] or [4] for details). We go back to the beginning and choose a new initial vector.   
The change $| \mathbf { b } _ { 1 } - \mathbf { b } _ { 0 } |$ might be less than some tolerance $\epsilon$ . We can use this as a criterion for stopping, iterating until it is satisfied, with a maximum of 5–10 iterations, say.   
After a few iterations, if $| \mathbf { b } _ { k + 1 } - \mathbf { b } _ { k } |$ is not decreasing rapidly enough, we can try updating the eigenvalue according to (11.8.10). If $\tau _ { k + 1 } = \tau _ { k }$ to machine accuracy, we are not going to improve the eigenvector much more and can quit. Otherwise start another cycle of iterations with the new eigenvalue.

The reason we do not update the eigenvalue at every step is that when we solve the linear system (11.8.6) by $L U$ decomposition, we can save the decomposition if $\tau _ { k }$ is fixed (assuming we are working with the full matrix). We only need to do the backsubstitution step each time we update $\mathbf { b } _ { k }$ . The number of iterations we decide to do with a fixed $\tau _ { k }$ is a trade-off between the quadratic convergence but $O ( N ^ { 3 } )$ workload for updating $\tau _ { k }$ at each step and the linear convergence but $O ( N ^ { 2 } )$ load for keeping $\tau _ { k }$ fixed. If you have determined the eigenvalue by one of the routines given earlier in the chapter, it is probably correct to machine accuracy anyway, and you can omit updating it.

There are two different pathologies that can arise during inverse iteration. The first is multiple or closely spaced roots. This is more often a problem with symmetric matrices. Inverse iteration will find only one eigenvector for a given initial guess $\tau _ { 0 }$ . A good strategy is to perturb the last few significant digits in $\tau _ { 0 }$ and then repeat the iteration. Usually this provides an independent eigenvector. Special steps generally have to be taken to ensure orthogonality of the linearly independent eigenvectors, whereas the Jacobi and $Q L$ algorithms automatically yield orthogonal eigenvectors even in the case of multiple eigenvalues.

The second problem, peculiar to nonsymmetric matrices, is the defective case. Unless one makes a “good” initial guess, the growth factor is small. Moreover, iteration does not improve matters. In this case, the remedy is to choose random initial vectors, solve (11.8.6) once, and quit as soon as any vector gives an acceptably large growth factor. Typically only a few trials are necessary.

One further complication in the nonsymmetric case is that a real matrix can have complex-conjugate pairs of eigenvalues. You will then have to use complex arithmetic to solve (11.8.6) for the complex eigenvectors. For any moderate-sized (or larger) nonsymmetric matrix, our recommendation is to avoid inverse iteration in favor of a $\boldsymbol { \mathcal { Q } R }$ method like Unsymmeig.

A good discussion of these and other problems with inverse iteration is given in [5]. As discussed in $\ S 1 1 . 4 . 4$ , for symmetric tridiagonal matrices, the MRRR algorithm is a sophisticated version of inverse iteration that avoids all these problems.

# CITED REFERENCES AND FURTHER READING:

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America).   
Wilkinson, J.H., and Reinsch, C. 1971, Linear Algebra, vol. II of Handbook for Automatic Computation (New York: Springer),p. 418.[1]   
Smith, B.T., et al. 1976, Matrix Eigensystem Routines — EISPACK Guide, 2nd ed., vol. 6 of Lecture Notes in Computer Science (New York: Springer).[2]   
Anderson, E., et al. 1999, LAPACK User’s Guide, 3rd ed. (Philadelphia: S.I.A.M.). Online with software at $^ { 2 0 0 7 + }$ , http://www.netlib.org/lapack.[3]   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 6 . 6 . 3 . [ 4 ]$ 1   
Dhillon, I.S. 1998, “Current Inverse Iteration Software Can Fail,” BIT Numerical Mathematics, vol. 38, pp. 685–704.[5]
