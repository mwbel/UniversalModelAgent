![](images/9e88795f3857bd7be0897a0e28479ec33f1aa5c6fa50b595d8054621db7644f4.jpg)  
Figure 18.0.2. Relaxation method (schematic). An initial solution is guessed that approximately satisfies the differential equation and boundary conditions. An iterative process adjusts the function to bring it into close agreement with the true solution.

equations “exactly” (or as exactly as we care to make our numerical integration), but the trial solutions come to satisfy the required boundary conditions only after the iterations are finished.

Relaxation methods use a different approach. The differential equations are replaced by finite difference equations on a mesh of points that covers the range of the integration. A trial solution consists of values for the dependent variables at each mesh point, not satisfying the desired finite difference equations, nor necessarily even satisfying the required boundary conditions. The iteration, now called relaxation, consists of adjusting all the values on the mesh so as to bring them into successively closer agreement with the finite difference equations and, simultaneously, with the boundary conditions (see Figure 18.0.2). For example, if the problem involves three coupled equations and a mesh of 100 points, we must guess and improve 300 variables representing the solution.

With all this adjustment, you may be surprised that relaxation is ever an efficient method, but (for the right problems) it really is! Relaxation works better than shooting when the boundary conditions are especially delicate or subtle, or where they involve complicated algebraic relations that cannot easily be solved in closed form. Relaxation works best when the solution is smooth and not highly oscillatory. Such oscillations would require many grid points for accurate representation. The number and position of required points may not be known a priori. Shooting methods are usually preferred in such cases, because their variable stepsize integrations adjust naturally to a solution’s peculiarities.

Relaxation methods are often preferred when the ODEs have extraneous solutions that, while not appearing in the final solution satisfying all boundary conditions, may wreak havoc on the initial value integrations required by shooting. The typical case is that of trying to maintain a dying exponential in the presence of growing exponentials.

Good initial guesses are the secret of efficient relaxation methods. Often one has to solve a problem many times, each time with a slightly different value of some parameter. In that case, the previous solution is usually a good initial guess when the parameter is changed, and relaxation will work well.

Until you have enough experience to make your own judgment between the two methods, you might wish to follow the advice of your authors, who are notorious computer gunslingers: We always shoot first, and only then relax.

# 18.0.1 Problems Reducible to the Standard Boundary Problem

There are two important problems that can be reduced to the standard boundary value problem described by equations $( 1 8 . 0 . 1 ) - ( 1 8 . 0 . 3 )$ . The first is the eigenvalue problem for differential equations. Here the right-hand side of the system of differential equations depends on a parameter $\lambda$ ,

$$
{ \frac { d y _ { i } ( x ) } { d x } } = g _ { i } ( x , y _ { 0 } , \dots , y _ { N - 1 } , \lambda )
$$

and one has to satisfy $N + 1$ boundary conditions instead of just $N$ . The problem is overdetermined and in general there is no solution for arbitrary values of $\lambda$ . For certain special values of $\lambda$ , the eigenvalues, equation (18.0.4) does have a solution.

We reduce this problem to the standard case by introducing a new dependent variable

$$
y _ { N } \equiv \lambda
$$

and another differential equation

$$
{ \frac { d y _ { N } } { d x } } = 0
$$

An example of this trick is given in $\ S 1 8 . 4$ .

The other case that can be put in the standard form is a free boundary problem. Here only one boundary abscissa $x _ { 1 }$ is specified, while the other boundary $x _ { 2 }$ is to be determined so that the system (18.0.1) has a solution satisfying a total of $N + 1$ boundary conditions. Here we again add an extra constant dependent variable:

$$
\begin{array} { c } { { y _ { N } \equiv x _ { 2 } - x _ { 1 } } } \\ { { } } \\ { { { \frac { d y _ { N } } { d x } } = 0 } } \end{array}
$$

We also define a new independent variable $t$ by setting

$$
x - x _ { 1 } \equiv t y _ { N } , \qquad 0 \leq t \leq 1
$$

The system of $N + 1$ differential equations for $d y _ { i } / d t$ is now in the standard form, with $t$ varying between the known limits 0 and 1.

# CITED REFERENCES AND FURTHER READING:

Keller, H.B. 1968, Numerical Methods for Two-Point Boundary-Value Problems; reprinted 1991 (New York: Dover).   
Kippenhan, R., Weigert, A., and Hofmeister, E. 1968, in Methods in Computational Physics, vol. 7 (New York: Academic Press), pp. 129ff.   
Eggleton, P.P. 1971, “The Evolution of Low Mass Stars,” Monthly Notices of the Royal Astronomical Society,vol.151, pp.351-364.   
London, R.A., and Flannery, B.P. 1982, “Hydrodynamics of X-Ray Induced Stellar Winds,” Astrophysical Journal, vol. 258, pp.260-269.   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 7 . 3 - \ S 7 . 4$ .

# 18.1 The Shooting Method

In this section we discuss “pure” shooting, where the integration proceeds from $x _ { 1 }$ to $x _ { 2 }$ , and we try to match boundary conditions at the end of the integration. In the next section, we describe shooting to an intermediate fitting point, where the solution to the equations and boundary conditions is found by launching “shots” from both sides of the interval and trying to match continuity conditions at some intermediate point.

Our implementation of the shooting method exactly implements multidimensional, globally convergent Newton-Raphson (-9.7). It seeks to zero $n _ { 2 }$ functions of $n _ { 2 }$ variables. The functions are obtained by integrating $N$ differential equations from $x _ { 1 }$ to $x _ { 2 }$ . Let us see how this works.

At the starting point $x _ { 1 }$ there are $N$ starting values $y _ { i }$ to be specified, but subject to $n _ { 1 }$ conditions. Therefore there are $n _ { 2 } = N - n _ { 1 }$ freely specifiable starting values. Let us imagine that these freely specifiable values are the components of a vector $\mathbf { V }$ that lives in a vector space of dimension $n _ { 2 }$ . Then you, the user, knowing the functional form of the boundary conditions (18.0.2), can write a function or functor that generates a complete set of $N$ starting values $\mathbf { y }$ , satisfying the boundary conditions at $x _ { 1 }$ , from an arbitrary vector value of $\mathbf { V }$ in which there are no restrictions on the $n _ { 2 }$ component values. In other words, (18.0.2) converts to a prescription

$$
y _ { i } ( x _ { 1 } ) = y _ { i } ( x _ { 1 } ; V _ { 0 } , \ldots , V _ { n _ { 2 } - 1 } ) \qquad i = 0 , \ldots , N - 1
$$

In the routine Shoot below, the function or functor that implements (18.1.1) will be called load, but you can pass it as an argument to the routine with any name of your choosing.

Notice that the components of $\mathbf { V }$ might be exactly the values of certain “free” components of $\mathbf { y }$ , with the other components of $\mathbf { y }$ determined by the boundary conditions. Alternatively, the components of $\mathbf { V }$ might parametrize the solutions that satisfy the starting boundary conditions in some other convenient way. Boundary conditions often impose algebraic relations among the $y _ { i }$ , rather than specific values for each of them. Using some auxiliary set of parameters often makes it easier to “solve” the boundary relations for a consistent set of $y _ { i }$ ’s. It makes no difference which way you go, as long as your vector space of $\mathbf { V }$ ’s generates (through 18.1.1) all allowed starting vectors $\mathbf { y }$ .

Given a particular $\mathbf { V }$ , a particular $\mathbf { y } ( x _ { 1 } )$ is thus generated. It can then be turned into a $\mathbf { y } ( x _ { 2 } )$ by integrating the ODEs to $x _ { 2 }$ as an initial value problem (e.g., using Chapter 17’s Odeint). Now, at $x _ { 2 }$ , let us define a discrepancy vector $\mathbf { F }$ , also of dimension $n _ { 2 }$ , whose components measure how far we are from satisfying the $n _ { 2 }$ boundary conditions at $x _ { 2 }$ (18.0.3). Simplest of all is just to use the right-hand sides of (18.0.3),

$$
F _ { k } = B _ { 2 k } ( x _ { 2 } , \mathbf { y } ) \qquad k = 0 , \ldots , n _ { 2 } - 1
$$

As in the case of $\mathbf { V }$ , however, you can use any other convenient parametrization, as long as your space of $\mathbf { F }$ ’s spans the space of possible discrepancies from the desired boundary conditions, with all components of $\mathbf { F }$ equal to zero if and only if the boundary conditions at $x _ { 2 }$ are satisfied. Below, you will be asked to supply a user-written function or functor that uses (18.0.3) to convert an $N$ -vector of ending values $\mathbf { y } ( x _ { 2 } )$ into an $n _ { 2 }$ -vector of discrepancies $\mathbf { F }$ . Inside Shoot, this function is called score.

Now, as far as Newton-Raphson is concerned, we are nearly in business. We want to find a vector value of $\mathbf { V }$ that zeros the vector value of $\mathbf { F }$ . We do this by invoking the globally convergent Newton’s method implemented in the routine newt of $\ S 9 . 7$ . Recall that the heart of Newton’s method involves solving the set of $n _ { 2 }$ linear equations

$$
\mathbf { J } \cdot \boldsymbol { \delta } \mathbf { V } = - \mathbf { F }
$$

and then adding the correction back,

$$
{ \bf V } ^ { \mathrm { n e w } } = { \bf V } ^ { \mathrm { o l d } } + \delta { \bf V }
$$

In (18.1.3), the Jacobian matrix $\mathbf { J }$ has components given by

$$
J _ { i j } = \frac { \partial F _ { i } } { \partial V _ { j } }
$$

It is not feasible to compute these partial derivatives analytically. Rather, each requires a separate integration of the $N$ ODEs, followed by the evaluation of

$$
\frac { \partial F _ { i } } { \partial V _ { j } } \approx \frac { F _ { i } ( V _ { 0 } , \dots , V _ { j } + \Delta V _ { j } , \dots ) - F _ { i } ( V _ { 0 } , \dots , V _ { j } , \dots ) } { \Delta V _ { j } }
$$

This is done automatically for you in the functor NRfdjac that comes with newt. The only input to newt that you have to provide is the routine vecfunc that calculates $\mathbf { F }$ by integrating the ODEs. Here is the appropriate routine, a functor called Shoot, that is to be passed as the actual argument in newt:

template <class L, class R, class S>   
struct Shoot {   
Functor for use with newt to solve a two-point boundary value problem by shooting. Int nvar; Number of coupled ODEs. Doub x1,x2; Start and end points. L &load; Supplies initial values for ODEs from $\mathtt { v } [ 0 \dots \mathrm { n } 2 \AA ^ { - 1 } ]$ . R &d; Supplies derivative information to the ODE integrator. S &score; Returns the n2 functions that ought to be zero to satisfy Doub atol,rtol; the boundary conditions at $\tt x 2$ . Doub h1,hmin; VecDoub y; Shoot(Int nvarr, Doub xx1, Doub xx2, L &loadd, R &dd, S &scoree) nvar(nvarr), x1(xx1), x2(xx2), load(loadd), d(dd), score(scoree), atol(1.0e-14), rtol(atol), hmin(0.0), y(nvar) {}

Routine for use with newt to solve a two-point boundary value problem for nvar coupled ODEs by shooting from x1 to $\tt x 2$ . Initial values for the nvar ODEs at x1 are generated from the n2 input coefficients v[0..n2-1], using the user-supplied routine load.

This is the functor used by newt. It integrates the ODEs to x2 using an eighth-order Runge-Kutta method with absolute and relative tolerances atol and rtol, initial stepsize h1, and minimum stepsize hmin. At $\mathbf { x } 2$ it calls the user-supplied routine score and returns the n2 functions that ought to be zero. newt uses a globally convergent Newton’s method to adjust the values of v until the returned functions are in fact zero.

$\mathtt { h 1 } = \left( \mathtt { x 2 } \mathtt { - x 1 } \right) / 1 0 0 \ldots 0 ;$ ; y=load(x1,v); Output out; No output generated by Odeint. Odeint<StepperDopr853<R> $>$ integ(y,x1,x2,atol,rtol,h1,hmin,out,d); integ.integrate(); return score(x2,y); } };

Note that Shoot is templated on the load, right-hand side for Odeint, and score routines. In practice, you will almost always want to write these as functors rather than functions. This makes communicating the various parameters in the problem easy — just pass them as parameters in the constructors.

For some problems the initial stepsize $\Delta V$ might depend sensitively upon the initial conditions. It is straightforward to alter load to compute a suggested stepsize h1 as a member variable and feed it fist to Shoot and hence to NRfdjac when the Shoot object is passed to newt.

A complete cycle of the shooting method thus requires $n _ { 2 } + 1$ integrations of the $N$ coupled ODEs: one integration to evaluate the current degree of mismatch, and $n _ { 2 }$ for the partial derivatives. Each new cycle requires a new round of $n _ { 2 } + 1$ integrations. This illustrates the enormous extra effort involved in solving two-point boundary value problems compared with initial value problems.

If the differential equations are linear, then only one complete cycle is required, since $( 1 8 . 1 . 3 ) - ( 1 8 . 1 . 4 )$ should take us right to the solution. A second round can be useful, however, in mopping up some (never all) of the roundoff error.

As given here, Shoot uses the high-efficiency eighth-order Runge-Kutta method of $\ S 1 7 . 2$ to integrate the ODEs, but any of the other methods of Chapter 17 could just as well be used.

You, the user, must supply Shoot with: (i) a function or functor load $( \mathbb { x } 1 , \mathbb { v } )$ that returns the n-vector $\mathtt { y } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ (satisfying the starting boundary conditions, of course), given the freely specifiable variables of $\mathtt { v } [ 0 \dots \mathrm { n } 2 \AA ^ { - 1 } ]$ at the initial point $\tt x 1$ ; (ii) a function or functor $\mathtt { s c o r e } ( \mathtt { x } 2 , \mathtt { y } )$ that returns the discrepancy vector $\mathtt { f } [ 0 \ldots$ $\mathtt { n } 2 \mathtt { - } 1 ]$ of the ending boundary conditions, given the vector $\mathtt { y } [ 0 \dots \underbrace { \mathtt { n } ^ { - 1 } } ]$ at the endpoint $_ { \tt X 2 }$ ; (iii) a starting vector $\mathtt { v } [ 0 \dots \mathrm { n } 2 \AA ^ { - 1 } ]$ ; (iv) a function or functor, called d in the routine, for the ODE integration; and other obvious parameters as described in the header comment above.

In $\ S 1 8 . 4$ we give a sample program illustrating how to use Shoot.

# CITED REFERENCES AND FURTHER READING:

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America).   
Keller, H.B. 1968, Numerical Methods for Two-Point Boundary-Value Problems; reprinted 1991 (New York: Dover).

# 18.2 Shooting to a Fitting Point

The shooting method described in $\ S 1 8 . 1$ tacitly assumed that the “shots” would be able to traverse the entire domain of integration, even at the early stages of convergence to a correct solution. In some problems it can happen that, for very wrong starting conditions, an initial solution can’t even get from $x _ { 1 }$ to $x _ { 2 }$ without encountering some incalculable, or catastrophic, result. For example, the argument of a square root might go negative, causing the numerical code to crash. Simple shooting would be stymied.

A different, but related, case is where the endpoints are both singular points of the set of ODEs. One frequently needs to use special methods to integrate near the singular points, analytic asymptotic expansions, for example. In such cases it is feasible to integrate in the direction away from a singular point, using the special method to get through the first little bit and then reading off “initial” values for further numerical integration. However, it is generally not feasible to integrate into a singular point. Usually the desired boundary condition is that one wants a regular solution at the singular point, but integrating into a singularity is guaranteed to pick out a singular solution, which by definition is growing as one integrates inward. Any small numerical inaccuracy will include some admixture of the “wrong” solution, which grows and swamps the desired solution.

The solution to the above-mentioned difficulties is shooting to a fitting point. Instead of integrating from $x _ { 1 }$ to $x _ { 2 }$ , we integrate first from $x _ { 1 }$ to some point $x _ { f }$ that is between $x _ { 1 }$ and $x _ { 2 }$ ; and second from $x _ { 2 }$ (in the opposite direction) to $x _ { f }$ .

If (as before) the number of boundary conditions imposed at $x _ { 1 }$ is $n _ { 1 }$ , and the number imposed at $x _ { 2 }$ is $n _ { 2 }$ , then there are $n _ { 2 }$ freely specifiable starting values at $x _ { 1 }$ and $n _ { 1 }$ freely specifiable starting values at $x _ { 2 }$ . (If you are confused by this, go back to $\ S 1 8 . 1 .$ .) We can therefore define an $n _ { 2 }$ -vector $\mathbf { V } ^ { ( 1 ) }$ of starting parameters at $x _ { 1 }$ and a prescription load1(x1,v1) for mapping $\mathbf { V } ^ { ( 1 ) }$ into a $\mathbf { y }$ that satisfies the boundary conditions at $x _ { 1 }$ :

$$
y _ { i } ( x _ { 1 } ) = y _ { i } ( x _ { 1 } ; V _ { 0 } ^ { ( 1 ) } , \ldots , V _ { n _ { 2 } - 1 } ^ { ( 1 ) } ) \qquad i = 0 , \ldots , N - 1
$$

Likewise we can define an $n _ { 1 }$ -vector $\mathbf { V } ^ { ( 2 ) }$ of starting parameters at $x _ { 2 }$ and a prescription load2 $( \mathtt { x } 2 , \mathtt { v } 2 )$ for mapping $\mathbf { V } ^ { ( 2 ) }$ into a $\mathbf { y }$ that satisfies the boundary conditions at $x _ { 2 }$ :

$$
y _ { i } ( x _ { 2 } ) = y _ { i } ( x _ { 2 } ; V _ { 0 } ^ { ( 2 ) } , \ldots , V _ { n _ { 1 } - 1 } ^ { ( 2 ) } ) \qquad i = 0 , \ldots , N - 1
$$

We thus have a total of $N$ freely adjustable parameters in the combination of V .1/ and V .2/. The N conditions that must be satisfied are that there be agreement in $N$ components of $\mathbf { y }$ at $x _ { f }$ between the values obtained integrating from one side and from the other,

$$
y _ { i } ( x _ { f } ; { \mathbf { V } } ^ { ( 1 ) } ) = y _ { i } ( x _ { f } ; { \mathbf { V } } ^ { ( 2 ) } ) \qquad i = 0 , \ldots , N - 1
$$

In some problems, the $N$ matching conditions can be better described (physically, mathematically, or numerically) by using $N$ different functions $F _ { i }$ ; $i = 0 \dots N - 1$ , each possibly depending on the $N$ components $y _ { i }$ . In those cases, (18.2.3) is replaced by

$$
F _ { i } [ { \bf y } ( x _ { f } ; { \bf V } ^ { ( 1 ) } ) ] = F _ { i } [ { \bf y } ( x _ { f } ; { \bf V } ^ { ( 2 ) } ) ] \qquad i = 0 , \dots , N - 1
$$

In the program below, a user-supplied function or functor, called score(xf,y) in the routine, is supposed to map an input $N$ -vector y into an output $N$ -vector F . In most cases, you can simply use the identity mapping $\mathbf { F } = \mathbf { y }$ .

Shooting to a fitting point uses globally convergent Newton-Raphson exactly as in $\ S 1 8 . 1$ . Comparing closely with the routine Shoot of the previous section, you should have no difficulty in understanding the following routine Shootf. The main differences in use are that you have to supply both load1 and load2. Also, in the calling program you must supply initial guesses for $\mathtt { v 1 } [ 0 \dots \mathrm { n 2 } \overline { { 2 } } \overline { { - 1 } } ]$ and $\mathtt { v } 2 [ 0 \dots \mathrm { n } 1 - 1 ]$ . Once again, a sample program illustrating shooting to a fitting point is given in $\ S 1 8 . 4$ .

template <class L1, class L2, class R, class S> struct Shootf {

Functor for use with newt to solve a two-point boundary value problem by shooting to a fitting point.

Int nvar,n2; nvar is the number of coupled ODEs.   
Doub x1,x2,xf; Start and end points and fitting point.   
L1 &load1; load1 and load2 supply initial values for the ODEs.   
L2 &load2;   
R &d; Supplies derivative information to the ODE integrator.   
S &score; Computes the mismatch of the solutions at the fitting   
Doub atol,rtol; point.   
Doub h1,hmin;   
VecDoub y,f1,f2;   
Shootf(Int nvarr, Int nn2, Doub xx1, Doub xx2, Doub xxf, L1 &loadd1, L2 &loadd2, R &dd, S &scoree) : nvar(nvarr), n2(nn2), x1(xx1), x2(xx2), xf(xxf), load1(loadd1), load2(loadd2), d(dd), score(scoree), atol(1.0e-14), rtol(atol), hmin(0.0), y(nvar), f1(nvar), f2(nvar) {}

Routine for use with newt to solve a two-point boundary value problem for nvar coupled ODEs by shooting from $\tt x 1$ and $\tt x 2$ to a fitting point xf. Initial values for the nvar ODEs at x1 are generated from the n2 coefficients v1 and the user-supplied routine load1. Likewise, those at $\tt x 2$ are from the n1=nvar-n2 coefficients v2, using load2. The coefficients v1 and v2 should be stored in a single array v[0..nvar-1] in the main program with v1 in $\mathtt { v } [ 0 \dots \mathrm { n } 2 \AA ^ { - 1 } ]$ and v2 in v[n2..nvar-1].

VecDoub operator() (VecDoub_I &v) {

This is the functor used by newt. It integrates the ODEs to xf using an eighth-order Runge-Kutta method with absolute and relative tolerances atol and rtol, initial stepsize h1, and minimum stepsize hmin. At xf it calls the user-supplied routine score to evaluate the nvar functions f1 and f2 that ought to match at xf. The differences are returned on output. newt uses a globally convergent Newton’s method to adjust the values of v until the differences are zero. A user-supplied function or functor d supplies derivative information to the ODE integrator (see Chapter 17).

VecDoub v2(nvar-n2,&v[n2]); h1=(x2-x1)/100.0; y=load1(x1,v); Path from x1 to xf with best trial values v1. Output out; No output generated by Odeint. Odeint<StepperDopr853<R> $>$ integ1(y,x1,xf,atol,rtol,h1,hmin,out,d); integ1.integrate(); f1=score(xf,y); y=load2(x2,v2); Path from x2 to xf with best trial values v2. Odeint<StepperDopr853<R> $>$ integ2(y,x2,xf,atol,rtol,h1,hmin,out,d); integ2.integrate(); f2=score(xf,y); for (Int $\scriptstyle \dot { 1 } = 0$ ;i<nvar;i++) f1[i] $- =$ f2[i]; return f1; } };

There are boundary value problems where even shooting to a fitting point fails — the integration interval has to be partitioned by several fitting points with the solution being matched at each such point. For more details see [1].

# CITED REFERENCES AND FURTHER READING:

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America).   
Keller, H.B. 1968, Numerical Methods for Two-Point Boundary-Value Problems; reprinted 1991 (New York: Dover).   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 7 . 3 . 5 - \ S 7 . 3 . 6 .$ [1]

# 18.3 Relaxation Methods

In relaxation methods we replace ODEs by approximate finite difference equations (FDEs) on a grid or mesh of points that spans the domain of interest. As a typical example, we could replace a general first-order differential equation

$$
{ \frac { d y } { d x } } = g ( x , y )
$$

with an algebraic equation relating function values at two points $k , k - 1$ :

$$
y _ { k } - y _ { k - 1 } - \left( x _ { k } - x _ { k - 1 } \right) g \left[ { \textstyle { \frac { 1 } { 2 } } } ( x _ { k } + x _ { k - 1 } ) , { \textstyle { \frac { 1 } { 2 } } } ( y _ { k } + y _ { k - 1 } ) \right] = 0
$$

The form of the FDE in (18.3.2) illustrates the idea, but not uniquely: There are many ways to turn the ODE into an FDE. When the problem involves $N$ coupled first-order ODEs represented by FDEs on a mesh of $M$ points, a solution consists of values for $N$ dependent functions given at each of the $M$ mesh points, or $N \times M$ variables in all. The relaxation method determines the solution by starting with a guess and improving it, iteratively. As the iterations improve the solution, the result is said to relax to the true solution.

While several iteration schemes are possible, for most problems our old standby, multidimensional Newton’s method, works well. The method produces a matrix equation that must be solved, but the matrix takes a special, “block diagonal” form that allows it to be inverted far more economically both in time and storage than would be possible for a general matrix of size $( M N ) \times ( M N )$ . Since $M N$ can easily be several thousand or more, this is crucial for the feasibility of the method.

Our implementation couples at most pairs of points, as in equation (18.3.2). More points can be coupled, but then the method becomes more complex. We will provide enough background so that you can write a more general scheme if you have the patience to do so.

Let us develop a general set of algebraic equations that represent the ODEs by FDEs. The ODE problem is exactly identical to that expressed in equations $( 1 8 . 0 . 1 ) - ( 1 8 . 0 . 3 )$ , where we had $N$ coupled first-order equations that satisfy $n _ { 1 }$ boundary conditions at one end of the interval and $n _ { 2 } = N - n _ { 1 }$ boundary conditions at the other. We first define a mesh or grid by a set of $k = 0 , 1 , . . . , M - 1$ points at which we supply values for the independent variable $x _ { k }$ . In particular, $x _ { 0 }$ is the initial boundary and $x _ { M - 1 }$ is the final boundary. We use the notation $\mathbf { y } _ { k }$ to refer to the entire set of dependent variables $y _ { 0 } , y _ { 1 } , \dots , y _ { N - 1 }$ at point $x _ { k }$ . At an arbitrary point $k$ in the middle of the mesh, we approximate the set of $N$ first-order ODEs by algebraic relations of the form

$$
0 = \mathbf { E } _ { k } \equiv \mathbf { y } _ { k } - \mathbf { y } _ { k - 1 } - ( x _ { k } - x _ { k - 1 } ) \mathbf { g } _ { k } ( x _ { k } , x _ { k - 1 } , \mathbf { y } _ { k } , \mathbf { y } _ { k - 1 } ) , k = 1 , 2 , \ldots , M - 1
$$

The notation signifies that $\mathbf { g } _ { k }$ can be evaluated using information from both points $k , k - 1$ The FDEs labeled by $\mathbf { E } _ { k }$ provide $N$ equations coupling $2 N$ variables at points $k , k - 1$ . There

are $M - 1$ points, $k = 1 , 2 , \ldots , M - 1$ , at which difference equations of the form (18.3.3) apply. Thus the FDEs provide a total of $( M - 1 ) N$ equations for the $M N$ unknowns. The remaining $N$ equations come from the boundary conditions.

At the first boundary we have

$$
0 = \mathbf { E } _ { 0 } \equiv \mathbf { B } ( x _ { 0 } , \mathbf { y } _ { 0 } )
$$

while at the second boundary

$$
0 = { \bf E } _ { M } \equiv { \bf C } ( x _ { M - 1 } , { \bf y } _ { M - 1 } )
$$

The vectors $\mathbf { E } _ { 0 }$ and $\mathbf { B }$ have only $n _ { 1 }$ nonzero components, corresponding to the $n _ { 1 }$ boundary conditions at $x _ { 0 }$ . It will turn out to be useful to take these nonzero components to be the last $n _ { 1 }$ components. In other words, $E _ { j , 0 } \neq 0$ only for $j ~ = ~ n _ { 2 } , n _ { 2 } + 1 , \ldots , N - 1$ . At the other boundary, only the first $n _ { 2 }$ components of $\mathbf { E } _ { M }$ and $\mathbf { C }$ are nonzero: $E _ { j , M } \neq 0$ only for $j = 0 , 1 , \ldots , n _ { 2 } - 1$ .

The “solution” of the FDE problem in $( 1 8 . 3 . 3 ) - ( 1 8 . 3 . 5 )$ consists of a set of variables $y _ { j , k }$ , the values of the $N$ variables $y _ { j }$ at the $M$ points $x _ { k }$ . The algorithm we describe below requires an initial guess for the $y _ { j , k }$ . We then determine increments $\Delta y _ { j , k }$ such that $y _ { j , k } +$ $\Delta y _ { j , k }$ is an improved approximation to the solution.

Equations for the increments are developed by expanding the FDEs in first-order Taylor series with respect to small changes $\Delta \mathbf { y } _ { k }$ . At an interior point, $k = 1 , 2 , \ldots , M - 1$ , this gives

$$
\mathbf { E } _ { k } ( \mathbf { y } _ { k } + \Delta \mathbf { y } _ { k } , \mathbf { y } _ { k - 1 } + \Delta \mathbf { y } _ { k - 1 } ) \approx \mathbf { E } _ { k } ( \mathbf { y } _ { k } , \mathbf { y } _ { k - 1 } ) + \sum _ { n = 0 } ^ { N - 1 } { \frac { \partial \mathbf { E } _ { k } } { \partial y _ { n , k - 1 } } } \Delta y _ { n , k - 1 } + \sum _ { n = 0 } ^ { N - 1 } { \frac { \partial \mathbf { E } _ { k } } { \partial y _ { n , k } } } \Delta y _ { n , k - 1 } .
$$

For a solution we want the updated value $\mathbf { E } ( \mathbf { y } + \Delta \mathbf { y } )$ to be zero, so the general set of equations at an interior point can be written in matrix form as

$$
\sum _ { n = 0 } ^ { N - 1 } S _ { j , n } \Delta y _ { n , k - 1 } + \sum _ { n = N } ^ { 2 N - 1 } S _ { j , n } \Delta y _ { n - N , k } = - E _ { j , k } , \quad j = 0 , 1 , \ldots , N - 1
$$

where

$$
S _ { j , n } = \frac { \partial E _ { j , k } } { \partial y _ { n , k - 1 } } , S _ { j , n + N } = \frac { \partial E _ { j , k } } { \partial y _ { n , k } } , n = 0 , 1 , \ldots , N - 1
$$

