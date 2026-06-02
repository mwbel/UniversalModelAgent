bn=bet/n; $x 1 = ( 1 \mathrm { ~ . ~ 0 + a 1 f ~ } ) * ( 2 \mathrm { ~ . ~ 7 8 / ( 4 \mathrm { ~ . ~ 0 + n * n } ) + 0 \mathrm { ~ . ~ 7 6 8 * a n / n ) } \mathrm { ~ ; } }$ ; r2=1. $0 { + 1 }$ .48\*an+0.96\*bn+0.452\*an\*an+0.83\*an\*bn; $z { = } 1$ .0-r1/r2;   
} else if ( $\scriptstyle { \mathrm { ~ i ~ } } = = { \mathrm { ~ 1 ~ } }$ ) { Initial guess for the second largest root. $\Gamma \mathrm { 1 = ( 4 . 1 \mathrm { + } a l f ) / ( ( 1 . 0 \mathrm { + } a l f ) * ( 1 . 0 \mathrm { + } 0 . 1 5 6 \mathrm { * } a l f ) ) ; }$ $\mathbf { r } 2 { = } 1 \ldots 0 { + } 0 \ldots 0 6 * \left( \mathbf { n } { - } 8 \ldots 0 \right) * \left( 1 \ldots 0 { + } 0 \ldots 1 2 { * } { \mathrm { a l f } } \right) / \mathbf { n } ;$ r3=1.0+0.012\*bet\*(1.0+0.25\*abs(alf))/n; $\mathrm { ~ z ~ } \mathrm { ~ -- ~ } ( 1 \mathrm { ~ . ~ } 0 \mathrm { - } \mathrm { z } ) \ast \mathrm { r } 1 \ast \mathrm { r } 2 \ast \mathrm { r } 3$ ;   
} else if ( $\\scriptstyle { \dot { \overline { { 1 } } } } \ = = \ 2 $ ) { Initial guess for the third largest root. r1=(1.67+0.28\*alf)/(1. $0 { + } 0$ .37\*alf); ${ \bf r } 2 { \bf = } 1 \mathrm { . } 0 + 0 \mathrm { . } 2 2 * ( \mathrm { n } - 8 \mathrm { . } 0 ) / \mathrm { n } \mathrm { ; }$ r3=1.0+8.0\*bet/((6.28+bet)\*n\*n); $\mathbf { \Sigma } _ { \subset } \ - \ \mathbf { \Sigma } ( \mathbf { x } \left[ 0 \right] - \mathbf { z } ) { * \mathbf { r } \mathbf { 1 } * \mathbf { r } 2 * \mathbf { r } 3 }$ ;   
} else if ( $\mathrm { ~ i ~ } = = \mathrm { ~ n } { - } 2 )$ ) { Initial guess for the second smallest root. r1=(1.0+0.235\*bet)/(0.766+0.119\*bet); r2=1.0/(1.0+0.639\*(n-4.0)/(1.0+0.71\*(n-4.0))); r3=1.0/(1.0+20.0\*alf/((7.5+alf)\*n\*n)); z += (z-x[n-4])\*r1\*r2\*r3;   
} else if ( $\mathrm { ~ i ~ } = = \mathrm { ~ n - 1 } )$ { Initial guess for the smallest root. r1=(1.0+0.37\*bet)/(1.67+0.28\*bet); $\mathbf { r } 2 { = } 1$ .0/(1.0+0.22\*(n-8.0)/n); $\scriptstyle x 3 = 1$ .0/(1.0+8.0\*alf/((6.28+alf) $\ast \mathtt { n } \ast \mathtt { n } .$ )); z += (z-x[n-3])\*r1\*r2\*r3;   
} else { Initial guess for the other roots. z=3.0\*x[i-1]-3.0\*x[i-2]+x[i-3];   
1   
alfbet $=$ alf+bet;   
for (its ${ = } 1$ ;its $< =$ MAXIT;its $^ { + + }$ ) { Refinement by Newton’s method. temp $^ { + 2 }$ .0+alfbet; Start the recurrence with $P _ { 0 }$ and $P _ { 1 }$ to avoid p1=(alf-bet+temp\*z)/2.0; a division by zero when $\alpha + \beta = 0$ or $\mathtt { p } 2 \mathtt { = } 1$ .0; $^ { - 1 }$ . for ( $\scriptstyle { \dot { \mathsf { J } } } = 2$ ;j $< = \mathtt { n }$ ;j++) { Loop up the recurrence relation to get the p3=p2; Jacobi polynomial evaluated at $_ { z }$ . p2=p1; temp $^ { \prime = 2 \ast }$ j+alfbet; a=2\*j\*(j+alfbet)\*(temp-2.0); b=(temp-1.0)\*(alf\*alf-bet\*bet+temp\*(temp-2.0)\*z); c=2.0\*(j-1+alf)\*(j-1+bet)\*temp; p1=(b\*p2-c\*p3)/a; } pp=(n\*(alf-bet-temp\*z)\*p1+2. $^ { 0 * }$ (n+alf)\*(n+bet)\*p2)/(temp\*(1.0-z\*z)); p1 is now the desired Jacobi polynomial. We next compute pp, its derivative, by a standard relation involving also p2, the polynomial of one lower order. $z 1 = z$ ; z=z1-p1/pp; Newton’s formula. if (abs(z-z1) $< =$ EPS) break;   
if (its $>$ MAXIT) throw("too many iterations in gaujac");   
$\mathbf { x } \left[ \mathbf { i } \right] = \mathbf { z }$ ; Store the root and the weight.   
w[i] $=$ exp(gammln(alf $+ \mathtt { n }$ )+gammln(bet+n)-gammln(n+1.0)- gammln(n+alfbet+1.0))\*temp\*pow(2.0,alfbet)/(pp\*p2);

Legendre polynomials are special cases of Jacobi polynomials with $\alpha = \beta = 0$ , but it is worth having the separate routine for them, gauleg, given above. Chebyshev polynomials correspond to $\alpha = \beta = - 1 / 2$ (see $\ S 5 . 8 )$ . They have analytic abscissas and weights:

$$
\begin{array} { l } { { x _ { j } = \cos \left( { \frac { \pi ( j + { \frac { 1 } { 2 } } ) } { N } } \right) } } \\ { { w _ { j } = { \cfrac { \pi } { N } } } } \end{array}
$$

# 4.6.2 Case of Known Recurrences

Turn now to the case where you do not know good initial guesses for the zeros of your orthogonal polynomials, but you do have available the coefficients $a _ { j }$ and $b _ { j }$ that generate them. As we have seen, the zeros of $p _ { N } ( x )$ are the abscissas for the $N$ -point Gaussian quadrature formula. The most useful computational formula for the weights is equation (4.6.9) above, since the derivative $p _ { N } ^ { \prime }$ can be efficiently computed by the derivative of (4.6.6) in the general case, or by special relations for the classical polynomials. Note that (4.6.9) is valid as written only for monic polynomials; for other normalizations, there is an extra factor of $\lambda _ { N } / \lambda _ { N - 1 }$ , where $\lambda _ { N }$ is the coefficient of $x ^ { N }$ in $p _ { N }$ .

Except in those special cases already discussed, the best way to find the abscissas is not to use a root-finding method like Newton’s method on $p _ { N } ( x )$ . Rather, it is generally faster to use the Golub-Welsch [3] algorithm, which is based on a result of Wilf [4]. This algorithm notes that if you bring the term $x p _ { j }$ to the left-hand side of (4.6.6) and the term $p _ { j + 1 }$ to the right-hand side, the recurrence relation can be written in matrix form as

$$
x \left[ \begin{array} { c } { p _ { 0 } } \\ { p _ { 1 } } \\ { \vdots } \\ { p _ { N - 2 } } \\ { p _ { N - 1 } } \end{array} \right] = \left[ \begin{array} { c c c c c c } { a _ { 0 } } & { 1 } & & & & \\ { b _ { 1 } } & { a _ { 1 } } & { 1 } & & & \\ & { \vdots } & { \vdots } & & & \\ & & & { b _ { N - 2 } } & { a _ { N - 2 } } & { 1 } \\ & & & & { b _ { N - 1 } } & { a _ { N - 1 } } \end{array} \right] \cdot \left[ \begin{array} { c } { p _ { 0 } } \\ { p _ { 1 } } \\ { \vdots } \\ { p _ { N - 2 } } \\ { p _ { N - 1 } } \end{array} \right] + \left[ \begin{array} { c } { 0 } \\ { 0 } \\ { \vdots } \\ { 0 } \\ { p _ { N } } \end{array} \right]
$$

or

$$
x { \mathbf { p } } = { \mathbf { T } } \cdot { \mathbf { p } } + p _ { N } { \mathbf { e } } _ { N - 1 }
$$

Here $\mathbf { T }$ is a tridiagonal matrix; $\mathbf { p }$ is a column vector of $p _ { 0 } , p _ { 1 } , \ldots , p _ { N - 1 }$ ; and $\mathbf { e } _ { N - 1 }$ is a unit vector with a 1 in the $( N - 1 ) \mathrm { s t }$ (last) position and zeros elsewhere. The matrix $\mathbf { T }$ can be symmetrized by a diagonal similarity transformation $\mathbf { D }$ to give

$$
\mathbf { J } = \mathbf { D } \mathbf { T } \mathbf { D } ^ { - 1 } = \left[ \begin{array} { c c c c c c } { a _ { 0 } } & { \sqrt { b _ { 1 } } } & & & & \\ { \sqrt { b _ { 1 } } } & { a _ { 1 } } & { \sqrt { b _ { 2 } } } & & & \\ & { \vdots } & & { \vdots } & & \\ & & & { \sqrt { b _ { N - 2 } } } & { a _ { N - 2 } } & { \sqrt { b _ { N - 1 } } } \\ & & & & { \sqrt { b _ { N - 1 } } } & { a _ { N - 1 } } \end{array} \right]
$$

The matrix $\mathbf { J }$ is called the Jacobi matrix (not to be confused with other matrices named after Jacobi that arise in completely different problems!). Now we see from (4.6.26) that $p _ { N } ( x _ { j } ) =$ 0 is equivalent to $x _ { j }$ being an eigenvalue of $\mathbf { T }$ . Since eigenvalues are preserved by a similarity transformation, $x _ { j }$ is an eigenvalue of the symmetric tridiagonal matrix $\mathbf { J }$ . Moreover, Wilf [4] shows that if ${ \bf v } _ { j }$ is the eigenvector corresponding to the eigenvalue $x _ { j }$ , normalized so that $\mathbf { v } \cdot \mathbf { v } = 1$ , then

$$
w _ { j } = \mu _ { 0 } v _ { j , 0 } ^ { 2 }
$$

where

$$
\mu _ { 0 } = \int _ { a } ^ { b } W ( x ) d x
$$

and where $v _ { j , 0 }$ is the zeroth component of $\mathbf { V }$ . As we shall see in Chapter 11, finding all eigenvalues and eigenvectors of a symmetric tridiagonal matrix is a relatively efficient and well-conditioned procedure. We accordingly give a routine, gaucof, for finding the abscissas and weights, given the coefficients $a _ { j }$ and $b _ { j }$ . Remember that if you know the recurrence relation for orthogonal polynomials that are not normalized to be monic, you can easily convert it to monic form by means of the quantities $\lambda _ { j }$ .

void gaucof(VecDoub_IO &a, VecDoub_IO &b, const Doub amu0, VecDoub_O &x, VecDoub_O &w)

Computes the abscissas and weights for a Gaussian quadrature formula from the Jacobi matrix. On input, $\mathbf { a } \left[ 0 \ldots \mathbf { n - 1 } \right]$ and b $\left[ 0 \ldots \mathbf { n } \mathbf { - } 1 \right]$ are the coefficients of the recurrence relation for the set of monic orthogonal polynomials. The quantity $\begin{array} { r } { \mu _ { 0 } \equiv \int _ { a } ^ { b } W ( x ) d x } \end{array}$ is input as amu0. The abscissas $\mathbf { x } \left[ 0 \ldots \mathbf { n - 1 } \right]$ are returned in descending order, with the corresponding weights in $\mathtt { w } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ . The arrays a and b are modified. Execution can be speeded up by modifying tqli and eigsrt to compute only the zeroth component of each eigenvector.

Int $\mathrm { n } = \mathrm { a }$ .size(); for (Int $\scriptstyle \dot { 1 } = 0$ ;i<n; $\mathrm { i } + + \mathrm { j }$ ) if (i $\ ! =$ 0) b[i] $=$ sqrt(b[i]); Set up superdiagonal of Jacobi matrix. Symmeig sym(a,b); for (Int $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) { x[i] $=$ sym.d[i]; w[i] $=$ amu0\*sym.z[0][i]\*sym.z[0][i]; Equation (4.6.28). } }

# 4.6.3 Orthogonal Polynomials with Nonclassical Weights

What do you do if your weight function is not one of the classical ones dealt with above and you do not know the $a _ { j }$ ’s and $b _ { j }$ ’s of the recurrence relation (4.6.6) to use in gaucof? Obviously, you need a method of finding the $a _ { j }$ ’s and $b _ { j }$ ’s.

The best general method is the Stieltjes procedure: First compute $a _ { 0 }$ from (4.6.7), and then $p _ { 1 } ( x )$ from (4.6.6). Knowing $p _ { 0 }$ and $p _ { 1 }$ , compute $a _ { 1 }$ and $b _ { 1 }$ from (4.6.7), and so on. But how are we to compute the inner products in (4.6.7)?

The textbook approach is to represent each $p _ { j } ( x )$ explicitly as a polynomial in $x$ and to compute the inner products by multiplying out term by term. This will be feasible if we know the first $2 N$ moments of the weight function,

$$
\mu _ { j } = \int _ { a } ^ { b } x ^ { j } W ( x ) d x \qquad j = 0 , 1 , \ldots , 2 N - 1
$$

However, the solution of the resulting set of algebraic equations for the coefficients $a _ { j }$ and $b _ { j }$ in terms of the moments $\mu _ { j }$ is in general extremely ill-conditioned. Even in double precision, it is not unusual to lose all accuracy by the time $N = 1 2$ . We thus reject any procedure based on the moments (4.6.30).

Gautschi [5] showed that the Stieltjes procedure is feasible if the inner products in (4.6.7) are computed directly by numerical quadrature. This is only practicable if you can find a quadrature scheme that can compute the integrals to high accuracy despite the singularities in the weight function $W ( x )$ . Gautschi advocates the Fejer quadrature scheme ´ [5] as a generalpurpose scheme for handling singularities when no better method is available. We have personally had much better experience with the transformation methods of $\ S 4 . 5$ , particularly the DE rule and its variants.

We use a structure Stiel that implements the Stieltjes procedure. Its member function get_weights generates the coefficients $a _ { j }$ and $b _ { j }$ of the recurrence relation, and then calls gaucof to find the abscissas and weights. You can easily modify it to return the $a _ { j }$ ’s and $b _ { j }$ ’s if you want them as well. Internally, the routine calls the function quad to do the integrals in (4.6.7). For a finite range of integration, the routine uses the straight DE rule. This is effected by invoking the constructor with five parameters: the number of quadrature abscissas (and weights) desired, the lower and upper limits of integration, the parameter $h _ { \mathrm { m a x } }$ to be passed to the DE rule (see $\ S 4 . 5 )$ ), and the weight function $W ( x )$ . For an infinite range of integration, the routine invokes the trapezoidal rule with one of the coordinate transformations discussed in $\ S 4 . 5$ . For this case you invoke the constructor that has no $h _ { \mathrm { m a x } }$ , but takes the mapping function $x = x ( t )$ and its derivative $d x / d t$ in addition to $W ( x )$ . Now the range of integration you input is the finite range of the trapezoidal rule.

This will all be clearer with some examples. Consider first the weight function

$$
W ( x ) = - \log x
$$

on the finite interval $( 0 , 1 )$ . Normally, for the finite range case (DE rule), the weight function must be coded as a function of two variables, $W ( x , \delta )$ , where $\delta$ is the distance from the endpoint singularity. Since the logarithmic singularity at the endpoint $x = 0$ is “mild,” there is no need to use the argument $\delta$ in coding the function:

Doub wt(const Doub x, const Doub del)   
{ return -log(x);   
}

A value of $h _ { \mathrm { m a x } } = 3 . 7$ will give full double precision, as discussed in $\ S 4 . 5$ , so the calling code looks like this:

$\mathtt { n } = \mathtt { \Gamma } \dots . \mathtt { n } .$ VecDoub $\mathbf { x } \left( \mathbf { n } \right)$ , $\mathtt { w } ( \mathtt { n } )$ ; Stiel $\mathbf { s } \left( \mathtt { n } , 0 . 0 , 1 . 0 , 3 . 7 , \mathtt { w t } \right)$ ; s.get_weights $( \mathbf { x } , \mathbf { w } )$ ;

For the infinite range case, in addition to the weight function $W ( x )$ , you have to supply two functions for the coordinate transformation you want to use (see equation 4.5.14). We’ll denote the mapping $x = x ( t )$ by $\mathtt { f x }$ and $d x / d t$ by fdxdt, but you can use any names you like. All these functions are coded as functions of one variable.

Here is an example of the user-supplied functions for the weight function

$$
W ( x ) = { \frac { x ^ { 1 / 2 } } { e ^ { x } + 1 } }
$$

on the interval $( 0 , \infty )$ . Gaussian quadrature based on $W ( x )$ has been proposed for evaluating generalized Fermi-Dirac integrals [6] (cf. $\ S 4 . 5 \AA$ ). We use the “mixed” DE rule of equation (4.5.14), $x = e ^ { t - e ^ { - t } }$ . As is typical with the Stieltjes procedure, you get abscissas and weights within about one or two significant digits of machine accuracy for $N$ of a few dozen.

Doub wt(const Doub x)   
{ Doub s=exp(-x); return sqrt(x)\*s/(1.0+s);   
}   
Doub fx(const Doub t)   
{ return exp(t-exp(-t));   
}   
Doub fdxdt(const Doub t)   
{ Doub $\tt { s } =$ exp(-t); return exp(t-s)\*(1.0+s);   
}   
Stiel ss(n,-5.5,6.5,wt,fx,fdxdt)   
ss.get_weights(x,w);

The listing of the Stiel object, and discussion of some of the $\mathrm { C } { + } { + }$ intricacies of its coding, are in a Webnote [9].

Two other algorithms exist [7,8] for finding abscissas and weights for Gaussian quadratures. The first starts similarly to the Stieltjes procedure by representing the inner product integrals in equation (4.6.7) as discrete quadratures using some quadrature rule. This defines a matrix whose elements are formed from the abscissas and weights in your chosen quadrature rule, together with the given weight function. Then an algorithm due to Lanczos is used to transform this to a matrix that is essentially the Jacobi matrix (4.6.27).

The second algorithm is based on the idea of modified moments. Instead of using powers of $x$ as a set of basis functions to represent the $p _ { j }$ ’s, one uses some other known set of orthogonal polynomials $\pi _ { j } ( x )$ , say. Then the inner products in equation (4.6.7) will be expressible

in terms of the modified moments

$$
\nu _ { j } = \int _ { a } ^ { b } \pi _ { j } ( x ) W ( x ) d x \qquad j = 0 , 1 , \ldots , 2 N - 1
$$

The modified Chebyshev algorithm (due to Sack and Donovan [10] and later improved by Wheeler [11]) is an efficient algorithm that generates the desired $a _ { j }$ ’s and $b _ { j }$ ’s from the modified moments. Roughly speaking, the improved stability occurs because the polynomial basis “samples” the interval $( a , b )$ better than the power basis when the inner product integrals are evaluated, especially if its weight function resembles $W ( x )$ . The algorithm requires that the modified moments (4.6.33) be accurately computed. Sometimes there is a closed form, for example, for the important case of the $\log x$ weight function [12,8]. Otherwise you have to use a suitable discretization procedure to compute the modified moments [7,8], just as we did for the inner products in the Stieltjes procedure. There is some art in choosing the auxiliary polynomials $\pi _ { j }$ , and in practice it is not always possible to find a set that removes the ill-conditioning.

Gautschi [8] has given an extensive suite of routines that handle all three of the algorithms we have described, together with many other aspects of orthogonal polynomials and Gaussian quadrature. However, for most straightforward applications, you should find Stiel together with a suitable DE rule quadrature more than adequate.

# 4.6.4 Extensions of Gaussian Quadrature

There are many different ways in which the ideas of Gaussian quadrature have been extended. One important extension is the case of preassigned nodes: Some points are required to be included in the set of abscissas, and the problem is to choose the weights and the remaining abscissas to maximize the degree of exactness of the the quadrature rule. The most common cases are Gauss-Radau quadrature, where one of the nodes is an endpoint of the interval, either $a$ or $b$ , and Gauss-Lobatto quadrature, where both $a$ and $b$ are nodes. Golub [13,8] has given an algorithm similar to gaucof for these cases.

An $N$ -point Gauss-Radau rule has the form of equation (4.6.1), where $x _ { 1 }$ is chosen to be either $a$ or $b$ $x _ { 1 }$ must be finite). You can construct the rule from the coefficients for the corresponding ordinary $N$ -point Gaussian quadrature. Simply set up the Jacobi matrix equation (4.6.27), but modify the entry $a N _ { - 1 }$ :

$$
a _ { N - 1 } ^ { \prime } = x _ { 1 } - b _ { N - 1 } \frac { p _ { N - 2 } ( x _ { 1 } ) } { p _ { N - 1 } ( x _ { 1 } ) }
$$

Here is the routine:

void radau(VecDoub_IO &a, VecDoub_IO &b, const Doub amu0, const Doub x1, VecDoub_O &x, VecDoub_O &w)

# gauss wgts2.h

Computes the abscissas and weights for a Gauss-Radau quadrature formula. On input, $\mathtt { a } \left[ 0 \ldots \ldots \right] \mathtt { a } \left[ \mathtt { 1 } \right]$ and $\mathbf { b } \left[ 0 \ldots \mathbf { n - 1 } \right]$ are the coefficients of the recurrence relation for the set of monic orthogonal polynomials corresponding to the weight function. (b[0] is not referenced.) The quantity $\textstyle \mu _ { 0 } \equiv \int _ { a } ^ { b } W ( x ) d x$ is input as amu0. x1 is input as either endpoint of the interval. The abscissas $\mathbf { x } \left[ 0 \ldots \mathbf { n - 1 } \right]$ are returned in descending order, with the corresponding weights in $\mathtt { w } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ . The arrays a and b are modified.

Int $\mathtt { n } = \mathtt { a }$ .size();  
if $\mathbf { \Omega } ( \mathbf { n \Omega } = \mathbf { \Omega } 1 )$ {$\mathbf { x } \left[ 0 \right] { = } \mathbf { x } { 1 }$ ;$\mathtt { w } [ 0 ] =$ amu0;  
} else {Doub p=x1-a[0];

Compute $p _ { \mathit { N } - 1 }$ and $p N - 2$ by recurrence.

Doub pm1 $^ { = 1 }$ .0; Doub $\mathrm { p 1 = p }$ ; for (Int $\dot { \bar { 1 } } = 1$ ;i<n-1;i++) { $\mathrm { p } =$ (x1-a[i])\*p1-b[i]\*pm1; pm1=p1; $\mathtt { p 1 = p }$ ; } a[n-1]=x1-b[n-1]\*pm1/p; Equation (4.6.34). gaucof(a,b,amu0,x,w); } }

An $N$ -point Gauss-Lobatto rule has the form of equation (4.6.1) where $x _ { 1 } = a$ , $x _ { N } = b$ (both finite). This time you modify the entries $a N _ { - 1 }$ and $b _ { N - 1 }$ in equation (4.6.27) by solving two linear equations:

$$
\begin{array} { r l } { \left[ \begin{array} { l l } { p _ { N - 1 } ( x _ { 1 } ) } & { p _ { N - 2 } ( x _ { 1 } ) } \\ { p _ { N - 1 } ( x _ { N } ) } & { p _ { N - 2 } ( x _ { N } ) } \end{array} \right] \left[ \begin{array} { l } { a _ { N - 1 } ^ { \prime } } \\ { b _ { N - 1 } ^ { \prime } } \end{array} \right] = \left[ \begin{array} { l } { x _ { 1 } p _ { N - 1 } ( x _ { 1 } ) } \\ { x _ { N } p _ { N - 1 } ( x _ { N } ) } \end{array} \right] } \end{array}
$$

void lobatto(VecDoub_IO &a, VecDoub_IO &b, const Doub amu0, const Doub x1, const Doub xn, VecDoub_O &x, VecDoub_O &w)

Computes the abscissas and weights for a Gauss-Lobatto quadrature formula. On input, the vectors $\mathtt { a } \left[ 0 \ldots \mathtt { n - 1 } \right]$ and $\mathbf { b } \left[ 0 \ldots \mathbf { n - 1 } \right]$ are the coefficients of the recurrence relation for the set of monic orthogonal polynomials corresponding to the weight function. (b[0] is not referenced.) The quantity $\textstyle \mu _ { 0 } \equiv \int _ { a } ^ { b } W ( x ) d x$ is input as amu0. x1 amd xn are input as the endpoints of the interval. The abscissas $\mathbf { x } \left[ 0 \ldots \ldots \right] $ are returned in descending order, with the corresponding weights in $\mathtt { w } \left[ 0 \ldots \ldots \ldots 1 \right]$ . The arrays a and b are modified.

Doub det,pl,pr,p1l,p1r,pm1l,pm1r;   
Int $\mathrm { n } = \mathrm { a }$ .size();   
if $\mathbf { \Phi } _ { \mathbf { n } } \ < = \ 1 \mathbf { \Phi } _ { \mathbf { \Phi } }$ ) throw( $" \mathtt { n }$ must be bigger than 1 in lobatto");   
$\mathtt { p l } \mathtt { = x } 1 \mathtt { - a }$ [0]; Compute $p _ { { N } - 1 }$ and $p N - 2$ at $x _ { 1 }$ and $x N$ by recur  
pr=xn-a[0]; rence.   
pm1l $^ { = 1 }$ .0;   
pm1r $^ { = 1 }$ .0;   
p1l=pl;   
p1r=pr;   
for (Int i=1;i<n-1;i++) { $\mathtt { p 1 } =$ (x1-a[i])\*p1l-b[i]\*pm1l; $\mathbf { p } \mathbf { r } ^ { = }$ (xn-a[i])\*p1r-b[i]\*pm1r; pm1l=p1l; pm1r=p1r; $\mathtt { p 1 1 } \mathtt { = p 1 }$ ; p1r=pr;   
}   
det=pl\*pm1r-pr\*pm1l; Solve equation (4.6.35).   
a[n-1] $=$ (x1\*pl\*pm1r-xn\*pr\*pm1l)/det;   
b[n-1] $=$ (xn-x1)\*pl\*pr/det;   
gaucof(a,b,amu0,x,w);

The second important extension of Gaussian quadrature is the Gauss-Kronrod formulas. For ordinary Gaussian quadrature formulas, as $N$ increases, the sets of abscissas have no points in common. This means that if you compare results with increasing $N$ as a way of estimating the quadrature error, you cannot reuse the previous function evaluations. Kronrod [14] posed the problem of searching for optimal sequences of rules, each of which reuses all abscissas of its predecessor. If one starts with $N = m$ , say, and then adds $n$ new points, one has $2 n + m$ free parameters: the $n$ new abscissas and weights, and $m$ new weights for the fixed previous abscissas. The maximum degree of exactness one would expect to achieve would therefore be $2 n + m - 1$ . The question is whether this maximum degree of exactness can actually be achieved in practice, when the abscissas are required to all lie inside $( a , b )$ . The answer to this question is not known in general.

