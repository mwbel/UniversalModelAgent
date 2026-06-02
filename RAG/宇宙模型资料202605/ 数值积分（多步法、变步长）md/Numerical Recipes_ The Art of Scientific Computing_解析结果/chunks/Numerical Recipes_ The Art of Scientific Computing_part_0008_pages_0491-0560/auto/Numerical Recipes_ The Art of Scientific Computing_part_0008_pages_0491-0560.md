the complex unit circle, approximately equally spaced around it. When the method converges on a simple complex zero, it is known that its convergence is third order.

In some instances the complex arithmetic in the Laguerre method is no disadvantage, since the polynomial itself may have complex coefficients.

To motivate (although not rigorously derive) the Laguerre formulas we can note the following relations between the polynomial and its roots and derivatives:

$$
P _ { n } ( x ) = ( x - x _ { 0 } ) ( x - x _ { 1 } ) \dots ( x - x _ { n - 1 } )
$$$$
{ \begin{array} { c } { { \displaystyle { r _ { n } } ( x ) = ( x - x _ { 0 } ) ( x - x _ { 1 } ) \ldots ( x - x _ { n - 1 } ) } } \\ { { \ln \left| P _ { n } ( x ) \right| = \ln \left| x - x _ { 0 } \right| + \ln \left| x - x _ { 1 } \right| + \ldots + \ln \left| x - x _ { n - 1 } \right| } } \\ { { \displaystyle { \frac { d \ln \left| P _ { n } ( x ) \right| } { d x } } = + { \frac { 1 } { x - x _ { 0 } } } + { \frac { 1 } { x - x _ { 1 } } } + \ldots + { \frac { 1 } { x - x _ { n - 1 } } } = { \frac { P _ { n } ^ { \prime } } { P _ { n } } } = G } } \\ { { - { \frac { d ^ { 2 } \ln \left| P _ { n } ( x ) \right| } { d x ^ { 2 } } } = + { \frac { 1 } { ( x - x _ { 0 } ) ^ { 2 } } } + { \frac { 1 } { ( x - x _ { 1 } ) ^ { 2 } } } + \ldots + { \frac { 1 } { ( x - x _ { n - 1 } ) ^ { 2 } } } } } \\ { { = \left[ { \frac { P _ { n } ^ { \prime } } { P _ { n } } } \right] ^ { 2 } - { \frac { P _ { n } ^ { \prime \prime } } { P _ { n } } } = H } } \end{array} }
$$

Starting from these relations, the Laguerre formulas make what Acton [1] nicely calls “a rather drastic set of assumptions”: The root $x _ { 0 }$ that we seek is assumed to be located some distance $a$ from our current guess $x$ , while all other roots are assumed to be located at a distance $b$ ,

$$
x - x _ { 0 } = a , \quad x - x _ { i } = b , \qquad i = 1 , 2 , \ldots , n - 1
$$

Then we can express (9.5.6) and (9.5.7) as

$$
{ \begin{array} { c } { { \frac { 1 } { a } } + { \frac { n - 1 } { b } } = G } \\ { { \frac { 1 } { a ^ { 2 } } } + { \frac { n - 1 } { b ^ { 2 } } } = H } \end{array} }
$$

which yields as the solution for $a$

$$
a = \frac { n } { G \pm \sqrt { ( n - 1 ) ( n H - G ^ { 2 } ) } }
$$

where the sign should be taken to yield the largest magnitude for the denominator. Since the factor inside the square root can be negative, $a$ can be complex. (A more rigorous justification of equation 9.5.11 is in [4].)

The method operates iteratively: For a trial value $x$ , calculate $a$ by equation (9.5.11). Then use $x - a$ as the next trial value. Continue until $a$ is sufficiently small.

The following routine implements the Laguerre method to find one root of a given polynomial of degree m, whose coefficients can be complex. As usual, the first coefficient, $\mathtt { a } [ 0 ]$ , is the constant term, while $\mathsf { a } \left[ \mathsf { m } \right]$ is the coefficient of the highest power of $x$ . The routine implements a simplified version of an elegant stopping criterion due to Adams [5], which neatly balances the desire to achieve full machine accuracy, on the one hand, with the danger of iterating forever in the presence of roundoff error, on the other.

# void laguer(VecComplex_I &a, Complex &x, Int &its) {

Given the $\mathtt { m } { + } 1$ complex coefficients a[0..m] of the polynomial $\scriptstyle \sum _ { i = 0 } ^ { \mathrm { m } } \mathsf { a } [ i ] x ^ { i }$ , and given a complex value x, this routine improves x by Laguerre’s method until it converges, within the achievable roundoff limit, to a root of the given polynomial. The number of iterations taken is returned as its.

const Int MR ${ } = 8$ ,MT $\mathtt { \lambda } = 1 0$ ,MAXI $\scriptstyle \mathrm { T = M T * l }$ MR;   
const Doub EPS numeric_limits<Doub>::epsilon();   
Here EPS is the estimated fractional roundoff error. We try to break (rare) limit cycles with   
MR different fractional values, once every MT steps, for MAXIT total allowed iterations.   
static const Doub frac[MR+1] $=$ {0.0,0.5,0.25,0.75,0.13,0.38,0.62,0.88,1.0};   
Fractions used to break a limit cycle.   
Complex dx,x1,b,d,f,g,h,sq,gp,gm,g2;   
Int $\mathtt { m } = \mathtt { a }$ .size()-1;   
for (Int iter=1;iter $< =$ MAXIT;iter++) { Loop over iterations up to allowed maximum. its=iter; $\mathtt { b } = \mathtt { a }$ [m]; Doub err=abs(b); $\mathtt { d } \mathtt { = } \mathtt { f } = 0$ .0; Doub abx $=$ abs(x); for (Int j=m-1;j>=0;j--) { Efficient computation of the polynomial and f=x\*f+d; its first two derivatives. f stores $P ^ { \prime \prime } / 2$ . d=x\*d+b; b=x\*b+a[j]; err=abs(b)+abx\*err; err $\ast =$ EPS; Estimate of roundoff error in evaluating polynomial. if (abs(b) $< =$ err) return; We are on the root. $s { = } \mathrm { d } / \mathrm { b }$ ; The generic case: Use Laguerre’s formula. g2=g\*g; h=g2-2.0\*f/b; sq=sqrt(Doub(m-1)\*(Doub(m)\*h-g2)); gp=g+sq; gm=g-sq; Doub abp=abs(gp); Doub abm $\downharpoonleft$ abs(gm); if (abp $<$ abm) ${ \tt g p } = { \tt g m }$ ; dx=MAX(abp,abm) > 0.0 ? Doub(m)/gp : polar(1+abx,Doub(iter)); $\tt x 1 = \tt x$ -dx; if $\mathbf { \bar { x } } \ \mathbf { = } \ \mathbf { x } 1$ ) return; Converged. if (iter % MT $! = ~ 0 ^ { \prime }$ ) $\tt x { = } \tt x 1$ ; else $\begin{array} { r l } { \mathbf { x } } & { { } - = } \end{array}$ frac[iter/MT]\*dx; Every so often we take a fractional step, to break any limit cycle (itself a rare occurrence).   
throw("too many iterations in laguer");

Very unusual; can occur only for complex roots. Try a different starting guess.

Here is a driver routine that calls laguer in succession for each root, performs the deflation, optionally polishes the roots by the same Laguerre method — if you are not going to polish in some other way — and finally sorts the roots by their real parts. (We will use this routine in Chapter 13.)

# void zroots(VecComplex_I &a, VecComplex_O &roots, const Bool &polish)

Given the $\mathtt { m } { + } 1$ complex coefficients a[0..m] of the polynomial $\scriptstyle \sum _ { i = 0 } ^ { \mathrm { m } } \mathsf { a } ( i ) x ^ { i }$ , this routine successively calls laguer and finds all m complex roots in roots $\left[ 0 \cdot \cdot \cdot \mathrm { m } ^ { - 1 } \right]$ . The boolean variable polish should be input as true if polishing (also by Laguerre’s method) is desired, false if the roots will be subsequently polished by other means.   
{   
Int i,its;   
Complex x,b,c;   
Int $\mathtt { m } = \mathtt { a }$ .size()-1;   
VecComplex ad $\left( \mathrm { m } { + } 1 \right)$ ;   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j $< = \mathtt { m }$ ;j++) ad[j] $= \mathtt { a }$ [j]; Copy of coefficients for successive deflation.   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = { \mathsf { m } } - 1$ ; $\scriptstyle { \dot { \mathsf { J } } } > = 0$ ;j--) { Loop over each root to be found. $\mathtt { x } = 0 \mathtt { . 0 }$ ; Start at zero to favor convergence to small-VecComplex ad_v(j+2); est remaining root, and return the root. for (Int $\scriptstyle { \dot { ] } } { \dot { ] } } = 0$ ;jj<j+2;jj $^ { + + }$ ) ad_v[jj] $=$ ad[jj]; laguer(ad_v,x,its); if (abs(imag $\mathbf { \Psi } ( \mathbf { x } )$ ) $< =$ 2.0\*EPS\*abs(real(x))) x=Complex(real(x),0.0); roots[j] $= \mathbf { x }$ ; b=ad[j+1]; Forward deflation. for (Int jj=j;jj> ${ \tt > } 0$ ;jj--) { $^ { \circ = }$ ad[jj]; ad[jj] $\mathtt { \Gamma } = \mathtt { b }$ ; b=x\*b+c; }   
}   
if (polish) for (Int j=0;j<m;j $^ { + + }$ ) Polish the roots using the undeflated coeffilaguer(a,roots[j],its); cients.   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<m;j++) { Sort roots by their real parts by straight inx=roots[j]; sertion. for (i=j-1; $\scriptstyle \dot { 1 } > = 0$ ;i--) { if (real(roots[i]) $< =$ real $\mathbf { \Psi } ( \mathbf { x } )$ ) break; roots[i+1] $=$ roots[i]; } roots $[ \dot { \bf 1 } + 1 ] = \bf { \underline { { x } } }$ ;   
}