The quantity $S _ { j , n }$ is an $N \times 2 N$ matrix at each point $k$ . Each interior point thus supplies a block of $N$ equations coupling $2 N$ corrections to the solution variables at the points $k , k - 1$ .

Similarly, the algebraic relations at the boundaries can be expanded in a first-order Taylor series for increments that improve the solution. Since $\mathbf { E } _ { 0 }$ depends only on $\mathbf { y } _ { 0 }$ , we find at the first boundary

$$
\sum _ { n = 0 } ^ { N - 1 } S _ { j , n } \Delta y _ { n , 0 } = - E _ { j , 0 } , \quad j = n _ { 2 } , n _ { 2 } + 1 , \dots , N - 1
$$

where

$$
S _ { j , n } = \frac { \partial E _ { j , 0 } } { \partial y _ { n , 0 } } , \quad n = 0 , 1 , \ldots , N - 1
$$

At the second boundary,

$$
\sum _ { n = 0 } ^ { N - 1 } S _ { j , n } \Delta y _ { n , M - 1 } = - E _ { j , M } , \quad j = 0 , 1 , \ldots , n _ { 2 } - 1
$$

where

$$
S _ { j , n } = \frac { \partial E _ { j , M } } { \partial y _ { n , M - 1 } } , \quad n = 0 , 1 , \ldots , N - 1
$$

![](images/5412fcf8dff9c46c0b217aeb42c3ef963c305d76c6127bf6319c7b76b08b470f.jpg)  
Figure 18.3.1. Matrix structure of a set of linear finite difference equations (FDEs) with boundary conditions imposed at both endpoints. Here $\mathbf { X }$ represents a coefficient of the FDEs, V represents a component of the unknown solution vector, and B is a component of the known right-hand side. Empty spaces represent zeros. The matrix equation is to be solved by a special form of Gaussian elimination. (See text for details.)

We thus have in equations $( 1 8 . 3 . 7 ) - ( 1 8 . 3 . 1 2 )$ a set of linear equations to be solved for the corrections $\Delta \mathbf { y }$ , iterating until the corrections are sufficiently small. The equations have a special structure, because each $S _ { j , n }$ couples only points $k , k - 1$ . Figure 18.3.1 illustrates the typical structure of the complete matrix equation for the case of five variables and four mesh points, with three boundary conditions at the first boundary and two at the second. The $3 \times 5$ block of nonzero entries in the top left-hand corner of the matrix comes from the boundary condition $S _ { j , n }$ at point $k \ = \ 0$ . The next three $5 \times 1 0$ blocks are the $S _ { j , n }$ at the interior points, coupling variables at mesh points (2,1), (3,2), and (4,3). Finally we have the block corresponding to the second boundary condition.

We can solve equations $( 1 8 . 3 . 7 ) \mathrm { ~ - ~ } ( 1 8 . 3 . 1 2 )$ for the increments $\Delta \mathbf { y }$ using a form of Gaussian elimination that exploits the special structure of the matrix to minimize the total number of operations, and that minimizes storage of matrix coefficients by packing the elements in a special blocked structure. (You might wish to review Chapter 2, especially $\ S 2 . 2$ , if you are unfamiliar with the steps involved in Gaussian elimination.) Recall that Gaussian elimination consists of manipulating the equations by elementary operations such as dividing rows of coefficients by a common factor to produce unity in diagonal elements, and adding appropriate multiples of other rows to produce zeros below the diagonal. Here we take advantage of the block structure by performing a bit more reduction than in pure Gaussian elimination, so that the storage of coefficients is minimized. Figure 18.3.2 shows the form that we wish to achieve by elimination, just prior to the backsubstitution step. Only a small subset of the reduced $M N \times M N$ matrix elements needs to be stored as the elimination progresses. Once the matrix elements reach the stage in Figure 18.3.2, the solution follows quickly by a backsubstitution procedure.

Furthermore, the entire procedure, except the backsubstitution step, operates only on one block of the matrix at a time. The procedure contains four types of operations: (1) partial reduction to zero of certain elements of a block using results from a previous step; (2) elimination of the square structure of the remaining block elements such that the square section contains unity along the diagonal, and zero in off-diagonal elements; (3) storage of the

![](images/c7a59aa34bc9bec1338be88b6bd92855d84aa8fba30894ff6d2a560837a58fb7.jpg)  
Figure 18.3.2. Target structure of the Gaussian elimination. Once the matrix of Figure 18.3.1 has been reduced to this form, the solution follows quickly by backsubstitution.

$$
{ \begin{array} { r l } { ( { \mathrm { a } } ) ~ { \mathrm { ~ D ~ D ~ D ~ A ~ A ~ } } \qquad } & { { \mathrm { ~ V ~ } } \qquad { \mathrm { A } } } \\ { { \mathrm { ~ D ~ D ~ D ~ A ~ A ~ } } \qquad } & { { \mathrm { ~ V ~ } } \qquad { \mathrm { A } } } \\ { { \mathrm { ~ D ~ D ~ D ~ A ~ A ~ } } \qquad } & { { \mathrm { ~ V ~ } } \qquad { \mathrm { A } } } \\ { } & { { \mathrm { ~ V ~ } } \qquad { \mathrm { ~ A } } } \\ { ( { \mathrm { b } } ) ~ 1 ~ 0 ~ 0 ~ { \mathrm { ~ S ~ S ~ } } \qquad } & { { \mathrm { ~ V ~ } } \qquad { \mathrm { S } } } \\ { } & { { \mathrm { ~ 0 ~ 1 ~ 0 ~ S ~ S ~ } } \qquad { \mathrm { ~ V ~ } } \qquad { \mathrm { S } } } \\ { } & { { \mathrm { ~ 0 ~ 0 ~ 1 ~ 5 ~ S ~ } } \qquad { \mathrm { ~ V ~ } } \qquad { \mathrm { S } } } \end{array} }
$$

Figure 18.3.3. Reduction process for the first (upper-left) block of the matrix in Figure 18.3.1. (a) Original form of the block, (b) final form. (See text for explanation.)

remaining nonzero coefficients for use in later steps; and (4) backsubstitution. We illustrate the steps schematically by figures.

Consider the block of equations describing corrections available from the initial boundary conditions. We have $n _ { 1 }$ equations for $N$ unknown corrections. We wish to transform the first block so that its left-hand $n _ { 1 } \times n _ { 1 }$ square section becomes unity along the diagonal and zero in off-diagonal elements. Figure 18.3.3 shows the original and final forms of the first block of the matrix. In the figure we designate matrix elements that are subject to diagonalization by “D” and elements that will be altered by “A”; in the final block, elements that are stored are labeled by “S.” We get from start to finish by selecting in turn $n _ { 1 }$ “pivot” elements from among the first $n _ { 1 }$ columns, normalizing the pivot row so that the value of the “pivot” element is unity, and adding appropriate multiples of this row to the remaining rows so that they contain zeros in the pivot column. In its final form, the reduced block expresses values for the corrections to the first $n _ { 1 }$ variables at mesh point 0 in terms of values for the remaining $n _ { 2 }$ unknown corrections at point 0, i.e., we now know what the first $n _ { 1 }$ elements are in terms of the remaining $_ { n _ { 2 } }$ elements. We store only the final set of $_ { n _ { 2 } }$ nonzero columns from the initial block, plus the column for the altered right-hand side of the matrix equation.

We must emphasize here an important detail of the method. To exploit the reduced storage allowed by operating on blocks, it is essential that the ordering of columns in the s matrix of derivatives be such that pivot elements can be found among the first $n _ { 1 }$ rows of the matrix. This means that the $n _ { 1 }$ boundary conditions at the first point must contain some dependence on the first $\mathbf { j } { = } 0 , 1 , \ldots , { } n _ { 1 } - 1$ dependent variables, y[j][0]. If not, then the original square $n _ { 1 } \times n _ { 1 }$ subsection of the first block will appear to be singular, and the method will fail. Alternatively, we would have to allow the search for pivot elements to involve all $N$ columns of the block, and this would require column swapping and far more bookkeeping. The code provides a simple method of reordering the variables, i.e., the columns of the s matrix, so that this can be done easily. End of important detail.

![](images/c2f4c981a4b2d6e126f7e31f3f27ecfc940271c9320b144c1dc3a5453054b8a9.jpg)  
Figure 18.3.4. Reduction process for intermediate blocks of the matrix in Figure 18.3.1. (a) Original form, (b) final form. (See text for explanation.)

Next consider the block of $N$ equations representing the FDEs that describe the relation between the $2 N$ corrections at points 1 and 0. The elements of that block, together with results from the previous step, are illustrated in Figure 18.3.4. Note that by adding suitable multiples of rows from the first block we can reduce to zero the first $n _ { 1 }$ columns of the block (labeled by $\because \angle ^ { \dag }$ ), and, to do so, we will need to alter only the columns from $n _ { 1 }$ to $N - 1$ and the vector element on the right-hand side. Of the remaining columns we can diagonalize a square subsection of $N \times N$ elements, labeled by “D” in the figure. In the process we alter the final set of $n _ { 2 }$ columns, denoted “A” in the figure. The second half of the figure shows the block when we finish operating on it, with the stored $n _ { 2 } \times N$ elements labeled by “S.”

If we operate on the next set of equations corresponding to the FDEs coupling corrections at points 2 and 1, we see that the state of available results and new equations exactly reproduces the situation described in the previous paragraph. Thus, we can carry out those steps again for each block in turn through block $M - 1$ . Finally on block $M$ we encounter the remaining boundary conditions.

Figure 18.3.5 shows the final block of $n _ { 2 }$ FDEs relating the $N$ corrections for variables at mesh point $M - 1$ , together with the result of reducing the previous block. Again, we can first use the prior results to zero the first $n _ { 1 }$ columns of the block. Now, when we diagonalize the remaining square section, we strike gold: We get values for the final $n _ { 2 }$ corrections at mesh point $M - 1$ .

With the final block reduced, the matrix has the desired form shown previously in Figure 18.3.2, and the matrix is ripe for backsubstitution. Starting with the bottom row and working up toward the top, at each stage we can simply determine one unknown correction in terms of known quantities.

The object Solvde organizes the steps described above. The principal procedures used in the algorithm are performed by functions called internally by Solvde. The function red eliminates leading columns of the s matrix using results from prior blocks. pinvs diagonalizes the square subsection of s and stores unreduced coefficients. bksub carries out the backsubstitution step. The user of Solvde must understand the calling arguments, as described below, and supply an object Difeq, called by Solvde, with a method smatrix that evaluates the s matrix for each block.

![](images/f9500ac9b93850c6d4662973321d3941f92f02418834ac8dd69d87c47673a222.jpg)  
Figure 18.3.5. Reduction process for the last (lower-right) block of the matrix in Figure 18.3.1. (a) Original form, (b) final form. (See text for explanation.)

Most of the arguments in the constructor call to Solvde have already been described, but some require discussion. On input, array y[j][k] contains the initial guess for the solution, with $\dot { \mathsf { J } }$ labeling the dependent variables at mesh points $\mathtt { k }$ . The problem involves ne FDEs spanning points $\mathtt { k } = 0$ ,..., $\mathtt { m } - 1$ . nb boundary conditions apply at the first point $\mathtt { k } = 0$ . The array indexv[j] establishes the correspondence between columns of the s matrix; equations (18.3.8), (18.3.10), and (18.3.12); and the dependent variables. As described above, it is essential that the nb boundary conditions at $\mathtt { k } = 0$ involve the dependent variables referenced by the first nb columns of the s matrix. Thus, columns $\dot { ] }$ of the s matrix can be ordered by the user in Difeq to refer to derivatives with respect to the dependent variable indexv[j].

The function only attempts itmax correction cycles before returning, even if the solution has not converged. The parameters conv, slowc, and scalv relate to convergence. Each inversion of the matrix produces corrections for ne variables at m mesh points. We want these to become vanishingly small as the iterations proceed, but we must define a measure for the size of corrections. This error “norm” is very problem-specific, so the user might wish to rewrite this section of the code as appropriate. In the program below we compute a value for the average correction err by summing the absolute value of all corrections, weighted by a scale factor appropriate to each type of variable:

$$
\mathsf { e r r } = \frac { 1 } { \mathrm { m \times n e } } \sum _ { \mathrm { k } = 0 } ^ { \mathrm { m - 1 } } \sum _ { \mathrm { j } = 0 } ^ { \mathrm { n e - 1 } } \frac { \left| \Delta Y \left[ \mathrm { j } \right] \left[ \mathrm { k } \right] \right| } { \mathrm { s c a l v } \left[ \mathrm { j } \right] }
$$

When err $\leq$ conv, the method has converged. Note that the user gets to supply an array scalv that measures the typical size of each variable.

Obviously, if err is large, we are far from a solution, and perhaps it is a bad idea to believe that the corrections generated from a first-order Taylor series are accurate. The number slowc modulates the application of corrections. After each iteration we apply only a fraction of the corrections found by matrix inversion:

$$
Y [ \mathbf { j } ] [ \mathbf { k } ]  Y [ \mathbf { j } ] [ \mathbf { k } ] + \frac { \mathsf { s l o w c } } { \mathsf { m a x } ( \mathbf { s l o w c , e r r } ) } \Delta Y [ \mathbf { j } ] [ \mathbf { k } ]
$$

Thus, when ${ \tt e r r } >$ slowc only a fraction of the corrections are used, but when err $\leq$ slowc the entire correction gets applied.

As already mentioned, the constructor initializes the array $\mathtt { y } [ 0 \AA \cdot \cdot \mathrm { n e } \mathrm { - } 1 ] \ [ 0 \AA \cdot \cdot \mathrm { m } \mathrm { - } 1 ]$ in Solvde with the trial solution. Internally, workspace arrays $\mathsf { c } \left[ 0 \ldots \mathsf { n e } \mathrm { - 1 } \right] \left[ 0 \ldots \mathsf { n e } \mathrm { - n b } \right] \left[ 0 \ldots \mathsf { m } \right]$ , $\mathbf { s } \left[ 0 , . . \mathrm { n e } { - } 1 \right] \left[ 0 . . 2 \ast \mathrm { n e } \right]$ are allocated. The array $^ \texttt { c }$ is the blockbuster: It stores the unreduced elements of the matrix built up for the backsubstitution step. If there are m mesh points, then there will be $\mathtt { m } + 1$ blocks, each requiring ne rows and $\mathtt { n e - n b + 1 }$ columns. Although large, this is small compared with $( \mathtt { n e } \times \mathtt { m } ) ^ { 2 }$ elements required for the whole matrix if we did not break it into blocks.

We now describe the workings of the user-supplied object Difeq. The constructor can be used to pass problem-specific information from your main program. The object must contain a method smatrix with the following declaration:

void smatrix(const Int k, const Int k1, const Int k2, const Int jsf, const Int is1, const Int isf, VecInt_I &indexv, MatDoub_O &s, MatDoub_I &y);

As the declaration shows, the only information passed from Difeq to Solvde is the matrix of derivatives $\mathbf { s } \left[ 0 , . . \mathrm { n e } { - } 1 \right] \left[ 0 . . 2 \ast \mathrm { n e } \right]$ ; all other arguments are input to smatrix and should not be altered. k indicates the current mesh point, or block number. k1, k2 label the first and last points in the mesh. If $\mathrm { ~ \bf ~ k ~ } = \mathrm { ~ \bf ~ k 1 ~ }$ or $\texttt { k } > \texttt { k } 2$ , the block involves the boundary conditions at the first or final point; otherwise the block acts on FDEs coupling variables at points $\mathtt { k } { - } 1$ , k.

The convention on storing information into the array s[i][j] follows that used in equations (18.3.8), (18.3.10), and (18.3.12): Rows i label equations and columns $\dot { \mathsf { J } }$ refer to derivatives with respect to dependent variables in the solution. Recall that each equation will depend on the ne dependent variables at either one or two points. Thus, $\dot { ] }$ runs from 0 to either ne-1 or $2 { \ast } \mathtt { n e - 1 }$ . The column ordering for dependent variables at each point must agree with the list supplied in indexv[j]. Thus, for a block not at a boundary, the first column multiplies $\Delta Y ( \mathrm { 1 = i n d e x v } \left[ 0 \right] , \mathrm { k - 1 } )$ , and the column ne multiplies $\Delta Y ( \tt { 1 } \mathrm { { = } i n d e x v [ 0 ] , k ) }$ . The parameters is1, isf give the numbers of the starting and final rows that need to be filled in the s matrix for this block. jsf labels the column in which the difference equations $E _ { j , k }$ of equations $( 1 8 . 3 . 3 ) - ( 1 8 . 3 . 5 )$ are stored. Thus, s[i][jsf] is the vector on the right-hand side of the matrix. The reason for the minus sign is that smatrix supplies the actual difference equation, $E _ { j , k }$ , not its negative. Note that Solvde supplies a value for jsf such that the difference equation is put in the column just after all derivatives in the s matrix. Thus, smatrix expects to find values entered into s[i][j] for rows $\mathbf { i s } 1 \leq \mathbf { i } \leq$ isf and $0 \leq \mathrm { j } \leq \mathrm { j } \mathbf { s } \mathbf { f }$ .

Finally, the quantities $\mathbf { s } \left[ 0 . \mathbf { \nabla } . \mathtt { n s i - 1 } \right] \left[ 0 . \mathbf { \nabla } . \mathtt { n s j - 1 } \right]$ and $\mathtt { y } [ 0 \mathrm { . . n y j - 1 } ] [ 0 \mathrm { . . n y k - 1 } ]$ sup ply smatrix with storage for s and the values of the solution variables y for this iteration. An example of how to use this routine is given in the next section.

Detailed implementing code for Solvde is given in a Webnote [1], many ideas in which are due to Eggleton [2].

# 18.3.1 “Algebraically Difficult" Sets of Differential Equations

Relaxation methods allow you to take advantage of an additional opportunity that, while not obvious, can speed up some calculations enormously. It is not necessary that the set of variables $\underline { { y } } _ { j , k }$ correspond exactly with the dependent variables of the original differential equations. They can be related to those variables through algebraic equations. Obviously, it is necessary only that the solution variables allow us to evaluate the functions $y , g , \mathbf { B } , \mathbf { C }$ that are used to construct the FDEs from the ODEs. In some problems, $g$ depends on functions of $y$ that are known only implicitly, so that iterative solutions are necessary to evaluate functions in the ODEs. Often one can dispense with this “internal” nonlinear problem by defining a new set of variables from which both $y , g$ and the boundary conditions can be obtained directly. A typical example occurs in physical problems where the equations require the solution of a complex equation of state that can be expressed in more convenient terms using variables other than the original dependent variables in the ODE. While this approach is analogous to performing an analytic change of variables directly on the original ODEs, such an analytic transformation might be prohibitively complicated. The change of variables in the relaxation method is easy and requires no analytic manipulations.

# CITED REFERENCES AND FURTHER READING:

Numerical Recipes Software 2007, “Solvde Implementation,” Numerical Recipes Webnote No. 25, at http://www.nr.com/webnotes?25 [1]   
Eggleton, P.P. 1971, “The Evolution of Low Mass Stars,” Monthly Notices of the Royal Astronomical Society,vol. 151,pp.351-364.[2]   
Keller, H.B. 1968, Numerical Methods for Two-Point Boundary-Value Problems; reprinted 1991 (New York: Dover).   
Kippenhan, R., Weigert, A., and Hofmeister, E. 1968, in Methods in Computational Physics, vol. 7 (New York: Academic Press), pp. 129ff.

# 18.4 A Worked Example: Spheroidal Harmonics

The best way to understand the algorithms of the previous sections is to see them employed to solve an actual problem. As a sample problem, we have selected the computation of spheroidal harmonics. (The more common name is spheroidal angle functions, but we prefer the explicit reminder of the kinship with spherical harmonics.) We will show how to find spheroidal harmonics, first by the method of relaxation (-18.3), and then by the methods of shooting (-18.1) and shooting to a fitting point (-18.2).

Spheroidal harmonics typically arise when certain partial differential equations are solved by separation of variables in spheroidal coordinates. They satisfy the following differential equation on the interval $- 1 \leq x \leq 1$ :

$$
\frac { d } { d x } \left[ ( 1 - x ^ { 2 } ) \frac { d S } { d x } \right] + \left( \lambda - c ^ { 2 } x ^ { 2 } - \frac { m ^ { 2 } } { 1 - x ^ { 2 } } \right) S = 0
$$

Here $m$ is an integer, $c$ is the “oblateness parameter,” and $\lambda$ is the eigenvalue. Despite the notation, $c ^ { 2 }$ can be positive or negative. For $c ^ { 2 } > 0$ , the functions are called “prolate,” while if $c ^ { 2 } < 0$ they are called “oblate.” The equation has singular points at $x = \pm 1$ and is to be solved subject to the boundary conditions that the solution be regular at $x = \pm 1$ . Only for certain values of $\lambda$ , the eigenvalues, will this be possible.

If we consider first the spherical case, where $c \ = \ 0$ , we recognize the differential equation for Legendre functions $P _ { n } ^ { m } ( x )$ . In this case the eigenvalues are $\lambda _ { m n } = n ( n + 1 )$ , $n = m , m + 1 , \ldots$ The integer $n$ labels successive eigenvalues for fixed $m$ : When $n = m$ we have the lowest eigenvalue, and the corresponding eigenfunction has no nodes in the interval $- 1 < x < 1$ ; when $n = m + 1$ we have the next eigenvalue, and the eigenfunction has one node inside $( - 1 , 1 )$ ; and so on.

A similar situation holds for the general case $c ^ { 2 } \neq 0$ . We write the eigenvalues of (18.4.1) as $\lambda _ { m n } ( c )$ and the eigenfunctions as $S _ { m n } ( x ; c )$ . For fixed $m , n = m , m +$ $1 , \ldots$ labels the successive eigenvalues.

The computation of $\lambda _ { m n } ( c )$ and $S _ { m n } ( x ; c )$ traditionally has been quite difficult. Complicated recurrence relations, power series expansions, etc., can be found in [1-3]. Cheap computing makes evaluation by direct solution of the differential equation quite feasible.

The first step is to investigate the behavior of the solution near the singular points $x = \pm 1$ . Substituting a power series expansion of the form

$$
S = ( 1 \pm x ) ^ { \alpha } \sum _ { k = 0 } ^ { \infty } a _ { k } ( 1 \pm x ) ^ { k }
$$

in equation (18.4.1), we find that the regular solution has $\alpha = m / 2$ . (Without loss of generality we can take $m \geq 0$ since $m  - m$ is a symmetry of the equation.) We get an equation that is numerically more tractable if we factor out this behavior. Accordingly we set

$$
S = ( 1 - x ^ { 2 } ) ^ { m / 2 } y
$$

We then find from (18.4.1) that $y$ satisfies the equation

$$
( 1 - x ^ { 2 } ) { \frac { d ^ { 2 } y } { d x ^ { 2 } } } - 2 ( m + 1 ) x { \frac { d y } { d x } } + ( \mu - c ^ { 2 } x ^ { 2 } ) y = 0
$$

where

$$
\mu \equiv \lambda - m ( m + 1 )
$$

Both equations (18.4.1) and (18.4.4) are invariant under the replacement $x $ $- x$ . Thus the functions $S$ and $y$ must also be invariant, except possibly for an overall scale factor. (Since the equations are linear, a constant multiple of a solution is also a solution.) Because the solutions will be normalized, the scale factor can only be $\pm 1$ . If $n - m$ is odd, there are an odd number of zeros in the interval $( - 1 , 1 )$ . Thus we must choose the antisymmetric solution $y ( - x ) = - y ( x )$ , which has a zero at $x = 0$ . Conversely, if $n - m$ is even, we must have the symmetric solution. Thus

$$
y _ { m n } ( - x ) = ( - 1 ) ^ { n - m } y _ { m n } ( x )
$$

and similarly for $S _ { m n }$

The boundary conditions on (18.4.4) require that $y$ be regular at $x = \pm 1$ . In other words, near the endpoints the solution takes the form

$$
y = a _ { 0 } + a _ { 1 } ( 1 - x ^ { 2 } ) + a _ { 2 } ( 1 - x ^ { 2 } ) ^ { 2 } + \cdots
$$

Substituting this expansion in equation (18.4.4) and letting $x \to 1$ , we find that

$$
a _ { 1 } = - \frac { \mu - c ^ { 2 } } { 4 ( m + 1 ) } a _ { 0 }
$$

Equivalently,

$$
y ^ { \prime } ( 1 ) = \frac { \mu - c ^ { 2 } } { 2 ( m + 1 ) } y ( 1 )
$$

A similar equation holds at $x \ = \ - 1$ with a minus sign on the right-hand side. The irregular solution has a different relation between function and derivative at the endpoints.

Instead of integrating the equation from $^ { - 1 }$ to 1, we can exploit the symmetry (18.4.6) to integrate from 0 to 1. The boundary condition at $x = 0$ is

$$
\begin{array} { l l } { { y ( 0 ) = 0 , } } & { { n - m \mathrm { ~ o d d } } } \\ { { y ^ { \prime } ( 0 ) = 0 , } } & { { n - m \mathrm { ~ e v e n } } } \end{array}
$$

A third boundary condition comes from the fact that any constant multiple of a solution $y$ is a solution. We can thus normalize the solution. We adopt the normalization that the function $S _ { m n }$ has the same limiting behavior as $P _ { n } ^ { m }$ at $x = 1$ :

$$
\operatorname * { l i m } _ { x \to 1 } ( 1 - x ^ { 2 } ) ^ { - m / 2 } S _ { m n } ( x ; c ) = \operatorname * { l i m } _ { x \to 1 } ( 1 - x ^ { 2 } ) ^ { - m / 2 } P _ { n } ^ { m } ( x )
$$

Various normalization conventions in the literature are tabulated by Flammer [1].

Imposing three boundary conditions for the second-order equation (18.4.4) turns it into an eigenvalue problem for $\lambda$ or equivalently for $\mu$ . We write it in the standard form by setting

$$
\begin{array} { r } { y _ { 0 } = y } \\ { y _ { 1 } = y ^ { \prime } } \\ { y _ { 2 } = \mu } \end{array}
$$

Then

$$
\begin{array} { l } { { y _ { 0 } ^ { \prime } = y _ { 1 } } } \\ { { y _ { 1 } ^ { \prime } = \displaystyle \frac { 1 } { 1 - x ^ { 2 } } \left[ 2 x ( m + 1 ) y _ { 1 } - ( y _ { 2 } - c ^ { 2 } x ^ { 2 } ) y _ { 0 } \right] } } \\ { { y _ { 2 } ^ { \prime } = 0 } } \end{array}
$$

The boundary condition at $x = 0$ in this notation is

$$
\begin{array} { l l } { { y _ { 0 } = 0 , } } & { { n - m \mathrm { o d d } } } \\ { { y _ { 1 } = 0 , } } & { { n - m \mathrm { e v e n } } } \end{array}
$$

At $x = 1$ we have two conditions:

$$
\begin{array} { l } { \displaystyle { y _ { 1 } = \frac { y _ { 2 } - c ^ { 2 } } { 2 ( m + 1 ) } y _ { 0 } } } \\ { \displaystyle { y _ { 0 } = \operatorname* { l i m } _ { x \to 1 } ( 1 - x ^ { 2 } ) ^ { - m / 2 } P _ { n } ^ { m } ( x ) = \frac { ( - 1 ) ^ { m } ( n + m ) ! } { 2 ^ { m } m ! ( n - m ) ! } \equiv \gamma } } \end{array}
$$

We are now ready to illustrate the use of the methods of previous sections on this problem.

# 18.4.1 Relaxation

If we just want a few isolated values of $\lambda$ or $S$ , shooting is probably the quickest method. However, if we want values for a large sequence of values of $c$ , relaxation is better. Relaxation rewards a good initial guess with rapid convergence, and the previous solution should be a good initial guess if $c$ is changed only slightly.

For simplicity, we choose a uniform grid on the interval $0 \leq x \leq 1$ . For a total of $M$ mesh points, we have

$$
\begin{array} { l } { \displaystyle { h = \frac { 1 } { M - 1 } } } \\ { \displaystyle { x _ { k } = k h , \quad k = 0 , 1 , \ldots , M - 1 } } \end{array}
$$

At interior points $k = 1 , 2 , \ldots , M - 1$ , equation (18.4.15) gives

$$
E _ { 0 , k } = y _ { 0 , k } - y _ { 0 , k - 1 } - { \frac { h } { 2 } } ( y _ { 1 , k } + y _ { 1 , k - 1 } )
$$

Equation (18.4.16) gives

$$
\begin{array} { l } { E _ { 1 , k } = y _ { 1 , k } - y _ { 1 , k - 1 } - \beta _ { k } } \\ { \times \left[ \frac { ( x _ { k } + x _ { k - 1 } ) ( m + 1 ) ( y _ { 1 , k } + y _ { 1 , k - 1 } ) } { 2 } - \alpha _ { k } \frac { ( y _ { 0 , k } + y _ { 0 , k - 1 } ) } { 2 } \right] } \end{array}
$$

where

$$
\begin{array} { l } { \displaystyle \alpha _ { k } = \frac { y _ { 2 , k } + y _ { 2 , k - 1 } } { 2 } - \frac { c ^ { 2 } ( x _ { k } + x _ { k - 1 } ) ^ { 2 } } { 4 } } \\ { \displaystyle \beta _ { k } = \frac { h } { 1 - \frac { 1 } { 4 } ( x _ { k } + x _ { k - 1 } ) ^ { 2 } } } \end{array}
$$

Finally, equation (18.4.17) gives

$$
E _ { 2 , k } = y _ { 2 , k } - y _ { 2 , k - 1 }
$$

Now recall that the matrix of partial derivatives $S _ { i , j }$ of equation (18.3.8) is defined so that $i$ labels the equation and $j$ the variable. In our case, $j$ runs from 0 to 2 for $y _ { j }$ at $k - 1$ and from 3 to 5 for $y _ { j }$ at $k$ . Thus equation (18.4.23) gives

