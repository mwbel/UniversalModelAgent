} } } } while (ju-jl > 1) { Hunt is done, so begin the final bisection phase: jm $=$ (ju+jl) >> 1; if (x >= xx[jm] $= =$ ascnd) jl=jm; else ju=jm; cor $=$ abs(jl-jsav) $>$ dj ? 0 : 1; Decide whether to use hunt or locate next jsav $= \ j 1$ ; time. return MAX(0,MIN(n-mm,jl-((mm-2)>>1)));

The methods locate and hunt each update the boolean variable cor in the base class, indicating whether consecutive calls seem correlated. That variable is then used by interp to decide whether to use locate or hunt on the next call. This is all invisible to the user, of course.

# 3.1.2 Example: Linear Interpolation

You may think that, at this point, we have wandered far from the subject of interpolation methods. To show that we are actually on track, here is a class that efficiently implements piecewise linear interpolation.

struct Linear_interp : Base_interp   
Piecewise linear interpolation object. Construct with x and y vectors, then call interp for interpolated values.

Linear_interp(VecDoub_I &xv, VecDoub_I &yv) : Base_interp(xv,&yv[0],2) {} Doub rawinterp(Int j, Doub x) if (xx[j] $= =$ xx[j+1]) return yy[j]; Table is defective, but we can recover. else return yy[j] $^ +$ ((x-xx[j])/(xx[j+1]-xx[j]))\*(yy[j+1]-yy[j]); } };

You construct a linear interpolation object by declaring an instance with your filled vectors of abscissas $x _ { i }$ and function values $y _ { i } = f ( x _ { i } )$ ,

Int n=...;  
VecDoub xx(n), yy(n);  
Linear_interp myfunc(xx,yy);

Behind the scenes, the base class constructor is called with $M = 2$ because linear interpolation uses just the two points bracketing a value. Also, pointers to the data are saved. (You must ensure that the vectors $\tt x x$ and yy don’t go out of scope while myfunc is in use.)

When you want an interpolated value, it’s as simple as

Doub x,y;   
$\mathrm { ~ y ~ } =$ myfunc.interp(x);

If you have several functions that you want to interpolate, you declare a separate instance of Linear_interp for each one.

We will now use the same interface for more advanced interpolation methods.

# CITED REFERENCES AND FURTHER READING:

Knuth, D.E. 1997, Sorting and Searching, 3rd ed., vol. 3 of The Art of Computer Programming (Reading, MA: Addison-Wesley), $\ S 6 . 2 . 1$ .

# 3.2 Polynomial Interpolation and Extrapolation

Through any two points there is a unique line. Through any three points there is a unique quadratic. Et cetera. The interpolating polynomial of degree $M - 1$ through the $M$ points $y _ { 0 } = f ( x _ { 0 } ) , y _ { 1 } = f ( x _ { 1 } ) , \ldots , y _ { M - 1 } = f ( x _ { M - 1 } )$ is given explicitly by Lagrange’s classical formula,

$$
\begin{array} { l } { { P ( x ) = \displaystyle \frac { ( x - x _ { 1 } ) ( x - x _ { 2 } ) . . . ( x - x _ { M - 1 } ) } { ( x _ { 0 } - x _ { 1 } ) ( x _ { 0 } - x _ { 2 } ) . . . ( x _ { 0 } - x _ { M - 1 } ) } y _ { 0 } } } \\ { { + \displaystyle \frac { ( x - x _ { 0 } ) ( x - x _ { 2 } ) . . . ( x - x _ { M - 1 } ) } { ( x _ { 1 } - x _ { 0 } ) ( x _ { 1 } - x _ { 2 } ) . . . ( x _ { 1 } - x _ { M - 1 } ) } y _ { 1 } + \cdots } } \\ { { + \displaystyle \frac { ( x - x _ { 0 } ) ( x - x _ { 1 } ) . . . ( x - x _ { M - 2 } ) } { ( x _ { M - 1 } - x _ { 0 } ) ( x _ { M - 1 } - x _ { 1 } ) . . . ( x _ { M - 1 } - x _ { M - 2 } ) } y _ { M - 1 } } } \end{array}
$$

There are $M$ terms, each a polynomial of degree $M - 1$ and each constructed to be zero at all of the $x _ { i }$ ’s except one, at which it is constructed to be $y _ { i }$ .

It is not terribly wrong to implement the Lagrange formula straightforwardly, but it is not terribly right either. The resulting algorithm gives no error estimate, and it is also somewhat awkward to program. A much better algorithm (for constructing the same, unique, interpolating polynomial) is Neville’s algorithm, closely related to and sometimes confused with Aitken’s algorithm, the latter now considered obsolete.

Let $P _ { 0 }$ be the value at $x$ of the unique polynomial of degree zero (i.e., a constant) passing through the point $( x _ { 0 } , y _ { 0 } )$ ; so $P _ { 0 } = y _ { 0 }$ . Likewise define $P _ { 1 } , P _ { 2 } , \ldots$ ; $P _ { M - 1 }$ . Now let $P _ { 0 1 }$ be the value at $x$ of the unique polynomial of degree one passing through both $( x _ { 0 } , y _ { 0 } )$ and $( x _ { 1 } , y _ { 1 } )$ . Likewise $P _ { 1 2 }$ $, P _ { 2 3 } , . . . , P _ { ( M - 2 ) ( M - 1 ) }$ . Similarly, for higher-order polynomials, up to $P _ { 0 1 2 . . . ( M - 1 ) }$ , which is the value of the unique interpolating polynomial through all $M$ points, i.e., the desired answer. The various $P$ ’s form a “tableau” with “ancestors” on the left leading to a single “descendant” at the extreme right. For example, with $M = 4$ ,

$$
\begin{array} { l l l l l l } { { x _ { 0 } : } } & { { \mathrm { } } } & { { y _ { 0 } = P _ { 0 } } } & { { } } & { { } } & { { } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { P _ { 0 1 } } } & { { } } & { { } } \\ { { x _ { 1 } : } } & { { \mathrm { } } } & { { y _ { 1 } = P _ { 1 } } } & { { } } & { { P _ { 0 1 2 } } } & { { } } \\ { { } } & { { } } & { { } } & { { P _ { 1 2 } } } & { { } } & { { P _ { 0 1 2 3 } } } \\ { { x _ { 2 } : } } & { { \mathrm { } } } & { { y _ { 2 } = P _ { 2 } } } & { { } } & { { P _ { 1 2 3 } } } & { { } } \\ { { } } & { { } } & { { } } & { { } } & { { P _ { 2 3 } } } & { { } } & { { } } \\ { { x _ { 3 } : } } & { { \mathrm { } } } & { { y _ { 3 } = P _ { 3 } } } & { { } } & { { } } & { { } } & { { } } \end{array}
$$

Neville’s algorithm is a recursive way of filling in the numbers in the tableau a column at a time, from left to right. It is based on the relationship between a

“daughter” $P$ and its two “parents,”

$$
P _ { i ( i + 1 ) \dots ( i + m ) } = { \frac { ( x - x _ { i + m } ) P _ { i ( i + 1 ) \dots ( i + m - 1 ) } + ( x _ { i } - x ) P _ { ( i + 1 ) ( i + 2 ) \dots ( i + m ) } } { x _ { i } - x _ { i + m } } }
$$

This recurrence works because the two parents already agree at points $x _ { i + 1 } \ldots$ $x _ { i + m - 1 }$ .

An improvement on the recurrence (3.2.3) is to keep track of the small differences between parents and daughters, namely to define (for $m = 1 , 2 , \ldots , M - 1 )$ ,

$$
\begin{array} { l } { { C _ { m , i } \equiv P _ { i \dots ( i + m ) } - P _ { i \dots ( i + m - 1 ) } } } \\ { { D _ { m , i } \equiv P _ { i \dots ( i + m ) } - P _ { ( i + 1 ) \dots ( i + m ) } . } } \end{array}
$$

Then one can easily derive from (3.2.3) the relations

$$
\begin{array} { l } { \displaystyle { D _ { m + 1 , i } = \frac { ( x _ { i + m + 1 } - x ) ( C _ { m , i + 1 } - D _ { m , i } ) } { x _ { i } - x _ { i + m + 1 } } } } \\ { \displaystyle { C _ { m + 1 , i } = \frac { ( x _ { i } - x ) ( C _ { m , i + 1 } - D _ { m , i } ) } { x _ { i } - x _ { i + m + 1 } } } } \end{array}
$$

At each level $m$ , the $C$ ’s and $D$ ’s are the corrections that make the interpolation one order higher. The final answer $P _ { 0 . . . ( M - 1 ) }$ is equal to the sum of any $y _ { i }$ plus a set of $C$ ’s and/or $D$ ’s that form a path through the family tree to the rightmost daughter.

Here is the class implementing polynomial interpolation or extrapolation. All of its “support infrastructure” is in the base class Base_interp. It needs only to provide a rawinterp method that contains Neville’s algorithm.

# struct Poly_interp : Base_interp

Polynomial interpolation object. Construct with $\mathbf { x }$ and $\mathbf { y }$ vectors, and the number $M$ of points to be used locally (polynomial order plus one), then call interp for interpolated values.

Doub dy; Poly_interp(VecDoub_I &xv, VecDoub_I &yv, Int m) : Base_interp(xv,&yv[0],m), dy(0.) {} Doub rawinterp(Int jl, Doub x);

# };

# Doub Poly_interp::rawinterp(Int jl, Doub x)

Given a value $\mathbf { x }$ , and using pointers to data xx and yy, this routine returns an interpolated value y, and stores an error estimate dy. The returned value is obtained by mm-point polynomial interpolation on the subrange $\mathbf { x } \mathbf { x } \left[ \mathbf { j } \mathbf { 1 } . . . \mathbf { j } \mathbf { 1 } + \mathbf { m m } ^ { - 1 } \right]$ .

Int i,m,ns ${ = } 0$ ;   
Doub y,den,dif,dift,ho,hp,w;   
const Doub \*xa $=$ &xx[jl], \*ya $=$ &yy[jl];   
VecDoub c(mm),d(mm);   
dif $=$ abs(x-xa[0]);   
for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<mm; $\dot { 1 } + +$ ) { Here we find the index ns of the closest table entry, if ((dift $=$ abs(x-xa[i])) $<$ dif) { ns=i; dif=dift; } c[i]=ya[i]; and initialize the tableau of c’s and d’s. d[i]=ya[i];   
}   
y=ya[ns--]; This is the initial approximation to y.   
for ( $\scriptstyle { \mathtt { m } } = 1$ ;m<mm;m++) { For each column of the tableau,

for (i=0;i<mm-m;i++) { we loop over the current c’s and d’s and update ho=xa[i]-x; them. hp=xa[i+m]-x; w=c[i+1]-d[i]; if ((den=ho-hp) == 0.0) throw("Poly_interp error"); This error can occur only if two input xa’s are (to within roundoff) identical. den=w/den; d[i] $\risingdotseq$ hp\*den; Here the c’s and d’s are updated. c[i] $=$ ho\*den; $\begin{array} { r } { \mathrm { ~  ~ y ~ } + = \mathrm { ~  ~ ( d y = ( 2 * ( n s + 1 ) ~  ~ < ~ ( m m - m ) ~  ~ \stackrel { { ~ \wedge ~ } } { ~ } c ~ \unboldmath [ n s + 1 ] ~ \unboldmath : ~ d [ n s - - 1 ) ~ ) ~ } ; } \end{array}$ After each column in the tableau is completed, we decide which correction, c or d, we want to add to our accumulating value of y, i.e., which path to take through the tableau — forking up or down. We do this in such a way as to take the most “straight line” route through the tableau to its apex, updating ns accordingly to keep track of where we are. This route keeps the partial approximations centered (insofar as possible) on the target $\mathbf { x }$ . The last dy added is thus the error indication. } return y;

The user interface to Poly_interp is virtually the same as for Linear_interp (end of -3.1), except that an additional argument in the constructor sets $M$ , the number of points used (the order plus one). A cubic interpolator looks like this:

Int n=...;   
VecDoub xx(n), yy(n);   
Poly_interp myfunc(xx,yy,4);

Poly_interp stores an error estimate dy for the most recent call to its interp function:

Doub x,y,err;   
$\mathtt { y } =$ myfunc.interp(x);   
err $=$ myfunc.dy;

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, $\ S 2 5 . 2$ .   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 2 . 1$ .   
Gear, C.W. 1971, Numerical Initial Value Problems in Ordinary Differential Equations (Englewood Cliffs, NJ: Prentice-Hall), $\ S 6 . 1$ .

# 3.3 Cubic Spline Interpolation

Given a tabulated function $y _ { i } = y ( x _ { i } )$ ; $i = 0 . . . N - 1$ , focus attention on one particular interval, between $x _ { j }$ and $x _ { j + 1 }$ . Linear interpolation in that interval gives the interpolation formula

$$
y = A y _ { j } + B y _ { j + 1 }
$$

where

$$
A \equiv { \frac { x _ { j + 1 } - x } { x _ { j + 1 } - x _ { j } } } \qquad B \equiv 1 - A = { \frac { x - x _ { j } } { x _ { j + 1 } - x _ { j } } }
$$

Equations (3.3.1) and (3.3.2) are a special case of the general Lagrange interpolation formula (3.2.1).

Since it is (piecewise) linear, equation (3.3.1) has zero second derivative in the interior of each interval and an undefined, or infinite, second derivative at the abscissas $x _ { j }$ . The goal of cubic spline interpolation is to get an interpolation formula that is smooth in the first derivative and continuous in the second derivative, both within an interval and at its boundaries.

Suppose, contrary to fact, that in addition to the tabulated values of $y _ { i }$ , we also have tabulated values for the function’s second derivatives, $y ^ { \prime \prime }$ , that is, a set of numbers $y _ { i } ^ { \prime \prime }$ . Then, within each interval, we can add to the right-hand side of equation (3.3.1) a cubic polynomial whose second derivative varies linearly from a value $y _ { j } ^ { \prime \prime }$ on the left to a value $y _ { j + 1 } ^ { \prime \prime }$ on the right. Doing so, we will have the desired continuous second derivative. If we also construct the cubic polynomial to have zero values at $x _ { j }$ and $x _ { j + 1 }$ , then adding it in will not spoil the agreement with the tabulated functional values $y _ { j }$ and $y _ { j + 1 }$ at the endpoints $x _ { j }$ and $x _ { j + 1 }$ .

A little side calculation shows that there is only one way to arrange this construction, namely replacing (3.3.1) by

$$
y = A y _ { j } + B y _ { j + 1 } + C y _ { j } ^ { \prime \prime } + D y _ { j + 1 } ^ { \prime \prime }
$$

where $A$ and $B$ are defined in (3.3.2) and

$$
{ \begin{array} { r l r } { C \equiv { \frac { 1 } { 6 } } ( A ^ { 3 } - A ) ( x _ { j + 1 } - x _ { j } ) ^ { 2 } } & { { } } & { D \equiv { \frac { 1 } { 6 } } ( B ^ { 3 } - B ) ( x _ { j + 1 } - x _ { j } ) ^ { 2 } } \end{array} }
$$

Notice that the dependence on the independent variable $x$ in equations (3.3.3) and (3.3.4) is entirely through the linear $x$ -dependence of $A$ and $B$ , and (through $A$ and $B$ ) the cubic $x$ -dependence of $C$ and $D$ .

We can readily check that $y ^ { \prime \prime }$ is in fact the second derivative of the new interpolating polynomial. We take derivatives of equation (3.3.3) with respect to $x$ , using the definitions of $A , B , C$ ; and $D$ to compute $d A / d x , d B / d x , d C / d x$ , and $d D / d x$ . The result is

$$
\frac { d y } { d x } = \frac { y _ { j + 1 } - y _ { j } } { x _ { j + 1 } - x _ { j } } - \frac { 3 A ^ { 2 } - 1 } { 6 } ( x _ { j + 1 } - x _ { j } ) y _ { j } ^ { \prime \prime } + \frac { 3 B ^ { 2 } - 1 } { 6 } ( x _ { j + 1 } - x _ { j } ) y _ { j + 1 } ^ { \prime \prime }
$$

for the first derivative, and

$$
{ \frac { d ^ { 2 } y } { d x ^ { 2 } } } = A y _ { j } ^ { \prime \prime } + B y _ { j + 1 } ^ { \prime \prime }
$$

for the second derivative. Since $A = 1$ at $x _ { j }$ , $A = 0$ at $x _ { j + 1 }$ , while $B$ is just the other way around, (3.3.6) shows that $y ^ { \prime \prime }$ is just the tabulated second derivative, and also that the second derivative will be continuous across, e.g., the boundary between the two intervals $( x _ { j - 1 } , x _ { j } )$ and $( x _ { j } , x _ { j + 1 } )$ .

The only problem now is that we supposed the $y _ { i } ^ { \prime \prime }$ ’s to be known, when, actually, they are not. However, we have not yet required that the first derivative, computed from equation (3.3.5), be continuous across the boundary between two intervals. The key idea of a cubic spline is to require this continuity and to use it to get equations for the second derivatives $y _ { i } ^ { \prime \prime }$ .

The required equations are obtained by setting equation (3.3.5) evaluated for $x = x _ { j }$ in the interval $( x _ { j - 1 } , x _ { j } )$ equal to the same equation evaluated for $x = x _ { j }$ but in the interval $( x _ { j } , x _ { j + 1 } )$ . With some rearrangement, this gives (for $j = 1 , \ldots$ ; $N - 2 )$

$$
\frac { x _ { j } - x _ { j - 1 } } { 6 } y _ { j - 1 } ^ { \prime \prime } + \frac { x _ { j + 1 } - x _ { j - 1 } } { 3 } y _ { j } ^ { \prime \prime } + \frac { x _ { j + 1 } - x _ { j } } { 6 } y _ { j + 1 } ^ { \prime \prime } = \frac { y _ { j + 1 } - y _ { j } } { x _ { j + 1 } - x _ { j } } - \frac { y _ { j } - y _ { j - 1 } } { x _ { j } - x _ { j - 1 } }
$$

These are $N - 2$ linear equations in the $N$ unknowns $y _ { i } ^ { \prime \prime } , i = 0 , \ldots , N - 1$ . Therefore there is a two-parameter family of possible solutions.

For a unique solution, we need to specify two further conditions, typically taken as boundary conditions at $x _ { 0 }$ and $x N { - } 1$ . The most common ways of doing this are either

- set one or both of $y _ { 0 } ^ { \prime \prime }$ and $y _ { N - 1 } ^ { \prime \prime }$ equal to zero, giving the so-called natural cubic spline, which has zero second derivative on one or both of its boundaries, or - set either of $y _ { 0 } ^ { \prime \prime }$ and $y _ { N - 1 } ^ { \prime \prime }$ to values calculated from equation (3.3.5) so as to make the first derivative of the interpolating function have a specified value on either or both boundaries.

Although the boundary condition for natural splines is commonly used, another possibility is to estimate the first derivatives at the endpoints from the first and last few tabulated points. For details of how to do this, see the end of $\ S 3 . 7$ . Best, of course, is if you can compute the endpoint first derivatives analytically.

One reason that cubic splines are especially practical is that the set of equations (3.3.7), along with the two additional boundary conditions, are not only linear, but also tridiagonal. Each $y _ { j } ^ { \prime \prime }$ is coupled only to its nearest neighbors at $j \pm 1$ . Therefore, the equations can be solved in $O ( N )$ operations by the tridiagonal algorithm (-2.4). That algorithm is concise enough to build right into the function called by the constructor.

The object for cubic spline interpolation looks like this:

struct Spline_interp : Base_interp

Cubic spline interpolation object. Construct with $\mathbf { x }$ and $\mathbf { y }$ vectors, and (optionally) values of the first derivative at the endpoints, then call interp for interpolated values.

VecDoub y2;

Spline_interp(VecDoub_I &xv, VecDoub_I &yv, Doub yp1=1.e99, Doub ypn=1.e99)   
: Base_interp(xv,&yv[0],2), y2(xv.size())   
{sety2(&xv[0],&yv[0],yp1,ypn);}   
Spline_interp(VecDoub_I &xv, const Doub \*yv, Doub yp $\scriptstyle 1 = 1$ .e99, Doub ypn $^ { = 1 }$ .e99)   
: Base_interp(xv,yv,2), y2(xv.size())   
{sety2(&xv[0],yv,yp1,ypn);} void sety2(const Doub \*xv, const Doub \*yv, Doub yp1, Doub ypn);   
Doub rawinterp(Int jl, Doub xv);

For now, you can ignore the second constructor; it will be used later for two-dimensional spline interpolation.

The user interface differs from previous ones only in the addition of two constructor arguments, used to set the values of the first derivatives at the endpoints, $y _ { 0 } ^ { \prime }$ and $y _ { N - 1 } ^ { \prime }$ . These are coded with default values that signal that you want a natural spline, so they can be omitted in most situations. Both constructors invoke sety2 to do the actual work of computing, and storing, the second derivatives.

void Spline_interp::sety2(const Doub \*xv, const Doub \*yv, Doub yp1, Doub ypn) This routine stores an array $\mathtt { y 2 } [ 0 \ldots \mathtt { n } { - } 1 ]$ with second derivatives of the interpolating function at the tabulated points pointed to by xv, using function values pointed to by yv. If yp1 and/or ypn are equal to $1 \times 1 0 ^ { 9 9 }$ or larger, the routine is signaled to set the corresponding boundary condition for a natural spline, with zero second derivative on that boundary; otherwise, they are the values of the first derivatives at the endpoints.

Int i,k;   
Doub p,qn,sig,un;   
Int n=y2.size();   
VecDoub $\mathtt { u } ( \mathtt { n } ^ { - 1 } )$ ;   
if (yp1 $>$ 0.99e99) The lower boundary condition is set either to be “nat-${ \tt y } 2 \left[ 0 \right] = { \tt u } \left[ 0 \right] = 0 . 0 \ \mathrm { : }$ ; ural”   
else { or else to have a specified first derivative. y2[0] $= - 0 . 5$ ; u[0] $=$ (3.0/(xv[1]-xv[0]))\*((yv[1]-yv[0])/(xv[1]-xv[0])-yp1);   
}   
for ( $\dot { 1 } = 1$ ;i<n-1; $\dot { 1 } + + \dot { 1 }$ ) { This is the decomposition loop of the tridiagonal alsig=(xv[i]-xv[i-1])/(xv[i+1]-xv[i-1]); gorithm. y2 and u are used for temp=sig\*y2[i-1]+2.0; porary storage of the decomposed y2[i] $=$ (sig-1.0)/p; factors. u[i] $=$ (yv[i+1]-yv[i])/(xv[i+1]-xv[i]) - (yv[i]-yv[i-1])/(xv[i]-xv[i-1]); u[i] $=$ (6.0\*u[i]/(xv[i+1]-xv[i-1])-sig\*u[i-1])/p;   
}   
if (ypn $>$ 0.99e99) The upper boundary condition is set either to be qn=un=0.0; “natural”   
else { or else to have a specified first derivative. qn=0.5; un=(3.0/(xv[n-1]-xv[n-2]))\*(ypn-(yv[n-1]-yv[n-2])/(xv[n-1]-xv[n-2]));   
}   
y2[n-1] $=$ (un-qn\*u[n-2])/(qn\*y2[n-2]+1.0);   
for (k=n-2;k>=0;k--) This is the backsubstitution loop of the tridiagonal y2[k]=y2[k]\*y2[k+1]+u[k]; algorithm.

Note that, unlike the previous object Poly_interp, Spline_interp stores data that depend on the contents of your array of $y _ { i }$ ’s at its time of creation — a whole vector y2. Although we didn’t point it out, the previous interpolation object actually allowed the misuse of altering the contents of their $x$ and $y$ arrays on the fly (as long as the lengths didn’t change). If you do that with Spline_interp, you’ll get definitely wrong answers!

The required rawinterp method, never called directly by the users, uses the stored y2 and implements equation (3.3.3):

Doub Spline_interp::rawinterp(Int jl, Doub x)   
Given a value x, and using pointers to data xx and yy, and the stored vector of second derivatives y2, this routine returns the cubic spline interpolated value y.   
{ Int klo=jl,khi=jl+1;   
Doub y,h,b,a;   
h=xx[khi]-xx[klo];   
if $\mathit { \Omega } ^ { \prime } \mathbf { h } \ = = \ 0 . 0$ ) throw("Bad input to routine splint");   
$\mathtt { a } =$ (xx[khi]-x)/h;

The xa’s must be distinct.

$\mathtt { b } =$ (x-xx[klo])/h; Cubic spline polynomial is now evaluated.   
y=a\*yy[klo]+b\*yy[khi]+((a\*a\*a-a)\*y2[klo] +(b\*b\*b-b)\*y2[khi]) $^ *$ (h\*h)/6.0;   
return y;

Typical use looks like this:

Int n=...;   
VecDoub xx(n), yy(n);   
Spline_interp myfunc(xx,yy);

and then, as often as you like,

Doub x,y;   
y = myfunc.interp(x);

Note that no error estimate is available.

# CITED REFERENCES AND FURTHER READING:

De Boor, C. 1978, A Practical Guide to Splines (New York: Springer).   
Ueberhuber, C.W. 1997, Numerical Computation: Methods, Software, and Analysis, vol. 1 (Berlin: Springer), Chapter 9.   
Forsythe, G.E., Malcolm, M.A., and Moler, C.B. 1977, Computer Methods for Mathematical Computations (Englewood Cliffs, NJ: Prentice-Hall), $\ S 4 . 4 - \ S 4 . 5$ .   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 2 . 4$ .   
Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), $\ S 3 . 8$ .

# 3.4 Rational Function Interpolation and Extrapolation

Some functions are not well approximated by polynomials but are well approximated by rational functions, that is quotients of polynomials. We denote by $R _ { i ( i + 1 ) \dots ( i + m ) }$ a rational function passing through the $m + 1$ points $( x _ { i } , y _ { i } ) , \ldots$ ; $( x _ { i + m } , y _ { i + m } )$ . More explicitly, suppose

$$
R _ { i ( i + 1 ) \ldots ( i + m ) } = { \frac { P _ { \mu } ( x ) } { Q _ { \nu } ( x ) } } = { \frac { p _ { 0 } + p _ { 1 } x + \dots + p _ { \mu } x ^ { \mu } } { q _ { 0 } + q _ { 1 } x + \dots + q _ { \nu } x ^ { \nu } } }
$$

Since there are $\mu + \nu + 1$ unknown $p$ ’s and $q$ ’s ( $\scriptstyle { \dot { q } } _ { 0 }$ being arbitrary), we must have

$$
m + 1 = \mu + \nu + 1
$$

In specifying a rational function interpolating function, you must give the desired order of both the numerator and the denominator.

Rational functions are sometimes superior to polynomials, roughly speaking, because of their ability to model functions with poles, that is, zeros of the denominator of equation (3.4.1). These poles might occur for real values of $x$ , if the function to be interpolated itself has poles. More often, the function $f ( x )$ is finite for all finite real $x$ but has an analytic continuation with poles in the complex $x$ -plane. Such poles can themselves ruin a polynomial approximation, even one restricted to real values of $x$ , just as they can ruin the convergence of an infinite power series in $x$ . If you draw a circle in the complex plane around your $m$ tabulated points, then you should not expect polynomial interpolation to be good unless the nearest pole is rather far outside the circle. A rational function approximation, by contrast, will stay “good” as long as it has enough powers of $x$ in its denominator to account for (cancel) any nearby poles.

For the interpolation problem, a rational function is constructed so as to go through a chosen set of tabulated functional values. However, we should also mention in passing that rational function approximations can be used in analytic work. One sometimes constructs a rational function approximation by the criterion that the rational function of equation (3.4.1) itself have a power series expansion that agrees with the first $m + 1$ terms of the power series expansion of the desired function $f ( x )$ . This is called Pade approximation´ and is discussed in $\ S 5 . 1 2$ .

Bulirsch and Stoer found an algorithm of the Neville type that performs rational function extrapolation on tabulated data. A tableau like that of equation (3.2.2) is constructed column by column, leading to a result and an error estimate. The Bulirsch-Stoer algorithm produces the so-called diagonal rational function, with the degrees of the numerator and denominator equal (if $m$ is even) or with the degree of the denominator larger by one (if $m$ is odd; cf. equation 3.4.2 above). For the derivation of the algorithm, refer to [1]. The algorithm is summarized by a recurrence relation exactly analogous to equation (3.2.3) for polynomial approximation:

$$
\begin{array} { r l } & { R _ { i ( i + 1 ) \dots ( i + m ) } = R _ { ( i + 1 ) \dots ( i + m ) } } \\ & { \qquad + \frac { R _ { ( i + 1 ) \dots ( i + m ) } - R _ { i \dots ( i + m - 1 ) } } { \left( \frac { x - x _ { i } } { x - x _ { i + m } } \right) \left( 1 - \frac { R _ { ( i + 1 ) \dots ( i + m ) } - R _ { i \dots ( i + m - 1 ) } } { R _ { ( i + 1 ) \dots ( i + m ) } - R _ { ( i + 1 ) \dots ( i + m - 1 ) } } \right) - 1 } } \end{array}
$$

This recurrence generates the rational functions through $m + 1$ points from the ones through $m$ and (the term $R _ { ( i + 1 ) \dots ( i + m - 1 ) }$ in equation $3 . 4 . 3 ) m - 1$ points. It is started with

$$
R _ { i } = y _ { i }
$$

and with

$$
{ \cal R } \equiv [ R _ { i ( i + 1 ) \ldots ( i + m ) } \quad \mathrm { w i t h } \quad m = - 1 ] = 0
$$

Now, exactly as in equations (3.2.4) and (3.2.5) above, we can convert the recurrence (3.4.3) to one involving only the small differences

$$
\begin{array} { l } { { C _ { m , i } \equiv R _ { i \dots ( i + m ) } - R _ { i \dots ( i + m - 1 ) } } } \\ { { D _ { m , i } \equiv R _ { i \dots ( i + m ) } - R _ { ( i + 1 ) \dots ( i + m ) } } } \end{array}
$$

Note that these satisfy the relation

$$
C _ { m + 1 , i } - D _ { m + 1 , i } = C _ { m , i + 1 } - D _ { m , i }
$$

which is useful in proving the recurrences

$$
\begin{array} { r l } & { D _ { m + 1 , i } = \frac { C _ { m , i + 1 } \left( C _ { m , i + 1 } - D _ { m , i } \right) } { \left( \frac { x - x _ { i } } { x - x _ { i + m + 1 } } \right) D _ { m , i } - C _ { m , i + 1 } } } \\ & { C _ { m + 1 , i } = \frac { \left( \frac { x - x _ { i } } { x - x _ { i + m + 1 } } \right) D _ { m , i } \left( C _ { m , i + 1 } - D _ { m , i } \right) } { \left( \frac { x - x _ { i } } { x - x _ { i + m + 1 } } \right) D _ { m , i } - C _ { m , i + 1 } } } \end{array}
$$

The class for rational function interpolation is identical to that for polynomial interpolation in every way, except, of course, for the different method implemented in rawinterp. See the end of $\ S 3 . 2$ for usage. Plausible values for $M$ are in the range 4 to 7.

# struct Rat_interp : Base_interp

Diagonal rational function interpolation object. Construct with $\mathbf { x }$ and $\mathbf { y }$ vectors, and the number m of points to be used locally, then call interp for interpolated values.

Doub dy; Rat_interp(VecDoub_I &xv, VecDoub_I &yv, Int m) : Base_interp(xv,&yv[0],m), dy(0.) {} Doub rawinterp(Int jl, Doub x);

# Doub Rat_interp::rawinterp(Int jl, Doub x)

Given a value $\mathbf { x }$ , and using pointers to data xx and yy, this routine returns an interpolated value y, and stores an error estimate dy. The returned value is obtained by mm-point diagonal rational function interpolation on the subrange $\mathbf { x } \mathbf { x } \left[ \mathbf { j } \mathbf { 1 } . . \mathbf { j } \mathbf { 1 } + \mathbf { m m } - 1 \right]$ .

const Doub TINY $^ { = 1 }$ .0e-99; A small number.   
Int m,i,ns=0;   
Doub y,w,t,hh,h,dd;   
const Doub \*xa $=$ &xx[jl], \*ya = &yy[jl];   
VecDoub c(mm),d(mm);   
hh=abs(x-xa[0]);   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<mm; $\dot { 1 } + + \dot { 2 }$ ) { $\mathrm { h } =$ abs(x-xa[i]); if $( \mathbf { h _ { \alpha } } = = \mathbf { \beta } 0 . 0 ) ^ { \prime }$ ) { dy=0.0; return ya[i]; } else if (h $<$ hh) $\mathbf { n } \mathbf { s } { = } \dot { \mathbf { 1 } }$ ; hh=h; } c[i]=ya[i]; d[i]=ya[i]+TINY; The TINY part is needed to prevent a rare zero-over-zero   
} condition.   
y=ya[ns--];   
for $\scriptstyle ( { \mathtt { m } } = 1$ ;m<mm;m++) { for (i=0;i<mm-m;i++) { w=c[i+1]-d[i]; h=xa[i+m]-x; h will never be zero, since this was tested in the initial-$\mathtt { t } =$ (xa[i]-x)\*d[i]/h; izing loop. dd=t-c[i+1]; if ( $\mathsf { d } \mathsf { d } \ = = \ 0 . 0 \rangle$ ) throw("Error in routine ratint"); This error condition indicates that the interpolating function has a pole at the requested value of x. dd=w/dd; d[i] $= \mathtt { c }$ [i+1]\*dd; c[i]=t\*dd;

} y += (dy=(2\*(ns+1) < (mm-m) ? c[ns+1] : d[ns--])); } return y;