# 9.5.4 Eigenvalue Methods

The eigenvalues of a matrix A are the roots of the “characteristic polynomial” $P ( x ) = \det [ \mathbf { A } - x \mathbf { I } ]$ . However, as we will see in Chapter 11, root finding is not generally an efficient way to find eigenvalues. Turning matters around, we can use the more efficient eigenvalue methods that are discussed in Chapter 11 to find the roots of arbitrary polynomials. You can easily verify (see, e.g., [6]) that the characteristic polynomial of the special $m \times m$ companion matrix

$$
\mathbf { A } = \left( \begin{array} { c c c c c } { - \frac { a _ { m - 1 } } { a _ { m } } } & { - \frac { a _ { m - 2 } } { a _ { m } } } & { \cdots } & { - \frac { a _ { 1 } } { a _ { m } } } & { - \frac { a _ { 0 } } { a _ { m } } } \\ { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 1 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { } & { } & { } & { \vdots } \\ { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \end{array} \right)
$$

is equivalent to the general polynomial

$$
P ( x ) = \sum _ { i = 0 } ^ { m } a _ { i } x ^ { i }
$$

If the coefficients $a _ { i }$ are real, rather than complex, then the eigenvalues of A can be found using the routine Unsymmeig in $\ S 1 1 . 6 - \ S 1 1 . 7$ (see discussion there). This method, implemented in the routine zrhqr following, is typically about a factor 2 slower than zroots (above). However, for some classes of polynomials, it is a more robust technique, largely because of the fairly sophisticated convergence methods embodied in Unsymmeig. If your polynomial has real coefficients, and you are having trouble with zroots, then zrhqr is a recommended alternative.

# void zrhqr(VecDoub_I &a, VecComplex_O &rt)

Find all the roots of a polynomial with real coefficients, $\scriptstyle \sum _ { i = 0 } ^ { \mathrm { m } } \mathsf { a } ( i ) x ^ { i }$ , given the coefficients a[0..m]. The method is to construct an upper Hessenberg matrix whose eigenvalues are the desired roots and then use the routine Unsymmeig. The roots are returned in the complex vector rt[0..m-1], sorted in descending order by their real parts.

Int $\mathtt { m } = \mathtt { a }$ .size()-1;   
MatDoub hess(m,m);   
for (Int $\mathtt { k } = 0$ ;k<m;k++) { Construct the matrix. hess[0][k] $=$ -a[m-k-1]/a[m]; for (Int $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<m; $\mathrm { j } + +$ ) hess[j][k] $= 0 . 0$ ; if (k $\ ! = \ \mathtt { m } - 1 \ :$ ) hess[k+1][k] $^ { = 1 }$ .0;   
}   
Unsymmeig h(hess, false, true); Find its eigenvalues.   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<m; ${ \mathrm { j } } + +$ ) rt[j]=h.wri[j];

# 9.5.5 Other Sure-Fire Techniques

The Jenkins-Traub method has become practically a standard in black-box polynomial root finders, e.g., in the IMSL library [3]. The method is too complicated to discuss here, but is detailed, with references to the primary literature, in [4].

The Lehmer-Schur algorithm is one of a class of methods that isolate roots in the complex plane by generalizing the notion of one-dimensional bracketing. It is possible to determine efficiently whether there are any polynomial roots within a circle of given center and radius. From then on it is a matter of bookkeeping to hunt down all the roots by a series of decisions regarding where to place new trial circles. Consult [1] for an introduction.

# 9.5.6 Techniques for Root Polishing

Newton-Raphson works very well for real roots once the neighborhood of a root has been identified. The polynomial and its derivative can be efficiently simultaneously evaluated as in $\ S 5 . 1$ . For a polynomial of degree n with coefficients ${ \mathsf { c } } \left[ 0 \right] \ldots { \mathsf { c } } \left[ { \mathsf { n } } \right]$ , the following segment of code carries out one cycle of Newton-Raphson:

$\mathtt { p } \mathtt { = c }$ [n]\*x+c[n-1];   
$\mathtt { p 1 } \mathtt { = c }$ [n];   
for(i=n-2;i>=0;i--) { p1=p+p1\*x; p=c[i]+p\*x;   
}   
if $\mathbf { \bar { p } 1 } \ \mathbf { = } \ 0 . 0 \mathbf { \bar { \rho } }$ ) throw("derivative should not vanish");   
$\bf { x _ { \alpha } } \mathrm { ~ -- ~ } \mathtt { p } / \mathtt { p } 1$ ;

Once all real roots of a polynomial have been polished, one must polish the complex roots, either directly or by looking for quadratic factors.

Direct polishing by Newton-Raphson is straightforward for complex roots if the above code is converted to complex data types. With real polynomial coefficients, note that your starting guess (tentative root) must be off the real axis, otherwise you will never get off that axis — and may get shot off to infinity by a minimum or maximum of the polynomial.

For real polynomials, the alternative means of polishing complex roots (or, for that matter, double real roots) is Bairstow’s method, which seeks quadratic factors. The advantage of going after quadratic factors is that it avoids all complex arithmetic. Bairstow’s method seeks a quadratic factor that embodies the two roots $x = a \pm i b$ , namely

$$
x ^ { 2 } - 2 a x + ( a ^ { 2 } + b ^ { 2 } ) \equiv x ^ { 2 } + B x + C
$$

In general, if we divide a polynomial by a quadratic factor, there will be a linear remainder

$$
P ( x ) = ( x ^ { 2 } + B x + C ) Q ( x ) + R x + S .
$$

Given $B$ and $C$ , $R$ and $S$ can be readily found, by polynomial division (-5.1). We can consider $R$ and $S$ to be adjustable functions of $B$ and $C$ , and they will be zero if the quadratic factor is a divisor of $P ( x )$ .

In the neighborhood of a root, a first-order Taylor series expansion approximates the variation of $R , S$ with respect to small changes in $B , C$ :

$$
\begin{array} { l } { \displaystyle R ( B + \delta B , C + \delta C ) \approx R ( B , C ) + \frac { \partial R } { \partial B } \delta B + \frac { \partial R } { \partial C } \delta C } \\ { \displaystyle S ( B + \delta B , C + \delta C ) \approx S ( B , C ) + \frac { \partial S } { \partial B } \delta B + \frac { \partial S } { \partial C } \delta C } \end{array}
$$

To evaluate the partial derivatives, consider the derivative of (9.5.15) with respect to $C$ . Since $P ( x )$ is a fixed polynomial, it is independent of $C$ , hence

$$
0 = ( x ^ { 2 } + B x + C ) { \frac { \partial Q } { \partial C } } + Q ( x ) + { \frac { \partial R } { \partial C } } x + { \frac { \partial S } { \partial C } }
$$

which can be rewritten as

$$
- Q ( x ) = ( x ^ { 2 } + B x + C ) { \frac { \partial Q } { \partial C } } + { \frac { \partial R } { \partial C } } x + { \frac { \partial S } { \partial C } }
$$

Similarly, $P ( x )$ is independent of $B$ , so differentiating (9.5.15) with respect to $B$ gives

$$
- x Q ( x ) = ( x ^ { 2 } + B x + C ) { \frac { \partial Q } { \partial B } } + { \frac { \partial R } { \partial B } } x + { \frac { \partial S } { \partial B } }
$$

Now note that equation (9.5.19) matches equation (9.5.15) in form. Thus if we perform a second synthetic division of $P ( x )$ , i.e., a division of $Q ( x )$ by the same quadratic factor, yielding a remainder $R _ { 1 } x + S _ { 1 }$ , then

$$
{ \frac { \partial R } { \partial C } } = - R _ { 1 } \qquad { \frac { \partial S } { \partial C } } = - S _ { 1 }
$$

To get the remaining partial derivatives, evaluate equation (9.5.20) at the two roots of the quadratic, $x _ { + }$ and $x _ { - }$ . Since

$$
Q ( x _ { \pm } ) = R _ { 1 } x _ { \pm } + S _ { 1 }
$$

we get

$$
\begin{array} { l } { \displaystyle { \frac { \partial R } { \partial B } x _ { + } + \frac { \partial S } { \partial B } = - x _ { + } ( R _ { 1 } x _ { + } + S _ { 1 } ) } } \\ { \displaystyle { \frac { \partial R } { \partial B } x _ { - } + \frac { \partial S } { \partial B } = - x _ { - } ( R _ { 1 } x _ { - } + S _ { 1 } ) } } \end{array}
$$