$$
\begin{array} { l l l } { { S _ { 0 , 0 } = - 1 , \quad } } & { { S _ { 0 , 1 } = - \displaystyle \frac { h } { 2 } , \quad } } & { { S _ { 0 , 2 } = 0 } } \\ { { \mathrm { } } } & { { \mathrm { } } } & { { S _ { 0 , 3 } = 1 , \quad \quad S _ { 0 , 4 } = - \displaystyle \frac { h } { 2 } , \quad \quad S _ { 0 , 5 } = 0 } } \end{array}
$$

Similarly equation (18.4.24) yields

$$
\begin{array} { l l } { { S _ { 1 , 0 } = \alpha _ { k } \beta _ { k } / 2 , ~ } } & { { S _ { 1 , 1 } = - 1 - \beta _ { k } ( x _ { k } + x _ { k - 1 } ) ( m + 1 ) / 2 , } } \\ { { S _ { 1 , 2 } = \beta _ { k } ( y _ { 0 , k } + y _ { 0 , k - 1 } ) / 4 , ~ } } & { { S _ { 1 , 3 } = S _ { 1 , 0 } , } } \\ { { S _ { 1 , 4 } = 2 + S _ { 1 , 1 } , ~ } } & { { S _ { 1 , 5 } = S _ { 1 , 2 } } } \end{array}
$$

while from equation (18.4.27) we find

$$
\begin{array} { l l } { { S _ { 2 , 0 } = 0 , \quad } } & { { S _ { 2 , 1 } = 0 , \quad \quad S _ { 2 , 2 } = - 1 } } \\ { { S _ { 2 , 3 } = 0 , \quad } } & { { S _ { 2 , 4 } = 0 , \quad \quad S _ { 2 , 5 } = 1 } } \end{array}
$$

At $x = 0$ we have the boundary condition