Kronrod showed that if you choose $\textit { n } = \textit { m } + 1$ , an optimal extension can be found for Gauss-Legendre quadrature. Patterson [15] showed how to compute continued extensions of this kind. Sequences such as $N = 1 0 , 2 1 , 4 3 , 8 7 , . . .$ are popular in automatic quadrature routines [16] that attempt to integrate a function until some specified accuracy has been achieved.

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, $\ S 2 5 . 4$ .[1]   
Stroud, A.H., and Secrest, D. 1966, Gaussian Quadrature Formulas (Englewood Cliffs, NJ: Prentice-Hall).[2]   
Golub, G.H., and Welsch, J.H. 1969, “Calculation of Gauss Quadrature Rules,” Mathematics of Computation, vol. 23, pp.221-230 and A1-A10.[3]   
Wilf, H.S. 1962, Mathematics for the Physical Sciences (New York: Wiley), Problem 9, p. 80.[4]   
Gautschi, W. 1968, “Construction of Gauss-Christoffel Quadrature Formulas,” Mathematics of Computation, vol. 22, pp. 251-270.[5]   
Sagar, R.P. 1991, “A Gaussian Quadrature for the Calculation of Generalized Fermi-Dirac Integrals,” Computer Physics Communications, vol. 66, pp. 271–275.[6]   
Gautschi, W. 1982, “On Generating Orthogonal Polynomials,” SIAM Journal on Scientific and Statistical Computing, vol. 3, pp.289-317.[7]   
Gautschi, W. 1994, “ORTHPOL: A Package of Routines for Generating Orthogonal Polynomials and Gauss-type Quadrature Rules,” ACM Transactions on Mathematical Software, vol. 20, pp. 21–62 (Algorithm 726 available from netlib).[8]   
Numerical Recipes Software 2007, “Implementation of Stiel,” Numerical Recipes Webnote No. 3, at http://www.nr.com/webnotes?3 [9]   
Sack, R.A., and Donovan, A.F. 1971/72, “An Algorithm for Gaussian Quadrature Given Modified Moments,” Numerische Mathematik, vol. 18, pp. 465–478.[10]   
Wheeler, J.C. 1974, “Modified Moments and Gaussian Quadratures,” Rocky Mountain Journal of Mathematics,vol. 4,pp. 287-296.[11]   
Gautschi, W. 1978, in Recent Advances in Numerical Analysis, C. de Boor and G.H. Golub, eds. (New York: Academic Press), pp. 45–72.[12]   
Golub, G.H. 1973, “Some Modified Matrix Eigenvalue Problems,” SIAM Review, vol. 15, pp. 318– 334.[13]   
Kronrod, A.S. 1964, Doklady Akademii Nauk SSSR, vol. 154, pp. 283–286 (in Russian); translated as Soviet Physics “Doklady”.[14]   
Patterson, T.N.L. 1968, “The Optimum Addition of Points to Quadrature Formulae,” Mathematics of Computation,vol. 22, pp.847-856 and C1-C11; 1969,op. cit.,vol.23,p.892.[15]   
Piessens, R., de Doncker-Kapenga, E., Überhuber, C., and Kahaner, D. 1983 QUADPACK, A Subroutine Package for Automatic Integration (New York: Springer). Software at http://www.netlib.org/quadpack.[16]   
Gautschi, W. 1981, in E. B. Christoffel, P.L. Butzer and F. Fehér, eds. (Basel: Birkhäuser), pp. 72– 147.   
Gautschi, W. 1990, in Orthogonal Polynomials, P. Nevai, ed. (Dordrecht: Kluwer Academic Publishers), pp. 181–216.

Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 3 . 6$ .

# 4.7 Adaptive Quadrature

The idea behind adaptive quadrature is very simple. Suppose you have two different numerical estimates $I _ { 1 }$ and $I _ { 2 }$ of the integral

$$
I = \int _ { a } ^ { b } f ( x ) d x
$$

Suppose $I _ { 1 }$ is more accurate. Use the relative difference between $I _ { 1 }$ and $I _ { 2 }$ as an error estimate. If it is less than $\epsilon$ , accept $I _ { 1 }$ as the answer. Otherwise divide the interval $[ a , b ]$ into two subintervals,

$$
I = \int _ { a } ^ { m } f ( x ) d x + \int _ { m } ^ { b } f ( x ) d x \qquad m = ( a + b ) / 2
$$

and compute the two integrals independently. For each one, compute an $I _ { 1 }$ and $I _ { 2 }$ , estimate the error, and continue subdividing if necessary. Dividing any given subinterval stops when its contribution to $\epsilon$ is sufficiently small. (Obviously recursion will be a good way to implement this algorithm.)

The most important criterion for an adaptive quadrature routine is reliability: If you request an accuracy of $1 0 ^ { - 6 }$ , you would like to be sure that the answer is at least that good. From a theoretical point of view, however, it is impossible to design an adaptive quadrature routine that will work for all possible functions. The reason is simple: A quadrature is based on the value of the integrand $f ( x )$ at a finite set of points. You can alter the function at all the other points in an arbitrary way without affecting the estimate your algorithm returns, while the true value of the integral changes unpredictably. Despite this point of principle, however, in practice good routines are reliable for a high fraction of functions they encounter. Our favorite routine is one proposed by Gander and Gautschi [1], which we now describe. It is relatively simple, yet scores well on reliability and efficiency.

A key component of a good adaptive algorithm is the termination criterion. The usual criterion

$$
| I _ { 1 } - I _ { 2 } | < \epsilon | I _ { 1 } |
$$

is problematic. In the neighborhood of a singularity, $I _ { 1 }$ and $I _ { 2 }$ might never agree to the requested tolerance, even if it’s not particularly small. Instead, you need to somehow come up with an estimate of the whole integral $I$ of equation (4.7.1). Then you can terminate when the error in $I _ { 1 }$ is negligible compared to the whole integral:

$$
| I _ { 1 } - I _ { 2 } | < \epsilon | I _ { s } |
$$

where $I _ { s }$ is the estimate of $I$ . Gander and Gautschi implement this test by writing

$$
( { \bf i s _ { \alpha } } + { \bf \Gamma } ( { \bf i } 1 { - } { \bf i } 2 ) = { \bf i s } )
$$

which is equivalent to setting $\epsilon$ to the machine precision. However, modern optimizing compilers have become too good at recognizing that this is algebraically equivalent to

if (i1-i2 == 0.0)

which might never be satisfied in floating point arithmetic. Accordingly, we implement the test with an explicit $\epsilon$ .

The other problem you need to take care of is when an interval gets subdivided so small that it contains no interior machine-representable point. You then need to terminate the recursion and alert the user that the full accuracy might not have been attained. In the case where the points in an interval are supposed to be $\{ a , m ~ =$ $( a + b ) / 2 , b \}$ , you can test for $m \leq a$ or $b \leq m$ .

The lowest order integration method in the Gander-Gautschi method is the fourpoint Gauss-Lobatto quadrature (cf. $\ S 4 . 6 )$

$$
\begin{array} { r } { \int _ { - 1 } ^ { 1 } f ( x ) d x = \frac { 1 } { 6 } \Big [ f ( - 1 ) + f ( 1 ) \Big ] + \frac { 5 } { 6 } \Big [ f \Big ( - \frac { 1 } { \sqrt { 5 } } \Big ) + f \Big ( \frac { 1 } { \sqrt { 5 } } \Big ) \Big ] } \end{array}
$$

This formula, which is exact for polynomials of degree 5, is used to compute $I _ { 2 }$ . To reuse these function evaluations in computing $I _ { 1 }$ , they find the seven-point Kronrod extension,

$$
\begin{array} { l } { { \displaystyle \int _ { - 1 } ^ { 1 } f ( x ) d x = \frac { 1 1 } { 2 1 0 } \Big [ f ( - 1 ) + f ( 1 ) \Big ] + \frac { 7 2 } { 2 4 5 } \Big [ f \Big ( - \sqrt { \frac 2 3 } \Big ) + f \Big ( \sqrt { \frac 2 3 } \Big ) \Big ] } } \\ { { \displaystyle ~ + \frac { 1 2 5 } { 2 9 4 } \Big [ f \Big ( - \frac { 1 } { \sqrt { 5 } } \Big ) + f \Big ( \frac { 1 } { \sqrt { 5 } } \Big ) \Big ] + \frac { 1 6 } { 3 5 } f ( 0 ) } } \end{array}
$$

whose degree of exactness is nine. The formulas (4.7.5) and (4.7.6) get scaled from $[ - 1 , 1 ]$ to an arbitrary subinterval $[ a , b ]$ .

For $I _ { s }$ , Gander and Gautschi find a 13-point Kronrod extension of equation (4.7.6), which lets them reuse the previous function evaluations. The formula is coded into the routine below. You can think of this initial 13-point evaluation as a kind of Monte Carlo sampling to get an idea of the order of magnitude of the integral. But if the integrand is smooth, this initial evaluation will itself be quite accurate already. The routine below takes advantage of this.

Note that to reuse the four function evaluations in (4.7.5) in the seven-point formula (4.7.6), you can’t simply bisect intervals. But dividing into six subintervals works (there are six intervals between seven points).

To use the routine, you need to initialize an Adapt object with your required tolerance,

Adapt s(1.0e-6);

and then call the integrate function:

ans=s.integrate(func,a,b);

You should check that the desired tolerance could be met:

if (s.out_of_tolerance) cout << "Required tolerance may not be met" << endl;

The smallest allowed tolerance is 10 times the machine precision. If you enter a smaller tolerance, it gets reset internally. (The routine will work using the machine precision itself, but then it usually just takes lots of function evaluations for little additional benefit.)

The implementation of the Adapt object is given in a Webnote [2].

Adaptive quadrature is no panacea. The above routine has no special machinery to deal with singularities other than to refine the neighboring intervals. By using suitable schemes for $I _ { 1 }$ and $I _ { 2 }$ , one can customize an adaptive routine to deal with a particular kind of singularity (cf. [3]).

# CITED REFERENCES AND FURTHER READING:

Gander, W., and Gautschi, W. 2000, “Adaptive Quadrature — Revisited,” BIT vol. 40, pp. 84– 101.[1]   
Numerical Recipes Software 2007, “Implementation of Adapt,” Numerical Recipes Webnote No.4,at http://www.nr.com/webnotes?4 [2]   
Piessens, R., de Doncker-Kapenga, E., Überhuber, C., and Kahaner, D. 1983 QUADPACK A Subroutine Package for Automatic Integration (New York: Springer).Software at http://www.netlib.org/quadpack.[3]   
Davis, P.J., and Rabinowitz, P. 1984, Methods of Numerical Integration, 2nd ed., (Orlando, FL: Academic Press), Chapter 6.

# 4.8 Multidimensional Integrals

Integrals of functions of several variables, over regions with dimension greater than one, are not easy. There are two reasons for this. First, the number of function evaluations needed to sample an $N$ -dimensional space increases as the $N$ th power of the number needed to do a one-dimensional integral. If you need 30 function evaluations to do a one-dimensional integral crudely, then you will likely need on the order of 30000 evaluations to reach the same crude level for a three-dimensional integral. Second, the region of integration in $N$ -dimensional space is defined by an $N - 1$ dimensional boundary that can itself be terribly complicated: It need not be convex or simply connected, for example. By contrast, the boundary of a onedimensional integral consists of two numbers, its upper and lower limits.

The first question to be asked, when faced with a multidimensional integral, is, can it be reduced analytically to a lower dimensionality? For example, so-called iterated integrals of a function of one variable $f ( t )$ can be reduced to one-dimensional integrals by the formula

$$
\int _ { 0 } ^ { x } d t _ { n } \int _ { 0 } ^ { t _ { n } } d t _ { n - 1 } \cdots \int _ { 0 } ^ { t _ { 3 } } d t _ { 2 } \int _ { 0 } ^ { t _ { 2 } } f ( t _ { 1 } ) d t _ { 1 } = { \frac { 1 } { ( n - 1 ) ! } } \int _ { 0 } ^ { x } ( x - t ) ^ { n - 1 } f ( t ) d t _ { 1 }
$$

Alternatively, the function may have some special symmetry in the way it depends on its independent variables. If the boundary also has this symmetry, then the dimension can be reduced. In three dimensions, for example, the integration of a spherically symmetric function over a spherical region reduces, in polar coordinates, to a onedimensional integral.

The next questions to be asked will guide your choice between two entirely different approaches to doing the problem. The questions are: Is the shape of the boundary of the region of integration simple or complicated? Inside the region, is the integrand smooth and simple, or complicated, or locally strongly peaked? Does the problem require high accuracy, or does it require an answer accurate only to a percent, or a few percent?

If your answers are that the boundary is complicated, the integrand is not strongly peaked in very small regions, and relatively low accuracy is tolerable, then your problem is a good candidate for Monte Carlo integration. This method is very straightforward to program, in its cruder forms. One needs only to know a region with simple boundaries that includes the complicated region of integration, plus a method of determining whether a random point is inside or outside the region of integration. Monte Carlo integration evaluates the function at a random sample of points and estimates its integral based on that random sample. We will discuss it in more detail, and with more sophistication, in Chapter 7.

If the boundary is simple, and the function is very smooth, then the remaining approaches, breaking up the problem into repeated one-dimensional integrals, or multidimensional Gaussian quadratures, will be effective and relatively fast [1]. If you require high accuracy, these approaches are in any case the only ones available to you, since Monte Carlo methods are by nature asymptotically slow to converge.

For low accuracy, use repeated one-dimensional integration or multidimensional Gaussian quadratures when the integrand is slowly varying and smooth in the region of integration, Monte Carlo when the integrand is oscillatory or discontinuous but not strongly peaked in small regions.

If the integrand is strongly peaked in small regions, and you know where those regions are, break the integral up into several regions so that the integrand is smooth in each, and do each separately. If you don’t know where the strongly peaked regions are, you might as well (at the level of sophistication of this book) quit: It is hopeless to expect an integration routine to search out unknown pockets of large contribution in a huge $N$ -dimensional space. (But see $\ S 7 . 9$ .)

If, on the basis of the above guidelines, you decide to pursue the repeated onedimensional integration approach, here is how it works. For definiteness, we will consider the case of a three-dimensional integral in $x , y , z$ -space. Two dimensions, or more than three dimensions, are entirely analogous.

The first step is to specify the region of integration by (i) its lower and upper limits in $x$ , which we will denote $x _ { 1 }$ and $x _ { 2 }$ ; (ii) its lower and upper limits in $y$ at a specified value of $x$ , denoted $y _ { 1 } ( x )$ and $y _ { 2 } ( x )$ ; and (iii) its lower and upper limits in $z$ at specified $x$ and $y$ , denoted $z _ { 1 } ( x , y )$ and $z _ { 2 } ( x , y )$ . In other words, find the numbers $x _ { 1 }$ and $x _ { 2 }$ , and the functions $y _ { 1 } ( x ) , y _ { 2 } ( x ) , z _ { 1 } ( x , y )$ , and $z _ { 2 } ( x , y )$ such that

$$
{ \begin{array} { l } { I \equiv \iiint d x d y d z f ( x , y , z ) } \\ { = \int _ { x _ { 1 } } ^ { x _ { 2 } } d x \int _ { y _ { 1 } ( x ) } ^ { y _ { 2 } ( x ) } d y \int _ { z _ { 1 } ( x , y ) } ^ { z _ { 2 } ( x , y ) } d z f ( x , y , z ) } \end{array} }
$$

For example, a two-dimensional integral over a circle of radius one centered on the origin becomes

$$
\int _ { - 1 } ^ { 1 } d x \int _ { - \sqrt { 1 - x ^ { 2 } } } ^ { \sqrt { 1 - x ^ { 2 } } } d y \ f ( x , y )
$$

Now we can define a function $G ( x , y )$ that does the innermost integral,

$$
G ( x , y ) \equiv \int _ { z _ { 1 } ( x , y ) } ^ { z _ { 2 } ( x , y ) } f ( x , y , z ) d z
$$

![](images/4f297a4d7aa71c4997e783d42aaee87e82953b7bef9278bc5a7e45cd8727c272.jpg)  
Figure 4.8.1. Function evaluations for a two-dimensional integral over an irregular region, shown schematically. The outer integration routine, in $y$ , requests values of the inner, $x$ , integral at locations along the $y$ -axis of its own choosing. The inner integration routine then evaluates the function at $x$ locations suitable to $i t$ . This is more accurate in general than, e.g., evaluating the function on a Cartesian mesh of points.

and a function $H ( x )$ that does the integral of $G ( x , y )$ ,

$$
H ( x ) \equiv \int _ { y _ { 1 } ( x ) } ^ { y _ { 2 } ( x ) } G ( x , y ) d y
$$

and finally our answer as an integral over $H ( x )$

$$
I = \int _ { x _ { 1 } } ^ { x _ { 2 } } H ( x ) d x
$$

In an implementation of equations $( 4 . 8 . 4 ) - ( 4 . 8 . 6 )$ , some basic one-dimensional integration routine (e.g., qgaus in the program following) gets called recursively: once to evaluate the outer integral $I$ , then many times to evaluate the middle integral $H$ , then even more times to evaluate the inner integral $G$ (see Figure 4.8.1). Current values of $x$ and $y$ , and the pointers to the user-supplied functions for the integrand and the boundaries, are passed “over the head” of the intermediate calls through member variables in the three functors defining the integrands for $G$ , $H$ and $I$ .

# struct NRf3 {

Doub xsav,ysav; Doub (\*func3d)(const Doub, const Doub, const Doub); Doub operator()(const Doub z) The integrand $f ( x , y , z )$ evaluated at fixed $x$ and { $y$ . return func3d(xsav,ysav,z); } };

struct NRf2 { NRf3 f3; Doub (\*z1)(Doub, Doub); Doub (\*z2)(Doub, Doub); NRf2(Doub zz1(Doub, Doub), Doub zz2(Doub, Doub)) : z1(zz1), z2(zz2) {} Doub operator()(const Doub y) This is $G$ of eq. (4.8.4). { f3.ysav=y; return qgaus(f3,z1(f3.xsav,y),z2(f3.xsav,y)); }   
};   
struct NRf1 { Doub (\*y1)(Doub); Doub (\*y2)(Doub); NRf2 f2; NRf1(Doub yy1(Doub), Doub yy2(Doub), Doub z1(Doub, Doub), Doub z2(Doub, Doub)) : y1(yy1),y2(yy2), f2(z1,z2) {} Doub operator()(const Doub x) This is $H$ of eq. (4.8.5). { f2.f3.xsav $= \mathbf { x }$ ; return qgaus(f2,y1(x),y2(x)); }   
};

# template <class T>

Doub quad3d(T &func, const Doub x1, const Doub x2, Doub y1(Doub), Doub y2(Doub), Doub z1(Doub, Doub), Doub z2(Doub, Doub))

Returns the integral of a user-supplied function func over a three-dimensional region specified by the limits x1, x2, and by the user-supplied functions y1, y2, z1, and $_ { z 2 }$ , as defined in (4.8.2). Integration is performed by calling qgaus recursively.

NRf1 f1(y1,y2,z1,z2);   
f1.f2.f3.func3d=func;   
return qgaus(f1,x1,x2);

Note that while the function to be integrated can be supplied either as a simple function

Doub func(const Doub x, const Doub y, const Doub z);

or as the equivalent functor, the functions defining the boundary can only be functions:

Doub y1(const Doub x);   
Doub y2(const Doub x);   
Doub z1(const Doub x, const Doub y);   
Doub z2(const Doub x, const Doub y);

This is for simplicity; you can easily modify the code to take functors if you need to.

The Gaussian quadrature routine used in quad3d is simple, but its accuracy is not controllable. An alternative is to use a one-dimensional integration routine like qtrap, qsimp or qromb, which have a user-definable tolerance eps. Simply replace all occurrences of qgaus in quad3d by qromb, say.

Note that multidimensional integration is likely to be very slow if you try for too much accuracy. You should almost certainly increase the default eps in qromb from $1 0 ^ { - 1 0 }$ to $1 0 ^ { - 6 }$ or bigger. You should also decrease JMAX to avoid a lot of waiting around for an answer. Some people advocate using a smaller eps for the inner quadrature (over $z$ in our routine) than for the outer quadratures (over $x$ or $y$ ).

# CITED REFERENCES AND FURTHER READING:

Stroud, A.H. 1971, Approximate Calculation of Multiple Integrals (Englewood Cliffs, NJ: Prentice-Hall).[1]   
Dahlquist, G., and Bjorck, A. 1974, Numerical Methods (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2003 (New York: Dover), $\ S 7 . 7$ , p. 318.   
Johnson, L.W., and Riess, R.D. 1982, Numerical Analysis, 2nd ed. (Reading, MA: Addison-Wesley), $\ S 6 . 2 . 5$ , p. 307.   
Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, equations 25.4.58ff.

# 5.0 Introduction

The purpose of this chapter is to acquaint you with a selection of the techniques that are frequently used in evaluating functions. In Chapter 6, we will apply and illustrate these techniques by giving routines for a variety of specific functions. The purposes of this chapter and the next are thus mostly congruent. Occasionally, however, the method of choice for a particular special function in Chapter 6 is peculiar to that function. By comparing this chapter to the next one, you should get some idea of the balance between “general” and “special” methods that occurs in practice.

Insofar as that balance favors general methods, this chapter should give you ideas about how to write your own routine for the evaluation of a function that, while “special” to you, is not so special as to be included in Chapter 6 or the standard function libraries.

# CITED REFERENCES AND FURTHER READING:

Fike, C.T. 1968, Computer Evaluation of Mathematical Functions (Englewood Cliffs, NJ: Prentice-Hall).

Lanczos, C. 1956, Applied Analysis; reprinted 1988 (New York: Dover), Chapter 7.

# 5.1 Polynomials and Rational Functions

A polynomial of degree $N$ is represented numerically as a stored array of coefficients, $\mathsf { c } \left[ \mathsf { j } \right]$ with ${ \mathrm { j } } = 0 , \ldots , N$ . We will always take $\mathsf { c } \left[ 0 \right]$ to be the constant term in the polynomial and $\mathsf { c } \left[ N \right]$ the coefficient of $x ^ { N }$ ; but of course other conventions are possible. There are two kinds of manipulations that you can do with a polynomial: numerical manipulations (such as evaluation), where you are given the numerical value of its argument, or algebraic manipulations, where you want to transform the coefficient array in some way without choosing any particular argument. Let’s start with the numerical.

We assume that you know enough never to evaluate a polynomial this way:

$\mathtt { p = c } [ 0 ] + \mathtt { c } [ 1 ] * _ { \mathbb { X } } + \mathtt { c } [ 2 ] * _ { \mathbb { X } } * _ { \mathbb { X } } + \mathtt { c } [ 3 ] * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } + \mathtt { c } [ 4 ] * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } * _ { \mathbb { X } } ] * _ { \mathbb { X } } \mathtt { X } ( \mathtt { X } ) \mathtt { X } ( ) \mathtt { X } ( \mathtt { X } ) ( \mathtt { X } ) \mathtt { X } ( ) \mathtt { X } ( \mathtt { X } ) ( \mathtt { X } ) \mathtt { X } ( ) \mathtt { X } ( \mathtt { X } ) ( \mathtt { X } ) \mathtt { X } ( ) \mathtt { X } ( \mathtt { X } ) ( \mathtt { X } ) \mathtt { X } ( ) \mathtt { X } ( \mathtt { X } ) ( \mathtt { X } ) \mathtt { X } ( ) \mathtt { X } ( ) \mathtt { X } ) ,$ or (even worse!),

$$
\mathtt { p } = \mathtt { C } \left[ 0 \right] + \mathtt { c } \left[ 1 \right] * _ { \mathrm { X } ^ { + } \mathrm { C } } \left[ 2 \right] * _ { \mathtt { P } ^ { \mathrm { O } } } \mathtt { w } ( \mathrm { x } , 2 , 0 ) + \mathtt { c } \left[ 3 \right] * _ { \mathtt { P } ^ { \mathrm { O } } } \mathtt { w } ( \mathrm { x } , 3 , 0 ) + \mathtt { c } \left[ 4 \right] * _ { \mathtt { P } ^ { \mathrm { O } } } \mathtt { w } ( \mathrm { x } , 4 , 0 ) 
$$

Come the (computer) revolution, all persons found guilty of such criminal behavior will be summarily executed, and their programs won’t be! It is a matter of taste, however, whether to write

$$
\operatorname { p } \mathbf { = } \mathbf { c } \left[ 0 \right] \mathbf { + } \mathbf { x } \mathbf { * } \left( \mathbf { c } \left[ 1 \right] \mathbf { + } \mathbf { x } \mathbf { * } \left( \mathbf { c } \left[ 2 \right] \mathbf { + } \mathbf { x } \mathbf { * } \left( \mathbf { c } \left[ 3 \right] \mathbf { + } \mathbf { x } \mathbf { * } \left[ 4 \right] \right) \right) \right) \mathbf { ; }
$$

or

$$
\begin{array} { r } { \mathtt { p } = \left( \left( \left( \mathtt { c } \left[ 4 \right] \ast _ { \mathbf { X } } + \mathtt { c } \left[ 3 \right] \right) \ast _ { \mathbf { X } } + \mathtt { c } \left[ 2 \right] \right) \ast _ { \mathbf { X } } + \mathtt { c } \left[ 1 \right] \right) \ast _ { \mathbf { X } } + \mathtt { c } \left[ 0 \right] ; } \end{array}
$$

If the number of coefficients ${ \mathsf { c } } \left[ 0 \ldots \cdot \mathbf { n } ^ { - 1 } \right]$ is large, one writes

$\mathtt { p - c }$ [n-1];   
for(j=n-2;j>=0;j--) p=p\*x+c[j];

or

$\mathtt { p } = \mathtt { c } [ \mathtt { j } = \mathtt { n } - 1 ]$ ;  
while ( $\mathrm { . j } { > } 0 \mathrm { . }$ ) p=p\*x+c[--j];

We can formalize this by defining a function object (or functor) that binds a reference to an array of coefficients and endows them with a polynomial evaluation function,

#

struct Poly {   
Polynomial function object that binds a reference to a vector of coefficients. VecDoub &c; Poly(VecDoub &cc) : c(cc) {} Doub operator() (Doub x) { Returns the value of the polynomial at x. Int j; Doub $\mathtt { p } \ = \ \mathtt { c } [ \mathtt { j } = \mathtt { c }$ .size()-1]; while ( ${ \bf j } > 0 )$ $\texttt { p } = \texttt { p } { * } \texttt { x } + \texttt { c } [ \texttt { -- j } ]$ ; return p; }   
};

which allows you to write things like

${ \bf y } = { \bf P o l y } ( { \bf c } ) ( { \bf x } ) ;$ where c is a coefficient vector.

Another useful trick is for evaluating a polynomial $P ( x )$ and its derivative $d P ( x ) / d x$ simultaneously:

$$
\begin{array} { r l } & { \mathrm { p = c \left[ n - 1 \right] ; } } \\ & { \mathrm { d p = 0 . } ; } \\ & { \mathrm { f o r \left( j = n - 2 ; j > = 0 ; j \mathrm { -- } \right) \{ d p = d p { * } x { + } \mathrm { p } ; \mathrm { p = p } { * } x { + } \mathrm { c \left[ j \right] } ; \} } } \end{array}
$$

or

$\mathtt { p } = \mathtt { c } [ \mathtt { j } = \mathtt { n } - 1 ]$ ;   
$\mathtt { d p = } 0$ .;   
while ( ${ \mathrm { . j } } { \mathrm { > } } 0 { \mathrm { : } }$ ) {dp=dp\*x+p; p=p\*x+c[--j];}

which yields the polynomial as p and its derivative as dp using coefficients ${ \mathsf { c } } \left[ 0 \ldots \cdot \mathbf { n } ^ { - 1 } \right]$ .

The above trick, which is basically synthetic division [1,2], generalizes to the evaluation of the polynomial and nd of its derivatives simultaneously:

# void ddpoly(VecDoub_I &c, const Doub x, VecDoub_O &pd)

Given the coefficients of a polynomial of degree nc as an array $\mathtt { c } [ 0 \dots \mathtt { n c } ]$ of size $\mathtt { n c } { + 1 }$ (with $^ \texttt { c }$ [0] being the constant term), and given a value x, this routine fills an output array pd of size $\mathtt { n d } { + 1 }$ with the value of the polynomial evaluated at x in pd[0], and the first nd derivatives at x in pd[1..nd].

Int nnd,j,i,nc $\mathtt { \mathtt { \mathtt { \mathtt { \mathtt { \mathtt { \mathtt { \mathtt \mathtt { \mathtt \mathtt { \mathtt \mathtt { \mathtt \mathtt { \mathtt \mathtt \Lambda } } } } } } } } } } }$ .size()-1,nd=pd.size()-1; Doub cnst ${ = } 1$ .0; pd[0] $= _ { \mathbb { C } }$ [nc]; for ( $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<nd+1;j++) pd[j] ${ = } 0$ .0; for (i=nc-1; $\scriptstyle \dot { 1 } > = 0$ ;i--) { nnd (nd $<$ (nc-i) ? nd : nc-i); for (j=nnd;j>0;j--) pd[j] $=$ pd[j]\*x+pd[j-1]; pd[0]=pd[0]\*x+c[i]; } for ( $\scriptstyle \dot { \mathbf { 1 } } = 2$ ;i<nd+1; $\dot { \bf 1 } + + \dot { }$ ) { After the first derivative, factorial constants come in. cnst $\ast = \textit { i }$ ; pd[i] $\ast =$ cnst; } }