# 3.4.1 Barycentric Rational Interpolation

Suppose one tries to use the above algorithm to construct a global approximation on the entire table of values using all the given nodes $x _ { 0 } , x _ { 1 } , \ldots , x _ { N - 1 }$ . One potential drawback is that the approximation can have poles inside the interpolation interval where the denominator in (3.4.1) vanishes, even if the original function has no poles there. An even greater (related) hazard is that we have allowed the order of the approximation to grow to $N - 1$ , probably much too large.

An alternative algorithm can be derived [2] that has no poles anywhere on the real axis, and that allows the actual order of the approximation to be specified to be any integer $d \digamma < N$ . The trick is to make the degree of both the numerator and the denominator in equation (3.4.1) be $N - 1$ . This requires that the $p$ ’s and the $q$ ’s not be independent, so that equation (3.4.2) no longer holds.

The algorithm utilizes the barycentric form of the rational interpolant

$$
R ( x ) = { \frac { \displaystyle \sum _ { i = 0 } ^ { N - 1 } { \frac { w _ { i } } { x - x _ { i } } } y _ { i } } { \displaystyle \sum _ { i = 0 } ^ { N - 1 } { \frac { w _ { i } } { x - x _ { i } } } } }
$$

One can show that by a suitable choice of the weights $w _ { i }$ , every rational interpolant can be written in this form, and that, as a special case, so can polynomial interpolants [3]. It turns out that this form has many nice numerical properties. Barycentric rational interpolation competes very favorably with splines: its error is often smaller, and the resulting approximation is infinitely smooth (unlike splines).

Suppose we want our rational interpolant to have approximation order $d$ , i.e., if the spacing of the points is $O ( h )$ , the error is $O ( h ^ { d + 1 } )$ as $h  0$ . Then the formula for the weights is

$$
w _ { k } = \sum _ { \stackrel { i = k - d } { 0 \leq i < N - d } } ^ { k } ( - 1 ) ^ { k } \prod _ { \stackrel { j = i } { j \neq k } } ^ { i + d } \frac { 1 } { x _ { k } - x _ { j } }
$$

For example,

$$
\begin{array} { l l } { { w _ { k } = ( - 1 ) ^ { k } , ~ } } & { { d = 0 } } \\ { { w _ { k } = ( - 1 ) ^ { k - 1 } \left[ \displaystyle \frac { 1 } { x _ { k } - x _ { k - 1 } } + \displaystyle \frac { 1 } { x _ { k + 1 } - x _ { k } } \right] , ~ } } & { { d = 1 } } \end{array}
$$

In the last equation, you omit the terms in $w _ { 0 }$ and $w _ { N - 1 }$ that refer to out-of-range values of $x _ { k }$ .

Here is a routine that implements barycentric rational interpolation. Given a set of $N$ nodes and a desired order $d$ , with $d \digamma < N$ , it first computes the weights $w _ { k }$ . Then subsequent calls to interp evaluate the interpolant using equation (3.4.9). Note that the parameter $\mathrm { j } \mathrm { 1 }$ of rawinterp is not used, since the algorithm is designed to construct an approximation on the entire interval at once.

The workload to construct the weights is of order $O ( N d )$ operations. For small $d$ , this is not too different from splines. Note, however, that the workload for each subsequent interpolated value is $O ( N )$ , not $O ( d )$ as for splines.

# struct BaryRat_interp : Base_interp

Barycentric rational interpolation object. After constructing the object, call interp for interpolated values. Note that no error estimate dy is calculated.

VecDoub w; Int d; BaryRat_interp(VecDoub_I &xv, VecDoub_I &yv, Int dd); Doub rawinterp(Int jl, Doub x); Doub interp(Doub x); ;

BaryRat_interp::BaryRat_interp(VecDoub_I &xv, VecDoub_I &yv, Int dd) : Base_interp(xv,&yv[0],xv.size()), w(n), d(dd)   
Constructor arguments are $\mathbf { x }$ and $\mathbf { y }$ vectors of length n, and order $d$ of desired approximation.   
{   
if ( $\scriptstyle \mathbf { n < = d } ,$ ) throw("d too large for number of points in BaryRat_interp");   
for (Int $\mathtt { k } = 0$ ;k<n;k++) { Compute weights from equation (3.4.10). Int imin=MAX(k-d,0); Int imax = k >= n-d ? n-d-1 : k; Doub temp $=$ imin & 1 ? -1.0 : 1.0; Doub sum $= 0 . ($ 0; for (Int $\dot { \bf 1 } =$ imin;i $\cdot { } ^ { < = }$ imax;i++) { Int jmax MIN(i+d,n-1); Doub term $^ { 1 = 1 }$ .0; for (Int $\scriptstyle { \dot { \mathsf { J } } } = { \dot { \mathsf { I } } }$ ;j $< =$ jmax;j++) { if (j $\scriptstyle = = \mathbf { k }$ ) continue; term $\ast =$ (xx[k]-xx[j]); } term $\cdot ^ { = }$ temp/term; temp $\mid =$ -temp; sum $+ =$ term; w[k] $=$ sum;   
}

Use equation (3.4.9) to compute the barycentric rational interpolant. Note that $\mathbf { j } \mathbf { 1 }$ is not used since the approximation is global; it is included only for compatibility with Base_interp.

Doub num $_ { = 0 }$ ,den ${ = } 0$ ;   
for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) { Doub $\mathbf { \hat { h } } \mathbf { = x } \mathbf { \cdot }$ -xx[i]; if $( \mathbf { h _ { \alpha } } = = \mathbf { \beta } 0 . 0 )$ ) { return yy[i]; } else { Doub temp=w[i]/h; num $+ =$ temp\*yy[i]; den $+ =$ temp; }   
  
return num/den;

Doub BaryRat_interp::interp(Doub x) {

No need to invoke hunt or locate since the interpolation is global, so override interp to simply call rawinterp directly with a dummy value of $\mathrm { j } \mathrm { 1 }$ .

return rawinterp(1,x);

# CITED REFERENCES AND FURTHER READING:

Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 2 . 2 . [ 1 ]$   
Floater, M.S., and Hormann, K. ${ 2 0 0 6 + }$ , “Barycentric Rational Interpolation with No Poles and High Rates of Approximation,” at http://www.in.tu-clausthal.de/fileadmin/ homes/techreports/ifi0606hormann.pdf.[2]   
Berrut, J.-P., and Trefethen, L.N. 2004, “Barycentric Lagrange Interpolation,” SIAM Review, vol. 46, pp. 501–517.[3]   
Gear, C.W. 1971, Numerical Initial Value Problems in Ordinary Differential Equations (Englewood Cliffs, NJ: Prentice-Hall), $\ S 6 . 2$ .   
Cuyt, A., and Wuytack, L. 1987, Nonlinear Methods in Numerical Analysis (Amsterdam: North-Holland), Chapter 3.

# 3.5 Coefficients of the Interpolating Polynomial

Occasionally you may wish to know not the value of the interpolating polynomial that passes through a (small!) number of points, but the coefficients of that polynomial. A valid use of the coefficients might be, for example, to compute simultaneous interpolated values of the function and of several of its derivatives (see -5.1), or to convolve a segment of the tabulated function with some other function, where the moments of that other function (i.e., its convolution with powers of $x$ ) are known analytically.

Please be certain, however, that the coefficients are what you need. Generally the coefficients of the interpolating polynomial can be determined much less accurately than its value at a desired abscissa. Therefore, it is not a good idea to determine the coefficients only for use in calculating interpolating values. Values thus calculated will not pass exactly through the tabulated points, for example, while values computed by the routines in $\ S 3 . 1 - \ S 3 . 3$ will pass exactly through such points.

Also, you should not mistake the interpolating polynomial (and its coefficients) for its cousin, the best-fit polynomial through a data set. Fitting is a smoothing process, since the number of fitted coefficients is typically much less than the number of data points. Therefore, fitted coefficients can be accurately and stably determined even in the presence of statistical errors in the tabulated values. (See $\ S 1 4 . 9 .$ ) Interpolation, where the number of coefficients and number of tabulated points are equal, takes the tabulated values as perfect. If they in fact contain statistical errors, these can be magnified into oscillations of the interpolating polynomial in between the tabulated points.

As before, we take the tabulated points to be $y _ { i } \equiv y ( x _ { i } )$ . If the interpolating polynomial is written as

$$
y = c _ { 0 } + c _ { 1 } x + c _ { 2 } x ^ { 2 } + \cdots + c _ { N - 1 } x ^ { N - 1 }
$$

then the $c _ { i }$ ’s are required to satisfy the linear equation

$$
\left[ \begin{array} { c c c c c c } { 1 } & { x _ { 0 } } & { x _ { 0 } ^ { 2 } } & { \cdots } & { x _ { 0 } ^ { N - 1 } } \\ { 1 } & { x _ { 1 } } & { x _ { 1 } ^ { 2 } } & { \cdots } & { x _ { 1 } ^ { N - 1 } } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } \\ { 1 } & { x _ { N - 1 } } & { x _ { N - 1 } ^ { 2 } } & { \cdots } & { x _ { N - 1 } ^ { N - 1 } } \end{array} \right] \cdot \left[ \begin{array} { c } { c _ { 0 } } \\ { c _ { 1 } } \\ { \vdots } \\ { c _ { N - 1 } } \end{array} \right] = \left[ \begin{array} { c } { y _ { 0 } } \\ { y _ { 1 } } \\ { \vdots } \\ { y _ { N - 1 } } \end{array} \right]
$$

This is a Vandermonde matrix, as described in $\ S 2 . 8$ . One could in principle solve equation (3.5.2) by standard techniques for linear equations generally (-2.3); however, the special method that was derived in $\ S 2 . 8$ is more efficient by a large factor, of order $N$ , so it is much better.

Remember that Vandermonde systems can be quite ill-conditioned. In such a case, no numerical method is going to give a very accurate answer. Such cases do not, please note, imply any difficulty in finding interpolated values by the methods of $\ S 3 . 2$ , but only difficulty in finding coefficients.

Like the routine in $\ S 2 . 8$ , the following is due to G.B. Rybicki.

# void polcoe(VecDoub_I &x, VecDoub_I &y, VecDoub_O &cof)

Given arrays $\mathbf { x } \left[ 0 \ldots \ldots \right]$ and $\mathtt { y } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ containing a tabulated function $\mathsf { y } _ { i } = f ( \mathbf { x } _ { i } )$ , this routine returns an array of coefficients cof[0..n-1], such that $\begin{array} { r } { \mathsf { y } _ { i } = \sum _ { j = 0 } ^ { n - 1 } \mathsf { c o f } _ { j } \mathsf { x } _ { i } ^ { j } } \end{array}$ .

Int k,j,i, $\mathrm { n } { = } \mathrm { x }$ .size(); Doub phi,ff,b; VecDoub s(n); for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) s[i] $=$ cof[i]=0.0; s[n-1] $=$ -x[0]; for ( $\dot { \mathbf { 1 } } = 1$ ;i<n; $\dot { 1 } + +$ ) { Coefficients $\mathsf { s } _ { i }$ of the master polynomial $P ( x )$ are for (j=n-1-i;j<n-1;j++) found by recurrence. $\begin{array} { r } { \mathbf { s } \left[ \mathrm { j } \right] \ \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { - } = \ \mathbf { x } \left[ \mathrm { i } \right] \ast \mathbf { s } \left[ \mathrm { j } + 1 \right] \mathrm { i } \left. \mathbf { \Sigma } \right. } \end{array}$ ; s[n-1] -= x[i]; } for (j=0;j<n;j++) { phi=n; for (k=n-1;k>0;k--) The quantity $\begin{array} { r } { \mathtt { p h i } = \prod _ { j \ne k } ( x _ { j } - x _ { k } ) } \end{array}$ is found as a phi=k\*s[k]+x[j]\*phi; derivative of $P ( x _ { j } )$ . ff=y[j]/phi; b=1.0; Coefficients of polynomials in each term of the Lafor (k=n-1;k> ${ = } 0$ ;k--) { grange formula are found by synthetic division of cof[k] $+ =$ b\*ff; $P ( x )$ by $( x - x _ { j } )$ . The solution $\mathtt { c } _ { k }$ is accumu-$\mathtt { b } = \mathtt { s }$ [k]+x[j]\*b; lated. } } }

# 3.5.1 Another Method

Another technique is to make use of the function value interpolation routine already given (polint; -3.2). If we interpolate (or extrapolate) to find the value of the interpolating polynomial at $x = 0$ , then this value will evidently be $c _ { 0 }$ . Now we can subtract $c _ { 0 }$ from the $y _ { i }$ ’s and divide each by its corresponding $x _ { i }$ . Throwing out one point (the one with smallest $x _ { i }$ is a good candidate), we can repeat the procedure to find $c _ { 1 }$ , and so on.

It is not instantly obvious that this procedure is stable, but we have generally found it to be somewhat more stable than the routine immediately preceding. This method is of order $N ^ { 3 }$ , while the preceding one was of order $N ^ { 2 }$ . You will find, however, that neither works very well for large $N$ , because of the intrinsic ill-condition of the Vandermonde problem. In single precision, $N$ up to 8 or 10 is satisfactory; about double this in double precision.

# void polcof(VecDoub_I &xa, VecDoub_I &ya, VecDoub_O &cof)

Given arrays $\mathtt { x a } [ 0 \ldots \mathtt { n - 1 } ]$ and ya[0..n-1] containing a tabulated function $\mathtt { y a } _ { i } = f ( \mathtt { x a } _ { i } )$ , this routine returns an array of coefficients cof $\left[ 0 \ldots \mathbf { n } \mathbf { - } 1 \right]$ , such that $\begin{array} { r } { \mathtt { y a } _ { i } = \sum _ { j = 0 } ^ { n - 1 } \mathtt { c o f } _ { j } \mathtt { x a } _ { i } ^ { j } } \end{array}$ .

Int k,j,i,n=xa.size();   
Doub xmin;   
VecDoub x(n),y(n);   
for ( $\scriptstyle \dot { \ j } = 0$ ;j<n;j++) { x[j]=xa[j]; y[j]=ya[j];   
}   
for (j=0;j<n;j++) { VecDoub x_t(n-j),y_t(n-j); for $( \mathtt { k } = 0$ ;k<n-j;k++) { x_t[k] $= \tt x$ [k]; y_t[k]=y[k]; } Poly_interp interp(x,y,n-j); cof[j] $=$ interp.rawinterp(0,0.); xmin $^ { = 1 }$ .0e99; $\texttt { k } = \texttt { - 1 }$ ; for (i=0;i<n-j;i++) { if (abs(x[i]) $<$ xmin) { xmin $\cdot ^ { = }$ abs(x[i]); k=i; } if (x[i] != 0.0) y[i] $=$ (y[i]-cof[j])/x[i]; } for (i=k+1;i<n-j;i++) { y[i-1]=y[i]; $\mathbf { x } \left[ \mathbf { i } - 1 \right] = \mathbf { x }$ [i]; }   
}

Find the remaining $\mathbf { x } _ { i }$ of smallest absolute value

(meanwhile reducing all the terms)

and eliminate it.

If the point $x \ = \ 0$ is not in (or at least close to) the range of the tabulated $x _ { i }$ ’s, then the coefficients of the interpolating polynomial will in general become very large. However, the real “information content” of the coefficients is in small differences from the “translation-induced” large values. This is one cause of illconditioning, resulting in loss of significance and poorly determined coefficients. In this case, you should consider redefining the origin of the problem, to put $x = 0$ in a sensible place.

Another pathology is that, if too high a degree of interpolation is attempted on a smooth function, the interpolating polynomial will attempt to use its high-degree coefficients, in combinations with large and almost precisely canceling combinations, to match the tabulated values down to the last possible epsilon of accuracy. This effect is the same as the intrinsic tendency of the interpolating polynomial values to oscillate (wildly) between its constrained points and would be present even if the machine’s floating precision were infinitely good. The above routines polcoe and polcof have slightly different sensitivities to the pathologies that can occur.

Are you still quite certain that using the coefficients is a good idea?

# CITED REFERENCES AND FURTHER READING:

Isaacson, E., and Keller, H.B. 1966, Analysis of Numerical Methods; reprinted 1994 (New York: Dover), $\ S 5 . 2$ .

# 3.6 Interpolation on a Grid in Multidimensions

In multidimensional interpolation, we seek an estimate of a function of more than one independent variable, $y ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ . The Great Divide is, Are we given a complete set of tabulated values on an $n$ -dimensional grid? Or, do we know function values only on some scattered set of points in the $n$ -dimensional space? In one dimension, the question never arose, because any set of $x _ { i }$ ’s, once sorted into ascending order, could be viewed as a valid one-dimensional grid (regular spacing not being a requirement).

As the number of dimensions $n$ gets large, maintaining a full grid becomes rapidly impractical, because of the explosion in the number of gridpoints. Methods that work with scattered data, to be considered in $\ S 3 . 7$ , then become the methods of choice. Don’t, however, make the mistake of thinking that such methods are intrinsically more accurate than grid methods. In general they are less accurate. Like the proverbial three-legged dog, they are remarkable because they work at all, not because they work, necessarily, well!

Both kinds of methods are practical in two dimensions, and some other kinds as well. For example, finite element methods, of which triangulation is the most common, find ways to impose some kind of geometrically regular structure on scattered points, and then use that structure for interpolation. We will treat two-dimensional interpolation by triangulation in detail in $\ S 2 1 . 6$ ; that section should be considered as a continuation of the discussion here.

In the remainder of this section, we consider only the case of interpolating on a grid, and we implement in code only the (most common) case of two dimensions. All of the methods given generalize to three dimensions in an obvious way. When we implement methods for scattered data, in $\ S 3 . 7$ , the treatment will be for general $n$ .

In two dimensions, we imagine that we are given a matrix of functional values $y _ { i j }$ , with $i = 0 , \ldots , M - 1$ and $j = 0 , \ldots , N - 1$ . We are also given an array of $x _ { 1 }$ values $x _ { 1 i }$ , and an array of $x _ { 2 }$ values $x _ { 2 j }$ , with $i$ and $j$ as just stated. The relation of these input quantities to an underlying function $y ( x _ { 1 } , x _ { 2 } )$ is just

$$
y _ { i j } = y ( x _ { 1 i } , x _ { 2 j } )
$$

We want to estimate, by interpolation, the function $y$ at some untabulated point $( x _ { 1 } , x _ { 2 } )$ .

An important concept is that of the grid square in which the point $( x _ { 1 } , x _ { 2 } )$ falls, that is, the four tabulated points that surround the desired interior point. For convenience, we will number these points from 0 to 3, counterclockwise starting from the lower left. More precisely, if

$$
\begin{array} { l } { { x _ { 1 i } \leq x _ { 1 } \leq x _ { 1 ( i + 1 ) } } } \\ { { x _ { 2 j } \leq x _ { 2 } \leq x _ { 2 ( j + 1 ) } } } \end{array}
$$

defines values of $i$ and $j$ , then

$$
\begin{array} { l } { y _ { 0 } \equiv y _ { i j } } \\ { y _ { 1 } \equiv y _ { ( i + 1 ) j } } \\ { y _ { 2 } \equiv y _ { ( i + 1 ) ( j + 1 ) } } \\ { y _ { 3 } \equiv y _ { i ( j + 1 ) } } \end{array}
$$

The simplest interpolation in two dimensions is bilinear interpolation on the grid square. Its formulas are

$$
\begin{array} { c } { t \equiv ( x _ { 1 } - x _ { 1 i } ) / ( x _ { 1 ( i + 1 ) } - x _ { 1 i } ) } \\ { u \equiv ( x _ { 2 } - x _ { 2 j } ) / ( x _ { 2 ( j + 1 ) } - x _ { 2 j } ) } \end{array}
$$

(so that $t$ and $u$ each lie between 0 and 1) and

$$
y ( x _ { 1 } , x _ { 2 } ) = ( 1 - t ) ( 1 - u ) y _ { 0 } + t ( 1 - u ) y _ { 1 } + t u y _ { 2 } + ( 1 - t ) u y _ { 3 }
$$

Bilinear interpolation is frequently “close enough for government work.” As the interpolating point wanders from grid square to grid square, the interpolated function value changes continuously. However, the gradient of the interpolated function changes discontinuously at the boundaries of each grid square.

We can easily implement an object for bilinear interpolation by grabbing pieces of “machinery” from our one-dimensional interpolation classes:

# struct Bilin_interp {

Object for bilinear interpolation on a matrix. Construct with a vector of $x _ { 1 }$ values, a vector of $x _ { 2 }$ values, and a matrix of tabulated function values $y _ { i j }$ . Then call interp for interpolated values.

Int m,n;  
const MatDoub &y;  
Linear_interp x1terp, x2terp;

Bilin_interp(VecDoub_I &x1v, VecDoub_I &x2v, MatDoub_I &ym) : m(x1v.size()), n(x2v.size()), y(ym), x1terp(x1v,x1v), x2terp(x2v,x2v) {} Construct dummy 1-dim interpolations for their locate and hunt Doub interp(Doub x1p, Doub x2p) { functions. Int i,j; Doub yy, t, u; $\begin{array} { r l } { \dot { \mathbf { 1 } } } & { { } = } \end{array}$ x1terp.cor ? x1terp.hunt(x1p) : x1terp.locate(x1p); ${ \dot { \textbf { j } } } =$ x2terp.cor ? x2terp.hunt(x2p) : x2terp.locate(x2p); Find the grid square. $\begin{array} { r l } { \mathbf { \epsilon } _ { \mathbf { { t } } } } & { { } = } \end{array}$ (x1p-x1terp.xx[i])/(x1terp.xx[i+1]-x1terp.xx[i]); Interpolate. $\mathrm { ~ \textbar ~ { ~ u ~ } ~ } =$ (x2p-x2terp.xx[j])/(x2terp.xx[j+1]-x2terp.xx[j]); yy = (1.-t)\*(1.-u)\*y[i][j] $^ +$ t\*(1.-u)\*y[i+1][j] + (1.-t)\*u\*y[i][j+1] $^ +$ t\*u\*y[i+1][j+1]; return yy; } };

Here we declare two instances of Linear_interp, one for each direction, and use them merely to do the bookkeeping on the arrays $x _ { 1 i }$ and $x _ { 2 _ { j } }$ — in particular, to provide the “intelligent” table-searching mechanisms that we have come to rely on. (The second occurrence of $\tt { x 1 v }$ and $\tt { x 2 v }$ in the constructors is just a placeholder; there are not really any one-dimensional “y” arrays.)

Usage of Bilin_interp is just what you’d expect:

Int $\mathrm { m } = .$ .. $\mathbf { n } =$ ..   
MatDoub yy(m,n);   
VecDoub x1(m), x2(n);   
Bilin_interp myfunc(x1,x2,yy);

followed (any number of times) by

Doub x1,x2,y;   
$\mathrm { ~ y ~ } =$ myfunc.interp(x1,x2);

Bilinear interpolation is a good place to start, in two dimensions, unless you positively know that you need something fancier.

There are two distinctly different directions that one can take in going beyond bilinear interpolation to higher-order methods: One can use higher order to obtain increased accuracy for the interpolated function (for sufficiently smooth functions!), without necessarily trying to fix up the continuity of the gradient and higher derivatives. Or, one can make use of higher order to enforce smoothness of some of these derivatives as the interpolating point crosses grid-square boundaries. We will now consider each of these two directions in turn.

# 3.6.1 Higher Order for Accuracy