$$
E _ { 2 , 0 } = \left\{ { { y _ { 0 , 0 } } , \begin{array} { l l } { { n - m \mathrm { { \ o d d } } } } \\ { { { y _ { 1 , 0 } } , } } \end{array} } \right.
$$

Recall the convention adopted in the solvde routine that for one boundary condition at $k = 0$ only $S _ { 2 , j }$ can be nonzero. Also, $j$ takes on the values 3 to 5 since the boundary condition involves only $y _ { k }$ , not $y _ { k - 1 }$ . Accordingly, the only nonzero values of $S _ { 2 , j }$ at $x = 0$ are

$$
\begin{array} { l l } { { S _ { 2 , 3 } = 1 , \quad } } & { { n - m \mathrm { ~ o d d } } } \\ { { S _ { 2 , 4 } = 1 , \quad } } & { { n - m \mathrm { ~ e v e n } } } \end{array}
$$

At $x = 1$ we have

$$
\begin{array} { l l } { { E _ { 0 , M } = y _ { 1 , M - 1 } - \displaystyle \frac { y _ { 2 , M - 1 } - c ^ { 2 } } { 2 ( m + 1 ) } y _ { 0 , M - 1 } } } \\ { { E _ { 1 , M } = y _ { 0 , M - 1 } - \gamma } } \end{array}
$$

Thus

$$
\begin{array} { l l l } { { S _ { 0 , 3 } = - { \frac { y _ { 2 , M - 1 } - c ^ { 2 } } { 2 ( m + 1 ) } } , \quad } } & { { S _ { 0 , 4 } = 1 , \quad } } & { { S _ { 0 , 5 } = - { \frac { y _ { 0 , M - 1 } } { 2 ( m + 1 ) } } } } \\ { { S _ { 1 , 3 } = 1 , \quad } } & { { S _ { 1 , 4 } = 0 , \quad } } & { { S _ { 1 , 5 } = 0 } } \end{array}
$$

Here now is the sample program that implements the above algorithm. We need a main program, sfroid, that calls the routine Solvde, and we must supply the object Difeq to be passed to Solvde. For simplicity we choose an equally spaced mesh of $\mathtt { m } = 4 1$ points, that is, $h = . 0 2 5$ . As we shall see, this gives good accuracy for the eigenvalues up to moderate values of $n - m$ .

Since the boundary condition at $x = 0$ does not involve $y _ { 0 }$ if $n - m$ is even, we have to use the indexv feature of Solvde. Recall that the value of indexv[j] describes which column of s[i][j] the variable y[j] has been put in. If $n - m$ is even, we need to interchange the columns for $y _ { 0 }$ and $y _ { 1 }$ so that there is not a zero pivot element in s[i][j].

The program prompts for values of $m$ and $n$ . It then computes an initial guess for $y$ based on the Legendre function $P _ { n } ^ { m }$ . It next prompts for $c ^ { 2 }$ , solves for $y$ , prompts for $c ^ { 2 }$ , solves for $y$ using the previous values as an initial guess, and so on.

Int main_sfroid(void)   
Sample program using Solvde. Computes eigenvalues of spheroidal harmonics $S _ { m n } ( x ; c )$ for $m \geq 0$ and $n \geq m$ . In the program, $m$ is mm, ${ \overset { \smile } { c } } ^ { 2 }$ is $^ { c 2 }$ , and $\gamma$ of equation (18.4.20) is anorm. {   
const Int M=40,MM=4;   
const Int NE=3,NB $\scriptstyle = 1$ ,NYJ $\mathop { : = }$ NE,NYK=M+1;   
Int mm=3, $_ { \mathrm { 2 } } = 5$ ,mpt=M+1;   
VecInt indexv(NE);   
VecDoub x(M+1),scalv(NE);   
MatDoub y(NYJ,NYK);   
Int itmax $\mathtt { \Pi } = 1 0 0$ ;   
Doub c2[] $=$ {16.0,20.0,-16.0,-20.0};   
Doub conv $= 1$ .0e-14,slowc $= 1$ .0, $\scriptstyle 1 = 1$ .0/M;   
if ((n+mm & 1) $\ ! = \ 0$ ) { No interchanges necessary. indexv[0] ${ = } 0$ ; indexv[1] $= 1$ ; indexv[2] $^ { = 2 }$ ;   
} else { Interchange $y _ { 0 }$ and $y _ { 1 }$ . indexv[0] $= 1$ ; indexv[1] ${ = } 0$ ; indexv[2] $^ { = 2 }$ ;   
1   
Doub anorm $^ { = 1 }$ .0; Compute .   
if (mm $\ ! = \ 0$ ) { Doub $\mathtt { q 1 } = \mathtt { n }$ ; for (Int $\bf { i } \mathrm { = } 1 ; \bf { i } \mathrm { < = } \mathrm { m m ; \bf { i } \mathrm { + + } } ) ~ \mathrm { a n o r m ~ \bf { = ~ } } - 0 . 5 \mathrm { * } \mathrm { a n o r m * ( n \mathrm { + + } ) * ( q 1 \mathrm { - - } / \bf { i } ) ; }$   
for (Int $\mathtt { k } = 0$ ;k<M;k++) { Initial guess. x[k] $=$ k\*h; Doub fac $_ { \lfloor = 1 }$ .0-x[k] $^ { * \mathrm { x } }$ [k]; Doub fac2 $: = .$ exp((-mm/2.0)\*log(fac1));

y[0][k] $=$ plgndr(n,mm,x[k])\*fac2; $P _ { n } ^ { m }$ from $\ S 6 . 7$ . Doub deriv = -((n-mm+1)\*plgndr $( \mathtt { n } + 1$ n ,mm,x[k])- Derivative of $P _ { n } ^ { m }$ from a recur-$( \mathtt { n } + 1 ) * \mathtt { x }$ [k]\*plgndr(n,mm,x[k]))/fac1; rence relation. y[1][k]=mm\*x[k]\*y[0][k]/fac1+deriv\*fac2; y[2][k] ${ \bf \delta } = { \bf n } { * } \left( { \bf n } { + } 1 \right) { \bf - } { \bf n } { \bf m } { * } \left( { \bf { \bar { \ n } } } { \bf m } { + } 1 \right)$ ; } x[M] $= 1$ .0; Initial guess at $x = 1$ done sepy[0][M] $=$ anorm; arately. y[2][M] ${ \bf \delta } = { \bf n } { * } \left( { \bf n } { + } 1 \right) { \bf - m m } { * } \left( { \bf m m } { + } 1 \right)$ ; y[1][M] $=$ y[2][M]\*y[0][M]/(2.0\*(mm+1.0)); scalv[0] $=$ abs(anorm); Set scaling. scalv[1] $=$ (y[1][M] $>$ scalv[0] ? y[1][M] : scalv[0]); scalv[2] $=$ (y[2][M] $>$ 1.0 ? y[2][M] : 1.0); for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<MM;j $^ { + + }$ ) { Difeq difeq(mm,n,mpt,h,c2[j],anorm,x); Set up Difeq object. Solvde solvde(itmax,conv,slowc,scalv,indexv,NB,y,difeq); cout $< <$ endl $< < \mathrm { ~ " ~ } \mathrm { ~ m ~ } = \mathrm { ~ " ~ } < <$ setw(3) $< <$ mm; cout << " $\mathrm { ~ \tt ~ n ~ } = \mathrm { ~ \tt ~ n ~ } < <$ setw(3) << n << " c\*\*2 = "; cout $< <$ fixed $< <$ setprecision(3) $< <$ setw(7) << c2[j]; cout << " lamda $=$ " << setprecision(6) $< <$ (y[2][0] $\scriptstyle + \operatorname* { m m } + \left( \mathrm { m m } + 1 \right) .$ ); cout $< <$ endl; Return for another value of $c ^ { 2 }$ . } return 0;

# struct Difeq {

Provides matrix s for Solvde.

const Int &mm,&n,&mpt; These variables are defined in sfroid.   
const Doub &h,&c2,&anorm;   
const VecDoub &x;   
Difeq(const Int &mmm, const Int &nn, const Int &mptt, const Doub &hh, const Doub &cc2, const Doub &anormm, VecDoub_I &xx) : mm(mmm), n(nn), mpt(mptt), h(hh), c2(cc2), anorm(anormm), x(xx) {}   
void smatrix(const Int k, const Int k1, const Int k2, const Int jsf, const Int is1, const Int isf, VecInt_I &indexv, MatDoub_O &s, MatDoub_I &y)   
Returns matrix s for solvde.   
{

Doub temp,temp1,temp2;

if $( \mathrm { ~ k ~ } = = \mathrm { ~ k ~ 1 ~ }$ ) { Boundary condition at first point.if ((n+mm & 1) $\smash { \ ! = \ 0 }$ ) {s[2][3+indexv[0]] $= 1$ .0; Equation (18.4.32).s[2][3+indexv[1]]=0.0;s[2][3+indexv[2]]=0.0;s[2][jsf]=y[0][0]; Equation (18.4.31).} else {s[2][3+indexv[0]] ${ = } 0$ .0; Equation (18.4.32).s[2][3+indexv[1]] ${ = } 1$ .0;s[2][3+indexv[2]]=0.0;s[2][jsf]=y[1][0]; Equation (18.4.31).}  
} else if (k > k2-1) { Boundary conditions at last point.s[0][3+indexv[0]] $=$ -(y[2][mpt-1]-c2)/(2.0\*(mm+1.0)); (18.4.35).s[0][3+indexv[1]] ${ = } 1$ .0;s[0][3+indexv[2]] $=$ -y[0][mpt-1]/(2. $^ { 0 * }$ (mm+1.0));s[0][jsf]=y[1][mpt-1]-(y[2][mpt-1]-c2)\*y[0][mpt-1]/ (18.4.33).(2.0\*(mm+1.0));s[1][3+indexv[0]] $= 1$ .0; Equation (18.4.36).s[1][3+indexv[1]]=0.0;s[1][3+indexv[2]] ${ = } 0$ .0;

s[1][jsf]=y[0][mpt-1]-anorm; Equation (18.4.34).} else { Interior point.s[0][indexv[0]] $= - 1 . 0$ ; Equation (18.4.28).s[0][indexv[1]] $=$ -0.5\*h;s[0][indexv[2]]=0.0;s[0][3+indexv[0]] $^ { = 1 }$ .0;s[0][3+indexv[1]] = -0.5\*h;s[0][3+indexv[2]]=0.0;temp1 $= \mathbf { x }$ [k] $+ \mathbf { x }$ [k-1];temp=h/(1.0-temp1\*temp1\*0.25);temp $_ { 2 = 0 }$ .5\*(y[2][k]+y[2][k-1])-c2\*0.25\*temp1\*temp1;s[1][indexv[0]] $=$ temp\*temp2 $^ { * 0 }$ .5; Equation (18.4.29).s[1][indexv[1]] $=$ -1.0-0.5\*temp\*(mm+1.0)\*temp1;s[1][indexv[2]] ${ = } 0$ .25\*temp\*(y[0][k]+y[0][k-1]);s[1][3+indexv[0]] $= \tt s$ [1][indexv[0]];s[1][3+indexv[1]] $^ { = 2 }$ . $0 + \tt s$ [1][indexv[1]];s[1][3+indexv[2]] $= \tt s$ [1][indexv[2]];s[2][indexv[0]] ${ = } 0$ .0; Equation (18.4.30).s[2][indexv[1]] ${ = } 0$ .0;s[2][indexv[2]] $=$ -1.0;s[2][3+indexv[0]]=0.0;s[2][3+indexv[1]] ${ = } 0$ .0;s[2][3+indexv[2]] $= 1$ .0;s[0][jsf]=y[0][k]-y[0][k-1]-0.5\*h\*(y[1][k]+y[1][k-1]); (18.4.s[1][jsf]=y[1][k]-y[1][k-1]-temp\*((x[k]+x[k-1]) (18.4.\*0.5\*(mm+1.0)\*(y[1][k]+y[1][k-1])-temp2$* 0 \AA . 5 *$ (y[0][k]+y[0][k-1]));s[2][jsf]=y[2][k]-y[2][k-1]; Equation (18.4.27).}};

You can run the program and check it against values of $\lambda _ { m n } ( c )$ given in the tables at the back of Flammer’s book [1] or in Table 21.1 of Abramowitz and Stegun [2]. Typically it converges in about three iterations. The table below gives a few comparisons.

<table><tr><td colspan="4">Selected Output of sfroid</td></tr><tr><td>m</td><td>c2 n</td><td>2exact</td><td>λsfroid</td></tr><tr><td>2</td><td>2</td><td>0.1 6.01427 1.0 6.14095</td><td>6.01427 6.14095</td></tr><tr><td rowspan="3">2</td><td>5</td><td>4.0 6.54250</td><td>6.54253</td></tr><tr><td>1.0</td><td>30.4361</td><td>30.4372</td></tr><tr><td>16.0</td><td>36.9963</td><td>37.0135</td></tr><tr><td>4</td><td>11 -1.0</td><td>131.560</td><td>131.554</td></tr></table>

# 18.4.2 Shooting

To solve the same problem via shooting (-18.1), we supply a functor Rhs that implements equations $( 1 8 . 4 . 1 5 ) - ( 1 8 . 4 . 1 7 )$ . We will integrate the equations over the range $- 1 \leq x \leq 0$ . We provide the functor Load, which sets the eigenvalue $y _ { 2 }$ to its current best estimate, $\tt V [ 0 ]$ . It also sets the boundary values of $y _ { 0 }$ and $y _ { 1 }$ using equations (18.4.20) and (18.4.19) (with a minus sign corresponding to $x \ = \ - 1$ ). Note that the boundary condition is actually applied a distance dx from the boundary to avoid having to evaluate $y _ { 1 } ^ { \prime }$ right on the boundary. The functor Score follows from equation (18.4.18).

# struct Rhs {

Evaluates derivatives for Odeint. Int m; Doub c2; Rhs(Int mm, Doub cc2) : m(mm), c2(cc2) {} Constructor gets parameters from main. void operator() (const Doub x, VecDoub_I &y, VecDoub_O &dydx) { dydx[0]=y[1]; dydx[1] $=$ (2.0\*x\*(m+1.0)\*y[1]-(y[2]-c2\*x\*x)\*y[0])/(1.0-x\*x); dydx[2] $= 0 . 0$ ; }   
};

# struct Load {

Supplies starting values for integration at $x = - 1 + d x$ . Int n,m; Doub gmma,c2,dx; VecDoub y; Load(Int nn, Int mm, Doub gmmaa, Doub cc2, Doub dxx) : n(nn), m(mm), gmma(gmmaa), c2(cc2), dx(dxx), y(3) {} Constructor gets parameters from main. VecDoub operator() (const Doub x1, VecDoub_I &v) { Doub $\ y 1 ~ = ~ ( ~ ( \mathtt { n } \mathrm { - m } ~ \& ~ 1 ) ~ : = ~ 0 ~ ? ~ \mathrm { - g m m a ~ : ~ \ g m m a ) ~ } ;$ y[2] $= \tt v$ [0]; $\begin{array} { r } { \texttt { y } [ 1 ] ~ = ~ - \left( \texttt { y } [ 2 ] - \texttt c 2 \right) * \texttt { y } 1 / \left( 2 * \left( \texttt m + 1 \right) \right) ; } \end{array}$ $\mathtt { y } [ 0 ] = \mathtt { y } 1 + \mathtt { y } [ 1 ] * \mathrm { d } \mathtt { x } ;$ ; return y; }   
};   
struct Score {   
Computes amount by which boundary condition at $x = 0$ is violated. Int n,m; VecDoub f; Score(Int nn, Int mm) : n(nn), m(mm), f(1) {} Constructor gets parameters from main. VecDoub operator() (const Doub xf, VecDoub_I &y) { $\mathbf { f } \ [ 0 ] = \left( \ ( \mathbf { n } - \mathbf { m } \& \ \mathbf { 1 } ) \quad : = \ 0 \ \ ? \ \mathbf { y } \ [ 0 ] \ \ : \ \mathbf { y } \ [ 1 ] \ \right)$ ; return f; }   
};   
Int main_sphoot(void) {   
Sample program using Shoot. Computes eigenvalues of spheroidal harmonics $S _ { m n } ( x ; c )$ for   
$m \geq 0$ and $n \geq m$ . Note how the functor vecfunc for newt is provided by Shoot (-18.1). const Int $ \mathbb { N } 2 { = } 1 , \mathbb { M } \mathbb { M } { = } 3$ ; Bool check; VecDoub $\mathrm { v }$ (N2); Int j, $^ { \mathrm { m = 3 } , \mathrm { n = 5 } }$ ; Doub ${ \mathsf { c } } 2 \left[ { \mathsf { 1 } } = \left\{ 1 . 5 , - 1 . 5 , 0 . 0 \right\} \right.$ ; Int nvar $\scriptstyle = 3$ ; Number of equations. Doub d $\tt c { = } 1$ .0e-8; Avoid evaluating derivatives exactly at $x = - 1$ . for $\scriptstyle ( j = 0$ ;j<MM; ${ \dot { \mathsf { J } } } ^ { + + }$ ) { Doub gmma $^ { = 1 }$ .0; Compute $\gamma$ of equation (18.4.20). Doub $\mathtt { q 1 } = \mathtt { n }$ ; for (Int $\mathbf { i } { = } 1 \ ; \mathbf { i } < = \mathrm { I m } \ ; \mathbf { i } { + } { + } ) \quad \mathrm { g m m a } \quad { \ast } { = } \ - 0 \ . 5 { * } \left( \mathrm { n { + } i } \right) { * } \left( \mathrm { q } 1 { - } { - } / \mathbf { i } \right)$ ; $\mathrm { v } \left[ 0 \right] = \mathrm { n } { * \left( \mathrm { n } { + } 1 \right) } - \mathrm { m } { * \left( \mathrm { m } { + } 1 \right) } + \mathrm { c } 2 \left[ \mathrm { j } \right] / 2 . \mathrm { 0 } \mathrm { ~ }$ ; Initial guess for eigenvalue.

Doub x1= -1.0+dx; Set range of integration. Doub $\mathtt { x 2 = 0 , 0 }$ ; Load load(n,m,gmma,c2[j],dx); Set up Load, Rhs, and Score objects ... Rhs d(m,c2[j]); Score score(n,m); .. use them to set up Shoot object ... Shoot<Load,Rhs,Score> shoot(nvar,x1,x2,load,d,score); newt(v,check,shoot); ... and use it to find v that zeros vector f in if (check) { Score. cout << "shoot failed; bad initial guess" << endl; } else { cout << " " << "mu(m,n)" << endl; cout $< <$ fixed $< <$ setprecision(6); cout << setw(12) << v[0] << endl; } return 0;

# 18.4.3 Shooting to a Fitting Point

For variety we illustrate Shootf from $\ S 1 8 . 2$ by integrating over the whole range $- 1 + d x \leq x \leq 1 - d x$ , with the fitting point chosen to be at $x = 0$ . The routine Rhsfpt is identical to Rhs for Shoot since we are integrating the same equation. Now, however, there are two load routines. The functor Load1 for $x = - 1$ is essentially identical to Load above. At $x = 1$ , Load2 sets the function value $y _ { 0 }$ and the eigenvalue $y _ { 2 }$ to their best current estimates, $\tt v 2 [ 0 ]$ and v2[1], respectively. If you quite sensibly make your initial guess of the eigenvalue the same in the two intervals, then v1[0] will stay equal to v2[1] during the iteration. The functor Score computes the degree of mismatch of the three function values at the fitting point.

struct Rhsfpt { Int m; Doub c2; Rhsfpt(Int mm, Doub cc2) : m(mm), c2(cc2) {} void operator() (const Doub x, VecDoub_I &y, VecDoub_O &dydx) { dydx[0] $\mathbf { \mu } = \mathbf { y }$ [1]; dydx[1] $=$ (2.0\*x\*(m+1.0)\*y[1]-(y[2]-c2\*x\*x)\*y[0])/(1.0-x\*x); dydx[2] $= 0 . 0$ ; }   
};

# struct Load1 {

Supplies starting values for integration at $x = - 1 + d x$ . Int n,m; Doub gmma,c2,dx; VecDoub y; Load1(Int nn, Int mm, Doub gmmaa, Doub cc2, Doub dxx) : n(nn), m(mm), gmma(gmmaa), c2(cc2), dx(dxx), y(3) {} VecDoub operator() (const Doub x1, VecDoub_I &v1) { Doub $\begin{array} { r } { \mathrm { y 1 ~ = ~ ( ( n - m ~ \& ~ 1 ) ~ \theta 1 = ~ 0 ~ \theta ? - g m m a ~ : ~ \ g m m a ) ~ ; } } \end{array}$ y[2]=v1[0]; $\begin{array} { r } { \mathbb { y } \left[ 1 \right] ~ = ~ - \left( \mathbb { y } \left[ 2 \right] - \mathtt { c } 2 \right) { * \mathrm { y } 1 } / \left( 2 * \left( \mathtt { m } + 1 \right) \right) ; } \end{array}$ y[0]=y1+y[1]\*dx; return y; }   
};

# struct Load2 {

Supplies starting values for integration at $x = 1 - d x$ . Int m; Doub c2; VecDoub y; Load2(Int mm, Doub cc2) : m(mm), c2(cc2), y(3) {} VecDoub operator() (const Doub x2, VecDoub_I &v2) { y[2] $=$ v2[1]; y[0] $=$ v2[0]; y[1] $=$ (y[2]-c2)\*y[0]/(2\*(m+1)); return y; }   
};   
struct Score {   
Computes the mismatch of the solutions at the fitting point $x = 0$ . VecDoub f; Score() : f(3) {} VecDoub operator() (const Doub xf, VecDoub_I &y) { for (Int i=0;i<3;i++) f[i]=y[i]; return f; }   
};

# Int main_sphfpt(void) {

Sample program using Shootf. Computes eigenvalues of spheroidal harmonics $S _ { m n } ( x ; c )$ for $m \geq 0$ and $n \geq m$ . Note how the functor vecfunc for newt is provided by Shootf $( \ S 1 8 . 2 )$ . The routine Rhsfpt is the same as Rhs for sphoot.

const Int $\mathbb { N } 1 = 2$ ,N2=1,NTOT $\mathop {  }$ N1+N2,MM=3;   
Bool check;   
VecDoub $\mathtt { v }$ (NTOT);   
Int j, $\mathrm { m } = 3$ , $\mathtt { n } = 5$ , $\scriptstyle \mathtt { n 2 } = \mathtt { N 2 }$ ;   
Doub c2[] $=$ {1.5,-1.5,0.0};   
Int nvar $^ { * = }$ NTOT; Number of equations.   
Doub $\mathtt { d x } { = } 1$ .0e-8; Avoid evaluating derivatives exactly at $x = \pm 1$ .   
for $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<MM; $\mathrm { j } + +$ ) { Doub gmma $^ { = 1 }$ .0; Compute $\gamma$ of equation (18.4.20). Doub $\mathtt { q 1 } = \mathtt { n }$ ; for (In $\mathbf { \partial } ; \mathbf { i } = 1 ; \mathbf { i } < = \mathrm { I m } ; \mathbf { i } + + ) \mathbf { \partial } \operatorname { g m m } { \mathbf { a } } * = \mathbf { \partial } - 0 . 5 * ( \mathrm { n + i } ) * ( \mathrm { q } 1 \mathrm { -- } / \mathbf { i } )$ ; $\mathrm { v } \left[ 0 \right] = \mathrm { n } { \ast } \left( \mathrm { n } { + } 1 \right) { - } \mathrm { m } { \ast } \left( \mathrm { m } { + } 1 \right) { + } \mathrm { c } 2 \left[ { \bf j } \right] / 2 . 0 ;$ Initial guess for eigenvalue and function value. v[2]=v[0]; $\mathrm { ~ v ~ } [ 1 ] = \mathrm { g m m a } \ast \left( 1 . 0 - \left( \mathrm { v } \left[ 2 \right] - \mathrm { c } 2 \left[ \mathrm { j } \right] \right) \ast \mathrm { d } \mathrm { x } / \left( 2 \ast \left( \mathrm { m } + 1 \right) \right) \right) ;$ Doub $\mathbf { x } 1 = \mathbf { \Gamma } - 1$ . $0 +$ dx; Set range of integration. Doub $\tt x 2 = 1$ .0-dx; Doub x $\therefore = 0 , 0$ ; Fitting point. Load1 load1(n,m,gmma,c2[j],dx);Set up Load1, Load2, Rhsfpt, and Score Load2 load2(m,c2[j]); objects ... Rhsfpt d(m,c2[j]); Score score; Shootf<Load1,Load2,Rhsfpt,Score> shootf(nvar,n2,x1,x2,xf,load1, load2,d,score); ... use them to set up Shootf object ... newt(v,check,shootf); ... and use it to find v that zeros vector f in if (check) { Score. cout $< <$ "shootf failed; bad initial guess" << endl; } else { cout << " " << "mu(m,n)" << endl; cout $< <$ fixed $< <$ setprecision(6); cout << setw(12) $< < \texttt { v }$ [0] << endl; }   
}   
return 0;

# CITED REFERENCES AND FURTHER READING:

Flammer, C. 1957, Spheroidal Wave Functions (Stanford, CA: Stanford University Press); reprinted 2005 (New York: Dover).[1]

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, -21.[2]

Morse, P.M., and Feshbach, H. 1953, Methods of Theoretical Physics, Part II (New York: McGraw-Hill), pp. 1502ff.[3]

# 18.5 Automated Allocation of Mesh Points

In relaxation problems, you have to choose values for the independent variable at the mesh points. This is called allocating the grid or mesh. The usual procedure is to pick a plausible set of values and, if it works, to be content. If it doesn’t work, increasing the number of points usually cures the problem.

If we know ahead of time where our solutions will be rapidly varying, we can put more grid points there and less elsewhere. Alternatively, we can solve the problem first on a uniform mesh and then examine the solution to see where we should add more points. We then repeat the solution with the improved grid. The object of the exercise is to allocate points in such a way as to represent the solution accurately.

It is also possible to automate the allocation of mesh points, so that it is done “dynamically” during the relaxation process. This powerful technique not only improves the accuracy of the relaxation method, but also (as we will see in the next section) allows internal singularities to be handled in quite a neat way. Here we learn how to accomplish the automatic allocation.

We want to focus attention on the independent variable $x$ and consider two alternative reparametrizations of it. The first, we term $q$ ; this is just the coordinate corresponding to the mesh points themselves, so that $q = 0$ at $\mathtt { k } = 0$ , $q = 1$ at $\Bbbk = 1$ , and so on. Between any two mesh points we have $\Delta q = 1$ . In the change of independent variable in the ODEs from $x$ to $q$ ,

$$
{ \frac { d \mathbf { y } } { d x } } = \mathbf { g }
$$

becomes

$$
{ \frac { d \mathbf { y } } { d q } } = \mathbf { g } { \frac { d x } { d q } } 
$$

In terms of $q$ , equation (18.5.2) as an FDE might be written

$$
{ \bf y } _ { k } - { \bf y } _ { k - 1 } - \frac { 1 } { 2 } \bigg [ \bigg ( { \bf g } \frac { d x } { d q } \bigg ) _ { k } + \bigg ( { \bf g } \frac { d x } { d q } \bigg ) _ { k - 1 } \bigg ] = 0
$$

or some related version. Note that $d x / d q$ should accompany $\mathbf { g }$ . The transformation between $x$ and $q$ depends only on the Jacobian $d x / d q$ . Its reciprocal $d q / d x$ is proportional to the density of mesh points.

Now, given the function $\mathbf { y } ( x )$ , or its approximation at the current stage of relaxation, we are supposed to have some idea of how we want to specify the density of mesh points. For example, we might want $d q / d x$ to be larger where $\mathbf { y }$ is changing rapidly, or near to the boundaries, or both. In fact, we can probably make up a formula for what we would like $d q / d x$ to be proportional to. The problem is that we do not know the proportionality constant. That is, the formula that we might invent would not have the correct integral over the whole range of $x$ so as to make $q$ vary from 0 to $M - 1$ , according to its definition. To solve this problem we introduce a second reparametrization $Q ( q )$ , where $\boldsymbol { Q }$ is a new independent variable. The relation between $\boldsymbol { Q }$ and $q$ is taken to be linear, so that a mesh spacing formula for $d Q / d x$ differs only in its unknown proportionality constant. A linear relation implies

$$
{ \frac { d ^ { 2 } Q } { d q ^ { 2 } } } = 0
$$

or, expressed in the usual manner as coupled first-order equations,

$$
{ \frac { d Q ( x ) } { d q } } = \psi \qquad { \frac { d \psi } { d q } } = 0
$$

where $\psi$ is a new intermediate variable. We add these two equations to the set of ODEs being solved.

Completing the prescription, we add a third ODE that is just our desired mesh-density function, namely

$$
\phi ( x ) = { \frac { d Q } { d x } } = { \frac { d Q } { d q } } { \frac { d q } { d x } }
$$

where $\phi ( x )$ is chosen by us. Written in terms of the mesh variable $q$ , this equation is

$$
\frac { d x } { d q } = \frac { \psi } { \phi ( x ) }
$$

Notice that $\phi ( x )$ should be chosen to be positive-definite, so that the density of mesh points is everywhere positive. Otherwise (18.5.7) can have a zero in its denominator.

To use automated mesh spacing, you add the three ODEs (18.5.5) and (18.5.7) to your set of equations, i.e., to the array y[j][k]. Now $x$ becomes a dependent variable! $\boldsymbol { Q }$ and $\psi$ also become new dependent variables. Normally, evaluating $\phi$ requires little extra work since it will be composed from pieces of the $g$ ’s that exist anyway. The automated procedure allows one to investigate quickly how the numerical results might be affected by various strategies for mesh spacing. (A special case occurs if the desired mesh spacing function $\boldsymbol { Q }$ can be found analytically, i.e., $d Q / d x$ is directly integrable. Then, you need to add only two equations, those in 18.5.5, and two new variables $x , \psi$ .)

As an example of a typical strategy for implementing this scheme, consider a system with one dependent variable $y ( x )$ . We could set

$$
d Q = \frac { d x } { \Delta } + \frac { | d \ln { y } | } { \delta }
$$

or

$$
\phi ( x ) = \frac { d Q } { d x } = \frac { 1 } { \Delta } + \left| \frac { d y / d x } { y \delta } \right|
$$

where $\Delta$ and $\delta$ are constants that we choose. The first term would give a uniform spacing in $x$ if it alone were present. The second term forces more grid points to be used where $y$ is changing rapidly. The constants act to make every logarithmic change in $y$ of an amount $\delta$ about as “attractive” to a grid point as a change in $x$ of amount $\Delta$ . You adjust the constants according to taste. Other strategies are possible, such as a logarithmic spacing in $x$ , where $d x$ in the first term is replaced with $d \ln x$ .

# CITED REFERENCES AND FURTHER READING:

Eggleton, P.P. 1971, “The Evolution of Low Mass Stars,” Monthly Notices of the Royal Astronomical Society,vol.151, pp.351-364.   
Kippenhan, R., Weigert, A., and Hofmeister, E. 1968, in Methods in Computational Physics, vol. 7 (New York: Academic Press), pp. 129ff.

# 18.6 Handling Internal Boundary Conditions or Singular Points

Singularities can occur in the interiors of two-point boundary value problems. Typically, there is a point $x _ { s }$ at which a derivative must be evaluated by an expression of the form

$$
S ( x _ { s } ) = \frac { N ( x _ { s } , { \bf y } ) } { D ( x _ { s } , { \bf y } ) }
$$

where the denominator $D ( x _ { s } , \mathbf { y } ) = 0$ . In physical problems with finite answers, singular points usually come with their own cure: Where $D \to 0$ , there the physical solution $\mathbf { y }$ must be such as to make $N  0$ simultaneously, in such a way that the ratio takes on a meaningful value. This constraint on the solution $\mathbf { y }$ is often called a regularity condition. The condition that $D ( x _ { s } , \mathbf { y } )$ satisfy some special constraint at $x _ { s }$ is entirely analogous to an extra boundary condition, an algebraic relation among the dependent variables that must hold at a point.

We discussed a related situation earlier, in $\ S 1 8 . 2$ , when we described the “fitting point method” to handle the task of integrating equations with singular behavior at the boundaries. In those problems you are unable to integrate from one side of the domain to the other. However, the ODEs do have well-behaved derivatives and solutions in the neighborhood of the singularity, so it is readily possible to integrate away from the point. Both the relaxation method and the method of shooting to a fitting point handle such problems easily. Also, in those problems the presence of singular behavior served to isolate some special boundary values that had to be satisfied to solve the equations.

The difference here is that we are concerned with singularities arising at intermediate points, where the location of the singular point depends on the solution, so is not known a priori. Consequently, we face a circular task: The singularity prevents us from finding a numerical solution, but we need a numerical solution to find its location. Such singularities are also associated with selecting a special value for some variable that allows the solution to satisfy the regularity condition at the singular point. Thus, internal singularities take on aspects of being internal boundary conditions.

One way of handling internal singularities is to treat the problem as a free boundary problem, as discussed at the end of $\ S 1 8 . 0$ . Suppose, as a simple example, we consider the equation

$$
{ \frac { d y } { d x } } = { \frac { N ( x , y ) } { D ( x , y ) } }
$$

where $N$ and $D$ are required to pass through zero at some unknown point $x _ { s }$ . We add the equation

$$
z \equiv x _ { s } - x _ { 1 } \qquad { \frac { d z } { d x } } = 0
$$

where $x _ { s }$ is the unknown location of the singularity, and change the independent variable to $t$ by setting

$$
x - x _ { 1 } = t z , \qquad 0 \leq t \leq 1
$$

The boundary conditions at $t = 1$ become

$$
N ( x , y ) = 0 , \qquad D ( x , y ) = 0
$$

Use of an adaptive mesh as discussed in the previous section is another way to overcome the difficulties of an internal singularity. For the problem (18.6.2), we add the mesh spacing equations

$$
\begin{array} { l } { { \frac { d Q } { d q } = \psi } } \\ { { \frac { d \psi } { d q } = 0 } } \end{array}
$$

with a simple mesh spacing function that maps $x$ uniformly into $q$ , where $q$ runs from 0 to $M - 1$ , with $M$ the number of mesh points:

$$
Q ( x ) = x - x _ { 1 } , \quad { \frac { d Q } { d x } } = 1
$$

Having added three first-order differential equations, we must also add their corresponding boundary conditions. If there were no singularity, these could simply be

$$
\left. \begin{array} { l l } { \mathrm { a t } q = 0 : } & { x = x _ { 1 } , \quad Q = 0 } \\ { \mathrm { a t } q = M - 1 : } & { x = x _ { 2 } } \end{array} \right.
$$

and a total of $N$ values $y _ { i }$ specified at $q = 0$ . In this case the problem is essentially an initial value problem with all boundary conditions specified at $x _ { 1 }$ and the mesh spacing function is superfluous.

However, in the actual case at hand we impose the conditions

$$
\begin{array} { l l l } { { \mathrm { a t ~ } q = 0 : } } & { { x = x _ { 1 } , } } & { { Q = 0 } } \\ { { \mathrm { a t ~ } q = M - 1 : } } & { { N ( x , y ) = 0 , } } & { { D ( x , y ) = 0 } } \end{array}
$$

and $N - 1$ values $y _ { i }$ at $q \ : = \ : 0$ . The “missing” $y _ { i }$ is to be adjusted, in other words, so as to make the solution go through the singular point in a regular (zero-over-zero) rather than irregular (finite-over-zero) manner. Notice also that these boundary conditions do not directly impose a value for $x _ { 2 }$ , which becomes an adjustable parameter that the code varies in an attempt to match the regularity condition.

In this example the singularity occurred at a boundary, and the complication arose because the location of the boundary was unknown. In other problems we might wish to continue the integration beyond the internal singularity. For the example given above, we could simply integrate the ODEs to the singular point, and then as a separate problem recommence the integration from the singular point on as far we care to go. However, in other cases the singularity occurs internally, but does not completely determine the problem: There are still some more boundary conditions to be satisfied further along in the mesh. Such cases present no difficulty in principle, but do require some adaptation of the relaxation code given in $\ S 1 8 . 3$ . In effect, all you need to do is to add a “special” block of equations at the mesh point where the internal boundary conditions occur, and do the proper bookkeeping.

Figure 18.6.1 illustrates a concrete example where the overall problem contains five equations with two boundary conditions at the first point, one “internal” boundary condition, and two final boundary conditions. The figure shows the structure of the overall matrix equations along the diagonal in the vicinity of the special block. In the middle of the domain, blocks typically involve five equations (rows) in ten unknowns (columns). For each block prior to the special block, the initial boundary conditions provided enough information to zero the first two columns of the blocks. The five FDEs eliminate five more columns, and the final three columns need to be stored for the backsubstitution step (as described in $\ S 1 8 . 3 \AA$ ). To handle the extra condition, we break the normal cycle and add a special block with only one equation: the internal boundary condition. This effectively reduces the required storage of unreduced coefficients by one column for the rest of the grid, and allows us to reduce to zero the first three columns of subsequent blocks. The functions red, pinvs, and bksub can readily handle these cases with minor recoding, but each problem makes for a special case, and you will have to make the modifications as required.

# CITED REFERENCES AND FURTHER READING:

London, R.A., and Flannery, B.P. 1982, “Hydrodynamics of X-Ray Induced Stellar Winds,” Astrophysical Journal, vol. 258,pp.260-269.

![](images/40bef1fd2c6ab6b356706012d606879a94577e9022c245c7733c3103d8df942b.jpg)  
Figure 18.6.1. FDE matrix structure with an internal boundary condition. The internal condition introduces a special block. (a) Original form, compare with Figure 18.3.1; (b) final form, compare with Figure 18.3.2.

# Integral Equations and Inverse Theory

# CHAPTER 19

# 19.0 Introduction

Many people, otherwise numerically knowledgable, imagine that the numerical solution of integral equations must be an extremely arcane topic, since, until recently, it was almost never treated in numerical analysis textbooks. Actually there is a large and growing literature on the numerical solution of integral equations, including several good monographs [1-3]. One reason for the sheer volume of this activity is that there are many different kinds of equations, each with many different possible pitfalls; often many different algorithms have been proposed to deal with a single case.

There is a close correspondence between linear integral equations, which specify linear, integral relations among functions in an infinite-dimensional function space, and plain old linear equations, which specify analogous relations among vectors in a finite-dimensional vector space. Because this correspondence lies at the heart of most computational algorithms, it is worth making it explicit as we recall how integral equations are classified.

Fredholm equations involve definite integrals with fixed upper and lower limits. An inhomogeneous Fredholm equation of the first kind has the form

$$
g ( t ) = \int _ { a } ^ { b } K ( t , s ) f ( s ) d s
$$

Here $f ( t )$ is the unknown function to be solved for, while $g ( t )$ is a known “righthand side.” (In integral equations, for some odd reason, the familiar “right-hand side” is conventionally written on the left!) The function of two variables, $K ( t , s )$ , is called the kernel. Equation (19.0.1) is analogous to the matrix equation

$$
\mathbf { K } \cdot \mathbf { f } = \mathbf { g }
$$

whose solution is $\textbf { f } = \mathbf { K } ^ { - 1 } \cdot \textbf { g }$ , where $\mathbf { K } ^ { - 1 }$ is the matrix inverse. Like equation (19.0.2), equation (19.0.1) has a unique solution whenever $g$ is nonzero (the homogeneous case with $g = 0$ is almost never useful) and $K$ is invertible. However, as we shall see, this latter condition is as often the exception as the rule.

The analog of the finite-dimensional eigenvalue problem

$$
\mathbf { ( K - } \sigma \mathbf { 1 ) } \cdot \mathbf { f } = \mathbf { g }
$$

is called a Fredholm equation of the second kind, usually written

$$
f ( t ) = \lambda \int _ { a } ^ { b } K ( t , s ) f ( s ) d s + g ( t )
$$

Again, the notational conventions do not exactly correspond: $\lambda$ in equation (19.0.4) is $1 / \sigma$ in (19.0.3), while $\mathbf { g }$ is $- g / \lambda$ . If $g$ (or $\mathbf { g }$ ) is zero, then the equation is said to be homogeneous. If the kernel $K ( t , s )$ is bounded, then, like equation (19.0.3), equation (19.0.4) has the property that its homogeneous form has solutions for at most a denumerably infinite set $\lambda = \lambda _ { n }$ , $n = 1 , 2 , \ldots$ , the eigenvalues. The corresponding solutions $f _ { n } ( t )$ are the eigenfunctions. The eigenvalues are real if the kernel is symmetric.

In the inhomogeneous case of nonzero $g$ (or $\mathbf { g }$ ), equations (19.0.3) and (19.0.4) are soluble except when $\lambda$ (or $\sigma$ ) is an eigenvalue — because the integral operator (or matrix) is singular then. In integral equations this dichotomy is called the Fredholm alternative.

Fredholm equations of the first kind are often extremely ill-conditioned. Applying the kernel to a function is generally a smoothing operation, so the solution, which requires inverting the operator, will be extremely sensitive to small changes or errors in the input. Smoothing often actually loses information, and there is no way to get it back in an inverse operation. Specialized methods have been developed for such equations, which are often called inverse problems. In general, a method must augment the information given with some prior knowledge of the nature of the solution. This prior knowledge is then used, in one way or another, to restore lost information. We will introduce such techniques in $\ S 1 9 . 4$ .

Inhomogeneous Fredholm equations of the second kind are much less often illconditioned. Equation (19.0.4) can be rewritten as

$$
\int _ { a } ^ { b } [ K ( t , s ) - \sigma \delta ( t - s ) ] f ( s ) d s = - \sigma g ( t )
$$

where $\boldsymbol { \delta } ( t - s )$ is a Dirac delta function (and where we have changed from $\lambda$ to its reciprocal $\sigma$ for clarity). If $\sigma$ is large enough in magnitude, then equation (19.0.5) is, in effect, diagonally dominant and thus well-conditioned. Only if $\sigma$ is small do we go back to the ill-conditioned case.

Homogeneous Fredholm equations of the second kind are likewise not particularly ill-posed. If $K$ is a smoothing operator, then it will map many $f$ ’s to zero, or near-zero; there will thus be a large number of degenerate or nearly degenerate eigenvalues around $\sigma = 0$ $\lambda \to \infty$ ), but this will cause no particular computational difficulties. In fact, we can now see that the magnitude of $\sigma$ needed to rescue the inhomogeneous equation (19.0.5) from an ill-conditioned fate is generally much less than that required for diagonal dominance. Since the $\sigma$ term shifts all eigenvalues, it is enough that it be large enough to shift a smoothing operator’s forest of nearzero eigenvalues away from zero, so that the resulting operator becomes invertible (except, of course, at the discrete eigenvalues).

Volterra equations are a special case of Fredholm equations with $K ( t , s ) = 0$ for $s > t$ . Chopping off the unnecessary part of the integration, Volterra equations are written in a form where the upper limit of integration is the independent variable $t$ . The Volterra equation of the first kind,

$$
g ( t ) = \int _ { a } ^ { t } K ( t , s ) f ( s ) d s
$$

has as its analog the matrix equation (now written out in components)

$$
\sum _ { j = 0 } ^ { k } K _ { k j } f _ { j } = g _ { k }
$$

Comparing with equation (19.0.2), we see that the Volterra equation corresponds to a matrix K that is lower (i.e., left) triangular, with zero entries above the diagonal. As we know from Chapter 2, such matrix equations are trivially soluble by forward substitution. Techniques for solving Volterra equations are similarly straightforward. When experimental measurement noise does not dominate, Volterra equations of the first kind tend not to be ill-conditioned; the upper limit to the integral introduces a sharp step that conveniently spoils any smoothing properties of the kernel.

The Volterra equation of the second kind is written

$$
f ( t ) = \int _ { a } ^ { t } K ( t , s ) f ( s ) d s + g ( t )
$$

whose matrix analog is the equation

$$
( \mathbf { K } - \mathbf { 1 } ) \cdot \mathbf { f } = \mathbf { g }
$$

with $\mathbf { K }$ lower triangular. The reason there is no $\lambda$ in these equations is that (i) in the inhomogeneous case (nonzero $g$ ) it can be absorbed into $K$ , while (ii) in the homogeneous case $( g = 0$ ), it is a theorem that Volterra equations of the second kind with bounded kernels have no eigenvalues with square-integrable eigenfunctions.

We have specialized our definitions to the case of linear integral equations. In a nonlinear version of equation (19.0.1) or (19.0.6), instead of $K ( t , s ) f ( s )$ the integrand would be $K ( t , s , f ( s ) )$ . A nonlinear version of equation (19.0.4) or (19.0.8) would have an integrand $K ( t , s , f ( t ) , f ( s ) )$ . Nonlinear Fredholm equations are considerably more complicated than their linear counterparts. Fortunately, they do not occur as frequently in practice and we shall by and large ignore them in this chapter. By contrast, solving nonlinear Volterra equations usually involves only a slight modification of the algorithm for linear equations, as we shall see.

Almost all methods for solving integral equations numerically make use of quadrature rules, frequently Gaussian quadratures. This would be a good time for you to go back and review $\ S 4 . 6$ , especially the advanced material toward the end of that section.

In the sections that follow, we first discuss Fredholm equations of the second kind with smooth kernels (-19.1). Nontrivial quadrature rules come into the discussion, but we will be dealing with well-conditioned systems of equations. We then return to Volterra equations (-19.2), and find that simple and straightforward methods are generally satisfactory for these equations.

In $\ S 1 9 . 3$ we discuss how to proceed in the case of singular kernels, focusing largely on Fredholm equations (both first and second kinds). Singularities require special quadrature rules, but they are also sometimes blessings in disguise, since they can spoil a kernel’s smoothing and make problems well-conditioned.

In $\ S 1 9 . 4 - \ S 1 9 . 7$ we face up to the issues of inverse problems. Section 19.4 is an introduction to this large subject.

We should note here that wavelet transforms, already discussed in $\ S 1 3 . 1 0$ , are applicable not only to data compression and signal processing, but can also be used to transform some classes of integral equations into sparse linear problems that allow fast solution. You may wish to review $\ S 1 3 . 1 0$ as part of reading this chapter.

Some subjects, such as integro-differential equations, we must simply declare to be beyond our scope. For a review of methods for integro-differential equations, see Brunner [4].

It should go without saying that this one short chapter can only barely touch on a few of the most basic methods involved in this complicated subject.

# CITED REFERENCES AND FURTHER READING:

Delves, L.M., and Mohamed, J.L. 1985, Computational Methods for Integral Equations (Cambridge, UK: Cambridge University Press).[1]   
Linz, P. 1985, Analytical and Numerical Methods for Volterra Equations (Philadelphia: S.I.A.M.).[2]   
Atkinson, K.E. 1976, A Survey of Numerical Methods for the Solution of Fredholm Integral Equations of the Second Kind (Philadelphia: S.I.A.M.).[3]   
Brunner, H. 1988, in Numerical Analysis 1987, Pitman Research Notes in Mathematics vol. 170, D.F. Griffiths and G.A. Watson, eds. (Harlow, Essex, UK: Longman Scientific and Technical), pp. 18–38.[4]   
Smithies, F. 1958, Integral Equations (Cambridge, UK: Cambridge University Press).   
Kanwal, R.P. 1971, Linear Integral Equations (New York: Academic Press).   
Green, C.D. 1969, Integral Equation Methods (New York: Barnes & Noble).

# 19.1 Fredholm Equations of the Second Kind

We desire a numerical solution for $f ( t )$ in the equation

$$
f ( t ) = \lambda \int _ { a } ^ { b } K ( t , s ) f ( s ) d s + g ( t )
$$

The method we describe, a very basic one, is called the Nystrom method. It requires the choice of some approximate quadrature rule:

$$
\int _ { a } ^ { b } y ( s ) d s = \sum _ { j = 0 } ^ { N - 1 } w _ { j } y ( s _ { j } )
$$

Here the set $\{ w _ { j } \}$ are the weights of the quadrature rule, while the $N$ points $\{ s _ { j } \}$ are the abscissas.

What quadrature rule should we use? It is certainly possible to solve integral equations with low-order quadrature rules like the extended trapezoidal or Simpson’s rules. We will see, however, that the solution method involves $O ( N ^ { 3 } )$ operations, and so the most efficient methods tend to use high-order quadrature rules to keep $N$ as small as possible. For smooth, nonsingular problems, nothing beats Gaussian quadrature (e.g., Gauss-Legendre quadrature, $\ S 4 . 6 )$ . (For nonsmooth or singular kernels, see $\ S 1 9 . 3 . )$

Delves and Mohamed [1] investigated methods more complicated than the Nystrom method. For straightforward Fredholm equations of the second kind, they concluded “. . . the clear winner of this contest has been the Nystrom routine . . . with the $N$ -point Gauss-Legendre rule. This routine is extremely simple. . . . Such results are enough to make a numerical analyst weep.”

If we apply the quadrature rule (19.1.2) to equation (19.1.1), we get

$$
f ( t ) = \lambda \sum _ { j = 0 } ^ { N - 1 } w _ { j } K ( t , s _ { j } ) f ( s _ { j } ) + g ( t )
$$

Evaluate equation (19.1.3) at the quadrature points:

$$
f ( t _ { i } ) = \lambda \sum _ { j = 0 } ^ { N - 1 } w _ { j } K ( t _ { i } , s _ { j } ) f ( s _ { j } ) + g ( t _ { i } )
$$

Let $f _ { i }$ be the vector $f ( t _ { i } ) , g _ { i }$ the vector $g ( t _ { i } ) , K _ { i j }$ the matrix $K ( t _ { i } , s _ { j } )$ , and define

$$
\widetilde { K } _ { i j } = K _ { i j } w _ { j }
$$

Then, in matrix notation, equation (19.1.4) becomes

$$
( \mathbf { 1 } - \lambda { \widetilde { \mathbf { K } } } ) \cdot \mathbf { f } = \mathbf { g }
$$

This is a set of $N$ linear algebraic equations in $N$ unknowns that can be solved by standard triangular decomposition techniques $( \ S 2 . 3 )$ — that is where the $O ( N ^ { 3 } )$ operations count comes in. The solution is usually well-conditioned, unless $\lambda$ is very close to an eigenvalue.

Having obtained the solution at the quadrature points $\{ t _ { i } \}$ , how do you get the solution at some other point $t ?$ You do not simply use polynomial interpolation. This destroys all the accuracy you have worked so hard to achieve. Nystrom’s key observation was that you should use equation (19.1.3) as an interpolatory formula, maintaining the accuracy of the solution.

Our routine for solving linear Fredholm equations of the second kind is coded as the object Fred2. The constructor sets up equation (19.1.6) and then solves it by $L U$ decomposition with LUdcmp. The Gauss-Legendre quadrature is implemented by first getting the weights and abscissas with a call to gauleg. The routine Fred2 requires that you provide an external function or functor that returns $g ( t )$ and another that returns $\lambda K _ { i j }$ . It then computes the solution $f$ at the quadrature points in the member variable f. It also stores the quadrature points and weights. These are used by the member function fredin to carry out the Nystrom interpolation of equation (19.1.3) and return the value of $f$ at any point in the interval $[ a , b ]$ .

To be sure the usage is clear, here is the calling sequence when you have coded the external routines as functions:

Doub g(const Doub t) { ... }   
Doub ak(const Doub t, const Doub s) { ... }   
Fred2<Doub (Doub), Doub (Doub,Doub)> fred2(a,b,n,g,ak); Doub ans=fred2.fredin(x);

If the external routines are functors Gfunc and Kernel, say, then the declarations are

Gfunc g; This could have arguments if you like.   
Kernel ak;   
Fred2<Gfunc, Kernel> fred2(a,b,n,g,ak);

Here is the routine:

template <class G, class K>   
struct Fred2 {   
Solves a linear Fredholm equation of the second kind. const Doub a,b; const Int n; G &g; K &ak; VecDoub t,f,w; Fred2(const Doub aa, const Doub bb, const Int nn, G &gg, K &akk) a(aa), b(bb), $\mathbf { n } ( \mathbf { n n } )$ , $\pmb { \mathrm { g } } ( \pmb { \mathrm { g } } \pmb { \mathrm { g } } )$ , ak(akk), t(n), $\mathtt { f } \left( \mathtt { n } \right)$ , $\mathtt { w } ( \mathtt { n } )$ Quantities a and b are input as the limits of integration. The quantity n is the number of points to use in the Gaussian quadrature. $\mathsf { g }$ and ak are user-supplied functions or functors that respectively return $g ( t )$ and $\lambda K ( t , s )$ . This constructor computes arrays $\mathbf { t } \left[ 0 \ldots \mathbf { n - 1 } \right]$ and $\mathbf { \rho } : [ 0 \ldots \mathbf { n } \mathrm { - } 1 ]$ containing the abscissas $t _ { i }$ of the Gaussian quadrature and the solution $f$ at these abscissas. Also computed is the array $\mathtt { w } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ of Gaussian weights for use with the Nystrom interpolation routine fredin.   
{   
MatDoub omk ${ ( \mathtt { n } , \mathtt { n } ) }$ ;   
gauleg(a,b,t,w); Replace gauleg with another routine if not using   
for (Int $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) { Gauss-Legendre quadrature. for (Int j=0;j<n;j++) Form $\mathbf { 1 } - \lambda \widetilde { \mathbf { K } }$ . omk[i][j]=Doub( $\begin{array} { l l } { \dot { \perp } } & { = = } \end{array}$ j)-ak(t[i],t[j])\*w[j]; f[i]=g(t[i]);   
1   
LUdcmp alu(omk); Solve linear equations.   
alu.solve(f,f);

# Doub fredin(const Doub x)

Given arrays $\mathbf { t } \left[ 0 \ldots \mathbf { n } \mathbf { - } 1 \right]$ and $\mathtt { w } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ containing the abscissas and weights of the Gaussian quadrature, and given the solution array f[0..n-1], this function returns the value of $f$ at $\mathbf { x }$ using the Nystrom interpolation formula.

Doub sum $\mathord { \left. \downarrow \right. } = 0 . 0$ ; for (Int $\mathrm { i = 0 ; i < n ; i + + ) ~ s u m ~ + = ~ a k ( x , t [ i ] ) * _ { W } [ i ] * f [ i ] ; }$ return $\mathtt { g } ( \mathtt { x } ) + \mathtt { s u m }$ ; } ;

One disadvantage of a method based on Gaussian quadrature is that there is no simple way to obtain an estimate of the error in the result. The best practical method is to increase $N$ by $50 \%$ , say, and treat the difference between the two estimates as a conservative estimate of the error in the result obtained with the larger value of $N$ .

Turn now to solutions of the homogeneous equation. If we set $\lambda = 1 / \sigma$ and $\mathbf g = 0$ , then equation (19.1.6) becomes a standard eigenvalue equation,

$$
\widetilde { \mathbf { K } } \cdot \mathbf { f } = \sigma \mathbf { f }
$$

which we can solve with any convenient matrix eigenvalue routine (see Chapter 11). Note that if our original problem had a symmetric kernel, then the matrix K would be symmetric. However, since the weights $w _ { j }$ are not equal for most quadrature rules, the matrix $\widetilde { \mathbf { K } }$ (equation 19.1.5) is not symmetric. The matrix eigenvalue problem is much easier for symmetric matrices, and so we should restore the symmetry if possible. Provided the weights are positive (which they are for Gaussian quadrature), we can define the diagonal matrix $\mathbf { D } \ = \ \mathrm { d i a g } ( w _ { j } )$ and its square root, $\mathbf { D } ^ { 1 / 2 } \ =$ $\mathrm { d i a g } ( \sqrt { w _ { j } } )$ . Then equation (19.1.7) becomes

$$
\mathbf { K } \cdot \mathbf { D } \cdot \mathbf { f } = \sigma \mathbf { f }
$$

Multiplying by $\mathbf { D } ^ { 1 / 2 }$ , we get

$$
\left( \mathbf { D } ^ { 1 / 2 } \cdot \mathbf { K } \cdot \mathbf { D } ^ { 1 / 2 } \right) \cdot \mathbf { h } = \sigma \mathbf { h }
$$

where $ { \mathbf { h } } =  { \mathbf { D } } ^ { 1 / 2 }$ f . Equation (19.1.8) is now in the form of a symmetric eigenvalue problem.

Solution of equations (19.1.7) or (19.1.8) will in general give $N$ eigenvalues, where $N$ is the number of quadrature points used. For square-integrable kernels, these will provide good approximations to the lowest $N$ eigenvalues of the integral equation. Kernels of finite rank (also called degenerate or separable kernels) have only a finite number of nonzero eigenvalues (possibly none). You can diagnose this situation by a cluster of eigenvalues $\sigma$ that are zero to machine precision. The number of nonzero eigenvalues will stay constant as you increase $N$ to improve their accuracy. Some care is required here: A nondegenerate kernel can have an infinite number of eigenvalues that have an accumulation point at $\sigma = 0$ . You distinguish the two cases by the behavior of the solution as you increase $N$ . If you suspect a degenerate kernel, you will usually be able to solve the problem by analytic techniques described in all the textbooks.

# CITED REFERENCES AND FURTHER READING:

Delves, L.M., and Mohamed, J.L. 1985, Computational Methods for Integral Equations (Cambridge, UK: Cambridge University Press).[1]   
Atkinson, K.E. 1976, A Survey of Numerical Methods for the Solution of Fredholm Integral Equations of the Second Kind (Philadelphia: S.I.A.M.).

# 19.2 Volterra Equations

Let us now turn to Volterra equations, of which our prototype is the Volterra equation of the second kind,

$$
f ( t ) = \int _ { a } ^ { t } K ( t , s ) f ( s ) d s + g ( t )
$$

Most algorithms for Volterra equations march out from $t = a$ , building up the solution as they go. In this sense they resemble not only forward substitution (as discussed in $\ S 1 9 . 0 \}$ , but also initial value problems for ordinary differential equations. In fact, many algorithms for ODEs have counterparts for Volterra equations.

The simplest way to proceed is to solve the equation on a mesh with uniform spacing:

$$
t _ { i } = a + i h , \quad i = 0 , 1 , \ldots , N , \qquad h \equiv \frac { b - a } { N }
$$

To do so, we must choose a quadrature rule. For a uniform mesh, the simplest scheme is the trapezoidal rule, equation (4.1.11):

$$
\int _ { a } ^ { t _ { i } } K ( t _ { i } , s ) f ( s ) d s = h \left( { \frac { 1 } { 2 } } K _ { i 0 } f _ { 0 } + \sum _ { j = 1 } ^ { i - 1 } K _ { i j } f _ { j } + { \frac { 1 } { 2 } } K _ { i i } f _ { i } \right)
$$

Thus the trapezoidal method for equation (19.2.1) is

$$
{ \begin{array} { c } { f _ { 0 } = g _ { 0 } } \\ { \displaystyle ( 1 - { \frac { 1 } { 2 } } h K _ { i i } ) f _ { i } = h \Biggl ( { \frac { 1 } { 2 } } K _ { i 0 } f _ { 0 } + \sum _ { j = 1 } ^ { i - 1 } K _ { i j } f _ { j } \Biggr ) + g _ { i } , \qquad i = 1 , \dots , N } \end{array} }
$$

(For a Volterra equation of the first kind, the leading 1 on the left would be absent, and $g$ would have opposite sign, with corresponding straightforward changes in the rest of the discussion.)

Equation (19.2.4) is an explicit prescription that gives the solution in $O ( N ^ { 2 } )$ operations. Unlike Fredholm equations, it is not necessary to solve a system of linear equations. Volterra equations thus usually involve less work than the corresponding Fredholm equations, which, as we have seen, do involve the inversion of, sometimes large, linear systems.

The efficiency of solving Volterra equations is somewhat counterbalanced by the fact that systems of these equations occur more frequently in practice. If we interpret equation (19.2.1) as a vector equation for the vector of $m$ functions $f ( t )$ , then the kernel $K ( t , s )$ is an $m \times m$ matrix. Equation (19.2.4) must now also be understood as a vector equation. For each $i$ , we have to solve the $m \times m$ set of linear algebraic equations by Gaussian elimination.

The routine voltra below implements this algorithm. You must supply an external function or functor that returns the $k$ th function of the vector $g ( t )$ at the point $t$ and another that returns the $( k , l )$ element of the matrix $K ( t , s )$ at $( t , s )$ . The routine voltra then returns the vector $f ( t )$ at the regularly spaced points $t _ { i }$ .

# template <class G, class K>

# voltra.h

Int $\mathtt { n } { = } \mathtt { f }$ .ncols();   
VecDoub b(m);   
MatDoub a(m,m);   
t[0] $\mathtt { \mathtt { = t 0 } }$ ;   
for (Int $\mathtt { k } = 0$ ;k<m;k++) f[k][0]=g(k,t[0]); Initialize.   
for (Int $\dot { \bar { 1 } } = 1$ ;i<n;i++) { Take a step h. t[i] $\mathtt { \Omega } = \mathtt { t }$ [i-1]+h; for (Int $\mathtt { k } = 0$ ;k<m;k++) { Doub sum=g(k,t[i]); Accumulate right-hand side of linear for (Int l=0;l<m; $^ { 1 + + }$ ) { equations in sum. sum $+ =$ 0.5\*h\*ak(k,l,t[i],t[0])\*f[l][0]; for (Int $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<i;j++) sum $+ =$ h\*ak(k,l,t[i],t[j])\*f[l][j]; if $( \textbf { k } = \textbf { 1 } )$ ) Left-hand side goes in matrix a. a[k][l] $^ { = 1 }$ .0-0.5\*h\*ak(k,l,t[i],t[i]); else a[k][l] $=$ -0.5\*h\*ak(k,l,t[i],t[i]); } b[k] $=$ sum; LUdcmp alu(a); Solve linear equations. alu.solve(b,b); for (Int k=0;k<m;k++) f[k][i] $= \mathrm { b }$ [k];   
}

For nonlinear Volterra equations, equation (19.2.4) holds with the product $K _ { i i } f _ { i }$ replaced by $K _ { i i } ( f _ { i } )$ , and similarly for the other two products of $K$ ’s and $f$ ’s. Thus, for each $i$ we solve a nonlinear equation for $f _ { i }$ with a known right-hand side. Newton’s method $\mathrm { \ : 8 9 . 4 }$ or $\ S 9 . 6 )$ with an initial guess of $f _ { i - 1 }$ usually works very well provided the stepsize is not too big.

Higher-order methods for solving Volterra equations are, in our opinion, not as important as for Fredholm equations, since Volterra equations are relatively easy to solve. However, there is an extensive literature on the subject. Several difficulties arise. First, any method that achieves higher order by operating on several quadrature points simultaneously will need a special method to get started, when values at the first few points are not yet known.

Second, stable quadrature rules can give rise to unexpected instabilities in integral equations. For example, suppose we try to replace the trapezoidal rule in the algorithm above with Simpson’s rule. Simpson’s rule naturally integrates over an interval $2 h$ , so we easily get the function values at the even mesh points. For the odd mesh points, we could try appending one panel of the trapezoidal rule. But to which end of the integration should we append it? We could do one step of the trapezoidal rule followed by all Simpson’s rule, or Simpson’s rule with one step of the trapezoidal rule at the end. Surprisingly, the former scheme is unstable, while the latter is fine!

A simple approach that can be used with the trapezoidal method given above is Richardson extrapolation: Compute the solution with stepsizes $h$ and $h / 2$ . Then, assuming the error scales with $h ^ { 2 }$ , compute

$$
f _ { \mathrm { E } } = { \frac { 4 f ( h / 2 ) - f ( h ) } { 3 } }
$$

This procedure can be repeated as with Romberg integration.

The general consensus is that the best of the higher-order methods is the blockby-block method (see [1]). Another important topic is the use of variable stepsize

methods, which are much more efficient if there are sharp features in $K$ or $f$ . Variable stepsize methods are quite a bit more complicated than their counterparts for differential equations; we refer you to the literature [1,2] for a discussion.

You should also be on the lookout for singularities in the integrand. If you find them, look to $\ S 1 9 . 3$ for additional ideas.

# CITED REFERENCES AND FURTHER READING:

Linz, P. 1985, Analytical and Numerical Methods for Volterra Equations (Philadelphia: S.I.A.M.).[1] Delves, L.M., and Mohamed, J.L. 1985, Computational Methods for Integral Equations (Cambridge, UK: Cambridge University Press).[2]

# 19.3 Integral Equations with Singular Kernels

Many integral equations have singularities in either the kernel or the solution or both. A simple quadrature method will show poor convergence with $N$ if such singularities are ignored. There is sometimes art in how singularities are best handled.

We start with a few straightforward suggestions:

1. Integrable singularities can often be removed by a change of variable. For example, the singular behavior $K ( t , s ) \sim s ^ { 1 / 2 }$ or $s ^ { - 1 / 2 }$ near $s = 0$ can be removed by the transformation $z = s ^ { 1 / 2 }$ . Note that we are assuming that the singular behavior is confined to $K$ whereas the quadrature actually involves the product $K ( t , s ) f ( s )$ , and it is this product that must be “fixed.” Ideally, you must deduce the singular nature of the product before you try a numerical solution, and take the appropriate action. Commonly, however, a singular kernel does not produce a singular solution $f ( t )$ . (The highly singular kernel $K ( t , s ) = \delta ( t - s )$ is simply the identity operator, for example.)

2. If $K ( t , s )$ can be factored as $\dot { w } ( s ) \overline { { K } } ( t , s )$ , where $w ( s )$ is singular and $\overline { { K } } ( t , s )$ is smooth, then a Gaussian quadrature based on $w ( s )$ as a weight function will work well. Even if the factorization is only approximate, the convergence is often improved dramatically. All you have to do is replace gauleg in the routine fred2 by another quadrature routine. Section 4.6 explained how to construct such quadratures; or you can find tabulated abscissas and weights in the standard references [1,2]. You must of course supply $\bar { K }$ instead of $K$ .

This method is a special case of the product Nystrom method [3,4], where one factors out a singular term $p ( t , s )$ depending on both $t$ and $s$ from $K$ and constructs suitable weights for its Gaussian quadrature. The calculations in the general case are quite cumbersome, because the weights depend on the chosen $\left\{ t _ { i } \right\}$ as well as the form of $p ( t , s )$ .

We prefer to implement the product Nystrom method on a uniform grid, with a quadrature scheme that generalizes the extended Simpson’s 3/8 rule (equation 4.1.5) to arbitrary weight functions. We discuss this in the subsections below.

3. Special quadrature formulas are also useful when the kernel is not strictly singular, but is “almost” so. One example is when the kernel is concentrated near $t = s$ on a scale much smaller than the scale on which the solution $f ( t )$ varies. In that case, a quadrature formula can be based on locally approximating $f ( s )$ by a polynomial or spline, while calculating the first few moments of the kernel $K ( t , s )$ at the tabulation points $t _ { i }$ . In such a scheme the narrow width of the kernel becomes an asset, rather than a liability: The quadrature becomes exact as the width of the kernel goes to zero.

4. An infinite range of integration is also a form of singularity. Truncating the range at a large finite value should be used only as a last resort. If the kernel goes rapidly to zero, then a Gauss-Laguerre $[ w \sim \exp ( - \alpha s ) ]$ or Gauss-Hermite $[ w \sim \exp ( - s ^ { \bar { 2 } } ) ]$ quadrature should work well. Long-tailed functions often succumb to the transformation

$$
s = \frac { 2 \alpha } { z + 1 } - \alpha
$$

which maps $0 < s < \infty$ to $1 > z > - 1$ so that Gauss-Legendre integration can be used. Here $\alpha > 0$ is a constant that you adjust to improve the convergence.

5. A common situation in practice is that $K ( t , s )$ is singular along the diagonal line $t = s$ . Here the Nystrom method fails completely because the kernel gets evaluated at $( t _ { i } , s _ { i } )$ . Subtraction of the singularity is one possible cure:

$$
\begin{array} { l } { \displaystyle \int _ { a } ^ { b } K ( t , s ) f ( s ) d s = \int _ { a } ^ { b } K ( t , s ) [ f ( s ) - f ( t ) ] d s + \int _ { a } ^ { b } K ( t , s ) f ( t ) d s } \\ { \displaystyle \qquad = \int _ { a } ^ { b } K ( t , s ) [ f ( s ) - f ( t ) ] d s + r ( t ) f ( t ) } \end{array}
$$

where $\textstyle r ( t ) = \int _ { a } ^ { b } K ( t , s ) d s$ is computed analytically or numerically. If the first term on the right-hand side is now regular, we can use the Nystrom method. Instead of equation (19.1.4), we get

$$
f _ { i } = \lambda \sum _ { { j = 0 } \atop { j \not = i } } ^ { N - 1 } w _ { j } K _ { i j } [ f _ { j } - f _ { i } ] + \lambda r _ { i } f _ { i } + g _ { i }
$$

Sometimes the subtraction process must be repeated before the kernel is completely regularized. See [3] for details. (And read on for a different, we think better, way to handle diagonal singularities.)

# 19.3.1 Quadrature on a Uniform Mesh with Arbitrary Weight

It is possible in general to find $n$ -point linear quadrature rules that approximate the integral of a function $f ( x )$ , times an arbitrary weight function $w ( x )$ , over an arbitrary range of integration $( a , b )$ , as the sum of weights times $n$ evenly spaced values of the function $f ( x )$ , say at $x = k h$ $k h , ( k + 1 ) h , \dots , ( k + n - 1 ) h$ . The general scheme for deriving such quadrature rules is to write down the $n$ linear equations that must be satisfied if the quadrature rule is to be exact for the $n$ functions $f ( x ) = \mathrm { c o n s t } , x , x ^ { 2 } , \ldots , x ^ { n - 1 }$ , and then solve these for the coefficients. This can be done analytically, once and for all, if the moments of the weight function over the same range of integration,

$$
W _ { n } \equiv \frac { 1 } { h ^ { n } } \int _ { a } ^ { b } x ^ { n } w ( x ) d x
$$

are assumed to be known. Here the prefactor $h ^ { - n }$ is chosen to make $W _ { n }$ scale as $h$ if (as in the usual case) $b - a$ is proportional to $h$ .

Carrying out this prescription for the four-point case gives the result

$$
\begin{array} { r l r } {  { \int _ { a } ^ { b } w ( x ) f ( x ) d x = } } \\ & { } & { \frac { 1 } { 6 } f ( k h ) \big [ ( k + 1 ) ( k + 2 ) ( k + 3 ) W _ { 0 } - ( 3 k ^ { 2 } + 1 2 k + 1 1 ) W _ { 1 } + 3 ( k + 2 ) W _ { 2 } - W _ { 3 } \big ] } \\ & { } & { +  \frac { 1 } { 2 } f ( [ k + 1 ] h ) \big [ - k ( k + 2 ) ( k + 3 ) W _ { 0 } + ( 3 k ^ { 2 } + 1 0 k + 6 ) W _ { 1 } - ( 3 k + 5 ) W _ { 2 } + W _ { 3 } \big ]  } \\ & { } & { +  \frac { 1 } { 2 } f ( [ k + 2 ] h ) \big [ k ( k + 1 ) ( k + 3 ) W _ { 0 } - ( 3 k ^ { 2 } + 8 k + 3 ) W _ { 1 } + ( 3 k + 4 ) W _ { 2 } - W _ { 3 } \big ]  } \\ & { } & {  +  \frac { 1 } { 6 } f ( [ k + 3 ] h ) \big [ - k ( k + 1 ) ( k + 2 ) W _ { 0 } + ( 3 k ^ { 2 } + 6 k + 2 ) W _ { 1 } - 3 ( k + 1 ) W _ { 2 } + W _ { 3 } \big ]   } \end{array}
$$

While the terms in brackets superficially appear to scale as $k ^ { 2 }$ , there is typically cancellation at both $O ( k ^ { 2 } )$ and $O ( k )$ .

Equation (19.3.5) can be specialized to various choices of $( a , b )$ . The obvious choice is $a = k \bar { h } , b = ( k + 3 ) h$ , in which case we get a four-point quadrature rule that generalizes

Simpson’s 3/8 rule (equation 4.1.5). In fact, we can recover this special case by setting $w ( x ) =$ 1, in which case (19.3.4) becomes

$$
W _ { n } = \frac { h } { n + 1 } [ ( k + 3 ) ^ { n + 1 } - k ^ { n + 1 } ]
$$

The four terms in square brackets in equation (19.3.5) each become independent of $k$ , and (19.3.5) in fact reduces to

$$
\int _ { k h } ^ { ( k + 3 ) h } f ( x ) d x = { \frac { 3 h } { 8 } } f ( k h ) + { \frac { 9 h } { 8 } } f ( [ k + 1 ] h ) + { \frac { 9 h } { 8 } } f ( [ k + 2 ] h ) + { \frac { 3 h } { 8 } } f ( [ k + 3 ] h )
$$

Back to the case of general $w ( x )$ , some other choices for $a$ and $b$ are also useful. For example, we may want to choose $( a , b )$ to be $( [ k + 1 ] h , [ k + 3 ] h )$ or $( [ k + 2 ] h , [ k + 3 ] h )$ , allowing us to finish off an extended rule whose number of intervals is not a multiple of three, without loss of accuracy: The integral will be estimated using the four values $f ( k h ) , \ldots , f ( [ k + 3 ] h )$ . Even more useful is to choose $( a , b )$ to be $( [ k + 1 ] h , [ k + 2 ] h )$ , thus using four points to integrate a centered single interval. These weights, when sewed together into an extended formula, give quadrature schemes that have smooth coefficients, i.e., without the Simpson-like $2 , 4 , 2 , 4 , 2$ alternation. (In fact, this was the technique that we used to derive equation 4.1.14, which you may now wish to re-examine.)

All these rules are of the same order as the extended Simpson’s rule, that is, exact for $f ( x )$ a cubic polynomial. Rules of lower order, if desired, are similarly obtained. The threepoint formula is

$$
\begin{array} { r l } { \displaystyle \int _ { a } ^ { b } w ( x ) f ( x ) d x = \frac { 1 } { 2 } f ( k h ) \big [ ( k + 1 ) ( k + 2 ) W _ { 0 } - ( 2 k + 3 ) W _ { 1 } + W _ { 2 } \big ] } \\ { + \left. f ( [ k + 1 ] h ) \big [ - k ( k + 2 ) W _ { 0 } + 2 ( k + 1 ) W _ { 1 } - W _ { 2 } \big ] \right. } \\ { + \left. \frac 1 2 f ( [ k + 2 ] h ) \big [ k ( k + 1 ) W _ { 0 } - ( 2 k + 1 ) W _ { 1 } + W _ { 2 } \big ] \right. } \end{array}
$$

Here the simple special case is to take $w ( x ) = 1$ , so that

$$
W _ { n } = \frac { h } { n + 1 } [ ( k + 2 ) ^ { n + 1 } - k ^ { n + 1 } ]
$$

Then equation (19.3.8) becomes Simpson’s rule,

$$
\int _ { k h } ^ { ( k + 2 ) h } f ( x ) d x = { \frac { h } { 3 } } f ( k h ) + { \frac { 4 h } { 3 } } f ( [ k + 1 ] h ) + { \frac { h } { 3 } } f ( [ k + 2 ] h )
$$

For nonconstant weight functions $w ( x )$ , however, equation (19.3.8) gives rules of one order less than Simpson, since they do not benefit from the extra symmetry of the constant case.

The two-point formula is simply

$$
\int _ { k h } ^ { ( k + 1 ) h } w ( x ) f ( x ) d x = f ( k h ) [ ( k + 1 ) W _ { 0 } - W _ { 1 } ] + f ( [ k + 1 ] h ) [ - k W _ { 0 } + W _ { 1 } ]
$$

Here is a routine Wwghts that uses the above formulas to compute an extended $N$ -point quadrature rule for the interval $( a , b ) = ( 0 , [ N - 1 ] h )$ . Input to Wwghts is a user-supplied object called quad in the routine. This object must contain a function kermom, which is called to get the first four indefinite-integral moments of $w ( x )$ , namely

$$
F _ { m } ( y ) \equiv \int ^ { y } s ^ { m } w ( s ) d s \qquad m = 0 , 1 , 2 , 3
$$

(The lower limit is arbitrary and can be chosen for convenience.) Cautionary note: When called with $N < 4$ , Wwghts returns a rule of lower order than Simpson; you should structure your problem to avoid this.

# template <class Q>

struct Wwghts {   
Constructs weights for the n-point equal-interval quadrature from 0 to $( \mathtt { n } \mathrm { - } 1 ) \mathtt { h }$ of a function $f ( x )$   
times an arbitrary (possibly singular) weight function $w ( x )$ . The indefinite-integral moments   
$F _ { n } ( y )$ of $w ( x )$ are provided by the user-supplied function kermom in the quad object. Doub h; Int n; $\sf { Q }$ &quad; VecDoub wghts; Wwghts(Doub hh, Int nn, Q &q) : h(hh), n(nn), quad(q), wghts(n) {} Constructor arguments are h, n, and the user-supplied quad object. VecDoub weights() This function returns the weights in wghts[0..n-1]. Int k; Doub fac; Doub hi=1.0/h; for (Int j=0;j<n;j++) Zero all the weights so we can sum into wghts[j]=0.0; them. if (n >= 4) { Use highest available order. VecDoub wold(4),wnew(4),w(4); wold=quad.kermom(0.0); Evaluate indefinite integrals at lower end. Doub $\mathtt { b } = 0 . 0$ ; For another problem, you might change for (Int j=0;j<n-3;j++) { this lower limit. Doub c=j; This is called $k$ in equation (19.3.5). Doub $\mathtt { a } \mathtt { = } \mathtt { b }$ ; Set upper and lower limits for this step. $b = a + h$ ; if $( \mathrm { j } \ = = \ \mathrm { n } - 4 ) \mathrm { b } = ( \mathrm { n } - 1 ) * \mathrm { h } ;$ Last interval: Go all the way to end. wnew=quad.kermom(b); for (fac ${ \tt = } 1$ .0, $\mathtt { k } = 0$ ;k<4;k++,fac\*=hi) Equation (19.3.4). w[k] $=$ (wnew[k]-wold[k])\*fac; wghts[j $\begin{array} { r l r } { \hat { \mathsf { J } } } & { { } + = } & { { \mathsf { ( } } ( ( ( \mathsf { c } + 1 \mathsf { . 0 } ) * ( \mathsf { c } + 2 \mathsf { . 0 } ) * ( \mathsf { c } + 3 \mathsf { . 0 } ) * _ { \mathsf { W } } [ 0 ] } \end{array}$ Equation (19.3.5). -(11.0+c\*(12.0+c\*3.0))\*w[1]+3.0\*(c+2.0)\*w[2]-w[3])/6.0); $\mathrm { w g h t s \left[ j + 1 \right] ~ } + = \mathrm { ~ } \left( \left( - \mathsf { c } \ast \left( \mathsf { c } + 2 . 0 \right) \ast \left( \mathsf { c } + 3 . 0 \right) \ast \mathsf { w } \left[ 0 \right] \right. \right.$ +(6.0+c\*(10.0+c\*3.0))\*w[1]-(3.0\*c+5.0)\*w[2]+w[3])\*0.5); wg $\mathrm { \bf ~ \hat { h t s } ~ [ j + 2 ] } \mathrm { \bf ~ \mathrel { + } } = \mathrm { \bf ~ \mathopen { } \mathclose \bgroup \left( \left( c \ast \left( c + 1 . 0 \right) \ast \left( c + 3 . 0 \right) \ast \mathrm { \bf { u } } \left[ 0 \right] \right. \right. }$ -(3.0+c\*(8.0+c\*3.0))\*w[1]+(3.0\*c+4.0)\*w[2]-w[3])\*0.5); wghts[j+3] $+ =$ ((-c\*(c+1.0)\*(c+2.0)\*w[0] +(2.0+c\*(6.0+c\*3.0))\*w[1]-3.0\*(c+1.0)\*w[2]+w[3])/6.0); for $\scriptstyle 1 = 0$ ;k<4;k++) wold[k] $=$ wnew[k]; Reset lower limits for moments. } else if $\mathbf { \chi } _ { \mathrm { ~ n ~ } } = = \mathbf { \chi } _ { 3 }$ ) { Lower-order cases; not recommended. VecDoub wold(3),wnew(3),w(3); wold=quad.kermom(0.0); wnew=quad.kermom(h+h); w[0] $=$ wnew[0]-wold[0]; w[1]=hi\*(wnew[1]-wold[1]); w[2]=hi\*hi\*(wnew[2]-wold[2]); wghts[0] $= _ { \mathrm { { w } } }$ [0]-1.5\*w[1]+0.5\*w[2]; wghts[1] $^ { = 2 }$ .0\*w[1]-w[2]; wghts[2] ${ = } 0$ .5\*(w[2]-w[1]); } else if $\mathbf { \bar { n } } \ = = \ 2$ ) { VecDoub wold(2),wnew(2),w(2); wold=quad.kermom(0.0); wnew=quad.kermom(h); wghts[0] $=$ wnew[0]-wold[0]-(wghts[1] $\risingdotseq$ hi\*(wnew[1]-wold[1])); return wghts; }   
};

We will now give an example of how to apply Wwghts to a singular integral equation.

# 19.3.2 Worked Example: A Diagonally Singular Kernel

As a particular example, consider the integral equation

$$
f ( x ) + \int _ { 0 } ^ { \pi } K ( x , y ) f ( y ) d y = \sin { x }
$$

with the (arbitrarily chosen) nasty kernel

$$
K ( x , y ) = \cos x \cos y \times \left\{ { \begin{array} { l l } { - \ln ( x - y ) } & { y < x } \\ { \sqrt { y - x } } & { y \geq x } \end{array} } \right.
$$

which has a logarithmic singularity on the left of the diagonal, combined with a square-root discontinuity on the right.

The first step is to do (analytically, in this case) the required moment integrals over the singular part of the kernel, equation (19.3.12). Since these integrals are done at a fixed value of $x$ , we can use $x$ as the lower limit. For any specified value of $y$ , the required indefinite integral is then either

or

$$
\begin{array} { l l l } { { F _ { m } ( y ; x ) = \displaystyle \int _ { x } ^ { y } s ^ { m } ( s - x ) ^ { 1 / 2 } d s ~ = \displaystyle \int _ { 0 } ^ { y - x } ( x + t ) ^ { m } t ^ { 1 / 2 } d t ~ } } & { { \mathrm { ~ i f ~ } y > x } } \\ { { \nonumber } } \\ { { F _ { m } ( y ; x ) = - \displaystyle \int _ { x } ^ { y } s ^ { m } \ln ( x - s ) d s = \displaystyle \int _ { 0 } ^ { x - y } ( x - t ) ^ { m } \ln t d t ~ } } & { { \mathrm { ~ i f ~ } y < x } } \end{array}
$$

(where a change of variable has been made in the second equality in each case). Doing these integrals analytically (e.g., using a symbolic integration package), we package the resulting formulas in the function kermom in the following routine, Quad_matrix. Note that $\mathsf { w } ( j + 1 )$ returns $F _ { j } ( y ; x )$ . The constructor of Quad_matrix calls Wwghts to get the quadrature weights and then constructs the quadrature matrix.

# struct Quad_matrix {

Constructs in a[0..n-1][0..n-1] the quadrature matrix for an example Fredholm equation of the second kind.

Int n;

Communicates with kermom.

Quad_matrix(MatDoub_O &a) : n(a.nrows())

The constructor obtains the quadrature weights that integrate the singular part of the kernel via calls to Wwghts. It then sums the weights with the nonsingular part of the kernel to obtain the quadrature matrix.

const Doub $\mathtt { P I } = 3$ .14159263589793238;   
VecDoub wt(n);   
Doub h=PI/(n-1);   
Wwghts<Quad_matrix> w(h,n,\*this);   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j $^ { + + }$ ) { x=j\*h; Set x for kermom. wt=w.weights(); Doub cx=cos(x); Part of nonsingular kernel. for (Int $\mathtt { k } = 0$ ;k<n;k $^ { + + }$ ) Put together all the pieces of the kernel. a[j][k] $=$ wt[k]\*cx\*cos(k\*h); ++a[j][j]; For equations of the second kind, there is a diagonal   
} piece independent of $h$ .

# }

# VecDoub kermom(const Doub y)

Returns $\mathtt { w } \left[ 0 \dots \dots \dots 1 \right]$ , the first m indefinite-integral moments of one row of the singular part of the kernel. (For this example, m is hard-wired to be 4.) The input variable y labels the column, while the member variable $\mathbf { x }$ is the row. We can take $\mathbf { x }$ as the lower limit of integration. Thus, we return the moment integrals either purely to the left or purely to the right of the diagonal.

Doub d,df,clog,x2,x3,x4,y2; VecDoub w(4); if $( \mathbb { y } ) = \textbf { x } )$ ) { $\scriptstyle { \mathsf { d } } = { \boldsymbol { \mathsf { y } } } - { \boldsymbol { \mathsf { x } } }$ ; df=2.0\*sqrt(d)\*d; w[0]=df/3.0; w[1]=df\*(x/3.0+d/5.0); w[2]=df\*((x/3.0 + 0.4\*d)\*x + d\*d/7.0); w[3]=df\*(((x/3.0 + 0.6\*d)\*x + 3.0\*d\*d/7.0)\*x+d\*d\*d/9.0); } else { $\mathbf { x } 3 = \left( \mathbf { x } 2 \mathbf { = x } { \ast } \mathbf { x } \right) { \ast } \mathbf { x } ;$ $_ { \tt X } 4 { = } _ { \tt X } 2 * _ { \tt X } 2$ ; y2=y\*y; $\scriptstyle \mathtt { d } = \mathbf { x } - \mathbf { y }$ ; w[0]=d\*((clog=log(d))-1.0); $\begin{array} { r l r } { \mathbf { w } \left[ 1 \right] } & { { } = } & { - 0 . 2 5 * \left( 3 \cdot 0 * \mathbf { x } + \mathbf { y } ^ { - } 2 . 0 * \mathbf { c } 1 \circ \mathbf { g } * \left( \mathbf { x } + \mathbf { y } \right) \right) * \mathbf { d } } \end{array}$ ; w[2]=(-11.0\*x3+y\*(6.0\*x2+y\*(3.0\*x+2.0\*y)) +6.0\*clog\*(x3-y\*y2))/18.0; $\mathtt { w } \left[ 3 \right] = ( - 2 5 . 0 * \mathtt { x } 4 + \mathtt { y } * ( 1 2 . 0 * \mathtt { x } 3 + \mathtt { y } * ( 6 . 0 * \mathtt { x } 2 + \mathtt { y } * ( 4 . 0 * \mathtt { x } 4 ) ) ) .$ (4.0\*x+3.0\*y)))+12.0\*clog\*(x4-(y2\*y2)))/48.0; } return w; }