As a curiosity, you might be interested to know that polynomials of degree $n > 3$ can be evaluated in fewer than $n$ multiplications, at least if you are willing to precompute some auxiliary coefficients and, in some cases, do some extra addition. For example, the polynomial

$$
P ( x ) = a _ { 0 } + a _ { 1 } x + a _ { 2 } x ^ { 2 } + a _ { 3 } x ^ { 3 } + a _ { 4 } x ^ { 4 }
$$

where $a _ { 4 } ~ > ~ 0$ , can be evaluated with three multiplications and five additions as follows:

$$
P ( x ) = [ ( A x + B ) ^ { 2 } + A x + C ] [ ( A x + B ) ^ { 2 } + D ] + E
$$

where $A , B , C , D$ ; and $E$ are to be precomputed by

$$
\begin{array} { l } { A = ( a _ { 4 } ) ^ { 1 / 4 } } \\ { B = \frac { a _ { 3 } - A ^ { 3 } } { 4 A ^ { 3 } } } \\ { D = 3 B ^ { 2 } + 8 B ^ { 3 } + \frac { a _ { 1 } A - 2 a _ { 2 } B } { A ^ { 2 } } } \\ { C = \frac { a _ { 2 } } { A ^ { 2 } } - 2 B - 6 B ^ { 2 } - D } \\ { E = a _ { 0 } - B ^ { 4 } - B ^ { 2 } ( C + D ) - C D } \end{array}
$$

Fifth-degree polynomials can be evaluated in four multiplies and five adds; sixthdegree polynomials can be evaluated in four multiplies and seven adds; if any of this strikes you as interesting, consult references [3-5]. The subject has something of the same flavor as that of fast matrix multiplication, discussed in $\ S 2 . 1 1$ .

Turn now to algebraic manipulations. You multiply a polynomial of degree $n - 1$ (array of range $\left[ 0 \cdot \cdot \mathbf { n } ^ { - 1 } \right]$ ) by a monomial factor $x - a$ by a bit of code like the following,

$\mathtt { c } [ \mathtt { n } ] = \mathtt { c } [ \mathtt { n } - 1 ]$ ;  
for ( $\scriptstyle \cdot j = \mathtt { n } - 1$ ; $\scriptstyle { \dot { \mathsf { J } } } > = 1$ ;j--) c[j] $= _ { \mathbb { C } }$ [j-1]-c[j]\*a;  
c[0] $\ast = ( - a )$ ;

Likewise, you divide a polynomial of degree n by a monomial factor $x - a$ (synthetic division again) using

rem=c[n];   
c[n] ${ = } 0$ .;   
for(i=n-1; $\scriptstyle \dot { 1 } > = 0$ ;i--) { swap $\eqcirc \mathbf { c }$ [i]; c[i]=rem; rem=swap+rem\*a;   
}

which leaves you with a new polynomial array and a numerical remainder rem.

Multiplication of two general polynomials involves straightforward summing of the products, each involving one coefficient from each polynomial. Division of two general polynomials, while it can be done awkwardly in the fashion taught using pencil and paper, is susceptible to a good deal of streamlining. Witness the following routine based on the algorithm in [3].

void poldiv(VecDoub_I &u, VecDoub_I &v, VecDoub_O &q, VecDoub_O &r)

Divide a polynomial u by a polynomial v, and return the quotient and remainder polynomials in q and r, respectively. The four polynomials are represented as vectors of coefficients, each starting with the constant term. There is no restriction on the relative lengths of u and $\mathtt { v }$ , and either may have trailing zeros (represent a lower degree polynomial than its length allows). q and r are returned with the size of u, but will usually have trailing zeros. {

Int k,j, $\mathbf { n } { = } \mathbf { u }$ .size()-1,nv=v.size()-1;   
while ( $\mathrm { \Delta \ n v ~ } > = \mathrm { \Delta ~ 0 }$ && v[nv] $\scriptstyle = = \ 0 .$ ) nv--;   
if (nv $< ~ 0$ ) throw("poldiv divide by zero polynomial");   
$\mathrm { ~ \tt ~ { ~ r ~ } ~ } = \mathrm { ~ \tt ~ { ~ u ~ } ~ }$ ; May do a resize.   
q.assign(u.size(),0.); May do a resize.   
for $( \mathtt { k } \mathrm { = n - n v } ; \mathtt { k } \mathrm { > } = 0 ; \mathtt { k } \mathrm { - } - )$ { q[k] $= x$ [nv+k]/v[nv]; for (j=nv+k-1;j>=k;j--) r[j] -= q[k]\*v[j-k];   
}   
for (j=nv; $\mathtt { i } < = \mathtt { n }$ ;j $^ { + + }$ ) r[j] $= 0 . 0$ ;

# 5.1.1 Rational Functions

You evaluate a rational function like

$$
R ( x ) = { \frac { P _ { \mu } ( x ) } { Q _ { \nu } ( x ) } } = { \frac { p _ { 0 } + p _ { 1 } x + \dots + p _ { \mu } x ^ { \mu } } { q _ { 0 } + q _ { 1 } x + \dots + q _ { \nu } x ^ { \nu } } }
$$

in the obvious way, namely as two separate polynomials followed by a divide. As a matter of convention one usually chooses $q _ { 0 } = 1$ , obtained by dividing the numerator and denominator by any other $q _ { 0 }$ . In that case, it is often convenient to have both sets of coefficients, omitting $q _ { 0 }$ , stored in a single array, in the order

$$
( p _ { 0 } , p _ { 1 } , \ldots , p _ { \mu } , q _ { 1 } , \ldots , q _ { \nu } )
$$

The following object encapsulates a rational function. It provides constructors from either separate numerator and denominator polynomials, or a single array like (5.1.5) with explicit values for ${ \tt n } = \mu + 1$ and $\mathtt { d } = \nu + 1$ . The evaluation function makes Ratfn a functor, like Poly. We’ll make use of this object in $\ S 5 . 1 2$ and $\ S 5 . 1 3$ .

# struct Ratfn {

Function object for a rational function.

Ratfn(VecDoub_I &num, VecDoub_I &den) : cofs(num.size()+den.size()-1),   
nn(num.size()), dd(den.size()) {   
Constructor from numerator, denominator polyomials (as coefficient vectors). Int j; for (j=0;j<nn;j $^ { + + }$ ) cofs[j] $=$ num[j]/den[0]; for (j $= 1$ ;j<dd;j $^ { + + }$ ) cofs[j+nn-1] $=$ den[j]/den[0];   
}

Ratfn(VecDoub_I &coffs, const Int n, const Int d) : cofs(coffs), nn(n), dd(d) {} Constructor from coefficients already normalized and in a single array.

Doub operator() (Doub x) const {  
Evaluate the rational function at $\mathbf { x }$ and return result.Int j;Doub sumn $\mathit { \Theta } = \mathit { \Theta } 0 .$ , sumd $\qquad = \ 0$ .;for ( $\scriptstyle { \mathrm { j } = \mathrm { n n - 1 } }$ ; $\scriptstyle { \dot { \mathcal { I } } } > = 0$ ;j--) sumn $=$ sumn\*x $^ +$ cofs[j];for (j=nn+dd-2;j>=nn;j--) sumd $=$ sumd\*x $^ +$ cofs[j];return sumn/(1. $^ { 0 + }$ x\*sumd);  
}

};

# 5.1.2 Parallel Evaluation of a Polynomial

A polynomial of degree $N$ can be evaluated in about $\log _ { 2 } N$ parallel steps [6]. This is best illustrated by an example, for example with $N = 5$ . Start with the vector of coefficients, imagining appended zeros:

$$
c _ { 0 } , \quad c _ { 1 } , \quad c _ { 2 } , \quad c _ { 3 } , \quad c _ { 4 } , \quad c _ { 5 } , \quad 0 , \quad \ldots .
$$

Now add the elements by pairs, multiplying the second of each pair by $x$ :

$$
c _ { 0 } + c _ { 1 } x , \quad c _ { 2 } + c _ { 3 } x , \quad c _ { 4 } + c _ { 5 } x , \quad 0 , \quad . . .
$$

Now the same operation, but with the multiplier $x ^ { 2 }$ :

$$
( c _ { 0 } + c _ { 1 } x ) + ( c _ { 2 } + c _ { 3 } x ) x ^ { 2 } , \quad ( c _ { 4 } + c _ { 5 } x ) + ( 0 ) x ^ { 2 } , \quad 0 \quad . . .
$$

And a final time with multiplier $x ^ { 4 }$ :

$$
[ ( c _ { 0 } + c _ { 1 } x ) + ( c _ { 2 } + c _ { 3 } x ) x ^ { 2 } ] + [ ( c _ { 4 } + c _ { 5 } x ) + ( 0 ) x ^ { 2 } ] x ^ { 4 } , \quad 0 \quad . . .
$$

We are left with a vector of (active) length 1, whose value is the desired polynomial evaluation. You can see that the zeros are just a bookkeeping device for taking care of the case where the active subvector has an odd length; in an actual implementation you can avoid most operations on the zeros. This parallel method generally has better roundoff properties than the standard sequential coding.

# CITED REFERENCES AND FURTHER READING:

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), pp. 183, 190.[1]

Mathews, J., and Walker, R.L. 1970, Mathematical Methods of Physics, 2nd ed. (Reading, MA: W.A. Benjamin/Addison-Wesley), pp. 361–363.[2]   
Knuth, D.E. 1997, Seminumerical Algorithms, 3rd ed., vol. 2 of The Art of Computer Programming (Reading, MA: Addison-Wesley), $\ S 4 . 6 . [ 3 ]$   
Fike, C.T. 1968, Computer Evaluation of Mathematical Functions (Englewood Cliffs, NJ: Prentice-Hall), Chapter 4.   
Winograd, S. 1970, “On the number of multiplications necessary to compute certain functions,” Communications on Pure and Applied Mathematics,vol.23,pp.165-179.[4]   
Kronsjö, L. 1987, Algorithms: Their Complexity and Efficiency, 2nd ed. (New York: Wiley).[5]   
Estrin, G. 1960, quoted in Knuth, D.E. 1997, Seminumerical Algorithms, 3rd ed., vol. 2 of The Art of Computer Programming (Reading, MA: Addison-Wesley), $\ S 4 . 6 . 4 . [ 6 ]$

# 5.2 Evaluation of Continued Fractions

Continued fractions are often powerful ways of evaluating functions that occur in scientific applications. A continued fraction looks like this:

$$
f ( x ) = b _ { 0 } + { \frac { a _ { 1 } } { b _ { 1 } + { \frac { a _ { 2 } } { b _ { 2 } + { \frac { a _ { 3 } } { b _ { 3 } + { \frac { a _ { 4 } } { b _ { 4 } + { \frac { a _ { 5 } } { b _ { 5 } + \cdots } } } } } } } } } } 
$$

Printers prefer to write this as

$$
f ( x ) = b _ { 0 } + { \frac { a _ { 1 } } { b _ { 1 } + } } { \frac { a _ { 2 } } { b _ { 2 } + } } { \frac { a _ { 3 } } { b _ { 3 } + } } { \frac { a _ { 4 } } { b _ { 4 } + } } { \frac { a _ { 5 } } { b _ { 5 } + } } \cdots
$$

In either (5.2.1) or (5.2.2), the $a$ ’s and $b$ ’s can themselves be functions of $x$ , usually linear or quadratic monomials at worst (i.e., constants times $x$ or times $x ^ { 2 }$ ). For example, the continued fraction representation of the tangent function is

$$
\tan x = { \frac { x } { 1 - } } { \frac { x ^ { 2 } } { 3 - } } { \frac { x ^ { 2 } } { 5 - } } { \frac { x ^ { 2 } } { 7 - } } \cdots
$$

Continued fractions frequently converge much more rapidly than power series expansions, and in a much larger domain in the complex plane (not necessarily including the domain of convergence of the series, however). Sometimes the continued fraction converges best where the series does worst, although this is not a general rule. Blanch [1] gives a good review of the most useful convergence tests for continued fractions.

There are standard techniques, including the important quotient-difference algorithm, for going back and forth between continued fraction approximations, power series approximations, and rational function approximations. Consult Acton [2] for an introduction to this subject, and Fike [3] for further details and references.

How do you tell how far to go when evaluating a continued fraction? Unlike a series, you can’t just evaluate equation (5.2.1) from left to right, stopping when the change is small. Written in the form of (5.2.1), the only way to evaluate the continued fraction is from right to left, first (blindly!) guessing how far out to start. This is not the right way.

The right way is to use a result that relates continued fractions to rational approximations, and that gives a means of evaluating (5.2.1) or (5.2.2) from left to right. Let $f _ { n }$ denote the result of evaluating (5.2.2) with coefficients through $a _ { n }$ and $b _ { n }$ . Then

$$
f _ { n } = { \frac { A _ { n } } { B _ { n } } }
$$

where $A _ { n }$ and $B _ { n }$ are given by the following recurrence:

$$
\begin{array} { l } { { A _ { - 1 } \equiv 1 \qquad B _ { - 1 } \equiv 0 } } \\ { { \ } } \\ { { A _ { 0 } \equiv b _ { 0 } \qquad B _ { 0 } \equiv 1 } } \\ { { \ } } \\ { { A _ { j } = b _ { j } A _ { j - 1 } + a _ { j } A _ { j - 2 } \qquad B _ { j } = b _ { j } B _ { j - 1 } + a _ { j } B _ { j - 2 } \qquad j = 1 , 2 , \ldots , n } } \end{array}
$$

This method was invented by J. Wallis in 1655 (!) and is discussed in his Arithmetica Infinitorum [4]. You can easily prove it by induction.

In practice, this algorithm has some unattractive features: The recurrence (5.2.5) frequently generates very large or very small values for the partial numerators and denominators $A _ { j }$ and $B _ { j }$ . There is thus the danger of overflow or underflow of the floating-point representation. However, the recurrence (5.2.5) is linear in the $A$ ’s and $B$ ’s. At any point you can rescale the currently saved two levels of the recurrence, e.g., divide $A _ { j } , B _ { j } , A _ { j - 1 }$ ; and $B _ { j - 1 }$ all by $B _ { j }$ . This incidentally makes $A _ { j } = f _ { j }$ and is convenient for testing whether you have gone far enough: See if $f _ { j }$ and $f _ { j - 1 }$ from the last iteration are as close as you would like them to be. If $B _ { j }$ happens to be zero, which can happen, just skip the renormalization for this cycle. A fancier level of optimization is to renormalize only when an overflow is imminent, saving the unnecessary divides. In fact, the C library function ldexp can be used to avoid division entirely. (See the end of $\ S 6 . 5$ for an example.)

Two newer algorithms have been proposed for evaluating continued fractions. Steed’s method does not use $A _ { j }$ and $B _ { j }$ explicitly, but only the ratio $D _ { j } = B _ { j - 1 } / B _ { j }$ . One calculates $D _ { j }$ and $\Delta f _ { j } = f _ { j } - f _ { j - 1 }$ recursively using

$$
\begin{array} { r } { D _ { j } = 1 / ( b _ { j } + a _ { j } D _ { j - 1 } ) } \\ { \Delta f _ { j } = ( b _ { j } D _ { j } - 1 ) \Delta f _ { j - 1 } } \end{array}
$$

Steed’s method (see, e.g., [5]) avoids the need for rescaling of intermediate results. However, for certain continued fractions you can occasionally run into a situation where the denominator in (5.2.6) approaches zero, so that $D _ { j }$ and $\Delta f _ { j }$ are very large. The next $\Delta f _ { j + 1 }$ will typically cancel this large change, but with loss of accuracy in the numerical running sum of the $f _ { j }$ ’s. It is awkward to program around this, so Steed’s method can be recommended only for cases where you know in advance that no denominator can vanish. We will use it for a special purpose in the routine besselik $( \ S 6 . 6 )$ .

The best general method for evaluating continued fractions seems to be the modified Lentz’s method [6]. The need for rescaling intermediate results is avoided by using both the ratios

$$
C _ { j } = A _ { j } / A _ { j - 1 } , \qquad D _ { j } = B _ { j - 1 } / B _ { j }
$$

and calculating $f _ { j }$ by

$$
f _ { j } = f _ { j - 1 } C _ { j } D _ { j }
$$

From equation (5.2.5), one easily shows that the ratios satisfy the recurrence relations

$$
D _ { j } = 1 / ( b _ { j } + a _ { j } D _ { j - 1 } ) , \qquad C _ { j } = b _ { j } + a _ { j } / C _ { j - 1 }
$$

In this algorithm there is the danger that the denominator in the expression for $D _ { j }$ , or the quantity $C _ { j }$ itself, might approach zero. Either of these conditions invalidates (5.2.10). However, Thompson and Barnett [5] show how to modify Lentz’s algorithm to fix this: Just shift the offending term by a small amount, e.g., $1 0 ^ { - 3 0 }$ . If you work through a cycle of the algorithm with this prescription, you will see that $f _ { j + 1 }$ is accurately calculated.

In detail, the modified Lentz’s algorithm is this:

- Set $f _ { 0 } = b _ { 0 }$ ; if $b _ { 0 } = 0$ , set $f _ { 0 } = \mathtt { t i n y }$ .   
- Set $C _ { 0 } = f _ { 0 }$ .   
- Set $D _ { 0 } = 0$ .   
- For $j = 1 , 2 , \dots$ Set $D _ { j } = b _ { j } + a _ { j } D _ { j - 1 }$ . If $D _ { j } = 0$ , set $D _ { j } = \mathtt { t i n y }$ . Set $C _ { j } = b _ { j } + a _ { j } / C _ { j - 1 }$ . If $C _ { j } = 0$ , set $C _ { j } = \mathtt { t i n y }$ . Set $D _ { j } = 1 / D _ { j }$ . Set $\Delta _ { j } = C _ { j } D _ { j }$ . Set $f _ { j } = f _ { j - 1 } \Delta _ { j }$ . If $| \Delta _ { j } - 1 | < \mathsf { e p s }$ , then exit.

Here eps is your floating-point precision, say $1 0 ^ { - 7 }$ or $1 0 ^ { - 1 5 }$ . The parameter tiny should be less than typical values of eps $| b _ { j } |$ , say $1 0 ^ { - 3 0 }$ .

The above algorithm assumes that you can terminate the evaluation of the continued fraction when $\lvert f _ { j } - f _ { j - 1 } \rvert$ is sufficiently small. This is usually the case, but by no means guaranteed. Jones [7] gives a list of theorems that can be used to justify this termination criterion for various kinds of continued fractions.

There is at present no rigorous analysis of error propagation in Lentz’s algorithm. However, empirical tests suggest that it is at least as good as other methods.

# 5.2.1 Manipulating Continued Fractions

Several important properties of continued fractions can be used to rewrite them in forms that can speed up numerical computation. An equivalence transformation

$$
a _ { n }  \lambda a _ { n } , \quad b _ { n }  \lambda b _ { n } , \quad a _ { n + 1 }  \lambda a _ { n + 1 }
$$

leaves the value of a continued fraction unchanged. By a suitable choice of the scale factor $\lambda$ you can often simplify the form of the $a$ ’s and the $b$ ’s. Of course, you can carry out successive equivalence transformations, possibly with different $\lambda$ ’s, on successive terms of the continued fraction.

The even and odd parts of a continued fraction are continued fractions whose successive convergents are $f _ { 2 n }$ and $f _ { 2 n + 1 }$ , respectively. Their main use is that they converge twice as fast as the original continued fraction, and so if their terms are not much more complicated than the terms in the original, there can be a big savings in computation. The formula for the even part of (5.2.2) is

$$
f _ { \mathrm { e v e n } } = d _ { 0 } + { \frac { c _ { 1 } } { d _ { 1 } + } } { \frac { c _ { 2 } } { d _ { 2 } + } } \cdots
$$

where in terms of intermediate variables

$$
\begin{array} { l } { \displaystyle \alpha _ { 1 } = \frac { a _ { 1 } } { b _ { 1 } } } \\ { \displaystyle \alpha _ { n } = \frac { a _ { n } } { b _ { n } b _ { n - 1 } } , \qquad n \ge 2 } \end{array}
$$

we have

$$
\begin{array} { r l } { d _ { 0 } = b _ { 0 } , } & { { } c _ { 1 } = \alpha _ { 1 } , \quad d _ { 1 } = 1 + \alpha _ { 2 } } \\ { \quad } & { { } c _ { n } = - \alpha _ { 2 n - 1 } \alpha _ { 2 n - 2 } , \quad d _ { n } = 1 + \alpha _ { 2 n - 1 } + \alpha _ { 2 n } , \qquad n \geq 2 } \end{array}
$$

You can find the similar formula for the odd part in the review by Blanch [1]. Often a combination of the transformations (5.2.14) and (5.2.11) is used to get the best form for numerical work.

We will make frequent use of continued fractions in the next chapter.

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, $\ S 3 . 1 0$ .   
Blanch, G. 1964, “Numerical Evaluation of Continued Fractions,” SIAM Review, vol. 6, pp. 383– 421.[1]   
Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), Chapter 11.[2]   
Cuyt, A., and Wuytack, L. 1987, Nonlinear Methods in Numerical Analysis (Amsterdam: North-Holland), Chapter 1.   
Fike, C.T. 1968, Computer Evaluation of Mathematical Functions (Englewood Cliffs, NJ: Prentice-Hall), $\ S 8 . 2$ , $\ S 1 0 . 4$ , and $\ S 1 0 . 5$ .[3]   
Wallis, J. 1695, in Opera Mathematica, vol. 1, p. 355, Oxoniae e Theatro Shedoniano. Reprinted by Georg Olms Verlag, Hildeshein, New York (1972).[4]   
Thompson, I.J., and Barnett, A.R. 1986, “Coulomb and Bessel Functions of Complex Arguments and Order,” Journal of Computational Physics, vol. 64, pp. 490–509.[5]   
Lentz, W.J. 1976, “Generating Bessel Functions in Mie Scattering Calculations Using Continued Fractions,” Applied Optics, vol. 15, pp. 668–671.[6]   
Jones, W.B. 1973, in Padé Approximants and Their Applications, P.R. Graves-Morris, ed. (London: Academic Press), p. 125.[7]

# 5.3 Series and Their Convergence

Everybody knows that an analytic function can be expanded in the neighborhood of a point $x _ { 0 }$ in a power series,

$$
f ( x ) = \sum _ { k = 0 } ^ { \infty } a _ { k } ( x - x _ { 0 } ) ^ { k }
$$

Such series are straightforward to evaluate. You don’t, of course, evaluate the $k$ th power of $x - x _ { 0 }$ ab initio for each term; rather, you keep the $k - 1$ st power and update it with a multiply. Similarly, the form of the coefficients $a _ { k }$ is often such as to make use of previous work: Terms like $k !$ or $( 2 k )$ Š can be updated in a multiply or two.

How do you know when you have summed enough terms? In practice, the terms had better be getting small fast, otherwise the series is not a good technique to use in the first place. While not mathematically rigorous in all cases, standard practice is to quit when the term you have just added is smaller in magnitude than some small $\epsilon$ times the magnitude of the sum thus far accumulated. (But watch out if isolated instances of $a _ { k } = 0$ are possible!)

Sometimes you will want to compute a function from a series representation even when the computation is not efficient. For example, you may be using the values obtained to fit the function to an approximating form that you will use subsequently (cf. -5.8). If you are summing very large numbers of slowly convergent terms, pay attention to roundoff errors! In floating-point representation it is more accurate to sum a list of numbers in the order starting with the smallest one, rather than starting with the largest one. It is even better to group terms pairwise, then in pairs of pairs, etc., so that all additions involve operands of comparable magnitude.

A weakness of a power series representation is that it is guaranteed not to converge farther than that distance from $x _ { 0 }$ at which a singularity is encountered in the complex plane. This catastrophe is not usually unexpected: When you find a power series in a book (or when you work one out yourself), you will generally also know the radius of convergence. An insidious problem occurs with series that converge everywhere (in the mathematical sense), but almost nowhere fast enough to be useful in a numerical method. Two familiar examples are the sine function and the Bessel function of the first kind,

$$
\begin{array} { c } { \displaystyle \sin x = \displaystyle \sum _ { k = 0 } ^ { \infty } \frac { ( - 1 ) ^ { k } } { ( 2 k + 1 ) ! } x ^ { 2 k + 1 } } \\ { \displaystyle J _ { n } ( x ) = \left( \frac { x } { 2 } \right) ^ { n } \sum _ { k = 0 } ^ { \infty } \frac { ( - \frac { 1 } { 4 } x ^ { 2 } ) ^ { k } } { k ! ( k + n ) ! } } \end{array}
$$

Both of these series converge for all $x$ . But both don’t even start to converge until $k \gg | x |$ ; before this, their terms are increasing. Even worse, the terms alternate in sign, leading to large cancellation errors with finite precision arithmetic. This makes these series useless for large $x$ .

# 5.3.1 Divergent Series

Divergent series are often very useful. One class consists of power series outside their radius of convergence, which can often be summed by the acceleration techniques we will describe below. Another class is asymptotic series, such as the Euler series that comes from Euler’s integral (related to the exponential integral $E _ { 1 }$ ):

$$
E ( x ) = \int _ { 0 } ^ { \infty } { \frac { e ^ { - t } } { 1 + x t } } d t \simeq \sum _ { k = 0 } ^ { \infty } ( - 1 ) ^ { k } k ! x ^ { k }
$$

Here the series is derived by expanding $( 1 + x t ) ^ { - 1 }$ in powers of $x$ and integrating term by term. The series diverges for all $x \neq 0$ . For $x \ = \ 0 . 1$ , the series gives only three significant digits before diverging. Nevertheless, convergence acceleration

techniques allow effortless evaluation of the function $E ( x )$ , even for $x \sim 2$ , when the series is wildly divergent!

# 5.3.2 Accelerating the Convergence of Series

There are several tricks for accelerating the rate of convergence of a series or, equivalently, of a sequence of partial sums

$$
s _ { n } = \sum _ { k = 0 } ^ { n } a _ { k }
$$

(We’ll use the terms sequence and series interchangeably in this section.) An excellent review has been given by Weniger [1]. Before we can describe the tricks and when to use them, we need to classify some of the ways in which a sequence can converge. Suppose $s _ { n }$ converges to $s$ , say, and that

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { a _ { n + 1 } } { a _ { n } } } = \rho
$$

If $0 < | \rho | < 1$ , we say the convergence is linear; if $\rho = 1$ , it is logarithmic; and if $\rho = 0$ , it is hyperlinear. Of course, if $| \rho | > 1$ , the sequence diverges. (More rigorously, this classification should be given in terms of the so-called remainders $s _ { n } \mathrm { ~ - ~ } s$ [1]. However, our definition is more practical and is equivalent if we restrict the logarithmic case to terms of the same sign.)

The prototype of linear convergence is a geometric series,

$$
s _ { n } = \sum _ { k = 0 } ^ { n } x ^ { k } = { \frac { 1 - x ^ { n + 1 } } { 1 - x } }
$$

It is easy to see that $\rho = x$ , and so we have linear convergence for $0 < | x | < 1$ . The prototype of logarithmic convergence is the series for the Riemann zeta function,

$$
\zeta ( x ) = \sum _ { k = 1 } ^ { \infty } { \frac { 1 } { k ^ { x } } } , \qquad x > 1
$$

which is notoriously slowly convergent, especially as $x \ \to \ 1$ . The series (5.3.2) and (5.3.3), or the series for $e ^ { x }$ , exemplify hyperlinear convergence. We see that hyperlinear convergence doesn’t necessarily imply that the series is easy to evaluate for all values of $x$ . Sometimes convergence acceleration is helpful only once the terms start decreasing.

Probably the most famous series transformation for accelerating convergence is the Euler transformation (see, e.g., [2,3]), which dates from 1755. Euler’s transformation works on alternating series (where the terms in the sum alternate in sign). Generally it is advisable to do a small number of terms directly, through term $n - 1$ , say, and then apply the transformation to the rest of the series beginning with term $n$ . The formula (for $n$ even) is