The basic idea is to break up the problem into a succession of one-dimensional interpolations. If we want to do $\mathtt { m } - 1$ order interpolation in the $x _ { 1 }$ direction, and $\mathtt { n - 1 }$ order in the $x _ { 2 }$ direction, we first locate an $m \times n$ sub-block of the tabulated function matrix that contains our desired point $( x _ { 1 } , x _ { 2 } )$ . We then do m one-dimensional interpolations in the $x _ { 2 }$ direction, i.e., on the rows of the sub-block, to get function values at the points $( x _ { 1 i } , x _ { 2 } )$ , with $m$ values of $i$ . Finally, we do a last interpolation in the $x _ { 1 }$ direction to get the answer.

Again using the previous one-dimensional machinery, this can all be coded very concisely as

# struct Poly2D_interp {

Object for two-dimensional polynomial interpolation on a matrix. Construct with a vector of $x _ { 1 }$ values, a vector of $x _ { 2 }$ values, a matrix of tabulated function values $y _ { i j }$ , and integers to specify the number of points to use locally in each direction. Then call interp for interpolated values.

Int m,n,mm,nn; const MatDoub &y; VecDoub yv; Poly_interp x1terp, x2terp; Poly2D_interp(VecDoub_I &x1v, VecDoub_I &x2v, MatDoub_I &ym, Int mp, Int np) : m(x1v.size()), n(x2v.size()), mm(mp), nn(np), y(ym), yv(m), x1terp(x1v,yv,mm), x2terp(x2v,x2v,nn) {} Dummy 1-dim interpolations for their locate and hunt functions. Doub interp(Doub x1p, Doub x2p) { Int i,j,k; $\begin{array} { r l } { \dot { \bf \lambda } _ { 1 } } & { { } = } \end{array}$ x1terp.cor ? x1terp.hunt(x1p) : x1terp.locate(x1p); ${ \dot { \mathrm { ~  ~ j ~ } } } =$ x2terp.cor ? x2terp.hunt(x2p) : x2terp.locate(x2p); Find grid block. for $( \Bbbk { = } \dot$ ;k<i+mm;k++) { mm interpolations in the $x _ { 2 }$ direction. x2terp.yy $=$ &y[k][0]; yv[k] $=$ x2terp.rawinterp(j,x2p); } return x1terp.rawinterp(i,x1p); A final interpolation in the $x _ { 1 }$ direc-} tion. };

The user interface is the same as for Bilin_interp, except that the constructor has two additional arguments that specify the number of points (order plus one) to be used locally in, respectively, the $x _ { 1 }$ and $x _ { 2 }$ interpolations. Typical values will be in the range 3 to 7.

Code stylists won’t like some of the details in Poly2D_interp (see discussion in $\ S 3 . 1$ immediately following Base_interp). As we loop over the rows of the sub-block, we reach into the guts of x2terp and repoint its yy array to a row of our $y$ matrix. Further, we alter the contents of the array yv, for which x1terp has stored a pointer, on the fly. None of this is particularly dangerous as long as we control the implementations in both Base_interp and Poly2D_interp; and it makes for a very efficient implementation. You should view these two classes as not just (implicitly) friend classes, but as really intimate friends.

# 3.6.2 Higher Order for Smoothness: Bicubic Spline

A favorite technique for obtaining smoothness in two-dimensional interpolation is the bicubic spline. To set up a bicubic spline, you (one time) construct $M$ one-dimensional splines across the rows of the two-dimensional matrix of function values. Then, for each desired interpolated value you proceed as follows: (1) Perform $M$ spline interpolations to get a vector of values $y ( x _ { 1 i } , x _ { 2 } )$ , $i = 0 , \ldots , M - 1$ . (2) Construct a one-dimensional spline through those values. (3) Finally, splineinterpolate to the desired value $y ( x _ { 1 } , x _ { 2 } )$ .

If this sounds like a lot of work, well, yes, it is. The one-time setup work scales as the table size $M \times N$ , while the work per interpolated value scales roughly as $M \log M + N$ , both with pretty hefty constants in front. This is the price that you pay for the desirable characteristics of splines that derive from their nonlocality. For tables with modest $M$ and $N$ , less than a few hundred, say, the cost is usually tolerable. If it’s not, then fall back to the previous local methods.

Again a very concise implementation is possible:

# struct Spline2D_interp {

Object for two-dimensional cubic spline interpolation on a matrix. Construct with a vector of $x _ { 1 }$ values, a vector of $x _ { 2 }$ values, and a matrix of tabulated function values $y _ { i j }$ . Then call interp for interpolated values.

Int m,n; const MatDoub &y; const VecDoub &x1; VecDoub yv; NRvector<Spline_interp\*> srp; Spline2D_interp(VecDoub_I &x1v, VecDoub_I &x2v, MatDoub_I &ym) : m(x1v.size()), n(x2v.size()), y(ym), yv(m), x1(x1v), srp(m) { for (Int $\scriptstyle \dot { 1 } = 0$ ;i<m;i++) srp[i] $=$ new Spline_interp(x2v,&y[i][0]); Save an array of pointers to 1-dim row splines. } \~Spline2D_interp(){ for (Int $\scriptstyle \dot { 1 } = 0$ ;i<m;i++) delete srp[i]; We need a destructor to clean up. } Doub interp(Doub x1p, Doub x2p) { for (Int $\scriptstyle \dot { 1 } = 0$ ;i<m; $\lfloor + +$ ) yv[i] $=$ (\*srp[i]).interp(x2p); Interpolate on each row. Spline_interp scol(x1,yv); Construct the column spline, return scol.interp(x1p); and evaluate it. } };

The reason for that ugly vector of pointers to Spline_interp objects is that we need to initialize each row spline separately, with data from the appropriate row. The user interface is the same as Bilin_interp, above.

![](images/21ffb3f36620e71067758979f88a8786f6dce3aec5d443f16813bd421c0241c3.jpg)  
Figure 3.6.1. (a) Labeling of points used in the two-dimensional interpolation routines bcuint and bcucof. (b) For each of the four points in (a), the user supplies one function value, two first derivatives, and one cross-derivative, a total of 16 numbers.

# 3.6.3 Higher Order for Smoothness: Bicubic Interpolation

Bicubic interpolation gives the same degree of smoothness as bicubic spline interpolation, but it has the advantage of being a local method. Thus, after you set it up, a function interpolation costs only a constant, plus $\log M + \log N$ , to find your place in the table. Unfortunately, this advantage comes with a lot of complexity in coding. Here, we will give only some building blocks for the method, not a complete user interface.

Bicubic splines are in fact a special case of bicubic interpolation. In the general case, however, we leave the values of all derivatives at the grid points as freely specifiable. You, the user, can specify them any way you want. In other words, you specify at each grid point not just the function $y ( x _ { 1 } , x _ { 2 } )$ , but also the gradients $\partial y / \partial x _ { 1 } \ \equiv \ y _ { , 1 }$ , $\partial y / \partial x _ { 2 } \equiv y _ { , 2 }$ and the cross derivative $\partial ^ { 2 } y / \partial x _ { 1 } \partial x _ { 2 } \ \equiv \ y , _ { 1 2 }$ (see Figure 3.6.1). Then an interpolating function that is cubic in the scaled coordinates $t$ and $u$ (equation 3.6.4) can be found, with the following properties: (i) The values of the function and the specified derivatives are reproduced exactly on the grid points, and (ii) the values of the function and the specified derivatives change continuously as the interpolating point crosses from one grid square to another.

It is important to understand that nothing in the equations of bicubic interpolation requires you to specify the extra derivatives correctly! The smoothness properties are tautologically “forced,” and have nothing to do with the “accuracy” of the specified derivatives. It is a separate problem for you to decide how to obtain the values that are specified. The better you do, the more accurate the interpolation will be. But it will be smooth no matter what you do.

Best of all is to know the derivatives analytically, or to be able to compute them accurately by numerical means, at the grid points. Next best is to determine them by numerical differencing from the functional values already tabulated on the grid. The relevant code would be something like this (using centered differencing):

y1a[j][k] $=$ (ya[j $+ 1 ]$ [k]-ya[j-1][k])/(x1a[j+1]-x1a[j-1]); y2a[j][k] $=$ (ya[j][k+1]-ya[j][k-1])/(x2a[k+1]-x2a[k-1]); y12a[j][k] $=$ (ya[j $+ 1 ]$ [k+1]-ya[j+1][k-1]-ya[j-1][k+1]+ya[j-1][k-1]) /((x1a[j+1]-x1a[j-1])\*(x2a[k+1]-x2a[k-1]));

To do a bicubic interpolation within a grid square, given the function y and the derivatives y1, y2, y12 at each of the four corners of the square, there are two steps: First obtain the 16 quantities $c _ { i j }$ ; $i , j = 0 , \ldots , 3$ using the routine bcucof below. (The formulas that obtain the $c$ ’s from the function and derivative values are just a complicated linear transformation, with coefficients that, having been determined once in the mists of numerical history, can be tabulated and forgotten.) Next, substitute the $c$ ’s into any or all of the following bicubic formulas for function and derivatives, as desired:

$$
\begin{array} { l } { \displaystyle y ( x _ { 1 } , x _ { 2 } ) = \sum _ { i = 0 } ^ { 3 } \sum _ { j = 0 } ^ { 3 } c _ { i j } t ^ { i } u ^ { j } } \\ { \displaystyle y _ { , 1 } ( x _ { 1 } , x _ { 2 } ) = \sum _ { i = 0 } ^ { 3 } \sum _ { j = 0 } ^ { 3 } i c _ { i j } t ^ { i - 1 } u ^ { j } \left( d t / d x _ { 1 } \right) } \\ { \displaystyle y _ { , 2 } ( x _ { 1 } , x _ { 2 } ) = \sum _ { i = 0 } ^ { 3 } \sum _ { j = 0 } ^ { 3 } j c _ { i j } t ^ { i } u ^ { j - 1 } \left( d u / d x _ { 2 } \right) } \\ { \displaystyle y _ { , 1 2 } ( x _ { 1 } , x _ { 2 } ) = \sum _ { i = 0 } ^ { 3 } \sum _ { j = 0 } ^ { 3 } i j c _ { i j } t ^ { i - 1 } u ^ { j - 1 } \left( d u / d x _ { 1 } \right) \left( d u / d x _ { 2 } \right) } \end{array}
$$

where $t$ and $u$ are again given by equation (3.6.4).

void bcucof(VecDoub_I &y, VecDoub_I &y1, VecDoub_I &y2, VecDoub_I &y12,const Doub d1, const Doub d2, MatDoub_O &c) {

Given arrays y[0..3], y1[0..3], y2[0..3], and y12[0..3], containing the function, gradients, and cross-derivative at the four grid points of a rectangular grid cell (numbered counterclockwise from the lower left), and given d1 and d2, the length of the grid cell in the 1 and 2 directions, this routine returns the table c[0..3][0..3] that is used by routine bcuint for bicubic interpolation.

static Int wt_d[16\*16] $=$ {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, 3, 0, 0, 0, 0,-2, 0, 0,-1, 0, 0, 0, 0, 2, 0, 0,-2, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,-3, 0, 0, 3, 0, 0, 0, 0,-2, 0, 0,-1, 0, 0, 0, 0, 2, 0, 0,-2, 0, 0, 0, 0, 1, 0, 0, 1, -3, 3, 0, 0,-2,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-3, 3, 0, 0,-2,-1, 0, 0, 9,-9, 9,-9, 6, 3,-3,-6, 6,-6,-3, 3, 4, 2, 1, 2, -6, 6,-6, 6,-4,-2, 2, 4,-3, 3, 3,-3,-2,-1,-1,-2, 2,-2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,-2, 0, 0, 1, 1, 0, 0, -6, 6,-6, 6,-3,-3, 3, 3,-4, 4, 2,-2,-2,-2,-1,-1, 4,-4, 4,-4, 2, 2,-2,-2, 2,-2,-2, 2, 1, 1, 1, 1};   
Int l,k,j,i;   
Doub xx,d1d2=d1\*d2;   
VecDoub cl(16),x(16);   
static MatInt wt(16,16,wt_d);   
for (i=0;i<4;i++) { Pack a temporary vector x. x[i]=y[i]; x[i+4]=y1[i]\*d1; x[i+8]=y2[i]\*d2; x[i+12]=y12[i]\*d1d2;   
  
for (i=0;i<16;i++) { Matrix-multiply by the stored table. $\mathtt { x x } { = } 0 . 0$ ; for (k=0;k<16;k++) xx += wt[i][k]\*x[k]; cl[i] $= \tt x x$ ;   
}   
$\mathtt { 1 } = 0$ ;   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<4;i++) Unpack the result into the output table for (j ${ = } 0$ ;j<4;j++) c[i][j]=cl[l++];

The implementation of equation (3.6.6), which performs a bicubic interpolation, gives back the interpolated function value and the two gradient values, and uses the above routine bcucof, is simply:

void bcuint(VecDoub_I &y, VecDoub_I &y1, VecDoub_I &y2, VecDoub_I &y12, const Doub x1l, const Doub x1u, const Doub x2l, const Doub x2u, const Doub x1, const Doub x2, Doub &ansy, Doub &ansy1, Doub &ansy2) {   
Bicubic interpolation within a grid square. Input quantities are y,y1,y2,y12 (as described in   
bcucof); $\tt x 1 1$ and x1u, the lower and upper coordinates of the grid square in the 1 direction;   
$\tt x 2 1$ and x2u likewise for the 2 direction; and $\mathbf { x } \mathbf { 1 } , \mathbf { x } 2$ , the coordinates of the desired point for   
the interpolation. The interpolated function value is returned as ansy, and the interpolated   
gradient values as ansy1 and ansy2. This routine calls bcucof.   
Int i;   
Doub t,u,d1=x1u-x1l,d2=x2u-x2l;   
MatDoub c(4,4);   
bcucof(y,y1,y2,y12,d1,d2,c); Get the c’s.   
if $( \mathrm { x 1 u ~ } = = \mathrm { ~ \ x 1 1 ~ }$ || x $\ Q \ \mathbf { u } \ = \ \mathbf { x } 2 1 .$ ) throw("Bad input in routine bcuint");   
$\mathtt { t = }$ (x1-x1l)/d1; Equation (3.6.4).   
$\mathrm { u } =$ (x2-x2l)/d2;   
ansy=ansy2=ansy $\scriptstyle 1 = 0$ .0;   
for ( $\dot { 1 } = 3$ ; $\therefore 2 = 0$ ;i--) { Equation (3.6.6). ansy=t\*ansy+((c[i][3]\*u+c[i][2])\*u+c[i][1])\*u+c[i][0]; ansy2 $\Bumpeq$ t\*ansy2+(3.0\*c[i][3] $\ast \mathtt { u } + 2$ .0\*c[i][2])\*u+c[i][1]; ansy1=u\*ansy1+(3.0\*c[3][i]\*t+2.0\*c[2][i])\*t+c[1][i];   
ansy1 $/ =$ d1;   
ansy2 $/ =$ d2;

You can combine the best features of bicubic interpolation and bicubic splines by using splines to compute values for the necessary derivatives at the grid points, storing these values, and then using bicubic interpolation, with an efficient tablesearching method, for the actual function interpolations. Unfortunately this is beyond our scope here.

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, $\ S 2 5 . 2$ .

Kinahan, B.F., and Harm, R. 1975, “Chemical Composition and the Hertzsprung Gap,” Astrophysical Journal, vol. 200,pp. 330-335.

Johnson, L.W., and Riess, R.D. 1982, Numerical Analysis, 2nd ed. (Reading, MA: Addison-Wesley), $\ S 5 . 2 . 7$ .   
Dahlquist, G., and Bjorck, A. 1974, Numerical Methods (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2003 (New York: Dover), $\ S 7 . 7$ .

# 3.7 Interpolation on Scattered Data in Multidimensions

We now leave behind, if with some trepidation, the orderly world of regular grids. Courage is required. We are given an arbitrarily scattered set of $N$ data points $( { \bf x } _ { i } , y _ { i } ) , i = 0 , \dots , N - 1$ in $n$ -dimensional space. Here $\mathbf { X } _ { i }$ denotes an $n$ -dimensional vector of independent variables, $( x _ { 1 i } , x _ { 2 i } , \dots , x _ { n i } )$ , and $y _ { i }$ is the value of the function at that point.

In this section we discuss two of the most widely used general methods for this problem, radial basis function $( R B F )$ interpolation, and kriging. Both of these methods are expensive. By that we mean that they require $O ( N ^ { 3 } )$ operations to initially digest a set of data points, followed by $O ( N )$ operations for each interpolated value. Kriging is also able to supply an error estimate — but at the rather high cost of $O ( N ^ { 2 } )$ per value. Shepard interpolation, discussed below, is a variant of RBF that at least avoids the $O ( N ^ { 3 } )$ initial work; otherwise these workloads effectively limit the usefulness of these general methods to values of $N \lesssim 1 0 ^ { 4 }$ . It is therefore worthwhile for you to consider whether you have any other options. Two of these are

- If $n$ is not too large (meaning, usually, $n = 2$ ), and if the data points are fairly dense, then consider triangulation, discussed in $\ S 2 1 . 6$ . Triangulation is an example of a finite element method. Such methods construct some semblance of geometric regularity and then exploit that construction to advantage. Mesh generation is a closely related subject.   
- If your accuracy goals will tolerate it, consider moving each data point to the nearest point on a regular Cartesian grid and then using Laplace interpolation (-3.8) to fill in the rest of the grid points. After that, you can interpolate on the grid by the methods of $\ S 3 . 6$ . You will need to compromise between making the grid very fine (to minimize the error introduced when you move the points) and the compute time workload of the Laplace method.

If neither of these options seem attractive, and you can’t think of another one that is, then try one or both of the two methods that we now discuss. RBF interpolation is probably the more widely used of the two, but kriging is our personal favorite. Which works better will depend on the details of your problem.

The related, but easier, problem of curve interpolation in multidimensions is discussed at the end of this section.

# 3.7.1 Radial Basis Function Interpolation

The idea behind RBF interpolation is very simple: Imagine that every known point $j$ “influences” its surroundings the same way in all directions, according to some assumed functional form $\phi ( r )$ — the radial basis function — that is a function only of radial distance $r = | { \bf x } - { \bf x } _ { j } |$ from the point. Let us try to approximate the interpolating function everywhere by a linear combination of the $\phi$ ’s, centered on all the known points,

$$
y ( \mathbf { x } ) = \sum _ { i = 0 } ^ { N - 1 } w _ { i } \phi ( | \mathbf { x } - \mathbf { x } _ { i } | )
$$

where the $w _ { i }$ ’s are some unknown set of weights. How do we find these weights? Well, we haven’t used the function values $y _ { i }$ yet. The weights are determined by requiring that the interpolation be exact at all the known data points. That is equivalent to solving a set of $N$ linear equations in $N$ unknowns for the $w _ { i }$ ’s:

$$
y _ { j } = \sum _ { i = 0 } ^ { N - 1 } w _ { i } \phi ( | \mathbf { x } _ { j } - \mathbf { x } _ { i } | )
$$

For many functional forms $\phi$ , it can be proved, under various general assumptions, that this set of equations is nondegenerate and can be readily solved by, e.g., $L U$ decomposition $( \ S 2 . 3 )$ . References [1,2] provide entry to the literature.

A variant on RBF interpolation is normalized radial basis function (NRBF) interpolation, in which we require the sum of the basis functions to be unity or, equivalently, replace equations (3.7.1) and (3.7.2) by

$$
y ( \mathbf { x } ) = \frac { \sum _ { i = 0 } ^ { N - 1 } w _ { i } \phi ( | \mathbf { x } - \mathbf { x } _ { i } | ) } { \sum _ { i = 0 } ^ { N - 1 } \phi ( | \mathbf { x } - \mathbf { x } _ { i } | ) }
$$

and

$$
y _ { j } \sum _ { i = 0 } ^ { N - 1 } \phi ( | \mathbf { x } _ { j } - \mathbf { x } _ { i } | ) = \sum _ { i = 0 } ^ { N - 1 } w _ { i } \phi ( | \mathbf { x } _ { j } - \mathbf { x } _ { i } | )
$$

Equations (3.7.3) and (3.7.4) arise more naturally from a Bayesian statistical perspective [3]. However, there is no evidence that either the NRBF method is consistently superior to the RBF method, or vice versa. It is easy to implement both methods in the same code, leaving the choice to the user.

As we already mentioned, for $N$ data points the one-time work to solve for the weights by $L U$ decomposition is $O ( N ^ { 3 } )$ . After that, the cost is $O ( N )$ for each interpolation. Thus $N \sim 1 0 ^ { 3 }$ is a rough dividing line (at 2007 desktop speeds) between “easy” and “difficult.” If your $N$ is larger, however, don’t despair: There are fast multipole methods, beyond our scope here, with much more favorable scaling [1,4,5]. Another, much lower-tech, option is to use Shepard interpolation discussed later in this section.

Here are a couple of objects that implement everything discussed thus far. RBF_fn is a virtual base class whose derived classes will embody different functional forms for $\mathtt { r b f } ( r ) \equiv \phi ( r )$ . RBF_interp, via its constructor, digests your data and solves the equations for the weights. The data points $\mathbf { X } _ { i }$ are input as an $N \times n$ matrix, and the code works for any dimension $n$ . A boolean argument nrbf inputs whether NRBF is to be used instead of RBF. You call interp to get an interpolated function value at a new point $\mathbf { X }$ .

# struct RBF_fn {

Abstract base class template for any particular radial basis function. See specific examples below.

virtual Doub rbf(Doub $\mathbf { \boldsymbol { r } } ) \ = \ \mathbf { \boldsymbol { 0 } } ;$ };

struct RBF_interp {   
Object for radial basis function interpolation using n points in dim dimensions. Call constructor once, then interp as many times as desired. Int dim, n;   
const MatDoub &pts;   
const VecDoub &vals;   
VecDoub w;   
RBF_fn &fn;   
Bool norm;

RBF_interp(MatDoub_I &ptss, VecDoub_I &valss, RBF_fn &func, Bool nrbf $=$ false) : dim(ptss.ncols()), n(ptss.nrows()) , pts(ptss), vals(valss), $\ l { w } ( { \mathrm { n } } )$ , fn(func), norm(nrbf) {

Constructor. The $\textbf { n } \times$ dim matrix ptss inputs the data points, the vector valss the function values. func contains the chosen radial basis function, derived from the class RBF_fn. The default value of nrbf gives RBF interpolation; set it to 1 for NRBF.

Int i,j;   
Doub sum;   
MatDoub rbf ${ ( \mathtt { n } , \mathtt { n } ) }$ ;   
VecDoub rhs(n);   
for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<n; $\mathbf { i } + +$ ) { Fill the matrix $\phi ( | { \bf r } _ { i } - { \bf r } _ { j } | )$ and the r.h.s. vector. sum $\qquad = \ 0 .$ .; for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<n;j++) { sum $+ =$ (rbf[i][j] $=$ fn.rbf(rad(&pts[i][0],&pts[j][0]))); } if (norm) rhs[i] $=$ sum\*vals[i]; else rhs[i] $=$ vals[i];   
}   
LUdcmp lu(rbf); Solve the set of linear equations.   
lu.solve(rhs,w);

# }

# Doub interp(VecDoub_I &pt) {

Return the interpolated function value at a dim-dimensional point pt.

Doub fval, sum $_ { = 0 }$ ., sumw ${ \tt = } 0$ .; if (pt.size() $! =$ dim) throw("RBF_interp bad pt size"); for (Int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<n; $\mathbf { i } + +$ ) { Sum over all tabulated points. fval $=$ fn.rbf(rad(&pt[0],&pts[i][0])); sumw $+ =$ w[i]\*fval; sum $+ =$ fval; } return norm ? sumw/sum : sumw; }

#

Doub rad(const Doub \*p1, const Doub \*p2) { Euclidean distance. Doub sum $\qquad = \ 0$ .; for (Int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<dim; $\dot { 1 } + + \dot { 1 }$ ) sum $+ =$ SQR(p1[i]-p2[i]); return sqrt(sum); } };

# 3.7.2 Radial Basis Functions in General Use

The most often used radial basis function is the multiquadric first used by Hardy, circa 1970. The functional form is

$$
\phi ( r ) = ( r ^ { 2 } + r _ { 0 } ^ { 2 } ) ^ { 1 / 2 }
$$

where $r _ { 0 }$ is a scale factor that you get to choose. Multiquadrics are said to be less sensitive to the choice of $r _ { 0 }$ than some other functional forms.

In general, both for multiquadrics and for other functions, below, $r _ { 0 }$ should be larger than the typical separation of points but smaller than the “outer scale” or feature size of the function that you are interpolating. There can be several orders of magnitude difference between the interpolation accuracy with a good choice for $r _ { 0 }$ , versus a poor choice, so it is definitely worth some experimentation. One way to experiment is to construct an RBF interpolator omitting one data point at a time and measuring the interpolation error at the omitted point.

The inverse multiquadric

$$
\phi ( r ) = ( r ^ { 2 } + r _ { 0 } ^ { 2 } ) ^ { - 1 / 2 }
$$

gives results that are comparable to the multiquadric, sometimes better.

It might seem odd that a function and its inverse (actually, reciprocal) work about equally well. The explanation is that what really matters is smoothness, and certain properties of the function’s Fourier transform that are not very different between the multiquadric and its reciprocal. The fact that one increases monotonically and the other decreases turns out to be almost irrelevant. However, if you want the extrapolated function to go to zero far from all the data (where an accurate value is impossible anyway), then the inverse multiquadric is a good choice.

The thin-plate spline radial basis function is

$$
\phi ( r ) = r ^ { 2 } \log ( r / r _ { 0 } )
$$

with the limiting value $\phi ( 0 ) = 0$ assumed. This function has some physical justification in the energy minimization problem associated with warping a thin elastic plate. There is no indication that it is generally better than either of the above forms, however.

The Gaussian radial basis function is just what you’d expect,

$$
\begin{array} { r } { \phi ( r ) = \exp \left( - \frac { 1 } { 2 } r ^ { 2 } / r _ { 0 } ^ { 2 } \right) } \end{array}
$$

The interpolation accuracy using Gaussian basis functions can be very sensitive to $r _ { 0 }$ , and they are often avoided for this reason. However, for smooth functions and with an optimal $r _ { 0 }$ , very high accuracy can be achieved. The Gaussian also will extrapolate any function to zero far from the data, and it gets to zero quickly.

Other functions are also in use, for example those of Wendland [6]. There is a large literature in which the above choices for basis functions are tested against specific functional forms or experimental data sets [1,2,7]. Few, if any, general recommendations emerge. We suggest that you try the alternatives in the order listed above, starting with multiquadrics, and that you not omit experimenting with different choices of the scale parameters $r _ { 0 }$ .

The functions discussed are implemented in code as:

struct RBF_multiquadric : RBF_fn {   
Instantiate this and send to RBF_interp to get multiquadric interpolation. Doub r02; RBF_multiquadric(Doub scale $^ { = 1 }$ .) : r02(SQR(scale)) {} Constructor argument is the scale factor. See text. Doub rbf(Doub r) { return sqrt(SQR(r) $+ \tt r 0 2$ ); }   
};

struct RBF_thinplate : RBF_fn { Same as above, but for thin-plate spline.

Doub r0; RBF_thinplate(Doub scal $\mathtt { e } = 1$ .) : r0(scale) {} Doub rbf(Doub r) { return $x \ < = \ 0$ . ? 0. : SQR(r)\*log(r/r0); } ;

struct RBF_gauss : RBF_fn {   
Same as above, but for Gaussian. Doub r0; RBF_gauss(Doub scale $\ B = 1$ .) : r0(scale) {} Doub rbf(Doub r) { return exp(-0.5\*SQR(r/r0)); }   
};   
struct RBF_inversemultiquadric : RBF_fn {   
Same as above, but for inverse multiquadric. Doub r02; RBF_inversemultiquadric(Doub scale $^ { \prime = 1 }$ .) : r02(SQR(scale)) {} Doub rbf(Doub r) { return 1./sqrt(SQR(r)+r02); }   
};

Typical use of the objects in this section should look something like this:

Int npts $=$ ...,ndim=...;   
Doub r0=...;   
MatDoub pts(npts,ndim);   
VecDoub y(npts);   
RBF_multiquadric multiquadric(r0);   
RBF_interp myfunc(pts,y,multiquadric,0);

followed by any number of interpolation calls,

VecDoub pt(ndim);   
Doub val;   
val $=$ myfunc.interp(pt);

# 3.7.3 Shepard Interpolation

An interesting special case of normalized radial basis function interpolation (equations 3.7.3 and 3.7.4) occurs if the function $\phi ( r )$ goes to infinity as $r  0$ , and is finite (e.g., decreasing) for $r > 0$ . In that case it is easy to see that the weights $w _ { i }$ are just equal to the respective function values $y _ { i }$ , and the interpolation formula is simply

$$
y ( \mathbf { x } ) = \frac { \sum _ { i = 0 } ^ { N - 1 } y _ { i } \phi ( | \mathbf { x } - \mathbf { x } _ { i } | ) } { \sum _ { i = 0 } ^ { N - 1 } \phi ( | \mathbf { x } - \mathbf { x } _ { i } | ) }
$$

(with appropriate provision for the limiting case where $\mathbf { X }$ is equal to one of the $\mathbf { X } _ { i }$ ’s). Note that no solution of linear equations is required. The one-time work is negligible, while the work for each interpolation is $O ( N )$ , tolerable even for very large $N$ .

Shepard proposed the simple power-law function

$$
\phi ( r ) = r ^ { - p }
$$

with (typically) $1 < p \lesssim 3$ , as well as some more complicated functions with different exponents in an inner and outer region (see [8]). You can see that what is going on is basically interpolation by a nearness-weighted average, with nearby points contributing more strongly than distant ones.

Shepard interpolation is rarely as accurate as the well-tuned application of one of the other radial basis functions, above. On the other hand, it is simple, fast, and often just the thing for quick and dirty applications. It, and variants, are thus widely used.

An implementing object is

# struct Shep_interp {

Object for Shepard interpolation using n points in dim dimensions. Call constructor once, then interp as many times as desired.

Int dim, n;   
const MatDoub &pts;   
const VecDoub &vals;   
Doub pneg;

Shep_interp(MatDoub_I &ptss, VecDoub_I &valss, Doub $\scriptstyle \mathrm { p } = 2 .$ ) : dim(ptss.ncols()), n(ptss.nrows()) , pts(ptss), vals(valss), pneg $( - \tt p )$ {}

Constructor. The $\textbf { n } \times$ dim matrix ptss inputs the data points, the vector valss the function values. Set p to the desired exponent. The default value is typical.

Doub interp(VecDoub_I &pt) {

Return the interpolated function value at a dim-dimensional point pt. Doub r, w, sum $_ { 1 = 0 }$ ., sumw $\mathtt { \mathtt { \mathtt { = 0 } } }$ .; if (pt.size() $\ ! =$ dim) throw("RBF_interp bad pt size"); for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) { if ( $\scriptstyle x =$ rad(&pt[0],&pts[i][0])) $\mathrm { = } \mathrm { = } \ 0 .$ ) return vals[i]; sum $+ =$ ( ${ \textbf { \boldsymbol { w } } } =$ pow(r,pneg)); sumw $+ =$ w\*vals[i]; } return sumw/sum;   
}