Finally, we solve the linear system for any particular right-hand side, here sin $x$ .

# Int main_fredex(void)

This sample program shows how to solve a Fredholm equation of the second kind using the product Nystrom method and a quadrature rule especially constructed for a particular, singular, kernel.

const Int $\mathtt { N = 4 0 }$ ; Here the size of the grid is specified.   
const Doub $\mathtt { P I } = 3$ .141592653589793238;   
VecDoub g(N);   
MatDoub a(N,N);   
Quad_matrix qmx(a); Make the quadrature matrix; all the action is here.   
LUdcmp alu(a); Decompose the matrix.   
for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<N;j++) Construct the right-hand side, here sin $x$ . g[j] $=$ sin(j\*PI/(N-1));   
alu.solve(g,g); Backsubstitute.   
for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<N; $\mid + +$ ) { Write out the solution. Doub x=j\*PI/(N-1); cout $< <$ fixed $< <$ setprecision(2) << setw(6) $< < \mathrm { ( j + 1 ) }$ ; cout $< <$ setprecision(6) << setw(13) << x << setw(13) << g[j] << endl;   
}   
return 0;

With $N = 4 0$ , this program gives accuracy at about the $1 0 ^ { - 5 }$ level. The accuracy increases as $N ^ { 4 }$ (as it should for our Simpson-order quadrature scheme) despite the highly singular kernel. Figure 19.3.1 shows the solution obtained, also plotting the solution for smaller values of $N$ , which are themselves seen to be remarkably faithful. Notice that the solution is smooth, even though the kernel is singular, a common occurrence.

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands.[1]   
Stroud, A.H., and Secrest, D. 1966, Gaussian Quadrature Formulas (Englewood Cliffs, NJ: Prentice-Hall).[2]   
Delves, L.M., and Mohamed, J.L. 1985, Computational Methods for Integral Equations (Cambridge, UK: Cambridge University Press).[3]   
Atkinson, K.E. 1976, A Survey of Numerical Methods for the Solution of Fredholm Integral Equations of the Second Kind (Philadelphia: S.I.A.M.).[4]