Solve these two equations for the partial derivatives, using

$$
\begin{array} { r } { x _ { + } + x _ { - } = - B \qquad x _ { + } x _ { - } = C } \end{array}
$$

and find

$$
{ \frac { \partial R } { \partial B } } = B R _ { 1 } - S _ { 1 } \qquad { \frac { \partial S } { \partial B } } = C R _ { 1 }
$$

Bairstow’s method now consists of using Newton-Raphson in two dimensions (which is actually the subject of the next section) to find a simultaneous zero of $R$ and $S$ . Synthetic division is used twice per cycle to evaluate $R , S$ and their partial derivatives with respect to $B , C$ . Like one-dimensional Newton-Raphson, the method works well in the vicinity of a root pair (real or complex), but it can fail miserably when started at a random point. We therefore recommend it only in the context of polishing tentative complex roots.

id qroot(VecDoub_I &p, Doub &b, Doub &c, const Doub eps)

Given $\tt { n } { + 1 }$ coefficients $\mathtt { p } [ 0 \cdot \cdot \mathtt { n } ]$ of a polynomial of degree n, and trial values for the coefficients of a quadratic factor $x ^ { * } x + b + x + c$ , improve the solution until the coefficients b,c change by less than eps. The routine poldiv in $\ S 5 . 1$ is used.

const Int ITMAX $= 2 0$ ; At most ITMAX iterations.   
const Doub TINY $\sp { \prime } = 1$ .0e-14;   
Doub sc,sb,s,rc,rb,r,dv,delc,delb;   
Int $\mathrm { n } { = } _ { \mathrm { p } }$ .size()-1;   
VecDoub d(3),q $\left( \mathtt { n } { + } 1 \right)$ ,qq $\left( \mathtt { n } { + } 1 \right)$ ,rem(n+1);   
d[2] $^ { = 1 }$ .0;   
for (Int iter ${ \tt = } 0$ ;iter<ITMAX;iter $^ { + + }$ ) { d[1] $\mathtt { \Gamma } = \mathtt { b }$ ; $\mathtt { d } [ 0 ] = \mathtt { c }$ ; poldiv(p,d,q,rem); s=rem[0]; First division, r,s. $\mathbf { r } { } =$ rem[1]; poldiv(q,d,qq,rem); sb = -c\*(rc = -rem[1]); Second division, partial r,s with respect to rb = -b\*rc+(sc $=$ -rem[0]); c. dv=1.0/(sb\*rc-sc\*rb); Solve $_ { 2 \times 2 }$ equation. delb=(r\*sc-s\*rc)\*dv; delc $=$ (-r\*sb+s\*rb)\*dv; b $+ =$ (delb $\mid =$ (r\*sc-s\*rc)\*dv); c $+ =$ (delc=(-r\*sb+s\*rb)\*dv); if ((abs(delb) $< =$ eps\*abs(b) || abs(b) < TINY) && (abs(delc) $< =$ eps\*abs(c) || abs(c) < TINY)) { return; Coefficients converged. }   
}   
throw("Too many iterations in routine qroot");

We have already remarked on the annoyance of having two tentative roots collapse to one value under polishing. You are left not knowing whether your polishing procedure has lost a root, or whether there is actually a double root, which was split only by roundoff errors in your previous deflation. One solution is deflate-andrepolish; but deflation is what we are trying to avoid at the polishing stage. An alternative is Maehly’s procedure. Maehly pointed out that the derivative of the reduced polynomial

$$
P _ { j } ( x ) \equiv \frac { P ( x ) } { ( x - x _ { 0 } ) \cdots ( x - x _ { j - 1 } ) }
$$

can be written as

$$
P _ { j } ^ { \prime } ( x ) = { \frac { P ^ { \prime } ( x ) } { ( x - x _ { 0 } ) \cdots ( x - x _ { j - 1 } ) } } - { \frac { P ( x ) } { ( x - x _ { 0 } ) \cdots ( x - x _ { j - 1 } ) } } \sum _ { i = 0 } ^ { j - 1 } ( x - x _ { i } ) ^ { - 1 }
$$

Hence one step of Newton-Raphson, taking a guess $x _ { k }$ into a new guess $x _ { k + 1 }$ , can be written as

$$
x _ { k + 1 } = x _ { k } - { \frac { P ( x _ { k } ) } { P ^ { \prime } ( x _ { k } ) - P ( x _ { k } ) \sum _ { i = 0 } ^ { j - 1 } ( x _ { k } - x _ { i } ) ^ { - 1 } } }
$$

This equation, if used with $i$ ranging over the roots already polished, will prevent a tentative root from spuriously hopping to another one’s true root. It is an example of so-called zero suppression as an alternative to true deflation.

Muller’s method, which was described above, can also be a useful adjunct at the polishing stage.

# CITED REFERENCES AND FURTHER READING:

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), Chapter 7.[1]   
Peters G., and Wilkinson, J.H. 1971, “Practical Problems Arising in the Solution of Polynomial Equations,” Journal of the Institute of Mathematics and Its Applications, vol. 8, pp. 16–35.[2]   
IMSL Math/Library Users Manual (Houston: IMSL Inc.)，see $^ { 2 0 0 7 + }$ ,http://www.vni.com/ products/imsl.[3]   
Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), $\ S 8 . 9 \substack { - 8 . 1 3 }$ .[4]   
Adams, D.A. 1967, “A Stopping Criterion for Polynomial Root Finding,” Communications of the ACM, vol.10,pp.655-658.[5]   
Johnson, L.W., and Riess, R.D. 1982, Numerical Analysis, 2nd ed. (Reading, MA: Addison-Wesley), $\ S 4 . 4 . 3$ .[6]   
Henrici, P. 1974, Applied and Computational Complex Analysis, vol. 1 (New York: Wiley).   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 5 . 5 - \ S 5 . 9$ .

# 9.6 Newton-Raphson Method for Nonlinear Systems of Equations

We make an extreme, but wholly defensible, statement: There are no good, general methods for solving systems of more than one nonlinear equation. Furthermore, it is not hard to see why (very likely) there never will be any good, general methods: Consider the case of two dimensions, where we want to solve simultaneously

$$
\begin{array} { r } { f ( x , y ) = 0 } \\ { g ( x , y ) = 0 } \end{array}
$$

![](images/208a8efacc3ecba0913ac48d4229cd0a3e19199f5b2c1605a49caf22e58ff068.jpg)  
Figure 9.6.1. Solution of two nonlinear equations in two unknowns. Solid curves refer to $f ( x , y )$ , dashed curves to $g ( x , y )$ . Each equation divides the $( x , y )$ -plane into positive and negative regions, bounded by zero curves. The desired solutions are the intersections of these unrelated zero curves. The number of solutions is a priori unknown.

The functions $f$ and $g$ are two arbitrary functions, each of which has zero contour lines that divide the $( x , y )$ -plane into regions where their respective function is positive or negative. These zero contour boundaries are of interest to us. The solutions that we seek are those points (if any) that are common to the zero contours of $f$ and $g$ (see Figure 9.6.1). Unfortunately, the functions $f$ and $g$ have, in general, no relation to each other at all! There is nothing special about a common point from either $f$ ’s point of view, or from $g$ ’s. In order to find all common points, which are the solutions of our nonlinear equations, we will (in general) have to do neither more nor less than map out the full zero contours of both functions. Note further that the zero contours will (in general) consist of an unknown number of disjoint closed curves. How can we ever hope to know when we have found all such disjoint pieces?

For problems in more than two dimensions, we need to find points mutually common to $N$ unrelated zero-contour hypersurfaces, each of dimension $N - 1$ . You see that root finding becomes virtually impossible without insight! You will almost always have to use additional information, specific to your particular problem, to answer such basic questions as, “Do I expect a unique solution?” and “Approximately where?” Acton [1] has a good discussion of some of the particular strategies that can be tried.

In this section we discuss the simplest multidimensional root-finding method, Newton-Raphson. This method gives a very efficient means of converging to a root, if you have a sufficiently good initial guess. It can also spectacularly fail to converge, indicating (though not proving) that your putative root does not exist nearby. In $\ S 9 . 7$ we discuss more sophisticated implementations of the Newton-Raphson method, which try to improve on Newton-Raphson’s poor global convergence. A multidimensional generalization of the secant method, called Broyden’s method, is also

discussed in $\ S 9 . 7$

A typical problem gives $N$ functional relations to be zeroed, involving variables $x _ { i } , i = 0 , 1 , \dotsc , N - 1$ :

$$
F _ { i } ( x _ { 0 } , x _ { 1 } , \ldots , x _ { N - 1 } ) = 0 \qquad i = 0 , 1 , \ldots , N - 1 .
$$

We let $\mathbf { X }$ denote the entire vector of values $x _ { i }$ and $\mathbf { F }$ denote the entire vector of functions $F _ { i }$ . In the neighborhood of $\mathbf { X }$ , each of the functions $F _ { i }$ can be expanded in Taylor series:

$$
F _ { i } ( \mathbf { x } + \delta \mathbf { x } ) = F _ { i } ( \mathbf { x } ) + \sum _ { j = 0 } ^ { N - 1 } \frac { \partial F _ { i } } { \partial x _ { j } } \delta x _ { j } + O ( \delta \mathbf { x } ^ { 2 } ) .
$$