Doub rad(const Doub \*p1, const Doub \*p2) { Euclidean distance. Doub sum $\qquad = \ 0 .$ .; for (Int i=0;i<dim; $\dot { 1 } + +$ ) sum $+ =$ SQR(p1[i]-p2[i]); return sqrt(sum); } };

# 3.7.4 Interpolation by Kriging

Kriging is a technique named for South African mining engineer D.G. Krige. It is basically a form of linear prediction (-13.6), also known in different communities as Gauss-Markov estimation or Gaussian process regression.

Kriging can be either an interpolation method or a fitting method. The distinction between the two is whether the fitted/interpolated function goes exactly through all the input data points (interpolation), or whether it allows measurement errors to be specified and then “smooths” to get a statistically better predictor that does not generally go through the data points (does not “honor the data”). In this section we consider only the former case, that is, interpolation. We will return to the latter case in $\ S 1 5 . 9$ .

At this point in the book, it is beyond our scope to derive the equations for kriging. You can turn to $\ S 1 3 . 6$ to get a flavor, and look to references [9,10,11] for details. To use kriging, you must be able to estimate the mean square variation of your function $y ( \mathbf { x } )$ as a function of offset distance r, a so-called variogram,

$$
\begin{array} { r } { v ( \mathbf { r } ) \sim \frac { 1 } { 2 } \left. \left[ y ( \mathbf { x } + \mathbf { r } ) - y ( \mathbf { x } ) \right] ^ { 2 } \right. } \end{array}
$$

where the average is over all $\mathbf { X }$ with fixed $\mathbf { r }$ . If this seems daunting, don’t worry. For interpolation, even very crude variogram estimates work fine, and we will give below a routine to estimate $v ( \mathbf { r } )$ from your input data points $\mathbf { X } _ { i }$ and $y _ { i } = y ( \mathbf { x } _ { i } )$ , $i = 0 , \ldots , N - 1$ , automatically. One usually takes $v ( \mathbf { r } )$ to be a function only of the magnitude $r = \left| \mathbf { r } \right|$ and writes it as $v ( r )$ .

Let $v _ { i j }$ denote $v ( | \mathbf { x } _ { i } - \mathbf { x } _ { j } | )$ , where $i$ and $j$ are input points, and let $v _ { * j }$ denote $v ( | \mathbf { x } _ { * } - \mathbf { x } _ { j } | )$ , $\mathbf { X } *$ being a point at which we want an interpolated value $y ( \mathbf { x } _ { * } )$ . Now define two vectors of length $N + 1$ ,

$$
\begin{array} { c } { { { \bf Y } = ( y _ { 0 } , y _ { 1 } , \dots , y _ { N - 1 } , 0 ) } } \\ { { { \bf V } _ { * } = ( v _ { * 1 } , v _ { * 2 } , \dots , v _ { * , N - 1 } , 1 ) } } \end{array}
$$

and an $( N + 1 ) \times ( N + 1 )$ symmetric matrix,

$$
\mathbf { V } = \left( \begin{array} { c c c c c } { v _ { 0 0 } } & { v _ { 0 1 } } & { \hdots } & { v _ { 0 , N - 1 } } & { 1 } \\ { v _ { 1 0 } } & { v _ { 1 1 } } & { \hdots } & { v _ { 1 , N - 1 } } & { 1 } \\ & & { \hdots } & & { \hdots } \\ { v _ { N - 1 , 0 } } & { v _ { N - 1 , 1 } } & { \hdots } & { v _ { N - 1 , N - 1 } } & { 1 } \\ { 1 } & { 1 } & { \hdots } & { 1 } & { 0 } \end{array} \right)
$$

Then the kriging interpolation estimate $\widehat { y } _ { * } \approx y ( \mathbf { x } _ { * } )$ is given by

$$
\widehat { y } _ { * } = \mathbf { V } _ { * } \cdot \mathbf { V } ^ { - 1 } \cdot \mathbf { Y }
$$

and its variance is given by

$$
\operatorname { V a r } ( \widehat { y } _ { * } ) = \mathbf { V } _ { * } \cdot \mathbf { V } ^ { - 1 } \cdot \mathbf { V } _ { * }
$$

Notice that if we compute, once, the $L U$ decomposition of $\mathbf { V }$ , and then backsubstitute, once, to get the vector $\mathbf { V } ^ { - 1 } \cdot \mathbf { Y }$ , then the individual interpolations cost only $O ( N )$ : Compute the vector $\mathbf { V } _ { * }$ and take a vector dot product. On the other hand, every computation of a variance, equation (3.7.15), requires an $O ( N ^ { 2 } )$ backsubstitution.

As an aside (if you have looked ahead to $\ S 1 3 . 6 )$ the purpose of the extra row and column in $\mathbf { V }$ , and extra last components in $\mathbf { V } _ { * }$ and $\mathbf { Y }$ , is to automatically calculate, and correct for, an appropriately weighted average of the data, and thus to make equation (3.7.14) an unbiased estimator.

Here is an implementation of equations (3.7.12) – (3.7.15). The constructor does the one-time work, while the two overloaded interp methods calculate either an interpolated value or else a value and a standard deviation (square root of the variance). You should leave the optional argument err set to the default value of NULL until you read $\ S 1 5 . 9$ .

# template<class T>

struct Krig {   
Object for interpolation by kriging, using npt points in ndim dimensions. Call constructor once, then interp as many times as desired. const MatDoub &x;   
const T &vgram;   
Int ndim, npt;   
Doub lastval, lasterr;   
VecDoub y,dstar,vstar,yvi;   
MatDoub v;   
LUdcmp \*vi;

Most recently computed value and (if computed) error.

Krig(MatDoub_I &xx, VecDoub_I &yy, T &vargram, const Doub \*err=NULL) : x(xx),vgram(vargram),npt(xx.nrows()),ndim(xx.ncols()),dstar(npt $+ 1 )$ , vstar(npt $^ { + 1 }$ ),v(npt+1,npt $+ 1$ ),y(npt+1),yvi(npt+1) {

Constructor. The npt $\times$ ndim matrix xx inputs the data points, the vector yy the function values. vargram is the variogram function or functor. The argument err is not used for interpolation; see $\ S 1 5 . 9$ .

Int i,j; for ( $\scriptstyle \dot { 1 } = 0$ ;i<npt; $\dot { \bf 1 } + +$ ) { Fill Y and V . y[i] $=$ yy[i]; for $( \ j = \mathtt { i }$ ;j<npt;j++) { v[i][j] $=$ v[j][i] $=$ vgram(rdist(&x[i][0],&x[j][0])); } v[i][npt] = v[npt][i] = 1.; } v[npt][npt] $=$ y[npt] = 0.; if (err) for ( $\dot { \bar { \boldsymbol { 1 } } } = 0$ ;i<npt; $\dot { 1 } + + \dot { 1 }$ ) v[i][i] -= SQR(err[i]); $\ S 1 5 . 9$ vi $=$ new LUdcmp(v); vi->solve(y,yvi); \~Krig() { delete vi; }

# Doub interp(VecDoub_I &xstar) {

Return an interpolated value at the point xstar. Int i; for ( $\scriptstyle \dot { \mathbf { 1 } } = 0$ ;i<npt; $\dot { 1 } + +$ ) vstar[i] $=$ vgram(rdist(&xstar[0],&x[i][0])); vstar[npt] $\ l = \ 1$ .; lastval $\qquad = \ 0 .$ .; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; $\ { \dot { \mathbf { 1 } } } < =$ npt; $\mathbf { i } + +$ ) lastval $+ =$ yvi[i]\*vstar[i]; return lastval;   
}

Doub interp(VecDoub_I &xstar, Doub &esterr) {

Return an interpolated value at the point xstar, and return its estimated error as esterr.

lastval $=$ interp(xstar);   
vi->solve(vstar,dstar);   
lasterr $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0 $ ;i $< =$ npt; $\Dot { \ b { 1 } } + +$ ) lasterr $+ =$ dstar[i]\*vstar[i];   
esterr $=$ lasterr $=$ sqrt(MAX(0.,lasterr));   
return lastval;

# }

Doub rdist(const Doub \*x1, const Doub \*x2) { Utility used internally. Cartesian distance between two points.

Doub $\mathtt { d } \mathtt { = } 0$ .;   
for (Int $\scriptstyle { \dot { 1 } } = 0$ ;i<ndim; $\dot { \bf 1 } + +$ ) d $+ =$ SQR(x1[i]-x2[i]);   
return sqrt(d);

The constructor argument vgram, the variogram function, can be either a func-

tion or functor (-1.3.3). For interpolation, you can use a Powvargram object that fits a simple model

$$
v ( r ) = \alpha r ^ { \beta }
$$

where $\beta$ is considered fixed and $\alpha$ is fitted by unweighted least squares over all pairs of data points $i$ and $j$ . We’ll get more sophisticated about variograms in $\ S 1 5 . 9$ ; but for interpolation, excellent results can be obtained with this simple choice. The value of $\beta$ should be in the range $1 \leq \beta < 2$ . A good general choice is 1:5, but for functions with a strong linear trend, you may want to experiment with values as large as 1:99. (The value 2 gives a degenerate matrix and meaningless results.) The optional argument nug will be explained in $\ S 1 5 . 9$ .

# struct Powvargram {

Functor for variogram $v ( r ) = \alpha r ^ { \beta }$ , where $\beta$ is specified, $\pmb { \alpha }$ is fitted from the data.

Doub alph, bet, nugsq;

Powvargram(MatDoub_I &x, VecDoub_I &y, const Doub beta $^ { = 1 }$ .5, const Doub nug=0.) : bet(beta), nugsq(nug\*nug) {

Constructor. The npt $\times$ ndim matrix $\mathbf { x }$ inputs the data points, the vector y the function values, beta the value of $\beta$ . For interpolation, the default value of beta is usually adequate. For the (rare) use of nug see $\ S 1 5 . 9$ .

Int i,j,k,npt=x.nrows(),ndim=x.ncols(); Doub rb,num $_ { = 0 }$ .,denom $_ { = 0 }$ .; for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<npt; $\dot { \bf 1 } + +$ ) for ( $\scriptstyle \cdot j = \mathbf { i } + 1$ ;j<npt;j++) { $x \mathrm { b } \ = \ 0 .$ ; for $\scriptstyle \mathtt { k } = 0$ ;k<ndim;k++) rb $+ =$ SQR(x[i][k]-x[j][k]); rb $=$ pow(rb,0.5\*beta); num $+ =$ rb\*(0.5\*SQR(y[i]-y[j]) - nugsq); denom $+ =$ SQR(rb); } alph $=$ num/denom; }

Doub operator() (const Doub r) const {return nugsq+alph\*pow(r,bet);} ;

Sample code for interpolating on a set of data points is

MatDoub x(npts,ndim);   
VecDoub y(npts), xstar(ndim);   
Powvargram vgram(x,y);   
Krig<Powvargram> krig(x,y,vgram);

followed by any number of interpolations of the form ystar $=$ krig.interp(xstar);

Be aware that while the interpolated values are quite insensitive to the variogram model, the estimated errors are rather sensitive to it. You should thus consider the error estimates as being order of magnitude only. Since they are also relatively expensive to compute, their value in this application is not great. They will be much more useful in $\ S 1 5 . 9$ , when our model includes measurement errors.

# 3.7.5 Curve Interpolation in Multidimensions

A different kind of interpolation, worth a brief mention here, is when you have an ordered set of $N$ tabulated points in $n$ dimensions that lie on a one-dimensional curve, $\mathbf { X } _ { 0 } , \ldots . . . \mathbf { X } _ { N - 1 }$ , and you want to interpolate other values along the curve. Two cases worth distinguishing are: (i) The curve is an open curve, so that $\mathbf { X } _ { 0 }$ and $\mathbf { X } _ { N - 1 }$ represent endpoints. (ii) The curve is a closed curve, so that there is an implied curve segment connecting $\mathbf { X } _ { N - 1 }$ back to $\mathbf { X } _ { 0 }$ .

A straightforward solution, using methods already at hand, is first to approximate distance along the curve by the sum of chord lengths between the tabulated points, and then to construct spline interpolations for each of the coordinates, $0 , \ldots$ ; $n - 1$ , as a function of that parameter. Since the derivative of any single coordinate with respect to arc length can be no greater than 1, it is guaranteed that the spline interpolations will be well-behaved.

Probably $90 \%$ of applications require nothing more complicated than the above. If you are in the unhappy $10 \%$ , then you will need to learn about Bezier curves ´ , $B$ - splines, and interpolating splines more generally [12,13,14]. For the happy majority, an implementation is

# struct Curve_interp {

Object for interpolating a curve specified by n points in dim dimensions.

Set if a closed curve.

Int dim, n, in;   
Bool cls;   
MatDoub pts;   
VecDoub s;   
VecDoub ans;   
NRvector<Spline_interp\*> srp;

Curve_interp(MatDoub &ptsin, Bool close $\mathtt { \mathtt { = 0 } }$ ) : n(ptsin.nrows()), dim(ptsin.ncols()), in(close ? 2\*n : n), cls(close), pts(dim,in), s(in), ans(dim), srp(dim) {

Constructor. The $\mathrm { ~ \tt ~ { ~ n ~ } ~ } \times$ dim matrix ptsin inputs the data points. Input close as 0 for an open curve, 1 for a closed curve. (For a closed curve, the last data point should not duplicate the first — the algorithm will connect them.)

Int i,ii,im,j,ofs; Doub ss,soff,db,de; ofs $=$ close ? n/2 : 0; The trick for closed curves is to duplicate half a $\mathbf { s } \left[ 0 \right] \ = \ 0 .$ ; period at the beginning and end, and then for ( $\scriptstyle \dot { 1 } = 0$ ;i<in; $\dot { \bf 1 } + +$ ) { use the middle half of the resulting spline. $\mathrm { i \mathrm { i } \mathrm { \Omega } = \Omega ( \mathrm { i } - \mathrm { o f } s + \mathrm { n } ) \Omega \mathrm { \Omega } \mathrm { \Omega } _ { \mathrm { 0 } } ^ { \mathrm { { q } } } \mathrm { n } ; }$ $\mathrm { i m \ = \ \Gamma ( i i \mathrm { \bf i - 1 + n } ) }$ % n; for $( \ j = 0$ ;j<dim; ${ \mathrm { j } } + + { \mathrm { j } }$ ) pts[j][i] $=$ ptsin[ii][j]; Store transpose. if (i>0) { Accumulate arc length. s[i] $=$ s[i-1] $^ +$ rad(&ptsin[ii][0],&ptsin[im][0]); if $\mathrm { \Delta \ J ~ } = = \mathrm { \Delta s [ i - 1 ] }$ ) throw("error in Curve_interp") Consecutive points may not be identical. For a closed curve, the last data point should not duplicate the first. } } ss $=$ close ? s[ofs+n]-s[ofs] : s[n-1]-s[0]; Rescale parameter so that the soff $=$ s[ofs]; interval [0,1] is the whole curve (or one period). for ( $\scriptstyle \dot { 1 } = 0$ ;i<in; $\dot { \bf 1 } + +$ ) s[i] $=$ (s[i]-soff)/ss; for (j ${ = } 0$ ;j<dim;j++) { Construct the splines using endpoint derivatives. db $=$ in $< ~ 4 ~ 7$ 1.e99 : fprime(&s[0],&pts[j][0],1); de $=$ in $<$ 4 ? 1.e99 : fprime(&s[in-1],&pts[j][in-1],-1); srp[j] $=$ new Spline_interp(s,&pts[j][0],db,de); } }

\~Curve_interp() {for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<dim;j++) delete srp[j];}

# VecDoub &interp(Doub t) {

Interpolate a point on the stored curve. The point is parameterized by t, in the range [0,1]. For open curves, values of t outside this range will return extrapolations (dangerous!). For closed curves, t is periodic with period 1.

if (cls) $\texttt { t } = \texttt { t }$ - floor(t); for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<dim; $\mathrm { j } + + \mathrm { . }$ ) ans[j] $=$ (\*srp[j]).interp(t); return ans; }

Doub fprime(Doub \*x, Doub \*y, Int pm) Utility for estimating the derivatives at the endpoints. x and y point to the abscissa and ordinate of the endpoint. If pm is $+ 1$ , points to the right will be used (left endpoint); if it is $^ { - 1 }$ , points to the left will be used (right endpoint). See text, below.

Doub $\mathbf { s } 1 ~ = ~ \mathbf { x } \left[ 0 \right] - \mathbf { x } \left[ \mathbf { p } \mathbf { m } * 1 \right]$ , ${ \bf s } 2 ~ = ~ { \bf x } \left[ 0 \right] - { \bf x } \left[ \mathrm { p m } { * 2 } \right]$ , ${ \bf s } 3 ~ = ~ { \bf x } \left[ 0 \right] - { \bf x } \left[ { \bf p } { \mathrm { m } } * 3 \right]$ , s12 $=$ s1-s2, $\mathtt { s } 1 3 \ = \ \mathtt { s } 1 - \mathtt { s } 3$ , ${ \tt s } 2 3 = { \tt s } 2 - { \tt s } 3 $ ;   
return -(s1\*s2/(s13\*s23\*s3))\*y[pm $^ *$ 3] $^ +$ (s1\*s3/(s12\*s2\*s23))\*y[pm\*2] -(s2\*s3/(s1\*s12\*s13))\*y[pm\*1]+(1./s1+1./s2+1./s3)\*y[0];

# }

Doub rad(const Doub \*p1, const Doub \*p2) {  
Euclidean distance.Doub sum $\qquad = \ 0$ .;for (Int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<dim;i++) sum $+ =$ SQR(p1[i]-p2[i]);return sqrt(sum);  
}

};

The utility routine fprime estimates the derivative of a function at a tabulated abscissa $x _ { 0 }$ using four consecutive tabulated abscissa-ordinate pairs, $( x _ { 0 } , y _ { 0 } ) , \ldots$ ; $( x _ { 3 } , y _ { 3 } )$ . The formula for this, readily derived by power-series expansion, is

$$
y _ { 0 } ^ { \prime } = - C _ { 0 } y _ { 0 } + C _ { 1 } y _ { 1 } - C _ { 2 } y _ { 2 } + C _ { 3 } y _ { 3 }
$$

where

$$
\begin{array} { l } { \displaystyle C _ { 0 } = \frac { 1 } { s _ { 1 } } + \frac { 1 } { s _ { 2 } } + \frac { 1 } { s _ { 3 } } } \\ { \displaystyle C _ { 1 } = \frac { s _ { 2 } s _ { 3 } } { s _ { 1 } ( s _ { 2 } - s _ { 1 } ) ( s _ { 3 } - s _ { 1 } ) } } \\ { \displaystyle C _ { 2 } = \frac { s _ { 1 } s _ { 3 } } { ( s _ { 2 } - s _ { 1 } ) s _ { 2 } ( s _ { 3 } - s _ { 2 } ) } } \\ { \displaystyle C _ { 3 } = \frac { s _ { 1 } s _ { 2 } } { ( s _ { 3 } - s _ { 1 } ) ( s _ { 3 } - s _ { 2 } ) s _ { 3 } } } \end{array}
$$

with

$$
\begin{array} { c } { { s _ { 1 } \equiv x _ { 1 } - x _ { 0 } } } \\ { { \nonumber } } \\ { { s _ { 2 } \equiv x _ { 2 } - x _ { 0 } } } \\ { { \nonumber } } \\ { { s _ { 3 } \equiv x _ { 3 } - x _ { 0 } } } \end{array}
$$

# CITED REFERENCES AND FURTHER READING:

Buhmann, M.D. 2003, Radial Basis Functions: Theory and Implementations (Cambridge, UK: Cambridge University Press).[1]

Powell, M.J.D. 1992, “The Theory of Radial Basis Function Approximation” in Advances in Numerical Analysis I: Wavelets, Subdivision Algorithms and Radial Functions,ed.W.A.Light (Oxford: Oxford University Press), pp. 105–210.[2]

Wikipedia. $^ { 2 0 0 7 + }$ , “Radial Basis Functions,” at http://en.wikipedia.org/.[3]

Beatson, R.K. and Greengard, L. 1997, “A Short Course on Fast Multipole Methods”, in Wavelets, Multilevel Methodsand Eliptic PDEs,eds.M.Ainsworth,J.Levesley，W.Light,andM.Marletta (Oxford: Oxford University Press), pp. 1–37.[4]

Beatson, R.K. and Newsam, G.N. 1998, “Fast Evaluation of Radial Basis Functions: Moment-Based Methods” in SIAM Journal on Scientific Computing, vol. 19, pp. 1428-1449.[5]   
Wendland, H. 2005, Scattered Data Approximation (Cambridge, UK: Cambridge University Press).[6]   
Franke, R. 1982, “Scattered Data Interpolation: Tests of Some Methods," Mathematics of Computation, vol.38,pp.181-200.[7]   
Shepard, D. 1968, “A Two-dimensional Interpolation Function for Irregularly-spaced Data,” in Proceedings of the 1968 23rd ACM National Conference (New York: ACM Press),pp.517- 524.[8]   
Cressie, N. 1991, Statistics for Spatial Data (New York: Wiley).[9]   
Wackernagel, H. 1998, Multivariate Geostatistics, 2nd ed. (Berlin: Springer).[10]   
Rybicki, G.B., and Press, W.H. 1992, “Interpolation, Realization, and Reconstruction of Noisy, Irregularly Sampled Data,” Astrophysical Journal, vol. 398, pp. 169–176.[11]   
Isaaks, E.H., and Srivastava, R.M. 1989, Applied Geostatistics (New York: Oxford University Press).   
Deutsch, C.V., and Journel, A.G. 1992, GSLIB: Geostatistical Software Library and User’s Guide (New York: Oxford University Press).   
Knott, G.D. 1999, Interpolating Cubic Splines (Boston: Birkhäuser).[12]   
De Boor, C. 2001, A Practical Guide to Splines (Berlin: Springer).[13]   
Prautzsch, H., Boehm, W., and Paluszny, M. 2002, Bézier and B-Spline Techniques (Berlin: Springer).[14]

# 3.8 Laplace Interpolation

In this section we look at a missing data or gridding problem, namely, how to restore missing or unmeasured values on a regular grid. Evidently some kind of interpolation from the not-missing values is required, but how shall we do this in a principled way?

One good method, already in use at the dawn of the computer age [1,2], is Laplace interpolation, sometimes called Laplace/Poisson interpolation. The general idea is to find an interpolating function $y$ that satisfies Laplace’s equation in $n$ dimensions,

$$
\nabla ^ { 2 } y = 0
$$

wherever there is no data, and which satisfies

$$
y ( \mathbf { x } _ { i } ) = y _ { i }
$$

at all measured data points. Generically, such a function does exist. The reason for choosing Laplace’s equation (among all possible partial differential equations, say) is that the solution to Laplace’s equation selects, in some sense, the smoothest possible interpolant. In particular, its solution minimizes the integrated square of the gradient,

$$
\int _ { \Omega } | \nabla y | ^ { 2 } d \Omega
$$

where $\Omega$ denotes the $n$ -dimensional domain of interest. This is a very general idea, and it can be applied to irregular meshes as well as to regular grids. Here, however, we consider only the latter.

For purposes of illustration (and because it is the most useful example) we further specialize to the case of two dimensions, and to the case of a Cartesian grid whose $x _ { 1 }$ and $x _ { 2 }$ values are evenly spaced — like a checkerboard.

In this geometry, the finite difference approximation to Laplace’s equation has a particularly simple form, one that echos the mean value theorem for continuous solutions of the Laplace equation: The value of the solution at any free gridpoint (i.e., not a point with a measured value) equals the average of its four Cartesian neighbors. (See $\ S 2 0 . 0 . \ r .$ ) Indeed, this already sounds a lot like interpolation.

If $y _ { 0 }$ denotes the value at a free point, while $y _ { u } , y _ { d } , y _ { l }$ , and $y _ { r }$ denote the values at its up, down, left, and right neighbors, respectively, then the equation satisfied is

$$
\begin{array} { r } { y _ { 0 } - \frac { 1 } { 4 } y _ { u } - \frac { 1 } { 4 } y _ { d } - \frac { 1 } { 4 } y _ { l } - \frac { 1 } { 4 } y _ { r } = 0 } \end{array}
$$

For gridpoints with measured values, on the other hand, a different (simple) equation is satisfied,

$$
y _ { 0 } = y _ { 0 } ( \mathrm { m e a s u r e d } )
$$

Note that these nonzero right-hand sides are what make an inhomogeneous, and therefore generally solvable, set of linear equations.

We are not quite done, since we must provide special forms for the top, bottom, left, and right boundaries, and for the four corners. Homogeneous choices that embody “natural” boundary conditions (with no preferred function values) are

$$
\begin{array} { r l } { y _ { 0 } - \frac 1 2 y _ { u } - \frac 1 2 y _ { d } = 0 \quad } & { ( \mathrm { l e f t a n d ~ r i g h t ~ b o u n d a r i e s } ) } \\ { y _ { 0 } - \frac 1 2 y _ { l } - \frac 1 2 y _ { r } = 0 \quad } & { ( \mathrm { t o p ~ a n d ~ b o t t o m ~ b o u n d a r i e s } ) } \\ { y _ { 0 } - \frac 1 2 y _ { r } - \frac 1 2 y _ { d } = 0 \quad } & { ( \mathrm { t o p \mathrm { - } l e f t ~ c o r n e r } ) } \\ { y _ { 0 } - \frac 1 2 y _ { l } - \frac 1 2 y _ { d } = 0 \quad } & { ( \mathrm { t o p \mathrm { - } r i g h t ~ c o r n e r } ) } \\ { y _ { 0 } - \frac 1 2 y _ { r } - \frac 1 2 y _ { u } = 0 \quad } & { ( \mathrm { b o t t o m \mathrm { - } l e f t ~ c o r n e r } ) } \\ { y _ { 0 } - \frac 1 2 y _ { l } - \frac 1 2 y _ { u } = 0 \quad } & { ( \mathrm { b o t t o m \mathrm { - } r i g h t ~ c o r n e r } ) } \end{array}
$$