![](images/64d33d3d7479f08eaabb6def151d3605f5d09abe82b05894d077bc3b6b14cff4.jpg)  
Figure 19.3.1. Solution of the example integral equation (19.3.14) with grid sizes $N = 1 0$ , 20, and 40. The tabulated solution values have been connected by straight lines; in practice, one would interpolate a small $N$ solution more smoothly.

# 19.4 Inverse Problems and the Use of A Priori Information

Later discussion will be facilitated by some preliminary mention of a couple of mathematical points. Suppose that $\mathbf { u }$ is an “unknown” vector that we plan to determine by some minimization principle. Let $\mathbf { \mathcal { A } } [ \mathbf { u } ] > 0$ and $\mathcal { B } [ { \bf u } ] > 0$ be two positive functionals of $\mathbf { u }$ , so that we can try to determine $\mathbf { u }$ by either

$$
\mathrm { m i n i m i z e : } \quad \mathbf { \mathcal { A } } [ \mathbf { u } ] \qquad \mathrm { o r } \qquad \mathrm { m i n i m i z e : } \quad \mathbf { \mathcal { B } } [ \mathbf { u } ]
$$

(Of course these will generally give different answers for $\mathbf { u }$ .) As another possibility, now suppose that we want to minimize $\mathcal { A } [ \mathbf { u } ]$ subject to the constraint that $\mathcal { B } [ \mathbf { u } ]$ have some particular value, say $b$ . The method of Lagrange multipliers gives the variation

$$
{ \frac { \delta } { \delta \mathbf { u } } } \left\{ { \mathcal { A } } [ \mathbf { u } ] + \lambda _ { 1 } ( { \mathcal { B } } [ \mathbf { u } ] - b ) \right\} = { \frac { \delta } { \delta \mathbf { u } } } \left( { \mathcal { A } } [ \mathbf { u } ] + \lambda _ { 1 } { \mathcal { B } } [ \mathbf { u } ] \right) = 0
$$

where $\lambda _ { 1 }$ is a Lagrange multiplier. Notice that $b$ is absent in the second equality, since it doesn’t depend on $\mathbf { u }$ .

Next, suppose that we change our minds and decide to minimize $\mathcal { B } [ \mathbf { u } ]$ subject to the constraint that $\mathcal { A } [ \mathbf { u } ]$ have a particular value, $a$ . Instead of equation (19.4.2) we

have

$$
\frac { \delta } { \delta \mathbf { u } } \left\{ \mathcal { B } [ \mathbf { u } ] + \lambda _ { 2 } ( \mathcal { A } [ \mathbf { u } ] - a ) \right\} = \frac { \delta } { \delta \mathbf { u } } \left( \mathcal { B } [ \mathbf { u } ] + \lambda _ { 2 } \mathcal { A } [ \mathbf { u } ] \right) = 0
$$

with, this time, $\lambda _ { 2 }$ the Lagrange multiplier. Multiplying equation (19.4.3) by the constant $1 / \lambda _ { 2 }$ , and identifying $1 / \lambda _ { 2 }$ with $\lambda _ { 1 }$ , we see that the actual variations are exactly the same in the two cases. Both cases will yield the same one-parameter family of solutions, say ${ \bf u } ( \lambda _ { 1 } )$ . As $\lambda _ { 1 }$ varies from 0 to $\infty$ , the solution ${ \bf u } ( \lambda _ { 1 } )$ varies along a so-called trade-off curve between the problem of minimizing $\mathcal { A }$ and the problem of minimizing $\mathcal { B }$ . Any solution along this curve can equally well be thought of as either (i) a minimization of $\mathcal { A }$ for some constrained value of $\mathcal { B }$ , or (ii) a minimization of $\mathcal { B }$ for some constrained value of $\mathcal { A }$ , or (iii) a weighted minimization of the sum $\mathcal { A } + \lambda _ { 1 } \mathcal { B }$ .

The second preliminary point has to do with degenerate minimization principles. In the example above, now suppose that $\mathcal { A } [ \mathbf { u } ]$ has the particular form

$$
\mathcal { A } [ \mathbf { u } ] = | \mathbf { A } \cdot \mathbf { u } - \mathbf { c } | ^ { 2 }
$$

for some matrix A and vector c. If A has fewer rows than columns, or if $\mathbf { A }$ is square but degenerate (has a nontrivial nullspace; see $\ S 2 . 6$ , especially Figure 2.6.1), then minimizing $\mathcal { A } [ \mathbf { u } ]$ will not give a unique solution for $\mathbf { u }$ . (To see why, review $\ S 1 5 . 4$ , and note that for a “design matrix” A with fewer rows than columns, the matrix $\mathbf { A } ^ { T } \cdot \mathbf { A }$ in the normal equations 15.4.10 is degenerate.) However, if we add any multiple $\lambda$ times a nondegenerate quadratic form $\mathcal { B } [ \mathbf { u } ]$ , for example $\mathbf { u } \cdot \mathbf { H } \cdot \mathbf { u }$ with $\mathbf { H }$ a positive-definite matrix, then minimization of $\mathcal { A } [ \mathbf { u } ] + \lambda \mathcal { B } [ \mathbf { u } ]$ will lead to a unique solution for u. (The sum of two quadratic forms is itself a quadratic form, with the second piece guaranteeing nondegeneracy.)

We can combine these two points, for this conclusion: When a quadratic minimization principle is combined with a quadratic constraint, and both are positive, only one of the two need be nondegenerate for the overall problem to be well-posed. We are now equipped to face the subject of inverse problems.

# 19.4.1 The Inverse Problem with Zeroth-Order Regularization

Suppose that $u ( x )$ is some unknown or underlying ( $u$ stands for both unknown and underlying!) physical process, which we hope to determine by a set of $N$ measurements $c _ { i }$ $\mathbf { \Phi } _ { ; , } i = 0 , 1 , \dots , N - 1$ . The relation between $u ( x )$ and the $c _ { i }$ ’s is that each $c _ { i }$ measures a (hopefully distinct) aspect of $u ( x )$ through its own linear response kernel $r _ { i }$ , and with its own measurement error $n _ { i }$ . In other words,

$$
c _ { i } \equiv s _ { i } + n _ { i } = \int r _ { i } ( x ) u ( x ) d x + n _ { i }
$$

(compare this to equations 13.3.1 and 13.3.2). Within the assumption of linearity, this is quite a general formulation. The $c _ { i }$ ’s might approximate values of $u ( x )$ at certain locations $x _ { i }$ , in which case $r _ { i } ( x )$ would have the form of a more or less narrow instrumental response centered around $x = x _ { i }$ . Or, the $c _ { i }$ ’s might “live” in an entirely different function space from $u ( x )$ , measuring different Fourier components of $u ( x )$ , for example.

The inverse problem is, given the $c _ { i }$ ’s, the $r _ { i } ( x )$ ’s, and perhaps some information about the errors $n _ { i }$ such as their covariance matrix,

$$
S _ { i j } \equiv { \bf C o v a r } [ n _ { i } , n _ { j } ]
$$

how do we find a good statistical estimator of $u ( x )$ , call it ${ \widehat { u } } ( x )$ ?

It should be obvious that this is an ill-posed problem. After all, how can we reconstruct a whole function ${ \widehat { u } } ( x )$ from only a finite number of discrete values $c _ { i }$ ? Yet, whether formally or informally, we do this all the time in science. We routinely measure “enough points” and then “draw a curve through them.” In doing so, we are making some assumptions, either about the underlying function $u ( x )$ , or about the nature of the response functions $r _ { i } ( x )$ , or both. Our purpose now is to formalize these assumptions, and to extend our abilities to cases where the measurements and underlying function live in quite different function spaces. (How do you “draw a curve” through a scattering of Fourier coefficients?)

We can’t really want every point $x$ of the function ${ \widehat { u } } ( x )$ . We do want some large number $M$ of discrete points $x _ { \mu }$ , $\mu = 0 , 1 , \ldots , M - 1$ , where $M$ is sufficiently large, and the $x _ { \mu }$ ’s are sufficiently evenly spaced, that neither $u ( x )$ nor $r _ { i } ( x )$ varies much between any $x _ { \mu }$ and $x _ { \mu + 1 }$ . (Here and following we will use Greek letters like $\mu$ to denote values in the space of the underlying process, and Roman letters like $i$ to denote values of immediate observables.) For such a dense set of $x _ { \mu }$ ’s, we can replace equation (19.4.5) by a quadrature like

$$
c _ { i } = \sum _ { \mu } R _ { i \mu } u ( x _ { \mu } ) + n _ { i }
$$

where the $N \times M$ matrix $\mathbf { R }$ has components

$$
R _ { i \mu } \equiv r _ { i } ( x _ { \mu } ) ( x _ { \mu + 1 } - x _ { \mu - 1 } ) / 2
$$

(or any other simple quadrature — it rarely matters which). We will view equations (19.4.5) and (19.4.7) as being equivalent for practical purposes.

How do you solve a set of equations like equation (19.4.7) for the unknown $u ( x _ { \mu } )$ ’s? Here is a bad way, but one that contains the germ of some correct ideas: Form a $\chi ^ { 2 }$ measure of how well a model $u ( x )$ agrees with the measured data,

$$
\begin{array} { l } { { \displaystyle \chi ^ { 2 } = \sum _ { i = 0 } ^ { N - 1 } \sum _ { j = 0 } ^ { N - 1 } \left[ c _ { i } - \sum _ { \mu = 0 } ^ { M - 1 } R _ { i \mu } u ( x _ { \mu } ) \right] S _ { i j } ^ { - 1 } \left[ c _ { j } - \sum _ { \mu = 0 } ^ { M - 1 } R _ { j \mu } u ( x _ { \mu } ) \right] } } \\ { { \displaystyle \approx \sum _ { i = 0 } ^ { N - 1 } \left[ \frac { c _ { i } - \sum _ { \mu = 0 } ^ { M - 1 } R _ { i \mu } u ( x _ { \mu } ) } { \sigma _ { i } } \right] ^ { 2 } } } \end{array}
$$

(compare with equation 15.1.6). Here $\mathbf { S } ^ { - 1 }$ is the inverse of the covariance matrix, and the approximate equality holds if you can neglect the off-diagonal covariances, with $\sigma _ { i } \equiv \mathsf { \bar { ( C o v a r } } [ i , i ] ) ^ { \bar { 1 } / 2 }$ .

Now you can use the method of singular value decomposition (SVD) in $\ S 1 5 . 4$ to find the vector $\mathbf { u }$ that minimizes equation (19.4.9). Don’t try to use the method of normal equations; since $M$ is greater than $N$ , they will be singular, as we already discussed. The SVD process will thus surely find a large number of zero singular values, indicative of a highly nonunique solution. Among the infinity of degenerate solutions (most of them badly behaved with arbitrarily large $u ( x _ { \mu } )$ ’s) SVD will select the one of them, call it $\widehat { \mathbf { u } }$ , with the smallest norm $| \widehat { \mathbf { u } } |$ in the sense of

$$
\sum _ { \mu } [ \widehat { u } ( x _ { \mu } ) ] ^ { 2 } \quad \mathrm { a \ m i n i m u m }
$$

(look at Figure 2.6.1). This solution is often called the principal solution. It is a limiting case of what is called zeroth-order regularization, corresponding to minimizing the sum of the two positive functionals

$$
\widehat { \mathbf { u } } \operatorname* { m i n i m i z e s : } \quad \chi ^ { 2 } [ \mathbf { u } ] + \lambda ( \mathbf { u } \cdot \mathbf { u } )
$$

in the limit of small $\lambda$ . Below, we will learn how to do such minimizations, as well as more general ones, without the ad hoc use of SVD.

What happens if we determine $\widehat { \mathbf { u } }$ by equation (19.4.11) with a non-infinitesimal value of $\lambda ?$ First, note that if $M \gg N$ (many more unknowns than equations), then $\mathbf { u }$ will often have enough freedom to be able to make $\chi ^ { 2 }$ (equation 19.4.9) quite unrealistically small, if not zero. In the language of $\ S 1 5 . 1$ , the number of degrees of freedom $\nu = N - M$ , which is approximately the expected value of $\chi ^ { 2 }$ when $\nu$ is large, is being driven down to zero (and, not meaningfully, beyond). Yet, we know that for the true underlying function $u ( x )$ , which has no adjustable parameters, the number of degrees of freedom and the expected value of $\chi ^ { 2 }$ should be about $\nu \approx N$ .

Increasing $\lambda$ pulls the solution away from minimizing $\chi ^ { 2 }$ in favor of minimizing $\widehat { \mathbf { u } } \cdot \widehat { \mathbf { u } }$ . From the preliminary discussion above, we can view this as minimizing $\widehat { \mathbf { u } } \cdot \widehat { \mathbf { u } }$ subject to the constraint that $\chi ^ { 2 }$ have some constant nonzero value. A popular choice, in fact, is to find that value of $\lambda$ which yields $\chi ^ { 2 } = N$ , that is, to get about as much extra regularization as a plausible value of $\chi ^ { 2 }$ dictates. The resulting ${ \widehat { u } } ( x )$ is called the solution of the inverse problem with zeroth-order regularization.

The value $N$ is actually a surrogate for any value drawn from a Gaussian distribution with mean $N$ and standard deviation $( 2 N ) ^ { 1 / 2 }$ (the asymptotic $\chi ^ { 2 }$ distribution). One might equally plausibly try two values of $\lambda$ , one giving $\chi ^ { 2 } = N +$ $( 2 N ) ^ { 1 / 2 }$ , the other $N - ( 2 N ) ^ { 1 / 2 }$ .

Zeroth-order regularization, though dominated by better methods, demonstrates most of the basic ideas that are used in inverse problem theory. In general, there are two positive functionals, call them $\mathcal { A }$ and $\mathcal { B }$ . The first, $\mathcal { A }$ , measures something like the agreement of a model to the data (e.g., $\chi ^ { 2 }$ ), or sometimes a related quantity like the “sharpness” of the mapping between the solution and the underlying function. When $\mathcal { A }$ by itself is minimized, the agreement or sharpness becomes very good (often impossibly good), but the solution becomes unstable, wildly oscillating, or in other ways unrealistic, reflecting that $\mathcal { A }$ alone typically defines a highly degenerate minimization problem.

That is where $\mathcal { B }$ comes in. It measures something like the “smoothness” of the desired solution, or sometimes a related quantity that parametrizes the stability of the solution with respect to variations in the data, or sometimes a quantity reflecting a priori judgments about the likelihood of a solution. $\mathcal { B }$ is called the stabilizing functional or regularizing operator. In any case, minimizing $\mathcal { B }$ by itself is supposed to give a solution that is “smooth” or “stable” or “likely” — and that has nothing at all to do with the measured data.

![](images/eb945e005355474d7e977e4e335c20871dcfaa89e8b733497626084eaac49d1b.jpg)  
Figure 19.4.1. Almost all inverse problem methods involve a trade-off between two optimizations: agreement between data and solution, or “sharpness” of mapping between true and estimated solutions (here denoted $\mathcal { A }$ ), and smoothness or stability of the solution (here denoted $\mathcal { B }$ ). Among all possible solutions, shown here schematically as the shaded region, those on the boundary connecting the unconstrained minimum of $\mathcal { A }$ and the unconstrained minimum of $\mathcal { B }$ are the “best” solutions, in the sense that every other solution is dominated by at least one solution on the curve.

The single central idea in inverse theory is the prescription

$$
\begin{array} { r l } { \operatorname* { m i n i m i z e : } } & { { } \mathcal { A } + \lambda \mathcal { B } } \end{array}
$$

for various values of $0 < \lambda < \infty$ along the so-called trade-off curve (see Figure 19.4.1), and then to settle on a “best” value of $\lambda$ by one or another criterion, ranging from fairly objective (e.g., making $\chi ^ { 2 } = N$ ) to entirely subjective. Successful methods, several of which we will now describe, differ as to their choices of $\mathcal { A }$ and $\mathcal { B }$ , as to whether the prescription (19.4.12) yields linear or nonlinear equations, as to their recommended method for selecting a final $\lambda$ , and as to their practicality for computer-intensive two-dimensional problems like image processing.

Equation (19.4.12) has a natural Bayesian interpretation that gives some additional insight. Given the data points c and measurements $\mathbf { u }$ , we can use Bayes’ law, equation (15.0.1), to write

$$
P ( \mathbf { u } | \mathbf { c } , I ) \propto P ( \mathbf { c } | \mathbf { u } , I ) P ( \mathbf { u } | I )
$$

where $P ( \mathbf { u } | I )$ is the Bayesian prior on $\mathbf { u }$ before we see any data, given any background information $I$ . Often, we can usefully write the right-hand side as the product of two exponentials, that is,

$$
P ( \mathbf { c } | \mathbf { u } , I ) \equiv e ^ { - \mathcal { A } ( \mathbf { c } , \mathbf { u } ) } , \qquad P ( \mathbf { u } | I ) \equiv e ^ { - \lambda \mathcal { B } ( \mathbf { u } ) }
$$

For example, if the measurement errors are distributed as a multivariate Gaussian, then equation (19.4.9) implies

$$
{ \mathcal A } = \textstyle \frac { 1 } { 2 } \chi ^ { 2 } ( { \bf c } , { \bf u } )
$$

while a Bayesian prior expressing the belief that $\mathbf { u }$ should not have wild, largeamplitude oscillations might be captured by the multivariate Gaussian prior

$$
\mathcal { B } = \lambda ( \mathbf { u } \cdot \mathbf { u } )
$$

Maximizing $P ( \mathbf { u } | \mathbf { c } , I )$ to find the most probable $\widehat { \mathbf { u } }$ is now exactly equivalent to equation (19.4.11). The constant $\lambda$ is now merely a convenient parameterization for the narrowness of the Gaussian prior. It acts as a trade-off parameter, exactly as described above. In subsequent sections we will learn how to devise more sophisticated smoothness priors. In several cases these will be positive-definite quadratic forms in $\mathbf { u }$ ; those cases correspond to more complicated multivariate Gaussian priors on u. In $\ S 1 9 . 7$ we will meet a prior that is not exactly Gaussian, but rather based on the concept of entropy.

Within the Bayesian framework, you can do more than just solve for the most likely model uy. For example, you can use Markov chain Monte Carlo (-15.8) to sample from the distribution of u’s given the observed data.

# CITED REFERENCES AND FURTHER READING:

Craig, I.J.D., and Brown, J.C. 1986, Inverse Problems in Astronomy (Bristol, UK: Adam Hilger).   
Twomey, S. 1977, Introduction to the Mathematics of Inversion in Remote Sensing and Indirect Measurements (Amsterdam: Elsevier).   
Tikhonov, A.N., and Arsenin, V.Y. 1977, Solutions of Ill-Posed Problems (New York: Wiley).   
Tikhonov, A.N., and Goncharsky, A.V. (eds.) 1987, Ill-Posed Problems in the Natural Sciences (Moscow: MIR).   
Parker, R.L. 1977, “Understanding Inverse Theory,” Annual Review of Earth and Planetary Science, vol.5, pp.35-64.   
Frieden, B.R. 1975, in Picture Processing and Digital Filtering, T.S. Huang, ed. (New York: Springer).   
Tarantola, A. 1995, Inverse Problem Theory and Methods for Model Parameter Estimation (Philadelphia: S.I.A.M.). Also available at http://www.ipgp.jussieu.fr/\~tarantola/ Files/Professional/SIAM.   
Baumeister, J. 1987, Stable Solution of Inverse Problems (Braunschweig, Germany: Friedr. Vieweg) [mathematically oriented].   
Titterington, D.M. 1985, “General Structure of Regularization Procedures in Image Reconstruction,” Astronomy and Astrophysics, vol. 144, pp. 381–387.   
Jeffrey, W., and Rosner, R. 1986, “On Strategies for Inverting Remote Sensing Data,” Astrophysical Journal, vol.310, pp. 463-472.

# 19.5 Linear Regularization Methods

What we will call linear regularization is also called the Phillips-Twomey method [1,2], the constrained linear inversion method [3], the method of regularization [4], and Tikhonov-Miller regularization [5-7]. (It probably has other names also, since it is so obviously a good idea.) In its simplest form, the method is an immediate generalization of zeroth-order regularization (equation 19.4.11, above). As before, the functional $\mathcal { A }$ is taken to be the $\chi ^ { 2 }$ deviation, equation (19.4.9), but the functional $\mathcal { B }$ is replaced by more sophisticated measures of smoothness that derive from first or higher derivatives.

For example, suppose that your a priori belief is that a credible $u ( x )$ is not too different from a constant. Then a reasonable functional to minimize is

$$
\mathcal { B } \propto \int [ \widehat { u } ^ { \prime } ( x ) ] ^ { 2 } d x \propto \sum _ { \mu = 0 } ^ { M - 2 } [ \widehat { u } _ { \mu } - \widehat { u } _ { \mu + 1 } ] ^ { 2 }
$$

since it is nonnegative and equal to zero only when ${ \widehat { u } } ( x )$ is constant. Here $\widehat { u } _ { \mu } \equiv$ $\widehat { \boldsymbol { u } } ( \boldsymbol { x } _ { \mu } )$ , and the second equality (proportionality) assumes that the $x _ { \mu }$ ’s are uniformly spaced. We can write the second form of $\mathcal { B }$ as

$$
\mathcal { B } = | \mathbf { B } \cdot \widehat { \mathbf { u } } | ^ { 2 } = \widehat { \mathbf { u } } \cdot ( \mathbf { B } ^ { T } \cdot \mathbf { B } ) \cdot \widehat { \mathbf { u } } \equiv \widehat { \mathbf { u } } \cdot \mathbf { H } \cdot \widehat { \mathbf { u } }
$$

where $\widehat { \mathbf { u } }$ is the vector of components $\widehat { u } _ { \mu } , ~ \mu = 0 , \ldots , M - 1 ; \mathbf { B }$ is the $( M - 1 ) \times M$ first difference matrix

