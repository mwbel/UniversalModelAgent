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

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0015_pages_0981-1050/auto/images/64d33d3d7479f08eaabb6def151d3605f5d09abe82b05894d077bc3b6b14cff4.jpg)  
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

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0015_pages_0981-1050/auto/images/eb945e005355474d7e977e4e335c20871dcfaa89e8b733497626084eaac49d1b.jpg)  
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

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0015_pages_0981-1050/auto/images/92437b479b5096016eb4edf5dcafb5ebafe636690992b09563bbbc27ebe986c7.jpg)  
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


<!-- chunk 0016: pages 1051-1120 -->
tional load and storage requirements, becomes the principal concern.

Because all the conditions on a boundary value problem must be satisfied “simultaneously,” these problems usually boil down, at least conceptually, to the solution of large numbers of simultaneous algebraic equations. When such equations are nonlinear, they are usually solved by linearization and iteration; so without much loss of generality we can view the problem as being the solution of special, large linear sets of equations.

As an example, one that we will refer to in $\ S 2 0 . 4 - \ S 2 0 . 6$ as our “model problem,” let us consider the solution of equation (20.0.3) by the finite difference method. We represent the function $u ( x , y )$ by its values at the discrete set of points

$$
\begin{array} { r l } { x _ { j } = x _ { 0 } + j \Delta , \qquad } & { { } j = 0 , 1 , . . . , J } \\ { y _ { l } = y _ { 0 } + l \Delta , \qquad } & { { } l = 0 , 1 , . . . , L } \end{array}
$$

where $\Delta$ is the grid spacing. From now on, we will write $u _ { j , l }$ for $u ( x _ { j } , y _ { l } )$ and $\rho _ { j , l }$ for $\rho ( x _ { j } , y _ { l } )$ . For (20.0.3) we substitute a finite difference representation (see Figure 20.0.2),

$$
\frac { u _ { j + 1 , l } - 2 u _ { j , l } + u _ { j - 1 , l } } { \Delta ^ { 2 } } + \frac { u _ { j , l + 1 } - 2 u _ { j , l } + u _ { j , l - 1 } } { \Delta ^ { 2 } } = \rho _ { j , l }
$$

or, equivalently,

$$
u _ { j + 1 , l } + u _ { j - 1 , l } + u _ { j , l + 1 } + u _ { j , l - 1 } - 4 u _ { j , l } = \Delta ^ { 2 } \rho _ { j , l }
$$

To write this system of linear equations in matrix form we need to make a vector out of $u$ . Let us number the two dimensions of grid points in a single onedimensional sequence by defining

$$
i \equiv j ( L + 1 ) + l \qquad \mathrm { f o r } \qquad j = 0 , 1 , . . . , J , \qquad l = 0 , 1 , . . . , L
$$

In other words, $i$ increases most rapidly along the columns representing $y$ values. Equation (20.0.6) now becomes

$$
u _ { i + L + 1 } + u _ { i - ( L + 1 ) } + u _ { i + 1 } + u _ { i - 1 } - 4 u _ { i } = \Delta ^ { 2 } \rho _ { i }
$$

This equation holds only at the interior points $j = 1 , 2 , . . . , J - 1 ; l = 1 , 2 , . . . , L - 1$ . The points where

$$
\begin{array} { r l } { j = 0 \quad } & { [ \mathrm { i . e . , } i = 0 , . . . , L ] } \\ { j = J \quad } & { [ \mathrm { i . e . , } i = J ( L + 1 ) , . . . , J ( L + 1 ) + L ] } \\ { l = 0 \quad } & { [ \mathrm { i . e . , } i = 0 , L + 1 , . . . , J ( L + 1 ) ] } \\ { l = L \quad } & { [ \mathrm { i . e . , } i = L , L + 1 + L , . . . , J ( L + 1 ) + L ] } \end{array}
$$

are boundary points where either $u$ or its derivative has been specified. If we pull all this “known” information over to the right-hand side of equation (20.0.8), then the equation takes the form

$$
\mathbf { A \cdot u } = \mathbf { b }
$$

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0016_pages_1051-1120/auto/images/a025d64aaeb79e881d2823f94de0756757e0b2df3557846713f480e5fd4ba07a.jpg)  
Figure 20.0.2. Finite difference representation of a second-order elliptic equation on a two-dimensional grid. The second derivatives at the point $A$ are evaluated using the points to which $A$ is shown connected. The second derivatives at point $B$ are evaluated using the connected points and also using “right-hand side” boundary information, shown schematically as $\otimes$ .

where $\mathbf { A }$ has the form shown in Figure 20.0.3. The matrix $\mathbf { A }$ is called “tridiagonal with fringes.” A general linear second-order elliptic equation

$$
\begin{array} { c } { \displaystyle { a ( x , y ) \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + b ( x , y ) \frac { \partial u } { \partial x } + c ( x , y ) \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } + d ( x , y ) \frac { \partial u } { \partial y } } } \\ { + \displaystyle { e ( x , y ) \frac { \partial ^ { 2 } u } { \partial x \partial y } + f ( x , y ) u = g ( x , y ) } } \end{array}
$$

will lead to a matrix of similar structure except that the nonzero entries will not be constants.

As a rough classification, there are three different approaches to the solution of equation (20.0.10), not all applicable in all cases: relaxation methods, “rapid” methods (e.g., Fourier methods), and direct matrix methods.

Relaxation methods make immediate use of the structure of the sparse matrix A. The matrix is split into two parts,

$$
\mathbf { A } = \mathbf { E } - \mathbf { F }
$$

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0016_pages_1051-1120/auto/images/e5d20b8df642de3f88c03e0192899576ba04c921bc8e458d62320face859ad69.jpg)  
Figure 20.0.3. Matrix structure derived from a second-order elliptic equation (here equation 20.0.6). All elements not shown are zero. The matrix has diagonal blocks that are themselves tridiagonal, and suband superdiagonal blocks that are diagonal. This form is called “tridiagonal with fringes.” A matrix this sparse would never be stored in its full form as shown here.

where $\mathbf { E }$ is easily invertible and $\mathbf { F }$ is the remainder. Then (20.0.10) becomes

$$
\mathbf { E } \cdot \mathbf { u } = \mathbf { F } \cdot \mathbf { u } + \mathbf { b }
$$

The relaxation method involves choosing an initial guess $\mathbf { u } ^ { ( 0 ) }$ and then solving successively for iterates $\mathbf { u } ^ { ( r ) }$ from

$$
\mathbf { E } \cdot \mathbf { u } ^ { ( r ) } = \mathbf { F } \cdot \mathbf { u } ^ { ( r - 1 ) } + \mathbf { b }
$$

Since $\mathbf { E }$ is chosen to be easily invertible, each iteration is fast. We will discuss relaxation methods in some detail in $\ S 2 0 . 5$ and $\ S 2 0 . 6$ .

So-called rapid methods [5] apply for only a rather special class of equations: those with constant coefficients, or, more generally, those that are separable in the chosen coordinates. In addition, the boundaries must coincide with coordinate lines. This special class of equations is met quite often in practice. We defer detailed discussion to $\ S 2 0 . 4$ . Note, however, that the multigrid relaxation methods discussed in $\ S 2 0 . 6$ can be faster than “rapid” methods.

Matrix methods attempt to solve the equation

$$
\mathbf { A \cdot x } = \mathbf { b }
$$

directly. The degree to which this is practical depends very strongly on the exact structure of the matrix A for the problem at hand, so our discussion can go no farther than a few remarks and references at this point.

Sparseness of the matrix must be the guiding force. Otherwise the matrix problem becomes prohibitively large. For example, a problem on a $1 0 0 0 \times 1 0 0 0$ spatial grid would involve $1 0 ^ { 6 }$ unknown $u _ { j , l }$ ’s, implying a $1 0 ^ { 6 } \times 1 0 ^ { 6 }$ matrix A containing $1 0 ^ { 1 2 }$ elements. A non-sparse $O ( N ^ { 3 } )$ solution method would require ${ \cal O } ( 1 0 ^ { 1 8 } )$ operations.

As we discussed at the end of $\ S 2 . 7$ , if A is symmetric and positive-definite (as it usually is in elliptic problems), the conjugate gradient algorithm can be used. In practice, rounding error often spoils the effectiveness of the conjugate gradient algorithm for solving finite difference equations. However, it is useful when incorporated in methods that first rewrite the equations so that A is transformed to a matrix $\mathbf { A } ^ { \prime }$ that is close to the identity matrix. The quadratic surface defined by the equations then has almost spherical contours, and the conjugate gradient algorithm works very well. In $\ S 2 . 7$ , in the routine linbcg, an analogous preconditioner was exploited for non-positive-definite problems with the more general biconjugate gradient method. There is a huge literature on the general subject of iterative methods to solve the sparse equations that typically arise in solving PDEs. Good places to start are [6-8].

Another class of matrix methods is the analyze-factorize-operate approach as described in $\ S 2 . 7$ .

Generally speaking, when you have the storage available to implement these methods — not nearly as much as the $1 0 ^ { 1 2 }$ above, but usually much more than is required by relaxation methods — then you should consider doing so. Only multigrid relaxation methods (-20.6) are competitive with the best matrix methods. For grids larger than, say, $1 0 0 0 \times 1 0 0 0$ , however, it is typically found that only relaxation methods, or “rapid” methods when they are applicable, are possible.

# 20.0.3 There Is More to Life than Finite Differencing

Besides finite differencing, there are other methods for solving PDEs. Most important are finite element, Monte Carlo, spectral, and variational methods. Unfortunately, we shall barely be able to do justice to finite differencing in this chapter, and we will give a brief introduction to spectral methods in $\ S 2 0 . 7$ . We shall not be able to discuss the other methods in this book. Finite element methods [9-11] are often preferred by practitioners in solid mechanics and structural engineering; these methods allow considerable freedom in putting computational elements where you want them, which is important when dealing with highly irregular geometries.

# CITED REFERENCES AND FURTHER READING:

Ames, W.F. 1992, Numerical Methods for Partial Differential Equations, 3rd ed. (New York: Academic Press).[1]   
Richtmyer, R.D., and Morton, K.W. 1967, Difference Methods for Initial Value Problems, 2nd ed. (New York: Wiley-Interscience); republished 1994 (Melbourne, FL: Krieger).[2]   
Roache, P.J. 1998, Computational Fluid Dynamics, revised edition (Albuquerque: Hermosa).[3]   
Thomas, J.W. 1995, Numerical Partial Differential Equations: Finite Difference Methods (New York: Springer).[4]   
Dorr, F.W. 1970, “The Direct Solution of the Discrete Poisson Equation on a Rectangle,” SIAM Review,vol.12,pp.248-263.[5]   
Saad, Y. 2003, Iterative Methods for Sparse Linear Systems, 2nd ed. (Philadelphia: S.I.A.M.).[6]   
Barrett, R., et al. 1993, Templates for the Solution of Linear Systems: Building Blocks for Iterative Methods (Philadelphia: S.I.A.M.).[7]   
Greenbaum, A. 1997, Iterative Methods for Solving Linear Systems (Philadelphia: S.I.A.M.).[8]   
Reddy, J.N. 2005, An Introduction to the Finite Element Method, 3rd ed. (New York: McGraw-Hill).[9]   
Smith, I.M., and Griffiths, V. 2004, Programming the Finite Element Method (New York: Wiley).[10]   
Zienkiewicz, O.C., Taylor, R.L., and Zhu, J.Z. 2005, The Finite Element Method: Its Basis and Fundamentals, 6th ed. (Oxford, UK: Elsevier Butterworth-Heinemann).[11]

# 20.1 Flux-Conservative Initial Value Problems

A large class of initial value (time-evolution) PDEs in one space dimension can be cast into the form of a flux-conservative equation,

$$
\frac { \partial \mathbf { u } } { \partial t } = - \frac { \partial \mathbf { F } ( \mathbf { u } ) } { \partial x }
$$

where $\mathbf { u }$ and $\mathbf { F }$ are vectors, and where (in some cases) $\mathbf { F }$ may depend not only on u but also on spatial derivatives of $\mathbf { u }$ . The vector $\mathbf { F }$ is called the conserved flux.

For example, the prototypical hyperbolic equation, the one-dimensional wave equation with constant velocity of propagation $v$ ,

$$
{ \frac { \partial ^ { 2 } u } { \partial t ^ { 2 } } } = v ^ { 2 } { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } }
$$

can be rewritten as a set of two first-order equations:

$$
\begin{array} { r } { \displaystyle { \frac { \partial r } { \partial t } } = v \displaystyle { \frac { \partial s } { \partial x } } } \\ { \displaystyle { \frac { \partial s } { \partial t } } = v \displaystyle { \frac { \partial r } { \partial x } } } \end{array}
$$

where

$$
\begin{array} { l } { r \equiv v \displaystyle \frac { \partial u } { \partial x } } \\ { s \equiv \displaystyle \frac { \partial u } { \partial t } } \end{array}
$$

In this case, $r$ and $s$ become the two components of $\mathbf { u }$ , and the flux is given by the linear matrix relation

$$
\mathbf { F } ( \mathbf { u } ) = \left( \begin{array} { l l } { 0 } & { - v } \\ { - v } & { 0 } \end{array} \right) \cdot \mathbf { u }
$$

(The physicist reader may recognize equations 20.1.3 as analogous to Maxwell’s equations for one-dimensional propagation of electromagnetic waves.)

We will consider, in this section, a prototypical example of the general fluxconservative equation (20.1.1), namely the equation for a scalar $u$ ,

$$
{ \frac { \partial u } { \partial t } } = - v { \frac { \partial u } { \partial x } }
$$

with $v$ a constant. As it happens, we already know analytically that the general solution of this equation is a wave propagating in the positive $x$ -direction,

$$
u = f ( x - v t )
$$

where $f$ is an arbitrary function. However, the numerical strategies that we develop will be equally applicable to the more general equations represented by (20.1.1). In some contexts, equation (20.1.6) is called an advective equation, because the quantity $u$ is transported by a “fluid flow” with a velocity $v$ .

How do we go about finite differencing equation (20.1.6) (or, analogously, 20.1.1)? The straightforward approach is to choose equally spaced points along both the $t$ - and $x$ -axes. Thus denote

$$
\begin{array} { c c } { { x _ { j } = x _ { 0 } + j \Delta x , } } & { { \qquad j = 0 , 1 , \ldots , J } } \\ { { } } & { { t _ { n } = t _ { 0 } + n \Delta t , } } & { { \qquad n = 0 , 1 , \ldots , N } } \end{array}
$$

Let $u _ { j } ^ { n }$ denote $u ( t _ { n } , x _ { j } )$ . We have several choices for representing the time derivative term. The obvious way is to set

$$
\left. \frac { \partial u } { \partial t } \right| _ { j , n } = \frac { u _ { j } ^ { n + 1 } - u _ { j } ^ { n } } { \Delta t } + O ( \Delta t )
$$

This is called forward Euler differencing (cf. equation 17.1.1). While forward Euler is only first-order accurate in $\Delta t$ , it has the advantage that one is able to calculate quantities at timestep $n + 1$ in terms of only quantities known at timestep $n$ . For the space derivative, we can use a second-order representation still using only quantities known at timestep $n$ :

$$
\left. \frac { \partial u } { \partial x } \right| _ { j , n } = \frac { u _ { j + 1 } ^ { n } - u _ { j - 1 } ^ { n } } { 2 \Delta x } + O ( \Delta x ^ { 2 } )
$$

The resulting finite difference approximation to equation (20.1.6) is called the FTCS representation (forward time centered space),

$$
\frac { u _ { j } ^ { n + 1 } - u _ { j } ^ { n } } { \Delta t } = - v \left( \frac { u _ { j + 1 } ^ { n } - u _ { j - 1 } ^ { n } } { 2 \Delta x } \right)
$$

which can easily be rearranged to be a formula for $u _ { j } ^ { n + 1 }$ in terms of the other quantities. The FTCS scheme is illustrated in Figure 20.1.1. It’s a fine example of an algorithm that is easy to derive, takes little storage, and executes quickly. Too bad it doesn’t work! (See below.)

The FTCS representation is an explicit scheme. This means that $u _ { j } ^ { n + 1 }$ for each $j$ can be calculated explicitly from the quantities that are already known. Later we shall meet implicit schemes, which require us to solve implicit equations coupling the $u _ { j } ^ { n + 1 }$ for various $j$ . (Explicit and implicit methods for ordinary differential equations were discussed in $\ S 1 7 . 5 .$ .) The FTCS algorithm is also an example of a single-level scheme, since only values at time level $n$ have to be stored to find values at time level $n + 1$ .

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0016_pages_1051-1120/auto/images/24e6010d707c02610e7616ed494e8d00d17e45ba3a6589b522122d3c2bc73457.jpg)  
Figure 20.1.1. Representation of the forward time centered space (FTCS) differencing scheme. In this and subsequent figures, the open circle is the new point at which the solution is desired; filled circles are known points whose function values are used in calculating the new point; the solid lines connect points that are used to calculate spatial derivatives; the dashed lines connect points that are used to calculate time derivatives. The FTCS scheme is generally unstable for hyperbolic problems and cannot usually be used.

# 20.1.1 von Neumann Stability Analysis

Unfortunately, equation (20.1.11) is of very limited usefulness. It is an unstable method, which can be used only (if at all) to study waves for a short fraction of one oscillation period. To find alternative methods with more general applicability, we introduce the von Neumann stability analysis.

The von Neumann analysis is local: Imagine that the coefficients of the difference equations are so slowly varying as to be considered constant in space and time. In that case, the independent solutions, or eigenmodes, of the difference equations are all of the form

$$
u _ { j } ^ { n } = \xi ^ { n } e ^ { i k j \Delta x }
$$

where $k$ is a real spatial wave number (which can have any value) and $\xi = \xi ( k )$ is a complex number that depends on $k$ . The key fact is that the time dependence of a single eigenmode is nothing more than successive integer powers of the complex number $\xi$ . Therefore, the difference equations are unstable (have exponentially growing modes) if $| \xi ( k ) | > 1$ for some $k$ . The number $\xi$ is called the amplification factor at a given wave number $k$ .

To find $\xi ( k )$ , simply substitute (20.1.12) back into (20.1.11). Divide by $\xi ^ { n }$ to get

$$
\xi ( k ) = 1 - i \frac { v \Delta t } { \Delta x } \sin { k \Delta x }
$$

whose modulus is $> 1$ for all $k$ ; so the FTCS scheme is unconditionally unstable.

If the velocity $v$ were a function of $t$ and $x$ , then we would write $v _ { j } ^ { n }$ in equation (20.1.11). In the von Neumann stability analysis we would still treat $v$ as a constant, the idea being that for $v$ slowly varying the analysis is local. In fact, even in the case of strictly constant $v$ , the von Neumann analysis does not rigorously treat the end effects at $j = 0$ and $j = N$ .

More generally, if the equation’s right-hand side were nonlinear in $u$ , then a von Neumann analysis would linearize by writing $\boldsymbol { u } = \boldsymbol { u } _ { 0 } + \delta \boldsymbol { u }$ , expanding to linear order in $\delta u$ . Assuming that the $u _ { 0 }$ quantities already satisfy the difference equation exactly, the analysis would look for an unstable eigenmode of $\delta u$ .

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0016_pages_1051-1120/auto/images/73cffc6e2d57cc90acedf0f20c6d5d0e124e5b50e90c1f7b9c56aa382a0beb1d.jpg)  
Figure 20.1.2. Representation of the Lax differencing scheme, as in the previous figure. The stability criterion for this scheme is the Courant condition.

Despite its lack of rigor, the von Neumann method generally gives valid answers and is much easier to apply than more careful methods. We accordingly adopt it exclusively. (See, for example, [1] for a discussion of other methods of stability analysis.)

# 20.1.2 Lax Method

The instability in the FTCS method can be cured by a simple change due to Lax. One replaces the term $u _ { j } ^ { n }$ in the time derivative term by its average (Figure 20.1.2):

$$
\begin{array} { r } { u _ { j } ^ { n }  \frac { 1 } { 2 } ( u _ { j + 1 } ^ { n } + u _ { j - 1 } ^ { n } ) } \end{array}
$$

This turns (20.1.11) into

$$
u _ { j } ^ { n + 1 } = \frac { 1 } { 2 } \left( u _ { j + 1 } ^ { n } + u _ { j - 1 } ^ { n } \right) - \frac { v \Delta t } { 2 \Delta x } \left( u _ { j + 1 } ^ { n } - u _ { j - 1 } ^ { n } \right)
$$

Substituting equation (20.1.12), we find for the amplification factor

$$
\xi = \cos { k \Delta x } - i \frac { v \Delta t } { \Delta x } \sin { k \Delta x }
$$

The stability condition $| \xi | ^ { 2 } \le 1$ leads to the requirement

$$
\frac { | v | \Delta t } { \Delta x } \leq 1
$$

This is the famous Courant-Friedrichs-Lewy stability criterion, often called simply the Courant condition. Intuitively, the stability condition can be understood as follows (Figure 20.1.3): The quantity $u _ { j } ^ { n + 1 }$ in equation (20.1.15) is computed from information at points $j - 1$ and $j + 1$ at time $n$ . In other words, $x _ { j - 1 }$ and $x _ { j + 1 }$ are the boundaries of the spatial region that is allowed to communicate information to $u _ { j } ^ { n + 1 }$ . Now recall that in the continuum wave equation, information actually propagates with a maximum velocity $v$ . If the point $u _ { j } ^ { n + 1 }$ is outside of the shaded region in Figure 20.1.3, then it requires information from points more distant than the differencing scheme allows. Lack of that information gives rise to an instability. Therefore, $\Delta t$ cannot be made too large.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0016_pages_1051-1120/auto/images/8843a9d2e79a45988f357d92bd6084ca2587c3b67dabb749bdd878b6b022453c.jpg)  
Figure 20.1.3. Courant condition for stability of a differencing scheme. The solution of a hyperbolic problem at a point depends on information within some domain of dependency to the past, shown here shaded. The differencing scheme (20.1.15) has its own domain of dependency determined by the choice of points on one time slice (shown as connected solid dots) whose values are used in determining a new point (shown connected by dashed lines). A differencing scheme is Courant stable if the differencing domain of dependency is larger than that of the PDEs, as in (a), and unstable if the relationship is the reverse, as in (b). For more complicated differencing schemes, the domain of dependency might not be determined simply by the outermost points.

The surprising result, that the simple replacement (20.1.14) stabilizes the FTCS scheme, is our first encounter with the fact that differencing PDEs is an art as much as a science. To see if we can demystify the art somewhat, let us compare the FTCS and Lax schemes by rewriting equation (20.1.15) so that it is in the form of equation (20.1.11) with a remainder term:

$$
\frac { u _ { j } ^ { n + 1 } - u _ { j } ^ { n } } { \Delta t } = - v \left( \frac { u _ { j + 1 } ^ { n } - u _ { j - 1 } ^ { n } } { 2 \Delta x } \right) + \frac { 1 } { 2 } \left( \frac { u _ { j + 1 } ^ { n } - 2 u _ { j } ^ { n } + u _ { j - 1 } ^ { n } } { \Delta t } \right)
$$

But this is exactly the FTCS representation of the equation

$$
\frac { \partial u } { \partial t } = - v \frac { \partial u } { \partial x } + \frac { ( \Delta x ) ^ { 2 } } { 2 \Delta t } \nabla ^ { 2 } u
$$

where $\nabla ^ { 2 } = \partial ^ { 2 } / \partial x ^ { 2 }$ in one dimension. We have, in effect, added a diffusion term to the equation, or, if you recall the form of the Navier-Stokes equation for viscous fluid flow, a dissipative term. The Lax scheme is thus said to have numerical dissipation, or numerical viscosity. We can see this also in the amplification factor. Unless $| v | \Delta t$ is exactly equal to $\Delta x , | \xi | < 1$ and the amplitude of the wave decreases spuriously.

Isn’t a spurious decrease as bad as a spurious increase? No. The scales that we hope to study accurately are those that encompass many grid points, so that they have $k \Delta x \ll 1$ . (The spatial wave number $k$ is defined by equation 20.1.12.) For these scales, the amplification factor can be seen to be very close to one, in both the stable and unstable schemes. The stable and unstable schemes are therefore about equally accurate. For the unstable scheme, however, short scales with $k \Delta x \sim 1$ , which we are not interested in, will blow up and swamp the interesting part of the solution. It is much better to have a stable scheme in which these short wavelengths die away innocuously. Both the stable and the unstable schemes are inaccurate for these short wavelengths, but the inaccuracy is of a tolerable character when the scheme is stable.

When the independent variable $\mathbf { u }$ is a vector, the von Neumann analysis is slightly more complicated. For example, we can consider equation (20.1.3), rewritten as

$$
{ \frac { \partial } { \partial t } } \left[ { \boldsymbol { r } } \right] = { \frac { \partial } { \partial x } } \left[ { \boldsymbol { v } } { \boldsymbol { s } } \right]
$$

The Lax method for this equation is

$$
\begin{array} { l c r } { { r _ { j } ^ { n + 1 } = \displaystyle \frac { 1 } { 2 } ( r _ { j + 1 } ^ { n } + r _ { j - 1 } ^ { n } ) + \displaystyle \frac { v \Delta t } { 2 \Delta x } ( s _ { j + 1 } ^ { n } - s _ { j - 1 } ^ { n } ) } } \\ { { s _ { j } ^ { n + 1 } = \displaystyle \frac { 1 } { 2 } ( s _ { j + 1 } ^ { n } + s _ { j - 1 } ^ { n } ) + \displaystyle \frac { v \Delta t } { 2 \Delta x } ( r _ { j + 1 } ^ { n } - r _ { j - 1 } ^ { n } ) } } \end{array}
$$

The von Neumann stability analysis now proceeds by assuming that the eigenmode is of the following (vector) form:

$$
{ \binom { r _ { j } ^ { n } } { s _ { j } ^ { n } } } = \xi ^ { n } e ^ { i k j \Delta x } { \binom { r ^ { 0 } } { s ^ { 0 } } }
$$

Here the vector on the right-hand side is a constant (both in space and in time) eigenvector, and $\xi$ is a complex number, as before. Substituting (20.1.22) into (20.1.21) and dividing by the power $\xi ^ { n }$ , gives the homogeneous vector equation

$$
\left[ \begin{array} { l l l } { ( \cos k \Delta x ) - \xi } & { i \frac { v \Delta t } { \Delta x } \sin k \Delta x } \\ { i \frac { v \Delta t } { \Delta x } \sin k \Delta x } & { ( \cos k \Delta x ) - \xi } \end{array} \right] \cdot \left[ \begin{array} { l } { r ^ { 0 } } \\ { s ^ { 0 } } \\ { s ^ { 0 } } \end{array} \right] = \left[ \begin{array} { l } { 0 } \\ { 0 } \\ { 0 } \end{array} \right]
$$

This admits a solution only if the determinant of the matrix on the left vanishes, a condition easily shown to yield the two roots $\xi$ ,

$$
\xi = \cos k \Delta x \pm i \frac { v \Delta t } { \Delta x } \sin k \Delta x
$$

The stability condition is that both roots satisfy $| \xi | \le 1$ . This again turns out to be simply the Courant condition (20.1.17).

# 20.1.3 Other Varieties of Error

Thus far we have been concerned with amplitude error, because of its intimate connection with the stability or instability of a differencing scheme. Other varieties of error are relevant when we shift our concern to accuracy, rather than stability.

Finite difference schemes for hyperbolic equations can exhibit dispersion, or phase errors. For example, equation (20.1.16) can be rewritten as

$$
\xi = e ^ { - i k \Delta x } + i \left( 1 - \frac { v \Delta t } { \Delta x } \right) \sin k \Delta x
$$

An arbitrary initial wave packet is a superposition of modes with different $k$ ’s. At each timestep the modes get multiplied by different phase factors (20.1.25), depending on their value of $k$ . If $\Delta t = \Delta x / v$ , then the exact solution for each mode of a wave packet $f ( x - v t )$ is obtained if each mode gets multiplied by $\exp ( - i k \Delta x )$ . For this value of $\Delta t$ , equation (20.1.25) shows that the finite difference solution gives the exact analytic result. However, if $v \Delta t / \Delta x$ is not exactly 1, the phase relations of the modes can become hopelessly garbled and the wave packet disperses. Note from (20.1.25) that the dispersion becomes large as soon as the wavelength becomes comparable to the grid spacing $\Delta x$ .

A third type of error is one associated with nonlinear hyperbolic equations and is therefore sometimes called nonlinear instability. For example, a piece of the Euler or Navier-Stokes equations for fluid flow looks like

$$
\frac { \partial v } { \partial t } = - v \frac { \partial v } { \partial x } + \ldots
$$

The nonlinear term in $v$ can cause a transfer of energy in Fourier space from long wavelengths to short wavelengths. This results in a wave profile steepening until a vertical profile or “shock” develops. Since the von Neumann analysis suggests that the stability can depend on $k \Delta x$ , a scheme that was stable for shallow profiles can become unstable for steep profiles. This kind of difficulty arises in a differencing scheme where the cascade in Fourier space is halted at the shortest wavelength representable on the grid, that is, at $k \sim 1 / \Delta x$ . If energy simply accumulates in these modes, it eventually swamps the energy in the long wavelength modes of interest.

Nonlinear instability and shock formation are thus somewhat controlled by numerical viscosity such as that discussed in connection with equation (20.1.18) above. In some fluid problems, however, shock formation is not merely an annoyance, but an actual physical behavior of the fluid whose detailed study is a goal. Then, numerical viscosity alone may not be adequate or sufficiently controllable. This is a complicated subject that we discuss further in the subsection on fluid dynamics, below.

For wave equations, propagation errors (amplitude or phase) are usually most worrisome. For advective equations, on the other hand, transport errors are usually of greater concern. In the Lax scheme, equation (20.1.15), a disturbance in the advected quantity $u$ at mesh point $j$ propagates to mesh points $j + 1$ and $j - 1$ at the next timestep. In reality, however, if the velocity $v$ is positive, then only mesh point $j + 1$ should be affected.

The simplest way to model the transport properties “better” is to use upwind differencing (see Figure 20.1.4):

$$
\frac { u _ { j } ^ { n + 1 } - u _ { j } ^ { n } } { \Delta t } = - v _ { j } ^ { n } \left\{ \frac { u _ { j } ^ { n } - u _ { j - 1 } ^ { n } } { \Delta x } , \quad v _ { j } ^ { n } > 0 \right.
$$

Note that this scheme is only first-order, not second-order, accurate in the calculation of the spatial derivatives. So how can it be “better”? The answer is one that annoys the mathematicians: The goal of numerical simulations is not always “accuracy” in a strictly mathematical sense, but sometimes “fidelity” to the underlying physics in a sense that is looser and more pragmatic. In such contexts, some kinds of error are much more tolerable than others. Upwind differencing generally adds fidelity to problems where the advected variables are liable to undergo sudden changes of state, e.g., as they pass through shocks or other discontinuities. You will have to be guided by the specific nature of your own problem.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0016_pages_1051-1120/auto/images/c77257863df2171b5b3c67848fc2f2b93f5b44ca553ecde8d342fb0dc984244f.jpg)  
Figure 20.1.4. Representation of upwind differencing schemes. The upper scheme is stable when the advection constant $v$ is negative, as shown; the lower scheme is stable when the advection constant $v$ is positive, also as shown. The Courant condition must, of course, also be satisfied.

For the differencing scheme (20.1.27), the amplification factor (for constant $v$ ) is

$$
\begin{array} { r } { \displaystyle \xi = 1 - \left| \frac { v \Delta t } { \Delta x } \right| \left( 1 - \cos k \Delta x \right) - i \frac { v \Delta t } { \Delta x } \sin k \Delta x } \\ { \displaystyle | \xi | ^ { 2 } = 1 - 2 \left| \frac { v \Delta t } { \Delta x } \right| \left( 1 - \left| \frac { v \Delta t } { \Delta x } \right| \right) \left( 1 - \cos k \Delta x \right) } \end{array}
$$

So the stability criterion $| \xi | ^ { 2 } \le 1$ is (again) simply the Courant condition (20.1.17).

There are various ways of improving the accuracy of first-order upwind differencing. In the continuum equation, material originally a distance $v \Delta t$ away arrives at a given point after a time interval $\Delta t$ . In the first-order method, the material always arrives from $\Delta x$ away. If $v \Delta t \ll \Delta x$ (to insure accuracy), this can cause a large error. One way of reducing this error is to interpolate $u$ between $j - 1$ and $j$ before transporting it. This gives effectively a second-order method. Various schemes for second-order upwind differencing are discussed and compared in [2,3].

# 20.1.4 Second-Order Accuracy in Time

When using a method that is first-order accurate in time but second-order accurate in space, one generally has to take $v \Delta t$ significantly smaller than $\Delta x$ to achieve the desired accuracy, say, by at least a factor of 5. Thus the Courant condition is not actually the limiting factor with such schemes in practice. However, there are schemes that are second-order accurate in both space and time, and these can often be pushed right to their stability limit, with correspondingly smaller computation times.

For example, the staggered leapfrog method for the conservation equation (20.1.1) is defined as follows (Figure 20.1.5): Using the values of $u ^ { n }$ at time $t ^ { n }$ , compute the fluxes $F _ { j } ^ { n }$ . Then compute new values $\boldsymbol u ^ { n + 1 }$ using the time-centered

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0016_pages_1051-1120/auto/images/b5864eb00906c50916eb05ca9a2572fd4cb4348424593d1662a412a174f7ba6a.jpg)  
Figure 20.1.5. Representation of the staggered leapfrog differencing scheme. Note that information from two previous time slices is used in obtaining the desired point. This scheme is second-order accurate in both space and time.

values of the fluxes:

$$
u _ { j } ^ { n + 1 } - u _ { j } ^ { n - 1 } = - \frac { \Delta t } { \Delta x } ( F _ { j + 1 } ^ { n } - F _ { j - 1 } ^ { n } )
$$

The name arises because the time levels in the time derivative term “leapfrog” over the time levels in the space derivative term. The method requires that $u ^ { n - 1 }$ and $u ^ { n }$ be stored to compute $u ^ { n + 1 }$ .

For our simple model equation (20.1.6), staggered leapfrog takes the form

$$
u _ { j } ^ { n + 1 } - u _ { j } ^ { n - 1 } = - \frac { v \Delta t } { \Delta x } ( u _ { j + 1 } ^ { n } - u _ { j - 1 } ^ { n } )
$$

The von Neumann stability analysis now gives a quadratic equation for $\xi$ , rather than a linear one, because of the occurrence of three consecutive powers of $\xi$ when the form (20.1.12) for an eigenmode is substituted into equation (20.1.31),

$$
\xi ^ { 2 } - 1 = - 2 i \xi \frac { v \Delta t } { \Delta x } \sin { k \Delta x }
$$

whose solution is

$$
\xi = - i \frac { v \Delta t } { \Delta x } \sin k \Delta x \pm \sqrt { 1 - \left( \frac { v \Delta t } { \Delta x } \sin k \Delta x \right) ^ { 2 } }
$$

Thus the Courant condition is again required for stability. In fact, $| \xi | ^ { 2 } = 1$ in equation (20.1.33) for any $v \Delta t \ \leq \ \Delta x$ . This is the great advantage of the staggered leapfrog method: There is no amplitude dissipation.

Staggered leapfrog differencing of equations like (20.1.20) is most transparent

if the variables are centered on appropriate half-mesh points:

$$
\begin{array} { l } { r _ { j + 1 / 2 } ^ { n } \equiv v \left. \frac { \partial u } { \partial x } \right| _ { j + 1 / 2 } ^ { n } = v \frac { u _ { j + 1 } ^ { n } - u _ { j } ^ { n } } { \Delta x } } \\ { s _ { j } ^ { n + 1 / 2 } \equiv \left. \frac { \partial u } { \partial t } \right| _ { j } ^ { n + 1 / 2 } = \frac { u _ { j } ^ { n + 1 } - u _ { j } ^ { n } } { \Delta t } } \end{array}
$$

This is purely a notational convenience: We can think of the mesh on which $r$ and $s$ are defined as being twice as fine as the mesh on which the original variable $u$ is defined. The leapfrog differencing of equation (20.1.20) is

$$
\frac { r _ { j + 1 / 2 } ^ { n + 1 } - r _ { j + 1 / 2 } ^ { n } } { \Delta t } = \frac { s _ { j + 1 } ^ { n + 1 / 2 } - s _ { j } ^ { n + 1 / 2 } } { \Delta x }
$$

If you substitute equation (20.1.22) in equation (20.1.35), you will find that once again the Courant condition is required for stability, and that there is no amplitude dissipation when it is satisfied.

If we substitute equation (20.1.34) in equation (20.1.35), we find that equation (20.1.35) is equivalent to

$$
\frac { u _ { j } ^ { n + 1 } - 2 u _ { j } ^ { n } + u _ { j } ^ { n - 1 } } { ( \Delta t ) ^ { 2 } } = v ^ { 2 } \frac { u _ { j + 1 } ^ { n } - 2 u _ { j } ^ { n } + u _ { j - 1 } ^ { n } } { ( \Delta x ) ^ { 2 } }
$$

This is just the “usual” second-order differencing of the wave equation (20.1.2). We see that it is a two-level scheme, requiring both $u ^ { n }$ and $u ^ { n - 1 }$ to obtain $u ^ { n + 1 }$ . In equation (20.1.35), this shows up as both $\scriptstyle { \bar { s } } ^ { n - 1 / 2 }$ and $r ^ { n }$ being needed to advance the solution.

For equations more complicated than our simple model equation, especially nonlinear equations, the leapfrog method usually becomes unstable when the gradients get large. The instability is related to the fact that odd and even mesh points are completely decoupled, like the black and white squares of a chess board, as shown in Figure 20.1.6. This mesh drifting instability is cured by coupling the two meshes through a numerical viscosity term, e.g., adding to the right side of (20.1.31) a small coefficient $( \ll ~ 1 )$ ) times $u _ { j + 1 } ^ { n } - 2 u _ { j } ^ { n } + u _ { j - 1 } ^ { n }$ . For more on stabilizing difference schemes by adding numerical dissipation, see, e.g., [4,5].

The two-step Lax-Wendroff scheme is a second-order in time method that avoids large numerical dissipation and mesh drifting. One defines intermediate values $u _ { j + 1 / 2 }$ at the half-timesteps $t _ { n + 1 / 2 }$ and the half-mesh points $x _ { j + 1 / 2 }$ . These are calculated by the Lax scheme:

$$
u _ { j + 1 / 2 } ^ { n + 1 / 2 } = \frac { 1 } { 2 } ( u _ { j + 1 } ^ { n } + u _ { j } ^ { n } ) - \frac { \Delta t } { \Delta x } ( F _ { j + 1 } ^ { n } - F _ { j } ^ { n } )
$$

Using these variables, one calculates the fluxe s F nC1=2 . Then the updated values unC1 a re calculated by the properly centered expression

$$
u _ { j } ^ { n + 1 } = u _ { j } ^ { n } - \frac { \Delta t } { \Delta x } \Big ( F _ { { j + 1 } / { 2 } } ^ { { n + 1 } / { 2 } } - F _ { { j - 1 } / { 2 } } ^ { { n + 1 } / { 2 } } \Big )
$$

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0016_pages_1051-1120/auto/images/7bc507af6d0b181d959db7cf114403d47e8a0eb1bffdce251cd280b6a990614e.jpg)  
Figure 20.1.6. Origin of mesh drift instabilities in a staggered leapfrog scheme. If the mesh points are imagined to lie in the squares of a chess board, then white squares couple to themselves and black to themselves, but there is no coupling between white and black. The fix is to introduce a small diffusive mesh-coupling piece.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0016_pages_1051-1120/auto/images/ea1c0d851688f00fb20e607e0fd02696ebf495f6cc04952159736fed75df5c6d.jpg)  
Figure 20.1.7. Representation of the two-step Lax-Wendroff differencing scheme. Two half-step points $( \otimes )$ are calculated by the Lax method. These, plus one of the original points, produce the new point via staggered leapfrog. Half-step points are used only temporarily and do not require storage allocation on the grid. This scheme is second-order accurate in both space and time.

The provisional values unC1=2j C1=2 are now discarded. (See Figure 20.1.7.)

Let us investigate the stability of this method for our model advective equation, where $F = v u$ . Substitute (20.1.37) in (20.1.38) to get

$$
\begin{array} { r l } & { u _ { j } ^ { n + 1 } = u _ { j } ^ { n } - \alpha \left[ \frac { 1 } { 2 } ( u _ { j + 1 } ^ { n } + u _ { j } ^ { n } ) - \frac { 1 } { 2 } \alpha ( u _ { j + 1 } ^ { n } - u _ { j } ^ { n } ) \right. } \\ & { \qquad \left. - \frac { 1 } { 2 } ( u _ { j } ^ { n } + u _ { j - 1 } ^ { n } ) + \frac { 1 } { 2 } \alpha ( u _ { j } ^ { n } - u _ { j - 1 } ^ { n } ) \right] } \end{array}
$$

where

$$
\alpha \equiv { \frac { v \Delta t } { \Delta x } }
$$

Then

$$
\xi = 1 - i \alpha \sin k \Delta x - \alpha ^ { 2 } ( 1 - \cos k \Delta x )
$$

so

$$
| \xi | ^ { 2 } = 1 - \alpha ^ { 2 } ( 1 - \alpha ^ { 2 } ) ( 1 - \cos { k \Delta x } ) ^ { 2 }
$$

The stability criterion $| \xi | ^ { 2 } \le 1$ is therefore $\alpha ^ { 2 } \leq 1$ ; or $v \Delta t \leq \Delta x$ as usual. Incidentally, you should not think that the Courant condition is the only stability requirement that ever turns up in PDEs. It keeps doing so in our model examples just because those examples are so simple in form. The method of analysis is, however, general.

Except when $\alpha = 1$ , $| \xi | ^ { 2 } < 1$ in (20.1.42), so some amplitude damping does occur. The effect is relatively small, however, for wavelengths large compared with the mesh size $\Delta x$ . If we expand (20.1.42) for small $k \Delta x$ , we find

$$
| \xi | ^ { 2 } = 1 - \alpha ^ { 2 } ( 1 - \alpha ^ { 2 } ) \frac { ( k \Delta x ) ^ { 4 } } { 4 } + \cdots
$$

The departure from unity occurs only at fourth order in $k$ . This should be contrasted with equation (20.1.16) for the Lax method, which shows that

$$
| \xi | ^ { 2 } = 1 - ( 1 - \alpha ^ { 2 } ) ( k \Delta x ) ^ { 2 } + \cdots
$$

for small $k \Delta x$ .

In summary, our recommendation for initial value problems that can be cast in flux-conservative form, and especially problems related to the wave equation, is to use the staggered leapfrog method when possible. We have personally had better success with it than with the two-step Lax-Wendroff method. For problems sensitive to transport errors, upwind differencing or one of its refinements should be considered.

# 20.1.5 Fluid Dynamics with Shocks

As we alluded to earlier, the treatment of fluid dynamics problems with shocks has become a very complicated and very sophisticated subject. All we can attempt to do here is to guide you to some starting points in the literature.

There are basically three important general methods for handling shocks. The oldest and simplest method, invented by von Neumann and Richtmyer, is to add artificial viscosity to the equations, modeling the way Nature uses real viscosity to smooth discontinuities. A good starting point for trying out this method is the differencing scheme in $\ S 1 2 . 1 1$ of [1]. This scheme is excellent for nearly all problems in one spatial dimension.

The second method combines a high-order differencing scheme that is accurate for smooth flows with a low-order scheme that is very dissipative and can smooth the shocks. Typically, various upwind differencing schemes are combined using weights chosen to zero the low-order scheme unless steep gradients are present, and also chosen to enforce various “monotonicity” constraints that prevent nonphysical oscillations from appearing in the numerical solution. References [2,3,6] are a good place to start with these methods.

The third, and potentially most powerful method, is Godunov’s approach. Here one gives up the simple linearization inherent in finite differencing based on Taylor series and includes the nonlinearity of the equations explicitly. There is an analytic solution for the evolution of two uniform states of a fluid separated by a discontinuity, the Riemann shock problem. Godunov’s idea was to approximate the fluid by a large number of cells of uniform states, and piece them together using the Riemann solution. There have been many generalizations of Godunov’s approach, which are now called high resolution shock capturing methods. The most influential such algorithm has probably been the PPM method [7]. General discussions of high resolution shock capturing methods and other modern algorithms are given in [8-10].

# CITED REFERENCES AND FURTHER READING:

Ames, W.F. 1992, Numerical Methods for Partial Differential Equations, 3rd ed. (New York: Academic Press), Chapter 4.   
Richtmyer, R.D., and Morton, K.W. 1967, Difference Methods for Initial Value Problems, 2nd ed. (New York: Wiley-Interscience); republished 1994 (Melbourne, FL: Krieger).[1]   
Centrella, J., and Wilson, J.R. 1984, “Planar Numerical Cosmology II: The Difference Equations and Numerical Tests,” Astrophysical Journal Supplement, vol. 54, pp. 229–249, Appendix B.[2]   
Hawley, J.F., Smarr, L.L., and Wilson, J.R. 1984, “A Numerical Study of Black Hole Accretion: II. Finite Differencing and Code Calibration,” Astrophysical Journal Supplement, vol. 55, pp. 211–246, $\ S 2 0$ .[3]   
Kreiss, H.-O., and Busenhart, H. U. 2001, Time-Dependent Partial Differential Equations and Their Numerical Solution (Basel: Birkhäuser),pp. 49.[4]   
Gustafsson, B., Kreiss, H.-O., and Oliger, J. 1995, Time Dependent Problems and Difference Methods (New York: Wiley), Ch. 2.[5]   
Harten, A., Lax, P.D., and Van Leer, B. 1983, “On Upstream Differencing and Godunov-Type Schemes for Hyperbolic Conservation Laws,” SIAM Review, vol. 25, pp. 36–61.[6]   
Woodward, P., and Colella, P. 1984, “The Piecewise Parabolic Method (PPM) for Gasdynamical Simulations,” Journal of Computational Physics, vol. 54, pp. 174–201; op. cit., vol. 54, pp. 115–173.[7]   
LeVeque, R.J. 2002, Finite Volume Methods for Hyperbolic Problems (Cambridge, UK: Cambridge University Press).[8]   
LeVeque, R.J. 1992, Numerical Methods for Conservation Laws, 2nd ed. (Basel: Birkhäuser).[9]   
Toro, E.F. 1997, Riemann Solvers and Numerical Methods for Fluid Dynamics (Berlin: Springer).[10]

# 20.2 Diffusive Initial Value Problems

Recall the model parabolic equation, the diffusion equation in one space dimension,

$$
\frac { \partial u } { \partial t } = \frac { \partial } { \partial x } \left( D \frac { \partial u } { \partial x } \right)
$$

where $D$ is the diffusion coefficient. Actually, this equation is a flux-conservative equation of the form considered in the previous section, with

$$
F = - D { \frac { \partial u } { \partial x } }
$$

the flux in the $x$ -direction. We will assume $D ~ \geq ~ 0$ , otherwise equation (20.2.1) has physically unstable solutions: A small disturbance evolves to become more and more concentrated instead of dispersing. (Don’t make the mistake of trying to find a stable differencing scheme for a problem whose underlying PDEs are themselves unstable!)

Even though (20.2.1) is of the form already considered, it is useful to consider it as a model in its own right. The particular form of flux (20.2.2), and its direct generalizations, occur quite frequently in practice. Moreover, we have already seen that numerical viscosity and artificial viscosity can introduce diffusive pieces like the right-hand side of (20.2.1) in many other situations.

Consider first the case when $D$ is a constant. Then the equation

$$
{ \frac { \partial u } { \partial t } } = D { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } }
$$

can be differenced in the obvious way:

$$
\frac { u _ { j } ^ { n + 1 } - u _ { j } ^ { n } } { \Delta t } = D \left[ \frac { u _ { j + 1 } ^ { n } - 2 u _ { j } ^ { n } + u _ { j - 1 } ^ { n } } { ( \Delta x ) ^ { 2 } } \right]
$$

This is the FTCS scheme again, except that it is a second derivative that has been differenced on the right-hand side. But this makes a world of difference! The FTCS scheme was unstable for the hyperbolic equation; however, a quick calculation shows that the amplification factor for equation (20.2.4) is

$$
\xi = 1 - \frac { 4 D \Delta t } { ( \Delta x ) ^ { 2 } } \sin ^ { 2 } \left( \frac { k \Delta x } { 2 } \right)
$$

The requirement $| \xi | \le 1$ leads to the stability criterion

$$
\frac { 2 D \Delta t } { ( \Delta x ) ^ { 2 } } \leq 1
$$

The physical interpretation of the restriction (20.2.6) is that the maximum allowed timestep is, up to a numerical factor, the diffusion time across a cell of width $\Delta x$ .

More generally, the diffusion time $\tau$ across a spatial scale of size $\lambda$ is of order

$$
\tau \sim { \frac { \lambda ^ { 2 } } { D } }
$$

Usually we are interested in modeling accurately the evolution of features with spatial scales $\lambda \gg \Delta x$ . If we are limited to timesteps satisfying (20.2.6), we will need to evolve through of order $\lambda ^ { 2 } / ( \Delta x ) ^ { 2 }$ steps before things start to happen on the scale of interest. This number of steps is usually prohibitive. We must therefore find a stable way of taking timesteps comparable to, or perhaps — for accuracy — somewhat smaller than, the time scale of (20.2.7).

This goal poses an immediate “philosophical” question. Obviously the large timesteps that we propose to take are going to be woefully inaccurate for the small scales that we have decided not to be interested in. We want those scales to do something stable, “innocuous,” and perhaps not too physically unreasonable. We want to build this innocuous behavior into our differencing scheme. What should it be?

There are two different answers, each of which has its pros and cons. The first answer is to seek a differencing scheme that drives small-scale features to their equilibrium forms, e.g., satisfying equation (20.2.3) with the left-hand side set to zero. This answer generally makes the best physical sense; but, as we will see, it leads to a differencing scheme (“fully implicit”) that is only first-order accurate in time for the scales that we are interested in. The second answer is to let small-scale features maintain their initial amplitudes, so that the evolution of the larger-scale features of interest takes place superposed with a kind of “frozen in” (though fluctuating) background of small-scale stuff. This answer gives a differencing scheme (Crank-Nicolson) that is second-order accurate in time. Toward the end of an evolution calculation, however, one might want to switch over to some steps of the other kind, to drive the small-scale stuff into equilibrium. Let us now see where these distinct differencing schemes come from.

Consider the following differencing of (20.2.3):

$$
\frac { u _ { j } ^ { n + 1 } - u _ { j } ^ { n } } { \Delta t } = D \left[ \frac { u _ { j + 1 } ^ { n + 1 } - 2 u _ { j } ^ { n + 1 } + u _ { j - 1 } ^ { n + 1 } } { ( \Delta x ) ^ { 2 } } \right]
$$

This is exactly like the FTCS scheme (20.2.4), except that the spatial derivatives on the right-hand side are evaluated at timestep $n + 1$ . Schemes with this character are called fully implicit or backward time, by contrast with FTCS (which is called fully explicit). To solve equation (20.2.8), one has to solve a set of simultaneous linear equations at each timestep for the $u _ { j } ^ { n + 1 }$ . Fortunately, this is a simple problem because the system is tridiagonal: Just group the terms in equation (20.2.8) appropriately:

$$
- \alpha u _ { j - 1 } ^ { n + 1 } + ( 1 + 2 \alpha ) u _ { j } ^ { n + 1 } - \alpha u _ { j + 1 } ^ { n + 1 } = u _ { j } ^ { n } , \qquad j = 1 , 2 . . . J - 1
$$

where

$$
\alpha \equiv \frac { D \Delta t } { ( \Delta x ) ^ { 2 } }
$$

Supplemented by Dirichlet or Neumann boundary conditions at $j = 0$ and $j = J$ , equation (20.2.9) is clearly a tridiagonal system, which can easily be solved at each timestep by the method of $\ S 2 . 4$ .

What is the behavior of (20.2.8) for very large timesteps? The answer is seen most clearly in (20.2.9), in the limit $\alpha \to \infty$ ( $\Delta t \to \infty$ ). Dividing by $\alpha$ , we see that the difference equations are just the finite difference form of the equilibrium equation

$$
{ \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } = 0
$$

What about stability? The amplification factor for equation (20.2.8) is

$$
\xi = \frac { 1 } { 1 + 4 \alpha \sin ^ { 2 } \left( \frac { k \Delta x } { 2 } \right) }
$$

Clearly $| \xi | < 1$ for any stepsize $\Delta t$ . The scheme is unconditionally stable. The details of the small-scale evolution from the initial conditions are obviously inaccurate for large $\Delta t$ . But, as advertised, the correct equilibrium solution is obtained. This is the characteristic feature of implicit methods.

Here, on the other hand, is how one gets to the second of our above philosophical answers, combining the stability of an implicit method with the accuracy of a method that is second order in both space and time. Simply form the average of the explicit and implicit FTCS schemes:

$$
\frac { u _ { j } ^ { n + 1 } - u _ { j } ^ { n } } { \Delta t } = \frac { D } { 2 } \left[ \frac { ( u _ { j + 1 } ^ { n + 1 } - 2 u _ { j } ^ { n + 1 } + u _ { j - 1 } ^ { n + 1 } ) + ( u _ { j + 1 } ^ { n } - 2 u _ { j } ^ { n } + u _ { j - 1 } ^ { n } ) } { ( \Delta x ) ^ { 2 } } \right]
$$

Here both the left- and right-hand sides are centered at timestep $\begin{array} { r } { n + \frac { 1 } { 2 } } \end{array}$ , so the method is second-order accurate in time as claimed. The amplification factor is

$$
\xi = \frac { 1 - 2 \alpha \sin ^ { 2 } \left( \frac { k \Delta x } { 2 } \right) } { 1 + 2 \alpha \sin ^ { 2 } \left( \frac { k \Delta x } { 2 } \right) }
$$

so the method is stable for any size $\Delta t$ . This scheme is called the Crank-Nicolson scheme and is our recommended method for any simple diffusion problem (perhaps supplemented by a few fully implicit steps at the end). (See Figure 20.2.1.)

Now turn to some generalizations of the simple diffusion equation (20.2.3). Suppose first that the diffusion coefficient $D$ is not constant, say $D = D ( x )$ . We can adopt either of two strategies. First, we can make an analytic change of variable

$$
y = \int \frac { d x } { D ( x ) }
$$

Then

$$
\frac { \partial u } { \partial t } = \frac { \partial } { \partial x } D ( x ) \frac { \partial u } { \partial x }
$$

becomes

$$
\frac { \partial u } { \partial t } = \frac { 1 } { D ( y ) } \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } }
$$

and we evaluate $D$ at the appropriate $y _ { j }$ . Heuristically, the stability criterion (20.2.6) in an explicit scheme becomes

$$
\Delta t \leq \operatorname* { m i n } _ { j } \left[ \frac { ( \Delta y ) ^ { 2 } } { 2 D _ { j } ^ { - 1 } } \right]
$$

Note that constant spacing $\Delta y$ in $y$ does not imply constant spacing in $x$ .

An alternative method that does not require analytically tractable forms for $D$ is simply to difference equation (20.2.16) as it stands, centering everything appropriately. Thus the FTCS method becomes

$$
\frac { u _ { j } ^ { n + 1 } - u _ { j } ^ { n } } { \Delta t } = \frac { D _ { j + 1 / 2 } ( u _ { j + 1 } ^ { n } - u _ { j } ^ { n } ) - D _ { j - 1 / 2 } ( u _ { j } ^ { n } - u _ { j - 1 } ^ { n } ) } { ( \Delta x ) ^ { 2 } }
$$

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0016_pages_1051-1120/auto/images/c1832ed4e25220cadfa3b9c5337619cee8a088fb28f7506cb1b38834f39b9b9a.jpg)  
Figure 20.2.1. Three differencing schemes for diffusive problems (shown as in Figure 20.1.2). (a) Forward time centered space is first-order accurate but stable only for sufficiently small timesteps. (b) Fully implicit is stable for arbitrarily large timesteps but is still only first-order accurate. (c) Crank-Nicolson is second-order accurate and is usually stable for large timesteps.

where

$$
D _ { j + 1 / 2 } \equiv D ( x _ { j + 1 / 2 } )
$$

and the heuristic stability criterion is

$$
\Delta t \leq \operatorname* { m i n } _ { j } \left[ \frac { ( \Delta x ) ^ { 2 } } { 2 D _ { j + 1 / 2 } } \right]
$$

The Crank-Nicolson method can be generalized similarly.

The second complication one can consider is a nonlinear diffusion problem, for example where $D = D ( u )$ . Explicit schemes can be generalized in the obvious way. For example, in equation (20.2.19) write

$$
\begin{array} { r } { D _ { j + 1 / 2 } = \frac { 1 } { 2 } \left[ D ( u _ { j + 1 } ^ { n } ) + D ( u _ { j } ^ { n } ) \right] } \end{array}
$$

Implicit schemes are not as easy. The replacement (20.2.22) with $n  n + 1$ leaves us with a nasty set of coupled nonlinear equations to solve at each timestep. Often there is an easier way: If the form of $D ( u )$ allows us to integrate

$$
d z = D ( u ) d u
$$

analytically for $z ( u )$ , then the right-hand side of (20.2.1) becomes $\partial ^ { 2 } z / \partial x ^ { 2 }$ , which

we difference implicitly as

$$
\frac { z _ { j + 1 } ^ { n + 1 } - 2 z _ { j } ^ { n + 1 } + z _ { j - 1 } ^ { n + 1 } } { ( \Delta x ) ^ { 2 } }
$$

Now linearize each term on the right-hand side of equation (20.2.24), for example

$$
\begin{array} { r } { z _ { j } ^ { n + 1 } \equiv z ( u _ { j } ^ { n + 1 } ) = z ( u _ { j } ^ { n } ) + ( u _ { j } ^ { n + 1 } - u _ { j } ^ { n } ) \left. \frac { \partial z } { \partial u } \right| _ { j , n } } \\ { = z ( u _ { j } ^ { n } ) + ( u _ { j } ^ { n + 1 } - u _ { j } ^ { n } ) D ( u _ { j } ^ { n } ) } \end{array}
$$

This reduces the problem to tridiagonal form again and in practice usually retains the stability advantages of fully implicit differencing.

# 20.2.1 Schrödinger Equation

Sometimes the physical problem being solved imposes constraints on the differencing scheme that we have not yet taken into account. For example, consider the time-dependent Schrodinger equation of quantum mechanics. This is basically a ¨ parabolic equation for the evolution of a complex quantity $\psi$ . For the scattering of a wavepacket by a one-dimensional potential $V ( x )$ , the equation has the form

$$
i \frac { \partial \psi } { \partial t } = - \frac { \partial ^ { 2 } \psi } { \partial x ^ { 2 } } + V ( x ) \psi
$$

(Here we have chosen units so that Planck’s constant $\hbar = 1$ and the particle mass $m = 1 / 2 .$ ) One is given the initial wavepacket, $\psi ( x , t = 0 )$ , together with boundary conditions that $\psi \ \to \ 0$ at $x  \pm \infty$ . Suppose we content ourselves with firstorder accuracy in time but want to use an implicit scheme, for stability. A slight generalization of (20.2.8) leads to

$$
i \left[ \frac { \psi _ { j } ^ { n + 1 } - \psi _ { j } ^ { n } } { \Delta t } \right] = - \left[ \frac { \psi _ { j + 1 } ^ { n + 1 } - 2 \psi _ { j } ^ { n + 1 } + \psi _ { j - 1 } ^ { n + 1 } } { ( \Delta x ) ^ { 2 } } \right] + V _ { j } \psi _ { j } ^ { n + 1 }
$$

for which

$$
\xi = \frac { 1 } { 1 + i \left[ \cfrac { 4 \Delta t } { ( \Delta x ) ^ { 2 } } \sin ^ { 2 } \left( \cfrac { k \Delta x } { 2 } \right) + V _ { j } \Delta t \right] }
$$

This is unconditionally stable but unfortunately is not unitary. The underlying physical problem requires that the total probability of finding the particle somewhere remains unity. This is represented formally by the modulus-square norm of $\psi$ remaining unity:

$$
\int _ { - \infty } ^ { \infty } | \psi | ^ { 2 } d x = 1
$$

The initial wave function $\psi ( x , 0 )$ is normalized to satisfy (20.2.29). The Schrodinger ¨ equation (20.2.26) then guarantees that this condition is satisfied at all later times.

Let us write equation (20.2.26) in the form

$$
i \frac { \partial \psi } { \partial t } = H \psi
$$

where the operator $H$ is

$$
H = - \frac { \partial ^ { 2 } } { \partial x ^ { 2 } } + V ( x )
$$

The formal solution of equation (20.2.30) is

$$
\psi ( x , t ) = e ^ { - i H t } \psi ( x , 0 )
$$

where the exponential of the operator is defined by its power series expansion.

The unstable explicit FTCS scheme approximates (20.2.32) as

$$
\psi _ { j } ^ { n + 1 } = ( 1 - i H \Delta t ) \psi _ { j } ^ { n }
$$

where $H$ is represented by a centered finite difference approximation in $x$ . The stable implicit scheme (20.2.27) is, by contrast,

$$
\psi _ { j } ^ { n + 1 } = ( 1 + i H \Delta t ) ^ { - 1 } \psi _ { j } ^ { n }
$$

These are both first-order accurate in time, as can be seen by expanding equation (20.2.32). However, neither operator in (20.2.33) or (20.2.34) is unitary.

The correct way to difference Schrodinger’s equation ¨ [1,2] is to use Cayley’s form for the finite difference representation of $e ^ { - i H t }$ , which is second-order accurate and unitary:

$$
e ^ { - i H t } \simeq \frac { 1 - \frac { 1 } { 2 } i H \Delta t } { 1 + \frac { 1 } { 2 } i H \Delta t }
$$

In other words,

$$
\begin{array} { r } { \left( 1 + \frac { 1 } { 2 } i H \Delta t \right) \psi _ { j } ^ { n + 1 } = \left( 1 - \frac { 1 } { 2 } i H \Delta t \right) \psi _ { j } ^ { n } } \end{array}
$$

On replacing $H$ by its finite difference approximation in $x$ , we have a complex tridiagonal system to solve. The method is stable, unitary, and second-order accurate in space and time. In fact, it is simply the Crank-Nicolson method once again!

# CITED REFERENCES AND FURTHER READING:

Thomas, J.W. 1995, Numerical Partial Differential Equations: Finite Difference Methods (New York: Springer).   
Ames, W.F. 1992, Numerical Methods for Partial Differential Equations, 3rd ed. (New York: Academic Press), Chapter 2.   
Goldberg, A., Schey, H.M., and Schwartz, J.L. 1967, “Computer-Generated Motion Pictures of One-Dimensional Quantum-Mechanical Transmission and Reflection Phenomena,” American Journal of Physics, vol.35,pp.177-186.[1]   
Galbraith, I., Ching, Y.S., and Abraham, E. 1984, “Two-Dimensional Time-Dependent Quantum-Mechanical Scattering Event,” American Journal of Physics, vol. 52, pp. 60–68.[2]

# 20.3 Initial Value Problems in Multidimensions

The methods described in $\ S 2 0 . 1$ and $\ S 2 0 . 2$ for problems in $1 + 1$ dimension (one space and one time dimension) can easily be generalized to $N + 1$ dimensions. However, the computing power necessary to solve the resulting equations grows extremely rapidly as the number of dimensions increases. If you have solved a one-dimensional problem with 100 spatial grid points, solving the two-dimensional version with $1 0 0 \times 1 0 0$ mesh points requires at least 100 times as much computing. You generally have to be content with very modest spatial resolution in multidimensional problems.

Indulge us in offering a bit of advice about the development and testing of multidimensional PDE codes: You should always first run your programs on very small grids, e.g., $8 \times 8$ , even though the resulting accuracy is so poor as to be useless. When your program is all debugged and demonstrably stable, then you can increase the grid size to a reasonable one and start looking at the results. We have actually heard someone protest, “my program would be unstable for a crude grid, but I am sure the instability will go away on a larger grid.” That is nonsense of a most pernicious sort, evidencing total confusion between accuracy and stability. In fact, new instabilities sometimes do show up on larger grids; but old instabilities never (in our experience) just go away.

Forced to live with modest grid sizes, some people recommend going to higherorder methods in an attempt to improve accuracy. This can be very dangerous. Unless the solution you are looking for is known to be smooth, and the high-order method you are using is known to be extremely stable, we do not recommend anything higher than second-order in time (for sets of first-order equations). For spatial differencing, we recommend the order of the underlying PDEs, perhaps allowing second-order spatial differencing for first-order-in-space PDEs. When you increase the order of a differencing method to greater than the order of the original PDEs, you introduce spurious solutions to the difference equations. This does not create a problem if they all happen to decay exponentially; otherwise you are going to see all hell break loose!

# 20.3.1 Lax Method for a Flux-Conservative Equation

As an example, we show now how to generalize the Lax method (20.1.15) to two dimensions for the conservation equation

$$
{ \frac { \partial u } { \partial t } } = - \nabla \cdot \mathbf { F } = - \left( { \frac { \partial F _ { x } } { \partial x } } + { \frac { \partial F _ { y } } { \partial y } } \right)
$$

Use a spatial grid with

$$
\begin{array} { r } { x _ { j } = x _ { 0 } + j \Delta } \\ { y _ { l } = y _ { 0 } + l \Delta } \end{array}
$$

We have chosen $\Delta x = \Delta y \equiv \Delta$ for simplicity. Then the Lax scheme is

$$
\begin{array} { c } { { u _ { j , l } ^ { n + 1 } = \displaystyle \frac { 1 } { 4 } ( u _ { j + 1 , l } ^ { n } + u _ { j - 1 , l } ^ { n } + u _ { j , l + 1 } ^ { n } + u _ { j , l - 1 } ^ { n } ) } } \\ { { - \displaystyle \frac { \Delta t } { 2 \Delta } ( F _ { j + 1 , l } ^ { n } - F _ { j - 1 , l } ^ { n } + F _ { j , l + 1 } ^ { n } - F _ { j , l - 1 } ^ { n } ) } } \end{array}
$$

Note that as an abbreviated notation $F _ { j + 1 }$ and $F _ { j - 1 }$ refer to $F _ { x }$ , while $F _ { l + 1 }$ and $F _ { l - 1 }$ refer to $F _ { y }$ .

Let us carry out a stability analysis for the model advective equation (analog of 20.1.6) with

$$
F _ { x } = v _ { x } u , \qquad F _ { y } = v _ { y } u
$$

This requires an eigenmode with two dimensions in space, though still only a simple dependence on powers of $\xi$ in time:

$$
u _ { j , l } ^ { n } = \xi ^ { n } e ^ { i k _ { x } j \Delta } e ^ { i k _ { y } l \Delta }
$$

Substituting in equation (20.3.3), we find

$$
\begin{array} { r } { \xi = \frac 1 2 ( \cos k _ { x } \Delta + \cos k _ { y } \Delta ) - i \alpha _ { x } \sin k _ { x } \Delta - i \alpha _ { y } \sin k _ { y } \Delta } \end{array}
$$

where

$$
\alpha _ { x } = \frac { v _ { x } \Delta t } { \Delta } , \qquad \alpha _ { y } = \frac { v _ { y } \Delta t } { \Delta }
$$

The expression for $| \xi | ^ { 2 }$ can be manipulated into the form

$$
\begin{array} { c } { { | \xi | ^ { 2 } = 1 - ( \sin ^ { 2 } k _ { x } \Delta + \sin ^ { 2 } k _ { y } \Delta ) \bigg [ \frac { 1 } { 2 } - ( \alpha _ { x } ^ { 2 } + \alpha _ { y } ^ { 2 } ) \bigg ] } } \\ { { - \frac { 1 } { 4 } ( \cos k _ { x } \Delta - \cos k _ { y } \Delta ) ^ { 2 } - ( \alpha _ { y } \sin k _ { x } \Delta - \alpha _ { x } \sin k _ { y } \Delta ) ^ { 2 } } } \end{array}
$$

The last two terms are negative, and so the stability requirement $| \xi | ^ { 2 } \le 1$ becomes

$$
\begin{array} { r } { \frac { 1 } { 2 } - ( \alpha _ { x } ^ { 2 } + \alpha _ { y } ^ { 2 } ) \ge 0 } \end{array}
$$

or

$$
\Delta t \leq \frac { \Delta } { \sqrt { 2 } ( v _ { x } ^ { 2 } + v _ { y } ^ { 2 } ) ^ { 1 / 2 } }
$$

This is an example of the general result for the $N$ -dimensional Courant condition: If $| v |$ is the maximum propagation velocity in the problem, then

$$
\Delta t \leq \frac { \Delta } { \sqrt { N } | v | }
$$

is the Courant condition.

# 20.3.2 Diffusion Equation in Multidimensions

Let us consider the two-dimensional diffusion equation,

$$
\frac { \partial u } { \partial t } = D \left( \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } \right)
$$

An explicit method, such as FTCS, can be generalized from the one-dimensional case in the obvious way. However, we have seen that diffusive problems are usually best treated implicitly. Suppose we try to implement the Crank-Nicolson scheme in two dimensions. This would give us

$$
\begin{array} { r } { u _ { j , l } ^ { n + 1 } = u _ { j , l } ^ { n } + \frac { 1 } { 2 } \alpha \left( \delta _ { x } ^ { 2 } u _ { j , l } ^ { n + 1 } + \delta _ { x } ^ { 2 } u _ { j , l } ^ { n } + \delta _ { y } ^ { 2 } u _ { j , l } ^ { n + 1 } + \delta _ { y } ^ { 2 } u _ { j , l } ^ { n } \right) } \end{array}
$$

Here

$$
\alpha \equiv { \frac { D \Delta t } { \Delta ^ { 2 } } } \qquad \Delta \equiv \Delta x = \Delta y
$$

$$
\delta _ { x } ^ { 2 } u _ { j , l } ^ { n } \equiv u _ { j + 1 , l } ^ { n } - 2 u _ { j , l } ^ { n } + u _ { j - 1 , l } ^ { n }
$$

and similarly for $\delta _ { y } ^ { 2 } u _ { j , l } ^ { n }$ . This is certainly a viable scheme; the problem arises in solving the coupled linear equations. Whereas in one space dimension the system was tridiagonal, that is no longer true, though the matrix is still very sparse. One possibility is to use a suitable sparse matrix technique (see $\ S 2 . 7$ and $\ S 2 0 . 0 \AA$ ).

Another possibility, which we generally prefer, is a slightly different way of generalizing the Crank-Nicolson algorithm. It is still second-order accurate in time and space, and unconditionally stable, but the equations are easier to solve than (20.3.13). Called the alternating-direction implicit method $( A D I )$ , this embodies the powerful concept of operator splitting or time splitting, about which we will say more below. Here, the idea is to divide each timestep into two steps of size $\Delta t / 2$ . In each substep, a different dimension is treated implicitly:

$$
\begin{array} { r l } & { u _ { j , l } ^ { n + 1 / 2 } = u _ { j , l } ^ { n } + \frac { 1 } { 2 } \alpha \left( \delta _ { x } ^ { 2 } u _ { j , l } ^ { n + 1 / 2 } + \delta _ { y } ^ { 2 } u _ { j , l } ^ { n } \right) } \\ & { u _ { j , l } ^ { n + 1 } = u _ { j , l } ^ { n + 1 / 2 } + \frac { 1 } { 2 } \alpha \left( \delta _ { x } ^ { 2 } u _ { j , l } ^ { n + 1 / 2 } + \delta _ { y } ^ { 2 } u _ { j , l } ^ { n + 1 } \right) } \end{array}
$$

The advantage of this method is that each substep requires only the solution of a simple tridiagonal system.

# 20.3.3 Operator Splitting Methods Generally

The basic idea of operator splitting, which is also called time splitting or the method of fractional steps, is this: Suppose you have an initial value equation of the form

$$
\frac { \partial u } { \partial t } = \mathcal { L } u
$$

where $\mathcal { L }$ is some operator. While $\mathcal { L }$ is not necessarily linear, suppose that it can at least be written as a linear sum of $m$ pieces, which act additively on $u$ ,

$$
\mathcal { L } u = \mathcal { L } _ { 1 } u + \mathcal { L } _ { 2 } u + \cdot \cdot \cdot + \mathcal { L } _ { m } u
$$

Finally, suppose that for each of the pieces, you already know a differencing scheme for updating the variable $u$ from timestep $n$ to timestep $n + 1$ , valid if that piece of the operator were the only one on the right-hand side. We will write these updatings symbolically as

$$
\begin{array} { c } { u ^ { n + 1 } = \mathcal { U } _ { 1 } ( u ^ { n } , \Delta t ) } \\ { u ^ { n + 1 } = \mathcal { U } _ { 2 } ( u ^ { n } , \Delta t ) } \\ { \cdots } \\ { u ^ { n + 1 } = \mathcal { U } _ { m } ( u ^ { n } , \Delta t ) } \end{array}
$$

Now, one form of operator splitting would be to get from $n$ to $n + 1$ by the

following sequence of updatings:

$$
\begin{array} { r } { \left. u ^ { n + ( 1 / m ) } = \mathcal { U } _ { 1 } ( u ^ { n } , \Delta t ) \right. } \\ { \left. u ^ { n + ( 2 / m ) } = \mathcal { U } _ { 2 } ( u ^ { n + ( 1 / m ) } , \Delta t ) \right. } \\ { \left. \qquad \cdots \right. } \\ { \left. u ^ { n + 1 } = \mathcal { U } _ { m } ( u ^ { n + ( m - 1 ) / m } , \Delta t ) \right. } \end{array}
$$

For example, a combined advective-diffusion equation, such as

$$
{ \frac { \partial u } { \partial t } } = - v { \frac { \partial u } { \partial x } } + D { \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } }
$$

might profitably use an explicit scheme for the advective term combined with a Crank-Nicolson or other implicit scheme for the diffusion term.

The alternating-direction implicit (ADI) method, equation (20.3.16), is an example of operator splitting with a slightly different twist. Let us reinterpret (20.3.19) to have a different meaning: Let $\mathcal { U } _ { 1 }$ now denote an updating method that includes algebraically all the pieces of the total operator $\mathcal { L }$ , but which is desirably stable only for the $\mathcal { L } _ { 1 }$ piece; likewise $\mathcal { U } _ { 2 } , \dots \mathcal { U } _ { m }$ . Then a method of getting from $u ^ { n }$ to $u ^ { n + 1 }$ is

$$
\begin{array} { r l } & { u ^ { n + 1 / m } = \mathcal { U } _ { 1 } ( u ^ { n } , \Delta t / m ) } \\ & { u ^ { n + 2 / m } = \mathcal { U } _ { 2 } ( u ^ { n + 1 / m } , \Delta t / m ) } \\ & { \qquad \cdots } \end{array}
$$

$$
u ^ { n + 1 } = \mathcal { U } _ { m } ( u ^ { n + ( m - 1 ) / m } , \Delta t / m )
$$

The timestep for each fractional step in (20.3.22) is now only $1 / m$ of the full timestep, because each partial operation acts with all the terms of the original operator.

Equation (20.3.22) is usually, though not always, stable as a differencing scheme for the operator $\mathcal { L }$ . In fact, as a rule of thumb, it is often sufficient to have stable $\mathcal { U } _ { i }$ ’s only for the operator pieces having the highest number of spatial derivatives — the other $\mathcal { U } _ { i }$ ’s can be unstable — to make the overall scheme stable!

It is at this point that we turn our attention from initial value problems to boundary value problems. These will occupy us for most of the remainder of the chapter.

# CITED REFERENCES AND FURTHER READING:

Thomas, J.W. 1995, Numerical Partial Differential Equations: Finite Difference Methods (New York: Springer).   
Ames, W.F. 1992, Numerical Methods for Partial Differential Equations, 3rd ed. (New York: Academic Press).

# 20.4 Fourier and Cyclic Reduction Methods for Boundary Value Problems

As discussed in $\ S 2 0 . 0$ , most boundary value problems (elliptic equations, for example) reduce to solving large sparse linear systems of the form

$$
\mathbf { A \cdot u } = \mathbf { b }
$$

either once, for boundary value equations that are linear, or iteratively, for boundary value equations that are nonlinear.

Two important techniques lead to a “rapid” solution of equation (20.4.1) when the sparse matrix is of certain frequently occurring forms. The Fourier transform method is directly applicable when the equations have coefficients that are constant in space. The cyclic reduction method is somewhat more general; its applicability is related to the question of whether the equations are separable (in the sense of “separation of variables”). Both methods require the boundaries to coincide with the coordinate lines. Finally, for some problems, there is a powerful combination of these two methods called FACR (Fourier analysis and cyclic reduction). We now consider each method in turn, using equation (20.0.3), with finite difference representation (20.0.6), as a model example. Generally speaking, the methods in this section are faster, when they apply, than the simpler relaxation methods discussed in $\ S 2 0 . 5$ , but they are not necessarily faster than the more complicated multigrid methods discussed in $\ S 2 0 . 6$ .

# 20.4.1 Fourier Transform Method

The discrete inverse Fourier transform in both $x$ and $y$ is

$$
u _ { j l } = \frac { 1 } { J L } \sum _ { m = 0 } ^ { J - 1 } \sum _ { n = 0 } ^ { L - 1 } \hat { u } _ { m n } e ^ { - 2 \pi i j m / J } e ^ { - 2 \pi i l n / L }
$$

This can be computed using the FFT independently in each dimension, or else all at once via the routine fourn of $\ S 1 2 . 5$ or the routine rlft3 of $\ S 1 2 . 6$ . Similarly,

$$
\rho _ { j l } = \frac { 1 } { J L } \sum _ { m = 0 } ^ { J - 1 } \sum _ { n = 0 } ^ { L - 1 } \hat { \rho } _ { m n } e ^ { - 2 \pi i j m / J } e ^ { - 2 \pi i l n / L }
$$

If we substitute expressions (20.4.2) and (20.4.3) in our model problem (20.0.6), we find

$$
\widehat { u } _ { m n } \left( e ^ { 2 \pi i m / J } + e ^ { - 2 \pi i m / J } + e ^ { 2 \pi i n / L } + e ^ { - 2 \pi i n / L } - 4 \right) = \widehat { \rho } _ { m n } \Delta ^ { 2 }
$$

or

$$
\widehat { u } _ { m n } = \frac { \widehat { \rho } _ { m n } \Delta ^ { 2 } } { 2 \left( \cos \displaystyle \frac { 2 \pi m } { J } + \cos \displaystyle \frac { 2 \pi n } { L } - 2 \right) }
$$

Thus the strategy for solving equation (20.0.6) by FFT techniques is

- Compute $\widehat { \rho } _ { m n }$ as the Fourier transform

$$
\widehat { \rho } _ { m n } = \sum _ { j = 0 } ^ { J - 1 } \sum _ { l = 0 } ^ { L - 1 } \rho _ { j l } e ^ { 2 \pi i m j / J } e ^ { 2 \pi i n l / L }
$$

- Compute $\widehat { u } _ { m n }$ from equation (20.4.5).

- Compute $u _ { j l }$ by the inverse Fourier transform (20.4.2).

The above procedure is valid for periodic boundary conditions. In other words, the solution satisfies

$$
u _ { j l } = u _ { j + J , l } = u _ { j , l + L }
$$

Next consider a Dirichlet boundary condition $u = 0$ on the rectangular boundary. Instead of the expansion (20.4.2), we now need an expansion in sine waves:

$$
u _ { j l } = \frac { 2 } { J } \frac { 2 } { L } \sum _ { m = 1 } ^ { J - 1 } \sum _ { n = 1 } ^ { L - 1 } \widehat { u } _ { m n } \sin \frac { \pi j m } { J } \sin \frac { \pi l n } { L }
$$

This satisfies the boundary conditions that $u = 0$ at $j = 0 , J$ and at $l = 0 , L$ . If we substitute this expansion and the analogous one for $\rho _ { j l }$ into equation (20.0.6), we find that the solution procedure parallels that for periodic boundary conditions:

- Compute $\widehat { \rho } _ { m n }$ by the sine transform

$$
\widehat { \rho } _ { m n } = \sum _ { j = 1 } ^ { J - 1 } \sum _ { l = 1 } ^ { L - 1 } \rho _ { j l } \sin \frac { \pi j m } { J } \sin \frac { \pi l n } { L }
$$

(A fast sine transform algorithm was given in $\ S 1 2 . 3 .$

- Compute $\widehat { u } _ { m n }$ from the expression analogous to (20.4.5),

$$
\widehat { u } _ { m n } = \frac { \Delta ^ { 2 } \widehat { \rho } _ { m n } } { 2 \left( \cos \displaystyle \frac { \pi m } { J } + \cos \displaystyle \frac { \pi n } { L } - 2 \right) }
$$

- Compute $u _ { j l }$ by the inverse sine transform (20.4.8).

If we have inhomogeneous boundary conditions, for example $u \ = \ 0$ on all boundaries except $u = f ( y )$ on the boundary $x = J \Delta$ , we have to add to the above solution a solution $u ^ { H }$ of the homogeneous equation

$$
{ \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } + { \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } } = 0
$$

that satisfies the required boundary conditions. In the continuum case, this would be an expression of the form

$$
u ^ { H } = \sum _ { n } A _ { n } \sinh \frac { n \pi x } { L \Delta } \sin \frac { n \pi y } { L \Delta }
$$

where $A _ { n }$ would be found by requiring that $u = f ( y )$ at $x = J \Delta$ . In the discrete case, we have

$$
u _ { j l } ^ { H } = \frac { 2 } { L } \sum _ { n = 1 } ^ { L - 1 } A _ { n } \sinh \frac { \pi n j } { L } \sin \frac { \pi n l } { L }
$$

If $f ( y = l \Delta ) \equiv f _ { l }$ , then we get $A _ { n }$ from the inverse formula

$$
A _ { n } = \frac { 1 } { \sinh \left( \pi n J / L \right) } \sum _ { l = 1 } ^ { L - 1 } f _ { l } \sin \frac { \pi n l } L
$$

The complete solution to the problem is

$$
u = u _ { j l } + u _ { j l } ^ { H }
$$

By adding appropriate terms of the form (20.4.12), we can handle inhomogeneous terms on any boundary surface.

A much simpler procedure for handling inhomogeneous terms is to note that whenever boundary terms appear on the left-hand side of (20.0.6), they can be taken over to the right-hand side since they are known. The effective source term is therefore $\rho _ { j l }$ plus a contribution from the boundary terms. To implement this idea formally, write the solution as

$$
\boldsymbol { u } = \boldsymbol { u } ^ { \prime } + \boldsymbol { u } ^ { B }
$$

where $u ^ { \prime } = 0$ on the boundary, while $u ^ { B }$ vanishes everywhere except on the boundary. There it takes on the given boundary value. In the above example, the only nonzero values of $u ^ { B }$ would be

$$
u _ { J , l } ^ { B } = f _ { l }
$$

The model equation (20.0.3) becomes

$$
\nabla ^ { 2 } u ^ { \prime } = - \nabla ^ { 2 } u ^ { B } + \rho
$$

or, in finite difference form,

$$
\begin{array} { l } { { u _ { j + 1 , l } ^ { \prime } + u _ { j - 1 , l } ^ { \prime } + u _ { j , l + 1 } ^ { \prime } + u _ { j , l - 1 } ^ { \prime } - 4 u _ { j , l } ^ { \prime } = } } \\ { { \qquad - ( u _ { j + 1 , l } ^ { B } + u _ { j - 1 , l } ^ { B } + u _ { j , l + 1 } ^ { B } + u _ { j , l - 1 } ^ { B } - 4 u _ { j , l } ^ { B } ) + \Delta ^ { 2 } \rho _ { j , l } } } \end{array}
$$

All the $u ^ { B }$ terms in equation (20.4.19) vanish except when the equation is evaluated at $j = J - 1$ , where

$$
u _ { J , l } ^ { \prime } + u _ { J - 2 , l } ^ { \prime } + u _ { J - 1 , l + 1 } ^ { \prime } + u _ { J - 1 , l - 1 } ^ { \prime } - 4 u _ { J - 1 , l } ^ { \prime } = - f _ { l } + \Delta ^ { 2 } \rho _ { J - 1 , l }
$$

Thus the problem is now equivalent to the case of zero boundary conditions, except that one row of the source term is modified by the replacement

$$
\Delta ^ { 2 } \rho _ { J - 1 , l }  \Delta ^ { 2 } \rho _ { J - 1 , l } - f _ { l }
$$

The case of Neumann boundary conditions $\nabla u = 0$ is handled by the cosine expansion (12.4.11):

$$
u _ { j l } = \frac { 2 } { J } \frac { 2 } { L } \sum _ { m = 0 } ^ { J } \sum _ { n = 0 } ^ { L } \stackrel { \prime \prime } { \tilde { u } _ { m n } } \cos \frac { \pi j m } { J } \cos \frac { \pi l n } { L }
$$

Here the double prime notation means that the terms for $m = 0$ and $m = J$ should be multiplied by $\frac { 1 } { 2 }$ , and similarly for $n \ = \ 0$ and $n \ = \ L$ . Inhomogeneous terms $\nabla \boldsymbol { u } \ = \boldsymbol { g }$ can be again included by adding a suitable solution of the homogeneous equation, or more simply by taking boundary terms over to the right-hand side. For example, the condition

$$
{ \frac { \partial u } { \partial x } } = g ( y ) \qquad { \mathrm { a t } } \quad x = 0
$$

becomes

$$
\frac { u _ { 1 , l } - u _ { - 1 , l } } { 2 \Delta } = g _ { l }
$$

where $g _ { l } \equiv g ( y = l \Delta )$ . Once again we write the solution in the form (20.4.16), where now $\nabla u ^ { \prime } = 0$ on the boundary. This time $\nabla \boldsymbol u ^ { B }$ takes on the prescribed value on the boundary, but $u ^ { B }$ vanishes everywhere except just outside the boundary. Thus equation (20.4.24) gives

$$
u _ { - 1 , l } ^ { B } = - 2 \Delta g _ { l }
$$

All the $u ^ { B }$ terms in equation (20.4.19) vanish except when $j = 0$ :

$$
u _ { 1 , l } ^ { \prime } + u _ { - 1 , l } ^ { \prime } + u _ { 0 , l + 1 } ^ { \prime } + u _ { 0 , l - 1 } ^ { \prime } - 4 u _ { 0 , l } ^ { \prime } = 2 \Delta g _ { l } + \Delta ^ { 2 } \rho _ { 0 , l }
$$

Thus $u ^ { \prime }$ is the solution of a zero-gradient problem, with the source term modified by the replacement

$$
\Delta ^ { 2 } \rho _ { 0 , l } \to \Delta ^ { 2 } \rho _ { 0 , l } + 2 \Delta g _ { l }
$$

Sometimes Neumann boundary conditions are handled by using a staggered grid, with the $u$ ’s defined midway between zone boundaries so that first derivatives are centered on the mesh points. You can solve such problems using similar techniques to those described above if you use the alternative form of the cosine transform, equation (12.4.17).

# 20.4.2 Cyclic Reduction

Evidently the FFT method works only when the original PDE has constant coefficients and boundaries that coincide with the coordinate lines. An alternative algorithm, which can be used on somewhat more general equations, is called cyclic reduction (CR).

We illustrate cyclic reduction on the equation

$$
{ \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } } + { \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } } + b ( y ) { \frac { \partial u } { \partial y } } + c ( y ) u = g ( x , y )
$$

This form arises very often in practice from the Helmholtz or Poisson equations in polar, cylindrical, or spherical coordinate systems. More general separable equations are treated in [1].

The finite difference form of equation (20.4.28) can be written as a set of vector equations

$$
\mathbf { u } _ { j - 1 } + \mathbf { T } \cdot \mathbf { u } _ { j } + \mathbf { u } _ { j + 1 } = \mathbf { g } _ { j } \Delta ^ { 2 }
$$

Here the index $j$ comes from differencing in the $x$ -direction, while the $y$ -differencing (denoted by the index $l$ previously) has been left in vector form. The matrix $\mathbf { T }$ has the form

$$
{ \bf T } = { \bf B } - 2 { \bf 1 }
$$

where the 21 comes from the $x$ -differencing and the matrix $\mathbf { B }$ from the $y$ -differencing.   
The matrix $\mathbf { B }$ , and hence $\mathbf { T }$ , is tridiagonal with variable coefficients.

The CR method is derived by writing down three successive equations like (20.4.29):

$$
\begin{array} { r l } & { \mathbf { u } _ { j - 2 } + \mathbf { T } \cdot \mathbf { u } _ { j - 1 } + \mathbf { u } _ { j } = \mathbf { g } _ { j - 1 } \boldsymbol { \Delta } ^ { 2 } } \\ & { \mathbf { u } _ { j - 1 } + \mathbf { T } \cdot \mathbf { u } _ { j } + \mathbf { u } _ { j + 1 } = \mathbf { g } _ { j } \boldsymbol { \Delta } ^ { 2 } } \\ & { \mathbf { u } _ { j } + \mathbf { T } \cdot \mathbf { u } _ { j + 1 } + \mathbf { u } _ { j + 2 } = \mathbf { g } _ { j + 1 } \boldsymbol { \Delta } ^ { 2 } } \end{array}
$$

Matrix-multiplying the middle equation by $- \mathbf { T }$ and then adding the three equations, we get

$$
\mathbf { u } _ { j - 2 } + \mathbf { T } ^ { ( 1 ) } \cdot \mathbf { u } _ { j } + \mathbf { u } _ { j + 2 } = \mathbf { g } _ { j } ^ { ( 1 ) } \Delta ^ { 2 }
$$

This is an equation of the same form as (20.4.29), with

$$
\begin{array} { l } { { \bf { T } } ^ { ( 1 ) } = 2 { \bf { 1 } } - { \bf { T } } ^ { 2 } } \\ { { \bf { g } } _ { j } ^ { ( 1 ) } = \Delta ^ { 2 } ( { \bf { g } } _ { j - 1 } - { \bf { T } } \cdot { \bf { g } } _ { j } + { \bf { g } } _ { j + 1 } ) } \end{array}
$$

After one level of CR, we have reduced the number of equations by a factor of two. Since the resulting equations are of the same form as the original equation, we can repeat the process. Taking the number of mesh points to be a power of 2 for simplicity, we finally end up with a single equation for the central line of variables:

$$
\mathbf { T } ^ { ( f ) } \cdot \mathbf { u } _ { J / 2 } = \Delta ^ { 2 } \mathbf { g } _ { J / 2 } ^ { ( f ) } - \mathbf { u } _ { 0 } - \mathbf { u } _ { J }
$$

Here we have moved ${ \bf u } _ { 0 }$ and $\mathbf { u } _ { J }$ to the right-hand side because they are known boundary values. Equation (20.4.34) can be solved for $\mathbf { u } _ { J / 2 }$ by the standard tridiagonal algorithm. The two equations at level $f - 1$ involve $\mathbf { u } _ { J / 4 }$ and $\mathbf { u } _ { 3 J / 4 }$ . The equation for $\mathbf { u } _ { J / 4 }$ involves ${ \bf u } _ { 0 }$ and $\mathbf { u } _ { J / 2 }$ , both of which are known and hence can be solved by the usual tridiagonal routine. A similar result holds true at every stage, so we end up solving $J - 1$ tridiagonal systems.

In practice, equations (20.4.33) should be rewritten to avoid numerical instability. For these and other practical details, refer to [2].

# 20.4.3 FACR Method

The best way to solve equations of the form (20.4.28), including the constant coefficient problem (20.0.3), is a combination of Fourier analysis and cyclic reduction, the FACR method [3-6]. If at the $r$ th stage of CR we Fourier analyze the equations of the form (20.4.32) along $y$ , that is, with respect to the suppressed vector index, we will have a tridiagonal system in the $x$ -direction for each $y$ -Fourier mode:

$$
\hat { u } _ { j - 2 ^ { r } } ^ { k } + \lambda _ { k } ^ { ( r ) } \hat { u } _ { j } ^ { k } + \hat { u } _ { j + 2 ^ { r } } ^ { k } = \Delta ^ { 2 } g _ { j } ^ { ( r ) k }
$$

Here $\lambda _ { k } ^ { ( r ) }$ is the eigenvalue of $\mathbf { T } ^ { ( r ) }$ corresponding to the $k$ th Fourier mode. For the k equation (20.0.3), we see from equation (20.4.5) that $\lambda _ { k } ^ { ( r ) }$ will involve terms like $\cos ( 2 \pi k / L ) - 2$ raised to a power. Solve the tridiagonal systems for $\widehat { u } _ { j } ^ { k }$ at the levels $j = 2 ^ { r } , 2 \times 2 ^ { r } , 4 \times 2 ^ { r } , . . . , J - 2 ^ { r }$ . Fourier synthesize to get the $y$ -values on these $x$ -lines. Then fill in the intermediate $x$ -lines as in the original CR algorithm.

The trick is to choose the number of levels of CR so as to minimize the total number of arithmetic operations. One can show that for a typical case of a $1 2 8 \times 1 2 8$ mesh, the optimal level is $r = 2$ ; asymptotically, $r  \log _ { 2 } ( \log _ { 2 } J )$ .

A rough estimate of running times for these algorithms for equation (20.0.3) is as follows: The FFT method (in both $x$ and $y$ ) and the CR method are roughly comparable. FACR with $r = 0$ (that is, FFT in one dimension and solve the tridiagonal equations by the usual algorithm in the other dimension) gives about a factor of two gain in speed. The optimal FACR with $r = 2$ gives another factor of two gain in speed.

# CITED REFERENCES AND FURTHER READING:

Swartzrauber, P.N. 1977, “The Methods of Cyclic Reduction, Fourier Analysis and the FACR Algorithm for the Discrete Solution of Poisson’s Equation on a Rectangle,” SIAM Review, vol. 19, pp. 490–501.[1]   
Buzbee, B.L, Golub, G.H., and Nielson, C.W. 1970, “On Direct Methods for Solving Poisson’s Equation,” SIAM Journal on Numerical Analysis, vol. 7, pp. 627–656; see also op. cit. vol. 11, pp. 753–763.[2]   
Hockney, R.W. 1965, “A Fast Direct Solution of Poisson’s Equation Using Fourier Analysis,” Journal of the Association for Computing Machinery,vol.12,pp.95-113.[3]   
Hockney, R.W. 1970, “The Potential Calculation and Some Applications,” Methods of Computational Physics, vol.9 (New York: Academic Press),pp.135-211.[4]   
Hockney, R.W., and Eastwood, J.W. 1981, Computer Simulation Using Particles (New York: McGraw-Hill), Chapter 6.[5]   
Temperton, C. 1980, “On the FACR Algorithm for the Discrete Poisson Equation,” Journal of Computational Physics,vol. 34,pp.314-329.[6]

# 20.5 Relaxation Methods for Boundary Value Problems

As we mentioned in $\ S 2 0 . 0$ , relaxation methods involve splitting the sparse matrix that arises from finite differencing and then iterating until a solution is found.

There is another way of thinking about relaxation methods that is somewhat more physical. Suppose we wish to solve the elliptic equation

$$
\mathcal { L } u = \rho
$$

where $\mathcal { L }$ represents some elliptic operator and $\rho$ is the source term. Rewrite the equation as a diffusion equation,

$$
\frac { \partial \boldsymbol { u } } { \partial t } = \boldsymbol { \mathcal { L } } \boldsymbol { u } - \boldsymbol { \rho }
$$

An initial distribution $u$ relaxes to an equilibrium solution as $t  \infty$ . This equilibrium has all time derivatives vanishing. Therefore, it is the solution of the original elliptic problem (20.5.1). We see that all the machinery of $\ S 2 0 . 2$ , on diffusive initial value equations, can be brought to bear on the solution of boundary value problems by relaxation methods.

Let us apply this idea to our model problem (20.0.3). The diffusion equation is

$$
\frac { \partial u } { \partial t } = \frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } - \rho
$$

If we use FTCS differencing (cf. equation 20.2.4), we get

$$
u _ { j , l } ^ { n + 1 } = u _ { j , l } ^ { n } + \frac { \Delta t } { \Delta ^ { 2 } } \left( u _ { j + 1 , l } ^ { n } + u _ { j - 1 , l } ^ { n } + u _ { j , l + 1 } ^ { n } + u _ { j , l - 1 } ^ { n } - 4 u _ { j , l } ^ { n } \right) - \rho _ { j , l } \Delta t
$$

Recall from (20.2.6) that FTCS differencing is stable in one spatial dimension only if $\Delta t / \Delta ^ { 2 } \leq \frac { 1 } { 2 }$ . In two dimensions this becomes $\Delta t / \Delta ^ { 2 } \leq \frac { 1 } { 4 }$ . Suppose we try to take the largest possible timestep and set $\Delta t = \Delta ^ { 2 } / 4$ . Then equation (20.5.4) becomes

$$
u _ { j , l } ^ { n + 1 } = \frac { 1 } { 4 } \left( u _ { j + 1 , l } ^ { n } + u _ { j - 1 , l } ^ { n } + u _ { j , l + 1 } ^ { n } + u _ { j , l - 1 } ^ { n } \right) - \frac { \Delta ^ { 2 } } { 4 } \rho _ { j , l }
$$

Thus the algorithm consists of using the average of $u$ at its four nearest-neighbor points on the grid (plus the contribution from the source). This procedure is then iterated until convergence.

This method is in fact a classical method with origins dating back to the last century, called Jacobi’s method (not to be confused with the Jacobi method for eigenvalues). The method is not practical because it converges too slowly. However, it is the basis for understanding the modern methods, which are always compared with it.

Another classical method is the Gauss-Seidel method, which turns out to be important in multigrid methods (-20.6). Here we make use of updated values of $u$ on the right-hand side of (20.5.5) as soon as they become available. In other words, the averaging is done “in place” instead of being “copied” from an earlier timestep to a later one. If we are proceeding along the rows, incrementing $j$ for fixed $l$ , we have

$$
u _ { j , l } ^ { n + 1 } = \frac { 1 } { 4 } \left( u _ { j + 1 , l } ^ { n } + u _ { j - 1 , l } ^ { n + 1 } + u _ { j , l + 1 } ^ { n } + u _ { j , l - 1 } ^ { n + 1 } \right) - \frac { \Delta ^ { 2 } } { 4 } \rho _ { j , l }
$$

This method is also slowly converging and only of theoretical interest when used by itself, but some analysis of it will be instructive.

Let us look at the Jacobi and Gauss-Seidel methods in terms of the matrix splitting concept. We change notation and call u “ $\mathbf { \hat { X } }$ ,” to conform to standard matrix notation. To solve

$$
\mathbf { A \cdot x } = \mathbf { b }
$$

we can consider splitting A as

$$
\mathbf { A } = \mathbf { L } + \mathbf { D } + \mathbf { U }
$$

where $\mathbf { D }$ is the diagonal part of $\mathbf { A } , \mathbf { L }$ is the lower triangle of $\mathbf { A }$ with zeros on the diagonal, and $\mathbf { U }$ is the upper triangle of A with zeros on the diagonal.

In the Jacobi method we write for the $r$ th step of iteration

$$
\mathbf { D } \cdot \mathbf { x } ^ { ( r ) } = - ( \mathbf { L } + \mathbf { U } ) \cdot \mathbf { x } ^ { ( r - 1 ) } + \mathbf { b }
$$

For our model problem (20.5.5), $\mathbf { D }$ is simply the identity matrix. The Jacobi method converges for matrices A that are “diagonally dominant” in a sense that can be made mathematically precise. For matrices arising from finite differencing, this condition is usually met.

What is the rate of convergence of the Jacobi method? A detailed analysis is beyond our scope, but here is some of the flavor: The matrix $- \mathbf { D } ^ { - 1 } \cdot ( \mathbf { L } + \mathbf { \dot { U } } )$ is the iteration matrix that, apart from an additive term, maps one set of $\mathbf { X }$ ’s into the next. The iteration matrix has eigenvalues, each one of which reflects the factor by which the amplitude of a particular eigenmode of undesired residual is suppressed during one iteration. Evidently those factors had better all have modulus $< 1$ for the relaxation to work at all! The rate of convergence of the method is set by the rate for the slowest-decaying eigenmode, i.e., the factor with the largest modulus. The modulus of this largest factor, therefore lying between 0 and 1, is called the spectral radius of the relaxation operator, denoted $\rho _ { s }$ .

The number of iterations $r$ required to reduce the overall error by a factor $1 0 ^ { - p }$ is thus estimated by

$$
r \approx { \frac { p \ln 1 0 } { ( - \ln \rho _ { s } ) } }
$$

In general, the spectral radius $\rho _ { s }$ goes asymptotically to the value 1 as the grid size $J$ is increased, so that more iterations are required. For any given equation, grid geometry, and boundary condition, the spectral radius can, in principle, be computed analytically. For example, for equation (20.5.5) on a $J \times J$ grid with Dirichlet boundary conditions on all four sides, the asymptotic formula for large $J$ turns out to be

$$
\rho _ { s } \simeq 1 - \frac { \pi ^ { 2 } } { 2 J ^ { 2 } }
$$

The number of iterations $r$ required to reduce the error by a factor of $1 0 ^ { - p }$ is thus

$$
r \simeq \frac { 2 p J ^ { 2 } \ln 1 0 } { \pi ^ { 2 } } \simeq \frac { 1 } { 2 } p J ^ { 2 }
$$

In other words, the number of iterations is proportional to the number of mesh points, $J ^ { 2 }$ . Since $1 0 0 \times 1 0 0$ and larger problems are common, it is clear that the Jacobi method is only of theoretical interest.

The Gauss-Seidel method, equation (20.5.6), corresponds to the matrix decomposition

$$
( \mathbf { L } + \mathbf { D } ) \cdot \mathbf { x } ^ { ( r ) } = - \mathbf { U } \cdot \mathbf { x } ^ { ( r - 1 ) } + \mathbf { b }
$$

The fact that $\mathbf { L }$ is on the left-hand side of the equation follows from the updating in place, as you can easily check if you write out (20.5.13) in components. One can show [1-3] that the spectral radius is just the square of the spectral radius of the Jacobi method. For our model problem, therefore,

$$
\begin{array} { c } { { \displaystyle \rho _ { s } \simeq 1 - \frac { \pi ^ { 2 } } { J ^ { 2 } } } } \\ { { \displaystyle r \simeq \frac { p J ^ { 2 } \ln 1 0 } { \pi ^ { 2 } } \simeq \frac { 1 } { 4 } p J ^ { 2 } } } \end{array}
$$

The factor of two improvement in the number of iterations over the Jacobi method still leaves the method impractical.

# 20.5.1 Successive Overrelaxation (SOR)

We get a better algorithm — one that was the standard algorithm until the 1970s — if we make an overcorrection to the value of $\mathbf { x } ^ { ( r ) }$ at the $r$ th stage of Gauss-Seidel iteration, thus anticipating future corrections. Solve (20.5.13) for $\mathbf { x } ^ { ( r ) }$ , add and subtract $\mathbf { x } ^ { ( r - 1 ) }$ on the right-hand side, and hence write the Gauss-Seidel method as

$$
\mathbf { x } ^ { ( r ) } = \mathbf { x } ^ { ( r - 1 ) } - ( \mathbf { L } + \mathbf { D } ) ^ { - 1 } \cdot \left[ ( \mathbf { L } + \mathbf { D } + \mathbf { U } ) \cdot \mathbf { x } ^ { ( r - 1 ) } - \mathbf { b } \right]
$$

The term in square brackets is just the residual vector $\xi ^ { ( r - 1 ) }$ , so

$$
\mathbf { x } ^ { ( r ) } = \mathbf { x } ^ { ( r - 1 ) } - ( \mathbf { L } + \mathbf { D } ) ^ { - 1 } \cdot \boldsymbol { \xi } ^ { ( r - 1 ) }
$$

Now overcorrect, defining

$$
\mathbf { x } ^ { ( r ) } = \mathbf { x } ^ { ( r - 1 ) } - \omega ( \mathbf { L } + \mathbf { D } ) ^ { - 1 } \cdot \xi ^ { ( r - 1 ) }
$$

Here $\omega$ is called the overrelaxation parameter, and the method is called successive overrelaxation (SOR).

The following theorems can be proved [1-3]:

- The method is convergent only for $0 < \omega < 2$ . If $0 < \omega < 1$ , we speak of underrelaxation.   
- Under certain mathematical restrictions generally satisfied by matrices arising from finite differencing, only overrelaxation $\ : 1 \ : < \ : \omega \ : < \ : 2 \ :$ ) can give faster convergence than the Gauss-Seidel method.   
- If $\rho _ { \mathrm { J a c o b i } }$ is the spectral radius of the Jacobi iteration (so that the square of it is the spectral radius of the Gauss-Seidel iteration), then the optimal choice for $\omega$ is given by

$$
\omega = { \frac { 2 } { 1 + \sqrt { 1 - \rho _ { \mathrm { J a c o b i } } ^ { 2 } } } }
$$

- For this optimal choice, the spectral radius for SOR is

$$
\rho _ { \mathrm { S O R } } = \biggl ( \frac { \rho _ { \mathrm { J a c o b i } } } { 1 + \sqrt { 1 - \rho _ { \mathrm { J a c o b i } } ^ { 2 } } } \biggr ) ^ { 2 }
$$

As an application of the above results, consider our model problem for which $\rho _ { \mathrm { J a c o b i } }$ is given by equation (20.5.11). Then equations (20.5.19) and (20.5.20) give

$$
\begin{array} { r } { \omega \simeq \displaystyle \frac { 2 } { 1 + \pi / J } } \\ { \rho _ { \mathrm { S O R } } \simeq 1 - \displaystyle \frac { 2 \pi } { J } \qquad \mathrm { f o r ~ l a r g e } \quad J } \end{array}
$$

Equation (20.5.10) gives for the number of iterations to reduce the initial error by a factor of $1 0 ^ { - p }$ ,

$$
r \simeq \frac { p J \ln 1 0 } { 2 \pi } \simeq \frac { 1 } { 3 } p J
$$

Comparing with equation (20.5.12) or (20.5.15), we see that optimal SOR requires of order $J$ iterations, as opposed to of order $J ^ { 2 }$ . Since $J$ is typically 100 or larger, this makes a tremendous difference! Equation (20.5.23) leads to the mnemonic that three-figure accuracy $\dot { \boldsymbol { p } } = 3$ ) requires a number of iterations equal to the number of mesh points along a side of the grid. For six-figure accuracy, we require about twice as many iterations.

How do we choose $\omega$ for a problem for which the answer is not known analytically? That is just the weak point of SOR! The advantages of SOR obtain only in a fairly narrow window around the correct value of $\omega$ . It is better to take $\omega$ slightly too large, rather than slightly too small, but best to get it right.

One way to choose $\omega$ is to map your problem approximately onto a known problem, replacing the coefficients in the equation by average values. Note, however, that the known problem must have the same grid size and boundary conditions as the actual problem. We give for reference purposes the value of $\rho _ { \mathrm { J a c o b i } }$ for our model problem on a rectangular $J \times L$ grid, allowing for the possibility that $\Delta x \neq \Delta y$ :

$$
\rho _ { \mathrm { J a c o b i } } = { \frac { \cos { \frac { \pi } { J } } + \left( { \frac { \Delta x } { \Delta y } } \right) ^ { 2 } \cos { \frac { \pi } { L } } } { 1 + \left( { \frac { \Delta x } { \Delta y } } \right) ^ { 2 } } }
$$

Equation (20.5.24) holds for homogeneous Dirichlet or Neumann boundary conditions. For periodic boundary conditions, make the replacement $\pi  2 \pi$ .

A second way, which is especially useful if you plan to solve many similar elliptic equations each time with slightly different coefficients, is to determine the optimum value $\omega$ empirically on the first equation and then use that value for the remaining equations. Various automated schemes for doing this and for “seeking out” the best values of $\omega$ are described in the literature.

While the matrix notation introduced earlier is useful for theoretical analyses, for practical implementation of the SOR algorithm we need explicit formulas. Consider a general second-order elliptic equation in $x$ and $y$ , finite differenced on a square as for our model equation. Corresponding to each row of the matrix $\mathbf { A }$ is an equation of the form

$$
a _ { j , l } u _ { j + 1 , l } + b _ { j , l } u _ { j - 1 , l } + c _ { j , l } u _ { j , l + 1 } + d _ { j , l } u _ { j , l - 1 } + e _ { j , l } u _ { j , l } = f _ { j , l }
$$

For our model equation, we had $a = b = c = d = 1 , e = - 4$ . The quantity $f$ is proportional to the source term. The iterative procedure is defined by solving (20.5.25) for $u _ { j , l }$ :

$$
u _ { j , l } ^ { * } = \frac { 1 } { e _ { j , l } } \left( f _ { j , l } - a _ { j , l } u _ { j + 1 , l } - b _ { j , l } u _ { j - 1 , l } - c _ { j , l } u _ { j , l + 1 } - d _ { j , l } u _ { j , l - 1 } \right)
$$

Then $u _ { j , l } ^ { \mathrm { n e w } }$ is a weighted average,

$$
u _ { j , l } ^ { \mathrm { n e w } } = \omega u _ { j , l } ^ { * } + ( 1 - \omega ) u _ { j , l } ^ { \mathrm { o l d } }
$$

We calculate it as follows: The residual at any stage is

$$
\xi _ { j , l } = a _ { j , l } u _ { j + 1 , l } + b _ { j , l } u _ { j - 1 , l } + c _ { j , l } u _ { j , l + 1 } + d _ { j , l } u _ { j , l - 1 } + e _ { j , l } u _ { j , l } - f _ { j , l }
$$

and the SOR algorithm (20.5.18) or (20.5.27) is

$$
u _ { j , l } ^ { \mathrm { n e w } } = u _ { j , l } ^ { \mathrm { o l d } } - \omega \frac { \xi _ { j , l } } { e _ { j , l } }
$$

This formulation is very easy to program, and the norm of the residual vector $\xi _ { j , l }$ can be used as a criterion for terminating the iteration.

Another practical point concerns the order in which mesh points are processed. The obvious strategy is simply to proceed in order down the rows (or columns).

Alternatively, suppose we divide the mesh into “odd” and “even” meshes, like the red and black squares of a checkerboard. Then equation (20.5.26) shows that the odd points depend only on the even mesh values, and vice versa. Accordingly, we can carry out one half-sweep updating the odd points, say, and then another halfsweep updating the even points with the new odd values. For the version of SOR implemented below, we shall adopt odd-even ordering.

The last practical point is that in practice the asymptotic rate of convergence in SOR is not attained until of order $J$ iterations. The error often grows by a factor of 20 before convergence sets in. A trivial modification to SOR resolves this problem. It is based on the observation that, while $\omega$ is the optimum asymptotic relaxation parameter, it is not necessarily a good initial choice. In SOR with Chebyshev acceleration, one uses odd-even ordering and changes $\omega$ at each half-sweep according to the following prescription:

$$
\begin{array} { r l } { \omega ^ { ( 0 ) } = 1 } & { { } } \\ { \omega ^ { ( 1 / 2 ) } = 1 / ( 1 - \rho _ { \mathrm { J a c o b i } } ^ { 2 } / 2 ) } \\ { \omega ^ { ( n + 1 / 2 ) } = 1 / ( 1 - \rho _ { \mathrm { J a c o b i } } ^ { 2 } \omega ^ { ( n ) } / 4 ) , } & { { } \quad n = 1 / 2 , 1 , . . . , \infty } \\ { \omega ^ { ( \infty ) }  \omega _ { \mathrm { o p t i m a l } } } & { { } } \end{array}
$$

The beauty of Chebyshev acceleration is that the norm of the error always decreases with each iteration. (This is the norm of the actual error in $u _ { j , l }$ . The norm of the residual $\xi _ { j , l }$ need not decrease monotonically.) While the asymptotic rate of convergence is the same as ordinary SOR, there is never any excuse for not using Chebyshev acceleration to reduce the total number of iterations required.

Here we give a routine for SOR with Chebyshev acceleration.

void sor(MatDoub_I &a, MatDoub_I &b, MatDoub_I &c, MatDoub_I &d, MatDoub_I &e, MatDoub_I &f, MatDoub_IO &u, const Doub rjac)

Successive overrelaxation solution of equation (20.5.25) with Chebyshev acceleration. a, b, c, d, e, and f are input as the coefficients of the equation, each dimensioned to the grid size [0..jmax-1][0..jmax-1]. u is input as the initial guess to the solution, usually zero, and returns with the final value. rjac is input as the spectral radius of the Jacobi iteration, or an estimate of it.

const Int MAXITS $=$ 1000;   
const Doub EPS $^ { = 1 }$ .0e-13;   
Doub anormf ${ = } 0$ .0,omega $^ { = 1 }$ .0;   
Int jmax $= a$ .nrows();   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<jmax-1; ${ \mathrm { j } } + +$ )   
Compute initial norm of residual and terminate iterations when norm has been reduced by   
a factor EPS. for (Int $\ b { 1 } = 1$ ;l<jmax-1;l++) anormf $+ =$ abs(f[j][l]); Assumes initial u is zero.   
for (Int $\mathtt { n } { = } 0$ ;n<MAXITS; $\mathtt { n } + +$ ) { Doub anorm ${ = } 0$ .0; Int jsw $^ { \cdot = 1 }$ ; for (Int ipass=0;ipass<2;ipass $^ { + + }$ ) { Odd-even ordering. Int lsw=jsw; for (Int j=1;j<jmax-1;j++) { for (Int l=lsw;l<jmax-1; $_ { 1 + = 2 }$ ) { Doub resid=a[j][l]\*u[j+1][l]+b[j][l]\*u[j-1][l] +c[j][l]\*u[j][l+1]+d[j][l]\*u[j][l-1] +e[j][l]\*u[j][l]-f[j][l];

anorm $+ =$ abs(resid); u[j][l] $- =$ omega\*resid/e[j][l]; } lsw=3-lsw; } js $\scriptstyle \tau = 3 \cdot$ -jsw; omega $( \mathbf { n _ { \alpha } } = \mathbf { \beta } 0 )$ && ipass $\scriptstyle \mathbf { \mu = } \mathbf { \Lambda } _ { 0 } \ ?$ 1.0/(1.0-0.5\*rjac\*rjac) 1.0/(1.0-0.25\*rjac\*rjac\*omega)); } if (anorm $<$ EPS\*anormf) return; } throw("MAXITS exceeded");

The main advantage of SOR is that it is very easy to program. Its main disadvantage is that it is still very inefficient on large problems.

# 20.5.2 ADl (Alternating-Direction Implicit) Method

The ADI method of $\ S 2 0 . 3$ for diffusion equations can be turned into a relaxation method for elliptic equations [1-4]. In $\ S 2 0 . 3$ , we discussed ADI as a method for solving the time-dependent heat-flow equation

$$
{ \frac { \partial u } { \partial t } } = \nabla ^ { 2 } u - \rho
$$

By letting $t \to \infty$ , one also gets an iterative method for solving the elliptic equation

$$
\nabla ^ { 2 } u = \rho
$$

In either case, the operator splitting is of the form

$$
\mathcal { L } = \mathcal { L } _ { x } + \mathcal { L } _ { y }
$$

where ${ \mathcal { L } } _ { x }$ represents the differencing in $x$ and $\mathcal { L } _ { y }$ that in $y$ .

For example, in our model problem (20.0.6) with $\Delta x = \Delta y = \Delta$ , we have

$$
\begin{array} { r } { \mathcal { L } _ { x } u = 2 u _ { j , l } - u _ { j + 1 , l } - u _ { j - 1 , l } } \\ { \mathcal { L } _ { y } u = 2 u _ { j , l } - u _ { j , l + 1 } - u _ { j , l - 1 } } \end{array}
$$

More complicated operators may be similarly split, but there is some art involved. A bad choice of splitting can lead to an algorithm that fails to converge. Usually one tries to base the splitting on the physical nature of the problem. We know for our model problem that an initial transient diffuses away, and we set up the $x$ and $y$ splitting to mimic diffusion in each dimension.

Having chosen a splitting, we difference the time-dependent equation (20.5.31) implicitly in two half-steps:

$$
\begin{array} { r l r } & { } & { \frac { u ^ { n + 1 / 2 } - u ^ { n } } { \Delta t / 2 } = - \frac { \mathcal { L } _ { x } u ^ { n + 1 / 2 } + \mathcal { L } _ { y } u ^ { n } } { \Delta ^ { 2 } } - \rho } \\ & { } & { \frac { u ^ { n + 1 } - u ^ { n + 1 / 2 } } { \Delta t / 2 } = - \frac { \mathcal { L } _ { x } u ^ { n + 1 / 2 } + \mathcal { L } _ { y } u ^ { n + 1 } } { \Delta ^ { 2 } } - \rho } \end{array}
$$

(cf. equation 20.3.16). Here we have suppressed the spatial indices $( j , l )$ . In matrix notation, equations (20.5.35) are

$$
\begin{array} { r l } & { ( \mathbf { L } _ { x } + r \mathbf { 1 } ) \cdot \mathbf { u } ^ { n + 1 / 2 } = ( r \mathbf { 1 } - \mathbf { L } _ { y } ) \cdot \mathbf { u } ^ { n } - \Delta ^ { 2 } \rho } \\ & { \quad ( \mathbf { L } _ { y } + r \mathbf { 1 } ) \cdot \mathbf { u } ^ { n + 1 } = ( r \mathbf { 1 } - \mathbf { L } _ { x } ) \cdot \mathbf { u } ^ { n + 1 / 2 } - \Delta ^ { 2 } \rho } \end{array}
$$

where

$$
r \equiv { \frac { 2 \Delta ^ { 2 } } { \Delta t } }
$$

The matrices on the left-hand sides of equations (20.5.36) and (20.5.37) are tridiagonal (and usually positive-definite), so the equations can be solved by the standard tridiagonal algorithm. Given ${ \mathbf { u } } ^ { n }$ , one solves (20.5.36) for $\mathbf u ^ { n + 1 / 2 }$ , substitutes on the right-hand side of (20.5.37), and then solves for $ { \mathbf { u } } ^ { n + 1 }$ . The key question is how to choose the iteration parameter $r$ , the analog of a choice of timestep for an initial value problem.

As usual, the goal is to minimize the spectral radius of the iteration matrix. Although it is beyond our scope to go into details here, it turns out that, for the optimal choice of $r$ , the ADI method has the same rate of convergence as SOR. The individual iteration steps in the ADI method are much more complicated than in SOR, so the ADI method would appear to be inferior. This is in fact true if we choose the same parameter $r$ for every iteration step. However, it is possible to choose a different $r$ for each step. If this is done optimally, then ADI is generally more efficient than SOR. We refer you to the literature [1-4] for details.

Our reason for not fully implementing ADI here is that, in most applications, it has been superseded by the multigrid methods described in the next section. Our advice is to use SOR for trivial problems (e.g., $3 0 \times 3 0 )$ ) or for solving a larger problem once only, where ease of programming outweighs expense of computer time. Occasionally, the sparse matrix methods of $\ S 2 . 7$ are useful for solving a set of difference equations directly. For production solution of large elliptic problems, however, multigrid is now almost always the method of choice.

# CITED REFERENCES AND FURTHER READING:

Hockney, R.W., and Eastwood, J.W. 1981, Computer Simulation Using Particles (New York: McGraw-Hill), Chapter 6.   
Young, D.M. 1971, Iterative Solution of Large Linear Systems (New York: Academic Press); reprinted 2003 (New York: Dover).[1]   
Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), $\ S 8 . 3 - \ S 8 . 6 .$ [2]   
Varga, R.S. 2000, Matrix Iterative Analysis, 2nd ed. (New York: Springer).[3]   
Spanier, J. 1967, in Mathematical Methods for Digital Computers, Volume 2 (New York: Wiley), Chapter 11.[4]

# 20.6 Multigrid Methods for Boundary Value Problems

Practical multigrid methods were first introduced in the 1970s by Brandt [1,2]. These methods can solve elliptic PDEs discretized on $N$ grid points in $O ( N )$ operations. The “rapid” direct elliptic solvers discussed in $\ S 2 0 . 4$ solve special kinds of elliptic equations in ${ \cal O } ( N \log N )$ operations. The numerical coefficients in these estimates are such that multigrid methods are comparable to the rapid methods in execution speed. Unlike the rapid methods, however, the multigrid methods can solve general elliptic equations with nonconstant coefficients with hardly any loss in efficiency. Even nonlinear equations can be solved with comparable speed.

Unfortunately, there is not a single multigrid algorithm that solves all elliptic problems. Rather, there is a multigrid technique that provides the framework for solving these problems. You have to adjust the various components of the algorithm within this framework to solve your specific problem. We can only give a brief introduction to the subject here. In particular, we will give two sample multigrid routines, one linear and one nonlinear. By following these prototypes and by perusing the references [3-6], you should be able to develop routines to solve your own problems.

There are two related, but distinct, approaches to the use of multigrid techniques. The first, termed the multigrid method, is a means for speeding up the convergence of a traditional relaxation method, as defined by you on a grid of prespecified fineness. In this case, you need to define your problem (e.g., evaluate its source terms) only on this grid. Other, coarser, grids defined by the method can be viewed as temporary computational adjuncts.

The second approach, termed (perhaps confusingly) the full multigrid (FMG) method, requires you to be able to define your problem on grids of various sizes (generally by discretizing the same underlying PDE into different-sized sets of finite difference equations). In this approach, the method obtains successive solutions on finer and finer grids. You can stop the solution either at a pre-specified fineness, or you can monitor the truncation error due to the discretization, quitting only when it is tolerably small.

In this section we will first discuss the multigrid method and then use the concepts developed to introduce the FMG method. The latter algorithm is the one that we implement in the accompanying programs.

# 20.6.1 From One-Grid, through Two-Grid, to Multigrid

The key idea of the multigrid method can be understood by considering the simplest case of a two-grid method. Suppose we are trying to solve the linear elliptic problem

$$
\mathcal { L } u = f
$$

where $\mathcal { L }$ is some linear elliptic operator and $f$ is the source term. Discretize equation (20.6.1) on a uniform grid with mesh size $h$ . Write the resulting set of linear algebraic equations as

$$
\mathcal { L } _ { h } u _ { h } = f _ { h }
$$

Let $\widetilde { u } _ { h }$ denote some approximate solution to equation (20.6.2). We will use the symbol $u _ { h }$ to denote the exact solution to the difference equations (20.6.2). Then the error in $\widetilde { u } _ { h }$ or the correction is

$$
v _ { h } = u _ { h } - \widetilde { u } _ { h }
$$

The residual or defect is

$$
d _ { h } = \mathcal { L } _ { h } \widetilde { u } _ { h } - f _ { h }
$$

(Beware: Some authors define residual as minus the defect, and there is not universal agreement about which of these two quantities 20.6.4 defines.) Since $\mathcal { L } _ { h }$ is linear, the error satisfies

$$
\mathcal { L } _ { h } v _ { h } = - d _ { h }
$$

At this point we need to make an approximation to $\mathcal { L } _ { h }$ in order to find $v _ { h }$ . The classical iteration methods, such as Jacobi or Gauss-Seidel, do this by finding, at each stage, an approximate solution of the equation

$$
\hat { \mathcal { L } } _ { h } \hat { v } _ { h } = - d _ { h }
$$

where $\widehat { \mathcal { L } } _ { h }$ is a “simpler” operator than $\mathcal { L } _ { h }$ . For example, $\widehat { \mathcal { L } } _ { h }$ is the diagonal part of $\mathcal { L } _ { h }$ for Jacobi iteration, or the lower triangle for Gauss-Seidel iteration. The next approximation is generated by

$$
\widetilde { u } _ { h } ^ { \mathrm { n e w } } = \widetilde { u } _ { h } + \widehat { v } _ { h }
$$

Now consider, as an alternative, a completely different type of approximation for $\mathcal { L } _ { h }$ , one in which we “coarsify” rather than “simplify.” That is, we form some appropriate approximation $\mathcal { L } _ { H }$ of $\mathcal { L } _ { h }$ on a coarser grid with mesh size $H$ (we will always take $H = 2 h$ , but other choices are possible). The residual equation (20.6.5) is now approximated by

$$
\mathcal { L } _ { H } v _ { H } = - d _ { H }
$$

Since $\mathcal { L } _ { H }$ has smaller dimension, this equation will be easier to solve than equation (20.6.5). To define the defect $d _ { H }$ on the coarse grid, we need a restriction operator $\mathcal { R }$ that restricts $d _ { h }$ to the coarse grid:

$$
d _ { H } = \mathcal { R } d _ { h }
$$

The restriction operator is also called the fine-to-coarse operator or the injection operator. Once we have a solution $\widetilde { v } _ { H }$ to equation (20.6.8), we need a prolongation operator $\mathcal { P }$ that prolongates or interpolates the correction to the fine grid:

$$
\widetilde { v } _ { h } = \mathcal { P } \widetilde { v } _ { H }
$$

The prolongation operator is also called the coarse-to-fine operator or the interpolation operator. Both $\mathcal { R }$ and $\mathcal { P }$ are chosen to be linear operators. Finally, the approximation $\widetilde { u } _ { h }$ can be updated:

$$
\widetilde { u } _ { h } ^ { \mathrm { n e w } } = \widetilde { u } _ { h } + \widetilde { v } _ { h }
$$

One step of this coarse-grid correction scheme is thus:

# Coarse-Grid Correction

- Compute the defect on the fine grid from (20.6.4).   
Restrict the defect by (20.6.9).   
- Solve (20.6.8) exactly on the coarse grid for the correction.   
Interpolate the correction to the fine grid by (20.6.10).   
- Compute the next approximation by (20.6.11).

Let’s contrast the advantages and disadvantages of relaxation and the coarsegrid correction scheme. Consider the error $v _ { h }$ expanded into a discrete Fourier series. Call the components in the lower half of the frequency spectrum the smooth components and the high-frequency components the nonsmooth components. We have seen that relaxation becomes very slowly convergent in the limit $h  0$ , i.e., when there are a large number of mesh points. The reason turns out to be that the smooth components are only slightly reduced in amplitude on each iteration. However, many relaxation methods reduce the amplitude of the nonsmooth components by large factors on each iteration: They are good smoothing operators.

For the two-grid iteration, on the other hand, components of the error with wavelengths $\lesssim 2 H$ are not even representable on the coarse grid and so cannot be reduced to zero on this grid. But it is exactly these high-frequency components that can be reduced by relaxation on the fine grid! This leads us to combine the ideas of relaxation and coarse-grid correction:

# Two-Grid Iteration

- Pre-smoothing: Compute $\overline { { u } } _ { h }$ by applying $\nu _ { 1 } \geq 0$ steps of a relaxation method to $\widetilde { u } _ { h }$ .   
- Coarse-grid correction: As- Post-smoothing: Compute e, using by app $\overline { { u } } _ { h }$ $\overline { { u } } _ { h } ^ { \mathrm { n e w } }$ .teps of the relaxation $\widetilde { u } _ { h } ^ { \mathrm { n e w } }$ $\nu _ { 2 } ~ \geq ~ 0$ method to $\overline { { u } } _ { h } ^ { \mathrm { n e w } }$ .

It is only a short step from the above two-grid method to a multigrid method. Instead of solving the coarse-grid defect equation (20.6.8) exactly, we can get an approximate solution of it by introducing an even coarser grid and using the twogrid iteration method. If the convergence factor of the two-grid method is small enough, we will need only a few steps of this iteration to get a good enough approximate solution. We denote the number of such iterations by $\gamma$ . Obviously we can apply this idea recursively down to some coarsest grid. There the solution is found easily, for example by direct matrix inversion or by iterating the relaxation scheme to convergence.

One iteration of a multigrid method, from finest grid to coarser grids and back to finest grid again, is called a cycle. The exact structure of a cycle depends on the value of $\gamma$ , the number of two-grid iterations at each intermediate stage. The case $\gamma = 1$ is called a V-cycle, while $\gamma = 2$ is called a W-cycle (see Figure 20.6.1). These are the most important cases in practice.

Note that once more than two grids are involved, the pre-smoothing steps after the first one on the finest grid need an initial approximation for the error $v$ . This should be taken to be zero.

# 20.6.2 Smoothing, Restriction, and Prolongation Operators

The most popular smoothing method, and the one you should try first, is Gauss-Seidel, since it usually leads to a good convergence rate. If we order the mesh points from 0 to $N - 1$ , then the Gauss-Seidel scheme is

$$
u _ { i } = - \Big ( \sum _ { \stackrel { j = 0 } { j \neq i } } ^ { N - 1 } L _ { i j } u _ { j } - f _ { i } \Big ) \frac { 1 } { L _ { i i } } \qquad i = 0 , \ldots , N - 1
$$

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0016_pages_1051-1120/auto/images/d665875cbc5f1fe8c5c7b1962b61a2a9558b7ea01aee6e71f7341b53e2f60009.jpg)  
Figure 20.6.1. Structure of multigrid cycles. S denotes smoothing, while E denotes exact solution on the coarsest grid. Each descending line n denotes restriction $( { \mathcal { R } } )$ and each ascending line $/$ denotes prolongation $( \mathcal P )$ . The finest grid is at the top level of each diagram. For the V-cycles $\gamma = 1$ ) the E step is replaced by one two-grid iteration each time the number of grid levels is increased by one. For the W-cycles $( \gamma = 2$ ), each E step gets replaced by two two-grid iterations.

where new values of $u$ are used on the right-hand side as they become available. The exact form of the Gauss-Seidel method depends on the ordering chosen for the mesh points. For typical second-order elliptic equations like our model problem equation (20.0.3), as differenced in equation (20.0.8), it is usually best to use redblack ordering, making one pass through the mesh updating the “even” points (like the red squares of a checkerboard) and another pass updating the “odd” points (the black squares). When quantities are more strongly coupled along one dimension than another, one should relax a whole line along that dimension simultaneously. Line relaxation for nearest-neighbor coupling involves solving a tridiagonal system, and so is still efficient. Relaxing odd and even lines on successive passes is called zebra relaxation and is usually preferred over simple line relaxation.

Note that SOR should not be used as a smoothing operator. The overrelaxation destroys the high-frequency smoothing that is so crucial for the multigrid method.

A succint notation for the prolongation and restriction operators is to give their symbol. The symbol of $\mathcal { P }$ is found by considering $v _ { H }$ to be 1 at some mesh point $( x , y )$ , zero elsewhere, and then asking for the values of $\mathcal P v _ { H }$ . The most popular prolongation operator is simple bilinear interpolation. It gives nonzero values at the nine points $( x , y )$ $, ( x + h , y ) , \dotsc , ( x - h , y - h )$ , where the values are $1 , { \frac { 1 } { 2 } } , \ldots , { \frac { 1 } { 4 } }$ .

Its symbol is therefore

$$
\left[ { \begin{array} { l l l } { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 4 } } } \\ { { \frac { 1 } { 2 } } } & { { 1 } } & { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 4 } } } \end{array} } \right]
$$

The symbol of $\mathcal { R }$ is defined by considering $v _ { h }$ to be defined everywhere on the fine grid, and then asking what is $\mathcal { R } v _ { h }$ at $( x , y )$ as a linear combination of these values. The simplest possible choice for $\mathcal { R }$ is straight injection, which means simply filling each coarse-grid point with the value from the corresponding fine-grid point. Its symbol is “Œ1.” However, difficulties can arise in practice with this choice. It turns out that a safe choice for $\mathcal { R }$ is to make it the adjoint operator to $\mathcal { P }$ . To define the adjoint, define the scalar product of two grid functions $u _ { h }$ and $v _ { h }$ for mesh size $h$ as

$$
\langle u _ { h } | v _ { h } \rangle _ { h } \equiv h ^ { 2 } \sum _ { x , y } u _ { h } ( x , y ) v _ { h } ( x , y )
$$

Then the adjoint of $\mathcal { P }$ , denoted $\mathcal { P } ^ { \dagger }$ , is defined by

$$
\langle u _ { H } | \mathcal { P } ^ { \dagger } v _ { h } \rangle _ { H } = \langle \mathcal { P } u _ { H } | v _ { h } \rangle _ { h }
$$

Now take $\mathcal { P }$ to be bilinear interpolation, and choose $u _ { H } = 1$ at $( x , y )$ , zero elsewhere. Set $\mathcal { P } ^ { \dagger } = \mathcal { R }$ in (20.6.15) and $H = 2 h$ . You will find that

$$
\begin{array} { r } { ( \mathscr { R } v _ { h } ) _ { ( x , y ) } = \frac { 1 } { 4 } v _ { h } ( x , y ) + \frac { 1 } { 8 } v _ { h } ( x + h , y ) + \frac { 1 } { 1 6 } v _ { h } ( x + h , y + h ) + \cdots } \end{array}
$$

so that the symbol of $\mathcal { R }$ is

$$
\left[ { \begin{array} { l l l } { { \frac { 1 } { 1 6 } } } & { { \frac { 1 } { 8 } } } & { { \frac { 1 } { 1 6 } } } \\ { { \frac { 1 } { 8 } } } & { { \frac { 1 } { 4 } } } & { { \frac { 1 } { 8 } } } \\ { { \frac { 1 } { 1 6 } } } & { { \frac { 1 } { 8 } } } & { { \frac { 1 } { 1 6 } } } \end{array} } \right]
$$

Note the simple rule: The symbol of $\mathcal { R }$ is $\textstyle { \frac { 1 } { 4 } }$ the transpose of the matrix defining the symbol of $\mathcal { P }$ , equation (20.6.13). This rule is general whenever $\mathcal R = \mathcal P ^ { \dagger }$ and $H = 2 h$ .

The particular choice of $\mathcal { R }$ in (20.6.17) is called full weighting. Another popular choice for $\mathcal { R }$ is half weighting, “halfway” between full weighting and straight injection. Its symbol is

$$
\left[ { \begin{array} { l l l } { 0 } & { { \frac { 1 } { 8 } } } & { 0 } \\ { { \frac { 1 } { 8 } } } & { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 8 } } } \\ { 0 } & { { \frac { 1 } { 8 } } } & { 0 } \end{array} } \right]
$$

A similar notation can be used to describe the difference operator $\mathcal { L } _ { h }$ . For example, the standard differencing of the model problem, equation (20.0.6), is represented by the five-point difference star

$$
\mathcal { L } _ { h } = \frac { 1 } { h ^ { 2 } } \left[ \begin{array} { r r r } { 0 } & { 1 } & { 0 } \\ { 1 } & { - 4 } & { 1 } \\ { 0 } & { 1 } & { 0 } \end{array} \right]
$$

If you are confronted with a new problem and you are not sure what $\mathcal { P }$ and $\mathcal { R }$ choices are likely to work well, here is a safe rule: Suppose $m _ { p }$ is the order of the interpolation $\mathcal { P }$ (i.e., it interpolates polynomials of degree $m _ { p } - 1$ exactly). Suppose $m _ { r }$ is the order of $\mathcal { R }$ , and that $\mathcal { R }$ is the adjoint of some $\mathcal { P }$ (not necessarily the $\mathcal { P }$ you intend to use). Then, if $m$ is the order of the differential operator $\mathcal { L } _ { h }$ , you should satisfy the inequality $m _ { p } + m _ { r } > m$ . For example, bilinear interpolation and its adjoint, full weighting for Poisson’s equation satisfy $m _ { p } + m _ { r } = 4 > m = 2$ .

Of course the $\mathcal { P }$ and $\mathcal { R }$ operators should enforce the boundary conditions for your problem. The easiest way to do this is to rewrite the difference equation to have homogeneous boundary conditions by modifying the source term if necessary (cf. -20.4). Enforcing homogeneous boundary conditions simply requires the $\mathcal { P }$ operator to produce zeros at the appropriate boundary points. The corresponding $\mathcal { R }$ is then found by $\mathcal { R } = \mathcal { P } ^ { \dagger }$ .

# 20.6.3 Full Multigrid Algorithm

So far we have described multigrid as an iterative scheme, where one starts with some initial guess on the finest grid and carries out enough cycles (V-cycles, W-cycles,. . . ) to achieve convergence. This is the simplest way to use multigrid: Simply apply enough cycles until some appropriate convergence criterion is met. However, efficiency can be improved by using the full multigrid algorithm (FMG), also known as nested iteration.

Instead of starting with an arbitrary approximation on the finest grid (e.g., $u _ { h } =$ 0), the first approximation is obtained by interpolating from a coarse-grid solution:

$$
u _ { h } = \mathscr { P } u _ { H }
$$

The coarse-grid solution itself is found by a similar FMG process from even coarser grids. At the coarsest level, you start with the exact solution. Rather than proceed as in Figure 20.6.1, then, FMG gets to its solution by a series of increasingly tall “N’s,” each taller one probing a finer grid (see Figure 20.6.2).

Note that $\mathcal { P }$ in (20.6.20) need not be the same $\mathcal { P }$ used in the multigrid cycles. It should be at least of the same order as the discretization $\mathcal { L } _ { h }$ , but sometimes a higher-order operator leads to greater efficiency.

It turns out that you usually need one or at most two multigrid cycles at each level before proceeding down to the next finer grid. While there is theoretical guidance on the required number of cycles (e.g., [3]), you can easily determine it empirically. Fix the finest level and study the solution values as you increase the number of cycles per level. The asymptotic value of the solution is the exact solution of the difference equations. The difference between this exact solution and the solution for a small number of cycles is the iteration error. Now fix the number of cycles to be large, and vary the number of levels, i.e., the smallest value of $h$ used. In this way you can estimate the truncation error for a given $h$ . In your final production code, there is no point in using more cycles than you need to get the iteration error down to the size of the truncation error.

The simple multigrid iteration (cycle) needs the right-hand side $f$ only at the finest level. FMG needs $f$ at all levels. If the boundary conditions are homogeneous, you can use $f _ { H } = \mathcal { R } f _ { h }$ . This prescription is not always safe for inhomogeneous boundary conditions. In that case it is better to discretize $f$ on each coarse grid.

Note that the FMG algorithm produces the solution on all levels. It can therefore be combined with techniques like Richardson extrapolation.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0016_pages_1051-1120/auto/images/36dc3b0e566c060006d0ff260ee25296b3318f55d973a71cb1512eb865f2915a.jpg)  
Figure 20.6.2. Structure of cycles for the full multigrid (FMG) method (notation as in Figure 20.6.1). This method starts on the coarsest grid, interpolates, and then refines (by “V’s”) the solution onto grids of increasing fineness.

We now give a routine Mglin that implements the full multigrid algorithm for a linear equation, the model problem (20.0.6). It uses red-black Gauss-Seidel as the smoothing operator, bilinear interpolation for $\mathcal { P }$ , and half-weighting for $\mathcal { R }$ . To change the routine to handle another linear problem, all you need do is modify the functions relax, resid, and slvsml appropriately. A feature of the routine is the dynamical allocation of storage for variables defined on the various grids.

# struct Mglin {

Full multigrid algorithm for solution of linear elliptic equation, here the model problem (20.0.6) on a square domain of side 1, so that $\Delta = 1 / ( { \mathfrak { n } } - 1 )$ .

Int n,ng;   
MatDoub \*uj,\*uj1;   
NRvector<NRmatrix<Doub> \*> rho; Vector of pointers to $\rho$ on each level.

glin(MatDoub_IO &u, const Int ncycle) : n(u.nrows()), ${ \tt n g } ( 0 )$

On input u[0..n-1][0..n-1] contains the right-hand side $\rho$ , while on output it returns the solution. The dimension n must be of the form $2 ^ { j } + 1$ for some integer $j$ . ( $j$ is actually the number of grid levels used in the solution, called ng below.) ncycle is the number of V-cycles to be used at each level.

Int $\mathtt { n n } { = } \mathtt { n }$ ;   
while (nn >>= 1) $\mathrm { n g + + }$ ;   
if ( $( \mathtt { n - 1 } ) \quad ! = \ ( 1 \ < \ \mathtt { n g } ) )$ throw( $" \mathrm { n } - 1$ must be a power of 2 in mglin.");   
$\mathtt { n n } { = } \mathtt { n }$ ;   
Int ngrid=ng-1;   
rho.resize(ng);   
rho[ngrid] $=$ new MatDoub(nn,nn); Allocate storage for r.h.s. on grid $\tt { n g - 1 }$ ,   
\*rho[ngrid] ${ = } \mathrm { u }$ ; and fill it with the input r.h.s.   
while (nn $> 3$ ) { Similarly allocate storage and fill r.h.s. on nn=nn/2+1; all coarse grids by restricting from finer grids.

rho[--ngrid] $\equiv$ new MatDoub(nn,nn); rstrct(\*rho[ngrid],\*rho[ngrid+1]); } nn=3; uj=new MatDoub(nn,nn); slvsml(\*uj,\*rho[0]); Initial solution on coarsest grid. for (Int $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<ng;j++) { Nested iteration loop. nn=2\*nn-1; uj $\mathbf { \lambda } ^ { 1 = }$ uj; uj=new MatDoub(nn,nn); interp(\*uj,\*uj1); Interpolate from grid ${ \mathrm { j } } - 1$ to next finer grid delete uj1; j. for (Int jcycle ${ = } 0$ ;jcycle<ncycle;jcycle $^ { + + }$ ) V-cycle loop. mg(j,\*uj,\*rho[j]); } u = \*uj; Return solution in u.

# \~Mglin()

Destructor deletes storage.   
{ if (uj != NULL) delete uj; for (Int j=0;j<ng;j++) if (rho[j] $\downarrow =$ NULL) delete rho[j];   
}

# void interp(MatDoub_O &uf, MatDoub_I &uc)

Coarse-to-fine prolongation by bilinear interpolation. If nf is the fine-grid dimension, the coarse-grid solution is input as uc[0..nc-1][0..nc-1], where $\mathtt { n c } = \mathtt { n f } / 2 + 1$ . The finegrid solution is returned in uf[0..nf-1][0..nf-1].   
{   
Int nf $=$ uf.nrows();   
Int nc=nf/2+1;   
for (Int jc=0;jc<nc;jc $^ { + + }$ ) Do elements that are copies. for (Int ic=0;ic<nc;ic++) uf[2\*ic][2\*jc]=uc[ic][jc];   
for (Int jf=0;jf<nf;jf $+ = 2$ ) Do even-numbered columns, interpolating verfor (Int iif $= 1$ ;iif<nf-1;iif $+ { = } 2$ ) tically. uf[iif][jf] ${ = } 0$ . $^ { 5 \ast }$ (uf[iif+1][jf]+uf[iif-1][jf]);   
for (Int jf=1;jf<nf-1;jf $+ { = } 2$ ) Do odd-numbered columns, interpolating horfor (Int iif ${ = } 0$ ;iif<nf;iif $^ { + + }$ ) izontally. uf[iif][jf] ${ = } 0$ . $^ { 5 \ast }$ (uf[iif][jf+1]+uf[iif][jf-1]);

# }

# void addint(MatDoub_O &uf, MatDoub_I &uc, MatDoub_O &res)

Does coarse-to-fine interpolation and adds result to uf. If nf is the fine-grid dimension, the coarse-grid solution is input as uc[0..nc-1][0..nc-1], where $\mathtt { n c } = \mathtt { n f } / 2 + 1$ . The fine-grid solution is returned in uf[0..nf-1][0..nf-1]. res[0..nf-1][0..nf-1] is used for temporary storage.

Int nf $=$ uf.nrows();   
interp(res,uc);   
for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<nf;j++) for (Int $\scriptstyle \dot { 1 } = 0$ ;i<nf;i++) uf[i][j] $+ =$ res[i][j];

# }

# void slvsml(MatDoub_O &u, MatDoub_I &rhs)

Solution of the model problem on the coarsest grid, where $\begin{array} { r } { h = { \frac { 1 } { 2 } } } \end{array}$ . The right-hand side is input in rhs[0..2][0..2] and the solution is returned in u[0..2][0..2].

Doub h=0.5;   
for (Int i=0;i<3;i++) for (Int $\scriptstyle { \dot { \mathbf { J } } } = 0$ ;j<3;j++) u[i][j]=0.0;

u[1][1] $=$ -h\*h\*rhs[1][1]/4.0; }

void relax(MatDoub_IO &u, MatDoub_I &rhs)

Red-black Gauss-Seidel relaxation for model problem. Updates the current value of the solution u[0..n-1][0..n-1], using the right-hand side function rhs[0..n-1][0..n-1]. {

Int $\mathbf { n } { = } \mathbf { u }$ .nrows();   
Doub $\mathrm { { h } } = 1$ .0/(n-1);   
Doub h2=h\*h;   
for (Int ipass $\scriptstyle \mathtt { \backslash = 0 }$ ,js $\scriptstyle { \mathtt { G } } = 1$ ;ipass<2;ipass++,jsw=3-jsw) { Red and black sweeps. for (Int $\scriptstyle { \dot { \mathsf { J } } } = 1$ ,isw=jsw;j<n-1;j++,isw=3-isw) for (Int i=isw;i<n-1; $\scriptstyle \dot { 1 } + = 2$ ) Gauss-Seidel formula. u[i][j] ${ = } 0$ .25\*(u[i+1][j]+u[i-1][j]+u[i][j+1] +u[i][j-1]-h2\*rhs[i][j]);   
}

# }

# void resid(MatDoub_O &res, MatDoub_I &u, MatDoub_I &rhs)

Returns minus the residual for the model problem. Input quantities are u[0..n-1][0..n-1] and rhs[0..n-1][0..n-1], while res[0..n-1][0..n-1] is returned. {

Int $\mathbf { n } { = } \mathbf { u }$ .nrows();   
Doub $\mathrm { { h } } = 1$ .0/(n-1);   
Doub h2i $= 1$ .0/(h\*h);   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<n-1;j++) Interior points. for (Int $\dot { \ b _ { 1 } } = 1$ ;i<n-1; $\dot { \bf 1 } + + \dot { }$ ) res[i][j] $=$ -h2i\*(u[i+1][j]+u[i-1][j]+u[i][j+1] +u[i][j-1]-4.0\*u[i][j])+rhs[i][j];   
for (Int i=0;i<n; $\dot { \bar { \lambda } } + +$ ) Boundary points. res[i][0] $=$ res[i][n-1] $=$ res[0][i] $=$ res[n-1][i] ${ = } 0$ .0;

# }

# void rstrct(MatDoub_O &uc, MatDoub_I &uf)

Half-weighting restriction. If nc is the coarse-grid dimension, the fine-grid solution is input in uf[0..2\*nc-2][0..2\*nc-2].The coarse-grid solution obtained by restriction is returned in uc[0..nc-1][0..nc-1].

Int nc=uc.nrows(); Int ncc $\mathbf { \lambda } = \mathbf { \vec { \lambda } }$ 2\*nc-2; for (Int $\scriptstyle { \dot { \mathtt { J } } } { \dot { \mathtt { I } } } = 2$ ,j $\mathtt { c } = 1$ ;jc<nc-1;jc $^ { + + }$ ,jf $+ { = } 2$ ) { Interior points. for (Int iif $^ { = 2 }$ ,ic=1;ic<nc-1;ic++,iif $+ = 2$ ) { uc[ic][jc]=0.5\*uf[iif][jf]+0.125\*(uf[iif+1][jf]+uf[iif-1][jf] +uf[iif][jf+1]+uf[iif][jf-1]); } } for (Int j $\mathtt { c } = 0$ ,ic=0;ic<nc;ic++,jc $\scriptstyle \cdot + = 2$ ) { Boundary points. uc[ic][0] $=$ uf[jc][0]; uc[ic][nc-1] $=$ uf[jc][ncc]; } for (Int j $\mathtt { c } = 0$ ,i $\mathtt { C } = 0$ ;ic<nc;ic++,jc $+ = 2$ ) { uc[0][ic] $=$ uf[0][jc]; uc[nc-1][ic] $=$ uf[ncc][jc]; } }

# void mg(Int j, MatDoub_IO &u, MatDoub_I &rhs)

Recursive multigrid iteration. On input, j is the current level, u is the current value of the solution, and rhs is the right-hand side. On output u contains the improved solution at the current level.

const Int NPRE $\ c =$ 1,NPOST $\spadesuit = 1$ ;   
Int nf=u.nrows();   
Int nc $=$ (nf+1)/2;

Number of relaxation sweeps before and after the coarse-grid correction is computed.

if (j == 0) Bottom of V: Solve on coarsest grid. slvsml(u,rhs); else On downward stoke of the V. MatDoub res(nc,nc),v(nc,nc,0.0),temp(nf,nf); v is zero for initial guess in each relaxation. for (Int jpr $\mathtt { e } = 0$ ;jpre<NPRE;jpre++) relax(u,rhs); Pre-smoothing. resid(temp,u,rhs); rstrct(res,temp); Restriction of the residual is the next r.h.s. mg(j-1,v,res); Recursive call for the coarse-grid correction. addint(u,v,temp); On upward stroke of V. for (Int jpost ${ = } 0$ ;jpost<NPOST;jpost++) relax(u,rhs); Post-smoothing. } } };

The routine $\mathtt { M g l i n }$ is written for clarity, not maximum efficiency, so that it is easy to modify. Several simple changes will speed up the execution time:

- The defect $d _ { h }$ vanishes identically at all black mesh points after a red-black Gauss-Seidel step. Thus $d _ { H } ~ = ~ \mathcal { R } d _ { h }$ for half-weighting reduces to simply copying half the defect from the fine grid to the corresponding coarse-grid point. The calls to resid followed by rstrct in the first part of the V-cycle can be replaced by a routine that loops only over the coarse grid, filling it with half the defect. - Similarly, the quantity $\widetilde { u } _ { h } ^ { \mathrm { n e w } } = \widetilde { u } _ { h } + \mathcal { P } \widetilde { v } _ { H }$ need not be computed at red mesh Seidel sweep. This means that addint need only loop over black points. - You can speed up relax in several ways. First, you can have a special form when the initial guess is zero. Next, you can store $h ^ { 2 } f _ { h }$ on the various grids and save a multiplication. Finally, it is possible to save an addition in the Gauss-Seidel formula by rewriting it with intermediate variables. - For typical problems, Mglin with ncycle $= 1$ will return a solution with the iteration error bigger than the truncation error for the given size of $h$ . To knock the error down to the size of the truncation error, you have to set ncycle $= 2$ or, more cheaply, NPRE $= 2$ . A more efficient way turns out to be to use a higher-order $\mathcal { P }$ in (20.6.20) than the linear interpolation used in the V-cycle.

Implementing all the above features typically gives up to a factor of two improvement in execution time and is certainly worthwhile in a production code.

# 20.6.4 Nonlinear Multigrid: The FAS Algorithm

Now turn to solving a nonlinear elliptic equation, which we write symbolically as

$$
\mathcal { L } ( u ) = 0
$$

Any explicit source term has been moved to the left-hand side. Suppose equation (20.6.21) is suitably discretized:

$$
\mathcal { L } _ { h } ( u _ { h } ) = 0
$$

We will see below that in the multigrid algorithm we will have to consider equations where a nonzero right-hand side is generated during the course of the solution:

$$
\mathcal { L } _ { h } ( u _ { h } ) = f _ { h }
$$

One way of solving nonlinear problems with multigrid is to use Newton’s method, which produces linear equations for the correction term at each iteration. We can then use linear multigrid to solve these equations. A great strength of the multigrid idea, however, is that it can be applied directly to nonlinear problems. All we need is a suitable nonlinear relaxation method to smooth the errors, plus a procedure for approximating corrections on coarser grids. This direct approach is Brandt’s full approximation storage algorithm (FAS). No nonlinear equations need be solved, except perhaps on the coarsest grid.

To develop the nonlinear algorithm, suppose we have a relaxation procedure that can smooth the residual vector as we did in the linear case. Then we can seek a smooth correction $v _ { h }$ to solve (20.6.23):

$$
\mathcal { L } _ { h } ( \widetilde { \boldsymbol { u } } _ { h } + \boldsymbol { v } _ { h } ) = f _ { h }
$$

To find $v _ { h }$ , note that

$$
\begin{array} { r } { \mathcal { L } _ { h } ( \widetilde { \boldsymbol { u } } _ { h } + \boldsymbol { v } _ { h } ) - \mathcal { L } _ { h } ( \widetilde { \boldsymbol { u } } _ { h } ) = f _ { h } - \mathcal { L } _ { h } ( \widetilde { \boldsymbol { u } } _ { h } ) } \\ { = - d _ { h } } \end{array}
$$

The right-hand side is smooth after a few nonlinear relaxation sweeps. Thus we can transfer the left-hand side to a coarse grid:

$$
\mathcal { L } _ { H } ( u _ { H } ) - \mathcal { L } _ { H } ( \mathcal { R } \widetilde { u } _ { h } ) = - \mathcal { R } d _ { h }
$$

that is, we solve

$$
\mathcal { L } _ { H } ( u _ { H } ) = \mathcal { L } _ { H } ( \mathcal { R } \tilde { u } _ { h } ) - \mathcal { R } d _ { h }
$$

on the coarse grid. (This is how nonzero right-hand sides appear.) Suppose the approximate solution is $\widetilde { u } _ { H }$ . Then the coarse-grid correction is

$$
\widetilde { v } _ { H } = \widetilde { u } _ { H } - \mathcal { R } \widetilde { u } _ { h }
$$

and

$$
\widetilde { u } _ { h } ^ { \mathrm { n e w } } = \widetilde { u } _ { h } + \mathcal { P } ( \widetilde { u } _ { H } - \mathcal { R } \widetilde { u } _ { h } )
$$

Note that $\mathcal { P R } \neq 1$ in general, so $\widetilde { u } _ { h } ^ { \mathrm { n e w } } \neq \mathcal { P } \widetilde { u } _ { H }$ . This is a key point: In equation (20.6.29), the interpolation error comes only from the correction, not from the full solution $\widetilde { u } _ { H }$ .

Equation (20.6.27) shows that one is solving for the full approximation $u _ { H }$ , not just the error as in the linear algorithm. This is the origin of the name FAS.

The FAS multigrid algorithm thus looks very similar to the linear multigrid algorithm. The only differences are that both the defect $d _ { h }$ and the relaxed approximation $u _ { h }$ have to be restricted to the coarse grid, where now it is equation (20.6.27) that is solved by recursive invocation of the algorithm. However, instead of implementing the algorithm this way, we will first describe the so-called dual viewpoint, which leads to a powerful alternative way of looking at the multigrid idea.

The dual viewpoint considers the local truncation error, defined as

$$
\tau \equiv \mathcal { L } _ { h } ( u ) - f _ { h }
$$

where $u$ is the exact solution of the original continuum equation. If we rewrite this as

$$
\mathcal { L } _ { h } ( u ) = f _ { h } + \tau
$$

we see that $\tau$ can be regarded as the correction to $f _ { h }$ so that the solution of the fine-grid equation will be the exact solution $u$ .

Now consider the relative truncation error $\tau _ { h }$ , which is defined on the $H$ -grid relative to the $h$ -grid:

$$
\tau _ { h } \equiv \mathcal { L } _ { H } ( \mathcal { R } u _ { h } ) - \mathcal { R } \mathcal { L } _ { h } ( u _ { h } )
$$

Since $\mathcal { L } _ { h } ( u _ { h } ) = f _ { h }$ , this can be rewritten as

$$
\mathcal { L } _ { H } ( u _ { H } ) = f _ { H } + \tau _ { h }
$$

In other words, we can think of $\tau _ { h }$ as the correction to $f _ { H }$ that makes the solution of the coarse-grid equation equal to the fine-grid solution. Of course we cannot compute $\tau _ { h }$ , but we do have an approximation to it from using $\widetilde { u } _ { h }$ in equation (20.6.32):

$$
\tau _ { h } \simeq \tilde { \tau } _ { h } \equiv \mathcal { L } _ { H } ( \mathcal { R } \tilde { u } _ { h } ) - \mathcal { R } \mathcal { L } _ { h } ( \tilde { u } _ { h } )
$$

Replacing $\tau _ { h }$ by $\widetilde { \tau } _ { h }$ in equation (20.6.33) gives

$$
\mathcal { L } _ { H } ( u _ { H } ) = \mathcal { L } _ { H } ( \mathcal { R } \tilde { u } _ { h } ) - \mathcal { R } d _ { h }
$$

which is just the coarse-grid equation (20.6.27)!

Thus we see that there are two complementary viewpoints for the relation between coarse and fine grids:

- Coarse grids are used to accelerate the convergence of the smooth components of the fine-grid residuals.   
- Fine grids are used to compute correction terms to the coarse-grid equations, yielding fine-grid accuracy on the coarse grids.

One benefit of this new viewpoint is that it allows us to derive a natural stopping criterion for a multigrid iteration. Normally the criterion would be

$$
\| d _ { h } \| \leq \epsilon
$$

and the question is how to choose $\epsilon$ . There is clearly no benefit in iterating beyond the point when the remaining error is dominated by the local truncation error $\tau$ . The computable quantity is $\widetilde { \tau } _ { h }$ . What is the relation between $\tau$ and $\widetilde { \tau } _ { h }$ ? For the typical case of a second-order accurate differencing scheme,

$$
\tau = \mathcal { L } _ { h } ( u ) - \mathcal { L } _ { h } ( u _ { h } ) = h ^ { 2 } \tau _ { 2 } ( x , y ) + \cdots
$$

Assume the solution satisfies $u _ { h } = u + h ^ { 2 } u _ { 2 } ( x , y ) + \cdot \cdot \cdot$ . Then, assuming $\mathcal { R }$ is of high enough order that we can neglect its effect, equation (20.6.32) gives

$$
\begin{array} { r l } & { \tau _ { h } \simeq \mathcal { L } _ { H } ( u + h ^ { 2 } u _ { 2 } ) - \mathcal { L } _ { h } ( u + h ^ { 2 } u _ { 2 } ) } \\ & { \quad = \mathcal { L } _ { H } ( u ) - \mathcal { L } _ { h } ( u ) + h ^ { 2 } [ \mathcal { L } _ { H } ^ { \prime } ( u _ { 2 } ) - \mathcal { L } _ { h } ^ { \prime } ( u _ { 2 } ) ] + \cdot \cdot \cdot } \\ & { \quad = ( H ^ { 2 } - h ^ { 2 } ) \tau _ { 2 } + O ( h ^ { 4 } ) } \end{array}
$$

For the usual case of $H = 2 h$ , we therefore have

$$
\begin{array} { r } { \tau \simeq \frac { 1 } { 3 } \tau _ { h } \simeq \frac { 1 } { 3 } \widetilde { \tau } _ { h } } \end{array}
$$

The stopping criterion is thus equation (20.6.36) with

$$
\begin{array} { r } { \epsilon = \alpha \| \widetilde { \tau } _ { h } \| , \qquad \alpha \sim \frac { 1 } { 3 } } \end{array}
$$

We have one remaining task before implementing our nonlinear multigrid algorithm: choosing a nonlinear relaxation scheme. Once again, your first choice should probably be the nonlinear Gauss-Seidel scheme. If the discretized equation (20.6.23) is written with some choice of ordering as

$$
L _ { i } \left( u _ { 0 } , \dots , u _ { N - 1 } \right) = f _ { i } , \qquad i = 0 , \dots , N - 1
$$

then the nonlinear Gauss-Seidel schemes solves

$$
L _ { i } ( u _ { 0 } , \dots , u _ { i - 1 } , u _ { i } ^ { \mathrm { n e w } } , u _ { i + 1 } , \dots , u _ { N - 1 } ) = f _ { i }
$$

for $u _ { i } ^ { \mathrm { n e w } }$ . As usual, new $u$ ’s replace old $u$ ’s as soon as they have been computed. Often i equation (20.6.42) is linear in $u _ { i } ^ { \mathrm { n e w } }$ , since the nonlinear terms are discretized by means of

its neighbors. If this is not the case, we replace equation (20.6.42) by one step of a Newton iteration:

$$
u _ { i } ^ { \mathrm { n e w } } = u _ { i } ^ { \mathrm { o l d } } - \frac { L _ { i } ( u _ { i } ^ { \mathrm { o l d } } ) - f _ { i } } { \partial L _ { i } ( u _ { i } ^ { \mathrm { o l d } } ) / \partial u _ { i } }
$$

For example, consider the simple nonlinear equation

$$
\nabla ^ { 2 } u + u ^ { 2 } = \rho
$$

In two-dimensional notation, we have

$$
\mathcal { L } ( u _ { i , j } ) = ( u _ { i + 1 , j } + u _ { i - 1 , j } + u _ { i , j + 1 } + u _ { i , j - 1 } - 4 u _ { i , j } ) / h ^ { 2 } + u _ { i , j } ^ { 2 } - \rho _ { i , j } = 0
$$

Since

$$
\frac { \partial \mathcal { L } } { \partial u _ { i , j } } = - 4 / h ^ { 2 } + 2 u _ { i , j }
$$

the Newton Gauss-Seidel iteration is

$$
u _ { i , j } ^ { \mathrm { n e w } } = u _ { i , j } - \frac { \mathcal { L } ( u _ { i , j } ) } { - 4 / h ^ { 2 } + 2 u _ { i , j } }
$$

Here is a routine Mgfas that solves equation (20.6.44) using the full multigrid algorithm and the FAS scheme. Restriction and prolongation are done as in $\mathtt { M g l i n }$ . We have included the convergence test based on equation (20.6.40). A successful multigrid solution of a problem should aim to satisfy this condition with the maximum number of V-cycles, maxcyc, equal to 1 or 2. The routine Mgfas uses the same functions interp and rstrct as $\mathtt { M g l i n }$ .

# struct Mgfas {

Full multigrid algorithm for FAS solution of nonlinear elliptic equation, here equation (20.6.44) on a square domain of side 1, so that $h = 1 / ( \mathbf { n } - 1 )$ .

Int n,ng;   
MatDoub \*uj,\*uj1;   
NRvector<NRmatrix<Doub> \*> rho; Vector of pointers to $\rho$ on each level.

Mgfas(MatDoub_IO &u, const Int maxcyc) : n(u.nrows()), ${ \tt n g } ( 0 )$

On input u[0..n-1][0..n-1] contains the right-hand side $\rho$ , while on output it returns the solution. The dimension n must be of the form $2 ^ { j } + 1$ for some integer $j$ . ( $j$ is actually the number of grid levels used in the solution, called ng below.) maxcyc is the maximum number of V-cycles to be used at each level.   
  
Int $\mathrm { n n } { = } \mathrm { n }$ ;   
while (n $\mathrm { ~  ~ n ~ } > > = \mathrm { ~  ~ 1 ~ }$ ) $\tt { n g + + }$ ;   
if ( $( \mathtt { n - 1 } ) \quad ! = \ ( 1 \ \ll \ \mathtt { n g } ) ;$ ) throw( $" \mathtt { n } - 1$ must be a power of 2 in mgfas.");   
$\mathrm { n n } { = } \mathrm { n }$ ;   
Int ngrid=ng-1;   
rho.resize(ng);   
rho[ngrid] $=$ new MatDoub(nn,nn); Allocate storage for r.h.s. on grid $\tt { n g - 1 }$ ,   
\*rho[ngrid] ${ = } \mathrm { u }$ ; and fill it with the input r.h.s.   
while (nn > 3) { Similarly allocate storage and fill r.h.s. by nn=nn/2+1; restriction on all coarse grids. rho[--ngrid] $=$ new MatDoub(nn,nn); rstrct(\*rho[ngrid],\*rho[ngrid+1]);   
}   
nn=3;   
uj=new MatDoub(nn,nn);   
slvsm2(\*uj,\*rho[0]); Initial solution on coarsest grid.   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<ng;j++) { Nested iteration loop. nn=2\*nn-1; uj $ 1 =$ uj; uj $=$ new MatDoub(nn,nn);

MatDoub temp(nn,nn); interp(\*uj,\*uj1); Interpolate from grid ${ \mathrm { j } } - 1$ to next finer grid delete uj1; j. for (Int jcycle ${ = } 0$ ;jcycle<maxcyc;jcycle++) { V-cycle loop. Doub trerr ${ \tt = } 1$ .0; R.h.s. is dummy. mg(j,\*uj,temp,rho,trerr); lop(temp,\*uj); Form residual $\| d _ { h } \|$ . matsub(temp,\*rho[j],temp); Doub res $=$ anorm2(temp); if (res < trerr) break; No more V-cycles needed if residual small } enough. } $\mu = \ast \mathrm { u j }$ ; Return solution in u.

# \~Mgfas()

Destructor deletes storage.   
{ if (uj $! =$ NULL) delete uj; for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<ng;j++) if (rho[j] $! =$ NULL) delete rho[j];   
} void matadd(MatDoub_I &a, MatDoub_I &b, MatDoub_O &c)   
Matrix addition: Adds a[0..n-1][0..n-1] to b[0..n-1][0..n-1] and returns result in c[0..n-1][0..n-1].   
Int n=a.nrows();   
for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<n;j++) for (Int $\scriptstyle \dot { 1 } = 0$ ;i<n; $\dot { 1 } + +$ ) c[i][j] $= a$ [i][j]+b[i][j];

# }

void matsub(MatDoub_I &a, MatDoub_I &b, MatDoub_O &c)

Matrix subtraction: Subtracts b[0..n-1][0..n-1] from a[0..n-1][0..n-1] and returns result in c[0..n-1][0..n-1].

{ Int $\mathtt { n } = \mathtt { a }$ .nrows(); for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<n;j++) for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<n;i++) c[i][j] $= a$ [i][j]-b[i][j];   
}

# void slvsm2(MatDoub_O &u, MatDoub_I &rhs)

Solution of equation (20.6.44) on the coarsest grid, where $\begin{array} { r } { h = { \frac { 1 } { 2 } } } \end{array}$ . The right-hand side is input in rhs[0..2][0..2] and the solution is returned in u[0..2][0..2]. {

Doub $\mathtt { h } = 0$ .5;   
for (Int i=0;i<3;i++) for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<3;j $^ { + + }$ ) u[i][j] $= 0 . 0$ ;   
Doub fact $^ { = 2 }$ .0/(h\*h);   
Doub disc $=$ sqrt(fact\*fact+rhs[1][1]);   
u[1][1] $=$ -rhs[1][1]/(fact+disc);

# void relax2(MatDoub_IO &u, MatDoub_I &rhs)

Red-black Gauss-Seidel relaxation for equation (20.6.44). The current value of the solution u[0..n-1][0..n-1] is updated, using the right-hand side function rhs[0..n-1][0..n-1].

{Int n=u.nrows();Int jsw=1;Doub $\mathrm { h } = 1$ .0/(n-1);

Doub h2i=1.0/(h\*h); Doub foh2 $=$ -4. $0 * \mathtt { h } 2 \mathtt { i }$ ; for (Int ipas $\mathtt { s } = 0$ ;ipass<2;ipass $^ { + + }$ ,jsw $\scriptstyle = 3$ -jsw) { Red and black sweeps. Int isw=jsw; for (Int $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<n-1;j++,isw=3-isw) { for (Int $\mathrm { i } =$ isw;i<n-1; $\scriptstyle \dot { 1 } + = 2$ ) { Doub res=h2i\*(u[i+1][j]+u[i-1][j]+u[i][j+1]+u[i][j-1]- 4.0\*u[i][j])+u[i][j]\*u[i][j]-rhs[i][j]; u[i][j] $- =$ res/(foh2+2.0\*u[i][j]); Newton Gauss-Seidel formula. } } } }

# void rstrct(MatDoub_O &uc, MatDoub_I &uf)

Half-weighting restriction. If nc is the coarse-grid dimension, the fine-grid solution is input in uf[0..2\*nc-2][0..2\*nc-2].The coarse-grid solution obtained by restriction is returned in uc[0..nc-1][0..nc-1].

Int nc=uc.nrows(); Int ncc 2\*nc-2; for (Int $\scriptstyle { \dot { \mathcal { I } } } \mathbf { f } = 2$ ,j $\mathtt { c } = 1$ ;jc<nc-1;jc++,jf $+ { = } 2$ ) { Interior points. for (Int iif $^ { - 2 }$ ,ic=1;ic<nc-1;ic $^ { + + }$ ,iif $+ { = } 2$ ) { uc[ic][jc]=0.5\*uf[iif][jf]+0.125\*(uf[iif+1][jf]+uf[iif-1][jf] +uf[iif][jf+1]+uf[iif][jf-1]); } } for (Int $\scriptstyle { \mathrm { i } } c = 0$ ,ic=0;ic<nc;ic++,jc $+ { = } 2$ ) { Boundary points. uc[ic][0] $=$ uf[jc][0]; uc[ic][nc-1] $=$ uf[jc][ncc]; } for (Int $\mathtt { c } = 0$ ,ic=0;ic<nc;ic++,jc $+ { = } 2$ ) { uc[0][ic] $=$ uf[0][jc]; uc[nc-1][ic] $=$ uf[ncc][jc]; } }

void lop(MatDoub_O &out, MatDoub_I &u)   
Given u[0..n-1][0..n-1], returns $\mathcal { L } _ { h } ( \widetilde { u } _ { h } )$ for eqn. (20.6.44) in out[0..n-1][0..n-1]. {   
Int $\mathbf { n } { = } \mathbf { u }$ .nrows();   
Doub $\mathrm { { h } } = 1$ .0/(n-1);   
Doub h2i=1.0/(h\*h);   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<n-1;j $^ { + + }$ ) Interior points. for (Int $\dot { \bar { 1 } } = 1$ ;i<n-1;i++) out[i][j]=h2i\*(u[i+1][j]+u[i-1][j]+u[i][j+1]+u[i][j-1]- 4.0\*u[i][j]) $+ \ u$ [i][j]\*u[i][j];   
for (Int i=0;i<n;i++) Boundary points. out[i][0] $=$ out[i][n-1] $=$ out[0][i] $=$ out[n-1][i] ${ = } 0$ .0;

# }

# void interp(MatDoub_O &uf, MatDoub_I &uc)

Coarse-to-fine prolongation by bilinear interpolation. If nf is the fine-grid dimension, the coarse-grid solution is input as uc[0..nc-1][0..nc-1], where $\mathtt { n c } = \mathtt { n f } / 2 + 1$ . The finegrid solution is returned in uf[0..nf-1][0..nf-1].   
{   
Int nf $=$ uf.nrows();   
Int nc=nf/2+1;   
for (Int $\scriptstyle { \mathrm { j } } \subset = 0$ ;jc<nc;jc $^ { + + }$ ) Do elements that are copies. for (Int ic=0;ic<nc;ic $^ { + + }$ ) uf[2\*ic][2\*jc] $=$ uc[ic][jc];   
for (Int $\scriptstyle { \mathrm { j } } ^ { \mathbf { f } = 0 }$ ;jf<nf;jf $\scriptstyle + = 2$ ) Do even-numbered columns, interpolating verfor (Int iif ${ = } 1$ ;iif<nf-1;iif $+ { = } 2$ ) tically. uf[iif][jf] ${ = } 0$ .5\*(uf[iif+1][jf]+uf[iif-1][jf]);   
for (Int jf=1;jf<nf-1;jf $\scriptstyle + = 2$ ) Do odd-numbered columns, interpolating horizontally.

for (Int iif ${ = } 0$ ;iif<nf;iif $^ { + + }$ ) uf[iif][jf] ${ = } 0$ . $^ { 5 \ast }$ (uf[iif][jf $^ +$ 1]+uf[iif][jf-1]);

# Doub anorm2(MatDoub_I &a)

Returns the Euclidean norm of the matrix a[0..n-1][0..n-1]. {

Doub sum $_ { = 0 }$ .0;   
Int $\mathtt { n } = \mathtt { a }$ .nrows();   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) for (Int $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) sum $+ =$ a[i][j]\*a[i][j];   
return sqrt(sum)/n;

# }

# void mg(const Int j, MatDoub_IO &u, MatDoub_I &rhs, NRvector<NRmatrix<Doub> \*> &rho, Doub &trerr)

Recursive multigrid iteration. On input, j is the current level and u is the current value of the solution. For the first call on a given level, the right-hand side is zero, and the argument rhs is dummy. This is signaled by inputting trerr positive. Subsequent recursive calls supply a nonzero rhs as in equation (20.6.33). This is signaled by inputting trerr negative. rho is the vector of pointers to $\rho$ on each level. On output u contains the improved solution at the current level. When the first call on a given level is made, the relative truncation error $\tau$ is returned in trerr.

const Int NPR $\scriptstyle \sum 1$ ,NPOST=1;   
Number of relaxation sweeps before and after the coarse-grid correction is computed.   
const Doub ALPHA $\mathtt { \mathtt { = 0 } }$ .33; Relates the estimated truncation error to the   
Doub dum=-1.0; norm of the residual.   
Int nf $= \mathtt { u }$ .nrows();   
Int nc $=$ (nf+1)/2;   
MatDoub temp(nf,nf);   
if (j $\scriptstyle = = 0$ ) { Bottom of V: Solve on coarsest grid. matadd(rhs,\*rho[j],temp); slvsm2(u,temp);   
} else { On downward stoke of the V. MatDoub v(nc,nc),ut(nc,nc),tau(nc,nc),tempc(nc,nc); for (Int jpr ${ \tt > } 0$ ;jpre<NPRE;jpre++) { Pre-smoothing. if (trerr $<$ 0.0) { matadd(rhs,\*rho[j],temp); relax2(u,temp); } else relax2(u,\*rho[j]); } rstrct(ut,u); $\mathcal { R } \widetilde { u } _ { h }$ . v=ut; Make a copy in $\mathtt { v }$ . lop(tau,ut); $\mathcal { L } _ { H } ( \mathcal { R } \widetilde { u } _ { h } )$ stored temporarily in $\widetilde { \tau } _ { h }$ . lop(temp,u); $\mathcal { L } _ { h } ( \widetilde { u } _ { h } )$ . if (trerr < 0.0) $\mathcal { L } _ { h } ( \widetilde { \boldsymbol { u } } _ { h } ) - \mathcal { f } _ { h }$ . matsub(temp,rhs,temp); rstrct(tempc,temp); $\begin{array} { r l } & { \mathcal { R L } _ { h } ( \widetilde { u } _ { h } ) - f _ { H } . } \\ & { \widetilde { \tau } _ { h } + f _ { H } = \mathcal { L } _ { H } ( \mathcal { R } \widetilde { u } _ { h } ) - \mathcal { R L } _ { h } ( \widetilde { u } _ { h } ) + f _ { H } . } \end{array}$ matsub(tau,tempc,tau); if (trerr $>$ 0.0) trerr ALPHA\*anorm2(tau); Estimate truncation error $\tau$ . mg(j-1,v,tau,rho,dum); Recursive call for the coarse-grid correction. matsub(v,ut,tempc); On upward stroke of $\vee$ , form $\widetilde { u } _ { h } ^ { \mathrm { n e w } } = \widetilde { u } _ { h } +$ interp(temp,tempc); $\mathcal { P } ( \widetilde { u } _ { H } - \mathcal { R } \widetilde { u } _ { h } )$ . matadd(u,temp,u); for (Int jpost ${ = } 0$ ;jpost<NPOST;jpost $^ { + + }$ ) { Post-smoothing. if (trerr $<$ 0.0) { matadd(rhs,\*rho[j],temp); relax2(u,temp); }

else relax2(u,\*rho[j]); } } } };

# CITED REFERENCES AND FURTHER READING:

Brandt, A. 1977, “Multilevel Adaptive Solutions to Boundary-Value Problems,” Mathematics of Computation,vol. 31,pp.333-390.[1]   
Brandt, A. 1982, in Multigrid Methods, W. Hackbusch and U. Trottenberg, eds. (Springer Lecture Notes in Mathematics No. 960) (New York: Springer).[2]   
Hackbusch, W. 1985, Multi-Grid Methods and Applications (New York: Springer).[3]   
Stuben, K., and Trottenberg, U. 1982, in Multigrid Methods, W. Hackbusch and U. Trottenberg, eds. (Springer Lecture Notes in Mathematics No. 960) (New York: Springer), pp. 1–176.[4]   
Briggs, W.L., Henson, V.E., and McCormick, S. 2000, A Multigrid Tutorial (Cambridge, UK: Cambridge University Press).[5]   
Trottenberg, U., Oosterlee, C.W., and Schuller, A. 2001, Multigrid (Cambridge, MA: Academic Press).[6]   
McCormick, S., and Rude, U., eds. 2006, “Multigrid Computing,” special issue of Computing in Science and Engineering,vol.8,No.6 (November/December),pp.10-62.   
Hackbusch, W., and Trottenberg, U. (eds.) 1991, Multigrid Methods III (Basel: Birkhäuser).   
Wesseling, P. 1992, An Introduction to Multigrid Methods (New York: Wiley); corrected reprint 2004 (Philadelphia: R.T. Edwards).

# 20.7 Spectral Methods

Spectral methods are a very powerful tool for solving PDEs. When they can be used, they are the method of choice if you need high spatial resolution in multidimensions. For a second-order accurate finite difference code in three dimensions, increasing the resolution by a factor of 2 in each dimension requires eight times as many grid points, and improves the error typically by a factor of 4. In a spectral code, a similar increase in resolution often gives an improvement of a factor of $1 0 ^ { 6 }$ . Even for one-dimensional problems, spectral methods will amaze you with their power and efficiency.

Spectral methods work well for smooth solutions. Discontinuities like shocks are bad — don’t even try spectral methods. Even mild nonsmoothness (like a discontinuity in some high-order derivative of the solution) can spoil the convergence of spectral methods. (Actually, getting spectral methods to work with discontinuities and shocks is an active research area; see [1] for an introduction.)

The key difference between finite difference methods and spectral methods is that in finite difference methods you approximate the equation you are trying to solve, whereas in spectral methods you approximate the solution you are trying to find. While finite differencing replaces the continuum equation by an equation on grid points, a spectral method expresses the solution as a truncated expansion in a set

of basis functions:

$$
f ( x ) \simeq f _ { N } ( x ) = \sum _ { n = 0 } ^ { N } a _ { n } \phi _ { n } ( x )
$$

Different choices of basis functions and methods of computing $a _ { n }$ give different flavors of spectral methods.

# 20.7.1 Example

We illustrate the idea of spectral methods with an example. Consider the onesided wave equation (advective equation) in one dimension:

$$
{ \frac { \partial u } { \partial t } } = { \frac { \partial u } { \partial x } }
$$

with periodic boundary conditions on $[ 0 , 2 \pi ]$ and initial condition

$$
u ( t = 0 , x ) = f ( x )
$$

You get the analytic spectral solution by expanding $u$ in a Fourier series,

$$
u ( t , x ) = \sum _ { n = - \infty } ^ { \infty } a _ { n } ( t ) e ^ { i n x }
$$

Substituting this expansion into equation (20.7.2) gives

$$
{ \frac { d a _ { n } } { d t } } = i n a _ { n }
$$

with solution

$$
a _ { n } ( t ) = a _ { n } ( 0 ) e ^ { i n t }
$$

You get $a _ { n } ( 0 )$ from the initial condition: Expand

$$
f ( x ) = \sum _ { n = - \infty } ^ { \infty } f _ { n } e ^ { i n x }
$$

from which you see that

$$
a _ { n } ( 0 ) = f _ { n }
$$

For example, suppose

$$
f ( x ) = \sin ( \pi \cos x )
$$

which gives the analytic solution

$$
u ( t , x ) = \sin [ \pi \cos ( x + t ) ]
$$

The spectral coefficients in the solution (20.7.4) are

$$
\begin{array} { c } { \displaystyle a _ { n } ( 0 ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \sin ( \pi \cos x ) e ^ { - i n x } d x } \\ { = ( - 1 ) ^ { ( n - 1 ) / 2 } J _ { n } ( \pi ) , \qquad n \mathrm { o d d } } \end{array}
$$

In a numerical version of this spectral solution, we would truncate the expansion at $n = N$ . How well does $u _ { N } ( t , x )$ approximate the exact solution? One measure is the root-mean-square error,

$$
\begin{array} { l } { { \displaystyle { \cal L } _ { 2 } = \left[ \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \left| u ( t , x ) - u _ { N } ( t , x ) \right| ^ { 2 } d x \right] ^ { 1 / 2 } } } \\ { { \displaystyle ~ = \left[ \frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } \left| \sum _ { | n | > N } a _ { n } ( 0 ) e ^ { i n x } e ^ { i n t } \right| ^ { 2 } d x \right] ^ { 1 / 2 } } } \\ { { \displaystyle ~ = \left[ \sum _ { | n | > N } | a _ { n } ( 0 ) | ^ { 2 } \right] ^ { 1 / 2 } } } \end{array}
$$

Now $J _ { n } ( \pi )$ goes to zero exponentially as $n  \infty$ , so the error decreases exponentially with $N$ for any $t \geq 0$ . This is the key feature of a good spectral method, one you should always strive for. By contrast, a second-order finite difference method has an error that scales as $1 / N ^ { 2 }$ .

This exponential convergence of spectral methods sets in when one has resolved the main features of the solution. In the above example, the Bessel functions go rapidly to zero once $n \gtrsim \pi$ , which corresponds to having about $\pi$ basis functions per wavelength. On can show that this is a general property of spectral methods [2]. By contrast, second-order accurate finite differencing needs about 20 points per wavelength for $1 \%$ accuracy [2]. Moreover, once the solution is resolved, the accuracy improves much more quickly with spectral methods.

There are three properties of the functions $e ^ { i n x }$ that are crucial for this analytic spectral solution, which is just the separation of variables technique:

1. They are a complete set of basis functions.   
2. Each basis function by itself obeys the boundary conditions.   
3. They are eigenfunctions of the operator in the problem, $d / d x$ .

As we’ll see, only property 1 is essential for numerical spectral methods. Spectral methods are not limited to Fourier series — a wide choice of basis functions can be used.

# 20.7.2 Choice of Basis Functions

You can’t simply use Fourier series as basis functions for all problems — it depends on the boundary conditions. Here is a recipe that will take care of $9 9 \%$ o f cases you’ll encounter:

- If the solution is periodic, use Fourier series.   
- If the solution is not periodic and the domain is a square or a cube, or can be mapped to a rectangular region by a simple coordinate transformation, use Chebyshev polynomials along each dimension. If the domain is spherical, use spherical harmonics for the angles. In the radial direction, use Chebyshev polynomials for a spherical shell. For a sphere that includes the origin, use the radial basis functions in [8]. These incorporate the correct analytic behavior at the origin and are much better than other choices. They can also be used for cylindrical domains. If the domain is infinite, consult [9,10,4].

Expansions based on for example Chebyshev or Legendre polynomials have the property that their convergence rate is governed by the smoothness of the solution only, not the boundary conditions it satisfies. Fourier expansions, on the other hand, require periodic boundary conditions as well as smoothness for rapid convergence. (These properties are proved, e.g., in [2]. The key point is that basis functions whose convergence rate is independent of the boundary conditions are solutions of singular Sturm-Liouville equations.) It is this independence from the details of the boundary conditions that makes basis functions like Chebyshev polynomials “magical.”

Another reason for the popularity of Chebyshev polynomials is that they are really just trigonometric functions whose argument $\theta$ has been mapped by $x = \cos \theta$ :

$$
T _ { n } ( x ) = \cos ( n \theta ) , \qquad x = \cos \theta
$$

Thus an expansion in Chebyshev polynomials can be evaluated efficiently by the FFT. Moreover, the derivatives of such an expansion can also be evaluated by FFT techniques, as discussed below.

For spherical domains, spherical harmonics are products of Legendre functions in cos $\theta$ and Fourier series in $\phi$ . Once again one gets exponential convergence for smooth functions.

# 20.7.3 Computing the Expansion Coefficients

How do we compute the $a _ { n }$ ? There are three basic ways, which can be compared by considering the residual when the expansion (20.7.1) is substituted into the equation you are trying to solve:

1. Tau method. Here we require that the $a _ { n }$ be computed so that the boundary conditions are satisfied, and that the residual be orthogonal to as many of the basis functions as possible.   
2. Galerkin method. In this case you combine the basis functions into a new set, each of which satifies the boundary conditions. Then make the residual orthogonal to as many of the new basis functions as possible. (This is essentially what you do when you separate variables in solving a PDE, as we did for equation 20.7.2. Usually you start with basis functions that already satisfy the boundary conditions individually.)   
3. Collocation or pseudospectral method. As in the tau method, require the boundary conditions to be satisfied, but make the residual zero at a set of suitably chosen points.

As we will see, the pseudospectral method has an alternative interpretation that makes it very easy to use. Accordingly, we will only discuss this method, leaving the others to the references.

The big advantage of the pseudospectral method is that it is easy to implement for nonlinear problems. Instead of working with the spectral coefficients, as with the other two methods, you work with the values of the solution at the special grid points associated with the basis functions (typically, the Gaussian quadrature points). These are called the collocation points. Often we say we are working with the solution in physical space as opposed to in spectral space.

A pseudospectral method is an interpolating method: Think of the representation

$$
y ( x ) = \sum _ { n = 0 } ^ { N } a _ { n } \phi _ { n } ( x )
$$

as a polynomial that interpolates the solution. Require this interpolating polynomial to be exactly equal to the solution at the $N + 1$ collocation points. If we do things right, then as $N  \infty$ , the errors in between the points tend to zero exponentially fast.

# 20.7.4 Spectral Methods and Gaussian Quadrature

Recall the formula for Gaussian quadrature (-4.6.1):

$$
\int _ { a } ^ { b } y ( x ) w ( x ) d x \approx \sum _ { i = 0 } ^ { N } w _ { i } y ( x _ { i } )
$$

Here $w ( x )$ is the so-called weight function that typically factors out some singular behavior of the integrand, leaving $y ( x )$ as a smooth function. The formula is derived by choosing the $2 N + 2$ weights and abscissas, $w _ { i }$ and $x _ { i }$ , by requiring that the formula be exact for the polynomials $1 , x , x ^ { 2 } , \ldots , x ^ { 2 N + 1 }$ . (Don’t be confused by the notation: There is no direct relationship between $w _ { i }$ and $w ( x )$ .) As shown in $\ S 4 . 6$ , Gaussian quadrature is related to the orthogonal polynomials $\phi _ { n } ( x )$ with the given weight function:

$$
\langle \phi _ { n } | \phi _ { m } \rangle \equiv \int _ { a } ^ { b } \phi _ { n } ( x ) \phi _ { m } ( x ) w ( x ) d x = \delta _ { m n }
$$

The abscissas $x _ { i }$ turn out to be the $N + 1$ roots of $\phi _ { N + 1 } ( x )$ , and the weights $w _ { i }$ are given by equation (4.6.9).

We can use Gaussian quadrature to define the discrete inner product of two functions:

$$
\langle f \vert g \rangle _ { \mathrm { G } } \equiv \sum _ { i = 0 } ^ { N } w _ { i } f ( x _ { i } ) g ( x _ { i } )
$$

Here the subscript $\mathbf { G }$ stands for Gaussian.

An important property of Gaussian quadrature is the discrete orthogonality relation

$$
\langle \phi _ { n } | \phi _ { m } \rangle _ { \mathrm { G } } = \delta _ { m n } , \qquad m + n \leq 2 N + 1
$$

Proof: Equation (20.7.18) is the Gaussian quadrature version of equation (20.7.16). By assumption, the integrand $\phi _ { n } ( x ) \phi _ { m } ( x )$ of equation (20.7.16) is a polynomial of degree $m + n \le 2 N + 1$ . But Gaussian quadrature is arranged to integrate polynomials of degree $\leq 2 N + 1$ exactly. QED.

Now suppose we approximate $y ( x )$ by the pseudospectral interpolating polynomial

$$
P _ { N } ( x ) = \sum _ { n = 0 } ^ { N } \overline { { { a } } } _ { n } \phi _ { n } ( x )
$$

where the collocation points are chosen to be the Gaussian quadrature points:

$$
P _ { N } ( x _ { i } ) = y ( x _ { i } ) , \qquad i = 0 , 1 , \dots , N
$$

This is always possible, since the interpolating polynomial through $N + 1$ points is a polynomial of degree $N$ , and the functions up to $\phi _ { N } ( x )$ are a basis for such polynomials. The perhaps unexpected result is that the coefficients $\left\{ \overline { { a } } _ { n } \right\}$ of the expansion (20.7.19) are given exactly by the Gaussian quadrature

$$
\overline { { a } } _ { n } = \langle y | \phi _ { n } \rangle _ { \mathrm { G } }
$$

To see this, take the discrete inner product of both sides of equation (20.7.19) with $\phi _ { m }$ :

$$
\langle P _ { N } | \phi _ { m } \rangle _ { \mathrm { G } } = \sum _ { n = 0 } ^ { N } \overline { { { a } } } _ { n } \langle \phi _ { n } | \phi _ { m } \rangle _ { \mathrm { G } }
$$

If we use the discrete orthogonality relation (20.7.18), the right-hand side evaluates to $\overline { { a } } _ { m }$ . On the left-hand side, we can replace $P _ { N } ( x _ { i } )$ in the Gaussian quadrature by $y ( x _ { i } )$ since $P _ { N }$ is the interpolating polynomial. Hence the result follows.

Now comes the key point. The actual spectral expansion of $y ( x )$ is

$$
y ( x ) = \sum _ { n = 0 } ^ { \infty } a _ { n } \phi _ { n } ( x )
$$

where the exact spectral coefficients are

$$
a _ { n } = \langle y | \phi _ { n } \rangle = \int _ { a } ^ { b } y ( x ) \phi _ { n } ( x ) w ( x ) d x
$$

The pseudospectral expansion coefficients $\overline { { a } } _ { n }$ are the exact expansion coefficients of $P _ { N } ( x )$ , the interpolating polynomial (20.7.19). The relation between the exact spectral coefficients and the pseudospectral expansion coefficients follows from equation (20.7.21):

$$
\begin{array} { l } { { \displaystyle \overline { { { a } } } _ { n } = \langle y | \phi _ { n } \rangle _ { \mathrm { G } } } } \\ { { \displaystyle \quad = \sum _ { m = 0 } ^ { \infty } a _ { m } \langle \phi _ { m } | \phi _ { n } \rangle _ { \mathrm { G } } \qquad \mathrm { ( u s i n g ~ e q u a t i o n ~ 2 0 . 7 . 2 3 ) } } } \\ { { \displaystyle \quad = \sum _ { m = 0 } ^ { N } a _ { m } \langle \phi _ { m } | \phi _ { n } \rangle _ { \mathrm { G } } + \sum _ { m > N } a _ { m } \langle \phi _ { m } | \phi _ { n } \rangle _ { \mathrm { G } } } } \\ { { \displaystyle \quad = a _ { n } + \sum _ { m > N } a _ { m } \langle \phi _ { m } | \phi _ { n } \rangle _ { \mathrm { G } } } } \end{array}
$$

Thus, since for large $N$ the exact spectral coefficients give an exponentially good approximation to $y ( x )$ , so do the pseudospectral coefficients. By the way, this is the reason for the name pseudospectral method: We use coefficients that are not the actual spectral coefficients, but are very close to them. From now on we won’t bother to distinguish between the two sets of coefficients; we just write $a _ { n }$ for either $a _ { n }$ or ${ \overline { { a } } } _ { n }$ .

The Gaussian quadrature collocation points, the roots of $\phi _ { N + 1 } ( x )$ , all lie inside the interval $( a , b )$ , away from the endpoints. There is another version of Gaussian quadrature that includes the two endpoints of the interval. This is called Gauss-Lobatto quadrature, and the collocation points are the Gauss-Lobatto points (-4.6.4). These points are as effective as the ordinary Gaussian points, and are more convenient when you need to impose boundary conditions at the endpoints.

As a slight digression, you may be under the mistaken impression that the only advantage of Gaussian integration over integration with equally spaced points is that its degree of exactness is $2 N + 1$ as opposed to $N$ , the maximum you can get with only the $N + 1$ weights at your disposal. In fact, however, the main advantage of Gaussian integration is that it converges exponentially with $N$ for smooth functions. You can see this explicitly from the above formulas by setting $m = 0$ in equation (20.7.21):

$$
\overline { { a } } _ { 0 } = \phi _ { 0 } \sum _ { i = 0 } ^ { N } w _ { i } y ( x _ { i } )
$$

where $\phi _ { 0 }$ is a constant. But this converges exponentially to the expression given by equation (20.7.24):

$$
a _ { 0 } = \phi _ { 0 } \int _ { a } ^ { b } y ( x ) w ( x ) d x
$$

as claimed.

How do Fourier series fit into this discussion? After all, the collocation points are equally spaced (usually $x _ { j } = 2 \pi j / N$ , $j = 0 , \ldots , N - 1 )$ . But in fact these are the correct collocation points if we think of Fourier series as interpolating $y ( x )$ by a trigonometric polynomial. The corresponding Gaussian quadrature (using the equally spaced points) is the midpoint rule, and the Gauss-Lobatto quadrature, which includes the endpoints, is the trapezoidal rule. The textbooks tell you that the midpoint and trapezoidal rules are low-order methods. This is true for arbitrary functions. But if you apply them to periodic functions (-5.8.1), or functions that go rapidly to zero at infinity $\ S 4 . 5$ and $\ S 1 3 . 1 1 )$ , they are in fact exponentially convergent, like any self-respecting Gaussian quadrature method should be.

# 20.7.5 Cardinal Functions

You can write any polynomial interpolation formula for a function $f ( x )$ as

$$
P _ { N } ( x ) = \sum _ { i = 0 } ^ { N } f ( x _ { i } ) C _ { i } ( x )
$$

where the $C _ { i } ( x )$ are called cardinal functions. They are polynomials of degree $N$ that satisfy

$$
C _ { i } ( x _ { j } ) = \delta _ { i j }
$$

i.e., $C _ { i } ( x )$ is 1 at the $i$ th collocation point and 0 at all the others.

One explicit representation of cardinal functions comes from the formula for Lagrange interpolation (see equation 3.2.1):

$$
C _ { i } ( x ) = \prod _ { j = 0 \atop j \not = i } ^ { N } { \frac { x - x _ { j } } { x _ { i } - x _ { j } } }
$$

If you substitute this in equation (20.7.28), it is just the Lagrange interpolation formula. Each choice of basis functions implies a corresponding choice of collocation points $x _ { j }$ , and so a corresponding choice of cardinal functions by equation (20.7.30).

There are other equivalent ways of writing $C _ { i } ( x )$ . For example, if $\phi _ { n } ( x )$ is a set of orthogonal polynomials, and the collocation points are the zeros of $\phi _ { N + 1 } ( x )$ (Gaussian quadrature points), then $C _ { i } ( x )$ is almost $\phi _ { N + 1 } ( x )$ , except $\phi _ { N + 1 } ( x )$ vanishes at all the grid points. Since near $x = x _ { i }$

$$
\phi _ { N + 1 } ( x ) = \phi _ { N + 1 } ( x _ { i } ) + ( x - x _ { i } ) \phi _ { N + 1 } ^ { \prime } ( x _ { i } ) + \cdot \cdot \cdot
$$

we get the cardinal function by dividing out the zero at $x = x _ { i }$ :

$$
C _ { i } ( x ) = \frac { \phi _ { N + 1 } ( x ) } { ( x - x _ { i } ) \phi _ { N + 1 } ^ { \prime } ( x _ { i } ) }
$$

In practice you don’t need to know any of the formulas like equations (20.7.30) or (20.7.32). The books in the references have formulas for the $C _ { i } ( x )$ for all the standard basis functions if you are curious. What you do need are the derivatives of the cardinal functions, the differentiation matrices (see below).

You might be nervous about using very high-order polynomial interpolation to represent your solution, especially if you’ve ever encountered the Runge phenomenon: If the grid points are equally spaced, then the error in $P _ { N } ( x )$ can tend to infinity as $N  \infty$ . What happens is that the error shows up near the endpoints of the interval — the middle is fine. The fix is to make the points more concentrated toward the endpoints, which is exactly what choosing the Gaussian points does. This is the same reason why Chebyshev approximation often works when polynomial approximation fails, as was discussed in $\ S 5 . 8 . 1$ .

# 20.7.6 Spectral vs. Grid Point Representation

Let’s contrast the representations of the solution of

$$
\mathcal { L } y = f
$$

in spectral space and in physical space. Assume that $\mathcal { L }$ is a linear differential operator for simplicity.

# Spectral Space

# Physical Space

$$
\begin{array} { c c } { { y ( x ) = \displaystyle \sum _ { n = 0 } ^ { N } a _ { n } \phi _ { n } ( x ) } } & { { \qquad y ( x ) = \displaystyle \sum _ { j = 0 } ^ { N } y _ { j } C _ { j } ( x ) } } \\ { { \displaystyle \sum _ { n = 0 } ^ { N } a _ { n } \mathscr { L } \phi _ { n } ( x ) = f ( x ) } } & { { \qquad \displaystyle \sum _ { j = 0 } ^ { N } y _ { j } \mathscr { L } C _ { j } ( x ) = f ( x ) } } \end{array}
$$

Impose at collocation points only:

$$
\sum _ { n = 0 } ^ { N } a _ { n } \mathcal { L } \phi _ { n } ( x _ { j } ) = f ( x _ { j } ) \qquad \sum _ { j = 0 } ^ { N } y _ { j } \mathcal { L } C _ { j } ( x _ { i } ) = f ( x _ { i } )
$$

i.e., $L a = f ,$ where $L _ { j n } = \mathcal { L } \phi _ { n } ( x _ { j } )$ i.e., $L ^ { ( c ) } y = f ,$ where $L _ { i j } ^ { ( c ) } = \mathcal { L } C _ { j } ( x _ { i } )$

The two representations are related as follows: To go from grid point values to spectral coefficients you project $y ( x )$ along each basis function:

$$
{ \begin{array} { r l } { a _ { i } = \left. \phi _ { i } \mid y \right. } \\ { \ } & { = \sum _ { j } w _ { j } \phi _ { i } ( x _ { j } ) y _ { j } \qquad { \mathrm { ( d o i n g ~ t h e ~ i n t e g r a l ~ b y ~ G a u s s i a n ~ q u a d r a t u r e ) } } } \end{array} }
$$

That is,

$$
\begin{array} { r } { { \bf { a } } = { \bf { M } } \cdot { \bf { y } } , \qquad \mathrm { w h e r e } \quad M _ { i j } = \phi _ { i } ( x _ { j } ) w _ { j } } \end{array}
$$

Thus the relation in spectral space $\mathbf { L } \cdot \mathbf { a } = \mathbf { f }$ becomes $\mathbf { L } \cdot \mathbf { M } \cdot \mathbf { y } = \mathbf { f }$ . But in physical space $\mathbf { L } ^ { \left( c \right) } \cdot \mathbf { y } = \mathbf { f }$ , so

$$
\mathbf { L } ^ { \left( c \right) } = \mathbf { L } \cdot \mathbf { M }
$$

with inverse

$$
\mathbf { L } = \mathbf { L } ^ { ( c ) } \cdot \mathbf { M } ^ { - 1 }
$$

Note also that equation (20.7.35) implies

$$
\mathbf { y } = \mathbf { M } ^ { - 1 } \cdot \mathbf { a }
$$

Since $\begin{array} { r } { y = \sum a _ { n } \phi _ { n } } \end{array}$ , we see that ${ \bf { M } } ^ { - 1 }$ is the matrix that sums the spectral series to get the grid point values, i.e.,

$$
M _ { i j } ^ { - 1 } = \phi _ { j } ( x _ { i } )
$$

You can check that these relations are all consistent:

$$
\begin{array} { l } { { ( { \bf M } \cdot { \bf M } ^ { - 1 } ) _ { i j } = \displaystyle \sum _ { k } M _ { i k } M _ { k j } ^ { - 1 } } } \\ { { \displaystyle \qquad = \sum _ { k } [ \phi _ { i } ( x _ { k } ) w _ { k } ] [ \phi _ { j } ( x _ { k } ) ] } } \\ { { \displaystyle \qquad = \langle \phi _ { i } | \phi _ { j } \rangle _ { \mathrm { G } } } } \\ { { \displaystyle \qquad = \delta _ { i j } \qquad \quad \mathrm { ( b y ~ d i s c r e t e ~ o r t h o g o n a l i t y ) } } } \end{array}
$$

In practice, the transformations (20.7.35) and (20.7.38) are often done with FFTs for Fourier or Chebyshev basis functions if $N$ is large. For simple programs, just do matrix multiplication.

# 20.7.7 Differentiation Matrices

We’ve seen above that the key ingredient in the pseudospectral method is to form

$$
L _ { i j } ^ { ( c ) } = \mathcal { L } C _ { j } ( x _ { i } )
$$

which involves taking derivatives of the cardinal functions at the collocation points. Consider the first derivative $\partial _ { x }$ . You then need the matrix

$$
D _ { i j } ^ { ( 1 ) } = \partial _ { x } C _ { j } ( x _ { i } )
$$

This quantity can be computed ahead of time and stored. Then, to compute the vector of first derivatives at the grid points, just do a matrix multiplication:

$$
\begin{array} { r c l } { \frac { \partial y } { \partial x } } & { \displaystyle \longleftrightarrow } & { \displaystyle \sum _ { j = 0 } ^ { N } D _ { i j } ^ { ( 1 ) } y _ { j } } \end{array}
$$

Similarly one can define the second derivative matri x D.2/ , and so on.

The matrix multiplication in equation (20.7.43) requires $O ( N ^ { 2 } )$ operations. For Fourier basis functions $e ^ { i k x }$ , one can compute the derivative alternatively as follows:

$$
{ \begin{array} { r l } { y } & { { \xrightarrow { \operatorname { F F T } } } \quad a } \\ { a } & { \longrightarrow \quad i k a } \\ { i k a } & { { \xrightarrow { \operatorname { i n v e r s e } \operatorname { F F T } } } \quad y ^ { \prime } } \end{array} }
$$

For Chebyshev basis functions, there is a simple $O ( N )$ recurrence relation in the middle step to get the coefficients for the derivative from the coefficients for the function (see equation 5.9.2). Thus the procedure is ${ \cal O } ( N \log N )$ . However, it is typically faster than the $O ( N ^ { 2 } )$ matrix multiplication only for $N \gtrsim 1 6 - 1 2 8$ , depending on the computer. So just use matrix multiplication for simple programs.

It is worth pointing out that this idea of using recurrence relations to evaluate operators in spectral space is much more general than the simple example of derivatives of Chebyshev functions. It is important for efficient production codes when the operators consist of derivatives times simple powers of the coordinates. See the references for details.

# 20.7.8 Computing Differentiation Matrices

There are several options for computing differentiation matrices:

1. Derive the formulas by differentiating the Lagrange polynomial representation (20.7.30).   
2. Differentiate the basis function representation (20.7.32).   
3. Look up the explicit formulas that have been derived for the various basis functions in books, e.g. Chapter 2 of [3].   
4. Use the routine given below, based on the routine in [6]. This algorithm computes any order of differentiation matrix given only a set of collocation points $\{ x _ { i } \}$ .

Obviously, the last choice is the easiest. However, it does have the potential drawback for high-precision work that roundoff error can be larger than necessary. If this is a problem, see [7].

# void weights(const Doub z, VecDoub_I &x, MatDoub_O &c)

Compute the differentiation matrices for pseudospectral collocation. Input are $_ { z }$ , the location where the matrices are to be evaluated, and $\mathbf { x } \left[ 0 \ldots \ldots \right]$ , the set of $\mathtt { n } { + } 1$ grid points. On output, c[0..n][0..m] contains the weights at grid locations $\mathbf { x } \left[ 0 \ldots \ldots \right]$ for derivatives of order 0..m. The element c[j][k] contains the weight to be applied to the function value at $\mathbf { x } \left[ \mathrm { j } \right]$ when the kth derivative is approximated by the set of $n + 1$ collocation points $\mathbf { x }$ . Note that the elements of the zeroth derivative matrix are returned in $\mathtt { c } [ 0 \cdot \mathtt { \lrcorner n } ]$ [0]. These are just the values of the cardinal functions, i.e., the weights for interpolation.

Int $\mathrm { n } { = } \mathrm { c }$ .nrows()-1;   
Int $\mathtt { m } = \mathtt { c }$ .ncols()-1;   
Doub $\mathtt { c 1 } = 1$ .0;   
Doub $\mathtt { c 4 } \mathtt { = x }$ [0]-z;   
for (Int $\mathtt { k } = 0$ ;k<=m;k++) for (Int j=0;j<=n;j++) c[j][k]=0.0;   
c[0][0] $= 1$ .0;   
for (Int $\dot { \bar { 1 } } = 1$ ; $\mathrm { i } < = \mathrm { n }$ ;i++) { Int mn=MIN(i,m);

Doub $^ { c 2 = 1 }$ .0; Doub $c 5 { = } c 4$ ; $\mathtt { c 4 } \mathtt { = x }$ [i]-z; for (Int j=0;j<i;j++) { Doub c3=x[i]-x[j]; $_ { \mathtt { C } 2 = \mathtt { C } 2 * \mathtt { C } 3 }$ ; if ${ \mathrm { ( j ~ } } = = { \mathrm { ~ i - 1 } } { \mathrm { ) } }$ ) { for (Int k=mn;k>0;k--) c[i][k] $=$ c1\*(k\*c[i-1][k-1]-c5\*c[i-1][k])/c2; c[i][0] $=$ -c1\*c5\*c[i-1][0]/c2; } for (Int k=mn;k>0;k--) c[j][k] $=$ (c4\*c[j][k]-k\*c[j][k-1])/c3; c[j][0] $=$ c4\*c[j][0]/c3; } $\mathtt { c 1 } = \mathtt { c 2 }$ ; } }

Typical usage of the weights routine to compute first- and second-order derivative matrices is

VecDoub $\mathbf { x } ( \mathtt { n } )$ ;   
MatDoub c(n,3),d1(n,n),d2(n,n);   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j++) x[j] $=$ ...   
for ( $\scriptstyle \dot { 1 } = 0$ ;i<n;i++) { weights(x[i],x,c); for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j $^ { + + }$ ) { d1[i][j] $= \mathtt { c }$ [j][1]; d2[i][j] $= \mathtt { c }$ [j][2]; }   
}

# 20.7.9 A Note on Interpolation

Often you want to evaluate the solution at points that are not the collocation points. This requires an interpolation. To preserve the full spectral accuracy, you want to use all the information in the solution. However, it is not necessary to transform the solution to spectral space and then evaluate the representation (20.7.1) at the desired point, e.g., by Clenshaw’s method. Just use the interpolation formula (20.7.28). A simple way to do this is to use the above routine, which will return the interpolation weights $C _ { i } ( \boldsymbol { x } _ { k } )$ for any set of target points $x _ { k }$ when m, the second dimension of c in the code, is zero. So interpolating to a set of points can again be done as a matrix multiplication.

# 20.7.10 Pseudospectral Collocation as a Finite Difference Method

Consider finite difference approximations for $d / d x$ at the center of an equally spaced grid, for example

$$
\begin{array} { r l r } {  { h f ^ { \prime } ( x ) = - { \frac { 1 } { 2 } } f ( x - h ) + { \frac { 1 } { 2 } } f ( x + h ) + O ( h ^ { 2 } ) } } \\ & { } & { \quad = { \frac { 1 } { 1 2 } } f ( x - 2 h ) - { \frac { 2 } { 3 } } f ( x - h ) + { \frac { 2 } { 3 } } f ( x + h ) - { \frac { 1 } { 1 2 } } f ( x + 2 h ) + O ( h ^ { 4 } ) } \\ & { } &  \quad = \quad \cdots \qquad ( 2 0 \ \end{array}
$$

For centered differences like these, the limit as $N  \infty$ of the weights (coefficients of $f$ ) is finite. But for one-sided approximations, or partially one-sided approximations, the weights diverge [5]. Since one has to use such approximations near the endpoints of the grid, it’s not surprising that high-order finite difference approximations have large errors near the boundaries.

But suppose the grid points are not equally spaced. In particular, suppose they are closer together near the endpoints, like the Gaussian quadrature points. Then the finite difference approximation is convergent as $N \to \infty$ .

The pseudospectral method gives the exact derivative of the interpolating polynomial that passes through the data at the $N + 1$ grid points. You would get the same result for a finite difference method that uses all $N + 1$ grid points, This follows from the uniqueness of the interpolating polynomial, a polynomial of degree $N$ through all $N + 1$ points.

With this point of view, think of a pseudospectral method as a way to find high-order numerical approximations to derivatives at grid points. Then, just like finite difference methods, satisfy the equation you want to solve at the grid points.

# 20.7.11 Variable Coefficients and Nonlinearities

Suppose you have a term like $\sinh ( x ) y ( x )$ in your equation. No need to expand $\sinh ( x )$ in basis functions — just multiply $\sinh ( x )$ by $y$ at each collocation point. Similarly, nonlinear terms like $y ^ { 2 }$ are evaluated directly using the values at the collocation points. This is the big advantage over the tau and Galerkin methods — handling nonlinearities in physical space rather than spectral space is much easier.

# 20.7.12 A Worked Example

Here is a simple one-dimensional example, taken from Appendix B of [5]. Consider the equation

$$
\begin{array} { c } { { y ^ { \prime \prime } + y ^ { \prime } - 2 y + 2 = 0 , - 1 \leq x \leq 1 , } } \\ { { y ( - 1 ) = y ( 1 ) = 0 } } \end{array}
$$

The exact solution is

$$
y ( x ) = 1 - { \frac { e ^ { x } \sinh 2 + e ^ { - 2 x } \sinh 1 } { \sinh 3 } }
$$

Let’s make an expansion in Chebyshev polynomials with $N = 4$ :

$$
y = \sum _ { n = 0 } ^ { 4 } a _ { n } T _ { n } ( x )
$$

Choose the collocation points to be

$$
x _ { i } = - \cos { \frac { i \pi } { 4 } } , \qquad i = 0 , \dots , 4
$$

These are the Gauss-Lobatto points associated with Chebyshev polynomials, i.e., they include the endpoints. We always include the endpoints when we want to impose Dirichlet boundary conditions, that is, function values on the boundaries. Using

one of the methods for finding differentiation matrices, we get

$$
[ D ^ { ( 1 ) } y ] _ { i } = \left[ { \begin{array} { c c c c c } { - { \frac { 1 1 } { 2 } } } & { 4 + 2 { \sqrt { 2 } } } & { - 2 } & { 4 - 2 { \sqrt { 2 } } } & { - { \frac { 1 } { 2 } } } \\ { - 1 - { \frac { 1 } { 2 } } { \sqrt { 2 } } } & { { \frac { 1 } { 2 } } { \sqrt { 2 } } } & { { \sqrt { 2 } } } & { - { \frac { 1 } { 2 } } { \sqrt { 2 } } } & { 1 - { \frac { 1 } { 2 } } { \sqrt { 2 } } } \\ { { \frac { 1 } { 2 } } } & { - { \sqrt { 2 } } } & { 0 } & { { \sqrt { 2 } } } & { - { \frac { 1 } { 2 } } } \\ { - 1 + { \frac { 1 } { 2 } } { \sqrt { 2 } } } & { { \frac { 1 } { 2 } } { \sqrt { 2 } } } & { - { \sqrt { 2 } } } & { - { \frac { 1 } { 2 } } { \sqrt { 2 } } } & { 1 + { \frac { 1 } { 2 } } { \sqrt { 2 } } } \\ { { \frac { 1 } { 2 } } } & { - 4 + 2 { \sqrt { 2 } } } & { 2 } & { - 4 - 2 { \sqrt { 2 } } } & { { \frac { 1 1 } { 2 } } } \end{array} } \right] \left[ { \begin{array} { c } { y _ { 0 } } \\ { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \\ { y _ { 4 } } \end{array} } \right]
$$

and

$$
[ D ^ { ( 2 ) } y ] _ { i } = \left[ { \begin{array} { c c c c c } { 1 7 } & { - 2 0 - 6 { \sqrt { 2 } } } & { 1 8 } & { - 2 0 + 6 { \sqrt { 2 } } } & { 5 } \\ { 5 + 3 { \sqrt { 2 } } } & { - 1 4 } & { 6 } & { - 2 } & { 5 - 3 { \sqrt { 2 } } } \\ { - 1 } & { 4 } & { - 6 } & { 4 } & { - 1 } \\ { 5 - 3 { \sqrt { 2 } } } & { - 2 } & { 6 } & { - 1 4 } & { 5 + 3 { \sqrt { 2 } } } \\ { 5 } & { - 2 0 + 6 { \sqrt { 2 } } } & { 1 8 } & { - 2 0 - 6 { \sqrt { 2 } } } & { 1 7 } \end{array} } \right] \left[ { \begin{array} { l } { y _ { 0 } } \\ { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \\ { y _ { 4 } } \end{array} } \right]
$$

Requiring that the differential equation hold at the interior collocation points $x _ { k }$ , $k = 1 , 2 , 3$ , uses the middle three rows of these matrices. Enforcing the boundary conditions $y _ { 0 } = y _ { 4 } = 0$ means we don’t need the first and last columns. So equation (20.7.45) gives

$$
\left[ { \begin{array} { r r r } { - 1 6 + { \frac { 1 } { 2 } } { \sqrt { 2 } } } & { 6 + { \sqrt { 2 } } } & { - 2 - { \frac { 1 } { 2 } } { \sqrt { 2 } } } \\ { 4 - { \sqrt { 2 } } } & { - 8 } & { 4 + { \sqrt { 2 } } } \\ { - 2 + { \frac { 1 } { 2 } } { \sqrt { 2 } } } & { 6 - { \sqrt { 2 } } } & { - 1 6 - { \frac { 1 } { 2 } } { \sqrt { 2 } } } \end{array} } \right] \left[ { \begin{array} { r r r } { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \end{array} } \right] = \left[ { \begin{array} { r r r } { - 2 } \\ { - 2 } \\ { - 2 } \end{array} } \right]
$$

with solution

$$
{ \left[ \begin{array} { l } { y _ { 1 } } \\ { y _ { 2 } } \\ { y _ { 3 } } \end{array} \right] } = { \left[ \begin{array} { l } { { \frac { 1 0 1 } { 3 5 0 } } + { \frac { 1 3 } { 3 5 0 } } { \sqrt { 2 } } } \\ { \qquad { \frac { 1 3 } { 2 5 } } } \\ { { \frac { 1 0 1 } { 3 5 0 } } - { \frac { 1 3 } { 3 5 0 } } { \sqrt { 2 } } } \end{array} \right] }
$$

The exact solution (20.7.47) gives for example $y ( x = 0 ) = 0 . 5 2 0 6 5$ , compared with $y _ { 2 } = 0 . 5 2 0 0 0$ . Not bad for five grid points! The real point, however, is that the error is about $1 0 ^ { - 1 6 }$ for $N = 1 6$ . With a second-order finite difference scheme, the error would go down by only a factor of 10 or so with this increase in $N$ .

# 20.7.13 Multidimensional Spectral Methods

For a time-dependent problem, the simplest approach is the method of lines. Expand the solution as

$$
y ( t , x ) = \sum _ { j } C _ { j } ( x ) y _ { j } ( t )
$$

where now the coefficients $y _ { j }$ are functions of time. Then

$$
\left. \frac { \partial y } { \partial t } \right| _ { i } = \dot { y } _ { i } , \qquad \left. \frac { \partial y } { \partial x } \right| _ { i } = \sum _ { j } D _ { i j } ^ { ( 1 ) } y _ { j } , \quad \mathrm { e t c . }
$$

You get a system of ODEs in $t$ for the $y _ { j }$ , which you can solve in the standard way.   
Runge-Kutta is a good method to start with.

Problems with two or three spatial dimensions are usually handled by making expansions along each dimension separately:

$$
u ( x , y , z ) = \sum _ { i j k } u _ { i j k } C _ { i } ( x ) C _ { j } ( y ) C _ { k } ( z )
$$

Elliptic equations give simultaneous algebraic equations for the coefficients that are typically solved with iterative methods because of the large number of variables. See [11] for an example and references to the literature.

# CITED REFERENCES AND FURTHER READING:

Hesthaven, J., Gottlieb, S., and Gottlieb, D. 2007, Spectral Methods for Time-Dependent Problems (New York: Cambridge University Press), Chapter 9.[1]

Gottlieb, D., and Orszag, S.A. 1977, Numerical Analysis of Spectral Methods: Theory and Applications (Philadelphia: S.I.A.M.).[2][A classic,and still somewhat useful.]

Canuto, C., Hussaini, M.Y., Quarteroni, A., and Zang, T.A. 1988, Spectral Methods in Fluid Dynamics (Berlin: Springer).[3] [Standard reference for fluid dynamics applications,but applicable to other areas.]

Boyd, J.P. 2001, Chebyshev and Fourier Spectral Methods, 2nd ed. (New York: Dover Publications). Available at http://www-personal.engin.umich.edu/\~jpboyd.[4] [Best single book: complete, and not too formal.]

Fornberg, B. 1996, A Practical Guide to Pseudospectral Methods (New York: Cambridge University Press).[5] [Good for getting started, but not for large-scale problems.]

Fornberg, B. 1998, “Calculation of Weights in Finite Difference Formulas,” SIAM Review vol. 40, pp. 685–691.[6]

Baltensperger, R., and Trummer, M.R. 2003, “Spectral Differencing with a Twist,” SIAM Journal on Scientific Computing,vol. 24,pp.1465-1487.[7]

Matsushima, T., and Marcus, P.S. 1995, “A Spectral Method for Polar Coordinates,” Journal of Computational Physics vol. 120,pp. 365-374.[8]

Matsushima, T., and Marcus, P.S. 1997, “A Spectral Method for Unbounded Domains,” Journal of Computational Physics vol. 137, pp. 321-345.[9]

Rawitscher, G.H. 1991, “Accuracy Analysis of a Bessel Spectral Function Method for the Solution of Scattering Equations,” Journal of Computational Physics vol. 94, pp. 81–101.[10]

Pfeiffer, H.P., Kidder, L.E., Scheel, M.A., and Teukolsky, S.A. 2003, “A Multidomain Spectral Method for Solving Elliptic Equations,” Computer Physics Communications, vol. 152, pp. 253– 273.[11]

Bjørhus, M. 1995, “The ODE Formulation of Hyperbolic PDEs Discretized by the Spectral Collocation Method,” SIAM Journal on Scientific Computing, vol. 16, pp. 542–557. [Describes a good algorithm for hyperbolic equations.]


<!-- chunk 0017: pages 1121-1190 -->
# Computational Geometry

# 21.0 Introduction

It is a safe bet that more computer cycles are expended on the formulas of computational geometry than on all other uses of computers put together. We include not just the computer’s nominal CPU, of course, but also those other other, often vastly more powerful, CPUs hidden in the computer’s graphics chipset, and in all the video entertainment and high-definition television boxes in the world.

Indeed, computational geometry, and the broader fields of computer graphics and computer vision in which it is embedded, have become central areas of computer science, supporting a huge industrial base of applied work and employment for computer scientists and program developers at all professional levels. It is impossible for us to do justice to this colossus in a single chapter. Yet, there are a number of elementary techniques from the field that ought to be in the repertory of any practicing computational scientist.

In this chapter we will build a body of methods sufficient to construct efficient Delaunay triangulations in two dimensions, and to use such triangulations for interpolating functions of two variables on an irregular grid, and other applications. In getting to this goal (and a bit beyond it) we will allow ourselves to be diverted into various other interesting, and often useful, topics, including:

- tree data structures for sets of points   
nearest-neighbor problems much about lines, triangles, and polygons spheres in $n$ dimensions, and rotation matrices Voronoi and all that convex hulls minimum spanning trees   
- finding intersecting objects

and more.

In the spirit of full disclosure, we must mention that our treatment of some of the most interesting topics in the above list will be restricted to the two-dimensional case, even when the three-dimensional case may be equally relevant to computational science. The reason is simply one of space on the page. Three-dimensional algorithms are often more complex, have more special cases that must be treated, and generally result in codes that are too long for us to include. We have struggled to condense working, reasonably efficient, two-dimensional codes to an appropriate size for this chapter. You will be able to use these for two-dimensional problems, or you can mine them for understanding before seeking out three-dimensional solutions in the references.

An additional disclosure relates to our use of floating-point arithmetic, and our treatment of special cases of “exact” equality. Since floating-point numbers and their arithmetic are not exact, it usually does not make computational sense to test for cases of exact equality. However, historically, geometers have always distinguished, e.g., between a point being “inside” a triangle versus “on an edge” or “at a vertex.” This has introduced a certain schizophrenia into the field. On the one hand (and especially before about 1990), practitioners have labored to create algorithms that use exact (integer) arithmetic, so that the traditional distinctions can be elegantly preserved. On the other hand (and especially after about 1990, when fast floating operations in special-purpose graphics processors started to be available), many of these niceties are no longer needed, and sloppiness at the level of “machine epsilon” can be tolerated in the interest of speed. In this chapter we are unapologetically in the sloppy camp. In boundary cases, our code is supposed to produce reasonable results, but not necessarily choose that specific reasonable result that you might think you want. Caveat emptor.

A less specific goal in this chapter is to give some of the “flavor” of the field of computational geometry. It is a flavor that deliciously combines elements of Euclid (pardon!) with elements of modern computer science and mathematics.

Some good general references are listed here.

# CITED REFERENCES AND FURTHER READING:

de Berg, M., van Kreveld, M., Overmars, M., and Schwarzkopf, O. 2000, Computational Geometry: Algorithms and Applications, 2nd revised ed.(Berlin: Springer). [Best-selling text, especially strong on references to the published literature.]   
O’Rourke, J. 1998, Computational Geometry in C, 2nd ed. (Cambridge, UK: Cambridge University Press). [Well written, with clear explanations and C code.]   
Preparata, F.P. and Shamos, M.I. 1991, Computational Geometry: An Introduction (Berlin: Springer).   
Schneider, P.J. and Eberly, D.H. 2003, Geometric Tools for Computer Graphics (San Francisco: Morgan Kaufmann). [Huge compendium of formulas and code.]   
Bowyer, A. and Woodwark, J. 1983, A Programmer’s Geometry (London: Butterworths). [Delightful classic, especially for those who get nostalgic at seeing Fortran printed in all uppercase.]   
Glassner, A.S., ed. 1990, Graphics Gems (San Diego: Academic Press). [Series of books full of algorithmic tricks-of-the-trade.]   
Arvo, J., ed. 1991, Graphics Gems II (San Diego: Academic Press).   
Kirk, D., ed. 1992, Graphics Gems III (Cambridge, MA: Academic Press).   
Heckbert, P.S., ed. 1994, Graphics Gems IV (Cambridge, MA: Academic Press).   
Euclid, ca. 300BC, Euclid’s Elements; reprinted 2002 (Santa Fe, NM: Green Lion Press).

# 21.1 Points and Boxes

A point $\mathbf { p }$ in a $D$ -dimensional space is specified by its $D$ Cartesian coordinates, $( x _ { 0 } , x _ { 1 } , \ldots , x _ { D - 1 } )$ . Generally we will concern ourselves only with the cases $D = 2$ (points in a plane) and $D = 3$ (points in 3-space), but the concept is more general.

The representation in code follows just this paradigm. By eschewing special names for individual coordinates — like $x$ , y, z — we keep the ability to loop easily over coordinates in $D$ dimensions.

template<Int DIM> struct Point {   
Simple structure to represent a point in DIM dimensions. Doub x[DIM]; The coordinates. Point(const Point &p) { Copy constructor. for (Int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ; i<DIM; $\mathrm { i + + ) } \ \mathrm { \ x [ i ] ~ \eta = \ p \cdot \mathrm { \ x [ i ] : } }$ Point& operator $=$ (const Point &p) { Assignment operator. for (Int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ; i<DIM; $\dot { \bf 1 } + +$ ) x[i] $=$ p.x[i]; return \*this; 1 bool operator $\mathrel { = } =$ (const Point &p) const { for (Int $\scriptstyle \dot { 1 } = 0$ ; i<DIM; $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \beta } } } .$ ) if (x[i] $\ ! = \ p . \mathbf { x }$ [i]) return false; return true; } Point(Doub $\mathbf { x } 0 ~ = ~ 0 . 0$ , Doub $\mathrm { ~ x 1 ~ } = ~ 0 . 0$ , Doub ${ \bf x } 2 ~ = ~ 0 . 0$ ) { $\mathbf { x } \left[ 0 \right] \ = \ \mathbf { x } 0$ ; Constructor by coordinate values. Arguments if (DIM $> 1 \dot { }$ ) $\mathbf { x } \left[ 1 \right] \ = \ \mathbf { x } 1$ ; beyond the required number are not used if (DIM $> 2$ ) $\mathbf { x } \left[ 2 \right] \ = \ \mathbf { x } 2$ ; and can be omitted. if (DIM $> 3$ ) throw("Point not implemented for DIM > 3"); }   
};

# pointbox.h

#

In the interest of concise code, the constructor above may pass some unnecessary default arguments of zero. You can easily clean this up if you care.

If we have two points $\mathbf { p }$ and $\mathbf { q }$ , we can compute their distance $d$ ,

$$
d = | \mathbf { p } - \mathbf { q } | = \left[ \sum _ { i = 0 } ^ { D - 1 } ( p _ { i } - q _ { i } ) ^ { 2 } \right] ^ { 1 / 2 }
$$

where $p _ { i }$ and $q _ { i }$ are now the respective Cartesian coordinates for each point.

In code, we have

template<Int DIM> Doub dist(const Point<DIM> &p, const Point<DIM> &q) { Returns the distance between two points in DIM dimensions.

Doub dd $= ~ 0 . 0$ ;  
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<DIM; ${ \mathrm { j } } + + { \mathrm { . } }$ ) dd $+ =$ SQR(q.x[j]-p.x[j]);  
return sqrt(dd);

Note that dist is not a member of the class Point, but rather a freestanding function whose arguments are Points. We will overload dist with other types of arguments, signifying other kinds of distances between objects.

# 21.1.1 Boxes

By a box, we mean a rectangle (for $D = 2$ ) or rectangular parallelepiped (for $D = 3$ , a “brick” in other words) that is aligned with the coordinate axes. Boxes are interesting because they can tessellate (that is, partition) $D$ -dimensional space, and they can contain other objects. Indeed, every finite, extended object has a bounding box, which is the unique smallest box that contains it. One way to represent a box is by the points at two special, diagonally opposite, corners. The first point (“low”) has coordinate values that are the minima on the surface of the box; the second point (“high”) has coordinate values that are the maxima. All other corners of a box, it should be obvious, have coordinate values that are, dimension by dimension, either the value of “low” or the value of “high”; and all such permutations are corners, $2 ^ { D }$ in all.

The code follows this description:

template<Int DIM> struct Box {   
Structure to represent a Cartesian box in DIM dimensions. Point<DIM> lo, hi; Diagonally opposite corners (min of all coordinates and Box() {} max of all coordinates) are stored as two points. Box(const Point<DIM> &mylo, const Point<DIM> &myhi) : lo(mylo), hi(myhi) {}   
};

Note that a copy constructor and assignment operator are not needed, since by default the two Points will be appropriately copied or assigned (one convenience of this representation).

A point can be either outside a box, inside it, or — in principle — on its surface. As mentioned in $\ S 2 1 . 0$ , we represent all coordinates as (approximate) floating-point numbers, not (exact) integers, so it would not be prudent to depend on any exact equalities of coordinate values or distances. We will be careful, therefore, not to put too much credence in the idea of the exact surface of a box; usually we’ll consider the surface (should some exact equality happen to hold) as a part of the box’s interior.

If a point is outside a box, then we define its distance from the box to be the distance to the nearest point on the surface of (or inside) the box. A glance at Figure 21.1.1 shows that this distance is the Pythagorean sum (that is, square root of sum of squares) of the distances from the point to some — but not all — of the hyperplanes that bound the box. The rule is that when a point has a coordinate that is greater than the corresponding max of the box, or less than the corresponding min, then that coordinate contributes to the sum. When the point has a coordinate between the max and min, then it does not contribute to the sum, since (along that coordinate) the shortest line can be perpendicular to the hyperplane. When a point is inside, or on the surface of, a box, we define its distance to the box to be zero.

These definitions of distance are embodied in the following code.

template<Int DIM> Doub dist(const Box<DIM> &b, const Point<DIM> &p) { If point p lies outside box b, the distance to the nearest point on b is returned. If p is inside b or on its surface, zero is returned.

Doub dd $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
for (Int $\scriptstyle { \dot { 1 } } = 0$ ; i<DIM; i++) { if (p.x[i]<b.lo.x[i]) dd $+ =$ SQR(p.x[i]-b.lo.x[i]); if (p.x[i]>b.hi.x[i]) dd $+ =$ SQR(p.x[i]-b.hi.x[i]);   
}   
return sqrt(dd);

Frequently we want to know if a point is inside or outside a box. The above dist routine can be used for this. A positive return means outside, zero means inside. If inside-versus-outside, and not distance, is all you want to know, then some streamlining is possible: Replace dd by a Boolean variable, substitute logical-or’s for the additions, and of course omit the square root. The logic remains otherwise the same.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/f851fd2782bf32c8a5b8131b8b67e821578328dd87fb3ddfb0496498b62705c5.jpg)  
Figure 21.1.1. Distance from a point to a $D$ -dimensional box. The general formula (as for lines $A A ^ { \prime }$ and $C C ^ { \prime } )$ ) is a Pythagorean sum of $D$ distances to the plane that includes the nearer side of the box. But when the point is between two such parallel planes (as for $B B ^ { \prime }$ and $D D ^ { \prime }$ ) then the corresponding coordinate is omitted from the sum.

# 21.1.2 Nodes for Binary Trees of Boxes

In the next section we will construct a binary tree of nested boxes, wherein each box is subdivided into, and linked to, two daughter boxes. Each box in the tree will also contain a list of points that lie inside the box. For use in such a task, we here give a structure, derived from the Box structure, but with additional variables that can point to a mother box, two daughter boxes, and the low and high indices on a list of points (designating the range of points inside the box). The constructor just sets all the values explicitly.

template<Int DIM> struct Boxnode : Box<DIM>   
Node in a binary tree of boxes containing points. See text for details. Int mom, dau1, dau2, ptlo, pthi; Boxnode() {} Boxnode(Point<DIM> mylo, Point<DIM> myhi, Int mymom, Int myd1, Int myd2, Int myptlo, Int mypthi) : Box<DIM>(mylo, myhi), mom(mymom), dau1(myd1), dau2(myd2), ptlo(myptlo), pthi(mypthi) {}

# 21.2 KD Trees and Nearest-Neighbor Finding

Once, long ago, the term “kd tree” (or “k-D tree”) was an abbreviation for “ $k$ -dimensional tree.” However, the term has come to mean a very specific, and useful, kind of tree structure for partitioning points, especially in small numbers of dimensions, like 2 or 3. A KD tree that contains $N$ points can be constructed in ${ \cal O } ( N \log N )$ time and $O ( N )$ space. Once constructed, the KD tree facilitates such operations as finding a point’s nearest neighbor in ${ \cal O } ( \log N )$ time, or all nearest neighbors in ${ \cal O } ( N \log N )$ time. KD trees were first described by Bentley [8] in 1975. Let’s see how this works.

Start with a very large box, one that easily contains all possible points that are of interest. There is no penalty for making this root box humongous, so coordinates of $\pm 1 0 ^ { 9 9 }$ are fine. Now generate a list of $N$ points (of interest to your application) that lie inside the root box. The defining principles of a KD tree are

- Boxes are successively partitioned into two daughter boxes.   
Each partition is along the axis of one coordinate.   
The coordinates are used cyclically in successive partitions. In making the partition, the position of the “cut” is chosen to leave equal numbers of points on the two sides (or differing by one in the case of an odd number of points).

Within these principles, there are some arbitrary design choices to be made. In the implementation below, the partition “cut” goes exactly through one of the points (i.e., shares one of its coordinate values). This avoids a bit of extra bookkeeping incurred by other possible choices. Also, we terminate the tree when a box node contains either one or two points, avoiding the additional partitioning of two-point boxes into two one-point boxes. This choice is natural because the Boxnode structure already has pointers to two points (ptlo and pthi), and it reduces the total number of stored boxes by as much as $50 \%$ .

With these principles and design rules in mind, you can decode Figure 21.2.1, which shows a two-dimensional KD tree containing 1000 points. (As a bit of artistic license, the root box in the figure has been shrunk to just contain the points, instead of being off near infinity.)

Interestingly, given $N$ , the number of points, it is possible to give an exact formula for the number of boxes generated by our KD tree partition rules. (This makes memory allocation for the tree very straightforward.) If $N _ { B } ( N )$ is the number of boxes needed for $N$ points, then two obvious recurrence relations describe what happens in the initial partitioning of $2 n$ points into $n$ plus $n$ , or $2 n - 1$ points into $n$ plus $n - 1$ :

$$
\begin{array} { c } { { N _ { B } ( 2 n ) = 2 N _ { B } ( n ) + 1 } } \\ { { N _ { B } ( 2 n - 1 ) = N _ { B } ( n ) + N _ { B } ( n - 1 ) + 1 } } \end{array}
$$

The $+ 1$ in both formulas refers to the additional mother box that “glues together” two daughter partial trees at each stage. The solution to these recurrences is

$$
\begin{array} { r } { N _ { B } ( N ) = \operatorname* { m i n } ( M - 1 , ~ 2 N - \frac { 1 } { 2 } M - 1 ) } \end{array}
$$

where $M$ is the smallest power of 2 greater or equal to $N$ , that is,

$$
M = 2 ^ { \left\lceil \log _ { 2 } N \right\rceil }
$$

(You can verify this solution by induction, working out the various possibilities of the min function. Or — much more fun — you can write a program to verify it numerically for $N < 1 0 ^ { 9 }$ , say.)

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/2d00070a1095da26458eeacf6d31d91aa7bd8f0aa929d422b4bde570f54efa24.jpg)  
Figure 21.2.1. KD tree constructed from 1000 points in the plane. The first subdivision is visible as a fullheight vertical line about halfway across the figure. The next subdivisions are horizontal lines, extending halfway across the figure. The subdivisions alternate between horizontal and vertical, and partition into (nearly) equal numbers of points at each stage. This tree terminates when there are either one or two points in a box (one of which is usually on the box boundary).

# 21.2.1 Implementation of the KD Tree

We implement the KD tree as a structure that gets built from a vector of Points and contains methods that embody the principal applications that we will discuss below, mainly various kinds of nearest-neighbor problems.

template<Int DIM> struct KDtree   
Structure for implementing a KD tree. static const Doub BIG; Size of the root box, value set below. Int nboxes, npts; Number of boxes, number of points. vector< Point<DIM> $>$ &ptss; Reference to the vector of points in the KD tree. Boxnode<DIM> \*boxes; The array of Boxnodes that form the tree. VecInt ptindx, rptindx; Index of points (see text), and reverse index. Doub \*coords; Point coordinates rearranged contiguously. KDtree(vector< Point<DIM> $>$ &pts); Constructor. \~KDtree() {delete [] boxes;} Next, utility functions for use after the tree is constructed. See below. Doub disti(Int jpt, Int kpt); Int locate(Point<DIM> pt); Int locate(Int jpt); Next, applications that use the KD tree. See text. Int nearest(Int jpt); Int nearest(Point<DIM> pt); void nnearest(Int jpt, Int \*nn, Doub \*dn, Int n); static void sift_down(Doub \*heap, Int \*ndx, Int nn); Used by nnearest. Int locatenear(Point<DIM> pt, Doub r, Int \*list, Int nmax);   
};

Note that the KDtree structure keeps a reference to the vector of Points that created it. This is used in some of the applications and has the implication that the user should not modify the vector of points while its derived KD tree is in scope. The array coords is an internal representation of the points-vector that is used during the construction of the KD tree, and then is immediately returned to the memory pool.

What makes the KD tree fast to construct is the existence of fast partition algorithms, $O ( N )$ in time, that not only find the median value in an array of $N$ values, but also move all smaller values to one side of the array and all larger values to the other. We already met such an algorithm in $\ S 8 . 5$ , in the routine select. Here, we need a slight variant, selecti, that partitions an array of integers not by their values, but by using them to index a separate array of values that remain unaltered. Because we will want to partition subsegments of arrays, we pass all references to the arrays by address.

Int selecti(const Int k, Int \*indx, Int n, Doub \*arr)   
Permutes indx[0..n-1] to make arr[indx[0..k-1]]  arr[indx[k]]  arr[indx[k+1..n-1]]. The array arr is not modified. See comments in the routine select.   
{   
Int i,ia,ir,j,l,mid;   
Doub a;   
l=0;   
$\scriptstyle { \mathrm { i } x = n - 1 }$ ;   
for (;;) { if (ir <= l+1) { if ( $\scriptstyle \mathbf { i r } \ = = \ 1 + 1$ && arr[indx[ir]] $<$ arr[indx[l]]) SWAP(indx[l],indx[ir]); return indx[k]; else { mid=(l+ir) >> 1; SWAP(indx[mid],indx $[ 1 + 1 ]$ ); if (arr[indx[l]] $>$ arr[indx[ir]]) SWAP(indx[l],indx[ir]); if (arr[indx[l+1]] $>$ arr[indx[ir]]) SWAP(indx[l+1],indx[ir]); if (arr[indx[l]] $>$ arr[indx[l+1]]) SWAP(indx[l],indx[l+1]); $\dot { 1 } = 1 + 1$ ; $\scriptstyle { \dot { \mathsf { J } } } = { \dot { \mathsf { 1 } } } { \boldsymbol { \mathbf { r } } }$ ; ia $=$ indx[l+1]; a=arr[ia]; for (;;) { do $\dot { \bf 1 } + +$ ; while (arr[indx[i]] < a); do j--; while (arr[indx[j]] > a); if (j < i) break; SWAP(indx[i],indx[j]); indx[l+1] $=$ indx[j]; indx[j] $=$ ia; if (j $> = { \textbf { k } } .$ ) ir=j-1; if (j $< = { \bf \nabla } \mathbf { k } .$ ) $\mathbf { \vec { \tau } } _ { 1 } = \mathbf { \dot { \tau } }$ ; }   
}

The basic strategy for constructing the KD tree is this: Set up an array of integers that index the $N$ points (ptindx, below). Next, copy all the point coordinates into an array (coords) in which all the $x _ { 0 }$ coordinates are contiguous, followed by all the $x _ { 1 }$ coordinates, and so on through all the dimensions. Now use selecti to partition (and rearrange) the index of points according to the value of their $x _ { 0 }$ coordinates, with half the points on each side of the partition. These two halves, now viewed as separate arrays, contain the points in two new daughter boxes. Now partition each of them into half by the value of the $x _ { 1 }$ coordinate. And so on, recursively, going through the coordinates cyclically.

The recursion is so simple that it is easy to code it as a simple “pending task list,” thus avoiding the overhead of recursive function calls. A pending task consists of an index pointing to the box ready for further partitioning (the expectant mother, as it were) and a value that remembers which dimension is next to partition along. Because the tree is constructed “depth first,” the task list never grows larger than the log of the total number of boxes. Every new daughter box is born with a pointer to its mother, and pointers to its beginning and end elements in the points index array ptindx. Although these elements will generally be permuted in subsequent partitionings, none will ever be moved out of the range specified when a daughter box is first created. That is why the whole process can be done in a single pointindex array, with all boxes simply pointing into some subrange of that array.

The KDtree constructor, below, should now be straightforward to understand.

plate<Int DIM> KDtree<DIM>::KDtree(vector< Point<DIM> $>$ &pts) :   
s(pts), npts(pts.size()), ptindx(npts), rptindx(npts) {   
nstruct a KD tree from a vector of points.   
Int ntmp,m,k,kk,j,nowtask,jbox,np,tmom,tdim,ptlo,pthi;   
Int \*hp;   
Doub \*cp;   
Int taskmom[50], taskdim[50]; Enough stack for $2 ^ { 5 0 }$ points!   
for $( \mathtt { k } = 0$ ; k<npts; $\mathbf { k } { + } { + } \mathbf { \Gamma } .$ ) ptindx[k] $= \texttt { k }$ ; Initialize the index of points.   
Calculate the number of boxes and allocate memory for them.   
${ \texttt { m } } = { \texttt { 1 } }$ ;   
for (ntmp $=$ npts; ntmp; ntmp >>= 1) { m $< < = ~ 1$ ;   
}   
nboxes $=$ 2\*npts - $\mathrm { ~ ( ~ m ~ } > > \ 1 )$ ;   
if (m < nboxes) nboxes $= ~ \mathfrak { m }$ ;   
nboxes--   
boxes $=$ new Boxnode<DIM>[nboxes];   
Copy the point coordinates into a contiguous array.   
coords $=$ new Doub[DIM\*npts];   
for ( $\scriptstyle \dot { \ j } = 0$ , kk $_ { = 0 }$ ; $\mathrm { j } < \tt D I M$ ; ${ \dot { \mathsf { J } } } ^ { + + }$ , kk $+ =$ npts) { for $\scriptstyle ( \mathtt { k } = 0$ ; k<npts; $\mathbf { k } { + } { + }$ ) coords[kk+k] $=$ pts[k].x[j];   
Initialize the root box and put it on the task list for subdivision.   
Point<DIM> lo(-BIG,-BIG,-BIG), hi(BIG,BIG,BIG); Syntax OK for 2-D too.   
boxes[0] $=$ Boxnode<DIM>(lo, hi, 0, 0, 0, 0, npts-1);   
jbox $\qquad = \ 0$ ;   
taskmom[1] $\mathit { \Theta } = \mathit { \Theta } 0$ ; Which box.   
taskdim[1] $\qquad = \ 0$ ; Which dimension.   
nowtask $= ~ 1$ ;   
while (nowtask) { Main loop over pending tasks. tmom $=$ taskmom[nowtask]; tdim $=$ taskdim[nowtask--]; ptlo $=$ boxes[tmom].ptlo; pthi $=$ boxes[tmom].pthi; hp $=$ &ptindx[ptlo]; Points to left end of subdivision. $\mathtt { c p } \ =$ &coords[tdim\*npts]; Points to coordinate list for current dim. np $=$ pthi - ptlo + 1; Number of points in the subdivision. kk $=$ (np-1)/2; Index of last point on left (boundary point). (void) selecti(kk,hp,np,cp); Here is where all the work is done. Now create the daughters and push them onto the task list if they need further subdividing. hi $=$ boxes[tmom].hi; lo $=$ boxes[tmom].lo; hi.x[tdim] $=$ lo.x[tdim] $=$ coords[tdim\*npts $^ +$ hp[kk]]; boxes[ $: + +$ jbox] $=$ Boxnode<DIM>(boxes[tmom].lo,hi,tmom,0,0,ptlo,ptlo+kk); boxes $[ + +$ jbox] $=$ Boxnode<DIM>(lo,boxes[tmom].hi,tmom,0,0,ptlo+kk+1,pthi); boxes[tmom].dau1 $=$ jbox-1; boxes[tmom].dau2 $=$ jbox; if (kk $> 1 \dot { 2 }$ ) { taskmom[++nowtask] $=$ jbox-1; taskdim[nowtask] $=$ (tdim $^ { + 1 }$ ) % DIM; } if (np - kk $> 3$ ) { taskmom[++nowtask] $=$ jbox; taskdim[nowtask] $=$ (tdim $^ { + 1 }$ ) % DIM; }   
for $( \mathrm { j } = 0 ) \mathrm { i }$ ; j<npts; ${ \mathrm { j } } + + { \mathrm { . } }$ ) rptindx[ptindx[j]] $=$ j; Create reverse index.   
delete [] coords; Don’t need them anymore.

There are a small number of utility functions that are easy to provide. Although we generally prefer to have our distance (dist) functions be freestanding, it is useful to have a KDtree member routine that returns the distance between two points in a KD tree, referenced by their integer position in the underlying vector of points.

template<Int DIM> Doub KDtree<DIM>::disti(Int jpt, Int kpt) { Returns the distance between two points in the kdtree given their indices in the array of points, but returns a large value if the points are identical.

if (jpt $= =$ kpt) return BIG; else return dist(ptss[jpt], ptss[kpt]); }

There is a special reason for returning BIG when the two points are identical: Later, when we find a point’s nearest neighbor, we don’t want the invariable answer to be “itself!”

Another simple function takes an arbitrary Point as the argument and returns the index of the box that uniquely contains it. In this function we first see an example of traversing the tree hierarchically, starting at the root box and then choosing only one of two daughter boxes at each stage. Also, by keeping track of which dimension is next to be partitioned on (jdim, below), we need only check one of the point’s coordinates at each stage. Evidently, the whole process is ${ \cal O } ( \log N )$ in time, since there can be only that many levels in the tree.

template<Int DIM> Int KDtree<DIM>::locate(Point<DIM> pt) {   
Given an arbitrary point pt, return the index of which kdtree box it is in. Int nb,d1,jdim; $\mathbf { n b } \ = \ \mathbf { j d i m } \ = \ 0$ ; Start with the root box. while (boxes[nb].dau1) { As far as possible down the tree. d1 $=$ boxes[nb].dau1; if (pt.x[jdim] $< =$ boxes[d1].hi.x[jdim]) $\mathtt { n b } { = } \mathtt { d } 1$ ; else nb $\ c =$ boxes[nb].dau2; jdim $\begin{array} { r l } { = } & { { } + + } \end{array}$ jdim % DIM; Increment the dimension cyclically. } return nb;   
}

The actual Box can be obtained from the returned integer, say j, by referencing boxes[j] in the KDtree, since Boxnode is a derived class of Box.

A very similar utility returns the index of the box that contains one of the points used to construct the KDtree. This is not necessarily the same box as the above routine would return, because of the possibility of multiple ties in coordinate values, in which case some tied points can lie on one side of the median partition and others on the other side.

template<Int DIM> Int KDtree<DIM>::locate(Int jpt) {   
Given the index of a point in the kdtree, return the index of which box it is in. Int nb,d1,jh; jh $=$ rptindx[jpt]; The reverse index tells where the point lies in the nb $\mathit { \Theta } = \mathit { \Theta } 0$ ; index of points. while (boxes[nb].dau1) { d1 $=$ boxes[nb].dau1; if (jh $< =$ boxes[d1].pthi) nb=d1; else nb $=$ boxes[nb].dau2; } return nb;   
}

# 21.2.2 Applications of KD Trees

Most applications of KD trees make use of locality properties of its nested boxes. This is best seen in a few examples.

Suppose we want to know which of the $N$ points in a KD tree is closest to an arbitrary point p (not necessarily one of the points in the tree). Without the tree, this is evidently a calculation that requires $O ( N )$ operations, as we compare $\mathbf { p }$ to each candidate point in turn. However, if we have invested the ${ \cal O } ( N \log N )$ operations required to construct the tree, then we can proceed in the following way. First, find the box in which $\mathbf { p }$ lies, and find the closest point in the tree that lies in that box. This takes ${ \cal O } ( \log N )$ operations, as we saw above. The found point might in fact be the nearest neighbor (we don’t know yet), but in any case its distance is now an upper bound on how far away the true nearest neighbor can be.

Second, traverse the tree by a depth-first recursion (exactly the way we did when we constructed the tree). As we encounter each new box, we check whether it could possibly contain a point closer than the nearest point found so far. Since we start with a point that is already pretty close (in the same box as $\mathbf { p }$ ), most boxes get rejected at this step. When a box is rejected, we don’t need to open its daughter boxes, so a whole branch of the tree gets “pruned.” On average, only about ${ \cal O } ( \log N )$ boxes actually get opened, so the total work load to find the nearest point is ${ \cal O } ( \log N )$ .

If we are really interested in only a single point $\mathbf { p }$ , then the “slow,” $O ( N )$ , method would have been faster. But if we are repeating the operation for many different points ${ \bf p } _ { i }$ , comparing to the same $N$ points in the tree each time, then calling the following routine for each ${ \bf p } _ { i }$ in turn is a big win.

# kdtree.h

if (d < dnrst) { nrst $=$ ptindx[i]; dnrst $\qquad = \ \mathrm { ~ d ~ }$ ; } } Second stage, we traverse the tree opening only possibly better boxes. task[1] $\mathit { \Theta } = \mathit { \Theta } _ { 0 } ;$ ntask $\ l = \ 1$ ; while (ntask) { $\mathrm { ~ \bf ~ k ~ } =$ task[ntask--]; if (dist(boxes[k],pt) $<$ dnrst) { Distance to closest point in box. if (boxes[k].dau1) { If not an end node, put on task list. task $[ + + ]$ ntask] $=$ boxes[k].dau1; task[++ntask] $=$ boxes[k].dau2; } else { Check the 1 or 2 points in the box. for ( $\mathrm { i } =$ boxes[k].ptlo; $\div < =$ boxes[k].pthi; $\dot { 1 } + +$ ) { d $=$ dist(ptss[ptindx[i]],pt); if (d $<$ dnrst) { nrst $=$ ptindx[i]; dnrst $\mathit { \Theta } = \mathit { \Theta } \mathtt { d }$ ; } } } } } return nrst;

What if we want to know the nearest-neighbor point not of an arbitrary location, but of one of the points stored in the KD tree? The above routine won’t do. If we send it a point in the tree, it will give the obvious result that the point is its own nearest neighbor! We need to modify the routine so as to use disti from KDtree, which defined a point’s self-distance as being large, rather than small.

An additional useful feature is to find not the single nearest neighbor, but the $n$ nearest neighbors for some specified $n < N - 1$ . The trick here is to avoid making the algorithm $O ( n \log N )$ , which is what it would be if, for each candidate point, we compared the candidate to all $n$ of the best points so far. A good way to proceed is with a heap structure, as described in $\ S 8 . 3$ and used (for a very similar purpose) in the routine hpsel in $\ S 8 . 5$ . The work load then scales as $O ( \log n \log N )$ .

The following routine is coded so as to lose hardly any efficiency in the case $n = 1$ (find the single nearest neighbor) while using a heap structure in the case $n > 1$ .

template<Int DIM> void KDtree<DIM>::nnearest(Int jpt, Int \*nn, Doub \*dn, Int n) Given the index jpt of a point in a kdtree, return a list $\mathtt { n n } [ 0 \ldots \mathtt { n } - 1 ]$ of the indices of the n points in the tree nearest to point $\dot { \mathsf { J } }$ , and a list $\mathtt { d d } [ 0 \dots \cdot \mathtt { n } ^ { - 1 } ]$ of their distances.

Int i,k,ntask,kp;   
Int task[50]; Stack for boxes to be opened.   
Doub d;   
if ( $\textbf { \em n } >$ npts-1) throw("too many neighbors requested");   
for $\scriptstyle \dot { 1 } = 0$ ; i<n; $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \rho } } } .$ ) dn[i] $=$ BIG;   
Find smallest mother box with enough points to initialize the heap.   
$\tt k p \tt =$ boxes[locate(jpt)].mom;   
while (boxes[kp].pthi - boxes[kp].ptlo < n) kp $=$ boxes[kp].mom;   
Examine its points and save the n closest.   
for ( $\dot { \bf 1 } =$ boxes[kp].ptlo; $\ \mathrm { i } < =$ boxes[kp].pthi; $\dot { \bf 1 } + +$ ) { if (jpt $= =$ ptindx[i]) continue;   
${ \texttt { d } } =$ disti(ptindx[i],jpt);   
if (d < dn[0]) { dn[0] $=$ d; nn[0] $=$ ptindx[i]; if (n>1) sift_down(dn,nn,n); Maintain the heap structure.   
}   
Now we traverse the tree opening only possibly better boxes.   
task[1] $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
ntask $\ l = \ 1$ ;   
while (ntask) { $\mathrm { ~ \bf ~ k ~ } =$ task[ntask--]; if $( \mathrm { k \Omega } = = \mathrm { k p } )$ continue; Don’t redo the box used to initialize. if (dist(boxes[k],ptss[jpt]) $<$ dn[0]) { if (boxes[k].dau1) If not an end node, put on task list. task[++ntask] $=$ boxes[k].dau1; task[++ntask] $=$ boxes[k].dau2; } else { Check the 1 or 2 points in the box. for ( $\dot { \bf 1 } =$ boxes[k].ptlo; $\dot { \bf 1 } < =$ boxes[k].pthi; i++) { d $=$ disti(ptindx[i],jpt); if (d $<$ dn[0]) { dn[0] $=$ d; nn[0] $=$ ptindx[i]; if $\cdot \mathtt { n } > 1$ ) sift_down(dn,nn,n); Maintain the heap. } } } }   
}   
return;

The following routine is used by the above for the sift-down process on the heap, differing from the sift_down used by hpsort $( \ S 8 . 3 )$ only in its tailored interface for the present application, and the fact that it simultaneously rearranges two arrays, the distances (forming a heap) and the corresponding point numbers.

template<Int DIM> void KDtree<DIM>::sift_down(Doub \*heap, Int \*ndx, Int nn) Fix heap[0..nn-1], whose first element (only) may be wrongly filed. Make a corresponding permutation in ndx[0.. $\mathtt { n n - 1 } ]$ . The algorithm is identical to that used by sift_down in hpsort.

Int $\mathrm { ~ n ~ } = \mathrm { ~ n ~ n ~ } \mathrm { ~ - ~ } \mathrm { ~ 1 ~ }$ ; Int j,jold,ia; Doub a; $\mathrm { ~ a ~ } =$ heap[0]; $\mathrm { ~ i ~ a ~ } = \mathrm { ~ n d x } [ 0 ]$ ; jold $\mathit { \Theta } = \mathit { \Theta } 0$ ; $\dot { \mathrm { ~ \scriptsize ~ j ~ } } = \mathrm { ~ \scriptsize ~ 1 ~ }$ ; while (j $< = { \mathrm { ~ \bf ~ n ~ } } .$ ) { if $( \mathrm { ~ j ~ } < \mathrm { ~ n ~ }$ && heap[j] $<$ heap[j $+ 1 ]$ ) j++; if ( $a \ > =$ heap[j]) break; heap[jold] $=$ heap[j]; ndx[jold] $=$ ndx[j]; jold $=$ j; ${ \mathrm {  ~ j ~ } } = ~ 2 * { \mathrm {  ~ j ~ } } + ~ 1 { \mathrm {  ~ \Omega ~ } }$ ; } heap[jold] $\qquad = \ \mathtt { a }$ ; ndx[jold] $=$ ia; }

As a final illustrative example, here is how to find all points in a KD tree that lie within a specified radius $r$ of some arbitrary location p.

template<Int DIM>   
Int KDtree<DIM>::locatenear(Point<DIM> pt, Doub r, Int \*list, Int nmax) {   
Given a point pt and radius r, returns a value nret such that list[0..nret-1] is a list of a   
kdtree points within a radius r of pt, up to a user-specified maximum of nmax points. Int k,i,nb,nbold,nret,ntask,jdim,d1,d2; Int task[50]; $\mathrm { n b ~ = ~ j d i m ~ = ~ n r e t ~ = ~ 0 ~ } ;$ if ( $\mathrm { ~ \bf ~ r ~ } < 0 . 0 )$ throw("radius must be nonnegative"); Find the smallest box that contains the ”ball” of radius r. while (boxes[nb].dau1) { nbold $=$ nb; d1 $=$ boxes[nb].dau1; ${ \tt d } 2 { \it \Delta \phi } = { \tt d } $ boxes[nb].dau2; Only need to check the dimension that divides the daughters. if (pt.x[jdim] $+ \mathrm { ~  ~ r ~ } < =$ boxes[d1].hi.x[jdim]) nb = d1; else if (pt.x[jdim] - $\scriptstyle \mathbf { \underline { { ~ r ~ } } } > =$ boxes[d2].lo.x[jdim]) $\mathrm { { n b } } ~ = ~ \mathrm { { d } } 2$ ; jdim $= \quad + +$ jdim % DIM; if (nb $= =$ nbold) break; Neither daughter encloses the ball. } Now traverse the tree below the starting box only as needed. task[1] $=$ nb; ntask $= ~ 1$ ; while (ntask) { $\mathrm { ~ \bf ~ k ~ } =$ task[ntask--]; if (dist(boxes[k],pt) > r) continue; Box and ball are disjoint. if (boxes[k].dau1) { Expand box further when possible. task $^ { , + + }$ ntask] $=$ boxes[k].dau1; task[++ntask] $=$ boxes[k].dau2; } else { Otherwise process points in the box. for ( $\mathrm { i } =$ boxes[k].ptlo; $\ \mathrm { i } < =$ boxes[k].pthi; $\mathbf { i } + +$ ) { if (dist(ptss[ptindx[i]],pt) $< = \texttt { r }$ && nret $<$ nmax) list[nret++] $=$ ptindx[i]; if (nret $= =$ nmax) return nmax; Not enough space! } } } return nret;   
}

You might wonder why the above routine doesn’t also use the tree structure to find cases where a box lies entirely inside the “ball” of radius $r$ , in which case it could add the box’s points to the output list without further opening of its daughters. The improvement is potentially a factor of $O ( \log n )$ , where $n$ is the typical number of neighbors returned. The resulting routine is slightly too long for us to include, however. A good exercise is to code this modification yourself. You’ll see that it is harder to check whether a box is inside a ball than vice versa: You have to check all $2 ^ { D }$ corners of the box, not just the diagonally opposite “low” and “high” ones.

# CITED REFERENCES AND FURTHER READING:

Bentley, J.L. 1975, “Multidimensional Binary Search Trees Used for Associative Searching,” Communications of the ACM,vol.18, pp. 509-517.   
de Berg, M., van Kreveld, M., Overmars, M., and Schwarzkopf, O. 2000, Computational Geometry:Algorithms and Applications, 2nd revised ed.(Berlin: Springer), $\ S 5 . 2$ .   
Samet, H. 1990, The Design and Analysis of Spatial Data Structures (Reading, MA: Addison-Wesley).

# 21.3 Triangles in Two and Three Dimensions

Not since the time of Euclid has the lowly triangle attracted as much attention as it does today in computer graphics. Triangles and triangulation (the decomposition, or approximation, of complicated geometrical objects using only triangles) are at the heart of practically every computer-generated image.

Three points, call them a, b, c, define a triangle. They are its vertices. If the points are two-dimensional, the triangle lies in the two-dimensional plane. If the points have higher dimensionality, then the triangle floats in the corresponding $D$ - dimensional space (most commonly $D = 3$ ). For now, consider only the former case, with $D = 2$ , so that a has coordinates $( a _ { 0 } , a _ { 1 } )$ , and similarly for $\mathbf { b }$ and c.

Area. The area $\mathbf { \mathcal { A } } ( \mathbf { a b c } )$ of the triangle $\triangle$ abc can be written in a number of equivalent ways, including

$$
{ \begin{array} { r l } & { 2 { \mathcal { A } } ( \mathbf { a b c } ) = { \left| \begin{array} { l l l } { a _ { 0 } } & { a _ { 1 } } & { 1 } \\ { b _ { 0 } } & { b _ { 1 } } & { 1 } \\ { c _ { 0 } } & { c _ { 1 } } & { 1 } \end{array} \right| } } \\ & { \qquad = ( \mathbf { b } - \mathbf { a } ) \times ( \mathbf { c } - \mathbf { a } ) = ( b _ { 0 } - a _ { 0 } ) ( c _ { 1 } - a _ { 1 } ) - ( b _ { 1 } - a _ { 1 } ) ( c _ { 0 } - a _ { 0 } ) } \\ & { \qquad = ( \mathbf { c } - \mathbf { b } ) \times ( \mathbf { a } - \mathbf { b } ) = ( c _ { 0 } - b _ { 0 } ) ( a _ { 1 } - b _ { 1 } ) - ( c _ { 1 } - b _ { 1 } ) ( a _ { 0 } - b _ { 0 } ) } \\ & { \qquad = ( \mathbf { a } - \mathbf { c } ) \times ( \mathbf { b } - \mathbf { c } ) = ( a _ { 0 } - c _ { 0 } ) ( b _ { 1 } - c _ { 1 } ) - ( a _ { 1 } - c _ { 1 } ) ( b _ { 0 } - c _ { 0 } ) } \end{array} }
$$

Here $\times$ denotes the vector cross product, defined in two dimensions simply by

$$
\mathbf { A } \times \mathbf { B } = A _ { 0 } B _ { 1 } - B _ { 1 } A _ { 0 } \qquad { \mathrm { ( t w o d i m e n s i o n s ~ o n l y ) } }
$$

Below, when we consider triangles in three dimensions, it will be the vector cross product forms in equation (21.3.1) that give a generalized formula for the area. Let us also note in passing that the formulas for area are separately linear in each of the six coordinates $a _ { 0 } , a _ { 1 } , b _ { 0 } , b _ { 1 } ,$ $c _ { 0 }$ , and $c _ { 1 }$ .

Equation (21.3.1) can yield a value that is positive, zero, or negative: The area is a signed area. By convention (embodied in equation 21.3.1), the area is positive if a traversal from a to $\mathbf { b }$ to c goes counterclockwise (CCW) around the triangle, and negative if it goes clockwise (CW). The area is zero if and only if the three points are collinear, in which case the triangle is degenerate. (In the formulas that follow, we will generally assume the nondegenerate case.)

The absolute value $\left| \mathcal { A } \right|$ is the (unsigned) “area” of the triangle in the conventional geometrical sense. It can also be calculated directly from the side lengths $d _ { a b }$ , $d _ { b c }$ , and $d _ { c a }$ as follows:

$$
| \mathcal { A } | = \sqrt { s ( s - d _ { a b } ) ( s - d _ { b c } ) ( s - d _ { c a } ) }
$$

where $s$ is half the perimeter,

$$
s \equiv { \frac { 1 } { 2 } } ( d _ { a b } + d _ { b c } + d _ { c a } )
$$

(Does it go without saying that you compute the side lengths by taking the coordinate differences and using the Pythagorean theorem?)

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/272ff61df8aab3671b08739de5b058b772702e09874ff4f507079c9da2b5ab7b.jpg)  
Figure 21.3.1. Three kinds of triangle centers. (a) Incircle and incenter; bisectors of the three vertex angles meet at the incenter. (b) Circumcircle and circumcenter; perpendicular bisectors of the edges meet at the circumcenter. (c) Centroid; lines from the edge midpoints to the opposite vertices meet at the centroid.

Related Circles. Every nondegenerate triangle has an inscribed circle or incircle, which is the largest circle that can be drawn inside the triangle. The incircle is tangent to all three sides of the triangle. Lines from its center, the incenter, to each vertex bisect the angle at that vertex (see Figure 21.3.1). If $\mathbf { q }$ is the incenter point, with coordinates $( q _ { 0 } , q _ { 1 } )$ , then its location is given by

$$
q _ { i } = \frac { 1 } { 2 s } ( d _ { b c } a _ { i } + d _ { c a } b _ { i } + d _ { a b } c _ { i } ) ~ ( i = 0 , 1 )
$$

while its radius is given by

$$
r _ { \mathrm { i n } } = \left( \frac { ( s - d _ { a b } ) ( s - d _ { b c } ) ( s - d _ { c a } ) } { s } \right) ^ { 1 / 2 }
$$

Every nondegenerate triangle also has a circumscribed circle or circumcircle, which is the unique circle that goes through its three vertices. Suppose $\mathbf { Q }$ is the circumcenter point, with coordinates $( Q _ { 0 } , Q _ { 1 } )$ . Let $[ b a ] _ { 0 }$ and $[ b a ] _ { 1 }$ denote the coordinate differences $b _ { 0 } - a _ { 0 }$ and $b _ { 1 } - a _ { 1 }$ , respectively; and similarly for $[ c a ] _ { 0 }$ and $[ c a ] _ { 1 }$ . Then, in $2 \times 2$ determinant form,

$$
\begin{array} { c c } { { \displaystyle Q _ { 0 } = a _ { 0 } + \frac { 1 } { 2 } \left| \begin{array} { c c } { { ( [ b a ] _ { 0 } ) ^ { 2 } + ( [ b a ] _ { 1 } ) ^ { 2 } } } & { { [ b a ] _ { 1 } } } \\ { { ( [ c a ] _ { 0 } ) ^ { 2 } + ( [ c a ] _ { 1 } ) ^ { 2 } } } & { { [ c a ] _ { 1 } } } \end{array} \right| } } & { { \left| \begin{array} { c c } { { [ b a ] _ { 0 } } } & { { [ b a ] _ { 1 } } } \\ { { [ c a ] _ { 0 } } } & { { [ c a ] _ { 1 } } } \end{array} \right| } } \\ { { \displaystyle Q _ { 1 } = a _ { 1 } + \frac { 1 } { 2 } \left| \begin{array} { c c } { { [ b a ] _ { 0 } } } & { { ( [ b a ] _ { 0 } ) ^ { 2 } + ( [ b a ] _ { 1 } ) ^ { 2 } } } \\ { { [ c a ] _ { 0 } } } & { { ( [ c a ] _ { 0 } ) ^ { 2 } + ( [ c a ] _ { 1 } ) ^ { 2 } } } \end{array} \right| } } & { { \left| \begin{array} { c c } { { [ b a ] _ { 0 } } } & { { [ b a ] _ { 1 } } } \\ { { [ c a ] _ { 0 } } } & { { [ c a ] _ { 1 } } } \end{array} \right| } } \end{array}
$$

The circumcenter is, by definition, the same distance from all three vertices. Therefore the radius of the circumcircle is

$$
r _ { \mathrm { c i r c u m } } = \sqrt { ( Q _ { 0 } - a _ { 0 } ) ^ { 2 } + ( Q _ { 1 } - a _ { 1 } ) ^ { 2 } }
$$

where $Q _ { 0 }$ and $Q _ { 1 }$ are given above. (Obviously you can save the semi-final results in equation 21.3.7 for this computation, before adding $a _ { 0 }$ or $a _ { 1 }$ .)

Later, in $\ S 2 1 . 6$ , we will be calculating a lot of circumcircles. We use the following simple definition of a structure Circle, and a routine circumcircle() that directly implements equations (21.3.7) and (21.3.8).

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/a98a9dab3b012c5b5ae88d737a0a4a3f357f30e389c6dc9f439d4ec7fae2e2aa.jpg)  
Figure 21.3.2. Any point in the plane $\mathbf { q }$ can be expressed as a linear combination of a triangle’s three vertices. The coefficients $( \alpha , \beta , \gamma )$ , called barycentric coordinates, sum to 1 and are proportional to the areas of 4qbc, $\triangle \mathbf { q c a }$ , and $\triangle$ qab, respectively.

struct Circle {Point<2> center;Doub radius;Circle(const Point<2> &cen, Doub rad) : center(cen), radius(rad) {}  
};

Circle circumcircle(Point<2> a, Point<2> b, Point<2> c) { Doub a0,a1,c0,c1,det,asq,csq,ctr0,ctr1,rad2; $\mathtt { a 0 } \ =$ a.x[0] - b.x[0]; a1 $=$ a.x[1] - b.x[1]; $\mathtt { c 0 } \ =$ c.x[0] - b.x[0]; c1 $=$ c.x[1] - b.x[1]; det $=$ a0\*c1 - c0\*a1; if (det $\mathit { \Theta } = = \ 0 . 0$ ) throw("no circle thru colinear points"); det $=$ 0.5/det; asq $=$ a0\*a0 $^ +$ a1\*a1; csq $=$ c0\*c0 $^ +$ c1\*c1; ctr0 $=$ det\*(asq\*c1 - csq\*a1); ctr1 $=$ det\*(csq\*a0 - asq\*c0); rad2 $=$ ctr0\*ctr0 $^ +$ ctr1\*ctr1; return Circle(Point $\mathrm { \tt { < } } 2 \mathrm { \tt { > } }$ (ctr0 $^ +$ b.x[0], ctr1 $^ +$ b.x[1]), sqrt(rad2));

Centroid and Barycentric Coordinates. Distinct from both its incenter and its circumcenter is a triangle’s centroid, or center of gravity, M. This point lies at the intersections of the lines drawn from each vertex to the midpoint of the opposite side. Its coordinates are simply the means of the coordinates of the vertices,

$$
M _ { i } = { \textstyle \frac { 1 } { 3 } } ( a _ { i } + b _ { i } + c _ { i } ) \qquad ( i = 0 , 1 )
$$

The centroid is also the point $\mathbf { M }$ where the areas $\mathcal { A } ( \mathbf { a b } \mathbf { M } )$ , $\mathcal { A } ( \mathbf { b c M } )$ , and $\mathbf { \mathcal { A } } ( \mathbf { c a M } )$ are all equal. In $\ S 2 1 . 7$ we will be using a triangular mesh to interpolate a function. The significance of the centroid is that it is the point where a linearly interpolated function takes on the value that is the mean of the function values at the three vertices.

In fact, generalizing the idea of the centroid, any point $\mathbf { q }$ in the plane can be written as a linear combination of the three vertices a, b, c, with coefficients that sum to unity. These coefficients are called $\mathbf { q }$ ’s barycentric coordinates and can be intuitively expressed in terms of the area formulas for triangles (see Figure 21.3.2). The equations are

$$
\begin{array} { l } { \mathbf { q } = \alpha \mathbf { a } + \beta \mathbf { b } + \gamma \mathbf { c } } \\ { \alpha = \mathcal { A } ( \mathbf { b c q } ) / \mathcal { A } ( \mathbf { a b c } ) } \\ { \beta = \mathcal { A } ( \mathbf { c a q } ) / \mathcal { A } ( \mathbf { a b c } ) } \\ { \gamma = \mathcal { A } ( \mathbf { a b q } ) / \mathcal { A } ( \mathbf { a b c } ) } \end{array}
$$

with, by construction,

$$
\alpha + \beta + \gamma = 1
$$

The first line in equation (21.3.10) is thus equivalent to

$$
{ \bf q } = { \bf c } + \alpha ( { \bf a } - { \bf c } ) + \beta ( { \bf b } - { \bf c } )
$$

This can be viewed as the equation for a coordinate transformation, one that transforms from $( \alpha , \beta )$ coordinates to $( q _ { 0 } , q _ { 1 } )$ coordinates. Evidently, since it is linear, its inverse — the formulas for $\alpha$ and $\beta$ in equation (21.3.10) — must also be linear. But we knew this already, having remarked on the fact that the area formulas (21.3.1) are linear in all their coordinates, so linear in $q _ { 0 }$ and $q _ { 1 }$ in particular. Barycentric coordinates generalize to triangles in three or more dimensions in a useful way, as we will see below.

Note that $\alpha$ , $\beta$ , or $\gamma$ go to 1 as the point $\mathbf { q }$ approaches a, $\mathbf { b }$ , or c, respectively; and that along any edge of the triangle (say $\overline { { a b } }$ ) the coefficient of the opposite vertex (here, $\gamma$ ) vanishes. The point $\mathbf { q }$ is inside the triangle $\triangle$ abc if and only if $\alpha$ , $\beta$ , and $\gamma$ are all positive. In fact, this is a good way to test for a point’s “insideness” in a triangle. (You can of course omit calculating the denominator area in this application.)

Barycentric coordinates are also useful when you want to pick a uniformly random point $\mathbf { q }$ inside $\triangle$ abc: First pick $\alpha$ and $\beta$ as each uniformly random in $( 0 , 1 )$ . Next, if $\alpha + \beta > 1$ , modify them both by $\alpha  1 - \alpha$ and $\beta  1 - \beta$ . Finally, apply equation (21.3.12). The idea is that the first choice of $\alpha$ and $\beta$ is random in the parallelogram spanned by two sides of the triangle; then, if it is on the wrong side of the diagonal, we move it to the correct side by a reflection.

# 21.3.1 Triangles in Three Dimensions

Our favorite triangle is still defined by the three points a, $\mathbf { b }$ , and c, but these are now points in three dimensions, with coordinates (e.g., for a) $( a _ { 0 } , a _ { 1 } , a _ { 2 } )$ . The generalization of the signed area $\mathcal { A }$ (equation 21.3.1) is now a vector area $\vec { \mathcal { A } }$ whose direction is normal to the plane of the triangle and whose length is the area of the triangle. It is most easily written using a vector cross product, defined in three dimensions by

$$
{ \begin{array} { r l } & { \mathbf { A } \times \mathbf { B } = { \left| \begin{array} { l l l } { { \widehat { \mathbf { e } } } _ { 0 } } & { { \widehat { \mathbf { e } } } _ { 1 } } & { { \widehat { \mathbf { e } } } _ { 2 } } \\ { A _ { 0 } } & { A _ { 1 } } & { A _ { 2 } } \\ { B _ { 0 } } & { B _ { 1 } } & { B _ { 2 } } \end{array} \right| } } \\ & { \qquad = ( A _ { 1 } B _ { 2 } - A _ { 2 } B _ { 1 } ) { \widehat { \mathbf { e } } } _ { 0 } + ( A _ { 2 } B _ { 0 } - A _ { 0 } B _ { 2 } ) { \widehat { \mathbf { e } } } _ { 1 } + ( A _ { 0 } B _ { 1 } - A _ { 1 } B _ { 0 } ) { \widehat { \mathbf { e } } } _ { 2 } } \end{array} }
$$

where $\widehat { \mathbf { e } } _ { 0 } , \widehat { \mathbf { e } } _ { 1 }$ , and $\widehat { \mathbf { e } } _ { 2 }$ are respectively the unit vectors $( 1 , 0 , 0 ) , ( 0 , 1 , 0 )$ , and $( 0 , 0 , 1 )$ . Then we have (cf. equation 21.3.1)

$$
{ \begin{array} { r } { 2 { \vec { \mathcal { A } } } ( \mathbf { a b c } ) = ( \mathbf { b } - \mathbf { a } ) \times ( \mathbf { c } - \mathbf { a } ) } \\ { = ( \mathbf { c } - \mathbf { b } ) \times ( \mathbf { a } - \mathbf { b } ) } \\ { = ( \mathbf { a } - \mathbf { c } ) \times ( \mathbf { b } - \mathbf { c } ) } \end{array} }
$$

You calculate the positive scalar area $\mathcal { A } \equiv | \vec { \mathcal { A } } |$ by the usual square-root sum of the squares of $\vec { \mathcal { A } }$ ’s three components; or you can instead use equation (21.3.3), with $d _ { a b } = | \mathbf { a } - \mathbf { b } |$ , etc.

Plane Defined by Triangle. A point $\mathbf { q }$ lies in the plane defined by $\triangle$ abc if and only if the volume of the tetrahedron abcq is zero. The tetrahedral volume, in general, is given by

$$
{ \begin{array} { r l } & { \left| a _ { 0 } \quad a _ { 1 } \quad a _ { 2 } \quad 1 \right| } \\ & { = \left| b _ { 0 } \quad b _ { 1 } \quad b _ { 2 } \quad 1 \right| } \\ & { \left| c _ { 0 } \quad c _ { 1 } \quad c _ { 2 } \quad 1 \right| } \\ & { \qquad \left| d _ { 0 } \quad q _ { 1 } \quad q _ { 2 } \quad 1 \right| } \\ & { \qquad = \left( \mathbf { b } - \mathbf { a } \right) \cdot \left[ \left( \mathbf { c } - \mathbf { a } \right) \times \left( \mathbf { q } - \mathbf { a } \right) \right] } \\ & { \qquad = \left( \mathbf { c } - \mathbf { a } \right) \cdot \left[ \left( \mathbf { q } - \mathbf { a } \right) \times \left( \mathbf { b } - \mathbf { a } \right) \right] } \\ & { \qquad = \left( \mathbf { q } - \mathbf { a } \right) \cdot \left[ \left( \mathbf { b } - \mathbf { a } \right) \times \left( \mathbf { c } - \mathbf { a } \right) \right] } \end{array} }
$$

where “	” signifies vector dot product. You can also cyclically permute a, $\mathbf { b }$ , and c in the above equation, for a seemingly infinite number of variations of the same formula!

The volume $\mathcal { V }$ is signed and is positive if $\triangle$ abc is counterclockwise when viewed from outside (side away from $\mathbf { q }$ ), that is, the right-hand rule gives an outwardpointing normal.

The last form in equation (21.3.15) is particularly nice, because setting it to zero gives the equation satisfied by any point $\mathbf { q }$ in the plane defined by $\triangle$ abc:

$$
\mathbf { q } \cdot \mathbf { N } = D
$$

with

$$
\begin{array} { r l } & { \mathbf { N } = \left( \mathbf { b } - \mathbf { a } \right) \times \left( \mathbf { c } - \mathbf { a } \right) \quad ( \mathrm { o r c y c l i c ~ p e r m u t a t i o n ~ o f ~ } \mathbf { a } , \mathbf { b } , \mathbf { c } ) } \\ & { D = \mathbf { a } \cdot \mathbf { N } \quad ( \mathrm { o r , f o r ~ t h a t ~ m a t t e r } ) \quad = \mathbf { b } \cdot \mathbf { N } = \mathbf { c } \cdot \mathbf { N } } \end{array}
$$

We could also divide equation (21.3.16) by $| \mathbf { N } |$ , in which case the vector on the left will be $\hat { \bf N } = { \bf N } / | { \bf N } |$ , the unit vector normal to the plane, and $\widehat { D } = D / | \mathbf { N } |$ will be the plane’s distance from the origin.

With the same machinery, we can readily project any point $\mathbf { p }$ into a new point $ { \mathbf { b } } ^ { \prime }$ that lies in the plane of $\triangle$ abc:

$$
{ \bf p } \longrightarrow { \bf p } ^ { \prime } = { \bf p } + \frac { [ ( { \bf a } - { \bf p } ) \cdot { \bf N } ] { \bf N } } { | { \bf N } | ^ { 2 } }
$$

where $\mathbf { N }$ is as above. For a in this formula, you can substitute $\mathbf { b } , \mathbf { c }$ , or any other point in the plane.

We can project one triangle into the plane defined by another triangle by projecting its three points in turn. (This is a very common operation in rendering a triangulated three-dimensional model in the two-dimensional “camera plane” of your computer’s screen.)

Barycentric Coordinates. Barycentric coordinates are valid in three dimensions for points $\mathbf { q }$ in the triangle’s plane, and equation (21.3.10), in particular, still holds. To compute $( \alpha , \beta )$ , one can in principle calculate the various $\mathcal { A }$ ’s from (21.3.14), but an easier equivalent calculation is

$$
\begin{array} { r l } & { \alpha = \frac { \mathbf { b } ^ { \prime 2 } ( \mathbf { a } ^ { \prime } \cdot \mathbf { q } ^ { \prime } ) - ( \mathbf { a } ^ { \prime } \cdot \mathbf { b } ^ { \prime } ) ( \mathbf { b } ^ { \prime } \cdot \mathbf { q } ^ { \prime } ) } { \mathbf { a } ^ { \prime 2 } \mathbf { b } ^ { \prime 2 } - ( \mathbf { a } ^ { \prime } \cdot \mathbf { b } ^ { \prime } ) ^ { 2 } } } \\ & { \beta = \frac { \mathbf { a } ^ { \prime 2 } ( \mathbf { b } ^ { \prime } \cdot \mathbf { q } ^ { \prime } ) - ( \mathbf { a } ^ { \prime } \cdot \mathbf { b } ^ { \prime } ) ( \mathbf { a } ^ { \prime } \cdot \mathbf { q } ^ { \prime } ) } { \mathbf { a } ^ { \prime 2 } \mathbf { b } ^ { \prime 2 } - ( \mathbf { a } ^ { \prime } \cdot \mathbf { b } ^ { \prime } ) ^ { 2 } } } \end{array}
$$

(compute identical denominators only once) where

$$
\mathbf { a } ^ { \prime } \equiv \mathbf { a } - \mathbf { c } , \qquad \mathbf { b } ^ { \prime } \equiv \mathbf { b } - \mathbf { c } , \qquad \mathbf { q } ^ { \prime } \equiv \mathbf { q } - \mathbf { c }
$$

By the way, if $\mathbf { q }$ is not in the plane of $\triangle$ abc, you can still use equation (21.3.19). In that case, you get the $( \alpha , \beta )$ coordinates of the projected point in the plane. Also, notice what happens in the special case that $\triangle$ abc is a right triangle, with right vertex c, and with sides $\overline { { a c } }$ and $\overline { { b c } }$ of unit length, i.e., ${ d } _ { a c } = { d } _ { b c } = 1$ . Then the coordinate transformations, in both directions, are simply

$$
\begin{array} { c } { \displaystyle \mathbf { q } = \mathbf { c } + \alpha ( \mathbf { a } - \mathbf { c } ) + \beta ( \mathbf { b } - \mathbf { c } ) } \\ { \displaystyle [ \alpha , \beta ] = [ ( \mathbf { a } - \mathbf { c } ) \cdot ( \mathbf { q } - \mathbf { c } ) , ( \mathbf { b } - \mathbf { c } ) \cdot ( \mathbf { q } - \mathbf { c } ) ] } \end{array}
$$

In other words, we project into an orthonormal coordinate system in the plane by a simple change of origin (to c) and dot products with the two “axes” a  c and $\mathbf b - \mathbf c$ .

Frequently, barycentric coordinates are the coordinates of choice for operations in a plane in three dimensions that is (or can be) specified by a triangle. A trivial example is that we can test whether a projected point $\mathbf { p } ^ { \prime }$ is inside or outside of $\triangle$ abc by using equation (21.3.19) (or, if applicable, 21.3.21) to get $\alpha$ and $\beta$ , and then checking that $\alpha$ , $\beta$ , and $\gamma = 1 - \alpha - \beta$ are all positive.

Angle Between Two Triangles. The dihedral angle between two triangles (with a common edge, say) is the same as the angle between the normal vectors of the two triangles. The normal vectors are given by the vector area formula (21.3.14). The angle is best computed using equation (21.4.13), in the next section.

# CITED REFERENCES AND FURTHER READING:

Bowyer, A. and Woodwark, J. 1983, A Programmer’s Geometry (London: Butterworths), Chapter 4.

Schneider, P.J. and Eberly, D.H. 2003, Geometric Tools for Computer Graphics (San Francisco: Morgan Kaufmann), $\ S 3 . 5$ and Appendix C.

López-López, F.J. 1992, “Triangles Revisited,” in Graphics Gems III, Kirk, D., ed. (Cambridge, MA: Academic Press).

Glassner, A.S. 1990, “Useful 3D Geometry,” in Graphics Gems, Glassner, A.S., ed. (San Diego: Academic Press).

# 21.4 Lines, Line Segments, and Polygons

A line is defined by any two points through which it passes. Call them a and b. As in $\ S 2 1 . 1$ , the points can be two-dimensional, if the domain of interest is a plane, or three-dimensional (or higher), if the line is embedded in a higher-dimensional space. For now, consider only the two-dimensional case.

Parametrically, any point c that lies on the line defined by a and $\mathbf { b }$ must be a linear combination of those two points. One way to write this is

$$
\mathbf { c } = \mathbf { a } + s ( \mathbf { b } - \mathbf { a } ) ( - \infty < s < \infty )
$$

where $s$ is a parameter along the line. The chosen normalization is to make $s = 0$ at a and $s = 1$ at $\mathbf { b }$ . The part of the line between a and $\mathbf { b }$ has $0 \leq s \leq 1$ and is a line segment, denoted ab. The whole line is denoted ab.

The easiest way to get the equation satisfied by all points c on the line $\stackrel {  } { \mathbf { a b } }$ is to take the vector cross product of equation (21.4.1) with $\mathbf { ( b - a ) }$ on the right. Using the fact that the cross product of any vector with itself is zero, we get

$$
\mathbf { c } \times ( \mathbf { b } - \mathbf { a } ) = \mathbf { a } \times \mathbf { b }
$$

or writing out the components,

$$
c _ { 0 } ( b _ { 1 } - a _ { 1 } ) - c _ { 1 } ( b _ { 0 } - a _ { 0 } ) = a _ { 0 } b _ { 1 } - a _ { 1 } b _ { 0 }
$$

which is indeed a linear relation between the coordinates $c _ { 0 }$ and $c _ { 1 }$ . While it is tempting to divide this equation by $b _ { 0 } - a _ { 0 }$ to get an equation in that old familiar high school form “ ${ \dot { \boldsymbol { y } } } = m { \boldsymbol { x } } + b$ ,” one should often resist that temptation since, as written, equation (21.4.3) remains valid for the case of a vertical line, when $b _ { 0 } - a _ { 0 } = 0$ .

Intersection of Two Lines. In the plane, two lines $\stackrel {  } { \mathbf { a b } }$ and most always intersect. We can solve for the point of intersection by equating the two lines’ parametric forms,

$$
{ \bf a } + s ( { \bf b } - { \bf a } ) = { \bf x } - t ( { \bf y } - { \bf x } )
$$

and then solving the two equations (components 0 and 1) for the two unknowns $s$ and $t$ . The result is

$$
\begin{array} { c c l } { s = \displaystyle \frac { ( \mathbf { x } - \mathbf { y } ) \times ( \mathbf { a } - \mathbf { x } ) } { ( \mathbf { b } - \mathbf { a } ) \times ( \mathbf { x } - \mathbf { y } ) } = \frac { ( x _ { 0 } - y _ { 0 } ) ( a _ { 1 } - x _ { 1 } ) - ( x _ { 1 } - y _ { 1 } ) ( a _ { 0 } - x _ { 0 } ) } { ( b _ { 0 } - a _ { 0 } ) ( x _ { 1 } - y _ { 1 } ) - ( b _ { 1 } - a _ { 1 } ) ( x _ { 0 } - y _ { 0 } ) } } \\ { t = \displaystyle \frac { ( \mathbf { a } - \mathbf { x } ) \times ( \mathbf { b } - \mathbf { a } ) } { ( \mathbf { b } - \mathbf { a } ) \times ( \mathbf { x } - \mathbf { y } ) } = \frac { ( a _ { 0 } - x _ { 0 } ) ( b _ { 1 } - a _ { 1 } ) - ( a _ { 1 } - x _ { 1 } ) ( b _ { 0 } - a _ { 0 } ) } { ( b _ { 0 } - a _ { 0 } ) ( x _ { 1 } - y _ { 1 } ) - ( b _ { 1 } - a _ { 1 } ) ( x _ { 0 } - y _ { 0 } ) } } \end{array}
$$

Of course, the special case of parallel lines with no intersection is indicated by the vanishing of the denominators.

All those cross products might make you think that equation (21.4.5) has a geometrical interpretation. Indeed so. In Figure 21.4.1, the lines intersect at o. Segment $\overline { { { \bf { X 0 } } } }$ is therefore just $\mathbf { \overline { { X Y } } }$ scaled by $t$ , while $\overline { { \mathbf { a 0 } } }$ is similarly $\overline { { \mathbf { a b } } }$ scaled by $s$ . The area of $\triangle$ oxa is therefore given (cf. equation 21.3.1) by

$$
2 \mathcal { A } ( \mathbf { o x } \mathbf { a } ) = s t \ ( \mathbf { x } - \mathbf { y } ) \times ( \mathbf { a } - \mathbf { b } )
$$

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/2d9ca76a8f3a5df7e29daa09db25332994de16c5fdef319127f50ceeba84d65f.jpg)  
Figure 21.4.1. Geometrical construction that yields the intersection point of two lines in terms of ratios of triangle areas. See text for details.

By linearity of a triangle’s area with its height (holding the base fixed), we also have

$$
\mathcal { A } ( \mathbf { o x a } ) / \mathcal { A } ( \mathbf { y x a } ) = t \qquad \mathcal { A } ( \mathbf { o x a } ) / \mathcal { A } ( \mathbf { b x a } ) = s
$$

Equation (21.4.5) follows immediately from these relations and equation (21.3.1).

Point-to-Line Distance. What is the perpendicular distance $d$ from an arbitrary point $\mathbf { q }$ to the line ab that passes through points a and b? Evidently $d$ is the height of $\triangle$ abq when its base is the segment ab. Therefore, from the schoolbook “one-half base times height” formula,

$$
d = { \frac { 2 { \mathcal { A } } ( \mathbf { a b q } ) } { | \mathbf { a - b } | } } = { \frac { ( q _ { 0 } - b _ { 0 } ) ( a _ { 1 } - b _ { 1 } ) - ( q _ { 1 } - b _ { 1 } ) ( a _ { 0 } - b _ { 0 } ) } { { \sqrt { ( a _ { 0 } - b _ { 0 } ) ^ { 2 } + ( a _ { 1 } - b _ { 1 } ) ^ { 2 } } } } }
$$

Note that $d$ is signed, positive if it is to the left of the directed line from $\mathbf { a }$ to $\mathbf { b }$ , negative if it is to the right, and a good segue to our next topic.

# 21.4.1 Line Segment Intersections and “Left-Of" Relations

You can use equation (21.4.5) to test whether two line segments, $\overline { { \mathbf { a b } } }$ and $\mathbf { \overline { { X y } } }$ , intersect: Calculate $s$ and $t$ and then check if they are both in the range $( 0 , 1 )$ . (To keep our discussion brief, we won’t say much here, or in what follows, about the various degenerate cases where $s$ or $t$ or both are exactly 0 or 1. These are straightforward to figure out if your application so demands.)

A related, but slightly different, approach is to use the fact that the formulas for triangle areas given in equation (21.3.1) are signed. This means that, as equivalent statements, we have

$$
\begin{array} { r } { \mathcal { A } ( \mathbf { a b c } ) > 0 \quad \Longleftrightarrow \quad \left[ \begin{array} { l } { \mathbf { c } \mathrm { ~ i s ~ t o ~ t h e ~ } l e f t \mathrm { ~ o f ~ l i n e ~ } \overleftrightarrow { \mathbf { a b } } } \\ { \mathrm { ~ w h e n ~ i t ~ i s ~ t r a v e r s e d ~ i n ~ } } \\ { \mathrm { t h e ~ d i r e c t i o n ~ f r o m ~ } \mathbf { a } \mathrm { ~ t o ~ } \mathbf { b } } \end{array} \right] } \end{array}
$$

while $\mathbf { \mathcal { A } } ( \mathbf { a b c } ) < 0$ implies that c is to the right of the same line. We refer to either statement in (21.4.9) as a left-of relation.

A necessary and sufficient condition for two segments $\overline { { \mathbf { a b } } }$ and $\mathbf { \overline { { X y } } }$ to intersect is that $\mathbf { X }$ and $\mathbf { y }$ be on opposite sides of $\stackrel {  } { \mathbf { a b } }$ , and a and b be on opposite sides of . (We again omit discussion of the various special cases of collinearity.) This test, using the triangle area formulas in equation (21.3.1), involves evaluating four leftof relations, each computationally a cross product, which is just slightly more work than computing $s$ and $t$ (which share a denominator). However, you can sometimes use the same cross products, once computed, in other parts of your calculation. So, it is often a toss-up whether to use the $^ { 6 6 } S$ , $t ^ { \prime \prime }$ method or the “left-of” method — you should consider both.

Table 21.4.1. Relationship between two line segments classified by the signs of the areas of various triangles. Refer to Figure 21.4.2 for an illustration of each case.   

<table><tr><td rowspan=1 colspan=1>Fig.</td><td rowspan=1 colspan=1>△abx</td><td rowspan=1 colspan=1>△aby</td><td rowspan=1 colspan=1>△xya</td><td rowspan=1 colspan=1>△xyb</td><td rowspan=1 colspan=1>Intersection</td><td rowspan=1 colspan=1>Hull</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>1+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>1+</td><td rowspan=1 colspan=1>ab× xyab × xy</td><td rowspan=1 colspan=1>□axby□aybx</td></tr><tr><td rowspan=1 colspan=1>34</td><td rowspan=1 colspan=1>+1</td><td rowspan=1 colspan=1>1+</td><td rowspan=2 colspan=1>+</td><td rowspan=5 colspan=1>1+++1</td><td rowspan=7 colspan=1>axxy&gt;ba xxyabxxyxabxabxabyx xab</td><td rowspan=7 colspan=1>△ayx△byx△bxy△axy△yba△xba△xab△yab</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+</td><td rowspan=3 colspan=1>+1+</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>external</td><td rowspan=4 colspan=1>□ayxb□abxyabxyaxyb</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>external</td></tr><tr><td rowspan=2 colspan=1>1314</td><td rowspan=2 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>external</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>external</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+1</td><td rowspan=1 colspan=1>+</td><td rowspan=1 colspan=1>+1</td><td rowspan=1 colspan=2>Not possible!Not possible!</td></tr></table>

Table 21.4.1 enumerates the 16 cases that you get if you compute all four possible “left-of” tests for two line segments. (Actually, only 14 are geometrically possible!) The table classifies each possibility as to whether the segments intersect (intersection denoted by $\times .$ , not to be confused with vector cross product!), whether the unidirectional extension of one segment (a ray) intersects the other segment, or (lastly) whether an ordinary line intersection occurs external to both segments. Also shown for each case is the outer hull of the two segments (the smallest triangle or quadrilateral enclosing both segments) and how it is traversed in clockwise order. Figure 21.4.2 shows an example of each possibility.

You can use the table to find combinations that test for specific circumstances.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/b1758e3c22fd6c85a0f3f33ee5d00f9e35f0af2a3b83a5cc483edee1317af789.jpg)  
Figure 21.4.2. Two line segments, $a b$ and $x y$ , define four triangles (4abx, 4aby, $\triangle x y a$ , and $\triangle x y b )$ , each of which can have positive or negative area. Of the 16 combinations of signs, 14 (shown here) correspond to to possible intersection relationships between the line segments or their extensions as rays.

For example, if you need a test for whether the ray $\vec { \mathbf { a b } }$ intersects the segment $\mathbf { \overline { { X y } } }$ (including the possibility of the segments intersecting), you examine rows 1, 2, 3, and 6 in the table and read off a test that involves just three left-of relations:

$$
\mathbf { \mathcal { A } } ( \mathbf { a b x } ) \mathbf { \mathcal { A } } ( \mathbf { a b y } ) < 0 \qquad \mathrm { a n d } \qquad \mathbf { \mathcal { A } } ( \mathbf { a b y } ) \mathbf { \mathcal { A } } ( \mathbf { x y a } ) > 0
$$

Of course there are exactly equivalent tests using $s$ and $t$ , for this example (with $s$ and $t$ as in equation 21.4.4) $s > 0$ and $0 < t < 1$ .

Angle Between Two Vectors. Suppose that $\mathbf { U }$ and $\mathbf { V }$ are difference vectors along each of two lines, and that $\theta$ is the angle between the lines (measured from $\mathbf { U }$ to $\mathbf { V }$ ). In the previous notation, $\mathbf { U } = \mathbf { y } - \mathbf { x }$ and $\mathbf { V } = \mathbf { b } - \mathbf { a }$ . Elementary vector analysis tells us that

$$
\begin{array} { r } { \mathbf { U } \cdot \mathbf { V } = U _ { 0 } V _ { 0 } + U _ { 1 } V _ { 1 } = | \mathbf { U } | | \mathbf { V } | \cos ( \theta ) } \\ { \mathbf { U } \times \mathbf { V } = U _ { 0 } V _ { 1 } - U _ { 1 } V _ { 0 } = | \mathbf { U } | | \mathbf { V } | \sin ( \theta ) } \end{array}
$$

Many people try to get $\theta$ by using one or the other of the above relations, computing the vector norms and taking an inverse cosine or inverse sine. Big mistake! Not only are there quadrant ambiguities in the inverse trig functions, but there are also angles near the flat extrema of the sine and cosine functions where you can lose up to half of your significant figures in the answer. Not to mention the need to calculate square roots for the norms! The better approach is

$$
\theta = \mathtt { a t a n 2 } ( \mathbf { U } \times \mathbf { V } , \mathbf { U } \cdot \mathbf { V } ) = \mathtt { a t a n 2 } ( U _ { 0 } V _ { 1 } - U _ { 1 } V _ { 0 } , U _ { 0 } V _ { 0 } + U _ { 1 } V _ { 1 } )
$$

where atan2() is C’s or $\mathrm { C } { + } { + }$ ’s quadrant-sensitive arctangent function. That function allows either of its arguments to be zero and returns a value in the range $- \pi / 2$ to $\pi / 2$ . (An identical function exists in Fortran and most other languages.)

# 21.4.2 Lines in Three Dimensions

The immediate generalization of equation (21.4.12) to three-dimensional space gives the angle between two 3-vectors,

$$
\boldsymbol { \theta } = \mathsf { a t a n 2 } \left( | \mathbf { U } \times \mathbf { V } | , \mathbf { U } \cdot \mathbf { V } \right)
$$

Note the occurrence of the modulus of the vector cross product, which requires taking a square root.

Brevity constraints allow us to say only a little more about lines in three-dimensional space. The parameterization

$$
\mathbf { c } = \mathbf { a } + s \mathbf { v } ( - \infty < s < \infty )
$$

(equation 21.4.1 with $\mathbf { v } \equiv \mathbf { b } - \mathbf { a }$ ) still works, with a, $\mathbf { V }$ , and c now points in 3-space. The parameter $s$ at which a line intersects a plane specified by $\mathbf { N }$ and $D$ (see equation 21.3.16) is given by

$$
s = { \frac { D - \mathbf { a } \cdot \mathbf { N } } { \mathbf { v } \cdot \mathbf { N } } }
$$

with the denominator vanishing if the line is parallel to the plane.

The closest approach of a line to a point $\mathbf { q }$ occurs when

$$
s = { \frac { \left( \mathbf { q } - \mathbf { a } \right) \cdot \mathbf { v } } { | \mathbf { v } | ^ { 2 } } }
$$

You can also use this to see whether a line intersects a sphere in 3-space: Calculate the closest point on the line to the sphere’s center, and then check if the distance is less than the sphere’s radius (or compare squares of distances to avoid the square root).

Two lines, call them $\mathbf { a } + s \mathbf { v }$ and $\mathbf { x } + t \mathbf { u }$ , will not, in general, share a common point; rather, they will be skew to one another. However, their points of closest approach can be calculated as [2]

$$
s = { \frac { \operatorname* { d e t } \{ ( \mathbf { a } - \mathbf { x } ) , \mathbf { u } , \mathbf { u } \times \mathbf { v } \} \} } { | \mathbf { u } \times \mathbf { v } | ^ { 2 } } } \qquad t =  \frac { \operatorname* { d e t } \{ ( \mathbf { a } - \mathbf { x } ) , \mathbf { v } , \mathbf { u } \times \mathbf { v } \} \} }
$$

where det is the $3 \times 3$ determinant whose columns are the indicated 3-vectors. The denominator vanishes if the lines are parallel. If you really must check for an actual intersection, plug these values for $s$ and $t$ into the parametric forms for each line, and check whether the distance between two points thus obtained is less than some roundoff tolerance.

A common operation in computer graphics is to test whether a line intersects a triangle in three dimensions. To do this with methods already discussed, use equation (21.3.17) to get $\mathbf { N }$ and $D$ for the triangle’s plane. Then use equations (21.4.14) and (21.4.15) to get the line’s intersection with that plane. Finally, use equation (21.3.19) to get the barycentric coordinates $\alpha$ and $\beta$ of the intersection. If $\alpha$ , $\beta$ , and $\gamma \equiv 1 - \alpha - \beta$ are all positive, then the intersection is inside the triangle. See [4,1] for various ways to streamline this procedure.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/4c9928eddd49e7475338713148160b1e2fbd0b4bc7df6b0d885e139a7fe9b451.jpg)  
Figure 21.4.3. Polygons are classified as simple if they have no intersecting edge, as in (a) and (b), or complex (c) otherwise. Simple polygons are either convex (a) or concave (b).

# 21.4.3 Polygons

We define a polygon as a vector of $N$ points (vertices), numbered from 0 to $N - 1$ , and the $N$ directed line segments that connect them in cyclic order, that is 0 to 1, 1 to 2, : : :, $N - 2$ to $N - 1$ , and (importantly!) $N - 1$ to 0. (In some formulas below we will use the convention that vertex $N$ is to be taken as meaning vertex 0.)

We consider two polygons to be the same if they differ only by a cyclical renumbering of the points, so that all their line segments are the same. However, if we reverse the order of traversing the points, we consider the resulting polygon to be different. (For example, the sign of its area will change.) If the boundary of a region cannot be traversed by a single cyclical vector (e.g., the region between an outer square and an enclosed triangle), we don’t call it a polygon; other conventions are of course also possible.

With the definition given, it is useful to classify a polygon as either simple, meaning that none of its $N$ line segments intersect, or complex if there are one or more segment intersections. We classify simple polygons according to whether they are convex or concave. A convex polygon can be defined either by (i) all $N ( N { - } 1 ) / 2$ line segments connecting two vertices lie in its interior (or on its boundary), or (ii) its exterior angles all have the same sign (zeros allowed). Whichever property is taken as the definition, the other becomes a theorem. Figure 21.4.3 shows examples of the three types.

For simple polygons, the sum of the exterior angles is always $\pm 2 \pi$ . That is, you turn through exactly one circle in driving around the polygon. If the polygon is concave, then the sign of the exterior angles must be taken into account when doing the sum. This is shown in Figure 21.4.4. The sign of the $2 \pi$ is positive for a counterclockwise (CCW) traversal, negative for clockwise (CW).

Complex (that is, self-intersecting) polygons can also have exterior angles that sum to $2 \pi$ , as the polygon in Figure 21.4.3(c), so the exterior angles do not provide, in general, any magical way of finding intersections. However, one small bit of magic does exist: If the exterior angles of a polygon are all of one sign (or zero), and if they sum to $\pm 2 \pi$ , then the polygon is both simple and convex. This provides a very rapid way to test for the simple-and-convex case, but it does not distinguish between simple-concave and complex polygons. Doing so requires a detailed check for intersecting edges (which we will implement in code below).

Winding Number. If you sit on a point p in the plane, and watch someone drive around a polygon, then they will drive around you some net integer number of times (with the usual sign convention, CCW being positive). This is the polygon’s winding number with respect to a point. For simple polygons, the winding number is 1 for points inside a CCW polygon, $^ { - 1 }$ for points inside a CW polygon, and 0 for points outside. For complex polygons, however, there are no simple rules. Figure 21.4.5 shows a complicated case. Note that interior regions of a complex polygon can have winding number 0, so a point’s winding number (alone) does not determine whether it is inside or outside a complex polygon. Note also that the sum of a polygon’s exterior angles, divided by $2 \pi$ , is not necessarily the winding number of that polygon with respect to any point in the plane.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/68c528bf86d3264b5bb94cedb642b436956d9d244264ac3dafa4b07f4d4bf54a.jpg)  
Figure 21.4.4. The exterior angles of simple polygons sum to one full circle. (a) If the polygon is convex, all the angles have the same sign. (b) If the polygon is concave, one or more angles (here, the shaded angle) has opposite sign.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/93cf8b562a3520a8f1da1158e40f3bf7d8ada969a780320e8864c9881e5be34b.jpg)  
Figure 21.4.5. Complex polygon with different winding numbers (indicated by integers) around points in different regions. The total winding number of the polygon (sum of exterior angles divided by $2 \pi$ ) is 3, a value not realized in any single region. Note that interior regions can have winding number 0.

Doubtless the worst way to compute a polygon’s winding number with respect to a point $\mathbf { q }$ is to add up the $N$ incremental angles between $\mathbf { q }$ and consecutive vertices ${ \bf p } _ { i }$ of the polygon, that is,

$$
\operatorname { W . N . } ( { \mathbf { q } } ) = \frac { 1 } { 2 \pi } \sum _ { i = 0 } ^ { N - 1 } \angle ( { \mathbf { p } } _ { i + 1 } { \mathbf { q } } { \mathbf { p } } _ { i } )
$$

(with the usual convention $\mathbf { p } _ { N } \equiv \mathbf { p } _ { 0 } ,$ ). Even using the trick in equation (21.4.12) to get the angles, there is an enormous amount of unnecessary computation in this approach.

Instead, we can observe that if a polygon winds $M$ times around $\mathbf { q }$ , then its edges must cross any ray from $\mathbf { q }$ to infinity a net of exactly $M$ times, where ray crossings in the CCW direction are counted as positive, CW as negative. In particular, if we take the ray to be the horizontal ray to the right of $\mathbf { q }$ , we can immediately reject edges that fail to cross the horizontal line that contains $\mathbf { q }$ , and then check for the ray crossing (and its sign) with a single “left-of” test [5]. These ideas are embodied in the following routine.

polywind(const vector< Point<2> > &vt, const Point<2> &pt) {

Return the winding number of a polygon (specified by a vector of vertex points vt) around an arbitrary point pt.

Int i,np, wind $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
Doub d0,d1,p0,p1,pt0,pt1;   
np $=$ vt.size();   
pt0 $=$ pt.x[0];   
pt1 $=$ pt.x[1];   
p0 $=$ vt[np-1].x[0]; Save last vertex as ”previous” to first.   
p1 $=$ vt[np-1].x[1];   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; i<np; $\dot { \bf 1 } + +$ ) { Loop over edges. $\mathrm { ~ d 0 ~ } =$ vt[i].x[0]; d1 $=$ vt[i].x[1]; if (p1 $< =$ pt1) { if (d1 $>$ pt1 && Upward-crossing edge. Is pt to its left? (p0-pt0)\*(d1-pt1)-(p1-pt1)\*(d0-pt0) > 0) wind++; } else { if (d1 $< =$ pt1 && Downward-crossing edge. Is pt to its right? (p0-pt0)\*(d1-pt1)-(p1-pt1)\*(d0-pt0) < 0) wind-} $\mathtt { p 0 = d 0 }$ ; Current vertex becomes previous one. $\mathtt { p 1 } \mathtt { = d 1 }$ ;   
}   
return wind;

Is there a similarly efficient way to find the total winding number of a polygon ${ \bf p } _ { i }$ $( i \ : = \ : 0 , \ldots , N \ : - \ : 1 )$ , that is, the sum of its exterior angles divided by $2 \pi 2$ Yes. Consider the derived polygon whose vertex points $\mathbf { q } _ { i }$ are given by the vector differences

$$
\mathbf { q } _ { i } = \mathbf { p } _ { i + 1 } - \mathbf { p } _ { i } \qquad ( i = 0 , \ldots , N - 1 )
$$

Then the winding number of this derived polygon around the origin is just the total winding number of the original polygon. (Draw a picture if this isn’t immediately obvious to you.) The routine polywind() can be used for the computation.

Point Inside Polygon. How can you tell whether an arbitrary point $\mathbf { q }$ is inside or outside a polygon [5]? Let us first assume that your polygon is known to be simple. For simple polygons, two commonly used approaches are the “winding number method” and the “Jordan curve theorem method.” However, when these are each implemented efficiently, they become virtually identical!

The winding number method is simply to compute the winding number of the polygon around the point (e.g., using polywind(), above). If the answer is $\pm 1$ , then the point is inside the polygon. If it is zero, it is outside. Any other answer indicates that the polygon wasn’t simple as assumed.

The Jordan curve theorem method observes that any ray from the point to infinity will cross the polygon an odd number of times if the point is inside, or an even number of times if it is outside [Figure 21.4.6(a)]. If we implemented this in code, it would be almost identical to the code in polywind except for one detail: Instead of incrementing or decrementing a counter at each ray crossing (according to the direction of the crossing), we would always increment it. Then, at the end, we would check whether the counter is even or odd. But if polywind as written returns 0, it must have encountered the same number of increments as decrements, hence an even number of crossings. And if it returns $\pm 1$ (the only other possible value for a simple polygon), it must similarly have encountered an odd number. So the two methods are really the same.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/10c21a0c015b20914ff2b9698ec18a8417e84f33f77ed6e6bf8c0221220b557c.jpg)  
Figure 21.4.6. Is a point inside a polygon? (a) For a simple polygon, either the winding number, or the Jordan curve theorem (even or odd number of crossings of a ray) can be used. (b) For complex polygons, there is no simple test.

What if your polygon is not simple? As Figure 21.4.6(b) illustrates, you are in deep waters. Both the winding number method and the Jordan curve theorem method will say that the upper point in the figure is inside the complex polygon shown, and this seems intuitively correct. However, both methods will say that the lower point is outside the polygon. Indeed, there are some self-consistent ways of defining “insideness” for complex polygons that make this the case. The result is so counterintuitive, however, as to be useless in most practical applications. It is generally better just to avoid using the idea of “insideness” with complex polygons.

Classification of Polygons. We are now in a position to combine several of the ideas already introduced into a function that classifies any polynomial as either simple or complex, and (if it is simple) whether it is convex or concave, and whether it is CCW (total winding number 1) or CW (total winding number $^ { - 1 }$ ).

# Int ispolysimple(const vector< Point<2> $>$ &vt) {

Classifies a polygon specified by a vector of vertex points vt. Returns 0 if the polygon is complex (has intersecting edges). Returns $\pm 1$ if it is simple and convex. Returns $\pm 2$ if it is simple and concave. The sign of the returned value indicates whether the polygon is CCW $( + )$ or CW $( - )$ .

Int i,ii,j,jj,np,schg ${ \left. = 0 \right. }$ ,wind=0; Initialize sign change and winding number.   
Doub p0,p1,d0,d1,pp0,pp1,dd0,dd1,t,tp,t1,t2,crs,crsp $_ { 1 = 0 }$ .0;   
$\mathrm { n p } \ =$ vt.size();   
$\mathtt { p 0 } \ =$ vt[0].x[0]-vt[np-1].x[0];   
$\mathtt { p 1 } \ =$ vt[0].x[1]-vt[np-1].x[1];   
for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ,ii=1; i<np; $\dot { \bf 1 } + +$ ,ii++) { Loop over edges. if (ii $\begin{array} { r } { \mathrm { ~  ~ \omega ~ } = \mathrm { ~  ~ n p ~ } . } \end{array}$ ) $ { \mathrm { ~ \textrm ~ { ~ ~ } ~ } }  { \mathrm { 1 } }  { \mathrm { 1 } } { \mathrm { 1 } } = \mathrm { ~ 0 ~ }$ ; d0 $=$ vt[ii].x[0]-vt[i].x[0]; d1 $=$ vt[ii].x[1]-vt[i].x[1]; crs $=$ p0\*d1-p1\*d0; Cross product at this vertex. if (crs\*crsp $<$ 0) schg $= ~ 1$ ; Sign change (i.e., concavity) found. if (p1 <= 0.0) { Winding number logic as in polywind. if (d1 $> ~ 0 , 0$ && crs $> ~ 0 . 0$ ) wind++; } else { if (d1 $< = ~ 0 . 0$ && crs < 0.0) wind--; } $\mathtt { p 0 = d 0 }$ ; $\mathtt { p 1 } \mathtt { = d 1 }$ ; if (crs $! = ~ 0 . 0$ ) crsp = crs; Save previous cross product only if it has a   
} sign!

if (abs(wind) $\smash  ! = ~ 1 2$ ) return 0; Can already conclude polygon is complex. if (schg $\scriptstyle = = 0$ ) return (wind>0? 1 : -1); Polygon is simple and convex. Drat, we’ve exhausted all the quick tricks and now have to check all pairs of edges for intersections:

for ( $\scriptstyle { \dot { 1 } } = 0$ ,ii=1; i<np; $\dot { \bf 1 } + +$ ,ii $^ { + + }$ ) { if (i $\mathrm { \Omega _ { i } ~ = = ~ \mathrm { \Omega _ { n p } } }$ ) $\scriptstyle \dot { 1 } \dot { 1 } = 0$ ; $\mathtt { d 0 } \ =$ vt[ii].x[0]; ${ \tt d } 1 \ =$ vt[ii].x[1]; $\mathtt { p 0 } \ =$ vt[i].x[0]; $\mathtt { p 1 } \ =$ vt[i].x[1]; t ${ \bf \Phi } : { \bf p } = { \bf \Phi } 0 . 0$ ; for ( $\scriptstyle { \dot { \mathsf { J } } } = { \dot { \mathsf { 1 } } } + 1$ ,jj $= \dot { 1 } + 2$ ; j<np; j++,jj $^ { + + }$ ) { if (jj $\begin{array} { r } { \mathrm { ~  ~ \omega ~ } = \mathrm { ~  ~ n p ~ } . } \end{array}$ ) {if ( $\scriptstyle { \dot { 1 } } = = 0$ ) break; jj=0;} dd0 $=$ vt[jj].x[0]; dd1 $=$ vt[jj].x[1]; $\begin{array} { r l } { \tplus } & { { } = } \end{array}$ (dd0-d0) $^ *$ (p1-d1) - (dd1-d1) $^ *$ (p0-d0); if (t\*tp $< = ~ 0 . 0$ && j>i+1) { First loop is only to compute starting tp, pp0 $=$ vt[j].x[0]; hence test on j. pp1 $=$ vt[j].x[1]; t1 = (p0-dd0)\*(pp1-dd1) - (p1-dd1)\*(pp0-dd0); t2 = (d0-dd0)\*(pp1-dd1) - (d1-dd1)\*(pp0-dd0); if (t1\*t2 <= 0.0) return 0; Found an intersection, so done. } tp = t; }   
}   
return (wind>0? 2 : -2); No intersections found, so simple concave.

When ispolysimple finds that the quick indicators are not enough, and that it needs to check all pairs of edges for intersections, it does so by the obvious $O ( N ^ { 2 } )$ method of two nested loops. For small $N$ , say less than 10, this is likely as fast as any other strategy. If you are dealing with large numbers of large- $N$ polygons, however, you will want to substitute a method with better scaling in $N$ . One way, using the code from $\ S 2 1 . 8$ , would be to define a class for segments with a collides() method, then store the segments into a QO tree one at a time, looking for collisions at each step. (Don’t forget that adjacent edges of a simple polynomial are allowed to “collide” at their shared vertex.)

Area of Polygons. As a next topic, let us turn to the area of a polygon. The (signed) area of a polygon is the sum of the areas of each of its regions weighted by that region’s winding number. For simple polygons the area is thus what you would expect geometrically, except that its sign will be negative for a polygon traversed CW rather than CCW. (We previously saw this in the special case of triangles.) For a complex polygon like that shown in Figure 21.4.5, the answer is less intuitive (and generally less useful) since some regions, such as the interior region with winding number 0, are not counted at all, while others are counted (in this case) twice.

The great advantage of this definition of area, however, is that it results in a simple expression for the area that applies to both simple and complex polygons. Let $x _ { i }$ and $y _ { i }$ be, respectively, the 0 and 1 coordinates of the polygon’s vertex ${ \bf p } _ { i }$ , and let $\mathcal { A }$ be the polygon’s area. Then, in three equivalent forms,

$$
2 \mathcal { A } = \sum _ { i = 0 } ^ { N - 1 } x _ { i } y _ { i + 1 } - x _ { i + 1 } y _ { i }
$$

$$
\begin{array} { l } { \displaystyle = \sum _ { i = 0 } ^ { N - 1 } ( x _ { i + 1 } + x _ { i } ) ( y _ { i + 1 } - y _ { i } ) } \\ { \displaystyle = \sum _ { i = 0 } ^ { N - 1 } x _ { i } ( y _ { i + 1 } - y _ { i - 1 } ) } \end{array}
$$

Evaluation of any of these forms takes just one loop over the polygon’s vertices. (These formulas go back as far as Meister in 1769 and Gauss in 1795.)

Although we won’t derive equation (21.4.20) in detail, the middle form does have an intuitive interpretation. It sums the areas of trapezoids each with two points on the $y$ -axis $( x = 0$ ) at $y _ { i }$ and $y _ { i + 1 }$ , and with the other two points the points on the polygon at these $y$ ’s. In going around the polygon, negative-area trapezoids subtract from positive-area ones so as to leave just the area inside.

Interestingly, there are very similar formulas for the $x$ and $y$ coordinates of the centroid or center-of-mass of an arbitrary polygon [3],

$$
{ \begin{array} { l } { { \overline { { x } } } = { \frac { 1 } { 6 } } \displaystyle \sum _ { i = 0 } ^ { N - 1 } ( x _ { i + 1 } + x _ { i } ) ( x _ { i } y _ { i + 1 } - x _ { i + 1 } y _ { i } ) } \\ { { \overline { { y } } } = { \frac { 1 } { 6 } } \displaystyle \sum _ { i = 0 } ^ { N - 1 } ( y _ { i + 1 } + y _ { i } ) ( x _ { i } y _ { i + 1 } - x _ { i + 1 } y _ { i } ) } \end{array} } 
$$

Note the common subexpressions with equation (21.4.20), so that it is efficient to calculate the area and centroid position together.

Finally, a couple of polygon tidbits for your edification or amusement:

- If two simple polygons have the same area, then the first can be cut into a finite number of polygonal pieces that can be reassembled into the second. This is known as the Bolyai-Gerwien theorem. (The corresponding statement about polyhedra in three dimensions, “Hilbert’s Third Problem,” was proved false by Dehn in 1900.)   
The regular polygon with $N$ sides is constructible with a compass and straightedge if the factorization of $N$ contains only the factors 2, 3, 5, 17, 257, 257, and 65537 (whose odd members are the Fermat primes), with each odd factor occurring at most once. It is not known whether any other $N$ -gons are also constructible; but, if so, then their $N$ must contain a factor at least as   
large as $2 ^ { 2 ^ { 3 3 } } + 1$ . The product of the known Fermat primes, which is perforce the largest known constructible polygon with an odd number of sides, is $2 ^ { 3 2 } - 1 = 4 2 9 4 9 6 7 2 9 5$ , a number well known to computer trolls as the largest positive 32-bit integer. Go figure.

# CITED REFERENCES AND FURTHER READING:

Bowyer, A. and Woodwark, J. 1983, A Programmer’s Geometry (London: Butterworths).   
Schneider, P.J. and Eberly, D.H. 2003, Geometric Tools for Computer Graphics (San Francisco: Morgan Kaufmann), $\ S 1 1 . 1 . 2 [ 1 ]$   
de Berg, M., van Kreveld, M., Overmars, M., and Schwarzkopf, O. 2000, Computational Geometry: Algorithms and Applications, 2nd revised ed. (Berlin: Springer), Chapter 2.   
O’Rourke, J. 1998, Computational Geometry in C, 2nd ed. (Cambridge, UK: Cambridge University Press), $\ S 7 . 4$ .   
Goldman, R. 1990, “Intersection of Two Lines in Three-Space,” in Graphics Gems, Glassner, A.S., ed. (San Diego: Academic Press).[2]   
Bashein, G. and Detmer, P.R. 1994, “Centroid of a Polygon,” in Graphics Gems IV, Heckbert, P.S., ed. (Cambridge, MA: Academic Press).[3]   
Sunday, D. $^ { 2 0 0 7 + }$ , at http://softsurfer.com/algorithm_archive.htm.[4]   
Haines, E. 1994, “Point in Polygon Strategies,” in Graphics Gems IV, Heckbert, P.S., ed. (Cambridge, MA: Academic Press).[5]   
Wikipedia $^ { 2 0 0 7 + }$ , “Polygon,” at http://en.wikipedia.org.

# 21.5 Spheres and Rotations

The surface of the Earth is called a 2-sphere by topologists, but a 3-sphere by geometers; so the term $n$ -sphere is somewhat unclear. We’ll say “sphere in $n$ dimensions” to avoid any ambiguity. (For Earth, $n = 3 .$ .) Sphere refers to the surface, ball to the interior volume.

A sphere of radius $r$ in $n$ dimensions, centered on the origin, is the locus of points for which

$$
x _ { 0 } ^ { 2 } + \dots + x _ { n - 1 } ^ { 2 } = r ^ { 2 }
$$

Points on the sphere in $n$ dimensions can be specified by $n - 1$ angular coordinates, roughly the analogs of latitude and longitude on the sphere in three dimensions,

$$
\begin{array} { c } { { x _ { 0 } = r \cos \psi _ { 0 } } } \\ { { \ } } \\ { { x _ { 1 } = r \sin \psi _ { 0 } \cos \psi _ { 1 } } } \\ { { \ } } \\ { { \ldots } } \\ { { \ } } \\ { { x _ { n - 2 } = r \sin \psi _ { 0 } \sin \psi _ { 1 } \ldots \cos \psi _ { n - 2 } } } \\ { { \ } } \\ { { x _ { n - 1 } = r \sin \psi _ { 0 } \sin \psi _ { 1 } \ldots \sin \psi _ { n - 2 } } } \end{array}
$$

All the angles except the last have the range

$$
0 \leq \psi _ { i } \leq \pi , \qquad i = 0 , \ldots , n - 3
$$

i.e., are “latitude-like.” The last angle is “longitude-like,”

$$
0 \leq \psi _ { n - 2 } \leq 2 \pi
$$

The surface area $S _ { n }$ of the sphere in $n$ dimensions has a simple recurrence,

$$
\begin{array} { l l } { { S _ { 1 } = 2 } } & { { \mathrm { ( t w o  p o i n t s ) } } } \\ { { S _ { 2 } = 2 \pi r } } & { { \mathrm { ( c i r c u m f e r e n c e ~ o f ~ c i r c l e ) } } } \\ { { S _ { n } = { \displaystyle \frac { 2 \pi r ^ { 2 } } { n - 2 } } S _ { n - 2 } , } } & { { n > 2 } } \end{array}
$$

The volume $V _ { n }$ of the $n$ -dimensional ball is equal to $r / n$ times the area of the enclosing sphere in $n$ dimensions, and also has a simple recurrence,

$$
{ \begin{array} { r l r } & { V _ { 1 } = 2 r \qquad } & { { \mathrm { ( l e n g t h ~ o f ~ l i n e ) } } } \\ & { V _ { 2 } = \pi r ^ { 2 } \qquad } & { { \mathrm { ( a r e a ~ o f ~ c i r c l e ) } } } \\ & { \qquad \cdots } \\ & { V _ { n } = { \frac { r } { n } } S _ { n } = { \frac { 2 \pi r ^ { 2 } } { n } } V _ { n - 2 } } \end{array} }
$$

Closed-form formulas require a gamma function,

$$
\begin{array} { l } { { S _ { n } = \displaystyle \frac { 2 \pi ^ { n / 2 } } { \Gamma ( \frac { 1 } { 2 } n ) } r ^ { n - 1 } } } \\ { { { \cal V } _ { n } = \displaystyle \frac { 2 \pi ^ { n / 2 } } { n \Gamma ( \frac { 1 } { 2 } n ) } r ^ { n } } } \end{array}
$$

As $n$ becomes large, the ratio of the volume of a ball to the volume of the circumscribed (hyper-) cube rapidly becomes small,

$$
{ \frac { V _ { n } } { 2 ^ { n } } }  0 , \qquad n  \infty
$$

# 21.5.1 Picking a Random Point on the Sphere

You don’t get a random point on the sphere in $n$ dimensions by picking uniformly random values for the $n - 1$ angles in equation (21.5.2), just as you don’t get a random point on the Earth’s surface by throwing darts at a Mercator map (or any other non-equal-area projection).

An elegant general method is to generate $n$ independent, identically distributed, normal (Gaussian) deviates of zero mean, say $y _ { 0 } , \ldots , y _ { n - 1 }$ (see $\ S 7 . 3 )$ , and then calculate a point $\mathbf { X }$ on the unit sphere in $n$ dimensions by

$$
\mathbf { x } = { \frac { \mathbf { y } } { | \mathbf { y } | } }
$$

or, in other words,

$$
x _ { i } = y _ { i } \Bigg / \sqrt { \sum _ { j = 0 } ^ { n - 1 } y _ { j } ^ { 2 } }
$$

This works because the spherically symmetric Gaussian distribution in $n$ dimensions trivially factorizes into a product of independent one-dimensional Gaussians. If you want a random point inside the enclosed $n$ -volume, generate an additional uniform random deviate $u$ in Œ0; 1 and calculate the point’s coordinates as

$$
x _ { i } = u ^ { 1 / n } y _ { i } \Bigg / \sqrt { \sum _ { j = 0 } ^ { n - 1 } y _ { j } ^ { 2 } }
$$

You can of course scale to any other radius of sphere.

Faster special methods are available for the spheres in two, three, and four dimensions. For two dimensions, the circle, pick $u _ { 0 }$ and $u _ { 1 }$ uniform in $[ - 1 , 1 ]$ , rejecting choices for which $u _ { 0 } ^ { 2 } + u _ { 1 } ^ { 2 } > 1$ . This picks a random point inside the unit circle. Now scale in the obvious way to get a point on the circle,

$$
x _ { 0 } = \frac { u _ { 0 } } { \sqrt { u _ { 0 } ^ { 2 } + u _ { 1 } ^ { 2 } } } , \qquad x _ { 1 } = \frac { u _ { 1 } } { \sqrt { u _ { 0 } ^ { 2 } + u _ { 1 } ^ { 2 } } }
$$

(We already discussed this method in $\ S 7 . 3$ , under Cauchy deviates.)

A faster method for three dimensions, also using only two random deviates, is due to Marsalgia [1]. Pick a point inside the unit circle $( u _ { 0 } , u _ { 1 } )$ as above. Then a random point on the sphere in three dimensions is

$$
\begin{array} { l } { { x _ { 0 } = 2 u _ { 0 } \sqrt { 1 - u _ { 0 } ^ { 2 } - u _ { 1 } ^ { 2 } } } } \\ { { \ } } \\ { { x _ { 1 } = 2 u _ { 1 } \sqrt { 1 - u _ { 0 } ^ { 2 } - u _ { 1 } ^ { 2 } } } } \\ { { \ } } \\ { { x _ { 2 } = 1 - 2 ( u _ { 0 } ^ { 2 } + u _ { 1 } ^ { 2 } ) } } \end{array}
$$

For the sphere in four dimensions, pick two independent points inside the unit circle as above, $( u _ { 0 } , u _ { 1 } )$ and $( u _ { 2 } , u _ { 3 } )$ . Then a random point on the sphere in four dimensions is [1]

$$
\begin{array} { r l } & { x _ { 0 } = u _ { 0 } } \\ & { x _ { 1 } = u _ { 1 } } \\ & { x _ { 2 } = u _ { 2 } \sqrt { \cfrac { 1 - u _ { 0 } ^ { 2 } - u _ { 1 } ^ { 2 } } { u _ { 2 } ^ { 2 } + u _ { 3 } ^ { 2 } } } } \\ & { x _ { 3 } = u _ { 3 } \sqrt { \cfrac { 1 - u _ { 0 } ^ { 2 } - u _ { 1 } ^ { 2 } } { u _ { 2 } ^ { 2 } + u _ { 3 } ^ { 2 } } } } \end{array}
$$

Unfortunately, there is no known generalization to higher dimensions.

# 21.5.2 Picking a Random Rotation Matrix

Don’t confuse this with picking a point on a sphere. A rotation matrix $\mathbf { M }$ in $n$ dimensions is an orthogonal $n \times n$ matrix. For a proper rotation, M must have determinant 1. The other possibility, determinant $^ { - 1 }$ , represents an improper rotation, decomposable into a proper rotation followed by a reflection. The rotation matrix M maps any point $\mathbf { X }$ to a new point $\mathbf { x } ^ { \prime }$ by

$$
\mathbf { x } ^ { \prime } = \mathbf { M } \cdot \mathbf { x }
$$

A general method for picking a uniformly random rotation matrix is to fill an $n \times n$ matrix $\mathbf { G }$ with independent, identically distributed, normal (Gaussian) deviates of zero mean. Then, use QRdcmp in $\ S 2 . 1 0$ to construct the $\boldsymbol { \mathcal { Q } R }$ decomposition, namely ${ \bf G } = { \bf Q } \cdot { \bf R }$ . Except for the possibility that it might have the wrong sign of determinant, the matrix $\mathbf { Q }$ is now a uniformly random rotation matrix. The method used in QRdcmp is to apply $n - 1$ Householder transformations, each of which is a reflection with determinant $^ { - 1 }$ . Thus, to get determinant 1, we do nothing to $\mathbf { Q }$ if $n$ is odd; if $n$ is even, we simply interchange any pair of rows in $\mathbf { Q }$ , giving the final answer.

For large $n$ the work of doing the decomposition scales as $O ( n ^ { 3 } )$ , which can be burdensome. For faster, but more complicated, methods, see [2,3].

Faster special methods are available for two and three dimensions. A random two-dimensional rotation matrix has components that are the sine and cosine of a random angle $\theta$ in $[ 0 , 2 \pi ]$ ,

$$
\left( \begin{array} { l l } { \cos \theta } & { \sin \theta } \\ { - \sin \theta } & { \cos \theta } \end{array} \right)
$$

We get the components without trigonometric function calls by using (21.5.12) to find a random point on the unit circle and then taking cos $\theta = x _ { 0 }$ and $\sin \theta = x _ { 1 }$ .

In the case of three dimensions, a fast method is to use equation (21.5.14) to generate a random point on the sphere in four dimensions, and then to construct the $3 \times 3$ orthogonal matrix,

$$
{ \left[ \begin{array} { l l l } { 1 - 2 ( x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } ) } & { 2 ( x _ { 0 } x _ { 1 } - x _ { 3 } x _ { 2 } ) } & { 2 ( x _ { 0 } x _ { 2 } + x _ { 3 } x _ { 1 } ) } \\ { 2 ( x _ { 0 } x _ { 1 } + x _ { 3 } x _ { 2 } ) } & { 1 - 2 ( x _ { 0 } ^ { 2 } + x _ { 2 } ^ { 2 } ) } & { 2 ( x _ { 1 } x _ { 2 } - x _ { 3 } x _ { 0 } ) } \\ { 2 ( x _ { 0 } x _ { 2 } - x _ { 3 } x _ { 1 } ) } & { 2 ( x _ { 1 } x _ { 2 } + x _ { 3 } x _ { 0 } ) } & { 1 - 2 ( x _ { 0 } ^ { 2 } + x _ { 1 } ^ { 2 } ) } \end{array} \right] }
$$

which will be uniformly random among all rotations [4,5].

# CITED REFERENCES AND FURTHER READING:

Marsaglia, G. 1972, “Choosing a Point from the Surface of a Sphere,” Annals of Mathematical Statistics,vol.43, pp. 645-646.[1]

Genz, A. 2000, “Methods for Generating Random Orthogonal Matrices,” in Monte Carlo and Quasi-Monte Carlo Methods,Proceedings of the Third International Conference on Monte Carlo and Quasi-Monte Carlo Methods in Scientific Computing (MCQMC98) (Berlin: Springer).[2]

Anderson, T.W., Olkin, I., and Underhill, L.G. 1987, “Generation of Random Orthogonal Matrices,” SIAM Journal on Scientific and Statistical Computing, vol. 8, pp. 625–629.[3]

Shoemake, K. 1985, “Animating Rotation with Quaternion Curves,” Computer Graphics, Proceedings of SIGGRAPH 1985, vol. 19, pp. 245–254.[4]

Shoemake, K. 1992, “Uniform Random Rotations,” in Graphics Gems III, Kirk, D., ed. (Cambridge, MA: Academic Press), pp. 124–132.[5]

# 21.6 Triangulation and Delaunay Triangulation

We can informally define a triangulation of a set of $N$ points in the plane as follows: Connect the given points by straight-line segments as many times as you can without any two segments crossing. When you can’t connect any more, you have a triangulation. Obviously there are many triangulations of a given set of points. Figure 21.6.1 shows three triangulations of the same set of 50 points. Two are “random,” where the informal definition was pretty much followed literally. The third one is a very special triangulation, called a Delaunay triangulation. In a sense that we will make more precise below, it is the triangulation whose triangles best avoid small angles and long sides.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/11cdeb7cc639bb45b2322c0e953725fdc3f32445d3651e53347cf804e5cce30a.jpg)  
Figure 21.6.1. Three triangulations of the same 50 random points: (a) and (b) are “bad” (random) triangulations, while (c) is a “good” (Delaunay) triangulation. The number of lines and triangles is the same in each case.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/4b38fe68131e78b71d2580862b591d57cdb05ec7e6cdc101ebe2a820384c6ca5.jpg)  
Figure 21.6.2. How to count lines and triangles in a triangulation. (a) Each triangle “uses up” $1 / 2$ of a point, and $_ { 3 / 2 }$ lines. (b) The $n$ points in the convex hull “use up” $n / 2 + 1$ points and $n / 2$ lines.

All triangulations of a given set of points have the same outer boundary, called the convex hull of the point set. This should be evident, again informally, from the definition of triangulation: A line segment (edge) on the outer convex boundary can’t interfere with any other actual or potential interior edges, so it will always be added before the stopping rule is reached. The number of points $n$ (and also edges) in the convex hull is at least three, and can be as large as $N$ , e.g., if the points all lie on a circle. (Here and below, we will ignore degenerate cases like “all points lie on a line.”)

It is surprising, perhaps, that all triangulations of a given point set have the same number of lines $( L )$ and triangles $( T )$ , given explicitly by the relations

$$
\begin{array} { c } { { L = 3 N - n - 3 } } \\ { { T = 2 N - n - 2 } } \end{array}
$$

The proof, known to Gauss, is very easy if you consult Figure 21.6.2. Since the interior angles of a triangle sum to $\pi$ radians, each triangle “uses up” half a point’s worth of angle. It is useful to think about each line as being two half-lines, representing the two possible directions of traversal in clockwise triangles. Then, each triangle uses up three half-lines. We must separately account for the vertices on the convex hull, as follows: Each such point uses up $\pi$ radians on its own (dark-shaded angles in the figure), plus (sum of the light-shaded exterior angles) $2 \pi$ additional radians in going around the convex hull. These considerations give the relations

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/ac7135ccacbdd646a3c4c0579567194346c663d3b20f57d43fced5df16f1c747.jpg)  
Figure 21.6.3. Example of a triangulation with $N = 1 2$ , $n = 6$ , $T = 1 6$ , and $L = 2 7$ , values that satisfy equation (21.6.1).

$$
\begin{array} { r l r l } { { 2 } \pi N = \pi T + \pi n + 2 \pi } & { } & { { } { \mathrm { ( a c c o u n t ~ f o r ~ r a d i a n s ) } } } \\ { 2 L = 3 T + n } & { } & { { } { \mathrm { ( a c c o u n t ~ f o r ~ h a l f - l i n e s ) } } } \end{array}
$$

which can be rearranged to give equation (21.6.1). Figure 21.6.3 shows the triangulation of Figure 21.6.2(b) with its points and triangles enumerated.

# 21.6.1 Delaunay Triangulation

Boris Nikolaevich Delone (1890–1980), a Russian mathematician also celebrated as a rock climber, first published the ideas behind Delaunay triangulation in 1934. Since his paper was written in French, his name was transliterated so as to be pronounced (approximately) correctly by French speakers. A better English pronunciation might be “dyeh-LOAN-yeh.”

Delaunay triangulations have a number of remarkable properties and can be defined in various abstract ways. However, we’ll take as the definition one very concrete property, shown in Figure 21.6.4. Consider all triangulations in which four points, $A , B , C , D$ ; are the vertices of two back-to-back triangles. Then, one can get a different triangulation by deleting the common edge ( $B D$ in the figure) and replacing it by the other diagonal of the quadrilateral ( $A C$ in the figure). A Delaunay triangulation is defined as one that always chooses the diagonal that gives the largest minimum angle for the six interior angles in the two triangles. The edge shown as $B D$ is thus illegal for a Delaunay triangulation, while $A C$ is termed legal. Changing a triangulation from an illegal edge to a legal one is called an edge flip. When any two triangles have a common edge, exactly one configuration, unchanged or edgeflipped, is legal (unless all four points lie on a circle, in which case both are legal).

This “largest minimum angle” property is geometrically equivalent to other statements about the points $A , B , C , D$ . One such statement is that the circumcircle of an illegal triangle, like $A B D$ or $B C D$ in part (a) of the figure, always contains another point, $C$ or $A$ , respectively. For a legal triangle, as in part (b) of the figure, this is never the case. One can use this as a starting point to prove the theorem:

- The circumcircle of any triangle in a Delaunay triangulation contains no other vertices.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/a455ee9cb6a0afbdbe5d7bccf2b83cf048f180f403a52597d0117df233c41498.jpg)  
Figure 21.6.4. A Delaunay triangulation can be defined as one in which back-to-back triangles always have a larger minimum angle than they would have if their common edge were flipped to the other diagonal. Equivalently, any triangle’s circumcircle does not contain another vertex. A so-called edge flip converts (a) to (b) in the figure.

Although the largest minimum angle property was defined locally, for one quadrilateral at a time, it can be shown to imply a remarkable global theorem:

- Among all triangulations of a set of points, a Delaunay triangulation has the largest minimum angles, as defined by sorting all angles from smallest to largest and comparing lexicographically to the angles of any other triangulation.

Comparing lexicographically means: First compare the smallest angle; if there is a winner, stop. If there is a tie on the smallest angle, compare the second-smallest angle. And so on.

Another theorem is

- Two vertices are connected by a Delaunay edge if and only if there is some circle that contains them and contains no other vertices.

If the points in a set have generic positions, meaning that no three are collinear and no four lie on the same circle, then the Delaunay triangulation exists and is unique; any method for constructing it will give the identical set of triangles.

You might wonder whether a Delaunay triangulation is also a minimum weight triangulation, defined as the triangulation with the smallest total of edge lengths. The answer is, in general, no. While minimum weight triangulations might be useful in applications, it is not even known whether they can be constructed in less than time that grows exponentially with $N$ . Delaunay construction, on the other hand, is fast, ${ \cal O } ( N \log N )$ . So, in practice, Delaunay is what we’ve got!

So, how do we construct a Delaunay triangulation? Conceptually, we can start with any triangulation and then eliminate illegal edges, by edge flips, as long as possible. This must terminate in a Delaunay triangulation after a finite number of flips because (i) each flip changes and increases the lexicographic order in the list of angles, and (ii) there are only a finite number of possible triangulations. Although, as stated, this is not an efficient algorithm, it can be readily be turned into one, the so-called randomized incremental algorithm [1].

This algorithm, which we now implement, is “incremental” in that it adds points to the triangulation one at a time, maintaining a Delaunay triangulation at each stage. It is “randomized” in that the points are added in a random order. It turns out that the randomization (almost) guarantees ${ \cal O } ( N \log N )$ expected time for the algorithm. (Without randomization, one could encounter pathological cases with

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/4e5efbc3c4454458efa0442979fc0586d052eeffcbc06c8768f188151b3ed415.jpg)  
Figure 21.6.5. Steps in inserting a new point into a Delaunay triangulation. (a) Connect new point $P$ to vertices of enclosing triangle. (b) Check enclosing triangle for illegal edges (here, replace $Q R$ by $P S$ ). (c) Recursively check any new triangles created that have $P$ as a vertex. (Here, $R S$ is legal, so we terminate.)

$O ( N ^ { 2 } )$ running time.)

Figure 21.6.5 shows the procedure for adding a new point $P$ that lies within an existing triangle. First, connect it to the vertices of the enclosing triangle. This creates three new triangles. (We exclude the special case where $P$ is exactly on an existing line. More on this below.) Next, check whether the edges opposite $P$ in the three new triangles are legal or illegal. If they are illegal, do edge flips. Each edge flip creates two new triangles with $P$ as a vertex, and (therefore) with two edges opposite $P$ that now also need to be checked for legality. So the process is recursive, but it never wanders away from $P$ . That is the key point: The only edges that can be made illegal by inserting point a point $P$ are edges opposite $P$ in triangles that include $P$ . The proof that the algorithm is ${ \cal O } ( N \log N )$ uses this fact, and then bounds the average number of triangles of which $P$ can be a vertex by relations like those of equation (21.6.1). (For details in the proof, see [2].)

Since, up to now, we only know how to add a point $P$ that falls inside the triangulation, how can we get started? An easy way is to add three “fictitious” points to the set of points, forming a very large starting triangle that will enclose all the “real” points subsequently added. Then, at the very end, the fictitious points and all edges connecting to them are removed. Strictly speaking, the fictitious points must actually be treated as if at infinity (thus requiring special logic in the code whenever they are referenced). If their distance is merely finite, the constructed triangulation may be “not-quite” Delaunay. For example, its outer boundary (convex hull) could in unusual cases be left slightly concave, with small negative angles on the order of the diameter of the “real” point set divided by the distance to the “fictitious” points.

That’s enough general information. We next get into the details.

# 21.6.2 Implementation Details

Since most readers skip a section with this title, this is a good place for us to confess a couple of dirty tricks in our Delaunay implementation, whose purpose is to keep the code and its explication to manageable length. If you need a bullet-proof Delaunay code, with no such tricks, a Web search will turn up several that are freely available. Our code is short and fast, and fine for its intended purpose; but it is approximate in two respects: First, we don’t take the initial bounding triangle off to infinity (as we sanctimoniously advised, above). Instead, it lies at a distance of about bigscale (an adjustable parameter, default value 1000), measured in units of the bounding-box size of the set of points. Second, we don’t provide for the special case, mentioned above, where the point being added falls on an existing edge (or does so within roundoff tolerance). For generic point locations, this should “never” happen; but in real life it “always” happens, because users love to try test examples with points in regular patterns! When we detect this problem, we randomly alter the location of the offending point by a small fraction fuzz (another adjustable parameter, default $1 0 ^ { - 6 }$ ) of the bounding box dimensions.

A very important implementation detail, not yet discussed, is how to find in which existing triangle a new point lies. Conceptually, we might throw the triangles into a QO tree (-21.8), but this would not yield the desired ${ \cal O } ( N \log N )$ behavior for our algorithm. A better solution, well established in the literature, is to maintain a tree structure of the descendants of any given triangle that ever existed in the construction. That is, starting with the huge “root” triangle, whenever a triangle is subdivided into three new triangles, we set pointers to its three daughters. And, when two triangles are lost in an edge flip, and two new triangles are created, we make the new triangles daughters of both of the lost triangles (even though each lost triangle contains only a part of each new one). In this scheme a triangle has two or three daughters at most, so we can easily reserve space for the pointers explicitly (i.e., no expandable linked lists needed).

With this structure, it is very fast to locate a point within the existing triangulation: Start at the root triangle, and recursively pick whichever daughter contains the point. When you reach a terminal node in the tree, you will have found a triangle in the current triangulation that contains the point. We thus need a structure for a “triangle element” or Triel:

struct Triel {   
Structure for an element in a descendancy tree of triangles, each having at most three daughters. Point<2> \*pts; Pointer to the array of the points. Int p[3]; The triangle’s three vertices, always in CCW order. Int d[3]; Pointers for up to three daughters. Int stat; Nonzero if this element is “live.” void setme(Int a, Int b, Int c, Point<2> \*ptss) { Set the data in a Triel. pts $=$ ptss; p[0] $=$ a; p[1] $=$ b; ${ \mathfrak { p } } [ 2 ] \ = \ { \mathfrak { c } } ;$ ; d[0] $= \textrm { d } [ 1 ] ~ = ~ \textrm { d } [ 2 ] ~ = ~ - 1$ ; The values $^ { - 1 }$ mean no daughters. stat $\ l = \ 1$ ; Create as “live.” } Int contains(Point<2> point) { Return 1 if point is in the triangle, 0 if on boundary, $^ { - 1 }$ if outside. (CCW triangle is assumed.) Doub d; Int i,j,ztest $\mathit { \Theta } = \mathit { \Theta } 0$ ; for (i=0; i<3; $\dot { 1 } + +$ ) { ${ \dot { ] } } \ =$ (i+1) %3; d $=$ (pts[p[j]].x[0]-pts[p[i]].x[0]) $^ *$ (point.x[1]-pts[p[i]].x[1]) (pts[p[j]].x[1]-pts[p[i]].x[1])\*(point.x[0]-pts[p[i]].x[0]); if (d < 0.0) return $^ { - 1 }$ ; if ( $\mathrm { ~ d ~ } = = \mathrm { ~ 0 ~ . 0 } ,$ ) ztest $\ c = ~ 1$ ; return (ztest? 0 : 1); }   
};

We create an big enough array of Triels at the start, and use integers to point to array elements. We’ve omitted any explicit constructor or assignment operators in Triel, since they are not needed for our use here. Be sure to add them if you use Triel in any other way.

We will need a way to do two other fast lookups: (1) Given a point and opposite edge in a triangle, find the fourth point in the quadrilateral, that is, the point (if any) on the other side of the given edge. (2) Given three points, find the index of their triangle (if it exists) in an array of Triel elements. Our strategy is to use hash memories (respectively called linehash and trihash) for these two functions. In particular, whenever we create a triangle (always CCW) with vertices $A , B , C$ , we store an index pointing to each point under a specially constructed key,

$$
\mathtt { l i n e h a s h } ( h ( B ) - h ( C ) )  A
$$

where the function $h$ is a 64-bit hash function, and “et cyc.” means do the same thing for the other two cyclic permutations of $A , B , C$ . The trick here is that, if we ever want to find the point on the other side of edge $B C$ , we just look for a key $h ( C ) - h ( B )$ (“negative” of the key in equation 21.6.3) in the hash table. The similar trick for storing and retrieving Triels is that, when we create a Triel at location $j$ in the storage array, we set

$$
\mathrm { \ t r i h a s h } ( h ( A ) \ \hat { \ } - \ h ( B ) \ \hat { \ } - \ h ( C ) ) \gets j
$$

where ^ is the XOR operation. Since this key is symmetric in $A , B , C$ ; we can find a triangle knowing its vertices in any order.

Since we are computing hash keys “by hand,” we can signal the two hash memories to use a null (therefore fast) hash of their own. That, and a utility for determining whether a point is inside the circumcircle of three other points, are the following two code fragments:

Doub incircle(Point<2> d, Point<2> a, Point<2> b, Point<2> c) Return positive, zero, or negative value if point d is respectively inside, on, or outside the circle through points a, b, and c.

Circle cc = circumcircle(a,b,c); Routine defined in $\ S 2 1 . 3$ .   
Doub radd $=$ SQR(d.x[0]-cc.center.x[0]) $^ +$ SQR(d.x[1]-cc.center.x[1]);   
return (SQR(cc.radius) - radd);

# }

# struct Nullhash {

Null hash function. Use a key (assumed to be already hashed) as its own hash. Nullhash(Int nn) {} inline Ullong fn(const void \*key) const { return $^ *$ ((Ullong \*)key); }   
};

These are all the preliminaries we need before declaring the Delaunay structure.

# struct Delaunay {

Structure for constructing a Delaunay triangulation from a given set of points. Int npts,ntri,ntree,ntreemax,opt; Number of points, triangles, elements in the Doub delx,dely; Triel list, and maximum of same. Size vector< Point<2> $>$ pts; of the bounding box. vector<Triel> thelist; The list of Triel elements. Hash<Ullong,Int,Nullhash> \*linehash; Create the hash memories with null hash Hash<Ullong,Int,Nullhash> \*trihash; function. Int \*perm; Delaunay(vector<Point<2> $>$ &pvec, Int options $\mathit { \Theta } = \mathit { \Theta } _ { 0 } )$ ; Construct the Delaunay triangulation from a vector of points. The variable options is used by some applications. Ranhash hashfn; The raw hash function. Doub interpolate(const Point<2> &p, const vector<Doub> &fnvals, Doub defaultval ${ = } 0$ .0); The next four functions are explained in detail below. void insertapoint(Int r); Int whichcontainspt(const Point<2> &p, Int strict $\mathit { \Theta } = \mathit { \Theta } 0 )$ ; Int storetriangle(Int a, Int b, Int c); void erasetriangle(Int a, Int b, Int c, Int d0, Int d1, Int d2); static Uint jran; Random number counter. static const Doub fuzz, bigscale;   
};   
const Doub Delaunay::fuzz $\ l = \ 1$ .0e-6; Adjust if you wish. See text.   
const Doub Delaunay::bigscale $=$ 1000.0; Adjust if you wish. See text.   
Uint Delaunay::jran $=$ 14921620;

The variable jran is used in conjunction with the hash function as a convenient random number generator. The function interpolate() is for the application of interpolating a function on an irregular mesh, to be discussed in $\ S 2 1 . 7$ . Everything else should become clear as we proceed.

The action starts with the constructor. We compute a bounding box for the set of points, construct and store the “huge” root triangle enclosing the points, create a random permutation to be the order in which points are added, and then (for the real work) call the function insertapoint() for each point in turn. After that there is just some cleanup housekeeping.

Delaunay::Delaunay(vector< Point<2> $>$ &pvec, Int options) : npts(pvec.size()), ntri(0), ntree(0), ntreemax(10\*npts+1000), opt(options), pts(npts+3), thelist(ntreemax) {   
Construct Delaunay triangulation from a vector of points pvec. If bit 0 in options is nonzero,   
hash memories used in the construction are deleted. (Some applications may want to use them   
and will set options to 1.) Int j; Doub xl,xh,yl,yh; linehash $=$ new Hash<Ullong,Int,Nullhash>(6\*npts+12,6\*npts+12); trihash $=$ new Hash<Ullong,Int,Nullhash>(2\*npts+6,2\*npts+6); perm $=$ new Int[npts]; Permutation for randomizing point order. $\mathbf { x } 1 \ = \ \mathbf { x } \mathbf { h } \ =$ pvec[0].x[0]; Copy points to local store and calculate their $\mathrm { { y } 1 ~ = ~ \mathrm { { y h } ~ = ~ } }$ pvec[0].x[1]; bounding box. for $( \ j = 0$ ; j<npts; ${ \mathrm { j } } + + { \mathrm { . } }$ ) { pts[j] $=$ pvec[j]; perm[j] $=$ j; if (pvec[j].x[0] < xl) xl $=$ pvec[j].x[0]; if (pvec[j].x[0] $>$ xh) xh $=$ pvec[j].x[0]; if (pvec[j].x[1] $<$ yl) yl $=$ pvec[j].x[1]; if (pvec[j].x[1] $>$ yh) yh $=$ pvec[j].x[1]; } delx $=$ xh - xl; Store bounding box dimensions, then construct dely $=$ yh - yl; the three fictitious points and store them. pts[npts] $=$ $\mathtt { P o i n t } < 2 > ( 0 \_ 5 * ( \mathrm { x 1 \_ + \ x h } )$ , yh $^ +$ bigscale\*dely); pts[npts+1] $=$ Point<2>(xl - 0. $^ { 5 \ast }$ bigscale\*delx,yl - 0.5\*bigscale\*dely); pts[npts+2] $=$ Point<2>(xh $^ +$ 0.5\*bigscale\*delx,yl - 0.5\*bigscale\*dely); storetriangle(npts,npts+1,npts $+ 2 )$ ; Create a random permutation: for (j=npts; j>0; j--) SWAP(perm[j-1],perm[hashfn.int64(jran $^ { + + }$ ) % j]); for ( $\scriptstyle { \dot { \ j } } = 0$ ; j<npts; ${ \mathrm { j } } + + { \mathrm { . } }$ ) insertapoint(perm[j]); All the action is here! for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<ntree; ${ \dot { \mathsf { J } } } ^ { + + }$ ) { Delete the huge root triangle and all of its conif (thelist[j].stat $>$ 0) { necting edges. if (thelist[j].p[0] $> =$ npts thelist[j].p[1] >= npts || thelist[j].p[2] $> =$ npts) { thelist[j].stat $\begin{array} { r l } { \mathbf { \Phi } } & { { } = \mathbf { \Phi } - \mathbf { 1 } \mathbf { \Phi } } \end{array}$ ; ntri--; } if (!(opt & 1)) { Clean up, unless option bit says not to. delete [] perm; delete trihash; delete linehash; }   
}

The guts of the algorithm as previously described are in insertapoint(). We first locate the triangle that contains the new point. (Failure here can mean only that the point lies on an existing line, in which case we fuzz the point’s location, as we confessed above, and try again.) We store three new triangles and delete the old one. Then, we locate and fix any illegal edges, doing the recursion by a simple last-in-first-out stack of pending edges to check.

# void Delaunay::insertapoint(Int r) {

Add the point with index r incrementally to the Delaunay triangulation.

Int i,j,k,l,s,tno,ntask,d0,d1,d2;   
Ullong key;   
Int tasks[50], taski[50], taskj[50];   
for $( \ j = 0$ ; j<3; ${ \mathrm { j } } + + { \mathrm { . } }$ ) { tno $=$ whichcontainspt(pts[r],1); if (tno $> = ~ 0 ^ { \cdot }$ ) break;

Stacks (3 vertices) for legalizing edges. Find triangle containing point. Fuzz if it lies on an edge. The desired result: Point is OK.

pts[r].x[0] $+ =$ fuzz $^ *$ delx $^ *$ (hashfn.doub(jran $^ { + + }$ )-0.5); pts[r].x[1] $+ =$ fuzz $^ *$ dely $^ *$ (hashfn.doub(jran ${ . + + }$ )-0.5); if $( { \mathrm { j } } { \mathrm { \Omega } } = = { \mathrm { \Omega } } 3 )$ ) throw("points degenerate even after fuzzing"); ntask $\mathit { \Theta } = \mathit { \Theta } 0$ ; $\begin{array} { r l } { \dot { \bf 1 } } & { { } = } \end{array}$ thelist[tno].p[0]; ${ \dot { \mathrm { ~ \bf ~ j ~ } } } =$ thelist[tno].p[1]; $\mathrm { ~ \bf ~ k ~ } =$ thelist[tno].p[2]; The following line is relevant only when the indicated bit in opt is set. This feature is used by the convex hull application and causes any points already known to be interior to the convex hull to be omitted from the triangulation, saving time (but giving in an incomplete triangulation). if (opt & 2 && i $<$ npts && j $<$ npts && k < npts) return; ${ \tt d } 0 \ =$ storetriangle(r,i,j); Create three triangles and queue them tasks $: + + :$ ntask] $\mathbf { \Phi } = \mathbf { \Phi } _ { \mathbf { T } }$ ; taski[ntask] $=$ i; taskj[ntask] $= \ j$ ; for legal edge tests. ${ \tt d } 1 { \it \Delta \phi } =$ storetriangle(r,j,k); tasks[++ntask] $\mathbf { \Phi } = \mathbf { \Phi } _ { \mathbf { T } }$ ; taski[ntask] $=$ j; taskj[ntask] $\mathit { \Theta } = \mathit { \Theta } \mathbf { k }$ ; $\mathrm { ~ d } 2 \ =$ storetriangle(r,k,i); tasks[++ntask] $= x$ ; taski[ntask] $= \texttt { k }$ ; taskj[ntask] $\mathbf { \Sigma } = \mathbf { \Sigma } _ { \mathrm { ~ i ~ } }$ ; erasetriangle(i,j,k,d0,d1,d2); Erase the old triangle. while (ntask) { Legalize edges recursively. $\mathbf { s } =$ tasks[ntask]; $\mathrm { i } =$ taski[ntask]; j=taskj[ntaskkey $=$ hashfn.int64(j) - hashfn.int64(i); Look up fourth point. if ( ! linehash->get(key,l) ) continue; Case of no triangle on other side. if (incircle(pts[l],pts[j],pts[s],pts[i]) > 0.0){ Needs legalizing? $\mathtt { d 0 } \ =$ storetriangle(s,l,j); Create two new triangles d1 $=$ storetriangle(s,i,l); erasetriangle(s,i,j,d0,d1,-1); and erase old ones. erasetriangle(l,j,i,d0,d1,-1); key $=$ hashfn.int64(i)-hashfn.int64(j); Erase line in both directions. linehash->erase(key); key $\mathit { \Theta } = \mathit { \Theta } 0$ - key; Unsigned, hence binary minus. linehash->erase(key); Two new edges now need checking: tasks $^ { + + }$ ntask] $=$ s; taski[ntask] $= ~ 1$ ; taskj[ntask] $\mathit { \Theta } = \mathit { \Pi } _ { \dot { ] } } \mathit { \Psi } _ { : }$ ; tasks $[ + +$ ntask] $\qquad = \ \mathtt { s }$ ; taski[ntask] $=$ i; taskj[ntask] $\mathbf { \omega } = \mathbf { \varepsilon } _ { 1 } ;$ } }

The only pieces left are the utility functions for finding the triangle that contains a point, and for storing and erasing a triangle. When we “erase” a triangle, we actually only mark it as inactive in the current triangulation, and we set its daughters in the descendancy tree, as already discussed.

# Int Delaunay::whichcontainspt(const Point<2> &p, Int strict) {

Given point p, return index in thelist of the triangle in the triangulation that contains it, or return $^ { - 1 }$ for failure. If strict is nonzero, require strict containment, otherwise allow the point to lie on an edge.

Int i,j, $\mathtt { k } = 0$ ;   
while (thelist[k].stat $< = ~ 0$ ) { Descend in tree until reach a “live” triangle. for ( $\scriptstyle \dot { 1 } = 0$ ; i<3; $\dot { 1 } + +$ ) { Check up to three daughters. if ( $( { \bf j _ { \alpha } } =$ thelist[k].d[i]) < 0) continue; Daughter doesn’t exist. if (strict) { if (thelist[j].contains(p) > 0) break; } else { Yes, descend on this branch. if (thelist[j].contains(p) $> = ~ 0$ ) break; } } if (i == 3) return -1; No daughters contain the point. k = j; Set new mother.   
}   
return k; Normal return.

void Delaunay::erasetriangle(Int a, Int b, Int c, Int d0, Int d1, Int d2) { Erase triangle abc in trihash and inactivate it in thelist after setting its daughters.

Ullong key; Int j; key $=$ hashfn.int64(a) ^ hashfn.int64(b) ^ hashfn.int64(c); if (trihash->get(key,j) $\scriptstyle = = 0 .$ ) throw("nonexistent triangle"); trihash->erase(key); thelist[j].d[0] $=$ d0; thelist[j].d[1] $=$ d1; thelist[j].d[2] $=$ d2; thelist[j].stat $\qquad = \ 0$ ; ntri--

# Int Delaunay::storetriangle(Int a, Int b, Int c) {

Store a triangle with vertices a, b, c in trihash. Store its points in linehash under keys to opposite sides. Add it to thelist, returning its index there.

Ullong key;   
thelist[ntree].setme(a,b,c,&pts[0]);   
key $=$ hashfn.int64(a) ^ hashfn.int64(b) ^ hashfn.int64(c);   
trihash->set(key,ntree);   
key $=$ hashfn.int64(b)-hashfn.int64(c);   
linehash->set(key,a);   
key $=$ hashfn.int64(c)-hashfn.int64(a);   
linehash->set(key,b);   
key $=$ hashfn.int64(a)-hashfn.int64(b);   
linehash->set(key,c);   
if ( $^ { + + }$ ntree $= =$ ntreemax) throw("thelist is sized too small");   
ntri $^ { + + }$ ;   
return (ntree-1);

You might wonder how to get the answer out of our Delaunay structure. We have not provided a function for this, because it so much depends on what you want to do with the answer. The general idea, however, is that you just loop through thelist $[ j ]$ for $0 \leq j <$ nlist. Each element is a Triel. If its value of save is $\leq 0$ , ignore it and go on. If it is 1, then the element represents a triangle in the final Delaunay triangulation. There should be ntri of these elements in all. The element’s array $\mathtt { p } [ ]$ has integers that point to the triangle’s three points in your vector of points. Several routines in the next section mine the Delaunay structure for points, edges, or triangles and can be used as template examples.

Figure 21.6.6 shows sample output for a Delaunay triangulation of 300 points.

# CITED REFERENCES AND FURTHER READING:

Guibas, L.J., Knuth, D.E., and Sharir, M. 1992, “Randomized Incremental Construction of Delaunay and Voronoi Diagrams,” Algorithmica, vol. 7, pp. 381–413.[1]   
Lischinski, D. 1994, “Incremental Delaunay Triangulation,” in Graphics Gems IV, Heckbert, P.S., ed. (Cambridge, MA: Academic Press). [Shows use of linked data structure instead of our use of hash memory.]   
de Berg, M., van Kreveld, M., Overmars, M., and Schwarzkopf, O. 2000, Computational Geometry: Algorithms and Applications, 2nd revised ed. (Berlin: Springer),Chapter 9.[2]   
O’Rourke, J. 1998, Computational Geometry in C, 2nd ed. (Cambridge, UK: Cambridge University Press), $\ S 5 . 3$ .

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/8e5b2ec2c44415465097e416652c5e9b616b043529c3d038127ed18f670da6ae.jpg)  
Figure 21.6.6. Delaunay triangulation of 300 points randomly chosen within a circle, as computed by the routines in this section.

# 21.7 Applications of Delaunay Triangulation

Emerging from the thicket of detail that was needed to implement the Delaunay triangulation, we are now ready to make use of it in several important applications. In this section we assume that you have a vector of points (say, vecp), and that you have invoked the code in -21.6 to construct a Delaunay structure. This usually means writing just the one line of code,

Delaunay mygrid(vecp);

So, what next?

# 21.7.1 Two-Dimensional Interpolation on an Irregular Grid

This is probably the most-asked-for algorithm that was missing from the previous two editions of Numerical Recipes. The basic setup is very simple. You are given a set of $N$ points in the plane. You triangulate that set with a “good” triangulation, that is, one favoring short lines and big angles — in other words, Delaunay. You evaluate a function of interest at each of the points, and store the values in a vector (in the same order as the vector of points, of course).

Now it is easy to interpolate the function at a new point $\mathbf { p }$ that lies within the triangulation, that is, specifically, within the convex hull of your set of points. First, locate which triangle the point falls in. This takes only ${ \cal O } ( \log N )$ operations if you use the whichcontainspt() method of the Delaunay structure. Then, linearly interpolate between the three function values at the three triangle vertices. The linear interpolation is uniquely defined, because (imagining your function plotted in the third dimension above the plane in which $\mathbf { p }$ lies) three points uniquely define a plane in three dimensions .

Constructively, the linear interpolation is easily done using barycentric coordinates as defined in equation (21.3.10), which in turn reduces to using the triangle area formula (equation 21.3.1) three times. Appropriately normalized, each barytropic coordinate value is exactly the weight of its corresponding vertex.

These ideas are implemented in the following function:

# Doub Delaunay::interpolate(const Point<2> &p, const vector<Doub> &fnvals, Doub defaultval) {

Triangular grid interpolation of a function. Given an arbitrary point p and a vector of function values fnvals at the points that were used to construct the Delaunay structure, return the linearly interpolated function value in the triangle in which p lies. If $\mathtt { p }$ lies outside of the triangulation, instead return defaultval.

Int n,i,j,k;   
Doub wgts[3];   
Int ipts[3];   
Doub sum, ans $= ~ 0 . 0$ ;   
$\mathrm { ~ n ~ } =$ whichcontainspt(p); Locate the point in the triangulation.   
if ( $\mathrm { ~  ~ \cdot ~ n ~ } < \mathrm { ~  ~ 0 ~ }$ ) return defaultval; Point outside of convex hull.   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; i<3; $\dot { 1 } + +$ ) ipts[i] $=$ thelist[n].p[i];   
for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ , $\scriptstyle { \dot { \mathsf { J } } } = 1$ , $\mathrm { k } = 2$ ; i<3; $\dot { \bf 1 } + +$ , $\mathrm { j } + +$ ,k++) { Calculate the barycentric coordinates, proif $( { \ j } \ = = \ 3 )$ ) $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; portional to the weights. if $( \textbf { k } = = \textbf { 3 }$ ) $\mathtt { k } = 0$ ; wgts[k] $=$ (pts[ipts[j]].x[0]-pts[ipts[i]].x[0])\*(p.x[1]-pts[ipts[i]].x[1]) (pts[ipts[j]].x[1]-pts[ipts[i]].x[1]) $^ *$ (p.x[0]-pts[ipts[i]].x[0]);   
}   
sum $=$ wgts[0] $^ +$ wgts[1] $^ +$ wgts[2]; Normalization of the weights.   
if (sum $\ c = 0 .$ ) throw("degenerate triangle");   
for ( $\scriptstyle { \dot { 1 } } = 0$ ; i<3; $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \rho } } } .$ ) ans $+ =$ wgts[i]\*fnvals[ipts[i]]/sum; Linear interpolation.   
return ans;

# }

Keep in mind that you should not expect high accuracy from linear interpolation. The interpolated function is piecewise linear, and continuous within the convex hull, but it has discontinuous derivatives in the direction perpendicular to the triangle’s edges. On a triangle edge, it interpolates between the two function values at each end of the edge. You need a lot of triangles to get a reasonable representation of any function with much detailed structure.

# 21.7.2 Voronoi Diagrams

Around 1907, the Ukrainian mathematician Georgy Fedoseevich Voronoi revisited a problem that had been previously discussed by Dirichlet as early as 1850: Given $N$ points, or sites, in the plane, each site p defines a region that is closer to $\mathbf { p }$ than to any of the other $N - 1$ sites. That region is called p’s Voronoi region. What are the properties of the Voronoi regions, and how can we construct them?

If you imagine that everyone in a city shops at the closest supermarket (“as the crow flies”), then the Voronoi regions map out the districts served by each supermarket. If you imagine that fires are simultaneously set at sites in a forest, and that they spread circularly at a fixed speed, then the Voronoi regions are the areas burned by each different fire.

Figure 21.7.1, an example of a Voronoi diagram, shows the Voronoi regions around 40 sites chosen randomly in the plane. Yes, the boundaries of the Voronoi regions are polygons, although possibly open and extending to infinity. It is obvious, in fact, that the boundary of a site $\mathbf { p }$ ’s Voronoi region must consist of line segments each lying on the perpendicular bisector of the line connecting $\mathbf { p }$ to some other site, say $\mathbf { q } _ { i }$ . That is because the perpendicular bisector is the locus of points equidistant from $\mathbf { p }$ and $\mathbf { q } _ { i }$ . So the real questions are, for a given $\mathbf { p }$ , which are the $\mathbf { q } _ { i }$ ’s that contribute boundary segments? and is there a fast way to compute their intersections (the vertices of the Voronoi diagram)?

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/1a8d2f8e3f1a4580cf756f3474a5133ba1dbe9d0286457c92708c21fbe9cf53b.jpg)  
Figure 21.7.1. Voronoi diagram for 40 random sites. Each site has a Voronoi region, the area closer to it than to any other site. The boundaries of the Voronoi regions are straight-line segments that lie on the perpendicular bisectors between pairs of sites.

Remarkably, these questions are completely answered by the Delaunay triangulation of the Voronoi sites. (In fact, many texts start with the Voronoi diagram as fundamental, and then consider Delaunay triangulation as an application. We find it easier to go the other way.)

Some facts are

- Every edge in a site p’s Voronoi region boundary lies on the perpendicular bisector of a Delaunay edge that connects to $\mathbf { p }$ .   
- In fact, every Delaunay edge corresponds to exactly one Voronoi edge, and vice versa.   
- The vertices of the Voronoi diagram are exactly the circumcenters of the Delaunay triangles.   
- The Voronoi diagram and the Delaunay triangulation are dual graphs (but don’t worry if you don’t know what this means)

Figure 21.7.2 shows the key ideas in the proof of the first two facts above. We already know that the boundary is made of some perpendicular bisector segments. We need to show that (i) every one of a point’s Delaunay edges does contribute a segment, and (ii) lines drawn from that point to any other sites don’t contribute any segments.

Part (a) of the figure shows a piece of Delaunay triangulation around site $o$ . The perpendicular bisectors of $O A$ and $O C$ meet at the point $X$ , which is therefore the center of the circle containing $A$ , $o$ , and $C$ . The issue is whether the Delaunay edge $O B$ can be “blocked” by the other two edges. Now, $B$ must lie inside the circumcircle just mentioned; otherwise, the edge $O B$ would have been an illegal edge when the Delaunay triangulation was constructed. But this means that the perpendicular bisector of $O B$ , labeled $U V$ , must “cut off the corner” at $X$ . Thus it does contribute a segment to the boundary.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/a4119f99d01e945daf4e983af5e451cee993aae4abfcba081f091bd8350d1c7e.jpg)  
Figure 21.7.2. Key ideas in the proof that every Delaunay edge contributes exactly one Voronoi edge, lying on its perpendicular bisector. (a) Delaunay requires $B$ to lie inside the circle $A O C$ , hence its bisector must clip the corner inside $X$ . (b) Delaunay requires any other site $P$ to lie outside of the circle $A O B$ , hence its bisector can’t clip the corner inside $X$ .

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/b959753465ddd1f262613fca798a4b2a12cc3c790ae6683aa345a81de399d604.jpg)  
Figure 21.7.3. The circumcenters of the Delaunay triangles around a point $o$ are the vertices of $o$ ’s Voronoi region (shown as shaded), because the perpendicular bisectors of the Delaunay edges meet at these circumcenters. Notice that a Voronoi edge need not actually intersect the Delaunay edge with which it is associated, as $S R$ and $o c$ .

Part (b) of the figure shows a Delaunay triangle $O A B$ whose edges $O A$ and $O B$ are contributing perpendicular bisector segments to the Voronoi boundary around $O$ . Point $P$ is some other site. Can it somehow worm its way in close enough to contribute a segment of its own bisector, between the other two? Evidently not: We know that the circumcircle of any Delaunay triangle contains no other sites. Since $P$ must lie outside the circumcircle, its bisector $U V$ can’t cut off the corner at $X$ .

The fact that the Voronoi vertices are the circumcenters of Delaunay triangles is an immediate consequence of the previous discussion (see Figure 21.7.3). The circumcenters are where the perpendicular bisectors of the edges meet. Since every Delaunay edge contributes a segment, every such circumcenter must be a vertex. Notice, however, that not every Delaunay triangle contains its own circumcenter (as $O C D$ in the figure), so that a segment on the boundary of a Voronoi region need not actually intersect the Delaunay edge with which it is associated (as $R S$ and $O C$ in the figure).

We can count the number of edges and vertices in a Voronoi diagram with $N$ sites ( $\scriptstyle { n }$ of which are on the convex hull) simply by knowing that its dual is the Delaunay triangulation and using equation (21.6.1). The number of Voronoi edges is thus $L$ in that equation, while the number of Voronoi vertices is $T$ . The number of Voronoi regions is by definition $N$ . The unbounded Voronoi regions are exactly those whose points lie on the convex hull of the sites, so there are $n$ of these. It turns out (not immediately obviously) that the average number of edges in one Voronoi region (averaged over all the sites) does not exceed six.

Turning to the implementing code, it is convenient to have a structure for holding Voronoi edges, and also their association with the site that they surround (as an integer pointer to a list of sites).

# struct Voredge {

Structure for an edge in a Voronoi diagram, containing its two endpoints and an integer pointer to the site of which it is a boundary.

Point<2> p[2];   
Int nearpt;   
Voredge() {}   
Voredge(Point<2> pa, Point<2> pb, Int np) : nearpt(np) { p[0] $=$ pa; p[1] $=$ pb;   
}

Now it is straightforward to define a Voronoi structure, as a derived class of the Delaunay structure. The constructor creates a Delaunay triangulation of the sites, and then loops over the sites. For each, it first finds any one triangle with the site as a vertex, and then works its way around the site in a circle, navigating counterclockwise from one triangle to the next by looking up their common edge in the linehash hash memory. Each triangle’s circumcenter is a Voronoi vertex, and a Voronoi edge is stored for each two consecutive circumcenters as the site is circumnavigated.

# struct Voronoi : Delaunay {

Structure for creating a Voronoi diagram, derived from the Delaunay structure. Int nseg; Number of edges in the diagram. VecInt trindx; Will index triangles. vector<Voredge> segs; Will be array of all segments. Voronoi(vector< Point<2> $>$ pvec); Construct Voronoi diagram from array of points.   
};   
Voronoi::Voronoi(vector< Point<2> $>$ pvec) : Delaunay(pvec,1), nseg(0), trindx(npts), segs(6\*npts+12) {   
Constructor for Voronoi diagram of a vector of sites pvec. Bit ”1” sent to the Delaunay con  
structor tells it not to delete linehash. Int i,j,k,p,jfirst; Ullong key; Triel tt; Point<2> cc, ccp; Create a table so that, given a point numfor $\scriptstyle ( { \dot { \mathsf { J } } } = 0$ ; j<ntree; ${ \mathrm { j } } + + { \mathrm { . } }$ ) { ber, we can find one triangle with it as if (thelist[j].stat $\scriptstyle < = 0 .$ ) continue; a vertex. tt $=$ thelist[j]; for $\scriptstyle ( \mathtt { k } = 0$ ; k<3; $\mathrm { k } { + } { + }$ ) trindx[tt.p[k]] = j; } Now loop over the sites. for ( $\scriptstyle \cdot p = 0$ ; p<npts; $\mathbb { p } ^ { + + }$ ) {

tt $=$ thelist[trindx[p]]; if (tt.p[0] $\scriptstyle = = \ p ,$ ) {i = tt.p[1]; ${ \dot { \mathrm { ~  ~ } } } =$ tt.p[2];} Get the vertices into canonelse if (tt.p[1] $\scriptstyle = = \ p$ ) {i $=$ tt.p[2]; ${ \mathrm { ~ j ~ } } =$ tt.p[0];} ical order. else if (tt.p[2] $\mathbf { \Phi } = \mathbf { \Phi } _ { \mathsf { P } }$ ) {i $=$ tt.p[0]; j $=$ tt.p[1];} else throw("triangle should contain $\mathbb { P } ^ { \mathfrak { \ " } } .$ ); jfirst $= \ j$ ; Save starting vertex and its circumcircle. ccp $=$ circumcircle(pts[p],pts[i],pts[j]).center; while (1) { Go around CCW, find circumcenters and store segments. key $=$ hashfn.int64(i) - hashfn.int64(p); if ( ! linehash->get(key,k) ) throw("Delaunay is incomplete"); cc $=$ circumcircle(pts[p],pts[k],pts[i]).center; segs[nseg $+ + ] =$ Voredge(ccp,cc,p); if (k $= =$ jfirst) break; Circumnavigation completed. Normal way out. $\mathsf { c c p } \ = \ \mathsf { c c }$ ; $\dot { \mathsf { J } } { } ^ { = } \dot { \mathsf { \Phi } }$ ; $\dot { \bf \Phi } _ { 1 } = \bf k$ ; } } }

The result of the Voronoi construct is available by looping through the segs array from 0 to nseg-1. Each array element is a Voredge that stores the endpoints, and also the site number with which it is associated. Note that each segment appears twice in the list, with opposite sense, as it is associated in turn with the sites on its two sides.

If you read our confession about dirty tricks in the previous section, you’ll want to keep in mind that the “open” Voronoi polygons are actually closed by segments that lie at a distance of order bigscale times the size of the bounding box of the sites. Those segments are included in segs but appear only once, since there is no site on their other side.

# 21.7.3 Other Applications

Nearest Neighbors, Again. A line segment that connects a point to its nearest neighbor among a set of points will be an edge in the set’s Delaunay triangulation. Informal proof: The nearest neighbor obviously must contribute a boundary to the Voronoi diagram. Formal proof (using a theorem mentioned above): The circle whose diameter connects a point to its nearest neighbor can’t contain any other points (they’d be closer than the nearest neighbor), so that diameter must be a Delaunay edge.

Since we can construct the Delaunay triangulation in ${ \cal O } ( N \log N )$ time, it follows that we can use it to find all nearest neighbors of a set of $N$ points in ${ \cal O } ( N \log N )$ time. The process is as follows: (i) Construct Delaunay. (ii) For each point, circumnavigate it. (We saw how to do this in our implementation of Voronoi, above.) (iii) Pick the shortest of the edges with the point at one end.

Convex Hull. Sometimes you may need to know the convex hull of a set of points in the plane for some other application. Although it might seem wasteful to construct the whole Delaunay triangulation just to get the hull, doing so is not too bad a method. Better efficiency can be achieved by ignoring, during the triangulation, points that are found to be already inside interior triangles. To sort the edges into the order of a CCW polygon, we create a nextpt table of edge destinations as we go, then chain through it once to output the vertices of the convex hull in proper order.

# struct Convexhull : Delaunay {

Structure for constructing the convex hull of a set of points in the plane. After construction, nhull is the number of points in the hull, and hullpoints[0..nhull-1] are integers pointing to points in the vector pvec that are in the hull, in CCW order.

Int nhull; Int \*hullpts; Convexhull(vector< Point<2> $>$ pvec); Construct from a vector of points. };

Convexhull::Convexhull(vector< Point<2> $>$ pvec) : Delaunay(pvec,2), nhull(0) { Constructor for convex hull of a vector of points pvec. Bit ” $2 "$ sent to the Delaunay constructor tells it to ignore interior points when it can, for extra speed.

Int i,j,k,pstart;   
vector<Int> nextpt(npts);   
for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ; j<ntree; ${ \mathrm { j } } + + { \mathrm { , } }$ ) { Triangles with stat $\ c = - 1$ may contain if (thelist[j].stat $\ ! = ~ - 1 )$ continue; hull segments. for $^ { \prime } \mathrm { i } { = } 0 , \mathrm { k } { = } 1$ ; i<3; i++,k++) { Need two valid points to qualify. if $( \mathrm {  ~ k ~ } ) = = \mathrm {  ~ 3 ~ }$ ) $\mathtt { k } = 0$ ; if (thelist[j].p[i] $<$ npts && thelist[j].p[k] $<$ npts) break; if ( $\scriptstyle \dot { 1 } = = 3$ ) continue; Case where failed to qualify. ++nhull; Yes! Put its other end in the lookup table, and save nextpt[(pstart $=$ thelist[j].p[k])] $=$ thelist[j].p[i]; its value in case it’s   
} the last one we find.   
if (nhull $\scriptstyle = = 0 .$ ) throw("no hull segments found");   
hullpts $=$ new Int[nhull]; Now we know how many, can allocate.   
$\scriptstyle { \dot { \mathsf { J } } } = 0$ ; One chain through the lookup table, start   
$\begin{array} { r l } { \dot { \bf 1 } } & { { } = } \end{array}$ hullpts[j $+ + ] \ =$ pstart; ing with pstart, gives the answer.   
while (( $\dot { \bf { \nabla } } \dot { \bf { \sigma } }$ nextpt[i]) $! =$ pstart) hullpts[j++] = i;

Largest Empty Circle Problem. The largest empty circle whose center lies (strictly) inside the convex hull of a set of points in the plane has its center on a Voronoi vertex. So, you can find it by looping through the Voronoi vertices, calculating the radius of the largest circle centered on each one, and taking the maximum of these. Even better, loop through the Delaunay triangles, calculate the circumcenter of each, and pick the one with the largest circumradius (since Delaunay circumcenters are exactly Voronoi vertices). Think of yourself as finding the best location for a fast-food restaurant within the (convex) city limits, one that best avoids all the other fast-food restaurants.

Avoiding Obstacles. If you want to navigate around the plane staying as far as possible from a set of points, your path will be along the edges of a Voronoi diagram. Think of yourself as a fighter pilot avoiding enemy radars.

Minimum Spanning Tree. The minimum spanning tree (sometimes Euclidean minimum spanning tree) is the set of line segments of shortest total length that connect $N$ points (see, e.g., Figure 21.7.4). Think of it as the highway map of the cheapest highway system that lets you visit all $N$ cities. It is topologically a tree (i.e., has no loops) because if it did have a loop, you could save highway money by deleting one of the loop’s segments.

The important theorem is: The minimum spanning tree is a subset of the Delaunay edges. You might think this isn’t very useful, since it doesn’t tell you which subset. Fortunately, there is a fast algorithm, Kruskal’s algorithm, for doing the construction. The basic idea is to sort all the Delaunay edges by length, and then add them one at a time to the growing tree, in order from smallest to largest.

Your tree starts off growing in multiple disconnected components, but when you have added exactly $N - 1$ segments, it will be a single piece, and the answer. There is only one catch: As you add segments, you must not add a segment if both its ends are already in the same component (else it would form a loop). So, you have to maintain an “equivalence class” relation for each vertex, making it equivalent to all other vertices in its connected component. We already know how to do this efficiently, as in $\ S 8 . 6$ ’s routine eclass. In the code below, there is a similar logic of sweeping up pointers to single “mother” representatives. Do this properly, and the method is ${ \cal O } ( N \log N )$ .

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/23f76da6d401494b204ac6cbb46708a57253888c131e319085adab38da8beaf5.jpg)  
Figure 21.7.4. Minimum spanning tree of 1001 points at random locations within a circle. The tree is composed of 1000 segments that connect all the points with the shortest total length and is a subset of the Delaunay triangulation of the same points.

Kruskal’s algorithm is a so-called greedy algorithm, since it just takes the best edge at each step willy nilly. It is rare for a greedy algorithm to yield the true global optimum; but this is the happy case where it does.

# struct Minspantree : Delaunay {

Structure for constructing the minimum spanning tree of a set of points in the plane. After construction, nspan is the number of segments (always $=$ npts1), and minsega[0..nspan-1] and minsegb[0..nspan-1] contain integers pointing to points in the vector pvec that are the two ends of each segment.

Int nspan; VecInt minsega, minsegb; Allocate arrays for the output. Minspantree(vector< Point<2> > pvec); };

inspantree::Minspantree(vector< Point<2> $>$ pvec) :

Delaunay(pvec,0), nspan(npts-1), minsega(nspan), minsegb(nspan) {

Constructor for the minimum spanning tree of a vector of points pvec. The Delaunay constructor gives the triangulation. We need only find the correct subset of edges.

Int i,j,k,jj,kk,m,tmp,nline, $\mathrm { ~ \tt ~ n ~ } = \mathrm { ~ 0 ~ }$ ;   
Triel tt;   
nline $=$ ntri $^ +$ npts -1; Number of edges in the triangulation.   
VecInt sega(nline); Allocate working space for two ends of each edge,   
VecInt segb(nline); edge length, and index on which we will sort.   
VecDoub segd(nline); Also the ”mother” tree for equivalence classes.   
VecInt mo(npts);   
for $\scriptstyle \dot { \mathcal { I } } = 0$ ; j<ntree; $\ j + + )$ ) { Find all edges in the triangulation, store them if (thelist[j].stat $\scriptstyle = = 0$ ) continue; and their lengths. tt $=$ thelist[j]; for ( $\mathbf { i } = 0 , \mathbf { k } = 1$ ; i<3; i++,k++) { if ( $k = = 3$ ) $\mathtt { k } = 0$ ;

if (tt.p[i] $>$ tt.p[k]) continue; Ensure we get each edge only once. if (tt.p[i] $> =$ npts || tt.p[k] $> =$ npts) continue; No edges connectsega[n] $=$ tt.p[i]; ing to fictitious segb[n] $=$ tt.p[k]; points. segd[n] $=$ dist(pts[sega[n]],pts[segb[n]]); $\mathtt { n } + +$ ; } Indexx idx(segd); Sort the edges by creating an index array. for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ; j<npts; ${ \mathrm { j } } + + { \mathrm { . } }$ ) mo[j] = j; Initialize equivalence relation tree. $\texttt { n } = \texttt { - } 1$ ; for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ; i<nspan; i++) { Add exactly nspan segments. for (;;) { Loop for the shortest valid segment n. jj $\mathbf { \dot { \omega } } = \mathbf { \dot { \omega } } \mathbf { j } \mathbf { \omega } = \mathbf { \dot { \omega } }$ idx.el(sega, $+ + \mathtt { n } )$ ; kk $= { \textbf { k } } =$ idx.el(segb,n); while (mo[jj] $\ ! =$ jj) jj $=$ mo[jj]; Track each end to its highest anceswhile (mo[kk] $\ ! =$ kk) kk $=$ mo[kk]; tor. if (jj ! $\downarrow =$ kk) { The segment is valid only if it connects different minsega[i] $=$ j; highest ancestors. minsegb[i] $=$ k; $\qquad { \textbar { 1 1 } } =$ mo[jj] $=$ kk; Now, equate the highest ancestors, and retrace $\mathrm { ~ j ~ j ~ } = \mathrm { ~ j ~ }$ ; our steps pointing all nodes encountered to while (mo[jj] $! = \mathrm { ~ m } )$ ) { that highest node, necessary for speed of the tmp $=$ mo[jj]; algorithm. mo[jj] $= ~ \mathfrak { m }$ ; jj = tmp; } kk $= \texttt { k }$ ; while (mo[kk] $! = \mathrm { ~ m } )$ ) { tmp $=$ mo[kk]; mo[kk] $= ~ \mathfrak { m }$ ; kk $=$ tmp; } break; A segment has been successfully added. } } }

# CITED REFERENCES AND FURTHER READING:

de Berg, M., van Kreveld, M., Overmars, M., and Schwarzkopf, O. 2000, Computational Geometry:Algorithms and Applications, 2nd revised ed. (Berlin:Springer),Chapters 7 and 11.

O’Rourke, J. 1998, Computational Geometry in C, 2nd ed. (Cambridge, UK: Cambridge University Press), Chapter 5.

# 21.8 Quadtrees and Octrees: Storing Geometrical Objects

Different from a KD tree is another kind of box tree, usually called a quadtree in two dimensions or a octree in three dimensions. Yes, we know that it ought to be spelled “octtree,” not “octree,” but the latter usage has become standard. We’ll refer to quadtrees and octrees generically as “QO trees” and thus avoid linguistic controversy.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/404be769d57b6f334ccf96ae94d5a1d7ea58316909bc6a5f18b12ff2356c9eb4.jpg)  
Figure 21.8.1. In a quadtree, the initial square 1 is first subdivided into squares 2, 3, 4, and 5. At the next level of subdivision, 2 is subdivided into 6, 7, 8, 9; 3 into 10, 11, 12, 13; and so forth.

QO trees start with a finite-sized box, usually square or cubical, rather than the near-infinite box used in the KD tree. A QO tree then subdivides each box not in one dimension at a time (as a KD tree) but rather in all dimensions. Thus, a square is subdivided into four daughter squares, a cube into eight daughter cubes — quite a brood. The coordinates of the subdivisions are taken to exactly bisect the mother box in each dimension, so all the boxes at one level of the tree are congruent, differing from the original box by a fixed power-of-two factor. Figure 21.8.1 illustrates this in the case of two dimensions.

QO trees thus provide a kind of addressing scheme for two- or three-dimensional space. Accordingly, they can be used to store and retrieve finite-sized geometrical objects that fit into the boxes of the tree at one or another level, and to test for intersections of such objects, for nearness relationships, and so on. The general idea (although there can be variations on this) is to store each object in the smallest box that completely contains it — or, in the case of a zero-sized object like a point, in the appropriate box at the deepest level of tree that we care to implement. Then, when doing a collision or nearness test, we traverse only those parts of the tree that are relevant, much as we did in the applications of KD trees.

Although we will illustrate only the most elementary of applications, QO trees are often at the heart of more complicated algorithms, for example [1-3],

- Hidden polygon removal in the visual plane (which projected polygons intersect a given pixel in the visual field?)   
- Fast gravitational or Coulomb N-body calculations (store fictitious objects on various scales that sweep up the multipole moments of the collections of point masses that they contain) [4,5,6]   
- Mesh generation (choose a local mesh scale to match the scale in the QO tree at which obstacles or boundaries are stored; the concept of a balanced QO tree is often used)   
- Image compression (store slowly varying parts of the image as objects high in the tree, and prune unnecessary daughters).

A main weakness of QO trees follows just from their geometrical regularity. If a finite-sized object being stored in a QO tree falls on the boundary between two boxes of about its size, then it can’t be stored in either of them. Instead, it gets stored in the larger — sometimes very much larger — box that first completely contains it. If $N$ “small” objects are stored, then the number that fall on boundaries of the highest-level boxes scales in two dimensions as $N ^ { 1 / 2 }$ , or in three dimensions as $N ^ { \bar { 2 } / 3 }$ . These objects will thus end up stored in just a few boxes at the top of the tree, and they will participate in almost all operations that check for collisions or nearness. Thus, QO trees can usually effect a time savings that turns a naive algorithm scaling as $N$ into one that scales as $N ^ { 1 / 2 }$ (in the two-dimensional case); but only rarely, or with specialized methods, can they get to that Nirvana of $\log N$ or constant scaling. Still, the square- (or, in three dimensions, cube-) root of a large number can be a large factor, and well worth saving in time. So QO trees are good to know about.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/216a4fa563a2e14bd0d1ddc482f4ba75a07e1720450a8bd63fcb674692674908.jpg)  
Figure 21.8.2. Quadtree shown in tree form. Because of its regularity, a quadtree’s relationships can be described numerically. For example, the mother of box $_ n$ is the integer part of $n / 4$ . The left daughter of box $_ { n }$ is $4 n - 2$ .

That same geometrical regularity of QO trees allows them to be implemented, at least optionally, as an efficient hash structure where most boxes in the tree, if they are empty, require no storage space. We will give such an implementation here, both for its intrinsic advantages and because it is fairly concise to code, using the Hash and Mhash classes from $\ S 7 . 6$ .

The key observations follow from Figure 21.8.2, which shows a QO tree laid out in tree form. The boxes are numbered as in Figure 21.8.1, starting with box 1 at the root of the tree. With this numbering scheme, there exist simple numerical relations between the mother and daughter boxes. This enables one to navigate the tree — up, down, and sideways — without the use of any stored pointers. In particular, if $k \geq 1$ is a box’s number, the following relationships hold in $D$ (for us, two or three) dimensions:

$$
\begin{array} { c } { { \mathrm { m o t h e r } \left( k \right) = \lfloor ( k + 2 ^ { D } - 2 ) / 2 ^ { D } \rfloor } } \\ { { \mathrm { l e f t m o s t d a u g h t e r } \left( k \right) = 2 ^ { D } k - 2 ^ { D } + 2 } } \\ { { \mathrm { r i g h t m o s t d a u g h t e r } \left( k \right) = 2 ^ { D } k + 1 } } \\ { { \mathrm { t o t a l b o x e s ~ t h r o u g h ~ l e v e l ~ p = \lfloor ( 2 ^ { D } ) ^ { p } - 1 \rfloor / ( 2 ^ { D } - 1 ) } } } \end{array}
$$

Note that the integer divide by $2 ^ { D }$ implied by the $\lfloor \ \rfloor$ notation can be implemented simply as a right shift by $D$ bits. You should check the formulas in (21.8.1) against Figure 21.8.2 to be sure that you understand how they work. The “levels” of the tree are numbered starting with $p = 1$ for (only) box 1. Notice that the mother of box 1 computes to 0, indicating that it has no mother; this is convenient for testing when to exit loops over ancestry.

Before we get to implementation details for the implementing class Qotree, we need to discuss the prerequisites for a class of geometrical objects to be stored in the tree. Qotree will be templated by a type parameter elT representing those objects. To store an object myel of type elT, you must be sure to provide a method myel.isinbox() whose argument is a Box, and which returns 1 if myel is in the Box, or 0 otherwise. Similarly, to erase an object, you need to provide an $= =$ operator, to decide (by comparison) which is the object to be erased. Those two methods are all that Qotree needs for itself. However, many applications of Qotree (including some that we illustrate later in this section) need either or both of the methods myel.contains() and myel.collides(), the first returning whether myel contains a given point, the second returning whether myel collides with another element of type elT.

Here is a simple example of a class, representing a circle (when DIM is 2) or sphere (when DIM is 3), that has these methods and can thus be stored and processed with a Qotree:

template<Int DIM> struct Sphcirc {   
Circle $\mathrm { \ ( D I M } { = } 2 )$ ) or sphere $\mathtt { D I M } = 3$ ) object, with methods suitable for use with Qotree. Point<DIM> center; Doub radius; Sphcirc() {} Default constructor is needed to make arrays. Sphcirc(const Point<DIM> &mycenter, Doub myradius) Construct by explicit center : center(mycenter), radius(myradius) {} and radius. bool operator $= =$ (const Sphcirc &s) const { Test if identical. return (radius $= =$ s.radius && center $= =$ s.center); } Int isinbox(const Box<DIM> &box) { Is the circle/sphere inside a box? for (Int i=0; i<DIM; $\dot { \bf 1 } + +$ ) { if ((center.x[i] - radius $<$ box.lo.x[i]) || (center.x[i] $^ +$ radius $>$ box.hi.x[i])) return 0; return 1; } Int contains(const Point<DIM> &point) { Is a given point inside the circle/sphere? if (dist(point,center) $>$ radius) return 0; else return 1; } Int collides(const Sphcirc<DIM> &circ) { Does it collide with another circle/sphere? if (dist(circ.center,center) $>$ circ.radius+radius) return 0; else return 1; }   
};

# 21.8.1 A Hashed QO Tree Implementation

We will implement the QO tree using two hash memories. First, there is an Mhash multimap memory (called elhash) whose keys are box numbers and whose stored elements are the geometrical objects that may be stored in the QO tree, with possibly multiple objects in a single box. Second, there is a single-valued Hash memory (called pophash) that associates an integer with every box that either (i) contains one or more elements (is “populated”), or (ii) is an ancestor to a box that is populated. In that integer, bit 0 (least significant bit) is used to indicate whether the box is populated, while bits $1 \ldots 2 ^ { D }$ (that is, 1 : : : 4 or 1 : : : 8) are used to indicate which (if any) daughters are themselves either populated or are an ancestor to a populated box. In other words, pophash, combined with the relationships in equation (21.8.1), substitutes for the entire structure of doubly linked pointers that might more conventionally implement the tree.

The maximum number of levels $p _ { \mathrm { m a x } }$ that we can represent is limited only by the largest value that can be represented by the integer type that stores box numbers $k$ . Using 32-bit signed integers, 16 levels are possible in two dimensions, since $( 4 ^ { 1 6 } - 1 ) / 3 < \breve { 2 } ^ { 3 1 } - 1$ (cf. equation 21.8.1). In three dimensions, 11 levels can be represented, since $( 8 ^ { 1 1 } - 1 ) / 7 <$ $2 ^ { 3 1 } - 1$ . Often there is no need for this much resolution $( \sim \mathsf { 1 0 } ^ { 9 }$ boxes), so we will provide for setting a smaller value of $p _ { \mathrm { m a x } }$ , a good idea since the time to traverse one branch of the tree from root to leaf (a frequently occurring “atom” in other procedures) scales linearly with $p _ { \mathrm { m a x } }$ .

template<class elT, Int DIM> struct Qotree {   
Quadtree $\left( \mathtt { D I M } = 2 \right)$ ) or octree $\scriptstyle \left( \mathtt { D I M } = 3 \right)$ ) object to store geometrical objects of type elT. static const Int PMAX $=$ 32/DIM; Roughly how many levels fit in 32 bits. static const Int $\mathsf { Q } \mathsf { O } \ = \ \mathsf { ( 1 } \ \ll \ \mathsf { D } \mathtt { I } \mathsf { M } )$ ; I.e., 4 for quad-, 8 for oct-. static const Int $\mathbb { Q } \mathbb { L } \ = \ \left( \mathbb { Q } \mathbb { O } \ - \ 2 \right)$ ; Offset constant to leftmost daughter. Int maxd; Doub blo[DIM]; Doub bscale[DIM]; Mhash<Int,elT,Hashfn1> elhash; Contains stored elements hashed by box #. Hash<Int,Int,Hashfn1> pophash; Contains node population info. Qotree(Int nh, Int nv, Int maxdep); The constructor. See below. void setouterbox(Point<DIM> lo, Point<DIM> hi); Set scale and position. Box<DIM> qobox(Int k); Return the box whose number is k. Int qowhichbox(elT tobj); Return smallest box containing tobj. Int qostore(elT tobj); Store an elT object in the Qotree. Int qoerase(elT tobj); Erase an elT object in the Qotree. Int qoget(Int k, elT \*list, Int nmax); Retrieve all objects in box k. Int qodump(Int \*k, elT \*list, Int nmax); Retrieve all objects. Int qocontainspt(Point<DIM> pt, elT \*list, Int nmax); See below. Int qocollides(elT qt, elT \*list, Int nmax); See below.   
};

template<class elT, Int DIM> Qotree<elT,DIM>::Qotree(Int nh, Int nv, Int maxdep) : elhash(nh, nv), maxd(maxdep), pophash(maxd\*nh, maxd\*nv)

Constructor for a quad- $\mathtt { ( D I M = 2 ) }$ ) or oc- $\mathtt { ( D I M = 3 ) }$ ) tree that can store a max of nv elements of type elT, using hash tables of length nh (typically $\approx \mathtt { n v }$ ). maxdep is the number of levels to be represented.

if (maxd $>$ PMAX) throw("maxdep too large in Qotree"); setouterbox(Point<DIM>(0.0,0.0,0.0),Point<DIM>(1.0,1.0,1.0)); Default scale. }

template<class elT, Int DIM>   
void Qotree<elT,DIM>::setouterbox(Point<DIM> lo, Point<DIM> hi) {   
Sets the scale of Qotree to an outer box defined by points lo and hi. Must be called before any elements are stored in the tree.   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<DIM; $\mathrm { j } { + + } )$ { blo[j] $=$ lo.x[j]; bscale[j] $=$ hi.x[j] - lo.x[j];   
}

You will normally call setouterbox() immediately after invoking the qotree constructor to create a QO tree. Otherwise, you get the default box with a corner at the origin and unit size in each dimension.

Right away, we need two utility routines. The first takes a box’s number (e.g., as in Figure 21.8.1) and returns the actual box (as a Box<DIM>). The second takes an object of the type to be stored in the tree (elT) and returns the number of the smallest box that contains it. It does this by starting at the top of the tree, trying each possible daughter, and moving deeper into the tree only when a containment is found.

template<class elT, Int DIM>   
Box<DIM> Qotree<elT,DIM>::qobox(Int k) {   
Returns the box indexed by k. Int j, kb; Point<DIM> plo, phi;   
Doub offset[DIM];   
Doub del $= ~ 1 , 0$ ;   
for $( \ j = 0$ ; j<DIM; $\mathrm { j } { + } { + } )$ offset[j] $= ~ 0 . 0$ ;   
while (k > 1) { Up through ancestors until get to root. kb $=$ (k + QL) % QO; Which daughter is $\mathtt { k 7 }$ Add its offset. for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<DIM; ${ \dot { \mathsf { J } } } ^ { + + }$ ) { if (kb & $( 1 < < \mathrm { ~ j ~ } )$ offset[j] $+ =$ del; $\mathrm { \bf ~ k ~ } = \mathrm { \bf ~ \left( ~ k ~ + ~ \frac { } { } ~ \frac { } { } ~ \right) ~ } > > \mathrm { \bf ~ D I M } ;$ Replace k by its mother, del $* = ~ 2 , 0$ ; where offsets will be twice as big.   
}   
for $( \ j = 0$ ; j<DIM; $\mathrm { j } { + + } )$ { At the end, scale the offsets by the final del to plo.x[j] $=$ blo[j] $^ +$ bscale[j]\*offset[j]/del; make them metrically correct. phi.x[j] $=$ blo[j] $^ +$ bscale[j] $^ *$ (offset[j] $^ { + 1 }$ .0)/del;   
}   
return Box<DIM>(plo,phi); Construct the box and return it.

# template<class elT, Int DIM>

Int Qotree<elT,DIM>::qowhichbox(elT tobj) {

Return the box number of the smallest box that can contain an element tobj, without regard to whether tobj is already stored in the tree.

Int p,k,kl,kr,ks $^ { = 1 }$ ; Answer is box 1 unless a smaller box found.   
for ${ \tt ( p = } 2$ ; $\mathrm { p } < =$ maxd; $\mathtt { p } ^ { + + }$ ) { Go down through the levels. $\mathrm { k 1 ~ = ~ 0 0 ~ ^ { \circ } ~ ^ { \circ } ~ ^ { \mathrm { k s } ~ - ~ } ~ \mathsf { Q L } }$ ; Leftmost daughter. $\mathbf { k } \mathbf { r } \ = \ \mathbf { k } \mathbf { l } + \mathbf { 0 } 0 - \mathbf { 1 } ;$ ; Rightmost daughter. for (k=kl; $\mathtt { k } < = \mathtt { k } \mathtt { r }$ ; $\mathtt { k } { + } { + }$ ) { Do any daughters contain tobj? if (tobj.isinbox(qobox(k))) $\left\{ \begin{array} { r l } \end{array} \right. \mathrm { k s } = \mathrm { ~ k ~ } _ { 1 }$ ; break; } } if $( \textbf { k } > \textbf { k r } )$ ) break; No. Therefore, discontinue descent here.   
}   
return ks;

Now we are ready to store elements into the tree, or to erase elements previously stored. With qowhichbox(), above, and the methods that belong to the Mhash, it is trivial to do the actual store or erase. Trickier to code is to create or erase the trail of “breadcrumbs” in pophash that connect the box to its ancestors. When we erase, we must be sure not to cut off the trail to any remaining elements in the same box, or to elements in descendant boxes.

template<class elT, Int DIM>   
Int Qotree<elT,DIM>::qostore(elT tobj){   
Store the element tobj in the Qotree, and return the box number into which it was stored. Int k,ks,kks,km; $\mathbf { k } \mathbf { s } ~ = ~ \mathbf { k } \mathbf { k } \mathbf { s } ~ = ~ \mathbf { \Omega }$ qowhichbox(tobj); elhash.store(ks, tobj); Store the element in elhash pophash[ks] $\mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf { \Sigma } \mathbf \Sigma \mathbf { \Sigma } \mathbf { \Sigma } \mathbf \Sigma \Sigma \mathbf { } \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \mathbf \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \Sigma \ S \Sigma \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S \ S $ ; and mark its box as populated. while (ks > 1){ Now leave trail of breadcrumbs to the root mother. km $=$ (ks $^ +$ QL) >> DIM; Mother of ks. $\mathrm { ~ \bf ~ k ~ } = \mathrm { ~ \bf ~ k s ~ } - { \bf ~ \tau }$ (QO\*km - QL); Which daughter of km is ks. $\mathtt { k s } ~ = ~ \mathtt { k m }$ ; Now set the daughter bit in the mother. pophash[ks] $| = \mathbf { \Gamma } ( 1 \ < < \ \mathbf { \Gamma } ( \mathbf { k } { + } 1 ) ) \ \rangle$ ; } return kks;   
} template<class elT, Int DIM>   
Int Qotree<elT,DIM>::qoerase(elT tobj) {   
Erase the element tobj, returning the box number into which it was stored or 0 if the element was not found in the Qotree. Note logic very similar to qostore. Int k,ks,kks,km;   
Int \*ppop;   
ks $=$ kks $=$ qowhichbox(tobj); Find the box.   
if (elhash.erase(ks, tobj) $\ c = 0 .$ ) return 0; It ain’t there! if (elhash.count(ks)) return kks; Sisters still in same box, so we are done.   
ppop $=$ &pophash[ks];   
\*ppop &= \~((Uint)1);   
while (ks > 1) { if (\*ppop) break; pophash.erase(ks); km $=$ (ks $^ +$ QL) $> >$ DIM; $\mathrm { ~ \bf ~ k ~ } =$ ks - (QO\*km - QL); k $\mathrm { ~ s ~ } = \mathrm { ~ k m ~ }$ ; ppop $=$ &pophash[ks]; \*ppop $\& =$ \~((Uint)(1 << (k+1)));   
return kks; Must now erase any unneeded breadcrumbs.   
Unmark the pop bit.   
Up through the ancestors...   
Box is populated or has daughters, so done.   
Erase unneeded (zero) pophash entry.   
Mother of ks.   
Which daughter of km is ks.

Unset the daughter bit in the mother.

Finally, we need methods to retrieve elements previously stored, either those in a given box (by number), or else all the elements in the tree. In the former case, the Mhash does all the work. In the latter case, however, we must provide the machinery for a recursive search of the tree, since at any stage we may encounter a box with multiple populated daughters. Notice that the calling routine is responsible for supplying storage (as an array list[]) for the result and declaring the maximum number nmax of elements that it is prepared to accept.

# template<class elT, Int DIM>

Int Qotree<elT,DIM>::qoget(Int k, elT \*list, Int nmax)

Retrieve all (or up to nmax if it is smaller) elements that are stored in box k of the Qotree. The elements are copied into list[0..nlist-1] and the value nlist ( $\leq$ nmax) is returned.

Int ks, pop, nlist; ks $\mathit { \Theta } = \mathit { \Theta } \mathbf { k }$ ; nlist $\qquad = \ 0$ ; pophash.get(ks,pop); if ((pop & 1) && elhash.getinit(ks)) { while (nlist $<$ nmax && elhash.getnext(list[nlist])) {nlist++;} return nlist; }

#

# template<class elT, Int DIM>

Int Qotree<elT,DIM>::qodump(Int \*klist, elT \*list, Int nmax) {

Retrieve all (or up to nmax if it is smaller) elements that are stored anywhere in the Qotree, along with their corresponding box numbers. The elements are copied into list[0..nlist-1] and the value nlist ( $\leq$ nmax) is returned. The box numbers are copied into klist[0..nlist-1].

Int nlist, ntask, ks, pop, k;   
Int tasklist[200]; Stack of pending box numbers as we recur  
nlist $\qquad = \ 0$ ; sively traverse the tree.   
ntask $\ c = ~ 1$ ;   
tasklist[1] $\ l = \ 1$ ;   
while (ntask) { As long as tasks remain... ks $=$ tasklist[ntask--]; if (pophash.get(ks,pop) $\ c = 0 .$ ) continue; Box empty and no daughters. if ((pop & 1) && elhash.getinit(ks)) { The box is populated, so we output while (nlist $<$ nmax && elhash.getnext(list[nlist])) { its contents. klist[nlist] $=$ ks; nlist++; } } if (nlist $= =$ nmax) break; No more room for output! $\mathrm { ~ \bf ~ k ~ } =$ QO\*ks - QL; Leftmost daughter. while (pop $> > = ~ 1$ ) { Loop over the daughter bits in pop. if (pop & 1) tasklist[++ntask] $= \mathrm { ~ k ~ } ;$ Daughter exists. Add to task list. k++; Next daughter. }   
}   
return nlist;

The additional functions declared in Qotree pertain to applications, as we now discuss.

# 21.8.2 QO Tree Elementary Applications

Two important building blocks for applications of QO trees are, first, a routine that returns a list of all stored elT elements that intersect (i.e., contain) a specified point; and, second, a routine that returns a similar list of all stored elT elements that intersect (i.e., collide with) a specified elT element.

An element that intersects a point will evidently be stored in a box that is an ancestor to the box that the point is in, or else in the same box as the point. It takes just one pass down through the levels of the tree to find all such elements.

template<class elT, Int DIM> Int Qotree<elT,DIM>::qocontainspt(Point<DIM>pt, elT \*list, Int nmax) { Retrieve all (or up to nmax if it is smaller) elements in Qotree that contain the point pt. The elements are copied into list[0..nlist-1] and the value nlist $\leq$ nmax) is returned.

Int j,k,ks,pop,nlist;   
Doub bblo[DIM], bbscale[DIM];   
for $\scriptstyle \dot { \ j } = 0$ ; j<DIM; $\mathrm { j } { + } { + } )$ { bblo[j] $=$ blo[j]; bbscale[j] $=$ bscale[j]; }   
nlist $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
ks $= ~ 1$ ; Start at the top of the tree.   
while (pophash.get(ks,pop)) { Descend as long as something is there. if (pop & 1) { The box is populated, so we check its conelhash.getinit(ks); tained elements, while (nlist $<$ nmax && elhash.getnext(list[nlist])) if (list[nlist].contains(pt)) {nlist++;} returning any that contain } pt. } if ((pop $> > = \ 1 ) = = \ 0 \ ,$ ) break; The box has no daughters, so we are done. for $( \mathrm { k } = 0$ , $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<DIM; ${ \mathrm { j } } + + )$ { Compute k, the single daughter containing bbscale[j] $* = ~ 0 , 5$ ; pt. if (pt.x[j] $>$ bblo[j] $^ +$ bbscale[j]) { k $+ = \ ( \mathrm {  ~ 1 ~ } \ll \mathrm {  ~ j ~ } )$ ; bblo[j] $+ =$ bbscale[j]; } } $\mathrm { i f } ( ( \mathrm { p o p } > > \mathrm { k } ) \& \ 1 ) = = 0 )$ ) break; No such daughter exists in the tree. $\mathrm { k s ~ = ~ 0 0 ~ * ~ k s ~ - ~ 0 L ~ + ~ k } ;$ ; Daughter exists and is the next node to check.   
1   
return nlist;

When an element $A$ intersects another element $B$ , either $A$ and $B$ are in the same box, or else $A$ is in an ancestor box to $B$ , or else $B$ is in an ancestor box to $A$ . Equivalently, for a fixed $A$ , we can find all intersecting $B$ ’s by searching $A$ ’s box, its ancestors, and its descendants. The latter search requires a task list stack, as we have seen before (e.g., in qodump).

# qotree.h

# template<class elT, Int DIM>

Int Qotree<elT,DIM>::qocollides(elT qt, elT \*list, Int nmax) {

Retrieve all (or up to nmax if it is smaller) elements in Qotree that collide with an element qt (which needn’t be in the tree itself). The elements are copied into list[0..nlist-1] and the value nlist $\mathbf { \beta } ( \leq \mathtt { n m a x } )$ is returned.

Int k,ks,kks,pop,nlist,ntask;   
Int tasklist[200];   
nlist $\mathit { \Theta } = \mathit { \Theta } 0$ ;   
k $\begin{array} { r } { \mathrm { ~  ~ \tau ~ } _ { \mathrm { S } } ~ = ~ \mathrm { k s } ~ = ~ } \end{array}$ qowhichbox(qt);   
ntask $\qquad = \ 0$ ;   
while (ks $> 0$ ) {   
Stack of pending box numbers.   
kks saves the starting box.   
Put the starting box and all its ancestors on the task list.

tasklist $[ + +$ ntask] $=$ ks; ks = (ks + QL) >> DIM; Move to mother. } while (ntask) { ks $=$ tasklist[ntask--]; if (pophash.get(ks,pop) $\scriptstyle = = 0$ ) continue; Box empty and no daughters. if (pop & 1) { The box is populated, so we check its contained elhash.getinit(ks); elements, while (nlist $<$ nmax && elhash.getnext(list[nlist])) { if (list[nlist].collides(qt)) {nlist++;} returning any that col-} lide with qt. } if (ks $> =$ kks) { Recurse only for descendants, not ancestors! $\mathrm { ~ \bf ~ k ~ } =$ QO\*ks - QL; Leftmost daughter. while (pop $> > = ~ 1$ ) { if (pop & 1) Daughter exists. Add to task list. tasklist[ $^ { + + }$ ntask] k; k++; Next daughter. } } 1 return nlist;

As an example of a simple application of a QO tree, let’s replicate the functionality of KDtree::locatenear (-21.2) with a routine that finds all stored points within a specified radius $r$ of a test point. Using the class Sphcirc, points are represented as circles/spheres of zero radius, the test point as a circle/sphere of radius $r$ , and we use qocollides to find the collisions.

We implement this application as a structure, Nearpoints, whose constructor creates the QO tree out of a vector of points, and whose member function locatenear can then be called to find all stored points within any specified radius of any specified point.

# template <int DIM> struct Nearpoints {

Object for constructing a QO tree containing a set of points, and for repeatedly querying which stored points are within a specified radius of a specified new point.

Int npts;   
Qotree<Sphcirc<DIM>,DIM> thetree;   
Sphcirc<DIM> \*sphlist;   
Nearpoints(const vector< Point<DIM> $>$ &pvec) : npts(pvec.size()), thetree(npts,npts,32/DIM) Constructor. Creates the QO tree from a vector of points pvec. Int j,k; sphlist $=$ new Sphcirc<DIM>[npts]; Point<DIM> lo $=$ pvec[0], hi $=$ pvec[0]; Find bounding box for the points. for (j=1; j<npts; j++) for ( $\scriptstyle 1 = 0$ ; k<DIM; $\mathrm { k } { + } { + } \mathrm { \Gamma }$ ) { if (pvec[j].x[k] $<$ lo.x[k]) lo.x[k] $=$ pvec[j].x[k]; if (pvec[j].x[k] $>$ hi.x[k]) hi.x[k] $=$ pvec[j].x[k]; } for $( \mathrm { k } = 0$ ; k<DIM; $\mathtt { k } { + } { + }$ ) { Expand it by $10 \%$ so that all points lo.x[k] $- =$ 0.1\*(hi.x[k]-lo.x[k]); are well interior. hi.x[k] $+ =$ 0.1\*(hi.x[k]-lo.x[k]); } thetree.setouterbox(lo,hi); Set the tree’s outer box and store all the points. for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<npts; ${ \dot { \mathsf { J } } } ^ { + + }$ ) thetree.qostore(Sphcirc<DIM>(pvec[j],0.0));   
}   
\~Nearpoints() { delete [] sphlist; }   
Int locatenear(Point<DIM> pt, Doub r, Point<DIM> \*list, Int nmax) {

Once the tree is constructed, this function can be called repeatedly with varying points pt and radii $\mathbf { r }$ . It returns n, the number of stored points within radius r of pt (but no larger than nmax), and copies those points into list[0..n-1].

Int j,n; $\mathrm { ~ n ~ } =$ thetree.qocollides(Sphcirc<DIM>(pt,r),sphlist,nmax); for ( $\scriptstyle { \dot { \mathbf { J } } } = 0$ ; $\scriptstyle { \dot { \mathsf { J } } } < { \mathsf { n } }$ ; ${ \mathrm { j } } + +$ ) list[j] $=$ sphlist[j].center; return n; } };

In practice, the routine above is rather slower than KDtree::locatenear for this application, because there is a lot of overhead involved in copying Point and Sphcirc elements around, and in computing Boxes as we drill down the tree. By contrast, KDtree is lean and mean, since it only stores points and, in our implementation, copies them internally to a fast store of coordinates.

Unlike the KD tree, however, the technique illustrated here can be generalized to much more complicated situations. For example, instead of being simple points, the stored objects could be broadcast reception areas for FM radio stations on a given frequency, and we might want to know where collisions occur with proposed new stations. The collides() function between two broadcast areas might involve a lengthy calculation taking into account their powers, the surrounding detailed topography, and so on. In such a case, the overhead of the QO tree might well be negligible as we seek to minimize the number of calls to collides().

As a second example of a simple application, consider a square Petri dish on which spores land, in random positions, one at a time. Each such spore quickly grows into a circular colony that just touches the nearest existing colony (or the edge of the dish), and then stops. (Don’t ask us why. This is only an example.) What does the dish look like after $N$ spores have landed?

Rather than give the code in detail, a simple description should suffice: The objects stored in the QO tree are circles. Looping over the number of spores, we pick a random location for each in turn. If the QO tree method qocontainspt() indicates that the location lies within an already-stored colony, go on to the next spore. Otherwise, start with a small trial radius and increase it (by doubling, e.g.) until qotreecollides() first indicates collisions. Now adjust the trial radius to be the minimum of distances to the colliding elements, add that colony to the tree, and go on to the next spore.

Figure 21.8.3 shows an example of the resulting configuration, after 1000 colonies have grown. (Another 3592 spores landed inside existing colonies and died immediately.)

# CITED REFERENCES AND FURTHER READING:

de Berg, M., van Kreveld, M., Overmars, M., and Schwarzkopf, O. 2000, Computational Geometry: Algorithms and Applications, 2nd revised ed. (Berlin: Springer), Chapter 14.[1]   
Samet, H. 1990, The Design and Analysis of Spatial Data Structures (Reading, MA: Addison-Wesley).[2]   
Samet, H. 1990, Applications of Spatial Data Structures: Computer Graphics, Image Processing, and GIS (Reading, MA: Addison-Wesley).[3]   
Pfalzner, S. and Gibbon, P. 1996, Many-Body Tree Methods in Physics (Cambridge, UK: Cambridge University Press).[4]   
Greengard, L., and Wandzura, S., eds. 1998, “Fast Multipole Methods,” special issue of IEEE Computational Science and Engineering,vol.5, no.3 (July-September),pp.16-56.[5]   
Gumerov, N.A., and Duraiswami, R. 2004, Fast Multipole Methods for the Helmholtz Equation in Three Dimensions (Amsterdam: Elsevier).[6]

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/16cdb71e80be9eafc4a7cf67e388f1f727454d5c0f09c1f4aa465beee28751e8.jpg)  
Figure 21.8.3. Spores land randomly on a square (!) Petri dish, and grow to colonies that barely touch the nearest pre-existing colony, or the edge of the dish. A QO tree can be used to keep track of collisions. Here, 1000 colonies have grown to their maximum size.

# Less-Numerical Algorithms

# 22.0 Introduction

You can stop reading now. You are done with Numerical Recipes, as such. This final chapter is an idiosyncratic set of “less-numerical recipes” that, for one reason or another, we have decided to include between the covers of an otherwise morenumerically oriented book. Authors of computer science texts, we’ve noticed, like to throw in a token numerical subject (usually quite a dull one — quadrature, for example). We find that we are not free of the reverse tendency.

Our selection of material is not completely arbitrary. In $\ S 9 . 0$ we promised to provide a simple plotting routine. Another promised topic, Gray codes, was already used in the construction of quasi-random sequences $( \ S 7 . 8 )$ and here needs only some additional explication. Two other topics, on diagnosing a computer’s floating-point parameters, and on arbitrary precision arithmetic, give additional insight into the machinery behind the casual assumption that computers are useful for doing things with real numbers (as opposed to integers or characters). The latter of these topics also shows a very different use for Chapter 12’s fast Fourier transform.

The three other topics (checksums, Huffman, and arithmetic coding) involve different aspects of data coding, compression, and validation. The material here is intended to be somewhat less abstract, and somewhat more practical, than the discussion of coding in $\ S 1 6 . 2$ , where coding was used to illustrate statistical aspects of state estimation. If you handle a large amount of data (numerical data, even), then a passing familiarity with these subjects might at some point come in handy. In $\ S 1 3 . 6$ , for example, we already encountered a good use for Huffman coding.

But again, you don’t have to read this chapter. (And you should learn about quadrature from Chapters 4 and 17, not from a computer science textbook!)

# 22.1 Plotting Simple Graphs

Yes, we all have our favorite plotting or graphics packages, and our favorite ways of generating plots from within $\mathrm { C } { + } { + }$ programs. But wait: Are your $\mathrm { C } { + + }$ programs generating long text files of numbers, just so that you can read those numbers into a separate plotting or graphics package? If so, you might benefit from this section.

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0017_pages_1121-1190/auto/images/004b61c6d541197b4e91fdd6f7579a33cd110c20ae664f4188347b9f432dfe15.jpg)  
Figure 22.1.1. Simple plot generated using the objects PSpage and PSplot, which are wrappers for generating PostScript.

We find it useful to have on hand a couple of short $\mathrm { C } { + } { + }$ objects, implemented in simple source code, that generate simple plots. (By “simple,” we mean “like most of the figures in this book.”) We are then able to make plots from anywhere in our programs, whether as an aid in debugging or as final output. Equally important, we can make changes to the plotting source code at will, adding features or modifying the look of the plot.

One way of accomplishing these goals is by means of a $\mathrm { C } { + + }$ “wrapper” that does no more, nor less, than to write out a valid PostScript [1] file, which can be viewed or printed using a PostScript viewer such as the freely available Ghostscript/GSview [2]. In fact, the viewer can readily be invoked by a method within the wrapper object, so that the plot simply pops up in its own window on your screen.

An example will make this clearer. Figure 22.1.1 shows a sample plot that has a couple of $x$ ; $y$ scaled boxes, some lines and points of varying types, and some text labels. Here is the code that generates the figure:

x1[i] $=$ 5.\*i/499.;   
y1[i] $=$ exp(-0.5\*x1[i]);   
y2[i] $=$ exp(-0.5\*SQR(x1[i]));   
y3[i] $=$ exp(-0.5\*sqrt(5.-x1[i]));   
x2[i] $=$ cos(0.062957\*i);   
y4[i] $=$ sin(0.088141\*i);

# }

PSpage pg("d:\\nr3\\newchap20\\myplot.ps") PSplot plot1(pg,100.,500.,100.,500.);   
plot1.setlimits(0.,5.,0.,1.);   
plot1.frame();   
plot1.autoscales();   
plot1.xlabel("abscissa");   
plot1.ylabel("ordinate");   
plot1.lineplot(x1,y1);   
plot1.setdash("2 4");   
plot1.lineplot(x1,y2);   
plot1.setdash("6 2 4 2");   
plot1.lineplot(x1,y3);   
plot1.setdash("");   
plot1.pointsymbol(1.,exp(-0.5),72,16.);   
plot1.pointsymbol(2.,exp(-1.),108,12.);   
plot1.pointsymbol(2.,exp(-2.),115,12.);   
plot1.label("dingbat 72",1.1,exp(-0.5));   
plot1.label("dingbat 108",2.1,exp(-1.));   
plot1.label("dingbat 115",2.1,exp(-2.));   
Instantiate a page.   
Instantiate a plot on the page. Position is specified in pt $( 7 2 { \mathsf { p t } } =$ 1 in, or $2 8 ~ { \mathsf { p t } } = 1 ~ { \mathsf { c m } }$ ).

Unsets dash.

PSplot plot2(pg,325.,475.,325.,475.);   
plot2.clear();   
plot2.setlimits(-1.2,1.2,-1.2,1.2);   
plot2.frame();   
plot2.scales(1.,0.5,1.,0.5);   
plot2.lineplot(x2,y4); Instantiate a second plot.   
Erase what’s underneath it. pg.close();   
pg.display();

Pop up a window displaying the plot file.

The general idea is that a PSpage object (pg in the example above) represents a whole sheet of paper, or window on the screen. It can contain one or more PSplot objects. In the above example there are two: plot1 and plot2. PSplot objects can be separate on the page, or overlapping. Each has its own $x , y$ coordinate system, its own $x$ - and $y$ -axis labels, and so forth. With no more explanation than this, you should be able to find a program line above that corresponds to each feature in the figure. The last line makes the plot pop up on our screen.

Point symbols are referenced by their character number in the Zapf Dingbats font, which is built into PostScript. If you want to see all the possible symbols, a Web search for “LaTeX Postscript Dingbats” will turn up several charts. Or, just write a program to plot them all. (Hint: There are possibly useful symbols from 33 to 126, and from 161 to 254.)

A Webnote [3] gives the complete source code for the PSpage and PSplot objects, which is only about 150 lines long. In the course of writing this book, our personal version of the code expanded to about 450 lines. This is an order of magnitude or two less than the standard packages that are available in open source code, GNUPLOT, for example [4]. It is a question of trading off capability (theirs much greater) for ease of modifying the source code (you be the judge).

If you choose to go down this road, you’ll soon want to learn more of PostScript as a language. A good reference is [5].

# CITED REFERENCES AND FURTHER READING:

Adobe Systems, Inc. 1999, PostScript Language Reference, 3rd ed. (Reading, MA: Addison-Wesley).[1]   
Ghostscript and GSview $^ { 2 0 0 7 + }$ , at http://www.cs.wisc.edu/\~ghost/.[2]   
Numerical Recipes Software 2007, “Code for PSpage and PSplot,” Numerical Recipes Webnote No. $^ { 2 6 }$ ,athttp://www.nr.com/webnotes?26 [3]   
GNUPLOT $^ { 2 0 0 7 + }$ , at http://www.gnuplot.info.[4]   
McGilton, H., and Campione, M. 1992, PostScript by Example (Reading, MA: Addison-Wesley).[5]

# 22.2 Diagnosing Machine Parameters

A convenient fiction is that a computer’s floating-point arithmetic is “accurate enough.” If you believe this fiction, then numerical analysis becomes a very clean subject. Roundoff error disappears, and many finite algorithms are exact. Only manageable truncation error (-1.1) stands between you and a perfect calculation. Sounds rather naive, doesn’t it?

Yes, it is naive. Notwithstanding, we have adopted this fiction throughout most of this book. To do a good job of answering the question of how roundoff error propagates, or can be bounded, for every algorithm that we have discussed would be impractical. In fact, it would not be possible: Rigorous analysis of many practical algorithms has never been made, by us or anyone.

Almost all processors today share the same floating-point data representation, namely that specified in IEEE Standard 754-1985 [1], and therefore the same strengths and weaknesses as regards roundoff error. But this was not always so! The history of computing is full of machines with strange floating-point representations by modern standards. Many early computers had 36-bit words, typically partitioned as a sign bit, 8 bits of exponent, and 27 bits of mantissa. The influential IBM 7090/7094 series was of this type. The legendary CDC 6600 and 7600 machines, designed by Seymour Cray, had 60-bit words (sign, 11-bit exponent, 48-bit mantissa). A particularly odd design was the IBM STRETCH, whose 64 bits were allocated to an exponent flag bit, 10 exponent bits, the exponent sign, a 48-bit mantissa, its sign, and three flag bits. The exponent flag bit was used to signal overflow or underflow, while the other flag bits could be set by the user to indicate — anything! So let us all be grateful for IEEE 754.

Likewise, almost all numerical computing today is done in double precision, that is, in 64-bit words, what $\mathrm { C } { + } { + }$ defines as double and we denote as Doub. This, also, was not always so. It has happened (one might argue) because the availability of memory has increased even more rapidly than the appetite for it in numerical computation. Many programmers born before 1960 still feel a small frisson when they type double instead of float. Indeed, the vast majority of routines in this book will work just fine, for the vast majority of applications, with merely float precision. In most cases, the use of double simply serves to reinforce an erroneous belief in the above “convenient fiction.”

Still, every once in a while, you will need to know what the limitations of your machine’s floating-point arithmetic actually are — the more so when your treatment of floating-point roundoff error is going to be intuitive, experimental, or casual. This will certainly be true if you ever encounter a processor with nonstandard (that is, non-IEEE compliant) hardware. Such processors still do exist, though generally hidden away in embedded special-purpose devices.

If you are lucky, then calls to the methods in the $\mathrm { C } { + } { + }$ standard library class numeric_limits will tell you what you need to know. It is a good idea to familiarize yourself with that class, including some of its esoterica, like round_style and has_denorm [2].

A more experimental approach is to use methods that were developed to ferret out machine parameters in the bad old days before standards [3,4], especially parameters that were supposed to be transparent to the (ordinary) user. The object Machar, listed in full in a Webnote [5], gives an implementation of a number of of these methods. The quantities determined are

- ibeta is the radix in which numbers are represented, almost always 2, but historically sometimes 16, or even 10.   
- it is the number of base-ibeta digits in the floating-point mantissa $M$ .   
- machep is the exponent of the smallest (most negative) power of ibeta that, added to 1:0, gives something different from 1:0.   
- eps is the floating-point number ibetamachep, loosely referred to as the “floating-point precision.”   
- negep is the exponent of the smallest power of ibeta that, subtracted from 1:0, gives something different from 1:0.   
- epsneg is ibeta $\mathtt { n e g e p }$ , another way of defining floating-point precision. Not infrequently, epsneg is 0.5 times eps; occasionally eps and epsneg are equal.   
- iexp is the number of bits in the exponent (including its sign or bias).   
- minexp is the smallest (most negative) power of ibeta consistent with there being no leading zeros in the mantissa.   
- xmin is the floating-point number ibetaminexp, generally the smallest (in magnitude) useable floating value.   
- maxexp is the smallest (positive) power of ibeta that causes overflow.   
- xmax is $( 1 - \mathsf { e p s n e g } ) \times \mathsf { i b e t a } ^ { \mathrm { m a x e x p } }$ , generally the largest (in magnitude) useable floating value.   
- irnd returns a code in the range 0 : : : 5, giving information on what kind of rounding is done in addition, and on how underflow is handled. See below.   
- ngrd is the number of “guard digits” used when truncating the product of two mantissas to fit the representation.

The parameter irnd needs some additional explanation. In the IEEE standard, bit patterns correspond to exact, “representable” numbers. The specified method for rounding an addition is to add two representable numbers “exactly,” and then round the sum to the closest representable number. If the sum is precisely halfway between two representable numbers, it should be rounded to the even one (low-order bit zero). The same behavior should hold for all the other arithmetic operations, that is, they should be done in a manner equivalent to infinite precision, and then rounded to the closest representable number.

If irnd returns 2 or 5, then your processor is compliant with this standard. If it returns 1 or 4, then it is doing some kind of rounding, but not the IEEE standard. If irnd returns 0 or 3, then it is truncating the result, not rounding it — not desirable.

<table><tr><td rowspan=1 colspan=4>Sample Results Returned by Machar</td></tr><tr><td rowspan=1 colspan=1>precision</td><td rowspan=1 colspan=2>IEEE-compliant processorfloat          double</td><td rowspan=1 colspan=1>historicalDEC-VAX</td></tr><tr><td rowspan=1 colspan=1>ibeta</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>it</td><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1>53</td><td rowspan=1 colspan=1>24</td></tr><tr><td rowspan=1 colspan=1>machep</td><td rowspan=1 colspan=1>-23</td><td rowspan=1 colspan=1>-52</td><td rowspan=1 colspan=1>-24</td></tr><tr><td rowspan=1 colspan=1>eps</td><td rowspan=1 colspan=1>1.19 × 10-7</td><td rowspan=1 colspan=1>2.22 × 10-16</td><td rowspan=1 colspan=1>5.96 × 10-8</td></tr><tr><td rowspan=1 colspan=1>negep</td><td rowspan=1 colspan=1>-24</td><td rowspan=1 colspan=1>-53</td><td rowspan=1 colspan=1>-24</td></tr><tr><td rowspan=1 colspan=1>epsneg</td><td rowspan=1 colspan=1>5.96 × 10-8</td><td rowspan=1 colspan=1>1.11 × 10-16</td><td rowspan=1 colspan=1>5.96×10-8</td></tr><tr><td rowspan=1 colspan=1>iexp</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1>minexp</td><td rowspan=1 colspan=1>-126</td><td rowspan=1 colspan=1>-1022</td><td rowspan=1 colspan=1>-128</td></tr><tr><td rowspan=1 colspan=1>xmin</td><td rowspan=1 colspan=1>1.18 × 10-38</td><td rowspan=1 colspan=1>2.23×10-308</td><td rowspan=1 colspan=1>2.94 × 10-39</td></tr><tr><td rowspan=1 colspan=1>maxexp</td><td rowspan=1 colspan=1>128</td><td rowspan=1 colspan=1>1024</td><td rowspan=1 colspan=1>127</td></tr><tr><td rowspan=1 colspan=1>xmax</td><td rowspan=1 colspan=1>3.40 × 1038</td><td rowspan=1 colspan=1>1.79 × 10308</td><td rowspan=1 colspan=1>1.70 × 1038</td></tr><tr><td rowspan=1 colspan=1>irnd</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>ngrd</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr></table>

The other issue addressed by irnd concerns underflow. If a floating value is less than xmin, many computers underflow its value to zero. Values $\mathrm { i r n d } = 0 , 1$ ; or 2 indicate this behavior. The IEEE standard specifies a more graceful kind of underflow: As a value becomes smaller than xmin, its exponent is frozen at the smallest allowed value while its mantissa is decreased, acquiring leading zeros and “gracefully” losing precision. This is indicated by $\mathrm { i r n d } = 3 , 4$ ; or 5.

Sometimes results can be compiler-dependent. For example, some compilers underflow intermediate results ungracefully, yielding irnd $= 2$ rather than 5.

Call the report method in Machar to see the comparison between its results and those returned by numeric_limits. Some values returned by Machar for IEEE compliant processors are given in the table above and compared with an important historical processor, the DEC-VAX. This processor, like its predecessor PDP-11, used a representation with a “phantom” leading 1 bit in the mantissa. You can see that this achieved a smaller eps for the same wordlength but could not underflow gracefully, since there were no denormalized numbers.

# CITED REFERENCES AND FURTHER READING:

IEEE Standard for Binary Floating-Point Numbers,ANSI/IEEE Std 754-1985 (New York: IEEE, 1985).[1]   
Josuttis, N.M. 1999, The $C { + } { + }$ Standard Library: A Tutorial and Reference (Boston: Addison-Wesley), $\ S 4 . 3 . [ 2 ]$ 1   
Cody, W.J. 1988, “MACHAR: A Subroutine to Dynamically Determine Machine Parameters,” ACM Transactions on Mathematical Software,vol.14, pp. 303-311.[3]   
Malcolm, M.A. 1972, “Algorithms to Reveal Properties of Floating-Point Arithmetic,” Communications of the ACM, vol.15,pp.949-951.[4]   
Numerical Recipes Software 2007, “Code for Machar,” Numerical Recipes Webnote No. 27, at http://www.nr.com/webnotes?27 [5]   
Goldberg, D. 1991, “What Every Computer Scientist Should Know About Floating-Point Arithmetic,” ACM Computing Surveys, vol. 23, pp. 5–48.

# 22.3 Gray Codes

A Gray code is a function $G ( i )$ of the integers $i$ that for each integer $N \geq 0$ is one-to-one for $0 \leq i \leq 2 ^ { N } - 1$ , and that has the following remarkable property: The binary representations of $G ( i )$ and $G ( i + 1 )$ differ in exactly one bit. An example of a Gray code (in fact, the most commonly used one) is the sequence 0000, 0001, 0011, 0010, 0110, 0111, 0101, 0100, 1100, 1101, 1111, 1110, 1010, 1011, 1001, and 1000, for $i = 0 , \ldots , 1 5$ . The algorithm for generating this code is simply to form the bitwise exclusive-or (XOR) of $i$ with $i / 2$ (integer part). Think about how the carries work when you add one to a number in binary, and you will be able to see why this works. You will also see that $G ( i )$ and $G ( i + 1 )$ differ in the bit position of the rightmost zero bit of $i$ (prefixing a leading zero if necessary).

The spelling is “Gray,” not “gray”: The codes are named after one Frank Gray, who first patented the idea for use in shaft encoders. A shaft encoder is a wheel with concentric coded stripes, each of which is “read” by a fixed optical sensor or conducting brush. The idea is to generate a binary code describing the angle of the wheel. The obvious, but wrong, way to build a shaft encoder is to have one stripe (the innermost, say) present on half the wheel, but absent on the other half; the next stripe is present in quadrants 1 and 3; the next stripe is present in octants 1, 3, 5, and 7; and so on. The optical or electrical sensors together then read a direct binary code for the position of the wheel.

The reason this method is bad is that there is no way to guarantee that all the brushes will make or break contact exactly simultaneously as the wheel turns. Going from position 7 (0111) to 8 (1000), one might pass spuriously and transiently through 6 (0110), 14 (1110), and 10 (1010), as the different brushes make or break contact. Use of a Gray code on the encoding stripes guarantees that there is no transient state between 7 (0100 in the sequence above) and 8 (1100).

Of course we then need circuitry, or algorithmics, to translate from $G ( i )$ to $i$ . Figure 22.3.1(b) shows how this is done by a cascade of XOR gates. The idea is that each output bit should be the XOR of all more significant input bits. To do $N$ bits of Gray code inversion requires $N - 1$ steps (or gate delays) in the circuit. (Nevertheless, this is typically very fast in circuitry.) In a register with word-wide binary operations, we don’t have to do $N$ consecutive operations, but only $\ln _ { 2 } N$ . The trick is to use the associativity of XOR and group the operations hierarchically. This involves sequential right-shifts by $1 , 2 , 4 , 8 , \ldots$ bits until the wordlength is exhausted. Here is a piece of code for doing both $G ( i )$ and its inverse:


<!-- chunk 0018: pages 1191-1260 -->
![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0018_pages_1191-1260/auto/images/c8d39bd479d7069bb175a27deb475da158dc3822b2d52f2be6734029d4a7a46a.jpg)

(a)

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0018_pages_1191-1260/auto/images/c20adf96de98c1b083f2c59ab10d8889cd96036c78fb4814fd42a55b66bcf44c.jpg)  
Figure 22.3.1. Single-bit operations for calculating the Gray code $G ( i )$ from $i$ (a), or the inverse (b). LSB and MSB indicate the least and most significant bits, respectively. XOR denotes exclusive-or.

# struct Gray {

Methods for the Gray code and its inverse.

Uint gray(const Uint n) {return n ^ (n >> 1);} Return the Gray code of an integer n. This is the easy direction!

Uint invgray(const Uint n) { Return the inverse of the Gray code. Int ish $^ { = 1 }$ ; Uint ans $= _ { \mathrm { n } }$ ,idiv; for (;;) { In hierarchical stages, starting with a one-bit right-shift, ans $\hat { \mathbf { \alpha } } =$ (idiv=ans >> ish); cause each bit to be XORed with all more sigif (idiv $\scriptstyle < = ~ 1$ || ish $\scriptstyle = = \ 1 6 $ ) return ans; nificant bits. ish $< < = ~ 1$ ; Double the amount of shift on the next cycle. } } };

In numerical work, Gray codes can be useful when you need to do some task that depends intimately on the bits of $i$ , looping over many values of $i$ . Then, if there are economies in repeating the task for values differing by only one bit, it makes sense to do things in Gray code order rather than consecutive order. We saw an example of this in $\ S 7 . 8$ , for the generation of quasi-random sequences.

# CITED REFERENCES AND FURTHER READING:

Horowitz, P., and Hill, W. 1989, The Art of Electronics, 2nd ed. (New York: Cambridge University Press), $\ S 8 . 0 2$ .   
Knuth, D.E. 2005, Generating All Tuples and Permutations, fascicle 2 of vol. 4 of The Art of Computer Programming (Upper Saddle River, NJ: Addison-Wesley), $\ S 7 . 2 . 1 . 1$ .

# 22.4 Cyclic Redundancy and Other Checksums

There are networks all around you: not just “the” Internet with its IP and TCP protocols, but also embedded networks that move bits around within a device or among closely coupled devices. Examples include the SMBus network that communicates power management information between smart batteries and the devices that they power, or the Bluetooth network that connects cell phones to nearby accessories. We wouldn’t be overly surprised to find a network inside of our wristwatch or electric toothbrush!

Different networks have different protocols, but standard engineering practice is to package the raw information into packets with fixed or variable numbers of bits. Packet lengths are typically in the range from a few tens to a few thousand bits. Smaller would imply proportionally too much overhead per packet, while longer would make excessive demands on buffer sizes, collision avoidance, etc.

When a packet is sent from point A to point B, one wants to know that it has arrived without error. The simplest form of insurance is to add a “parity bit,” chosen so as to make the total number of one-bits (versus zero-bits) either always even (“even parity”) or always odd (“odd parity”). Any single-bit error in a packet will thereby be detected. When errors are sufficiently rare, or their consequence sufficiently minor, use of parity provides enough error detection. For example, the ASCII character set was originally designed for 7-bit characters, with an 8th parity bit.

Since the parity bit has two possible values (0 and 1), it has, on average, only a $50 \%$ chance of detecting an erroneous packet with multiple wrong bits. That is not nearly good enough for most applications. Most communications protocols [1] use a multibit generalization of the parity bit called a “cyclic redundancy check” or CRC. Often, the CRC is 16 bits (two bytes) long. Then the chance of a random set of errors going undetected is 1 in $2 ^ { 1 6 } = 6 5 5 3 6$ .

Now enters mathematics. It is easy to find $M$ -bit CRCs that have the property of detecting all errors that occur in $M$ or fewer consecutive bits, for any length of message. (We prove this below.) Since noise in communication channels tends to be “bursty,” with short sequences of adjacent bits getting corrupted, this consecutive-bit property is highly desirable. Furthermore, for packets with a fixed (or bounded) payload size of $N$ bits, one can find CRCs that find all occurrences of $D$ or fewer errors anywhere in the payload. Obviously, the game is to find the CRC that maximizes $D$ . The value $D + 1$ is the Hamming distance of the CRC for that value of $N$ using that checksum (cf. $\ S 1 6 . 2 )$ .

<table><tr><td rowspan=1 colspan=4>Useful 16-bit CRC Polynomials (after [3])</td></tr><tr><td rowspan=1 colspan=1>j</td><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Polynomial</td><td rowspan=1 colspan=1>Best N (bits)</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0x755B=(x³+x²+1)*(x6+x5+x²+x+1)*(x7+x³+1)*</td><td rowspan=1 colspan=1>242-2048+</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>OxA7D3=(x³+x²+1)*(x+x5+x²+x+1)*(x7+x6+x5+x4+1)*</td><td rowspan=1 colspan=1>256-2048+</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>ANSI-16</td><td rowspan=1 colspan=1>0x8005=(x+1)(x15+x+1)*</td><td rowspan=1 colspan=1>242-2048+</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>CCITT-16</td><td rowspan=1 colspan=1>0x1021=(x+1)(x15+x14+x13+x12+x4+x³+x2+x+1)*</td><td rowspan=1 colspan=1>242-2048+</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0x5935=(x16+x14+𝑥1²+x11+x8+x5+x4+x²+1)</td><td rowspan=1 colspan=1>136-241</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0x90D9=(x+1)(x15+x11+x10+x9+x8+x7+x5+x4+x²+x+1)</td><td rowspan=1 colspan=1>20-135</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>IEC-16</td><td rowspan=1 colspan=1>0x5B93=(x+1)(x+1)(x7+x+x³+x+1)*(x7+x+x5+x4+x³+x²+1)*</td><td rowspan=1 colspan=1>20-112</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0x2D17=(x²+x+1)*(x14+x1³+x9+x7+x5+x4+1)</td><td rowspan=1 colspan=1>16-19</td></tr><tr><td rowspan=1 colspan=4>* denotes primitive factor</td></tr></table>

The design of CRCs lies in the province of communications software experts and chip-level hardware designers — people with bits under their fingernails. A passing familiarity with some of the concepts involved can be useful, however, both because the mathematics involved has connections to other applications (for example, random number generation, cf. $\ S 7 . 1$ and $\ S 7 . 5$ , and because you might actually want to add a couple of bytes of checksum to your own data records in some applications where you are handling, or moving, large amounts of data.

Sometimes CRCs can be used to compress data as they are recorded. If identical data records occur frequently, one can keep sorted in memory the CRCs of previously encountered records. A new record is archived in full if its CRC is different, otherwise only a pointer to a previous record need be archived. In this application one might use 8 bytes of CRC, to make the odds of mistakenly discarding a different data record tolerably small; or, if previous records can be randomly accessed, a full comparison can be made to decide whether records with identical CRCs are in fact identical.

Now let us briefly discuss the theory of CRCs. After that, we will give an implementation that generates 16-bit CRCs that are known to be particularly good, or else are enshrined as standard (and, it turns out, this is not the same thing!).

The mathematics underlying CRCs is “polynomials over the integers modulo 2.” Any binary message can be thought of as a polynomial with coefficients 0 and 1. For example, the message “1100001101” is the polynomial $x ^ { 9 } + x ^ { 8 } + x ^ { 3 } + x ^ { 2 } + 1$ Since 0 and 1 are the only integers modulo 2, a power of $x$ in the polynomial is either present (1) or absent (0).

An $M$ -bit-long CRC is based on a polynomial of degree $M$ , called the generator polynomial. Given the generator polynomial $G$ (which can be written either in polynomial form or as a bit-string, e.g., 10001000000100001 for $x ^ { 1 6 } + x ^ { 1 2 } + x ^ { 5 } + 1 )$ , here is how you compute the CRC for a sequence of bits $S$ : First, multiply $S$ by $x ^ { M }$ , that is, append $M$ zero bits to it. Second, divide, by long division, $G$ into $S x ^ { M }$ . Keep in mind that the subtractions in the long division are done modulo 2, so that there are never any “borrows”: Modulo 2 subtraction is the same as logical exclusive-or (XOR). Third, ignore the quotient you get. Fourth, when you eventually get to a remainder, it is the CRC; call it $C$ . $C$ will be a polynomial of degree $M - 1$ or less, otherwise you would not have finished the long division. Therefore, in bit-string form, it has $M$ bits, which may include leading zeros. ( $C$ might even be all zeros; see below.)

If you work through the above steps in an example, you will see that most of what you write down in the long-division tableau is superfluous. You are actually just left-shifting sequential bits of $S$ , from the right, into an $M$ -bit register. Every time a 1 bit gets shifted off the left end of this register, you zap the register by an XOR with the $M$ low-order bits of $G$ (that is, all the bits of $G$ except its leading 1). When a 0 bit is shifted off the left end you don’t zap the register. When the last bit that was originally part of $S$ gets shifted off the left end of the register, what remains is the CRC.

You can immediately recognize how efficiently this procedure can be implemented in hardware. It requires only a shift register with a few hard-wired XOR taps into it. That is how CRCs are computed in communications devices, taking a tiny part of a single chip. In software, the implementation is not so elegant, since bit-shifting is not generally very efficient. One therefore typically finds (as in our implementation below) table-driven routines that pre-calculate the result of a bunch of shifts and XORs, say for each of 256 possible 8-bit inputs [2].

Every generator polynomial of degree $M$ with a nonzero $x ^ { 0 }$ term yields a CRC that detects all possible combinations of errors in any frame of $M$ consecutive bits. (A special case of this is that it detects any single-bit error in a message of arbitrary length $N$ .) To see how this works, suppose two messages, $S$ and $T$ , differ only within a frame of $M$ bits. Then their CRCs differ by an amount that is the remainder when $G$ is divided into $( S - T ) x ^ { M } \equiv R$ . Now $R$ has the form of leading zeros (which can be ignored), followed by some 1’s in an $M$ -bit frame, followed by trailing zeros (which are just multiplicative factors of $x$ ): $R = x ^ { n } F$ , where $F$ is a polynomial of degree at most $M - 1$ and $n > 0$ . But since $G$ has a nonzero $x ^ { 0 }$ term, it is not divisible by $x$ . So $G$ cannot divide $R$ . Therefore $S$ and $T$ must have different CRCs.

What about two-bit errors, not necessarily in a frame of size $M ?$ That leads us to primitive polynomials: A polynomial over the integers modulo 2 may be irreducible, meaning that it can’t be factored. A subset of the irreducible polynomials is the primitive polynomials. These generate maximum length sequences when used in shift registers, as described in $\ S 7 . 5$ . The polynomial $x ^ { 2 } + 1$ is not irreducible: $x ^ { 2 } +$ $1 = ( x + 1 ) ( x + 1 )$ , so it is also not primitive. The polynomial $x ^ { 4 } + x ^ { 3 } + x ^ { 2 } + x + 1$ is irreducible, but it turns out not to be primitive. The polynomial $x ^ { 4 } + x + 1$ is both irreducible and primitive.

Primitive polynomials are here interesting because they have a very high order. Don’t confuse order with degree: The order $e$ of a polynomial is the smallest integer $e$ such that the polynomial divides (in the present mod 2 case) $x ^ { e } + 1$ . Primitive polynomials, it turns out, have the largest possible order $e$ for their degree $n$ , given by

$$
e = 2 ^ { n } - 1
$$

(In fact, this is why their shift registers have maximum length.) If two messages differ on exactly two bits, spaced $k$ bits apart, then their difference is $x ^ { k } + 1$ times some trailing powers of $x$ . If the generator $G$ contains a primitive factor of order $e$ , then $G$ can’t possibly divide this difference, as long as $k < e$ .

Thus, a primitive factor of degree $n$ guarantees two-bit error detection for spacings up to $2 ^ { n } - 1$ . For this reason, generators are often chosen to be primitive polynomials of degree $M$ . Alternatively, the generator may be chosen be a primitive polynomial times $( 1 + x )$ , which turns out to detect parity errors for all message sizes $N$ , while the range of two-bit detections is reduced only by a factor of 2.

A number of “standard” CRC polynomials were chosen by no other criteria, sometimes adding only the criterion that they should have only a small number of terms. (This was at one time important for hardware design.) For example, the CCITT (Comite Consultatif International T ´ el´ egraphique et T ´ el´ ephonique) has ´ anointed $x ^ { 1 6 } + x ^ { 1 2 } + x ^ { 5 } + 1$ as “CCITT- $1 6 ^ { \circ }$ ; it is the product of $x + 1$ and a primitive polynomial. The polynomial ANSI-16 (see table on p. 1169) also has this character.

Similarly for some choices other than 16 bits: “CRC-12” is $( x + 1 ) ( x ^ { 1 1 } + x ^ { 2 } +$ 1/, the latter factor being primitive. The most common 32-bit CRC, “CRC-32,” used in the ethernet standard (IEEE 802.3) and elsewhere, is $x ^ { 3 2 } + x ^ { 2 6 } + x ^ { 2 3 } + x ^ { 2 2 } +$ $x ^ { 1 6 } + x ^ { 1 2 } + x ^ { 1 1 } + x ^ { 1 0 } + x ^ { 8 } + x ^ { 7 } + x ^ { 5 } + x ^ { 4 } + x ^ { 2 } + x + 1$ , which is primitive.

Now here is something relatively new in this ancient field [3]: For carefully chosen generators $G$ , all two-bit errors in a packet with payload size $N$ can be detected even if $e < N$ . This is because the previous argument was sufficient, but not necessary: A cleverly chosen $G$ can fail to divide $x ^ { k } - 1$ for other reasons than having a primitive factor of large order. This idea opens up the design space to search, essentially by brute force, for generators that have $D > 2$ , that is, are capable of finding not just all two-bit errors, but all three-bit errors, all four-bit errors, etc., up to some bound that depends on $N$ and $M$ . Several of these “new” generators are shown in the table on p. 1169, which is based on [3] (which see for details), along with their recommended values of $N$ . A generator that is good for large $N$ is not necessarily good for small $N$ , and vice versa, so you should stick to the recommended values. The hexadecimal values in the table give binary representations of the polynomials, with the convention that each must be prefaced by a leading 1 (the $x ^ { 1 6 }$ term).

In most protocols, a transmitted block of data consists of some $N$ data bits, directly followed by the $M$ bits of their CRC (or the CRC XORed with a constant; see below). There are two equivalent ways of validating a block at the receiving end. Most obviously, the receiver can compute the CRC of the data bits, and compare it to the transmitted CRC bits. Less obviously, but more elegantly, the receiver can simply compute the CRC of the total block, with $N + M$ bits, and verify that a result of zero is obtained. Proof: The total block is the polynomial $S x ^ { M } + C$ (data left-shifted to make room for the CRC bits). The definition of $C$ is that $S x ^ { m } = Q G + C$ , where $Q$ is the discarded quotient. But then $S x ^ { M } + C = Q G + C + C = Q G$ (remember modulo 2), which is a perfect multiple of $G$ . It remains a multiple of $G$ when it gets multiplied by an additional $x ^ { M }$ on the receiving end, so it has a zero CRC, q.e.d.

A couple of small variations on the basic procedure need to be mentioned [1]: First, when the CRC is computed, the $M$ -bit register need not be initialized to zero.

Initializing it to some other $M$ -bit value (e.g., all 1’s) in effect prefaces all blocks by a phantom message that would have given the initialization value as its remainder. It is advantageous to do this, since the CRC described thus far otherwise cannot detect the addition or removal of any number of initial zero bits. (Loss of an initial bit, or insertion of zero bits, are common “clocking errors.”) Second, one can add (XOR) any $M$ -bit constant $K$ to the CRC before it is transmitted. This constant can either be XORed away at the receiving end, or else it just changes the expected CRC of the whole block by a known amount, namely the remainder of dividing $G$ into $K x ^ { M }$ . The constant $K$ is frequently “all bits,” changing the CRC into its ones complement. This has the advantage of detecting another kind of error that the CRC would otherwise not find: deletion of an initial 1 bit in the message with spurious insertion of a 1 bit at the end of the block.

The following object Icrc implements the calculation of 16-bit CRCs for the generators listed in the table. The constructor sets which generator is to be used, and also whether the initial register should be all bits (the default) or zero. Icrc is loosely based on the function in [2]. Here is how to understand its operation: First look at the function icrc1. This is used only by the constructor, to initialize a table of length 256, incorporating one character into a 16-bit CRC register. The only trick used is that a character’s bits are XORed into the most significant bits of the register, all eight together, instead of being fed into the least significant bit, one bit at a time, at the time of the register shift. This works because XOR is associative and commutative — we can feed in character bits any time before they will determine whether to zap with the generator polynomial.

Now look at the methods crc and concat. Go back to thinking about a character’s bits being shifted into the CRC register from the least significant end. The key observation is that while 8 bits are being shifted into the register’s low end, all the generator zapping is being determined by the bits already in the high end. Since XOR is commutative and associative, all we need is a table of the results of all this zapping, for each of 256 possible high-bit configurations. Then we can play catch-up and XOR an input character into the result of a lookup into this table. But this is exactly the table that was constructed by icrc1. References [2,4,5] give further details on table-driven CRC computations.

# struct Icrc {

Object for computing 16-bit cyclic redundancy checksums.

Uint jcrc,jfill,poly;   
static Uint icrctb[256];   
Icrc(const Int jpoly, const Bool fill $=$ true) : jfill(fill ? 255 : 0) {   
Constructor. Choose one of 8 generators (see table) by the value of jpoly. Initialize the   
CRC register to all bits if fill is true, otherwise to zero. Int j; Uint okpolys[8] $=$ {0x755B,0xA7D3,0x8005,0x1021,0x5935,0x90D9,0x5B93,0x2D17}; Generator polynomials, see table. poly $=$ okpolys[jpoly & 7]; for ( $\scriptstyle \dot { \mathcal { I } } = 0$ ;j<256; ${ \mathrm { j } } ^ { + + }$ ) { icrctb[j] $=$ icrc1(j << 8,0); Table of CRCs of all characters. jcrc $=$ (jfill | (jfill << 8));   
Uint crc(const string &bufptr) {   
Initialize the CRC register, compute and return the 16-bit CRC for the string bufptr. jcrc $=$ (jfill | (jfill $\ < < ~ 8 )$ ); return concat(bufptr);   
}

Uint concat(const string &bufptr) {

Without reinitializing the CRC register, compute and return the 16-bit CRC for the string bufptr. In effect, this appends bufptr to previous strings since the last call of crc and returns the overall CRC.

Uint j,cword=jcrc,len=bufptr.size();   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<len;j++) { Loop over the characters in the string. cword=icrctb[Uchar(bufptr[j]) ^ hibyte(cword)] ^ (lobyte(cword) << 8);   
return jcrc $=$ cword;

Uint icrc1(const Uint jcrc, const Uchar onech) {

Given a remainder up to now, return the new CRC after one character is added. Used by Icrc to initialize its table.

Int i;   
Uint ans ${ } = { }$ (jcrc ^ onech $\ < < ~ 8 )$ ;   
for ( $\scriptstyle { \dot { 1 } } = 0$ ;i<8; $\dot { \bf 1 } + +$ ) { Here is where 8 one-bit shifts, and some XORs if (ans & 0x8000) ans $=$ (ans $\angle < = \ 1$ ) $\hat { }$ poly; with the generator polyelse ans $< < = ~ 1$ ; nomial, are done. ans $\& =$ 0xffff;   
}   
return ans;

inline Uchar lobyte(const unsigned short x) { return (Uchar) $( \mathbb { x }$ & 0xff); } inline Uchar hibyte(const unsigned short x) { return (Uchar)( $( \mathrm {  ~ x ~ } > > \mathrm {  ~ 8 ~ }$ ) & 0xff); } }; Uint Icrc::icrctb[256];

What if you need more than 16 bits of checksum? For a true 32-bit CRC, you will need to rewrite the routines given to work with a longer generating polynomial. For example, $x ^ { 3 2 } + x ^ { 7 } + x ^ { 5 } + x ^ { 3 } + x ^ { 2 } + x + 1$ is primitive modulo 2 and has nonleading, nonzero bits only in its least significant byte (which makes for some simplification). The idea of table lookup on only the most significant byte of the CRC register goes through unchanged.

Easier, if you don’t care about the $M$ -consecutive bit property of the checksum, is to just instantiate more than one copy of Icrc, each with a different generator (first argument in constructor). These provide statistically independent checks.

# 22.4.1 Other Kinds of Checksums

Quite different from CRCs are the various techniques used to append a decimal “check digit” to numbers that are handled by human beings (e.g., typed into a computer). Check digits need to be proof against the kinds of highly structured errors that humans tend to make, such as transposing consecutive digits. Wagner and Putter [6] give an interesting introduction to this subject, including specific algorithms.

Checksums now in widespread use vary from fair to poor. The 10-digit ISBN (International Standard Book Number) that you find on most books, including this

one, uses the check equation

$$
1 0 d _ { 1 } + 9 d _ { 2 } + 8 d _ { 3 } + \cdots + 2 d _ { 9 } + d _ { 1 0 } = 0 { \pmod { 1 1 } }
$$

where $d _ { 1 0 }$ is the right-hand check digit. The character “X” is used to represent a check digit value of 10. Another popular scheme is the so-called “IBM check,” often used for account numbers (including, e.g., MasterCard). Here, the check equation is

$$
2 \# d _ { 1 } + d _ { 2 } + 2 \# d _ { 3 } + d _ { 4 } + \cdots = 0 \pmod { 1 0 }
$$

where $2 \# d$ means, “multiply $d$ by two and add the resulting decimal digits.” United States banks code checks with a nine-digit processing number whose check equation is

$$
3 a _ { 1 } + 7 a _ { 2 } + a _ { 3 } + 3 a _ { 4 } + 7 a _ { 5 } + a _ { 6 } + 3 a _ { 7 } + 7 a _ { 8 } + a _ { 9 } = 0 { \pmod { 1 0 } }
$$

The familiar 12-digit Universal Product Code (UPC) is printed with both a decimal representation and a synonymous bar code. The digits are divided into a one-digit “category,” a five-digit manufacturer, a five-digit product identification, and one-digit checksum. The check equation is

$$
3 a _ { 1 } + a _ { 2 } + 3 a _ { 3 } + a _ { 4 } + 3 a _ { 5 } + \cdot \cdot \cdot + 3 a _ { 1 1 } + a _ { 1 2 } = 0 { \pmod { 1 0 } }
$$

The bar code put on many envelopes by the U.S. Postal Service is decoded by removing the single tall marker bars at each end and breaking the remaining bars into six or ten groups of five. In each group the five bars signify (from left to right) the values $7 , 4 , 2 , 1 , 0$ . Exactly two of them will be tall. Their sum is the represented digit, except that zero is represented as $7 + 4$ . The five- or nine-digit zip code is followed by a check digit, with the check equation

$$
\sum d _ { i } = 0 { \pmod { 1 0 } }
$$

None of these schemes is close to optimal. An elegant scheme due to Verhoeff is described in [6]. The underlying idea is to use the ten-element dihedral group $D _ { 5 }$ , which corresponds to the symmetries of a pentagon, instead of the cyclic group of the integers modulo 10. The check equation is

$$
a _ { 1 } * f ( a _ { 2 } ) * f ^ { 2 } ( a _ { 3 } ) * \cdots * f ^ { n - 1 } ( a _ { n } ) = 0
$$

where $^ *$ is (noncommutative) multiplication in $D _ { 5 }$ , and $f ^ { i }$ denotes the $i$ th iteration of a certain fixed permutation. Verhoeff’s method finds all single errors in a string, and all adjacent transpositions. It also finds about $9 5 \%$ of twin errors $( a a  b b$ ), jump transpositions $( a c b  b c a$ ), and jump twin errors $( a c a  b c b$ ). Here is an implementation:

# decchk.h

# Bool decchk(string str, char &ch) {

Decimal check digit computation or verification. Returns as ch a check digit for appending to string[0..n-1], that is, for storing into string[n]. In this mode, ignore the returned boolean value. If string[0..n-1] already ends with a check digit (string[n-1]), returns the function value true if the check digit is valid, otherwise false. In this mode, ignore the returned value of ch. Note that string and ch contain ASCII characters corresponding to the digits 0-9, not byte values in that range. Other ASCII characters are allowed in string, and are ignored in calculating the check digit.

char c;

Int j, $\mathtt { k } = 0$ , $\mathtt { m } = 0$ , $\mathbf { n } =$ str.length();   
static Int ip[10][8] $=$ {{0,1,5,8,9,4,2,7},{1,5,8,9,4,2,7,0}, {2,7,0,1,5,8,9,4},{3,6,3,6,3,6,3,6},{4,2,7,0,1,5,8,9}, {5,8,9,4,2,7,0,1},{6,3,6,3,6,3,6,3},{7,0,1,5,8,9,4,2}, {8,9,4,2,7,0,1,5},{9,4,2,7,0,1,5,8}};   
static Int ij[10][10] $=$ {{0,1,2,3,4,5,6,7,8,9},{1,2,3,4,0,6,7,8,9,5}, {2,3,4,0,1,7,8,9,5,6},{3,4,0,1,2,8,9,5,6,7},{4,0,1,2,3,9,5,6,7,8}, {5,9,8,7,6,0,4,3,2,1},{6,5,9,8,7,1,0,4,3,2},{7,6,5,9,8,2,1,0,4,3}, {8,7,6,5,9,3,2,1,0,4},{9,8,7,6,5,4,3,2,1,0}}; Group multiplication and permutation tables.   
for (j=0;j<n;j++) { Look at successive characters. c=str[j]; if (c >= 48 && $\mathrm { ~ c ~ } < = \ 5 7 .$ ) Ignore everything except digits. k=ij[k][ip[(c+2) % 10][7 & m++]];   
}   
for (j=0;j<10;j++) Find which appended digit will check proper if (ij[k][ip[j][m & 7]] $\scriptstyle = = 0$ ) break;   
ch=char $( \mathrm { j + 4 8 } )$ ; Convert to ASCII.   
return $\mathtt { k } = = 0$ ;

# CITED REFERENCES AND FURTHER READING:

Saadawi, T.N., and Ammar, M.H. 1994, Fundamentals of Telecommunication Networks (New York: Wiley).[1]   
LeVan, J. 1987, “A Fast CRC,” Byte, vol. 12, pp. 339–341 (November).[2]   
Koopman, P., and Chakravarty, T. 2004, “Cyclic Redundancy Code (CRC) Polynomial Selection for Embedded Networks,” in International Conference on Dependable Systems and Networks (DSN-2004) (IEEE Computer Society).[3]   
Sarwate, D.V. 1988, “Computation of Cyclic Redundancy Checks via Table Look-Up,” Communications of the ACM,vol.31,pp.1008-1013.[4]   
Griffiths, G., and Stones, G.C. 1987, “The Tea-Leaf Reader Algorithm: An Efficient Implementation of CRC-16 and CRC-32,” Communications of the ACM, vol. 30, pp. 617–620.[5]   
Wagner, N.R., and Putter, P.S. 1989, “Error Detecting Decimal Digits,” Communications of the ACM, vol. 32,pp. 106-110.[6]

# 22.5 Huffman Coding and Compression of Data

A lossless data compression algorithm takes a string of symbols (typically ASCII characters or bytes) and translates it reversibly into another string, one that is on the average of shorter length. The words “on the average” are crucial; it is obvious that no reversible algorithm can make all strings shorter — there just aren’t enough short strings to be in one-to-one correspondence with longer strings. Compression algorithms are possible only when, on the input side, some strings, or some input symbols, are more common than others. These can then be encoded in fewer bits than rarer input strings or symbols, giving a net average gain. We already quantified this idea, with the concept of entropy, in $\ S 1 4 . 7$ .

There exist many, quite different, compression techniques, corresponding to different ways of detecting and using departures from equiprobability in input strings.

In this section and the next we shall consider only variable length codes with defined word inputs. In these, the input is sliced into fixed units, for example ASCII characters, while the corresponding output comes in chunks of variable size. The simplest such method is Huffman coding [1], discussed in this section. Another example, arithmetic compression, is discussed in $\ S 2 2 . 6$ .

At the opposite extreme from defined-word, variable length codes are schemes that divide up the input into units of variable length (words or phrases of English text, for example) and then transmit these, often with a fixed length output code. The most widely used code of this general type is the Ziv-Lempel code [2]. References [3-5] give the flavor of some other compression techniques, with references to the large literature.

The idea behind Huffman coding is simply to use shorter bit patterns for more common characters. Suppose the input alphabet has $N _ { \mathrm { c h } }$ characters, and that these occur in the input string with respective probabilities $p _ { i } , i \ = \ 1 , . . . , N _ { \mathrm { c h } }$ , so that $\sum p _ { i } \ = \ 1$ . As we saw in $\ S 1 4 . 7$ , strings consisting of independently random sequences of these characters (a conservative, but not always realistic assumption) require, on the average, at least

$$
H = - \sum p _ { i } \log _ { 2 } p _ { i }
$$

bits per character, where $H$ is the entropy of the probability distribution. Moreover, coding schemes exist that approach the bound arbitrarily closely. For the case of equiprobable characters, with all $p _ { i } = 1 / N _ { \mathrm { c h } }$ , one easily sees that $H = \log _ { 2 } N _ { \mathrm { c h } }$ , which is the case of no compression at all. Any other set of $p _ { i }$ ’s gives a smaller entropy, allowing some useful compression.

Notice that the bound of (22.5.1) would be achieved if we could encode character $i$ with a code of length $L _ { i } = - \log _ { 2 } p _ { i }$ bits: Equation (22.5.1) would then be the average $\sum p _ { i } L _ { i }$ . The trouble with such a scheme is that $- \log _ { 2 } { p _ { i } }$ is not generally an integer. How can we encode the letter “Q” in 5.32 bits? Huffman coding makes a stab at this by, in effect, approximating all the probabilities $p _ { i }$ by integer powers of $1 / 2$ , so that all the $L _ { i }$ ’s are integral. If all the $p _ { i }$ ’s are in fact of this form, then a Huffman code does achieve the entropy bound $H$ .

The construction of a Huffman code is best illustrated by example. Imagine a language, Vowellish, with the $N _ { \mathrm { c h } } ~ = ~ 5$ character alphabet A, E, I, O, and U, occurring with the respective probabilities 0.12, 0.42, 0.09, 0.30, and 0.07. Then the construction of a Huffman code for Vowellish is accomplished in the table on the next page.

Here is how it works, proceeding in sequence through $N _ { \mathrm { c h } }$ stages, represented by the columns of the table. The first stage starts with $N _ { \mathrm { c h } }$ nodes, one for each letter of the alphabet, containing their respective relative frequencies. At each stage, the two smallest probabilities are found, summed to make a new node, and then dropped from the list of active nodes. (A “block” denotes the stage where a node is dropped.) All active nodes (including the new composite) are then carried over to the next stage (column). In the table, the names assigned to new nodes (e.g., AUI) are inconsequential. In the example shown, it happens that (after stage 1) the two smallest nodes are always an original node and a composite one; this need not be true in general: The two smallest probabilities might be both original nodes, or both composites, or one of each. At the last stage, all nodes will have been collected into one grand composite of total probability 1.

<table><tr><td>Node</td><td>Stage:</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1</td><td>A:</td><td>0.12</td><td>0.12</td><td></td><td></td><td></td></tr><tr><td>2</td><td>E:</td><td>0.42</td><td>0.42</td><td>0.42</td><td>0.42</td><td></td></tr><tr><td>3</td><td>I:</td><td>0.09</td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>0:</td><td>0.30</td><td>0.30</td><td>0.30</td><td></td><td></td></tr><tr><td>5</td><td>U:</td><td>0.07</td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td></td><td>UI:</td><td>0.16</td><td></td><td></td><td></td></tr><tr><td>7</td><td></td><td></td><td>AUI:</td><td>0.28</td><td></td><td></td></tr><tr><td>8</td><td></td><td></td><td></td><td>AUIO:</td><td>0.58</td><td></td></tr><tr><td>9</td><td></td><td></td><td></td><td></td><td>EAUIO:</td><td>1.00</td></tr></table>

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0018_pages_1191-1260/auto/images/c0078414d512bc5f40346193df5316b60d06ed347e4db346cd96dd18b2e7850f.jpg)  
Figure 22.5.1. Huffman code for the fictitious language Vowellish, in tree form. A letter (A, E, I, O, or U) is encoded or decoded by traversing the tree from the top down; the code is the sequence of 0’s and 1’s on the branches. The value to the right of each node is its probability; to the left, its node number in the table.

Now, to see the code, you redraw the data in the table as a tree (Figure 22.5.1). As shown, each node of the tree corresponds to a node (row) in the table, indicated by the integer to its left and probability value to its right. Terminal nodes, so called, are shown as circles; these are single alphabetic characters. The branches of the tree are labeled 0 and 1. The code for a character is the sequence of zeros and ones that lead to it, from the top down. For example, E is simply 0, while U is 1010.

Any string of zeros and ones can now be decoded into an alphabetic sequence. Consider, for example, the string 1011111010. Starting at the top of the tree we descend through 1011 to I, the first character. Since we have reached a terminal node, we reset to the top of the tree, next descending through 11 to O. Finally 1010 gives U. The string thus decodes to IOU.

These ideas are embodied in the following Huffcode object. The constructor lets you specify $N _ { \mathrm { c h } }$ , and an integer frequency-of-occurrence table of length $N _ { \mathrm { c h } }$ telling how often each character occurs in some large corpus of text. These integers are, of course, proportional to the $p _ { i }$ ’s. The reason for using integers is so that any two computers will produce exactly the same code from the same input data. This might not be true if we used floating-point values. The constructor utilizes a heap structure (see $\ S 8 . 3 )$ for efficiency; for a detailed description, see Sedgewick [6].

Once you have created an instance of Huffcode, you code a message by calling codeone for each message character in turn. This writes bits into a byte array code that you supply as an argument. There is no message-dependent saved state, so you could interleave different messages if there were some reason to do so.

Decoding a Huffman-encoded message is slightly more complicated. The coding tree must be traversed from the top down, using up a variable number of bits. This is done by the method decodeone.

There is no such thing as an “end of message” (EOM) marker in Huffman codes not unless you provide one. Successive calls to decodeone will happily decode bits into characters until your hardware traps an illegal memory read! That is because every path on the tree (cf. Figure 22.5.1) terminates in a valid character. In practice, one increases $N _ { \mathrm { c h } }$ by 1, and gives the extra character a frequency of occurrence of 1 (versus large values for the other characters). The new character becomes the EOM marker. Similarly, one can add other extra characters for other “out-of-band” signaling. If these occur rarely, the overhead on the message is negligible.

# struct Huffcode {

Object for Huffman encoding and decoding.

Int nch,nodemax,mq;   
Int ilong,nlong;   
VecInt ncod,left,right;   
VecUint icod;   
Uint setbit[32];

Huffcode(const Int nnch, VecInt_I &nfreq) : nch(nnch), mq(2\*nch-1), icod(mq), ncod(mq), left(mq), right(mq) { Constructor. Given the frequency of occurrence table nfreq[0..nnch-1] for nnch characters, constructs the Huffman code. Also sets ilong and nlong as the character number that produced the longest code symbol, and the length of that symbol.

Int ibit,j,node,k,n,nused;   
VecInt index(mq), nprob(mq), up(mq);   
for ( $\scriptstyle \mathrm { i = 0 }$ ;j<32;j++) setbit[j] $= \ 1 \ < <$ j;   
for (nused ${ = } 0$ , $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<nch;j $^ { + + }$ ) { nprob[j] $=$ nfreq[j]; icod[j]=ncod[j] ${ = } 0$ ; if (nfreq[j] $! = ~ 0 ^ { \prime }$ ) index[nused++]=j;   
}   
for (j=nused-1;j> ${ = } 0$ ;j--) Sort nprob into a heap structure in index. heep(index,nprob,nused,j);   
$\mathtt { k } =$ nch;   
while (nused $> ~ 1$ ) { Combine heap nodes, remaking the heap at node $=$ index[0]; each stage. index[0] $=$ index[(nused--)-1]; heep(index,nprob,nused,0); nprob[k] $=$ nprob[index[0]]+nprob[node]; left[k] $=$ node; Store left and right children of a node. right[k++] $=$ index[0]; up[index[0]] $=$ -Int(k); Indicate whether a node is a left or right index[0]=k-1; of its parent. up[node] ${ \tt = } \tt k$ ; heep(index,nprob,nused,0);   
up[(nodemax $\scriptstyle = \mathbf { k }$ )-1] ${ = } 0$ ;   
for ( $\scriptstyle \mathbf { j } = 0$ ;j<nch; $\mid + +$ ) { Make the Huffman code from the tree. if (nprob[j] $! = ~ 0 ^ { \cdot }$ ) { for ( $\scriptstyle \mathtt { n } = 0$ ,ibit ${ = } 0$ ,node $=$ up[j];node;node=up[node-1],ibit++) { if (node $\mathit { \Theta } < \mathit { \Theta } 0 \mathit { \Theta }$ ) { n $| =$ setbit[ibit]; node $=$ -node; } } icod[j] $= \mathbf { n }$ ; ncod[j] $=$ ibit; }   
}   
nlong $_ { = 0 }$ ;   
for (j=0;j<nch;j++) { if (ncod[j] $>$ nlong) nlong=ncod[j]; ilong=j; }   
}   
if (nlong $>$ numeric_limits<Uint>::digits) throw("Code too long in Huffcode. See text.");

void codeone(const Int ich, char \*code, Int &nb) {

Huffman encode the single character ich (in the range 0..nch-1), write the result to the byte array code starting at bit nb (whose smallest valid value is zero), and increment nb to the first unused bit. This routine is called repeatedly to encode consecutive characters in a message. The user is responsible for monitoring that the value of nb does not overrun the length of code.

Int m,n,nc; if (ich $> =$ nch) throw("bad ich (out of range) in Huffcode"); if (ncod[ich] $\scriptstyle = = 0$ ) throw("bad ich (zero prob) in Huffcode"); for ( $\mathtt { n } =$ ncod[ich]-1;n >= 0;n--,++nb) { Loop over the bits in the stored nc=nb $\ b > 3$ ; Huffman code for ich. m=nb & 7; if $\mathbf { \Omega } _ { \mathrm { ~ m ~ } } = = \mathbf { \Omega } 0$ ) code[nc] ${ = } 0$ ; Set appropriate bits in code. if ((icod[ich] & setbit[n]) $! = ~ 0 ^ { \prime }$ ) code[nc] $| =$ setbit[m]; } }

# Int decodeone(char \*code, Int &nb) {

Starting at bit number nb in the byte array code, decode a single character (returned as ich in the range 0..nch-1) and increment nb appropriately. Repeated calls, starting with $\mathtt { n b } = 0$ , will return successive characters in a compressed message. The user is responsible for detecting EOM from the message content.

Int nc;   
Int node=nodemax-1;   
for (;;) { Set node to the top of the decoding tree, and nc=nb >> 3; loop until a valid character is obtained. node $=$ ((code[nc] & setbit[7 & nb++]) $\smash { ! = \begin{array} { l l } { 0 } & { ? } \end{array} }$ right[node] : left[node]); Branch left or right in tree, depending on its value. if (node $<$ nch) return node; If we reach a terminal node, we have a com-  
} plete character and can return.

void heep(VecInt_IO &index, VecInt_IO &nprob, const Int n, const Int m) { Used by the constructor to maintain a heap structure in the array index[0..m-1].

Int $\dot { \mathtt { 1 } } = \mathtt { m }$ ,j,k;$\mathtt { k } =$ index[i];while (i < $\mathrm { ~ ( ~ n ~ } > > \ 1 )$ ) {if $( ( \ j \ = \ 2 * \ i + 1 ) \ < \ \mathtt { n } - 1$ && nprob[index[j]] $>$ nprob[index[j+1]]) j++;if (nprob[k] $< =$ nprob[index[j]]) break;index[i] $=$ index[j];i=j;}index[i] ${ \tt = } \tt k$ ;}};

Huffcode requires that the longest code for a single character fits into your machine’s integer wordlength (typically 32 bits), and will tell you if this is violated. If this happens, you’ll need to increase the frequency-of-occurrence value for the rarest characters. This will affect your compression hardly at all.

It is a feature, not a bug, that Huffcode allows you to specify some characters as having zero frequency of occurrence, and then completely omits these from the code. This can be very useful when, for example, you want to compress a file consisting only of ASCII characters $0 { - } 9 , + , - ,$ , and “.”, as might occur in a file of numerical values. But don’t then try to encode one of the omitted characters!

# 22.5.1 Run-Length Encoding

For the compression of highly correlated bit streams (for example the black or white values along a facsimile scan line), Huffman compression is often combined with run-length encoding: Instead of sending each bit, the input stream is converted to a series of integers indicating how many consecutive bits have the same value. These integers are then Huffman-compressed. The Group 3 CCITT facsimile standard functions in this manner, with a fixed, immutable, Huffman code, optimized for a set of eight standard documents [7].

# CITED REFERENCES AND FURTHER READING:

Hamming, R.W. 1980, Coding and Information Theory (Englewood Cliffs, NJ: Prentice-Hall).   
Huffman, D.A. 1952, “A Method for the Construction of Minimum-Redundancy Codes,” Proceedings of the Institute of Radio Engineers,vol.40,pp.1098-1101.[1]   
Ziv, J., and Lempel, A. 1978, “Compression of Individual Sequences via Variable-Rate Coding,” IEEE Transactions on Information Theory,vol. IT-24,pp.530-536.[2]   
Sayood, K. 2005, Introduction to Data Compression, 3rd ed. (San Francisco: Morgan Kaufmann).[3]   
Salomon, D. 2004, Data Compression: The Complete Reference, 3rd ed. (New York: Springer).[4]   
Wayner, P. 1999, Compression Algorithms for Real Programmers (San Francisco: Morgan Kaufmann).[5]   
Sedgewick, R. 1998, Algorithms in C, 3rd ed. (Reading, MA: Addison-Wesley), Chapter 22.[6]   
Hunter, R., and Robinson, A.H. 1980, “International Digital Facsimile Coding Standard,” Proceedings of the IEEE,vol. 68, pp.854-867.[7]

# 22.6 Arithmetic Coding

We saw in the previous section, as well as $\ S 1 4 . 7$ , that a perfect coding scheme would use $L _ { i } = - \log _ { 2 } p _ { i }$ bits to encode character $i$ (in the range $1 \leq i \leq N _ { \mathrm { c h } } )$ , if $p _ { i }$ is its probability of occurrence and characters occur independently randomly. Huffman coding gives a way of rounding the $L _ { i }$ ’s to close integer values and constructing a code with those lengths. Arithmetic coding [1], which we now discuss, actually does manage to encode characters using noninteger numbers of bits! It also provides a convenient way to output the result not as a stream of bits, but as a stream of symbols in any desired radix. This latter property is particularly useful if you want, e.g., to convert data from bytes (radix 256) to printable ASCII characters (radix 94), or to case-independent alphanumeric sequences containing only A-Z and 0-9 (radix 36).

In arithmetic coding, an input message of any length is represented as a real number $R$ in the range $0 \leq R < 1$ . The longer the message, the more precision required of $R$ . This is best illustrated by an example, so let us return to the fictitious language, Vowellish, of the previous section. Recall that Vowellish has a five-character alphabet (A, E, I, O, U), with occurrence probabilities 0.12, 0.42, 0.09, 0.30, and 0.07, respectively. Figure 22.6.1 shows how a message beginning “IOU” is encoded: The interval $[ 0 , 1 )$ is divided into segments corresponding to the five alphabetical characters; the length of a segment is the corresponding $p _ { i }$ . We see that the first message character, “I”, narrows the range of $R$ to $0 . 3 7 \leq R < 0 . 4 6$ . This interval is now subdivided into five subintervals, again with lengths proportional to the $p _ { i }$ ’s. The second message character, “O”, narrows the range of $R$ to $0 . 3 7 6 3 \le R < 0 . 4 0 3 3$ . The “U” character further narrows the range to $0 . 3 7 6 3 0 \leq R < 0 . 3 7 8 1 9$ Any value of $R$ in this range can be sent as encoding “IOU”. In particular, the binary fraction :011000001 is in this range, so “IOU” can be sent in 9 bits. (Huffman coding took 10 bits for this example; see $\ S 2 2 . 5 . \ O$ )

Of course there is the problem of knowing when to stop decoding. The fraction :011000001 represents not simply “IOU,” but “IOU. . . ,” where the ellipses represent an infinite string of successor characters. We had a similar problem in Huffman coding, but there we would at least stop when we ran off the edge of the input buffer. Here, the real number :011000001 actually does represent an infinite message! Arithmetic coding therefore always must assume the existence of a special $N _ { \mathrm { c h } } + 1 \mathrm { s t }$ character, EOM (end of message), which occurs only once at the end of the input. Since EOM has a low probability of occurrence, it gets allocated only a very tiny piece of the number line.

In the above example, we gave $R$ as a binary fraction. We could just as well have output it in any other radix, e.g., base 94 or base 36, whatever is convenient for the anticipated storage or communication channel.

You might wonder how one deals with the seemingly incredible precision required of $R$ for a long message. The answer is that $R$ is never actually represented all at once. At any give stage we have upper and lower bounds for $R$ represented as a finite number of digits in the output radix. As digits of the upper and lower bounds become identical, we can left-shift them away and bring in new digits at the lowsignificance end. The object below has a parameter NWK for the number of working digits to keep around. This must be large enough to make the chance of an accidental degeneracy vanishingly small. (The object signals if a degeneracy ever occurs.)

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0018_pages_1191-1260/auto/images/21c608b485877440122b9bf1303442a638514f9a9b493f9cc914f619a66d5d64.jpg)  
Figure 22.6.1. Arithmetic coding of the message “IOU...” in the fictitious language Vowellish. Successive characters give successively finer subdivisions of the initial interval between 0 and 1. The final value can be output as the digits of a fraction in any desired radix. Note how the subinterval allocated to a character is proportional to its probability of occurrence.

Since the process of discarding old digits and bringing in new ones is performed identically on encoding and decoding, everything stays synchronized.

In the Arithcode object below, the constructor has arguments to specify the number of characters and an integer frequency-of-occurrence table (as in Huffcode), plus an argument that allows you to specify an output radix for the code. Because there is some saved state between coding successive characters (the upper and lower bounds for $R$ , for example), you must call messageinit prior to encoding or decoding the first character of a new message, and not interleave the encoding of different messages in a single instance of Arithcode. If you want to interleave messages, create more than one instance.

Successive calls to codeone for each input character encode the message. A final call with character nch (that is, one larger than your specified character set) adds the EOM marker and is mandatory. After this final call, lcd will be set to the number of bytes in the coded message (i.e., will point to the first unused location in code). The decodeone routine similarly returns successive characters of the decoded message in turn, with nch returned to indicate EOM.

Unlike the Huffcode object, Arithcode has no provision for omitting specified message characters from the code. Therefore, it also refuses to believe zero values in the table nfreq; a 0 is treated as if it were a 1. If you want to live dangerously, with a very slightly more efficient coding, you can change this in the constructor.

# struct Arithcode {

Object for arithmetic coding.

Int nch,nrad,ncum;   
Uint jdif,nc,minint;   
VecUint ilob,iupb;   
VecInt ncumfq;   
static const Int NWK $:$ 20;

Arithcode(VecInt_I &nfreq, const Int nnch, const Int nnrad) : nch(nnch), nrad(nnrad), ilob(NWK), iupb(NWK), ncumfq(nch+2) { Constructor. Given the frequency of occurrence table nfreq[0..nnch-1] for nnch characters, constructs the Huffman code whose output has radix nnrad (which must be $\leq 2 5 6$ ).

# Int j;

if (nrad $>$ 256) throw("output radix must be $< =$ 256 in Arithcode");   
minint $=$ numeric_limits<Uint>::max()/nrad;   
ncumfq $[ 0 ] = 0$ ;   
for ( $\scriptstyle { \dot { \mathbf { J } } } = 1$ ;j<=nch;j++) ncumfq[j] $=$ ncumfq[j-1]+MAX(nfreq[j-1],1);   
ncum ncumfq[nch $^ +$ 1] $=$ ncumfq[nch] $+ 1$ ;

# void messageinit() {

Clear saved state for a new message (either encode or decode). This is mandatory before encoding or decoding the first character.

Int j;   
jdif=nrad-1;   
for (j=NWK-1;j> ${ \tt > } = 0$ ;j--) { Initialize enough digits of the upper and lower iupb[j] $=$ nrad-1; bounds. ilob[j]=0; nc=j; if (jdif $>$ minint) return; Initialization complete. jdif ${ } = { }$ (jdif+1)\*nrad-1;   
}   
throw("NWK too small in arcode.");

oid codeone(const Int ich, char \*code, Int &lcd) {

Encode the single character ich in the range 0 : : : nch-1 into the byte array code, starting at location code[lcd] and (if necessary) incrementing lcd so that, on return, it points to the first unused byte in code. A final call with ich $\cdot ^ { = }$ nch encodes “end of message.” Byte values written into code will be in the range 0 : : : nrad  1.

if (ich $>$ nch) throw("bad ich in Arithcode");   
advance(ich,code,lcd,1);

Check for valid input character.

# }

# Int decodeone(char \*code, Int &lcd) {

Decode and return a single message character, using code starting at location code[lcd], and (if necessary) increment lcd appropriately. Successive calls return successive message characters. The returned value nch indicates end of message (subsequent calls will return nonsense).

Int ich;   
Uint j,ihi,ja,m;   
$\mathtt { j a } =$ (Uchar) code[lcd]-ilob[nc];   
for (j=nc+1;j<NWK;j++) { ja $\ast =$ nrad; ja $+ =$ Uchar(code[lcd+j-nc])-ilob[j];   
}   
ihi=nch+1;   
ich $_ { = 0 }$ ;   
while (ihi-ich $>$ 1) { If decoding, locate the character ich by bisection.

$\mathbb { m } =$ (ich+ihi)>>1; if (ja $> =$ multdiv(jdif,ncumfq[m],ncum)) ich=m; else ihi $= \mathtt { m }$ ; } if (ich $\ ! =$ nch) advance(ich,code,lcd,-1); return ich; }

void advance(const Int ich, char \*code, Int &lcd, const Int isign) { Used internally. Operations common to encoding and decoding. Convert character ich to a new subrange [ilob,iupb).

Uint j,k,jh,jl;   
jh=multdiv(jdif,ncumfq[ich+1],ncum);   
jl=multdiv(jdif,ncumfq[ich],ncum);   
jdif=jh-jl;   
arrsum(ilob,iupb,jh,NWK,nrad,nc);   
arrsum(ilob,ilob,jl,NWK,nrad,nc);   
for (j=nc;j<NWK;j++) { How many leading digits to output (if enif (ich $\ ! =$ nch && iupb[j] $\ ! =$ ilob[j]) break; coding) or skip over? if (isign $> 0 \dot { . }$ ) code[lcd] $=$ ilob[j]; lcd++;   
}   
if (j+1 $>$ NWK) return; Ran out of message. Did someone forget to   
nc=j; encode a terminating ncd?   
for(j=0;jdif<minint;j++) How many digits to shift? jdif $\ast =$ nrad;   
if (j $>$ nc) throw("NWK too small in arcode.");   
if (j $! = ~ 0 ^ { \prime }$ ) Shift them. for (k=nc;k<NWK;k++) { iupb[k-j] $=$ iupb[k]; ilob[k-j] $=$ ilob[k]; }   
nc $\mathrm { ~ -- ~ } \mathrm { ~ j ~ }$ ;   
for ( $\mathbf { k } =$ NWK-j;k<NWK;k++) iupb[k] $=$ ilob[k]=0;   
return; Normal return.

inline Uint multdiv(const Uint j, const Uint k, const Uint m) { Calculate $( \mathtt { k } { * } \mathtt { j } ) / \mathtt { m }$ without overflow by use of double-length integers. return Uint((Ullong(j)\*Ullong(k)/Ullong(m))); }

void arrsum(VecUint_I &iin, VecUint_O &iout, Uint ja,   
const Int nwk, const Uint nrad, const Uint nc) {   
Add the integer ja to the radix nrad multiple-precision integer iin[nc..nwk-1]. Return the result in iout[nc..nwk-1].

Uint karry ${ = } 0$ ,j,jtmp; for (j=nwk-1;j>nc;j--) { jtmp=ja; ja /= nrad; iout[j]=iin[j]+(jtmp-ja\*nrad)+karry; if (iout[j] $> =$ nrad) { iout[j] $- =$ nrad; karry=1; } else karry ${ \tt = } 0$ ; iout[nc]=iin[nc]+ja+karry; };

A few further notes: When an interval of size jdif is to be partitioned in the proportions of some n to some ntot, say, then we must compute (n\*jdif)/ntot.

With ordinary integer arithmetic, the numerator is likely to overflow; and, unfortunately, an expression like jdif/(ntot/n) is not equivalent. We therefore need to use double-length integers, type Ullong, usually 64 bits, just for this operation.

The internally set variable minint, which is the minimum allowed number of discrete steps between the upper and lower bounds, determines when new lowsignificance digits are added. minint must be large enough to provide resolution of all the input characters. That is, we must have $p _ { i } \ \times \mathrm { m i n i n t } \ > \ 1$ for all $i$ . A value of $1 0 0 N _ { \mathrm { c h } }$ , or $1 . 1 / \operatorname* { m i n } p _ { i }$ , whichever is larger, is generally adequate. However, for safety, the routine takes minint to be as large as possible, with the product minint\*nradd just smaller than overflow. This results in some time inefficiency, and in a few unnecessary characters being output at the end of a message. You can decrease minint if you want to live closer to the edge.

If radix-changing, rather than compression, is your primary aim (for example to convert an arbitrary file into printable characters), then you are of course free to set all the components of nfreq equal, say, to 1.

While the output radix is limited to 256 (so that values fit into a byte), the input alphabet size $N _ { \mathrm { c h } } =$ nch can be less than, equal to, or greater than 256.

# CITED REFERENCES AND FURTHER READING:

Sayood, K. 2005, Introduction to Data Compression, 3rd ed. (San Francisco: Morgan Kaufmann).   
Salomon, D. 2004, Data Compression: The Complete Reference, 3rd ed. (New York: Springer).   
Wayner, P. 1999, Compression Algorithms for Real Programmers (San Francisco: Morgan Kaufmann).   
Witten, I.H., Neal, R.M., and Cleary, J.G. 1987, “Arithmetic Coding for Data Compression,” Communications of the ACM,vol.30,pp. 520-540.[1]

# 22.7 Arithmetic at Arbitrary Precision

Let’s compute the number $\pi$ to a couple of thousand decimal places. In doing so, we’ll learn some things about multiple precision arithmetic on computers and meet quite an unusual application of the fast Fourier transform (FFT). We’ll also develop a set of routines that you can use for other calculations at any desired level of arithmetic precision.

To start with, we need an analytic algorithm for $\pi$ . Useful algorithms are quadratically convergent, i.e., they double the number of significant digits at each iteration. Quadratically convergent algorithms for $\pi$ are based on the AGM (arithmetic geometric mean) method, which also finds application to the calculation of elliptic integrals (cf. $\ S 6 . 1 2 )$ and in advanced implementations of the ADI method for elliptic partial differential equations (-20.5). Borwein and Borwein [1] treat this subject, which is beyond our scope here. One of their algorithms for $\pi$ starts with the initializations

$$
\begin{array} { l } { { X _ { 0 } = \sqrt { 2 } } } \\ { { \pi _ { 0 } = 2 + \sqrt { 2 } } } \\ { { { Y _ { 0 } = \sqrt [ 4 ] { 2 } } } } \end{array}
$$

and then, for $i = 0 , 1 , \ldots$ , repeats the iteration

$$
\begin{array} { l c r } { \displaystyle { X _ { i + 1 } = \frac { 1 } { 2 } \left( \sqrt { X _ { i } } + \frac { 1 } { \sqrt { X _ { i } } } \right) } } \\ { \displaystyle { \pi _ { i + 1 } = \pi _ { i } \left( \frac { X _ { i + 1 } + 1 } { Y _ { i } + 1 } \right) } } \\ { \displaystyle { Y _ { i + 1 } = \frac { Y _ { i } \sqrt { X _ { i + 1 } } + \frac { 1 } { \sqrt { X _ { i + 1 } } } } { Y _ { i } + 1 } } } \end{array}
$$

The value $\pi$ emerges as the limit $\pi _ { \infty }$

Now to the question of how to do arithmetic to arbitrary precision: In a highlevel language like $\mathrm { C } { + + }$ , a natural choice is to work in radix (base) 256, so that character arrays can be directly interpreted as strings of digits. At the very end of our calculation, we will want to convert our answer to radix 10, but that is essentially a frill for the benefit of human ears, accustomed to the familiar chant, “three point one four one five nine. . . .” For any less frivolous calculation, we would likely never leave base 256 (or the thence trivially reachable hexadecimal, octal, or binary bases).

We will adopt the convention of storing digit strings in the “human” ordering, that is, with the first stored digit in an array being most significant, the last stored digit being least significant. The opposite convention would, of course, also be possible. “Carries,” where we need to partition a number larger than 255 into a low-order byte and a high-order carry, present a minor programming annoyance, solved, in the routines below, by the use of the functions lobyte and hibyte. It will be our usual convention to assume that the digit strings represent floating-point numbers with the radix point falling after the the first digit. When an operation results in a number that requires more digits in front of the decimal point, it is the responsibility of the user to shift the digits to the right and keep track of any excess factors of 256 that this implies.

It is easy at this point, following Knuth [2], to write a routines for the “fast” arithmetic operations: short addition (adding a single byte to a string), addition, subtraction, short multiplication (multiplying a string by a single byte), short division, ones-complement negation, and a couple of utility operations, copying and left-shifting strings. These are implemented in the following MParith object. The additional routines that are declared, but not defined, are discussed below.

# struct MParith {

Multiple precision arithmetic operations done on character strings, interpreted as radix 256 numbers with the radix point after the first digit. Implementations for the simpler operations are listed here.

void mpadd(VecUchar_O &w, VecUchar_I &u, VecUchar_I &v) {

Adds the unsigned radix 256 numbers u and v, yielding the unsigned result w. To achieve the full available accuracy, the array w must be longer, by one element, than the shorter of the two arrays u and v.

Int j, $\mathbf { n } { = } \mathbf { u }$ .size(), $\mathtt { m } = \mathtt { v }$ .size(), $\mathtt { p - w }$ .size();   
Int n_min $\ c =$ MIN(n,m),p_min $\boldsymbol { \cdot }$ MIN(n_min,p-1);   
Uint ireg ${ \left. \sum 0 \right. }$ ;   
for (j=p_min-1;j>=0;j--) { ireg=u[j]+v[j]+hibyte(ireg); w[j+1]=lobyte(ireg);   
}   
w[0]=hibyte(ireg);   
if (p > p_min $+ 1$ )

for (j=p_min+1;j<p;j++) w[j] ${ = } 0$ ;

# }

void mpsub(Int &is, VecUchar_O &w, VecUchar_I &u, VecUchar_I &v) {

Subtracts the unsigned radix 256 number v from u yielding the unsigned result w. If the result is negative (wraps around), is is returned as $^ { - 1 }$ ; otherwise it is returned as 0. To achieve the full available accuracy, the array $\mathtt { w }$ must be as long as the shorter of the two arrays u and v.

Int j, $\mathbf { n } { = } \mathbf { u }$ .size(), $\mathrm { m } { = } \mathrm { v }$ .size(), $\mathtt { p - w }$ .size();   
Int n_min $\ c =$ MIN(n,m),p_min $\downharpoonleft$ MIN(n_min,p-1);   
Uint ireg=256;   
for (j=p_min-1;j>=0;j--) { ireg=255+u[j]-v[j]+hibyte(ireg); w[j] $=$ lobyte(ireg);   
}   
is=hibyte(ireg)-1;   
if (p > p_min) for (j=p_min;j<p;j++) w[j] ${ = } 0$ ;

oid mpsad(VecUchar_O &w, VecUchar_I &u, const Int iv) {

Short addition: The integer iv (in the range $\begin{array} { r } { 0 \leq \mathrm { i v } \leq 2 5 5 } \end{array}$ ) is added to the least significant radix position of unsigned radix 256 number u, yielding result $\mathtt { w }$ . To ensure that the result does not require two digits before the radix point, one may first right-shift the operand u so that the first digit is 0, and keep track of multiples of 256 separately.

Int j, $\mathbf { n } { = } \mathbf { u }$ .size(), $\mathtt { p - w }$ .size();   
Uint ireg=256\*iv;   
for (j=n-1; $\scriptstyle { \dot { \mathsf { J } } } > = 0$ ;j--) { ireg=u[j]+hibyte(ireg); if (j+1 < p) w[j+1] $=$ lobyte(ireg);   
}   
w[0]=hibyte(ireg);   
for ( $\scriptstyle { \dot { \mathsf { J } } } = { \mathsf { n } } + 1$ ;j<p;j $^ { + + }$ ) w[j] ${ = } 0$ ;

void mpsmu(VecUchar_O &w, VecUchar_I &u, const Int iv) {

Short multiplication: The unsigned radix 256 number u is multiplied by the integer iv (in the range $\begin{array} { r } { 0 \leq \mathtt { i v } \leq 2 5 5 , } \end{array}$ ), yielding result w. To ensure that the result does not require two digits before the radix point, one may first right-shift the operand u so that the first digit is 0, and keep track of multiples of 256 separately.

Int j, $\mathbf { n } { = } \mathbf { u }$ .size(), $\mathtt { p - w }$ .size();   
Uint ireg=0;   
for $\scriptstyle \ j = \mathtt { n } - 1$ ; $\scriptstyle { \dot { \mathcal { I } } } > = 0$ ;j--) { ireg=u[j]\*iv+hibyte(ireg); if (j < p-1) w[j+1] $=$ lobyte(ireg);   
  
w[0] $=$ hibyte(ireg);   
for ( $\scriptstyle { \dot { \mathbf { J } } } = { \mathbf { n } } + 1$ ;j<p;j++) w[j] ${ = } 0$ ;

void mpsdv(VecUchar_O &w, VecUchar_I &u, const Int iv, Int &ir) {

Short division: The unsigned radix 256 number u is divided by the integer iv (in the range $\mathbf { 0 } \leq \mathrm { i v } \leq 2 5 5$ ), yielding a quotient w and a remainder ir (with ${ \mathbf { 0 } } \leq \mathrm { i } { \mathbf { r } } \leq 2 5 5$ ). To achieve the full available accuracy, the array w must be as long as the array u.

Int i,j, $\mathbf { n } { = } \mathbf { u }$ .size(), $\mathtt { p - w }$ .size(),p_min=MIN(n,p);   
$\scriptstyle { \dot { \mathtt { 1 } } } \mathbf { r } = 0$ ;   
for (j=0;j<p_min;j $^ { + + }$ ) { i=256\*ir+u[j]; w[j]=Uchar(i/iv); ir=i % iv;   
}   
if (p > p_min) for (j=p_min;j<p;j++) w[j] ${ = } 0$ ;   
void mpneg(VecUchar_IO &u) {   
Ones-complement negate the unsigned radix 256 number u. Int j, $\mathbf { n } { = } \mathbf { u }$ .size(); Uint ireg=256; for ( $\dot { \mathsf { J } } = \mathtt { n } - \dot { \mathsf { 1 } }$ 1; $\scriptstyle { \dot { \mathsf { J } } } > = 0$ ;j--) { ireg=255-u[j]+hibyte(ireg); u[j] $= 1$ lobyte(ireg); }   
} void mpmov(VecUchar_O &u, VecUchar_I &v) {   
Move the unsigned radix 256 number v into u. To achieve full accuracy, the array $\mathtt { v }$ must be as long as the array u.

Int j, $\mathbf { n } { = } \mathbf { u }$ .size(), $\mathtt { m } = \mathtt { v }$ .size(),n_min=MIN(n,m); for (j $_ { | = 0 }$ ;j<n_min;j++) u[j] $= \tt v$ [j]; if (n $>$ n_min) for(j=n_min;j<n-1;j++) u[j] ${ = } 0$ ;

# }

void mplsh(VecUchar_IO &u) { Left-shift digits of unsigned radix 256 number u. The final element of the array is set to 0.

Int j, $\mathrm { n } { = } \mathrm { u }$ .size();   
for ( $\scriptstyle \mathbf { j } = 0$ ;j<n-1;j++) u[j] $= \mathrm { u }$ [j+1];   
u[n-1] ${ = } 0$ ;

# }

Uchar lobyte(Uint x) {return (x & 0xff);} Uchar hibyte(Uint x) {return ( $( \mathrm {  ~ x ~ } > > \mathrm {  ~ 8 ~ }$ ) & 0xff);}

The following, more complicated, methods have discussion and implementation below.

void mpmul(VecUchar_O &w, VecUchar_I &u, VecUchar_I &v);   
void mpinv(VecUchar_O &u, VecUchar_I &v);   
void mpdiv(VecUchar_O &q, VecUchar_O &r, VecUchar_I &u, VecUchar_I &v);   
void mpsqrt(VecUchar_O &w, VecUchar_O &u, VecUchar_I &v);   
void mp2dfr(VecUchar_IO &a, string &s);   
string mppi(const Int np);

};

Full multiplication of two strings of digits, if done by the traditional hand method, is not a fast operation: In multiplying two strings of length $N$ , the multiplicand would be short-multiplied in turn by each byte of the multiplier, requiring $O ( N ^ { 2 } )$ operations in all. We will see, however, that all the arithmetic operations on numbers of length $N$ can in fact be done in $O ( N \times \log N \times \log \log N )$ operations.

The trick is to recognize that multiplication is essentially a convolution (-13.1) of the digits of the multiplicand and multiplier, followed by some kind of carry operation. Consider, for example, two ways of writing the calculation $4 5 6 \times 7 8 9$ :

<table><tr><td colspan="2">456 ×789</td><td>×</td><td>4 7</td><td>5 8</td><td>9</td></tr><tr><td colspan="2">4104</td><td></td><td></td><td>36 45 54</td><td></td></tr><tr><td colspan="2">3648</td><td>32</td><td></td><td>4048</td><td></td></tr><tr><td colspan="2">3192 359784</td><td>2835</td><td>42</td><td></td><td></td></tr><tr><td colspan="2"></td><td>28 67 359</td><td>118</td><td>93 54</td><td>784</td></tr></table>

The tableau on the left shows the conventional method of multiplication, in which three separate short multiplications of the full multiplicand (by 9, 8, and 7) are added to obtain the final result. The tableau on the right shows a different method (sometimes taught for mental arithmetic), where the single-digit cross products are all computed (e.g. $8 \times 6 = 4 8$ ), then added in columns to obtain an incompletely carried result (here, the list 28; 67; 118; 93; 54). The final step is a single pass from right to left, recording the single least-significant digit and carrying the higher digit or digits into the total to the left (e.g. $9 3 + 5 = 9 8$ , record the 8, carry 9).

You can see immediately that the column sums in the right-hand method are components of the convolution of the digit strings, for example $1 1 8 = 4 \times 9 + 5 \times$ $8 + 6 \times 7$ . In $\ S 1 3 . 1$ , we learned how to compute the convolution of two vectors by the fast Fourier transform (FFT): Each vector is FFT’d, the two complex transforms are multiplied, and the result is inverse-FFT’d. Since the transforms are done with floating arithmetic, we need sufficient precision so that the exact integer value of each component of the result is discernible in the presence of roundoff error. We should therefore allow a (conservative) few times $\log _ { 2 } ( \log _ { 2 } N )$ bits for roundoff in the FFT. A number of length $N$ bytes in radix 256 can generate convolution components as large as the order of $( 2 5 6 ) ^ { 2 } N$ , thus requiring $1 6 + \log _ { 2 } N$ bits of precision for exact storage. If it is the number of bits in the floating mantissa (cf. -22.2), we obtain the condition

$$
1 6 + \log _ { 2 } { N } + \mathrm { f e w } \times \log _ { 2 } { \log _ { 2 } { N } } < \mathrm { i t }
$$

We see that single precision, say with $\mathrm { i t } = 2 4$ , is inadequate for any interesting value of $N$ , while double precision, say with $\mathrm { i t } \ = \ 5 3$ , allows $N$ to be greater than $1 0 ^ { 6 }$ , corresponding to some millions of decimal digits. The use of Doub in the routines realft (-12.3) and four1 (-12.2) is therefore a necessity, not merely a convenience, for this application.

void MParith::mpmul(VecUchar_O &w, VecUchar_I &u, VecUchar_I &v) { Uses fast Fourier transform to multiply the unsigned radix 256 integers u[0..n-1] and $\mathtt { v } \left[ 0 \dots \dots \dots 1 \right]$ , yielding a product $\mathtt { w } [ 0 \rVert \cdot \mathtt { \sigma } \mathtt { \cdot n } \mathtt { + m } \mathtt { - } 1 ]$ .

const Doub RX $\equiv$ 256.0;   
Int j, $\mathrm { n n } { = } 1$ , $\mathbf { n } { = } \mathbf { u }$ .size(), ${ \mathfrak { m } } { = } \mathfrak { v }$ .size(), $\mathtt { p - w }$ .size(),n_max=MAX(m,n);   
Doub cy,t;   
while ( $\ln \mathrm { ~ < ~ } \mathrm { n } _ { - } \mathrm { m a x } ) \mathrm { n n ~ } < < = \mathrm { ~ 1 } ;$ Find the smallest usable power of 2 for the transform. nn $< < = ~ 1$ ;   
VecDoub a(nn,0.0),b(nn,0.0);   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j $^ { + + }$ ) a[j] ${ \bf \varepsilon } = { \bf u }$ [j]; Move $U$ and $V$ to double precision floating arrays. for ( $\scriptstyle \mathrm { j = 0 }$ ;j<m;j++) b[j] $= \tt v$ [j];   
realft(a,1); Perform the convolution: First, the two Fourier transrealft(b,1); forms.   
b[0] $\ast = \mathrm { ~ a ~ } [ 0 ]$ ; Then multiply the complex results (real and imagib[1] $\ast =$ a[1]; nary parts).   
for ( $\scriptstyle \mathbf { j } = 2$ ;j<nn;j $+ { = } 2$ ) {   
b[j] $=$ (t=b[j])\*a[j]-b[j+1]\*a[j+1];   
b[j+1]=t\*a[j+1]+b[j+1]\*a[j];   
}   
realft(b,-1); Then do the inverse Fourier transform.   
$\mathtt { c y = 0 . 0 }$ ; Make a final pass to do all the carries.   
for (j=nn-1;j>=0;j--) {   
t=b[j]/(nn >> 1)+cy+0.5; The 0.5 allows for roundoff error.   
cy=Uint(t/RX);   
b[j]=t-cy\*RX;   
}   
if (cy $> =$ RX) throw("cannot happen in mpmul");   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<p;j++) w[j] ${ = } 0$ ;   
w[0]=Uchar(cy); Copy answer to output.   
for ( $\mathrm { j } = 1$ ;j<MIN(n+m,p);j++) w[j] $\mathbf { \delta } =$ Uchar(b[j-1]);

With multiplication thus a “fast” operation, division is best performed by multiplying the dividend by the reciprocal of the divisor. The reciprocal of a value $V$ is calculated by iteration of Newton’s rule,

$$
U _ { i + 1 } = U _ { i } ( 2 - V U _ { i } )
$$

which results in the quadratic convergence of $U _ { \infty }$ to $1 / V$ , as you can easily prove. (Many historical supercomputers, and some more recent RISC processors, actually use this iteration to perform divisions.) We can now see where the operations count $N \log N \log \log N$ , mentioned above, originates: $N \log N$ is in the Fourier transform, with the iteration to converge Newton’s rule giving an additional factor of $\log \log N$ .

# void MParith::mpinv(VecUchar_O &u, VecUchar_I &v) {

Character string $\mathtt { v } \left[ 0 \dots \dots \dots 1 \right]$ is interpreted as a radix 256 number with the radix point after (nonzero) v[0]; u[0..n-1] is set to the most significant digits of its reciprocal, with the radix point after u[0].

const Int $\tt N F { = } 4$ ;   
const Doub $\mathbb { B } \mathbb { I } = 1$ .0/256.0;   
Int i,j, $\mathbf { n } { = } \mathbf { u }$ .size(), $\mathtt { m } = \mathtt { v }$ .size(),mm=MIN(MF,m);   
Doub fu,fv=Doub(v[mm-1]);   
VecUchar s $\left( \mathtt { n } + \mathtt { m } \right)$ ,r(2\*n+m);   
for $( { \mathrm { j } } { = } { \mathrm { m m } } { - } 2 ; { \mathrm { j } } { > } { = } 0 ; { \mathrm { j } } { - } { - } )$ { Use ordinary floating arithmetic to get an initial fv $\ast = \mathrm { ~ B I ~ }$ ; approximation. fv += v[j];   
}   
fu=1.0/fv;   
for (j=0;j<n;j++) { i=Int(fu); u[j]=Uchar(i); fu=256.0\*(fu-i);   
}   
for (;;) { Iterate Newton’s rule to convergence. mpmul(s,u,v); Construct $2 - U V$ in $s$ . mplsh(s); mpneg(s); s[0] $+ =$ Uchar(2); Multiply $s U$ into $U$ . mpmul(r,s,u); mplsh(r); mpmov(u,r); for ( $\mathrm { j } = 1$ ;j<n-1;j++) If fractional part of $s$ is not zero, it has not if (s[j] $! = ~ 0 )$ break; converged to 1. if $\scriptstyle \ j = = \mathtt { n - 1 }$ ) return;   
}

Division now follows as a simple corollary, with only the necessity of calculating the reciprocal to sufficient accuracy to get an exact quotient and remainder.

void MParith::mpdiv(VecUchar_O &q, VecUchar_O &r, VecUchar_I &u, VecUchar_I &v) { Divides unsigned radix 256 integers $\mathbf { u } \left[ 0 \ldots \mathbf { n - 1 } \right]$ by $\mathtt { v } [ 0 \dots \dots \dots 1 ]$ (with $\mathtt { m } \le \mathtt { n }$ required), yielding a quotient q[0..n-m] and a remainder $\mathbf { r } \left[ 0 \ldots \ldots \right] $ .

const Int MACC $\mathrel { \mathop = } 1$ ;   
Int i,is,mm, $\mathbf { n } { = } \mathbf { u }$ .size(), $\mathtt { m } = \mathtt { v }$ .size(), $\mathtt { p - r }$ .size(),n_min $\cdot ^ { = }$ MIN(m,p);   
if $\mathbf { \chi } _ { \mathrm { ~ m ~ } } > \mathbf { \chi } _ { \mathrm { ~ n ~ } }$ ) throw("Divisor longer than dividend in mpdiv");   
mm=m+MACC;   
VecUchar s(mm),rr(mm),ss(mm+1),qq(n-m+1),t(n);   
mpinv(s,v); Set $S = 1 / V$ .   
mpmul(rr,s,u); Set $Q = S U$ .   
mpsad(ss,rr,1); mplsh(ss);   
mplsh(ss);   
mpmov(qq,ss);   
mpmov(q,qq);   
mpmul(t,qq,v); Multiply and subtract to get the remainder.   
mplsh(t);   
mpsub(is,t,u,t);   
if (is $! = ~ 0$ ) throw("MACC too small in mpdiv");   
for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<n_min; $\dot { 1 } + +$ ) r[i] $\mathtt { \Omega } = \mathtt { t }$ [i+n-m];   
if (p>m) for (i=m;i<p; $\Dot { \ b { 1 } } + +$ ) $\mathbf { r } \left[ \dot { \mathbf { 1 } } \right] { = } 0$ ;

}

Square roots are calculated by a Newton’s rule much like division. If

$$
\begin{array} { r } { U _ { i + 1 } = \frac { 1 } { 2 } U _ { i } ( 3 - V U _ { i } ^ { 2 } ) } \end{array}
$$

then $U _ { \infty }$ converges quadratically to $1 / \sqrt { V }$ . A final multiplication by $V$ gives $\sqrt { V }$ .

void MParith::mpsqrt(VecUchar_O &w, VecUchar_O &u, VecUchar_I &v) { Character string $\mathtt { v } [ 0 \dots \dots 1 ]$ is interpreted as a radix 256 number with the radix point after $\tt v [ 0 ]$ ; $\mathtt { w } \left[ 0 \ldots \ldots \ldots 1 \right]$ is set to its square root (radix point after $\mathtt { w } [ 0 ]$ ), and $\mathtt { u } [ 0 \ldots \mathtt { n } ^ { - 1 } ]$ is set to the reciprocal thereof (radix point before u[0]). w and u need not be distinct, in which case they are set to the square root.

const Int $\mathtt { M F } { = } 3$ ;   
const Doub $\mathbb { B } \mathbb { I } = 1$ .0/256.0;   
Int i,ir,j, $\mathbf { n } { = } \mathbf { u }$ .size(), ${ \mathfrak { m } } { = } \mathfrak { v }$ .size(),mm=MIN(m,MF);   
VecUchar $\mathtt { r } ( 2 \ast \mathtt { n } )$ ,x $\left( \mathtt { n } + \mathtt { m } \right)$ ,s(2\*n+m),t(3\*n+m);   
Doub fu,fv $=$ Doub(v[mm-1]);   
for (j=mm-2;j>=0;j--) { Use ordinary floating arithmetic to get an initial apfv $\ast =$ BI; proximation. fv += v[j];   
}   
fu=1.0/sqrt(fv);   
for (j=0;j<n;j++) $\dot { \bf 1 } =$ Int(fu); u[j]=Uchar(i); fu=256.0\*(fu-i);   
}   
for (;;) { Iterate Newton’s rule to convergence. mpmul(r,u,u); Construct $S = ( 3 - V U ^ { 2 } ) / 2$ . mplsh(r); mpmul(s,r,v); mplsh(s); mpneg(s); s[0] $+ =$ Uchar(3); mpsdv(s,s,2,ir); for (j=1;j<n-1; $\mathrm { i } + +$ ) { If fractional part of $s$ is not zero, it has not conif (s[j] != 0) { verged to 1. mpmul(t,s,u); Replace $U$ by $s U$ . mplsh(t); mpmov(u,t); break; } if (j<n-1) continue; mpmul(x,u,v); Get square root from reciprocal and return. mplsh(x); mpmov(w,x); return;   
}

We already mentioned that radix conversion to decimal is a merely cosmetic operation that should normally be omitted. The simplest way to convert a fraction to decimal is to multiply it repeatedly by 10, picking off (and subtracting) the resulting integer part. This has an operations count of $O ( N ^ { 2 } )$ , however, since each liberated decimal digit takes an $O ( N )$ operation. It is possible to do the radix conversion as a fast operation by a “divide-and-conquer” strategy, in which the fraction is (fast) multiplied by a large power of 10, enough to move about half the desired digits to the left of the radix point. The integer and fractional pieces are now processed independently, each further subdivided. If our goal were a few billion digits of $\pi$ , instead of a few thousand, we would need to implement this scheme. For present purposes, the following lazy routine is adequate:

# void MParith::mp2dfr(VecUchar_IO &a, string &s)

Converts a radix 256 fraction a[0..n-1] (radix point before a[0]) to a decimal fraction represented as an ASCII string $\mathbf { s } \left[ 0 \ldots \ldots \right]$ , where m is a returned value. The input array $\mathbf { a } \left[ 0 \ldots \mathbf { n - 1 } \right]$ is destroyed. NOTE: For simplicity, this routine implements a slow $( \propto \dot { N } ^ { 2 } )$ algorithm. Fast $( \propto N \ln N )$ ), more complicated, radix conversion algorithms do exist.   
{   
const Uint IAZ=48;   
char buffer[4];   
Int j,m;   
Int $\mathrm { n } = \mathrm { a }$ .size();   
m=Int(2.408\*n);   
sprintf(buffer,"%d",a[0]);   
s=buffer;   
s +=   
mplsh(a);   
for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<m;j++) { mpsmu(a,a,10); s $+ =$ a[0]+IAZ; mplsh(a);   
}

Finally, then, we arrive at a routine implementing equations (22.7.1) and (22.7.2):

string MParith::mppi(const Int np) J   
Demonstrate multiple precision routines by calculating and printing the first np bytes of $\pi$ . const Uint IAOFF $\ddots$ 48,MACC $^ { * 2 }$ ; Int ir,j,n=np+MACC; Uchar mm; string s; VecUchar x(n),y(n),sx(n),sxi(n),z(n),t(n),pi(n),ss( $^ { 2 * \mathrm { n } }$ ),tt $( 2 \ast \mathtt { n } )$ ; t[0] $^ { = 2 }$ ; Set $T = 2$ . for ( $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<n;j++) t[j] ${ = } 0$ ; mpsqrt(x,x,t); Set $X _ { 0 } = \sqrt { 2 }$ . mpadd(pi,t,x); Set $\pi _ { 0 } = 2 + { \sqrt { 2 } }$ . mplsh(pi); mpsqrt(sx,sxi,x); Set $Y _ { 0 } = 2 ^ { 1 / 4 }$ . mpmov(y,sx); for (;;) { mpadd(z,sx,sxi); Set $X _ { i + 1 } = ( X _ { i } ^ { 1 / 2 } + X _ { i } ^ { - 1 / 2 } ) / 2$ . mplsh(z); mpsdv(x,z,2,ir);mpsqrt(sx,sxi,x); Form the temporary $T = Y _ { i } X _ { i + 1 } ^ { 1 / 2 } + X _ { i + 1 } ^ { - 1 / 2 }$ . mpmul(tt,y,sx); mplsh(tt);

mpadd(tt,tt,sxi); mplsh(tt); x[0]++; Increment $X _ { i + 1 }$ and $Y _ { i }$ by 1. y[0]++; mpinv(ss,y); Set $Y _ { i + 1 } = T / ( Y _ { i } + 1 )$ . mpmul(y,tt,ss); mplsh(y); mpmul(tt,x,ss); Form temporary $T = ( X _ { i + 1 } + 1 ) / ( Y _ { i } + 1 )$ . mplsh(tt); mpmul(ss,pi,tt); Set $\pi _ { i + 1 } = T \pi _ { i }$ . mplsh(ss); mpmov(pi,ss); mm=tt[0]-1; If $T = 1$ , then we have converged. for ( $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j < n-1;j++) if (tt[j] $! = ~ \mathtt { m m } ,$ ) break; if ${ \mathrm { ( j ~ } } = = { \mathrm { ~ n } } - 1 { \mathrm { ) } }$ ) { mp2dfr(pi,s); Convert to decimal for printing. NOTE: The conversion routine, for this demon stration only, is a slow $( \propto N ^ { 2 } )$ algorithm. Fast $( \propto N \ln N )$ , more complicated radix conversion algorithms do exist. s.erase(Int(2.408\*np),s.length()); return s; } } }

$$
{ \frac { 1 } { \pi } } = { \frac { \sqrt { 8 } } { 9 8 0 1 } } \sum _ { n = 0 } ^ { \infty } { \frac { ( 4 n ) ! ( 1 1 0 3 + 2 6 3 9 0 n ) } { ( n ! 3 9 6 ^ { n } ) ^ { 4 } } }
$$

using the above routines. You might also use the routines to verify that the number $2 ^ { 5 1 2 } ~ + ~ 1$ is not a prime, but has factors 2,424,833 and 7,455,602,825,647,884,208,337,395,736,200,454,918,783,366,342,657 (which are in fact prime; the remaining prime factor being about $7 . 4 1 6 \times 1 0 ^ { 9 8 }$ ) [4].

# CITED REFERENCES AND FURTHER READING:

Borwein, J.M., and Borwein, P.B. 1987, Pi and the AGM: A Study in Analytic Number Theory and Computational Complexity (New York: Wiley).[1]   
Knuth, D.E. 1997, Seminumerical Algorithms, 3rd ed., vol. 2 of The Art of Computer Programming (Reading, MA: Addison-Wesley), $\ S 4 . 3 . [ 2 ]$   
Ramanujan, S. 1927, Collected Papers of Srinivasa Ramanujan, G.H. Hardy, P.V. Seshu Aiyar, and B.M. Wilson, eds. (Cambridge, UK: Cambridge University Press), pp. 23–39.[3]   
Kolata, G. 1990, June 20, “Biggest Division a Giant Leap in Math,” The New York Times.[4]   
Kronsjö, L. 1987, Algorithms: Their Complexity and Efficiency, 2nd ed. (New York: Wiley).   
Abstract Base Class (ABC) 24, 33, 34, 87, 114, 703, 874   
Accelerated convergence of series 177, 211–218   
Accuracy 8–12 achievable in minimization 493, 497, 503 achievable in root finding 448 contrasted with fidelity 1037, 1046 CPU different from memory 230 vs. stability 907, 931, 932, 1035, 1050   
Adams-Bashford-Moulton method 943   
Adams’ stopping criterion 467   
Adaptive integration 901, 910–921, 928, 930, 935, 946, 995 Monte Carlo 410–418 PI stepsize control 915 predictive stepsize control 939 see also Adaptive quadrature   
Adaptive quadrature 155, 167, 194–196 and singularities 195 termination criterion 194   
Addition multiple precision 1186 theorem, elliptic integrals 310   
ADI (alternating direction implicit) method 1052, 1053, 1065, 1066, 1185   
Adjoint operator 1071   
Advanced topics (explanation) 6   
Advective equation 1032   
Affine scaling 543   
Agglomerative clustering 873–882   
AGM (arithmetic geometric mean) 1185   
Airy function 254, 283, 289, 291 routine for 290   
Aitken’s delta squared process 212, 214 interpolation algorithm 118   
Algorithms, less-numerical 1160–1193   
Aliasing 606, 685 see also Fourier transform   
Alignment of strings by DP 559–562   
All-poles or all-zeros models 681, 682 see also Maximum entropy method (MEM); Periodogram   
Alternating-direction implicit method (ADI) 1052, 1053, 1065, 1066, 1185   
Alternating series 211, 216   
Alternative extended Simpson’s rule 160   
AMD (approximate minimum degree) 544, 548   
Amoeba 503 see also Simplex, method of Nelder and Mea   
Amplification factor 1033, 1035, 1038, 1045, 1046   
Amplitude error 1036   
Analog-to-digital converter 1018, 1166   
Analyticity 246   
Analyze/factorize/operate package 76, 1030   
Anderson-Darling statistic 739   
Andrew’s sine 821   
Angle between vectors 1120, 1121 coordinates on $n$ -sphere 1128 exterior, of polygons 1122   
Annealing, method of simulated 487, 488, 549–555 assessment 554, 555 for continuous variables 550, 552–554 schedule 551, 552 thermodynamic analogy 550 traveling salesman problem 551, 552   
ANSI-16 1171   
ANSI/ISO $\mathrm { C } { + } { + }$ standard 5   
Antonov-Saleev variant of Sobol’ sequence 404–406, 408, 409   
Apple Mac OS X 5   
Approximate inverse of matrix 63   
Approximation of functions 110 by Chebyshev polynomials 234, 625 by rational functions 247–251 by wavelets 711, 712, 989 Pade approximant 212, 245–247 ´ see also Fitting   
Area polygon 1126 sphere in $n$ -dimensions 1128 triangle 1111   
Arithmetic arbitrary precision 1160, 1185–1193 floating point 1163 IEEE standard 1164, 1165 rounding 1164, 1165 64 bit 341   
Arithmetic coding 755, 1160, 1181–1185   
Arithmetic-geometric mean (AGM) method 1185   
Array assign function 27 centered subarray of 115 classes for 24–29 resize function 27 size function 27 three-dimensional 36 unit-offset 36 zero-offset 36   
Artificial viscosity 1037, 1042   
Ascending transformation, elliptic integrals 310   
ASCII character set 1168, 1175, 1181   
assign 27   
Associated Legendre polynomials 971 recurrence relation for 294 relation to Legendre polynomials 293   
Association, measures of 721, 741, 758–761   
Asymptotic series 210, 216 exponential integral 216, 269   
Attenuation factors 698   
Autocorrelation in linear prediction 673–675 use of FFT 648, 649 Wiener-Khinchin theorem 602, 682   
Autoregressive model (AR) see Maximum entropy method (MEM)   
Average deviation of distribution 723   
Averaging kernel, in Backus-Gilbert method 1014   
B-spline 148   
Backsubstitution 47, 49, 53, 56, 103 complex equations 55 direct for computing ${ \bf A } ^ { - 1 }$ - B 53 in band-diagonal matrix 60 relaxation solution of boundary value problems 966   
Backtracking 522 in quasi-Newton methods 478–483   
Backus-Gilbert method 1014–1016   
Backward deflation 464, 465   
Bader-Deuflhard method 940   
Bahl-Cocke-Jelinek-Raviv algorithm forward-backward algorithm 867   
Bairstow’s method 466, 471   
Balancing 592, 594   
Band-diagonal matrix 56, 58–61 backsubstitution 60 $_ { L U }$ decomposition 59 multiply by vector 58 storage 58   
Band-pass filter 667, 670 wavelets 701   
Bandwidth limited function 605   
Bank accounts, checksum for 1174   
Bar codes, checksum for 1174   
Barrier method 541   
Bartels-Golub update 535   
Bartlett window 657   
Barycentric coordinates 1114, 1116   
Barycentric rational interpolation 113, 127, 128   
Base class 23   
Base of representation 8, 1164   
Basin of convergence 461, 463   
Basis functions in general linear least squares 788   
Baum-Welch re-estimation hidden Markov model 865–867 relation to expectation-maximization 866   
Bayes’ theorem 774, 777, 825   
Bayesian approach to inverse problems 1005, 1022 contrasted with frequentist 774 estimation of parameters by MCMC 774, 824–835 lack of goodness-of-fit methods 779, 1010 normalizing constant 779 odds ratio 757, 779 parameter estimation 777, 778 prior 757, 775, 777, 1005 views on straight line fitting 787 vs. historic maximum entropy method 1022   
Bayesian algorithms hidden Markov model 868 Viterbi decoding 868   
Bayesian networks 840, 841 node parents 841 nodes 840 posterior probabilities 841 prior probabilities 841   
Bayesian re-estimation hidden Markov model 864–866   
Belief networks 840 forward-backward algorithm 867   
Bellman-Dijkstra-Viterbi algorithm 556, 850, 853   
Berlekamp-Massey decoding algorithm 852   
Bernoulli number 164   
Bessel functions 274–292 asymptotic form 274, 279, 284 complex 254 continued fraction 283, 284, 287, 288 fractional order 274, 283–292 Miller’s algorithm 221, 278 modified 279–283 modified, fractional order 287–289 modified, normalization formula 282, 288 modified, routines for 280 normalization formula 221 recurrence relation 219, 274, 275, 278, 281, 283–285 reflection formulas 286 reflection formulas, modified functions 289 routines for 276, 286 routines for modified functions 289 series for 210, 274 series for $K _ { \nu }$ 288 series for $Y _ { \nu }$ 284, 285 spherical 283, 291, 292 turning point 283

![](../chunks/Numerical Recipes_ The Art of Scientific Computing_part_0018_pages_1191-1260/auto/images/a03563108e75539239b188b39a7e5fe588fbd594e92a35a8d363f8bf6036c888.jpg)  
Figure 22.7.1. The first 2398 decimal digits of $\pi$ , computed by the routines in this section.

Wronskian 283, 284, 287 Best-fit parameters 773, 781, 785, 822–824 see also Fitting Beta function 256, 258, 259 incomplete see Incomplete beta function Beta probability distribution 333, 334 deviates 371 gamma as limiting case 333 Betting 755–758, 760, 761 fair bet 755, 756, 758, 760, 761 proportional 758, 760 Bezier curve 148 BFGS algorithm see Broyden-Fletcher-Goldfarb-Shanno algorithm Bias of exponent 8 removal in linear prediction 145, 678, 679 Biconjugacy 88 Biconjugate gradient method elliptic partial differential equations 1030 for sparse system 88, 716 preconditioning 89, 1030 Bicubic interpolation 136–138 Bicubic spline 135 Big-endian 9 Biharmonic equation 153 Bilinear interpolation 133, 134 Binary block code 851 Binomial coefficients 256, 258 recurrences for 258 Binomial probability function 258, 338, 339 deviates from 374–377 moments of 735 Poisson as limiting case 338 Binormal distribution 746, 813 Biorthogonality 88 Bisection 115, 460 compared to minimum bracketing 492 root finding 445, 447–449, 454, 492, 584 Bispectrum 604 Bit 8, 754–756, 760, 761 phantom 9 pop count 16 reversal in fast Fourier transform (FFT) 610, 638 Bit-parallel random comparison 374 Bit-twiddling hacks 16 Bitwise logical functions 1170 test if integer a power of 2 16, 611 trick for next power of 2 16, 361 Black-Scholes formula 329 BLAST (software) 562 BLAT (software) 562 Block-by-block method 994 Bluetooth 1168 Bode’s rule 158 Boltzmann probability distribution 550 Boltzmann’s constant 550 Bolyai-Gerwien theorem 1127 Bookie, information theory view of 758

Bool 25   
Bootstrap method 809, 810   
Bordering method for Toeplitz matrix 96   
Borwein and Borwein method for $\pi$ 1185   
Boundary 196, 528, 955   
Boundary conditions for differential equations 900 for spheroidal harmonics 972, 973 in multigrid method 1072 initial value problems 900 partial differential equations 620, 1025, 1053–1058 two-point boundary value problems 900, 955–984   
Boundary value problems 1026 see also Differential equations; Elliptic partial differential equations; Two-point boundary value problems   
Bounds checking 35 in vector by at 35   
Box 1099–1101 test if point inside 1100 tree of, as data structure 1101   
Box-Muller algorithm for normal deviate 364   
Bracketing of function minimum 445, 490–496, 503 of roots 443, 445–447, 454, 455, 464, 465, 470, 492   
Branch cut, for hypergeometric function 252–254   
Break iteration 15   
Brenner’s FFT implementation 611, 628   
Brent’s method minimization 489, 496–499, 785 minimization, using derivative 489, 499, 500 root finding 443, 449, 453–456, 459, 786   
Broyden-Fletcher-Goldfarb-Shanno algorithm 490, 521–525   
Broyden’s method 474, 483–486 singular Jacobian 486   
Bubble sort 420   
Bugs, how to report 5   
Bulirsch-Stoer algorithm for rational function interpolation 125 for second order equations 929 method 252, 318, 900, 901, 909, 921–929, 942 method, dense output 927 method, implementation 927 method, stepsize control 924–926, 929   
Burg’s LP algorithm 677   
Burn-in 826, 833–835   
Butterfly 360, 361, 610   
Byte 8   
C (programming language) 1 _FILE__ and __LINE__ macros 30 idioms 16 syntax 12–17   
$\mathrm { C } { + } { + }$ ANSI/ISO standard 5 C family syntax 12–17 const statement 31, 32 contiguous storage for vector 27 control structures 14, 15 error class 30 inline directive 29 NR not a textbook on 2 operator associativity 12 operator precedence 12 overloading 28 scope, temporary 20, 21 standard library 10, 24 templates 17, 22, 26, 33, 34, 419, 421 throw 30 try and catch 30 types 25 types used in NR 4 user-defined conversions 31 valarray class 25 vector class 24 virtual function 33 why used in NR 1   
C# (programming language) 1, 12   
Calendar algorithms 2, 3, 6, 7   
Calibration 778   
Cardinal functions 1089–1091   
Cards, sorting a hand of 420, 422   
Carlson’s elliptic integrals 310–316   
Carpe diem 830   
catch 30   
Cauchy principal value integrals 178   
Cauchy probability distribution 322, 323 deviates from 367 see also Lorentzian probability distribution   
Cauchy problem for partial differential equations 1024   
Cavender-Felsenstein model 873   
Cayley’s representation of $\exp ( - i H t )$ 1049   
CCITT (Comite Consultatif International ´ Tel´ egraphique et T ´ el´ ephonique) 1171, 1180 ´   
CCITT-16 1171   
CDF see Cumulative Distribution Function   
Center of mass 399, 400, 1113, 1127   
Central limit theorem 777   
Central tendency, measures of 721   
Centroid see Center of mass   
Change of variable in integration 170–172, 995 in Monte Carlo integration 401 in probability distribution 362   
Char 25   
Character-based clustering methods 869   
Characteristic polynomial digital filter 670 eigensystems 563, 583, 665 linear prediction 676 matrix with a specified 469 of recurrence relation 221 of tridiagonal system 665   
Characteristics of partial differential equations 1024–1026   
Chebyshev acceleration in successive over-relaxation (SOR) 1064   
Chebyshev approximation 95, 156, 232–239 Clenshaw-Curtis quadrature 241 Clenshaw’s recurrence formula 236 coefficients for 234 contrasted with Pade approximation 245 ´ derivative of approximated function 232, 240, 241 economization of series 243–245 even function 237 fast cosine transform and 625 for error function 264 gamma functions 285 integral of approximated function 240, 241 odd function 237 polynomial fits derived from 241, 243, 248 rational function 247–251 Remes exchange algorithm for filter 669   
Chebyshev polynomials 183, 187, 233–239 basis functions for spectral methods 1085 continuous orthonormality 233 discrete orthonormality 233 explicit formulas for 233 formula for $x ^ { k }$ in terms of 233   
Check digit (decimal) 1173   
Checksum 1160, 1168–1175 cyclic redundancy (CRC) 1168–1173   
Chemical reaction networks 946–954   
Chi-by-eye 774   
Chi-square fitting see Fitting; Least-squares fitting   
Chi-square probability function 330, 331, 732, 778, 779, 1003 as boundary of confidence region 812 deviates from 371   
Chi-square test 731–734 and confidence limit estimation 812 chi-by-eye 774 chi-square-gamma test 735 degrees of freedom 732, 733 for binned data 731–734 for contingency table 742–745 for inverse problems 1003 for straight line fitting 781 for straight line fitting, errors in both coordinates 785 for two binned data sets 732 goodness-of-fit 780 how much $\Delta \chi ^ { 2 }$ is significant 816 least-squares fitting 778–780 and likelihood ratio test 735 modified Neyman 735 nonlinear models 799 small numbers of counts 734, 735 for two binned data sets 735 unequal size samples 733   
Chirp signal 672   
Cholesky decomposition 100–102, 525, 568 and covariance structure 378, 379 decorrelating random variables 379 multivariate Gaussian distribution 847, 848 operation count 100 pivoting 101 solution of normal equations 543, 790, 791 sparse decomposition 544, 548   
Circle inscribed or circumscribed 1112 largest empty 1147 random point on 1131   
Circulant 700   
Circumscribed circle (circumcircle) 1112   
CLAPACK 567   
Class 17–24 abstract base (ABC) 24, 33, 34, 87, 114, 703, 874 base class 23 derived 23 error class 30 inheritance 23, 24 is-a relationship 23 matrix 24–29 partial abstraction via 24 prerequisite relationship 23 public vs. private 17 pure virtual 34 suffix _I, _O, _IO 26, 32 templated 22, 33, 34 vector 24–29 see also Object   
Class library 2   
Classification 840–898 kernel methods 889, 892 support vector machine 883–898   
Clenshaw-Curtis quadrature 156, 241, 624, 625   
Clenshaw’s recurrence formula 219, 222, 223 for Chebyshev polynomials 236 stability 223   
Clock, program timing routine 355   
Clocking errors 1172   
CLP (linear programming package) 536   
Clustering agglomerative 873–882 hierarchical 868–882 k-means 848–850 neighbor-joining (NJ) 873, 878–882   
cn function 316   
Coarse-grid correction 1068   
Coarse-to-fine operator 1068   
Codes binary block codes 851 codeword 851 correcting bit errors 855 error-correcting 851–855 Golay code 852 Hamming code 852 Hamming distance 851, 1168 hard-decision decoding 853 linear codes 851

minimal trellis 853 perfect code 852 Reed-Solomon 852, 855 soft-decision decoding 853 syndrome decoding 852 trellis 853, 856 turbo codes 855 Viterbi decoding 854 Coding arithmetic 755, 1181–1185 checksums 1168–1175 compression 754, 756 decoding a Huffman-encoded message 1178 Huffman 713, 1175–1180 run-length 1180 variable length code 1176 Ziv-Lempel 1176 see also Arithmetic coding; Huffman coding Coefficients binomial 258 for Gaussian quadrature 179, 180 for Gaussian quadrature, nonclassical weight function 189–191, 995 for quadrature formulas 157–162, 995 Column operations on matrix 43, 45 Column totals 743, 759 Combinatorial minimization see Annealing Comite Consultatif International T ´ el´ egraphique et ´ Tel´ ephonique (CCITT) 1171, 1180´ Communications protocol 1168 Comparison function for rejection method 366 Compiler check on via constructors 36 tested 5 Complementary error function see Error function Complete elliptic integral see Elliptic integrals Complex arithmetic 225, 226 access vector as if complex 613, 620 avoidance of in path integration 253 Complex type 25 cubic equations 228, 229 linear equations 55 quadratic equations 227 Complex error function 302 Complex plane fractal structure for Newton’s rule 462 path integration for function evaluation 251–254, 318 poles in 124, 210, 252, 256, 670, 682, 922 Complex systems of linear equations 55 Compression of data 713, 715, 1160, 1175–1185 Computational geometry floating point arithmetic in 1098 Computer graphics 1097 Computer vision 1097 Concordant pair for Kendall’s tau 751 Condition number 69, 89, 791, 793 Conditional entropy 758–761 Confidence level 810, 811, 814–816 Confidence limits

and chi-square 811 bootstrap method 809, 810 by Monte Carlo simulation 807–810 confidence region, confidence interval 810, 811 from singular value decomposition (SVD) 816, 817 on estimated model parameters 807–817   
Confluent hypergeometric function 254, 287   
Conjugate directions 509, 511, 512, 516   
Conjugate gradient method and wavelets 716 biconjugate 88 compared to variable metric method 521 elliptic partial differential equations 1030 for minimization 489, 515–520, 1011, 1020 for sparse system 87–92, 716 minimum residual method 89 preconditioner 89, 90   
Conservative differential equations 928, 930   
const correctness 26, 31, 32 protects container, not contents 31, 32 to protect data 32   
Constellation in Viterbi decoding 855   
Constrained linear inversion method 1006   
Constrained linear optimization see Linear programming   
Constrained optimization 487   
Constraints deterministic 1011–1013 linear 526, 530   
Constructor 18, 27   
Container, STL 421   
Contingency coefficient C 743, 744   
Contingency table 741–745, 753, 758, 759 statistics based on chi-square 742–745 statistics based on entropy 758–761   
Continue statement 15   
Continued fraction 206–209 and recurrence relation 222 Bessel functions 283, 284, 288 convergence criterion 208 equivalence transformation 208 evaluation 206–209 evaluation along with normalization condition 288 even and odd parts 208, 260, 267, 298, 301 exponential integral 267 Fresnel integral 298 incomplete beta function 270 incomplete gamma function 260 Lentz’s method 207, 260 modified Lentz’s method 208 Pincherle’s theorem 222 ratio of Bessel functions 287 rational function approximation 207, 260 recurrence for evaluating 207, 208 sine and cosine integrals 301 Steed’s method 207 tangent function 206 typography for 206   
Continuous variable (statistics) 741   
Control structures and scope 21   
Convergence accelerated, for series 177, 211–218 basin of 461, 463 criteria for 448, 493, 503, 598, 599, 802, 969 eigenvalues accelerated by shifting 585 exponential 174–178, 180, 238, 239, 1083–1096 golden ratio 449, 500 hyperlinear (series) 211 linear 448, 495 linear (series) 211 logarithmic (series) 211 Markov model 858 of algorithm for $\pi$ 1185 of golden section search 494, 495 of Levenberg-Marquardt method 802 of $Q L$ method 584, 585 of Ridders’ method 452 quadratic 64, 452, 459, 511, 512, 522, 1185 rate 448, 454, 457, 459 recurrence relation 222 series vs. continued fraction 206 spectral radius and 1061, 1066   
Conversions, user-defined 31   
Convex hull 1097, 1132, 1146   
Convex sets, use in inverse problems 1011–1013   
Convolution and polynomial interpolation 129 denoted by asterisk 602 finite impulse response (FIR) 642, 643 multiple precision arithmetic 1188 multiplication as 1188 necessity for optimal filtering 645 of functions 602, 616, 617, 631 of large data sets 646, 647 overlap-add method 647 overlap-save method 646 relation to wavelet transform 700, 701 theorem 602, 641, 656 theorem, discrete 642, 643 treatment of end effects 643 use of FFT 641–647 wraparound problem 643   
Cooley-Tukey FFT algorithm 616   
Cornwell-Evans algorithm 1021   
Corporate promotion ladder 427   
Corrected distance transformation 873   
Corrected two-pass algorithm 724   
Correction, in multigrid method 1067   
Correlation coefficient (linear) 745–748   
Correlation function 602, 617 and Fourier transforms 602, 617 autocorrelation 602, 649, 673–675 theorem 602, 648 three-point 604 treatment of end effects 648

using FFT 648, 649 Wiener-Khinchin theorem 602, 682 Correlation, statistical 721, 741 among parameters in a fit 782, 793 Kendall’s tau 749, 751–754 linear correlation coefficient 745–748, 783 linear related to least-squares fitting 745, 783 nonparametric or rank statistical 748–754 Spearman rank-order coefficient 749–751 sum squared difference of ranks 749 uncertainty coefficient 761 Coset leader 852 Cosine function, recurrence 219 Cosine integral 297, 300–302 continued fraction 301 routine for 301 series 301 Cosine transform see Fast Fourier transform (FFT); Fourier transform Coulomb wave function 254, 283 Counts, small numbers of 734, 735 Courant condition 1034, 1036, 1038–1040, 1042 multidimensional 1051 Courant-Friedrichs-Lewy stability criterion see Courant condition Covariance a priori 824 from singular value decomposition (SVD) 817 in general linear least squares 790, 791, 794 in nonlinear models 802 in straight line fitting 782 matrix, and normal equations 790 matrix, Cholesky decomposition 101 matrix, is inverse of Hessian matrix 802 matrix, of errors 1003, 1015 matrix, when it is meaningful 812, 813 relation to chi-square 812–816 CR method see Cyclic reduction (CR) Cramer’s V 743, 744 Crank-Nicolson method 1045, 1049, 1051, 1052 Cray, Seymour 1163 CRC (cyclic redundancy check) 1168–1173 CRC-12 1171 Critical (Nyquist) sampling 605, 607, 653 Cross $\otimes$ (denotes matrix outer product) 78 Crosstabulation analysis 742 see also Contingency table Crout’s algorithm 49, 59 Cubic equations 227–229, 461 Cubic spline interpolation 120–124 see also Spline Cumulative Distribution Function (cdf) 435 Curse of dimensionality 556, 891 Curvature matrix see Hessian matrix Curve interpolation 147 Cycle, in multigrid method 1069 Cyclic Jacobi method 573 Cyclic reduction (CR) 224, 1054, 1057, 1058 Cyclic redundancy check (CRC) 1168–1173

Cyclic tridiagonal systems 79, 80   
D.C. (direct current) 602   
Danielson-Lanczos lemma 609, 610, 638   
Data continuous vs. binned 731 entropy 754–761, 1176 essay on 720 fitting 773–838 fraudulent 780 glitches in 777 iid (independent and identically distributed) 809 linearly separable 884 missing data points 150–154 modeling 773–838 smoothing 721, 766–772 statistical tests 720–772 unevenly or irregularly sampled 139–154, 685, 690, 771 use of CRCs in manipulating 1169 windowing 655–667 see also Statistical tests   
Data compression 713, 715, 1160 arithmetic coding 1181–1185 cosine transform 625 Huffman coding 713, 1175–1181 linear predictive coding (LPC) 679–681 lossless 1175   
Data Encryption Standard (DES) 358–361   
Data type 8   
DAUB4 700, 702, 706, 707, 711, 715   
DAUB6 702   
DAUB20 706   
Daubechies wavelet coefficients 700–702, 704, 706–708, 715   
Davidon-Fletcher-Powell algorithm 490, 521, 522   
Dawson’s integral 302, 304, 717 approximation for 303 routine for 303   
DE rule 174 implementation 175 infinite range 176   
Decoding Berlekamp-Massey algorithm for Reed-Solomon code 852 directed graph 556, 850 hard-decision 853 hard-decision vs. soft-decision 855 maximum likelihood 854 Reed-Solomon codes 855 soft-decision decoding 853 syndrome decoding 852 Turbo codes 855 Viterbi algorithm 854 Viterbi, compared to hidden Markov model 867, 868   
Decomposition see Cholesky decomposition; $_ { L U }$ decomposition; $\boldsymbol { Q R }$ decomposition; Singular value decomposition (SVD)   
Deconvolution 645–647, 650 see also Convolution; Fast Fourier transform (FFT); Fourier transform   
Decorrelating random variables 379   
Defect, in multigrid method 1067   
Deferred approach to the limit see Richardson’s deferred approach to the limit   
Deflation of matrix 585 of polynomials 464–466, 471   
Degeneracy kernel 992 linear algebraic equations 73, 793 minimization principle 1002   
Degrees of freedom 732, 733, 778, 779, 813–815   
Delaunay triangulation 1097, 1131–1149 applications of 1141–1149 incremental constructions 1134 interpolation using 1141 largest minimum angle property 1134 minimum spanning tree 1147 not minimum weight 1134   
Delone, B.N. see Delaunay Triangulation   
Dense output, for differential equations 904, 915, 927   
Dependencies, program 4   
Dependency graph or matrix 949   
Derivatives approximation by sinc expansion 178 computation via Chebyshev approximation 232, 240, 241 computation via Savitzky-Golay filters 232, 769 matrix of first partial see Jacobian determinant matrix of second partial see Hessian matrix numerical computation 229–232, 480, 769, 936, 960, 978 of polynomial 202 use in optimization 499–502   
Derived class 23   
DES see Data Encryption Standard   
Descending transformation, elliptic integrals 310   
Descent direction 478, 484, 522   
Descriptive statistics 720–772 see also Statistical tests   
Design matrix 768, 788, 1002   
Design of experiments 410   
Detailed balance equation 825–827   
Determinant 39, 54, 55   
Devex 535   
Deviates, random see Random deviates   
DFP algorithm see Davidon-Fletcher-Powell algorithm   
Diagonal dominance 57, 802, 987, 1060   
Diagonal rational function 125   
Diehard test, for random numbers 345   
Difference equations, finite see Finite difference equations (FDEs)   
Difference operator 212   
Differential equations 899–954

accuracy vs. stability 907, 931   
Adams-Bashforth-Moulton schemes 943   
adaptive stepsize control 901, 910–921,   
924–926, 929, 939, 941, 943, 944, 946   
algebraically difficult sets 970   
backward Euler’s method 932   
Bader-Deuflhard method for stiff 940   
boundary conditions 900, 955, 962, 977   
Bulirsch-Stoer method 252, 318, 900, 901,   
909, 921–928, 942   
Bulirsch-Stoer method for conservative   
equations 928, 930   
comparison of methods 900, 901, 942, 946,   
957   
conservative 928, 930   
dense output 904, 915, 927   
discreteness effects 946–954   
eigenvalue problem 958, 973, 977–981   
embedded Runge-Kutta method 911, 936   
equivalence of multistep and multivalue   
methods 945   
Euler’s method 900, 907, 931   
forward Euler’s method 931   
free boundary problem 958, 983   
global vs. local error 914   
high-order implicit methods 934   
implicit differencing 932, 933, 944   
initial value problems 900   
integrating to an unknown point 916   
internal boundary conditions 983, 984   
internal singular points 983, 984   
interpolation on right-hand sides 115   
Kaps-Rentrop method for stiff 934   
local extrapolation 911   
modified midpoint method 922, 923   
multistep methods 900, 942–946   
multivalue methods 942–946   
Nordsieck method 944   
order of method 907, 922   
path integration for function evaluation   
251–254, 318   
predictor-corrector methods 900, 909, 934,   
942–946   
r.h.s. independent of $x$ 932, 934   
reduction to first-order sets 899, 956   
relaxation method 957, 964–970   
relaxation method, example of 971, 973–977   
Rosenbrock methods for stiff 934–940   
Runge-Kutta method 900, 907–921, 934, 942,   
1096   
Runge-Kutta method, high-order 907–910,   
912   
scaling stepsize to required accuracy 913, 914   
second order 928, 930   
semi-implicit differencing 934   
semi-implicit Euler method 934, 940   
semi-implicit extrapolation method 934, 935,   
940, 941   
semi-implicit midpoint rule 940   
shooting method 956, 959–961

shooting method, example 971, 977–981 similarity to Volterra integral equations 993 singular points 921, 962, 983, 984 solving with sinc expansions 178 step doubling 910 stepsize control 901, 910–920, 924, 929, 938, 941, 944, 946 stepsize, danger of too small 920 stiff 901, 931–941 stiff methods compared 941 stochastic simulation 946–954 Stoermer’s rule 928 see also Partial differential equations; Two-point boundary value problems Differentiation matrix 1091 routine for 1092 Diffusion equation 1024, 1043–1049, 1059 Crank-Nicolson method 1045, 1049, 1051, 1052 forward time centered space (FTCS) 1044, 1046, 1059 implicit differencing 1045 multidimensional 1051, 1052 Digamma function 267 Digital filtering see Filter Dihedral angle 1116 Dihedral group $D _ { 5 }$ 1174 Dimensionality, curse of 556, 891 Dimensions (units) 801 Diminishing increment sort 422 Dingbats, Zapf 1162 Dirac delta function 700, 987 Direct method see Periodogram Direct methods for linear algebraic equations 40 Direct product see Outer product of matrices Directed graph Markov model 856 stages and states 556, 850 transition matrix 856 transition probability 856 trellis 856 Viterbi decoding 850 Direction numbers, Sobol’s sequence 404 Direction of largest decrease 512 Direction set methods for minimization 489, 509–514 Dirichlet boundary conditions 1026, 1045, 1055, 1061, 1063 Discordant pair for Kendall’s tau 751 Discrete convolution theorem 642, 643 Discrete Fourier transform (DFT) 605–608 approximation to continuous transform 607, 608 see also Fast Fourier transform (FFT) Discrete optimization 536, 549 Discrete prolate spheroidal sequence (dpss) 662–667 Discretization error 173 Discriminant 227, 572 Dispersion 1036

DISPO see Savitzky-Golay filters   
Dissipation, numerical 1035   
Distance matrix 869   
Distributions, statistical see Statistical distributions   
Divergent series 210, 211, 216   
Divide-and-conquer method 589   
Division complex 226 integer vs. floating 8 multiple precision 1190 of polynomials 204, 464, 471   
dn function 316   
DNA sequence 559–562, 869, 884   
Do-while iteration 15   
Dogleg step methods 486   
Domain of integration 196   
Dominant solution of recurrence relation 220   
Dormand-Prince parameters 912, 920   
Dot - denotes matrix multiplication 37 denotes row or column sums 759   
Doub 25   
Double exponential error distribution 820   
Double root 443   
Doubling rate 756   
Downhill simplex method see Simplex, method of Nelder and Mead   
DP see Dynamic programming   
dpss (discrete prolate spheroidal sequence) 662–667   
Dual problem 538, 886   
Dual viewpoint, in multigrid method 1077   
Duality gap 538   
Duplication theorem, elliptic integrals 311   
DWT (discrete wavelet transform) see Wavelet transform   
Dynamic programming 555–562 Bellman-Dijkstra-Viterbi algorithm 556, 850 directed graph 556, 850   
e-folding rate 756   
Eardley’s equivalence class method 440   
Economization of power series 243–245   
Eigensystems 563–599 and integral equations 987, 992 balancing matrix 592, 594 bounds on eigenvalues 64 calculation of few eigenvectors or eigenvalues 568, 598 canned routines 567 characteristic polynomial 563, 583 completeness 564, 565 defective 564, 591, 598, 599 deflation 585 degenerate eigenvalues 563, 565 divide-and-conquer method 589 eigenvalues 563 elimination method 567, 594 factorization method 567 fast Givens reduction 578

generalized eigenproblem 568, 569   
Givens reduction 578–583   
Givens transformation 587   
Hermitian matrix 590   
Hessenberg matrix 567, 585, 590–595, 598   
Householder transformation 567, 578–584,   
587, 590, 594   
ill-conditioned eigenvalues 591, 592   
implicit shifts 586–589   
invariance under similarity transform 566   
inverse iteration 568, 584, 589, 597–599   
Jacobi transformation 567, 570–576, 578,   
590, 599   
left eigenvalues 565   
list of tasks 568   
Markov model transition matrix 858, 859   
MRRR algorithm 589, 599   
multiple eigenvalues 599   
nonlinear 568, 569   
nonsymmetric matrix 590–595   
operation count of balancing 592   
operation count of Givens reduction 578   
operation count of Householder reduction   
582   
operation count of inverse iteration 598, 599   
operation count of Jacobi method 573, 574   
operation count of $Q L$ method 585, 588   
operation count of $\boldsymbol { Q R }$ method for Hessenberg   
matrices 596   
operation count of reduction to Hessenberg   
form 594   
orthogonality 564   
polynomial roots and 469   
$Q L$ method 584–586, 590   
$\boldsymbol { Q R }$ method 67, 567, 571, 584–586   
$\boldsymbol { Q R }$ method for Hessenberg matrices 596   
real symmetric matrix 188, 576, 577, 582,   
992   
reduction to Hessenberg form 594, 595   
relation to singular value decomposition   
(SVD) 569, 570   
right eigenvalues 565   
shifting eigenvalues 563, 585, 596   
special matrices 568   
termination criterion 598, 599   
tridiagonal matrix 567, 576, 577, 583–589,   
598   
genvalue and eigenvector, defined 563   
igenvalue problem for differential equations   
958, 973, 977–981   
genvalues and polynomial root finding 469   
ISPACK 567   
lectromagnetic potential 631   
imination see Gaussian elimination   
lipse in confidence limit estimation 811, 814,   
815   
lliptic integrals 309–316, 1185   
addition theorem 310   
Carlson’s forms and algorithms 310–316   
Cauchy principal value 311

duplication theorem 311 Legendre 309, 314, 315 routines for 311–315 symmetric form 309, 310 Weierstrass 310   
Elliptic partial differential equations 1024 alternating-direction implicit method (ADI) 1065, 1066, 1185 analyze/factorize/operate package 1030 biconjugate gradient method 1030 boundary conditions 1026 comparison of rapid methods 1058 conjugate gradient method 1030 cyclic reduction 1054, 1057, 1058 Fourier analysis and cyclic reduction (FACR) 1053–1058 Gauss-Seidel method 1060, 1061, 1068, 1078 Jacobi’s method 1060, 1061, 1068 matrix methods 1028, 1030 multigrid method 1030, 1066–1083 rapid (Fourier) method 1029, 1054–1057 relaxation method 1028, 1059–1066 spectral methods 1096 successive over-relaxation (SOR) 1061–1066, 1070   
EM algorithm see Expectation-maximization algorithm   
Embedded networks 1168   
Embedded Runge-Kutta method 911, 936   
Encryption 358   
Entropy 754–761, 1006, 1176 chain rule 759 conditional 758–761 of data 1017 relative 756   
EOM (end of message) 1178, 1181   
epsilon () algorithm 212   
Equality constraints 526, 528   
Equations cubic 227–229, 461 differential see Differential equations normal (fitting) 768, 789–793, 1007 quadratic 10, 227–229 see also Differential equations; Partial differential equations; Root finding   
Equilibrium, physical 825   
Equivalence classes 419, 439–441   
Equivalence transformation 208   
Ergodic Markov model 858   
Ergodic property 825   
Error 8–12 checksums for preventing 1172 clocking 1172 discretization 173 double exponential distribution 820 in multigrid method 1067 interpolation 113 local truncation 1077, 1078 Lorentzian distribution 820 nonnormal 779, 812, 818–824 relative truncation 1077 roundoff 10, 11, 229, 1163, 1164 series, advantage of an even 165, 923 systematic vs. statistical 778 trimming 173 truncation 11, 173, 229, 500, 910, 911, 116 varieties of, in PDEs 1036–1038 see also Roundoff error   
Error-correcting codes 851–855 Berlekamp-Massey decoding algorithm 852 binary block code 851 codeword 851 correcting bit errors 855 coset leader 852 Golay code 852 Hamming code 852 Hamming distance 851, 1168 hard-decision decoding 853 linear codes 851 minimal trellis 853 parity-check matrix 851 perfect code 852 Reed-Solomon 852, 855 soft-decision decoding 853 syndrome 852 syndrome decoding 852 trellis 853, 856 turbo codes 855 Viterbi decoding 854, 855   
Error ellipse, how to draw 817, 847   
Error function 259, 264–266, 718 approximation via sampling theorem 718, 719 Chebyshev approximation 264 complex 302 Fisher’s z-transformation 747 inverse 264 relation to Dawson’s integral 302 relation to Fresnel integrals 298 relation to incomplete gamma function 264 routine for 264 significance of correlation 746 sum squared difference of ranks 750   
Error handling in programs 2, 30, 31, 35   
Estimation of parameters see Fitting; Maximum likelihood estimate   
Estimation of power spectrum 681–684   
Euclid 1098   
Euler equation (fluid flow) 1037   
Euler-Maclaurin summation formula 164, 167   
Euler’s constant 267, 269, 300   
Euler’s method for differential equations 900, 907, 931   
Euler’s transformation 211, 212   
Evaluation of functions see Function   
Even and odd parts, of continued fraction 208, 260, 267   
Even parity 1168   
Exception handling in programs 2, 30, 31, 35   
Expectation-maximization algorithm 842–844 expectation step (E-step) 843 for hidden Markov model 866 maximization step (M-step) 843 relation to Baum-Welch re-estimation 866   
Explicit differencing 1032   
Exponent in floating point format 8, 1164   
Exponential convergence 174–178, 180, 238, 239, 1083–1096   
Exponential integral 266–269 asymptotic expansion 269 continued fraction 267 recurrence relation 219 related to incomplete gamma function 267 relation to cosine integral 301 routine for $\operatorname { E i } ( x )$ 269 routine for $E _ { n } ( x )$ 268 series 267   
Exponential probability distribution 326, 327, 686 deviate from 362 relation to Poisson process 369, 829   
Extended midpoint rule 157, 161, 167   
Extended precision, use in iterative improvement 62   
Extended Simpson’s rule 160, 994, 997 three-eighths rule 995   
Extended trapezoidal rule 157, 159, 162, 167, 993 roundoff error 165   
Extirpolation (so-called) 690, 691   
Extrapolation 110–154 Bulirsch-Stoer method 922, 924 by linear prediction 673–681 differential equations 900 local 911 maximum entropy method as type of 683 polynomial 922, 924, 943 rational function 922 relation to interpolation 110 Romberg integration 166 see also Interpolation   
Extremization see Minimization   
$F$ -distribution probability function 332, 333 deviates 371   
F-test for differences of variances 728, 730   
FACR see Fourier analysis and cyclic reduction (FACR)   
Facsimile standard 1180   
Factorial evaluation of 210 relation to gamma function 256 representability 257 routine for 257 routine for log 258   
False position 449, 452, 454   
Family tree 440   
FAS (full approximation storage algorithm) 1076–1083

st Fourier transform (FFT) 608–616, 640, 11   
alternative algorithms 615, 616   
applications 640–719   
approximation to continuous transform 608   
bare routine for 611   
bit reversal 610, 638   
butterfly 360, 361, 610   
Clenshaw-Curtis quadrature 241   
convolution 616, 631, 641–647, 1189   
convolution of large data sets 646, 647   
Cooley-Tukey algorithm 616   
correlation 648, 649   
cosine transform 241, 624–627, 1056   
cosine transform, second form 625, 1057   
Danielson-Lanczos lemma 609, 610, 638   
data sets not a power of 2 616   
data smoothing 766, 767   
data windowing 655–667   
decimation-in-frequency algorithm 616   
decimation-in-time algorithm 615   
decomposition into blocks 614   
differentiation matrix using 1092   
discrete autocorrelation 649   
discrete convolution theorem 642, 643   
discrete correlation theorem 648   
double frequency 690   
endpoint corrections 694   
external storage 637, 638   
figures of merit for data windows 658   
filtering 667–672   
FIR filter 668, 669   
for quadrature 156   
for spherical harmonic transforms 296   
four-step framework 615   
Fourier integrals 692–699   
Fourier integrals,infinite range 699   
history 609   
IIR filter 668–672   
image processing 1010, 1012   
integrals using 156   
inverse of sine transform 623   
large data sets 637, 638   
leakage 655, 656   
Lomb periodogram and 689   
memory-local algorithm 638   
multidimensional 627–630   
multiple precision arithmetic 1185   
multiple precision multiplication 1189   
number-theoretic transforms 616   
of real data in 2D and 3D 631–637   
of real functions 617–627, 631–637   
of single real function 618–620   
of two real functions simultaneously 617, 6   
operation count 609, 610   
optimal (Wiener) filtering 649–652, 673, 67   
order of storage in 611   
parallel 614   
partial differential equations 1029,   
1054–1057   
periodicity of 608

periodogram 653–656, 681, 683 power spectrum estimation 652–667 related algorithms 615, 616 Sande-Tukey algorithm 616 sine transform 620–623, 1055 Singleton’s algorithm 637, 638 six-step framework 615 spectral methods 1086 treatment of end effects in convolution 643 treatment of end effects in correlation 648 Tukey’s trick for frequency doubling 690 two real functions simultaneously 617 use in smoothing data 766, 767 virtual memory machine 638 Winograd algorithms 616 zoom transforms 615 see also Discrete Fourier transform (DFT); Fourier transform; Spectral density Fast Legendre transform 295, 297 Fast multipole methods 140, 1150 FASTA (software) 562 Faure sequence 404 Fax (facsimile) Group 3 standard 1180 Feasible vector 526, 538 basis vector 528 Fermi-Dirac integral 178 FFT see Fast Fourier transform (FFT) Field, in data record 428 Figure-of-merit function 773 __FILE__ (ANSI C macro) 30 Fill-in, sparse linear equations 59, 76, 535, 544 Filon’s method 698 Filter 667–672 acausal 668 bilinear transformation method 670, 672 by fast Fourier transform (FFT) 637, 649, 667–672 causal 668, 767, 770 characteristic polynomial 670 data smoothing 766 digital 667–672 DISPO 767 finite impulse response (FIR) 642, 643, 668, 669 homogeneous modes of 670 infinite impulse response (IIR) 668–672, 681 Kalman 824 linear 668–672 low-pass for smoothing 766 nonrecursive 668 optimal (Wiener) 645, 649–652, 673, 674, 767 quadrature mirror 701, 708 realizable 668, 670, 671 recursive 668–672, 681 Remes exchange algorithm 669 Savitzky-Golay 232, 766–772 stability of 670, 671 time domain 667–672 Fine-to-coarse operator 1068

Finite difference equations (FDEs) 964, 970, 98 accuracy of 1085 alternating-direction implicit method (ADI) 1052, 1053, 1065, 1066 art, not science 1035 Cayley’s form for unitary operator 1049 Courant condition 1034, 1036, 1038, 1042 Courant condition (multidimensional) 1051 Crank-Nicolson method 1045, 1049, 1051, 1052 eigenmodes of 1033, 1034 explicit vs. implicit schemes 1033 forward Euler 1032 forward time centered space (FTCS) 1032, 1044, 1049, 1059 implicit scheme 1045 in relaxation methods 964 Lax method 1034–1036, 1042 Lax method (multidimensional) 1050, 1051 mesh drifting instability 1040 numerical derivatives 229 partial differential equations 1027 relation to spectral methods 1093 staggered leapfrog method 1038, 1039 two-step Lax-Wendroff method 1040 upwind differencing 1037, 1042 see also Partial differential equations   
Finite element methods 132, 1030   
Finite impulse response (FIR) 642, 643   
FIR (finite impulse response) filter 668, 669   
First-class objects 397   
Fisher discriminant algorithm 892   
Fisher’s z-transformation 746   
Fitting 773–838 basis functions 788 by Chebyshev approximation 234 by rational Chebyshev approximation 247–251 chi-square 778–780 confidence levels from singular value decomposition (SVD) 816, 817 confidence levels related to chi-square values 812–816 confidence limits on fitted parameters 807–817 covariance matrix not always meaningful 774, 812 degeneracy of parameters 797 exponential, an 797 freezing parameters in 791, 824 Gaussians, a sum of 805 general linear least squares 788–798 how much $\Delta \chi ^ { 2 }$ is significant 816 K–S test, caution regarding 740 Kalman filter 824 kriging 836–838 least squares 776–780 Legendre polynomials 797 Levenberg-Marquardt method 801–806, 1022 linear regression 780–785 Markov chain Monte Carlo 824–835 maximum likelihood estimation 777, 818 Monte Carlo simulation 740, 779, 807–810 multidimensional 798, 836–838 nonlinear models 799–806 nonlinear models, advanced methods 806 nonlinear problems that are linear 797 nonnormal errors 781, 812, 818–824 of sharp spectral features 682 polynomial 94, 129, 241, 243, 768, 788, 797 robust methods 818–824 standard (probable) errors on fitted parameters 781, 782, 786, 787, 790, 794, 795, 807–817 straight line 780–785, 822–824 straight line, errors in both coordinates 785–787 see also Error; Least-squares fitting; Maximum likelihood estimate; Robust estimation   
Five-point difference star 1071   
Fixed point format 8   
Fletcher-Powell algorithm see Davidon-Fletcher-Powell algorithm   
Fletcher-Reeves algorithm 489, 515–519   
Floating point format 8–11, 1163–1165 care in numerical derivatives 229, 230 in computational geometry 1098 enabling exceptions 35, 575 history 1163 IEEE 9, 10, 34, 1164 little- vs. big-endian 9 NaN 34, 35   
Flux-conservative initial value problems 1031–1043   
FMG (full multigrid method) 1067, 1072–1076   
for iteration 14   
Formats of numbers 8–11, 1163–1165   
Fortran 1 INTENT attribute 26   
Forward-backward algorithm as a sum-product algorithm 867 Bahl-Cocke-Jelinek-Raviv algorithm 867 belief propagation 867 compared to Viterbi decoding 867 hidden Markov model 861, 862, 864–867 renormalization 862   
Forward deflation 464, 465   
Forward difference operator 212   
Forward Euler differencing 1032   
Forward Time Centered Space see FTCS   
Four-step framework, for FFT 615   
Fourier analysis and cyclic reduction (FACR) 1054, 1058   
Fourier and spectral applications 600, 640–719   
Fourier integrals attenuation factors 698 endpoint corrections 694 tail integration by parts 699 use of fast Fourier transform (FFT) 692–699

urier series as basis functions for spectral   
methods 1085   
ourier transform 110, 600–640   
aliasing 606, 685   
approximation of Dawson’s integral 303   
autocorrelation 602   
basis functions compared 621   
contrasted with wavelet transform 699, 700,   
711   
convolution 602, 616, 617, 631, 641–647,   
1189   
correlation 602, 617, 648, 649   
cosine transform 241, 624–627, 1056   
cosine transform, second form 625, 1057   
critical sampling 605, 653, 655   
decomposition into blocks 614   
definition 600   
discrete Fourier transform (DFT) 233, 236,   
605–608   
Gaussian function 717, 718   
image processing 1010, 1012   
infinite range 699   
inverse of discrete Fourier transform 608   
method for partial differential equations   
1054–1057   
missing data 685   
missing data, fast algorithm 689–692   
Nyquist frequency 605, 607, 632, 653, 655,   
685   
optimal (Wiener) filtering 649–652, 673, 674   
Parseval’s theorem 602, 603, 608, 654   
power spectral density (PSD) 602, 603   
power spectrum estimation by FFT 652–667   
power spectrum estimation by maximum   
entropy method 681–684   
properties of 601   
sampling rate 605   
sampling theorem 605, 653, 655, 717–719   
scalings of 601   
significance of a peak in 686   
sine transform 620–623, 1055   
symmetries of 601   
uneven sampling, fast algorithm 689–692   
unevenly sampled data 685–692   
wavelets and 707, 708   
Wiener-Khinchin theorem 602, 674, 682   
see also Fast Fourier transform (FFT); Spectral   
density   
ractal region 462   
actional step methods 1052   
edholm alternative 987   
redholm equations 986   
eigenvalue problems 987, 992   
error estimate in solution 991   
first kind 986   
Fredholm alternative 987   
homogeneous vs. inhomogeneous 987   
homogeneous, second kind 991   
ill-conditioned 987   
infinite range 995

inverse problems 987, 1001–1006 kernel 986 nonlinear 988 Nystrom method 989–992, 995 product Nystrom method 995 second kind 987–992 subtraction of singularity 996 symmetric kernel 992 with singularities 995–1000 with singularities, worked example 999, 1000 see also Inverse problems   
Frequency domain 600   
Frequency spectrum see Fast Fourier transform (FFT)   
Frequentist, contrasted with Bayesian 774   
Fresnel integrals 297–300 asymptotic form 298 continued fraction 298 routine for 299 series 298   
Friday the 13th 7   
FSAL (first-same-as-last) 913   
FTCS (forward time centered space) 1032, 1044, 1049 stability of 1033, 1044, 1060   
Full approximation storage (FAS) algorithm 1076–1083   
Full conditional distribution 827   
Full moon 7   
Full multigrid method (FMG) 1067, 1072–1076   
Full Newton methods, nonlinear least squares 806   
Full pivoting 43   
Full weighting 1071   
Function Airy 254, 283, 289, 291 approximation 110, 233–239 associated Legendre polynomial 293, 971 autocorrelation of 602 bandwidth limited 605 Bessel 219, 254, 274–292 beta 258, 259 branch cuts of 252–254 chi-square probability 1003 complex 251 confluent hypergeometric 254, 287 convolution of 602, 617 correlation of 602, 617 Coulomb wave 254, 283 cumulative distribution (cdf) 320–339 Dawson’s integral 302, 304, 717 digamma 267 elliptic integrals 309–316, 1185 error 264–266, 298, 302, 718, 746, 750 error function 259 evaluation 201–254 evaluation by path integration 251–254, 318 exponential integral 219, 266–269, 301 factorial 256, 257 Fermi-Dirac integral 178

Fresnel integral 297–300 functor 21–23, 444, 459, 905 gamma 256, 257 hypergeometric 252, 318–320 incomplete beta 270–273 incomplete gamma 259–263, 732, 779 inverse cumulative distribution 320–339 inverse hyperbolic 227, 310 inverse incomplete gamma 263 inverse of $x \log ( x )$ 307–309, 335 inverse trigonometric 310 Jacobian elliptic 309, 316, 317 Kolmogorov-Smirnov probability 737, 763 Legendre polynomial 219, 293, 797 log factorial 258 logarithm 310 minimization 487–562 modified Bessel 279–283 modified Bessel, fractional order 287–289 object 21 path integration to evaluate 251–254 pathological 111, 445 probability 320–339 representations of 600 routine for plotting a 444 sine and cosine integrals 297, 300–302 sn, dn, cn 316, 317 spherical Bessel 283 spherical harmonics 292–297 spheroidal harmonic 971–981 statistical 320–339 templated 17, 22, 26 utility 17 virtual 33 Weber 254 unction object see Functor unctional iteration, for implicit equations 943 unctor 21–23, 202, 204, 237, 240, 444, 459, 660, 905, 936, 940 WHM (full width at half maximum) 659

solution of normal equations 790 storage requirements 44 Gauss-Kronrod quadrature 192, 195 Gauss-Laguerre integration 183, 995 Gauss-Legendre integration 183, 193 see also Gaussian integration Gauss-Lobatto quadrature 191, 192, 195, 241, 624, 1089 Gauss-Markov estimation 144 Gauss-Radau quadrature 191 Gauss-Seidel method (relaxation) 1060–1062, 1068 nonlinear 1078 Gauss transformation 310 Gaussian Hardy’s theorem on Fourier transforms 717 multivariate 378, 379, 842, 843, 847, 848, 1006, 1129, 1130 see also Gaussian (normal) distribution Gaussian (normal) distribution 341, 776, 778, 1004 central limit theorem 777 Cholesky decomposition of 847, 848 deviates from 364, 365, 368, 686 kurtosis of 723, 724 multivariate 813, 842 semi-invariants of 725 sum of 12 uniform 377 tails compared to Poisson 778 two-dimensional (binormal) 746 variance of skewness of 723 see also Normal (Gaussian) distribution Gaussian elimination 46–48, 65, 71 fill-in 59, 76, 535 in reduction to Hessenberg form 594 integral equations 993 operation count 47 relaxation solution of boundary value problems 966, 984 Gaussian integration 159, 179–193, 238, 296, 995, 997, 1086–1089 and orthogonal polynomials 181, 1087 calculation of abscissas and weights 182–188 discrete orthogonality relation 1087 error estimate in solution 991 exponential convergence of 180, 1089 extensions of 191–193, 1089 for integral equations 988, 990 from known recurrence relation 188, 189 Golub-Welsch algorithm for weights and abscissas 188 for incomplete beta function 271 for incomplete gamma function 260, 262 nonclassical weight function 189–191, 995 preassigned nodes 191 weight function $\log x$ 190, 191 weight functions 179–181, 995 Gaussian mixture model 842–848 Gaussian process regression 144, 836–838 Gear’s method (stiff ODEs) 934, 941

$^ { \mathrm { g + + } }$ 5   
Gambling 755–758, 760, 761   
Gamma function 256, 257 and area of sphere 1129 complex 257 incomplete see Incomplete gamma function   
Gamma probability distribution 331, 332 as limiting case of beta 333 deviates from 369 relation to Poisson process 829 sum rule for deviates 370   
Gauss-Chebyshev integration 180, 183, 187, 625   
Gauss-Hermite integration 183, 995 abscissas and weights 185 normalization 185   
Gauss-Jacobi integration 183 abscissas and weights 186   
Gauss-Jordan elimination 41–46, 75 operation count 47, 54   
Geiger counter 340   
Gene sequencing alignment algorithms 559–562 hidden Markov model 866   
Generalized eigenvalue problems 568, 569   
Generalized minimum residual method (GMRES) 89   
Genetic algorithms 840   
Geometric series 211, 214   
Geophysics, use of Backus-Gilbert method 1016   
Gerchberg-Saxton algorithm 1012   
Ghostscript 1161   
Gibbs sampler 827, 828 recommended for discrete distributions 828   
Gilbert and Sullivan 920   
Gillespie method 947   
Givens reduction 578–583, 587 fast 578 operation count 578   
Glassman, A.J. 229   
Global optimization 487, 488, 549–555, 774 continuous variables 552–554 difficulty of 803   
Globally convergent minimization 521–525 root finding 474, 477–486, 959, 960, 963   
GLPK (linear programming package) 536   
GMRES (generalized minimum residual method) 89   
GNU $\mathrm { C } { + } { + }$ compiler 5   
GNU Scientific Library 3   
Gnuplot 1162   
Godunov’s method 1043   
Golden mean (golden ratio) 11, 449, 494, 500   
Golden section search 443, 489, 496   
Goldman-Tucker theorem 539   
Golub-Welsch algorithm, for Gaussian quadrature 188   
Goodness-of-fit 773, 779, 782, 783, 787, 813 no good Bayesian methods 779, 1010   
Gram-Schmidt orthogonalization 105, 564, 565, 589, 598 SVD as alternative to 74   
Graphics, function plotting 444, 1160–1163   
Gravitational potential 631   
Gray code 405, 1160, 1166–1168   
Greenbaum, A. 90   
Gregorian calendar 6   
Grid square 132   
Gridding 150–154   
Group, dihedral 1174   
Guard digits 1164   
Half weighting 1071   
Halley’s method 263, 264, 271, 335, 463

Halton’s quasi-random sequence 404   
Hamming code 852   
Hamming distance 873   
error-correcting codes 851, 1168   
Hamming window 658

Hamming’s motto 443   
Hann window 657   
Hard-decision decoding 853 error correction 855   
Harmonic analysis see Fourier transform   
Harwell-Boeing format 83   
Hash collision strategy 387, 390 examples 396 function 352, 387–389 key 387 memory 392–397 multimap memory 394–397 table 386–392 of whole array 358–361   
Heap (data structure) 426, 434, 952, 1178   
Heapsort 420, 426–428, 434   
Helmholtz equation 1057   
Hermite interpolation 916   
Hermite polynomials 183, 185   
Hermitian matrix 564, 590   
Hertz (unit of frequency) 600   
Hessenberg matrix 105, 567, 585, 590–595, 598 QR algorithm 596 see also Matrix   
Hessian matrix 483, 510, 517, 521, 522, 799–801, 1011, 1020, 1021 is inverse of covariance matrix 802 second derivatives in 800, 801   
Hidden Markov model 856–868 backward estimate 861 Baum-Welch re-estimation 865–867 Bayesian nature of 868 Bayesian posterior probability 860, 861, 864 Bayesian re-estimation 864–866 compared to Viterbi algorithm 867, 868 convergence of Baum-Welch re-estimation 866 expectation-maximization algorithm 866 forward-backward algorithm 861, 862, 864–867 forward estimate 860 gene sequencing 866 hidden state 859 know intermediate states 864 missing data 864 observations 859 re-estimation of symbol probability matrix 865 re-estimation of transition probabilities 865 renormalization 862 speech recognition 866 symbols 859 trellis decoding 864 variations 864   
Hierarchical clustering 868–882   
Hierarchically band-diagonal matrix 716   
High-order not same as high-accuracy 112, 156, 238, 489, 500, 908, 911, 943   
High-pass filter 667   
Higher-order statistics 604   
Hilbert matrix 94   
Hilbert’s Third Problem 1127   
Histogram, variable-size bins 438   
Historic maximum entropy method 1022   
Hobson’s choice 704   
Homogeneous linear equations 69   
Hook step methods 486   
HOPDM (software) 548   
Hotelling’s method for matrix inverse 64, 716   
Householder transformation 67, 567, 578–584, 586, 587, 590, 594 in $\boldsymbol { Q R }$ decomposition 103 operation count 582   
Huffman coding 680, 713, 1160, 1175–1181   
Hull, convex 1097, 1132, 1146   
Hyperbolic functions, explicit formulas for inverse 227   
Hyperbolic partial differential equations 1024 advective equation 1032 flux-conservative initial value problems 1031–1043   
Hypergeometric function 252, 318–320 routine for 318, 319   
Hypothesis, null 720   
_I 26, 32, 36   
IBM bad random number generator 344 checksum 1174 radix base for floating point arithmetic 592   
ICF (intrinsic correlation function) model 1022   
Identity (unit) matrix 39   
Idioms 16   
IEEE floating point format 9, 10, 34, 257   
if structure 14 warning about nesting 14   
IIR (infinite impulse response) filter 668–672, 681   
Ill-conditioned integral equations 987   
Image processing 631, 1010 as an inverse problem 1010 cosine transform 625 fast Fourier transform (FFT) 631, 637, 1010 from modulus of Fourier transform 1012 maximum entropy method (MEM) 1016–1022 QO tree and 1150 wavelet transform 713, 715   
Implicit function theorem 442 pivoting 44 shifts in $Q L$ method 586–589   
Implicit differencing 1033 for diffusion equation 1045 for stiff equations 932, 933, 944   
Importance sampling, in Monte Carlo 411, 412, 414, 835, 836   
Improper integrals 167–172   
Impulse response function 641–643, 649, 668   
IMSL 3, 40, 76, 466, 470, 568   
IMT (Iri, Moriguti, Takasawa) rule 173   
In-place selection 439   
Include files 3, 4   
Incomplete beta function 270–273 for F-test 730 for Student’s t 729 routine for 273   
Incomplete gamma function 259–263 deviates from 369 for chi-square 732, 779 inverse 263   
Increment of linear congruential generator 343   
Incremental quantile estimation 435 changes with time 438   
Indentation of blocks 14   
Index table 419, 426, 428–431   
Inequality constraints 526, 528, 538   
Inference 840–898   
Information mutual 758–761 side 760, 761 theory 754–761   
Inheritance 23, 24 examples of in NR 23   
Initial value problems 900, 1024, 1026 see also Differential equations;   
Injection operator 1068   
inline directive 29   
Inscribed circle (incircle) 1112   
Instability see Stability   
Instantiation 18, 19   
Int, __int32, __int64 25   
Integer programming 536   
Integral equations 986–1023 adaptive stepsize control 995 block-by-block method 994 correspondence with linear algebraic equations 986 degenerate kernel 992 eigenvalue problems 987, 992 error estimate in solution 991 Fredholm 986, 989–992 Fredholm alternative 987 homogeneous, second kind 991 ill-conditioned 987 infinite range 995 inverse problems 987, 1001–1006 kernel 986 nonlinear 988, 994 Nystrom method 989–992, 995 product Nystrom method 995 solving with sinc expansions 178 subtraction of singularity 996 symmetric kernel 992 unstable quadrature 994 Volterra 988, 992–995 wavelets 989 with singularities 995–1000 with singularities, worked example 999, 10 see also Inverse problems   
Integral operator, wavelet approximation of 71 989   
Integration of functions 155–200 Chebyshev approximation 240, 241 cosine integrals 300 Fourier integrals 692–699 Fourier integrals, infinite range 699 Fresnel integrals 297 Gauss-Hermite 185 Gauss-Jacobi 186 Gauss-Laguerre 184 Gauss-Legendre 183 infinite ranges 176–178 integrals that are elliptic integrals 309 path integration 251–254 sine integrals 300 see also Quadrature   
Integro-differential equations 989   
INTENT attribute (Fortran) 26   
Interior-point method 85, 536–549 see also Linear Programming   
Intermediate value theorem 445   
Interpolation 110–154 Aitken’s algorithm 118 avoid in Fourier analysis 685 barycentric rational 113, 127, 128 bicubic 136–138 biharmonic 153 bilinear 133, 134 caution on high-order 112, 113 coefficients of polynomial 111, 129–131, 241, 243, 690 curve 139, 147 error estimates for 111 for computing Fourier integrals 694 for differential equation output 916 functions with poles 124 grid, on a 132–135 Hermite 916 inverse multiquadric 142 inverse quadratic 454, 496 irregular grid 139–149, 1097, 1141, 1142 kriging 144–147 Laplace/Poisson 150–154 minimum curvature 153 multidimensional 113, 132–135, 139–154 multigrid method, in 1070–1072 multiquadric 141 Neville’s algorithm 118, 231, 924 normalized radial basis functions 140 Nystrom 990 open vs. closed curve 148 operation count for 111 operator 1068 order of 112 ordinary differential equations and 113 oscillations of polynomial 112, 129, 489, 5 parabolic, for minimum finding 496–499

polynomial 110, 118–120, 231, 924 pseudospectral method and 1087 radial basis functions 139–144 rational Chebyshev approximation 247–251 rational function 110, 113, 124–128, 245, 275, 922 reverse (extirpolation) 690, 691 scattered data 139–154 Shepard’s method 140 spline 111, 120–124, 135 trigonometric 110 see also Fitting Intersection line and sphere 1121 line and triangle 1121 line segments 1118 lines 1117 QO tree used to find 1150 Intersections 1097 Interval variable (statistics) 741 Intrinsic correlation function (ICF) model 1022 Inverse function of $x$ $\log ( x )$ 307–309, 335 Inverse hyperbolic function 227, 310 Inverse iteration see Eigensystems stable equilibrium of Markov model 859 Inverse multiquadric 142 Inverse problems 987, 1001–1006 and integral equations 987 Backus-Gilbert method 1014–1016 Bayesian approach 1005, 1022 central idea 1005 constrained linear inversion method 1006 data inversion 1014 deterministic constraints 1011–1013 Gerchberg-Saxton algorithm 1012 in geophysics 1016 incomplete Fourier coefficients 1018, 1020 linear regularization 1006–1013 maximum entropy method (MEM) 1016–1022 MEM demystified 1019, 1020 optimally localized average 1014–1016 Phillips-Twomey method 1006 principal solution 1004 regularization 1002–1006 regularizing operator 1004 stabilizing functional 1004 Tikhonov-Miller regularization 1007 trade-off curve 1002, 1016 two-dimensional regularization 1010, 1011 use of conjugate gradient minimization 1011, 1020 use of convex sets 1011–1013 use of Fourier transform 1010, 1012 Van Cittert’s method 1011 Inverse quadratic interpolation 454, 496 Inverse response kernel, in Backus-Gilbert method 1014 Inverse trigonometric function 310 _IO 26, 32, 36

IQ (incremental quantile) agent 435   
Irreducibility of Markov model 858   
Irreducible polynomials modulo 2 382   
Irregular grid, interpolation on 139–149, 1141, 1142   
Is-a relationship 23   
ISBN (International Standard Book Number) checksum 1173   
Iterated integrals 196, 197   
Iteration 14 for linear algebraic equations 40 functional 943 in root finding 443 required for two-point boundary value problems 955–957 to improve solution of linear algebraic equations 61–65, 245   
Iteration matrix 1060   
Jacobi matrix, for Gaussian quadrature 188   
Jacobi transformation (or rotation) 105, 567, 570–576, 578, 590, 599 decorrelating random variables 380   
Jacobi’s method (relaxation) 1060, 1061, 1068   
Jacobian determinant 364, 981   
Jacobian elliptic functions 309, 316, 317   
Jacobian matrix 475, 477, 480, 483, 540, 935, 936 singular in Newton’s rule 486   
Java 1, 12   
Jenkins-Traub method 470   
Jordan curve theorem 1124   
JPEG-2000 standard 712   
Julian Day 3, 6   
Jump transposition errors 1174

two-dimensional 762–766 variants 738, 762 Kriging 139 fitting by 836–838 fitting not same as interpolation 838 interpolation by 144–147 is Gaussian process regression 837 linear prediction and 674, 679 nugget effect 838 Kuiper’s statistic 739 Kullback-Leibler distance 756–758 symmetrized 757 Kurtosis 723, 725

K-means clustering 848–850   
K-S test see Kolmogorov-Smirnov test   
Kalman filter 824   
Kaps-Rentrop method 934   
KD tree 1101–1110 construction of 1102–1106 number of boxes in 1102   
Kelly’s formula 758   
Kendall’s tau 749, 751–754   
Kernel 986 averaging, in Backus-Gilbert method 1014 degenerate 992 finite rank 992 inverse response 1014 separable 992 singular 995 symmetric 992   
Kernel methods of classification 840, 889, 892   
Keys used in sorting 428   
KKT (Karush-Kuhn-Tucker) conditions 539, 542, 886, 889   
Kolmogorov-Smirnov probability distribution 334–336   
Kolmogorov-Smirnov test 731, 736–738, 819   
L-estimate 818   
Lag 602, 648, 669   
Lagged Fibonacci generator 354   
Lagrange multiplier 758, 760, 1001   
Lagrange’s formula for polynomial interpolation 94, 118, 690, 691, 694, 1089, 1092   
Laguerre polynomials 183   
Laguerre’s method 444, 466–469 convergence 466   
Lanczos lemma 609, 610   
Lanczos method for gamma function 256   
Landen transformation 310   
LAPACK 40, 567   
Laplace’s equation 292, 1024 see also Poisson equation   
Laplace/Poisson interpolation 150–154   
Las Vegas 744   
Latin square or hypercube 409, 410   
Latitude/longitude in $n$ -dimensions 1128   
Laurent series 681, 682   
Lax method 1034–1036, 1042, 1050, 1051 multidimensional 1050, 1051   
Lax-Wendroff method 1040   
LCG see Linear congruential random number generator   
ldexp 207, 279, 283   
LDL 544, 548   
Ldoub 25   
Leakage in power spectrum estimation 655, 656, 658, 662–665   
Leakage width 658, 659   
Leapfrog method 1038, 1039   
Least-squares filters see Savitzky-Golay filters   
Least-squares fitting 776–798 degeneracies in 794, 795, 797 Fourier components 686 freezing parameters in 791, 824 general linear case 788–798 how much $\Delta \chi ^ { 2 }$ is significant 816 Levenberg-Marquardt method 801–806, 1022 Lomb periodogram 686 maximum likelihood estimator 777 method for smoothing data 768 multidimensional 798 nonlinear 486, 799–806, 1022 nonlinear, advanced methods 806 normal equations 768, 789–793, 1007 normal equations often singular 793, 797 optimal (Wiener) filtering 650 $\boldsymbol { Q R }$ method in 105, 791 rational Chebyshev approximation 249 relation to linear correlation 745, 783 Savitzky-Golay filter as 768 singular value decomposition (SVD) 39, 65–75, 249, 793 skewed by outliers 778 spectral analysis 686 standard (probable) errors on fitted parameters 794 weighted 777 see also Fitting   
Left eigenvalues or eigenvectors 564, 565   
Legendre elliptic integral see Elliptic integrals   
Legendre polynomials 183, 293 basis functions for spectral methods 1086 fitting data to 797 recurrence relation 219 see also Associated Legendre polynomials; Spherical harmonics   
Lehmer-Schur algorithm 470   
Lemarie’s wavelet 708   
Lentz’s method for continued fraction 207, 260   
Lepage, P. 414   
Leptokurtic distribution 723   
Levenberg-Marquardt algorithm 486, 801–806, 1022 advanced implementation 806   
Levin transformation 214   
Levinson’s method 96   
Liapunov stability 933   
Likelihood ratio 735, 757   
Limbo 457   
Limit cycle Laguerre’s method 466 Markov model 858   
Line 1097, 1117–1121 closest approach of two 1121 closest approach to point 1121 distance of point to 1118 equation satisfied by 1117 in 3 dimensions 1121 intersection of two 1117 intersection with sphere 1121 intersection with triangle 1121 left-of relations 1118 segments 1118–1120 skew 1121 _LINE__ (ANSI C macro) 30   
Line minimization see Minimization, along a ray   
Line search see Minimization, along a ray   
Linear algebraic equations 37–109 and integral equations 986, 990 band-diagonal 58–61 biconjugate gradient method 88 Cholesky decomposition 100–102, 378, 379, 525, 543, 568, 791 complex 55 computing A-1 - B 53 conjugate gradient method 87–92, 716 cyclic tridiagonal 79, 80 direct methods 40, 76 Gauss-Jordan elimination 41–46 Gaussian elimination 46, 48 Hilbert matrix 94 Hotelling’s method 64, 716 iterative improvement 61–65, 245, 548 iterative methods 40, 87–92 large sets of 38, 39 least-squares solution 65, 70, 73, 249, 793 $_ { L U }$ decomposition 48–55, 245, 483, 484, 486, 534, 936, 990, 1008 nonsingular 38, 39 overdetermined 39, 249, 793, 1004 parallel solution 57 partitioned 81 QR decomposition 102–106, 483, 484, 486, 791 row vs. column elimination 45, 46 Schultz’s method 64, 716 Sherman-Morrison formula 76–79, 94, 534 singular 38, 69, 73, 249, 793 singular value decomposition (SVD) 65–75, 249, 793, 1003 sparse 39, 58, 75–92, 534, 544, 548, 937, 1011 summary of tasks 39, 40 Toeplitz 93, 96–99, 245 Vandermonde 93–96, 130 wavelet solution 715, 716, 989 Woodbury formula 80, 81, 94 see also Eigensystems   
Linear codes 851   
Linear congruential random number generator 341, 343, 348   
Linear constraints 526, 530   
Linear convergence 448, 495   
Linear correlation (statistics) 745–748   
Linear dependency constructing orthonormal basis 74, 105 in linear algebraic equations 38 of directions in $N$ -dimensional space 511   
Linear equations see Differential equations; Integral equations; Linear algebraic equations   
Linear feedback shift register (LFSR) 346, 380–386 state vector 380 update rule 380   
Linear inversion method, constrained 1006   
Linear optimization 526   
Linear prediction 673–681 characteristic polynomial 676 coefficients 673–681 compared with regularization 1008 contrasted to polynomial extrapolation 675, 677 is Gaussian process regression 837

kriging and 144   
multidimensional 836–838   
related to optimal filtering 673, 674   
removal of bias in 145, 678, 679   
stability 676   
near predictive coding (LPC) 679–681   
near programming 488, 526–549   
affine scaling 543   
artificial variables 530, 531   
augmented equations 543, 548   
auxiliary objective function 530   
barrier method 541   
basic variables 529, 531   
boundary 528   
bounded variables 535, 546   
centering parameter 541   
central path 540   
complementarity condition 539   
complementary slackness theorem 539   
constraints 526, 530   
cycling 534   
degenerate basis 533   
Devex 535   
dual algorithm 535   
dual feasible basis vector 538   
dual interior-point method 542   
dual problem 538, 539   
duality gap 538   
duality measure 541   
efficiency 537, 541   
ellipsoid method 537   
equality constraints 526, 528   
feasible basis vector 528, 529, 532   
feasible vector 526, 538   
free variables 538   
fundamental theorem 528   
Goldman-Tucker theorem 539   
inequality constraints 526, 528, 538   
infeasible method 537   
interior-point method 85, 488, 536–549   
KKT conditions 539, 542   
logical variables 530, 538   
long-step method 541   
minimum ratio test 532   
multiple pricing 535   
nonbasic variables 529, 531   
normal equations 85, 543, 548   
objective function 526, 528, 530   
optimal feasible vector 526, 528, 532   
path-following method 541   
phases one and two 530   
predictor-corrector method 547   
primal algorithm 535   
primal-dual interior-point method 542   
primal-dual solution 539   
primal interior-point method 542   
primal problem 538   
reduced cost 531   
scaling of variables 535, 546   
short-step method 541

simplex method 488, 502, 526–536, 548 simplex vs. interior-point 548 slack variables 529, 531, 535, 538, 547 sparse linear algebra 534, 544, 548 stalling 534 standard form 529, 530, 538 steepest edge pricing 535 strict complementarity 539 strong duality theorem 539 structural variables 530 surplus variables 529 unbounded objective function 532, 538 vertex of simplex 528, 531 weak duality theorem 538 worked example 530–533 zero variables 530   
Linear regression 780–787 see also Fitting   
Linear regularization 1006–1013   
Linearly separable data 884   
LINPACK 40, 567   
Little-endian 9, 34   
Llong 25   
Local extrapolation 911, 914   
Local extremum 487, 551   
Localization of roots see Bracketing   
Log-sum-exp formula 844   
Logarithmic function 310 barrier function 541 inverse of $x$ log.x/ 307–309, 335   
Logistic probability distribution 324–326 deviates from 363   
Lognormal probability distribution 328, 329, 827   
Lomb periodogram method of spectral analysis 685–687 fast algorithm 689–692   
long long int 25   
Loops 14   
Lorentzian distribution 322   
Lorentzian probability distribution 820   
Low-pass filter 667, 766   
LP coefficients see Linear prediction   
LPC (linear predictive coding) 679–681   
lp solve 535, 536   
$_ { L U }$ decomposition 48–55, 62, 65, 71, 75, 108, 475, 534, 790, 936 band-diagonal matrix 59 Bartels-Golub update 535 complex equations 55 Crout’s algorithm 49, 59 fill-in, minimizing 535 for ${ \bf A } ^ { - 1 }$ - B 53 for integral equations 990 for inverse iteration of eigenvectors 598 for inverse problems 1008 for matrix inverse 54 for nonlinear sets of equations 475, 486 for Pade approximant 245 ´ for Toeplitz matrix 98 operation count 49, 54

pivoting 50, 535 repeated backsubstitution 54, 60 solution of linear algebraic equations 54 solution of normal equations 790 stable equilibrium of Markov model 859 threshold partial pivoting 535 Lucifer (encryption algorithm) 358 Lucy’s $Y ^ { 2 }$ and $Z ^ { 2 }$ statistic 735 LUSOL 535

M-estimates 818 how to compute 821, 822 local 819–821 see also Maximum likelihood estimate   
Machine accuracy 10, 1163   
Machine learning 840 supervised 883 support vector machine 883–898 unsupervised 842, 868   
Macintosh, see Apple Macintosh   
Maehly’s procedure 465, 472   
Magic in MEM image restoration 1019, 1020 in Pade approximation 246, 247 ´   
Mantissa in floating point format 8–10, 1164   
Mantissa in floating-point format 1189   
Maple (software) 3   
Marginals 743, 759, 825   
Markov chain 825   
Markov chain Monte Carlo 551, 774, 824–836 acceptance probability 827, 832 best stepsize 832 burn-in 826, 833–835 candidate point 827 compared to Monte Carlo integration 825 convergence diagnostics 835 converges to sample, not population, values 834 correlated directions 831 correlation time 834 detailed balance equation 825, 827 ergodic average 834 ergodic behavior 825 fitting model parameters 825 full conditional distributions 827 Gibbs sampler 827, 828 and inverse problems 1006 lognormal steps 827 Metropolis-Hastings algorithm 826, 827 normalizing constant 825, 828, 835, 836 parallel computing 835 parameter uncertainties 833 proposal distribution 826–828, 835 proposal generator 830 rapid mixing 826, 831 variable dimension models 835   
Markov model 856–868 aperiodic 858 as ensemble 857 convergence 858 corrected phylogenetic distance for 873 diagnosing 858, 859 directed graph 856 equilibrium distribution 857 ergodic 858 evolution in time 857 hidden 856–868 inverse iteration 859 irreducible 858 limit cycle 858 $_ { L U }$ decomposition 859 multiple equilibria 859 population vector 857 transition matrix 856 transition probability 856 unstable equilibria 858, 859   
Markowitz criterion 535   
Marquardt method (least-squares fitting) 801–806, 1022   
Mass, center of 399, 400   
MasterCard checksum 1174   
MatDoub , MatInt, etc. 26   
Mathematica (software) 1, 3   
Mathematical Center (Amsterdam) 454   
Matlab 1, 3   
Matrix 37, 38 approximation of 74, 75, 715 band-diagonal 56, 58–61, 76 band triangular 76 banded 40, 568 bidiagonal 67 block diagonal 76, 964, 966 block triangular 76 block tridiagonal 76 bordered 76 characteristic polynomial 563, 583 Cholesky decomposition 100–102, 378, 379, 525, 543, 568, 791 class for 24–29 column augmented 42, 43 complex 55 condition number 69, 89 curvature 800 cyclic banded 76 cyclic tridiagonal 79, 80 defective 564, 591, 598, 599 of derivatives see Hessian matrix; Jacobian determinant design (fitting) 768, 788 determinant of 39, 54, 55 diagonalization 566 distance 869 elementary row and column operations 42, 43 finite differencing of partial differential equations 1027 Hermitian 564, 568, 590 Hermitian conjugate 564 Hessenberg 105, 567, 585, 590–596, 598 Hessian see Hessian matrix hierarchically band-diagonal 716

Hilbert 94   
identity 39   
ill-conditioned 69, 71, 130, 131   
indexed storage of 82–87   
integral equations and 986, 990   
inverse 39, 41, 47, 54, 76, 78, 81, 82,   
106–108, 565   
inverse by Hotelling’s method 64, 716   
inverse by Schultz’s method 64, 716   
inverse multiplied by a matrix 53   
inverse, approximate 63   
iteration for inverse 63–65, 716   
Jacobi rotation 573   
Jacobi transformation 567, 570–576, 578   
Jacobian 935, 936   
logical multiplication 949   
lower triangular 48, 100, 988   
Moore-Penrose inverse 70   
multiplication denoted by dot 37   
multiplication, optimizing order of 558, 559   
norm 64   
normal 564, 565   
nullity 67, 68   
nullspace 39, 67–70, 72, 563, 1002   
orthogonal 103, 564, 579, 703, 1130   
orthogonal transformation 566, 578, 584   
orthonormal basis 74, 105   
outer product denoted by $\otimes$ 78, 523   
partitioning for determinant 82   
partitioning for inverse 81, 82   
positive-definite 40, 100, 543, 791   
pseudoinverse 70, 73   
$\boldsymbol { Q R }$ decomposition 102–106, 483, 484, 486,   
791   
range 67, 68   
rank 67   
rank-nullity theorem 68   
residual 63   
responsibility 842   
rotation 1097, 1130, 1131   
row and column indices 38   
row vs. column operations 45, 46   
self-adjoint 564, 565   
similarity transform 566, 567, 570, 592, 594   
singular 69, 71, 73, 563   
singular value decomposition 39, 65–75,   
1003   
sparse 39, 75–92, 534, 544, 548, 715, 937,   
964, 966, 1011   
special forms 40   
splitting in relaxation method 1060   
spread 1015   
storage schemes in $\mathrm { C } { + } { + }$ 38   
suffix _I, _O, _IO 26, 32, 36   
symmetric 40, 100, 563, 565, 568, 571,   
576–583, 992   
Toeplitz 93, 96–99, 245   
transpose of sparse 85   
triangular 567

tridiagonal 40, 56–61, 75, 76, 78, 122, 188, 576–589, 598, 1045, 1057, 1058, 1066 tridiagonal with fringes 1028 unitary 564 updating 105, 106, 484 upper Hessenberg 594 upper triangular 48, 103 Vandermonde 93–96, 130 see also Eigensystems; NRmatrix   
Matrix equations see Linear algebraic equations   
Matterhorn 723   
MAX utility function 17   
Maximization see Minimization   
Maximum entropy method (MEM) 681–684, 1006 algorithms for image restoration 1020 Bayesian 1022 Cornwell-Evans algorithm 1021 demystified 1019, 1020 for inverse problems 1016–1022 historic vs. Bayesian 1022 image restoration 1016–1022 intrinsic correlation function (ICF) model 1022 operation count 683 see also Linear prediction   
Maximum likelihood compared with probability 854 trellis decoding 854   
Maximum likelihood estimate (M-estimates) 812, 818 chi-square test 812 defined 777 how to compute 821, 822 mean absolute deviation 820, 822 relation to least squares 777   
Maxwell’s equations 1032   
MCMC see Markov chain Monte Carlo   
Mean absolute deviation of distribution 723, 820 related to median 822   
Mean value theorem 151   
Mean(s) of distribution 722, 723, 725 statistical differences between two 726–730   
Measurement errors 773   
Median 419 by selection 822 calculating 432 changes with time 438 incremental estimation 435 as L-estimate 818 of distribution 722, 725, 726 role in robust straight line fitting 822   
Median-of-three, in Quicksort 423   
MEM see Maximum entropy method (MEM)   
Memory, using scope to manage 20   
Merit function 773 for inverse problems 1004 for straight line fitting 781, 822 for straight line fitting, errors in both coordinates 785 in general linear least squares 788 nonlinear models 799   
Mesh-drift instability 1040   
Mesh generation 1150   
Mesokurtic distribution 723   
Message 754   
Method of lines 1095   
Method of regularization 1006   
Metropolis algorithm 550, 552, 825   
Metropolis-Hastings algorithm 551, 826, 827 Gibbs sampler as special case 827   
Microsoft integer types 26 NaN handling poor 35 Visual $\mathrm { C } { + } { + }$ 5 Windows 5   
Midpoint method see Modified midpoint method; Semi-implicit midpoint rule   
Mikado, or the Town of Titipu 920   
Miller’s algorithm 221, 278   
Min-sum algorithm dynamic programming 556 Viterbi decoding 867   
MIN utility function 17   
Minimal solution of recurrence relation 220, 221   
Minimal trellis 853   
Minimax polynomial 235, 248 rational function 248, 249   
Minimization 487–562 along a ray 88, 478, 489, 507–509, 511, 512, 519–521, 524, 540 annealing, method of simulated 487, 488, 549–555 bracketing of minimum 490–496, 503 Brent’s method 489, 496–500, 785 Broyden-Fletcher-Goldfarb-Shanno algorithm 490, 521–525 by searching smaller subspaces 1021 chi-square 778–780, 799 choice of methods 488–490 combinatorial 549 conjugate gradient method 489, 515–520, 1011, 1020 convergence rate 495, 511 Davidon-Fletcher-Powell algorithm 490, 521, 522 degenerate 1002 direction set methods 489, 509–514 downhill simplex method 489, 502–507, 552, 821 finding best-fit parameters 773 Fletcher-Reeves algorithm 489, 515–519 functional 1001, 1002 global 487, 552–554, 774 globally convergent multidimensional 521–525 golden section search 492–496 in nonlinear model fitting 799 KKT conditions 539, 542 line methods 507–509 linear 526 multidimensional 502–525 of path length 555–562 Polak-Ribiere algorithm 489, 517 Powell’s method 489, 502, 509–514 quasi-Newton methods 477, 489, 521–525 root finding and 476, 477 scaling of variables 523 steepest descent method 516, 1011 termination criterion 493, 503 use for sparse linear systems 87, 89 use in finding double roots 443 using derivatives 489, 499–502 variable metric methods 489, 521–525 see also Linear programming   
Minimum curvature method 153   
Minimum residual method, for sparse system 89   
Minimum spanning tree 1147   
MINPACK 806   
Missing data 150–154, 685 in hidden Markov model 864   
Mississippi River 552, 555   
Mixture model, Gaussian 842–848   
Mixture weight 843   
Mode of distribution 722, 725, 726   
Model-trust region 486, 806   
Modeling of data see Fitting   
Modes, homogeneous, of recursive filters 670   
Modified Bessel functions see Bessel functions   
Modified Lentz’s method, for continued fractions 208   
Modified midpoint method 922, 923   
Modified moments 190   
Modulation, trellis coded 855   
Modulus of linear congruential generator 343   
Moments and quadrature formulas 996 filter that preserves 768 modified problem of 190 of distribution 721–726 problem of 94 semi-invariants 725   
Monic polynomial 181   
Monotonicity constraint, in upwind differencing 1042   
Monte Carlo 197, 341, 397–418 adaptive 410–418 and Kolmogorov-Smirnov statistic 740, 762, 764 bootstrap method 809, 810 comparison of sampling methods 412–414 importance sampling 411, 412, 414, 835, 836 integration 156, 197, 397–403, 410–418 integration compared to MCMC 825 integration, recursive 416 integration, using Sobol’ sequence 408, 409 integration, VEGAS algorithm 414–416 Markov chain 774, 824–836 partial differential equations 1030 quasi-random sequences in 403–410 quick and dirty 809, 810 recursive 410–418 significance of Lomb periodogram 686, 687 simulation of data 779, 807–810, 812 stratified sampling 412–414, 416   
Moore-Penrose inverse 70   
Mother functions 700   
Mother Nature 807, 809   
Moving average (MA) model 681   
Moving window averaging 767   
MRRR algorithm (Multiple Relatively Robust Representations) 589, 599   
Muller’s method 466, 473   
Multidimensional confidence levels of fitting 810, 812, 814, 816 data, use of binning 741 fitting 798, 836–838 Fourier transform 627–630 Fourier transform, real data 631–637 initial value problems 1049–1053 integrals 156, 196–199, 398, 410 interpolation 132–135, 139–154 Kolmogorov-Smirnov test 762–766 minimization 502–525 Monte Carlo integration 397–403, 410 normal (Gaussian) distribution 813 partial differential equations 1049–1053, 1083, 1095 root finding 442–486, 956, 959, 960, 963, 964 search using quasi-random sequence 404 secant method 474, 483 wavelet transform 712, 713   
Multigrid method 1030, 1066–1083 avoid SOR 1070 boundary conditions 1072 choice of operators 1071 coarse-grid correction 1068 coarse-to-fine operator 1068 cycle 1069 dual viewpoint 1077 fine-to-coarse operator 1068 full approximation storage (FAS) algorithm 1076–1083 full multigrid method (FMG) 1067, 1072–1076 full weighting 1071 Gauss-Seidel relaxation 1069 half weighting 1071 importance of adjoint operator 1071 injection operator 1068 interpolation operator 1068 line relaxation 1070 local truncation error 1077, 1078 Newton’s rule 1077, 1079 nonlinear equations 1077 nonlinear Gauss-Seidel relaxation 1078 odd-even ordering 1070, 1073

operation count 1067 prolongation operator 1068 recursive nature 1069 relative truncation error 1077 relaxation as smoothing operator 1069 restriction operator 1068 speeding up FMG algorithm 1076 stopping criterion 1078 straight injection 1071 symbol of operator 1070, 1071 use of Richardson extrapolation 1072 V-cycle 1069 W-cycle 1069 zebra relaxation 1070 Multiple precision arithmetic 1185–1193 Multiple roots 443, 464 Multiplication complex 225 multiple precision 1188 Multiplicative linear congruential generator (MLCG) 341, 344, 348, 349 Multiplier of linear congruential generator 343 Multiply-with-carry (MWC) 347 Multipole methods, fast 140, 1150 Multiquadric 141 Multistep and multivalue methods (ODEs) 900, 942–946 see also Differential Equations; Predictor-corrector methods Multitaper methods 662–665 Multivariate normal deviates 378, 379 distribution 813, 847, 848 Murphy’s Law 509 Mutual information 758–761

NAG 3, 40, 76, 568   
Namespace, why no NR 36   
NaN (not-a-number) 34, 35 how to set and test 34 isnan 35 quiet vs. signalling 35   
Nat 755, 756, 760, 761   
Natural cubic spline 122   
Navier-Stokes equation 1035   
Nearest neighbor 1097, 1101–1110, 1146 all points within specified radius 1109 Delaunay edges connect 1146   
Needle, eye of (minimization) 503   
Needleman-Wunsch algorithm 559   
Negation, multiple precision 1186   
Negentropy 1017–1019   
Neighbor-joining (NJ) method 873, 878–882   
Nelder-Mead minimization method 489, 502–507   
Nested iteration 1072   
Netlib 3   
Networks 1168   
Neumann boundary conditions 1026, 1045, 1056, 1057, 1063   
Neural networks 840, 883   
Neutrino 762   
Neville’s algorithm 118, 125, 166, 231   
Newton-Cotes formulas 158, 179 open 158, 159   
Newton-Raphson method see Newton’s rule   
Newton’s rule 182, 229, 443, 444, 456–462, 46 466, 470, 584 caution on use of numerical derivatives 459 extended by Halley 463 first published by Raphson 456 for interior-point method 539 for matrix inverse 64, 716 for reciprocal of number 1190 for square root of number 1191 fractal domain of convergence 462 globally convergent multidimensional 474, 477–486, 959, 960, 963 in multidimensions 472–476, 959, 960, 96 964 in nonlinear multigrid 1077, 1079 nonlinear Volterra equations 994 safe 460 scaling of variables 484 singular Jacobian 486 solving stiff ODEs 943, 944 with backtracking 478–483   
Next reaction method 952   
Niederreiter sequence 404   
NIST-STS, for random number tests 345   
NL2SOL 806   
Noise bursty 1168 effect on maximum entropy method 683 equivalent bandwidth 658 fitting data that contains 770, 773 model, for optimal filtering 651   
Nominal variable (statistics) 741   
Non-interfering directions see Conjugate directions   
Nonexpansive projection operator 1012   
Nonlinear eigenvalue problems 568, 569   
Nonlinear equations finding roots of 442–486 in MEM inverse problems 1018 integral equations 988, 994 multigrid method for elliptic PDEs 1077   
Nonlinear instability 1037   
Nonlinear programming 536   
Nonnegativity constraints 526, 527 barrier function 541   
Nonparametric statistics 748–754   
Nonpolynomial complete (NP-complete) 551   
Nordsieck method 944   
Norm, of matrix 64   
Normal (Gaussian) distribution 320, 321, 341, 776, 778, 805, 1004 central limit theorem 777 deviates from 364, 365, 368, 377, 686 kurtosis of 723, 724

multivariate 378, 379, 813, 842, 843, 847, 848, 1006, 1129, 1130 semi-invariants of 725 sum of 12 uniform 377 tails compared to Poisson 778 two-dimensional (binormal) 746 variance of skewness of 723 see also Gaussian (normal) distribution Normal equations (fitting) 40, 768, 789–793, 1002, 1007 often are singular 793 Normal equations (interior-point method) 85, Normalization normalizing constant 825, 828, 835, 836 of Bessel functions 221 of floating-point representation 9 of functions 181, 973 of modified Bessel functions 282 Normalized Radial Basis Functions 140 Not a Number see NaN Notch filter 667, 671 NP-complete problem 551 NR::, why missing in 3rd ed. 36 nr3.h file 3, 4, 17, 28–30, 34–36 NRmatrix 26, 28, 29 bounds checking 35 instrumenting 36 methods in 27 NRvector 26, 28, 29 bounds checking 35 instrumenting 36 methods in 27 Nugget effect 838 different from measurement error 838 Null hypothesis 720 Nullity 67, 68 Nullspace 39, 67–70, 72, 563, 1002 Number-theoretic transforms 616 numeric_limits 10, 34 Numerical derivatives 178, 229–232, 769 Numerical integration see Quadrature Numerical Recipes bugs in 5 compilers tested 5 cookbook, not menu 3 dependencies 4 electronic versions 5 how to use routines in 3 is not a program library 2, 18 is not a programming text 2 machines tested 5 obtaining source code 3 types 25 webnotes 4 Nyquist frequency 605, 607, 632, 653, 655, 685–687, 693 Nystrom method 989–992, 995 product version 995 _O 26, 32, 36

Object 17–24 avoid copying large 36 constructor 18, 27 definition 18 destruction 20, 21 functor 21–23 grouping related functions 18 hides internal structure 17 inheritance 23, 24 instantiation 18, 19 multiple instances of 20 returning multiple values via 19 saving internal state 20 simple uses of 18–20 standardizing an interface 19 struct vs. class 17 see also Class   
Object-oriented programming (OOP) 17–21, 23   
Objective function 526, 528, 530   
Oblateness parameter 971   
Octave (software) 3   
Octree see QO tree   
Odd-even ordering in Gauss-Seidel relaxation 1070, 1073 in successive over-relaxation (SOR) 1064   
Odd parity 1168   
Odds ratio 757   
ODE see Differential equations   
One-sided power spectral density 602   
OOP see Object-oriented programming   
Operation count balancing 592 Baum-Welch re-estimation of hidden Markov model 865 Bessel function evaluation 278 bisection method 448 Cholesky decomposition 100 coefficients of interpolating polynomial 130 complex multiplication 108 cubic spline interpolation 122 evaluating polynomial 203 fast Fourier transform (FFT) 609, 610 Gauss-Jordan elimination 47, 54 Gaussian elimination 47 Givens reduction 578 Householder reduction 582 interpolation 111 inverse iteration 598, 599 iterative improvement 63 Jacobi transformation 573, 574 Kendall’s tau 752 $_ { L U }$ decomposition 49, 54 Markov model diagnosis 858 matrix inversion 108 matrix multiplication 107 maximum entropy method 683 multidimensional minimization 515 multigrid method 1067 multiplication 1188, 1190 polynomial evaluation 108, 203 QR decomposition 103, 105 $\boldsymbol { Q R }$ method for Hessenberg matrices 596 reduction to Hessenberg form 594 selection by partitioning 433 sorting 420, 422, 423 Toeplitz matrix 93 Vandermonde matrix 93   
Operator precedence, in $\mathrm { C } { + } { + }$ 12 splitting 1028, 1052, 1053, 1065   
Optimal (Wiener) filtering 645, 649–652, 673, 674, 767 compared with regularization 1008   
Optimal feasible vector 526, 528   
Optimally Localized Average (OLA) 1014–1016   
Optimization see Minimization   
Options, financial 329   
Ordinal variable (statistics) 741   
Ordinary differential equations see Differential equations   
Orthogonal see Orthonormal functions; Orthonormal polynomials   
Orthogonal transformation 566, 578, 584, 699   
Orthonormal basis, constructing 74, 105   
Orthonormal functions 181, 292   
Orthonormal polynomials and Gaussian quadrature 181, 1087 Chebyshev 183, 187, 233 construct for arbitrary weight 189–191 Gaussian weights from recurrence 188, 189 Hermite 183 in Gauss-Hermite integration 185 Jacobi 183 Laguerre 183 Legendre 183 weight function log x 190, 191   
Orthonormality 66, 68, 70, 181, 579   
Out-of-band signaling 1178   
Outer product of matrices (denoted by $\otimes$ ) 78, 523   
Outgoing wave boundary conditions 1026   
Outlier 723, 778, 779, 781, 818, 821 see also Robust estimation   
Overcorrection 1061, 1062   
Overflow 1164 in complex arithmetic 225, 226   
Overlap-add and overlap-save methods 646, 647   
Overrelaxation parameter 1062 choice of 1062–1064   
$p$ -value test 720   
Packet-switched networks 1168   
Pade approximant 125, 212, 245–247 ´   
Parabolic interpolation 496, 497   
Parabolic partial differential equations 1024, 1043   
Parallel axis theorem 413   
Parallel programming cyclic reduction 224

FFT 614   
polynomial evaluation 205   
recurrence relations 223, 224   
recursive doubling 223   
tridiagonal systems 57   
rameters in fitting function 776–780, 807–817   
rentheses, annoying 12   
rity bit 1168   
rity-check matrix 851   
rseval’s theorem 602, 603, 654   
discrete form 608   
rsimony, maximum 882   
rtial abstraction 24   
rtial differential equations 1024–1096   
advective equation 1032   
alternating-direction implicit method (ADI)   
1052, 1053, 1065, 1066   
amplification factor 1033, 1038   
analyze/factorize/operate package 1030   
artificial viscosity 1037, 1042   
biconjugate gradient method 1030   
boundary conditions 1025   
boundary value problems 1025–1030,   
1053–1058   
Cauchy problem 1024   
Cayley’s form 1049   
characteristics 1024–1026   
Chebyshev acceleration 1064   
classification of 1024–1030   
comparison of rapid methods 1058   
conjugate gradient method 1030   
Courant condition 1034, 1036, 1038–1040,   
1042   
Courant condition (multidimensional) 1051   
Crank-Nicolson method 1045, 1047, 1049,   
1051, 1052   
cyclic reduction (CR) method 1054, 1057,   
1058   
diffusion equation 1024, 1043–1049, 1051,   
1052, 1059   
Dirichlet boundary conditions 1026, 1045,   
1055, 1061, 1063   
elliptic, defined 1024   
error, varieties of 1036–1038   
explicit vs. implicit differencing 1033   
FACR method 1058   
finite difference method 1027   
finite element methods 1030   
flux-conservative initial value problems   
1031–1043   
forward Euler differencing 1032   
forward time centered space (FTCS) 1032,   
1044, 1049, 1059   
Fourier analysis and cyclic reduction (FACR)   
1053–1058   
Gauss-Seidel method (relaxation) 1060,   
1061, 1068, 1078   
Godunov’s method 1043   
Helmholtz equation 1057   
high-order methods, caution on 1050   
hyperbolic 1024, 1031   
implicit differencing 1045   
inhomogeneous boundary conditions 1055   
initial value problems 1024, 1026   
initial value problems, recommendations on   
1042   
Jacobi’s method (relaxation) 1060, 1061,   
1068   
Laplace’s equation 1024   
Lax method 1034–1036, 1042, 1050, 1051   
Lax method (multidimensional) 1050, 1051   
matrix methods 1028, 1030   
mesh drift instability 1040   
Monte Carlo methods 1030   
multidimensional initial value problems   
1049–1053   
multigrid method 1029, 1066–1083   
Neumann boundary conditions 1026, 1045,   
1056, 1057, 1063   
nonlinear diffusion equation 1047   
nonlinear instability 1037   
numerical dissipation or viscosity 1035   
operator splitting 1028, 1052, 1053, 1065   
outgoing wave boundary conditions 1026   
parabolic 1024, 1043   
periodic boundary conditions 1055, 1063   
piecewise parabolic method (PPM) 1043   
Poisson equation 1024, 1057   
rapid (Fourier) methods 620, 1029, 1054   
relaxation methods 1028, 1059–1066   
Schrodinger equation 1048, 1049¨   
second-order accuracy 1038–1042, 1045   
shock 1037, 1042, 1043   
sparse matrices from 76   
spectral methods 239, 1030, 1083–1096   
spectral radius 1061, 1066   
stability vs. accuracy 1035   
stability vs. efficiency 1027   
staggered grids 625, 1057   
staggered leapfrog method 1038, 1039   
successive over-relaxation (SOR) 1061–1066,   
1070   
time splitting 1052, 1053, 1065   
two-step Lax-Wendroff method 1040   
upwind differencing 1037, 1042   
variational methods 1030   
varieties of error 1036–1038   
von Neumann stability analysis 1033, 1034,   
1036, 1039, 1045, 1046   
wave equation 1024, 1031   
see also Elliptic partial differential equations;   
Finite difference equations (FDEs)   
rtial pivoting 43, 45, 535   
rtition-exchange 423, 433   
rtitioned matrix, inverse of 81, 82   
rty tricks 106, 203   
rzen window 657   
scal (language) 1   
th integration, for function evaluation   
251–254, 318

Path length, minimization of 555–562   
PAUP (software) 874   
PBCG (preconditioned biconjugate gradient method) 89, 1030   
PC methods see Predictor-corrector methods   
PCx (software) 548   
PDEs see Partial differential equations   
PDF (probability density function) see Statistical distributions   
Pearson’s r 745   
PECE method 944   
Penalty function 541   
Pentagon, symmetries of 1174   
Percentile 320, 419, 435   
Perfect code 852   
Period of linear congruential generator 343   
Periodic boundary conditions 1055, 1063   
Periodogram 653–657, 681, 683 Lomb’s normalized 685–687, 689 variance of 655, 656   
Perron’s theorems 221   
Perturbation methods for matrix inversion 76–79   
Peter Principle 427   
Phantom bit 9   
Phase error 1036   
Phase-locked loop 824   
Phi statistic 744   
Phillips-Twomey method 1006   
PHYLIP (software) 874   
Phylogenetic tree see Tree, phylogenetic   
$\pi$ , computation of 1185   
PI stepsize control 915   
Piecewise parabolic method (PPM) 1043   
Pigeonhole principle 387   
Pincherle’s theorem 222   
Pivot element 43, 46, 47, 967   
Pivoting 41, 43–45, 60, 76, 78, 101 and $\boldsymbol { Q R }$ decomposition 103, 105 for tridiagonal systems 57 full 43 implicit 44, 51 in $_ { L U }$ decomposition 50 in reduction to Hessenberg form 594 in relaxation method 967 Markowitz criterion 535 partial 43, 45, 46, 50, 535 threshold partial 535   
Pixel 631, 714, 715, 1010, 1017   
Planck’s constant 1048   
Plane rotation see Givens reduction; Jacobi transformation (or rotation)   
Plane, defined by triangle 1115   
Platykurtic distribution 723   
Plotting of functions 444, 1160–1163   
POCS (projection onto convex sets) 1012   
Point 1099–1101 closest approach of line to 1121 distance between two 1099 distance to line 1118 projection into plane 1115 random in triangle 1114 random on sphere 1129, 1130 test if inside box 1100 test if inside polygon 1124   
Poisson equation 631, 1024, 1057   
Poisson probability function 336–338, 390 as limiting case of binomial 338 deviates from 372–374, 686 moments of 725, 734 semi-invariants of 725 tails compared to Gaussian 778   
Poisson process 362, 369, 829, 830   
Polak-Ribiere algorithm 489, 517   
Poles see Complex plane, poles in   
Polishing of roots 459, 465, 471   
Polygon 1097, 1122–1127 area 1126 Bolyai-Gerwien theorem 1127 CCW vs. CW 1122 centroid of 1127 constructable by compass/straightedge 1127 convex vs. concave 1122 Jordan curve theorem 1124 pentagon, symmetries of 1174 removal of hidden 1150 routine for classifying 1125 simple vs. complex 1122, 1125 sum of exterior angles 1122 test if point inside 1124 winding number 1122–1124   
Polynomial interpolation 110, 118–120 Aitken’s algorithm 118 coefficients for 129–131 in Bulirsch-Stoer method 924 in predictor-corrector method 943 Lagrange’s formula 94, 118, 1089, 1092 multidimensional 132–135 Neville’s algorithm 118, 125, 166, 231, 924 pathology in determining coefficients for 130 Runge phenomenon 1090 smoothing filters 768 see also Interpolation   
Polynomials 201–205 algebraic manipulations 203 approximation from Chebyshev coefficients 241, 243 characteristic 469 characteristic, for digital filters 670, 676 characteristic, for eigenvalues of matrix 563, 583 Chebyshev 187 deflation 464–466, 471 derivatives of 202 division 95, 204, 464, 471 evaluation of 201, 202 evaluation of derivatives 202 extrapolation in Bulirsch-Stoer method 922, 924 extrapolation in Romberg integration 166 fitting 94, 129, 241, 243, 768, 788, 797

generator for CRC 1170 ill-conditioned 463 irreducible modulo 2 382 matrix method for roots 469 minimax 235, 248 modulo 2 381, 1169 monic 181 multiplication 203, 204 operation count for 203 order, distinct from degree 1170 orthonormal 181, 1087 parallel evaluation 205 primitive modulo 2 382–386, 406 roots of 227–229, 463–473 shifting of 243 stopping criterion in root finding 467 Population count of bits 16 Population vector 857 Portable random number generator see Random number generator Positive-definite matrix, testing for 101 Positivity constraints 526, 527 Postal Service (U.S.), barcode 1174 PostScript 1161 Powell’s method 489, 502, 509–514 Power (in a signal) 602 Power of 2 next higher 16, 361 test if integer is a 16, 611 Power series 201–205, 209–218, 246 economization of 243, 244 Pade approximant of 245–247 ´ Power spectral density see Fourier transform; Spectral density Power spectrum 655 Bartlett window 657 data windowing 655–660 estimation by FFT 652–667 figures of merit for data windows 658 Hamming window 658 Hann window 657 leakage 655, 656, 658, 662–665 mean squared amplitude 653 multitaper methods 662–667 normalization conventions 652, 653 overlapping data segments 660–662 Parzen window 657 periodogram 653–657 power spectral density 652 PSD 652 Slepian tapers 662–667 square window 656 sum squared amplitude 653 time-integral squared amplitude 653 variance reduction in spectral estimation 656 662 Welch window 658 Power spectrum estimation see Fourier transform; Spectral density PPM (piecewise parabolic method) 1043

Precedence of operators, in $\mathrm { C } { + } { + }$ 12   
Precision floating point 1164 multiple 1185–1193   
Preconditioned biconjugate gradient method (PBCG) 89   
Preconditioning, in conjugate gradient methods 1030   
Predictive stepsize control 939   
Predictor-corrector methods 900, 909, 934, 942–946 Adams-Bashforth-Moulton schemes 943 adaptive order methods 946 compared to other methods 942, 946 fallacy of multiple correction 943 functional iteration vs. Newton’s rule 944 multivalue compared with multistep 945, 946 Nordsieck method 944 starting and stopping 944 stepsize control 943, 944, 946 with fixed number of iterations 944   
Prerequisite relationship 23   
Primitive polynomials modulo 2 382–386, 406, 1170   
Principal component analysis (PCA) 892   
Principal directions 509, 512   
Principal solution, of inverse problem 1004   
Principal value integrals 178   
Prior probability 757, 775, 841, 1005 smoothness 1006   
Prize, $\$ 1000$ offer revoked 342   
Probability see Random number generator; Statistical tests; Statistical distributions   
Process loss 658   
Product Nystrom method 995   
Products, reaction 947   
Program(s) as black boxes 67, 255, 443, 507 dependencies 4 NR not a program library 2 typography of 14 validation 5   
Programming, NR not a textbook on 2   
Projection onto convex sets (POCS) 1011–1013 generalizations 1013   
Projection operator, nonexpansive 1012   
Prolongation operator 1068   
Proportional betting 758, 760   
Proposal distribution 826–828, 835   
Protocol, for communications 1168   
PSD (power spectral density) see Fourier transform; Spectral density; Power spectrum   
Pseudo-random numbers 340–386   
Pseudoinverse 70   
Pseudospectral method see Spectral methods   
Puns, particularly bad 35, 202, 946, 958, 1098   
Pure virtual class 34   
Pyramidal algorithm 702, 703   
Pythagorean theorem 1111   
Pythagoreans 494   
QO tree 1149–1158 applications of 1156–1158 intersecting objects 1150 use of hash in implementing 1151   
$\boldsymbol { Q R }$ decomposition 102–106, 483, 484, 486 and least squares 791 backsubstitution 103 operation count 103 pivoting 103 updating 105, 106, 483 use for orthonormal basis 74, 105 use for random rotation 1130 see also Eigensystems   
Quadratic convergence 64, 310, 452, 459, 511, 512, 522, 1185 equations 10, 227–229, 494, 572 interpolation 454, 466 programming 536, 884–886   
Quadrature 155–200 adaptive 155, 167, 194–196, 241, 995 alternative extended Simpson’s rule 160 and computer science 1160 arbitrary weight function 189–191, 995 Bode’s rule 158 Cauchy principal values 178 change of variable in 170–172, 995 Chebyshev fitting 156, 240, 241 classical formulas for 156–162 Clenshaw-Curtis 156, 241, 624, 625 closed formulas 157–160 cubic splines 156 DE rule 174 error estimate in solution 991 extended formula of order $1 / N ^ { 3 }$ 160 extended midpoint rule 161, 167 extended rules 159–162, 166, 993, 995, 997 extended Simpson’s rule 160 extended trapezoidal rule 159, 162 for improper integrals 167–172, 995–1000 for integral equations 988, 993 Fourier integrals 692–699 Fourier integrals, infinite range 699 functors and 22 Gauss-Chebyshev 183, 187, 625 Gauss-Hermite 183, 995 Gauss-Jacobi 183 Gauss-Kronrod 192, 195 Gauss-Laguerre 183, 995 Gauss-Legendre 183, 193, 990, 996 Gauss-Lobatto 191, 192, 195, 241, 624 Gauss-Radau 191 Gaussian integration 159, 179–193, 238, 296, 988, 990, 995, 1086–1089 Gaussian integration, nonclassical weight function 189–191, 995 IMT rule 173 infinite ranges 176–178 Monte Carlo 156, 197, 397–403, 410 multidimensional 156, 196–199

Newton-Cotes formulas 158, 179 Newton-Cotes open formulas 158, 159 open formulas 157–162, 167 oscillatory function 217 related to differential equations 155 related to predictor-corrector methods 943 Romberg integration 156, 166, 169, 231, 923, 994 semi-open formulas 160–162 Simpson’s rule 158, 165, 169, 698, 990, 994, 997 Simpson’s three-eighths rule 158, 995, 997 singularity removal 170, 171, 173, 995 singularity removal, worked example 999, 1000 TANH rule 173 trapezoidal rule 158, 160, 162, 166, 173, 175, 178, 695, 698, 989, 993 using FFTs 156 variable transformation 172–178 weight function log x 190, 191 see also Integration of functions Quadrature mirror filter 701, 708 Quadtree see QO tree Quantile changes with time 438 estimation 435 values 320, 419 Quantum mechanics, Uncertainty Principle 717 Quartet puzzling 882 Quartile value 419 Quasi-Newton methods for minimization 489, 521–525 Quasi-random sequence 403–410, 418, 1160, 1168 for Monte Carlo integration 408, 413, 418 Halton’s 404 Sobol’s 404–406 see also Random number generator Quicksort 420, 422–426, 429, 433 Quotient-difference algorithm 206

R (programming language) 3   
R-estimates 818   
Racetrack betting 757, 760   
Radial Basis Functions 139–144 Gaussian 142 inverse multiquadric 142 multiquadric 141 thin-plate spline 142 Wendland 142   
Radioactive decay 362   
Radix base for floating point arithmetic 592, 1164   
Radix base for floating-point arithmetic 1186, 1192   
Radix conversion 1181, 1185, 1192   
Ramanujan’s identity for $\pi$ 1193   
Random angle variables 364 bits 380–386 byte 352 point in triangle 1114 point on circle 1131 point on sphere 1129, 1130 rotation matrix 1130, 1131 variables, decorrelating 379 walk 10 walk, multiplicative 329   
Random deviates 340–386 angles 364 beta distribution 371 binomial 374–377 Cauchy distribution 367 chi-square distribution 371 exponential 362 $F$ -distribution 371 faster 377 gamma distribution 369 Gaussian 341, 364, 365, 368, 377, 686, 1004 integer range 343 logistic 363 multivariate Gaussian 378, 379 normal 341, 364, 365, 368, 377, 686 Poisson 372–374, 686 quasi-random sequences 403–410, 1160, 1168 Rayleigh 365 squeeze 368 Student’s-t distribution 371 sum of 12 uniform 377 trig functions 364 uniform 341–357   
Random number generator 32-bit limited 355–357 Box-Muller algorithm 364 combined generators 342, 345–352 Data Encryption Standard 358–361 Diehard test 345 floating point 354 for everyday use 351 for hash function 387 for integer-valued probability distribution 372 hash function 352 highest quality 342, 351 inheritance 23 lagged Fibonnaci 354 linear congruential generator 341, 343, 348 linear feedback shift register (LSFR) 346, 380–386 MLCG 341, 344, 348, 349 multiply with carry method (MWC) 347 NIST-STS test 345 nonrandomness of low-order bits 344 planes, numbers lie on 344 primitive polynomials modulo 2 382 pseudo-DES 358 quasi-random sequences 403–410, 1160, 1168 Quicksort use of 423 random bits 380–386 random byte 352 ratio-of-uniforms method 367–371 recommended methods 345–352 rejection method 365–368 simulated annealing method 551, 552 spectral test 344 subtractive method 354 successor relation 350, 352 system-supplied 342 timings 355 transformation method 362–365 trick for trigonometric functions 364, 367 uniform 341–357 xorshift method 345   
Random numbers see Monte Carlo; Random deviates   
RANDU, infamous routine 344   
Range 67, 68, 70   
Rank (matrix) 67 kernel of finite 992   
Rank (sorting) 419, 428–431   
Rank (statistics) 748–754, 818 Kendall’s tau 751–754 Spearman correlation coefficient 749–751 sum squared differences of 749   
Rank-nullity theorem 68   
Raphson, Joseph 456   
Rate equations 947, 948   
Ratio-of-uniforms method for random number generator 367–371   
Ratio variable (statistics) 741   
Rational Chebyshev approximation 247–251   
Rational function 110, 201–205, 245, 248, 670 approximation for Bessel functions 275 approximation for continued fraction 207, 260 as power spectrum estimate 681 Chebyshev approximation 247–251 diagonal 125 evaluation of 204, 205 extrapolation in Bulirsch-Stoer method 922 interpolation and extrapolation using 110, 124–128, 245, 247–251, 922 minimax 248, 249 response of recursive filter 670   
Rayleigh deviates 365   
RBF see Radial Basis Functions   
Reactions, chemical or nuclear 946–954 reaction products 947   
Realizable (causal) 668, 670, 671   
Rearranging see Sorting   
Reciprocal, multiple precision 1190   
Record, in data file 428   
Recurrence relation 219–223 and continued fraction 222 associated Legendre polynomials 294 Bessel function 219, 274, 275, 278, 283–285 binomial coefficients 258 Bulirsch-Stoer 125

characteristic polynomial of tridiagonal matrix 583, 665 Clenshaw’s recurrence formula 222, 223 continued fraction evaluation 207, 208 convergence 222 cosine function 219, 610 dominant solution 220 exponential integrals 219 gamma function 256 Golden Mean 11 hidden Markov model 861 Legendre polynomials 219 minimal vs. dominant solution 220 modified Bessel function 281 Neville’s 118, 231 orthonormal polynomials 181 parallel evaluation 223, 224 Perron’s theorems 221 Pincherle’s theorem 222 polynomial interpolation 118, 119, 231 random number generator 343 rational function interpolation 125 sequence of trig functions 219 sine function 219, 610 spherical harmonics 294 stability of 12, 220, 222, 223, 275, 278, 282, 294 trig functions 687 weight of Gaussian quadrature 183 Recursive doubling (parallel method) 223 Monte Carlo integration 410–418 multigrid method 1069 stratified sampling 416–418 Red-black see Odd-even ordering Reduction of variance in Monte Carlo integration 402, 410 Reed-Solomon code 852, 855 Berlekamp-Massey algorithm 852 syndrome decoding 852 References (explanation) 6 Reflection formula for gamma function 256 Regula falsi (false position) 449 Regularity condition 983 Regularization compared with optimal filtering 1008 constrained linear inversion method 1006 linear 1006–1013 nonlinear 1018 objective criterion 1009 of inverse problems 1002–1006 Phillips-Twomey method 1006 support vector machines 893 Tikhonov-Miller 1007 trade-off curve 1005 two-dimensional 1010, 1011 zeroth order 1002–1006 see also Inverse problems Regularizing operator 1004

Rejection method for random number generator 365–368   
Relative entropy 756   
Relaxation method automated allocation of mesh points 981–983 computation of spheroidal harmonics 971, 973–977 elliptic partial differential equations 1028, 1059–1066 example 971, 973–977 for algebraically difficult sets 970 for differential equations 957, 964–970 Gauss-Seidel method 1060, 1061, 1068, 1078 internal boundary conditions 983, 984 internal singular points 983, 984 Jacobi’s method 1060, 1061, 1068 successive over-relaxation (SOR) 1061–1066, 1070 see also Multigrid method   
Remes algorithms exchange algorithm 669 for minimax rational function 249   
Residual 63, 70, 88 in multigrid method 1067   
resize 27   
Resolution function, in Backus-Gilbert method 1014   
Response function 641–643, 649   
Responsibility matrix 842   
Restriction operator 1068   
Reward, $\$ 1000$ offer revoked 342   
Richardson’s deferred approach to the limit 166, 169, 231, 900, 911, 921, 922, 994, 1072 see also Bulirsch-Stoer method   
Richtmyer artificial viscosity 1042   
Ridders’ method for numerical derivatives 231 root finding 443, 449, 452–454   
Riemann shock problem 1043   
Riemann zeta function 211   
Right eigenvalues or eigenvectors 564, 565   
Rights management 5   
Rise/fall time 659   
Robust estimation 723, 778, 818–824 Andrew’s sine 821 average deviation 723 double exponential errors 820 Kalman filtering 824 Lorentzian errors 820 mean absolute deviation 723 nonparametric correlation 748–754 Tukey’s biweight 821 use of a priori covariances 824 see also Statistical tests   
Romberg integration 156, 166, 169, 231, 923, 994   
Root finding 181, 182, 442–486 advanced implementations of Newton’s rule 486 Bairstow’s method 466, 471

bisection 445, 447–449, 454, 460, 492, 584, 822 bracketing of roots 443, 445–447, 454, 455, 464, 465, 470 Brent’s method 443, 449, 453–456, 459, 786 Broyden’s method 474, 483–486 compared with multidimensional minimization 476, 477 complex analytic functions 466 convergence criteria 448, 475 deflation of polynomials 464, 471 double root 443 eigenvalue methods 469, 470 false position 449, 452, 454 Halley’s method 263, 264, 271, 335, 463 in complex plane 254 in one dimension 442 in relaxation method 964 in shooting method 956, 959 Jenkins-Traub method 470 Laguerre’s method 444, 466–469 Lehmer-Schur algorithm 470 Maehly’s procedure 465, 472 matrix method 469, 470 Muller’s method 466, 473 multidimensional 442, 459 multiple roots 443 Newton’s rule 182, 229, 443, 444, 456–462, 464, 466, 470–477, 539, 584, 944, 959, 964, 994, 1077, 1079, 1190, 1191 pathological cases 445, 457, 464, 474 polynomials 444, 463–473, 563 Ridders’ method 443, 449, 452–454 root polishing 459, 465, 470–473 safe Newton’s rule 460 secant method 449, 454, 466, 500 singular Jacobian in Newton’s rule 486 stopping criterion for polynomials 467 use of minimum finding 443 using derivatives 456 without derivatives 456 zero suppression 473 see also Roots Root polishing 459, 465, 470–473 Roots Chebyshev polynomials 233 cubic equations 228 multiple 443, 466 nonlinear equations 442–486 polynomials 444, 464, 563 quadratic equations 227 reflection in unit circle 676 square, multiple precision 1191 see also Root finding Rosenbrock method 934–940 compared with semi-implicit extrapolation 941 stepsize control 938 Rotation matrix 1097, 1130, 1131 Roundoff error 10, 11, 1163, 1164

bracketing a minimum 500 conjugate gradient method 1030 eigensystems 572, 573, 582, 584, 586, 591, 594 extended trapezoidal rule 165 general linear least squares 791, 795 graceful 1165 hardware aspects 1164 Householder reduction 581, 582 IEEE standard 1165 least-squares fitting 783, 791 Levenberg-Marquardt method 802 linear algebraic equations 38, 41, 43, 61, 72, 95 linear predictive coding (LPC) 680 magnification of 10, 11, 61 maximum entropy method (MEM) 683 multidimensional minimization 521, 525 multiple roots 464 numerical derivatives 229 recurrence relations 220 reduction to Hessenberg form 594 series 207, 210 straight line fitting 783 variance 724   
Row degeneracy 38 operations on matrix 42, 45 totals 743, 759   
RSS algorithm 416, 417   
RST properties (reflexive, symmetric, transitive) 440   
Run-length encoding 1180   
Runge-Kutta method 900, 901, 907–910, 935, 942, 1096 dense output 915 Dormand-Prince parameters 912, 920 embedded 911, 936 FSAL (first-same-as-last) 913 high-order 907–910, 912, 920 implementation 916–920 number of function evaluations 912 stepsize control 910–920   
Runge phenomenon 1090   
Rybicki, G.B. 96, 130, 183, 303, 634, 689, 717   
Sampling a distribution 825 importance 411, 412, 414 Latin square or hypercube 409, 410 Markov chain Monte Carlo 825 recursive stratified 416–418 stratified 412–414 uneven or irregular 685, 771   
Sampling theorem 178, 239, 605, 653 for numerical approximation 717–719   
Sande-Tukey FFT algorithm 616   
Savitzky-Golay filters for data smoothing 766–772 for numerical derivatives 232, 769   
ScaLAPACK 40   
Scallop loss 658   
Schrodinger equation 1048, 1049¨   
Schrage’s algorithm 344   
Schultz’s method for matrix inverse 64, 716   
Scilab (software) 3   
Scope, temporary 20, 21   
Searching an ordered table 114–118 selection 431–439 with correlated values 115   
Secant method 443, 449, 454, 466, 500 Broyden’s method 483–486 multidimensional (Broyden’s) 474, 483–48   
Second Euler-Maclaurin summation formula 16   
Second order differential equations 928, 930   
Seed of random number generator 343   
Selection 419, 431–439 by partition-exchange 433 find $m$ largest elements 434 for median 822 heap algorithm 434 in place 432, 439 incremental quantile estimation 435 largest or smallest 434 operation count 433, 439 single-pass 432 use to find median 726   
Semi-implicit Euler method 934, 940   
Semi-implicit extrapolation method 934, 935, 940, 941 compared with Rosenbrock method 941 stepsize control 941   
Semi-implicit midpoint rule 940   
Semi-invariants of a distribution 725   
Sentinel, in Quicksort 424, 433   
Separable kernel 992   
Separation of variables 292   
Sequence, alignment of by DP 559–562   
Sequential quantile estimation 435 changes with time 438   
Series 209–218 accelerating convergence of 177, 211–218 alternating 211, 216 asymptotic 210, 216 Bessel function $K _ { \nu }$ 288 Bessel function $Y _ { \nu }$ 284, 285 Bessel functions 210, 274 divergent 210, 211, 216 economization 243–245 $\epsilon$ algorithm 212 Euler’s transformation 211, 212 exponential integral 267, 269 Fresnel integral 298 geometric 211, 214 hypergeometric 252, 318 hyperlinear convergence 211 incomplete beta function 270 incomplete gamma function 259 Laurent 681, 682 Levin transformation 214 linear convergence 211 logarithmic convergence 211 relation to continued fractions 206 Riemann zeta function 211 roundoff error in 207 sine and cosine integrals 301 sine function 210 Taylor 456, 510, 900, 911, 965, 969 transformation of 211, 212 van Wijngaarden’s algorithm 217   
Set bits, counting 16   
Shaft encoder 1166   
Shell algorithm (Shell’s sort) 420–423   
Shepard interpolation 140   
Sherman-Morrison formula 76–79, 94, 483, 534   
Shifting of eigenvalues 563, 585, 596   
Shock wave 1037, 1042, 1043   
Shooting method computation of spheroidal harmonics 979 example 971, 977–981 for differential equations 956, 959–961, 971, 977–981 for difficult cases 962 interior fitting point 962   
Side information 760, 761   
Sidelobe level 658   
Sign bit in floating point format 8   
SIGN utility function 17   
Signal, bandwidth limited 605   
Significance (statistical) 727 of 2-d K-S test 763, 764 one- vs. two-sided 747 peak in Lomb periodogram 686, 687 two-tailed 730   
Similarity transform 566, 567, 570, 592, 594   
Simplex defined 502 method in linear programming 489, 502, 526–536, 548 method of Nelder and Mead 489, 502–507, 552, 821 use in simulated annealing 552   
Simplex method see Linear Programming   
Simpson’s rule 156, 158, 160, 165, 169, 698, 990, 994   
Simpson’s three-eighths rule 158, 995, 997   
Simulated annealing see Annealing, method of simulated   
Simulation see Monte Carlo   
Sinc expansion 178   
Sine function evaluated from tan. $\theta / 2 )$ / 219 recurrence 219 series 210   
Sine integral 297, 300–302 continued fraction 301 routine for 301 series 301 see also Cosine integral   
Sine transform see Fast Fourier transform (FFT); Fourier transform   
Singleton’s algorithm for FFT 637, 638   
Singular value decomposition (SVD) 39, 65–75 and least squares 65, 70, 73, 249, 791, 793 and rational Chebyshev approximation 249 approximation of matrices 74, 75 basis for nullspace and range 68 confidence levels from 816, 817 covariance matrix 817 fewer equations than unknowns 73 for inverse problems 1003 in minimization 512 more equations than unknowns 73, 74 of square matrix 69–73 relation to eigendecomposition 569, 570 use for ill-conditioned matrices 71, 73, 563 use for orthonormal basis 74, 105   
Singularities in integral equations 995–1000 in integral equations, worked example 999, 1000 in integrands 167, 173, 195, 995 of hypergeometric function 252, 253, 318 removal in numerical integration 170, 171, 173, 995   
Singularity, subtraction of the 996   
Six-step framework, for FFT 615   
size 27   
Skewness of distribution 723, 725   
Slack variables 529, 538, 888   
Slepian functions 662–667   
SMBus 1168   
Smith-Waterman algorithm 562   
Smoothing data 129, 766–772 in multigrid methods 1069 operator in integral equations 987   
Smoothness prior 1006   
sn function 316   
Sobol’s quasi-random sequence 404–406   
Soft-decision decoding 851–855 error correction 855 minimal trellis 853 trellis 853, 856 Viterbi algorithm 854   
Software engineering 2   
Sorting 419–441 bubble sort cautioned against 420 compared to selection 431 eigenvectors 575 Heapsort 420, 426–428, 434 index table 419, 426, 428–431 operation count 420, 422, 423 Quicksort 420, 422–426, 429, 433 rank table 419, 431 ranking 428–431 Shell’s method 420–423 straight insertion 420, 423, 575   
Source code, obtaining NR 3   
Sparse linear equations 39, 75–92, 534, 544, 548, 937 band-diagonal 58 Bartels-Golub update 535 biconjugate gradient method 88, 716 fill-in, minimizing 59, 76, 535, 544 in inverse problems 1011 indexed storage 82–87 minimum residual method 89 named patterns 76, 1028 partial differential equations 1028 relaxation method for boundary value problems 964 wavelet transform 700, 716 see also Matrix   
Spearman rank-order coefficient 749–751, 819   
Special functions see Function   
Spectral analysis see Fourier transform; Periodogram   
Spectral density one-sided PSD 602 periodogram 681, 683 power spectral density (PSD) 602, 603, 652 power spectral density per unit time 603 power spectrum estimation by MEM 681–684 two-sided PSD 603 see also Power spectrum   
Spectral lines, how to smooth 767   
Spectral methods 239, 1030, 1083–1096 analytic example 1084 and discontinuities 1083 and Gaussian quadrature 1087–1089 as finite difference methods 1093 cardinal functions 1089–1091 choice of basis functions 1085 collocation method 1086 contrasted with finite differencing 1083, 1085 differentiation matrix 1091 efficiency of 1083 exponential convergence of 1085 Galerkin method 1086 grid point representation 1090 interpolation of solution 1093 method of lines 1095 multidimensional equations 1095 nonlinear equations 1094 pseudospectral 1088 tau method 1086 variable coefficient equations 1094 worked example 1094, 1095   
Spectral radius 1061, 1066   
Spectral test for random number generator 344   
Spectrum see Fourier transform   
Speech recognition by hidden Markov model 866   
Sphere 1097, 1128–1130 2- vs. 3-sphere 1128 angular coordinates 1128 find all points within a 1109 intersection with line 1121 random point on 1129, 1130 surface area in $n$ -dimensions 1128 volume in $n$ -dimensions 1129   
Spherical Bessel functions 283 routine for 291   
Spherical coordinates 1128   
Spherical harmonics 292–297 basis functions for spectral methods 1085 fast transform 295, 297 orthogonality 292 routine for 294 stable recurrence for 294 table of 293 see also Associated Legendre polynomials   
Spheroidal harmonics 971–981 boundary conditions 972, 973 normalization 973 routines for 975–977   
Spline 111 cubic 120–124 gives tridiagonal system 122 interpolating 148 natural 122 operation count 122 two-dimensional (bicubic) 135   
Spread matrix 1015   
Square root complex 226 multiple precision 1191   
Square window 656   
Squeeze, for computing random deviates 368   
Stability 8–12 and stiff differential equations 932 Courant condition 1034, 1036, 1038, 1042, 1051 diffusion equation 1045, 1046 in quadrature solution of Volterra equation 994 mesh drift in PDEs 1040 nonlinear 1037 of Clenshaw’s recurrence 223 of Gauss-Jordan elimination 41, 43 of implicit differencing 932, 1046 of Markov model 858, 859 of polynomial deflation 464, 465 of recurrence relations 220, 222, 223, 275, 278, 282, 294 partial differential equations 1026, 1033 von Neumann analysis for PDEs 1033, 1034, 1036, 1039, 1045, 1046 see also Accuracy   
Stabilized Kolmogorov-Smirnov test 739   
Stabilizing functional 1004   
Stage, trellis 857   
Staggered leapfrog method 1038, 1039   
Standard (probable) errors 727, 781, 783, 786, 787, 790, 794, 807–817   
Standard deviation of a distribution 722, 723 of Fisher’s z 747 of linear correlation coefficient 746 of sum squared difference of ranks 750   
Standard Template Library (STL) containers 42   
State change vector 947   
Statistical distributions 320–339 beta 333, 334 binomial 338, 339 Cauchy 322, 323 chi-square 330, 331 density, change of variables in 362 exponential 326, 327 $F$ -distribution 332, 333 full conditional 827 gamma 331, 332 Kolmogorov-Smirnov 334–336 logistic 324–326 lognormal 328, 329 Lorentzian 322 normal 320, 321 Poisson 336–338 Student’s 323, 324 Weibull 327, 328   
Statistical error 778   
Statistical tests 720–772 Anderson-Darling 739 average deviation 723 bootstrap method 809, 810 chi-square 731–734, 742–745 contingency coefficient C 743, 744 contingency tables 741–745, 753, 758 correlation 721 Cramer’s V 743, 744 difference of distributions 730–740 difference of means 727 difference of variances 728, 730 entropy measures of association 758–761 F-test 728, 730 Fisher’s z-transformation 746 general paradigm 720 Kendall’s tau 749, 751–754 Kolmogorov-Smirnov 731, 736–738, 762, 819 Kuiper’s statistic 739 kurtosis 723, 725 L-estimates 818 linear correlation coefficient 745–748 Lucy’s $Y ^ { 2 }$ and $Z ^ { 2 }$ 735 M-estimates 818 mean 721–723, 725, 726 mean absolute deviation 723 measures of association 721, 741, 759 measures of central tendency 721–726 median 722, 725, 726, 818 mode 722, 725, 726 moments 721–726 nonparametric correlation 748–754 $p$ -value test 720 Pearson’s r 745 periodic signals 686, 687 phi statistic 744 R-estimates 818

rank correlation 748–754 robust 723, 749, 818–824 semi-invariants 725 shift vs. spread 739 significance 727 significance, one- vs. two-sided 730, 747 skewness 723, 725 small numbers of counts 734, 735 Spearman rank-order coefficient 749–751, 819 standard deviation 722, 723 strength vs. significance 727, 741 Student’s t 727–730, 746 Student’s t, for correlation 746 Student’s t, paired samples 729 Student’s t, Spearman rank-order coefficient 749 Student’s t, unequal variances 728 sum squared difference of ranks 749 tail test 720 Tukey’s trimean 818 two-dimensional 762–766 variance 721, 722, 724, 725, 729 Wilcoxon 818 see also Error; Robust estimation Statistics, higher-order 604 Steed’s method Bessel functions 283, 287 continued fractions 207 Steepest descent method 516 in inverse problems 1011 Step doubling 162, 174, 177, 910 tripling 168, 169 Stieltjes, procedure of 189 Stiff equations 901, 931–941 Kaps-Rentrop method 934 methods compared 941 predictor-corrector method 934 Rosenbrock method 934–940 scaling of variables 935 semi-implicit Euler method 940 semi-implicit extrapolation method 934, 935 semi-implicit midpoint rule 940 Stiff functions 111, 500 Stirling’s approximation 256, 1017 STL see Standard Template Library Stochastic simulation 946–954 when not to use 953 Stock market prices 329 Stoermer’s rule 928 Stopping criterion multigrid method 1078 polynomial root finding 467 Storage band-diagonal matrix 58 sparse matrices 82–87 Straight injection 1071 Straight insertion 420, 423, 575 Straight-line fitting 780–785

errors in both coordinates 785–787 robust estimation 822–824 Strassen’s fast matrix algorithms 107 Stratified sampling, Monte Carlo 412–414, 416 Strings, aligning by DP 559–562 struct see Class; Object Student-t deviates 371 Student’s probability distribution 323, 324 Cauchy as special case 323 normal as limiting case 323 Student’s t-test for correlation 746 for difference of means 727–730 for difference of means (paired samples) 729 for difference of means (unequal variances) 728 for difference of ranks 750 Spearman rank-order coefficient 749 Sturmian sequence 583 Sub-random sequences see Quasi-random sequence Subtraction, multiple precision 1186 Subtractive method for random number generator 354 Successive over-relaxation (SOR) 1061–1066 bad in multigrid method 1070 Chebyshev acceleration 1064 choice of overrelaxation parameter 1062–1064 Successor relation, random generators 350 Sum-product algorithm 867 Sum squared difference of ranks 749 Sums see Series Supernova 1987A 762 Support vector machine 883–898 dual formulation 886–889 kernel examples 891 kernel trick 889–892 linearly separable data 884 Mangasarian-Musicant variant 893–898 margin 884 regularization parameter 888, 893 SVMlight package 893 SVD see Singular value decomposition (SVD) SVM see Support vector machine SWAP utility function 17 Symbol, of operator 1070, 1071 Syndrome decoding coset leader 852 error-correcting codes 852 Golay code 852 Hamming code 852 perfect code 852 Reed-Solomon code 852 Synthetic division 95, 202, 243, 464, 471 Systematic errors 778 Tableau (interpolation) 118, 125 Tail test 720

Tangent function, continued fraction 206

TANH rule 173 infinite range 176   
Taylor series 229, 456, 510, 900, 911, 944, 965, 969   
Templates $( \mathbf { C } + + )$ ) 17, 22, 26, 419, 421   
Thermodynamics, and simulated annealing 550   
Thin-plate spline 142   
Three-dimensional array 36   
Threshold partial pivoting 535   
throw statement 30   
Tides 677   
Tikhonov-Miller regularization 1007   
Time domain 600   
Time reuse 952   
Time splitting 1052, 1053, 1065   
Timing, C routine for 355   
TNT parsimony software 882   
Toeplitz matrix 93, 96–99, 245 $_ { L U }$ decomposition 98 new, fast algorithms 99 nonsymmetric 96–98   
Tongue twisters 431   
Torus 400, 401, 408   
Trade-off curve 1002, 1016   
Transformation Gauss 310 Landen 310 method for random number generator 362–365   
Transforms, number theoretic 616   
Transition matrix directed graph 856 eigenvalues and eigenvectors 858, 859 Markov model 856   
Transition probability directed graph 856 Markov model 856   
Transport error 1037   
Transpose of sparse matrix 85   
Trapezoidal rule 158, 160, 162, 166, 173, 175, 178, 695, 698, 989, 993   
Traveling salesman problem 549, 551, 552   
Tree data structure 1097 KD see KD tree minimum spanning 1097, 1147 of boxes as data structure 1101 quadtree/octree see QO tree   
Tree, phylogenetic 868–882 additive 871 agglomerative clustering 874–882 branch length 870 corrected distance transformation 873 maximum likelihood 882 maximum parsimony 882 rooted vs. unrooted 871 search over topologies 882 software packages 874 ultrametric 871 UPGMA 877 WPGMA 877   
Trellis 853, 856 directed graph 856 maximum likelihood 854 stage 857   
Trellis coded modulation 855   
Triangle 1097, 1111–1116 angle between two 1116 area of 1111 centroid or barycenter 1113 circumscribed circle (circumcircle) 1112 in 3 dimensions 1114 inscribed circle (incircle) 1112 intersection with line 1121 plane defined by 1115 random point in 1114   
Triangulation and interpolation 132 applications of 1141–1149 definition 1131 Delaunay 1097, 1131–1149 hashing and 1136 incremental construction 1134 interpolation using 1141 largest minimum angle property 1134 minimum weight 1134 number of lines and triangles in 1132   
Tridiagonal matrix 56–61, 188, 567, 598 cyclic 79, 80 eigenvalues 576, 577, 583–589, 665 from cubic spline 122 from operator splitting 1066 in alternating-direction implicit method (ADI) 1066 in cyclic reduction 1057, 1058 parallel solution 57 reduction of symmetric matrix to 576–583 with fringes 1028 see also Matrix   
Trigonometric functions, $\tan ( \theta / 2 )$ as minimal 219 functions, recurrence relation 219, 687 interpolation 110 solution of cubic equation 228   
Trimming error 173   
Truncation error 11, 173, 500, 910, 911, 1163 exponentially decreasing 238 in multigrid method 1077 in numerical derivatives 229   
try 30   
Tukey’s biweight 821   
Tukey’s trimean 818   
Turbo codes 855   
Twenty questions 755, 758, 761   
Twin errors 1174   
Two-dimensional see Multidimensional   
Two-dimensional K–S test 762–766   
Two-pass algorithm for variance 724   
Two-point boundary value problems 900, 955–984

automated allocation of mesh points 981–983   
boundary conditions 955, 962, 977   
difficult cases 962   
eigenvalue problem for differential equations   
958, 973, 977–981   
free boundary problem 958, 983   
grid (mesh) points 957, 964, 981–983   
internal boundary conditions 983, 984   
internal singular points 983, 984   
linear requires no iteration 961   
multiple shooting 964   
problems reducible to standard form 958   
regularity condition 983   
relaxation method 957, 964–970   
relaxation method, example of 973–977   
shooting method 956, 959–961, 971, 977–981   
shooting method, example of 977–981   
shooting to a fitting point 962   
singular endpoints 962, 972, 978   
see also Elliptic partial differential equations   
o-sided exponential error distribution 820   
wo-sided power spectral density 603   
wo-step Lax-Wendroff method 1040   
pes used in NR 4, 25, 26   
Uchar 25   
Uint 25   
Ullong 25   
Ultrametric tree 871   
Uncertainty coefficient 761   
Uncertainty principle 717   
Underflow, in IEEE arithmetic 9, 1165   
Underrelaxation 1062   
Uniform deviates see Random deviates, uniform   
Unit-offset array 36   
Unitary (function) 1048, 1049   
Unitary (matrix) see Matrix   
Universal Product Code (UPC) 1174   
Unnormalized value 9   
Unsupervised learning 842, 868   
UPC checksum 1174   
UPGMA 877   
Upper Hessenberg matrix see Hessenberg matrix   
Upwind differencing 1037, 1042   
U.S. Postal Service barcode 1174   
Utility functions 17

V-cycle 1069   
valarray class 25   
Validation of Numerical Recipes procedures 5   
Valley, long or narrow 503, 509, 512, 516, 550, 552   
Van Cittert’s method 1011   
Van Wijngaarden-Dekker-Brent method see Brent’s method   
Vandermonde matrix 93–96, 130   
Variable length code 1176   
Variable metric method 489, 521–525 compared to conjugate gradient method 521   
Variable step-size integration 155, 167, 901, 924, 928–930, 938, 941, 943, 944, 946   
Variance(s) of distribution 721, 722, 725, 728–730 pooled 727 reduction of (in Monte Carlo) 402, 410 statistical differences between two 726–730 two-pass algorithm for computing 724 see also Covariance   
Variational methods, partial differential equations 1030   
Variogram 145, 837 various models for 837   
VecDoub , VecInt, etc. 26   
Vector angle between two 1120, 1121 $\mathrm { C } { + } { + }$ vector class 24 class for 24–29 contiguous storage for 27 of matrices 36 suffix _I , _O , _IO 26, 32, 36 see also Array; NRvector   
VEGAS algorithm for Monte Carlo 414–416   
Verhoeff’s algorithm for checksums 1174   
Viete’s formulas for cubic roots 228\`   
Viscosity artificial 1037, 1042 numerical 1035, 1042   
Viterbi decoding 850–855 as a min-sum algorithm 867 Bayesian nature of 868 compared to forward-backward algorithm 867 compared to hidden Markov model 867, 868 constellation 855 directed graph 850 state defined 850 training 867 transition 850 with arbitrary transition probability 867 with parameter re-estimation 867   
Volterra equations 988 adaptive stepsize control 995 analogy with ODEs 993 block-by-block method 994 first kind 988, 993 nonlinear 988, 994 second kind 988, 992–995 unstable quadrature 994   
von Neumann-Richtmyer artificial viscosity 1042   
von Neumann stability analysis for PDEs 1033, 1034, 1036, 1039, 1045, 1046   
Voronoi diagram 1097, 1142–1146 and Delaunay triangulation 1143 avoiding obstacles 1147   
Vowellish (coding example) 1176, 1181   
W-cycle 1069   
Wave equation 292, 1024, 1031   
Wavelet transform 699–716 and Fourier domain 707, 708 appearance of wavelets 706, 707

approximation condition of order $p$ 701 coefficient values 703, 704 contrasted with Fourier transform 699, 700, 711 Daubechies wavelet filter coefficients 700, 702, 704, 706–708, 715 detail information 701, 702 discrete wavelet transform (DWT) 702–706 DWT (discrete wavelet transform) 702–706 eliminating wraparound 703, 709 fast solution of linear equations 715, 716 filters 707, 708 for integral equations 989 image processing 713, 715 inheritance 23 inverse 703 JPEG-2000 712 Lemarie’s wavelet 708 mother-function coefficient 703 mother functions 700 multidimensional 712, 713 nonsmoothness of wavelets 707 of linear operator 715 on the interval 709 pyramidal algorithm 702, 703 quadrature mirror filter 701 smooth information 701, 702 truncation 711, 712 wavelet filter coefficient 700, 703 wavelets 700, 706, 707 Wavelets see Wavelet transform Weber function 254 Webnotes, Numerical Recipes 4 Weibull probability distribution 327, 328 Weighted Kolmogorov-Smirnov test 739 Weighted least-squares fitting see Least-squares fitting Weighting, full vs. half in multigrid 1071 Weights for Gaussian quadrature 179, 180, 995 nonclassical weight function 189–191, 995 Welch window 658 while iteration 14 Wiener filtering 645, 649–652, 673, 674, 767 compared to regularization 1008 Wiener-Khinchin theorem 602, 674, 682 Wilcoxon test 818 Winding number 1122–1124 Window function 660 Bartlett 657 flat-topped 658, 659 Hamming 658 Hann 657 Parzen 657 Slepian 662 square 656 Welch 658 Winograd Fourier transform algorithms 616 Woodbury formula 80, 81, 94 Wordlength 8, 12 WPGMA 877

Wraparound object for accessing vector 613 order for storing spectrum 611, 628, 632 problem in convolution 643   
Wronskian, of Bessel functions 283, 284, 287

X-ray diffraction pattern, processing of 1012   
Xorshift random number generator 345

Yale Sparse Matrix Package 76

Z-transform 670, 681   
Z-transformation, Fisher’s 746   
Zapf Dingbats 1162   
Zealots 1020   
Zebra relaxation 1070   
Zero contours 474   
Zero-offset array 36   
Zeroth-order regularization 1002–1006   
Zip code, barcode for 1174   
Ziv-Lempel compression 1176   
ZooAnimal (OOP example) 23   
Zoom transforms 615

# CAMBRIDGE UNIVERSITY PRESS and NUMERICAL RECIPES SOFTWARE

Coupon for Special Offer Number One

At a future time, this coupon will be exchangeable for a valuable benefit to owners of this Numerical Recipes, Third Edition book, ISBN 9780521866088. You must clip and mail this actual coupon, not a photocopy or fax. This coupon is valid only for Offer Number One, not for any other offer.

To find out about special offers, visit http://www.nr.com/specialoffers.html

# »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»» CAMBRIDGE UNIVERSITY PRESS and NUMERICAL RECIPES SOFTWARE

Coupon for Special Offer Number Two

At a future time, this coupon will be exchangeable for a valuable benefit to owners of this Numerical Recipes, Third Edition book, ISBN 9780521866088. You must clip and mail this actual coupon, not a photocopy or fax. This coupon is valid only for Offer Number Two, not for any other offer.

To find out about special offers, visit http://www.nr.com/specialoffers.html


<!-- chunk 0019: pages 1261-1262 -->
# CAMBRIDGE UNIVERSITY PRESS and NUMERICAL RECIPES SOFTWARE

Coupon for Special Offer Number Three

At a future time, this coupon will be exchangeable for a valuable benefit to owners of this Numerical Recipes, Third Edition book, ISBN 9780521866088. You must clip and mail this actual coupon, not a photocopy or fax. This coupon is valid only for Offer Number Three, not for any other offer.

To find out about special offers, visit http://www.nr.com/specialoffers.html

# »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»» CAMBRIDGE UNIVERSITY PRESS and NUMERICAL RECIPES SOFTWARE

Coupon for Special Offer Number Four

At a future time, this coupon will be exchangeable for a valuable benefit to owners of this Numerical Recipes, Third Edition book, ISBN 9780521866088. You must clip and mail this actual coupon, not a photocopy or fax. This coupon is valid only for Offer Number Four, not for any other offer.

To find out about special offers, visit http://www.nr.com/specialoffers.html