The matrix of partial derivatives appearing in equation (9.6.3) is the Jacobian matrix $\mathbf { J }$ :

$$
J _ { i j } \equiv { \frac { \partial F _ { i } } { \partial x _ { j } } } .
$$

In matrix notation equation (9.6.3) is

$$
\mathbf { F } ( \mathbf { x } + \delta \mathbf { x } ) = \mathbf { F } ( \mathbf { x } ) + \mathbf { J } \cdot \delta \mathbf { x } + O ( \delta \mathbf { x } ^ { 2 } ) .
$$

By neglecting terms of order $\delta \mathbf { x } ^ { 2 }$ and higher and by setting $\mathbf { F } ( \mathbf { x } + \delta \mathbf { x } ) = 0$ , we obtain a set of linear equations for the corrections $\displaystyle { \delta \mathbf { x } }$ that move each function closer to zero simultaneously, namely

$$
\mathbf { J } \cdot \delta \mathbf { x } = - \mathbf { F } .
$$

Matrix equation (9.6.6) can be solved by $L U$ decomposition as described in $\ S 2 . 3$ . The corrections are then added to the solution vector,

$$
{ \bf x } _ { \mathrm { n e w } } = { \bf x } _ { \mathrm { o l d } } + \delta { \bf x }
$$

and the process is iterated to convergence. In general it is a good idea to check the degree to which both functions and variables have converged. Once either reaches machine accuracy, the other won’t change.

The following routine mnewt performs ntrial iterations starting from an initial guess at the solution vector $\mathbf { x } \left[ 0 \ldots \ldots \right]$ . Iteration stops if either the sum of the magnitudes of the functions $F _ { i }$ is less than some tolerance tolf, or the sum of the absolute values of the corrections to $\boldsymbol { \delta x } _ { i }$ is less than some tolerance tolx. mnewt calls a user-supplied function with the fixed name usrfun, which must provide the function values $\mathbf { F }$ and the Jacobian matrix J. (The more sophisticated methods later in this chapter will have a more versatile interface.) If $\mathbf { J }$ is difficult to compute analytically, you can try having usrfun invoke the routine NRfdjac of $\ S 9 . 7$ to compute the partial derivatives by finite differences. You should not make ntrial too big; rather, inspect to see what is happening before continuing for some further iterations.

void usrfun(VecDoub_I &x, VecDoub_O &fvec, MatDoub_O &fjac);

void mnewt(const Int ntrial, VecDoub_IO &x, const Doub tolx, const Doub tolf) { Given an initial guess $\mathbf { x } \left[ 0 \ldots \ldots \right] $ for a root in n dimensions, take ntrial Newton-Raphson steps to improve the root. Stop if the root converges in either summed absolute variable increments tolx or summed absolute function values tolf.

Int i, $\mathrm { n } { = } \mathrm { x }$ .size();   
VecDoub p(n),fvec(n);   
MatDoub fjac(n,n);   
for (Int $\mathtt { k } = 0$ ;k<ntrial; $\mathtt { k } { + } { + }$ ) { usrfun(x,fvec,fjac); User function supplies function values at $\mathbf { x }$ in Doub errf ${ = } 0$ .0; fvec and Jacobian matrix in fjac. for ( $\scriptstyle \dot { 1 } = 0$ ;i<n; $\dot { 1 } + +$ ) errf $+ =$ abs(fvec[i]); Check function convergence. if (errf $< =$ tolf) return; for ( $\scriptstyle \dot { 1 } = 0$ ;i<n; $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \beta } } } .$ ) p[i] $=$ -fvec[i]; Right-hand side of linear equations. LUdcmp alu(fjac); Solve linear equations using $_ { L U }$ decomposition. alu.solve(p,p); Doub errx $_ { = 0 }$ .0; Check root convergence. for ( $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) { Update solution. errx $+ =$ abs(p[i]); x[i] $+ = \mathrm { ~ p [ i ] }$ ; } if (errx $< =$ tolx) return;   
}   
return;

# 9.6.1 Newton's Method versus Minimization

In the next chapter, we will find that there are efficient general techniques for finding a minimum of a function of many variables. Why is that task (relatively) easy, while multidimensional root finding is often quite hard? Isn’t minimization equivalent to finding a zero of an $N$ -dimensional gradient vector, which is not so different from zeroing an $N$ -dimensional function? No! The components of a gradient vector are not independent, arbitrary functions. Rather, they obey so-called integrability conditions that are highly restrictive. Put crudely, you can always find a minimum by sliding downhill on a single surface. The test of “downhillness” is thus one-dimensional. There is no analogous conceptual procedure for finding a multidimensional root, where “downhill” must mean simultaneously downhill in $N$ separate function spaces, thus allowing a multitude of trade-offs as to how much progress in one dimension is worth compared with progress in another.

It might occur to you to carry out multidimensional root finding by collapsing all these dimensions into one: Add up the sums of squares of the individual functions $F _ { i }$ to get a master function $F$ that (i) is positive-definite and (ii) has a global minimum of zero exactly at all solutions of the original set of nonlinear equations. Unfortunately, as you will see in the next chapter, the efficient algorithms for finding minima come to rest on global and local minima indiscriminately. You will often find, to your great dissatisfaction, that your function $F$ has a great number of local minima. In Figure 9.6.1, for example, there is likely to be a local minimum wherever the zero contours of $f$ and $g$ make a close approach to each other. The point labeled $M$ is such a point, and one sees that there are no nearby roots.

However, we will now see that sophisticated strategies for multidimensional root finding can in fact make use of the idea of minimizing a master function $F$ , by combining it with Newton’s method applied to the full set of functions $F _ { i }$ . While such methods can still occasionally fail by coming to rest on a local minimum of $F$ , they often succeed where a direct attack via Newton’s method alone fails. The next section deals with these methods.

# CITED REFERENCES AND FURTHER READING:

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), Chapter 14.[1]   
Ostrowski, A.M. 1966, Solutions of Equations and Systems of Equations, 2nd ed. (New York: Academic Press).   
Ortega, J., and Rheinboldt, W. 1970, Iterative Solution of Nonlinear Equations in Several Variables (New York: Academic Press); reprinted 200o (Philadelphia: S.l.A.M.).

# 9.7 Globally Convergent Methods for Nonlinear Systems of Equations

We have seen that Newton’s method for solving nonlinear equations has an unfortunate tendency to wander off into the wild blue yonder if the initial guess is not sufficiently close to the root. A global method [1] would be one that converges to a solution from almost any starting point. Such global methods do exist for minimization problems; an example is the quasi-Newton method that we will describe in $\ S 1 0 . 9$ . In this section we will develop an algorithm that is an analogous quasi-Newton method for multidimensional root finding. Alas, while it is better behaved than Newton’s method, it is still not truly global.

What the method does do is combine the rapid local convergence of Newton’s method with a higher-level strategy that guarantees at least some progress at each step — either toward an actual root (usually), or else, hopefully rarely, toward the situation labeled “no root here!” in Figure 9.6.1. In the latter case, the method recognizes the problem and signals failure. By contrast, Newton’s method can bounce around forever, and you are never sure whether or not to quit.

Recall our discussion of $\ S 9 . 6$ : The Newton step for the set of equations

$$
\mathbf { F } ( \mathbf { x } ) = 0
$$

is

$$
{ \bf x } _ { \mathrm { n e w } } = { \bf x } _ { \mathrm { o l d } } + \delta { \bf x }
$$

where

$$
\delta \mathbf { x } = - \mathbf { J } ^ { - 1 } \cdot \mathbf { F }
$$

Here $\mathbf { J }$ is the Jacobian matrix. How do we decide whether to accept the Newton step $\delta \mathbf { x } ?$ A reasonable strategy is to require that the step decrease $| \mathbf { F } | ^ { 2 } = \mathbf { F } \cdot \mathbf { F }$ . This is the same requirement we would impose if we were trying to minimize

$$
\begin{array} { r } { f = \frac { 1 } { 2 } { \bf F } \cdot { \bf F } } \end{array}
$$

(The $\frac { 1 } { 2 }$ is for later convenience.) Every solution to (9.7.1) minimizes (9.7.4), but there may be local minima of (9.7.4) that are not solutions to (9.7.1). Thus, as already mentioned, simply applying one of our minimum-finding algorithms from Chapter 10 to (9.7.4) is not a good idea.

To develop a better strategy, note that the Newton step (9.7.3) is a descent direction for $f$ :

$$
\nabla f \cdot \delta \mathbf { x } = ( \mathbf { F } \cdot \mathbf { J } ) \cdot ( - \mathbf { J } ^ { - 1 } \cdot \mathbf { F } ) = - \mathbf { F } \cdot \mathbf { F } < 0
$$

Thus our strategy is quite simple: We always first try the full Newton step, because once we are close enough to the solution we will get quadratic convergence. However, we check at each iteration that the proposed step reduces $f$ . If not, we backtrack along the Newton direction until we have an acceptable step. Because the Newton step is a descent direction for $f$ , we are guaranteed to find an acceptable step by backtracking. We will discuss the backtracking algorithm in more detail below.