Since every gridpoint corresponds to exactly one of the equations in (3.8.4), (3.8.5), or (3.8.4), we have exactly as many equations as there are unknowns. If the grid is $M$ by $N$ , then there are $M N$ of each. This can be quite a large number; but the equations are evidently very sparse. We solve them by defining a derived class from $\ S 2 . 7$ ’s Linbcg base class. You can readily identify all the cases of equations (3.8.4) – (3.8.6) in the code for atimes, below.

# struct Laplace_interp : Linbcg {

Object for interpolating missing data in a matrix by solving Laplace’s equation. Call constructor once, then solve one or more times (see text).

MatDoub &mat;   
Int ii,jj;   
Int nn,iter;   
VecDoub b,y,mask;   
Laplace_interp(MatDoub_IO &matrix) : mat(matrix), ii(mat.nrows()),   
jj(mat.ncols()), nn(ii\*jj), iter(0), b(nn), y(nn), mask(nn) {   
Constructor. Values greater than 1.e99 in the input matrix mat are deemed to be missing   
data. The matrix is not altered until solve is called. Int i,j,k; Doub $\mathtt { v 1 } = 0 .$ .;

for $\scriptstyle ( \mathtt { k } = 0$ ;k<nn;k++) { Fill the r.h.s. vector, the initial guess, $\mathrm { ~ i ~ } = \mathrm { ~ k ~ } / \mathrm { j } \mathrm { j }$ ; and a mask of the missing data. $\mathrm { ~ j ~ } = \mathrm { ~ k ~ }$ - i\*jj; if (mat[i][j] < 1.e99) { b[k] $=$ y[k] $\ l = \ l { \nabla \bot } =$ mat[i][j]; mask[k] $\ c = ~ 1$ ; } else { b[k] $\qquad = \ 0 .$ ; y[k] $\mathbf { \Sigma } = \mathbf { \Sigma } \_ { 1 } \mathbf { \Sigma } _ { 1 }$ ; mask[k] $\mathit { \Theta } = \mathit { \Theta } 0$ ; } } }

void asolve(VecDoub_I &b, VecDoub_O &x, const Int itrnsp);   
void atimes(VecDoub_I &x, VecDoub_O &r, const Int itrnsp);   
See definitions below. These are the real algorithmic content.

Doub solve(Doub tol $= 1$ .e-6, Int itmax=-1) {

Invoke Linbcg::solve with appropriate arguments. The default argument values will usually work, in which case this routine need be called only once. The original matrix mat is refilled with the interpolated solution.

Int i,j,k; Doub err; if (itmax $\mathit { \Theta } < = \mathit { \Theta } 0 .$ ) itmax $\quad = \ 2 *$ MAX(ii,jj); Linbcg::solve(b,y,1,tol,itmax,iter,err); for $\scriptstyle 1 = 0$ , $\scriptstyle \dot { 1 } = 0$ ;i<ii; $\dot { \bf 1 } + +$ ) for ( $\scriptstyle \mathbf { j } = 0$ ;j<jj;j $^ { + + }$ ) mat[i][j] $=$ y[k $+ + ]$ ; return err; } };

void Laplace_interp::asolve(VecDoub_I &b, VecDoub_O &x, const Int itrnsp) {   
Diagonal preconditioner. (Diagonal elements all unity.) Int i, $\mathtt { n } = \mathtt { b }$ .size(); for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n; $\dot { 1 } + +$ ) x[i] $=$ b[i];   
}

void Laplace_interp::atimes(VecDoub_I &x, VecDoub_O &r, const Int itrnsp) { Sparse matrix, and matrix transpose, multiply. This routine embodies eqs. (3.8.4), (3.8.5), and (3.8.6).

Int i,j,k, $\mathbf { n } { = } \mathbf { r }$ .size(),jjt,it;   
Doub del;   
for $( \mathtt { k } = 0$ ;k<n;k++) r[k] = 0.;   
for $\scriptstyle ( \mathtt { k } = 0$ ;k<n;k $^ { + + }$ ) { $\begin{array} { r l } { \dot { \mathbf { 1 } } } & { { } = } \end{array}$ k/jj; j = k - i\*jj; if (mask[k]) { Measured point, eq. (3.8.5). r[k] $+ =$ x[k]; } else if ( $\mathtt { i } > 0$ && i<ii-1 && j>0 && j<jj-1) { Interior point, eq. (3.8.4). if (itrnsp) { r[k] $+ =$ x[k]; del $=$ -0.25\*x[k]; r[k-1] $+ =$ del; r[k+1] $+ =$ del; r[k-jj] $+ =$ del; r[k+jj] $+ =$ del; } else { r[k] $=$ x[k] - 0.25\*(x[k-1]+x[k+1]+x[k+jj]+x[k-jj]); } } else if (i>0 && i<ii-1) { Left or right edge, eq. (3.8.6). if (itrnsp) { r[k] $+ = \texttt { x }$ [k]; del $=$ -0.5\*x[k]; r[k-jj] $+ =$ del;

r[k+jj] $+ =$ del; } else { r[k] $=$ x[k] - 0.5\*(x[k+jj]+x[k-jj]); } } else if (j>0 && j<jj-1) { Top or bottom edge, eq. (3.8.6). if (itrnsp) { r[k] $+ =$ x[k]; del $=$ -0.5\*x[k]; r[k-1] $+ =$ del; r[k+1] $+ =$ del; } else { r[k] $=$ x[k] - 0.5\*(x[k+1]+x[k-1]); } } else { Corners, eq. (3.8.6). jjt $= \mathrm { \ i = = } 0$ ? jj : -jj; it $= \mathrm { \ j = = } 0$ ? 1 : -1; if (itrnsp) { r[k] $+ =$ x[k]; del $=$ -0.5\*x[k]; r[k+jjt] $+ =$ del; r[k+it] $+ =$ del; } else { r[k] $=$ x[k] - 0.5\*(x[k+jjt]+x[k+it]); } }

Usage is quite simple. Just fill a matrix with function values where they are known, and with 1.e99 where they are not; send the matrix to the constructor; and call the solve routine. The missing values will be interpolated. The default arguments should serve for most cases.

Int m=...,n=...;   
MatDoub mat(m,n);   
Laplace_interp mylaplace(mat);   
mylaplace.solve();

Quite decent results are obtained for smooth functions on $3 0 0 ~ \times ~ 3 0 0$ matrices in which a random $10 \%$ of gridpoints have known function values, with $90 \%$ interpolated. However, since compute time scales as $M N$ max $( M , N )$ (that is, as the cube), this is not a method to use for much larger matrices, unless you break them up into overlapping tiles. If you experience convergence difficulties, then you should call solve, with appropriate nondefault arguments, several times in succession, and look at the returned error estimate after each call returns.

# 3.8.1 Minimum Curvature Methods

Laplace interpolation has a tendency to yield cone-like cusps around any small islands of known data points that are surrounded by a sea of unknowns. The reason is that, in two dimensions, the solution of Laplace’s equation near a point source is logarithmically singular. When the known data is spread fairly evenly (if randomly) across the grid, this is not generally a problem. Minimum curvature methods deal with the problem at a more fundamental level by being based on the biharmonic equation

$$
\nabla ( \nabla y ) = 0
$$

instead of Laplace’s equation. Solutions of the biharmonic equation minimize the integrated square of the curvature,

$$
\int _ { \Omega } | \nabla ^ { 2 } y | ^ { 2 } d \Omega
$$

Minimum curvature methods are widely used in the earth-science community [3,4].

The references give a variety of other methods that can be used for missing data interpolation and gridding.

# CITED REFERENCES AND FURTHER READING:

Noma, A.A. and Misulia, M.G. 1959, “Programming Topographic Maps for Automatic Terrain Model Construction,” Surveying and Mapping, vol. 19, pp. 355–366.[1]   
Crain, I.K. 1970, “Computer Interpolation and Contouring of Two-dimensional Data: a Review,” Geoexploration,vol.8,pp.71-86.[2]   
Burrough, P.A. 1998, Principles of Geographical Information Systems, 2nd ed. (Oxford, UK: Clarendon Press)   
Watson, D.F. 1982, Contouring: A Guide to the Analysis and Display of Spatial Data (Oxford, UK: Pergamon).   
Briggs, I.C. 1974, “Machine Contouring Using Minimum Curvature,” Geophysics, vol. 39, pp. 39– 48.[3]   
Smith, W.H.F. and Wessel, P. 1990, “Gridding With Continuous Curvature Splines in Tension,” Geophysics,vol.55,pp.293-305.[4]

# 4.0 Introduction

Numerical integration, which is also called quadrature, has a history extending back to the invention of calculus and before. The fact that integrals of elementary functions could not, in general, be computed analytically, while derivatives could be, served to give the field a certain panache, and to set it a cut above the arithmetic drudgery of numerical analysis during the whole of the 18th and 19th centuries.

With the invention of automatic computing, quadrature became just one numerical task among many, and not a very interesting one at that. Automatic computing, even the most primitive sort involving desk calculators and rooms full of “computers” (that were, until the 1950s, people rather than machines), opened to feasibility the much richer field of numerical integration of differential equations. Quadrature is merely the simplest special case: The evaluation of the integral

$$
I = \int _ { a } ^ { b } f ( x ) d x
$$

is precisely equivalent to solving for the value $I \equiv y ( b )$ the differential equation

$$
{ \frac { d y } { d x } } = f ( x )
$$

with the boundary condition

$$
y ( a ) = 0
$$

Chapter 17 of this book deals with the numerical integration of differential equations. In that chapter, much emphasis is given to the concept of “variable” or “adaptive” choices of stepsize. We will not, therefore, develop that material here. If the function that you propose to integrate is sharply concentrated in one or more peaks, or if its shape is not readily characterized by a single length scale, then it is likely that you should cast the problem in the form of $( 4 . 0 . 2 ) - ( 4 . 0 . 3 )$ and use the methods of Chapter 17. (But take a look at $\ S 4 . 7$ first.)

The quadrature methods in this chapter are based, in one way or another, on the obvious device of adding up the value of the integrand at a sequence of abscissas within the range of integration. The game is to obtain the integral as accurately as possible with the smallest number of function evaluations of the integrand. Just as in the case of interpolation (Chapter 3), one has the freedom to choose methods of various orders, with higher order sometimes, but not always, giving higher accuracy. Romberg integration, which is discussed in $\ S 4 . 3$ , is a general formalism for making use of integration methods of a variety of different orders, and we recommend it highly.

Apart from the methods of this chapter and of Chapter 17, there are yet other methods for obtaining integrals. One important class is based on function approximation. We discuss explicitly the integration of functions by Chebyshev approximation (Clenshaw-Curtis quadrature) in $\ S 5 . 9$ . Although not explicitly discussed here, you ought to be able to figure out how to do cubic spline quadrature using the output of the routine spline in $\ S 3 . 3$ . (Hint: Integrate equation 3.3.3 over $x$ analytically. See [1].)

Some integrals related to Fourier transforms can be calculated using the fast Fourier transform (FFT) algorithm. This is discussed in $\ S 1 3 . 9$ . A related problem is the evaluation of integrals with long oscillatory tails. This is discussed at the end of $\ S 5 . 3$ .

Multidimensional integrals are a whole ’nother multidimensional bag of worms. Section 4.8 is an introductory discussion in this chapter; the important technique of Monte Carlo integration is treated in Chapter 7.

# CITED REFERENCES AND FURTHER READING:

Carnahan, B., Luther, H.A., and Wilkes, J.O. 1969, Applied Numerical Methods (New York: Wiley), Chapter 2.   
Isaacson, E., and Keller, H.B. 1966, Analysis of Numerical Methods; reprinted 1994 (New York: Dover), Chapter 7.   
Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), Chapter 4.   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), Chapter 3.   
Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), Chapter 4.   
Dahlquist, G., and Bjorck, A. 1974, Numerical Methods (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2003 (New York: Dover), $\ S 7 . 4$ .   
Kahaner, D., Moler, C., and Nash, S. 1989, Numerical Methods and Software (Englewood Cliffs, NJ: Prentice-Hall), Chapter 5.   
Forsythe, G.E., Malcolm, M.A., and Moler, C.B. 1977, Computer Methods for Mathematical Computations (Englewood Cliffs,NJ: Prentice-Hal), $\ S 5 . 2$ , p. 89.[1]   
Davis, P., and Rabinowitz, P. 1984, Methods of Numerical Integration, 2nd ed. (Orlando, FL: Academic Press).

# 4.1 Classical Formulas for Equally Spaced Abscissas

Where would any book on numerical analysis be without Mr. Simpson and his “rule”? The classical formulas for integrating a function whose value is known at equally spaced steps have a certain elegance about them, and they are redolent with historical association. Through them, the modern numerical analyst communes with the spirits of his or her predecessors back across the centuries, as far as the time of Newton, if not farther. Alas, times do change; with the exception of two of the most modest formulas (“extended trapezoidal rule,” equation 4.1.11, and “extended midpoint rule,” equation 4.1.19; see $\ S 4 . 2 )$ , the classical formulas are almost entirely useless. They are museum pieces, but beautiful ones; we now enter the museum. (You can skip to $\ S 4 . 2$ if you are not touristically inclined.)

![](images/4ed7d53eca85e8394337854f1af11bc3251723c433230bf5f6bf28f45cc62ad7.jpg)  
Figure 4.1.1. Quadrature formulas with equally spaced abscissas compute the integral of a function between $x _ { 0 }$ and $x _ { N }$ . Closed formulas evaluate the function on the boundary points, while open formulas refrain from doing so (useful if the evaluation algorithm breaks down on the boundary points).

Some notation: We have a sequence of abscissas, denoted $x _ { 0 } , x _ { 1 } , \ldots , x _ { N - 1 } , x _ { N }$ , that are spaced apart by a constant step $h$ ,

$$
x _ { i } = x _ { 0 } + i h \qquad i = 0 , 1 , \dotsc , N
$$

A function $f ( x )$ has known values at the $x _ { i }$ ’s,

$$
f ( x _ { i } ) \equiv f _ { i }
$$

We want to integrate the function $f ( x )$ between a lower limit $a$ and an upper limit $b$ , where $a$ and $b$ are each equal to one or the other of the $x _ { i }$ ’s. An integration formula that uses the value of the function at the endpoints, $f ( a )$ or $f ( b )$ , is called a closed formula. Occasionally, we want to integrate a function whose value at one or both endpoints is difficult to compute (e.g., the computation of $f$ goes to a limit of zero over zero there, or worse yet has an integrable singularity there). In this case we want an open formula, which estimates the integral using only $x _ { i }$ ’s strictly between $a$ and $b$ (see Figure 4.1.1).

The basic building blocks of the classical formulas are rules for integrating a function over a small number of intervals. As that number increases, we can find rules that are exact for polynomials of increasingly high order. (Keep in mind that higher order does not always imply higher accuracy in real cases.) A sequence of such closed formulas is now given.

# 4.1.1 Closed Newton-Cotes Formulas

Trapezoidal rule:

$$
\begin{array} { r l } { \displaystyle \int _ { x _ { 0 } } ^ { x _ { 1 } } f ( x ) d x = h \biggl [ \frac { 1 } { 2 } f _ { 0 } + \frac { 1 } { 2 } f _ { 1 } \biggr ] } & { { } + O ( h ^ { 3 } f ^ { \prime \prime } ) } \end{array}
$$

Here the error term $O ( )$ signifies that the true answer differs from the estimate by an amount that is the product of some numerical coefficient times $h ^ { 3 }$ times the value of the function’s second derivative somewhere in the interval of integration. The coefficient is knowable, and it can be found in all the standard references on this subject. The point at which the second derivative is to be evaluated is, however, unknowable. If we knew it, we could evaluate the function there and have a higherorder method! Since the product of a knowable and an unknowable is unknowable, we will streamline our formulas and write only $O ( )$ , instead of the coefficient.

Equation (4.1.3) is a two-point formula $x _ { 0 }$ and $x _ { 1 }$ ). It is exact for polynomials up to and including degree 1, i.e., $f ( x ) = x$ . One anticipates that there is a threepoint formula exact up to polynomials of degree 2. This is true; moreover, by a cancellation of coefficients due to left-right symmetry of the formula, the three-point formula is exact for polynomials up to and including degree 3, i.e., $f ( x ) = x ^ { 3 }$ .

Simpson’s rule:

$$
\int _ { x _ { 0 } } ^ { x _ { 2 } } f ( x ) d x = h \biggl [ \frac { 1 } { 3 } f _ { 0 } + \frac { 4 } { 3 } f _ { 1 } + \frac { 1 } { 3 } f _ { 2 } \biggr ] \quad + O ( h ^ { 5 } f ^ { ( 4 ) } )
$$

Here $f ^ { ( 4 ) }$ means the fourth derivative of the function $f$ evaluated at an unknown place in the interval. Note also that the formula gives the integral over an interval of size $2 h$ , so the coefficients add up to 2.

There is no lucky cancellation in the four-point formula, so it is also exact for polynomials up to and including degree 3.

Simpson’s $\frac { 3 } { 8 }$ rule:

$$
\begin{array} { r l } { \displaystyle \int _ { x _ { 0 } } ^ { x _ { 3 } } f ( x ) d x = h \biggl [ \frac { 3 } { 8 } f _ { 0 } + \frac { 9 } { 8 } f _ { 1 } + \frac { 9 } { 8 } f _ { 2 } + \frac { 3 } { 8 } f _ { 3 } \biggr ] } & { { } + O ( h ^ { 5 } f ^ { ( 4 ) } ) } \end{array}
$$

The five-point formula again benefits from a cancellation:

Bode’s rule:

$$
\int _ { x _ { 0 } } ^ { x _ { 4 } } f ( x ) d x = h \biggl [ { \frac { 1 4 } { 4 5 } } f _ { 0 } + { \frac { 6 4 } { 4 5 } } f _ { 1 } + { \frac { 2 4 } { 4 5 } } f _ { 2 } + { \frac { 6 4 } { 4 5 } } f _ { 3 } + { \frac { 1 4 } { 4 5 } } f _ { 4 } \biggr ] \quad + { \cal O } ( h ^ { 7 } f ^ { ( 6 ) } )
$$

This is exact for polynomials up to and including degree 5.

At this point the formulas stop being named after famous personages, so we will not go any further. Consult [1] for additional formulas in the sequence.

# 4.1.2 Extrapolative Formulas for a Single Interval

We are going to depart from historical practice for a moment. Many texts would give, at this point, a sequence of “Newton-Cotes Formulas of Open Type.” Here is

an example:

$$
\begin{array} { r l } { \displaystyle \int _ { x _ { 0 } } ^ { x _ { 5 } } f ( x ) d x = h \biggl [ \frac { 5 5 } { 2 4 } f _ { 1 } + \frac { 5 } { 2 4 } f _ { 2 } + \frac { 5 } { 2 4 } f _ { 3 } + \frac { 5 5 } { 2 4 } f _ { 4 } \biggr ] } & { { } + O ( h ^ { 5 } f ^ { ( 4 ) } ) } \end{array}
$$

Notice that the integral from $a = x _ { 0 }$ to $b = x _ { 5 }$ is estimated, using only the interior points $x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 }$ . In our opinion, formulas of this type are not useful for the reasons that (i) they cannot usefully be strung together to get “extended” rules, as we are about to do with the closed formulas, and (ii) for all other possible uses they are dominated by the Gaussian integration formulas, which we will introduce in $\ S 4 . 6$ .

Instead of the Newton-Cotes open formulas, let us set out the formulas for estimating the integral in the single interval from $x _ { 0 }$ to $x _ { 1 }$ , using values of the function $f$ at $x _ { 1 } , x _ { 2 } , \ldots .$ These will be useful building blocks later for the “extended” open formulas.

$$
\begin{array} { r l } { \displaystyle \int _ { x _ { 0 } } ^ { x _ { 1 } } f ( x ) d x = h [ f _ { 1 } ] } & { { } + O ( h ^ { 2 } f ^ { \prime } ) } \\ { \displaystyle } & { { } } \\ { \displaystyle \int _ { x _ { 0 } } ^ { x _ { 1 } } f ( x ) d x = h \biggl [ \frac { 3 } { 2 } f _ { 1 } - \frac { 1 } { 2 } f _ { 2 } \biggr ] } & { { } + O ( h ^ { 3 } f ^ { \prime \prime } ) } \\ { \displaystyle \int _ { x _ { 0 } } ^ { x _ { 1 } } f ( x ) d x = h \biggl [ \frac { 2 3 } { 1 2 } f _ { 1 } - \frac { 1 6 } { 1 2 } f _ { 2 } + \frac { 5 } { 1 2 } f _ { 3 } \biggr ] } & { { } + O ( h ^ { 4 } f ^ { ( 3 ) } ) } \\ { \displaystyle } & { { } \int _ { x _ { 0 } } ^ { x _ { 1 } } f ( x ) d x = h \biggl [ \frac { 5 5 } { 2 4 } f _ { 1 } - \frac { 5 9 } { 2 4 } f _ { 2 } + \frac { 3 7 } { 2 4 } f _ { 3 } - \frac { 9 } { 2 4 } f _ { 4 } \biggr ] } & { { } + O ( h ^ { 5 } f ^ { ( 4 ) } ) } \end{array}
$$

Perhaps a word here would be in order about how formulas like the above can be derived. There are elegant ways, but the most straightforward is to write down the basic form of the formula, replacing the numerical coefficients with unknowns, say $p , q , r , s$ . Without loss of generality take $x _ { 0 } = 0$ and $x _ { 1 } = 1$ , so $h = 1$ . Substitute in turn for $f ( x )$ (and for $f _ { 1 } , f _ { 2 } , f _ { 3 } , f _ { 4 } )$ the functions $f ( x ) = 1$ , $f ( x ) = x$ , $f ( x ) =$ $x ^ { 2 }$ , and $f ( x ) = x ^ { 3 }$ . Doing the integral in each case reduces the left-hand side to a number and the right-hand side to a linear equation for the unknowns $p , q , r , s$ . Solving the four equations produced in this way gives the coefficients.

# 4.1.3 Extended Formulas (Closed)

If we use equation (4.1.3) $N - 1$ times to do the integration in the intervals $( x _ { 0 } , x _ { 1 } ) , ( x _ { 1 } , x _ { 2 } ) , . . .$ ; $( x _ { N - 2 } , x _ { N - 1 } )$ and then add the results, we obtain an “extended” or “composite” formula for the integral from $x _ { 0 }$ to $x N { - } 1$ .

Extended trapezoidal rule:

$$
\begin{array} { r l } { \displaystyle \int _ { x _ { 0 } } ^ { x _ { N - 1 } } f ( x ) d x = h \bigg [ \frac { 1 } { 2 } f _ { 0 } + f _ { 1 } + f _ { 2 } + } & { } \\ { \displaystyle \qquad \cdots + f _ { N - 2 } + \frac { 1 } { 2 } f _ { N - 1 } \bigg ] } & { + O \left( \frac { ( b - a ) ^ { 3 } f ^ { \prime \prime } } { N ^ { 2 } } \right) } \end{array}
$$

Here we have written the error estimate in terms of the interval $b - a$ and the number of points $N$ instead of in terms of $h$ . This is clearer, since one is usually holding $a$ and

$b$ fixed and wanting to know, e.g., how much the error will be decreased by taking twice as many steps (in this case, it is by a factor of 4). In subsequent equations we will show only the scaling of the error term with the number of steps.

For reasons that will not become clear until $\ S 4 . 2$ , equation (4.1.11) is in fact the most important equation in this section; it is the basis for most practical quadrature schemes.

The extended formula of order $1 / N ^ { 3 }$ is

$$
\begin{array} { r l } { \displaystyle \int _ { x _ { 0 } } ^ { x _ { N - 1 } } f ( x ) d x = h \biggl [ \frac { 5 } { 1 2 } f _ { 0 } + \frac { 1 3 } { 1 2 } f _ { 1 } + f _ { 2 } + f _ { 3 } + } & { } \\ { \qquad \cdots + f _ { N - 3 } + \frac { 1 3 } { 1 2 } f _ { N - 2 } + \frac { 5 } { 1 2 } f _ { N - 1 } \biggr ] } & { { } + { \cal O } \left( \frac { 1 } { N ^ { 3 } } \right) } \end{array}
$$

(We will see in a moment where this comes from.)

If we apply equation (4.1.4) to successive, nonoverlapping pairs of intervals, we get the extended Simpson’s rule:

$$
\begin{array} { r l } { \displaystyle \int _ { x _ { 0 } } ^ { x _ { N - 1 } } f ( x ) d x = h \biggl [ \frac { 1 } { 3 } f _ { 0 } + \frac { 4 } { 3 } f _ { 1 } + \frac { 2 } { 3 } f _ { 2 } + \frac { 4 } { 3 } f _ { 3 } + } & { { } } \\ { \displaystyle \qquad \cdots + \frac { 2 } { 3 } f _ { N - 3 } + \frac { 4 } { 3 } f _ { N - 2 } + \frac { 1 } { 3 } f _ { N - 1 } \biggr ] } & { { } + O \left( \frac { 1 } { N ^ { 4 } } \right) } \end{array}
$$

Notice that the $2 / 3 , 4 / 3$ alternation continues throughout the interior of the evaluation. Many people believe that the wobbling alternation somehow contains deep information about the integral of their function that is not apparent to mortal eyes. In fact, the alternation is an artifact of using the building block (4.1.4). Another extended formula with the same order as Simpson’s rule is