$$
\sum _ { s = 0 } ^ { \infty } ( - 1 ) ^ { s } a _ { s } = a _ { 0 } - a _ { 1 } + a _ { 2 } \ldots - a _ { n - 1 } + \sum _ { s = 0 } ^ { \infty } \frac { ( - 1 ) ^ { s } } { 2 ^ { s + 1 } } [ \Delta ^ { s } a _ { n } ]
$$

Here $\Delta$ is the forward difference operator, i.e.,

$$
\begin{array} { c } { \Delta a _ { n } \equiv a _ { n + 1 } - a _ { n } } \\ { \Delta ^ { 2 } a _ { n } \equiv a _ { n + 2 } - 2 a _ { n + 1 } + a _ { n } } \\ { \Delta ^ { 3 } a _ { n } \equiv a _ { n + 3 } - 3 a _ { n + 2 } + 3 a _ { n + 1 } - a _ { n } } \end{array}
$$

etc.

Of course you don’t actually do the infinite sum on the right-hand side of (5.3.9), but only the first, say, $p$ terms, thus requiring the first $p$ differences (5.3.10) obtained from the terms starting at $a _ { n }$ . There is an elegant and subtle implementation of Euler’s transformation due to van Wijngaarden [6], discussed in full in a Webnote [7].

Euler’s transformation is an example of a linear transformation: The partial sums of the transformed series are linear combinations of the partial sums of the original series. Euler’s transformation and other linear transformations, while still important theoretically, have generally been superseded by newer nonlinear transformations that are considerably more powerful. As usual in numerical work, there is no free lunch: While the nonlinear transformations are more powerful, they are somewhat riskier than linear transformations in that they can occasionally fail spectacularly. But if you follow the guidance below, we think that you will never again resort to puny linear transformations.

The oldest example of a nonlinear sequence transformation is Aitken’s $\Delta ^ { 2 }$ - process. If $s _ { n } , s _ { n + 1 } , s _ { n + 2 }$ are three successive partial sums, then an improved estimate is

$$
s _ { n } ^ { \prime } \equiv s _ { n } - \frac { ( s _ { n + 1 } - s _ { n } ) ^ { 2 } } { s _ { n + 2 } - 2 s _ { n + 1 } + s _ { n } } = s _ { n } - \frac { ( \Delta s _ { n } ) ^ { 2 } } { \Delta ^ { 2 } s _ { n } }
$$

The formula (5.3.11) is exact for a geometric series, which is one way of deriving it. If you form the sequence of $s _ { i } ^ { \prime }$ ’s, you can apply (5.3.11) a second time to that sequence, and so on. (In practice, this iteration will only rarely do much for you after the first stage.) Note that equation (5.3.11) should be computed as written; there exist algebraically equivalent forms that are much more susceptible to roundoff error.

Aitken’s $\Delta ^ { 2 }$ -process works only on linearly convergent sequences. Like Euler’s transformation, it has also been superseded by algorithms such as the two we will now describe. After giving routines for these algorithms, we will supply some rules of thumb on when to use them.

The first “modern” nonlinear transformation was proposed by Shanks. An efficient recursive implementation was given by Wynn, called the $\epsilon$ algorithm. Aitken’s $\Delta ^ { 2 }$ -process is a special case of the $\epsilon$ algorithm, corresponding to using just three terms at a time. Although we will not give a derivation here, it is easy to state exactly what the $\epsilon$ algorithm does: If you input the partial sums of a power series, the $\epsilon$ algorithm returns the “diagonal” Pade approximants ( ´ -5.12) evaluated at the value of $x$ used in the power series. (The coefficients in the approximant itself are not calculated.) That is, if $[ M / N ]$ denotes the Pade approximant with a polynomial of ´ degree $M$ in the numerator and degree $N$ in the denominator, the algorithm returns the numerical values of the approximants

Œ0; 0; Œ1=0; Œ1=1; Œ2=1; Œ2=2; Œ3; 2; Œ3; 3 (The object Epsalg below is roughly equivalent to pade in $\ S 5 . 1 2$ followed by an evaluation of the resulting rational function.)

In the object Epsalg, which is based on a routine in [1], you supply the sequence term by term and monitor the output for convergence in the calling program. Internally, the routine contains a check for division by zero and substitutes a large number for the result. There are three conditions under which this check can be triggered: (i) Most likely, the algorithm has already converged, and should have been stopped earlier; (ii) there is an “accidental” zero term, and the program will recover; (iii) hardly ever in practice, the algorithm can actually fail because of a perverse combination of terms. Because (i) and (ii) are vastly more common than (iii), Epsalg hides the check condition and instead returns the last-known good estimate.

# struct Epsalg {

Convergence acceleration of a sequence by the  algorithm. Initialize by calling the constructor with arguments nmax, an upper bound on the number of terms to be summed, and epss, the desired accuracy. Then make successive calls to the function next, with argument the next partial sum of the sequence. The current estimate of the limit of the sequence is returned by next. The flag cnvgd is set when convergence is detected.

VecDoub e; Workspace.   
Int n,ncv;   
Bool cnvgd;   
Doub eps,small,big,lastval,lasteps; Numbers near machine underflow a overflow limits.   
Epsalg(Int nmax, Doub epss) : e(nmax), n(0), ncv(0),   
cnvgd(0), eps(epss), lastval(0.) { small $=$ numeric_limits<Doub>::min()\*10.0; big $=$ numeric_limits<Doub>::max();   
}   
Doub next(Doub sum) { Doub diff,temp1,temp2,val; e[n] $=$ sum; temp2=0.0; for (Int $\scriptstyle { \dot { \mathbf { J } } } = { \mathbf { n } }$ ; $\mathrm { j } > 0$ ; j--) { temp1 $=$ temp2; temp2=e[j-1]; diff $\mathtt { \mathtt { \mathtt { = e } } }$ [j]-temp2; if (abs(diff) $< =$ small) e[j-1] $=$ big; else e[j-1] $=$ temp1+1.0/diff; } $\mathtt { n } + +$ ; val $=$ (n & 1) ? e[0] : e[1]; Cases of n even or odd. if (abs(val) $>$ 0.01\*big) val $=$ lastval; lasteps $=$ abs(val-lastval); if (lasteps $>$ eps) ncv $\qquad = \ 0$ ; else ncv++; if (ncv $\scriptstyle > = \ 3 .$ ) cnvgd $\ l = \ 1$ ; return (lastval $\mathbf { \mu } = \mathbf { \mu } \mathtt { v a l } .$ );   
}

# };

The last few lines above implement a simple criterion for deciding whether the sequence has converged. For problems whose convergence is robust, you can simply put your calls to next inside a while loop like this:

Doub val, partialsum, eps $=$ ...   
Epsalg mysum(1000,eps);   
while (! mysum.cnvgd) { partialsum $=$ val $=$ mysum.next(partialsum);   
}

For more delicate cases, you can ignore the cnvgd flag and just keep calling next until you are satisfied with the convergence.

A large class of modern nonlinear transformations can be derived by using the concept of a model sequence. The idea is to choose a “simple” sequence that approximates the asymptotic form of the given sequence and construct a transformation that sums the model sequence exactly. Presumably the transformation will work well for other sequences with similar asymptotic properties. For example, a geometric series provides the model sequence for Aitken’s $\Delta ^ { 2 }$ -process.

The Levin transformation is probably the best single sequence acceleration method currently known. It is based on approximating a sequence asymptotically by an expression of the form

$$
s _ { n } = s + \omega _ { n } \sum _ { j = 0 } ^ { k - 1 } { \frac { c _ { j } } { ( n + \beta ) ^ { j } } }
$$

Here $\omega _ { n }$ is the dominant term in the remainder of the sequence:

$$
s _ { n } - s = \omega _ { n } [ c + O ( n ^ { - 1 } ) ] , \qquad n \to \infty
$$

The constants $c _ { j }$ are arbitrary, and $\beta$ is a parameter that is restricted to be positive. Levin showed that for a model sequence of the form (5.3.13), the following transformation gives the exact value of the series:

$$
s = { \frac { \displaystyle \sum _ { j = 0 } ^ { k } ( - 1 ) ^ { j } { \binom { k } { j } } { \frac { ( \beta + n + j ) ^ { k - 1 } } { ( \beta + n + k ) ^ { k - 1 } } } { \frac { s _ { n + j } } { \omega _ { n + j } } } } { \displaystyle \sum _ { j = 0 } ^ { k } ( - 1 ) ^ { j } { \binom { k } { j } } { \frac { ( \beta + n + j ) ^ { k - 1 } } { ( \beta + n + k ) ^ { k - 1 } } } { \frac { 1 } { \omega _ { n + j } } } } }
$$

(The common factor $( \beta + n + k ) ^ { k - 1 }$ in the numerator and denominator reduces the chances of overflow for large $k$ .) A derivation of equation (5.3.15) is given in a Webnote [4].

The numerator and denominator in (5.3.15) are not computed as written. Instead, they can be computed efficiently from a single recurrence relation with different starting values (see [1] for a derivation):

$$
D _ { k + 1 } ^ { n } ( \beta ) = D _ { k } ^ { n + 1 } ( \beta ) - \frac { ( \beta + n ) ( \beta + n + k ) ^ { k - 1 } } { ( \beta + n + k + 1 ) ^ { k } } D _ { k } ^ { n } ( \beta )
$$

The starting values are

$$
D _ { 0 } ^ { n } ( \beta ) = \left\{ \begin{array} { l l } { s _ { n } / \omega _ { n } , } & { \mathrm { n u m e r a t o r } } \\ { 1 / \omega _ { n } , } & { \mathrm { d e n o m i n a t o r } } \end{array} \right.
$$

Although $D _ { k } ^ { n }$ is a two-dimensional object, the recurrence can be coded in a onedimensional array proceeding up the counterdiagonal $n + k =$ constant.

The choice (5.3.14) doesn’t determine $\omega _ { n }$ uniquely, but if you have analytic information about your series, this is where you can make use of it. Usually you won’t be so lucky, in which case you can make a choice based on heuristics. For example, the remainder in an alternating series is approximately half the first neglected term, which suggests setting $\omega _ { n }$ equal to $a _ { n }$ or $a _ { n + 1 }$ . These are called the Levin $t$ and $d$ transformations, respectively. Similarly, the remainder for a geometric series is the difference between the partial sum (5.3.7) and its limit $1 / ( 1 - x )$ . This can be written as $a _ { n } a _ { n + 1 } / ( a _ { n } - a _ { n + 1 } )$ , which defines the Levin $v$ transformation. The most popular choice comes from approximating the remainder in the $\zeta$ function (5.3.8) by an integral:

$$
\sum _ { k = n + 1 } ^ { \infty } { \frac { 1 } { k ^ { x } } } \approx \int _ { n + 1 } ^ { \infty } { \frac { d k } { k ^ { x } } } = { \frac { ( n + 1 ) ^ { 1 - x } } { x - 1 } } = { \frac { ( n + 1 ) a _ { n + 1 } } { x - 1 } }
$$

This motivates the choice $( n + \beta ) a _ { n }$ (Levin $u$ transformation), where $\beta$ is usually chosen to be 1. To summarize:

$$
\omega _ { n } = \left\{ \begin{array} { l l } { ( \beta + n ) a _ { n } , } & { u \mathrm { ~ t r a n s f o r m a t i o n } } \\ { a _ { n } , } & { t \mathrm { ~ t r a n s f o r m a t i o n } } \\ { a _ { n + 1 } , } & { d \mathrm { ~ t r a n s f o r m a t i o n } \mathrm { ( m o d i f i e d ~ } t \mathrm { ~ t r a n s f o r m a t i o n ) } } \\ { \frac { a _ { n } a _ { n + 1 } } { a _ { n } - a _ { n + 1 } } , } & { v \mathrm { ~ t r a n s f o r m a t i o n } } \end{array} \right.
$$

For sequences that are not partial sums, so that the individual $a _ { n }$ ’s are not defined, replace $a _ { n }$ by $\Delta s _ { n - 1 }$ in (5.3.19).

Here is the routine for Levin’s transformation, also based on the routine in [1]:

# struct Levin {

Convergence acceleration of a sequence by the Levin transformation. Initialize by calling the constructor with arguments nmax, an upper bound on the number of terms to be summed, and epss, the desired accuracy. Then make successive calls to the function next, which returns the current estimate of the limit of the sequence. The flag cnvgd is set when convergence is detected.

Numerator and denominator computed via (5.3.16).

VecDoub numer,denom;   
Int n,ncv;   
Bool cnvgd;   
Doub small,big;   
Doub eps,lastval,lasteps;

Numbers near machine underflow and overflow limits.

Levin(Int nmax, Doub epss) : numer(nmax), denom(nmax), n(0), ncv(0),   
cnvgd(0), eps(epss), lastval(0.) { small $\equiv$ numeric_limits<Doub>::min()\*10.0; big=numeric_limits<Doub>::max();   
}

Doub next(Doub sum, Doub omega, Doub beta $^ { = 1 }$ .) {

Arguments: sum, the nth partial sum of the sequence; omega, the nth remainder estimate $\omega _ { n }$ , usually from (5.3.19); and the parameter beta, which should usually be set to 1, but sometimes 0.5 works better. The current estimate of the limit of the sequence is returned.

Int j;   
Doub fact,ratio,term,val;   
term $^ { = 1 }$ .0/(beta+n);   
denom[n] $=$ term/omega;   
numer[n] $=$ sum\*denom[n];   
if $\mathbf { \Phi } ( \mathbf { n } \mathbf { \Phi } > \mathbf { \Phi } 0 ) .$ ) { ratio $=$ (beta+n-1)\*term; for ( $\scriptstyle { \dot { \ j } } = 1$ ;j $< = _ { \mathrm { n } }$ ; $\mathrm { j } + +$ ) {

fact $=$ (n-j+beta)\*term; numer[n-j] $=$ numer[n-j+1]-fact\*numer[n-j]; denom[n-j] $=$ denom[n-j+1]-fact\*denom[n-j]; term=term\*ratio; } } $\mathrm { n } { + } { + }$ ; val $=$ abs(denom[0]) $<$ small ? lastval : numer[0]/denom[0]; lasteps $=$ abs(val-lastval); if (lasteps $< =$ eps) ncv++; if (ncv $> = ~ 2 ^ { \prime } .$ ) cnvgd $\ l = \ 1$ ; return (lastval $=$ val); } };

You can use, or not use, the cnvgd flag exactly as previously discussed for Epsalg.

An alternative to the model sequence method of deriving sequence transformations is to use extrapolation of a polynomial or rational function approximation to a series, e.g., as in Wynn’s $\rho$ algorithm [1]. Since none of these methods generally beats the two we have given, we won’t say any more about them.

# 5.3.3 Practical Hints and an Example

There is no general theoretical understanding of nonlinear sequence transformations. Accordingly, most of the practical advice is based on numerical experiments [5]. You might have thought that summing a wildly divergent series is the hardest problem for a sequence transformation. However, the difficulty of a problem depends more on whether the terms are all of the same sign or whether the signs alternate, rather than whether the sequence actually converges or not. In particular, logarithmically convergent series with terms all of the same sign are generally the most difficult to sum. Even the best acceleration methods are corrupted by rounding errors when accelerating logarithmic convergence. You should always use double precision and be prepared for some loss of significant digits. Typically one observes convergence up to some optimum number of terms, and then a loss of significant digits if one tries to go further. Moreover, there is no single algorithm that can accelerate every logarithmically convergent sequence. Nevertheless, there are some good rules of thumb.

First, note that among divergent series it is useful to separate out asymptotic series, where the terms first decrease before increasing, as a separate class from other divergent series, e.g., power series outside their radius of convergence. For alternating series, whether convergent, asymptotic, or divergent power series, Levin’s $u$ transformation is almost always the best choice. For monotonic linearly convergent or monotonic divergent power series, the $\epsilon$ algorithm typically is the first choice, but the $u$ transformation often does a reasonable job. For logarithmic convergence, the $u$ transformation is clearly the best. (The $\epsilon$ algorithm fails completely.) For series with irregular signs or other nonstandard features, typically the $\epsilon$ algorithm is relatively robust, often succeeding where other algorithms fail. Finally, for monotonic asymptotic series, such as (6.3.11) for $\operatorname { E i } ( x )$ , there is nothing better than direct summation without acceleration.

The $v$ and $t$ transformations are almost as good as the $u$ transformation, except that the $t$ transformation typically fails for logarithmic convergence.

If you have only a few numerical terms of some sequence and no theoretical insight, blindly applying a convergence accelerator can be dangerous. The algorithm can sometimes display “convergence” that is only apparent, not real. The remedy is to try two different transformations as a check.

Since convergence acceleration is so much more difficult for a series of positive terms than for an alternating series, occasionally it is useful to convert a series of positive terms into an alternating series. Van Wijngaarden has given a transformation for accomplishing this [6]:

$$
\sum _ { r = 1 } ^ { \infty } v _ { r } = \sum _ { r = 1 } ^ { \infty } ( - 1 ) ^ { r - 1 } w _ { r }
$$

where

$$
w _ { r } \equiv v _ { r } + 2 v _ { 2 r } + 4 v _ { 4 r } + 8 v _ { 8 r } + \cdots
$$

Equations (5.3.20) and (5.3.21) replace a simple sum by a two-dimensional sum, each term in (5.3.20) being itself an infinite sum (5.3.21). This may seem a strange way to save on work! Since, however, the indices in (5.3.21) increase tremendously rapidly, as powers of 2, it often requires only a few terms to converge (5.3.21) to extraordinary accuracy. You do, however, need to be able to compute the $v _ { r }$ ’s efficiently for “random” values $r$ . The standard “updating” tricks for sequential $r$ ’s, mentioned above following equation (5.3.1), can’t be used.

Once you’ve generated the alternating series by Van Wijngaarden’s transformation, the Levin $d$ transformation is particularly effective at summing the series [8]. This strategy is most useful for linearly convergent series with $\rho$ close to 1. For logarithmically convergent series, even the transformed series (5.3.21) is often too slowly convergent to be useful numerically.

As an example of how to call the routines Epsalg or Levin, consider the problem of evaluating the integral

$$
I = \int _ { 0 } ^ { \infty } { \frac { x } { 1 + x ^ { 2 } } } J _ { 0 } ( x ) d x = K _ { 0 } ( 1 ) = 0 . 4 2 1 0 2 4 4 3 8 2 \dots .
$$

Standard quadrature methods such as qromo fail because the integrand has a long oscillatory tail, giving alternating positive and negative contributions that tend to cancel. A good way of evaluating such an integral is to split it into a sum of integrals between successive zeros of $J _ { 0 } ( x )$ :

$$
I = \int _ { 0 } ^ { \infty } f ( x ) d x = \sum _ { j = 0 } ^ { \infty } I _ { j }
$$

where

$$
I _ { j } = \int _ { x _ { j - 1 } } ^ { x _ { j } } f ( x ) d x , \qquad f ( x _ { j } ) = 0 , \quad j = 0 , 1 , \ldots
$$

We take $x _ { - 1 }$ equal to the lower limit of the integral, zero in this example. The idea is to evaluate the relatively simple integrals $I _ { j }$ by qromb or Gaussian quadrature, and then accelerate the convergence of the series (5.3.23), since we expect the contributions to alternate in sign. For the example (5.3.22), we don’t even need accurate values of the zeros of $J _ { 0 } ( x )$ . It is good enough to take $x _ { j } = ( j + 1 ) \pi$ , which is asymptotically correct. Here is the code:

Doub func(const Doub x) Integrand for (5.3.22).

{ if $\mathit { \check { x } } = = \ 0 . 0 $ ) return 0.0; else { Bessel bess; return x\*bess.jnu(0.0,x)/(1.0+x\*x); }   
}

# Int main_levex(void)

This sample program shows how to use the Levin $\boldsymbol { u }$ transformation to evaluate an oscillatory integral, equation (5.3.22).

const Doub $\mathtt { P I } = 3$ .141592653589793;   
Int nterm $= 1 2$ ;   
Doub beta $= 1$ .0, $\mathtt { a } = 0$ .0, $\scriptstyle \mathtt { > } = 0$ .0,sum=0.0;   
Levin series(100,0.0);   
cout << setw(5) $< <$ "N" << setw(19) << "Sum (direct)" << setw(21) << "Sum (Levin)" << endl;   
for (Int $\mathtt { n } { = } 0$ ; $\mathbf { n } { < } =$ nterm; $\mathbf { n } { + } { + }$ ) { $\mathrm { b + = } \mathrm { P I }$ ; Doub $\tt { s } =$ qromb(func,a,b,1.e-8); a=b; sum $+ { = } { \tt s }$ ; Doub omega (beta+n)\*s; Use u transformation. Doub ans=series.next(sum,omega,beta); cout $< <$ setw(5) $< < \texttt { n } < <$ fixed $< <$ setprecision(14) << setw(21) << sum $< <$ setw(21) $< <$ ans $< <$ endl;   
}   
return 0;

Setting eps to $1 \times 1 0 ^ { - 8 }$ in qromb, we get 9 significant digits with about 200 function evaluations by $n = 8$ . Replacing qromb with a Gaussian quadrature routine cuts the number of function evaluations in half. Note that $n = 8$ corresponds to an upper limit in the integral of $9 \pi$ , where the amplitude of the integrand is still of order $1 0 ^ { - 2 }$ . This shows the remarkable power of convergence acceleration. (For more on oscillatory integrals, see $\ S 1 3 . 9 .$ )

# CITED REFERENCES AND FURTHER READING:

Weniger, E.J. 1989, “Nonlinear Sequence Transformations for the Acceleration of Convergence and the Summation of Divergent Series,” Computer Physics Reports, vol. 10, pp. 189– 371.[1]   
Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, $\ S 3 . 6$ .[2]   
Mathews, J., and Walker, R.L. 1970, Mathematical Methods of Physics, 2nd ed. (Reading, MA: W.A. Benjamin/Addison-Wesley), -2.3.[3]   
Numerical Recipes Software 2007, “Derivation of the Levin Transformation,” Numerical Recipes Webnote No. 6,at http://www.nr.com/webnotes?6 [4]   
Smith, D.A., and Ford, W.F. 1982, “Numerical Comparisons of Nonlinear Convergence Accelerators,” Mathematics of Computation, vol. 38, pp. 481–499.[5]   
Goodwin, E.T. (ed.) 1961, Modern Computing Methods, 2nd ed. (New York: Philosophical Library), Chapter 13 [van Wijngaarden’s transformations].[6]   
Numerical Recipes Software 2007, “Implementation of the Euler Transformation,” Numerical Recipes Webnote No.5,at http://www.nr.com/webnotes?5 [7]   
Jentschura, U.D., Mohr, P.J., Soff, G., and Weniger, E.J. 1999, “Convergence Acceleration via Combined Nonlinear-Condensation Transformations,” Computer Physics Communications, vol. 116, pp. 28–54.[8]   
Dahlquist, G., and Bjorck, A. 1974, Numerical Methods (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2003 (New York: Dover), Chapter 3.

# 5.4 Recurrence Relations and Clenshaw's Recurrence Formula

Many useful functions satisfy recurrence relations, e.g.,

$$
( n + 1 ) P _ { n + 1 } ( x ) = ( 2 n + 1 ) x P _ { n } ( x ) - n P _ { n - 1 } ( x )
$$

$$
J _ { n + 1 } ( x ) = { \frac { 2 n } { x } } J _ { n } ( x ) - J _ { n - 1 } ( x )
$$

$$
n E _ { n + 1 } ( x ) = e ^ { - x } - x E _ { n } ( x )
$$

$$
\begin{array} { r } { \mathrm { s s } n \theta = 2 \cos \theta \cos ( n - 1 ) \theta - \cos ( n - 2 ) \theta } \end{array}
$$

$$
\mathrm { i n } n \theta = 2 \cos \theta \sin ( n - 1 ) \theta - \sin ( n - 2 ) \theta
$$

where the first three functions are Legendre polynomials, Bessel functions of the first kind, and exponential integrals, respectively. (For notation see [1].) These relations are useful for extending computational methods from two successive values of $n$ to other values, either larger or smaller.

Equations (5.4.4) and (5.4.5) motivate us to say a few words about trigonometric functions. If your program’s running time is dominated by evaluating trigonometric functions, you are probably doing something wrong. Trig functions whose arguments form a linear sequence $\theta \ : = \ : \theta _ { 0 } \ : + \ : n \delta$ , $n = 0 , 1 , 2 , \ldots$ , are efficiently calculated by the recurrence

$$
\begin{array} { c } { \cos ( \theta + \delta ) = \cos \theta - [ \alpha \cos \theta + \beta \sin \theta ] } \\ { \sin ( \theta + \delta ) = \sin \theta - [ \alpha \sin \theta - \beta \cos \theta ] } \end{array}
$$

where $\alpha$ and $\beta$ are the precomputed coefficients

$$
\alpha \equiv 2 \sin ^ { 2 } \left( { \frac { \delta } { 2 } } \right) \qquad \beta \equiv \sin \delta
$$

The reason for doing things this way, rather than with the standard (and equivalent) identities for sums of angles, is that here $\alpha$ and $\beta$ do not lose significance if the incremental $\delta$ is small. Likewise, the adds in equation (5.4.6) should be done in the order indicated by the square brackets. We will use (5.4.6) repeatedly in Chapter 12, when we deal with Fourier transforms.

Another trick, occasionally useful, is to note that both $\sin \theta$ and cos $\theta$ can be calculated via a single call to tan:

$$
t \equiv \tan \left( { \frac { \theta } { 2 } } \right) \qquad \cos \theta = { \frac { 1 - t ^ { 2 } } { 1 + t ^ { 2 } } } \qquad \sin \theta = { \frac { 2 t } { 1 + t ^ { 2 } } }
$$

The cost of getting both sin and cos, if you need them, is thus the cost of tan plus 2 multiplies, 2 divides, and 2 adds. On machines with slow trig functions, this can be a savings. However, note that special treatment is required if $\theta  \pm \pi$ . And also note that many modern machines have very fast trig functions; so you should not assume that equation (5.4.8) is faster without testing.

# 5.4.1 Stability of Recurrences

You need to be aware that recurrence relations are not necessarily stable against roundoff error in the direction that you propose to go (either increasing $n$ or decreasing $n$ ). A three-term linear recurrence relation

$$
y _ { n + 1 } + a _ { n } y _ { n } + b _ { n } y _ { n - 1 } = 0 , \qquad n = 1 , 2 , \ldots
$$

has two linearly independent solutions, $f _ { n }$ and $g _ { n }$ , say. Only one of these corresponds to the sequence of functions $f _ { n }$ that you are trying to generate. The other one, $g _ { n }$ , may be exponentially growing in the direction that you want to go, or exponentially damped, or exponentially neutral (growing or dying as some power law, for example). If it is exponentially growing, then the recurrence relation is of little or no practical use in that direction. This is the case, e.g., for (5.4.2) in the direction of increasing $n$ , when $x \ < \ n$ . You cannot generate Bessel functions of high $n$ by forward recurrence on (5.4.2).

To state things a bit more formally, if

$$
f _ { n } / g _ { n } \to 0 \quad \mathrm { { ~ a s ~ } } \quad n \to \infty
$$

then $f _ { n }$ is called the minimal solution of the recurrence relation (5.4.9). Nonminimal solutions like $g _ { n }$ are called dominant solutions. The minimal solution is unique, if it exists, but dominant solutions are not — you can add an arbitrary multiple of $f _ { n }$ to a given $g _ { n }$ . You can evaluate any dominant solution by forward recurrence, but not the minimal solution. (Unfortunately it is sometimes the one you want.)

Abramowitz and Stegun (in their Introduction!) [1] give a list of recurrences that are stable in the increasing or decreasing direction. That list does not contain all possible formulas, of course. Given a recurrence relation for some function $f _ { n } ( x )$ , you can test it yourself with about five minutes of (human) labor: For a fixed $x$ in your range of interest, start the recurrence not with true values of $f _ { j } ( x )$ and $f _ { j + 1 } ( x )$ , but (first) with the values 1 and 0, respectively, and then (second) with 0 and 1, respectively. Generate 10 or 20 terms of the recursive sequences in the direction that you want to go (increasing or decreasing from $j$ ), for each of the two starting conditions. Look at the differences between the corresponding members of the two sequences. If the differences stay of order unity (absolute value less than 10, say), then the recurrence is stable. If they increase slowly, then the recurrence may be mildly unstable but quite tolerably so. If they increase catastrophically, then there is an exponentially growing solution of the recurrence. If you know that the function that you want actually corresponds to the growing solution, then you can keep the recurrence formula anyway (e.g., the case of the Bessel function $Y _ { n } ( x )$ for increasing $n$ ; see $\ S 6 . 5$ ). If you don’t know which solution your function corresponds to, you must at this point reject the recurrence formula. Notice that you can do this test before you go to the trouble of finding a numerical method for computing the two starting functions $f _ { j } ( x )$ and $f _ { j + 1 } ( x )$ : Stability is a property of the recurrence, not of the starting values.

An alternative heuristic procedure for testing stability is to replace the recurrence relation by a similar one that is linear with constant coefficients. For example, the relation (5.4.2) becomes

$$
y _ { n + 1 } - 2 \gamma y _ { n } + y _ { n - 1 } = 0
$$

where $\gamma \equiv n / x$ is treated as a constant. You solve such recurrence relations by trying solutions of the form $y _ { n } = a ^ { n }$ . Substituting into the above recurrence gives

$$
a ^ { 2 } - 2 \gamma a + 1 = 0 \qquad { \mathrm { o r } } \qquad a = \gamma \pm { \sqrt { \gamma ^ { 2 } - 1 } }
$$

The recurrence is stable if $| a | \le 1$ for all solutions $a$ . This holds (as you can verify) if $| \gamma | \leq 1$ or $n \leq x$ . The recurrence (5.4.2) thus cannot be used, starting with $J _ { 0 } ( x )$ and $J _ { 1 } ( x )$ , to compute $J _ { n } ( x )$ for large $n$ .

Possibly you would at this point like the security of some real theorems on this subject (although we ourselves always follow one of the heuristic procedures). Here are two theorems, due to Perron [2]:

Theorem $A$ . If in (5.4.9) $a _ { n } \sim a n ^ { \alpha }$ , $b _ { n } \sim b n ^ { \beta }$ as $n  \infty$ , and $\beta < 2 \alpha$ , then

$$
g _ { n + 1 } / g _ { n } \sim - a n ^ { \alpha } , \qquad f _ { n + 1 } / f _ { n } \sim - ( b / a ) n ^ { \beta - \alpha }
$$

and $f _ { n }$ is the minimal solution to (5.4.9).

Theorem $B$ . Under the same conditions as Theorem A, but with $\beta \ : = \ : 2 \alpha$ , consider the characteristic polynomial

$$
t ^ { 2 } + a t + b = 0
$$

If the roots $t _ { 1 }$ and $t _ { 2 }$ of (5.4.14) have distinct moduli, $\left| t _ { 1 } \right| > \left| t _ { 2 } \right|$ say, then

$$
g _ { n + 1 } / g _ { n } \sim t _ { 1 } n ^ { \alpha } , \qquad f _ { n + 1 } / f _ { n } \sim t _ { 2 } n ^ { \alpha }
$$

and $f _ { n }$ is again the minimal solution to (5.4.9). Cases other than those in these two theorems are inconclusive for the existence of minimal solutions. (For more on the stability of recurrences, see [3].)

How do you proceed if the solution that you desire is the minimal solution? The answer lies in that old aphorism, that every cloud has a silver lining: If a recurrence relation is catastrophically unstable in one direction, then that (undesired) solution will decrease very rapidly in the reverse direction. This means that you can start with any seed values for the consecutive $f _ { j }$ and $f _ { j + 1 }$ and (when you have gone enough steps in the stable direction) you will converge to the sequence of functions that you want, times an unknown normalization factor. If there is some other way to normalize the sequence (e.g., by a formula for the sum of the $f _ { n }$ ’s), then this can be a practical means of function evaluation. The method is called Miller’s algorithm. An example often given [1,4] uses equation (5.4.2) in just this way, along with the normalization formula

$$
1 = J _ { 0 } ( x ) + 2 J _ { 2 } ( x ) + 2 J _ { 4 } ( x ) + 2 J _ { 6 } ( x ) + \cdot \cdot \cdot
$$

Incidentally, there is an important relation between three-term recurrence relations and continued fractions. Rewrite the recurrence relation (5.4.9) as

$$
{ \frac { y _ { n } } { y _ { n - 1 } } } = - { \frac { b _ { n } } { a _ { n } + y _ { n + 1 } / y _ { n } } }
$$

Iterating this equation, starting with $n$ , gives

$$
{ \frac { y _ { n } } { y _ { n - 1 } } } = - { \frac { b _ { n } } { a _ { n } - } } { \frac { b _ { n + 1 } } { a _ { n + 1 } - } } \cdots
$$

Pincherle’s theorem [2] tells us that (5.4.18) converges if and only if (5.4.9) has a minimal solution $f _ { n }$ , in which case it converges to $f _ { n } / f _ { n - 1 }$ . This result, usually for the case $n = 1$ and combined with some way to determine $f _ { 0 }$ , underlies many of the practical methods for computing special functions that we give in the next chapter.

# 5.4.2 Clenshaw's Recurrence Formula

Clenshaw’s recurrence formula [5] is an elegant and efficient way to evaluate a sum of coefficients times functions that obey a recurrence formula, e.g.,

$$
f ( \theta ) = \sum _ { k = 0 } ^ { N } c _ { k } \cos k \theta \qquad { \mathrm { o r } } \qquad f ( x ) = \sum _ { k = 0 } ^ { N } c _ { k } P _ { k } ( x )
$$

Here is how it works: Suppose that the desired sum is

$$
f ( x ) = \sum _ { k = 0 } ^ { N } c _ { k } F _ { k } ( x )
$$

and that $F _ { k }$ obeys the recurrence relation

$$
F _ { n + 1 } ( x ) = \alpha ( n , x ) F _ { n } ( x ) + \beta ( n , x ) F _ { n - 1 } ( x )
$$

for some functions $\alpha ( n , x )$ and $\beta ( n , x )$ . Now define the quantities $y _ { k }$ . $( k = N , N -$ $1 , \ldots , 1 )$ by the recurrence

$$
\begin{array} { r l } { { y _ { N + 2 } } = y _ { N + 1 } = 0 } & { { } } \\ { { y _ { k } } = \alpha ( k , x ) y _ { k + 1 } + \beta ( k + 1 , x ) y _ { k + 2 } + c _ { k } } & { { } ( k = N , N - 1 , \ldots , 1 ) } \end{array}
$$

If you solve equation (5.4.21) for $c _ { k }$ on the left, and then write out explicitly the sum (5.4.19), it will look (in part) like this:

$$
\begin{array} { r l } { f ( x ) = \cdots } \\ { { } } & { { } + [ y _ { 8 } - \alpha ( 8 , x ) y _ { 9 } - \beta ( 9 , x ) y _ { 1 0 } ] F _ { 8 } ( x ) } \\ { { } } & { { } + [ y _ { 7 } - \alpha ( 7 , x ) y _ { 8 } - \beta ( 8 , x ) y _ { 9 } ] F _ { 7 } ( x ) } \\ { { } } & { { } + [ y _ { 6 } - \alpha ( 6 , x ) y _ { 7 } - \beta ( 7 , x ) y _ { 8 } ] F _ { 6 } ( x ) } \\ { { } } & { { } + [ y _ { 5 } - \alpha ( 5 , x ) y _ { 6 } - \beta ( 6 , x ) y _ { 7 } ] F _ { 5 } ( x ) } \\ { { } } & { { } + \cdots } \\ { { } } & { { } + [ y _ { 2 } - \alpha ( 2 , x ) y _ { 3 } - \beta ( 3 , x ) y _ { 4 } ] F _ { 2 } ( x ) } \\ { { } } & { { } + [ y _ { 1 } - \alpha ( 1 , x ) y _ { 2 } - \beta ( 2 , x ) y _ { 3 } ] F _ { 1 } ( x ) } \\ { { } } & { { } + [ c _ { 0 } + \beta ( 1 , x ) y _ { 2 } - \beta ( 1 , x ) y _ { 2 } ] F _ { 0 } ( x ) } \end{array}
$$

Notice that we have added and subtracted $\beta ( 1 , x ) y _ { 2 }$ in the last line. If you examine the terms containing a factor of $y _ { 8 }$ in (5.4.22), you will find that they sum to zero as a consequence of the recurrence relation (5.4.20); similarly for all the other $y _ { k }$ ’s down through $y _ { 2 }$ . The only surviving terms in (5.4.22) are

$$
f ( x ) = \beta ( 1 , x ) F _ { 0 } ( x ) y _ { 2 } + F _ { 1 } ( x ) y _ { 1 } + F _ { 0 } ( x ) c _ { 0 }
$$

Equations (5.4.21) and (5.4.23) are Clenshaw’s recurrence formula for doing the sum (5.4.19): You make one pass down through the $y _ { k }$ ’s using (5.4.21); when you have reached $y _ { 2 }$ and $y _ { 1 }$ , you apply (5.4.23) to get the desired answer.

Clenshaw’s recurrence as written above incorporates the coefficients $c _ { k }$ in a downward order, with $k$ decreasing. At each stage, the effect of all previous $c _ { k }$ ’s is “remembered” as two coefficients that multiply the functions $F _ { k + 1 }$ and $F _ { k }$ (ultimately $F _ { 0 }$ and $F _ { 1 }$ ). If the functions $F _ { k }$ are small when $k$ is large, and if the coefficients $c _ { k }$ are small when $k$ is small, then the sum can be dominated by small $F _ { k }$ ’s. In this case, the remembered coefficients will involve a delicate cancellation and there can be a catastrophic loss of significance. An example would be to sum the trivial series

$$
J _ { 1 5 } ( 1 ) = 0 \times J _ { 0 } ( 1 ) + 0 \times J _ { 1 } ( 1 ) + \ldots + 0 \times J _ { 1 4 } ( 1 ) + 1 \times J _ { 1 5 } ( 1 )
$$

Here $J _ { 1 5 }$ , which is tiny, ends up represented as a canceling linear combination of $J _ { 0 }$ and $J _ { 1 }$ , which are of order unity.

The solution in such cases is to use an alternative Clenshaw recurrence that incorporates the $c _ { k }$ ’s in an upward direction. The relevant equations are

$$
\begin{array} { l } { { y _ { - 2 } = y _ { - 1 } = 0 } } \\ { { \mathrm { ~ } y _ { k } = \displaystyle \frac { 1 } { \beta ( k + 1 , x ) } [ y _ { k - 2 } - \alpha ( k , x ) y _ { k - 1 } - c _ { k } ] , \quad k = 0 , 1 , . . . , N - 1 } } \\ { { \mathrm { ~ } f ( x ) = c _ { N } F _ { N } ( x ) - \beta ( N , x ) F _ { N - 1 } ( x ) y _ { N - 1 } - F _ { N } ( x ) y _ { N - 2 } } } \end{array}
$$

The rare case where equations $( 5 . 4 . 2 5 ) - ( 5 . 4 . 2 7 )$ should be used instead of equations (5.4.21) and (5.4.23) can be detected automatically by testing whether the operands in the first sum in (5.4.23) are opposite in sign and nearly equal in magnitude. Other than in this special case, Clenshaw’s recurrence is always stable, independent of whether the recurrence for the functions $F _ { k }$ is stable in the upward or downward direction.

# 5.4.3 Parallel Evaluation of Linear Recurrence Relations

When desirable, linear recurrence relations can be evaluated with a lot of parallelism. Consider the general first-order linear recurrence relation

$$
u _ { j } = a _ { j } + b _ { j - 1 } u _ { j - 1 } , \qquad j = 2 , 3 , \ldots , n
$$

with initial value $u _ { 1 } = a _ { 1 }$ . To parallelize the recurrence, we can employ the powerful general strategy of recursive doubling. Write down equation (5.4.28) for $2 j$ and for $2 j - 1$ :

$$
\begin{array} { c } { { u _ { 2 j } = a _ { 2 j } + b _ { 2 j - 1 } u _ { 2 j - 1 } } } \\ { { u _ { 2 j - 1 } = a _ { 2 j - 1 } + b _ { 2 j - 2 } u _ { 2 j - 2 } } } \end{array}
$$

Substitute the second of these equations into the first to eliminate $u _ { 2 j - 1 }$ and get

$$
u _ { 2 j } = ( a _ { 2 j } + a _ { 2 j - 1 } b _ { 2 j - 1 } ) + ( b _ { 2 j - 2 } b _ { 2 j - 1 } ) u _ { 2 j - 2 }
$$

This is a new recurrence of the same form as (5.4.28) but over only the even $u _ { j }$ , and hence involving only $n / 2$ terms. Clearly we can continue this process recursively, halving the number of terms in the recurrence at each stage, until we are left with a recurrence of length 1 or 2 that we can do explicitly. Each time we finish a subpart of the recursion, we fill in the odd terms in the recurrence, using the second equation in (5.4.29). In practice, it’s even easier than it sounds. The total number of operations is the same as for serial evaluation, but they are done in about $\log _ { 2 } n$ parallel steps.

There is a variant of recursive doubling, called cyclic reduction, that can be implemented with a straightforward iteration loop instead of a recursive procedure [6]. Here we start by writing down the recurrence (5.4.28) for all adjacent terms $u _ { j }$ and $u _ { j - 1 }$ (not just the even ones, as before). Eliminating $u _ { j - 1 }$ , just as in equation (5.4.30), gives

$$
u _ { j } = ( a _ { j } + a _ { j - 1 } b _ { j - 1 } ) + ( b _ { j - 2 } b _ { j - 1 } ) u _ { j - 2 }
$$

which is a first-order recurrence with new coefficients $a _ { j } ^ { \prime }$ and $b _ { j } ^ { \prime }$ . Repeating this process gives successive formulas for $u _ { j }$ in terms of $u _ { j - 2 } , u _ { j - 4 } , u _ { j - 8 } , . . . .$ The procedure terminates when we reach $u _ { j - n }$ (for $n$ a power of 2), which is zero for all $j$ . Thus the last step gives $u _ { j }$ equal to the last set of $a _ { j } ^ { \prime }$ ’s.

In cyclic reduction, the length of the vector $u _ { j }$ that is updated at each stage does not decrease by a factor of 2 at each stage, but rather only decreases from $\sim n$ to $\sim n / 2$ during all $\log _ { 2 } n$ stages. Thus the total number of operations carried out is $O ( n \log n )$ , as opposed to $O ( n )$ for recursive doubling. Whether this is important depends on the details of the computer’s architecture.

Second-order recurrence relations can also be parallelized. Consider the second-order recurrence relation

$$
y _ { j } = a _ { j } + b _ { j - 2 } y _ { j - 1 } + c _ { j - 2 } y _ { j - 2 } , \qquad j = 3 , 4 , \ldots , n
$$

with initial values

$$
y _ { 1 } = a _ { 1 } , \qquad y _ { 2 } = a _ { 2 }
$$

With this numbering scheme, you supply coefficients $a _ { 1 } , \dots , a _ { n } , b _ { 1 } , \dots , b _ { n - 2 }$ , and $c _ { 1 } , . . .$ ; $c _ { n - 2 }$ . Rewrite the recurrence relation in the form [6]

$$
\left( { \begin{array} { c } { y _ { j } } \\ { y _ { j + 1 } } \end{array} } \right) = \left( { \begin{array} { c } { 0 } \\ { a _ { j + 1 } } \end{array} } \right) + \left( { \begin{array} { c c } { 0 } & { 1 } \\ { c _ { j - 1 } } & { b _ { j - 1 } } \end{array} } \right) \left( { \begin{array} { c } { y _ { j - 1 } } \\ { y _ { j } } \end{array} } \right) , \qquad j = 2 , \ldots , n - 1
$$

that is,

$$
\mathbf { u } _ { j } = \mathbf { a } _ { j } + \mathbf { b } _ { j - 1 } \cdot \mathbf { u } _ { j - 1 } , \qquad j = 2 , \ldots , n - 1
$$

where

$$
{ \mathbf { u } } _ { j } = ( { y } _ { j } ) , \qquad { \mathbf { a } } _ { j } = ( { 0 \atop a _ { j + 1 } } ) , \qquad { \mathbf { b } } _ { j - 1 } = ( { 0 \atop c _ { j - 1 } }  \ { 1 \atop b _ { j - 1 } } )
$$

and

$$
\mathbf { u } _ { 1 } = \mathbf { a } _ { 1 } = { \binom { y _ { 1 } } { y _ { 2 } } } = { \binom { a _ { 1 } } { a _ { 2 } } }
$$

This is a first-order recurrence relation for the vectors $\mathbf { u } _ { j }$ and can be solved by either of the algorithms described above. The only difference is that the multiplications are matrix multiplications with the $2 \times 2$ matrices ${ \mathbf { b } } _ { j }$ . After the first recursive call, the zeros in a and $\mathbf { b }$ are lost, so we have to write the routine for general two-dimensional vectors and matrices. Note that this algorithm does not avoid the potential instability problems associated with secondorder recurrences that were discussed in $\ S 5 . 4 . 1$ . Also note that the algorithm generalizes in the obvious way to higher-order recurrences: An nth-order recurrence can be written as a first-order recurrence involving vectors and matrices of dimension $n$ .

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, pp. xiii, 697.[1]   
Gautschi, W. 1967, “Computational Aspects of Three-Term Recurrence Relations,” SIAM Review, vol. 9, pp.24-82.[2]   
Lakshmikantham, V., and Trigiante, D. 1988, Theory of Difference Equations: Numerical Methods and Applications (San Diego: Academic Press).[3]   
Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), pp. 20ff.[4]   
Clenshaw, C.W. 1962, Mathematical Tables, vol. 5, National Physical Laboratory (London: H.M. Stationery Office).[5]   
Dahlquist, G., and Bjorck, A. 1974, Numerical Methods (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2003 (New York: Dover), $\ S 4 . 4 . 3$ , p. 111.   
Goodwin, E.T. (ed.) 1961, Modern Computing Methods, 2nd ed. (New York: Philosophical Library), p. 76.   
Hockney, R.W., and Jesshope, C.R. 1988, Parallel Computers 2: Architecture, Programming, and Algorithms (Bristol and Philadelphia: Adam Hilger), $\ S 5 . 2 . 4$ and $\ S 5 . 4 . 2 .$ [6]

# 5.5 Complex Arithmetic

Since $\mathrm { C } { + + }$ has a built-in class complex, you can generally let the compiler and the class library take care of complex arithmetic for you. Generally, but not always. For a program with only a small number of complex operations, you may want to code these yourself, in-line. Or, you may find that your compiler is not up to snuff: It is disconcertingly common to encounter complex operations that produce overflows or underflows when both the complex operands and the complex result are perfectly representable. This occurs, we think, because software companies mistake the implementation of complex arithmetic for a completely trivial task, not requiring any particular finesse.

Actually, complex arithmetic is not quite trivial. Addition and subtraction are done in the obvious way, performing the operation separately on the real and imaginary parts of the operands. Multiplication can also be done in the obvious way, with four multiplications, one addition, and one subtraction:

$$
( a + i b ) ( c + i d ) = ( a c - b d ) + i ( b c + a d )
$$

(the addition sign before the $i$ doesn’t count; it just separates the real and imaginary parts notationally). But it is sometimes faster to multiply via

$$
( a + i b ) ( c + i d ) = ( a c - b d ) + i [ ( a + b ) ( c + d ) - a c - b d ]
$$

which has only three multiplications $( a c , b d , ( a + b ) ( c + d ) )$ , plus two additions and three subtractions. The total operations count is higher by two, but multiplication is a slow operation on some machines.

While it is true that intermediate results in equations (5.5.1) and (5.5.2) can overflow even when the final result is representable, this happens only when the final

answer is on the edge of representability. Not so for the complex modulus, if you or your compiler is misguided enough to compute it as

$$
| a + i b | = { \sqrt { a ^ { 2 } + b ^ { 2 } } }
$$

whose intermediate result will overflow if either $a$ or $b$ is as large as the square root of the largest representable number (e.g., $1 0 ^ { 1 9 }$ as compared to $1 0 ^ { 3 8 }$ ). The right way to do the calculation is

$$
| a + i b | = \{ | a | \sqrt { 1 + ( b / a ) ^ { 2 } } \quad | a | \geq | b |
$$

Complex division should use a similar trick to prevent avoidable overflow, underflow, or loss of precision:

$$
\frac { a + i b } { c + i d } = \left\{ \begin{array} { l l } { \frac { [ a + b ( d / c ) ] + i [ b - a ( d / c ) ] } { c + d ( d / c ) } } & { | c | \geq | d | } \\ { \frac { [ a ( c / d ) + b ] + i [ b ( c / d ) - a ] } { c ( c / d ) + d } } & { | c | < | d | } \end{array} \right.
$$

Of course you should calculate repeated subexpressions, like $c / d$ or $d / c$ , only once.

Complex square root is even more complicated, since we must both guard intermediate results and also enforce a chosen branch cut (here taken to be the negative real axis). To take the square root of $c + i d$ , first compute

$$
w \equiv \left\{ \begin{array} { l l } { 0 } & { c = d = 0 } \\ { \sqrt { | c | } \sqrt { \displaystyle \frac { 1 + \sqrt { 1 + ( d / c ) ^ { 2 } } } { 2 } } } & { | c | \geq | d | } \\ { \sqrt { | d | } \sqrt { \displaystyle \frac { | c / d | + \sqrt { 1 + ( c / d ) ^ { 2 } } } { 2 } } } & { | c | < | d | } \end{array} \right.
$$

Then the answer is

$$
{ \sqrt { c + i d } } = { \{ \begin{array} { l l } { 0 } & { w = 0 } \\ { w + i ( { \frac { d } { 2 w } } ) } & { w \neq 0 , c \geq 0 } \\ { | { \frac { d } { 2 w } } + i w } & { w \neq 0 , c < 0 , d \geq 0 } \\ { | { \frac { d } { 2 w } } - i w  } & { w \neq 0 , c < 0 , d < 0 } \end{array}  }
$$

# CITED REFERENCES AND FURTHER READING:

Midy, P., and Yakovlev, Y. 1991, “ Computing Some Elementary Functions of a Complex Variable,” Mathematics and Computers in Simulation, vol. 33, pp.33-49.

Knuth, D.E. 1997, Seminumerical Algorithms, 3rd ed., vol. 2 of The Art of Computer Programming (Reading, MA: Addison-Wesley) [see solutions to exercises 4.2.1.16 and 4.6.4.41].

# 5.6 Quadratic and Cubic Equations

The roots of simple algebraic equations can be viewed as being functions of the equations’ coefficients. We are taught these functions in elementary algebra. Yet, surprisingly many people don’t know the right way to solve a quadratic equation with two real roots, or to obtain the roots of a cubic equation.

There are two ways to write the solution of the quadratic equation

$$
a x ^ { 2 } + b x + c = 0
$$

with real coefficients $a , b , c$ , namely

$$
x = { \frac { - b \pm { \sqrt { b ^ { 2 } - 4 a c } } } { 2 a } }
$$

and

$$
x = { \frac { 2 c } { - b \pm { \sqrt { b ^ { 2 } - 4 a c } } } }
$$

If you use either (5.6.2) or (5.6.3) to get the two roots, you are asking for trouble: If either $a$ or $c$ (or both) is small, then one of the roots will involve the subtraction of $b$ from a very nearly equal quantity (the discriminant); you will get that root very inaccurately. The correct way to compute the roots is

$$
q \equiv - \frac { 1 } { 2 } \left[ b + \mathrm { s g n } ( b ) \sqrt { b ^ { 2 } - 4 a c } \right]
$$

Then the two roots are

$$
x _ { 1 } = { \frac { q } { a } } \qquad \mathrm { a n d } \qquad x _ { 2 } = { \frac { c } { q } }
$$

If the coefficients $a , b , c$ , are complex rather than real, then the above formulas still hold, except that in equation (5.6.4) the sign of the square root should be chosen so as to make

$$
\mathrm { R e } ( b ^ { * } { \sqrt { b ^ { 2 } - 4 a c } } ) \geq 0
$$

where Re denotes the real part and asterisk denotes complex conjugation.

Apropos of quadratic equations, this seems a convenient place to recall that the inverse hyperbolic functions $\mathrm { s i n h } ^ { - 1 }$ and $\mathrm { c o s h } ^ { - 1 }$ are in fact just logarithms of solutions to such equations

$$
\begin{array} { r } { \sinh ^ { - 1 } ( x ) = \quad \ln \bigl ( x + \sqrt { x ^ { 2 } + 1 } \bigr ) } \\ { \cosh ^ { - 1 } ( x ) = \pm \ln \bigl ( x + \sqrt { x ^ { 2 } - 1 } \bigr ) } \end{array}
$$

Equation (5.6.7) is numerically robust for $x \ge 0$ . For negative $x$ , use the symmetry $\sinh ^ { - 1 } ( - x ) = - \sinh ^ { - 1 } ( x )$ . Equation (5.6.8) is of course valid only for $x \ge 1$ .

For the cubic equation

$$
x ^ { 3 } + a x ^ { 2 } + b x + c = 0
$$

with real or complex coefficients $a , b , c$ , first compute

$$
Q \equiv { \frac { a ^ { 2 } - 3 b } { 9 } } { \mathrm { a n d } } R \equiv { \frac { 2 a ^ { 3 } - 9 a b + 2 7 c } { 5 4 } }
$$

If $Q$ and $R$ are real (always true when $a , b , c$ are real) and $R ^ { 2 } < Q ^ { 3 }$ , then the cubic equation has three real roots. Find them by computing

$$
\theta = \operatorname { a r c c o s } ( R / \sqrt { Q ^ { 3 } } )
$$

in terms of which the three roots are

$$
\begin{array} { l } { { x _ { 1 } = - 2 \sqrt Q \cos \left( \displaystyle { \frac { \theta } { 3 } } \right) - \displaystyle { \frac { a } { 3 } } } } \\ { { x _ { 2 } = - 2 \sqrt Q \cos \left( \displaystyle { \frac { \theta + 2 \pi } { 3 } } \right) - \displaystyle { \frac { a } { 3 } } } } \\ { { x _ { 3 } = - 2 \sqrt Q \cos \left( \displaystyle { \frac { \theta - 2 \pi } { 3 } } \right) - \displaystyle { \frac { a } { 3 } } } } \end{array}
$$

(This equation first appears in Chapter VI of Franc¸ois Viete’s treatise “De emenda- \` tione,” published in 1615!)

Otherwise, compute

$$
A = - \left[ R + \sqrt { R ^ { 2 } - Q ^ { 3 } } \right] ^ { 1 / 3 }
$$

where the sign of the square root is chosen to make

$$
\mathrm { R e } ( R ^ { * } \sqrt { R ^ { 2 } - Q ^ { 3 } } ) \geq 0
$$

(asterisk again denoting complex conjugation). If $Q$ and $R$ are both real, equations $( 5 . 6 . 1 3 ) - ( 5 . 6 . 1 4 )$ are equivalent to

$$
A = - \mathrm { s g n } ( R ) \left[ | R | + \sqrt { R ^ { 2 } - Q ^ { 3 } } \right] ^ { 1 / 3 }
$$

where the positive square root is assumed. Next compute

$$
B = \left\{ \begin{array} { l l } { Q / A } & { \quad ( A \neq 0 ) } \\ { 0 } & { \quad ( A = 0 ) } \end{array} \right.
$$

in terms of which the three roots are

$$
x _ { 1 } = ( A + B ) - { \frac { a } { 3 } }
$$

(the single real root when $a , b , c$ are real) and

$$
\begin{array} { l } { { \displaystyle x _ { 2 } = - \frac { 1 } { 2 } ( A + B ) - \frac { a } { 3 } + i \frac { \sqrt { 3 } } { 2 } ( A - B ) } } \\ { { \displaystyle x _ { 3 } = - \frac { 1 } { 2 } ( A + B ) - \frac { a } { 3 } - i \frac { \sqrt { 3 } } { 2 } ( A - B ) } } \end{array}
$$

(in that same case, a complex-conjugate pair). Equations (5.6.13) – (5.6.16) are arranged both to minimize roundoff error and also (as pointed out by A.J. Glassman) to ensure that no choice of branch for the complex cube root can result in the spurious loss of a distinct root.

If you need to solve many cubic equations with only slightly different coefficients, it is more efficient to use Newton’s method (-9.4).

# CITED REFERENCES AND FURTHER READING:

Weast, R.C. (ed.) 1967, Handbook of Tables for Mathematics, 3rd ed. (Cleveland: The Chemical Rubber Co.), pp. 130–133.

Pachner, J. 1983, Handbook of Numerical Analysis Applications (New York: McGraw-Hill), $\ S 6 . 1$ .

McKelvey, J.P. 1984, “Simple Transcendental Expressions for the Roots of Cubic Equations,” American Journal of Physics,vol.52,pp.269-270; see also vol.53,p.775,and vol. 55, pp. 374–375.

# 5.7 Numerical Derivatives

Imagine that you have a procedure that computes a function $f ( x )$ , and now you want to compute its derivative $f ^ { \prime } ( x )$ . Easy, right? The definition of the derivative, the limit as $h  0$ of

$$
f ^ { \prime } ( x ) \approx { \frac { f ( x + h ) - f ( x ) } { h } }
$$

practically suggests the program: Pick a small value $h$ ; evaluate $f ( x + h )$ ; you probably have $f ( x )$ already evaluated, but if not, do it too; finally, apply equation (5.7.1). What more needs to be said?

Quite a lot, actually. Applied uncritically, the above procedure is almost guaranteed to produce inaccurate results. Applied properly, it can be the right way to compute a derivative only when the function $f$ is fiercely expensive to compute; when you already have invested in computing $f ( x )$ ; and when, therefore, you want to get the derivative in no more than a single additional function evaluation. In such a situation, the remaining issue is to choose $h$ properly, an issue we now discuss.

There are two sources of error in equation (5.7.1), truncation error and roundoff error. The truncation error comes from higher terms in the Taylor series expansion,

$$
\begin{array} { r } { f ( x + h ) = f ( x ) + h f ^ { \prime } ( x ) + \frac { 1 } { 2 } h ^ { 2 } f ^ { \prime \prime } ( x ) + \frac { 1 } { 6 } h ^ { 3 } f ^ { \prime \prime \prime } ( x ) + \cdot \cdot \cdot } \end{array}
$$

whence

$$
{ \frac { f ( x + h ) - f ( x ) } { h } } = f ^ { \prime } + { \frac { 1 } { 2 } } h f ^ { \prime \prime } + \cdot \cdot \cdot
$$

The roundoff error has various contributions. First there is roundoff error in $h$ : Suppose, by way of an example, that you are at a point $x = 1 0 . 3$ and you blindly choose $h \ : = \ : 0 . 0 0 0 1$ . Neither $x = 1 0 . 3$ nor $x + h \ : = \ : 1 0 . 3 0 0 0 1$ is a number with an exact representation in binary; each is therefore represented with some fractional error characteristic of the machine’s floating-point format, $\epsilon _ { m }$ , whose value in single precision may be $\sim 1 0 ^ { - 7 }$ . The error in the effective value of $h$ , namely the difference between $x + h$ and $x$ as represented in the machine, is therefore on the order of $\epsilon _ { m } x$ , which implies a fractional error in $h$ of order $\sim \epsilon _ { m } x / h \sim 1 0 ^ { - 2 } !$ By equation (5.7.1), this immediately implies at least the same large fractional error in the derivative.

We arrive at Lesson 1: Always choose $h$ so that $x + h$ and $x$ differ by an exactly representable number. This can usually be accomplished by the program steps

$$
\begin{array} { c } { \mathsf { t e m p } = x + h } \\ { h = \mathsf { t e m p } - x } \end{array}
$$

Some optimizing compilers, and some computers whose floating-point chips have higher internal accuracy than is stored externally, can foil this trick; if so, it is usually enough to declare temp as volatile, or else to call a dummy function donothing(temp) between the two equations (5.7.4). This forces temp into and out of addressable memory.

With $h$ an “exact” number, the roundoff error in equation (5.7.1) is approximately $e _ { r } \sim \epsilon _ { f } | f ( x ) / h |$ . Here $\epsilon _ { f }$ is the fractional accuracy with which $f$ is computed; for a simple function this may be comparable to the machine accuracy, $\epsilon _ { f } \approx$ $\epsilon _ { m }$ , but for a complicated calculation with additional sources of inaccuracy it may be larger. The truncation error in equation (5.7.3) is on the order of $e _ { t } \sim | h f ^ { \prime \prime } ( x ) |$ . Varying $h$ to minimize the sum $e _ { r } + e _ { t }$ gives the optimal choice of $h$ ,

$$
h \sim \sqrt { \frac { \epsilon _ { f } f } { f ^ { \prime \prime } } } \approx \sqrt { \epsilon _ { f } } x _ { c }
$$

where $x _ { c } \equiv ( f / f ^ { \prime \prime } ) ^ { 1 / 2 }$ is the “curvature scale” of the function $f$ or the “characteristic scale” over which it changes. In the absence of any other information, one often assumes $x _ { c } ~ = ~ x$ (except near $x = 0$ , where some other estimate of the typical $x$ scale should be used).

With the choice of equation (5.7.5), the fractional accuracy of the computed derivative is

$$
( e _ { r } + e _ { t } ) / | f ^ { \prime } | \sim \sqrt { \epsilon _ { f } } ( f f ^ { \prime \prime } / f ^ { \prime 2 } ) ^ { 1 / 2 } \sim \sqrt { \epsilon _ { f } }
$$

Here the last order-of-magnitude equality assumes that $f , f ^ { \prime }$ , and $f ^ { \prime \prime }$ all share the same characteristic length scale, which is usually the case. One sees that the simple finite difference equation (5.7.1) gives at best only the square root of the machine accuracy $\epsilon _ { m }$ .

If you can afford two function evaluations for each derivative calculation, then it is significantly better to use the symmetrized form

$$
f ^ { \prime } ( x ) \approx { \frac { f ( x + h ) - f ( x - h ) } { 2 h } }
$$

In this case, by equation (5.7.2), the truncation error is $e _ { t } \sim h ^ { 2 } f ^ { \prime \prime \prime }$ . The roundoff error $e _ { r }$ is about the same as before. The optimal choice of $h$ , by a short calculation analogous to the one above, is now

$$
h \sim \left( \frac { \epsilon _ { f } f } { f ^ { \prime \prime \prime } } \right) ^ { 1 / 3 } \sim ( \epsilon _ { f } ) ^ { 1 / 3 } x _ { c }
$$

and the fractional error is

$$
( e _ { r } + e _ { t } ) / | f ^ { \prime } | \sim ( \epsilon _ { f } ) ^ { 2 / 3 } f ^ { 2 / 3 } ( f ^ { \prime \prime \prime } ) ^ { 1 / 3 } / f ^ { \prime } \sim ( \epsilon _ { f } ) ^ { 2 / 3 }
$$

which will typically be an order of magnitude (single precision) or two orders of magnitude (double precision) better than equation (5.7.6). We have arrived at Lesson 2: Choose $h$ to be the correct power of $\epsilon _ { f }$ or $\epsilon _ { m }$ times a characteristic scale $x _ { c }$ .

You can easily derive the correct powers for other cases [1]. For a function of two dimensions, for example, and the mixed derivative formula

$$
{ \frac { \partial ^ { 2 } f } { \partial x \partial y } } = { \frac { [ f ( x + h , y + h ) - f ( x + h , y - h ) ] - [ f ( x - h , y + h ) - f ( x - h , y - h ) ] } { 4 h ^ { 2 } } }
$$

the correct scaling is $h \sim \epsilon _ { f \_ } ^ { 1 / 4 } x _ { c }$

It is disappointing, certainly, that no simple finite difference formula like equation (5.7.1) or (5.7.7) gives an accuracy comparable to the machine accuracy $\epsilon _ { m }$ , or even the lower accuracy to which $f$ is evaluated, $\epsilon _ { f }$ . Are there no better methods?

Yes, there are. All, however, involve exploration of the function’s behavior over scales comparable to $x _ { c }$ , plus some assumption of smoothness, or analyticity, so that the high-order terms in a Taylor expansion like equation (5.7.2) have some meaning. Such methods also involve multiple evaluations of the function $f$ , so their increased accuracy must be weighed against increased cost.

The general idea of “Richardson’s deferred approach to the limit” is particularly attractive. For numerical integrals, that idea leads to so-called Romberg integration (for review, see $\ S 4 . 3 )$ . For derivatives, one seeks to extrapolate, to $h  0$ , the result of finite difference calculations with smaller and smaller finite values of $h$ . By the use of Neville’s algorithm (-3.2), one uses each new finite difference calculation to produce both an extrapolation of higher order and also extrapolations of previous, lower, orders but with smaller scales $h$ . Ridders [2] has given a nice implementation of this idea; the following program, dfridr, is based on his algorithm, modified by an improved termination criterion. Input to the routine is a function $f$ (called func), a position $x$ , and a largest stepsize h (more analogous to what we have called $x _ { c }$ above than to what we have called $h$ ). Output is the returned value of the derivative and an estimate of its error, err.

# template<class T>

Doub dfridr(T &func, const Doub x, const Doub h, Doub &err)

Returns the derivative of a function func at a point x by Ridders’ method of polynomial extrapolation. The value h is input as an estimated initial stepsize; it need not be small, but rather should be an increment in x over which func changes substantially. An estimate of the error in the derivative is returned as err.

const Int ntab $\scriptstyle 1 = 1 0$ ; Sets maximum size of tableau.   
const Doub con $= 1$ .4, con2 $=$ (con\*con); Stepsize decreased by CON at each iteration. const Doub big=numeric_limits<Doub>::max();   
const Doub safe $= 2 , 0$ ; Return when error is SAFE worse than the Int i,j; best so far.   
Doub errt,fac,hh,ans;   
MatDoub a(ntab,ntab);   
if $\mathrm { ~  ~ \lambda ~ } ^ { \prime } { \mathrm {  ~ h ~ } } = = \mathrm {  ~ 0 ~ } . 0 $ ) throw("h must be nonzero in dfridr.");   
hh=h;   
a[0][0] $=$ (func(x+hh)-func(x-hh))/(2.0\*hh);   
err=big;   
for ( $\dot { 1 } = 1$ ;i<ntab;i++) {   
Successive columns in the Neville tableau will go to smaller stepsizes and higher orders of extrapolation. hh $/ { = }$ con;   
a[0][i] $=$ (func(x+hh)-func(x-hh))/(2.0\*hh); Try new, smaller stepsize.   
fac=con2;

for (j ${ = } 1$ ;j ${ \tt { \tt { \tt { \tt { \Lambda } } } } } = \dot { \tt { \tt { \tt { 1 } } } }$ ;j++) { Compute extrapolations of various orders, requiring a[j][i] $=$ (a[j-1][i]\*fac-a[j-1][i-1])/(fac-1.0); no new function evalfac=con2\*fac; uations. errt=MAX(abs(a[j][i]-a[j-1][i]),abs(a[j][i]-a[j-1][i-1])); The error strategy is to compare each new extrapolation to one order lower, both at the present stepsize and the previous one. if (errt $< =$ err) { If error is decreased, save the improved answer. err $^ { * } =$ errt; ans $= a$ [j][i]; } if (abs(a[i][i]-a[i-1][i-1]) $> =$ safe\*err) break; If higher order is worse by a significant factor SAFE, then quit early. } return ans;

In dfridr, the number of evaluations of func is typically 6 to 12, but is allowed to be as great as $2 \times \tt N T A B$ . As a function of input h, it is typical for the accuracy to get better as h is made larger, until a sudden point is reached where nonsensical extrapolation produces an early return with a large error. You should therefore choose a fairly large value for h but monitor the returned value err, decreasing h if it is not small. For functions whose characteristic $x$ scale is of order unity, we typically take h to be a few tenths.

Besides Ridders’ method, there are other possible techniques. If your function is fairly smooth, and you know that you will want to evaluate its derivative many times at arbitrary points in some interval, then it makes sense to construct a Chebyshev polynomial approximation to the function in that interval, and to evaluate the derivative directly from the resulting Chebyshev coefficients. This method is described in $\ S 5 . 8 - \ S 5 . 9$ , following.

Another technique applies when the function consists of data that is tabulated at equally spaced intervals, and perhaps also noisy. One might then want, at each point, to least-squares fit a polynomial of some degree $M$ , using an additional number $n _ { L }$ of points to the left and some number $n _ { R }$ of points to the right of each desired $x$ value. The estimated derivative is then the derivative of the resulting fitted polynomial. A very efficient way to do this construction is via Savitzky-Golay smoothing filters, which will be discussed later, in $\ S 1 4 . 9$ . There we will give a routine for getting filter coefficients that not only construct the fitting polynomial but, in the accumulation of a single sum of data points times filter coefficients, evaluate it as well. In fact, the routine given, savgol, has an argument ld that determines which derivative of the fitted polynomial is evaluated. For the first derivative, the appropriate setting is $1 { \dot { \mathsf { d } } } { = } 1$ , and the value of the derivative is the accumulated sum divided by the sampling interval $h$ .

# CITED REFERENCES AND FURTHER READING:

Dennis, J.E., and Schnabel, R.B. 1983, Numerical Methods for Unconstrained Optimization and Nonlinear Equations; reprinted 1996 (Philadelphia: S.l.A.M.), $\ S 5 . 4 - \ S 5 . 6 . [$ [1]   
Ridders, C.J.F. 1982, “Accurate computation of $F ^ { \prime } ( x )$ and $F ^ { \prime } ( x ) F ^ { \prime \prime } ( x )$ ,” Advances in Engineering Software,vol.4,no.2,pp.75-76.[2]

# 5.8 Chebyshev Approximation

The Chebyshev polynomial of degree $n$ is denoted $T _ { n } ( x )$ and is given by the explicit formula

$$
T _ { n } ( x ) = \cos ( n \operatorname { a r c c o s } x )
$$

This may look trigonometric at first glance (and there is in fact a close relation between the Chebyshev polynomials and the discrete Fourier transform); however, (5.8.1) can be combined with trigonometric identities to yield explicit expressions for $T _ { n } ( x )$ (see Figure 5.8.1):

$$
\begin{array} { r l } & { T _ { 0 } ( x ) = 1 } \\ & { T _ { 1 } ( x ) = x } \\ & { T _ { 2 } ( x ) = 2 x ^ { 2 } - 1 } \\ & { T _ { 3 } ( x ) = 4 x ^ { 3 } - 3 x } \\ & { T _ { 4 } ( x ) = 8 x ^ { 4 } - 8 x ^ { 2 } + 1 } \\ & { \qquad \cdots } \\ & { r _ { n + 1 } ( x ) = 2 x T _ { n } ( x ) - T _ { n - 1 } ( x ) \quad n \geq 1 . } \end{array}
$$

(There also exist inverse formulas for the powers of $x$ in terms of the $T _ { n }$ ’s — see, e.g., [1].)

The Chebyshev polynomials are orthogonal in the interval $[ - 1 , 1 ]$ over a weight $( 1 - x ^ { 2 } ) ^ { - 1 / 2 }$ . In particular,

$$
\int _ { - 1 } ^ { 1 } { \frac { T _ { i } ( x ) T _ { j } ( x ) } { { \sqrt { 1 - x ^ { 2 } } } } } d x = { \left\{ \begin{array} { l l } { 0 } & { i \neq j } \\ { \pi / 2 } & { i = j \neq 0 } \\ { \pi } & { i = j = 0 } \end{array} \right. }
$$

The polynomial $T _ { n } ( x )$ has $n$ zeros in the interval $[ - 1 , 1 ]$ , and they are located at the points

$$
x = \cos \left( { \frac { \pi ( k + { \frac { 1 } { 2 } } ) } { n } } \right) \qquad k = 0 , 1 , \ldots , n - 1
$$

In this same interval there are $n + 1$ extrema (maxima and minima), located at

$$
x = \cos \left( { \frac { \pi k } { n } } \right) \qquad k = 0 , 1 , \ldots , n
$$

At all of the maxima $T _ { n } ( x ) = 1$ , while at all of the minima $T _ { n } ( x ) = - 1$ ; it is precisely this property that makes the Chebyshev polynomials so useful in polynomial approximation of functions.

The Chebyshev polynomials satisfy a discrete orthogonality relation as well as the continuous one (5.8.3): If $x _ { k } ( k = 0 , \ldots , m - 1 )$ are the m zeros of $T _ { m } ( x )$ given by (5.8.4), and if $i , j < m$ , then

$$
\sum _ { k = 0 } ^ { m - 1 } T _ { i } ( x _ { k } ) T _ { j } ( x _ { k } ) = { \left\{ \begin{array} { l l } { 0 } & { i \neq j } \\ { m / 2 } & { i = j \neq 0 } \\ { m } & { i = j = 0 } \end{array} \right. }
$$

![](images/d6a1bdae899e062decc43c59210cf4ce5c89839e4300d48aad36f1d3950709c7.jpg)  
Figure 5.8.1. Chebyshev polynomials $T _ { 0 } ( x )$ through $T _ { 6 } ( x )$ . Note that $T _ { j }$ has $j$ roots in the interval $( - 1 , 1 )$ and that all the polynomials are bounded between $\pm 1$ .

It is not too difficult to combine equations (5.8.1), (5.8.4), and (5.8.6) to prove the following theorem: If $f ( x )$ is an arbitrary function in the interval $[ - 1 , 1 ]$ , and if $N$ coefficients $c _ { j } , j = 0 , \ldots , N - 1$ , are defined by

$$
\begin{array} { l } { \displaystyle { c _ { j } = \frac { 2 } { N } \sum _ { k = 0 } ^ { N - 1 } f ( x _ { k } ) T _ { j } ( x _ { k } ) } } \\ { \displaystyle { = \frac { 2 } { N } \sum _ { k = 0 } ^ { N - 1 } f \left[ \cos \left( \frac { \pi ( k + \frac { 1 } { 2 } ) } { N } \right) \right] \cos \left( \frac { \pi j ( k + \frac { 1 } { 2 } ) } { N } \right) } } \end{array}
$$

then the approximation formula

$$
f ( x ) \approx \left[ \sum _ { k = 0 } ^ { N - 1 } c _ { k } T _ { k } ( x ) \right] - \frac { 1 } { 2 } c _ { 0 }
$$

is exact for $x$ equal to all of the $N$ zeros of $T _ { N } ( x )$ .

For a fixed $N$ , equation (5.8.8) is a polynomial in $x$ that approximates the function $f ( x )$ in the interval $[ - 1 , 1 ]$ (where all the zeros of $T _ { N } ( x )$ are located). Why is this particular approximating polynomial better than any other one, exact on some other set of $N$ points? The answer is not that (5.8.8) is necessarily more accurate than some other approximating polynomial of the same order $N$ (for some specified definition of “accurate”), but rather that (5.8.8) can be truncated to a polynomial of lower degree $m \ll N$ in a very graceful way, one that does yield the “most accurate” approximation of degree $m$ (in a sense that can be made precise). Suppose $N$ is so large that (5.8.8) is virtually a perfect approximation of $f ( x )$ . Now consider the truncated approximation

$$
f ( x ) \approx \left[ \sum _ { k = 0 } ^ { m - 1 } c _ { k } T _ { k } ( x ) \right] - \frac { 1 } { 2 } c _ { 0 }
$$

with the same $c _ { j }$ ’s, computed from (5.8.7). Since the $T _ { k } ( x )$ ’s are all bounded between $\pm 1$ , the difference between (5.8.9) and (5.8.8) can be no larger than the sum of the neglected $c _ { k }$ ’s $( k = m , \ldots , N - 1 )$ . In fact, if the $c _ { k }$ ’s are rapidly decreasing (which is the typical case), then the error is dominated by $c _ { m } T _ { m } ( x )$ , an oscillatory function with $m + 1$ equal extrema distributed smoothly over the interval $[ - 1 , 1 ]$ . This smooth spreading out of the error is a very important property: The Chebyshev approximation (5.8.9) is very nearly the same polynomial as that holy grail of approximating polynomials the minimax polynomial, which (among all polynomials of the same degree) has the smallest maximum deviation from the true function $f ( x )$ . The minimax polynomial is very difficult to find; the Chebyshev approximating polynomial is almost identical and is very easy to compute!

So, given some (perhaps difficult) means of computing the function $f ( x )$ , we now need algorithms for implementing (5.8.7) and (after inspection of the resulting $c _ { k }$ ’s and choice of a truncating value $m$ ) evaluating (5.8.9). The latter equation then becomes an easy way of computing $f ( x )$ for all subsequent time.

The first of these tasks is straightforward. A generalization of equation (5.8.7) that is here implemented is to allow the range of approximation to be between two arbitrary limits $a$ and $b$ , instead of just $^ { - 1 }$ to 1. This is effected by a change of variable

$$
y \equiv { \frac { x - { \frac { 1 } { 2 } } ( b + a ) } { { \frac { 1 } { 2 } } ( b - a ) } }
$$

and by the approximation of $f ( x )$ by a Chebyshev polynomial in $y$ .

It will be convenient for us to group a number of functions related to Chebyshev polynomials into a single object, even though discussion of their specifics is spread out over $\ S 5 . 8 - \ S 5 . 1 1$ :

# struct Chebyshev {

Object for Chebyshev approximation and related methods.

Int n,m; Number of total, and truncated, coefficients.   
VecDoub c;   
Doub a,b; Approximation interval. Chebyshev(Doub func(Doub), Doub aa, Doub bb, Int nn);   
Constructor. Approximate the function func in the interval [aa,bb] with nn terms. Chebyshev(VecDoub &cc, Doub aa, Doub bb)   
: n(cc.size()), m(n), c(cc), a(aa), b(bb) {}   
Constructor from previously computed coefficients.   
Int setm(Doub thresh) {while (m>1 && abs(c[m-1])<thresh) m--; return m;} Set m, the number of coefficients after truncating to an error level thresh, and return the value set.

Doub eval(Doub x, Int m); inline Doub operator() (Doub x) {return eval(x,m);} Return a value for the Chebyshev fit, either using the stored m or else overriding it.

Chebyshev derivative(); See $\ S 5 . 9$ .   
Chebyshev integral();

VecDoub polycofs(Int m); See -5.10. inline VecDoub polycofs() {return polycofs(m);} Chebyshev(VecDoub &pc); See $\ S 5 . 1 1$ .

# };

The first constructor, the one with an arbitrary function func as its first argument, calculates and saves nn Chebyshev coefficients that approximate func in the range aa to bb. (You can ignore for now the second constructor, which simply makes a Chebyshev object from already-calculated data.) Let us also note the method setm, which provides a quick way to truncate the Chebyshev series by (in effect) deleting, from the right, all coefficients smaller in magnitude than some threshold thresh.

Chebyshev::Chebyshev(Doub func(Doub), Doub aa, Doub bb, Int $\mathtt { n n } mathtt { = } 5 0$ ) : n(nn), m(nn), c(n), a(aa), b(bb)

Chebyshev fit: Given a function func, lower and upper limits of the interval [a,b], compute and nn coe, where ientsand f the Chebyshev approximation such that are related by (5.8.10). This routine is in $\begin{array} { r } { \mathbf { f u n c } ( x ) \approx [ \sum _ { k = 0 } ^ { \mathtt { n n } - 1 } \mathtt { c } _ { k } T _ { k } ( y ) ] - } \end{array}$ $c _ { 0 } / 2$ $y$ $x$   
ately large n (e.g., 30 or 50), the array of c’s subsequently to be truncated at the smaller value m such that ${ \mathsf { c } } _ { m }$ and subsequent elements are negligible.   
{

const Doub pi $^ { = 3 }$ .141592653589793;Int k,j;Doub fac,bpa,bma,y,sum;VecDoub f(n);bma=0.5\*(b-a);bpa=0.5\*(b+a);for $_ { - \tt k = 0 }$ ;k<n;k++) { We evaluate the function at the n points requiredy=cos(pi\*(k+0.5)/n); by (5.8.7).f[k]=func(y\*bma+bpa);fac $^ { = 2 }$ .0/n;for $( \ j = 0$ ;j<n;j++) { Now evaluate (5.8.7).sum=0.0;for $\scriptstyle 1 = 0$ ;k<n;k++)sum $+ =$ f[k]\*cos(pi\*j\*(k+0.5)/n);c[j] ${ = } \mathbf { f }$ ac\*sum;}}

If you find that the constructor’s execution time is dominated by the calculation of $N ^ { 2 }$ cosines, rather than by the $N$ evaluations of your function, then you should look ahead to $\ S 1 2 . 3$ , especially equation (12.4.16), which shows how fast cosine transform methods can be used to evaluate equation (5.8.7).

Now that we have the Chebyshev coefficients, how do we evaluate the approximation? One could use the recurrence relation of equation (5.8.2) to generate values for $T _ { k } ( x )$ from $T _ { 0 } = 1 , T _ { 1 } = x$ , while also accumulating the sum of (5.8.9). It is better to use Clenshaw’s recurrence formula (-5.4), effecting the two processes simultaneously. Applied to the Chebyshev series (5.8.9), the recurrence is

$$
\begin{array} { c } { { d _ { m + 1 } \equiv d _ { m } \equiv 0 } } \\ { { d _ { j } = 2 x d _ { j + 1 } - d _ { j + 2 } + c _ { j } \qquad j = m - 1 , m - 2 , \ldots , 1 } } \\ { { f ( x ) \equiv d _ { 0 } = x d _ { 1 } - d _ { 2 } + \frac 1 2 c _ { 0 } } } \end{array}
$$

# Doub Chebyshev::eval(Doub $_ \textrm { x }$ , Int m)

Cheb v polynomial $\begin{array} { r } { \sum _ { k = 0 } ^ { \mathtt { m } - 1 } \mathtt { c } _ { k } T _ { k } ( y ) - \mathtt { c } _ { 0 } / 2 } \end{array}$ is evaluated at a $\mathtt { y } = [ \mathtt { x } - ( \mathtt { b } + \mathtt { a } ) / 2 ] / [ ( \mathtt { b } - \mathtt { a } ) / 2 ]$

Doub $\mathsf { d } = 0 \ldots 0 , \mathsf { d } \mathsf { d } = 0 \ldots 0 , \mathsf { s v } , \mathsf { y } , \mathsf { y } 2 ;$ ;   
Int j;   
if ( $( \mathbf { x } { - } \mathbf { a } ) * ( \mathbf { x } { - } \mathbf { b } ) \ > \ 0 \ldots 0 )$ throw("x not in range in Chebyshev::eval");   
$y 2 = 2 . 0 * ( y = ( 2 . 0 * \mathbf { x } - \mathbf { a } - \mathbf { b } ) / ( \mathbf { b } - \mathbf { a } ) )$ ; Change of variable.   
for $( \mathrm { j } { = } \mathrm { m } { - } 1$ ;j>0;j--) { Clenshaw’s recurrence. sv=d; d=y2\*d-dd+c[j]; dd=sv;   
}   
return y\*d-dd+0.5\*c[0]; Last step is different.

The method eval has an argument for specifying how many leading coefficients m should be used in the evaluation. If you simply want to use a stored value of m that was set by a previous call to setm (or, by hand, by you), then you can use the Chebyshev object as a functor. For example,

Chebyshev approxfunc(func,0.,1.,50);   
approxfunc.setm(1.e-8);   
$\mathrm { ~ y ~ } =$ approxfunc(x);

If we are approximating an even function on the interval $[ - 1 , 1 ]$ , its expansion will involve only even Chebyshev polynomials. It is wasteful to construct a Chebyshev object with all the odd coefficients zero [2]. Instead, using the half-angle identity for the cosine in equation (5.8.1), we get the relation

$$
T _ { 2 n } ( x ) = T _ { n } ( 2 x ^ { 2 } - 1 )
$$

Thus we can construct a more efficient Chebyshev object for even functions simply by replacing the function’s argument $x$ by $2 x ^ { 2 } - 1$ , and likewise when we evaluate the Chebyshev approximation.

An odd function will have an expansion involving only odd Chebyshev polynomials. It is best to rewrite it as an expansion for the function $f ( x ) / x$ , which involves only even Chebyshev polynomials. This has the added benefit of giving accurate values for $f ( x ) / x$ near $x = 0$ . Don’t try to construct the series by evaluating $f ( x ) / x$ numerically, however. Rather, the coefficients $c _ { n } ^ { \prime }$ for $f ( x ) / x$ can be found from those for $f ( x )$ by recurrence:

$$
\begin{array} { l } { { c _ { N + 1 } ^ { \prime } = 0 ~ } } \\ { { c _ { n - 1 } ^ { \prime } = 2 c _ { n } - c _ { n + 1 } ^ { \prime } , ~ n = N - 1 , N - 3 , . . . } } \end{array} . . .
$$

Equation (5.8.13) follows from the recurrence relation in equation (5.8.2).

If you insist on evaluating an odd Chebyshev series, the efficient way is to once again to replace $x$ by $y = 2 x ^ { 2 } - 1$ as the argument of your function. Now, however,

you must also change the last formula in equation (5.8.11) to be

$$
f ( x ) = x [ ( 2 y - 1 ) d _ { 1 } - d _ { 2 } + c _ { 0 } ]
$$

and change the corresponding line in eval.

# 5.8.1 Chebyshev and Exponential Convergence

Since first mentioning truncation error in $\ S 1 . 1$ , we have seen many examples of algorithms with an adjustable order, say $M$ , such that the truncation error decreases as the $M$ th power of something. Examples include most of the interpolation methods in Chapter 3 and most of the quadrature methods in Chapter 4. In these examples there is also another parameter, $N$ , which is the number of points at which a function will be evaluated.

We have many times warned that “higher order does not necessarily give higher accuracy.” That remains good advice when $N$ is held fixed while $M$ is increased. However, a recently emerging theme in many areas of scientific computation is the use of methods that allow, in very special cases, $M$ and $N$ to be increased together, with the result that errors not only do decrease with higher order, but decrease exponentially!

The common thread in almost all of these relatively new methods is the remarkable fact that infinitely smooth functions become exponentially well determined by $N$ sample points as $N$ is increased. Thus, mere power-law convergence may be just a consequence of either (i) functions that are not smooth enough, or (ii) endpoint effects.

We already saw several examples of this in Chapter 4. In $\ S 4 . 1$ we pointed out that high-order quadrature rules can have interior weights of unity, just like the trapezoidal rule; all of the “high-orderness” is obtained by a proper treatment near the boundaries. In $\ S 4 . 5$ we further saw that variable transformations that push the boundaries off to infinity produce rapidly converging quadrature algorithms. In $\ S 4 . 5 . 1$ we in fact proved exponential convergence, as a consequence of the Euler-Maclaurin formula. Then in $\ S 4 . 6$ we remarked on the fact that the convergence of Gaussian quadratures could be exponentially rapid (an example, in the language above, of increasing $M$ and $N$ simultaneously).

Chebyshev approximation can be exponentially convergent for a different (though related) reason: Smooth periodic functions avoid endpoint effects by not having endpoints at all! Chebyshev approximation can be viewed as mapping the $x$ interval $[ - 1 , 1 ]$ onto the angular interval $[ 0 , \pi ]$ (cf. equations 5.8.4 and 5.8.5) in such a way that any infinitely smooth function on the interval $[ - 1 , 1 ]$ becomes an infinitely smooth, even, periodic function on $[ 0 , 2 \pi ]$ . Figure 5.8.2 shows the idea geometrically. By projecting the abscissas onto a semicircle, a half-period is produced. The other half-period is obtained by reflection, or could be imagined as the result of projecting the function onto an identical lower semicircle. The zeros of the Chebyshev polynomial, or nodes of a Chebyshev approximation, are equally spaced on the circle, where the Chebyshev polynomial itself is a cosine function (cf. equation 5.8.1). This illustrates the close connection between Chebyshev approximation and periodic functions on the circle; in Chapter 12, we will apply the discrete Fourier transform to such functions in an almost equivalent way (-12.4.2).

The reason that Chebyshev works so well (and also why Gaussian quadratures work so well) is thus seen to be intimately related to the special way that the the sample points are bunched up near the endpoints of the interval. Any function that is bounded on the interval will have a convergent Chebyshev approximation as $N $ $\infty$ , even if there are nearby poles in the complex plane. For functions that are not infinitely smooth, the actual rate of convergence depends on the smoothness of the function: the more deriviatives that are bounded, the greater the convergence rate. For the special case of a $C ^ { \infty }$ function, the convergence is exponential. In $\ S 3 . 0$ , in connection with polynomial interpolation, we mentioned the other side of the coin: equally spaced samples on the interval are about the worst possible geometry and often lead to ill-conditioned problems.

![](images/f0fc758cfd9d4576544a8efb6fa5f298443061901a3689bf82882bff507bf88f.jpg)  
Figure 5.8.2. Geometrical construction showing how Chebyshev approximation is related to periodic functions. A smooth function on the interval is plotted in (a). In (b), the abscissas are mapped to a semicircle. In (c), the semicircle is unrolled. Because of the semicircle’s vertical tangents, the function is now nearly constant at the endpoints. In fact, if reflected into the interval $[ \pi , 2 \pi ]$ , it is a smooth, even, periodic function on $[ 0 , 2 \pi ]$ .

Use of the sampling theorem (-4.5, $\ S 6 . 9$ , $\ S 1 2 . 1$ , $\ S 1 3 . 1 1 \ r$ ) is often closely associated with exponentially convergent methods. We will return to many of the concepts of exponentially convergent methods when we discuss spectral methods for partial differential equations in $\ S 2 0 . 7$ .

# CITED REFERENCES AND FURTHER READING:

Arfken, G. 1970, Mathematical Methods for Physicists, 2nd ed. (New York: Academic Press), p. 631.[1]   
Clenshaw, C.W. 1962, Mathematical Tables, vol. 5, National Physical Laboratory (London: H.M. Stationery Office).[2]   
Goodwin, E.T. (ed.) 1961, Modern Computing Methods, 2nd ed. (New York: Philosophical Library), Chapter 8.   
Dahlquist, G., and Bjorck, A. 1974, Numerical Methods (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2003 (New York: Dover), $\ S 4 . 4 . 1$ , p. 104.   
Johnson, L.W., and Riess, R.D. 1982, Numerical Analysis, 2nd ed. (Reading, MA: Addison-Wesley), $\ S 6 . 5 . 2$ , p. 334.   
Carnahan, B., Luther, H.A., and Wilkes, J.O. 1969, Applied Numerical Methods (New York: Wiley), $\ S 1 . 1 0$ , p. 39.

# 5.9 Derivatives or Integrals of a Chebyshev-Approximated Function

If you have obtained the Chebyshev coefficients that approximate a function in a certain range (e.g., from chebft in $\ S 5 . 8 )$ , then it is a simple matter to transform them to Chebyshev coefficients corresponding to the derivative or integral of the function. Having done this, you can evaluate the derivative or integral just as if it were a function that you had Chebyshev-fitted ab initio.

The relevant formulas are these: If $c _ { i }$ ; $i = 0 , \ldots , m - 1$ are the coefficients that approximate a function $f$ in equation (5.8.9), $C _ { i }$ are the coefficients that approximate the indefinite integral of $f$ , and $c _ { i } ^ { \prime }$ are the coefficients that approximate the derivative of $f$ , then

$$
\begin{array} { c } { { C _ { i } = \displaystyle \frac { c _ { i - 1 } - c _ { i + 1 } } { 2 i } \qquad ( i > 0 ) } } \\ { { c _ { i - 1 } ^ { \prime } = c _ { i + 1 } ^ { \prime } + 2 i c _ { i } \qquad ( i = m - 1 , m - 2 , \ldots , 1 ) } } \end{array}
$$

Equation (5.9.1) is augmented by an arbitrary choice of $C _ { 0 }$ , corresponding to an arbitrary constant of integration. Equation (5.9.2), which is a recurrence, is started with the values $c _ { m } ^ { \prime } = c _ { m - 1 } ^ { \prime } = 0$ , corresponding to no information about the $m + 1 \mathrm { s t }$ Chebyshev coefficient of the original function $f$ .

Here are routines for implementing equations (5.9.1) and (5.9.2). Each returns a new Chebyshev object on which you can setm, call eval, or use directly as a functor.

# Chebyshev Chebyshev::derivative()

Return a new Chebyshev object that approximates the derivative of the existing function over the same range [a,b].

Int j;   
Doub con;   
VecDoub cder(n);   
cder $\left[ \mathrm { n - 1 } \right] { = } 0 . 0$ ;   
cder[n-2] $^ { - 2 * }$ (n-1)\*c[n-1];   
for (j=n-2;j>0;j--) cder[j-1] $=$ cder[j+1]+2\*j\*c[j];   
con=2.0/(b-a);   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n; ${ \mathrm { j } } + +$ ) cder[j] $\ast =$ con;   
return Chebyshev(cder,a,b);

$\mathtt { n - 1 }$ and $\mathtt { n } \mathtt { - } 2$ are special cases.

Equation (5.9.2).

Normalize to the interval b-a.

# Chebyshev Chebyshev::integral()

Return a new Chebyshev object that approximates the indefinite integral of the existing function over the same range [a,b]. The constant of integration is set so that the integral vanishes at a. {

Int j;  
Doub sum $_ { = 0 }$ .0,fac $= 1$ .0,con;  
VecDoub cint(n);  
con=0.25\*(b-a);  
for $\displaystyle { ( \ j = 1 }$ ;j<n-1;j $^ { + + }$ ) {cint[j] $=$ con\*(c[j-1]-c[j+1])/j;sum $+ =$ fac\*cint[j];fac $=$ -fac;  
}  
cint[n-1] $=$ con\*c[n-2]/(n-1);

Factor that normalizes to the interval $^ \mathtt { b - a }$

Equation (5.9.1).   
Accumulates the constant of integration.   
Will equal $\pm 1$ .

Special case of (5.9.1) for $\mathtt { n - 1 }$ .

sum $+ =$ fac\*cint[n-1];   
cint[0] $^ { = 2 }$ . $^ { 0 * }$ sum;   
return Chebyshev(cint,a,b);

Set the constant of integration.

# 5.9.1 Clenshaw-Curtis Quadrature

Since a smooth function’s Chebyshev coefficients $c _ { i }$ decrease rapidly, generally exponentially, equation (5.9.1) is often quite efficient as the basis for a quadrature scheme. As described above, the Chebyshev object can be used to compute the integral $\textstyle { \int _ { a } ^ { x } f ( x ) d x }$ when many different values of $x$ in the range $a \ \leq \ x \ \leq \ b$ are needed. If only the single definite integral $\textstyle \int _ { a } ^ { b } f ( x ) d x$ is required, then instead use the simpler formula, derived from equation (5.9.1),

$$
\int _ { a } ^ { b } f ( x ) d x = ( b - a ) \left[ { \frac { 1 } { 2 } } c _ { 0 } - { \frac { 1 } { 3 } } c _ { 2 } - { \frac { 1 } { 1 5 } } c _ { 4 } - \cdots - { \frac { 1 } { ( 2 k + 1 ) ( 2 k - 1 ) } } c _ { 2 k } - \cdots \right]
$$

where the $c _ { i }$ ’s are as returned by chebft. The series can be truncated when $c _ { 2 k }$ becomes negligible, and the first neglected term gives an error estimate.

This scheme is known as Clenshaw-Curtis quadrature [1]. It is often combined with an adaptive choice of $N$ , the number of Chebyshev coefficients calculated via equation (5.8.7), which is also the number of function evaluations of $f ( x )$ . If a modest choice of $N$ does not give a sufficiently small $c _ { 2 k }$ in equation (5.9.3), then a larger value is tried. In this adaptive case, it is even better to replace equation (5.8.7) by the so-called “trapezoidal” or Gauss-Lobatto (-4.6) variant,

$$
c _ { j } = { \frac { 2 } { N } } \sum _ { k = 0 } ^ { N } f \left[ \cos \left( { \frac { \pi k } { N } } \right) \right] \cos \left( { \frac { \pi j k } { N } } \right) \qquad j = 0 , \dots , N - 1
$$

where (N.B.!) the two primes signify that the first and last terms in the sum are to be multiplied by $1 / 2$ . If $N$ is doubled in equation (5.9.4), then half of the new function evaluation points are identical to the old ones, allowing the previous function evaluations to be reused. This feature, plus the analytic weights and abscissas (cosine functions in 5.9.4), often give Clenshaw-Curtis quadrature an edge over high-order adaptive Gaussian quadrature (cf. $\ S 4 . 6 . 4 )$ , which the method otherwise resembles.

If your problem forces you to large values of $N$ , you should be aware that equation (5.9.4) can be evaluated rapidly, and simultaneously for all the values of $j$ , by a fast cosine transform. (See $\ S 1 2 . 3$ , especially equation 12.4.11. We already remarked that the nontrapezoidal form (5.8.7) can also be done by fast cosine methods, cf. equation 12.4.16.)

# CITED REFERENCES AND FURTHER READING:

Goodwin, E.T. (ed.) 1961, Modern Computing Methods, 2nd ed. (New York: Philosophical Library), pp. 78–79.   
Clenshaw, C.W., and Curtis, A.R. 1960, “A Method for Numerical Integration on an Automatic Computer,” Numerische Mathematik, vol. 2, pp. 197–205.[1]

# 5.10 Polynomial Approximation from Chebyshev Coefficients

You may well ask after reading the preceding two sections: Must I store and evaluate my Chebyshev approximation as an array of Chebyshev coefficients for a transformed variable $y$ ?

Can’t I convert the $c _ { k }$ ’s into actual polynomial coefficients in the original variable $x$ and have an approximation of the following form?

$$
f ( x ) \approx \sum _ { k = 0 } ^ { m - 1 } g _ { k } x ^ { k } , \qquad a \leq x \leq b
$$

Yes, you can do this (and we will give you the algorithm to do it), but we caution you against it: Evaluating equation (5.10.1), where the coefficient $g$ ’s reflect an underlying Chebyshev approximation, usually requires more significant figures than evaluation of the Chebyshev sum directly (as by eval). This is because the Chebyshev polynomials themselves exhibit a rather delicate cancellation: The leading coefficient of $T _ { n } ( x )$ , for example, is $2 ^ { n - 1 }$ ; other coefficients of $T _ { n } ( x )$ are even bigger; yet they all manage to combine into a polynomial that lies between $\pm 1$ . Only when $m$ is no larger than 7 or 8 should you contemplate writing a Chebyshev fit as a direct polynomial, and even in those cases you should be willing to tolerate two or so significant figures less accuracy than the roundoff limit of your machine.

You get the $g$ ’s in equation (5.10.1) in two steps. First, use the member function polycofs in Chebyshev to output a set of polynomial coefficients equivalent to the stored $c _ { k }$ ’s (that is, with the range $[ a , b ]$ scaled to $[ - 1 , 1 ] ,$ ). Second, use the routine pcshft to transform the coefficients so as to map the range back to $[ a , b ]$ . The two required routines are listed here:

# VecDoub Chebyshev::polycofs(Int m)

Polynomial coefficients from a Chebyshev fit. Given a coefficient array $\mathbf { c } \left[ 0 \ldots \mathbf { n - 1 } \right]$ , this routine returns a coefficient array method is Clenshaw’s recu ${ \mathsf { d } } \left[ 0 \ldots \mathbf { n - 1 } \right]$ such that .11), but n $\begin{array} { r } { \sum _ { k = 0 } ^ { \mathtt { n } - 1 } \mathtt { d } _ { k } y ^ { k } = \sum _ { k = 0 } ^ { \mathtt { n } - 1 } \mathtt { c } _ { k } T _ { k } ( y ) - \mathtt { c } _ { 0 } / 2 } \end{array}$ . Themetically.

Int k,j;  
Doub sv;  
VecDoub d(m),dd(m);  
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<m;j++) d[j] $=$ dd[j] ${ = } 0$ .0;  
d[0] $= \mathtt { c }$ [m-1];  
for $\scriptstyle \cdot j = m - 2$ ;j>0;j--) {for (k=m-j;k>0;k--) {sv=d[k];d[k]=2.0\*d[k-1]-dd[k];dd[k] $=$ sv;}$\tt S V = d$ [0];d[0] $=$ -dd[0]+c[j];dd[0] $=$ sv;  
}  
for $\scriptstyle \cdot j = m - 1$ ;j>0;j--) d[j] $=$ d[j-1]-dd[j];  
d[0] $=$ -dd[0] $+ 0$ .5\*c[0];  
return d;

void pcshft(Doub a, Doub b, VecDoub_IO &d)

Polynomial coefficient shift. Given a coefficient array ${ \mathsf { d } } \left[ 0 \ldots \ldots \mathbf { n - 1 } \right]$ , this routine generates a coefficient array $g \left[ 0 \ldots \ldots \ldots \right]$ such that $\textstyle \sum _ { k = 0 } ^ { \mathtt { n } - 1 } \mathtt { d } _ { k } y ^ { k } = \sum _ { k = 0 } ^ { \mathtt { n } - 1 } g _ { k } x ^ { k }$ , where $x$ and $y$ are related by (5.8.10), i.e., the interval $- 1 < y < 1$ is mapped to the interval ${ \mathfrak { a } } < x < { \mathfrak { b } }$ . The array $_ g$ returned in d.

Int k,j, $\mathtt { n } { = } \mathtt { d }$ .size();   
Doub cnst $^ { = 2 }$ .0/(b-a), fac=cnst;   
for $( \ j = 1$ ;j<n;j $^ { + + }$ ) { First we rescale by the factor const... d[j] $\ast =$ fac; fac $\ast =$ cnst;   
}   
cnst ${ = } 0$ .5\*(a+b); ...which is then redefined as the desired shift.

for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j $< = \mathtt { n } - 2$ ;j++) We accomplish the shift by synthetic division, a miracle for (k=n-2;k>=j;k--) of high-school algebra. d[k] $- =$ cnst\*d[k $^ { + 1 ] }$ ;

# CITED REFERENCES AND FURTHER READING:

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), pp. 59, 182–183 [synthetic division].

# 5.11 Economization of Power Series

One particular application of Chebyshev methods, the economization of power series, is an occasionally useful technique, with a flavor of getting something for nothing.

Suppose that you know how to compute a function by the use of a convergent power series, for example,

$$
f ( x ) \equiv { \frac { 1 } { 2 } } - { \frac { x } { 4 } } + { \frac { x ^ { 2 } } { 8 } } - { \frac { x ^ { 3 } } { 1 6 } } + \cdots
$$

(This function is actually just $1 / ( x + 2 )$ , but pretend you don’t know that.) You might be doing a problem that requires evaluating the series many times in some particular interval, say Œ0; 1. Everything is fine, except that the series requires a large number of terms before its error (approximated by the first neglected term, say) is tolerable. In our example, with $x = 1$ , it takes about 30 terms before the first neglected term is $< 1 0 ^ { - 9 }$ .

Notice that because of the large exponent in $x ^ { 3 0 }$ , the error is much smaller than $1 0 ^ { - 9 }$ everywhere in the interval except at the very largest values of $x$ . This is the feature that allows “economization”: If we are willing to let the error elsewhere in the interval rise to about the same value that the first neglected term has at the extreme end of the interval, then we can replace the 30-term series by one that is significantly shorter.

Here are the steps for doing this:

1. Compute enough coefficients of the power series to get accurate function values everywhere in the range of interest.   
2. Change variables from $x$ to $y$ , as in equation (5.8.10), to map the $x$ interval into $- 1 \leq$ $y \le 1$ .   
3. Find the Chebyshev series (like equation 5.8.8) that exactly equals your truncated power series.   
4. Truncate this Chebyshev series to a smaller number of terms, using the coefficient of the first neglected Chebyshev polynomial as an estimate of the error.   
5. Convert back to a polynomial in $y$ .   
6. Change variables back to $x$ .

We already have tools for all of the steps, except for steps 2 and 3. Step 2 is exactly the inverse of the routine pcshft (-5.10), which mapped a polynomial from $y$ (in the interval $[ - 1 , 1 ] )$ to $x$ (in the interval $[ a , b ] )$ ). But since equation (5.8.10) is a linear relation between $x$ and $y$ , one can also use pcshft for the inverse. The inverse of

$$
\mathtt { p c s h f t } ( a , b , \mathtt { d } , \mathtt { n } )
$$

turns out to be (you can check this)

Step 3 requires a new Chebyshev constructor, one that computes Chebyshev coefficients from a vector of polynomial coefficients. The following code accomplishes this. The algorithm is based on constructing the polynomial by the technique of $\ S 5 . 3$ starting with the highest coefficient d[n-1] and using the recurrence of equation (5.8.2) written in the form

$$
\begin{array} { l } { { x T _ { 0 } = T _ { 1 } } } \\ { { x T _ { n } = \frac { 1 } { 2 } ( T _ { n + 1 } + T _ { n - 1 } ) , \quad n \geq 1 . } } \end{array}
$$

The only subtlety is to multiply the coefficient of $T _ { 0 }$ by 2 since it gets used with a factor 1/2 in equation (5.8.8).

Chebyshev::Chebyshev(VecDoub &d) : n(d.size()), ${ \mathfrak { m } } ( { \mathfrak { n } } )$ , ${ \mathsf { c } } \left( { \mathtt { n } } \right)$ , $\mathsf { a } ( - 1 . )$ , b(1.)   
Inverse of routine polycofs in Chebyshev: Given an array of polynomial coefficients d[0..n-1],   
construct an equivalent Chebyshev object.

c[n-1] ${ \overline { { = } } } \dot { \mathsf { c } }$ d[n-1];c[n-2] $^ { = 2 }$ .0\*d[n-2];for (Int $\scriptstyle { \dot { \mathtt { j } } } = { \mathtt { n } } - 3$ ;j>=0;j--) {c[j]=2.0\*d[j]+c[j+2];for (Int i=j+1;i<n-2;i++) {c[i] $=$ (c[i]+c[i+2])/2;}c[n-2] /= 2;c[n-1] /= 2;}}

Putting them all together, steps 2 through 6 will look something like this (starting with a vector powser of power series coefficients):

ipcshft(a,b,powser);   
Chebyshev cpowser(powser);   
cpowser.setm(1.e-9);   
VecDoub $\mathtt { d } =$ cpowser.polycofs();   
pcshft(a,b,d);

In our example, by the way, the number of terms required for $1 0 ^ { - 9 }$ accuracy is reduced from 30 to 9. Replacing a 30-term polynomial with a 9-term polynomial without any loss of accuracy — that does seem to be getting something for nothing. Is there some magic in this technique? Not really. The 30-term polynomial defined a function $f ( x )$ . Equivalent to economizing the series, we could instead have evaluated $f ( x )$ at enough points to construct its Chebyshev approximation in the interval of interest, by the methods of $\ S 5 . 8$ . We would have obtained just the same lower-order polynomial. The principal lesson is that the rate of convergence of Chebyshev coefficients has nothing to do with the rate of convergence of power series coefficients; and it is the former that dictates the number of terms needed in a polynomial approximation. A function might have a divergent power series in some region of interest, but if the function itself is well-behaved, it will have perfectly good polynomial approximations. These can be found by the methods of $\ S 5 . 8$ , but not by economization of series. There is slightly less to economization of series than meets the eye.

# CITED REFERENCES AND FURTHER READING:

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), Chapter 12.

# 5.12 Padé Approximants

A Pade approximant ´ , so called, is that rational function (of a specified order) whose power series expansion agrees with a given power series to the highest possible order. If the rational function is

$$
R ( x ) \equiv { \frac { \displaystyle \sum _ { k = 0 } ^ { M } a _ { k } x ^ { k } } { \displaystyle 1 + \sum _ { k = 1 } ^ { N } b _ { k } x ^ { k } } }
$$

then $R ( x )$ is said to be a Pade approximant to the series ´

$$
f ( x ) \equiv \sum _ { k = 0 } ^ { \infty } c _ { k } x ^ { k }
$$

if

$$
R ( 0 ) = f ( 0 )
$$

and also

$$
\left. { \frac { d ^ { k } } { d x ^ { k } } } R ( x ) \right| _ { x = 0 } = \left. { \frac { d ^ { k } } { d x ^ { k } } } f ( x ) \right| _ { x = 0 } , \qquad k = 1 , 2 , \ldots , M + N
$$

Equations (5.12.3) and (5.12.4) furnish $M + N + 1$ equations for the unknowns $a _ { 0 } , \dots , a _ { M }$ and $b _ { 1 } , \dots , b _ { N }$ . The easiest way to see what these equations are is to equate (5.12.1) and (5.12.2), multiply both by the denominator of equation (5.12.1), and equate all powers of $x$ that have either $a$ ’s or $b$ ’s in their coefficients. If we consider only the special case of a diagonal rational approximation, $M = N$ (cf. -3.4), then we have $a _ { \mathbf { 0 } } = c _ { \mathbf { 0 } }$ , with the remaining $a$ ’s and $b$ ’s satisfying

$$
\begin{array} { l } { { \displaystyle \sum _ { m = 1 } ^ { N } b _ { m } c _ { N - m + k } = - c _ { N + k } , \quad \quad k = 1 , \dots , N } } \\ { { \displaystyle \qquad \sum _ { m = 0 } ^ { k } b _ { m } c _ { k - m } = a _ { k } , \qquad \quad k = 1 , \dots , N } } \end{array}
$$

(note, in equation 5.12.1, that $b _ { 0 } = 1$ ). To solve these, start with equations (5.12.5), which are a set of linear equations for all the unknown $b$ ’s. Although the set is in the form of a Toeplitz matrix (compare equation 2.8.8), experience shows that the equations are frequently close to singular, so that one should not solve them by the methods of $\ S 2 . 8$ , but rather by full $L U$ decomposition. Additionally, it is a good idea to refine the solution by iterative improvement (method mprove in $\ S 2 . 5 )$ [1].

Once the $b$ ’s are known, then equation (5.12.6) gives an explicit formula for the unknown $a$ ’s, completing the solution.

Pade approximants are typically used when there is some unknown underlying function ´ $f ( x )$ . We suppose that you are able somehow to compute, perhaps by laborious analytic expansions, the values of $f ( x )$ and a few of its derivatives at $x = 0$ : $f ( 0 )$ , $f ^ { \prime } ( 0 )$ , $f ^ { \prime \prime } ( 0 )$ , and so on. These are of course the first few coefficients in the power series expansion of $f ( x )$ ; but they are not necessarily getting small, and you have no idea where (or whether) the power series is convergent.

By contrast with techniques like Chebyshev approximation $( \ S 5 . 8 )$ or economization of power series (-5.11) that only condense the information that you already know about a function, Pade approximants can give you genuinely new information about your function’s values. ´

![](images/bef37d06baaf4c252cd776bfd0cee67622398e92e27fe548bc76bc9be6654440.jpg)  
Figure 5.12.1. The five-term power series expansion and the derived five-coefficient Pade approximant for ´ a sample function $f ( x )$ . The full power series converges only for $x < 1$ . Note that the Pade approximant ´ maintains accuracy far outside the radius of convergence of the series.

It is sometimes quite mysterious how well this can work. (Like other mysteries in mathematics, it relates to analyticity.) An example will illustrate.

Imagine that, by extraordinary labors, you have ground out the first five terms in the power series expansion of an unknown function $f ( x )$ ,

$$
f ( x ) \approx 2 + { \frac { 1 } { 9 } } x + { \frac { 1 } { 8 1 } } x ^ { 2 } - { \frac { 4 9 } { 8 7 4 8 } } x ^ { 3 } + { \frac { 1 7 5 } { 7 8 7 3 2 } } x ^ { 4 } + \cdots
$$

(It is not really necessary that you know the coefficients in exact rational form — numerical values are just as good. We here write them as rationals to give you the impression that they derive from some side analytic calculation.) Equation (5.12.7) is plotted as the curve labeled “power series” in Figure 5.12.1. One sees that for $x \ \gtrsim \ 4$ it is dominated by its largest, quartic, term.

We now take the five coefficients in equation (5.12.7) and run them through the routine pade listed below. It returns five rational coefficients, three $a$ ’s and two $b$ ’s, for use in equation (5.12.1) with $M = N = 2$ . The curve in the figure labeled “Pade” plots the resulting rational ´ function. Note that both solid curves derive from the same five original coefficient values.

To evaluate the results, we need Deus ex machina (a useful fellow, when he is available) to tell us that equation (5.12.7) is in fact the power series expansion of the function

$$
f ( x ) = [ 7 + ( 1 + x ) ^ { 4 / 3 } ] ^ { 1 / 3 }
$$

which is plotted as the dotted curve in the figure. This function has a branch point at $x = - 1$ , so its power series is convergent only in the range $- 1 ~ < ~ x ~ < ~ 1$ . In most of the range shown in the figure, the series is divergent, and the value of its truncation to five terms is rather meaningless. Nevertheless, those five terms, converted to a Pade approximant, give a ´ remarkably good representation of the function up to at least $x \sim 1 0$ .

Why does this work? Are there not other functions with the same first five terms in their power series but completely different behavior in the range (say) $2 < x < 1 0 ?$ Indeed there are. Pade approximation has the uncanny knack of picking the function ´ you had in mind from among all the possibilities. Except when it doesn’t! That is the downside of Pade´ approximation: It is uncontrolled. There is, in general, no way to tell how accurate it is, or how far out in $x$ it can usefully be extended. It is a powerful, but in the end still mysterious, technique.

Here is the routine that returns a Ratfn rational function object that is the Pade approxi-´ mant to a set of power series coefficients that you provide. Note that the routine is specialized to the case $M = N$ . You can then use the Ratfn object directly as a functor, or else read out its coefficients by hand (-5.1).

# Ratfn pade(VecDoub_I &cof)

Given cof $[ 0 \ldots 2 * \mathtt { n } ]$ , the leading terms in the power series expansion of a function, solve the linear Pad´e equations to return a Ratfn object that embodies a diagonal rational function approximation to the same function.

const Doub BIG $^ { - 1 }$ .0e99;   
Int j,k, $\mathbf { n } =$ (cof.size()-1)/2;   
Doub sum;   
MatDoub q(n,n),qlu(n,n);   
VecInt indx(n);   
VecDoub x(n),y(n),num(n+1),denom $\left( \mathtt { n } + 1 \right)$ ;   
for (j=0;j<n;j++) { Set up matrix for solving. y[j] $=$ cof[n+j+1]; for $\scriptstyle ( \mathtt { k } = 0$ ;k<n;k++) q[j][k] $=$ cof[j-k+n];   
}   
LUdcmp lu(q); Solve by $_ { L U }$ decomposition and backsubstitu  
lu.solve(y,x); tion, with iterative improvement.   
for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<4; ${ \mathrm { j } } + + { \mathrm { j } }$ ) lu.mprove(y,x);   
for $\scriptstyle \mathbf { k } = 0$ ;k<n;k++) { Calculate the remaining coefficients. for (sum=cof[k+1], $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j $< = \mathrm { k }$ ;j $^ { + + }$ ) sum $- = \texttt { x }$ [j]\*cof[k-j]; y[k] $=$ sum;   
num[0] $=$ cof[0];   
denom[0] $\mathit { \Theta } = \mathit { \Theta } 1 \cdot$ ;   
for (j=0;j<n; $\mathrm { j } { + + } )$ { Copy answers to output. num[j+1]=y[j]; denom[j+1] $=$ -x[j];   
}   
return Ratfn(num,denom);

# CITED REFERENCES AND FURTHER READING:

Ralston, A. and Wilf, H.S. 1960, Mathematical Methods for Digital Computers (New York: Wiley), p. 14.   
Cuyt, A., and Wuytack, L. 1987, Nonlinear Methods in Numerical Analysis (Amsterdam: North-Holland), Chapter 2.   
Graves-Morris, P.R. 1979, in Padé Approximation and Its Applications, Lecture Notes in Mathematics, vol. 765, L. Wuytack, ed. (Berlin: Springer).[1]

# 5.13 Rational Chebyshev Approximation

In $\ S 5 . 8$ and $\ S 5 . 1 0$ we learned how to find good polynomial approximations to a given function $f ( x )$ in a given interval $a \leq x \leq b$ . Here, we want to generalize the task to find good approximations that are rational functions (see $\ S 5 . 1 \ r .$ ). The reason for doing so is that, for some functions and some intervals, the optimal rational function approximation is able to achieve substantially higher accuracy than the optimal polynomial approximation with the same number of coefficients. This must be weighed against the fact that finding a rational function approximation is not as straightforward as finding a polynomial approximation, which, as we saw, could be done elegantly via Chebyshev polynomials.

Let the desired rational function $R ( x )$ have a numerator of degree $m$ and denominator of degree $k$ . Then we have

$$
R ( x ) \equiv { \frac { p _ { 0 } + p _ { 1 } x + \cdots + p _ { m } x ^ { m } } { 1 + q _ { 1 } x + \cdots + q _ { k } x ^ { k } } } \approx f ( x ) \qquad { \mathrm { f o r ~ } } a \leq x \leq b
$$

The unknown quantities that we need to find are $p _ { 0 } , \ldots , p _ { m }$ and $q _ { 1 } , \ldots , q _ { k }$ , that is, $m +$ $k + 1$ quantities in all. Let $r ( x )$ denote the deviation of $R ( x )$ from $f ( x )$ , and let $r$ denote its maximum absolute value,

$$
r ( x ) \equiv R ( x ) - f ( x ) \qquad r \equiv \operatorname* { m a x } _ { a \leq x \leq b } | r ( x ) |
$$

The ideal minimax solution would be that choice of $p$ ’s and $q$ ’s that minimizes $r$ . Obviously there is some minimax solution, since $r$ is bounded below by zero. How can we find it, or a reasonable approximation to it?

A first hint is furnished by the following fundamental theorem: If $R ( x )$ is nondegenerate (has no common polynomial factors in numerator and denominator), then there is a unique choice of $p$ ’s and $q$ ’s that minimizes $r$ ; for this choice, $r ( x )$ has $m + k + 2$ extrema in $a \leq x \leq b$ , all of magnitude $r$ and with alternating sign. (We have omitted some technical assumptions in this theorem. See Ralston [1] for a precise statement.) We thus learn that the situation with rational functions is quite analogous to that for minimax polynomials: In $\ S 5 . 8$ we saw that the error term of an nth-order approximation, with $n + 1$ Chebyshev coefficients, was generally dominated by the first neglected Chebyshev term, namely $T _ { n + 1 }$ , which itself has $n + 2$ extrema of equal magnitude and alternating sign. So, here, the number of rational coefficients, $m + k + 1$ , plays the same role of the number of polynomial coefficients, $n + 1$ .

A different way to see why $r ( x )$ should have $m + k + 2$ extrema is to note that $R ( x )$ can be made exactly equal to $f ( x )$ at any $m + k + 1$ points $x _ { i }$ . Multiplying equation (5.13.1) by its denominator gives the equations

$$
p _ { 0 } + p _ { 1 } x _ { i } + \cdot \cdot \cdot + p _ { m } x _ { i } ^ { m } = f ( x _ { i } ) ( 1 + q _ { 1 } x _ { i } + \cdot \cdot \cdot + q _ { k } x _ { i } ^ { k } ) \qquad i = 0 , 1 , \dots , m + k ,
$$

This is a set of $m + k + 1$ linear equations for the unknown $p$ ’s and $q$ ’s, which can be solved by standard methods (e.g., $L U$ decomposition). If we choose the $x _ { i }$ ’s to all be in the interval $( a , b )$ , then there will generically be an extremum between each chosen $x _ { i }$ and $x _ { i + 1 }$ , plus also extrema where the function goes out of the interval at $a$ and $b$ , for a total of $m + k + 2$ extrema. For arbitrary $x _ { i }$ ’s, the extrema will not have the same magnitude. The theorem says that, for one particular choice of $x _ { i }$ ’s, the magnitudes can be beaten down to the identical, minimal, value of $r$ .

Instead of making $f ( x _ { i } )$ and $R ( x _ { i } )$ equal at the points $x _ { i }$ , one can instead force the residual $r ( x _ { i } )$ to any desired values $y _ { i }$ by solving the linear equations

$$
p _ { 0 } + p _ { 1 } x _ { i } + \cdots + p _ { m } x _ { i } ^ { m } = [ f ( x _ { i } ) - y _ { i } ] ( 1 + q _ { 1 } x _ { i } + \cdots + q _ { k } x _ { i } ^ { k } ) \qquad i = 0 , 1 , \ldots , m + k
$$

In fact, if the $x _ { i } { } ^ { \mathrm { i } }$ ’s are chosen to be the extrema (not the zeros) of the minimax solution, then the equations satisfied will be

$$
p _ { 0 } + p _ { 1 } x _ { i } + \dots + p _ { m } x _ { i } ^ { m } = [ f ( x _ { i } ) \pm r ] ( 1 + q _ { 1 } x _ { i } + \dots + q _ { k } x _ { i } ^ { k } ) \qquad i = 0 , 1 , \dots , m + k + 1
$$

where the $\pm$ alternates for the alternating extrema. Notice that equation (5.13.5) is satisfied at $m + k + 2$ extrema, while equation (5.13.4) was satisfied only at $m + k + 1$ arbitrary points. How can this be? The answer is that $r$ in equation (5.13.5) is an additional unknown, so that the number of both equations and unknowns is $m + k + 2$ . True, the set is mildly nonlinear (in $r$ ), but in general it is still perfectly soluble by methods that we will develop in Chapter 9.

We thus see that, given only the locations of the extrema of the minimax rational function, we can solve for its coefficients and maximum deviation. Additional theorems, leading up to the so-called Remes algorithms [1], tell how to converge to these locations by an iterative process. For example, here is a (slightly simplified) statement of Remes’ Second Algorithm: (1) Find an initial rational function with $m + k + 2$ extrema $x _ { i }$ (not having equal deviation). (2) Solve equation (5.13.5) for new rational coefficients and $r$ . (3) Evaluate the resulting $R ( x )$ to find its actual extrema (which will not be the same as the guessed values). (4) Replace each guessed value with the nearest actual extremum of the same sign. (5) Go back to step 2 and iterate to convergence. Under a broad set of assumptions, this method will converge. Ralston [1] fills in the necessary details, including how to find the initial set of $x _ { i }$ ’s.

Up to this point, our discussion has been textbook standard. We now reveal ourselves as heretics. We don’t much like the elegant Remes algorithm. Its two nested iterations (on $r$ in the nonlinear set 5.13.5, and on the new sets of $x _ { i }$ ’s) are finicky and require a lot of special logic for degenerate cases. Even more heretical, we doubt that compulsive searching for the exactly best, equal deviation approximation is worth the effort — except perhaps for those few people in the world whose business it is to find optimal approximations that get built into compilers and microcode.

When we use rational function approximation, the goal is usually much more pragmatic: Inside some inner loop we are evaluating some function a zillion times, and we want to speed up its evaluation. Almost never do we need this function to the last bit of machine accuracy. Suppose (heresy!) we use an approximation whose error has $m + k + 2$ extrema whose deviations differ by a factor of 2. The theorems on which the Remes algorithms are based guarantee that the perfect minimax solution will have extrema somewhere within this factor of 2 range — forcing down the higher extrema will cause the lower ones to rise, until all are equal. So our “sloppy” approximation is in fact within a fraction of a least significant bit of the minimax one.

That is good enough for us, especially when we have available a very robust method for finding the so-called “sloppy” approximation. Such a method is the least-squares solution of overdetermined linear equations by singular value decomposition ( $\ S 2 . 6$ and $\ S 1 5 . 4 )$ . We proceed as follows: First, solve (in the least-squares sense) equation (5.13.3), not just for $m + k + 1$ values of $x _ { i }$ , but for a significantly larger number of $x _ { i } { } ^ { \mathrm { : } }$ s, spaced approximately like the zeros of a high-order Chebyshev polynomial. This gives an initial guess for $R ( x )$ . Second, tabulate the resulting deviations, find the mean absolute deviation, call it $r$ , and then solve (again in the least-squares sense) equation (5.13.5) with $r$ fixed and the $\pm$ chosen to be the sign of the observed deviation at each point $x _ { i }$ . Third, repeat the second step a few times.

You can spot some Remes orthodoxy lurking in our algorithm: The equations we solve are trying to bring the deviations not to zero, but rather to plus-or-minus some consistent value. However, we dispense with keeping track of actual extrema, and we solve only linear equations at each stage. One additional trick is to solve a weighted least-squares problem, where the weights are chosen to beat down the largest deviations fastest.

Here is a function implementing these ideas. Notice that the only calls to the function fn occur in the initial filling of the table fs. You could easily modify the code to do this filling outside of the routine. It is not even necessary that your abscissas xs be exactly the ones that we use, though the quality of the fit will deteriorate if you do not have several abscissas between each extremum of the (underlying) minimax solution. The function returns a Ratfn object that you can subsequently use as a functor, or from which you can extract the stored coefficients.

Ratfn ratlsq(Doub fn(const Doub), const Doub a, const Doub b, const Int mm, const Int kk, Doub &dev)

Returns a rational function approximation to the function fn in the interval $( \mathsf { a } , \mathsf { b } )$ . Input quantities mm and kk specify the order of the numerator and denominator, respectively. The maximum absolute deviation of the approximation (insofar as is known) is returned as dev.

Int i,it,j,ncof=mm+kk+1,npt ${ } = { }$ NPFAC\*ncof;   
Number of points where function is evaluated, i.e., fineness of the mesh.   
Doub devmax,e,hth,power,sum;   
VecDoub bb(npt),coff(ncof),ee(npt),fs(npt),wt(npt),xs(npt);   
MatDoub u(npt,ncof);   
Ratfn ratbest(coff,mm+1,kk+1);   
dev=BIG;   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<npt; $\mathrm { i } + +$ ) { Fill arrays with mesh abscissas and function valif (i < (npt/2)-1) { ues. hth=PIO2\*i/(npt-1.0); At each end, use formula that minimizes roundxs[i]=a+(b-a)\*SQR(sin(hth)); off sensitivity. } else { hth=PIO2\*(npt-i)/(npt-1.0); xs[i]=b-(b-a)\*SQR(sin(hth)); fs[i]=fn(xs[i]); wt[i]=1.0; In later iterations we will adjust these weights to ee[i]=1.0; combat the largest deviations.   
}   
$\mathtt { e } = 0$ .0;   
for (it=0;it<MAXIT;it++) { Loop over iterations. for ( $\scriptstyle \dot { 1 } = 0$ ;i<npt;i++) { Set up the “design matrix” for the least-squares power wt[i]; fit. bb[i] $=$ power\*(fs[i] $^ +$ SIGN(e,ee[i])); Key idea here: Fit to $\mathtt { f n } ( x ) + e$ where the deviation is positive, to $\mathtt { f n } ( x ) { - e }$ where it is negative. Then $e$ is supposed to become an approximation to the equal-ripple deviation. for $( \mathrm { j } = 0$ ;j<mm+1;j++) { u[i][j] $=$ power; power $\ast =$ xs[i]; power $=$ -bb[i]; for $\scriptstyle ( { \mathrm { j } } = { \mathrm { m m } } + 1$ ;j<ncof;j++) { power $\ast =$ xs[i]; u[i][j]=power; } } SVD svd(u); Singular value decomposition. svd.solve(bb,coff); In especially singular or difficult cases, one might here edit the singular values, replacing small values by zero in w[0..ncof-1]. devmax=sum ${ = } 0$ .0; Ratfn rat(coff,mm+1,kk+1); for (j=0;j<npt;j++) { Tabulate the deviations and revise the weights. ee[j]=rat(xs[j])-fs[j]; wt[j] $=$ abs(ee[j]); Use weighting to emphasize most deviant points. sum $+ =$ wt[j]; if (wt[j] $>$ devmax) devmax=wt[j]; e=sum/npt; Update e to be the mean absolute deviation. if (devmax $< =$ dev) { Save only the best coefficient set found. ratbest $=$ rat; dev=devmax; } cout << " ratlsq iteratio $\ l _ { 1 } = \ l _ { 1 } \ l < <$ it; cout << " max error= " << setw(10) << devmax << endl;   
return ratbest;

![](images/afc88aa4350e4110cd68055693f1b27440f27ce97140186813409d549fcff3b0.jpg)  
Figure 5.13.1. Solid curves show deviations $r ( x )$ for five successive iterations of the routine ratlsq for an arbitrary test problem. The algorithm does not converge to exactly the minimax solution (shown as the dotted curve). But, after one iteration, the discrepancy is a small fraction of the last significant bit of accuracy.

minimax solution. The iterations do not converge in the order that the figure suggests. In fact, it is the second iteration that is best (has smallest maximum deviation). The routine ratlsq accordingly returns the best of its iterations, not necessarily the last one; there is no advantage in doing more than five iterations.

# CITED REFERENCES AND FURTHER READING:

Ralston, A. and Wilf, H.S. 1960, Mathematical Methods for Digital Computers (New York: Wiley), Chapter 13.[1]

# 5.14 Evaluation of Functions by Path Integration

In computer programming, the technique of choice is not necessarily the most efficient, or elegant, or fastest executing one. Instead, it may be the one that is quick to implement, general, and easy to check.

One sometimes needs only a few, or a few thousand, evaluations of a special function, perhaps a complex-valued function of a complex variable, that has many different parameters, or asymptotic regimes, or both. Use of the usual tricks (series, continued fractions, rational function approximations, recurrence relations, and so forth) may result in a patchwork program with tests and branches to different formulas. While such a program may be highly efficient in execution, it is often not the shortest way to the answer from a standing start.

A different technique of considerable generality is direct integration of a function’s defining differential equation — an ab initio integration for each desired function value — along a path in the complex plane if necessary. While this may at first seem like swatting a fly with a golden brick, it turns out that when you already have the brick, and the fly is asleep right under it, all you have to do is let it fall!

As a specific example, let us consider the complex hypergeometric function $_ 2 F _ { 1 } ( a , b , c ; z )$ , which is defined as the analytic continuation of the so-called hypergeometric series,

$$
{ \begin{array} { r l } & { _ { 2 } F _ { 1 } ( a , b , c ; z ) = 1 + { \frac { a b } { c } } { \frac { z } { 1 ! } } + { \frac { a ( a + 1 ) b ( b + 1 ) } { c ( c + 1 ) } } { \frac { z ^ { 2 } } { 2 ! } } + \cdots } \\ & { \qquad + { \frac { a ( a + 1 ) \ldots ( a + j - 1 ) b ( b + 1 ) \ldots ( b + j - 1 ) } { c ( c + 1 ) \ldots ( c + j - 1 ) } } { \frac { z ^ { j } } { j ! } } + \cdots } \end{array} }
$$

The series converges only within the unit circle $| z | < 1$ (see [1]), but one’s interest in the function is often not confined to this region.

The hypergeometric function ${ } _ { 2 } F _ { 1 }$ is a solution (in fact the solution that is regular at the origin) of the hypergeometric differential equation, which we can write as

$$
z ( 1 - z ) F ^ { \prime \prime } = a b F - [ c - ( a + b + 1 ) z ] F ^ { \prime }
$$

Here prime denotes $d / d z$ . One can see that the equation has regular singular points at $z = 0 , 1$ ; and $\infty$ . Since the desired solution is regular at $z = 0$ , the values 1 and $\infty$ will in general be branch points. If we want ${ } _ { 2 } F _ { 1 }$ to be a single-valued function, we must have a branch cut connecting these two points. A conventional position for this cut is along the positive real axis from 1 to $\infty$ , though we may wish to keep open the possibility of altering this choice for some applications.

Our golden brick consists of a collection of routines for the integration of sets of ordinary differential equations, which we will develop in detail later, in Chapter 17. For now, we need only a high-level, “black-box” routine that integrates such a set from initial conditions at one value of a (real) independent variable to final conditions at some other value of the independent variable, while automatically adjusting its internal stepsize to maintain some specified accuracy. That routine is called Odeint and, in one particular invocation, it calculates its individual steps with a sophisticated Bulirsch-Stoer technique.

Suppose that we know values for $F$ and its derivative $F ^ { \prime }$ at some value $z _ { 0 }$ , and that we want to find $F$ at some other point $z _ { 1 }$ in the complex plane. The straight-line path connecting these two points is parametrized by

$$
z ( s ) = z _ { 0 } + s ( z _ { 1 } - z _ { 0 } )
$$

with $s$ a real parameter. The differential equation (5.14.2) can now be written as a set of two first-order equations,

$$
\begin{array} { l } { { \displaystyle { \frac { d F } { d s } } = ( z _ { 1 } - z _ { 0 } ) F ^ { \prime } } } \\ { { \displaystyle { \frac { d F ^ { \prime } } { d s } } = ( z _ { 1 } - z _ { 0 } ) \left( \frac { a b F - [ c - ( a + b + 1 ) z ] F ^ { \prime } } { z ( 1 - z ) } \right) } } \end{array}
$$

![](images/b66d7c03d45cd3da204f14dbf4ac98e8d6d6c2342c955f65113728fc6ead49ee.jpg)  
Figure 5.14.1. Complex plane showing the singular points of the hypergeometric function, its branch cut, and some integration paths from the circle $| z | = 1 / 2$ (where the power series converges rapidly) to other points in the plane.

to be integrated from $s \ = \ 0$ to $s \ = \ 1$ . Here $F$ and $F ^ { \prime }$ are to be viewed as two independent complex variables. The fact that prime means $d / d z$ can be ignored; it will emerge as a consequence of the first equation in (5.14.4). Moreover, the real and imaginary parts of equation (5.14.4) define a set of four real differential equations, with independent variable $s$ . The complex arithmetic on the right-hand side can be viewed as mere shorthand for how the four components are to be coupled. It is precisely this point of view that gets passed to the routine Odeint, since it knows nothing of either complex functions or complex independent variables.

It remains only to decide where to start, and what path to take in the complex plane, to get to an arbitrary point $Z$ . This is where consideration of the function’s singularities, and the adopted branch cut, enter. Figure 5.14.1 shows the strategy that we adopt. For $| z | \le 1 / 2$ , the series in equation (5.14.1) will in general converge rapidly, and it makes sense to use it directly. Otherwise, we integrate along a straightline path from one of the starting points $( \pm 1 / 2 , 0 )$ or $( 0 , \pm 1 / 2 )$ . The former choices are natural for $0 < \mathrm { R e } ( z ) < 1$ and $\mathrm { R e } ( z ) < 0$ , respectively. The latter choices are used for $\mathrm { R e } ( z ) > 1$ , above and below the branch cut; the purpose of starting away from the real axis in these cases is to avoid passing too close to the singularity at $z = 1$ (see Figure 5.14.1). The location of the branch cut is defined by the fact that our adopted strategy never integrates across the real axis for $\mathrm { R e } ( z ) > 1$ .

An implementation of this algorithm is given in $\ S 6 . 1 3$ as the routine hypgeo.

A number of variants on the procedure described thus far are possible and easy to program. If successively called values of $Z$ are close together (with identical values of $a , b$ ; and $c$ ), then you can save the state vector $( F , F ^ { \prime } )$ and the corresponding value of $Z$ on each call, and use these as starting values for the next call. The incremental integration may then take only one or two steps. Avoid integrating across the branch cut unintentionally: The function value will be “correct,” but not the one you want.

Alternatively, you may wish to integrate to some position $Z$ by a dog-leg path that does cross the real axis $\mathrm { R e } ( z ) > 1$ , as a means of moving the branch cut. For example, in some cases you might want to integrate from $( 0 , 1 / 2 )$ to $( 3 / 2 , 1 / 2 )$ , and go from there to any point with $\mathrm { R e } ( z ) > 1$ — with either sign of $\mathrm { I m } z$ . (If you are, for example, finding roots of a function by an iterative method, you do not want the integration for nearby values to take different paths around a branch point. If it does, your root-finder will see discontinuous function values and will likely not converge correctly!)

In any case, be aware that a loss of numerical accuracy can result if you integrate through a region of large function value on your way to a final answer where the function value is small. (For the hypergeometric function, a particular case of this is when $a$ and $b$ are both large and positive, with $c$ and $x \gtrsim 1 .$ .) In such cases, you’ll need to find a better dog-leg path.

The general technique of evaluating a function by integrating its differential equation in the complex plane can also be applied to other special functions. For example, the complex Bessel function, Airy function, Coulomb wave function, and Weber function are all special cases of the confluent hypergeometric function, with a differential equation similar to the one used above (see, e.g., [1] $\ S 1 3 . 6$ , for a table of special cases). The confluent hypergeometric function has no singularities at finite $Z$ : That makes it easy to integrate. However, its essential singularity at infinity means that it can have, along some paths and for some parameters, highly oscillatory or exponentially decreasing behavior: That makes it hard to integrate. Some case-bycase judgment (or experimentation) is therefore required.

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands.[1]

# 6.0 Introduction

There is nothing particularly special about a special function, except that some person in authority or a textbook writer (not the same thing!) has decided to bestow the moniker. Special functions are sometimes called higher transcendental functions (higher than what?) or functions of mathematical physics (but they occur in other fields also) or functions that satisfy certain frequently occurring second-order differential equations (but not all special functions do). One might simply call them “useful functions” and let it go at that. The choice of which functions to include in this chapter is highly arbitrary.

Commercially available program libraries contain many special function routines that are intended for users who will have no idea what goes on inside them. Such state-of-the-art black boxes are often very messy things, full of branches to completely different methods depending on the value of the calling arguments. Black boxes have, or should have, careful control of accuracy, to some stated uniform precision in all regimes.

We will not be quite so fastidious in our examples, in part because we want to illustrate techniques from Chapter 5, and in part because we want you to understand what goes on in the routines presented. Some of our routines have an accuracy parameter that can be made as small as desired, while others (especially those involving polynomial fits) give only a certain stated accuracy, one that we believe is serviceable (usually, but not always, close to double precision). We do not certify that the routines are perfect black boxes. We do hope that, if you ever encounter trouble in a routine, you will be able to diagnose and correct the problem on the basis of the information that we have given.

In short, the special function routines of this chapter are meant to be used — we use them all the time — but we also want you to learn from their inner workings.

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands.

Andrews, G.E., Askey, R., and Roy, R. 1999, Special Functions (Cambridge, UK: Cambridge University Press).   
Thompson, W.J. 1997, Atlas for Computing Mathematical Functions (New York: Wiley-Interscience).   
Spanier, J., and Oldham, K.B. 1987, An Atlas of Functions (Washington: Hemisphere Pub. Corp.).   
Wolfram, S. 2003, The Mathematica Book, 5th ed. (Champaign, IL: Wolfram Media).   
Hart, J.F., et al. 1968, Computer Approximations (New York: Wiley).   
Hastings, C. 1955, Approximations for Digital Computers (Princeton: Princeton University Press).   
Luke, Y.L. 1975, Mathematical Functions and Their Approximations (New York: Academic Press).

# 6.1 Gamma Function, Beta Function, Factorials, Binomial Coefficients

The gamma function is defined by the integral

$$
\Gamma ( z ) = \int _ { 0 } ^ { \infty } t ^ { z - 1 } e ^ { - t } d t
$$

When the argument $Z$ is an integer, the gamma function is just the familiar factorial function, but offset by 1:

$$
n ! = \Gamma ( n + 1 )
$$

The gamma function satisfies the recurrence relation

$$
\Gamma ( z + 1 ) = z \Gamma ( z )
$$

If the function is known for arguments $z > 1$ or, more generally, in the half complex plane $\mathrm { R e } ( z ) > 1$ , it can be obtained for $z < 1$ or Re $( z ) < 1$ by the reflection formula

$$
\Gamma ( 1 - z ) = { \frac { \pi } { \Gamma ( z ) \sin ( \pi z ) } } = { \frac { \pi z } { \Gamma ( 1 + z ) \sin ( \pi z ) } }
$$

Notice that $\Gamma ( z )$ has a pole at $z = 0$ and at all negative integer values of $Z$ .

There are a variety of methods in use for calculating the function $\Gamma ( z )$ numerically, but none is quite as neat as the approximation derived by Lanczos [1]. This scheme is entirely specific to the gamma function, seemingly plucked from thin air. We will not attempt to derive the approximation, but only state the resulting formula: For certain choices of rational $\gamma$ and integer $N$ , and for certain coefficients $c _ { 1 } , c _ { 2 } , \dots , c _ { N }$ , the gamma function is given by

$$
\begin{array} { r l } { \displaystyle \Gamma ( z + 1 ) = ( z + \gamma + \frac { 1 } { 2 } ) ^ { z + \frac { 1 } { 2 } } e ^ { - ( z + \gamma + \frac { 1 } { 2 } ) } } & { } \\ { \displaystyle \times \sqrt { 2 \pi } \left[ c _ { 0 } + \frac { c _ { 1 } } { z + 1 } + \frac { c _ { 2 } } { z + 2 } + \cdots + \frac { c _ { N } } { z + N } + \epsilon \right] } & { ( z > 0 ) } \end{array}
$$

You can see that this is a sort of take-off on Stirling’s approximation, but with a series of corrections that take into account the first few poles in the left complex plane. The constant $c _ { 0 }$ is very nearly equal to 1. The error term is parametrized by