Note that this method minimizes $f$ only “incidentally,” either by taking Newton steps designed to bring $\mathbf { F }$ to zero, or by backtracking along such a step. The method is not equivalent to minimizing $f$ directly by taking Newton steps designed to bring $\nabla f$ to zero. While the method can nevertheless still fail by converging to a local minimum of $f$ that is not a root (as in Figure 9.6.1), this is quite rare in real applications. The routine newt below will warn you if this happens. The only remedy is to try a new starting point.

# 9.7.1 Line Searches and Backtracking

When we are not close enough to the minimum of $f$ , taking the full Newton step $\mathbf { p } = \delta \mathbf { x }$ need not decrease the function; we may move too far for the quadratic approximation to be valid. All we are guaranteed is that initially $f$ decreases as we move in the Newton direction. So the goal is to move to a new point $\mathbf { X } _ { \mathrm { n e w } }$ along the direction of the Newton step $\mathbf { p }$ , but not necessarily all the way:

$$
\begin{array} { r } { { \bf x } _ { \mathrm { n e w } } = { \bf x } _ { \mathrm { o l d } } + \lambda { \bf p } , \qquad 0 < \lambda \leq 1 \quad } \end{array}
$$

The aim is to find $\lambda$ so that $f ( \mathbf { x } _ { \mathrm { o l d } } + \lambda \mathbf { p } )$ has decreased sufficiently. Until the early 1970s, standard practice was to choose $\lambda$ so that $\mathbf { X } _ { \mathrm { n e w } }$ exactly minimizes $f$ in the direction $\mathbf { p }$ . However, we now know that it is extremely wasteful of function evaluations to do so. A better strategy is as follows: Since $\mathbf { p }$ is always the Newton direction in our algorithms, we first try $\lambda = \bar { 1 }$ , the full Newton step. This will lead to quadratic convergence when $\mathbf { X }$ is sufficiently close to the solution. However, if $f ( \mathbf { x } _ { \mathrm { n e w } } )$ does not meet our acceptance criteria, we backtrack along the Newton direction, trying a smaller value of $\lambda$ , until we find a suitable point. Since the Newton direction is a descent direction, we are guaranteed to decrease $f$ for sufficiently small $\lambda$ .

What should the criterion for accepting a step be? It is not sufficient to require merely that $f ( \mathbf { x } _ { \mathrm { n e w } } ) ~ < ~ f ( \mathbf { x } _ { \mathrm { o l d } } )$ . This criterion can fail to converge to a minimum of $f$ in one of two ways. First, it is possible to construct a sequence of steps satisfying this criterion with $f$ decreasing too slowly relative to the step lengths. Second, one can have a sequence where the step lengths are too small relative to the initial rate of decrease of $f$ . (For examples of such sequences, see [2], p. 117.)

A simple way to fix the first problem is to require the average rate of decrease of $f$ to be at least some fraction $\alpha$ of the initial rate of decrease $\nabla f \cdot \mathbf { p }$ :

$$
f ( \mathbf { x } _ { \mathrm { n e w } } ) \leq f ( \mathbf { x } _ { \mathrm { o l d } } ) + \alpha \nabla f \cdot ( \mathbf { x } _ { \mathrm { n e w } } - \mathbf { x } _ { \mathrm { o l d } } )
$$

Here the parameter $\alpha$ satisfies $0 \textless \alpha \textless 1$ . We can get away with quite small values of $\alpha$ ;   
$\alpha = 1 0 ^ { - 4 }$ is a good choice.

The second problem can be fixed by requiring the rate of decrease of $f$ at $\mathbf { X } _ { \mathrm { n e w } }$ to be greater than some fraction $\beta$ of the rate of decrease of $f$ at $\mathbf { X } _ { \mathrm { o l d } }$ . In practice, we will not need to impose this second constraint because our backtracking algorithm will have a built-in cutoff to avoid taking steps that are too small.

Here is the strategy for a practical backtracking routine: Define

$$
g ( \lambda ) \equiv f ( \mathbf { x } _ { \mathrm { o l d } } + \lambda \mathbf { p } )
$$

so that

$$
g ^ { \prime } ( \lambda ) = \nabla f \cdot \mathbf { p }
$$

If we need to backtrack, then we model $g$ with the most current information we have and choose $\lambda$ to minimize the model. We start with $g ( 0 )$ and $g ^ { \prime } ( 0 )$ available. The first step is always the Newton step, $\lambda = 1$ . If this step is not acceptable, we have available $g ( 1 )$ as well. We can therefore model $g ( \lambda )$ as a quadratic:

$$
g ( \lambda ) \approx [ g ( 1 ) - g ( 0 ) - g ^ { \prime } ( 0 ) ] \lambda ^ { 2 } + g ^ { \prime } ( 0 ) \lambda + g ( 0 )
$$

Taking the derivative of this quadratic, we find that it is a minimum when

$$
\lambda = - \frac { g ^ { \prime } ( 0 ) } { 2 [ g ( 1 ) - g ( 0 ) - g ^ { \prime } ( 0 ) ] }
$$

Since the Newton step failed, one can show that $\begin{array} { r } { \lambda \lesssim \frac { 1 } { 2 } } \end{array}$ for small $\alpha$ . We need to guard against too small a value of $\lambda$ , however. We set $\lambda _ { \mathrm { m i n } } = 0 . 1$ .

On second and subsequent backtracks, we model $g$ as a cubic in $\lambda$ , using the previous value $g ( \lambda _ { 1 } )$ and the second most recent value $g ( \lambda _ { 2 } )$ :

$$
g ( \lambda ) = a \lambda ^ { 3 } + b \lambda ^ { 2 } + g ^ { \prime } ( 0 ) \lambda + g ( 0 )
$$

Requiring this expression to give the correct values of $g$ at $\lambda _ { 1 }$ and $\lambda _ { 2 }$ gives two equations that can be solved for the coefficients $a$ and $b$ :

$$
\left[ \begin{array} { l } { a } \\ { b } \end{array} \right] = \frac { 1 } { \lambda _ { 1 } - \lambda _ { 2 } } \left[ \begin{array} { c c } { 1 / \lambda _ { 1 } ^ { 2 } } & { - 1 / \lambda _ { 2 } ^ { 2 } } \\ { - \lambda _ { 2 } / \lambda _ { 1 } ^ { 2 } } & { \lambda _ { 1 } / \lambda _ { 2 } ^ { 2 } } \end{array} \right] \cdot \left[ \begin{array} { c } { g ( \lambda _ { 1 } ) - g ^ { \prime } ( 0 ) \lambda _ { 1 } - g ( 0 ) } \\ { g ( \lambda _ { 2 } ) - g ^ { \prime } ( 0 ) \lambda _ { 2 } - g ( 0 ) } \end{array} \right]
$$

The minimum of the cubic (9.7.12) is at

$$
\lambda = \frac { - b + \sqrt { b ^ { 2 } - 3 a g ^ { \prime } ( 0 ) } } { 3 a }
$$

We enforce that $\lambda$ lie between $\lambda _ { \operatorname* { m a x } } = 0 . 5 \lambda _ { 1 }$ and $\lambda _ { \operatorname* { m i n } } = 0 . 1 \lambda _ { 1 }$

The routine has two additional features, a minimum step length alamin and a maximum step length stpmax. lnsrch will also be used in the quasi-Newton minimization routine dfpmin in the next section.

# template <class T>

void lnsrch(VecDoub_I &xold, const Doub fold, VecDoub_I &g, VecDoub_IO &p, VecDoub_O &x, Doub &f, const Doub stpmax, Bool &check, T &func) {

Given an $\mathbf { n } .$ -dimensional point xold[0..n-1], the value of the function and gradient there, fold and $\mathtt { g } [ 0 \ldots \mathtt { n - 1 } ]$ , and a direction $\mathfrak { p } \left[ 0 \ldots \mathbf { n } ^ { - 1 } \right]$ , finds a new point $\mathbf { x } \left[ 0 \ldots \ldots \right] $ along the direction $\mathtt { p }$ from xold where the function or functor func has decreased “sufficiently.” The new function value is returned in f. stpmax is an input quantity that limits the length of the steps so that you do not try to evaluate the function in regions where it is undefined or subject to overflow. p is usually the Newton direction. The output quantity check is false on a normal exit. It is true when $\mathbf { x }$ is too close to xold. In a minimization algorithm, this usually signals convergence and can be ignored. However, in a zero-finding algorithm the calling program should check whether the convergence is spurious.

const Doub $\mathrm { A L F } { = } 1$ .0e-4, TOLX=numeric_limits<Doub>::epsilon();

ALF ensures sufficient decrease in function value; TOLX is the convergence criterion on $\Delta x$

Doub a,alam,alam2 $_ { = 0 }$ .0,alamin,b,disc,f2=0.0;   
Doub rhs1,rhs2,slope $\scriptstyle = 0$ .0,sum $_ { = 0 }$ .0,temp,test,tmplam; Int i, $\mathbf { n } =$ xold.size();   
check=false;   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<n; $\mathrm { i } + + \mathrm { j }$ ) sum $+ =$ p[i]\*p[i];   
sum=sqrt(sum);   
if (sum $>$ stpmax)   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<n;i++)