$$
\begin{array} { r l r } {  { \int _ { x _ { 0 } } ^ { x _ { N - 1 } } f ( x ) d x = h \biggl [ \frac { 3 } { 8 } f _ { 0 } + \frac { 7 } { 6 } f _ { 1 } + \frac { 2 3 } { 2 4 } f _ { 2 } + f _ { 3 } + f _ { 4 } + } } \\ & { } & { \quad \cdots + f _ { N - 5 } + f _ { N - 4 } + \frac { 2 3 } { 2 4 } f _ { N - 3 } + \frac { 7 } { 6 } f _ { N - 2 } + \frac { 3 } { 8 } f _ { N - 1 } \biggr ] } \\ & { } & { \quad + O ( \frac { 1 } { N ^ { 4 } } ) \qquad ( 4 . 1 . } \end{array}
$$

This equation is constructed by fitting cubic polynomials through successive groups of four points; we defer details to $\ S 1 9 . 3$ , where a similar technique is used in the solution of integral equations. We can, however, tell you where equation (4.1.12) came from. It is Simpson’s extended rule, averaged with a modified version of itself in which the first and last steps are done with the trapezoidal rule (4.1.3). The trapezoidal step is two orders lower than Simpson’s rule; however, its contribution to the integral goes down as an additional power of $N$ (since it is used only twice, not $N$ times). This makes the resulting formula of degree one less than Simpson.

# 4.1.4 Extended Formulas (Open and Semi-Open)

We can construct open and semi-open extended formulas by adding the closed formulas (4.1.11) – (4.1.14), evaluated for the second and subsequent steps, to the extrapolative open formulas for the first step, (4.1.7) – (4.1.10). As discussed immediately above, it is consistent to use an end step that is of one order lower than the (repeated) interior step. The resulting formulas for an interval open at both ends are as follows.

Equations (4.1.7) and (4.1.11) give

$$
\int _ { x _ { 0 } } ^ { x _ { N - 1 } } f ( x ) d x = h \biggl [ { \frac { 3 } { 2 } } f _ { 1 } + f _ { 2 } + f _ { 3 } + \cdots + f _ { N - 3 } + { \frac { 3 } { 2 } } f _ { N - 2 } \biggr ] \quad + { \cal O } \left( { \frac { 1 } { N ^ { 2 } } } \right)
$$

Equations (4.1.8) and (4.1.12) give

$$
\begin{array} { r l } { \displaystyle \int _ { x _ { 0 } } ^ { x _ { N - 1 } } f ( x ) d x = h \biggl [ \frac { 2 3 } { 1 2 } f _ { 1 } + \frac { 7 } { 1 2 } f _ { 2 } + f _ { 3 } + f _ { 4 } + } & { { } } \\ { \displaystyle \qquad \cdots + f _ { N - 4 } + \frac { 7 } { 1 2 } f _ { N - 3 } + \frac { 2 3 } { 1 2 } f _ { N - 2 } \biggr ] } & { { } + { \cal O } \left( \frac { 1 } { N ^ { 3 } } \right) } \end{array}
$$

Equations (4.1.9) and (4.1.13) give

$$
\begin{array} { r l } { \displaystyle \int _ { x _ { 0 } } ^ { x _ { N - 1 } } f ( x ) d x = h \bigg [ \frac { 2 7 } { 1 2 } f _ { 1 } + 0 + \frac { 1 3 } { 1 2 } f _ { 3 } + \frac { 4 } { 3 } f _ { 4 } + } & { { } } \\ { \displaystyle \qquad \cdots + \frac { 4 } { 3 } f _ { N - 5 } + \frac { 1 3 } { 1 2 } f _ { N - 4 } + 0 + \frac { 2 7 } { 1 2 } f _ { N - 2 } \bigg ] } & { { } + O \left( \frac { 1 } { N ^ { 4 } } \right) } \end{array}
$$

The interior points alternate 4/3 and $2 / 3$ . If we want to avoid this alternation, we can combine equations (4.1.9) and (4.1.14), giving

$$
\begin{array} { r l r } {  { \int _ { x _ { 0 } } ^ { x _ { N - 1 } } f ( x ) d x = h \biggl [ \frac { 5 5 } { 2 4 } f _ { 1 } - \frac { 1 } { 6 } f _ { 2 } + \frac { 1 1 } { 8 } f _ { 3 } + f _ { 4 } + f _ { 5 } + f _ { 6 } + } } \\ & { } & { \quad \cdots + f _ { N - 6 } + f _ { N - 5 } + \frac { 1 1 } { 8 } f _ { N - 4 } - \frac { 1 } { 6 } f _ { N - 3 } + \frac { 5 5 } { 2 4 } f _ { N - 2 } \biggr ] } \\ & { } & { \quad + O ( \frac { 1 } { N ^ { 4 } } ) \quad \quad \quad ( 4 . 1 . 1 } \end{array}
$$

We should mention in passing another extended open formula, for use where the limits of integration are located halfway between tabulated abscissas. This one is known as the extended midpoint rule and is accurate to the same order as (4.1.15):

$$
\int _ { x _ { 0 } } ^ { x _ { N - 1 } } f ( x ) d x = h [ f _ { 1 / 2 } + f _ { 3 / 2 } + f _ { 5 / 2 } + \cdots + f _ { N - 5 / 2 } + f _ { N - 3 / 2 } ] \quad + O \left( { \frac { 1 } { N ^ { 2 } } } \right)
$$

There are also formulas of higher order for this situation, but we will refrain from giving them.

The semi-open formulas are just the obvious combinations of equations (4.1.11) $- \left( 4 . 1 . 1 4 \right)$ with (4.1.15) – (4.1.18), respectively. At the closed end of the integration, use the weights from the former equations; at the open end, use the weights from

![](images/f380df23b3368f34b77a19598a8ca7f4a455df5f73929b6bf0a45c0208576956.jpg)  
Figure 4.2.1. Sequential calls to the routine Trapzd incorporate the information from previous calls and evaluate the integrand only at those new points necessary to refine the grid. The bottom line shows the totality of function evaluations after the fourth call. The routine qsimp, by weighting the intermediate results, transforms the trapezoid rule into Simpson’s rule with essentially no additional overhead.

the latter equations. One example should give the idea, the formula with error term decreasing as $1 / N ^ { 3 }$ , which is closed on the right and open on the left:

$$
\begin{array} { r l } { \displaystyle \int _ { x _ { 0 } } ^ { x _ { N - 1 } } f ( x ) d x = h \biggl [ \frac { 2 3 } { 1 2 } f _ { 1 } + \frac { 7 } { 1 2 } f _ { 2 } + f _ { 3 } + f _ { 4 } + } & { } \\ { \qquad \cdots + f _ { N - 3 } + \frac { 1 3 } { 1 2 } f _ { N - 2 } + \frac { 5 } { 1 2 } f _ { N - 1 } \biggr ] } & { { } + { \cal O } \left( \frac { 1 } { N ^ { 3 } } \right) } \end{array}
$$

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, $\ S 2 5 . 4$ .[1]   
Isaacson, E., and Keller, H.B. 1966, Analysis of Numerical Methods; reprinted 1994 (New York: Dover), $\ S 7 . 1$ .

# 4.2 Elementary Algorithms

Our starting point is equation (4.1.11), the extended trapezoidal rule. There are two facts about the trapezoidal rule that make it the starting point for a variety of algorithms. One fact is rather obvious, while the second is rather “deep.”

The obvious fact is that, for a fixed function $f ( x )$ to be integrated between fixed limits $a$ and $b$ , one can double the number of intervals in the extended trapezoidal rule without losing the benefit of previous work. The coarsest implementation of the trapezoidal rule is to average the function at its endpoints $a$ and $b$ . The first stage of refinement is to add to this average the value of the function at the halfway point. The second stage of refinement is to add the values at the 1/4 and 3/4 points. And so on (see Figure 4.2.1).

As we will see, a number of elementary quadrature algorithms involve adding successive stages of refinement. It is convenient to encapsulate this feature in a Quadrature structure:

# struct Quadrature{

Abstract base class for elementary quadrature algorithms. Int n; Current level of refinement. virtual Doub next ${ \mathrm { ~ ( ~ ) ~ } } = { \mathrm { ~ 0 ~ } }$ ; Returns the value of the integral at the nth stage of refinement. The function next() must be defined in the derived class.

Then the Trapzd structure is derived from this as follows:

template<class T>   
struct Trapzd : Quadrature {   
Routine implementing the extended trapezoidal rule. Doub a,b,s; Limits of integration and current value of integral. T &func; Trapzd() {}; Trapzd(T &funcc, const Doub aa, const Doub bb) : func(funcc), a(aa), b(bb) $\{ \mathbf { n } { = } 0 ; \}$ The constructor takes as inputs func, the function or functor to be integrated between limits a and b, also input. Doub next() { Returns the nth stage of refinement of the extended trapezoidal rule. On the first call $\scriptstyle ( \mathtt { n } = 1 )$ ), the routine returns the crudest estimate of $\textstyle \int _ { a } ^ { b } f ( x ) d x$ . Subsequent calls set $\scriptstyle \mathtt { n = 2 } , 3 , \dotsc$ . and improve the accuracy by adding $2 ^ { \mathtt { n } - 2 }$ additional interior points. Doub x,tnm,sum,del; Int it,j; $\mathtt { n } + +$ ; if $\mathbf { \Phi } _ { \mathrm { ~ n ~ } } = = \mathbf { \Phi } _ { 1 }$ ) { return (s=0.5\*(b-a)\*(func(a)+func(b))); } else { for ( $\dot { \bar { 1 } } \ t = 1$ ,j=1;j<n-1;j++) it <<= 1; tnm $_ { 1 } =$ it; del (b-a)/tnm; This is the spacing of the points to be added. $\mathtt { x } \mathtt { = a } \mathtt { + } 0$ .5\*del; for (sum $_ { 1 = 0 }$ .0, $\scriptstyle \mathbf { j } = 0$ ;j<it;j++, $_ { \tt X } + =$ del) sum $+ =$ func(x); $\mathtt { s } = 0$ .5\*(s+(b-a)\*sum/tnm); This replaces s by its refined value. return s; } }   
};

Note that Trapzd is templated on the whole struct and does not just contain a templated function. This is necessary because it retains a reference to the supplied function or functor as a member variable.

The Trapzd structure is a workhorse that can be harnessed in several ways. The simplest and crudest is to integrate a function by the extended trapezoidal rule where you know in advance (we can’t imagine how!) the number of steps you want. If you want $2 ^ { M } + 1$ , you can accomplish this by the fragment

Ftor func; Functor func here has no parameters.   
Trapzd<Ftor> s(func,a,b);   
for( $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j $< = \mathtt { m } + 1$ ;j++) val $= \tt s$ .next();

with the answer returned as val. Here Ftor is a functor containing the function to be integrated.

Much better, of course, is to refine the trapezoidal rule until some specified degree of accuracy has been achieved. A function for this is

# template<class T>

Doub qtrap(T &func, const Doub a, const Doub b, const Doub eps $^ { = 1 }$ .0e-10) Returns the integral of the function or functor func from a to b. The constants EPS can be set to the desired fractional accuracy and JMAX so that 2 to the power JMAX-1 is the maximum allowed number of steps. Integration is performed by the trapezoidal rule.

const Int JMAX $= 2 0$ ;   
Doub s,olds $= 0 . 0$ ; Initial value of olds is arbitrary.   
Trapzd<T> t(func,a,b);   
for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<JMAX; ${ \mathrm { j } } + + { \mathrm { j } }$ ) { $\mathtt { s } \mathtt { = } \mathtt { t }$ .next(); if (j > 5) Avoid spurious early convergence. if (abs(s-olds) $<$ eps\*abs(olds) $\mathrm { ~ \bf ~ s ~ } = = \mathrm { ~ \bf ~ 0 . 0 ~ }$ && olds $\scriptstyle = = \ 0 . 0 )$ ) return s; olds=s;   
}   
throw("Too many steps in routine qtrap");

The optional argument eps sets the desired fractional accuracy. Unsophisticated as it is, routine qtrap is in fact a fairly robust way of doing integrals of functions that are not very smooth. Increased sophistication will usually translate into a higher-order method whose efficiency will be greater only for sufficiently smooth integrands. qtrap is the method of choice, e.g., for an integrand that is a function of a variable that is linearly interpolated between measured data points. Be sure that you do not require too stringent an eps, however: If qtrap takes too many steps in trying to achieve your required accuracy, accumulated roundoff errors may start increasing, and the routine may never converge. A value of $1 0 ^ { - 1 0 }$ or even smaller is usually no problem in double precision when the convergence is moderately rapid, but not otherwise. (Of course, very few problems really require such precision.)

We come now to the “deep” fact about the extended trapezoidal rule, equation (4.1.11). It is this: The error of the approximation, which begins with a term of order $1 / N ^ { 2 }$ , is in fact entirely even when expressed in powers of $1 / N$ . This follows directly from the Euler-Maclaurin summation formula,

$$
\begin{array} { l } { \displaystyle \int _ { x _ { 0 } } ^ { x _ { N - 1 } } f ( x ) d x = h \bigg [ \frac { 1 } { 2 } f _ { 0 } + f _ { 1 } + f _ { 2 } + \cdots + f _ { N - 2 } + \frac { 1 } { 2 } f _ { N - 1 } \bigg ] } \\ { \displaystyle \qquad - \frac { B _ { 2 } h ^ { 2 } } { 2 ! } ( f _ { N - 1 } ^ { \prime } - f _ { 0 } ^ { \prime } ) - \cdots - \frac { B _ { 2 k } h ^ { 2 k } } { ( 2 k ) ! } ( f _ { N - 1 } ^ { ( 2 k - 1 ) } - f _ { 0 } ^ { ( 2 k - 1 ) } ) - \cdots } \end{array}
$$

Here $B _ { 2 k }$ is a Bernoulli number, defined by the generating function

$$
{ \frac { t } { e ^ { t } - 1 } } = \sum _ { n = 0 } ^ { \infty } B _ { n } { \frac { t ^ { n } } { n ! } }
$$

with the first few even values (odd values vanish except for $B _ { 1 } = - 1 / 2$ )

$$
B _ { 0 } = 1 B _ { 2 } = \frac { 1 } { 6 } B _ { 4 } = - \frac { 1 } { 3 0 } B _ { 6 } = \frac { 1 } { 4 2 }
$$

$$
B _ { 8 } = - { \frac { 1 } { 3 0 } } \quad B _ { 1 0 } = { \frac { 5 } { 6 6 } } \quad B _ { 1 2 } = - { \frac { 6 9 1 } { 2 7 3 0 } }
$$

Equation (4.2.1) is not a convergent expansion, but rather only an asymptotic expansion whose error when truncated at any point is always less than twice the magnitude

of the first neglected term. The reason that it is not convergent is that the Bernoulli numbers become very large, e.g.,

$$
B _ { 5 0 } = { \frac { 4 9 5 0 5 7 2 0 5 2 4 1 0 7 9 6 4 8 2 1 2 4 7 7 5 2 5 } { 6 6 } }
$$

The key point is that only even powers of $h$ occur in the error series of (4.2.1). This fact is not, in general, shared by the higher-order quadrature rules in $\ S 4 . 1$ . For example, equation (4.1.12) has an error series beginning with ${ \cal O } ( 1 / N ^ { 3 } )$ , but continuing with all subsequent powers of $N \colon 1 / N ^ { 4 }$ , $1 / N ^ { 5 }$ , etc.

Suppose we evaluate (4.1.11) with $N$ steps, getting a result $S _ { N }$ , and then again with $2 N$ steps, getting a result $S _ { 2 N }$ . (This is done by any two consecutive calls of Trapzd.) The leading error term in the second evaluation will be 1/4 the size of the error in the first evaluation. Therefore the combination

$$
\begin{array} { r } { S = \frac { 4 } { 3 } S _ { 2 N } - \frac { 1 } { 3 } S _ { N } } \end{array}
$$

will cancel out the leading order error term. But there is no error term of order $1 / N ^ { 3 }$ , by (4.2.1). The surviving error is of order $1 / N ^ { 4 }$ , the same as Simpson’s rule. In fact, it should not take long for you to see that (4.2.4) is exactly Simpson’s rule (4.1.13), alternating 2/3’s, 4/3’s, and all. This is the preferred method for evaluating that rule, and we can write it as a routine exactly analogous to qtrap above:

# template<class T>

Doub qsimp(T &func, const Doub a, const Doub b, const Doub eps $^ { = 1 }$ .0e-10) Returns the integral of the function or functor func from a to b. The constants EPS can be set to the desired fractional accuracy and JMAX so that 2 to the power JMAX-1 is the maximum allowed number of steps. Integration is performed by Simpson’s rule.

const Int JMAX $= 2 0$ ;   
Doub s,st,ost ${ = } 0$ .0,os ${ = } 0$ .0;   
Trapzd<T> t(func,a,b);   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<JMAX;j++) { st=t.next(); $\mathrm { { s } = }$ (4.0\*st-ost)/3.0; Compare equation (4.2.4), above. if (j > 5) Avoid spurious early convergence. if (abs(s-os) $<$ eps\*abs(os) ( $\mathrm { ~  ~ s ~ } = = \mathrm { ~  ~ 0 ~ } . 0$ && os $\scriptstyle \ = = \ 0 . 0 )$ ) return s; $\mathtt { o s } { = } \mathtt { s }$ ; ost=st;   
}   
throw("Too many steps in routine qsimp");

The routine qsimp will in general be more efficient than qtrap (i.e., require fewer function evaluations) when the function to be integrated has a finite fourth derivative (i.e., a continuous third derivative). The combination of qsimp and its necessary workhorse Trapzd is a good one for light-duty work.

# CITED REFERENCES AND FURTHER READING:

Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 3 . 1$ .   
Dahlquist, G., and Bjorck, A. 1974, Numerical Methods (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2003 (New York: Dover), $\ S 7 . 4 . 1 - \ S 7 . 4 . 2$ .   
Forsythe, G.E., Malcolm, M.A., and Moler, C.B. 1977, Computer Methods for Mathematical Computations (Englewood Cliffs, NJ: Prentice-Hall), $\ S 5 . 3$ .

# 4.3 Romberg Integration

We can view Romberg’s method as the natural generalization of the routine qsimp in the last section to integration schemes that are of higher order than Simpson’s rule. The basic idea is to use the results from $k$ successive refinements of the extended trapezoidal rule (implemented in trapzd) to remove all terms in the error series up to but not including $O ( 1 / N ^ { 2 k } )$ . The routine qsimp is the case of $k = 2$ . This is one example of a very general idea that goes by the name of Richardson’s deferred approach to the limit: Perform some numerical algorithm for various values of a parameter $h$ , and then extrapolate the result to the continuum limit $h = 0$ .

Equation (4.2.4), which subtracts off the leading error term, is a special case of polynomial extrapolation. In the more general Romberg case, we can use Neville’s algorithm (see $\ S 3 . 2 )$ to extrapolate the successive refinements to zero stepsize. Neville’s algorithm can in fact be coded very concisely within a Romberg integration routine. For clarity of the program, however, it seems better to do the extrapolation by a function call to Poly_interp::rawinterp, as given in $\ S 3 . 2$ .

# template <class T>

Doub qromb(T &func, Doub a, Doub b, const Doub eps $\ L = 1$ .0e-10) {   
Returns the integral of the function or functor func from a to b. Integration is performed by   
Romberg’s method of order 2K, where, e.g., $\mathtt { K } = 2$ is Simpson’s rule. const Int JMAX $= 2 0$ , JMAXP $\nu =$ JMAX $+ 1$ , $\mathtt { K } mathtt { = } 5$ ; Here EPS is the fractional accuracy desired, as determined by the extrapolation error estimate; JMAX limits the total number of steps; K is the number of points used in the extrapolation. VecDoub s(JMAX),h(JMAXP); These store the successive trapezoidal approxi-Poly_interp polint(h,s,K); mations and their relative stepsizes. h[0] $= 1$ .0; Trapzd<T> t(func,a,b); for (Int $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j $< =$ JMAX;j++) s[j-1] $\mathtt { \Omega } = \mathtt { t }$ .next(); if (j >= K) { Doub ss=polint.rawinterp(j-K,0.0); if (abs(polint.dy) $< =$ eps\*abs(ss)) return ss; } h[j] $] = 0 \cdot 2 !$ 5\*h[j-1]; This is a key step: The factor is 0.25 even though the stepsize is decreased by only 0.5. This makes the extrapolation a polynomial in $h ^ { 2 }$ as allowed by equation (4.2.1), not just a polynomial in $h$ . } throw("Too many steps in routine qromb");

The routine qromb is quite powerful for sufficiently smooth (e.g., analytic) integrands, integrated over intervals that contain no singularities, and where the endpoints are also nonsingular. qromb, in such circumstances, takes many, many fewer function evaluations than either of the routines in $\ S 4 . 2$ . For example, the integral

$$
\int _ { 0 } ^ { 2 } x ^ { 4 } \log ( x + \sqrt { x ^ { 2 } + 1 } ) d x
$$

converges (with parameters as shown above) on the second extrapolation, after just 6 calls to trapzd, while qsimp requires 11 calls (32 times as many evaluations of the integrand) and qtrap requires 19 calls (8192 times as many evaluations of the integrand).

# CITED REFERENCES AND FURTHER READING:

Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 3 . 4 - \ S 3 . 5$ .

Dahlquist, G., and Bjorck, A. 1974, Numerical Methods (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2003 (New York: Dover), $\ S 7 . 4 . 1 - \ S 7 . 4 . 2$ .

Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), $\ S 4 . 1 0 { - } 2$ .

# 4.4 Improper Integrals

For our present purposes, an integral will be “improper” if it has any of the following problems:

- its integrand goes to a finite limiting value at finite upper and lower limits, but cannot be evaluated right on one of those limits (e.g., $\sin x / x$ at $x = 0$ )   
- its upper limit is $\infty$ , or its lower limit is $- \infty$   
$\bullet$ it has an integrable singularity at either limit (e.g., $x ^ { - 1 / 2 }$ at $x = 0$ )   
$\bullet$ it has an integrable singularity at a known place between its upper and lower limits   
- it has an integrable singularity at an unknown place between its upper and lower limits

(e.g., If an integral is infinite (e.g., $\textstyle \int _ { - \infty } ^ { \infty } \cos x d x )$ 1 , we do not call it improper; we call it impossible. No amount of $\textstyle { \int _ { 1 } ^ { \infty } x ^ { - 1 } d x ) }$ , or does not exist in a limiting sense clever algorithmics will return a meaningful answer to an ill-posed problem.

In this section we will generalize the techniques of the preceding two sections to cover the first four problems on the above list. A more advanced discussion of quadrature with integrable singularities occurs in Chapter 19, notably $\ S 1 9 . 3$ . The fifth problem, singularity at an unknown location, can really only be handled by the use of a variable stepsize differential equation integration routine, as will be given in Chapter 17, or an adaptive quadrature routine such as in $\ S 4 . 7$ .

We need a workhorse like the extended trapezoidal rule (equation 4.1.11), but one that is an open formula in the sense of $\ S 4 . 1$ , i.e., does not require the integrand to be evaluated at the endpoints. Equation (4.1.19), the extended midpoint rule, is the best choice. The reason is that (4.1.19) shares with (4.1.11) the “deep” property of having an error series that is entirely even in $h$ . Indeed there is a formula, not as well known as it ought to be, called the Second Euler-Maclaurin summation formula,

$$
\begin{array} { l } { \displaystyle \int _ { x _ { 0 } } ^ { x _ { N - 1 } } f ( x ) d x = h [ f _ { 1 / 2 } + f _ { 3 / 2 } + f _ { 5 / 2 } + \cdots + f _ { N - 5 / 2 } + f _ { N - 3 / 2 } ] } \\ { + \frac { B _ { 2 } h ^ { 2 } } { 4 } ( f _ { N - 1 } ^ { \prime } - f _ { 0 } ^ { \prime } ) + \cdots } \\ { + \frac { B _ { 2 k } h ^ { 2 k } } { ( 2 k ) ! } ( 1 - 2 ^ { - 2 k + 1 } ) ( f _ { N - 1 } ^ { ( 2 k - 1 ) } - f _ { 0 } ^ { ( 2 k - 1 ) } ) + \cdots } \end{array}
$$

This equation can be derived by writing out (4.2.1) with stepsize $h$ , then writing it out again with stepsize $h / 2$ , and then subtracting the first from twice the second.

It is not possible to double the number of steps in the extended midpoint rule and still have the benefit of previous function evaluations (try it!). However, it is possible to triple the number of steps and do so. Shall we do this, or double and accept the loss? On the average, tripling does a factor $\sqrt { 3 }$ of unnecessary work, since the “right” number of steps for a desired accuracy criterion may in fact fall anywhere in the logarithmic interval implied by tripling. For doubling, the factor is only $\sqrt { 2 }$ , but we lose an extra factor of 2 in being unable to use all the previous evaluations. Since $1 . 7 3 2 < 2 \times 1 . 4 1 4$ , it is better to triple.

Here is the resulting structure, which is directly comparable to Trapzd.

template <class T>   
struct Midpnt : Quadrature {   
Routine implementing the extended midpoint rule. Doub a,b,s; Limits of integration and current value of inte-T &funk; gral. Midpnt(T &funcc, const Doub aa, const Doub bb) : funk(funcc), a(aa), b(bb) $\{ \mathbf { n } { = } 0 ; \}$ The constructor takes as inputs func, the function or functor to be integrated between limits a and b, also input. Doub next(){ Returns the nth stage of refinement of the extended midpoint rule. On the first call $\scriptstyle ( \mathtt { n } = 1$ ), the routine returns the crudest estimate of $\textstyle \int _ { a } ^ { b } f ( x ) d x$ . Subsequent calls set $\scriptstyle \mathtt { n = 2 } , 3 , \dotsc$ . and improve the accuracy by adding $( 2 / 3 ) \times 3 ^ { \mathrm { n - 1 } }$ additional interior points. Int it,j; Doub x,tnm,sum,del,ddel; $\mathbf { n } { + } +$ ; if $\mathbf { \Omega } ( \mathbf { n _ { \alpha } } = \mathbf { \Omega } 1 \mathbf { \Omega } )$ ) { return (s=(b-a)\*func(0.5\*(a+b))); } else { for(it=1,j=1;j<n-1;j++) it \*= 3; tnm=it; del $=$ (b-a)/(3.0\*tnm); ddel=del+del; The added points alternate in spacing bex=a+0.5\*del; tween del and ddel. sum $_ { = 0 }$ .0; for (j ${ = } 0$ ;j<it;j++) { sum $+ =$ func(x); $\mathrm { ~ \texttt ~ { ~ x ~ } ~ } + =$ ddel; sum $+ =$ func(x); x $+ =$ del; $\mathrm { s } =$ (s+(b-a)\*sum/tnm)/3.0; The new sum is combined with the old intereturn s; gral to give a refined integral. } virtual Doub func(const Doub x) {return funk(x);} Identity mapping.   
};

You may have spotted a seemingly unnecessary extra level of indirection in Midpnt, namely its calling the user-supplied function funk through an identity function func. The reason for this is that we are going to use mappings other than the identity mapping between funk and func to solve the problems of improper integrals listed above. The new quadratures will simply be derived from Midpnt with func overridden.

The structure Midpnt could be used to exactly replace Trapzd in a driver routine like qtrap (-4.2); one could simply change Trapzd<T> t(func,a,b) to Midpnt<T> t(func,a,b), and perhaps also decrease the parameter JMAX since

$3 ^ { \mathrm { J M A X - 1 } }$ (from step tripling) is a much larger number than $2 ^ { \operatorname { J M A X - 1 } }$ (step doubling). The open formula implementation analogous to Simpson’s rule (qsimp in $\ S 4 . 2 )$ could also substitute Midpnt for Trapzd, decreasing JMAX as above, but now also changing the extrapolation step to be

$$
\mathbf { s } { = } \left( 9 . 0 { * } \mathbf { s } { \mathrm { t } } { - } { \circ } \mathbf { s } { \mathrm { t } } \right) / 8 . 0 ;
$$

since, when the number of steps is tripled, the error decreases to $1 / 9 \mathrm { t h }$ its size, not $1 / 4 \mathrm { t h }$ as with step doubling.

Either the thus modified qtrap or qsimp will fix the first problem on the list at the beginning of this section. More sophisticated, and allowing us to fix more problems, is to generalize Romberg integration in like manner:

# template<class T>

# Doub qromo(Midpnt<T> &q, const Doub eps $^ { - 3 }$ .0e-9) {

Romberg integration on an open interval. Returns the integral of a function using any specified elementary quadrature algorithm q and Romberg’s method. Normally q will be an open formula, not evaluating the function at the endpoints. It is assumed that q triples the number of steps on each call, and that its error series contains only even powers of the number of steps. The routines midpnt, midinf, midsql, midsqu, midexp are possible choices for q. The constants below have the same meanings as in qromb.

const Int JMAX 14, JMAXP $^ { 1 } =$ JMAX+1, $\mathtt { K } = 5$ ;   
VecDoub h(JMAXP),s(JMAX);   
Poly_interp polint(h,s,K);   
h[0] $^ { = 1 }$ .0;   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<=JMAX;j++) { s[j-1]=q.next(); if ( $\mathrm { ~ j ~ } > = \mathrm { ~ K ~ }$ { Doub ss=polint.rawinterp(j-K,0.0); if (abs(polint.dy) $< =$ eps\*abs(ss)) return ss; } h[j] $\mathbf { \tau } = \mathbf { h }$ [j-1]/9.0; This is where the assumption of step tripling and an even   
} error series is used.   
throw("Too many steps in routine qromo");

# }

Notice that we now pass a Midpnt object instead of the user function and limits of integration. There is a good reason for this, as we will see below. It does, however, mean that you have to bind things together before calling qromo, something like this, where we integrate from a to b:

Midpnt<Ftor> q(ftor,a,b);   
Doub integral=qromo(q);

or, for a bare function,

Midpnt<Doub(Doub)> q(fbare,a,b);   
Doub integral $=$ qromo(q);

Laid back $\mathrm { C } { + } { + }$ compilers will let you condense these to

Doub integral $=$ qromo(Midpnt<Ftor>(Ftor(),a,b));

or

# Doub integral $=$ qromo(Midpnt<Doub(Doub)>(fbare,a,b));

but uptight compilers may object to the way that a temporary is passed by reference, in which case use the two-line forms above.

As we shall now see, the function qromo, with its peculiar interface, is an excellent driver routine for solving all the other problems of improper integrals in our first list (except the intractable fifth).

The basic trick for improper integrals is to make a change of variables to eliminate the singularity or to map an infinite range of integration to a finite one. For example, the identity

$$
\int _ { a } ^ { b } f ( x ) d x = \int _ { 1 / b } ^ { 1 / a } { \frac { 1 } { t ^ { 2 } } } f \left( { \frac { 1 } { t } } \right) d t \qquad a b > 0
$$

can be used with either $b  \infty$ and $a$ positive, $o r$ with $a  - \infty$ and $b$ negative, and works for any function that decreases toward infinity faster than $1 / x ^ { 2 }$ .

You can make the change of variable implied by (4.4.2) either analytically and then use, e.g., qromo and Midpnt to do the numerical evaluation, or you can let the numerical algorithm make the change of variable for you. We prefer the latter method as being more transparent to the user. To implement equation (4.4.2) we simply write a modified version of Midpnt, called Midinf, which allows $b$ to be infinite (or, more precisely, a very large number on your particular machine, such as $1 \times 1 0 ^ { 9 9 }$ ), or $a$ to be negative and infinite. Since all the machinery is already in place in Midpnt, we write Midinf as a derived class and simply override the mapping function.

# template <class T>

# struct Midinf : Midpnt<T>{

This routine is an exact replacement for midpnt, i.e., returns the nth stage of refinement of the integral of funcc from aa to bb, except that the function is evaluated at evenly spaced points in $1 / x$ rather than in $x$ . This allows the upper limit bb to be as large and positive as the computer allows, or the lower limit aa to be as large and negative, but not both. aa and bb must have the same sign.

Doub func(const Doub x) { return Midpnt<T>::funk(1.0/x)/(x\*x); Effect the change of variable. } Midinf(T &funcc, const Doub aa, const Doub bb) Midpnt $< \mathrm { T } >$ (funcc, aa, bb) { Midpnt<T>:: $\mathtt { a } = 1$ .0/bb; Set the limits of integration. Midpnt<T>::b $^ { * 1 }$ .0/aa; } };