$$
\mathbf { B } = \left( \begin{array} { c c c c c c c c c } { - 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { - 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { \vdots } & { } & { } & { } & { \ddots } & { } & { } & { } & { \vdots } \\ { 0 } & { \cdots } & { 0 } & { 0 } & { 0 } & { 0 } & { - 1 } & { 1 } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { - 1 } & { 1 } \end{array} \right)
$$

and $\mathbf { H }$ is the $M \times M$ matrix

$$
\mathbf { H } = \mathbf { B } ^ { T } \cdot \mathbf { B } = { \left( \begin{array} { l l l l l l l l l } { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { { - 1 } } & { { 2 } } & { { - 1 } } & { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { { - 1 } } & { { 2 } } & { { - 1 } } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { { \vdots } } & { { } } & { { } } & { { \ddots } } & { } & { } & { { \vdots } } \\ { 0 } & { { \cdots } } & { { 0 } } & { 0 } & { 0 } & { { - 1 } } & { { 2 } } & { { - 1 } } & { 0 } \\ { 0 } & { { \cdots } } & { { 0 } } & { 0 } & { 0 } & { 0 } & { { - 1 } } & { { 2 } } & { { - 1 } } \\ { 0 } & { { \cdots } } & { { 0 } } & { 0 } & { 0 } & { 0 } & { 0 } & { { - 1 } } & { { 1 } } \end{array} \right) }
$$

Note that $\mathbf { B }$ has one fewer row than column. It follows that the symmetric $\mathbf { H }$ is degenerate; it has exactly one zero eigenvalue corresponding to the value of a constant function, any one of which makes $\mathcal { B }$ exactly zero.

If, just as in $\ S 1 5 . 4$ , we write

$$
A _ { i \mu } \equiv R _ { i \mu } / \sigma _ { i } b _ { i } \equiv c _ { i } / \sigma _ { i }
$$

then, using equation (19.4.9), the minimization principle (19.4.12) is

$$
\mathrm { m i n i m i z e : ~ \boldsymbol { \mathcal { A } } + \lambda \mathcal { B } = | \mathbf { A } \cdot \widehat { \mathbf { u } } - \mathbf { b } | ^ { 2 } + \lambda \widehat { \mathbf { u } } \cdot \mathbf { H } \cdot \widehat { \mathbf { u } } }
$$

This can readily be reduced to a linear set of normal equations, just as in $\ S 1 5 . 4$ : The components $\widehat { u } _ { \mu }$ of the solution satisfy the set of $M$ equations in $M$ unknowns,

$$
\sum _ { \rho } \biggl [ \Bigl ( \sum _ { i } A _ { i \mu } A _ { i \rho } \Bigr ) + \lambda H _ { \mu \rho } \biggr ] \hat { u } _ { \rho } = \sum _ { i } A _ { i \mu } b _ { i } \qquad \mu = 0 , 1 , \ldots , M - 1
$$

or, in vector notation,

$$
( \mathbf { A } ^ { T } \cdot \mathbf { A } + \lambda \mathbf { H } ) \cdot \widehat { \mathbf { u } } = \mathbf { A } ^ { T } \cdot \mathbf { b }
$$

Equations (19.5.7) or (19.5.8) can be solved by the standard techniques of Chapter 2, e.g., $L U$ decomposition. The usual warnings about normal equations being illconditioned do not apply, since the whole purpose of the $\lambda$ term is to cure that same ill-conditioning. Note, however, that the $\lambda$ term by itself is ill-conditioned, since it does not select a preferred constant value. You hope your data can at least do that!

Although inversion of the matrix $( \mathbf { A } ^ { T } \cdot \mathbf { A } + \mathbf { \bar { \lambda } } \mathbf { \bar { H } } )$ is not generally the best way to solve for $\widehat { \mathbf { u } }$ , let us digress to write the solution to equation (19.5.8) schematically as

$$
\widehat { \mathbf { u } } = \left( \frac { 1 } { \mathbf { A } ^ { T } \cdot \mathbf { A } + \lambda \mathbf { H } } \cdot \mathbf { A } ^ { T } \cdot \mathbf { A } \right) \mathbf { A } ^ { - 1 } \cdot \mathbf { b }
$$

where the identity matrix in the form $\mathbf { A \cdot A } ^ { - 1 }$ has been inserted. This is schematic not only because the matrix inverse is fancifully written as a denominator, but also because, in general, the inverse matrix $\mathbf { A } ^ { - 1 }$ does not exist. However, it is illuminating to compare equation (19.5.9) with equation (13.3.6) for optimal or Wiener filtering, or with equation (13.6.6) for general linear prediction. (The concepts of $\ S 1 5 . 9$ are also related.) One sees that $\bar { \mathbf { A } ^ { T } } \cdot \mathbf { A }$ plays the role of $S ^ { 2 }$ , the signal power or autocorrelation, while $\lambda \mathbf { H }$ plays the role of $N ^ { 2 }$ , the noise power or autocorrelation. The term in parentheses in equation (19.5.9) is something like an optimal filter, whose effect is to pass the ill-posed inverse $\mathbf { A } ^ { - 1 } \cdot \mathbf { b }$ through unmodified when $\mathbf { A } ^ { T } \cdot \mathbf { A }$ is sufficiently large, but to suppress it when $\mathbf { A } ^ { T } \cdot \mathbf { A }$ is small.

The above choices of $\mathbf { B }$ and $\mathbf { H }$ are only the simplest in an obvious sequence of derivatives. If your a priori belief is that a linear function is a good approximation to $u ( x )$ , then minimize

$$
\mathcal { B } \propto \int [ \widehat { u } ^ { \prime \prime } ( x ) ] ^ { 2 } d x \propto \sum _ { \mu = 0 } ^ { M - 3 } [ - \widehat { u } _ { \mu } + 2 \widehat { u } _ { \mu + 1 } - \widehat { u } _ { \mu + 2 } ] ^ { 2 }
$$

implying

$$
\mathbf { B } = \left( \begin{array} { c c c c c c c c c } { - 1 } & { 2 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { - 1 } & { 2 } & { - 1 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { \vdots } & { } & { } & { } & { \ddots } & { } & { } & { \vdots } \\ { 0 } & { \cdots } & { 0 } & { 0 } & { 0 } & { - 1 } & { 2 } & { - 1 } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { 0 } & { 0 } & { 0 } & { - 1 } & { 2 } & { - 1 } \end{array} \right)
$$

and

$$
\mathbf { H } = \mathbf { B } ^ { T } \cdot \mathbf { B } = { \left( \begin{array} { l l l l l l l l l l } { 1 } & { - 2 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { - 2 } & { 5 } & { - 4 } & { 1 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { 1 } & { - 4 } & { 6 } & { - 4 } & { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { 1 } & { - 4 } & { 6 } & { - 4 } & { 1 } & { 0 } & { \cdots } & { 0 } \\ { \vdots } & { } & { } & { \ddots } & { } & { } & { \vdots } \\ { 0 } & { \cdots } & { 0 } & { 1 } & { - 4 } & { 6 } & { - 4 } & { 1 } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { 0 } & { 1 } & { - 4 } & { 6 } & { - 4 } & { 1 } \\ { 0 } & { \cdots } & { 0 } & { 0 } & { 0 } & { 1 } & { - 4 } & { 5 } & { - 2 } \\ { 0 } & { \cdots } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { - 2 } & { 1 } \end{array} \right) }
$$

This $\mathbf { H }$ has two zero eigenvalues, corresponding to the two undetermined parameters of a linear function.

If your a priori belief is that a quadratic function is preferable, then minimize

$$
\mathcal { B } \propto \int [ \widehat { u } ^ { \prime \prime \prime } ( x ) ] ^ { 2 } d x \propto \sum _ { \mu = 0 } ^ { M - 4 } [ - \widehat { u } _ { \mu } + 3 \widehat { u } _ { \mu + 1 } - 3 \widehat { u } _ { \mu + 2 } + \widehat { u } _ { \mu + 3 } ] ^ { 2 }
$$

with

$$
\mathbf { B } = \left( \begin{array} { c c c c c c c c c } { - 1 } & { 3 } & { - 3 } & { 1 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { - 1 } & { 3 } & { - 3 } & { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { \vdots } & { } & { } & { } & { \ddots } & { } & { } & { } & { \vdots } \\ { 0 } & { \cdots } & { 0 } & { 0 } & { - 1 } & { 3 } & { - 3 } & { 1 } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { 0 } & { 0 } & { - 1 } & { 3 } & { - 3 } & { 1 } \end{array} \right)
$$

and now

$$
\mathbf { H } = { \left( \begin{array} { l l l l l l l l l l l l } { 1 } & { - 3 } & { 3 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { - 3 } & { 1 0 } & { - 1 2 } & { 6 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { 3 } & { - 1 2 } & { 1 9 } & { - 1 5 } & { 6 } & { - 1 } & { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { - 1 } & { 6 } & { - 1 5 } & { 2 0 } & { - 1 5 } & { 6 } & { - 1 } & { 0 } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { - 1 } & { 6 } & { - 1 5 } & { 2 0 } & { - 1 5 } & { 6 } & { - 1 } & { 0 } & { \cdots } & { 0 } \\ { \vdots } & & & & { \ddots } & & & & { \vdots } & & & { \vdots } \\ { 0 } & { \cdots } & { 0 } & { - 1 } & { 6 } & { - 1 5 } & { 2 0 } & { - 1 5 } & { 6 } & { - 1 } & { 0 } \\ { 0 } & { \cdots } & { 0 } & { 0 } & { - 1 } & { 6 } & { - 1 5 } & { 2 0 } & { - 1 5 } & { 6 } & { - 1 } \\ { 0 } & { \cdots } & { 0 } & { 0 } & { 0 } & { - 1 } & { 6 } & { - 1 5 } & { 1 9 } & { - 1 2 } & { 3 } \\ { 0 } & { \cdots } & { 0 } & { 0 } & { 0 } & { 0 } & { - 1 } & { 6 } & { - 1 2 } & { 1 0 } & { - 3 } \\ { 0 } & { \cdots } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { - 1 } & { 3 } & { - 3 } & { 1 } \end{array} \right) }
$$

(We’ll leave the calculation of cubics and above to the compulsive reader.)

Notice that you can regularize with “closeness to a differential equation,” if you want. Just pick B to be the appropriate sum of finite difference operators (the coefficients can depend on $x$ ) and calculate $\mathbf { H } = \mathbf { B } ^ { T } \cdot \mathbf { B }$ . You don’t need to know the values of your boundary conditions, since B can have fewer rows than columns, as above; hopefully, your data will determine them. Of course, if you do know some boundary conditions, you can build these into $\mathbf { B }$ , too.

With all the proportionality signs above, you may have lost track of what actual value of $\lambda$ to try first. A simple trick for at least getting “on the map” is to first try

$$
\lambda = \mathrm { T r } ( \mathbf { A } ^ { T } \cdot \mathbf { A } ) / \mathrm { T r } ( \mathbf { H } )
$$

where $\mathrm { T r }$ is the trace of the matrix (sum of diagonal components). This choice will tend to make the two parts of the minimization have comparable weights, and you can adjust from there.

As for what is the “correct” value of $\lambda$ , an objective criterion, if you know your errors $\sigma _ { i }$ with reasonable accuracy, is to make $\chi ^ { 2 }$ (that is, $| \mathbf { A } \cdot { \widehat { \mathbf { u } } } - \mathbf { b } | ^ { 2 } )$ equal to $N$ , the number of measurements. We remarked above on the twin acceptable choices $N \pm ( 2 N ) ^ { 1 / 2 }$ . A subjective criterion is to pick any value that you like in the range $0 < \lambda < \infty$ , depending on your relative degree of belief in the a priori and a posteriori evidence. (Yes, people actually do that.) The problem with being a rigorous Bayesian at this stage is that rarely, if ever, is your understanding of the prior so complete as to give a firm, objective, value for $\lambda$ , and, as we pointed out in $\ S 1 5 . 1 . 1$ , purely Bayesian methods for assessing goodness-of-fit are largely nonexistent.

# 19.5.1 Two-Dimensional Problems and Iterative Methods

Up to now our notation has been indicative of a one-dimensional problem, finding ${ \widehat { u } } ( x )$ or $\widehat { u } _ { \mu } = \widehat { u } ( x _ { \mu } )$ . However, all of the discussion easily generalizes to the problem of estimating a two-dimensional set of unknowns $\widehat { u } _ { \mu \kappa }$ , $\mu = 0 , \ldots , M - 1$ ; $\kappa = 0 , \ldots , K - 1$ , corresponding, say, to the pixel intensities of a measured image. In this case, equation (19.5.8) is still the one we want to solve.

In image processing, it is usual to have the same number of input pixels in a measured “raw” or “dirty” image as desired “clean” pixels in the processed output image, so the matrices $\mathbf { R }$ and A (equation 19.5.5) are square and of size $M K \times M K$ . A is typically too large to represent as a full matrix, but often it is either (i) sparse, with coefficients blurring an underlying pixel $( i , j )$ only into measurements $( i \pm$ few; $j \pm \mathrm { f e w } )$ , or (ii) translationally invariant, so that $A _ { ( i , j ) ( \mu , \nu ) } = A ( i - \mu , j - \nu )$ . Both of these situations lead to tractable problems.

In the case of translational invariance, fast Fourier transforms (FFTs) are the obvious method of choice. The general linear relation between underlying function and measured values (19.4.7) now becomes a discrete convolution like equation (13.1.1). If k denotes a two-dimensional wave vector, then the two-dimensional FFT takes us back and forth between the transform pairs

$$
A ( i - \mu , j - \nu ) \iff \widetilde { \mathbf { A } } ( \mathbf { k } ) \qquad b _ { ( i , j ) } \iff \widetilde { b } ( \mathbf { k } ) \qquad \widehat { u } _ { ( i , j ) } \iff \widetilde { u } ( \mathbf { k } )
$$

We also need a regularization or smoothing operator $\mathbf { B }$ and the derived $\mathbf { H } = \mathbf { B } ^ { T } \cdot \mathbf { B }$ . One popular choice for $\mathbf { B }$ is the five-point finite difference approximation of the Laplacian operator, that is, the difference between the value of each point and the average of its four Cartesian neighbors. In Fourier space, this choice implies

$$
\begin{array} { c } { { \widetilde { B } ( { \bf k } ) \propto \sin ^ { 2 } ( \pi k _ { 1 } / M ) \sin ^ { 2 } ( \pi k _ { 2 } / K ) } } \\ { { \widetilde { H } ( { \bf k } ) \propto \sin ^ { 4 } ( \pi k _ { 1 } / M ) \sin ^ { 4 } ( \pi k _ { 2 } / K ) } } \end{array}
$$

In Fourier space, equation (19.5.7) is merely algebraic, with solution

$$
\widetilde { u } ( \mathbf { k } ) = \frac { \widetilde { A } ^ { * } ( \mathbf { k } ) \widetilde { b } ( \mathbf { k } ) } { | \widetilde { A } ( \mathbf { k } ) | ^ { 2 } + \lambda \widetilde { H } ( \mathbf { k } ) }
$$

where the asterisk denotes complex conjugation. You can make use of the FFT routines for real data in $\ S 1 2 . 6$ .

Turn now to the case where $\mathbf { A }$ is not translationally invariant. Direct solution of (19.5.8) is now hopeless, since the matrix A is just too large. We need some kind of iterative scheme.

One way to proceed is to use the full machinery of the conjugate gradient method in $\ S 1 0 . 8$ to find the minimum of $\mathcal { A } + \lambda \mathcal { B }$ , equation (19.5.6). Of the various methods in Chapter 10, the conjugate gradient is the unique best choice because (i) it does not require storage of a Hessian matrix, which would be infeasible here, and (ii) it does exploit gradient information, which we can readily compute: The gradient of equation (19.5.6) is

$$
\nabla ( \mathcal { A } + \lambda \mathcal { B } ) = 2 [ ( \mathbf { A } ^ { T } \cdot \mathbf { A } + \lambda \mathbf { H } ) \cdot \widehat { \mathbf { u } } - \mathbf { A } ^ { T } \cdot \mathbf { b } ]
$$

(cf. 19.5.8). Evaluation of both the function and the gradient should of course take advantage of the sparsity of A, for example using the methods ax and atx in the NRsparseMat object in $\ S 2 . 7 . 5$ . We will discuss the conjugate gradient technique further in $\ S 1 9 . 7$ , in the context of the (nonlinear) maximum entropy method. Some of that discussion can apply here as well.

The conjugate gradient method notwithstanding, application of the unsophisticated steepest descent method (see $\ S 1 0 . 8 )$ ) can sometimes produce useful results, particularly when combined with projections onto convex sets (see below). If the solution after $k$ iterations is denoted $\widehat { \mathbf { u } } ^ { ( k ) }$ , then after $k + 1$ iterations we have

$$
\widehat { \mathbf { u } } ^ { ( k + 1 ) } = [ \mathbf { 1 } - \epsilon ( \mathbf { A } ^ { T } \cdot \mathbf { A } + \lambda \mathbf { H } ) ] \cdot \widehat { \mathbf { u } } ^ { ( k ) } + \epsilon \mathbf { A } ^ { T } \cdot \mathbf { b }
$$

Here $\epsilon$ is a parameter that dictates how far to move in the downhill gradient direction. The method converges when $\epsilon$ is small enough, in particular satisfying

$$
0 < \epsilon < \frac { 2 } { \mathrm { m a x ~ e i g e n v a l u e } \left( \mathbf { A } ^ { T } \cdot \mathbf { A } + \lambda \mathbf { H } \right) }
$$

There exist complicated schemes for finding optimal values or sequences for $\epsilon$ , see [7]; or, one can adopt an experimental approach, evaluating (19.5.6) to be sure that downhill steps are in fact being taken.

In those image processing problems where the final measure of success is somewhat subjective (e.g., “how good does the picture look?”), iteration (19.5.21) sometimes produces significantly improved images long before convergence is achieved. This probably accounts for much of its use, since its mathematical convergence is extremely slow. In fact, (19.5.21) can be used with $\mathbf H = 0$ , in which case the solution is not regularized at all, and full convergence would be disastrous! This is called Van Cittert’s method and goes back to the 1930s. A number of iterations the order of $1 0 ^ { 3 }$ is not uncommon [7].

# 19.5.2 Deterministic Constraints: Projections onto Convex Sets

A set of possible underlying functions (or images) $\{ \widehat { \mathbf { u } } \}$ is said to be convex if, for any two elements $\widehat { \mathbf { u } } _ { a }$ and $\widehat { \mathbf { u } } _ { b }$ in the set, all the linearly interpolated combinations

$$
( 1 - \eta ) \widehat { \mathbf { u } } _ { a } + \eta \widehat { \mathbf { u } } _ { b } \qquad 0 \leq \eta \leq 1
$$

are also in the set. Many deterministic constraints that one might want to impose on the solution $\widehat { \mathbf { u } }$ to an inverse problem in fact define convex sets, for example:

- positivity   
- compact support (i.e., zero value outside of a certain region)   
- known bounds (i.e., $u _ { L } ( x ) \leq \widehat { u } ( x ) \leq u _ { U } ( x )$ for specified functions $u _ { L }$ and $u \sigma ,$ ).

(In this last case, the bounds might be related to an initial estimate and its error bars, e.g., $\hat { u } _ { 0 } ( x ) \pm \gamma \sigma ( x )$ , where $\gamma$ is of order 1 or 2.) Notice that these, and similar, constraints can be either in the image space, or in the Fourier transform space, or (in fact) in the space of any linear transformation of $\widehat { \mathbf { u } }$ .

If $C _ { i }$ is a convex set, then $\mathcal { P } _ { i }$ is called a nonexpansive projection operator onto that set if (i) $\mathcal { P } _ { i }$ leaves unchanged any $\widehat { \mathbf { u } }$ already in $C _ { i }$ , and (ii) $\mathcal { P } _ { i }$ maps any $\widehat { \mathbf { u } }$ outside $C _ { i }$ to the closest element of $C _ { i }$ , in the sense that

$$
\left| \mathcal { P } _ { i } \widehat { \mathbf { u } } - \widehat { \mathbf { u } } \right| \leq \left| \widehat { \mathbf { u } } _ { a } - \widehat { \mathbf { u } } \right| \quad \mathrm { f o r \ a l l \ } \widehat { \mathbf { u } } _ { a } \mathrm { \ i n \ } C _ { i }
$$

While this definition sounds complicated, examples are very simple: A nonexpansive projection onto the set of positive $\widehat { \mathbf { u } }$ ’s is “set all negative components of $\widehat { \mathbf { u } }$ equal to zero.” A nonexpansive projection onto the set of ${ \widehat { u } } ( x )$ ’s bounded by $u _ { L } ( x ) \ \leq$ ${ \widehat { u } } ( x ) \leq u _ { U } ( x )$ is “set all values less than the lower bound equal to that bound, and set all values greater than the upper bound equal to that bound.” A nonexpansive projection onto functions with compact support is “zero the values outside of the region of support.”

The usefulness of these definitions is the following remarkable theorem: Let $C$ be the intersection of $m$ convex sets $C _ { 1 } , C _ { 2 } , \ldots , C _ { m } .$ . Then the iteration

$$
\widehat { \mathbf { u } } ^ { ( k + 1 ) } = ( \mathcal { P } _ { 1 } \mathcal { P } _ { 2 } \cdot \cdot \cdot \mathcal { P } _ { m } ) \widehat { \mathbf { u } } ^ { ( k ) }
$$

will converge to $C$ from all starting points, as $k  \infty$ . Also, if $C$ is empty (there is no intersection), then the iteration will have no limit point. Application of this theorem is called the method of projections onto convex sets or sometimes POCS [7].

A generalization of the POCS theorem is that the $\mathcal { P } _ { i }$ ’s can be replaced by a set of $\mathcal { T } _ { i }$ ’s,

$$
\mathcal { T } _ { i } \equiv \mathbf { 1 } + \beta _ { i } ( \mathcal { P } _ { i } - \mathbf { 1 } ) \qquad 0 < \beta _ { i } < 2
$$

A well-chosen set of $\beta _ { i }$ ’s can accelerate the convergence to the intersection set $C$

Some inverse problems can be completely solved by iteration (19.5.25) alone! For example, a problem that occurs in both astronomical imaging and $\mathrm { X }$ -ray diffraction work is to recover an image given only the modulus of its Fourier transform (equivalent to its power spectrum or autocorrelation) and not the phase. Here two convex sets can be utilized: the set of all positive images, and the set of all images with zero intensity outside of some specified region. A third set, the set of all images whose Fourier transform has the specified modulus to within specified error bounds, is not convex: It is an annulus in the complex plane for each Fourier component. (Of course FFTs are used to get in and out of Fourier space each time the Fourier constraint is imposed.) The POCS iteration (19.5.25) that cycles among all three sets, imposing each constraint in turn, is thus not guaranteed (by the POCS theorem) to converge; it can get stuck in traps [8]. However, it often does work.

The specific application of POCS to constraints (not necessarily all convex) alternately in the spatial and Fourier domains is known as the Gerchberg-Saxton algorithm [9]. While this algorithm is nonexpansive, and is frequently convergent in practice, it does not converge in all cases [8,10]. In the phase-retrieval problem just mentioned, the algorithm often gets stuck in traps for many iterations. After as many as $1 0 ^ { 4 }$ to $1 0 ^ { 5 }$ iterations, sudden, dramatic improvements may occur. In principle, some traps may be permanent, requiring more interventional “unsticking” procedures; see [8,11]. The uniqueness of the solution is also not well understood, although for two-dimensional images of reasonable complexity it is believed to be unique. The use of nonconvex sets in an iteration like (19.5.25) is called the method of generalized projections.

Deterministic constraints can be incorporated, via projection operators, into iterative methods of linear regularization. In particular, rearranging terms somewhat, we can write the iteration (19.5.21) as

$$
\widehat { \mathbf { u } } ^ { ( k + 1 ) } = ( \mathbf { 1 } - \epsilon \lambda \mathbf { H } ) \cdot \widehat { \mathbf { u } } ^ { ( k ) } + \epsilon \mathbf { A } ^ { T } \cdot ( \mathbf { b } - \mathbf { A } \cdot \widehat { \mathbf { u } } ^ { ( k ) } )
$$

If the iteration is modified by the insertion of projection operators at each step

$$
\hat { \mathbf { u } } ^ { ( k + 1 ) } = ( \mathcal { P } _ { 1 } \mathcal { P } _ { 2 } \cdots \mathcal { P } _ { m } ) [ ( \mathbf { 1 } - \epsilon \lambda \mathbf { H } ) \cdot \hat { \mathbf { u } } ^ { ( k ) } + \epsilon \mathbf { A } ^ { T } \cdot ( \mathbf { b } - \mathbf { A } \cdot \hat { \mathbf { u } } ^ { ( k ) } ) ]
$$

(or, instead of $\mathcal { P } _ { i }$ ’s, the $\mathcal { T } _ { i }$ operators of equation 19.5.26), then it can be shown that the convergence condition (19.5.22) is unmodified, and the iteration will converge to minimize the quadratic functional (19.5.6) subject to the desired nonlinear deterministic constraints. See [7] for references to more sophisticated, and faster converging, iterations along these lines.

# CITED REFERENCES AND FURTHER READING:

Phillips, D.L. 1962, “A Technique for the Numerical Solution of Certain Integral Equations of the First Kind,” Journal of the Association for Computing Machinery, vol. 9, pp. 84–97.[1]   
Twomey, S. 1963, “On the Numerical Solution of Fredholm Integral Equations of the First Kind by the Inversion of the Linear System Produced by Quadrature,” Journal of the Association for Computing Machinery,vol.10,pp.97-101.[2]   
Twomey, S. 1977, Introduction to the Mathematics of Inversion in Remote Sensing and Indirect Measurements (Amsterdam: Elsevier).[3]   
Craig, I.J.D., and Brown, J.C. 1986, Inverse Problems in Astronomy (Bristol, UK: Adam Hilger).[4]   
Tikhonov, A.N., and Arsenin, V.Y. 1977, Solutions of Ill-Posed Problems (New York: Wiley).[5]   
Tikhonov, A.N., and Goncharsky, A.V. (eds.) 1987, Ill-Posed Problems in the Natural Sciences (Moscow: MIR).   
Miller, K. 1970, “Least Squares Methods for Ill-Posed Problems with a Prescribed Bound,” SIAM Journal on Mathematical Analysis,vol.1,pp.52-74.[6]   
Schafer, R.W., Mersereau, R.M., and Richards, M.A. 1981, “Constrained Iterative Restoration Algorithm,” Proceedings of the IEEE, vol. 69, pp. 432–450.   
Biemond, J., Lagendijk, R.L., and Mersereau, R.M. 1990, “Iterative Methods for Image Deblurring,” Proceedings of the IEEE, vol. 78, pp. 856–883.[7]   
Sezan, M.I. 1992, “An Overview of Convex Projections Theory and Its Application to Image Recovery Problems,” Ultramicroscopy, vol. 40, pp. 55–67.[8]   
Gerchberg, R.W., and Saxton, W.O. 1972, “A Practical Algorithm for the Determination of Phase from Image and Diffraction Plane Pictures,” Optik, vol. 35, pp. 237–246.[9]   
Fienup, J.R. 1982, “Phase Retrieval Algorithms: A Comparison,” Applied Optics, vol. 15, pp. 2758– 2769.[10]   
Fienup, J.R., and Wackerman, C.C. 1986, “Phase-Retrieval Stagnation Problems and Solutions,” Journal of the Optical Society of America A,vol.3,pp.1897-1907.[11]

# 19.6 Backus-Gilbert Method

The Backus-Gilbert method [1,2], also known as the optimally localized average (OLA) method (see, e.g., [3] or [4] for summaries) differs from other regularization methods in the nature of its functionals $\mathcal { A }$ and $\mathcal { B }$ . For $\mathcal { B }$ , the method seeks to maximize the stability of the solution ${ \widehat { u } } ( x )$ rather than, in the first instance, its smoothness. That is,

$$
{ \mathcal B } \equiv \mathrm { V a r } [ \widehat { u } ( x ) ]
$$

is used as a measure of how much the solution ${ \widehat { u } } ( x )$ varies as the data vary within their measurement errors. Note that this variance is not the expected deviation of ${ \widehat { u } } ( x )$ from the true $u ( x )$ — that will be constrained by $\mathcal { A }$ — but rather measures the expected experiment-to-experiment scatter among estimates ${ \widehat { u } } ( x )$ if the whole experiment were to be repeated many times.

For $\mathcal { A }$ the Backus-Gilbert method looks at the relationship between the solution ${ \widehat { u } } ( x )$ and the true function $u ( x )$ , and seeks to make the mapping between these as close to the identity map as possible in the limit of error-free data. The method is linear, so the relationship between ${ \widehat { u } } ( x )$ and $u ( x )$ can be written as

$$
\widehat { u } ( x ) = \int \widehat { \delta } ( x , x ^ { \prime } ) u ( x ^ { \prime } ) d x ^ { \prime }
$$

for some so-called resolution function or averaging kernel $\widehat { \delta } ( x , x ^ { \prime } )$ . The Backus-Gilbert method seeks to minimize the width or spread of $\widehat { \delta }$ (that is, maximize the resolving power). $\mathcal { A }$ is chosen to be some positive measure of the spread.

While Backus-Gilbert’s philosophy is thus rather different from that of Phillips-Twomey and related methods, in practice the differences between the methods are less than one might think. A stable solution is almost inevitably bound to be smooth: The wild, unstable oscillations that result from an unregularized solution are always exquisitely sensitive to small changes in the data. Likewise, making $\widehat { \boldsymbol { u } } ( \boldsymbol { x } )$ close to $u ( x )$ inevitably will bring error-free data into agreement with the model. Thus $\mathcal { A }$ and $\mathcal { B }$ play roles closely analogous to their corresponding roles in the previous two sections.

The principal advantage of the Backus-Gilbert formulation is that it gives good control over just those properties that it seeks to measure, namely stability and resolving power. Moreover, in the Backus-Gilbert method, the choice of $\lambda$ (playing its usual role of compromise between $\mathcal { A }$ and $\mathcal { B }$ ) is conventionally made, or at least can easily be made, before any actual data are processed. One’s uneasiness at making a post hoc, and therefore potentially subjectively biased, choice of $\lambda$ is thus removed. Backus-Gilbert is often recommended as the method of choice for designing and predicting the performance of experiments that require data inversion.

Let’s see how this all works. Starting with equation (19.4.5),

$$
c _ { i } \equiv s _ { i } + n _ { i } = \int r _ { i } ( x ) u ( x ) d x + n _ { i }
$$

and building in linearity from the start, we seek a set of inverse response kernels $q _ { i } ( x )$ such that

$$
{ \hat { u } } ( x ) = \sum _ { i } q _ { i } ( x ) c _ { i }
$$

is the desired estimator of $u ( x )$ . It is useful to define the integrals of the response kernels for each data point,

$$
R _ { i } \equiv \int r _ { i } ( x ) d x
$$

Substituting equation (19.6.4) into equation (19.6.3), and comparing with equation (19.6.2), we see that

$$
\widehat { \delta } ( x , x ^ { \prime } ) = \sum _ { i } q _ { i } ( x ) r _ { i } ( x ^ { \prime } )
$$

We can require this averaging kernel to have unit area at every $x$ , giving

$$
1 = \int { \widehat { \delta } } ( x , x ^ { \prime } ) d x ^ { \prime } = \sum _ { i } q _ { i } ( x ) \int r _ { i } ( x ^ { \prime } ) d x ^ { \prime } = \sum _ { i } q _ { i } ( x ) R _ { i } \equiv \mathbf { q } ( x ) \cdot \mathbf { R }
$$

where $\mathbf { q } ( x )$ and $\mathbf { R }$ are each vectors of length $N$ , the number of measurements.

Standard propagation of errors, and equation (19.6.1), give

$$
{ \mathcal { B } } = \mathrm { V a r } [ { \widehat { u } } ( x ) ] = \sum _ { i } \sum _ { j } q _ { i } ( x ) S _ { i j } q _ { j } ( x ) = \mathbf { q } ( x ) \cdot \mathbf { S } \cdot \mathbf { q } ( x )
$$

where $S _ { i j }$ is the covariance matrix (equation 19.4.6). If one can neglect off-diagonal covariances (as when the errors on the $c _ { i }$ ’s are independent), then $S _ { i j } ~ = ~ \delta _ { i j } \sigma _ { i } ^ { 2 }$ is diagonal.

We now need to define a measure of the width or spread of $\widehat { \delta } ( x , x ^ { \prime } )$ at each value of $x$ . While many choices are possible, Backus and Gilbert choose the second moment of its square. This measure becomes the functional $\mathcal { A }$ ,

$$
\begin{array} { l } { { \displaystyle { \mathcal A } \equiv w ( x ) = \int ( x ^ { \prime } - x ) ^ { 2 } [ \widehat \delta ( x , x ^ { \prime } ) ] ^ { 2 } d x ^ { \prime } } \ ~ } \\ { { \displaystyle ~ = \sum _ { i } \sum _ { j } q _ { i } ( x ) W _ { i j } ( x ) q _ { j } ( x ) \equiv \mathbf q ( x ) \cdot \mathbf W ( x ) \cdot \mathbf q ( x ) } } \end{array}
$$

where we have here used equation (19.6.6) and defined the spread matrix $\mathbf { W } ( x )$ by

$$
W _ { i j } ( x ) \equiv \int ( x ^ { \prime } - x ) ^ { 2 } r _ { i } ( x ^ { \prime } ) r _ { j } ( x ^ { \prime } ) d x ^ { \prime }
$$

The functions $q _ { i } ( x )$ are now determined by the minimization principle

$$
\mathrm { m i n i m i z e : } \quad \boldsymbol { \mathcal { A } } + \boldsymbol { \lambda } \boldsymbol { \mathcal { B } } = \mathbf { q } \left( \boldsymbol { x } \right) \cdot \left[ \mathbf { W } \left( \boldsymbol { x } \right) + \boldsymbol { \lambda } \mathbf { S } \right] \cdot \mathbf { q } \left( \boldsymbol { x } \right)
$$

subject to the constraint (19.6.7) that ${ \bf q } ( x ) \cdot { \bf R } = 1$

The solution of equation (19.6.11) is

$$
\mathbf { q } ( x ) = \frac { [ \mathbf { W } ( x ) + \lambda \mathbf { S } ] ^ { - 1 } \cdot \mathbf { R } } { \mathbf { R } \cdot [ \mathbf { W } ( x ) + \lambda \mathbf { S } ] ^ { - 1 } \cdot \mathbf { R } }
$$

(Reference [4] gives an accessible proof.) For any particular data set c (set of measurements $c _ { i }$ ), the solution $\widehat { \boldsymbol { u } } ( \boldsymbol { x } )$ is thus

$$
\widehat { u } ( x ) = \frac { \mathbf { c } \cdot [ \mathbf { W } ( x ) + \lambda \mathbf { S } ] ^ { - 1 } \cdot \mathbf { R } } { \mathbf { R } \cdot [ \mathbf { W } ( x ) + \lambda \mathbf { S } ] ^ { - 1 } \cdot \mathbf { R } }
$$

(Don’t let this notation mislead you into inverting the full matrix $\mathbf { W } ( x ) + \lambda \mathbf { S }$ . You only need to solve the linear system $( \mathbf { W } ( x ) + \lambda \mathbf { S } ) \cdot \mathbf { y } = \mathbf { R }$ for the vector $\mathbf { y }$ , and then substitute y into both the numerators and denominators of 19.6.12 or 19.6.13.)

Equations (19.6.12) and (19.6.13) have a completely different character from the linearly regularized solutions to (19.5.7) and (19.5.8). The vectors and matrices in (19.6.12) all have size $N$ , the number of measurements. There is no discretization of the underlying variable $x$ , so $M$ does not come into play at all. One solves a different $N \times N$ set of linear equations for each desired value of $x$ . By contrast, in (19.5.8), one solves an $M \times M$ linear set, but only once. In general, the computational burden of repeatedly solving linear systems makes the Backus-Gilbert method unsuitable for other than one-dimensional problems.

How does one choose $\lambda$ within the Backus-Gilbert scheme? As already mentioned, you can (in some cases should) make the choice before you see any actual data. For a given trial value of $\lambda$ , and for a sequence of $x$ ’s, use equation (19.6.12) to calculate $\mathbf { q } ( x )$ ; then use equation (19.6.6) to plot the resolution functions $\widehat { \delta } ( x , x ^ { \prime } )$ as a function of $x ^ { \prime }$ . These plots will exhibit the amplitude with which different underlying values $x ^ { \prime }$ contribute to the point ${ \widehat { u } } ( x )$ of your estimate. For the same value of $\lambda$ , also plot the function $\sqrt { \mathrm { V a r } [ \widehat { u } ( x ) ] }$ using equation (19.6.8). (You need an estimate of your measurement covariance matrix for this.)

As you change $\lambda$ you will see very explicitly the trade-off between resolution and stability. Pick the value that meets your needs. You can even choose $\lambda$ to be a function of $x$ , $\lambda = \lambda ( x )$ , in equations (19.6.12) and (19.6.13), should you desire to do so. (This is one benefit of solving a separate set of equations for each $x$ .) For the chosen value or values of $\lambda$ , you now have a quantitative understanding of your inverse solution procedure. This can prove invaluable if — once you are processing real data — you need to judge whether a particular feature, a spike or jump for example, is genuine, and/or is actually resolved. The Backus-Gilbert method has found particular success among geophysicists, who use it to obtain information about the structure of the Earth (e.g., density run with depth) from seismic travel time data.

# CITED REFERENCES AND FURTHER READING:

Backus, G.E., and Gilbert, F. 1968, “The Resolving Power of Gross Earth Data,” Geophysical Journal of the Royal Astronomical Society,vol.16,pp.169-205.[1]   
Backus, G.E., and Gilbert, F. 1970, “Uniqueness in the Inversion of Inaccurate Gross Earth Data,” Philosophical Transactions of the Royal Society of London A,vol.266,pp.123-192.[2]   
Parker, R.L. 1977, “Understanding Inverse Theory,” Annual Review of Earth and Planetary Science, vol. 5, pp.35-64.[3]   
Loredo, T.J., and Epstein, R.I. 1989, “Analyzing Gamma-Ray Burst Spectral Data,” Astrophysical Journal, vol. 336,pp.896-919.[4]

# 19.7 Maximum Entropy Image Restoration

We must first comment in passing that the connection between maximum entropy inverse methods, considered here, and maximum entropy spectral estimation, discussed in $\ S 1 3 . 7$ , is rather distant. For practical purposes, the two techniques, though both named maximum entropy method or MEM, are unrelated. On the other hand, what we discuss here has a close connection to the discussion of entropy in $\ S 1 4 . 7$ .

The entropy of a physical system in some macroscopic state, usually denoted $S$ , is the logarithm of the number of microscopically distinct configurations that all have the same macroscopic observables (i.e., consistent with the observed macroscopic state). Actually, we will find it useful to denote the negative of the entropy, also called the negentropy, by $H \equiv - S$ (a notation that goes back to Boltzmann). In situations where there is reason to believe that the a priori probabilities of the microscopic configurations are all the same (these situations are called ergodic), the Bayesian prior $P ( \mathbf { u } | I )$ for a macroscopic state with entropy $S$ is proportional to exp.S / or $\exp ( - H )$ .

MEM uses this concept to assign a prior probability to any given underlying function $\mathbf { u }$ . This very general idea is applicable to much more than image restoration [1,2]. For definiteness, however, we consider that application only. Suppose [3-5] that the measurement of luminance in each pixel in an image is quantized to (in some units) an integer value. Let

$$
U = \sum _ { \mu = 0 } ^ { M - 1 } u _ { \mu }
$$

be the total number of luminance quanta in the whole image. Then we can base our “prior” on the notion that each luminance quantum has an equal a priori chance of being in any pixel. (See [6] for a more abstract justification of this idea.) The number of ways of getting a particular configuration $\mathbf { u }$ is

$$
\frac { U ! } { u _ { 0 } ! u _ { 1 } ! \cdots u _ { M - 1 } ! } \propto \exp \Biggl [ - \sum _ { \mu } u _ { \mu } \ln ( u _ { \mu } / U ) + \textstyle { \frac { 1 } { 2 } } \Biggl ( \ln U - \sum _ { \mu } \ln u _ { \mu } \Biggr ) \Biggr ]
$$

Here the left side can be understood as the number of distinct orderings of all the luminance quanta, divided by the numbers of equivalent reorderings within each pixel, while the right side follows by Stirling’s approximation to the factorial function. Taking the negative of the logarithm, and neglecting terms of order $\log U$ in the presence of terms of order U , we get the negentropy

$$
H ( { \mathbf { u } } ) = \sum _ { \mu = 0 } ^ { M - 1 } u _ { \mu } \ln ( u _ { \mu } / U )
$$

As discussed for equations $( 1 9 . 4 . 1 3 ) - ( 1 9 . 4 . 1 5 )$ , we now seek to maximize

$$
\begin{array} { r } { P ( \mathbf { u } | \mathbf { c } , I ) \propto \exp \biggl [ - \frac { 1 } { 2 } \chi ^ { 2 } \biggr ] \exp [ - H ( \mathbf { u } ) ] } \end{array}
$$

or, equivalently,

$$
\displaystyle - \ln { \big [ } P ( \mathbf { u } | \mathbf { c } , I ) { \big ] } = { \textstyle { \frac { 1 } { 2 } } } \chi ^ { 2 } [ \mathbf { u } ] + H ( \mathbf { u } ) = { \textstyle { \frac { 1 } { 2 } } } \chi ^ { 2 } [ \mathbf { u } ] + \sum _ { \mu = 0 } ^ { M - 1 } u _ { \mu } \ln ( u _ { \mu } / U )
$$

This ought to remind you of equation (19.4.11), or equation (19.5.6), or in fact any of our previous minimization principles along the lines of $\mathcal { A } + \lambda \mathcal { B }$ , where $\lambda { \mathcal { B } } = H ( \mathbf { u } )$ is a regularizing operator. Where is $\lambda ?$ We need to put it in for exactly the reason discussed following equation (19.4.11): Degenerate inversions are likely to be able to achieve unrealistically small values of $\chi ^ { 2 }$ . We need an adjustable parameter to bring $\chi ^ { 2 }$ into its expected narrow statistical range of $N \pm ( 2 N ) ^ { 1 / 2 }$ . The discussion at the beginning of $\ S 1 9 . 4$ showed that it makes no difference which term we attach the $\lambda$ to. For consistency in notation, we absorb a factor 2 into $\lambda$ and put it on the entropy term. (Another way to see the necessity of an undetermined $\lambda$ factor is to note that it is necessary if our minimization principle is to be invariant under changing the units in which $\mathbf { u }$ is quantized, e.g., if an 8-bit analog-to-digital converter is replaced by a 12-bit one.) We can now also put “hats” back to indicate that this is the procedure for obtaining our chosen statistical estimator:

$$
\widehat { \mathbf { u } } \mathrm { \ m i n i m i z e s : \quad } \mathcal { A } + \lambda \mathcal { B } = \chi ^ { 2 } [ \mathbf { u } ] + \lambda H ( \mathbf { u } ) = \chi ^ { 2 } [ \mathbf { u } ] + \lambda \sum _ { \mu = 0 } ^ { M - 1 } u _ { \mu } \ln ( u _ { \mu } )
$$

(Formally, we might also add a second Lagrange multiplier $\lambda ^ { \prime } U$ , to constrain the total intensity $U$ to be constant.)

It is not hard to see that the negentropy, $H ( \mathbf { u } )$ , is in fact a regularizing operator, similar to $\mathbf { u } \cdot \mathbf { u }$ (equation 19.4.11) or $\mathbf { u } \cdot \mathbf { H } \cdot \mathbf { u }$ (equation 19.5.6). The following of its properties are noteworthy:

1. When $U$ is held constant, $H ( \mathbf { u } )$ is minimized for $\widehat { u } _ { \mu } = U / M =$ constant, so it smooths in the sense of trying to achieve a constant solution, similar to equation (19.5.4). The fact that the constant solution is a minimum follows from the fact that the second derivative of $u \ln u$ is positive.

2. Unlike equation (19.5.4), however, $H ( \widehat { \mathbf { u } } )$ is local, in the sense that it does not difference neighboring pixels. It simply sums some function $f$ , here

$$
f ( u ) = u \ln u
$$

over all pixels; it is invariant, in fact, under a complete scrambling of the pixels in an image. This form implies that $H ( \mathbf { u } )$ is not seriously increased by the occurrence of a small number of very bright pixels (point sources) embedded in a low-intensity smooth background.

3. $H ( \mathbf { u } )$ goes to infinite slope as any one pixel goes to zero. This causes it to enforce positivity of the image, without the necessity of additional deterministic constraints.

4. The biggest difference between $H ( \mathbf { u } )$ and the other regularizing operators that we have met is that $H ( \mathbf { u } )$ is not a quadratic functional of $\mathbf { u }$ , so the equations obtained by varying equation (19.7.6) are nonlinear. This fact is itself worthy of some additional discussion.

Nonlinear equations are harder to solve than linear equations. For image processing, however, the large number of equations usually dictates an iterative solution procedure, even for linear equations, so the practical effect of the nonlinearity is somewhat mitigated. Below, we will summarize some of the methods that are successfully used for MEM inverse problems.

For some problems, notably the problem in radio-astronomy of image recovery from an incomplete set of Fourier coefficients, the superior performance of MEM inversion can be, in part, traced to the nonlinearity of $H ( \mathbf { u } )$ . One way to see this [3] is to consider the limit of perfect measurements $\sigma _ { i } \to 0$ . In this case, the $\chi ^ { 2 }$ term in the minimization principle (19.7.6) gets replaced by a set of constraints, each with its own Lagrange multiplier, requiring agreement between model and data; that is,

$$
\widehat { \mathbf { u } } \mathrm { \ m i n i m i z e s : } \quad \sum _ { j } \lambda _ { j } \left[ c _ { j } - \sum _ { \mu } R _ { j \mu } u _ { \mu } \right] + H ( \mathbf { u } )
$$

(cf. equation 19.4.7). Setting the formal derivative with respect to $u _ { \mu }$ to zero gives

$$
{ \frac { \partial H } { \partial u _ { \mu } } } = f ^ { \prime } ( u _ { \mu } ) = \sum _ { j } \lambda _ { j } R _ { j \mu }
$$

or defining a function $G$ as the inverse function of $f ^ { \prime }$ ,

$$
u _ { \mu } = G \left( \sum _ { j } \lambda _ { j } R _ { j \mu } \right)
$$

This solution is only formal, since the $\lambda _ { j }$ ’s must be found by requiring that equation (19.7.10) satisfy all the constraints built into equation (19.7.8). However, equation (19.7.10) does show the crucial fact that if $G$ is linear, then the solution $\widehat { \mathbf { u } }$ contains only a linear combination of basis functions $R _ { j \mu }$ corresponding to actual measurements $j$ . This is equivalent to setting unmeasured $c _ { j }$ ’s to zero. Notice that the principal solution obtained from equation (19.4.11) in fact has a linear $G$ .

In the problem of incomplete Fourier image reconstruction, the typical $R _ { j \mu }$ has the form $\exp ( - 2 \pi i \mathbf { k } _ { j } \cdot \mathbf { x } _ { \mu } )$ , where $\mathbf { x } _ { \mu }$ is a two-dimensional vector in the image space and $\mathbf { k } _ { \mu }$ is a two-dimensional wave vector. If an image contains strong point sources, then the effect of setting unmeasured $c _ { j }$ ’s to zero is to produce sidelobe ripples throughout the image plane. These ripples can mask any actual extended, low-intensity image features lying between the point sources. If, however, the slope of $G$ is smaller for small values of its argument and larger for large values, then ripples in low-intensity portions of the image are relatively suppressed, while strong point sources will be relatively sharpened (“superresolution”). This behavior on the slope of $G$ is equivalent to requiring $f ^ { \prime \prime \prime } ( u ) < 0$ . For $f ( u ) = u \ln u$ , we in fact have $f ^ { \prime \prime \prime } ( u ) = - 1 / u ^ { 2 } < 0$ .

In more picturesque language, the nonlinearity acts to “create” nonzero values for the unmeasured $c _ { i }$ ’s, so as to suppress the low-intensity ripple and sharpen the point sources.

# 19.7.1 Is MEM Really Magical?

How unique is the negentropy functional (19.7.3)? Recall that that equation is based on the assumption that luminance elements are a priori distributed over the pixels uniformly. If we instead had some other preferred a priori image in mind, one with pixel intensities $m _ { \mu }$ , then it is easy to show that the negentropy becomes

$$
H ( \mathbf { u } ) = \sum _ { \mu = 0 } ^ { M - 1 } u _ { \mu } \ln ( u _ { \mu } / m _ { \mu } ) + \mathrm { c o n s t a n t }
$$

(the constant can then be ignored). All the rest of the discussion then goes through.

More fundamentally, and despite statements by zealots to the contrary [5], there is actually nothing universal about the functional form $f ( u ) ~ = ~ u \ln u$ . In some other physical situations (for example, the entropy of an electromagnetic field in the limit of many photons per mode, as in radio-astronomy) the physical negentropy functional is actually $f ( u ) = - \ln u$ (see [3] for other examples). In general, the question, “Entropy of what?” is not uniquely answerable in any particular situation. (See reference [7] for an attempt at articulating a more general principle that reduces to one or another entropy functional under appropriate circumstances.)

The four numbered properties summarized above, plus the desirable sign for nonlinearity, $f ^ { \prime \prime \prime } ( u ) \ < \ 0$ , are all as true for the function $f ( u ) ~ = - \ln u$ as for $f ( u ) = u \ln u .$ . In fact, these properties are shared by a nonlinear function as simple as $f ( u ) = - { \sqrt { u } }$ , which has no information-theoretic justification at all (no logarithms!). MEM reconstructions of test images using any of these entropy forms are virtually indistinguishable [3].

By all available evidence, MEM seems to be neither more nor less than one usefully nonlinear version of the general regularization scheme $\mathcal { A } + \lambda \mathcal { B }$ that we have by now considered in many forms. Its peculiarities become strengths when applied to the reconstruction from incomplete Fourier data of images that are expected to be dominated by very bright point sources, but which also contain interesting lowintensity, extended sources. For images of some other character, there is no reason to suppose that MEM methods will generally dominate other regularization schemes, either ones already known or yet to be invented.

# 19.7.2 Algorithms for MEM

The goal is to find the vector $\widehat { \mathbf { u } }$ that minimizes $\mathscr { A } + \lambda \mathscr { B }$ where in the notation of equations (19.5.5), (19.5.6), and (19.7.7),

$$
{ \mathcal { A } } = | \mathbf { b - A \cdot u } | ^ { 2 } \qquad { \mathcal { B } } = \sum _ { \mu } f ( u _ { \mu } )
$$

Compared with a “general” minimization problem, we have the advantage that we can compute the gradients and the second partial derivative matrices (Hessian matrices) explicitly,

$$
\begin{array} { r l } { \nabla \mathcal { A } = 2 ( \mathbf { A } ^ { T } \cdot \mathbf { A } \cdot \mathbf { u } - \mathbf { A } ^ { T } \cdot \mathbf { b } ) \qquad } & { \frac { \partial ^ { 2 } \mathcal { A } } { \partial u _ { \mu } \partial u _ { \rho } } = [ 2 \mathbf { A } ^ { T } \cdot \mathbf { A } ] _ { \mu \rho } } \\ { [ \nabla \mathcal { B } ] _ { \mu } = f ^ { \prime } ( u _ { \mu } ) \qquad } & { \frac { \partial ^ { 2 } \mathcal { B } } { \partial u _ { \mu } \partial u _ { \rho } } = \delta _ { \mu \rho } f ^ { \prime \prime } ( u _ { \mu } ) } \end{array}
$$

It is important to note that while $\mathcal { A }$ ’s second partial derivative matrix cannot be stored (its size is the square of the number of pixels), it can be applied to any vector by first applying A, then $\mathbf { A } ^ { T }$ . In the case of reconstruction from incomplete Fourier data, or in the case of convolution with a translation invariant point spread function, these applications will typically involve several FFTs. Likewise, the calculation of the gradient $\nabla \mathcal { A }$ will involve FFTs in the application of A and $\mathbf { A } ^ { T }$ .

While some success has been achieved with the classical conjugate gradient method (-10.8), it is often found that the nonlinearity in $f ( u ) = u \ln u$ causes problems. Attempted steps that give u with even one negative value must be cut in magnitude, sometimes so severely as to slow the solution to a crawl. The underlying problem is that the conjugate gradient method develops its information about the inverse of the Hessian matrix a bit at a time, while changing its location in the search space. When a nonlinear function is quite different from a pure quadratic form, the old information becomes obsolete before it gets usefully exploited.

Skilling and collaborators [4,5,8,9] developed a complicated but highly successful scheme, wherein a minimum is repeatedly sought not along a single search direction, but in a small- (typically three-) dimensional subspace, spanned by vectors that are calculated anew at each landing point. The subspace basis vectors are chosen in such a way as to avoid directions leading to negative values. One of the most successful choices is the three-dimensional subspace spanned by the vectors with components given by

$$
\begin{array} { r l } & { e _ { \mu } ^ { ( 1 ) } = u _ { \mu } [ \nabla \mathcal { A } ] _ { \mu } } \\ & { e _ { \mu } ^ { ( 2 ) } = u _ { \mu } [ \nabla \mathcal { B } ] _ { \mu } } \\ & { e _ { \mu } ^ { ( 3 ) } = \frac { u _ { \mu } \sum _ { \rho } ( \partial ^ { 2 } \mathcal { A } / \partial u _ { \mu } \partial u _ { \rho } ) u _ { \rho } [ \nabla \mathcal { B } ] _ { \rho } } { \sqrt { \sum _ { \rho } u _ { \rho } \left( \left[ \nabla \mathcal { B } \right] _ { \rho } \right) ^ { 2 } } } - \frac { u _ { \mu } \sum _ { \rho } ( \partial ^ { 2 } \mathcal { A } / \partial u _ { \mu } \partial u _ { \rho } ) u _ { \rho } [ \nabla \mathcal { A } ] _ { \rho } } { \sqrt { \sum _ { \rho } u _ { \rho } \left( \left[ \nabla \mathcal { A } \right] _ { \rho } \right) ^ { 2 } } } } \end{array}
$$

(In these equations there is no sum over $\mu$ .) The form of the $\mathbf { e } ^ { ( 3 ) }$ has some justification if one views dot products as occurring in a space with the metric $g _ { \mu \nu } = \delta _ { \mu \nu } / u _ { \mu }$ , chosen to make zero values “far away”; see [4].

Within the three-dimensional subspace, the three-component gradient and ninecomponent Hessian matrix are computed by projection from the large space, and the minimum in the subspace is estimated by (trivially) solving three simultaneous linear equations, as in $\ S 1 0 . 9$ , equation (10.9.4). The size of a step $\Delta \mathbf { u }$ is required to be limited by the inequality

$$
\sum _ { \mu } ( \Delta u _ { \mu } ) ^ { 2 } / u _ { \mu } < ( 0 . 1 \mathrm { t o } 0 . 5 ) U
$$

Because the gradient directions $\nabla \mathcal { A }$ and $\nabla { \mathcal { B } }$ are separately available, it is possible to combine the minimum search with a simultaneous adjustment of $\lambda$ so as finally to satisfy the desired constraint. There are various further tricks employed.

A less general, but in practice often equally satisfactory, approach is due to Cornwell and Evans [10]. Here, noting that $\mathcal { B }$ ’s Hessian (second partial derivative) matrix is diagonal, one asks whether there is a useful diagonal approximation to $\mathcal { A }$ ’s Hessian, namely $2 \mathbf { A } ^ { T } \cdot \mathbf { A }$ . If $\Lambda _ { \mu }$ denotes the diagonal components of such an approximation, then a useful step in $\mathbf { u }$ would be

$$
\Delta u _ { \mu } = - \frac 1 { \Lambda _ { \mu } + \lambda f ^ { \prime \prime } ( u _ { \mu } ) } ( \nabla \mathcal { A } + \lambda \nabla \mathcal { B } )
$$

(again compare equation 10.9.4). Even more extreme, one might seek an approximation with constant diagonal elements, $\Lambda _ { \mu } = \Lambda$ , so that

$$
\Delta u _ { \mu } = - \frac { 1 } { \Lambda + \lambda f ^ { \prime \prime } ( u _ { \mu } ) } ( \nabla \mathcal { A } + \lambda \nabla \mathcal { B } )
$$

Since $\mathbf { A } ^ { T } \cdot \mathbf { A }$ has something of the nature of a doubly convolved point spread function, and since in real cases one often has a point spread function with a sharp

central peak, even the more extreme of these approximations is often fruitful. One starts with a rough estimate of $\Lambda$ obtained from the $A _ { i \mu }$ ’s, e.g.,

$$
\Lambda \sim \left. \sum _ { i } [ A _ { i \mu } ] ^ { 2 } \right.
$$

An accurate value is not important, since in practice $\Lambda$ is adjusted adaptively: If $\Lambda$ is too large, then equation (19.7.17)’s steps will be too small (that is, larger steps in the same direction will produce even greater decrease in $\mathcal { A } + \lambda \mathcal { B }$ ). If $\Lambda$ is too small, then attempted steps will land in an unfeasible region (negative values of $u _ { \mu }$ ) or will result in an increased $\mathcal { A } + \lambda \mathcal { B }$ . There is an obvious similarity between the adjustment of $\Lambda$ here and the Levenberg-Marquardt method of $\ S 1 5 . 5$ ; this should not be too surprising, since MEM is closely akin to the problem of nonlinear leastsquares fitting. Reference [10] also discusses how the value of $\Lambda + \lambda f ^ { \prime \prime } ( u _ { \mu } )$ can be used to adjust the Lagrange multiplier $\lambda$ so as to converge to the desired value of $\chi ^ { 2 }$ .

All practical MEM algorithms are found to require on the order of 30 to 50 iterations to converge. This convergence behavior is not now understood in any fundamental way.

# 19.7.3 “Bayesian" versus “Historic" Maximum Entropy

Several generalizations of the basic maximum entropy image restoration technique go under the rubric “Bayesian” to distinguish them from the previous “historic” methods. See [11] for details and references. (Our view, of course, is that all the methods are about equally Bayesian, as discussed in $\ S 1 9 . 4 .$ )

- Better priors: We already noted that the entropy functional (equation 19.7.7) is invariant under scrambling all pixels and has no notion of smoothness. The so-called “intrinsic correlation function” (ICF) model (reference [11], where it is called “New MaxEnt”) is similar enough to the entropy functional to allow similar algorithms, but it makes the values of neighboring pixels correlated, enforcing smoothness.   
Better estimation of $\lambda$ : Above we chose $\lambda$ to bring $\chi ^ { 2 }$ into its expected narrow statistical range of $N \pm ( 2 N ) ^ { 1 / 2 }$ . This in effect overestimates $\chi ^ { 2 }$ , however, since some effective number $\gamma$ of parameters are being “fitted” in doing the reconstruction. A Bayesian approach leads to a self-consistent estimate of this  and an objectively better choice for $\lambda$ .

# CITED REFERENCES AND FURTHER READING:

Gzyl, H. 1995, The Method of Maximum Entropy (Singapore: World Scientific).[1]   
Wu, N. 1997, The Maximum Entropy Method (Berlin: Springer).[2]   
Narayan, R., and Nityananda, R. 1986, “Maximum Entropy Image Restoration in Astronomy,” Annual Review of Astronomyand Astrophysics,vol. 24,pp.127-170.[3]   
Skilling, J., and Bryan, R.K. 1984, “Maximum Entropy Image Reconstruction: General Algorithm,” Monthly Notices of the Royal Astronomical Society,vol.211,pp.111-124.[4]   
Burch, S.F., Gull, S.F., and Skilling, J. 1983, “Image Restoration by a Powerful Maximum Entropy Method,” Computer Vision, Graphics and Image Processing, vol. 23, pp. 113–128.[5]   
Skilling, J. 1989, in Maximum Entropy and Bayesian Methods, J. Skilling, ed. (Boston: Kluwer).[6]   
Frieden, B.R. 1983, “Unified Theory for Estimating Frequency-of-Occurrence Laws and Optical Objects,” Journal of the Optical Society of America, vol. 73, pp. 927–938.[7]   
Skilling, J., and Gull, S.F. 1985, in Maximum-Entropy and Bayesian Methods in Inverse Problems,C.R. Smith and W.T. Grandy, Jr.,eds. (Dordrecht: Reidel).[8]   
Skilling, J. 1986, in Maximum Entropy and Bayesian Methods in Applied Statistics, J.H. Justice, ed. (Cambridge, UK: Cambridge University Press).[9]   
Cornwell, T.J., and Evans, K.F. 1985, “A Simple Maximum Entropy Deconvolution Algorithm,” Astronomy and Astrophysics,vol.143,pp.77-83.[10]   
Gull, S.F. 1989, in Maximum Entropy and Bayesian Methods, J. Skilling, ed. (Boston: Kluwer).[11]

# CHAPTE R20

# Partial Differential Equations

# 20.0 Introduction

The numerical treatment of partial differential equations (PDEs) is, by itself, a vast subject. Partial differential equations are at the heart of many, if not most, computer analyses or simulations of continuous physical systems, such as fluids, electromagnetic fields, the human body, and so on. The intent of this chapter is to give the briefest possible useful introduction. Ideally, there would be an entire second volume of Numerical Recipes dealing with partial differential equations alone. (The references [1-4] provide, of course, available alternatives.)

Mathematicians like to classify the partial differential equations that typically occur in applications into three categories, hyperbolic, parabolic, and elliptic, on the basis of their characteristics, or curves of information propagation. The prototypical example of a hyperbolic equation is the one-dimensional wave equation

$$
{ \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } } = v ^ { 2 } { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } }
$$

where $v =$ constant is the velocity of wave propagation. The prototypical parabolic equation is the diffusion equation

$$
\frac { \partial u } { \partial t } = \frac { \partial } { \partial x } \left( D \frac { \partial u } { \partial x } \right)
$$

where $D$ is the diffusion coefficient. The prototypical elliptic equation is the Poisson equation

$$
{ \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } + { \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } } = \rho ( x , y )
$$

where the source term $\rho$ is given. If the source term is equal to zero, the equation is Laplace’s equation.

From a computational point of view, the classification into these three canonical types is not very meaningful — or at least not as important as some other essential distinctions. Equations (20.0.1) and (20.0.2) both define initial value or Cauchy problems: If information on $u$ (perhaps including time derivative information) is given at some initial time $t _ { 0 }$ for all $x$ , then the equations describe how $\boldsymbol { u } ( \boldsymbol { x } , t )$ propagates itself forward in time. In other words, equations (20.0.1) and (20.0.2) describe time evolution. The goal of a numerical code should be to track that time evolution with some desired accuracy.

![](images/92437b479b5096016eb4edf5dcafb5ebafe636690992b09563bbbc27ebe986c7.jpg)  
Figure 20.0.1. Initial value problem (a) and boundary value problem (b) are contrasted. In (a), initial values are given on one “time slice,” and it is desired to advance the solution in time, computing successive rows of open dots in the direction shown by the arrows. Boundary conditions at the left and right edges of each row $( \otimes )$ must also be supplied, but only one row at a time. Only one, or a few, previous rows need be maintained in memory. In (b), boundary values are specified around the edge of a grid, and an iterative process is employed to find the values of all the internal points (open circles). All grid points must be maintained in memory.

By contrast, equation (20.0.3) directs us to find a single “static” function $u ( x , y )$ that satisfies the equation within some $( x , y )$ region of interest, and that — one must also specify — has some desired behavior on the boundary of the region of interest. These problems are called boundary value problems (see Figure 20.0.1). In general it is not possible stably to just “integrate in from the boundary” in the same sense that an initial value problem can be “integrated forward in time.” Therefore, the goal of a numerical code is somehow to converge on the correct solution everywhere at once.

This, then, is the most important classification from a computational point of view: Is the problem at hand an initial value (time evolution) problem? or is it a boundary value (static solution) problem? Figure 20.0.1 emphasizes the distinction. Notice that while the italicized terminology is standard, the terminology in parentheses is a much better description of the dichotomy from a computational perspective. The subclassification of initial value problems into parabolic and hyperbolic is much less important because (i) many actual problems are of a mixed type, and (ii) as we will see, most hyperbolic problems get parabolic pieces mixed into them by the time one is discussing practical computational schemes.

# 20.0.1 Initial Value Problems

An initial value problem is defined by answers to the following questions:

- What are the dependent variables to be propagated forward in time?   
- What is the evolution equation for each variable? Usually the evolution equations will all be coupled, with more than one dependent variable appearing on the right-hand side of each equation.   
- What is the highest time derivative that occurs in each variable’s evolution equation? If possible, this time derivative should be put alone on the equation’s left-hand side. Not only the value of a variable, but also the value of all its time derivatives — up to the highest one — must be specified to define the evolution. What special equations (boundary conditions) govern the evolution in time of points on the boundary of the spatial region of interest? Examples: Dirichlet conditions specify the values of the boundary points as a function of time; Neumann conditions specify the values of the normal gradients on the boundary; outgoing wave boundary conditions are just what they say.

Sections $2 0 . 1 - 2 0 . 3 $ of this chapter deal with initial value problems of several different forms. We make no pretense of completeness, but rather hope to convey a certain amount of generalizable information through a few carefully chosen model examples. These examples will illustrate an important point: One’s principal computational concern must be the stability of the algorithm. Many reasonable-looking algorithms for initial value problems just don’t work — they are numerically unstable.

# 20.0.2 Boundary Value Problems

The questions that define a boundary value problem are

- What are the variables?   
- What equations are satisfied in the interior of the region of interest? What equations are satisfied by points on the boundary of the region of interest? (Here Dirichlet and Neumann conditions are possible choices for elliptic second-order equations, but more complicated boundary conditions can also be encountered.)

In contrast to initial value problems, stability is relatively easy to achieve for boundary value problems. Thus, the efficiency of the algorithms, both in computa-