p[i] $\ast =$ stpmax/sum; Scale if attempted step is too big. for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n; $\dot { \bar { 1 } } + + \dot { bar { 1 } }$ ) slope $+ =$ g[i]\*p[i]; if (slope $> = \ 0 . 0 \dot { } .$ ) throw("Roundoff problem in lnsrch."); test ${ = } 0$ .0; Compute $\lambda _ { \operatorname* { m i n } }$ . for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n; $\dot { 1 } + +$ ) { temp=abs(p[i])/MAX(abs(xold[i]),1.0); if (temp $>$ test) test $=$ temp; } alamin $\boldsymbol { \cdot }$ TOLX/test; alam $= 1$ .0; Always try full Newton step first. for (;;) { Start of iteration loop. for (i=0;i<n;i++) x[i] $=$ xold[i]+alam\*p[i]; f=func(x); if (alam $<$ alamin) { Convergence on $\Delta x$ . For zero findfor ( $\mathtt { i } = 0$ ;i<n;i++) x[i] $\equiv$ xold[i]; ing, the calling program should check=true; verify the convergence. return; } else if $\mathrm { ~ \bf ~ \underline { ~ } { ~ f ~ } ~ } < =$ fold+ALF\*alam\*slope) return; Sufficient function decrease. else { Backtrack. if (alam $\scriptstyle = = ~ 1 . 0 )$ tmplam $=$ -slope/(2.0\*(f-fold-slope)); First time. else { Subsequent backtracks. rhs1 $=$ f-fold-alam\*slope; rhs2=f2-fold-alam2\*slope; $\mathtt { a } =$ (rhs1/(alam\*alam)-rhs2/(alam2\*alam2))/(alam-alam2); $\mathtt { b } =$ (-alam2\*rhs1/(alam\*alam)+alam\*rhs2/(alam2\*alam2))/(alam-alam2); if ( $\texttt { a } = 0 . 0 \rangle$ tmplam $=$ -slope/(2.0\*b); else { disc=b\*b-3.0\*a\*slope; if (disc $<$ 0.0) tmplam $_ { 1 = 0 }$ . $^ { 5 * }$ alam; else if (b $< =$ 0.0) tmplam $\cdot ^ { = }$ (-b+sqrt(disc))/(3. $^ { 0 * } \mathtt { a } )$ ; else tmplam=-slope/(b+sqrt(disc)); } if (tmplam>0. $^ { 5 \ast }$ alam) tmplam=0.5\*alam; $\lambda \le 0 . 5 \lambda _ { 1 } .$ . } alam2 $\Bumpeq$ alam; $\pounds _ { 2 } \ = \ \mathrm { f }$ ; alam=MAX(tmplam,0.1\*alam); $\lambda \ge 0 . 1 \lambda _ { 1 }$ . } Try again.

# 9.7.2 Globally Convergent Newton Method

Using the above results on backtracking, here is the globally convergent Newton routine newt that uses lnsrch. A feature of newt is that you need not supply the Jacobian matrix analytically; the routine will attempt to compute the necessary partial derivatives of $\mathbf { F }$ by finite differences in the routine NRfdjac. This routine uses some of the techniques described in $\ S 5 . 7$ for computing numerical derivatives. Of course, you can always replace NRfdjac with a routine that calculates the Jacobian analytically if this is easy for you to do.

The routine requires a user-supplied function or functor that computes the vector of functions to be zeroed. Its declaration as a function is

# VecDoub vecfunc(VecDoub_I x);

(The name vecfunc is arbitrary.) The declaration as a functor is similar.

# template <class T>

# void newt(VecDoub_IO &x, Bool &check, T &vecfunc) {

Given an initial guess x[0..n-1] for a root in n dimensions, find the root by a globally convergent Newton’s method. The vector of functions to be zeroed, called fvec[0..n-1] in the routine below, is returned by the user-supplied function or functor vecfunc (see text). The output quantity check is false on a normal return and true if the routine has converged to a local minimum of the function fmin defined below. In this case try restarting from a different initial guess.

const Doub TOLF $\spadesuit = 1$ .0e-8,TOLMIN $\sp { \prime } = 1$ .0e-12,STPMX 100.0;   
const Doub TOLX $\cdot ^ { = }$ numeric_limits<Doub>::epsilon();   
Here MAXITS is the maximum number of iterations; TOLF sets the convergence criterion on   
function values; TOLMIN sets the criterion for deciding whether spurious convergence to a   
minimum of fmin has occurred; STPMX is the scaled maximum step length allowed in line   
searches; and TOLX is the convergence criterion on ${ \boldsymbol { \delta \mathbf { x } } }$ .   
Int i,j,its, $\mathbf { n } { = } \mathbf { x }$ .size();   
Doub den,f,fold,stpmax,sum,temp,test;   
VecDoub g(n),p(n),xold(n);   
MatDoub fjac(n,n);   
NRfmin<T> fmin(vecfunc); Set up NRfmin object.   
NRfdjac<T> fdjac(vecfunc); Set up NRfdjac object.   
VecDoub &fvec=fmin.fvec; Make an alias to simplify coding.   
$\mathbf { f } =$ fmin(x); fvec is also computed by this call.   
test ${ = } 0$ .0; Test for initial guess being a root. Use   
for (i=0;i<n;i++) more stringent test than simply TOLF. if (abs(fvec[i]) > test) test $=$ abs(fvec[i]);   
if (test $<$ 0.01\*TOLF) { check=false; return;   
}   
sum $_ { 1 = 0 }$ .0;   
for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<n;i++) sum $+ =$ SQR(x[i]); Calculate stpmax for line searches.   
stpmax STPMX\*MAX(sqrt(sum),Doub(n));   
for (its ${ = } 0$ ;its<MAXITS;its $^ { + + }$ ) { Start of iteration loop. fjac=fdjac(x,fvec); If analytic Jacobian is available, you can replace the struct NRfdjac below with your own struct. for (i=0;i<n;i++) { Compute $\nabla f$ for the line search. sum $= 0$ .0; for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<n;j++) sum $+ =$ fjac[j][i]\*fvec[j]; g[i] $=$ sum; } for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) xold[i] $= \mathrm { x }$ [i]; Store $\mathbf { x }$ , fold=f; and $f$ . for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) p[i] $=$ -fvec[i]; Right-hand side for linear equations. LUdcmp alu(fjac); Solve linear equations by $_ { L U }$ decompoalu.solve(p,p); sition. lnsrch(xold,fold,g,p,x,f,stpmax,check,fmin); lnsrch returns new x and $f$ . It also calculates fvec at the new $\mathbf { x }$ when it calls fmin.   
test ${ = } 0$ .0; Test for convergence on function values.   
for (i=0;i<n;i++) if (abs(fvec[i]) $>$ test) test=abs(fvec[i]);   
if (test $<$ TOLF) { check=false; return;   
}   
if (check) { Check for gradient of $f$ zero, i.e., sputest=0.0; rious convergence. den=MAX(f,0.5\*n); for ( $\mathtt { i } = 0$ ;i<n;i++) { temp=abs(g[i])\*MAX(abs(x[i]),1.0)/den; if (temp $>$ test) test=temp; }

check=(test $<$ TOLMIN); return; } test=0.0; Test for convergence on ${ \displaystyle \delta \mathbf { x } }$ . for (i=0;i<n;i++) { temp $\mid =$ (abs(x[i]-xold[i]))/MAX(abs(x[i]),1.0); if (temp $>$ test) test=temp; } if (test $<$ TOLX) return; } throw("MAXITS exceeded in newt");

template <class T>   
struct NRfdjac {   
Computes forward-difference approximation to Jacobian. const Doub EPS; Set to approximate square root of the machine pre-T &func; cision. NRfdjac(T &funcc) : EPS(1.0e-8),func(funcc) {} Initialize with user-supplied function or functor that returns the vector of functions to be zeroed. MatDoub operator() (VecDoub_I &x, VecDoub_I &fvec) { Returns the Jacobian array df[0..n-1][0..n-1]. On input, $\mathbf { x } \left[ 0 \ldots \ldots \right]$ is the point at which the Jacobian is to be evaluated and fvec[0..n-1] is the vector of function values at the point.

Int $\mathbf { n } { = } \mathbf { x }$ .size(); MatDoub df(n,n); VecDoub xh=x; for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<n;j++) { Doub temp=xh[j]; Doub $\mathtt { h } =$ EPS\*abs(temp); if $\mathrm { ~ \mathit ~ { ~ L ~ } ~ } = = \mathrm { ~ \mathit ~ { ~ O ~ . ~ 0 ~ } ~ }$ ) h=EPS; xh[j] $=$ temp+h; Trick to reduce finite-precision error. $\mathrm { h } =$ xh[j]-temp; VecDoub $\mathtt { f } =$ func(xh); xh[j] $=$ temp; for (Int $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) Forward difference formula. df[i][j] $=$ (f[i]-fvec[i])/h; return df; } };

template <class T>   
struct NRfmin {   
Returns $\begin{array} { r } { f = \frac { 1 } { 2 } { \bf F } \cdot { \bf F } } \end{array}$ . Also stores value of $\mathbf { F }$ in fvec. VecDoub fvec; T &func; Int n; NRfmin(T &funcc) : func(funcc){} Initialize with user-supplied function or functor that returns the vector of functions to be zeroed. Doub operator() (VecDoub_I &x) { Returns $f$ at $\mathbf { x }$ , and stores $\mathbf { F } ( \mathbf { x } )$ in fvec. $\mathrm { n } { = } \mathrm { x }$ .size(); Doub sum ${ = } 0$ ; fvec=func(x); for (Int $\scriptstyle { \dot { 1 } } = 0$ ;i<n; $\mathrm { i } + +$ ) sum $+ =$ SQR(fvec[i]); return $0 , 5 *$ sum; }   
};