An integral from 2 to $\infty$ , for example, might be calculated by

Midinf<Ftor> q(ftor,2.,1.e99);   
Doub integral=qromo(q);

If you need to integrate from a negative lower limit to positive infinity, you do this by breaking the integral into two pieces at some positive value, for example,

Midpnt<Ftor> q1(ftor,-5.,2.);  
Midinf<Ftor> q2(ftor,2.,1.e99);  
integral $\cdot ^ { = }$ qromo(q1)+qromo(q2);

Where should you choose the breakpoint? At a sufficiently large positive value so that the function funk is at least beginning to approach its asymptotic decrease to zero value at infinity. The polynomial extrapolation implicit in the second call to qromo deals with a polynomial in $1 / x$ , not in $x$ .

To deal with an integral that has an integrable power-law singularity at its lower limit, one also makes a change of variable. If the integrand diverges as $( x - a ) ^ { - \gamma }$ , $0 \leq \gamma < 1$ , near $x = a$ , use the identity

$$
\int _ { a } ^ { b } f ( x ) d x = { \frac { 1 } { 1 - \gamma } } \int _ { 0 } ^ { ( b - a ) ^ { 1 - \gamma } } t ^ { { \frac { \gamma } { 1 - \gamma } } } f ( t ^ { \frac { 1 } { 1 - \gamma } } + a ) d t \qquad ( b > a )
$$

If the singularity is at the upper limit, use the identity

$$
\int _ { a } ^ { b } f ( x ) d x = { \frac { 1 } { 1 - \gamma } } \int _ { 0 } ^ { ( b - a ) ^ { 1 - \gamma } } t ^ { { \frac { \gamma } { 1 - \gamma } } } f ( b - t ^ { \frac { 1 } { 1 - \gamma } } ) d t \qquad ( b > a )
$$

If there is a singularity at both limits, divide the integral at an interior breakpoint as in the example above.

Equations (4.4.3) and (4.4.4) are particularly simple in the case of inverse squareroot singularities, a case that occurs frequently in practice:

$$
\int _ { a } ^ { b } f ( x ) d x = \int _ { 0 } ^ { \sqrt { b - a } } 2 t f ( a + t ^ { 2 } ) d t \qquad ( b > a )
$$

for a singularity at $a$ , and

$$
\int _ { a } ^ { b } f ( x ) d x = \int _ { 0 } ^ { \sqrt { b - a } } 2 t f ( b - t ^ { 2 } ) d t \qquad ( b > a )
$$

for a singularity at $b$ . Once again, we can implement these changes of variable transparently to the user by defining substitute routines for Midpnt that make the change of variable automatically:

template <class $\mathrm { T } >$   
struct Midsql : Midpnt<T>{   
This routine is an exact replacement for midpnt, except that it allows for an inverse square-root singularity in the integrand at the lower limit aa.

Doub aorig; Doub func(const Doub x) { return 2.0\*x\*Midpnt<T>::funk(aorig+x\*x); Effect the change of variable. Midsql(T &funcc, const Doub aa, const Doub bb) : Midpnt<T>(funcc, aa, bb), aorig(aa) Midpnt<T>:: $\mathtt { a } = 0$ ; Midpnt<T>::b sqrt(bb-aa); } };

# quadrature.h

Similarly,

template <class T>   
struct Midsqu : Midpnt<T>{   
This routine is an exact replacement for midpnt, except that it allows for an inverse square-root singularity in the integrand at the upper limit bb.

Doub borig; Doub func(const Doub x) { return 2.0\*x\*Midpnt<T>::funk(borig-x\*x); Effect the change of variable. Midsqu(T &funcc, const Doub aa, const Doub bb) : Midpnt<T>(funcc, aa, bb), borig(bb) { Midpnt<T>:: $\mathtt { a } = 0$ ; Midpnt<T>::b=sqrt(bb-aa); } };

One last example should suffice to show how these formulas are derived in general. Suppose the upper limit of integration is infinite and the integrand falls off exponentially. Then we want a change of variable that maps $e ^ { - x } d x$ into $( \pm ) d t$ (with the sign chosen to keep the upper limit of the new variable larger than the lower limit). Doing the integration gives by inspection

$$
t = e ^ { - x } \qquad { \mathrm { o r } } \qquad x = - \log t
$$

so that

$$
\int _ { x = a } ^ { x = \infty } f ( x ) d x = \int _ { t = 0 } ^ { t = e ^ { - a } } f ( - \log t ) { \frac { d t } { t } }
$$

The user-transparent implementation would be

# template <class T>

struct Midexp : Midpnt<T>{

This routine is an exact replacement for midpnt, except that bb is assumed to be infinite (value passed not actually used). It is assumed that the function funk decreases exponentially rapidly at infinity.

Doub func(const Doub x) { return Midpnt<T>::funk(-log(x))/x; Effect the change of variable. Midexp(T &funcc, const Doub aa, const Doub bb) Midpnt<T>(funcc, aa, bb) { Midpnt<T>:: $\mathtt { a } = 0$ .0; Midpnt<T>::b $=$ exp(-aa); } };

# CITED REFERENCES AND FURTHER READING:

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), Chapter 4.   
Dahlquist, G., and Bjorck, A. 1974, Numerical Methods (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2003 (New York: Dover), $\ S 7 . 4 . 3$ , p. 294.   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 3 . 7$ .

# 4.5 Quadrature by Variable Transformation

Imagine a simple general quadrature algorithm that is very rapidly convergent and allows you to ignore endpoint singularities completely. Sound too good to be true? In this section we’ll describe an algorithm that in fact handles large classes of integrals in exactly this way.

Consider evaluating the integral

$$
I = \int _ { a } ^ { b } f ( x ) d x
$$

As we saw in the construction of equations $( 4 . 1 . 1 1 ) - ( 4 . 1 . 2 0 )$ , quadrature formulas of arbitrarily high order can be constructed with interior weights unity, just by tuning the weights near the endpoints. But if a function dies off rapidly enough near the endpoints, then those weights don’t matter at all. In such a case, an $N$ -point quadrature with uniform weights converges converges exponentially with $N$ . (For a more rigorous motivation of this idea, see $\ S 4 . 5 . 1$ . For the connection to Gaussian quadrature, see the discussion at the end of $\ S 2 0 . 7 . 4 . )$

What about a function that doesn’t vanish at the endpoints? Consider a change of variables $x = x ( t )$ , such that $x \in [ a , b ] \to t \in [ c , d ]$ :

$$
I = \int _ { c } ^ { d } f [ x ( t ) ] { \frac { d x } { d t } } d t
$$

Choose the transformation such that the factor $d x / d t$ goes rapidly to zero at the endpoints of the interval. Then the simple trapezoidal rule applied to (4.5.2) will give extremely accurate results. (In this section, we’ll call quadrature with uniform weights trapezoidal quadrature, with the understanding that it’s a matter of taste whether you weight the endpoints with weight $1 / 2$ or 1, since they don’t count anyway.)

Even when $f ( x )$ has integrable singularities at the endpoints of the interval, their effect can be overwhelmed by a suitable transformation $x = x ( t )$ . One need not tailor the transformation to the specific nature of the singularity: We will discuss several transformations that are effective at obliterating just about any kind of endpoint singularity.

The first transformation of this kind was introduced by Schwartz [1] and has become known as the TANH rule:

$$
\begin{array} { r l } & { \quad x = \displaystyle \frac { 1 } { 2 } ( b + a ) + \frac { 1 } { 2 } ( b - a ) \operatorname { t a n h } t , \qquad x \in [ a , b ] \to t \in [ - \infty , \infty ] } \\ & { \displaystyle \frac { d x } { d t } = \frac { 1 } { 2 } ( b - a ) \operatorname { s e c h } ^ { 2 } t = \frac { 2 } { b - a } ( b - x ) ( x - a ) } \end{array}
$$

The sharp decrease of $\operatorname { s e c h } ^ { 2 } t$ as $t  \pm \infty$ explains the efficiency of the algorithm and its ability to deal with singularities. Another similar algorithm is the IMT rule [2]. However, $x ( t )$ for the IMT rule is not given by a simple analytic expression, and its performance is not too different from the TANH rule.

There are two kinds of errors to consider when using something like the TANH rule. The discretization error is just the truncation error because you are using the trapezoidal rule to approximate $I$ . The trimming error is the result of truncating the infinite sum in the trapezoidal rule at a finite value of $N$ . (Recall that the limits are now $\pm \infty$ .) You might think that the sharper the decrease of $d x / d t$ as $t $ $\pm \infty$ , the more efficient the algorithm. But if the decrease is too sharp, then the density of quadrature points near the center of the original interval $[ a , b ]$ is low and the discretization error is large. The optimal strategy is to try to arrange that the discretization and trimming errors are approximately equal.

For the TANH rule, Schwartz [1] showed that the discretization error is of order

$$
\epsilon _ { d } \sim e ^ { - 2 \pi w / h }
$$

where $w$ is the distance from the real axis to the nearest singularity of the integrand. There is a pole when $\operatorname { s e c h } ^ { 2 } t \to \infty$ , i.e., when $t = \pm i \pi / 2$ . If there are no poles closer to the real axis in $f ( x )$ , then $w = \pi / 2$ . The trimming error, on the other hand, is

$$
\epsilon _ { t } \sim \mathrm { s e c h } ^ { 2 } t _ { N } \sim e ^ { - 2 N h }
$$

Setting $\epsilon _ { d } \sim \epsilon _ { t }$ , we find

$$
h \sim \frac { \pi } { ( 2 N ) ^ { 1 / 2 } } , \qquad \epsilon \sim e ^ { - \pi ( 2 N ) ^ { 1 / 2 } }
$$

as the optimum $h$ and the corresponding error. Note that $\epsilon$ decreases with $N$ faster than any power of $N$ . If $f$ is singular at the endpoints, this can modify equation (4.5.5) for $\epsilon _ { t }$ . This usually results in the constant $\pi$ in (4.5.6) being reduced. Rather than developing an algorithm where we try to estimate the optimal $h$ for each integrand a priori, we recommend simple step doubling and testing for convergence. We expect convergence to set in for $h$ around the value given by equation (4.5.6).

The TANH rule essentially uses an exponential mapping to achieve the desired rapid fall-off at infinity. On the theory that more is better, one can try repeating the procedure. This leads to the DE (double exponential) rule:

$$
\begin{array} { c } { { x = \displaystyle \frac 1 2 ( b + a ) + \frac 1 2 ( b - a ) \operatorname { t a n h } ( c \sinh t ) , x \in [ a , b ] \to t \in [ - \infty , \infty ] } } \\ { { \displaystyle \frac { d x } { d t } = \frac 1 2 ( b - a ) \operatorname { s e c h } ^ { 2 } ( c \sinh t ) c \cosh t \sim \exp ( - c \exp | t | ) \quad \mathrm { a s } \quad | t | \to \infty } } \end{array}
$$

Here the constant $c$ is usually taken to be 1 or $\pi / 2$ . (Values larger than $\pi / 2$ are not useful since $w = \pi / 2$ for $0 < c \leq \pi / 2$ , but $w$ decreases rapidly for larger $c$ .) By an analysis similar to equations (4.5.4) – (4.5.6), one can show that the optimal $h$ and corresponding error for the DE rule are of order

$$
h \sim \frac { \log ( 2 \pi N w / c ) } { N } , \qquad \epsilon \sim e ^ { - k N / \log N }
$$

where $k$ is a constant. The improved performance of the DE rule over the TANH rule indicated by comparing equations (4.5.6) and (4.5.8) is borne out in practice.

# 4.5.1 Exponential Convergence of the Trapezoidal Rule

The error in evaluating the integral (4.5.1) by the trapezoidal rule is given by the Euler-Maclaurin summation formula,

$$
I \approx \frac { h } { 2 } [ f ( a ) + f ( b ) ] + h \sum _ { j = 1 } ^ { N - 1 } f ( a + j h ) - \sum _ { k = 1 } ^ { \infty } \frac { B _ { 2 k } h ^ { 2 k } } { ( 2 k ) ! } [ f ^ { ( 2 k - 1 ) } ( b ) - f ^ { ( 2 k - 1 ) } ( a ) ]
$$

Note that this is in general an asymptotic expansion, not a convergent series. If all the derivatives of the function $f$ vanish at the endpoints, then all the “correction terms” in equation (4.5.9) are zero. The error in this case is very small — it goes to zero with $h$ faster than any power of $h$ . We say that the method converges exponentially. The straight trapezoidal rule is thus an excellent method for integrating functions such as $\exp ( - x ^ { 2 } )$ on $( - \infty , \infty )$ , whose derivatives all vanish at the endpoints.

The class of transformations that will produce exponential convergence for a function whose derivatives do not all vanish at the endpoints is those for which $d x / d t$ and all its derivatives go to zero at the endpoints of the interval. For functions with singularities at the endpoints, we require that $f ( x ) d x / d t$ and all its derivatives vanish at the endpoints. This is a more precise statement of $\mathbf { \ddot { \psi } } d x / d t$ goes rapidly to zero” given above.

# 4.5.2 Implementation

Implementing the DE rule is a little tricky. It’s not a good idea to simply use Trapzd on the function $f ( x ) d x / d t$ . First, the factor $\operatorname { s e c h } ^ { 2 } ( c \sinh t )$ in equation (4.5.7) can overflow if sech is computed as $1 /$ cosh. We follow [3] and avoid this by using the variable $q$ defined by

$$
q = e ^ { - 2 \sinh t }
$$

(we take $c = 1$ for simplicity) so that

$$
\frac { d x } { d t } = 2 ( b - a ) \frac { q } { ( 1 + q ) ^ { 2 } } \cosh t
$$

For large positive $t , q$ just underflows harmlessly to zero. Negative $t$ is handled by using the symmetry of the trapezoidal rule about the midpoint of the interval. We write

$$
\begin{array} { l } { { I \simeq h \sum _ { j = - N } ^ { N } f ( x _ { j } )  \frac { d x } { d t } | _ { j } } } \\ { { \displaystyle = h \bigg \lbrace  f [ ( a + b ) / 2 ]  \frac { d x } { d t } | _ { 0 } + \sum _ { j = 1 } ^ { N } [ f ( a + \delta _ { j } ) + f ( b - \delta _ { j } ) ]  \frac { d x } { d t } | _ { j } \bigg \rbrace } } \end{array}
$$

where

$$
\delta = b - x = ( b - a ) \frac { q } { 1 + q }
$$

A second possible problem is that cancellation errors in computing $a + \delta$ or $b - \delta$ can cause the computed value of $f ( x )$ to blow up near the endpoint singularities. To handle this, you should code the function $f ( x )$ as a function of two arguments, $f ( x , \delta )$ . Then compute the singular part using $\delta$ directly. For example, code the function $x ^ { - \alpha } ( 1 - x ) ^ { - \beta }$ as $\delta ^ { - \alpha } ( 1 - x ) ^ { - \beta }$ near $x = 0$ and $\dot { x } ^ { - \alpha } \delta ^ { - \beta }$ near $x = 1$ . (See $\ S 6 . 1 0$ for another example of a $f ( x , \delta )$ .) Accordingly, the routine DErule below expects the function $f$ to have two arguments. If your function has no singularities, or the singularities are “mild” (e.g., no worse than logarithmic), you can ignore $\delta$ when coding $f ( x , \delta )$ and code it as if it were just $f ( x )$ .

The routine DErule implements equation (4.5.12). It contains an argument $h _ { \mathrm { m a x } }$ that corresponds to the upper limit for $t$ . The first approximation to $I$ is given by the first term on the right-hand side of (4.5.12) with $h = h _ { \operatorname* { m a x } }$ . Subsequent refinements correspond to halving $h$ as usual. We typically take $h _ { \mathrm { m a x } } = 3 . 7$ in double precision, corresponding to $q = 3 \times 1 0 ^ { - 1 8 }$ . This is generally adequate for “mild” singularities, like logarithms. If you want high accuracy for stronger singularities, you may have to increase $h _ { \mathrm { m a x } }$ . For example, for $1 / { \sqrt { x } }$ you need $h _ { \mathrm { m a x } } = 4 . 3$ to get full double precision. This corresponds to $q = 1 0 ^ { - 3 2 } = ( 1 0 ^ { - 1 6 } ) ^ { 2 }$ , as you might expect.

DErule(T &funcc, const Doub aa, const Doub bb, const Doub hmaxx $\scriptstyle = 3$ .7) : func(funcc), a(aa), b(bb), hmax(hmaxx) $\{ \mathrm { n } { = } 0 ; \}$

Constructor. funcc is the function or functor that provides the function to be integrated between limits aa and bb, also input. The function operator in funcc takes two arguments, $x$ and $\delta$ , as described in the text. The range of integration in the transformed variable $t$ is .hmaxx; hmaxx/. Typical values of hmaxx are 3.7 for logarithmic or milder singularities, and 4.3 for square-root singularities, as discussed in the text.

# Doub next() {

On the first call to the function next $( n = 1 )$ ), the routine returns the crudest estimate of $\textstyle \int _ { a } ^ { b } f ( x ) d x$ . Subsequent calls to next $( n = 2 , 3 , \ldots )$ will improve the accuracy by adding $2 ^ { n - 1 }$ additional interior points.

Doub del,fact,q,sum,t,twoh; Int it,j; $\mathrm { n } { + } { + }$ ; if $\mathbf { \Phi } _ { \mathrm { ~ n ~ } } = = \mathbf { \Phi } _ { 1 } )$ ) { fact ${ = } 0$ .25; return s=hmax\*2. $^ { 0 * }$ (b-a)\*fact\*func(0. $^ { 5 * }$ (b+a),0.5\*(b-a)); } else { for ( $\dot { \tt 1 } + = 1$ , $\dot { \mathsf { J } } ^ { = 1 }$ ;j<n-1;j++) it $< < = ~ 1 ;$ twoh=hmax/it; Twice the spacing of the points to be added. $\mathtt { t } = 0$ .5\*twoh; for (sum $_ { = 0 }$ .0,j ${ = } 0$ ;j<it;j++) { q=exp(-2.0\*sinh(t)); del $=$ (b-a)\*q/(1.0+q); fact=q/SQR(1.0+q)\*cosh(t); sum $+ =$ fact\*(func(a+del,del)+func(b-del,del)); t $+ =$ twoh; } return $\mathtt { s } = 0$ .5\*s+(b-a)\*twoh\*sum; Replace s by its refined value and return. } } };

If the double exponential rule (DE rule) is generally better than the single exponential rule (TANH rule), why don’t we keep going and use a triple exponential rule, quadruple exponential rule, . . . ? As we mentioned earlier, the discretization error is dominated by the pole nearest to the real axis. It turns out that beyond the double exponential the poles come nearer and nearer to the real axis, so the methods tend to get worse, not better.

If the function to be integrated itself has a pole near the real axis (much nearer than the $\pi / 2$ that comes from the DE or TANH rules), the convergence of the method slows down. In analytically tractable cases, one can find a “pole correction term” to add to the trapezoidal rule to restore rapid convergence [4].

# 4.5.3 Infinite Ranges

Simple variations of the TANH or DE rules can be used if either or both of the limits of integration is infinite:

<table><tr><td rowspan=1 colspan=1>Range</td><td rowspan=1 colspan=1>TANH Rule</td><td rowspan=1 colspan=1>DE Rule</td><td rowspan=1 colspan=1>Mixed Rule</td></tr><tr><td rowspan=1 colspan=1>（0,00）</td><td rowspan=1 colspan=1>x=et</td><td rowspan=1 colspan=1>x = e2c sinht</td><td rowspan=1 colspan=1>x=et-e-t</td></tr><tr><td rowspan=1 colspan=1>(18,）</td><td rowspan=1 colspan=1>x= sinht</td><td rowspan=1 colspan=1>x = sinh(c sinht)</td><td rowspan=1 colspan=1>1</td></tr></table>

The last column gives a mixed rule for functions that fall off rapidly ( ${ e ^ { - x } }$ or $e ^ { - x ^ { 2 } }$ ) at infinity. It is a DE rule at $x = 0$ but only a single exponential at infinity. The exponential fall-off of the integrand makes it behave like a DE rule there too. The mixed rule for $( - \infty , \infty )$ is constructed by splitting the range into $( - \infty , 0 )$ and $( 0 , \infty )$ and making the substitution $x \ \to \ - x$ in the first range. This gives two integrals on $( 0 , \infty )$ .

To implement the DE rule for infinite ranges we don’t need the precautions we used in coding the finite range DE rule. It’s fine to simply use the routine Trapzd directly as a function of $t$ , with the function func that it calls returning $f ( x ) d x / d t$ . So if funk is your function returning $f ( x )$ , then you define the function func as a function of t by code of the following form (for the mixed rule)

x=exp(t-exp(-t));   
dxdt=x\*(1. $^ { 0 + }$ exp(-t));   
return funk(x)\*dxdt;

and pass func to Trapzd. The only care required is in deciding the range of integration. You want the contribution to the integral from the endpoints of the integration to be negligible. For example, $( - 4 , 4 )$ is typically adequate for $x = \exp ( \pi \sinh t ) $ .

# 4.5.4 Examples

As examples of the power of these methods, consider the following integrals:

$$
\begin{array} { l } { \displaystyle \int _ { 0 } ^ { 1 } \log x \log ( 1 - x ) d x = 2 - \frac { \pi ^ { 2 } } { 6 } } \\ { \displaystyle \int _ { 0 } ^ { \infty } \frac { 1 } { x ^ { 1 / 2 } ( 1 + x ) } d x = \pi } \\ { \displaystyle \int _ { 0 } ^ { \infty } x ^ { - 3 / 2 } \sin \frac { x } { 2 } e ^ { - x } d x = [ \pi ( \sqrt { 5 } - 2 ) ] ^ { 1 / 2 } } \\ { \displaystyle \int _ { 0 } ^ { \infty } x ^ { - 2 / 7 } e ^ { - x ^ { 2 } } d x = \frac { 1 } { 2 } \Gamma ( \frac { 5 } { 1 4 } ) } \end{array}
$$

The integral (4.5.15) is easily handled by DErule. The routine converges to machine precision $( 1 0 ^ { - 1 6 } )$ with about 30 function evaluations, completely unfazed by the singularities at the endpoints. The integral (4.5.16) is an example of an integrand that is singular at the origin and falls off slowly at infinity. The routine Midinf fails miserably because of the slow fall-off. Yet the transformation $x = \exp ( \pi \sinh t ) $ again gives machine precision in about 30 function evaluations, integrating $t$ over the range $( - 4 , 4 )$ . By comparison, the transformation $\boldsymbol { x } ~ = ~ e ^ { t }$ for $t$ in the range $( - 9 0 , 9 0 )$ requires about 500 function evaluations for the same accuracy.

The integral (4.5.17) combines a singularity at the origin with exponential falloff at infinity. Here the “mixed” transformation $x = \exp ( t - e ^ { - t } )$ is best, requiring about 60 function evaluations for $t$ in the range $( - 4 . 5 , 4 )$ . Note that the exponential fall-off is crucial here; these transformations fail completely for slowly decaying oscillatory functions like $x ^ { - 3 / 2 } \sin x$ . Fortunately the series acceleration algorithms of $\ S 5 . 3$ work well in such cases.

The final integral (4.5.18) is similar to (4.5.17), and using the same transformation requires about the same number of function evaluations to achieve machine precision. The range of $t$ can be smaller, say $( - 4 , 3 )$ , because of the more rapid fall-off of the integrand. Note that for all these integrals the number of function evaluations would be double the number we quote if we are using step doubling to decide when the integrals have converged, since we need one extra set of trapezoidal evaluations to confirm convergence. In many cases, however, you don’t need this extra set of function evaluations: Once the method starts converging, the number of significant digits approximately doubles with each iteration. Accordingly, you can set the convergence criterion to stop the procedure when two successive iterations agree to the square root of the desired precision. The last iteration will then have approximately the required precision. Even without this trick, the method is quite remarkable for the range of difficult integrals that it can tame efficiently.

An extended example of the use of the DE rule for finite and infinite ranges is given in $\ S 6 . 1 0$ . There we give a routine for computing the generalized Fermi-Dirac integrals

$$
F _ { k } ( \eta , \theta ) = \int _ { 0 } ^ { \infty } { \frac { x ^ { k } ( 1 + { \frac { 1 } { 2 } } \theta x ) ^ { 1 / 2 } } { e ^ { x - \eta } + 1 } } d x
$$

Another example is given in the routine Stiel in $\ S 4 . 6$ .

# 4.5.5 Relation to the Sampling Theorem

The sinc expansion of a function is

$$
f ( x ) \simeq \sum _ { k = - \infty } ^ { \infty } f ( k h ) \operatorname { s i n c } \left[ { \frac { \pi } { h } } ( x - k h ) \right]
$$

where $\operatorname { s i n c } ( x ) \equiv \sin { x } / { x }$ . The expansion is exact for a limited class of analytic functions. However, it can be a good approximation for other functions too, and the sampling theorem characterizes these functions, as will be discussed in $\ S 1 3 . 1 1$ . There we will use the sinc expansion of $e ^ { - x ^ { 2 } }$ to get an approximation for the complex error function. Functions well-approximated by the sinc expansion typically fall off rapidly as $x  \pm \infty$ , so truncating the expansion at $k = \pm N$ still gives a good approximation to $f ( x )$ .

If we integrate both sides of equation (4.5.20), we find

$$
\int _ { - \infty } ^ { \infty } f ( x ) d x \simeq h \sum _ { k = - \infty } ^ { \infty } f ( k h )
$$

which is just the trapezoidal formula! Thus, rapid convergence of the trapezoidal formula for the integral of $f$ corresponds to $f$ being well-approximated by its sinc expansion. The various transformations described earlier can be used to map $x \to x ( t )$ and produce good sinc approximations with uniform samples in $t$ . These approximations can be used not only for the trapezoidal quadrature of $f$ , but also for good approximations to derivatives, integral transforms, Cauchy principal value integrals, and solving differential and integral equations [5].

# CITED REFERENCES AND FURTHER READING:

Schwartz, C. 1969, “Numerical Integration of Analytic Functions,” Journal of Computational Physics,vol.4,pp.19-29.[1]   
Iri, M., Moriguti, S., and Takasawa, Y. 1987, “On a Certain Quadrature Formula,” Journal of Computational and Applied Mathematics,vol.17,pp.3-20.(English version of Japanese article originally published in 1970.)[2]   
Evans, G.A., Forbes, R.C., and Hyslop, J. 1984, “The Tanh Transformation for Singular Integrals,” International Journal of Computer Mathematics,vol.15, pp.339-358.[3]   
Bialecki, B. 1989, BIT, “A Modified Sinc Quadrature Rule for Functions with Poles near the Arc of Integration,” vol. 29, pp. 464–476.[4]   
Stenger, F. 1981, “Numerical Methods Based on Whittaker Cardinal or Sinc Functions,” SIAM Review,vol.23,pp.165-224.[5]   
Takahasi, H., and Mori, H. 1973, “Quadrature Formulas Obtained by Variable Transformation,” Numerische Mathematik,vol.21,pp.206-219.   
Mori, M. 1985, “Quadrature Formulas Obtained by Variable Transformation and DE Rule,” Journal of Computational and Applied Mathematics, vol.12&13,pp.119-130.   
Sikorski, K., and Stenger, F. 1984, “Optimal Quadratures in $H _ { p }$ Spaces,” ACM Transactions on Mathematical Software,vol. 10, pp. 140-151; op. cit., pp. 152-160.

# 4.6 Gaussian Quadratures and Orthogonal Polynomials

In the formulas of $\ S 4 . 1$ , the integral of a function was approximated by the sum of its functional values at a set of equally spaced points, multiplied by certain aptly chosen weighting coefficients. We saw that as we allowed ourselves more freedom in choosing the coefficients, we could achieve integration formulas of higher and higher order. The idea of Gaussian quadratures is to give ourselves the freedom to choose not only the weighting coefficients, but also the location of the abscissas at which the function is to be evaluated. They will no longer be equally spaced. Thus, we will have twice the number of degrees of freedom at our disposal; it will turn out that we can achieve Gaussian quadrature formulas whose order is, essentially, twice that of the Newton-Cotes formula with the same number of function evaluations.

Does this sound too good to be true? Well, in a sense it is. The catch is a familiar one, which cannot be overemphasized: High order is not the same as high accuracy. High order translates to high accuracy only when the integrand is very smooth, in the sense of being “well-approximated by a polynomial.”

There is, however, one additional feature of Gaussian quadrature formulas that adds to their usefulness: We can arrange the choice of weights and abscissas to make the integral exact for a class of integrands “polynomials times some known function $W ( x ) ^ { \dag }$ rather than for the usual class of integrands “polynomials.” The function $W ( x )$ can then be chosen to remove integrable singularities from the desired integral. Given $W ( x )$ , in other words, and given an integer $N$ , we can find a set of weights $w _ { j }$ and abscissas $x _ { j }$ such that the approximation

$$
\int _ { a } ^ { b } W ( x ) f ( x ) d x \approx \sum _ { j = 0 } ^ { N - 1 } w _ { j } f ( x _ { j } )
$$

is exact if $f ( x )$ is a polynomial. For example, to do the integral

$$
\int _ { - 1 } ^ { 1 } { \frac { \exp ( - \cos ^ { 2 } x ) } { \sqrt { 1 - x ^ { 2 } } } } d x
$$

(not a very natural looking integral, it must be admitted), we might well be interested in a Gaussian quadrature formula based on the choice

$$
W ( x ) = { \frac { 1 } { \sqrt { 1 - x ^ { 2 } } } }
$$

in the interval $( - 1 , 1 )$ . (This particular choice is called Gauss-Chebyshev integration, for reasons that will become clear shortly.)

Notice that the integration formula (4.6.1) can also be written with the weight function $W ( x )$ not overtly visible: Define $g ( x ) \equiv W ( x ) f ( x )$ and $v _ { j } \equiv w _ { j } / W ( x _ { j } )$ . Then (4.6.1) becomes

$$
\int _ { a } ^ { b } g ( x ) d x \approx \sum _ { j = 0 } ^ { N - 1 } v _ { j } g ( x _ { j } )
$$

Where did the function $W ( x )$ go? It is lurking there, ready to give high-order accuracy to integrands of the form polynomials times $W ( x )$ , and ready to deny high-order accuracy to integrands that are otherwise perfectly smooth and well-behaved. When you find tabulations of the weights and abscissas for a given $W ( x )$ , you have to determine carefully whether they are to be used with a formula in the form of (4.6.1), or like (4.6.4).

So far our introduction to Gaussian quadrature is pretty standard. However, there is an aspect of the method that is not as widely appreciated as it should be: For smooth integrands (after factoring out the appropriate weight function), Gaussian quadrature converges exponentially fast as $N$ increases, because the order of the method, not just the density of points, increases with $N$ . This behavior should be contrasted with the power-law behavior (e.g., $1 / N ^ { 2 }$ or $1 / N ^ { 4 }$ ) of the Newton-Cotes based methods in which the order remains fixed (e.g., 2 or 4) even as the density of points increases. For a more rigorous discussion, see $\ S 2 0 . 7 . 4$ .

Here is an example of a quadrature routine that contains the tabulated abscissas and weights for the case $W ( x ) = 1$ and $N = 1 0$ . Since the weights and abscissas are, in this case, symmetric around the midpoint of the range of integration, there are actually only five distinct values of each:

# template <class T>

Doub qgaus(T &func, const Doub a, const Doub b)

Returns the integral of the function or functor func between a and b, by ten-point Gauss-Legendre integration: the function is evaluated exactly ten times at interior points in the range of integration.

Here are the abscissas and weights:   
static const Doub x[] $= \{ 0$ .1488743389816312,0.4333953941292472, 0.6794095682990244,0.8650633666889845,0.9739065285171717};   
static const Doub w[] $=$ {0.2955242247147529,0.2692667193099963, 0.2190863625159821,0.1494513491505806,0.0666713443086881};   
Doub $\mathtt { x m = 0 }$ .5\*(b+a);   
Doub $\tt x r { = } 0$ .5\*(b-a);   
Doub $\mathtt { s } = 0$ ; Will be twice the average value of the function, since the   
for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<5;j++) { ten weights (five numbers above each used twice) Doub dx=xr\*x[j]; sum to 2. s += w[j]\*(func(xm+dx)+func(xm-dx));   
}   
return s \*= xr; Scale the answer to the range of integration.