The routine newt assumes that the typical values of all components of $\mathbf { X }$ and of $\mathbf { F }$ are of order unity, and it can fail if this assumption is badly violated. You should rescale the variables by their typical values before invoking newt if this problem occurs.

# 9.7.3 Multidimensional Secant Methods: Broyden's Method

Newton’s method as implemented above is quite powerful, but it still has several disadvantages. One drawback is that the Jacobian matrix is needed. In many problems analytic derivatives are unavailable. If function evaluation is expensive, then the cost of finite difference determination of the Jacobian can be prohibitive.

Just as the quasi-Newton methods to be discussed in $\ S 1 0 . 9$ provide cheap approximations for the Hessian matrix in minimization algorithms, there are quasi-Newton methods that provide cheap approximations to the Jacobian for zero finding. These methods are often called secant methods, since they reduce to the secant method $( \ S 9 . 2 )$ in one dimension (see, e.g., [2]). The best of these methods still seems to be the first one introduced, Broyden’s method [3].

Let us denote the approximate Jacobian by $\mathbf { B }$ . Then the $i$ th quasi-Newton step $\delta \mathbf { x } _ { i }$ is the solution of

$$
\mathbf { B } _ { i } \cdot \delta \mathbf { x } _ { i } = - \mathbf { F } _ { i }
$$

where $\delta \mathbf { x } _ { i } = \mathbf { x } _ { i + 1 } - \mathbf { x } _ { i }$ (cf. equation 9.7.3). The quasi-Newton or secant condition is that $\mathbf { B } _ { i + 1 }$ satisfy

$$
\mathbf { B } _ { i + 1 } \cdot \delta \mathbf { x } _ { i } = \delta \mathbf { F } _ { i }
$$

where $\delta \mathbf { F } _ { i } = \mathbf { F } _ { i + 1 } - \mathbf { F } _ { i }$ . This is the generalization of the one-dimensional secant approximation to the derivative, $\delta F / \delta x$ . However, equation (9.7.16) does not determine $\mathbf { B } _ { i + 1 }$ uniquely in more than one dimension.

Many different auxiliary conditions to pin down $\mathbf { B } _ { i + 1 }$ have been explored, but the bestperforming algorithm in practice results from Broyden’s formula. This formula is based on the idea of getting $\mathbf { B } _ { i + 1 }$ by making the least change to $\mathbf { B } _ { i }$ consistent with the secant equation (9.7.16). Broyden showed that the resulting formula is

$$
\mathbf { B } _ { i + 1 } = \mathbf { B } _ { i } + { \frac { ( \delta \mathbf { F } _ { i } - \mathbf { B } _ { i } \cdot \delta \mathbf { x } _ { i } ) \otimes \delta \mathbf { x } _ { i } } { \delta \mathbf { x } _ { i } \cdot \delta \mathbf { x } _ { i } } }
$$

You can easily check that $\mathbf { B } _ { i + 1 }$ satisfies (9.7.16).

Early implementations of Broyden’s method used the Sherman-Morrison formula, equation (2.7.2), to invert equation (9.7.17) analytically,

$$
\mathbf { B } _ { i + 1 } ^ { - 1 } = \mathbf { B } _ { i } ^ { - 1 } + \frac { ( \delta \mathbf { x } _ { i } - \mathbf { B } _ { i } ^ { - 1 } \cdot \delta \mathbf { F } _ { i } ) \otimes \delta \mathbf { x } _ { i } \cdot \mathbf { B } _ { i } ^ { - 1 } } { \delta \mathbf { x } _ { i } \cdot \mathbf { B } _ { i } ^ { - 1 } \cdot \delta \mathbf { F } _ { i } }
$$

Then, instead of solving equation (9.7.3) by, e.g., $L U$ decomposition, one determined

$$
\delta \mathbf { x } _ { i } = - \mathbf { B } _ { i } ^ { - 1 } \cdot \mathbf { F } _ { i }
$$

by matrix multiplication in $O ( N ^ { 2 } )$ operations. The disadvantage of this method is that it cannot easily be embedded in a globally convergent strategy, for which the gradient of equation (9.7.4) requires $\mathbf { B }$ , not $\mathbf { B } ^ { - 1 }$ ,

$$
\nabla ( \frac { 1 } { 2 } { \bf F } \cdot { \bf F } ) \simeq { \bf B } ^ { T } \cdot { \bf F }
$$

Accordingly, we implement the update formula in the form (9.7.17).

However, we can still preserve the $O ( N ^ { 2 } )$ solution of (9.7.3) by using $\mathcal Q R$ decomposition $( \ S 2 . 1 0 )$ instead of $L U$ decomposition. The reason is that because of the special form of equation (9.7.17), the $\mathcal Q R$ decomposition of $\mathbf { B } _ { i }$ can be updated into the $\mathcal Q R$ decomposition of $\mathbf { B } _ { i + 1 }$ in $O ( N ^ { 2 } )$ operations $( \ S 2 . 1 0 )$ . All we need is an initial approximation ${ \bf B } _ { 0 }$ to start the ball rolling. It is often acceptable to start simply with the identity matrix, and then allow $O ( N )$

updates to produce a reasonable approximation to the Jacobian. We prefer to spend the first $N$ function evaluations on a finite difference approximation to initialize $\mathbf { B }$ via a call to NRfdjac.

Since $\mathbf { B }$ is not the exact Jacobian, we are not guaranteed that $\&$ is a descent direction for $\begin{array} { r } { f = \frac { 1 } { 2 } { \bf F } \cdot { \bf F } } \end{array}$ (cf. equation 9.7.5). Thus the line search algorithm can fail to return a suitable step if $\mathbf { B }$ wanders far from the true Jacobian. In this case, we reinitialize $\mathbf { B }$ by another call to NRfdjac.

Like the secant method in one dimension, Broyden’s method converges superlinearly once you get close enough to the root. Embedded in a global strategy, it is almost as robust as Newton’s method, and often needs far fewer function evaluations to determine a zero. Note that the final value of $\mathbf { B }$ is not always close to the true Jacobian at the root, even when the method converges.

The routine broydn, given below, is very similar to newt in organization. The principal differences are the use of $\mathcal Q R$ decomposition instead of $L U$ , and the updating formula instead of directly determining the Jacobian. The remarks at the end of newt about scaling the variables apply equally to broydn.

# template <class T>

# void broydn(VecDoub_IO &x, Bool &check, T &vecfunc) {

Given an initial guess $\mathbf { x } \left[ 0 \ldots \mathbf { n - 1 } \right]$ for a root in n dimensions, find the root by Broyden’s method embedded in a globally convergent strategy. The vector of functions to be zeroed, called fvec[0..n-1] in the routine below, is returned by the user-supplied function or functor vecfunc. The routines NRfdjac and NRfmin from newt are used. The output quantity check is false on a normal return and true if the routine has converged to a local minimum of the function fmin or if Broyden’s method can make no further progress. In this case try restarting from a different initial guess.

const Int MAXITS $=$ 200;   
const Doub EPS=numeric_limits<Doub>::epsilon();   
const Doub TOLF $\ l = 1$ .0e-8, TOLX $\ c =$ EPS, STPMX $\cdot ^ { = }$ 100.0, TOLMIN $\sp { \prime } = 1$ .0e-12;   
Here MAXITS is the maximum number of iterations; EPS is the machine precision; TOLF   
is the convergence criterion on function values; TOLX is the convergence criterion on ${ \displaystyle \delta \mathbf { x } }$ ;   
STPMX is the scaled maximum step length allowed in line searches; and TOLMIN is used to   
decide whether spurious convergence to a minimum of fmin has occurred.   
Bool restrt,skip;   
Int i,its,j, $\mathbf { n } { = } \mathbf { x }$ .size();   
Doub den,f,fold,stpmax,sum,temp,test;   
VecDoub fvcold(n),g(n),p(n),s(n),t(n),w(n),xold(n);   
QRdcmp \*qr;   
NRfmin<T> fmin(vecfunc); Set up NRfmin object.   
NRfdjac<T> fdjac(vecfunc); Set up NRfdjac object.   
VecDoub &fvec=fmin.fvec; Make an alias to simplify coding.   
$\mathtt { f } =$ fmin(x); The vector fvec is also computed by this   
test ${ = } 0$ .0; call.   
for (i=0;i<n;i++) Test for initial guess being a root. Use more if (abs(fvec[i]) $>$ test) test ${ } _ { , } = { }$ abs(fvec[i]); stringent test than sim  
if (test $<$ 0.01\*TOLF) { ply TOLF. check $\left. \vert = \right.$ false; return;   
}   
for (sum $_ { 1 = 0 }$ .0, $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) sum $+ =$ SQR(x[i]); Calculate stpmax for line searches.   
stpmax $: =$ STPMX\*MAX(sqrt(sum),Doub(n));   
restrt=true; Ensure initial Jacobian gets computed.   
for (its $= 1$ ;its $< =$ MAXITS;its $^ { + + }$ ) { Start of iteration loop. if (restrt) { Initialize or reinitialize Jacobian and $Q R$ deqr=new QRdcmp(fdjac(x,fvec)); compose it. if (qr->sing) throw("singular Jacobian in broydn"); } else { Carry out Broyden update. for (i=0;i<n;i++) s[i] $= \mathrm { x }$ [i]-xold[i]; $\mathbf { s } = \delta \mathbf { x }$ . for ( $\mathtt { i } = 0$ ;i<n;i++) { $\mathbf { t } = \mathbf { R } \cdot \mathbf { s } .$ . for (sum $_ { = 0 }$ .0, $\scriptstyle { \dot { \mathsf { J } } } = { \dot { \mathsf { I } } }$ ;j<n;j++) sum $+ =$ qr->r[i][j] $^ { * } \mathtt { s }$ [j]; t[i] $=$ sum; } skip $\mid =$ true; w[i]=fvec[i]-fvcold[i]-sum; if (abs(w[i]) >= EPS\*(abs(fvec[i]) $^ +$ abs(fvcold[i]))) skip=false; Don’t update with noisy components of $\mathbf { w }$ . else w[i]=0.0; } if (!skip) { qr->qtmult(w,t); $\mathbf { t } = \mathbf { Q } ^ { T } \cdot \mathbf { w } .$ for (den $_ { = 0 }$ .0, $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) den $+ =$ SQR(s[i]); for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n; $\dot { \bf 1 } + +$ ) s[i] $/ { = }$ den; Store ${ \bf s } / ( { \bf s } \cdot { \bf s } )$ in $\tt s$ . qr->update(t,s); Update $\mathbf { R }$ and $\mathbf { Q } ^ { T }$ if (qr->sing) throw("singular update in broydn"); }   
}   
qr->qtmult(fvec,p);   
for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<n;i++) Right-hand side for linear equations is $- \mathbf { Q } ^ { T } \cdot \mathbf { F }$ . p[i] $=$ -p[i];   
for (i=n-1; $\scriptstyle \dot { 1 } > = 0$ ;i--) { Compute $\nabla f \approx ( \mathbf { Q } \cdot \mathbf { R } ) ^ { T } \cdot \mathbf { F }$ for the line search. for (sum $_ { 1 = 0 }$ .0,j=0;j $< = \pm$ ;j $^ { + + }$ ) sum $- = \mathrm {  ~ \ q r ^ { - } } > _ { \Sigma }$ [j][i]\*p[j]; g[i] $=$ sum;   
}   
for (i=0;i<n;i++) { Store $\mathbf { x }$ and $\mathbf { F }$ . xold[i] $= \mathbf { x }$ [i]; fvcold[i]=fvec[i];   
fold=f; Store $f$ .   
qr->rsolve(p,p); Solve linear equations.   
lnsrch(xold,fold,g,p,x,f,stpmax,check,fmin);   
lnsrch returns new x and $f$ . It also calculates fvec at the new $\mathbf { x }$ when it calls fmin.   
test ${ = } 0$ .0; Test for convergence on function values.   
for (i=0;i<n;i++) if (abs(fvec[i]) $>$ test) test=abs(fvec[i]);   
if (test $<$ TOLF) { check=false; delete qr; return;   
}   
if (check) { True if line search failed to find a new $\mathbf { x }$ . if (restrt) { Failure; already tried reinitializing the Jacobian. delete qr; return; } else { test ${ = } 0$ .0; Check for gradient of $f$ zero, i.e., spurious conden $\cdot ^ { = }$ MAX(f,0.5\*n); vergence. for ( $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) { temp=abs(g[i])\*MAX(abs(x[i]),1.0)/den; if (temp $>$ test) test=temp; if (test $<$ TOLMIN) { delete qr; return; } else restrt $=$ true; Try reinitializing the Jacobian. }   
} else { Successful step; will use Broyden update for next restrt=false; step. test=0.0; Test for convergence on ${ \displaystyle \delta \mathbf { x } }$ . for ( $\mathtt { i } = 0$ ;i<n;i++) { temp $\mid =$ (abs(x[i]-xold[i]))/MAX(abs(x[i]),1.0); if (temp $>$ test) test $=$ temp; } if (test < TOLX) { delete qr; return; } }   
  
throw("MAXITS exceeded in broydn");

# 9.7.4 More Advanced Implementations

One of the principal ways that the methods described so far can fail is if $\mathbf { J }$ (in Newton’s method) or $\mathbf { B }$ in (Broyden’s method) becomes singular or nearly singular, so that $\&$ cannot be determined. If you are lucky, this situation will not occur very often in practice. Methods developed so far to deal with this problem involve monitoring the condition number of $\mathbf { J }$ and perturbing $\mathbf { J }$ if singularity or near singularity is detected. This is most easily implemented if the $\mathcal Q R$ decomposition is used instead of $L U$ in Newton’s method (see [2] for details). Our personal experience is that, while such an algorithm can solve problems where $\mathbf { J }$ is exactly singular and the standard Newton method fails, it is occasionally less robust on other problems where $L U$ decomposition succeeds. Clearly implementation details involving roundoff, underflow, etc., are important here and the last word is yet to be written.

Our global strategies both for minimization and zero finding have been based on line searches. Other global algorithms, such as the hook step and dogleg step methods, are based instead on the model-trust region approach, which is related to the Levenberg-Marquardt algorithm for nonlinear least squares (-15.5). While somewhat more complicated than line searches, these methods have a reputation for robustness even when starting far from the desired zero or minimum [2].

# CITED REFERENCES AND FURTHER READING:

Deuflhard, P. 2004, Newton Methods for Nonlinear Problems (Berlin: Springer).[1]   
Dennis, J.E., and Schnabel, R.B. 1983, Numerical Methods for Unconstrained Optimization and Nonlinear Equations; reprinted 1996 (Philadelphia: S.I.A.M.).[2]   
Broyden, C.G. 1965, “A Class of Methods for Solving Nonlinear Simultaneous Equations,” Mathematics of Computation, vol.19,pp.577-593.[3]

# Minimization or Maximization of Functions

# CHAPTER 10

# 10.0 Introduction

In a nutshell: You are given a single function $f$ that depends on one or more independent variables. You want to find the value of those variables where $f$ takes on a maximum or a minimum value. You can then calculate what value of $f$ is achieved at the maximum or minimum. The tasks of maximization and minimization are trivially related to each other, since one person’s function $f$ could just as well be another’s $- f$ . The computational desiderata are the usual ones: Do it quickly, cheaply, and in small memory. Often the computational effort is dominated by the cost of evaluating $f$ (and also perhaps its partial derivatives with respect to all variables, if the chosen algorithm requires them). In such cases the desiderata are sometimes replaced by the simple surrogate: Evaluate $f$ as few times as possible.

An extremum (maximum or minimum point) can be either global (truly the highest or lowest function value) or local (the highest or lowest in a finite neighborhood and not on the boundary of that neighborhood). (See Figure 10.0.1.) Finding a global extremum is, in general, a very difficult problem. Two standard heuristics are widely used: (i) Find local extrema starting from widely varying starting values of the independent variables (perhaps chosen quasi-randomly, as in $\ S 7 . 8 )$ , and then pick the most extreme of these (if they are not all the same); or (ii) perturb a local extremum by taking a finite amplitude step away from it, and then see if your routine returns you to a better point, or “always” to the same one. More recently, so-called simulated annealing methods (-10.12) have demonstrated important successes on a variety of global extremization problems.

Our chapter title could just as well be optimization, which is the usual name for this very large field of numerical research. The importance ascribed to the various tasks in this field depends strongly on the particular interests of whom you talk to. Economists, and some engineers, are particularly concerned with constrained optimization, where there are a priori limitations on the allowed values of independent variables. For example, the production of wheat in the United States must be a nonnegative number. One particularly well-developed area of constrained optimization is linear programming, where both the function to be optimized and the constraints happen to be linear functions of the independent variables. Sections 10.10 and 10.11, which are otherwise somewhat disconnected from the rest of the material that we have chosen to include in this chapter, discuss the two major approaches to such problems, the so-called simplex algorithm and interior-point methods.

![](images/83199decde8d7712dcb40117893af34022229efc530bf249c4b8b7e033cfed74.jpg)  
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

![](images/5fde25ee5cccabdb18b2fc7dc418870cfd543f14a89ee8b52af5294b554a1c45.jpg)  
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

![](images/5372286af901df7d15d03db9b41538f7b686fa71e7aab732147a8d22cfd8b9ff.jpg)  
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

![](images/628c51c22228232a1a3418549fc9eef7566cd8552f3a8dd5bc0f2d59350f9c2f.jpg)  
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

![](images/0f95fd46687b8ee9b82ed10b3c5a3c1989a835a012a4116bcf8442cc15f8f43b.jpg)  
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

![](images/50c764c62eb96427d67b85f3291fd0ba39bc8f3cd274ed6af29dadb611ba857b.jpg)  
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

![](images/29a6ebed72346b36c767d7647d6ea5f7cec2657c7914c948414076ff69c063cd.jpg)  
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

![](images/524671d61b195e00e9f7387d866eb729ebc5c6be2c6d86bed540c357d57b2681.jpg)  
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