The above routine illustrates that one can use Gaussian quadratures without necessarily understanding the theory behind them: One just locates tabulated weights and abscissas in a book (e.g., [1] or [2]). However, the theory is very pretty, and it will come in handy if you ever need to construct your own tabulation of weights and abscissas for an unusual choice of $W ( x )$ . We will therefore give, without any proofs, some useful results that will enable you to do this. Several of the results assume that $W ( x )$ does not change sign inside $( a , b )$ , which is usually the case in practice.

The theory behind Gaussian quadratures goes back to Gauss in 1814, who used continued fractions to develop the subject. In 1826, Jacobi rederived Gauss’s results by means of orthogonal polynomials. The systematic treatment of arbitrary weight functions $W ( x )$ using orthogonal polynomials is largely due to Christoffel in 1877. To introduce these orthogonal polynomials, let us fix the interval of interest to be $( a , b )$ . We can define the “scalar product of two functions $f$ and $g$ over a weight function $W$ ” as

$$
\langle f \vert g \rangle \equiv \int _ { a } ^ { b } W ( x ) f ( x ) g ( x ) d x
$$

The scalar product is a number, not a function of $x$ . Two functions are said to be orthogonal if their scalar product is zero. A function is said to be normalized if its scalar product with itself is unity. A set of functions that are all mutually orthogonal and also all individually normalized is called an orthonormal set.

We can find a set of polynomials (i) that includes exactly one polynomial of order $j$ , called $p _ { j } ( x )$ , for each $j = 0 , 1 , 2 , \ldots$ and (ii) all of which are mutually orthogonal over the specified weight function $W ( x )$ . A constructive procedure for finding such a set is the recurrence relation

$$
\begin{array} { l } { { p _ { - 1 } ( x ) \equiv 0 } } \\ { { p _ { 0 } ( x ) \equiv 1 } } \\ { { p _ { j + 1 } ( x ) = ( x - a _ { j } ) p _ { j } ( x ) - b _ { j } p _ { j - 1 } ( x ) \qquad j = 0 , 1 , 2 , . . . } } \end{array}
$$

where

$$
\begin{array} { l l } { { a _ { j } = \displaystyle \frac { \left. x p _ { j } | p _ { j } \right. } { \left. p _ { j } | p _ { j } \right. } ~ } } & { { ~ j = 0 , 1 , . . . } } \\ { { b _ { j } = \displaystyle \frac { \left. p _ { j } | p _ { j } \right. } { \left. p _ { j - 1 } | p _ { j - 1 } \right. } ~ } } & { { ~ j = 1 , 2 , . . . } } \end{array}
$$

The coefficient $b _ { 0 }$ is arbitrary; we can take it to be zero.

The polynomials defined by (4.6.6) are monic, that is, the coefficient of their leading term $[ x ^ { j }$ for $p _ { j } ( x ) ]$ is unity. If we divide each $p _ { j } ( x )$ by the constant $[ \left. p _ { j } | p _ { j } \right. ] ^ { 1 / 2 }$ , we can render the set of polynomials orthonormal. One also encounters orthogonal polynomials with various other normalizations. You can convert from a given normalization to monic polynomials if you know that the coefficient of $x ^ { j }$ in $p _ { j }$ is $\lambda _ { j }$ , say; then the monic polynomials are obtained by dividing each $p _ { j }$ by $\lambda _ { j }$ . Note that the coefficients in the recurrence relation (4.6.6) depend on the adopted normalization.

The polynomial $p _ { j } ( x )$ can be shown to have exactly $j$ distinct roots in the interval $( a , b )$ . Moreover, it can be shown that the roots of $p _ { j } ( x )$ “interleave” the $j - 1$ roots of $p _ { j - 1 } ( x )$ , i.e., there is exactly one root of the former in between each two adjacent roots of the latter. This fact comes in handy if you need to find all the roots. You can start with the one root of $p _ { 1 } ( x )$ and then, in turn, bracket the roots of each higher $j$ , pinning them down at each stage more precisely by Newton’s rule or some other root-finding scheme (see Chapter 9).

Why would you ever want to find all the roots of an orthogonal polynomial $p _ { j } ( x ) ?$ Because the abscissas of the $N$ -point Gaussian quadrature formulas (4.6.1) and (4.6.4) with weighting function $W ( x )$ in the interval $( a , b )$ are precisely the roots of the orthogonal polynomial $p _ { N } ( x )$ for the same interval and weighting function. This is the fundamental theorem of Gaussian quadratures, and it lets you find the abscissas for any particular case.

Once you know the abscissas $x _ { 0 } , \ldots , x _ { N - 1 }$ , you need to find the weights $w _ { j }$ , $j = 0 , \ldots , N - 1$ . One way to do this (not the most efficient) is to solve the set of linear equations

$$
\left[ \begin{array} { c c c c } { p _ { 0 } ( x _ { 0 } ) } & { \ldots } & { p _ { 0 } ( x _ { N - 1 } ) } \\ { p _ { 1 } ( x _ { 0 } ) } & { \ldots } & { p _ { 1 } ( x _ { N - 1 } ) } \\ { \vdots } & { } & { \vdots } \\ { p _ { N - 1 } ( x _ { 0 } ) } & { \ldots } & { p _ { N - 1 } ( x _ { N - 1 } ) } \end{array} \right] \left[ \begin{array} { c } { w _ { 0 } } \\ { w _ { 1 } } \\ { \vdots } \\ { w _ { N - 1 } } \end{array} \right] = \left[ \begin{array} { c } { \int _ { a } ^ { b } W ( x ) p _ { 0 } ( x ) d x } \\ { 0 } \\ { \vdots } \\ { 0 } \end{array} \right]
$$

Equation (4.6.8) simply solves for those weights such that the quadrature (4.6.1) gives the correct answer for the integral of the first $N$ orthogonal polynomials. Note that the zeros on the right-hand side of (4.6.8) appear because $p _ { 1 } ( x ) , \ldots , p _ { N - 1 } ( x )$ are all orthogonal to $p _ { 0 } ( x )$ , which is a constant. It can be shown that, with those weights, the integral of the next $N - 1$ polynomials is also exact, so that the quadrature is exact for all polynomials of degree $2 N - 1$ or less. Another way to evaluate the weights (though one whose proof is beyond our scope) is by the formula

$$
w _ { j } = \frac { \langle p _ { N - 1 } | p _ { N - 1 } \rangle } { p _ { N - 1 } ( x _ { j } ) p _ { N } ^ { \prime } ( x _ { j } ) }
$$

where $p _ { N } ^ { \prime } ( x _ { j } )$ is the derivative of the orthogonal polynomial at its zero $x _ { j }$

The computation of Gaussian quadrature rules thus involves two distinct phases: (i) the generation of the orthogonal polynomials $p _ { 0 } , \ldots , p _ { N }$ , i.e., the computation of the coefficients $a _ { j } , b _ { j }$ in (4.6.6), and (ii) the determination of the zeros of $p _ { N } ( x )$ , and the computation of the associated weights. For the case of the “classical” orthogonal polynomials, the coefficients $a _ { j }$ and $b _ { j }$ are explicitly known (equations $4 . 6 . 1 0 \textrm { -- }$ 4.6.14 below) and phase (i) can be omitted. However, if you are confronted with a “nonclassical” weight function $W ( x )$ , and you don’t know the coefficients $a _ { j }$ and $b _ { j }$ , the construction of the associated set of orthogonal polynomials is not trivial. We discuss it at the end of this section.

# 4.6.1 Computation of the Abscissas and Weights

This task can range from easy to difficult, depending on how much you already know about your weight function and its associated polynomials. In the case of classical, well-studied, orthogonal polynomials, practically everything is known, including good approximations for their zeros. These can be used as starting guesses, enabling Newton’s method (to be discussed in $\ S 9 . 4 )$ to converge very rapidly. Newton’s method requires the derivative $p _ { N } ^ { \prime } ( x )$ , which is evaluated by standard relations in terms of $p _ { N }$ and $p _ { N - 1 }$ . The weights are then conveniently evaluated by equation (4.6.9). For the following named cases, this direct root finding is faster, by a factor of 3 to 5, than any other method.

Here are the weight functions, intervals, and recurrence relations that generate the most commonly used orthogonal polynomials and their corresponding Gaussian quadrature formulas.

Gauss-Legendre:

$$
\begin{array} { c } { { W ( x ) = 1 \qquad - 1 < x < 1 } } \\ { { ( j + 1 ) P _ { j + 1 } = ( 2 j + 1 ) x P _ { j } - j P _ { j - 1 } } } \end{array}
$$

Gauss-Chebyshev:

$$
\begin{array} { c } { { W ( x ) = ( 1 - x ^ { 2 } ) ^ { - 1 / 2 } \qquad - 1 < x < 1 } } \\ { { T _ { j + 1 } = 2 x T _ { j } - T _ { j - 1 } } } \end{array}
$$

Gauss-Laguerre:

$$
\begin{array} { c } { { W ( x ) = x ^ { \alpha } e ^ { - x } \qquad 0 < x < \infty } } \\ { { ( j + 1 ) L _ { j + 1 } ^ { \alpha } = ( - x + 2 j + \alpha + 1 ) L _ { j } ^ { \alpha } - ( j + \alpha ) L _ { j - 1 } ^ { \alpha } } } \end{array}
$$

Gauss-Hermite:

$$
\begin{array} { c } { { W ( x ) = e ^ { - x ^ { 2 } } ~ - \infty < x < \infty } } \\ { { H _ { j + 1 } = 2 x H _ { j } - 2 j H _ { j - 1 } } } \end{array}
$$

Gauss-Jacobi:

$$
\begin{array} { l } { { W ( x ) = ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } \qquad - 1 < x < 1 } } \\ { { c _ { j } P _ { j + 1 } ^ { ( \alpha , \beta ) } = ( d _ { j } + e _ { j } x ) P _ { j } ^ { ( \alpha , \beta ) } - f _ { j } P _ { j - 1 } ^ { ( \alpha , \beta ) } } } \end{array}
$$

where the coefficients $c _ { j } , d _ { j } , e _ { j }$ , and $f _ { j }$ are given by

$$
\begin{array} { l } { c _ { j } = 2 ( j + 1 ) ( j + \alpha + \beta + 1 ) ( 2 j + \alpha + \beta ) } \\ { d _ { j } = ( 2 j + \alpha + \beta + 1 ) ( \alpha ^ { 2 } - \beta ^ { 2 } ) } \\ { e _ { j } = ( 2 j + \alpha + \beta ) ( 2 j + \alpha + \beta + 1 ) ( 2 j + \alpha + \beta + 2 ) } \\ { f _ { j } = 2 ( j + \alpha ) ( j + \beta ) ( 2 j + \alpha + \beta + 2 ) } \end{array}
$$

We now give individual routines that calculate the abscissas and weights for these cases. First comes the most common set of abscissas and weights, those of Gauss-Legendre. The routine, due to G.B. Rybicki, uses equation (4.6.9) in the special form for the Gauss-Legendre case,

$$
w _ { j } = \frac { 2 } { ( 1 - x _ { j } ^ { 2 } ) [ P _ { N } ^ { \prime } ( x _ { j } ) ] ^ { 2 } }
$$

The routine also scales the range of integration from $( x _ { 1 } , x _ { 2 } )$ to $( - 1 , 1 )$ , and provides abscissas $x _ { j }$ and weights $w _ { j }$ for the Gaussian formula

$$
\int _ { x _ { 1 } } ^ { x _ { 2 } } f ( x ) d x = \sum _ { j = 0 } ^ { N - 1 } w _ { j } f ( x _ { j } )
$$

void gauleg(const Doub x1, const Doub x2, VecDoub_O &x, VecDoub_O &w) Given the lower and upper limits of integration x1 and $\tt x 2$ , this routine returns arrays $\mathbf { x } \left[ 0 \ldots \ldots \right] $ and $\mathtt { w } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ of length n, containing the abscissas and weights of the Gauss-Legendre n-point quadrature formula.

const Doub EPS $^ { = 1 }$ .0e-14; EPS is the relative precision.   
Doub z1,z,xm,xl,pp,p3,p2,p1;   
Int $\mathrm { n } { = } \mathrm { x }$ .size();   
Int ${ \mathrm { m } } { = } \left( { \mathrm { n } } { + } 1 \right) / 2$ ; The roots are symmetric in the interval, so   
xm=0.5\*(x2+x1); we only have to find half of them.   
$\mathtt { x l } { = } 0$ .5\*(x2-x1);   
for (Int $\scriptstyle { \dot { 1 } } = 0$ ;i<m;i++) { Loop over the desired roots. $_ { z = }$ cos(3.141592654\*(i+0.75)/(n+0.5)); Starting with this approximation to the ith root, we enter the main loop of refinement by Newton’s method. do { $\mathtt { p 1 } = 1$ .0; $\mathtt { p 2 = 0 }$ .0; for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) { Loop up the recurrence relation to get the $\mathtt { p 3 } \mathrm { = p 2 }$ ; Legendre polynomial evaluated at $_ { z }$ . $\mathtt { p } 2 \mathrm { = p } 1$ ; p1=((2.0\*j+1.0)\*z\*p2-j\*p3)/(j+1); } p1 is now the desired Legendre polynomial. We next compute pp, its derivative, by a standard relation involving also p2, the polynomial of one lower order. pp=n\*(z\*p1-p2)/(z\*z-1.0); $z 1 { = } z$ ; z=z1-p1/pp; Newton’s method. } while (abs(z-z1) > EPS); x[i]=xm-xl\*z; Scale the root to the desired interval, x[n-1-i] $=$ xm+xl\*z; and put in its symmetric counterpart. w[i]=2.0\*xl/((1.0-z\*z)\*pp\*pp); Compute the weight w[n-1-i] $= _ { \mathrm { w } }$ [i]; and its symmetric counterpart.   
}

Next we give three routines that use initial approximations for the roots given by Stroud and Secrest [2]. The first is for Gauss-Laguerre abscissas and weights, to be used with the integration formula

$$
\int _ { 0 } ^ { \infty } x ^ { \alpha } e ^ { - x } f ( x ) d x = \sum _ { j = 0 } ^ { N - 1 } w _ { j } f ( x _ { j } )
$$

oid gaulag(VecDoub_O &x, VecDoub_O &w, const Doub alf)

Given alf, the parameter $\pmb { \alpha }$ of the Laguerre polynomials, this routine returns arrays $\mathbf { x } \left[ 0 \ldots \ldots \right]$ and $\mathtt { w } \left[ 0 \ldots \ldots \mathtt { n } ^ { - 1 } \right]$ containing the abscissas and weights of the $\mathbf { n }$ -point Gauss-Laguerre quadrature formula. The smallest abscissa is returned in $\mathbf { x } \left[ 0 \right]$ , the largest in $\mathbf { x } \left[ \mathbf { n - 1 } \right]$ .

const Int MAXIT ${ \tt = } 1 0$ ;   
const Doub EPS $\mathrel { \mathop : } = 1$ .0e-14; EPS is the relative precision.   
Int i,its,j;   
Doub ai,p1,p2,p3,pp,z,z1;   
Int $\mathrm { n } { = } \mathrm { x }$ .size();   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n; $\dot { \bf 1 } + +$ ) { Loop over the desired roots. if $\mathrm {  ~ \dot { ~ 1 ~ } ~ } = = \mathrm {  ~ 0 ~ }$ ) { Initial guess for the smallest root. z=(1.0+alf)\*(3.0+0.92\*alf)/(1.0+2.4\*n+1.8\*alf); } else if $\mathbf { \dot { \textbf { i } } } = = \mathbf { \textbf { 1 } }$ ) { Initial guess for the second root. z += (15.0+6.25\*alf)/(1.0+0.9\*alf+2.5\*n); } else { Initial guess for the other roots. $\mathsf { a } \dot { \mathsf { 1 } } = \dot { \mathsf { 1 } } - 1$ ;

z += ((1.0+2.55\*ai)/(1.9\*ai)+1.26\*ai\*alf/ (1.0+3.5\*ai))\*(z-x[i-2])/(1.0+0.3\*alf); for (its ${ = } 0$ ;its<MAXIT;its++) { Refinement by Newton’s method. $\mathtt { p 1 } = 1$ .0; p2=0.0; for (j=0;j<n;j++) { Loop up the recurrence relation to get the $\mathtt { p 3 } \mathtt { = p 2 }$ ; Laguerre polynomial evaluated at $_ { z }$ . $\mathtt { p } 2 \mathrm { = p } 1$ ; p1=((2\*j+1+alf-z)\*p2-(j+alf)\*p3)/(j+1); } p1 is now the desired Laguerre polynomial. We next compute pp, its derivative, by a standard relation involving also p2, the polynomial of one lower order. pp=(n\*p1-(n+alf)\*p2)/z; $_ { z 1 } = z$ ; $\scriptstyle \mathtt { z } = \mathtt { z } 1 - \mathtt { p } 1 / \mathtt { p } \mathtt { p }$ ; Newton’s formula. if (abs(z-z1) $< =$ EPS) break; } if (its $> =$ MAXIT) throw("too many iterations in gaulag"); $\mathbf { x } \left[ \dot { \mathbf { 1 } } \right] = \mathbf { z }$ ; Store the root and the weight. w[i] $=$ -exp(gammln(alf+n)-gammln(Doub(n)))/(pp\*n\*p2); }

Next is a routine for Gauss-Hermite abscissas and weights. If we use the “standard” normalization of these functions, as given in equation (4.6.13), we find that the computations overflow for large $N$ because of various factorials that occur. We can avoid this by using instead the orthonormal set of polynomials $\widetilde { H } _ { j }$ . They are generated by the recurrence

$$
\tilde { H } _ { - 1 } = 0 , \quad \tilde { H } _ { 0 } = \frac { 1 } { \pi ^ { 1 / 4 } } , \quad \tilde { H } _ { j + 1 } = x \sqrt { \frac { 2 } { j + 1 } } \tilde { H } _ { j } - \sqrt { \frac { j } { j + 1 } } \tilde { H } _ { j - 1 }
$$

The formula for the weights becomes

$$
w _ { j } = \frac { 2 } { [ { \widetilde { H } _ { N } ^ { \prime } ( x _ { j } ) } ] ^ { 2 } }
$$

while the formula for the derivative with this normalization is

$$
\widetilde { H } _ { j } ^ { \prime } = \sqrt { 2 j } \widetilde { H } _ { j - 1 }
$$

The abscissas and weights returned by gauher are used with the integration formula

$$
\int _ { - \infty } ^ { \infty } e ^ { - x ^ { 2 } } f ( x ) d x = \sum _ { j = 0 } ^ { N - 1 } w _ { j } f ( x _ { j } )
$$

# void gauher(VecDoub_O &x, VecDoub_O &w)

This routine returns arrays $\mathbf { x } \left[ 0 \ldots \ldots \right]$ and $\mathtt { w } \left[ 0 \ldots \ldots \mathtt { n } ^ { - 1 } \right]$ containing the abscissas and weights of the n-point Gauss-Hermite quadrature formula. The largest abscissa is returned in $\mathbf { x } \left[ 0 \right]$ , the most negative in $\mathbf { x } \left[ \mathbf { n - 1 } \right]$ .

const Doub EPS $= 1$ .0e-14,PIM4 $\mathtt { \mathtt { = 0 } }$ .7511255444649425;   
Relative precision and $1 / \pi ^ { 1 / 4 }$ .   
const Int MAXIT=10; Maximum iterations.   
Int i,its,j,m;   
Doub p1,p2,p3,pp,z,z1;   
Int $\mathbf { n } { = } \mathbf { x }$ .size();   
${ \mathrm { m } } { = } \left( { \mathrm { n } } { + } 1 \right) / 2$ ;   
The roots are symmetric about the origin, so we have to find only half of them.   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<m;i++) { Loop over the desired roots. if ( $\mathrm { ~ \dot ~ { ~ 2 ~ } ~ } = = \mathrm { ~ 0 ~ }$ ) { Initial guess for the largest root. $z =$ sqrt(Doub( $^ { 2 * \mathtt { n } + 1 }$ ))-1.85575\*pow(Doub $^ { 2 * \mathrm { n } + 1 ) }$ ,-0.16667); } else if ( $\begin{array} { r } { \dot { \textbf { 1 } } = = \textbf { 1 } } \end{array}$ ) { Initial guess for the second largest root. $\textbf { z } \mathrel { \mathop { \sim } } 1$ .14\*pow(Doub(n),0.426)/z; } else if $\mathbf { \dot { \textbf { 1 } } } = = \mathbf { \nabla } 2$ ) { Initial guess for the third largest root. $z { = } 1$ .86\*z-0.86\*x[0]; } else if $\mathrm { ~ i ~ } = = \ 3$ ) { Initial guess for the fourth largest root. $z { = } 1$ .91\*z-0.91\*x[1]; } else { Initial guess for the other roots. z=2.0\*z-x[i-2]; for (its ${ = } 0$ ;its<MAXIT;its $^ { + + }$ ) { Refinement by Newton’s method. p1=PIM4; $\mathtt { p 2 } = 0$ .0; for (j=0;j<n;j++) { Loop up the recurrence relation to get p3=p2; the Hermite polynomial evaluated at p2=p1; z. p1=z\*sqrt(2.0/(j+1))\*p2-sqrt(Doub(j)/(j+1))\*p3; } p1 is now the desired Hermite polynomial. We next compute pp, its derivative, by the relation (4.6.21) using p2, the polynomial of one lower order. pp=sqrt(Doub(2\*n))\*p2; $z 1 = z$ ; $z { = } z { \mathrm { 1 - p 1 / p p } }$ ; Newton’s formula. if (abs(z-z1) $< =$ EPS) break; if (its $> =$ MAXIT) throw("too many iterations in gauher"); $\mathbf { x } \left[ \dot { \mathbf { 1 } } \right] = \mathbf { z }$ ; Store the root $\mathbf { x } \left[ \mathbf { n - 1 - i } \right] \ = \ - \mathbf { z } ;$ ; and its symmetric counterpart. w[i]=2.0/(pp\*pp); Compute the weight w[n-1-i] $= _ { \mathrm { w } }$ [i]; and its symmetric counterpart.   
}

Finally, here is a routine for Gauss-Jacobi abscissas and weights, which implement the integration formula

$$
\int _ { - 1 } ^ { 1 } ( 1 - x ) ^ { \alpha } ( 1 + x ) ^ { \beta } f ( x ) d x = \sum _ { j = 0 } ^ { N - 1 } w _ { j } f ( x _ { j } )
$$

void gaujac(VecDoub_O &x, VecDoub_O &w, const Doub alf, const Doub bet)

Given alf and bet, the parameters $\pmb { \alpha }$ and $\beta$ of the Jacobi polynomials, this routine returns arrays $\mathbf { x } \left[ 0 \ldots \ldots \right] $ and $\mathtt { w } \left[ 0 \ldots \ldots \mathtt { n } ^ { - 1 } \right]$ containing the abscissas and weights of the $\mathbf { n } \cdot$ -point Gauss-Jacobi quadrature formula. The largest abscissa is returned in $\mathbf { x } \left[ 0 \right]$ , the smallest in $\mathbf { x } \left[ \mathbf { n } \mathrm { - } 1 \right]$ .

const Int MAXIT ${ \tt = } 1 0$ ;   
const Doub EPS $^ { = 1 }$ .0e-14;   
Int i,its,j;   
Doub alfbet,an,bn,r1,r2,r3;   
Doub a,b,c,p1,p2,p3,pp,temp,z,z1;   
Int $\mathbf { n } { = } \mathbf { x }$ .size();   
for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) { if ( $\mathrm { ~ \\\dot { ~ 1 ~ } ~ } = = \mathrm { ~ 0 ~ }$ ) { an alf/n;

EPS is the relative precision.

Loop over the desired roots.   
Initial guess for the largest root.